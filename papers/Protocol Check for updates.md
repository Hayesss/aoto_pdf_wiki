---
marker_extracted: true
title: "Protocol Check for updates"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/protocol-check-for-updates.md]
confidence: medium
year: 2024
---

# Protocol Check for updates

> 原文: [[protocol-check-for-updates]]

## 摘要

Pre-mRNA alternative splicing is a prevalent mechanism for diversifying eukaryotic transcriptomes and proteomes. Regulated alternative splicing plays a role in many biological processes, and dysregulated alternative splicing is a feature of many human diseases. Short-read RNA sequencing (RNA-seq) is now the standard approach for transcriptome-wide analysis of alternative splicing. Since 2011, our laboratory has developed and maintained Replicate Multivariate Analysis of Transcript Splicing (rMATS), a computational tool for discovering and quantifying alternative splicing events from RNA-seq data. Here we provide a protocol for the contemporary version of rMATS, rMATS-turbo, a fast and scalable re-implementation that maintains the statistical framework and user interface of the original rMATS software, while incorporating a revamped computational workflow with a substantial improvement in speed and data storage efficiency. The rMATS-turbo software scales up to massive RNA-seq datasets with tens of thousands of samples. To illustrate the utility of rMATS-turbo, we describe two representative application scenarios. First, we describe a broadly applicable two-group comparison to identify differential alternative splicing events between two sample groups, including both annotated and novel alternative splicing events. Second, we describe a quantitative analysis of alternative splicing in a large-scale RNA-seq dataset (~1,000 samples), including the discovery of alternative splicing events associated with distinct cell states. We detail the workflow and features of rMATS-turbo that enable efficient parallel processing and analysis of large-scale RNA-seq datasets on a compute cluster. We anticipate that this protocol will help the broad user base of rMATS-turbo make the best use of this software for studying alternative splicing in diverse biological systems.



## 背景与目的

Alternative splicing is a prevalent RNA regulatory mechanism for diversifying the transcriptomic and proteomic output of eukaryotic cells[1](#page-20-0) . During the splicing of precursor mRNA, introns are removed and exons are joined together to generate mature mRNA produc[t2](#page-20-1) . Alternative choices of exons and splice sites during pre-mRNA splicing (i.e., alternative splicing) can therefore generate multiple mRNA isoforms from a single gene. Alternative splicing is controlled by *cis*-acting splicing regulatory elements within the pre-mRNA and *trans*-acting splicing factors that interact with these *cis* element[s3](#page-20-2),[4](#page-20-3) . Regulated alternative splicing plays a role in many biological processes, such as cell differentiation and tissue developmen[t5](#page-20-4)[,6](#page-20-5) . Dysregulated alternative splicing is a feature of many human diseases and frequently contributes to disease pathogenesis and progression[7](#page-20-6) .

RNA sequencing (RNA-seq) on massively parallel sequencers is now the standard approach for transcriptome analysis[8](#page-20-7) . Contemporary short-read sequencers are capable of generating tens to hundreds of millions of RNA-seq reads at a modest cost, allowing transcriptome-wide discovery and quantification of alternative splicing events on any RNA sampl[e9](#page-20-8) . Three classic papers in 2008 demonstrated the utility of RNA-seq for alternative splicing analysis[10–](#page-20-9)[12](#page-20-10). In the past decade, various computational tools have been developed for analyzing alternative splicing using RNA-seq data (summarized in refs. [9](#page-20-8),[13](#page-20-11),[14\)](#page-20-12). Although early RNA-seq studies of alternative splicing were limited to a small number of conditions and samples, it is now routine for a single RNA-seq study to examine tens to hundreds of sample[s15](#page-20-13). Large-scale genomics projects, such as The Cancer Genome Atlas (TCGA) program and the Genoty


## 主要发现

Alternative splicing detection and quantification Skipped exon Alternative 5′ splice sites Alternative 3′ splice sites Mutually exclusive exons Retained intron Protocol Box 1 Description of command line arguments of rMATS-turbo -h, --help Show this help message and exit --version Show program’s version number and exit --gtf GTF An annotation of genes and transcripts in GTF format --b1 B1 A text file containing a comma separated list of the BAM files for sample_1. (Only if using BAM) --b2 B2 A text file containing a comma separated list of the BAM files for sample_2. (Only if using BAM) --s1 S1 A text file containing a comma separated list of the FASTQ files for sample_1. If using paired reads the format is “:” to separate pairs and “,” to separate replicates. (Only if using fastq) --s2 S2 A text file containing a comma separated list of the FASTQ files for sample_2. If using paired reads the format is “:” to separate pairs and “,” to separate replicates. (Only if using fastq) --od OD The directory for final output from the post step --tmp TMP The directory for intermediate output such as “.

## 方法概述

between PC3E and GS689 cell lines ▲ CrItICAl Also see Fig. 2. Set up the working directory and input files for rMATS-turbo analysis ● tIMInG ~5 min 1. Set up the working directory where all outputs will be generated. mkdir -p PC3E-GS689/rmats cd PC3E-GS689/rmats 2. Generate configuration files (b1.txt and b2.txt) as input files for rMATS-turbo. These two files contain comma-separated lists of FASTQ or BAM files for sample groups 1 and 2, respectively. ls $prefix_dir_group1 | tr '\n' ',' | sed 's/,$/\n/' > ./b1.txt ls $prefix_dir_group2 | tr '\n' ',' | sed 's/,$/\n/' > ./b2.txt $prefix_dir_group1: folder containing all FASTQ or BAM files for sample group 1. $prefix_dir_group2: folder containing all FASTQ or BAM files for sample group 2.

## 讨论与结论

a c RI 12,909 SE 60,577 MXE 46,844 A3SS 20,428 A5SS 14,298 b RI 1,410 SE 6,061 MXE 3,798 A3SS 1,964 A5SS 977 d e USO1 PC3E PSI = 0.91 MAST3 PC3E PSI = 0.09 498 471 60 GS689 PSI = 0.05 GS689 PSI = 0.41 36 24 448 f Nature Protocols | Volume 19 | April 2024 | 1083–1104 1096 MKPR Delta PSI (GS689 – PC3E) 4 5 49 27 27 39 )RDF( gol– 01 ≥15 Not significant High in GS689 (n = 2,658) High in PC3E (n = 3,403) ssecorp_lacigoloiB tnenopmoc_ralulleC noitcnuf_raluceloM 10 5 0 –1.0 –0.5 0 0.5 1.0 4 3 2 1 4 3 2 1 Exon 12 Exon 13 Exon 14 Exon 4 Exon 5 Cellular protein modification process (GO:0006464) Regulation of apoptotic process (GO:0042981) Regulation of transcription from RNA polymerase II promoter (GO:0006357) Cellular protein metabolic process (GO:0044267) Organelle assembly (GO:0070925) Cytoskelet...

## 关键词

Check, Protocol, updates

## 相关实体

方法: RNA-seq

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
