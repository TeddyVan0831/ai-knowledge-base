---
title: "LangChain 问答链类型（Chain Types）"
outline: deep
---

# LangChain 问答链类型（Chain Types）

> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 

## 摘要

LangChain 框架中用于组合多个检索文档的四种问答链类型：stuff、map_reduce、refine、map_rerank。不同 chain_type 决定了如何将检索到的文档片段组织并传递给 LLM 生成答案。

## 详情

在 LangChain 框架中，问答链（load_qa_chain）用于组合文档并将上下文和问题发送给 LLM 。问答链中有 4 种 chain_type 。

### 四种 Chain Types 对比

来源: 

| Chain Type     | 说明                   | 适用场景                    |
| -------------- | ---------------------- | --------------------------- |
| **stuff**      | 直接把文档作为 prompt 输入    | 文档拆分的比较小，一次获取文档比较少，优先使用 |
| **map_reduce** | 每个 chunk 单独处理再合并     | 可并发，但缺少上下文              |
| **refine**     | 在第一个 chunk 上处理，合并下一个 | 部分保留上下文，控制 token        |
| **map_rerank** | 每个 chunk 打分，返回最好的    | 大量调用 LLM，独立处理           |

### 选择建议

能使用 `stuff` 的就使用这种方式（调用 LLM 次数少）。

优先级顺序：**stuff > refine > map_reduce > map_rerank** 。

## 关联

- 相关概念: [RAG（检索增强生成）](/rag/concept-rag), [RAG 高级检索技术](/rag/concept-rag-advanced-retrieval)

## 引用来源

- [1]  — LangChain 问答链类型：四种 chain_type 对比、选择建议

## 变更记录

- 2026-05-26: 初始创建，来源 
