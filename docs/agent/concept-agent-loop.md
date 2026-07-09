---
title: "Agent Loop（智能体循环）"
outline: deep
---

# Agent Loop（智能体循环）

> **类型**: concept
> **创建时间**: 2026-07-09
> **最后更新**: 2026-07-09
> **来源**: 
> **领域**: ai

## 摘要

Agent Loop（智能体循环）是 Agent 持续完成任务的核心运行机制：模型在"推理（思考）→ 行动（调用工具/写文件/发消息）→ 观察（获取结果）→ 再推理"的闭环中反复迭代，直到任务完成或触发终止/升级条件。它常被认为是 Agent 的"引擎"，但单独的 Loop 并不足以构成完整 Harness——没有状态、权限、验证、恢复等外部装置时，Loop 只是一种"会重复思考并行动的循环"（如 ReAct），无法独立保障任务正确完成。

## 详情

### 一、Loop 的基本形态（ReAct 范式）

最经典的循环是 **ReAct**（Reason + Act）：

1. **推理（Thought）**：模型基于当前上下文决定下一步动作
2. **行动（Action）**：调用工具、执行命令、读写文件、发送消息
3. **观察（Observation）**：工具/环境返回结果，作为下一轮输入
4. 回到 1，直到给出最终答案或满足停止条件

> Loop 在说"模型什么时候继续想和行动"——它是 Agent 与一次性 LLM 调用最本质的区别。

### 二、Loop ≠ 完整 Harness（关键区分）

| 对象 | 能否独立保障 Agent 任务 |
|------|---------|
| **Agent Loop / ReAct** | ❌ 不能（无状态/权限/验证时只是循环）|
| **Context Engineering** | ❌ 不能（是核心子系统但非全部）|
| **MCP / ACP / Tools** | ❌ 不能（是接口或协议）|
| **Agent Framework / SDK** | ❌ 不能自动保证（需具体配置）|
| **Agent Harness** | ✅ 讨论的核心对象（Loop + 状态 + 权限 + 验证 + 恢复）|

一句话定位：
- **Loop** 在说"模型什么时候继续想和行动"
- **Context Engineering** 在说"每轮喂给模型什么"
- **Harness** 在说"这件事在哪里运行、能做什么、状态怎样保存、结果怎样验收、出错怎样恢复"

### 三、Loop 在生命周期中的嵌入

Agent Loop 不是孤立组件，而是嵌入在 [Agent 任务生命周期](/agent/concept-agent-task-lifecycle) 的"行动 → 观察"阶段，并受编排层（状态机、路由、计划、重试、停止、子任务、多 Agent）驱动。一个健壮的 Loop 必须依赖：

| 保障维度 | 说明 |
|---------|------|
| **预算控制** | step / time / cost budget，no-progress 检测，重新规划 |
| **停止条件** | 显式终止、最大步数、任务完成信号 |
| **安全边界** | Policy gate、审批、只读/可逆/不可逆动作分级 |
| **错误恢复** | 幂等键、状态查询、事务、重试、回滚 |
| **状态维持** | Session / Progress / Checkpoint / 记忆，避免 context reset 后重复劳动 |

> 相关运行与控制系统层级见 [Harness Engineering](/agent/concept-harness-engineering) 的 L2-L3 层（行动与环境、任务运行与服务）。

### 四、典型 Loop 实现模式

- **单 Agent 串行循环**：最基础，逐步推进
- **带子任务分解的 Loop**：每轮可派生子 Agent 处理子目标
- **多 Agent 编排 Loop**：多个角色在循环中协作（见 [多智能体协作（Multi-Agent Collaboration）](/agent/concept-multi-agent-collaboration)）
- **长任务持久化 Loop**：跨会话/跨进程通过事件流与 Checkpoint 维持连续性

## 关联

- 相关概念: [Harness Engineering（harness 工程）](/agent/concept-harness-engineering)、[Agent 任务生命周期](/agent/concept-agent-task-lifecycle)、[上下文工程（Context Engineering）](/agent/concept-context-engineering)、[MCP 协议（已合并）](/base-models/concept-mcp-protocol)、[智能体记忆管理（Agent Memory Management）](/agent/concept-agent-memory)、[多智能体协作（Multi-Agent Collaboration）](/agent/concept-multi-agent-collaboration)
- 主题: [2026 Agent 架构综述](/agent/topic-agent-architecture-2026)
- 案例: [Anthropic 长任务 Harness 案例（Opus 4.5）](/agent/case-anthropic-long-running-agent)、[SWE-agent ACI 接口实验案例](/agent/case-swe-agent-aci-experiment)、[OpenAI Agent-first 仓库案例](/agent/case-openai-agent-first-warehouse)
- 配套资料: 

## 引用来源

- [1]  — 第 2 章 Harness 定义光谱、四问法（T1 运行时闭环）
- [2] [Harness Engineering（harness 工程）](/agent/concept-harness-engineering) — 易混概念区分表、L0-L5 分层
- [3] [Agent 任务生命周期](/agent/concept-agent-task-lifecycle) — 生命周期 8 阶段、6 大系统模块

## 变更记录

- 2026-07-09: 初始创建（Lint P1 修复：原被 4 处引用但无独立页，由 Harness 课程笔记 + 生命周期页内容综合编译）
