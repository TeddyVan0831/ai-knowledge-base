---
title: "Agent 五级分类体系"
outline: deep
---

# Agent 五级分类体系

> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 

## 摘要

Agent 系统按复杂度可分为 5 个等级——从独立的推理引擎到自进化系统，每级建立在前一级的能力之上。

## 详情

### Level 0: 核心推理系统

语言模型独立运行，仅依赖预训练知识，无工具、无记忆、无环境交互。擅长解释概念和规划方法，但对实时事件完全无知 。

### Level 1: 连接型问题解决者

推理引擎通过连接外部工具成为功能完整的 Agent。能执行 Think→Act→Observe 循环，使用搜索 API、金融 API、RAG 等获取实时信息 。

### Level 2: 战略型问题解决者

关键能力：**上下文工程**——Agent 主动选择、打包和管理每步计划中最相关的信息，防止上下文过载。能规划多步复杂目标 。

### Level 3: 协作多 Agent 系统

从单一"超级 Agent"转向"专家团队"模式。Agent 将其他 Agent 当作工具使用，通过委派子任务实现分工协作 。

### Level 4: 自进化系统

Agent 能识别自身能力缺口并动态创建新工具或新 Agent 来填补。从使用固定资源到主动扩展资源，实现真正的自主进化 。

## 关联

- 相关概念: [多智能体协作（Multi-Agent Collaboration）](/agent/concept-multi-agent-collaboration), [上下文工程（Context Engineering）](/agent/concept-context-engineering), [智能体记忆管理（Agent Memory Management）](/agent/concept-agent-memory)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — A Taxonomy of Agentic Systems（五级分类）

## 变更记录

- 2026-05-31: 初始创建
