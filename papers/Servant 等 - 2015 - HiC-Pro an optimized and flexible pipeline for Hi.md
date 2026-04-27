---
title: "Servant 等 - 2015 - HiC-Pro an optimized and flexible pipeline for Hi"
created: 2025-04-22
updated: 2025-04-22
type: paper
tags: ["hic"]
sources: ["raw/papers/servant-等-2015-hic-pro-an-optimized-and-flexib.md"]
confidence: medium
marker_extracted: true
---

# Servant 等 - 2015 - HiC-Pro an optimized and flexible pipeline for Hi

> Zotero Item Key: 3N8YBT74
> 原文: [[servant-等-2015-hic-pro-an-optimized-and-flexib]]

## 摘要

HiC-Pro is an optimized and flexible pipeline for processing Hi-C data from raw reads to normalized contact maps. HiC-Pro maps reads, detects valid ligation products, performs quality controls and generates intra- and inter-chromosomal contact maps. It includes a fast implementation of the iterative correction method and is based on a memory-efficient data format for Hi-C contact maps. In addition, HiC-Pro can use phased genotype data to build allele-specific contact maps. We applied HiC-Pro to different Hi-C datasets, demonstrating its ability to easily process large data in a reasonable time. Source code and documentation are available at http://github.com/nservant/HiC-Pro.

**Keywords:** Chromosome conformation, Hi-C, Bioinformatics pipeline, Normalization

## 背景与目的

High-throughput chromosome conformation capture methods are now widely used to map chromatin interactions within regions of interest and across the genome. The use of Hi-C has notably changed our vision of genome organization and its impact on chromatin and gene regulation [1, 2]. The Hi-C technique involves sequencing pairs of interacting DNA fragments, where each mate is associated with one interacting locus. Briefly, cells are crossed-linked, DNA is fragmented using a restriction enzyme [3] or a nuclease [4], and interacting fragments are ligated together. After paired-end sequencing, each pair of reads can be associated to one DNA interaction.

In recent years, the Hi-C technique has demonstrated that the genome is partitioned into domains of different scale and compaction level. The first Hi-C application has described that the genome is partitioned into distinct compartments of open and closed chromatin [3]. Higher throughput and resolution have then suggested the presence of megabase-long and evolutionarily conserved smaller domains. These topologically associating domains are characterized by a high frequency of intra-domain chromatin interactions but infrequent inter-domain chromatin

interactions [5, 6]. More recently, very large data sets with deeper sequencing have been used to increase the Hi-C resolution in order to detect loops across the entire genome [7, 8].

As with any genome-wide sequencing data, Hi-C usually requires several millions to billions of paired-end sequencing reads, depending on genome size and on the desired resolution. Managing these data thus requires optimized bioinformatics workflows able to extract the contact frequencies in reasonable computational time and with reasonable resource and storage requirements. The overall strategy to process Hi-C data is converging among recent studies [9], but there remains a lack of stable, flexible and efficient bioinformatics workflows to process such data. Solutions such as the HOMER [10], HICUP [11], HiC-inspector [12], HiCdat [13] and HiCbox [14] pipelines are already available for Hi-C data processing. HOMER offers several functions to analyze Hi-C data but does not perform the mapping of reads nor the correction of systematic biases. HiCdat, HiCinspector and HiCbox do not allow chimeric reads to be rescued during the mapping of reads. HICUP provides a complete pipeline until the detection of valid interaction products. Using HICUP together with the SNPsplit program [15] allows the extraction of allele-specific interaction products whereas all other solutions do not allow allele-specific analysis. The HiCdat and HiCbox packages offer a means of correcting contact maps for systematic

<sup>2</sup>INSERM, U900, Paris, France

Full list of author information is available at the end of the article

<sup>\*</sup> Correspondence: nicolas.servant@curie.fr <sup>1</sup>Institut Curie, Paris, France

biases. Finally, none of these software were designed to process very large amounts of data in a parallel mode. The hiclib package is currently the most commonly used solution for Hi-C data processing. However, hiclib is a Python library that requires programming skills, such as knowledge of Python and advanced Linux command line, and cannot be used in a single command-line manner. In addition, parallelization is not straightforward and it has limitations with regard to the analysis and normalization of very high-resolution data (Table 1).

Here, we present HiC-Pro, an easy-to-use and complete pipeline to process Hi-C data from raw sequencing reads to normalized contact maps. HiC-Pro allows the processing of data from Hi-C protocols based on restriction enzyme or nuclease digestion such as DNase Hi-C [\[4](#page-10-0)] or Micro-C [\[16\]](#page-10-0). When phased genotypes are available, HiC-Pro is able to distinguish allele-specific interactions and to build both maternal and paternal contact maps. It is optimized and offers a parallel mode for very high-resolution data as well as a fast implementation of the iterative correction method [\[17\]](#page-10-0).

## 主要发现

# HiC-Pro results and performance

We processed Hi-C data from two public datasets: IMR90 human cell lines from Dixon et al. [[6\]](#page-10-0) (IMR90) and from Rao et al. [\[7](#page-10-0)] (IMR90\_CCL186). The latter is currently one of the biggest datasets available, used to generate up to 5-kb contact maps. For each dataset, we ran HiC-Pro and generated normalized contact maps at 20 kb, 40 kb, 150 kb, 500 kb and 1 Mb resolution. Normalized contact maps at 5 kb were only generated for the IMR90\_CCL186 dataset. The datasets were either used in their original form or split into chunks containing 10 or 20 million read pairs.

Using HiC-Pro, the processing of the Dixon's dataset (397.2 million read pairs split into 84 read chunks) was completed in 2 hours using 168 CPUs (Table [2\)](#page-2-0). Each chunk was mapped on the human genome using four CPUs (two for each mate) and 7 GB of RAM Processing the 84 chunks in parallel allows extraction of the list of valid interactions in less than 30 minutes. All chunks were then merged to generate and normalize the genome-wide contact map.

In order to compare our results with the hiclib library, we ran HiC-Pro on the same dataset, and without initial read splitting, using eight CPUs. HiC-Pro performed the complete analysis in less than 15 hours compared with 28 hours for the hiclib pipeline. The main difference in speed is explained by our two-step mapping strategy compared with the iterative mapping strategy of hiclib, which aligned the 35 base pair (bp) reads in four steps. Optimization of the binning process and implementation of the normalization algorithm led to a three-fold decrease in time to generate and normalize the genomewide contact map.

The IMR90 sample from the Rao dataset (1.5 billion read pairs split into 160 read chunks) was processed in parallel using 320 CPUs to generate up to 5-kb contact maps in 12 hours, demonstrating the ability of HiC-Pro to analyze very large amounts of data in a reasonable time. At a 5-kb resolution, we observe the presence of chromatin loops as described by Rao et al. [\[7](#page-10-0)] (Figure S1 in Additional file [1\)](#page-9-0). The merged list of valid interactions was generated in less than 7.5 hours. Normalization of the genome-wide contact map at 1 Mb, 500 kb, 150 kb, 40 kb, 20 kb and 5 kb was performed in less than 4 hours. Details about the results and the implementation of the different solutions are available in Additional file [1.](#page-9-0)

Finally, we compared the Hi-C processing results of hiclib and HiC-Pro on the IMR90 dataset. Although the processing and filtering steps of the two pipelines are not exactly the same, we observed a good concordance in the results (Fig. [1](#page-4-0)). Using default parameters, HiC-Pro is less stringent than hiclib and used more valid interactions to

Table 1 Comparing solutions for Hi-C data processing

|               | Mapping | Detection of valid interactions | Binning | Correction of systematic noise | Parallel implementation | Allele-specific analysis |
|---------------|---------|---------------------------------|---------|--------------------------------|-------------------------|--------------------------|
| HOMER         |         | x                               | x       |                                |                         |                          |
| HICUP         | x       | x                               |         |                                |                         | x                        |
| HiC-inspector | xa      | x                               | x       |                                |                         |                          |
| HiC-Box       | xa      | x                               | x       | x                              |                         |                          |
| HiCdat        | xa      | x                               | x       | x                              |                         |                          |
| Hiclib        | x       | x                               | x       | x                              |                         |                          |
| HiC-Pro       | x       | x                               | x       | x                              | x                       | x                        |

HOMER [[10](#page-10-0)] offers several programs to analysis Hi-C data from aligned reads. <sup>a</sup> HiC-inpector [\[12](#page-10-0)], HiCdat [[13\]](#page-10-0) and HiC-Box [\[14](#page-10-0)] do not allow chimeric reads to be rescued during the mapping. HICUP [\[11\]](#page-10-0) provides a complete pipeline until the detection of valid interaction products. It can be used together with the SNPsplit software [[15](#page-10-0)] to extract allele-specific mapped reads. The hiclib Python library [[17\]](#page-10-0) can be applied for all analysis steps but requires good programming skills and cannot be used in a single command-line manner. None of these software enable very large amounts of data to be processed easily in a parallel mode. Note that HOMER, hiclib and HiCdat also offer additional functions for downstream analysis. In the case of HiC-Pro, the downstream analysis is supported by the HiTC BioConductor package [\[28\]](#page-10-0)

<span id="page-2-0"></span>Table 2 HiC-Pro performance and comparison with hiclib

| Dataset                | IMR90       | IMR90       | IMR90            | IMR90_CCL186     |
|------------------------|-------------|-------------|------------------|------------------|
| Number of reads        | 397,200,000 | 397,200,000 | 397,200,000      | 1,535,222,082    |
| Pipeline               | hiclib      | HiC-Pro     | HiC-Pro parallel | HiC-Pro parallel |
| Number of input files  | 10          | 10          | 84               | 160              |
| Number of jobs         | 1           | 1           | 42               | 80               |
| Number of CPUs per job | 8           | 8           | 4                | 4                |
| Maximum memory         | 10          | 7           | 7                | 24               |
| Wall time              | 28:24       | 14:32       | 02:15            | 11:49            |
| Mapping                | 22:03       | 10:31       | 00:21            | 05:56            |
| Filtering              | 00:30       | 03:10       | 00:05            | 00:36            |
| Merge                  |             | 00:20       | 00:18            | 00:50            |
| Contacts maps          | 01:45       | 00:15       | 00:15            | 00:42            |
| Normalization          | 04:06       | 01:16       | 01:16            | 03:49            |

HiC-Pro was run on the IMR90 Hi-C dataset from Dixon et al. and Rao et al. in order to generate contact maps at resolutions of 20 kb, 40 kb, 150 kb, 500 kb and 1 Mb. Contact maps at 5 kb were also generated for the IMR90\_CCL186 dataset. The CPU time for each step of the pipeline is reported and compared with the hiclib Python library. The reported results include time of writing contact maps in text format. Times are minutes:seconds

build the contact maps. The two sets of normalized contact maps generated at different resolutions are highly similar (Fig. [1c](#page-4-0)). We further explored the similarity between the maps generated by the two pipelines by computing the Spearman correlation of the normalized intra-chromosomal maps. The average correlation coefficient across all chromosomes at different resolutions was 0.83 (0.65–0.95). Finally, since the inter-chromosomal data are usually very sparse, we summarized the interchromosomal signal using two one-dimensional coverage vectors of rows and columns [\[18, 19\]](#page-10-0). The average Spearman correlation coefficient of all coverage vectors between hiclib and HiC-Pro inter-chromosomal contact maps was 0.75 (0.46–0.98).

## 方法概述

# HiC-Pro workflow

HiC-Pro is organized into four distinct modules following the main steps of Hi-C data analysis: (i) read alignment, (ii) detection and filtering of valid interaction products, (iii) binning and (iv) contact map normalization (Fig. [3\)](#page-6-0).

## 讨论与结论

（待补充）

## 关键词

HiC-Pro, Servant, flexible, optimized, pipeline

## 相关实体

暂无识别到特定实体

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
