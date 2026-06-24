---
title: "Agent 能力优化与效果评估"
outline: deep
---

# Agent 能力优化与效果评估

> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-05-26
> **最后更新**: 2026-05-26
> **来源**: 
> **领域**: ai

## 摘要

Agent 上线前需要系统评估其效果，核心关注**回答完整性、幻觉检测、内容安全、响应延迟和 Token 成本** 。主要评估工具有 LangSmith（调试观测）、OpenEvals（开源评估器）、DeepEval（CI/CD 质检）、LangFuse（开源可观测性平台），各自定位互补 。

## 详情

### Agent 效果评估核心问题

| 问题                 | 说明                                     |
| ------------------ | -------------------------------------- |
| Agent 是否正确选择了处理模式？ | 选择正确的 Agent 架构：反应式、深思熟虑式、ReAct、PER、自进化 |
| 回答是否完整？            | 是否包含期望的关键信息                            |
| 是否有幻觉？             | 是否生成了虚假信息                              |
| 是否有害内容？            | 内容安全合规                                 |
| 响应是否及时？            | 延迟、Token 消耗、成本                         |


**企业 RAG 上线要求**：速度快（3-5 秒内开始出结果），准确率高（客服辅助场景要求 99.9% 以上，可以不回答但不能出错）。

### LangSmith — 调试观测平台

LangSmith 是 LangChain 官方提供的 **LLM 应用观测、调试、测试与评估平台** 。

| 功能        | 说明                             |
| --------- | ------------------------------ |
| **调试与追踪** | 实时追踪每个 LLM 调用、工具使用和 Agent 决策过程 |
| **性能监控**  | 监控响应时间、Token 使用量、成本等关键指标       |
| **测试与评估** | 创建测试数据集，评估模型输出质量               |
| **数据分析**  | 分析用户查询模式、错误率、成功率等              |


**核心功能**：
- **Trace 视图**：每个节点的输入和输出、LLM 的完整 Prompt 和响应、工具调用的参数和结果 
- **Waterfall 瀑布图**：每一步的耗时，找出"卡点"，区分串行/并行步骤 
- **从 Trace 添加测试样本**：将当前 Trace 保存为带输入/输出参考答案的样本，挂到 Dataset 里用于批量回归测试 

**RunnableConfig 的作用** ：
| 字段         | 用途                             |
| ---------- | ------------------------------ |
| `tags`     | 为每次运行打标签，方便在 LangSmith 后台筛选、分组 |
| `metadata` | 附加业务上下文（用户ID、风险偏好等）            |
| `run_name` | 命名本次运行，便于在 Trace 列表中快速识别       |

**Prompt Ops（提示工程运维）**：一种**工程化方法**，用于系统地管理、测试、优化和监控 LLM 应用中的提示，确保提示的质量和一致性，实现持续改进 。

核心循环：改 Prompt → 跑评估 → 看数据 → 再改 Prompt 。

### OpenEvals — 开源评估器库

OpenEvals 是 LangChain 团队开发的**开源评估器库**，`pip install openevals` 。

**11 种内置评估器** ：

| #   | 评估器                     | 功能        | 使用场景         |
| --- | ----------------------- | --------- | ------------ |
| 1   | Correctness             | 正确性评估     | 验证答案正确性      |
| 2   | Conciseness             | 简洁性评估     | 评估回答简洁度      |
| 3   | Answer Relevance        | 相关性评估     | 评估回答相关性      |
| 4   | RAG Helpfulness         | RAG 帮助性   | RAG 系统评估     |
| 5   | RAG Groundedness        | RAG 基础性   | 验证基于检索内容     |
| 6   | RAG Retrieval Relevance | RAG 检索相关性 | 评估检索质量       |
| 7   | Toxicity                | 毒性/有害性    | 内容安全检测       |
| 8   | Hallucination           | 幻觉检测      | 检测无根据声明      |
| 9   | Code Correctness        | 代码正确性     | 代码评估         |
| 10  | Code Correctness w/ Ref | 带参考的代码评估  | 有标准答案的代码评估   |
| 11  | Plan Adherence          | 计划遵循度     | Agent 计划执行评估 |

### DeepEval — CI/CD 质检门禁

DeepEval 是一个**开源的 LLM 评估框架**，类似于传统软件开发中的 Pytest/JUnit 。

- 内置 **50+ 评估指标**，覆盖 RAG、Agent、对话等场景 
- 类似软件开发里的单元测试，负责在上线前给模型打分 

### LangFuse — 开源可观测性平台

LangFuse 是一个**开源的 LLM 工程平台**，定位是"可观测性 + 调试 + 评估"三合一的 LLMOps 工具 。

- 全开源，任何框架/模型都能接入 
- 与 LangSmith 对比：LangFuse 全开源、框架无关；LangSmith 是 LangChain 官方商业产品，深度耦合 LangChain 生态 

### 四大工具对比

| 维度         | DeepEval          | LangSmith                    |
| ---------- | ----------------- | ---------------------------- |
| **传统软件类比** | Pytest / JUnit    | Datadog / Sentry             |
| **核心作用**   | 跑分测试              | 调试观测                         |
| **场景**     | 离线、CI/CD 流水线、回归测试 | 在线、链路追踪、Debug、成本分析、Prompt 管理 |


| 维度                 | OpenEvals         | DeepEval                          |
| ------------------ | ----------------- | --------------------------------- |
| **定位**             | LangChain 生态的亲儿子  | 独立的开源评估框架                         |
| **指标丰富度**          | 核心指标为主            | 胜出（实现了 RAGAS、Helm、MT-bench 等论文指标） |
| **自定义体验**          | 自定义 Prompt + create_llm_as_judge，简单直接 | G-Eval 语法糖，写起来最短                  |
| **与 LangSmith 集成** | 一条命令即可在实验中调用      | 需要手动封装                            |


**工具选择建议** ：
- **LangChain / LangSmith 用户**：优先选 OpenEvals
- **需要丰富指标**：DeepEval 胜出
- **需要观测与调试**：LangSmith 不可替代
- **完整方案**：LangSmith（观测）+ OpenEvals/DeepEval（评估）

**DeepEval 和 LangSmith 可以协同工作**：DeepEval 负责上线前的质量把关，LangSmith 负责上线后的监控和调试 。

### 自动化测试流程

```
检查环境（API Key）
    ↓
准备测试数据集
    ↓
执行评估（调用 LangSmith evaluate()）
    ↓
结果展示（提供 LangSmith 界面链接查看）
```


**评估器类型**：
1. **ProcessingModeEvaluator**：评估 Agent 是否正确选择了处理模式（反应式 vs 深思熟虑），返回 0.0 或 1.0 
2. **ResponseCompletenessEvaluator**：评估响应是否包含期望的关键信息，按包含的关键词比例给出 0-1 分数 

### Qwen-Agent 与 LangChain 对比

| 特性         | LangChain/LangGraph | Qwen-Agent     |
| ---------- | ------------------- | -------------- |
| **学习曲线**   | 陡峭（2-3 周）           | 平缓（3-5 天）      |
| **可控性**    | 高（精确控制）             | 中（框架控制）        |
| **可视化调试**  | ✅ LangSmith         | ❌              |
| **中文支持**   | 一般                  | ✅ 优化           |
| **代码量**    | 较多（需显式配置）         | 较少（约定优于配置）     |


## 关联
- 相关概念: [Agent 自主规划 — 五大架构模式](/agent/concept-agent-planning)、[AI 框架设计与选型](/inference-deploy/concept-ai-framework-selection)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源
- [1]  — LangSmith/OpenEvals/DeepEval/LangFuse 评估工具对比、自动化测试流程、Prompt Ops

## 变更记录
- 2026-05-26: 初始创建，来源 
