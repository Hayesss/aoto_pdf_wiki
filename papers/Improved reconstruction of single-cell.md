---
marker_extracted: true
title: "Improved reconstruction of single-cell"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/improved-reconstruction-of-single-cell.md]
confidence: medium
year: 2025
---

# Improved reconstruction of single-cell

> 原文: [[improved-reconstruction-of-single-cell]]

## 摘要

and Supplementary Tables 2–4). The agreement between known and surpassed eight developmental hierarchy inference methods for predicted developmental orderings was quantified using weighted cross-dataset (absolute) and intra-dataset (relative) performance3,14–20, Kendall correlation to ensure balanced evaluation and minimize bias demonstrating over 60% higher correlation, on average, for recon- (Supplementary ). structing relative orderings in 57 developmental systems, including We started by evaluating model hyperparameters through data from Tabula Sapiens33 (Fig. 1h,i and Supplementary Tables 12 cross-validation and observed minimal performance variation across and 13). Similar results were observed when comparing CytoTRACE 2 a wide range of values (Extended Data Fig. 1e,f and Supplementary against nearly 19k annotated gene sets34–36 (Fig. 1i and Supplementary ). Based on this, we selected stable hyperparameters and ) and scVelo5, a generalized RNA velocity model for predicting retrained the model. On the training data, we demonstrated that future cell states (Extended Data Fig. 8 and Supplementary ). CytoTRACE 2 achieves high accuracy in distinguishing absolute Previous genomic studies of stemness largely focused on pluri- potency for broad potency labels (Fig. 1d). potency, with limited insight into other potency states.

## 背景与目的

redro evitaleR )τ( 0.6 0.4 0.2 0 0 0.2 0.4 0.6 0.8 Absolute order prediction Absolute order prediction (τ) (τ) noitciderp redro evitaleR )τ naidem( g h i Test set Tabula Sapiens (n = 14 held-out datasets) (n = 48 tissue, platform pairs) 0.4 0.2 0 0 0.2 0.4 1 ECARTotyC Less diff. More diff. hturt dnuorG2 ECARTotyC Dataset Potency category Gene set binary network modules Toti. Totipotent Pluripotent Potency Pluri. Multipotent probability Multi. Oligopotent Oligo. Unipotent Uni. GS1 Potency score Calculates enrichments Predicts potency score Toti. Pluri. Multi. Oligo. Uni. Diff. Toti. Pluri. Multi. Oligo. Uni. Diff. ... ... ... ... Binary weight matrix ... ... ... ... ... Gene sets seneG X1 Enrichment layers X2 X4 XN ... τ = 0.82 τ = 0.81 Differentiated Diff. P < 2.2 × 10–16 P < 2.2 × 10–16 GS2 GST X3 G G S S 1 1G G S S 2 2 G G S S T T 1 Toti. GS1GS2 GST Pluri. Multi. 0.5 GS1GS2 GST Oligo. Uni. Diff. 0 1 Learns gene sets 2 3 Leave-clade-out model (n = 33 datasets) Predicted potency τ = 0.86 τ = 0.70 Toti. P < 2.2 × 10−16 P < 2.2 × 10−16 Pluri. Multi. Oligo. Uni. Diff. Ground truth potency (n = 24 granular potency levels) CytoTRACE 2 CytoTRACE 1 SCENT (CCAT) SCENT (SR) FitDevo SLICE StemID scTour mRNAsi Gene sets (n = 18,706) Brief Communication Training set Test set 0.6 0.4 0.2 0 –0.2 –0.

## 主要发现

moderate labeling variation was well tolerated. Performance may 12. Stuart, T. et al. Comprehensive integration of single-cell data. Cell decline when analyzing cells with very low RNA content or number 177, 1888–1902.e1821 (2019). of expressed genes (Extended Data Fig. 3). While some phenotypes 13. Zheng, X. et al. Massively parallel in vivo Perturb-seq reveals were misclassified in held-out data, absolute errors remained low and cell-type-specific transcriptional networks in cortical outcompeted existing methods. Finally, although the current model is development. Cell 187, 3236–3248 e3221 (2024). Nature Methods Brief Communication 14. Teschendorff, A. E., Maity, A. K., Hu, X., Weiyan, C. & Lechner, M. 31. Tan, Y. & Cahan, P. SingleCellNet: a computational tool to classify Ultra-fast scalable estimation of single-cell differentiation single cell RNA-seq data across platforms and across species. potency from scRNA-seq data. Bioinformatics 37, 1528–1534 Cell Syst. 9, 207–213 e202 (2019). (2020). 32. Kiselev, V. Y., Yiu, A. & Hemberg, M. scmap: projection of 15. Teschendorff, A. E. & Enver, T. Single-cell entropy for accurate single-cell RNA-seq data across data sets. Nat. Methods 15, estimation of differentiation potency from a cell’s transcriptome. 359–362 (2018). Nat. Commun. 8, 15599 (2017). 33. Consortium, T. T. S. et al. The Tabula Sapiens: a multiple-organ, 16. Herman, J. S., Sagar & Grün, D.

## 方法概述

#### **Ethical compliance**

All animal procedures were performed in compliance with ethical regulations and conducted according to a protocol approved by the Stanford University Administrative Panel for Laboratory Animal Care committee (protocol no. 10868).


## 讨论与结论

that higher values received lower ranks and vice versa. models across two scenarios of training cohort annotation error, then For categorical predictions (CytoTRACE 2 and potency classifica- evaluated model performance over the test cohort (see ‘Training and tion benchmarking outputs only), we evaluated potency classification test datasets’). To simulate annotation error, we formulated label noise performance as well. Binary correctness of predicted versus ground as a transition matrix54, encoding the probability of perturbation from truth broad potency categories was assessed via mean multiclass F1 one potency to another (Extended Data Fig. 3a). Transition matrix score, implemented with function f1_score from sklearn.metrics with perturbation probabilities were designed to follow a Gaussian distribu- average = none (Extended Data Figs. 1c top, 2d second from right, tion based on the rank distance between the original potency and 3b–e left bottom, 7a left and 7b x axis). To account for the magnitude perturbed potency. In detail, the probability that the potency label of of deviations from ground truth potency, we also considered mean cell s transitions from true potency j to perturbed potency i absolute error (MAE), assigning each broad potency class an integer label corresponding to the class ordering, with labels ranging from 1 (j−i) 2 1 (differentiated) to 6 (totipotent), and computing the absolute value P(si|sj)= √2πσ2 exp(− 2σ2 ),i,j∈{1,2,3,4,5,6} of the difference betwe...

## 关键词

Improved, reconstruction, single-cell

## 相关实体

方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
