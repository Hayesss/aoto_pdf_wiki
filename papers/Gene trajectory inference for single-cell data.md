---
marker_extracted: true
title: "Gene trajectory inference for single-cell data"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/gene-trajectory-inference-for-single-cell-data.md]
confidence: medium
year: 2024
---

# Gene trajectory inference for single-cell data

> 原文: [[gene-trajectory-inference-for-single-cell-data]]

## 摘要

that GeneTrajectory extracts gene geometry without the need for Next, we construct a k-nearest neighbor (kNN) graph of cells based constructing cell pseudotime, revealing independent trajectories of on their relative distances in the cell embedding (Fig. 1c). This concurrent processes that are otherwise obscured by cell pseudotime establishes a cell–cell connectivity map that serves as the approaches. ‘roadmap’ for transporting gene distributions in the next step. Here, for a given pair of cells u and v, we search for the shortest Results path connecting them in the kNN cell graph and denote its length Computing optimal transport between genes over the cell as the graph distance dG(u,v) between cells u and v. This graph graph distance will be used to define the cost of transporting a point mass A progressive dynamic biological process is usually governed by a between cells u and v in the next step. finely regulated gene cascade25–27, in which genes are activated and • Compute gene–gene Wasserstein distances over the cell graph. deactivated in a temporal order along the process, dictating the We model the expression level of genes as discrete distributions transcriptomic changes of underlying cell states. Moreover, cells can on the cell graph. Specifically, we divide the original expression partic ipate in multiple processes simultaneously, either in a dependent level of a given gene in each cell by the sum of its expression level or independent manner.

## 背景与目的

simultaneously in the same group of cells. n Original number of genes m′ Reduced number of cells after coarse-graining GeneTrajectory resolves myeloid gene dynamics We demonstrate GeneTrajectory’s application using myeloid δ(p)(ρ,ρ′) Wasserstein-P distance between distributions ρ and ρ′ lineage differentiation, a classical biological system with a well-defined d E (u, v) Euclidean distance between cell u and v bifurcation of two major lineages38,39. We extracted human myeloid d (u, v) Graph distance between cells u and v cells from a public 10× Genomics peripheral blood mononuclear cell G (PBMC) dataset and identified four cell types based on canonical mark- C Transport cost matrix on the cell graph. C represents the cost of transport between cell u and v u,v ers (Fig. 3a and Extended Data Fig. 2b,c). These included CD14+ mono- cytes, intermediate monocytes with high expression of HLA-DR (Human C′ Transport cost matrix on the coarse-grained cell graph Leukocyte Antigen – DR isotype), CD16+ monocytes and myeloid type-2 M kNN membership matrix for the cell graph. M(u, a) = 1/∣a∣ if and dendritic cells. The UMAP visualization of the cell embedding shows a only if the cell u belongs to the ath subset, where ∣a∣ represents the number of cells in that subset; otherwise M(u, a) = 0 continuum of cell states underlying myeloid lineage genesis, compris- ing monocyte maturation and dendritic cell differentiation.

## 主要发现

#### **Computing optimal transport between genes over the cell graph**

A progressive dynamic biological process is usually governed by a finely regulated gene cascade–27, in which genes are activated and deactivated in a temporal order along the process, dictating the transcriptomic changes of underlying cell states. Moreover, cells can participate in multiple processes simultaneously, either in a dependent or independent manner. For instance, we illustrate two contrasting scenarios by considering the concurrence of a linear process (for example, differentiation) and a cyclic process (for example, CC; Fig. 1a\). When these two processes are strictly dependent on each other, they can be parameterized by a common latent variable and result in a one-dimensional cell curve. In this scenario, it is straightforward to assign a meaningful pseudotime for the cells by ordering them along the curve. However, deconvolving genes into two processes and retrieving their pseudotemporal order in each process is not immediately apparent, which requires additional postprocessing (for example, clustering gene dynamics along the cell pseudotime12\). In contrast, when these two processes are independent, cells fall into a manifold (as a Cartesian product of these two processes) with an intrinsic dimension >1. These processes do not share a common latent variable, thus gene dynamics inference based on unidimensional interpolation along the cell–cell manifold is no longer appropriate. In practice, the weak and stochastic nature of the dependency between concurrent biological processes can complicate the extraction of the cell path and the construction of cell pseudotime.

Here we present GeneTrajectory, an approach to inferring gene processes through learning the gene–gene geometry without one-dimensional parameterization of the cell manifold (Fig. 1b).


## 方法概述

#### Workflow

The major workflow of GeneTrajectory comprises the following four main steps. Core notations are listed in Table 1.

- Step 1—build a cell–cell kNN graph in which each cell is connected to its kNNs. Find the shortest path connecting each pair of cells in the graph and denote its length as the graph distance between cells.
- Step 2—compute pairwise graph-based Wasserstein distance between gene distributions, which quantifies the minimum cost of transporting the distribution of a given gene into the distribution of another gene in the cell graph.
- Step 3—generate a low-dimensional representation of genes (using diffusion map by default) based on the gene—gene Wasserstein distance matrix. Identify gene trajectories in a sequential manner.
- Step 4-determine the order of genes along each gene trajectory.

Step 1. Construct a cell-cell graph and define graph distances. *Data preprocessing*. The data preprocessing contains the following steps:

- standard preprocessing of the count matrix (*m* cells and *n* genes).
- (2) dimension reduction.

Standard preprocessing—the original count matrix (cell-by-gene) is first preprocessed by using the standard pipeline in single-cell analysis, including library normalization, top variable gene selection and scaling.

Dimension reduction—due to the low-rank nature of single-cell data, we run dimensionality reduction on the original count matrix to generate a low-dimensional representation of the cell geometry (cell embedding). Commonly used methods include PCA, t-SNE, UMAP and diffusion maps. By default, we apply PCA for the initial step of dimensionality reduction and retain the leading n (typically around 30–100) principal components (PCs). Then we use diffusion map to generate a manifold-preserving low-dimensional representation of cells. Specifically, for a given pair of cells u and v, we calculate the Euclidean distance $d_{\rm E}(u,v)$ between their coordinates of the leading u PCs.


## 讨论与结论

We developed GeneTrajectory, an approach for constructing gene trajectories where each trajectory comprises genes organized in a pseudotemporal order that characterizes the transcriptional dynamics of a specific biological process. GeneTrajectory uses optimal-transport-based gene—gene dissimilarity metrics. These metrics naturally leverage the underlying geometry of the cell—cell graph to reveal a coherent relation among genes that are involved in progressive processes. Importantly, GeneTrajectory bypasses the need for constructing cell pseudotime, which is a common requirement in existing methods. This renders it broadly applicable in scenarios where cells do not form into clear lineages.

It is worthwhile to note that cell trajectory inference and gene trajectory inference can complement each other to address different

types of questions. Cell trajectory inference aims to define biological processes by lineages of cells, while gene trajectory inference associates each process with a sequence of genes. As demonstrated above, when cells participate in concurrent processes, cell trajectory inference may fail to deconvolve them. Similarly, when one gene participates in multiple biological processes, theoretically, it should be placed at the joint of gene trajectories. However, if that gene is expressed across many cells, it may have a small Wasserstein distance to genes that are homogeneously expressed (uninformative genes). As a result, it will be colocalized with uninformative genes in the gene embedding, causing difficulty for GeneTrajectory to distinguish them. Moreover, there are multiple aspects of our proposed algorithm that could be further refined. For instance, the branch identification procedure requires interactive optimization and might exhibit instability if the branches differ substantially in length and size. In addition, GeneTrajectory cannot automatically infer the directionality of progression along each trajectory.


## 关键词

Gene, data, inference, single-cell, trajectory

## 相关实体

通路: differentiation
方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
