---
title: "NVIDIA Jetson Orin 与 Thor 全系对照（跨代归一化）"
outline: deep
---

# NVIDIA Jetson Orin 与 Thor 全系对照（跨代归一化）

> **类型**: concept
> **创建时间**: 2026-07-19
> **最后更新**: 2026-07-19
> **来源**: 
> **领域**: ai

## 摘要
NVIDIA Jetson 边缘 AI 平台的两个时代：Orin 时代（**Ampere 架构**，8nm 三星，INT8 TOPS 口径）与 Thor 时代（**Blackwell 架构**，4nm 台积电，FP4 TFLOPS 口径）。两代旗舰 AGX Orin 64GB（275 TOPS）与 AGX Thor/T5000（2070 TFLOPS FP4-sparse）因"单位/精度/稀疏"三维全不同**不可直接除法比较**，须按 [算力口径方法论](/base-models/concept-ai-compute-caliber) 归一化。Thor 全系（T5000/T4000/T3000/T2000）2026-07-15 新发布主流模组，预计 2027 Q1 供货。

## 详情

### 两个时代的旗舰平台总览
| 维度 | Orin 时代（Ampere） | Thor 时代（Blackwell） |
|------|---------------------|------------------------|
| 首发模组 | Jetson AGX Orin（2022） | Jetson AGX Thor（2025） |
| GPU 架构 | NVIDIA Ampere | NVIDIA Blackwell（第 5 代 Tensor Core） |
| 算力标注口径 | TOPS（INT8 为主） | TFLOPS（FP4，稀疏） |
| 旗舰模组峰值 | 275 TOPS（AGX Orin 64GB） | 2070 TFLOPS FP4-sparse（AGX Thor / T5000） |
| 制程 | 8nm Samsung | 4nm TSMC |
| 内存技术 | LPDDR5 | LPDDR5X |
| 定位 | 当前主流机器人/自动驾驶边缘 | 物理 AI、机器人、生成式 AI 边缘旗舰 |

### Orin 全系（Ampere，INT8 TOPS 稠密/稀疏）
- **AGX Orin 64GB**：275 TOPS · 2048-core Ampere/64 Tensor · 12×Cortex-A78AE · 64GB LPDDR5/204.8 GB/s · 15–60W
- **AGX Orin 32GB**：248 TOPS · 同 GPU · 32GB LPDDR5 · 15–60W
- **AGX Orin 工业版**：241 TOPS · 64GB LPDDR5 **(+ECC)** · 15–60W（全系唯一带 ECC 款）
- **Orin NX 16GB**：100 TOPS(稠密)/157 TOPS(稀疏) · 8×A78AE · 16GB/102.4 GB/s · 10–40W
- **Orin NX 8GB**：70/117 TOPS · 8×A78AE · 8GB/102.4 GB/s · 10–40W
- **Orin Nano 8GB**：40 TOPS(稠密)/67 TOPS(SUPER) · 6×A78AE · 8GB/68 GB/s · 7–25W
- **Orin Nano 4GB**：34 TOPS · 6×A78AE · 4GB/51 GB/s · 7–15W
- **ECC**：全系仅 AGX Orin 工业版带 Inline ECC（NVIDIA 官方论坛确认，NX/Nano 硬件不支持）。

### Thor 全系（Blackwell，FP4 TFLOPS）
> T5000/T4000 官方明确为 **FP4-sparse**；T3000/T2000 发布稿仅写 "FP4 TFLOPS"，稀疏/稠密待 datasheet 确认。

- **AGX Thor / T5000**（首发 2025）：2070 TFLOPS(FP4-sparse) · 2560-core Blackwell/96×第5代 Tensor Core · 14×Neoverse-V3AE · 128GB LPDDR5X **(+ECC, Alt-link)** /273 GB/s · 40–130W
- **Thor T4000**（首发 2025）：1200 TFLOPS(FP4-sparse) · 1536-core/64×Tensor · 12×Neoverse-V3AE · 64GB LPDDR5X/273 GB/s · 40–130W
- **Jetson T3000**（2026-07-15 新发，预计 2027 Q1 供货）：865 TFLOPS(FP4) · 8×Neoverse · 32GB LPDDR5X/273 GB/s · 尺寸/功耗约 T5000 一半，**多模态推理性能与 T5000 相当**（软件内存优化）· 支持 25 GbE · IGX T3000 含功能安全（Halos for Robotics）
- **Jetson T2000**（2026-07-15 新发，预计 2027 Q1 供货）：400 TFLOPS(FP4) · 16GB · 入门级 Thor，面向视觉 AI 智能体/AMR/工业机械臂

### 跨代归一化对照（重点：口径不可直接比）
| 对比项 | AGX Orin 64GB | AGX Thor (T5000) |
|--------|---------------|------------------|
| 官方标注算力 | 275 TOPS (INT8, 稠密) | 2070 TFLOPS (FP4, 稀疏) |
| GPU 架构 | Ampere | Blackwell |
| 内存 | 64GB LPDDR5/204.8 GB/s | 128GB LPDDR5X/273 GB/s |
| 功耗区间 | 15–60W | 40–130W |
| 制程 | 8nm | 4nm |
| NVIDIA 官方宣称 | — | 比 AGX Orin **AI 算力高 7.5 倍以上，能效高 3.5 倍** |

粗略量级换算（仅建立直觉，非精确等价）：Orin 275 INT8 稠密 → FP4-sparse 口径 ≈ 1100 TFLOPS，仍低于 Thor 2070（含架构代际提升）；Thor 2070 FP4-sparse ÷ 4 ≈ 500 TOPS(INT8 稠密) 当量，仍高于 Orin 275。**结论**：Thor 真实优势 = 架构升级 + 精度红利 + 稀疏红利 + 内存带宽提升，叠加而成。

### 选型速查
| 需求档位 | 推荐模组 |
|----------|----------|
| 旗舰机器人/边缘大模型 | AGX Thor (T5000)：2070 FP4、128GB、Blackwell 原生 FP4 |
| 高性能主流（半功耗≈T5000 性能） | T3000 / IGX T3000：865 FP4、32GB、273GB/s |
| 入门级边缘 AI/视觉智能体/机械臂 | T2000：400 FP4、16GB |
| 高带宽工业/轨交（已量产） | AGX Orin 64GB / 工业版 |
| 中端紧凑（已量产） | Orin NX 16GB |
| 入门/教育/轻量（已量产） | Orin Nano 8GB / 4GB |

> T3000/T2000 为 2026-07-15 新发布，预计 2027 Q1 供货；当前量产主力仍为 AGX Thor (T5000) 与 Orin 全系。

## 关联
- 相关概念: [算力口径方法论：单位 × 精度 × 计算模式](/base-models/concept-ai-compute-caliber)（跨代归一化方法论）、[ARM 处理器 IP 全谱系与车规 CPU 对比（A78AE vs V3AE）](/base-models/concept-arm-cpu-ip-lineage)（Orin=A78AE / Thor=V3AE CPU）、[LPDDR5/5X 内存带宽、容量与 ECC 全解](/base-models/concept-lpddr-ecc)（Orin LPDDR5 / Thor LPDDR5X + ECC）、[半导体制程节点：三星 8nm vs 台积电 4nm 与「等效 Xnm」对照](/tools-ecosystem/concept-semiconductor-process-node)（Orin 8nm 三星 / Thor 4nm 台积电）
- 相关实体: [NVIDIA B200 GPU](/base-models/model-b200)（Blackwell 数据中心旗舰）、[NVIDIA H100 GPU](/base-models/model-h100)
- 参见: [topic-ai-soc-comparison-table-2026q2](/base-models/topic-ai-soc-comparison-table-2026q2)、[concept-ai-soc-competitive-landscape](/base-models/concept-ai-soc-competitive-landscape)、[concept-edge-ai-architecture-evolution](/base-models/concept-edge-ai-architecture-evolution)、[concept-ondevice-llm-deployment](/base-models/concept-ondevice-llm-deployment)、[LLM 边缘推理综述](/inference-deploy/concept-llm-edge-inference)

## 引用来源
- [1]  — Orin/Thor 全系规格、跨代归一化、选型速查
- [2]  — Orin/Thor 口径差异实战演示
- [3]  — ECC 纠偏（Orin 仅工业版带 ECC，Thor T5000 支持 Alt-link ECC）

## 变更记录
- 2026-07-19: 初始创建，来源 

> ⚠️ 矛盾标注：Thor 算力口径（与既有 wiki 全景表）
> - **争议来源**：[topic-ai-soc-comparison-table-2026q2](/base-models/topic-ai-soc-comparison-table-2026q2) 记 Thor AGX 为 **~1035 (FP8)**（L26）；本页与 [concept-ai-soc-competitive-landscape](/base-models/concept-ai-soc-competitive-landscape)（L68 主表）记 **2070 TFLOPS (FP4-sparse)**；而 competitive-landscape 能效表（L197）又写 **~1035(FP8)**，页内自相矛盾。
> - **观点A（全景表 2026 Q2）**：Thor ≈ 1035 (FP8)。
> - **观点B（官方/NVIDIA 博客/notes-52）**：Thor T5000 = 2070 TFLOPS (FP4-sparse)。
> - **AI 判断**：**实质一致，属口径不同，非真矛盾**。按 [算力口径方法论](/base-models/concept-ai-compute-caliber)：FP8 → FP4 吞吐约 ×2，1035(FP8) × 2 ≈ 2070(FP4)；若再叠加 2:4 稀疏则差距更大。两者是同一芯片在不同精度口径下的标注。建议全库统一采用官方 **FP4-sparse** 口径并在表头显式标注，旧 "1035(FP8)" 保留为备注。
> - **裁决依据**：notes-52 数据来源为 NVIDIA 官方 Jetson 规格比较页 + 官方博客（2026-07-15），且 competitive-landscape 主表已采用 2070 FP4，故以官方 FP4-sparse 为准。
