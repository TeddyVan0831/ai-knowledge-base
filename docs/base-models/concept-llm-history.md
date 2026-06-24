---
title: "大语言模型发展简史"
outline: deep
---

# 大语言模型发展简史

> **创建时间**: 2026-05-27
> **最后更新**: 2026-05-27
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-27
> **最后更新**: 2026-05-27
> **来源**: 
> **领域**: ai

## 摘要

从 2017 年 Transformer 架构到 2025 年 DeepSeek-R1 的大语言模型发展脉络，涵盖四个里程碑：Transformer (2017)、GPT-3 (2020)、ChatGPT (2022)、DeepSeek-R1 (2025)。

## 详情

### 第一阶段：Transformer 革命 (2017)

Vaswani 等人发表论文《Attention is All You Need》引入 Transformer 架构，解决 RNN/LSTM 的关键限制（计算效率低、训练时间长、梯度消失） 。

**核心创新** ：
- **自注意力机制**：允许模型动态权衡每个 token 相对于其他 token 的重要性，支持并行计算
- **多头注意力**：多个独立注意力头并行操作，从多个角度捕捉语义关系
- **位置编码**：通过正弦/余弦函数将位置信息注入输入嵌入

### 第二阶段：预训练 Transformer 时代 (2018–2020)

- **BERT (2018)**：Google 推出，使用 Transformer 编码器 (Encoder)，双向训练，掩码语言建模 (MLM) + 下一句预测 (NSP) 
- **GPT (2018)**：OpenAI 推出，仅解码器 (Decoder) 架构，参数 1.17 亿，4.6GB 训练数据 
- **GPT-2 (2019)**：参数 15 亿，40GB 训练数据，零样本学习能力 
- **GPT-3 (2020)**：参数 1750 亿，展示少样本/零样本学习，标志 LLM 真正引起广泛关注 

### 第三阶段：后训练对齐 (2021–2022)

- **SFT (监督微调)**：在高质量输入-输出对上训练模型，但可扩展性有限 
- **RLHF (基于人类反馈的强化学习)**：训练奖励模型 + PPO 强化学习微调，解决 SFT 的可扩展性限制 
- **ChatGPT (2022)**：基于 GPT-3.5 + RLHF，引发"ChatGPT 时刻" 

### 第四阶段：多模态与推理模型 (2023–2025)

- **GPT-4V (2023)**：整合文本与图像 
- **GPT-4o (2024)**：整合文本、图像、音频、视频 
- **OpenAI o1 (2024)**：长链思维 (Long CoT)，AIME 2024 解决 74%-93% 的问题，而 GPT-4o 仅为 12% 
- **DeepSeek-R1 (2025)**：训练成本约 560 万美元，GRPO 强化学习，推理成本比 o1 便宜 20-50 倍，开源 

## 关联

- 相关概念: [In-Context Learning](/base-models/concept-in-context-learning), [推理模型（Reasoning Models）](/base-models/concept-reasoning-models), [RLHF（基于人类反馈的强化学习）](/training-optimization/concept-rlhf), [Few-Shot Prompting](/base-models/concept-few-shot-prompting), [大语言模型训练范式](/base-models/concept-llm-training-paradigm)
- 相关实体: [Qwen3-Embedding 系列](/base-models/model-qwen3-embedding), [Meta / Facebook](/base-models/company-meta), [OpenAI](/base-models/company-openai), [Google / Alphabet](/base-models/company-google), [Anthropic](/base-models/company-anthropic)
- 参见: [模型优化](/training-optimization/topic-model-optimization)

## 引用来源

- [1]  — LLM 简史完整时间线

## 变更记录

- 2026-05-27: 初始创建
