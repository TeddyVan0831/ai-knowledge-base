# AI 知识库

> 从基础理论到行业应用的完整 AI 知识图谱 —— 113 个核心概念，9 大主题域，用 Markdown 写作，自动构建为在线网站。
> 
> 2026.6.15 updated

**在线阅读**：[https://teddyvan0831.github.io/ai-knowledge-base/](https://teddyvan0831.github.io/ai-knowledge-base/)

---

## 知识体系

```
导读              如何阅读 · 页面类型说明
基础模型与训练     Transformer · Embedding · LLM 演进 · 推理模型 · GPU 硬件
模型架构            MoE · 注意力优化 · KV Cache · 解码加速 · 显存计算
训练与优化          微调 · 量化 · 剪枝 · 蒸馏 · RLHF · WebRL
推理与部署          高并发 · 硬件选型 · llama.cpp · SGLang · 边缘推理
Agent 智能体       设计模式 · MCP · AutoGLM · 评估 · 五级分类
RAG 检索增强       基础 RAG · Agentic RAG · Text-to-SQL
多模态与视觉        图像生成 · 视频生成 · 数字人 · 视觉识别
行业应用案例        财务表格 · HR培训 · 直播助手
工具与生态          CUDA · NVIDIA · ASML · 芯片竞争
```

## 本地开发

```bash
npm install
npm run docs:dev      # 开发预览 http://localhost:5173/ai-knowledge-base/
npm run docs:build    # 构建
npm run docs:preview  # 预览构建产物
```

推送代码到 `main` 分支后，GitHub Actions 会自动构建并部署到 GitHub Pages。

## 内容来源

本知识库基于 Andrej Karpathy 的 LLM Wiki 模式构建，所有内容来自个人 AI 学习笔记的系统化编译整理。

## License

代码采用 MIT 许可；文档内容采用 CC BY-SA 4.0 许可。
