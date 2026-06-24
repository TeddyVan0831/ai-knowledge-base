---
title: "AutoGLM：智能体操作框架"
outline: deep
---

# AutoGLM：智能体操作框架

> **创建时间**: 2026-06-12
> **最后更新**: 2026-06-12
> **来源**: 
> **类型**: concept
> **创建时间**: 2026-06-12
> **最后更新**: 2026-06-12
> **来源**: 
> **领域**: ai

## 摘要

AutoGLM 是智谱（Zhipu AI）发布的智能体操作框架，核心目标是让 AI 能够在可视化屏幕上（网页和手机 App）替代人类完成一系列操作。采用**两阶段解耦架构**（规划器 + 执行器），通过自然语言中间界面连接，核心创新在于 **WebRL** 强化学习框架。PC 端基于 Chrome 插件实现，移动端基于安卓无障碍服务。

## 详情

### 典型应用场景

| 场景 | 示例 |
|------|------|
| 社交 | 微信点赞评论 |
| 电商 | 淘宝下单、携程订酒店 |
| 生活服务 | 美团订外卖 |
| 内容平台 | 知乎搜索/点赞/收藏/发布、小红书搜索 |
| 出行 | 12306 操作 |



### PC 端能力

通过 **Google Chrome 插件** 实现，支持通用模式（所有网页可用）和高级模式（仅限约十余个支持网站，如知乎、微博、百度贴吧、GitHub、网易新闻等）。

**操作示例**：搜索"强化学习"文章 → 筛选文章 → 按最多赞同排序 → 点赞并收藏。整个流程 AutoGLM 自动完成。

### 移动端能力

通过安卓系统的**无障碍服务（Accessibility Service）**获取操作权限。核心技术原理：

```
手机屏幕 → 无障碍服务 → 布局树文字描述 → LLM 理解 → 决策操作
```



移动端**不需要截图**，获取的是页面的结构化文字描述（类似 HTML 布局树），包含 Header、列表、元素（图片、标题、评分等）。手机端仅向部分用户开放，与荣耀手机厂商有合作。

### 两阶段解耦架构

AutoGLM 的核心架构创新——通过 **自然语言中间界面** 进行解耦：

**第一阶段：规划器（Planner）**
- 负责任务规划，输出纯文字描述
- 输出示例：动作（点击）、动作幅度（向下滑动 200 像素）、目标元素（右下角的"提交订单"按钮）
- 输出格式为固定槽位（Slot），共 6 种可执行动作：click、long press、scroll up/down/left/right
- 

**第二阶段：执行器（Executor）**
- 负责动作执行，接收规划器的自然语言指令
- 具备语言理解能力，精准预测屏幕坐标和操作
- 

架构流程：
```
用户指令 → [规划器] → 自然语言描述 → [执行器] → 屏幕操作
```



### 三大核心挑战

| 挑战 | 说明 |
|------|------|
| 训练数据稀缺 | 轨迹数据获取成本极高，需真人手动标注 |
| 反馈信号稀疏 | 不像游戏（赢/输），网页操作很难自动判断是否成功 |
| 策略分布漂移 | 模型输出的动作概率分布与实际最优分布之间的偏差 |



### 性能评估（WebArena-Lite 基准）

| 模型 | 配置 | 成功率 | 备注 |
|------|------|--------|------|
| GLM-4-Chat（未经微调） | 9B | **6.1%** | 基线 |
| GLM-4-9B（经过 WebRL） | 9B | **43.0%** | 提升 7.05x |
| GPT-4o（未经微调） | - | **13.9%** | 论文实测值 |
| Llama 3.1 8B（未经微调） | 8B | **4.8%** | 基线 |
| Llama 3.1 8B（经过 WebRL） | 8B | **42.4%** | 提升 8.83x |
| Llama 3.1 70B（经过 WebRL） | 70B | **49.1%** | 规模扩展效果 |



**关键结论**：
- WebRL 可将小模型（8B-9B）从几乎不可用提升到 42%-43% 的成功率
- 框架跨模型泛化（对 GLM 和 Llama 都有效）
- 授课人质疑：与 GPT-4o 的对比不够公平（GPT-4o 未在 WebArena 上微调）
- 43% 在真实场景中仍不可用，在重点优化网站可能达 85% 以上 

### 生态与评价

AutoGLM 全部基于现有语言模型（无新模型结构），核心创新在 WebRL 强化学习框架。授课人评价："没有任何新的概念，没有任何新的框架，也没有任何新的模型，也没有任何新的模型结构。" 

⚠️ **矛盾标注**：关于论文标题「Self-Evolving Online Curriculum Reinforcement Learning」——授课人最初认为"在线课程"是翻译错误（应为 Online Learning），但经原文核查（arXiv: 2411.02337），标题确为 "Self-Evolving Online Curriculum Reinforcement Learning"，翻译准确无误。

## 关联

- 相关概念: [WebRL：网页强化学习框架](/training-optimization/concept-webrl), [ORM：结果监督奖励模型](/training-optimization/concept-orm-reward-model), [Agent：从可控性到自主反思](/agent/concept-agent-controllability), [Agent 五级分类体系](/agent/concept-agent-taxonomy), [直播间 AI 评论互动助手](/industry-cases/concept-live-streaming-ai-assistant)
- 相关概念: [RLHF（基于人类反馈的强化学习）](/training-optimization/concept-rlhf), [MCP（Model Context Protocol）— 模型上下文协议](/agent/concept-mcp), [Agent 质量评估](/agent/concept-agent-evaluation)
- 参见: [Agent 开发全览 — 从原理到实践](/agent/topic-agent-development)

## 引用来源

- [1]  — AutoGLM 完整学习笔记：架构、WebRL、ORM、性能评估

## 变更记录

- 2026-06-12: 初始创建，来源 
