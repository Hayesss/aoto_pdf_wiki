---
marker_extracted: true
title: "Conesaetal.GenomeBiology (2016) 17:13 DOI10.1186/s13059-016-0881-8 REVIEW Open Access A survey of best practices for RNA-seq data"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/conesaetalgenomebiology-2016-1713-doi101186s13059-016-0881-8-review-open-access.md]
confidence: medium
year: 2016
---

# Conesaetal.GenomeBiology (2016) 17:13 DOI10.1186/s13059-016-0881-8 REVIEW Open Access A survey of best practices for RNA-seq data

> 原文: [[conesaetalgenomebiology-2016-1713-doi101186s13059-016-0881-8-review-open-access]]

## 摘要

RNA-sequencing (RNA-seq) has a wide variety of applications, but no single analysis pipeline can be used in all cases. We review all of the major steps in RNA-seq data analysis, including experimental design, quality control, read alignment, quantification of gene and transcript levels, visualization, differential gene expression, alternative splicing, functional analysis, gene fusion detection and eQTL mapping. We highlight the challenges associated with each step. We discuss the analysis of small RNAs and the integration of RNA-seq with other functional genomics techniques. Finally, we discuss the outlook for novel technologies that are changing the state of the art in transcriptomics.


## 背景与目的

their differential regulation. Furthermore, investigators Transcript identification and the quantification of gene might be interested only in messenger RNA isoform ex- expression have been distinct coreactivities inmolecular pression or microRNA (miRNA) levels or allele variant biology ever since the discovery of RNA’s role as the key identification. Boththe experimentaldesign andtheana- intermediate between the genome and the proteome. lysis procedures will vary greatly in each of these cases. The power of sequencing RNA lies in the fact that the RNA-seq can be used solo for transcriptome profiling or twin aspectsofdiscovery andquantification can be com- in combination with other functional genomics methods bined in a single high-throughput sequencing assay to enhance the analysis of gene expression. Finally, RNA- called RNA-sequencing (RNA-seq). The pervasive adop- seq can be coupled with different types of biochemical tion of RNA-seq has spread well beyond the genomics assaytoanalyzemanyotheraspectsofRNAbiology,such communityandhasbecomea standardpartofthetoolkit as RNA–protein binding, RNA structure, or RNA–RNA usedbythelifesciencesresearchcommunity.Manyvaria- interactions. These applications are, however, beyond the tions of RNA-seq protocols and analyses have been scopeofthisreviewaswefocuson‘typical’RNA-seq. Every RNA-seq experimental scenario could poten- tially have different optimal methods for transcript

## 主要发现

DNA. For example, we expect between 70 and 90 % of madebyVanDijketal.[199],suchastheuseofadapterswith regular RNA-seq reads to map onto the human genome randomnucleotidesattheextremitiesortheuseofchemical-based (depending on the read mapper used) [15], with a sig- fragmentationinsteadofRNaseIII-basedfragmentation.Ifthe nificant fraction of reads mapping to a limited number RNA-seqexperimentislargeandsampleshavetobeprocessedin of identical regions equally well (‘multi-mapping reads’). differentbatchesand/orIlluminaruns,cautionshouldbetakento When reads are mapped against the transcriptome, we randomizesamplesacrosslibrarypreparationbatchesandlanesso expect slightly lower total mapping percentages because astoavoidtechnicalfactorsbecomingconfoundedwith reads coming from unannotated transcripts will be lost, experimentalfactors.Anotheroption,whensamplesareindividually and significantly more multi-mapping reads because of reads falling onto exons that are shared by different barcodedandmultipleIlluminalanesareneededtoachievethe transcript isoformsofthesamegene.

## 方法概述

Gene Set Variation Analysis (GSVA) [107] or SeqGSEA typical eQTL experiment, genotype and transcriptome [108] packages also combine splicing and implement en- profiles are obtained from the same tissue type across a richmentanalyses similar toGSEA. relatively large number of individuals (>50) and correla- Functional analysis requires the availability of suffi- tions between genotype and expression levels are then cient functional annotation data for the transcriptome detected. These associations can unravel the genetic under study. Resources such as Gene Ontology [109], basis of complex traits such as height [121], disease sus- Bioconductor [110], DAVID [111, 112] or Babelomics ceptibility [122] or even features of genome architecture [113] contain annotation data for most model species.

## 讨论与结论

proteomics integration, the PG Nexus pipeline [172] con- successfully reverse-transcribed to cDNA [8, 176]; but verts mass spectrometry data to mappings that are co- deeper sequencing is potentially useful for discovering visualizedwithRNA-seqalignments. and measuring allele-specific expression, as additional reads couldprovideusefulevidence. Outlook Single-cell transcriptomes typically include about RNA-seqhasbecomethestandardmethodfortranscrip- 3000–8000 expressed genes, which is far fewer than are tome analysis, but the technology and tools are continu- counted in the transcriptomes of the corresponding ing to evolve. It should be noted that the agreement pooled populations.

## 关键词

Access, Conesaetal, DOI10, GenomeBiology, Open, REVIEW, RNA-seq, best, data, practices, s13059-016-0881-8, survey

## 相关实体

细胞类型: all
方法: RNA-seq

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
