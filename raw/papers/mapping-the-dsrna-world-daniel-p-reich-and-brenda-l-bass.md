---
source_path: /mnt/c/Users/Administrator/Zotero/storage/6S72QEY6/Reich和Bass - 2019 - Mapping the dsRNA World.pdf
ingested: 2026-04-23
sha256: ed0174506f19a2b3
---

Mapping the dsRNA World
Daniel P. Reich and Brenda L. Bass
DepartmentofBiochemistry,UniversityofUtah,SaltLakeCity,Utah84112
Correspondence:bbass@biochem.utah.edu
SUMMARY
Long double-stranded RNAs (dsRNAs) are abundantly expressed in animals, in which they
′
frequentlyoccurinintronsand3 untranslatedregionsofmRNAs.Functionsoflong,cellular
dsRNAs are poorly understood, although deficiencies in adenosine deaminases that act on
RNA,orADARs,promotetheirrecognitionasviraldsRNAandanaberrantimmuneresponse.
DiversedsRNA-bindingproteinsbindcellulardsRNAs,hintingatadditionalroles.Understand-
ingtheserolesisfacilitatedbymappingthegenomiclocationsthatexpressdsRNAinvarious
tissuesandorganisms.ADAReditingprovidesasignatureofdsRNAstructureincellulartran-
scripts.Inthisreview,wedetailapproachestomapADAReditingsitesanddsRNAsgenome-
wide, with particular focus on high-throughput sequencing methods and considerations for
theirsuccessfulapplicationtothedetectionofeditingsitesanddsRNAs.
Outline
1 Introduction 5 FindingeditedRNAsinhigh-throughput
datasets
2 ThedsRNAworldisaworldgovernedby
differentpropertiesthantheRNAworld 6 Lookingtowardthefuture
3 FeaturesofthedsRNAome References
4 Historicalperspectiveonmethodstofind
ADAReditingsites
Editors:ThomasR.Cech,JoanA.Steitz,andJohnF.Atkins
AdditionalPerspectivesonRNAWorldsavailableatwww.cshperspectives.org
Copyright#2019ColdSpringHarborLaboratoryPress;allrightsreserved;doi:10.1101/cshperspect.a035352
CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352 1
D.P.ReichandB.L.Bass
1 INTRODUCTION ger an immune response. The source of viral dsRNA is
attributedtogenomesofdsRNAviruses,replicationinter-
TheabilityofRNAtocopyitself,orreplicate,isakeyfeature
mediatesandcopy-backstructuresofsingle-strandedRNA
ofanRNAworld,allowingDarwinianevolutionandwhat
viruses,andbidirectionaltranscriptionofcertainDNAvi-
wecalllife(Rich1962;Gilbert1986;Joyce2002;Robertson
ruses(Schlee2013).Whenassayed,thisdsRNAistypically
andJoyce2012).TheRNAWorldhypothesisassumesthat
Watson–Crickbase-pairingwaskeytoreplicationinapri-
≥100basepairs(Pfalleretal.2015)andthusdistinctfrom
mordial cell. Thus, by definition, replication of an RNA smaller silencing RNAs, such as microRNAs (miRNAs)
andsmall-interferingRNAs(siRNAs).Itisnowclearthat
genomeinvolveddouble-strandedRNA(dsRNA)interme-
our own cells encode and express long dsRNA, in both
diates,andevolutionofmodern-daycellslikelyoccurredin
vertebratesandinvertebrates(Whippleet al.2015;Blango
theconstantpresenceofdsRNA.Ourgoalinthisreviewis
and Bass 2016; Reich et al. 2018), and that the adenosine
todescribetheuniquepropertiesdsRNAconfersonabio-
deaminasesthatactonRNA(ADARs),byconvertingaden-
logicalsystemandthetechniquesusedforthegenome-wide
osine to inosine (A-to-I), mark a dsRNA as self (Hartner
mappingofdsRNA(i.e.,determiningadsRNAome).
etal.2009;Mannionetal.2014;Liddicoatetal.2015;Pestal
Inmodern-daycells,nucleicacidsplaykeyandobvious
etal.2015;Georgeetal.2016;Reichetal.2018).Tounder-
roles, but they are also fundamental to self versus nonself
standhowcellsdiscriminatebetweenselfdsRNAandnon-
discrimination(Crowletal.2017).ThediverseRNAediting
and modifications found in all kingdoms of life, in recent self viral dsRNA, it is important to understand the
dsRNAome.
years referred to as the Epitranscriptome (Saletore et al.
2012), have myriad functions in modern-day cells, but it
seemsveryplausible,andothershaveproposed(Eigenbrod
etal.2015;O’Connelletal.2015),thattheyoriginatedasa 2 THEdsRNAWORLDISAWORLDGOVERNEDBY
means to discriminate self from nonself. Selfish elements DIFFERENTPROPERTIESTHANTHERNAWORLD
and viruses of the early RNA world also may have had There are several properties of the dsRNAworld that are
an RNA genome that replicated through a dsRNA inter- distinctfromthoseoftheRNAworld.First,theRNAsthat
mediate. Perhaps reflecting an ancient and ongoing con- comprisethedsRNAworldarerod-shapedmoleculesthat
flict between cells and selfish elements, in modern cells, can stretch for hundreds of base pairs with few branches
dsRNA-mediated pathways play critical roles in immune (Fig. 1). Short dsRNA helices are the secondarystructural
defenseinresponsetoviralinfection. elements that assemble to create the three-dimensional
Viruses have long been known to give rise to dsRNA shapes of RNA molecules. However, with few exceptions
(EhrenfeldandHunt1971),whichactsinthecytoplasmas (Riederetal.2013),dsRNA-bindingproteins(dsRBPs)do
a pathogen-associated molecularpattern (PAMP), to trig- notbinddsRNAhelicesthatareburiedintertiarystructure.
~170 base pairs
~250 base pairs
Mouse Sppl2a 3′ UTR
ΔG = –1096 kcal/mol
~290 base pairs
Human SPPL2A 3′ UTR C. elegans eif-2α pre-mRNA
ΔG = –2100 kcal/mol ΔG = –2012 kcal/mol
Figure1.Representativedouble-strandedRNAs(dsRNAs)fromthreeorganisms.UNAfold-predictedRNAstruc-
turesareshownformouseSppl2a3′ untranslatedregion(3′ UTR),humanSPPL2A3′ UTR,andCaenorhabditis
eleganseif-2αpre-mRNA.Approximatelengthsofhighlybase-pairedregionsareshownforscale,andminimum
(moststable)predictedfoldingfreeenergies(ΔG)arereportedbeneathstructures.
2 CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352
MappingthedsRNAWorld
ADAR and PKR do not bind transfer RNA (tRNA) (Bass Figure 2 illustrates three dsRNAomes, with genomic
and Weintraub 1987; Schmedt et al. 1995), and similarly, locations that express dsRNA, sometimes called editing
the A-to-I modifications created by ADARs are not ob- enriched regions (EERs), indicated on chromosomes of
served in ribosomal RNA (rRNA) (Paul and Bass 1998). mouse, human, and Caenorhabditis elegans. Based on
ThepreferenceforbindingtodsRNAthatisnotburiedin dsRNAomes determined to date (Table 1), dsRNA is pre-
tertiary structure is likely important for self:nonself dis- dominantly encoded within protein-coding genes, rather
criminationbydsRBPs.Althoughwild-typeRIG-I,adsRBP thanintergenicregions,with5.9%ofprotein-codinggenes
essential for the mammalian innate immune response, encoding structures in C. elegans, 13% in human mono-
shows limited association with rRNA, a RIG-I mutation cytes, and 1.3% in mouse bone marrow–derived macro-
observedinSingleton–Mertensyndromeallowstheprotein phages.(Repetitiveelementsinmousearemoredivergent,
toassociatewithdsRNAexpansionsequencesinthelarge resultinginfewerpairingpartnersandlowerfreeenergies
rRNAsubunit (Lässigetal.2015). [Neemanetal.2006;BlangoandBass2016].)Forprotein-
Because of the A-form structure of dsRNA, which in- codinggenes,structuresmostlyinhabitnoncodingregions
cludes a deep major groove, it is difficult for dsRBPs to of mRNAs, introns and 3 ′ untranslated regions (UTRs).
recognize dsRNA sequence (Tian et al. 2004). In fact, al- Base-pairingusuallyoccursintramolecularly(Fig.1),with
though dsRBPs bind tightly to dsRNA, typically showing complementarysequenceswithinasingletranscriptfolding
dissociation constants in the nanomolar range (Kim et al. backonthemselves.ThedsRNAsarepredictedtofoldinto
1994;Schmedtetal.1995;Ohmanetal.2000;Maetal.2008; remarkably stable structures (Table 1) and, depending on
Parkeretal.2008;Sinhaetal.2015),theyarenotsequence- the organism, encompass an average of 546–845 nucleo-
specific.ThissecondpropertyofthedsRNAworldiskeyto tides(nt).
functionsofdsRBPs,whichinteractwithdsRNAsofdiverse ThechromosomemapsofFigure2highlightinteresting
sequences. For example, Dicer must bind pre-miRNAs of trends—somethatareeasilyexplainedandothersthatare
many different sequences (Daugaard and Hansen 2017), enigmatic,possiblyhintingatEERfunctions.Forexample,
ADARsmusteditnumerousdistinctdsRNAs(Bajadetal. humanchromosome19hasadenseconcentrationofEERs,
2017),andantiviraldsRBPsmustbinddiverseviralRNAs likelybecauseitisgene-rich,withahighnumberofrepet-
(Yooetal.2014).ConsistentwiththeideathatdsRBPshave itiveelements(Grimwoodetal.2004).Consistentwiththeir
structuralspecificityfortheA-formhelix,disruptionstothe abilitytobase-pair,repeats,especiallythosethatareinvert-
helix,suchasmismatchesandloops,canestablisharegister ed,inhabitmanyEERs(Fig.3).Abundantrepeatclassesare
for dsRBP binding (Lehmann and Bass 1999). Similarly, represented in EERs, like Alu elements, which occur in
althoughdsRBPscannotaccessfunctionalgroupsofbases more than a million copies in the human genome (Bazak
withinthemajorgrooveofcompletelybase-paireddsRNA, etal.2014)andDNAtransposons,comprising12.6%ofthe
sequence-specific contacts in the minor groove can also C.elegansgenome(AhringerandGasser2018).Compari-
establishregister(Stefletal.2010). sonsoftranscriptswiththegreatestnumberofeditingsites,
ThefinalpropertyofthedsRNAworldisderivativeof or“hyperedited”dsRNAs,indiversemetazoa,indicatethat
thefirsttwo.BecausedsRBPsallbinddsRNA,andtheyare repeats,particularlytransposon-derivedrepeats,giveriseto
notsequence-specific,thedsRNAworldisaworldofcon- mostcellulardsRNAs(Porathetal.2017).
stantcompetition.Duringitslifetime,agivendsRNAmay IntheC.elegansdsRNAome,EERsareenrichedondis-
interactwithmultipledsRBPs. talarms,orchromosomeends,ofautosomes(Fig.2).This
trendisnotobservedontheXchromosome,whichoverall
has fewer EERs. Distal arms of C. elegans chromosomes
3 FEATURESOFTHEdsRNAome
show properties of heterochromatin and, compared with
This review focuses on methods used to determine centralregions,havefeweressentialgenes,morerepetitive
dsRNAomes, and with few exceptions, these involve the elements,lowerlevels ofgeneexpression,andlongerthan
determination of ADAR RNA editing sites. ADARs are a averageintrons(Prachumwatetal.2004;Liuetal.2011;Ho
familyofRNAeditingenzymes,presentinallanimals(Def- et al. 2014; Ahringer and Gasser 2018). Intriguingly, al-
fit and Hundley 2016; Nishikura 2016; Walkley and Li thoughEERsalsoareenrichedforrepetitiveelementsand
′
2017).ADARstargetonlydsRNA,andthelongeradsRNA inhabitlongerthanaverageintronsand3 UTRs,theytyp-
is,themoreeditingsitesitwillacquire.Theobservationof ically inhabit genes with higher than average expression
ADAReditingsitesinanendogenousRNAisproofthatthe (Fig.4).Exceptforthecorrelationwithrepetitiveelements,
RNAisdouble-strandedinvivo, agoldstandardusednot asobservedonhumanchromosome19,anenrichmentof
only in determining dsRNAomes, but also as proof for EERsonspecificregionsofmammalianchromosomeshas
specificdsRNAstructures(SijenandPlasterk2003). notbeenobserved.
CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352 3
D.P.ReichandB.L.Bass
342 mouse EERs (BMDMs) 3438 human EERs (peripheral blood monocytes)
1 1
2 2
3
3
4
4
5
5
6
6
7
7 8
8 9
9 10
1962 C. elegans EERs
10 11 (all developmental stages)
12
11
13 I
12
14 II
13
15 III
14
16 IV
15 17
V
16 18
X
17 19
18 20 1 Mb
21
19
22
X
X = Editing-enriched regions
Y
Y
10 Mb
10 Mb
Figure2.Mouse,human,andCaenorhabditiselegansdsRNAomes.Verticalblacklinesdenotepositionsofediting
enrichedregions(EERs)onchromosomesofmouse,human,andC.elegans.Chromosomesarenotdrawntoscale,so
thehorizontalblackbarsatthebottomdisplayrelativechromosomelength.MapsofmouseandhumandsRNAomes
weregeneratedwithIdiographicaandthatforC.eleganswithPhenoGram(KinandOno2007;Wolfeetal.2013).
BMDMs,bonemarrow–derivedmacrophages.
AlthoughEERsarenotconservedatasequencelevel,of in the same locations in orthologous genes, and an EER
the285mousegenesthatcontainEERs,74(26%)havean withinanintroncanbeinaUTRintheortholog.Regardless,
orthologoushumangenewithanEER(p<0.0001,χ2test) thepresenceofEERsandstructuredintronsinorthologous
(BlangoandBass2016).Similarly,whereasaCaenorhabditis genesandchromosomaldomainsraisesthepossibilityofa
briggsae dsRNAome has not been determined, of 1092 conservedfunctioningeneregulation.
C. elegans genes with a structured intron (ΔG/nt<–0.5
∗
kcal/mole ntat20°C),147haveanorthologousC.briggsae
gene with a structured intron, a significant enrichment 4 HISTORICALPERSPECTIVEONMETHODS
abovetheexpectednumber(p<0.0001,χ2test).Structured TOFINDADAREDITINGSITES
intronsclusteronautosomedistalarmsinC.briggsae,asin ADARswerediscoveredwhenperfectlybase-paireddsRNA
C.elegans(Fig.5).EERsandstructuredintronsdonotoccur wasinjectedintoXenopuslaevisembryos.Researchersno-
Table1.PropertiesoflongdsRNAs(EERs)
EERs EER-associatedgenes
Organism(celltype) # Length(nt) ΔG/nta # %ofallgenesb %withintronicEERs %with3′-UTREERs
Caenorhabditiselegans 1962 563 −0.349 1196 5.9 65.0 41.6
Mouse(BMDMs) 342 546 −0.307 285 1.3 20.4 69.1
Human(monocytes) 3438 845 −0.346 2792 13.0 57.4 23.9
EERs,editingenrichedregions;UTR,untranslatedregion;ΔG,predictedfoldingfreeenergy;nt,nucleotide;BMDMs,bonemarrow–derivedmacrophages.
aPredictedat37°C;kcal/mol∗nt.
bProtein-codinggenesonly.
4 CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352
Mouse EERs cultured cells (Wagner and Nishikura 1988). Subsequent
studies, using thin-layer chromatography or high-perfor-
manceliquidchromatography(HPLC)toanalyzenucleo-
SINE
tides in treated dsRNA, revealed the activity involved
Non- 32.2% covalent modification of adenosine to inosine (Bass and
repetitive
Weintraub 1988; Wagner et al. 1989). Only then was it
43.6% realized that dsRNA strands were not being unwound.
9.3% Rather, the RNA was becoming more single-stranded in
LTR characterasAUbasepairswerechangedtoIUmismatches.
AlthoughADARsindeedchangethestabilityofdsRNA,to
Other: 3.4% LINE: 5.5%
datethereisnoexampleinwhicheditingcausesdsRNAto
Simple repeat: 2.6% Satellite: 3.4%
completely separate into two single strands. Subsequent
studiesrevealedthatA-to-Iconversionoccurredbyhydro-
Human EERs
lyticdeamination(Polsonetal.1991),andtheactivitywas
briefly called dsRAD or DRADA. In 1997, researchers
agreedtorenametheenzymeADAR,basedonrecommen-
Non- Alu dationsbytheHUGOcommittee(Bassetal.1997).
repetitive
37.1% Although ADAR activity in the above studies was de-
42.8%
tectedusingdsRNApreparedinvitro,itwasnotlongbefore
in vivo editing within naturally occurring transcripts was
Other: 3.4% reported. The first example was identified serendipitously
9.3% bySangersequencingofclonedcDNAsmadefrommeasles
DNA TE: 2.9%
virus transcripts (Cattaneo et al. 1988; Bass et al. 1989).
LTR: 4.5% LINE
Inosine base-pairs like guanosine and prefersto pair with
cytidine. Thus, reverse transcription of RNA containing
C. elegans EERs
****
10000
Non-
repetitive
DNA
TE 1000
40.9%
56.3%
100
10
Other: 2.8%
Figure3.Repeatcontentofmouse,human,andCaenorhabditisele-
ganseditingenrichedregions(EERs).Piechartsdepictpercentageof
total EER sequences that overlap RepeatMasker-annotated repeats
(mouse: mm10; human: hg19; C. elegans: ce10). Major classes of
repetitive elements (>2% of total EER sequence) are labeled, and
classes comprising <2% are grouped as “Other.” Nonrepetitive se-
quences did not overlap any sequences annotated as repetitive by
RepeatMasker. SINE, short interspersed nuclear element; LINE,
longinterspersednuclearelement;LTR,longterminalrepeat;DNA
TE,DNAtransposableelement.
ticed that after incubation in Xenopus cells, the dsRNA
migrated aberrantly on native gels (Bass and Weintraub
1987) and showed altered sensitivity to single-strand-spe-
cific ribonucleases (Rebagliati and Melton 1987). Thus,
ADARs were initially called an unwinding activity, and
this activity was also observed in extracts of mammalian
)MKPF(
noisserpxE
1
0.1
0.01
llA sGAE llA sGAE llA sGAE llA sGAE
MappingthedsRNAWorld
**** **** ****
Stage: Embryo E. larval L. larval Y. adult
Figure4.ExpressionofCaenorhabditiseleganseditingenrichedre-
gion (EER)-associated genes (EAGs). Tukey box plot shows gene
expression,infragmentsperkilobase∗millionreads(FPKM),forall
expressedgenesorEAGsinRNA-seqoffourC.elegansdevelopmen- talstages:embryo,earlylarval(E.larval;L1–L2),latelarval(L.larval;
L3–L4),andyoungadult(Y.adult)stages.∗∗∗∗,P<0.0001,Mann–
WhitneyU-test.
CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352 5
Bass1999),aswellastherealizationthatADARsconstituted
–0.1
afamilyofenzymes(Melcheretal.1996),withsomeorgan-
ismshavingasingleADARandothersseveral(Bass2002).
–0.2
AnastoundingfindingwasthatlethalityofADAR2 −/−
mice could be rescued by replacing the unedited GRIA2
allelewiththeeditedone(Higuchietal.2000).Thesestud-
–0.3
iesforeshadowedthemanyimportantADAReditingevents
that occur in the nervous system of vertebrates and inver-
tebrates(MorseandBass1999;Rosenthal2015;Behmand
Ohman 2016; Deffit and Hundley 2016; Nishikura 2016)
andfocusedthefieldonfindingandcharacterizingADAR
editing in codons. The nonselective editing observed in
earlystudieswasputasidebymost.
SangersequencingofclonedcDNAswasinstrumental
in the identification of the first ADARediting sites. How-
ever,thismethodrequiredsequencingcDNAsonacase-by-
casebasisandwasnotamenabletothesystematicdiscovery
ofADAReditingsites.Towardthisgoal,amethodforino-
sine-specificcleavage(MorseandBass1997)wasdeveloped
and,whencoupledwithdifferentialdisplay,allowedthefirst
unbiasedidentificationofA-to-IeditedRNAsinC.elegans
(Morse and Bass 1999) and human brain (Morse et al.
2002).Theseeffortswerefacilitatedbylarge-scalegenome
sequencingprojects(Berksetal.1995;C.elegansSequenc-
A-to-I editing shows T-to-C changes in the first-strand ingConsortium1998;Landeretal.2001;Venteretal.2001)
cDNA, revealed as A-to-G changes in the second-strand that allowed identified transcripts to be cross-referenced
cDNA. Initial examples of in vivo ADAR editing showed with genomic sequences and specific genes. At the time,
numerouseditingeventsinindividual,clonedcDNAs(Bass the field assumed that the primary role of ADARs was to
1997),reiteratingthenonselectivehypereditingobservedin edit codons, and it was perplexing that this “systematic”
theperfectlypaireddsRNAsusedinthefirstinvitrostudies. method identified inosine only in noncoding sequences,
′
IntheseearlydaysofADARresearch,itwashardtoimag- largely introns and 3 UTRs, in which base-pairing often
ineanimportantbiologicalactivityforADARs. occurred between repetitive elements. This hinted that
Thisallchangedwiththeobservationofeditingevents ADAR editing in codons, or mRNA recoding, is a rare
in specific codons. The first reported example involved a event,somethingnowknowntobetrueforstudiedorgan-
specific codon in an α‐amino‐3‐hydroxy‐5‐methylisoxa- isms, excepting some coleoid cephalopods (Liscovitch-
zole‐4‐propionicacid(AMPA)glutamatereceptor,GRIA2 Braueretal.2017).Althoughinosine-specificcleavagepro-
(previously called GluR-B) (Sommer et al. 1991). cDNA vided a systematic way to find editing sites, the method
analyses indicated a specific amino acid was encoded as a required isolation of differentially cleaved bands from a
glutamine or arginine, and the arginine was known to be gel and was limited compared with the high-throughput
importantforiontransportpropertiesofchannelsassem- protocols used today. Similar limitations applied to other
bled with glutamate receptors. Researchers were puzzled methodsdevelopedtoidentifyADAReditingsiteswithout
when only a single gene could be identified for GRIA2, Sanger sequencing.These included approachesto identify
and its genomic sequence specified a glutamine codon. recodingsitesbyimmunoprecipitatingADAR2anddetect-
TheinvestigatorshypothesizedthatADAReditingchanged ing enriched transcripts by microarray analysis (Ohlson
aglutamine(Q)codontoanarginine(R)codon(Q/Red- etal.2005)andmethodsusinghigh-resolutionmeltanaly-
itingsite).Indeed,subsequentstudiesrevealedcomplemen- sis, denaturing HPLC, or allele-specific polymerase chain
tary sequence in the intron adjacent to the Q/R site that reaction (PCR) to detect and measure editing in cDNA
could fold back to encompass the edited codon (Higuchi amplicons(Galloetal.2002;Chateigner-BoutinandSmall
et al. 1993; Egebjerg et al. 1994). The predicted structure 2007;Chenetal.2008).
wasdisruptedbymismatchesandloops,andtheideathat The first attempt to identify inosine-containing tran-
suchdisruptionscouldpromotemoreselectiveeditingbe- scripts focused on C. elegans, because at the time it had
gantoemerge(Hurstetal.1995;Bass1997;Lehmannand themostcompletegenomesequence(C.elegansSequenc-
tn/GΔ
nortni
egarevA
)tn*lom/lack(
D.P.ReichandB.L.Bass
Chromosome III
–0.4 C. elegans
C. briggsae
–0.5
–0.5 0.0 0.5
Relative position
Figure5. PredictedintronstructurealongchromosomeIIIfortwo
nematode species. Length-normalized UNAFold-predicted folding
freeenergiesareplottedbyrelativepositiononchromosomeIIIof
Caenorhabditis elegans (blue) and Caenorhabditis briggsae (red).
Trends observed on chromosome III are representative of all
C.elegansautosomes.AverageintronicΔG/ntvalueswerecalculated
bysplittingchromosomesinto1000equal-lengthsegmentsandav-
eragingΔG/ntvaluesofintronsineachsegment.LowerΔG/ntvalues
indicate presence of more stable intronic structures. ΔG, predicted
foldingfreeenergy;nt,nucleotide.
6 CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352
MappingthedsRNAWorld
ing Consortium 1998). As sequencing of other genomes A-to-G differences between RNA-derived cDNA libraries
progressed (Adams et al. 2000; Landeret al. 2001; Venter andmatchedgenomicsequences.Firstandforemost,find-
et al. 2001; Mouse Genome Sequencing Consortium et al. ing RNA editing sites requires that edited RNAs are well
2002),comparativeanalysesbecamefeasible.Phylogenetic representedamongthetranscriptssequencedinanexper-
comparisons of glutamate receptor pre-mRNAs from six iment. Samples dominated by abundant transcripts like
vertebratesrevealedsurprisingconservationofexonicand ribosomalRNA(rRNA)willnothavesufficientsequencing
intronic sequences around the R/G recoding site, which coverageofeditedtranscriptstoreliablydistinguishediting
results in the conversion of an arginine (R) to a glycine sitesfromsequencingerrorsandgenomicvariants.Equally
(G)(AruscavageandBass2000).Similarregionsofstrong importantistheapproachusedtoalignsequencingreadsto
conservationbetweendifferentDrosophilaspeciesallowed the genome. By definition, edited reads will not perfectly
identificationof16geneseditedincodingsequences(Hoo- align to the genome, and mismatch parameters for align-
pengardneretal.2003),andcomparativeanalysesinmam- ment and read filtering must be carefully chosen to avoid
mals identified a handful of previously unrecognized discardingeditedtranscripts(Leeetal.2013).
editingsites(Clutterbucketal.2005;Levanonetal.2005). Editingsitesthatoccuratlowfrequencyareparticularly
Aroundthistime,largenumbersofcDNAsandcDNA problematic.Asitenaturallyeditedinonly10%ofcellular
fragments, many as expressed sequence tags (ESTs), were transcripts on averagewill appearas G in onlyone of ten
sequenced and mapped to genomic DNA sequences (Bo- reads. Increasing the number of sequencing reads will in-
guskietal.1993;Kikunoetal.2002;Otaetal.2004).Several creasetheaveragenumberoftimesaparticularnucleotideis
research groups recognized that cDNA and EST libraries, represented, or the depth of coverage (Sims et al. 2014).
whencomparedwithgenomicsequences,couldbeusedto Given a site edited at frequency f, one can calculate the
identifyediting-dependent RNA–DNA differences (Atha- numberofreads,n,thatprovideprobabilityPofobserving
nasiadisetal.2004;Blowetal.2004;Kimetal.2004;Leva- editingatthatsiteusingtheformula
non et al. 2004) and found tens of thousands of unique
editingsitesinhumantranscripts.Thesestudiesindicated n=log (1−P).
1−f
thatA-to-Gconversions,themostabundantclassofRNA–
DNA mismatches, were abundant in repetitive sequences,
Forinstance,oneneedsapproximately18readstohave
especially Alu retroelements,and displayed nearest neigh-
a90%chanceofobservingeditingatasiteeditedin12%of
borpreferencessimilartothoseobservedforADARinvitro
endogenoustranscripts,whereascoverageofapproximately
(Polson and Bass 1994; Lehmann and Bass 2000). Ap- fivereadsonlyprovidesan∼50%chance.Inpractice,costs
proachestoalignandcomparelibrariesofcDNAsequences
ofhigh-throughputsequencingarebalancedwithcoverage
provedpowerful,butultimatelywerelimitedbythenumber
demands. Regardless, coverage of edited transcripts will
of cDNAs and ESTs available. As described below, using
increasebyremovingabundantuneditedtranscriptsorby
modernsequencingtechnology,onecansequencemillions biochemically enriching for edited RNAs, without signifi-
of cDNAs per sample and detect editing using rapid and
cant increase in costs. Thus, this is standard protocol in
robustpipelines.
analysesofeditedtranscripts.
5 FINDINGEDITEDRNAsINHIGH-THROUGHPUT 5.1 EnrichingforEditedTranscripts
DATASETS
High-abundancetranscripts,especiallyrRNAs,presentthe
Although early cDNA and EST sequencing projects com- majorobstacletoobtainingdeepcoverageofeditedRNAs.
piledtenstohundreds ofthousandsof cellularsequences, Because rRNA makes up 80%–90% of most total RNA
high-throughput technologies like RNA-seq rapidly pro- samples (O’Neil et al. 2013), its inclusion in sequencing
ducetenstohundredsofmillionsofsequencespersample librariessubstantiallyreducesthefractionofRNA-seqreads
(Wangetal.2009).RNA-seqfacilitatesgenome-widepro- that contain editing information. Typically, rRNA is re-
filingofRNAexpressionandeditingpatternsandcaneasily moved from an RNA sample before library preparation,
beappliedtodifferentorganisms,celltypes,andconditions, either by selecting polyadenylated RNAs with oligo(dT)
forcomparativeanalyses.Severalpreviousreviewsprovide ordepletingrRNAswithbead-conjugatedantisenseoligos
useful information for detecting edited RNAs with high- (ribo-minus) (O’Neil et al. 2013; Zhao et al. 2014). Al-
throughput protocols (Eisenberg et al. 2010; Ramaswami though oligo(dT) capture removes rRNA, it also depletes
andLi2016). transcriptsthat lack a poly(A) tail, including nascent pre-
Like Sanger sequencing and cDNA/EST approaches, mRNAs that have not yet acquired a poly(A) tail, spliced
RNA-seq is used to identify editing sites by searching for intronlariats,andabundantpolymeraseIIItranscriptslike
CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352 7
D.P.ReichandB.L.Bass
tRNAs.Ribo-minusprotocols,althoughtheyremoverRNA mutant showed increased editing in ∼40% of well-repre-
less efficiently than oligo(dT) capture, do not deplete in- sented edited RNAs. In mammalian cells, reduction in
tronic and intergenic sequences and otherabundant non- N6-methyladenosine RNA modification by METTL3 or
coding RNAs (Cui et al. 2010). If the goal is to look for METTL14 knockdown likewise results in elevated A-to-I
editing sites in mature mRNAs, poly(A) selection is an editing at many sites (Xiang et al. 2018). Performing
excellentmethod.However,ifthegoalisacomprehensive RNA-seqonmutantswithelevatededitingwillenablede-
determination of editing sites, including those that fre- terminationofamorecomprehensivedsRNAome.Howev-
quently occur in introns (Table 1) (Whipple et al. 2015; er, if the goal is to determine biologically relevant editing
Zhaoetal.2015;BlangoandBass2016),ribo-minustreat- sites,itisimportanttorememberthatsuchgeneticpertur-
menttoremoverRNAispreferable. bations will identifyediting sitesthat may not exist in the
In additiontoincreasingthecomplexityofRNAsam- wild-typecontext.
plesbyremovingabundant,uneditedtranscripts,biochem- A-to-IeditingonlyoccursindsRNAstructures,which
icalapproachescanbeusedtoenrichforADARsubstrates may impede efficient reverse transcription. The use of
inRNA-seqlibraries.Animmunoprecipitationapproachto thermostable reverse transcriptases at high temperatures,
enrichfordsRNAwiththeJ2anti-dsRNAantibody,raised or addition of organic solvents like dimethylsulfoxide
against L-dsRNA, from a “killer” virus of Saccharomyces (DMSO),canrelaxsecondarystructuretopromotecDNA
cerevisiae(Schönbornetal.1991),hasbeenusedinstudies synthesis from long RNA duplexes (Yasukawa et al. 2010;
ofhumanDicer(Kanekoetal.2011),TDP-1,theC.elegans Mohr et al. 2013; Whipple et al. 2015; Nottingham et al.
ortholog of TDP-43 (Saldi et al. 2014), and in RNA-seq 2016).However,theseadaptationsareusuallyunnecessary,
approaches to map dsRNAs using ADAR editing sites because RNA fragmentation during library preparation
(Whipple et al. 2015; Blango and Bass 2016; Reich et al. reduces the length, and thus the stability, of base-paired
2018). Although this immunoprecipitation approach can regions, and further, dsRNAs containing many IU mis-
improvecoverageofdsRNAs,itsreportedefficiencyismod- matches are easier to reverse transcribewith conventional
est. In C. elegans, edited sequences were enriched about enzymes(Whippleetal.2015).Importantly,libraryprepa-
twofold (Reich et al. 2018), and transposon sequences, ration protocols should incorporate high-fidelity enzymes
whichoftenforminvertedrepeatstructures,wereenriched to maintain low error rates during cDNA synthesis (Lee
four-orfivefold(Saldietal.2014).Whenappliedtomouse etal.2013).
RNAs, J2 immunoprecipitation improved the number of
EERs detected byat most 1.8-fold, suggesting it may have
limitedbenefitincertainsystems(BlangoandBass2016). 5.2 SequencingandAlignmentProtocols
OtherresearchgroupshaveimmunoprecipitatedADARsto Most RNA editing studies use Illumina sequencing plat-
isolate bound RNAs and compare substrate specificity of forms because of their ability to sequence relatively long
differentADARisoformsandparalogs(Wangetal.2013). readsatdeepcoverage,providingaround200millionreads
Although not all ADAR-bound RNAs were edited, these perlane(Diromaetal.2017).Thehighsequenceinforma-
groups observed edited RNAs enriched among ADAR- tion content of long reads (>100nt) enables accurate
bound transcripts and in one case identified thousands of mapping to a reference genome, especially across splice
noveleditingsites(Wangetal.2013).Still,immunoprecip- junctions and in repetitive regions. Paired-end protocols
itation methods run risks. For example, it is unknown effectively double the information per read bysequencing
′ ′
whether hyperedited transcripts with numerous IU mis- fromboth5 and3 ends(Chhangawalaetal.2015).Strand-
matchesareefficientlyimmunoprecipitatedwiththeJ2an- ed library construction protocols further refine mapping
tibody.Nonetheless,althoughnotessentialtodefineedited information and distinguish between A-to-G and T-to-C
sequences, enrichment protocols can improve coverage of conversions (Mills et al. 2013). We typically perform
editedtranscripts. stranded, paired-end RNA-seq with >100-nt reads fored-
Sequencing RNA from genetic mutantsthat eitherac- iting detection studies, because paired-end reads with
cumulatedsRNAorlackproteinsthatcompetewithADARs ∼200-nttotalsequencerarelyaligntomorethanonegeno-
for binding dsRNA can also increase coverage of edited miclocation,eveniftheyincluderepetitivesequences.
sequences and/or elevate editing levels. Several C. elegans Early studies used cloned cDNAs to determine the
studiesusedmutantstrains,includingdcr-1(mg375),which number of editing sites per transcript and defined tran-
contains a mutation in the helicase domain of C. elegans scriptswithA-to-Gchangesat>10%ofadenosinesasnon-
Dicer that results in deficient endo-siRNA processing selectively edited or hyperedited (Bass 1997). Although a
(Whippleetal.2015),andtdp-1(ok803),whichaccumulates numberof viral transcripts were found to be hyperedited,
excesscellulardsRNA(Saldietal.2014).Indeed,thetdp-1 with a fewexceptions (Morse and Bass 1999; Morse et al.
8 CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352
MappingthedsRNAWorld
2002), endogenous transcripts showed editing at <10% of Hongetal.2013).Inonecomparison,GNUMAPidentified
theadenosinesinasinglebase-pairedregion.Information more editing sites and editing clusters than the “editing
about the number of editing sites in a single transcript is unaware” aligner, Novoalign, which aligned 100-nt reads
oftenlimitedwhenusingIlluminaRNA-seqprotocols,be- withuptofourmismatches(Whippleetal.2015).Applying
cause individual reads are comparatively short. Compila- asimilar“editingaware”principle,severalresearchgroups
tionofallreadsforagiventranscriptindicatesthenumber used a “three-base” approach, so-called because it takes
of potential editing sites, but not the number of sites that highlyedited reads unmapped by conventional alignment
canoccurinasingletranscript.High-throughputprotocols andrealignsthemafterconvertingallAstoGsinreadand
suited for sequencing longer reads, such as the 300-nt referencegenomesequences,thusrestrictingthegenometo
paired-end reads provided by Illumina MiSeq platforms, three bases: G, C, and T (Wu et al. 2011; St Laurent et al.
havebeenusedtodeterminehowmanyeditingeventsoccur 2013;Porathetal.2014;Zhaoetal.2015).Three-basemeth-
in a single transcript (Wheeler et al. 2015). Such studies odsinvolveadditionalalignmentandcomputationalsteps
provideinformationabouthoweditingatonepositionin- and risk mapping reads that contain G-to-A mismatches
fluenceseditingatothersites. (Porath et al. 2014). Thus, editing-aware algorithms (e.g.,
Afterlibraryconstructionandsequencing,qualitycon- GNUMAP)thataccuratelymaphighlyeditedsequencesin
trolsoftwaresuchasFastQC(seebioinformatics.babraham asinglealignmentstepareusuallypreferable.
.ac.uk/projects/fastqc/) assess base quality and sequence
complexity in the resulting RNA-seq reads. Preprocessing
5.3 ToolsandApproachestoIdentifyEditingSites
programslikeCutadapt(Martin2011)trimreadstoremove
adaptersequences,poly(A)tails,andlow-qualitybases,af- A growing number of bioinformatics tools and pipelines
ter which reads are aligned to a reference genome. Align- arepubliclyavailablefordetectingADAReditingsites(Por-
ment algorithms differ in run time and accuracy (Ruffalo athetal.2014;Whippleetal.2015;BlangoandBass2016;
etal.2011;Borozanetal.2013).Manyalignersdetectexon– Deffit and Hundley 2016; Diroma et al. 2017). Editing
intron junctionsto map spliced RNA-seq reads, although detection pipelines use variant calling to identify A-to-G
alignerswithoutthisfeaturemapsplicedreadseffectivelyif conversions in RNA-seq reads, and then assess if A-to-G
provided a table of splice junctions (Borozan et al. 2013; changes represent true editing events. Assessment ap-
Diromaetal.2017). proaches aim to distinguish editing sites from genetic
Two ways are commonly used to align reads so as to polymorphisms and sequencing errors, typically through
avoid discarding those with ADAR editing sites. The first statistical analyses or filtering based on location and fre-
usesstandardalignmentalgorithms,butincreasesthenum- quency of editing (Porath et al. 2014; Deffit and Hundley
ber of mismatches allowed in a single read, whereas the 2016;Wangetal.2016;Diromaetal.2017;Johnetal.2017).
seconduses“editingaware”alignmentalgorithmstoalign Our laboratory uses applications in the USeq (see github
cDNA sequences with either an A or G to a genomic .com/HuntsmanCancerInstitute/USeq)andSAMtools(see
A.Usingastandardaligner,onemustallowformismatched github.com/samtools/) sequencing analysis suitesto iden-
bases to map edited reads, because the edited sequence tifyedited sites and define editing clusters (Whipple et al.
varies from the genomic sequence. The optimal number 2015; Blango and Bass 2016; Reich et al. 2018). In addi-
of mismatches allowed depends on read length, because a tion to variant-calling (SAMtools mpileup) and editing-
100-nt read with four possible mismatches will generally detectionfunctions(USeqRNAEditingPileupParser),these
align to fewer locations than a 50-nt read with the same analysis suites provide useful, intuitive programs to work
number of mismatches. Because most C. elegans edited withsequencingdatasetsandcompareeditingsitestoother
RNAs have four or fewer editing events per molecule genomicfeatures.Otherpipelinesarespecificallyfordetect-
(Wheeler et al. 2015), we permit four mismatches when ingRNAediting,andarecentreviewevaluatedfiveofthese
using a standard aligner to map 100-nt paired-end reads for accuracy and sensitivity (Diroma et al. 2017). Results
from C. elegans. For other organisms, different mismatch variedbasedonalignmentalgorithmused,butoverallthe
parameters should be tested to find those that accurately RNAEditor, JACUSA, and REDItools pipelines predicted
map edited reads while minimizing mapping to multiple the most editing sites, whereas GIREMI predicted fewer
locations. sites but with a lower false discovery rate. All-inclusive
The second approach to mapping ADAR-edited se- programs like RNAEditorand RES-Scannerare useful for
quences relies on alignment programs like GSNAP and those with little experience to quickly and easily identify
GNUMAP that include “editing aware” modes. These editing sites, as they incorporate alignment, detection,
aligners are particularly adept at mapping highly edited andfilteringstepstodefineeditingsitesfromrawsequenc-
sequences (Clement et al. 2010; Wu and Nacu 2010; ingfiles(Wangetal.2016;Johnetal.2017).However,for
CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352 9
D.P.ReichandB.L.Bass
determinationofdsRNAomes,weprefertheEERpipeline matched genomic sequence (Ramaswami et al. 2013; Zhu
(describedbelow),whichdefineseditingclusterstoidentify et al. 2013; Zhang and Xiao 2015). However, without an
longdsRNAs(Whippleetal.2015;BlangoandBass2016; available reference sequence to align reads, DNA-seq is
Reichetal.2018). important to determine RNA–DNA differences (Alon
InadditiontoRNA-seq-basedapproachesthatidentify etal.2015).
editing through A-to-G changes, high-throughput se- Filtering out sequencing errors is critical for accurate
quencingcanbeappliedtoinosine-specificdetectionmeth- editingdetection.HigherIlluminaerrorratesatreadends,
ods.Inosine-specificcleavagewithRNaseT1,anearlytool andmismatchesintroducedbyrandomhexamerpriming,
for editing detection (Morse and Bass 1999), was paired leadtoclusteringofsequencingerrorsattheendsofreads
′ ′
withRNA-seqtoidentify665editingsitesinmousebrain, (Minocheetal.2011;vanGurpetal.2013).Thus,5 and3
many of which were novel (Cattenoz et al. 2013). Inosine readendsaretypicallytrimmedbeforevariantcallingeither
reactivitywithacrylonitrileunderliesanotherchemicalde- byafixedamountoraccordingtomismatchdensity(Bazak
tectionmethod,termedinosinechemicalerasing(ICE)(Sa- etal.2014;Whippleetal.2015;Zhaoetal.2015;Wangetal.
kurai et al. 2010). High-throughput sequencing improves 2016). Reads with multiple non-A-to-G mismatches are
the scale and sensitivity of these methods (Cattenoz et al. also typically filtered out, because additional mismatches
2013;Sakuraietal.2014;Suzukietal.2015),whichdistin- are an indication of poor sequence quality or inaccurate
guishinosinefromA-to-Gchangescausedbygeneticpoly- mapping(BlangoandBass2016;Deffitetal.2017).Repet-
morphismsorsequencingerrors.However,thesemethods itivegenomicregions,inparticular,riskissuesofmismap-
rely on chemical conversion methods that are not 100% ping(Eisenberg2012).Althoughreadsthatmaptomultiple
efficient; the recommended conditions for ICE convert repetitiveregionscanberemoved,editingismostabundant
only 80%–90% of inosines at the highly edited GRIA2 in repetitive sequences (Bazak et al. 2014; Whipple et al.
Q/Rsite(Suzukietal.2015).Further,becauseinosine-spe- 2015; Blango and Bass 2016; Porath et al. 2017). Filter-
cificdetectionmethodsrequirecomplexanalysispipelines ing out repetitively mapped reads removes sequences car-
and suffer from the same read coverage issues as conven- rying true editing sites. Sequencing protocolsthat provide
tional editing detection pipelines (Cattenoz et al. 2013; longer reads facilitate more accurate mapping, including
Sakuraietal.2014;Suzukietal.2015),theydonotprovide within repetitive sequences, so these protocols reduce the
astrongadvantageoverotherapproaches. number of reads needed to be filtered due to ambiguous
alignment.Evenwithlongreads,werecommendincluding
repetitivelymappedreads,astheyarerichsourcesofediting
5.4 ExcludingFalsePositives
information.
EffectiveeditingpipelinesmustdistinguishtrueRNAedit- Several approaches can be used to validate that align-
ingeventsfromediting-independentmismatchesthatarise mentanddetectionparametersareappropriateforediting
because of single-nucleotide polymorphisms (SNPs) and discovery.Themoststraightforwardistochoosecandidate
errorsinsequencingandalignment.ControllingforSNPs edited regions for editing validation by another method,
requiresaccuratelyidentifyinggeneticvariantsandremov- typically cDNA amplification and Sanger sequencing (Li
ingthemfromanalysis.SequencinggenomicDNAfromthe etal.2009).Thisapproachisaccurateandsensitive,butit
same samples used for RNA-seq provides a definitive so- can be time-consuming to test many candidates. We rec-
lution(PicardiandPesole2013;Wangetal.2016)bypro- ommendinitiallyinterrogatingdatasetsforthepresenceof
vidingamoreaccurategenomicsequencethanapublished knownADARtargets.Bycomparingknowneditingsitesto
reference. Alternatively, RNA-seq analyses of ADAR mu- experimentally determined patterns, one can identify and
tantstrainscanvalidatethatidentifiedA-to-Gconversions addresspotentialissuesinbioinformaticpipelines.Forin-
require ADAR (Bahn et al. 2012; Zhao et al. 2015). Al- stance,theabsenceofeditingwithinwell-expressedADAR
though these approaches effectively control for genomic substrates might indicate that edited reads are being dis-
variation, they are expensive and resource-intensive, and cardedduringalignmentorfiltering.Publiclyavailableda-
SNPstypically make up atinyfraction of A-to-G changes tabases, including DARNED, RADAR, and REDIportal,
identified(<0.1%inZhaoetal.2015).Acheapalternativeis provide curated information on RNA editing sites, incor-
tosimplyremoveSNPsrecordedinpublicvariantdatabases poratingannotation,editinglevel,andtissue-specificedit-
frompotentialeditingsites(Ramaswamietal.2013;Bazak inginformation(Kiranetal.2013;RamaswamiandLi2014;
et al. 2014; Whipple et al. 2015; Blango and Bass 2016; Picardietal.2017).However,thesedatabasesdonotalways
Diromaetal.2017;Tanetal.2017).Severalresearchgroups include up-to-date information; whereas DARNED and
haveshownthattrueeditingsitescanbeaccuratelyidenti- RADAR only provide data for human, mouse, and Dro-
fiedusingonlyRNA-seqdata,withouttheneedforsample- sophila, REDIportal currently includes only humaninfor-
10 CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352
MappingthedsRNAWorld
mation(Kiranetal.2013;RamaswamiandLi2014;Picardi several dozen EERs in a genome browser to determine if
etal.2017).Withoutcurateddata,wehaveusedpublished singlestructuresaremergedwithoutalsomergingseparate
editingtargets(Morseetal.2002;HellwigandBass2008)to transcripts.Includingagapparameteroccasionallycauses
validateparametersfordetectingeditinginC.elegansdata closelyjuxtaposedindependentstructures(asineIF-2αpre-
sets(Whippleetal.2015).Oncethepipelineisconsidered mRNAinFig.1)tobemergedintooneEER;however,itis
optimal, it is standard practice to verify editing sites in a rarethatstructuresfromdifferentgenesaremerged(Whip-
subsetofnewlyidentifiedtargetsusingcDNAamplification pleetal.2015;BlangoandBass2016).
and Sanger sequencing, especially those chosen for more Once EERs are defined, additional methods are used
in-depthstudy. to validate that dsRNAs have been accurately deter-
mined(Whippleetal.2015;BlangoandBass2016).RNA
secondary structure prediction algorithms like UNAFold
5.5 DefiningEditingClustersandDetermining
(MarkhamandZuker2008)provideameasureofthether-
adsRNAome
modynamic stabilityof predicted EER structures. Length-
In highly base-paired dsRNAs, ADARs nonselectively de- matchedrandomregionsprovideacontroltoconfirmthat
aminatemanyadenosinestoinosine(Nishikura2010;Sam- predicted dsRNAs are more structured than expected by
uel2011;DeffitandHundley2016),resultinginclustersof chance.Length-matchedcontrolsetsshouldsampleprop-
A-to-Gchangesinsequencingreads.Definingeditingclus- ertiesofthetranscriptomethatmeetthesamecriteriaused
ters provides increased sensitivity to identify true editing todefinedsRNAs.Forinstance,ifthepipelinedictatesthat
events,becausesequencingerrorsor genomicvariantsare EERsaredefinedonlyinregionscoveredbymorethanfive
unlikely to result in clusters of a single variant (A-to-G) reads,controlregionsshouldberestrictedtothesameread
(Bazak et al. 2014; Zhao et al. 2015). Importantly, editing coveragethreshold.WeusetheBEDtools2(seegithub.com/
clusters also indicate the presence of long, highly base- arq5x/bedtools2) application shuffleBed to make length-
paired dsRNA (Fig. 1) and, when mapped on a genome- matchedcontrolregions,becauseitcanrandomlypermute
widescale,allowthedeterminationofadsRNAome(Fig.2). regions across the genome or within specified areas.
WehavedetermineddsRNAomesforspecificcelltypesof For edited sequences that do not have predicted duplex
human and mouse, as well as C. elegans (Whipple et al. structure, we use the BLAT sequence alignment tool to
2015;BlangoandBass2016). findcomplementarygenomicsequencesthatmayfacilitate
Our EER-detection pipeline uses a window-scanning intermolecular dsRNA formation (Whipple et al. 2015).
approach to find genomic regions covered by RNA-seq Similarapproachestodetectproximal(within10kb)com-
reads carrying clustered A-to-G changes (Whipple et al. plementarysequenceswiththebl2seqalgorithmhavebeen
2015; Blango and Bass 2016; Reich et al. 2018). Genomic used in other editing cluster analyses (Porath et al. 2014;
regionswithsufficientreadcoverage(≥5reads)arescanned 2017).ExaminingnearestneighborpreferencesofEERed-
insmallwindows,typically50nt,toidentifywindowscon- itingsitesvalidatesthatsitesshowcharacteristicsofADAR
taining≥3siteswithA-to-Gchangesin>1%ofreads.We editing(Whippleetal.2015;BlangoandBass2016).
chosereadcoverageandeditingthresholdstooptimizethe
sensitivity of EER detection without markedly increasing
the false discovery rate. Alternative parameters could be 6 LOOKINGTOWARDTHEFUTURE
used to predict greater numbers of clusters, or to identify
6.1 DeterminingOtherdsRNAomes
clusterswithextremelylowfalse-positiverates.
Onceeditedwindowsaredetermined,overlappingwin- Todate,ADAReditingsiteshavebeendeterminedforap-
dows are merged, and then combined with other merged proximately 23 metazoan species (Liscovitch-Brauer et al.
windows separated by a predetermined “gap” distance to 2017;Porathetal.2017)and53humantissues(Tanetal.
definetheEER.Thegap parameterconnectscomplemen- 2017).Inallcases,editingshowssimilarproperties(Table
taryregionsofanintramoleculardsRNAthatmaybesep- 1). It predominates in noncoding sequences, particularly
′
aratedbyunedited,interveningsequences.Theoptimalgap introns and 3 UTRs (Whipple et al. 2015; Blango and
distancevariesbetweenorganisms.ForC.elegans,agapof1 Bass 2016; Liscovitch-Brauer et al. 2017; Porath et al.
kb merges complementary sequences of a single dsRNA 2017), and frequently occurs in mobile element–derived
without also combining dsRNAs from separate, indepen- repetitivesequencespredictedtoformstableintramolecu-
denttranscripts(Whippleetal.2015),whereasmouseand larstructures(Fig.3)(Bazaketal.2014;Whippleetal.2015;
human dsRNAomes require a longer 2.5-kb gap (Blango BlangoandBass2016;Porathetal.2017).
and Bass 2016). We typically determine optimal gap dis- In most cases, editing information from these studies
tance by testing several lengths and manually surveying has not been used to map structures and determine a
CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352 11
D.P.ReichandB.L.Bass
dsRNAome. Such analyses would be straightforward be- Selfishelementsthatintegrateintoagenomeovertime
cause existing data can simply be mined and analyzed canbecomerecognizedas“self,”sotheaboveideaisclosely
with available pipelines. EERs and editing sites can be tied withstudiesindicatingthat ADARsfunctiontomark
viewedinagenomebrowser,allowingresearcherstoeval- cellulardsRNAasself(Hartneretal.2009;Mannionetal.
uatetheirfavoritegenes.BEDfilesofexistingdsRNAomes 2014;Liddicoatetal.2015;Pestaletal.2015;Georgeetal.
(Whipple et al. 2015; Blango and Bass 2016; Reich et al. 2016; Reich et al. 2018). The simple idea is that ADARs,
2018)arefreelyavailableintheGeneExpressionOmnibus which are typically in the nucleus, target cellular dsRNA,
repository. whereasviruses,whichoftenreplicateinthecytoplasm,are
AnunansweredquestioniswhetheralllongdsRNAsare protectedfromdeamination.However,theactualsituation
edited. Most dsRNAomes were determined using ADAR is clearly more complicated. Some viruses replicate in the
editingsitesasaninvivosignatureofdsRNA,sodsRNAs nucleus,suchasHDV,whichuseseditingforregulatingits
without editing sites were not identified. Possibly, certain life cycle (Polson et al. 1996). The ADAR1 isoform most
dsRNAs are protected from ADAR editing by other closelyassociatedwithanimmuneresponse,ADAR1p150,
dsRBPs, and indeed, there are clear examples of dsRBPs isexpressedinresponsetointerferonandisfoundinboth
competingforthesamesubstrates(Warfetal.2012;Elbar- the nucleus and cytoplasm (Patterson and Samuel 1995).
baryetal.2013;Sakuraietal.2017).Inafewcases,cellular Mounting evidence indicates additional regulation during
dsRNAs were identified byothercriteria, including acces- viralinfection.ADAR1p110isdegradedinresponsetoin-
sibilitytonuclease(Lietal.2012),chemicalprobes(Lucks terferon (Li et al. 2016), whereas the timing of interferon
etal.2011),orinvivocross-linkingtodsRBPs(Rybak-Wolf induction of ADAR1p150 is balanced with induction of
etal.2014).About18%ofC.elegansEERs(Whippleetal. MDA5 and other proteins that mediate the mammalian
2015)overlap9972ssRNAnuclease-resistantsites(Lietal. immuneresponse(Ahmadetal.2018).Asdiscussedearlier,
2012), validating the double-stranded character of EERs. some viral transcripts are edited by ADARs (Pfaller et al.
NonoverlappingsitescouldincludedsRNAthatisprotect- 2015), and ADARs can have both proviral and antiviral
edfromADARediting,butthelatterstudywasnotfocused effects (Samuel 2011). Repurposing ADARs as antiviral
onlongdsRNAs,andmanynonoverlappingsitesareshort factorsemphasizestheirrolesininnateimmunity.Indeed,
dsRNAregionsburiedintertiarystructurethatareinacces- ADAR1 shows evidence ofpositive selection,suggesting it
sible to ADARs. About 26% of human EER-associated has adapted through genetic conflict with viruses (Forni
genes overlap DICER-bound human genes (Rybak-Wolf etal.2015).
et al. 2014; Blango and Bass 2016), consistent with the ADARslikelyarose,andcontinuetofunction,forthese
idea that dsRBPs compete for dsRNA structures. These global roles, but have also been co-opted for additional
twostudieswereperformedindifferentcelltypes,soagain, purposes, such as mRNA recoding (Higuchi et al. 2000;
furtheranalysesarerequiredtoevaluatewhethernonover- JepsonandReenan2009;GarrettandRosenthal2012;Lis-
lappingsitesaredsRNAsthatareprotectedfromediting.In covitch-Brauer et al. 2017), creating or destroying splice
future studies,itwillbeinterestingtoobtaindefinitivein- sites or altering splicing regulatory sequences (Rueter
formation about competition between dsRBPs and deter- et al. 1999; Solomon et al. 2013). A key issue in future
mineifcompetitionisaffectedbydsRBPtissue-specificity, studieswillbetodefinitivelyconnectobservedphenotypes
abundance,orintracellularlocalization. with specific editing events. In C. elegans lacking ADARs,
most unedited dsRNAs, rather than a small subset, are
processed into siRNAs by antiviral RNAi machinery
6.2 WhatIstheFunctionofthedsRNAome? (Reich et al. 2018). Similarly, in ADAR1-deficient human
ThedsRNAomesdeterminedso farindicatethatEERsdo cells, MDA5 oligomerizes on hundreds of inverted-repeat
not show a predilection for the type of gene they inhabit; Alu elements and triggers downstream immune signaling
theyaretypicallyenrichedingenesexpectedtobeexpressed (Ahmadetal.2018).However,inC.elegansandmammals,
intheparticularcelltypeorconditionbeingstudied(Blan- it is unclear if all, or only some, dsRNAs are relevant to
go and Bass 2016). Is the dsRNAome just a vestige of an mutantphenotypes.TheearlylethalityofADAR2
−/−
mu-
ongoingbattlewithmobileelements?Silencingmobileel- tant mice and chemotaxis defects of adr-1;adr-2 mutant
ementexpressionisessentialforviability(FriedliandTrono C. elegans are largely ascribed to editing of single targets
2015), and studies in C. elegans (Reich et al. 2018) and (Higuchi et al. 2000; Deffit et al. 2017). Understanding if
D. melanogaster (Savva et al. 2013) are consistent with the same applies to immune-relevant ADAR-dependent
the idea that ADARs exist to allow expression of mRNAs pathologiescouldallowpotentialtreatmentstospecifically
that contain repetitive elements and otherwise would be targetrelevantsubstrateswithoutdisruptingglobalADAR
silenced. functions.
12 CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352
MappingthedsRNAWorld
REFERENCES Chateigner-BoutinA-L,SmallI.2007.Arapidhigh-throughputmethod
forthedetectionandquantificationofRNAeditingbasedonhigh-
AdamsMD,CelnikerSE,HoltRA,EvansCA,GocayneJD,Amanatides resolutionmeltingofamplicons.NucleicAcidsRes35:e114.
PG,SchererSE,LiPW,HoskinsRA,GalleRF,etal.2000.Thegenome ChenY-C,KaoS-C,ChouH-C,LinW-H,WongF-H,ChowW-Y.2008.
sequenceofDrosophilamelanogaster.Science287:2185–2195. Areal-timePCRmethodforthequantitativeanalysisofRNAeditingat
AhmadS,MuX,YangF,GreenwaldE,ParkJW,JacobE,ZhangC-Z,Hur specificsites.AnalBiochem375:46–52.
S.2018.Breachingself-tolerancetoAluduplexRNAunderliesMDA5- ChhangawalaS,RudyG,MasonCE,RosenfeldJA.2015.Theimpactof
mediatedinflammation.Cell172:797–810.e13. read length on quantification of differentially expressed genes and
Ahringer J, Gasser SM. 2018. Repressive chromatin in Caenorhabditis
splicejunctiondetection.GenomeBiol16:131.
elegans:Establishment,composition,andfunction.Genetics208:491– ClementNL,SnellQ,ClementMJ,HollenhorstPC,PurwarJ,GravesBJ,
511. CairnsBR,JohnsonWE.2010.TheGNUMAPalgorithm:Unbiased
AlonS,GarrettSC,LevanonEY,OlsonS,GraveleyBR,RosenthalJJC, probabilistic mapping of oligonucleotides from next-generation se-
EisenbergE.2015.Themajorityoftranscriptsinthesquidnervous
quencing.Bioinformatics26:38–45.
systemareextensivelyrecodedbyA-to-IRNAediting.eLife4:e05198. ClutterbuckDR,LeroyA,O’ConnellMA,SempleCAM.2005.Abioin-
AruscavagePJ,BassBL.2000.Aphylogeneticanalysisrevealsanunusual formaticscreenfornovelA-IRNAeditingsitesrevealsrecodingediting
sequenceconservationwithinintronsinvolvedinRNAediting.RNA6: inBC10.Bioinformatics21:2590–2595.
257–269. CrowlJT,GrayEE,PestalK,VolkmanHE,StetsonDB.2017.Intracellular
AthanasiadisA,RichA,MaasS.2004.WidespreadA-to-IRNAeditingof
nucleicaciddetectioninautoimmunity.AnnuRevImmunol35:313–
Alu-containing mRNAs in the human transcriptome. PLoS Biol 2: 336.
e391. CuiP,LinQ,DingF,XinC,GongW,ZhangL,GengJ,ZhangB,YuX,
BahnJH,LeeJ-H,LiG,GreerC,PengG,XiaoX.2012.Accurateiden- YangJ,etal.2010.Acomparisonbetweenribo-minusRNA-sequenc-
tificationofA-to-IRNAeditinginhumanbytranscriptomesequenc- ingandpolyA-selectedRNA-sequencing.Genomics96:259–265.
ing.GenomeRes22:142–150. DaugaardI,HansenTB.2017.BiogenesisandfunctionofAgo-associated
Bajad P, Jantsch MF, Keegan L, O’Connell M. 2017. A to I editing in
RNAs.TrendsGenet33:208–219.
diseaseisnotfakenews.RNABiol14:1223–1231. DeffitSN,HundleyHA.2016.Toeditornottoedit:RegulationofADAR
editingspecificityandefficiency.WileyInterdiscipRevRNA7:113–
BassBL.1997.RNAeditingandhypermutationbyadenosinedeamina-
tion.TrendsBiochemSci22:157–162. 127.
DeffitSN,YeeBA,ManningAC,RajendrenS,VadlamaniP,WheelerEC,
BassBL.2002.RNAeditingbyadenosinedeaminasesthatactonRNA.
AnnuRevBiochem71:817–846. Domissy A, Washburn MC, Yeo GW, Hundley HA. 2017. The C.
elegansneuraleditomerevealsanADARtargetmRNArequiredfor
Bas
u
s
n
B
w
L
in
,
d
W
s
e
R
in
N
t
A
rau
d
b
up
H
le
.
x
1
e
9
s.
8
C
7.
el
A
l4
d
8
e
:
v
6
e
0
lo
7
p
–
m
61
e
3
n
.
tallyregulatedactivitythat properchemotaxis.eLife6:e28625.
DiromaMA,CiacciaL,PesoleG,PicardiE.2017.Elucidatingtheedi-
BassBL,WeintraubH.1988.Anunwindingactivitythatcovalentlymod-
ifiesitsdouble-strandedRNAsubstrate.Cell55:1089–1098. tome:BioinformaticsapproachesforRNAeditingdetection.BriefBio-
informdoi:10.1093/bib/bbx129.
BassBL,WeintraubH,CattaneoR,BilleterMA.1989.Biasedhypermu-
Egebjerg J, Kukekov V, Heinemann SF. 1994. Intron sequence directs
tationofviralRNAgenomescouldbeduetounwinding/modification
RNA editing of the glutamate receptor subunit GluR2 coding se-
ofdouble-strandedRNA.Cell56:331.
quence.ProcNatlAcadSci91:10270–10274.
BassBL,NishikuraK,KellerW,SeeburgPH,EmesonRB,O’ConnellMA,
Ehrenfeld E, Hunt T. 1971. Double-stranded poliovirus RNA inhibits
SamuelCE,HerbertA.1997.Astandardizednomenclatureforaden-
initiationofproteinsynthesisbyreticulocytelysates.ProcNatlAcad
osinedeaminasesthatactonRNA.RNA3:947–949.
Sci68:1075–1078.
BazakL,HavivA,BarakM,Jacob-HirschJ,DengP,ZhangR,IsaacsFJ,
EigenbrodT,KellerP,KaiserS,RimbachK,DalpkeAH,HelmM.2015.
RechaviG,LiJB,EisenbergE,etal.2014.A-to-IRNAeditingoccursat Recognition of specified RNA modifications by the innate immune
overahundredmilliongenomicsites,locatedinamajorityofhuman system.MethEnzymol560:73–89.
genes.GenomeRes24:365–376.
EisenbergE.2012.BioinformaticapproachesforidentificationofA-to-I
Behm M, Ohman M. 2016. RNA editing: A contributor to neuronal editingsites.CurrTopMicrobiolImmunol353:145–162.
dynamicsinthemammalianbrain.TrendsGenet32:165–175.
EisenbergE,LiJB,LevanonEY.2010.Sequencebasedidentificationof
Berks M,Mapping CEG,ConsortiumS. 1995. TheC.elegans genome RNAeditingsites.RNABiol7:248–252.
sequencingproject.GenomeRes5:99–104. ElbarbaryRA,LiW,TianB,MaquatLE.2013.STAU1binding3′UTR
BlangoMG,BassBL.2016.Identificationofthelong,editeddsRNAome
IRAluscomplementsnuclearretentiontoprotectcellsfromPKR-me-
ofLPS-stimulatedimmunecells.GenomeRes26:852–862. diatedtranslationalshutdown.GenesDev27:1495–1510.
BlowM,FutrealPA,WoosterR,StrattonMR.2004.AsurveyofRNA Forni D, Mozzi A, Pontremoli C, Vertemara J, Pozzoli U, Biasin M,
editinginhumanbrain.GenomeRes14:2379–2387.
Bresolin N, Clerici M, Cagliani R, Sironi M. 2015. Diverse selective
BoguskiMS,LoweTM,TolstoshevCM.1993.dbEST—Databasefor“ex-
regimes shape genetic diversityat ADAR genes and at theircoding
pressedsequencetags”.NatGenet4:332–333. targets.RNABiol12:149–161.
BorozanI,WattSN,FerrettiV.2013.Evaluationofalignmentalgorithms Friedli M, Trono D. 2015. The developmental control of transposable
for discoveryand identification of pathogens using RNA-Seq. PLoS elementsandtheevolutionofhigherspecies.AnnuRevCellDevBiol
ONE8:e76935. 31:429–451.
C.elegansSequencingConsortium.1998.Genomesequenceofthenem- GalloA,ThomsonE,BrindleJ,O’ConnellMA,KeeganLP.2002.Micro-
atode C. elegans: A platform for investigating biology. Science 282: processingeventsinmRNAsidentifiedbyDHPLCanalysis.Nucleic
2012–2018. AcidsRes30:3945–3953.
CattaneoR,SchmidA,EschleD,BaczkoK,MeulenterV,BilleterMA. GarrettS,RosenthalJJC.2012.RNAeditingunderliestemperatureadap-
1988. Biased hypermutation and other genetic changes in defective tationinK+channelsfrompolaroctopuses.Science335:848–851.
measlesvirusesinhumanbraininfections.Cell55:255–265. GeorgeCX,RamaswamiG,LiJB,SamuelCE.2016.Editingofcellular
CattenozPB,TaftRJ,WesthofE,MattickJS.2013.Transcriptome-wide self-RNAs by adenosine deaminase ADAR1 suppresses innate im-
identificationofA>IRNAeditingsitesbyinosinespecificcleavage. munestressresponses.JBiolChem291:6158–6168.
RNA19:257–270. GilbertW.1986.TheRNAworld.Nature319:618.
CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352 13
D.P.ReichandB.L.Bass
Grimwood J, Gordon LA, Olsen A, Terry A, Schmutz J, Lamerdin J, LeeJ-H,AngJK,XiaoX.2013.AnalysisanddesignofRNAsequencing
HellstenU,GoodsteinD,CouronneO,Tran-GyamfiM,etal.2004. experimentsforidentifyingRNAeditingandothersingle-nucleotide
TheDNAsequenceandbiologyofhumanchromosome19.Nature variants.RNA19:725–732.
428:529–535. LehmannKA,BassBL.1999.Theimportanceofinternalloopswithin
HartnerJC,WalkleyCR,LuJ,OrkinSH.2009.ADAR1isessentialforthe RNAsubstratesofADAR1.JMolBiol291:1–13.
maintenanceofhematopoiesisandsuppressionofinterferonsignaling. LehmannKA,BassBL.2000.Double-strandedRNAadenosinedeami-
NatImmunol10:109–115. nasesADAR1andADAR2haveoverlappingspecificities.Biochemistry
HellwigS,BassBL.2008.Astarvation-inducednoncodingRNAmodu-
39:12875–12884.
lates expression of Dicer-regulated genes. Proc Natl Acad Sci 105: LevanonEY,EisenbergE,YelinR,NemzerS,HalleggerM,ShemeshR,
12897–12902. FligelmanZY,ShoshanA,PollockSR,SztybelD,etal.2004.Systematic
HiguchiM,SingleFN,KöhlerM,SommerB,SprengelR,SeeburgPH.
identificationofabundantA-to-Ieditingsitesinthehumantranscrip-
1993.RNAeditingofAMPAreceptorsubunitGluR-B:Abase-paired
tome.NatBiotechnol22:1001–1005.
intron–exon structure determines position and efficiency. Cell 75: Levanon EY, Hallegger M, Kinar Y, Shemesh R, Djinovic-Carugo K,
1361–1370. RechaviG,JantschMF,EisenbergE.2005.Evolutionarilyconserved
HiguchiM,MaasS,SingleFN,HartnerJ,RozovA,BurnashevN,Feld- humantargetsofadenosinetoinosineRNAediting.NucleicAcidsRes
meyerD,SprengelR,SeeburgPH.2000.PointmutationinanAMPA
33:1162–1168.
receptorgenerescueslethalityinmicedeficientintheRNA-editing LiJB,LevanonEY,YoonJ-K,AachJ,XieB,LeproustE,ZhangK,GaoY,
enzymeADAR2.Nature406:78–81. ChurchGM.2009.Genome-wideidentificationofhumanRNAedit-
HoJWK,JungYL,LiuT,AlverBH,LeeS,IkegamiK,SohnK-A,Minoda ing sites by parallel DNA capturing and sequencing. Science 324:
A, Tolstorukov MY, Appert A, et al. 2014. Comparative analysis of
1210–1213.
metazoanchromatinorganization.Nature512:449–452. LiF,ZhengQ,RyvkinP,DragomirI,DesaiY,AiyerS,ValladaresO,Yang
J,BambinaS,SabinLR,etal.2012.GlobalanalysisofRNAsecondary
HongC,ClementNL,ClementS,HammoudSS,CarrellDT,CairnsBR,
structureintwometazoans.CellRep1:69–82.
SnellQ,ClementMJ,JohnsonWE.2013.Probabilisticalignmentleads
toimprovedaccuracyandreadcoverageforbisulfitesequencingdata. LiL,QianG,ZuoY,YuanY,ChengQ,GuoT,LiuJ,LiuC,ZhangL,
BMCBioinformatics14:337. ZhengH. 2016.Ubiquitin-dependent turnoverofadenosine deami-
naseactingonRNA1(ADAR1)isrequiredforefficientantiviralac-
HoopengardnerB,BhallaT,StaberC,ReenanR.2003.Nervoussystem
targets of RNA editing identified by comparative genomics. Science
tivityofTypeIinterferon.JBiolChem291:24974–24985.
301:832–836. LiddicoatBJ,PiskolR,ChalkAM,RamaswamiG,HiguchiM,HartnerJC,
LiJB,SeeburgPH,WalkleyCR.2015.RNAeditingbyADAR1prevents
Hurst SR, Hough RF, Aruscavage PJ, Bass BL. 1995. Deamination of
MDA5sensingofendogenousdsRNAasnonself.Science349:1115–
mammalianglutamatereceptorRNAbyXenopusdsRNAadenosine
deaminase:SimilaritiestoinvivoRNAediting.RNA1:1051–1060. 1120.
Liscovitch-BrauerN,AlonS,PorathHT,ElsteinB,UngerR,ZivT,Ad-
JepsonJEC,ReenanRA.2009.Adenosine-to-inosinegeneticrecodingis
monA,LevanonEY,RosenthalJJC,EisenbergE.2017.Trade-offbe-
requiredintheadultstagenervoussystemforcoordinatedbehaviorin
Drosophila.JBiolChem284:31391–31400. t
C
w
e
e
ll
e
1
n
6
t
9
ra
:
n
1
s
9
c
1
r
–
ip
2
t
0
o
2
m
.
eplasticityandgenomeevolutionincephalopods.
JohnD,WeirickT,DimmelerS,UchidaS.2017.RNAEditor:Easyde-
LiuT,RechtsteinerA,EgelhoferTA,VielleA,LatorreI,CheungM-S,
tectionofRNAeditingeventsandtheintroductionofeditingislands.
ErcanS,IkegamiK,JensenM,Kolasinska-ZwierzP,etal.2011.Broad
BriefBioinform18:993–1001.
chromosomaldomainsofhistonemodificationpatternsinC.elegans.
JoyceGF.2002.TheantiquityofRNA-basedevolution.Nature418:214–
GenomeRes21:227–236.
221.
LucksJB,MortimerSA,TrapnellC,LuoS,AviranS,SchrothGP,Pachter
KanekoH,DridiS,TaralloV,GelfandBD,FowlerBJ,ChoWG,Kleinman
L,DoudnaJA,ArkinAP.2011.MultiplexedRNAstructurecharacter-
ME,PonicsanSL,HauswirthWW,ChiodoVA,etal.2011.DICER1 izationwithselective2′-hydroxylacylationanalyzedbyprimerexten-
deficitinducesAluRNAtoxicityinage-relatedmaculardegeneration. sionsequencing(SHAPE-Seq).ProcNatlAcadSci108:11063–11068.
Nature471:325–330.
MaE,MacRaeIJ,KirschJF,DoudnaJA.2008.Autoinhibitionofhuman
KikunoR,NagaseT,WakiM,OharaO.2002.HUGE:Adatabasefor dicerbyitsinternalhelicasedomain.JMolBiol380:237–243.
humanlargeproteinsidentifiedintheKazusacDNAsequencingproj-
Mannion NM, Greenwood SM, Young R, Cox S, Brindle J, Read D,
ect.NucleicAcidsRes30:166–168.
Nellåker C, Vesely C, Ponting CP, McLaughlin PJ, et al. 2014. The
KimU,GarnerTL,SanfordT,SpeicherD,MurrayJM,NishikuraK.1994. RNA-editingenzyme ADAR1controlsinnateimmune responsesto
Purificationandcharacterizationofdouble-strandedRNAadenosine RNA.CellRep9:1482–1494.
deaminase from bovine nuclear extracts. J Biol Chem 269: 13480– MarkhamNR,ZukerM.2008.UNAFold:Softwarefornucleicacidfold-
13489. ingandhybridization.MethodsMolBiol453:3–31.
KimDDY,KimTTY,WalshT,KobayashiY,MatiseTC,BuyskeS,Gabriel Martin M. 2011. Cutadapt removes adapter sequences from high-
A.2004.WidespreadRNAeditingofembeddedaluelementsinthe throughputsequencingreads.EMBnetjournal17:10–12.
humantranscriptome.GenomeRes14:1719–1725.
MelcherT,MaasS,HerbA,SprengelR,SeeburgPH,HiguchiM.1996.A
KinT,OnoY.2007.Idiographica:Ageneral-purposewebapplicationto mammalianRNAeditingenzyme.Nature379:460–464.
buildidiogramson-demandforhuman,mouseandrat.Bioinformatics MillsJD,KawaharaY,JanitzM.2013.Strand-specificRNA-seqprovides
23:2945–2946. greaterresolutionoftranscriptomeprofiling.CurrGenomics14:173–
KiranAM,O’MahonyJJ,SanjeevK,BaranovPV.2013.Darnedin2013:
181.
Inclusion of model organisms and linking with Wikipedia. Nucleic MinocheAE,DohmJC,HimmelbauerH.2011.Evaluationofgenomic
AcidsRes41:D258–D261.
high-throughput sequencing data generated on Illumina HiSeq and
Lander ES, Linton LM, Birren B, Nusbaum C, Zody MC, Baldwin J, genomeanalyzersystems.GenomeBiol12:R112.
DevonK,DewarK,DoyleM,FitzHughW,etal.2001.Initialsequenc- MohrS,GhanemE,SmithW,SheeterD,QinY,KingO,PolioudakisD,
ingandanalysisofthehumangenome.Nature409:860–921. IyerVR,Hunicke-SmithS,SwamyS,etal.2013.ThermostablegroupII
LässigC,MatheislS,SparrerKMJ,deOliveiraMannCC,MoldtM,Patel intron reverse transcriptase fusion proteins and their use in cDNA
JR,GoldeckM,HartmannG,García-SastreA,HornungV,etal.2015. synthesisandnext-generationRNAsequencing.RNA19:958–970.
ATPhydrolysisbytheviralRNAsensorRIG-Ipreventsunintentional Morse DP, Bass BL.1997. Detection of inosineinmessengerRNA by
recognitionofself-RNA.eLife4:e10859. inosine-specificcleavage.Biochemistry36:8429–8434.
14 CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352
MappingthedsRNAWorld
MorseDP,BassBL.1999.LongRNAhairpinsthatcontaininosineare PolsonAG,BassBL,CaseyJL.1996.RNAeditingofhepatitisdeltavirus
presentinCaenorhabditiseleganspoly(A)+RNA.ProcNatlAcadSci antigenomebydsRNA-adenosinedeaminase.Nature380:454–456.
96:6048–6053. PorathHT,CarmiS,LevanonEY.2014.Agenome-widemapofhyper-
MorseDP,AruscavagePJ,BassBL.2002.RNAhairpinsinnoncoding editedRNArevealsnumerousnewsites.NatCommun5:4726.
regionsofhumanbrainandCaenorhabditiselegansmRNAareedited PorathHT,KnisbacherBA,EisenbergE,LevanonEY.2017.MassiveA-
by adenosine deaminases that act on RNA. Proc Natl Acad Sci 99: to-IRNAeditingiscommonacrossthemetazoaandcorrelateswith
7906–7911. dsRNAabundance.GenomeBiol18:185.
MouseGenomeSequencingConsortium,WaterstonRH,Lindblad-Toh PrachumwatA,DeVincentisL,PalopoliMF.2004.Intronsizecorrelates
K,BirneyE,RogersJ,AbrilJF,AgarwalP,AgarwalaR,AinscoughR, positivelywithrecombinationrateinCaenorhabditiselegans.Genetics
AlexanderssonM,etal.2002.Initialsequencingandcomparativeanal- 166:1585–1590.
ysisofthemousegenome.Nature420:520–562.
RamaswamiG,LiJB.2014.RADAR:Arigorouslyannotateddatabaseof
NeemanY,LevanonEY,JantschMF,EisenbergE.2006.RNAeditinglevel A-to-IRNAediting.NucleicAcidsRes42:D109–D113.
inthemouseisdeterminedbythegenomicrepeatrepertoire.RNA12: RamaswamiG,LiJB.2016.IdentificationofhumanRNAeditingsites:A
1802–1809. historicalperspective.Methods107:42–47.
NishikuraK.2010.FunctionsandregulationofRNAeditingbyADAR RamaswamiG,ZhangR,PiskolR,KeeganLP,DengP,O’ConnellMA,Li
deaminases.AnnuRevBiochem79:321–349.
JB.2013.IdentifyingRNAeditingsitesusingRNAsequencingdata
NishikuraK.2016.A-to-Ieditingofcodingandnon-codingRNAsby alone.NatMeth10:128–132.
ADARs.NatRevMolCellBiol17:83–96.
RebagliatiMR,MeltonDA.1987.AntisenseRNAinjectionsinfertilized
NottinghamRM,WuDC,QinY,YaoJ,Hunicke-SmithS,Lambowitz frogeggsrevealanRNAduplexunwindingactivity.Cell48:599–605.
AM.2016.RNA-seqofhumanreferenceRNAsamplesusingather-
ReichDP,TycKM,BassBL.2018.C.elegansADARsantagonizesilenc-
mostablegroupIIintronreversetranscriptase.RNA22:597–613.
ingofcellulardsRNAsbytheantiviralRNAipathway.GenesDev32:
O’ConnellMA,MannionNM,KeeganLP.2015.Theepitranscriptome
271–282.
andinnateimmunity.PLoSGenet11:e1005687.
RichA.1962.Ontheproblemsofevolutionandbiochemicalinformation
OhlsonJ,EnsteröM,SjöbergB-M,OhmanM.2005.Amethodtofind
transfer. In Horizons inbiochemistry(ed. KashaM, Pullman B), pp.
tissue-specificnovelsitesofselectiveadenosinedeamination.Nucleic
103–126,Academic,NewYork.
AcidsRes33:e167.
RiederLE,StaberCJ,HoopengardnerB,ReenanRA.2013.Tertiarystruc-
OhmanM,KällmanAM,BassBL.2000.Invitroanalysisofthebindingof turalelementsdeterminetheextentandspecificityofmessengerRNA
ADAR2tothepre-mRNAencodingtheGluR-BR/Gsite.RNA6:687–
editing.NatCommun4:2232.
697.
RobertsonMP,JoyceGF.2012.TheoriginsoftheRNAworld.ColdSpring
O’NeilD,GlowatzH,SchlumpbergerM.2013.RibosomalRNAdepletion
HarbPerspectBiol4:a003608.
for efficient use of RNA-seq capacity. Curr Protoc Mol Biol doi:
RosenthalJJC.2015.TheemergingroleofRNAeditinginplasticity.JExp
10.1002/0471142727.mb0419s103. Biol218:1812–1821.
OtaT,SuzukiY,NishikawaT,OtsukiT,SugiyamaT,IrieR,Wakamatsu
Rueter SM, Dawson TR, Emeson RB. 1999. Regulation of alternative
A
ch
,
a
H
ra
a
c
y
t
a
e
s
r
h
iz
i
a
K
ti
,
o
S
n
at
o
o
f
H
21
,
,
N
24
a
3
ga
fu
i
l
K
l-
,
le
e
n
t
g
a
t
l.
h
2
h
0
u
04
m
.
a
C
n
om
cD
p
N
le
A
te
s.
se
N
q
a
u
t
en
G
c
e
i
n
n
e
g
t
a
3
n
6
d
:
splicingbyRNAediting.Nature399:75–80.
40–45. RuffaloM,LaFramboiseT,KoyutuerkM.2011.Comparativeanalysisof
algorithmsfornext-generationsequencingreadalignment.Bioinfor-
Parker GS, Maity TS, Bass BL. 2008. dsRNA binding properties of
RDE-4andTRBPreflecttheirdistinctrolesinRNAi.JMolBiol384:
matics27:2790–2796.
967–979. Rybak-WolfA,JensM,MurakawaY,HerzogM,LandthalerM,Rajewsky
N.2014.AvarietyofdicersubstratesinhumanandC.elegans.Cell159:
PattersonJB,SamuelCE.1995.Expressionandregulationbyinterferonof
a double-stranded-RNA-specific adenosine deaminase from human
1153–1167.
cells: Evidence for two forms of the deaminase. Mol Cell Biol 15: SakuraiM,YanoT,KawabataH,UedaH,SuzukiT.2010.Inosinecya-
5376–5388. noethylationidentifiesA-to-IRNAeditingsitesinthehumantran-
PaulMS,BassBL.1998.InosineexistsinmRNAattissue-specificlevels
scriptome.NatChemBiol6:733–740.
andismostabundantinbrainmRNA.EMBOJ17:1120–1127. SakuraiM,UedaH,YanoT,OkadaS,TerajimaH,MitsuyamaT,Toyoda
A,FujiyamaA,KawabataH,SuzukiT.2014.Abiochemicallandscape
PestalK,FunkCC,SnyderJM,PriceND,TreutingPM,StetsonDB.2015.
IsoformsofRNA-editingenzymeADAR1independentlycontrolnu- ofA-to-IRNAeditinginthehumanbraintranscriptome.GenomeRes
cleicacidsensorMDA5-drivenautoimmunityandmulti-organdevel-
24:522–534.
opment.Immunity43:933–944. SakuraiM,ShiromotoY,OtaH,SongC,KossenkovAV,Wickramasinghe
PfallerCK,MastorakosGM,MatchettWE,MaX,SamuelCE,CattaneoR. J, Showe LC, Skordalakes E, Tang H-Y, Speicher DW, et al. 2017.
2015.MeaslesvirusdefectiveinterferingRNAsaregeneratedfrequent- ADAR1 controls apoptosis of stressed cells by inhibiting Staufen1-
lyandearlyintheabsenceofCproteinandcan bedestabilized by
mediatedmRNAdecay.NatStructMolBiol24:534–543.
adenosine deaminaseactingonRNA-1-likehypermutations.JVirol SaldiTK,AshPE,WilsonG,GonzalesP,Garrido-LeccaA,RobertsCM,
89:7735–7747. DostalV,GendronTF,SteinLD,BlumenthalT,etal.2014.TDP-1,the
Picardi E, Pesole G. 2013. REDItools: High-throughput RNA editing CaenorhabditiselegansorthologofTDP-43,limitstheaccumulationof
detectionmadeeasy.Bioinformatics29:1813–1814. double-strandedRNA.EMBOJ33:2947–2966.
PicardiE,D’ErchiaAM,GiudiceLoC,PesoleG.2017.REDIportal:A SaletoreY,MeyerK,KorlachJ,VilfanID,JaffreyS,MasonCE.2012.The
comprehensive database of A-to-I RNA editing events in humans. birthoftheEpitranscriptome:DecipheringthefunctionofRNAmod-
NucleicAcidsRes45:D750–D757. ifications.GenomeBiol13:175.
PolsonAG,BassBL.1994.Preferentialselectionofadenosinesformod- SamuelCE.2011.AdenosinedeaminasesactingonRNA(ADARs)are
ificationbydouble-strandedRNAadenosinedeaminase.EMBOJ13: bothantiviralandproviral.Virology411:180–193.
5701–5711. SavvaYA,JepsonJEC,ChangY-J,WhitakerR,JonesBC,StLaurentG,
PolsonAG,CrainPF,PomerantzSC,McCloskeyJA,BassBL.1991.The Tackett MR, Kapranov P, Jiang N, Du G, et al. 2013. RNA editing
mechanismofadenosinetoinosineconversionbythedouble-stranded regulates transposon-mediated heterochromatic gene silencing. Nat
RNAunwinding/modifyingactivity:Ahigh-performanceliquidchro- Commun4:2745.
matography-mass spectrometry analysis. Biochemistry 30: 11507– SchleeM.2013.MastersensorsofpathogenicRNA—RIG-Ilikereceptors.
11514. Immunobiol218:1322–1335.
CitethisarticleasColdSpringHarbPerspectBiol2019;11:a035352 15
