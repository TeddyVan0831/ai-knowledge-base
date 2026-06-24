---
title: "KV Cache"
outline: deep
---

# KV Cache

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **领域**: ai

## 摘要

KV Cache（键值缓存）是自回归生成过程中缓存历史 token 的 Key 和 Value 的技术，避免重复计算，将复杂度从 O(L×S²×D) 降至 O(L×S×D)，但占用大量显存，是 LLM 推理的核心瓶颈。

## 详情

### 为什么需要 KV Cache

在自回归生成中，每生成一个新 token 都要计算它与之前所有 token 的注意力。不缓存会重复计算历史 token 的 Key 和 Value：

```
不用 KV Cache：O(L × S² × D)
用 KV Cache：  O(L × S × D)  ← 降一个数量级
```

### 内存占用公式

`Memory_KV = 2 × L × H_kv × S × D × b` 

| 符号 | 含义 |
|------|------|
| L | 层数 |
| H_kv | KV 头数（GQA/MQA 用 `num_key_value_heads`） |
| S | 序列长度 |
| D | 每头维度 |
| b | 数据类型大小（FP16=2 字节） |

### 实际案例

| 模型 | 参数 | L | H | D | 单 token | 2K context |
|------|------|---|---|---|---------|-----------|
| Llama-2-7B | 7B | 32 | 32 | 128 | 512KB  | ~1GB  |
| Llama-2-13B | 13B | 40 | 40 | 128 | 800KB  | ~1.6GB  |
| Llama-2-70B | 70B | 80 | 8（GQA） | 128 | ~320KB  | ~640MB  |

> **注意**：70B 使用 GQA，KV 头数=8，计算时必须用 `num_key_value_heads` 而非 `num_attention_heads`。Llama-3 全系列、Mistral、Qwen2 等也使用 GQA 。

### 批量推理的内存放大效应

7B 模型，batch=32，2K context ：
- KV Cache = 32 × 1GB = 32GB 
- 模型参数 = 14GB（FP16） 
- KV Cache 是模型参数的 2.3 倍！ 

### 六大优化方向

```
缓存复用层：Trie → Radix Tree → RadixAttention
存储管理层：PagedAttention（分页按需分配，浪费率 60-80%→~3%） 
动态压缩层：H2O / Scissorhands / StreamingLLM（内存节省 50-90%） 
量化存储层：FP16 → INT8/INT4（内存节省 50-75%） 
跨请求复用层：Prompt Registry / 多租户隔离 / 预热预取 
```

### 边缘设备的三大挑战

| 挑战 | 说明 | 后果 |
|------|------|------|
| 内存带宽限制 | 边缘设备带宽 10-50 GB/s  | 实际利用率仅 30-50% |
| 缓存层级小 | L3 通常 8-32MB  | KV Cache 远超容量，频繁访问 DRAM |
| 功耗约束 | DRAM 访问功耗是 SRAM 的 ~100 倍 | KV Cache 频繁访问 DRAM，功耗压力大 |

## 关联

- 相关概念: [KV Cache 动态压缩](/architecture/concept-kv-cache-compression)、[KV Cache 量化](/architecture/concept-kv-cache-quantization)、[AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai)
- 相关实体: [vLLM](/inference-deploy/product-vllm)、[SGLang](/inference-deploy/product-sglang)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)

## 引用来源

- [1]  — KV Cache 全景图、内存公式、GQA 影响、六大优化方向、边缘设备挑战

## 变更记录

- 2026-05-26: 初始创建，来源 
