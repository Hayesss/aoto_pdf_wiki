---
source_url: zotero://select/items/3T549S7E
ingested: 2026-04-22
sha256: e11957de4999e524
---

# Dong 等 - 2020 - Differentiation of transplanted haematopoietic ste

> Zotero Item Key: 3T549S7E
> Original File: Dong 等 - 2020 - Differentiation of transplanted haematopoietic ste.pdf

## Extracted Text

Articles
https://doi.org/10.1038/s41556-020-0512-1
Differentiation of transplanted haematopoietic
stem cells tracked by single-cell transcriptomic
analysis
Fang Dong1,2,3,9, Sha Hao1,2,3,9, Sen Zhang 1,3,9, Caiying Zhu1,3,9, Hui Cheng1,2,3,9, Zining Yang1,3,
Fiona K. Hamey4, Xiaofang Wang1,3,5, Ai Gao1,3, Fengjiao Wang1,3, Yun Gao 6, Ji Dong6,
Chenchen Wang1,3, Jinyong Wang 1,7, Yu Lan 5, Bing Liu1,8, Hideo Ema1,2,3, Fuchou Tang 6,
Berthold Göttgens 4,10 ✉, Ping Zhu 1,2,3,10 ✉ and Tao Cheng 1,2,3,10 ✉
How transplanted haematopoietic stem cells (HSCs) behave soon after they reside in a preconditioned host has not been stud-
ied due to technical limitations. Here, using single-cell RNA sequencing, we first obtained the transcriptome-based classifica-
tions of 28 haematopoietic cell types. We then applied them in conjunction with functional assays to track the dynamic changes
of immunophenotypically purified HSCs in irradiated recipients within the first week after transplantation. Based on our tran-
scriptional classifications, most homed HSCs in bone marrow and spleen became multipotent progenitors and, occasionally,
some HSCs gave rise to megakaryocytic–erythroid or myeloid precursors. Parallel in vitro and in vivo functional experiments
supported the paradigm of robust differentiation without substantial HSC expansion during the first week. Therefore, this
study uncovers the previously inaccessible kinetics and fate choices of transplanted HSCs in myeloablated recipients at early
stage, with implications for clinical applications of HSCs and other stem cells.
H
aematopoietic stem cells (HSCs) are able to give rise to proliferation in myeloablated recipients to meet the urgent need
the haematopoietic system1,2, thereby serving as an invalu- of haematopoietic regeneration after transplantation, followed
able source in regenerative medicine (transplantation) by stepwise differentiation into multiple lineages10. However, the
for patients with many devastating diseases3. In clinical practice, validity of this model has never been rigorously or comprehen-
transplanted stem cells commonly encounter diseased or dam- sively investigated, which is mainly due to technical difficulties
aged recipient environments. Despite a variety of diseased condi- such as the very limited number of donor-derived cells that can be
tions, current transplantation protocols for patients involve the use collected shortly after transplantation.
of preconditioning with chemotherapeutic agents or total body The rapid development of single-cell RNA sequencing
irradiation before transplantation. Thus, proper engagement with (scRNA-seq) technology provides a powerful tool and an unprec-
the microenvironment (niche) and ordered propagation of trans- edented opportunity to define cell taxonomy, track differentiation
planted HSCs in the early stage in such pathological recipients are and uncover transcriptional networks at single-cell resolution for
critical to the long-term engraftment and ultimate success of the any given isolatable heterogeneous cell population14–16. Thus, we
transplantation. Homing, lodgment, localization, niche interactions used scRNA-seq to comprehensively characterize 28 cell populations
and proliferation of transplanted HSCs have been extensively stud- in the haematopoietic system and applied transcriptome-based clas-
ied in the past4–7. Although the abundance of HSCs is thought to sifications to track donor-derived cells after HSC transplantation.
reach homeostatic levels during long-term engraftment, how HSCs
behave after transplantation is largely unknown. Results
In mouse transplant models, platelet production is first Single-cell transcriptomes of murine haematopoietic cells. A
observed as early as 7–9 days after HSC transplantation8,9. Given comprehensive single-cell transcriptome reference for the haema-
the classical stepwise haematopoietic cascade model10, HSCs must topoietic system was established by performing scRNA-seq for 28
quickly respond to the myeloablated host environment. In contrast haematopoietic cell populations from bone marrow (BM) or spleen
to the homeostatic condition in which HSCs only divide for limited (SP) of adult C57BL/6 mice (Fig. 1a). Single cells were isolated by
times in a lifespan11–13, HSCs are supposed to undergo dramatic fluorescence-activated cell sorting with well-established cell surface
1State Key Laboratory of Experimental Hematology, National Clinical Research Center for Blood Diseases, Institute of Hematology and Blood Diseases
Hospital, Chinese Academy of Medical Sciences and Peking Union Medical College, Tianjin, China. 2Center for Stem Cell Medicine, Chinese Academy
of Medical Sciences, Tianjin, China. 3Department of Stem Cell and Regenerative Medicine, Peking Union Medical College, Tianjin, China. 4Cambridge
University Department of Hematology, Wellcome Trust and MRC Cambridge Stem Cell Institute, Jeffrey Cheah Biomedical Centre, Cambridge, UK.
5Key Laboratory for Regenerative Medicine of Ministry of Education, Institute of Hematology, School of Medicine, Jinan University, Guangzhou, China.
6Beijing Advanced Innovation Center for Genomics, Biomedical Institute for Pioneering Investigation via Convergence, College of Life Sciences, Peking
University, Beijing, China. 7CAS Key Laboratory of Regenerative Biology and Guangdong Provincial Key Laboratory of Stem Cell and Regenerative Medicine,
Guangzhou Institutes of Biomedicine and Health, Chinese Academy of Sciences, Guangzhou, China. 8Fifth Medical Center of Chinese PLA General
Hospital, Beijing, China. 9These authors contributed equally: Fang Dong, Sha Hao, Sen Zhang, Caiying Zhu, Hui Cheng. 10These authors jointly supervised
this work: Tao Cheng, Ping Zhu, Berthold Göttgens. ✉e-mail: bg200@cam.ac.uk; zhuping@ihcams.ac.cn; chengtao@ihcams.ac.cn
NATuRE CELL BioLoGY | www.nature.com/naturecellbiology
Articles Nature Cell Biology
b
Enrichment of GO terms
Electron, proton transport
Cell cycle phase transition
Response to ER stress
B cell proliferation
Translation, viral transcription
Protein targeting to ER
RNA regulation, splicing
Embryo development
c d
100
80
60
40
20
0
C1 C2 C3
H S H S H S t t t
markers17–21 (Supplementary Table 1; Extended Data Fig. 1). In total, cells were tHSC1 and 29–45% were tHSC2. Fraction III was com-
1,270 single cells passed quality control (≥1,000 genes expressed), posed of 70% tHSC1 and 30% tHSC3, without tHSC2 (Fig. 1f).
and these were used to map the haematopoietic system (Methods). Using the same strategy, nine types of immunophenotypical
Diffusion map analysis of our single-cell haematopoietic stem and multipotent progenitors (iMPPs) were grouped into five clusters
progenitor cell data showed clear lineage branching that was consis- with distinct transcriptional features, hereafter termed as transcrip-
tent with previously published datasets22, which indicates that our tional MPP1 (tMPP1), tMPP2, tMPP3, tMPP4 and tMPP5 (Fig. 2a).
sequencing data is of high quality (Extended Data Fig. 2a–c). The compositions of tMPPs by iMPPs and that of iMPPs by tMPPs
We then thoroughly compared the transcriptomes of showed large transcriptional heterogeneity (Fig. 2b,c). Furthermore,
immunophenotype-defined cells. As expected, principal component committed progenitors23,24, erythrocytes, megakaryocytes, granulo-
analysis (PCA) and unsupervised hierarchical clustering revealed cytes, monocyte–macrophages and lymphocytes were also clustered
significant transcriptional heterogeneity within immunophenotypi- on the basis of their gene expression profiles and termed as tCP1–3
cal HSCs (iHSCs; Fig. 1b). Five types of iHSCs were grouped into (committed progenitors), tME1–3 (megakaryocyte–erythrocytes),
three clusters with distinct transcriptional features, hereafter termed tGM1–3 (granulocyte–monocyte–macrophages) and tLym1–4 (lym-
as transcriptional HSC1 (tHSC1), tHSC2 and tHSC3 (Fig. 1c). Egr1 phocytes) (Extended Data Fig. 3a,c,e,g). The composition of the

... [truncated]
