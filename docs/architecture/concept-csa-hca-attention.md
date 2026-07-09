---
title: "CSA + HCA 混合注意力（百万级上下文解决方案）"
outline: deep
---

# CSA + HCA 混合注意力（百万级上下文解决方案）

> **类型**: concept
> **创建时间**: 2026-07-06
> **最后更新**: 2026-07-06
> **来源**: 
> **领域**: ai

## 摘要

DeepSeek V4 用 **CSA（Compressed Sparse Attention，压缩稀疏注意力）+ HCA（Heavily Compressed Attention，重压缩注意力）+ SWA（Sliding Window Attention）** 三大组件替代 V3.2 的 MLA + DSA 方案，在 1M 上下文下将 FLOPs 降至 V3.2 的 **10%-27%**、KV Cache 降至 **7%-10%**。这是"百万元上下文从理论可行变为实际高效"的关键架构突破。

> ⚠️ **命名澄清**：授课 PPT 中标注为 "DSA"，但根据 DeepSeek-V4 官方技术报告，V4 的核心方案是 **CSA + HCA 混合注意力**。DSA 是 V3.2 的方案，V4 已升级。

## 详情

### 一、为什么百万上下文是难题

**计算量与显存增长是 N² 指数级**：
- 传统全注意力下，百万级上下文推理一次至少需 **100 GB 显存**
- 根因：Transformer 自注意力机制——每个 token 都要与所有其他 token 建立关系（attention matrix），形成 N×N 矩阵

### 二、DeepSeek V4 的解决方案

> 🖼️ [图 2] **CSA + HCA 混合注意力方案** — 三大组件详图（CSA 4:1 压缩、Lightning Indexer、HCA 128:1 压缩、SWA 128 token 滑窗）+ 1M 上下文 FLOPs/KV Cache 节省对比 — 

#### 2.1 CSA（Compressed Sparse Attention，压缩稀疏注意力）

**4:1 压缩** + **Lightning Indexer 快速筛选**

| 步骤 | 流程 |
|------|------|
| ① Token 级压缩 | 每 4 个 token 压缩为 1 个（m=4）→ 1M → 25 万 |
| ② Lightning Indexer | 低秩查询打分 + Top-1024 筛选关键块 |
| ③ 共享 KV MQA | 选中条目同时作为 Key 和 Value |
| ④ 分组输出投影 | n_h 个头分 g 组，先投影低维再拼接 |
| ⑤ Sliding Window | 额外保留最近 128 个未压缩 KV |

**作用**：局部信息掌握更好；CSA 单组件局部计算量减少约 1000x

#### 2.2 HCA（Heavily Compressed Attention，重压缩注意力）

**128:1 压缩**（更极端）

| 维度 | 与 CSA 的区别 |
|------|-------------|
| 压缩比 | m' = 128（比 CSA 高 32 倍）|
| 稀疏选择 | **不使用**（压缩后序列足够短）→ 稠密注意力 |
| 共享 KV MQA | ✅ 同 CSA |
| 分组输出投影 | ✅ 同 CSA |
| Sliding Window | ✅ 同 CSA |

**作用**：捕捉远距离内容之间的联系；HCA 单组件局部计算量减少约 10 万倍

#### 2.3 SWA（Sliding Window Attention，128 token 滑窗）

- 只关注 128 token 滑窗内上下文
- 配合 BF16 精读计算
- 缓解 CSA/HCA 的精度损失

#### 2.4 混合配置策略

- **前 2 层**：纯 SWA（浅层主要负责局部特征提取）
- **后续层**：交替使用 CSA 和 HCA
- **部分 RoPE**：仅对隐藏维度的最后 64 维应用旋转位置编码
- **Attention Sink**：可学习 sink logit 防止 Softmax 分母趋近于零
- **混合精度 KV Cache**：BF16 + FP8 混合精度存储

### 三、实际效果（权威源数字）

| 模型 | 1M 上下文 FLOPs | 1M 上下文 KV Cache |
|------|----------------|-------------------|
| V3.2（MLA+DSA）| 100%（基准）| 100%（基准）|
| **V4-Flash** | **10%** | **7%** |
| **V4-Pro** | **27%** | **10%** |
| 传统 BF16 GQA8 | — | **约 200%**（即 V4 缩减到约 2%）|

### 四、诚实评估：信息丢失

> "说实话是丢失的" — 授课人原话

- 不仅是 DeepSeek，所有声称支持百万上下文的模型（GLM 5.2、Grok 5.5、Opus 4.8）**都有不同程度的丢失**
- DeepSeek 大致在中游水平
- **约 600K-700K 时出现比较明显的信息丢失**
- 验证方法："大海捞针"测试（needle-in-a-haystack）

## 关联

- 相关概念: [DeepSeek V4](/base-models/concept-deepseek-v4)、[DeepSeekMoE：混合专家架构](/architecture/concept-deepseek-moe)、[MLA：多头潜在注意力（Multi-head Latent Attention）](/architecture/concept-mla-multi-head-latent-attention)
- 配套资料: 

## 引用来源

- [1]  — 第 2 章百万级上下文原理与 DSA 方案
- [2] [DeepSeek-V4 技术报告深度解读（chang-wenbin.github.io）](https://chang-wenbin.github.io/AIbin-Note/MLA_DSA/2026-04-24_deepseek-v4-technical-analysis.html) — CSA / HCA / SWA 详细架构、压缩比、FLOPs/KV Cache 数据
- [3] [DeepSeek V4 技术报告一手解读（zhuanlan.zhihu.com）](https://zhuanlan.zhihu.com/p/2031082307185005393) — 混合注意力架构综述

## 变更记录

- 2026-07-06: 初始创建，来源 notes-50 第 2 章，融合 DeepSeek-V4 技术报告权威源
- 2026-07-06: ⚠️ 命名澄清——PPT 中"DSA"是错误命名，V4 官方为 CSA + HCA 混合注意力
