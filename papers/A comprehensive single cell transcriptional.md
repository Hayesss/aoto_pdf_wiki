---
marker_extracted: true
title: "A comprehensive single cell transcriptional"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/a-comprehensive-single-cell-transcriptional.md]
confidence: medium
year: 2019
---
marker_extracted: true

# A comprehensive single cell transcriptional

> 原文: [[a-comprehensive-single-cell-transcriptional]]

## 摘要

Fig. 4** Human Lin—CD34/CD164 versus mouse Kit+ transcriptome map and gene expression dynamics analysis. **a** Classification of individual cells into 11 homogenous transcriptional groups, based on inferred principal trajectories on mouse Kit+ transcriptome data (Supplementary Fig. 3c for details). Group labels and colors have been set to highlight similarities with Lin—CD34/CD164 fractionating map. Solid lines show results based on final converged iteration (Supplementary Fig. 3c for details). Dashed lines added manually to highlight a potential additional trajectory not present in final iteration and suggested by PBA analysis reported in the middle (DC-M). MPP, MultiPotent progenitor cells; Meg, megakaryocytes; BE, baso/eosinophils; E, erythroid cells; Ly, lymphoid cells; DC, dendritic cells; M, monocytes; G, granulocytes. **b** Comparison of human and mouse transcriptional states during erythropoiesis. Upper panels, schemes of the comparison. Mirror heatmaps, expression of the 721 orthologous genes selectively expressed along the human and mouse erythroid differentiation (LRT adjusted *p* value < 0.05). **c** Representative comparable dynamics of the orthologues TRIB2/Trib2 and CA2/Car2 reported in Tusi et al. vs divergent dynamics of the orthologues CD47/Cd47 and ZFPM1/Zfpm1 reported in Pishesha et al.

This difference in the expression of the machinery of ribosome biogenesis during erythropoiesis could explain why mouse models of red blood cells disorders caused by a partial loss of ribosomal function, such as Diamond–Blackfan anemia, are not able to recapitulate the human phenotype.

**Exploring CD164** as a marker of early human HSPC. We next asked whether we could take advantage of the data to rationally select a cell surface marker to fractionate human HSPCs for transplantation and gene therapy (Fig. 5). To date, the CD38 antigen has served to negatively enrich for the primitive progenitors for transplantation.


## 背景与目的

of differentiating states towards erythroid commitment. Our conducted a series of in vitro differentiation assays starting from results could be formalized, on a computational basis, by both FACS sorting Lin−CD34+ cells into CD135+ (FLT3+) (by high dimensions (using PBA algorithm, Fig. 2c) and inferred definition containing common myeloid progenitors (CMP) and transcriptional trajectories (Fig. 2d and Supplementary Fig. 3b) granulocyte–monocyte progenitors; GMP) and CD135−(FLT3−) andwereconfirmeduponanalyzingthedatawithanindependent (by definition containing MEP) cells (Fig. 3b–d and Supplemen- method(DiffusionMaps27,SupplementaryFig.5,6)thatdoesnot tary Fig. 9c).

## 主要发现

Generating a high-resolution scRNA map of CD34+ progenitors. To establish a reference data set and to address the heterogeneity and fate potential of the known CD34+ subsets, our first investigations aimed at mapping at high-resolution the single-cell transcriptional states of cells commonly defined as human HSPCs (Fig. 1a). To this goal, we separated CD34+ cells purified by magnetic beads selection into seven subpopulations, marking cells of differing fate potential (Fig. 1b) and tagged and sequenced the transcriptome of 6011 single cells (Supplementary Fig. 1a and Supplementary Table 1). We then used the

scRNA-Seq data to infer the structure of cell states in highdimensional gene expression space (Fig. 1c). We applied a visualization method previously developed for mouse hematopoietic progenitors, whereby each cell represents a graph node, with graph edges linking nearest neighbor cells. The scRNA-Seq graph, visualized using SPRING force-directed layout, shows a hierarchical, tree-like continuum of states, with branches that terminate at cells expressing recognizable transcriptional signatures of lineage commitment before the expression of final maturation markers (Fig. 1c, d) (megakaryocytes (Meg), erythroid cells (E), granulocytes (G), dendritic cells (DC), lymphoid cells (Ly1-2)). The structure of the single-cell data broadly partitions based on immunophenotypic subpopulations, but, significantly and in line with recent suggestions, we observed that previously defined HSPC subpopulations hide substantial transcriptional heterogeneity (Supplementary Fig. 2a).

Our scRNA-Seq map of CD34+ subpopulations suggests that HSPCs do not undergo a single-step transition from CLOUD-HSPCs to unilineage states. Instead, they form a structured hierarchy (Fig. 1c). The earliest fate split separates erythroid-megakaryocyte progenitors from lymphoid-myeloid progenitors (LMPs), which separate further into lymphoid, DC and granulocytic progenitors.


## 方法概述

**Cell preparation**. BM samples were collected from adult healthy donors at Children's Hospital in Boston with the approval of the Committee on Clinical Investigations Children's Hospital Boston and consent from the subjects under the protocol #09-04-0167. Mononuclear cells (MNCs) were isolated using Ficoll-Hypaque gradient separation (Lymphoprep, STEMCELL Technologies). CD34+cells were purified from MNCs with the human anti-CD34 MicroBeads Isolation Kit (Miltenyi Biotec) according to the manufacturer's specifications or were purchased from commercial sources (AllCells).

Cell sorting and immunophenotyping. Seven HSPC subpopulations were purified from the CD34+ fraction of a healthy donor BM cells through a two-step four-way sorting using FACSAria II (BD Biosciences) and processed to generate the transcriptome network in Fig. 1. The following combinations of cell surface markers were used to identify and separate the HSPC subsets. Hematopoietic stem cells (HSC): Lin-CD34+CD38-CD90+CD45RA-; multipotent progenitors (MPP): Lin-CD34+CD38-CD90-CD45RA+; multi-lymphoid progenitors (MLP): Lin-CD34+CD38-CD90-CD45RA+; pre-B lymphocytes/natural killer cells (PREB/NK): Lin-CD34+CD38+CD7-CD10+; MEP: Lin-CD34+CD38+CD7-CD10-CD135-CD45RA-; CMP: Lin-CD34+CD38+CD7-CD10-CD135-CD45RA-; CMP: Lin-CD34+CD38+CD7-CD10-CD135-CD45RA+.

For the generation of the transcriptome network in Fig. 2, four cell fractions were purified from a healthy donor BM MNCs through a four-way sorting using the following combinations of cell surface markers: ${\rm Lin-CD34+CD164+}$ ; ${\rm Lin-CD34-CD164^{high}}$ ; ${\rm Lin-CD34-CD164^{how}}$ . CD71 was included to identify erythroid progenitors.

For in vitro functional assays, Lin–CD34+CD135– and Lin–CD34+CD135+ fractions were purified from the CD34+ cells of three independent BM through a two-way sorting. The cell subsets CD34+CD164high and CD34+CD164low were FACS-sorted from the CD34+ cells of nine independent BM.


## 讨论与结论

We here report the generation of high-resolution scRNA maps of human hematopoietic cell fate commitment and the interrogation of our transcriptional profiling for conducting investigations into the basic biology of early hematopoiesis. Our fractionation strategy of the BM Lin— cells extended outside the CD34+ compartment constitutes a main advance over previous studies in that allowed us to preserve high resolution at both primitive and lineage-primed progenitors level. The results of the in silico, in vitro, and in vivo analyses reported in this work strongly suggests that human haematopoiesis develops along early cell fate bifurcations occurring in a continuum of states forming a hierarchical-like structure.

Our investigations into the origin of the basophil branch suggest that a very early priming of CD38- progenitors might be in place toward either the MK/erythroid/basophil or the lymphoid/granulo/DC/monocyte commitment and that this might be dependent on the expression of the CD135 surface marker. This observation calls for further studies into the potential heterogeneous composition of the CD34+CD38- compartment. In this regard, we would like to raise awareness on the arbitrary nature of the current strategies for the cytofluorimetric identification of the CD38- compartment. Indeed, despite using a very stringent CD38- sorting strategy we still observed an overlap of transcriptional states between CD38- HSC/MPP and CD38+ CMP/ MEP (Supplementary Fig. 2a). This is owing to the continuum of CD38 expression, which does not provide a clear-cut way to isolate with high purity primitive progenitors. We therefore suggest that, upon validating potential early lineage priming of human HSC or MPP, one should commit to the use of an extremely conservative CD38- gate in order to obtain high purity of bona fide multipotent progenitors.


## 关键词

cell, comprehensive, single, transcriptional

## 相关实体

细胞类型: erythroid, lymphoid, progenitor
方法: scRNA, scRNA-Seq, single-cell

---
marker_extracted: true

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
