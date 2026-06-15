---
title: "模型优化"
outline: deep
---

# 模型优化

> **类型**: topic
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 、、、、、

## 摘要

模型优化是使大语言模型适应下游任务、压缩部署的全景方法论，涵盖五大技术路线：高效微调（LoRA/QLoRA）、量化压缩（PTQ/旋转量化/极低比特）、剪枝稀疏化（结构化/非结构化/2:4 半结构化）、知识蒸馏（答案/特征/自蒸馏）、注意力机制优化（Flash Attention/MQA/GQA/稀疏/线性）。这些技术可叠加使用，实现极致的模型压缩与推理加速。

## 详情

### 技术路线全景

```
模型优化五大技术路线：

┌─────────────────────────────────────────────────────────────┐
│                    模型优化全景                                │
├─────────────────┬─────────────────┬─────────────────────────┤
│  🔧 高效微调     │  📦 量化压缩     │  ✂️ 剪枝稀疏化           │
│  LoRA/QLoRA    │  PTQ (INT4/INT8) │  结构化/2:4/N:M         │
│  只训 1-10% 参数 │  16GB → 4GB     │  16GB → 8GB (50%稀疏)   │
│  [LLM 微调原理](/training-optimization/concept-llm-fine-tuning) │ [后训练量化（PTQ）](/training-optimization/concept-quantization-ptq) │ [模型剪枝与稀疏化](/training-optimization/concept-model-pruning) │
├─────────────────┼─────────────────┼─────────────────────────┤
│  🎓 知识蒸馏     │  ⚡ 注意力优化    │  🔬 极低比特量化         │
│  大模型教小模型   │  Flash/MQA/GQA  │  INT2/三值/二值/BitNet  │
│  传递"暗知识"    │  减少 HBM/O(N²)  │  需 QAT + 知识蒸馏       │
│  [知识蒸馏](/training-optimization/concept-knowledge-distillation) │ [注意力机制优化](/architecture/concept-attention-optimization) │ [旋转量化与极低比特量化](/training-optimization/concept-quantization-rotation) │
└─────────────────┴─────────────────┴─────────────────────────┘
```

### 组合压缩效果

**量化 + 剪枝** ：
- 纯 INT4 量化：16GB → 4GB（4x 压缩）
- 纯 2:4 稀疏（FP16）：16GB → ~8.75GB（~1.8x 压缩）
- **INT4 + 2:4 组合**：16GB → ~2.75GB（~5.8x 压缩）

**蒸馏 + 量化** 协同优化 ：
```
蒸馏：让小模型更聪明
量化：让模型更省内存
两者叠加：小模型 + 更聪明 + 更省内存 = 极致压缩
```

**完整部署链路**：
```
大模型（教师）
  → 蒸馏 → 小模型（学生）
    → 剪枝 → 更小的模型
      → 量化（INT4 PTQ） → 端侧部署
        → 注意力优化（Flash + GQA） → 推理加速
```

### 量化精度全景

| 精度 | 7B 模型大小 | 压缩比 | PPL 增加 | 是否需要训练 | 成熟度 |
|------|------------|--------|---------|------------|--------|
| FP16 | 14 GB | 1x | 0% | 否 | ✅ 基准  |
| INT8 | 7 GB | 2x | +1-3% | 否（PTQ） | ✅ 成熟  |
| INT4 | 3.5 GB | 4x | +3-5% | 否（PTQ） | ✅ 主流  |
| **INT4+QuaRot** | 3.5 GB | 4x | **+0.63**（最优） | 否（PTQ） | ✅ 可用  |
| **INT2** | 1.75 GB | 8x | +15-30% | **是（QAT）** | 🔬 研究  |
| **三值** | ~2 GB | ~8x | +15-25% | **是（从头）** | 🔬 研究  |
| **BitNet b1.58** | ~2 GB | ~7x | **<5%**（大模型） | **是（原生）** | 🔬 突破  |

### 注意力优化对比

| 方案 | 核心思路 | 计算精度 | 加速比 | KV Cache |
|------|---------|---------|--------|---------|
| Flash Attention | 分块 + 增量 softmax | **精确** | 1.5-3× | 不变  |
| MQA | 所有头共享 KV | **精确** | 1.5-4× | **1/H**  |
| GQA | 分组共享 KV | **精确** | 1.5-2× | **G/H**  |
| 稀疏注意力 | 只算重要连接 | 近似 | 2-5× | 不变  |
| 线性注意力 | 改变计算顺序 | 近似 | 3-10× | **O(1)**  |

### 硬件效率

**能效对比**（Horowitz 2014, 45nm 工艺） ：
| 操作 | 能耗 | 相对 FP32 |
|------|------|----------|
| FP32 MAC | 4.6 pJ | 1x |
| INT8 MAC | ~0.2 pJ | ~20x 能效 |
| DRAM 访问 | 2.6 nJ | 比计算贵 ~565x |

**二值网络硬件加速** ：
| 精度 | SIMD 并行（AVX-512） | 相对 FP32 能效 |
|------|---------------------|---------------|
| INT4 | 128 路 | ~8x |
| 三值 | 部分支持 | ~16x |
| 二值（XNOR+popcount） | 512 路 | ~32x |

## 关联
- 相关概念: [LLM 微调原理](/training-optimization/concept-llm-fine-tuning)、[后训练量化（PTQ）](/training-optimization/concept-quantization-ptq)、[旋转量化与极低比特量化](/training-optimization/concept-quantization-rotation)、[模型剪枝与稀疏化](/training-optimization/concept-model-pruning)、[知识蒸馏](/training-optimization/concept-knowledge-distillation)、[注意力机制优化](/architecture/concept-attention-optimization)
- 相关实体: [NVIDIA H100 GPU](/base-models/model-h100) — NVIDIA H100 GPU（量化与剪枝的硬件基准）
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops) — AI 部署与运维主题综述

## 引用来源
- [1]  — 高效微调方法、LoRA 数学原理
- [2]  — PTQ、GPTQ、AWQ、SmoothQuant、GGUF
- [3]  — QuaRot、INT2/三值/二值、BitNet b1.58
- [4]  — 结构化/非结构化/2:4 稀疏、模型合并、稀疏存储
- [5]  — 答案蒸馏、特征蒸馏、自蒸馏、蒸馏+量化协同
- [6]  — Flash Attention、MQA/GQA、稀疏注意力、线性注意力

## 变更记录
- 2026-05-26: 初始创建，综合 6 篇原始笔记