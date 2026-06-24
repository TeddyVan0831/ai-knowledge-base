---
title: "RLHF（基于人类反馈的强化学习）"
outline: deep
---

# RLHF（基于人类反馈的强化学习）

> **创建时间**: 2026-05-27
> **最后更新**: 2026-05-27
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-27
> **最后更新**: 2026-05-27
> **来源**: 
> **领域**: ai

## 摘要

RLHF（Reinforcement Learning from Human Feedback）是 2022 年 OpenAI 引入的后训练对齐技术，通过人类排名反馈训练奖励模型，再用 PPO 强化学习微调 LLM，使模型生成更符合人类偏好的输出。

## 详情

### 解决的问题

GPT-3 等模型存在"幻觉"问题——生成内容与事实不符，甚至"一本正经地胡说八道" 。RLHF 解决了 SFT（监督微调）的可扩展性限制 。

### 两阶段过程

1. **训练奖励模型**：人类注释者对模型生成的多个输出进行排名，创建偏好数据集，训练奖励模型学习根据人类反馈评估输出质量 
2. **使用强化学习微调 LLM**：奖励模型使用 PPO（近端策略优化）指导 LLM 微调，通过迭代更新使模型生成更符合人类期望的输出 

### 与 SFT 的区别

- **SFT**：需要人类编写完整输出，劳动密集型，可扩展性差 
- **RLHF**：只需人类对输出排名，更高效的数据收集和标注 

### ChatGPT 的 RLHF 实践

ChatGPT 通过 RLHF 学会了生成不仅有用而且诚实和无害的响应，人类培训师根据质量对响应进行排名，使模型逐步改进表现 。

### 与推理模型的对比

DeepSeek-R1-Zero 完全消除了 SFT 阶段，直接从预训练模型开始基于规则的 RL（GRPO），代表了 RLHF 的演进方向 。

## 关联

- 相关概念: [大语言模型发展简史](/base-models/concept-llm-history), [推理模型（Reasoning Models）](/base-models/concept-reasoning-models), [Few-Shot Prompting](/base-models/concept-few-shot-prompting), [WebRL：网页强化学习框架](/training-optimization/concept-webrl), [ORM：结果监督奖励模型](/training-optimization/concept-orm-reward-model)
- 参见: [模型优化](/training-optimization/topic-model-optimization), [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — 第四章后训练对齐：SFT 与 RLHF

## 变更记录

- 2026-05-27: 初始创建
