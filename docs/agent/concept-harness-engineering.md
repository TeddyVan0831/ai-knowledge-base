---
title: "Harness Engineering（harness 工程）"
outline: deep
---

# Harness Engineering（harness 工程）

> **类型**: concept
> **创建时间**: 2026-07-05
> **最后更新**: 2026-07-05
> **来源**: 
> **领域**: ai

## 摘要

Harness Engineering 是研究"如何围绕模型构建完整的运行与控制系统"的工程学科。它不是单一组件，而是把模型从"生成一段文字"变成"在真实环境中持续完成任务"所需的所有外部装置——循环、工具、状态、权限、验证、观测和恢复——的总称。Harness 没有唯一稳定定义，公开讨论中的分歧来自分析单位不同（运行时 / 项目外层 / 工程方法 / 组织系统），而非谁对谁错。

## 详情

### 一、Harness 的核心问题

> **当模型不再只是给出一段回复，而是要在真实系统里持续完成任务时，模型周围需要什么？**

### 二、五种分析单位（公开讨论中的分歧）

| 视角 | 代表来源 | 核心定位 | 适合解释什么 |
|------|----------|---------|------------|
| **严格运行时** | Macedo；Zhong & Zhu | 循环、工具、任务上下文、独立控制 | 判断对象是否足够完整 |
| **执行与托管运行时** | Anthropic；Microsoft；Codex | Shell/文件/Sandbox/审批/会话 | 模型怎样接到真实执行 |
| **用户外层控制** | Birgitta Böckeler | Guides + Sensors：文档、Skills、测试、Review | Coding Agent 外层补什么 |
| **失败防复发方法** | Mitchell Hashimoto | 每次失败沉淀为规则/工具/回归测试 | Harness 持续改进方法 |
| **Agent-first 交付系统** | Ryan Lopopolo / OpenAI | 仓库知识/CI/架构约束/组织 | Harness 扩展到组织交付 |

> 🖼️ [图 3] **Harness 定义光谱** — 五种分析单位（严格运行时 / 执行与托管运行时 / 用户外层控制 / 失败防复发方法 / Agent-first 交付系统），底部副标："它们可以同时成立，因为描述的不是同一层" — 

> **核心结论**：五种分析单位可以同时成立，因为描述的不是同一层——运行时、项目外层、工程方法、组织系统。

### 三、推荐的三层口径（课程技术核心）

从内到外的嵌套结构：

1. **模型（L0）**：被 Harness 包裹的核心
2. **Agent 运行与控制系统（L2-L3）**：循环、工具、工作空间、状态、权限、验证、恢复 — **本课程技术重点**
3. **项目 / 仓库外层 Harness（L1, L4）**：文档、Skills、CI、测试、架构规则、回归、评审
4. **Agent-first Operating Model（L5）**：组织、任务分配、审批、责任、交付方式

英文资料常写 Agent Harness / Runtime Harness / Runtime Substrate。

> 🖼️ [图 4] **推荐的三层口径** — 同心嵌套 4 层：模型（最内）→ Agent 运行与控制系统（蓝，循环/工具/状态/权限/验证/恢复）→ 项目/仓库外层 Harness（绿，文档/Skills/CI/测试/评审）→ Agent-first Operating Model（最外红，组织/任务分配/审批/责任）— 

### 四、三个易混概念区分

| 对象 | 能否独立保障 Agent 任务 |
|------|---------|
| **Prompt Engineering** | ❌ 不能（影响行为但不强制执行）|
| **Context Engineering** | ❌ 不能（是核心子系统但非全部）|
| **Agent Loop / ReAct** | ❌ 不能（无状态/权限/验证时只是循环）|
| **MCP / ACP / Tools** | ❌ 不能（是接口或协议）|
| **Agent Framework / SDK** | ❌ 不能自动保证（需具体配置）|
| **Agent Harness** | ✅ 讨论的核心对象 |
| **Agent-first Operating Model** | 更外层社会技术系统 |

**一句话**：
- **Prompt** 在说"希望模型怎样做"
- **Loop** 在说"模型什么时候继续想和行动"
- **Harness** 在说"这件事在哪里运行、能做什么、状态怎样保存、结果怎样验收、出错怎样恢复"

### 五、四问法（边界判断工具）

> 来自 Macedo 2026 预印本 *What makes a harness a harness*（[arXiv 2606.10106](https://arxiv.org/abs/2606.10106)），用作边界测试工具，非行业标准。

| 问题 | 通过条件 | 通过示例 | 不通过示例 |
|------|---------|---------|-----------|
| **T1 运行时是否存在"推理—行动—观察"闭环** | 观察能改变下一步 | 失败信息决定修改哪段代码 | 固定执行"检索→生成→格式化" |
| **T2 模型是否能感知并改变外部环境** | 工具允许写文件/调用命令 | 编辑仓库/创建工单（受权限约束）| 只给修改建议文本 |
| **T3 系统是否按任务内容管理上下文/状态** | 进入模型窗口的信息由当前任务决定 | 从 Progress/Plan/失败日志中选下一步 | 每轮追加全部聊天历史 |
| **T4 是否有不依赖模型服从的控制/验证** | 权限/测试/策略门能独立阻断 | 工具调用上限/审批门/幂等键 | 只在 Prompt 里写"请勿删除文件" |

四项都"是"时，才适合称为完整 Harness。

> 🖼️ [图 5] **四问法** — 判断一个对象是不是完整 Agent Harness 的 4 个并列问题：(1) 有没有运行时循环？观察结果会不会改变下一步；(2) 能不能作用于环境？工具能读取并改变外部状态；(3) 有没有任务感知的上下文/状态？不是把全部聊天记录原样推回去；(4) 有没有独立于模型服从的控制？权限、测试、策略或状态检查 — 

### 六、Harness 覆盖层次 L0-L5

| 层次 | 内容 | 备注 |
|------|------|------|
| **L5 治理与组织** | 身份、审批、平台模板、责任、成本、审计 | 外层 operating model；编码成策略后部分进入 Harness |
| **L4 质量与交付** | Trace、Event logs、Tests、Eval、CI、Review | 典型 outer harness |
| **L3 任务运行与服务** | Loop、编排、状态、记忆、恢复、消息、流式 | 技术核心 |
| **L2 行动与环境** | Tools、MCP、Skills、Workspace、Sandbox | 技术核心 |
| **L1 指导与上下文** | Prompt、规则、文档、RAG、Progress | 关键组件；单独不充分 |
| **L0 模型** | 权重、推理能力、版本、预算 | 被 Harness 包裹的核心，**不是 Harness** |

> 🖼️ [图 7] **Harness 覆盖层次** — 从模型到组织的 6 层嵌套：L0 模型（被 Harness 包裹）→ L1 指导与上下文（关键组件；单独不充分）→ L2 行动与环境（技术核心）→ L3 任务运行与服务（技术核心）→ L4 质量与交付（典型 outer harness）→ L5 治理与组织（外层 operating model）— 

### 七、Harness 厚度矩阵

| 任务类型 | 所需 Harness 厚度 |
|---------|---------------|
| 短任务 × 低风险（只读问答）| 薄 Harness：格式、超时、基本日志 |
| 短任务 × 高风险（一次写入/外部操作）| 需要权限、审批、幂等与结果验证 |
| 长任务 × 低风险（研究汇总/批量分析）| 需要状态、Checkpoint、进度与成本控制 |
| 长任务 × 高风险（持续行动/多系统协同）| 完整状态机、恢复、审计、Eval 与人工升级 |

> 决定 Harness 厚度不是"用了多大的模型"，而是任务持续时间、副作用可逆性、动态探索需求、独立验证难度、失败成本与责任。

> 🖼️ [图 9] **Harness 厚度矩阵** — 二维矩阵（X：任务跨度/状态持续时间，Y：副作用与验证强度），4 象限分别对应：短任务×低风险（薄 Harness）/ 短任务×高风险（权限审批幂等）/ 长任务×低风险（状态 Checkpoint 进度）/ 长任务×高风险（完整状态机恢复审计）— 

## 关联

- 相关概念: [Agent Loop（智能体循环）](/agent/concept-agent-loop), [上下文工程（Context Engineering）](/agent/concept-context-engineering), [MCP 协议（已合并）](/base-models/concept-mcp-protocol), [智能体记忆管理（Agent Memory Management）](/agent/concept-agent-memory), [Agent：从可控性到自主反思](/agent/concept-agent-controllability), [Agent 质量评估](/agent/concept-agent-evaluation)
- 主题: [2026 Agent 架构综述](/agent/topic-agent-architecture-2026)
- 案例: [Anthropic 长任务 Harness 案例（Opus 4.5）](/agent/case-anthropic-long-running-agent), [SWE-agent ACI 接口实验案例](/agent/case-swe-agent-aci-experiment), [OpenAI Agent-first 仓库案例](/agent/case-openai-agent-first-warehouse)
- 配套资料: 

## 引用来源

- [1]  — 课堂转录稿 + 配套讲义 + 11 张图片识别（2026-07-01）
- [2] Macedo 2026 预印本 *What makes a harness a harness* — [arXiv 2606.10106](https://arxiv.org/abs/2606.10106)
- [3] Anthropic Engineering 2025-11-26 *Effective harnesses for long-running agents*
- [4] Ryan Lopopolo / OpenAI 2026 *Harness engineering: leveraging Codex in an agent-first world*
- [5] John Yang et al. NeurIPS 2024 *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*

## 变更记录

- 2026-07-05: 初始创建，来源 
