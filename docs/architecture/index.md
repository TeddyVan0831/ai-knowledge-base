---
title: "模型架构"
outline: deep
---

# 模型架构

深入 LLM 内部架构 —— 注意力机制优化、KV Cache 管理、MoE 混合专家、投机解码等核心技术。

## 注意力机制

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-attention-optimization](./concept-attention-optimization) | 注意力机制优化 | Flash Attention、MQA/GQA、稀疏注意力等多种优化方案 |
| [concept-mla-multi-head-latent-attention](./concept-mla-multi-head-latent-attention) | MLA：多头潜在注意力 | DeepSeek V3 核心创新，KV Cache 占用减少约 14 倍 |

## KV Cache 优化

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-kv-cache](./concept-kv-cache) | KV Cache | 自回归生成中的键值缓存技术，LLM 推理的核心瓶颈 |
| [concept-kv-cache-compression](./concept-kv-cache-compression) | KV Cache 动态压缩 | 剔除不重要 token 实现 50-90% 内存节省 |
| [concept-kv-cache-quantization](./concept-kv-cache-quantization) | KV Cache 量化 | 从 FP16 压缩到 INT8/INT4，误差自回归累积 |

## MoE 混合专家

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-deepseek-moe](./concept-deepseek-moe) | DeepSeekMoE：混合专家架构 | 671B 总参数，每次推理仅激活 ~37B |
| [concept-loss-free-load-balancing](./concept-loss-free-load-balancing) | Loss-Free Load Balancing | DeepSeek V3 无辅助损失的 MoE 负载均衡方案 |

## 解码加速

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-speculative-decoding](./concept-speculative-decoding) | 投机解码（Speculative Decoding） | 小模型草稿 + 大模型验证，1.7-3.5x 加速 |
| [concept-ttft-optimization](./concept-ttft-optimization) | TTFT 优化（首 Token 延迟） | 预填充阶段占 90%+，并行化与算子融合优化 |
| [concept-mtp-multi-token-prediction](./concept-mtp-multi-token-prediction) | MTP：多 Token 预测 | 训练时辅助预测模块，推理时丢弃 |

## 推测解码与加速

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-speculative-decoding](./concept-speculative-decoding) | 推测解码 | 小模型草稿 + 大模型验证，加速自回归推理 |
| [concept-dflash-v2](./concept-dflash-v2) | DFlash V2：下一代推测解码 | 块扩散 + KV 注入，4.3× 吞吐，ICML 2026 |
| [concept-ttft-optimization](./concept-ttft-optimization) | TTFT 优化 | 首 Token 延迟优化策略 |

## 精度与显存

| 文件 | 标题 | 摘要 |
|------|------|------|
| [concept-fp8-mixed-precision](./concept-fp8-mixed-precision) | FP8 混合精度训练 | 核心组件高精度，非关键计算降为 FP8 |
| [concept-vram-calculation](./concept-vram-calculation) | 显存计算方法论 | 训练显存 ≈ 推理显存 × 4 |
