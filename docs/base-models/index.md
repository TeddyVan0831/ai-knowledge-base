---
title: "基础模型与训练"
outline: deep
---

# 基础模型与训练

从 Transformer 架构到 LLM 训练范式，从 Embedding 原理到推理模型演进 —— 本模块覆盖 AI 大模型的全部基础知识。

## 基础概念

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-transformer-architecture](./concept-transformer-architecture) | Transformer 架构 | Google 2017 年提出的序列建模框架，几乎所有 AI 模型的基础架构 |
| [concept-llm-history](./concept-llm-history) | 大语言模型发展简史 | 从 2017 Transformer 到 2025 DeepSeek-R1 的发展脉络 |
| [concept-llm-training-paradigm](./concept-llm-training-paradigm) | 大语言模型训练范式 | 预训练 → SFT → 对齐的三阶段训练流程 |
| [concept-llm-wiki](./concept-llm-wiki) | LLM Wiki | Karpathy 提出的结构化知识系统架构 |

## 嵌入与语义

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-embedding](./concept-embedding) | Embedding（嵌入） | 将不同模态特征转换为固定维度稠密向量的降维技术 |
| [concept-word2vec](./concept-word2vec) | Word2Vec | Google 提出的词向量技术，奠定了现代 Embedding 的基础 |
| [concept-cosine-similarity](./concept-cosine-similarity) | 余弦相似度 | 衡量两个向量语义相似度的核心方法 |
| [concept-embedding-model-selection](./concept-embedding-model-selection) | Embedding 模型选型 | 基于 MTEB 榜单和业务场景权衡维度、上下文窗口和部署成本 |

## 提示与学习

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-in-context-learning](./concept-in-context-learning) | In-Context Learning | RAG 的底层能力 —— 模型能看着参考资料回答问题 |
| [concept-few-shot-prompting](./concept-few-shot-prompting) | Few-Shot Prompting | 在提示词中加入优秀回答样例以提升模型回答质量 |
| [concept-bayesian-reasoning](./concept-bayesian-reasoning) | 贝叶斯推理 | 在推理模型的 Chain-of-Thought 中提供数学基础 |

## 推理模型

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-reasoning-models](./concept-reasoning-models) | 推理模型（Reasoning Models） | LLM 发展的新范式，从模式匹配转向结构化逻辑推理 |
| [concept-reasoning-models-deepseek-r1](./concept-reasoning-models-deepseek-r1) | 推理模型与 DeepSeek R1 | R1-Zero 到多阶段训练的完整流程 |
| [concept-reasoning-techniques](./concept-reasoning-techniques) | 推理技术（Reasoning Techniques） | CoT、推理扩展等思考过程提升输出质量 |

## 模型档案

| 文件 | 标题 | 摘要 |
|------|------|------|
| [model-b200](./model-b200) | NVIDIA B200 GPU | 基于 Blackwell 架构的下一代 AI 旗舰 GPU，192GB HBM3e |
| [model-h100](./model-h100) | NVIDIA H100 GPU | 基于 Hopper 架构的企业级 AI GPU，7B-70B 模型的中流砥柱 |
| [model-rtx4090](./model-rtx4090) | NVIDIA RTX 4090 | 个人用户性价比最高的消费级 GPU，24GB GDDR6X |
| [model-bge-m3](./model-bge-m3) | BGE-M3 | 支持 100+ 语言的通用文本嵌入模型 |
| [model-jina-embedding](./model-jina-embedding) | Jina Embeddings V4 | 多模态多语言通用嵌入模型，支持 Matryoshka 表示 |
| [model-qwen3-embedding](./model-qwen3-embedding) | Qwen3-Embedding 系列 | 当前开源 Embedding 模型的性能标杆 |
