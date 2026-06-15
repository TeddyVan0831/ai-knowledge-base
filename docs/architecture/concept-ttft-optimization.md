---
title: "TTFT 优化（首 Token 延迟）"
outline: deep
---

# TTFT 优化（首 Token 延迟）

> **类型**: concept
> **创建时间**: 2026-06-02
> **最后更新**: 2026-06-02
> **来源**: 

## 摘要

TTFT（Time To First Token）是从用户按下发送键到屏幕跳出第一个字的等待时间。预填充阶段（Prefill）是 TTFT 的绝对主力（长序列占 90%+ ），优化方向包括并行化、算子融合、混合精度和 Chunked/Streaming Prefill。

## 详情

### TTFT 的四大组成部分

TTFT = T_preprocess + T_prefill + T_generate + T_overhead 。

| 场景 | T_prefill 占比 | 说明 |
|------|---------------|------|
| 短序列（<128 tokens） | 50-60%  | T_overhead 占 20-30%  |
| 中等序列（128-512） | 70-80%  | 预填充成为大头 |
| 长序列（>512） | 90%+  | 绝对主力 |

### 四大优化方向

1. **并行化**：序列级/张量级/流水线级并行 
2. **算子融合**：Flash Attention、LayerNorm-Linear 融合 
3. **混合精度**：敏感操作用高精度，不敏感的用低精度 
4. **Chunked/Streaming Prefill**：把长序列切块，边处理边返回，O(n) 延迟降到 O(n/k) 

### 关键影响因素

**输入预处理（T_preprocess）**：Tokenization（15-20%）+ Embedding 查找（60-70%，瓶颈！）+ 位置编码（10-15%）。

**预填充阶段（T_prefill）**：处理完整个输入序列，生成 KV Cache。是计算密集（compute-bound）而非内存密集（memory-bound）操作，因为注意力计算 O(n²) 的 FLOPs 很高 。

### 混合精度预填充

不同操作对精度敏感度不同：
- **高精度必需**：LayerNorm、注意力 softmax、logits 计算
- **低精度可用**：线性层权重、KV Cache 存储

通过混合精度，可以在保持质量的同时减少内存占用和计算时间 。

### Chunked/Streaming Prefill

核心思路：将长序列切成 k 块，每块处理完后返回一个 partial result，将 O(n) 延迟降到 O(n/k) 。

## 关联

- 相关概念: [KV Cache](/architecture/concept-kv-cache), [注意力机制优化](/architecture/concept-attention-optimization), [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai), [SGLang 深度优化：Radix 缓存与极致吞吐](/inference-deploy/concept-sglang-optimization)
- 相关实体: [vLLM](/inference-deploy/product-vllm), [SGLang](/inference-deploy/product-sglang)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops), [模型优化](/training-optimization/topic-model-optimization)

## 引用来源

- [1]  — TTFT 组成分析、预填充优化、混合精度、Chunked/Streaming Prefill

## 变更记录

- 2026-06-02: 初始创建
