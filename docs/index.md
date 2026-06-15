---
title: "AI 知识库 — 全景速览"
outline: false
---

# AI 知识库全景速览

> **AI 知识图谱** —— 这一页速览全部 113 个核心概念。每个概念给「一句话」，快速建立全图认知。需要深入细节时点击「详细 →」进入对应页面。

---

## 基础模型与训练

一切 AI 能力的起点——从 Transformer 架构到 LLM 训练范式，从经典模型到前沿推理。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| Transformer 架构 | 自注意力 + FFN + 残差归一化的 decoder-only 解码块 | [→](/base-models/concept-transformer-architecture) |
| Embedding 与向量化 | 将离散文本映射到稠密向量空间的核心技术 | [→](/base-models/concept-embedding) |
| LLM 训练范式 | 预训练 → SFT → RLHF 的分阶段训练方法论 | [→](/base-models/concept-llm-training-paradigm) |
| 推理模型 | 2024 年起的新范式——从模式匹配到结构化逻辑推理 | [→](/base-models/concept-reasoning-models) |
| DeepSeek R1 | 推理模型里程碑——纯强化学习训练出思维链能力 | [→](/base-models/concept-reasoning-models-deepseek-r1) |
| In-Context Learning | RAG 的底层能力——模型看着参考资料回答但不"学会" | [→](/base-models/concept-in-context-learning) |

[基础模型全部 20 页 →](/base-models/)

## 模型架构

模型"长什么样"——现代 LLM 的解剖结构与关键演进。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| DeepSeek MoE | DeepSeekV3 的混合专家架构——稀疏激活 + 无辅助损失负载均衡 | [→](/architecture/concept-deepseek-moe) |
| MLA | Multi-head Latent Attention——大幅降低 KV Cache 的内存占用 | [→](/architecture/concept-mla-multi-head-latent-attention) |
| 注意力机制优化 | Flash Attention / MQA / GQA / 稀疏注意力 / 线性注意力 | [→](/architecture/concept-attention-optimization) |
| KV Cache | 缓存历史 K/V 避免重算——自回归推理部署的基础 | [→](/architecture/concept-kv-cache) |

[模型架构全部 12 页 →](/architecture/)

## 训练与优化

如何让模型更小、更快、更好——微调、量化、剪枝、蒸馏、强化学习对齐。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| LLM 微调 | LoRA / QLoRA 高效微调——冻结基座只训练低秩增量 | [→](/training-optimization/concept-llm-fine-tuning) |
| 后训练量化 | GPTQ / AWQ / SmoothQuant——将 FP16 模型压缩至 INT8/INT4 | [→](/training-optimization/concept-quantization-ptq) |
| 知识蒸馏 | 大模型教师指导小模型学生学习"暗知识" | [→](/training-optimization/concept-knowledge-distillation) |
| RLHF | 用人类偏好做强化学习的经典对齐路线 | [→](/training-optimization/concept-rlhf) |
| WebRL | 自进化网页强化学习框架——AutoGLM 的核心创新 | [→](/training-optimization/concept-webrl) |

[训练与优化全部 9 页 →](/training-optimization/)

## 推理与部署

从云端到边缘——GPU 选型、高并发、框架选择、边缘推理。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| 企业级 AI 部署 | GPU 选型 + 内存墙 + 四大推理框架 + 结构化输出 | [→](/inference-deploy/concept-enterprise-ai-deployment) |
| llama.cpp | 零依赖、纯 C/C++ 的边缘推理框架——GGUF 量化 + 平台优化 | [→](/inference-deploy/concept-llamacpp) |
| SGLang 优化 | RadixAttention + PD 分离——吞吐量高达 6.4x vs vLLM | [→](/inference-deploy/concept-sglang-optimization) |
| 边缘推理全景 | llama.cpp vs MediaPipe vs MNN 三大框架对比与选择决策树 | [→](/inference-deploy/topic-edge-inference) |

[推理与部署全部 16 页 →](/inference-deploy/)

## Agent 智能体

让 LLM 从"回答问题"到"完成复杂任务"——设计模式、通信协议、评估体系。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| MCP 协议 | Model Context Protocol——标准化 Agent 与工具的 N×M 集成 | [→](/agent/concept-mcp) |
| AutoGLM | 智谱发布的智能体操作框架——让 AI 在屏幕上替代人类操作 | [→](/agent/concept-autoglm) |
| Prompt Chaining | 将复杂任务拆解为序列化的子任务链 | [→](/agent/concept-prompt-chaining) |
| Agent 开发综述 | 从原理到实践的 Agent 全览——五级分类到部署运维 | [→](/agent/topic-agent-development) |

[Agent 全部 29 页 →](/agent/)

## RAG 检索增强

给 LLM 接上外部知识——从基础检索到 Agentic RAG。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| RAG 基础 | 检索 + 生成的经典范式——用外部知识减少幻觉 | [→](/rag/concept-rag) |
| Agentic RAG | 让 Agent 自己决定查什么、怎么查、查完怎么看 | [→](/rag/concept-agentic-rag) |
| Text-to-SQL | 自然语言转数据库查询——Vanna 框架与 SQL Copilot | [→](/rag/concept-text-to-sql) |

[RAG 全部 7 页 →](/rag/)

## 多模态与视觉

LLM 之外的另一条主线——图像/视频生成、数字人、视觉识别。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| 视频生成 | ViViT → 3D UNet → DiT → Sora 的完整演进 | [→](/multimodal/concept-video-generation) |
| 数字人技术 | 五层架构 + 语音/形象/大脑建模 + 国内外平台对比 | [→](/multimodal/concept-digital-human) |
| 图像生成 | GAN → VAE → Diffusion → Stable Diffusion 技术演进 | [→](/multimodal/concept-image-generation) |

[多模态全部 11 页 →](/multimodal/)

## 行业应用案例

AI 在真实业务场景中的落地实践。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| 财务表格 AI | 通义千问/DeepSeek/GPT-4o 在预算表格识别中的横向评测 | [→](/industry-cases/concept-ai-table-recognition-evaluation) |
| 培训对练智能体 | 8 种顾客性格 × 6 种场景 + 意愿值 + 三角色商业架构 | [→](/industry-cases/concept-ai-training-agent) |
| 直播 AI 助手 | Chrome 插件 + Tampermonkey + Coze 三步架构 | [→](/industry-cases/concept-live-streaming-ai-assistant) |

[行业应用全部 4 页 →](/industry-cases/)

## 工具与生态

GPU 硬件、CUDA 生态、芯片竞争——AI 的"基础设施"。

| 概念 | 一句话 | 详细 |
|------|--------|------|
| NVIDIA 五大壁垒 | 硬件/互联/软件生态/开发者/系统——英伟达的护城河 | [→](/tools-ecosystem/concept-nvidia-five-barriers) |
| ASML EUV 光刻 | 芯片制造之巅——ASML 如何垄断 EUV 光刻设备 | [→](/tools-ecosystem/concept-asml-euv-lithography) |
| AI 经典论文 | 从 Attention Is All You Need 到 DeepSeek 的必读论文汇览 | [→](/tools-ecosystem/topic-ai-classic-papers) |

[工具与生态全部 5 页 →](/tools-ecosystem/)

---

**关于本知识库**：基于 Andrej Karpathy 的 LLM Wiki 模式构建，将原始学习笔记编译为结构化知识层。113 个页面、9 大主题域、完整的交叉引用网络。

[如何阅读 →](/guide/) · [GitHub →](https://github.com/teddyvan0831/ai-knowledge-base)
