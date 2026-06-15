---
title: "Agent 质量评估"
outline: deep
---

# Agent 质量评估

> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 

## 摘要

Agent 质量评估涵盖从原型到生产的全流程——包括 LM Judge 评估、CI/CD 质量关卡、安全部署策略（金丝雀/蓝绿）、可观测性（OpenTelemetry Traces）和持续优化闭环。

## 详情

### 评估作为质量关卡

传统软件的 `output == expected` 断言不适用于概率性 Agent。需要 LM Judge 评估"质量"——Agent 是否做了该做的、没做不该做的、语气是否恰当 。

### 自动化 CI/CD 管道

构建评估数据集→自动运行测试→对比基准→判定 Go/No-Go。每次代码变更或模型更新都通过统一的质量管道 。

### 安全部署策略

| 策略 | 说明 |
|------|------|
| **金丝雀发布** | 先向少量用户发布新版本，监控质量指标后逐步扩大 |
| **蓝绿部署** | 同时运行新旧两个版本，通过流量切换实现零停机更新 |
| **特性开关** | 通过配置开关控制新功能的可见性 |

### 可观测性

通过 OpenTelemetry Traces 暴露完整推理轨迹：模型的内部独白、选择的工具、生成的参数、观察的结果 。

## 关联

- 相关概念: [Agent Ops](/agent/concept-agent-ops), [护栏与安全模式（Safety Guardrails）](/agent/concept-safety-guardrails), [反思（Reflection）](/agent/concept-reflection), [AI 表格数据识别与模型评测方法论](/industry-cases/concept-ai-table-recognition-evaluation)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)

## 引用来源

- [1]  — Agent 质量评估完整章节
- [2]  — Evaluation as a Quality Gate 章节

## 变更记录

- 2026-05-31: 初始创建
