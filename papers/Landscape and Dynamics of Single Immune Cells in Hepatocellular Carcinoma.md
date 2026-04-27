---
marker_extracted: true
title: "Landscape and Dynamics of Single Immune Cells in Hepatocellular Carcinoma"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/landscape-and-dynamics-of-single-immune-cells-in-hepatocellular-carcinoma.md]
confidence: medium
year: 2019
---

# Landscape and Dynamics of Single Immune Cells in Hepatocellular Carcinoma

> 原文: [[landscape-and-dynamics-of-single-immune-cells-in-hepatocellular-carcinoma]]

## 摘要

d Pairedligand-receptoranalysesimplicatetheregulationof lymphocytesbyLAMP3+DCs d Macrophagesubsetsintumorsshowdistinctstatesand potentialstoegresstoascites Zhangetal.,2019,Cell179,829–845 October31,2019ª2019ElsevierInc. Article Landscape and Dynamics of Single Immune Cells in Hepatocellular Carcinoma QimingZhang,1,14YaoHe,2,14NanLuo,3,4,14ShashankJ.Patel,5YanjieHan,1RanranGao,1MadhuraModak,6 SebastianCarotta,7ChristianHaslinger,8DavidKind,8GregoryW.Peet,5GuojieZhong,1ShuangjiaLu,1WeihuaZhu,9 YileiMao,10MengmengXiao,11MichaelBergmann,12XuedaHu,1SidP.Kerkar,5AnneB.Vogt,13StefanPflanz,6 KangLiu,5,*JirunPeng,3,4,*XianwenRen,1,*andZeminZhang1,2,15,* 1BIOPIC,BeijingAdvancedInnovationCenterforGenomics,SchoolofLifeSciences,PekingUniversity,Beijing100871,China 2Peking-TsinghuaCenterforLifeSciences,AcademyforAdvancedInterdisciplinaryStudies,PekingUniversity,Beijing100871,China 3DepartmentofSurgery,BeijingShijitanHospital,CapitalMedicalUniversity,Beijing100038,China 4NinthSchoolofClinicalMedicine,PekingUniversity,Beijing100038,China 5DepartmentofCancerImmunologyandImmuneModulation,BoehringerIngelheimPharmaceuticals,Inc.,900RidgeburyRoad,Ridgefield, CT06877,USA 6DepartmentofCancerImmunologyandImmuneModulation,BoehringerIngelheimPharma,BirkendorferStr.65,88400Biberach,Germany 7DepartmentofCancerCellSignaling,BoehringerIngelheimRCVGmBH&CoKG.,Dr.

## 背景与目的

Liver cancer is the third leading cause of cancer-related mortality in the world (Forner et al., 2018), and hepatocellular carcinoma (HCC) accounts for approximately 90% of the incidence of all liver cancers \(Bray et al., 2018\). Although treatments with sorafenib and regorafenib lead to a modest survival benefit, overall anti-tumor responses are still limited (Llovet et al., 2008; Ray, 2017\). Although immunotherapies have clinical benefits for other cancer indications, the response rates in HCC are much lower \(El-Khoueiry et al., 2017\). Because parameters of the immune contexture have been associated with treatment efficacy \(Gnjatic et al., 2017), it is important to characterize the baseline HCC immune milieu to clarify the composition and property of tumor-infiltrating immune cells in comparison with ones in other immune-relevant anatomical compartments.

The cellular components of the tumor microenvironment (TME) are highly complex, with diverse populations of myeloid cells and lymphocytes playing important roles in inflammation, cancer immune evasion, and responses to immunotherapy treatment \(Hackl et al., 2016; Ringelhan et al., 2018). The presence of myeloid cells in the TME is often linked to altered patient survival \(Engblom et al., 2016). Tumor-associated macrophages (TAMs) have been reported to prevent T cells from recognizing and killing cancer cells \(Peranzoni et al., 2018; Engblom et al., 2016; Georgoudaki et al., 2016\). Conventional dendritic cell (DC) subsets (cDC1 and cDC2) have been reported to migrate into tumor-draining LN and prime CD8<sup>+</sup> or CD4<sup>+</sup> T cells in mouse models (Binnewies et al., 2019; Salmon et al., 2016\). However, the characteristics and functions of TAM and DC subsets in HCC patients are still poorly understood. We have previously characterized T cells in HCC by single-cell RNA sequencing (scRNA-seq) (Zheng et al., 2017a\), but the global immune landscape is still unknown.


## 主要发现

#### High-Resolution Immune Landscape of HCC by Integrated Analysis of Full-Length and 3 scRNA-Seq

To characterize the immune cells in HCC, we applied scRNA-seq methods to study CD45<sup>+</sup> cells isolated from tumors and four immune-relevant sites (adjacent liver, hepatic LNs, blood, and ascites) of 16 treatment-naive liver cancer patients (Figures S1A–S1C; Tables S1 and S2). For patient DSN09, both 10x Genomics and SMART-seq2 methods were applied in parallel, giving us the opportunity to evaluate the power of integrated analysis on two types of datasets. Using graph-based clustering \(Traag et al., 2019) to analyze the cells from this patient, we identified 20 clusters for 10x data and 22 for SMART-seq2 \(Figure 1A). Examination of canonical marker genes revealed major cell populations, including T cells, natural killer (NK) cells, and diverse myeloid-lineage cells in both platforms (Figures S1D and S1E), demonstrating the stability and accuracy of our data. Minor cell populations, though, varied between the two platforms. For instance, the *LAMP3*<sup>+</sup> DC, *CD14*<sup>+</sup> , and *FCGR3A*<sup>+</sup> monocyte groups were only identified in SMART-seq2, whereas type 3 innate lymphoid cells (ILCs) were only captured by 10x \(Figure 1A). In addition, we observed that SMART-seq2 could help distinguish closely related clusters, possibly by capturing more RNA molecules that contribute to cell type classification (Svensson et al., 2017\). For instance, *CD4*<sup>+</sup> and *CD8*<sup>+</sup> T cell subtypes (*CD8*<sup>+</sup> *PDCD1*<sup>+</sup> , *CD8*<sup>+</sup> *GZMK*<sup>+</sup> , and *CD8*<sup>+</sup> *CX3CR1*<sup>+</sup> clusters) were readily separated. In contrast, 10x-based T cell clusters were composed of a mixture of *CD4*<sup>+</sup> and *CD8*<sup>+</sup> T cells, as evidenced by their simultaneous similarities to those defined by SMART-seq2 (Figure S2A). We then integrated the two types of datasets using the Harmony algorithm (Korsunsky et al.


## 方法概述

(CD4-c3-IL-7R and CD4-c4-TCF7), effector memory T cells associatedwithasurvivaldisadvantageinbothLIHCandlung (CD8-c4-SELLandCD8-c5-GZMK),Texcells,Tregcells,andpro- cancer,suggestingthistypeoftumor-infiltratingTAMsasapo- liferativeTcells (Figures 7E and S7B), suggestingthatLAMP3+ tential cellular candidate for therapeutic targeting in multiple DCsmayemploytheCD274/PDCD1LG2-PDCD1axistoregulate typesofcancers.TAM-likemacrophagesinHCCtumorshighly multipletypesofTcells.MulticolorIHCstainingofHCCtumors express two marker genes, SLC40A1 and GPNMB. SLC40A1 also showed the physical juxtaposition of PD-1-expressing encodesferroportin,anironexporter,andregulatesTLR-stim- T cells (CD3+CD4+ or CD3+CD8+) and PD-L1-expressing ulus-inducedpro-inflammatorycytokines,includingIL-6,IL-23, LAMP3+DCs(CD80+)(Figures7FandS7D).Basedonanalysis andIL-1b,consistentwithrecentfindingsofironmetabolismin of 366 TCGA HCC patients, the LAMP3+ DC gene signature apolarizingmacrophagephenotypeintheTME(Mertensetal., showed a modest correlation with cytotoxic T cells (R = 0.26, 2017;Moraetal.,2019).Basedonourobservations,wehypoth- p < 1e(cid:2)07, Pearson’s correlation) but strong correlations with esizethatironmetabolismisinvolvedinshapinginnateimmunity Texcells(R=0.51,p<2.2e(cid:2)16)andTregcells(R=0.44,p< intheTME,butthemechanisticdetailsneedfurtherstudy. 2.2e(cid:2)16)(Figures7DandS7C).

## 讨论与结论

Advanced cancer is a systemic disease, and the dynamic response of the immune system at different sites in cancer

remains to be completely deciphered. Here we generated transcriptome data by the combination of 10x Genomics and SMART-seq2, covering more than 75,000 individual CD45<sup>+</sup> cells of 16 liver cancer patients from multiple immune-relevant tissue sites, providing a rich resource for understanding multi-dimensional characterization of immune cells in HCC. Transcriptome profiling, when augmented by analyses of RNA velocity, mitochondrial mutation-based lineage tracing, and L-R based cell-cell interaction, can lead to a far more dynamic picture, illustrating how various myeloid cells develop within the tumor, cross-talk with lymphocytes, and migrate to LNs or ascites.

Macrophages in tumors have been studied in lung cancer and breast cancer using scRNA-seq data (Azizi et al., 2018; Lavin et al., 2017). Here we identified two distinct macrophage states enriched in HCC tumor tissues. TAM-like macrophages in HCC highly resemble the TAMs identified in lung cancer (Lavin et al., 2017), and enrichment of TAM gene signatures is significantly associated with a survival disadvantage in both LIHC and lung cancer, suggesting this type of tumor-infiltrating TAMs as a potential cellular candidate for therapeutic targeting in multiple types of cancers. TAM-like macrophages in HCC tumors highly express two marker genes, SLC40A1 and GPNMB. SLC40A1 encodes ferroportin, an iron exporter, and regulates TLR-stimulus-induced pro-inflammatory cytokines, including IL-6, IL-23, and IL-1β, consistent with recent findings of iron metabolism in a polarizing macrophage phenotype in the TME (Mertens et al., 2017; Mora et al., 2019). Based on our observations, we hypothesize that iron metabolism is involved in shaping innate immunity in the TME, but the mechanistic details need further study.

Although much attention has been focused on cDCs (Azizi et al., 2018; Chevrier et al.


## 关键词

Carcinoma, Cells, Dynamics, Hepatocellular, Immune, Landscape, Single

## 相关实体

方法: scRNA-Seq, scRNA-seq
疾病: Carcinoma, cancer

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
