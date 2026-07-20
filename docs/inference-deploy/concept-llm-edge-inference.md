---
title: "LLM 边缘推理综述"
outline: deep
---

# LLM 边缘推理综述

> **创建时间**: 2026-06-23
> **最后更新**: 2026-06-23
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-06-23
> **最后更新**: 2026-06-23
> **来源**: 
> **领域**: ai

## 摘要

基于 ACM Computing Surveys 2026 顶刊综述（arXiv:2604.22906），首次以跨层系统视角梳理 LLM 边缘推理全景：从四类协作架构（单节点→纵向→横向→混合）到三大根问题（KV缓存滚雪球、预填/解码分裂、无线不稳定），覆盖量化/剪枝/蒸馏等模型压缩、连续批处理/PagedAttention 等资源调度、以及 NPU 产品规划建议。核心主张是边缘推理 = 架构选型→模型适配→资源分配三步闭环。

## 详情

### 核心问题

LLaMA-70B 仅 FP16 权重需约 140GB，远超单一边缘设备承载能力。云推理有延迟/隐私/带宽三重约束；纯设备端受限于单机内存与功耗。边缘推理 = 设备+近边缘+云三者协同。

### LLM 推理基础

**Decoder-only 已成主流架构**。推理分两阶段不对称计算 ：
- **Prefill（预填充）**：一次性处理输入提示词，计算密集矩阵乘法 → compute-bound
- **Decode（解码）**：逐 token 生成，反复读 KV 缓存 → memory-bound

### 四类协作架构

| 架构 | 机制 | 优势 | 局限 | 论文来源 |
|------|------|------|------|---------|
| 单一边缘节点 | 单服务器部署量化 LLM | 低协调开销、隐私好 | 受单机内存/算力限制 | §3.1 |
| 纵向协作 | LLM 切分到设备→边缘→云 | 弹性容量、低感知延迟 | 带宽敏感、编排复杂 | §3.2 |
| 横向协作 | 同层多设备 TP/PP/DP 并行 | 突破单机上限 | 设备间链路敏感 | §3.3 |
| 混合协作 | 纵向+横向同时协作 | 终极方案 | KV 缓存跨节点迁移复杂 | §3.4 |

选型核心原则：能本地就本地，不行就近找人，还不行送云端。

### 八大挑战（§3.5）

论文列出 8 个独特挑战：有状态推理、两阶段不对称、大规模参数、设备异构、数据异构、不确定资源需求、时变无线信道、移动性和间歇连接。其中三个根问题互为放大循环 ：

1. **KV 缓存"滚雪球"**：多用户并发每人一份，碎片化导致 OOM
2. **预填/解码"精神分裂"**：同一台机既要扛计算又要扛内存
3. **无线网络不确定性**：丢包/抖动/延迟波动是常态

### 模型压缩技术

| 技术 | 关键指标 | 代表方法 |
|------|---------|---------|
| 量化（§4.1.1） | AWQ >3× vs FP16，保留 1% 显著权重 | AWQ, LLM.int8(), SmoothQuant |
| 剪枝（§4.1.2） | SparseGPT >50% 稀疏，无需重训 | SparseGPT, Wanda, Sheared-LLaMA（仅 3% 重训量） |
| 蒸馏（§4.1.3） | MiniLM 参数减半保留 >99% 精度 | MiniLM, FUSELLM, Fine-tune-CoT |
| 低秩分解（§4.1.4） | 从 O(mn) 降到 O((m+n)×r) | ASVD, DSFormer（压缩率高 40%） |



### 解码加速

| 技术 | 核心原理 | 关键数据 |
|------|---------|---------|
| 推测解码 | 小草案模型→大模型并行验证 | Sun 2023 额外 1.37× |
| 级联推理 | 设备小模型↔云端大模型自适应路由 | 减少大模型调用 ~40% |
| 提前退出 | 中间层置信度提前停止 | LayerSkip 层丢弃+自推测 |
| Agentic AI | Plan-Act-Observe 循环+边缘部署 | 轻量设备端+计算密集云 |



### 资源调度技术链

演进路线（里程碑指标均来自论文原文）：

```
静态批处理 → 动态批处理 → 连续批处理(Orca: 36.9×)
  → 分页KV(vLLM: 2-4×+ vs Orca) → 分块预填充(Sarathi: 最高 3.7×)
```

| 系统 | 技术路线 | 关键指标 |
|------|---------|---------|
| Orca (2022) | 连续批处理 | 吞吐量 ×36.9 |
| vLLM (2023) | PagedAttention | 比 Orca 高 2-4× |
| FlexGen (2023) | GPU+CPU+SSD 卸载 | 单卡推理 OPT-175B（1 tok/s, bs=144） |
| Sarathi-Serve (2024) | 分块预填充 | 容量比 vLLM 最高 3.7×（Yi-34B） |

### NPU 产品建议（推演）

基于论文约束推导的硬件设计建议：
- **标配**：INT4/8 混合精度 + 分页内存控制器 + 注意力加速器
- **护城河**：稀疏计算引擎（2:4 N:M）+ 多芯片低延迟互联 + 双模推理（草案/验证）
- **预研**：AirComp 分布式推理 + 5G 基带融合、Agentic AI 多任务并发



### 评估方法论（§6）

论文 §6 定义六大评估指标维度 ：

| 维度 | 核心指标 | 边缘特殊考量 |
|------|---------|-------------|
| 延迟 | TTFT / E2EL / TPOT | 无线抖动→尾延迟尖峰 |
| 吞吐 | TPS / RPS / E2ET | 预填/解码分别报告 |
| 有效吞吐 | SLO 约束下的合规请求占比 | 网络波动下原始 TPS 高但 Goodput 低 |
| 能效 | TPJ / RPJ | 单次 ChatGPT 查询 ~0.34 Wh |
| 内存 | 模型占用 + KV缓存 + 峰值推理内存 | 长上下文下 KV 缓存主导 |
| 推理质量 | 准确率 / 幻觉率 / 偏见毒性 | 紧凑压缩模型对幻觉敏感 |

**评测模型**：8 家族（LLaMA/Mistral/Gemma/Qwen/Phi/OPT/TinyLLaMA/DeepSeek-Coder）

**数据集四象限**（S=Short ≤1000 tokens, L=Long >1000）：
- S↔S（MMLU/HellaSwag）→ 准确率
- S↔L（GSM8K/HumanEval CoT）→ 输出质量+TPOT
- L↔S（LongBench QA）→ 内存+KV 扩展
- L↔L（文档摘要）→ 吞吐压力

**评估平台**：硬件仿真（gem5）→系统仿真（TVM/MLPerf）→网络仿真（ns-3）→真实设备（Jetson/手机）

### 未来方向（§7）

论文 §7 识别三大前沿 ：

1. **多模型/多模态边缘服务**：Qwen2-VL、LLaVA-1.5 等 VLM 的 edge-native 部署
2. **安全隐私保护执行**：四类边缘攻击面 + 定制化缓解策略
3. **绿色推理**：单次查询碳排放驱动，能效与延迟并列为边缘系统同等 KPI

## 关联

- 相关概念: [llama.cpp 边缘推理框架](/inference-deploy/concept-llamacpp), [MediaPipe LLM 推理框架](/inference-deploy/concept-mediapipe-llm), [MNN 边缘推理框架](/inference-deploy/concept-mnn), [企业级 AI 部署：硬件选型与框架选择](/inference-deploy/concept-enterprise-ai-deployment)
- 相关概念: [后训练量化（PTQ）](/training-optimization/concept-quantization-ptq), [投机解码（Speculative Decoding）](/architecture/concept-speculative-decoding), [KV Cache](/architecture/concept-kv-cache)
- 相关概念: [模型剪枝与稀疏化](/training-optimization/concept-model-pruning), [知识蒸馏](/training-optimization/concept-knowledge-distillation), [TTFT 优化（首 Token 延迟）](/architecture/concept-ttft-optimization)
- 参见: [边缘推理框架全景](/inference-deploy/topic-edge-inference), [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)
- 相关概念: [NVIDIA Jetson Orin 与 Thor 全系对照（跨代归一化）](/inference-deploy/concept-nvidia-jetson-orin-thor)（Jetson Orin/Thor 边缘硬件平台）, [LPDDR5/5X 内存带宽、容量与 ECC 全解](/base-models/concept-lpddr-ecc)（边缘内存带宽与 ECC）, [算力口径方法论：单位 × 精度 × 计算模式](/base-models/concept-ai-compute-caliber)（边缘算力口径）, [ARM 处理器 IP 全谱系与车规 CPU 对比（A78AE vs V3AE）](/base-models/concept-arm-cpu-ip-lineage)（车规 CPU 全大核同构）

## 引用来源

- [1]  — ACM Computing Surveys 2026 综述：四类协作架构、八大挑战、模型优化、资源调度、NPU 规划

## 变更记录

- 2026-06-23: 初始创建，来源 
- 2026-06-23: 笔记 v2→v4 更新同步——新增评估方法论（六大指标/四象限数据集/四类平台）和未来方向（多模态/安全/绿色推理），补充 13 处行号引用
