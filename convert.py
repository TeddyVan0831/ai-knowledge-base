"""
AI 知识库 → VitePress 转换脚本 (v2.0)
适配统一知识库架构：从多域 wiki 中仅提取 domain:ai 的页面
按技术领域重组到 9 个主题域
"""
import os
import re
import shutil
from pathlib import Path
from collections import defaultdict

# ============ 配置 ============
WIKI_ROOT = r"C:\Users\vanem\OneDrive\应用\remotely-save\Obsidian LLM WIKI Vault\统一知识库"
TARGET_ROOT = r"D:\TeddyWorkshop\WorkBuddy\ai-knowledge-base\docs"
TARGET_DOMAIN = "ai"  # 只发布 AI 域

# ============ 跳过页（库内索引/已合并页，不发布到站点） ============
SKIP_PAGES = {
    "concept-mcp-protocol",  # 已合并到 concept-mcp
    "model-qwen3",           # 已合并到 model-qwen3-embedding
    "ai-home",               # 域主页（Obsidian 内部索引，非读者内容）
}

# ============ 领域映射表（AI 域内 9 个子域） ============
DOMAIN_MAP = {
    # base-models: Transformer, Embedding, 训练范式, LLM 演进, 推理模型, GPU硬件, 嵌入模型实体
    "base-models": [
        "concept-transformer-architecture", "concept-embedding", "concept-word2vec",
        "concept-cosine-similarity", "concept-llm-history", "concept-llm-training-paradigm",
        "concept-reasoning-models", "concept-reasoning-models-deepseek-r1",
        "concept-embedding-model-selection", "concept-in-context-learning",
        "concept-few-shot-prompting", "concept-reasoning-techniques",
        "concept-bayesian-reasoning", "concept-llm-wiki",
        "concept-category-theory-llm",
        "model-h100", "model-b200", "model-rtx4090",
        "model-qwen3-embedding", "model-jina-embedding", "model-bge-m3",
        "company-deepseek", "company-openai", "company-anthropic",
        "company-google", "company-meta",
        "concept-deepseek-v4", "concept-ascend-ecosystem",
        "concept-atlas-superpod", "company-huawei",
    ],
    # architecture: MoE, 注意力优化, KV Cache, 解码加速
    "architecture": [
        "concept-deepseek-moe", "concept-mla-multi-head-latent-attention",
        "concept-mtp-multi-token-prediction", "concept-loss-free-load-balancing",
        "concept-fp8-mixed-precision", "concept-attention-optimization",
        "concept-kv-cache", "concept-kv-cache-compression",
        "concept-kv-cache-quantization", "concept-speculative-decoding",
        "concept-dflash-v2", "concept-ttft-optimization", "concept-vram-calculation",
        "concept-csa-hca-attention",
    ],
    # training-optimization: 微调, 量化, 剪枝, 蒸馏, RLHF, WebRL
    "training-optimization": [
        "concept-llm-fine-tuning", "concept-quantization-ptq",
        "concept-quantization-rotation", "concept-model-pruning",
        "concept-knowledge-distillation", "concept-rlhf",
        "concept-webrl", "concept-orm-reward-model",
    ],
    # inference-deploy: 部署, 高并发, 框架选择, 边缘推理, SGLang, OpenClaw
    "inference-deploy": [
        "concept-enterprise-ai-deployment", "concept-high-concurrency-ai",
        "concept-sglang-optimization", "concept-openclaw-hermes",
        "concept-ai-framework-selection", "concept-llamacpp",
        "concept-mediapipe-llm", "concept-mnn",
        "product-vllm", "product-sglang", "product-langchain",
        "product-openclaw", "product-hermes", "product-faiss",
        "concept-llm-edge-inference", "concept-ascend-deployment",
    ],
    # agent: Agent 设计模式, 评估, MCP, AutoGLM, 安全
    "agent": [
        "concept-agent-controllability", "concept-agent-taxonomy",
        "concept-context-engineering", "concept-agent-ops",
        "concept-mcp", "concept-agent-evaluation",
        "concept-agent-interoperability", "concept-prompt-chaining",
        "concept-agent-routing", "concept-parallelization",
        "concept-reflection", "concept-tool-use",
        "concept-function-calling", "concept-human-in-the-loop",
        "concept-multi-agent-collaboration", "concept-agent-planning",
        "concept-agent-memory", "concept-agent-learning",
        "concept-goal-management", "concept-error-recovery",
        "concept-safety-guardrails", "concept-resource-optimization",
        "concept-agent-optimization", "concept-a2a-communication",
        "concept-deep-agent", "concept-langchain-chain-types",
        "concept-autoglm",
        # Harness 工程簇 + Agent 案例 + 生命周期
        "concept-harness-engineering", "concept-harness-coverage-levels",
        "concept-harness-four-questions", "concept-agent-task-lifecycle",
        "case-anthropic-long-running-agent", "case-openai-agent-first-warehouse",
        "case-swe-agent-aci-experiment",
        "concept-claude-code-agent", "concept-agent-loop",
    ],
    # rag: RAG 基础, 高级检索, Agentic RAG, 分块策略
    "rag": [
        "concept-rag", "concept-rag-advanced-retrieval",
        "concept-agentic-rag", "concept-chunking-strategy",
        "concept-query-rewriting", "concept-text-to-sql",
    ],
    # multimodal: 视觉, 图像/视频生成, 数字人, MAE
    "multimodal": [
        "concept-multimodal-transformer", "concept-multimodal-edge",
        "concept-vision-quality-inspection", "concept-vision-recognition",
        "concept-image-generation", "concept-video-generation",
        "concept-meta-sapiens", "concept-mae-masked-autoencoder",
        "concept-humans-300m-dataset", "concept-digital-human",
        "concept-ai-video-workflow", "comparison-rcnn-vs-yolo",
    ],
    # industry-cases: 行业应用案例
    "industry-cases": [
        "concept-ai-education-cases", "concept-ai-table-recognition-evaluation",
        "concept-live-streaming-ai-assistant", "concept-ai-training-agent",
    ],
    # tools-ecosystem: CUDA, GPU 生态, ASML, 经典论文
    "tools-ecosystem": [
        "concept-cuda-parallel-computing", "concept-nvidia-software-ecosystem",
        "concept-nvidia-five-barriers", "concept-asml-euv-lithography",
        "concept-ai-api-protocols",
    ],
}

# Topic pages mapping
TOPIC_DOMAIN_MAP = {
    "topic-agent-development": "agent",
    "topic-agentic-design-patterns": "agent",
    "topic-rag-optimization": "rag",
    "topic-model-optimization": "training-optimization",
    "topic-ai-deployment-ops": "inference-deploy",
    "topic-edge-inference": "inference-deploy",
    "topic-ai-classic-papers": "tools-ecosystem",
    "topic-ai-industry-applications": "industry-cases",
    "topic-harness-engineering-2026": "agent",
    "topic-agent-architecture-2026": "agent",
}

# Build reverse map: page_name → domain
PAGE_DOMAIN = {}
for domain, pages in DOMAIN_MAP.items():
    for p in pages:
        PAGE_DOMAIN[p] = domain
for topic, domain in TOPIC_DOMAIN_MAP.items():
    PAGE_DOMAIN[topic] = domain


# ============ v2.0 新增：域过滤 ============
def read_page_domain(md_path):
    """从页面内容中提取 `> **领域**: xxx` 标签"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                m = re.match(r'>\s*\*\*领域\*\*\s*:\s*(\S+)', line)
                if m:
                    return m.group(1).strip()
    except:
        pass
    return None


# ============ 原有函数（微调） ============

def get_clean_name(filename):
    """Extract kebab-case name without .md"""
    return Path(filename).stem


def get_page_title(md_path):
    """Read the first # heading from a markdown file"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# ') and not line.startswith('## '):
                    return line[2:].strip()
    except:
        pass
    return None


def get_page_metadata(md_path):
    """Extract metadata line (type, created date) from file"""
    metadata = {"type": "unknown", "created": ""}
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                m = re.match(r'>\s*\*\*类型\*\*:\s*(\w+)', line)
                if m:
                    metadata["type"] = m.group(1)
                m = re.match(r'>\s*\*\*创建时间\*\*:\s*([-\d]+)', line)
                if m:
                    metadata["created"] = m.group(1)
    except:
        pass
    return metadata


def load_all_titles(wiki_root):
    """Build a mapping of page_name → page_title (only AI domain pages)"""
    titles = {}
    concepts_dir = os.path.join(wiki_root, "wiki", "concepts")
    entities_dir = os.path.join(wiki_root, "wiki", "entities")
    topics_dir = os.path.join(wiki_root, "wiki", "topics")
    
    for d in [concepts_dir, entities_dir, topics_dir]:
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if not f.endswith('.md'):
                continue
            name = get_clean_name(f)
            fpath = os.path.join(d, f)
            
            # v2.0: only load AI domain pages into title index
            page_domain = read_page_domain(fpath)
            if page_domain != TARGET_DOMAIN:
                continue
            
            title = get_page_title(fpath)
            if title:
                titles[name] = title
    return titles


def convert_wikilinks(content, titles, page_domain, source_name):
    """Convert Obsidian [[wikilinks]] to standard Markdown links"""
    
    def replace_wikilink(match):
        full = match.group(1)  # full content inside [[ ]]
        parts = full.split('|')
        target = parts[0].strip()
        display = parts[1].strip() if len(parts) > 1 else None
        
        if target.startswith('raw/'):
            # Raw references become simple footnotes - remove from output
            return ''
        
        # Extract page name
        if '/' in target:
            path_parts = target.split('/')
            page_name = path_parts[-1].replace('.md', '')
        else:
            page_name = target.replace('.md', '')
        
        # Skip non-content references
        if page_name in ['index']:
            return ''
        
        domain = page_domain.get(page_name, 'base-models')
        link_display = display if display else titles.get(page_name, page_name)
        link_path = f"/{domain}/{page_name}"
        
        return f"[{link_display}]({link_path})"
    
    content = re.sub(r'\[\[(wiki/[^\]]+|raw/[^\]]+)\]\]', replace_wikilink, content)
    content = re.sub(r'\[\[(concept-[^\]]+|topic-[^\]]+|model-[^\]]+|product-[^\]]+)\]\]', replace_wikilink, content)
    
    return content


def clean_content_for_vitepress(content):
    """Clean Obsidian-specific formatting for VitePress"""
    lines = content.split('\n')
    result = []
    in_frontmatter = False
    frontmatter_end = False
    skip_block = False
    
    for line in lines:
        if line.strip() == '---' and not frontmatter_end:
            if not in_frontmatter:
                in_frontmatter = True
                skip_block = True
                continue
            else:
                in_frontmatter = False
                frontmatter_end = True
                skip_block = False
                continue
        
        if skip_block:
            continue
        
        # Keep metadata lines
        if line.startswith('> **') or line.startswith('> **领域**'):
            result.append(line)
            continue
        
        result.append(line)
    
    return '\n'.join(result)


def add_vitepress_frontmatter(content, title, domain):
    """Add VitePress frontmatter"""
    fm = f"""---
title: "{title.replace('"', "'")}"
outline: deep
---

"""
    return fm + content


def convert_page(src_path, dst_path, titles, page_domain, domain, source_name):
    """Convert a single wiki page to VitePress format"""
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = clean_content_for_vitepress(content)
    content = convert_wikilinks(content, titles, page_domain, source_name)
    title = get_page_title(src_path) or source_name
    content = add_vitepress_frontmatter(content, title, domain)
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return title


# ============ v2.0 新增：域过滤列表构建 ============
def build_ai_page_set(wiki_root):
    """扫描所有 wiki 页面，返回 domain:ai 的页面名集合"""
    ai_pages = set()
    for subdir in ["concepts", "entities", "topics"]:
        dir_path = os.path.join(wiki_root, "wiki", subdir)
        if not os.path.isdir(dir_path):
            continue
        for f in os.listdir(dir_path):
            if not f.endswith('.md'):
                continue
            name = get_clean_name(f)
            fpath = os.path.join(dir_path, f)
            page_domain = read_page_domain(fpath)
            if page_domain == TARGET_DOMAIN:
                ai_pages.add(name)
    return ai_pages


def main():
    print("=== 统一知识库 → VitePress 转换脚本 v2.0 ===")
    print(f"源: {WIKI_ROOT}")
    print(f"目标: {TARGET_ROOT}")
    print(f"目标域: {TARGET_DOMAIN}")
    
    # v2.0: Build set of AI-domain page names
    ai_pages = build_ai_page_set(WIKI_ROOT)
    print(f"\n🔍 扫描到 {len(ai_pages)} 个 AI 域页面")
    
    # Load titles (only AI domain)
    titles = load_all_titles(WIKI_ROOT)
    print(f"📖 加载了 {len(titles)} 个页面标题")

    # ============ 未映射页自检（固化：防止新页静默落入 base-models） ============
    mapped = set(PAGE_DOMAIN.keys())
    unmapped = sorted(ai_pages - mapped - SKIP_PAGES)
    if unmapped:
        print(f"\n⚠️ 警告：发现 {len(unmapped)} 个 AI 域页面未登记进 DOMAIN_MAP，"
              f"将被默认丢进 base-models/（分类不准）！")
        print("   建议在 convert.py 的 DOMAIN_MAP / TOPIC_DOMAIN_MAP 中补充：")
        for name in unmapped:
            print(f"   • {name}  —  {titles.get(name, '(无标题)')}")
        print("   （已合并/索引类页面可加入 SKIP_PAGES 跳过发布）")
    else:
        print("✅ 自检通过：所有 AI 域页面均已映射，无未分类页。")

    domain_count = defaultdict(int)
    skipped_count = 0
    
    # Convert concept pages
    concepts_dir = os.path.join(WIKI_ROOT, "wiki", "concepts")
    for f in sorted(os.listdir(concepts_dir)):
        if not f.endswith('.md'):
            continue
        name = get_clean_name(f)
        
        if name not in ai_pages:
            skipped_count += 1
            continue
        
        if name in SKIP_PAGES:
            continue
        
        domain = PAGE_DOMAIN.get(name, 'base-models')
        src = os.path.join(concepts_dir, f)
        dst = os.path.join(TARGET_ROOT, domain, f"concept-{name.replace('concept-', '')}.md")
        
        convert_page(src, dst, titles, PAGE_DOMAIN, domain, name)
        domain_count[domain] += 1
        print(f"  ✅ {domain:25s} ← {name}")
    
    # Convert entity pages
    entities_dir = os.path.join(WIKI_ROOT, "wiki", "entities")
    for f in sorted(os.listdir(entities_dir)):
        if not f.endswith('.md'):
            continue
        name = get_clean_name(f)
        
        if name not in ai_pages:
            skipped_count += 1
            continue
        
        if name in SKIP_PAGES:
            continue
        
        domain = PAGE_DOMAIN.get(name, 'base-models')
        src = os.path.join(entities_dir, f)
        dst = os.path.join(TARGET_ROOT, domain, f"{name}.md")
        
        convert_page(src, dst, titles, PAGE_DOMAIN, domain, name)
        domain_count[domain] += 1
        print(f"  ✅ {domain:25s} ← {name}")
    
    # Convert topic pages
    topics_dir = os.path.join(WIKI_ROOT, "wiki", "topics")
    for f in sorted(os.listdir(topics_dir)):
        if not f.endswith('.md'):
            continue
        name = get_clean_name(f)
        
        if name not in ai_pages:
            skipped_count += 1
            continue
        
        if name in SKIP_PAGES:
            continue
        
        domain = TOPIC_DOMAIN_MAP.get(name, 'base-models')
        src = os.path.join(topics_dir, f)
        dst = os.path.join(TARGET_ROOT, domain, f"{name}.md")
        
        convert_page(src, dst, titles, PAGE_DOMAIN, domain, name)
        domain_count[domain] += 1
        print(f"  ✅ {domain:25s} ← {name} (topic)")
    
    print(f"\n=== 统计 ===")
    total = sum(domain_count.values())
    for d in sorted(domain_count.keys()):
        print(f"  {d}: {domain_count[d]} 页")
    print(f"  合计: {total} 页")
    if skipped_count > 0:
        print(f"  跳过 (非 AI 域): {skipped_count} 页")
    print("\n✅ 转换完成!")


if __name__ == "__main__":
    main()
