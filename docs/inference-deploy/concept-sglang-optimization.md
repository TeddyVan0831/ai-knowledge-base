---
title: "SGLang 深度优化：Radix 缓存与极致吞吐"
outline: deep
---

# SGLang 深度优化：Radix 缓存与极致吞吐

> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 

## 摘要

SGLang 是由 LMSYS 团队开发的复杂 LLM 程序运行时，与 vLLM 是互补关系：vLLM 跑模型，SGLang 跑业务逻辑。SGLang 的核心技术包括 PD 分离架构、RadixAttention 基数树缓存复用、压缩 FSM 约束解码和 API 推测执行，在多轮对话、Agent、结构化输出场景下实现高达 6.4 倍的吞吐量提升。

## 详情

### 一、SGLang vs vLLM 定位差异

| 维度 | vLLM | SGLang | 选型建议 |
|------|------|--------|----------|
| 定位 | 通用推理引擎（像 MySQL） | 复杂 LLM 程序运行时（像 Redis+Lua） | 简单对话用 vLLM；Agent/多轮/结构化输出用 SGLang |
| 缓存策略 | PagedAttention（块级复用） | RadixAttention（前缀树复用） | 多轮对话场景 SGLang 缓存命中率更高 |
| 编程方式 | OpenAI API 调用 | Python 原生嵌入（@function） | 需要复杂控制流（分支/循环/并行）选 SGLang |
| JSON 生成 | 靠 Prompt + 后校验 | 原生约束解码（正则强制） | 必须输出标准 JSON 的接口用 SGLang 更稳 |
| 兼容性 | OpenAI API 兼容 | OpenAI API 兼容 + SGLang 原生语法 | SGLang 也支持 OpenAI API，迁移成本低 |



**一句话总结**：vLLM 是跑模型的，SGLang 是跑业务逻辑的。简单问答用 vLLM；多轮对话、并行任务、严格 JSON 输出用 SGLang 。

### 二、PD 分离架构：Prefill/Decode 解耦

**为什么需要 PD 分离**：
| 对比维度 | Prefill（预填充） | Decode（解码） |
|----------|-------------------|----------------|
| 做什么 | 一次性处理整个 Prompt，计算所有 token 的 KV Cache | 逐个生成新 token（自回归） |
| 计算特性 | 计算密集型（Compute-Bound），大量矩阵乘法 | 内存带宽密集型（Memory-Bound），瓶颈在读取 KV Cache |
| 资源需求 | 高算力、高并行度 | 大显存、高带宽 |
| 关键指标 | TTFT（首 Token 延迟） | TPOT（Token 间延迟） |



**混合执行的问题**：Prefill 阻塞 Decode → TPOT 飙升（用户感觉卡顿）；Decode 时 GPU 计算单元大量空闲 → 浪费了 Prefill 需要的算力 。

**核心优势**：
| 优势 | 说明 |
|------|------|
| 消除干扰 | 两阶段物理隔离，Prefill 不再阻塞 Decode，TPOT 稳定 |
| 资源特化 | Prefill 用高算力 GPU，Decode 用大显存 GPU，各取所需 |
| 独立扩展 | 根据负载动态调整 P/D 实例比例 |
| Batching 差异化 | Prefill 用小 Batch（已是 Compute-Bound），Decode 用大 Batch（缓解 Memory-Bound） |



**为什么 Prefill 适合小 Batch，Decode 适合大 Batch**：
- Prefill：GPU 算力已打满，增大 Batch 只增加排队延迟 
- Decode：GPU 算力大量空闲，增大 Batch 利用空闲算力，从 Memory-Bound 转向 Compute-Bound 

### 三、四大优化技术叠加逻辑

| 技术 | 优化层面 | 解决的问题 | 核心方案 |
|------|----------|------------|----------|
| PagedAttention | 内存层 | KV Cache 碎片和浪费 | 块化按需分配，像虚拟内存 |
| Continuous Batching | 调度层 | GPU 空闲等待 | Token 级动态插入，完成即腾位 |
| 推测解码 | 算法层 | Decode 阶段 GPU 算力空闲 | 小模型猜 + 大模型验证 |
| PD 分离 | 架构层 | Prefill 和 Decode 互相干扰 | 两阶段物理隔离到不同 GPU |



**使用逻辑**：
- PagedAttention 是基础设施，贯穿 Prefill 和 Decode 两端，所有场景都需要 
- Continuous Batching 在 Prefill 和 Decode 集群内部各自运行，提升各自的 GPU 利用率 
- 推测解码只在 Decode 集群中使用（Decode 阶段是 Memory-Bound，最需要加速）
- PD 分离是最外层的部署策略，决定了上面三者在哪里运行 

### 四、SGLang 编程语言

SGLang 是一种为 LLMs 设计的结构化生成语言，用于简化和加速复杂语言模型程序的编程和执行 。

实验表明，SGLang 在各种大型语言和多模态模型上的任务中，实现了高达 6.4 倍的吞吐量提升（涵盖少样本学习、多轮对话、Agent 工作流、JSON 解码等多种工作负载，NeurIPS 2024 正式版论文数据）。

**SGLang 原语**：
| 原语 | 功能 |
|------|------|
| `function` | 定义一个函数 |
| `select` | 从一组选项中选择最高概率的选项 |
| `fork` | 创建并行处理的分支 |
| `gen` | 生成文本或内容 |



### 五、RadixAttention：基数树 KV 缓存重用

**核心数据结构：基数树（Radix Tree）** 是传统前缀树（Trie）的优化版：Trie 每条边标记单个元素，Radix Tree 每条边可标记不同长度的元素序列 → 大幅提升效率 。

KV 缓存以非连续、分页布局存储（Radix Tree 以 token 为单位管理节点映射，底层采用分页存储），LRU 逐出策略：优先逐出最久未使用的叶子节点 。

**缓存感知调度**：根据匹配前缀长度排序，优先处理匹配前缀更长的请求 。

根据 LMSYS 组织的研究，在 A10G GPU 上使用 Llama-7B 和 Mixtral-8x7B 模型进行的测试表明，与现有系统（如 Guidance 和 vLLM）相比，采用 RadixAttention 的 SGLang 系统实现了高达 5 倍的吞吐量提升 。

### 六、压缩 FSM：高效约束解码

传统约束解码每次只解码一个 token → 即使多个 token 可以同时满足约束条件 → 效率低下 。

SGLang 分析 FSM，将相邻的单次转换边压缩成单个边 → 识别何时可以一起解码多个 token 。

```
压缩前：状态 A --"{"→ 状态 B --"summary"→ 状态 C --":"→ 状态 D --" "→ 状态 E --"""→ 状态 F
压缩后：状态 A --'{"summary": "'→ 状态 F  （多个 token 合并为一条边）
```



**效果**：压缩转换边上的多个 token 可以在一个前向传递中解码 → 大大加速结构化输出生成 。

### 七、API 推测执行

针对黑盒 API 模型（如 GPT-4），无法修改内部 → 通过推测执行优化多调用程序 。

```
传统：gen("name") + gen("job") → 两次 API 调用 → 为相同的上下文 token 付费两次
SGLang：第一次 gen 启用推测执行 → 忽略停止条件继续生成额外 token → 缓存并重用
```



### 八、vLLM vs SGLang 性能对比（本地实验）

实验设置：模型 Qwen3-0.6B，硬件 RTX 4090 (24GB)，两个引擎均使用 40% GPU 显存 。

**vLLM 基线测试**：
| 基准项 | 结果 | 说明 |
|--------|------|------|
| 冷启动延迟 | 1482ms | 首次请求，无 KV Cache |
| 缓存命中延迟 | 1061ms (10 次平均) | 加速比 1.40x，Prefix Caching 生效 |
| 共享前缀 (20 请求) | 8722ms | 平均每请求 436ms |
| 并发吞吐 (8 并发) | QPS 6.41 / 吞吐 641.3 tok/s | 20 个请求，总耗时 3.12s |



**SGLang 性能测试**：
| 基准项 | 结果 | 说明 |
|--------|------|------|
| 冷启动延迟 | 315ms | 首次请求即极快 |
| 缓存命中延迟 | 222ms (10 次平均) | 最低 206ms，RadixAttention 高效复用 |
| 共享前缀 (20 请求) | 432ms | 平均每请求仅 21.6ms |



**直接对比**：
| 指标 | vLLM | SGLang | 对比 |
|------|------|--------|------|
| 单请求延迟 (ms) | 1051.8 | 209.7 | SGLang 快 5.0x |
| 共享前缀 20 请求并发 (ms) | 1071.2 | 378.9 | SGLang 快 2.8x |
| QPS (8 并发) | 6.47 | 22.43 | SGLang 高 3.5x |
| 吞吐 (tok/s) | 647.2 | 2242.5 | SGLang 高 3.5x |



> *注：5.0x 延迟差异中包含 Qwen3 thinking 模式（生成更多 token）和 vLLM --enforce-eager 因素，框架实际性能差距远小于此。* 

**为什么 SGLang 全面领先**：
- 共享前缀（2.8x）：SGLang 的 RadixAttention 通过 Radix 树自动识别 20 个请求的共同前缀，KV Cache 只计算一次；vLLM 的 Prefix Caching 是块级匹配，粒度不如 Radix 树灵活 
- 并发吞吐（3.5x）：SGLang 的缓存感知调度会优先处理命中率高的请求，叠加 RadixAttention 减少重复计算 

### 九、SGLang 环境准备

**强烈推荐使用 CUDA 12.4 镜像（官方推荐版本）！** CUDA 11.8 可能遇到各种兼容性问题 。

安装顺序：`sgl-kernel` → `sglang[all]` → `transformers==4.57.1` 。SGLang 与 vLLM 依赖冲突，需要使用独立环境 。

**RTX 4090 跑 Qwen3-8B 推荐配置**：
```
--mem-fraction-static 0.85 --max-running-requests 16 --context-length 4096 --chunked-prefill-size 2048 --enable-metrics
```


## 关联

- 相关概念: [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai) — AI 服务高并发原理与性能监控调优
- 相关概念: [企业级 AI 部署：硬件选型与框架选择](/inference-deploy/concept-enterprise-ai-deployment) — 企业级 AI 部署：硬件选型与框架选择
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops) — AI 部署与运维主题综述

## 引用来源

- [1]  — SGLang 深度优化：Radix 缓存与复杂任务的极致吞吐

## 变更记录

- 2026-05-26: 初始创建，来源 
