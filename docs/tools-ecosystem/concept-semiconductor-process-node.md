---
title: "半导体制程节点：三星 8nm vs 台积电 4nm 与「等效 Xnm」对照"
outline: deep
---

# 半导体制程节点：三星 8nm vs 台积电 4nm 与「等效 Xnm」对照

> **类型**: concept
> **创建时间**: 2026-07-19
> **最后更新**: 2026-07-19
> **来源**: 
> **领域**: ai

## 摘要
代工厂节点数字（如"8nm""4nm"）是**营销标签，不对应真实物理尺寸**，且各厂独立命名、无统一标准（ITRS 2016 解散后由 IRDS 做预测但不强制）。三星 8nm(8LPP) 本质是 10nm 改良半节点（DUV+FinFET，密度 55–65 MTr/mm²），比台积电 4nm(N4/N4P，EUV+FinFET，密度 170–180 MTr/mm²) 落后约两个整节点、密度差 2–3 倍——典型"节点数字不可信"案例。跨厂比较必须用**晶体管密度**对齐成"等效 Xnm"。该维度是 Orin(8nm 三星) vs Thor(4nm 台积电) 代差的根因之一。

## 详情

### 8nm 三星 vs 4nm 台积电：差整整一代
- **三星 8nm(8LPP)**：10nm 改良半节点，DUV(193nm 浸没式)+FinFET，2018–2019 量产，密度约 55–65 MTr/mm²，属"10nm 级别"。
- **台积电 4nm(N4/N4P)**：5nm(N5) 再收缩，全面 EUV(13.5nm)+FinFET（N4 是 FinFET 绝唱，N2 才上 GAA 纳米片），2021–2022 量产，密度约 170–180 MTr/mm²。
- 结论：三星 8nm 比台积电 4nm 落后约两整节点，密度差 2–3 倍，能效明显更弱。

### 代工阵营全景
按"能走到多先进"分三档：

| 梯队 | 厂商 | 先进节点进展 |
|------|------|------------|
| **第一梯队(先进)** | TSMC 台积电 | N3/N2(GAA)，公认领先 |
| | Samsung 三星 | 4nm、3nm GAA（首发 GAA，早期良率/密度吃亏） |
| | Intel 英特尔(IFS) | Intel 4、20A/18A（Å 命名，RibbonFET GAA） |
| **第二梯队(受限先进)** | SMIC 中芯国际 | 14nm、7nm(N+1/N+2，**无 EUV**，靠 DUV 多重曝光) |
| **成熟/特色** | GF、UMC、华虹、Tower、力积电、Rapidus | 止步 12–28nm，专攻车规/RF/嵌入式/功率 |

> 关键关系：这些厂是"竞争关系"非"标准制定者"，无机构规定"8nm 必须等于某尺寸"；各起各的节点名，设计不能直接跨厂移植（独立 PDK/标准单元库/IP）。

### 「等效 Xnm」：把营销标签翻译成真实指标
> 🖼️ [图1] 半导体代工厂节点命名对照 — TSMC/Samsung/Intel/SMIC/其他(GF/UMC/华虹)各自独立节点命名（N7/N6、8LPP、Intel 7、14nm…），节点数字已与栅长脱钩，跨厂命名无统一标准，必须用密度/性能对齐后再比 — 

节点数字失真：≥130nm 时≈栅长/半间距（真实物理量）；28nm 之后纯属各家营销代号。比较只能换尺子：
- **晶体管密度(MTr/mm²)** —— 最硬指标。三星 8LPP≈55–65｜台积电 N7≈91｜N5≈173｜N4≈180；三星 4LPE≈130–150(≈台积电 N7+/N6，≠N4)；Intel 7≈100(≈N7)｜Intel 4≈160–200(≈N5/N4)。
- **同功耗性能、能效比**、**SRAM 密度、良率成熟度**。

> 🖼️ [图2] 等效 Xnm 跨厂映射 — 按密度/性能对齐：三星 8nm≈台积电 10/12nm 级；三星 4nm(4LPE)≈台积电 5nm 级(**非 4nm!**)；Intel 7≈台积电 7nm；Intel 4≈台积电 5/4nm；SMIC N+1 自称"等效 7nm"实为 10nm 级 — 

最典型"等效"误读：SMIC N+1 自称"等效 7nm"实为 10nm 级（无 EUV，DUV 多重曝光锁死密度天花板）。"等效"既是技术对标，也可能是宣传话术。

### EUV vs DUV 与 Å(埃)命名
- **EUV vs DUV 是真正分水岭**：DUV(193nm) 做 7nm 以下靠多重曝光，成本高、良率难；EUV(13.5nm) 才能干净往下走。三星 8nm 用 DUV；台积电 5/4nm、三星/Intel 先进节点用 EUV；**无 EUV 阵营(SMIC)卡在 7nm 级**。
- **Nnm 正被 Å 取代**：Intel 率先改 20Å=2nm、18Å=1.8nm(RibbonFET GAA)；台积电把 1.6nm 叫 A16。未来看到"18A"而非"1.8nm"。

### 做芯片对比的三条铁律
1. 别看节点数字比大小，先看晶体管密度(MTr/mm²)。
2. 跨厂必须"等效对齐"：三星 8nm≈台积电 10/12nm，三星 4nm≈台积电 5nm，Intel 7≈台积电 7nm。
3. 制程只是其一，还要看架构、内存带宽、良率成熟度——正如 Orin(三星 8nm) vs Thor(台积电 4nm) 那种代差。

## 关联
- 相关概念: [NVIDIA Jetson Orin 与 Thor 全系对照（跨代归一化）](/inference-deploy/concept-nvidia-jetson-orin-thor)（Orin 8nm 三星 / Thor 4nm 台积电的直接落点）、[算力口径方法论：单位 × 精度 × 计算模式](/base-models/concept-ai-compute-caliber)（制程是算力之外的另一不可比维度）、[ARM 处理器 IP 全谱系与车规 CPU 对比（A78AE vs V3AE）](/base-models/concept-arm-cpu-ip-lineage)
- 参见: [ASML EUV 光刻机与芯片制造瓶颈](/tools-ecosystem/concept-asml-euv-lithography)（EUV 光刻设备）、[concept-edge-ai-architecture-evolution](/base-models/concept-edge-ai-architecture-evolution)

## 引用来源
- [1]  — 8nm vs 4nm 代差、代工阵营、等效 Xnm、EUV/DUV、Å 命名
- [2]  — Orin 8nm / Thor 4nm 制程对照 corroboration

## 变更记录
- 2026-07-19: 初始创建，来源 
