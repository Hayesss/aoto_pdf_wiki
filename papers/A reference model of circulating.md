---
marker_extracted: true
title: "A reference model of circulating"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/a-reference-model-of-circulating.md]
confidence: medium
year: 2024
---

# A reference model of circulating

> 原文: [[a-reference-model-of-circulating]]

## 摘要

a framework for the deployment of single-cell genomics in hematology, previously shown to represent a rare cell population enriched with for the diagnosis of MDS, and possibly other stem cell-related blood self-renewal capacity in both the BM and cord blood13. Our model malignancies, from the PB, reducing the need for BM analysis. included data on 14,440 HLF and AVP expressing HSCs that could be matched with cells from independent BM atlases14, suggesting that, Results under a steady state, HSCs with potential self-renewal capacity are HSPC states observed across humans in PB present in the PB (Extended Data Fig. 3f). Further functional studies To evaluate interpersonal diversity in subtype distribution and regu- are needed to establish this finding. Together with HLF and AVP, we dis- lation of cHSPCs, we combined multiplexed scRNA-seq, bulk DNA covered 14 genes expressed at least 1.75-fold higher in HSCs compared genotyping and integrated clinical data (Fig. 1a). Multiplexing was with their 2 immediate differentiation branches (Extended Data Fig. 3g resolved using SNPs identified in the 3′-UTR of cHSPCs’ RNA, facili- and Supplementary ). We identified several transcription fac- tating precise matching of cells to individuals and improving control tors (TFs) enriched in HSCs, including HOXB5, TLE4 and GATA3 (Fig. 1c). for batch effects and doublets.

## 背景与目的

production genotyping + CH panels ×148 23–91 y + ears old 50 m p l a o ti f e P n B t per P1(98.34%) Complete CBC PBMC Sample Magnetic bead- CD34+ fraction scRNA library prep history isolation pooling based CD34 enriched from (10×) and (Ficoll) enrichment 0.1% to >90% sequencing (Illumina/Ultima) MEBEMP-E Resource by comparison of TCF7 and IRF8 expression (Fig. 1g,h and Extended Our previous work19 and the work of others20 correlated high RDW with Data Fig. 4c). We therefore termed this population natural killer (NK) CH and predisposition to acute myeloid leukemia. Our data suggest cell, T cell and DC progenitors (NKTDPs)17,18. To summarize, our map that reduction in CLP frequencies is associated with CH (Extended Data of cHSPCs showed a rich spectrum of progenitor states, which refined Fig. 6a). A similar trend was suggested by genotyping of transcriptomes previous analyses and a remarkable consistency of these states across (GoT)21 performed on one of our DNMT3A R882H cases, showing a individuals. This provided an opportunity for deciphering interindi- lower fraction of CLP cells within the mutant clone (P < 0.005, Fisher’s vidual hematopoietic variability based on our solid and quantitative exact test; Extended Data Fig. 6b). Although this trend was suggested in definition of cHSPC subtypes. other GoT data22, sample size is insufficient to prove it statistically and explore the clonal mechanisms underlying it.

## 主要发现

#### **HSPC states observed across humans in PB**

To evaluate interpersonal diversity in subtype distribution and regulation of cHSPCs, we combined multiplexed scRNA-seq, bulk DNA genotyping and integrated clinical data (Fig. [1a](#page-1-0)). Multiplexing was resolved using SNPs identified in the 3′-UTR of cHSPCs' RNA, facilitating precise matching of cells to individuals and improving control for batch effects and doublets. Altogether, we collected cHSPCs from 79 men and 69 women between the ages of 23 years and 91 years (median 61.5 years) (Extended Data Fig. 1a and Supplementary Table 1). We performed deep targeted somatic mutation analysis to identify cases of CH (Supplementary Table 1[\)10](#page-9-6). After quality control and filtering, we retained 840,104 single-cell profiles, which were normalized to control for sequencing-platform batch effects and combined to construct and annotate a metacell manifold model (Extended Data Fig. 1b,c). We retained 626,966 CD34+ single cells for downstream analysis (Extended Data Fig. 1d). These formed a rich repertoire of states, associated with cHSPCs and their differentiation trajectories (Fig. [1b](#page-1-0) and Extended Data Fig. 1e,f). The derived model recapitulated and deepened earlier characterization efforts of HSPC states from the BM. We noted that, although we could not assume that cHSPCs fully reflect BM HSPC dynamics, previous studies, as well as our own BM scRNA-seq comparisons, supported at least partial compatibility between the two (Extended Data Figs. 2 and 3a). One notable characteristic specific to cHSPCs was, however, the repression of cell-cycle gene expression (Extended Data Fig. 3b), previously demonstrated by others . Importantly, we found our cHSPC model to be consistent across individuals. The median number of individuals contributing cells to each metacell was 84 and all metacells included cells from at least 47 individuals.


## 方法概述

#### **Patient recruitment**

All healthy reference model individuals (*n* = 148, analyzed in Figs. [1–](#page-1-0) and Extended Data Figs. 1–6) volunteered to participate in our study and donated blood at the Weizmann Institute of Science (WIS) between November 2020 and December 2023. They were recruited from the WIS community and primary care clinics and consisted of 79 men and 69 women aged 23–91 (median 61.5) years. Their demographic data and CBCs are included in Supplementary Table 1. Written informed consent allowing access to their demographic, longitudinal CBC and sequencing data (CH and genotyping panels) was obtained from all participants in accordance with the Declaration of Helsinki. All relevant ethical regulations were followed and all protocols were approved by the WIS ethics committee (under Institutional Review Board (IRB) protocol no. 283-1).

For the main reference model (Figs. [–3\)](#page-5-0), recruitment was intended to allow characterization of the normal variation in cHSPC states. As no such profiling had been previously performed, we could not assume much about the variance in the population a priori. Participants were therefore required to lack any known hematological condition, including hematological malignancy or premalignant state, or any prior evidence of blood clonality. An Illumina-sequenced subset of these 148 individuals (*n* = 79) was used for constructing the healthy reference model used in Fig. ('Fig. reference model'), filtering out individuals with any blood count abnormality (up to 5 years before sampling) and putting aside 41 healthy samples for classifier training.

Recruitment of the cytopenic cohort (including patients with MDS and non-MDS-related cytopenia, analyzed in Fig. and Extended Data Figs. 7–10) took place between November 2021 and February 2024.


## 讨论与结论

The present study characterizes interindividual heterogeneity in cHSPCs across 148 healthy individuals using scRNA-seq analysis of PB CD34+ cells. The magnitude of our cohort, along with the potency and resolution of modern single-cell technologies and the computational methods used in the present study, allowed us to characterize in detail the transcriptional programs of diverse, sometimes rare (NKTDP and BEMP), HSPC subpopulations, refining and augmenting previous findings from smaller cohorts (Fig. ). We defined a normal reference range for cHSPC subpopulation frequencies within an age- and sex-diverse healthy population and showed that cHSPC subtype compositions were highly variable between individuals, whereas the cell states themselves were remarkably general (Fig. [2\)](#page-3-0). These compositions remained stable over a 1-year follow-up period. Future studies will need to further explore and better define the mechanistic and genetic basis for this compositional heterogeneity. With current sample size, we showed that the known age-related myeloid bias in HSPCs is predominantly male driven and that composition-controlled RNA expression can be used to infer chronological age (Fig. ).

Our data show that cHSPCs are transcriptionally similar to their BM counterparts (Extended Data Figs. 2 and 3), except for reduced cell-cycle gene expression. Although not a complete model for BM hematopoiesis, cHSPCs serve as a highly accessible proxy for key hematological processes. Interindividual differences in cHSPC compositions and states can thus serve as a tool for capturing key aspects of a patient's hematopoietic state. The relevance and importance of a cHSPC normal reference (Fig. [2b\)](#page-3-0) can perhaps be better understood in view of the normal CBC reference range, developed in the 1930s . The development of a population-wide CBC reference enabled the identification of numerous pathological blood states that characterize distinct clinical entities.


## 关键词

circulating, model, reference

## 相关实体

细胞类型: MDS
通路: self-renewal
方法: scRNA-seq, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
