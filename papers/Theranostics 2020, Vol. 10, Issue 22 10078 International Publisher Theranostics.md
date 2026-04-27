---
marker_extracted: true
title: "Theranostics 2020, Vol. 10, Issue 22 10078 International Publisher Theranostics"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/theranostics-2020-vol-10-issue-22-10078-international-publisher-theranostics.md]
confidence: medium
year: 2020
---

# Theranostics 2020, Vol. 10, Issue 22 10078 International Publisher Theranostics

> 原文: [[theranostics-2020-vol-10-issue-22-10078-international-publisher-theranostics]]

## 摘要

**Background:** Urinary bladder cancer (UBC) is one of the most common causes of morbidity and mortality worldwide characterized by a high risk of invasion and metastasis; however, the molecular classification biomarkers and underlying molecular mechanisms for UBC patient stratification on clinical outcome need to be investigated.

**Methods:** A systematic transcriptomic analysis of 185 glycogenes in the public UBC datasets with survival information and clinicopathological parameters were performed using unsupervised hierarchical clustering. The gene signature for glycogene-type classification was identified using Limma package in R language, and correlated to 8 known molecular features by Gene Set Variation Analysis (GSVA). The clinical relevance and function of a glycogene was characterized by immunohistochemistry in UBC patient samples, and quantitative RT-PCR, Western blotting, promoter activity, MAL II blotting, immunofluorescence staining, wound healing, and transwell assays in UBC cells.

**Results:** A 14-glycogene signature for glycogene-type classification was identified. Among them, ST3GAL6, a glycotransferase to transfer sialic acid to 3'-hydroxyl group of a galactose residue, showed a significant negative association with the subtype with luminal feature in UBC patients (n=2,130 in total). Increased ST3GAL6 was positively correlated to tumor stage, grade, and survival in UBCs from public datasets or our cohort (n=52). Transcription factor GATA3, a luminal-specific marker for UBC, was further identified as a direct upstream regulator of ST3GAL6 to negatively regulate its transactivation. ST3GAL6 depletion decreased MAL II level, cell invasion and migration in 5637 and J82 UBC cells. ST3GAL6 could reverse the effects of GATA3 on global sialylation and cell invasion in SW780 cells.

**Conclusions:** Herein, we successfully identified a novel 14-gene signature for glycogene-type classification of UBC patients. ST3GAL6 gene, from this signature, was demonst


## 背景与目的

Urinary bladder cancer (UBC) is one of the most common causes of morbidity and mortality worldwide characterized by a high risk of invasion, metastasis and recurrence [1]. These tumors are

<sup>\*</sup>These authors contributed equally to this article.

staged using the Tumor-Node-Metastasis (TNM) system, as non-muscle-invasive bladder cancer (NMIBC; Tis, Ta, and T1) and muscle-invasive bladder cancer (MIBC; T2, T3, and T4) according to the extent of invasions. Ta tumors are restricted to the urothelium; T1 tumors have invaded the lamina propria; and T2, T3, and T4 tumors have invaded the superficial muscle, perivesical fat, and surrounding organs, respectively [2]. UBCs could be graded according to cellular characteristics as papillary urothelial neoplasm of low malignant potential (PUNLMP), low grade and high grade papillary urothelial carcinoma in the 2004 WHO/ISUP criteria [3]. Current prognostication and clinical management are highly based on above basic histopathologic evaluation.

The intratumoral and intertumoral heterogeneity at the genomic, transcriptional and cellular levels contribute to the capricious outcomes of UBC patients [4]. Even the pathologically similar, the intrinsic molecular and genetic events were quite different; thus, a number of groups used gene expression patterns to reveal the molecular subtypes which traverse stage and grade classification [5-10]. For MIBCs, the luminal-like subtype was characterized by the expression of transcription factors and markers for differentiation (GATA3, FoxA1 and KRT20) [11, 12]; whereas, the basal-like subtype was enriched with cancer stem cell, mesenchymal-like markers (KRT14, KRT5, CD44, and Snails) and squamous differentiation markers (TGM1 and PI3) [9]. Such molecular classification helps to a precise prediction of UBC outcomes and therapeutic interventions. For example, the luminal subtype with papillary feature had the longest 5-year survival; the luminal subtype with EMT feature and basal subtype


## 主要发现

#### **Molecular classification based on the expression pattern of glycogenes correlated to prognosis of UBC patients**

To investigate whether the abnormal glycogene expression defines a molecular subtype of UBC patients, we designed the study with the details shown in Figure S1. An unsupervised hierarchical clustering was carried out using 185 unique glycogenes in UBC patients from TCGA-BLCA (TCGA provisional dataset; n=408). The result demonstrated that UBC patients can be categorized into two clusters (A and B) or four subclusters (A1, A2, B1 and B2; Figure 1A). UBC patients in this dataset have been well defined as five molecular subtypes, including Luminal papillary (~35%), Luminal infiltrated (~19%), Luminal (~6%), Basal squamous (~35%), and Neuronal (~5%), based on the mRNA expression pattern combining BayesNMF with a consensus hierarchical clustering approach [9]. The strong correlation between our four- subcluster and above five-subtype classification was observed (Figure 1A). The association between subcluster B1 and Luminal papillary subtype, as well as the association between subcluster A2 and Basal squamous subtypes were especially notable. In addition, the patients in subcluster B1 were negatively associated with tumor grade (*p* < 0.0001) and tumor stage (*p* < 0.0001; Table S2), and showed significantly better prognosis than other subclusters for all stages (I-IV) (*p* = 0.0043; Figure 1B) or for stages II-III (*p* =

0.0441; Figure 1C). It is indicated that the novel glycogene expressionbased profiling (glycogene-type) may also be suitable for UBC classification with clinical outcomes.

To simplify the gene signature to differentiate the subcluster B1 from other three subclusters, 14 glycogenes (*B4GALNT1, B4GALNT2, CHSY3, FUT7, GALNT17, GGTA1P, GLT1D1, GLT8D2, GXYLT2, ST3GAL6, ST6GALNAC5, UGT2B4, UGT2B15, and UGT2B28*) were identified to be significantly dysregulated in subcluster B1, comparing with the other three subclusters, in the TCGA provisi


## 方法概述

#### **Unsupervised hierarchical clustering and assembly of the TCGA and GEO datasets**

Gene expression and clinical data from the UBC cohort in TCGA database (TCGA-BLCA) were downloaded from Genomic Data Commons Data Portal (https://portal.gdc.cancer.gov/). The FPKM expression of each gene was applied with Log(1+FPKM) and normalized with Z-score (mean-centered). Gene expression and clinical data from MSK (JCO 2013) dataset were collected from Cbioportal (https://www.cbioportal.org/) [25-27]. Medium expression of genes from this dataset was applied in the following analysis. Other public microarray data as well as the corresponding clinical data were obtained from the Gene Expression Omnibus (GEO) database (http://www.ncbi.nlm.nih. gov/geo). Gene expression in GEO were normalized with Z-score (mean-centered). In the case one gene with the multiple probes, the averaged expression was used. 185 glycogenes were obtained from the glycogene database (GGDB, https://acgg.asia/ ggdb2/) and the previous reports [18, 28, 29].

Unsupervised hierarchical clustering of TCGA and GEO datasets were indicated in Morpheus (https://software.broadinstitute.org/morpheus) by Average Linkage method with One minus Pearson correlation. Different expressed genes in TCGA-BLCA dataset were analyzed using Limma, an R package using the linear models to assess the differential expression, based on the Log(1+FPKM). Glycogenes exhibited remarkable differential expression between B1 subcluster and other subclusters (A1, A2 and B2; Log2 Fold Change > 1.5, p < 0.05, and FDR < 0.01) and the confirmation study was performed in other three independent datasets (MSK (JCO 2013), GSE13507, and GSE32894).

To investigate the relationship between glycogene-types and molecular features, data from 12 independent datasets (TCGA-BLCA, MSK (JCO 2013), GSE13507, GSE32894, GSE48276, GSE128702, GSE48075, GSE87304, GSE32584, GSE31684, GSE128192 and GSE3167; n=2,130 in total) were analyzed using Gene Set Variation Ana


## 讨论与结论

Post-translational modifications including glycosylation play key roles in UBC development. In this study, to our knowledge, we are the first to provide a global and unbiased approach to identify a novel 14-glycogene signature for glycogene-type based classification and prediction of clinical outcomes in UBC patients by integrating the transcriptomic data and corresponding survival information. This glycogene-type based classification was validated in a total number of 962 UBC patients derived from four independent datasets. From this 14-glycogene signature, overexpressed ST3GAL6 was further identified to be positively associated with tumor aggressiveness and poor prognosis in UBC patients, from both public datasets and our own cohorts.

Multiple strategies for molecular classification of UBCs have been reported [5, 6, 8-10, 37]. Molecular subtypes, including luminal, basal, squamousdifferentiation, epithelial-mesenchymal, cancer-stem cell, Claudin-low, p53-like, and neuroendocrine, started to be used for predictions of clinical outcomes and therapeutic interventions. However, most of these classifications were based on complicated gene expression patterns; the underlying molecular mechanisms are still to be investigated. Herein, we simplified the expression pattern to a 14-gene signature, and furthermore a glycogene (ST3GAL6), whose expression level was negatively correlated with luminal feature, as well as the positive associations with other features (including basal feature) in the majority of 12 datasets (n=2,130 in total). The novel finding that luminal-specific transcriptional factor GATA3 suppressed ST3GAL6 gene transactivation provided a possible mechanistic evidence for the negative association between ST3GAL6 mRNA level and the subtype with luminal feature in UBCs.

Aberrant global glycosylation has been implicated in cancer development and associated with cell adhesion, invasion and metastasis. The elevated levels of sLeA and sLex, which are essential fo


## 关键词

International, Issue, Publisher, Theranostics, Vol

## 相关实体

疾病: cancer

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
