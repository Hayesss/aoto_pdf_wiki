---
marker_extracted: true
title: "Experimental reproducibility limits the correlation"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/experimental-reproducibility-limits-the-correlation.md]
confidence: medium
year: 2022
---

# Experimental reproducibility limits the correlation

> 原文: [[experimental-reproducibility-limits-the-correlation]]

## 摘要

Large-scalestudiesofhumanproteomeshaverevealedonlyamoderatecorrelationbetweenmRNAandpro- teinabundances.Itisuncleartowhatextentthismoderatecorrelationreflectspost-transcriptionalregulation andtowhatextentitreflectsmeasurementerror.Here,byanalyzingreplicateprofilesoftumorsandcelllines, weshowthatthereisconsiderablevariationinthereproducibilityofmeasurementsoftranscriptsandpro- teins from individual genes. Proteins with more reproducible measurements tend to have a higher mRNA- protein correlation, suggesting that measurement reproducibility accounts for a substantial fraction of the unexplainedvariationbetweenmRNAandproteinabundances.Thereproducibilityofindividualproteinsis somewhat consistent across studies, and we exploit this to develop an aggregate reproducibility score that explains a substantial amount of the variation in mRNA-protein correlations across multiple studies. Finally,weshowthatpathwayspreviouslyreportedtohaveahigher-than-averagemRNA-proteincorrelation maysimplycontainmembersthatcanbemorereproduciblyquantified. INTRODUCTION ease samples from humans have therefore primarily focused onDNAsequencevariationandtranscriptomicvariation. Proteins are the primary actors in our cells, responsible for As transcriptomes are easier to quantify than proteomes, almost all biological activities. Therefore, understanding how mRNAabundancesareoftenusedasaproxyforproteinabun- protein abundances vary between healthy and disease states dances.

## 背景与目的

Proteins are the primary actors in our cells, responsible for almost all biological activities. Therefore, understanding how protein abundances vary between healthy and disease states can provide an insight into how biological activities are altered in disease conditions. Among patients with the same disease, e.g., breast cancer, variation in protein abundances may explain differences in survival outcomes (Osz et al., 2021 } ) and drug responses (Shenoy et al., 2020\). Consequently, significant efforts have been made recently to characterize proteomes across large patient cohorts \(Ellis et al., 2013). However, our ability to quantify protein abundances at scale has lagged behind our ability to sequence genomes and quantify mRNA abundances. Large-scale efforts to molecularly characterize healthy and disease samples from humans have therefore primarily focused on DNA sequence variation and transcriptomic variation.

As transcriptomes are easier to quantify than proteomes, mRNA abundances are often used as a proxy for protein abundances. However, the relationship between mRNA abundances and protein abundances is complex and non-linear and varies significantly from protein to protein. Consistent with this, largescale studies in humans and model organisms have revealed that for most genes there is only a moderate correlation between mRNA and protein abundances (Buccitelli and Selbach, 2020; Vogel and Marcotte, 2012\). We note that correlations between mRNA and protein abundances can be calculated in two different ways: across all proteins within a given sample (i.e., in a given cell line, are the most abundant proteins also the most abundant transcripts?) or for a single protein across multiple

Systems Biology Ireland, University College Dublin, Dublin, Ireland

Lead contact

<sup>\*</sup>Correspondence: colm.ryan@ucd.ie

samples (i.e.


## 主要发现

### A standardized pipeline reveals differences in the mRNA-protein correlation across studies

The average mRNA-protein correlation reported for different tumor proteomic profiling efforts varies substantially across studies—ranging from 0.23 in an early proteomic study of colorectal cancer (Zhang et al., 2014\) to 0.53 in a recent study of lung adenocarcinoma \(Gillette et al., 2020\) (Table 1). However, it is not meaningful to directly compare the reported correlations because the methods used to quantify the mRNA-protein correlation have varied across studies—different studies have used different summary statistics (mean versus median), different correlation metrics (Pearson versus Spearman), and different criteria for protein inclusion (e.g., no missing values, at least 30% measured values, only the 10% most variable proteins) \(Table 1\). To enable a more direct comparison across studies, we calculated the mRNA-protein correlation for thirteen proteomic studies using a standardized pipeline. The datasets analyzed comprise ten studies of tumor samples (Clark et al., 2019; Dou et al., 2020; Gillette et al., 2020; Huang et al., 2021; Krug et al., 2020; Mertins et al., 2016; Vasaikar et al., 2019; Wang et al., 2021; Zhang et al., 2014, ), two studies of cancer cell lines \(Guo et al., 2019; Nusinow et al., 2020\), and one study of healthy tissues (Jiang et al., 2020\). Within each study, we calculated the median Spearman correlation between mRNA and protein for all proteins that were measured in at least 80% of samples \(STAR Methods; Tables 1 and S1\). Applying the same pipeline using Pearson correlation rather than Spearman correlation revealed broadly similar results (Table 1\), and so throughout the remainder of the paper, we focus our analysis on correlation calculated using Spearman correlation as it is the metric most commonly used in proteogenomic studies (9 of 13 studies).

Across all studies, the median recalculated correlation was 0.


## 方法概述

lower-than-average mRNA-protein correlation that may be viouslyidentifiedashavingahighmRNA-proteincorrelationare attributedtopost-transcriptionalmechanisms,thehigher-than- likely just more reproducibly measured. We therefore suggest averagemRNA-proteincorrelationpreviouslyobservedformeta- that conclusions about functional groups with higher or lower bolicpathwaysmaysimplyreflectmorereproduciblemeasure- mRNA-proteincorrelations,especiallywithregardtothepoten- mentsoftheirconstituentproteinsandtranscripts. tial role played by post-transcriptional regulation, should be made only after accounting for variation in the measurement DISCUSSION reproducibility of their constituent proteins.

## 讨论与结论

Here, we have demonstrated that the reproducibility of protein and transcript measurements is a very significant factor in the observed correlations between mRNA and protein abundances. After taking this into account, we found that some pathways previously identified as having a high mRNA-protein correlation are likely just more reproducibly measured. We therefore suggest that conclusions about functional groups with higher or lower mRNA-protein correlations, especially with regard to the potential role played by post-transcriptional regulation, should be made only after accounting for variation in the measurement reproducibility of their constituent proteins. To this end, we have generated an aggregate protein reproducibility rank for each protein that can explain a significant amount of the variance across multiple proteogenomic studies and that may be useful for identifying those proteins that can be reliably and

Figure 7. Metabolic pathways with higher-than-average mRNA-protein correlations may reflect differential reproducibility Bar charts displaying the KEGG pathway enrichment analysis of the CCLE mRNA-protein correlation before (left) and after (right) accounting for protein-protein and mRNA-mRNA reproducibility. The log10 of Benjamini-Hochberg false discovery rate (FDR)-corrected p values calculated using Mann-Whitney U test is used to assess enrichment for the pathway. For each bar chart, the gray line indicates the threshold considered for significant enrichment (FDR < 0.05). If the enrichment is below the threshold, then it is not considered significant. The bars are colored orange if the median mRNA-protein correlation of genes within the pathway is greater than the median mRNA-protein correlation of genes not in the pathway; otherwise, the bars are colored blue.

reproducibly measured by mass spectrometry. Such proteins may be more useful to assay in, e.g., diagnostic panels.


## 关键词

Experimental, correlation, limits, reproducibility

## 相关实体

疾病: cancer, tumor

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
