---
title: "Raftrey 等 - 2021 - Dach1 Extends Artery Networks and Protects Against Cardiac Injury"
created: 2025-04-22
updated: 2025-04-22
type: paper
tags: ["biomedical"]
sources: ["raw/papers/raftrey-等-2021-dach1-extends-artery-networks-a.md"]
confidence: medium
marker_extracted: true
---

# Raftrey 等 - 2021 - Dach1 Extends Artery Networks and Protects Against Cardiac Injury

> Zotero Item Key: 2NS8639M
> 原文: [[raftrey-等-2021-dach1-extends-artery-networks-a]]

## 摘要

（待补充）

## 背景与目的

（待补充）

## 主要发现

## Dach1 Overexpression Increases Artery Specification and Branching in the Heart

Since *Dach1* deletion impairs artery development,8 we hypothesized that increasing it would promote artery growth. Thus, we generated a transgenic mouse that would inducibly overexpress *Dach1*. A transgene containing the *CAG* promoter upstream of a *Flox-Stop-Flox-Dach1-IRES-EGFP* sequence was inserted into the *ROSA26* locus (Figure 1A). We next crossed these with *ApjCreER*, which is expressed in ECs of the developing coronary capillary plexus and veins but not in differentiated arterial ECs.14 Cre induction with Tamoxifen resulted in excision of the transcriptional stop sequence and permanent co-expression of *Dach1* and EGFP in plexus ECs. We observed high levels of Cre-dependent recombination and *Dach1* expression inferred from EGFP expression (Figure 1B) and anti-Dach1 immunofluorescence (Figure 1C). Tamoxifen was given to experimental (*ApjCreER;Dach1OE*) and control (Cre-negative *Dach1OE*) mice, but we verified that neither transgene affected coronary development in the absence of Tamoxifen (data not shown). This tool was then used to explore the effects of *Dach1* overexpression on artery formation.

We induced *Dach1OE* at embryonic day (e) 13.5, when arterial EC differentiation normally begins, and harvested embryos at e15.5 (Figure 1D). At this time, single, preartery ECs that have differentiated within the immature capillary plexus have begun to coalesce into coronary arteries that can be morphologically distinguished.10 The effect of *Dach1OE* was assessed by immunostaining for ECs (VE-cadherin) and the arterial EC marker CX40 (connexin 40). CX40-positive artery ECs in control hearts were in larger diameter arterial vessels and the capillary plexus as cells that have been specified as arterial but have not yet assembled into the artery, ie, preartery cells (Figure 1E, upper). In *Dach1OE* mutants, we observed an increase in the number of capillary plexus ECs expressing CX40 (Figure 1E, lower panels). Quantifying the area of each heart covered by CX40 positive ECs revealed a 71% increase in *Dach1OE* hearts (Figure 1F). These results indicate that *Dach1* overexpression stimulates preartery specification in ECs within the capillary plexus. We did not find statistically significant differences in proximal coronary artery diameters (Figure 1G), heart sizes (Figure 1H), and the number of ECs within the myocardium (Figure 1I). We concluded that *Dach1* overexpression increased the abundance of arterialized ECs without grossly affecting cardiac development.

We next analyzed artery morphology 4 days post-induction at e17.5 when arteries are more mature (Figure 2A). Immunostaining for CX40 revealed that distal branches were more numerous, while diameters of proximal branches were not significantly different (Figure 2B). Additional branches expressed other artery markers (*Jag1*, CX37) (Figure IA through IC in the [Data Supplement\)](https://www.ahajournals.org/doi/suppl/10.1161/CIRCRESAHA.120.318271) and received blood flow as assessed by fluorescent lectin perfusions (Figure ID and I E in the [Data Supplement](https://www.ahajournals.org/doi/suppl/10.1161/CIRCRESAHA.120.318271)). EC coverage was not grossly affected as assessed by VE-cadherin staining (Figure 2B). Summing the lengths of all CX40+ vessels revealed a 79% increase in artery lengths (Figure 2C) and counting junctions showed a 334% increase in branching (Figure 2D). No statistically significant difference in primary artery diameters was found between groups (Figure 2E). This suggests that the increased preartery specification observed at e15.5 precedes the development of excessive distal artery branches at e17.5.

To extend our analysis beyond embryonic development, we induced *Dach1* at postnatal day (P) 0 and analyzed arteries at P6 (Figure 2F). Similar to embryonic hearts, distal artery branches were more numerous (Figure 2G and 2 H) with increased branching (Figure 2I) in the watershed area between the right and left coronary arteries. Diameters of proximal coronary branches were not significantly different (Figure 2J).

We next determined whether the increase in artery branches resulted from Dach1 activity in capillary plexus or arterial ECs. Above, *ApjCreER* will only induce *Dach1OE* in the capillary plexus, but overexpression will be maintained in the arteries that differentiate from these cells. To test whether *Dach1* has the same effects when expressed exclusively in artery ECs, we analyzed *CX40CreER;Dach1OE* e15.5 embryos dosed with Tamoxifen at e13.5 (Figure 2K). In contrast to *ApjCreER* induction, there was no statistically significant difference in artery abundance or width in *CX40CreER;Dach1OE* animals (Figure 2L through 2N). We conclude that *Dach1* increases arterial branching through its activity in capillary plexus ECs.

## 方法概述

#### Data Availability

All scRNA seq data including raw reads and Seurat processed data are publicly available at GEO (GSE179857).

Details of the experimental methods are available in the [Data Supplement.](https://www.ahajournals.org/doi/suppl/10.1161/CIRCRESAHA.120.318271)

Please see the Major Resources Table in the [Data](https://www.ahajournals.org/doi/suppl/10.1161/CIRCRESAHA.120.318271)  [Supplement.](https://www.ahajournals.org/doi/suppl/10.1161/CIRCRESAHA.120.318271)

For the majority of experiments, female *Dach1OE/ Dach1OE* mice were crossed to *ApjCreER* males to generate *Cre- ;Dach1OE/+* or *Cre+;Dach1OE/+* animals used as either controls or Dach1 overexpressors respectively, upon administration of Tamoxifen. Tissue collection, fixation, immunostaining, and

imaging were performed on embryonic hearts,10 postnatal hearts,11 retinas,8 and adult hearts12 as previously described.

To prepare samples for single-cell RNA seq, embryonic hearts were enzymatically digested, and the single-cell suspension was FACS sorted to remove red blood cells and enrich for ECs. Single-cell sequencing was done using the 10X singlecell V3 platform and analysis was performed using Cell Ranger, R, and Seurat.13

Coronary artery ligation experiments were done by opening the chest cavity and placing a 7-0 silk suture around the left anterior descending artery, with occlusion verified by blanching of the underlying myocardium. Transthoracic echocardiograms were then used to assess cardiac function. After fixation, ligated hearts were embedded in paraffin, sectioned, and stained with Masson's Trichrome.

## 讨论与结论

Coronary artery ECs differentiate from capillaries; however, transcriptional regulators of this transition remain incompletely understood. We found that overexpression of *Dach1* drove ectopic arterial EC specification in coronary capillaries. Extra arterial ECs contributed to artery remodeling to create longer, more branched arterial networks, which was also detected in the retina. ScRNAseq revealed that *Dach1OE* suppressed lipid transport genes in all ECs but upregulated arterial genes specifically in capillaries on the arterial side of the artery-vein vein continuum and in preartery and arterial populations. Finally, *Dach1* overexpression in adults improved survival and heart function after MI, which was accompanied by an increase in arteries and perfusion that occurred only in the days after injury.

Mosaically expressing *Dach1OE* in retinal ECs resulted their localization first to the tip cell location and then to arteries, supporting previous data proposing that Dach1 supports artery development by potentiating EC migration against the direction of blood flow into growing arteries.8 In the retina, cells at the tips of the growing angiogenic front are selected as preartery cells and eventually change direction to migrate into developing arteries.16,17,25 These data align Dach1 overexpression with this process and demonstrate that it potentiates arterialization in a cell autonomous manner.

Endogenously, *Dach1* is widely expressed in coronary ECs in both embryos and adults, although levels are downregulated in the mature artery.8 This widespread, high expression of *Dach1* in capillaries and veins, suggests that (1) its ability to induce arterialization is dependent on the context of the particular EC and (2) Dach1 may have functions independent of inducing artery genes. During arterialization, we propose that Dach1 either collaborates with a co-factor with a more restricted expression pattern or functions to lower the threshold for arterialization signals present at specific locations in the tissue.

Given the developmental effect of *Dach1* overexpression, we hypothesized that it could enhance recovery from ischemic injury. Animals with *Dach1* overexpression in coronary capillary and vein ECs experienced increased ejection fraction and survival. Notable was the pattern of myocardial fibrosis in *Dach1OE*—damaged myocardium was restricted to an intramyocardial region and covered by surviving myocardium on both the epicardial and endocardial faces. While overexpression did not result in statistically significant changes in arterial structure before injury, we found evidence for increased artery growth after infarction that benefited re-perfusion. Thus, injury may reactivate pathways not present in healthy tissue that allow Dach1 to induce artery differentiation. This work supports further investigation of Dach1 as a potential therapeutic target aimed at enhancing revascularization of ischemic hearts.

## 关键词

Against, Artery, Cardiac, Dach1, Extends, Injury, Networks, Protects, Raftrey

## 相关实体

暂无识别到特定实体

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
