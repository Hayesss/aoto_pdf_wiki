---
title: "Transcriptome-wide quantification of double-"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/transcriptome-wide-quantification-of-double.md]
confidence: medium
year: 2021
---

# Transcriptome-wide quantification of double-

> 原文: [[transcriptome-wide-quantification-of-double]]

## 摘要

Double-stranded RNAs (dsRNAs) are abundantly present in cells, playing multiple regulatory functions. dsRNAs of viral origin activate innate immune responses. Since RNA editing and modifications affect the structure and recognition of RNAs, their alteration can result in the accumulation of aberrant endogenous dsRNAs inducing a deleterious innate immune response. Here, we present a complete protocol for the measurement of dsRNAs in a live mouse tissue using dsRNA immunoprecipitation and sequencing (dsRIP-Seq). This pro- tocol focuses on tissue isolation, dsRNA immunoprecipitation and downstream computationalanalysis. For complete details on the use and execution of this protocol, please refer to Gaoetal.(2020). BEFOREYOUBEGIN Timedbreeding Timing:15–20days 1. Timedbreedingtoobtainfetalliver. a. Setupmatingbetweenonemaleandtwofemalemice(8–16weeksold)percageintheafternoon 15–20daysbeforeexperiment.Setupasmanycagesasneededtoobtaindesirednumberoffetal liverspergenotype,takingintoaccountbreedingsuccessformousestrainandseason. b. Checkforvaginalplugeachmorningaftermatinghasbeensetup.Movefemalemousewith plugtoaseparatecage.ThemorningaplugisdetectediscountedasdayE0.5. c. OndayE14.5proceedwithfetalliverisolation.Usually,oneE14.5fetalliverwillyieldapprox- imately30mgRNA((cid:1)40–50millionnucleatedcells),sufficientforasingleexperimentalsample. Isolationofmurinefetallivers Timing:2h 2.

## 背景与目的

multiple regulatory functions. dsRNAs of viral origin activate innate immune responses. Since RNA editing and modifications affect the structure and recognition of RNAs, their alteration can result in the accumulation of aberrant endogenous dsRNAs inducing a deleterious innate immune response. Here, we present a complete protocol for the measurement of dsRNAs in a live mouse tissue using dsRNA immunoprecipitation and sequencing (dsRIP-Seq). This pro- tocol focuses on tissue isolation, dsRNA immunoprecipitation and downstream computationalanalysis. For complete details on the use and execution of this protocol, please refer to Gaoetal.(2020). BEFOREYOUBEGIN Timedbreeding Timing:15–20days 1. Timedbreedingtoobtainfetalliver. a.

## 主要发现

Mouse:Vav-Cre;Mettl3fl/fl (Gaoetal.,2020) N/A Mouse:C57BL/6J Inhousecolony JAX:000664 Softwareandalgorithms STARv2.3.3a N/A edgeR Bioconductor release/bioc/html/edgeR.html FastUniqv1.1 N/A RNAfoldv2.4.11 ViennaRNApackage FastQCv0.11.5 N/A projects/fastqc/ Other TapeStation2200 AgilentTechnologies Cat#G2964AA HiSeq2500SequencingSystem Illumina Cat#SY–401–2501 MATERIALSANDEQUIPMENT dsRIPlysisbuffer Reagent Finalconcentration Volume(100mL) NaCl 100mM 2mL Tirs-HClpH7.4 50mM 5mL MgCl2 3mM 0.3mL IGEPALCA-630 0.5% 0.5mL H2O,RNase-free n/a 92.2mL Total n/a 100mL STARProtocols2,100366,March19,2021 3 ll OPEN ACCESS Protocol Onthedayoftheexperiment,to10mLdsRIPlysisbufferadd0.4mLof253CompleteProteinase Inhibitorand20mLSUPERase,In(cid:2)RNaseInhibitorforimmediateuse;maintainat4(cid:3)C. CRITICAL: The dsRIP lysis buffer can be stored at 4(cid:3)C for one month. Make fresh lysis bufferiflongertimeperiodelapsesbetweenexperiments.

## 方法概述

trt (cid:4)log 2 dsRIP ctrl j>jlog 2 INPUT trt (cid:4)log 2 INPUT ctrl j.Inourworked example,thiscriterionwasnotassociatedwithanedgeRcontrast,thereforeitisnotdependent onapvalue. DownstreamstructuralandfunctionalanalysisofdsRNAs ThepopulationsofrelevantgenesortranscriptswithdsRNAconformationidentifiedbydsRIP-Seq canbefurthercharacterizedwithstructuraloffunctionalcomputationalanalysistools(Figure4). 38. Predictthesecondarystructureoftheidentifiedgenesortranscripts.Inourworkedexample,we usedtheRNAfoldalgorithmcontainedintheViennaRNApackage(v2.4.11)(Lorenzetal.,2011) (see

## 讨论与结论

deeperinthefemalemouse’svagina. Problem InsufficientRNAisisolatedafterdsRNAimmunoprecipitation. Potentialsolution SteriletechniqueandRNAsefreesurfaces,tools,andreagentsarekey.Incubationstepsshouldbe exactly timed. Avoid unnecessary delays between steps. Long-term storage of RNA should be avoided prior to sequencing. A positive control to confirm the dsRNA immunoprecipitation pro- cess is1 mg polyinosinic:polycytidylic acid (pI:pC). 1 mg can be used to monitor and confirm the efficiency of each step, as pI:pC is a well-characterized dsRNA which can be recognized by J2 antibody. Problem ContaminationofphenolafterRNAextractionidentifiedbyanunexpectedpeakat270nmduring TapeStationsystemqualitycontrolanalysisofisolatedRNAs.

## 关键词

Transcriptome-wide, double, quantification

## 相关实体

暂无识别到特定实体

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
