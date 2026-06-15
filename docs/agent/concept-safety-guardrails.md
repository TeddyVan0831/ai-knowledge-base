---
title: "护栏与安全模式（Safety Guardrails）"
outline: deep
---

# 护栏与安全模式（Safety Guardrails）

> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 

## 摘要

护栏与安全模式为智能体系统构建多层次安全防护——包括输入过滤、输出审查、行为约束和越狱防御，确保 AI 系统在开放环境中安全可靠地运行。

## 详情

### 模式概述

安全护栏的核心是**防御纵深**——在智能体系统的多个层面设置安全检查点，从输入到输出的完整链路中防止有害行为 。

### 安全层次

**1. 输入护栏（Input Guardrails）**：
- 检测越狱攻击（Jailbreaking）
- 过滤恶意指令和有害内容
- 防止提示注入（Prompt Injection）

**2. 输出护栏（Output Guardrails）**：
- 审查生成内容是否合规
- 检测偏见、歧视、有害建议
- 阻止敏感信息泄露

**3. 行为护栏（Behavioral Guardrails）**：
- 限制智能体的操作权限
- 设置 API 调用频率和范围上限
- 防止未授权的外部访问

### 实践实现

书中提供了 CrewAI 和 Vertex AI 的实战代码示例 ，展示了如何在实际工程中实现安全防护。

### 关键要点

- 安全护栏是**生产级智能体**的必备组件
- 多层防护优于单一检查——攻击者可能绕过某一层
- 安全策略需要**持续更新**——新的攻击手法不断出现

## 关联

- 相关概念: [异常处理与恢复（Error Handling & Recovery）](/agent/concept-error-recovery), [人类参与环节（Human-in-the-Loop）](/agent/concept-human-in-the-loop), [Agent 质量评估](/agent/concept-agent-evaluation), [Agent：从可控性到自主反思](/agent/concept-agent-controllability)
- 参见: [Agent 设计模式](/agent/topic-agentic-design-patterns)

## 引用来源

- [1]  — 第 18 章：护栏与安全模式、CrewAI/Vertex AI 代码示例、工程化可靠智能体

## 变更记录

- 2026-05-31: 初始创建，来源 Agentic Design Patterns 电子书第 18 章
