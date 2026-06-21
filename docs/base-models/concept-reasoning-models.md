---
title: "推理模型（Reasoning Models）"
outline: deep
---

# 推理模型（Reasoning Models）

> **类型**: concept
> **创建时间**: 2026-05-27
> **最后更新**: 2026-05-27
> **来源**: 

## 摘要

推理模型是 2024 年起 LLM 发展的新范式，从模式匹配转向结构化逻辑推理，代表性模型包括 OpenAI o1/o3 和 DeepSeek-R1。

## 详情

### 核心理念

传统 LLM 擅长「系统 1 思维」（快速、直觉），但在复杂推理任务上有所欠缺。推理模型采用 **「长链思维」（Long CoT）** ——内部的推理轨迹，使模型能够通过分解问题、批判自己的解决方案并探索替代方案来"思考"问题 。

### OpenAI o1 系列

| 模型 | 发布时间 | 关键指标 |
|------|---------|---------|
| o1-preview | 2024-09-12 | AIME 2024 解决 74%-93% 的问题，超越 GPT-4o 的 12%  |
| o1-mini | 2024 | 更便宜更快版本，成本为完整版 o1 的 20%，在编码任务表现出色  |
| o3-mini | 2025-01-31 | SWE-Bench Verified ~49%，Codeforces Elo ~2073  |
| o3 | 2025-04-16 | ARC-AGI 87.5%（超人类 85%），SWE-Bench 71.7%，Codeforces 2727 Elo（全球前 200），FrontierMath 25.2%（vs 此前 2.0%）  |

### DeepSeek-R1

- 训练成本约 **560 万美元**，仅为西方公司投资的一小部分 
- 推理成本相比 OpenAI o1 可进一步降低 **20 到 50 倍** 
- 开源设计挑战了 AI 领域的传统规范 

## 关联

- 相关概念: [大语言模型发展简史](/base-models/concept-llm-history), [RLHF（基于人类反馈的强化学习）](/training-optimization/concept-rlhf), [贝叶斯推理](/base-models/concept-bayesian-reasoning), [推理技术（Reasoning Techniques）](/base-models/concept-reasoning-techniques)
- 参见: [模型优化](/training-optimization/topic-model-optimization)

## 引用来源

- [1]  — 第七章推理模型、第八章 DeepSeek-R1

## 变更记录

- 2026-05-27: 初始创建
