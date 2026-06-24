---
title: "人类参与环节（Human-in-the-Loop）"
outline: deep
---

# 人类参与环节（Human-in-the-Loop）

> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 
> **领域**: ai

## 摘要

人类参与环节模式在智能体工作流中嵌入人工审核点——在关键决策节点暂停自动执行，等待人类确认、修正或提供额外信息后再继续，确保高风险操作的可控性和可信度。

## 详情

### 模式概述

HITL 的核心是**人机协同决策**——在智能体的自主执行中设置"检查点"，将关键决策权保留在人类手中 。

**常见检查点**：
- **审批点**：智能体提案，人类审批后执行（如发送邮件、修改数据库）
- **纠偏点**：智能体执行后，人类检查结果并修正偏差
- **补充点**：智能体遇到信息不足时，请求人类补充上下文

### 实践应用

- **内容发布**：AI 生成文章 → 人工审核 → 发布
- **代码部署**：AI 生成代码 → Code Review → 合并部署
- **医疗诊断**：AI 初步诊断 → 医生确认 → 治疗方案

### 关键要点

- HITL 在**高风险、低容错**场景中必不可少
- 检查点数量需要平衡——太多降低自动化效率，太少失去控制
- 人类反馈应该**结构化**——便于智能体学习和复用

## 关联

- 相关概念: [护栏与安全模式（Safety Guardrails）](/agent/concept-safety-guardrails), [Agent 质量评估](/agent/concept-agent-evaluation), [反思（Reflection）](/agent/concept-reflection), [路由（Agent Routing）](/agent/concept-agent-routing), [Agent：从可控性到自主反思](/agent/concept-agent-controllability)
- 参见: [Agent 设计模式](/agent/topic-agentic-design-patterns)

## 引用来源

- [1]  — 第 13 章：人类参与环节模式概述、实践应用、代码示例

## 变更记录

- 2026-05-31: 初始创建，来源 Agentic Design Patterns 电子书第 13 章
