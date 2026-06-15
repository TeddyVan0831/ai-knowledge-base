---
title: "Agent 互操作性（A2A）"
outline: deep
---

# Agent 互操作性（A2A）

> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 

## 摘要

A2A（Agent-to-Agent）协议是 Agent 之间的标准化通信协议——实现 Agent 能力的可复用、可发现和跨平台互操作，解决多 Agent 系统中的集成和协作问题。

## 详情

### 为什么需要 A2A

当 Agent 数量增长时，Agent 之间的点对点通信变得不可维护。A2A 提供标准化协议，让 Agent 可以像微服务一样被发现和调用 。

### 核心能力

- **可复用性**：一个 Agent 的能力可以被多个其他 Agent 调用
- **标准化**：统一的请求/响应格式，消除集成摩擦
- **跨平台**：不同框架（ADK、LangGraph 等）构建的 Agent 可以互操作
- **可发现性**：Agent 可以动态发现并调用其他 Agent 的能力

### 实现方式

通过 `unicorn` 或 Agent Engine 等服务器将现有 Agent 暴露为 A2A 兼容的端点，使其他 Agent 可以通过标准协议调用它 。

## 关联

- 相关概念: [多智能体协作（Multi-Agent Collaboration）](/agent/concept-multi-agent-collaboration), [MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp), [智能体间通信（A2A Communication）](/agent/concept-a2a-communication)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — A2A 章节

## 变更记录

- 2026-05-31: 初始创建
