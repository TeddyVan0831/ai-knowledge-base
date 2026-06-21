---
title: "Agent 设计模式"
outline: deep
---

# Agent 设计模式

> **类型**: topic
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 

## 摘要

Agent 设计模式涵盖 Prompt Chaining、Parallelization、Routing、Tool Use、Reflection、Multi-Agent Collaboration 等核心模式，用于构建高效、可控的 AI Agent 系统。

## 详情

### 核心设计模式

| 模式 | 说明 | 来源 |
|------|------|------|
| **Prompt Chaining** | 将复杂任务分解为多个子任务，按顺序执行 |  |
| **Parallelization** | 并行执行多个独立任务，提高效率 |  |
| **Routing** | 根据输入类型或意图，将请求路由到不同的处理路径 |  |
| **Tool Use** | Agent 自主调用外部工具（API、搜索、代码执行等） |  |
| **Reflection** | Agent 自我反思和修正输出 |  |
| **Multi-Agent Collaboration** | 多个 Agent 协作完成复杂任务 | |
| **Human-in-the-Loop** | 在关键节点引入人工审核和干预 | |

### 相关概念

- [Agent 质量评估](/agent/concept-agent-evaluation)
- [智能体学习与适应（Agent Learning & Adaptation）](/agent/concept-agent-learning)
- [路由（Agent Routing）](/agent/concept-agent-routing)
- [智能体间通信（A2A Communication）](/agent/concept-a2a-communication)
- [异常处理与恢复（Error Handling & Recovery）](/agent/concept-error-recovery)
- [目标设定与监控（Goal Setting & Monitoring）](/agent/concept-goal-management)
- [人类参与环节（Human-in-the-Loop）](/agent/concept-human-in-the-loop)
- [多智能体协作（Multi-Agent Collaboration）](/agent/concept-multi-agent-collaboration)
- [提示链（Prompt Chaining）](/agent/concept-prompt-chaining)
- [并行化（Parallelization）](/agent/concept-parallelization)
- [推理技术（Reasoning Techniques）](/base-models/concept-reasoning-techniques)
- [反思（Reflection）](/agent/concept-reflection)
- [资源感知优化（Resource-Aware Optimization）](/agent/concept-resource-optimization)
- [护栏与安全模式（Safety Guardrails）](/agent/concept-safety-guardrails)
- [工具使用（Tool Use / Function Calling）](/agent/concept-tool-use)

## 关联

- 相关概念: [Deep Agent](/agent/concept-deep-agent), [Agent：从可控性到自主反思](/agent/concept-agent-controllability), [Agentic RAG](/rag/concept-agentic-rag)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — Agent 设计模式全集

## 变更记录

- 2026-05-31: 初始创建
