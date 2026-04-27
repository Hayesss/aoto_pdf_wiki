---
title: "Single-cell chromatin accessibility reveals principles"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/single-cell-chromatin-accessibility-reveals-principles.md]
confidence: medium
year: 2015
---

# Single-cell chromatin accessibility reveals principles

> 原文: [[single-cell-chromatin-accessibility-reveals-principles]]

## 摘要

sively characterize variability associated with trans-factors within variabilityofGATA1bindingsitesthatco-occurwithJUNorCEBPB individual K562 cells, we computed variability across all available (ExtendedDataFig.6i).WealsofindpeaksuniquetoGATA1binding ENCODE ChIP-seq, transcription factor motifs and regions that are significantly more accessible than peaks unique to GATA2 differed in replication timing (as determined from Repli-Seq data (Extended Data Fig. 6k–l) supporting the hypothesis that GATA1, sets19) (Fig. 2c, d). We found measures of cell-to-cell variability anactivatorofaccessibility,competeswithGATA2toinducesingle- were highly reproducible across biological replicates (Extended cellvariability.ExtendingthisanalysistoalltranscriptionfactorChIP- DataFig.5).Asexpectedfromproliferating cells,wefind increased seqdatasetsrevealedatrans-factorsynergylandscapeforaccessibility variability within differentreplication timing domains, representing variation(Fig.2gandExtendedDataFig.6j).Forexample,chromatin variable ATAC-seq signal associated with changes in DNA content accessibilityvarianceassociatedwithGATA2bindingissignificantly across the cell cycle. In addition, we discover a set of trans-factors enhanced when the same region could also be bound by GATA1, associated with high variability. These factors include sequence- TAL1 or P300.

## 背景与目的

lleC GATA1 GATA1 40 inaccessible cells accessible cells P300:ChIP-seq 30 Permuted s.d. = 1 Observed s.d. = 3.1 4 20 1 10 Variability 0 4 1 Variability 5 10 15 20 25 Ranked principal components denialpxe ecnairav fo noitcarF a b Compute difference from downsampled ensemble 1 1 2 1 0 2 2 1 0 2 1 0 1 0 0 0 2 76 48 TF 0 1 0 1 0 0 1 0 0 0 0 3 1 0 1 1 0 23 13 Deviation = . 2 0 0 1 1 0 1 0 1 0 1 1 1 2 1 0 0 –22 –3 . . 1 1 2 1 0 2 2 1 0 2 1 0 1 0 0 0 2 211 50 0 1 0 1 0 0 1 0 0 0 0 3 1 0 1 1 0 –22 –12 2 0 0 1 1 0 1 0 1 0 1 1 1 2 1 0 0 –18 –10 Variability = 1 1 2 1 0 2 2 1 0 2 1 0 1 0 0 0 2 87 42 Rank sorted variability scores Observed 0.25 Permuted 0.2 0.15 0.1 Cell-cycle PC 0.05 0 1kaeP 2kaeP 3k.aeP . . Cell 1 [TF] Collect Sum across Sample fragment peaks across peaks counts per cell with TF motif and compute BS 6 –9 21 42 –7 6 19 Cell 2 [TF] FT SB 1 Calculate deviation and variability scores Identify TF motif in peaks . . . . . . SB N From aggregate map all fragments and call peaks From single cells compute deviation and variability taepeR 12 17 BS –7 RMS 41 –20 (TF)2 2 5 1 (BS mean)2 SB naem 28 27 16 45 37 19 29 SB SMR cells cells 2ATAG TSEROC TSEROC 003P 1RLBT 1ATAG 1LAT A3DIRA FFAM KFAM 1TATS 1INI 6TRIS 472FNZ 1GRB BPBEC 2TATS FTA NUJC 2LOP 1PDB 3LOP 8XBC 2XBC 3CMS 21ZUS FCTC 341FNZ RESEARCH LETTER Figure2|Trans-factorsareassociatedwithsingle-cellepigenomic measuredfrompermutedbackground(seeMethods)isshowningreydots. variability.

## 主要发现

1622–1626(2012). 9. Buenrostro,J.D.,Giresi,P.G.,Zaba,L.C.,Chang,H.Y.&Greenleaf,W.J. AuthorInformationAlldatahasbeendepositedinGEOundertheaccessionnumber Transpositionofnativechromatinforfastandsensitiveepigenomicprofilingof GSE65360.FluidigmC1scriptsforperformingscATAC-seqareavailableat openchromatin,DNA-bindingproteinsandnucleosomeposition.NatureMethods www.fluidigm.com/c1openapp/scripthub/script/2015-06/single-cell-chromatin- 10,1213–1218(2013). accessib-1433443631246-1.Reprintsandpermissionsinformationisavailableat 10. Lieberman-Aiden,E.etal.Comprehensivemappingoflong-rangeinteractions www.nature.com/reprints.Readersarewelcometocommentontheonlineversionof revealsfoldingprinciplesofthehumangenome.Science326,289–293(2009). thepaper.Theauthorsdeclarecompetingfinancialinterests:detailsareavailableinthe 11. Michor,F.etal.Dynamicsofchronicmyeloidleukaemia.Nature435,1267–1270 onlineversionofthepaper.Correspondenceandrequestsformaterialsshouldbe (2005). 490 | NATURE | VOL 523 | 23 JULY 2015 G2015 MacmillanPublishersLimited.Allrightsreserved b d 0 20 40 60 80 Cell Barcode sdaer etacilpud noitcarF 0.75 0.5 0.25 0 0 20 40 60 80 Cell Barcode 501xdecneuqes sdaeR c Tn5-DNA DNA purification EDTA (mM) Temperature (°C) Fragments released complex - - RT 1.00 + - RT 6.72 - 10 RT 3.80 - 20 RT 1.99 - 50 RT 2.65 - 10 50 6.46 - 20 50 11.21 - 50 50 12.79 * - 50 70 8.98 Tn5 - + + + + 50 70 8.

## 方法概述

i j ZNF143 CTCF SUZ12 GATA1 Shared GATA2 SMC3 n=270 n=2,722 n = 3,554 CBX2 var=1.01 var=3.08 var=1.74 CBX8 error=0.07 error=0.08 error=0.21 POL3 BDP1 POL2 CJUN ATF STAT2 CEBPB k l BRG1 ZNF274 INI1 SIRT6 STAT1 MAFK MAFF ARID3A TAL1 GATA1 GATA2 COREST COREST P300 TBLR1 -log10(p-value) zScore = 6.22 pValue ~ 4.88x10-10 5 0 1RLBT 003P TSEROC TSEROC 2ATAG 1ATAG 1LAT A3DIRA FFAM KFAM 1TATS 6TRIS 1INI 472FNZ 1GRB BPBEC 2TATS FTA NUJC 2LOP 1PDB 3LOP 8XBC 2XBC 3CMS 21ZUS FCTC 341FNZ RESEARCH LETTER ExtendedDataFigure6|Characterizationofhigh-variancetrans-factorsin differentreplicationtimings(Repli-Seq)havestrongvariationalongthisaxis. K562cells. a–d,DistributionofGATA1(a),GATA2(b),actin(c)andCTCF h,i,VenndiagramsshowingvariabilityofGATA1and/orGATA2(h),cJUN (d)fluorescenceobservedbyflowcytometry.Distributionsingreydepict and/orGATA2andCEBPBand/orGATA2(co-)occurringChIP-seqsites isotypecontrols.e,Bi-clusteredheatmapofsingle-celldeviationsasobserved (i).j,The2log (Pvalues)ofcalculatedchangesinco-occurringChIP-seqsites 10 withinK562cells(n5239).Labelsonrightidentifyco-clusteringofrelated showninFig.2g.k,DistributionofaccessibilityamongGATA1only,GATA2 factors.f,Bi-clusteredheatmapofsingle-celldeviationsobservedfrom only,andsharedsites.l,MeanaccessibilityfromGATA1only,GATA2only, permuteddata.g,Projectionoffactorloadingsontoprincipalcomponent1 andsharedsitesink,errorbarsrepresentonestandarddeviationgeneratedby versus5fromprincipalcomponent(PC)analysisofheatmapshownine.

## 讨论与结论

noitalerroC 1.7740AM-1LSOF 1.0940AM-BNUJ 1.8740AM-2LSOF 1.1940AM-DNUJ 1.6740AM-SOF 1.9840AM-NUJ 1.2640AM-NUJ-FTAB 1.1050AM-FAM-2EFN 2.0510AM-2l2efN 1.1950AM-kfaM-1hcaB 3.0800AM-1ipS 1.3740AM-1FLE 1.5740AM-1ILF 2.8900AM-1stE 1.4740AM-grE 1.8950AM-FHE 1.6510AM-VEF 1.1010AM-LER 1.7010AM-ALER 3.5010AM-1BKFN 1.0060AM-2XFR 1.9050AM-1xfR 1.0610AM-2A4RN 2.1410AM-brrsE 1.2950AM-ARRSE 2.2000AM-1XNUR 1.1150AM-2XNUR 1.3700AM-1BERR 2.3010AM-1BEZ 3.4010AM-ncyM 1.0900AM-1DAET 2.5900AM-1YY 1.9310AM-FCTC 1.7700AM-9XOS 3.3410AM-2xoS 1.5150AM-6xoS GONAN-8002.nehC 2.0410AM-1ATAG-1LAT 2.6300AM-2ATAG 1.2840AM-4ataG 3.5300AM-1ataG 2.7300AM-3ATAG RESEARCH LETTER GATA3-MA0037.2 Gata1-MA0035.3 Gata4-MA0482.1 GATA2-MA0036.2 TAL1-GATA1-MA0140.2 Chen.2008-NANOG Sox6-MA0515.1 Sox2-MA0143.3 SOX9-MA0077.1 CTCF-MA0139.1 YY1-MA0095.2 TEAD1-MA0090.1 Mycn-MA0104.3 ZEB1-MA0103.2 RREB1-MA0073.1 RUNX2-MA0511.1 RUNX1-MA0002.2 ESRRA-MA0592.1 Esrrb-MA0141.2 NR4A2-MA0160.1 Rfx1-MA0509.1 RFX2-MA0600.1 NFKB1-MA0105.3 RELA-MA0107.1 REL-MA0101.1 FEV-MA0156.1 EHF-MA0598.1 Erg-MA0474.1 Ets1-MA0098.2 FLI1-MA0475.1 ELF1-MA0473.1 Spi1-MA0080.3 Bach1-Mafk-MA0591.1 Nfe2l2-MA0150.2 NFE2-MAF-MA0501.1 BATF-JUN-MA0462.1 JUN-MA0489.1 FOS-MA0476.1 JUND-MA0491.1 FOSL2-MA0478.1 JUNB-MA0490.1 FOSL1-MA0477.1 ExtendedDataFigure8|Transcriptionfactormotifcorrelationand b,c,Variabilityofregionsassociatedwithchromatinstates(b),asidentifiedin variabilityacrosschromatinstate. a,Hierarchicalbi-clusteringofhigh- ref.26,andhistonemodifications(c).

## 关键词

Single-cell, accessibility, chromatin, principles, reveals

## 相关实体

细胞类型: all
方法: ChIP-seq, Single-cell, single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
