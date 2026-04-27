---
marker_extracted: true
title: "A fast, scalable and versatile tool for analysis"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/a-fast-scalable-and-versatile-tool-for-analysis.md]
confidence: medium
year: 2024
---
marker_extracted: true

# A fast, scalable and versatile tool for analysis

> 原文: [[a-fast-scalable-and-versatile-tool-for-analysis]]

## 摘要

number of cells23,24. Deep neural network models, known for their high identifying unique cell clusters and revealing biological patterns. The training costs, often require specialized computational hardware such functional enrichment module offers detailed data interpretation like as graphics processing units (GPUs) to be computationally feasible. differential accessibility and motif analysis. Finally, the multimodal In this study, we describe a nonlinear dimensionality reduction omics analysis part allows for the examination of complex and mul- algorithm that achieves both computational efficiency and accuracy tifaceted biological datasets, combining different types of biological in discerning cellular composition of complex tissues from a broad data, and building networks to understand gene regulation. spectrum of single-cell omics data types. The key innovation of our algorithm is the use of a matrix-free spectral embedding algorithm Efficient and accurate cell embedding for scATAC-seq data to project single-cell omics data into a low-dimensional space that Spectral embedding, also known as Laplacian eigenmaps, is a widely preserves the intrinsic geometric properties of the underlying data. used technique for nonlinear dimensionality reduction29.

## 背景与目的

increase in runtime as the number of cells in the dataset expanded. We observed similar robustness in performance when assess- Neural network-based methods, despite their linear scalability, were ing noise levels. SnapATAC2 achieved perfect ARI scores (1.0) at all considerably slower. For example, SnapATAC2 took only 13.4 min to examined noise levels, followed closely by Signac and the original analyze a dataset with 200,000 cells, whereas PeakVI needed approxi- SnapATAC (Fig. 2d). In comparison, SCALE and PeakVI showed the most mately 4 h. sensitivity to noise, with their ARI scores dropping to 0.57 and 0.46, Regarding memory efficiency, SnapATAC2 stood out by requiring respectively, at a noise level of 0.4 (Fig. 2d,e). Moreover, SnapATAC2 only 21 GB of memory to process 200,000 cells (Fig. 1d). In contrast, excelled in identifying rare cell populations in simulated datasets the original SnapATAC package showed limitations, encountering with variable cell-type abundances (Extended Data Fig. 1). In sum- out-of-memory errors when handling over 80,000 cells on a server mary, our results demonstrate that SnapATAC2 is highly robust to both with 500 GB of available memory. cisTopic, although not constrained variable sequencing depths and noise levels, delivering consistently by memory, demonstrated the highest growth in runtime among high-quality embeddings. all tested methods (Fig. 1c,d).

## 主要发现

#### **An overview of the SnapATAC2 workflow**

SnapATAC2 is a comprehensive, high-performance solution for single-cell omics data analysis. Like the original SnapATA[C9](#page-9-17) , SnapA-TAC2 offers a wide range of functionalities to streamline the analysis of scATAC-seq data across multiple stages of the process. Moreover, SnapATAC2 is designed with flexibility in mind, intended for a variety of single-cell omics data types. For instance, its dimensionality reduction subroutine is readily applicable to scATAC-seq, scRNA-seq, single-cell DNA methylation and scHi-C data, showcasing its adaptability. To enhance performance and scalability, SnapATAC2 uses the Rust programming language for executing computationally intensive subroutines and provides a Pytho[n27](#page-9-7) interface for seamless installation and user-friendly operation. This combination allows for efficient processing of large-scale single-cell omics data while maintaining accessibility for researchers across various levels of expertise. To further improve scalability when handling large-scale single-cell data, on-disk data structures and out-of-core algorithms are used whenever possible. These modifications facilitate the analysis of large datasets without overburdening system resources. Additionally, SnapATAC2 is modular and adaptable, and allows users to tailor their analysis to specific requirements and integrate with other software packages from the scverse ecosystem, such as SCANPY and scvi-tools[14.](#page-9-9)

The SnapATAC2 package is made up of four main parts: preprocessing, embedding/clustering, functional enrichment analysis and multimodal omics analysis (Fig. [1a](#page-2-0)). The preprocessing module handles raw BAM files, assesses data quality, creates count matrices and spots doublets, ensuring a strong base for downstream analysis. The core of SnapATAC2 is its embedding/clustering module, which introduces a new algorithm for reducing data dimensions.


## 方法概述

#### Dimensionality reduction using spectral embedding

In this section, we outline the core algorithms used to perform dimensionality reduction in the SnapATAC2 package. We first describe the preprocessing steps and then the classic spectral embedding method that works for arbitrary similarity metrics. Finally, we describe the matrix-free spectral embedding algorithm that works only for cosine similarity, but substantially decreases the running time and memory usage. Note the steps described below can be accomplished using the 'snapatac2.tl.spectral' function from the SnapATAC2 package.

**Preprocessing.** Given a cell-by-feature count matrix $C \in \mathbb{R}^{n \times p}$ , we first scale the columns of the matrix by the inverse document frequency (IDF). The IDF of a column or a feature f is defined by $idf(f) = \log \frac{n}{1 + |i: C_{i,i} \neq 0|}$ .

**Spectral embedding.** Assuming the cell-by-feature count matrix C has been preprocessed according to the procedures described above, in classic spectral embedding, we first compute the $n \times n$ pairwise similarity matrix W such that $W_{ij} = \delta(C_{i*}, C_{j*})$ , where $\delta: \mathbb{R}^p \times \mathbb{R}^p \to \mathbb{R}$ is the function defining the similarity between any two cells. Typical choices of $\delta$ include the Jaccard index and the cosine similarity. We then compute the symmetric normalized graph Laplacian $L_{\text{sym}} = I - D^{-1/2}WD^{-1/2}$ , where I is the identity matrix and D = diag(W1). The bottom eigenvectors of $L_{\text{sym}}$ are selected as the lower-dimensional embedding. The corresponding eigenvectors can be computed alternatively as the top eigenvectors of the similarly normalized weight matrix: $\widetilde{W} = D^{-1/2}WD^{-1/2}$ .

**Matrix-free spectral embedding with cosine similarity.** In this section, we introduce a matrix-free algorithm for spectral embedding that avoids calculating the similarity matrix.


## 讨论与结论

In the present study, we describe SnapATAC2 for the analysis of a diverse array of single-cell omics data. The performance of SnapATAC2 exceeds that of existing dimensionality reduction methods in terms of accuracy,

noise robustness and scalability, thus providing researchers with a powerful tool for investigating gene regulatory programs using single-cell genomics, transcriptomics and epigenomics analysis.

SnapATAC2 offers a unique advantage in its seamless compatibility with other software tools widely used in the single-cell analytics ecosystem. By adopting the AnnData format, it facilitates effortless integration with established packages like SCANPY, scvi-tools and

, UMAP visualization of the embeddings generated by Higashi, SnapATAC2, scHiCluster and PCA for the 4DN dataset by Kim et al. Cells are color coded based on cell-type labels. **b**, Table displaying normalized scores (0–1 range) of four metrics used to evaluate each method's bio-conservation on the 4DN dataset by Kim et al. . **c**, Table displaying normalized scores (0–1 range) of four metrics used to evaluate

each method's bio-conservation on the Lee et al. dataset. **d**, Table displaying the bio-conservation scores of four dimensionality reduction methods across five benchmark datasets (Extended Data Fig. 7). **e**, UMAP visualization of the embeddings produced by the best performing method (SnapATAC2) and the worst performing method (scVI) for the Zhengmix4uneq dataset[35.](#page-9-33) Cells are color coded according to cell-type labels.

SCENIC+. This feature is especially advantageous for researchers seeking to carry out specialized analyses, such as data imputation or trajectory inference, thereby enhancing the core functions of SnapATAC2.

The key innovation of SnapATAC2 lies in its matrix-free spectral embedding algorithm for dimensionality reduction.


## 关键词

analysis, fast, scalable, tool, versatile

## 相关实体

方法: scRNA-seq, single-cell

---
marker_extracted: true

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
