---
marker_extracted: true
title: "Deciphering early human pancreas"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/deciphering-early-human-pancreas.md]
confidence: medium
year: 2023
---

# Deciphering early human pancreas

> 原文: [[deciphering-early-human-pancreas]]

## 摘要

entiationinmiceandonlyasinglephaseinhumans13,26. largenumberofEPsandendocrinecellsweregeneratedafterPCW8 Single-cell RNA sequencing (scRNA-seq) and single-cell assay (Fig. 1c). The expression patterns of the top 100 differentially fortransposaseaccessiblechromatinsequencing(scATAC-seq)are expressedgenes(DEGs)ineachclusterwerevisualizedinaheatmap, powerful tools that have already been applied in developmental with TFs highlighted (Fig. 1d, Supplementary Fig. 2d and Supple- biology.Recentstudiesinmiceandhumanshaverevealedthecel- mentaryData2).GATA4-andFOXA2-positiveMPcellscouldbedivi- lular composition, molecular heterogeneity and developmental dedintotwogroups;thedorsalMPcellsexpressedNR2F1,whilethe trajectory of pancreatic cells in fetuses at the single-cell ventralMPcellsexpressedTBX3(Fig.1d,e,SupplementaryFig.2d,e). resolution27–36. However, due to the scarcity of human embryo WepresenttheanalysesofthedorsalandventralMPcellsinlater samplesandthedifficultyofpancreasisolationfromearlyembryos, sections.Earlytip,tip,andacinarcellsexpressedincreasinglevelsof littleisknownaboutthemolecularfeaturesandregulatorynetwork CPA2,RBPJLandCTRB2(Fig.1e,SupplementaryFig.2d,e).Theacinar ofearlypancreaticdevelopmentinhumans,especiallybeforepost- cellsexpressingCLPSandCTRB1,whichmainlyappearedinPCW11, conceptionweek(PCW)8. didnotshowtheexpressionofanyamylase-associatedgenes(Fig.1c, Here, we performed scRNA-seq of human embryonic pancreas Supplementary Fig. 2d, e).

## 背景与目的

mation,tissueprocessing,andscRNA-seqprofilingmethods.PCW,post- thelialcells.Transcriptionfactorsofeachcelltypearelabeledontheright. conceptionweek.bUMAPplotofallsinglecellscoloredbycelltypeandtimepoint eFeatureplotshowingtheexpressionofkeymarkergenesofpancreaticepithelial inpancreaticepithelialcells.UMAPuniformmanifoldapproximationandprojec- cells.fUMAPplotshowingthedevelopmentaltrajectoriesofpancreaticepithelial tion,MP,multipotentprogenitor,EPendocrineprogenitor.cBarplotshowingthe cells.SeealsoSupplementaryFigs.1,2andSupplementaryData1,2. NatureCommunications|( 2023)1 4:5354 3 UMAP_1 Ventralmultipotentprogenitorcellsoriginatefrompancreato- cells were related to pattern specification process, Wnt signaling biliaryprogenitors pathway,neuronprojectiondevelopment,growthfactorstimulusand Other endoderm-derived organ primordia, such as the liver, EHBD glanddevelopment(Fig.2g).RNAvelocityanalysisdemonstratedthat (includinggallbladder)andduodenum,areadjacenttothedorsaland ventralMPandEHBDcellsoriginatedfromPBprogenitors(Fig.2h).We ventralpancreas14,15.Thehepato-pancreato-biliaryorgansystemorigi- alsodepictedthedevelopmentaltrajectoryofPB,EHBD,andventral natesfromacommonventralendodermprogenitorcompartmentin MP cells and calculated the pseudotime for each cell type with mice14.Tofurthercharacterizetherelationshipsbetweentheseorgans, Monocle3 (Supplementary Fig. 3d)37. The results revealed that PB weanalyzedtheepithelialcellsfromtheseorgansinPCW4to5.

## 主要发现

#### Cell diversity of the human pancreas in early development

We collected human embryonic pancreas samples at 8 time points from PCW 4 to 11 from 17 donors, including 6 males and 11 females (Supplementary Data 1). After the digestion of the isolated pancreas, we performed scRNA-seq of all 17 processed samples using the 10x Genomics platform (Fig. [1a](#page-2-0), Supplementary Data 1). In total, 68,714 cells passed the quality control procedures, with an average of 3,000 expressed genes per cell (Supplementary Fig. 1a). Our data showed high similarity among the samples from the same time point (Supplementary Fig. 1b, c). Because PCW 4-6 samples also contained non-pancreatic cells, we analyzed and presented our dataset in two groups for batch correction, dimension reduction and clustering. A total of six major cell-type classes were identified, including epithelial (EPCAM + ), mesenchymal (COL3A1 + ), endothelial (PECAM1 + ), neural (ASCL1 + ), immune (PTPRC + ), and erythroid (HBA1 + ) cells (Supplementary Fig. 1d–h). Our data showed the continuity of cells in the same cell class across different time points (Supplementary Fig. 1i). Mesenchymal cells constituted the majority of both two datasets, and their proportion differed more obviously between PCW 4-6 and PCW 7-11 owing to the different sample isolation methods (Supplementary Fig. 1h, i). From PCW 7 to 11, the proportion of mesenchymal cells gradually decreased, while epithelial and other classes of cells increased (Supplementary Fig. 1i).


## 方法概述

#### Sample collection

The research complies with all relevant ethical regulations and guidelines. With approval from the Ethics Committee of The First Affiliated Hospital of Hainan Medical University (certificate #201901) and informed consent from the patients taking voluntary abortions, we acquired pancreas from human embryos in PCW 4-11.

The PCW of the embryos was determined by combining gestational age information, ultrasound assessments and anatomical features of the embryos according to the guidelines (Supplementary Data 1[\)75](#page-15-0)–[77.](#page-15-0) In PCW 4-6, the GI tract part beneath the stomach and above the duodenum was dissected to include both the dorsal and ventral pancreas. In PCW 7-11, when the dorsal and ventral pancreas merged and the pancreas became distinct, the developing pancreas was separated, and as much of the surrounding mesenchyme was removed as much as possible. The dissected tissues were processed as appropriate for the subsequent experiments.


## 讨论与结论

In this study, we present an extensive analysis of the single-cell transcriptomic and chromatin accessibility profiles of human embryonic pancreas samples from the first trimester. The pancreas arises from both the dorsal and ventral endoderm domains, but it is not clear how the two parts contribute to the pancreas development. We first identified dorsal and ventral MP cells in humans and identified two new marker genes of these cells, NR2F1 (dorsal) and TBX3 (ventral). These results are similar to those of previous studies involving laser capture and deep sequencing in the human early dorsal pancrea[s60](#page-14-0). In contrast to mouse pancreas development, there is only a single phase of NEU-ROG3 expression and endocrine differentiation after PCW 8 in the human pancreas[,26.](#page-14-0) It might be that TFs related to endocrinogenesis, such as RFX6 and NEUROG3, were expressed in mouse MP-early cell[s27](#page-14-0) but were not detected in our MP cells (Fig. d). The early dorsal pancreas and ventral pancreas receive different signals from adjacent tissues and may have distinct differentiation abilities,[42.](#page-14-0) Our data showed that the Wnt signaling pathway was more involved in dorsal MP cell development. A study in transgene-labeled mice showed that more endocrine cells were generated in the dorsal pancrea[s61](#page-14-0). No significant differences in differentiation potentials between dorsal and ventral MP cells were observed in our data. In addition, these published scRNA-seq datasets also identified intermediate progenitors in the mouse ventral domain, which could generate hepatoblasts, EHBD cells, and pancreatic progenitor[s61](#page-14-0),. We only identified PB progenitors that could differentiate into ventral MP and EHBD cells in our dataset. Our earliest samples were from the CS13 stage, and intermediate progenitors that could also generate hepatoblasts might exist before CS13 in humans.


## 关键词

Deciphering, early, human, pancreas

## 相关实体

细胞类型: all
方法: Single-cell, scRNA-seq, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
