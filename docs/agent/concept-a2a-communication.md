---
title: "智能体间通信（A2A Communication）"
outline: deep
---

# 智能体间通信（A2A Communication）

> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 

## 摘要

A2A（Agent-to-Agent）通信模式定义智能体之间的标准化通信协议——使不同框架、不同厂商开发的智能体能够互相发现、协商和协作，类似于微服务之间的 API 调用。

## 详情

### 模式概述

A2A 解决的是**智能体互操作性**问题——当多个智能体需要协同工作时，如何定义消息格式、发现对方、建立连接并交换信息 。

### A2A 与 MCP 对比 

| 维度 | A2A | MCP |
|------|-----|-----|
| 通信对象 | 智能体 ↔ 智能体 | 智能体 ↔ 工具/数据源 |
| 消息类型 | 任务请求、状态更新、结果返回 | 工具调用、数据查询 |
| 典型场景 | 多智能体协作、任务委托 | 工具集成、数据接入 |

### 核心概念

- **Agent Card**：智能体的"名片"，描述能力、接口和可用状态
- **Task**：结构化任务定义，包含输入、期望输出和约束条件
- **Protocol**：通信协议，定义消息格式和交互流程

### 关键要点

- A2A 是**多智能体协作**的底层基础设施
- 标准化通信协议是实现跨框架协作的前提
- 需要解决**发现机制**——智能体如何找到合适的合作伙伴

## 关联

- 相关概念: [多智能体协作（Multi-Agent Collaboration）](/agent/concept-multi-agent-collaboration), [MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp), [智能体记忆管理（Agent Memory Management）](/agent/concept-agent-memory)
- 参见: [Agent 设计模式](/agent/topic-agentic-design-patterns), [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — 第 15 章：A2A 通信模式概述、核心概念、与 MCP 对比、代码示例

## 变更记录

- 2026-05-31: 初始创建，来源 Agentic Design Patterns 电子书第 15 章
