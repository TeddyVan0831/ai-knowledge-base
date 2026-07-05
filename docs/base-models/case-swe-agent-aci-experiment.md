---
title: "SWE-agent ACI 接口实验案例"
outline: deep
---

# SWE-agent ACI 接口实验案例

> **类型**: entity
> **创建时间**: 2026-07-05
> **最后更新**: 2026-07-05
> **来源**:  第 9 章
> **领域**: ai

## 摘要

John Yang 等 NeurIPS 2024 论文 *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*。**研究问题**：在不修改模型权重的情况下，给 Agent 设计不同的文件查看、搜索、编辑、反馈和上下文接口（ACI = Agent-Computer Interface），会不会改变软件修复表现？**关键结论**：在模型与任务集相同的情况下，**行动接口、反馈格式、上下文窗口和确定性检查会实质改变 Agent 的可实现能力**（自定义 ACI vs Shell-only：解决率 18.0% vs 11.0%，相对提升约 64%）。

## 详情

### 一、实验设置

| 维度 | 设置 |
|------|------|
| 模型 | GPT-4 Turbo（同一模型）|
| Benchmark | SWE-bench Lite 300 个真实 GitHub Issue |
| 控制变量 | 同一模型、同一 benchmark |
| 改变因素 | 编辑/搜索接口、视图大小、Lint、历史管理 |

### 二、核心实验数据

#### 整体解决率

| 方案 | 解决率 | 相对提升 |
|------|--------|---------|
| 自定义 ACI | **18.0%** | +64% |
| Shell-only | **11.0%** | baseline |
| SWE-bench 整体 pass@1 | 12.5% | — |

> ⚠️ 数据差异：论文摘要中 SWE-bench 整体 pass@1 为 12.5%；本笔记 18.0%/11.0% 来自课堂讲义与讲师口述，具体绝对值以论文正文为准。

#### 消融实验

| 消融项 | 解决率 | 变化 |
|--------|--------|------|
| 完整自定义 ACI | 18.0% | baseline |
| 移除专用编辑器 | **10.3%** | -7.7pp |
| 保留编辑器但去掉 Lint 阻断 | 15.0% | -3.0pp |
| 文件视图从 100 行改完整文件 | 12.7% | -5.3pp |
| "最近 5 个观察" → 完整历史 | 15.0% | -3.0pp |

### 三、关键启示

1. **接口设计是 Harness 的一部分**：ACI 设计直接影响任务表现，不需要修改模型权重
2. **确定性检查（Lint）有效**：去掉 Lint 阻断后解决率从 18.0% 降到 15.0%（-3.0pp），证明自动检查机制可减少错误累积
3. **上下文窗口策略关键**：完整文件视图反而不如 100 行窗口（噪声淹没关键信息）
4. **历史管理也重要**：完整历史不如"最近 5 个观察"（信息过载）

### 四、对 Harness 设计的指导

| 设计原则 | SWE-agent 经验 |
|---------|---------------|
| 提供专用工具接口 | 不要让 Agent 自己用通用 Shell 处理一切 |
| 内置确定性检查 | Lint 阻断比 Prompt 要求更有效 |
| 限制上下文窗口 | 适度窗口比完整历史表现更好 |
| 保持简洁历史 | "最近 5 个观察"比完整历史更聚焦 |

## 关联

- 相关概念: [Harness Engineering（harness 工程）](/base-models/concept-harness-engineering), [concept-agent-loop](/base-models/concept-agent-loop)
- 主题: [topic-agent-architecture-2026](/base-models/topic-agent-architecture-2026)
- 配套资料: 
- 相关案例: [Anthropic 长任务 Harness 案例（Opus 4.5）](/base-models/case-anthropic-long-running-agent), [OpenAI Agent-first 仓库案例](/base-models/case-openai-agent-first-warehouse)

## 引用来源

- [1]  — 第 9.1 节 SWE-agent 观察
- [2] John Yang et al. NeurIPS 2024 *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*

## 变更记录

- 2026-07-05: 初始创建，来源  第 9 章
