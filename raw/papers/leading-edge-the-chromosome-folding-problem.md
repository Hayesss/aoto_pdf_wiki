---
source_path: /mnt/c/Users/Administrator/Zotero/storage/5FVM2KJ5/Dekker和Mirny - 2024 - The chromosome folding problem and how cells solve it.pdf
ingested: 2026-04-23
sha256: 6c621f89acf8ffca
---

ll
OPENACCESS
Leading Edge
Review
The chromosome folding problem
and how cells solve it
JobDekker1,2,*andLeonidA.Mirny3,*
1DepartmentofSystemsBiology,UniversityofMassachusettsChanMedicalSchool,Worcester,MA,USA
2HowardHughesMedicalInstitute,ChevyChase,MD,USA
3InstituteforMedicalEngineeringandScienceandDepartmentofPhysics,MassachusettsInstituteofTechnology,Cambridge,MA,USA
*Correspondence:job.dekker@umassmed.edu(J.D.),leonid@mit.edu(L.A.M.)
https://doi.org/10.1016/j.cell.2024.10.026
SUMMARY
Everycellmustsolvetheproblemofhowtofolditsgenome.Wedescribehowthefoldedstateofchromo-
somesistheresultofthecombinedactivityofmultipleconservedmechanisms.Homotypicaffinity-drivenin-
teractionsleadtospatialpartitioningofactiveandinactiveloci.Molecularmotorsfoldchromosomesthrough
loop extrusion. Topological features such as supercoiling and entanglements contribute to chromosome
foldinganditsdynamics,andtetheringlocitosub-nuclearstructuresaddsadditionalconstraints.Dramati-
callydiversechromosomeconformationsobservedthroughoutthecellcycleandacrossthetreeoflifecan
be explained through differential regulation and implementation of these basic mechanisms. We propose
thatthefirstfunctionsofchromosomefoldingaretomediategenomereplication,compaction,andsegrega-
tionandthatmechanismsoffoldinghavesubsequentlybeenco-optedforotherroles,includinglong-range
generegulation,indifferentconditions,celltypes,andspecies.
In1970,RisandKubaiwrotethefollowing1:‘‘theanalysisofchro- prokaryotic nucleoids,5 and speculations on folding of DNA
mosomestructureseekstodescribethespatialrelationshipsof within the peculiar nuclei of dinoflagellates,6 eukaryotes with
thevariousmolecularcomponentsofchromosomesandtorelate apparent liquid crystalline chromosomes that have become to
changesintheseconfigurationstochromosomefunctionssuch thetopicofrenewedinterestrecently.7,8
asreplication,transcription,andgeneticrecombination.’’Around In the 1960s, it was known that chromosomes were each
thesametimeThomaswroteasfollows2:‘‘wedonotknowhow composedofasinglelongstrandofDNA,andthequestionof
chromosomesareorganized,buttherearesometantalizingclues, howthatDNAwasspatiallyarrangedtofulfillitsroleasgenetic
andwemaybeontheedgeoffindingout.’’ carrierwasonlyjustbeguntobeasked,andfewanswerswere
RisandKubaidescribedthechallengesinthefieldofchromo- available.Atfirstglance,itappearedthattherewerefewcom-
somebiology,whichholdstruetothisday.Thomaswascorrect monalitiesbetweenthestructureofchromosomesfromorgan-
whenhesaidthatweweregoingtofindout,althoughittookde- ismsfromdifferentkingdoms(e.g.,eukaryotesvs.prokaryotes),
cades for the development of new methods, the contributions between chromosomes from different tissues within a species
fromdifferentdisciplinesrangingfrommoleculartocellbiology (e.g., Drosophila polytene chromosomes in salivary glands vs.
to evolutionary biology, and the sequencing of complete ge- moreconventionaleukaryoticchromatininothertissues),orbe-
nomes. Parallel developments in physics continued changing tweenchromosomesobservedatdifferentstagesofthecellcy-
ourviewofthenatureofchromosomes,furtherpushingtheen- cle for any one cell type (the classical X-shaped compacted
velopeofPolymerPhysics.Today,weknowatleastaboutsome mitoticchromosomesreadilyvisibleinthelightmicroscopevs.
ofthestructures,molecules,andmechanismsdrivingchromo- interphase chromosomes that essentially disappeared from
somefolding.Yethowtheseprocessesandresultingchromo- view).Chromosomescouldbelinear,circular,regularlypacked
some structures relate to chromosome function continues to inproteinaceouscapsidsinphages,lightlypackedinnucleoids
beatopicofintensestudyanddebate.Still,thereisthesame inbacteria,wrappedaroundnucleosomesin(most)eukaryotes,
sense of optimism that we may be on the edge of finding out supercoiledornot,andsometimesarrangedinloops.
theconnectionsbetweenfoldingandtheworkingofthegenome. As for many other fields, the study of chromosome folding
awaitedthedevelopmentofnewtechnologiesandassaysthat
THEVIEWOFCHROMOSOMES50YEARSAGO would ultimately allow the visualization of entire genomes at
nearbase-pairedresolutionin3Dwithinsinglecells.Thesede-
Among the first articles in Cell covering chromatin structure, velopmentswerecomplementedbythejoiningtogetherofsci-
chromosomefolding,andnuclearorganizationwerestudieson entistsfromarangeofdisciplines,includingcellbiology,molec-
fine-scale organization of eukaryotic chromatin fibers as ular biology, and structural biology, on the one hand, and
‘‘beads-on-a-string,’’3 formation of histone tetramers,4 folded physics,computationalbiology,andbioinformaticsontheother.
6424 Cell187,November14,2024ª2024TheAuthor(s).PublishedbyElsevierInc.
ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).
ll
Review OPENACCESS
Thisinterdisciplinaryefforthasoverthelastfewdecadesstarted of histone modifications that define different chromatin states
toidentifycommonprinciplesofchromosomefoldingacrossthe including euchromatin and heterochromatin. Like the protein
treeoflife. folding problem, defined as the question of how the primary
amino acid sequence of a protein dictates its 3D folding, the
THENEEDTOFOLDCHROMOSOMES chromosome folding problem can be defined as the question
ofhowthelinearepigenomeisrelatedtothespatialarrangement
In all organisms, the lengths of their genomes are large andfoldingofchromosomesinthecell.
comparedwiththedimensionsofthecellornucleus.Stretched However,andthisisdifferentfromproteinfolding(seeMirny14
out,thegenomeofE.coliis(cid:1)1.7mmlong,comparedwithacell forreview), chromosome folding isnotonlydrivenbyaffinities
diameterof2mm.Thelengthofthehumangenomeinallchromo- andinteractionsbetweengenomicelements,italsoinvolvesbio-
somesis(cid:1)2m,andthecellnucleusisonly(cid:1)5–10mmindiam- logicalactivitiesthatdirectlyfoldandrefoldchromosomes,and
eter.However,giventhatDNAfibersaresothin(2nmofDNA these molecular processes can in some cases fold chromo-
or11nmofthechromatinfiber),thevolumeofthegenomefits somesinwayslargely unrelated tothelinear epigenome, e.g.,
very comfortably in the cell or nucleus. So, is there really a inmitosis.15–20Chromosomeconformationisalsohighlyvariable
needforcellstoactivelyorganizeandfoldchromosomes? betweenindividualcells,aresultoftheverylargelengthofchro-
Therearestrongargumentsforwhycellsneedtoactivelyfold mosomes,combinedwiththeirstochasticdynamicsofself-as-
theirchromosomes.First,assumingthatchromatinbehavesas sembly,21–23andtheactionofhighlydynamicfoldingprocesses
an ‘‘unconstrained’’ polymer (i.e., an ideal chain, resembling a such as loop extrusion, which rearrange chromosomes at the
randomwalk)andthatithasapersistencelengthofa(cid:1)70nm scale of hundreds of kilobases over tens of minutes. Further-
containing(cid:1)3–5kb,9,10thediameterofanunconstrainedchro- more,chromosomescanrapidly,inmereminutes,changetheir
mosomeofthelengthofjust1copyofhumanchromosome1 foldingstate,e.g.,duringentryandexitofmitosis.16,24–27
would be about 16 mm (Rg = sqrt(250,000/3) 3 70/sqrt(6) = Weproposeamoreexpansivedefinitionofthechromosome
8 mm; diameter of the coils is twice that: 16 mm), exceeding folding problem: the question of how biophysical forces and
that of the whole nucleus. Clearly, extensive compaction is molecular mechanisms, through the action of specific folding
requiredtofitinall46chromosomes. machineries, act on the linear epigenome to dynamically fold
Second,wepreviously11outlinedthatthepolymerstateofchro- and refold chromosomes at different lengths and timescales,
mosomeshasimportantimplicationsforwhichlocicanphysically e.g., during the cell cycle, development, and other biological
interact(e.g.,genesandtheirregulatoryelements),thekineticsby transitions.
which such interactions can form, and in what fraction of cells Chromosome folding appears todiffer indramatic waysbe-
such interactions can occur. In the absence of any constraints tweenspeciesfromdifferentkingdoms(e.g.,prokaryotesvs.eu-
or active processes folding chromatin, short-range interactions karyotes) and as cells progress through the cell cycle. Such
betweengenomicloci,e.g.,separatedbyuptotensofkilobases, observationssuggestthatmanydifferentsolutionstothechro-
will be frequent enough to occur in most cells in a reasonable mosomefoldingproblemmayexistandthatspecies-andcondi-
amount of time (e.g., the duration of the cell cycle). However, tion-specificfoldingmechanismsmusthaveevolved.
longer-range interactions will be rare ((cid:1)6% of the time for Oneofthemostexcitingdiscoveriesofthelasttwodecades
0.5-Mbseparation12)andwillnotbeformedinmostcells,even hasbeenthatonlyasmallnumberofuniversalbiophysicaland
at very large timescales. Finally, in the absence of active and molecular processes drive chromosome folding. These major
controlledfoldingprocesses,itishardtoimaginehowspecificity folding mechanisms are deeply conserved across the tree of
ininteractionscanbeobtained(below). lifebutaredirected,regulated,anddeployedindifferentways
Third,intheabsenceofactivemanagementofchromosome to produce different folded statesof chromosomes to accom-
organization, any genomic process would be compromised. modatethemanydifferentfunctionsofgenomes.
For instance, replicating long DNA molecules leads to pairs of
sisterDNAsthataretopologicallyintertwined,creatingasignifi- BREAKTHROUGHSINDETERMININGCHROMOSOME
cantchallengetothecell,aswasrealizedbyDelbruckalreadyin FOLDING
1956.13Tosegregatethesesistermoleculestodaughtercells,
cellsneedtocompacteachsothattheyareshortandrigidto Chromosomeswerefirstdescribedusingmicroscopicmethods.
facilitate segregation, while simultaneously also topologically Giventhatinitiallyonlylargemitoticandmeioticchromosomesin
unlinkingthem.Thisprocessisfundamentaltolifeandisintui- plantsandamphibianscouldbeindividuallyobservedbymicro-
tively the most obvious case for the need for processes to scopic means, initial studies focused on these chromosomes.
activelyfoldchromosomes. Firstconceptsofchromosomefoldinginmitosisdevelopedthe
notion of the ‘‘folded fiber,’’ ranging from irregular fibers28 to
THECHROMOSOMEFOLDINGPROBLEM radial loop structures29,30 to hierarchical models.19,31–34 Initial
physical models of interphase chromosomes started to arise
The(cell-type-dependent)foldingofchromosomesisrelatedto when fluorescence in situ hybridization (FISH) imaging estab-
the (cell-type-dependent) linear epigenome patterning along lishedhowthespatialdistancebetweenlociincreaseswiththe
thegenome:thepresence,location,andactivityofcis-regulatory genomic separation between theprobes. The first quantitative
elementssuchasenhancers,insulatorsandpromoters,and(in models considered an interphase chromosome as a random-
eukaryotes) the presence of regions of specific combinations walkpolymer35oraconfinedortetheredpolymer.36Alternative
Cell187,November14,2024 6425
ll
OPENACCESS Review
Figure1. Evolvingphysicalmodelsoverthelastdecades
Overthelast50years,PolymerPhysicshasputforthincreasinglyrefinedmodelsofchromosomeconformation.
Seetextfordetails.
models were proposed where chromosomes were folded into tureofentirechromosomes,orevengenomes,canbetracedin
megabase-size loops along otherwise random-walk poly- single cells. These include large-scale locus tracing72,73;
mers37,38(Figure1). OligoStormandOligoDNAPaint,74,75andORCA.76Thosepar-
Overthelasttwodecades,fourimportantdevelopmentshave alleled developments of live-cell ‘‘tracking’’ of chromosomal
greatlyenhancedandtransformedthestudyofchromatin,chro- dynamicsthatshedslightonunderlyingfoldingprocesses.12,77
mosomes,andentiregenomes. Thefourthaspectincludesdevelopmentsintheunderstand-
Thefirstofwhichwastheabilitytodeterminethesequenceof ingofchromosomefoldingfromthepolymerphysicspointof
complete genomes for many species. While initial genome view: from the random-walk35 andworm-like chain models in
sequencing efforts in the 1990s focused on smaller genomes theearly1990s36toearlymodelsofchainswithloops,37,38to
of bacteria and some model organisms (e.g., budding yeast appreciationoftopologicaleffects,78–80tomorerecentstudies
S. cerevisiae,39 the nematode C. elegans,40 and the fruit fly ofactivepolymers81orpolymerdrivenbymotors(loopextru-
D. melanogaster41) and large-scale international efforts were sion)82,83 and folded onto loops,84 and to models of polymer
required to sequence the mouse and human genomes,42–44 dynamics and response to external forces.85,86
furtherincreasesinthroughputandlowercostsnowenablethe Thedevelopmentandapplicationofgenomicandimaging-
sequencing of any number of species and individuals. Now based methods to determine the structure of chromosomes
(near)full-lengthgenomesequencesareavailableforthousands have been extensively reviewed elsewhere,87–91 and we
of species, ranging from bacteria, to protozoa, archaea, fungi, refer the reader to those reviews and the primary literature
plants, birds, mammals, etc. (e.g., Christmas et al.,45 Stiller cited therein. Here, we focus on current views of what the
et al.,46and Wangetal.47).Notably, Hi-C can alsobeused to chromosome structure is, under different conditions and in
assemblethelineargenome(firstshownbyKaplanandDekker48 different species; the mechanisms by which this structure is
andBurtonandco-workers49in2013)andisnowroutinelyused formed; and how chromosome structure and function are
toassemblegenomesofnewspecies(e.g.,Dudchenkoetal.50 related.
andHoencampetal.,51andseeObinuetal.52foranevaluation
oftheseapproaches). FOURMECHANISMSFORFOLDINGCHROMOSOMES
Second, the development of genomic methods to probe the
folding of chromosomes now allows for mapping chromosome Studiesinmanyspecieshaveshownthattheysharekeymech-
structuredirectlytogenomesequence.Someofthesemethods anisms by which they fold chromosomes. Here, we describe
are based on chromosome conformation capture (3C,53 4C,54 thesemechanisms.
5C,55 Hi-C,56 Micro-C,57 DNAse-Hi-C,58 Chia-PET,59 HiChIP,60
Plac-seq,61etc.),whileothermethodsrelyonmappingDNAse- Compartmentalization
quences near sub-nuclear structures such as DamID,62 TSA- Oneofthefirstfeaturesdescribedforthespatialorganizationof
seq,63ortheidentificationoflocico-locatedinclustersorspecific chromatin inside eukaryotic interphase nuclei is the spatial
sectionsofthenucleus(GAM64;SPRITE,65etc.).Inrecentyears, segregation of inactive heterochromatic chromatin from active
theresolutionofthesemethodshasincreasedsothat3Dmaps euchromatin(Figure2),asfirstdescribedbyEmilHeitz.92Classic
ofgenomescanbeacquiredatsub-kilobaseresolution,aswell microscopystudiesshoweddense,compactedchromatinclus-
asinsinglecells(e.g.,Naganoetal.,66Naganoetal.,67Ramani tered near the nuclear periphery, while decondensed, open
etal.,68Lietal.,69Kindetal.,70andTanetal.71). chromatin was located more centrally. Later studies showed
Third,thedevelopmentofimagingmethodsthatcananalyze that more gene-dense chromosomes tend to locate centrally,
thespatiallocationsofthousandsofloci,sothatthe3Dstruc- while gene-poor chromosomes are more peripheral in the
6426 Cell187,November14,2024
ll
Review OPENACCESS
Figure2. Twoprocessesfornuclearorgani-
zation: Compartmentalization through ho-
motypic affinities and tethering to the nu-
clearperiphery
(A) Eukaryotic chromosomes are composed of
alternatingAandBcompartments.Inconventional
nuclearorganization,strongB-Baffinitiesleadto
spatialseparationofAandBcompartments.A-A
affinities are much weaker and contribute to a
lesserextent.Inaddition,someBcompartments
aretetheredtothenuclearperiphery,resultingin
enrichmentofheterochromatinatthenuclearpe-
riphery,leavingeuchromatinlocatedcentrally.
(B)IntheabsenceoftetheringofBcompartment
domainstothenuclearperiphery,A/Bcompart-
mentalizationoccursnormally,butthestrongB-B
affinities result in clustering of all B compart-
mentsinthecenterofthenucleus,withAcom-
partmentslocatedat theperiphery(invertednu-
cleus).
(C)Amorecomplexpicturewhenmorethantwo
compartment types are present. A and B com-
partmentscanbesplitindifferentsub-compart-
mentsthatcanalsodisplaysignificantpreferential
homotypic affinities, leading to their spatial
segregation.
interactwithoneanother.Thisphenome-
non is referred to as compartmentali-
zation.
Initial lower-resolution Hi-C studies
(megabase scale) showed the presence
ofjusttwotypesofchromatinsthatself-
interact, and these two types (A and B
compartments) had all the hallmarks
of euchromatin and heterochromatin,
respectively.56 Subsequent higher-reso-
lution Hi-C maps showed that each of
these two major types of compartments
can be split in so-called sub-compart-
mentsthatdifferintheirprecisechromatin
composition, e.g., histone modification
patterns,andcanbeassmallasseveral
kilobases.99Eachofthesesub-compart-
mentsdisplayscharacteristicpatternsof
long-range interactions with other loci,
butmostdisplayapreferencetointeract
withotherlociofthesamesub-compart-
ment type (Figure 2A). A major recent
nucleus.93–95 Studies on the timing of DNA replication also insightisthatthenumberoftypesofsub-compartmentsislarger
showed spatial segregation of early and late replicating chro- than previously anticipated (Figure 2C) and that these are not
matin,correlatingwitheuchromatinandheterochromatin.96 necessarily universally present, i.e., in a given cell type not all
GenomicassayssuchasDamIDdirectlymappedsequences sub-compartmenttypesmaybeobserved.100,101
nearthenuclearlamina,againidentifyingregionspooringenes Compartmentalizationisthoughttobedrivenbyhomotypicaf-
and mostly transcriptionally silent.97,98 The very first 4C and finitiesbetweenloci102–106(Figure2).Themolecularnatureofthe
Hi-C datasets showed spatially segregated euchromatic and factorsthatmediatetheseaffinitiesarenotknownindetail.Itis
heterochromatic domains at genome-wide scale.54,56 In Hi-C, intriguing that compartmentalization has mostly been detected
enrichedinteractionsarereadilydetectedbetweenlociofsimilar in eukaryotes that have nucleosomes and not in eukaryotes
chromatinandactivitystate:activeandopenchromatininteracts without nucleosomal DNA, e.g., dinoflagellates7,8 and in some
with other active and open loci, along the same chromosome archaea.107 Although other explanations can be proposed, it
(cis) and between chromosomes (trans). Similarly, inactive loci may indicate a key role for histones in this process.
Cell187,November14,2024 6427
ll
OPENACCESS Review
Compartmentalizationiscorrelatedwiththepresenceofhistone acting chromatin segments dissociate within tens of minutes.
modifications:eachsub-compartmenthasacharacteristiccom- Importantly,thekineticsofdissociationwererelatedtothechro-
bination of histone modifications.100,101,108 In vitro, short chro- matinstate,withheterochromaticlocidissociatingslowerthan
matin fibers carrying histone H3 lysine 9 trimethylation euchromatic loci, pointing to higher affinities between hetero-
(H3K9me3) can form condensates, indicating that the modified chromatic loci. Together with observations obtained with very
histonesthemselvescan playa roleinthe clusteringofhetero- deeplysequencedHi-Cdatasets,99thesedatashowthatsub-
chromatin.109Furthermore,factorsthatrecognizepatternsofhis- compartmentscanbeassmallasseveralkilobases.Heterochro-
tone modification can act as bridging factors and, in that way, maticinteractionsbetweenH3K9me3-markedlociwerefoundto
connectdistallocitostabilizecompartmentalization.Forinstance, bemorestable andthuscontribute moststronglytocompart-
HP1proteinscanbindH3K9me3andcanbindmultiplehistone mentalization,aspredictedbymodeling.104
tailssimultaneously.Suchbridgingfactorscanalsophasesepa- A mechanism of compartmentalization driven by largely rela-
ratethemselves,leadingtoaggregationofsuchproteinstogether tivelystableinteractionsbetweenH3K9me3-markedheterochro-
with multiple loci.110–114 While HP1 proteins can contribute to maticlocidoesnotruleoutaffinitiesbetweenotherregions,e.g.,
compartmentalizationinthatmanner,lossofHP1hassurprisingly euchromaticloci(thatamongotherfactorscanbedirectormedi-
little effect on compartment formation,115 pointing to roles for atedbynuclearspeckles)(Figure2C).Infact,enrichmentofcon-
otheryettobeidentifiedfactors.Otherexamplesarepolycomb tactsbetweenhistoneH3lysine27acetylation(H3K27ac)regions
complexesthatmediatedepositionofhistoneH3lysine27trime- isevidentfromMicro-C125,126byaveragingoverthousandsofre-
thylation(H3K27me3)modificationsandthenassociatewithchro- gionsinHi-C,127butitismostdistinctlyobservedwithregion-cap-
matincarryingthismark,stabilizinglong-rangeinteractionsincis tureMicro-C.128,129Whileindicatingthateuchromatinregionsalso
andintransbetweenlocisilencedbythesefactors(forreviewsof have some homotypic affinities, the need for averaging or for
theextensiveliteratureonthistopic,seeAkillietal.116andSchuet- exceedingly deep sequencing suggest that such contacts are
tengruber117). While many polycomb-bound loci reside in the rare, consistent with microscopy.127 Although they can help to
larger A compartment and can be located in nuclei centers,118 stabilizeotherwisetransientinteractionsbetweenregulatoryele-
they tend to engage in prominent long range with other poly- ments and promoters at sub-megabase separations, the rarity
comb-boundsites,e.g.,inDrosophila119andvertebrates,espe- ofsuchcontactsatlargergenomicdistancessuggestsfewfunc-
ciallyinembryonicstemcells.120,121 tionalrolesthattheycanplay.Interactionsbetweenactivelocican
Compartmentalization constitutes a phenomenon of micro- alsobedrivenbybridgingfactors.Forinstance,Brd2/3/4proteins
phaseseparation,i.e.,aphenomenonwhereapolymer(chromo- can drive clustering of chromatin marked with H3K27ac both
some) made of blocks of A and B monomers (or more types) invivoandinvitro.109Aparticularlyinterestingcaseisanonco-
formsspatiallyseparateddomainswhosesizesdependonthe genic BRD4-NUT protein fusion that can lead to the spreading
sizes of the blocks in the sequence. Such a process can be ofH3K27acthroughlargeregions,whichinturnresultsinspatial
drivenbyattractionsbetweenhomotypicelements(A-Aand/or clusteringofsuchhyperacetylated‘‘megadomains.’’130Thismay
B-B).Phaseseparationhasalsobeenseenininvitrochromatin berelevantfornormalcells aswell, whereevenrelativelysmall
reconstructionexperiments.109Initialstudiesdemonstratedthat H3K27ac-enriched loci such as enhancers and promoters can
the characteristic pattern of A/B compartmentalization seen in formsmallmicrocompartmentdomains.128,131,132
Hi-Cdatacanbereproducedbymodelswithhomotypicaffin- An important aspect of compartmentalization as an affinity-
ities,106,122yettherelativecontributionsoftheseaffinitiesforA driven process is that such clustering and spatial segregation
and B compartments remained unknown. A solution came willoccurbothincisandintrans.Thismakesthisprocessfunda-
from a rare biological system of the ‘‘inverted’’ nucleus in the mentallydifferentfromothermechanismsofchromosomefolding
rodphotoreceptors.123Naturallossofattachmentofheterochro- suchasloopextrusionthatactsstrictlyincis(seebelow).Further-
matin to the nuclear periphery in such nuclei resulted in the more,compartmentalizationisdrivenbylocalinteractionsleading
repositioning of the heterochromatin to the center with the tostochasticassembliesatthescaleofwholechromosomesor
euchromatin takingperipheral locations. Bothmicroscopy and genomes. In other words, in each cell, a different configuration
Hi-C104 confirmed that despite their inversion such nuclei are isobtained,butineachcell,activelocipreferentiallyclusterwith
perfectlycompartmentalized,demonstratingthatcompartmen- otheractiveloci,butwhichspecificsetsoflociclustertogether
talization is driven by interactions within chromatin rather than can differ. The process results in stochastic co-localization of
anchoringofheterochromaticlocitothelamina.Polymermodels lociofsimilarchromatinstatebuthasotherwiselimitedspecificity
furtherdemonstratedthathomotypicaffinitiesofheterochromat- intermsofwhichspecificDNAsequencesinteractinanygiven
ic regions drive compartmentalization, with affinities between cell. This aspect is important for understanding potential func-
euchromaticregionsbeingmuchweaker(Figure2B). tionalrolesforcompartmentalization.
These predictions from models were confirmed with direct Althoughcompartmentalizationismostlyobservedineukary-
observation of dissociation kinetics of chromatin interactions otes,the biophysical process thatunderlies thisphenomenon,
byliquidchromatinHi-C.124InliquidchromatinHi-C,chromatin affinity-driven clustering loci, likely also occurs in prokary-
isfragmentedinsitu,leadingtoprogressivedissociationofchro- otes(below).
matininteractionsovertime,whichcanbemeasuredusingHi-C.
Itwasfoundthatchromosomesremaincompartmentalizedeven Loops,extrusion,andtheircontrol
whenchromatinisfragmentedtoanaveragesizeof10–20kb. Afirstdescriptionofchromosomeloopsinmitoticchromosomes
Whenchromatinisfragmentedtoasizeoflessthan6kb,inter- appeared in this journal in 1977,133 leading to the radial loop
6428 Cell187,November14,2024
ll
Review OPENACCESS
Figure 3. Two regimes of loop extrusion
produce different conformations, consis-
tentwithinterphaseandmitosis
(A)Activityofaloopextruder:thecomplexloads
andextrudessomeamountoftimeafterwhichit
maydissociateorisactivelyunloaded.
(B) Left: During interphase (in vertebrates), co-
hesinisthemainloopextrusioncomplex.Ithasa
shortresidencetime,generatingalowdensityof
transient loops, and the chromosomes appear
diffuse in shape. Cohesin can be blocked by
CTCF-bound sites, generating enrichment of
positionedloopsattheseelements.Right:During
mitosis,condensinsarethemainloopextrusion
complexes. Condensin II has a long residence
time, generating stable arrays of consecutive
loops that lead to compaction into the rod-
shapedmitoticchromosomes.Condensinisnot
blocked by CTCF, and the loop array is not
positionedatreproduciblelociinthecellpopu-
lation.
(C) In bacteria, repeated loading of loop-
extrudingcomplexesatdefinedloadingsitescan
lead to juxtaposition of the chromosome arms,
sequencesoneithersideoftheloadingsite.
ofchromatidsleadingtomorphologiesof
simulatedchromosomesresemblingthose
ofearlyprophasechromosomes.148Loop
extrusion during interphase149,150 was
suggested as a mechanism underlying
thethenrecentlydiscoveredtopologically
modelofmitoticchromosomes.30,134Proposalsaboutthepres- associatingdomains(TADs151,152)andassociatedfeaturessuch
ence of loops in interphase chromosomes have started to asstripesanddotsobservedinHi-Cinteractionmaps.100These
appear at about the same time, based on sedimentation features emerge naturally in polymer models of loop extrusion
data,135,136 and later as physical models fit to microscopy when extrusion is occluded by boundaries. Modeling studies
data.37,38,137 alsosuggestedthatloop-extrudingmotorsareSMCcomplexes:
Whatisnowknownastheprocessofloopextrusion(Figure3) cohesins in interphase and condensins during mitosis, while
hasarichhistory.Theideasof enzyme-mediated loopgrowth extrusionbarriersareDNA-boundCCCTC-bindingfactor(CTCF)
startedtoemergeintheliteratureasmanyunrelatedhypotheti- proteins. The loop extrusion hypothesis gained broad support
calmechanismsunderlyingVDJrecombination,138compaction by CTCF and cohesin depletion153,154 and modulation experi-
of interphase chromosomes,139 enhancer-promoter interac- ments,allgeneratingmodel-predictedoutcomes.155Directvisual-
tions,139,140supercoiling,141andmitoticcompactionandsegre- izationandcharacterizationofloopextrusionbySMCsinsingle-
gation.142Manyworksattributedtheseprocessestostructural molecule experiments (see Davidson and Peters156 and
maintenance of chromosomes (SMCs) complexes,143–145 with HoencampandRowland157forreviews)demonstratedthatthese
indications that SMCs can function as chromatin compacting complexes are indeed loop extrusion motors, as antici-
motors.146Inthecontextofmitoticcompaction,loopextrusion pated.142,147,149Thedemonstrationthatthesamemechanismin
wasfirstmathematicallymodeled.147However,becauseofthe differentregimes158canleadtoeitherinterphaseorganizationor
lackofpolymermodelstomakeconcretepredictionsfollowing to mitotic compaction (Figure 3B) suggests that loop extrusion
from the activity of these mechanisms, and experimental data by SMCs can be a universal mechanism organizing chro-
to test and validate the models, these proposals remained mosomes.
largelyhypothetical. SMCs are ring-shaped and flexible protein complexes and
Emergence of chromosome conformation capture data pro- include cohesin, condensin, SMC5/6, their bacterial counter-
vided rich grounds for developing and testing mechanisms of parts,andpossiblyothercomplexesinvolvedinDNArepair.157
chromosomefoldingbyloopextrusion.Onepredictionofthethe- Whilecondensinswereknowntobeessentialformitoticchro-
ory147wasthatachievingmitoticcompactionwouldleadtothe mosomecompaction,159–161theirmodeofactionwaslongun-
formation of a loop array where non-overlapping loops follow known. Cohesin has been characterized as a complex that
eachother (if extruders cannotbypasseachother). Indeed, 5C keepstwosisterchromatidstogether.142Predictedloopextru-
andHi-Cdataformitoticcellswerefoundtobeconsistentwith sion activity of SMCs147,149 was initially a surprise, but single-
such organization of loops.15 Polymer simulations further indi- molecule experiments have definitively demonstrated that
catedthatloopextrusioncancompactandsegregatepolymers SMC complexes can extrude loops in an ATP-dependent
Cell187,November14,2024 6429
ll
OPENACCESS Review
manner.162–166InsuchinvitroexperimentswithnakedDNAas (at ParS sites in bacteria,187 and likely loading at active en-
template,aswellasinlivecellsonendogenouschromatin,12,24 hancers183,186,188butnotatpromotersinanimals),domainsof
loop extrusion is fast: (cid:1)1–3 kb/s. Different SMCs were found localized extrusion activity (suggested in the silkworm189), and
tobeeitherone-sidedortwo-sidedloopextruders,162–165with sitesofSMCunloading(e.g.,30endsofactivegenesinhuman183
two-sided extrusion possibly resulting from rapid switching of andmouse190).Theroleofepigeneticcontextinregulatingloop
one-sidedextrusionactivity.167Thesecomplexeshaverelatively extrusion is less well understood. While extrusion is active in
low stall forces162,164 (i.e., forces of 0.1–1 pN suffice to stop both euchromatin and heterochromatin compartments,101het-
extrusion), and some complexes such as cohesin are blocked erochromatin is refractory to CTCF binding and hence devoid
byobstaclessuchasRNApolymerases,168CTCF,andminichro- ofboundaries.
mosomemaintenance(MCM)proteins(thelattertwothrougha Learning rules in one organism and extrapolating these to
specific protein-protein interaction169,170). On the other hand, others, we anticipate that (1) the speed of extrusion, loading,
condensinsdisplaythesurprisingabilitytobypasseachother171 and unloading can be controlled epigenetically in animals; (2)
or obstacles much bigger than their size.172Yet the molecular replication forks and likely other genomic processes can halt/
mechanismofloopextrusionandforcegenerationremainsenig- pause extrusion, thus breaking or establishing extrusion-medi-
maticandanareaofactiveresearch.173,174 ated interactions; and (3) extrusion activity can be non-uniform
ThesedevelopmentsparalleledstudiesofSMCsandtheiractiv- alongthegenome.Broadly,changesinextrusion-mediatedpat-
ityinbacteria.5CandHi-CinB.subtilis175andC.crescentus176,177 ternsthroughdifferentiationanddevelopmentsuggestthatepige-
revealedfoldingofthechromosomes‘‘inhalf’’withtwojuxtaposed neticmarkscancontrolextrusionandbarriers.Extrusionmayin
arms, in an SMC-dependent manner. Further studies not turn play a role in the localization and spreading of epigenetic
onlyindicatedloadingofsomeSMCsatspecificsites(origin-prox- marks,assuggestedbyCTCF-demarcateddomainsofgamma-
imal in many species, e.g., at ParS sites near the origin in H2AXspreadingupondouble-strandedbreak(DSB)repair.191,192
B.subtilis178)butalsodirectlyvisualizedhowsuchloadingresulted
inaprogressivejuxtapositionofthearms(Figure3C).Strikingly, Associationswithlandmarksofthenucleus
aheadofstudiesineukaryotes,time-resolvedHi-Cinbacteriaal- Ineukaryotes,locicanbecometetheredtothenuclearperiphery
lowedformeasuringthespeedofloopextrusioninlivingcellsat and the nucleolus as well as other structures such as nuclear
(cid:1)1kb/s.179 specklesthatareenrichedinRNAprocessingandsplicingfac-
Our understanding of the loop extrusion mechanism has tors. In prokaryotes specific loci can be found tethered to the
significantly progressed in recent years. Practically every cell wall, e.g., the ParS sites in C. crescentus are tethered to
assumptionandpredictionoftheoriginalloopextrusionmodel thewallatonepoleoftheelongatedcell.
hasbeenchallengedandmostlyconfirmed.Asanticipated,co- Themolecularmechanismsoftetheringarebecomingclearer
hesindepletionleadstoanincreaseindistancesbetweenallloci onlyforafewofsuchassociations.Invertebrates,tetheringof
as seen by chromatin tracing,73 and (cid:1)50% of chromatin is heterochromatic domains to the nuclear periphery has been
located in extruded loops at any moment.12 Many processes studiedextensively.Largedomains,referredtoaslamin-associ-
and complexes on crowded DNA function as barriers to loop ateddomainsorLADs,arefoundassociatedwiththenuclearpe-
extrusion, including the process of transcription,168 elements riphery.97,98 These domains are enriched in particular histone
of the replicative machinery,180 even in G1. CTCF remains the modificationssuchasH3K9me3andH3K9me2andaretypically
strongest known barrier that relies on a specific peptide that transcriptionally silent and compacted. Lamins may not be
can halt extrusion.100,153,169 Single CTCF sites, however, are exclusivelyinvolved,193,194andotherfactorssuchasthelamin
permeable181 and loops that bridge two CTCF sites are rare B receptor have been found to play roles.195 However much
andtransient.77,12Broadly,thesefindingsindicatethatpatterns less is known about the factors that determine clustering of
ofcontactsformedbyloopextrusionaretransient,suggesting lociaroundnucleoliorspeckles,butaroleforCTCFhasbeen
that it is the process of extrusion rather than specific patterns proposed.196
thatcanplayfunctionalroles.182,183 Thefunctionalrelevanceoftetheringlociatsub-nuclearstruc-
Several ‘‘rules of engagement’’ for SMCs, which determine turesislargelyunknown.Whilemostcellshaveheterochromatic
howencountersbetweendifferentcomplexesalongthechromo- domains localized at the nuclear periphery, in specialized cell
some are resolved, are being discovered24,184 (Figure 4): they types such as rod cells, heterochromatin is not tethered and
canblockeachother(likelycohesins184),onetriggeringunload- now is instead localized in the center of the nucleus.123 This
ing of the other (e.g., condensins triggering unloading of does not affect compartmentalization and does not appear to
extrudingcohesins24),ortheycanbypasseachotherandthus have dramatic effects on gene expression. It should also be
formmorecomplexoverlappingloops(asseeninsingle-mole- notedthatsomeactivechromatincanbefoundlocalizedatthe
cule experiments171,172 and in bacteria185). Interactions of nuclearperipheryaswell,especiallyaroundnuclearpores.The
loop-extruding SMCs with SMCs holding sisters chromatids functional relevance of these associations is not established,
(‘‘cohesive cohesins’’) can vary as well, with yeast cohesins but one possible role could be that this would facilitate rapid
stoppingatsitesofsistercohesion,184whileanimalcondensins mRNAexport(‘‘genegating’’).197
bypasssuchsitesinmitosis.24 Inotherorganismsorconditions,tetheringoflocitothecellwall
Manyofthesemechanismscanbecontrolledbygenomicel- (bacteria198) orthe nuclear envelope is critical for chromosome
ements and epigenetic context.183,186 Examples known so far segregationorchromosomepairing(e.g.,meiosisI199).Although
includemethylation-dependentCTCFbinding,targetedloading tetheringisastraightforwardwaytofacilitatespatialpositioning
6430 Cell187,November14,2024
ll
Review OPENACCESS
Figure4. Rulesofengagementfordifferent
SMCs result in different loop organization
andstructuresofcompactedchromosomes
(A)Threepossibleoutcomesofanencounterbe-
tween loop-extruding SMCs (green and yellow):
theycanblockeachother,leadingtoformationof
consecutiveloops;bypasseachotherformingso-
calledZ-loop171;oronecanfacilitatedissociation
ofanother(otheroutcomesarealsopossible,e.g.,
onepushingtheotherback,etc.).
(B) Two possible outcomes of interactions be-
tween cohesive cohesins (blue rings) and loop-
extrudingSMCs(yellow).Top:whenextrudersare
blockedbycohesivecomplexes,sisterchromatids
arepredictedtobeconnectedatthebasesofthe
loops,formingasingleaxis(asinmeioticprophase
Iandearlymitoticprophase).Whenextruderscan
bypasscohesivecomplexes,sisterchromatidsare
predictedtobeconnectedthroughthetipsoftheir
loops(asinmitoticprometaphase).
can leadto two phenomena: (1) exceed-
inglyslowmixingbetweenchromosomes
afterexitfrommitosis,leadingtotheforma-
tion of chromosomal territories; and (2)
slow equilibration within each chromo-
some, leading to the folding of the chain
into a non-equilibrium and long-lived
hierarchically organized and unknotted
stateknownasthefractal(or‘‘crumpled’’)
globule.79
Polymersimulationsandanalysisofmi-
croscopy data for Drosophila suggested
that polymers within each chromosome
arefoldedintosuchacrumpledstate,204
and they likely equilibrate exceedingly
slowly. The first Hi-C data and polymer
simulations provided compelling evi-
dence that human interphase chromo-
somesarefoldedintothefractalglobule
state at the scale below (cid:1)10 Mb.56 In
this state, a chromosome resembles a
‘‘space-filling’’curve,i.e.,continuousre-
gionsofthechromosomeformcompact
ofloci,muchworkisneededtoexplorethemolecularplayers,194 spatialblobs,asobservedbymicroscopy.205Thecontactprob-
as well as roles of any cis-elements that participate in these abilityPbetweengenomiclocidecayswithgenomicdistance(s)
events,andtoexplorethefunctionalrelevance. asP(s)(cid:1)s(cid:3)ɑwithɑz1–1.1.206Thiscontrastsapolymerwithout
topological constraints, i.e., strand passage can freely occur,
Topologicalconstraints whichwhencompacted, resemblesa random-walk configura-
The role of topological effects in the way cells manage their tion in a confinement, where short continuous regions are
exceedingly long chromosomes, disentangling strands, and expandedratherthan compacted, leading to a rapid decay of
compactinglongchainshaveconcernedbiologists200andphys- thecontactprobabilitywithgenomicdistance(ɑz1.5)followed
icists13,78alike.TopoisomeraseIIwasfoundtobeessentialfor by a plateau. Interestingly, chromosomal arms of yeast
chromosomeindividualization201andwasarguedtobeessential S. cerevisiae, which are relatively short (up to 0.8 Mb) and do
forfastmitoticcompaction.78Effectsoftopologicalconstraints nothaveacompactmitoticstate,showarandom-walkfolding
andentanglementsonpolymerdynamicshavebeenwellknown (ɑz1.5).9 Multi-contact 3C data and polymer simulation for
inphysics202andhypothesizedtoimpactthewaythegenomeis mammalian cells also demonstrate that each chromosome is
folded.79,203 largelyunknotted.207Itremainstobeseenwhethersuchunknot-
Polymertheorysuggestedthatthepresenceoftopologicalcon- ted and locally compact fractal globule folding and chromo-
straints,i.e.,whentopoisomeraseIIactivityisabsentorverylow, somal territories have any specific functional roles or simply
Cell187,November14,2024 6431
ll
OPENACCESS Review
representamemoryoftheunentangledtelophasestate208pre- thatyeastchromosomalarms—awayfromclusteredcentromeres
servedbytopologicalconstraints. andanchoredtelomeres—arelargelyunconstrainedpolymers.215
Recently,amorecomplexpictureofhowcellsmanagetopo- Invertebrates,thefractalglobulenatureoffoldingisfullyconsis-
logical states of chromosomes started to emerge. Activity of tentwithcompartmentalizationandloopextrusion.84,208Yetthe
topoisomerase II allows strand passage, turning the chain physical nature of this crumpled state, and thus the interphase
intoatopologicallyunconstrainedone,whichcanresultinan vertebrate chromosomes, remains enigmatic due to difficulties
increasedoradecreasedlevelofentanglement.Interestingly, in reconciling the fractal globule state with dynamics and force
loop extrusion can bias topoisomerase II activity toward un- response.86
knottinganinitiallyknottedchain.209Extrudedloopscanalso Studies of chromosome dynamics provide a view comple-
buffertopologicalinteractions,makingthechainlesssensitive mentary to thatlearned from Hi-Cand microscopy. Moreover,
totopologicalconstraints,84e.g.,ininterphasechromosomes. timescales and frequencies of contacts measured by live-cell
Self-entanglement of mitotic chromosomes have long been microscopyprovideafoundationforunderstandinginteractions
anticipatedduetothecriticalroleoftopoisomeraseIIinmitotic between functional elements (see Grosse-Holz86 and Tortora
compaction201,210,211 and as demonstrated in micromechani- etal.218forreviews).
cal experiments.212 A recent study showed that mitotic and Earlyworksinchromosomedynamicsinvertebratesusedhis-
interphase chromosomes have very different topological tone-fusedphotoactivatablegreenfluorescentprotein(GFP),al-
states,withmitoticchromosomesbeinghighlyself-entangled lowing fortrackingchanges inpatternsof globalchromosome
whileinterphaseisrelativelyfreeofknots,anditsuggesteda organization in the nucleus, and brought two key insights.219
pathwaythatallowscellstointerconvertbetweenthemascells First,dynamicsduringinterphaseisratherslowwithadisplace-
exitmitosis.208Yettoconverthighlyentangledmitoticchromo- mentof(cid:1)1mmduringan(cid:1)24-hinterphase.Second,agreatdeal
somesintoanunentangledinterphasestate,cellsrequirehigh ofrandomizationofpositionsofindividuallocioccursafteracell
activityoftopoisomeraseIIduringmitoticexit.Todirecttopo- division.
isomeraseIIactivitytowardunentanglementandthenpreserve Tracking of individual (or pairs of) loci in live cells allowed
this unentangled interphase state, a two-stage mitotic exit forquantifyingmean-squareddisplacement(MSD)overanin-
mechanismwasproposed.208Atthefirststage,decompaction tervalt,yieldingMSD(cid:1)tmwithm=0.35–0.5inbacteria,yeast,
while preserving mitotic loops biases topoisomerase II to fly,andmammaliancells.12,77,220–223InS.cerevisiae,measured
disentangle the mitotic state, creating the unentangled m=0.5221,224isinperfectagreementwithHi-Candmicroscopy
compactstateattelophase.Duringthesecondstage,chromo- and is characteristic of a motion of a locus of a flexible but
somes expand without much topoisomerase II activity, thus otherwiseunconstrainedpolymer(theso-calledRousemodel).
forming chromosomal territories and fractal globule states Surprisingly,mostofthestudiesinanimalcellsalsoreportedm=
inG1. 0.5,12,77,225 which is hard to reconcile with P(s) and R(s) and
Sisterchromatidsareinitiallytopologicallyintertwinedduring broadly with the fractal globule that is expected to give m=
and after S-phase. Such topological connections will maintain 0.2–0.4(seeTammandPolovnikov226forreview).Suchincon-
connectionsbetweensisterchromatidsevenintheabsenceof sistency between crumpled R(s) and unconstrained MSD
cohesivecohesincomplexes.Forsegregation,theseintertwines became most evident when both characteristics were
need to be removed. Loop extrusion in the presence of topo- measured using the same approach and in the same cells
isomerase II activity has been shown by modeling to drive (seeGrosse-Holz86andBru¨ckner227forreviews).Somestudies
compaction of each sister chromatid, while unlinking them.148 inmammaliancellsyieldedm=0.2interpretedasareflectionof
Ineffect,extrusionpullsthesistersawayfromeachother,which the properties of the nucleoplasm and suggesting a near gel
will drive the otherwise unbiased strand passage reaction by state of the chromatin.222 Live-cell measurements, however,
topoisomeraseIItowarddecatenation. and their analysis heavily rely on specifics of the experiment
andcorrectionforlocalizationuncertainty(seeGrosse-Holz86
THEPHYSICALSTATEOFCHROMOSOMES forreview).
Live-celltrackingalsoestimatesthetimeittakesforachro-
WhileHi-Cprovidescrucialinformationabouttheglobalstateof mosomal region to sample its conformations. For example,
chromatininthescalingofthecontactprobabilitywithgenomic in mammalian cells it takes about 40 min for a chromosomal
distanceP(s)(cid:1)s(cid:3)ɑ,206microscopymeasuresacomplementary region of 0.5 Mb to sample its conformations,12 only 5 min
characteristic: spatial separation R(s) (cid:1) sv. Interphase animal for two loci separated by 150 Mb to come sufficiently close
chromosomestypicallyyieldɑz1–1.2andvz0.25–0.3,73,213 ((cid:1)100–200 nm),77 while a larger ((cid:1)2-Mb) region didn’t equili-
for s z 0.5–10 Mb, both consistent with the fractal (crumpled) brate in 40 min.223 These times do not simply imply
globulefolding,i.e.,nearlyspace-fillingorganizationwherelong same times for functional molecular interactions between
continuous regions of the genome occupy continuous volumes chromosomal loci. For example, CTCF sites separated by
inspace.Thefractalglobulestateisperturbedbyextrudedloops 0.5 Mb form a stable interaction only about once per day
andthusisbestvisiblewhencohesinisdepletedandinsynchro- andrequirecohesin-mediatedextrusion.12Broadly,itremains
nizedcells,leadingtoP(s)(cid:1)s(cid:3)1.1scalingfrom10kbto10Mb to be seen how dynamics and proximity translate into func-
(e.g.,Schwarzeretal.,214,Hsiehetal.,126andSamejimaetal.24). tional interactions, which can critically depend on the radii
In S. cerevisiae, Hi-C and microscopy yield ɑ z 1.5 and v z over which such interactions can be established and on the
0.5,215–217bothcharacteristicofrandom-walkchains,indicating molecular context.
6432 Cell187,November14,2024
ll
Review OPENACCESS
havebeenproposedtoguidemitoticandmeioticchromosome
compactionandchromosomesegregation.228–230
Mechanicalperturbationofthewholenucleusdemonstrated
thatforsmalldisplacementsthenuclearresponseisdrivenby
elasticpropertiesofthepolymerofchromatinattachedtothenu-
clearlamina,whileforlargerdisplacementsitisthestretchingof
the lamina thatdetermines the response.231 Inducing elevated
levels of histone methylation makes chromatin stiffer, while
elevated histone acetylation makes it softer.232 This suggests
thatinsomecelltypes,chromatinmayplayaroleinproviding
optimalmechanicalpropertiesofthenucleus.
Micromechanical studiesof isolated human mitoticchromo-
somes230 have provided important insights by demonstrating
(1)theextraordinaryelasticityofchromosomesthatareableto
extendtomorethanfivetimestheirlength233;(2)theroleofhis-
tonemethylationinrigidifyingchromatin,consistentwithself-af-
finityofsuchheterochromatinregions234;(3)theroleofHP1al-
pha in mediating some of these interactions111; and (4) the
suggested key roles of condensins and topological entangle-
ment in providing mechanical stability of mitotic chromo-
somes.212 Broadly, these studies suggested that significant
crosslinkingturnsamitoticchromosomeintoagel.230However,
the nature of these crosslinks—topological vs. SMC vs. non-
SMCbased—areyettobeunderstood.
A recent study of interphase chromosomes was able to
perform a pull-release mechanical perturbation in live human
cells.85 These experiments showed that chromosomes re-
spondedasalmostunconstrained(Rouse)polymers,consistent
withtheirdynamics(seeabove).Surprisingly,chromosomalloci
could travel micrometers across the nucleus in mere minutes.
Models of a free polymer subject to weak affinities to the sur-
rounding media can reproduce this behavior of chromatin,
arguingthatinterphasechromosomes,unlikemitoticones,are
not gel-like or crosslinked. In summary, developing a physical
model ofinterphase chromosomes thatcan unifyHi-C,micro-
scopy, live-cell dynamics, and mechanics is an important
challenge.86
Figure5. Currentmodelsofinterphasechromosomeorganization
throughintegratedactivityofmultiplemechanisms FOLDINGCHROMOSOMESTHROUGHTHECOMBINED
Schematicdepictionofinterphasechromosomeconformationineukaryotes ACTIONOFDIFFERENTFOLDINGMECHANISMS
asthecombinedandintegratedresultofmultiplefoldingmechanisms.The
chromosomeisaworm-likechainthatphaseseparatesindistinctcompart-
ments(A/Bcompartmentsorfinersub-compartments)drivenbyhomotypic The final folding state of a chromosome, or whole genome, is
affinities.Tetheringofdomainstosub-nuclearstructures,suchasthenuclear determinedbythecombinedactionoftheseveralfoldingmech-
lamina,thenucleolus,ornuclearbodiesincludingspeckles,leadstoposi- anismsdescribedabove22,235,236(Figure5).Inadditiontophys-
tioningoflociandchromosomesatspecificnuclearlocations.Topological
constraintspreventmixingininterphase,butself-entanglementsareformedin icallinkage,everylocusissubjecttotheforcesimposedbythese
mitosis,facilitatingfullandfastcompaction.Atthescaleofhundredsofkilo- mechanismsthatcombineddetermineitspositionwithrespect
bases,loopextrusion,guided bycis-elements thatdetermineloading, un- tootherloci,itslocaldynamics,anditsassociationwithsub-nu-
loading,andblocking(CTCF)ofloopextruders,andwithextensiveinterplay
clearstructuressuchasthenuclearperipheryornuclearbodies
with other folding mechanisms, including compartmentalization, adds an
additionallayerofchromosomefolding. includingspecklesandnucleoli.Inaddition,thereisinterplaybe-
tween folding mechanisms, e.g., between loop extrusion and
compartmentalization so that chromosome folding is not just
Studiesofchromosomemechanics theadditiveeffectofeachprocessinisolation.Wediscussthe
ComplementarytopicturesobtainedbymicroscopyandHi-Care foldingofvertebrateinterphasegenomefoldingasanexample
studiesofchromosomemechanics.Loopformationandexpan- giventhatthisrepresentsthebestunderstoodcasebutempha-
sionandcompaction/expansionofchromatindomainsoccurin sizethatwebelievesuchcombinedactioncanexplainchromo-
thecontextofacrowdedchromatinenvironment,leadingtome- somefoldingmoregenerally.
chanicalforcesactingonchromosomes.Interplaybetweenmo- Ininterphase,alongthelengthofeachchromosometheepige-
lecularprocessesthatfoldchromosomesandmechanicalforces nome alternates forming a sequence of chromatin domains of
Cell187,November14,2024 6433
ll
OPENACCESS Review
differenttypes.Theprocessof(sub-)compartmentalizationleads Finally,eventhoughtopologicalentanglementsalongandbe-
to spatial clustering of loci of similar types, through an affinity- tweenchromosomesappeartoberareininterphase(ineukary-
drivenprocess.Thisprocessnaturallyproducesastochasticas- otes), this does not mean that topological transitions do not
semblyatthemegabase-to-whole-chromosomescale.Additional playaroleinmodulatinginterphasechromosomefoldingineu-
constraintsareimposedthroughtetheringlocitothenuclearpe- karyotes. For instance, the increased compartmentalization
riphery,thenucleolus,speckles,etc.Inaddition,highlydynamic observed upon acute depletion of cohesin is partly dependent
cohesin-mediated loop extrusion will bring loci together at the on topoisomerase II activity.208 Any real-time changes in
scaleofuptohundredsofkilobases.Alloftheseareactingona compartmentalizationmayinvolvemovementofloci,whichmay
chromatin fiber that is subject to topological constraints. As be facilitated by allowing topoisomerase II-dependent strand
describedabove,cohesinextrusionpatternsacrossthegenome passageingeneral.
areguidedbythepresenceofactiveenhancersthatcanfacilitate
cohesin loading, CTCF-bound sites that can block extrusion, THESAMEMECHANISMSCANPRODUCEDIFFERENT
and sites where cohesin is unloaded (e.g., downstream of FOLDEDSTATES
active genes). These cis-elements determine a cohesin ‘‘traffic
pattern’’183,186 that produces, over the cell population, a range Inmulticellularorganisms,duringinterphasedifferentcelltypes
ofstructuralfeaturesobservedbyHi-C:formationofcontiguous expressdifferentgenesthroughdifferentialactivityofcis-regula-
domains of enriched extrusion-dependent chromatin contacts tory elements, different patterns of histone modification, and
(TADs)boundedbynearbyCTCFsites;transientloopsbetween DNA methylation. Given that affinity-driven compartmentaliza-
convergentCTCFsites,enrichedcontactsbetweenCTCFsites, tion as well as cohesin-mediated loop extrusion are directly
andflankingdomains(stripesorflaresinHi-Cmaps);andsome guided and regulated by these features and cis-elements
enhancer-promoterinteractionsfacilitatedbyloopextrusionand (above),thewaythegenomeisfoldedindifferentcelltypesis
alsobyaffinity-driveninteractions(seebelow). different. However, although different loci will be clustered
Thereisimportantinterplaybetweendifferentfoldingmecha- togetherorlooped,thegeneralfoldingprinciplesarethesame:
nisms. This is perhaps best exemplified by the interaction be- affinitiesbetweensub-compartmentswilldrivetheirspatialclus-
tweencompartmentalizationandloopextrusion.237Loopextru- tering,andloopextrusionwilloccurthroughoutthegenomewith
sioncanextendtohundredsofkilobasesandcancrossfromone cohesinbeingrecruited,unloaded,andblockedatcis-elements
sub-compartment domain into another, thereby bringing activeinthatcelltype.
togetherlociofdifferentchromatinstatesthatwouldotherwise In contrast, chromosome organization can appear very
tendtospatiallysegregate.Thisaffectsnotjustdirectlyadjacent different in different species and kingdoms (e.g., prokaryotes
domains,buttheincreasedmixingofchromatinalsoappearsto vs.eukaryotes),andacrossthemitoticandmeioticcellcycles,
leadtomixingofdomainsatlargerscale,e.g.,interactionsbe- suggesting the possibility that in these cases, very different
tweencompartmentdomainsseparatedbylargegenomicdis- foldingprinciplesandmechanismsmaybeatwork.Akeyinsight
tances or even located on different chromosomes. In effect, fromextensive studies over the last decade on many different
loop extrusion makes different sub-compartments segregate species, and with cells that synchronously progress through
lessthantheyotherwisewould. thecellcycle,hasbeenthatinallcasesfoldingisdrivenbythe
Simulationssuggestthatthesearenotonlyextrudedloopsbut same small set of mechanisms described above. The reason
the whole active process of extrusion itself that weakens thisispossibleisthatthesemechanisms,andespeciallythepro-
compartmentalization.237Thiseffectisparticularlyclearlyvisible cess of loop extrusion, are particularly malleable and can be
inexperimentswhereloopextrusionisabolishedthroughrapid regulatedinmanydifferentways,resultinginavarietyofchromo-
depletionofcohesin,e.g.,usingdegronapproachestoinducibly somearchitectures.
degradesubunitsofthecohesincomplex.214,238Insuchexperi- Belowweprovideexamplesofhowdifferentialdeploymentof
ments, compartmentalization is more pronounced, i.e., com- loopextrusion,compartmentalization,tethering,andtopological
partmentssegregatebytypemorestrongly.Inaddition,smaller entanglements can give rise to a large diversity of structures
compartment domains emerged that in control cells appeared seenthroughoutthecellcycle,andevenacrosskingdoms.
subsumed by the flanking domains in a cohesin-dependent
manner. The compartment pattern seen in cohesin-depleted Interphasevs.mitosis
cellscorrelatesbetterwiththeepigenomeprofile,againshowing The dramatic changes in chromosome morphology during the
thatloopextrusioninterfereswiththenaturaltendencyfordo- cellcycleserveasanexcellentexampleofhowcellscanfold,
mains to compartmentalize via intrinsic affinity-driven pro- unfold,andrefoldtheirgenomestoaccommodategeneexpres-
cesses. sionininterphaseandaccuratechromosomesegregationduring
WhiletetheringoflocifromtheBcompartmenttotheperiph- mitosis (Figures 3B and 4B). As originally proposed based on
eryisnotdirectlydrivingcompartmentalizationitself,104itdoes extensive microscopy studies,30,133 biochemical and imaging
determinewhichBdomainsinteractwithwhichotherBdomains experiments,141,160,240andlatergenomic(5CandHi-C)studies
onotherchromosomes,observedwithHi-C.239Intheabsenceof and polymer modeling,15,16,24 we now understand that by late
suchtethering,e.g.,intheinvertednucleiofrodcells,thepro- prometaphaseeachsisterchromatidisfoldedasacompressed
cess of compartmentalization is unaffected, but the pattern in arrayofconsecutiveloops.Theseloopsareformedbyconden-
interchromosomal interactions between B compartment do- sin complexes: condensin II initially generates relatively large
mainsisaltered. (400-kbto1-Mb)loopsinprophase,andduringprometaphase,
6434 Cell187,November14,2024
ll
Review OPENACCESS
condensin I then splits these in smaller (100-kb) loops.16 This First,itispossiblethatthefactorsthatininterphasemediatethe
generates a nested arrangement of loops. In contrast to inter- affinity between compartment domains are inactivated.A good
phase, where many loops are positioned at reproducible sites exampleisthefamilyofHP1proteins.Theseproteinscanbridge
(e.g.,CTCFsites),positionedloopsarenotobservedinmitosis. locicontainingtheH3K9me3modification.Inmitosis,theresidue
Thearrayofloopsthenacquiresahelicalorganization.Thishe- immediately adjacent to K9 (H3S10) becomes phosphorylated.
licalorganizationrequirescondensinIIandisirregular.Perver- Histone tails carrying both modifications, H3K9me3 and
sions,wherethehandednessofthehelicalturnsalternatesevery H3S10P,cannotbeboundbyHP1proteins.246Giventhathistone
half turn, have been observed as well, and these have been tails become massively phosphorylated during mitosis, it is
linkedtothe presenceof connectionsbetweensisterchroma- possiblethatmanyotherbridgingfactorscannotbind,andthus
tids.241At the sametime chromatincondenses through global affinity-drivencompartmentalizationwillbeprevented.Analterna-
reductioninhistoneacetylation,leadingtogeneralaffinity-driven tive,oradditionalexplanationcomesfromaveryrecentstudythat
locus-locusinteractions.242InHi-Cstudies,nooronlyveryweak showed that when condensins are depleted while cells are ar-
AorBcompartmentshavebeenobserved. rested in prometaphase, some form of compartmentalization is
The organization of mitotic chromosomes appears very observed.115 This result suggests that the factors and mecha-
distinctfrominterphasechromosomesdescribedabove.How- nismsforcompartmentalizationareactiveduringmitosisbutare
ever,bothstatesaredrivenbymechanisticallysimilarloopextru- somehowoverruledbythecondensin-drivenlooparrayformation,
sion processes and affinity-driven locus-locus interactions. similar to how in interphase cohesin-mediated loop extrusion
Whatmakesthestructuresdistinctisthewaythesemechanisms counteractscompartmentalization.
areimplemented. Fourth,tetheringoflocitothenuclearperiphery,nucleoli,and
First,ininterphase,cohesinisthemainloop-extrudingcom- speckles dominate interphase nuclear organization. During
plex, whereas in mitosis two types of condensin complexes mitosisthesestructuresaredisassembled,andasaresultthe
act. This simple switch in extruder complexes explains much genome becomes untethered so that free rod-shaped mitotic
ofthedifferenceininterphaseandmitoticchromosomefolding. chromosomescanform.
AllcomplexesareestimatedtoextrudeDNAatsimilarspeeds Fifth,topologicalentanglementswithineachchromosomeare
(1–2kb/sinvitro156andinvivo24).However,cohesinhasarela- rareininterphase,butself-entanglementswithinindividualsister
tivelyshortresidencetimeonchromatin(5–20min),andthere- chromatidsareabundantinmitosis(above).Thisdifferencecan
foreinterphaseloopsarerelativelysparse,short-lived,anddy- atleastinpartbeexplainedsimplybythefactthattopoisomerase
namic.Incontrast,condensinIIcomplexesappeartorarelyor IIaactivityishighinmitosis,whichtogetherwithacondensedand
never dissociate during mitosis,243 and therefore they can compactedchromatinstatewilldrivethechromosomestoward
extrudelargerandmorestableloops.Thisalsoexplainswhyin becoming self-entangled. Polymer theory predicts that such
interphase only a fraction of DNA ((cid:1)60%12,149) is extruded in change in topological state will facilitate rapid compaction, as
loops at any given time, while by prometaphase, almost the wouldberequiredduringprometaphase.78However,moreactive
entiregenomeisextrudedandcontainedwithincondensinloops processesdrivingself-entanglementsmayalsobeatwork.
(Figure3B).
Second,cohesinandcondensindifferinhowtheyresolveen- Longvs.shortmitoticchromosomes
counterswithothercomplexesandproteinswhiletheyextrude In vitro, condensin complexes can bypass rather larger ob-
chromatin(above;Figure4).CohesinisblockedatCTCF-bound jects,172includingothercondensincomplexes.171Invivo,during
sitesinadirectionalmanner,leadingtopositionedandmoresta- mitosisitappearsthatsuchbypassingofcondensinsisrare,at
bleloopsbetweenpairsofconvergentCTCFsitesthatcanbe leastforcondensinIIinvertebrates.16,24Asaresult,condensin
cell-typespecific.Condensins,however,donotgetblockedby IIcomplexesextrudeloopstilltheyencounteroneanotherand
CTCF244oranyothercomplexasfarasweknow,andtherefore then stop so that a tightly spaced consecutive loop array is
theydonotformpositionedloops.Interestingly,duringmitosisin formed. This also strictly requires two-sided extrusion activity
living cells, condensins do not appear to bypass one another by condensin II,247 as observed in single-molecule experi-
invivo(Figure4),leadingtoconsecutiveratherthanoverlapping ments.164,165 The size of these loops, assuming condensin II
loops.15,16,24 doesnotturnover,willbedeterminedbyhowmanycondensins
Wenotethattheclearseparationofactionofcohesinsandcon- are recruited to chromatin.158 When many condensins are re-
densins during interphase and mitosis, respectively described cruited,loopswilltendtobesmallandmitoticchromatidswill
aboveforvertebrates,isnotalwayssoclear.InDrosophila,con- be relatively long and narrow. When fewer condensins are re-
densinIIplaysrolesinchromosomefoldingininterphase,andin cruited,loopswillonaveragebelarger,andmitoticchromatids
C. elegans, condensin I contributes to folding the interphase willbeshorterandwider.Thus,intheory,theoveralldimensions
genome.245 In budding yeast, cohesin extrudes loops during ofmitoticchromosomescanberegulatedsimplybyregulating
mitosis.216 condensinrecruitment.
Third,cell-type-specificaffinity-drivencompartmentalizationis Interestingly,mitoticchromosomescanhaveverydifferentdi-
amajorfeatureofinterphasechromosomesbutisabsentwithin mensions when compared between species, or even within a
mitoticchromosomes.Thishasbeenpuzzlingbecausethepat- species but at different stages of development. For instance,
ternsofhistonemodificationsalongchromosomesthatcorrelate whenmitoticchromosomedimensionsarecomparedforhuman
strongly with (sub-) compartments are largely preserved andmousecells,itwasobservedthattheydifferintheamountof
throughoutthecellcycle.Thereareseveralpossibleexplanations. DNAthatispacked permicronlengthof chromosome.244The
Cell187,November14,2024 6435
ll
OPENACCESS Review
difference was correlated with different loop sizes: in mouse (Figure4B).Consistentwiththisproposalisthatduringmeiosis,
cells, the mitotic loops are considerably larger than in human cohesin plays a significant role in loop array formation, and a
cells (1 Mb vs. 400 kb), suggesting fewer condensins are re- recentstudyshowedthat(mitotic)cohesincannotbypasscohe-
cruitedpermegabaseinmousecellsascomparedwithhuman sivecohesin.184CTCF,whichremainschromatinboundduring
cells.Intriguingly,thedifferencemayberelatedtothefactthat meioticprophaseandisalsofoundattheconjoinedaxesofsis-
mouse chromosomes areall acrocentric, and thusthe longest terchromatids,mayalsocontributetothisarrangementofcohe-
chromosome arm in the mouse genome is much longer than sin-mediatedsisterloops.254
the longest arm in the human genome. Increasing loop size Finally,itisnoteworthythatatearlyprophasestagesinmitosis
through regulating condensin recruitment genome-wide may inhumancells,sisterchromatidsarealsotransientlyconnected
ensure that even the longest chromosomes are short enough attheirloopbases.255Possiblycondensinsinitiallystallatcohe-
tofacilitatetheirsegregationduringanaphase. sivecohesincomplexesandonlylaterbypass.Clearly,howSMC
Asimilaradaptivescalingofmitoticchromosomedimensions complexesresolveencountersbetweenthemduringinterphase,
appearstooccurduringXenopusdevelopment.248Duringearly mitosis,andmeiosiscanleadtoverydistinctchromosomecon-
cleavage stages of development, the cells are very large, and formationsatthemacroscale.Severalofsuchrulesofengage-
mitoticchromosomesarerelativelylong.Atlaterstagesofdevel- ment have now been described,24 but surely additional ones
opment, when cells are much smaller, mitotic chromosomes remaintobediscovered.
becomeincreasinglyshort.Again,analysisofloopsizesshowed
thatthedifferenceisduetotheformationofsmallloopsinearly Acrossthetreeoflife:Prokaryotesvs.eukaryotes
stagesandlargerloopsatlaterstages.Differentialrecruitmentof Although bacterial nucleoids and eukaryotic chromosomes
condensincomplexeswouldexplainthisphenomenon.Interest- appearverydifferentinsizeandconformation,similarprocesses
ingly,factorsonthechromatinindifferentiated cellsappearto fold these genomes. Such similarities were already recognized
reduce condensin loading. One such factor could be histone and reviewed a number of years ago.256 Loop extrusion by
H1.8.InvitroreconstitutionexperimentsshowedthatinXenopus SMC-likecomplexesactonbacterialchromosomes,andasineu-
eggextracts,depletionofH1.8resultedinincreasedcondensin karyoticchromosomes,cis-elementscandeterminewherethese
recruitment,longerchromosomes,andsmallerloops.249 complexesloadandwheretheyareblocked(forreview,seeYa´-
Theseexamplesshowthatbysimplyregulatingtherecruitment n˜ez-CunaandKoszul257).Forinstance,inB.subtilis,theParSsites
ofloop-extrudingfactors,thesameprocessofloopextrusioncan at the centromere recruits SMC complexes that then start to
producemitoticchromosomesofdistinctdimensions.Thismakes extrude DNA bi-directionally, leading to co-alignment of the
mitoticchromosomearchitectureadaptabletoensurecondition- arms of the chromosomes.175 In E. coli, SMC-like complexes
appropriatescalingofchromosomearmlength. extrudeDNAwithineacharm,therebycondensingthenucleoid.
Interestingly,inB.subtilis,withengineeredarrangementofParS
Mitosisvs.meiosis sites complicated patterns of folding have been observed that
Mitoticandmeioticchromosomesarebothfoldedasarraysof can be explained when SMC complexes can bypass one
loops to form rod-shaped compacted chromatids. While tran- another.185Suchbypassingcanbecriticaltoavoidtrafficjamsbe-
scriptionceasesduringmitosisandcompartmentsbecomeun- tweenSMCsloadedatninenativeproximalParSsites,providing
detectable, during meiotic prophase I, transcription continues anotherexampleofa‘‘ruleofengagement’’wherebyresolutionof
and a form of compartmentalization remains present.250,251 molecularencountersbetweenextrudingcomplexescandeter-
Another key difference is how sister chromatids are arranged minefoldingofentiregenomes.
withrespecttoeachother:inmitosis,byprometaphase,sister Inbacteria,topologicalfeaturesappeartoplayamuchmore
chromatids are connected through cohesin-mediated connec- dominantroleinchromosomefoldingthanininterphaseineukary-
tions within their loops. Microscopically, this can be deduced otes.Supercoilingwillcompactthenucleoidandisdeterminedby
fromthefactthatcohesincomplexesarelocalizedinbetween transcriptionandreplicationbutalsodirectlybyenzymessuchas
themassesofeachsisterchromatidandawayfromtheconden- gyrasethatintroducepositivesupercoiling.Interestingly,chromo-
sincomplexesthatarelocatedatthebasesoftheloopsinthe somalinteractiondomains(CIDs)havebeenobservedalongthe
centerofeachchromatid.24,252Incontrast,duringmeioticpro- C.crescentusandB.subtilischromosomesthatinHi-Cresem-
phase, sisters are cohesed at the bases of the loops.253 We blesTADs.176CIDs,however,couldbeformedinanSMC-inde-
recentlyproposedthatthemitoticarrangementcouldarisenatu- pendentmannerasdensearraysofplectonemesthataresepa-
rallywhenactivelyextrudingcondensinsstepovercohesincom- ratedbyplectoneme-freeregionsathighlyexpressedgenes.
plexesthatholdsisterchromatidstogether(so-calledcohesive Finally,eventhoughconventionalcompartmentalizationisnot
cohesincomplexes).24Thiswillresultincohesivecohesinbeing observed, some form of affinity-driven clustering of loci can
localized inside condensin-mediated loops. Modeling showed occur in bacteria. For instance, nucleoid-associated proteins,
thatwhencondensin,oranyotherloop-extrudingcomplex(co- suchasHUandH-NS,canactasbridgingfactorscondensing
hesin likely in meiosis), cannot bypass cohesive cohesins, the chromosomaldomains.258
extruding complexes and cohesive cohesins will both localize
atthebaseoftheloops,ascenariothatmaybepresentduring Acrossthetreeoflife:Morevariationsoffolding
meioticprophase.Itisthereforepossiblethatbysimplymodu- mechanisms,andpossiblyadditionalmechanisms?
lating the ability to bypass cohesive cohesins, one can obtain Inarecentstudy,chromosomefoldingfor24eukaryoticspecies
either the mitotic or meiotic arrangement of sister chromatids fromacrossthetreeoflifewasstudiedbyHi-C.51Theseincluded
6436 Cell187,November14,2024
ll
Review OPENACCESS
severalvertebrateclassesandanimalphyla,plants,andfungi. foldingintheseorganisms.Theyexpresscondensin-andcohe-
Two main types of folding architectures were described: one sin-likecomplexes,andthereforeitispossiblethattheyrepre-
type is defined by a Rabl-like organization with centromeres sent yet another example where new ways have evolved to
clustered,telomeresclustered,and/orchromosomearmsbeing employtheseconservedfoldingmachines.Ontheotherhand,
alignedtoeachotherfromcentromeretotelomere;thesecond giventhattheirchromosomesappearsodifferentfromanyother
typelacksthesefeaturesbuthaschromosometerritories.Inter- group,itisalsopossiblethatnewmechanismstofoldchromo-
estingly,asinglefactor,thepresenceorabsenceofcondensinII, someshaveemergedinthislineage.
defines whether the first type or the second type is formed.
The authors proposed a model where condensin II mediates STRUCTURE-FUNCTIONRELATIONSHIPS
length-wide compaction during mitosis, which then facilitates
chromosometerritoryformationinthenextG1,whilepreventing Higher-order chromosome folding in eukaryotes is linked to
centromere and telomere clustering. This study shows how genomic functions, including for instance, chromosome
genome-wide chromosome-foldingpatterns in eukaryotes can compaction,segregation,andregulationoftranscription.How-
bealteredbysimplyturningoneextrusioncomplexonoroff. ever,despiteextensiveefforts,ithasprovendifficulttodemon-
These results show that studying chromosome folding in a stratethathigher-orderfoldinghasconsistent,conserved,and
rangeofspeciescanbefruitfulforgainingabetterunderstanding genome-wideconsequencesforgeneexpression.Thisislikely
ofthebasicchromosomefoldingmechanismsdiscussedhere. because the primary function of chromosome folding is not
Throughsuchanapproach,wecandiscoveradditionalwaysin generegulationbutinsteadisforcellstomanagelongDNAmol-
whichtheseconservedmechanismscanberegulatedandim- eculestoensuretheirreplication,compaction,segregation,and
plemented.Possiblynewvariantsofthebasicmachinery,e.g., subsequent decompaction. Consistent with this, the proteins
additional SMC complexes, can be discovered. Finally, it is involved in chromosome compaction, especially the factors
possiblethatentirelynewandyettobediscoveredmechanisms thatperformloopextrusionappearconservedinallorganisms.
of folding chromosomes remain to bediscovered in groups of Weproposethatoncemechanismsforfoldingandunfoldingge-
specieswithhighlydivergentchromosomeconformations. nomesareinplace,thesesamemechanisms,e.g.,loopextru-
Weenvisiontwowaystoselectgroupsoforganismsforsuch sionandaffinity-drivenclusteringofloci,aresubsequentlyco-
evolutionarystudies.First,onecanstudygroupsoforganisms opted for roles in additional processes, including long-range
that contain distinct variants of the conserved machineries for regulation of genes by distal regulatory elements, etc. (see
chromosomefolding.Anexamplearethetwomajorgroupsof below). Given that these latter functions are secondary, and
archaea,theeuryarchaeaandcrenarchaea.Thesesingle-cellor- possiblyadhoc,chromosomefoldingwillnotnecessarilyhave
ganisms differ in how they organize chromatin and have been consistent, conserved, and genome-wide roles for regulating
studied only recently using 3C-based assays. Interestingly, expression of all genes and in different organisms. Such roles
botharchaealgroupsexpressSMC-relatedproteins,andthese of chromosome-folding processes in gene regulation and,
proteinsmayplayrolesinchromosomefolding.259Inmostcases broadly, in epigenetic mechanisms have started to emerge in
ineuryarchaea,thesecomplexesareclearlyrelatedtoconden- disparate biological systems, with universal effects yet to be
sins.Intriguingly,thecrenarchaeaappeartohavelostthecon- discovered.
densin-like SMC complex and instead have acquired a poorly
characterized SMC-like complex called coalescin.260 Hi-C Functionalrolesformitoticchromosomecompaction
studiesshowthatcoalescinplaysrolesinchromosomefolding The most obvious functional role of chromosome folding is
andcompartmentalization.ThefactthatanSMC-relatedcom- related to chromosome duplication and segregation. In large
plex may be involved in compartmentalization may point to a vertebrate genomes, loci replicate at different times during
newroleforanSMCcomplex,andithighlightshowthestudy S-phase.Thisphenomenonshowsaclearconnectionwithchro-
ofdivergentspeciescanprovideopportunitiestodiscovernew mosome folding: DNA replication timing is strongly correlated
roles or new ways to employ these otherwise conserved ma- withcompartmentalization,263andwhenreplicationtimingisdis-
chineries. ruptedoraltered,thiscanleadtochangesincompartmentaliza-
In a second approach, one can select species that display tion.264 After replication, sister chromatids are to a significant
chromosome conformations that appear particularly different level topologically intertwined. These interlinks need to be
fromanyothergroupofspecies.Oneexampleisthedinoflagel- resolvedtofacilitatetheirsegregationduringanaphase.Inaddi-
lates. Dinoflagellates are single-cell eukaryotes with very large tion,eachsisterchromatidneedstocompactintomitoticchro-
genomes (up to hundreds of gigabases), which do not wrap matids. In eukaryotes this involves the formation of arrays of
thebulkoftheirgenomearoundnucleosomes.Macroscopically, loopsmostlybythecondensincomplexes(above).Theseloops
dinoflagellatechromosomesappearverydistinctfromanyother can become topologically interlinked (i.e., mitotic chromatids
group261,262: the chromosomes are permanently condensed can become self-entangled). These two processes are likely
throughthecellcycle,andtheyhaveopticalpropertiesthatsug- mechanisticallylinkedasloopextrusionincis,inthepresence
gestaliquidcrystallinearrangementofchromatinfiberswithin oftopoisomeraseIIenzymes,andwillautomaticallydrivethesis-
them. Recent Hi-C studies show that the chromosomes are ter chromatids to become unlinked while they are still held
composed of structural domains, resembling TADs and CIDs, together by cohesive cohesin complexes.148 The function of
eachofwhichcontainsapairofdivergentlytranscribedgenear- thiselaborateprocessoffolding,self-entangling,andunlinking
rays.7,8Verylittleisknownaboutthemechanismofchromosome sister chromatids is to facilitate chromosome segregation to
Cell187,November14,2024 6437
ll
OPENACCESS Review
daughter cells. Anyfunctional role of self-entanglement is less ond,evenwhenenhancersandpromotershavebeenobserved
understood.Ithasbeenshown,throughmicromechanicalmea- inclosespatialproximity,thedistancethatseparatesthemwas
surementsofsingleisolatedmitoticchromosomes,thathuman relativelylarge,i.e.,300nm.273
mitoticchromosomesareself-entangledandthattheseentan- Severalnewinsights,experimentalapproachesandmodels,
glementscontributetomechanicalrigidityofchromosomes.212 arenowattemptingtounifytheseobservations.First,thediscov-
Suchrigiditymaybeimportantforchromosomesegregationto erythattranscriptioncomplexescanformcondensatesthatcan
counteractspindleforces. be several hundreds of nanometers in diameter suggests that
suchcondensatescanpotentiallymediateconnectionsbetween
Rolesofchromosomefoldingincontrollinggene enhancerandpromoters.273Byimaging,theenhancerandpro-
expression motercanthenappearnottobedirectlytouching,yet3C-based
Ineukaryoticcells,genescanberegulatedbyenhancersthatare assays that employ formaldehyde crosslinking may still detect
locateduptomanyhundredsofkilobasesfromtheirpromoter.A thesecontactsasloopinginteractions.
long-standingmodelhasbeenthatthespatialfoldingofchromo- Second, several models have been proposed to explain the
somes would allow enhancers to loop to gene promoters and lackofsimplecorrelation betweenthefrequency ofenhancer-
throughphysicalinteractionsbetweencomplexesboundtothe promoter contacts (measured by Hi-C and microscopy) and
enhancer and the promoter and possibly, through factors transcriptionfromthetargetpromoter.274,275Theideaofthese
bridging them such as the Mediator complex, would activate modelsisthattransientandrareenhancer-promoterinteractions
transcription.265,266Othermechanismshavealsobeenputforth, result in the incremental but cumulative changes in the multi-
such as models where factors recruited at an enhancer can statepromoter,withonlythefinalstateresultingintranscription.
somehow travel along chromatin over considerable distances These changes may, for example, reflect the accumulation of
andinthatwayreachtargetpromotersthatarethenactivated marks at the promoter and enhancer. Importantly, such multi-
withoutneedingadirectphysicalinteractionbetweentheseele- statemodelsshowasigmoidalresponsetocontactfrequency
ments (‘‘tracking models’’). In the latter case, chromosome with small changes in contact frequency resulting in large
folding may not be critical for long-range gene regulation. It changesintranscription.Whenacriticallevelofmarksisdeliv-
nowappearsmultiplemechanismsmaycontribute. ered,thepromoterwillbecomeactive.Thesemodelsofmulti-
Oneofthefirstapplicationsof3C-basedassayshadbeento state promoters await validation by experimental live-cell dy-
determinewhetherloopinginteractionsbetweengenesandtheir namic measurements of distance and transcription at high
distal regulatory elements occur. In a very early study, it was temporalandspatialresolutions.
found that the locus control region (LCR) of the mouse beta- Whatisthemechanismbywhichanenhancercanlooptotarget
globin locus physically touches a target beta-globin gene only promoters?Oneattractiveproposalisthatcohesin-mediatedloop
in cell types where that gene is expressed.267 Further work extrusionactivelybringselementstogether.Theobservationthat
showed that when different beta-globin genes become active transcriptionalelements,suchasenhancers,promoters,insula-
during development, the LCR switches its long-range interac- tors(CTCFsites),and30endsofactivegenes,allplayrolesinre-
tionsaccordingly.268Thislocusremainsoneofthebeststudied cruiting,pausing,blocking,andunloadingcohesin,respectively,
examplesoflong-rangeinteractionsinrelationtogeneexpres- alreadysuggestslinksbetweentranscriptionalcontrolandcohe-
sion.Inademonstrationoftheimportanceofphysicalinterac- sin-mediatedloopextrusion.183,186However,acutedepletionof
tions between enhancers and promoters, it was shown that cohesin was found to have little immediate effect on transcrip-
directtetheringofthedistalLCRtothetargetgeneissufficient tion.154,214Mostrecentstudies,however,demonstratedthatthe
foractivationofthegene.269 lossofcohesinactivityinpostmitoticcellshasaprofoundeffect
Sincethen,numerousstudieshavedetectedmanymorelong- oncellandorganismphysiology,suchasneuronalmaturation276
range promoter-enhancer interactions, e.g., in single gene anddifferentiationandresponsetoactivationbydendriticcellsof
studies for the alpha-globin locus,129 in higher throughput theinnateimmunesystem.277
studiesforhundredsofgenesthroughoutnumeroustargetedre- Afteryearsofconflictingobservations,aunifiedviewisnow
gionsofthehumangenome(5C270),oringenome-wideanalyses emergingonhowcohesinplaysaroleinlong-rangegeneregu-
using targeted approaches (Capture-C,271 and ChiaPET59). lation(Figure6).Inthisview,cohesincanbeloadedatrandom
Fromthesestudies,onewouldconcludethattheloopingmodel positions, with some preference for cis-elements such as en-
is firmly established. However, other lines of experimentation hancers.Thesecomplexescanthenextrudeloopsandthrough
producedobservationsthatwereatfirstglancenotconsistent this process reach distal target promoters. This can lead to
withthe‘‘activationbyphysicalcontact’’modelforlong-range detectableenhancer-promoterloopsin3C-basedassays.How-
control of gene expression. First, imaging-based studies ever,insuchassays,theseinteractionsappearweak,suggest-
showedthat3Dspatialdistancesbetweenenhancersandpro- ing these are either rare or very transient contacts. As stated
motersdonotcorrelatewellwithgeneactivation,neitherinlive above, repeated transient interactions may be sufficient to
cells in real time nor over cell populations (reviewed by Chen triggerchangesinpromoterstatesthatwillbecomeactiveafter
etal.272).Furthermore,arelativelysmall((cid:1)2-to3-fold)increase severalinteractions.
inthecontactfrequencywithinaTADresultsinamuchgreater Anotherfactoristhatenhancer-promotercommunicationmay
activationoftranscription.Thislackofcorrelationbetweencon- requireadifferenttypeofinteractionthancontactscapturedby
tacts,orcloseproximity,andgeneactivationmayappeartobe 3C-based assays or microscopy. For example, functional
inconsistent with a mechanistic role of looping contacts. Sec- communication may require close interactions between
6438 Cell187,November14,2024
