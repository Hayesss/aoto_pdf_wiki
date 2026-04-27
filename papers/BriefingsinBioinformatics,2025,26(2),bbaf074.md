---
marker_extracted: true
title: "BriefingsinBioinformatics,2025,26(2),bbaf074"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/briefingsinbioinformatics2025262bbaf074.md]
confidence: medium
year: 2025
---

# BriefingsinBioinformatics,2025,26(2),bbaf074

> 原文: [[briefingsinbioinformatics2025262bbaf074]]

## 摘要

**Motivation:** The 3D organization of the genome plays a crucial role in various biological processes. Hi-C technology is widely used to investigate chromosome structures by quantifying 3D proximity between genomic regions. While numerous computational tools exist for detecting differences in Hi-C data between conditions, a comprehensive review and benchmark comparing their effectiveness is lacking. **Results:** This study offers a comprehensive review and benchmark of 10 generic tools for differential analysis of Hi-C matrices at the interaction count level. The benchmark assesses the statistical methods, usability, and performance (in terms of precision and power) of these tools, using both real and simulated Hi-C data. Results reveal a striking variability in performance among the tools, highlighting the substantial impact of preprocessing filters and the difficulty all tools encounter in effectively controlling the false discovery rate across varying resolutions and chromosome sizes. **Availability:** The complete benchmark is available at [https://](https://forgemia.inra.fr/scales/replication-chrocodiff) [forgemia.inra.fr/scales/replication-chrocodiff](https://forgemia.inra.fr/scales/replication-chrocodiff) using processed data deposited at [https://doi.org/10.57745/LR0W9R.](https://doi.org/10.57745/LR0W9R) **Contact:** [nathalie.](nathalie.vialaneix@inrae.fr) [vialaneix@inrae.fr](nathalie.vialaneix@inrae.fr)

**Keywords**: Hi-C; differential analysis; statistical tests; benchmark


## 背景与目的

Chromosomes are highly compacted within the cell nucleus, resulting in the spatial proximity of linearly distant genomic positions [[1\]](#page-14-0). Hi-C [] is a widely used technology to profile the 3D organization of the genome. It does so by estimating the spatial proximity between pairs of genomic positions through their frequency of interaction. The typical output of a Hi-C experiment, after preliminary data preprocessing, is usually summarized as a symmetric matrix of counts, where the entry *(i*, *j)* (or *(j*, *i)*) corresponds to the number of interactions registered during the Hi-C experiment between genomic regions ("bins") *i* and *j*. Hi-C has been widely used to uncover structural genomic elements at different hierarchical levels, such as A/B chromatin compartments, TADs, and loops [\[–3\]](#page-14-2). Many computational tools exist to call these structures from Hi-C data, with variable reliability however [\[4–](#page-14-3)[6\]](#page-14-4).

Changes in 3D structures have been implicated in gene expression, cell division, cell differentiation, developmental disorders, and cancers [[7–](#page-14-5)]. This underscores the need for reliable methods and tools to compare Hi-C data across different conditions. One approach to comparing Hi-C data is to compute a similarity score for a pair of matrices, either at the level of the entire matrix (matrix-level) or for specific genomic regions (bin-level). Gunsalus et al., 2023 [\] reviewed several methods for the pairwise comparison of Hi-C matrices, classifying them into three categories: *basic methods*, which directly compute a similarity score (e.g. a correlation) between two matrices [\], *map-informed methods*, which first calculate a Hi-C-related metric along a 1D track for each matrix separately (e.g. directionality index) and then compare the resulting tracks [\[12\]](#page-14-9), and *feature-informed methods*, which predict specific chromatin structures for each matrix (e.g.


## 主要发现

### **Number of tested bin pairs**

We used the H0 setting to assess the differences in the number of bin pairs filtered before the test procedure by the different tools. [Figure](#page-8-1) 3 provides the proportion of tests performed for each tool in the H0 setting (relative to the maximum number of possible tests, as given in [Table](#page-8-0) 3 for each chromosome and resolution). The difference in the numbers of tested bins is thus only due to differences in the filtering step.

The different tools apply pre-filtering steps that resulted in a very different number of tested bin pairs. **HiCcompare** performed a number of tests that is constantly close to the maximum and **HiCDCPlus** constantly performed a very low number of tests because it only tests (the union of) regions with an interaction considered significantly above the interaction background (FDR adjusted *p*-value *<* 10%). For the relatively short chromosome 21, **multiHiCcompare** did not perform any test (all interactions were filtered out at preprocessing). However, it performed a number of tests close the maximum for the other two chromosomes at resolutions 500 kb and 1 Mb. At a 500 kb resolution (the only resolution available for this tool), **sslHiC** performed a number of tests close to the maximum for the three chromosomes. Finally, **diffHic** and **Selfish** filtered out approximately half of the bin pairs.

Note that the differences in the number of tested bin pairs are partially due to default values set differently by different tools for the same parameter: For instance, **HiCcompare** filters out bin pairs with an average *A* value smaller than the 10th percentile of *A* values while **multiHiCcompare** filters out bin pairs with an average *A* value smaller than 5.


## 方法概述

# **Methodological overview of the tools**

This article covers tools that all aim at answering the same question: given a set of *n* Hi-C matrices, M1, *...* , M*n*, belonging to *K* different groups of biological interest (that we will call "conditions"), are we able to find bin pairs with significantly different interaction counts between conditions? While several descriptive metrics (such as correlation or other similarity measures) can be used for this purpose, we focus on approaches that provide statistical guarantees for identified bin pairs. Such approaches perform one statistical test for each bin pair. The result of each of these tests can be summarized by a *p*-value (or an adjusted *p*value), which quantifies the statistical evidence of a significant difference.

The tools discussed in this article all have a common workf low [\(Fig.](#page-2-0) 1). In short, this workf low takes Hi-C matrices from different conditions and performs a statistical test, which results in a *p*value (or an adjusted *p*-value) for each bin pair. **CHESS** is the only tool that slightly differs from this description because it provides *p*-values for fixed-sized windows of the Hi-C matrix (and not for every bin pair; see Section "Methodological background of the tools").

As shown in [Fig.](#page-2-0) 1, the Hi-C differential analysis workf low can be decomposed into four main steps:

- *filtering*, which consists in removing bin pairs considered not relevant from the analysis in all Hi-C matrices;
- *normalization*, which consists in making bin pairs in a matrix or bin pairs between different matrices more comparable;

- • *model and p-value computation*, which is the core of the statistical analysis and performs a test on all remaining bin pairs, using normalized interaction values;
- *multiple testing correction*, which aims at accounting for the fact that a large number of tests have been performed.


## 讨论与结论

provides the percentage of tests declared significant for it occasionally presented a strong excess of false positives, as all chromosomes, resolutions, and tools, based on a 5% and a observed on chromosome 21. 1% thresholding of p-values and adjusted p-values. Figure S1 in Precision and Recall (H setting) Supplementary material additionally provides the same plots for 1 a 10% threshold. a provides the proportion of tested interactions that are In H0 settings, the percentage of p-values below 5% is expected located within the target zone, where positive calls are expected to be at most 5% if the test is properly calibrated (type-I error con- (true signal). This proportion may vary even for tools that rely trol).

## 关键词

BriefingsinBioinformatics, bbaf074

## 相关实体

细胞类型: all

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
