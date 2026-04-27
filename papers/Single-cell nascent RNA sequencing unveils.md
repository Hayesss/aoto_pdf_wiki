---
marker_extracted: true
title: "Single-cell nascent RNA sequencing unveils"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/single-cell-nascent-rna-sequencing-unveils.md]
confidence: medium
year: 2023
---

# Single-cell nascent RNA sequencing unveils

> 原文: [[single-cell-nascent-rna-sequencing-unveils]]

## 摘要

Article Single-cell nascent RNA sequencing unveils coordinated global transcription Dig B. Mahat1, Nathaniel D. Tippens1, Jorge D. Martin-Rufino2, Sean K. Waterton1,3, Jiayu Fu1,4, Sarah E. Blatt1,5 & Phillip A. Sharp1 ✉ Received: 15 September 2023 Accepted: 3 May 2024 Transcription is the primary regulatory step in gene expression. Divergent Published online: xx xx xxxx transcription initiation from promoters and enhancers produces stable RNAs from Open access genes and unstable RNAs from enhancers1,2. Nascent RNA capture and sequencing Check for updates assays simultaneously measure gene and enhancer activity in cell populations3. However, fundamental questions about the temporal regulation of transcription and enhancer–gene coordination remain unanswered, primarily because of the absence of a single-cell perspective on active transcription.

## 背景与目的

Building on this foundation, we applied our newly developed chem- enabling the detection of transcribing RNA polymerases genome-wide istry to single cells (Fig. 1a). For congruence with the original nascent at single-nucleotide resolution (Fig. 2a). RNA sequencing method of GRO–seq, we named this single-cell version With this new approach, we examined the evidence of bursting scGRO–seq. Intact nuclei containing nascent RNA labelled with prop- de novo without previous assumptions by quantifying the incidence argyl, following a nuclear run-on reaction with 3′-(O-propargyl)-NTPs, of transcribing RNA polymerases. If transcription occurs in bursts, we 2 | Nature | www.nature.

## 主要发现

RNA polymerases per burst, whereas burst frequency was calculated was even stronger for genes with a higher burst frequency (Extended as the number of bursts per allele per unit of time required for RNA Data Fig. 8d). However, we observed a poor correlation between burst polymerase to traverse through the burst window (Fig. 2d), corrected frequencies from scGRO–seq and scRNA–seq data, as well as between for capture efficiency (Methods). We considered genes longer than 11 kb intron seqFISH and scRNA-seq data (Extended Data Fig. 8e). This find- (n = 13,564) and excluded 500 bp regions at either end that are known ing highlights potential limitations in kinetic estimates derived from to harbour paused polymerases21, thereby using the remaining 10 kb as mature transcripts. In contrast to a previous report18, we did not find the burst window. We assigned reads to a single allele based on previous an impact of gene length on kinetic estimates (Extended Data Fig. 8f). evidence showing that alleles in mouse ES cells burst independently to We further confirmed that the burst frequencies calculated from 10 kb generate monoallelic RNA22.

## 方法概述

#### **scGRO–seq conceptualization**

Capturing nascent RNA with sufficient efficiency from single cells for meaningful analysis was deemed challenging. However, recognizing the potential insights into transcription mechanisms that single-cell nascent RNA sequencing could offer, we set out to develop a single-cell version of the GRO–seq method a decade after its use in cell populations. Our efforts were met with two significant challenges: selectively capturing a small fraction of nascent RNA among various RNA species within a cell and accurately distinguishing nascent RNAs from individual cells.

The primary limitation we encountered was capture efficiency. The quantity of nascent RNA from transcribing RNA polymerases in an individual cell, mainly due to the intermittent nature of transcription with short bursts and long latency periods, is significantly lower than the mRNA copies that accumulate over time. Traditional nascent RNA capture methods yield only a meagre number of nascent RNAs from single cells. Miniaturizing GRO–seq using strategies derived from scRNA-seq was not feasible because nascent RNA lacks the consensus polyadenylation sequence used in RNA-seq. Instead, GRO–seq and related methods selectively label nascent RNA in bulk cells using modified nucleotides and use single-stranded RNA–RNA ligation with PCR handles on both ends. This ligation process proved unsuitable for scGRO–seq owing to its low efficiency and the need for nascent RNA purification before ligation, which risks depleting the already scarce nascent RNA from single cells.

To overcome these challenges, we devised a strategy that involved labelling nascent RNA in cells and attaching single-cell barcodes to the labelled nascent RNA without requiring purification from other cellular RNA. After exploring several approaches without success, we turned to click chemistry, specifically CuAAC. We speculated that by sourcing or synthesizing CuAAC-compatible chain-terminating nucleotide triphospha


## 讨论与结论

We developed scGRO–seq to enable the assessment of co-transcription and prediction of enhancer–gene regulatory networks in their native context. By reporting the activity of genes and distal regulatory elements—and therefore the functional consequences of transcriptional signals and networks—scGRO–seq is inherently multimodal for understanding transcription regulation in high detail. We illustrated these advantages by determining burst size and frequency for expressed genes, transcription dynamics during cell cycle phases and genome-wide gene–gene and enhancer–gene co-transcription detection. We restricted this study to mouse ES cells for comparison with large available datasets for validation.

The current scGRO–seq methodology has its limitations. The preservation of nuclear integrity, achieved through a low sarkosyl concentration, failed to promote the run-on of RNA polymerases in the pause complex, thereby limiting the detection of promoter–proximal paused polymerases. The read depth and cell numbers limited our analyses of burst kinetics and co-transcription of gene–gene and enhancer– gene pairs. Improved efficiency in future iterations will facilitate more precise evaluation of these phenomena.

scGRO–seq is also limited by the abundance of nascent RNA per cell at any given time, which is considerably lower than that of mature mRNA. Nascent RNA detection requires technology that does not depend on a polyadenylated terminus, which initially raised doubts about the feasibility of nascent RNA sequencing in single cell[s48](#page-7-41). However, implementing highly efficient CuAAC has overcome this limitation, enabling the capture of approximately 10% of nascent RNA with the current single-cell protocol. To streamline the process and to ensure compatibility with future automation, we optimized the biochemical steps by replacing multiple rounds of nascent RNA purification and nucleic acid ligation with click chemistry. Further adaptations, including high-throughput


## 关键词

RNA, Single-cell, nascent, sequencing, unveils

## 相关实体

方法: Single-cell, scRNA, scRNA-seq, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
