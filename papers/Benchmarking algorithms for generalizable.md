---
marker_extracted: true
title: "Benchmarking algorithms for generalizable"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/benchmarking-algorithms-for-generalizable.md]
confidence: medium
year: 2025
---

# Benchmarking algorithms for generalizable

> 原文: [[benchmarking-algorithms-for-generalizable]]

## 摘要

Zhiting Wei 1,2,3,4,6, Yiheng Wang1,2,5,6, Yicheng Gao1,2,6, Shuguang Wang  1,2,6, Ping Li1 , Duanmiao Si1,2, Yuli Gao1,2, Siqi Wu1,2, Danlu Li1,2, Kejing Dong  1,2, Xingbo Yang1,2, Chen Tang1,2, Shaliu Fu 1,2, Xiaohan Chen1,2, Wannian Li1,2, Yuzhou You1,2, Chen Zhang1,2, Aibin Liang , Guohui Chuai 1,2,3 & Qi Liu  1,2,3


## 背景与目的

sGED-nommoC Robustness Scalability Overall rank Method 1 Method 2 Method 3 Level of noise Limitation and insights ycaruccA Level of sparsity ycaruccA emiT Number of perturbations/cells yromeM a Scenarios Kang et al. Haber et al. Norman et al. Datasets Replogle et al. ... 9 single 3 single 1 combo 14 methods 18 methods scGen, CellOT, trVAE, scELMo, scFoundation, CPA, biolord, Methods inVAE, scPreGAN, SCREEN, scDisInFact, scGPT, GeneCompass, baseMLP, chemCPA, scPRAM,baseMLP, biolord, AttentionPert, baseControl, PRnet, baseControl, trainMean, scVIDR scouter,GEARS, trainMean, cycleCDR baseReg GenePert,linearModel baseReg Population-average metrics MSE, PCC-delta, E-distance Evaluation Population-distribution metrics Wasserstein, Out of . . m .

## 主要发现

A comprehensive framework for benchmarking single-cell perturbation effect prediction

Methods. To thoroughly assess the performance of prediction methods in this field, we developed a comprehensive benchmark framework, including state-of-the-art methods, diverse datasets and rigorous evaluation metrics (Fig. 1a). In this study, we evaluated the methods across two key scenarios: cellular context generalization and perturbation generalization (Fig. 1a). While we aimed to include a diverse set of methods in our evaluation, several tools were excluded for specific reasons (Supplementary Note 1). As a result, in the cellular context generalization scenario, we examined 10 methods from published studies: biolord, CellOT, inVAE, scDisInFact, scGen, scPRAM, scPreGAN, SCREEN, scVIDR and trVAE. In the perturbation generalization scenario, we examined another 14 methods: AttentionPert, biolord, CPA, GEARS, GenePert, linearModel, scFoundation, scGPT, chemCPA, scouter, scELMo, GeneCompass, PRnet and cycleCDR. Given the growing concerns raised in recent literature regarding the effectiveness of advanced machine learning models, particularly foundation models, we also included 4 baseline models named baseReg, baseMLP, baseControl and trainMean (Methods). These baseline models serve as benchmarks to determine whether more complex methods learn additional meaningful information from the data. In total, our evaluation includes 23 published methods and 4 baseline models, covering a broad spectrum of methodological approaches in single-cell perturbation effect prediction.

**Datasets.** The systematic benchmark relies on a collection of diverse datasets designed to reflect real-world biological challenges. For the cellular context generalization scenario, we curated 12 datasets categorized on the basis of the cellular context<sup>1,32-37</sup> (Fig. 1b).


## 方法概述

#### Settings of benchmark methods

In this study, we selected a range of advanced modeling approaches to systematically compare their ability to predict single-cell perturbation effects. The models include diverse theoretical frameworks and algorithmic structures, ranging from linear models to foundation models, and other deep learning-based approaches. In this study, we evaluated the methods in two key scenarios: cellular context generalization and perturbation generalization. In the cellular context generalization scenario, we selected 14 methods, including 10 published methods, namely, biolord, CellOT, inVAE, scDisInFact, scGen. scPRAM, scPreGAN, SCREEN, scVIDR and trVAE and 4 baseline models. In the perturbation generalization scenario, we examined 18 methods: AttentionPert, biolord, CPA, GEARS, GenePert, linearModel, scFoundation, scGPT, chemCPA, scouter, scELMo, GeneCompass, PRnet, cycleCDR and 4 baseline models. For each method, the parameters were set according to official guidelines and tailored to align with our benchmarking datasets. Please refer to Supplementary Note 1 for detailed descriptions and settings of all benchmark methods.


## 讨论与结论

In this study, we provide a comprehensive benchmark of single-cell perturbation prediction methods across two key scenarios: cellular context generalization and perturbation generalization. We assessed 27 methods with a total of 29 datasets using 6 evaluation metrics— MSE, PCC-delta, E-distance, Wasserstein distance, KL-divergence and Common-DEGs—with a focus on evaluating the methods' generalizability. Simulated data were also used to assess the impact of noise and sparsity on performance. Our findings revealed that no single method performs well across all datasets, highlighting the need for user-specific guidance in selecting methods on the basis of dataset characteristics. These results are as follows: (1) In the cellular context generalization scenario, trVAE, CellOT and inVAE demonstrated the best overall performance on single-condition datasets. For the accurate prediction of the top most differentially expressed genes, scPRAM is the optimal choice. Additionally, when the dataset includes perturbation dosage information, scVIDR is the best method. (2) In the perturbation generalization scenario, for predicting genetic single-perturbation effects, GenePert is the optimal choice when the training dataset is small. When the fine-tuning dataset is sufficiently large, CPA and scGPT are preferable. For predicting genetic combined-perturbation effects, the linearModel and scouter method perform the best. In chemical single-perturbation effect prediction, chemCPA is the preferred choice, whereas the baseReg baseline model achieves the highest accuracy in chemical combined-perturbation effect prediction (Fig. [5g](#page-9-0)).

For designing future algorithms, the following limitations of existing methods and insights should be considered: (1) In the cellular context generalization scenario, most existing tools do not incorporate time-point/dosage covariates, and those that do are still far from sufficiently accurate.


## 关键词

Benchmarking, algorithms, generalizable

## 相关实体

方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
