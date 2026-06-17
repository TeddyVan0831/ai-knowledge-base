---
title: "MCP（Model Context Protocol）— 模型上下文协议"
outline: deep
---

# MCP（Model Context Protocol）— 模型上下文协议

> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-06-10
> **来源**: , 

## 摘要

MCP（Model Context Protocol，模型上下文协议）由 **Anthropic** 于 **2024 年 11 月**推出，是 Agent 与工具之间的标准化互操作协议——解决"N×M 集成问题"，通过 Host/Client/Server 架构实现工具的可发现性、安全性和跨平台互操作 。通俗理解：MCP 是 **"AI 领域的 USB-C 接口"** 。

## 详情

### N×M 集成问题

在没有标准协议的情况下，n 个 Agent 需要与 m 个工具建立 n×m 个独立连接。MCP 通过标准化接口将问题简化为 n+m 。

### 核心架构

MCP 采用 **客户端-服务器（Client-Server）架构** ：

| 组件             | 说明                            | 示例                                      |
| -------------- | ----------------------------- | --------------------------------------- |
| **MCP Host**   | 运行 AI 模型的环境（Agent 应用）         | Claude Desktop、Cursor IDE、Cherry Studio |
| **MCP Client** | 嵌入在 Host 中，负责发起请求并与 Server 通信 | Host 内置组件                               |
| **MCP Server** | 轻量级服务，提供特定功能供 AI 调用           | 高德地图 Server、Tavily 搜索 Server            |



### 通信层

基于 JSON-RPC 的消息协议，支持多种传输方式（stdio、HTTP SSE 等）。消息类型包括请求、响应、通知和错误 。

### 关键原语

| 原语 | 说明 |
|------|------|
| **Tools（工具调用）** | Agent 可调用的能力，包含定义、参数 schema、返回结果。允许 AI 执行外部操作，如发邮件、查地图、调 API |
| **Resources（知识扩展）** | 提供结构化数据以增强 AI 的上下文理解，如数据库、文档 |
| **Prompts（提示模板）** | 预定义的指令模板，优化任务执行 |
| **Sampling（采样）** | Server 请求 Host 的 LLM 生成特定结构化的响应数据，用于辅助 Server 决策 |
| **Elicitation（用户输入）** | Server 请求用户输入 |
| **Roots（文件系统根目录）** | 定义文件系统根目录，限制 Agent 访问范围 |

基于  和 

### 工具设计最佳实践

在 MCP 中设计工具应遵循以下原则 ：

- **文档至关重要**：工具名称、描述、参数说明均需清晰，使用人类可读的名称（如 `create_critical_bug_in_jira_with_priority` > `update_jira`）
- **描述行为而非实现**：告诉 Agent 工具做什么（"创建 bug 描述问题"），而非怎么做（"调用 create_bug 工具"）。避免在提示词中重复工具文档 
- **职责单一**：每个工具做一件事并做好，保持细粒度 
- **设计简洁输出**：避免返回大量数据消耗上下文窗口，减少对对话历史的影响 
- **有效使用验证**：利用 schema 验证工具输入输出，既是文档又是运行时校验 
- **提供描述性错误信息**：帮助 Agent 理解失败原因并自我修正 
- **指定默认值**：为关键参数提供默认值并充分文档化 

### 战略优势 vs 风险

**优势**：加速开发、可复用生态、动态增强 Agent 能力、架构灵活性、治理基础 

**风险**：性能瓶颈（上下文膨胀）、企业就绪性差距（缺乏原生可观测性）、安全挑战（Context 注入、Confused Deputy 问题）

### MCP 与 Function Calling、Skill 的关系

```
能力层 (Capability)
    └── Function Calling: 模型理解"什么时候该调什么函数"。

封装层 (Encapsulation)
    └── Skill: 把函数、Prompt、业务逻辑打包成"技能包"，方便 Agent 调用。

协议层 (Protocol)
    └── MCP: 统一插头标准。让 Skill 和工具能在不同厂商的模型间无缝流动。
```


### 实战案例：高德地图 MCP 旅游攻略

**配置方式**（Cursor 中编辑 `mcp.json`）：
```json
{
  "mcpServers": {
    "amap-maps": {
      "command": "npx",
      "args": ["-y", "@amap/amap-maps-mcp-server"],
      "env": { "AMAP_MAPS_API_KEY": "你的API KEY" }
    }
  }
}
```

**实际使用效果**：在 Cursor 的 Agent 模式下输入"用高德 MCP，做上海一天旅游攻略"，AI 会自动 ：
1. 调用 `maps_text_search` 搜索上海景点（外滩、东方明珠、豫园等）
2. 调用 `maps_search_detail` 获取景点详细信息（地址、门票、开放时间）
3. 调用天气查询获取当日天气
4. 调用路径规划获取步行/驾车路线
5. 综合以上信息，生成完整的一日游攻略

**关键洞察**：LLM 会**自主选择**合适的 MCP 工具进行调用，无需手动指定 。

### 实战案例：Tavily 搜索 MCP

Tavily 提供两大核心工具 ：

**`tavily-search` — 实时网络搜索** ：
- `query`：搜索关键词（必填）
- `max_results`：返回结果条数（默认 3-10）
- `search_depth`：`basic` / `advanced`（advanced 会抓取并总结页面正文）
- `include_domains` / `exclude_domains`：限定/排除域名
- `time_range`：时间过滤 `day` / `week` / `month`
- `include_answer`：是否直接返回答案
- `include_raw_content`：是否携带原始 HTML

**`tavily-extract` — 网页内容智能提取** ：
- `urls`：要提取的页面地址（必填）
- `extract_depth`：`basic` / `advanced`（advanced 解析更多细节并过滤噪音）
- `format`：`text` / `markdown` / `json`（默认 text）
- `include_images`：是否同时提取图片链接

## 关联
- 相关概念: [Function Calling — 模型的"手指"](/agent/concept-function-calling)、[Agent 自主规划 — 五大架构模式](/agent/concept-agent-planning)、[工具使用（Tool Use / Function Calling）](/agent/concept-tool-use)、[智能体间通信（A2A Communication）](/agent/concept-a2a-communication)、[Agent 互操作性（A2A）](/agent/concept-agent-interoperability)（Agent 互操作性与 A2A 协议）、[AI API 端点协议](/tools-ecosystem/concept-ai-api-protocols)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)、[AI 经典论文汇览](/tools-ecosystem/topic-ai-classic-papers)

## 引用来源
- [1]  — MCP 定义、架构、三大核心能力、高德/Tavily 实战案例、与 Function Calling/Skill 的关系
- [2]  — N×M 集成问题、JSON-RPC 通信、6 原语、工具设计最佳实践、战略优势与风险

## 变更记录
- 2026-05-26: 初始创建，来源 
- 2026-06-10: 合并 [MCP 协议（已合并）](/base-models/concept-mcp-protocol) 的 N×M 集成、JSON-RPC 通信、工具设计最佳实践、战略风险分析等深度内容，来源 
