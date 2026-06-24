---
title: "工具使用（Tool Use / Function Calling）"
outline: deep
---

# 工具使用（Tool Use / Function Calling）

> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-31
> **最后更新**: 2026-05-31
> **来源**: 
> **领域**: ai

## 摘要

工具使用模式让智能体能够自主选择和调用外部工具（API、数据库、搜索引擎等）来扩展自身能力边界——从"只会说话"升级为"能做实事"。

## 详情

### 模式概述

工具使用的核心是**能力扩展**——智能体根据任务需求自主判断需要调用什么工具、如何构造参数，并处理工具的返回结果 。

**工具调用流程**：
1. **意图识别**：判断是否需要调用工具
2. **工具选择**：从可用工具集中选择最合适的
3. **参数构造**：根据工具 schema 构造正确的参数
4. **执行与处理**：调用工具并处理返回结果

### 实践应用

- **信息检索**：调用搜索引擎、数据库 API 获取实时数据
- **代码执行**：调用代码解释器执行 Python/SQL 等
- **外部服务**：调用天气 API、地图 API、翻译 API 等

### 关键要点

- 工具描述（docstring）的质量直接影响 LLM 的调用准确率
- 工具数量需要控制——太多工具增加选择难度，太少限制能力
- 需要处理**工具调用失败**的场景（参考异常处理模式）

## 关联

- 相关概念: [Function Calling — 模型的"手指"](/agent/concept-function-calling), [MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp), [Agent：从可控性到自主反思](/agent/concept-agent-controllability), [Agent 自主规划 — 五大架构模式](/agent/concept-agent-planning)
- 参见: [Agent 设计模式](/agent/topic-agentic-design-patterns), [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — 第 5 章：工具使用模式概述、LangChain/CrewAI/ADK 代码示例

## 变更记录

- 2026-05-31: 初始创建，来源 Agentic Design Patterns 电子书第 5 章
