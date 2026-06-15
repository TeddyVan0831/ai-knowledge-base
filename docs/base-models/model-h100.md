---
title: "NVIDIA H100 GPU"
outline: deep
---

# NVIDIA H100 GPU

> **类型**: entity
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 

## 摘要
NVIDIA H100 是基于 Hopper 架构的企业级 AI GPU，拥有 16,896 个 CUDA 核心和 80GB HBM3 显存（带宽 3.35TB/s），是 2026 年 7B-70B 模型训练与推理的中流砥柱，云厂商主力机型。

## 详情

### 核心规格
- **架构**: Hopper 
- **CUDA 核心数**: 16,896 个（SXM/NVL 版本）；PCIe 版本为 14,592 个 
- **显存/带宽**: 80GB HBM3 / 3.35TB/s 
- **定位**: 中流砥柱 

### 适用场景
- 7B-70B 训练/推理 
- 7B-30B 全参训练推荐配置：H100（FP8 + 梯度检查点），生态最成熟 
- 交付稳定，云厂商主力 

### 架构代际
Ada Lovelace (2022) → Hopper (2022) → Blackwell (2025) 

### 与其他 GPU 的关系
- H 系列是通用计算芯片，在气象模拟、分子动力学等科学计算上仍更优 
- GB200 超级芯片在特定推理场景下，能效比 H100 最高提升约 25 倍（取决于工作负载和量化精度） 
- B200 单卡推理性能约相当于 5 个 H100 节点 

## 关联
- 相关实体: [NVIDIA B200 GPU](/base-models/model-b200)、[NVIDIA RTX 4090](/base-models/model-rtx4090)
- 相关概念: [企业级 AI 部署：硬件选型与框架选择](/inference-deploy/concept-enterprise-ai-deployment)
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)

## 引用来源
- [1]  — 企业级 AI 硬件选型与规划，GPU 型号对比、架构代际、Blackwell 革命性变化

## 变更记录
- 2026-05-26: 初始创建，来源 
