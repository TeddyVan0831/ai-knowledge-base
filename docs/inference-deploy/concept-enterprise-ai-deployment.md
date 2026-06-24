---
title: "企业级 AI 部署：硬件选型与框架选择"
outline: deep
---

# 企业级 AI 部署：硬件选型与框架选择

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **领域**: ai

## 摘要

企业级 AI 部署涉及从硬件选型（GPU 架构差异、内存墙问题、核心 GPU 型号对比）到推理框架选择（Ollama/vLLM/SGLang/TensorRT-LLM）的完整决策链路。2026 年硬件选型已从算力优先转向带宽优先 + 显存容量优先，LLM 推理的核心瓶颈是内存带宽而非算力。

## 详情

### 一、CPU vs GPU 架构差异

| 维度 | CPU | GPU |
|------|-----|-----|
| 设计初衷 | 处理顺序指令，擅长复杂逻辑控制和串行计算 | 并行矩阵运算 |
| 核心数 | 数十核，单核能力强 | 数千个小而高效的核心 |
| 举例 | — | H100 (SXM/NVL): 16,896 个 CUDA 核心 / (PCIe): 14,592 个；RTX 4090: 16,384 个 CUDA 核心；4090D: 14,592 个 CUDA 核心 |



**CUDA**：NVIDIA 推出的并行计算平台和编程模型（Compute Unified Device Architecture），CUDA 核心是 GPU 的基本计算单元 。

### 二、内存墙问题：LLM 推理卡在数据搬运

**三层存储架构**：
| 存储层 | 速度 | 容量 | 比喻 |
|--------|------|------|------|
| SRAM（共享内存） | 40TB/s+ 级聚合带宽（保守估计，实际依配置可达更高） | 每 SM 约 128KB（共享内存配置） | 芯片内的超高速小仓库 |
| HBM（高带宽内存） | 4.8-8TB/s | 80-288GB | 芯片外的大仓库 |
| DRAM（系统内存） | ~50GB/s | TB 级 | 远端仓库 |



**核心问题**：
- 大模型推理 **90% 的时间花在数据搬运而非计算上** 
- SRAM 计算极快，但 HBM 搬运速度比计算慢 50 倍以上 → GPU 算力被内存带宽卡死 
- 2026 年硬件选型逻辑已从**算力优先**转向**带宽优先 + 显存容量优先** 

**SRAM 的三大用途**：数据复用（Tiling）、并行归约、结果聚合与缓存 。

### 三、核心 GPU 型号对比

| 型号 | 架构 | 显存/带宽 | 定位 | 适用场景 |
|------|------|-----------|------|----------|
| H100 | Hopper | 80GB HBM3 / 3.35TB/s | 中流砥柱 | 7B-70B 训练/推理 |
| H200 | Hopper | 141GB HBM3e / 4.8TB/s | 内存怪兽 | 长上下文 >128K、70B+ 单卡 |
| B200 | Blackwell | 192GB HBM3e / 8TB/s | 下一代主力 | MoE、FP4 低精度、千卡集群 |
| B300 | Blackwell Ultra | 288GB HBM3e / 8TB/s | 显存之王 | 超大模型单卡承载 |
| L40S | Ada Lovelace | 48GB GDDR6 / 864GB/s | 推理黑马 | 放宽延迟的连续批处理 |
| RTX 4090 | Ada Lovelace | 24GB GDDR6X | 原型验证 | 1B-7B 本地调试 |



**架构代际**：Ada Lovelace (2022) → Hopper (2022) → Blackwell (2025) 。

### 四、选型建议

| 场景 | 推荐 | 说明 |
|------|------|------|
| < 7B 参数 | L40S 或 RTX 6000 Ada | H100 性能过剩 |
| 7B-30B 全参训练 | H100（FP8 + 梯度检查点） | 生态最成熟 |
| 30B-70B 推理 | H200（141GB 单卡跑 70B） | 避免多卡通信开销 |
| > 70B dense/MoE | B200（192GB + NVLink 5） | 显著缓解显存瓶颈 |
| 超长上下文 >128K | 训练选 B200，推理选 H200 | 性价比考量 |



**NVLink**：NVIDIA 的 GPU 间高速互联技术，多卡训练必需 。

### 五、Blackwell 架构的革命性变化

| 特性 | 说明 |
|------|------|
| FP4 精度 | 相比 FP8 内存占用减半，推理吞吐显著提升，精度损失可接受（具体提升比例因工作负载而异） |
| 第五代 NVLink | 带宽 1.8TB/s，适合千卡级超大规模训练 |
| 能效比 | GB200 超级芯片在特定推理场景下，能效比 H100 最高提升约 25 倍（取决于工作负载和量化精度）；B200 单卡推理性能约相当于 5 个 H100 节点 |



**B 系列 vs H 系列**：B 系列是专用 AI 芯片（大模型训练/推理更优），H 系列是通用计算芯片（气象模拟、分子动力学等科学计算仍更优）。

### 六、资源配比与功耗散热

**CPU 与内存的隐形瓶颈**：
- CPU 负责：并发请求调度、Tokenization、前后处理（JSON 解析、正则过滤）
- CPU/GPU 配比建议：**每 1 张 GPU 配 16-32 核 CPU + 512GB-1TB DRAM** 

**功耗与散热**：
| GPU | 功耗 | 散热 | 价格 |
|-----|------|------|------|
| RTX 4090 | 450W | 标准三风扇，满载 62-70°C | ~¥15,000-20,000 |
| RTX 5090 | 575-600W | 风冷可压但温度高（75-85°C） | ~¥20,000-25,000 |
| RTX 6000 Ada | 300W | 涡轮散热，满载 85°C | ~¥46,000 |
| B200 | 1000-1200W | 必须液冷 | 企业级 |



**个人购买建议**：
- **最推荐**：RTX 4090（24GB 可跑 13B-30B 量化，性价比优于 5090）
- **预算紧张**：二手 RTX 3090（24GB，约 ¥5,500-6,000）
- **不推荐**：RTX 6000 Ada（价格高约 50%，但在部分深度学习场景中与 4090 性能接近甚至略低，性价比不占优）

2026 年新建机房必须预留液冷基础设施，传统风冷已无法满足 Blackwell 集群需求 。

### 七、四大主流部署框架

| 框架 | 核心创新 | 适用场景 | 2026 最新动态 | 开源协议 |
|------|----------|----------|---------------|----------|
| vLLM | PagedAttention（页式 KV Cache 管理） | 高吞吐、大批量 Prompt | V1 架构重构，加入 PyTorch 基金会，生态最活跃 | Apache 2.0 |
| SGLang | RadixAttention（前缀树 KV 复用） | 多轮对话、Agent/CoT/RAG | 日处理数万亿 Token（官方数据），加入 PyTorch 生态 | Apache 2.0 |
| TensorRT-LLM | 硬件原生优化、自定义 CUDA 核 | 极致性能的 NVIDIA GPU 环境 | v1.0+ 原生支持 OpenAI 兼容 API | Apache 2.0 |
| Ollama | 极简封装（基于 llama.cpp） | 本地开发、边缘设备、CPU 推理 | 定位不变，适合快速验证 | Apache 2.0 |



**选型指南**：
- 新手/快速验证 → **Ollama**（2 分钟跑起来）
- 生产环境通用 → **vLLM**（生态最全，文档最丰富）
- 长上下文/Agent/多轮对话 → **SGLang**（前缀缓存复用率 90%+）
- 极致性能/已用 Triton → **TensorRT-LLM**（Blackwell 上 FP4 推理必需）

### 八、Ollama 的局限性

- **不支持 PagedAttention 与 Continuous Batching** → 高并发能力有限，更适合单用户调试 
- Go 的并发 ≠ 推理层的连续批处理。llama.cpp 主要为单用户本地运行设计，缺乏 PagedAttention 机制 
- Ollama 定位：**本地单用户调试工具**，不是生产级高并发服务 

### 九、vLLM 关键参数

| 参数 | 说明 |
|------|------|
| `--tensor-parallel-size N` | 在 N 个 GPU 上分布式运行 |
| `--max-model-len N` | 最大上下文长度 |
| `--enforce-eager` | 禁用 torch.compile。Qwen3 在 vLLM < 0.9.0 版本中必须加（否则 FakeTensorMode 报错），0.9.0+ 已修复。此参数会带来约 10-20% 性能损失 |
| `--gpu-memory-utilization` | 控制显存占用，默认 0.9 |
| `--quantization gptq` | 显式声明 GPTQ 量化 |



### 十、结构化输出

**Outlines 核心原理**：JSON Schema → 正则表达式 → 有限状态机（FSM）→ Token 级约束采样 。

**加速机制**：
1. FSM 合并（Coalescence）：把只有一个转移状态的节点合并，跳过不必要的采样步骤 
2. 字符 → Token 转换：将基于字符的 FSM 转为基于 Token 的 FSM，一次调用生成多个 token 

**与传统生成的对比**：传统需 n 轮调用生成 n 个 token，Outlines FSM 合并后只需 2-3 次调用即可生成完整 JSON 。

**DashScope 评估结果**：在官方评估测试集中，设置 `strict=true` 的结构化输出格式合规率达到 **100%**（格式合规率，不保证语义/计算正确性）。

**⚠️ 结构化约束保证格式合法，不保证语义正确**（如 total_price 计算错误需程序端重算）。

## 关联

- 相关概念: [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai) — AI 服务高并发原理与性能监控调优
- 相关概念: [SGLang 深度优化：Radix 缓存与极致吞吐](/inference-deploy/concept-sglang-optimization) — SGLang 深度优化：Radix 缓存与极致吞吐
- 相关概念: [llama.cpp 边缘推理框架](/inference-deploy/concept-llamacpp) — llama.cpp 边缘推理框架
- 相关概念: [NVIDIA 软件生态栈：cuBLAS / cuDNN / NCCL / TensorRT / NVLink](/tools-ecosystem/concept-nvidia-software-ecosystem), [CUDA：并行计算平台](/tools-ecosystem/concept-cuda-parallel-computing)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops) — AI 部署与运维主题综述
- 参见: [边缘推理框架全景](/inference-deploy/topic-edge-inference) — 边缘推理框架全景

## 引用来源

- [1]  — 企业级 AI 部署：硬件选型 + GPU 架构 + 内存墙 + 部署框架 + 结构化输出

## 变更记录

- 2026-05-26: 初始创建，来源 
