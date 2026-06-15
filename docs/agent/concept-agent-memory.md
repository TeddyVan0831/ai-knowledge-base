---
title: "智能体记忆管理（Agent Memory Management）"
outline: deep
---

# 智能体记忆管理（Agent Memory Management）

> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 

## 摘要

智能体记忆管理为 Agent 提供短期和长期记忆能力——通过 Session 跟踪每次交互、State 维护会话临时状态、Memory Service 管理长期知识，使智能体具备上下文感知和持续学习能力。

## 详情

### 模式概述

记忆管理的核心是**状态持久化**——让智能体在多轮交互中保持对历史信息的记忆，并能跨会话访问长期知识 。

### 三层记忆架构

**1. Session（会话级）**：
- 跟踪每次聊天的完整历史
- 适合短期上下文保持
- 会话结束后自动清理

**2. State（状态级）**：
- 会话的"临时记事本"，存储关键变量和中间状态
- 跨多轮交互保持不变
- 适合跟踪任务进度、用户偏好等

**3. Memory Service（长期记忆）**：
- 持久化存储，跨会话访问
- 用户画像、领域知识库、历史决策记录
- 需要设计检索策略（向量搜索、关键词匹配等）

### 实践实现

书中提供了 Google ADK、LangChain/LangGraph 和 Vertex Memory Bank 三种实现方式 ：
- **Google ADK**：Session + State + MemoryService 三层原生支持
- **LangChain**：BufferMemory / ConversationSummaryMemory / VectorStore Memory
- **Vertex Memory Bank**：Google Cloud 的持久化记忆服务

### 关键要点

- 记忆管理是**智能体从工具升级为助手**的关键能力
- 需要平衡**记忆容量**与**检索速度**——记忆太多会导致上下文窗口溢出
- 长期记忆需要设计**遗忘策略**——不是所有历史信息都需要永久保留

## 关联

- 相关概念: [智能体学习与适应（Agent Learning & Adaptation）](/agent/concept-agent-learning), [KV Cache](/architecture/concept-kv-cache)
- 相关实体: [FAISS](/inference-deploy/product-faiss), [OpenClaw](/inference-deploy/product-openclaw), [Hermes](/inference-deploy/product-hermes)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — 第 8 章：记忆管理实践、Google ADK/LangChain/Vertex 实现

## 变更记录

- 2026-05-31: 初始创建，来源 Agentic Design Patterns 电子书第 8 章
