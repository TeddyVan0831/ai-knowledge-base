---
title: "图像生成技术"
outline: deep
---

# 图像生成技术

> **类型**: concept
> **创建时间**: 2026-06-04
> **最后更新**: 2026-06-04
> **来源**: 

## 摘要

图像生成技术从 GAN 到 Stable Diffusion 的演进脉络，核心矛盾是多样性 vs 可控性。关键里程碑：VAE（多样性突破）→ 扩散模型/DDPM（预测噪声）→ 分类器指导（第一次可控）→ DALL·E 2（CLIP 打通图文）→ Latent Diffusion/Stable Diffusion（在潜空间生图）。

## 详情

### 核心矛盾：多样性 vs 可控性

图像生成模型的两条主线始终共存又冲突——多样性（创造力）要求生成全新图片，可控性（听指令）要求精确控制每个细节。最终平衡方案在数学空间（向量空间）中找到 。

### 演进路线

| 阶段 | 模型 | 时间 | 核心贡献 |
|------|------|------|---------|
| 有限多样性 | GAN | 2014 | 生成+辨别对抗，但无创造力（临摹不是创造） |
| 多样性突破 | VAE | 2013/2015 | 输出高斯分布参数 μ、σ，在曲线随机采样，创造全新图片  |
| 范式转换 | DDPM | 2020 | 从"预测图"改为"预测噪声"，预测噪声任务更简单；改进版 U-Net 架构  |
| 第一次可控 | 分类器指导 | 2021 | 加分类器做指导员，去噪过程中修正方向  |
| 图文打通 | DALL·E 2 | 2022 | CLIP 联合训练 4 亿对图文数据，证明文字和图片向量可在同一空间互通；Prior + Decoder 两阶段生成  |
| 效率革命 | Latent Diffusion / Stable Diffusion | 2022 | 不在像素空间做扩散，在潜空间（Latent Space）里完成，效率大幅提升  |

### 关键概念

- **像素空间 vs 潜空间**：像素空间（人类看懂）vs 潜空间 Latent Space（机器看懂，低维向量）
- **VAE 本质**：不输出确定向量，输出高斯分布参数，随机采样后还原，所以能创造训练集里从未出现过的图 
- **扩散模型本质**：Forward 加噪声 → Reverse 去噪还原。DDPM 核心创新是把"预测图"改为"预测噪声" 
- **CLIP**：联合训练 4 亿对图文数据，文字和图片的向量在同一空间 
- **Stable Diffusion** = LDM = VAE Encoder → 潜空间扩散去噪 → VAE Decoder 还原到像素空间 

### 技术趋势

自回归 vs 扩散模型可替换——DALL·E 2 的 Prior 可选用扩散或自回归；GPT-4o 原生图像生成（2025）全面用自回归替代扩散模型 。

## 关联

- 相关概念: [多模态 Transformer](/multimodal/concept-multimodal-transformer), [多模态前沿：Agent 构建与视频 AIGC](/multimodal/concept-multimodal-edge), [视觉识别技术](/multimodal/concept-vision-recognition), [视频生成模型](/multimodal/concept-video-generation), [数字人核心技术与应用](/multimodal/concept-digital-human), [AI 视频生成工作流](/multimodal/concept-ai-video-workflow)
- 参见: [模型优化](/training-optimization/topic-model-optimization)

## 引用来源

- [1]  — GAN→VAE→扩散模型→DALL·E 2→Latent Diffusion 完整演进

## 变更记录

- 2026-06-04: 初始创建
