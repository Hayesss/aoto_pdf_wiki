---
marker_extracted: true
title: "OmicVerse: a framework for bridging and"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/omicverse-a-framework-for-bridging-and.md]
confidence: medium
year: 2024
---

# OmicVerse: a framework for bridging and

> 原文: [[omicverse-a-framework-for-bridging-and]]

## 摘要

lutionalgorithms,suchasTAPE23,CIBERSORT(CS)24,MuSiC25,CIBER- thesamplingofsingle-celldata,withtheproceduraldetailsoutlinedin SORTx(CSx)26,andBisque27,whicharenotreallyeffectiveinsolving the “Methods” section. This process is facilitated by a deep neural the“omitted”cellproblembecausetheylackagenerativecapability. network(DNN)-basedautoencodermodel,wherethesimulatedBulk ThissuggeststhatGenerativeAdversarialNetworks(GANs)maybethe servesasinput,theencoder’soutputreflectstheproportionsofactual bestsolutiontothe“omitted”cellproblem. cells,andthesimulatedBulkconstitutesthedecoder’soutput.Mean To address these challenges, we have developed OmicVerse absolute error (MAE) is used as the evaluation metric for both the ( a comprehensive Python library encoderanddecoder.Subsequenttomodelconvergence,therealBulk designedfortranscriptomicresearch.OmicVersestreamlinesaccessto dataisutilizedasinputfortheAEmodel,withthecriticalrequirement a spectrum of models and algorithms for bulk-seq and scRNA-seq beingthealignmentofthegeneration,basedonthebest-pretrained analyses,improvingcomputationalefficiencyandvisualengagement. decoder,with the real Bulkdata.Atthis point,the cell proportions Rewritten models and algorithms and integrated different pre- outputbytheencoderaccuratelyreflectthecellproportionsofthe processing options stem from benchmark testing28 (Supplementary actualBulk(Fig.1a). Note1).

## 背景与目的

c d e f Expression Correlation Marker Similarity Interpolation Density of (Unique) (Unique) Transformation pseudotime Gene 1->N Continuous Matrix Attr: Celltype Cell 1->J Cell 1->J Generate RNA-seq Inference Predicted Cell 1->M+j (j<J) Connectivities network Community Gene 1->N - Cell 1 - Cell 2 - Cell 3 - Cell 4 Continuous cell m θ ax log p (A|F) interpolation Cell 1->K Article Step1: Simulated Bulk Step2: AE training and fine-tuning Step3: VAE training Step4: Noisy Filtered NatureCommunications|( 2024)1 5:5983 3 Article Fig.1|ArchitectureoftheBulkTrajBlendframework.aSingle-CellProfileGen- celltypesfortheoverlappingCelltypes.cCorrelationScoreofCell-TypeMarker erationinBulkTrajBlend:Thisstageoutlinesthecreationofsingle-cellprofiles.An GeneExpression:Thiscomponentdisplayscorrelationscoresforcell-typemarker initialsingle-cellprofile,representingthegroundtruthforcellfractions,and geneexpressionacrossthreemodelswithintheDentateGyrusandHematopoietic simulatedbulktranscriptomedataareinputintoanautoencoder(AE).Simulta- datasets.dCell-TypeMarkerSimilarityAssessmentUsingCosineSimilarity:This neously,realbulktranscriptomedataserveastheoptimalinputfortheAE.TheAE’s partaddressestheassessmentofsimilaritiesbetweencell-typemarkergenesusing predictedcellfractionsdefinetheclusteringspaceoftheresultingsingle-cell cosinesimilarity.

## 主要发现

#### Design concept of BulkTrajBlend and Benchmarking

The conceptualization of BulkTrajBlend draws upon prior research, proposing that Bulk RNA-seq data is a composite of scRNA-seq data through a nonlinear superposition mechanism29,. Central to this notion is the implementation of the beta-variational autoencoder (β-VAE), a potent tool for approximating Bulk RNA-seq data to scRNA-seq representation31,32. Integrating the β-VAE enables the construction of an encoder and decoder from single-cell data, traditionally characterized by unconstrained attributes.

BulkTrajBlend advances the foundational structure of autoencoders (AE) and β-VAE. These enhancements involve (1) employing an AE to construct a Bulk RNA-seq generator analogous to real Bulk RNA-seq inspired by TAPE23. We modeled the cellular proportion space of Bulk RNA-seq on the output of the Encoder, the input of the Decoder. Subsequently utilizing ground truth bulk RNA-seq generated from single cell RNA-seq as input of Encoder for calculating the true cellular fractions. (2) When we trained β-VAE using real single cell RNAseq, the Encoder outputs were V (cell type fraction) and W (cell type correlated generative factor). We added a loss function to minimize the relationship between V and the real cell type fraction. We obtained W for each cell at the end of model training and averaged W for each cell type to represent that cell type. (3) We used the true cell type fraction V calculated by AE with the cell type-associated generating factor W obtained by β-VAE as input to β-VAE for generating single-cell data, and deploying unsupervised clustering to denoise and refine the outcomes of the β-VAE. (4) We employed a graph neural network (GNN) to sample the generated single-cell data, thereby identifying overlapping cell communities. Sampling the overlapping communities of cells helps us to insert "omitted" cells without losing cell continuity.


## 方法概述

#### Methods for BulkTraiBlend

BulkTrajBlend is primarily designed to address the issue of "omitted" cells in single-cell data, making the inference of developmental or differentiation trajectories continuous. To achieve this goal, we designed BulkTrajBlend to generate potential "missing" cells from bulk RNA-seq data for inferring pseudo-time cell trajectories. This process consists of the following four steps (where communities represent cell types):

**Cell proportion calculation**. To estimate the proportion of cells in Bulk RNA-seq, we first annotated the single-cell data with respective cell types and aggregate the gene counts of single cells by cell type, resulting in an $N^*M$ matrix, where M represents the number of cell types and N represents the number of genes. We define this $N \times M$ matrix as the simulated Bulk RNA-seq cell type matrix, and then we sum M columns of each row to get the simulated Bulk RNA-seq $B_{simulated}$ , and we input the simulated Bulk RNA-seq into the self-encoder of AE. In the self-encoder, we define the output of the encoder as T, and we make T close to $\frac{Number of the cell}{Number of all cells}$ , i.e., Cell

Proportion, by training AE. We then define the output of the generator as G and we make G and $B_{simulated}$ close to each other by MAE as an evaluation. After training the optimal AE, we change the input to real Bulk RNA-seq $B_{groundtruth}$ , at which time the output of the encoder, T, is the Cell Proportion corresponding to real Bulk, which we use as the range of the generator space for the subsequent $\beta$ -VAE.

**Generation of single-cell data.


## 讨论与结论

The innovative fusion of the variational autoencoder and graph neural networks combined in the creation of the BulkTrajBlend framework. This framework aims to deconvolve scRNA-seq data within Bulk RNAseq and elucidate precise cell-specific developmental trajectories in scRNA-seq. It demonstrates significant accuracy and robustness, due in large part to the unique integration of the topological overlap community in graph neural networks, which skillfully addresses the potential bias introduced by unsupervised clustering in the single-cell data outcomes.

A conceptual parallel exists between back-calculating cell proportions in Bulk RNA-seq from scRNA-seq and using Bulk RNA-seq as a scaffold for interpolating scRNA-seq. However, the latter is inherently more challenging due to the need to accurately interpolat the inadequate target cell type. While numerous single-cell generators perform well in generating scRNA-seq data, the incorporation of unknown information remains an intrinsic challenge. For example, scDesign3 is a proficient statistical simulator that creates realistic single-cell data by learning interpretable parameters from actual scRNA-seq data. Nevertheless, reconstructing cell developmental trajectories often requires elusive parameters, which necessarily leverages known data from Bulk RNA-seq61. Hence, BulkTrajBlend is meticulously crafted based on the principles of scDesign and scGen32, with the state space and parameters being informed by Bulk RNA-seq. Notably, cell categorization in the resulting single-cell data often relies on unsupervised annotation. By introducing GNN, BulkTrajBlend effectively reduces resolution-dependent issues associated with unsupervised clustering.

While BulkTrajBlend can efficiently extract the state space of cells from Bulk RNA-seq and interpolate the original scRNA-seq data, this interpolation relies on the selection of the reference scRNA-seq versus the reference Bulk RNA-seq data.


## 关键词

OmicVerse, bridging, framework

## 相关实体

方法: Bulk RNA-seq, scRNA-seq, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
