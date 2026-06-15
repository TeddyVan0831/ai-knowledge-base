---
title: "Agent 智能体"
outline: deep
---

# Agent 智能体

从设计模式到通信协议，从五大架构到评估体系 —— 构建可控、可靠、可进化的 AI Agent。

## 综述

| 文件 | 标题 | 摘要 |
|------|------|------|
| [topic-agent-development](./topic-agent-development) | Agent 开发全览 | 从底层能力到上线评估的完整技术链路 |
| [topic-agentic-design-patterns](./topic-agentic-design-patterns) | Agent 设计模式 | Prompt Chaining、Routing、Reflection 等核心模式 |

## 架构与分类

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-agent-planning](./concept-agent-planning) | Agent 自主规划 — 五大架构模式 | 从即时响应到持续自进化的能力递进关系 |
| [concept-agent-taxonomy](./concept-agent-taxonomy) | Agent 五级分类体系 | 从独立推理引擎到自进化系统 |
| [concept-agent-controllability](./concept-agent-controllability) | Agent：从可控性到自主反思 | Workflow Agent vs ReAct Agent 两种核心形态 |
| [concept-deep-agent](./concept-deep-agent) | Deep Agent | 2025 年收敛的 Agent 技术形态 |

## 设计模式

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-prompt-chaining](./concept-prompt-chaining) | 提示链（Prompt Chaining） | 最基础的智能体设计模式 —— 步骤串联 |
| [concept-parallelization](./concept-parallelization) | 并行化（Parallelization） | 独立子任务并发处理 |
| [concept-agent-routing](./concept-agent-routing) | 路由（Agent Routing） | 自动分类并路由到最合适的处理路径 |
| [concept-tool-use](./concept-tool-use) | 工具使用（Tool Use） | 从只会说话升级为能做实事 |
| [concept-reflection](./concept-reflection) | 反思（Reflection） | 生成 → 反思 → 修正的自我改进循环 |
| [concept-multi-agent-collaboration](./concept-multi-agent-collaboration) | 多智能体协作 | 分工、通信、协调机制 |

## 核心能力

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-function-calling](./concept-function-calling) | Function Calling | 模型调用预设外部函数的原子化能力 |
| [concept-mcp](./concept-mcp) | MCP：模型上下文协议 | AI 领域的 USB-C 接口 |
| [concept-a2a-communication](./concept-a2a-communication) | 智能体间通信（A2A） | 跨框架跨厂商的标准化通信协议 |
| [concept-agent-interoperability](./concept-agent-interoperability) | Agent 互操作性（A2A） | 可复用、可发现的跨平台互操作协议 |
| [concept-context-engineering](./concept-context-engineering) | 上下文工程 | Level 2+ Agent 的关键能力 |
| [concept-agent-memory](./concept-agent-memory) | 智能体记忆管理 | Session → State → Memory 三层记忆架构 |
| [concept-agent-learning](./concept-agent-learning) | 智能体学习与适应 | 从失败中学习、外部进化、自我反馈 |

## 工程与安全

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-agent-ops](./concept-agent-ops) | Agent Ops | DevOps → MLOps → GenAIOps → AgentOps 演进 |
| [concept-agent-optimization](./concept-agent-optimization) | Agent 能力优化与效果评估 | 回答完整性、幻觉检测、安全与成本评估 |
| [concept-agent-evaluation](./concept-agent-evaluation) | Agent 质量评估 | 从原型到生产的全流程评估 |
| [concept-goal-management](./concept-goal-management) | 目标设定与监控 | 子目标设定、进度跟踪、自我纠正 |
| [concept-error-recovery](./concept-error-recovery) | 异常处理与恢复 | 错误检测、诊断和自我修复 |
| [concept-resource-optimization](./concept-resource-optimization) | 资源感知优化 | Token 消耗、API 成本的动态管控 |
| [concept-human-in-the-loop](./concept-human-in-the-loop) | 人类参与环节 | 高风险操作的审核点 |
| [concept-safety-guardrails](./concept-safety-guardrails) | 护栏与安全模式 | 多层次安全防护体系 |

## 框架与产品

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-autoglm](./concept-autoglm) | AutoGLM：智能体操作框架 | 智谱两阶段解耦架构（规划器 + 执行器） |
| [concept-langchain-chain-types](./concept-langchain-chain-types) | LangChain 问答链类型 | stuff/map_reduce/refine/map_rerank 四种类型 |
