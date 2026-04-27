---
marker_extracted: true
title: "DOI:10.1038/s41467-018-03843-3 Quantitative assessment of protein activity in"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/doi101038s41467-018-03843-3-quantitative-assessment-of-protein-activity-in.md]
confidence: medium
year: 2018
---

# DOI:10.1038/s41467-018-03843-3 Quantitative assessment of protein activity in

> 原文: [[doi101038s41467-018-03843-3-quantitative-assessment-of-protein-activity-in]]

## 摘要

ARTICLE OPEN DOI:10.1038/s41467-018-03843-3 Quantitative assessment of protein activity in orphan tissues and single cells using the metaVIPER algorithm Hongxu Ding1,2, Eugene F. DouglassJr.1, Adam M. Sonabend3, Angeliki Mela3, Sayantan Bose1,9, Christian Gonzalez1,10, Peter D. Canoll3, Peter A. Sims1, Mariano J. Alvarez1,4 & Andrea Califano1,4,5,6,7,8 Weandothershaveshownthattransitionandmaintenanceofbiologicalstatesiscontrolled bymasterregulatorproteins,whichcanbeinferredbyinterrogatingtissue-specificregulatory models(interactomes)withtranscriptionalsignatures,usingtheVIPERalgorithm.Yet,some tissuesmaylackmolecularprofilesnecessaryforinteractomeinference(orphantissues),or, as for single cells isolated from heterogeneous samples, their tissue context may be unde- termined.Toaddressthisproblem,weintroducemetaVIPER,analgorithmdesignedtoassess proteinactivityin tissue-independent fashionbyintegrative analysisofmultiple, non-tissue- matched interactomes.

## 背景与目的

T interactome inference. These “orphan tissues” include, for more of them. Based on previous results7, VIPER can accurately instance, rare or poorly characterized cancers, as well as pro- infer differential protein activity, as long as 40% or more of its genitor states during lineage differentiation. In addition, the transcriptional targets are correctly identified. As a result, even specific tissue lineage of a sample may be poorly defined, thus partial regulon overlap may suffice. Indeed, paradoxically, there preventing selection of appropriate interactome models. Con- are cases where a protein’s regulon may be more accurately sider, for instance, a single cell isolated from a heterogeneous represented in a non-tissue matched interactome than in the sample, such as whole brain or stroma-...

## 主要发现

Overview of metaVIPER. Let us assume a tissue context T for which a matched tissue-specific interactome was not available. Furthermore, without loss of generality, let us focus on a specific protein of interest P and on its T-specific regulon R<sub>T</sub>. Given a sufficient number of additional tissues $T_1 \dots T_N$ for which accurate, context-specific interactomes are available, we hypothesize that R<sub>T</sub> will be at least partially recapitulated in one or more of them. Based on previous results, VIPER can accurately infer differential protein activity, as long as 40% or more of its transcriptional targets are correctly identified. As a result, even partial regulon overlap may suffice. Indeed, paradoxically, there are cases where a protein's regulon may be more accurately represented in a non-tissue matched interactome than in the tissue-specific one. This may occur, for instance, when expression of the gene encoding for the protein of interest has little variability in the tissue of interest and greater variability in a distinct tissue context where the targets are relatively well conserved. A key challenge, however, is that one does not know a priori which of the tissue-specific interactomes may provide reasonable vs. poor models for R<sub>T</sub>.

To address this challenge, we leverage previous studies showing that if an interactome-specific regulon provides poor $R_T$ representation, approaching random selection in the limit, then it will also not be statistically significantly enriched in genes that are differentially expressed in a tissue-specific signature $S_T$ . Thus, if one were to compute the enrichment of all available regulons for the protein P in the signature $S_T$ , only those providing a good representation will produce statistically significant enrichment, if P is differentially active in the tissue of interest. Conversely, if the

Fig. 1 Inferring protein activity with metaVIPER. a Overview of metaVIPER.


## 方法概述

Regulatory networks. All regulatory networks were reverse engineered by ARA-CNe9 and summarized in Supplementary Table. Twenty-four core TCGA RNA-Seq derived interactomes are available in R-package aracne.networks from Bioconductor. The TCGA human SKCM network was assembled from RNA-Seq profiles. TCGA RNA-Seq level 3 data (counts per gene) were obtained from the TCGSA data portal, and normalized by Variance Stabilization Transformation (VST), as implemented in the DESeq package from Bioconductor. The human B lymphocyte interactome was reported by Basso et al.9. The human T lymphocyte interactome was reported by Piovan et al.. The human brain tumor regulatory networks were assembled from four more gene expression datasets besides the TCGA glioblastoma RNA-Seq dataset. For the Rembrandt, Phillips, TCGA-Agilent, and TCGA-Affymetrix, informative probe clusters were assembled with the cleaner algorithm and the expression data were summarized and normalized with the MAS5 algorithm, as implemented in the affy R-package from Bioconductor . Differences in sample distributions were removed with the robust spline normalization procedure implemented in the lumi R-package from Bioconductor. In a similar way, differences in sample distribution for the TCGA-Agilent dataset were removed by the robust spline normalization method. ARA-CNe was run with 100 bootstrap iterations using 1813 transcription factors (genes annotated in gene ontology molecular function database, as GO:0003700, "transcription factor activity", or as GO:0003677, "DNA binding", and GO:0030528, "transcription regulator activity", or as GO:00034677 and GO: 0045449, "regulation of transcription"), 969 transcriptional cofactors (a manually curated list, not overlapping with the transcription factor list, built upon genes annotated as GO:0003712, "transcription cofactor activity", or GO:0030528 or GO:0045449), and 3370 signaling pathway related genes (annotated in GO biological process database as GO:0007165 "signal...


## 讨论与结论

We have shown that integration of multiple interactomes using an evidence integration platform (metaVIPER) can provide accurate assessment of protein activity independent of tissue lineage. By systematic, we mean that activity of 6000 proteins can be reproducibly assessed from any tissue, independent of their gene expression; this is especially valuable in single cell analyses. MetaVIPER can thus help infer activity of key regulators in tissues lacking a matched interactome—either due to low sample availability (orphan tissues) or to lack of tissue lineage information—as well as in highly heterogeneous single cell populations isolated from bulk tissue. We propose a specific metric (ECDF $_{\rm NESI}$ ) to assess whether a specific repertoire of interactomes is adequate for the metaVIPER analysis of an unknown or orphan tissue

MetaVIPER is especially useful for the study of single cell biology, as its results are largely independent of sequencing depth and allow quantitative inference of protein activity even when the corresponding mRNA is undetectable. Indeed, differential activity of established lineage markers of T, B, and melanoma cells could be clearly assessed in single cells from a complex mixture, even though most of these markers were either not detected or could not be identified as statistically significantly differentially expressed at the mRNA level. The reduction in bias and batch effects is an additional advantage, allowing integration of datasets from multiple labs or generated at different times, thus addressing the important issue of single cell data reproducibility.

Among the most obvious limitations of the method, metaVI-PER cannot accurately measure activity of proteins whose regulons are not adequately represented in at least one of the available interactomes. This includes proteins whose targets are exceedingly tissue-specific within rare tissue types and single cell sub-populations, for instance in LIHC and TGCT.


## 关键词

DOI, Quantitative, activity, assessment, protein, s41467-018-03843-3

## 相关实体

暂无识别到特定实体

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
