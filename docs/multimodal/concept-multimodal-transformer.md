---
title: "多模态 Transformer"
outline: deep
---

# 多模态 Transformer

> **创建时间**: 2026-05-29
> **最后更新**: 2026-05-31
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-29
> **最后更新**: 2026-05-31
> **来源**: 
> **领域**: ai

## 摘要

多模态 Transformer 是从 CNN 演进到图文统一架构的技术路线，涵盖 ResNet（2015）→ VL-BERT（2019）→ ViT（2021）→ Swin Transformer（2021）→ CLIP（2021）等关键论文，实现了文字与图片在统一数学空间中的融合。

## 详情

### 技术演进路线

```
ResNet (2015) → VL-BERT 类 (2019) → ViT (2021) → Swin Transformer (2021) → CLIP (2021)
```

### ResNet（2015）：残差网络的革命

- **作者**：何恺明（Kaiming He），微软亚洲研究院 
- **核心问题**：深度退化——56 层网络训练误差反而比 20 层大 
- **残差连接**：Output = F(x) + x，保留浅层信息，允许层"偷懒" 
- **对 Transformer 的影响**：直接借鉴残差连接和多头机制（多头来自 CNN 多卷积核思路），使网络可达上千层 

### ViT（Vision Transformer, 2021）

- **机构**：Google Research + Google Brain 
- **核心思路**：图片切成 16×16 patch，每个 patch 对应 NLP 的 token，用纯 Transformer 做图像分类 
- **关键区别**：Patch 不可穷举（任意图片的任意 16×16 区域有无穷多种可能），与 token 不同 

### VL-BERT 类模型（2019）：图文融合 Transformer 先驱

- **地位**：五篇关键论文之一，时间上早于 ViT、Swin、CLIP 
- **核心思路**：将文字 token 和图片区域（RoI）向量通过分隔符拼接成一个长序列，一并送入 Transformer Encoder 处理 
- **历史意义**：这是 GPT-4O 多模态理解能力在概念层面上的早期探索——将不同模态统一为同一 Transformer 序列的思想 

### Swin Transformer（2021）

- **改进 ViT**：恢复尺度概念和局部注意力，弥补 ViT 切 patch 后丢失的空间信息 

### CLIP（2021）：打通文字与图片的数学空间

- **核心**：将文字和图片映射到同一向量空间，实现图文匹配 

### CNN vs Transformer：共存而非替代

- **CNN**：局部感知、平移不变性强、计算效率高
- **Transformer**：全局上下文、长程依赖、灵活性强
- **趋势**：两者融合而非替代，各自发挥优势 

## 关联

- 相关概念: [Transformer 架构](/base-models/concept-transformer-architecture), [大语言模型发展简史](/base-models/concept-llm-history)
- 参见: [模型优化](/training-optimization/topic-model-optimization)

## 引用来源

- [1]  — 多模态 Transformer 演进（ResNet→VL-BERT→ViT→Swin→CLIP）、图文混合序列、Patch 概念、残差连接

## 变更记录

- 2026-05-29: 初始创建
