---
marker_extracted: true
title: "Pertpy: an end-to-end framework for"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/pertpy-an-end-to-end-framework-for.md]
confidence: medium
year: 2024
---

# Pertpy: an end-to-end framework for

> 原文: [[pertpy-an-end-to-end-framework-for]]

## 摘要

experiment-specific pipelines, leading to more robust outcomes. To evaluate methods and obtained representations for perturbations, we Differential abundance Milo Dann et al.39 scCODA 2.0 Büttner et al.37 implemented a series of shared metrics. The wide array of use cases and tascCODA 2.0 Ostner et al.38 different types of growing datasets are addressed by pertpy through MCPs DIALOGUE Jerby-Arnon and its sparse and memory-efficient implementations, which leverage the Regev40 parallelization and graphics processing unit (GPU) acceleration library JAX15, thereby making them substantially faster than original imple- Enrichment Drug2Cell Kanemaru et al.67 mentations (Extended Data Fig. 1). We demonstrate this versatility by Perturbation response Distances and metrics Novel applying pertpy to three different, popular, single-cell RNA sequencing evaluation Augur Skinnider et al.68 CINEMA-OT Squair et al.69 (scRNA-seq) perturbation use cases. To show how pertpy can discover Dong et al.41 new gene programs, we study a CRISPR activation (CRISPRa) screen Embedding Perturbation spaces Novel (Perturb-seq)16, projecting it onto a meaningful perturbation space and evaluating the effect of different preprocessing strategies. Moreover, we demonstrate how pertpy can be used to deconvolve perturbation The first data transformation step assigns guide RNAs (gRNAs) to responses into viability-dependent and viability-independent compo- cells.

## 背景与目的

1 eneG 2 eneG n eneG MCP 1 MCP 2 1 eneG 2 eneG n eneG a b Knowledge inference Differential abundance Enriched in A A Enriched in B B * C * * D * E * * –1.0 0 1.0 log fold change project score 2 PRISM mondo Connectivity Map Disease Ontology CancerRxGene DepMap Human Phenotype Ontology Fig. 1 | Modules of the pertpy framework. a, Unimodal or multimodal single-cell successfully or not successfully perturbed. Together, these modules enable the perturbation data originating from genetic modifications, chemical treatments, calculation of a meaningful perturbation space. b, Pertpy enables downstream physical interventions, environmental changes or diseases are enriched with analyses, depending on the question of interest. These include differential metadata from several databases. During preprocessing, confounding factors expression analysis, response prediction, determination of MCPs, calculation of such as cell cycle and batch effects may be removed. Targeted cells are labeled as distance between perturbations and mechanism of action enrichment. Article for multiple conditions, batch effects and nested comparisons simulta- Built on the scverse14 ecosystem, pertpy ensures seamless interop- neously.

## 主要发现

#### **Pertpy enables fast and scalable perturbation analyses**

Pertpy includes methods for analysis of single and combinatorial perturbations covering diverse types of perturbation data, including genetic knockouts, drug screens and disease states. The framework is designed for flexibility, offering more than 100 composable and interoperable analysis functions organized in modules that further ease downstream interpretation and visualization (Table 1\). These modules host fundamental building blocks for implementation and methods that share functionality and can be chained into custom pipelines. To facilitate setting up these pipelines, pertpy guides analysts through a general analysis pipeline (Fig. 1\) with the goal of elucidating underlying biological mechanisms by examining how specific interventions alter cellular states and interactions.

The inputs to a typical analysis with pertpy are unimodal scRNA-seq or multimodal perturbation readouts stored in AnnData22 or MuData23 objects. Although pertpy is primarily designed to explore perturbations such as genetic modifications, drug treatments, exposure to pathogens and other environmental conditions, its utility extends to various other perturbation settings, including diverse disease states where experimental perturbations have not been applied.

| Analysis step | Tool or algorithm | Original authors |
|-------------------------------------|------------------------------------------------------|-----------------------------------------------------------------|
| Datasets | Data loaders | Peidli et al.43 |
| Metadata annotation | API requests to public<br>databases | Novel |
| gRNA assignment | Threshold-based<br>Poisson−Gaussian<br>mixture model | Adamson et al. 66<br>Repogle et al. 11 |
| Differential gene<br>expression | 'Formulaic' interface | Novel |
| Pooled CRISPR screens | Mixscape | Papalexi et al. 19 |
| Differential abundance | Milo<br>scCODA 2.0<br>tascCODA 2.0 | Dann et al.39<br>Büttner et al.


## 方法概述

#### **Implementation of pertpy**

Pertpy is implemented in Python and builds upon several scientific open-source libraries, including NumPy, Scipy71, JAX, scikit-learn72, Pandas72,73, AnnData22, scanpy, muon23, NumPyro74, OTT-JAX75, blitzG-SEA69, PyTorch76 and scvi-tools for omics data handling and matplotlib77 and seaborn78 for data visualization.

**Summary table of implemented methods.** Pertpy provides implementations of many novel, but also established, methods that can be easily accessed and combined to easily build custom analysis pipelines (Table 1\).

**gRNA assignment.** Assigning relevant guides to each cell is essential in genetic perturbation assays, ensuring that the observed cellular responses are accurately linked to the intended genetic modifications. This step is critical for validating experimental design and interpreting results reliably. Pertpy provides two approaches to assigning cells to guides.

First, a simple thresholding model where the most expressed gRNA is assigned to a cell if it additionally exceeds an optional user-specified count threshold.

Second, a previously published Poisson−Gaussian model11. For each guide, cells with non-zero expression are log2 transformed and modeled as a mixture of two populations, with cells automatically classified as negative if they show zero expression. A cell is labeled as positive for a guide if it belongs to the higher-expressing population, with a maximum of five guide assignments per cell to prevent over-assignment; cells exceeding this threshold are marked as 'multiple', whereas those failing to meet the mixture model threshold for any guide are designated as 'negative'.

**Differential gene expression.** Differential gene expression analysis compares the mean gene expression levels between different conditions or groups to identify genes with statistically significant changes, utilizing statistical models to account for between-sample variability and control for false discovery rates.


## 讨论与结论

Pertpy facilitates the end-to-end analysis of complex perturbation datasets with a versatile toolbox of interoperable components, encompassing metadata annotation, data analysis and visualization tools. Through shared infrastructure and modules and with collaboration with original authors, we developed improved versions of widely used methods that were originally unmaintained or easily available only to the R community, making them widely available to the Python community as well. Our community effort will ensure that all of these methods are jointly maintained and further developed. We demonstrated pertpy's flexibility through several use cases, including the identification of perturbation-specific gene programs using a CRISPRa screen (Perturb-seq) dataset, deconvolution of viability-related response signatures in a chemical perturbation dataset and deciphering treatment response to drugs in TNBC. Many further use cases can be found in pertpy's extensive online tutorials.

As perturbation datasets grow larger and incorporate additional modalities such as spatial transcriptomics, we anticipate the development of specialized methods for analyzing multimodal perturbation data. By combining efforts such as Squidpy and pertpy, additional functionality designed for spatial perturbations to uncover, for example, differentially regulated neighborhoods, could be made widely available. To scale to datasets with hundreds of millions of cells, such as the recently published Tahoe-100M63 dataset, further optimizations in

 | **Pertpy identifies complex perturbation effects in multicellular tissue as demonstrated on a TNBC treatment dataset. a**, Schematic overview of the experimental design. **b**, scRNA-seq of tissue from 15 patients with TNBC, comparing pre-treatment and post-treatment responses to anti-PD-L1 therapy and NACT. **c**, MSE distance between treatment responses shows higher distances between partial responses and stable disease.


## 关键词

Pertpy, end-to-end, framework

## 相关实体

方法: scRNA-seq, single-cell
疾病: disease

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
