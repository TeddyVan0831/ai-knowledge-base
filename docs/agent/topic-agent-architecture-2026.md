---
title: "2026 Agent 架构综述"
outline: deep
---

# 2026 Agent 架构综述

> **类型**: topic
> **创建时间**: 2026-07-09
> **最后更新**: 2026-07-09
> **来源**: 
> **领域**: ai

## 摘要

2026 年的 Agent 架构（Agent Architecture）已经超越"一个会调工具的 LLM"，演化为一套由**模型 + 运行与控制系统（Harness）+ 项目外层 + 组织 Operating Model** 组成的分层社会技术系统。本综述从 Harness Engineering 视角，把 Agent 架构拆解为运行循环（Loop）、上下文工程、工具与 MCP、状态与记忆、验证与 Eval、服务化与治理六大支柱，并串联本知识库已有的 Agent 概念页与案例页，给出一张可导航的架构地图。

## 详情

### 一、分层口径：从模型到组织

Agent 架构不是单一组件，而是嵌套的四层同心结构（详见 [Harness Engineering](/agent/concept-harness-engineering) 的 L0-L5 分层）：

| 层次 | 内容 | 关注点 |
|------|------|--------|
| L0 模型 | 权重、推理能力、版本、预算 | 被 Harness 包裹的核心 |
| L1 指导与上下文 | Prompt、规则、文档、RAG、Progress | 关键但不充分 |
| L2 行动与环境 | Tools、MCP、Skills、Workspace、Sandbox | 技术核心 |
| L3 任务运行与服务 | Loop、编排、状态、记忆、恢复、消息、流式 | 技术核心 |
| L4 质量与交付 | Trace、Event logs、Tests、Eval、CI、Review | 外层 Harness |
| L5 治理与组织 | 身份、审批、平台模板、责任、成本、审计 | Operating Model |

### 二、六大架构支柱

| 支柱 | 核心问题 | 对应概念页 |
|------|---------|-----------|
| **1. 运行循环 Loop** | 模型何时继续想与行动 | [Agent Loop（智能体循环）](/agent/concept-agent-loop)、[Agent 任务生命周期](/agent/concept-agent-task-lifecycle) |
| **2. 上下文工程** | 每轮喂给模型什么 | [上下文工程（Context Engineering）](/agent/concept-context-engineering) |
| **3. 工具与协议** | 如何获得行动力并限制副作用 | [MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp)、[工具使用（Tool Use / Function Calling）](/agent/concept-tool-use)、[Function Calling — 模型的"手指"](/agent/concept-function-calling) |
| **4. 状态与记忆** | 多轮/长任务如何保持连续 | [智能体记忆管理（Agent Memory Management）](/agent/concept-agent-memory)、[目标设定与监控（Goal Setting & Monitoring）](/agent/concept-goal-management) |
| **5. 验证与 Eval** | 如何独立验收、归因失败、持续改进 | [Agent 质量评估](/agent/concept-agent-evaluation)、[Agent：从可控性到自主反思](/agent/concept-agent-controllability) |
| **6. 服务化与治理** | 如何作为长期系统对外提供 + 组织责任 | [Agent Ops](/agent/concept-agent-ops)、[智能体间通信（A2A Communication）](/agent/concept-a2a-communication) |

### 三、设计模式谱系

Agent 架构在模式层面已形成较完整谱系（综述见 [Agent 设计模式](/agent/topic-agentic-design-patterns)）：

- **Prompt Chaining**（顺序链）
- **Routing / Parallelization**（路由 / 并行）
- **Reflection**（反思自检）
- **Planning**（规划与再规划）
- **Multi-Agent Collaboration**（多智能体协作）
- **Human-in-the-Loop**（人在回路）
- **Error Recovery**（错误恢复）

> 决定 Harness 厚度（薄/厚）的不是"用了多大的模型"，而是：任务持续时间、副作用可逆性、动态探索需求、独立验证难度、失败成本与责任。详见 [Harness Engineering（harness 工程）](/agent/concept-harness-engineering) 的厚度矩阵。

### 四、案例切片（验证架构如何落地）

| 案例 | 架构亮点 | 页面 |
|------|---------|------|
| Anthropic 长任务 Agent | 长任务编排、状态持久化、人工升级 | [Anthropic 长任务 Harness 案例（Opus 4.5）](/agent/case-anthropic-long-running-agent) |
| SWE-agent | Agent-Computer Interface（ACI）实验 | [SWE-agent ACI 接口实验案例](/agent/case-swe-agent-aci-experiment) |
| OpenAI Agent-first 仓库 | 仓库即交付单元、CI/架构约束进 Harness | [OpenAI Agent-first 仓库案例](/agent/case-openai-agent-first-warehouse) |

## 关联

- 核心概念: [Harness Engineering（harness 工程）](/agent/concept-harness-engineering)、[Agent Loop（智能体循环）](/agent/concept-agent-loop)、[Agent 任务生命周期](/agent/concept-agent-task-lifecycle)
- 设计模式: [Agent 设计模式](/agent/topic-agentic-design-patterns)、[Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)
- 案例: [Anthropic 长任务 Harness 案例（Opus 4.5）](/agent/case-anthropic-long-running-agent)、[SWE-agent ACI 接口实验案例](/agent/case-swe-agent-aci-experiment)、[OpenAI Agent-first 仓库案例](/agent/case-openai-agent-first-warehouse)
- 配套资料: 

## 引用来源

- [1]  — 第 2 章（定义光谱）、第 3 章（三层口径）、第 6 章（生命周期与模块地图）、第 7 章（覆盖层次）
- [2] [Harness Engineering（harness 工程）](/agent/concept-harness-engineering) — L0-L5 分层、厚度矩阵
- [3] [Agent 任务生命周期](/agent/concept-agent-task-lifecycle) — 6 大系统模块

## 变更记录

- 2026-07-09: 初始创建（Lint P1 修复：原被 6 处引用但无独立页，由 Harness 课程笔记综合编译为 Agent 架构综述）
