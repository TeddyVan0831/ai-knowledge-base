---
title: "华为昇腾 AI 生态"
outline: deep
---

# 华为昇腾 AI 生态

> **类型**: concept
> **创建时间**: 2026-07-06
> **最后更新**: 2026-07-06
> **来源**: 
> **领域**: ai

## 摘要

华为昇腾是中国最完整的 AI 芯片生态——从 **鲲鹏 CPU**（ARM 自研，2026Q4 推出灵犀核 950）到 **昇腾 NPU**（910/910B/910C/950PR/950DT/960/970 全产品线），从 **CANN 软件栈**（对标 NVIDIA CUDA）到 **MindIE LLM**（闭源官方推理引擎）和 **vLLM-Ascend**（开源社区版推理引擎）。整个生态分层对齐 NVIDIA（CUDA / TensorRT / cuDNN / NCCL），是当前国内唯一能开始追赶 CUDA 的厂商。

## 详情

### 一、五层全栈架构

> 🖼️ [图 3] **昇腾 AI 系统全栈** — 五层架构：硬件（NPU）→ 编译（CANN）→ 训练框架（MindSpore）→ 推理引擎（MindIE LLM / vLLM-Ascend）→ 开发体系 → 算法应用 — 

| 层级 | 华为 | NVIDIA 对照 |
|------|------|------------|
| **AI 硬件** | Ascend NPU | TPU / GPU / IPU / NPU / CPU |
| **AI 编译 & 计算架构** | **CANN** | CUDA / TVM / XLA / LLVM / GCC |
| **AI 训练 & 推理框架** | MindSpore | PyTorch / JAX / TensorFlow |
| **AI 推理引擎** | **MindIE LLM**（闭源）/ **vLLM-Ascend**（开源）| TensorRT / vLLM |
| **开发体系** | Python + 主流语言集成 | Python |
| **算法应用** | CV / NLP / Audio | CV / NLP / Audio |

> "NV 的 CUDA 比 GPU 还要重要……它的核心的护城河" — 课程观点

### 二、鲲鹏 CPU 系列

> 🖼️ [图 4] **华为硬件 - CPU 鲲鹏** — 鲲鹏 920 vs 950 对比：架构（ARM v8.2 vs 自研灵犀核）、核数（64 vs 256）、线程（64 vs 384）、内存（DDR4/PCIe 4.0 vs DDR5/PCIe 5.0）— 

| 维度 | 鲲鹏 920 | 鲲鹏 950（2026Q4）|
|------|----------|------------------|
| 架构 | ARM v8.2 | **自研"灵犀核" ARM** |
| 制程 | 7nm | 7nm（成熟先进工艺）|
| 最大核数 | 64 核 | **256 核** |
| 最大线程 | 64 | **384 线程**（双线程）|
| 频率 | 2.6GHz | — |
| 内存 | DDR4 / PCIe 4.0 | **DDR5 + PCIe 5.0** |
| 单核性能 | 基准 | **+50%** |

### 三、昇腾 NPU 推理显卡核心特点

> 🖼️ [图 5] **昇腾推理显卡架构** — 三大核心：高能效计算核心 + 高带宽存储系统（HBM）+ 高效片上互联 — 

**vs 普通 GPU 的关键差异**：
- **不显示输出**（纯推理）
- **HBM 显存**（High Bandwidth Memory）集成到芯片上（vs 焊主板）
- **片上自带网络功能**（RoCE 协议），可绕过服务器直接组网

**HBM 国产化**（关键进展）：
- 长鑫长兴（长鑫存储）已能生产
- 华为新显卡（950 系列）已搭载国产 HBM

### 四、昇腾 AI 芯片演进路线图

> 🖼️ [图 6] **昇腾芯片演进 - 上一代** — 910 / 910B / 910C 三代对比：FP16/INT8 算力、HBM 容量、带宽 — 
>
> 🖼️ [图 7] **昇腾芯片演进 - 今年** — 950PR vs 950DT：发布时间、FP8/FP4 算力、HBM 容量、互联带宽、目标场景（Prefill vs Decode）— 
>
> 🖼️ [图 9] **昇腾芯片规划** — 960 (2027Q4) / 970 (2028Q4)：FP8/FP4 算力、内存带宽、互联 — 

| 型号 | 发布时间 | 制程 | 单卡算力（FP8）| HBM |
|------|---------|------|--------------|-----|
| 昇腾 910 初代 | 2019 | 7nm | — | 32GB HBM2 |
| 昇腾 910B | 2023 | 7nm N+2 | — | 32GB HBM2 |
| 昇腾 910C | 2025 Q1 | 7nm 双芯封装 | — | 128GB HBM2e / 3.2 TB/s |
| **昇腾 950PR** | **2026 Q1** | 7nm | 1 PFLOPS / FP4 2 PFLOPS | 1.6 TB / 128GB |
| **昇腾 950DT** | **2026 Q4** | 7nm | 1 PFLOPS / FP4 2 PFLOPS | **4 TB / 144GB** |
| 昇腾 960 | 2027 Q4 | — | ~2 PFLOPS | 288GB HBM / ~8 TB/s |
| 昇腾 970 | 2028 Q4 | — | ~4 PFLOPS | ~14.4 TB/s |

> **950PR vs 950DT 设计哲学**：
> - **Prefill 阶段**（处理输入）可并行 → 更看重算力，对显存带宽要求低 → 950PR
> - **Decode 阶段**（逐字生成）不可并行 → 更看重显存带宽，对算力要求低 → 950DT

> 🖼️ [图 8] **主流 AI 芯片对比** — 昇腾 950DT vs NVIDIA H200 vs NVIDIA B300：制程、FP8/FP16 算力、带宽、显存、定位 — 

### 五、推理框架对比

> 🖼️ [图 13] **推理框架对比** — MindIE LLM vs vLLM-Ascend：协议、模型支持、4 卡加速比、P99 延迟、部署周期 — 

| 维度 | MindIE LLM（昇腾官方）| vLLM-Ascend（社区开源）|
|------|---------------------|---------------------|
| 协议 | **非开源**（需官方授权）| **Apache 2.0 开源** |
| 模型支持 | 约 45+ 主流模型 | **120+ 主流开源模型** |
| 4 卡加速比 | 3.7× | 3.2× |
| P99 延迟 | -12% | 略高 |
| 部署周期 | 3-5 工作日 | 容器化、步骤减少 40% |
| 适用场景 | 大规模生产集群、极致稳定性 | 中小规模、快速验证、异构部署 |

**选型决策**：
- 公司业务稳定 + 极致成本优化 → MindIE LLM
- 一般同学 / 多模型适配 → vLLM-Ascend

### 六、工具链：npu-smi

> 🖼️ [图 14] **npu-smi 介绍** — 五大用法：info / list / watch / version / board，命令示例及输出解读 — 

- 对标 NVIDIA 的 `nvidia-smi`
- 五大用法：info / list / watch / version / board
- **注意**：Memory Usage 都是 0，但 **HBM Usage 有数据**——证明这是带 HBM 的推理卡

## 关联

- 相关概念: [华为 Atlas SuperPoD 超节点](/base-models/concept-atlas-superpod)、[国产算力部署实践（昇腾 910B + vLLM-Ascend）](/inference-deploy/concept-ascend-deployment)、[CUDA：并行计算平台](/tools-ecosystem/concept-cuda-parallel-computing)、[NVIDIA 五大壁垒与 AI 芯片竞争格局](/tools-ecosystem/concept-nvidia-five-barriers)
- 相关实体: [华为（Huawei）](/base-models/company-huawei)（待创建）
- 配套资料: 

## 引用来源

- [1]  — 第 3-4 章华为昇腾 AI 生态
- [2] [百度百科 昇腾 950 芯片](https://baike.baidu.com/item/%E6%98%87%E8%85%BE950%E8%8A%AF%E7%89%87/66775346) — 950PR 2026Q1、950DT 2026Q4
- [3] [华为全联接大会 2025-09-18 公布](https://www.sh.chinanews.com.cn/kjjy/2025-09-19/140127.shtml) — 950/960/970 时间表

## 变更记录

- 2026-07-06: 初始创建，来源 notes-50 第 3-4 章
