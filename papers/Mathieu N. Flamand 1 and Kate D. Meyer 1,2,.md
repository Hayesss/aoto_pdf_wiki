---
marker_extracted: true
title: "Mathieu N. Flamand 1 and Kate D. Meyer 1,2,*"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/mathieu-n-flamand-1-and-kate-d-meyer-12.md]
confidence: medium
year: 2022
---

# Mathieu N. Flamand 1 and Kate D. Meyer 1,2,*

> 原文: [[mathieu-n-flamand-1-and-kate-d-meyer-12]]

## 摘要

The transport of mRNAs to distal subcellular compartments is an important component of spatial gene expression control in neurons. However, the mechanisms that control mRNA localization in neurons are not completely understood. Here, we identify the abundant base modification, mA, as a novel regulator of this process. Transcriptome-wide analysis following genetic loss of mA reveals hundreds of transcripts that exhibit altered subcellular localization in hippocampal neurons. Additionally, using a reporter system, we show that mutation of specific mA sites in select neuronal transcripts diminishes their localization to neurites. Single molecule fluorescent in situ hybridization experiments further confirm our findings and identify the mA reader proteins YTHDF2 and YTHDF3 as mediators of this effect. Our findings reveal a novel function for mA in controlling mRNA localization in neurons and enable a better understanding of the mechanisms through which mA influences gene expression in the brain.


## 背景与目的

Subcellular RNA localization is an important mechanism of spatial gene expression control in cells. This is especially true in neurons, in which thousands of mRNAs can be localized to distal compartments such as axons and dendrites, where they can in turn undergo local translation to produce proteins critical for axon outgrowth and synaptic plasticity, respectively (1-3). The subcellular trafficking of neuronal transcripts to these distal locations plays important roles in neurodevelopment and synaptic remodeling. However, the mechanisms that govern which mRNAs are destined for subcellular transport are poorly understood. Several RNA binding proteins (RBPs) have been shown to facilitate mRNA transport through their recognition of specific cis-acting sequence and structural elements, usually those in 3'UTRs (3–5). However, there is no universal localization element shared by all distally-localized transcripts, and there are likely to be other mechanisms beyond sequence and structure that confer localization information.

In addition to RNA sequence motifs and structural elements, RNA base modifications provide a mechanism for controlling RNA: protein interactions in cells. $N^6$ methyladenosine (mA) is the most abundant internal mRNA modification, and its levels are particularly high within the brain (6,7). Furthermore, recent studies have revealed important roles for mA in neurodevelopment and learning and memory (8–11), two processes which require precise spatial control of RNA expression (3). mA controls nearly every stage of the mRNA life cycle, and these various functional roles of mA are carried out by mA-dependent regulation of RNA:protein interactions (12,13). In particular, direct recognition of mA residues by YTH domaincontaining proteins is a major mechanism through which mA regulates mRNA fate.


## 主要发现

# **Identification of the local transcriptome of hippocampal neurons**

To identify RNAs that localize to axons and dendrites, we cultured mouse hippocampal neurons on a microporous membrane, which enables physical separation of dendrites and axons from the cell body (soma) \(52–54\) (Figure 1A). This method results in a clear separation of the two compartments, as shown by the presence of nuclear proteins exclusively in the soma fraction and synaptic proteins in both fractions (Figure 1B). We extracted RNA from the soma and neurites of mature (DIV 15) neurons and used RNAseq to identify RNAs from each compartment. To identify transcripts enriched in neurites relative to the cell body, we used differential gene expression analysis \(39\) to establish an enrichment ratio which calculates the fold change in RNA abundance in the neurite and soma fractions (FCN/S). We identified 2420 RNAs that were significantly enriched in neurites relative to cell bodies, and 657 RNAs that were enriched in cell bodies relative to neurites (Figure 1C; Supplementary Table S1). RNAs that have previously been shown to localize to dendrites \(55\), such as *Camk2a and Shank1*, were among the most enriched transcripts in neurites (Figure 1C and D; Supplementary Table S1). In contrast, RNAs that primarily localized to the nucleus, such as the small nucleolar RNA host gene *Snhg11*, were found almost exclusively in the soma fraction (Figure 1D; Supplementary Table S1). In addition, we observed a high degree of overlap between transcripts detected in hippocampal neurite samples and those found in the neurites of Ascl1-induced neurons \(54\), cortical neurons \(53\) and mouse hippocampal neuropil samples \(56\), indicating the accuracy of our approach (Supplementary Figure S1A).

The majority of transcripts that we identified as enriched in neurites were protein-coding genes (64.1%) (Supplementary Figure S1B).


## 方法概述

### **Biological resources**

Cell lines. HEK293T cells were obtained from ATCC and maintained at 37°C and 5% CO<sub>2</sub>, using DMEM (Corning) supplemented with 10% fetal bovine serum (VWR) and Pen/Strep (Gibco).

Constructs. 3'UTRs for reporter genes, as well as 5xBoxB and 6xMS2 3'UTRs, were cloned downstream of Dendra2 in the pFUGW lentiviral backbone plasmid containing Dendra2 by Gibson assembly. For the 3'UTR reporter assays, we identified mA sites within the 3'UTR by examining antibody-based mA mapping data from neuron and brain samples (6,22,24,25), either by selecting single nucleotide mapped sites or by finding consensus DRACH sequences found within MeRIP-seq peaks. Mutations of mA sites were introduced by either PCR mutagenesis or cloning of gene fragments (IDT) and assembled using Gibson assembly. Cloning of shRNAs was done by ligating annealed oligonucleotides (IDT) into a modified pLKO.1-TRC lentiviral backbone where the puromycin was swapped for a CFP using Gibson assembly. Coding sequences from YTHDF proteins were amplified from a mouse hippocampal cDNA library and cloned into the pFUGW backbone followed by the XTEN linker sequence (26) and $\lambda$ N-HA. A complete list of the oligonucleotides used for cloning can be found in Supplementary Table S7. psPAX2 and pMD2.g were a gift from Didier Trono (Addgene plasmid # 12260 and # 12259). pLKO.1-TRC cloning vector was a gift from David Root (Addgene plasmid # 10878) (27). pET42a-lambdaN+-L+-GSH was a gift from Pascale Legault (Addgene plasmid # 98894) (28). pUbC-nls-hastdMCP-stdGFP was a gift from Robert Singer (Addgene plasmid # 98916) (29). pAAV-hSyn-Cre-P2A-dTomato was a gift from Rylan Larsen (Addgene plasmid # 107738). pUCmini-iCAP-PHP.eB was a gift from Viviana Gradinaru (Addgene plasmid # 103005) (30). pAdDeltaF6 was a gift from James M. Wilson (Addgene plasmid # 112867).

Virus production. Lentiviral vectors were co-transfected with psPAX2 and pMD2.


## 讨论与结论

Neurons possess a complex architecture which often includes an elaborate dendritic tree and a long axon that can extend hundreds of microns from the cell body. The sensing and processing of signaling events at these distal locations requires rapid responses to ensure the maintenance and strengthening of synaptic connections. Such responses are mediated by a host of intricate regulatory mechanisms which collectively enable the local translation of mRNAs residing in remote locations such as synapses and the growth cone. A critical component of this complex regulatory process is the transport of select mRNAs to distal neuronal compartments. Several sequence motifs and structural elements within mRNAs have been implicated in mRNA localization, but the full complement of *cis*-acting elements that control this process is far from being elucidated. Here, we identify adenosine methylation as an additional layer of regulation which influences the subcellular localization of neuronal mRNAs. Our studies uncover hundreds of neuronal transcripts whose targeting to neurites is altered following knockout of the mA methyltransferase METTL3, and we provide the first direct demonstration that mA residues within the 3'UTR promote the neuritic localization of a subset of neuronal transcripts.

mA provides a versatile mechanism for regulating the subcellular localization of a transcript of interest within the cell. Since most, if not all, mRNAs contain the core mA consensus (RAC) within their sequence, virtually any mRNA is susceptible to mA methylation. Furthermore,

Figure 7. YTHDF proteins bind overlapping and distinct RNAs in neurons. (A) Euler diagrams showing overlap of enriched RNAs in YTHDF1, YTHDF2 or YTHDF3 RIP-seq libraries with DART-seq and MeRIP-seq (6) datasets. (B) Cumulative distribution plots of the enrichment in YTHDF RIP over input for transcripts with 0, 1–3, 4–7 or >8 MeRIP-seq peaks.


## 关键词

Flamand, Kate, Mathieu, Meyer

## 相关实体

暂无识别到特定实体

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
