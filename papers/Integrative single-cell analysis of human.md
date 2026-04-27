---
marker_extracted: true
title: "Integrative single-cell analysis of human"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/integrative-single-cell-analysis-of-human.md]
confidence: medium
year: 2024
---

# Integrative single-cell analysis of human

> 原文: [[integrative-single-cell-analysis-of-human]]

## 摘要

nature cancer Analysis Integrative single-cell analysis of human colorectal cancer reveals patient stratification with distinct immune evasion mechanisms Received: 17 June 2023 Xiaojing Chu 1,5, Xiangjie Li 1,5, Yu Zhang1,5, Guohui Dang 1,2, Yuhui Miao 1, Wenbin Xu1, Jinyu Wang1, Zemin Zhang 3,4,6 & Sijin Cheng 1,6 Accepted: 16 July 2024 Published online: xx xx xxxx The tumor microenvironment (TME) considerably influences colorectal Check for updates cancer (CRC) progression, therapeutic response and clinical outcome, but studies of interindividual heterogeneities of the TME in CRC are lacking. Here, by integrating human colorectal single-cell transcriptomic data from approximately 200 donors, we comprehensively characterized transcriptional remodeling in the TME compared to noncancer tissues and identified a rare tumor-specific subset of endothelial cells with T cell recruitment potential.

## 背景与目的

Mono-CD16 T-CD8-MAIT-KLRB1 EC-artery-GJA5 T/NK/ILCs Myelo S id tr o c m el a ls l cells M M a o c n r o o - - F C C 1 N Q 1 C T IL - C pr -I o L l 4 if I e 1 rating E E C C - - c c a a p p i i l l l l a a r r y y - - B C T A N 4 L9 B cells M M M a a a c c c r r r o o o - - - I L S S Y P G V P 1 E 1 5 1 Ma M li a g li n g a n n a t n /e t p c i e th ll elial cells E E E C C C - - - H H ly E E m V V p - - C S h E a X L t C i E c L 1 E 0 C-LYVE1 Mast cell-TPSAB1 Epithelial cell EC-lymphatic EC-PROX1 Myeloid-proliferating EC-proliferating EC-transiting 1 EC-transiting 2 EC-vein-ACKR1 d f g Plasma Mono/macro CD4 CD8 Plasma−IgA Plasma−IgG 0.75 0.50 0.25 0 Nature Cancer noitroporP 0.8 0.6 0.4 0.

## 主要发现

#### **A single-cell atlas of the human colorectum**

To establish a comprehensive single-cell atlas of the human colorectum under both physiological and pathological conditions, we collected published single-cell RNA-sequencing data of healthy colorectal tissues12,13, uninflamed and inflamed tissues from patients with ulcerative colitis (UC)–17, colorectal polyp tissues18, paracancerous tissues and tumor tissues of CRC,9–11,,. The atlas comprised 1,144,726 cells across 427 samples from 192 donors (Supplementary Table 1). After quality control, we classified 873,302 cells into 58 subsets, including 15 T cell/natural killer (NK) cell/innate lymphoid cell (ILC) subsets, 12 myeloid cell subsets, 12 endothelial cell (EC) subsets and others based on their distinct gene expression patterns (Extended Data Figs. 1 and 2a–e). We then filtered out cells expressing <800 genes and constructed a high-quality colorectal atlas containing 671,192 single cells (http://118.190.148.166:8918/\). This atlas includes data on tumor tissues from 124 donors, paracancerous tissues from 78 donors, polyps from 9 donors, inflamed tissues from 23 donors, uninflamed tissues from 11 donors and healthy tissues from 36 donors (Fig. 1a–c). Addressing the concerns about batch effects, we observed that cells were clustered based on cell types and pathological status rather than datasets (Extended Data Fig. 3a). We also conducted a principal component (PC) analysis (PCA) and a distance analysis on the samples based on cell subtype proportions. The results showed that the differences between the samples were mainly caused by pathological status (Fig. 1d,e and Extended Data Fig. 3b). We further collected single-cell data from 31 new patients with CRC and annotated the subclusters (Methods). These new patients were used as a validation cohort (Supplementary Table 2).

We next aimed to characterize major cell-type preferences among different tissues (Extended Data Fig.


## 方法概述

#### **Single-cell RNA-sequencing data collection and quality control**

We collected single-cell transcriptomic data from 15 public datasets comprising 427 human colon and rectum samples from 192 donors divided into six groups, including healthy, uninflamed, inflamed, polyp, paracancerous and tumor samples,9–17,, (Supplementary Table 1). Samples from the inflamed region and those from the unaffected colorectal regions of patients with UC served as the inflamed and uninflamed samples, respectively. Biopsy specimens taken from the tumor center and adjacent normal region in patients diagnosed with CRC were grouped as the tumor and paracancerous samples, respectively. In total, we collected data from 1,144,726 cells with or without quality control.

To annotate cell subsets accurately, we excluded cells with <800 detected genes and with >20% mitochondrial counts for fibroblasts, ECs, monocytes/macrophages and DCs for cluster identification and annotation. For the remaining cell types, cells with <500 detected genes were excluded. We filtered out potential doublets, which were identified by the coexpression of different well-known cell-type markers, leaving 873,392 cells with identified subsets.


## 讨论与结论

In this study, we established a high-quality cell atlas for colorectal tissues and characterized transcriptional remodeling in tumors compared to local inflammation. Notably, we identified a rare HEV-like endothelial subset (HEV-CXCL10) that correlated with T cell recruitment. However, limited by the sampling bias of the 10x Genomics technology, we were not able to collect and annotate neutrophils. This requires particular attention in future studies. The atlas is accessible at http://118.190.148.166:8918/, allowing for more in-depth functional studies.

Most importantly, based on the individual-level abundance of the TME cell subsets, we constructed a classification system dividing patients into six groups using an unsupervised approach. We observed that malignant cells could downregulate cytokine-related genes and express ligands such as *COL1A1* to recruit fibroblasts to block the infiltration of immune cells. Meanwhile, upregulation of the *PDL1/2*– *PDCD1* and *CD47*–*SIRPA* axes and downregulation of Fcγ receptors

 | **Transcriptional alterations of CRC genetic risk genes. a**, Quantile–quantile plot showing the nominal P-value distribution derived from an expected distribution (dashed line) (n = 288, 266, 193, 149, 120, 187, 198, 119, 143, 112, 99 and 93 genes from top to bottom). **b**, Bar plot showing lambda statistics for each cell type (n = 288, 266, 193, 149, 120, 187, 198, 119, 143, 112, 99 and 93 genes from top to bottom). **c**, Heatmap showing the $\log_2(\text{fold change})$ of each risk gene in each cell type. **d**, Violin plot showing the expression of COL4A2 in each cell type (top;

n=28,158,49,042,54,671,41,247,4,236,1,263,38,132,7,769,5,186,8,337,29,998 and 1,693 cells from left to right) and in fibroblasts and ECs from tumors and paracancerous tissues (bottom; n=14,981,15,017,4,349 and 3,988 cells from left to right).


## 关键词

Integrative, analysis, human, single-cell

## 相关实体

细胞类型: T cell, lymphoid, myeloid
方法: single-cell
疾病: cancer, tumor

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
