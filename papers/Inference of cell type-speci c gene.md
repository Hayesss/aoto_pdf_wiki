---
marker_extracted: true
title: "Inference of cell type-speci c gene"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/inference-of-cell-type-speci-c-gene.md]
confidence: medium
year: 2023
---

# Inference of cell type-speci c gene

> 原文: [[inference-of-cell-type-speci-c-gene]]

## 摘要

Results sion model while the others are based on linear models. INDEP is Single-cellMulti-TasklearningNetworkInference(scMTNI)for similar to scMTNI but does not incorporate the lineage prior. Each definingregulatorynetworksoncelllineages algorithm was applied within a stability selection framework and We developed scMTNI, a multi-task graph learning framework for evaluated with Area under the Precision recall curve (AUPR) and inferringcelltype-specificgeneregulatorynetworksfromscRNA-seq F-score oftop k edges,where kisthe number ofedges in the true and scATAC-seqdatasets (Fig. 1a),whereacelltype is definedbya network(Fig.2b,c).Ondataset1,basedonAUPR,scMTNI,MRTLE,and clusterofcellswithadistincttranscriptional,and,ifavailable,acces- AMuSRareabletorecoverthenetworkstructurebetterthantheother sibilityprofile.scMTNImodelsaGRNasaDependencynetwork22,a multi-task learning and single-task learning algorithms (Fig. 2b). probabilistic graphical model with random variables representing Ontogenetperformsbetterthanthesingle-tasklearningalgorithmsin genesandregulators,suchastranscriptionfactors(TFs)andsignaling at least two cell types. Finally, GNAT performs comparably to the proteins. single-tasklearningalgorithms.Whencomparingalgorithmsbasedon scMTNI takes as input cell clusters with gene expression and F-scoreoftopkedges,wehavesimilarobservationsthatscMTNIand accessibilityprofilesand alineagestructure linking thecellclusters MRTLE have a better performance than other algorithms (Fig. 2c).

## 背景与目的

dynamicnetworkanalysismethods:edge-basedk-meansclusteringandLatent stemcellsandmultipotentprogenitors,LMPlymphoid-myeloidprogenitors, DirichletAllocation(LDA)basedtopicmodelstoidentifykeyregulatorsandsub- MEMPMK-erythroid-mastprogenitorscombinedwithcyclingMEMPs,GPgranu- networksassociatedwithaparticularcellclusterorasetofclustersonabranch. locyticprogenitors,Eryerythroidcells,pDCplasmacytoiddendriticcells. cDatasetsusedwithscMTNI.Thesimulationdatacomprisedalineartrajectoryof medicine as well as for generating patient-specific disease models. scMTNI+PriorhadamongthehighestF-scores,highnumberofpre- However, this process is inefficient as a small fraction of cells get dictableTFsandagreatercoverageofthegoldstandardscomparedto reprogrammed to the pluripotent state31. To gain insight into gene competingmethodsusingexpressionalone(SCENIC)aswellasthose regulatory networks that govern the dynamics of this process, we that either incorporated accessibility information (CellOracle, profiledsinglecellaccessibility(scATAC-seq)duringreprogramming INDEP+Prior)orcelllineageinformation(scMTNI). of mouse embryonic fibroblasts (MEFs) to the induced pluripotent Toperformaninitialassessmentofthenetworkdynamicsonthe stateandfourintermediatetimepoints,day3,day6,day9,andday12, celllineage,wecomputedF-scorebetweeneachpairofinferrednet- toconstituteadatasetof6timepoints.WeusedLIGERtointegratethe works defined by the top 4k edges (Fig. 3g). Both scMTNI and scRNA-seqandscATAC-seqdatasets(Fig.

## 主要发现

## Single-cell Multi-Task learning Network Inference (scMTNI) for defining regulatory networks on cell lineages

We developed scMTNI, a multi-task graph learning framework for inferring cell type-specific gene regulatory networks from scRNA-seq and scATAC-seq datasets (Fig. 1a), where a cell type is defined by a cluster of cells with a distinct transcriptional, and, if available, accessibility profile. scMTNI models a GRN as a Dependency network22, a probabilistic graphical model with random variables representing genes and regulators, such as transcription factors (TFs) and signaling proteins.

scMTNI takes as input cell clusters with gene expression and accessibility profiles and a lineage structure linking the cell clusters (Fig. 1\). Such inputs can be obtained from existing methods for integrative clustering and lineage construction24. scMTNI uses the scATAC-seq data for each cell cluster to define cell type-specific sequence motif-based TF-target interactions (e.g., a motif for a particular TF, which is accessible only in specific cell types will result in a TFtarget interaction only in those cell types) which are used as a prior to guide network inference (Methods). scMTNI can also take bulk ATACseq data for corresponding cell types to generate cell type-specific prior networks or cell type-agnostic priors derived from sequencespecific motifs that in turn could be filtered with relevant ATAC-seq data. scMTNI's multi-task learning framework incorporates a probabilistic lineage tree prior, which uses the lineage tree structure to influence the similarity of gene regulatory networks on the lineage. This lineage tree prior models the change of a GRN from a start state (e.g., progenitor cell state) to an end state (e.g., more differentiated state) as a series of individual edge-level probabilistic transitions. The output of scMTNI is a set of cell type-specific GRNs one for each cell cluster in the lineage tree.


## 方法概述

This research complies with all relevant ethical regulations. Mice used in the reprogramming study were maintained in agreement with our UW-Madison Institutional Animal Care and Use Committee (IACUC) approved protocol (ID M005180-R03).


## 讨论与结论

Single-cell technologies have transformed our ability to study cellular heterogeneity and cell-type specific gene regulation of known and novel cell populations. Defining gene regulatory networks from scRNA-seq data of developmental systems has remained challenging as most existing methods have assumed a static view of the GRN and do not leverage accessibility to inform the GRN structure. To address this need, we developed single-cell Multi-Task Network Inference (scMTNI), a probabilistic graphical model-based approach that uses multi-task learning to infer cell type-specific GRNs on a cell lineage tree by integrating scRNA-seq and scATAC-seq data and model the dynamics of these regulatory interactions on a lineage. A major benefit of the scMTNI framework is its flexibility in incorporating different sources of accessibility information as well as the ability to model dynamics on cell lineages of different topologies. The probabilistic prior-based framework makes scMTNI more robust to noisy or incomplete accessibility data and allows the incorporation of additional regulators such as signaling proteins and TFs with no binding information. Guided by the cell lineage structure, scMTNI's inferred networks exhibit meaningful changes along the trajectory and identify regulators and network components specific to cell populations transitioning to different lineage paths.

Multi-task learning is well-suited for the inference of cell typespecific GRNs. However, a key question is how to implement multi-task learning for GRN inference. A number of multi-task learning algorithms were developed for inferring GRNs and functional networks from bulk transcriptomic data but have not been systematically compared for their effectiveness on single-cell transcriptomic data. Some approaches, such as AMuSR have used a flat hierarchy where all the tasks are considered equally related.


## 关键词

Inference, cell, gene, type-speci

## 相关实体

方法: Single-cell, scRNA-seq

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
