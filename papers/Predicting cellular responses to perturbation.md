---
marker_extracted: true
title: "Predicting cellular responses to perturbation"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/predicting-cellular-responses-to-perturbation.md]
confidence: medium
year: 2025
---

# Predicting cellular responses to perturbation

> 原文: [[predicting-cellular-responses-to-perturbation]]

## 摘要

Cellular responses to perturbations are a cornerstone for understanding biological mechanisms and selecting potential drug targets. While computational models offer tremendous potential for predicting perturbation effects compared to experimental approaches, they currently struggle to generalize effects from experimentally observed cellular contexts to unobserved ones. Here, we introduce STATE, a machine learning architecture that predicts perturbation effects while accounting for cellular heterogeneity within and across perturbation experiments. State operates across physical scales: it consists of a state transition model that learns perturbation effects across sets of cells using data from over 100 million perturbed cells across 70 cell contexts and a cell embedding model trained on observational single-cell data from 167 million human cells. State improved discrimination of perturbation effects on multiple large datasets by over 50% and identified true differentially expressed genes across genetic, signaling, and chemical perturbations with over 2-fold accuracy compared to existing models. Using its embedding model, State can also identify strong perturbations in novel cellular contexts where no perturbations have been observed during training. We further introduce Cell-Eval, a comprehensive evaluation framework using biologically relevant metrics that highlights how STATE enables more precise discovery of cell type-specific perturbation responses, such as those related to cell survival. Overall, the performance and flexibility of STATE sets the stage for scaling the development of virtual cell models.

<sup>\*</sup>State core contributor.

<sup>&</sup>lt;sup>†</sup>These authors supervised this work.

<sup>&</sup>lt;sup>‡</sup>Corresponding author: Y.H.R. (yusuf.roohani@arcinstitute.org)


## 背景与目的

man et al., 2019). However, these assays remain cost-prohibitive and labor-intensive to scale across many contexts. Improving our ability to generalize perturbation response pre- dictions across diverse biological contexts would greatly accelerate causal target discovery, deepen our understanding of cellular function and disease, and in turn facilitate the design of context-specific interventions, creating a foundation for personalized treatment predictions. A range of computational approaches have been developed to tackle this problem (Lot- follahi et al., 2019, 2023; Bunne et al., 2023; Roohani et al., 2024a; Cui et al., 2024; Hao et al., 2024).

## 主要发现

perturbation effects within and across diverse datasets. State is a multi-scale model with two complementary modules: a State Transition model (ST) and a State Embedding model (SE). ST is a transformer that uses self-attention to model perturbation-induced transfor- mations across sets of cells, where each cell is represented either by its raw gene expression profile or a learned embedding. SE is pretrained to generate expressive cell embeddings by learning gene expression variation between cells across diverse datasets (Zhang et al., 2025; Programetal.,2025;Youngblutetal.,2025), yieldingrepresentationsthatarerobusttotech- nical variation and optimized for detecting perturbation effects. By leveraging self-attention over sets of cells, ST can flexibly capture biological heterogeneity without relying on explicit distributional assumptions. Together, SE and ST enable State to generalize across datasets and perturbations, improving transferability of perturbation-response modeling.

## 方法概述

which includes 100 million cells spanning thousands of perturbations across dozens of base- line cellular contexts, and Parse-PBMC, which includes 10 million cells across 12 donors and 18 cell types, as compared to the genome-scale genetic perturbation datasets conducted in just a few cell lines. This highlights State’s ability to leverage data scale and context diversity more effectively than existing models, which do not display proportionate gains 10 bioRxiv preprint doi: this version posted June 27, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license.

## 讨论与结论

(unperturbed) cell population, SE computes cell embeddings. ST then predicts how those embed- dings shift in response to a specified perturbation, effectively modeling the distributional effect of the perturbation in latent space. Finally, a learnt decoder maps the predicted embeddings back into gene expression space. (Continued on next page) 12 bioRxiv preprint doi: this version posted June 27, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license.

## 关键词

Predicting, cellular, perturbation, responses

## 相关实体

方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
