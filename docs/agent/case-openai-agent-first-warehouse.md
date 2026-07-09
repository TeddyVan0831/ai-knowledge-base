---
title: "OpenAI Agent-first 仓库案例"
outline: deep
---

# OpenAI Agent-first 仓库案例

> **类型**: entity
> **创建时间**: 2026-07-05
> **最后更新**: 2026-07-05
> **来源**:  第 9 章
> **领域**: ai

## 摘要

Ryan Lopopolo / OpenAI Engineering 2026 论文 *Harness engineering: leveraging Codex in an agent-first world*。**背景**：团队从空仓库开始，让 Codex 生成产品代码、测试、CI、文档、可观测和内部工具；人主要负责意图、环境和反馈回路。**关键数据**：5 个月内产出约 100 万行代码，合并约 1,500 个 PR，估计速度为手写代码的 1/10；产品 beta 版包含 0 行手写代码。**核心教训**：巨型 `AGENTS.md` 会失败；仓库知识、计划、观察信号和质量约束需要被设计成 Agent 可发现、可执行、可验证的系统资产。

## 详情

### 一、关键数据

| 指标 | 数值 |
|------|------|
| 时间 | 5 个月 |
| 代码产出 | **~100 万行** |
| PR 合并数 | **~1,500 个** |
| 速度比 | 手写代码的 **1/10** |
| Beta 版手写代码 | **0 行** |

### 二、AGENTS.md 失败设计 → 改进结构

#### 失败设计：巨型 AGENTS.md

**问题**：
- 大量规则挤占上下文
- 所有规则失去重点
- 规则迅速陈旧
- 难以机械检查

#### 改进结构：分层组织

| 层次 | 作用 |
|------|------|
| 约百行的 `AGENTS.md` | 只做目录 |
| 详细事实 | 进入版本化 `docs/` |
| 复杂任务 | 使用带进度和决策记录的 execution plan |
| 文档结构、新鲜度、交叉链接 | Lint 和 CI 检查 |
| 日志、指标、Trace | 暴露给 Agent 查询和验证 |

### 三、关键启示

1. **AGENTS.md 是目录，不是规则库**：百行级别的目录文件 + 版本化 `docs/` + execution plan 是更可持续的结构
2. **复杂任务需要 execution plan**：包含进度和决策记录，让 Agent 能跨会话继续
3. **质量约束要可机械检查**：Lint/CI 检查文档结构、新鲜度、交叉链接
4. **可观测资产对 Agent 友好**：日志、指标、Trace 暴露给 Agent 查询和验证
5. **0 手写代码 ≠ 0 人工**：人主要负责意图、环境和反馈回路

### 四、对 Harness 设计的指导

| 维度 | OpenAI 经验 |
|------|------------|
| 文档组织 | 巨型 AGENTS.md 会失败；分层结构（目录 + docs/ + plan）更可持续 |
| 任务分解 | 复杂任务用 execution plan 跟踪进度和决策 |
| 质量检查 | Lint/CI 检查文档结构而非依赖模型自觉 |
| 可观测性 | 日志/指标/Trace 必须 Agent 可查询 |
| 协作模式 | 0 手写代码可行，但需要人持续提供意图和环境 |

## 关联

- 相关概念: [Harness Engineering（harness 工程）](/agent/concept-harness-engineering), [Harness 覆盖层次（L0–L5）](/agent/concept-harness-coverage-levels)
- 主题: [2026 Agent 架构综述](/agent/topic-agent-architecture-2026)
- 配套资料: 
- 相关案例: [Anthropic 长任务 Harness 案例（Opus 4.5）](/agent/case-anthropic-long-running-agent), [SWE-agent ACI 接口实验案例](/agent/case-swe-agent-aci-experiment)

## 引用来源

- [1]  — 第 9.1 节 OpenAI 观察
- [2] Ryan Lopopolo / OpenAI Engineering 2026 *Harness engineering: leveraging Codex in an agent-first world*

## 变更记录

- 2026-07-05: 初始创建，来源  第 9 章
