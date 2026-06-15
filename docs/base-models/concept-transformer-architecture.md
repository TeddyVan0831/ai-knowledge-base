---
title: "Transformer 架构"
outline: deep
---

# Transformer 架构

> **类型**: concept
> **创建时间**: 2026-05-29
> **最后更新**: 2026-05-29
> **来源**: 

## 摘要

Transformer 是 Google 于 2017 年提出的序列建模框架（《Attention Is All You Need》），至今八年已成为几乎所有 AI 模型的基础架构。它不是一个具体模型，而是框架——GPT、通义千问、DeepSeek 等都套用该架构，内部结构永不改变，变化的是训练数据和目标。

## 详情

### 完整处理流程

```
用户输入 → ① Token 化 → ② Embedding 向量化 → ③ 位置编码
  → ④ N 层 Decoder（每层 = 多头自注意力 + 前馈网络）
  → ⑤ Linear 层 → ⑥ Softmax 归一化 → 选下一个 token
  → 自回归循环
```

**核心洞察**：大语言模型内部 90% 以上的数学计算，全部是为了"看懂"输入的每一个文字——深刻理解上下文，而非直接生成回复 。

### Tokenization

- 将文字转化为模型基本处理单元 token 
- 中文常用汉字 3000-5000 个，但所有汉字有 8-10 万个。通过拆分子词（如偏旁部首）来复用，缩小词表规模 
- 不涉及 AI 计算，纯粹查表映射 

### Embedding

将每个 token 映射为高维数学向量，以便后续数学运算。现代 LLM 的向量维度通常为 12288 维或更高。

### 位置编码（Positional Encoding）

为每个向量加入位置信息（如 128 位置 → 12288 维向量），使模型知道 token 的顺序。

### 多头自注意力（Multi-Head Attention）

Transformer 的核心创新——允许模型动态权衡每个 token 相对于其他 token 的重要性，捕捉全局上下文信息。

### 前馈网络（Feedforward Network, FFN）

每个 Transformer 层包含一个应用于每个 token 的前馈网络，由两层全连接层组成。96 层 Decoder 共约 28,000 个线性层/权重矩阵 。

### 训练过程

- **梯度下降**：通过反向传播优化参数
- **Batch/Epoch**：分批训练，全部过完一遍为一个 epoch
- **收敛**：损失函数逐步降低，模型参数趋于稳定

## 关联

- 相关概念: [大语言模型训练范式](/base-models/concept-llm-training-paradigm), [注意力机制优化](/architecture/concept-attention-optimization), [大语言模型发展简史](/base-models/concept-llm-history)
- 参见: [模型优化](/training-optimization/topic-model-optimization), [AI 经典论文汇览](/tools-ecosystem/topic-ai-classic-papers)（AI 经典论文汇览，覆盖 Transformer 全系论文）

## 引用来源

- [1]  — Transformer 总览、Tokenization、Embedding、位置编码、多头注意力、前馈网络、训练过程

## 变更记录

- 2026-05-29: 初始创建
