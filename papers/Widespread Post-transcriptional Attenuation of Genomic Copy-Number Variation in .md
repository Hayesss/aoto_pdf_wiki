---
marker_extracted: true
title: "Widespread Post-transcriptional Attenuation of Genomic Copy-Number Variation in Cancer"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/widespread-post-transcriptional-attenuation-of-genomic-copy-number-variation-in.md]
confidence: medium
year: 2017
---

# Widespread Post-transcriptional Attenuation of Genomic Copy-Number Variation in Cancer

> 原文: [[widespread-post-transcriptional-attenuation-of-genomic-copy-number-variation-in]]

## 摘要

Cell Systems Article Widespread Post-transcriptional Attenuation of Genomic Copy-Number Variation in Cancer EmanuelGonc¸alves,1AthanassiosFragoulis,3LuzGarcia-Alonso,1ThorstenCramer,3,4,5JulioSaez-Rodriguez,1,2,* andPedroBeltrao1,6,* 1EuropeanMolecularBiologyLaboratory,EuropeanBioinformaticsInstitute(EMBL-EBI),WellcomeGenomeCampus,Cambridge CB101SD,UK 2RWTHAachenUniversity,FacultyofMedicine,JointResearchCentreforComputationalBiomedicine,52057Aachen,Germany 3MolecularTumorBiology,DepartmentofGeneral,VisceralandTransplantationSurgery,RWTHUniversityHospital,Pauwelsstraße30, 52074Aachen,Germany 4NUTRIMSchoolofNutritionandTranslationalResearchinMetabolism,MaastrichtUniversity,Maastricht,theNetherlands 5ESCAM–EuropeanSurgeryCenterAachenMaastricht,GermanyandtheNetherlands 6LeadContact SUMMARY ficationsandotherCNVsarethoughttobedetrimentaldueto changes in gene expression that cause an imbalance to the Copy-number variations (CNVs) are ubiquitous in cell.Infemales,oneofthetwoXchromosomesisinactivated cancerandoftenactasdriverevents,buttheeffects byaspecializedRNA-basedsilencingmechanism(Avnerand ofCNVsontheproteomeoftumorsarepoorlyunder- Heard, 2001; Lyon, 1961), but such a mechanism does not stood.

## 背景与目的

Cancer development is driven by the acquisition of somatic genetic variation that includes point mutations, copy-number variations (CNVs), and large chromosome rearrangements or duplications (i.e., aneuploidy) ([Beroukhim et al., 2010\)](#page-11-0). These events can result in a fitness advantage and cancer progression, but they are most often detrimental to cellular fitness. While somatic gene amplification of key oncogenes such as MYCN, AKT2, ERBB2, and others [\(Santarius et al., 2010\)](#page-12-0) can drive cancer development, germline CNVs are rare and are under negative selection [\(Itsara et al., 2009](#page-12-0)). Gene amplifications and other CNVs are thought to be detrimental due to changes in gene expression that cause an imbalance to the cell. In females, one of the two X chromosomes is inactivated by a specialized RNA-based silencing mechanism [\(Avner and](#page-11-0) [Heard, 2001; Lyon, 1961](#page-11-0)), but such a mechanism does not exist for gene-dosage imbalances in the autosomal chromosomes. Protein and mRNA abundance measurements in models of aneuploidy in yeast and human cells have shown that most autosomal gene duplications are propagated to the protein level, with the notable exception of protein complex subunits that showed attenuated (i.e., less than expected) changes in protein abundance [\(Dephoure et al.,](#page-12-0) [2014; Stingele et al., 2012](#page-12-0)). In yeast aneuploid strains, the discrepancy between gene copy-number and protein abundance has been shown to be mostly due to control of protein abundance by degradation ([Dephoure et al., 2014](#page-12-0)). For protein complexes in particular, this observation fits with a model where subunits are degraded when free from the complex [\(Abovich et al., 1985](#page-11-0)). Given that not all subunits were observed to be attenuated, it has been hypothesized that these non-attenuated subunits could act as scaffolding proteins or be rate-limiting for the assembly of the complex ([D


## 主要发现

### Tumor Pan-cancer Proteomics Reveals Attenuation of Copy-Number Alterations in Protein Complex Subunits

To study the implication of gene-dosage changes on the proteome of cancer cells we compiled and standardized existing datasets made available by the TCGA and CPTAC consortia, comprising three different cancer types: breast (BRCA) [\(Cancer Genome Atlas Network, 2012b; Mertins et al., 2016\)](#page-12-0), high-grade serous ovarian (HGSC) ([Cancer Genome Atlas](#page-12-0) [Research Network, 2011; Zhang et al., 2016](#page-12-0)), and colon and rectal (COREAD) [\(Cancer Genome Atlas Network, 2012a;](#page-12-0) [Zhang et al., 2016\)](#page-12-0) ([Figure 1](#page-3-0)A). These datasets provide molecular characterization of gene CNVs, gene expression, and protein abundance of solid tumor samples of 282 patients for which clinical information is also available [\(Figure 1](#page-3-0)A, Table S1).

Current methods can reliably measure the complete expressed transcriptome, but measuring the total proteome is still a challenge with current techniques only providing partial snapshots ([Nagaraj et al., 2011](#page-12-0)). Thus, we quantified the fraction of expressed transcripts measured in the proteomics experiments in each tumor sample [\(Figure 1](#page-3-0)B) (see the [STAR](#page-14-0) [Methods\)](#page-14-0). COREAD samples displayed the lowest average coverage of the expressed transcriptome (22.3%) compared with the coverage measured for the HGSC (42.0%) and BRCA (56.1%) samples. The proteomics experiments were not conducted using the same methodologies, and therefore it is crucial to take into consideration potential confounding effects. In particular, the COREAD [\(Zhang et al., 2014](#page-13-0)) quantifications were done with a label-free approach, while the HGSC and BRCA were quantified using isobaric labeling [\(Mertins et al., 2016; Zhang et al., 2016\)](#page-12-0). To ensure comparable measurements among datasets we removed confounding and systematic ef


## 方法概述

Ashburner,M.,Ball,C.A.,Blake,J.A.,Botstein,D.,Butler,H.,MichaelCherry, ments(ThompsonandCompton,2011),andthesecanpossibly J., Davis, A.P., Dolinski, K., Dwight, S.S., Eppig, J.T., et al. (2000). Gene provideinsightsintotheirfunctionalimplicationsandhopefully ontology:toolfortheunificationofbiology.Nat.Genet.25,25–29. opennoveltherapeuticopportunities. Avner,P.,andHeard,E.(2001).X-Chromosomeinactivation:counting,choice andinitiation.Nat.Rev.Genet.2,59–67. STAR+METHODS Bailey Blackburn, J.,Pokrovskaya, I.,Fisher,P., Ungar, D.,and Lupashin, V.V.(2016).COGcomplexcomplexities:detailedcharacterizationofacom- pletesetofHEK293TcellslackingindividualCOGsubunits.Front.CellDev. Detailedmethodsareprovidedintheonlineversionofthispaper Biol.4,23. andincludethefollowing: Battle,A.,Khan,Z.,Wang,S.H.,Mitrano,A.,Ford,M.J.,Pritchard,J.K.,and Gilad,Y.(2015).Genomicvariation.ImpactofregulatoryvariationfromRNA d KEYRESOURCESTABLE toprotein.Science347,664–667. d CONTACTFORREAGENTANDRESOURCESHARING Beroukhim,R.,Mermel,C.H.,Porter,D.,Wei,G.,Raychaudhuri,S.,Donovan, d EXPERIMENTALMODELANDSUBJECTDETAILS J.,Barretina,J.,Boehm,J.S.,Dobson,J.,Urashima,M.,etal.(2010).Theland- d METHODDETAILS scapeofsomaticcopy-numberalterationacrosshumancancers.Nature463, B CellLinesDrugResponseAnalysis 899–905. B shRNADeliveryviaLentiviralTransduction Boyle,E.A.,Li,Y.I.,andPritchard,J.K.(2017).Anexpandedviewofcomplex B WesternBlotValidation traits:frompolygenictoomnigenic.Cell169,1177–1186.

## 讨论与结论

### Gene-Dosage Changes Are Attenuated for 23%–33% of Proteins

We aimed here to study the extent by which gene dosage is attenuated in cancer at the protein level and what are the mechanisms that govern this process. We observed that, while CNVs have on average a good agreement with transcript measurements, 23%–33% of the proteins undergo post-transcriptional regulation, which attenuates the impact of CNVs ([Figures 1C](#page-3-0) and 1D). We cannot rule out the possibility that some of the apparent protein level attenuation may be due to higher measurement error in the protein abundance relative to the gene expression measurements. However, this is not expected to alter the ranking of proteins from strongest to weakest attenuation as shown by the replication with the cell line data [\(Figure 2](#page-4-0)C). The identification of attenuated proteins alone is very relevant for the identification of causal genes within amplified genome regions. Since copy-number changes are buffered and not observed at the protein level, these are therefore less likely to be drivers of cancer progression and similarly less likely to explain changes in drug associations. Notably, this attenuation was more pronounced in protein subunits and complexes, in agreement with previous observations [\(Dephoure et al., 2014;](#page-12-0) [Stingele et al., 2012](#page-12-0)). This is likely explained by the fact that the stoichiometry of complexes needs to be preserved, and that proteins over-represented compared with other members of the complex are likely degraded due to increased instability [\(McShane et al., 2016](#page-12-0)). Furthermore, we observed that proteins with stronger attenuation are more quickly ubiquitinated [\(Kim](#page-12-0) [et al., 2011](#page-12-0)) [\(Figure 2](#page-4-0)D), suggesting that the attenuation may be mostly driven by changes in degradation instead of translation rates. In line with this, it has been shown, in time-series

<span id="page-10-0"></span>Figure


## 关键词

Attenuation, Cancer, Copy-Number, Genomic, Post-transcriptional, Variation, Widespread

## 相关实体

疾病: Cancer, Tumor, cancer

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
