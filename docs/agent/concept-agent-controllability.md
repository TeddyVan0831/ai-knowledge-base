---
title: "Agent：从可控性到自主反思"
outline: deep
---

# Agent：从可控性到自主反思

> **创建时间**: 2026-05-30
> **最后更新**: 2026-05-30
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-30
> **最后更新**: 2026-05-30
> **来源**: 
> **领域**: ai

## 摘要

Agent 是给大模型加上可控性的系统——解决大模型三大缺陷（幻觉、只会说不会做、步骤规划不靠谱）。两种核心形态：Workflow Agent（工作流，强调准确性）和 ReAct Agent（推理-行动，强调自主决策）。

## 详情

### 为什么需要 Agent？

大语言模型的三个核心缺陷 ：
1. **幻觉**：遇到不会的问题硬着头皮回答
2. **只会说不会做**：能输出文字但无法执行实际操作
3. **步骤规划不靠谱**：需要人类预先设计固定步骤

**核心定位**：模型提供智能，但智能需要可控 → Agent = 给模型加上可控性 

### 两种 Agent 形态

#### Workflow Agent（工作流智能体）
- **核心思想**：人类预先设计好固定步骤，大模型按步骤执行 
- **适用场景**：对准确性和可控性要求极高的场景
- **关键机制**：意图识别与分流——先识别问题类型，再选择知识库回答或启动工作流

#### ReAct Agent（推理-行动智能体）
- **核心思想**：Reasoning + Acting + 反馈循环的自主决策模式
- **适用场景**：需要自主探索和工具调用的复杂任务
- **核心组件**：意图识别、CoT、反思、Memory、上下文工程

### Agent 架构

```
大脑（LLM） + 提示词 + 工具 + 知识库 + 记忆 + 触发器
```

**Function Call**：大模型自主判断调用工具的能力——这是 Workflow Agent 向 ReAct Agent 过渡的关键能力。

## 关联

- 相关概念: [Deep Agent](/agent/concept-deep-agent), [Agentic RAG](/rag/concept-agentic-rag), [推理模型（Reasoning Models）](/base-models/concept-reasoning-models), [AutoGLM：智能体操作框架](/agent/concept-autoglm), [上下文工程（Context Engineering）](/agent/concept-context-engineering), [Agent Ops](/agent/concept-agent-ops)
- **Harness Engineering 视角（2026-07 新增）**: [Harness Engineering（harness 工程）](/base-models/concept-harness-engineering)（T4 独立控制是四问法关键）、[Harness 四问法（边界判断工具）](/base-models/concept-harness-four-questions)、[Agent 任务生命周期](/base-models/concept-agent-task-lifecycle)
- 相关实体: [OpenClaw](/inference-deploy/product-openclaw), [Hermes](/inference-deploy/product-hermes), [LangChain](/inference-deploy/product-langchain)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development), [Agent Harness 工程综述（2026）](/base-models/topic-harness-engineering-2026)

## 引用来源

- [1]  — Agent 起源、Workflow Agent、ReAct Agent、Function Call、架构设计

## 变更记录

- 2026-05-30: 初始创建
