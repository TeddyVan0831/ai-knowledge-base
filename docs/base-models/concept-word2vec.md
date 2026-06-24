---
title: "Word2Vec"
outline: deep
---

# Word2Vec

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **领域**: ai

## 摘要

Word2Vec 是 Google 提出的词向量技术，通过神经网络将离散单词映射到稠密向量空间，使语义相似的词在向量空间中距离相近，奠定了现代 Embedding 的基础思想。

## 详情

### 基本思想

通过一个神经网络，把词所在空间映射到一个新的空间中去，使得语义上相似的单词在该空间内距离相近。

### 架构要点

- 输入侧使用 **one-hot 编码**
- 隐藏层的神经元数量为 `hidden_size`（即 Embedding 维度）
- 输入-隐藏层之间的权值矩阵大小为 `[vocab_size, hidden_size]`
- **矩阵相乘时实质上是查表**：取出权值矩阵中对应输入词的那一行，即为该词的 Word2Vec 表示
- 输出层为 `[vocab_size]` 大小的向量，每个值代表输出一个词的概率

### 关键洞察

- Word2Vec 的隐藏层权重矩阵就是 **Embedding 查找表**
- 隐层的输出是每个输入单词的 Word Embedding
- 转换后的向量包含语义特征，可通过向量相似度判别词语的语义相似性

### 经典示例

- GloVe 向量化后，King 的 50 维向量  中各权重在 [-2, 2] 范围 
- 比较向量距离：**Man 和 Woman 更接近**
- 向量运算：**king - man + woman ≈ queen**（语义关系可通过向量运算表达）

## 关联

- 相关概念: [Embedding（嵌入）](/base-models/concept-embedding)、[余弦相似度](/base-models/concept-cosine-similarity)
- 参见: [Embedding 模型选型](/base-models/concept-embedding-model-selection)

## 引用来源

- [1]  — §2 Word Embedding 部分，涵盖 one-hot → Word2Vec 演进
- [2] Word2Vec 论文: https://arxiv.org/abs/1301.3781

## 变更记录

- 2026-05-26: 初始创建，来源 
