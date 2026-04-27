---
marker_extracted: true
title: "Integrated Single-Cell Analysis Maps the Continuous Regulatory Landscape of Human Hematopoietic Differentiation"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/integrated-single-cell-analysis-maps-the-continuous-regulatory-landscape-of-huma.md]
confidence: medium
year: 2018
---

# Integrated Single-Cell Analysis Maps the Continuous Regulatory Landscape of Human Hematopoietic Differentiation

> 原文: [[integrated-single-cell-analysis-maps-the-continuous-regulatory-landscape-of-huma]]

## 摘要

5InstituteforStemCellBiologyandRegenerativeMedicine,StanfordUniversitySchoolofMedicine,Stanford,CA94305,USA 6DivisionofHematology,DepartmentofMedicine,StanfordUniversitySchoolofMedicine,Stanford94305,CA,USA 7PrograminEpithelialBiology,StanfordUniversitySchoolofMedicine,Stanford,CA94305,USA 8DepartmentofAppliedPhysics,StanfordUniversity,Stanford,CA94025,USA 9ChanZuckerbergBiohub,SanFrancisco,CA94158,USA 10DepartmentofPathology,MassachusettsGeneralHospital&HarvardMedicalSchool,Boston,MA02115,USA 11DepartmentofBiostatistics,HarvardT.H.ChanSchoolofPublicHealth,Boston,MA02115,USA 12LeadContact SUMMARY ation as a ball rolling down a bifurcating three-dimensional surface(Goldbergetal.,2007;Waddington,1957).Thisdevelop- Humanhematopoiesisinvolvescellulardifferentiation mentallandscapedefinesadescriptivepathacellmightfollow, of multipotent cells into progressively more lineage- choosing different developmental fates as it reaches saddle restricted states. While the chromatin accessibility points that separate different, increasingly restricted, cellular landscape of this process has been explored in states. The shape of this landscape is largely defined by tran- defined populations, single-cell regulatory variation scriptionfactors(‘‘guy-wires’’),whichrecruitchromatineffectors toreconfigurechromatin(CaloandWysocka,2013;Longetal., hasbeenhiddenbyensembleaveraging.

## 背景与目的

In 1957, Conrad Waddington developed an influential analogy for developmental cell biology by conceptualizing cellular differentiation as a ball rolling down a bifurcating three-dimensional surface (Goldberg et al., 2007; Waddington, 1957). This developmental landscape defines a descriptive path a cell might follow, choosing different developmental fates as it reaches saddle points that separate different, increasingly restricted, cellular states. The shape of this landscape is largely defined by transcription factors (''guy-wires''), which recruit chromatin effectors to reconfigure chromatin (Calo and Wysocka, 2013; Long et al., 2016\) and promote new cellular phenotypes (Graf and Enver, 2009; Takahashi and Yamanaka, 2006). These concepts—the first a descriptive notion of development (Figure S1A), and the second a mechanistic description of the molecular actors that drive state changes (Figure S1B)—have provided a conceptual framework for understanding cell fate choices. Recent technological advances in single-cell epigenomic assays \(Kelsey et al., 2017\) now provide the opportunity to ascribe epigenomic features to this landscape by quantifying overall epigenomic similarity of individual cells during a normal differentiation process, as well as the activity of master regulators that influence cell fate decisions.

Hematopoietic differentiation serves as an ideal model for exploring the nature of multipotent cell fate decisions \(Laurenti and Go¨ ttgens, 2018; Orkin and Zon, 2008\). The hematopoietic system is maintained by the activity of a small number of selfrenewing, long-lived hematopoietic stem cells (HSCs) capable of giving rise to the majority of blood cell lineages (Becker et al., 1963; Laurenti and Go¨ ttgens, 2018; Orkin and Zon, 2008\) whereby multipotent cells transit multiple decision points while becoming increasingly lineage-restricted (Figure 1A).


## 主要发现

### Single-Cell Chromatin Accessibility of Distinct Hematopoietic Cell Types

We used FACS to isolate 8 distinct cellular populations from CD34<sup>+</sup> human bone marrow, which included cell types spanning the myeloid, erythroid, and lymphoid lineages \(Figures 1A and 1B). In addition, we also profiled a CD34<sup>+</sup> CD38CD45RA<sup>+</sup> CD123 subset that has not been well characterized \(Manz et al., 2002). Cells analyzed after sorting and cells cryopreserved after sorting provided comparable data quality and yield (Figures S1C–S1E), and therefore we performed all further scATAC-seq measurements on cryopreserved cells (Figure 1C). Together, this sorting strategy captures 97% of all CD34<sup>+</sup> cells (Figure S1F) and using post-sort analysis, we found that sorted cell types were on average 97% pure by cell surface marker immunophenotype (Corces et al., 2016\). Using this approach, we profiled the chromatin accessibility landscapes (CALs) across a total of 30 independent single-cell experiments representing 6 human donors, with each progenitor population assayed from two or more donors (Figure S1G). We did not profile CD34 bone marrow stem cells, as they are rare and less well described \(Matsuoka et al., 2015).

Aggregated single-cell chromatin accessibility profiles closely resemble bulk CD34<sup>+</sup> ATAC-seq profiles (Figures 1D, S1H, and S1I). Including previously published scATAC-seq data from LMPPs and monocytes (Corces et al., 2016), this dataset comprised 3,072 single-cell CALs across 32 integrated fluidic circuits (IFCs). Single-cell profiles were of consistent high-quality with 2,034 cells passing stringent quality filtering, yielding a median of 8,268 fragments per cell with 76% of those fragments mapping to peaks, resulting in a median of 6,442 fragments in peaks per cell (Figure 1E; see STAR Methods).


## 方法概述

0.1 0.1 0 0 high con m f. e l d o . o c p o s nf lo . w lo o c A p o l s l n p f. e l a o k o - p g s ene pairs nosraeP naeM CEBPD expression D 0.3 0.2 0.1 0 <1kb 1-10k 1 b 0-100 1 k 0 b 0kb-1Mb 1-10Mb nosraeP naeM C 0 Max E G 0.5 0.4 0.3 0.2 0.1 0 -2 0 2 4 6 8 10 12 14 Myeloid pseudo-time stnemele yrotaluger elbairav 500,41 seneg elbairav 389,1 Correlate dynamics REs to nearby genes (+/-10Mb) scATAC/RNAcapture correlation HiC ta tnemhcirne noitcaretnI )lav-p 01gol-( sLTQe-sic 0 Max Chromosome 8 S c c h a r8 le : 48,500,000 1 Mb 49,000,000 49,500,000 hg1950,000,000 K1-HSC K2-CMP K9-GMP K10-GMP K11-Mono CD34+_HSPCs CE P B R PD KDC MCM4 EFCAB1 SNAI2 C8 B o C rf 0 2 4 2 2029 KIAA0146 UBE2V2 F 4 3 2 1 0 Expression per cell (L0g2) scATAC-seq scRNA-seq Peak activity HSC mono HSC CMP GMP Mono 2 Early to repress 1 Late to repress 0 Transition peaks Early to activate Late to activate Early to 1 repress 0.5 Late to <0.5 repress Transition expression Early to activate Late to activate nosraeP Figure6. RegulatoryElementDynamicsLinksDistalElementstoGenes (A)FragmentspercellforaCEBPDdistalelementorderedbymyeloidpseudo-time,(top)cellsarecoloredbytheirsortedidentityand(bottom)valuesare smoothed(blue).Errorbars(gray)denotes95%confidenceintervals. (B)cis-RegulatoryandexpressiondynamicsacrossfourregulatoryelementsnearthemyeloidregulatorCEBPD. (C)Accessibility(top)andexpression(bottom)dynamicsacrossmyeloidpseudo-time,rowsaresortedbytheirpeakintensityinthemyeloidtrajectory.

## 讨论与结论

We used single-cell chromatin accessibility and transcriptomic analysis to identify regulatory heterogeneity and continuous differentiation trajectories in early human hematopoiesis by developing a broadly applicable computational framework for analysis of these single-cell data. This framework includes a means for visualizing single-cell chromatin accessibility, and computationally pairing these data with single-cell RNA-seq, by using bulk data as a reference. With this approach, we find that immunophenotypically defined cell populations often flow from one state to another and further we dissociate TF motif activity variability within these populations as correlated or uncorrelated to axis of differentiation. In this effort, we find the activity of TF motifs, such as the GATA motif in HSCs, may represent indicators of lineage priming pulling cells toward different

Figure 6. Regulatory Element Dynamics Links Distal Elements to Genes

- (A) Fragments per cell for a CEBPD distal element ordered by myeloid pseudo-time, (top) cells are colored by their sorted identity and (bottom) values are smoothed (blue). Error bars (gray) denotes 95% confidence intervals.
- (B) cis-Regulatory and expression dynamics across four regulatory elements near the myeloid regulator CEBPD.
- (C) Accessibility (top) and expression (bottom) dynamics across myeloid pseudo-time, rows are sorted by their peak intensity in the myeloid trajectory.
- (D) Regulatory profiles surrounding the CEBPD gene, dynamic enhancers are highlighted in gray with significant (blue) and non-significant (gray) correlated peak-gene pairs shown as loops.
- (E and F) Mean Pearson correlation coefficients binned by (E) genomic distance to the gene and (F) loop confidence. Error bars represent 1 SD on the estimate of the mean.
- (G) p value of enriched peak-gene correlation or promoter capture HiC at *cis*-eQTLs overlapping dynamic enhancers. See also Figure S6.

developmentally committed states.


## 关键词

Analysis, Continuous, Differentiation, Hematopoietic, Human, Integrated, Landscape, Maps, Regulatory, Single-Cell

## 相关实体

细胞类型: all, erythroid, lymphoid, myeloid
通路: Differentiation
方法: FACS, Single-Cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
