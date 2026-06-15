---
title: "WebRL：网页强化学习框架"
outline: deep
---

# WebRL：网页强化学习框架

> **类型**: concept
> **创建时间**: 2026-06-12
> **最后更新**: 2026-06-12
> **来源**: 

## 摘要

WebRL（Web Reinforcement Learning）是智谱提出的自进化在线课程强化学习框架，是 AutoGLM 的核心创新。通过结果监督奖励模型（ORM）提供自动化反馈信号，结合课程学习实现模型自我迭代，将小模型在 Web 操作任务上的成功率从 4.8%-6.1% 大幅提升至 42%-49%。

## 详情

### 名称澄清

论文标题全称为「Self-Evolving Online Curriculum Reinforcement Learning」，中文译为"自进化在线课程强化学习框架"。授课人曾误以为"在线课程"是翻译错误（应为 Online Learning），但论文原文（arXiv: 2411.02337）确为此标题，翻译准确。

### WebArena 环境

WebArena 是一个网页交互模拟环境 + 评测数据集。论文使用 **WebArena-Lite** 版本（完整 WebArena 的子集）：

- 包含多个模拟网站（各有独立域名）
- 评测使用 **165 个测试用例**（源自完整 WebArena 的 800+ 任务集）
- 每个任务平均约需 **10 个步骤**完成
- 每个任务有明确的标准目标



### 强化学习整体流程

```
1. 智能体（语言模型）在 WebArena 中执行任务
2. 记录每一步操作（历史行动）
3. 记录最终状态的页面
4. ORM 根据（任务指令 + 历史行动 + 最终状态）给出奖励
5. 强化学习算法根据奖励信号优化模型
6. 循环迭代
```



### 数据策略

**人工轨迹数据**：
- 收集约 **1,000 条 Oracle 轨迹**（由智谱真人完成）
- 每条轨迹包含：用户指令 + 中间点击步骤 + 成功结果
- 可直接用于 SFT 或 LoRA 微调

**强化学习自生成数据**：
- 通过 WebRL 框架让模型自我探索和试错
- ORM 提供自动反馈信号，无需人工标注
- 实现规模化数据生成



### 课程学习（自进化）

自进化（Self-evolving）= 训练过程中动态调整难度：

- 初始阶段：简单任务（步骤少、目标明确）
- 随着模型能力提升：逐步增加任务难度和复杂度
- 最终覆盖所有 WebArena-Lite 中的任务



### 核心性能数据

| 模型 | 成功率 | 提升幅度 |
|------|--------|---------|
| GLM-4-9B（原生） | 6.1% | 基线 |
| GLM-4-9B（+WebRL） | **43.0%** | 7.05x |
| Llama 3.1 8B（原生） | 4.8% | 基线 |
| Llama 3.1 8B（+WebRL） | **42.4%** | 8.83x |
| Llama 3.1 70B（+WebRL） | **49.1%** | 10.23x |



> ⚠️ **公平性质疑**：授课人指出与 GPT-4o 对比（13.9%）"稍微有一点点不公平"，因为 GLM-4-9B 在 WebArena 上做了微调而 GPT-4o 没有，且 GPT-4o 未见网页点击类任务。

### 与 RLHF 的关系

- ORM 提供自动化、大规模的二进制奖励（0/1）
- RLHF 提供人工精细化的质量评估
- 两者可结合使用，类似主流 LLM 训练流程
- AutoGLM 产品界面中用户可"点赞/踩"，这些数据可用于 RLHF 

## 关联

- 相关概念: [AutoGLM：智能体操作框架](/agent/concept-autoglm), [ORM：结果监督奖励模型](/training-optimization/concept-orm-reward-model), [RLHF（基于人类反馈的强化学习）](/training-optimization/concept-rlhf)
- 相关概念: [Agent 质量评估](/agent/concept-agent-evaluation), [Agent：从可控性到自主反思](/agent/concept-agent-controllability)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — WebRL 框架详情、WebArena 环境、数据策略、课程学习

## 变更记录

- 2026-06-12: 初始创建，来源 
