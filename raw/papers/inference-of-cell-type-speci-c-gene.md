---
source_path: /mnt/c/Users/Administrator/Zotero/storage/T5XKLRGW/Zhang 等 - 2023 - Inference of cell type-specific gene regulatory ne.pdf
ingested: 2026-04-23
sha256: a5198d804402a9cf
---

Article https://doi.org/10.1038/s41467-023-38637-9
fi
Inference of cell type-speci c gene
regulatory networks on cell lineages from
single cell omic datasets
Received:25July2022 ShiluZhang1,SaptarshiPyne1,StefanPietrzak1,2,SpencerHalberg1,3,
SunnieGraceMcCalla1,4,AlirezaFotuhiSiahpirani1,5,RupaSridharan1,2&
Accepted:10May2023
SushmitaRoy 1,3
Checkforupdates Celltype-specificgeneexpressionpatternsareoutputsoftranscriptionalgene
regulatorynetworks(GRNs)thatconnecttranscriptionfactorsandsignaling
proteinstotargetgenes.Single-celltechnologiessuchassinglecellRNA-
sequencing(scRNA-seq)andsinglecellAssayforTransposase-Accessible
Chromatinusingsequencing(scATAC-seq),canexaminecell-typespecific
generegulationatunprecedenteddetail.However,currentapproachesto
infercelltype-specificGRNsarelimitedintheirabilitytointegratescRNA-seq
andscATAC-seqmeasurementsandtomodelnetworkdynamicsonacell
lineage.Toaddressthischallenge,wehavedevelopedsingle-cellMulti-Task
NetworkInference(scMTNI),amulti-tasklearningframeworktoinfertheGRN
foreachcelltypeonalineagefromscRNA-seqandscATAC-seqdata.Using
simulatedandrealdatasets,weshowthatscMTNIisabroadlyapplicable
frameworkforlinearandbranchinglineagesthataccuratelyinfersGRN
dynamicsandidentifieskeyregulatorsoffatetransitionsfordiverseprocesses
suchascellularreprogramminganddifferentiation.
Transcriptional gene regulatory networks (GRNs) specify connec- Existing methods of network inference from single cell omic
tionsbetweenregulatoryproteinsandtargetgenesanddetermine data4–16have primarilyused transcriptomicmeasurements and have
thespatialandtemporalexpressionpatternsofgenes1,2.Thesenet- low recovery of experimentally verified interactions17,18. Recently a
worksreconfigureduringdynamicprocessessuchasdevelopmentor smallnumberofmethodshaveattemptedtointegratescRNA-seqand
disease progression, to specify cell type specific expression levels. scATAC-seqdatasets19–21toexaminegeneregulation,however,many
Recent advances in single cell omic techniques such as single cell ofthesemethodsfocusondefininingcellclustersandthenetworkis
RNA-sequencing(scRNA-seq)andsinglecellAssayforTransposase- definedentirelybasedonaccessiblesequence-specificmotifmatches.
Accessible Chromatin using sequencing (scATAC-seq)3 enable col- Thisrestrictstheclassofregulatorsthatcanbeincorporatedintothe
lectinghighresolutionmolecularphenotypesofadevelopingsystem regulatorynetworktothosewithknownmotifs.Furthermore,existing
andofferunprecedentedopportunitiesforthediscoveryofcelltype- methodsinferasingleGRNfortheentiredatasetordonotmodelthe
specificregulatorynetworksandtheirdynamics.However,compu- cellpopulationstructurewhichisimportanttodiscerndynamicsand
tationalmethodstosystematicallyleveragethesedatasetstoidentify transitionsintheinferrednetworksforcelltype-specificity.Toover-
regulatorynetworksdrivingcelltype-specificexpressionpatternsare comethelimitationsofexistingmethods,wehavedevelopedsingle-
limited. cell Multi-Task Network Inference (scMTNI), a multi-task learning
1WisconsinInstituteforDiscovery,UniversityofWisconsin-Madison,Madison,WI,USA.2DepartmentofCellandRegenerativeBiology,UniversityofWisconsin-
Madison,Madison,WI,USA.3DepartmentofBiostatisticsandMedicalInformatics,UniversityofWisconsin-Madison,Madison,WI,USA.4Laboratoryof
Genetics,UniversityofWisconsin-Madison,Madison,WI53706,USA.5Presentaddress:DepartmentofBioinformatics,InstituteofBiochemistryandBio-
physics,UniversityofTehran,Tehran,Iran. e-mail:sroy@biostat.wisc.edu
NatureCommunications|( 2023)1 4:3064 1
;,:)(0987654321 ;,:)(0987654321
Article https://doi.org/10.1038/s41467-023-38637-9
frameworkthatintegratesthecelllineage structure,scRNA-seq and Theseapproachesidentifykeyregulatorsandsubnetworksassociated
scATAC-seq measurements to enable joint inference of cell type- withaparticularcellclusterorasetofcellclustersonabranch.
specificGRNs.scMTNItakesasinputacelllineagetree,scRNA-seqdata
andscATAC-seqbasedpriornetworksforeachcelltype.scMTNIusesa Multi-tasklearningalgorithmsoutperformsingle-taskalgo-
probabilisticpriortoincorporatethelineagestructureduringnetwork rithmsforsinglecellnetworkinference
inferenceandoutputsGRNsforeachcelltypeonacelllineage.We ToevaluatescMTNIandotherexistingalgorithmswithknownground
performedacomprehensivebenchmarkingstudyofmulti-tasklearn- truthnetworksonsingle-celltranscriptomicdata,wesetupasimula-
ing approaches including scMTNI on simulated data and show that tionframework,whichentailedcreationofacelllineage,generating
incorporationofmulti-tasklearningandtreestructureisbeneficialfor syntheticnetworksandcorrespondingsingle-cellexpressiondatasets
GRNinference. for each cell type on the lineage (Fig. 2a). We used a probabilistic
WeappliedscMTNItoapreviouslyunpublishedscRNA-seqand process of network structure evolution to generate the network
scATAC-seqtimecoursedatasetforcellularreprogramminginmouse structure for three cell types, each containing 15 regulators and 65
and two published scRNA-seq and scATAC-seq cell-type specific genes and between 202–239 edges (Methods). Next, we applied
datasets for human hematopoietic differentiation. We demonstrate BoolODE17 to simulate the in silico single-cell expression data using
the advantage of scMTNI’s framework to integrate scATAC-seq and eachcelltype’sgeneratednetwork.Tomimicthesparsityinsingle-cell
scRNA-seqdatasetsforinferringcelltypespecificGRNsonlinearand expression data, we set 80% of the values to 0. We created three
branchinglineagetopologies.Weexaminedhowtheinferrednetworks datasetswithdifferentnumbersofcells:2000,1000,and200,refer-
change along the trajectory and identified regulators and network redhereasdatasets1,2,and3.
components specific to different parts of the lineage tree. Our pre- Weaskedwhethermulti-tasklearningisbeneficialcomparedto
dictions include known as well as previously uncharacterized reg- single-task learning for network inference from scRNA-seq data. To
ulators of cell populations transitioning to different lineage paths, this end, we compared scMTNI and four other multi-task learning
providinginsightintoregulatorymechanismsassociatedwithrepro- algorithms, MRTLE25, GNAT26, Ontogenet27, and AMuSR28 to three
grammingefficiencyandhematopoieticspecification. single-task algorithms, LASSO regression29, INDEP, and SCENIC30
(Methods).Ofthesemethods,onlySCENICusesanon-linearregres-
Results sion model while the others are based on linear models. INDEP is
Single-cellMulti-TasklearningNetworkInference(scMTNI)for similar to scMTNI but does not incorporate the lineage prior. Each
definingregulatorynetworksoncelllineages algorithm was applied within a stability selection framework and
We developed scMTNI, a multi-task graph learning framework for evaluated with Area under the Precision recall curve (AUPR) and
inferringcelltype-specificgeneregulatorynetworksfromscRNA-seq F-score oftop k edges,where kisthe number ofedges in the true
and scATAC-seqdatasets (Fig. 1a),whereacelltype is definedbya network(Fig.2b,c).Ondataset1,basedonAUPR,scMTNI,MRTLE,and
clusterofcellswithadistincttranscriptional,and,ifavailable,acces- AMuSRareabletorecoverthenetworkstructurebetterthantheother
sibilityprofile.scMTNImodelsaGRNasaDependencynetwork22,a multi-task learning and single-task learning algorithms (Fig. 2b).
probabilistic graphical model with random variables representing Ontogenetperformsbetterthanthesingle-tasklearningalgorithmsin
genesandregulators,suchastranscriptionfactors(TFs)andsignaling at least two cell types. Finally, GNAT performs comparably to the
proteins. single-tasklearningalgorithms.Whencomparingalgorithmsbasedon
scMTNI takes as input cell clusters with gene expression and F-scoreoftopkedges,wehavesimilarobservationsthatscMTNIand
accessibilityprofilesand alineagestructure linking thecellclusters MRTLE have a better performance than other algorithms (Fig. 2c).
(Fig.1).Suchinputscanbeobtainedfromexistingmethodsforinte- OntogenetperformsbetterthanLASSOandINDEPinatleasttwocell
grative clustering23 and lineage construction24. scMTNI uses the types,andcomparabletoSCENIC,exceptthatOntogenetincelltype3
scATAC-seq data for each cell cluster to define cell type-specific isworsethanSCENIC.GNATiscomparabletothesingle-tasklearning
sequencemotif-basedTF-targetinteractions(e.g.,amotifforaparti- algorithmsforatleast2ofthecelltypes.ThelowF-scoreofAMuSRis
cularTF,whichisaccessibleonlyinspecificcelltypeswillresultinaTF- because the inferred networks are too sparse, with fewer than 100
targetinteractiononlyinthosecelltypes)whichareusedasapriorto edges,whiletheotheralgorithmsinferredsimilarnumberofedgesas
guidenetworkinference(Methods).scMTNIcanalsotakebulkATAC- thetruenetworks.Theseresultsremainconsistentfordatasets2and3
seq data for corresponding cell types to generate cell type-specific which have fewer cells (1000 and 200, respectively); scMTNI and
prior networks or cell type-agnostic priors derived from sequence- MRTLEremainsuperiorinperformancethanotheralgorithmsmea-
specificmotifsthatinturncouldbefilteredwithrelevantATAC-seq suredbybothAUPRandF-score(Fig.2b,c).WeexpectscMTNItobe
data. scMTNI’s multi-task learning framework incorporates a prob- bettersincethenetworksimulationprocedureissimilar,butthedata
abilistic lineage tree prior, which uses the lineage tree structure to generationprocessisdifferentandindependentfromscMTNI’smodel.
influencethe similarity of gene regulatory networks on the lineage. Finally,weaggregatedtheresultsacrossallthreecelltypesanddata-
ThislineagetreepriormodelsthechangeofaGRNfromastartstate setstoobtainanoverallcomparisonofthealgorithms.Herewecon-
(e.g.,progenitorcellstate)toanendstate(e.g.,moredifferentiated sideredalgorithmsacrossallparametersettingstestedaswellasthe
state)asaseriesofindividualedge-levelprobabilistictransitions.The bestparametersettingdeterminedbythebestF-scoreorAUPR.Based
outputofscMTNIisasetofcelltype-specificGRNsoneforeachcell on the AUPR of “all parameter setting”, we found that multi-task
clusterinthelineagetree.scMTNIisabletoincorporatebothlinear learningmethods,especiallyscMTNIandMRTLEaregenerallybetter
lineage and tree-based lineage structure. scMTNI takes known cell thansingle-tasklearningmethodswithhigherAUPRs(Supplementary
lineagetreestructureorcomputationallyinferredcelllineageusing, Fig.1A,C).AMuSRalsooutperformedthesingle-taskalgorithmsbased
forexample,aminimumspanningtree(MST24)approachonscRNA- onAUPRs,althoughthiswasnotassignificantasMRTLEandscMTNI.
seqdata.WhilescMTNIwasdevelopedtoincorporatebothscRNA-seq Whenconsideringthe“bestparametersetting”,themethodswerenot
andscATAC-seqdata,itcanbeappliedtosituationswherescATAC- significantlydifferentwhenusingAUPR,thoughMRTLEandscMTNI
seq,andthereforeacelltype-specificpriornetwork,isnotavailable. hadthehighestAUPR(SupplementaryFig.1B,D).WhenusingtheF-
WerefertotheversionsofourapproachasscMTNI+PriorandscMTNI score,scMTNIandMRTLEremainedtopperformingalgorithmsforthe
dependinguponwhetheritusespriorknowledgeornot.Theoutput “all parameter setting” (Supplementary Fig. 2A, C) and the “best
networksofscMTNIareanalyzedusingtwodynamicnetworkanalysis parameter setting” (Supplementary Fig. 2B, D). Further, GNAT and
methods:edge-basedk-meansclusteringandtopicmodels(Fig.1b). OntogenethadahigherF-scorethanthesingle-tasklearningmethod
NatureCommunications|( 2023)1 4:3064 2
a Lineage tree scRNA-seq data
C1 C2 C3
C2
Gene expressions
Lineage prior
scATAC-seq + motifs
TF1 motif C1 TF1 motif C2
C4 Gene1 XGene1
X
TF2 motif TF2 motif
XGene2 Gene2
X
TF1TF2 TF1TF2
G1 G2 G1 G2
Prior network
LASSOforthe“allparameter”and“bestparameter”settings,respec- and MRTLE are able to more accurately infer networks than other
tively.AMuSRsufferedontheF-scoremetricduetothehighsparsityin multi-tasklearningalgorithms.
theinferrednetworks.Acrossdifferentsingle-taskalgorithms,LASSO
hadtheworstperformance.Overall,theresultsonthesimulatednet- Inferenceofgeneregulatorynetworksofsomaticcellrepro-
workssuggestthatmulti-tasklearningalgorithmshaveabetterper- grammingtoinducedpluripotentstemcells
formancethansingle-taskalgorithmsfornetworkinferenceonsparse Cellularreprogrammingistheprocessofconvertingcellsinadiffer-
datasetssuchassingle-celltranscriptomicdata.Furthermore,scMTNI entiatedstatetoapluripotentstateandisimportantinregenerative
eneG
C4 X
P(Iu C , 5 v| I u C , 4 v ) X1 3
C1 X X 3 2 X 4
X4 X X
X5 2 5
C5 C2 C3 X6 X
X7 6
X8
t I h e u C , 5 v s i t n at d u i s c a o t f o r e d v g a e ri a u b -> le v t i h n a t C e 5 ncodes X9 X 1
TF1 motif C3
Gene1 C3 X 3 X 3
X 4 X 4
TF2 motif
Gene2 X 2 X 5 X 2 X 5
X 6 X 6
X 1 X 1
TF1TF2
G1 G2
b
X3
X4
C1 X2 X5
X6
X1
X3
X4
C2 X2 X5
X6 X1
X3 X4 C3 X2 X5
X6
X1
c
Simulations
C1 C2 C3
Cellular reprogramming
D3 D6 D9D12
MEF iPSCs
Hematopoiesis
HSC CMP GMP Mono
snaem-k
ADL
X X X 3 5
X1X2X3X4X5X6
X 3 X 5 X 6
6 X 3 X 6 X 4 X 1 X 5 X X 6 X 4 X 1 3 X 5
X 4 X 1
desab-egdE
gniledom
cipoT
gniretsulc
C1 C2 C3
C1
X C2 X 3 5 X 6
X C3 X 3
X 5 k topics
6
scipot
k
Article https://doi.org/10.1038/s41467-023-38637-9
targets
TFs
Human fetal hematopoiesis
HSC-MPP
LMP GP MEMP
Mono pDC B Granulocyte Ery Mast Megakaryocyte
NatureCommunications|( 2023)1 4:3064 3
Article https://doi.org/10.1038/s41467-023-38637-9
Fig.1|AnoverviewofthescMTNIframework.ascMTNItakesasinputacell threecelltypes,whilethethreerealdatasetscamefromareprogrammingtime-
lineagetreeandcelltype-specificscRNA-seqdataandcelltype-specificpriornet- seriesprocess,immunophenotypiccelltypesidentifiedduringhumanadult
worksderivedfromscATAC-seqdatasets.IfscATAC-seqdataisnotavailable,bulk hematopoieticdifferentiation,andimmunophenotypicbloodcellsduringhuman
orsequence-basedpriornetworkscanbeusedforthecelltypes.Theoutputof fetalhematopoiesis.MEFmouseembryonicfibroblast,iPSCsinducedpluripotent
scMTNIisasetofcelltype-specificgeneregulatorynetworksforeachcelltypeon cells,HSChematopoieticstemcell,CMPcommonmyeloidprogenitor,GMP
thecelllineagetree.bTheoutputnetworksofscMTNIareanalyzedusingtwo granulocyte-macrophageprogenitors,Monomonocyte,HSC-MPPhematopoietic
dynamicnetworkanalysismethods:edge-basedk-meansclusteringandLatent stemcellsandmultipotentprogenitors,LMPlymphoid-myeloidprogenitors,
DirichletAllocation(LDA)basedtopicmodelstoidentifykeyregulatorsandsub- MEMPMK-erythroid-mastprogenitorscombinedwithcyclingMEMPs,GPgranu-
networksassociatedwithaparticularcellclusterorasetofclustersonabranch. locyticprogenitors,Eryerythroidcells,pDCplasmacytoiddendriticcells.
cDatasetsusedwithscMTNI.Thesimulationdatacomprisedalineartrajectoryof
medicine as well as for generating patient-specific disease models. scMTNI+PriorhadamongthehighestF-scores,highnumberofpre-
However, this process is inefficient as a small fraction of cells get dictableTFsandagreatercoverageofthegoldstandardscomparedto
reprogrammed to the pluripotent state31. To gain insight into gene competingmethodsusingexpressionalone(SCENIC)aswellasthose
regulatory networks that govern the dynamics of this process, we that either incorporated accessibility information (CellOracle,
profiledsinglecellaccessibility(scATAC-seq)duringreprogramming INDEP+Prior)orcelllineageinformation(scMTNI).
of mouse embryonic fibroblasts (MEFs) to the induced pluripotent Toperformaninitialassessmentofthenetworkdynamicsonthe
stateandfourintermediatetimepoints,day3,day6,day9,andday12, celllineage,wecomputedF-scorebetweeneachpairofinferrednet-
toconstituteadatasetof6timepoints.WeusedLIGERtointegratethe works defined by the top 4k edges (Fig. 3g). Both scMTNI and
scRNA-seqandscATAC-seqdatasets(Fig.3a,b)andidentified8clus- scMTNI+Prior networks diverged in a manner consistent with the
ters(Methods).Oftheseclusters,C4isMEF-specificwhileC5isESC- lineagestructure.scMTNInetworksformedthreegroupsofcelltypes,
specific(Fig.3c,d)andshowedgoodintegrationofthescRNA-seqand (C4,C8,C1,C7),(C2,C3)and(C5(ESC)).scMNTI+Priorfoundsimilar
scATAC-seqprofiles(SupplementaryFig.3).WeremovedC6asitdid groupingsbutplacedC5(ESC)closerto(C1,C7,C8,C4)branch.Both
not have scRNA-seq cells and applied a minimum spanning tree methodsshowedthatC5isclosesttoC1,whichcouldbeanimportant
(MST24) approach to construct the cell lineage tree from the 7 cell transitioning state of cells during reprogramming. SCENIC showed
clusterswithbothscRNA-seqandscATAC-seq(Methods,Fig.3e).The similarityamongC1,C4,C7,howeverhadlowersimilarityscoresfor
MEF-specific cluster (C4) is at one end of the tree, while the ESC- mostpairwisecomparisonswhichmadeitdifficulttodiscernaclear
specific cluster (C5) is at the other end. This is consistent with the lineagestructure.CellOracletopologyidentifiedthe(C2,C3)group,
starting and end state of the reprogramming process and we con- but placed itunder a subtree with (C4, C8), which, though feasible
sidered C4 to represent the root of the tree. The other clusters giventheheterogeneityofthesystem,islessconsistentwiththegra-
representedamixofcellsfromdifferenttimepoints,whichiscon- dual progression of the reprogramming process through the inter-
sistentwiththelevelofheterogeneityofthereprogrammingsystem32. mediateC7state.Thenetworksinferredbytheothermethodswere
Wefurtherverifiedtheidentityoftheseintermediateclusterswitha verydissimilarwhichisbiologicallyunrealisticgiventhehighhetero-
Monoclebasedtrajectoryanalysis33whichshowsthatC7,C2,andC3 geneity of the reprogramming system with several intermediate
representcellsthatmightexitthetrajectorytowardsreprogramming populations32. Overall, these results suggest that scMTNI+Prior
andC8representscellsupstreamofthispoint(SupplementaryFig.4). recovered regulatory networks of high quality and the networks
WeappliedscMTNI,scMTNI+Prior(scMTNIwithpriornetwork), exhibit a gradual rewiring of structure from the MEF to the
INDEP, INDEP+Prior (INDEP with prior network), SCENIC and addi- pluripotentstate.
tionallyCellOracletothisdataset(Fig.3f).WeincludedCellOracleasit
combinesscRNA-seqandscATAC-seqdata,byusingaccessibilityto scMTNIpredictskeyregulatorynodesandGRNcomponents
restrictthesetofedgesselectedbasedonexpression.Weusedthe thatarerewiredduringreprogramming
matchedscATAC-seqclusterstoobtainTF-targetpriorinteractionsfor Togaininsightintotheregulatorymechanismsofcellpopulationsthat
each scRNA-seq cluster needed for INDEP+Prior, scMTNI+Prior and successfullyreprogramversusthosethatdonotandtofurtherchar-
CellOracle(Methods).Weassessedthequalityoftheinferrednetworks acterizethesedifferentcellclusters,weexaminedtherewirednetwork
bycomparingtomultiplegoldstandarddatasetsinmouseembryonic componentsineachcelltype-specificnetworkinferredbyscMTNI+
stemcells(mESCs,Table1):onederivedfromChIP-seqexperiments Prior.Weusedtwocomplementaryapproaches:k-meansedgeclus-
("ChIP”)fromESCAPEorENCODEdatabases34,35,onefromregulator teringandLatentDirichletAllocation(LDA,Methods).Inthek-means
perturbation experiments ("Perturb”)34,36, and the third from the edge clustering approach, we represented each edge in the top 4k
intersectionofedgesinChIPandPerturb("ChIP+Perturb”).Wefirst confidencesetofanycellcluster,byavectorofconfidencescoresin
comparedtheperformanceofthemethodsusingF-scoreonthetop each cell cluster-specific network (if an edge is not inferred in the
500,1k,and2kedgesacrossmethods(Fig.3f,SupplementaryFigs.5, networkitisassignedaweightof0).Next,weclusterededgesbasedon
6). On Perturb, CellOracle and scMTNI+Prior had the best perfor- theiredgeconfidencepatterninto20clustersdeterminedbytheSil-
mance,beatingotheralgorithmssignificantly.OnChIP,SCENICand houette Index coefficient optimization (Fig. 4a). The largest “edge
CellOracle were the best performing methods. Finally, on Perturb+ clusters”exhibitedinteractionsspecifictoonecellcluster(e.g.,E4,E6,
ChIP, CellOracle and scMTNI+Prior had the best performance. E7,E11,E13,E15,andE16),whilesmallerclustersexhibitedconserved
AlthoughCellOraclehadhighF-scores,itsinferredGRNsincludeda edges formore thanonecellcluster(e.g.,E2,E5,E12).Tointerpret
substantiallysmallernumberofregulators(7–11)comparedtoSCENIC theseedgeclusters,weidentifiedthetopregulatorsassociatedwith
orscMTNI+Prior(29–36).InadditiontoF-score,wealsoconsidered eachoftheedgeclusters(Fig.4b).E16,whichwasMEF-specific(C4)
thenumberofpredictableTFsasanadditionalmetric(Supplementary hadNpm1,Nme2,Thy1,Ddx5,andLoxl2asthetopregulatorswhichare
Fig.7,Methods).ThisisdefinedasthenumberofindividualTFswhose knownMEF-specificgenes.Incontrast,E11,whichwasESC-specific(C5)
targetshadasignificantoverlapwiththegold standard.Higherthe hadKlf4,Sp1,Sp3assomeofitstopregulators,whichhaveknownroles
number of predictable TFs, the better is a method. On ChIP, instemcellmaintenance(Klf4),orareessentialforearlydevelopment
scMTNI+Prior had the highest average number of predictable TFs. (Sp137)andpostnataldevelopment(Sp338).Edgeclustersthatshared
scMTNIhadthehighestnumberofpredictableTFsforthePerturb, edgesacrossmultiple cellclusters,e.g.,E5(C4,C8,and C1),shared
Perturb+ChIP datasets followed closely by scMTNI+Prior. Overall, someofthetop-rankingregulatorssuchasNpm1andThy1withthe
NatureCommunications|( 2023)1 4:3064 4
1) Simulate GRNs 2) Simulate in silico single-cell gene
expression data using BoolODE
Cell Lineage tree
C1 C2 C3
C1 C2 C3
C2=0 C2=1 C3=0 C3=1
C1=0 C1=1
C1=0 C2=0
C1=1 C2=1
C1 C2 C3
Cells
b AUPR
Dataset 1 Dataset 2 Dataset 3
cell type 3
celll type 2
cell type 1
GNAT scMTNIMRTLEOntogentAMuSR Lasso Scenic INDEP GNAT scMTNIMRTLEOntogentAMuSR Lasso Scenic INDEP GNAT scMTNIMRTLEOntogentAMuSR Lasso Scenic INDEP
model
AUPR 0.21 0.23 0.25 0.27 AUPR
0.21 0.23 0.25 0.27
c
Fscore
Dataset 1 Dataset 2 Dataset 3
cell type 3
cell type 2
cell type 1
GNAT scMTNIMRTLEOntogentAMuSR Lasso Scenic INDEP GNAT scMTNIMRTLEOntogentAMuSR Lasso Scenic INDEP GNAT scMTNIMRTLEOntogentAMuSR Lasso Scenic INDEP
model
Fscore Fscore 0.1 0.2 0.3
0.1 0.2 0.3
seneG
3) Add dropouts
seneG
C1 C2 C3
Cells
6) Evaluation 5) Run multi-task and single-task
GRN inference algorithms
AUPR
noisicerP
F-score of top edges
0
0
0 1
.
.
. .
2
5
7 0
5
0
5 0
0
0
0
.
.
.
2
3
4
●● ●●
●● ●●
●●●●●●●●●●●●●●●●●●●●●●●●●●●●
0.1 ●●
0.00 ●● ●●
0 0.250.5 0.75 1 25005000750010000
Recall Number of top edges
erocs-F
a
4) Generate 3 simulation datasets
Dataset 1: 2000 cells
0
seneg
56
C1 C2 C3
2000 cells 2000 cells 2000 cells
Dataset 2: 1000 cells (downsampled)
Dataset 3: 200 cells (downsampled)
seneg
56
C1 C2 C3
1000 cells 1000 cells 1000 cells
seneg
56
Article https://doi.org/10.1038/s41467-023-38637-9
Ontogenet
scMTNI
AMuSR GNAT
MRTLE
Scenic
INDEP
C1 C2 C3
200 cells200 cells200 cells Lasso
Fig.2|Benchmarkingalgorithmsonsimulateddata.aSimulationframeworkfor precisionandrecallcurve(AUPR)andF-scoreoftopedges.bAUPRcomparing
scMTNI.WefirstsimulateGRNsforcelltypesacrossacelllineagetree.Next,we inferrednetworkstogroundtruthnetworksofsimulateddatasets1,2,3.cF-score
generateinsilicosingle-cellgeneexpressiondataforeachcelltypeusingBoolODE comparingtopKedgesintheinferrednetworkstothoseinthegroundtruth
usingthesimulatedGRNsandadd80%zerosinthesimulationdata.Then,weapply networksofsimulateddatasets1,2,3(celltype1:K=202,celltype2:K=217,cell
fivemulti-tasklearningalgorithmsandthreesingle-tasklearningalgorithmsfor type3:K=239).Thebrighterandlargerthecirclethebettertheperformanceofthe
GRNinferencetothesimulateddatasetsandpredictnetworksinstabilityselection algorithm.SourcedataareprovidedasaSourceDatafile.
framework.Wecomparetheperformanceofthesealgorithmsbasedonareaunder
NatureCommunications|( 2023)1 4:3064 5
a LIGER clusters b Samples
scATAC-seq scRNA-seq
c d
MEF-specificclusterandalsoidentifiedotherfibroblast-specificgenes Whilethek-meansanalysisidentifiedregulatoryhubsspecificto
suchasCol5a2 and Ybx1. Finally, E2 which comprised shared edges individual cell clusters, it was challenging to identify entire sub-
betweencellclustersC1andC5,containedEsrrb,asitstopregulator networksthatrewiredatspecificbranchpointsbecauseittreatseach
(Fig.4b).Esrrbplaysanimportantroleforestablishingandmaintaining edgeindependently.WedevelopedanapproachbyadoptingLatent
thepluripotencynetwork39.Thisfurthersupportsthelineagestructure DirichletAllocation(LDA)thatwasrecentlyusedtostudyregulatory
thatC1likelyrepresentsapopulationofcellsthatarecommittedto network rewiring from transcription factor ChIP-seq datasets40
becomingpluripotent. (Methods).Inthisapproach,eachTFistreatedasa“document”and
qes-CATAcs
qes-ANRcs
UMAP 1
Totalcells C1 C2 C3 C4 C5 C6 C7 C8 FBS_Day12 5219 0.07 0 0.050.09 0 0.1 0.590.09
FBS_Day3 3315 0.050.190.170.25 0 0.120.060.15
FBS_Day6 5115 0.040.020.130.16 0 0.170.370.11
FBS_Day9 5333 0.040.010.08 0.1 0 0.110.580.07
MEF 4950 0 0 0.030.94 0 0.02 0 0.01
mESC 6412 0.06 0 0 0 0.93 0 0 0
FBS_Day12 403 0.140.090.220.060.03 0 0.44 0
FBS_Day3 685 0.390.030.130.29 0 0 0.090.07
FBS_Day6 601 0.14 0.1 0.180.08 0 0 0.470.03
FBS_Day9 706 0.180.080.230.03 0 0 0.470.02
FBS_mESCs 313 0.12 0 0.010.020.84 0 0 0
MEF_Day0 752 0.010.03 0 0.93 0 0 0 0.02
Number of cells Proportion of cells
Number of cells Proportion of cells
0 2500 5000 7500 0.00 0.25 0.50 0.75 2000 4000 6000 0.00 0.25 0.50 0.75
e f
2 PAMU
Cluster
1
2
3 4
5
6
7
8
UMAP 1
2 PAMU
Samples
atac_FBS_Day12
atac_FBS_Day3
atac_FBS_Day6
atac_FBS_Day9
atac_MEF atac_mESC
rna_FBS_Day12
rna_FBS_Day3
rna_FBS_Day6
rna_FBS_Day9
rna_FBS_mESCs
rna_MEF_Day0
Totalcellsatac rna
C1 1931 1357 574
C2 1015 816 199
C3 2540 2081 459
C4 8299 7298 1001
C5 6327 6050 277
C6 2452 2452 0
C7 9129 8272 857
C8 2111 2018 93
C4 MEF
FBS-Day3
C8 FBS-Day6
FBS-Day9
FBS-Day12
C7 C1
mESC
C3 C5
C2
retsulc
FBS_D F a B y1 S 2 _D F a B y S 3 _D F a B y S 6 _Da M y9 EF mESC FBS_D F a B y1 S 2 _D F a B y S 3 _D F a B y S 6 _D FB ay S 9 _ m M E E S F C _ s Day0
0.260.110.160.170.020.29 0.10.460.150.220.070.01
0.020.780.120.060.01 0 0.190.110.30.270.010.13
0.130.280.310.220.06 0 0.2 0.20.230.360.01 0
0.060.110.110.070.64 0 0.020.20.050.020.010.7
0 0 0 0 0 0.99 0.05 0 0 0 0.95 0
0.210.170.360.230.03 0 0 0 0 0 0 0
0.370.030.230.37 0 0 0.210.070.330.39 0 0
0.240.250.270.20.030.01 0.010.510.180.13 0 0.17
ChIP Perturb Perturb+ChIP
g
INDEP INDEP+Prior Scenic scMTNI scMTNI+Prior CellOracle
C5 C8 C2 C3 C7 C4 C1 C5 C8 C2 C3 C7 C4 C1 C5 C8 C2 C3 C7 C4 C1 C5 C3 C2 C1 C7 C4 C8 C3 C2 C5 C7 C8 C4 C1 C5 C4 C8 C3 C2 C1 C7
C5 0 0 0 0.010.010.01 C5 0 0 0 0.020.010.01 C5 0 0.010.010.020.040.05 C5 0.2 0.190.4 0.250.250.27 C3 0.170.060.160.110.160.13 C5 0.170.160.110.120.260.17
C8 0 0.010.010.010.020.02 C8 0 0.010.010.010.020.01 C8 0 0.030.030.040.070.05 C30.2 0.540.350.5 0.380.4 C20.17 0.050.110.070.110.09 C4 0.17 0.420.35 0.4 0.340.29
C2 0 0.01 0.020.010.040.01 C2 0 0.01 0.020.010.020.01 C20.010.03 0.060.040.070.04 C20.190.54 0.3 0.420.310.31 C50.060.05 0.1 0.090.090.23 C8 0.160.42 0.410.450.38 0.4
C3 0 0.010.02 0.030.050.03 C3 0 0.010.02 0.020.030.02 C30.010.030.06 0.060.090.07 C10.4 0.350.3 0.450.480.48 C70.160.110.1 0.170.210.18 C3 0.110.350.41 0.670.250.33
C70.010.010.010.03 0.050.04 C70.020.010.010.02 0.030.02 C70.020.040.040.06 0.140.13 C70.250.5 0.420.45 0.470.5 C80.110.070.090.17 0.210.18 C2 0.12 0.4 0.450.67 0.24 0.3
C40.010.020.040.050.05 0.07 C40.010.020.020.030.03 0.03 C40.040.070.070.090.14 0.17 C40.250.380.310.480.47 0.55 C40.160.110.090.210.21 0.23 C1 0.260.340.380.250.24 0.35
C10.010.020.010.030.040.07 C10.010.010.010.020.020.03 C10.050.050.040.070.130.17 C80.270.4 0.310.480.5 0.55 C10.130.090.230.180.180.23 C7 0.170.29 0.4 0.33 0.3 0.35
Fscore
0.00.2 0.4 0.6
PEDNI CINECS INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI CINECS INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI CINECS INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC
0.08
0.007
0.012 0.006 0.06
0.005 0.008
0.04
0.004 0.004
0.003 0.02
erocsf
Article https://doi.org/10.1038/s41467-023-38637-9
FBS Fscore (top1k)
FBS t−test FDR (top1k)
ChIP Perturb Perturb+ChIP
INDEP 0.0094< 0.15< 0.16< 0.15< 0.00021< 0.67> 0.19< 0.19< 0.013< 0.013< 0.56< 0.39< 0.1< 0.034< 0.0011<
SCENIC 0.0094> 0.16> 0.15> 0.0058> 0.81> 0.67< 0.29< 0.29< 0.035< 0.013< 0.56> 0.86> 0.2< 0.089<0.00064<
scMTNI 0.15> 0.16< 0.81> 0.72> 0.15< 0.19> 0.29> 0.42< 0.0029< 0.013< 0.39> 0.86< 0.15< 0.047<0.00064<
INDEP+Prior 0.16> 0.15< 0.81< 0.75> 0.15< 0.19> 0.29> 0.42> 0.027< 0.013< 0.1> 0.2> 0.15> 0.56< 0.12<
scMTNI+Prior 0.15> 0.0058< 0.72< 0.75< 0.021< 0.013> 0.035> 0.0029> 0.027> 0.013< 0.034> 0.089> 0.047> 0.56> 0.096<
CellOracle 0.00021> 0.81< 0.15> 0.15> 0.021> 0.013> 0.013> 0.013> 0.013> 0.013> 0.0011>0.00064>0.00064> 0.12> 0.096>
-log(FDR)
5.0 7.5 10.0
NatureCommunications|( 2023)1 4:3064 6
Article https://doi.org/10.1038/s41467-023-38637-9
Fig.3|Inferenceofcell-typespecificnetworksofmousecellularreprogram- FDR<0.05wasconsideredsignificantlybetter.Thesign<or>specifieswhether
mingdata.aUMAPofLIGERcellclustersonthescATAC-seqdataandscRNA-seq therowalgorithm’sF-scoreswereworseorbetterthanthecolumnalgorithm’s
data.bUMAPdepictingthesamplelabelsofthescATAC-seqandscRNA-seqdata F-scores.Thecolorscaleisspecifiedby−log(FDR),withtheredcolorproportional
frommousecellularreprogramming.cThedistributionofsamplesineachLIGER tosignificance.Non-significanceiscoloredingray.Intheboxplot,thehorizontal
cluster.dThedistributionofLIGERclustersineachsample.eInferredlineage middlelineofeachplotisthemedian.Theboundsoftheboxare0.25quantile(Q1)
structureforscMTNIlinkingthe7cellclusterswithscRNA-seqmeasurements. and0.75quantile(Q).Theupperwhiskeristheminimumofthemaximumvalue
3
fF-scoreoftop1kedgesinpredictednetworksofscMTNI,scMTNI+Prior,INDEP, andQ +1.5*IQR,whereIQR=Q −Q.Thelowerwhiskeristhemaximumofthe
3 3 1
INDEP+Prior,SCENICandCellOraclecomparedtothreegoldstandarddatasets: minimumvalueandQ1 −1.5*IQR.gPairwisesimilarityofnetworksfromeachcell
ChIP,PerturbandPerturb+ChIP.ThetopboxplotsshowtheF-scoresofn=7cell clusterusingF-scoreonthetop4kedges.Rowsandcolumnsareorderedbasedon
clusters,whilethebottomheatmapsshowFDRcorrectedt-testcomparingthe thedendrogramcreatedusingtheF-scoresimilarity.Sourcedataareprovidedasa
F-scoresoftherowalgorithmtothatofthecolumnalgorithm.Thetwo-sidedpaired SourceDatafile.
t-testisconductedonF-scoresofn=7cellclustersforeverypairofalgorithms.A
targetgenesaretreatedas“words”inthedocument.Eachdocument regulators that showed a difference in connectivity between these
(TF)isassumedtohavewords(genes)fromamixtureoftopics,each branchesincludingtopics2,3,4,6,8,and9.Theregulatorsthatgained
topic in turn interpreted as a pathway. TFs across cell clusters are edges in the pluripotency branch compared to the stalled branch
treated as separate documents. We applied LDA with k=10 topics included cell cycle regulators (Top2a, Ccnb1: topic 3) and known
(Fig.4c,d,SupplementaryFigs.8–10),andexaminedeachofthetopics pluripotencygenes(Esrrb:topic3andKlf4:topic4,Fig.4d).Incon-
based on their Gene Ontology process enrichment (Supplementary trast,regulatorsthatgainedconnectionsinC7-C3-C2branchrelative
Fig.11),andthetendencyandidentityofspecificregulatorstorewire totheC1-C5branch(ormaintainedconnectionssimilartoC4),inclu-
acrossthecellclusters.Topics3and6areenrichedforcellcycleterms dedMEF-specificgenessuchasLoxl2,Fosl2(topic2),Aebp1(topic6),
(SupplementaryFig.11).Otherprocessesassociatedwiththesetopics Hoxd13(topic8),andFosl1,Nme2andCcng1(topic9).Nme2isknown
includedimmuneresponse(topic1),developmentalprocesses(topics to regulate Myc, which is one of the four reprogramming factors41.
1,3and8),electrontransport(topic9),andchromosomeorganization Aebp1, associated with fibroblast differentiation42, and Loxl2, asso-
(topic10).Topic3networkswereamongthemostdivergentnetworks ciatedwithconnectivetissue43,44,persistedinallthreecellclustersin
acrossthecellpopulationsandidentifiedseveralknownregulatorsof thestalledbranch(C7-C3-C2).Overall,ouranalysisindicatedthatin
pluripotency(Fig.4c).Inparticular,EsrrbwasahubinC5(ESC)andC1 cell populations that do not reprogram successfully, cell cycle reg-
(closesttoESC)butabsentintheothercellclusters. ulators have lower connectivity while several of the MEF regulators
WeusedtheLDAanalysistofurthercharacterizecellpopulations (e.g.,Nme2,Aebp1)persistorgainconnections.Thesenewpredicted
thatbecomepluripotent(C1-C5branch),andthosethatremainstalled regulatorscanbeperturbedtoexaminetheimpactoncellularrepro-
(C7-C3-C2branch)byidentifyingregulatorsthatgainedorlostcon- grammingefficiency.
nections between these two branches. Several topics included
Inferringgeneregulatorynetworksinhumanhematopoietic
differentiation
Table1|Thestatisticsofthegoldstandarddatasetsusedfor ToexaminetheutilityofscMTNIinadifferentcellfatespecification
themousereprogrammingandhumanhematopoiesisstudies
system,weappliedscMTNItoapublishedscATAC-seqandscRNA-seq
Dataset Goldstandards Number Number
datasetforhumanadulthematopoieticdifferentiation45.Thisdataset
ofTFs oftargets profiledaccessibilityandtranscriptomicstateofimmunophenotypic
Mouse ChIP 54 31,367 populations that were sorted based on cell surface markers and
reprogramming enabled studies of how multipotent progenitors transition into
Perturb 179 21,019 lineage-specificcellstates.Weconsideredthecellpopulationsprofiled
Perturb+ChIP 47 6109 with both scATAC-seq and scRNA-seq datasets: hematopoietic stem
Human Hematopoieticstemcells(HSC) 6 9173 cell (HSC), common myeloid progenitor (CMP), granulocyte-
hematopoiesis macrophageprogenitors(GMP)andmonocyte(Mono).Thesepopu-
CD14_monocytes 1 6523 lations are known to be heterogeneous comprising multiple sub-
populations45. To identify these sub-populations, we again applied
megakaryocytes 4 8733
LIGER23andidentified10integratedclustersofRNAandaccessibility
erythroid_progenitors 1 7955
(Fig.5a–d).Mostclustersexhibitedamixedcomposition:C8ismainly
R3R4_erythroid_cells 1 8494
composed of HSCs but also included CMP0 cells; C6 and C9 are
macrophages 1 163
composedofGMPandCMP0cells.C1(73cells)andC4(37cells)were
CD34_hematopoietic_stem_cells- 3 5847 mainlycomposedofMonocellsandwerecombinedintoC1.C5had
derived_proerythroblasts
toofewRNAcells(22cells)andwasexcludedfromfurtheranalysis.We
T-cells 3 6189 next inferred a cell lineage tree from these 8 cell clusters using a
B-cells 1 7036 minimalspanningtreeapproach24asdescribedinthereprogramming
GM_B-cells 48 10,597 study(Fig.5e,Methods).AsC8islargelymadeupofHSCcellsandHSC
Human UniBind 56 10,621 isthestartingcelltype,wetreatedC8astherootofthelineage.
hematopoiesis Weappliedthesamesetofnetworkinferencealgorithmstothis
Cus_ChIP 149 6179 datasetasthereprogrammingdataset:scMTNI,scMTNI+Prior,INDEP,
Cus_KO 50 6108 INDEP+Prior,SCENICandCellOracle.Weassessedthequalityofthe
inferred networks from each method by comparing them to gold-
Cus_KO+Cus_ChIP 26 2124
standardedgesfrompublishedChIP-seqandregulatorperturbation
Cus_KO+UniBind 12 2020
assays from several human hematopoietic cell types. This included
Formousereprogramming,shownarenetworkstatisticsforthemouseembryonicstemcell ChIP-seq datasets from the UniBind database (Unibind46), ChIP-seq
(ESC)linefromESCAPE34andENCODE35databasesandNishiyamaetal.36.Forthehuman
hematopoieticstudies,shownarenetworkstatisticsforthegoldstandarddatasetsobtained (Cus_ChIP) and regulator perturbation (Cus_KO) experiments in the
fromtheUniBinddatabase46andCusanovichetal.47. GM12878 lymphoblastoid cell line from Cusanovich et al.47 and the
NatureCommunications|( 2023)1 4:3064 7
a b
kmeans clustering
C4 C8 C1 C5 C7 C3 C2 # Edges
E20 0.95 0.71 0.86 0.24 0.8 0.88 0 153
E18 0.94 0.57 0.91 0.24 0.89 0 0.12 231
E1 0.93 0.6 0.75 0.28 0.87 0.94 0.88 225
E5 0.93 0.24 0.88 0 0 0.06 0.04 266 Degree
E9 0.93 0.09 0.07 0 0.02 0.85 0.27 189 60
E14 0.93 0.23 0 0.06 0.87 0.13 0.08 260 40 E10 0.91 0.07 0.37 0.85 0.01 0.05 0.05 148
E16 0.89 0.03 0 0 0 0 0.02 2498 20
E17 0.46 0.69 0.87 0.85 0 0.12 0.13 66 0
E19 0.01 0.09 0.05 0.07 0.87 0.84 0.38 195 Degree
E7 0 0 0 0 0 0 0.69 3032 60
E6 0 0.5 0 0 0 0 0 2731
E E 12 8 0 0 0 0 . . 1 0 4 9 0 0 . . 3 8 5 8 0. 0 83 0 0 . . 8 8 8 4 0 0 . . 0 1 9 2 0 0 . . 0 1 3 1 1 1 9 4 0 0 4 2 0 0 0
E3 0 0.03 0.04 0.05 0 0.8 0.76 280
E2 0 0.02 0.85 0.84 0 0.01 0.04 552
E13 0 0.02 0.82 0 0 0.01 0.01 # Ed2g2e29s
E15 0 0.01 0 0 0.81 0 0.01 2634
E11 0 0.01 0 0.78 0 0.01 0 2774
E4 0 0.01 0.01 0.01 0 0.76 0 2765
c Topic 3 networks Sp1 Mcm6 Ets1
Wt1 Ax C l d44 NTporp12Nausap1 Sp2 Sp1 Uhrf1 Mcm6
Sp1 Uhrf1 Mcm6 Sp1 Uhrf1 Mcm6 Esrrb Ccnb1 Axl Top2aNusap1 Sp2
Axl
Nusap1 Sp2 Cd44 Top2a Sp2 Esrrb Ccnb1
CcnPblk11
C1 C5
C7 C3 C2
C8
C4
weight #targets MEF
0.80 a 0 FBS-Day3 Wt1 Ets1 Wt1 Wt1
0.85 a 10 FBS-Day6 Sp1 Uhrf1 Mcm6 Sp1 Uhrf1 Mcm6 Sp1 Mcm6
0.90 a 20 FBS-Day9 Axl Cd44 Nusap1 Axl Cd44 Axl Cd44
0.95 a 30 FBS-Day12 Ccnb1 Ccnb1
mESC
1.00
d
topic: 1 topic: 2 topic: 3 topic: 4 topic: 5
Hn G D Y rn d b n x p a x 5 1 k s T F L T c o o h f s x 1 y l l 2 2 1 2 N C u M U C s c c S h n a d m A r b p 4 p f x 1 6 1 4 1 1 l Hs C p I E g o P 9 f E l c K K r 5 0 b r m l a b p k l l x f f 2 7 4 3 1 1 1 3 H N m T u A A r g p i a b t t r f f 2 1 4 5 3
Fk S b Z p t I a i r 1 c f t 2 7 a 1 P D N k m C n r r 0 s o t f b x c 1 1 2 2 r T E o N E P S W s p p t l r 2 p k s r r t 1 b 1 1 a 1 2 D P u F X d T s E o g K b p h x g A f p 1 y l c r r f 1 1 b 3 1 4 1 xl P D F o o E m u S x g 3 r p h r f t 4 1 1 3 1
topic: 6 topic: 7 topic: 8 topic: 9 topic: 10
M Ju eg n 3 b F T K h c lf f l2 6 4 Cnbp C R N c r m S n e g e b p 1 2 1 3 G Ce a n bp p a a
Npm1 Tgf E b1 ts i 2 1 Hnrnpab F B o t s g l1 2 Ccnf
Aebp1 Hoxc8 Klf2 Zfp B 1 t 4 f3 8 Pttg1
Egr2 Elk Il 1 k Hoxd13 Zf S p u 2 b 8 1 1 Sep15
Mo T r c f f 4 1 l2 5 A Zb n C t k d b r 4 7 d b 4 1 Wt1 T T c c E e e V g b b r d 1 2 1 r Fk D bp d 1 x a 5
C4 C8 C1 C5 C7 C3 C2 C4 C8 C1 C5 C7 C3 C2 C4 C8 C1 C5 C7 C3 C2 C4 C8 C1 C5 C7 C3 C2 C4 C8 C1 C5 C7 C3 C2
Degree 10 20 30 40 Degree
0 10 20 30 40
1mpN 6flK 2a5loC 2emN 1pbeA 1gncC 3pbfgI 1pS 1tW 1xbY pbnC 41psuD 3klE 4flK 1yhT apneC 21flK 1rpuN 1xrrP 3pS 2lcsA b1fahC r1fsC 5xdD fhE 4flE brrsE 2pxoF 5frI 7flK 2xhL 2lxoL leaM 1rpN 1b0rN 2liwiP 2xonkP 4daeT 31pfZ 24pfZ 528pfZ
Article https://doi.org/10.1038/s41467-023-38637-9
Top regulators for edge clusters
E20
E18
E1
E5
E9
E14 E10
E16
E17
E19
E7
E6
E12 E8
E3
E2
E13
E15
E11
E4
number
score of edges
0.00 0.25 0.50 0.75 1000 2000 3000
Top regulators per topic and cluster
Fig.4|NetworkdynamicsanalysisofGRNsfromcellularreprogramming. andbrightnessofthecircleisproportionaltothenumberoftargets.cLDAtopic3
ak-meansclusteringanalysisoftop4kedgesininferrednetworks.Shownarethe networksalongthecelllineage.Thelayoutofeachnetworkisthesame,edges
meanprofilesofedgeconfidenceof20edgeclusters.Eachrowcorrespondstoan presentinaparticularcellclusterareshowninred.Labelednodescorrespondto
edgeclusterandeachcolumncorrespondstoacellcluster.Theredintensity regulatorswithdegreelargerthan10.dTopcellcluster-specificregulatorsforeach
correspondstotheaverageconfidenceofedgesinthatcluster.Shownalsoarethe topic.Shownareonlyregulatorsthathaveatleast10targetsinanycellcluster.The
numberofedgesintheedgecluster.bTop5regulatorsforeachedgecluster. moreyellowandlargerthecircle,thegreaterarethenumberoftargetsforthe
Shownareonlyregulatorsthathaveatleast10targetsinanyedgecluster.Thesize regulator.SourcedataareprovidedasaSourceDatafile.
NatureCommunications|( 2023)1 4:3064 8
10
1
5
7
3 0 4 2 10 8
6
−5
9
−10
5
−15
−20 −10 0 10
UMAP 1
intersection of ChIP and perturbation studies (Cus_KO+Cus_ChIP, onthreeofthefivegoldstandards.OnUnibindandCus_KO+Unibind,
Cus_KO+Unibind). Intotal, wehad five gold standardnetworks.We SCENIC is significantly better than INDEP and scMTNI (Fig. 5f, Sup-
usedF-scoreandthenumberofpredictableTFsofthetop500,1k,2k plementaryFig.13).Methodsthatusedpriorknowledge,CellOracle,
edges in the inferred network (Methods, Fig. 5f, Supplementary INDEP+Prior, scMTNI+Prior, were generally better than methods
Fig.12).Therelativeperformanceofthealgorithmsdependedupon withoutpriorsfortheChIP-baseddatasets(Cus_ChIP,Unibind).Cel-
thegoldstandard.Algorithmsthatdidnotusepriors(INDEP,SCENIC lOracle performs better than INDEP+Prior and scMTNI+Prior on
andscMTNI)performedcomparably(withnosignificantdifference) Cus_ChIPandUnibind,butisoutperformedbyallmethodsonanyof
2 PAMU
10
rna−mono
5
Cluster
1 rrnnaa−−ccmmr ppn 21a−cmp0 1 2 0 0 tac−mono rn a a t a − a t h c a − s c c H − S C C MP 3 atac−GMP
4 5 rna−gmp
6 −5
7
8
9
−10
−15
−20 −10 0 10
UMAP 1
2 PAMU
a LIGER clusters b Samples e Cell lineage tree
C8
Celltype
atac−CMP C3 atac−GMP atac−HSC atac−mono
rna−cmp0 C2 rna−cmp1
rna−cmp2
rna−gmp
rna−hsc C6 C1
rna−mono
C9 C10
C7
c
Totalcells C1 C2 C3 C4 C5 C6 C7 C8 C9 C10
hsc CMP 492 0.070.170.030.070.080.120.120.160.070.12
GMP 402 0.120.070.010.160.050.230.030.080.190.06 cmp0
HSC 347 0.120.090.050.080.060.120.110.270.050.05 cmp1
mono 64 0.220.030.020.580.020.050.050.020.03 0
cmp2
cmp0 2508 0 0 0.03 0 0 0.070.610.150.040.09
cmp1 626 0 0.390.07 0 0 0.050.320.060.040.07 gmp
cmp2 1320 0 0.410.06 0 0 0.060.320.050.040.06 mono
gmp 1096 0 0.02 0 0 0 0.720.010.010.24 0
hsc 2268 0 0.260.08 0 0 0.01 0 0.64 0 0
mono 129 0.57 0 0 0.290.140.01 0 0 0 0
Number of cells
0 10001500 2500 0.000.250.500.751.00
qes-CATAcs
qes-ANRcs
d scATAC-seq scRNA-seq
Total
cellsatacCMPGMPHSCmonornacmp0cmp1cmp2gmphsc mono
C1 2101370.240.340.31 0.1 73 0 0 0 0 0 1
C2 15451430.58 0.2 0.210.011402 0 0.170.390.010.42 0
C3 421 35 0.370.110.490.03 386 0.180.12 0.2 0.010.49 0
C4 199162 0.2 0.4 0.170.23 37 0 0 0 0 0 1
C5 107 85 0.480.250.260.01 22 0.18 0 0 0 0 0.82
C6 1304195 0.3 0.470.220.0211090.170.030.070.720.02 0
C7 22931130.54 0.1 0.340.032180 0.7 0.09 0.2 0 0 0
C8 21502060.380.170.45 0 1944 0.2 0.020.03 0 0.75 0
C9 5631310.250.590.150.02 432 0.220.050.13 0.6 0 0
C10 460 98 0.590.230.17 0 362 0.650.120.220.01 0 0
Number of cells Proportion of cells Proportion of cells
500 2000 0 1000 2000 0.00 0.50 1.00
f Buenrostro Fscore (top 1k)
Cus_KO Cus_ChIP UniBind Cus_KO+Cus_ChIP Cus_KO+UniBind
0.010 0.08 0.14
0.010 0.0075 0.008 0.06 0.12
0.04 0.10
0.0050 0.006
0.005 0.02 0.08
0.0025 0.004 0.06
0.00 0.04
g
INDEP INDEP+Prior Scenic scMTNI scMTNI+Prior CellOracle
C1C3C9C8C6C2C10C7 C3C1C8C6C9C10C2C7 C1C9C3C10C2C8C6C7 C1C6C9C10C7C2C8C3 C1C6C9C10C7C2C8C3 C1C10C7C6C9C8C3C2
C1 0 0 0 0 0 0 0 C3 0.030.020.020.020.030.030.02 C1 0 0 0 0 0 0 0 C1 0.110.120.130.130.10.090.16 C1 0.020.060.050.040.010.020.02 C1 0.190.240.280.280.270.260.27
C3 0 0 0.010.010.020.010.02 C10.03 0.030.030.040.030.020.02 C90 0.050.080.060.070.140.1 C60.11 0.250.250.230.170.170.2 C60.02 0.1 0.10.120.070.080.07C100.19 0.57 0.5 0.510.480.560.52
C9 0 0 0.010.020.010.010.02 C80.020.03 0.060.030.030.030.03 C30 0.05 0.080.120.120.110.13 C90.120.25 0.290.260.150.140.19 C90.060.1 0.160.130.040.050.06 C70.240.57 0.460.490.480.530.52
C8 0 0.010.01 0.020.020.010.03 C60.020.030.06 0.040.030.030.04C100 0.080.08 0.1 0.10.120.19C100.130.250.29 0.380.170.160.22C100.050.10.16 0.220.060.060.08 C60.28 0.5 0.46 0.650.540.530.54
C6 0 0.010.020.02 0.020.020.04 C90.020.040.030.04 0.050.040.03 C20 0.060.120.1 0.160.140.2 C70.130.230.260.38 0.170.150.2 C70.040.120.130.22 0.090.090.1 C90.280.510.490.65 0.510.540.52
C2 0 0.020.010.020.02 0.020.04C100.030.030.030.030.05 0.040.04 C80 0.070.120.10.16 0.160.19 C20.10.170.150.170.17 0.190.22 C20.010.070.040.060.09 0.070.08 C80.270.480.480.540.51 0.6 0.6
C100 0.010.010.010.020.02 0.04 C20.030.020.030.030.040.04 0.04 C60 0.140.110.120.140.16 0.2 C80.090.170.140.160.150.19 0.23 C80.020.080.050.060.090.07 0.09 C30.260.560.530.530.54 0.6 0.69
C7 0 0.020.020.030.040.040.04 C70.020.020.030.040.030.040.04 C70 0.10.130.190.20.190.2 C30.160.20.190.220.20.220.23 C30.020.070.060.080.10.080.09 C20.270.520.520.540.52 0.6 0.69
Fscore
0.0 0.2 0.4 0.6
erocsf
Cus_KO Cus_ChIP UniBind Cus_KO+Cus_ChIP Cus_KO+UniBind
0.97> 0.23> 0.048< 0.048<0.00029> 0.8> 0.19>0.00027<0.0059<7.7e−05< 0.0093< 0.74>7.7e−05<0.0025<1.9e−05< 0.5> 0.63< 0.013< 0.053< 0.06> 0.0071<0.038> 0.095< 0.35> NA>
0.97< 0.72> 0.048< 0.083<0.00048> 0.8< 0.41> 0.0024< 0.03<0.00019< 0.0093> 0.01> 0.0011< 0.67<5.1e−05< 0.5< 0.52<0.00058<0.018< 0.13> 0.0071> 0.00065>0.041> 0.043> NA>
0.23< 0.72< 0.048< 0.048<0.00029> 0.19< 0.41< 4.2e−05<0.0016<7.3e−05< 0.74< 0.01< 0.00023<0.00084<1.9e−05< 0.63> 0.52> 0.079< 0.19< 0.053> 0.038<0.00065< 0.00028<0.92> NA>
0.048> 0.048> 0.048> 0.72> 2e−04> 0.00027>0.0024>4.2e−05> 0.22>0.00019< 7.7e−05>0.0011>0.00023> 0.071>2e−05< 0.013>0.00058>0.079> 0.078> 0.1> 0.095> 0.041<0.00028> 0.095> NA>
0.048> 0.083> 0.048> 0.72< 2e−04> 0.0059> 0.03> 0.0016> 0.22< 0.00045< 0.0025> 0.67>0.00084>0.071< 0.00034< 0.053> 0.018> 0.19> 0.078< 0.1> 0.35< 0.043< 0.92< 0.095< NA>
0.00029<0.00048<0.00029<2e−04<2e−04< 7.7e−05>0.00019>7.3e−05>0.00019>0.00045> 1.9e−05>5.1e−05>1.9e−05>2e−05>0.00034> 0.06< 0.13< 0.053< 0.1< 0.1< NA> NA> NA> NA> NA>
PEDNI CINECS INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI CINECS INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI CINECS INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI CINECS INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI CINECS INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC
Article https://doi.org/10.1038/s41467-023-38637-9
INDEP
SCENIC
scMTNI
INDEP+Prior
scMTNI+Prior
CellOracle
Buenrostro t−test FDR (top 1k) -log(FDR)
5.0 7.510.012.5
NatureCommunications|( 2023)1 4:3064 9
Article https://doi.org/10.1038/s41467-023-38637-9
Fig.5|Inferenceofcelltype-specificnetworksforhumanhematopoieticdif- FDR<0.05wasconsideredsignificantlybetter.Thesign<or>specifieswhether
ferentiationdata.aUMAPofLIGERcellclustersofthescATAC-seqandscRNA-seq therowalgorithm’sF-scoreswereworseorbetterthanthecolumnalgorithm’s
data.bUMAPdepictingtheoriginalcelltypes(samples)withscATAC-seqand F-scores.Thecolorscaleisspecifiedby−log(FDR),withtheredcolorproportional
scRNA-seqdata.cThedistributionofcellclustersineachsample.dThedistribu- tosignificance.Non-significanceiscoloredingray.Intheboxplot,thehorizontal
tionofsamplesineachLIGERcluster.eInferredlineagestructurelinkingtheeight middlelineofeachplotisthemedian.Theboundsoftheboxare0.25quantile(Q1)
cellclusterswithscRNA-seqdata.fBoxplotsshowingF-scoresofn=7cellclusters and0.75quantile(Q).Theupperwhiskeristheminimumofthemaximumvalue
3
(allcellclustersexcludingC1)fortop1kedgesinpredictednetworksfromscMTNI, andQ +1.5*IQR,whereIQR=Q −Q.Thelowerwhiskeristhemaximumofthe
3 3 1
scMTNI+Prior,INDEP,INDEP+Prior,SCENICandCellOraclecomparedtogold minimumvalueandQ1 −1.5*IQR.gPairwisesimilarityofnetworksfromeachcell
standarddatasets(top).FDR-correctedt-testtocomparetheF-scoreoftherow clusterusingF-scoreonthetop5kedges.Rowsandcolumnsorderedbyhier-
algorithmtotheF-scoreofthecolumnalgorithm(bottom).Thetwo-sidedpaired archicalclusteringusingF-scoreasthesimilaritymeasure.Sourcedataarepro-
t-testisconductedonF-scoresofn=7cellclustersforeverypairofalgorithms.A videdasaSourceDatafile.
the regulator perturbation datasets. INDEP+Prior and scMTNI+Prior hematopoieticstemcells51.E12additionallyhadKLF1,FLI1,S100A4as
arecomparableacrossthegoldstandarddatasetswithnosignificant top regulators. KLF1 is an essential regulator for the erythroid
differenceinperformance(Fig.5f,SupplementaryFig.13).Basedon lineage52,53, which isderived fromthe myeloidprogenitor cells.FLI1
numberofpredictableTFsinthepredictednetworks(Supplementary also plays a role in erythroid lineage by regulating the Erythpoetin
Fig.14),INDEP+PriorandscMTNI+Priorrecoveredmorepredictable protein54,suggestingthesecellsarecommittedtotheerythroidline-
TFs especially in KO experiments, while CellOracle recovered more age.Incontrast,E18whichsharededgesbetweenC6andC9identified
predictable TFs in Cus_ChIP and UniBind. For the Unibind dataset, immunesystem-relatedregulatorssuchasIRF8andNFKBIAwhichhave
wehadChIP-seqbasedgoldstandardedgesfordifferentbloodcell beenassociatedwithgenerallymphoiddevelopment(IRF855)orspe-
types,with1to48transcriptionfactors(Table1).Ofthe10celltypes, cific lineages such as B cells (NKBIA56). Overall, the k-means edge
methodsthatusedpriorsperformedsignificantlybetterthanmethods clusteringapproachhelpedidentifythekeyregulatorswithknownor
thatdidnotontheGM_B-cellsandHematopoieticStemCells(HSCs) plausible roles in hematopoiesis that could explain the differences
which had the largest number of TFs (Supplementary Figs. 15, 16). amongthedifferentlineages.
However,CellOraclehadmuchlowerperformanceinothercelltypes Our LDA topic analysis predicted several cell type-specific net-
and was outperformed by methods with and without priors, likely workcomponents with different extents of conservation acrossthe
becauseofthesmallernumberofTFsinthesedatasets.Thenumberof lineage (Fig. 6c, d, Supplementary Figs. 18–20). These topics were
predictableTFsperdatasetandmethodwasgenerallylowwiththe enrichedindiversebiologicalprocessessuchascellcycle(Topic1and
exceptionofGM_B-cellswheremethodswithpriorswerebetterthan 8,SupplementaryFig.21)andbloodrelatedprocesses(Topic9).Topic
methodswithoutpriors(SupplementaryFig.17).However,thesegold 2showedagradualrewiringofanID2-specificnetworkfromtheHSC
standardsweremuchsmallerandthereforecanassesssmallerportion populations(C8,C3,C2),toKLF1andMYCcenterednetworksforC7
oftheinferrednetworks. andC10whichrepresentedtheCMPpopulations(Fig.6c,d).ID2which
Wenextexaminedtheinferrednetworksfortheextentofchange belongstotheInhibitorsofDNAfamilyofproteinshasbeenshownto
on the lineage structure (Fig. 5g). The single-task learning methods regulateboththeerythroidandlymphoidlineages57andisconsistent
INDEPandINDEP+Priorexhibitedalowoverlapacrosseachpairofcell withitspresenceintheC8,C3,C2clusters.Furthermore,KLF1con-
linesanddidnotassuchobeythelineagestructure.SCENICrecovers nectivitywasmorepronouncedinC7comparedtoC10,whichcould
partofthelineagestructure,butplacedC7(commonmyeloid)closeto indicatethesecellsaremorecommittedthanthoseinC10.Similarly,
C6 (granulocyte-macrophage progenitors (GMP)) rather than C10, PBX1whichisakeyregulatorofdifferentiationversusself-renewalwas
whichhassimilarsamplecompositionasC7.Incontrast,scMTNIand seeninC7andC9.Topic3capturedadditionaldifferencesbetweenthe
scMTNI+Priorwereabletofindtwogroupsofcelltypes,onecorre- twoGMPclusters,C6andC9,withIRF8exhibitingmoreconnectionsin
spondingtotheHSCandCMP2branchconsistingofC8,C3,andC2, C6comparedtoC9(Fig.6d,SupplementaryFig.18).Topics1,6and10
andthesecondcorrespondingtotheCMP0,CMP1,andGMPbranch exhibited a conserved core around HMGB2, TSC22D3, and YBX1
(C6,C9,C10,andC7).CellOraclealsoinferredasimilartreewithsmall respectively, across all cells clusters (Supplementary Figs. 18–20).
variationswithinthesetwogroups.Forthisdataset,theadditionof HMGB2isanimportantregulatorforHSCs58.BothYBX1andTSC22D3,
accessibility or lineage information was helpful to capture realistic whichwerealsoidentifiedinourk-meansanalysis,haveknownrolesin
extentsofnetworklevelchanges. hematopoiesis48. Topic 8 wasassociated with various cell cycleand
chromatinremodelingregulatorssuchasTOP2A,CDC20,andCCNB1
Inferringsharedandlineage-specificregulatorsforhemato- (SupplementaryFigs.20,21).Takentogether,theLDAanalysisiden-
poieticdifferentiation tifiedsubnetworkscenteredoncandidatekeyregulatorswithknown
Similartoourcellularreprogrammingstudy,weexaminedthescMTNI generalrolesinhematopoiesisaswellasregulatorsinvolvedinspecific
+Priornetworkstoidentifycelltype-specificregulatorsandnetwork lineagedecisions.
components (Fig. 6) with k-means and LDA analysis. We applied
k-meansedgeclusteringtotheunionoftop5kedgesinanyofthecell Inferringgeneregulatorynetworksinhumanfetal
clustersandidentified19edgeclusters(Methods).Comparedtothe hematopoiesis
reprogrammingstudy,alargerportion(94%vs86%)oftheedgesare Our applications of scMTNI so far were on cell lineages where a
specifictoonecellcluster(Fig.6a).Weusedtheseedgeclustersto branching structure was computationally inferred. To examine the
examine the differences and similarities at the branch between the utilityofscMTNIinasystemwithknownbranchinglineagestructure,
CMPclusters(C7,C10),andtheGMPclusters(C6andC9).Edgecluster we applied it to a published scATAC-seq and scRNA-seq dataset of
E12wasspecifictoC7and C10,E18wasspecifictoC6and C9,and humanfetalhematopoiesis59,whichcapturedspecificationtomultiple
E19sharededgesfromC6,C9,C10,C7.BothE19andE12hadYBX1and bloodlineages(Fig.7a).Weconsideredthecellpopulationsmeasured
TSC22D3astopregulators(Fig.6b).YBX1isknowntodirectfateof withbothscATAC-seqandscRNA-seqdatasetsattworesolutions:(1)
HSCswithhighexpressioninmyeloidprogenitorcells48andinvolved coarse resolution comprising hematopoietic stem cell (HSC), multi-
in monocyte/macrophage differentiation49. TSC22D3, whichisa glu- potent progenitors (MPPs), lymphoid-myeloid progenitors (LMPs),
cocorticoid leucine zipper50, is involved in differentiation of MK-erythroid-mast progenitors (MEMPs), granulocytic progenitors
NatureCommunications|( 2023)1 4:3064 10
Top regulators for edge clusters
kmeans clustering b
C8 C3 C2 C1 C6 C9 C10 C7 # Edges
E9 0.91 0.85 0.83 0.09 0.93 0.91 0.86 0.97 152
E14 0.83 0.13 0.05 0.02 0.23 0.12 0.14 0.93 123
E16 0.81 0.45 0.73 0.05 0.28 0.12 0.07 0 116
E15 0.8 0.69 0.87 0.02 0.78 0.04 0.64 0.96 128
E3 0.69 0.01 0 0 0 0 0 0 4390
E18 0.08 0.06 0.04 0.09 0.82 0.76 0.25 0 126
E10 0.08 0.15 0.8 0.02 0.01 0.03 0.14 0.94 142
E19 0.08 0.06 0.09 0.08 0.87 0.89 0.86 0.96 188
E7 0.03 0.08 0.22 0.02 0.83 0.09 0.12 0.94 106
E13 0.01 0.04 0.02 0.09 0 0.76 0.42 0.91 243
E17 0.01 0.04 0.01 0.1 0 0.66 0.64 0 277
E12 0.01 0.03 0.01 0.03 0.01 0 0.77 0.93 493
E11 0 0 0 0 0.71 0 0 0 4202
E6 0 0 0 0.02 0 0.64 0 0 3909
E4 0 0.38 0 0 0 0 0 0 4186
E8 0 0 0 0.01 0 0 0.61 0 3515
E2 0 0.01 0 0.01 0 0 0 0.89 3428
E5 0 0 0.67 0 0 0 0 0 4382
E1 0 0 0 0.31 0 0 0 0 4437
score
0.00 0.25 0.50 0.75 1000200030004000
c Topic 2 networks
weight C6 0.80 0.85 a 0
0.90 a 20
0.95 a 40
1.00 a 60
d Top regulators per topic and cluster
Degree 10 20 30 40 Degree
0 10 20 30 40
1XBY 3D22CST 2NGMH 2BGMH 1FLK 1A1FEE 7FLK 1ILF 2DI 2FLK 3FLK 4FLK 1MILDP KELP 4A001S 3PS 6DRKNA 1PPLOD 4FLE A2MPE 5VTE APBAG 1IFG XLH 8FRI 21FLK 5FLK 4LTBM3L 2DBM 8MCM ADNM AIBKFN 4HCTON 6F2RN A1RLOP 41SGR 1PS 4PS A2POT 3ORYT 4KLU 202FNZ 714FNZ 47FNZ 39FNZ
Article https://doi.org/10.1038/s41467-023-38637-9
a
E9
E14
E16
E15
E3
E18
E10
E19
E7
E13
E17
E12
E11
E6
E4
E8
E2
E5
E1
number
of edges Degree Degree 200100 0
100 200
ID2 NFKBIA ID2 NFKBIA PBX2 ID2 JUNB ID2 JUNB
MYC MYC NFKBIA MYC NFKBIA
KLF1 KLF1
PBX2 PBX2
C1 MCM3 PBX1
C8 CCCCCC33333 C2 C10 C7
hsc
ID2
cmp0 NFKBIA
cmp1 ID2 JUNB #targets ID2 JUNB MYC NFKBIA cmp2 NFKBIA C9 KLF1
MYC PBX2
gmp
mono PBX2 MCM3 PBX1
topic: 1 topic: 2 topic: 3 topic: 4 topic: 5
N H H U M M M S C G G A M N B P 2 3 2 1 NF P K M B B I Y D X I C A 2 2 K C L I D R F K F 1 8 3 1 HSP N E 9 E C P N 0 L F B M O K L 1 1 1 1 1 Z E F E P P F F 3 O T Z 1 6 M S F A L B A X 1 2
MYBL2 KLF12
A R U A P K R D L L K K F 5 B 1 1 5 M J P K C U B L N M X F B 3 1 1 PD E L F T I L M V I 5 1 1 ZB E T K S B T L A V P 7 F R A 2 8 1 Z G B A T K K F B B L L G 7 P F F R A B 7 3
topic: 6 topic: 7 topic: 8 topic: 9 topic: 10
CDC20 S1 P 0 L 0 E A K 4 YBX1
KLF4 CCNB1 CTNNBL1
GATA1 E2F2
PTTG1 KLF2
TSC22D3 CYCS TOP2A P P P T P P 1 R R C 1 A 4A P MAD2L1
AURKA LAT
SP3 MCM7
EGR1 NR2C2 TLE1
PLK1 E Z E N F F 1 5 A 7 1 8 PTMA
C8C3C2C1C6C9C10C7 C8C3C2C1C6C9C10C7 C8C3C2C1C6C9C10C7 C8C3C2C1C6C9C10C7 C8C3C2C1C6C9C10C7
Fig.6|Networkrewiringduringhematopoieticdifferentiation.ak-meansedge numberoftargets.cTopic-specificnetworksacrosseachcellclusterfortopic2.The
clustersofthetop5kedges(rows)across8cellclusters(columns).Theedge layoutofeachnetworkisthesame,edgespresentinaparticularcellclusterare
confidencematrixwasclusteredinto19clusterstoidentifycommonanddivergent showninred.Labelednodescorrespondtoregulatorswithdegreelargerthan10.
networks.Theredintensitycorrespondstotheaverageconfidenceofedgesinthat dTopregulatorsassociatedwitheachcellcluster’snetworkineachtopic.Shown
cluster.Shownalsoarethenumberofedgesintheedgecluster.bTop5regulators areonlyregulatorsthathaveatleast10targetsinanycellcluster.Themoreyellow
ofeachedgecluster.Shownareonlyregulatorswithatleast10targetsinagiven andlargerthecircle,thegreaterarethenumberoftargetsfortheregulator.Source
edgecluster.Thesizeandbrightness(yellow)ofthecircleisproportionaltothe dataareprovidedasaSourceDatafile.
NatureCommunications|( 2023)1 4:3064 11
a Cell lineage tree
b
Cus_KO Cus_ChIP UniBind Cus_KO+Cus_ChIP Cus_KO+UniBind
c
scMTNI scMTNI+Prior CellOracle
(GPs),and(2)fine-grainedresolution,whichadditionallyincludedthe difference)onallfivegoldstandards(Fig.7b,SupplementaryFigs.22,
derivedcelltypesfromtheseprogenitorpopulations.Weevaluated 23)).INDEP+Prior,scMTNI+Prior,whichusepriorsweresignificantly
themethodsthatincorporatepriorandtheirno-priorversionsonthis betterthanmethodswithoutpriors,whileCellOracleperformedthe
dataset:scMTNI,scMTNI+Prior,INDEP,INDEP+Prior,andCellOracle,at worstinallgoldstandards.INDEP+PriorandscMTNI+Priorarecom-
twolevelsofresolutionofthecelltypes(Methods). parableacrossthegoldstandarddatasets.BasedonpredictableTFs,
Onthefinelineage,algorithmsthatdidnotusepriors(INDEPand scMTNI+PriorandINDEP+Priorwerethebest(SupplementaryFig.24).
scMTNI)performedcomparablybasedonF-score(withnosignificant AsobservedintheBuenrostrodataset,CellOracledidcomparablyto
PEDNI INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC PEDNI INTMcs roirP+PEDNI roirP+INTMcs elcarOlleC
0.020 0.010
0.008 0.09
0.015 0.008 0.10
0.006 0.06
0.010
0.005 0.004 0.006 0.03 0.05
0.002 0.004 0.00
erocsf
Ranzoni Fscore (top 1k)
Cus_KO Cus_ChIP UniBind Cus_KO+Cus_ChIP Cus_KO+UniBind
0.62< 0.0015<0.00021<0.00021> 0.14< 0.0052<0.0022<0.0052> 0.087< 0.0025<0.001< 0.071> 0.6< 2.8e−05<2.5e−05<1.8e−05> 0.21> 0.0044< 0.2< 1.2e−05>
0.62> 0.0033<0.00087<7e−05> 0.14> 0.0058<0.0022<0.0052> 0.087> 0.0096<0.00061<0.028> 0.6> 8.2e−05<9.9e−05<1.8e−05> 0.21< 1.8e−05<0.0044<2.8e−06>
0.0015>0.0033> 0.63> 7e−05> 0.0052>0.0058> 0.28> 0.0022> 0.0025>0.0096> 0.92> 0.0096> 2.8e−05>8.2e−05> 0.007>1.8e−05> 0.0044>1.8e−05> 0.12> 2.8e−06>
0.00021>0.00087>0.63< 7e−05> 0.0022>0.0022> 0.28< 0.0022> 0.001>0.00061>0.92< 0.0087> 2.5e−05>9.9e−05>0.007< 1.8e−05> 0.2> 0.0044> 0.12< 1.7e−05>
0.00021<7e−05<7e−05<7e−05< 0.0052<0.0052<0.0022<0.0022< 0.071< 0.028< 0.0096<0.0087< 1.8e−05<1.8e−05<1.8e−05<1.8e−05< 1.2e−05<2.8e−06<2.8e−06<1.7e−05<
INDEP INDEP+Prior
PEDNI INTMcs
roirP+PEDNI roirP+INTMcs
elcarOlleC
PEDNI INTMcs
roirP+PEDNI roirP+INTMcs
elcarOlleC
PEDNI INTMcs
roirP+PEDNI roirP+INTMcs
elcarOlleC
PEDNI INTMcs
roirP+PEDNI roirP+INTMcs
elcarOlleC
PEDNI INTMcs
roirP+PEDNI roirP+INTMcs
elcarOlleC
Ranzoni t−test FDR (top 1k)
INDEP
scMTNI
INDEP+Prior
scMTNI+Prior
CellOracle
-log(FDR)
3 6 9 12 15
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 00.010.010.010.01
0 0 0.010 00.0100.010.010.01
0 00.01 0 00.010.010.010.010.01
0 0 0 0 0 0 00.010.010.01
0 0 0 0 0 0.010.010.010.010.01
0 00.010.0100.01 0.010.010.010.01
00.0100.0100.010.01 0.010.020.02
00.010.010.010.010.010.010.01 0.020.03
00.010.010.010.010.010.010.020.02 0.05
00.010.010.010.010.010.010.020.030.05
sllec−diorhtyrE
sPML
setyconoM
sCDp
etycoyrakageM
sllec−tsaM etycolunarG
sPG sllec−B sPMEM
sPPM−CSH
Erythroid−cells 0.0100.010.010 0 00.010.010.01
LMPs 0.01 0.010.020.010.010.010.010.010.010.01
Monocytes 00.01 0.030.010.010.010.010.010.020.01
pDCs 0.010.020.03 0.020.030.010.010.010.020.01
Megakaryocyte 0.010.010.010.02 0.020.010.020.010.020.02
Mast−cells 00.010.010.030.02 0.020.020.020.030.03
Granulocyte 00.010.010.010.010.02 0.020.020.040.02
GPs 00.010.010.010.020.020.02 0.020.040.03
B−cells 0.010.010.010.010.010.020.020.02 0.070.04
MEMPs 0.010.010.020.020.020.030.040.040.07 0.07
HSC−MPPs 0.010.010.010.010.020.030.020.030.040.07
setyconoM
sCDp
sllec−tsaM
etycoyrakageM
etycolunarG
sllec−diorhtyrE
sPML sPG sllec−B sPMEM
sPPM−CSH
Monocytes 0.120.130.110.130.120.120.130.170.120.13
pDCs 0.12 0.140.110.130.120.130.120.190.130.13
Mast−cells 0.130.14 0.110.140.140.130.140.190.160.16
Megakaryocyte 0.110.110.11 0.290.130.140.150.160.180.18
Granulocyte 0.130.130.140.29 0.180.190.190.240.270.29
Erythroid−cells 0.120.120.140.130.18 0.210.20.190.250.2
LMPs 0.120.130.130.140.190.21 0.210.20.260.2
GPs 0.130.120.140.150.190.20.21 0.20.270.21
B−cells 0.170.190.190.160.240.190.20.2 0.260.28
MEMPs 0.120.130.160.180.270.250.260.270.26 0.33
HSC−MPPs 0.130.130.160.180.290.20.20.210.280.33
setyconoM
sCDp sllec−B
etycolunarG
sPG
sllec−diorhtyrE etycoyrakageM
sllec−tsaM
sPML sPMEM
sPPM−CSH
Monocytes 0.060.070.060.060.080.050.060.050.050.06
pDCs 0.06 0.060.050.060.080.070.080.060.050.06
B−cells 0.070.06 0.060.070.10.060.050.060.070.07
Granulocyte 0.060.050.06 0.150.080.070.080.060.060.06
GPs 0.060.060.070.15 0.110.110.120.070.080.08
Erythroid−cells 0.080.080.10.080.11 0.10.110.070.080.08
Megakaryocyte 0.050.070.060.070.110.1 0.180.10.090.1
Mast−cells 0.060.080.050.080.120.110.18 0.080.070.08
LMPs 0.050.060.060.060.070.070.10.08 0.090.08
MEMPs 0.050.050.070.060.080.080.090.070.09 0.09
HSC−MPPs 0.060.060.070.060.080.080.10.080.080.09
setyconoM
sllec−B sCDp
etycolunarG
sPG sPML sPMEM
sPPM−CSH sllec−tsaM
etycoyrakageM sllec−diorhtyrE
Monocytes 0.870.730.770.730.760.720.730.730.710.71
B−cells 0.87 0.740.770.730.780.740.740.720.720.71
pDCs 0.730.74 0.810.80.770.780.770.750.80.74
Granulocyte 0.770.770.81 0.810.780.780.780.790.790.78
GPs 0.730.730.80.81 0.780.770.790.740.750.74
LMPs 0.760.780.770.780.78 0.790.790.730.760.75
MEMPs 0.720.740.780.780.770.79 0.80.740.770.77
HSC−MPPs 0.730.740.770.780.790.790.8 0.720.740.74
Mast−cells 0.730.720.750.790.740.730.740.72 0.780.76
Megakaryocyte 0.710.720.80.790.750.760.770.740.78 0.78
Erythroid−cells 0.710.710.740.780.740.750.770.740.760.78
sllec−B
setyconoM
sPG sPMEM
etycolunarG
sllec−diorhtyrE
sCDp
sllec−tsaM sPPM−CSH
sPML
etycoyrakageM
Article https://doi.org/10.1038/s41467-023-38637-9
HSC-MPP
LMP GP MEMP
Mono pDC B Granulocyte Ery Mast Megakaryocyte
B−cells
Monocytes
GPs
MEMPs
Granulocyte
Erythroid−cells
pDCs
Mast−cells
HSC−MPPs
LMPs
Megakaryocyte
HSC-MPP HSC-MPP HSC-MPP Fscore HSC-MPP
0.2 0.4 0.6 0.8
MEMP
MEMP
Megakaryocyte B LMP MEMP Ery GP LMP GP MEMP HSC-MPP GP Granulocyte
Ery
pDC Mono Granulocyte Mast GP LMP Meg B akaryocyt G e ranulocyte Mono pDC B Ery MastMegakaryocyte LMP GP MEMP LMP Mast Ery
Granulocyte
Mono MegakaryocytepDC
Mono
Mast pDC Mono pDC B Ery MastMegakaryocyte
Granulocyte B
NatureCommunications|( 2023)1 4:3064 12
Article https://doi.org/10.1038/s41467-023-38637-9
Fig.7|Inferenceofcelltype-specificnetworksforhumanfetalhematopoiesis and0.75quantile(Q3).Theupperwhiskeristheminimumofthemaximumvalue
data.aCelllineagestructurelinkingthecellclustersfromscRNA-seq.bBoxplots andQ +1.5*IQR,whereIQR=Q −Q.Thelowerwhiskeristhemaximumofthe
3 3 1
showingF-scoresofn=11cellclustersfortop1kedgesinpredictednetworksfrom minimumvalueandQ −1.5*IQR.c.Pairwisesimilarityofnetworksfromeachcell
1
scMTNI,scMTNI+Prior,INDEP,INDEP+Prior,andCellOraclecomparedtogold clusterusingF-scoreonthetop5kedges.Rowsandcolumnsorderedbyhier-
standarddatasets(top).FDR-correctedt-testtocomparetheF-scoreoftherow archicalclusteringusingF-scoreasthesimilaritymeasure.Reconstructedcell
algorithmtotheF-scoreofthecolumnalgorithm(bottom).Thetwo-sidedpaired lineagetreesareshownatthebottomofthepairwiseF-scoresimilaritymatrixand
t-testisconductedonF-scoresofn=11cellclustersforeverypairofalgorithms.A areconstructedusingtheMSTalgorithmontheF-scorematrix.HSC-MPPhema-
FDR<0.05wasconsideredsignificantlybetter.Thesign<or>specifieswhether topoieticstemcellsandmultipotentprogenitors,LMPlymphoid-myeloidpro-
therowalgorithm’sF-scoreswereworseorbetterthanthecolumnalgorithm’s genitors,MEMPMK-erythroid-mastprogenitorscombinedwithcyclingMEMPs,GP
F-scores.Thecolorscaleisspecifiedfor−log(FDR),withtheredcolorproportional granulocyticprogenitors,Eryerythroidcells,Monomonocyte,pDCplasmacytoid
tosignificance.Non-significanceiscoloredingray.Intheboxplot,thehorizontal dendriticcells.SourcedataareprovidedasaSourceDatafile.
middlelineofeachplotisthemedian.Theboundsoftheboxare0.25quantile(Q1)
othermethodsontheChIP-basedgoldstandards(Unibind,Cus_ChIP), PTMA, SNRPD1, SOX4 and EEF1A1, which have immune-related func-
buthadfewerpredictableTFsintheothergoldstandards.Thepoor tions. E18 which was specific to MEMPs was associated with KLF1,
performanceofCellOracleislikelyduetoitscompleterelianceonthe BRPF3 and PTMA. KLF1, which was found in the Buenrostro et al.
prior network for determining the structure of the final inferred datasetofadulthematopoiesisaswell45,isanessentialregulatorfor
network. We compared scMTNI+Prior and CellOracle on the coarse the erythroid lineage52,53, and was also found to be upregulated by
lineageandobservedsimilarsuperiorperformanceofscMTNI+Prior Ranzonietal.ascellstransitionedfromHSC/MPPtoMEMPs59.E16and
on both F-score and predictable TF metrics (Supplementary E14areedgeclusterssharedacrossallcelltypeswithEEF1A1,CDC20,
Fig.30A,B). HMGN2,NPM1,TOP2Aastopregulators.HMGN2belongstothehigh-
WenextexaminedthelineagestructurebyconstructinganMST mobilitygroupofproteins,whichwasidentifiedinouranalysisofthe
frompairwisedistancesoftheinferrednetworksandcompareditto Buenrostroetal.datasetaswell.Otherregulatorsimplicatedcellcycle
thegroundtruth(Fig.7c).Thesingle-tasklearningmethodsINDEPand (CDC20,TOP2A)ormoregeneralregulatorsofdevelopmentandpro-
INDEP+Priorinferrednetworkshadverylowoverlapforeachpairof liferation(NPM1).Cell-cycleandcell-fatedecisionsareinherentlytied
celllinesandtheresultinglineagetreewasdifferentfromtheground especiallyinprogenitorpopulationswherethecellfatedecisioncould
truth (Fig. 7c). In contrast, scMTNI and scMTNI+Prior were able to beinfluencedbythecellcyclestageofthecells64.Thek-meansanalysis
recoverthecelllineageexactlyastheinputcelllineagetree.CellOra- ofthecoarselineageexhibitedmuchmoresharednetworkstructure
cle, inferred more similarity across cell types and captured several comparedtothefinelineage,thoughitalsoidentifiededgesetsspe-
aspectsoftheoriginallineage(e.g.,MEMPderivingfromHSC-MPP), cifictoeachcoarsecelltype(E1:HSC,E3:GPs,E2:LMPs,Supplemen-
butdidnotcorrectlyrecoverseveralotheraspects(e.g.,LMPsandGPs tary Fig. 31). Several of the regulators identified in the fine lineage
derived from HSC, Granulocytes derived from GPs). For the coarse analysiswereseeninthecoarselineageanalysisshowingoverallcon-
lineage, scMTNI+Prior and CellOracle inferred the same tree, but sistencyofourresults.Forexample,E8whichhadedgessharedacross
placedLMPsandGPsunderMEMPsinsteadofunderHSCs(Supple- all cell types had EEF1A1, FOS, HMGN2,NPM1 as the top regulators.
mentary Fig. 30C). Taken together, these results show that Similarly,KLF1wasidentifiedintheMEMP-specificedgeclusterinthe
scMTNI+Prior’sframeworkofusinglineageinformationandaccessi- coarse (E4) and fine lineages (E17). The coarse lineage analysis also
bility results in inference of more accurate GRN structure and foundadditionalregulators.Forexample,E2,whichwasspecifictothe
dynamicsduringthedifferentiationprocessforknownbranchingcell LMPlineagewasassociatedwithIRF8,KLF3,BAG4,andMAP2K7.IRF8,
typetrajectories. whichwasidentifiedintheBuenrostroetal.datasetaswellplaysakey
roleininnateimmuneresponseandisanessentialfordevelopmentof
ExaminingdynamicsofGRNcomponentsforfetal thelymphoidlineageincludingBcells55,monocytesandpDCs65.
hematopoiesis OurLDAanalysisidentifiedtopicsrepresentingsubnetworksthat
Weappliedourk-meansandLDAanalysistoidentifyregulatorsasso- rewirefromtheHSCstatetodifferentlineages(Methods).Thetopic
ciated with edge rewiring and subnetwork changes for the fine geneswereenrichedinimmuneresponse(topic1),cell-cycle(topics2,
(Fig. 8a–c, Supplementary Figs. 25–28) and coarse hematopoiesis 3and5),cellularrespiration(topic4)andgeneralmetabolicprocesses
lineages (Fig. 8d, Supplementary Figs. 31–35). The k-means analysis (topic7,SupplementaryFig.29A).LDAtopic3identifiedaregulatory
identifiededgeclustersspanningmultiplecelltypesofthelineagetree subnetwork that gained connections in B cells for regulators like
(e.g.,E16,E15,E21,E14,E13,E19,E7)aswellasindividuallineages(E4: FOXP4andPPR2R5B(Fig.8c,SupplementaryFig.26)andwasenriched
B cells, E3: Granulocytes, E5: Erythrocytes, E9: Mast cells, E2: HSC- forcellcycleprocesses(SupplementaryFig.29A).Incontrast,topic1
MPPs,E18:MEMPs)(Fig.8a).Weexaminedtheregulatorsassociated representedanoppositepatternofgraduallossofedgesconnectedto
with the edge clusters shared across multiple cell types and found FOSfromHSC-MPPtodownstreamlineages(SupplementaryFig.25).
HNRNPK and PTMA to be frequently associated with these clusters FOSwasfoundtobeupregulatedinRanzonietal.intheHSCs/MPPs
(Fig.8b).HNRNPKhasanumberofregulatoryfunctionsacrossdiverse population59.OthertopicsexhibitedconservedhubslikePTMA(topic
cell types including asa regulator of hematopoiesis60. PTMA, which 4,SupplementaryFig.26),HNRNPK(topic8,SupplementaryFig.27)),
standsforprothymosinalphaisnotwellunderstoodforitsfunction andNPM1(topic5,SupplementaryFig.26)acrossmultiplelineagesand
butisimplicatedingrowthandsurvivalofcellsofhematopoieticori- severalcellcycleregulatorssuchasTOP2AandCDC20(topic2,Fig.8c,
gin, and required for the filament-inducing activity of macrophage Supplementary Fig. 25). On the coarse lineage, the LDA analysis
lysate61,whichwouldbeconsistentwithitsexpressioninthehema- revealedmorehubsinHSC-MPPswhichwerelostwhendifferentiating
topoietic lineage62. E17 had edges common to the Myeloid lineage to the other lineages (Fig. 8d, Supplementary Figs. 31–35). The
spanning HSC-MPPs, MEMPs, Mast-cells, Megakaryocytes and Ery- exceptionswereENO1(topic7,SupplementaryFig.34),HMGN2and
throid populations and had ENO1, NPM1, SNRPD1 in addition to NPM1(topic4,SupplementaryFigs.31,33)andPTMA(topic3,Sup-
HNRNPKandPTMAastopregulators(Fig.8b).ENO1encodesagly- plementaryFig.31),whichpersistedatalllineages.NPM1,whichwas
colyticenzymewhichisexpressedinseveralhumantissuesandhas foundbothinfineandcoarsetree,playsanimportantroleinhema-
been shown to be a regulatory enzyme with links to the MYC topoieticprogenitors,especiallyinearlymyeloiddifferentiation66.A
pathway63.E2hadedgesspecifictoHSC-MPPsandwasassociatedwith few regulators also gained connections in specific lineages, for
NatureCommunications|( 2023)1 4:3064 13
c
topic: 1 topic: 2 topic: 3 topic: 4 topic: 5
topic: 6 topic: 7 topic: 8 topic: 9 topic: 10
example, LGALS1 (topic 3),JAG1(topic 7), CDK1 (topic4) had more andourresultsfromBuenrostroetal.(SupplementaryFig.33).Taken
edgesintheLMPlineageandPLEKintheMEMPlineage(Supplemen- together,thek-meansandLDAanalysisidentifiedseveralcomponents
taryFig.31).BothLGALS167andJAG168havebeenshowntobeinvolved offetalhematopoiesisGRNsthatchangedascellsdifferentiatedfrom
inhematopoiesis,however,thespecificrolesinthisprocessisnotas HSC-MPP to differentiated cell types. While many of the regulators
well-characterized.Intopic5,weobservedthepersistenceofanIRF8- havewell-characterizedrolesinhematopoiesis,severalarepreviously
specificnetworkfromtheHSCs/MPPstoLMPspopulations,whichwas uncharacterized that can be followed up with targeted functional
lostinMEMPs/GPslineageandisconsistentwithourk-meansanalysis studies.
sPPM−CSH sPML setyconoM sCDp sllec−B sPG setycolunarG sPMEM sllec−tsaM setycoyrakageM sllec−diorhtyrE sPPM−CSH sPML setyconoM sCDp sllec−B sPG setycolunarG sPMEM sllec−tsaM setycoyrakageM sllec−diorhtyrE sPPM−CSH sPML setyconoM sCDp sllec−B sPG setycolunarG sPMEM sllec−tsaM setycoyrakageM sllec−diorhtyrE sPPM−CSH sPML setyconoM sCDp sllec−B sPG setycolunarG sPMEM sllec−tsaM setycoyrakageM sllec−diorhtyrE sPPM−CSH sPML setyconoM sCDp sllec−B sPG setycolunarG sPMEM sllec−tsaM setycoyrakageM sllec−diorhtyrE
a kmeans clustering b Top regulators for edge clusters
63
76
185
90
42
395
49
73
61
46
136
88
730
599
740
445
676
640
648
406
552
672
score number of edges Degree
0.000.250.500.75
200400600 0 25 50 75 100
DU F S O P S 1 S H N C T M R O D G P P C D N 2 2 A 1 2 0 P N A C K U T U D M C S C R C D A Y F K A P K T 1 B 5 9 1 1 1 P P O S P O 1 O L P L 0 R L T R 0 2 R M A 2 J 2 A 2 4 L I M N C P M M 7 1
ZNF148 CS A R C P P 2 5 S T O C X F 4 4
B K R L IP F 1 6 D Z L P N L G T F M T A 4 O G P 90 5 4 1 PP Z Z P F P N N R O 2 E F F D R X T 2 2 M 5 V P 2 1 B 5 5 1 5 4 SLC P P O 2 O A L E U C 4 R D 2 F R 2 F F L G C 1 2 1 PT ID K7 1
ZN M E F I C R B 4 M F F 67 8 1 4 E N D E F E U B A F N S T 1 T O C P A F 1 3 1 1 3 HNRNPK LG E F A G U L R S T4 1 1 CC P N L B K 1 1
MA E M AF L3 1 C C H D EK K5 2 PSTP J I R P K 2 CREBBP
Z P X N E B F S R P 3 K 3 0 1 I M R A E E P K I X R T 2 L O K V F F 7 1 4 5 4 MEF2C ZN C F W F 1 T L 3 1 1 3 SO TT X K 4
Degree
d 0 10 20 30 40
egdE
#
0.910.920.920.720.820.910.750.980.88 0.8 0.95
0.990.210.080.02 0.1 0.720.930.980.070.160.33
0.970.060.010.01 0 0.32 0 0.96 0 0.1 0.15
0.920.130.080.020.020.160.180.930.920.220.35
0.990.780.760.760.870.770.670.880.620.460.02
0 0.02 0 0.01 0 0.050.010.880.060.040.03
0.96 0.8 0.220.110.680.680.020.88 0.4 0.130.48
0.980.110.12 0.1 0.970.130.090.480.11 0.1 0.08
0.05 0.6 0.7 0.8 0.830.410.210.350.520.350.44
0 0.240.040.090.020.14 0 0.210.220.770.76
0.090.080.090.080.040.860.880.090.090.070.08
0.120.810.310.840.020.240.210.040.010.110.09
0 0.010.020.030.95 0 0.010.010.020.010.02
0 0 0.010.01 0 0 0.850.010.010.01 0
0 0.020.870.01 0 0.010.02 0 0.010.010.01
0 0.010.010.01 0 0.81 0 0 0 0.01 0
0 0 0 0 0 0 0 0 0 0.74 0
0 0 0 0 0 0.01 0 0 0 0 0.78
0 0.010.010.01 0 0 0.01 0 0.830.010.01
0.950.050.010.01 0 0.060.02 0 0.020.010.01
0 0.73 0 0 0 0 0 0 0 0 0
0 0 0 0.79 0 0 0 0 0 0.010.01
sPPM−CSH
sPML
setyconoM
sCDp sllec−B sPG
setycolunarG
sPMEM
sllec−tsaM setycoyrakageM sllec−diorhtyrE
E16
E15
E21
E17
E14
E18
E13
E19
E7
E20
E6
E22
E4
E3
E11
E10
E8
E5
E9
E2
E12
E1
5PCA 1TKA 2TKA BKRUA K2PMB MGPB 1PIRB 3FPRB KTB 1BNCC 02CDC APB24CDC 1KDC 1LFC 1A1FEE 1RGE 4KLE 1ONE GRE SOF 1OXOF 4PXOF 2H2FTG 4C3FTG 2NGMH KPNRNH 1DI 4FRI 8FRI 1FLK 6FLK 7FLK 3LTBM3L 4OML 3LMAM 4MCM 7MCM C2FEM 5TAFN 1CTAFN 2EMN 1MPN 1NKP 2J2RLOP NAPP AMTP 1GTTP KABR LIKS GR4A2CLS 1DPRNS 4XOS 1PS 2PS 3PS 4PS B1FAT 02FCT 4FCT 1PDFT 1I1BFGT A2POT 5MIRT 2BAX 1XBY 841FNZ 112FNZ 032FNZ 182FNZ 03FNZ 663FNZ 764FNZ A585FNZ
E16
E15
E21
E17
E14
E18
E13
E19
E7
E20
E6
E22
E4
E3
E11
E10
E8
E5
E9
E2
E12
E1
Degree 25 50 75 100
topic: 1 topic: 2 topic: 3 topic: 4 topic: 5
FOS AHR BANF1 AURKB DDX5
FOSB HIST1H1B CFL1 BRCA1 HMGN1
ELF2 HIST1H2BG EDF1 CDC20 IRF8
FOSL1 HNRNPK HIST1H1D CDC25C PATZ1
HESX1 MEIS1 HIST1H1E CDCA5 E2F1
KLF6 MYC LGALS1 CDK1 FOXO1
PLCG1 TFCP2 PHPT1 CDKN3 GFI1B
PLEK CREB1 POLR2I DLGAP5 SP2
CSF1R ERG PTMA HELLS SP3
HINFP ETV3 S100A4 HMGN2 TCF3
topic: 6 topic: 7 topic: 8 topic: 9 topic: 10
CIITA ENO1 BCL11A FOXP1 ZNF76
HOXA9 HSP90B1 CDK6 KLF4 BCL3
RFX5 NR2F6 IRF9 SP1 HOXB2
KLF7 XBP1 SPI1 SP4 ACP5
SMAD9 ATF3 TCF12 EEF1A1 ASCL2
ATF4 EAF1 TCF4 SNAI3 BACH1
E2F5 ESRRG JUNB HCFC1 EPAS1
FOSL2 HOXB4 MNDA KLF12 FOXJ1
FOXO3 JAG1 ZNF219 KLF8 NFE2L2
HLF JUN BACH2 MECOM PURA
Degree 10 20 30 40
CSH sPMEM sPG sPML CSH sPMEM sPG sPML CSH sPMEM sPG sPML CSH sPMEM sPG sPML CSH sPMEM sPG sPML
Article https://doi.org/10.1038/s41467-023-38637-9
Top regulators per topic (fine lineage)
Degree 10 20 30 40
Top regulators per topic (coarse lineage)
Degree
0 10 20 30 40
NatureCommunications|( 2023)1 4:3064 14
Article https://doi.org/10.1038/s41467-023-38637-9
Fig.8|Networkrewiringduringhumanfetalhematopoiesis.ak-meansedge tree.Shownareonlyregulatorsthathaveatleast10targetsinanycellcluster.The
clustersofthetop1kedges(rows)across11cellclusters(columns).Theedge brighterandlargerthecircle,thegreaterarethenumberoftargetsforthereg-
confidencematrixwasclusteredinto21clusterstoidentifycommonanddivergent ulator.dTopregulatorsassociatedwitheachcellcluster’snetworkineachtopicfor
networks.Theredintensitycorrespondstotheaverageconfidenceofedgesinthat coarselineagetree.Shownareonlyregulatorsthathaveatleast10targetsinany
cluster.Shownalsoarethenumberofedgesintheedgecluster.bTop5regulators cellcluster.Thebrighterandlargerthecircle,thegreaterarethenumberoftargets
ofeachedgecluster.Thesizeandbrightnessofthecircleisproportionaltothe fortheregulator.Foreaseofinterpretationonlythetop10regulatorspertopicare
numberoftargets.Regulatorsmentionedintextareinred.cTopregulators shown.ThefulllistofregulatorspertopicareshowninSupplementaryFig.31.
associatedwitheachcellcluster’snetworkineachtopicforfine-grainedlineage SourcedataareprovidedasaSourceDatafile.
Discussion methodologicaldevelopmentforGRNinferencefromsinglecellomic
Single-celltechnologieshavetransformedourabilitytostudycellular datasets. Importantly, single-task learning infers very different net-
heterogeneity and cell-type specific gene regulation of known and works that makes it challenging to study transitions across the
novel cell populations. Defining gene regulatory networks from networks.
scRNA-seqdataofdevelopmentalsystemshasremainedchallenging OnceGRNsareinferredacrossmultiplecelltypes,thenextchal-
asmostexistingmethodshaveassumedastaticviewoftheGRNand lengeistoexaminewhichcomponentsoftheGRNschangealongthe
donotleverageaccessibilitytoinformtheGRNstructure.Toaddress lineage. We developed two complementary techniques to study
this need, we developed single-cell Multi-Task Network Inference dynamics.Ourk-meansedgeclusteringmethodwasabletofindreg-
(scMTNI),a probabilistic graphical model-based approachthat uses ulatoryconnectionsthatwereuniquetoeachcellcluster,whileour
multi-tasklearningtoinfercelltype-specificGRNsonacelllineagetree LDA topic model-based dynamic network analysis highlighted sub-
by integrating scRNA-seq and scATAC-seq data and model the networks that were activated or deactivated along the lineage. We
dynamicsoftheseregulatoryinteractionsonalineage.Amajorbenefit appliedourtoolstostudyGRNdynamicsinadultandfetalhemato-
of the scMTNI framework is its flexibility in incorporating different poieticcelldifferentiationandreprogrammingfrommouseembryo-
sources of accessibility information as well as the ability to model nicfibroblaststoembryonicstemcells.Wefoundthatthesesystems
dynamics on cell lineages of different topologies. The probabilistic exhibited different dynamics,with the reprogramming system exhi-
prior-based framework makes scMTNI more robust to noisy or biting more edges shared across populations compared to the
incomplete accessibility data and allows the incorporation of addi- adult hematopoietic system which identified most edges as cell
tionalregulatorssuchassignalingproteinsandTFswithnobinding cluster-specific.Inallthreesystems,ouranalysisidentifiedknownand
information.Guidedbythecelllineagestructure,scMTNI’sinferred previously uncharacterized regulators. For example, in the repro-
networksexhibitmeaningfulchangesalongthetrajectoryandidentify grammingsystem,wefoundthatcellsthatwereclosertotheendpoint
regulators and network components specific to cell populations pluripotent state already had an Esrrb-centered GRN component
transitioningtodifferentlineagepaths. active.Incontrast,cellsthatwereonanalternatetrajectoryexhibited
Multi-task learning is well-suited for the inference of cell type- persistenceoftheMEFregulatoryprogramincludingregulatorssuch
specificGRNs.However,akeyquestionishowtoimplementmulti-task as Aebp1. Between adult and fetal hematopoiesis we found several
learningforGRNinference.Anumberofmulti-tasklearningalgorithms shared regulators that were known lineage-specific regulators (e.g.,
weredevelopedforinferringGRNsandfunctionalnetworksfrombulk IRF8inthelymphoidlineage),butalsoidentifiedregulatorsuniqueto
transcriptomic data buthave notbeen systematicallycompared for eachsystemwhichcouldbefollowedupwithfuturevalidationstudies.
their effectiveness on single-cell transcriptomic data. Some approa- scMTNI currently assumes that the input lineage structure is
ches,suchasAMuSR28haveusedaflathierarchywhereallthetasksare accurate. However, lineage construction, especially from integrated
considered equally related. For heterogeneously related datasets, a scRNA-seq and scATAC-seq datasets is a challenging problem. One
hierarchy or a tree is well-suited to model the dependence across direction offuturework is toassumethe initial lineage structureis
datasets.Suchhierarchiescanbeimplementedasaphylogenetictree inaccurateandincorporatetherefinementofthelineagestructureas
withobserveddataatthetipsofthetreeasinGNAT26andMRTLE25,or partoftheGRNinferenceprocedure.Aseconddirectionofworkisto
asacell-lineagetreewithobservationsatallnodesinthetree.scMTNI modelmorefine-grainedtransitionswithineachcellpopulation,for
and MRTLE both use a tree-based structure prior, whereas AMuSR, exampleusingRNAvelocityorpseudotime69,whichwillcomplement
GNAT, and Ontogenet used a regularized regression parameter to thecoarse-graineddynamicsthatscMTNIcurrentlyhandles.Studies
implementmulti-tasklearning.scMTNIandMRTLEhavebetterper- from bulk RNA-seq data have shown that estimating hidden tran-
formanceinpredictingthegeneregulatoryrelationshipsthansingle- scriptionfactoractivity(TFA)70canfurtherimprovetheperformance
tasklearningalgorithms.TheperformanceofOntogenetisbetterthan of network inference. Thus, another direction of future work is to
thesingle-tasklearningalgorithmsLASSOandINDEPinatleasttwocell estimatehiddenTFAandincorporatethesetoimprovetheaccuracyof
types,andcomparabletoSCENIC.Aprominentfactorcontributingto the inferred networks. Finally, SCENIC generally outperforms the
thedifferenceintheperformanceofthealgorithmswaswhetherthe single-tasklearningalgorithmswhichdonotuseprior,whichislikely
models inferred a directed graph versus an undirected graph, with becauseof its regression-tree based model that captures non-linear
GNAT generally suffering likely due to this reason. Performance of dependenciesandislesspronetothesparsityofthedataset.While
GNATisworstamongmulti-tasklearningalgorithmsandcomparable scMTNI’sstabilityselectionframeworkcancapturesomenon-linear-
to the single-task learning algorithms. We speculate that the undir- ities,anotherdirectionoffutureworkistoextendscMTNItomodel
ectedgraphicalmodelslearnedbyGNATmightbeareasonthatthe morenon-lineardependencies.
performanceisnotasgoodasothermulti-tasklearningalgorithms.We Insummary,scMTNIisatooltoinfercelltype-specificregulatory
alsoexaminedtheperformanceofalgorithmsacrossdifferentpara- networksandtheirdynamicsonacelllineagewhichcombinesscRNA-
meter settings thatcontrol for sparsity as well as for sharing infor- seqandscATAC-seqdata.Assinglecellmulti-omicdatasetsbecome
mation. We found thatthe algorithms weregenerallyrobust to the increasinglyavailable,weexpectscMTNItobebroadlyapplicableto
settingofsharingandmoresensitivetotheextentofsparsity.How- predict GRNs and prioritize regulators associated with regulatory
ever, multi-task learning algorithms generally outperformed single- network dynamicsacrosscell types indiverse cell-fate specification
tasklearningalgorithmsindicatingthatthisisausefuldirectionfor processes.
NatureCommunications|( 2023)1 4:3064 15
