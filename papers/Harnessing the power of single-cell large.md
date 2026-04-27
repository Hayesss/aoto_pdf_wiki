---
marker_extracted: true
title: "Harnessing the power of single-cell large"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/harnessing-the-power-of-single-cell-large.md]
confidence: medium
year: 2025
---

# Harnessing the power of single-cell large

> 原文: [[harnessing-the-power-of-single-cell-large]]

## 摘要

nature machine intelligence Article Harnessing the power of single-cell large language models with parameter-efficient fine-tuning using scPEFT Received: 25 February 2025 Fei He 1, Ruixin Fei1, Jordan E. Krull 2,3, Yang Yu 1, Xinyu Zhang1, Xianyu Wang1, Hao Cheng2,3, Mingyue Gao1, Li Su 1,4, Yibo Chen 1,4, Accepted: 4 December 2025 Jinpu Li 1,4, Baichuan Jin1, Yuzhou Chang2,3, Anjun Ma 2,3, Qin Ma 2,3 & Published online: 31 December 2025 Dong Xu 1,4 Check for updates Single-cell large language models (scLLMs) capture essential biological insights from vast single-cell atlases but struggle in out-of-context applications, where zero-shot predictions can be unreliable. To address this, here we introduce a single-cell parameter-efficient fine-tuning (scPEFT) framework that integrates learnable, low-dimensional adapters into scLLMs.

## 背景与目的

A = N(0, σ2) Attention Down Token adapter Prefix adapter LoRA Encoder adapter Domain-agnostic cell-type identification Cross-species transfer Condition-specific Context-aware cell group gene significance characterization G1 G2 G3 Pretrain Pretrain Domain Normal Perturbation prediction Adaptation Adaptation Adaptation G2 G3 G1 Tuned Batch correction Disease Enable Enhance consistently outperformed fine-tuning. However, increasing the keeping the query set unchanged. The results (Fig. 3g) show that as the number of transformer blocks with adapters did not yield consistent amount of reference data was decreased, the validation performance performance improvements.

## 主要发现

#### **Achieving superior performance with scPEFT in cell-type identification under disease conditions**

The design and technical details of scPEFT are presented in Methods and Fig. 1. To evaluate its adaptability to disease conditions unseen in the pretrained stage of scLLMs, we first focused on cell-type identification using the Non-Small Cell Lung Cancer (NSCLC) dataset comprising diverse T cell subtypes from the tumour microenvironment. scPEFT was benchmarked with scBERT, Geneformer, scGPT and scFoundation as backbones (see Supplementary Note 4 for benchmarking settings), and we compared their native and fine-tuned performances. A uniform manifold approximation and projection (UMAP) visualization (Fig. 2a\) illustrates the behaviour of selected cell representations under native scGPT, fine-tuned scGPT and scPEFT, indicating that native scGPT struggled with out-of-context scenarios, whereas its fine-tuned model was prone to catastrophic forgetting. The benchmarking results showed the poor performance of native scLLMs in identifying out-of-distribution cells, as their pretraining data were derived from normal conditions (Fig. 2b\). Fine-tuning improved their performance but was computationally intensive, whereas scPEFT further boosted accuracy under identical conditions and fivefold cross-validation (39.7–81.7% accuracy improvements with *P* < 0.001 compared with native models, and 4.3–15% accuracy improvements with *P* < 0.05 compared with fine-tuned models). Notable performance gaps were observed across the tested scLLMs (Fig. 2b), with the four adapter types in scPEFT demonstrating various levels of efficacy (Supplementary Figs. 1a and 2a), driven by their gene tokenizer designs and pretrained knowledge. Despite the various native performances, scPEFT consistently elevated scLLMs to similar levels, except for scBERT, which was pretrained on a smaller corpus. This highlights the ability of scPEFT to unlock the full potential of scLLMs.


## 方法概述

#### Architecture of scLLMs

A typical scLLM has a tokenizer to vectorize gene identities and expression values and a multi-head transformer encoder to aggregate gene expression in cells into gene and cell representations. These are followed by a task-specific projector for inference (Fig. 1a).

**Tokenizer.** Current scLLMs conceptualize single-cell expression profiles as a form of biological language. Like LLMs, current scLLMs require the tokenization of genes, which converts them into vector representations for downstream learning. However, the key difference in scLLMs is that their tokenizer needs to encode both the gene name and its expression profile. Each scLLM maintains a gene vocabulary based on its training corpus, assigning a unique integer identifier, id $(g_j)$ , to each gene $g_j$ within a given input cell i. Consequently, the gene token vector $\mathbf{t}_a^{(j)}$ for cell i is represented as follows:

$$\mathbf{t}_{\mathrm{g}}^{(i)} = \left[ \mathrm{id}\left(\mathbf{g}_{1}^{(i)}\right), \mathrm{id}\left(\mathbf{g}_{2}^{(i)}\right), \dots, \mathrm{id}\left(\mathbf{g}_{M}^{(i)}\right) \right]. \tag{1}$$

Here M is the total number of genes in the input cell. When input genes do not match the predefined vocabulary, scLLMs omit them from the input. Furthermore, unlike traditional LLMs, scLLMs also incorporate the expression profile of each gene into the token. A prevalent approach used by scBERT and scGPT involves discretizing the normalized expression value $X_{(i,j)}$ of cell i into m discrete bins $[b_1,b_2,\ldots,b_m]$ , yielding the expression profile vector $\mathbf{x}_{\mathrm{e}}^{(i)}$ :

$$\mathbf{x}_{\mathrm{e}}^{(i)} = \left\{k, \; \mathsf{if} X_{(i,j)} > 0 \; \mathsf{and} X_{(i,j)} \in \left[b_k, b_{k+1}\right], \; k \in [1,m] \; ; \; 0, \; \mathsf{if} X_{(i,j)} = 0\right\}.


## 讨论与结论

Traditionally, full fine-tuning of scLLMs is used to enhance downstream task performance by updating all model parameters. However, this approach risks distorting pretrained features12, especially in out-of-context applications where the data distribution diverges substantially from the pretraining corpus. scPEFT addresses this by reparameterizing the model parameters with low-dimensional proxies and restricting task adaptation to a separate subspace. This greatly reduces the number of trainable parameters, enabling faster convergence and less annotated data requirements, thereby cutting adaptation time and effort. By preserving the original parameter values, scPEFT minimizes overfitting and catastrophic forgetting, resulting in better performance and greater computational efficiency across diverse single-cell analyses. We recommend using scPEFT to generate context-aware embeddings from scLLMs for a wide range of downstream tasks. It supports both supervised and unsupervised modes for datasets with or without pre-annotations. Furthermore, its attention analysis enables condition-specific interpretation, which facilitates more precise and context-aware discoveries.

scPEFT extends the capabilities of scLLMs beyond their original human-centric pretraining corpus. Its plug-in adapters enable the recognition of gene programs in other species by leveraging orthologous gene subsets. However, one-to-one orthologous mapping is not always possible. Future work will explore advanced homology inference methods to incorporate non-orthologous genes with functional or evolutionary similarity. Another promising direction involves developing a gene vocabulary adapter to align non-orthologous gene embeddings into the orthologous feature space, which would enable scPEFT to capture transcriptomic landscapes across species.

We describe optimal use cases of scPEFT across diverse scLLM backbones and applications in Supplementary Note 10.


## 关键词

Harnessing, large, power, single-cell

## 相关实体

细胞类型: T cell
方法: Single-cell, single-cell
疾病: Cancer, disease

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
