---
title: "Anthropic 长任务 Harness 案例（Opus 4.5）"
outline: deep
---

# Anthropic 长任务 Harness 案例（Opus 4.5）

> **类型**: entity
> **创建时间**: 2026-07-05
> **最后更新**: 2026-07-05
> **来源**:  第 3 章
> **领域**: ai

## 摘要

Anthropic Engineering 2025-11-26 发表 *Effective harnesses for long-running agents*，以 Claude Agent SDK 中的 **Opus 4.5** 为实验对象（已具备工具调用和上下文压缩 Compaction），探索长任务（跨多个上下文窗口循环执行高层 Web 应用任务）的稳定交付机制。**核心发现**：有了强模型、工具、Agent Loop 和上下文压缩，**长任务仍然不能自然变成稳定交付**；必须通过外部系统工件（feature list / progress.txt / git / init.sh / 端到端测试）将任务状态从聊天上下文迁移到可见、可版本化、可验证的外部世界。

## 详情

### 一、5 种稳定出现的失败模式

| # | 失败模式 | 根因 |
|---|---------|------|
| 1 | **一次做太多、上下文耗尽** | Agent 试图一次完成太多工作，上下文耗尽时留下半实现、未说明的代码 |
| 2 | **新会话失忆** | 新会话不知道上一会话到底做了什么，只能从仓库现状重新猜 |
| 3 | **误判已有进展** | 项目已有部分功能后，后续会话容易把"已有进展"误判成"全部完成" |
| 4 | **环境带病继续** | 环境已经损坏时，Agent 仍继续增加功能，使错误继续累积 |
| 5 | **提前宣布完成** | 模型自己说自己完成，但没有外部验收证据 |

> 课堂结论：**这些失败不是"模型完全不会写代码"，而是"循环和上下文压缩只解决继续调用模型，并没有自动解决目标分解、跨会话状态、工作基线、完成证据和交接"**。

### 二、5 项系统工件修复表

| 观察到的失败 | 加入的系统工件或规则 | 为什么有用 |
|---|---|---|
| 一次做太多、上下文中断 | 初始会话把高层目标展开为完整功能清单；后续会话一次只推进一个功能 | 把"整个项目"改造成有限、可选择、可检查的下一步 |
| 新会话失忆 | `claude-progress.txt` 与 Git 历史 | 新会话读取外部事实，而不是依赖压缩后的聊天摘要猜测 |
| 不知道怎样启动和检查系统 | initializer 生成 `init.sh`；新会话先启动应用并做基础端到端检查 | 先确认当前基线可工作，再增加新变化 |
| 提前宣布完成 | 功能清单初始全部标记为 failing；实际端到端测试后才允许改为 passing | "完成"由外部验收结果决定，不由模型一句话决定 |
| 环境留下半成品 | 每次会话结束前提交代码、记录进度并保持可继续工作的基线 | 让恢复、回滚和下一次交接都有明确落点 |

### 三、关键工件清单

| 工件 | 作用 |
|------|------|
| `feature_list.json` | 把高层需求展开成可验证的端到端功能；示例里细到上百项，开始时全部标记为 failing |
| `claude-progress.txt` | 记录每个会话做过什么、剩下什么 |
| Git 历史 | 保存可恢复的工作基线和变更事实 |
| `init.sh` | 让后续会话不必重新猜测怎样启动应用 |
| Puppeteer MCP / 基础端到端测试 | 新会话先确认基础功能仍然可用，再开始新工作 |

> **核心理念**：这些工件不是"记忆插件"的堆叠，而是把**任务状态从聊天上下文迁移到可见、可版本化、可验证的外部世界**。

### 四、关键启示

1. **循环 ≠ 任务管理**：Agent Loop + Context Compaction 只解决"继续调用模型"，不解决"目标分解、跨会话状态、工作基线、完成证据和交接"
2. **外部化是核心**：所有关键状态都应外化到文件/版本控制，避免依赖聊天历史
3. **验收独立化**：完成由外部测试决定，不由模型自己说
4. **基线可重放**：每次会话结束保留可继续工作的基线，便于恢复和回滚

## 关联

- 相关概念: [Harness Engineering（harness 工程）](/base-models/concept-harness-engineering), [Agent 任务生命周期](/base-models/concept-agent-task-lifecycle), [Harness 覆盖层次（L0–L5）](/base-models/concept-harness-coverage-levels)
- 主题: [topic-agent-architecture-2026](/base-models/topic-agent-architecture-2026)
- 配套资料: 
- 相关案例: [SWE-agent ACI 接口实验案例](/base-models/case-swe-agent-aci-experiment), [OpenAI Agent-first 仓库案例](/base-models/case-openai-agent-first-warehouse)

## 引用来源

- [1]  — 第 3 章 案例（图片识别 3）
- [2] Anthropic Engineering 2025-11-26 *Effective harnesses for long-running agents*

## 变更记录

- 2026-07-05: 初始创建，来源  第 3 章
