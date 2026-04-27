---
marker_extracted: true
title: "Pan-cancer analysis of mRNA stability for decoding"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/pan-cancer-analysis-of-mrna-stability-for-decoding.md]
confidence: medium
year: 2022
---

# Pan-cancer analysis of mRNA stability for decoding

> 原文: [[pan-cancer-analysis-of-mrna-stability-for-decoding]]

## 摘要

ARTICLE OPEN Pan-cancer analysis of mRNA stability for decoding tumour post-transcriptional programs Gabrielle Perron 1,2, Pouria Jandaghi2, Elham Moslemi2, Tamiko Nishimura2, Maryam Rajaee2, ✉ Rached Alkallas 1,2,3, Tianyuan Lu 1,2,4, Yasser Riazalhosseini 1,2 & Hamed S. Najafabadi 1,2 MeasuringmRNA decayin tumours isa prohibitive challenge, limitingourabilitytomapthe post-transcriptional programs of cancer. Here, using a statistical framework to decouple transcriptionalandpost-transcriptionaleffectsinRNA-seqdata,weuncoverthemRNAstability changes that accompany tumour development and progression. Analysis of 7760 samples across 18 cancer typessuggests that mRNA stability changes are ~30% as frequent as tran- scriptional events, highlighting their widespread role in shaping the tumour transcriptome.

## 背景与目的

f 1 0 r = 0.52 r = –0.10 –2 0 +2 0.3 noitalerroc nosraeP )ytilibats derusaem .sv CARffiD( +2 0 –2 0.6 0.9 1.2 Measured differential mRNA stability DiffRAC standard error of mean (TN vs. ES) (average for bins of 50 genes) ytilibats laitnereffid derusaeM i,j j m = (p )b × γ i,j i j i,j i,j i,f(j) 1 0 0 0 0 0 1 1 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 = + × 1 0 0 0 1 0 1 b 0 0 1 0 1 0 b 0 1 1 1 0 0 b 1 1 g 0.01 < FDR ≤ 0.05 FDR ≤ 0.01 DiffRAC statistical significance decilpsnU decilpS 1 2 3 4 1 2 3 4 j elpmaS 1 2 1 2 )j(f noitidnoC ARTICLE COMMUNICATIONSBIOLOGY| log(λint) ii,,j log(λeeexo) ii,,j log( sint ) j log( sexo ) j log( p ) + log( l ) i,1 i log( p ) – log( p ) i,2 i,1 log( p ) – log( p ) i,3 i,1 log( p ) – log( p ) i,4 i,1 log( l ') – log( l ) + log(...

## 主要发现

A generalized linear model for statistical testing of mRNA stability. The spliced and unspliced transcripts of each gene follow a power-law relationship, with deviations from this power-law trend reflecting changes in the degradation rate of the mature mRNA (Supplementary Fig. 1a, b). The power-law exponent reflects the coupling between transcription rate and RNA processing rate-an exponent of 1 indicates no coupling between

transcription and processing rate constants, whereas values smaller than 1 indicate that as transcription increases, processing rate constant decreases, potentially due to saturation of the RNA processing machinery (Supplementary Fig. 1a). To use this power-law relationship for the inference of differential stability, it is essential to correctly model the variability in RNA-seq counts. For this purpose, we developed DiffRAC (https://github.com/csglab/DiffRAC), a framework that converts the unspliced-spliced relationship to a generalized linear model whose parameters can then be inferred from sequencing count data using an appropriate error model of choice (Fig. 1b, c and Supplementary Fig. 1c, d).

We evaluated the performance of DiffRAC for estimating differential mRNA stability using a previously published dataset<sup>18,19</sup>, consisting of RNA-seq data from mouse embryonic stem cells and terminal neurons, along with experimentally measured transcript half-life measurements after transcriptional blockage with actinomycin D, which here we consider as "groundtruth" measurements for benchmarking purposes. We observed an overall Pearson correlation of 0.22 between RNA-seq-based stability estimates from DiffRAC and ground-truth stability measurements (Fig. 1d and Supplementary Data 1a), in line with previous reports on RNA stability estimation using this specific benchmarking dataset<sup>15,17</sup>.


## 方法概述

Joint modelling of intronic and exonic read counts and mRNA stability. Our approach for statistical modeling of intronic and exonic read counts builds on

previous research that connects the abundance of pre-mRNA and mature mRNA to mRNA stability (Supplementary Fig. 1a, b):

$$\log \mathbf{m} = b \times \log \mathbf{p} + \log \varphi + \log \mathbf{y} \tag{1}$$

here, m corresponds to the vector of the mature mRNA abundance for a given gene across different samples, p is the abundance of the pre-mature mRNA, $\gamma$ is the mRNA stability across samples, $\varphi$ is the maximum processing rate of RNA, and b is the bias-term (Supplementary Fig. 1b). Vectors are differentiated from scalars using bold typeface.

We further model the logarithm of mRNA stability as a linear function of a set of sample-level variables:

$$\log v = X \times \beta + \alpha \tag{2}$$

here, X is the $n \times k$ matrix of sample-level variables (for n samples and k variables), $\beta$ is the vector of coefficients that quantify the effect of each variable on the mRNA stability, and $\alpha$ is an intercept (matrices are differentiated from vectors using capital letters). This leads to:

$$\log m = b \times \log p + c + X \times \beta \tag{3}$$

where $c=\log \varphi + \alpha$ . We model the mean of intronic read counts for a given gene across samples as a function of the pre-mRNA abundance for that gene, a gene-level scaling factor that can be interpreted as the effective length, and a sample-specific scaling factor that can be interpreted as library size (Fig. 1b):

$$\boldsymbol{\lambda}^{int} = \boldsymbol{p} \times l \times \boldsymbol{s}^{int} \tag{4}$$

here, int stands for intronic, $\lambda$ represents the mean read count, l is the gene-specific scaling factor, and s is the sample-specific scaling factor.


## 讨论与结论

By quantifying differential mRNA stability patterns across 18 cancer types, our study presents a systematic resource for mining the post-transcriptional landscape of cancer. Importantly, our results uncovered recurrent changes in the stability of >13,000 mRNAs in at least one cancer type, highlighting the widespread

role of post-transcriptional regulation in shaping the cancer transcriptome. We note that this resource also provides an approximation for the relative contribution of transcriptional and post-transcriptional events in shaping cancer transcriptome: on average, 19% of genes that are significantly upregulated at the expression level are detected by DiffRAC as significantly stabilized in tumours,

and 23% of genes with significantly reduced expression are detected as significantly destabilized. In comparison, 66% and 61% of genes whose expression is significantly up- or downregulated are detected as transcriptionally activated or inhibited in tumours, respectively (Supplementary Fig. 11). We note that about 57% of the variability in the number of differentially stabilized genes across cancer types appears to be attributed to sample size, suggesting that our analysis may be underpowered for smaller cancer cohorts (Supplementary Fig. 12). Nonetheless, these results suggest an important role for post-transcriptional changes in shaping the cancer transcriptome, with recurrent changes that are ~30% as frequent as transcriptional events.

Our study also highlights the coordinated post-transcriptional deregulation of genes that are involved in the same pathways. Notably, we observed recurrent stabilization of mRNAs that encode epithelial-mesenchymal transition (EMT) proteins and MYC targets across multiple cancer types.


## 关键词

Pan-cancer, analysis, decoding, mRNA, stability

## 相关实体

疾病: cancer

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
