---
title: "Claude Code + CC Switch 实战"
outline: deep
---

# Claude Code + CC Switch 实战

> **类型**: concept
> **创建时间**: 2026-07-06
> **最后更新**: 2026-07-06
> **来源**: 
> **领域**: ai

## 摘要

**Vibe Coding** 概念由 Claude Code 首次提出（"看着 AI 编程，提供情绪价值"），通过 **CC Switch**（中国开发者开源）把任意 LLM 服务（自部署的 DeepSeek V4 / GLM / 第三方模型）"装进" Claude Code 工作流——核心是 **Anthropic Messages 协议 → OpenAI Chat Completions 协议** 的转换。配合 `/init`（生成项目规则文档）和 **Plan Mode**（先出计划再执行），形成完整的 Vibe Coding 实战工作流。

## 详情

### 一、Claude Code 简介

- **Vibe Coding 概念首个提出者**
- 形态：CLI 工具（NodeJS 实现，可通过 NPM 安装）
- vs Cursor：Claude Code 的"外部控制台"形态不同
- 中国大陆使用：需要翻墙，Anthropic 屏蔽大量 IP

### 二、定价（截至 2026-07-05）

| 套餐 | 价格 | 适用场景 |
|------|------|---------|
| **Pro** | **$20/月**（按年付费约 $17/月）| 轻量级开发够用 |
| **Max 5x** | **$100/月** | 中度使用 |
| **Max 20x** | **$200/月** | 重度使用 |

> ⚠️ 2026-07-05 之前流传的"Pro $17"为不准确，官方定价为 $20/月（年付约 $17/月）

### 三、CC Switch 工具

- **中国人开发**（"非常好用"）
- 支持工具：Claude Code、Codex、OpenCode、小龙虾 Claude、HERMES
- 下载：GitHub release 列表
- **核心价值**：协议转换（Anthropic Messages → OpenAI Chat Completions）

### 四、CC Switch 配置流程

| 步骤 | 操作 |
|------|------|
| 1 | 下载安装 CC Switch |
| 2 | 打开"自定义配置项" |
| 3 | **API Key** 留空（自部署无 Key）|
| 4 | **请求地址** 填服务器公网 IP（**不能填 localhost**）|
| 5 | 完整 API URL 推荐填 `http://IP:8000/v1/chat/completions` |
| 6 | **⚠️ 高级选项**：选择 OpenAI chat completions 格式 |
| 7 | **模型映射**：把自部署模型名映射到 Claude Code 能识别的名字 |

### 五、路由机制（CC Switch 工作原理）

```
Claude Code → CC Switch 路由（协议转换）→ 自部署模型
           （Anthropic 协议转 OpenAI 协议）
```

**常见问题**：
- "绑定失败，提示 80 端口被占用" → 之前的 CC Switch 实例还在运行 → 退出后再启动

### 六、Claude Code 实战技巧

| 技巧 | 作用 |
|------|------|
| **`/init`** | 扫描项目已初始化内容，生成 `CLAUDE.md` 规则文档（开发规范、设计规范、业务规范）→ 后续维护都参考此文档 |
| **Plan Mode**（Shift+Tab）| 任何操作前先让 Claude Code 输出计划，**不修改任何文件** → 用户审阅计划 → 讨论修改 → 确认后再执行 |

> "他一开始做计划的时候，他不会影响到你所有的就是已有的在项目中所有的内容他不愿意给你乱改" — 授课人原话

### 七、完整工作流（自部署模型接入）

```
1. 自部署 DeepSeek 模型（昇腾 910B × 8 + vLLM-Ascend Docker）
2. CC Switch 配置（Anthropic 协议 → OpenAI chat completions 转换）
3. Claude Code 连接 CC Switch
4. 进入项目文件夹
5. /init 生成 CLAUDE.md 项目规则文档
6. Plan Mode 模式下讨论方案
7. 执行任务（如：写贪吃蛇游戏）
8. 验证：贪吃蛇可玩
```

### 八、为什么 Claude Code 是 Vibe Coding 的开创者

- **工作目录感知**：进入项目后自动建立上下文（CLAUDE.md）
- **Plan Mode 安全机制**：先出方案，不直接动文件
- **协议灵活性**：通过 CC Switch 可对接任意 LLM 后端
- **工具调用标准化**：tool use + function calling 一致体验

## 关联

- 相关概念: [国产算力部署实践（昇腾 910B + vLLM-Ascend）](/inference-deploy/concept-ascend-deployment)、[Agent Ops](/agent/concept-agent-ops)
- 配套资料: 

## 引用来源

- [1]  — 第 6 章 Claude Code + CC Switch 实战
- [2] [Claude Code 价格指南（2026-07-05 更新）](https://blog.laozhang.ai/zh/posts/claude-code-pricing-guide) — Pro $20/月、Max $100/$200
- [3] [Claude Code Pricing 2026 (aitoolsrecap.com)](https://aitoolsrecap.com/Blog/claude-code-pricing-explained-2026) — 五层定价
- [4] [CC Switch GitHub Release](https://github.com/farion1231/cc-switch/releases) — 协议转换工具

## 变更记录

- 2026-07-06: 初始创建，来源 notes-50 第 6 章
