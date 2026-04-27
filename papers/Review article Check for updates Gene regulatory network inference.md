---
marker_extracted: true
title: "Review article Check for updates Gene regulatory network inference"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/review-article-check-for-updates-gene-regulatory-network-inference.md]
confidence: medium
year: 2023
---

# Review article Check for updates Gene regulatory network inference

> 原文: [[review-article-check-for-updates-gene-regulatory-network-inference]]

## 摘要

The interplay between chromatin, transcription factors and genes generates complex regulatory circuits that can be represented as gene regulatory networks (GRNs). The study of GRNs is useful to understand how cellular identity is established, maintained and disrupted in disease. GRNs can be inferred from experimental data – historically, bulk omics data – and/or from the literature. The advent of single-cell multi-omics technologies has led to the development of novel computational methods that leverage genomic, transcriptomic and chromatin accessibility information to infer GRNs at an unprecedented resolution. Here, we review the key principles of inferring GRNs that encompass transcription factor-gene interactions from transcriptomics and chromatin accessibility data. We focus on the comparison and classification of methods that use singlecell multimodal data. We highlight challenges in GRN inference, in particular with respect to benchmarking, and potential further developments using additional data modalities.



## 背景与目的

Cells regulate gene transcription to coordinate cellular activities in response to intracellular and extracellular signals. Transcription is largely regulated by transcription factors (TFs), proteins that bind to specific sequences of DNA (DNA binding sites) and can have positive or negative effects on the transcriptional rate of target genes[1](#page-12-5) . Genomic DNA is tightly packed with structural proteins into complexes known as nucleosomes, which are the basic unit of chromatin, making most genes inaccessible to the transcription machinery. To enable transcription, the region near a gene transcription start site, known as the promoter, needs to be exposed by displacing tightly packed nucleosomes. Changes in DNA accessibility can be triggered by the binding of so-called pioneer TFs[2](#page-12-8) . Other TFs can bind to distal *cis*-regulatory elements (CREs) of the DNA and, together with cofactors and other proteins, cooperatively enable the recruitment and stabilization of the RNA polymerase protein complex that synthesizes mRNA from the gene body DNA (Fig. [1a](#page-2-0)).

Gene regulatory networks (GRNs) are interpretable computational models of the regulation of gene expression in the form of networks, mathematically also defined as graphs. Multiple components of gene regulation, such as TFs, splicing factors, long non-coding RNAs, micro-RNAs and metabolites, can be incorporated in GRNs. Here, we focus on their simplest representation, which captures only the interplay between TFs and target genes, whereby the nodes of the GRN consist of genes, some of them being TFs, and the edges of the GRN represent regulatory interactions between the genes (Fig. [1b](#page-2-0)). Other possible GRN representations are discussed elsewhere[3](#page-12-9)[–6](#page-12-10) . Uncovering the topology and the dynamics of GRNs is fundamental to understanding how cellular identity is established and maintained[7](#page-12-11) , which has important implications for engineeri


## 主要发现

have different coverage of TFs, and prediction algorithms model bind- ing differently, results between GRN inference methods might differ Box 1 even if they use similar modelling strategies. The majority of methods allow for using different TF binding motif databases than their default, Binding motif databases and but most methods fix the motif matcher algorithm used — except for SCENIC+67, which implements three algorithms, cisTarget67, DEM67 and motif matcher algorithms HOMER68. In addition, GRN inference methods use different genomic distance cutoffs to assign open chromatin regions to target genes. Some consider close distances up to 10 kb, others medium distances Generating genome-wide binding data for multiple transcription up to 100 kb, others large distal effects up to 1,000 kb and others do factors (TFs) requires laborious experiments, so methods for gene not specify the distance cutoff either in the original publication or in regulatory network (GRN) inference instead predict TF binding the source code (). Given that functionally validated interactions events on open genomic regions based on prior information.

## 方法概述

Bulk transcriptomics d In silico perturbation Original cell fates Perturbation N times propagation Predicted cell fates Pseudotime Expression Pseudotime Perturbation analysis Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 746 2 PAMU UMAP 1 2 PAMU Fig. 3 | Applications of gene regulatory networks. a, Topological analysis. or organisms. c, Inference of TF activity. GRNs can be coupled to enrichment Network centrality measures can be used to identify hubs of transcription factors methods to infer which TFs might be functionally active from transcriptomics (TFs) or genes within a gene regulatory network (GRN) that are highly connected. data. GRNs inferred from multi-omics data can then be used to infer TF activities Clustering of nodes based on their connectivity gives rise to sub-network in other contexts, such as independent single-cell, spatial or bulk transcriptomics modules that can be associated with biological functions. b, Comparative data. d, In silico perturbation experiments. GRNs can be used to simulate analysis. Comparison of the connectivities in different GRNs by the pairwise perturbation experiments by propagating changes in gene expression through subtraction of TF–gene interactions between GRNs can provide insight into the the network over short iterations. The obtained simulated gene expression rewiring of gene regulation between different cell types, individuals, conditions profiles can then be used to infer cell fate decisions.

## 讨论与结论

Advances in high-throughput, single-cell multimodal technologies together with computational methods are paving the way to increasingly accurate GRN inference models. The large scale of the data sets makes it increasingly possible to train deep learning methods to predict gene expression from sequencing data,,202. GRNs complement these approaches by giving a more interpretable model. Together, these different approaches might help us to better understand differences in gene regulation across cell types, organs, populations and species, and serve as tools to control cell fate decisions. In the biomedical field, such knowledge could enable the identification of novel drug targets that control pathophysiological processes in different diseases.

Published online: 26 June 2023


## 关键词

Check, Gene, Review, article, inference, network, regulatory, updates

## 相关实体

方法: single-cell
疾病: disease

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
