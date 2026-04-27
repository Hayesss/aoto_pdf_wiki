---
marker_extracted: true
title: "A pan-cancer single-cell transcriptional atlas of"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/a-pan-cancer-single-cell-transcriptional-atlas-of.md]
confidence: medium
year: 2021
---

# A pan-cancer single-cell transcriptional atlas of

> 原文: [[a-pan-cancer-single-cell-transcriptional-atlas-of]]

## 摘要

Tumor-infiltratingmyeloidcells(TIMs)arekeyregulatorsintumorprogression,butthesimilarityanddistinc- tionoftheirfundamentalpropertiesacrossdifferenttumorsremainelusive.Here,byperformingapan-cancer analysisofsinglemyeloidcellsfrom210patientsacross15humancancertypes,weidentifieddistinctfeatures of TIMs acrosscancertypes.Mastcellsinnasopharyngeal cancerwerefound tobe associated withbetter prognosisandexhibitedananti-tumorphenotypewithahighratioofTNF+/VEGFA+cells.Systematiccompar- isonbetweencDC1-andcDC2-derivedLAMP3+cDCsrevealedtheirdifferencesintranscriptionfactorsand external stimulus. Additionally, pro-angiogenic tumor-associated macrophages (TAMs) were characterized withdiversemarkersacrossdifferentcancertypes,andthecompositionofTIMsappearedtobeassociated withcertainfeaturesofsomaticmutationsandgeneexpressions.Ourresultsprovideasystematicviewofthe highlyheterogeneousTIMsandsuggestfutureavenuesforrational,targetedimmunotherapies. INTRODUCTION targeting myeloid cells are ongoing in pre-clinical and clinical studies(NakamuraandSmyth,2020),althoughtheheterogene- Tumorsarecomplexecosystemswhereheterogeneousmalig- ityofmyeloidcellsremainslessstudied. nant cells interact with both immune and nonimmune cells to TIMsconsistofseveraldistinctmajorlineagesincludingmast shapethecomplexcellularnetworkofthetumormicroenviron- cells,plasmacytoiddendriticcells(pDCs),conventionaldendritic ment (TME) (Hanahan and Weinberg, 2011).

## 背景与目的

Tumors are complex ecosystems where heterogeneous malignant cells interact with both immune and nonimmune cells to shape the complex cellular network of the tumor microenvironment (TME) (Hanahan and Weinberg, 2011). Because myeloid cells constitute a key cellular component of immune cells that infiltrate into tumors and play important roles in modulating tumor inflammation and angiogenesis (Engblom et al., 2016; Schmid and Varner, 2010), several therapeutic approaches

targeting myeloid cells are ongoing in pre-clinical and clinical studies (Nakamura and Smyth, 2020), although the heterogeneity of myeloid cells remains less studied.

TIMs consist of several distinct major lineages including mast cells, plasmacytoid dendritic cells (pDCs), conventional dendritic cells (cDCs), monocytes, and macrophages (Engblom et al., 2016). In the past decade, primarily with the aid of flow cytometry, the complexity of major myeloid lineages has begun to be revealed. Monocytes are usually classified based on the expression of surface markers CD14 and CD16 (Yang et al., 2014).

<sup>&</sup>lt;sup>12</sup>Peking University International Cancer Institute, Beijing 100191, China

<sup>&</sup>lt;sup>13</sup>These authors contributed equally

Lead contact


## 主要发现

#### Landscapes of myeloid cells in 15 cancer types revealed by scRNA-seq analysis

To generate a deep transcriptional atlas of TIMs, we obtained scRNA-seq data on myeloid cells in 380 samples from 210 patients diagnosed with one of the 15 common cancer types, including newly collected 82 treatment-naive patients of 10 cancer types ([Figure 1](#page-2-0)A; [Table S1](#page-15-0)). After strict quality control and filtration, we collected a total of 138,161 myeloid cells derived from the tumors, adjacent non-cancer tissues, peripheral blood, or lymph node of 194 patients (338 samples) across 15 common cancer types ([Figures 1A](#page-2-0), 1B, [S1A](#page-26-0), and S1B; [Table S1;](#page-15-0) [STAR](#page-19-0) [methods](#page-19-0)).

To characterize the subsets of myeloid cells and minimize batch effects among different datasets, we analyzed each dataset independently. We performed unsupervised graph-based clustering on myeloid cells and then identified four common major linages (mast cells, pDCs, cDCs, monocytes, or macrophages) based on canonical cell markers. In addition, cDCs and monocytes or macrophages could be further divided into multiple sub-populations ([Figure S1](#page-26-0)C, [STAR methods\)](#page-19-0). Using esophageal carcinoma (ESCA) as an example, mast cells, pDCs, cDCs, and monocytes/macrophages were characterized by specific high expression of *KIT*, *LILRA4*, *HLA/FCER1A*, and *CD68*/*CD163*, respectively [\(Figures 1C](#page-2-0) and 1D). Three distinct subsets in cDCs were identified [\(Figures 1E](#page-2-0) and [S1](#page-26-0)C), including two classical cDC subsets (*CLEC9A*<sup>+</sup> cDC1s and *CD1C*<sup>+</sup> cDC2s) and a mature cDC subset (*LAMP3*<sup>+</sup> cDC) recently characterized [\(Zhang et al., 2019](#page-18-1)).


## 方法概述

dictedasoneofthemainoriginsofLAMP3+cDCs(Figures5F thesimilarityanalysisfailedtoexactlyclustermacrophagesub- and S6C). Comparing with other cDC2 subsets, the setswiththesameidentityfromdifferentcancertypestogether C06_cDC2_CXCL9 sub-cluster showed higher expression of (Figure6A),indicatingthatmacrophagesubsetsexhibitedhigh CXCL9andIDO1(FiguresS6DandS6E),whichhavebeenre- levelofcomplexity,whichmightberelatedtothedominantef- ported to regulate immune activation and induce immune fects of the local tissue microenvironment on macrophages repression, respectively (Tokunaga et al., 2018; Wu et al., (Gosselin et al., 2014; Lavin et al., 2014). These findings were 2018).

## 讨论与结论

We collected a large number of myeloid cells from patients diagnosed with one of 15 cancer types to systematically investigate the complexity of TIMs. Surprisingly, distinguished from other cancer types, mast cells in NPC were characterized with high anti-tumor preference, which was supported by their association with better prognosis. Our findings identified specific cancer type with the potential to response to mast cell-targeted immunotherapy, whose possibility and mechanisms should be further explored.

Our pan-cancer scRNA-seq analysis proved that the *LAMP3*<sup>+</sup> cDCs were broadly present and extended the conclusion of their diverse origins to all cancer types. Based on the extensive transcriptional analysis, we reason that cDC1-derived and cDC2 derived *LAMP3*<sup>+</sup> cDCs are regulated by different ligand-receptor pairs and might have diverse functions. Particularly, in agreement with a recent study that elucidated the dual functions of cDC1-derived *LAMP3*<sup>+</sup> cDCs on Tregs and CD8<sup>+</sup> T cells ([Maier](#page-17-15) [et al., 2020\)](#page-17-15), we also confirmed the complex co-expression

pattern of activation and inhibitory molecules in cDC1-derived *LAMP3*<sup>+</sup> cDCs in our pan-cancer analysis. Additionally, during the transition from *CXCL9*<sup>+</sup> cDC2s to *LAMP3*<sup>+</sup> cDCs, we identified opposite trends of expression for *IDO1* and *CXCL9*, implying the enhanced immunosuppressive ability of cDC2-derived *LAMP3*<sup>+</sup> cDCs.

Aside from the reported CD163<sup>+</sup> CD14<sup>+</sup> ''pro-inflammatory'' cDC2 subset enriched in blood ([Dutertre et al., 2019](#page-16-6)), we identified a tumor-enriched cDC2 subset C03\_cDC2\_IL1B with high expression of pro-inflammatory mediators, such as *IL1B* and *TNF*. To a certain degree, the *IL1B*<sup>+</sup> cDC2s resemble the ''pro-inflammatory'' cDC2B identified in human spleen, which is also characterized with a high expression of *IL1B* ([Brown et al.


## 关键词

atlas, pan-cancer, single-cell, transcriptional

## 相关实体

细胞类型: myeloid
方法: scRNA-seq, single-cell
疾病: Tumor, cancer, tumor

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
