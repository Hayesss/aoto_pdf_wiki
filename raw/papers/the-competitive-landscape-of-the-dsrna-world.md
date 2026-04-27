---
source_path: /mnt/c/Users/Administrator/Zotero/storage/BH62QGBG/Cottrell 等 - 2024 - The competitive landscape of the dsRNA world.pdf
ingested: 2026-04-23
sha256: 0c9110fb66a798f6
---

ll
Review
The competitive landscape of the dsRNA world
KyleA.Cottrell,1,3,*RyanJ.Andrews,2,3andBrendaL.Bass2,*
1DepartmentofBiochemistry,PurdueUniversity,WestLafayette,IN,USA
2DepartmentofBiochemistry,UniversityofUtah,SaltLakeCity,UT,USA
3Theseauthorscontributedequally
*Correspondence:kacottre@purdue.edu(K.A.C.),bbass@biochem.utah.edu(B.L.B.)
https://doi.org/10.1016/j.molcel.2023.11.033
SUMMARY
The ability to sense and respond to infection is essential for life. Viral infection produces double-stranded
RNAs (dsRNAs) that are sensed by proteins that recognize the structure of dsRNA. This structure-based
recognitionofviraldsRNAallowsdsRNAsensorstorecognizeinfectionbymanyviruses,butitcomesata
cost—the dsRNA sensors cannot always distinguish between ‘‘self’’ and ‘‘nonself’’ dsRNAs. ‘‘Self’’ RNAs
oftencontaindsRNAregions,andnotsurprisingly,mechanismshaveevolvedtopreventaberrantactivation
ofdsRNAsensorsby‘‘self’’RNA.Here,wereviewcurrentknowledgeaboutthelifeofendogenousdsRNAsin
mammals—the biosynthesis and processing of dsRNAs, the proteins they encounter, and their ultimate
degradation. We highlight mechanisms that evolved to prevent aberrant dsRNA sensor activation and the
importanceofcompetitionintheregulationofdsRNAsensorsandotherdsRNA-bindingproteins.
INTRODUCTION sequences,18 systematic searches for inosine-containing
RNAs,19,20 made more comprehensive by next generation
Duringthe1970s,scientistsrealizedviralinfectionofmammalian sequencing,21,22ledtothecurrentviewthatthemajorityofhu-
cells generated viral double-stranded RNA (dsRNA) that in- man protein-coding genesexpress dsRNA in theirnon-coding
hibited protein synthesis1,2 and triggered the interferon (IFN) regions,theirintrons,and30 UTRs.23Most,butnotall,ofthese
response.3TodayweknowthatallvirusesmakedsRNAusing expressed dsRNAs involve pairing between repetitive ele-
mechanismsinvolvingdefectiveinterferingparticles,panhandle ments,23andinprimates,thesearedominatedbyAluelements,
structures, and convergent transcription4,5 and that host re- ofwhichthereareoveramillioncopies,accountingforaround
sponses to viral infection are driven by binding of viral dsRNA 10% of our genome.24 Possibly related to the fact that many
todedicatedimmunesensors.6UponrecognizingdsRNA,these dsRNAs are synthesized from regions that historically were
‘‘dsRNAsensors’’activatediverseimmuneresponses:theRIG- thoughtofas‘‘junkDNA,’’weknowverylittleaboutthefateof
I-likereceptors(RLRs)andToll-likereceptor3(TLR3)instigate these dsRNAs. What happens to long dsRNAs after they are
the IFN response, protein kinase R (PKR) and oligoadenylate transcribed in the nucleus? If they make it to the cytoplasm,
synthases(OASs)inducegrowthinhibitionbydisruptingprotein howaretheydistinguishedfromthelongviraldsRNAsthatcan
synthesisanddegradingRNA,respectively,whereasotherpro- infectthecytoplasm?
teinsnucleateinflammasomestopromotecelldeathbypyropto- AdiscussionofthelifeofadsRNAisallabouttheproteinsit
sis.7 In this review, we discuss mammalian pathways, with a meetsalongtheway(Figure1).TheA-formhelicalstructureof
focus on endogenous dsRNA-binding proteins (dsRBPs) and dsRNAhasaverynarrowanddeepmajorgroove,makingitdiffi-
the dsRNA sensors, RLRs and PKR (Box 1). We capitalize on cult for proteins to make sequence-specific interactions, and,
recent results that emphasize the large role that competition indeed, dsRBPs typically bind any dsRNA they encounter.54
plays in regulating dsRNA-mediated pathways and highlight Thatsaid,mismatches,bulges,orloopsthatdisruptthecontig-
outstanding questions that can be framed in the context of a uous base-paired structure of dsRNA will widen the major
competitionmodel. groove,allowingforsequence-specificinteractions,andcertain
Evenintheearlystudiestherewerehintsthathostcellscon- sequence-specific minor groove interactions allow a dsRBP
taineddsRNAevenwithoutinfection,3butitwouldbedecades to bind in a certain register.55 Regardless of the binding
beforetheactualDNAsequencesthatencodedandexpressed preferences that might occur from structural disruptions, or
dsRNAwereidentified.Allanimalcellsanalyzedsofarexpress sequence-specific minor groove interactions, dsRBPs will still
dsRNA,16,17 and in most cases these dsRNAs were identified bindanydsRNAtheyencounter,beitcellularorviral.Yet,under
because they contained inosine from in vivo RNA editing by healthyconditions,cellscandistinguishthegoodfromthebad.
adenosinedeaminasesthatactonRNAorADARs(Box2).These Thebiologicalpathwaysthathavearisentoallowforself-versus
enzymes convert adenosine to inosine (A-to-I) within dsRNA, non-self-recognitionofdsRNAarefascinatingand,intruth,not
andbecause theywillonlytarget dsRNA,findinganinosine in yet fully understood. However, recent examples emphasize
an RNA is proof it was double-stranded in vivo. Although the thatsequence-independentbindingallowscompetitiontoplay
earliest of the identified endogenous dsRNAs included coding aroleinthisdiscrimination.
MolecularCell84,January4,2024ª2023ElsevierInc. 107
ll
Review
dsRNA structures are formed during transcription, a subset of
Box1.Innateimmunesensors
theadenosineswithinthemaredeaminatedbyADARstocreate
THERIG-ILIKERECEPTORS inosine (Box 2),56,57 which serves as a mark for ‘‘self’’ if the
dsRNAmakesittothecytoplasm(Box3).58Althoughbothiso-
In humans, RIG-I-like receptors (RLRs) are represented by
formsofADAR1canshuttletothenucleusandcarryoutedit-
three proteins: RIG-I, MDA5, and LGP2 (encoded by RIGI, ing,59 the p110 isoform is responsible for most nuclear A-to-I
IFIH1, and DHX58, respectively),5,8 which have well-known editing.45,60
rolesininnate immunity.Bindingofeither RIG-IorMDA5to
OtherRNAmodificationsthatmark‘‘self’’RNAsalsooccurco-
dsRNA drives induction of IFN signaling through activation transcriptionally, such as pseudouridylation71,72 and methyl-
of MAVS. The third member of the RLR family, LGP2, lacks ation,tocreateN6-methyladenosine(m6A).73–75m6Ahasbeen
the N-terminal caspase activation and recruitment domains reported to preclude the formation of dsRNA76 and thus indi-
(CARDs) found in RIG-I and MDA5 (Figure 1) and cannot
rectly protect against aberrant immune responses. Uridines
directly inducesignaling buthas beenreportedtomodulate
withinsingle-strandedRNAs(ssRNAs)induceaninnateimmune
theactivityofbothMDA5andRIG-I.
responseviathessRNA-specificendosomalreceptorsTLR7and
RLRsbindtodsRNAviatheirhelicasedomain(Figure1),which TLR8,77,78 and the demonstration that pseudouridine reduces
isofthesamefamilyasthehelicasedomainofDICER.9MDA5
thisresponse79gainednotorietywiththerecentNobelPrizeto
andRIG-IrecognizespecificfeaturesofdsRNA.RIG-Irecog-
KatalinKariko´ andDrewWeissman.The‘‘cap’’structurethatis
nizesbluntdsRNA(nooverhangs)with50di-ortriphosphates,
added during RNAP II transcription also marks transcripts as
whichisrareamongcellulartranscripts,andthusallowsself- ‘‘self,’’80 and prevents them from subsequently activating the
versusnon-self-discrimination.UponbindingdsRNA,RIG-Iun-
dsRNA sensor RIG-I in the cytoplasm. RIG-I recognizes the di
dergoes a conformational change that exposes its
andtriphosphatesonviraldsRNA(non-self)butcannotrecog-
CARDs,allowinginteractionwithMAVSand,ultimately,thepro-
nize the m7GpppNm ‘‘cap 1’’ modification that occurs on all
ductionoftypeIIFNsandpro-inflammatorycytokines. hostmRNAs(Box1).81
Incontrast,MDA5showsapreferenceforlongerdsRNAsand
RNA-seq analyses readily detect dsRNA within the steady-
doesnot recognize dsRNA termini.10Instead,MDA5exhibits state population of intronic sequences in the nucleus,23 but
length-dependentactivation,efficientlyformingactivated fila-
directevidenceintomechanismsofnucleardsRNAdegradation
ments along perfectly paired dsRNAs. Because MDA5 does
is elusive and worthy of future studies. Humans encode two
not distinguish termini, it can be activated by both viral and
dsRNAendonucleasesoftheRNaseIIIfamily,DROSHA,which
hostdsRNAs,butthistypicallyispreventedbyADARA-to-Ied-
processes primary miRNAs (pri-miRNAs) in the nucleus, and
itingofendogenousdsRNA(Box3).LGP2actsasacofactorfor DICER,whichprocessespre-miRNAsinthecytoplasm.82Non-
MDA5,aidingfilamentformationandstabilizingdsRNAinterac-
canonical functions in the nucleus have been suggested for
tions.11,12SimilartoRIG-I,thebindingandfilamentformation
both enzymes,83 with some studies indicating that DICER is
alongdsRNAexposesMDA5’sCARDs,allowingforinteracting
involved in degrading intermolecular dsRNA from converging
withMAVSandactivatingIFN-stimulatedgenes. transcripts.84Althoughdirectevidenceislacking,theexclusive
nuclearlocalizationofDROSHA,anditspreferenceforcleavage
PKR
at the base of a stem flanked by two single-stranded regions,
makesitmoresuitablethanDICERforcleavageoftheintramo-
UnliketheRIG-Ifamilymembers,thedsRNAsensorPKR(en-
leculardsRNAsthatoccurinintrons.Indeed,DROSHAcleavage
coded by EIF2AK2) binds to dsRNA via two dsRNA-binding
in regions that do not encode miRNAs has been reported.85
domains (dsRBDs, also referred to as dsRBMs). Similar to
Additionally, the vast majority of human dsRNA is found in in-
other domains that interact with dsRNA, dsRBDs bind in a
trons, and after splicing and debranching, it is also possible
sequence-non-specific manner. Binding of PKR to dsRNA of
thatdsRNA-containingintronsarerapidlydegradedbythenu-
asufficientlength,greaterthan30basepairs,promotesdimer-
clear exosome.86,87 Interestingly, in processing pri-miRNAs,
izationofPKR.13DimerizedPKRthencarriesoutanautophos-
DROSHA associates with the accessory factor DGCR8, but
phorylation reaction, which activates the kinase function of
some studies indicate DGCR8 also has functions separate
PKR.14TheprimarysubstrateofPKRisthetranslationinitiation
fromDROSHAthataremediatedbyinteractionwithexosomal
factor eIF2a (encoded by EIF2S1). Similar to phosphorylation
components.88
by other proteins involved in the integrated stress response,
AlthoughearlyreportsindicatedthatediteddsRNAswerere-
phosphorylation of eIF2a by PKR causes a global reduction
tained in the nucleus,89,90 other studies showed that edited
intranslationinitiation.15Fromanantiviralperspective,activa-
dsRNAwithin30UTRswasexportedtothecytoplasmandfound
tionofPKRthusservestoreduceproductionofviralproteins.
onpolysomes.91Thisdiscrepancymightbeexplainedifcertain
experimental conditions unintentionally caused stress, which
WHATHAPPENSTOENDOGENOUSdsRNAINTHE sometimes leads to formation of paraspeckles, subnuclear
NUCLEUS? structures that sequester RNAs.92 Being composed of RNA
andprotein,paraspeckleshaveawell-definedarchitecturethat
Thelong‘‘self’’dsRNAswearemostfamiliarwithinmammals iscoordinatedbythelongnoncodingRNA(lncRNA)NEAT1,as
aretranscribedbyRNApolymeraseII(RNAPII)andarewithin wellasseveralproteinsthatareessentialfortheirformation,93
the introns and 30 UTRs of nascent transcripts. As soon as includingNONO(formerlyknownasp54nrb),whichcanbindto
108 MolecularCell84,January4,2024
ll
Review
Box2.ADARs
AllmembersoftheADARfamilycontaindsRBDsandadeaminase(‘‘editase’’)domain(Figure1).Theyarehighlyconservedand
found in all metazoa so far analyzed,25 allowing for researchers to determine their conserved and divergent functions, from
C.eleganstohumans.AlthoughthedeaminasedomainitselfcanbinddsRNA,26dsRNAaffinityisfurtherconferredviadifferent
configurationsofdsRNA-andZ-DNA-bindingdomains(ZBDs).
ADAR1
AsillustratedinFigure1,mammalshavethreeADARs,eachwithaC-terminalcatalyticdomainand2or3dsRBDs.ADAR1,en-
codedbytheADARgeneinhumans,hastwoisoforms,p150andp110,anditisp150thatisresponsibleforsuppressionofdsRNA
sensingbyMDA5andPKR(Box3).27–29,30,31–36Thetwoisoformsaregeneratedthroughtheuseoftwopromoters,andalthough
thelongerisoformiscanonicallythoughtofasbeingIFNinducible,bothisoformsareinducedtosomeextentbyIFNsignaling.37,38
InadditiontothedsRBDsanddeaminasedomain,p110andp150bothpossessoneortwoZBDs,respectively.39Onlythefirst
ZBD of p150 (Zɑ) is capable of binding Z-DNA and Z-RNA.40 Although ADAR1 and ADAR2 (below) are capable of editing a
widerangeofdsRNAsubstrates,theydohavesomepreferences.DeaminationbyADAR1andADAR2requiresflippingoftheedi-
tedadenosineoutofthedoublehelix,thusleavinganunpaired‘‘orphanbase.’’41,42ThismechanismfavorsanA-Cmismatchatthe
editedsite43anddisfavorsa50guanosineofthetargetedadenosine.41Additionally,thereisapreferencefora50UorAanda30Gor
CforbothADAR1andADAR2.44TheabilitytobindZ-RNA,whichtakesonaleft-handedhelicalstructure,contributestotheediting
ofasmallportionofthetotalnumberofRNAseditedbyp150.45
ADAR2
ThehumanADAR2proteinisencodedbythegeneADARB1(Adarb1,mice).ExpressionofADAR2islargelyconfinedtothebrain.46
TheeditingfunctionofADAR2isessentialinmicewhereiteditstheGRIA2mRNA,whichencodesanAMPA(a-amino-3-hydroxy-
5-methyl-4-isoxazolepropionate)glutamatereceptor.47EditingofGRIA2mRNAconvertsaCAGcodontoCIG,thusrecodingthe
mRNAtomakeArginplaceofGlnintheproteinproduct.47Thisistheonlyknownessentialrecodingeventinmammals.48
ADAR3
Inhumans,theADAR3proteinisencodedbythegeneADARB2(Adarb2,mice).UnlikeADAR1andADAR2,ADAR3hasnocatalytic
activityandhastheabilitytobindsingle-strandedRNA.49ADAR3expressionislargelyconfinedtothebrain,50whereitisinvolved
inlearningandmemory.51RecentworkhasrevealedaroleforADAR3inglioblastomawhereitregulatesA-to-IeditingbyADAR1,
MAVSproteinexpression,andNF-kBsignaling.52,53
inosine-containingRNAs.89Otherreportsshowthatexportof30 lated by dsRNA.59,99 Could these secondary interactions with
UTRsthatcontaininvertedAluscanberegulatedbymethylation dsRBPsfacilitatemoregeneraldsRNAexport?Additionally,dur-
ofNONO94orbindingofthedsRBPSTAU1(Figure1),95which ingmitosis,cytoplasmicPKRisactivatedbynucleardsRNAs,100
mightalsoexplaindiscrepanciesinreportsofnuclearretention suggesting that, at least in some cases, dsRNAs could
of30UTRsthatcontaininvertedAlus. simply diffuse to the cytoplasm when the nuclear envelope
breaksdown.
EXPORTOFdsRNAOUTOFTHENUCLEUS Understanding mechanisms of dsRNA export is extremely
important because aberrant export of dsRNA increases the
AlthoughdsRNAwithinintronswouldpresumablystayinthenu- chanceofactivationofdsRNAsensorsinthecytoplasm;indeed,
cleus,atleastsome30UTRsthatcontaindsRNAareexportedto
some studies indicate that certain viruses arrest export to
thecytoplasmandfoundonpolysomes;91,96however,theexport decreaseactivationofinnateimmunepathways.101Tightregula-
mechanisms involved have not been clearly defined. Mature tionofexportmightbeimportantduringtimesofstress,which,in
mRNAswithdsRNAintheir30UTRsmightbeexportedviacon-
somecases,leadstoincreaseddsRNA.Forexample,afterDNA
ventionalpathways,97albeitsomestudiesindicateSTAU1bind- double-strand breaks occur, transcription of antisense RNA is
ingisimportanttoovercomenuclearretention.95 upregulated,leadingtoanincreaseinhighlypairedintermolec-
Hypothetically, dsRNA could take advantage of alternative ulardsRNA.84,102Iftheselong,perfectlypairedsense,antisense
mechanismstoenterthecytoplasm.Onepossibilityisviatheex- dsRNAsmadeittothecytoplasm,theywouldstimulatedsRNA
portin protein XPO5, which shuttles pre-miRNAs from the nu- immunesensors.
cleus into the cytoplasm. Although the binding of XPO5 to its
pre-miRNA substrate is specific and mediated by recognition WHATHAPPENSTOdsRNAINTHECYTOPLASM?
ofthetwo-nucleotide30overhangleftafterDROSHAcleavage,98
XPO5isalsoknowntoexportdsRBPs,includingADAR1-p110, For the dsRNAs that make it to the cytoplasm, their future is
ILF3,PKR,andSTAU1,andinsomecases,thisexportisstimu- largely determined by what proteins they encounter, but how
MolecularCell84,January4,2024 109
ll
Review
Figure1. Open-readingframestructuresand
subcellularlocationsofdsRBPs
DomainarrangementsofhumandsRBPsandRLRs
aredepictedascoloredboxes(inlegend)alongthe
length of the peptide chain (gray). Lengths and
domainarchitecturesapproximatelytoscale.Adja-
centtoeachschematicisthesubcellularlocation(s)
for each: N for nuclear, C for cytoplasmic, M for
mitochondrial,andSfornuclearspeckles.Allan-
notationswereretrievedfromtheUniProtdatabase
on October 13, 2023; we note that nuclear-
cytoplasmicshuttlingispervasive,anditisdifficult
toproveexclusivitytoasubcellularcompartment.
simply loaded onto ribosomes and trans-
lated.91 During translation, mRNAs can
be subject to nonsense-mediated decay
(NMD), a process that serves to degrade
faulty mRNAs or regulate their levels.107
Interestingly,thereisarelateddecaypro-
cess called Staufen-mediated decay
(SMD),107 which, in mammals, involves
STAU1 and STAU2 (Figure 1) and targets
mRNAs containing regions of dsRNA in
their30 UTRs.Forexample,theADPribo-
sylation factor (ARF1) mRNA has a
short stem-loop in its 30 UTR that binds
STAU1andleadstoSMD.108Otherexam-
ples involve Alu elements within 30 UTRs
that form dsRNA by pairing intermolecu-
larly with complementary Alu elements
in lncRNAs.109 At present, it is somewhat
mysteriousastowhichdsRNA-containing
transcripts are subject to SMD, but
compelling models have been pro-
posed.110
HowmanyendogenousdsRNAsare
immunogenic,andwhatistheir
identity?
Of the ADAR family members, ADAR1-
p150 seems most important for marking
endogenous dsRNA as self, and loss of
this is controlled is unclear. In healthy cells, in the absence of ADAR1 causes activation of MDA527–29,31 and PKR30,32–36
stress or viral infection, innate immune dsRNA sensors, such (Box 3). Most assume that the dsRNAs that activate MDA5
astheRLRsandPKR(Box1),areexpressedatlowlevels,103,104 and/or PKR following loss of ADAR1 arise from the
and cytoplasmic dsRBPs carry out their normal functions on inverted Alu sequences that inhabit many 30 UTRs, but in
endogenousdsRNA.Awell-characterizedandobviousexample truth, the identity of the immunogenic dsRNAs is not proven.
istheprocessingofpre-miRNAsinthecytoplasmbythedsRBP RNase A protection assays performed in cells support
DICER.105,106 This exemplifies the importance of segregating binding of MDA5 to Alu sequences and a decreased
longer dsRNAs, for example, the pri-miRNAs, in the nucleus binding in the presence of ADAR1,111 but definitive evidence
wheretheywillnotencounterdsRNAsensors.Theshorterpre- that inverted Alus are responsible for inducing an MDA5-
miRNAs do not have the triphosphorylated 50 end that would dependent interferon response is lacking. Indeed, in vitro
be expected to trigger RIG-I, and their short length and mis- studies show that the oligomerization of MDA5 required for
matcheswouldprecludeactivationofMDA5. interferon induction is impeded by the mismatches that typi-
Presumably,longerdsRNAsthatenterthecytoplasmfromthe cally are found in base-paired inverted Alus, even without
nucleusareprimarilylocatedin30UTRsthathavebeeneditedby A-to-I editing sites; however, at higher MDA5 concentrations,
ADARs.TheinosinesintheseRNAsmeansthatMDA5willnotbe binding can be observed and is decreased by ADAR-editing
activated(Box3),andinsomecases,itisclearthemRNAsare sites.111
110 MolecularCell84,January4,2024
ll
Review
Box3.A-to-Ieditingandsuppressionofinnateimmunity
A-to-IeditingbyADAR1isessentialformarking‘‘self’’RNAsandsuppressingactivationofdsRNAsensors.MutationsinADAR1
causetheinterferonopathyAicardi-Goutie`ressyndrome(AGS).61(ForanuptodateandthoroughreviewoftheroleofADAR1in
innateimmunity,seedeReuverandMaelfait.62)MouseknockoutsofADAR1areembryoniclethal,withdeathatE11.0–E12.5.63
TheAdar1(cid:2)/(cid:2)embryosshowelevatedIFNsignalinganddefectivehematopoiesis.64KnockoutofMDA5(encodedbythegene
Ifih1)orMAVSsuppressestheembryoniclethalityofAdar1(cid:2)/(cid:2),withmicesurvivingtopost-natalday1.27ADAR1-p150-specific
knockoutslargelyphenocopyknockoutofADAR1,suggestingthatADAR1-p150isresponsibleforsuppressionofdsRNAsensing
byMDA5.28ThisfunctionofADAR1-p150requiresA-to-IeditingactivityasaknockinmutantofADAR1thatiscatalyticallyinactive
(Adar1E861A/E861A) closely phenocopies knockout of Adar1, and can be rescued by knockout of MDA5.29 Interestingly, the
Adar1E861A/E861A Ifih1(cid:2)/(cid:2) mice live much longer than the Adar1(cid:2)/(cid:2) Ifih1(cid:2)/(cid:2) mice, suggesting editing-independent roles for
ADAR1.AlthoughthesedatastronglysupportthemodelthatADAR1-p150suppressesMDA5activationthroughA-to-Iediting,
somequestionshaveremainedunanswereduntilmorerecently.Foremost,whatcausespost-natallethalityofAdar1(cid:2)/(cid:2)Ifih1(cid:2)/(cid:2)
mice.RecentworkshowsthatPKRisactivatedinAdar1(cid:2)/(cid:2)Ifih1(cid:2)/(cid:2)butnotAdar1E861A/E861AIfih1(cid:2)/(cid:2)miceandthatknockoutof
PKRinaddition to MDA5(Adar1(cid:2)/(cid:2)Ifih1(cid:2)/(cid:2)Eif2ak2(cid:2)/(cid:2))rescues the lethalityof Adar1 knockoutto adulthood.65,66Inthemain
text,wedescribethemechanismofPKRinhibitionbyADAR1,whichdoesnotrequireeditingbyADAR1.
AlthoughADAR1-p110andADAR1-p150arenearlyidentical,bothcontainingadeaminasedomainandthreedsRBDs,theyarenot
redundantintheroleofpreventingPKRandMDA5activation.Thisispartiallydrivenbythelocalizationofthetwoproteinswiththe
nuclearADAR1-p110primarilyeditingintrons,whereasthegenerallycytoplasmicADAR1-p150primarilyedits30UTRs,whichare
morelikelytoencounterMDA5andPKRinthecytoplasm.45AnotherkeydifferencebetweentheproteinsistheactiveZBDof
ADAR1-p150,Zɑ.MutationsintheZɑdomainarecommoninAGS,61suggestingthatZɑhasanimportantroleinsuppressingacti-
vationofdsRNAsensors.MousemodelsofAGSthathavehemizygousmutationsofAdar1,combiningpointmutationsinZɑwith
knockoutofAdar1orAdar1-p150,showvaryingdegreesoflethalityandactivationofIFNsignalingthroughMDA5.30,67,68Similarly,
theabilityofADAR1tobindZ-RNApreventsactivationofZBP1,theonlyotherhumanproteinthatcontainsaZBD.69,70Thesedata
highlighttheimportanceoftheZBDforADAR1’sabilitytosuppressactivationofdsRNAsensorsbyendogenousdsRNAs.
An increasingly popular view is that only a small subset of by ADAR1-p150 to prevent activation of PKR and MDA5, it is
dsRNAs are responsible for activating MDA5 following loss of important to note that mitochondrially encoded RNAs can
ADAR1-p15045,60 and that possibly their features have made alsoformdsRNAthatcanbindtoandactivatedsRNAsensors,
them difficult to find.112 In a mouse mutant lacking ADAR1- such as PKR.114 Bidirectional transcription of mitochondrial
p110andADAR2,leavingonlyADAR1-p150 tocarryoutA-to-I DNA can generate intermolecular dsRNA with perfect base
editing,only2%ofeditsremained.60This2%ofremainingedits, pairingin lengthsmuchlongerthanthedsRNA regionsarising
however, was sufficient to prevent activation of type I IFN fromrepetitiveelements,uptoseveralkilobases.115Thesemt-
signalingdownstreamofMDA5. dsRNAs can represent a significant proportion of the RNAs
Recent work sought to identify the ‘‘immunogenic’’ dsRNAs identified by pull-down with a dsRNA-specific antibody or by
thatactivateMDA5followinglossofADAR1-p150byidentifying pull-down of PKR.114 In some cell lines, such as HeLa or
theRNAsspecificallyeditedbyADAR1-p150andADAR1-p110 HEK293T, mt-dsRNAs represent the majority of dsRNA in the
inhumancells.113Thisanalysisrevealedthatasmallsubsetof cell(70%–90%),whereasinothercelltypes,suchasneurons,
A-to-IeditsareresponsibleforsuppressionofMDA5activation, mt-dsRNAs represent a small proportion (40%).116 Given the
in agreement with prior work in mice described above. These endosymbiotic evolution of the mitochondrion within eukary-
editslargelyoccurredin30UTRs,generallywithininvertedAlure- otes, it is interesting to think about what systems may have
peats,andvariedgreatlybetweencelllines.Overexpressionof evolved to prevent sensing of mt-dsRNA as foreign RNA—
the ADAR1-p150-specific dsRNAs caused activation of IFN althoughitwasoriginally foreign.
signalingintheabsenceofADAR1-p150whenMDA5wasover-
expressed.Thesefindingssuggestthatonlyasmallnumberof REGULATIONBYCOMPETITION:THEINTRICATE
endogenous dsRNAs are responsible for the activation of BALANCEOFdsRBPsANDdsRNAs
MDA5intheabsenceofADAR1.Giventhevariabilityofediting
across tissues, and possible changes in the expression of BecausedsRBPsarenotsequencespecific,changesinthecon-
endogenousdsRNAs,itmaybethecasethatthedsRNAsthat centrationofadsRBPordsRNA,whetheritderivesfromavirus
activateMDA5and/orPKRfollowinglossofADAR1varybytis- orendogenoustranscript,hasthepotentialtochangebiological
sueorcelltype.Furthermore,giventhebindingpreferencesof outcome by competition. It is our hypothesis that competition
PKR and MDA5, the RNAs that activate each protein in the between dsRBPsand dsRNAsisoperating in thenucleus,the
absence of ADAR1 may not be the same. Future work is still cytoplasm,andthroughoutthelifeofadsRNA.Inthesections
neededtodefinitivelyidentifytheRNAsthatbindtoandactivate below, we review existing examples of competition between
MDA5,andimportantly,PKR,followinglossofADAR1. dsRBPs and dsRNA, using these to build models whereby
Although our discussion above highlights the search for nu- competition plays a natural role in the regulation of dsRBPs
clear-derived immunogenic RNAs, in particular those edited andtheirfunctions.
MolecularCell84,January4,2024 111
ll
Review
CompetitionbetweenviralandhostdsRBPs highlight the complex competition between these three
Themoleculararmsracebetweenvirusesandthemammalian dsRBPs—STAU1, ADAR1, and PKR.
innateimmunesystemoffersnumerouslong-recognized117ex- In yet another example, the RNA helicase DHX9 functions
amplesofnon-sequence-specificdsRBPscompetingfordsRNA redundantly with ADAR1 to suppress several dsRNA-sensing
substrates.118,119Forexample,inchicken,similartothatinhu- pathways.124Itwasfoundthat,inADAR1-dependentcelllines,
mans, MDA5 activates the type I IFN pathway upon infection depletion of DHX9 caused activation of PKR, whereas in
with an RNA virus. The infectious bursal disease virus of ADAR1-independent cell lines, depletion of both ADAR1 and
chickensevadesthisactivationviaitsVP3protein.120VP3com- DHX9 was required for activation of multiple dsRNA-sensing
petes directly with MDA5 for binding to the viral dsRNA via pathways, resulting in a viral mimicry phenotype. Mechanistic
itsdsRBD. studies revealed that the dsRBDs of DHX9 were sufficient to
Althoughthefavoredmodelforthemechanismoftheseviral rescue activation of PKR. Given the nuclear localization of
suppressorsofRNAsensors(VSRs)involvestheviral-encoded DHX9, these findings suggest that DHX9 sequesters some
proteincoatingthedsRNAtosequesteritfromdsRNAsensors, endogenousdsRNAsinthenucleustopreventPKRactivation.
suchasMDA5orRIG-I,inmanycases,thishasnotbeenproven. Inmanyoftheexamplesabove,effectswererescuedsimply
AlthoughdsRBDsaredefinedbytheirabilitytobinddsRNA,they byexpressingadsRBD.Interestingly,inothercases,thedsRBP
can also form direct protein-protein interactions, such as the may contain other domains that are important for a biological
interactionofTRBPwithDICER.105,121Experimentalmutations function, and competition between dsRBDs may bring in new
that disrupt dsRNA binding may also disrupt protein-protein functions. For example, by binding to mRNAs important for
interaction;therefore,dsRBDmutationsthatprecludeinhibition propermitoticprogression,thedsRBPNF90(encodedbyILF3)
donotprovetheVSRiscoatingdsRNA.Indeed,paramyxovirus stabilizes the mRNAs by competing with the dsRBPs STAU1
V protein acts as a VSR by interacting directly with MDA5 to and STAU2 for binding, thus preventing SMD of pro-mitotic
disruptitsfolding.122 mRNAs.125ThisfunctionofNF90isenabledbyinteractionwith
NF45viatheDZF(domainassociatedwithzincfingers)ofboth
CompetitionbetweenendogenousdsRBPs proteins, which other studies show increases dsRNA binding
Although itisstraightforwardto understandwhyviruses might by10-fold,126possiblyallowingNF90-NF45 tobettercompete
capitalize on the non-sequence specificity of dsRBPs and withSTAU1andSTAU2.
encodedsRBPsthatcompetewithdsRNAsensorsforbinding Although,sofar,ourdiscussionofcompetitionhasfocusedon
to viral dsRNA, there are also many examples indicating that examples involving the dsRBD, there are similar examples
hostdsRBPs bindeach other’s substrates. Although itiseasy involvingthehelicasedomainofDICER.RNA-independentinter-
to categorize these examples as artifacts of the experimental actionsoccurbetweenDICER’shelicasedomainandADAR1,127
setup, it also seems possible that competition is an intrinsic TRBP, and PACT,105 and competition with these interactions
featureoftheregulationofdsRBPsincells. could also affect the balance of dsRNA and dsRBPs.127,128
Recent work shows that activation of dsRNA sensors by RNA-dependent interactions with DICER’s helicase domain
endogenous dsRNA can be inhibited by increased levels of also seem likely to affect the balance.128 Immunoprecipitation
endogenous dsRBPs, because the dsRBPs compete with oftaggedDICERfollowedbyLC-MS/MS,todetermineinteract-
thesensorsforbindingtotheendogenousRNA.Asdiscussed ingproteins,identifiedthedirectinteractionwithTRBP,withor
in Box 3, ADAR1 is essential for suppression of dsRNA withoutviralinfection,andaslewofotherproteinsthataresignif-
sensing by MDA5 and has also been implicated in suppres- icantlyenrichedinthepresenceofinfectionwitheitherSindbis
sion of PKR activation.30,32–36 Whereas suppression of virus or Semliki forest virus,128 including PKR, ADAR1, PACT,
MDA5activationbyADAR1-p150isdependentonA-to-Iedit- and DHX9.128 Treatment with ribonuclease confirmed that
ing,studiesinADAR1-dependentcelllines(celllinesthatacti- DICERandTRBPinteractedviaadirectprotein,proteininterac-
vate dsRNA-sensing pathways following loss of ADAR1) tion,whereasinteractionsofDICERwithPKR,PACT,andDHX9
show that overexpression of catalytically inactive ADAR1- werealmostcompletelylostafterRNasetreatment.Intriguingly,
p150 is sufficient to suppress PKR activation and rescue cell deletionofDICER’shelicasedomaintriggeredaPKR-dependent
viability.33,34 These findings suggest that ADAR1 suppresses decreaseinviraltiter,suggestingthat,bysequesteringPKR,the
PKR activation by endogenous dsRNA by some means other helicasedomainpreventedanantiviralresponse.
than editing, presumably through competition with PKR for
dsRNA binding. More recent work directly establishes that Competitionisconserved
ADAR1-p150 suppresses PKR activation through its ability Observationsofcompetitionarenotlimitedtomammaliancells.
to bind dsRNA.65 In this study, overexpression of the SimilartomammalianADARs,ADARsfrombothC.elegansand
dsRBDs of ADAR1, ADAR2, and STAU1 each could prevent D. melanogaster have editing-independent effects.129–131 In
activation of PKR in the absence of ADAR1, suggesting that C.elegans,deletionofthegeneencodingthecatalyticallyinac-
theidentityofthedsRBDwasnotasimportantasitsgeneral tive ADAR homolog, ADR-1, causes accumulation of mature
ability to bind dsRNA. Similar to ADAR1-p150, STAU1 has miRNAs and depletion of pri-miRNAs,129 consistent with the
been shown to bind dsRNA within the 30 UTRs of some ideathatADR-1competeswithDROSHAforpri-miRNAbinding
mRNAs and prevent the activation of PKR.95 ADAR1 also in- toaffectmiRNAprocessing.Similarly,carefulexaminationofthe
hibits STAU1 function in an editing-independent way, by miR-376clusterinhumancelllinesrevealedthatADAR2blocks
competing for its dsRNA-binding sites.123 These findings pri-miRNAprocessingbyDROSHAthroughitsdsRNA-binding
112 MolecularCell84,January4,2024
ll
Review
ability.130Similar observations have been made in human em- balance ofcytoplasmic immunogenicdsRNAand dsRNAsen-
bryonicstemcells,whereADAR1hasanimportantroleinsup- sors in a controlled way is a promising therapeutic option for
pressing processing of miR-302, which promotes stem cell cancer.
self-renewal, by preventing processing of pri-miR-302 in an IfonebelievesinaprimordialRNAworld,137replicationlikely
RNA-editing-independentmanner.132 involved a dsRNA intermediate, and as proteins entered the
InvertebrateslackacanonicalIFNpathway,anditisDicerthat scene,thecompetitionbegan.Moderndaysolutionswerebuilt
mediatesantiviraldefense.Yet,despitethedifferencesbetween onafinelybalancedinterplaybetweendsRNAanddsRBPs.An
vertebrate and invertebrate immune responses, the role advantageforextantimmunepathwaysisthatthesystemallows
for ADARs in modulating the response is conserved. The thecelltobeeverreadytofightinfection.dsRNAsensorscanbe
invertebrate C. elegans triggers an antiviral RNAi response in expressed even in the presence of endogenous dsRNAs that
the absence of its ADAR RNA-editing enzyme.133 Similarly, in couldactivatethem,readytocomeintoplayasthebalanceis
D. melanogaster, loss of A-to-I editing by Drosophila ADAR tilted by high levels of viral dsRNA (Figure 2A). An interesting
(a homolog of human ADAR2)134 causes an innate immune exampleoftheimportanceofthisbalancecanbeseeninhuman
response.131Theaberrantimmuneresponsecausedbydeple- neurons,whichhaveunusuallyhighlevelsofimmunostimulatory
tionofDrosophilaADARisrescuedbyoverexpressionofcatalyt- dsRNA. Recent studies show that this is due to ELAVL RNA-
icallyinactiveADAR,suggestingthatRNA-editing-independent binding proteins that increase 30 UTR length, presumably to
roles for ADAR in suppression of dsRNA sensing have been encompass additional regions of dsRNA.116 The activation of
conservedacrossspecies. dsRNAsensorsinthesecellsisfine-tuned,soasnottocause
cell death, but high enough that the cell is primed to respond
Fociandclusters toviralinfection.Shorteningof30UTRsleadstoreduceddsRNA
Althoughtheexamplesdiscussedsofaraddressthecompeti- sensor activation and susceptibility to viral infection. It is pro-
tion that occurs after a change in the levels of dsRBPs, it is posed that this exemplifies a situation whereby self dsRNAs
also important to consider what happens when levels of are used to preemptively induce antiviral immunity to protect
dsRNA increase. Recent studies show that introduction of neuronal cells from viral infection. This example emphasizes
dsRNA into the cytoplasm due to viral infection, expression the need to carefully evaluate different tissues to determine if
from a reporter, during mitosis, or after knockdown of thereisauniquebalanceofdsRBPsanddsRNAtunedforthe
ADAR1 induces the formation of foci135 or clusters136 that specificneedsofthetissue.
are distinct from stress granules. Both recent studies show There are many open questions in regard to how competi-
thatthelocalizationofproteinstothesefoci/clustersisdepen- tion contributes to dsRNA sensing during an innate immune
dentondsRBDs,andwhenanalyzed,thefoci/clusterscontain response, or in the natural regulation of dsRBP function. For
dsRNA.Togetherthestudiesindicatethefoci/clusterscontain instance,howmanyotherdsRBPscompetewithdsRNAsen-
PKR,ADAR1,PACT,STAU1,NLRP1,andDHX9(Figure1).The sors for binding to endogenous or foreign RNA? For each
reports offer opposing speculations on function, proposing competing dsRBP found, it will be important to evaluate their
either that the foci/clusters contribute to PKR activation or substrate specificity and affinity for dsRNA binding, as well
that they are inhibitory to PKR activation.135,136 As described as their abundance in various cells and conditions. Some
below, in our favorite model, PKR would be subject to sub- work has been done in this area; surprisingly, the number of
strate inhibition infoci/clusters. dsRBDs is thus far not predictive of affinity.138 Additionally,
cooperative binding may influence competition between
Amodel dsRBPs. Cataloging proteins capable of binding dsRNA is
Regulation by competition mandates a fine balance between complicated by the fact that, as of yet, it is not clear that we
dsRNAanddsRBPs.Indeed,onewondersifthemanyrepetitive understand all of the motifs that allow dsRNA binding, such
elementsretainedinourgenomesservetoexpressdsRNAthat as zinc-finger domains and diverse helicases,54 hindering
helpsmaintainthisbalance.Figure2Aillustrateshowcontrolled sequence similarity searches. Although complex, identifying
balance between dsRBP expression and dsRNA abundance the dsRBPs that are capable of suppressing dsRNA sensing
might determine whether or not dsRNA sensors involved in throughcompetition,andgainingamechanisticunderstanding
innate immunity are active. Under healthy conditions, cellular ofhowthishappens,mayofferimportant,therapeuticallyrele-
dsRBPs sequester dsRNA, and dsRNA sensors are inactive. vantinsightintotheinnateresponsetoviralinfectionandauto-
TheincreasedabundanceofdsRNAthatwouldaccompanyviral immune disorders.
infectionorstresswouldshiftthebalanceandallowactivationof Intrinsic to the competition model is the dsRBD, which al-
dsRNA sensors. This, in turn, would trigger an IFN response, lowsdsRBPsthatcontainthismotiftobindinasequence-in-
leading to increased expression of dsRNA sensors and defini- dependentmannertoanydsRNA.Eachmotifbinds(cid:3)16base
tively tilting the balance to favor antiviral defense. Eventually pairs, interacting with (cid:3)1.5 helical turns of an A-form RNA
this feedback loop would be broken when the abundance of duplex and spanning two minor grooves and the intervening
dsRNAinthecytoplasmwasreduced,eitherthroughdegrada- major groove54; it is common to find multiple copies of the
tion or editing by ADAR1. Finally, loss or reduced expression dsRBD in a dsRBP. In Figure 2B, we go one step further in
ofanendogenousdsRBPcouldalsoallowbindingandactivation our competition model, illustrating that ‘‘productive binding’’
of innate immune dsRNA sensors. As discussed in the final involvesalldsRBDsofagivendsRBPinteractingwithasingle
sectionofthisarticle,recentstudiesindicatethatchangingthe dsRNA (Figure 2B, left), whereas ‘‘nonproductive binding’’
MolecularCell84,January4,2024 113
ll
Review
A Figure2. Amodelforregulationby
competition
(A)BalancebetweendsRNAsensorsanddsRBPs.
Inahealthycell(left),dsRNAsensorsareexpressed
atlowlevels,butdsRBPsareprevalentandactto
keep dsRNA sensors from being activated by
dsRNA.dsRBPscanusedifferentmechanismsto
reducetheamountofimmunogenicdsRNA avail-
able for interacting with dsRNA sensors, for
example,theymightedit,degrade,orsimplybind
dsRNA.Upon lossofthesedsRBPs (topright) or
duringaviralinfection(bottomright),theconcen-
trationofdsRNAreachesathresholdthatallowsfor
dsRNAsensoractivation.NLRP1,NLRfamilypyrin
domaincontaining1.
(B)Productiveversusnonproductivebinding.Two
B dsRBPsareshown,eachwithtwodsRBDs(blue)
and a functional/catalytic domain (salmon).
Productive binding involves each protein
interacting with a single dsRNA; in one example
the functional/catalytic domain also interacts with
dsRNA, as would occur with an ADAR. In
nonproductive binding, a high concentration of
dsRNA promotes dsRBD binding to different
dsRNAstoformfociorclusters.
(C) Competitive binding dynamics. Two distinct
dsRBPs,eachwithtwodsRBDs(blue)andasingle
functional domain (dsRBP-1, salmon rectangle;
dsRBP-2, green triangle), are first illustrated
C
productively binding a single dsRNA. Next,
dsRBP-2, with the help of accessory proteins
(bottom) that confer a competitive edge (pink
three-quarter circle), or increased concentration
(top), displaces dsRBP-1, showcasing potential
regulationofdsRBPfunctionsthroughcompetition.
LOOKINGTOWARDTHEFUTURE:
ACTIVATIONOFdsRNASENSORSAS
ATHERAPYFORCANCER
An exciting and emerging twist to cancer
therapeutics involves shifting the balance
of immunogenic dsRNA in the cytoplasm
involves each dsRBD of a single protein interacting with to trigger an innate immune response, sometimes referred to
different dsRNAs to create an interconnected network of asviralmimicry.141Viralmimicryhasgreatpotentialasathera-
dsRNA (Figure 2B, right). Nonproductive binding would be peutic approach forcancer, and in addition to cell intrinsic ef-
more likely at high concentrations of dsRNA, such as what fects,itcansometimesawakentheimmunesystemtothepres-
might occur within foci or clusters, and has been used to ence of the tumor and promote anti-tumor immunity. For
explain the substrate inhibition that has long been known to example,knockdownofADAR1-p150intumorcellsreducesed-
occurwithboth ADARs139and PKR140athighconcentrations itingofdsRNA,inducinginterferonandsensitizingthetumorsto
ofdsRNA.Inthislight,foci/clustersmaybeameansofinacti- immunotherapy.142
vating the dsRBPs withinthem. Given the above, it is not surprising that ADAR1-p150 is an
Althoughexistingexamplesarelimited,anintriguingprediction essentialgeneinmanycancercelllines—includingthosederived
ofthemodelisthatcompetitionbetweendsRBDscouldactually frombreastandlung.33–35DepletionofADAR1insomecancercell
regulate,orswitch,biologicaloutcome.Figure2Cillustratestwo lines with elevated IFN signaling causes cell death. In ADAR1-
dsRBD-containingproteinsinteractingwithdsRNAinaproduc- dependentcells,followingdepletionofADAR1,thereisactivation
tive manner, with each dsRBP including a third ‘‘functional’’ ofthetypeIIFNpathwaydownstreamofMDA5andactivationof
domain (labeled 1 and 2), which might comprise a catalytic PKRtodrivetranslationalrepression.33–35Althoughforsomecan-
domain, such as a kinase or deaminase. Competition between cercellsdepletionofADAR1aloneissufficienttoinduceaviral
such dsRBPs could actually switch which catalytic/functional mimicryphenotype,forothercells,thisdoesnotoccur.Asdis-
domainwasinteractingwiththedsRNA,thusregulatingbiolog- cussed above, depletion of DHX9 in combination with ADAR1
ical outcome. In this scenario the competition of NF90/45 and can induce a viral mimicry phenotype. In this case, the loss of
STAU1/2discussedabovewouldberesponsiblefortheregula- DHX9andADAR1togetherisnecessarytoshiftthebalanceof
tionofmRNAdegradation. dsRBPsinthecellandenableactivationofdsRNAsensors.
114 MolecularCell84,January4,2024
ll
Review
Thesameeffectcanbeachievedbyincreasingtheabundance 3.Carter,W.A.,andDeClercq,E.(1974).Viralinfectionandhostdefense.
ofdsRNAsinthecell.CellstreatedwiththeDNAmethyltransfer- Science186,1172–1178.
ase (DNMT) inhibitor 5-AZA-CdR induce transcription of 4.Schlee,M.,andHartmann,G.(2016).Discriminatingselffromnon-selfin
retroelements, including inverted SINEs, and thereby induce nucleicacidsensing.Nat.Rev.Immunol.16,566–580.
ADAR1 dependency.143 In some cell lines, DNMT inhibitors 5.Rehwinkel,J.,andGack,M.U.(2020).RIG-I-likereceptors:theirregula-
alone are sufficient to induce a viral mimicry phenotype tionandrolesinRNAsensing.Nat.Rev.Immunol.20,537–551.
through activation of dsRNA sensors.141,144 The same pheno-
6.Chen,Y.G.,andHur,S.(2022).CellularoriginsofdsRNA,theirrecogni-
typecanbeaccomplishedbydepletionofepigeneticsilencing tionandconsequences.Nat.Rev.Mol.CellBiol.23,286–301.
complexes that are important for suppressing retroelement 7.Barnett,K.C.,Li,S.,Liang,K.,andTing,J.P.(2023).A360(cid:4)viewofthe
expression.145,146 Similarly, certain splicing inhibitors lead to inflammasome: mechanisms of activation, cell death, and diseases.
exportofunsplicedtranscriptsthatcontainintronicdsRNA,re- Cell186,2288–2312.
sulting in antiviral signaling and apoptosis,147 and likewise, 8.Hur,S.(2019).Double-strandedRNAsensorsandmodulatorsininnate
disruption of splicing regulatory proteins can result in dsRNA immunity.Annu.Rev.Immunol.37,349–375.
accumulationandimmunostimulatoryphenotypes.Forexample,
9.Ahmad,S.,andHur,S.(2015).Helicasesinantiviralimmunity:dualprop-
knockdown of proteins such as HNRPNM148 and HNRNPC149 ertiesassensorsandeffectors.TrendsBiochem.Sci.40,576–585.
results in unspliced mRNAs that are transported to the cyto-
10.Peisley,A.,Lin,C.,Wu,B.,Orme-Johnson,M.,Liu,M.,Walz,T.,andHur,
plasmandinduceaninnateimmuneresponse.Decreasingthe S.(2011).CooperativeassemblyanddynamicdisassemblyofMDA5fil-
degradationofdsRNAscanalsodriveactivationofdsRNAsen- aments for viral dsRNA recognition. Proc. Natl. Acad. Sci. USA 108,
21010–21015.
sors, and depletion of RNA exonuclease XRN1 in cancer cell
lines with elevated IFN signaling causes activation of PKR, 11.Duic,I.,Tadakuma,H.,Harada,Y.,Yamaue,R.,Deguchi,K.,Suzuki,Y.,
MAVS,andcelldeath.150,151Similarly,phosphorothioateDNAol- Yoshimura,S.H.,Kato,H.,Takeyasu,K.,andFujita,T.(2020).ViralRNA
recognitionbyLGP2andMDA5,andactivationofsignalingthroughstep-
igonucleotides, similar to those used in some FDA-approved by-stepconformationalchanges.NucleicAcidsRes.48,11664–11674.
therapies,havebeenshowntopreventnucleardecayofintronic
12.Bruns,A.M.,Leser,G.P.,Lamb, R.A., andHorvath, C.M. (2014).The
and intergenic retroelements leading to activation of PKR and innateimmunesensorLGP2activatesantiviralsignalingbyregulating
OAS/RNaseL.152 MDA5-RNAinteractionandfilamentassembly.Mol.Cell55,771–781.
Ineachoftheexamplesabove,thebalancebetweenbinding
13.Lemaire,P.A.,Anderson,E.,Lary,J.,andCole,J.L.(2008).Mechanismof
ofdsRNAbydsRBPsanddsRNAsensorshasbeenshiftedto- PKRactivationbydsRNA.J.Mol.Biol.381,351–360.
ward the dsRNA sensors. As we have discussed above, this
14.Galabru,J.,Katze,M.G.,Robert,N.,andHovanessian,A.G.(1989).The
can occur through loss of dsRBPs, increased expression of bindingofdouble-strandedRNAandadenovirusVAIRNAtotheinter-
dsRNA sensors, or increased dsRNA abundance. Disrupting feron-inducedproteinkinase.Eur.J.Biochem.178,581–589.
thisbalancehasgreatpotentialforcancertherapiesand,poten-
15.Hinnebusch,A.G.(2011).Molecularmechanismofscanningandstart
tially,antiviraltherapies.Further,althoughwehavefocusedon codonselectionineukaryotes.Microbiol.Mol.Biol.Rev.75,434–467.
usingviralmimicrytotreatcancer,othertherapeuticapplications
16.Whipple, J.M., Youssef, O.A., Aruscavage, P.J., Nix, D.A., Hong, C.,
canbeenvisioned.TheELAVLproteinsthatincreaseimmuno- Johnson,W.E.,andBass,B.L.(2015).Genome-wideprofilingoftheC.
genicdsRNAinneuronscouldbeexpressedtoincreasedsRNA elegansdsRNAome.RNA21,786–800.
levelsforcancertreatmentbutalsodepletedtodecreasedsRNA 17.Blango,M.G.,andBass,B.L.(2016).Identificationofthelong,edited
asatherapeuticmeanstotreatneuroinflammatorydisease.116 dsRNAomeofLPS-stimulatedimmunecells.GenomeRes.26,852–862.
Therapies that shift the balance away from dsRNA sensors
18.Sommer,B.,Ko¨hler,M.,Sprengel,R.,andSeeburg,P.H.(1991).RNAed-
may be beneficial for many autoimmune disorders that arise itinginbraincontrolsadeterminantofionflowinglutamate-gatedchan-
fromaberrantsensingofdsRNA.6 nels.Cell67,11–19.
19.Morse,D.P.,andBass,B.L.(1999).LongRNAhairpinsthatcontainino-
ACKNOWLEDGMENTS sineare presentinCaenorhabditiseleganspoly(A)+RNA.Proc.Natl.
Acad.Sci.USA96,6048–6053.
ThisworkwassupportedbyfundingtoK.A.C.fromtheNationalInstituteon 20.Morse,D.P.,Aruscavage,P.J.,andBass,B.L.(2002).RNAhairpinsin
Minority Healthand Health Disparities (R00MD016946) and to B.L.B. from noncodingregionsofhumanbrainandCaenorhabditiselegansmRNA
theNationalInstituteofGeneralMedicalSciences(R35GM141262)andthe are edited by adenosine deaminases that act on RNA. Proc. Natl.
NationalCancerInstituteoftheNationalInstitutesofHealth(R01CA260414). Acad.Sci.USA99,7906–7911.
21.Eisenberg,E.,Li,J.B.,andLevanon,E.Y.(2010).Sequencebasediden-
DECLARATIONOFINTERESTS tificationofRNAeditingsites.RNABiol.7,248–252.
22.Ramaswami,G.,andLi,J.B.(2016).IdentificationofhumanRNAediting
Theauthorsdeclarenocompetinginterests.
sites:Ahistoricalperspective.Methods107,42–47.
REFERENCES 23.Reich, D.P., and Bass, B.L. (2019). Mapping the dsRNA world. Cold
SpringHarb.Perspect.Biol.11,a035352.
1.Ehrenfeld,E.,andHunt,T.(1971).Double-strandedpoliovirusRNAin- 24.Schaffer,A.A.,andLevanon,E.Y.(2021).ALUA-to-IRNAediting:millions
hibitsinitiationofproteinsynthesisbyreticulocytelysates.Proc.Natl. ofsitesandmanyopenquestions.MethodsMol.Biol.2181,149–162.
Acad.Sci.USA68,1075–1078.
25.Erdmann,E.A.,Mahapatra,A.,Mukherjee,P.,Yang,B.,andHundley,
2.Hunt,T.,andEhrenfeld,E.(1971).Cytoplasmfrompoliovirus-infected H.A.(2021).Toprotectandmodifydouble-strandedRNA-thecritical
HeLa Cells inhibits Cell-free haemoglobin Synthesis. Nat. New Biol. rolesofADARsindevelopment,immunityandoncogenesis.Crit.Rev.
230,91–94. Biochem.Mol.Biol.56,54–87.
MolecularCell84,January4,2024 115
ll
Review
26. Macbeth,M.R.,Schubert,H.L.,Vandemark,A.P.,Lingam,A.T.,Hill,C.P., 44.Eggington,J.M.,Greene,T.,andBass,B.L.(2011).Predictingsitesof
andBass,B.L.(2005).InositolhexakisphosphateisboundintheADAR2 ADAReditingindouble-strandedRNA.Nat.Commun.2,319.
coreandrequiredforRNAediting.Science309,1534–1539.
45.Kleinova,R.,Rajendra,V.,Leuchtenberger,A.F.,LoGiudice,C.,Vesely,
27. Mannion,N.M.,Greenwood,S.M.,Young,R.,Cox,S.,Brindle,J.,Read, C.,Kapoor,U.,Tanzer,A.,Derdak,S.,Picardi,E.,andJantsch,M.F.
D.,Nella˚ker,C.,Vesely,C.,Ponting,C.P.,McLaughlin,P.J.,etal.(2014). (2023). The ADAR1 editome reveals drivers of editing-specificity for
TheRNA-editingenzymeADAR1controlsinnateimmuneresponsesto ADAR1-isoforms.NucleicAcidsRes.51,4191–4207.
RNA.CellRep.9,1482–1494.
46.Melcher,T.,Maas,S.,Herb,A.,Sprengel,R.,Seeburg,P.H.,andHiguchi,
28. Pestal,K.,Funk,C.C.,Snyder,J.M.,Price,N.D.,Treuting,P.M.,andStet- M.(1996).AmammalianRNAeditingenzyme.Nature379,460–464.
son,D.B.(2015).IsoformsofRNA-editingenzymeADAR1independently
controlnucleicacidsensorMDA5-drivenautoimmunityandmulti-organ 47.Higuchi,M.,Maas,S.,Single,F.N.,Hartner,J.,Rozov,A.,Burnashev,N.,
development.Immunity43,933–944. Feldmeyer,D.,Sprengel,R.,andSeeburg,P.H.(2000).Pointmutationin
anAMPAreceptorgenerescueslethalityinmicedeficientintheRNA-ed-
29. Liddicoat,B.J.,Piskol,R.,Chalk,A.M.,Ramaswami,G.,Higuchi,M., itingenzymeADAR2.Nature406,78–81.
Hartner,J.C.,Li,J.B.,Seeburg,P.H.,andWalkley,C.R.(2015).RNAedit-
ingbyADAR1preventsMDA5sensingofendogenousdsRNAasnonself. 48.Chalk,A.M.,Taylor,S.,Heraud-Farlow,J.E.,andWalkley,C.R.(2019).
Science349,1115–1120. ThemajorityofA-to-IRNAeditingisnotrequiredformammalianhomeo-
stasis.GenomeBiol.20,268.
30. Maurano,M.,Snyder,J.M.,Connelly,C.,Henao-Mejia,J.,Sidrauski,C.,
and Stetson, D.B. (2021). Protein kinase R and the integrated stress 49.Chen,C.X.,Cho,D.S.,Wang,Q.,Lai,F.,Carter,K.C.,andNishikura,K.
response drive immunopathology caused by mutations in the RNA (2000).AthirdmemberoftheRNA-specificadenosinedeaminasegene
deaminaseADAR1.Immunity54,1948–1960.e5. family,ADAR3,containsbothsingle-anddouble-strandedRNAbinding
domains.RNA6,755–767.
31. George,C.X.,Ramaswami,G.,Li,J.B.,andSamuel,C.E.(2016).Editing
ofcellularself-RNAsbyadenosinedeaminaseADAR1suppressesinnate 50.Melcher,T.,Maas,S.,Herb,A.,Sprengel,R.,Higuchi,M.,andSeeburg,
immunestressresponses.J.Biol.Chem.291,6158–6168. P.H.(1996).RED2,abrain-specificmemberoftheRNA-specificadeno-
sinedeaminasefamily.J.Biol.Chem.271,31795–31798.
32. Chung,H.,Calis,J.J.A.,Wu,X.,Sun,T.,Yu,Y.,Sarbanes,S.L.,DaoThi,
V.L.,Shilvock,A.R.,Hoffmann,H.H.,Rosenberg,B.R.,etal.(2018).Hu- 51.Mladenova, D.,Barry, G.,Konen,L.M.,Pineda, S.S., Guennewig, B.,
man ADAR1 prevents endogenous RNA from triggering translational Avesson, L., Zinn, R., Schonrock, N., Bitar, M., Jonkhout, N., et al.
shutdown.Cell172,811–824.e14. (2018).Adar3isinvolvedinlearningandmemoryinmice.Front.Neurosci.
12,243.
33. Kung,C.P.,Cottrell,K.A.,Ryu,S.,Bramel,E.R.,Kladney,R.D.,Bao,E.A.,
Freeman,E.C.,Sabloak,T.,Maggi,L.,Jr.,andWeber,J.D.(2021).Eval- 52.RaghavaKurup,R.,Oakes,E.K.,Vadlamani,P.,Nwosu,O.,Danthi,P.,
uatingthetherapeuticpotentialofADAR1inhibitionfortriple-negative andHundley,H.A.(2022).ADAR3activatesNF-kBsignalingandpro-
breastcancer.Oncogene40,189–202. motes glioblastoma cell resistance to temozolomide. Sci. Rep.
12,13362.
34. Gannon,H.S.,Zou,T.,Kiessling,M.K.,Gao,G.F.,Cai,D.,Choi,P.S.,
Ivan,A.P.,Buchumenski,I.,Berger,A.C.,Goldstein,J.T.,etal.(2018). 53.RaghavaKurup,R.,Oakes,E.K.,Manning,A.C.,Mukherjee,P.,Vadla-
IdentificationofADAR1adenosinedeaminasedependencyinasubset mani,P.,andHundley,H.A.(2022).RNAbindingbyADAR3inhibitsaden-
ofcancercells.Nat.Commun.9,5450. osine-to-inosineeditingandpromotesexpressionofimmuneresponse
proteinMAVS.J.Biol.Chem.298,102267.
35. Liu,H.,Golji,J.,Brodeur,L.K.,Chung,F.S.,Chen,J.T.,deBeaumont,
R.S.,Bullock,C.P.,Jones,M.D.,Kerr,G.,Li,L.,etal.(2019).Tumor- 54.Tian,B.,Bevilacqua,P.C.,Diegelman-Parente,A.,andMathews,M.B.
derivedIFNtriggerschronicpathwayagonismandsensitivitytoADAR (2004). The double-stranded-RNA-binding motif: interference and
loss.Nat.Med.25,95–102. muchmore.Nat.Rev.Mol.CellBiol.5,1013–1023.
36. Pfaller,C.K.,Donohue,R.C.,Nersisyan,S.,Brodsky,L.,andCattaneo,R. 55.Masliah,G.,Barraud,P.,andAllain,F.H.(2013).RNArecognitionbydou-
(2018).Extensiveeditingofcellularandviraldouble-strandedRNAstruc- ble-strandedRNAbindingdomains:amatterofshapeandsequence.
turesaccountsforinnateimmunitysuppressionandtheproviralactivity Cell.Mol.LifeSci.70,1875–1895.
ofADAR1p150.PLoSBiol.16,e2006577.
56.Hsiao,Y.E.,Bahn,J.H.,Yang,Y.,Lin,X.,Tran,S.,Yang,E.W.,Quinones-
37. Sun,T.,Yu,Y.,Wu,X.,Acevedo,A.,Luo,J.D.,Wang,J.,Schneider, Valdez,G.,andXiao,X.(2018).RNAeditinginnascentRNAaffectspre-
W.M.,Hurwitz,B.,Rosenberg,B.R.,Chung,H.,etal.(2021).Decoupling mRNAsplicing.GenomeRes.28,812–823.
expressionandeditingpreferencesofADAR1p150andp110isoforms.
Proc.Natl.Acad.Sci.USA118,e2021757118. 57.Bentley, D.L.(2014).CouplingmRNAprocessingwithtranscriptionin
timeandspace.Nat.Rev.Genet.15,163–175.
38. George,C.X.,andSamuel,C.E.(1999).HumanRNA-specificadenosine
deaminaseADAR1transcriptspossessalternativeexon1structuresthat 58.Quin,J.,Sedmı´k,J.,Vukic(cid:1),D.,Khan,A.,Keegan,L.P.,andO’Connell,
initiatefromdifferentpromoters,oneconstitutivelyactiveandtheother M.A.(2021).ADARRNAmodifications,theepitranscriptomeandinnate
interferoninducible.Proc.Natl.Acad.Sci.USA96,4621–4626. immunity.TrendsBiochem.Sci.46,758–771.
39. Herbert,A.(2021).To"Z"ornotto"Z":Z-RNA,self-recognition,andthe 59.Fritz,J.,Strehblow,A.,Taschner,A.,Schopoff,S.,Pasierbek,P.,and
MDA5helicase.PLoSGenet.17,e1009513. Jantsch, M.F. (2009). RNA-regulated interaction of transportin-1 and
exportin-5withthedouble-strandedRNA-bindingdomainregulatesnu-
40. Athanasiadis,A.,Placido,D.,Maas,S.,Brown,B.A.,2nd,Lowenhaupt, cleocytoplasmicshuttlingofADAR1.Mol.Cell.Biol.29,1487–1497.
K.,andRich,A.(2005).ThecrystalstructureoftheZbetadomainofthe
RNA-editingenzymeADAR1revealsdistinctconservedsurfacesamong 60.Kim,J.I.,Nakahama,T.,Yamasaki,R.,CostaCruz,P.H.,Vongpipatana,
Z-domains.J.Mol.Biol.351,496–507. T.,Inoue,M.,Kanou,N.,Xing,Y.,Todo,H.,Shibuya,T.,etal.(2021).RNA
editingatalimitednumberofsitesissufficienttopreventMDA5activa-
41. Kuttan,A.,andBass,B.L.(2012).Mechanisticinsightsintoediting-site tioninthemousebrain.PLoSGenet.17,e1009516.
specificityofADARs.Proc.Natl.Acad.Sci.USA109,E3295–E3304.
61.Rice,G.I.,Kasher,P.R.,Forte,G.M.,Mannion,N.M.,Greenwood,S.M.,
42. Matthews,M.M.,Thomas,J.M.,Zheng,Y.,Tran,K.,Phelps,K.J.,Scott, Szynkiewicz,M.,Dickerson,J.E.,Bhaskar,S.S.,Zampini,M.,Briggs,
A.I.,Havel,J.,Fisher,A.J.,andBeal,P.A.(2016).Structuresofhuman T.A., et al. (2012). Mutations in ADAR1 cause Aicardi-Goutieres syn-
ADAR2boundtodsRNArevealbase-flippingmechanismandbasisfor drome associated with a type I interferon signature. Nat. Genet. 44,
siteselectivity.Nat.Struct.Mol.Biol.23,426–433. 1243–1248.
43. Wong,S.K.,Sato,S.,andLazinski,D.W.(2001).Substraterecognitionby 62.de Reuver, R., and Maelfait, J. (2023). Novel insights into double-
ADAR1andADAR2.RNA7,846–858. strandedRNA-mediatedimmunopathology.Nat.Rev.Immunol.
116 MolecularCell84,January4,2024
ll
Review
63.Wang,Q.,Miyakoda,M.,Yang,W.,Khillan,J.,Stachura,D.L.,Weiss, 79.Kariko´,K.,Buckstein,M.,Ni,H.,andWeissman,D.(2005).Suppression
M.J., and Nishikura, K. (2004). Stress-induced apoptosis associated ofRNArecognitionbytoll-likereceptors:theimpactofnucleosidemodi-
with null mutation of ADAR1 RNA editing deaminase gene. J. Biol. ficationandtheevolutionaryoriginofRNA.Immunity23,165–175.
Chem.279,4952–4961.
80.Garg,G.,Dienemann,C.,Farnung,L.,Schwarz,J.,Linden,A.,Urlaub,H.,
64.Hartner,J.C.,Walkley,C.R.,Lu,J.,andOrkin,S.H.(2009).ADAR1is andCramer,P.(2023).Structuralinsightsintohumanco-transcriptional
essentialforthemaintenanceofhematopoiesisandsuppressionofinter- capping.Mol.Cell83,2464–2477.e5.
feronsignaling.Nat.Immunol.10,109–115.
81.Devarkar,S.C.,Wang,C.,Miller,M.T.,Ramanathan,A.,Jiang,F.,Khan,
A.G.,Patel,S.S.,andMarcotrigiano,J.(2016).Structuralbasisform7G
65.Hu,S.B.,Heraud-Farlow,J.,Sun,T.,Liang,Z.,Goradia,A.,Taylor,S., recognitionand20-O-methyldiscriminationincappedRNAsbytheinnate
Walkley, C.R., and Li, J.B. (2023). ADAR1p150 prevents MDA5 and
immunereceptorRIG-I.Proc.Natl.Acad.Sci.USA113,596–601.
PKRactivationviadistinctmechanismstoavertfatalautoinflammation.
Mol.Cell83,3869–3884.e7.
82.Nicholson, A.W. (2014). Ribonuclease III mechanisms of double-
strandedRNAcleavage.WileyInterdiscip.Rev.RNA5,31–48.
66.Sinigaglia,K.,Cherian,A.,Vukic,D.,Melicherova,J.,Linhartova,P.,Du,
Q.,Zerad,L.,Stejskal,S.,Malik,R.,Prochazka,J.,etal.(2023).Aberrant 83.Burger,K.,andGullerova,M.(2015).Swissarmyknives:non-canonical
activationoftheinnateimmunesensorPKRbyselfdsRNAisprevented functions of nuclear Drosha and Dicer. Nat. Rev. Mol. Cell Biol. 16,
bydirectinteractionwithADAR1.PreprintatbioRxiv. 417–430.
67.Tang, Q., Rigby, R.E., Young, G.R., Hvidt, A.K., Davis, T., Tan, T.K., 84.White,E.,Schlackow,M.,Kamieniarz-Gdula,K.,Proudfoot,N.J.,and
Bridgeman, A., Townsend, A.R., Kassiotis, G., and Rehwinkel, J. Gullerova,M.(2014).HumannuclearDicerrestrictsthedeleteriousaccu-
(2021).Adenosine-to-inosineeditingofendogenousZ-formRNAbythe mulationofendogenousdouble-strandedRNA.Nat.Struct.Mol.Biol.21,
deaminaseADAR1preventsspontaneousMAVS-dependenttypeIinter- 552–559.
feronresponses.Immunity54,1961–1975.e5.
85.Kim, B., Jeong, K., and Kim, V.N. (2017). Genome-wide mapping of
68.Nakahama,T.,Kato,Y.,Shibuya,T.,Inoue,M.,Kim,J.I.,Vongpipatana, DROSHAcleavagesitesonprimarymicroRNAsandnoncanonicalsub-
T.,Todo,H.,Xing,Y.,andKawahara,Y.(2021).Mutationsintheadeno- strates.Mol.Cell66,258–269.e5.
sinedeaminaseADAR1thatpreventendogenousZ-RNAbindinginduce
Aicardi-Goutieres-syndrome-likeencephalopathy.Immunity54,1976– 86.Lingaraju,M.,Schuller,J.M.,Falk,S.,Gerlach,P.,Bonneau,F.,Basquin,
J.,Benda,C.,andConti,E.(2019).Toprocessortodecay:Amechanistic
1988.e7.
viewofthenuclearRNAexosome.ColdSpringHarb.Symp.Quant.Biol.
84,155–163.
69.deReuver,R.,Verdonck,S.,Dierick,E.,Nemegeer,J.,Hessmann,E.,
Ahmad, S., Jans, M., Blancke, G., Van Nieuwerburgh, F., Botzki, A.,
87.Weick,E.M.,andLima,C.D.(2021).RNAhelicasesarehubsthatorches-
etal.(2022).ADAR1preventsautoinflammationbysuppressingsponta- trate exosome-dependent 30-50 decay. Curr. Opin. Struct. Biol.
neousZBP1activation.Nature607,784–789.
67,86–94.
70.Jiao,H.,Wachsmuth,L.,Wolf,S.,Lohmann,J.,Nagata,M.,Kaya,G.G., 88.Macias, S., Cordiner, R.A., Gautier, P., Plass, M., and Ca´ceres, J.F.
Oikonomou,N.,Kondylis,V.,Rogg,M.,Diebold,M.,etal.(2022).ADAR1 (2015).DGCR8actsasanadaptorfortheexosomecomplextodegrade
avertsfataltypeIinterferoninductionbyZBP1.Nature607,776–783. double-strandedstructuredRNAs.Mol.Cell60,873–885.
71.Martinez,N.M.,Su,A.,Burns,M.C.,Nussbacher,J.K.,Schaening,C., 89.Zhang,Z.,andCarmichael,G.G.(2001).ThefateofdsRNAinthenu-
Sathe,S.,Yeo,G.W.,andGilbert,W.V.(2022).Pseudouridinesynthases cleus:ap54(nrb)-containingcomplexmediatesthenuclearretentionof
modifyhumanpre-mRNAco-transcriptionallyandaffectpre-mRNApro- promiscuouslyA-to-IeditedRNAs.Cell106,465–475.
cessing.Mol.Cell82,645–659.e9.
90.Kumar,M.,andCarmichael,G.G.(1997).NuclearantisenseRNAinduces
72.Sun,H.,Li,K.,Liu,C.,andYi,C.(2023).Regulationandfunctionsofnon- extensiveadenosinemodificationsandnuclearretentionoftargettran-
m6AmRNAmodifications.Nat.Rev.Mol.CellBiol.24,714–731. scripts.Proc.Natl.Acad.Sci.USA94,3542–3547.
91.Hundley,H.A.,Krauchuk,A.A.,andBass,B.L.(2008).C.elegansandH.
73.Ke,S.,Pandya-Jones,A.,Saito,Y.,Fak,J.J.,Va˚gbø,C.B.,Geula,S., sapiensmRNAswithedited30UTRsarepresentonpolysomes.RNA14,
Hanna, J.H., Black, D.L., Darnell, J.E., Jr., and Darnell, R.B. (2017).
m6AmRNAmodificationsaredepositedinnascentpre-mRNAandare 2050–2060.
not required for splicing but do specify cytoplasmic turnover. Genes 92.McCluggage, F., and Fox, A.H. (2021). Paraspeckle nuclear conden-
Dev.31,990–1006.
sates:globalsensorsofcellstress?BioEssays43,e2000245.
74.Wang,Z.,Pan,Z.,Adhikari,S.,Harada,B.T.,Shen,L.,Yuan,W.,Abey- 93.Fox, A.H., Nakagawa, S., Hirose, T., and Bond, C.S. (2018). Para-
wardana,T.,Al-Hadid,Q.,Stark,J.M.,He,C.,etal.(2021).m6Adeposi- speckles:wherelongnoncodingRNAmeetsphaseseparation.Trends
tionisregulatedbyPRMT1-mediatedargininemethylationofMETTL14in Biochem.Sci.43,124–135.
itsdisorderedC-terminalregion.EMBOJ.40,e106309.
94.Hu,S.B.,Xiang,J.F.,Li,X.,Xu,Y.,Xue,W.,Huang,M.,Wong,C.C.,Sa-
75.Huang,H.,Weng,H.,Zhou,K.,Wu,T.,Zhao,B.S.,Sun,M.,Chen,Z., gum,C.A.,Bedford,M.T.,Yang,L.,etal.(2015).Proteinargininemethyl-
Deng,X.,Xiao,G.,Auer,F.,etal.(2019).HistoneH3trimethylationat transferaseCARM1attenuatestheparaspeckle-mediatednuclearreten-
lysine 36 guides m6A RNA modification co-transcriptionally. Nature tionofmRNAscontainingIRAlus.GenesDev.29,630–645.
567,414–419.
95.Elbarbary,R.A.,Li,W.,Tian,B.,andMaquat,L.E.(2013).STAU1binding
76.Gao,Y.,Vasic,R.,Song,Y.,Teng,R.,Liu,C.,Gbyli,R.,Biancon,G.,Ne-
30UTRIRAluscomplementsnuclearretentiontoprotectcellsfromPKR-
lakanti,R.,Lobben,K.,Kudo,E.,etal.(2020).m6Amodificationprevents mediatedtranslationalshutdown.GenesDev.27,1495–1510.
formationofendogenousdouble-strandedRNAsanddeleteriousinnate
96.Chen,L.L.,DeCerbo,J.N.,andCarmichael,G.G.(2008).Aluelement-
immune responses during hematopoietic development. Immunity 52,
mediatedgenesilencing.EMBOJ.27,1694–1705.
1007–1021.e8.
97.Khan,M.,Hou,S.,Chen,M.,andLei,H.(2023).MechanismsofRNA
77.Nance,K.D.,andMeier,J.L.(2021).Modificationsinanemergency:the exportandnuclearretention.WileyInterdiscip.Rev.RNA14,e1755.
roleofN1-MethylpseudouridineinCOVID-19vaccines.ACSCent.Sci.7,
748–756. 98.Lund,E.,Gu€ttinger,S.,Calado,A.,Dahlberg,J.E.,andKutay,U.(2004).
NuclearexportofmicroRNAprecursors.Science303,95–98.
78.Nelson,J.,Sorensen,E.W.,Mintri,S.,Rabideau,A.E.,Zheng,W.,Besin,
G.,Khatwani,N.,Su,S.V.,Miracco,E.J.,Issa,W.J.,etal.(2020).Impact 99.Brownawell,A.M.,andMacara,I.G.(2002).Exportin-5,anovelkaryo-
ofmRNAchemistryandmanufacturingprocessoninnateimmuneacti- pherin,mediatesnuclearexportofdouble-strandedRNAbindingpro-
vation.Sci.Adv.6,eaaz6893. teins.J.CellBiol.156,53–64.
MolecularCell84,January4,2024 117
ll
Review
100. Kim,Y.,Lee,J.H.,Park,J.E.,Cho,J.,Yi,H.,andKim,V.N.(2014).PKRis 119.Li,W.X.,andDing,S.W.(2022).MammalianviralsuppressorsofRNA
activatedbycellulardsRNAsduringmitosisandactsasamitoticregu- interference.TrendsBiochem.Sci.47,978–988.
lator.GenesDev.28,1310–1322.
120.Ye,C.,Jia,L.,Sun,Y.,Hu,B.,Wang,L.,Lu,X.,andZhou,J.(2014).Inhi-
101. Burke,J.M.,Gilchrist,A.R.,Sawyer,S.L.,andParker,R.(2021).RNaseL bitionofantiviralinnateimmunitybybirnavirusVP3proteinviablockage
limitshostandviralproteinsynthesisviainhibitionofmRNAexport.Sci. ofviraldouble-strandedRNAbindingtothehostcytoplasmicRNAdetec-
Adv.7,eabh2479. torMDA5.J.Virol.88,11154–11165.
102. Burger,K.,Schlackow,M.,Potts,M.,Hester,S.,Mohammed,S.,and 121.Liu,Z.,Wang,J.,Cheng,H.,Ke,X.,Sun,L.,Zhang,Q.C.,andWang,H.W.
Gullerova,M.(2017).NuclearphosphorylatedDicerprocessesdouble- (2018).Cryo-EMstructureofhumandiceranditscomplexeswithaPre-
strandedRNAinresponsetoDNAdamage.J.CellBiol.216,2373–2389. miRNAsubstrate.Cell173,1191–1203.e12.
103. Kim,M.S.,Pinto,S.M.,Getnet,D.,Nirujogi,R.S.,Manda,S.S.,Chaer- 122.Motz,C.,Schuhmann,K.M.,Kirchhofer,A.,Moldt,M.,Witte,G.,Conzel-
kady, R., Madugundu, A.K., Kelkar, D.S., Isserlin, R., Jain, S., et al. mann,K.K.,andHopfner,K.P.(2013).ParamyxovirusVproteinsdisrupt
(2014).Adraftmapofthehumanproteome.Nature509,575–581. thefoldoftheRNAsensorMDA5toinhibitantiviralsignaling.Science
339,690–693.
104. Moreno, P., Fexova, S., George, N., Manning, J.R., Miao, Z., Mo-
hammed, S., Mun˜oz-Pomer, A., Fullgrabe, A., Bi, Y., Bush, N., et al. 123.Sakurai,M.,Shiromoto,Y.,Ota,H.,Song,C.,Kossenkov,A.V.,Wickra-
(2022).ExpressionAtlasupdate:geneandproteinexpressioninmultiple masinghe, J., Showe, L.C., Skordalakes, E., Tang, H.Y., Speicher,
species.NucleicAcidsRes.50,D129–D140. D.W.,andNishikura,K.(2017).ADAR1controlsapoptosisofstressed
cells by inhibiting Staufen1-mediated mRNA decay. Nat. Struct. Mol.
105. Lee,H.Y.,Zhou,K.,Smith,A.M.,Noland,C.L.,andDoudna,J.A.(2013). Biol.24,534–543.
DifferentialrolesofhumanDicer-binding proteinsTRBPandPACTin
smallRNAprocessing.NucleicAcidsRes.41,6568–6576. 124.Cottrell,K.A.,Ryu,S.,Torres,L.S.,Schab,A.M.,andWeber,J.D.(2023).
InductionofviralmimicryuponlossofDHX9andADAR1inbreastcancer
106. Ha,M.,andKim,V.N.(2014).RegulationofmicroRNAbiogenesis.Nat. cells.PreprintatbioRxiv.
Rev.Mol.CellBiol.15,509–524.
125.Nourreddine,S.,Lavoie,G.,Paradis,J.,BenElKadhi,K.,Me´ant,A.,Au-
107. Kim,Y.K.,andMaquat,L.E.(2019).UPFrontandcenterinRNAdecay: bert,L.,Grondin,B.,Gendron,P.,Chabot,B.,Bouvier,M.,etal.(2020).
UPF1 in nonsense-mediated mRNA decay and beyond. RNA 25, NF45 and NF90 regulate mitotic gene expression by competing with
407–422. Staufen-mediatedmRNAdecay.CellRep.31,107660.
126.Schmidt,T.,Knick,P.,Lilie,H.,Friedrich,S.,Golbik,R.P.,andBehrens,
108. Kim,Y.K.,Furic,L.,Parisien,M.,Major,F.,DesGroseillers,L.,andMa-
S.E.(2017).ThepropertiesoftheRNA-bindingproteinNF90areconsid-
quat,L.E.(2007).Staufen1regulatesdiverseclassesofmammaliantran-
erablymodulatedbycomplexformationwithNF45.Biochem.J.474,
scripts.EMBOJ.26,2670–2681.
259–280.
109. Gong,C.,andMaquat,L.E.(2011).lncRNAstransactivateSTAU1-medi-
atedmRNAdecaybyduplexingwith30UTRsviaAluelements.Nature 127.Ota,H.,Sakurai,M.,Gupta,R.,Valente,L.,Wulff,B.E.,Ariyoshi,K.,Ii-
zasa,H.,Davuluri,R.V.,andNishikura,K.(2013).ADAR1formsacom-
470,284–288.
plex with Dicer to promote microRNA processing and RNA-induced
genesilencing.Cell153,575–589.
110. Ricci,E.P.,Kucukural,A.,Cenik,C.,Mercier,B.C.,Singh,G.,Heyer,E.E.,
Ashar-Patel,A.,Peng,L.,andMoore,M.J.(2014).Staufen1sensesover-
128.Montavon,T.C.,Baldaccini,M.,Lefe`vre,M.,Girardi,E.,Chane-Woon-
alltranscriptsecondarystructuretoregulatetranslation.Nat.Struct.Mol.
Ming, B., Messmer, M., Hammann, P., Chicher, J., and Pfeffer, S.
Biol.21,26–35.
(2021).HumanDICERhelicasedomainrecruitsPKRandmodulatesits
antiviralactivity.PLoSPathog.17,e1009549.
111. Ahmad,S.,Mu,X.,Yang,F.,Greenwald,E.,Park,J.W.,Jacob,E.,Zhang,
C.Z.,andHur,S.(2018).Breachingself-tolerancetoAluduplexRNAun-
129.Warf,M.B.,Shepherd,B.A.,Johnson,W.E.,andBass,B.L.(2012).Ef-
derliesMDA5-mediatedinflammation.Cell172,797–810.e13.
fects of ADARs on small RNA processing pathways in C. elegans.
GenomeRes.22,1488–1498.
112. Barak,M.,Porath,H.T.,Finkelstein,G.,Knisbacher,B.A.,Buchumenski,
I.,Roth,S.H.,Levanon,E.Y.,andEisenberg,E.(2020).Purifyingselection 130.Heale,B.S.,Keegan,L.P.,McGurk,L.,Michlewski,G.,Brindle,J.,Stan-
oflongdsRNAisthefirstlineofdefenseagainstfalseactivationofinnate ton,C.M.,Caceres,J.F.,andO’Connell,M.A.(2009).Editingindependent
immunity.GenomeBiol.21,26. effects of ADARs on the miRNA/siRNA pathways. EMBO J. 28,
3145–3156.
113. Sun,T.,Li,Q.,Geisinger,J.M.,Hu,S.-B.,Fan,B.,Su,S.,Tsui,W.,Guo,
H.,Ma,J.,andLi,J.B.(2022).AsmallsubsetofcytosolicdsRNAsmust 131.Deng,P.,Khan,A.,Jacobson,D.,Sambrani,N.,McGurk,L.,Li,X.,Jayas-
beEditedbyADAR1toevadeMDA5-mediatedautoimmunity.Preprintat ree,A.,Hejatko,J.,Shohat-Ophir,G.,O’Connell,M.A.,etal.(2020).Adar
bioRxiv. RNAediting-dependentand-independenteffectsarerequiredforbrain
andinnateimmunefunctionsinDrosophila.Nat.Commun.11,1580.
114. Kim,Y.,Park,J.,Kim,S.,Kim,M.,Kang,M.G.,Kwak,C.,Kang,M.,Kim,
B.,Rhee,H.W.,andKim,V.N.(2018).PKRsensesnuclearandmitochon- 132.Chen,T.,Xiang,J.F.,Zhu,S.,Chen,S.,Yin,Q.F.,Zhang,X.O.,Zhang,J.,
drialsignalsbyinteractingwithendogenousdouble-strandedRNAs.Mol. Feng,H.,Dong,R.,Li,X.J.,etal.(2015).ADAR1isrequiredfordifferen-
Cell71,1051–1063.e6. tiationandneuralinductionbyregulatingmicroRNAprocessinginacata-
lyticallyindependentmanner.CellRes.25,459–476.
115. Young,P.G.,andAttardi,G.(1975).Characterizationofdouble-stranded
RNAfromHeLacellmitochondria.Biochem.Biophys.Res.Commun.65, 133.Reich,D.P.,Tyc,K.M.,andBass,B.L.(2018).C.elegansADARsantag-
1201–1207. onizesilencingofcellulardsRNAsbytheantiviralRNAipathway.Genes
Dev.32,271–282.
116. Dorrity,T.J.,Shin,H.,Wiegand,K.A.,Aruda,J.,Closser,M.,Jung,E.,
Gertie, J.A., Leone, A., Polfer, R., Culbertson, B., et al. (2023). Long 134.Keegan,L.P.,McGurk,L.,Palavicini,J.P.,Brindle,J.,Paro,S.,Li,X.,
30UTRspredisposeneuronstoinflammationbypromotingimmunosti- Rosenthal,J.J.,andO’Connell,M.A.(2011).Functionalconservationin
mulatorydouble-strandedRNAformation.Sci.Immunol.8,eadg2979. human and Drosophila of Metazoan ADAR2 involved in RNA editing:
lossofADAR1ininsects.NucleicAcidsRes.39,7249–7262.
117. Langland,J.O.,Cameron,J.M.,Heck,M.C.,Jancovich,J.K.,andJa-
cobs, B.L. (2006). Inhibition of PKR by RNA and DNA viruses. Virus 135.Corbet,G.A.,Burke,J.M.,Bublitz,G.R.,Tay,J.W.,andParker,R.(2022).
Res.119,100–110. dsRNA-inducedcondensationofantiviralproteinsmodulatesPKRactiv-
ity.Proc.Natl.Acad.Sci.USA119,e2204235119.
118. Zinzula,L.,andTramontano,E.(2013).Strategiesofhighlypathogenic
RNA viruses to block dsRNA detection by RIG-I-like receptors: hide, 136.Zappa,F.,Muniozguren,N.L.,Wilson,M.Z.,Costello,M.S.,Ponce-Ro-
mask,hit.AntiviralRes.100,615–635. jas,J.C.,andAcosta-Alvear,D.(2022).Signalingbytheintegratedstress
118 MolecularCell84,January4,2024
ll
Review
responsekinasePKRisfine-tunedbydynamicclustering.J.CellBiol. 145.Cuellar,T.L.,Herzner,A.M.,Zhang,X.,Goyal,Y.,Watanabe,C.,Fried-
221,e202111100. man,B.A.,Janakiraman,V.,Durinck,S.,Stinson,J.,Arnott,D.,etal.
(2017).SilencingofretrotransposonsbySETDB1inhibitstheinterferon
137.Joyce,G.F.,andSzostak,J.W.(2018).ProtocellsandRNAself-replica- responseinacutemyeloidleukemia.J.CellBiol.216,3535–3549.
tion.ColdSpringHarb.Perspect.Biol.10,a034801.
146.Tunbak,H.,Enriquez-Gasca,R.,Tie,C.H.C.,Gould,P.A.,Mlcochova,P.,
138.Wang,X.,Vukovic,L.,Koh,H.R.,Schulten,K.,andMyong,S.(2015).Dy- Gupta,R.K.,Fernandes,L.,Holt,J.,vanderVeen,A.G.,Giampazolias,
namicprofilingofdouble-strandedRNAbindingproteins.NucleicAcids E.,etal.(2020).TheHUSHcomplexisagatekeeperoftypeIinterferon
Res.43,7566–7576. throughepigeneticregulationofLINE-1s.Nat.Commun.11,5387.
139.Hough,R.F.,andBass,B.L.(1994).PurificationoftheXenopuslaevis 147.Bowling,E.A.,Wang,J.H.,Gong,F.,Wu,W.,Neill,N.J.,Kim,I.S.,Tyagi,
double-stranded RNA adenosine deaminase. J. Biol. Chem. 269,
S.,Orellana,M.,Kurley,S.J.,Dominguez-Vidan˜a,R.,etal.(2021).Spli-
9933–9939. ceosome-targetedtherapiestriggeranantiviralimmuneresponseintri-
ple-negativebreastcancer.Cell184,384–403.e21.
140.Kostura,M.,andMathews,M.B.(1989).Purificationandactivationofthe
148.Zheng,R.,Dunlap,M.,Lyu,J.,Gonzalez-Figueroa,C.,Bobkov,G.,Har-
double-stranded RNA-dependenteIF-2kinaseDAI. Mol.Cell.Biol.9,
vey,S.E.,Chan,T.W.,Quinones-Valdez,G.,Choudhury,M.,Vuong,A.,
1576–1586.
etal.(2023).LINE-associatedcrypticsplicinginducesdsRNA-mediated
interferonresponseandtumorimmunity.PreprintatbioRxiv.
141.Roulois,D.,LooYau,H.,Singhania,R.,Wang,Y.,Danesh,A.,Shen,S.Y.,
Han,H.,Liang,G.,Jones,P.A.,Pugh,T.J.,etal.(2015).DNA-demethylat-
149.Wu,Y.,Zhao,W.,Liu,Y.,Tan,X.,Li,X.,Zou,Q.,Xiao,Z.,Xu,H.,Wang,Y.,
ingagentstargetcolorectalcancercellsbyinducingviralmimicryby
andYang,X.(2018).FunctionofHNRNPCinbreastcancercellsbycon-
endogenoustranscripts.Cell162,961–973. trollingthedsRNA-inducedinterferonresponse.EMBOJ.37,e99017.
142.Ishizuka,J.J.,Manguso,R.T.,Cheruiyot,C.K.,Bi,K.,Panda,A.,Iracheta- 150.Zou, T., Zhou, M., Gupta, A., Zhuang, P., Fishbein, A.R., Wei, H.Y.,
Vellve,A.,Miller,B.C.,Du,P.P.,Yates,K.B.,Dubrot,J.,etal.(2019).Loss Zhang,Z.,Cherniack,A.D.,andMeyerson,M.(2023).XRN1deletionin-
of ADAR1 in tumours overcomes resistance to immune checkpoint ducesPKR-dependentcelllethalityininterferon-activatedcancercells.
blockade.Nature565,43–48. bioRxiv.
143.Mehdipour,P.,Marhon,S.A.,Ettayebi,I.,Chakravarthy,A.,Hosseini,A., 151.Hosseini, A., Lindholm, H.T., Chen, R., Mehdipour, P., Marhon, S.A.,
Wang,Y.,deCastro,F.A.,LooYau,H.,Ishak,C.,Abelson,S.,etal. Ishak,C.A.,andDeCarvalho,D.D.(2023).Retroelementdecaybythe
(2020).EpigenetictherapyinducestranscriptionofinvertedSINEsand exonucleaseXRN1isaviralmimicrydependencyincancer.Preprintat
ADAR1dependency.Nature588,169–173. bioRxiv.
144.Chiappinelli,K.B.,Strissel,P.L.,Desrichard,A.,Li,H.,Henke,C.,Akman, 152.Chitrakar,A.,Solorio-Kirpichyan,K.,Prangley,E.,Rath,S.,Du,J.,and
B.,Hein,A.,Rote,N.S.,Cope,L.M.,Snyder,A.,etal.(2015).Inhibiting Korennykh, A. (2021). Introns encode dsRNAs undetected by RIG-I/
DNAmethylationcausesaninterferonresponseincancerviadsRNA MDA5/interferonsandsensedviaRNaseL.Proc.Natl.Acad.Sci.USA
includingendogenousretroviruses.Cell162,974–986. 118,e2102134118.
MolecularCell84,January4,2024 119
