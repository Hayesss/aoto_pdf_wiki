---
source_path: /mnt/c/Users/Administrator/Zotero/storage/HIRABJ46/PIIS009286741830446X.pdf
ingested: 2026-04-23
sha256: c27c6e53c1faaf97
---

Resource
Integrated Single-Cell Analysis Maps the Continuous
Regulatory Landscape of Human Hematopoietic
Differentiation
Graphical Abstract Authors
JasonD.Buenrostro,M.RyanCorces,
HSC CalebA.Lareau,...,RavindraMajeti,
HowardY.Chang,WilliamJ.Greenleaf
Correspondence
jbuen@broadinstitute.org(J.D.B.),
wjg@stanford.edu(W.J.G.)
Myeloid Erythroid
In Brief
Integrativeanalysisofsingle-cell
transcriptomicsandchromatin
accessibilityprovidesinsightsinto
regulatoryfeaturesanddynamicsin
humanhematopoiesis.
Highlights
d Single-cellchromatinaccessibilityrevealsaheterogeneous
hematopoieticlandscape
d TFmotif-associatedchromatinvariabilityinHSCsfollows
erythroid/lymphoidpaths
d CharacterizationoftwoGMPsubsetswithchromatinand
transcriptomedifferences
d
Integrativeanalysisenablesregulatoryinsightsintocis-and
trans-actingfactors
noitaitnereffiD
i) cell type analysis
HSC
CMP
GMP
FACS scATAC-seq clusters
Lymphoid
single-cell ATAC-seq
ii) TF dynamics
+
single-cell RNA-seq
iii) enhancer-gene correlation
A A A
A A A
FACS known cell types Integrated single-cell analysis
expression
Myeloid pseudo-time
Buenrostroetal.,2018,Cell173,1535–1548
May31,2018ª2018ElsevierInc.
https://doi.org/10.1016/j.cell.2018.03.074
Resource
Integrated Single-Cell Analysis Maps
the Continuous Regulatory Landscape
of Human Hematopoietic Differentiation
JasonD.Buenrostro,1,2,*M.RyanCorces,3CalebA.Lareau,1,11BeijingWu,4AliciaN.Schep,4MartinJ.Aryee,1,10,11
RavindraMajeti,5,6HowardY.Chang,3,4,7andWilliamJ.Greenleaf3,4,8,9,12,*
1BroadInstituteofMITandHarvard,Cambridge,MA02142,USA
2HarvardSocietyofFellows,HarvardUniversity,Cambridge,MA02138,USA
3CenterforPersonalDynamicRegulomes,StanfordUniversity,Stanford,CA94305,USA
4DepartmentofGenetics,StanfordUniversitySchoolofMedicine,Stanford,CA94305,USA
5InstituteforStemCellBiologyandRegenerativeMedicine,StanfordUniversitySchoolofMedicine,Stanford,CA94305,USA
6DivisionofHematology,DepartmentofMedicine,StanfordUniversitySchoolofMedicine,Stanford94305,CA,USA
7PrograminEpithelialBiology,StanfordUniversitySchoolofMedicine,Stanford,CA94305,USA
8DepartmentofAppliedPhysics,StanfordUniversity,Stanford,CA94025,USA
9ChanZuckerbergBiohub,SanFrancisco,CA94158,USA
10DepartmentofPathology,MassachusettsGeneralHospital&HarvardMedicalSchool,Boston,MA02115,USA
11DepartmentofBiostatistics,HarvardT.H.ChanSchoolofPublicHealth,Boston,MA02115,USA
12LeadContact
*Correspondence:jbuen@broadinstitute.org(J.D.B.),wjg@stanford.edu(W.J.G.)
https://doi.org/10.1016/j.cell.2018.03.074
SUMMARY ation as a ball rolling down a bifurcating three-dimensional
surface(Goldbergetal.,2007;Waddington,1957).Thisdevelop-
Humanhematopoiesisinvolvescellulardifferentiation mentallandscapedefinesadescriptivepathacellmightfollow,
of multipotent cells into progressively more lineage- choosing different developmental fates as it reaches saddle
restricted states. While the chromatin accessibility points that separate different, increasingly restricted, cellular
landscape of this process has been explored in states. The shape of this landscape is largely defined by tran-
defined populations, single-cell regulatory variation scriptionfactors(‘‘guy-wires’’),whichrecruitchromatineffectors
toreconfigurechromatin(CaloandWysocka,2013;Longetal.,
hasbeenhiddenbyensembleaveraging.Wecollected
2016) and promote new cellular phenotypes (Graf and Enver,
single-cell chromatin accessibility profiles across 10
2009; Takahashi and Yamanaka, 2006). These concepts—the
populationsofimmunophenotypicallydefinedhuman
firstadescriptivenotionofdevelopment (FigureS1A),andthe
hematopoieticcelltypesandconstructedachromatin
second a mechanistic description of the molecular actors that
accessibility landscape of human hematopoiesis to
drivestatechanges(FigureS1B)—haveprovidedaconceptual
characterizedifferentiationtrajectories.Wefindvaria- frameworkforunderstandingcellfatechoices.Recenttechno-
tion consistent with lineage bias toward different logical advances in single-cell epigenomic assays (Kelsey
developmental branches in multipotent cell types. etal.,2017)nowprovidetheopportunitytoascribeepigenomic
We observe heterogeneity within common myeloid features to this landscape by quantifying overall epigenomic
progenitors (CMPs) and granulocyte-macrophage similarity ofindividual cellsduringa normaldifferentiation pro-
progenitors(GMPs)anddevelopastrategytopartition cess,aswellastheactivityofmasterregulatorsthatinfluence
cellfatedecisions.
GMPs along their differentiation trajectory. Further-
Hematopoietic differentiation serves as an ideal model for
more, we integrated single-cell RNA sequencing
exploring the nature of multipotent cell fate decisions (Laurenti
(scRNA-seq) data to associate transcription factors
and Go¨ttgens, 2018; Orkin and Zon, 2008). The hematopoietic
tochromatinaccessibilitychangesandregulatoryele-
system is maintained by the activity of a small number of self-
mentstotargetgenesthroughcorrelationsofexpres-
renewing, long-lived hematopoietic stem cells (HSCs) capable
sionandregulatoryelementaccessibility.Overall,this ofgivingrisetothemajorityofbloodcelllineages(Beckeretal.,
workprovidesaframeworkforintegrativeexploration 1963;LaurentiandGo¨ttgens,2018;OrkinandZon,2008)whereby
of complex regulatory dynamics in a primary human multipotentcellstransitmultipledecisionpointswhilebecoming
tissueatsingle-cellresolution. increasingly lineage-restricted (Figure 1A). The human hemato-
poietic system is an extensively characterized adult stem cell
INTRODUCTION hierarchywithdiversecelltypescapableofphenotypicisolation
withmulti-parameterfluorescenceactivatedcellsorting(FACS)
In1957,ConradWaddingtondevelopedaninfluentialanalogyfor (Corcesetal.,2016;LaurentiandGo¨ttgens,2018).Thiscapacity
developmentalcellbiologybyconceptualizingcellulardifferenti- for phenotypic isolation has enabled measurement of the
Cell173,1535–1548,May31,2018ª2018ElsevierInc. 1535
A
HSC
MPP
LMPP CMP
pDC GMP MEP
Monocyte, mDC Ery,
Granulocytes Mega
TCF4
epigenomicandtranscriptionaldynamicsassociatedwithsorted cell epigenomic measurements that may define cis- and trans-
humanprogenitorsacrossdifferentiationprovidingafoundation regulatory mechanisms underlying transcriptional and cell fate
forthedissectionofregulatoryvariationinnormalmulti-lineage commitmentheterogeneityinhematopoiesis.
cellulardifferentiation(Chenetal.,2014;Corcesetal.,2016;Farlik To define a single-cell chromatin accessibility landscape of
etal.,2016;Novershternetal.,2011).Furthermore,recentwork this developmental hierarchy, we applied a single-cell assay
measuring single-cell transcriptomes has revealed significant fortransposase-accessiblechromatinbysequencing(scATAC-
transcriptionalheterogeneityinisolatedprogenitors(Nottaetal., seq) (Buenrostro et al., 2015b) to 10 sortable populations in
2016) and across differentiation (Laurenti and Go¨ttgens, 2018; humanbonemarroworbloodcomprisingmultipotentandline-
Veltenetal.,2017).Theseobservationssetthestageforsingle- agerestrictedprogenitors.Wefindthattheregulatorylandscape
noitaitnereffiD
sCPSH
+43DC
10 5 10 5
10 4 10 4
3
3 10
10
2
10 0
02 -10 2
-10
3 4 5 3 4 5
0 10 10 10 0 10 10 10
10 5 10 5
10 4 10 4
10 3 10 3
10 2 10 2 -10 02 -10 02
0 10 3 10 4 10 5 0 10 3 10 4 10 5
83DC
CD34
CD45RA
2
0
Fragments
09DC
CD45RA
CD10
CD123
B CD45RA
CLP
B, T Peripheral
NK cells pDC
C Single-cell ATAC-seq E
Human Cell capture Transpose PCR Bone Marrow FACS
D
F
0 400 800 1200 1600
Rank Sorted TF motifs
ytilibairav
llec-lleC
High-throughput Sequencing
Integrated Fluidics Circuit (IFC)
1 2 3 4 5
Number of fragments in peaks, log10
Obs
5 GATA1 Perm
4 CEBPB
BCL11A
3 IRF8
STAT1
2 EBF1
HOXA4
1
skaep
ni
stnemgarf
fo
tnecreP
CLP (8.2%)
pDC (15.8%)
HSC (10.8%)
LMPP (2.1%) CMP (24.3%) GMP
(23.0%)
MPP (3.3%) Unknown MEP (7.1%) (5.3%)
100 Filter (n=1,038) Pass Filter (n=2,034)
80
Freeze & bank 60
40 1
Scale 100 kb hg19
1_chr4: 105,950,000 106,000,000 106,050,000 TET2 0
CD34+ ATAC Density
0_ 20
1_
CD34+ scATAC
HSC (N=347)
MPP (N=142)
LMPP (N=160)
CMP (N=502)
GMP (N=216)
MEP (N=138)
CLP (N=78)
pDC (N=141)
Monocyte (N=64)
Unkown (N=60)
Figure1. Single-CellATAC-SeqProfilesChromatinAccessibilitywithinSingleHematopoieticProgenitors
(A)Aschematicofhumanhematopoieticdifferentiation.
(B)SortingstrategyforCD34+cells.
(C)Single-cellATAC-seqworkflowusedinthisstudy.
(D)Single-cellepigenomicprofilesalongtheTET2locus.
(E)Percentfragmentsinpeaksbynumberoffragmentsinpeaks,redlinesshowcutoffsusedfordeterminingwhichcellspassfilter;pointsarecoloredbydensity.
(F)TFmotifvariabilityanalysisinallsingle-cellepigenomicprofilescollectedforthisstudy.
SeealsoFigureS1andTableS1.
1536 Cell173,1535–1548,May31,2018
ofhumanhematopoiesisiscontinuous,withcellsurfacemarkers mappingtopeaks,resultinginamedianof6,442fragmentsin
reflecting ‘‘basins’’ within thislandscape. Thissingle-cell anal- peakspercell(Figure1E;seeSTARMethods).
ysis also uncovered substantial heterogeneity within immuno-
phenotypicallydefinedcellularpopulations,includingvariability TFActivityInferenceUsingChromVAR
withinmultipotentprogenitorsstronglycorrelatedalongthedi- We applied ChromVAR to calculate TF motif-associated CAL
mensions of hematopoietic differentiation—an observation changes and identify potential regulators of epigenomic vari-
consistentwithlineageprimingatthelevelofchromatinacces- ability (Buenrostro et al., 2015b; Schep et al., 2017). This
sibility. We observe especially strong variability within popula- approach quantifies accessibility variation across single-cells
tions of immunophenotypically defined common myeloid byaggregatingaccessibleregionscontainingaspecificTFmotif,
progenitor (CMP) and granulocyte-macrophage progenitor thencomparestheobservedaccessibilityofallpeakscontaining
(GMP)celltypes.UsingATAC-seqandRNAsequencing(RNA- aTFmotiftoabackgroundsetofpeaksnormalizingforknown
seq), we confirm that GMPs are substantially heterogeneous technical confounders. ChromVAR identifies high-variance TF
onbothepigenomicandtranscriptomiclevelsanddemonstrate motifsacrossCALsrepresentingknownmasterregulatorsofhe-
astrategytoenrichforsub-populationswithinGMPsatdifferent matopoiesis such as GATA1, BATF, and CEBPB (Figure 1F).
developmental stages of a myeloid differentiation trajectory. Notably,TFsofthesamefamilyoftenshareasimilarmotifand
Last, we generate scRNA-seq data and integrate these data thusaredifficulttodisambiguate,thereforeTFmotifshighlighted
withscATAC-seqtoassociateexpressionchangesoftranscrip- throughout the text are representative TF motifs that may
tion factors (TFs) to changes in chromatin accessibility at encompasstheindividualactivitiesofmultipleexpressedTFs.
cis-regulatory elements. Using these integrated data, we also Hierarchicalclusteringofsingle-cellprofilesusingTFZscores
link changes at cis-regulatory elements to changes in the generally classifies single-cells by their immunophenotypically
expression of nearby genes. These methods for assaying and defined cell type identity (Figure 2A). Interestingly, despite the
analyzingsingle-cellepigenomicsdataprovidetheopportunity overall high quality of the HSC profiles (Figures S1J–S1L),
fordenovodiscoveryofcelltypesandstates,defineregulatory HSCsexhibitlowTFZscoresforlineagespecifyingTFmotifs.
variability within immunophenotypically pure populations, and Furthermore,theHOXTFmotifwasmostenrichedinHSCs,pre-
capture the cis- and trans-regulatory dynamics across a cell- viously shown to regulate stem cell activity (Lawrence et al.,
resolvedregulatorylandscapeofdifferentiation. 1997;Magnussonetal.,2007),however,thisTFmotifalsoex-
hibitedrelativelylow-levelactivitycomparedtolineagedefining
RESULTS TFsinmore-differentiatedcells.Lowlevelexpressionoflineage
specifying TFs in other multipotent cell systems has been
Single-CellChromatinAccessibilityofDistinct described (Gru¨n et al., 2016) and is hypothesized to generally
HematopoieticCellTypes promote multipotency (Graf and Enver, 2009), which may also
We used FACS to isolate 8 distinct cellular populations explainthelowlevelTFZscoresinthisanalysisofHSCs.
from CD34+ human bone marrow, which included cell types UsingthevectorofTFZscoresasfeatures,wevisualizehe-
spanning the myeloid, erythroid, and lymphoid lineages matopoieticdifferentiationwithinthesedatausingt-SNE,which
(Figures 1A and 1B). In addition, we also profiled a clearlydisplaystheexpectedbranchingintofourdistinctdiffer-
CD34+CD38(cid:1)CD45RA+CD123(cid:1) subset that has not been well entiatedfinalstatesrepresentingerythroid,myeloid,lymphoid,
characterized (Manz et al., 2002). Cells analyzed after sorting and pDC differentiation (Figures 2B and S2A–S2D). In past
and cells cryopreserved after sorting provided comparable work,wealsousedchromatinimmunoprecipitationsequencing
dataqualityandyield(FiguresS1C–S1E),andthereforeweper- (ChIP-seq) data as annotations to explore chromatin accessi-
formedallfurtherscATAC-seqmeasurementsoncryopreserved bility differences in single-cell profiles (Buenrostro et al.,
cells(Figure1C).Together,thissortingstrategycaptures(cid:3)97% 2015b).Here,wefoundthatChIP-seqdatafromK562cells,a
ofallCD34+cells(FigureS1F)andusingpost-sortanalysis,we cell line described as an erythroid progenitor model, discrimi-
foundthatsortedcelltypeswereonaverage97%purebycell natedbetweencellsatdifferentstagesoferythroiddifferentia-
surface marker immunophenotype (Corces et al.,2016). Using tion, however, failed to capture the variance associated with
this approach, we profiled the chromatin accessibility land- myeloidandlymphoidtrajectories(FigureS2E).Therefore,due
scapes(CALs)acrossatotalof30independentsingle-cellex- to the relatively paucity of TF ChIP-seq in primary bone
periments representing 6 human donors, with each progenitor marrow-derived CD34+ cells or in early myeloid and lymphoid
populationassayedfromtwoormoredonors(FigureS1G).We cellmodels,wechosetouseTFmotifsindownstreamanalyses.
didnotprofileCD34(cid:1)bonemarrowstemcells,astheyarerare
andlesswelldescribed(Matsuokaetal.,2015). MappingSingleProfilesonHematopoieticPrincipal
Aggregatedsingle-cellchromatinaccessibilityprofilesclosely Components
resemblebulkCD34+ATAC-seqprofiles(Figures1D,S1H,and The TF Z scores can be used to cluster single-cell profiles,
S1I). Including previously published scATAC-seq data from however, this unsupervised analysis may not distinguish chro-
LMPPs and monocytes (Corces et al., 2016), this dataset matin accessibility changes associated with differentiation
comprised 3,072 single-cell CALs across 32 integrated fluidic from changes associated with other biological phenomenon
circuits(IFCs).Single-cellprofileswereofconsistenthigh-quality such as the cell cycle or niche-dependent cell-cell signaling
with 2,034 cells passing stringent quality filtering, yielding a (Crane et al., 2017). Furthermore, the use of t-SNE and TF
medianof8,268fragmentspercellwith76%ofthosefragments Zscoresforclusteringmakesrelativecell-celldistancesdifficult
Cell173,1535–1548,May31,2018 1537
A B
KLF2
CTCF GATA3 GATA1
HOXA4 MAFF
ERG
ETV4
RARA EPCAT BAEF FXB4 12PB
SPIB STAT1
IRF8 SPI1
BCL11A
RUNX2 MEIS3
ID3 TCF12
HSC LMPP GMP CLP Unknown Z-score-5 5
MPP CMP MEP pDC Mono Dim. 1
C
0
-2
-4 15
20 -6 25 30 35 -12 -10 -8 -6 -4 -2 0 2
D
tointerpret.Wereasonedareferenceguidedapproachthatuti- scores each single-cell by the contribution of each PC. Cells
lizes accessibility co-variance of regulatory elements in bulk aresubsequentlyclusteredusingthePearsoncorrelationcoeffi-
hematopoietic samples, combining previously published (Cor- cientsbetweenthesenormalizedPCsscoresandallothercells
ces et al., 2016) and additional reference profiles (see STAR (FigureS2G).Forlow-dimensionalvisualrepresentation,weper-
Methods), would provide a natural and intuitive subspace for formedPCAonthiscorrelationmatrix(Figures2Cand2D)and
dimensionality reduction of single-cell data. To achieve this, display the first 3 principal components, which represent
we implemented a computational strategy, similar to recent 93.7%ofthetotalsubspacevariance(FiguresS2H–S2M).
methods for single-cell RNA-seq analysis (Li et al., 2017), that Wevalidatedthiscomputationalapproachbydownsampling
first identifies principal components (PCs) of variation in bulk bulkprofilesto104fragmentsandfindthatthePCA-projection
ATAC-seq samples (Figure S2F) (Corces et al., 2016), then approach closely follows sample clustering using the bulk
)%24.01(
3CP
E G
GATA1 motif
%)
5 5. 4 1 ( C P
PC2 (37.8%)
F Z-score H Z-score
-8.4 7.9 -2.9 3.2
CEBPB motif HOXA9 motif
LLLLLLyymmmmmpphhhoooooiiidddd
0
-2
-4 EErryyyyytthhrrrrrooooooooooooooooooooooiiiddddddddd MMMMMMyyeelllllooiidd 15
20 -6 25 30
35 -12 -10 -8 -6 -4 -2 0 2
)%24.01(
3CP
GGAAAAAATAA1111moootif
0
-2
-4 15
20 -6 25 30 35 -12 -10 -8 -6 -4 -2 0 2
%)
5 5. 4
1
(
C P
PC2 (37.8%)
)%24.01(
3CP %)
5 5. 4 1 ( C P
PC2 (37.8%)
CCEEEEEEBPPBBBBmmmotif
0
-2
-4 15
20 -6 25 30
35 -12 -10 -8 -6 -4 -2 0 2
)%24.01(
3CP
HHOOOOOOXXXXA9999moootif
0
-2
-4 %) 15
P C 1
( 4 5. 5 -6
-12 -10 -8 -6 -4 -2 0 2 3
3
5
2 0 2 5 0
PC2 (37.8%)
)%24.01(
3CP
Z-score
-6.1 6.4
IIIIIIDD33 mmootttttiiff
0
-2
-4 15
20 -6 25 30 35 -12 -10 -8 -6 -4 -2 0 2
%)
5 5. 4
1
(
C P
PC2 (37.8%)
)%24.01(
3CP
-60 -40 -20 0 20 40 60
Z-score
-11.7 11.2
%)
5 5. 4 1 ( C P
PC2 (37.8%)
Density
0 1
2
.miD
40
30 Lymphoid
20
10
0
-10
-20
Erythroid
-30
-40 Myeloid
-50
Figure2. LineageProjectionofHumanHematopoieticProgenitors
(A)Top:hierarchicalclusteringofsingle-cellepigenomicprofiles(columns)andTFmotifaccessibilityZscores(rows).Bottom:single-cellprofilescoloredbytheir
sortedimmunophenotypeidentity.
(B)t-SNEofTFZscoresshownin(A),cellsarecoloredbytheirsortedimmunophenotypeidentify.
(CandD)Single-cellepigenomiclandscapedefinedbyPCAprojection(seeSTARMethods)coloredby(C)celltypeidentityusingimmunophenotypeand(D)
density(seeSTARMethods)overlaidwithnominaltrajectoriesexpectedfromtheliterature,asshowninFigure1A.
(E–H)PCprojectioncoloredby(E)GATA,(F)CEBPB,(G)ID3,and(H)HOXA9TFmotifaccessibilityZscores.
SeealsoFigureS2,TableS2,andDataS1andS2.
1538 Cell173,1535–1548,May31,2018
dataset(FigureS2N).Wenextdown-sampledensemblesingle- DeNovoIdentificationofUncharacterizedChromatin
cellprofilestomatchthesequencedepthsobservedinsingle- States
cellstoquantifytheexpectedmeanerrortobe1.95%,1.70%, Giventheobservedlimitationsofoursortmarkers,wesoughtto
and 3.1% per cell of the total signal for PCs 1–3, respectively definehematopoieticcelltypesdenovobyapplyingk-medoids
(Figures S2O and S2P). To test our sensitivity for identifying clustering on the first five principal components from this PC
intermediate cell states, we created synthetic mixtures from projection approach. We defined 14 unique clusters (Figures
ensembleprofiles, down-sampled to104 fragments andfound 3A and 3B; see STAR Methods) that largely overlap with
thesyntheticmixturestocloselyfollowtheexpectedpaths(Fig- previouslydefinedcellsurfacemarker-baseddefinitionsofhu-
uresS2QandS2R).Last,wefoundthisapproachtoberobustto man hematopoietic subsets (Figure 3C) and changes in the
expectedexperimentalconfoundersinsingle-celldata(Figures accessibility of TF motifs associated with hematopoiesis (Fig-
S2S–S2V).Overall,thisvisualrepresentationofthedataprovides ure 3D). This analysis identified key hematopoietic regulators
areference-guidedlandscapeofdifferentiationwithsimilarities denovo,includingmotifsassociatedwithwell-describedmaster
toWaddington’sdevelopmentallandscape(FigureS1A),further- regulators GATA1 (erythroid), CEBPD (myeloid), and EBF1
more layering TF Z scores onto this representation provides (lymphoid) lineage-specifying factors (Orkin and Zon, 2008).
insight into the ‘‘guy wires’’ that may underlie epigenomic Notably,wealsofindaspecificHSCclusterofTFsthatinclude
changesduringdifferentiation(FigureS1B). HOX,ERG,andMAFFmotifs.
Using thisclustering approach, we find that CMPs separate
TheContinuousLandscapeofHumanHematopoiesis into 4clusters denoted here asclusters 2–5,which includes a
Usingthiscomputationalapproach,wefindtheCALofhuman clusterwithmixedcontributionfromCMPandMEPcells(cluster
hematopoiesisradiatesawayfromacommonbasinofearlyhe- 5). We observe that the 4 CMP clusters within our data show
matopoieticprogenitors(Figure2C).HSC/MPP(left)andLMPP significant variability across motifs associated with GATA1,
(right)localizeatthecenteroftheprojection,followedbyCMP BCL11A, and SPI1 (PU.1), TFs implicated in myeloid/erythroid
andGMPcellsthatcomprisealargeanddiversebasin.Differen- specification(FigureS3I).Weidentify1,801differentiallyacces-
tiation into CLP (lymphoid), MEP (erythroid), and monocytes sible regions across these CMP clusters, including two previ-
(myeloid) appear as distinct differentiation trajectories that ously validated erythroid enhancers (Fulco et al., 2016)
swoop away from the central HSC basin (Figure 2D). Further- regulatingGATA1expression(FiguresS3IandS3J).Giventhese
more, motifs associated with master lineage regulators ID3, differences, we assigned CMP clusters as CMP-K3 (early
CEBPB, and GATA1 (Orkin and Zon, 2008) show continuous erythroid), CMP-K5 (late erythroid), CMP-K4 (unknown), and
gradients of activity across lymphoid, myeloid, and erythroid CMP-K2(myeloidprimed).Thesestrongchromatinaccessibility
development, while the HSC and LMPP compartment show differences further validate recent work describing functional
higheraccessibilityassociatedwiththeHOXmotif(Figures2E– and transcriptional heterogeneity within mouse (Paul et al.,
2H). We also observe examples of FACS misclassification of 2015; Perie´ et al., 2015) and human (Notta et al., 2016) CMPs
cell types, particularly between CMP:MPP, GMP:LMPP (sepa- andstronglysuggestthatCMPscanbepartitionedintomyeloid
ratedbyCD38),andGMP:CLP(separatedbyCD10),likelydue and erythroid committed progenitors. In addition, we also find
to the continuous nature of the cell surface markers (Figures thatMEP(K5–K7),GMP(K9,K10),andpDCs(K12,K13)predom-
S3A–S3D). inantly separate as two or more distinct clusters each, likely
CMP, GMP, and MEP profiles appear markedly heteroge- representingearly-andlate-stageprogenitordifferentiation.
neous in this projected space. We quantified the statistical
significance of this observed heterogeneity by comparing ChromatinAccessibilityVariabilitywithinDataDriven
the observed variability to down-sampled aggregate profiles Clusters
and found CMPs to be the most heterogeneous cell type (p < Wenextsoughttomeasurechromatinaccessibilitydifferences
10(cid:1)111), with all cell types displaying statistically significant withinstringentlydefinedHSCandLMPPprogenitors,popula-
heterogeneity(FigureS3E).Tofurtherassessthestatisticalsig- tions previously described as primed toward different lineage
nificanceofthisheterogeneity,wepermutedpeaksmatchedin fates(Buschetal.,2015;Karamitrosetal.,2018;Laurentiand
mean accessibility and GC content (see STAR Methods) and Go¨ttgens,2018;Naiketal.,2013;Peietal.,2017).Toquantify
find that variability across all cell types, with the exception of this variability, we created stringent cluster definitions that
monocytes(p=0.35),remainedstatisticallysignificant(Figures requiredcellstobebothCALcluster-pureandimmunopheno-
S3F and S3G). Finally, single-cell TF Z scores (Schep et al., typically (FACS identity) pure populations, which we call
2017),whicharecalculatedwithoutusingbulkATAC-seqdata epigenomicallyandimmunophenotypicallypure(EIPP)clusters.
asareference,alsoexhibitsignificantvariabilityforallcelltypes We then computed TF Z scores (Schep et al., 2017) for cells
(Figure S3H). Thus, rather than identifying a series of discrete within each EIPP group and found substantial heterogeneity
cellular states (Figure 1A), these results suggest that the CAL within these subsets (Figure S3K). To explore the relationship
in early hematopoietic differentiation (HSC, MPP, LMPP, and ofTF-associatedvariabilitywithinHSCstodirectionsofdifferen-
CMP) comprise a fairly broad basin of allowable states, while tiation,wecategorizedindividualEIPPHSCsbytheirTFZscores
pathsoflaterdifferentiationbecomemorecanalizedintodistinct (highorlow),computedthedistancebetweenhigh/lowcentroids
andcontinuousdifferentiationtrajectories(seeDataS1;single- in the PC space, and calculated statistical significance by
cell CALs can be further explored using our web resource: comparing high/low distances to permuted HSC EIPP profiles
http://schemer.buenrostrolab.com/). (Figures 3E and S3L–S3N). Using this analysis approach, we
Cell173,1535–1548,May31,2018 1539
A B C Freq.
0 1
CCCCCCCLLLPPP 14 HSC
pppDDDCC 13
12
11 K14 MPP
HSCC 10
MMEPP 9 K13 CMP
8
0 6 7 K7 K1 MEP
-2 4 5 K6 K2 K8 K12 LMPP
2 3 K5 GMP
-4 1 K3 K9
CMP 2 1 0 5 K4 K10 Mono -6 3 2 0 5 K11 pDC -12 -10 -8 -6 -4 -2 0 2 35 CLP
1 2 3 4 5 6 7 8 9 10 11 12 13 14
TF Z-score Clusters
D 0 Max E F
PAX5 EBF1
RUNX2
TCF12 LYL1 TCF4 MEIS3
TBX15
IRF1
PRDM1
STAT1
MEF2A BCL11A
KLF4
KLF14
ESRRA
RARA
RELA G H STAT3
MAFF
2 GATA2 motif 2 MESP1 motif
BACH2
ATF4
CEBPD
JUND 0 0
SPI1
ATF3
ERG -2 -2
HOXA9
CTCF
H AL O X X 4 A4 -4 -4
GATA1
FOXO4 -6 v d a ir r e ia c b tio ili n ty p = - 1 v . a 4 l 3 ue=10-17Low High -6 v d a ir r e ia c b tio ili n ty p = - 1 v . a 3 l 6 ue=10-8 Low High
FOXP3
1 2 3 4 5 6 7 8 9 10 11 12 13 14 -12 -8 -4 0 4 -12 -8 -4 0 4
Clusters
findCTCF,nuclearfactorkB(NF-kB)(representedbytheRELA thisTFbiasisconsistentwithpreviousstudiesthatlineagetrace
motif), and ETS motifs to be significantly variable in HSCs, HSCsthatsuggestthatHSCsexhibitoligo-lineagebiastoward
however,uncorrelatedwithanyspecificdirectionofdifferentia- erythroid-myeloidorlymphoidcellfates(Peietal.,2017).
tion (Figure 3F). Interestingly, NF-kB signaling (inflammatory We next turned to LMPPs, a subset previously shown to
signaling)hasbeenimplicatedinmouseHSCstem-cellmainte- demonstrate lineage priming toward dendritic (pDC), myeloid
nance (Zhao et al., 2012) and HSC emergence mediated by (GMP:monocytes), and lymphoid (CLP:B cell) fates in mice
neutrophil secretion of tumor necrosis factor alpha (TNF-a) (Buschetal.,2015;Naiketal.,2013)andinhuman(Karamitros
(Espı´n-Palazo´n et al., 2014; Sawamiphak et al., 2014). In etal.,2018).Interestingly,wefoundmotifsassociatedwiththe
contrast,wefindtheGATA(p=10(cid:1)17)andMESP/ID(p=10(cid:1)8) TFs TCF4, STAT1, and CEBPE to be significantly correlated
motifs(representedbyGATA2andMESP1motifs)TFZscores with directionality toward CLP, pDC, and GMP differentiation,
to be significantly correlated to erythroid and lymphoid trajec- respectively(FiguresS3O–S3R),notablytheTCF4motifissimilar
tories respectively (Figures3G,3H,andS3N). Thedirection of to the TCF3, ID3, and MESP1 motifs. TCF4 and CEBPE motif
)%24.01(
3CP
K1111144
0 KKKK7 KKKK
K KKKK -2 KKKKKKKKK2222222222222222222
-4 KKKKK9999999999999
4 5. 5 %) -6 K KKK 000000000000 K111111 2 2 5 1 0 5 P C 1 ( -12 -10 -8 -6 -4 -2 0 2 3 3 5 0
PC2 (37.8%)
)%24.01(
3CP %) 5 GMP 4 5. 1 ( C P
PC2 (37.8%)
0 5 10 15 20 25
Direction score, -log10 p-value
Z-score Z-score -2.7 2.7
-3.1 2.6
erocs-z
FT ,ytilibairaV
2.2 GATA motif 2 RELA motif
CTCF ID motif
CTCF motif
1.8 RE C LA TCFL N ET K S F B m m ot o if tif 0
NFKB1 FLI1 GATA2 -2 1.4 ETV4 ID ID 3 4 M M E E S S P P 2 1 GATA3 G G A A T T A A 1 5 -4
1
-6
0.6
-12 -8 -4 0 4
PC2
3CP
Z-score
-3.8 3.4
variability=1.80
direction p-value=0.28Low High
Figure3. MolecularCharacterizationofData-DefinedClusters
(A)Single-cellepigenomiclandscapedefinedbyPCAprojection,coloredbydata-drivenclusternumber.
(B)Medoidsofdata-drivencentroidsdepictedonthePCAsub-space.
(C)Confusionmatrixofdata-drivenclustersrepresentingthepercentfrequencyofimmunophenotypicallydefinedcelltypes.
(D)TFmotifaccessibilityZscoresaveragedacrossdatadefinedclustersandhierarchicallyclustered.ScoresarenormalizedbythemaxvalueofeachTFmotif.
(E)TFmotifvariabilityanddirection–log10pvalueforeachTFmotiffortheHSCEIPPcluster,TFssharingasimilarmotifarehighlighted.
(F–H)TFmotifaccessibilityZscoresofHSCprofilesfor(F)RELA,(G)GATA2,and(H)MESP1motifs,arrowsdenotethedirectionofthesignalbiasandarecolored
bythetargetcelltype.
SeealsoFigureS3.
1540 Cell173,1535–1548,May31,2018
A B G
C D H
E F
Figure4. IdentifyingContinuousDifferentiationTrajectories
(A–D)PC2byPC3projectionofsingle-cellshighlightingcellsprogressingthroughtheinferred(A)erythroid,(B)lymphoid,(C)pDC,and(D)myeloiddevelopmental
trajectory(blackline),cellsusedforinferencearecoloredbysortedidentity,allothercellsareshowningray.
(E)SortingschemafordifferentGMPprogenitorsdefinedbyCD123expression,markedbyCD123low(GMP-A,light-gray),CD123medium(GMP-B,gray),and
CD123high(GMP-C,dark-gray).
(F)BulkRNA-seqlog2-fold-changeand-(logpvalue)forexpressedgenescomparingGMP-CandGMP-A.
(G)Single-cellsusedforthemyeloidtrajectorycoloredby(left)theirclusteridentity(clustercolorsasinFigure3)or(right)theirdensityalongthetrajectory.
(H)Densityofmyeloidprogressionscoresforimmunophenotypicallydefinedcelltypes,includingtheGMPsubsets.
SeealsoFigureS4.
accessibility were anti-correlated with each other, and each Toachievethis,wefirstdeterminedtheshortestpathbetween
defined a unique direction toward CLP (lymphoid) or GMP clustercentroids andassignedcellsto theclosest pointalong
(myeloid) differentiation, respectively, suggesting antagonism thatpath;asimilarapproachhasbeendescribedforanalyzing
between myeloid/lymphoid differentiation programs. Sepa- scRNA-seq data (Shin et al., 2015). This approach aligned
rately, the STAT1 motif accessibility appeared to be directed cells to well-defined lineage pathways (Orkin and Zon, 2008)
toward CLP (lymphoid) and pDC (dendritic) cell fates. Overall, producing an ordering of single cells along continuous
this reference-guided computational approach provides a erythroid (K1,K3,K5,K6,K7), lymphoid (K1,K2,K8,K14), pDC
statistical framework for assigning TF motif-associated vari- (K1,K2,K8,K12,K13),andmyeloid(K1,K2,K9,K10,K11)differenti-
abilitytolineage-associatedCALvariationprovidingaresource ation trajectories (Figures 4A–4D and S4A–S4D). These
foridentifyingmolecularfactorsthatmaybeinvolvedinlineage trajectoriesallowforinterpretationofCALheterogeneitywithin
primingacrossmultipotentcellpopulations. progenitors and provide methods to further parse cellular sub
statesacrossdifferentiation.
HeterogeneousCellTypesCanBeFurtherDividedalong We examined variability within two clusters (K9 and K10) of
DevelopmentalTrajectories GMPs,whichshowsignificantdifferencesinaccessibilityamong
We next sought to order cells along continuous differentiation myeloid-defining factors SPI1 (PU.1) and CEBP-associated
trajectories across branches of hematopoietic development. motifsacrossthemyeloiddevelopmentaltrajectory(FigureS4E).
Cell173,1535–1548,May31,2018 1541
Tofurtherpartitionthispopulation,wesoughttoidentifycellsur- MatchingTranscriptomeswithChromatinAccessibility
facemarkersthatmaydifferentiallyenrichforK9andK10GMPs. Wenextaimedtodevelopameanstopairsingle-cellepigenomic
We hypothesized that CD123 expression may correlate with andtranscriptomicmeasurements,withthegoaloflinkingchro-
earlyandlateGMPdifferentiationfortworeasons:(1)theUNK matin accessibility changes associated with DNA sequence
population, which is CD123(cid:1)/lo, is enriched in the GMP K9 motifstoexpressedTFs,aswellaslinkingaccessibilitychanges
cluster, and (2)CD123, alsoknown asIL3RA,isa high-affinity atputativeenhancerstoexpressionchangesattargetgenes.We
receptor for the myeloid promoting cytokine IL3. We therefore first performed single-cell RNA-seq (10X genomics platform)
performed scATAC-seq, bulk ATAC-seq (Buenrostro et al., acrossHSC,CMP,andGMPs,collectingatotalof7,818cells
2013, 2015a), and bulk RNA-seq on cells from three distinct passingfilter(2,268,4,454,and1,096,respectively;Figure5D).
bins of CD123 expression (Figure 4E). Bulk ATAC-seq and In addition, we included publically available scRNA-seq data
RNA-seqdatarevealedsubstantialchromatinaccessibilityand from CD34+ and CD14+ monocyte cells (Zheng et al., 2017),
transcriptomic differences across the GMP-A and GMP-C altogether analyzing transcriptional dynamics of 14,432 cells
populations(Figures4FandS4F–S4H).Thelistofdifferentially acrossmyeloiddifferentiation.Usingthesedata,wedeveloped
expressedgenesincludedimportantdevelopmentalregulators, areference-guidedapproachtopairscATAC-seqandscRNA-
including downregulation of HSPC TFs GATA2 and TAL1 and seqprofiles(seeDataS2).Todothis,wefirstfitalinearmodel
upregulation of myeloid genes SPIB, IRF8, TLR7, and MPEG1 to match the measured bulk ATAC-seq PCs, which measure
intheGMP-Ccellpopulation(Figure4F).Inaddition,projection global variation in chromatin accessibility, to changes in gene
of the scATAC-seq data from the three cell fractions revealed expressionasmeasuredbybulkRNA-seqacrosssortedpopu-
that this strategy provides strong separation of early (GMP-A) lations (Figures S5D–S5F). We then used this map between
andlate(GMP-C)stagesofmyeloiddifferentiation(Figures4G, ATAC-seq PCs and gene expression to assign ‘‘inferred tran-
4H, and S4I–S4K). Altogether, we validate the heterogeneity scriptomes’’toeachcellinthescATAC-seqdataset(FigureS5G).
within GMPs and more generally demonstrate a data driven Finally,topaireachscRNA-seqprofiletoascATAC-seqcell,we
approach for defining cell populations from single-cell epige- assigned scRNA-seq profiles to the most correlated scATAC-
nomicdata. seq‘‘inferredtranscriptome’’(FigureS5H).Usingthisapproach,
we found that the sorted identity of scRNA-seq profiles were
MotifAccessibilityDynamicsalongMyeloidCell enriched for the corresponding matched sorted identity for
Differentiation scATAC-seq profiles (Figure S5I). Furthermore, by pairing
Themyeloidtrajectorydescribedabovetransitstwoheteroge- single-cell RNA-seq to scATAC-seq cells, we found scRNA-
neous cell populations (CMP and GMP), as such, regulatory seq profiles of FACS-sorted CMPs associated with the four
analysisofmyeloiddifferentiationhasbeenpreviouslyobscured scATAC-seq-defined CMP clusters discussed above (Fig-
inbulkstudiesduetothelimitationsoftheimmunophenotypic ureS5J).Furthervalidatingtherecentreportsofheterogeneity
markers of these populations. We therefore sought to charac- inmouse(Pauletal.,2015;Perie´ etal.,2015)andhuman(Notta
terize TF dynamics across myeloid development by mapping etal.,2016)CMPs,wefoundexpressionheterogeneityofknown
TFZscorestocellsalongthecontinuousmyeloiddifferentiation hematopoietic regulators in CMPs, which included the TFs
trajectory (Figures S4L–S4N). Using this approach, we find HOXA5,GATA1,andCEBPB(FiguresS5KandS5L).
6 clusters (see STAR Methods) of TF Z score profiles during Our approach provides a computational method to fit gene
myeloid development (Figures 5Aand S5A–S5C). Accessibility expressionchangesacrossbulkATAC-seqandRNA-seq‘‘an-
atTFmotifsassociatedwithregulatorsHOXB8andGATA1(clus- chor points’’ generated from well-defined sorted populations,
ter1)ishigh inHSCs anddecreases through differentiation to providingareferenceforanalysisofsingle-cellgeneexpression
CMPs. Interestingly, loss of GATA motif accessibility (repre- andchromatinchangesspanningtheseanchorpointstoresolve
sentedbytheGATA1motif)beginswithintheHSCcompartment, continuousregulatorychangesincelldifferentiation.Thisrefer-
whileHOXmotifaccessibility(representedbytheHOXB8motif) ence-guidedstrategyresultedinatotalof9,312scRNA-seqcells
islostatthetransitionofHSCtoCMPdifferentiation,suggesting positionedacrossmyeloidpseudo-timewithhighconcordance
that loss of GATA motif accessibility may be an early event in intheenrichmentofimmunophenotypicallydefinedcellsacross
lineagecommitmentwithinHSCs(Figure5B).Wealsoobserve thetrajectories(Figure5E).Usingthisunifiedlineageorder,we
two distinct modes of activation for myeloid-associated TF mappedexpressiondynamicsacrossmyeloidcelldifferentiation
motifs; cluster 4 TFs (CEBPD- and SPIB-associated motifs) andfoundexpectedpatternsacrossknownregulatorsofmyelo-
display early and gradual gain in activity beginning within poesis (Figures 5F and 5G). To further validate this pairing
CMPs,whilecluster5TFs(STAT1-,IRF8-,andBCL11A-associ- approach, we compared the ATAC:RNA paired lineage order
ated motifs) increase sharply in activity across the GMP-A to with ordering scRNA-seq cells using diffusion pseudotime
GMP-C transition, implicating the CEBP family of TFs (repre- (DPT)(Haghverdietal.,2016).Inthiscomparison,wefindthat
sentedbytheCEBPDmotif)asaninitiatingfactorformyeloid- thetwoapproachesforcellorderingareoverallhighlycorrelated
erythroid specification (Figure 5C). In addition to the activity (R = 0.86; Figure S5M). However, we find that unsupervised
patterns associated with canonical myeloid-defining factors, orderingofHSCsusingDPTwasmorecorrelatedtothenumber
we also identify a pulse of activity within CMPs from cluster of genes detected than the ATAC:RNA pairing approach
2 TFs (TCF3/12 associated TF motifs upregulated in CLP/ described above (R = 0.68 versus R = 0.14), suggesting
pDC),whichmayreflecttransientactivationofalymphoidpro- computational ordering of scRNA-seq data with DPT may be
gramwithinpre-committedmyeloid-biasedCMPs(FigureS5C). moresensitivetodropout(FiguresS5NandS5O).Thismaybe
1542 Cell173,1535–1548,May31,2018
A
HOXA9 GATA1
HOXB8
CEBPD, K4
BCL11A, K5
expectedasDPTdoesnotexplicitlymodelcell-celldifferences LinkingTFExpressionwithAssociatedAccessibility
in dropout (zero counts for genes) and further suggests that VariationinBindingMotif
computational tools for joint analysis of scATAC-seq and InefforttodisambiguateTFsthatbindthesameorsimilarmotif
scRNA-seq may be more robust to technical confounders. and thus assign expression of TFs to downstream changes
Mostimportantly,thegeneexpressiontrajectories(FigureS5P) in chromatin accessibility at TF motifs, we correlated the
arelargelysimilarbetweenthetwoapproaches,supportingour expression of TFs with the TF motif Z scores across myeloid
ATAC:RNApairingapproach. pseudo-time. We then filtered for motif accessibility-TF
1=k
2=k
3=k
4=k
5=k
6=k
sfitom
63
sfitom
25
sfitom
52
sfitom 53
sfitom
02
sfitom
73
B HSC CMP GMP Mono C HSC CMP GMP Mono
HSC CMP GMP Mono
CTCF
TCF3 TCF12
BPTF -2 0 2 4 6 8 10 12
Myeloid pseudo-time FOXJ3
CEBPG SPIB DBP CEBPA
STAT1
IRF8 BCL11A
IRF4
ESRRA RORB
KLF2
-2 0 2 4 6 8 10 12 14
Myeloid pseudo-time
erocS
noitaiveD
1
0.8
0.6
0.4
0.2
0
-2 0 2 4 6 8 10 12
Myeloid pseudo-time
erocS
noitaiveD
TF Z-score
0 Max 1
0.8
0.6
0.4
HOXB8, K1 0.2
GATA1, K1
95% CI 0 95% CI
E
HSC CMP
GMP
mono
HSC
CMP
GMP
mono
-1 0 1 2 3 4 5 6 7 8 9 101112
H
RNA expression of TF Motif accessibility of TF Pearson
HOXB7
HOXB6
NFIB
GATA3
MECOM
GATA2
SPI1
CEBPD
SPIB
IRF8
IRF2
-2 0 2 4 6 8 10 12 -2 0 2 4 6 8 10 12
Myeloid pseudo-time Myeloid pseudo-time
CATAcs
ANRcs
Myeloid pseudo-time F 5
0
-2 0 2 4 6 8 10 12
noisserpxe
2gol
CEBPD expression
2
1
0
5
0
-2 0 2 4 6 8 10 12
Myeloid pseudo-time
noisserpxe
2gol
D
-40 -30 -20 -10 0 10 20 30 40 50
Dim. 1
G
GATA2 expression
1
0
2 .miD
Rel. Density
10x scRNA-seq 0 1 60 HSC GMP 50 CMP Mono
40
30
20
10
0
-10
1
0.5
Pearson
Figure5. TranscriptionFactorDynamicsacrossMyeloidDifferentiation
(A)K-medoidsclusteringofTFmotifaccessibility(left)andPWMlogos(right)fordynamicTFmotifprofilesacrossmyeloiddevelopment.
(BandC)SmoothedprofilesofTFmotifaccessibilityZscoresinmyeloidprogressionfor(B)HSCactiveTFsGATA1(blue)andHOXB8(green),and(C)monocyte
activeregulatorsCEBPD(yellow)andBCL11A(red).Errorbars(gray)denote95%confidenceintervals.
(D)t-SNEofscRNA-seqdatashowingHSC,CMP,GMP,andmonocytecells.
(E)Densityofmyeloidpseudo-timescoresfor(top)scATAC-seqand(bottom)computationallymatchedscRNA-seqprofiles(seeSTARMethods).
(FandG)Log2meanexpressionprofilesforTFs(F)CEBPDand(G)GATA2acrossmyeloidpseudo-time,(top)individualcellsarecoloredbytheirsortedidentity,
CD34+cellsareshowninblackand(bottom)smoothedprofilesareshowninred.
(H)Left:expressionand(right)TFmotifaccessibilitydynamicsacrossmyeloidpseudo-timeforcorrelated(R>0.5)gene-motifpairs.
SeealsoFigureS5.
Cell173,1535–1548,May31,2018 1543
expressioncorrelationsofR>0.5,thisapproachyielded11TFs (Figure6D).Moregenerally,wecalculatedthecorrelationofreg-
thatdefineddifferentstagesofmyeloiddevelopment(Figure5H), ulatoryelements to dynamicgeneswithin 10Mbof annotated
including loss in the expression of HOX factors (HOXB7 and transcription start sites (‘‘peak-gene pairs’’) and found that
HOXB8) (Argiropoulos and Humphries, 2007) and activation of proximalregulatoryelements(<100kb)weresignificantlymore
well-known master regulators of myeloid cell development correlated to the expression of nearby genes than distant ele-
includingSPI1(PU.1)andIRF8(Satpathyetal.,2012).Resolution ments (>100 kb) (Figure 6E). Further validating this approach,
of the developmental order of these activated TFs across we also found that the correlation of regulatory elements to
myeloid differentiation has been previously obscured in bulk targetgenesimprovedasafunctionofloop confidence within
studies, in part, due to the cellular heterogeneity within CMPs promoter capture HiC (PCHiC) data (Figure 6F), here defined
andGMPs.Interestingly,wealsoobservedastrongcorrelation byPCHiCloopsfrombothCD34+(Mifsudetal.,2015)andmono-
betweenGATA3expressionandGATAmotifaccessibility,dele- cyte(Javierreetal.,2016)cells.Importantly,wefindloopinterac-
tionofGATA3hasbeenshowntopromoteself-renewalinHSCs tions at this resolution do not necessarily define correlated
(Frelin et al., 2013), together leading to the hypothesis that peak-gene pairs. In our analysis, only 45% of dynamic en-
GATA3 may be associated with HSC lineage priming. Here, hancers within high confidence loops are called as correlated
single-cell chromatin accessibility, paired with single-cell tran- totheexpressionofPCHiCdefinedtargetgenes(FigureS6G).
scriptomics,resolvesthetemporaldynamicsofmasterregulator ThisobservationmaybeduetothefactthatPCHiCloopslink
expression and associated chromatin changes in myeloid cell relatively large genomic regions, often encompassing multiple
development,providingaresourceforfurtherfunctionalstudies regulatoryelements,which mayindependently regulatedown-
and for the analysis of regulatory changes associated with streamgenes.
differentiation. Wenextsoughttotestwhetherpreviouslydefinedcis-linked
expression quantitative trait loci (cis-eQTLs) overlapped
RegulatoryElementandGeneActivationacross enhancer-geneinteractionsidentifiedusingtheseintegratedsin-
Myelopoiesis gle-cell data. We reasoned that correlated peak-gene pairs
We next sought to characterize locus-specific cis-regulatory couldbeusedtofunctionallyconnectrelevantgeneticvariation
dynamicsduringmyeloiddifferentiation.Wefirstfilteredforreg- at regulatory elements to consequences in gene expression
ulatoryelementswithhighfragmentcountsandwithsignificant importantinnormalmonocytefunction.Wethereforecollected
variabilityacrosstheorderedcellsidentifying14,005cis-regula- previously published cis-eQTLs, derived from interferon-g and
toryelementsforanalysis(seeSTARMethods).Theseregulatory lipopolysaccharide stimulation of monocytes (Fairfax et al.,
elements exhibited highly heterogeneous patterns of accessi- 2014),andfilteredforSNPswithindevelopmentallydynamicreg-
bilitychanges(Figures6A–6CandS6A–S6C)—suggestingthat ulatory elements linked to dynamic genes (n = 370 peak-gene
alimitednumberofTFmotifaccessibilitypatterns(k=6)could pairs). To directly compare enrichment of either correlated
induce a surprising level of variation of chromatin accessibility peak-gene pairs or PCHiC loops at cis-eQTL defined peak-
atindividualregulatoryelements.Forexample,withintheregula- gene interactions, we determined significant enrichment of
tory elements surrounding the myeloid regulator CEBPD eachdatasetbynormalizingtoabackgroundsetofpeak-genes
(numbered for simplicity, see Figure 6B), the distal element matched for distance (Figure S6H). We found that cis-eQTLs
CEBPD-1 was ‘‘fast-to-activate’’ and showed stepwise gains were strongly enriched for scATAC/scRNA-seq correlated
ofactivitywhilethedistalelementCEBPD-2was‘‘slow-to-acti- peak-genepairs(p=4.9310(cid:1)5)andobservedonlyamodest
vate’’andshowedamorediscretepulseofactivity(Figure6B). enrichmentPCHiCloopinteractions(p=0.19)(Figures6Gand
To visualize the complete repertoire of dynamic regulatory S6I). Thus, statistical linkage between single-cell chromatin
profiles, we ordered elements based on their accessibility accessibility and gene expression can serve as a means to
changesoverthistrajectory(Figures6CandS6).Thisanalysis functionallylinkenhancerstotargetgenepromoters.
revealsmultiplebroadclassesofregulatoryelementbehaviors,
rangingfromfast-toslow-to-repressHSCregulatoryelements DISCUSSION
andfast-toslow-to-activatemonocyteregulatoryelements(Fig-
ure6C).Wealsoobserveacollectionof‘‘transition’’cis-regula- Weusedsingle-cellchromatinaccessibilityandtranscriptomic
tory elements that exhibit peak accessibility at intermediate analysis to identify regulatory heterogeneity and continuous
stages of myeloid development, as well as ‘‘reactivation’’ ele- differentiation trajectories in early human hematopoiesis by
mentsthatareinitiallylostandsubsequentlyreactivatedinlater developing a broadly applicable computational framework for
stages of myeloid differentiation (Figures S6D and S6E).Thus, analysis of these single-cell data. This framework includes a
fromasmallnumberofdiscreteclustersofTFmotifaccessibility, means for visualizing single-cell chromatin accessibility, and
highlydiversecis-regulatoryprofileslikelyarisefromthecombi- computationally pairing these data with single-cell RNA-seq,
natorialcontroloftrans-factorbindingtotheirtargetregulatory byusingbulkdataasareference.Withthisapproach,wefind
elements(FigureS6F). that immunophenotypically defined cell populations often flow
Wereasonedthatcorrelationbetweendynamicallyactivated from one state to another and further we dissociate TF motif
patterns of distal regulatory elements with nearby expressed activityvariabilitywithinthesepopulationsascorrelatedorun-
genes may be used to connect enhancers to target genes correlated to axis of differentiation. In this effort, we find the
(Figure6C).Indeed,wefounddynamicregulatoryelementssur- activityofTFmotifs,suchastheGATAmotifinHSCs,mayrepre-
roundingCEBPDwerehighlycorrelatedwithCEBPDexpression sentindicatorsof lineagepriming pulling cellstoward different
1544 Cell173,1535–1548,May31,2018
A B
-2 0 2 4 6 8 10 12 14
Myeloid pseudo-time
developmentallycommittedstates.Whilethisreference-guided already or soon-to-be collected (Regev et al., 2017). As such,
approachenabledustopairscATAC-seqandscRNA-seqdata thedatageneratedhereandassociatedcomputationalmethods
alongacommonlineagetrajectory,thisapproachmaybegener- maybebroadlyadaptedtofurtherdevelopcomputationaltools
alized to pair cells along more-diverse cell fate transitions. topairdifferentsingle-celldatatypes.
Notably,methodsforcomputationallypairingmulti‘‘-omic’’pro- Furthermore, single-cell CALs can be aggregated to define
fileshaveadvantagesoverexperimentallycoupledapproaches, unique cis-regulatory elements active at different stages of
for example, a computational approach may provide (1) more differentiation.Theintersectionofgeneticvariantswiththesereg-
flexible experimental workflows, (2) allow pairing data across ulatoryelementsmayprovidenewinsightsintocelltypesorstages
experimental methods that may not be easily combined, and of differentiation relevant to disease (Corces et al., 2016; Guo
(3) the reanalysis of the large repertoire of scRNA-seq data etal.,2017).Currentexperimentalmethodsthataimtoassociate
llec rep
stnemgarF
3
2
-2 0 2 4 6 8 10 12 14
Myeloid pseudo-time
llec rep
stnemgarF
CEBPD:promoter CEBPD-2:distal
0.6 CEBPD-1:distal CEBPD-3:intronic
1 0.5
0 0.5 0.4 CEBPD-1:distal
0.4 95% CI 0.3
0.3
0.2
0.2
0.1 0.1
0
0
high con m f. e l d o . o c p o s nf lo . w lo o c A p o l s l n p f. e l a o k o - p g s ene pairs
nosraeP
naeM
CEBPD expression
D
0.3
0.2
0.1
0 <1kb 1-10k 1 b 0-100 1 k 0 b 0kb-1Mb 1-10Mb
nosraeP
naeM
C
0 Max
E G
0.5
0.4
0.3
0.2
0.1
0 -2 0 2 4 6 8 10 12 14 Myeloid pseudo-time
stnemele
yrotaluger
elbairav
500,41
seneg
elbairav
389,1
Correlate dynamics
REs to nearby genes (+/-10Mb)
scATAC/RNAcapture correlation HiC
ta
tnemhcirne
noitcaretnI
)lav-p
01gol-(
sLTQe-sic
0 Max
Chromosome 8
S c c h a r8 le : 48,500,000 1 Mb 49,000,000 49,500,000 hg1950,000,000
K1-HSC
K2-CMP
K9-GMP
K10-GMP
K11-Mono
CD34+_HSPCs
CE P B R PD KDC MCM4 EFCAB1 SNAI2 C8 B o C rf 0 2 4 2 2029
KIAA0146 UBE2V2
F
4
3
2
1
0
Expression
per
cell
(L0g2)
scATAC-seq scRNA-seq Peak activity
HSC mono
HSC CMP GMP Mono
2 Early to repress
1
Late to
repress
0
Transition
peaks
Early to
activate
Late to
activate
Early to
1 repress
0.5 Late to
<0.5 repress
Transition
expression
Early to
activate
Late to
activate
nosraeP
Figure6. RegulatoryElementDynamicsLinksDistalElementstoGenes
(A)FragmentspercellforaCEBPDdistalelementorderedbymyeloidpseudo-time,(top)cellsarecoloredbytheirsortedidentityand(bottom)valuesare
smoothed(blue).Errorbars(gray)denotes95%confidenceintervals.
(B)cis-RegulatoryandexpressiondynamicsacrossfourregulatoryelementsnearthemyeloidregulatorCEBPD.
(C)Accessibility(top)andexpression(bottom)dynamicsacrossmyeloidpseudo-time,rowsaresortedbytheirpeakintensityinthemyeloidtrajectory.
(D)RegulatoryprofilessurroundingtheCEBPDgene,dynamicenhancersarehighlightedingraywithsignificant(blue)andnon-significant(gray)correlatedpeak-
genepairsshownasloops.
(EandF)MeanPearsoncorrelationcoefficientsbinnedby(E)genomicdistancetothegeneand(F)loopconfidence.Errorbarsrepresent1SDontheestimateof
themean.
(G)pvalueofenrichedpeak-genecorrelationorpromotercaptureHiCatcis-eQTLsoverlappingdynamicenhancers.
SeealsoFigureS6.
Cell173,1535–1548,May31,2018 1545
non-coding genetic variation to changes in gene expression B BulkandsinglecellRNA-Seqanalysis
generally measure either physical interactions using chromatin B MatchingscRNA-seqtoscATAC-seq
conformationcaptureapproaches(Javierreetal.,2016)ordirect B IntegrationofpromotercaptureHi-Cdata
geneticperturbation(Fulcoetal.,2016).Here,weshowthatcorre- B Monocytecis-eQTLdata
lationofnaturallyoccurringregulatoryheterogeneityacrosssin- d DATAANDSOFTWAREAVAILABILITY
gle-cellscanbeusedtopairregulatoryelementstotargetgenes. d ADDITIONALRESOURCES
Thissingle-cellinferenceapproachforlinkingregulatoryelements
togenesmaybeparticularlyusefulforinferringenhancer-gene SUPPLEMENTALINFORMATION
interactions in rare cells or across cells states where FACS
markers are not well defined. We expect future studies will SupplementalInformationincludessixfigures,twotables,andtwodatafiles
combineanintegratedsingle-cellinferenceapproachwithphys- and can be found with this article online at https://doi.org/10.1016/j.cell.
2018.03.074.
icalinteractionorgeneticperturbationmapsforimprovedlinking
of enhancers to target genes, providing a single-cell resolved
ACKNOWLEDGMENTS
interactionlandscapeofnon-codinggeneticvariation.
Overall this work has defined one representation of the
WethankmembersofGreenleaf,Chang,Majeti,andBuenrostrolabsforvalu-
epigenomic states underlying hematopoiesis, reminiscent of able discussions. We acknowledge the C. Bustamante lab for help with
Waddington’s landscapeof differentiation. However,given the sequencing. This work was supported by NIH (P50HG007735 and
staticsnapshotoftheCALprofileswehavequantifieditremains UM1HG009442 to H.Y.C. and W.J.G.and U19AI057266 to W.J.G.), Stine-
uncertaintowhatdegreedensityofthislandscapemightallow hart-Reed Foundation (to R.M. and H.Y.C.), the Rita Allen Foundation (to
W.J.G.),theBaxterFoundationFacultyScholarGrant,andtheHumanFron-
inference of cell state transition kinetics and potential. Joint
tiersScienceProgramgrantRGY006S(toW.J.G).W.J.GisaChanZuckerberg
measureswiththeemergingrepertoireofCRISPR-basedtools
Biohubinvestigatorandacknowledgesgrants2017-174468and2018-182817
forlineagetracing(Woodworthetal.,2017)willbeessentialfor fromtheChanZuckerbergInitiative.J.D.B.acknowledgessupportfromthe
quantifying the epigenomic contribution of lineage priming on HarvardSocietyofFellowsandBroadInstituteFellowship.J.D.B.alsoac-
cellfatedecisionsovertime.Italsoremainstobeseentowhat knowledgestheAllenDistinguishedInvestigatorProgram,throughThePaul
extent lineage priming is reflected in transcriptional diversity G.AllenFronteirsGroup,forfunding.R.M.isaLeukemiaandLymphomaSo-
cietyScholar.M.R.CisaFellowofTheLeukemia&LymphomaSociety.
withinHSCsandwhetherthelineage-associatedCALvariability
we observe within HSCs is tightly coupled with transcriptional
AUTHORCONTRIBUTIONS
changes (Yu et al., 2016). We expect future work to couple
single-cell epigenomic, transcriptomic, proteomic, and lineage
J.D.B.,M.R.C.,H.Y.C.,andW.J.G.conceivedtheproject.M.R.C.andR.M.
measures may reveal important insights into the molecular performedcell sorting.J.D.B.performedATAC-seq andscATAC-seq data
detailsandtemporalorderofinitiatingregulatoryfactorsgovern- analysisandoversawscATAC-seqlibrarygenerationandprotocoloptimiza-
ingmultipotentcellfatetransitions.Altogether,weexpectfurther tionperformedbyB.W.B.W.generatedthescATAC,bulkATAC-seq,bulk
improvements in experimentally or computationally integrating RNA-seq,andscRNA-seqdata.C.A.L.performedtheRNA-seqandPCHi-C
dataanalysiswithhelpfromM.J.A..A.N.S.developedtheTFmotifanalysis
multiplesingle-celldatatypeswillunraveladynamicregulatory
tools.C.A.L.developedtheassociatedwebresourcewithhelpfromM.J.A.
landscapeprovidingasingle-cellresolvedsystemsperspective
J.D.B.andW.J.G.wrotethemanuscriptwithinputfromallauthors.
fordevelopmentalordiseasecellfatedecisions.
DECLARATIONOFINTERESTS
STAR+METHODS
StanfordUniversityhasfiledaprovisionalpatentonATAC-seq;J.D.B.,H.Y.C.,
andW.J.G.arenamedasinventors.H.Y.C.andW.J.G.arescientificco-foun-
Detailedmethodsareprovidedintheonlineversionofthispaper
dersofEpinomics.
andincludethefollowing:
Received:August14,2017
d KEYRESOURCESTABLE
Revised:January3,2018
d CONTACTFORREAGENTANDRESOURCESHARING
Accepted:March27,2018
d EXPERIMENTALMODELANDSUBJECTDETAILS Published:April26,2018
B Cellcollectionandisolation
d METHODDETAILS REFERENCES
B Single-cellATAC-seqandsingle-cellRNA-seq
B Single-cellRNA-seq Argiropoulos,B.,andHumphries,R.K.(2007).Hoxgenesinhematopoiesis
andleukemogenesis.Oncogene26,6766–6776.
B BulkATAC-seqandRNA-seq
d QUANTIFICATIONANDSTATISTICALANALYSIS Becker,A.J.,McCulloch,E.A.,andTill,J.E.(1963).Cytologicaldemonstration
of the clonal nature of spleen colonies derived from transplanted mouse
B Datapre-processingandTFscores
marrowcells.Nature197,452–454.
B PCAprojection
Brennecke,P.,Anders,S.,Kim,J.K.,Ko1odziejczyk,A.A.,Zhang,X.,Proser-
B Clustering,K-medoidsandcomputingdensity
pio,V.,Baying,B.,Benes,V.,Teichmann,S.A.,Marioni,J.C.,etal.(2013).
B Lineagebiasanalysis
Accounting for technical noise in single-cell RNA-seq experiments. Nat.
B SignificantlydifferentialCMPpeaks Methods10,1093–1095.
B Orderingcellsforpseudo-timeandsmoothing Buenrostro,J.D.,Giresi,P.G.,Zaba,L.C.,Chang,H.Y.,andGreenleaf,W.J.
B Filteringandregulatoryelementanalysis (2013).Transpositionofnativechromatinforfastandsensitiveepigenomic
1546 Cell173,1535–1548,May31,2018
profilingofopenchromatin,DNA-bindingproteinsandnucleosomeposition. Javierre,B.M.,Burren,O.S.,Wilder,S.P.,Kreuzhuber,R.,Hill,S.M.,Sewitz,S.,
Nat.Methods10,1213–1218. Cairns, J., Wingett, S.W., Va´rnai, C., Thiecke, M.J., et al.; BLUEPRINT
Buenrostro, J.D., Wu, B., Chang, H.Y., and Greenleaf, W.J. (2015a). Consortium (2016). Lineage-specific genome architecture links enhancers
ATAC-seq: a method for assaying chromatin accessibility genome-wide. and non-coding disease variants to target gene promoters. Cell 167,
Curr.Protoc.Mol.Biol.109,21.29.1–21.29.9. 1369–1384.
Karamitros,D.,Stoilova,B.,Aboukhalil,Z.,Hamey,F.,Reinisch,A.,Samitsch,
Buenrostro,J.D.,Wu,B.,Litzenburger,U.M.,Ruff,D.,Gonzales,M.L.,Snyder,
M.,Quek,L.,Otto,G.,Repapi,E.,Doondeea,J.,etal.(2018).Single-cellanal-
M.P.,Chang,H.Y.,andGreenleaf,W.J.(2015b).Single-cellchromatinacces-
sibilityrevealsprinciplesofregulatoryvariation.Nature523,486–490. ysisrevealsthecontinuumofhumanlympho-myeloidprogenitorcells.Nat.
Immunol.19,85–97.
Busch,K.,Klapproth,K.,Barile,M.,Flossdorf,M.,Holland-Letz,T.,Schlenner,
Kelsey,G.,Stegle,O.,andReik,W.(2017).Single-cellepigenomics:recording
S.M.,Reth,M.,Ho¨fer,T.,andRodewald,H.-R.(2015).Fundamentalproperties
ofunperturbedhaematopoiesisfromstemcellsinvivo.Nature518,542–546.
thepastandpredictingthefuture.Science358,69–75.
Laurenti,E.,andGo¨ttgens,B.(2018).Fromhaematopoieticstemcellstocom-
Calo,E.,andWysocka,J.(2013).Modificationofenhancerchromatin:what,
how,andwhy?Mol.Cell49,825–837.
plexdifferentiationlandscapes.Nature553,418–426.
Lawrence,H.J.,Helgason,C.D.,Sauvageau,G.,Fong,S.,Izon,D.J.,Humph-
Chen,L.,Kostadima,M.,Martens,J.H.A.,Canu,G.,Garcia,S.P.,Turro,E.,
ries,R.K.,andLargman,C.(1997).Micebearingatargetedinterruptionofthe
Downes,K.,Macaulay,I.C.,Bielczyk-Maczynska,E.,Coe,S.,etal.(2014).
homeoboxgeneHOXA9havedefectsinmyeloid,erythroid,andlymphoidhe-
Transcriptionaldiversityduringlineagecommitmentofhumanbloodprogeni-
matopoiesis.Blood89,1922–1930.
tors.Science345,1251033.
Li,H.,Courtois,E.T.,Sengupta,D.,Tan,Y.,Chen,K.H.,Goh,J.J.L.,Kong,S.L.,
Corces,M.R.,Buenrostro,J.D.,Wu,B.,Greenside,P.G.,Chan,S.M.,Koenig,
Chua,C.,Hon,L.K.,Tan,W.S.,etal.(2017).Referencecomponentanalysisof
J.L.,Snyder,M.P.,Pritchard,J.K.,Kundaje,A.,Greenleaf,W.J.,etal.(2016).
single-cell transcriptomes elucidates cellular heterogeneity in human colo-
Lineage-specificandsingle-cellchromatinaccessibilitychartshumanhema- rectaltumors.Nat.Genet.49,708–718.
topoiesisandleukemiaevolution.Nat.Genet.48,1193–1203.
Long,H.K.,Prescott,S.L.,andWysocka,J.(2016).Ever-changinglandscapes:
Crane,G.M.,Jeffery,E.,andMorrison,S.J.(2017).Adulthaematopoieticstem transcriptionalenhancersindevelopmentandevolution.Cell167,1170–1187.
cellniches.Nat.Rev.Immunol.17,573–590.
Magnusson, M., Brun, A.C.M., Lawrence, H.J., and Karlsson, S. (2007).
Dobin,A.,Davis,C.A.,Schlesinger,F.,Drenkow,J.,Zaleski,C.,Jha,S.,Batut,
Hoxa9/hoxb3/hoxb4compoundnullmicedisplayseverehematopoieticde-
P.,Chaisson,M.,andGingeras,T.R.(2013).STAR:ultrafastuniversalRNA-seq fects.Exp.Hematol.35,1421–1428.
aligner.Bioinformatics29,15–21.
Manz,M.G.,Miyamoto,T.,Akashi,K.,andWeissman,I.L.(2002).Prospective
Espı´n-Palazo´n,R.,Stachura,D.L.,Campbell,C.A.,Garcı´a-Moreno,D.,Del isolationofhumanclonogeniccommonmyeloidprogenitors.Proc.Natl.Acad.
Cid, N., Kim, A.D., Candel, S., Meseguer, J., Mulero, V., and Traver, D. Sci.USA99,11872–11877.
(2014). Proinflammatory signaling regulates hematopoietic stem cell emer-
Matsuoka,Y.,Sumide,K.,Kawamura,H.,Nakatsuka,R.,Fujioka,T.,Sasaki,
gence.Cell159,1070–1085.
Y.,andSonoda,Y.(2015).Humancordblood-derivedprimitiveCD34-negative
Fairfax,B.P.,Humburg,P.,Makino,S.,Naranbhai,V.,Wong,D.,Lau,E.,Jos- hematopoieticstemcells(HSCs)aremyeloid-biasedlong-termrepopulating
tins,L.,Plant,K.,Andrews,R.,McGee,C.,andKnight,J.C.(2014).Innate HSCs.BloodCancerJ.5,e290.
immuneactivityconditionstheeffectofregulatoryvariantsuponmonocyte
Mifsud,B.,Tavares-Cadete,F.,Young,A.N.,Sugar,R.,Schoenfelder,S.,Fer-
geneexpression.Science343,1246949.
reira,L.,Wingett,S.W.,Andrews,S.,Grey,W.,Ewels,P.A.,etal.(2015).Map-
Farlik,M.,Halbritter,F.,Mu¨ller,F.,Choudry,F.A.,Ebert,P.,Klughammer,J., pinglong-rangepromotercontactsinhumancellswithhigh-resolutioncapture
Farrow,S.,Santoro,A.,Ciaurro,V.,Mathur,A.,etal.(2016).DNAmethylation Hi-C.Nat.Genet.47,598–606.
dynamicsofhumanhematopoieticstemcelldifferentiation.CellStemCell19,
Naik,S.H.,Perie´,L.,Swart,E.,Gerlach,C.,vanRooij,N.,deBoer,R.J.,and
808–822.
Schumacher,T.N.(2013).Diverseandheritablelineageimprintingofearlyhae-
Frelin,C.,Herrington,R.,Janmohamed,S.,Barbara,M.,Tran,G.,Paige,C.J., matopoieticprogenitors.Nature496,229–232.
Benveniste, P., Zun˜iga-Pflu¨cker, J.-C., Souabni, A., Busslinger, M., and
Notta,F.,Gan,O.I.,Wilson,G.,Kaufmann,K.B.,Mcleod,J.,Laurenti,E.,Dun-
Iscove,N.N.(2013).GATA-3regulatestheself-renewaloflong-termhemato-
ant,C.F.,John,D.,Stein,L.D.,Dror,Y.,etal.(2016).Distinctroutesoflineage
poieticstemcells.Nat.Immunol.14,1037–1044.
developmentreshapethehumanbloodhierarchyacrossontogeny.Science
Fulco,C.P.,Munschauer,M.,Anyoha,R.,Munson,G.,Grossman,S.R.,Perez, 351,aab2116.
E.M.,Kane,M.,Cleary,B.,Lander,E.S.,andEngreitz,J.M.(2016).Systematic Novershtern,N.,Subramanian,A.,Lawton,L.N.,Mak,R.H.,Haining,W.N.,
mappingoffunctionalenhancer-promoterconnectionswithCRISPRinterfer- McConkey,M.E.,Habib,N.,Yosef,N.,Chang,C.Y.,Shay,T.,etal.(2011).
ence.Science354,769–773.
Denselyinterconnectedtranscriptionalcircuitscontrolcellstatesinhumanhe-
Goldberg,A.D.,Allis,C.D.,andBernstein,E.(2007).Epigenetics:alandscape matopoiesis.Cell144,296–309.
takesshape.Cell128,635–638.
Orkin,S.H.,andZon,L.I.(2008).Hematopoiesis:anevolvingparadigmfor
Graf,T.,andEnver,T.(2009).Forcingcellstochangelineages.Nature462, stemcellbiology.Cell132,631–644.
587–594. Paul,F.,Arkin,Y.,Giladi,A.,Jaitin,D.A.,Kenigsberg,E.,Keren-Shaul,H.,
Gru¨n,D.,Muraro,M.J.,Boisset,J.-C.,Wiebrands,K.,Lyubimova,A.,Dhar- Winter,D.,Lara-Astiaso,D.,Gury,M.,Weiner,A.,etal.(2015).Transcriptional
madhikari,G.,vandenBorn,M.,vanEs,J.,Jansen,E.,Clevers,H.,etal. heterogeneity and lineage commitment in myeloid progenitors. Cell 163,
(2016).Denovopredictionofstemcellidentityusingsingle-celltranscriptome 1663–1677.
data.CellStemCell19,266–277. Pei,W.,Feyerabend, T.B., Ro¨ssler, J.,Wang, X., Postrach, D.,Busch, K.,
Guo,M.H.,Nandakumar,S.K.,Ulirsch,J.C.,Zekavat,S.M.,Buenrostro,J.D., Rode,I.,Klapproth,K.,Dietlein,N.,Quedenau,C.,etal.(2017).Polyloxbar-
Natarajan, P., Salem, R.M., Chiarle, R., Mitt, M., Kals, M., et al. (2017).
codingrevealshaematopoieticstemcellfatesrealizedinvivo.Nature548,
Comprehensivepopulation-basedgenomesequencingprovidesinsightinto 456–460.
hematopoietic regulatory mechanisms. Proc. Natl. Acad. Sci. USA 114, Perie´,L.,Duffy,K.R.,Kok,L.,deBoer,R.J.,andSchumacher,T.N.(2015).The
E327–E336. branchingpointinerythro-myeloiddifferentiation.Cell163,1655–1662.
Haghverdi,L.,Bu¨ttner,M.,Wolf,F.A.,Buettner,F.,andTheis,F.J.(2016).Diffu- Regev,A.,Teichmann,S.A.,Lander,E.S.,Amit,I.,Benoist,C.,Birney,E.,Bod-
sionpseudotimerobustlyreconstructslineagebranching.Nat.Methods13, enmiller,B.,Campbell,P.J.,Carninci,P.,Clatworthy,M.,etal.(2017).Science
845–848. Forum:TheHumanCellAtlas.eLife6,e27041.
Cell173,1535–1548,May31,2018 1547
Satpathy,A.T.,Wu,X.,Albring,J.C.,andMurphy,K.M.(2012).Re(de)finingthe poieticstemcelllineagecommitmentisacontinuousprocess.Nat.CellBiol.
dendriticcelllineage.Nat.Immunol.13,1145–1154. 19,271–281.
Sawamiphak,S.,Kontarakis,Z.,andStainier,D.Y.R.(2014).Interferongamma Waddington,C.(1957).TheStrategyoftheGenes:ADiscussionofSome
signalingpositivelyregulateshematopoieticstemcellemergence.Dev.Cell AspectsofTheoreticalBiology(Allen&Unwin).
31,640–653.
Woodworth,M.B.,Girskis,K.M.,andWalsh,C.A.(2017).Buildingalineage
Schep,A.N.,Wu,B.,Buenrostro,J.D.,andGreenleaf,W.J.(2017).chromVAR: fromsinglecells:genetictechniquesforcelllineagetracking.Nat.Rev.Genet.
Inferringtranscriptionfactorvariationfromsingle-cellepigenomicdata.Nat. 18,230–244.
Methods14,975–978.
Yu,V.W.C.,Yusuf,R.Z.,Oki,T.,Wu,J.,Saez,B.,Wang,X.,Cook,C.,Bar-
Shin,J.,Berg,D.A.,Zhu,Y.,Shin,J.Y.,Song,J.,Bonaguidi,M.A.,Enikolopov, yawno,N.,Ziller,M.J.,Lee, E.,etal. (2016).Epigenetic memory underlies
G.,Nauen,D.W.,Christian,K.M.,Ming,G.-L.,andSong,H.(2015).Single-cell cell-autonomousheterogeneousbehaviorofhematopoieticstemcells.Cell
RNA-seq with waterfall reveals molecular cascades underlying adult 167,1310–1322.
neurogenesis.CellStemCell17,360–372.
Zhao,C.,Xiu,Y.,Ashton,J.,Xing,L.,Morita,Y.,Jordan,C.T.,andBoyce,B.F.
Takahashi,K.,andYamanaka,S.(2006).Inductionofpluripotentstemcells (2012).NoncanonicalNF-kBsignalingregulateshematopoieticstemcellself-
frommouseembryonicandadultfibroblastculturesbydefinedfactors.Cell renewalandmicroenvironmentinteractions.StemCells30,709–718.
126,663–676.
Zheng,G.X.Y.,Terry,J.M.,Belgrader,P.,Ryvkin,P.,Bent,Z.W.,Wilson,R.,
Velten, L., Haas,S.F., Raffel,S., Blaszkiewicz, S.,Islam, S.,Hennig,B.P., Ziraldo,S.B.,Wheeler,T.D.,McDermott,G.P.,Zhu,J.,etal.(2017).Massively
Hirche,C.,Lutz,C.,Buss,E.C.,Nowak,D.,etal.(2017).Humanhaemato- paralleldigitaltranscriptionalprofilingofsinglecells.Nat.Commun.8,14049.
1548 Cell173,1535–1548,May31,2018
