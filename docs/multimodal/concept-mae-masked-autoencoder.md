---
title: "MAE（Masked Autoencoder）掩码自编码器"
outline: deep
---

# MAE（Masked Autoencoder）掩码自编码器

> **创建时间**: 2026-06-09
> **最后更新**: 2026-06-09
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-06-09
> **最后更新**: 2026-06-09
> **来源**: 
> **领域**: ai

## 摘要
MAE（Masked Autoencoder）是何恺明（Kaiming He）等人在 2021 年提出的**视觉自监督学习框架**，通过随机遮住 75% 图像块训练编码器和解码器，核心目标是**从极端困难的重建任务中学到深层视觉特征**。预训练完成后只保留编码器用于下游任务，解码器被丢弃。

## 核心概念

### 基本信息

- **论文**：*Masked Autoencoders Are Scalable Vision Learners*
- **作者**：何恺明（Kaiming He）等
- **时间**：2021 年 11 月（arXiv 预印本），2022 年 CVPR 正式发表
- **机构**：Facebook AI Research (FAIR)
- **影响力**：2024 年的 Sapiens 仍基于 MAE，说明其影响力持久 

### 核心算法流程

1. **输入**：一张完整图片，切成 patch 后随机遮住 75% 的 patch 
2. **编码器（Encoder）**：仅处理**可见的 25% patch**，提取特征向量 
3. **解码器（Decoder）**：接收编码器输出 + 被遮住 patch 的占位向量（learnable mask token），重建完整图片 
4. **损失函数**：重建图与原图的误差（仅在被遮住区域计算）

### 非对称架构（Asymmetric Design）

- **编码器**：工作量大，只处理可见 patch → 计算量降为原来的 1/4
- **解码器**：工作量小，处理全部 patch（可见 + 被遮），但结构轻量 

### 高遮挡率（75%）的必要性

- 图像冗余信息多：如果只遮住少量 patch，简单插值就能恢复，模型学不到东西
- 遮住 75% → 任务极具挑战性 → 被迫学习深层特征 → 讲师比喻为 **"穷人家的孩子早当家"**
- 训练数据量大时（如数亿张图），虽然单张只看 25%，但不同图片看到的不同 25% 互补 

### MAE 的核心价值

- **编码器泛化能力强**：在极端困难条件下训练出的编码器，抽出的特征更好用
- **抗过拟合**：不像"富二代"模型（给太多冗余数据导致记忆训练集），MAE 强迫模型真正理解
- **解码器训练后丢弃**：预训练完成后，解码器不需要了，只保留编码器用于下游任务 

### 与语言模型自监督的对比

| 维度 | 语言模型 | 视觉模型（MAE 之前） |
|------|----------|----------------------|
| 自监督方式 | 遮住下一个词 / 完形填空 | 缺乏有效的遮码策略 |
| 信息密度 | 语言信息密度高，遮几个字就是大挑战 | 图像冗余多，遮少量 patch 无意义 |
| 进展 | 自监督预训练已成主流 | 进展滞后于 NLP |

MAE 解决了视觉领域"如何有效做掩码自监督"的问题 。

## 关联
- 相关概念: [Meta Sapiens：人体视觉基座模型](/multimodal/concept-meta-sapiens)（Sapiens 基于 MAE + ViT 架构）
- 相关概念: [Humans-300M 数据集](/multimodal/concept-humans-300m-dataset)（Humans-300M 使用 MAE 做自监督预训练）
- 相关概念: [视觉识别技术](/multimodal/concept-vision-recognition)（CNN / ResNet 视觉识别）
- 相关概念: [Transformer 架构](/base-models/concept-transformer-architecture)（ViT 骨干网络）
- 相关概念: [图像生成技术](/multimodal/concept-image-generation)（VAE / Diffusion 生成模型）
- 相关实体: [NVIDIA H100 GPU](/base-models/model-h100)（训练硬件）

## 引用来源
- [1]  — MAE 基本信息
- [2]  — 核心算法流程
- [3]  — 非对称架构、高遮挡率、核心价值
- [4]  — 与语言模型自监督对比

## 变更记录
- 2026-06-09: 初始创建，来源 
