---
title: "Squidiff: predicting cellular development"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/squidiff-predicting-cellular-development.md]
confidence: medium
year: 2026
---

# Squidiff: predicting cellular development

> 原文: [[squidiff-predicting-cellular-development]]

## 摘要

tion, gene perturbation and drug treatment. Squidiff is a conditional single-cell transcriptomic data into a unified latent representation denoising diffusion implicit model (DDIM)22 generating new tran- space comprising semantic variables (z ), while the diffusion model sem scriptomes representing distinct cellular states. Squidiff allows for generates target cell transcriptomes from denoising a Gaussian noise the incorporation of diverse perturbation conditions, including gene x conditioned on z via a standard denoising process (Fig. 1b and T sem edits and drug compounds with defined structures and dosages, when Supplementary Fig. 1a; see Methods for details). Overall, Squidiff is this information is available. It excels in predicting the differentiation capable of generating transcriptomic data reflecting cell type varia- of induced pluripotent stem cells (iPSCs) into the three germ layers, tions, cell state transitions and cell type-specific responses to multiple guided by stimulus vectors. Notably, Squidiff captures transient cel- stimuli such as drug and gene perturbations. lular states that other methods often miss. Moreover, it effectively pre- To explain the Squidiff framework, we first show an application dicts nonadditive gene perturbation and cell type-specific responses, to synthetic single-cell RNA-sequencing (scRNA-seq) data gener- as shown in glioblastoma and melanoma cells in response to new drug ated using Splatter26 (Supplementary Fig.

## 背景与目的

model architecture, based on diffusion autoencoders20. The model comprises indicating the semantic latent space. f, Top: correlation between ground truth a semantic encoder and a conditional DDIM. The semantic encoder maps and reconstructed gene expression levels for cell type A and its perturbed scRNA-seq data into a semantic latent space (z ). The conditional DDIM state, showing high accuracy in predictions. Bottom: density plot comparing sem includes a diffusion process that incrementally adds noise to input data x, the distribution of gene expression values between generated, original and 0 transforming it into Gaussian noise x after T steps, and a denoising process perturbed data, indicating successful reconstruction by Squidiff. g, PCA T that decodes the latent variables (z , x) to generate gene expression profiles visualization of gene expression for cell types A and B, illustrating the temporal sem T (see Methods for details). c, Principal-component (PC) analysis (PCA) of latent progression of interpolated states from t = 0 (original) to t = 1 (fully interpolated). representations: z (left) shows clustering of cell types A, B and C, while x Intermediate time points (t = 0.25, t = 0.5 and t = 0.75) show the gradual transition sem T (right) displays stochastic variations across the same cell types. d, Visualization between cell types A and B in the latent space. of the forward diffusion process (left) and the reverse diffusion process (right) Article

## 主要发现

z2 sem Predict drug responses * * NS Nature Methods | Volume 23 | January 2026 | 65–77 70 52BTBZ ? PTPN12 ANRcs hturt dnuorG Predicted ZBTB25 + PTPN12 Pearson R = 0.97 R2 = 0.92 Predicted scRNA Oligodendrocytes Vehicle Training data Tumor cells Etoposide Held-out data Myeloid cells Panobinostat R04929097 Tazemetostat Ispenisib ANA-12 Oligodendrocytes Tumor cells Reconstructed scRNA ANRcs hturt dnuorG Reconstructed scRNA ANRcs hturt dnuorG a b c d e f g Pearson R = 0.915 Pearson R = 0.912 Vehicle Etoposide Panobinostat R04929097 Tazemetostat Ispenisib ANA-12 h i Genes slleC Semantic encoder Conditional DDIM slleC Semantic variable z sem SMILES RDKit Drug compounds rFCFP Genes Gaussian noise slleC Unperturbed cells Unseen compounds Drug-perturbed cells erocs nosraeP 2R Unseen compounds Random split Random split erocs nosraeP 2R R2 with true change in expression (all genes) erocS Percentage of all genes with opposite direction erocS 4 3 1.0 20 z1 sem 2 0.8 10 1 0.6 0 0 GEARSscGenSquidiff GEARS scGenSquidiff 0 2 4 zTumor zMyeloid sem sem R04929097 R04929097 Panobinostat Vehicle Vehicle zOligodendrocyte Vehicle sem Etoposide 177 127 193 4 4 Panobinostat 102 143 220 3 3 R04929097 116 30 125 2 2 Tazemetostat 108 39 151 1 1 Ispenisib 99 37 142 0 0 0 2 4 0 2 4 ANA-12 186 86 178 Myeloid cel O ls ligodendrocytes Tu mor cells 1.00 1.00 0.95 0.95 0.90 0.90 Squidiff PRnet Squidiff PRnet *** 1.00 1.00 x ≈ N(0, I) T 0.95 0.95 0.90 0.90 Squidiff PRnet Squidiff PRnet Fig.

## 方法概述

0 core 0 2,500 5,000 Combined score Fig. 6 | Treatment potential of G-CSF in securing against radiation disruption irradiated fibroblasts, endothelial cells and mural cells. Data to predict include in BVOs. a, Schematic illustration of the signaling pathways activated by G-CSF irradiated and G-CSF-treated fibroblasts, endothelial cells and mural cells. treatment50. G-CSF binds to its receptor (G-CSF-R), triggering downstream c, Scatterplots comparing ground truth scRNA-seq data with Squidiff-predicted signaling cascades involving MEK1, MEK2, ERK1, ERK2, PI3K and AKT. This leads data for irradiated fibroblasts (top) and irradiated mural cells (bottom) treated to the degradation of IκBα and nuclear translocation of NF-κB, promoting the with G-CSF. Pearson correlation and R2 values indicate high prediction accuracy. expression of target genes such as those encoding MMP2, VEGF and β integrin, d, Gene Ontology (Biological Process) enrichment for differentially expressed 1 which are involved in cell survival, proliferation and migration. b, UMAP genes in fibroblasts and endothelial cells. Bubble size indicates genes in set (%) visualization of scRNA-seq data from BVOs on day 11, showing the distribution and color indicates FDR; x axis shows the combined score. FDR, false discovery of healthy, irradiated and G-CSF-treated cell types. The training data include rate. The illustration in a was created with BioRender.com. healthy fibroblasts, endothelial cells and mural cells.

## 讨论与结论

Methods Reverse process. The reverse process of DPMs aims to learn the noise Ethics statement distribution p(x |x), which is an intractable and complex distribution. t − 1 t All procedures involving human iPSCs were conducted in accordance Fortunately, we know from the diffusion process that p(x |x, x ) is a t − 1 t 0 with institutional and federal ethical regulations, with guidance from Gaussian distribution. In this regard, the diffusion model first estimates the Columbia Stem Cell Initiative. The established WTC11 hiPSC line was the clean data ‘x ’ using the mean of distribution p(x |x), denoted 0 0 t obtained from B. Conklin at the Gladstone Institutes under a material as µ(x, t): θ t transfer agreement (to G.V.-N.). Diffusion probabilistic models (DPMs) are a class of latent variable μθ(xt,t)= 1 (xt− βt ϵθ(xt,t)). generative models that iteratively transform data into noise and then √αt √1−αt reverse this process to reconstruct the original data. A DPM consists of Here ε(x, t) is the noise predicted by the denoiser, that is, a neural θ t the forward process, the reverse process and the sampling procedure. network parameterized by θ. Based on the estimation, the diffusion The model learns to reverse the diffusion processes step by step, cap- model will sample x from p(x |x = x, x = µ(x, t)). t − 1 t − 1 t 1 0 θ t turing complex data distributions.

## 关键词

Squidiff, cellular, development, predicting

## 相关实体

细胞类型: Myeloid
通路: differentiation
方法: scRNA, single-cell
疾病: Tumor

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
