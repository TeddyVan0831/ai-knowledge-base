---
title: "AI 框架设计与选型"
outline: deep
---

# AI 框架设计与选型

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **领域**: ai

## 摘要

编写一个 AI Agent 框架，需要解决四个核心问题：**大脑适配层（LLM 统一接口与 Prompt 管理）、双手标准化（工具注册与调度）、记忆存储（Context 管理机制）、中枢编排（控制流设计）** 。四大主流框架 LangChain、LlamaIndex、Qwen-Agent、AutoGen 各有侧重，选型需根据业务场景决定 。

## 详情

### AI Agent 的四大核心问题

```
┌───────────────────────────────────────────────────┐
│                  AI Agent 核心问题                   │
├──────────────┬────────────────────────────────────┤
│ ① 大脑适配层  │ LLM 统一接口与 Prompt 管理           │
│ ② 双手标准化  │ 工具注册与调度 (Tool Registry)        │
│ ③ 记忆存储    │ Context 管理机制                     │
│ ④ 中枢编排    │ 控制流设计 (Orchestration)           │
└──────────────┴────────────────────────────────────┘
```


### 1. 大脑适配层：LLM 统一接口

框架做中间层，把统一指令翻译成特定模型的 API 调用 。

| 框架             | 封装方式                          | 特点                    |
| -------------- | ----------------------------- | --------------------- |
| **LangChain**  | `ChatTongyi` / `ChatOpenAI` 类 | 丰富的模型适配器，统一接口         |
| **Qwen-Agent** | `llm_cfg` 字典配置                | 配置式，支持多种 model_server |
| **LlamaIndex** | `DashScope` / `OpenAI` 类      | 与 `Settings` 全局配置结合   |


**统一接口的作用**：统一调用方式（`invoke("你好")`）、统一参数配置（temperature、top_p 等）、输出格式统一转为 Message 对象 。

### 2. 双手标准化：工具注册与调度

框架将 Python 函数的 name、docstring、type hints 转换为 JSON Schema 喂给 LLM 。

| 模式                   | 框架         | 特点                 |
| -------------------- | ---------- | ------------------ |
| `@tool` 装饰器          | LangChain  | 最简洁，docstring 自动解析 |
| `@register_tool` + 类 | Qwen-Agent | 显式参数定义，结构清晰        |
| `FunctionTool` 封装    | LlamaIndex | 强类型约束，适合复杂工具       |


### 3. 记忆管理机制

**为什么需要记忆管理**：LLM 是无状态的，记不住你说过什么，且 Context Window 是昂贵资源 → **有限注意力的管理** 。

三大框架记忆系统核心差异 ：

| 维度            | LangChain                      | Qwen-Agent                                      | LlamaIndex                      |
| ------------- | ------------------------------ | ----------------------------------------------- | ------------------------------- |
| 官方分层记忆架构      | 经典记忆组件 + 新版 LangGraph          | ❌ 无任何官方分层记忆设计                                   | ✅ 短期 FIFO + 三大 MemoryBlock 长期记忆 |
| 短期记忆能力        | 窗口截断 / 摘要，v1.0 主推 LangGraph 管控 | 仅依赖模型上下文窗口自动截断，无框架级记忆分层                         | FIFO 队列、Token 限流、自动冲刷至长期记忆      |
| 内置事实抽取        | ❌ 无，需自行开发                      | ❌ 无，仅有关键词生成                                     | ✅ 原生 FactExtractionMemoryBlock  |
| 原生向量 / 混合检索   | 需自行对接向量库                       | ✅ 内置 vector_search /hybrid_search（需额外依赖 + 手动开启） | ✅ 原生 VectorMemoryBlock 语义检索     |
| 对话持久化         | LangGraph Checkpointer 多存储自动落盘 | Memory 类不存对话；Server 层自动 JSON 落盘                 | 内置可持久化 SQLite / 远端库             |
| 会话隔离能力        | ✅ ThreadID+Checkpointer 强隔离    | ⚠️ 单实例隔离，GroupChat 全局共享                         | ✅ 会话索引天然隔离                      |
| 原生支持 .md 记忆文件 | ✅ 内置解析加载                       | ❌ 解析白名单不含 MD，传入静默跳过                             | ✅ 原生解析加载                        |
| 记忆自定义可插拔度     | 极高                             | 低，封装固化                                          | 高，模块化可插拔                        |


**记忆管理关键结论**：
1. 仅 **LangChain、LlamaIndex** 原生支持 `.md` 解析作为记忆 / 知识库；Qwen-Agent 官方白名单不支持 MD 
2. 三者中只有 **LlamaIndex 原生内置自动事实抽取** 
3. Qwen-Agent 有官方内置 `vector_search` / `hybrid_search` 检索能力，但**默认关闭、需装依赖 + 配 Key + 手动开启** 
4. LangChain 旧记忆组件可用但已标记废弃，新项目强制采用 LangGraph + Checkpointer 
5. 三大框架均**无内置一键导出会话记忆为 MD**，需开发者自定义封装 

### 4. 中枢编排：控制流设计

| 模式               | 说明                                       | 适用场景         |
| ---------------- | ---------------------------------------- | ------------ |
| **管道（Pipeline）** | LangChain的`prompt \| llm \| parser` 链式调用 | 线性处理流程       |
| **单人（Loop）**     | 经典 ReAct 循环：思考 → 行动 → 观察                 | 单 Agent 完成任务 |
| **多人接力（DAG）**    | 明确的执行顺序                                  | 流程化任务（如投资决策） |
| **多人圆桌（Chat）**   | 自由讨论                                     | 开放式协作        |


### 四大框架对比

| 维度          | LangChain                    | Qwen-Agent              | LlamaIndex       | AutoGen          |
| ----------- | ---------------------------- | ----------------------- | ---------------- | ---------------- |
| **核心定位**    | 全能型框架                        | 轻量工具调用                  | RAG 数据接口         | 多 Agent 协作       |
| **工具注册**    | `@tool` 装饰器                  | `@register_tool`        | `FunctionTool` 类 | `@register` 装饰器  |
| **RAG 支持**  | 需集成 VectorStore              | 基础文件读取                  | **专业级向量索引**      | 需自行集成            |
| **多 Agent** | LangGraph 支持                 | 基础支持                    | 需自行编排            | **原生 GroupChat** |
| **代码执行**    | 需集成                          | **内置 code_interpreter** | 需集成              | UserProxyAgent   |
| **学习曲线**    | 中等                           | **简单**                  | 中等               | 中等               |
| **生态完整度**   | **最丰富**                      | 阿里生态                    | RAG 社区           | 微软生态             |


### 业务场景选型决策

| 场景              | 推荐                            | 理由                                        |
| --------------- | ----------------------------- | ----------------------------------------- |
| **企业知识库问答**     | LlamaIndex                    | 专业文档处理 + 多种检索策略 + 索引持久化                   |
| **快速 Demo/POC** | Qwen-Agent                    | 配置最简单 + 内置 WebUI + 开箱即用的 code_interpreter |
| **通用 AI 应用**    | LangChain                     | 灵活控制流程 + 丰富生态 + 支持多种模型                    |
| **多 Agent 协作**  | AutoGen                       | 多智能体对话 + 角色自定义 + 群聊管理                     |
| **数据分析 + 绘图**   | Qwen-Agent                    | 内置 code_interpreter 沙箱                    |
| **超长文档处理**      | Qwen-Agent                    | Qwen 模型 1M Context 优势                     |
| **复杂工作流编排**     | LangChain + LangGraph         | LCEL + 图编排                                |
| **企业私有化部署**     | Dify / Qwen-Agent / LangChain | 开源 + 可私有部署                                |


**选型口诀**：知识库选 LlamaIndex、快 Demo 选 Qwen-Agent、复杂流程选 LangChain、多 Agent 选 AutoGen 。

### AutoGen 多智能体框架

微软开源的多智能体对话框架，用于构建多个 AI Agent 协作完成复杂任务 。

核心理念：让 Agent 之间通过**自然语言对话**协作，而非硬编码的函数调用 。

> ⚠️ **重要变更**：2025 年 10 月起，微软将 AutoGen 置为维护模式。所有新特性都做到 **Agent Framework** 上（下一代 Semantic Kernel + AutoGen）。

**发言者选择策略** ：
| 策略            | 说明         | 适用场景                 |
| ------------- | ---------- | -------------------- |
| `round_robin` | 按列表顺序轮流发言  | 流程明确的任务（数据→分析→风控→决策） |
| `random`      | 随机选择       | 头脑风暴、创意讨论            |
| `auto`        | LLM 判断谁最适合 | 开放式讨论、问答场景           |
| 自定义函数         | 完全控制选择逻辑   | 复杂业务流程、条件分支          |

## 关联
- 相关概念: [Agent 自主规划 — 五大架构模式](/agent/concept-agent-planning)、[Function Calling — 模型的"手指"](/agent/concept-function-calling)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源
- [1]  — 四大核心问题、四大框架对比、记忆管理系统对比、AutoGen 多智能体、选型决策

## 变更记录
- 2026-05-26: 初始创建，来源 
