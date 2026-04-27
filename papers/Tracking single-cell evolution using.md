---
title: "Tracking single-cell evolution using"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/tracking-single-cell-evolution-using.md]
confidence: medium
year: 2022
---

# Tracking single-cell evolution using

> 原文: [[tracking-single-cell-evolution-using]]

## 摘要

DNAm-based age prediction model enabled single-cell age prediction ATAC-seq of FACS-sorted blood cells, induced pluripotent stem cell from single-cell methylation sequencing data30,31, suggesting that (iPSC) induction experiments and native immune cells showed that clock-like DNAm changes are not merely a statistical phenomenon at EpiTrace accurately predicted sample age in concordance with known the population scale but also occur at the single-cell level. developmental trajectories (Supplementary Notes and Supplementary Based on the intrinsic link between chromatin accessibility and Figs. 2–5). We then adopted the algorithm for scATAC-seq data. In brief, DNAm32–37, we hypothesized that age-dependent DNAm could either a reference ClockDML set was provided to the algorithm. ClockAcc, result from or result in chromatin accessibility changes at ClockDML. If the total chromatin accessibility on this reference ClockDML set, is so, the derived mitotic age of single cells from scATAC-seq data would measured for each cell. The measurement was performed using a hid- serve as a powerful tool to delineate developmental trajectory. In den Markov model (HMM)-mediated diffusion-smoothing approach, theory, mitotic age is a ‘timekeeper’ tracker: the mitotic age of an ances- borrowing information from similar single cells to reduce noise in the tor cell is lower than that of its progeny, and cells originating earlier in single-cell measurement: cells were clustered via correlation of top tim...

## 背景与目的

e e ll ll age Updated age 1 Updated age 2 ……. Final sc age Censor Age × loci normalization correlation Accessibility measurement Iteration HMM-based Until smoothing convergence Ranking to output Fig. 1 | ChrAcc change associated with irreversible DNAm drift on ClockDML of the human early embryonic development scATAC dataset. Color indicates enables cell age estimation. a, Schematic diagram of the underlying epigenetic the developmental stage of human embryo. f, The total chromatin accessibility mechanism of cell mitotic age tracing using ChrAcc on ClockDML. b, Correlation on ClockDML (ClockAcc), HMM-smoothened ClockAcc and initial and iterative between the DNAm level on G8-group ClockDML and sample age in human EpiTrace ranking result (EpiTrace age) corresponding to the embryonic dataset. PBMCs. 95% CI is shown as a gray area around the linear regression line. Sample numbers of biologically independent samples: n = 1 (Oocyte); 1 (Sperm); R = −0.978, P < 2.2 × 10−16. c, Enrichment of mitosis-associated ClockDML (Mitosis, 2 (Zygote); 5 (two-cell); 1 (four-cell); 6 (eight-cell); 2 (Morula); 5 (ICM); 4 (Naive size = 1,934 bp), actual age-associated ClockDML (Chronology, size = 58,7801 bp) hESC); 7 (Primed hESC); 2 (TE); and 3 (Differentiated trophoblast). The upper and solo-WCGW loci (size = 5 Mbp) in each class of ATAC peaks (size = 281 Mbp and lower bounds of boxes show 25% and 75% percentiles of the data.

## 主要发现

(GSE142745 (ref. 8)) of cultured CD34 hematopoietic stem cells (HSCs) as ‘Int-only’; and clones with both Int and Prog cells were classified as that underwent in vitro expansion for 14 d before being forced into ‘Both’ (Supplementary Fig. 25a). The mean EpiTrace age of the clones differentiation under SCF/IL3/EPO toward myeloid/erythroid lineages at the initial timepoint was measured as mean EpiTrace age of cells for an additional 6 d (Fig. 4a). These cells were sequenced at day 8 (D8), from D8 (Supplementary Fig. 25b,d). We then tracked their clonal Fig. 3 | Inferring single-cell age reversal in iPSC induction with EpiTrace. estimated with EpiTrace from f. The induced cultures were either subjected to a, Schematic overview of the in vitro chemical induction of human pluripotent the full induction paradigm (+Chem: C6NYSA + T5J) or had 5-azaC or JNKin8 stem cells (‘Primed’) back to 8-cell like cell (8CLC) state, through serially culturing removed (−5aza, −JNKin8). Sample numbers of biologically independent cells: in 4-cell-like medium (4CL, three passages (P3)) and the enhanced 4CL-medium n = 8,826 (uninduced); 4,667 (+Chem, −JNKin8); 10,257 (+Chem, −5aza); and (e4CL). b, DNAm age of D0 (day 0, Primed) and D12 (day 12, 4CL) cultures and 8,671 (+Chem stage II). Statistical comparisons are shown between groups by sorted 8CLCs from D17 (day 17) culture, from WGBS data. n = 2 independent two-sided Wilcoxon test.

## 方法概述

e NR2F1 scRNA expression f LMO3 scRNA expression 2PAMU In1 Cyc.prog In3 RG nIPC In2 GluN2 OPC GluN3 GluN5 Trajectory with EpiTrace GluN4 combined with RNA velocity and CytoTRACE UMAP1 b CytoTRACE only RNA velocity only EpiTrace age nnIIPPCC nnIIPPCC AAccttiivvee pprroolliiff.. ssiinnkk ssiinnkk nnIIPPCC 1 GGlluuNN ssaaddddllee 0 i EC/peric EpiTrace phylogeny IN1 IN2 GluN3 IN3 mGPC/OPC nIPC/GluN1 SP GluN2 GluN5 GluN4 GluN4 GluN3 GluN5 GluN2 RG nIPC/GluN1 Cyc. prog SP RG 0 0.5 1 1 0.5 0 EpiTrace age CytoTRACE epyt lleC j k ega ecarTipE P < 2.2 × 10–16 1.00 1.00 0.75 0.75 0.50 0.50 0.25 0.25 0 LMO3+ NR2F1+ LMO3+ NR2F1+ ECARTotyC High High Low Low g h P = 0.017 G yru s N R 2F1+ N R2F1+ Sulcus Early expanding maintains P N Early generated: GluN4/5 division Post mitotic maturation Late expanding switch to N N Late generated: GluN2/3 division later LMO3+ Fig. 6 | EpiTrace reveals the developmental history during human cortical and 1,198 (NR2F1+). P < 2.2 × 10−16 (Wilcoxon test, two-sided; the P value resulted gyrification. a, UMAP projected cell evolution trajectory built with CellRank in numerical underflow). h, CytoTRACE of cells belong to the LMO3+ population by using a hybrid kernel of EpiTrace, CytoTRACE and RNA velocity of an or NR2F1+ population. Sample numbers as in g. P = 0.017 (Wilcoxon test, two- scMultiomic-seq dataset from a pcw21 human brain. EC, endothelial cell; sided).

## 讨论与结论

analysis suggests an endothelial origin of kidney tubules and deline- tumor sphere cultures85, these clones coexist within the same tumor ates a cell-type-specific generation cascade during nephrogenesis and share common somatic mutations, such as deletion of PTEN and (Extended Data Fig. 1b), with correlation to their spatial position (Sup- CDKN2A84,86, indicating that they were derived from the same ancestral plementary Fig. 30). The distribution of EpiTrace age for each cell type clone. scRNA-seq87,88 suggests that PDGFRA+/EGFR+ double-positive suggests a distal-to-proximal genesis cascade of nephron tubules with cells exist in GBM. Single-positive PDGFRA+ or EGFR+ descendent clones a late expansion of proximal tubules (PTs) (Extended Data Fig. 1c). could emerge from double-positive parental clones without specific In the PT lineage, EpiTrace age-derived phylogeny could be orthog- selection86. These observations are similar to our observation with Epi- onally validated with small nuclear RNA (snRNA)-derived phylogeny Trace. In our analysis, although we sampled only a fraction of the tumor, (Supplementary Fig. 31; GSE121862 (ref. 75)). The correlation between the similar cell age estimated for MDM4+/EGFR+ and MDM4+/PDGFRA+ EpiTrace age and peak openness showed clear segregation of peaks clones suggested that neither of these clones gained selective advan- opened in progenitor or differentiated PT cells (Extended Data Fig. 1d). tage during tumor growth.

## 关键词

Tracking, evolution, single-cell, using

## 相关实体

细胞类型: erythroid, myeloid
通路: differentiation
方法: ATAC-seq, FACS, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
