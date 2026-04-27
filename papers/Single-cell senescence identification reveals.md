---
marker_extracted: true
title: "Single-cell senescence identification reveals"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/single-cell-senescence-identification-reveals.md]
confidence: medium
year: 2024
---

# Single-cell senescence identification reveals

> 原文: [[single-cell-senescence-identification-reveals]]

## 摘要

Cellular senescence underlies many aging-related pathologies, but its heterogeneity poses challenges for studyingandtargetingsenescentcells.Wepresenthereamachinelearningprogramsenescentcellidentifi- cation (SenCID), which accurately identifies senescent cells in both bulk and single-cell transcriptome. Trainedon602samplesfrom52senescencetranscriptomedatasetsspanning30celltypes,SenCIDidentifies sixmajorsenescenceidentities(SIDs).DifferentSIDsexhibitdifferentsenescencebaselines,stemness,gene functions,andresponsestosenolytics.SenCIDenablesthereconstructionofsenescenttrajectoriesunder normal aging,chronic diseases, and COVID-19. Additionally,when applied to single-cell Perturb-seq data, SenCIDhelpsrevealahierarchyofsenescencemodulators.Overall,SenCIDisanessentialtoolforprecisesin- gle-cellanalysisofcellularsenescence,enablingtargetedinterventionsagainstsenescentcells. INTRODUCTION cells,18makingitanurgentneedtoidentifythesedifferentialpat- ternsandtheirspecificregulators,thustoenhancetreatmentef- Cellular senescence is a state of permanent cell cycle arrest1 ficacyandspecificity. inducedbymultipletypesofstresses,includingover-replication, Tobettertargetthesenescentcells,itisessentialtoaccurately DNA-damage-stress-like radiation,oxidativestress,andonco- identifysenescentcellsindifferentbiologicalenvironments.Un- gene activation.2,3 Both proliferating and post-mitotic cells fortunately,thereiscurrentlynosinglemarkerthatisuniquefor (e.g.

## 背景与目的

Cellular senescence is a state of permanent cell cycle arrest[1](#page-13-0) induced by multiple types of stresses, including over-replication, DNA-damage-stress-like radiation, oxidative stress, and oncogene activation.[2](#page-13-1)[,3](#page-13-2) Both proliferating and post-mitotic cells (e.g., fully differentiated cells) can be induced to senescence,[3](#page-13-2)[,4](#page-14-0) which exhibit various senescence-related phenotypes, like increased size of nucleoli, enlarged and overloaded lysosome, and secretion of senescence-associated secretory phenotype (SASP) factors.[5–7](#page-14-1) Senescent cells accumulate inside the body during aging[4,](#page-14-0)[8](#page-14-2) and contribute to the initiation and progression of various aging-related chronic diseases.[9–11](#page-14-3) Treatments to target and kill senescent cells, like senolytics, have shown promising results in extending lifespans and ameliorating various diseases.[12](#page-14-4)[,13](#page-14-5) The target specificity and toxicity to non-senescent cells is still a big hurdle for clinical applications of the current senolyitc treatments.[14](#page-14-6)[,15](#page-14-7) Wrongly targeting quiescent (a state where the cells temporarily arrest for growth but reversible[8](#page-14-2) ) or differentiated cells as senescent cells obviously has dire consequences. Furthermore, there are beneficial effects of senescent cells in certain circumstances, which brings more critical requirements to study the right time and condition for senolytics to overcome the harmful effects.[16](#page-14-8) Besides, senescence patterns are variable across cell types, tissues, and inductions.[17](#page-14-9) Some senolytic drugs are effective in some cell types but not others, suggestive of differential patterns or modes of senescence among cells,[18](#page-14-10) making it an urgent need to identify these differential patterns and their specific regulators, thus to enhance treatment efficacy and specificity.

To better 


## 主要发现

#### Heterogeneity of senescence signatures across cell types

To develop a program applicable to a broad range of cellular senescence identification, we collect published transcriptome data from 602 samples across 52 senescence-related studies, including 306 senescent and 296 non-senescent labels[.17](#page-14-9)[,21](#page-14-14)[,27](#page-14-18)[,35–80](#page-14-22) The bulk transcriptome dataset (BTD) contain 57 types of cell lines and 30 cell types with various senescence inductions ([Figures S1](#page-13-3)A and S1B; [Table S1\)](#page-13-3). We first compare 3 different machine learning methods, supporting vector machine (SVM), random forest, and deep-neural-network-based multilayer perceptron classifier (MLPC), along with a routine gene set ranking method (gene set variation analysis, GSVA)[,26](#page-14-17) based on a gene set with 1,290 SRGs collected from literature ([STAR](#page-19-0) [Methods\)](#page-19-0). We implement a leave-one-cell-type-out strategy for all the machine learning methods [\(STAR Methods](#page-19-0)) and use areas under receiver operator characteristic (ROC) curves (AUCs) from predictions on each test set. The machine learning algorithms generally perform better (with ROC AUCs over 0.9 in 88.9% of cell types in average) than GSVA (with AUC over 0.9 in 76.6% of cell types) [\(Figure S1C](#page-13-3)). Furthermore, when only considering the ability to distinguish senescent cells from quiescent cells, machine learning methods (with AUC over 0.9 in 80% of cell types in average) perform much better than GSVA (with AUC over 0.9 in only 20% of cell types) [\(Figure S1](#page-13-3)D), suggesting that the machine learningmodels aremore specific to the senescence state,making them applicable to normal aging and degenerative processes, rather than being limited to cancers and proliferating cell lines.

Among the three machine learning methods we tested, SVM performs the best, with AUC over 0.9 in 96.7% of cell types [\(Fig](#page-13-3)[ure S1


## 方法概述

0.8 0.6 0.4 0.2 0.0 Unassigne N d onTargeting BRCA1 PTPRD RB1 ARID1B TP53 MultiTargeting OtherTargets RPE1 Perturbed GSEA vacuolar proton−transporting V−type ATPase complex vacuolar membrane structural constituent of ribosome structural constituent of cytoskeleton sister chromatid segregation ribosomal subunit response to unfolded protein response to topologically incorrect protein respira re to s r p y o n ch se a in to c h o y m p p ox le ia x |NES| proton−transporting V−type ATPase complex 1.5 protein localization to endoplasmic reticulum proteasome complex 2.0 primary active transmembrane trans a p c o ti r v t i e ty r 2.5 positive regulation of cell−substrate adhesion 3.

## 讨论与结论

In summary, our SenCID program is an innovative machine learning algorithm capable of identifying senescence in both bulk and single-cell transcriptome data. It quantitatively assesses senescence states and heterogeneity in cell lines or primary tissues in aging and aging-related diseases. Our models reveal that cells can be classified into six different SID categories, with differing baselines of senescence inversely correlated to

stemness, distinct senescence signatures, and varying responses to senolytics. SenCID also enables the dissection of heterogeneity and reconstruction of senescent trajectories and has uncovered potential regulons for chronic human diseases, normal human tissue aging, and COVID-19. We have found that senescent cells in each pathological condition not only upregulate SASP genes to influence other cells but also enhance SASP autocrine loop, as found in multiple previous studies[,124–127](#page-18-0) further highlighting the potential for self-perpetuating regulation as a target for breaking the vicious cycle of cell senescence, similar to the case for fibrosis[.128](#page-18-1) Lastly, our analysis of single-cell Perturb-seq data reveals that senescence can be induced by the disruption of eight essential cellular machineries, with the majority of senescence-promoting perturbations channeled through cell cycle and chromatin-segregation-related group 2 to induce senescence. Our findings indicate a clear modularity and hierarchy among senescence modulators.

<span id="page-13-3"></span>Our study provides deep insights into the ubiquity and complexity of senescence in human tissues during aging and diseases, revealing the fundamental relationship between basal senescence level and stemness and elucidating the modular nature of senescence triggers converging on a core module leading to similar senescence endpoints. Importantly, our SenCID tool allows characterizing senescent patterns that are specific to certain disease and aging processes, tiss


## 关键词

Single-cell, identification, reveals, senescence

## 相关实体

方法: Single-cell, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
