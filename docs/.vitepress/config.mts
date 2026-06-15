import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "AI 知识库",
  description: "从基础理论到行业应用的完整 AI 知识图谱",
  base: "/ai-knowledge-base/",
  lang: "zh-CN",
  lastUpdated: true,
  ignoreDeadLinks: true,

  head: [
    ['meta', { name: 'theme-color', content: '#2563eb' }],
    ['link', { rel: 'icon', href: '/ai-knowledge-base/favicon.ico' }],
  ],

  themeConfig: {
    logo: false,
    
    nav: [
      { text: '首页', link: '/' },
      { text: '导读', link: '/guide/' },
    ],

    sidebar: {
      '/base-models/': [
        {
          text: '基础模型与训练',
          items: [
            { text: '总览', link: '/base-models/' },
            { text: 'Transformer 架构', link: '/base-models/concept-transformer-architecture' },
            { text: 'Embedding 与向量化', link: '/base-models/concept-embedding' },
            { text: 'LLM 训练范式', link: '/base-models/concept-llm-training-paradigm' },
            { text: 'LLM 演进史', link: '/base-models/concept-llm-history' },
            { text: '推理模型', link: '/base-models/concept-reasoning-models' },
            { text: 'DeepSeek R1', link: '/base-models/concept-reasoning-models-deepseek-r1' },
            { text: 'In-Context Learning', link: '/base-models/concept-in-context-learning' },
            { text: 'Few-Shot Prompting', link: '/base-models/concept-few-shot-prompting' },
            { text: '贝叶斯推理', link: '/base-models/concept-bayesian-reasoning' },
            { text: 'Embedding 模型选型', link: '/base-models/concept-embedding-model-selection' },
            { text: 'H100 GPU', link: '/base-models/model-h100' },
            { text: 'B200 GPU', link: '/base-models/model-b200' },
          ]
        }
      ],
      '/architecture/': [
        {
          text: '模型架构',
          items: [
            { text: '总览', link: '/architecture/' },
            { text: 'DeepSeek MoE', link: '/architecture/concept-deepseek-moe' },
            { text: 'MLA 多头潜在注意力', link: '/architecture/concept-mla-multi-head-latent-attention' },
            { text: 'MTP 多 Token 预测', link: '/architecture/concept-mtp-multi-token-prediction' },
            { text: '注意力机制优化', link: '/architecture/concept-attention-optimization' },
            { text: 'KV Cache', link: '/architecture/concept-kv-cache' },
            { text: 'KV Cache 压缩', link: '/architecture/concept-kv-cache-compression' },
            { text: 'KV Cache 量化', link: '/architecture/concept-kv-cache-quantization' },
            { text: '推测解码', link: '/architecture/concept-speculative-decoding' },
            { text: 'TTFT 优化', link: '/architecture/concept-ttft-optimization' },
            { text: '显存计算', link: '/architecture/concept-vram-calculation' },
          ]
        }
      ],
      '/training-optimization/': [
        {
          text: '训练与优化',
          items: [
            { text: '总览', link: '/training-optimization/' },
            { text: 'LLM 微调原理', link: '/training-optimization/concept-llm-fine-tuning' },
            { text: '后训练量化 PTQ', link: '/training-optimization/concept-quantization-ptq' },
            { text: '旋转量化', link: '/training-optimization/concept-quantization-rotation' },
            { text: '模型剪枝与稀疏化', link: '/training-optimization/concept-model-pruning' },
            { text: '知识蒸馏', link: '/training-optimization/concept-knowledge-distillation' },
            { text: 'RLHF', link: '/training-optimization/concept-rlhf' },
            { text: 'WebRL 强化学习', link: '/training-optimization/concept-webrl' },
            { text: 'ORM 奖励模型', link: '/training-optimization/concept-orm-reward-model' },
            { text: '模型优化综述', link: '/training-optimization/topic-model-optimization' },
          ]
        }
      ],
      '/inference-deploy/': [
        {
          text: '推理与部署',
          items: [
            { text: '总览', link: '/inference-deploy/' },
            { text: '企业级 AI 部署', link: '/inference-deploy/concept-enterprise-ai-deployment' },
            { text: '高并发 AI 服务', link: '/inference-deploy/concept-high-concurrency-ai' },
            { text: 'SGLang 优化', link: '/inference-deploy/concept-sglang-optimization' },
            { text: 'llama.cpp', link: '/inference-deploy/concept-llamacpp' },
            { text: 'MNN 框架', link: '/inference-deploy/concept-mnn' },
            { text: 'MediaPipe LLM', link: '/inference-deploy/concept-mediapipe-llm' },
            { text: 'vLLM', link: '/inference-deploy/product-vllm' },
            { text: 'LangChain', link: '/inference-deploy/product-langchain' },
            { text: '边缘推理全景', link: '/inference-deploy/topic-edge-inference' },
            { text: '部署运维综述', link: '/inference-deploy/topic-ai-deployment-ops' },
          ]
        }
      ],
      '/agent/': [
        {
          text: 'Agent 智能体',
          items: [
            { text: '总览', link: '/agent/' },
            { text: 'Agent 可控性', link: '/agent/concept-agent-controllability' },
            { text: 'Agent 五级分类', link: '/agent/concept-agent-taxonomy' },
            { text: 'MCP 协议', link: '/agent/concept-mcp' },
            { text: 'AutoGLM', link: '/agent/concept-autoglm' },
            { text: 'Prompt Chaining', link: '/agent/concept-prompt-chaining' },
            { text: 'Reflection 反思', link: '/agent/concept-reflection' },
            { text: 'Tool Use', link: '/agent/concept-tool-use' },
            { text: '多 Agent 协作', link: '/agent/concept-multi-agent-collaboration' },
            { text: 'Agent 评估', link: '/agent/concept-agent-evaluation' },
            { text: 'Agent 开发综述', link: '/agent/topic-agent-development' },
            { text: '设计模式综述', link: '/agent/topic-agentic-design-patterns' },
          ]
        }
      ],
      '/rag/': [
        {
          text: 'RAG 检索增强',
          items: [
            { text: '总览', link: '/rag/' },
            { text: 'RAG 基础', link: '/rag/concept-rag' },
            { text: 'RAG 高级检索', link: '/rag/concept-rag-advanced-retrieval' },
            { text: 'Agentic RAG', link: '/rag/concept-agentic-rag' },
            { text: 'Text-to-SQL', link: '/rag/concept-text-to-sql' },
            { text: 'RAG 优化综述', link: '/rag/topic-rag-optimization' },
          ]
        }
      ],
      '/multimodal/': [
        {
          text: '多模态与视觉',
          items: [
            { text: '总览', link: '/multimodal/' },
            { text: '多模态 Transformer', link: '/multimodal/concept-multimodal-transformer' },
            { text: '图像生成', link: '/multimodal/concept-image-generation' },
            { text: '视频生成', link: '/multimodal/concept-video-generation' },
            { text: '数字人技术', link: '/multimodal/concept-digital-human' },
            { text: '视觉识别', link: '/multimodal/concept-vision-recognition' },
            { text: 'Meta Sapiens', link: '/multimodal/concept-meta-sapiens' },
            { text: 'MAE 掩码自编码器', link: '/multimodal/concept-mae-masked-autoencoder' },
          ]
        }
      ],
      '/industry-cases/': [
        {
          text: '行业应用案例',
          items: [
            { text: '总览', link: '/industry-cases/' },
            { text: 'AI 教育产品', link: '/industry-cases/concept-ai-education-cases' },
            { text: '财务表格识别', link: '/industry-cases/concept-ai-table-recognition-evaluation' },
            { text: '直播 AI 助手', link: '/industry-cases/concept-live-streaming-ai-assistant' },
            { text: '培训对练智能体', link: '/industry-cases/concept-ai-training-agent' },
          ]
        }
      ],
      '/tools-ecosystem/': [
        {
          text: '工具与生态',
          items: [
            { text: '总览', link: '/tools-ecosystem/' },
            { text: 'CUDA 并行计算', link: '/tools-ecosystem/concept-cuda-parallel-computing' },
            { text: 'NVIDIA 软件生态', link: '/tools-ecosystem/concept-nvidia-software-ecosystem' },
            { text: 'NVIDIA 五大壁垒', link: '/tools-ecosystem/concept-nvidia-five-barriers' },
            { text: 'ASML EUV 光刻', link: '/tools-ecosystem/concept-asml-euv-lithography' },
            { text: 'AI 经典论文', link: '/tools-ecosystem/topic-ai-classic-papers' },
          ]
        }
      ],
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/teddyvan0831/ai-knowledge-base' },
    ],

    footer: {
      message: 'AI 知识库 — 从基础理论到行业应用的完整 AI 知识图谱',
      copyright: '内容采用 CC BY-SA 4.0 许可 | 代码采用 MIT 许可'
    },

    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: {
            displayDetails: '显示详情',
            resetButtonTitle: '重置',
            backButtonTitle: '返回',
            noResultsText: '未找到结果',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' }
          }
        }
      }
    },

    docFooter: {
      prev: '上一页',
      next: '下一页'
    },

    outline: {
      label: '页面导航',
      level: [2, 3]
    },
  },
})
