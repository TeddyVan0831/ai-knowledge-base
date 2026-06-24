---
title: "DeepSeekMoE：混合专家架构"
outline: deep
---

# DeepSeekMoE：混合专家架构

> **创建时间**: 2026-06-09
> **最后更新**: 2026-06-09
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-06-09
> **最后更新**: 2026-06-09
> **来源**: 
> **领域**: ai

## 摘要
DeepSeekMoE 是 DeepSeek V3 采用的**混合专家（Mixture of Experts）架构**的改进版本。总参数量 671B，但每次推理仅激活约 370 亿（占总参数约 1/20）。核心创新为**细粒度专家分割**和**共享专家**机制，每层 256 个路由专家 + 1 个共享专家，每次激活 Top-K=8 个路由专家 + 1 个共享专家 = 共 9 个 。

## 核心概念

### MoE 的基本思想

- **核心目标**：模型总参数量可以很大，但每次推理只激活其中一部分 → 降低推理成本
- **类比**：类似人脑——处理不同任务时，不同神经元区域被点亮，而非全部神经元同时工作
- **分工方式**：专家间的分工不是人为按领域（数学/文学）划分的，而是在训练过程中**自动分化**出来的
- **架构位置**：MoE 在每层 Decoder 内部用 MoE 结构替换原有的前馈网络（FFN）模块，注意力模块（MLA）保持不变 

### DeepSeekMoE 两大创新

#### 创新一：细粒度专家分割（Expert Granularity）

- 专家应该拆得更细，但**不增加总计算量**
- 公平比较原则：将一个专家的 FFN 拆分成 M 个更小的专家，每个小专家的隐藏维度变为原来的 1/M
- 举例：原始方案 32 个专家 × 维度 1000 → 拆分后 160 个专家（32×5）× 维度 200（1000÷5），计算量完全相同
- DeepSeek V3 每层多达 **256 个路由专家**（远超 GPT-4 推测的 16 个） 

#### 创新二：共享专家（Shared Expert）

- 处理各种任务时需要**公共知识**，因此设定不受门控网络控制的共享专家
- 共享专家每次**必定激活**
- 如果共享专家占 1 个名额，路由专家从选 4 个变成选 3 个（保持总激活数不变） 

### DeepSeek V3 的 MoE 具体配置

| 参数项 | 数值 |
|--------|------|
| Transformer 总层数 | 61 |
| 使用 MoE 的层 | 第 3-60 层（前 3 层为普通 FFN） |
| 每层路由专家数 | 256 |
| 每层共享专家数 | 1 |
| 每次激活 Top-K | 8（路由）+ 1（共享）= **9 个** |

> 前 3 层为什么不用 MoE？讲解者表示也没有完全理解 

### MoE 门控机制

- **V3 使用 Sigmoid**（非通用 Softmax）：`raw_score → Sigmoid → Top-K 选择 → 对选中的归一化 → 门控值`
- 专家代表向量与输入做相似度计算（点积），或直接用门控神经网络处理输入 → 输出 N 个数值 → Top-K 选择 

### 与 GPT-4 MoE 的对比

| 对比项 | GPT-4（推测）* | DeepSeek V3 |
|--------|-------------|-------------|
| 总参数量 | ~1.8 万亿 | 6710 亿 |
| Transformer 层数 | 120 | 61 |
| 每层专家数 | 16 | 256 路由 + 1 共享 |
| 每次激活 | 未明确 | 9 个（8 路由 + 1 共享） |

> \* GPT-4 架构参数从未被 OpenAI 官方公开，数据来源为第三方推测 

## 关联
- 相关概念: [MLA：多头潜在注意力（Multi-head Latent Attention）](/architecture/concept-mla-multi-head-latent-attention)（MLA 也是 V3 的核心优化方向）
- 相关概念: [MTP：多 Token 预测（Multi-Token Prediction）](/architecture/concept-mtp-multi-token-prediction)（V3 的另一项训练优化）
- 相关概念: [Loss-Free Load Balancing：无辅助损失的 MoE 负载均衡](/architecture/concept-loss-free-load-balancing)（Loss-Free 解决 MoE 负载均衡问题）
- 相关概念: [FP8 混合精度训练](/architecture/concept-fp8-mixed-precision)（V3 的混合精度训练优化）
- 相关概念: [推理模型与 DeepSeek R1：从 R1-Zero 到多阶段训练](/base-models/concept-reasoning-models-deepseek-r1)（R1 推理模型同样基于 V3 MoE 底座）
- 相关概念: [推理模型（Reasoning Models）](/base-models/concept-reasoning-models)（推理模型通用概念）
- 参见: [知识蒸馏](/training-optimization/concept-knowledge-distillation)（知识蒸馏，小模型通过蒸馏获得推理能力）

## 引用来源
- [1]  — MoE 基本原理与架构定位
- [2]  — 细粒度专家分割 + 共享专家两大创新
- [3]  — V3 的具体 MoE 配置
- [4]  — 门控机制（Sigmoid vs Softmax）

## 变更记录
- 2026-06-09: 初始创建，来源 
