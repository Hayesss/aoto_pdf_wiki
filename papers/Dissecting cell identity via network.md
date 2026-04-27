---
marker_extracted: true
title: "Dissecting cell identity via network"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/dissecting-cell-identity-via-network.md]
confidence: medium
year: 2023
---

# Dissecting cell identity via network

> 原文: [[dissecting-cell-identity-via-network]]

## 摘要

Article Dissecting cell identity via network inference and in silico gene perturbation Kenji Kamimoto1,2,3, Blerta Stringa1,3, Christy M. Hoffmann1,2,3, Kunal Jindal1,2,3, Lilianna Solnica-Krezel1,3 & Samantha A. Morris1,2,3 ✉ Received: 4 January 2022 Accepted: 28 December 2022 Cell identity is governed by the complex regulation of gene expression, represented Published online: 8 February 2023 as gene-regulatory networks1. Here we use gene-regulatory networks inferred from Open access single-cell multi-omics data to perform in silico transcription factor perturbations, Check for updates simulating the consequent changes in cell identity using only unperturbed wild-type data. We apply this machine-learning-based approach, CellOracle, to well-established paradigms—mouse and human haematopoiesis, and zebrafish embryogenesis— and we correctly model reported changes in phenotype that occur as a result of transcription factor perturbation.

## 背景与目的

state in response to a TF perturbation, projecting the results onto the cell negative perturbation scores (shown in log scale). Dashed lines represent trajectory map (right). b, Force-directed graph of 2,730 myeloid progenitor cut-off values corresponding to false-positive rate (FPR) = 0.01. Genes are cells from Paul et al.16. Twenty-four cell clusters (Louvain clustering) were classified into four categories on the basis of their previously reported functions organized into six main cell types. Mk, megakaryocytes. c, Differentiation (Supplementary ). The asterisk refers to Supplementary Fig. 11, where vectors for each cell projected onto the force-directed graph. d, CellOracle we expand on the predicted phenotype.

## 主要发现

2.0 1 1.5 0 1.0 –1 0.5 0 –0.5 –1.0 FA1 2AF a b c Notochord GRN Prechordal plate GRN Pseudotime Pseudotime gradient vector Notochord Early AM Prechordal plate Notochord Late differentiation Early Prechordal plate differentiation FA1 0.1 0.2 0.3 2AF noto noto mix1l mix1l sox11b lhx1a foxa2 sox11b foxd3 foxd3 vox vox sox3 sox11a sox11a foxa lhx1a foxd5 foxa meox1 foxd5 foxa2 meox1 klf17 cdx4 sox3 sox19a sebox tbx16 foxe3 sebox bhlha15 gsc vent hoxb1b tbx16 sp5l gsc twist2 sox19a gata5 ved nkx1.2la foxp1b eve1 six7 foxa1 foxa1 shox2 zgc:110425 irx3a pitx2 zic2b gbx1 six3b zgc:174153 ved gata5 vent ctslb 0.1 0.2 0.3 Degree centrality Degree centrality Fig. 3 | CellOracle KO simulation with zebrafish embryogenesis data. prechordal plate (right). Black text denotes TFs. Grey text denotes non-TFs. a, Two-dimensional force-directed graph of the axial mesoderm (AM) d, Expression of noto projected onto the axial mesoderm sub-branch. e, Noto sub-branch (n = 1,669 cells) in a published zebrafish embryogenesis atlas KO simulation vector and perturbation scores. f, Markov simulation to estimate (Farrell et al.32).

## 方法概述

#### **CellOracle algorithm overview**

The CellOracle workflow consists of several steps: (1) base GRN construction using scATAC-seq data or promoter databases; (2) scRNA-seq data preprocessing; (3) context-dependent GRN inference using scRNA-seq data; (4) network analysis; (5) simulation of cell identity following TF perturbation; and (6) calculation of the pseudotime gradient vector field and the inner-product score to generate perturbation scores. We implemented and tested CellOracle in Python (versions 3.6 and 3.8) and designed it for use in the Jupyter notebook environment. CellOracle code is open source and available on GitHub \(https://github. com/morris-lab/CellOracle), along with detailed descriptions of functions and tutorials.


## 讨论与结论

The emerging discipline of perturbational single-cell omics enables regulators of cell identity and behaviour to be modelled and predicted . For example, scGen combines variational autoencoders with latent

Fig. 5 | Experimental validation of lhx1a as a putative regulator of zebrafish axial mesoderm development. a, Top 30 TFs according to predicted KO effects. Red and \*: previously reported notochord regulators (Supplementary Table 2). *lhx1a*, *sebox* and *irx3a* were selected for experimental validation. **b**. lhx1a LOF simulation in the axial mesoderm sub-branch, predicting an inhibition of axial mesoderm differentiation from early stages. c, scRNA-seq validation of experimental LOF: cell cluster composition of the axial mesoderm clusters normalized to the whole cell number in lhx1a and tyr (control) crispant samples. Early notochord is significantly expanded ( $P = 1.34 \times 10^{-35}$ , chi-square test) and differentiated axial mesoderm populations are significantly depleted (notochord: $P = 3.83 \times 10^{-3}$ ; prechordal plate: $P = 1.28 \times 10^{-7}$ , chi-square test) in lhx1a crispants. d, lhx1a and tyr crispant axial mesoderm cells at 10 hpf. Left, cell type annotation of *lhx1* and *tyr* crispant cells. Right, *lhx1a* and control crispant data projected onto the WT UMAP. **e**, Control cell density (left, n = 2,342 cells) and lhx1a crispant cell density (right, n = 2,502 cells). **f**, Rug plot showing the

difference in averaged NMF module scores between lhx1a and tyr crispants in notochord lineage cells. Black, cell-type-specific modules. Light grey, broad cluster modules. CM, cephalic mesoderm. g, Violin plot of NMF module score in notochord lineage cells (n = 1.918 lhx1a crispant and n = 2.616 tyr crispant cells. h, Violin plots of gene expression in the notochord (NC) lineage cells. \*\*\*\*P < 0.0001, two-tailed Wilcoxon rank-sum test with Bonferroni correction. i, Quantification (number of spots in flattened HCR image) normalized to WT.


## 关键词

Dissecting, cell, identity, network, via

## 相关实体

通路: differentiation
方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
