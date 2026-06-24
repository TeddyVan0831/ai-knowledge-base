---
title: "vLLM"
outline: deep
---

# vLLM

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: , 
> **类型**: entity
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: , 
> **领域**: ai

## 摘要
vLLM 是由伯克利大学 LMSYS 组织开源的高吞吐 LLM 推理框架，核心创新为 PagedAttention（页式 KV Cache 管理）与 Continuous Batching，显著提升 GPU 利用率与服务吞吐量。

## 详情

### 基本定位
- 定位：**通用推理引擎**，类似 MySQL，解决"如何让模型跑得快"的问题 
- 适用场景：**生产环境通用**、**高吞吐、大批量 Prompt** 
- 生态：加入 PyTorch 基金会，**生态最活跃**、**支持模型最多、文档最全、国内头部厂商广泛采用** 
- 开源协议：Apache 2.0 

### 核心创新：PagedAttention
- 类比操作系统虚拟内存：**不连续的显存块（Block） → 逻辑上连续的序列** 
- 分割成固定大小 Block（通常 **16 tokens/块**），通过 Block Table 维护映射 
- 三大机制：
  1. **按需分配**：100 tokens 序列，需要 7 个 blocks，实际分配 56MB，传统方式 1024MB，**节省 94.5% 显存** 
  2. **写时复制（Copy-on-Write）**：Beam Search / Parallel Sampling 场景，共享部分只存一份，**节省 50% 显存** 
  3. **动态重排（Dynamic Repacking）**：Continuous Batching 的关键 

### Continuous Batching
- 粒度细化到 Token 级别，**请求完成即刻腾出位置给新请求** 
- **Iteration-level Scheduling**：每生成一个 token 后就调度，传统方案是整个 batch 完成后才调度 
- 性能提升（教学示例数据）：

| 指标 | 静态 Batch | Continuous Batching | 提升 |
|------|-----------|---------------------|------|
| GPU 利用率 | **40-60%**  | **85-95%**  | 1.5-2x |
| 吞吐量 (tokens/s) | **800**  | **1800**  | 2.25x |
| 平均延迟 (P50) | **1200ms**  | **800ms**  | 1.5x |

### 关键性能指标
| 指标 | 健康阈值 |
|------|---------|
| **TTFT**（首 Token 时间） | **< 500ms**  |
| **TPOT**（Token 间时间） | **< 50ms**  |
| **GPU 利用率** | **> 80%**  |

### 推理加速技术汇总
| 技术 | 加速比 | 适用场景 |
|------|--------|---------|
| **PagedAttention** | **2-4x（内存效率）**  | 所有高并发场景 |
| **Continuous Batching** | **1.5-2.25x**  | 多请求并发 |
| **推测解码** | **1.5-3x**  | 单个大模型推理 |

### 基本使用
```bash
vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \
    --tensor-parallel-size 2 \
    --max-model-len 32768 \
    --enforce-eager
```

### 关键参数
| 参数 | 说明 |
|------|------|
| `--tensor-parallel-size N` | 在 N 个 GPU 上分布式运行  |
| `--max-model-len N` | 最大上下文长度  |
| `--enforce-eager` | 禁用 torch.compile（约 **10-20% 性能损失**） |
| `--gpu-memory-utilization` | 控制显存占用，默认 0.9  |

## 关联
- 相关概念: [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai), [SGLang 深度优化：Radix 缓存与极致吞吐](/inference-deploy/concept-sglang-optimization), [KV Cache](/architecture/concept-kv-cache), [KV Cache 动态压缩](/architecture/concept-kv-cache-compression), [KV Cache 量化](/architecture/concept-kv-cache-quantization)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)
- 对比: [SGLang](/inference-deploy/product-sglang)

## 引用来源
- [1]  — 企业级 AI 部署：从硬件选型到框架选择（vLLM 框架介绍、PagedAttention、Continuous Batching、关键参数）
- [2]  — AI 服务核心：高并发原理与性能监控调优（KV Cache 瓶颈、PagedAttention 三机制、性能指标、调优策略、推测解码、MEDUSA、EAGLE）

## 变更记录
- 2026-05-26: 初始创建，来源 , 
