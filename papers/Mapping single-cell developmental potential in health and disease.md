---
marker_extracted: true
title: "Mapping single-cell developmental potential in health and disease"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/mapping-single-cell-developmental-potential-in-health-and-disease.md]
confidence: medium
year: 2024
---

# Mapping single-cell developmental potential in health and disease

> 原文: [[mapping-single-cell-developmental-potential-in-health-and-disease]]

## 摘要

Single-cell RNA sequencing (scRNA-seq) has transformed our understanding of cell fate in developmental systems. However, identifying the molecular hallmarks of potency – the capacity of a cell to differentiate into other cell types – has remained challenging. Here, we introduce CytoTRACE 2, an interpretable deep learning framework for characterizing potency and differentiation states on an absolute scale from scRNA-seq data. Across 31 human and mouse scRNA-seq datasets encompassing 28 tissue types, CytoTRACE 2 outperformed existing methods for recovering experimentally determined potency levels and differentiation states covering the entire range of cellular ontogeny. Moreover, it reconstructed the temporal hierarchy of mouse embryogenesis across 62 timepoints; identified pan-tissue expression programs that discriminate major potency levels; and facilitated discovery of cellular phenotypes in cancer linked to survival and immunotherapy resistance. Our results illuminate a fundamental feature of cell biology and provide a broadly applicable platform for delineating single-cell differentiation landscapes in health and disease.


## 背景与目的

All cells, from the fertilized egg to its mature progeny, are hierarchically organized in multicellular life. Such maps of 'cellular ontogeny' are exemplified by the lineage tree of *C. elegans*, where every parent-daughter relationship is known1. While lineage tracing, functional transplantation assays, and single-cell genomics have revealed key insights into developmental hierarchies2-5, the molecular programs underlying potency – a cell's ability to differentiate into more specialized cell types – remain unclear. For example, totipotent, multipotent, and unipotent cells each have vastly different developmental capacities, yet little is known about the transcriptional profiles that distinguish them. An improved understanding of cell potency would facilitate new insights into diverse physiological and pathological processes, including cancer, where altered differentiation states and plasticity programs shape clinical outcomes6.

In recent work, we showed that the number of detectably expressed genes per cell is a hallmark of developmental potential. Leveraging this finding, we developed CytoTRACE, a computational method for predicting cellular maturity from single-cell RNA sequencing (scRNA-seq) data7. Despite its broad applicability, CytoTRACE – like other methods for trajectory inference, including scVelo8, CellRank9, and Monocle 310 – predicts single-cell orderings in a manner that is relative to each dataset (thus, the least differentiated cells in one dataset may have equivalent potency to the most differentiated cells in another). This has made it difficult to unify such predictions across datasets and contextualize them against the backdrop of cellular potency.

To overcome these challenges, we developed CytoTRACE 2, an interpretable deep learning framework for jointly determining single-cell potency categories and absolute developmental potential from scRNA-seq data.


## 主要发现

#### **Modeling cell potency with interpretable AI**

CytoTRACE 2 was designed to provide a unique view of developmental potential. Unlike other methods, it predicts single-cell potency categories and differentiation states on an absolute scale using classically defined developmental stages as "anchor points" (**Methods**). To achieve this goal, we focused on six potency categories spanning the full range of cellular ontogeny: totipotent stem cells capable of generating an entire multicellular organism; pluripotent stem cells with the capacity to differentiate into all adult cell types; lineage-restricted multipotent, oligopotent, and unipotent cells, each capable of producing >3, 2 or 3, or 1 downstream cell type(s), respectively, and differentiated cells, ranging from mature to terminally differentiated phenotypes (**Figure 1A**; additional details in **Methods**). With these annotations, we screened online repositories for scRNA-seq data with assignable potency levels from humans and mice, for which extensive genomic data are available. This yielded a comprehensive training set consisting of 88 cell phenotypes (79 mouse and 20 human), 18 tissue types, 17 datasets, and six platforms, including droplet and plate-based assays, with 176k cells confidently assigned to potency levels in both species (**Figure 1B**, **Methods**).

Like its predecessor, we developed CytoTRACE 2 with an emphasis on understanding the molecular determinants of developmental potential. However, since most deep learning methods require dedicated procedures to ascertain feature importance11,12, we designed CytoTRACE 2 with a novel, fully explainable architecture for single-cell classification tasks (**Methods**).


## 方法概述

All methods are provided in the supplement.


## 讨论与结论

In this study, we describe CytoTRACE 2 as an interpretable deep learning framework for predicting classically defined cell potency labels and differentiation states on an absolute scale from scRNA-seq data. CytoTRACE 2 is the first in silico method designed to achieve both goals, while providing an explicit readout of the molecular profiles that drive performance.

Previous methods for profiling differentiation states from scRNA-seq data are limited by technical biases and cross-dataset interpretability, with no mechanism to explicitly link predictions of stemness/pseudotime to absolute developmental potential710,14-20,58. Separately, most deep learning architectures are not inherently explainable and require indirect strategies to extract feature importance11,12. Leveraging a modular architecture that achieves full transparency, we trained and validated CytoTRACE 2 on a rich repertoire of tissue types, organs, and developmental systems, spanning all major potency levels in humans and mice. With these data, we identified conserved signatures of cell potency and established a resource and analytical tool to dissect developmental potential with high granularity from existing and emerging cell atlases.

We anticipate that CytoTRACE 2 will facilitate important applications beyond those demonstrated in this work. For example, it can be applied to (i) optimize and troubleshoot somatic cell reprogramming and stem cell engineering experiments where the generation of cells with specific potency levels is desired; (ii) distinguish developmental variation from non-developmental state changes in scRNA-seq data; and (iii) promote the discovery of developmental phenotypes and associated tissue microenvironments from scRNA-seq data integrated with spatial transcriptomics data.


## 关键词

Mapping, developmental, disease, health, potential, single-cell

## 相关实体

细胞类型: all
通路: differentiation
方法: Single-cell, scRNA-seq, single-cell
疾病: cancer, disease

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
