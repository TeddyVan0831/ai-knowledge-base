---
title: "Agent Ops"
outline: deep
---

# Agent Ops

> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: , 

## 摘要

Agent Ops 是针对随机性 Agent 系统的结构化运维方法——从 DevOps→MLOps→GenAIOps→AgentOps 的演进链，涵盖质量评估、指标驱动开发、可观测性调试和人类反馈引导。

## 详情

### 为什么需要 Agent Ops

传统软件单元测试可以简单断言 `output == expected`，但 Agent 的响应是概率性的。语言很复杂，通常需要 LLM 来评估"质量"——Agent 的响应是否做了该做的事、没做不该做的事、语气是否恰当 。

### 核心组件

| 组件 | 说明 |
|------|------|
| **LM Judge 质量评估** | 用 LLM 代替传统的 Pass/Fail 测试，评估 Agent 响应质量 |
| **指标驱动开发** | 部署前的 Go/No-Go 决策，基于关键业务指标 |
| **OpenTelemetry 可观测性** | 通过 Trace 回答"为什么"——暴露完整推理轨迹 |
| **人类反馈引导** | 引导自动化方向，持续优化 Agent 行为 |

### 运维体系演进

```
DevOps → MLOps → GenAIOps
                    ├── AgentOps
                    └── RAGOps
              └── LLMOps
                    └── PromptOps
```

## 关联

- 相关概念: [Agent 质量评估](/agent/concept-agent-evaluation), [资源感知优化（Resource-Aware Optimization）](/agent/concept-resource-optimization), [护栏与安全模式（Safety Guardrails）](/agent/concept-safety-guardrails)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)

## 引用来源

- [1]  — Agent Ops 完整章节
- [2]  — Agent Ops 章节

## 变更记录

- 2026-05-31: 初始创建
