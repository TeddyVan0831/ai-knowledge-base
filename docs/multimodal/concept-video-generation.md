---
title: "视频生成模型"
outline: deep
---

# 视频生成模型

> **类型**: concept
> **创建时间**: 2026-06-04
> **最后更新**: 2026-06-04
> **来源**: 

## 摘要

视频生成模型的技术演进——从 ViViT（视频理解）→ 3D UNet（时空建模）→ DiT/Diffusion Transformer（架构革命）→ Sora（DiT 规模化实践）→ Imagen Video。核心突破是 Sora 用 DiT 替代传统 U-Net，通过 Patch 化将视频转为 token 进行扩散训练。

## 详情

### 文生图的全部逻辑，在文生视频里同样成立——只是更复杂

视频生成 = 图片生成 + 时间维度（时序建模）。需要同时理解空间内容（画面中有什么）和时间连续性（前后帧的关系）。

### 技术演进路线

| 阶段 | 模型/技术 | 时间 | 核心贡献 |
|------|----------|------|---------|
| 视频理解 | ViViT | 2021 | Video Vision Transformer——将视频切成 patches，用 Transformer 理解视频内容  |
| 视频理解 | C3D / I3D / SlowFast | 2014-2020 | 3D 卷积——在 2D 卷积基础上加时间维度（3D 卷积核），同时提取空间+时间特征  |
| 视频生成骨干 | 3D UNet | 2022 | Imagen Video——在 2D UNet 基础上加 3D 卷积层（时间注意力），实现帧间一致性  |
| **架构革命** | **DiT (Diffusion Transformer)** | 2023 | 用 Transformer 替代 U-Net 作为扩散模型骨干——patch 化输入、scaling 属性、自然支持多模态条件  |
| 规模化实践 | **Sora (OpenAI)** | 2024 | DiT 的工程化巅峰——极大 patch size（1×1×1=原生 token）、极大规模训练数据、涌现物理规则  |

### DiT（Diffusion Transformer）—— 架构革命

DiT 是 2023 年由 William Peebles 和 Saining Xie 发表的论文（UC Berkeley），核心创新是用 Transformer 替代传统扩散模型的 U-Net 。

**为什么用 Transformer 替换 U-Net？**

| 维度 | U-Net | DiT (Transformer) |
|------|-------|-------------------|
| 架构形态 | U 型 + 跳连 | Transformer block |
| Scaling 属性 | 平庸 | 强（符合 Transformer scaling law） |
| 多模态条件 | 弱 | 自然支持（Cross Attention / In-Context Conditioning） |
| Patch 化 | 不自然 | 自然（图像切成 patch 就是 token） |

**DiT vs ViT 的关键区别**：DiT 继承了 ViT 的 patch 化输入和 Transformer block，但做了针对扩散模型的适配——patch 化 + latent + 时序 embedding。

### Sora 的完整架构

Sora = DiT 的工程化规模化。关键步骤 ：

1. **压缩网络**：视频 → VAE → 潜空间（时空 patch）
2. **Patch 化**：1×1×1 = 一个原生 token（不是把视频预处理成固定大小的 patch，而是把最小的视频单元当作 token）
3. **扩散训练**：在潜空间中加噪声→去噪
4. **条件注入**：文字→CLIP→Cross Attention 控制生成内容
5. **解码**：潜空间→VAE→像素空间视频

**Sora 现象级效果的原因**：
- Scale 优势——极大 patch size + 极大规模训练数据
- 涌现出物理规则理解（水花飞溅、食物融化等自然的物理行为）

### Imagen Video（Google, 2022）

用 3D UNet + 级联扩散架构（7 个子模型）实现高质量视频生成。引入**时间注意力**层——每帧内部做空间注意力 + 帧与帧之间做时间注意力，保证帧间一致性 。

### 工程化：如何生成高分辨率视频

| 策略 | 说明 |
|------|------|
| **级联缩放** | 先低分辨率，再逐步上采样（文本→64×64→256×256→1024×1024） |
| **超分模型** | 专门训练的超分辨率模型把视频从低清变高清 |
| **帧插值** | 在关键帧之间插入过渡帧，提升帧率 |

## 关联

- 相关概念: [图像生成技术](/multimodal/concept-image-generation), [多模态 Transformer](/multimodal/concept-multimodal-transformer), [多模态前沿：Agent 构建与视频 AIGC](/multimodal/concept-multimodal-edge), [视觉识别技术](/multimodal/concept-vision-recognition)
- 参见: [模型优化](/training-optimization/topic-model-optimization)

## 引用来源

- [1]  — ViViT→3D UNet→DiT→Sora→Imagen Video 完整演进

## 变更记录

- 2026-06-04: 初始创建
