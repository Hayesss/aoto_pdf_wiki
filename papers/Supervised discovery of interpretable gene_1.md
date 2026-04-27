---
title: "Supervised discovery of interpretable gene"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/supervised-discovery-of-interpretable-gene.md]
confidence: medium
year: 2023
---

# Supervised discovery of interpretable gene

> 原文: [[supervised-discovery-of-interpretable-gene]]

## 摘要

methods, enabling it to identify more interpretable factors and dis- macrophages), leaving Spectra to infer factors associated with finer cover new biology. First, Spectra uses known cell-type information and cell-type distinctions, such as T cell activation or macrophage polariza- allows for cell-type-specific factors. Second, Spectra represents exist- tion (Fig. 2b, Extended Data Fig. 1, Supplementary and Meth- ing gene sets as an input gene–gene knowledge graph, enabling their ods). Fitting the Spectra model with default parameters (Methods) and data-driven modification and the derivation of entirely new factors. our cell-type labels and immunology knowledge base as input resulted Cell-type labels are provided as input to Spectra, which models the in 152 global and 45 cell-type-specific factors, the latter including CD4+ influence of a factor on gene expression relative to baseline expression T cells (n = 12), CD8+ T cells (n = 7) and myeloid cells (n = 6). per cell type, thereby mitigating its influence on the factors. The ability We determined overlap with known gene sets to assess whether to incorporate cell-type-specific factors guides inference. For example, Spectra can identify biologically interpretable programs.

## 背景与目的

–0.6 –0.8 –1.0 erocs llec naeM LPS perturbation LPS response factor 10 B T/ILC M slleC Fig. 1 | Spectra uses gene sets and cell types to guide gene program discovery base. c, Design of the perturbation experiments from Kartha et al.8. PBMCs from scRNA-seq data. a, As input, Spectra receives a gene expression count (n = 23,754) from healthy human donors (n = 3) were incubated for 6 h with LPS, matrix with cell-type labels for each cell as well as predefined gene sets, which it PMA or recombinant human IFNγ. d, Ability of different algorithms to identify converts to a gene–gene graph. The algorithm fits a factor analysis model using gene programs associated with biological perturbations in the PBMC dataset. a loss function that optimizes reconstruction of the count matrix and guides For select factors, mean per-donor cell scores are provided for T cells or innate factors to support the input gene–gene graph. As output, Spectra provides lymphoid cells (T/ILCs), B cells (B) and myeloid cells (M; n = 3 donors). Boxes factor loadings (cell scores) and gene programs corresponding to cell types and and lines represent interquartile range (IQR) and median, respectively; whiskers cellular processes (factors). b, Gene set categories in the immunology knowledge represent 1.5× IQR. Article (Extended Data Fig. 4). Spectra overcomes pleiotropy by implicitly down- coexpressed in the same cells.

## 主要发现

PDIA6 CD8 T AASS PIPOX TMLHE CANX CD4 T Glu FKBP2 B naive ALDH7A1 SEC61G PYCR2/3 BBOX1 SERP1 B mem NH 3 AADAT HERPUD1 B GC PIP SEC1 SLC25A15 DNAJB9 HSPA5 Acetyl-CoA SELENOS SSR4 HSP90B1 FKBP11 Input gene ERLEC1 New gene (Spectra) FKBP2 R ex e p la r t e iv ss e i on 0.15 0.30 0.45 0.60 0.75 0.90 P fr o a s c i t t i i o v n e 0.8 0.6 0.4 0.2 c Factor 103: Lysine metabolism Factor 103: Lysine metabolism Bassez et al. Cell score Zhang et al. Cell score Input Bassez et al. 0.14 0.35 2 20 0.12 0.30 4 AADAT 0.10 0.25 XBP1 11 HERPUD1 AASS 0.08 0.20 ALDH7A1 1 17 E FK R B LE P C 2 1 BBOX1 0.06 0.15 IGKC PIPOX 0.04 0.10 SLC3A1 ITM2C SLC7A1 0.02 0.05 MYDGF 21 PDIA6 SLC7A2 0 0 SPCS1 SDF2L1 SPCS3 Zhang et al. SEC11C TMLHE SEC61B SERP1 SSR3 SSR4 TMED2 TMEM59 TPT1 overlapping cellular neighborhoods (states) that only expand under (ref. 69)), some of which suppress inflammatory cytokine (IL-6 and anti-PD-1 therapy in non-responders (Fig. 5b) and are high in the novel TNF-α) release65. Our results suggest that in individuals who do not invasion program (Fig. 5c). This invasion program does not correspond respond to ICT, macrophages may upregulate these genes coordinately to input gene sets (η = 0.24) but has high importance and information (Fig. 5d). By focusing on residual expression that is not well explained scores; moreover, Slalom6 and scHPF4 do not identify a similar pro- by the gene knowledge graph, Spectra can thus find a gene program gram (Extended Data Fig. 8e–g).

## 方法概述

Nat. Immunol. 20, 326–336 (2019). stress and regulates metabolism. Nat. Commun. 10, 947 (2019). 25. Siddiqui, I. et al. Intratumoral TCF1+PD-1+CD8+ T cells with 46. Sharma, R. B., Darko, C. & Alonso, L. C. Intersection of the ATF6 stem-like properties promote tumor control in response to and XBP1 ER stress pathways in mouse islet cells. J. Biol. Chem. vaccination and checkpoint blockade immunotherapy. Immunity 295, 14164–14177 (2020). 50, 195–211 (2019). 47. Vekich, J. A., Belmont, P. J., Thuerauf, D. J. & Glembotski, C. C. 26. Schmid, P. et al. Pembrolizumab for early triple-negative breast Protein disulfide isomerase-associated 6 is an ATF6-inducible cancer. N. Engl. J. Med. 382, 810–821 (2020). ER stress response protein that protects cardiac myocytes from 27. Liu, B., Zhang, Y., Wang, D., Hu, X. & Zhang, Z. Single-cell ischemia/reperfusion-mediated cell death. J. Mol. Cell. Cardiol. meta-analyses reveal responses of tumor-reactive CXCL13+ T cells 53, 259–267 (2012). to immune-checkpoint blockade. Nat. Cancer 3, 1123–1136 48. Ricci, D., Gidalevitz, T. & Argon, Y. The special unfolded (2022). protein response in plasma cells. Immunol. Rev. 303, 35–51 28. Liu, X. et al. Genome-wide analysis identifies NR4A1 as a key (2021). mediator of T cell dysfunction. Nature 567, 525–529 (2019). 49. Dennler, P., Fischer, E. & Schibli, R. Antibody conjugates: from 29. Chowdhury, P. S., Chamoto, K., Kumar, A. & Honjo, T. heterogeneous populations to defined reagents.

## 讨论与结论

and global factors, allowing Spectra to effectively deal with expression of this approach is its flexibility. Gene sets are naturally incorporated variance at multiple scales. To perform this cell-type-integrative factor into a graph by forming fully connected cliques among members analysis, for cell type c and cell i, the model is extended to of each set. Further, more complex prior knowledge graph structures can 𝔼𝔼𝔼Xcij]=(gj+δ)α⊤ c,i,∶K θj+(gcj+δ)α⊤ c,i,K+1∶ θcj be used as input, for example, arising from gene programs esti- mated from a separate dataset or cell atlas. Most importantly, the where c is the cell-type label for cell i, g is cell-type-specific gene scal- structure of this input gene–gene graph can be improved by fitting cj ing, and θcj∈ΔKc−1 is a cell-type-specific gene representation with it to the data and learning gene programs that are more faithful to αc,i∈ℝK+Kc. Single-subscript variables, such as g j and θ j , denote global the data. parameters, whereas the notation α indicates the first K elements of A second advantage of the graph prior is its scalability. Although :K a vector (typically denoting global elements), and α indicates the gene sets may be highly overlapping, especially when curated from K+1: tail of the vector from the K + 1st element (typically denoting several separate databases, this redundancy is eliminated when stor- cell-type-specific elements).

## 关键词

Supervised, discovery, gene, interpretable

## 相关实体

细胞类型: T cell, macrophage, myeloid

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
