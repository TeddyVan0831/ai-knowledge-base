---
title: "AI 经典论文汇览"
outline: deep
---

# AI 经典论文汇览

> **类型**: topic
> **创建时间**: 2026-06-10
> **最后更新**: 2026-06-10
> **来源**: 综合知识库中 [[raw/]] 全部 42 篇笔记

## 摘要
本文汇总了 AI 知识库中引用的 65+ 篇经典论文，按主题分为 13 个领域：基础架构、对齐与 RLHF、推理模型、推理加速、注意力优化、KV Cache 管理、量化、高效微调、知识蒸馏、Agent 与推理框架、视觉识别与生成、RAG 检索增强、安全与评估。每篇论文标注了年份、会议、来源文件和相关 Wiki 概念页。


## 二、对齐与 RLHF

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **InstructGPT** | Ouyang et al. (OpenAI) | 2022 | arXiv:2203.02155 | ,  |
| **PPO** | Schulman et al. (OpenAI) | 2017 | arXiv:1707.06347 |  |
| **DPO** | Rafailov et al. | 2023 | NeurIPS 2023 |  |

> **关联 Wiki**: [RLHF（基于人类反馈的强化学习）](/training-optimization/concept-rlhf) | [推理模型（Reasoning Models）](/base-models/concept-reasoning-models)

---

## 三、推理加速 & 推测解码

| 论文 | 作者 | 年份 | 来源 |
|------|------|------|------|
| **Speculative Decoding** | Leviathan et al. (Google) | 2022 | ,  |
| **Speculative Sampling** | Chen et al. (DeepMind) | 2023 |  |
| **MEDUSA** | — | 2024 | ,  |
| **EAGLE** | — | 2024 | ,  |
| **EAGLE-2** | — | 2024 | ,  |
| **EAGLE-3** | — | 2025 | ,  |
| **Multi-Token Prediction (MTP)** | Meta | 2024 |  |

> **关联 Wiki**: [AI 服务高并发原理与性能监控调优](/inference-deploy/concept-high-concurrency-ai) | [投机解码（Speculative Decoding）](/architecture/concept-speculative-decoding) | [TTFT 优化（首 Token 延迟）](/architecture/concept-ttft-optimization) | [MTP：多 Token 预测（Multi-Token Prediction）](/architecture/concept-mtp-multi-token-prediction)

---

## 四、注意力机制优化

| 论文 | 作者 | 年份 | 来源 |
|------|------|------|------|
| **MQA（Multi-Query Attention）** | Shazeer et al. | 2019 |  |
| **GQA（Grouped-Query Attention）** | Ainslie et al. | 2023 |  |
| **FlashAttention** | Dao et al. | 2022 |  |
| **FlashAttention-2** | Tri Dao | 2023 |  |

> **关联 Wiki**: [注意力机制优化](/architecture/concept-attention-optimization) | [Transformer 架构](/base-models/concept-transformer-architecture) | [MLA：多头潜在注意力（Multi-head Latent Attention）](/architecture/concept-mla-multi-head-latent-attention)

---

## 五、KV Cache 管理 & 推理框架

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **vLLM (PagedAttention)** | Kwon et al. (LMSYS/Berkeley) | 2023 | SOSP | ,  |
| **SGLang (RadixAttention)** | Zheng et al. (LMSYS) | 2024 | NeurIPS | ,  |
| **H2O（Heavy-Hitter Oracle）** | Zhang et al. | 2023 | NeurIPS |  |
| **StreamingLLM** | Xiao et al. | 2023 | — |  |
| **KVQuant** | — | 2024 | — |  |

> **关联 Wiki**: [KV Cache](/architecture/concept-kv-cache) | [KV Cache 动态压缩](/architecture/concept-kv-cache-compression) | [KV Cache 量化](/architecture/concept-kv-cache-quantization) | [vLLM](/inference-deploy/product-vllm) | [SGLang](/inference-deploy/product-sglang)

---

## 六、量化技术

### 后训练量化（PTQ）

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **GPTQ** | Frantar et al. | 2023 | ICLR | ,  |
| **AWQ** | Lin et al. | 2023 | — | ,  |
| **SmoothQuant** | Xiao et al. | 2023 | ICML | ,  |

### 旋转量化 & 极低比特

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **QuaRot** | Ashkboos et al. | 2024 | NeurIPS |  |
| **BitNet b1.58** | Microsoft | 2024 | — |  |

> **关联 Wiki**: [后训练量化（PTQ）](/training-optimization/concept-quantization-ptq) | [旋转量化与极低比特量化](/training-optimization/concept-quantization-rotation) | [FP8 混合精度训练](/architecture/concept-fp8-mixed-precision)

---

## 七、高效微调

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **LoRA** | Hu et al. (Microsoft) | 2021 | ICLR | ,  |
| **QLoRA** | Dettmers et al. | 2023 | NeurIPS |  |

> **关联 Wiki**: [LLM 微调原理](/training-optimization/concept-llm-fine-tuning)

---

## 八、知识蒸馏 & 模型压缩

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **Distilling the Knowledge in a Neural Network** | Hinton et al. | 2015 | NeurIPS Workshop |  |
| **Born Again Neural Networks (BAN)** | Furlanello et al. | 2018 | ICML |  |
| **Deep Compression** | Han et al. | 2016 | ICLR |  |

> **关联 Wiki**: [知识蒸馏](/training-optimization/concept-knowledge-distillation) | [模型剪枝与稀疏化](/training-optimization/concept-model-pruning)

---

## 九、Agent & 推理框架

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **Chain-of-Thought (CoT)** | Wei et al. (Google) | 2022 | NeurIPS | ,  |
| **Self-Consistency** | Wang et al. | 2022 | — |  |
| **Tree of Thoughts (ToT)** | Yao et al. | 2023 | NeurIPS |  |
| **ReAct** | Yao et al. | 2022 | arXiv:2210.03629 | , ,  |
| **Generative Agents (Smallville)** | Park et al. (Google/Stanford) | 2023 | UIST |  |
| **Multi-Agent Design** | — | 2025 | arXiv:2502.02533 |  |
| **Self-Improving Coding Agent** | Robeyns et al. | 2025 | arXiv:2504.15228 |  |
| **MLGym** | Nathani et al. | 2025 | arXiv:2502.14499 |  |
| **Multi-Agent Fault Tolerance** | Shi et al. | 2024 | arXiv:2412.00534 |  |
| **Code Generation Survey** | Jiang et al. | 2024 | arXiv:2406.00515 |  |
| **DirectGPT** | Masson et al. | 2024 | arXiv:2310.03691 |  |

> **关联 Wiki**: [Agent：从可控性到自主反思](/agent/concept-agent-controllability) | [提示链（Prompt Chaining）](/agent/concept-prompt-chaining) | [路由（Agent Routing）](/agent/concept-agent-routing) | [反思（Reflection）](/agent/concept-reflection) | [工具使用（Tool Use / Function Calling）](/agent/concept-tool-use) | [多智能体协作（Multi-Agent Collaboration）](/agent/concept-multi-agent-collaboration) | [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development) | [Agent 设计模式](/agent/topic-agentic-design-patterns)

---

## 十、RAG 检索增强生成

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **RAG** | Lewis et al. (Meta) | 2020 | NeurIPS |  |
| **Lost in the Middle** | Liu et al. | 2023 | TACL 2024 |  |
| **GraphRAG** | Microsoft | 2024 | — |  |
| **RAG-MCP** | Gan & Sun | 2025 | arXiv:2505.03275 |  |

> **关联 Wiki**: [RAG（检索增强生成）](/rag/concept-rag) | [Agentic RAG](/rag/concept-agentic-rag) | [In-Context Learning](/base-models/concept-in-context-learning) | [RAG 高级检索技术](/rag/concept-rag-advanced-retrieval) | [Query 改写（查询改写）](/rag/concept-query-rewriting)

---

## 十一、视觉识别 & 自监督学习

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **LeNet-5** | LeCun et al. | 1998 | IEEE |  |
| **AlexNet** | Krizhevsky, Sutskever & Hinton | 2012 | NeurIPS | ,  |
| **ResNet** | Kaiming He et al. | 2015 | CVPR | , ,  |
| **GoogLeNet** | Szegedy et al. | 2014 | CVPR |  |
| **SENet** | Hu et al. | 2017 | CVPR |  |
| **ViT** | Dosovitskiy et al. | 2021 | ICLR |  |
| **Swin Transformer** | Liu et al. (MSRA) | 2021 | ICCV |  |
| **CLIP** | Radford et al. (OpenAI) | 2021 | ICML | ,  |
| **VL-BERT** | Su et al. | 2019 | ICLR 2020 |  |
| **MAE** | Kaiming He et al. | 2021 | CVPR 2022 |  |
| **Sapiens** | Meta | 2024 | — |  |

### 目标检测 & 分割

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **YOLOv1** | Redmon et al. | 2015 | arXiv:1506.02640 | ,  |
| **YOLOv3** | Redmon et al. | 2018 | arXiv:1804.02767 | ,  |
| **Faster R-CNN** | Ren et al. (Microsoft) | 2015 | NeurIPS |  |
| **U-Net** | Ronneberger et al. | 2015 | MICCAI |  |

> **关联 Wiki**: [视觉识别技术](/multimodal/concept-vision-recognition) | [视觉检测与视觉大模型在工业质检中的应用](/multimodal/concept-vision-quality-inspection) | [多模态 Transformer](/multimodal/concept-multimodal-transformer) | [Meta Sapiens：人体视觉基座模型](/multimodal/concept-meta-sapiens) | [MAE（Masked Autoencoder）掩码自编码器](/multimodal/concept-mae-masked-autoencoder) | [Humans-300M 数据集](/multimodal/concept-humans-300m-dataset)

---

## 十二、图像 & 视频生成

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **DDPM** | Ho et al. | 2020 | NeurIPS |  |
| **Stable Diffusion (LDM)** | Rombach et al. | 2021 | CVPR 2022 | ,  |
| **ViViT** | Arnab et al. (Google) | 2021 | ICCV |  |
| **DiT (Diffusion Transformer)** | Peebles & Xie | 2023 | ICCV |  |
| **Sora** | OpenAI | 2024 | — |  |
| **CatVTON** | — | 2024 | ICLR 2025 |  |

> **关联 Wiki**: [图像生成技术](/multimodal/concept-image-generation) | [视频生成模型](/multimodal/concept-video-generation) | [多模态前沿：Agent 构建与视频 AIGC](/multimodal/concept-multimodal-edge)

---

## 十三、安全、评估与 MCP 协议

| 论文 | 作者 | 年份 | 来源 |
|------|------|------|------|
| **LLM-as-a-Judge** | Li et al. | 2024 |  |
| **Agent-as-a-Judge** | Zhuge et al. | 2024 |  |
| **Concrete Problems in AI Safety** | Amodei et al. | 2016 |  |
| **Unsolved Problems in ML Safety** | Hendrycks et al. | 2023 |  |
| **TruthfulQA** | Lin et al. | 2022 | ACL 2022 |  |
| **MCP Security Landscape** | Hou et al. | 2025 |  |

> **关联 Wiki**: [Agent 质量评估](/agent/concept-agent-evaluation) | [MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp) | [护栏与安全模式（Safety Guardrails）](/agent/concept-safety-guardrails)

---

## 十四、其他

| 论文 | 作者 | 年份 | 会议 | 来源 |
|------|------|------|------|------|
| **Word2Vec** | Mikolov et al. (Google) | 2013 | arXiv:1301.3781 |  |

> **关联 Wiki**: [Word2Vec](/base-models/concept-word2vec) | [Embedding（嵌入）](/base-models/concept-embedding)

---

## 统计一览

| 维度 | 数据 |
|------|------|
| **论文总数** | 65+ |
| **覆盖会议** | CVPR, NeurIPS, ICLR, ICML, ICCV, NAACL, ACL, TACL, MICCAI, UIST, SOSP, IEEE |
| **高引作者** | Vaswani, Kaiming He (何恺明), Hinton, Sutskever, Radford, Schulman, Tri Dao, Shazeer |
| **被引最多的论文** | "Attention Is All You Need" — 跨最多笔记文件引用 |

### 按年份分布

- 2024-2025: 约 25 篇（推理模型、DeepSeek 系列、Agent 最新进展）
- 2021-2023: 约 22 篇（ViT, LoRA, Flash Attention, 量化, vLLM, DPO）
- 2017-2020: 约 12 篇（Transformer, GPT, BERT, Scaling Laws）
- 2017 年之前: 约 6 篇（CNN 基础、知识蒸馏、Word2Vec）

---

## 关联
- 相关概念: [Transformer 架构](/base-models/concept-transformer-architecture)（Transformer 源头论文）
- 相关概念: [DeepSeekMoE：混合专家架构](/architecture/concept-deepseek-moe)（DeepSeek 系列论文）
- 相关概念: [推理模型与 DeepSeek R1：从 R1-Zero 到多阶段训练](/base-models/concept-reasoning-models-deepseek-r1)（R1 推理模型）
- 相关概念: [视觉识别技术](/multimodal/concept-vision-recognition)（视觉经典论文）
- 参见: [模型优化](/training-optimization/topic-model-optimization) | [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development) | [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops)

## 引用来源
- [1]  — LLM 演进史中的论文引用
- [2]  至  — 各篇学习笔记中的论文引用
- [3]  — PDF 电子书中的论文引用

## 变更记录
- 2026-06-10: 初始创建，综合知识库 42 篇 raw 笔记 + ebook 文献
