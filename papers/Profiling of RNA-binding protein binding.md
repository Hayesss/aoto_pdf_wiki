---
marker_extracted: true
title: "Profiling of RNA-binding protein binding"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/profiling-of-rna-binding-protein-binding.md]
confidence: medium
year: 2024
---

# Profiling of RNA-binding protein binding

> 原文: [[profiling-of-rna-binding-protein-binding]]

## 摘要

ture RBP–RNA interactions through in situ RT. We demonstrate that yield (Fig. 1d and Extended Data Fig. 1f,g). Altogether, ARTR-seq specifi- ARTR-seq sensitively profiles RBP targets with good sequencing quality, cally and effectively reverse transcribes RNAs near the targeted protein using as few as 20 cells or a single tissue section. Additionally, an imag- into biotinylated cDNA products. ing step can be readily built into the ARTR-seq procedure, providing We next tested ARTR-seq on PTBP1 using 40,000 HepG2 or HeLa direct spatial information of RBPs. With ARTR-seq, we show distinct cells, and compared the results with the published data from several binding patterns of splicing factors and the YTH family reader proteins known methods, namely CLIP, iCLIP, irCLIP, eCLIP, sCLIP, tRIP, LACE-seq of RNA N6-methyladenosine (m6A) modification. ARTR-seq unbiasedly and RT&Tag9–13,22,26,27. We observed that ARTR-seq displayed a compara- detects RNA binding by RBPs in both cytoplasm and nucleus and meas- ble or higher percentage of usable reads compared to published meth- ures RBP binding strength on RNA substrates. Furthermore, ARTR-seq ods, indicating a high complexity of the ARTR-seq libraries (Extended could monitor dynamic RNA binding by G3BP1 during stress granule Data Fig. 2a,b). Then, we calculated the correlation between biological (SG) assembly on a small timescale of 10 minutes. replicates (R = 0.

## 背景与目的

SuperScript III – – – – + Fig. 1 | ARTR-seq strategy and validation. a, Scheme of ARTR-seq. b, RT–qPCR was the loading control. d, Immunofluorescence imaging of the secondary analysis showing the RT activity of tested purified pAG-RTase fusion proteins. antibody (secondary Ab; yellow), pAG-RTase (red), biotinylated cDNA (green) Two commercial RTases, SuperScript II and SuperScript III, were loaded as and nucleus (blue) for PTBP1 ARTR-seq. The line graph analysis shows relative positive controls. n = 3 biological replicates. c, Biotin dot blot assay showing fluorescence intensity along the line. Scale bar, 10 μm. biotinylated cDNA products produced from ARTR-seq. Methylene blue staining Article The two methods were comparable when the distance from peaks to This suggests that the application of RNase may reduce reads from UGCAUG was within 200 nts (Extended Data Fig. 4b). It is worth not- direct targets, thereby potentially elevating the ratio of nonspecific or ing that RBFOX2 may have other noncanonical binding sites beyond indirect binding signals (Extended Data Fig. 6f). Overall, our studies the UGCAUG motif, as suggested by the similar percentage of distant revealed that RNase treatment could improve ARTR-seq resolution. RBFOX2 eCLIP peaks from this motif.

## 主要发现

#### Strategy and development of ARTR-seq

In ARTR-seq, we started with rapid formaldehyde fixation to preserve the cellular structure, followed by permeabilization of cell membranes (Fig. 1a(i)). We then targeted the reverse transcriptase (RTase) to the RBP of interest using corresponding antibodies (Fig. 1a(ii)). This involved delivering the primary antibody for RBP recognition (Fig. 1a(ii)1), followed by a secondary antibody to enhance the local antibody concentration, capitalizing on the potential for multiple secondary antibodies to bind a single primary antibody (Fig. 1a(ii)2). Subsequently, a fusion protein of protein A/G and RTase (pAG-RTase) was delivered to bind both primary and secondary antibodies, enabling site-specific attachment of RTase to the target RBP (Fig. 1a(ii)3). Each step was followed by thorough washing to remove any unbound antibodies or pAG-RTase.

After localizing RTase to the RBP, we initiated in situ RT at RBP binding sites by adding necessary RT components (Fig. 1a(iii)). To achieve efficient RT, we screened three commonly used RTases, including engineered Moloney murine leukemia virus (MMLV) RTase $^{24,25}$ , human immunodeficiency virus RTase and a truncated version of engineered MMLV RTase (25–497) in the pAG-RTase fusion constructs with a 30-amino-acid linker (Extended Data Fig. 1a,b). By employing RT with quantitative polymerase chain reaction (RT–qPCR), we confirmed pAG-MMLV RTase (25–497) as the most active and selected it for subsequent studies (Fig. 1b and Extended Data Fig. 1c).

To identify all RBP binding sites without sequence bias, we applied random RT primers with an adapter tag for library construction, and extended the primer length from commonly used 6 nucleotides (nts) to 10 nts to enhance RT efficiency (Extended Data Fig. 1d). For effective cDNA enrichment, biotinylated dNTPs were introduced into cDNA products.


## 方法概述

#### **Cell culture and stress treatment**

HeLa cells (American Type Culture Collection (ATCC) catalog no. CCL-2) and HepG2 cells (ATCC, catalog no. HB-8065) were purchased from ATCC and cultured in DMEM medium (Gibco) supplemented with 10% fetal bovine serum (Gibco) and penicillin-streptomycin (Gibco). K562 cells (ATCC, catalog no. CCL-243) were obtained from ATCC and cultured in RPMI 1640 Medium (Gibco) supplemented with 10% (v/v) fetal bovine serum. Penicillin-streptomycin (Gibco) and 2 mM l-glutamine (Gibco). Cells were grown at 37 °C with 5% CO2. For NaAsO2 treatment, HeLa cells were grown to 90% confluence and replaced in the prewarmed DMEM medium containing 0.5 mM NaAsO2, which was further maintained at 37 °C with 5% CO2 for indicated times.


## 讨论与结论

In this work, we present ARTR-seq, a method that captures RBP binding sites using in situ RT by antibody-located RTase. ARTR-seq demonstrated high sensitivity and specificity, even when using as few as 20 cells or limited tissues. The procedure is compatible with immunofluorescence imaging, providing direct spatial information of the targeted proteins without affecting downstream sequencing. With ARTR-seq, we observed the unique binding characteristics of PTBP1, RBFOX2 and HNRNPC related to their splicing regulatory roles. ARTR-seq also detected the preferences of m A reader proteins, YTHDF1, YTHDF2 and YTHDC1. Furthermore, we showed dynamic RNA binding of G3BP1 during SG assembly.

One advantage of ARTR-seq is the use of in situ RT to bypass the antibody-based IP step, thereby reducing material loss. ARTR-seq is also highly versatile and applicable for cell lines, tissues, and even clinical formaldehyde-fixed samples. Both inspired by CUT&Tag, ARTR-seq displays distinct advantages compared to the recently reported RT&Tag. First, ARTR-seq uses random primers to unbiasedly capture local signals, while RT&Tag uses oligo(dT) primer for RT, potentially losing signals from nonpolyadenylated RNAs. Additionally, RT&Tag may experience reduced local resolution due to uniform RT initiation from the poly-A tail and long matured mRNA length (roughly 2,065 bp), leading to coverage bias toward the RNA 3′ end. Second, Tn5 tagmentation on the RNA–cDNA heteroduplex is less efficient, hindering its applications when using limited starting materials. Third, ARTR-seq can be applied in various cellular compartments, whereas RT&Tag is limited to the isolated nucleus.

Investigations of dynamic RBP binding have been hindered by low UV-crosslinking efficiency, long incubation time and high material demands using the existing methods.


## 关键词

Profiling, RNA-binding, binding, protein

## 相关实体

暂无识别到特定实体

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
