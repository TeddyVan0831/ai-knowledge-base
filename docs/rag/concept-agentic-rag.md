---
title: "Agentic RAG"
outline: deep
---

# Agentic RAG

> **创建时间**: 2026-05-27
> **最后更新**: 2026-05-27
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-27
> **最后更新**: 2026-05-27
> **来源**: 
> **领域**: ai

## 摘要

Agentic RAG 在做 RAG 检索之前，先有一个小型 agent 处理 query：识别是否需要改写、决定如何改写、决定几次检索、判断检索数据源（向量数据库 vs SQL），实现智能化的检索前路由。

## 详情

### 核心流程

在 RAG 检索之前，小型 agent 负责：
1. 识别用户 query 是否需要改写 
2. 决定如何改写、改写成几条 query 
3. 决定要做几次 RAG 检索 
4. 判断哪些 query 应该检索知识库（向量数据库），哪些应该检索普通数据库（如订单、商品参数、物流信息 → 转为 SQL 查询） 

### 实现方式

一套提示词 + 样例即可，大语言模型能较好完成判断 。

### 与 Query 改写的关系

Agentic RAG 是 Query 改写的升级版，不仅改写 query，还负责**检索路由决策**——决定走向量检索还是结构化查询。

## 关联

- 相关概念: [Query 改写（查询改写）](/rag/concept-query-rewriting), [RAG（检索增强生成）](/rag/concept-rag), [Few-Shot Prompting](/base-models/concept-few-shot-prompting)
- 相关实体: [OpenClaw](/inference-deploy/product-openclaw), [Hermes](/inference-deploy/product-hermes), [LangChain](/inference-deploy/product-langchain)
- 参见: [RAG 优化策略](/rag/topic-rag-optimization), [Deep Agent](/agent/concept-deep-agent)

## 引用来源

- [1]  — §5.1.3 Agentic RAG

## 变更记录

- 2026-05-27: 初始创建，来源 
