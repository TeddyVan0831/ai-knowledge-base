---
title: "Agent 开发全览 — 从原理到实践"
outline: deep
---

# Agent 开发全览 — 从原理到实践

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 、、、、
> **类型**: topic
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 、、、、
> **领域**: ai

## 摘要

Agent 开发涵盖从底层能力（Function Calling/MCP）到架构选型（五大架构模式）、框架选择（LangChain/LlamaIndex/Qwen-Agent/AutoGen）、工具链构建（LangChain LCEL/ReAct），再到上线评估（LangSmith/OpenEvals/DeepEval）的完整技术链路。

## 详情

### 一、底层能力：Function Calling、Skill 与 MCP

Agent 的底层工具调用能力分为三层 ：

1. **能力层 — Function Calling**：模型理解"什么时候该调什么函数"，是原子化能力 
2. **封装层 — Skill**：把函数、Prompt、业务逻辑打包成"技能包"，是产品化封装 
3. **协议层 — MCP**：统一插头标准，让 Skill 和工具能在不同厂商的模型间无缝流动 

详见：[Function Calling — 模型的"手指"](/agent/concept-function-calling)、[MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp)

### 二、架构选型：Agent 五大架构

五种架构不是互斥关系，而是**能力递进关系**——从即时响应到持续自进化 。

| 架构 | 核心模式 | 最佳场景 |
| ---- | -------- | -------- |
| 反应式（Reactive） | 感知→决策→执行 | 简单、规则明确、需即时响应 |
| 深思熟虑（Deliberative） | 感知→建模→推理→决策→执行 | 复杂、多步、需战略规划 |
| ReAct | Thought → Action → Observation 循环 | 需要多轮工具调用的复杂问答 |
| PER（规划+反思） | Plan → Execute → Reflect → Refine | 需要高质量输出和自我修正的任务 |
| 自进化（PER+记忆+学习） | PER 循环 + 记忆库 + 学习反馈 | 需要持续优化和专业能力积累的领域 |

详见：[Agent 自主规划 — 五大架构模式](/agent/concept-agent-planning)

**构建 Agent 的三大核心思想** ：
1. 不要为所有任务构建 Agent —— Agent 适合处理复杂、模糊且高价值的任务
2. 保持简洁 —— 核心组件只有环境、工具集、系统提示
3. 像 Agent 一样思考 —— Agent 仅基于有限上下文（10-20k Token）做决策

### 三、框架选择：四大主流框架

详见：[AI 框架设计与选型](/inference-deploy/concept-ai-framework-selection)

**选型口诀**：知识库选 LlamaIndex、快 Demo 选 Qwen-Agent、复杂流程选 LangChain、多 Agent 选 AutoGen 。

所有框架都需要解决四大核心问题：LLM 适配、工具注册、Context 管理、控制流编排 。

### 四、工具链构建：LangChain 实践

详见 

#### LangChain 1.x 结构性变化

| 变化              | 说明                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| **包结构重构**       | `langchain-core`（基类+LCEL）、`langchain-community`（社区集成）、独立合作方包（`langchain-openai`、`langchain-anthropic`） |
| **新增子项目**       | **LangGraph**（图编排工作流）、**LangServe**（一键封装 REST API）、**LangSmith**（可视化调试+监控）                             |
| **API 转向 LCEL** | 用 `\|` 管道符拼 Runnable，不再继承 Chain 基类                                                                     |


#### LCEL 管道语法

LangChain Expression Language (LCEL) 是 1.x 的核心创新，使用 `\|` 管道符连接组件 ：

```python
chain = prompt | llm | StrOutputParser()
result = chain.invoke({"input": "..."})
```

**LCEL 优势** ：
- 直观的链式调用（类似 Unix 管道）
- 统一调用接口：`invoke()`、`stream()`、`batch()`、`ainvoke()`
- 支持流式输出、并行执行、异步

#### Agent vs LCEL 模式对比

| 维度   | LCEL 任务链                   | Agent 模式                   |
| ---- | -------------------------- | -------------------------- |
| 流程控制 | 开发者显式指定每步                  | LLM 自主决策                   |
| 适用场景 | 自定义流程、可控组合                 | 智能决策 + 多工具自动调度             |
| 灵活性  | 固定编排                       | 动态路由                       |


#### ReAct 模式

```
Question: 用户问题
  ↓
Thought: 我需要做什么？
  ↓
Action: 选择工具名
  ↓
Action Input: 工具输入
  ↓
Observation: 工具返回结果
  ↓
（重复 Thought → Action → Observation）
  ↓
Thought: 我现在知道最终答案
  ↓
Final Answer: 原始输入问题的最终答案
```


ReAct 将**推理（Reasoning）** 和 **动作（Acting）** 相结合，克服 LLM 胡言乱语的问题，提高结果可解释性和可信赖度 。

#### 工具注册

LangChain 最简洁的工具注册方式：`@tool` 装饰器，自动从 docstring 解析工具描述和参数 。

**关键**：docstring 非常重要！Agent 通过 docstring 判断何时使用该工具 。

#### 记忆管理

LangChain 1.x 使用 `RunnableWithMessageHistory` 管理会话历史 ：
- `MessagesPlaceholder` 用于在 Prompt 中插入历史消息
- `session_id` 用于区分不同用户/会话（多用户并发基础）
- `RunnableWithMessageHistory` 自动管理消息历史

四种短期记忆方式 ：
| 方式 | 策略 | 特点 |
| ---- | ---- | ---- |
| BufferMemory | 存储所有对话历史 | 完整但 Token 消耗大 |
| BufferWindowMemory | 只保留最近 K 组对话 | 滑动窗口，控制 Token |
| ConversationSummaryMemory | 对对话进行摘要 | 压缩历史，适合长对话 |
| VectorStore Memory | 向量存储 + 相似度匹配 | 按语义匹配最相关 K 组对话 |

### 五、效果评估与优化

详见：[Agent 能力优化与效果评估](/agent/concept-agent-optimization)

Agent 上线前必须经过系统评估，不能凭感觉 。

**四大评估工具**：

| 工具 | 定位 | 特点 |
| ---- | ---- | ---- |
| **LangSmith** | LangChain 官方商业产品 | 在线链路追踪、Debug、成本分析、Prompt 管理 |
| **OpenEvals** | LangChain 团队开源 | 11 种内置评估器，与 LangSmith 深度集成 |
| **DeepEval** | 独立开源 | 50+ 评估指标，类比 Pytest/JUnit，适合 CI/CD |
| **LangFuse** | 全开源可观测性平台 | 框架无关，可观测 + 提示管理 + 评估 |

**完整方案**：LangSmith（观测）+ OpenEvals/DeepEval（评估）。

**Prompt Ops 循环**：改 Prompt → 跑评估 → 看数据 → 再改 Prompt 。

## 关联
- 相关概念: [Function Calling — 模型的"手指"](/agent/concept-function-calling)、[MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp)、[Agent 自主规划 — 五大架构模式](/agent/concept-agent-planning)、[AI 框架设计与选型](/inference-deploy/concept-ai-framework-selection)、[Agent 能力优化与效果评估](/agent/concept-agent-optimization)

## 引用来源
- [1]  — Function Calling/Skill/MCP 三层架构
- [2]  — Agent 五大架构、构建原则
- [3]  — 四大框架对比、选型决策
- [4]  — LangChain LCEL/ReAct/Memory/工具链
- [5]  — 评估工具生态、Prompt Ops

## 变更记录
- 2026-05-26: 初始创建，综合来源 raw/notes-5 至 raw/notes-9
