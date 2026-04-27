---
marker_extracted: true
title: "A time- and single-cell-resolved model of murine"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/a-time--and-single-cell-resolved-model-of-murine.md]
confidence: medium
year: 2023
---

# A time- and single-cell-resolved model of murine

> 原文: [[a-time--and-single-cell-resolved-model-of-murine]]

## 摘要

Theparadigmatichematopoietictreemodelisincreasinglyrecognizedtobelimited,asitisbasedonhetero- geneous populations largely defined by non-homeostatic assays testing cell fate potentials. Here, we combine persistent labeling with time-series single-cell RNA sequencing to build a real-time, quantitative model of invivotissue dynamicsformurine bonemarrowhematopoiesis.Wecouplecascading single-cell expressionpatternswithdynamicchangesindifferentiationandgrowthspeeds.Theresultingexplicitlink- age between molecular states and cellular behavior reveals widely varying self-renewal and differentiation properties across distinct lineages. Transplanted stem cells show strong acceleration of differentiation at specific stages of erythroid and neutrophil production, illustrating how the model can quantify the impact of perturbations. Our reconstruction of dynamic behavior from snapshot measurements is akin to how a kinetoscopeallowssequentialimagestomergeintoamovie.Wepositthatthisapproachisgenerallyappli- cabletounderstandingtissue-scaledynamicsathighresolution. INTRODUCTION geneous. For instance, common myeloid progenitors (CMPs)4,5 andlymphoid-primedmultipotentprogenitors(LMPPs)6,7arehet- A continuous flow of cells replenishes blood throughout life to erogeneous at functional and RNA level. Further scRNA-seq maintainhematopoietichomeostasis.

## 背景与目的

A continuous flow of cells replenishes blood throughout life to maintain hematopoietic homeostasis. This flow originates from hematopoietic stem cells (HSCs) and progresses through a complex hierarchy of progenitors, collectively called hematopoietic stem and progenitor cells (HSPCs). Decades of research have revealed immunophenotypically defined HSPCs and their fate potentials, thus positioning them within the hematopoietic hierarchy and establishing the hematopoietic tree model. 1,2 Although scRNA-seq introduced high-resolution and resolved HSPC heterogeneity, scRNA-seq typically provides snapshot measurements with limited temporal information. Thus, the hematopoietic tree model, even complemented by scRNA-seq data, remains static and qualitative and does not capture the highly dynamic HSPC biology in real time.

To facilitate real-time modeling of HSPC dynamics, a previous study induced a persistent fluorescent reporter within the HSC compartment and assessed label propagation into progeny by flow cytometry. However, immunophenotyping has limited resolution, and flow-cytometry-defined HSPCs are functionally hetero-

geneous. For instance, common myeloid progenitors (CMPs)<sup>4,5</sup> and lymphoid-primed multipotent progenitors (LMPPs)<sup>6,7</sup> are heterogeneous at functional and RNA level. Further scRNA-seq studies suggested gradual molecular transitions from HSCs toward 8 distinct lineages, <sup>8–10</sup> including specific stages of erythroid differentiation. Nonetheless, although molecular states captured by scRNA-seq can be predictive of progenitor fate potential when assessed *in vitro*, <sup>11–13</sup> gaining insights into single-cell fates *in vivo* during homeostasis has remained more challenging. 

Lineage tracing in non-hematopoietic tissue combined with scRNA-seq has provided insights into progenitor cell differentiation to the airway epithelial lineage.


## 主要发现

## Hoxb5-CreERT2-Tomato reporter tracks HSC differentiation over time

To analyze HSPC dynamics, we aimed to employ a labeling approach (based on principles from Busch et al[.3](#page-14-2) ), in which an inducible HSC-specific CRE excises a STOP cassette in the *Rosa26-LoxP-STOP-LoxP-tdTomato* (*R26LSL-tdTomato*) reporter to permanently label HSCs and their subsequent progeny. We hypothesized that *Hoxb5*, which is specifically expressed in HSCs[,16](#page-15-0) is a suitable driver locus. To validate the specificity of *Hoxb5* expression at the protein level, first we generated *Hoxb5mKO2* mice, where HOXB5 and mKO2 fluorescent reporter expression is driven by the endogenous *Hoxb5* locus ([Figure S1](#page-14-12)A). mKO2 expression was selectively confined to the BM LinSca-1+ c-Kit+ (LSK) HSPC compartment ([Figures S1](#page-14-12)B–S1D, extended data Figure E1A, extended data figures ''E'' are available in Mendeley Data, see [key resources table](#page-17-0)). Although high mKO2 expression was exclusive to the LSKCD48CD150+ HSC fraction and enriched for this population [\(Figures S1B](#page-14-12)–S1D), low-level expression was also detected in LSKCD48CD150 multipotent progenitors (MPPs) [\(Figures S1](#page-14-12)B–S1D). At the functional level, we observed robust long-term multilineage repopulation activity of mKO2+ HSCs upon serial transplantation. Notably, chimerism in the HSC compartment of primary recipients was significantly lower in the mKO2 cohort, and mKO2 HSCs failed to efficiently sustain all lineages in secondary recipients [\(Figures S1E](#page-14-12) and E1B–E1D). Furthermore, scRNA-seq demonstrated that mKO2+ cells express canonical HSC-affiliated genes, display the highest HSC-score (Figures E2A–E2C)[,17](#page-15-1) and tightly occupy the region of the most immature stem cells on high-resolution HSPC landscap[e7](#page-14-6) (Figures E2D–E2F).


## 方法概述

Figure5. Continuousmodelscapturesingle-cellgrowthanddifferentiationratesalongsidetheirmolecularstate (A)Diagramofmegakaryocytetrajectoryanalysis.Followingthearrows:putativecelltransitions(pseudotimekernel)wereusedtoestimatecellfate,fromwhich trajectorywasisolated(dashedline).Alongthepseudotimecelldensitieswerecomputedforeachtimepoint(color-codedlines)andanalyzedusingthe pseudodynamicsframeworkprovidingdifferentiationandnetproliferationrateestimatesforeachcell. (B)(Left)UMAPprojectionoftheHSPClandscapecolor-codedbycellfateprobabilityofneutrophillineage(estimatedwithpseudotimekernel,seeA).Panelson therightshowUMAPprojectionsofisolatedneutrophiltrajectorycolor-codedbyindicatedparametersorgeneexpression.

## 讨论与结论

Quantitative models describing cell differentiation (e.g., Waddington landscape) were conceptualized decades ago.46 However, the generation of dynamic and quantitative abstractions of native hematopoiesis has been hampered by a lack of suitable experimental approaches, particularly reaching single-cell resolution. Here, we report a major effort, combining persistent HSC labeling, time-series scRNA-seq analyses, and mathematical modeling to build a predictive model of in vivo hematopoiesis dynamics. Analogously to the moving images in a kinetoscope, our approach employs multiple high-resolution snapshots of differentiation to reconstruct the real-time cellular flow between single-cell states within the BM multilineage hematopoiesis. Our model describes cell behavior with self-renewal and differentiation rates, which intuitively can be represented as the shape of a Waddington-like landscape (Figure 7). Using this analogy, the discrete model is a set of fixed platforms connected with slides. whereas the continuous model follows the curvature for all observed states (here: single cells). Differentiation rate indicates the slope between two states, with steeper slopes indicating faster transition. In turn, stable states, the flat areas, have little or no downward slope and combined with proliferation, constitute areas of high self-renewal (Figure 2B).

Differentiation rate and cell fate are naturally connected, but, crucially, exist in specific experimental contexts. CMPs have been originally proposed as a multipotent population with combined erythroid, megakaryocytic, neutrophilic, and monocytic potential.47 However, later studies reported that most CMPs are transcriptionally and epigenetically primed toward specific lineages, 4 exhibit lineage bias, and are primarily unipotent 5 in transplantation cell fate assays.


## 关键词

model, murine, single-cell-resolved, time

## 相关实体

细胞类型: HSC, erythroid, neutrophil
通路: differentiation, self-renewal
方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
