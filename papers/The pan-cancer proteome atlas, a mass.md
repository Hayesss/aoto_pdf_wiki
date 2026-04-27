---
marker_extracted: true
title: "The pan-cancer proteome atlas, a mass"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/the-pan-cancer-proteome-atlas-a-mass.md]
confidence: medium
year: 2025
---

# The pan-cancer proteome atlas, a mass

> 原文: [[the-pan-cancer-proteome-atlas-a-mass]]

## 摘要

Most cancer proteomics studies to date have focused on a single cancer type. We report The Pan-Cancer Pro- teome Atlas (TPCPA) based on data-independent acquisition mass spectrometry, to better understand cancer biology and identify therapeutic targets and biomarkers. TPCPA includes 9,670 proteins derived from 999 pri- mary tumors representing 22 cancer types. We describe pan-cancer and cancer type-enriched proteins with extensive external annotation, prioritizing candidate drug targets and biomarkers. Relevant for proteolysis-tar- geting chimeras, we identify E3-ubiquitin ligases highly expressed in specific tumor types, including HERC5 (esophageal cancer) and RNF5 (liver cancer). Co-expression analysis reveals 13 modules, including unexpected hub proteins as potential drug targets (e.g., GFPT1, LRPPRC, PINK1, DOCK2, and PTPN6). Analysis of 195 colorectal cancers identifies protein markers for RNA-based consensus molecular subtypes (CMSs) and two immune subtypes with prognostic value. We report a cancer type classifier for identification of cancers of unknown primary origin. All TPCPA data can be queried in a dedicated web resource. INTRODUCTION normal checks and balances. Molecular profiles of tumors may be leveraged for clinical intervention with personalized treat- Cancer is a heterogeneous collection of diseases characterized ments.

## 背景与目的

Cancer is a heterogeneous collection of diseases characterized by uncontrolled growth and spread of malignant cells escaping normal checks and balances. Molecular profiles of tumors may be leveraged for clinical intervention with personalized treatments. Large-scale genomics efforts of The Cancer Genome Atlas (TCGA) and the International Cancer Genome Consortium

<sup>1</sup>Amsterdam UMC, location Vrije Universiteit Amsterdam, Department of Medical Oncology, OncoProteomics Laboratory, De Boelelaan 1117, Amsterdam, the Netherlands

<sup>2</sup>Cancer Center Amsterdam, Imaging and Biomarkers, Amsterdam, the Netherlands

<sup>3</sup>School of Medicine, Westlake University, Hangzhou, Zhejiang, China

<sup>4</sup>Westlake Center for Intelligent Proteomics, Westlake Laboratory of Life Sciences and Biomedicine, Hangzhou, Zhejiang, China

<sup>5</sup>Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Urology, De Boelelaan 1117, Amsterdam, the Netherlands

<sup>6</sup>Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Neurosurgery, De Boelelaan 1117, Amsterdam, the Netherlands 7Medizinisches Proteom-Center, Ruhr-Universita¨ t Bochum, Bochum, Germany

<sup>8</sup>Department of Anesthesia, Intensive Care Medicine and Pain Therapy, University Hospital Knappschaftskrankenhaus Bochum, Bochum, Germany

<sup>9</sup>Department of Oncology-Pathology, Science for Life Laboratory, Karolinska Institutet, Stockholm, Sweden

<sup>10</sup>Amsterdam UMC location University of Amsterdam, Center for Experimental and Molecular Medicine, Laboratory for Experimental Oncology and Radiobiology, Meibergdreef 9, Amsterdam, the Netherlands

<sup>11</sup>Cancer Center Amsterdam, Cancer Biology and Immunology, Amsterdam, the Netherlands

<sup>12</sup>Department of Surgery, Division of HPB & Transplant Surgery, Erasmus MC Transplant Institute, University Medical Center Rotterdam, Rotterdam, the Netherlands

<sup>13</sup>Amsterdam UMC location University of Amsterdam, Dep


## 主要发现

#### Rediscovery of cancer types by unsupervised proteome analyses

Comprehensive profiling of protein expression patterns across cancer types may elucidate the shared and context-dependent nature of cancer phenotypes. To date, such an approach has

not been applied in a large pan-cancer context. To explore common and cancer (sub)type biology, we applied an unbiased proteomics approach based on DIA-MS to generate a pan-cancer analysis including 22 cancer types.

The TPCPA dataset originated from 1,236 DIA raw files comprising cancer samples, normal tissues and non-tumor adjacent tissues, adenoma tissues, benign tissues, as well as HeLa cell line control samples. A total of 1,172 samples met basic quality control criteria ([Tables](#page-15-0) S1 and [S2A](#page-15-0)). After further filtering for primary cancer samples only, a minimum number of five samples per cancer type and a minimum data presence of 30% per cancer type, 999 samples remained with a total of 11,250 identified protein groups for 22 cancer types [\(Table](#page-15-0) S2B). The final TPCPA dataset has been included as a data portal in the R2 platform [\(http://r2platform.com/TPCPA,](http://r2platform.com/TPCPA) [Figures](#page-15-0) S1A–S1E). Grouped by cancer type, the smallest sample set contained eight samples (skin/melanoma), whereas the largest contained 195 colorectal cancer (CRC) samples covering four consensus molecular subtypes.

[Figure](#page-4-0) 1 shows an overview of the TPCPA pan-cancer tissue landscape as measured by DIA-MS. [Figure](#page-4-0) 1A gives an overview of the cancer types in TPCPA. Most samples yielded 5,000– 6,000 identified proteins ([Figure](#page-4-0) 1B), with abundance spanning ∼4 orders of magnitude. Seven proteins are ''missing proteins'' according to the HUPO HPP Portal [\(https://hppportal.net](https://hppportal.net/)), one of which (USP17L10) was detected with four peptides. Uniform manifold approximation and projection (UMAP)-based dimension reduction shows ap


## 方法概述

CMS subtype proteome classifier To assess the potential of DIA-MS prote- ome profiling for CMS subtype classifica- tion, we constructed a CMS subtype and G2M checkpoint terms, confirming the previously reported classifier. The top 25 enriched proteins for each CMS were cell cycle enrichment. CMS3 had a metabolic phenotype, evi- used to train a classifier using the AMC cohort (n = 38) with a denced by fatty acid metabolism, and CMS4 had a mesen- balanced composition of transcriptomics-based CMS subtypes, chymal phenotype, with activation of angiogenesis, EMT, and while performance was examined on an independent label-free apical surface and junction terms. As new insights, we found colon cancer proteomics dataset from CPTAC (n = 100).

## 讨论与结论

Large-scale cancer genomics and in-depth cancer proteogenomics efforts of individual cancer types have increased our understanding of cancer biology and driving oncogenic mechanisms.[1–3,9–11](#page-15-0) To further obtain insights into cancer type biology in a pan-cancer context and unravel pan-cancer and cancer type markers and targets, a global molecular readout close to function is needed with sufficient throughput. High-throughput clinical proteomics based on single-shot DIA-MS has enabled large-scale proteome profiling in recent years, also in a multi-laboratory setting.[16,](#page-15-0)[89–92](#page-18-0)

In a collaborative effort of four cancer proteomics laboratories and their clinical partners, we generated a proteome atlas comprising 22 cancer types and performed pan-cancer and cancer (sub)type analyses of the resultant large pan-cancer landscape of almost 10,000 proteins based on 999 tumor samples. Our analysis pinpointed top candidate protein biomarkers and targets for individual cancer types and (pan-cancer) for solid and blood cancers. The value of the cancer type-enriched proteins was highlighted by constructing a cancer-type classifier of 75 proteins that was validated on four independent cohorts of renal, breast, ovarian, and colorectal tumors. Moreover, our immune subset analysis further uncovered tumor heterogeneity with potential implications for immunotherapy. Finally, analysis of 195 colon cancers in TPCPA identified protein markers and a 52-protein-based classifier for the four CRC CMS subtypes previously defined using transcriptomics data.[82](#page-17-0)

Our functional proteome analyses provide insights into (co-expressed) proteins linked to cancer hallmarks and immune landscapes that, together with cancer-type enrichment analyses and ranking, reveal potentially novel diagnostic and therapeutic avenues. Because not all cancer-enriched proteins are drivers themselves, identifying causally implicated markers remains a key challenge. We ther


## 关键词

atlas, mass, pan-cancer, proteome

## 相关实体

方法: mass spectrometry
疾病: Cancer, cancer, tumor

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
