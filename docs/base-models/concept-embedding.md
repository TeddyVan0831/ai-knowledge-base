---
title: "Embedding（嵌入）"
outline: deep
---

# Embedding（嵌入）

> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 

## 摘要

Embedding（嵌入/向量化）是一种降维技术，将不同模态的特征（文本、图片、音频等）转换为固定维度的稠密向量，使语义相似度可以通过向量空间距离来度量。

## 详情

### 定义

将离散数据（文本单词、图像像素等）转换为**低维、稠密**的向量表示。现在最常见的应用是**文本 Embedding**，但"万物皆可 embedding"。

### 核心特性

- 将离散数据转换为低维、稠密的向量
- 捕捉语义信息（而非仅表面特征）
- 向量空间中的距离（如余弦相似度）反映语义相似度

### 与 One-Hot 编码的对比

| 对比项 | One-Hot | Embedding |
|--------|---------|-----------|
| 维度 | 高维（=词表大小，如 10000 ） | 低维稠密（如 768、1024 ） |
| 稀疏性 | 极度稀疏（仅 1 位为 1） | 稠密（所有维度都有值） |
| 语义捕捉 | ❌ 无法表达语义相似性 | ✅ 语义相近的词向量距离近 |
| 存储效率 | 低 | 高 |

### 应用场景

| 场景 | 说明 |
|------|------|
| **推荐系统** | 计算用户和物品的向量相似度 |
| **语义搜索** | 基于语义相似度检索文档 |
| **文本分类** | 将文本转换为向量后输入分类器 |
| **聚类分析** | 将相似文本自动分组 |
| **文搜图** | 将文本和图片映射到同一向量空间，跨模态检索 |

### 关键结论

- **Word2Vec** 的本质是一个查找表：通过神经网络将词从 one-hot 空间映射到稠密向量空间
- **king - man + woman ≈ queen**：向量运算可以表达语义关系
- 不仅是单词，句子、段落、图像都可以转换为固定大小的向量表示

## 关联

- 相关概念: [Word2Vec](/base-models/concept-word2vec)、[余弦相似度](/base-models/concept-cosine-similarity)、[Embedding 模型选型](/base-models/concept-embedding-model-selection)
- 相关实体: [Qwen3-Embedding 系列](/base-models/model-qwen3-embedding)、[Jina Embeddings V4](/base-models/model-jina-embedding)
- 参见: [KV Cache](/architecture/concept-kv-cache)

## 引用来源

- [1]  — 系统学习笔记，涵盖 Embedding 定义、Word2Vec 原理、MTEB 榜单、向量数据库

## 变更记录

- 2026-05-26: 初始创建，来源 
