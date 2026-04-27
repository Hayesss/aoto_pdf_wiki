---
marker_extracted: true
title: "Feature selection methods affect the"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/feature-selection-methods-affect-the.md]
confidence: medium
year: 2025
---

# Feature selection methods affect the

> 原文: [[feature-selection-methods-affect-the]]

## 摘要

The study was conducted in accordance with the registered, peer- specific technical factor. Proper assessment of the effect of technical reviewed protocol at dataset features would require more datasets where each factor is (ref. 9). Except for pre-registered and approved pilot data, all anal ysis varied independently, potentially through a simulation study. results reported in the paper were collected after the date of the regis- Perhaps the most important consideration for metric selection tered protocol publication. is the correlation between metrics (Fig. 1b and Extended Data Fig. 3). We want metrics that measure different aspects of integration and Results query mapping and selecting several highly correlated metrics would Metric selection is critical for reliable benchmarking bias our results in that direction. This effect is evident in the Integra- For this study, we collected a wide variety of metrics covering different tion (Bio) category where several metrics (adjusted Rand index (ARI), aspects of integration and query mapping. While measuring a broad batch-balanced ARI (bARI)16, normalized mutual information (NMI), range of factors is important, the behavior of many of these metrics has batch-balanced NMI (bNMI)16, cLISI, label average silhouette width not been thoroughly characterized.

## 背景与目的

hparG ISILi WSA hctaB gnixiM TEBk WSA lebal detalosI 1F lebal detalosI IMNb ISILc ffiDfdl IRA elcyc lleC WSA lebaL erutcurts lacoL IMN IRAb ecnatsid lleC ecnatsid lebaL ISILm ISILq noitcurtsnoceR noitalerroc NNk )orcam( 1F )orcim( 1F )ytirar( 1F CRPUA ycaruccA )orcam( xedni draccaJ )orcim( xedni draccaJ )ytirar( xedni draccaJ CCM oliM ecnatsid llec neesnU ecnatsid lebal neesnU ytniatrecnU (batch) (bio) Mapping Classification Unseen Integration Integration Correlations between metrics Fig. 1 | Overview and results of the metric selection step. a, Diagram of the indicates the mean correlation, and the size of squares is the s.d. (larger points metric selection workflow. b, Results of the metric selection step. Densities are less variable). The heatmap on the right shows the mean correlation between for the observed range and correlation with the number of features across metrics grouped by metric type (Extended Data Fig. 3b). The color bar on the left datasets and integrations are shown for each metric. Colors indicate the mean indicates which metrics were selected for the final benchmark. This indication is value and vertical lines represent the median. The middle heatmap shows the continued as shaded areas in the other plots. mean correlation with technical dataset features (Extended Data Fig. 3a). Color Registered Report 1 Int. batch Int. bio 1 Mapping Class.

## 主要发现

#### **Metric selection is critical for reliable benchmarking**

For this study, we collected a wide variety of metrics covering different aspects of integration and query mapping. While measuring a broad range of factors is important, the behavior of many of these metrics has not been thoroughly characterized. This characterization is particularly important in our context as we use metrics developed to compare different integration approaches to instead assess the effect of feature selection methods. For this reason, we include a metric selection step to profile metrics and decide which to use for benchmarking. This step aims to select metrics that effectively measure performance, are not overly associated with technical factors and are nonredundant.

We performed the metric selection using random and highly variable (scanpy implementation of a Seurat algorithm11\) feature sets of different sizes for each dataset, performing integration and mapping, calculating metric scores and comparing the results (Fig. 1a\). The observed range of scores was calculated using the random gene sets for each dataset–integration combination. We also used random sets to calculate the correlation between metrics and technical aspects of datasets (number of features, number of reference cells, number of reference labels and batches, number of query cells and number of query batches and unseen labels). We calculated the correlation between metric scores and the number of selected features using the highly variable feature sets as random feature sets do not have any inherent ordering (the first 100 features are no more informative than the next 100). An ideal metric would accurately measure what it is designed for, returning scores across its whole output range that are independent of technical features of the data and are orthogonal to other metrics in the study. Figure 1b shows a summary of the metric evaluation.


## 方法概述

Our study follows a standard benchmark design, consisting of test datasets, feature selection methods to be evaluated and metrics for measuring performance (Extended Data Fig. 1). The complete benchmarking pipeline is implemented as a Nextflow workflow (Extended Data Fig. 2) available from GitHub and archived on Zenodo52. Summaries of the specific methods, metrics, datasets and processing steps are provided in the following sections. Please refer to the supplementary methods, pipeline code, original publications and package documentation for further information.


## 讨论与结论

In this comprehensive benchmark, we evaluated variants of 24 feature selection methods on ten datasets using 1,700 selected feature sets, over 6,000 integration runs producing over 140,000 metric scores. We performed a rigorous metric selection process and determined a number of features (2,000) that performed well across datasets. Our evaluation found highly variable feature selection methods to perform well, with the approach based on a variance-stabilizing transformation (Seurat-VST/scanpy-SeuratV3) being the top-ranked method. This result reinforces common practice and recommendations from previous benchmarks. Label-guided marker genes (Wilcoxon) also performed well but were more variable across datasets. We focused on unsupervised methods and other supervised techniques may produce more stable results; however, supervised feature selection only applies when cell labels are available, typically not the case before integration. The triku method was also highly ranked but showed some bias toward batch correction.

We did not find a consistent advantage for batch-aware variants of methods implemented in scanpy. Batch-aware selection could improve performance in some scenarios, but a more specific evaluation including additional methods is required to determine its applicability. For large datasets, batch-aware feature selection has a computational advantage, as loading the whole dataset into memory can be avoided. However, we could run many top-performing methods on the full datasets with relatively modest memory requirements.

We used scVI for our primary benchmark but compared the performance to scANVI, to inspect the effect of adding prior knowledge, and Symphony to see the interaction with an alternative integration approach.


## 关键词

Feature, affect, methods, selection

## 相关实体

细胞类型: all

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
