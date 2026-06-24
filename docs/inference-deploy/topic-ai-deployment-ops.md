---
title: "AI 部署与运维主题综述"
outline: deep
---

# AI 部署与运维主题综述

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: , , , 
> **类型**: topic
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: , , , 
> **领域**: ai

## 摘要

本主题综述企业级 AI 从硬件选型到部署运维的完整技术链路，涵盖 GPU 硬件选型（从 H100 到 B300）、内存墙问题与带宽优先趋势、四大推理框架（Ollama/vLLM/SGLang/TensorRT-LLM）选型、高并发原理（KV Cache、PagedAttention、推测解码、EAGLE 系列）、SGLang 深度优化（RadixAttention、PD 分离）、以及 OpenClaw/Hermes 智能体系统的部署架构。

## 详情

### 一、硬件选型：从算力优先到带宽优先

2026 年硬件选型逻辑已从**算力优先**转向**带宽优先 + 显存容量优先** 。大模型推理 **90% 的时间花在数据搬运而非计算上** ，SRAM 计算极快，但 HBM 搬运速度比计算慢 50 倍以上 → GPU 算力被内存带宽卡死 。

核心 GPU 型号从 H100（80GB HBM3 / 3.35TB/s）到 B300（288GB HBM3e / 8TB/s），显存和带宽逐代翻倍 。Blackwell 架构带来 FP4 精度（内存占用减半）、第五代 NVLink（带宽 1.8TB/s）、GB200 超级芯片能效比 H100 最高约 25 倍 。

**资源配比建议**：每 1 张 GPU 配 16-32 核 CPU + 512GB-1TB DRAM 。2026 年新建机房必须预留液冷基础设施，传统风冷已无法满足 Blackwell 集群需求 。

详见：[企业级 AI 部署：硬件选型与框架选择](/inference-deploy/concept-enterprise-ai-deployment)

### 二、推理框架选型：四大框架互补

| 框架 | 定位 | 适用场景 |
|------|------|----------|
| Ollama | 本地单用户调试工具 | 快速验证、教育、边缘设备 |
| vLLM | 通用推理引擎（生态最成熟） | 生产环境通用，大批量 Prompt |
| SGLang | 复杂 LLM 程序运行时 | 多轮对话、Agent/CoT/RAG、结构化输出 |
| TensorRT-LLM | 硬件原生优化 | 极致性能的 NVIDIA GPU 环境，Blackwell 上 FP4 推理必需 |



**Ollama 的局限性**：不支持 PagedAttention 与 Continuous Batching → 高并发能力有限，更适合单用户调试。Go 的并发 ≠ 推理层的连续批处理 。

详见：[企业级 AI 部署：硬件选型与框架选择](/inference-deploy/concept-enterprise-ai-deployment)

### 三、高并发原理：KV Cache 是显存杀手

模型参数本身只占 14GB，KV Cache 才是高并发场景下真正的显存杀手。以 LLaMA-2-7B 为例，每 token KV Cache 为 0.5 MB，上下文 4096 tokens = 2 GB/请求，并发 100 请求 = 200 GB >> A100 80GB 。

**PagedAttention 三机制**：
1. 按需分配（省 94.5% 显存）
2. 写时复制（Beam Search/Parallel Sampling 省 ~50%）
3. 动态重排（Continuous Batching 关键）

**Continuous Batching**：GPU 利用率从 40-60% 提升到 85-95%，吞吐量从 800 提升到 1800 tokens/s（2.25x）。

详见：[AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai)

### 四、推理加速技术矩阵

| 技术 | 加速比 | 适用场景 |
|------|--------|----------|
| PagedAttention | 2-4x（内存效率） | 所有高并发场景 |
| Continuous Batching | 1.5-2.25x | 多请求并发 |
| 推测解码 | 1.5-3x | 单个大模型推理 |
| MEDUSA | 2.2-2.8x | 单模型加速 |
| EAGLE | 2.7-3.5x | 单模型加速 |
| EAGLE-2 | 3.0-4.3x | 单模型加速 |
| EAGLE-3 | 峰值 6.5x | 单模型加速 |

，

所有加速技术可叠加使用：PagedAttention（基础）+ Continuous Batching（调度）+ EAGLE-2（生成）。EAGLE-2 效果最强（3.0-4.3x），部署最简单（无需额外模型）。

详见：[AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai)、[投机解码（Speculative Decoding）](/architecture/concept-speculative-decoding)

### 五、SGLang 深度优化：从模型到业务逻辑

**定位差异**：vLLM 是跑模型的，SGLang 是跑业务逻辑的 。SGLang 实现了高达 6.4 倍的吞吐量提升（NeurIPS 2024 正式版论文数据）。

**PD 分离架构**：Prefill（计算密集型）与 Decode（内存带宽密集型）物理隔离，各自使用特化 GPU 资源，消除互相干扰 。

**RadixAttention**：用基数树管理 KV 缓存，边标记序列而非单个 token，缓存感知调度按前缀长度排序请求，优先处理缓存命中率高的。在 A10G GPU 上吞吐量提升高达 5x 。

**压缩 FSM**：将相邻单次转移边合并，一次前向传递解码多个 token，大幅加速约束解码 。

**本地实验**：在 RTX 4090 上 Qwen3-0.6B，SGLang 相比 vLLM 实现 3.5x 吞吐提升、2.8x 共享前缀加速 。

详见：[SGLang 深度优化：Radix 缓存与极致吞吐](/inference-deploy/concept-sglang-optimization)

### 六、OpenClaw/Hermes 智能体系统部署

OpenClaw 的核心响应过程：**入口 → 接入 → 准备 → 主回路 → 回写 → 沉淀 → 继续/结束** 。三大特性：可见、可恢复、可继续 。

**关键构件**：
- Gateway（入口层，高扩展性）
- Session（状态管理，低扩展性）
- Agent Loop（执行回路，深耦合核心）
- Memory（沉淀层，Markdown 文件化记忆）
- Skills（行为策略层，高扩展性）

**Hermes 升级**：四级分层记忆（标题→摘要→全文→深层参考）、心跳增强（状态持久化、动态频率控制、上下文感知）、Skill 全自动提炼与 GEPA 进化、任务并行与失败隔离（主 Agent 永不挂）。

**准确率与风险矩阵**：OpenClaw 更适合作为入口层、网关层、协作层。高正确率 + 低行动风险场景（政策问答、知识检索）最现实。高行动风险场景（审批、财税、生产系统）不适合纯 OpenClaw 直接独立承担 。

**系统工程公式**：任务约束 + 预算约束 + 验证约束 + 泄露约束 。

详见：[OpenClaw 与 Hermes 智能体系统](/inference-deploy/concept-openclaw-hermes)

### 七、部署全景图

```
硬件层 ──────→ GPU 选型（H100/H200/B200/B300）
              带宽优先，显存容量优先
              每 1 GPU : 16-32 核 CPU : 512GB-1TB DRAM

推理层 ──────→ PagedAttention（内存层，所有场景）
              Continuous Batching（调度层，多请求并发）
              推测解码/EAGLE（算法层，Decode 加速）
              PD 分离（架构层，Prefill/Decode 解耦）

框架层 ──────→ vLLM（通用推理，生态最全）
              SGLang（复杂业务逻辑，RadixAttention）
              TensorRT-LLM（极致性能，FP4 必需）
              Ollama（本地调试，非生产级）

服务层 ──────→ OpenClaw（入口层 + 回路 + 状态 + 回写）
              Hermes（管家级升级：四级记忆、心跳增强、任务并行）

应用层 ──────→ 风险矩阵指导落地场景选择
              系统工程公式保障正确率
```

## 关联

- 相关概念: [企业级 AI 部署：硬件选型与框架选择](/inference-deploy/concept-enterprise-ai-deployment) — 企业级 AI 部署：硬件选型与框架选择
- 相关概念: [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai) — AI 服务高并发原理与性能监控调优
- 相关概念: [SGLang 深度优化：Radix 缓存与极致吞吐](/inference-deploy/concept-sglang-optimization) — SGLang 深度优化：Radix 缓存与极致吞吐
- 相关概念: [OpenClaw 与 Hermes 智能体系统](/inference-deploy/concept-openclaw-hermes) — OpenClaw 与 Hermes 智能体系统
- 相关概念: [Text-to-SQL 与数据智能](/rag/concept-text-to-sql) — Text-to-SQL 与数据智能
- 相关概念: [视觉检测与视觉大模型在工业质检中的应用](/multimodal/concept-vision-quality-inspection) — 视觉检测与视觉大模型在工业质检中的应用

## 引用来源

- [1]  — 硬件选型 + 框架选择
- [2]  — 高并发原理 + 性能调优
- [3]  — SGLang 深度优化
- [4]  — OpenClaw 与 Hermes 智能体系统

## 变更记录

- 2026-05-26: 初始创建，综合 4 篇原始学习笔记
