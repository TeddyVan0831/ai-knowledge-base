---
title: "MTP：多 Token 预测（Multi-Token Prediction）"
outline: deep
---

# MTP：多 Token 预测（Multi-Token Prediction）

> **创建时间**: 2026-06-09
> **最后更新**: 2026-06-09
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-06-09
> **最后更新**: 2026-06-09
> **来源**: 
> **领域**: ai

## 摘要
MTP（Multi-Token Prediction）是 DeepSeek V3 在训练阶段引入的**多 Token 预测辅助模块**。主模型预测下一个 Token 的同时，MTP 模块同时往前多看一步，通过额外的辅助预测提升训练时的主模型性能和输出稳定性。MTP 模块仅在训练时使用，推理时直接丢弃 。

## 核心概念

### 传统方式 vs MTP

| 方式 | 预测目标 |
|------|---------|
| 传统 | 一次只预测下一个 Token |
| MTP | 主模型预测下一个 Token，辅助模块同时往前多看一步  |

### MTP 的结构

- 主模型：61 层 Transformer Decoder
- MTP 模块：**1 层 Transformer Block**（相比主模型极轻量）
- 与主模型**共享 Embedding 层和输出头（Output Head）**
- MTP 独特参数约 115 亿（仅占主模型 6710 亿的约 **1.7%**）
- **实际配置**：DeepSeek V3 开源版本仅使用了 **1 个 MTP 模块**（`num_nextn_predict_layers=1`） 

### MTP 的工作机制

当主模型在基于 Token₁~Token₄ 预测 Token₅ 时，MTP 模块基于 Token₂~Token₅ 预测 Token₆ 

### MTP 的三大价值

1. **提升输出连贯性**：主模型在预测某个 Token 时，该位置的 Token 已被辅助模块从额外上下文窗口"预演"过
2. **提升稳定性**：主模型的 Top-K 概率分布可以与辅助模型的分布融合，减少关键 Token（如否定词"不"）的预测波动
3. **推理时不部署**：MTP 模块**仅在训练时使用**，推理时直接丢弃，主模型独立运行 

> 可选地在高并发场景下用辅助模块做推测解码以改善延迟 

## 关联
- 相关概念: [DeepSeekMoE：混合专家架构](/architecture/concept-deepseek-moe)（DeepSeekMoE 架构）
- 相关概念: [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai)（推测解码 / EAGLE / MEDUSA，推理时加速）
- 相关概念: [推理模型（Reasoning Models）](/base-models/concept-reasoning-models)（推理模型，同样涉及 MoE 底座 V3）

## 引用来源
- [1]  — MTP 原理、结构、价值

## 变更记录
- 2026-06-09: 初始创建，来源 
