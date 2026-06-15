---
title: "CUDA：并行计算平台"
outline: deep
---

# CUDA：并行计算平台

> **类型**: concept
> **创建时间**: 2026-06-10
> **最后更新**: 2026-06-10
> **来源**: 

## 摘要
CUDA（Compute Unified Device Architecture）是 NVIDIA 在 **2006 年**推出的并行计算平台和编程模型。最初仅支持 C/C++，使开发者能将科学计算任务方便地部署到 GPU 上。CUDA 的推出是 NVIDIA 的**关键转折**，历经 2006-2012 年"至暗时期"后，因 2012 年 AlexNet 在 NVIDIA GPU 上一飞冲天而证明其巨大价值。至今 GPU 计算流程从 2006 年至今未变 。

## 核心概念

### CUDA 是什么

- **全称**：Compute Unified Device Architecture（统一计算设备架构）
- **推出时间**：2006 年
- **支持语言**：最初仅支持 C/C++，后扩展到其他语言
- **核心价值**：让开发者能便捷地将科学计算（天气预测、分子模拟、核聚变等）搬到 GPU 

### CUDA 出现前后的对比

| 时期 | GPU 编程方式 | 局限 |
|------|------------|------|
| CUDA 之前 | OpenGL / Direct3D / DirectX | 仅限计算机图形学（游戏渲染），全球仅几百人有能力做科学计算 |
| CUDA 之后 | CUDA C/C++ API | 可便捷地将科学计算搬到 GPU  |

### GPU 计算完整流程（2006 年至今未变）

```
1. CPU 启动应用程序
2. CPU 将数据从硬盘 → 内存（A矩阵）
3. CPU 将数据从内存 → 显存（A1矩阵）
4. GPU 各计算核心从显存读取数据，执行并行计算
5. 计算结果写入显存（B1矩阵）
6. 通知 CPU "任务完成"
7. CPU 将结果从显存 → 内存（B矩阵）
``` 

> 这一流程从 2006 年至今未变。GPU 只负责"算数"，所有逻辑操作和调度由 CPU 完成。

### CUDA 的"至暗时期"与转折

- **2006 年前困境**：核心业务仅为游戏显卡（GPU），与 ATI 竞争，年利润长期徘徊在 4-5 亿美元
- **2006 年推出 CUDA**：黄仁勋顶着股东否决的压力，坚持投入并行计算方向
- **2006-2012 年至暗时期**：用户甚至投诉显卡因塞入科学计算核心而涨价
- **2012 年 AlexNet**：Ilya Sutskever、Alex Krizhevsky 与 Geoffrey Hinton 三人合作，在 NVIDIA GPU 上一飞冲天，证明 GPU 做 AI 的巨大价值 

## 关联
- 相关概念: [DeepSeekMoE：混合专家架构](/architecture/concept-deepseek-moe)（DeepSeekMoE，需 CUDA 平台运行）
- 相关概念: [企业级 AI 部署：硬件选型与框架选择](/inference-deploy/concept-enterprise-ai-deployment)（企业级 AI 部署与框架选择）
- 相关概念: [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai)（高并发推理与 CUDA 加速库）
- 参见: [NVIDIA H100 GPU](/base-models/model-h100)（H100 GPU 硬件）
- 参见: [vLLM](/inference-deploy/product-vllm)（vLLM 推理框架，依赖 CUDA）

## 引用来源
- [1]  — CUDA 定义、流程、重要性
- [2]  — 至暗时期与 AlexNet 转折

## 变更记录
- 2026-06-10: 初始创建，来源 
