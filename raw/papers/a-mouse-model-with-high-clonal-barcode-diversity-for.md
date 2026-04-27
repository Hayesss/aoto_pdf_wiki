---
source_path: /mnt/c/Users/Administrator/Zotero/storage/LRE48JAD/Li 等 - 2023 - A mouse model with high clonal barcode diversity f.pdf
ingested: 2026-04-23
sha256: 4c3be93f0c9c4778
---

Resource
A mouse model with high clonal barcode diversity for
joint lineage, transcriptomic, and epigenomic
profiling in single cells
Graphical abstract Authors
LiLi,SarahBowling,SeanE.McGeary,...,
AllonM.Klein,Shou-WenWang,
FernandoD.Camargo
Correspondence
wangshouwen@westlake.edu.cn
(S.-W.W.),
fernando.camargo@childrens.harvard.
edu(F.D.C.)
In brief
DARLINisaninduciblebarcodingsystem
thatallowsforlineagetracingand
analysisacrossmousetissuesaswellas
combinedtranscriptionaland
epigenomicsingle-cellmeasurements.
Highlights
d DARLINgeneratesmassivebarcodediversityandlabels
(cid:1)70%ofprofiledcells
d DARLINidentifiesearlyfatebiasamongHSCsandtheir
transcriptomicsignatures
d DARLINrevealslow-levelHSCcirculationbetweenbone-
marrownichesinadulthood
d StrongclonalmemoryinDNAmethylationratherthanmRNA
orchromatinaccessibility
Lietal.,2023,Cell186,5183–5199
November9,2023ª2023PublishedbyElsevierInc.
ll
https://doi.org/10.1016/j.cell.2023.09.019
ll
Resource
A mouse model with high clonal barcode diversity
for joint lineage, transcriptomic, and epigenomic
profiling in single cells
LiLi,1,2SarahBowling,1,2SeanE.McGeary,3QiYu,1,2BiancaLemke,1,2KarelAlcedo,1,2YuemengJia,1,2XugengLiu,1,2
MarkFerreira,1,2AllonM.Klein,3Shou-WenWang,4,5,6,*andFernandoD.Camargo1,2,7,*
1StemCellProgram,BostonChildren’sHospital,Boston,MA,USA
2DepartmentofStemCellandRegenerativeBiology,HarvardUniversity,Cambridge,MA,USA
3DepartmentofSystemsBiology,BlavatnikInstitute,HarvardMedicalSchool,Boston,MA02115,USA
4WestlakeLaboratoryofLifeSciencesandBiomedicine,Hangzhou,Zhejiang,China
5SchoolofLifeSciences,WestlakeUniversity,Hangzhou,Zhejiang310024,China
6SchoolofScience,WestlakeUniversity,Hangzhou,Zhejiang310024,China
7Leadcontact
*Correspondence:wangshouwen@westlake.edu.cn(S.-W.W.),fernando.camargo@childrens.harvard.edu(F.D.C.)
https://doi.org/10.1016/j.cell.2023.09.019
SUMMARY
Cellular lineage histories and their molecular states encode fundamental principles of tissue development
and homeostasis. Current lineage-recording mouse models have insufficient barcode diversity and single-
cell lineage coverage for profiling tissues composed of millions of cells. Here, we developed DARLIN, an
inducible Cas9 barcoding mouse line that utilizes terminal deoxynucleotidyl transferase (TdT) and 30
CRISPRtargetsites.DARLINisinducible,generatesmassivelineagebarcodesacrosstissues,andenables
thedetectionofeditedbarcodesin(cid:1)70%ofprofiledsinglecells.UsingDARLIN,weexaminedfatebiaswithin
developinghematopoieticstemcells(HSCs)andrevealeduniquefeaturesofHSCmigration.Additionally,we
establishedaprotocolforjointtranscriptomicandepigenomicsingle-cellmeasurementswithDARLINand
foundthatcellularclonalmemoryisassociatedwithgenome-wideDNAmethylationratherthangeneexpres-
sion or chromatin accessibility. DARLIN will enable the high-resolution study of lineage relationships and
theirmolecularsignaturesindiversetissuesandphysiologicalcontexts.
INTRODUCTION measurementoflineageandtranscriptomicinformationinsingle
cells.12–14Inmice,theseapproacheshavebeenusedtostudy
Tracingcellularlineagehistoryinanimalshasbeenalong-stand- earlyembryonicdevelopment15,16andcancerprogression.17,18
ingeffort.Historically,labelingcellswithdistinguishableandher- Applyingthesametools,wedevelopedCas9/CARLIN,astable
itablemarkerssuchasdyeshasledtomajordiscoveriesinearly andgeneticallydefinedmouseline,whichenablesflexibleinduc-
development and stem cell differentiation.1–3 However, this tionatanypointtogeneratediverse,transcribedlineagebarco-
approachislimitedtotrackingonlysmallorpre-definedpopula- desacrosstissues.19
tionsofcells.RetrovirallybarcodingcellswithsyntheticDNAse- Theseandothersingle-celllineage-tracingapproacheshave
quences has enabled analysis of much larger populations,4,5 generallyfacedthreetechnicalchallenges:(1)lowlineage-bar-
althoughthisrequiresexvivomanipulationofcells.InvivoDNA codecaptureefficiencyinsingle-cellreadout;(2)lowefficiency
barcoding in mouse models has been achieved through the ofintroducinglineagebarcodes;and(3)contaminationfrombar-
use of randomly integrated transposons or recombinases that codehomoplasy,whereanidenticaleditingeventoccursinde-
create genetic diversity within a distinct locus, which revealed pendentlyintwodifferentcells.Asaresultofthesechallenges,
adrasticallydifferentpictureofhematopoiesisinvivo.6–10How- only (cid:1)10% of profiled cells from the Cas9/CARLIN mouse
ever,thesemousemodelseitherhavelimitedbarcodediversity contain detected lineage barcodes that likely label individual
ordonotallowsimultaneousinterrogationoflineageandstate clones.19Therefore,ahigher-performinglineage-tracingmouse
informationinsinglecells. lineisneededtoenablehigh-coveragesingle-celllineagetracing
The advent of CRISPR-Cas9 technology has created a new inadulttissueswithmillionsofcells.
avenueforlineagetracingwherediverseDNAmutationscanbe Single-celllineagetracingwithtranscriptomicmeasurements
created within a defined locus through genome editing.11 The hasbeensuccessfullyusedtoidentifyearlyfatebiasamongpro-
mutationaloutcomescanbetranscribed,therebyallowingjoint genitors and find novel regulators of cell-fate choices.20–22
Cell186,5183–5199,November9,2023ª2023PublishedbyElsevierInc. 5183
ll
Resource
However,epigenomicmodalitiessuchaschromatinaccessibility sitesandleadstohigherbarcodediversitycomparedwithCas9
andDNAmethylationareknowntoplayacrucialroleinregulating alone(Figure1F).38Totestwhetherasimilarstrategyalsoworks
geneexpressionandmaintainingcellidentities.23–25Epigenetic inanorganismalcontext,wehydrodynamicallyinjectedaplasmid
changes are known to foreshadow changes in gene expres- encodingeitheraCas9-TdTfusionproteinornativeCas9intothe
sion,26–29suggestingthattheearliesteventsforcell-fatechoice tailveinsofadultmicecarryingthetargetarray(Figure1A)and
are unlikely to be captured using gene expression alone. This analyzed the resulting allele editing in mouse livers with bulk
view is supported by a recent state-fate lineage-tracing study RNAsequencing(RNA-seq)after1week(Figure1G).Weobserved
showingthatthetranscriptomeofacellaloneisinsufficientto thatCas9-TdTexpressionresultedinfewerdeletionsbuttwicethe
predictitsfateoutcome.21Tofullyunderstandcell-fatechoices insertioneventsperallelethanCas9expression(Figures1H–1J).
and the maintenance of cell identities, single-cell approaches Aggregating insertion events from all alleles, we also observed
thatintegratelineage,transcriptomic,andepigenomicinforma- moreinsertednucleotidesperalleleuponCas9-TdTexpression
tionwillbenecessary.Severalrecentstudieshavereportedsin- (Figure 1K), with all four nucleotides well-represented in the in-
gle-cellmeasurementofeitherlineageandtranscriptomicinfor- serted sequences (Figure 1L). These data demonstrate that
mation, lineage and epigenomic information, or transcriptomic Cas9-TdTintroducesmoreinsertionsaswellasfewerdeletions
and epigenomic information.25,30–32Although some multi-omic thanCas9upontarget-arrayeditinginanadultmouse.
studies have inferred lineage information using endogenous
DNAmutations,33,34theinferredclonesarelow-resolution and DARLIN:AninducibleCas9-TdTmouselineforhigh-
cannotbeusedtostudylineagerelationshipsatdefineddevelop- capacitylineagetracing
mentaltimepoints.Indeed,amethodcapableofsimultaneously Having established that the Cas9-TdT expression leads to
profiling engineered lineage barcodes, the transcriptome, and improved lineage-barcode editing in an adult mouse, we set
theepigenomeinsinglecellshasnotbeenreported. outtogenerateaninduciblegermlinemousemodelthatutilizes
Here,wedevelopedanimprovedlineage-tracingmouseline Cas9-TdTfortarget-arrayediting.First,wecreatedamouseem-
(DARLIN)thathasanextremelylargelineage-barcodecapacity bryonic stem cell (mESC) line with a Dox-inducible Cas9-TdT
andhighlyefficientlineagerecoveryinsingle-cellassays,greatly construct also carrying a CRISPR target array and cognate
outperforming the Cas9/CARLIN model. Furthermore, we gRNAs (Figure S1A). We validated that editing of the array in
extendedexistingapproachestosimultaneouslymeasureDNA thismESClinewassensitivetoDoxexposure(FiguresS1A–S1D).
methylation,chromatinaccessibility,geneexpression,andline- We next engineered knockin mice with the tetO-Cas9-TdT
ageinformationinsinglecells.WeutilizedDARLINanditsasso- constructinsertedintotheCol1a1locus.39Thislinewascrossed
ciated analysis tools to address three distinct lineage-related withanimalscontainingthegRNAsandCol1a1targetarray(CA)
problemsinhematopoiesis. previously described in the Cas9/CARLIN system to generate
Col1a1tetO-Cas9-TdT/gRNA-Array:Rosa26M2-rtTA/+ mice for lineage
RESULTS barcoding. We will refer to this particular line as DARLIN-v0
(Cas9-TdT CARLIN version 0; Figure 2A). To benchmark
Cas9-TdTintroducesmoreinsertionsthanCas9upon DARLIN-v0 against the original Cas9/CARLIN mouse line, we
transientinductioninCARLINmice comparedthealleleeditingobservedinlargenumbersofgranu-
CRISPR-Cas9-based DNA editing is prone to deletions, which locytesfromeachmouselineafter1weekofDoxtreatment,fol-
limits the resulting barcode diversity. Reanalyzing the editing lowedbyanother3dayswithoutDox(Figure2B;n=7mouse
eventsobservedamongthe10tandemtargetsiteswithinthein- replicates for DARLIN-v0 and n = 5 for Cas9/CARLIN).
tegrated locus (referred to as target array) from the published ComparedwithCas9/CARLIN,editedallelesfromtheDARLIN-
Cas9/CARLINmousedataset19(Figure1A),wefoundthatdele- v0 mouse were enriched in rare alleles (Figures 2C and S1E).
tionsoccurredmorefrequentlythaninsertions(Figure1B),with Indeed,formousereplicateswithover10,000alleles,(cid:1)65%of
1.5 insertion events and 2.5 deletion events per allele on alleleswereobservedonlyonce(referredtoassingletonalleles)
average. An allele generated by Cas9editing had a median of for DARLIN-v0, compared with (cid:1)30% for Cas9/CARLIN (Fig-
163bpdeletedoutofits270-bpuneditedtargetarray,implying ure 2D). For the same number of edited cells (i.e., UMIs), the
the deletion of 6 out of 10 tandem target sites (Figure 1C). By DARLIN-v0 mice exhibited 2.3-fold as many alleles as Cas9/
contrast,anallelehasonlyamedianof2bpinserted(Figure1D). CARLIN(FigureS1F).Sincetheutilityofanalleleforclonallabel-
These large deletion events can lead to information loss and ingdependsonitsoccurrencefrequency,weusedthemetric2H,
generate degenerate alleles. Consistent with this, common al- where H is the Shannon entropy of the normalized allele fre-
leles wereenrichedwithdeletion-only alleles, whereas rareal- quency across edited cells, to report the barcode diversity of
leles,whicharerequiredforconfidentassignmentofbonafide an ensemble of alleles.19 The Shannon allele diversity of
clones,preferentiallyresultedfromDNAinsertions(Figure1E). DARLIN-v0 alleles was (cid:1)5 times that of Cas9/CARLIN alleles
Wereasonedthatincreasingthefrequencyofinsertionscould (Figure2E).Consistent withthis,weobservedthatDARLIN-v0
greatlyincreasethegenerationofrarealleles,therebyincreasing not only had much fewer large-scale (>180 bp) deletions that
overallallelediversityandbarcodingcapacity.Terminaldeoxynu- resultindegeneratealleles(Figure2F)butalsomore(FigureS1G)
cleotidyltransferase(TdT)isatemplate-independentDNApoly- andlarger(Figure2G)insertions.Consideringallmutationevents
merasethatcaninsertrandomnucleotidesatbothoverhangand acrossalleles,eachinsertioninCas9/CARLINwasonaverage
blunt 30 ends.35–37 A recent study in cell lines showed that co- accompaniedbythreedeletions,whereasinDARLIN-v0,each
expressionofCas9andTdTgeneratesmoreinsertionsinthetarget insertion was accompanied by fewer than one deletion
5184 Cell186,5183–5199,November9,2023
ll
Resource
A
B C D E
F G H
I J K L
Figure1. AdvantageofCas9-TdToverCas9forgeneratinglineagebarcodes
(A)SchematicofCARLINlineage-recordingsystem(left),thetargetarray(middle),andeditingpatterns(right).
(B–E)ReanalysisofpublishedbulkgranulocyteCas9/CARLINdata.19
(B–D)Distributionofinsertionordeletionevents(B),totaldeletionlength(C),ortotalinsertionlength(D)pereditedallele.
(E)HistogramofalleleUMIcountsamongeditedalleles,whicheitheronlycontaindeletionsorhaveinsertionsandpossiblydeletions.UMI,uniquemolecular
identifier.
(F)Target-arrayeditingbyaCas9-TdTfusionprotein.
(G)Experimentalschemetocomparethetarget-arrayeditingfromCas9orCas9-TdTprotein.
(H)Boxplotoftheinsertion-to-deletioneventratioamongalleditedallelesfromCas9orCas9-TdTmice.Horizontallinesofeachboxrepresenttheminimum,
25th-,50th-,75th-percentiles,andmaximumvalues.
(I–K)Distributionofdeletion(I)orinsertion(J)eventsperalleleandtotalinsertionlengthperallele(K).
(L)InsertionfrequencyofallfourDNAnucleotidesineditedallelesgeneratedbyCas9-TdT.
(Figure2H).Therewerealsomoreinsertionsacrossthe10target target array in intestine, kidney, lung, liver, spleen, and gonad
sitesinDARLIN-v0mice(Figures2IandS1J),withallfournucle- viabulkRNA-seq(Figure2B).Theeditingefficiencywas>90%
otide identities well-represented within these inserted se- acrossthesetissuesascomparedwith30%–50%asreported
quences(FigureS1H).Thesedatademonstratethatcompared forCas9/CARLIN,19withonly(cid:1)4%backgroundeditingwithout
withCas9/CARLIN,theDARLIN-v0mouselineachievesalarger Dox induction (Figure 2J). The singleton-allele fraction was
fractionofrareallelesandgreaterbarcodediversityduetomore (cid:1)70%andwascomparableacrosstissuesoverabroadrange
insertionsandfewerlarge-scaledeletionsenabledbytheCas9- ofobservedallelenumbers(Figure2K).Poolingallelesfromall
TdTeditingsystem. tissuesamplesgaveasimilarsingleton-allelefraction,suggest-
ingthatindividualtissuesamplesweredominatedbydistinctal-
DARLIN-v0mouselineworksacrosstissuesandyields leles.Indeed,withinthesamemouse,only5%oflineagebarco-
>1millionalleles des were shared between the spleen, kidney, and intestine
WenextsoughttodemonstratethattheDARLIN-v0mousecan
((cid:1)30,000alleleseach),indicatingthatmostalleleswererelatively
work across tissues. We examined the editing patterns of the rare(Figure2L).
Cell186,5183–5199,November9,2023 5185
ll
Resource
A B
C D E F
G H I
J K L M
Figure2. CharacterizationofDARLIN-v0mice
(A)SchematicofDARLIN-v0system.Themutanttetracyclinereversetransactivator(M2-rtTA)expressedfromtheRosa26locusactivatesCas9-TdT-WPRE
expressionuponDoxadministration,leadingtoeditinginthetargetarray.WPRE:woodchuckhepatitisvirusposttranscriptionalregulatoryelement.
(B)Experimentalschemetocomparethetarget-arrayeditingbetweenDARLIN-v0andCas9/CARLIN.
(C–I)ComparisonoftheallelesgeneratedingranulocytesofCas9/CARLINwiththoseofDARLIN-v0.
(C)HistogramofUMIsperallele.
(D)Singleton-allelefractionasafunctionofobservedalleles.Eachpointrepresentsamousereplicateexceptfortherightmostpoints.
(E)ShannonallelediversityasafunctionoftotalUMIcounts(editedcells).
(FandG)Distributionoftotaldeletionlength(F)ortotalinsertionlength(G)pereditedallele.
(H)Boxplotoftheinsertion-to-deletionratio.
(I)RelativeUMIfractionofeditingpatternsacrosstentargetsites.
(J–L)Evaluationoftarget-arrayeditinginmultipletissuesfromDARLIN-v0.
(J)Observededitingefficiency.
(K)Singleton-allelefraction.
(L)Venndiagramofthealleleoverlapbetweenthreetissues.
(M)ObservedallelesasafunctionofeditedUMIsinDARLIN-v0.Thesepointscorrespondtomergedsamplesfromincreasingmousetissuesandtheirreplicates.
WenextestimatedtheclonalbarcodediversityoftheDARLIN- that the number of distinct alleles increased linearly with the
v0 model. By progressively pooling alleles from an increasing numberofeditedcells(goodnessoflinearfitr2=0.97;Figure2M),
number of mouse tissues and their replicates, we observed suggesting little-to-no saturation. Pooling alleles across all
5186 Cell186,5183–5199,November9,2023
ll
Resource
available data from the DARLIN-v0 mouse line, we observed each of these alleles, which we then used to identify alleles
5.23105uniqueallelesintotal(Figure2M),withasingletonfrac- that were statistically unlikely to be contaminated by barcode
tionof0.62(FigureS1K).Thelargefractionofsingletonsimplied homoplasy and therefore likely to have labeled real clones in
that many more unobserved alleles would be detected if we other experiments within this study. At a false discovery rate
samplemorecells.40Becauseoursamplingwasfarfromsatura- (FDR)of0.01forreliablecloneidentification,weestimatedthat
tion,wecouldnotdirectlycalculatethemaximumnumberofal- the alleles from our bank can label (cid:1)104 reliable clones when
leles that could be produced by the DARLIN-v0 mouse. We consideringonlyonetargetarrayand(cid:1)1012clonesifallthreear-
therefore inferred the number of total alleles using the Chao1 rays were to be used in combination (Figure S3D; STAR
estimator.40,41Thisapproachyieldedanestimateof1.33106 Methods). In practice, the barcoding capacity can be greatly
possible alleles, a value at least 30 times greater than the re- expandedbyincludingdenovoalleles(i.e.,allelesnotfoundin
ported 44,000 total alleles reported for Cas9/CARLIN.19 To ourrelativelysmallallelebank).Infact,(cid:1)80%ofallelesobserved
conclude, our DARLIN-v0 mouse line is suitable for lineage inourdatasetsfromactuallineage-tracingexperimentswerede
tracinginvarioustissuesandhasalargebarcodecapacity. novoalleles(FigureS5D).
DARLINmicecontainthreeindependenttargetarrays DARLINachievessuperiorsingle-celllineagecoverage
Tofurtherincreasetheclonalbarcodediversityfororganism-wide BecausetargetarraysinDARLINaretranscribed,onecansimul-
lineage tracing,wegeneratedtwoadditionalmouselines,each taneously profile the lineage barcodes and transcriptomes of
withadistincttargetarray:onewasintegratedattheTigrelocus singlecells.Transcriptomicinformationenablessystematicres-
(yieldingtheTigretarget-array[TA])andtheotherattheRosa26lo- olutionofcellstates,whichiscrucialforunderstandinglineage
cus(Rosa26target-array[RA]).BothTAandRAreusedthesame relationships in a heterogeneous population without conven-
10targetsequencesfromtheoriginalCA,suchthattheywould tionalsortingmarkers.However,onlycellswithlineagebarcodes
beeditedbytheexisting10tandemgRNAs,butindifferentorders thataredetected,edited,andrarewillbeusefulfordownstream
(FigureS2A).WegeneratedanadditionaltetO-Cas9-TdTknockin lineage analysis to avoid barcode homoplasy (Figure 3G). We
mouselinecarryinganindependentcopyofthe10gRNAsusedin thereforesystematicallyevaluatedthecharacteristicsofsingle-
theoriginalCARLINconstruct,withthegoalofenhancingbarcode celllineagetracingintheDARLINmouseline.
editing.Bycrossinghomozygousmicehavingallthreetargetar- WelabeledDARLINmiceatE17.0andgeneratedasingle-cell
rayswith homozygousCol1a1tetO-Cas9-TdT-gRNA/tetO-Cas9-TdT-gRNA: lineage-tracing dataset of blood cell progenitors by sorting
Rosa26M2-rtTA/M2-rtTA mice, we obtained DARLIN-v1 mice (Fig- Lin(cid:3)cKit+cellsfromskullbonemarrow(Figure3H).Weobtained
ure 3A). Unless otherwise stated, all the data presented below 6,094cellsafterqualitycontrol(QC)(Figure3I)anddetectedal-
were generated from this DARLIN-v1 line, referred to hereafter lelesfromatleastonetargetlocusin81%ofcells,halfofwhich
simplyasDARLINmice. (overall 40%) contained at least two of three target loci (Fig-
ToevaluatetheeditingperformanceacrosstheCA,TA,and ure3J).ThetargetarrayattheTigrelocusexhibitedmoreeffi-
RA loci, we induced six adult DARLIN mice with Dox for cient capture due to its higher expression (Figures 3J and
1weekandanalyzedtheallelesfrombone-marrowgranulocytes S2H). Among these 6,094cells, 3,839 cells (63%) had at least
withbulkDNAsequencing(Figure3B).Wefoundthatthethree one rare allele (Figure 3K), and this fraction was comparable
target arrays achieved a similar editing efficiency (Figure 3C), acrossthesevenbloodcelltypesintheskull(Figure3L).Wepro-
comparable Shannon allele diversity (Figures 3D and S2B), as filedhematopoieticcellsfromfourothertissues(left-leg-derived
well as (cid:1)60% singleton-allele fraction (Figure 3E). We further bonemarrow,liver,lung,andspleen)insingle-cellassays(Fig-
confirmed that the different arrays had similar editing patterns ure3H)andalsoobserved(cid:1)60%ofcellswithatleastonerare
(Figures3FandS2C–S2E).Thesedatawereinagreementwith allele(Figure3M).
theaboveCAdatafromtheDARLIN-v0mouse(Figures2C–2I). Next, we systematically compared the single-cell lineage
WealsoobservedthatCA,TA,andRAhadsimilareditingdy- readoutbetweenDARLINandCas9/CARLIN19mouselines.On
namicsuponDoxinductioninembryos,andtheyweresimilarly average,wedetectedexpressionfromatleastonelineagelocus
saturatedat(cid:1)100%after24hofDoxtreatment(FiguresS2Fand in80%ofcellsderivedfromtheDARLINmouse,comparedwith
S2G).WeconcludethatinDARLIN,TAandRAperformcompa- (cid:1)50%fromCas9/CARLIN(Figure3N).Amongthedetectedline-
rably to the original Col1a1-based target array with respect to agebarcodes,(cid:1)80%werefurthereditedinDARLIN,compared
editingefficiencyandbarcodediversity. with(cid:1)35%inCas9/CARLIN,whichwasconsistentwithourob-
Wealsoconfirmedthattheeditingofthethreearrayswasin- servations ofediting efficiencyin mouse embryos(Figure S2J)
dependent of each other (Figure S2I). This implies that the and adult mice (Figure 3C). Finally, among the edited cells,
maximum theoretical number of barcodes in DARLIN could (cid:1)93% of cells from DARLIN mice had at least one rare allele,
reach(cid:1)1018,assumingeachlocuscangenerateatleast106al- whereasthisfractionwasonly55%forCas9/CARLINmice.Into-
leles. Notably, this barcode complexity far exceeds the total tal,DARLINmiceachieved(cid:1)60%ofcellspassingallthreefilters
numberofcells((cid:1)1010)inanadultmouse. (i.e.,hadanallelethatwasdetected,edited,andrare),compared
Toidentifyrareallelesthatcanuniquelylabelaclone,weper- with(cid:1)10%inCas9/CARLIN.OurassessmentofCas9/CARLIN
formed an experiment to measure intrinsic allele frequencies agreed with our previous assessment19 and was consistent
(Figure S3). We collected an allele bank with (cid:1)105 alleles for across two additional single-cell Cas9/CARLIN datasets
eachofthethreearrays,aggregatedacrossthreebulkDARLIN analyzed with our method (Figure 3N). Together, the above
mouse replicates. We inferred the generation probability r for data demonstrate that the DARLIN mouse line has superior
Cell186,5183–5199,November9,2023 5187
ll
Resource
A
C D E
F
B
G I J
H
K L M N
Figure3. CharacterizationofDARLINmice
(A)GeneticelementsoftheDARLINsystem.
(B)Experimentalschemetocomparethetarget-arrayeditinginthethreelociofDARLIN.
(C–F)Analysesofallelesgeneratedfromthethreeloci:editingefficiency(C),ShannonallelediversityasafunctionofdetectedUMIs(D),thesingleton-allele
fractionasafunctionofobservedalleles(E),andfrequenciesofeditingpatternsacrossthe10targetsites(F).
(G)Qualitycontrol(QC)pipelineforselectingsinglecellswithreliablelineagebarcodes.
(H)Single-celllineage-tracingexperimentaldesignwithDARLIN.
(I)UMAPembeddingofthetranscriptomesfortheskull-derivedLin(cid:3)cKit+cells.HSC,hematopoieticstemcell;LMPP,lymphoid-biasedmultipotentprogenitor;
MkP,megakaryocyteprogenitor;Ery,erythrocyte;Baso,basophil;Neu,neutrophil;Mon,monocyte.UMAP,uniformmanifoldapproximationandprojectionfor
dimensionreduction.
(J)Venndiagramshowingthenumberofcellsforwhicheachtypeoftargetarrayorcombinationofthesewasdetected.
(K)Cellnumberateachfilteringstepfortheskulldataset.
(LandM)Fractionofcellsforwhicharareallelewasdetectedfromatleastonetargetarray,eitherfordifferentcelltypesfromtheskull(L)orbloodcellsfrom
differenttissues(M).Eachbariscoloredaccordingtothepercentageofcellswithallelesatonlyasinglelocusormultipleloci(>1).
(N)FractionofcellsthatpassedeachQCstep(describedinG)betweenDARLINandCas9/CARLIN.TheDARLINdataarefrom(M),theCas9/CARLINdata
generatedinthisstudywerecollectedfromthehead,tail,andtrunkofamouseembryo,andthepublishedCas9/CARLINdata(collectedfrombonemarrow)
correspondtothoseofFigure6fromBowlingetal.19
5188 Cell186,5183–5199,November9,2023
ll
Resource
single-cell lineage coverage and a barcode diversity that ex- panel).Interestingly,CoSparalsopredictedthatmonocytesorig-
ceedsthenumberofcellsinanentireadultanimal. inatepredominantlyfromLMPPs(Figure4F,rightpanel),which
agreedwithourclonalcouplinganalysis(Figure4C).Importantly,
Mappingcell-fatechoicesamongunperturbedblood wefailedtoinfersuchearlyfatebiaswhendown-samplingour
progenitorsinvivo DARLINdatatomatchthefrequencyofcellswithdetected,edi-
We next demonstrated the utility of DARLIN to study cell-fate ted,andrareallelesinCas9/CARLINdata(FigureS4D).
choice during developmental hematopoiesis. Several studies Next, to identify the early transcriptomic signature of MkP-
have shown that hematopoietic stem and progenitor cells biased HSCs, we inferred the differentiation trajectory from
(HSPCs)canbedividedintosubpopulationswithfunctionalhet- HSCs to MkPs using the above CoSpar predictions, then split
erogeneity,10,21,22,42includingsubsetswithdistinctfatebiases. theMkP-biasedHSCsintotwopopulationsbasedontheirpseu-
However,itisunclearwhenthisfatebiasisestablishedduring dotime:earlyorlateMkPbias(Figure4G).ComparedwithHSCs
development and what are the molecular features of these withoutMkPbias,theearlyMkP-biasedHSCsexhibitedenriched
biasedHSPCs. expressionofgenesinvolvedinmaintaininglong-termHSCiden-
Were-analyzedoursingle-celllineage-tracingdatafromskull- tity(Mecom,Mllt3,andHlf),cell-cycleinhibition(Ifitm1,Txnip,and
derivedbonemarrowinducedatE17.0andcollectedinadult- Ifitm3), and megakaryopoiesis regulation (Tbxas1, Mpl, and
hood(Figure3H).Weidentifiedsixmajorcelltypesamongthe Meis1) (Figures 4H and 4I).22 We also identified many genes
6,094 profiled single cells: hematopoietic stem cells (HSCs), withoutanestablishedassociationwithMkPbiasinHSCs(Fig-
lymphoid-biasedmultipotentprogenitors(LMPPs),megakaryo- ure 4J), including the transcription factors Klf12, Sox5, Rora,
cyte progenitors (MkPs), erythrocytes, neutrophils, and mono- Pbx3,Pbx1,andGata2(FigureS4C).Takentogether,ourana-
cytes(Figures3I,4A,andS4A).Weintegratedinformationfrom lyses demonstrated that the DARLIN mouse line generates
the three target-array loci to assign a clone ID to each cell high-quality single-cell lineage-tracing data that resolves early
(STARMethods).Intotal,weidentified1,034distinctclones(Fig- fatebiaswithinHSCs,leadingtotheidentificationofgenesigna-
ure4B):someclonesoccupiedmultiplecellfates(Figure4C,left turesofMkP-biasedHSCsinunperturbedhematopoiesisinvivo.
panel),whereasothershadonlyoneobservedfateoutcome(Fig-
ure 4C, middle and right panel). With these data, we asked if Lineagerelationshipsofbloodcellsacrossbonesreveal
some HSPCs (HSCs and LMPPs) demonstrated differentiation HSCmigrationdynamicsoverdevelopmentand
biastowardspecificfates(Figure4A). adulthood
The clonal coupling scores across major cell types (i.e., a Next,weusedtheDARLINmouselinetosystematicallyevaluate
normalized correlation to measure how often two cell types clonal dynamics of the migration of hematopoietic progenitors
jointlyappearwithinthesameclone;STARMethods)suggested over development and adulthood (Figure 5A). Although it is
astronglineagecouplingbetweenMkPsandHSCs(p<0.001) appreciated thatHSCsmigratefromthefetallivertothebone
and between monocytes and LMPPs (p < 0.05) (Figures 4D marrowataroundthetimeofbirth,theclonalityofbone-marrow
and S4B). This agrees with earlier reports that a subset of colonizationandtheextentofHSPCcirculationduringontogeny
HSCscandirectlygenerateMkPs8,22,43–46andthatLMPPsare remainunclear.Similarly,theextentofmigrationanddifferentia-
primedtogeneratemonocytesratherthanneutrophils.21Inmu- tionintheadultbonemarrowremainspoorlyexplored.HSCcir-
rine hematopoiesis, definitive blood progenitors arise at E10.5 culation in adulthood was previously studied in mice by pa-
with the formation of Runx1-expressing clusters within the rabiosis.50–52Inthesestudies,Wrightetal.observedthatupto
aorta-gonad-mesonephros (AGM) region in the embryo.47 At 8% of HSCs migrated from one mouse to the other over
aroundE11.5,theseprogenitorsbegintomigratetothefetalliver 39 weeks50; however, a later study observed only 1%–2.5%
wheretheyfirstundergorapidexpansionbeforecolonizingthe migratory HSCs.51 Parabiosis experiments are highly invasive
bonemarrowataroundthetimeofbirth(i.e.,E19–E21).Consid- andleadtoinjuryandinflammation,whichmightinfluencethe
eringthatbarcodingwasinducedatE17.0,adevelopmentaltime behaviorofHSPCsinsuchstudies.Thehighbarcodingcapacity
pointwhenHSCsstillresideinthefetalliver,ourdatasuggest oftheDARLINmodelpresenteduswiththeuniqueopportunityto
thatHSCsatthistimealreadycarryfunctionalfeaturesthatwill address these questions at the level of individual clones in a
beevidentevenaftertheirmigrationtothebonemarrow.Thus, completelyphysiologicalcontext.
MkPbiasislikelytoariseearlierthanwhathasbeenpreviously We induced DARLIN mice at different developmental stages
reported.48Wefoundthat48%ofour187clonesthatbothcon- (adulthood, neonate, and E17.0). After 4 months, we dissected
tainedmultiplecellsandincludedatleastoneHSPChadasingle bonemarrowfromfourlocations(skull,spinalcord,leftleg[i.e.,fe-
clonal fate (Figure 4D), suggesting the possibility of early fate mur,tibia,andfibula],andrightleg)andusedfluorescence-acti-
bias. Inspecting those HSPCs that were clonally associated vated cell sorting (FACS) to sort long-term (LT) HSCs, MPPs,
withasinglematurefate,wefoundthatonlyMkP-biasedclones myeloidprogenitors(MyPs),andMkPsfromeachbonetoprofile
haddistincttranscriptomicsignatures(Figure4E).Wepreviously theirlineagebarcodesviabulkRNA-seq(Figure5B,upperpanel
developed CoSpar, a computational approach that utilizes and S5A). In a separate experiment, we also induced one
coherent and sparse lineage dynamics to robustly infer early DARLINmouseatE10.0,waited2months,andprofiledthelineage
cell-fatechoice.49WeappliedCoSpartoinferearlyfatepriming barcodesacrossmajorbloodcelltypessortedfromfourdifferent
by integrating transcriptomic and lineage information. Consis- bones (Figure 5B, lower panel). In these bulk RNA-seq experi-
tentwiththeaboveobservations,CoSparpredictedthatMkPs ments,acloneisasetofUMIssharingthesame(rare)lineagebar-
originate specifically from a subset of HSCs (Figure 4F, left code,whichmaycomefromdifferentbonesorcelltypes.
Cell186,5183–5199,November9,2023 5189
ll
Resource
A C D
B E
F
G H I
J
Figure4. Earlyfateprimingamonghematopoieticstemandprogenitorcells(HSPCs)
(A)UMAPembeddingofHSPCs(seealsoFigure3I).
(B)Clonalprofileofthenormalizedproportionofeachannotatedcelltype(column)withineachclone(rows).Onlythe187cloneslabelingHSPCsareshown.
(C)Selectedcloneswithdifferentfateoutcomes.pvaluesofclonalfatebiasareshownforthelattertwoclones.
(D) Heatmap of clonal coupling scores across major cell types (STAR Methods). Coupling scores that are statistically significant are indicated
(*p<0.05;***p<0.001).
(E)UMAPembeddingofHSPCs,highlightingcellsthatwereclonallyassociatedwithasinglematurecelltype.
(F)CoSpar-predictedprobabilityofeachHSPCtogenerateamaturecelltype.
(G)IdentificationofearlyMkP-biasedHSCswithCoSpar.
(H)VolcanoplotofdifferentiallyexpressedgeneswhencomparingearlyMkP-biasedHSCswithinferredHSCswithnoMkPbias.
(I)UMAPembeddingofHSPCsoverlaidwithexpressionofselectedgenes.
(J)HeatmapshowingtheexpressionofselectedgenesacrossdifferentHSPCclustersandMkP.Zscoreswerecalculatedpergenewithinthefourcell
populations.
5190 Cell186,5183–5199,November9,2023
ll
Resource
A B
C D E
F
G H I
J
K L M
Figure5. Lineagerelationshipsofbloodcellsacrossbones
(A)Schematicofmigrationofbloodprogenitorsacrossdevelopmentalstages.
(B)ExperimentaldesigntoinvestigateHSCmigrationdynamics.Legbonesincludethefemur,tibia,andfibula,whereasarmbonesincludethehumerus,ulna,and
radius.
(C–F)Clonalanalysisofbulklineage-tracingdatafromweek-8induction.
(C)Heatmapofclonalcouplingscoresbetweencelltypesfromeachbone.(D)Sharedclonefractionofeachcelltypeacrossbones(*p<0.05;**p<0.01;
***p<0.001;****p<10(cid:3)4,ttest).
(E)Sharedclonefractionforeachcelltypeoverdifferentthresholdsofminimumallelecomplexityforexcludinglow-complexityalleles.
(F)SharedclonefractionwhenperformingdifferentamountsofUMIdown-sampling.
(legendcontinuedonnextpage)
Cell186,5183–5199,November9,2023 5191
ll
Resource
First,wedeterminedtowhatextenthematopoieticprogenitors ably, we still observed predominantly local hematopoiesis
circulateacrossdifferentbonesduringadulthoodbyanalyzing acrossbones4monthslater(Figures5HandS5B).Toconfirm
mice induced at 2 months of age. The presence of a clone in thatwecoulddetectdelocalizedhematopoiesisinDARLIN,we
more than one bone indicates inter-bone migration, by which labeledembryosatE10.0,withthegoaloflabelingclonesthat
an individual HSC (or progenitor) divides and colonizes a would further expand in the fetal liver and colonize multiple
different bone-marrow niche. Calculating the clonal coupling bones.Inthiscontext,asexpected,theclonalcouplingscores
scoresbetweenallpairsofcelltypesfromallsortedpopulations, ofbloodcellswithinthesamebonewerecomparabletothose
whichaccountsforcloneidentitiesandtheirsizes,weobserved betweendifferentbones(Figure5I),andan(cid:1)80%sharedclone
that hematopoietic populations were strongly related in clonal fraction between bones was observed for different cell types
origin within each bone but not between bones (Figure 5C). (Figures 5J–5M). Thus, our observations suggest that HSCs
Thisisconsistentwiththeideathathematopoiesisispredomi- labeledinthelatefetalliverstages(E17.0)predominantlyseed
nantlymaintainedlocallywithineachboneintheadult,atleast onesinglebonemicroenvironmentandproliferateanddifferen-
within 4 months. Indeed, each of the clones resided predomi- tiatelocallyafterbirth.54Thesharedclonefractionsfrominduc-
nantlyinonebone,withonlyasmallfractionofcells(UMIs)de- tionatE17.0weresimilartothoseofinductionatneonatebutstill
tectedinotherbones(FigureS5B).Consideringthefractionof higherthanthoseofinductioninadulthoodforHSCs,MPPs,and
HSC-containing clones found in one bone (e.g., skull HSCs) MkPs(Figures5J–5L).WealsoobservedthatMyPshadcompa-
that are also detected in HSCs from other bones (irrespective rablesharedclonefractionswhenlabelingacrossthesestages
ofclonesize),weobservedthat(cid:1)5%ofHSC-containingclones (Figure5M).ThisdifferencewasconsistentwithMyPsundergo-
weresharedwithHSCsfromatleastoneotherbone(Figure5D). ingmoreactivecirculationintheadultstage.
Theoverlapfractionincreasedsignificantlyto(cid:1)14%forMPPs(t Importantly,whenweinducedbarcodinginadultmiceforonly
test,p<10(cid:3)3)andto(cid:1)40%forMyPs(p<10(cid:3)3)(Figure5D).To 3daysandthenimmediatelyprofiledalleles,weobservedonlya
exclude contamination fromcommon alleles, we onlyused de (cid:1)1% shared clone fraction across cell types (Figures 5J and
novo alleles ((cid:1)80% of all alleles) from this experiment that S5C).Thissuggeststhattechnicalissues(i.e.,backgroundbar-
were not found in our pre-assembled allele bank with coding) have minimal effects on our observations. Additionally,
(cid:1)100,000alleles(FigureS5D).Accordingly,theinferredshared our results were corroborated by performing independent ana-
clone fraction was robust to (1) the mutational complexity of lyses using barcodes amplifiedfrom the CA and RA lociwithin
the alleles considered (Figure 5E), (2) down-sampling of UMIs thesamemice(FigureS5F).Inconclusion,thehighbarcodingca-
(Figure 5F), and (3) read cutoffs used for allele calling (Fig- pacityoftheDARLINmodelhasallowedustoobtainuniqueinsight
ureS5E).WealsoevaluatedtheextentofHSPCmigrationwith into the process of HSC migration during development and
age. Extending the chase period from 4 months to 1 year adulthood.
increased the observed shared clone fraction in HSCs from
(cid:1)5%to(cid:1)12%(Figure5J),suggestingthatHSPCmigrationoc- Camellia-seqsimultaneouslyprofileschromatin
cursatalowlevelandaccumulateswithage.Overall,ourdata accessibility,DNAmethylation,geneexpression,and
extendtheearlierfindingsofHSCcirculationbetweenbones50,51 lineageinformationinsinglecells
andprovidedefinitiveevidencethatthisprocessactivelyoccurs Integrating lineagetracingwithsingle-cell transcriptomic mea-
inanativephysiologicalcontext.Ourfindingsalsodemonstrate surementenablessystematicdissectionoffatebiasesforatran-
that less primitive populations like MPPs and MyPs circulate scriptomicallyheterogeneouspopulation.20–22,49Theepigenetic
moreactively. stateofacellalsoplaysacrucialroleinregulatingitsdynamics
Wenextstudiedthedynamicsofinter-bonemigrationinthe andfunction.23–25Anintegrativemeasurementoflineage,tran-
neonate.Itisunclearwhetherthemigrationofpost-birthHSCs scriptome,andepigenomeatthesingle-celllevelwouldenable
is more dynamic than those in the adult. Our results demon- a deeper understanding of how cell-fate choice is regulated
stratedthatat4monthsafterbirth,overalllocalhematopoiesis andhowcellidentityismaintainedacrossdifferentmodalities.
was still prevalent even when barcoding was induced in the Here, we developed a sequencing method to simultaneously
neonatalstage(Figure5G).Therewas,however,(cid:1)11%shared measurechromatinaccessibility,DNAmethylation,geneexpres-
clonefractionofHSCsbetweenthebonesstudied(Figure5J), sion,andlineageinformationinsinglecells(Camellia-seq)(Fig-
higher than the (cid:1)5% when induced in adulthood (p = 0.01). ure6A).Camellia-seqextendsscNMT-seq55–58byincorporating
Thus,ourresultssuggestanincreasedrateofinter-boneHSC lineagebarcodemeasurement.Briefly,asinglecellissplitinto
migration post birth in comparison to adulthood, consistent nuclearandcytoplasmicfractions.EndogenousmRNAsandex-
withanindirectstudybasedonliveimaging.53 pressedlineagebarcodetranscriptsarereverse-transcribedand
WealsoinducedatE17.0,astagewhenHSCsarepredomi- amplifiedfromthecytoplasmicfractionviaamodifiedSTRT-seq
nantlylocatedinthefetalliver.54Labelingatthisstagewilllikely protocol.59,60 The nuclear fraction is treated with GpC methyl-
result in effective barcoding right before birth, thereby mini- transferase,whichpreferentiallymethylatescytosinefromGpC
mizingtheeffectsofclonalexpansionbeforemigration.Remark- dinucleotides within regions of open chromatin.61 The
(G–I)Heatmapofclonalcouplingscoresbetweencelltypesacrossbonesformiceinducedattheneonatestage(G),E17.0(H),andE10.0(I).
(J–M)SharedclonefractionwithotherboneswheneditingwasinducedatdifferentdevelopmentalstagesforHSC(J),MPP(K),MkP(L),andMyP(M).When
present,‘‘(cid:3)1’’and‘‘(cid:3)2’’indicatedatafromreplicatemice.FortheE10.0,E17.0,neonate,andadultsamples,the(cid:3)Doxwaitingtimedurationswereasdescribed
in(B),andfortheadult(1year)samples,theywere1year,andthenegativecontrolsampleswereinducedinadulthoodandimmediatelyprofiled.
5192 Cell186,5183–5199,November9,2023
ll
Resource
A
B
C D E F
G
Figure6. Jointprofilingoflineage,geneexpression,chromatinaccessibility,andDNAmethylationwithCamellia-seq
(A)SchematicofCamellia-seq.
(B)Experimentalschemetoprofilebone-marrowHSCswithCamellia-seq.
(C)FractionofcellsthatpassedeachQCstepdescribedinFigure3G.
(D)BoxplotsshowingthenumberofobservedUMIs(left)orgenes(right)percellforthescRNA-seqdatageneratedwithCamellia-seq.ThecorrespondingUMIs
countpercellfromthe103Genomicsprotocol(Figure3I)isalsoshown.
(E)Theaveragechromatin-accessibilityorDNA-methylationprofileoverthetranscriptionstartsites(TSSs)of(cid:1)20,000differentgenesinacell.
(F)Boxplotshowingthegenomiccoverageacrosspromoters,genebodies,andCpGislands.EachGpCsitemustbecoveredbyR3reads,andCpGsitebyR
1read.
(G)PseudobulkchromatinaccessibilityandDNAmethylationsurroundingtheTSSofGata2andRunx1.ThebulkHSCATAC-seqpeaksfromLietal.54arealso
shown.ATAC-seq,assayfortransposase-accessiblechromatinwithsequencing.
endogenousDNAmethylation(methylatedcytosineinCpGdinu- decreaseswithanoscillatorypatterninthedirectionoftranscrip-
cleotides)andaccessiblechromatin(methylatedcytosineinGpC tioninitiation56(Figure6E).Furthermore,Camellia-seqachieved
dinucleotides) are then profiled with single-cell bisulfite a high genomic coverage: (cid:1)70% of promoters and (cid:1)90% of
sequencing.62 thegenebodieswererepresentedwithatleast3detectedGpC
WeprofiledHSCswithCamellia-seqtoevaluatethequalityof sitesand1CpGsite(Figure6F).Byaggregatingsingle-cellepige-
eachdatamodality.WeinducedlineagelabelingintheDARLIN nomic measurements into a pseudobulk dataset, we further
mouseatE10.0,whenHSCshavejustformedintheAGMregion, confirmed that the resulting chromatin-accessibility measure-
andextractedHSCs(Lin(cid:3)cKit+Sca1+CD48(cid:3))from9-month-old ments largely agreed with bulk ATAC-seq measurements of
adultbonemarrowtoperformCamellia-seq(Figure6B).Approx- HSCsfromapublisheddataset54(Figure6G;Pearsonr=0.63
imately50%ofthesinglecellsprofiledwithCamellia-seqhada fordisplayedregions)andanti-correlatedwithDNA-methylation
rarelineagebarcode(Figure6C).Weobservedamediantran- measurementsaroundpromotersinourdata(Figures6Eand6G).
scriptomicabundanceof(cid:1)100,000UMIsderivedfrom(cid:1)3,000
genespercell(Figure6D).Usingepigenomicmodalitiesfromsin- DNAmethylationmaintainsstrongclonalmemoryof
glecells,wereproducedthestereotypicpatternthatDNAmethyl- HSCsovertime
ationdecreaseswithin1kbofthetranscriptionstartingsite(TSS), WeutilizedCamellia-seqtogaininsightintothequestionofmo-
whereasthechromatinaccessibilityisgreatestneartheTSSand lecular memory in cell lineages: do cells from the same clonal
Cell186,5183–5199,November9,2023 5193
A B
Weak memory Strong clonal memory
Barcode cellsat E10
Wait 10 weeks Clone 1
Clone 2
UMAP-x
-------------------
F G H
-------------------- DNA methylation at selected genomic loci across clones ------------------------
I
lineage retain molecular signatures indicating that they arose of other clones when assessing their genome-wide molecular
from the same founder cell, despite potential changes in the statesinanunbiasedmanner,ascenarioforweakclonalmem-
external cellular environment among the daughter cells from ory,andtheoppositecaseisthatHSCsaremoresimilarwithin
thesameclone?Toexcludeconfoundingfactorslikecelldiffer- thesameclonethanacrossclones,ascenarioofstrongclonal
entiation,wefocusedonpurifiedHSCsandprofiledthemfrom memory(Figure7A,rightpanel).Wesoughttoaddressthisprob-
theadultbonemarrowwithCamellia-seq,followingDoxinduc- lemwithourdataandmeasuredcell-cellsimilaritywithinindivid-
tion at E10.0 (Figure 7A, left panel). One hypothesis is that ualcloneswithrespecttogeneexpression,chromatinaccessi-
HSCs within the same clone are indistinguishable from those bility,andDNAmethylation.
y-PAMU
with Camellia-seq
J
941_enolc 351_enolc 55_enolc 491_enolc 93_enolc 781_enolc 191_enolc 352_enolc 063_enolc 144_enolc
100
75
50
25
0
etar
.yhtem
AND
chr10:80997500-81001500
941_enolc 351_enolc 55_enolc 491_enolc 93_enolc 781_enolc 191_enolc 352_enolc 063_enolc 144_enolc
60
40
20
0
etar
.yhtem
AND
chr19:4988000-4994500
941_enolc 351_enolc 55_enolc 491_enolc 93_enolc 781_enolc 191_enolc 352_enolc 063_enolc 144_enolc
30
20
10
0
etar
.yhtem
AND
chr11:84518000-84531000
941_enolc 351_enolc 55_enolc 491_enolc 93_enolc 781_enolc 191_enolc 352_enolc 063_enolc 144_enolc
30
20
10
0
etar
.yhtem
AND
0.15
0.10
0.05
0.00
0.0 0.2 0.4 0.6 0.8 1.0
Intra-clone similarity score
chr11:84518000-84531000
ycneuqerf
dezilamroN
mRNA:p=0.048
0.150
Random
0.125
Observed
0.100
0.075
0.050
0.025
0.000
0.0 0.2 0.4 0.6 0.8 1.0
Intra-clone similarity score
ycneuqerf
dezilamroN
(Same experiment as Figure 6B)
----------------------------------------------------------------------------- Unsupervised UMAP embedding -----------------------------------------------------------------------
C Gene expression
nan
clone_149
clone_153
clone_55
clone_194
clone_39
clone_187
clone_191
clone_253
clone_360
clone_441
Chrom.acc.:p=0.343
0.20
Random
Observed 0.15
0.10
0.05
0.00
0.0 0.2 0.4 0.6 0.8 1.0
Intra-clone similarity score
ycneuqerf
dezilamroN
D Chromatin accessibility E DNA methylation
nan nnaann
clone_149 clone_149
clone_153 clone_153
clone_55 clone_55
clone_194 clone_194
clone_39 clone_39
clone_187 clone_187
clone_191 clone_191
clone_253 clone_253
clone_360 clone_360
clone_441 clone_441
DNAmet.:p=122...233 x33 EE1--000-1990
Random
Observed
sruoh
63
MGA syad
5.5
)1(
revil
lateF
syad
5.5
)2(
revil
lateF
skeew
01
)1(
worram
enoB
skeew
01
)2(
worram
enoB
1.5
1.0
0.5
0.0
:yromem
lanolC
).dnar.dts(/).dnar−.sbo(
30
20
10
0 1 2 3 6 8 12
Clone size (cell #)
met
acc
mRNA
tnuoc
enolC
ll
Resource
Figure7. TranscriptomicandepigenomicmemoryofHSCswithineachclone
(A)Experimentaldesign(left)andclassificationofclonalmemory(right).
(B)DistributionofclonesizesfromprofiledHSCs.
(C–E)UMAPembeddinggeneratedusingeithergene-expression(C),chromatin-accessibility(D),orDNA-methylation(E)datafromCamellia-seq.Cellsare
coloredbytheircloneidentities.
(F–H)Distributionofintra-clonesimilarityscoresfrom21observedand2131,000randomizedclones,calculatedusingeithergeneexpression(F),chromatin
accessibility(G),orDNAmethylation(H).pvaluesforeachmodalitywerecalculatedusingtheWilcoxonrank-sumtest.
(I)DNA-methylationlevelsatselectedgenomiclociacrossthetop10largestclones.
(J)Clonalmemoryscoreforeachmodalityacrossallmousesamplescollectedatdifferentdevelopmentalstages.
5194 Cell186,5183–5199,November9,2023
ll
Resource
Werestricted ouranalysistoclonescontainingR2cells(21 lineage coverage. Building on the current Cas9/CARLIN line-
clonesintotal)(Figure7B).Foreachofthethreemolecularmodal- age-tracingsystem,wefirstincorporatedTdTtoincreaseinser-
ities, we separately performed unsupervised dimensionality tion events in lineage barcodes and subsequently expanded
reduction and visualized the results via UMAP63 embedding DARLIN to include three independent lineage-recording loci.
(STARMethods),overlayingthecloneidentitiesontheembed- DARLIN can theoretically generate an estimated 1018 unique
ding.Forthe10largestclones,individualcellswithinthesame lineage barcodes, has (cid:1)90% barcode editing in the embryo,
clonewerelargelyscatteredacrosstheembeddingsgenerated and allows for(cid:1)80%barcode capture in traditional single-cell
using either gene expression or chromatin accessibility assays,leadingto(cid:1)60%ofprofiledcellshavingrarebarcodes
(Figures 7C and 7D), suggesting weak clonal memory with fordownstreamclonalanalysis.Thistranslatesintomoreuseful
respecttothesetwomodalities.Conversely,cellsbelongingto clones per sample, more cells per clone, and dramatically
thesameclonewerestronglyco-localizedwithintheembedding reducedexperimentalcostsforgeneratingadatasetwithsuffi-
generated from DNA methylation, suggesting stronger clonal cientclonalinformationtoaddressabiologicalquestion.Finally,
memory(Figure7E).Toquantifythestrengthofclonalmemory lineagebarcodinginDARLINcanbeinducedatanytimepoint
withrespecttoeachmodality,wecalculatedthesimilaritybe- and across a wide range of tissues, and DARLIN is a stable
tween any two cells using the Pearson correlation coefficient andgeneticallydefinedmouselinethatcanbesharedacrossa
andcomparedtheaveragesimilaritywithinthesameclonewith widebiologicalcommunity.
thosefromrandomizedcloneshavingthesameclonesizedistri- ThemassivebarcodediversitygeneratedbyDARLINnotonly
bution.Theseanalysesdemonstrated thatclonalmemorywith increasesthefractionofrareclonesinourdatabutalsoenables
respecttogeneexpressionwasbarelysignificant(p=0.049;Wil- thestudy oflargebiological systems,suchasadulttissue ho-
coxonrank-sumtest;Figure7F),andchromatinaccessibilitywas meostasis,inflammationresponse,andtissueinjuryandrepair.
notsignificant atall(p=0.34,Figure7G).However,theclonal Inmanyapplications,profilingallelesfromasingletarget-array
memorywithrespecttoDNAmethylationwashighlysignificant locus may already provide sufficient lineage information, with
(p = 1.2 3 10(cid:3)10; Figure 7H). Because most of the observed measurements from the remaining loci providing additional
clonesweresmall(i.e.,2–3cells),wealsoevaluatedeachclone robustness.
individually,findingthat19outofthe21testedcloneshadsignif- ThesuperiorperformanceinDARLINmiceislikelyduetothe
icantintra-clonesimilaritywithrespecttotheirDNAmethylation improvedgeneticdesign(Figure3A).Thehigherallelediversity,
(FigureS6A).Weidentified279genomicregionswithdifferential apart from having three target arrays, is mainly due to the in-
CpGmethylationamongclones(p<0.05;Benjamini-Hochberg- creaseofinsertionsfromTdTandmayalsobenefitfromfewer
adjustedone-wayANOVA;FigureS6B).Weprovidethreeexam- large-scale deletions that result in more degenerate alleles
plesinFigure7I,inwhicheachclonehasadifferentextentofDNA (Figures2F,S7A,andS7B;seeFiguresS7C–7Eforourproposed
methylationinselectedgenomicregions.These279differential modeltoexplainthisobservation).Theenhancededitingresults
methylatedregionswereneitherlocatedneardifferentiallyregu- fromboththeincreasedexpressionofCas-TdTduetoinclusion
latedgenes(FigureS6C)norpreferentiallyassociatedwithany ofthewoodchuckhepatitisvirusposttranscriptionalregulatory
gene-ontologyterms(FigureS6D),suggestingtheyrepresented element(WPRE)(FigureS7F)andalsoincreasedconversionof
randomgeneticlociratherthanfunctionallyrelevantregions. Cas9-inducedsingle-sitecleavageintoeditedalleleswithinser-
Wevalidatedourfindingsofclonalmemorywithadditionalbio- tions (rather than restoration of unedited sequences by direct
logicalsamplesviaCamellia-seq.TheseincludeHSCsthatwere blunt-end joining; Figures S7C–S7E). In practice, we have
labeled with lineage barcodes for 36 h (AGM HSCs), 5.5 days observed higher variability of editing efficiency when inducing
(fetalliverHSCs,tworeplicates)(FigureS6E),andanadditional adultmice(FiguresS1Iand3C)thanembryos(FiguresS2Jand
replicateofHSCstracedfor10weeks.Inourcombinedfivedata- S6I),suggestingtheneedtofurtherimprovetheprotocolforbar-
sets(mice),(cid:1)750cellssuccessfullypassedQC,comprisingato- codeinductioninadultmice.
tal of 63 clones with R2 cells. We confirmed that chromatin- Ahigheditingefficiencyalsohelpstomitigatetheimpactof
accessibility,DNA-methylation,andgeneexpressionmeasure- backgroundeditingwithoutDoxtreatment.Weobserved(cid:1)4%
mentscapturedstage-specificbiologicalsignals(FiguresS6F– background editing in an adult 8-week-old mouse (Figure 2J).
S6H),54andtheeditingefficiencieswerecloseto100%ineach Theseallelesresultingfrombackgroundeditingcouldbefurther
mousesample,with(cid:1)55%ofcellshavingvalidlineagecoverage editedatthetimeofDoxinductionduetothehigheditingeffi-
(Figures S6I and S6J). In these samples, we corroborated our ciency of DARLIN and split into different sub-alleles that label
findings that the memory scores were significant with respect clonesatthecorrecttiming(FiguresS7GandS7H).Combined
to DNA methylation for each of the HSC stages (Figure S6K) withourrare-allelefilteringstrategy,wehaveachieveda(cid:1)1%
andwereconsistentlyhigherthanthosefromtheothertwomo- falseinter-boneclonalsharing(backgroundnoise)inanegative
dalities (Figure 7J). Thus, we conclude that DNA methylation control experiment of adult HSC circulation (Figures 5J–5M
canretainthememoryofclonallyrelatedcellsmuchbetterthan andS5C).
eithergeneexpressionorchromatinaccessibility. In our applications, we demonstrated first that the DARLIN
mouse line enables the study of early fate bias within native
DISCUSSION HSCsathighresolution,leadingtotheidentificationofmultiple
new genes correlated with MkP bias in HSCs. In our second
Here,wedescribeDARLIN,alineage-tracingmouselinewitha application,westudiedthelineagerelationshipofhematopoietic
superior lineage barcoding capacity and enhanced single-cell cells across different bones. Our data demonstrate HSC
Cell186,5183–5199,November9,2023 5195
ll
Resource
inter-bonemigrationinacompletelyphysiologicalcontext,with B Mice
a(cid:1)5%sharedclonefractionofHSCsbetweendifferentbones B ESClines
accumulated over 4 months after induction in adulthood and d METHODDETAILS
higher fractions in aged animals. These observations support B Cas9–TdTFusionProteinDesign
theideathatHSCscontinuouslycirculateatlowlevelsinadult- B HydrodynamicTailVeinInjectionofCas9–TdTorCas9
hood.50Consideringthatwedissectedonly(cid:1)70%ofthemouse PlasmidintoCARLINMice
bonemarrow,welikelyunderestimatedtheextentofHSCmigra- B GenerationofCas9–TdT-relatedESCLines
tion.Ourdataalsospeaktotheprevalenceoflocalhematopoi- B GenerationofTigreandRosa26target-arrayESClines
esisevenwheninductionwasdoneeitherinthelatefetalliver B Generation of Tigre and Rosa26 target-array
or the neonate. Thus, our findings suggest limited migration mouselines
even after initial bone settlement. Barcoding models such as B GenerationofCas9–TdTMouseLines
DARLINrepresentanovelapproachtostudycellularmigration B AdministrationofDoxycyclineinMice
inthebonemarrow. B TissuePreparation
Inparallel,wehaveestablishedCamellia-seqtosimultaneously B FACS
profile lineage barcodes, chromatin accessibility, DNA methyl- B BulkLineageArrayLibraryPreparation
ation, and gene expression in single cells. Using DARLIN, we B Single-Cell Transcriptome and Lineage Array Library
showed that Camellia-seq generates high-quality data for each PreparationBasedon10XGenomics
ofthemodalities.ByfocusingonHSCsthatcanself-renew,we B Single-CellCamellia-seqLibraryPreparation
demonstratedthatgenome-wideDNA-methylationpatterns,but d QUANTIFICATIONANDSTATISTICALANALYSIS
not chromatin-accessibility or gene expression patterns, stably B Computationalanalysisoverview
propagate within individual clones over multiple cell divisions. B Allelepreprocessing
Finally,our(cid:1)750HSCsprofiledviaCamellia-seqcoverkeydevel- B Cloneidentification:theory
opmentalstagesofhematopoiesisandwillbeavaluableresource B Allelebankconstruction
to further understand hematopoiesis and, more generally, the B Homoplasyprobabilityinference
interplaybetweendifferentmodalitiesatthesingle-celllevel. B Cloneidentification:practice
Additionally, Camellia-seq is compatible with any lineage- B Clonalanalysis
tracing approach where the lineage barcodes are transcribed B Single-celltranscriptomicanalysis
asmRNA.31DARLINmicemayalsobeinducedwithDoxover B Chromatin-accessibilityandDNA-methylationanalysis
a series of time points to generate alleles with a hierarchical B Clonalmemoryanalysis
structure to obtain more hierarchical cellular lineage relation-
shipsoflargenumbersofcellsduringtissuedevelopmentorho- SUPPLEMENTALINFORMATION
meostasis. The lineage barcodes in DARLIN may also be
resolvedspatiallytounderstandspatiallineagedynamicsintis- Supplementalinformationcanbefoundonlineathttps://doi.org/10.1016/j.cell.
2023.09.019.
sues.Overall,theDARLINmouselineandCamellia-seqmethod
provideapowerfultoolforstudyingtherelationshipsandunder-
ACKNOWLEDGMENTS
lyingmolecularmechanismsofdiversebiologicalprocesses.
WearegratefultomembersofF.D.C.laboratory;theIDDRCGeneManipula-
Limitationsofthestudy tionCore(fundedbyNIHP50HD105351)forESCinjectionandchimeragen-
The target arrays in DARLIN still suffer from array deletions, eration;RonaldMathieu,MahnazPaktinat,RanjanMaskey,andBetelhemGe-
mechu from HSCI-BCH Flow Cytometry Research Lab for guidance and
whichmightlimittheiruseforlineagereconstructionacrossmul-
assistancewithFACS;AlejoRodriguez-Fraticelliforassistancewithdesigning
tiple cell divisions. This may be circumvented by generating
theCas9-TdTplasmid;SachinPatelforassistancewithdesigningtheclonal
sequentialmutationeventsalongtherecordingarraytoproduce memoryexperiment;Wei-ChienYuanforassistancewithhydrodynamicinjec-
hierarchicallylabeledclones.64Camellia-seqiscurrentlyalow- tionsandIPinjectionsinmice;FanZhouandChloe´Baronforassistancewith
throughput and costly plate-based method that requires deep mouseAGMdissectionandpre-HSCsorting;andFuchouTangandShuhui
genomic coverage for each cell. A cost-effective and high- Bianforassistancewithmulti-omicexperimentsandanalysis.WethankQiu
WufromtheKleinlabforconstructivecommentsonourmanuscript.F.D.C.
throughputmethodwouldbedesirable.
isfundedbygrantsR01HL128850,RC2DK131963,R01HL158192,theEd-
wardPEvansFoundation,andanAlexLemonadeCrazy8award.S.-W.W.ac-
STAR+METHODS
knowledgessupportfromtheWestlakeHigh-PerformanceComputingCenter.
S.B.acknowledgessupportfromEMBO(ALTF798-2018),theWellcomeTrust
Detailedmethodsareprovidedintheonlineversionofthispaper (grantnumber215920/Z/19/Z),andtheNIH(grantnumber1K99HL164969).
andincludethefollowing: IllustrativefiguresarecreatedwithBioRender.
d KEYRESOURCESTABLE AUTHORCONTRIBUTIONS
d RESOURCEAVAILABILITY
L.L., S.-W.W., and F.D.C. conceived the project, designed the study, and
B Leadcontact
analyzedthedata.L.L.,S.-W.W.,andF.D.C.wrotethemanuscriptwithhelp
B Materialsavailability
fromallotherauthors(especiallyS.E.M.).L.L.generatedCas9-TdT,Cas9-
B Dataandcodeavailability TdT-gRNAs and Cas9-TdT-gRNAs-TA mESCs, and Cas9-TdT, Cas9-TdT-
d EXPERIMENTALMODELANDSUBJECTDETAILS gRNAsmouselines.S.B.andB.L.producedTigre-andRosa26target-array
5196 Cell186,5183–5199,November9,2023
