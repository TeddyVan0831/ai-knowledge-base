---
title: "SGLang"
outline: deep
---

# SGLang

> **类型**: entity
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: , 

## 摘要
SGLang 是由 UC Berkeley LMSYS 团队开发的 LLM 推理引擎，通过 RadixAttention（基数树 KV 缓存复用）、PD 分离架构和压缩 FSM 等技术，在多轮对话、Agent 和复杂任务场景下实现最高 **6.4x**  的吞吐量提升。

## 详情

### 基本定位
- 定位：**复杂 LLM 程序运行时**，类似 Redis+Lua，解决"如何让业务逻辑跑得快"的问题 
- 适用场景：**多轮对话、Agent/CoT/RAG**、**高并发、低延迟的 API 服务** 
- 2025 年被 PyTorch 官方收编为生态项目 
- 开源协议：Apache 2.0 

### 核心创新：RadixAttention
- 核心数据结构：**基数树（Radix Tree）**，传统前缀树（Trie）的优化版，**每条边可标记不同长度的元素序列** 
- LRU 逐出策略：优先逐出最久未使用的叶子节点 
- 缓存感知调度：**根据匹配前缀长度排序，优先处理匹配前缀更长的请求** 
- 多轮对话前缀缓存命中率 **75-95%**，长上下文吞吐量是 vLLM 的 **2-5 倍** 
- 在 A10G GPU 上使用 Llama-7B 和 Mixtral-8x7B 模型测试，实现了**高达 5 倍的吞吐量提升**（对比 Guidance 和 vLLM）

### PD 分离架构（Prefill/Decode 解耦）
- **Prefill（预填充）**：**计算密集型（Compute-Bound）**，大量矩阵乘法，关键指标 TTFT 
- **Decode（解码）**：**内存带宽密集型（Memory-Bound）**，瓶颈在读取 KV Cache，关键指标 TPOT 
- 核心优势：两阶段物理隔离，Prefill 不再阻塞 Decode，TPOT 稳定；**首 Token 延迟可降低 60%** 
- Prefill 用小 Batch（算力已打满），Decode 用大 Batch（利用空闲算力）

### 压缩 FSM（约束解码）
- 传统约束解码每次只解码一个 token，效率低下 
- SGLang 将相邻的单次转换边压缩成单个边，**一次前向传递解码多个 token** 
- 示例：`{"summary": "` 原本需要 5 次解码，压缩后 **1 次前向传递完成** 
- JSON 生成比标准引擎**快 10 倍** 

### 性能对比

**官方基准测试（H100 单卡）**：
- 吞吐量：比 vLLM 高约 **29%**（**~16,200 vs 12,500 tok/s**）
- 百万日活场景下每月可省约 **$15,000 GPU 费用** 

**作者本地实验（RTX 4090, Qwen3-0.6B）**：
| 指标 | vLLM | SGLang | 对比 |
|------|------|--------|------|
| 单请求延迟(ms) | **1051.8** | **209.7** | **SGLang 快 5.0x**  |
| 共享前缀 20 请求(ms) | **1071.2** | **378.9** | **SGLang 快 2.8x**  |
| QPS (8并发) | **6.47** | **22.43** | **SGLang 高 3.5x**  |
| 吞吐(tok/s) | **647.2** | **2242.5** | **SGLang 高 3.5x**  |

> 实验表明，SGLang 在各种大型语言和多模态模型上的任务中，实现了**高达 6.4 倍的吞吐量提升**（NeurIPS 2024 正式版论文数据）

### 编程原语
| 原语 | 功能 |
|------|------|
| `function` | 定义一个函数  |
| `gen` | 生成文本或内容  |
| `select` | 从一组选项中选择最高概率的选项  |
| `fork` | 创建并行处理的分支  |

### 执行模式
- **解释器模式**：提示视为异步流，不等待生成完成即可继续 
- **编译器模式**：编译成计算图由图执行器执行 

## 关联
- 相关概念: [模型优化](/training-optimization/topic-model-optimization), [SGLang 深度优化：Radix 缓存与极致吞吐](/inference-deploy/concept-sglang-optimization), [模型优化](/training-optimization/topic-model-optimization), [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)
- 对比: [vLLM](/inference-deploy/product-vllm)

## 引用来源
- [1]  — 企业级 AI 部署：从硬件选型到框架选择（SGLang 框架介绍、性能对比、选型建议）
- [2]  — SGLang 深度优化：Radix 缓存与复杂任务的极致吞吐（PD 分离、RadixAttention、压缩 FSM、API 推测执行、5 大场景实战、vLLM vs SGLang 性能对比）

## 变更记录
- 2026-05-26: 初始创建，来源 , 
