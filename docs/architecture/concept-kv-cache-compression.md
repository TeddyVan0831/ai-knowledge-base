---
title: "KV Cache 动态压缩"
outline: deep
---

# KV Cache 动态压缩

> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 

## 摘要

KV Cache 动态压缩基于实证观察（注意力分布长尾，前 20% token 承载 >80% 权重），通过剔除不重要的 token 实现 50-90% 内存节省，主要方法包括重要性剔除、H2O、Scissorhands 和 StreamingLLM。

## 详情

### 核心原理

一个生成 token 对历史 token 的注意力权重是长尾分布：

```
帕累托定律：前 20% 的 token 承载 > 80% 的注意力权重
→ 剔除 80% 的低权重 token，内存节省 80%，质量损失可控
```

### Token 重要性评分

累积注意力权重：一个 token 被后续所有生成步骤"关注"的总次数越多，它越重要。

三种剔除策略：
- 硬阈值：保留 Importance > θ 的 token
- Top-K：保留最重要的 K 个 token
- 动态阈值：θ = μ - β·σ（均值减标准差）

### H2O（Heavy Hitter Oracle）

H2O 基于 Transformer 注意力的**累积注意力分数**识别"重要 token"：
- KV 缓存分两区：Heavy Hitter 区（保留累积注意力最高）+ Recent Window 区（保留最近 token）
- 驱逐策略：贪心驱逐不在两区中的 token
- 形式化为动态次模问题，有理论保证
- **不使用** Count-Min Sketch 等概率频率统计

### Scissorhands：自适应剪枝

核心观察：**重要性持久性假说**——在过去多个步骤中持续获得高注意力的 token，后续也大概率重要。
- 维护辅助缓存（CPU 内存），被驱逐的 token 可**重新准入**
- 固定内存预算管理，最高可减少 5× 内存，结合 4-bit 量化可达 20×

### StreamingLLM：滑动窗口 + 锚点

保留两类 token，丢弃中间：
1. 锚点 token：前 4 个（注意力汇聚点，防止分布崩溃）
2. 滑动窗口：最近 w 个

典型配置：Llama-2-7B 预训练 4096，KV Cache 容量 2048（4+2044），节省 87-93%。可稳定处理 400 万+ tokens。

### 压缩效果对比

| 方法 | 内存节省 | 质量影响 | 适用场景 |
|------|---------|---------|---------|
| 重要性剔除（保留 50%） | 50% | PPL + <5% | 通用 |
| H2O | 显著 | 可控 | 长文本 |
| Scissorhands | 显著（最高 20× 量化叠加） | 自适应 | 对话 |
| StreamingLLM（4+1024） | 87-93% | PPL + ~5% | 流式无限长 |

### 任务敏感性

| 任务 | 建议保留率 |
|------|-----------|
| 问答 | ≥70%（对剔除敏感） |
| 摘要 | ≥50%（中等敏感） |
| 翻译 | ≥40%（较不敏感） |

## 关联

- 相关概念: [KV Cache](/architecture/concept-kv-cache)、[KV Cache 量化](/architecture/concept-kv-cache-quantization)
- 相关实体: [vLLM](/inference-deploy/product-vllm)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)

## 引用来源

- [1]  — 第四章动态 KV Cache 压缩：H2O、Scissorhands、StreamingLLM、帕累托定律、任务敏感性

## 变更记录

- 2026-05-26: 初始创建，来源 
