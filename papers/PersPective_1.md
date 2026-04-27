---
title: "PersPective"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/perspective.md]
confidence: medium
year: 2020
---

# PersPective

> 原文: [[perspective]]

## 摘要

of the data due to biological fluctuations in the measured traits or into a single instance with a rich and user-friendly interface. Such limited sensitivity for quantifying small numbers of molecules13,24–26. an approach is especially important for biological analysis, as there These unique characteristics have motivated the development are often many links between primary data and metadata that need of statistical methods tailored for single-cell data analysis27–30. to be preserved throughout an analysis. Furthermore, as single-cell technologies mature, the increasing complexity and volume of data require fundamental changes in data The SingleCellExperiment container. Bioconductor uses the access, management and infrastructure alongside specialized meth- SingleCellExperiment class for storing single-cell assay data and ods to facilitate scalable analyses. metadata (Fig. 2). Primary data, such as count matrices, are stored To address these challenges, software packages developed for in the assays component as one or more matrices, where rows rep- the analysis of single-cell data have become an integral part of the resent features (for example, genes and transcripts) and columns Bioconductor project. Herein, we primarily focus on the analysis of represent cells. In addition, low-dimensional representations of 1Fred Hutchinson Cancer Research Center, Seattle, WA, USA. 2Cancer Research UK Cambridge Institute, University of Cambridge, Cambridge, UK.

## 背景与目的

For specific file formats, we can use dedicated methods from the the primary data, and metadata describing cell or feature charac- DropletUtils (for 10X data) or tximeta (for pseudo-alignment teristics, can also be stored in the SingleCellExperiment object. methods) packages. Through the SingleCellExperiment class, all pertinent data and results relevant to a scRNA-seq experiment can be stored in a single Quality control. Low-quality libraries in scRNA-seq data can instance. By standardizing the storage of single cell data and results, arise from a variety of sources such as cell damage during disso- Bioconductor fosters interoperability between single-cell analy- ciation or failure in library preparation (for example, inefficient sis packages and facilitates the development and usage of complex reverse transcription or PCR amplification). These usually mani- analysis workflows. fest as ‘cells’ with low total counts, few expressed genes and high mitochondrial read proportions. These low-quality libraries are Data processing problematic as they can contribute to misleading results in down- The aim of this section is to describe the precursor steps that are stream analyses. common to most scRNA-seq analyses. These preliminary steps For droplet-based protocols, it is common to exclude data from follow a general workflow (Fig. 3): (1) preprocessing raw sequenc- droplets that did not contain exactly one cell.

## 主要发现

in these calculations has a major impact on the behavior and per- For example, given a discrepancy between the visible clusters on a formance of such downstream methods. Feature selection methods 2-dimensional plot and those identified by clustering using the top aim to identify genes that contain useful information about the biol- PCs, one would be inclined to favor the latter. ogy of the system while removing genes that contain random noise. The SingleCellExperiment class has a dedicated component, By limiting analyses to such genes, interesting biological structure reducedDims, for storing lower dimensional representations of is preserved without the variance that obscures that structure. the assay data (Fig. 2). The scater41 package provides convenience Furthermore, focusing on such a subset of the transcriptome can wrapper functions for dimensionality reduction algorithms, significantly reduce the size of the dataset, improving the computa- including Principal Components Analysis (PCA), t-Distributed tional efficiency of downstream analyses. See refs. 50,51 for reviews in Stochastic Neighbor Embedding (t-SNE)53, and Uniform Manifold feature selection methods. Approximation and Projection (UMAP)54. Diffusion map methods The simplest approach to feature selection is to select the most are available via the destiny55 package. The zinbwave30 and glmpca48 variable genes based on their expression across the population.

## 方法概述

(Fig. 2), methods and software, and organized the packages along a sequencing data. Genome Biol. 16, 278 (2015). 28. Lun, A. T. L., Bach, K. & Marioni, J. C. Pooling across cells to normalize typical workflow (Fig. 3) for the most common single-cell analyses single-cell RNA sequencing data with many zero counts. Genome Biol. 17, (Fig. 4). Finally, we have developed an online companion book that 75 (2016). provides more details on focused topics as well as complete cod- 29. Ji, Z. & Ji, H. TSCAN: Pseudo-time reconstruction and evaluation in ing workflows ( This effort will be single-cell RNA-seq analysis. Nucleic Acids Res. 44, e117 (2016). continuously updated and maintained with new packages as they 30. Risso, D., Perraudeau, F., Gribkova, S., Dudoit, S. & Vert, J.-P. A general and flexible method for signal extraction from single-cell RNA-seq data. emerge, which increases discoverability of Bioconductor resources. Nat. Commun. 9, 284 (2018). 31. Chambers, J. M. Object-oriented programming, functional programming and Received: 26 March 2019; Accepted: 14 October 2019; R. Stat. Sci. 29, 167–180 (2014). Published online: 2 December 2019 32. Tian, L. et al. scPipe: a flexible R/Bioconductor preprocessing pipeline for single-cell RNA-sequencing data. PLoS Comput. Biol. 14, e1006361 (2018). References 33. Wang, Z., Hu, J., Johnson, W. E. & Campbell, J. D. scruff: an R/Bioconductor package for preprocessing single-cell RNA-sequencing data.

## 讨论与结论

23. Han, X. et al. Mapping the mouse cell atlas by microwell-seq. Cell 173, 54. Melville, J., McInnes, L. & Healy, J. UMAP: uniform manifold approximation 1307 (2018). and projection for dimension reduction. Preprint at arXiv 24. McDavid, A. et al. Data exploration, quality control and testing in abs/1802.03426 (2018). single-cell qPCR-based gene expression experiments. Bioinformatics 29, 55. Angerer., P. et al. Destiny: diffusion maps for large-scale single-cell data in R. 461–467 (2013). Bioinformatics 32, 1241–1243 (2016). 144 NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods NaTuRe MeTHods PersPective 56. Haghverdi, L., Lun, A. T. L., Morgan, M. D. & Marioni, J. C. Batch effects in 87. Rue-Albrecht, K., Marini, F., Soneson, C. & Lun, A. T. L. iSEE: interactive single-cell RNA-sequencing data are corrected by matching mutual nearest SummarizedExperiment Explorer. F1000Res. 7, 741 (2018). neighbors. Nat. Biotechnol. 36, 421–427 (2018). 88. Peterson, V. M. et al. Multiplexed quantification of proteins and transcripts in 57. Lin, Y. et al. scMerge leverages factor analysis, stable expression, and single cells. Nat. Biotechnol. 35, 936–939 (2017). pseudoreplication to merge multiple single-cell RNA-seq datasets. Proc. Natl. 89. Dey, S. S., Kester, L., Spanjaard, B., Bienko, M. & van Oudenaarden, A. Acad. Sci. USA 116, 9775–9784 (2019). Integrated genome and transcriptome sequencing of the same cell. 58. Kiselev, V. Y., Yiu, A.

## 关键词

PersPective

## 相关实体

方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
