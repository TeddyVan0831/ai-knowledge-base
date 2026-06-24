---
title: "Qwen3-Embedding 系列"
outline: deep
---

# Qwen3-Embedding 系列

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **类型**: entity
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **领域**: ai

## 摘要

Qwen3-Embedding 是阿里巴巴 Qwen 系列文本嵌入模型，在 MTEB 榜单中 8B 版本以 Mean Score 70.58 排名第 2，是当前开源 Embedding 模型中的性能标杆。

## 详情

### MTEB 榜单表现

| 模型 | 维度 | 最大 Token | Mean Score | 排名 |
|------|------|-----------|------------|------|
| Qwen3-Embedding-8B  | 4096  | 32768  | 70.58  | 2 |
| Qwen3-Embedding-4B  | 2560  | 32768  | 69.45  | 3 |
| Qwen3-Embedding-0.6B  | 1024  | 32768  | 64.34  | 4 |

### 关键特性

- **上下文窗口**：32768 tokens（全系列一致），支持长文档检索
- **维度覆盖**：1024 维（轻量）→ 4096 维（旗舰）
- **性价比**：0.6B 小模型 Mean Score 64.34，适合资源受限场景

### 选型建议

| 场景 | 推荐模型 | 理由 |
|------|---------|------|
| 高精度 RAG | Qwen3-Embedding-8B | Mean Score 70.58，语义最丰富 |
| 移动端/边缘部署 | Qwen3-Embedding-0.6B | 1024 维，推理速度快 |
| 平衡场景 | Qwen3-Embedding-4B | 2560 维，Mean Score 69.45 |

### MTEB 基准背景

MTEB (Massive Text Embedding Benchmark) 涵盖 **8 大类任务**和 **58 个数据集**，任务类型包括：检索（Retrieval）、STS（语义文本相似度）、重排序（Reranking）、分类（Classification）、聚类（Clustering）、对分类（Pair Classification）、双语挖掘（Bitext Mining）、摘要（Summarization）。

## 关联

- 相关概念: [Embedding（嵌入）](/base-models/concept-embedding)、[Embedding 模型选型](/base-models/concept-embedding-model-selection)
- 相关实体: [Jina Embeddings V4](/base-models/model-jina-embedding)、[BGE-M3](/base-models/model-bge-m3)
- 参见: [模型优化](/training-optimization/topic-model-optimization)

## 引用来源

- [1]  — §4.1 MTEB 榜单 Top 7，含 Qwen3-Embedding 三个版本性能数据

## 变更记录

- 2026-05-26: 初始创建，来源 
- 2026-06-10: 合并 [model-qwen3](/base-models/model-qwen3) 的 MTEB 基准背景信息，统一 Qwen3-Embedding 页面
- 2026-06-21: 竞品更新——截至 2026-04，NVIDIA NV-Embed-v2（72.31 英文 MTEB）和 BGE-en-ICL（71.24）已进入前列；Qwen3 自身 70.58 仍为开源标杆，新兴维度压缩（Matryoshka 32-4096 维）成为标配能力
