---
marker_extracted: true
title: "Mapping snoRNA-target RNA interactions in an RNA binding protein-dependent manner"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/mapping-snorna-target-rna-interactions-in-an-rna-binding-protein-dependent-manne.md]
confidence: medium
year: 2024
---

# Mapping snoRNA-target RNA interactions in an RNA binding protein-dependent manner

> 原文: [[mapping-snorna-target-rna-interactions-in-an-rna-binding-protein-dependent-manne]]

## 摘要

Small nucleolar RNAs (snoRNAs) are non-coding RNAs that function in ribosome and spliceosome biogenesis, primarily by guiding modifying enzymes to specific sites on ribosomal RNA (rRNA) and spliceosomal RNA (snRNA). However, many orphan snoRNAs remain uncharacterized, with unidentified or unvalidated targets, and studies on additional snoRNAassociated proteins are limited. We adapted an enhanced chimeric eCLIP approach to comprehensively profile snoRNA-target RNA interactions using both core and accessory snoRNA binding proteins as baits. Using core snoRNA binding proteins, we confirmed most annotated snoRNA-rRNA and snoRNA-snRNA interactions in mouse and human cell lines and called novel, high-confidence interactions for orphan snoRNAs. While some of these interactions result in chemical modification, others may have modification-independent functions. We then showed that snoRNA ribonucleoprotein complexes containing certain accessory proteins, like WDR43 and NOLC1, enriched for specific subsets of snoRNA-target RNA interactions with distinct roles in ribosome and spliceosome biogenesis. Notably, we discovered that SNORD89 guides 2'-Omethylation at two neighboring sites in U2 snRNA that are important for activating splicing, but also appear to ensure imperfect splicing for a subset of near-constitutive exons. Thus, chimeric eCLIP of snoRNA-associating proteins enables a comprehensive framework for studying snoRNA-target interactions in an RNA binding protein-dependent manner, revealing novel interactions and regulatory roles in RNA biogenesis.

 Department of Molecular & Cellular Biology, Harvard University, Cambridge MA USA

 Department of Biochemistry and Functional Genomics, Université de Sherbrooke, Québec CA

<sup>\*</sup>Authors contributed equally

<sup>†</sup> Corresponding authors: eric.vannostrand@bcm.edu, amanda\_whipple@fas.harvard.edu


## 背景与目的

Small nucleolar RNAs (snoRNAs) constitute a class of non-coding RNAs primarily known for their fundamental roles in ensuring the proper biogenesis of ribosomal RNA (rRNA). SnoRNAs can be categorized into box C/D and box H/ACA snoRNAs, distinguished by the presence of conserved box motif sequences and structural features. In addition, a class of snoRNAs known as small Cajal body-specific snoRNAs (scaRNAs), which contain either C/D, H/ACA, or hybrid (both) motifs, are involved in the biogenesis of spliceosomal RNAs (snRNAs). During their maturation, snoRNAs associate with core RNA-binding proteins (snoRBPs) to form functional snoRNPs. Specifically, C/D snoRNAs associate with FBL, NOP56, NOP58, and SNU13 (NHP2L1/15.5K), while H/ACA snoRNAs associate with DKC1, NOP10, NHP2 and GAR1 (Fig. 1A). SnoRNPs translocate to the nucleolus or Cajal body, where they interact with nascent pre-rRNA or snRNA [1]. The antisense elements of snoRNAs engage in base pairing with their RNA targets, orchestrating the precise positioning of 2'-O-methylation (Nm) by C/D snoRNPs or isomerization of uridine to pseudouridine (Ψ) by H/ACA snoRNPs. Human rRNA contains more than 200 nucleotides that undergo snoRNA-guided chemical modification [2]. Some of these chemical modifications cluster at functionally important regions of the ribosome, such as the peptidyl transferase center, tRNA binding sites, and the interface between the small and large subunits, and they contribute to the stabilization of rRNA folding, facilitation of efficient ribosome assembly, export of ribosomal subunits, and binding interactions with translation factors [3–5].

Over the years, research efforts have successfully identified snoRNA-target pairs for most known 2'-O-methylation and pseudouridine sites in rRNA. Advances in mass spectrometry approaches and high-throughput assays have facilitated the discernment of nucleotides subject to chemical modifications [2].


## 主要发现

### **Core snoRNP proteins show consistent RNA interactomes**

Previous profiling of the RNA interactomes of core C/D snoRNP proteins FBL, NOP56, and NOP58 by CLIP-seq led to the characterization of novel snoRNAs as well as the identification of candidate interactions for orphan snoRNAs [27,28]. However, of the four core H/ACA snoRNP proteins, the RNA interactome has only been profiled for DKC1 [27,29]. To expand upon this prior work, we set out to use the updated eCLIP framework that allows deeper recovery of unique RNA molecules as well as quantitative normalization against input controls to comprehensively profile the direct interactions for the C/D and H/ACA snoRNP complex members [30]. We obtained and performed IP-western blot validation of antibodies against the four core proteins for both C/D (FBL, NOP56, NOP58, and SNU13) and H/ACA (DKC1, NOP10, NHP2, and GAR1) snoRNP complexes respectively (Fig. S1A), followed by eCLIP in K562 cells to facilitate contrast analysis with other ENCODE RBP datasets (Fig. 1B).

Basic analysis of snoRBP eCLIP indicated successful enrichment of snoRNAs (Fig. 1C,D). Similar to previous observations with PAR-CLIP [27], eCLIP for FBL, NOP56, NOP58, and SNU13 each showed significant enrichment for C/D snoRNAs versus paired input (³ 6.5-fold) (Fig. 1C). Over 5% of reads mapped to C/D snoRNAs for FBL and NOP56, with an additional 80% of reads mapping to either precursor or mature rRNA; NOP58 and SNU13 had significantly enriched but lower frequency of reads mapping to C/D snoRNAs (>1.5%) (Fig. 1C). The C/D snoRBPs showed an average 1.5-fold depletion for H/ACA snoRNAs compared to size-matched inputs, suggesting that the C/D complex shows specificity for binding to C/D snoRNAs (Fig. 1C,D). Similarly, all four H/ACA snoRBPs showed significant enrichment for H/ACA snoRNAs (³ 6.2-fold) (Fig. 1C,D). Over 5% of reads mapped to H/ACA snoRNAs for each RBP and another 71% to rRNA (Fig. 1C).


## 方法概述

## *Cell culture*

293T (Clontech), K562 (ATCC) and HepG2 (ATCC) cell lines were purchased from commercial suppliers. 293T cells were cultured in DMEM (Thermo Fisher Scientific) supplemented with 10% FBS (Cytivia). Mouse ESC lines used in this study were derived from an *M. musculus* (129/Sv) × *M. castaneous* cross and have integrated EF1α-rtTA and TetO-Ngn2 constructs. For routine passaging, mESCs were maintained on plates pre-coated with 0.2% gelatin in DMEM (Thermo) supplemented with 10 mM HEPES (Thermo), 0.11 mM β-mercaptoethanol (Sigma), 1X nonessential amino acids (Corning), 2 mM L-glutamine (Corning), 15% fetal bovine serum (Cytivia), and 1000 U/mL leukemia inhibitory factor (LIF; Sigma). All cell lines were maintained in a humidified 5% CO2 incubator at 37°C, and cell lines were crosslinked as previously described [30].


## 讨论与结论

SnoRNAs play crucial roles in the modification and processing of rRNA and snRNA, impacting fundamental cellular processes such as translation and splicing. Despite clear biological relevance, research efforts have failed to identify targets for many orphan snoRNAs, and the roles of snoRNA-associated proteins are not well characterized. To address these gaps in understanding, we implemented an improved chimeric eCLIP approach that enables deep and accurate profiling of snoRNA interactions in an RBP-dependent manner. This new approach resulted in increased depth of snoRNA:target chimeras relative to previous efforts to directly map snoRNA interactions [14,15,18,28]. The high accuracy achieved (AUC > 97% in both human and mouse cell lines) allows for benchmarking against known targets and the characterization of novel interactions. Notably, this accuracy was achieved empirically without needing to model interaction complementarity as in previous work [28], enabling recovery of candidate interactions that may have non-canonical interaction dynamics.

Using stringent peak calling criteria, we identified novel snoRNA interactions, including those of orphan snoRNAs. For example, we called a high-confidence interaction between Snord101 and 28S rRNA as well as Snord89 and U2 snRNA. While similar interactions were detected in previous chimeric ligation sequencing approaches, the predicted Nm sites were either inaccurate or lacked

experimental validation [13,18]. We confirmed the bona fide effect of Snord101 and Snord89 on guiding Nm modification at 28S-G3283 and U2-G11/G12, respectively, in snoRNA loss-offunction experiments. Additionally, we identified putative interaction sites for Snord14, Snord23, Snord62 and Snord90, each supported by high methylation scores measured by RiboMeth-seq at the expected targeted nucleotide. Some of these interactions also have experimental support in other recent studies [13,14].


## 关键词

Mapping, RNA, binding, interactions, manner, protein-dependent, snoRNA-target

## 相关实体

方法: western blot

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
