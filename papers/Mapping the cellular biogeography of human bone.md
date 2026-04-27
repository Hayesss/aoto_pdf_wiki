---
marker_extracted: true
title: "Mapping the cellular biogeography of human bone"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/mapping-the-cellular-biogeography-of-human-bone-1.md]
confidence: medium
year: 2024
---

# Mapping the cellular biogeography of human bone

> 原文: [[mapping-the-cellular-biogeography-of-human-bone-1]]

## 摘要

Non-hematopoieticcellsareessentialcontributorstohematopoiesis.However,heterogeneityandspatialor- ganization of these cells in human bone marrow remain largely uncharacterized. We used single-cell RNA sequencing (scRNA-seq) to profile 29,325 non-hematopoietic cells and discovered nine transcriptionally distinct subtypes. We simultaneously profiled 53,417 hematopoietic cells and predicted their interactions with non-hematopoietic subsets. We employed co-detection by indexing (CODEX) to spatially profile over 1.2millioncells.WeintegratedscRNA-seqandCODEXdatatolinkpredictedcellularsignalingwithspatial proximity.Ouranalysisrevealedahyperoxygenatedarterio-endostealneighborhoodforearlymyelopoiesis, and an adipocytic localization for early hematopoietic stem and progenitor cells (HSPCs). We used our CODEXatlastoannotatenewimagesanduncoveredmesenchymalstromalcell(MSC)expansionandspatial neighborhoodsco-enrichedforleukemicblastsandMSCsinacutemyeloidleukemia(AML)patientsamples. This spatially resolved, multiomic atlas of human bone marrow provides a reference for investigation of cellularinteractionsthatdrivehematopoiesis. INTRODUCTION employing single-cell RNA sequencing (scRNA-seq) revealed theexistenceofmultiplesubpopulationsofthesenon-hemato- Thebonemarrowisacomplexorganthathousesdiversecells poieticmarrowelementsinmice.7–10 from the hematopoietic, mesenchymal, endothelial, vascular Despiteextensiveworkstudyinghumanhematopoieticcells, smooth muscle, and neural lineages.

## 背景与目的

The bone marrow is a complex organ that houses diverse cells from the hematopoietic, mesenchymal, endothelial, vascular smooth muscle, and neural lineages. Relatively rare non-hematopoietic cells are known to make critical contributions to hematopoiesis. Many non-hematopoietic cell types, including endothelial cells (ECs), mesenchymal stromal cells (MSCs), and osteoblasts have been proposed to be critical constituents of the bone marrow niche.3–6 Recent technological advances employing single-cell RNA sequencing (scRNA-seq) revealed the existence of multiple subpopulations of these non-hematopoietic marrow elements in mice.7–10

Despite extensive work studying human hematopoietic cells, there remains a relative paucity of analogous studies defining the non-hematopoietic cells that make up the human bone marrow microenvironment.11–13 Defining the single-cell composition of bone marrow niches has been limited by challenges in isolating sufficient viable non-hematopoietic cells, which make up <0.5% of the marrow cellularity.14, Moreover, specific cell

Cellular and Molecular Biology Graduate Group, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

Medical Scientist Training Program, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

Department of Orthopaedic Surgery, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA

Division of Oncology and Center for Childhood Cancer Research, Children's Hospital of Philadelphia, Philadelphia, PA, USA

Applied Mathematics & Computational Science Graduate Group, University of Pennsylvania, Philadelphia, PA, USA

Center for Single Cell Biology, Children's Hospital of Philadelphia, Philadelphia, PA, USA

Department of Bioengineering, University of Pennsylvania, Philadelphia, PA, USA

Genomics and Computational Biology Graduate Group, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA, USA 9Department of Computer and...


## 主要发现

### A comprehensive scRNA-seq atlas of the human bone marrow

To uncover the cellular composition of the human bone marrow, we developed an experimental pipeline for enzymatic release of cells from femoral head tissue (Figures S1A and S1B). We confirmed that areas of interest had normal trabecular structure by performing micro-computed tomography analysis (trabecular bone volume [BV] fraction: 0.261 ± 0.098 [mean ± SD], *n* = 6, Figure S1A). Next, we devised an enrichment strategy that would capture hematopoietic cells, rare hematopoietic stem and progenitor cells (HSPCs), and non-hematopoietic microenvironmental cells \(Figure 1A; STAR Methods). The three populations were pooled in a ratio favoring representation of rare HSPCs and non-hematopoietic cells and then subjected to scRNA-seq \(Figure 1A).

We collected bone marrow from fresh femoral heads from 16 individuals between 52 and 80 years of age who underwent hip replacement surgery, performing scRNA-seq on 12 of them and CODEX on another 12, with 8 overlapping samples \(Table S1\). In total, we sequenced 53,417 hematopoietic cells and 29,325 non-hematopoietic cells (Figures 1B and 1C). We captured rich, high-quality transcriptional information in each cell lineage, with per-cell medians of 16,903 unique molecular identifiers (UMIs), 3,117 unique genes, and 3% mitochondrial reads detected after quality control filtering (Figure S1C).

We first analyzed the hematopoietic populations. As expected, we identified tri-lineage hematopoiesis and HSPC subsets (Figure 1D; Table S2\). Additionally, we improved upon other hematopoiesis-focused bone marrow scRNA-seq references11, by capturing the full granulocyte differentiation trajectory by virtue of our sample processing not including density-based isolation of mononuclear cells—a standard clinical tissue banking process which results in granulocyte loss due to their multi-lobated nuclei (*CSF3R*; Figures 1B and S1D).


## 方法概述

F Integrated CellChat - CODEX Interaction Matrix CellChat/ CODEX Correlation Metric CellChat/ E CODEX Effect Size 0.5 0.4 0.3 0.2 0.1 0.0 Target Cell Type (legendonnextpage) 10 Cell187,1–21,June6,2024 Pleasecitethisarticleinpressas:Bandyopadhyayetal.,Mappingthecellularbiogeographyofhumanbonemarrownichesusingsingle-cell transcriptomicsandproteomicimaging,Cell(2024), ll Resource OPENACCESS asfrequentlossofbonetissue,wewereabletoidentifypara- erythroblasticislands,aswellasnovelneighborhoodssuchas trabecular cells with non-hematopoietic expression profiles one neighborhood of peri-arteriolar lymphoid cells (Figures 5A that we termed ‘‘endosteal.’’ Neither Osteo-MSCs nor Fibro- andS7C).

## 讨论与结论

We report the most comprehensive healthy human bone marrow reference to date, covering both hematopoietic and non-hematopoietic cell types and their spatial organization. We found that the bone marrow microenvironment contains at least six mesenchymal subsets, two endothelial cell subsets, and one vascular smooth muscle population. Our data clearly demonstrate the limitations of bone marrow aspirates as a sample source, where Adipo-MSCs are heavily favored and subsets like Fibro-MSCs are not captured at all.13,16–18 We identified markers to sort MSC subpopulations and pinpointed the rare Podoplanin+ Fibro-MSCs as the closest to the ISCT-defined mesenchymal stem cell. By contrast, Adipo- and THY1+ MSCs were found to be the most interactive with hematopoietic cells and not part of the endosteal signaling module. Adipo-, THY1+, Osteo-, Fibro-, and APOD+ MSCs also had significantly different profiles of support factor expression. These findings collectively demonstrate the utility of our atlas for understanding differential functions of MSC subsets.

We elucidated the spatial organization of the human bone marrow on a systematic, single-cell level. While recent studies have assessed human bone marrow organization using 7-color immunofluorescence, our work more deeply dissected the cellular differentiation continua of both hematopoietic and nonhematopoietic lineages by virtue of our 53-antibody panel. Our healthy atlas captured the spatial relationships of 32 cell types with respect to each other and to many manually annotated, difficult to segment cell types/structures. This atlas links mesenchymal heterogeneity on the transcriptional level to discrete spatial phenotypes *in situ*, for instance in the case of more central Adipo-/THY1+ versus endosteal Osteo-/Fibro-MSCs. Our spatial findings were generalizable across anatomic sites as well, as our observations in femoral head bone marrow were closely recapitulated in negative lymphoma staging marrows from iliac crest.


## 关键词

Mapping, biogeography, bone, cellular, human

## 相关实体

细胞类型: AML, progenitor
方法: scRNA-seq, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
