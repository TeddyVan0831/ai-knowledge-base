---
title: "Agent Harness 工程综述（2026）"
outline: deep
---

# Agent Harness 工程综述（2026）

> **类型**: topic
> **创建时间**: 2026-07-05
> **最后更新**: 2026-07-05
> **来源**: 
> **领域**: ai

## 摘要

本主题整合 2026 年 Harness Engineering 的核心概念、案例与工程实践。它从"模型不再只是给出一段回复"出发，定义 Harness 为把模型接入真实系统所需的运行与控制系统——行动、状态、控制、验证的闭环。涵盖 5 种分析单位、三层口径、L0-L5 覆盖层次、四问法边界判断、6 大系统模块、3 大工程观察（SWE-agent / Anthropic / OpenAI）以及 4 条工程结论。

## 详情

### 一、核心命题

> **Agent 的表现不是模型单独的属性，而是模型、Harness 与环境共同作用的结果。**

### 二、关键概念地图

| 概念 | 页面 |
|------|------|
| Harness Engineering 核心定义、五种分析单位、三层口径、四问法、厚度矩阵 | [Harness Engineering（harness 工程）](/base-models/concept-harness-engineering) |
| Agent 任务生命周期 8 阶段、6 大问题、6 大系统模块 | [Agent 任务生命周期](/base-models/concept-agent-task-lifecycle) |
| L0-L5 覆盖层次（从模型到组织） | [Harness 覆盖层次（L0–L5）](/base-models/concept-harness-coverage-levels) |
| 相关 Agent 概念 | [concept-agent-loop](/base-models/concept-agent-loop), [上下文工程（Context Engineering）](/agent/concept-context-engineering), [MCP 协议（已合并）](/base-models/concept-mcp-protocol), [智能体记忆管理（Agent Memory Management）](/agent/concept-agent-memory) |

### 三、3 大工程观察

| 观察 | 来源 | 核心结论 |
|------|------|---------|
| SWE-agent ACI 实验 | NeurIPS 2024 | 接口和控制会直接影响任务表现（18.0% vs 11.0%） |
| Anthropic 长任务案例 | Anthropic Engineering 2025-11-26 | 长任务需要外部状态和可验证交接 |
| OpenAI agent-first 仓库 | OpenAI Engineering 2026 | 仓库环境本身会成为 Harness 的一部分 |

详见：
- [SWE-agent ACI 接口实验案例](/base-models/case-swe-agent-aci-experiment)
- [Anthropic 长任务 Harness 案例（Opus 4.5）](/base-models/case-anthropic-long-running-agent)
- [OpenAI Agent-first 仓库案例](/base-models/case-openai-agent-first-warehouse)

### 四、4 条工程结论

1. **任务从可验证的契约开始**，而不是只从一段 Prompt 开始
   - 长任务案例用端到端功能清单定义"什么算完成"
   - agent-first 仓库把复杂工作写成包含进度和决策记录的 execution plan
   - 推论：目标、范围、证据、预算、权限、升级条件应成为外部任务对象

2. **上下文窗口不是任务状态**
   - Compaction 仍会让新会话猜测上一会话
   - Progress、Git、可启动基线承担连续性
   - 推论：计划、进度、决策、Workspace、证据需要独立持久化

3. **能用确定性机制表达的约束，不应只写成自然语言**
   - Lint 阻断比"请不要写出语法错误"更直接
   - 四问法 T4 强调控制不能依赖模型自觉
   - 推论：Schema、Policy、Tests、Linters、权限、状态断言应在模型之外执行

4. **重要失败要进入可重复的回归闭环**
   - 重复错误固化为规则、工具、程序化检查
   - 团队外层需要 Guides + Sensors
   - 推论：保存 Trace + 环境结果，先定位失败属于哪层 Harness，再修改最接近根因的层

### 五、Harness 6 大工程能力（学习地图）

| 能力面 | 覆盖内容 |
|--------|---------|
| **请求、输出与决策** | 单次模型请求、结构化输出、路由、任务分解、反思、多步编排 |
| **工具、MCP 与 Skills** | 工具调用回路、MCP 生态接入、Skills 撰写、选择、执行与校验 |
| **运行环境与安全边界** | Shell、文件、浏览器、Sandbox、权限、审批、幂等、风险分级 |
| **状态、记忆与协作** | Workspace、Checkpoint、长期记忆、自我成长、多 Agent 分发与回收 |
| **服务化、消息与用户入口** | API/Worker、流式输出、外部 IM、消息入口、取消、并发 |
| **观测、Eval 与治理** | Event logs、Trace、过程回放、Eval、成本、安全、审计 |

> 自我成长和多 Agent 协作是其中两条重要分支，但**不能代表全部 Harness 工程**。

### 六、与 AI 应用开发、Agent 开发的关系

| 角色 | 关注点 |
|------|--------|
| **Agent 开发工程师** | 关心具体业务场景中的细节落地（Function Calling、结构化输出、多轮对话、模型集成到业务系统）|
| **Harness 架构师 / AI 架构师** | 关注整个系统的宏观设计（关键模块、企业落地、如何把模块嵌入已有工作流）|
| **Harness 工程师** | 介于两者之间，更关注运行与控制层 |

### 七、求职方向（来自课堂答疑）

**Agent 开发工程师简历要点**：
- 较好完成 Function Calling 工作，理解输出控制原理
- 懂得知识库，能做多轮对话响应机器人
- 做过模型输出控制，对模型集成到业务系统有心得

**学习路径**：
- 零基础：先学完应用开发课程
- 进阶 Harness：必须从零搭一个自己的框架，真正理解原理（结构化输出控制、编排、单次请求组装）
- 理解原理后，可以用任何语言重新实现

### 八、常见框架定位

| 框架 | 定位 | 适用场景 |
|------|------|---------|
| OpenManus / 千问 Agent | 应用层框架，高度封装 | 快速 Demo |
| LangChain / LangGraph | 编排框架，更底层 | 复杂 Python 生态场景 |
| Dify / Flowise | 可视化编排框架 | DAG 能表达清楚的流程 |
| Ollama / vLLM / LM Studio | 模型推理框架 | 本地启动模型 |
| Pi | Agent 框架 | OpenClaude 核心任务处理层 |

## 关联

- 相关概念: [Harness Engineering（harness 工程）](/base-models/concept-harness-engineering), [Agent 任务生命周期](/base-models/concept-agent-task-lifecycle), [Harness 覆盖层次（L0–L5）](/base-models/concept-harness-coverage-levels)
- 相关案例: [SWE-agent ACI 接口实验案例](/base-models/case-swe-agent-aci-experiment), [Anthropic 长任务 Harness 案例（Opus 4.5）](/base-models/case-anthropic-long-running-agent), [OpenAI Agent-first 仓库案例](/base-models/case-openai-agent-first-warehouse)
- 配套资料: 

## 引用来源

- [1]  — 12 章节完整笔记 + 11 张图片识别（2026-07-01）
- [2] Macedo 2026 预印本 *What makes a harness a harness* — [arXiv 2606.10106](https://arxiv.org/abs/2606.10106)
- [3] Anthropic Engineering 2025-11-26 *Effective harnesses for long-running agents*
- [4] Ryan Lopopolo / OpenAI Engineering 2026 *Harness engineering: leveraging Codex in an agent-first world*
- [5] John Yang et al. NeurIPS 2024 *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*

## 变更记录

- 2026-07-05: 初始创建，来源 
