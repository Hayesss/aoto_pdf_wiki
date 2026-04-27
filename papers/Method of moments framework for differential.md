---
marker_extracted: true
title: "Method of moments framework for differential"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/method-of-moments-framework-for-differential.md]
confidence: medium
year: 2024
---

# Method of moments framework for differential

> 原文: [[method-of-moments-framework-for-differential]]

## 摘要

Differentialexpressionanalysisofsingle-cellRNAsequencing(scRNA-seq)dataiscentralforcharacterizing how experimental factorsaffectthe distribution ofgene expression. However, distinguishingbetween bio- logicalandtechnicalsourcesofcell-cellvariabilityandassessingthestatisticalsignificanceofquantitative comparisonsbetweencellgroupsremainchallenging.WeintroduceMemento,atoolforrobustandefficient differentialanalysisofmeanexpression,variability,andgenecorrelationfromscRNA-seqdata,scalableto millionsofcellsandthousandsofsamples.WeappliedMementoto70,000trachealepithelialcellstoidentify interferon-responsive genes, 160,000 CRISPR-Cas9 perturbed T cells to reconstruct gene-regulatory net- works, 1.2 million peripheral blood mononuclear cells (PBMCs) to map cell-type-specific quantitative trait loci (QTLs), and the 50-million-cell CELLxGENE Discover corpus to compare arbitrary cell groups. In all cases, Memento identified more significant and reproducible differences in mean expression compared with existing methods. It also identified differences in variability and gene correlation that suggest distinct transcriptionalregulationmechanismsimpartedbyperturbations. INTRODUCTION lished, maintained, and may be broken.

## 背景与目的

Gene expression, inherently determined by a cell's genetic constitution and its environmental interactions, can exhibit fluctuations due to both intrinsic noise (stemming from mRNA transcription and degradation) and extrinsic noise related to a cell's specific state.1, While genetics and environmental history significantly contribute to expression variability across a population of cells, stochastic transcriptional noise can also influence cellular responses to perturbations, as well as cellular development and differentiation.2–4 Characterizing how deterministic and stochastic factors jointly influence the distribution of gene expression is central to understanding how transcriptional control is established, maintained, and may be broken. These insights could illuminate mechanisms underlying phenomena where genotype-phenotype relationships are not completely explained, such as destabilization, incomplete penetrance, and variable expressivity.

The distribution of gene expression within a population of cells is primarily characterized by its mean and variance and related derived measures. Constitutively expressed housekeeping genes, which undergo transcription and degradation at constant rates, are predicted to conform to a Poisson distribution. Nonetheless, most genes display over-dispersion, exhibiting higher variance than expected, and genes within the same biological pathway are often transcriptionally correlated. These

*(legend on next page)*

observations are consistent with a model where the expression of related genes is regulated by similar *cis-*regulatory elements that interact with a common set of transcription factors that cycle between ''on'' and ''off'' states. Until recently, studying the distribution of gene expression, in particular the joint distribution of multiple genes, has been technologically challenging and has been mostly pursued in model organisms that can be genetically modified.


## 主要发现

#### Statistical model of scRNA-seq

Since its advent, scRNA-seq has yielded sparse data despite continuous advancements in molecular biology, manifesting in a high degree of cell-to-cell variability even in genetically identical cells exposed to the same environment (Figure 1A). Decomposing this variability into components of biological and measurement noise is pivotal for differential expression analysis of scRNA-seq data.

Here, we propose a statistical framework that models observed scRNA-seg counts as the result of hypergeometric sampling of the expressed transcripts within a cell. The motivation to implement the hypergeometric model stems from the observation that the capture of poly-adenylated mRNA for reverse transcription (RT) and sequencing of resultant libraries are processes that sample molecules from each cell without replacement, thereby introducing measurement noise into the final dataset. Central to our model is the flexibility to accommodate arbitrary distributions of gene expression within a cell prior to measurement. Formally, let $\boldsymbol{X}_c = \frac{\boldsymbol{Z}_c}{N_c}$ denote an m -dimensional random variable representing the normalized transcript counts of m genes in cell c, where $\mathbf{Z}_c$ defines a vector of the expressed transcript counts and $N_c$ the total transcript counts within a cell. We model scRNA-seq as a multivariate hypergeometric sampling process, wherein the observed transcript counts Yc originate from $X_c$ : $Y_c \sim \text{MultiHG}(N_cX_c, N_c, N_cq)$ . In this representation, q signifies the overall transcript sampling efficiency of scRNA-seg and is associated with measurement noise introduced during library preparation and sequencing (see STAR Methods for detailed exploration). Importantly, we empirically substantiate that the two-step noise process involving RT (hypergeometric) and sequencing (binomial) can be well represented with a single step of hypergeometric sampling with the overall q (Figure S1A).


## 方法概述

0.2 0.3 50607080 50607080 50607080 Number of individuals memento pseudobulk ncM / mye cM / mye NK / nk T8 / nk T8 / T T4 / T B / B B T4 T8 NK cM ncM 0 5 cell type zscore of rank sum statistic G G/G G/A A/A G/G G/A A/A I A/A A/G G/G A/A A/G G/G B T kn dioleym Memento B T4 T8 NK cM ncM cell type B T kn dioleym Pseudobulk 6 5 4 3 2 1 Enrichment -Log10(P) ll Resource OPENACCESS (legendonnextpage) Cell187,6393–6410,October31,2024 6403 ll OPENACCESS Resource knocked out, lead to decreased expression of the DMGs. they are hampered by computational inefficiency, a restricted Consistent with our expectations, TR-DMGs typically show a focusonmeancomparisons,andsusceptibilitytomisspecifica- positive correlation with each other within WT cells (Binomial tionintheunderlyingparametricmodel.

## 讨论与结论

Fueled by the development of scalable workflows, there is an emergence of scRNA-seq datasets where the quantitative comparison of gene expression distributions between groups of cells is a critical task. These include endeavors to compare single-cell expression profiles between experimental conditions, disparate genetic perturbations induced by genome editing,,54 and individuals inheriting different alleles.16–18 Initial observations that experimental and genetic perturbations predominantly induce subtle shifts in gene expression rather than unequivocal cell states have highlighted the need for methods adept at comparing gene expression distributions. However, scalable computational methods that facilitate hypothesis testing over large numbers of cells and an extensive array of covariates (e.g., hundreds of *in vitro* perturbations or millions of genetic polymorphisms) are still scarce. Moreover, even fewer methods currently test for differences in the variability of gene expression and gene correlations, unique parameters captured by scRNA-seq.

Figure 6. Extending Memento for near realtime differential expression analysis within CZI CELLxGENE Discover

- (A) UMAP of the SLE PBMC dataset within CELLxGENE.
- (B) Enumeration of different comparisons that can be made within and between groups of cells.
- (C and D) Comparisons of significance (*p* value) between the precomputed and full modes for (C) differential mean and (D) differential variability analyses.
- (E) Runtime as a function of the number of comparisons made at query time (excluding precomputation).
- (F) Schematic of multiple datasets analyzed with CELLxGENE identifying DMGs between pDCs and cDCs.
- (G) QQ-plot of *p* values from comparing pDCs and cDCs combining many datasets (cyan) and using each dataset alone (gray).

See also Figure S6.

Here, we introduced Memento, an endto-end method for the quantitative analysis of scRNA-seq data theoretically scalable to millions of cells.


## 关键词

Method, differential, framework, moments

## 相关实体

细胞类型: all
方法: CRISPR, scRNA, scRNA-seq

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
