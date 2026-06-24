---
title: "异常处理与恢复（Error Handling & Recovery）"
outline: deep
---

# 异常处理与恢复（Error Handling & Recovery）

> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 
> **领域**: ai

## 摘要

异常处理与恢复模式为智能体提供错误检测、诊断和自我修复能力——使 Agent 在遇到 API 失败、工具调用错误或逻辑异常时能够自主恢复，而不是直接崩溃。

## 详情

### 模式概述

异常处理的核心是**弹性执行**——智能体在执行过程中遇到错误时，能够识别错误类型、选择恢复策略并继续任务，而非终止执行 。

**恢复策略**：
- **重试**：临时性错误（网络超时、限流），等待后重试
- **降级**：主工具不可用时切换到备用工具
- **绕过**：非关键步骤失败时跳过，继续后续步骤
- **回滚**：错误导致状态不一致时回退到安全状态

### 实践应用

- **API 调用失败**：自动重试 + 指数退避
- **工具不可用**：切换到替代工具或告知用户
- **逻辑错误**：检测异常输出并重新执行

### 关键要点

- 异常处理是**生产级智能体**的必备能力
- 需要区分**可恢复错误**和**不可恢复错误**
- 恢复策略的优先级：重试 > 降级 > 绕过 > 终止

## 关联

- 相关概念: [护栏与安全模式（Safety Guardrails）](/agent/concept-safety-guardrails), [Agent 质量评估](/agent/concept-agent-evaluation), [目标设定与监控（Goal Setting & Monitoring）](/agent/concept-goal-management), [人类参与环节（Human-in-the-Loop）](/agent/concept-human-in-the-loop)
- 参见: [Agent 设计模式](/agent/topic-agentic-design-patterns)

## 引用来源

- [1]  — 第 12 章：异常处理与恢复模式概述、ADK 代码示例

## 变更记录

- 2026-05-31: 初始创建，来源 Agentic Design Patterns 电子书第 12 章
