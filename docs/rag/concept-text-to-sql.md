---
title: "Text-to-SQL 与数据智能"
outline: deep
---

# Text-to-SQL 与数据智能

> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 

## 摘要

Text-to-SQL（文本转 SQL）将自然语言问题自动转换为结构化的 SQL 查询语句，让不懂 SQL 的业务人员也能灵活查询数据库。技术演进经历了人工规则模板、Seq2Seq 机器学习、到大语言模型 + 提示工程/微调三个阶段。当前最佳实践是 LLM + RAG 架构，Vanna 是开源的 Text-to-SQL RAG 框架。

## 详情

### 一、Text-to-SQL 定义与技术演进

**Text-to-SQL**：将自然语言问题自动转换为结构化的 SQL 查询语句，让用户更直观地与数据库交互 。

**技术演变的三个阶段**：
| 阶段 | 技术方法 | 特点 |
|------|----------|------|
| 早期阶段 | 人工编写规则模板 | 基于规则匹配自然语言与 SQL 之间的对应关系 |
| 机器学习阶段 | Seq2Seq 等模型 | 用序列到序列模型学习自然语言和 SQL 的映射关系 |
| LLM 阶段 | 大语言模型 + 提示工程/微调 | 借助 LLM 的语言理解和代码生成能力，将 Text-to-SQL 性能提升到新高度 |



### 二、LLM 阶段系统流程

基于 LLM 的 Text-to-SQL 系统包含以下步骤：
1. **自然语言理解**：分析用户输入的自然语言问题，理解其意图和语义 
2. **模式链接（Schema Linking）**：将问题中的实体与数据库模式中的表和列进行链接 
3. **SQL 生成**：根据理解的语义和模式链接结果，生成相应的 SQL 查询语句 
4. **SQL 执行**：在数据库上执行 SQL 查询，将结果返回给用户 

### 三、LLM 模型选择

**闭源模型（商用级）**：
| 模型 | 发布方/时间 | 核心特点 | Text2SQL 表现 |
|------|-------------|----------|---------------|
| GPT-5.4 / GPT-5 | OpenAI 2026.03 | 272K-1M 上下文，Pro 版本支持深度推理 | 复杂 Schema 理解显著优于前代 |
| Claude Sonnet 4.6 / Opus 4.6 | Anthropic 2026.02 | 1M 上下文（beta），自适应推理深度 | Sonnet 4.6 为性价比最优选 |
| Gemini 3.1 Pro / Flash-Lite | Google 2026.02/2026.03 | 1M 上下文，多模态输入 | Flash-Lite 版价格低至 $0.25/M Tok |
| Qwen 3.6 Plus | 阿里 2026.04 | 100 万 token，混合架构，Agent 编程能力显著增强 | 长 Schema 处理首选，OpenRouter 免费预览，定价约为 Claude 的 1/17 |



**开源模型（本地部署）**：
| 模型 | 发布方/时间 | 架构 | 核心特点 |
|------|-------------|------|----------|
| DeepSeek-V4 Pro / V4 Flash | 2026.04 | 1.6T 总参数（MoE） | V4 Pro 为旗舰版，支持百万字超长上下文；V4 Flash 为极速版。Agent 能力暴力重构，完全基于华为昇腾芯片训练，MIT 协议全量开源 |
| Qwen3 / Qwen3-Coder-Next | 阿里 2025.04/2026.02 | 235B-A22B（22B 激活）/ 80B-Coder（仅 3B 激活），MoE | 256K-1M 上下文，Apache 2.0 协议；Coder-Next 在 SWE-bench Verified 达 70.6%，仅需 46GB 显存可本地部署 |



**选型建议**：优先用 Qwen 3.6 Plus（长 Schema 处理首选，性价比高）；本地部署推荐 Qwen3-Coder-Next（低显存、高能力）。

### 四、SQL Copilot 搭建方案

**两种方案对比**：
| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| LangChain SQLDatabase | 使用方便，自动连接数据库获取 metadata | 执行不灵活，需多次判断哪个表适合；复杂查询通过率低 | 快速原型、简单查询场景 |
| 自己编写（LLM + Prompt） | 重心在 RAG 提供上，准确性高，配置灵活 | 需要设置的规则多，开发成本高 | 复杂查询、生产环境 |



**本质**：LLM + RAG。RAG 可分两部分：向量数据库检索 + 固定文件（如本地数据表说明）。

### 五、Vanna 框架

**Vanna** 是开源的 RAG 框架，专注于将自然语言转换为 SQL 查询（Text-to-SQL），并支持与数据库交互。MIT 许可证，提供完整 Python 库 。

**当前版本**：PyPI 最新版本为 v2.0.2。v2.0 重构了整体架构（Agent-based），原有的 `vanna.base.VannaBase` 等 legacy API 被移至 `vanna.legacy` 目录下 。

**Vanna 特点**：
| 特点 | 说明 |
|------|------|
| 开源与可定制化 | 提供完整 Python 库（MIT 许可证），支持本地化部署，可自定义 LLM、向量数据库和关系型数据库 |
| RAG 增强的准确性 | 通过 DDL 语句、表注释、示例 SQL 等训练模型，显著提升复杂查询准确率 |
| 多场景支持 | 企业数据分析、智能客服、电商搜索、金融报告生成等 |
| 灵活的基础设施 | 支持多种 LLM、向量数据库和关系型数据库，可插拔设计 |



**Vanna 工作原理**：
```
用户问题 → 向量检索(DDL/Doc/SQL) → 组装 Prompt → LLM 生成 SQL → 执行 SQL → 返回 DataFrame + Plotly 图表
```


**训练阶段**：把数据库的元数据写入向量库，作为后续检索的知识库：
| 数据类型 | 用途 | 示例 |
|----------|------|------|
| DDL | 建表语句，告诉模型表结构与字段含义 | `CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100))` |
| Documentation | 业务文档、字段口径、术语解释 | "users 表存储 C 端注册用户，name 为脱敏昵称" |
| Question-SQL pairs | 高质量的问题-SQL 示例（few-shot 样本） | `{"q": "用户总数？", "sql": "SELECT COUNT(*) FROM users"}` |



**核心 API（legacy VannaBase 类）**：
| API | 作用 | 说明 |
|-----|------|------|
| `ask()` | 一站式查询入口 | 依次调用 generate_sql → run_sql → generate_plotly_code → get_plotly_figure → generate_followup_questions |
| `generate_sql()` | 生成 SQL 字符串（不执行） | 先检索相似 DDL/Doc/SQL → 组装 prompt → LLM 生成 SQL |
| `run_sql()` | 执行 SQL 语句 | 将生成的 SQL 发送到数据库，返回查询结果 |
| `train()` | 训练（写入向量库） | 支持三种训练方式 |
| `generate_followup_questions()` | 智能追问 | 根据当前结果，建议下一步追问 |
| `generate_summary()` | 结果摘要 | 用自然语言总结查询结果 |



**Vanna 配置项**：
| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `n_results_ddl` | 每次召回多少条 DDL 进 prompt | 10 |
| `n_results_sql` | 每次召回多少条 Question-SQL 对 | 10 |
| `n_results_documentation` | 每次召回多少条文档 | 10 |
| `language` | 输出语言（如 'Chinese'） | None（英文） |



**常见问题**：
- **表名是 SQL 关键字**：表名用反引号包起来，如 `SHOW CREATE TABLE \`using\`` 
- **相关表没被召回**：默认 `n_results_ddl=10`，库里表多时关键表可能进不到 prompt。修复方法：加大 `n_results_ddl` 到 30，或用 documentation 给关键表加业务描述 

### 六、提高 Text-to-SQL 准确率的关键

1. **提供完整的 Schema 信息**：DDL 建表语句必须完整 
2. **丰富训练数据**：DDL + Documentation + Question-SQL pairs 三者缺一不可 
3. **优化 Prompt 格式**：语言标记 + 建表语句 + SQL 代码块标记在末尾 
4. **控制召回质量**：设置相似度阈值，优化 few-shot 多样性 
5. **解决召回问题**：加大 `n_results_ddl` 或使用 documentation 间接召回关键表 

**Prompt 编写 3 大原则**：
1. 说明语言类型：`-- language: SQL` 告诉模型要生成 SQL 代码 
2. 包含建表语句：LLM 通过 CREATE TABLE 语句识别表结构和字段含义 
3. SQL 标记放在最后：用 ````sql` 包裹，放在 prompt 末尾，让模型直接续写 
4. 首尾最重要：Prompt 中的首尾部分对 LLM 的影响最大 

## 关联

- 相关概念: [RAG（检索增强生成）](/rag/concept-rag) — RAG 检索增强生成（Vanna 框架核心依赖）
- 参见: [AI 部署与运维主题综述](/inference-deploy/topic-ai-deployment-ops) — AI 部署与运维主题综述

## 引用来源

- [1]  — Text-to-SQL 技术演进、SQL Copilot 搭建、Vanna 框架实战与业务分析场景

## 变更记录

- 2026-05-26: 初始创建，来源 
