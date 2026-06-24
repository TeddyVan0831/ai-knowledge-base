---
title: "AI API 端点协议"
outline: deep
---

# AI API 端点协议

> **创建时间**: 2026-06-17
> **最后更新**: 2026-06-17
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-06-17
> **最后更新**: 2026-06-17
> **来源**: 
> **领域**: ai

## 摘要

AI API 的路径后缀不是随便写的——每一个 `/v1/chat/completions`、`/v1/responses`、`/v1/messages` 都代表一套完整的接口协议，规定了请求格式、响应格式、流式传输和工具调用方式。理解它们之间的差异与演进，能避免 "OpenAI-compatible 却不完全兼容" 的调试陷阱。

## 详情

### 演变历程

**① `/v1/completions` — 纯文本续写**：最早的 LLM 接口，无 role 概念、无 system message、无对话历史。需要手动在 prompt 中拼接角色对话。已退居二线。

**② `/v1/chat/completions` — 结构化对话**：将对话抽象为 messages 数组，每条消息有明确 role（system/user/assistant/tool）。被整个行业接受为事实标准——OpenAI、Mistral、xAI、DeepSeek 都用相同协议内核。

**⚠️ 兼容陷阱**：各平台都说自己 "OpenAI-compatible"，但兼容程度差很大：

| 能力 | 兼容程度 |
|------|----------|
| 基础文本聊天 | 几乎都能跑通 |
| stream 流式输出 | 大部分没问题 |
| tools 工具调用 | 参差不齐 |
| response_format 结构化输出 | 参差不齐 |
| vision / audio | 参差不齐 |



**③ `/v1/responses` — 任务型接口**：OpenAI 新接口，不再把交互框定为「聊天」，而是抽象为「任务」。输出包含多个 item（文本、工具调用、工具结果、推理步骤），更适合 Agent/多步骤任务流。

### 三家厂商对比

| 维度 | OpenAI | Anthropic | Google Gemini |
|------|--------|-----------|---------------|
| 核心接口 | `/v1/chat/completions` | `/v1/messages` | `/v1beta/models/{model}:generateContent` |
| system 位置 | messages 数组内 | 顶层字段 | contents 内 |
| 响应路径 | `choices[0].message.content` | `content[0].text` | `candidates[0].content.parts` |
| 内容结构 | 字符串或数组 | block 数组 | parts 数组 |
| 设计哲学 | 聊天补全 → 统一响应 | 独立消息协议 | 资源+方法（Google API 风格） |



### 配套接口

| 接口 | 功能 | 典型场景 |
|------|------|---------|
| `/v1/embeddings` | 文本转向量 | RAG 检索 |
| `/v1/models` | 列模型列表 | 调试/验证模型名 |



### 常见误区：`/v1` 不是模型版本

| 概念 | 含义 |
|------|------|
| API 版本（`/v1`） | 接口规范（字段名、错误格式、鉴权方式） |
| 模型版本 | 模型能力（上下文长度、推理能力、价格） |
| SDK 版本 | 客户端库（openai SDK 1.x / 2.x） |

三者各管各的，`/v1` 不是「第一代模型」。

### Base URL 配置要点

- **Base URL** 填到 `/v1`，不要带后面的 `/chat/completions`——SDK 会自动拼接
- **Endpoint / Full URL** 才填完整路径
- 填错导致 `404` 的最常见原因：Base URL 带了 `/chat/completions`



### 平台前缀含义

| 平台 | 前缀 | 含义 |
|------|------|------|
| Groq `/openai` | 平台命名空间 | 「我不是 OpenAI，但兼容 OpenAI 协议」 |
| 阿里百炼 `/compatible-mode` | 兼容模式入口 | 「提供兼容 OpenAI 协议的入口」 |

### 选型建议

| 场景 | 推荐接口 |
|------|----------|
| 普通聊天 | `/v1/chat/completions` |
| Agent/多工具 | `/v1/responses` |
| Claude | `/v1/messages`（用 Anthropic SDK） |
| Gemini | `:generateContent`（按 Google 风格） |
| RAG | embeddings + 聊天接口 |



## 关联

- 相关概念: [MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp), [Embedding（嵌入）](/base-models/concept-embedding), [RAG（检索增强生成）](/rag/concept-rag)
- 相关概念: [Agent：从可控性到自主反思](/agent/concept-agent-controllability), [Function Calling — 模型的"手指"](/agent/concept-function-calling)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — AI API 端点协议详解：演变历史、跨厂商对比、选型指南

## 变更记录

- 2026-06-17: 初始创建，来源 
