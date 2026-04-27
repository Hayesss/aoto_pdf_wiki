---
marker_extracted: true
title: "Model-based inference of RNA velocity modules improves cell fate"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/model-based-inference-of-rna-velocity-modules-improves-cell-fate.md]
confidence: medium
year: 2023
---

# Model-based inference of RNA velocity modules improves cell fate

> 原文: [[model-based-inference-of-rna-velocity-modules-improves-cell-fate]]

## 摘要

RNA velocity is a powerful paradigm that exploits the temporal information contained in spliced and unspliced RNA counts to infer transcriptional dynamics. Existing velocity models either rely on coarse biophysical simplifications or require extensive numerical approximations to solve the underlying differential equations. This results in loss of accuracy in challenging settings, such as complex or weak transcription rate changes across cellular trajectories. Here, we present cell2fate, a formulation of RNA velocity based on a *linearization* of the velocity ODE, which allows solving a biophysically accurate model in a fully Bayesian fashion. As a result, cell2fate decomposes the RNA velocity solutions into *modules*, which provides a new biophysical connection between RNA velocity and statistical dimensionality reduction. We comprehensively benchmark cell2fate in real-world settings, demonstrating enhanced interpretability and increased power to reconstruct complex dynamics and weak dynamical signals in rare and mature cell types. Finally, we apply cell2fate to a newly generated dataset from the developing human brain, where we spatially map RNA velocity modules onto the tissue architecture, thereby connecting the spatial organisation of tissues with temporal dynamics of transcription.


## 背景与目的

The concept of "RNA velocity", which involves inferring transcriptional dynamics from spliced and unspliced counts in single-cell RNA sequencing (scRNA-seq), has displayed significant potential<sup>1–3</sup>. The first implementations of RNA velocity models<sup>1–3</sup> have undergone an evolution of conceptual and technical refinements, including improved parameter inference<sup>4–6</sup>, as well as the use of numerical approaches<sup>5,7,8,9</sup> to allow for solving the underlying differential equations. However, these existing refinements are bound to trade-offs between either introducing coarse biophysical approximations<sup>1–4,6,10,11</sup> or relying on extensive numerical approximations<sup>5,7–9</sup>. Hence, the fundamental challenge remains to define a mathematically

sound framework that allows for capturing unconstrained transcriptional dynamics while retaining computational and numerical tractability.

To address the aforementioned limitations, we present cell2fate - a fully Bayesian model of RNA velocity based on a realistic biophysical model of complex transcription dynamics. Cell2fate employs a linearization to decompose complex differential equations into tractable components that can be solved analytically. By doing so, the model is at the same time expressive, interpretable and computationally efficient. The approach to decompose the velocity problem into components also provides a new connection between RNA velocity and dimensionality reduction using a biophysical solution.

We assess and benchmark cell2fate in the context of real-world settings, demonstrating its ability to capture complex dynamics and weak dynamical signals in rare and mature cell types. Finally, we show how cell2fate can be combined with spatial transcriptomics, thereby connecting transcriptional dynamics to their spatial tissue environment.


## 主要发现

#### **The cell2fate model**

Cell2fate builds on a long-stranding history of computational methods for RNA velocity, which employ a dynamical model to explain variation in spliced and unspliced read counts for individual genes and cells (Fig. 1a). At the core of cell2fate is a reformulation of the RNA velocity problem that gives rise to an analytically tractable solution for cell-specific transcription rates. This is achieved by linearizing the corresponding ODE for each gene into a set of M components with simpler dynamics. The dynamics of each module is defined by a switch on/off time, Tm,on/Tm,off on a cell specific time-scale Tc, as well as corresponding rates λm,on/λm,off and a gene loading parameter, Amg (Fig. 1b, top right). The linearized solution allows for estimating modules at the level of transcription rates, RNA velocities and observed counts (Fig. 1c, d).

The linearization also provides a biophysical connection between RNA velocity and statistical dimensionality reduction. This connection becomes apparent when casting the linearization as a mixed membership model, whereby spliced and unspliced counts of each gene are governed by a linear combination of M modules (Methods, Fig. 1b). The mixing coefficients can then be interpreted analogous to gene loadings of factor analysis or principal component analysis.

The cell2fate model directly operates on the raw cell-level counts as input, and it includes a series of refinements to account for technical sources of variation, including overdispersion, variation in detection sensitivity of spliced and unspliced RNA molecules, ambient RNA and known batches (Methods). Parameter inference is conducted in a fully Bayesian manner, which allows for encoding assumptions on sparsity using hierarchical priors, regularising the effective number of active modules, as well as sharing of evidence strength across genes, cells and modules (Methods).


## 方法概述

Methods and a description of the cell2fate model can be found in the supplemental methods document.


## 讨论与结论

Here we presented cell2fate, a Bayesian model of RNA velocity that is capable of inferring transcriptional dynamics in settings of complex changes or weak signals in rare and mature cell types. A core innovation of cell2fate is a formulation of the velocity problem that builds on linearization, which allows for solving a biophysically accurate model using analytically tractable linearized components. Another benefit of this formulation is that these linear components can be inspected as interpretable RNA velocity modules. This provides for a direct biophysical connection between cell2fate and statistical dimensionality reduction methods. We illustrated this feature by characterising late maturation trajectories in granule neurons that have been elusive with other methods. Furthermore, RNA velocity modules can be used to locate differentiation trajectories in spatial transcriptomics data. We exemplified this in the developing human brain where the RNA velocity modules of neuronal differentiation showed a high degree of spatial organisation.

The concepts proposed in cell2fate are general and give rise to several extensions that could be considered in the future. It is possible to formulate RNA velocity models with cellspecific splicing and degradation rates, stochastic rates at lineage branching points and causal connections between transcription rates at different time points, equivalent to dynamic gene regulatory networks (Methods). In the long term, dynamical models should also include the effects of cell-cell interactions, based on signalling molecules measured with spatial transcriptomics. An immediate step towards this goal would be combining RNA velocity module mapping with spatial cell-cell interaction tools, such as NCEM31, which could identify putative interactions that drive specific steps of a differentiation process.


## 关键词

Model-based, RNA, cell, fate, improves, inference, modules, velocity

## 相关实体

暂无识别到特定实体

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
