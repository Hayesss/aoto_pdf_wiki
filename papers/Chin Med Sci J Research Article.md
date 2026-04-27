---
marker_extracted: true
title: "Chin Med Sci J Research Article"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/chin-med-sci-j-research-article.md]
confidence: medium
year: 2025
---

# Chin Med Sci J Research Article

> 原文: [[chin-med-sci-j-research-article]]

## 摘要

Objective Recent advancements in single-cell RNA sequencing (scRNA-seq) have revolutionized the study of cellular heterogeneity, particularly within the hematological system. However, accurately annotating cell types remains challenging due to the complexity of immune cells. To address this challenge, we develop a PAN-blood single-cell Data Annotator (scPANDA), which leverages a comprehensive 10-million-cell atlas to provide precise cell type annotation.

Methods The atlas, constructed from data collected in 16 studies, incorporated rigorous quality control, preprocessing, and integration steps to ensure a high-quality reference for annotation. scPANDA utilizes a threelayer inference approach, progressively refining cell types from broad compartments to specific clusters. Iterative clustering and harmonization processes were employed to maintain cell type purity throughout the analysis. Furthermore, the performance of scPANDA was evaluated in three external datasets.

Results The atlas was structured hierarchically, consisting of 16 compartments, 54 classes, 4,460 low-level clusters (pd\_cc\_cl\_tfs), and 611 high-level clusters (pmid\_cts). Robust performance of the tool was demonstrated in annotating diverse immune scRNA-seq datasets, analyzing immune-tumor coexisting clusters in renal cell carcinoma, and identifying conserved cell clusters across species.

**Conclusion** scPANDA exemplifies effective reference mapping with a large-scale atlas, enhancing the accuracy and reliability of blood cell type identification.

Key words: single-cell RNA sequencing; immunology; cell type annotation; single-cell atlas; blood cells


## 背景与目的

Immune cells play vital roles in both physiological and pathological conditions in humans. Recent advancements in single-cell technologies have enabled researchers to observe cellular dynamics with unparalleled precision, tackling the challenge of cellular het-

erogeneity that bulk sequencing methods could not resolve. This has significantly advanced research in hematology and immunology. In 2022, Xie et al.[1] created detailed transcriptomic maps and transcription factor profiles for various human blood cells, establishing a platform for gene expression analysis and the prediction of blood cell types and functions. These resources provide essential references for further blood cell research. However, accurately annotating single-cell sequencing results and identifying cell identities are crucial for analyzing single-cell RNA sequencing (scRNA-seq) data, especially when studying the complex cellular compositions inherent in hematology and immune systems.

In recent years, various cell annotation methods

Received January 18, 2025; accepted March 4, 2025; published online March 31, 2025.

<sup>\*</sup>Corresponding author Email: cds@ism.pumc.edu.cn

<sup>©</sup> The authors 2025. Published by Chinese Academy of Medical Sciences. This is an open access article distributed under the terms of the CC BY-NC license (http://creativecommons.org/licenses/ by-nc/4.0).

have emerged, which can be broadly categorized into three types. The first uses marker-based approaches, such as CellAssign<sup>[2]</sup>, where specific genes label and classify cells, determining their cell type. The second method involves annotating cells based on their similarity to predefined reference cells, as seen in tools like SingleR<sup>[3]</sup>. The third category employs machine learning techniques for probability-based predictions, incorporating unbiased feature selection from reduced-dimensional spaces, exemplified by supervised classification methods like CellTypist<sup>[4]</sup>.


## 主要发现

## **The comprehensive 10 million blood single-cell atlas**

The bioinformatics workflow () ensures the inclusion of high-quality and abundant cells in the blood atlas, achieving computationally distinct and biologically meaningful cell compartments, classes, and clusters. The following criteria were considered for data inclusion: (1) ensuring comprehensiveness and heterogeneity by incorporating datasets covering physiological, aging, and disease conditions; (2) improving annotation accuracy and resolution by increasing the number of cells per type and state; and (3) minimizing batch effects by prioritizing large-scale datasets.

After quality control and preprocessing to remove low-quality and unidentified cells, the datasets were concatenated to create an expression profile matrix of 9,841,765 cells and 13,220 genes.

The top 3, 000 HVGs were selected for principal component analysis (PCA) and cell neighbor calculation, which were then input to CellHint, a machine learning approach that can (1) harmonize diverse cell type annotation styles in multiple datasets and (2) integrate the datasets. Here, the latter functionality (CellHint Integration) was firstly used to remove batch effects in the concatenated matrix.

To achieve finer partitioning, each class was clustered twice using the Leiden algorithm. In each of the resulting Leiden clusters, CellHint Harmonization was carried out to standardize the diverse annotation styles across the original datasets (*e*.*g*., "*CD4-Th (1)*" in PMID: 33657410 versus "*T\_CD4\_c01\_LEF1*" in PMID:34290408). This operation could possibly divide the Leiden cluster into multiple cell groups; further segregation by such groups gave the final clustering outcomes, *i.e.*, the 4,460 low-level clusters, each with ensured purity of cell types. The clusters were named using the structure "*pd\_cc\_cl\_tf*" (*e*.*g*.


## 方法概述

#### Data collection, quality control, and preprocessing

The large number of cells that constructed the sc-PANDA atlas were obtained from 16 studies (). In total, the raw data contained 11,215,872 single-cell transcriptomics. The atlas types of these datasets can be summarized into six categories: aging, COVID-19, bacterial infection, tuberculosis infection, immune, and tumor. Such diversity and scale of single-cell atlases across various biological contexts and diseases went through a series of operations (quality control, preprocessing, harmonization, and integration) to form the scPANDA atlas.

Scanpy was deployed to perform quality control (QC) of the raw scRNA-seq data. Cells with only a few genes (<200; possibly low-quality or empty droplets) or excessive genes (>6,000; potentially doublets) were excluded by scanpy. pp. filter\_cells to remove stressed or dying cells, only those with <15% mitochondrial (MT) gene content were retained via applying scanpy.pp.calculate\_qc\_metrics for MT percentage calculation and subsetting accordingly. Expression profiles of the filtered data were log-normalized by scanpy.pp.normalize\_total and scanpy.pp.log1p with a target sum of 1e4 (all the datasets were normalized in

Table 1. Summary of the 16 datasets that constructed the scPANDA atlas.

| PMID | Atlas type |
|--------------------------|--------------------------|
| 37963457 <sup>[20]</sup> | Aging |
| 34782790 <sup>[21]</sup> | Infection (COVID-19) |
| 33657410 <sup>[22]</sup> | Infection (COVID-19) |
| 35216673 <sup>[23]</sup> | Infection (COVID-19) |
| 33879890 <sup>[24]</sup> | Infection (COVID-19) |
| 34429372 <sup>[25]</sup> | Infection (COVID-19) |
| 35672358 <sup>[26]</sup> | Infection (bacterial) |
| 34031617 <sup>[27]</sup> | Infection (tuberculosis) |
| 34290408 <sup>[28]</sup> | Immune (tumor) |
| 35618845 <sup>[29]</sup> | Immune (eQTL) |
| 35549406 <sup>[4]</sup> | Immune (cross-tissue) |
| 35549310 <sup>[30]</sup> | Immune (developmental) |
| 34914499...


## 讨论与结论

In this study, we introduce scPANDA, a tool for annotating cell types in scRNA-seq data, specifically within the hematological system. Immune cells are crucial for human health, and recent single-cell technologies have enhanced the study of these cells by addressing cellular heterogeneity that bulk sequencing cannot resolve. Despite various existing methods for cell annotation, there is a notable gap in tools specialized for large-scale blood cell atlas. scPANDA addresses this by leveraging a comprehensive atlas of over 10 million cells derived from 16 studies, facilitating accurate and specialized annotation.

The atlas integrated data through a bioinformatics pipeline using Scanpy and CellHint, where raw data underwent rigorous quality control, preprocessing, and integration to ensure high-quality input. The atlas was organized hierarchically into 16 compartments, 54 classes, 4,460 low-level clusters (*pd\_cc\_cl\_ tf*s), and 611 high-level clusters (*pmid\_ct*s), with iterative clustering and harmonization steps to ensure cell type purity. DEGs and enrichments across different age groups, genders, and disease statuses within the atlas were explored, respectively, conveying insights into how cellular functions and responses vary with age, gender, and disease conditions.

Relying on three reference matrices built by performing DE analysis of the atlas, scPANDA follows a

**Figure 7. Deconvolved TCGA cancer bulk RNA-seq datasets using the scPANDA as reference.**

TCGA: The Cancer Genome Atlas; ACC: adrenocortical carcinoma; BLCA: bladder urothelial carcinoma; BRCA: breast invasive carcinoma; CESC: cervical squamous cell carcinoma and endocervical adenocarcinoma; CHOL: cholangiocarcinoma; COAD: colon adenocarcinoma; DLBC: diffuse large B-cell lymphoma; ESCA: esophageal carcinoma.


## 关键词

Article, Chin, Med, Research, Sci

## 相关实体

方法: scRNA-seq, single-cell
疾病: disease

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
