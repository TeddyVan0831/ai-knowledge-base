---
title: "DeepSeek V4"
outline: deep
---

# DeepSeek V4

> **类型**: concept
> **创建时间**: 2026-07-06
> **最后更新**: 2026-07-06
> **来源**: 
> **领域**: ai

## 摘要

DeepSeek V4 是深度求索（DeepSeek）于 **2026-04-24** 发布的第四代开源 MoE 大语言模型系列，包含 Pro（1.6T 总参 / 49B 激活）和 Flash（284B 总参 / 13B 激活）两个版本，均原生支持 **100 万 token** 上下文。V4 的核心突破是用 **CSA + HCA 混合注意力**（替代 V3.2 的 MLA + DSA）在 1M 上下文下将 FLOPs 降至 V3.2 的 10%-27%、KV Cache 降至 7%-10%。**完全开源 + 国产芯片推理适配** 是其最大差异化优势。

## 详情

### 一、两个版本对比

| 维度 | V4-Pro（旗舰性能版）| V4-Flash（高效经济版）|
|------|-------------------|---------------------|
| 总参数量 | 1.6T | 284B |
| 激活参数量 | 49B | 13B |
| 核心能力 | 复杂推理、竞赛编程、困难 Agent 任务顶尖 | 推理能力接近 Pro，简单 Agent 任务持平 |
| 输入定价 | 0.025 元（缓存）/ 3 元 / 百万 tokens | 0.02 元（缓存）/ 1 元 / 百万 tokens |
| 输出定价 | 6 元 / 百万 tokens | 2 元 / 百万 tokens |
| 上下文窗口 | 100 万 tokens | 100 万 tokens |
| 开源 | ✅ MIT | ✅ MIT |

> 🖼️ [图 1] **DeepSeek V4 简介** — 左右两栏对照 V4-Pro（1.6T/49B，左）与 V4-Flash（284B/13B，右），含输入输出定价对比 — 

### 二、V4 的核心目标

1. **以极低成本的 100% 百万级上下文**
2. **降低生成 token 的成本**（cache 命中价更具破坏性）

> "V4 真正优化的点不是性能最优，而是资源的使用。" — 课程观点

### 三、性能定位

- **发布时（2026-04-24）**：与第一梯队模型（Opus 4.6、GPT 5.5、Gemini 3.1）不分伯仲
- **两个月后（2026-06）**：第二梯队守门员——已被 Fabric 5、GLM 5.2、Grok 5.5、Opus 4.7/4.8 超越
- **能力定位**：日常代码任务满足 GitHub Copilot 级别，复杂长任务仍弱于闭源旗舰

### 四、关键架构创新

| 创新 | 说明 |
|------|------|
| **CSA + HCA 混合注意力** | 替代 V3.2 的 MLA + DSA，让 1M 上下文下 FLOPs 仅为 V3.2 的 10%-27% |
| **mHC（Manifold-Constrained HyperConnection）** | 流形约束超连接，将残差映射约束到双随机矩阵流形，保证 61 层深网训练稳定 |
| **Muon 优化器** | 替代 AdamW，配合混合 Newton-Schulz 迭代更快收敛 |
| **On-Policy Distillation（OPD）** | 领域专家独立训练 + 在线策略蒸馏，多教师→单学生 |

### 五、价格优势（核心杀手锏）

- 国外模型定价 = DeepSeek 的**约 10 倍**
- Claude Code 缓存命中率可达 95% → 实际成本断崖式下降
- 全球 API 使用量排行榜中 DeepSeek 使用量最大（课程观点）
- 纯推理部分运营成本可盈利 70% 毛利（"小道消息"，课程观点）

> "AI 能力马上要成为即水电煤气、网络之后的另一种基础设施。作为基础设施，它一定要便宜" — 课程观点

## 关联

- 相关概念: [CSA + HCA 混合注意力（百万级上下文解决方案）](/architecture/concept-csa-hca-attention)、[DeepSeekMoE：混合专家架构](/architecture/concept-deepseek-moe)、[推理模型与 DeepSeek R1：从 R1-Zero 到多阶段训练](/base-models/concept-reasoning-models-deepseek-r1)
- 相关实体: [DeepSeek（深度求索）](/base-models/company-deepseek)
- 配套资料: 
- 源转录原文: （PPT 图 1）

## 引用来源

- [1]  — DeepSeek V4 模型特性、定价、性能定位
- [2] DeepSeek-V4 技术报告（chang-wenbin.github.io / 2026-04-24 解读）— CSA + HCA 混合注意力、mHC、Muon 优化器、OPD 蒸馏
- [3] 百度百科 DeepSeek-V4：发布日 2026-04-24、参数 1.6T/49B、284B/13B
- [4] [digitalapplied.com DeepSeek V4 Preview](https://www.digitalapplied.com/blog/deepseek-v4-preview-launch-1m-context-efficiency) — 官方预览版细节
- [5] [ai-insight.org DeepSeek V4 报告](https://www.ai-insight.org/reports/deepseek-v4-2026) — 华为昇腾零日适配

## 变更记录

- 2026-07-06: 初始创建，来源 notes-50 第 1-2 章，融合 DeepSeek-V4 技术报告权威源
