---
title: "DeepSeek（深度求索）"
outline: deep
---

# DeepSeek（深度求索）

> **创建时间**: 2026-06-21
> **最后更新**: 2026-06-21
> **来源**: 综合知识库多处引用
> **类型**: entity
> **创建时间**: 2026-06-21
> **最后更新**: 2026-06-21
> **来源**: 综合知识库多处引用
> **领域**: ai

## 摘要

DeepSeek 是中国 AI 公司深度求索（DeepSeek AI），以 MoE + MLA 低成本路线著称，前沿旗舰模型全开源。代表模型包括 DeepSeek V3（671B MoE）、DeepSeek R1（推理模型）、DeepSeek V4（2026.04）。

## 详情

### 核心定位

- **路线**：MoE 稀疏激活 + MLA 潜在注意力，在有限算力下追求极限性能
- **开源策略**：V3/V4 全开源权重，社区生态活跃
- **影响力**：R1 推理模型引发全球 RL for Reasoning 浪潮

### 代表模型

| 模型 | 发布时间 | 参数 | 核心创新 |
|------|---------|------|---------|
| DeepSeek V3 | 2024.12 | 671B（37B 激活） | MoE 256 专家 + MLA + 无辅助损失负载均衡 |
| DeepSeek R1 | 2025.01 | 基于 V3 底座 | 纯 RL 训练推理能力 |
| DeepSeek V4 | 2026.04 | — | 原生 MTP 多 Token 预测 |

### 知识库中的相关页面

- [DeepSeekMoE：混合专家架构](/architecture/concept-deepseek-moe) — V3 的 MoE 架构详解
- [MLA：多头潜在注意力（Multi-head Latent Attention）](/architecture/concept-mla-multi-head-latent-attention) — MLA 注意力机制
- [MTP：多 Token 预测（Multi-Token Prediction）](/architecture/concept-mtp-multi-token-prediction) — MTP 多 Token 预测
- [推理模型与 DeepSeek R1：从 R1-Zero 到多阶段训练](/base-models/concept-reasoning-models-deepseek-r1) — R1 推理模型
- [Loss-Free Load Balancing：无辅助损失的 MoE 负载均衡](/architecture/concept-loss-free-load-balancing) — 无辅助损失负载均衡

## 关联

- 相关实体: [Jina Embeddings V4](/base-models/model-jina-embedding)
- 相关概念: [DeepSeekMoE：混合专家架构](/architecture/concept-deepseek-moe), [推理模型（Reasoning Models）](/base-models/concept-reasoning-models)

## 引用来源

- 综合知识库中 notes-40（V3 技术报告）、notes-39（R1 推理模型）、article-1（大语言模型简史）等多处引用

## 变更记录

- 2026-06-21: 初始创建，综合知识库多处数据汇总
