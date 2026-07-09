---
title: "华为（Huawei）"
outline: deep
---

# 华为（Huawei）

> **类型**: entity
> **创建时间**: 2026-07-09
> **最后更新**: 2026-07-09
> **来源**: 
> **领域**: ai

## 摘要

华为（Huawei）是中国最完整的 AI 全栈厂商——从 **鲲鹏（Kunpeng）CPU**（ARM 自研，2026Q4 推出灵犀核 950）到 **昇腾（Ascend）NPU**（910/910B/910C/950PR/950DT/960/970 全产品线），从 **CANN** 软件栈（对标 NVIDIA CUDA）到 **MindIE LLM**（闭源官方推理引擎）和 **vLLM-Ascend**（开源社区版推理引擎）。整个生态分层对齐 NVIDIA（CUDA / TensorRT / cuDNN / NCCL），是当前国内唯一能开始追赶 CUDA 的厂商；其 **Atlas SuperPoD / SuperCluster** 更构成面向国家级 AI 基础设施的算力底座。

## 详情

### 一、五层全栈架构

| 层 | 代表产品 | 对标 NVIDIA |
|----|---------|------------|
| CPU | 鲲鹏 920 / 灵犀核 950（2026Q4） | CPU 侧 |
| NPU | 昇腾 910 / 910B / 910C / 950PR / 950DT / 960 / 970 | GPU（H100/B200 等）|
| 软件栈 | CANN（对标 CUDA）| CUDA |
| 推理引擎 | MindIE LLM（闭源官方）、vLLM-Ascend（开源社区）| TensorRT / vLLM |
| 集群 | Atlas SuperPoD / SuperCluster（UB-Mesh + 全光互联）| NVL72 / NVLink 集群 |

### 二、算力底座：Atlas SuperPoD / SuperCluster

- **Atlas 950 SuperPoD**：最大 8,192 卡 / 15 EFLOPS FP8
- **Atlas 950 SuperCluster**：最大 52 万卡 / 524 EFLOPS
- 通过 **UB-Mesh 递归直连** + **跨柜全光互联**，把数千到数十万张昇腾卡组成单一逻辑计算单元，是"国产生态算力底座"的核心形态。详见 [华为 Atlas SuperPoD 超节点](/base-models/concept-atlas-superpod)。

### 三、部署范式（国产算力实践）

在 8 卡昇腾 910B + 鲲鹏 920 服务器上，通过 **vLLM-Ascend Docker** 部署 DeepSeek V4-Flash W8A8 MTP 量化版，全部容器化封装、不在 host 主系统做配置——这是国产算力部署的"标准范式"。详见 [国产算力部署实践](/inference-deploy/concept-ascend-deployment) 与 [华为昇腾 AI 生态](/base-models/concept-ascend-ecosystem)。

### 四、配套工具链

- **npu-smi**：对标 `nvidia-smi`（注意 Memory Usage 多为 0，但 **HBM Usage 有数据**，证明是带 HBM 的推理卡）
- 五大用法：info / list / watch / version / board

## 关联

- 相关概念: [华为昇腾 AI 生态](/base-models/concept-ascend-ecosystem)、[国产算力部署实践（昇腾 910B + vLLM-Ascend）](/inference-deploy/concept-ascend-deployment)、[华为 Atlas SuperPoD 超节点](/base-models/concept-atlas-superpod)、[CUDA：并行计算平台](/tools-ecosystem/concept-cuda-parallel-computing)、[NVIDIA 五大壁垒与 AI 芯片竞争格局](/tools-ecosystem/concept-nvidia-five-barriers)
- 相关产品: [product-ascend-310-series](/base-models/product-ascend-310-series)（昇腾 310 系列端侧 SoC）
- 配套资料: 

## 引用来源

- [1]  — 第 3-4 章华为昇腾 AI 生态
- [2] [百度百科 昇腾 950 芯片](https://baike.baidu.com/item/%E6%98%87%E8%85%BE950%E8%8A%AF%E7%89%87/66775346) — 950PR 2026Q1、950DT 2026Q4
- [3] [华为全联接大会 2025-09-18 公布](https://www.sh.chinanews.com.cn/kjjy/2025-09-19/140127.shtml) — 950/960/970 时间表

## 变更记录

- 2026-07-09: 初始创建（Lint P1 修复：原被 [华为昇腾 AI 生态](/base-models/concept-ascend-ecosystem) 引用标注"待创建"，由 notes-50 第 3-4 章综合编译）
