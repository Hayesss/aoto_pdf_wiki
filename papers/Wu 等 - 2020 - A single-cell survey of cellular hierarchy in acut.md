---
title: "Wu 等 - 2020 - A single-cell survey of cellular hierarchy in acut"
created: 2025-04-22
updated: 2025-04-22
type: paper
tags: ["scrna-seq"]
sources: ["raw/papers/wu-等-2020-a-single-cell-survey-of-cellular-hie.md"]
confidence: medium
marker_extracted: true
---

# Wu 等 - 2020 - A single-cell survey of cellular hierarchy in acut

> Zotero Item Key: 23ZKCYAJ
> 原文: [[wu-等-2020-a-single-cell-survey-of-cellular-hie]]

## 摘要

**Background:** Acute myeloid leukemia (AML) is a fatal hematopoietic malignancy and has a prognosis that varies with its genetic complexity. However, there has been no appropriate integrative analysis on the hierarchy of different AML subtypes.

**Methods:** Using Microwell-seq, a high-throughput single-cell mRNA sequencing platform, we analyzed the cellular hierarchy of bone marrow samples from 40 patients and 3 healthy donors. We also used single-cell single-molecule real-time (SMRT) sequencing to investigate the clonal heterogeneity of AML cells.

**Results:** From the integrative analysis of 191727 AML cells, we established a single-cell AML landscape and identified an AML progenitor cell cluster with novel AML markers. Patients with ribosomal protein high progenitor cells had a low remission rate. We deduced two types of AML with diverse clinical outcomes. We traced mitochondrial mutations in the AML landscape by combining Microwell-seq with SMRT sequencing. We propose the existence of a phenotypic "cancer attractor" that might help to define a common phenotype for AML progenitor cells. Finally, we explored the potential drug targets by making comparisons between the AML landscape and the Human Cell Landscape.

**Conclusions:** We identified a key AML progenitor cell cluster. A high ribosomal protein gene level indicates the poor prognosis. We deduced two types of AML and explored the potential drug targets. Our results suggest the existence of a cancer attractor.

**Keywords:** Acute myeloid leukemia, Single-cell mRNA sequencing, Microwell-seq, Ribosomal protein, Single-molecule real-time sequencing, Cancer attractor

<sup>1</sup>Center for Stem Cell and Regenerative Medicine, The First Affiliated Hospital, Zhejiang University School of Medicine, Hangzhou 310058, China <sup>2</sup>Institute of Hematology, The First Affiliated Hospital, Zhejiang University School of Medicine, Hangzhou 310003, China

Full list of author information is available at the end of the article

© The Author(s). 2020 **Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons sience and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.

<sup>\*</sup> Correspondence: xhan@zju.edu.cn; huanghe@zju.edu.cn; ggj@zju.edu.cn

 $<sup>^\</sup>dagger \mbox{Junqing}$  Wu, Yanyu Xiao, Jie Sun, Huiyu Sun and Haide Chen contributed equally to this work.

## 背景与目的

Acute myeloid leukemia (AML) is a hematopoietic malignancy with recurrent genetic abnormalities [[1,](#page-16-0) [2](#page-16-0)]. New therapeutic options such as targeted therapies and monoclonal antibodies may improve the long-term survival in patients with AML [\[3](#page-16-0), [4\]](#page-16-0). However, the prognosis of AML remains poor in some patients, suggesting its genetic and cellular complexity [[5](#page-16-0)–[7](#page-16-0)]. Therefore, it is of great importance to understand the major hierarchy and cellular compositions in different individuals with AML.

Flow cytometry is widely used for exploring cell heterogeneity in leukemia; however, it is limited to the choice of surface markers [[8\]](#page-16-0). Bulk population sequencing can probe into the cell genome and transcriptome, but misses the information of individual cells. Moreover, integrative analyses of samples from different patients with leukemia prove difficult, due to a lack of assay consistency and precision. The advances in single-cell techniques have made systematic analyses of leukemia cells possible [[9](#page-16-0), [10\]](#page-16-0). Several studies have applied singlecell analysis to normal and malignant hematopoietic cells [[11](#page-16-0)–[13](#page-16-0)]. However, because of the limited scales and technical consistency in these studies, an overall picture of AML and the common hierarchy among different patients have not yet been described.

One hallmark of cancer is the reprogramming of energy metabolism to fuel cell growth and division [\[14](#page-16-0)]. Ribosome biogenesis is an energy-demanding process, and it has been proposed that ribosomal proteins (RPs) have an effect on tumorigenesis [\[15](#page-16-0)]. A previous study reported that RPs exhibited strong dysregulation in particular cancer types, such as breast cancer, melanoma, and thyroid carcinoma [\[16](#page-16-0)]. Some RPs are involved in the specification of hematopoietic lineages, and their alterations lead to hematologic disorders, like Diamond-Blackfan anemia, Chromosome 5q deletion syndrome, and Shwachman-Diamond syndrome [\[17](#page-16-0), [18\]](#page-16-0). However, there is a lack of knowledge on the dysregulation of RPs in AML.

Mitochondrial mutations can suggest clonal relationships [[19\]](#page-16-0). They may preserve information about cell lineage relationships at single-cell resolution [[20](#page-16-0)]. However, no study has examined single-cell mitochondrial mutations in AML to explore the relationship between clonotype and phenotype.

Herein using Microwell-seq, we analyzed 191727 single cells of bone marrow mononuclear cells (BMMCs) from 40 de novo AMLs and 8561 single cells of BMMCs from three normal donors [[21](#page-16-0)]. To investigate the cellular and molecular changes after AML treatment, we followed-up four patients after they received chemotherapy. We demonstrated a global transcriptional heterogeneity and a lack of clear cell fate boundaries in AML samples. We showed that an AML progenitor cell cluster was associated with a dysregulation of RPs and revealed that patients with RP high progenitor cells had a low remission rate. We deduced two types of AML with diverse clinical outcomes. We suggested the existence of a phenotypic "cancer attractor" that might help to define a common phenotype for AML progenitor cells by combining Microwell-seq with SMRT sequencing. Finally, we investigated the potential targets by making comparisons with the Human Cell Landscape. These datasets have deepened our understanding and might open a way for novel diagnostic and therapeutic strategies in AML.

## 主要发现

#### Analysis of normal BMMC hierarchy

To gain insights into the heterogeneity of normal and malignant hematopoiesis, we first profiled the heterogeneity in normal BMMCs. We used Microwell-seq on three healthy donors and established the analysis pipeline (Fig. S[1A](#page-15-0)) [[21](#page-16-0)]. We performed t-Distributed stochastic neighbor embedding (t-SNE) analysis of individuals (Fig. [S1](#page-15-0)B and Supplementary Table [1](#page-15-0)). The t-SNE map of 8561 normal BMMCs of three healthy donors is shown in Fig. [1](#page-2-0)a, b. According to the gene expression patterns, we identified lymphoid, erythroid, and myeloid lineages (Fig. [1a](#page-2-0), c and Supplementary Table [2](#page-15-0)) [[22,](#page-16-0) [23\]](#page-16-0). Neutrophils are divided into three main types, neutrophil A, B, and C, along with three extended types, neutrophil D, E, and F (Fig. S[2](#page-15-0)A and Supplementary Table [2](#page-15-0)). The related marker genes are shown in Fig. S[2B](#page-15-0), C.

To perform lineage trajectory analyses, we integrated another 2000 hematopoietic stem/progenitor cells (HSPCs) and 2719 peripheral blood mononuclear cells (PBMCs) from our previous study to get a total of 13280 healthy cells [[24](#page-16-0)]. Using partition-based graph abstraction (PAGA), we revealed distinct developmental branches and built a transcriptional landscape for normal human hematopoiesis (Fig. [1d](#page-2-0)-f and Supplementary Table [3](#page-15-0)). The expression levels of marker genes change in the myeloid path, in conformity to the t-SNE analyses above (Fig. [1g](#page-2-0)).

## 方法概述

#### Patient samples and single-cell preparation

Samples were obtained from newly diagnosed patients with AML at the 1st Affiliated Hospital of Zhejiang University. Patients with AML were diagnosed according to the FAB classification. Patients diagnosed with other leukemia types were excluded. Patients with no clinical symptoms with blast cells in BM < 5%, hemoglobin concentration > 90 g/L, platelet > 100 × 10<sup>9</sup> /L, and normal white blood cells counts were considered to be in CR. The patients were considered to be in partial remission when the blast cells in BM < 20%, but > 5%. For relapse, the blast cells in BM > 20% again after remission. In our study, patients who were not in remission or partial remission after the second regimen were considered to be refractory patients. Cells were isolated from bone marrow aspirates by Ficoll Hypaque Solution (Haoyang Institute of Biotechnology, Tianjin, China), and diluted to ≈ 200000/ml for Microwell-seq in DPBS.

## 讨论与结论

The emergence of the single-cell technologies permits the dissection of cellular heterogeneity with genome, epigenome, transcriptome, and proteome analyses [[63](#page-17-0), [64\]](#page-17-0). Advances in technology deepens our understanding of the molecular mechanism underlying healthy and malignant hematopoiesis [[65](#page-17-0)]. Previous studies have been designed to study leukemia from diagnosis to prognosis [[12,](#page-16-0) [66](#page-17-0)–[68\]](#page-17-0). However, limited scales and technical consistency constrained them to draw a generalized picture of AML at the single-cell level. Herein using Microwell-seq, a high-throughput single-cell mRNA sequencing platform, we collected data from a large number of cells and carried out an integrative analysis on up to 40 patients.

Previous studies have reported the deregulation of ribosomal proteins (RPs) in human malignancies [\[15](#page-16-0)]. RPs confer a selective advantage to malignant cells [\[16](#page-16-0)]. They have been associated with malignant cells through extra ribosomal functions related to proliferation, DNA repair, apoptosis, and cellular homeostasis [\[69\]](#page-17-0). In addition, they play a critical role in the acquisition and maintenance of cancer stem cell phenotype [[70\]](#page-17-0). The impairment of ribosome biogenesis leads to p53 induction and cell cycle arrest [\[71](#page-17-0)]. Innovative drugs, which hinder ribosome biogenesis to stabilize p53, have shown preclinical activity and are currently in early clinical development in hematological malignancies [[72\]](#page-17-0). In our study, we found that the AML progenitor cells were characterized by a high expression level of multiple RP genes, which were involved in the p53 pathway. The dysregulation of transcriptome might lead to failure of remission.

There were limitations and bias in the comparison of the CR rate and survival rate in type I and II patients in our study. Our sample size was small, and we were not able to track all the patients. Some patients chose other hospitals for better treatment, and some patients, especially the elderly ones, go back home without treatment, or died from other diseases at the beginning of treatment, such as cerebral hemorrhage and atrial fibrillation. The elderly patients with good prognosis were more likely to receive continuous treatment, and this might lead to bias.

The combination of the next-generation sequencing and the targeted long-read sequencing is able to identify the mutations at a single-cell level. The targeted sequencing is for bulk sample, ignoring the cluster heterogeneity. Single-cell next-generation sequencing is harped by the coverage. It only sequences 150 bp from poly A, failing to identify mutations, which usually locate thousands of bases away. Previous studies have combined long-read nanopore sequencing with short-read based transcriptome profiling of barcoded single cells to track the clonal changes [[73,](#page-17-0) [74](#page-17-0)]. Though nanopore sequencing provides high throughput, the SMRT sequencing of PacBio sequences a molecule multiple times to generate high-quality data and has a better overall performance [[75\]](#page-17-0). In our study, SMRT sequencing was combined with Microwell-seq, so that the mutations with barcodes could be detected and associated with cell transcriptome.

Mitochondrial mutations are usually heteroplasmic, and the cell can tolerate a high percentage level of this variant before the biochemical threshold is exceeded [[76\]](#page-17-0). Our study regarded the mtDNA mutation as the clue of lineage tracing and found that the same phenotype contained multiple clones, implying that there were certain key attractors responsible for determining the switching between different states [\[77](#page-17-0)].

As Waddington's landscape has explained, the attractor state is regulated by underlying gene regulatory network [\[78](#page-17-0)]. Based on theory of gene regulatory networks, cancer cells also represent attractor states of the network dynamics [\[79](#page-17-0)]. Our study described the gene regulatory networks of AML progenitor cells and made comparisons with the normal and AML myeloid cell. For therapeutic purposes, it gives us a hint that drugs which help tumor cells exit from the cancer attractor and entry into a benign attractor may reduce tumor burden [\[80](#page-17-0)].

The treatment of AML has changed substantially in recent years. New targeted drugs have emerged, including midostaurin and gilteritinib to target FLT3, and ivosidenib and enasidenib to target mutant isocitrate dehydrogenase 1 and 2 [\[81](#page-17-0)]. The best responses to treatment are seen when these agents are combined with conventional chemotherapy [\[82](#page-17-0)]. Based on the comparison between AML map and HCL at a single-cell level, we proposed CCNA1 and RAB37 as new potential drug targets. They are highly expressed in only AML progenitor cell cluster rather than other tissues. Cell cycle regulators are considered attractive targets in cancer therapy [[83\]](#page-17-0). CCNA1 is a suitable immuno-therapeutic target for future clinical trials, and generating donor-derived CCNA1-specific T cells seems to be a possible approach to prolonged disease remission in post-HSCT patients [[84\]](#page-17-0). An aberrant expression of Rab proteins has been reported in multiple cancer types [[85](#page-17-0)]. The underlying mechanism of RAB37 in lung cancer has been widely discussed [[86\]](#page-17-0). However, there has been no study in AML. Moreover, transcription factors like MYB and some lncRNAs have significantly different levels of expression between AML progenitor cells and normal tissues. Even though they have barely been considered as priority targets, focusing on their interacting proteins might control their expressions [[62,](#page-17-0) [87\]](#page-17-0). We hope that our study will bring new insights into AML targeted therapy.

## 关键词

acut, cellular, hierarchy, single-cell, survey

## 相关实体

细胞类型: AML, erythroid, lymphoid, myeloid, progenitor
方法: single-cell
疾病: leukemia

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
