---
title: "R-CNN vs YOLO：两阶段与单阶段目标检测对比"
outline: deep
---

# R-CNN vs YOLO：两阶段与单阶段目标检测对比

> **类型**: comparison
> **创建时间**: 2026-07-09
> **最后更新**: 2026-07-09
> **来源**: 
> **领域**: ai

## 摘要

目标检测算法分为 **two-stage（两阶段，R-CNN 系列）** 与 **one-stage（单阶段，YOLO/SSD 系列）** 两大范式。本文对比两者核心差异，梳理 R-CNN 三代演进（Selective Search → SPPNet → RPN）与 YOLO 各代要点，并给出原始资料中的「YOLO vs Faster R-CNN」实测对比表。其中 R-CNN 各代架构细节与 YOLOv4+ 演进在 raw 资料中未展开，属 AI 综合推理，已明确标注。

## 详情

### 一、两大范式：two-stage vs one-stage

目标检测算法按流程分为两类 ：

- **two-stage（两阶段）**：基于 Region Proposal 的 R-CNN 系列（R-CNN、Fast R-CNN、Faster R-CNN）。需先使用启发式方法（**selective search**）或 CNN 网络（**RPN**）产生 Region Proposal，再在候选区域上做分类与回归 。
- **one-stage（单阶段）**：YOLO、SSD 等，只使用一个 CNN 网络直接预测目标的类别与位置 。

> **核心取舍**：Two-stage 方法准确度高一些，但速度慢；one-stage 算法速度快，但准确性低一些 。

### 二、R-CNN 系列三代演进

> 🤖 **AI 综合推理（外部通用知识）**：本节 R-CNN 各代的具体架构、年份与论文归属在 raw 原始资料中仅以 "selective search / RPN" 关键词提及，未展开。以下演进脉络属外部通用计算机视觉知识，**关键年份与论文归属建议人工核验**。

| 代际 | 年份 / 会议 | 候选区域机制 | 核心改进 | 遗留痛点 |
|------|-------------|-------------|----------|----------|
| **R-CNN** | 2014, CVPR（Girshick et al.） | **Selective Search**（启发式，约 2000 候选框） | 每张候选框独立过 CNN（AlexNet）提特征 → SVM 分类 + 边框回归 | 训练多阶段、速度极慢、候选框重复计算 |
| **Fast R-CNN** | 2015, ICCV（Girshick） | 仍依赖外部候选（Selective Search） | 整图一次 CNN 得特征图，**RoI Pooling** 从特征图截取候选区域，单阶段端到端训练 | 候选区域生成仍是速度瓶颈 |
| **Faster R-CNN** | 2015, NeurIPS（Ren et al., Microsoft） | **RPN（Region Proposal Network）** 替代 Selective Search | RPN 与检测网络共享卷积特征，端到端 two-stage | 两阶段串行，速度仍不及 one-stage |

- 演进主线即**候选区域生成机制的进化**：`Selective Search（手工启发）→ SPPNet 的空间金字塔池化思想（奠定 Fast R-CNN 的 RoI 思路）→ RPN（网络自动生成）`。
- 知识库中已确认的论文条目：**Faster R-CNN — Ren et al. (Microsoft), 2015, NeurIPS** [AI 经典论文汇览](/tools-ecosystem/topic-ai-classic-papers) → 。

### 三、YOLO 各代要点

**YOLO（You Only Look Once）**：只需一次 CNN 运算，把检测变为回归问题 。

发展沿革（原始资料 ）：

| 版本 | 特点 |
|------|------|
| YOLOv1 | 奠定基础，one-stage 检测 |
| YOLOv2 | 引入 Anchor Box |
| YOLOv3 | 多尺度预测 |
| YOLOv4-v12 | 社区持续改进 |

**YOLOv1 核心原理** ：
- 图片划分为 S×S 网格（v1 为 7×7），每 Grid 预测 B 个 Bounding Box，每 Box 输出 5 值 (x, y, w, h, confidence)，每 Grid 预测 C 类概率，输出维度 `S × S × (B × 5 + C)`。
- 速度 45–155 FPS，mAP 63.4%（Fast YOLO 52.7%）。
- 局限：每个 Grid 最多预测一个物体，密集小物体场景不适用 。

**YOLOv3 改进**（原始资料 ）：
- 多尺度预测：13×13、26×26、52×52
- 先验框适配：通过 k-means 聚类计算
- 每个单元格预测：`3 × (4 + 1 + B)` 个值

> 🤖 **AI 综合推理（外部通用知识）**：YOLOv4（2020, Bochkovskiy et al.）引入 CSPDarknet、PANet、CIoU；YOLOv5 起由 Ultralytics 以 PyTorch 维护；后续 v6/v7（2022）/v8（2023）/v9/v10/v11/v12 由社区持续改进，陆续加入解耦头、Anchor-Free、端到端等设计。原始资料仅以 "v4-v12 社区持续改进" 概括，未展开，**建议人工核验各代细节**。

### 四、R-CNN（Faster R-CNN）vs YOLO 核心对比

以下为原始资料直接给出的实测对比表 ：

| 特性 | YOLO | Faster R-CNN |
|------|------|--------------|
| 类型 | One-stage | Two-stage |
| 速度 | 快（45–155 FPS） | 慢（7–18 FPS） |
| 精度 | 中等（mAP 63–70%） | 高（mAP 70–73%） |
| 适用场景 | 实时检测、边缘计算 | 高精度要求 |

> 工业缺陷检测选型建议：YOLO（速度）vs Faster R-CNN（精度）。

## 可视化

> 以下三张图为本文内容的可视化附件，均为**自包含 SVG**（硬编码调色板、无外部 CSS/JS 依赖），可在 Obsidian 阅读模式与 VitePress 站点直接渲染。数据来源同上方正文与引用。

### 图1 · two-stage vs one-stage 流程对比

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 390" width="100%" role="img" aria-label="Two-stage versus one-stage object detection pipeline">
<defs>
<marker id="arr1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="#5F5E5A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</marker>
</defs>
<line x1="180" y1="94" x2="180" y2="128" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr1)"/>
<line x1="180" y1="186" x2="180" y2="218" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr1)"/>
<line x1="180" y1="276" x2="180" y2="318" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr1)"/>
<line x1="500" y1="94" x2="500" y2="128" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr1)"/>
<line x1="500" y1="186" x2="500" y2="318" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr1)"/>
<text x="180" y="26" text-anchor="middle" font-size="14" font-weight="500" fill="#3C3489">Two-stage · R-CNN 系列</text>
<text x="500" y="26" text-anchor="middle" font-size="14" font-weight="500" fill="#085041">One-stage · YOLO 系列</text>
<rect x="90" y="50" width="180" height="44" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="180" y="72" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#2C2C2A">输入图像</text>
<rect x="70" y="130" width="220" height="56" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="180" y="148" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#2C2C2A">Region Proposal</text>
<text x="180" y="166" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#5F5E5A">Selective Search / RPN</text>
<rect x="70" y="220" width="220" height="56" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="180" y="238" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#2C2C2A">逐候选框分类 + 回归</text>
<text x="180" y="256" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#5F5E5A">每个框独立前向</text>
<rect x="90" y="320" width="180" height="44" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="180" y="342" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#2C2C2A">输出: 类别 + 框</text>
<rect x="410" y="50" width="180" height="44" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
<text x="500" y="72" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#2C2C2A">输入图像</text>
<rect x="390" y="130" width="220" height="56" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
<text x="500" y="148" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#2C2C2A">单 CNN 直接回归</text>
<text x="500" y="166" text-anchor="middle" dominant-baseline="central" font-size="12" fill="#5F5E5A">网格划分 + 置信度</text>
<rect x="410" y="320" width="180" height="44" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
<text x="500" y="342" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="500" fill="#2C2C2A">输出: 类别 + 框</text>
<text x="340" y="195" text-anchor="middle" font-size="14" font-weight="500" fill="#5F5E5A">VS</text>
<text x="340" y="215" text-anchor="middle" font-size="12" fill="#888780">准确↑ 慢</text>
<text x="340" y="233" text-anchor="middle" font-size="12" fill="#888780">快 精度↓</text>
</svg>

### 图2 · R-CNN 与 YOLO 演进时间线

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 345" width="100%" role="img" aria-label="R-CNN and YOLO evolution timeline">
<defs>
<marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="#5F5E5A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</marker>
</defs>
<line x1="180" y1="108" x2="180" y2="128" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr2)"/>
<line x1="180" y1="178" x2="180" y2="198" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr2)"/>
<line x1="500" y1="108" x2="500" y2="128" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr2)"/>
<line x1="500" y1="178" x2="500" y2="198" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr2)"/>
<line x1="500" y1="248" x2="500" y2="268" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arr2)"/>
<text x="180" y="34" text-anchor="middle" font-size="14" font-weight="500" fill="#3C3489">R-CNN 家族 (two-stage)</text>
<text x="500" y="34" text-anchor="middle" font-size="14" font-weight="500" fill="#085041">YOLO 家族 (one-stage)</text>
<rect x="80" y="60" width="200" height="48" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="180" y="80" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="500" fill="#2C2C2A">2014 · R-CNN</text>
<text x="180" y="98" text-anchor="middle" dominant-baseline="central" font-size="11" fill="#5F5E5A">Selective Search + SVM</text>
<rect x="80" y="130" width="200" height="48" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="180" y="150" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="500" fill="#2C2C2A">2015 · Fast R-CNN</text>
<text x="180" y="168" text-anchor="middle" dominant-baseline="central" font-size="11" fill="#5F5E5A">RoI Pooling 共享卷积</text>
<rect x="80" y="200" width="200" height="48" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="180" y="220" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="500" fill="#2C2C2A">2015 · Faster R-CNN</text>
<text x="180" y="238" text-anchor="middle" dominant-baseline="central" font-size="11" fill="#5F5E5A">RPN 替代候选框 (推理)</text>
<rect x="400" y="60" width="200" height="48" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
<text x="500" y="80" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="500" fill="#2C2C2A">2015 · YOLOv1</text>
<text x="500" y="98" text-anchor="middle" dominant-baseline="central" font-size="11" fill="#5F5E5A">7×7 网格回归</text>
<rect x="400" y="130" width="200" height="48" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
<text x="500" y="150" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="500" fill="#2C2C2A">2016 · YOLOv2</text>
<text x="500" y="168" text-anchor="middle" dominant-baseline="central" font-size="11" fill="#5F5E5A">Anchor Box</text>
<rect x="400" y="200" width="200" height="48" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
<text x="500" y="220" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="500" fill="#2C2C2A">2018 · YOLOv3</text>
<text x="500" y="238" text-anchor="middle" dominant-baseline="central" font-size="11" fill="#5F5E5A">多尺度 13/26/52</text>
<rect x="400" y="270" width="200" height="48" rx="8" fill="#9FE1CB" stroke="#0F6E56" stroke-width="0.5"/>
<text x="500" y="290" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="500" fill="#2C2C2A">2020+ · v4–v12 (推理)</text>
<text x="500" y="308" text-anchor="middle" dominant-baseline="central" font-size="11" fill="#5F5E5A">社区改进</text>
</svg>

### 图3 · 性能对比（速度 / mAP，取自 notes-10#L612）

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 430" width="100%" role="img" aria-label="YOLO vs Faster R-CNN performance: speed and mAP">
<text x="40" y="24" font-size="14" font-weight="500" fill="#2C2C2A">推理速度 (FPS，越高越快)</text>
<line x1="120" y1="180" x2="560" y2="180" stroke="#5F5E5A" stroke-width="0.5"/>
<rect x="170" y="44" width="90" height="136" fill="#1D9E75"/>
<rect x="420" y="164" width="90" height="16" fill="#534AB7"/>
<text x="215" y="34" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A">YOLO</text>
<text x="465" y="154" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A">Faster R-CNN</text>
<text x="215" y="200" text-anchor="middle" font-size="11" fill="#5F5E5A">45–155 FPS</text>
<text x="465" y="200" text-anchor="middle" font-size="11" fill="#5F5E5A">7–18 FPS</text>
<text x="40" y="244" font-size="14" font-weight="500" fill="#2C2C2A">mAP (%)，越高越准</text>
<line x1="120" y1="400" x2="560" y2="400" stroke="#5F5E5A" stroke-width="0.5"/>
<rect x="170" y="301" width="90" height="99" fill="#1D9E75"/>
<rect x="420" y="294" width="90" height="106" fill="#534AB7"/>
<text x="215" y="291" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A">YOLO</text>
<text x="465" y="284" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A">Faster R-CNN</text>
<text x="215" y="420" text-anchor="middle" font-size="11" fill="#5F5E5A">63–70%</text>
<text x="465" y="420" text-anchor="middle" font-size="11" fill="#5F5E5A">70–73%</text>
<text x="115" y="414" font-size="10" fill="#888780">0</text>
<text x="555" y="414" font-size="10" fill="#888780">100</text>
<text x="120" y="430" font-size="10" fill="#888780">* 柱高取范围中值示意（速度 YOLO≈100 / Faster≈12 FPS；mAP YOLO≈66 / Faster≈71%）。真实范围见柱下标签。来源：notes-10#L612</text>
</svg>

## 关联

- 相关概念: [视觉检测与视觉大模型在工业质检中的应用](/multimodal/concept-vision-quality-inspection)、[视觉识别技术](/multimodal/concept-vision-recognition)
- 参见: [AI 经典论文汇览](/tools-ecosystem/topic-ai-classic-papers)（含 Faster R-CNN / YOLOv1 / YOLOv3 论文条目）

## 引用来源

- [1]  — two-stage/one-stage 分类、YOLO 发展史与原理、YOLO vs Faster R-CNN 对比表（L126-L139, L142-L227, L612-L625）
- [2] [AI 经典论文汇览](/tools-ecosystem/topic-ai-classic-papers) — Faster R-CNN 论文条目（Ren et al., 2015, NeurIPS）
- [3] 🤖 AI 综合推理（外部通用计算机视觉知识，非 raw 来源）— R-CNN / Fast / Faster 各代架构与年份、YOLOv4+ 社区演进细节；**建议人工核验关键年份与论文归属**

## 变更记录

- 2026-07-09: 初始创建，来源  + AI 综合推理补充 R-CNN 三代演进与 YOLO 各代要点
- 2026-07-09: 嵌入三张自包含 SVG 可视化（图1 流程对比 / 图2 演进时间线 / 图3 性能条形图），去除 WorkBuddy 宿主 CSS 变量与外部 JS 依赖，适配 Obsidian 阅读模式与 VitePress 渲染
