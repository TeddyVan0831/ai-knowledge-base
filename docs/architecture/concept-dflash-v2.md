---
title: "DFlash V2：下一代推测解码"
outline: deep
---

# DFlash V2：下一代推测解码

> **类型**: concept
> **创建时间**: 2026-06-16
> **最后更新**: 2026-06-16
> **来源**: 

## 摘要

DFlash V2 是推测解码路线的最新突破（ICML 2026），由 Z Lab + SGLang + Modal 联合发布。核心创新有二：**块扩散并行出稿**（草稿模型一次前向出一整块 token，消除自回归等待）和 **每层 KV 注入**（目标 LLM 隐藏态实时注入草稿每一层 KV cache，消除信号衰减）。在 Qwen 3.5 397B-A17B / 8×B200 上达到 baseline 吞吐的 **4.3 倍**，比模型自带 MTP 快 **50%**。

## 详情

### 背景：推测解码的二次瓶颈

投机解码让大模型一次性验证小模型的草稿，但草稿模型自己仍是逐 token 自回归生成——瓶颈从大模型转移到了小模型。草稿延迟随长度线性增长（4→8→16 token，延迟同步翻倍），实践中草稿深度多被限制在 1-3 层。

### 核心创新一：块扩散并行出稿

草稿模型不再逐 token 自回归生成，而是用扩散方式从含噪表示开始，一次前向传播并行生成一整块 token（4/8/16）：

| 方式 | 延迟 | 说明 |
|------|------|------|
| EAGLE 自回归 | γ × τ_layer | 逐 token 线性增长 |
| DFlash 块扩散 | 1 × τ_block | 恒定，几乎不随 γ 增长 |

5 层 DFlash 出 16 token 延迟 < EAGLE-3 单层出 4 token 延迟。

### 核心创新二：每层 KV 注入

EAGLE 只在输入端注入一次目标 LLM 特征，信号随层深衰减。DFlash 将目标 LLM 每层的隐藏态投影到草稿对应层的 KV cache——草稿模型的每一层都在"听原版广播"：

```
DFlash KV 注入：
  目标 LLM 隐藏态 → 投影 → 注入草稿每一层 KV cache
  → 信号永不衰减 → 草稿深度可扩展至 5 层以上，接受率不降反升
```



**即时物化**：KV 投影在草稿前向之前完成，投影产物不存储——完成即丢弃，零额外显存。Triton 融合 Norm+RoPE 后处理在单 kernel 内完成。

### 消融实验（Qwen 3-4B，5层草稿）

| 变体 | 出稿方式 | KV注入 | GSM8K speedup |
|------|----------|--------|---------------|
| EAGLE-3（基线） | 自回归 | ❌ | 2.1× |
| DFlash 仅扩散 | 块扩散 | ❌ | 2.9× |
| DFlash 仅注入 | 自回归 | ✅ | 2.4× |
| **DFlash 完整** | 块扩散 | ✅ | **3.3×** |

两机制正交互补——加速来自块扩散（消自回归等待）和 KV 注入（提接受率）的叠加。

### Flagship 结果

Qwen 3.5 397B-A17B / 8×B200 / HumanEval / greedy：
- baseline: 1.0×
- 原生 MTP（7步）: ~2.87×
- DFlash（块大小 16）: **4.3×**（+330% vs baseline, +50% vs MTP）



### 三方法演进本质

| 方法 | 核心思路 | 瓶颈 |
|------|---------|------|
| Medusa | 主模型多预测头并行猜 | 各猜各的，无依赖，接受率低 |
| EAGLE | 偷看主模型特征 → 自回归逐字写 | 草稿自回归 = 新瓶颈 |
| DFlash V2 | 每层 KV 注入（全程直播）+ 块扩散（整页复印） | — |

**DFlash vs MTP**：MTP 是训练时写死在模型里的"天赋"（不能跨模型用），DFlash 是外挂草稿模型的"后天技能"（随时挂、跨模型复用）。实际测试 DFlash 比 Qwen 自带 MTP 快 50%。

### Spec V2 重叠调度

不改模型和算法，纯工程优化——Host 端清理/分配与 GPU 计算并行：Qwen 3-8B 单 B200 并发 32 场景获 **33%+ 吞吐提升**。

### 局限

- 仅 greedy 解码下测试（未覆盖 temperature>0 场景）
- 仅 Qwen 模型族验证
- 训练细节需查原文 arXiv:2602.06036
- 结构化输出场景未覆盖



## 关联

- 相关概念: [投机解码（Speculative Decoding）](/architecture/concept-speculative-decoding), [MTP：多 Token 预测（Multi-Token Prediction）](/architecture/concept-mtp-multi-token-prediction), [注意力机制优化](/architecture/concept-attention-optimization), [KV Cache](/architecture/concept-kv-cache)
- 相关概念: [KV Cache 量化](/architecture/concept-kv-cache-quantization), [TTFT 优化（首 Token 延迟）](/architecture/concept-ttft-optimization)
- 参见: [模型优化](/training-optimization/topic-model-optimization)

## 引用来源

- [1]  — DFlash V2 完整分析：块扩散、KV注入、Spec V2、三方法对比、部署实践
- [2] LMSYS Blog (2026-06-15) — The next generation of speculative decoding: DFlash and Spec V2

## 变更记录

- 2026-06-16: 初始创建，来源 
