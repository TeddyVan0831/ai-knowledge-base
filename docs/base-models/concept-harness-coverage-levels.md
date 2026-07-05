---
title: "Harness 覆盖层次（L0–L5）"
outline: deep
---

# Harness 覆盖层次（L0–L5）

> **类型**: concept
> **创建时间**: 2026-07-05
> **最后更新**: 2026-07-05
> **来源**: 
> **领域**: ai

## 摘要

Harness 的"覆盖层次"是从模型到组织的 **6 层嵌套结构**（L0–L5）。它把"组件"和"整体"分开：L0 是被包裹的模型本体，L1-L4 是不同深度的 Harness 组件层，L5 是治理与组织的 operating model。**完整 Harness 不是"每一层都塞满功能"，而是至少形成行动、状态、控制与验证的闭环，厚度与任务风险相匹配。**

## 详情

### 一、L0–L5 分层结构

```
┌─────────────────────────────────────────────────────────────┐
│ L5 治理与组织（Operating Model）                              │
│ 身份、审批、平台模板、责任、成本、审计                          │
├─────────────────────────────────────────────────────────────┤
│ L4 质量与交付（Outer Harness）                                │
│ Trace、Event logs、Tests、Eval、CI、Review                    │
├─────────────────────────────────────────────────────────────┤
│ L3 任务运行与服务（Runtime Core）                              │
│ Loop、编排、状态、记忆、恢复、消息、流式                       │
├─────────────────────────────────────────────────────────────┤
│ L2 行动与环境（Action Layer）                                 │
│ Tools、MCP、Skills、Workspace、Sandbox                        │
├─────────────────────────────────────────────────────────────┤
│ L1 指导与上下文（Guidance Layer）                             │
│ Prompt、规则、文档、RAG、Progress                            │
├─────────────────────────────────────────────────────────────┤
│ L0 模型（被包裹的核心）                                       │
│ 权重、推理能力、模型版本、预算                                 │
└─────────────────────────────────────────────────────────────┘
```

### 二、各层详解

| 层次 | 内容 | 关键判断 |
|------|------|---------|
| **L0 模型** | 权重、推理能力、模型版本、预算 | **不是 Harness**——是被包裹的核心 |
| **L1 指导与上下文** | Prompt、规则、文档、RAG、Progress | 关键组件，**单独不充分** |
| **L2 行动与环境** | Tools、MCP、Workspace、Sandbox | 让模型能感知和改变现实状态 |
| **L3 任务运行与服务** | Loop、编排、状态、记忆、恢复、消息、Streaming | 负责持续执行，**技术核心** |
| **L4 质量与交付** | Event logs、Trace、Tests、Eval、CI、Review | 让结果可见、可验、可回归 |
| **L5 治理与组织** | 身份、审批、成本、审计、职责、平台模板 | 通常是 operating model；编码成运行策略后部分进入 Harness |

### 三、判断完整 Harness 的核心准则

> **完整 Harness 至少形成：行动、状态、控制、验证 — 4 个闭环**（来自 [Macedo 2026 四问法](https://arxiv.org/abs/2606.10106)）

且厚度与任务风险相匹配（参见 [concept-harness-engineering#七-Harness-厚度矩阵](/base-models/concept-harness-engineering#七-Harness-厚度矩阵)）。

### 四、容易混淆的边界

| 现象 | 是不是 Harness？ | 原因 |
|------|---------------|------|
| 单次 Prompt 模板 | ❌ 组件 | 不负责执行和验证 |
| 仅 `AGENTS.md` / `CLAUDE.md` | ❌ 组件 | 是规则入口；需要运行系统读取 |
| MCP Server / 工具集合 | ❌ 组件 | 提供行动接口，不决定任务推进 |
| Sandbox / 容器 | ❌ 组件 | 控制环境权限，不负责规划/记忆/交接 |
| 固定 DAG 工作流 | ❌ 组件 | 观察结果不能改变整体策略 |
| 仅 `while loop + tools`（无持久状态/验证）| ❌ 邻接系统 | 长任务会缺状态、权限、完成验收 |
| 成熟 Coding Agent 产品（完整配置）| ✅ 完整 Harness | 循环+工具+上下文+权限+验证齐全 |
| Agent + 状态 + Policy + Tests | ✅ 完整 Harness | 自建系统也可以完整 |

> **关键判断**：MCP Server、Sandbox、固定 DAG 工作流都可能是关键组件，但**单独看通常不构成完整 Harness**。

### 五、L0-L5 与三层口径的对应

- **L0–L1（核心层）** = 三层口径的"模型"层
- **L2–L3（技术核心）** = 三层口径的"Agent 运行与控制系统"层
- **L4（外层）** = 三层口径的"项目/仓库外层 Harness"层
- **L5（最外）** = 三层口径的"Agent-first Operating Model"层

## 关联

- 相关概念: [Harness Engineering（harness 工程）](/base-models/concept-harness-engineering), [Agent 任务生命周期](/base-models/concept-agent-task-lifecycle)
- 主题: [topic-agent-architecture-2026](/base-models/topic-agent-architecture-2026)
- 配套资料: 

## 引用来源

- [1]  — 第 7 章 Harness 覆盖层次（图片识别 9）
- [2] [Harness Engineering（harness 工程）](/base-models/concept-harness-engineering) — 父级核心概念

## 变更记录

- 2026-07-05: 初始创建，来源  第 7 章
