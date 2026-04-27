---
source_path: /mnt/c/Users/Administrator/Zotero/storage/JX5465P2/Juszkiewicz和Hegde - 2018 - Quality Control of Orphaned Proteins.pdf
ingested: 2026-04-23
sha256: fc9c9a30d764e9ca
---

Molecular Cell
Review
Quality Control of Orphaned Proteins
SzymonJuszkiewicz1andRamanujanS.Hegde1,*
1MRCLaboratoryofMolecularBiology,CambridgeCB20QH,UK
*Correspondence:rhegde@mrc-lmb.cam.ac.uk
https://doi.org/10.1016/j.molcel.2018.07.001
Thebillionsofproteinsinsideaeukaryoticcellareorganizedamongdozensofsub-cellularcompartments,
withinwhichtheyarefurtherorganizedintoproteincomplexes.Themaintenanceofbothlevelsoforganiza-
tion is crucial for normal cellular function. Newly made proteins that fail to be segregated to the correct
compartmentorassembledintotheappropriatecomplexaredefinedasorphans.Inthisreview,wediscuss
the challenges faced by a cell of minimizing orphaned proteins, the quality control systems that recognize
orphans,andtheconsequencesofexcessorphansforproteinhomeostasisanddisease.
Introduction OrganizationoftheEukaryoticProteome
Theadventofmethodstoobservetheinteriorofcellsbyelectron Bioinformatictoolstopredictproteinlocationbasedonknown
microscopyinthe1950srevealedfar morecompartmentaliza- trafficking signals (Emanuelsson et al., 2007), together with
tionthanwasapparentpreviouslyusinglightmicroscopywithvi- increasingly thorough proteome-wide analytic tools (Itzhak
taldyesandstains(Porter,1955–1956).Thisledtothedefinition et al., 2016; Mulvey et al., 2017), provide estimates of how
of many membrane-bound organelles in the cell and our first many proteins are delivered to non-cytosolic destinations. In
views of many non-membrane-bound structures such as the parallel,systematicanalysesofproteincomplexes(Babuetal.,
ribosome (Palade, 1955). In parallel with direct visualization, 2012;Gavinetal.,2006;Kroganetal.,2006)andtheirrelative
biochemical fractionation was able to isolate these various abundances (Kulak et al., 2014) inform on what proportion of
morphologically identifiable structures (Claude, 1943, 1946). nascent proteins need additional assembly. These studies
Thestructuresweresoonshowntohavedistinctfunctions(De showthatthevastmajorityofnewlymadeproteinsaredestined
Duve,1965)andeventuallyassociatedwithspecificsubsetsof foradifferentlocation,assembledwithothercellularfactors,or
cellular proteins that are often part of larger complexes with both(Figure1).
definedcompositionandstoichiometry.Thesestudiesinitiated Ofthe20,341referenceproteinsofthehumangenome(Uni-
modern cell biology, a major goal of which is to understand ProtConsortium,2018),(cid:1)7,000aretargetedtotheendoplasmic
how intracellular organization is generated and maintained to reticulumforeventualresidenceintheendomembranesystem,
facilitatecellularfunction. nuclear envelope, plasma membrane, outside the cell, and
The most extensive efforts have been aimed at determining peroxisomal membrane. Approximately 1,000 proteins are
how newly made proteins are segregated to the appropriate destinedformitochondria,(cid:1)50fortheperoxisomallumen,and
organelle (Blobel, 1980; Wickner and Schekman, 2005). a relative handful for morespecialized structures such aslipid
Althoughtheaccuracyofintracellularproteintargetingwasusu- droplets.Around5,000proteinsoperateprimarilyinthenucleus,
allyassumedtobehigh,onecouldanticipatethatitcannotbe althoughtheentryandexitofmanyoftheseareoftendynamic
perfect.Asdetailedbelow,itisincreasinglyclearthattherecog- and regulated. Thus, (cid:1)65% of genes encode for proteins that
nition and disposal of mistargeted copies of a protein is an mustberecognizedforselectivetraffickingtoamembrane-en-
importantfacetofachievingeffectivenetsegregation.Similarly, closedcompartment(Figure1A).
theassemblyofproteinsintocomplexesislikelytobeimperfect Analysisofproteininteractionsbymassspectrometryacross
(HarperandBennett,2016),necessitatingthedegradationofun- theyeastproteome(Gavinetal.,2006;Kroganetal.,2006)indi-
assembledcomponents.Thus,thepromptdegradationofpro- catesthatoverhalfofallproteinsmaybeinstablemulti-protein
teins that fail to be correctly localized or assembled is critical complexes(Figure1B).Whiletheproportionissomewhatlessfor
tothemaintenanceofintracellularorganization.Werefertopro- membraneproteins(Babuetal.,2012),thismaybeduetothe
teinsthatareterminallyseparatedfromtheircorrectlocationor additional challenge of retaining interactions during detergent
partnersasorphans. solubilization. Although data on the human proteome is less
In this review, we discuss our understanding of how cells complete,analysisoftherelativelyabundantcytosolicproteins
recognize orphans and selectively route them for degradation. inHeLaandHEK293cellsindicatethatalittlelessthanhalfof
We begin by providing an accounting of the eukaryotic prote- them are in stable complexes (Havugimana et al., 2012). This
ome and the extent of its sub-cellular organization into com- meansthatofthe(cid:1)35%ofproteinsthatdonottraffictoanother
partments and complexes. After defining the challenges to destination(seeabove),fewerthanhalfareunaccompaniedby
achievingawell-organizedproteome,weconsidersuccessively partners.Thus,only(cid:1)15%ofgenesencodeproteinsthatsimply
the mechanisms cells use to identify mislocalized and misas- foldandfunctionwithoutfirstrequiringsub-cellularlocalization
sembled proteins. We end with a consideration of how path- andassembly.
waysforthequalitycontroloforphanedproteinsimpactcellular When abundance, cell type, and growth rate are taken into
physiologyand disease. account,therearemanycircumstanceswherethevastmajority
MolecularCell71,August2,2018ª2018ElsevierInc. 443
MolecularCell
Review
A mechanisticframeworkfortheirselectiverecognitionanddegra-
dationisofsubstantialimportancetounderstandinghowprotein
homeostasis is maintained in cells to avoid various disease
states.
ChallengestoAccurateProteinLocalization
Thefundamentalprincipleunderlyingproteinsegregationtoor-
ganellesistherecognitionofsignalsequenceswithinanascent
proteinbytargetingfactorsthatspecifytheappropriatedestina-
tion(Blobel,1980).Withfewexceptions,thetargetingsignalfora
particular organelle is not a specific sequence. Instead, it is
typicallyspecifiedbymoregeneralpropertiessuchashydropho-
bicity,length,andcharge(vonHeijne,1995).Thus,thesetofpro-
teinsthatarerecognizedbyatargetingfactorhavesignalsthat
can differ substantially in sequence as long as they share the
relevantunderlyingbiochemicalfeature(s).
While molecular recognition of a distinct sequence can be
extremely specific, recognition of a diverse set of sequences
withlooselysharedfeatureswillnecessarilybelimitedinspeci-
B ficity.Theactualrateoffailurehasbeenstudiedonlycursorily
andisbestunderstoodforsecretoryproteinsegregationtothe
ER. Very early studies anecdotally noted that the signal se-
quences of some proteins are more efficient than others in
cell-freetranslocationassays.Itwaslaterappreciatedthatnot
only do signals differ in their relative efficiencies (Kim et al.,
2002;Levineetal.,2005),butalsointheirrequirementsfortrans-
location machinery (Fons et al., 2003; Ng et al., 1996; Voigt
etal.,1996).
Mammalian cell culture experiments comparing different ER
signal sequences showed that even the best signals fail (cid:1)5%
ofthetime(Levineetal.,2005;Raneetal.,2004).Inmousebrain,
it has been estimated that the efficient and well-characterized
signalfromprolactinfails(cid:1)1%–2%ofthetime,whilethemore
average signal from prion protein fails (cid:1)5% of the time (Rane
Figure1. AccountingofProteinLocalizationandAssembly
(A) The approximate percentages of human genes whose proteins are
etal.,2010).Theseinvitro,cellculture,andinvivoexperiments
destinedforvariousintracellularcompartmentsareshown. allindicatethatfailureratesofproteinsegregationtotheERare
(B)Datafromthreeproteomicstudiesindicatingthatroughlyhalfofallproteins on the order of 1%–10%. Although similar measurements of
inyeastandmammalsareinproteincomplexes.
mitochondrial import efficiency remain to be performed, the
comparable diversity of signal sequences (von Heijne, 1995)
of synthesized proteins must be localized or assembled. For andanalogousmechanismsofrecognition suggestthatfailure
example, in highly secretory cell types such as pancreatic ratesmaybecomparable.
exocrinecellsorantibody-secretingplasmacells,nearlyallribo- Inadditiontointrinsicfailureoflocalizationundernormalcon-
somesaresynthesizingproteinsdestinedfortheER(Brewerand ditions,acuteorganellestresshasbeenshowntoimpairprotein
Hendershot,2005;Pfefferetal.,2016).Inreticulocytes,almost importintotheERandmitochondria(Kangetal.,2006;Wright
all protein synthesis is dedicated to a- and b-globin, which et al., 2001). The step that fails appears to involve the actual
assembleintoaheterotetramer(BenzandForget,1974).Even translocationreactionacrossthemembrane,albeitbydifferent
in a less specialized cell type making a diverse proteome, the mechanisms.InthecaseofERtranslocation,itisthoughtthat
cell’s most abundant proteins are localized (e.g., histones to chaperonesinthelumenbindpartiallytranslocatedpolypeptides
the nucleus) or part of complexes (e.g., tubulin, ribosomes, topreventtheirback-sliding(Brodskyetal.,1995;Matlacketal.,
andproteasomes). 1999).Engagementofthesechaperoneswithmisfoldedproteins
Theseconsiderationsindicatethateveniftherateoffailurefor duringERstressreducestheiravailabilityfordrivingtransloca-
localizationorassemblyislessthan0.1%,theabsolutenumber tion.Thisisthoughttobeaprotectivemechanismtominimize
of polypeptides that must be recognized by quality control is the load of misfolded proteins in the ER during stress (Kang
high.Asarguedbelow,theactualfailureratesarelikelytobea etal.,2006)butresultsinanincreasednumberofmislocalized
fewpercent,imposingasubstantialconstitutiveburdenonqual- proteinsorphanedfromtheER.
itycontrolpathways.Basedontheseestimates,weproposethat Inthecaseofmitochondria,importofmanyproteinsrelieson
orphans are the major source of substrates for most cellular theelectrochemicalgradientacrosstheinnermembrane(Wie-
quality control pathways in normal unstressed cells. Thus, a demann and Pfanner, 2017). Stress conditions that impair this
444 MolecularCell71,August2,2018
Molecular Cell
Review
biosynthesis quality control Figure2. RecognitionFactorsforProtein
LocalizationandMislocalization
Sequence features in a nascent protein can be
recognizedbyvariousfactorsthatmediatelocal-
SRP izationtothedestinationsindicatedinparenthe-
TMD ses(leftside).Notallfactorsordestinationsare
shown. Orange indicates hydrophobicity, and
RNF126 blueindicatesbasicresidues.SRP,signalrecog-
(E3) nitionparticle;IPO,importinfamilymember;HSP,
heatshockprotein.Therightsideshowsthatthe
(ER membrane) BAG6 complex same sequence features used by biosynthesis
factorscanalsoberecognizedbyqualitycontrol
factorsthatultimatelyleadtodegradationatthe
E3 proteasome.
HSPs
(mito. membrane) UBQLNs
Various studies had informally noted
that cell-free translation of a protein in-
nascent +++ +++ tendedfortheERresultsintheprotein’s
protein
IPOs E2/E3 ubiquitination. This observation was ex-
proteasome
(nucleus) UBE2O ploited to identify factors needed for
recognitionandubiquitinationofthemis-
localized protein (Hessa et al., 2011).
+++ +++ These experiments led to Bag6 (also
? ? called Bat3 or Scythe), a large, widely
conserved cytosolic protein capable of
(mito. matrix) QC factor
recognizingmislocalizedproteins.Arole
forBag6inqualitycontrolwasconsistent
withearlierstudiesthatreportedarolein
gradientwillresultinreducedtranslocation.Atleastoneprotein thedegradationofnewlysynthesizedpolypeptidesprematurely
whose import is impaired initiates a stress response (Nargund releasedfromtheribosomewithpuromycin(Minamietal.,2010).
etal.,2012),whilethegeneralincreaseinmislocalizedproteins Aubiquitin-like(UBL)domaininBag6associateswithRNF126,a
seemstoinitiateacompensatoryincreaseincytosolicdegrada- ubiquitinligasethatworkswiththeE2enzymeUbcH5topoly-
tioncapacity(WangandChen,2015;Wrobeletal.,2015).Other ubiquitinate substrates associated with Bag6 (Rodrigo-Brenni
cellularstates,suchascelldivision,mayalsoresultintemporary etal.,2014).KnockdownofeitherBag6orRNF126partiallyim-
attenuation of mitochondrial protein import (Harbauer et al., pairsdegradationofproteinsthatfailtobesuccessfullyimported
2014; Schmidt et al., 2011; Weidberg and Amon, 2018). Thus, intotheER.
cellsactiveinproteinsynthesisareconstantlychallengedwith Thekeyfeatureofmislocalizedproteinsthatarerecognizedby
proteinsorphanedinthecytosolduetoacombinationofintrinsic Bag6provedtobepreciselytheelementsthatarealsorecog-
andstress-dependentfailuresinsegregatingproteinstotheER nizedbythetargetingandinsertionmachinery:transmembrane
andmitochondria.Theextentofimportfailureforproteinsthat domains(TMDs)andsignalsequences(Figure2).Thus,deleting
functionexclusivelyinthenucleus(e.g.,histones)remainspoorly these hydrophobic domains precludes Bag6 recognition and
studiedandmayfurthercontributetoorphans. ubiquitination despite the fact that the resulting protein is still
mislocalized and presumably unable to fold (Hessa et al.,
RecognitionofMislocalizedProteinOrphans 2011). It is instead apparently recognized by cytosolic quality
Anumberofearlyobservationsindicatedthatmislocalizedpro- controlpathwaysthatrecognizeproteinmisfolding.Indeed,en-
teins in the cytosol are degraded. First, rare human mutations forcedmislocalizationbydeletionofasignalsequenceinyeast
thatdisruptthefunctionofasignalpeptideresultinloweroverall results in recognition by the general chaperone Hsp70 (Park
expressionlevels(Cassanellietal.,1998;Karaplisetal.,1995; etal.,2007).
Seppenetal.,1996).Second,proteasomeinhibitionledtothe Analogous studies of a mitochondrial membrane protein
appearance of a non-glycosylated form of prion protein (Ma showedthatpriortoitsinsertionintomitochondria,itassociates
andLindquist,2001),whichlaterprovedtobegeneratedbysta- with members of the Ubiquilin (UBQLN) family (Itakura et al.,
bilization of the non-targeted population (Chakrabarti et al., 2016).Structure-functionanalysisofUBQLN1identifiedamiddle
2011; Drisaldi et al., 2003; Rane et al., 2004). Third, inhibition domainthatspecificallyassociateswiththeTMDsofmembrane
of ER translocation by small molecules (Besemer et al., 2005; proteins in the cytosol. Unlike substrate interaction with Bag6
Garrison et al., 2005) or acute ER stress (Kang et al., 2006) (Shaoetal.,2017),theUBQLN1associationisdynamic(Itakura
resulted in rapid proteasome-dependent degradation of the etal.,2016).However,iftheinteractionisprolonged,aswouldbe
non-translocatedprotein.Whilethesefindingsshowedthatmis- thecaseifimportintomitochondriafails,themembraneprotein
localized proteins are degraded in the cytosol, the factors becomes ubiquitinated in a UBQLN-dependent manner. This
involvedwerenotknown. ubiquitination is mediated by a yet-unidentified ligase that is
MolecularCell71,August2,2018 445
MolecularCell
Review
recruitedtotheubiquitin-associating(UBA)domaininUBQLN. andUBE2Omustactaftersubstrateshaveattemptedtargeting,
AlthoughothermembersoftheUBQLNfamily(mammalshave themechanismsofwhicharediscussedlater.Eventhoughthese
four)havebeenlesswellstudied,theyhavesimilarmiddledo- factorscollectivelyrecognizeabroadrangeoforphansmislocal-
mainsthatmayalsointeractwithTMDsofmislocalizedproteins ized to the cytosol, additional quality control machinery that
(Itakuraetal.,2016;SuzukiandKawahara,2016).Itisattractive recognize nuclear and mitochondrial targeting signals may
tospeculatethattheirspecificitiesaresomewhatdifferentfrom remaintobediscovered.
each other to collectively cover the wide range of sequences
thatdefineTMDs.Indeed,Bag6appearstoprefermorehydro- ProteinsOrphanedtotheWrongOrganelle
phobic TMDs than UBQLN1 (Itakura et al., 2016). Additional TheTMDsofmembraneproteinstargetedtotheERandmito-
studiesareneededtoinvestigatethesubstraterangesandmo- chondria are very similar in their biophysical properties (Guna
lecularbasisofspecificityofthesefactors. andHegde,2018),consistentwiththeireventualresidenceina
Unlike membrane proteins whose exposed TMDs provide a lipid bilayer. For many of these proteins, the TMD(s) serve as
distinctivecueforrecognitionofmislocalization,thesolublepro- themainorsoletargetingsignal.Duetothesimilaritiesamong
teinsofmembrane-boundcompartmentsmorecloselyresemble these TMDs, membrane proteins can be routed to the wrong
cytosolic proteins.InthecaseofproteinsdestinedfortheER, organelle.Howcellsdealwiththisproblemisonlypartiallyun-
signal sequences are sufficiently similar to TMDs that they derstood.
seemtoberecognizedbyBag6(Hessaetal.,2011).Solublepro- The simplest and best-studied case involves tail-anchored
teinsdestinedformitochondriaorthenucleushaveamphipathic (TA)membraneproteins(HegdeandKeenan,2011).Thesepro-
orbasicsignals,respectively.Whetherdedicatedfactorsrecog- teinscontainasingleTMDclosetotheCterminus,whichserves
nize persistent residence of these signals in the cytosol for asthesoletargetingsignal.TAproteinsdestinedforthemito-
degradation remains largely unexplored. One candidate factor chondriatendtohaveslightlylesshydrophobicTMDs(Watten-
forthisroleisUBE2O,ahybridE2-E3enzymethatwasrecently bergetal.,2007)andoftenhavedownstreambasicresiduesin
shown to recognize and ubiquitinate ribosomal proteins in the theC-terminaltail(Horieetal.,2002).Nevertheless,thereissub-
cytosol (Nguyen et al., 2017; Yanagitani et al., 2017). Under stantialoverlapintheirpropertiesandaclearriskofmistargeting.
normal circumstances, newly made ribosomal proteins are The best-characterized TA targeting pathway to the ER is
recognizedbydedicatednuclearimportfactors(Ja€kelandGo¨r- knownastheTRC(TMDrecognitioncomplex)pathwayinmam-
lich,1998),deliveredtothenucleolus,andassembledwithrRNA mals and the homologous GET (guided entry of TA proteins)
into pre-ribosomal subunits(Pen˜aetal.,2017).Itappears that pathway in yeast (Hegde and Keenan, 2011). Deletion of GET
failureofnuclearimportleadstorecognitionbyUBE2O,multi- pathway components in yeast results in mislocalization to the
mono-ubiquitination,andproteasomaldegradation. cytosol(oftenasproteinaggregates)andmitochondria(Jonikas
Although the precise sequence features recognized by et al., 2009; Schuldiner et al., 2008). A membrane-embedded
UBE2Oareunclear,itappearstobethejuxtapositionofhydro- AAA-ATPase Msp1 in the mitochondrial outer membrane is
phobicandbasicresidues(Yanagitanietal.,2017).Thisisnote- thoughttobeinvolvedinremovingTAproteinsmislocalizedto
worthybecauseitissimilarinsomewaystobothnuclearimport mitochondria (Chen et al., 2014; Okreglak and Walter, 2014).
(Ja€kelandGo¨rlich,1998)andmitochondrialimportsignals(von Asub-populationofMsp1isalsofoundintheperoxisomalmem-
Heijne,1995),aswellasacommonfeatureofnucleicacid-bind- brane,whereitisthoughttoserveasimilarrole(Weiretal.,2017).
ingproteins(Hentzeetal.,2018;Nelson,1995).Ribosomalpro- Hence,thelevelsofmislocalizedTAproteinsinmitochondriaor
teininteractionswithUBE2Oandnuclearimportfactorsappear peroxisomes increases when Msp1 (or its human homolog,
tobemutuallyexclusive(Yanagitanietal.,2017),suggestingthat ATAD1) is deleted. As this stabilization is seen even in wild-
UBE2Omayinteractwiththenuclearimportsignal.Itwillthere- type cells containing anintact TRC/GET pathway (Chen et al.,
forebeinterestingtodeterminewhetherthisisageneralproperty 2014), mislocalization must be a constitutive problem in cells
ofUBE2Oandwhetherothernucleicacidbindingproteins,such andtissues,consistentwiththechallengesofachievingprecise
ashistones,subunitsofthesignalrecognitionparticle(SRP),and targetingspecificity.
mitoribosomal proteins, are recognized by UBE2O when they ThemechanisticbasisofMsp1functioninclearanceofmislo-
areorphanedinthecytosol. calizedproteinsubstratesisnotwellunderstood.PurifiedMsp1
Thus,thecytosolappearstobepatrolledbyasetoffactors reconstitutedintosyntheticliposomeswasshowntodriveATP-
that can interact with signal sequences and TMDs on the one dependent extraction of a co-reconstituted TA protein to the
handandubiquitinligasesontheother(Figure2).Thesefactors cytosol (Wohlever et al., 2017). The ATPase domain of Msp1,
collectively recognize proteins that expose organelle targeting whichfacesthecytosol,wasshowntobeahexamercontaining
domains, an indicator that targeting may have failed, and acentralpore.BecausemutationswithintheporeimpairtheTA
mediatetheirtaggingfordegradation.Itisnoteworthythatthe proteinextractionactivity,ithasbeenpositedthatthesubstrate
substrate specificity of these factors, while likely to be rather ispulledthroughtheporeintothecytosol(Wohleveretal.,2017).
broad,appearstobeespeciallywellsuitedtothesameelements Suchamodelwouldbeconsistentwiththemechanismofaction
recognizedbyproteintargetingfactorssuchasSRPandTRC40 ofotherAAAproteinunfoldasesforwhichtranslocationthrough
(alsocalledGet3),whichmediatemembraneproteintargetingto thecentralporeisstronglysupported(SauerandBaker,2011).
theER(ShaoandHegde,2011),andImportins5and7,which How the substrate is kept in a soluble form after extraction,
mediatenuclearimportofribosomalproteins(Ja€kelandGo¨rlich, howitisubiquitinated,andhowitisdeliveredtotheproteasome
1998). In order to not interfere with targeting, Bag6, UBQLNs, allremainunknown.Onepossibilityisthatcytosolicfactorssuch
446 MolecularCell71,August2,2018
Molecular Cell
Review
Figure3. RecognitionofProtein
MislocalizationatOrganelles
peroxisome Membrane protein insertion into the wrong
organellecanberecognizedbyitslackofassoci-
ationwithaninteractionpartner.Inmitochondria
andperoxisomes,thehexamericATPaseMsp1is
Msp1 involvedinextractingsuchmislocalizedproteins
tothecytosolfordegradationbytheproteasome.
IntheER,thespecificmachineryformislocalized
proteins has not been studied, but probably in-
volvesknownER-associateddegradation(ERAD)
pathways. The molecular basis ofrecognition is
notknown,butmayinvolvethesamefeaturesthat
facilitate assembly into protein complexes, ex-
plainingwhysuccessfulassemblywouldprevent
recognitionbyqualitycontrolfactors.
proteasome
Msp1
ERAD?
endoplasmic mitochondrion overexpression conditions (Vitali et al.,
reticulum 2018). Furthermore, the ribosome-asso-
ciated chaperone-like protein NAC
appears to antagonize SRP and limit
its promiscuous recognition of nascent
mitochondrial proteins (Gamerdinger
et al., 2015; Wiedmann et al., 1994).
asBag6orUBQLNsmaymediatethesedownstreamstepssimi- Thus, when NAC levels are reduced, mitochondrial proteins
larly to how they recognize and degrade cytosolic orphans canbedetectedattheER.AlthoughtheseexamplesofERmis-
generated by failed targeting. Consistent with this concept, targetingareseenunderperturbedconditions,itislikelythata
Bag6 has been shown to maintain the solubility of membrane lowlevelofmistargetingoccursinnormalcells.Howthesemis-
proteinsextractedfromtheERuntiltheirdegradationatthepro- targetedproteinsarerecognizedanddegradedisunclear.One
teasome(Wangetal.,2011). possibility is that known ER-associated degradation pathways
ThebasisofsubstrateselectionbyMsp1isalsoonlypartially areinvolved(VembarandBrodsky,2008).Thisproblemwarrants
understood.StudiesoftheperoxisomalTAproteinPex15have investigation.ToolstoinduceexcessiveERmistargetingshould
provided initial insights into this key issue (Weir et al., 2017). facilitatethislineofinquiry.
Pex15isnormallyfoundincomplexwithPex3.Itwasobserved
that excess Pex15 in peroxisomes is degraded in an Msp1- ChallengestoAssemblyofProteinComplexes
dependentmanner,whilePex15incomplexwithPex3evades After segregating proteins to the correct compartment, most
Msp1 (Weir et al., 2017). As discussed in detail later, orphans proteinsmustadditionallyassemblewithoneormorepartners
ofmulti-proteincomplexesareoftentargetsforqualitycontrol (typically other proteins, but also RNAs). The assembly of
via recognition of the regions that are normally shielded by multi-proteincomplexesimposesthreemajorchallengestothe
interaction partner(s). It appears that Msp1 may use such a cell.First,thecomponentsofthecomplexmustbesynthesized
mechanism to recognize orphaned Pex15 and perhaps other intheappropriatestoichiometry.Second,theunassembledsub-
substrates(Figure3). units of a complex must avoid inappropriate interactions until
ThisfindingsuggeststhatwhenPex15ismistargetedtomito- their assembly. Third, partners must find each other within a
chondria,itsrecognitionbyMsp1fordegradationisduetothe crowded cell. As with protein localization, limitations to the
absence of Pex3. Whether all Msp1 substrates are normally overallefficiencyofachievingtheseessentialstepsincomplex
partoflargercomplexeswhoseabsencecuestheirrecognition assembly results in orphans that must be recognized and
remains to be determined. Furthermore, it is unclear whether degraded.
Msp1 directly recognizes substrates or uses adaptors. In this Directanalysisoftranslationratesbysequencingofribosome-
context,itisnoteworthythatMsp1associateswithCis1,apro- protectedfootprints(ribosomeprofiling)indicatesthatcellstypi-
teinthatisupregulatedbyexcessivemitochondrialimportfailure callyexpresssubunitsofamulti-proteincomplexatclosetothe
andplaysayet-unknownroleinclearanceoffailedimportprod- stoichiometryfoundinthefinalcomplex(Lietal.,2014).Acom-
ucts (Weidberg and Amon, 2018). Whether Cis1 is involved in binationofseveralmechanismscontributestothisconcordance.
identifying substrates for delivery to Msp1 remains unclear. First,thegenesforproteinsthatfunctiontogetherarefrequently
Thus, both the specific features of mistargeted proteins that organizedinasingleoperoninprokaryotes(AmesandMartin,
arerecognizedandthefactorsthatmediaterecognitionremain 1964). This allows the transcript levels to necessarily be
tobeelucidatedinmolecularterms. increasedanddecreasedinunison.Differencesintheorderof
Thefactor(s)thatplaytheanalogousroletoMsp1intheERare genes in an operon and their respective Shine-Dalgarno se-
unknown. It has recently been shown that mitochondrial TA quences can presumably further tune their relative levels of
proteins can be mistargeted to the ER, particularly under translation(Bondeetal.,2016;Limetal.,2011).
MolecularCell71,August2,2018 447
MolecularCell
Review
Ineukaryotes,geneorder(Da´vilaLo´pezetal.,2010)andthe T cell receptor (TCR) showed that the a subunit is rapidly
similaritiesofpromotersengagedbythesametranscriptionfac- degradedwhenexpressedwithoutitsinteractionpartners(Lip-
tors(Leeetal.,2009)canalsocoordinatetranscriptlevelsofpro- pincott-Schwartzetal.,1988).Conversely,itiswellappreciated
teinsubunits.Beyondthis,furtherfine-tuningofmRNAhalf-lives that knockdown or knockout of one subunit of a multi-protein
and translation rates via untranslated regions and codon opti- complex often destabilizes the other subunits. Thus, in
malityprobablycontributetoexpressionatthedesiredstoichi- numerous contexts and cellular compartments, cells have
ometry.Forexample,the50endofmRNAsencodingribosomal mechanismstoselectivelyidentifyorphanedsubunitsandtarget
proteinsandmanytranslationfactorscontainterminaloligo-py- themfordegradation.
rimidine sequences (Meyuhas and Kahan, 2015). These se- Twogeneralmechanismscanexplainhoworphansarerecog-
quencesallowthetranslationofthesemRNAstoberepressed nized.First,someproteinsmaynotbeabletoachieveastable
andde-repressedinconcert,therebymaintainingtheirapproxi- foldedstateintheabsenceofitsinteractionpartner.Thisinsta-
mate stoichiometry. Nevertheless, these mechanisms are all bility would result in its unfolding and recognition by general
subjecttostochasticity(Munskyetal.,2012),meaningthatthe quality control pathways that monitor protein folding. Second,
inevitableimbalancesinsynthesislevelsgenerateorphans.Itis asubunitinterfacethatisnormallyshieldedintheintactcomplex
reasonabletoassumethatachievingexpressionstoichiometry is recognized by a factor that ultimately leads to degradation.
to greater than 90% precision is very challenging given the Factors for both mechanisms have been identified in different
inherent noisiness of gene expression. For complexes with biologicalcontexts.
manysubunits,suchasribosomesandproteasomes,matching The most challenging multi-subunit complex to assemble in
expressionlevelsmaybeparticularlydifficult. cellsisprobablytheribosome.Itsbiogenesisfrom80proteins
Themechanismsbywhichproteinsareassembledintocom- and pre-rRNA involves dozens of dedicated assembly factors,
plexeshasbeenstudiedinanumberofcontexts,includingribo- numerousprocessingreactionsofbothproteinsandrRNA,ava-
somebiogenesisinthenucleolus(Pen˜aetal.,2017),hemoglobin riety of post-translational modifications, and multiple transport
assembly in pre-erythrocytes (Feng et al., 2004; Kihm et al., stepsacrossthenuclearenvelope(Pen˜aetal.,2017).Individual
2002), and histone assembly (Hammond et al., 2017). Each of ribosomal proteins have long been known to be refractory to
theseprocessesisdistinctiveinitsuseofspecificchaperones overexpression, suggesting efficient mechanism(s) for degrad-
andassemblyfactors.Themainunderlyingprinciplefromthese ing excess copies (Abovich et al., 1985; Warner et al., 1985).
studies is that unassembled subunits of a complex are held Despitethefactthatribosomeshaveaverylonghalf-life,ribo-
temporarily by an assembly factor until it is displaced by the somal proteins are a major set of proteins that accumulate
appropriateinteractingsubunit.Inmanycases,thepreciseorder when proteasome activity is diminished (Mayor et al., 2005,
of protein complex assembly is important and under selective 2007). This suggests that ribosomal proteins may be a major
pressure to be maintained, presumably to minimize misas- sourceoforphansinactivelygrowingcells.Theneedtodestroy
sembledproducts(Marshetal.,2013).However,theefficiency orphanedribosomalproteinsmaybeespeciallycriticalasthese
oftheseprocessesisunknowninmostcases,especiallyinvivo, factorsareaggregation-proneintheabsenceofanRNAscaffold
so their relative contributions to the generation of orphans re- oraribosomeassemblychaperone(Ja€keletal.,2002).
mainstobedetermined. Asdiscussedabove,aribosomalproteinorphanedatthestep
Recent proteomic pulse-chase experiments indicate a sub- ofimportintothenucleusisrecognizedinthecytosolbyUBE2O
stantialconstitutiveburdenofunassembledorphansincultured (Yanagitanietal.,2017).Afternuclearimport,failureatthestepof
cells(McShaneetal.,2016).Inthisstudy,kineticanalysisofpro- assemblywithrRNAisrecognizedbyadifferentmechanism.In
tein degradation found (cid:1)10% of proteins are degraded non- yeast, the large nuclear-localized E3 ligase Tom1 was shown
exponentially, with a proportion (ranging from 10% to 70%) to interact with unassembled ribosomal proteins and mediate
being degraded immediately after synthesis. Approximately theirubiquitination(Sungetal.,2016).Thesitesofubiquitination
70%ofthesenon-exponentiallydegradedproteinsaresubunits suggest that Tom1 probably interacts with basic regions that
of known multi-protein complexes, suggesting that the rapidly wouldordinarilyinteractwithrRNA.Theseregionsareinacces-
degradedpopulationsarethosepolypeptidesthatfailedassem- sible in intact ribosomes, which are not recognized by Tom1.
bly.Asthisanalysisidentifiedonlythemostabundantproteins,it HUWE1istheclosesthomologofTom1inmammals.Itsknock-
appears that cells mustconstantly identify and degrade unas- down partially increases the levels of overexpressed uL24/
sembledorphans. RPL26,butthebasisforthiseffectwasnotexploredinsufficient
depthtoconcludeadirecteffect(Sungetal.,2016).
RecognitionofUnassembledCytosolicProteinOrphans Inseparatestudies,however,itwasobservedthatHUWE1is
It has been apparent for many decades that unassembled or- required for efficient degradation of farnesyltransferase alpha
phans of multi-protein complexes are selectively degraded. (FTNA) and UBL4A when their respective binding partners are
The earliest appreciation of this phenomenon comes from the absent (Xu et al., 2016). Although interaction studies were not
studyofhemoglobin,ahetero-tetramernormallyformedoftwo performed,HUWE1presumablyrecognizestheexposedinter-
aandtwobsubunits(Perutzetal.,1960).Mutationsinhemoglo- facesoftheseandotherproteinstomediatetheirubiquitination.
binthatmarkedlyreduceitsunusuallylonghalf-lifewerecorre- Proteomic analysis identified 72 candidate HUWE1 substrates
lated with an increased tendency of tetramer dissociation into (although,curiously,notribosomalproteins),almostallofwhich
subunits and decreased binding to heme (Jacob et al., 1968; areknownsubunitsof multi-protein complexes. Mostofthese
Rieder, 1974). Many years later, studies of the multi-subunit candidate substrates operate in the nucleus, yet HUWE1
448 MolecularCell71,August2,2018
Molecular Cell
Review
Figure4. AssemblyInterfacesServeas
A
DegradationSignals
(A)Schematicofhemoglobinassemblyinwhich
theasubunitistemporarilyshieldedbya-hemo-
globin-stabilizingprotein(AHSP)untilitassembles
withthebsubunit.Freeasubunit,generateddue
toexcessoramutationthatpreventsassembly,is
instead recognized by UBE2O for ubiquitination
andtargetingtotheproteasomefordegradation.
(B) The assembly interface of a-globin showing
hydrophobic (yellow) and basic (blue) surfaces.
AHSPisshownintransparenttantoillustratehow
this interface is shielded. The positions of two
assemblymutantsthatcausehumananemiaare
indicated. UBE2O is known to bind composite
basic/hydrophobicpeptides,suggestingthatthe
interface is recognized via these features when
assemblyfails.
(C)AnexposedNorCterminuswithadestabiliz-
B ingresiduecanbeshieldedinacorrectlyassem-
bledcomplex(left)butexposedasanunassem-
bledorphan.N-endandC-endE3ubiquitinligases
C
that recognize such residues would then selec-
tivelytargettheorphanfordegradation.
Insupport of the latter possibility, acute
inductionofproteinmisfoldinghasbeen
shown to cause UBE2O upregulation in
cultured cells (Miyazaki et al., 2015).
Structure-functionanalysisofUBE2Oin-
dicates that it has two major substrate
interactiondomainswithdifferentbinding
properties (Nguyen et al., 2017; Yanagi-
tani et al., 2017). Identifying the client
appears to function in the cytosol. Thus, HUWE1 may identify rangesofthesedomainsandthestructuralbasisoftheirinterac-
orphansthatfaillocalization,assembly,orboth.Themolecular tionsremainsanimportantgoal.
featuressharedbyHUWE1clientsandthebasisoftheirrecog- Thegeneralconceptoforphanrecognitionviaexposureofa
nitionremaintobeaddressed. normallyburiedinterfacehasbeenexploitedbyotherubiquitina-
In addition to its role in recognizing mislocalized ribosomal tionfactors.TheN-endrulepathwaysofsubstrateubiquitination
proteinsdiscussedabove,UBE2Ocanalsorecognizedfolded recognizecertainresiduesatanexposedNterminusandselec-
but unassembled proteins. This conclusion comes from the tivelytargettheseproteinsfordegradation(Tasakietal.,2012).
observationthatinvitroandinvivo,UBE2Oisneededforeffi- One mechanism involves recognition of N-terminal acetylation
cientubiquitination and degradationof unassembled a-globin bytheubiquitin ligase CNOT4 (Shemorry etal.,2013).Several
(Nguyen et al., 2017; Yanagitani et al., 2017). The interface multi-protein complexes appear to contain N-acetylated sub-
of a-globin that interacts with b-globin is usually shielded by units whose N terminus is shielded by other subunits in the
a-hemoglobin-stabilizing protein (AHSP) until assembly with intactcomplex.Failuretoassembleintoacomplex(orcomplex
b-globin (Feng et al., 2004, 2005) (Figure 4A). Mutations in disassembly)exposestheN-terminaldegron,resultinginubiqui-
a-globin that impair interaction with AHSP (and b-globin) are tinationbyanN-endruleubiquitinligase(Figure4C).Examples
moreeffectivelyrecognizedandubiquitinatedbyUBE2O(Ya- includetheHcn1subunitoftheAPC/CcomplexandtheCog1
nagitanietal.,2017).ThisindirectlysuggeststhatUBE2Orec- subunitoftheyeastCOGcomplex.
ognizesthesameregionasAHSP.Thisinterfaceisbasicand It is possible that other N-end rule ligases exploit a similar
hydrophobic (Figure 4B), which is similar to other established mechanism to recognize different unassembled proteins. For
UBE2O targets such as unassembled ribosomal proteins example,theN-endruleubiquitinligaseUbr1wasshowntobe
(Nguyen et al., 2017; Yanagitani et al., 2017). Thus, orphan neededforefficientclearanceofunassembledFas2,asubunit
a-globinappearstobeidentifiedfordegradationbyitsexposed of the fatty acid synthase complex (Scazzari et al., 2015).
assemblyinterface. Whether Ubr1 uses its N-end rule recognition domain or uses
Notably, UBE2O is highly upregulated during erythrocyte anadaptorsuchasHsp70toidentifyunassembledFas2isun-
development concordantly with increased globin production clear at present. Hsp70 is needed for Ubr1-dependent Fas2
(Wefesetal.,1995).Whetherthisupregulationisaprogrammed ubiquitination,supportingthelatterhypothesis.Presumably,an
eventinpreparationfortheinevitableincreaseinsubstrateload interface of Fas2 shielded by its interaction partner, Fas1, is
oraresponsetoincreasedorphansremainstobedetermined. exploited for its recognition by chaperones, which over time
MolecularCell71,August2,2018 449
MolecularCell
Review
recruits a ubiquitin ligase to initiate degradation. The recent (Huber et al., 1976). After translocation into the ER lumen, the
discoveryofa‘‘C-endrule’’(Korenetal.,2018;Linetal.,2018) first heavy chain immunoglobulin domain (CH1) binds to the
raisesthepossibilitythatexposureofanormallyshieldedCter- chaperone BiP in an unfolded and reduced state (Bole et al.,
minus might also be exploited by cells to recognize orphans 1986;HaasandWabl,1983;Hendershotetal.,1987;Vanhove
(Figure4C).Thisidearemainstobeinvestigated. etal.,2001).CH1canonlyfolduponinteractionwithlightchain
(Feigeetal.,2009).Hence,intheabsenceoflightchains,heavy
RecognitionofUnassembledProteinOrphansattheER chainsareretainedintheERandareeventuallydislocatedtothe
Eachoftheexamplesofunassembledproteindegradationdis- cytosoltobedegradedbytheproteasome(Mancinietal.,2000).
cussedthusfaroccurinthecytosol.Analogousprocessesoper- Even though the assembly process varies between different
ateintheERmembraneandlumenandprobablyalsodifferent immunoglobulin isotypes (Baumal et al., 1971), BiP-mediated
mitochondrial compartments. In the ER, the most extensively retentionofheavychainsintheERappearstobeuniversal(Hen-
studiedmulti-proteinassemblieshavebeentheimmunoglobu- dershot et al., 1987). Prolonged association with BiP, whether
linsandTCR.TCRaandCD3d,twosubunitsoftheTCR,have oforphanheavychainsorTCRsubunits,mayresultindelivery
beenwidelyusedasmodelsforERAD(BonifacinoandLippin- to ERAD machinery via adaptors such as specific J-proteins
cott-Schwartz,1991;Bonifacinoetal.,1989;HuppaandPloegh, (ShenandHendershot,2005).
1997;Lippincott-Schwartzetal.,1988).Bothsubunitsaresingle-
spanning transmembrane proteins that are recognized for DistinguishingIntermediatesfromOrphans
degradation via their TMDs (Bonifacino et al., 1991; Cosson Proteinsshouldberecognizedasorphanstobedegradedonly
etal.,1991;Manoliosetal.,1990).Theprevailingmodelisthat after reasonable attempt(s) at localization and assembly have
theorphanedTMDsofTCRaandCD3darerecognizedbythe failed.Thus,thebiosynthesismachineryshouldhavehigherpri-
membrane-embeddedregionsofaER-residentubiquitinligase orityforaccesstonascentchainsthanthequalitycontrolma-
complex centered aroundHrd1 (Kikkert etal.,2004).Although chinery,butthispriorityshouldbetimelimited.Themechanistic
thestructuralbasisoftheirrecognitionremainsunknown,itde- basisofhowpriorityandtimingaredeterminedisimportantto
pendscriticallyonchargedresidueswithintheirTMDsthatare understandbecausethiscriticaldecisionbalancespromiscuous
shielded by other subunits in the assembled TCR. A similar degradationofnormalbiosyntheticintermediatesversusexces-
modeofrecognitionbyHrd1wasalsoshownforotherintegral sive persistence of potentially toxic and aggregation-prone
membranesubstratessuchasHmg2(Satoetal.,2009). orphans.
Basedontheseexamples,onemightspeculatethatorphans One mechanism by which priority can be conferred is by
ofmulti-proteincomplexesassembledviatheirTMDsarerecog- spatialsegregationofthebiosyntheticandqualitycontrolfac-
nizedbytheexposureofpolarresidueswithinthelipidbilayer. tors. The best illustration of this principle is SRP interaction
This would provide a relatively universal cue for unassembled with the ribosome. The majority of eukaryotic proteins
proteins without relying on sequence-specific recognition. In destined for the ER are recognized co-translationally by SRP
this light, it is intriguing that the recently determined cryo-EM (Chartron et al., 2016; Costa et al., 2018; Keenan et al.,
structure ofHrd1 showsahydrophilicpocket thatmightserve 2001). This interaction is facilitated by the ability of SRP to
as the site of recognition of such orphaned TMDs (Schoebel interactwiththeribosomesuchthatthesignalsequencebind-
etal.,2017).Eventhoughthefunctionalroleofthisputativebind- ingdomainispositionedpreciselyattheribosomalexittunnel
ingregionofHrd1remainstobeinvestigatedexperimentally,the (Halic et al., 2004; Voorhees and Hegde, 2015). Not only is
model is consistent with previous observations that mutations SRP thought to sample ribosomes for the presence of an
within this hydrophilic region of Hrd1 affect recognition of emergingsignal,butitmaybestabilizedtherewhilethesignal
someintegralmembraneERADsubstrates(Satoetal.,2009). is still inside the ribosomal tunnel (Berndt et al., 2009; Voo-
AlthoughrecognitionoforphanedTMDswithinthemembrane rheesandHegde,2015).
haslongbeenpresumed,experimentalevidenceforthisideais In this manner, nascent secretory and membrane proteins
generallylacking.AnalternativeideaisthatorphanedTMDs,due wouldnothaveanopportunitytoengagequalitycontrolfactors
totheirexposedpolarorchargedresidues,areunstableinthe such as Bag6 or UBQLNs unless SRP recognition has failed.
lipidbilayerandtranslocateintotheERlumen(FeigeandHen- Thus,despiteits(cid:1)5-to10-foldlowerabundance(Kulaketal.,
dershot,2013).Thisresultsintheirrecognitionbylumenalchap- 2014),SRPneverthelesshaspriorityduetoitspreciselocaliza-
erones,particularlyBiP,whichareproposedtodeliverthemfor tion at the ribosome. Once a protein has been released from
degradation.Successfulassemblywouldpreventthistransloca- theribosome,SRP’srelativelylowabundanceandpoorcapacity
tion, providing an explanation for why orphans are selectively tobindproteinsinsolutionprecludesitsinterferencewithother
degraded. Although both models ultimately involve Hrd1 (or processes.
another ubiquitin ligase complex) mediating retrotranslocation Atalaterstepinbiogenesis,secretoryandmembraneproteins
into the cytosol for degradation, one posits recognition in the are translocated into the ER through the ribosome-associated
ERlumenwhiletheotherinvolvesrecognitioninthemembrane. Sec61translocationchannel(Rapoportetal.,2017).Anyproteins
Althoughthetwoviewshaveyettobereconciled,oneattrac- thatselectivelyassociate,evendynamically,withSec61willget
tionofthelumenalrecognitionmodelisitssimilaritytohowmis- priorityforinteractionwiththenascentchainoverthosethatdo
assembledlumenalproteincomplexesmightbemonitored.One not.Indeed,processingenzymessuchasoligosaccharyltrans-
exampleofproteincomplexassemblyintheERlumenisimmu- feraseandsignalpeptidaseenjoysuchpriority(Braungeretal.,
noglobulins typicallybuiltfromtwoheavyandtwolightchains 2018), as might the chaperone BiP (via its recruitment by the
450 MolecularCell71,August2,2018
Molecular Cell
Review
transloconcomponentSec63[Brodskyetal.,1995])andCalnexin assembly. It is therefore possible that cells have evolved
(Lakkarajuetal.,2012).Inthismanner,biosyntheticfactorscould mechanisms to detect orphans co-translationally via failure of
begivenprioritybeforedegradationfactorssuchasHrd1. adecisiveco-translationalbiosyntheticstep.Earlydetectionis
Asecondmechanismofconferringpriorityistouseacombi- advantageous because minimizing the time an aberrant poly-
nationofabundanceandfastbinding.Thisappearstobehow peptideresidesinacellreducestheriskofinappropriateinterac-
newly made TA proteins are prioritized for ER targeting ahead tions,aggregation,andotheradverseconsequences.Although
of proteasomal degradation. Recent studies show that among co-translational orphan detection has not been established
thethreeTMDbindingfactorsinvolvedinTAproteintargeting, unambiguously,twoexamplesarenoteworthy.
SGTA is the fastest and first interactor (Shao et al., 2017). Its Thefirstexampleconcernsanautoregulatorymechanismto
competitiveadvantagemaybefurtherincreasedbyitsinterac- controlb-tubulinexpression.Asnotedalready,a-andb-tubulin
tionwiththeBag6complexorHsp70,bothofwhichcanasso- formaconstitutivecomplex(Feitetal.,1971).Inthepresence
ciatewiththeribosome.TAproteinscantransferfromSGTAto of excess unpolymerized tubulin subunits, synthesis of both
TRC40 (Mock et al., 2015; Shao et al., 2017) by a mechanism a-tubulin and b-tubulin polypeptides is reduced (Cleveland
thatdoesnotrequirereleaseofTAproteinintothebulkcytosol etal.,1981).Oneregulatorymechanisminvolvesselectivedegra-
(Shaoetal.,2017).LoadingonTRC40isacommitmenttotarget- dationofb-tubulinmRNA(PittengerandCleveland,1985).This
ingbecauseTAproteindissociationisveryslowrelativetothe degradationisstrictlydependentontranslationandmorespecif-
rate of targeting. TA proteins have a limited time to complete ically on the first four amino acids in the nascent polypeptide
theseeventsasdictatedbytheiroff-ratefromSGTA.Dissocia- (Bachurskietal.,1994;Gayetal.,1989).Remarkably,amono-
tion from SGTA permits an opportunity to be captured by clonalantibodythatbindsthesefourresiduesabolishedtransla-
Bag6, which recruits an E3 ligase for substrate ubiquitination tion-dependentmRNAdegradation(TheodorakisandCleveland,
(Rodrigo-Brennietal.,2014).VeryslowdissociationfromBag6 1992).Thesefindingsledtotheideathatco-translationalassoci-
meansTAbindingtothisfactoriseffectivelyacommitmentfor ation of nascent b-tubulin with some yet-unidentified factor
degradation.Thus,triagebymultiplefactorsofseeminglyiden- (whichisnota-tubulin)isneededtoescapemRNAdegradation.
ticalspecificitycanbeaccomplishedsimplybytheirdifferential Intheinterveningtimesincethesefindings,variouspathways
on-andoff-ratescombinedwithcommitteddownstreamevents ofmRNAdecayhavebeencharacterized,includingonesdepen-
suchasmembraneinsertionorubiquitination(Shaoetal.,2017). dentonribosomestalling(ShoemakerandGreen,2012).Thus,
Thefinalmechanismisbasedonanintrinsicallyslowreaction one attractive model is that a limiting assembly factor binds
followedbyaspecificcommitmentstep.Thisisbestexemplified nascent b-tubulin, the absence of which leads to translation
by glycoprotein quality control in which a specific irreversible arrest and mRNA degradation. Assuming that this factor is
trimmingeventofanN-linkedglycangeneratesaproductthat displaceduponassemblywitha-tubulin(ortubulinincorporation
is recognized by a lectin coupled to quality control pathways into microtubules), b-tubulin orphans would sequester the
(CarameloandParodi,2015;Tannousetal.,2015).Thetrimming assembly factor and lead to mRNA decay. In this way, the
event is carried out by intrinsically slow mannosidases, effec- productionoforphanb-tubulinwouldbetightlyrestrictedviaa
tively placing a time limit on protein maturation attempts. As co-translationaldetectionmechanism.
predicted by this model, overexpression of the mannosidase Thesecondexampleconcernstheconsequencesoffailedco-
acceleratestherateofdegradation(Hosokawaetal.,2001). translational recognition by SRP. It has been observed that
Ananalogousmechanismofaslowenzymaticreactionlinked knockdown of SRP or mutating a signal peptide such that it
toacommitmentstepseemstobeusedforsomeorphansinthe cannotberecognizedbySRPcausesareductioninthecorre-
cytosol.MembraneproteinsboundtoUBQLNsarenotinitially sponding mRNA and protein (Karamyshev et al., 2014). This
committed for degradation (Itakura et al., 2016). Instead, their effectwasdependentonArgonaute2,whichwasalsoobserved
dynamicreleaseandre-bindingprovidesopportunitiesatsuc- to interact with the SRP-deficient nascent chain at the
cessfulinsertion.However,arelativelyslowubiquitinationstep ribosome (Karamyshev et al., 2014). These findings suggest
seemstobethekeycommitmentstep.Whenubiquitinisadded a model in which co-translational failure of a hydrophobic
tothesubstrate,aUBAdomaininUBQLNsbindstoubiquitin, sequencetoberecognizedbySRPtriggersArgonaute2-depen-
preventing substrate release and thereby ending insertion at- dentmRNAdecay.
tempts (Itakura et al., 2016). Presumably, the time allowed for These two examples illustrate a potentially important princi-
insertionisdependentontheaffinityoftheligaseforUBQLNs, ple (Figure 5). If an interaction critical for biogenesis occurs
itsabundance,andspeedofubiquitination.Identifyingtheligase co-translationally, its failure would necessarily result in an
shouldallowtheseaspectsofthemodeltobetested. orphan. There may be mechanisms to detect such failures
co-translationally,whichwouldprovidethecellularqualitycon-
CanFailuresBeDetectedCo-translationally? trolsystemsaccesstoboththenascentpolypeptideandasso-
The systems for detection and degradation of orphans dis- ciated mRNA. Although still poorly studied, there is evidence
cussedsofaralloperatepost-translationally.Thisisconsistent that many protein complexes may initiate assembly during
withtheideathatbiosynthesismustnecessarilyhaveanoppor- translation (Duncan and Mata, 2011; Williams and Dichtl,
tunity to succeed before a polypeptide is deemed an orphan. 2018). If such co-translational interactions were coupled to
However, many biosynthetic reactions are initiated or occur translationelongation,themRNAdecaypathwaysdownstream
co-translationally:recognitionbySRP,theinitialstagesofpoly- of ribosome stalling could be exploited to fine-tune the
peptide folding, various modifications, and even multi-subunit balanced expression of subunits and minimize the generation
MolecularCell71,August2,2018 451
MolecularCell
Review
normal conditions excess unassembled orphans Figure5. HypotheticalModelforCo-
translationalMonitoringofProtein
Assembly
A nascent polypeptide emerging from the ribo-
someisrecognizedbyanassemblyfactor,which
is recycled when assembly occurs correctly.
When assembly fails, the assembly factor is
titrated by excess unassembled orphans (right
side). The unavailability of this nascent chain
binding protein at the ribosome is proposed
assembly to trigger ribosome-associated quality control
factor feedback to pathway via effects on translation (red arrow),
translation & QC perhapsviafactors(notshown)thatbindtothe
...
... s
s
e
e
q
m
u
b
e
ly
nc
fa
e
c
m
to
o
r.
tif normally recognized by the as-
...
...
mRNA degradation
oforphans.Suchanearly-detectionsystemmayrepresentone processes such as assembly of a membrane cytoskeleton
ofthephysiologicrolesofribosome-associatedqualitycontrol (Weatherall and Clegg, 2001). As noted above, unassembled
pathways. Intriguingly, up to (cid:1)12%–15% of nascent proteins a-globinisselectivelyrecognized,ubiquitinated,anddegraded
might be ubiquitinated co-translationally at the ribosome for byUBE2O.However,thisdoesnotseemtobetheonlydegrada-
reasons that remain to be investigated (Duttler et al., 2013; tion pathway, as some a-globin ubiquitination was observed
Wangetal.,2013). even in UBE2O knockout cells (Nguyen et al., 2017). Further-
more, the pathway of unpaired b-globin degradation remains
Orphan-RelatedPathologies unknown.Thesemayprovetobeimportantfacetsofthepatho-
Aswithothertypesofqualitycontrol,suchasproteinmisfolding physiologyoftheThalassemias.
or processing, excessive production of orphans can be domi- Given the detrimental consequences of orphans, it is note-
nantly detrimental to cellular homeostasis. This is observed in worthythataneuploidyisaprominentfeatureinalargepropor-
thediseasephenotypesofvariousinheritedmutations.Raremu- tionofcancers(RajagopalanandLengauer,2004).Asthegenes
tationshavebeendescribedinthesignalsequencesofawide for different subunits of multi-protein complexes are often on
rangeofproteins(Cassanellietal.,1998;Karaplisetal.,1995; different chromosomes, aneuploidy would necessarily unbal-
Seppenetal.,1996).Inmostcases,themutationdisruptsthehy- anceexpression.Experimentsinyeasthaveshownthatduplica-
drophobiccoreofthesignaltoreduceoreliminateitstargeting tion of a single chromosome in an otherwise haploid cell is
function.Thiswouldleadtoanincreaseoforphansinthecytosol detrimental,whileanadditionalchromosomeinadiploidcellis
ofcellsexpressingthemutantprotein.Accordingly,thepheno- lessso(Dephoureetal.,2014;Dodgsonetal.,2016;Oromendia
types are typically dominant and tissue-specific to the most etal.,2012).Thissuggeststhatproteomeimbalancemayunder-
highlyexpressingcelltype.Thissuggeststhattheincreaseinor- liethefitnesscost,anideaconsistentwiththeobservedprotein
phans,notsimplyalossoffunction,isthebasisofcellulardam- homeostasis defects seen in aneuploid yeast. Experiments in
age. Inmouse studiesofthe non-essential prion protein(PrP), human cells induced to be aneuploid support the findings in
introduction of a version containing a signal sequence that is yeast (Ben-David et al., 2014; Stingele et al., 2012; Williams
only(cid:1)50%efficientledtoadominantneurodegenerativepheno- etal.,2008),yetaneuploidcancercellsparadoxicallygrowunre-
type (Rane et al., 2008). Thus, over long times in a complex strained. This might imply that they manage to grow robustly
organism, even a modest increase in the load of mislocalized despite aneuploidy, not because of it. Consistent with this
orphansinthecytosolcanbedetrimental. idea,manycancercellshavehigherlevelsofthemajorcytosolic
Perhapsthemostcommonsetofdiseasesinvolvingorphans chaperoneHsp70(Murphy,2013),elevatedproteasomeactivity
are the Thalassemias, a group of hereditary blood diseases (ChenandMadura,2005),andincreasedautophagy(Singhetal.,
characterized by anemia, hemolysis, and various downstream 2018).ItisalsonoteworthythatUBE2Oisamplifiedinmanycan-
consequences(Olivieri,1999;PielandWeatherall,2014).These cers, while reduction of UBE2O in different mouse cancer
diseasesresultwhenoneormoreoftheallelesencodinga-or models provides a benefit by attenuating tumor growth (Liang
b-globinisdeficient,resultinginimbalancedsynthesisofhemo- etal.,2017;Vilaetal.,2017).Thus,understandingthemecha-
globinsubunits.Mutationsinthea-binterfacethatimpairassem- nisticbasisoforphanrecognitionanddegradationmayprovide
blyofhemoglobinalsocauserarevariantsofanemiarelatedto newtherapeuticopportunitiesinanumberofcommondiseases
the Thalassemias (Clarke and Higgins, 2000; Kohne, 2011). rangingfromThalassemiastocancers.
Whileareducedlevelofmaturehemoglobiniscertainlyamajor
contributor to the pathogenesis of these diseases, substantial
evidenceindicatesthattheunpairedglobinproteinsaredomi- ACKNOWLEDGMENTS
nantlytoxicinmanyways.Forexample,unpaireda-orb-globin
WethankHegdelabmembersforusefuldiscussions.Workintheauthors’lab
hasbeensuggestedtogenerateincreasedreactiveoxygenspe-
is supported by the UK Medical Research Council (MC_UP_A022_1007
cies,formintracellularaggregates,orinterferewithothercellular toR.S.H.).
452 MolecularCell71,August2,2018
Molecular Cell
Review
REFERENCES sitylipoproteinreceptorgeneinanItaliansubjectwithprimaryhypercholester-
olemia.Clin.Genet.53,391–395.
Abovich,N.,Gritz,L.,Tung,L.,andRosbash,M.(1985).EffectofRP51gene
Chakrabarti,O.,Rane,N.S.,andHegde,R.S.(2011).Cytosolicaggregates
dosage alterations on ribosome synthesis in Saccharomyces cerevisiae.
Mol.Cell.Biol.5,3429–3435. p
M
e
o
r
l
t
.
u
B
rb
io
t
l
h
.
e
C
d
e
e
ll
g
2
r
2
a
,
d
1
a
6
ti
2
o
5
n
–
o
1
f
6
n
3
o
7
n
.
translocatedsecretoryandmembraneproteins.
Ames, B.N., and Martin, R.G. (1964). Biochemical Aspects of Genetics:
TheOperon.Annu.Rev.Biochem.33,235–258. Chartron,J.W.,Hunt,K.C.L.,andFrydman,J.(2016).Cotranslationalsignal-in-
dependentSRPpreloadingduringmembranetargeting.Nature536,224–228.
Babu,M.,Vlasblom,J.,Pu,S.,Guo,X.,Graham,C.,Bean,B.D.M.,Burston,
H.E.,Vizeacoumar,F.J.,Snider,J.,Phanse,S.,etal.(2012).Interactionland- Chen,L.,andMadura,K.(2005).Increasedproteasomeactivity,ubiquitin-
scapeofmembrane-proteincomplexesinSaccharomycescerevisiae.Nature conjugatingenzymes,andeEF1Atranslationfactordetectedinbreastcancer
489,585–589. tissue.CancerRes.65,5599–5606.
Bachurski, C.J., Theodorakis, N.G., Coulson, R.M., and Cleveland, D.W. Chen,Y.-C.,Umanah,G.K.E.,Dephoure,N.,Andrabi,S.A.,Gygi,S.P.,Daw-
(1994).Anamino-terminaltetrapeptidespecifiescotranslationaldegradation son,T.M.,Dawson,V.L.,andRutter,J.(2014).Msp1/ATAD1maintainsmito-
ofbeta-tubulinbutnotalpha-tubulinmRNAs.Mol.Cell.Biol.14,4076–4086. chondrialfunctionbyfacilitatingthedegradationofmislocalizedtail-anchored
proteins.EMBOJ.33,1548–1564.
Baumal,R.,Potter,M.,andScharff,M.D.(1971).Synthesis,assembly,and
secretionofgammaglobulinbymousemyelomacells.3.Assemblyofthe Clarke,G.M.,andHiggins,T.N.(2000).Laboratoryinvestigationofhemoglo-
threesubclassesofIgG.J.Exp.Med.134,1316–1334. binopathiesandthalassemias:reviewandupdate.Clin.Chem.46,1284–1290.
Ben-David,U.,Arad,G.,Weissbein,U.,Mandefro,B.,Maimon,A.,Golan-Lev, Claude,A.(1943).Theconstitutionofprotoplasm.Science97,451–456.
T.,Narwani,K.,Clark,A.T.,Andrews,P.W.,Benvenisty,N.,andCarlosBian-
cotti,J.(2014).Aneuploidyinducesprofoundchangesingeneexpression,pro- Claude, A. (1946). Fractionation of Mammalian Liver Cells By Differential
liferationandtumorigenicityofhumanpluripotentstemcells.Nat.Commun. Centrifugation: Ii. Experimental Procedures and Results. J. Exp. Med.
5,4825. 84,61–89.
Benz, E.J., Jr., and Forget, B.G. (1974). The biosynthesis of hemoglobin. Cleveland,D.W.,Lopata,M.A.,Sherline,P.,andKirschner,M.W.(1981).Un-
Semin.Hematol.11,463–523. polymerizedtubulinmodulatestheleveloftubulinmRNAs.Cell25,537–546.
Berndt,U.,Oellerer,S.,Zhang,Y.,Johnson,A.E.,andRospert,S.(2009).A Cosson,P.,Lankford,S.P.,Bonifacino,J.S.,andKlausner,R.D.(1991).Mem-
signal-anchorsequencestimulatessignalrecognitionparticlebindingtoribo- braneproteinassociationbypotentialintramembranechargepairs.Nature
somesfrominsidetheexittunnel.Proc.Natl.Acad.Sci.USA106,1398–1403. 351,414–416.
Besemer,J.,Harant,H.,Wang,S.,Oberhauser,B.,Marquardt,K.,Foster, Costa,E.A.,Subramanian,K.,Nunnari,J.,andWeissman,J.S.(2018).Defining
C.A.,Schreiner,E.P.,deVries,J.E.,Dascher-Nadel,C.,andLindley,I.J.D. thephysiologicalroleofSRPinprotein-targetingefficiencyandspecificity.
(2005). Selective inhibition of cotranslational translocation of vascular cell Science359,689–692.
adhesionmolecule1.Nature436,290–293.
Da´vilaLo´pez,M.,Martı´nezGuerra,J.J.,andSamuelsson,T.(2010).Analysisof
Blobel,G.(1980).Intracellularproteintopogenesis.Proc.Natl.Acad.Sci.USA geneorderconservationineukaryotesidentifiestranscriptionallyandfunction-
77,1496–1500. allylinkedgenes.PLoSONE5,e10654.
Bole, D.G., Hendershot, L.M., and Kearney, J.F. (1986). Posttranslational DeDuve,C.(1965).Theseparationandcharacterizationofsubcellularparti-
association of immunoglobulin heavy chain binding protein with nascent cles.HarveyLect.59,49–87.
heavy chains in nonsecreting and secreting hybridomas. J. Cell Biol.
102, 1558–1566. Dephoure,N.,Hwang,S.,O’Sullivan,C.,Dodgson,S.E.,Gygi,S.P.,Amon,A.,
andTorres,E.M.(2014).Quantitativeproteomicanalysisrevealsposttransla-
Bonde,M.T.,Pedersen,M.,Klausen,M.S.,Jensen,S.I.,Wulff,T.,Harrison,S., tionalresponsestoaneuploidyinyeast.eLife3,e03023.
Nielsen,A.T.,Herrga˚rd,M.J.,andSommer,M.O.A.(2016).Predictabletuning
ofproteinexpressioninbacteria.Nat.Methods13,233–236.
Dodgson,S.E.,Kim,S.,Costanzo,M.,Baryshnikova,A.,Morse,D.L.,Kaiser,
C.A.,Boone,C.,andAmon,A.(2016).Chromosome-specificandglobalef-
Bonifacino,J.S.,andLippincott-Schwartz,J.(1991).Degradationofproteins fectsofaneuploidyinSaccharomycescerevisiae.Genetics202,1395–1409.
withintheendoplasmicreticulum.Curr.Opin.CellBiol.3,592–600.
Drisaldi,B.,Stewart,R.S.,Adles,C.,Stewart,L.R.,Quaglio,E.,Biasini,E.,Fior-
Bonifacino,J.S.,Suzuki,C.K.,Lippincott-Schwartz,J.,Weissman,A.M.,and
iti,L.,Chiesa,R.,andHarris,D.A.(2003).MutantPrPisdelayedinitsexitfrom
Klausner,R.D.(1989).Pre-GolgidegradationofnewlysynthesizedT-cellanti-
theendoplasmicreticulum,butneitherwild-typenormutantPrPundergoes
g J. e C n e r l e l c B e io p l t . o 1 r 0 c 9 h , a 7 i 3 n – s 8 : 3 in . trinsic sensitivity and the role of subunit assembly. retrotranslocation prior to proteasomal degradation. J. Biol. Chem. 278,
21732–21743.
Bonifacino, J.S., Cosson, P.,Shah,N.,and Klausner, R.D. (1991).Role of
Duncan,C.D.S.,andMata,J.(2011).Widespreadcotranslationalformationof
potentiallychargedtransmembraneresiduesintargetingproteinsforretention
anddegradationwithintheendoplasmicreticulum.EMBOJ.10,2783–2793.
proteincomplexes.PLoSGenet.7,e1002398.
Braunger,K.,Pfeffer,S.,Shrimal,S.,Gilmore,R.,Berninghausen,O.,Mandon, Duttler,S.,Pechmann,S.,andFrydman,J.(2013).Principlesofcotranslational
E.C.,Becker,T.,Fo¨rster,F.,andBeckmann,R.(2018).Structuralbasisfor
ubiquitinationandqualitycontrolattheribosome.Mol.Cell50,379–393.
couplingproteintransportandN-glycosylationatthemammalianendoplasmic
reticulum.Science360,215–219. Emanuelsson,O.,Brunak,S.,vonHeijne,G.,andNielsen,H.(2007).Locating
proteinsinthecellusingTargetP,SignalPandrelatedtools.Nat.Protoc.2,
Brewer,J.W.,andHendershot,L.M.(2005).Buildinganantibodyfactory:ajob 953–971.
fortheunfoldedproteinresponse.Nat.Immunol.6,23–29.
Feige,M.J.,andHendershot,L.M.(2013).Qualitycontrolofintegralmembrane
Brodsky,J.L.,Goeckeler,J.,andSchekman,R.(1995).BiPandSec63pare proteins by assembly-dependent membrane integration. Mol. Cell 51,
requiredforbothco-andposttranslationalproteintranslocationintotheyeast 297–309.
endoplasmicreticulum.Proc.Natl.Acad.Sci.USA92,9643–9646.
Feige,M.J.,Groscurth,S.,Marcinowski,M.,Shimizu,Y.,Kessler,H.,Hender-
Caramelo,J.J.,andParodi,A.J.(2015).Asweetcodeforglycoproteinfolding. shot,L.M.,andBuchner,J.(2009).AnunfoldedCH1domaincontrolstheas-
FEBSLett.589,3379–3387. semblyandsecretionofIgGantibodies.Mol.Cell34,569–579.
Cassanelli,S.,Bertolini,S.,Rolleri,M.,DeStefano,F.,Casarino,L.,Elicio,N., Feit,H.,Slusarek,L.,andShelanski,M.L.(1971).Heterogeneityoftubulinsub-
Naselli,A.,andCalandra,S.(1998).A‘denovo’pointmutationofthelow-den- units.Proc.Natl.Acad.Sci.USA68,2028–2031.
MolecularCell71,August2,2018 453
MolecularCell
Review
Feng,L.,Gell,D.A.,Zhou,S.,Gu,L.,Kong,Y.,Li,J.,Hu,M.,Yan,N.,Lee,C., Itakura,E.,Zavodszky,E.,Shao,S.,Wohlever,M.L.,Keenan,R.J.,andHegde,
Rich,A.M.,etal.(2004).MolecularmechanismofAHSP-mediatedstabilization R.S.(2016).Ubiquilinschaperoneandtriagemitochondrialmembraneproteins
ofa-hemoglobin.Cell119,629–640. fordegradation.Mol.Cell63,21–33.
Feng,L.,Zhou,S.,Gu,L.,Gell,D.A.,Mackay,J.P.,Weiss,M.J.,Gow,A.J.,and Itzhak,D.N.,Tyanova,S.,Cox,J.,andBorner,G.H.(2016).Global,quantitative
Shi,Y.(2005).Structureofoxidizeda-haemoglobinboundtoAHSPrevealsa anddynamicmappingofproteinsubcellularlocalization.eLife5,https://doi.
protectivemechanismforhaem.Nature435,697–701. org/10.7554/eLife.16950.
Fons,R.D.,Bogert,B.A.,andHegde,R.S.(2003).Substrate-specificfunction Jacob,H.S.,Brain,M.C.,Dacie,J.V.,Carrell,R.W.,andLehmann,H.(1968).
ofthetranslocon-associatedproteincomplexduringtranslocationacrossthe AbnormalhaembindingandglobinSHgroupblockadeinunstablehaemoglo-
ERmembrane.J.CellBiol.160,529–539. bins.Nature218,1214–1217.
Gamerdinger,M.,Hanebuth,M.A.,Frickey,T.,andDeuerling,E.(2015).The Ja€kel, S., and Go¨rlich, D. (1998). Importin beta, transportin, RanBP5 and
principle of antagonism ensures protein targeting specificity at the endo- RanBP7mediatenuclearimportofribosomalproteinsinmammaliancells.
plasmicreticulum.Science348,201–207. EMBOJ.17,4491–4502.
Garrison,J.L.,Kunkel,E.J.,Hegde,R.S.,andTaunton,J.(2005).Asubstrate- Ja€kel, S., Mingot, J.-M., Schwarzmaier, P., Hartmann, E., and Go¨rlich, D.
specificinhibitorofproteintranslocationintotheendoplasmicreticulum.Na- (2002).Importinsfulfiladualfunctionasnuclearimportreceptorsandcyto-
ture436,285–289. plasmicchaperonesforexposedbasicdomains.EMBOJ.21,377–386.
Gavin,A.C.,Aloy,P.,Grandi,P.,Krause,R.,Boesche,M.,Marzioch,M.,Rau, Jonikas,M.C.,Collins,S.R.,Denic,V.,Oh,E.,Quan,E.M.,Schmid,V.,Weibe-
C.,Jensen,L.J.,Bastuck,S.,Du€mpelfeld,B.,etal.(2006).Proteomesurveyre-
zahn,J.,Schwappach,B.,Walter,P.,Weissman,J.S.,andSchuldiner,M.
vealsmodularityoftheyeastcellmachinery.Nature440,631–636.
(2009).Comprehensivecharacterizationofgenesrequiredforproteinfolding
intheendoplasmicreticulum.Science323,1693–1697.
Gay,D.A.,Sisodia,S.S.,andCleveland,D.W.(1989).Autoregulatorycontrolof
beta-tubulin mRNA stability is linked to translation elongation. Proc. Natl. Kang,S.-W.,Rane,N.S.,Kim,S.J.,Garrison,J.L.,Taunton,J.,andHegde,
Acad.Sci.USA86,5763–5767.
R.S.(2006).Substrate-specifictranslocationalattenuationduringERstress
definesapre-emptivequalitycontrolpathway.Cell127,999–1013.
Guna,A.,andHegde,R.S.(2018).Transmembranedomainrecognitionduring
membraneproteinbiogenesisandqualitycontrol.Curr.Biol.28,R498–R511.
Karamyshev,A.L.,Patrick,A.E.,Karamysheva,Z.N.,Griesemer,D.S.,Hudson,
H.,Tjon-Kon-Sang,S.,Nilsson,I.,Otto,H.,Liu,Q.,Rospert,S.,etal.(2014).
Haas,I.G.,andWabl,M.(1983).Immunoglobulinheavychainbindingprotein.
InefficientSRPinteractionwithanascentchaintriggersamRNAqualitycontrol
Nature306,387–389.
pathway.Cell156,146–157.
Halic,M.,Becker,T.,Pool,M.R.,Spahn,C.M.T.,Grassucci,R.A.,Frank,J.,
Karaplis,A.C.,Lim,S.K.,Baba,H.,Arnold,A.,andKronenberg,H.M.(1995).
andBeckmann,R.(2004).Structureofthesignalrecognitionparticleinteract-
ingwiththeelongation-arrestedribosome.Nature427,808–814. Inefficientmembranetargeting,translocation,andproteolyticprocessingby
signal peptidase of a mutant preproparathyroid hormone protein. J. Biol.
Chem.270,1629–1635.
Hammond,C.M.,Strømme,C.B.,Huang,H.,Patel,D.J.,andGroth,A.(2017).
Histonechaperonenetworksshapingchromatinfunction.Nat.Rev.Mol.Cell
Biol.18,141–158.
r
K
e
e
c
e
o
n
g
a
n
n
it
,
io
R
n
.J
p
.,
a
F
rt
r
i
e
c
y
le
m
.
a
A
n
n
n
n
,
u
D
.
.
R
M
e
.
v
,
.
S
B
tr
i
o
o
u
c
d
h
,
e
R
m
.
.
M
7
.
0
,
,
a
7
n
5
d
5
W
–7
a
7
lt
5
e
.
r,P.(2001).Thesignal
Harbauer,A.B.,Opalin(cid:2)ska,M.,Gerbeth,C.,Herman,J.S.,Rao,S.,Scho¨nfisch,
Kihm,A.J.,Kong,Y.,Hong,W.,Russell,J.E.,Rouda,S.,Adachi,K.,Simon,
B.,Guiard,B.,Schmidt,O.,Pfanner,N.,andMeisinger,C.(2014).Mitochon-
M.C., Blobel, G.A., and Weiss, M.J. (2002).Anabundant erythroid protein
d
S
r
c
ia
ie
.
n
C
c
e
e
ll
3
c
4
y
6
c
,
le
1
-
1
d
0
e
9
p
–
e
1
n
1
d
1
e
3
n
.
tregulationofmitochondrialpreproteintranslocase. thatstabilizesfreealpha-haemoglobin.Nature417,758–763.
Kikkert,M.,Doolman,R.,Dai,M.,Avner,R.,Hassink,G.,vanVoorden,S.,Tha-
Harper,J.W.,andBennett,E.J.(2016).Proteomecomplexityandtheforces
thatdriveproteomeimbalance.Nature537,328–338. nedar,S.,Roitelman,J.,Chau,V.,andWiertz,E.(2004).HumanHRD1isanE3
ubiquitin ligase involved in degradation of proteins from the endoplasmic
Havugimana, P.C., Hart, G.T., Nepusz, T., Yang, H., Turinsky, A.L., Li, Z.,
reticulum.J.Biol.Chem.279,3525–3534.
Wang,P.I.,Boutz,D.R.,Fong,V.,Phanse,S.,etal.(2012).Acensusofhuman
solubleproteincomplexes.Cell150,1068–1081. Kim,S.J.,Mitra,D.,Salerno,J.R.,andHegde,R.S.(2002).Signalsequences
control gating of the protein translocation channel in a substrate-specific
Hegde,R.S.,andKeenan,R.J.(2011).Tail-anchoredmembraneproteininser-
manner.Dev.Cell2,207–217.
tionintotheendoplasmicreticulum.Nat.Rev.Mol.CellBiol.12,787–798.
Kohne,E.(2011).Hemoglobinopathies:clinicalmanifestations,diagnosis,and
Hendershot,L.,Bole,D.,Ko¨hler,G.,andKearney,J.F.(1987).Assemblyand
treatment.Dtsch.Arztebl.Int.108,532–540.
secretionofheavychainsthatdonotassociateposttranslationallywithimmu-
noglobulinheavychain-bindingprotein.J.CellBiol.104,761–767. Koren,I.,Timms,R.T.,Kula,T.,Xu,Q.,Li,M.Z.,andElledge,S.J.(2018).The
EukaryoticProteomeIsShapedbyE3UbiquitinLigasesTargetingC-Terminal
Hentze,M.W.,Castello,A.,Schwarzl,T.,andPreiss,T.(2018).Abravenew
Degrons.Cell173,1622–1635.e14.
worldofRNA-bindingproteins.Nat.Rev.Mol.CellBiol.19,327–341.
Krogan,N.J.,Cagney,G.,Yu,H.,Zhong,G.,Guo,X.,Ignatchenko,A.,Li,J.,
Hessa, T., Sharma, A., Mariappan, M., Eshleman, H.D., Gutierrez, E., and Pu,S.,Datta,N.,Tikuisis,A.P.,etal.(2006).Globallandscapeofproteincom-
Hegde,R.S.(2011).Proteintargetinganddegradationarecoupledforelimina- plexesintheyeastSaccharomycescerevisiae.Nature440,637–643.
tionofmislocalizedproteins.Nature475,394–397.
Kulak,N.A.,Pichler,G.,Paron,I.,Nagaraj,N.,andMann,M.(2014).Minimal,
Horie,C.,Suzuki,H.,Sakaguchi,M.,andMihara,K.(2002).Characterizationof encapsulatedproteomic-sampleprocessingappliedtocopy-numberestima-
signalthatdirectsC-tail-anchoredproteinstomammalianmitochondrialouter tionineukaryoticcells.Nat.Methods11,319–324.
membrane.Mol.Biol.Cell13,1615–1625.
Lakkaraju,A.K.,Abrami,L.,Lemmin,T.,Blaskovic,S.,Kunz,B.,Kihara,A.,Dal
Hosokawa, N., Wada, I., Hasegawa, K., Yorihuzi, T., Tremblay, L.O., Her- Peraro,M.,andvanderGoot,F.G.(2012).Palmitoylatedcalnexinisakey
scovics,A.,andNagata,K.(2001).AnovelERalpha-mannosidase-likeprotein componentoftheribosome-transloconcomplex.EMBOJ.31,1823–1835.
acceleratesER-associateddegradation.EMBORep.2,415–422.
Lee,J.W.,Zemojtel,T.,andShakhnovich,E.(2009).Systems-levelevidenceof
Huber, R., Deisenhofer, J., Colman, P.M., Matsushima, M., and Palm, W. transcriptionalco-regulationofyeastproteincomplexes.J.Comput.Biol.16,
(1976).CrystallographicstructurestudiesofanIgGmoleculeandanFcfrag- 331–339.
ment.Nature264,415–420.
Levine,C.G.,Mitra,D.,Sharma,A.,Smith,C.L.,andHegde,R.S.(2005).The
Huppa,J.B.,andPloegh,H.L.(1997).ThealphachainoftheTcellantigenre- efficiencyofproteincompartmentalizationintothesecretorypathway.Mol.
ceptorisdegradedinthecytosol.Immunity7,113–122. Biol.Cell16,279–291.
454 MolecularCell71,August2,2018
Molecular Cell
Review
Li,G.-W.,Burkhardt,D.,Gross,C.,andWeissman,J.S.(2014).Quantifyingab- Nargund,A.M.,Pellegrino,M.W.,Fiorese,C.J.,Baker,B.M.,andHaynes,C.M.
solute protein synthesis rates reveals principles underlying allocation of (2012).MitochondrialimportefficiencyofATFS-1regulatesmitochondrialUPR
cellularresources.Cell157,624–635. activation.Science337,587–590.
Liang,K.,Volk,A.G.,Haug,J.S.,Marshall,S.A.,Woodfin,A.R.,Bartom,E.T., Nelson,H.C.(1995).StructureandfunctionofDNA-bindingproteins.Curr.
Gilmore,J.M.,Florens,L.,Washburn,M.P.,Sullivan,K.D.,etal.(2017).Ther- Opin.Genet.Dev.5,180–189.
apeuticTargetingofMLLDegradationPathwaysinMLL-RearrangedLeuke-
mia.Cell168,59–72.e13. Ng,D.T.,Brown,J.D.,andWalter,P.(1996).Signalsequencesspecifythetar-
geting route to the endoplasmic reticulum membrane. J. Cell Biol. 134,
Lim,H.N.,Lee,Y.,andHussein,R.(2011).Fundamentalrelationshipbetween 269–278.
operonorganizationandgeneexpression.Proc.Natl.Acad.Sci.USA108,
10626–10631. Nguyen,A.T.,Prado,M.A.,Schmidt,P.J.,Sendamarai,A.K.,Wilson-Grady,
J.T.,Min,M.,Campagna,D.R.,Tian,G.,Shi,Y.,Dederer,V.,etal.(2017).
Lin,H.-C.,Yeh,C.-W.,Chen,Y.-F.,Lee,T.-T.,Hsieh,P.-Y.,Rusnac,D.V.,Lin, UBE2Oremodelstheproteomeduringterminalerythroiddifferentiation.Sci-
S.-Y.,Elledge,S.J.,Zheng,N.,andYen,H.S.(2018).C-TerminalEnd-Directed ence357,eaan0218.
ProteinEliminationbyCRL2UbiquitinLigases.Mol.Cell70,602–613.e3.
Okreglak,V.,andWalter,P.(2014).TheconservedAAA-ATPaseMsp1confers
Lippincott-Schwartz, J., Bonifacino, J.S., Yuan, L.C., and Klausner, R.D. organellespecificitytotail-anchoredproteins.Proc.Natl.Acad.Sci.USA111,
(1988).Degradationfromtheendoplasmicreticulum:disposingofnewlysyn-
8019–8024.
thesizedproteins.Cell54,209–220.
Olivieri,N.F.(1999).Theb-thalassemias.N.Engl.J.Med.341,99–109.
Ma,J.,andLindquist,S.(2001).Wild-typePrPandamutantassociatedwith
priondiseasearesubjecttoretrogradetransportandproteasomedegrada-
tion.Proc.Natl.Acad.Sci.USA98,14955–14960. O
pr
r
o
o
t
m
eo
e
t
n
o
d
x
i
i
a
c
,
s
A
tr
.
e
B
s
.,
s
D
in
o
y
d
e
g
a
s
s
o
t
n
.
,
G
S
e
.
n
E
e
.
s
,a
D
n
e
d
v.
A
2
m
6,
o
2
n
6
,
9
A
6
.
–2
(2
7
0
0
1
8
2
.
).Aneuploidycauses
Mancini,R.,Fagioli,C.,Fra,A.M.,Maggioni,C.,andSitia,R.(2000).Degrada-
tionofunassembledsolubleIgsubunitsbycytosolicproteasomes:evidence Palade, G.E. (1955). A small particulate component of the cytoplasm.
that retrotranslocation and degradation are coupled events. FASEB J. 14, J.Biophys.Biochem.Cytol.1,59–68.
769–778.
Park,S.-H.,Bolender,N.,Eisele,F.,Kostova,Z.,Takeuchi,J.,Coffino,P.,and
Manolios,N.,Bonifacino,J.S.,andKlausner,R.D.(1990).Transmembranehe- Wolf,D.H.(2007).ThecytoplasmicHsp70chaperonemachinerysubjectsmis-
licalinteractionsandtheassemblyoftheTcellreceptorcomplex.Science249, foldedandendoplasmicreticulumimport-incompetentproteinstodegrada-
274–277.
tionviatheubiquitin-proteasomesystem.Mol.Biol.Cell18,153–165.
Marsh,J.A.,Herna´ndez,H.,Hall,Z.,Ahnert,S.E.,Perica,T.,Robinson,C.V., Pen˜a,C.,Hurt,E.,andPanse,V.G.(2017).Eukaryoticribosomeassembly,
andTeichmann,S.A.(2013).Proteincomplexesareunderevolutionaryselec- transportandqualitycontrol.Nat.Struct.Mol.Biol.24,689–699.
tiontoassembleviaorderedpathways.Cell153,461–470.
Perutz,M.F.,Rossmann,M.G.,Cullis,A.F.,Muirhead,H.,Will,G.,andNorth,
Matlack,K.E.,Misselwitz,B.,Plath,K.,andRapoport,T.A.(1999).BiPactsasa A.C.T.(1960).Structureofhaemoglobin:athree-dimensionalFouriersynthesis
molecular ratchet during posttranslational transport of prepro-alpha factor at5.5-A.resolution,obtainedbyX-rayanalysis.Nature185,416–422.
acrosstheERmembrane.Cell97,553–564.
Pfeffer,S.,Dudek,J.,Zimmermann,R.,andFo¨rster,F.(2016).Organizationof
Mayor,T.,Lipford,J.R.,Graumann,J.,Smith,G.T.,andDeshaies,R.J.(2005). thenativeribosome-transloconcomplexatthemammalianendoplasmicretic-
AnalysisofpolyubiquitinconjugatesrevealsthattheRpn10substratereceptor ulummembrane.Biochim.Biophys.Acta1860,2122–2129.
contributestotheturnoverofmultipleproteasometargets.Mol.Cell.Prote-
omics4,741–751. Piel,F.B.,andWeatherall,D.J.(2014).Thea-thalassemias.N.Engl.J.Med.
371,1908–1916.
Mayor,T.,Graumann,J.,Bryan,J.,MacCoss,M.J.,andDeshaies,R.J.(2007).
Quantitativeprofilingofubiquitylatedproteinsrevealsproteasomesubstrates Pittenger,M.F.,andCleveland,D.W.(1985).Retentionofautoregulatorycon-
andthesubstraterepertoireinfluencedbytheRpn10receptorpathway.Mol. troloftubulinsynthesisincytoplasts:demonstrationofacytoplasmicmecha-
Cell.Proteomics6,1885–1895. nismthatregulatestheleveloftubulinexpression.J.CellBiol.101,1941–1952.
McShane,E.,Sin,C.,Zauber,H.,Wells,J.N.,Donnelly,N.,Wang,X.,Hou,J., Porter, K.R. (1955–1956). The submicroscopic morphology of protoplasm.
Chen,W.,Storchova,Z.,Marsh,J.A.,etal.(2016).Kineticanalysisofprotein HarveyLect.51,175–228.
stabilityrevealsage-dependentdegradation.Cell167,803–815.e21.
Rajagopalan,H.,andLengauer,C.(2004).Aneuploidyandcancer.Nature432,
Meyuhas,O.,andKahan,T.(2015).Theracetodecipherthetopsecretsof
338–341.
TOPmRNAs.Biochim.Biophys.Acta1849,801–811.
Rane,N.S.,Yonkovich,J.L.,andHegde,R.S.(2004).Protectionfromcytosolic
Minami,R.,Hayakawa,A.,Kagawa,H.,Yanagi,Y.,Yokosawa,H.,andKawa- prion protein toxicity by modulation of protein translocation. EMBO J. 23,
hara,H.(2010).BAG-6isessentialforselectiveeliminationofdefectiveprotea-
somalsubstrates.J.CellBiol.190,637–650. 4550–4559.
Rane,N.S.,Kang,S.-W.,Chakrabarti,O.,Feigenbaum,L.,andHegde,R.S.
Miyazaki,Y.,Chen,L.C.,Chu,B.W.,Swigut,T.,andWandless,T.J.(2015).
(2008).ReducedtranslocationofnascentprionproteinduringERstresscon-
Distincttranscriptionalresponseselicitedbyunfoldednuclearorcytoplasmic
proteininmammaliancells.eLife4,https://doi.org/10.7554/eLife.07687.
tributestoneurodegeneration.Dev.Cell15,359–370.
Mock,J.-Y.,Chartron,J.W.,Zaslaver,M.,Xu,Y.,Ye,Y.,andClemons,W.M., Rane,N.S.,Chakrabarti,O.,Feigenbaum,L.,andHegde,R.S.(2010).Signal
Jr.(2015).Bag6complexcontainsaminimaltail-anchor-targetingmoduleand sequence insufficiency contributes toneurodegeneration caused by trans-
amockBAGdomain.Proc.Natl.Acad.Sci.USA112,106–111. membraneprionprotein.J.CellBiol.188,515–526.
Mulvey, C.M., Breckels, L.M., Geladaki, A., Britov(cid:3)sek, N.K., Nightingale, Rapoport,T.A.,Li,L.,andPark,E.(2017).Structuralandmechanisticinsights
D.J.H., Christoforou, A., Elzek, M., Deery, M.J., Gatto, L., and Lilley, K.S.
intoproteintranslocation.Annu.Rev.CellDev.Biol.33,369–390.
(2017).UsinghyperLOPITtoperformhigh-resolutionmappingofthespatial
proteome.Nat.Protoc.12,1110–1135. Rieder,R.F.(1974).Humanhemoglobinstabilityandinstability:molecular
mechanisms and some clinical correlations. Semin. Hematol. 11,
Munsky,B.,Neuert,G.,andvanOudenaarden,A.(2012).Usinggeneexpres- 423–440.
sionnoisetounderstandgeneregulation.Science336,183–187.
Rodrigo-Brenni,M.C.,Gutierrez,E.,andHegde,R.S.(2014).Cytosolicquality
Murphy, M.E. (2013). The HSP70 family and cancer. Carcinogenesis 34, controlofmislocalizedproteinsrequiresRNF126recruitmenttoBag6.Mol.
1181–1188. Cell55,227–237.
MolecularCell71,August2,2018 455
MolecularCell
Review
Sato,B.K.,Schulz,D.,Do,P.H.,andHampton,R.Y.(2009).Misfoldedmem- Vanhove,M.,Usherwood,Y.K.,andHendershot,L.M.(2001).UnassembledIg
braneproteinsarespecificallyrecognizedbythetransmembranedomainof heavychainsdonotcyclefromBiPinvivobutrequirelightchainstotrigger
theHrd1pubiquitinligase.Mol.Cell34,212–222. theirrelease.Immunity15,105–114.
Sauer,R.T.,andBaker,T.A.(2011).AAA+proteases:ATP-fueledmachinesof Vembar,S.S.,andBrodsky,J.L.(2008).Onestepatatime:endoplasmicretic-
proteindestruction.Annu.Rev.Biochem.80,587–612. ulum-associateddegradation.Nat.Rev.Mol.CellBiol.9,944–957.
Scazzari,M.,Amm,I.,andWolf,D.H.(2015).Qualitycontrolofacytoplasmic Vila,I.K.,Yao,Y.,Kim,G.,Xia,W.,Kim,H.,Kim,S.J.,Park,M.K.,Hwang,J.P.,
protein complex: chaperone motors and the ubiquitin-proteasome system
Gonza´lez-Billalabeitia,E.,Hung,M.C.,etal.(2017).AUBE2O-AMPKa2axis
governthefateoforphanfattyacidsynthasesubunitFas2ofyeast.J.Biol. thatpromotestumorinitiationandprogressionoffersopportunitiesfortherapy.
Chem.290,4677–4687. CancerCell31,208–224.
Schmidt,O.,Harbauer,A.B.,Rao,S.,Eyrich,B.,Zahedi,R.P.,Stojanovski,D., Vitali,D.G.,Sinzel,M.,Bulthuis,E.P.,Kolb,A.,Zabel,S.,Mehlhorn,D.G.,Fig-
Scho¨nfisch, B., Guiard, B., Sickmann, A., Pfanner, N., and Meisinger, C.
ueiredoCosta,B.,Farkas,A´.,Clancy,A.,Schuldiner,M.,etal.(2018).TheGET
(2011).Regulationofmitochondrialproteinimportbycytosolickinases.Cell pathwaycanincreasetheriskofmitochondrialoutermembraneproteinstobe
144,227–239. mistargetedtotheER.J.CellSci.131,jcs211110.
Voigt, S., Jungnickel, B., Hartmann, E., and Rapoport, T.A. (1996). Signal
Schoebel,S.,Mi,W.,Stein,A.,Ovchinnikov,S.,Pavlovicz,R.,DiMaio, F.,
sequence-dependentfunctionoftheTRAMproteinduringearlyphasesofpro-
Baker,D.,Chambers,M.G.,Su,H.,Li,D.,etal.(2017).Cryo-EMstructureof
tein transport across the endoplasmic reticulum membrane. J. Cell Biol.
the protein-conducting ERAD channel Hrd1 in complex with Hrd3. Nature
548,352–355.
134,25–35.
vonHeijne,G.(1995).Proteinsortingsignals:simplepeptideswithcomplex
Schuldiner, M., Metz, J., Schmid, V., Denic, V., Rakwalska, M., Schmitt, functions.EXS73,67–76.
H.D.,Schwappach,B.,andWeissman,J.S.(2008).TheGETcomplexme-
diates insertionoftail-anchored proteinsintothe ERmembrane.Cell134,
Voorhees, R.M., and Hegde, R.S. (2015). Structures of the scanning and
634–645. engagedstatesofthemammalianSRP-ribosomecomplex.eLife4,https://
doi.org/10.7554/eLife.07975.
Seppen, J., Steenken, E., Lindhout, D., Bosma, P.J., and Elferink, R.P.
(1996). A mutation which disrupts the hydrophobic core of the signal Wang,X.,andChen,X.J.(2015).Acytosolicnetworksuppressingmitochon-
peptide of bilirubin UDP-glucuronosyltransferase, an endoplasmic reticu- dria-mediatedproteostaticstressandcelldeath.Nature524,481–484.
lum membrane protein, causes Crigler-Najjar type II. FEBS Lett. 390,
294–298. Wang,Q.,Liu,Y.,Soetandyo,N.,Baek,K.,Hegde,R.,andYe,Y.(2011).
Aubiquitinligase-associatedchaperoneholdasemaintainspolypeptidesin
Shao,S.,andHegde,R.S.(2011).Membraneproteininsertionattheendo- solublestatesforproteasomedegradation.Mol.Cell42,758–770.
plasmicreticulum.Annu.Rev.CellDev.Biol.27,25–56.
Wang,F.,Durfee,L.A.,andHuibregtse,J.M.(2013).Acotranslationalubiq-
Shao,S.,Rodrigo-Brenni,M.C.,Kivlen,M.H.,andHegde,R.S.(2017).Mech- uitination pathway for quality control of misfolded proteins. Mol. Cell 50,
anisticbasisforamoleculartriagereaction.Science355,298–302. 368–378.
Shemorry,A.,Hwang,C.S.,andVarshavsky,A.(2013).Controlofproteinqual- Warner, J.R.,Mitra, G.,Schwindinger, W.F., Studeny, M., and Fried, H.M.
ityandstoichiometriesbyN-terminalacetylationandtheN-endrulepathway. (1985).Saccharomycescerevisiaecoordinates accumulationofyeastribo-
Mol.Cell50,540–551. somalproteinsbymodulatingmRNAsplicing,translationalinitiation,andpro-
teinturnover.Mol.Cell.Biol.5,1512–1521.
Shen,Y.,andHendershot,L.M.(2005).ERdj3,astress-inducibleendoplasmic
reticulumDnaJhomologue,servesasacofactorforBiP’sinteractionswith Wattenberg,B.W.,Clark,D.,andBrock,S.(2007).Anartificialmitochondrial
unfoldedsubstrates.Mol.Biol.Cell16,40–50. tailsignal/anchorsequenceconfirmsarequirementformoderatehydropho-
bicityfortargeting.Biosci.Rep.27,385–401.
Shoemaker,C.J.,andGreen,R.(2012).TranslationdrivesmRNAqualitycon-
trol.Nat.Struct.Mol.Biol.19,594–601. Weatherall,D.J.,andClegg,J.B.(2001).Thethalassaemiasyndromes,4thedi-
tion(BlackwellPubl.Ltd.),pp.132–174.
Singh,S.S.,Vats,S.,Chia,A.Y.-Q.,Tan,T.Z.,Deng,S.,Ong,M.S.,Arfuso,F.,
Yap,C.T.,Goh,B.C.,Sethi,G.,etal.(2018).Dualroleofautophagyinhall- Wefes,I.,Mastrandrea,L.D.,Haldeman,M.,Koury,S.T.,Tamburlin,J.,Pickart,
marksofcancer.Oncogene37,1142–1158. C.M.,andFinley,D.(1995).Inductionofubiquitin-conjugatingenzymesduring
terminalerythroiddifferentiation.Proc.Natl.Acad.Sci.USA92,4982–4986.
Stingele,S.,Stoehr,G.,Peplowska,K.,Cox,J.,Mann,M.,andStorchova,Z.
Weidberg,H.,andAmon,A.(2018).MitoCPR-Asurveillancepathwaythatpro-
(2012).Globalanalysisofgenome,transcriptomeandproteomerevealsthe
responsetoaneuploidyinhumancells.Mol.Syst.Biol.8,608. tects mitochondria in response to protein import stress. Science 360,
eaan4146.
Sung,M.-K.,Porras-Yakushi,T.R.,Reitsma,J.M.,Huber,F.M.,Sweredoski,
Weir,N.R.,Kamber,R.A.,Martenson,J.S.,andDenic,V.(2017).TheAAApro-
M.J.,Hoelz,A.,Hess,S.,andDeshaies,R.J.(2016).Aconservedquality-con-
tein Msp1 mediates clearance of excess tail-anchored proteins from the
t
e
r
L
o
i
l
fe
pa
5
t
,
h
h
w
tt
a
p
y
s:
t
/
h
/d
at
oi
m
.o
e
rg
d
/
ia
1
t
0
e
.
s
75
d
5
e
4
g
/
r
e
a
L
d
if
a
e
t
.
i
1
o
9
n
1
o
0
f
5
u
.
nassembledribosomalproteins. peroxisomalmembrane.eLife6,https://doi.org/10.7554/eLife.28507.
Wickner,W.,andSchekman,R.(2005).Proteintranslocationacrossbiological
Suzuki,R.,andKawahara,H.(2016).UBQLN4recognizesmislocalizedtrans- membranes.Science310,1452–1456.
membranedomainproteinsandtargetsthesetoproteasomaldegradation.
EMBORep.17,842–857.
Wiedemann,N.,andPfanner,N.(2017).Mitochondrialmachineriesforprotein
importandassembly.Annu.Rev.Biochem.86,685–714.
Tannous, A., Pisoni, G.B., Hebert, D.N., and Molinari, M. (2015). N-linked
sugar-regulated protein folding and quality control in the ER. Semin. Cell Wiedmann,B.,Sakai,H.,Davis,T.A.,andWiedmann,M.(1994).Aprotein
Dev.Biol.41,79–89. complexrequiredforsignal-sequence-specificsortingandtranslocation.Na-
ture370,434–440.
Tasaki,T.,Sriram,S.M.,Park,K.S.,andKwon,Y.T.(2012).TheN-endrule
pathway.Annu.Rev.Biochem.81,261–289. Williams,N.K.,andDichtl,B.(2018).Co-translationalcontrolofproteincom-
plex formation: a fundamental pathway of cellular organization? Biochem.
Theodorakis,N.G.,andCleveland,D.W.(1992).Physicalevidenceforcotrans- Soc.Trans.46,197–206.
lational regulation of beta-tubulin mRNA degradation. Mol. Cell. Biol. 12,
791–799. Williams, B.R., Prabhu, V.R., Hunter, K.E., Glazier, C.M., Whittaker, C.A.,
Housman, D.E., and Amon, A. (2008). Aneuploidy affects proliferation
UniProt Consortium (2018). UniProt: the universal protein knowledgebase. and spontaneous immortalization in mammalian cells. Science 322,
NucleicAcidsRes.46,2699–2699. 703–709.
456 MolecularCell71,August2,2018
Molecular Cell
Review
Wohlever, M.L., Mateja, A., McGilvray, P.T., Day, K.J., and Keenan, R.J. Mistargeted mitochondrialproteins activate a proteostatic response in the
(2017). Msp1 Is a membrane protein dislocase for tail-anchored proteins. cytosol.Nature524,485–488.
Mol.Cell67,194–202.e6.
Xu,Y.,Anderson,D.E.,andYe,Y.(2016).TheHECTdomainubiquitinligase
Wright,G.,Terada,K.,Yano,M.,Sergeev,I.,andMori,M.(2001).Oxidative HUWE1targetsunassembledsolubleproteinsfordegradation.CellDiscov.
stressinhibitsthemitochondrialimportofpreproteinsandleadstotheirdegra- 2,16040.
dation.Exp.CellRes.263,107–117.
Yanagitani, K., Juszkiewicz, S., and Hegde, R.S. (2017). UBE2O is a
Wrobel,L.,Topf,U.,Bragoszewski,P.,Wiese,S.,Sztolsztener,M.E.,Oelje- quality control factor for orphans of multiprotein complexes. Science
klaus,S.,Varabyova,A.,Lirski,M.,Chroscicki,P.,Mroczek,S.,etal.(2015). 357, 472–475.
MolecularCell71,August2,2018 457
