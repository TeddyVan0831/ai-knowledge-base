---
title: "华为 Atlas SuperPoD 超节点"
outline: deep
---

# 华为 Atlas SuperPoD 超节点

> **类型**: concept
> **创建时间**: 2026-07-06
> **最后更新**: 2026-07-06
> **来源**: 
> **领域**: ai

## 摘要

华为 Atlas SuperPoD / SuperCluster 是面对 NVIDIA NVL72/NVLink 集群的"国产生态算力底座"——通过 **UB-Mesh 递归直连** + **跨柜全光互联**，把数千到数十万张昇腾卡组成单一逻辑计算单元。Atlas 950 SuperPoD 最大 8,192 卡 / 15 EFLOPS FP8，Atlas 950 SuperCluster 最大 52 万卡 / 524 EFLOPS——是国家级 AI 基础设施的终极算力。

> 课程核心观点："**虽然单卡能力会弱一些，但是我还是想到一个办法，这个办法很简单粗暴，就是做对卡就是了**" — 授课人原话

## 详情

### 一、Atlas 全产品线（六大系列）

> 🖼️ [图 10] **华为 Atlas 产品线** — 六大系列（200/300/500/800/900）的定位、代表产品、搭载芯片、关键规格 — 

> **概念澄清**："昇腾"是芯片（Ascend NPU），"Atlas"是产品线（板卡、服务器、集群）

| 系列 | 定位 | 代表产品 | 搭载芯片 |
|------|------|---------|---------|
| **Atlas 200** | 终端/边缘推理 | Atlas 200 DK 开发者套件 | 昇腾 310 |
| **Atlas 300** | 数据中心加速卡 | Atlas 300T 训练 / Atlas 350 加速 | 昇腾 910 / 950PR |
| **Atlas 500** | 边缘计算 | Atlas 500 Pro 智能边缘服务器 | 支持 Atlas 300 系列 |
| **Atlas 800** | 中心侧 AI 服务器 | Atlas 800 训练 / Atlas 800T A3 超节点 | 昇腾 910 × 8 |
| **Atlas 900** | 超大规模集群 | Atlas 950 SuperPoD / SuperCluster | 昇腾 950DT |

### 二、SuperPoD vs SuperCluster 对比

> 🖼️ [图 11] **昇腾超节点形态对比** — Atlas 950 SuperPoD / Atlas 960 SuperPoD / Atlas 950 SuperCluster 三大形态的 NPU 规模、总算力、互联带宽、协议 — 

| 形态 | NPU 规模 | 总算力 FP8 | 互联带宽 | 协议 |
|------|---------|-----------|---------|------|
| **Atlas 950 SuperPoD** | 最大 8,192 卡 | 15 EFLOPS | 16.3 PB/s | UB-Mesh 递归直连 |
| **Atlas 960 SuperPoD** | 最大 15,488 卡 | 30 EFLOPS | 34 PB/s | 跨柜全光互联 |
| **Atlas 950 SuperCluster** | 超 **520,000 卡** | **524 EFLOPS** | — | UB0e / RoCE |

### 三、关键设计理念

> "**做对卡就是解决方案**" — 单卡算力弱，就靠数量堆出集群级优势

**采购人群**：
- 大模型厂商
- 超大型国际央企
- 银行、证券总部

**生产逻辑**：
- 先有需求、先有人定才去做
- 50 万张卡 + 50 万根网线 → 制作成本极高
- 2025-09-18 华为全联接大会发布，2026-07 实际出货

### 四、与 NVIDIA NVL72 对标

| 维度 | Atlas 950 SuperPoD | NVIDIA NVL72 |
|------|-------------------|--------------|
| GPU/NPU 数 | 8,192 | 72 |
| 总算力 | 15 EFLOPS FP8 | ~1 EFLOPS FP8 |
| 单卡算力 | 弱（~2 PFLOPS）| 强（Blackwell B200 ~9 PFLOPS）|
| 集群规模 | 大 100x | 小 |
| 互联 | UB-Mesh 16.3 PB/s | NVLink 130 TB/s（单柜）|

> 华为走的是"以量取胜"路线——单卡算力弱，但能组成比 NVL72 大 100x 的集群

## 关联

- 相关概念: [华为昇腾 AI 生态](/base-models/concept-ascend-ecosystem)、[NVIDIA 五大壁垒与 AI 芯片竞争格局](/tools-ecosystem/concept-nvidia-five-barriers)
- 配套资料: 

## 引用来源

- [1]  — 第 4 章 Atlas 产品线
- [2] [Atlas 950 SuperPoD 百度百科](https://baike.baidu.com/item/Atlas%20950%20SuperPoD/66774777) — 2025-09-18 发布
- [3] [华为发布全球最强算力超节点和集群（央广网）](https://tech.cnr.cn/techgd/20250918/t20250918_527366958.shtml) — 8192/15488 卡规模
- [4] [Atlas 950/960 SuperPoD 强超节点集群（电子工程专辑）](https://www.eet-china.com/mp/a440308.html) — 8,192 张 Ascend 950DT

## 变更记录

- 2026-07-06: 初始创建，来源 notes-50 第 4 章
