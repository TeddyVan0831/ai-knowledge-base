---
title: "国产算力部署实践（昇腾 910B + vLLM-Ascend）"
outline: deep
---

# 国产算力部署实践（昇腾 910B + vLLM-Ascend）

> **类型**: concept
> **创建时间**: 2026-07-06
> **最后更新**: 2026-07-06
> **来源**: 
> **领域**: ai

## 摘要

在 8 卡昇腾 910B + 鲲鹏 920 服务器上，通过 **vLLM-Ascend Docker** 部署 DeepSeek V4-Flash W8A8 MTP 量化版，**不在 host 主系统上做任何配置**（避免国产系统挂掉），全部用容器化封装。完整流程：系统检查 → 模型下载 → Docker 启动 vLLM-Ascend → curl 验证 → 客户端接入。这是国产算力部署的"标准范式"。

## 详情

### 一、服务器配置参考

| 组件 | 规格 |
|------|------|
| **GPU** | 昇腾 910B × 8（8 卡 910B） |
| **CPU** | 鲲鹏 920，12 核 × 4 = **48 核** |
| **内存** | 约 1 TB |
| **存储** | 480GB SSD × 2 + 3.4TB NVMe |
| **网卡** | 2 块 200G 官网卡（插光纤）+ 2 块 25G |
| **操作系统** | 麒麟 V10 SP3（Kylin Linux V10，内核 4.19.90）|
| **全国产化** | 服务器 + 操作系统 + 显卡全部国产 |

### 二、部署模型选择

- **DeepSeek V4-Flash W8A8 MTP 量化版**
  - W8A8 = Weight 8-bit + Activation 8-bit 量化
  - MTP（Multi-Token Prediction）= 一次生成多个 token
- 模型大小：约 **300+ GB**
- 下载：阿里 ModelScope（国内可用）
- 选择原因："vLLM-Ascend 团队里边就是现在做的最好的一个模型"

### 三、核心原则：不在 host 上做配置

**为什么必须用 Docker**：
- 远程实体服务器配置复杂
- **不能动 host 主系统**——升级可能挂掉
- 8 卡系统重装非常麻烦
- 找到对应技术人员 → 重新装系统

> "这种的话我们就尽量不要动它，这个 host 不要动它……我们就采用容器化的形式是最方便的" — 授课人原话

### 四、Docker 部署关键参数

> 🖼️ [图 12] **昇腾软件栈 CANN** — CANN 六层架构：昇腾 AI 应用 → AscendCL 算子开发 → 算子库/调优 → 图编译器 → 执行器 → 基础层（对标 NVIDIA CUDA）— 

```bash
docker run \
  --device /dev/davinci0:/dev/davinci0 \  # 显卡映射
  -v /usr/local/dcmi:/usr/local/dcmi \      # 主机目录映射
  -p 8000:8000 \                            # 端口映射
  --name vllm-ascend-server \
  vllm-ascend-image
```

| 参数 | 作用 |
|------|------|
| `--device` | 主机显卡映射到容器 |
| `-v` | 主机目录映射到容器（容器内用外层文件夹）|
| `-p 8000:8000` | 端口映射，host 可通过 `host:8000` 访问 |

### 五、vLLM 启动参数

| 参数 | 作用 | 推荐值 |
|------|------|--------|
| `--dtype` | 计算精度 | **bfloat16**（模型原始精度）|
| `--max-model-len` | 最大输入输出总长 | **135K**（演示 Claude Code）|
| `--gpu-memory-utilization` | vLLM 占显存比 | **0.9 - 0.95** |
| `--block-size` | PagedAttention 块大小 | 官方推荐值 |
| `--tensor-parallel-size` | 张量并行卡数 | **8**（8 卡部署）|
| `--served-model-name` | API 调用别名 | 任意（如 "ds"）|
| `--speculative-config.num-speculative-tokens` | MTP 额外生成 token 数 | 1 或 2 |

**关键原理**：
- **PagedAttention**：把显存切成"页"（block），类似内存分页 → 减少碎片、提升利用率
- **张量并行**：单卡放不下整个模型 → 切到多卡部署

### 六、验证部署成功

```bash
# 1. 查看部署的模型
curl http://<服务器IP>:8000/v1/models

# 2. 测试对话
curl http://<服务器IP>:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "ds", "messages": [{"role": "user", "content": "你好"}]}'
```

**返回示例**（含 ID / object / created / model / choices / message）：
```json
{
  "id": "...",
  "object": "chat.completion",
  "model": "ds",
  "choices": [{
    "message": {
      "role": "assistant",
      "content": "你好，我是 DeepSeek"
    }
  }]
}
```

### 七、API 兼容性

- vLLM 默认提供 **OpenAI 兼容 Chat Completions API**
- base_url 默认 `http://localhost:8000/v1`
- 客户端可用任何 OpenAI 兼容 SDK 接入

## 关联

- 相关概念: [华为昇腾 AI 生态](/base-models/concept-ascend-ecosystem)、[Claude Code + CC Switch 实战](/agent/concept-claude-code-agent)
- 配套资料: 

## 引用来源

- [1]  — 第 5 章实操
- [2] [vLLM OpenAI Compatible Server 文档](https://docs.vllm.ai/en/stable/serving/online_serving/openai_compatible_server/) — API 路径 / 兼容性
- [3] [vLLM CLI 参考](https://docs.vllm.ai/en/latest/cli/) — `--served-model-name` 参数
- [4] [vLLM-Ascend GitHub](https://github.com/ascend-tribe/vllm-ascend) — 昇腾适配推理引擎

## 变更记录

- 2026-07-06: 初始创建，来源 notes-50 第 5 章
