---
title: "上下文工程（Context Engineering）"
outline: deep
---

# 上下文工程（Context Engineering）

> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: , 
> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: , 
> **领域**: ai

## 摘要

上下文工程是 Level 2+ Agent 的关键能力——Agent 主动选择、打包和管理最相关的信息用于每步计划，防止上下文过载，确保高效性能。核心机制包括 Sessions（会话管理）和 Memory（记忆管理）。

## 详情

### 什么是上下文工程

Agent 的准确性取决于聚焦、高质量的上下文。上下文工程管理模型有限的注意力，防止过载并确保高效性能 。

### Sessions（会话管理）

Session 是 Agent 与用户之间一次完整交互的有状态容器：
- 维护对话历史和事件序列
- 在多 Agent 系统中，子 Agent 可写入父 Session
- 生产考量：安全与隐私、数据完整性与生命周期、性能与可扩展性 

### Memory（记忆管理）

长期记忆提供跨会话持久化，通常实现为连接到向量数据库或搜索引擎的 RAG 系统 。

**记忆类型**：
- 短期记忆：当前对话的"草稿纸"，跟踪 (Action, Observation) 序列
- 长期记忆：跨会话持久化，通过 RAG 查询用户偏好和历史结果

**记忆生成**：
- 提取（Extraction）：从对话中提取关键信息
- 整合（Consolidation）：将提取的信息合并为结构化记忆

## 关联

- 相关概念: [智能体记忆管理（Agent Memory Management）](/agent/concept-agent-memory), [Agent 五级分类体系](/agent/concept-agent-taxonomy), [KV Cache](/architecture/concept-kv-cache)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — Context Engineering、Sessions、Memory 完整章节
- [2]  — Augment with Context 章节

## 变更记录

- 2026-05-31: 初始创建
