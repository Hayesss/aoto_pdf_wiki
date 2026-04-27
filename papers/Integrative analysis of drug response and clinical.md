---
marker_extracted: true
title: "Integrative analysis of drug response and clinical"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/integrative-analysis-of-drug-response-and-clinical.md]
confidence: medium
year: 2022
---

# Integrative analysis of drug response and clinical

> 原文: [[integrative-analysis-of-drug-response-and-clinical]]

## 摘要

Acutemyeloidleukemia(AML)isacancerofmyeloid-lineagecellswithlimitedtherapeuticoptions.Wepre- viouslycombinedexvivodrugsensitivitywithgenomic,transcriptomic,andclinicalannotations foralarge cohort of AML patients, which facilitated discovery of functional genomic correlates. Here, we present a datasetthathasbeenharmonizedwithourinitialreporttoyieldacumulativecohortof805patients(942spec- imens).Weshowstrongcross-cohortconcordanceandidentifyfeaturesofdrugresponse.Further,decon- volutingtranscriptomicdatashowsthatdrugsensitivityisgovernedbroadlybyAMLcelldifferentiationstate, sometimesconditionallyaffectingothercorrelatesofresponse.Finally,modelingofclinicaloutcomereveals asinglegene,PEAR1,tobeamongthestrongestpredictorsofpatientsurvival,especiallyforyoungpatients. Collectively,thisreportexpandsalargefunctionalgenomicresource,offersavenuesformechanisticexplo- rationanddrugdevelopment,andrevealstoolsforpredictingoutcomeinAML. INTRODUCTION in the United States (Jemal et al., 2010; SEER, 2021). Genetic features include 16 recurrent gene rearrangements and a Acute myeloid leukemia (AML) is characterized by neoplastic plethora of unique, tumor-specific aberrations (Arber et al., proliferationofmyeloid-lineagecells.Approximately21,000di- 2016).Inaddition,(cid:1)60genesexhibitrecurrentpointmutations agnosesand10,000AML-relateddeathsarereportedannually with many thousand additional rarely mutated genes (Cancer 850 CancerCell40,850–864,August8,2022ª2022TheAuthor(s).PublishedbyElsevierInc.

## 背景与目的

Acute myeloid leukemia (AML) is characterized by neoplastic proliferation of myeloid-lineage cells. Approximately 21,000 diagnoses and 10,000 AML-related deaths are reported annually in the United States (Jemal et al., 2010; SEER, 2021). Genetic features include 16 recurrent gene rearrangements and a plethora of unique, tumor-specific aberrations (Arber et al., 2016). In addition, 60 genes exhibit recurrent point mutations with many thousand additional rarely mutated genes (Cancer

Division of Bioinformatics and Computational Biology, Department of Medical Informatics and Clinical Epidemiology, Oregon Health & Science University, Portland, OR 97239, USA

Knight Cancer Institute, Oregon Health & Science University, Portland, OR 97239, USA

Division of Hematology & Medical Oncology, Department of Medicine, Oregon Health & Science University, Portland, OR 97239, USA

Department of Cell, Developmental & Cancer Biology, Oregon Health & Science University, Portland, OR 97239, USA

Department of Molecular & Medical Genetics, Oregon Health & Science University, Portland, OR 97239, USA

Division of Oncologic Sciences, Department of Medicine, Oregon Health & Science University, Portland, OR 97239, USA

Oregon Clinical and Translational Research Institute, Oregon Health & Science University, Portland, OR 97239, USA

Division of Hematology, Department of Internal Medicine, James Cancer Center, Ohio State University, Columbus, OH 43210, USA 9Integrated Genomics Laboratory, Oregon Health & Science University, Portland, OR 97239, USA

Division of Hematology and Oncology, Department of Pediatrics, Oregon Health & Science University, Portland, OR 97239, USA

Department of Molecular Microbiology and Immunology, Oregon Health & Science University, Portland, OR 97239, USA

Department of Hematology and Hematopoietic Stem Cell Transplant, City of Hope National Medical Center, Duarte, CA 91010, USA

Astex Pharmaceuticals, Cambridge, CB4 0QA, UK

Biostatistics Shared Resource, Oregon...


## 主要发现

To better understand the factors governing AML drug response and clinical outcome, we developed a comprehensive platform to combine clinical, cellular, and molecular features of disease. Our complete Oregon Health & Science University (OHSU) Beat AML cohort represents sample collection and characterization over a span of 10 years with integration of ex vivo drug sensitivity testing, curation of clinical annotations, and DNA and RNA sequencing (RNA-seq). The data in Tyner et al. (2018) represent the first tranche of patient sample data (denoted as waves 1 + 2). Here, we provide additional longitudinal samples for waves 1 + 2, updated clinical information, as well as additional patient accrual, which represents the final two waves (waves 3 + 4). Waves 3 + 4, collected over a 2.5-year period, comprise a total of 293 specimens from 279 patients (243 patients unique to waves 3 + 4). We also provide the harmonization of these datasets together, for a cumulative cohort of 942 specimens from 805 patients, which reflects a real-world cohort of AML cases, inclusive of de novo, transformed, and therapy-related AML as well as cases at the point of initial diagnosis (70% of cases) and smaller numbers with relapsed or residual disease. A full listing of samples, available data, and clinical annotations are in Table S1. All somatic variant calls, gene expression counts, and drug response data can be explored and visualized through our interactive browser, Vizome (vizome.org/aml2). For all cohort-level analyses, only specimens from the first timepoint of each patient were used (defined in Table S1), with all remission samples excluded. A broad overview of clinical data showed comparable features between the two datasets with only a slightly lower percentage of cases with de novo AML in the first dataset (49% in waves 1 + 2 versus 58% in waves 3 + 4). Frequencies of the most commonly mutated genes were also equivalent between cohorts (Figure 1A).


## 方法概述

sistedwithcurationandentryofpatientclinicalannotations.E.B.,H.H.,J.R., tending immunopharmacology content and introducing the IUPHAR/MMV M.L., R. Schuff, and A.Y. assisted with clinical data integration from the GuidetoMALARIAPHARMACOLOGY.NucleicAcidsRes.48,D1006–D1021. OHSU Research Data Warehouse. A.Y. integrated the ex vivo workflow in AvilaCobos,F.,Vandesompele,J.,Mestdagh,P.,andDePreter,K.(2018). theBeatAMLdatabase. Computationaldeconvolutionoftranscriptomicsdatafrommixedcellpopula- C.R.C.servedasaco-investigatorontherepositoryprotocol,obtainedcon- tions.Bioinformatics34,1969–1979. sentandcollectedsamplesfrompatients,processedandshippedspecimens, Barbie,D.A.,Tamayo,P.,Boehm,J.S.,Kim,S.Y.,Moody,S.E.,Dunn,I.F.

## 讨论与结论

The impact of AML LSCs on tumor biology and therapeutics has been explored and suggested to prime disease pathogenesis and seed relapse. However, a broader and more nuanced understanding of the full range of AML tumor cell maturation states, and the way in which these different cell states are tied to other disease features such as genetics and drug response, has been lacking. While some of these maturation states were roughly captured in the historical FAB classification system for AML, this system has been all but abandoned in current classification schemes that utilize primarily (or only) genetics and prior clinical history (Arber et al., 2016; Dohner et al., 2017). In addition, while targeting of LSCs has been a major goal for AML research with the notion that eliminating LSCs would induce tumor collapse, this result has proved elusive with the observation that relapse can be seeded by more mature cells, depending on the administered therapy. Through broad mapping of distinct AML cell maturation states with both genetic features and response to broad families of drugs, we find that tumors can display features of multiple, disparate cell maturation states and that a majority of drugs and drug families exhibit cell maturation state-biased response. Our expansive modeling of clinical outcome has also led to a single, targetable gene that is a strong determinant of overall survival in AML, PEAR1.

Figure 5. Drug family response is influenced by and conditional on cell type

(A) Similar to the analysis of single-inhibitor responses and their correlation with cell-type score, shown in Figure 3A, we can group the drug families from Figure 4 by their association with cell-type differentiation scores based on their Pearson's correlation (BY FDR <0.05; Benjamini and Yekutieli, 2001). (B) We can also determine instances where drug family correlation with mutational state is conditional on cell type (as we did for individual drugs in Figure 3B).


## 关键词

Integrative, analysis, clinical, drug, response

## 相关实体

细胞类型: AML
方法: RNA-seq
疾病: disease

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
