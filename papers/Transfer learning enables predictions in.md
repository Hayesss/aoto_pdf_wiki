---
marker_extracted: true
title: "Transfer learning enables predictions in"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/transfer-learning-enables-predictions-in.md]
confidence: medium
year: 2023
---

# Transfer learning enables predictions in

> 原文: [[transfer-learning-enables-predictions-in]]

## 摘要

Fine-tuning Model for layer for Genecorpus-30M fine-tuning task 1 Task 1 task 1 predictions Self-supervised Copy pretraining Pretrained weights ... Geneformer Fine-tuning Model for layer for fine-tuning task N Task N task N predictions Fine-tuning Limited task-specific data for task N Tissue representation of Genecorpus-30M Brain Placenta Prostate Breast Adrenal Small intestine Lymphatic Decidua Unlabelled Adipose Tonsil Bone marrow Pancreas Endothelial Bladder Oesophagus Airway Bone Stomach Skin Immune Cord blood Pluripotent Embryo Eye Spleen Intestine, NOS Nasal Testis Thymus Yolk sac Ear Large intestine Lymph node Muscle Liver Kidney Lung Heart Gene T Gene H Gene Y Gene A Gene Z Gene L understanding of network dynamics. The pretrained Geneformer accu- of downstream applications can be pursued to accelerate discovery rately predicted dosage-sensitive disease genes and their downstream of key network regulators and candidate therapeutic targets. targets through a context-aware in silico deletion approach. Further- more, fine-tuning Geneformer towards a diverse panel of downstream Geneformer architecture and pretraining tasks relevant to chromatin and network dynamics using just a limited set of task-specific training examples demonstrated that Geneformer Geneformer is a context-aware, attention-based deep learning model consistently boosted predictive accuracy.

## 背景与目的

overall relative ranking of genes within each cell remains more stable. the final cell-type predictions in that specific tissue. Therefore, these The rank value encoding of the transcriptome of each single cell then approaches do not take advantage of the large amounts of data avail- proceeds through six transformer encoder units1,2, each composed of able more broadly that are not specifically labelled for that task. By a self-attention layer and feed forward neural network layer (Fig. 1c). contrast, Geneformer learns from large-scale unlabelled data during Pretraining was accomplished using a masked learning objective, which the self-supervised pretraining using a generalizable learning objec- has been shown in other informational fields1,2 to improve generaliz- tive to gain fundamental knowledge that can then be transferred to a ability of the foundational knowledge learned during pretraining for multitude of new and diverse fine-tuning tasks. Compared to these a wide range of downstream fine-tuning objectives. During pretrain- alternative methods, Geneformer boosted cell-type predictions in a ing, 15% of the genes within each transcriptome were masked, and the variety of tissues, with the gap in performance by accuracy and macro F1 model was trained to predict which gene should be within each masked score increasing as the number of cell-type classes increased, indicating position in that specific cell state using the context of the remaining that Geneformer was robust in ...

## 主要发现

Bivalent versus non-methylated 1.0 1.0 0.8 0.8 0.6 0.6 0.4 0.4 0.2 0.2 0 0 0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0 False positive rate b d Bivalent versus Lys4-only methylated Long versus short-range TFs 1.0 1.0 0.8 0.8 0.6 0.6 0.4 0.4 0.2 0.2 0 0 0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0 False positive rate False positive rate Fig. 3 | Geneformer boosted predictions of chromatin dynamics with predictions of bivalent versus Lys4-only-methylated genes after fine-tuning limited data. a,b, ROC curve of Geneformer fine-tuned to distinguish bivalent on only 56 loci as in b. d, ROC curve of Geneformer fine-tuned to distinguish versus non-methylated (a) or bivalent versus Lys4-only-methylated (b) genes long-range versus short-range transcription factors (TFs) using limited data in 56 conserved loci from ref. 28 using limited data (about 15,000 ESCs), (about 38,000 cells from iPSC to cardiomyocyte differentiation), compared to compared to alternative methods. c, ROC curve of Geneformer’s genome-wide alternative methods. (Alternative methods described in Fig. 2). 1.0 1.0 0.8 0.8 0.6 0.6 0.4 0.4 0.2 0.2 0 0 1.0 0.8 0.6 0.4 0.2 0 To investigate the threshold for minimal data needed for fine-tuning, of Geneformer’s six layers has four attention heads that are meant to we fine-tuned the pretrained Geneformer with progressively smaller learn in an unsupervised manner to pay attention to distinct classes of numbers of normal ECs from the Heart Atlas32 to distinguish central genes to j...

## 方法概述

#### **Assembly and rank value encoding of transcriptomes in Genecorpus-30M**

**Assembly and uniform processing of single-cell transcriptomes.** We assembled a large-scale pretraining corpus, Genecorpus-30M, comprising 29.9 million (29,900,531) human single-cell transcriptomes from a broad range of tissues from publicly available data (Fig. [1b](#page-1-0) and Supplementary Table 1). We excluded cells with high mutational burdens (for example, malignant cells and immortalized cell lines) that could lead to substantial network rewiring without companion genome sequencing to facilitate interpretation. We only included droplet-based sequencing platforms to assure expression value unit comparability. Overall, 561 datasets were included and stored as uniform files in the .loom HDF5 format including metadata from the original studies as row (feature) and column (cell) attributes described below.

Publicly available datasets containing raw counts were collected from the National Center for Biotechnology Information (NCBI) Gene Expression Omnibus (GEO), NCBI Sequence Read Archive (SRA), Human Cell Atlas, European Molecular Biology Laboratory-European Bioinformatics Institute (EMBL-EBI) Single Cell Expression Atlas, Broad Institute Single Cell Portal, Brotman Baty Institute (BBI)-Allen Single Cell Atlases, Tumor Immune Single-cell Hub (TISCH) (excluding malignant cells), Panglao Database, 10x Genomics, University of California, Santa Cruz Cell Browser, European Genome-phenome Archive, Synapse, Riken, Zenodo, National Institutes of Health (NIH) Figshare Archive, NCBI dbGap, Refine.bio, China National GeneBank Sequence Archive, Mendeley Data and individual communication with authors of the original studies[11](#page-8-10),[23](#page-8-21),[29,](#page-8-28)[32,](#page-8-31)[45](#page-8-25),[47–](#page-11-0)[153](#page-12-0). Further resources for collecting information about suitable studies included Entrez Direct tools and the dataset summary from Database 2020 (ref. [154](#p


## 讨论与结论

In sum, we developed a context-aware deep learning model, Geneformer, pretrained on large-scale transcriptomic data to enable predictions in settings with limited data. Through the observation of a vast number of cell states during the pretraining process, Geneformer gained a fundamental understanding of network dynamics, encoding network hierarchy in the attention weights of the model in a completely self-supervised manner. Geneformer's ability to predict dosage-sensitive disease genes through the context-aware in silico deletion approach represents a valuable asset for interpretation of genetic variants, including prioritization of GWAS hits driving complex traits, and the specific tissues they are expected to affect. Experimental validation of a dosage-sensitive gene candidate in fetal

<span id="page-7-0"></span>**Fig. 6 | In silico treatment revealed candidate therapeutic targets.**

**a**, Fine-tuning Geneformer to distinguish cardiomyocytes from non-failing hearts or hearts affected by hypertrophic or dilated cardiomyopathy (HCM and DCM) defines the embedding position of each cell state. Then, disease modelling (left) can be performed by in silico deleting or activating random genes within non-failing cardiomyocytes to define the random distribution (grey cloud) and thereby identify genes whose in silico deletion or activation shifts the embedding significantly towards either the hypertrophic or dilated cardiomyopathy state. The reverse approach is taken for in silico treatment analysis (centre and right). **b**, Out-of-sample predictions of Geneformer fine-tuned to distinguish cardiomyocytes from non-failing hearts or hearts affected by hypertrophic or dilated cardiomyopathy. Accuracy 90%; precision 82%; recall 87%. (Training data: non-failing *n* = 9, hypertrophic *n* = 11, dilated *n* = 9, total 93,589 cells; out-of-sample data: non-failing *n* = 4, hypertrophic *n* = 4, dilated *n* = 2, total 39,006 cells). **c**, Hierarchical clustering of fine-tuned Gen


## 关键词

Transfer, enables, learning, predictions

## 相关实体

疾病: disease

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
