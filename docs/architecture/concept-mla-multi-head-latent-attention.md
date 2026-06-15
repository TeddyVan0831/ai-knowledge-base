---
title: "MLA：多头潜在注意力（Multi-head Latent Attention）"
outline: deep
---

# MLA：多头潜在注意力（Multi-head Latent Attention）

> **类型**: concept
> **创建时间**: 2026-06-09
> **最后更新**: 2026-06-09
> **来源**: 

## 摘要
MLA（Multi-head Latent Attention）是 DeepSeek V3 的核心创新之一，通过对 KV 向量进行**低秩联合压缩**到潜空间（Latent Space），将 KV Cache 占用的显存大幅减少约 **14 倍**。MLA 的本质是纯粹的**存储优化技术**，不是为提升模型智能程度，而是让 KV Cache 占用的显存大幅减少，从而支持更长的上下文或更低的推理成本 。

## 核心概念

### 背景：为什么需要 KV Cache？

在 Transformer 自回归生成中，模型一次输出一个字：

- 已生成的 1300 个 Token 各自对应一个 Q、一个 K、一个 V
- 新的 Q 需要与**所有历史 K** 逐一计算相关度
- **过去的 Q 可以丢弃**（相关度已计算完毕），但**过去的 K 和 V 必须缓存**
- 因此策略：缓存所有 K 和 V、丢弃所有 Q → **KV Cache** 

### KV Cache 的显存压力

以 GPT-3 为例（96 头 × 96 层 × 1300 Token）：
- 仅 600 个汉字的输入，KV Cache 就要占约 **12 GB** 显存
- 线性关系：13000 Token → 120 GB，13 万 Token → 1200 GB
- 现代模型支持 20 万 Token（MiniMax-01 甚至支持 400 万 Token）→ 显存压力巨大 

DeepSeek V3（128 头 × 61 层 × 1300 Token，不用 MLA 时 KV Cache 约 13 GB） 

### 已有的压缩方案对比

| 方案 | 英文全称 | 核心思路 |
|------|----------|----------|
| **MHA** | Multi-Head Attention | 标准多头注意力，无损但缓存最大 |
| **GQA** | Grouped Query Attention | Q 分组共享 KV，减少缓存但有性能折损 |
| **MQA** | Multi-Query Attention | 所有 Q 共享一套 KV，缓存最小但性能折损严重 |
| **MLA** | Multi-head Latent Attention | DeepSeek 的方案：在潜空间中做低秩压缩  |

### MLA 的核心原理

**对 KV 进行低秩联合压缩**，将高维 KV 向量压缩到低维潜空间向量，推理时再还原：

1. **下采样（压缩）**：用矩阵 W^{DKV} 将 KV（7168 维）压缩为 512 维潜向量
2. **上采样（还原）**：用 W^{UK} 还原 K，用 W^{UV} 还原 V
3. **KV 联合压缩**：K 和 V 被压缩到**同一个** 512 维向量中，通过两个不同的上采样矩阵还原 

### MLA 的极致效率优化

- **矩阵合并**：W^{UK} 与 W^Q 合并（还原出的 K 用来和 Q 做计算），W^{UV} 与 W^O 合并
- **实际效果**：推理过程中**不需要执行"还原"步骤**——压缩态的 KV 直接参与后续计算 

### 压缩比例

根据 DeepSeek V3 配置：

- **KV 压缩维度（d_c）**：**512**
- 原始向量维度：7168
- **压缩比**：7168 ÷ 512 ≈ **14 倍**
- Q 也被压缩（d_c'）：1,536

实际 KV Cache 从 ~32.5 亿数字压缩至 ~0.41 亿数字（1300 Token 时） 

### MLA 的本质定位

**MLA 不是为提升模型"聪明程度"，而是一个纯粹的存储优化技术。** 对模型效果本身并无直接贡献 

## 关联
- 相关概念: [KV Cache](/architecture/concept-kv-cache)（KV Cache 原理）
- 相关概念: [KV Cache 动态压缩](/architecture/concept-kv-cache-compression)（KV Cache 动态压缩）
- 相关概念: [DeepSeekMoE：混合专家架构](/architecture/concept-deepseek-moe)（DeepSeekMoE 架构，MLA 的兄弟优化）
- 相关概念: [MTP：多 Token 预测（Multi-Token Prediction）](/architecture/concept-mtp-multi-token-prediction)（V3 的另一项训练优化）
- 相关概念: [Loss-Free Load Balancing：无辅助损失的 MoE 负载均衡](/architecture/concept-loss-free-load-balancing)（V3 的另一项 MoE 优化）
- 相关概念: [FP8 混合精度训练](/architecture/concept-fp8-mixed-precision)（V3 的混合精度训练）
- 相关概念: [推理模型与 DeepSeek R1：从 R1-Zero 到多阶段训练](/base-models/concept-reasoning-models-deepseek-r1)（R1 推理模型同样基于 V3 MLA 底座）
- 相关概念: [Transformer 架构](/base-models/concept-transformer-architecture)（Transformer 多头注意力）

## 引用来源
- [1]  — KV Cache 原理与显存压力
- [2]  — MLA 核心原理、压缩比例、本质定位

## 变更记录
- 2026-06-09: 初始创建，来源 
