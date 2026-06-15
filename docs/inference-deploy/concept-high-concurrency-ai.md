---
title: "AI 服务高并发原理与性能监控调优"
outline: deep
---

# AI 服务高并发原理与性能监控调优

> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 

## 摘要

AI 服务高并发的核心瓶颈在于 KV Cache 显存占用，PagedAttention 通过 GPU 显存的"虚拟内存"机制解决内存碎片和浪费问题。vLLM 通过 Continuous Batching 实现 GPU 利用率从 40-60% 提升到 85-95%。推测解码（Speculative Decoding）、MEDUSA、EAGLE 系列等加速技术可进一步提升推理吞吐量。

## 详情

### 一、KV Cache 内存瓶颈

在 Transformer 自回归生成中，为避免每步重复计算历史 token 的 Key 和 Value 张量，将其缓存起来 。

**KV Cache 显存占用计算（LLaMA-2-7B 为例）**：模型参数为隐藏维度 4096，层数 32，注意力头数 32，FP16 精度 。

```
每 token KV Cache = 2(K+V) × 32(层) × 4096(维度) × 2(FP16字节) = 524,288 字节 = 0.5 MB/token
上下文 4096 tokens = 4096 × 0.5 MB = 2 GB/请求
并发 100 请求 = 100 × 2 GB = 200 GB >> A100 80GB
```



**关键洞察**：模型参数本身只占 14GB，KV Cache 才是高并发场景下真正的显存杀手 。

### 二、KV Cache 三大瓶颈

**瓶颈 1：内存碎片**：
- 内部碎片：预分配最大长度，实际用不完。分配 2048 tokens，实际只用 500，剩余 1548 被浪费 
- 外部碎片：释放后中间空隙不连续。请求 A(0-500) + 请求 B(1000-1500)，中间 500-999 空闲但无法分配给需要连续内存的请求 C 

**瓶颈 2：动态长度导致浪费**："你好" → 100 tokens；"解释量子力学" → 2000 tokens。传统方案按最大长度预分配，每个都分配 2000 tokens → 平均利用率 < 30% 。

**瓶颈 3：Copy-on-Decoding 开销**：当使用 Beam Search 时，需将 KV Cache 完整复制到每个 beam 分支。每次复制量 = Beam Width(4) × 序列长度(1000) × 0.5MB = 2 GB，每生成一个 token 都要复制 2GB 数据 。

### 三、PagedAttention：GPU 显存的"虚拟内存"

**核心思想**：类比操作系统虚拟内存，不连续的物理页 → 连续的虚拟地址。PagedAttention：不连续的显存块（Block） → 逻辑上连续的序列。分割成固定大小 Block（通常 16 tokens/块），通过 Block Table 维护映射 。

**三大机制**：

**机制 1：按需分配（On-demand Allocation）**：
```
传统方式：启动时预分配 max_seq_len(2048) × 0.5MB = 1024 MB
PagedAttention：生成 1 个 token 才分配 1 个 block（16 tokens 容量）
示例：100 tokens 序列，需要 blocks = ceil(100/16) = 7 个，实际分配 = 7 × 16 × 0.5MB = 56MB
节省 = 94.5% 显存
```


**机制 2：写时复制（Copy-on-Write）**：
解决 Beam Search / Parallel Sampling 的显存爆炸问题。
```
传统：3 × 6 = 18 blocks（完整复制 3 份）
CoW：6 blocks(共享) + 3 blocks(私有) = 9 blocks，节省 50% 显存
```


**机制 3：动态重排（Dynamic Repacking）**：Continuous Batching 的关键，新请求到达时无需寻找连续的大块显存，只需收集分散的空闲 blocks 。

### 四、vLLM 架构实现

**Continuous Batching（动态填充）**：请求完成即刻腾出位置给新请求，GPU 永远满负荷运行，没有空闲浪费 。

**性能对比**：
| 指标 | 静态 Batch | Continuous Batching | 提升 |
|------|------------|---------------------|------|
| GPU 利用率 | 40-60% | 85-95% | 1.5-2x |
| 吞吐量 (tokens/s) | 800 | 1800 | 2.25x |
| 平均延迟 (P50) | 1200ms | 800ms | 1.5x |



> *注：以上为教学示例数据，展示 Continuous Batching 的典型改善范围。实际数值因模型、硬件和负载而异。* 

### 五、推测解码（Speculative Decoding）

**角色**：Target Model（目标模型）为待加速的大模型（如 70B），Draft Model（草稿模型）为用来帮助加速的小模型（如 7B）。

**核心思想**：小模型生成草稿 token，大模型一次性验证，只要草稿的平均命中 token 数 > 0，就有推理加速。数学上保证最终输出分布与原模型一致 。

**实验结果（T5-XXL 11B）**：

| 任务 | Draft 模型 | γ（候选数） | α（接受率） | 加速比 |
|------|------------|-------------|-------------|--------|
| ENDE | T5-SMALL | 7 | 0.75 | ~3x |
| CNNDM | T5-BASE | 5 | 0.73 | 3.0x |



原论文摘要报告的整体加速范围为 2X-3X 。

### 六、MEDUSA 推理框架

MEDUSA 方案：在原始模型上增加多个解码头（Multiple Decoding Heads），不做 Next-Token 预测，做 Next-Next-Token 预测 。

**Medusa-1 vs Medusa-2**：
| 维度 | Medusa-1 | Medusa-2 |
|------|----------|----------|
| 原理 | 冻结原 LLM 参数，仅训练新增解码头 | 联合微调主干模型 + Heads |
| 生成质量 | 无损 | 几乎无损 |
| 加速比 | ~2.2x | ~2.8x |



**Medusa Heads**：在 decoder 后面增加多个 LM_Head，可以并行预测出后 k 个 tokens 的候选。在原始模型基础上增加了 3 个额外的 Head，可以并行预测出后 4 个 token 的候选。Top-1 约 60% 太低，需构建 Tree Attention 。

**Tree Attention**：每层 Medusa Head 的 Top-k 候选组合成树状结构。Attention Mask 设计：每个 token 只能看到自己和祖先节点（不能看兄弟），保证因果关系正确 。

**Typical Acceptance（典型接受）**：接受"合理"的候选 —— 既不太意外（surprising），也不太无聊（predictable）。
- 太 predictable：条件概率过高，信息量太低。"Donald" → "Trump"（几乎必然）
- 太 surprising：条件概率极低，不合常理。"Donald" → "蘑菇"（太离谱）
- Typical（合理）：概率适中，自然且有信息量。"Donald" → "announced" 

判断方法：计算原始模型在当前位置的预测分布的熵 H（衡量不确定性），计算候选 token 的信息量 -log(p)，如果候选 token 的信息量接近 H 则接受，偏离太远则拒绝 。

### 七、EAGLE 推理框架

**三代演进**：
| 框架 | 核心创新 |
|------|----------|
| EAGLE (2024) | 特征级自回归（feature + token → feature → token） |
| EAGLE-2 (2024) | 上下文感知动态草稿树 |
| EAGLE-3 (2025) | 放弃特征预测，改为直接 token 预测；引入多层特征融合；峰值加速 6.5x |



**为什么特征比 Token 更好预测**：Token 层面离散、不连续、不确定性高；特征层面连续、规则、时间平滑性强 。

**EAGLE Draft Model**：
- 嵌入层 + LM Head：复用目标 LLM 参数，无需额外训练 
- 自回归头部：FC 层（降维）+ 解码器层（预测下一个特征）
- 可训练参数：7B 仅 0.24B，70B 仅 0.99B 
- 训练成本：70B 模型在 A100 40G 上 1-2 天 

**EAGLE 实验结果**：
| 模型 | 任务 | 温度 | 加速比 | 平均接受长度 τ |
|------|------|------|--------|---------------|
| Vicuna 7B | HumanEval | 0 | 3.33x | 4.29 |
| Vicuna 13B | HumanEval | 0 | 3.58x | 4.39 |
| LLaMA2-70B | HumanEval | 0 | 3.52x | 4.42 |



**EAGLE-2 实验结果**：
| 模型 | 温度 | EAGLE-2 加速比 | EAGLE-1 加速比 | 提升 |
|------|------|---------------|---------------|------|
| Vicuna 7B | 1 | 3.05x | ~2.5x | +20% |
| LLaMA2-70B | 1 | 4.26x | ~3.0x | +40% |



### 八、vLLM 性能监控与调优

**关键性能指标**：
| 指标 | 说明 | 健康阈值 |
|------|------|----------|
| TTFT（首 Token 时间） | 从请求到第一个 token 输出的时间 | < 500ms |
| TPOT（Token 间时间） | 相邻 token 输出的间隔 | < 50ms |
| GPU 利用率 | GPU 计算核心的实际使用率 | > 80% |



**调优策略矩阵**：
| 场景 | 策略 | 效果 |
|------|------|------|
| TTFT 过高 | `--max-num-batched-tokens` 增加，`--gpu-memory-utilization` 调高 | 容纳更多并发请求 |
| TPOT 波动大 | 减少 `--max-num-seqs`，降低批次大小 | 减少排队等待 |
| GPU 利用率低 | 增加 `--max-num-batched-tokens` 和 `--max-num-seqs` | 提高并行度 |
| OOM | 降低 `--gpu-memory-utilization`（默认 0.9），减少 `--max-model-len` | 释放 KV Cache 空间 |
| 延迟敏感 | 降低 `--max-num-seqs`，优先保证单请求速度 | 牺牲吞吐量换低延迟 |
| 吞吐敏感 | 提高 `--max-num-batched-tokens`，`--max-num-seqs` | 牺牲延迟换高吞吐 |



**推理加速技术汇总**：
| 技术 | 加速比 | 适用场景 | 部署复杂度 |
|------|--------|----------|------------|
| PagedAttention | 2-4x（内存效率） | 所有高并发场景 | 低（vLLM 内置） |
| Continuous Batching | 1.5-2.25x | 多请求并发 | 低 |
| 推测解码 | 1.5-3x | 单个大模型推理 | 中（需 Draft 模型） |
| MEDUSA | 2.2-2.8x | 单模型加速 | 中（需训练 Heads） |
| EAGLE | 2.7-3.5x | 单模型加速 | 低（轻量头） |
| EAGLE-2 | 3.0-4.3x | 单模型加速 | 低（无需额外训练） |



所有加速技术中，EAGLE-2 效果最强（3.0-4.3x），部署最简单（无需额外模型）。

## 关联

- 相关概念: [企业级 AI 部署：硬件选型与框架选择](/inference-deploy/concept-enterprise-ai-deployment) — 企业级 AI 部署：硬件选型与框架选择
- 相关概念: [SGLang 深度优化：Radix 缓存与极致吞吐](/inference-deploy/concept-sglang-optimization) — SGLang 深度优化：Radix 缓存与极致吞吐
- 相关概念: [投机解码（Speculative Decoding）](/architecture/concept-speculative-decoding) — 投机解码（Speculative Decoding）推理加速算法
- 相关概念: [TTFT 优化（首 Token 延迟）](/architecture/concept-ttft-optimization) — 首 Token 延迟（TTFT）优化技术
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops) — AI 部署与运维主题综述

## 引用来源

- [1]  — AI 服务核心：高并发原理与性能监控调优

## 变更记录

- 2026-05-26: 初始创建，来源 
