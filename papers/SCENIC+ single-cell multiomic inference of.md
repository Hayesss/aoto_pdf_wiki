---
marker_extracted: true
title: "SCENIC+: single-cell multiomic inference of"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/scenic-single-cell-multiomic-inference-of.md]
confidence: medium
year: 2023
---

# SCENIC+: single-cell multiomic inference of

> 原文: [[scenic-single-cell-multiomic-inference-of]]

## 摘要

nature methods Article SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks Received: 19 August 2022 Carmen Bravo González-Blas1,2,4, Seppe De Winter 1,2,4, Gert Hulselmans1,2, Nikolai Hecker 1,2, Irina Matetovici 1,3, Valerie Christiaens1,2, Accepted: 6 June 2023 Suresh Poovathingal1, Jasper Wouters 1,2, Sara Aibar1,2 & Stein Aerts 1,2 Published online: 13 July 2023 Check for updates Joint profiling of chromatin accessibility and gene expression in individual cells provides an opportunity to decipher enhancer-driven gene regulatory networks (GRNs). Here we present a method for the inference of enhancer-driven GRNs, called SCENIC+. SCENIC+ predicts genomic enhancers along with candidate upstream transcription factors (TFs) and links these enhancers to candidate target genes. To improve both recall and precision of TF identification, we curated and clustered a motif collection with more than 30,000 motifs.

## 背景与目的

Motif 1 0.5 0.5 Motif 2 Cluster-Buster CRM scores database CRM ranking database Cluster 1 Cluster 2 Cluster 3 Motifs snoiger fo rebmuN snoigeR Region sets Motifs snoigeR Set1 versus Set2 Motifs snoigeR Cell clustering Enhancer identification Gene expression >30,000 PWMs TF annotations Curated Direct motif-to-TF TF TF TF Orthology annotations eRegulon Effector TF TF + motif + accessibility + gene expression TF TF TF Single cell viewer Genome Browser Network app SCope UCSC Cytoscape 500 400 300 200 100 0 0 25 50 75 100 Number of topics )s( emiT 1,500 K562 CGS - cisTopic HCT116 1,000 CGS - pycisTopic MCF7 Signac DARs 500 ArchR WarpLDA - cisTopic DARs pycisTopic HepG2 DARs Mallet - pycisTopic pycisTopic Topic 0 0 0.03 0.06 0.09 0.12 Human Mouse Fly Enhancer recovery Species sFT fo rebmuN Annotation Direct Orthology 200 100 0 0 25 50 75 100 Rank stih fo rebmuN a d b c e f 1,553 2 # 8 h 5 its 272 1,357 265 251 240 234 225 206 198 cisTarget (archetype) cisTarget (clustered) 467 cisTarget (unclustered) cisTarget (SCENIC) DEM (archetype) DEM (clustered) DEM (unclustered) DEM (SCENIC) Homer Fig. 1 | The SCENIC+ workflow and motif collection. a, SCENIC+ workflow. analysis. d, Workflow to create motif databases for SCENIC+.

## 主要发现

ARID3A(+) BCL11A(+) IRF8(+) MYB(+) PPARA(+) RUNX2(+) SPIB(+) 130 TCF4(+) B cells ZBTB18(+) CD14+ ATF3(+) Mono B C A R C EB H 5 1 ( ( + + ) ) CD4+ T F E O TV SB 6 ( ( + + ) ) CD8+ T FOS(+) FOXN2(+) cDC FOXN3(+) FOXO3(+) pDC JDP2(+) FCGR3A+ KLF4(+) Mono MEF2A(+) NK cells MEF2C(+) 0 RXRA(+) PAX5 24 STAT1(+) CEBPA(+) ChIP CEBPB(+) EBF1 85 IRF5(+) ChIP MAFB(+) POU2F2 79 MBD2(+) ChIP NR4A1(+) POU2F2(+) EBF1 PAX5 PAX5 POU2AF1 RARA(+) SPI1(+) 0.07 STAT2(+) e STAT6(+) ro TCF7L2(+) c S C B D c 4+ e C l T l D s c 8+ e l T ls c C N el D K ls 1 c 4+ e F l m l C s p o G D n R C o 3 s c A y + t e m s c o D n C o s cytes 0 96,225,000 B c L h N r1 K 0 position (kb) 96,300,000 1 2 3 4 5 6 7 8 9 3’ stiB 2.0 1.0 05’ 1 2 3 4 5 6 7 8 9 01 3’ stiB 2.0 1.0 05’ 1 1 1 7 7 2 2 2 3 3 8 8 6 6 9 9 0 0 5 5 4 4 1 2 1 1 2 1 1 1 1 1 1 1 2 3’ stiB 2.0 1.0 05’ 1 1 7 2 2 3 3 8 6 90 5 5 4 4 11 1 11 1 3’ stiB 05’ 2.0 1.0 1 2 3 4 5 6 7 8 9 3’ stiB 2.0 1.0 05’ 1 2 3 4 5 6 7 8 3’ stiB 2.0 1.0 05’ 1 2 3 4 5 6 7 8 3’ stiB 05’ 2.0 1.0 1 2 3 4 5 6 7 8 9 01 3’ stiB 2.0 1.0 05’ 1 2 3 4 5 6 7 8 9 01 3’ stiB 05’ 2.0 1.0 1 2 3 4 5 6 7 8 3’ stiB 2.0 1.

## 方法概述

#### **SCENIC+ workfow**

The SCENIC+ workflow consists of three main analysis steps: (1) unsupervised identification of enhancers with shared accessibility patterns from scATAC-seq data; (2) prediction of TFBSs via motif enrichment analysis; and (3) prediction of eGRNs combining TF expression, TFBSs, region accessibility and gene expression. These steps are performed using three Python modules: pycisTopic, pycisTarget and SCENIC+. Detailed explanations are described in Supplementary Note 1. Links to the tools, SCENIC+ code and tutorials are available at scenicplus. readthedocs.io.

**pycisTopic.***Consensus peak calling*. Pseudobulk fragment bed files per cell type were generated using the fragments file and cell-type annotations provided by the user. Peaks were called using MACS2 (ref. 81\) with parameters –format BEDPE –keep-dup all–shift 73 –ext\_size 146. An iterative approach described by Corces et al.82 was used to obtain a consensus peak set. Briefly, each peak's summit was extended with a 'peak\_half\_width' (default 250 bp) in each direction and overlapping and less-significant peaks were filtered out. The original peak was kept if there was only a single peak. The original peak with the highest score was kept if there were two or more overlapping peaks. This process was repeated until there were no more overlapping peaks. The process of consensus peak generation was repeated twice: first for each cell type separately and, second, after peak score normalization within the cell type, using the union of peaks across cell types.

*Quality control*. The sample-level statistics that we used to assess the overall quality of the sample were:

- • Barcode rank plot
- • Insertion size
- • Sample transcription start site (TSS) enrichment
- • Fraction of reads in peaks (FRiP) distribution
- • Duplication rate

The barcode-level statistics that we used to differentiate good quality cells versus the rest were:

- • Total number of unique fragments per cell barcode
- •...


## 讨论与结论

CREs are key to control differential gene expression across cell types, during development, in evolution and in disease–5,. Yet, only few GRNs have been characterized to the level of detail where they include CREs as nodes2,14. We lack such GRNs mainly due to challenges associated with high-throughput experimental identification and validation of TFBSs. For this reason, we need computational methods that can identify TFBSs on a genome-wide scale and at the cell-type-specific level. Single-cell chromatin accessibility and gene expression profiling combined with sequence analysis is ideally suited for this and led to the concept of eGRNs,14,–34. In this work we present SCENIC+, a computational method to efficiently infer eGRNs.

By applying SCENIC+ to single-cell multiome data across a range of biological systems and across species we showed that SCENIC+ can accurately identify key TF combinations for each cell type. More notably, it can confidently link these TFs to CREs and target genes. By comparing SCENIC+ to other methods, we could identify several elements that improve the quality of eGRN inference. First, the use of topic modeling improves unsupervised prioritization of informative regions. Second, the use of multiple motifs per TF and the use of a large motif collection improve the recall to identify important TFs. Finally, the use of motif enrichment analysis instead of motif scanning that is used in alternative methods reduces the false-positive rate of TFBS predictions.

One biological application where eGRN inference plays a pivotal role is in evolutionary genomics. For example, within the mammalian cortex, the majority of cell types were found to be conserved,71–73; however, hundreds of genes are differentially expressed between orthologous cell types60. Comparison of eGRNs inferred across species can provide insights into these discrepancies.


## 关键词

SCENIC, inference, multiomic, single-cell

## 相关实体

方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
