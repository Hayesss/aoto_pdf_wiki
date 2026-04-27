---
marker_extracted: true
title: "RNA codon expansion via programmable"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/rna-codon-expansion-via-programmable.md]
confidence: medium
year: 2025
---

# RNA codon expansion via programmable

> 原文: [[rna-codon-expansion-via-programmable]]

## 摘要

Article RNA codon expansion via programmable pseudouridine editing and decoding Jiangle Liu1,2,3,11, Xueqing Yan1,11, Hao Wu1,3,11, Ziqin Ji2, Ye Shan2,3, Xinyan Wang4, Yunfan Ran5, Yichen Ma1,3, Caitao Li6, Yuchao Zhu2,7, Ruichu Gu1,8, Han Wen8,9,10, Chengqi Yi1,2,3,9 ✉ & Received: 29 April 2024 Peng R. Chen2,3,7 ✉ Accepted: 15 May 2025 Published online: xx xx xxxx The incorporation of non-canonical amino acids (ncAAs) enables customized chemistry Check for updates to tailor protein functions1–3. Genetic code expansion offers a general approach for ncAA encoding by reassigning stop codons as the ‘blank’ codon; however, it is not completely orthogonal to translation termination for cellular transcripts. Here, to generate more bona fide blank codons, we developed an RNA codon-expansion (RCE) strategy that introduces and decodes bioorthogonally assignable pseudouridine (Ψ) codons (ΨGA, ΨAA or ΨAG) on specified mRNA transcripts to incorporate ncA...

## 背景与目的

Programmable Ψ Stop codon via gsnoRNA Ψ codon Undisturbed Non-target Non-target stop codon Unmodified RCE components gsnoRNA Endogenous targeted sequence UGA/UAA/UAG DKC1 DKC1 ncAA PylRS to aminoacylate Ψ codon: Specified mRNA Non-target mRNA Ribosome gsnoRNA Ψ codon-tRNAPyl Ψ codon-tRNAPyl with ncAA ΨGA/ΨAA/ΨAG b d gsnoRNA dosage per reporter = 0.25 gsnoRNA dosage per reporter = 1 PyIRS–tRNAPyl per reporter = 1 PyIRS–tRNAPyl per reporter = 4 30 bp 30 bp 30 bp 30 bp [0–2206244] [0–1795897] [0–1482475] [0–3600313] T CCTATATCACCGGAtgaGGATCAGCCCCA CCTATATCACCGGAtgaGGATCAGCCCCA CCTATATCACCGGAtgaGGATCAGCCCCA CTATATCACCGGAtgaGGATCAGCCCCAG Deletion at Ψ site Deletion at Ψ site Deletion at Ψ site Deletion at Ψ site c e 100 75 50 25 0 gsnoRNA dosage gctrl 0.

## 主要发现

A 30 GC T A 31 TC G A 32 CG T A 33 TC G C 37 AG T C 38 AG T C 39 AG T A 40 CG T A 41a CG T A 41b TC G C 41c AG T A 42 GC T A 43 CG T PosRefMut –ncAA UGA –ncAA UGA –ncAA UGA +ncAA ΨGA +ncAA ΨGA +ncAA ΨGA 000.0 500.0 010.0 Readthrough 510.0 020.0 1.0 2.0 3.0 WT NN A 27 CG T A 28 CG T C 29a AG T A 29b GC T A 30 GC T A 31 CG T A 32 CG T A 33 TC G A 37 CG T C 38 AG T A 39 GC T A 40 CG T A 41a CG T C 41b AG T A 41c CG T A 42 GC T A 43 GC T PosRefMut 0000.0 5200.0 0500.0 5700.0 0010.0 1.0 Readthrough 2.0 3.0 (ΨGA)-tRNAPyl on UGA RCE(ΨGA) WT NN C 27 AG T C 28 AG T A 29a TC G A 29b GC T A 30 GC T C 31 AG T A 32 CG T WT (ΨGA)-tRNAPyl A 33 TC G C 37 AG (ΨGA)-tRNAPyl on UGA T C 38 AG T A 39 TC G A 40 CG T A 41a CG T A 41b GC T A 42 TC G A 43 TC G PosRefMut (ΨGA)-tRNAPyl 1.0 2.0 Readthrough 4.0 000.0 500.0 010.0 510.0 3.0 30 40 30 40 30 40 37 37 37 Fig. 2 | Screening and evaluation of the specific and efficient decoder ratios are truncated to improve visualization. c,d, Representative fluorescence tRNA for the ΨGA codon over the UGA codon. a, Scheme demonstrating the images showing readthrough of (ΨGA)-tRNAPyl on UGA and ΨGA codons in screening strategy of decoder tRNA for the ΨGA codon.

## 方法概述

### **Cell culture**

HEK293T, U-2 OS, COS-7 and HeLa cells were cultured in DMEM medium (Corning, 10-013-CVR) and CHO-K1 cells were cultured in DMEM/F12 medium (Gibco). All cells were cultured with medium containing 10% FBS and 1% penicillin/streptomycin (both from Gibco, v/v) at 37 °C with 5% CO2. To passage cells, they were initially rinsed with PBS (Corning), and then treated with 0.25% Trypsin (Gibco) before incubation (37 °C, 1 min). Following this, the trypsin was neutralized by adding FBS-containing medium. The cells were subsequently collected by centrifugation (500*g*, 5 min), counted, and divided for various experimental uses. All cells were confirmed to be free from mycoplasma contamination using a mycoplasma detection kit (TransGene Biotech, FM311-01) prior to use.


## 讨论与结论

In summary, we established a general applicable RCE strategy and obtained three triply orthogonal pairs, ΨGA:(ΨGA)-tRNAPyl, ΨAA:(ΨAA)-tRNAPyl and ΨAG:(ΨAG)-tRNAPyl, for site-specific ncAA incorporation into proteins in mammalian cells. Using ribosome profiling and proteomics analysis, we demonstrated the translatome-wide decoding specificity of the RCE strategy, which significantly reduced off-target stop codon readthroughs compared with the standard GCE method. The high specificity of the RCE strategy was verified through multiple approaches, indicating that RCE-based protein decaging offers a general strategy for activation of enzymes of interest. In the encoding component, we identified high Ψ codon yields on these specified mRNA transcripts with specified gsnoRNAs . In the decoding component, the (Ψ codon)-tRNAPyl decode Ψ codons with robust Ψ codon preferences across various transcripts, consistent with the globally reduced off-target readthrough events. The specificities in encoding and decoding processes contributed to the overall ncAA-incorporating specificity of our RCE strategy, which could be further advanced by engineering the relevant mRNAs, small nucleolar RNAs (snoRNAs) and decoder tRNAs. In addition, although we focused on the stop codons in this study, our RCE strategy could in principle be extended to sense codons, owing to its programmability and specificity during the encoding and decoding processes. Indeed, a new GCE strategy leveraging rare codons has been reported recently51.

In addition to pseudouridine, the RCE approach may allow for the utilization of various post-transcriptionally modified RNA-expanded codons for translation. More than 150 types of chemical modification have been identified in cellular RNAs so far, most of which can influence the stability, structure and interactions of RNA to a certain extent, including *N* -methyladenosine, *N* -methylpseudouridine, 5-methylcytosine and 2′-*O*-methylation22,.


## 关键词

RNA, codon, expansion, programmable, via

## 相关实体

暂无识别到特定实体

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
