---
source_path: /mnt/c/Users/Administrator/Zotero/storage/A7LLWFPW/Wang 等 - 2023 - Integrative scATAC-seq and scRNA-seq analyses map .pdf
ingested: 2026-04-23
sha256: d67df3b962274609
---

Wangetal.CellDiscovery( 2023) 9:61 Cell Discovery
https://doi.org/10.1038/s41421-023-00547-x
www.nature.com/celldisc
ARTICLE Open Access
Integrative scATAC-seq and scRNA-seq analyses
i
map thymic NKT cell development and identify
Cbfβ
for its commitment
Jie Wang1,2, Indra Adrianto 1,2,3,4, Kalpana Subedi1,2, Tingting Liu1,2, Xiaojun Wu1,2, Qijun Yi1,2, Ian Loveless 3,
✉
Congcong Yin 1,2, Indrani Datta3, Derek B. Sant’Angelo5, Mitchell Kronenberg6, Li Zhou1,2,4,7 and
✉
Qing-Sheng Mi 1,2,4,7
Abstract
Unlike conventional αβT cells, invariant natural killer T (iNKT) cells complete their terminal differentiation to
functional iNKT1/2/17 cells in the thymus. However, underlying molecular programs that guide iNKT subset
differentiation remain unclear. Here, we profiled the transcriptomes of over 17,000 iNKT cells and the chromatin
accessibility states of over 39,000 iNKT cells across four thymic iNKT developmental stages using single-cell RNA
sequencing (scRNA-seq) and single-cell assay for transposase-accessible chromatin sequencing (scATAC-seq) to
define their developmental trajectories. Our study discovered novel features for iNKT precursors and different
iNKTsubsetsandindicatedthatiNKT2andiNKT17lineagecommitmentmayoccurasearlyasstage0(ST0)bytwo
distinct programs, while iNKT1 commitments may occur post ST0. Both iNKT1 and iNKT2 cells exhibit extensive
phenotypic and functional heterogeneity, while iNKT17 cells are relatively homogenous. Furthermore, we
identified that a novel transcription factor, Cbfβ, was highly expressed in iNKT progenitor commitment
checkpoint, which showed a similar expression trajectory with other known transcription factors for iNKT cells
development,Zbtb16andEgr2,andcoulddirectiNKTcellsfateanddrivetheireffectorphenotypedifferentiation.
ConditionaldeletionofCbfβblockedearlyiNKTcelldevelopmentandledtosevereimpairmentofiNKT1/2/17cell
differentiation. Overall, our findings uncovered distinct iNKT developmental programs as well as their cellular
heterogeneity, and identified a novel transcription factor Cbfβ as a key regulator for early iNKT cell commitment.
Introduction pairedwithadiversesetofTCRVβchains(Vβ8s,Vβ7or
Invariant natural killer T (iNKT) cells are innate-like Vβ2 chains), are positively selected by CD1d on DP thy-
T cells that share the characteristics of T cells and NK mocytes and highly express CD24 (CD24 + , defined as
cells1,2 and modulate a broad spectrum of immune stage 0 (ST0)). These newly selected iNKT cells enter
responsesanddiseases3.Inthemousethymiccortex,rare the medulla directed by the expression of Ccr74. In the
+ +
CD4 CD8 doublepositive(DP)thymocytesexpressinga thymic medulla, they sharply downregulate CD24
Vα14-Jα18 T-cell receptor (TCR) chain, preferentially (CD24 − CD44 − NK1.1 − , defined as stage 1 (ST1)), then
upregulate the adhesion molecule CD44 and acquire a
memory or activate phenotypes (CD44hiNK1.1 − , defined
Correspondence:LiZhou(lzhou1@hfhs.org)or as stage 2 (ST2)). ST2 iNKT cells either emigrate to the
Qing-ShengMi(QMI1@hfhs.org)
1CenterforCutaneousBiologyandImmunologyResearch,Departmentof peripheral organs or remain as long-lived resident cells
Dermatology,HenryFordHealth,Detroit,MI,USA and mature after acquiring NK1.1 and other NK lineage
2ImmunologyResearchProgram,HenryFordCancerInstitute,HenryFord markers(CD44hiNK1.1 + ,definedasstage3(ST3))inthe
Health,Detroit,MI,USA
thymus1.
Fulllistofauthorinformationisavailableattheendofthearticle
Theseauthorscontributedequally:JieWang,IndraAdrianto
©TheAuthor(s)2023
OpenAccessThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,whichpermitsuse,sharing,adaptation,distributionandreproduction
inanymediumorformat,aslongasyougiveappropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicense,andindicateif
changesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unlessindicatedotherwiseinacreditlinetothematerial.If
materialisnotincludedinthearticle’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutoryregulationorexceedsthepermitteduse,youwillneedtoobtain
permissiondirectlyfromthecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/licenses/by/4.0/.
;,:)(0987654321 ;,:)(0987654321 ;,:)(0987654321 ;,:)(0987654321
Wangetal.CellDiscovery (2023) 9:61 Page2of20
Results
Unlike conventional Th1/2/17 T cells, which differ-
entiate in the peripheral lymphoid tissues upon antigen Clustering thymic iNKT cells across successive
encounter or specific cytokine treatment, iNKT cells developmental stages by scRNA-seq and scATAC-seq
acquire their effector function and differentiate into To unveil the iNKT cell developmental landscape, thy-
iNKT1 (PLZFloT-bethi), iNKT2 (PLZFhiRORγt − ), and mic iNKT cells across successive developmental stages
iNKT17 (PLZFintRORγt + ) cells prior to thymic export. were harvested by fluorescence-activated cell sorting
TheseiNKTsubsetshavecytokineprofilessimilartotheir (FACS) for scRNA-seq and scATAC-seq assays (Fig. 1a,
+
Th1/2/17 counterparts, but are less strict. For example, b).GiventherarityofthymicST0(CD24 )iNKTcellsin
iNKT1 cells also produce IL-4, although they mainly C57BL/6 mice, we utilized Vα14-Jα18-transgenic mice
produce IFN-γ. Most ST3 iNKT cells are either CD4 + (also called rec-Vα14Tg) for ST0 iNKT cell analysis,
single positive (CD4SP) or CD4 − CD8 − double negative whichcloselymimictheendogenousTCRlocusbuthave
(DN) cells, while ST2 cells are more diverse, including abundant ST0 iNKT cells8,9 (Supplementary Fig. S1a, b).
CD4SP iNKT2 cells, DN iNKT17 cells, and immature As expected, we found a high similarity in scATAC-seq
iNKT1 cells5. profile in ST0 iNKT cells between the rec-Vα14Tg and
Although advanced studies have been conducted in C57BL/6mice(SupplementaryFig.S1c,d).Therefore,we
iNKTcellsrecently,severalcentralquestionsremainto furtherperformedscRNA-seqanalysesusingrec-Vα14Tg
be answered including: (1) What is the early biological mice for ST0 iNKT cells and C57BL/6 mice for ST1
event post iNKT positive selection? (2) How do the (CD24 − CD44loNK1.1 − ),ST2(CD24 − CD44hiNK1.1 − )and
specific transcription factors coordinated with their ST3 (CD24 − CD44hiNK1.1 + ) iNKT cells (Fig. 1a–c and
chromatin background guide iNKT cell sub-lineage Supplementary Fig. S1b).
commitment and differentiation in the thymus? (3) The scRNA-seq and scATAC-seq libraries were gener-
What is the potential checkpoint for different iNKT ated using the 10X Genomics platform. After the quality
subset differentiation? (4) Are iNKT1, iNKT2 and control filtering and excluding cell outliers, a total of
iNKT17 cells phenotypically/functionally hetero- 17,944 high-quality single thymic iNKT cells with a total
geneousorhomogenous?Recentadvancesinsingle-cell of 13,578 expressed genes were retained for the sub-
assays provide an avenue to explore the transcriptomic sequent scRNA-seq analysis. A total of sixteen clusters
and epigenetic heterogeneity of cells at single-cell were identified using the R Seurat package10,11 in the
resolution. Single-cell RNA sequencing (scRNA-seq) aggregated iNKT cells (ST0–ST3), from as few as 255
can be utilized to assess cell-to-cell variation and has cells to as many as 2817 cells per cluster (Fig. 1d, e). The
been used to discover rare populations and to infer mostdifferentiallyexpressedgenes(DEGs)ineachcluster
lineage relationships6,7, which offers an unbiased were shown in the heatmap (Fig. 1f) and violin plots
approach to study iNKT cell developmental trajectory (Fig.1g).Amongtheseclusters,fourclusters(C2,C4,C9,
and heterogeneity. Single-cell assay for transposase- and C14) were from ST0, eight clusters were from ST1
accessiblechromatinsequencing(scATAC-seq)offersa (C3, C5, C6, C7, C10, C11, C15, and C16), nine clusters
similar resolution and provides additional information were from ST2 (C1, C3, C5, C6, C7, C10, C11, C13, and
about gene regulatory processes. Here, we profiled the C15) and four clusters were from ST3 (C1, C5, C8, and
transcriptomes of over 17,000 iNKT cells and the C12) (Fig. 1d and Supplementary Fig. S2a). ST0
chromatinaccessibilitystatesofover39,000iNKTcells iNKT cells were clearly separated from the rest of the
across four thymic iNKT developmental stages. By iNKT stages, and the clusters from ST1 and ST2
integrating transcriptome and chromatin accessibility iNKTcellsmoderatelyoverlapped,whereasiNKTclusters
profiles, we identified two developmental programs in from ST3 were closely adjacent to those from ST2
ST0 that contribute to iNKT2 and iNKT17 differ- iNKT cells (Fig. 1d and Supplementary Fig. S2b). More-
entiation, while iNKT1 commitment occurs in ST1. over, the correlation analysis indicated that distinct clus-
Both iNKT2 and iNKT1 cells exhibit extensive het- ters within the same stage exhibit a relatively similar
erogeneity, while iNKT17 cells are relatively homo- transcriptomic pattern. For example, the correlation
genous. We identified a co-transcription factor Cbfβ between clusters in ST0 ranged from 0.37 (C2vs C14) to
highly expressed in the iNKT commitment checkpoint, 0.79 (C2 vs C4), and the correlation between clusters in
and conditional deletion of Cbfβ in the thymocytes ST3rangedfrom 0.39(C5vsC12)to0.87(C1vsC8).As
almosttotallyblockedearlyiNKTcelldevelopmentand expected, the clusters in different stages did not exhibit a
severely impaired iNKT1/2/17 cell differentiation. significant correlation, indicating that transcriptomic
Overall, our study captured iNKT cell developmental patterns are greatly distinct in the clusters belonging to
trajectories, revealed their cellular heterogeneity, and different stages (Supplementary Fig. S2c).
identified Cbfβ as a key regulator for early iNKT cell Cellular differentiation is accompanied by the expres-
commitment. sionofgenescontrolledbycis-regulatoryelements,which
Wangetal.CellDiscovery (2023) 9:61 Page3of20
Fig.1(Seelegendonnextpage.)
Wangetal.CellDiscovery (2023) 9:61 Page4of20
(seefigureonpreviouspage)
Fig.1ThediversityofmousethymiciNKTcell.aiNKTcellscollectedforscATAC-seqandscRNA-seqanalysis.bSortingstrategyofST0(CD24+),
ST1(CD24−CD44loNK1.1−),ST2(CD24−CD44hiNK1.1−)andST3(CD24−CD44hiNK1.1+)iNKTcells.cOverviewofstudydesign.dt-SNEplotsfrom10X
genomicsscRNA-seqdataset.CellsfromsortedthymicST0,ST1,ST2andST3iNKTcellswerepooled.Displayingrelationshipsbetweenindividualcells
withcolor-codedonST0/1/2/3iNKTcells(left);t-SNEplotsofdataidenticaltothoseintheleftbutcolor-codedonthedifferentclusters(right).Bar
graphrepresentscellnumbersineachcluster(top),n=2.eThefractionsofsixteenclustersdefinedinaggregatediNKTcellsacrossST0–3.fHeatmap
ofthetoptenDEGsfromeachclusterderivedfrom(d).Eachcolumnrepresentsgeneexpressionforanindividualcellwithcolor-codedongene
expressionprofiles.Yellowisupregulated,andpurpleisdownregulated.gViolinplotsofcluster-defininggenesineachclusterderivedfrom(d).
Fig.2Differentclustersassignedintofunctionalsubsets.aUMAPplotsshowingintegratedanalysisofscRNA-seqandscATAC-seqfromsorted
ST0–3iNKTcells.bBubbleplotsshowinggeneexpressioninindividualclusters(C1–C16)fromaggregatediNKTcells.Genenameslabeledinblueare
iNKT17signaturegenes,inredareiNKT1signaturegenesandingreenareiNKT2signaturegenes.yaxisshowsdifferentclustersidentifiedin(a).
must be in an open state in order to function properly. clusters, majorly from ST3 were categorized into iNKT1
WethereforeperformedscATAC-seqanalysesonthymic (Fig. 2b and Supplementary Fig. S2a, e); while a unique
iNKT cells from different developmental stages as those iNKT C13 from ST2 was assigned into iNKT17 (Fig. 2b
in scRNA-seq analysis and mapped the chromatin andSupplementaryFig.S2a,d).Asexpected,ST0clusters
accessibility landscape of individual iNKT cells using the (C2, C4, C9, and C14) did not stand out in any iNKT
RSeuratandSignacpackages.Atotalof39,428cellswere subsets(Fig.2b)sincetheydidnotexhibitstrongeffector
analyzed, with a median of 11,398 fragments per cell signatures. Overall, by integrating transcriptomic and
mappedtothenucleargenome(SupplementaryFig.S2d). epigenetic profiles, we mapped the dynamic tran-
As expected, those sixteen iNKT cell clusters were well scriptomeandchromatinlandscapesofthymiciNKTcells
identifiable after the integration with scRNA-seq data with sixteen clusters and uncovered the heterogeneity of
(Fig. 2a). Since scRNA-seq allows us to identify the cur- iNKT1 and iNKT2 cells and the relative homogeneity of
rentcellstateasimplicatedbythetranscriptome,wethen iNKT17 cells.
assigned each of the clusters (C1–C16) into defined iNKT cells proliferate briskly during development, espe-
iNKT1, iNKT2, and iNKT17 functional subsets based on ciallyatST1andST2,oriNKT2/17subsets(Supplementary
their signature transcriptomes as previously published12 Fig.S3a,b),wewonderedwhetherthecellcyclegenesmay
andcytokinetranscriptexpression.WefoundthatC3,C6, mask other functionally key genes for iNKT cells. To
C7, C10, C11, C15, and C16 clusters from ST1 and ST2 eliminate this confounding factor and unmask the under-
werecategorizedintoiNKT2subset;C1,C5,C8,andC12 lying iNKT cell heterogeneity, we regressed out celleffects
Wangetal.CellDiscovery (2023) 9:61 Page5of20
followed by re-clustering of these iNKT cells. As shown in Toexplore thedevelopmental programsafterselection,
Supplementary Fig. S3c–e afterremovingtheeffectsofthe we applied the Monocle toolkit20 in R to organize ST0
cellcycleonthetranscriptome,theclustersobservedinST0 iNKTp into a pseudotime trajectory. Two potential
andST3areveryconsistentwithourprimarydata(Fig.1d). developmental branches, C14-C2-C4 branch (termed as
Given that cell proliferation is the nature of ST1 and ST2, DP-DN) and C14-C9 branch (DP-CD4SP) were identified
and those cells have a very strong capability to expand (Fig. 3f). Both branches eventually meet at the develop-
iNKT1, iNKT2, and iNKT17 subsets, we included those mental ends with increased expression of chemokine
cells for our following analysis. receptor Ccr7 (Fig. 3g), which is required for ST0 iNKTp
migration from the thymic cortex to medulla21. Ccr7
Two developmental trajectories in ST0 expression patterns in DP, DN, and CD4SP iNKTp were
iNKTcelldevelopmentinthethymusreliesonthepool further confirmed at the protein level by flow cytometry
ofaround1000ST0iNKTprecursors(iNKTp)locatedin (Fig. 3h). Thus, after selection, DP iNKTp downregulate
thethymiccortex13.Here,weidentifiedfourclusters(C2, CD8 or both CD4 and CD8 expression to initiate DP-
C4,C9,andC14)inST0(Figs.1dand3a)andhighlighted CD4SP or DP-DN developmental programs in the thymic
the specific signatures for each cluster (Fig. 3b). To fur- cortex,whicheventuallymigrateintothethymicmedulla.
ther test the robustness of ST0 cells from rec-Vα14Tg
mice,wethencomparedST0fromrec-Vα14Tgmicewith Functional iNKT subset-lineage commitments in ST0
+
selected CD24 ST0 cells from C57BL/6 mice recently Wenextaskedhowthese twodevelopmental programs
reportedbyKrovietal.14.Aftercorrectionofbatcheffect, in ST0 contribute to iNKT subset-lineage commitments.
merging,andaligningofdatafromtwolibraries,ST0cells Although PLZF is annotated as a key iNKT2 signature, it
from C57BL/6 mice essentially mirrored the ones from is also critical for overall iNKT cell development,
rec-Vα14Tg mice with similar clusters (Supplementary including iNKT1 and iNKT17 cells. Thus, we first asses-
Fig.S4a,b).Furthermore,theco-expressionofthesegenes sed the expression pattern and chromatin accessibility of
in individual clusters were verified in both rec-Vα14Tg Zbtb16(encodesPLZF)inST0iNKTp.Wefoundthatthe
andC57BL/6micebyflowcytometry(SupplementaryFig. region +40kb and TSS to Zbtb16 was not accessible in
S4c,d).Alternatively,basedonCD4andCD8expression, the DP iNKTp (C14) but was accessible in CD4SP (C9)
theseST0clusterscanbeclassifiedintothreegroups:C14 and DN (C2 and C4) iNKTp with much higher levels of
areCD4 + CD8 + (DP)iNKTp;C9areCD4 + CD8 − (CD4SP) openness in C2 over C4, which closely resembled the
iNKTp, enriched with the regulators of T lymphocyte Zbtb16 expression pattern (Fig. 3i, j). The pseudotime
survival, including Id2 and Il7r; C2 and C4 are trajectory and flow cytometry further indicated that
CD4 − CD8 − (DN)iNKTp,withC4 highlyexpressingCd5 Zbtb16 was enriched in both DN and CD4SP iNKTp
andCd6,whileC2iNKTpabundantlyexpressesEgr2and (Fig. 3j, k). Interestingly, PLZFhi iNKT cells in CD4SP
Slamf6,whichareessentialforiNKTcelldevelopmentvia exhibitstrongerTCRsignalingstrengthcomparedtothat
regulation of PLZF expression and TCR signaling in DN iNKT cells, indicated by the increased expression
strength, respectively15,16 (Fig. 3b–d). levelsofPLZF,TCR,Nur77,andVβ722,23(Supplementary
Although previous studies claimed that iNKT cells are Fig. S7a). Given that iNKT2 differentiation requires the
either DN or CD4SP 17, a small DP iNKTp cluster (C14) strongest TCR signaling compared to iNKT1 and
was indeed uncovered in ST0 (Fig. 3c–e and Supple- iNKT1724,25,itislikelythatPLZFhiiNKTpinCD4SP(C9)
mentary Fig. S4a–d). To rule out the possibility that C14 prefer to commit into the iNKT2 cell lineage.
DP iNKTp might be the contaminated un-signaled DP RORγt is a key transcription factor to regulate iNKT17
thymocytes, we analyzed the usage of TCR Vβ8s/β7 in differentiation but is also highly expressed in un-signaled
both rec-Vα14Tg and C57BL/6 mice, and found that the DP thymocytes and promotes iNKT cell selection26.
Vβ repertoire of DP iNKTp was similar to non-DP ST0 Unlike Zbtb16, Rorc (encode RORγt) at the +4kb region
iNKTp and mature iNKT cells. More importantly, the was accessible in both DP (C14) and DN (C2 and C4)
expression of TCR Vβ chains in DP iNKTp was sig- iNKTp,butnotintheCD4SP(C9)cluster,while+13kbto
nificantly higher than that in un-signaled DP thymo- Rorc was only accessible in DP iNKTp (C14). The Rorc
cytes18 (Supplementary Fig. S5a, b). In addition, this expression pattern is consistent with its chromatin
cluster also highly expressed recombinase subunits (e.g., accessibility status in each cluster (Fig. 3l). Rorc was sig-
Rag1, Rag2, and Dntt) (Supplementary Fig. S6) and early nificantly highly expressed in DP iNKTp and was gradu-
T-cell decision molecule Ly6d19 (Fig. 3b), indicating that allydownregulatedintheDNbranch(C4andC2)butwas
C14 DP iNKTp had recently been TCR signaled. There- barely detected in CD4SP (C4) (Fig. 3m), which was fur-
fore, we assumed that C14 ST0 iNKT cells could be the ther validated by flow cytometry (Fig. 3n). Interestingly,
transient iNKT precursors from DP thymocytes, which the distinct PLZFintRORγthi iNKT population in DN
were recently positively selected to iNKT cell lineage. iNKTp exhibits a similar phenotype to the mature
Wangetal.CellDiscovery (2023) 9:61 Page6of20
Fig.3(Seelegendonnextpage.)
Wangetal.CellDiscovery (2023) 9:61 Page7of20
(seefigureonpreviouspage)
Fig.3CellulardiversityofiNKTcellsatST0.at-SNEplotsfromscRNA-seqdatasetfromsortedST0iNKTprecursors(iNKTp).bFeatureplots
depictingspecificgeneexpressionineachclusterinST0iNKTp.cFeatureplotdepictingsingle-cellgeneexpressionofCd4,Cd8aandtheirco-
expression(top).Bargraphrepresentstheaverage(Ave)expressionofCd4andCd8aintheclusters(bottom).dRepresentativeflowplotsofCD4vs
CD8expression.Thebargraphrepresentsmeans±SD,n=19.Datarepresentsevenindependentexperiments(bottom).DPCD4+CD8+double
positive,DNCD4−CD8−doublenegative,CD4SPCD4+singlepositive.eViolinplotsofCd8expressionineachcluster-derivedST0iNKTcellsfrom
C57BL/6mouse(red)andrec-Vα14Tgmouse(green).fTheorderingofST0iNKTpalongpseudotimeinastate-spacedefinedbyMonocle3.Each
colorrepresentsacluster.gThesamepseudotimeplotasin(f),featureplotsdepictingsingle-cellgeneexpressiontrajectoryofCcr7inST0iNKTp
development(left).ThebargraphrepresentsAveexpressionofCcr7(right).hRepresentativeflowplotsofCcr7expressioninST0iNKTp(left).Bar
graphpresentsmeanCCR7+iNKT±SD,n=3(right).i,lAggregatescATAC-seqbrowsertracksforZbtb16(i)andRorc(l)inST0iNKTpclusters.Thebar
graphrepresentsZbtb16(i)andRorc(l)Aveexpression(right).j,mThesamepseudotimeplotasinf;featureplotsdepictingsingle-cellgene
expressionofZbtb16(j)andRorc(m)intheST0iNKTpdevelopmenttrajectory.k,nRepresentativeflowplotsofPLZF(k)andRORγt(n)expression
patternsinST0iNKTp(bottom).BargraphsrepresentmeanPLZF+iNKT±SD(k)andmeanRORγt+iNKT±SD(n)(top).n=5,datarepresentthree
independentexperiments.
iNKT17 cells (Supplementary Fig. S7b). Thus, it is likely chromatinwasmuchmoreaccessiblecomparedwiththat
that iNKT17 commitment underwent the DP-DN devel- of other ST1 clusters (Supplementary Fig. S9c). The
opmentalprograminST0(C14-C4-C2).T-bet(encodedby dynamic expression pattern of Zbtb16, Tbx21, and Rorc
Tbx21) is a key transcription factor to regulate iNKT1 cell described three iNKT subset developmental trajectories,
differentiation27. Interestingly, we did not observe obvious respectively (Supplementary Fig. S10a). Zbtb16hi iNKT2
Tbx21 expression in any clusters or open regions near (C3, C6, C7, C10, C11, C15, and C16) may initiate their
Tbx21 in ST0 iNKTp (data not shown). Overall, our development from both DP-CD4SP (predominately) and
pseudotime-based analysis of developmental trajectories DP-DN branches in ST0 and continued throughout ST1
revealed that there might be two potential development and ST2. Interestingly, C6 cells were terminally ended at
programs in ST0, at which iNKT cells may initiate their ST1 as DN iNKT cells (Supplementary Fig. S10a, b);
commitment to iNKT2 and iNKT17 cells that occur as Tbx21 + iNKT1 cells start from CD4SP in ST1 and
early as ST0 and may initiate iNKT1 cells post ST0. undergo brisk proliferation transitioned through iNKT2
However,thishypothesisisstillunderfurtherinvestigation. clusters prior to the terminal iNKT1 differentiation in
ST3. Among the iNKT1 pool, C12 as DN iNKT cells
iNKT cell developmental trajectory reach the end of the developmental journey (Supple-
+
We understand that iNKT cells that are presorted from mentary Fig. S10a, b). Rorc iNKT17 cells (C13) rooted
ST0, ST1, ST2, and ST3 may not perfectly present the from the DP-DN branch in ST0 became terminally dif-
actualdevelopmentalpathoftheirdevelopment.Totestthe ferentiated at ST2 as DN iNKT cells (Supplementary Fig.
robustnessofourapproachandanalyzewhetherthesecells S10a, b). Collectively, our pseudotime-based analysis of
can unveil the model of iNKT cell development, we pro- developmental trajectories revealed that both iNKT1 and
jectedcellsfromdifferentdevelopmentalstagesonUniform iNKT17cellswereattheendsofthetrajectory,indicating
Manifold Approximation and Projection (UMAP) of a that they were well differentiated. However, the majority
recently published study from unbiased iNKT cells thymic of iNKT2 clusters (except C6) were centrally positioned
population14. We found a similar distribution of develop- along the iNKT cell differentiation axis suggesting a high
mentalstagesandclustersalongtheiNKTcelldevelopment plasticity in iNKT2 cells.
(Supplementary Fig. S8a–c). Furthermore, the gene Furthermore, an alternative computational approach,
expressionsofcellsineachstageforthosetwodatasetsare URD28, was performed, whereby cluster C14 from ST0
highly correlated (Pearson’s r≥0.95; Supplementary Fig. was used as the root point. Consistently, C13 (iNKT17)
S8d). Thus, we thereafter focused our stage-based was the first to branch off from the trunk, followed by
iNKT cells, which also provided another clue (e.g., stage iNKT2 clusters (C10, C6, and C3), and subsequently, the
related) for iNKT cell development. We found that iNKT1 clusters (C1, C5, C8, and C12) emerged. Notably,
iNKTcells,especiallyforiNKT1cells,werefollowinglinear clusterC5wasbranchedoutearlierthanC1,C8,andC12
“stage” of development; however, iNKT2/17 cells were (Supplementary Fig.S10c).Overall,usingURDapproach,
terminated their differentiation at ST2. we further validated iNKT cell thymic development
TounderstandtheiNKTsubsetdevelopmentpostST0, trajectory.
we mapped aggregated thymic iNKT cells (ST0–3) into a
pseudotime trajectory (Fig. 4a and Supplementary Cellular diversity in iNKT2 cells
Fig. S9a, b). Two branches stemming from ST0 were iNKT2 cells showed an extensive diversity, including C3,
merged into a narrow window-C16 at ST1, where Ccr7 C6,C7,C10,C11,C15,andC16clusters(Figs.2band4a,b).
Wangetal.CellDiscovery (2023) 9:61 Page8of20
Fig.4(Seelegendonnextpage.)
Wangetal.CellDiscovery (2023) 9:61 Page9of20
(seefigureonpreviouspage)
Fig.4CellulardiversityintheiNKT2cells.aTheorderingofiNKTcellsalongpseudotimeinastate-spacedefinedbyMonocle3.Eachcolor
representsaniNKTcluster(left)andstage(right).bThesamepseudotimeplotasin(a);featureplotsdepictingsingle-cellgeneexpressiontrajectory
ofZbtb16iniNKTcelldevelopment.cAggregatescATAC-seqbrowsertracksforZbtb16foriNKTcellclusters(left).BargraphrepresentsZbtb16
average(Ave)expressioniniNKTcellclusters(right).dUMAPprojectioncoloredbytheactivityofGATA3-bindingmotifs.eHeatmapshowing
pseudotimeorderingofmostDEGsselectedfromiNKT2clustersC3,C6,C10,andC16ofscRNA-seqdata.fFeatureplotsdepictingsingle-cellgene
expressiontrajectoryofG1,G2/M,andSphagesinaggregatediNKTcelldevelopment(left).BargraphrepresentsfractionofG1,G2/MandScellsin
iNKTcellsclusters(right).gDEGsinclusterC3,C6,C10,andC16.Pathwayenrichmentisexpressedasthe–log10(Pvalue)adjustedformultiple
comparison.
We first assessed Zbtb16 chromatin accessibility in inte- C5,C8,andC12)(Figs.2band5a).Within17.2kbofthe
gratediNKTcellclusters(C1–C16).In181kboftheZbtb16 Tbx21locus,thepromoterregions–3kband–4kbwere
locus,wefoundhighlyaccessibleregionsiniNKT2,iNKT1 highly accessible in C1, C5, and C12, but were less
and iNKT17 clusters, but much weaker regions in ST0 accessible in C8 (Fig. 5b). The same regions were also
clusters (C2, C4, C9, and C14). Zbtb16 expression was accessible in hyper-proliferative C7, C11, and C15
closely matched to its chromatin accessibility (Fig. 4c). iNKT2 clusters in ST1 and ST2. Importantly, Tbx21-
iNKT2 clusters and C2 and C9 in ST0 displayed high binding motif activity also occurred in these clusters,
activityofGATA3motif-bindingactivity,whichiscriticalfor butnotinST0clusters(Fig.5c).Flowcytometryanalysis
iNKT2 differentiation5 (Fig. 4d). As expected, most sig- further confirmed that a small fraction of PLZFhiiNKT2
nature genes for iNKT2 cells gradually increased until cells express T-bet in ST1 and ST2, with considerable
reachingtheirpeaksatanintermediatestage,followedbya proliferation ability as measured by Ki-67 (Fig. 5d).
down-regulation during the terminal differentiation. A few Therefore, it is possible that iNKT1 progenitors might
genes, however, including Btg1, Cebpb, and Osgin1, only hide in these so-called proliferative PLZFhiT-bethi
appearedneartheiNKTdevelopmentalend,whichmaybe iNKT2 cells.
related to iNKT2 cell terminal
events29–31
(Fig. 4e). Pseudotime analysis showed that most iNKT1 sig-
PreviousstudiesindicatedthatiNKTcellsinST1and natures were not highly expressed until reaching the end
ST2 undergo high proliferation. Cell-cycle pathway of the iNKT development continuum (Supplementary
enrichmentanalysissuggestedthatiNKT2clusters(C7, Fig. S12a). We found that a novel signature, signaling
C11, and C15) exhibited highly proliferative char- lymphocytic activation molecule family member 7
acteristics, which were either in S phase (C7) or G2/M (Slamf7),isenrichediniNKT1cellclusters(Fig.5e).Flow
phase (C11 and C15) (Fig. 4f). Ingenuity Pathway cytometry further confirmed this based on the strong
Analysis (IPA) indicated that clusters C3, C6, C10, and correlation between SLAM7 and NK1.1 expression in
C16 are functionally different. C16 is a transient phase PLZFloT-bethi iNKT1 cells (Fig. 5f). NK cell-related sig-
of iNKT cells from ST0 to ST1, and these cells sharply nature Slamf4 further distinguished terminal ended C12
+
elevated expression of genes associated with both gly- from other iNKT1 cell clusters. SLAMF4 iNKT cells
colysis and oxidative phosphorylation (Fig. 4g), sug- (C12) were mainly DN, and gradually sprouted out from
gesting their increased energy demands32. C6 PLZFloT-bethi iNKT1 cells (Fig. 5g–i and Supplementary
+
terminated at ST1, and these cells enriched with genes Fig.S12b,c).SLAMF4 iNKT1cellsmainlysecretedIFN-
in TCR signals, co-stimulation signaling, cytoskeleton, γ with less IL-4, like “classical iNKT1 cells”, while the
−
TNFR, and cell death and exhaustion pathways (Fig. majorityofSLAMF4 iNKT1cellssecretedbothIL-4and
4g).ThisclusterhighlyexpressesCd74(Supplementary IFN-γ upon stimulation (Fig. 5j). Furthermore, a small
Fig. S11a), a gene associated with class II major histo- population of SLAMF4 + PLZFloT-bethi iNKT1 cells also
compatibility complex and related to T cell–T cell expressed soluble cytotoxic mediator Gzma, identified as
interaction33. Consistently, flow cytometry analysis a cytotoxic iNKT1 population (Supplementary
further confirmed that the majority of CD74 + Fig.S12d–f).However,thesecytotoxicGZMA + SLAMF4 +
iNKT cells were in ST1 (Supplementary Fig. S11b). iNKT1cellswerebarelydetectedintheperipheralorgans
However, the functional profiles of C6 are still under (Supplementary Fig. S12g). C5 cells were enriched with
investigation. Taken together, iNKT2 exhibit a great Ifit1 and Ifit3, which are involved in the interferon sig-
cellular diversity. naling pathway34 (Fig. 5k and Supplementary Fig. S12h).
Overall, iNKT1 cells start their journey from as currently
Heterogeneity of iNKT1 cells defined “iNKT2 cells” at ST1, and gradually complete
+
iNKT1 cell differentiation was controlled by tran- their differentiation and turninto SLAMF4 iNKT1 cells
scriptionfactorTbx21andassignedtofourclusters(C1, at the end, as classical IFN-γ-secreting iNKT1 cells.
Wangetal.CellDiscovery (2023) 9:61 Page10of20
Fig.5(Seelegendonnextpage.)
Wangetal.CellDiscovery (2023) 9:61 Page11of20
(seefigureonpreviouspage)
Fig.5ExtensivecellularheterogeneityofiNKT1cells.aThesamepseudotimeplotasinFig.4a;featureplotsdepictingsingle-cellgene
expressiontrajectoryofTbx21iniNKTcelldevelopment.bAggregatescATAC-seqbrowsertracksforTbx21foriNKTcellclusters(left).Bargraph
representsTbx21average(Ave)expressioniniNKTcellclusters(right).cUMAPprojectioncoloredbytheactivityofTbx21-bindingmotif.
dRepresentativeflowplotsofPLZFvsT-betgatedoniNKTcells,iNKT2(PLZFhiT-bet−)ingreenanddifferentiNKT1(T-bethi)cells,markedbyPLZF
high(PLZFhiT-bethi)inblue,PLZFmedium(PLZFintT-bethi)inpurple,andPLZFlow(PLZFloT-bethi)inred(topleft).HistogramshowingKi-67expression
intheindicatediNKTsubsetsderivedfromtheright.RepresentativeflowplotsofCD44vsNK1.1expressionintheindicatediNKTsub-population
derivedfromtop(bottom).eThesamepseudotimeplotasinFig.4a;featureplotsdepictingsingle-cellgeneexpressiontrajectoryofSlamf7iniNKT
celldevelopment.fRepresentativeflowplotsofSLAMF7vsNK1.1expressioniniNKTcells.PLZFhiT-betloinorange,PLZFhiT-bethiinblue,PLZFint/
loT-bethiinred.gBargraphrepresentsSlamf4AveexpressioniniNKTcellclusters.hRepresentativeflowplotsofSLAMF4expressioniniNKT2
(PLZFhiT-bet−)ingreenanddifferentiNKT1(T-bethi)cells,markedbyPLZFhigh(PLZFhiT-bethi)inblue,PLZFmedium(PLZFintT-bethi)inpurple,and
PLZFlow(PLZFloT-bethi)inred.iDotgraphrepresentsmeanSLAMF4+±SD.n=9,Datarepresentthreeindependentexperiments,andwere
analyzedbyatwo-sidedpairedttest,****P<0.0001.jRepresentativeflowplotsofIL-4vsIFN-γproductioninSLAMF4−(left)andSLAMF4+(right)
iNKT1cellspostPMA/Ionomycinstimulationfor4h,n=5,Datarepresentthreeindependentexperiments.kDEGsinclustersC1,C5,C8,andC12.
Pathwayenrichmentisexpressedasthe–log10(Pvalue)adjustedformultiplecomparison.
iNKT17 cells exhibit limited heterogeneity DNA-binding capacity of RUNX (RUNX1, RUNX2, and
C13 was assigned as iNKT17 cells, which was segre- RUNX3), and therefore modulates the transcription of
gated distinctively from other clusters (Figs. 2b and 6a). their target genes. Here we observed that Runx1 shows a
Weobservedthat+4kband+14kbregionsofRorcwere similarexpressiontrajectoryasCbfβinthymiciNKTcells
accessible in ST0 clusters (C2, C4, and C14) and mature (Supplementary Fig. S13a) even though the expression
iNKT17 cluster (C13) (Fig. 6b), and binding motifs of level is relative lower. More interestingly, consistent with
RORCwereactivatediniNKT17clusteraswellasinST0 the high expression of Cbfb in C2, we observed a greater
iNKTp (Fig. 6c). These data suggested that iNKT cells RUNX1-binding activity in C2, compared with in other
maystarttheiriNKT17commitmentatST0andcomplete clusters in ST0 (Supplementary Fig. S13b). In mammals,
their differentiation at C13. At mRNA level, Rorc was two RNA splice variants, Cbfβ1 and Cbfβ2, are generated
highlyexpressedinC14inST0,whichwasconsistentwith from a single Cbfβ gene, and each variant has distinct
the chromatin accessibility at Rorc, but was gradually amino acid sequences at the C terminus36. To determine
downregulated in C4 and C2, and re-upregulated in C13, if Cbfβ regulates iNKT development, we examined iNKT
indicatingthatothertranscriptionfactor(s)maytargetthe cell development in thymic-specific Cbfβ knockout mice
open Rocr sites and manipulate Rorc expression during (CD4CreCbfβ f/f, Cbfβ KO), in which both Cbfβ1 and
iNKT17 differentiation. Cbfβ2 were deleted. Cbfβ deletion was further confirmed
To trace the developmental trajectory of iNKT17 cells, inproteinlevelandmRNAlevelindifferentT-cellsubsets
wefurthercheckediNKT17signaturegenesinanordered (Supplementary Fig. S14a, b). We observed that conven-
iNKTcelltrajectoryandfoundthatfewiNKT17signatures tional αβT cells with Cbfβ deletion phenotypically
includingRorcwereinitiallyexpressedintheearlyiNKTp, mimicked those in RUNX3 KO mice37, as Cbfβ KO mice
before they reached the mature iNKT17. However, the displayedabnormalitiesinCD4expression,impairmentof
majority of iNKT17-related signatures were barely CD8Tcellsmaturationinthymus,andalargeproportion
expressed in iNKTp (Fig. 6d). We further found that a of DP cells in peripheral (Supplementary Fig. S14c, d).
novel signature aquaporin-3 (Aqp3) was specifically Interestingly,deletionofCbfβledtoaseverereductionin
expressed in thymic iNKT17 (PLZFintRORγt + ) cells the frequency and absolute number of thymic iNKT cells
(Fig. 6e, f). Overall, iNKT cells likely initiate iNKT17 (Fig. 7c), as well as in the peripheral lymphoid organs
commitment at ST0 and these iNKT17 cells exhibits lim- (Supplementary Fig. S14e), which phenotypically
ited heterogeneity. mimicked iNKT cells in Runx1 deletion mice38, but not
Runx3 KO mice. This phenomenal explained a similar
Cbfβ regulates iNKT cell early commitment expression pattern of Cbfβ and Runx during iNKT cell
Egr2 and Slamf6 were reported to control early iNKT developmentandhigherbindingactivityofRUNX1atC2
cell development by modulating Zbtb16 expression and ST0(SupplementaryFig.S13a,b).Amorecomprehensive
TCR in ST015,16,35. Here, we identified a novel co- analysis revealed a selective and significant reduction in
transcription factor, Cbfβ, which showed a similar the frequency and absolute number of ST2 and ST3
expression pattern with Egr2and Slamf6,and exhibited a iNKTcellsinCbfβKOmice.ThefrequenciesofST0and
great enrichment at ST0 of iNKT cells, specifically in the ST1 iNKT cells were significantly increased in Cbfβ KO
DP-DN branch C2 (Fig. 7a, b). mice,buttheabsolutenumberswerecomparablebetween
Cbfβ-encoded CBFB is a non-DNA-binding regulatory Cbfβ KO and WT controls (Fig. 7d). Of interest, DP
subunit that allosterically enhances the sequence-specific iNKTp were increased in ST0 iNKT cells in Cbfβ KO
Wangetal.CellDiscovery (2023) 9:61 Page12of20
Fig.6iNKT17cellsexhibitlimitedheterogeneity.aThesamepseudotimeplotasinFig.4a;featureplotsdepictingsingle-cellgeneexpression
trajectoryofRorciniNKTcelldevelopment.bAggregatescATAC-seqbrowsertracksforRorcforiNKTcellclusters(left).BargraphrepresentsRorc
average(Ave)expressioniniNKTcellclusters(right).cUMAPprojectioncoloredbytheactivityofRORC-bindingmotif.dHeatmapshowing
pseudotimeorderingoftop30genesincluster13ofscRNA-seqdata.eThesamepseudotimeplotasinFig.4a;featureplotsdepictingsingle-cell
geneexpressiontrajectoryofAqp3iniNKTcelldevelopment.fRepresentativeflowplotsofAqp3expressioniniNKT1(PLZF−RORγt−,gray),iNKT2
(PLZFhiRORγt−,orange)andiNKT17(PLZFintRORγt+,purple).BargraphrepresentsmeanAqp3+iNKT±SD,n=8.Datarepresentthreeindependent
experiments,andwereanalyzedbyatwo-sidedpairedttest,****P<0.0001.
mice (Fig. 7e), suggesting that the deletion of Cbfβ par- PLZF expression at ST1 was significantly downregulated
tiallyblocksDPiNKTpconversiontoeitherCD4SPorDN inCbfβKOiNKTcells(Fig.7f).Similarphenomenonwas
lineages. We assume that Cbfβ may affect iNKT cells also observed on a proliferating marker, Ki-67 (Fig. 7g).
selectionatDP.Egr2showedasimilarexpressionpattern These data suggested that Cbfβ-deficient iNKT cells
as Cbfβ in ST0 (Fig. 7a), and is critical for iNKT lineage entered a relative quiescent status and were unable to
commitment at DP35, we therefore detected Egr2 normally upregulate PLZF expression at ST1. Further-
+
expression at DP stage. As shown in Supplementary more, the remnant PLZF iNKT cells in ST1 fail to
Fig.S14f,Egr2expressionwassignificantlyreducedinDP co-express T-bet to initiate iNKT1 differentiation and to
thymocytesfromCbfβKOmice,indicatingthatEgr2may co-express RORγt to initiate iNKT17 differentiation
involve in Cbfβ-mediated iNKT cell development. (Fig. 7h, i and Supplementary Fig. S14g). Bone marrow
ST1 iNKT cell undergoes briskly proliferation and chimera transfer experiments showed that there was a
contains the progenitors of iNKT subsets with high sever defect on iNKT cell development from the Cbfβ-
Zbtb16-encodedPLZFexpression.Hereweobservedthat deficient donors (Supplementary Fig. S15a, b), suggesting
Wangetal.CellDiscovery (2023) 9:61 Page13of20
Fig.7(Seelegendonnextpage.)
Wangetal.CellDiscovery (2023) 9:61 Page14of20
(seefigureonpreviouspage)
Fig.7CbfβregulatesiNKTcellearlycommitment.aiNKTST0pseudotimeplot;featureplotsdepictingsingle-cellgeneexpressiontrajectoryof
Cbfβ,Egr2,andSlamf6atST0iNKTcellsdevelopment(Fig.3f).bViolinplotsofCbfβexpressionindifferentstagesofiNKTcells,andCbfβexpressionin
differentclusters(C2,C9,C4,andC14)fromST0iNKTcells.cRepresentativeflowplotsofiNKTcellsfromCbfβKOandWTmice(left).Bargraphs
representmean±SDofiNKTcellfrequencyandiNKTcellnumber(right),n=5forCbfβKOandWTcontrols.Datarepresentthreeindependent
experiments.dRepresentativeflowplotsofdifferentstagesofiNKT(afteranti-CD1d-tetramerenrichment)fromCbfβKOandWTmice(left).Bar
graphsrepresentmean±SDofiNKTcellfrequencyandiNKTcellnumberinCbfβKOandWTcontrols(right).eRepresentativeflowplotsofCD8and
CD4expressioninST0iNKTcellsfromCbfβKOandWTcontrols(left).Bargraphrepresentsmeans±SDofDP,DN,andCD4SP±SD(right).WT
controls,n=6;CbfβKO,n=7.Datarepresentthreeindependentexperiments,datawereanalyzedbyatwo-sidedunpairedttest,*P<0.05.
f,gHistogramshowingPLZFexpression(f)andKi-67expression(g)inST1iNKTcellsfromCbfβKOandWTmice.Bargraphrepresentsmeans±SDof
indicatediNKTpopulation.WT,n=4.CbfβKO,n=6.Datarepresenttwoindependentexperiments,andwereanalyzedbyatwo-sidedunpairedt
test,*P<0.05,***P<0.001.hRepresentativeflowplotsofPLZFvsT-betexpressioninST1iNKTcellsfromCbfβKOandWTmice.iRepresentativeflow
plotsofPLZFvsRORγtexpressioninST2iNKTcellsfromCbfβKOandWTmice.jThespeculatedschematicmodelofmouseiNKTcelldevelopmental
trajectory(left)andtheroleofCbfβiniNKTcelldevelopment(right).
that the defective iNKT cell development in Cbfβ KO iNKT1/2/17 into different clusters from different devel-
mice was cell-intrinsic. Overall, our study suggests that opmental stages based on published signature markers.
Cbfβ serves as a key regulator to control early iNKT cell And this could allow us to trace iNKT1/2/17 differ-
development at ST0, iNKT cell differentiation at ST1/2, entiation trajectory in different stages and identify their
and final maturation at ST3 (Fig. 7j). progenitors. With the integration of single-cell tran-
scriptome and chromatin accessibility analysis, we found
Discussion
that iNKT2 and iNKT17 lineage commitment may occur
iNKT cell development was previously considered as a in ST0 by two distinct programs, and iNKT1 lineage
linear model with four successive stages (ST0–ST3). commitment may occur post ST0. Finally, we identified
However,recentstudieshaveindicatedthatthymiciNKT thattranscriptionfactorCbfβplaysakeyroleiniNKTcell
cell development is a complex cellular differentiation commitment.
process and the linear developmental model does not Previous studies suggested that iNKT cells arise from a
apply to all iNKT subsets13. A new functional classifica- common progenitor designated as PLZFhiCD24 + in ST0,
tion of three terminally differentiated subsets, iNKT1/2/ which further differentiate into iNKT1/2/17 subsets5,40.
17,wasproposedbasedontranscriptionfactorexpression However,itisstillunclearhowandatwhichspecifictime
and cytokine production patterns12,26. Very recently, window their effector programs unfold during their
Thomas Baranek et al. performed scRNA-seq on thymic development. In our current study, we found that ST0
whole iNKT cells pool and proposed a model for iNKT iNKTp exhibit extreme heterogeneity, suggesting that
cell effector differentiation in which iNKT1 and iNKTp may be destined to the specific subset lineages in
iNKT17 subsets derive from iNKT2. Moreover, ST0. A rare DP iNKT cell population that has been
iNKT1subsetariseslinearlyandsequentiallyfromiNKT2 ignoredpreviouslyandhiddeninST0islikelytheearliest
cells39. This study yielded strong evidence for iNKT cell iNKTp post-positive selection. These DP iNKTp then
development and differentiation models. However, are differentiate to either CD4SP or DN iNKTp in ST0, and
iNKT2 cells the earliest cells pool for iNKT1/17 lineages form two distinct developmental programs, DP-CD4SP
commitment? If no, how early can their progenitor be andDP-DN.Thetwodevelopmentalbranchesdifferedin
identified? To this end, we applied both scRNA-seq and many aspects including distinct transcriptomes, diversity
scATAC-seq analyses of thymic iNKT cells and mapped of TCR Vβ usage, and TCR signaling strength. Interest-
the developmental landscape of terminal iNKT1/2/ ingly, Zbtb16 upregulation only occurred at the end of
17 subsets on iNKT development. We did single-cell DP-CD4SPandDP-DNdevelopmentalbranches.Zbtb16 +
analysis based on “stages” of development, given the fol- iNKTp in the CD4SP path showed a stronger TCR sig-
lowing reasons: (1) There might be some key features of nalingstrengthandincreasedVβ7usagecomparedtothat
iNKT cells at the very early stage, which only take up in DP-DN iNKTp, suggesting that the iNKTp in the DP-
about 0.5% of total iNKT cells in mouse thymus, and CD4SP development program prefer to differentiate into
sorting whole iNKT cells as a pool may hide key features iNKT2 cells. However, Rorc chromatin accessibility and
inthisrarepopulation.Thus,sortingiNKTcellsbasedon geneexpressionarehighlyenrichedinDPiNKTpandthe
the stages would make sure that enough iNKT cells at DP-DNdevelopmentalbranch,supportingthenotionthat
earlierstageswereincludedforfurtherclusteringanalysis; iNKTp in the DP-DN branch prefer to be differentiated
in this case, we included a total of 7591 ST0 cells for into iNKT17 cells. We did not observe any open-
scRNA-seq and scATAC-seq analysis; (2) By pooling chromatin regions near Tbx21 and its gene expression
differentstagesofiNKTcells,wewerealsoabletoassign in ST0 iNKTp, but Tbx21 chromatin accessibility and its
Wangetal.CellDiscovery (2023) 9:61 Page15of20
gene expression occurred as early as ST1. These findings however, important to point out that Nfil3 was surpris-
highly suggest that iNKT2 and iNKT17 are pre- ingly foundto be enriched inthymic iNKT17clusterand
determined at ST0; however, iNKT1 are progressively a small fraction of iNKT1 cells. However, IL-10 expres-
determined at ST1. sion was undetectable in thymic iNKT cells (data not
AlthoughthreesubsetsofiNKTcellsweredefinedpost shown). It is still unknown whether these Nfil3 +
ST0 based on transcription factor and cytokine secretion iNKT cells can be converted into iNKT10 cells following
profiles, iNKT1 and iNKT2 cells exhibit extensive phe- αGalcer stimulation. More comprehensive study is still
notypic and functional heterogeneity, while iNKT17 cells ongoing.
are relatively homogenous. The trajectory of iNKT Collectively, ourstudy generated a comprehensive atlas
development showed that iNKT17 and iNKT1 branches of thymic iNKT cells and their developmental trajectory,
were both sprouted from the developmental tree. How- providing a valuable resource for future studies of iNKT
ever,theiNKT2cells,whichwerehighlyproliferativeand cell biology. We have also uncovered Cbfβ as a novel
heterogeneous, were located at the center of develop- regulator of early iNKT cell development (Fig. 7j).
mentaltrunk.Interestingly,wefoundthatbothTbx21and
Materials and methods
Rorcchromatinswerealsoaccessibleintheseproliferative
iNKT2clusters,indicatingthattheseproliferativeclusters Mice
hidden in so-called “iNKT2 cells” might contribute to C57BL/6werepurchasedfromJacksonLaboratory(Bar
early iNKT1/2/17 expansion and differentiation. These Harbor, ME). Rec-Vα14Tg TCR transgenic mice were
results further supported a recent notion that currently generated in Dr. Derek Sant’Angelo laboratory9, which
defined iNKT2 cells may contain mature iNKT2, transi- require Rag-mediated recombination to produce a func-
tioning iNKT17, and transitioning iNKT141. Aqp3 tional TCR (Supplementary Fig. S1a). These mice have
belongs to a family of highly conserved transmembrane increased numbers of iNKT cells, as compared with
channels that transport water and, in some cases, small C57BL/6mouse.Micecarryingaconditionalfloxedallele
solutes such as glycerol. Recent studies indicated that of Cbfβ (Cbfβfl/fl ) were previously described45 and pro-
Aqp3 is expressed on T cells and regulates their traf- vided by Dan R. Littman (New York University, New
ficking in skin and lung immune reactions42,43. T-cell York, NK). Mice were backcrossed to the C57BL/6
migration toward chemokines is dependent on Aqp3- backgroundfor7generationsandthenmatedtoC57BL/6
mediated hydrogen peroxide (H O ) uptake. Here, our mice carrying the Cd4 enhancer/promoter/silence Cre
2 2
fate-mappingidentifiedthatAqp3,asanewbiomarker,is allele (obtained from The Jackson Laboratory), to gen-
specifically expressed in iNKT17 cells. It will be very erate CD4CreCbfβ fl/fl conditional knockout mice (Cbfβ
interesting to further investigate Aqp3’s functions in KO). The full list of mouse strains used can be found in
iNKT17 cells, especially for their trafficking to peripheral Supplementary Table S1. 5-week-old, sex-matched mice
organs. were utilized in this study. All studies, protocol, and
iNKT cells express multiple Slam family receptors, but mouse handling were approved by the Institutional Ani-
only Slamf1, Slamf5 and Slamf6 are highly expressed in mal Care and Use Committee.
ST0 iNKTp (data not shown), which have been reported
to be required for iNKT cell development15. Here, we Flow cytometry gating strategy and antibodies
found that Slamf7, as a new marker, is specifically Single-cell suspensions were washed twice with FACS
expressed in iNKT1 cells. Most importantly, we found staining buffer (1× PBS, 2% FBS) and incubated with Fc
that Slamf4 was enriched in terminal DN iNKT1cluster block (clone 2.4G2). Cells were stained with anti-mouse
(C12). Given the dynamic transcription factor expression PBS57-loadedand-unloadedCD1d-tetramer(providedby
and cytokine production profiles, the Slamf4 + the NIH Tetramer Core Facility), the following fluores-
iNKT1 cells are likely the terminal differentiated cence conjugated antibodies were used: anti-TCRβ (H57-
iNKT1 cells as “classical iNKT1 cells” that highly secrete 597), anti-CD24 (M1/69), anti-CD44 (IM7), anti-NK1.1
IFN-γ. Interestingly, the few Slamf4 + iNKT1 cells might (PK136), anti-TCR Vβ8.1/8.2 (KJ16-133.18), anti-TCR
receive attention as novel cancer therapeutic targets. Vβ8.3 (1B3.3), anti-TCR Vβ7 (TR310), anti-Nur77
iNKT10 cells are a novel iNKT subset identified upon (12.14), anti-Ly6d (49-H4), anti-CD5 (53-7.3), anti-CD6
stimulation of the strong agonist αGalcer, which are (IM348), anti-Egr2 (erongr2), anti-ID2 (ILCID2), anti-
characterized by transcription factor Nfil3 (also term IL7R (A7R34), anti-Cbfβ, anti-Aqp3, anti-CD8 (53-6.7),
E4bp4) and IL-10 production44. Previous study suggested anti-CD4 (GK1.5), anti-RORγt (B2D), anti-PLZF
that the appearance of iNKT10 after αGalcer stimulation (Mags.21F7), anti-T-bet (eBio4B10 (4B10)), anti-Slamf7
could be the result of selective expansion of a rare (520914),anti-Slamf4(eBio244F4),anti-CD45.1(A20),and
population of pre-existing iNKT10 cells or some non- anti-CD45.2 (104). Cell surface staining was performed
iNKT10cellsconvertingintotheiNKT10phenotype.Itis, with staining buffer; intranuclear staining for anti-Aqp3,
