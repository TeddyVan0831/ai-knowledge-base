---
title: "训练与优化"
outline: deep
---

# 训练与优化

大语言模型的全生命周期优化 —— 从微调、量化、剪枝、蒸馏，到 RLHF/WebRL 强化学习对齐。

## 高效微调

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-llm-fine-tuning](./concept-llm-fine-tuning) | LLM 微调原理 | LoRA/QLoRA 等参数高效微调（PEFT）技术 |
| [topic-model-optimization](./topic-model-optimization) | 模型优化 | 五大技术路线的全景方法论 |

## 压缩与加速

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-quantization-ptq](./concept-quantization-ptq) | 后训练量化（PTQ） | 7B 模型从 14GB 压缩至 3.5GB（INT4） |
| [concept-quantization-rotation](./concept-quantization-rotation) | 旋转量化与极低比特量化 | INT4 是边缘部署甜点，更低比特需配合 QAT |
| [concept-model-pruning](./concept-model-pruning) | 模型剪枝与稀疏化 | 非结构化和结构化剪枝实现模型压缩 |
| [concept-knowledge-distillation](./concept-knowledge-distillation) | 知识蒸馏 | 大模型（教师）输出分布指导小模型（学生）训练 |

## 强化学习对齐

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-rlhf](./concept-rlhf) | RLHF（基于人类反馈的强化学习） | 2022 年 OpenAI 引入的后训练对齐技术 |
| [concept-webrl](./concept-webrl) | WebRL：网页强化学习框架 | 智谱自进化在线课程强化学习框架 |
| [concept-orm-reward-model](./concept-orm-reward-model) | ORM：结果监督奖励模型 | WebRL 核心组件，准确率 80.8% |
