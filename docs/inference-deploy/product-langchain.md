---
title: "LangChain"
outline: deep
---

# LangChain

> **类型**: entity
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: , 

## 摘要
LangChain 是全能型 LLM 应用开发框架，提供六大核心组件（Models、Prompts、Memory、Indexes、Chains、Agents），支持 LCEL 管道语法、Agent 工具链与 ReAct 模式，用于多任务应用开发。

## 详情

### 基本定位
- **定位**：**全能型 LLM 应用开发框架** 
- **GitHub**：github.com/langchain-ai/langchain 
- **生态**：**100+ 模型、50+ 向量数据库、大量预置工具** 

### 六大核心组件
| 组件 | 说明 |
|------|------|
| **LLM / ChatModel** | 大语言模型封装，LLM 用于文本补全，ChatModel 用于对话（支持 tool calling） |
| **Prompt Template** | 提示词模板，支持变量替换  |
| **Chain** | 将多个组件串联（如 `prompt | llm`） |
| **Agent** | 智能代理，自主决策调用哪些工具  |
| **Tools** | 工具集（搜索、计算、数据库查询等） |
| **Memory** | 保存对话历史，实现多轮对话  |

### LangChain 1.0 结构性变化
| 变化 | 说明 |
|------|------|
| **包结构重构** | `langchain-core`（基类+LCEL）、`langchain-community`（社区集成）、独立合作方包（`langchain-openai`、`langchain-anthropic`） |
| **新增子项目** | **LangGraph**（图编排工作流）、**LangServe**（一键封装 REST API）、**LangSmith**（可视化调试+监控） |
| **API 转向 LCEL** | 用 `|` 管道符拼 Runnable，不再继承 Chain 基类  |

### LCEL 管道语法
- LangChain Expression Language (LCEL) 使用 `|` 管道符连接组件 
- 优势：
  - **统一的调用接口**：`invoke()`、`stream()`、`batch()`、`ainvoke()` 
  - **支持流式输出**：`.stream()` 方法边生成边消费 
  - **支持并行**：`{"x": A, "y": B}` 并行执行 A 和 B 
  - **支持异步**：原生 `async/await` 支持 

### Chain Types（问答链类型）
在 RAG 场景中使用 `load_qa_chain` 时，有 4 种 chain_type：

| Chain Type | 说明 | 适用场景 |
|------------|------|---------|
| **stuff** | 直接把文档作为 prompt 输入 | 文档拆分的比较小，一次获取文档比较少，优先使用  |
| **map_reduce** | 每个 chunk 单独处理再合并 | 可并发，但缺少上下文  |
| **refine** | 在第一个 chunk 上处理，合并下一个 | 部分保留上下文，控制 token  |
| **map_rerank** | 每个 chunk 打分，返回最好的 | 大量调用 LLM，独立处理  |

**选择建议**：能使用 `stuff` 的就使用这种方式（调用 LLM 次数少）

### Memory 记忆管理
四种短期记忆方式：

| 方式 | 策略 | 特点 |
|------|------|------|
| **BufferMemory** | 存储所有对话历史 | 完整但 Token 消耗大  |
| **BufferWindowMemory** | 只保留最近 K 组对话 | 滑动窗口，控制 Token  |
| **ConversationSummaryMemory** | 对对话进行摘要 | 压缩历史，适合长对话  |
| **VectorStore Memory** | 向量存储 + 相似度匹配 | 按语义匹配最相关 K 组对话  |

### ReAct 模式
- **ReAct** = Reasoning + Acting，将推理和动作相结合 
- 循环：**Thought → Action → Observation → ... → Final Answer** 

### Agent vs LCEL 选择
| 维度 | LCEL 任务链 | Agent 模式 |
|------|------------|-----------|
| 流程控制 | 开发者显式指定每步 | LLM 自主决策  |
| 适用场景 | 自定义流程、可控组合 | 智能决策 + 多工具自动调度 |

## 关联
- 相关概念: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development), [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development), [RAG（检索增强生成）](/rag/concept-rag), [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development), [LangChain 问答链类型（Chain Types）](/agent/concept-langchain-chain-types)
- 相关实体: [FAISS](/inference-deploy/product-faiss)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源
- [1]  — RAG 基础与应用（LangChain 问答链类型、load_qa_chain、stuff 策略、RAG 三阶段流程）
- [2]  — LangChain：多任务应用开发（六大组件、LCEL 管道语法、Agent 与工具链、Memory 管理、ReAct 模式、实战案例）

## 变更记录
- 2026-05-26: 初始创建，来源 , 
