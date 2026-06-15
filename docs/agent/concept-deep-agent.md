---
title: "Deep Agent"
outline: deep
---

# Deep Agent

> **类型**: concept
> **创建时间**: 2026-05-27
> **最后更新**: 2026-05-27
> **来源**: 

## 摘要

Deep Agent 是 2025 年收敛的 Agent 技术形态，以 Claude Agent SDK 和 LangChain Deep Agent 为代表，具备行业性（够"垂"）、Long-running 稳定性、Main-Sub Agent 主从架构、自主规划、文件系统、上下文压缩等核心能力。

## 详情

### 两大特征

- **够"垂"（行业性）**：Agent 的知识和能力必须源于该行业的深度实践和共识，输出质量与行业专家无法区分 
- **Long-running（稳定性）**：能长时间持续运行不崩溃，能连续保质保量执行多步骤任务（可能涉及 50+ 个 tool/API 调用） 

### 五大核心能力

| 能力 | 说明 |
|------|------|
| **Planning（规划）** | 任务分解、保持焦点，通过 write_todos 等工具将复杂任务分解为离散步骤  |
| **Sub-Agents（子代理）** | 上下文隔离、并行执行、Token 效率（只返回高度综合结果），架构收敛为 Main-Agent + 按需 Sub-Agent  |
| **File System（文件系统）** | 上下文卸载、共享工作区、长期记忆，防止上下文窗口溢出  |
| **Long-term Memory（长期记忆）** | 跨会话记忆、经验积累，使 Agent 能够在多次运行中积累上下文  |
| **System Prompt（系统提示）** | 详细指导、示例学习、复杂性承载，最优秀的 deep research 拥有非常复杂和详细的系统提示  |

### 技术形态收敛（2025 年 9 月后）

以 **Claude Agent SDK**（2025-09-29 发布）和 **LangChain Deep Agent** 为代表的架构特点 ：
- **Main-Sub Agent 主从架构**
- **自主规划（Planning）能力**
- **独立文件系统**
- **上下文自动压缩**：上下文 Token 达到阈值时（Claude Agent SDK 默认 100,000 tokens），自动调用总结模型压缩 

### 分层工具调用

三层分层设计缓解上下文拥挤 ：
1. **原子层（Atomic Layer）**：~20 个核心工具（read file, edit file, bash, task 等）
2. **沙箱工具层（Sandbox Utilities）**：直接用 bash 调用预装程序，不再封装 Function Call
3. **代码/包层（Code/Packages）**：让 Agent 编写 Python 脚本一次性执行复杂串行逻辑

### 垂直业务适配

1. **业务知识技能化 (Skills via File System)**：将 SOP 抽象为 Skills，按需动态加载
2. **业务接口 MCP 化**：将企业 API 封装为 MCP 服务，按需连接调用
3. **提示词精细化**：分别针对 Main Agent 和 Sub Agent 编写详细的 System Prompt

## 关联

- 相关概念: [Agentic RAG](/rag/concept-agentic-rag), [MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp), [Agent 自主规划 — 五大架构模式](/agent/concept-agent-planning)
- 相关实体: [OpenClaw](/inference-deploy/product-openclaw), [Hermes](/inference-deploy/product-hermes)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — Deep Agent 定义、五大核心能力、技术形态收敛、分层工具调用

## 变更记录

- 2026-05-27: 初始创建
