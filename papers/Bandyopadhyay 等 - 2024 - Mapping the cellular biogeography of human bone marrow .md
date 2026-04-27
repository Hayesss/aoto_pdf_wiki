---
title: "Bandyopadhyay 等 - 2024 - Mapping the cellular biogeography of human bone marrow niches using single-cell transcriptomics"
created: 2025-04-22
updated: 2025-04-22
type: paper
tags: ["scrna-seq"]
sources: ["raw/papers/bandyopadhyay-等-2024-mapping-the-cellular-biog.md"]
confidence: medium
marker_extracted: true
---

# Bandyopadhyay 等 - 2024 - Mapping the cellular biogeography of human bone marrow niches using single-cell transcriptomics

> Zotero Item Key: 2R4S2PNW
> 原文: [[bandyopadhyay-等-2024-mapping-the-cellular-biog]]

## 摘要

（待补充）

## 背景与目的

The bone marrow is a complex organ that houses diverse cells from the hematopoietic, mesenchymal, endothelial, vascular smooth muscle, and neural lineages.[1](#page-18-0) Relatively rare non-hematopoietic cells are known to make critical contributions to hematopoiesis.[2](#page-18-1) Many non-hematopoietic cell types, including endothelial cells (ECs), mesenchymal stromal cells (MSCs), and osteoblasts have been proposed to be critical constituents of the bone marrow niche.[3–6](#page-18-2) Recent technological advances employing single-cell RNA sequencing (scRNA-seq) revealed the existence of multiple subpopulations of these non-hematopoietic marrow elements in mice.[7–10](#page-18-3)

Despite extensive work studying human hematopoietic cells, there remains a relative paucity of analogous studies defining the non-hematopoietic cells that make up the human bone marrow microenvironment.[11–13](#page-18-4) Defining the single-cell composition of bone marrow niches has been limited by challenges in isolating sufficient viable non-hematopoietic cells, which make up <0.5% of the marrow cellularity.[14,](#page-18-5)[15](#page-18-6) Moreover, specific cell

<span id="page-1-0"></span><sup>1</sup>Cellular and Molecular Biology Graduate Group, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-1"></span><sup>2</sup>Medical Scientist Training Program, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-2"></span><sup>3</sup>Department of Orthopaedic Surgery, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-4"></span><sup>4</sup>Division of Oncology and Center for Childhood Cancer Research, Children's Hospital of Philadelphia, Philadelphia, PA, USA

<span id="page-1-6"></span><sup>5</sup>Applied Mathematics & Computational Science Graduate Group, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-7"></span><sup>6</sup>Center for Single Cell Biology, Children's Hospital of Philadelphia, Philadelphia, PA, USA

<span id="page-1-8"></span><sup>7</sup>Department of Bioengineering, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-9"></span><span id="page-1-5"></span><sup>8</sup>Genomics and Computational Biology Graduate Group, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA 9Department of Computer and Information Science, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-11"></span><sup>10</sup>Department of Oral and Maxillofacial Surgery/Pharmacology, School of Dental Medicine, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-12"></span><sup>11</sup>Department of Pathology and Laboratory Medicine, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-13"></span><sup>12</sup>Department of Medicine, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-10"></span><sup>13</sup>Department of Pediatrics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

<span id="page-1-3"></span><sup>14</sup>These authors contributed equally

<span id="page-1-15"></span><sup>15</sup>Lead contact

<span id="page-1-14"></span><sup>\*</sup>Correspondence: [qinling@pennmedicine.upenn.edu](mailto:qinling@pennmedicine.upenn.edu) (L.Q.), [tank1@chop.edu](mailto:tank1@chop.edu) (K.T.) <https://doi.org/10.1016/j.cell.2024.04.013>

## 主要发现

### A comprehensive scRNA-seq atlas of the human bone marrow

To uncover the cellular composition of the human bone marrow, we developed an experimental pipeline for enzymatic release of cells from femoral head tissue (Figures S1A and S1B). We confirmed that areas of interest had normal trabecular structure by performing micro-computed tomography analysis (trabecular bone volume [BV] fraction: 0.261 ± 0.098 [mean ± SD], *n* = 6, Figure S1A). Next, we devised an enrichment strategy that would capture hematopoietic cells, rare hematopoietic stem and progenitor cells (HSPCs), and non-hematopoietic microenvironmental cells [\(Figure 1](#page-2-0)A; [STAR Methods](#page-22-0)). The three populations were pooled in a ratio favoring representation of rare HSPCs and non-hematopoietic cells and then subjected to scRNA-seq [\(Figure 1](#page-2-0)A).

We collected bone marrow from fresh femoral heads from 16 individuals between 52 and 80 years of age who underwent hip replacement surgery, performing scRNA-seq on 12 of them and CODEX on another 12, with 8 overlapping samples [\(Table S1\)](#page-17-0). In total, we sequenced 53,417 hematopoietic cells and 29,325 non-hematopoietic cells ([Figures 1B](#page-2-0) and 1C). We captured rich, high-quality transcriptional information in each cell lineage, with per-cell medians of 16,903 unique molecular identifiers (UMIs), 3,117 unique genes, and 3% mitochondrial reads detected after quality control filtering (Figure S1C).

We first analyzed the hematopoietic populations. As expected, we identified tri-lineage hematopoiesis and HSPC subsets ([Fig](#page-2-0)[ure 1D](#page-2-0); [Table S2\)](#page-17-0). Additionally, we improved upon other hematopoiesis-focused bone marrow scRNA-seq reference[s11](#page-18-4),[12](#page-18-13) by capturing the full granulocyte differentiation trajectory by virtue of our sample processing not including density-based isolation of mononuclear cells—a standard clinical tissue banking process which results in granulocyte loss due to their multi-lobated nuclei (*CSF3R*; [Figures 1B](#page-2-0) and S1D). Numerous plasma cells were also captured as a byproduct of the CD45 depletion procedure (*MZB1*; [Figures 1B](#page-2-0) and S1D). Age did not skew the frequencies of captured cell types (Figure S1E).

Next, we analyzed the non-hematopoietic cell compartment. We identified three major cell lineages—vascular smooth muscle cells (VSMCs) (*ACTA2*, *RGS5*, and *TAGLN*), ECs (*CDH5*, *PE-CAM1*, and *VWF*), and mesenchymal cells (*CXCL12* and *PDGFRA*) including MSCs and osteoblasts ([Figures 1B](#page-2-0)–1D and S1D; [Table S2\)](#page-17-0). Our analysis revealed far greater cellular diversity within these cells in bone marrow than existing scRNA-seq references (Figure S1F). Notably, contrary to earlier findings that characterize MSCs as relatively homogeneous with an adipocytic transcriptional profile,[13](#page-18-8)[,16–18](#page-18-9) we found these enzymatically released cells to be highly heterogeneous with numerous clusters identified [\(Figures 1](#page-2-0)B and S1F).

Importantly, we did not observe an inflammatory response signature, except in cell types which express inflammatory cytokines as part of their identity (mature neutrophils and monocytes, e.g., *CXCL8* and interleukin *IL-1B*), supporting the notion that these samples represent healthy aged bone marrow [\(Figures S2A](#page-38-0) and S2B). Moreover, compared to existing healthy donor aspirate-derived bone marrows, our samples did not express more

Figure 1. A single-cell transcriptomic atlas of hematopoietic and non-hematopoietic cells of human bone marrow

(A) Schematic for the scRNA-seq workflow. Magnetic-activated cell sorting (MACS) separation of hematopoietic, stem/progenitor, and mesenchymal fractions was performed and then pooled into one scRNA-seq reaction per patient.

(B) Uniform manifold approximation and projection (UMAP) representation of 82,742 single-cell transcriptomes from bone marrow of 12 individuals. AEC, arterial endothelial cell; SEC, sinusoidal endothelial cell; VSMC, vascular smooth muscle cell; Ba, basophil; Eo, eosinophil; Ma, mast cell; RBC, red blood cell; pDC, plasmacytoid dendritic cell; CLP, common lymphoid progenitor; MEP, megakaryocyte erythroid progenitor; GMP, granulocyte monocyte progenitor; MPP, multipotent progenitor; HSPC, hematopoietic stem and progenitor cell; HSC, hematopoietic stem cell; Meg/E, megakaryocyte/erythroid; MSC, mesenchymal stromal cell.

(C) Bar plots showing the cell counts for each lineage captured (left) and the cell lineage proportions per sample (right).

(D) Heatmap showing normalized gene expression scaled by row (gene) of top differentially expressed and key cell lineage marker genes. EC, endothelial cell; M, vascular smooth muscle. Genes are color-coded to match the lineage of the cell type in which they are differentially expressed. See also [Figures S1](#page-36-0), [S2,](#page-38-0) and [S3.](#page-39-0)

<span id="page-4-0"></span>(legend on next page)

## 方法概述

（待补充）

## 讨论与结论

We report the most comprehensive healthy human bone marrow reference to date, covering both hematopoietic and non-hematopoietic cell types and their spatial organization. We found that the bone marrow microenvironment contains at least six mesenchymal subsets, two endothelial cell subsets, and one vascular smooth muscle population. Our data clearly demonstrate the limitations of bone marrow aspirates as a sample source, where Adipo-MSCs are heavily favored and subsets like Fibro-MSCs are not captured at all.[13,](#page-18-8)[16–18](#page-18-9) We identified markers to sort MSC subpopulations and pinpointed the rare Podoplanin+ Fibro-MSCs as the closest to the ISCT-defined mesenchymal stem cell. By contrast, Adipo- and THY1+ MSCs were found to be the most interactive with hematopoietic cells and not part of the endosteal signaling module. Adipo-, THY1+, Osteo-, Fibro-, and APOD+ MSCs also had significantly different profiles of support factor expression. These findings collectively demonstrate the utility of our atlas for understanding differential functions of MSC subsets.

We elucidated the spatial organization of the human bone marrow on a systematic, single-cell level. While recent studies have assessed human bone marrow organization using 7-color immunofluorescence,[64](#page-20-11) our work more deeply dissected the cellular differentiation continua of both hematopoietic and nonhematopoietic lineages by virtue of our 53-antibody panel. Our healthy atlas captured the spatial relationships of 32 cell types with respect to each other and to many manually annotated, difficult to segment cell types/structures. This atlas links mesenchymal heterogeneity on the transcriptional level to discrete spatial phenotypes *in situ*, for instance in the case of more central Adipo-/THY1+ versus endosteal Osteo-/Fibro-MSCs. Our spatial findings were generalizable across anatomic sites as well, as our observations in femoral head bone marrow were closely recapitulated in negative lymphoma staging marrows from iliac crest. Our data will serve as a powerful tool for uncovering bone marrow niche biology in health and disease by enabling rapid reference mapping and label transfer to study how these otherwise conserved spatial patterns become dysregulated or co-opted, as we show in the AML vignette.

Our findings also highlight the importance of measuring all bone marrow cell types and microanatomical structures simultaneously. For instance, we extend prior findings[65](#page-20-12) of an HSPCadipocyte spatial relationship by showing that the relationship is strongest for more primitive[49,](#page-19-25)[50](#page-19-26) SPINK2+ HSPCs and is stronger than any spatial association between SPINK2+ HSPCs and other structures. This finding is of particular importance as adipocytic density increases as humans age and local adipocytic density is markedly reduced in the context of acute leukemia. Bone marrow adipogenesis has been proposed as a negative regulator of hematopoiesis in mice,[66](#page-20-13) but a growing body of evidence has proposed adipocytes as both stemness-maintaining and supportive of stress hematopoiesis,[67–70](#page-20-14) and so whether this interaction represents a hematopoiesis-supportive or suppressive interaction in humans warrants further investigation. We surprisingly did not find an endosteal or perivascular preference for human HSPCs in femoral head or iliac crest. These data do not mean that sinusoid/osteoblast-HSC communication is unimportant, only that human HSPCs are not closer to sinusoids than expected by chance in older adult samples. Similar profiling efforts across the spectrum of aging will help reveal the relative contribution of these structures at different developmental stages.

## 关键词

Bandyopadhyay, Mapping, biogeography, bone, cellular, human, marrow, niches, single-cell, transcriptomics, using

## 相关实体

细胞类型: progenitor
方法: scRNA-seq, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
