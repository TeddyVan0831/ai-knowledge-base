---
title: "Jina Embeddings V4"
outline: deep
---

# Jina Embeddings V4

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **类型**: entity
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **领域**: ai

## 摘要
Jina-Embeddings-v4 是由 Jina AI 开发的多模态多语言通用嵌入模型，基于 Qwen2.5-VL-3B-Instruct，维度 2048，支持 Matryoshka 俄罗斯套娃表示（128-2048 维可截断），最大上下文 32768 tokens。

## 详情

### 核心规格
| 特性 | 值 |
|------|-----|
| **基础模型** | Qwen2.5-VL-3B-Instruct  |
| **支持任务** | 检索、文本匹配、代码  |
| **模型数据类型** | BFloat 16  |
| **最大序列长度** | 32768  |
| **单向量维度** | 2048  |
| **套娃维度** | 128, 256, 512, 1024, 2048  |
| **池化策略** | 平均池化  |

### 背景
- Jina Embedding 由 Jina AI（官网 jina.ai）开发，公司总部位于德国柏林，专注于开源多模态搜索与向量化技术 
- Jina-embeddings-v4 是一个多模态和多语言检索的通用嵌入模型，特别适合用于复杂的文档检索，包括包含图表、表格和插图的视觉丰富文档 

### 俄罗斯套娃：Matryoshka Representation Learning (MRL)
- 模型总是先在内部生成最完整、维度最高（如 2048 维）的向量 
- 前 128 维、前 256 维、前 512 维...本身就是高质量的独立向量 
- 用户可通过 `embedding_size` 指定需要的维度 
- 生成完整向量后可按需截断 

## 关联
- 相关实体: [Qwen3-Embedding 系列](/base-models/model-qwen3-embedding)、[BGE-M3](/base-models/model-bge-m3)
- 相关概念: [Embedding（嵌入）](/base-models/concept-embedding)
- 参见: [Embedding 模型选型](/base-models/concept-embedding-model-selection)

## 引用来源
- [1]  — Jina Embedding 特性表、Matryoshka 表示学习原理

## 变更记录
- 2026-05-26: 初始创建，来源 
