---
marker_extracted: true
title: "Corrected: Author Correction Characterization of cell fate probabilities in"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/corrected-author-correction-characterization-of-cell-fate-probabilities-in.md]
confidence: medium
year: 2026
---

# Corrected: Author Correction Characterization of cell fate probabilities in

> 原文: [[corrected-author-correction-characterization-of-cell-fate-probabilities-in]]

## 摘要

October 2018 Corresponding author(s): Dana Pe'er Last updated by author(s): Jan 29, 2019 Reporting Summary Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Research policies, see Authors & Referees and the Editorial Policy Checklist. Statistics For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section. n/a Confirmed The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly The statistical test(s) used AND whether they are one- or two-sided Only common tests should be described solely by name; describe more complex techniques in the Methods section. A description of all covariates tested A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals) For null hypothesis testing, the test statistic (e.g.

## 背景与目的

of diffusion components) that are outliers in the stationary distri- trend in all lineages as cells commit11, whereas lineage-specific fac- bution—that is, the states into which the random walks converge tors such as CD79A, GATA1, and IRF8 are selectively upregulated (Fig. 1c). Once the terminal states are identified, we convert them in the lymphoid, erythroid, and dendritic cell lineages, respectively. to absorbing states with no outgoing edges. In an absorbing Markov MPO shows an initial upward trend across all lineages, which is chain, a random walk from any state will continue until it reaches subsequently maintained only in the monocyte lineage (Fig. 2f). a terminal absorbing state.

## 主要发现

**Development as a Markov process.** Differentiation proceeds through cell divisions, where daughter cells are generally very similar to their mother cells. Thus, the population is established by incremental divergences, driven by regulatory mechanisms that create paths through the space of possible cell states (phenotypes). Regulation constrains cell states to a low-dimensional manifold of possible phenotypes. Nearest-neighbor graphs, where each node represents a particular cell state and edges connect most similar cells, have been widely used to model this manifold<sup>1-3,13</sup>.

A single bone marrow sample contains the full spectrum of cell states in hematopoiesis and importantly the frequencies of each cell state. We leverage cell state frequencies to inform our model of possible differentiation paths in the neighbor graph and their likelihoods. Critically, paths along the graph represent probable trajectories of cells in the population rather than the path of a particular cell, and each cell state (graph node) is associated with a probability distribution for reaching the terminal states. We assert that cells traverse the manifold in small steps which can be modeled using a Markov chain to represent cell fate choices in a probabilistic manner, based on two key assumptions. Firstly, as in all pseudo-time inference algorithms<sup>1,3,7,8</sup>, we assume unidirectional progression from a less- to a more-differentiated state. We posit that it is a reasonable first order approximation for healthy differentiation, but note that it fails in aberrant systems such as cancer, which require additional information (for example, mutations) to determine directionality. Second, we assume that for any node, the probability of traversing to any neighbor is independent of its history, that is, the path taken to reach that state.


## 方法概述

scRNA-seq of CD34+ human bone marrow cells. Cryopreserved bone marrow stem/progenitor CD34+ cells from healthy donors were purchased from AllCells, LLC. (catalog no. ABM022F) and stored in vapor phase nitrogen until use. Typical for scRNA-seq, a vial was removed from the storage and immediately thawed at 50-ml conical tube. To prevent osmotic lysis and ensure gradual loss of cryoprotectant, 1 ml of warm medium (IMDM with 10% FBS supplement) was added dropwise, while gently shaking the tube. Then, the cell suspension was serially diluted 5 times with 1:1 volume additions of complete growth medium with 2-min wait between additions. The final ~32-ml volume of cell suspension was pelleted at 300g for 5 min. After removing supernatant, cells were washed twice in ice-cold 1× PBS with 0.04% (wt/vol) BSA supplement to remove traces of medium. Cell concentration and viability were determined with a Countess II automatic cell counter employing the trypan blue staining method.

scRNA-seq was performed with 10X genomics system using Chromium Single Cell 3' Library and Gel Bead Kit V2 (catalog no. 120234). Briefly, 8,700 cells (viability 90–97%) were loaded per reaction, targeting recovery of 5,000 cells with 3.9% multiplet rate. After reverse transcription reaction emulsions were broken, barcoded complementary DNA was purified with DynaBeads, followed by 12 cycles of PCR amplification. The resulting amplified cDNA was sufficient to construct next-generation sequencing libraries, which were sequenced on an Illumina HiSeq 2500 system (HiSeq SBS V4 chemistry kit).

scRNA-seq data processing. Data preprocessing. Data derived from each replicate were processed independently. scRNA-seq data were preprocessed using the SEQC pipeline using hg38 human genome and the default SEQC parameters for 10X to obtain the molecule count matrix.


## 讨论与结论

Unlike existing algorithms, Palantir generates a probabilistic model of cell fate choice as a continuous process. Palantir is robust to parameters, reproducible across replicates, and generalizes to diverse datasets. Palantir's high-resolution mapping of cells along differentiation trajectories allowed us to characterize the order and timing of regulatory factors that drive lineage choices in hematopoiesis. Our findings clarified that DP drops gradually during the progression from stem to differentiated cells and is hierarchical, such that cells are predisposed sequentially toward lymphoid, erythroid, and finally myeloid lineages (potential drops gradually within each lineage).

The key to Palantir's high resolution in pseudo-time is the use of multiple diffusion components and neighbor graphs to measure distances between cells in this embedded space (Supplementary Fig. 23a-c). This enables Markov chain construction, which is central to both terminal state identification and modeling continuities in lineage choices. Palantir outperforms other pseudo-time algorithms, which largely treat lineage choices as discrete bifurcations, in recovering biologically consistent gene expression trends and lineage relationships. Enrichment of stem and precursor cells from bone marrow was necessary to characterize lineage choices in early human hematopoiesis at high resolution. However, Palantir can robustly recover expression trends in datasets for which precursors are not enriched.

We anticipate that Palantir will be a valuable discovery tool for many less-characterized systems, including those profiled by the Human Cell Atlas Projec[t43.](#page-8-42) A key requisite is the presence of the full range of differentiating cells, made possible by the asynchronous nature of differentiation in tissues such as bone marrow, colon, and olfactory epithelium,[,35](#page-8-34). We note that this is not a feature of embryogenesis, which is typically studied using time course experiments[,44.


## 关键词

Author, Characterization, Corrected, Correction, cell, fate, probabilities

## 相关实体

细胞类型: all
通路: Differentiation

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
