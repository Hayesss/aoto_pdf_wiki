---
source_path: /mnt/c/Users/Administrator/Zotero/storage/ZZ8BBVT6/Buenrostro 等 - 2015 - Single-cell chromatin accessibility reveals principles of regulatory variation.pdf
ingested: 2026-04-23
sha256: 77d0c3ffbfd01b59
---

LETTER
doi:10.1038/nature14590
Single-cell chromatin accessibility reveals principles
of regulatory variation
JasonD.Buenrostro1,2,BeijingWu1*,UlrikeM.Litzenburger2*,DaveRuff3,MichaelL.Gonzales3,MichaelP.Snyder1,
HowardY.Chang2&WilliamJ.Greenleaf1,4
Cell-to-cellvariationisauniversalfeatureoflifethataffectsawide captured and assayed usinga programmablemicrofluidicsplatform
rangeofbiologicalphenomena,fromdevelopmentalplasticity1,2to (Fluidigm) with methods optimized for this task (Fig. 1a, Extended
tumourheterogeneity3.Althoughrecentadvanceshaveimproved DataFig.1andSupplementaryDiscussion).Aftertranspositionand
ourabilitytodocumentcellularphenotypicvariation4–8,thefun- PCRontheintegratedfluidicscircuit(IFC),librarieswere collected
damental mechanisms that generate variability from identical and PCR amplified with cell-identifying barcoded primers. Single-
DNAsequencesremainelusive.Herewerevealthelandscapeand celllibrarieswerethenpooledandsequencedonahigh-throughput
principlesofmammalianDNAregulatoryvariationbydeveloping sequencing instrument. Using single-cell ATAC-seq, we generated
arobustmethodformappingtheaccessiblegenomeofindividual DNAaccessibilitymapsfrom254individualGM12878lymphoblas-
cellsbyassayfortransposase-accessiblechromatinusingsequen- toid cells. Aggregate profiles of scATAC-seq data closely reproduce
cing (ATAC-seq)9 integrated into a programmable microfluidics ensemble measures of accessibility profiled by DNase-seq and
platform. Single-cell ATAC-seq (scATAC-seq) maps from hun- ATAC-seq generated from ,107 or ,104 cells, respectively
dreds of single cells in aggregate closely resemble accessibility (Fig.1b,candExtendedDataFig.2a).Datafromsinglecellsrecap-
profiles from tens of millions of cells and provide insights into itulateseveralcharacteristicsofbulkATAC-seqdata,includingfrag-
cell-to-cellvariation.Accessibilityvarianceissystematicallyassoc- ment-size periodicity corresponding to integer multiples of
iatedwithspecifictrans-factorsandcis-elements,andwediscover nucleosomes, and a strong enrichment of fragments within regions
combinationsoftrans-factorsassociatedwitheitherinductionor of accessible chromatin (Extended Data Fig. 2b, c). Microfluidic
suppression of cell-to-cell variability. We further identify sets of chambers generating low library diversity or poor measures of
trans-factors associated with cell-type-specific accessibility vari- accessibility, which correlate with empty chambers or dead cells,
ance across eight cell types. Targeted perturbations of cell cycle were excluded from further analysis (Fig. 1d and Extended Data
ortranscriptionfactorsignallingevokestimulus-specificchanges Fig. 2d–l). Chambers passing filter yielded an average of 7.3 3 104
inthisobservedvariability.Thepatternofaccessibilityvariationin fragmentsmappingtothenucleargenome.Wefurthervalidatedthe
cisacrossthegenomerecapitulateschromosomecompartments10 approachbymeasuringchromatinaccessibilityfromatotalof1,632
denovo,linkingsingle-cellaccessibilityvariationtothree-dimen- IFC chambers representing three tier 1 ENCODE cell lines16 (H1
sionalgenomeorganization.Single-cellanalysisofDNAaccessibil- human embryonic stem cells (ES cells), K562 chronic myelogenous
ityprovidesnewinsightintocellularvariationofthe‘regulome’. leukaemiaandGM12878lymphoblastoidcells),aswellasfromV6.5
Heterogeneitywithincellularpopulationshasbeenevidentsincethe mouseEScells,EML1cells(mousehaematopoieticprogenitors),TF-
firstmicroscopicobservationsofindividualcells.Recentproliferation 1 cells (human erythroblast), HL-60 cells (human promyeloblasts)
of powerful methods for interrogating single cells4–8 has allowed and BJ fibroblasts (human foreskin fibroblasts).
detailed characterization of this molecular variation, and provided Becauseregulatoryelementsaregenerallypresentattwocopiesina
deepinsightintocharacteristicsunderlyingdevelopmentalplasticity1,2, diploid genome, we observe a near digital (0 or 1) measurement of
cancerheterogeneity3,anddrugresistance11.Inparallel,genome-wide accessibilityatindividualelementswithinindividualcells(Extended
mapping of regulatory elements in large ensembles of cells have DataFig.3a).Forexample,withinatypicalsinglecellweestimatea
unveiledsubstantialvariationinchromatinstructureacrosscelltypes, totalof9.4%ofpromotersarerepresentedinatypicalscATAC-seq
particularlyat distal regulatory regions12. In particular, methods for library(ExtendedDataFig.3b–d).ThesparsenatureofscATAC-seq
probinggenome-wideDNAaccessibilityhaveprovenextremelyeffec- datamakesanalysisofcellularvariationatindividualregulatoryele-
tiveinidentifyingregulatoryelementsacrossavarietyofcelltypes13 mentsimpractical.Wethereforedevelopedananalysisinfrastructure
and quantifying changes that lead to both activation or repression tomeasureregulatoryvariationusingchangesofaccessibilityacross
of gene expression. Given this broad diversity of activity within setsofgenomicfeatures(Fig.2a,b).Toquantifythisvariationwefirst
regulatory elements when comparing phenotypically distinct cell chooseasetofopenchromatinpeaks,identifiedusingtheaggregate
populations,itisreasonabletohypothesizethatheterogeneityatthe accessibility track, which share a common characteristic (such as
single-cell level extends to accessibility variability within cell types transcriptionfactorbindingmotif,ChIP-seqpeaksorcellcyclerep-
at regulatory elements. However, the lack of methods to probe licationtimingdomains).Wethencalculatetheobservedfragments
DNA accessibilitywithinindividualcellshaspreventedquantitative intheseregionsminustheexpectedfragments, downsampledfrom
dissectionofthishypothesizedregulatoryvariation. theaggregateprofile,withinindividualcells.Tocorrectforbias,we
We have developed a single-cell assay for transposase-accessible divide this by the root mean square of fragments expected from a
chromatin (scATAC-seq). ATAC-seq is an ensemble measure of background signal constructed to estimate technical and sampling
open chromatin that uses the prokaryotic Tn5 transposase14,15 to error within single-cell data sets (Methods and Extended Data
tagregulatoryregions by inserting sequencing adapters into access- Fig. 4). Hereafter, we refer to this metric as ‘deviation’. Finally, for
ible regions of the genome. In scATAC-seq, individual cells are anysetoffeatures,wealsocalculateanoverall‘variability’scoreacross
1DepartmentofGenetics,StanfordUniversitySchoolofMedicine,Stanford,California94305,USA.2PrograminEpithelialBiologyandtheHowardHughesMedicalInstitute,StanfordUniversitySchoolof
Medicine,Stanford,California94305,USA.3FluidigmCorporation,SouthSanFrancisco,California94080,USA.4DepartmentofAppliedPhysics,StanfordUniversity,Stanford,California94025,USA.
*Theseauthorscontributedequallytothiswork.
486 | NATURE | VOL 523 | 23 JULY 2015
G2015 MacmillanPublishersLimited.Allrightsreserved
a
IFC
cell capture
Lyse Release Quench Extend and ATAC tra ( n E s D p T o A s ) ase (M ED gC TA l2) Tn5 ends PCR
b
d
all cells (Fig. 2b), a metric of excess variance over the background regulatoryelementswithbothGATA1andGATA2ChIP-seqsignals
signal. show increased variability in accessibility, whereas sites with only
WefirstfocusedouranalysisonK562myeloidleukaemiacells,a GATA1 or GATA2 show substantially less variability (Fig. 2g and
cell type with extensive epigenomic data sets17,18. To comprehen- ExtendedDataFig.6h).Incontrast,wefindnosubstantialchangein
sively characterize variability associated with trans-factors within variabilityofGATA1bindingsitesthatco-occurwithJUNorCEBPB
individual K562 cells, we computed variability across all available (ExtendedDataFig.6i).WealsofindpeaksuniquetoGATA1binding
ENCODE ChIP-seq, transcription factor motifs and regions that are significantly more accessible than peaks unique to GATA2
differed in replication timing (as determined from Repli-Seq data (Extended Data Fig. 6k–l) supporting the hypothesis that GATA1,
sets19) (Fig. 2c, d). We found measures of cell-to-cell variability anactivatorofaccessibility,competeswithGATA2toinducesingle-
were highly reproducible across biological replicates (Extended cellvariability.ExtendingthisanalysistoalltranscriptionfactorChIP-
DataFig.5).Asexpectedfromproliferating cells,wefind increased seqdatasetsrevealedatrans-factorsynergylandscapeforaccessibility
variability within differentreplication timing domains, representing variation(Fig.2gandExtendedDataFig.6j).Forexample,chromatin
variable ATAC-seq signal associated with changes in DNA content accessibilityvarianceassociatedwithGATA2bindingissignificantly
across the cell cycle. In addition, we discover a set of trans-factors enhanced when the same region could also be bound by GATA1,
associated with high variability. These factors include sequence- TAL1 or P300. In contrast, CTCF, SUZ12, and ZNF143 appear to
specific transcription factors, such as GATA1/2, JUN and STAT2, actasgeneralsuppressorsofaccessibilityvariance,unlessassociated
and chromatineffectors,such asBRG1(alsoknownasSMARCA4) withproximalbindingofZNF143orSMC3,thelatteracohesinsub-
and P300 (also known as EP300). Immunostaining followed by unitinvolvedinchromosomelooping18,20.Thus,singlecellaccessibility
microscopy or flow cytometry (Fig. 2e and Extended Data Fig. profilesnominatedistincttrans-factorsthat,incombination,induceor
6a–d) confirmed heterogeneous expression of GATA1 and suppresscell-to-cellregulatoryvariation.
GATA2. Principal component (PC) analysis of single-cell devia- Tovalidateourabilitytodetectchangesinaccessibilityvariance,we
tions across all trans-factors show seven significant PCs, with PC used chemical inhibitors to modulate potential sources of cell-cell
5 describing changes in DNA abundance throughout the cell cycle. variability. Inhibition of cyclin-dependent kinases 4 and 6 (CDK4/
This analysis suggests that high-variance trans-factors are variable 6),essentialcomponentsofthecellcycle,causedamarkedreduction
independentofthecellcycle(Fig.2fandExtendedDataFig.6e–g). of variability within peaks associated with DNA replication timing
The remaining PCs show contributions from several transcription domains(Repli-Seq)(Fig.3a). The additionofinhibitorsofJUNor
factors, suggesting that variance across sets of trans-factors repres- BCR–ABLkinases(JNKiandimatinib,respectively)increasedG1/S-
ent distinct regulatory states in individual cells. associatedvariabilitysuggestinganincreaseinthesubpopulationof
Wehypothesizedthatvariationassociatedwithdifferenttrans-fac- G1/Scells,whichwasvalidatedwithflowcytometry(ExtendedData
torscansynergize,eitherthroughcooperativeorcompetitivebinding, Fig.7).JUNvariabilitywassignificantlygainedinresponsetoJNKibut
toinduceorsuppresssite-to-sitevariabilityinchromatinaccessibility. not imatinib treatment, suggesting that high-variance trans-factors
For example, the most variant factors in K562 cells, GATA1 and can also be specifically and pharmacologically modulated. Tumour
GATA2,displayexpressionheterogeneityandalsobindanidentical necrosisfactor(TNF)treatmentofGM12878cellsspecificallymodu-
consensus sequence GATA, suggesting these factors may compete latedaccessibilityvariabilityatNF-kBsites(Fig.3b),consistentwith
foraccesstoDNAsequences.Insupportofthishypothesis,wefind theknownstochasticandoscillatorypropertyofnuclearshuttlingin
)%(
skaep
ni
stnemgarF
c
R value = 0.80
6 7 8 9 10 11
Scale 50 kb hg19 DNase-seq (log2 reads)
chr19: 36,150,000 36,200,000 36,250,000
0.56 _
Duke DNase
26 0 7 _ _
Bulk ATAC-seq
(ref. 9) 108 0 _ _ Aggregate
scATAC-seq 0 _ ETV2 UPK1A ZBTB32 IGFLR1 HSPB6 ARHGAP33
RBM42 COX6B1 KMT2B LIN37
U2AF1L4 PROSER3 PSENEN
254 single
cells 2
0
Fragments
)stnemgarf
2gol(
qes-CATAcs
LETTER RESEARCH
9
Collect 96
scATAC libraries 8
from IFC
7
PCR with cell
identifying barcodes
6
Density
Pool libraries and 0.2
sequence 5
0
60 Empty One cell 50 Dead cell Two cells
40
30
20
10
0
3 4 5 6
Library size (log10 fragments)
Figure1|Single-cellATAC-seqprovidesanaccuratemeasureofchromatin scATAC-seqarecorrelatedwithDNase-seqdata(R50.80).d,Librarysize
accessibilitygenome-wide. a,Workflowformeasuringsingleepigenomes versuspercentageoffragmentsinopenchromatinpeaks(filteredasdescribed
usingscATAC-seqonamicrofluidicdevice(Fluidigm).b,Aggregatesingle- inMethods)withinK562cells(n5288).Dottedlines(15%and10,000)
cellaccessibilityprofilescloselyrecapitulateprofilesofDNase-seqandATAC- representcutoffsusedfordownstreamanalysis.
seqinGM12878cells.c,Genome-wideaccessibilitypatternsobservedby
23 JULY 2015 | VOL 523 | NATURE | 487
G2015 MacmillanPublishersLimited.Allrightsreserved
Cell1
Cell2 Cell3
c
GATA1 GATA2
0.8
–0.8
this system21. Together, these results show that variability can be iouslyreportedtodynamicallylocalizeintothenucleus,includingNF-
experimentally modulated and further demonstrates that variability kB,JUNandETS/ERG21,24,25,suggestingthattemporalfluctuationsin
isnotsolelydependentonthecellcycle. transcriptionfactorconcentrationmaybedrivingobservedchromatin
We observe that trans-factors associated with high variabilityare accessibilityheterogeneity.Finally,wefindBJfibroblastsandHL-60
generally cell-type specific. Hierarchical bi-clustering of single-cell cells exhibit less variance among this set of annotated trans-factor
deviationsgeneratedfromthreecelllinesrevealscell-typespecificsets motifs,suggestingdifferencesinthegloballevelsoftrans-factorvari-
oftranscriptionfactormotifsassociatedwithhighvariability(Fig.3c). abilityacrosscelllines.Specificchromatinstatesandhistonemodifi-
Thisanalysisalsoshowscellsfromdifferentbiologicalreplicatesclus- cations26arealsosometimesassociatedwithaccessibilityvariationin
terwiththeircelltypeoforigin(withasingleexception),suggesting singlecells(ExtendedDataFig.8b,c).Overallthesefindingssuggest
scATAC-seq can also be used to deconvolve heterogeneous cellular that trans-factors promote cell-type specific chromatin accessibility
mixtures.Systematicanalysisofallassayedcelltypesidentifiedhigh- variationgenome-wide.
variancetrans-factormotifsthataregenerallyuniquetospecificcell Patterns of variation in accessibility along the linear genome in
types(Fig.3dandExtendedDataFig.8a).Forexample,regionsassoc- individualcellsrevealanunexpectedconnectiontohigher-orderchro-
iatedwithGATAtranscriptionfactorsaremostvariantinK562cells, mosome folding. We calculated single-cell deviations within sliding
whereas regions associated with master pluripotency transcription windows across the genome, each encompassing a fixed number of
factorsNanogandSox2aremostvariantinmouseEScells,consistent peaks (n 5 25)(Fig. 4a).Wedetermined whichwindowsco-varied
withpreviousobservationsofexpressionvariationofthesefactors22,23. withinindividualcellsbycalculatingtheco-correlationofeachwin-
We also find high variability of GATA1 and PU.1 (SPI1) binding dowacrossallotherswithinthesamechromosomewithinindividual
accessibility in EML cells, a cell type previously shown to have cells(ExtendedDataFig.9a,b).Wefurtherenhancedthisco-correla-
.200-foldGATA1and.15-foldPU.1expressiondifferenceswithin tionmatrixusingasecondarycorrelationanalysisusingmethodssim-
clonalcellularsubpopulations1.The completesetofidentifiedhigh- ilartothoseusedinchromosomeconformationstudies10(Methods).
variancetrans-factorscontainsanumberoftranscriptionfactorsprev- Theresultingmatrix,whichidentifiespairsofpositionsinthegenome
ytilibairav
llec–lleC
d g
3 GATA1:ChIP-seq Observed CTCF SMC3
G1/S:Repli-Seq Permuted ZNF143
JUND:Motif CTCF
SUZ12 CJUN:ChIP-seq SMC3 2 BRG1:ChIP-seq CBX2
STAT2:ChIP-seq CBX8 GATA1:Motif POL3
High variance BDP1
1 Low variance C PO JU L N 2
ATF
STAT2
0 100 200 300 400 –15 –10 –5 0 5 10 15 CEBPB
Deviation BRG1
e f ZNF274
DAPI GATA1 SIRT6
INI1
STAT1
MAFK
MAFF
ARID3A
GATA2 Overlay TAL1
GATA1
TBLR1 Synergy
P300 score
COREST
COREST
GATA2
Variability amplifiers Variability buffers
tnuoc
lleC
GATA1 GATA1
40 inaccessible cells accessible cells
P300:ChIP-seq 30 Permuted s.d. = 1 Observed s.d. = 3.1 4
20
1
10 Variability
0
4
1
Variability
5 10 15 20 25
Ranked principal components
denialpxe
ecnairav
fo
noitcarF
a b Compute difference
from downsampled
ensemble
1 1 2 1 0 2 2 1 0 2 1 0 1 0 0 0 2 76 48 TF
0 1 0 1 0 0 1 0 0 0 0 3 1 0 1 1 0 23 13 Deviation = . 2 0 0 1 1 0 1 0 1 0 1 1 1 2 1 0 0 –22 –3 . . 1 1 2 1 0 2 2 1 0 2 1 0 1 0 0 0 2 211 50 0 1 0 1 0 0 1 0 0 0 0 3 1 0 1 1 0 –22 –12 2 0 0 1 1 0 1 0 1 0 1 1 1 2 1 0 0 –18 –10 Variability = 1 1 2 1 0 2 2 1 0 2 1 0 1 0 0 0 2 87 42
Rank sorted variability scores
Observed
0.25 Permuted
0.2
0.15
0.1 Cell-cycle PC
0.05
0
1kaeP 2kaeP 3k.aeP . .
Cell 1 [TF] Collect Sum across Sample
fragment peaks across peaks
counts per cell with TF motif and compute BS
6
–9 21 42 –7 6 19
Cell 2 [TF]
FT SB 1
Calculate
deviation and
variability scores
Identify TF motif in peaks .
.
.
.
.
. SB N
From aggregate
map all fragments
and call peaks
From single cells compute deviation and variability taepeR
12
17 BS –7 RMS 41 –20 (TF)2 2 5 1 (BS mean)2
SB
naem
28
27 16 45 37 19 29
SB
SMR
cells cells
2ATAG TSEROC TSEROC 003P 1RLBT 1ATAG 1LAT A3DIRA FFAM KFAM 1TATS 1INI 6TRIS 472FNZ 1GRB BPBEC 2TATS FTA NUJC 2LOP 1PDB 3LOP 8XBC 2XBC 3CMS 21ZUS FCTC 341FNZ
RESEARCH LETTER
Figure2|Trans-factorsareassociatedwithsingle-cellepigenomic measuredfrompermutedbackground(seeMethods)isshowningreydots.
variability. a,Schematicshowingtwocellularstates(transcriptionfactorhigh d,Distributionofnormalizeddeviationsfromexpectedaccessibilitysignalfor
andtranscriptionfactorlow)leadingtodifferentialchromatinaccessibility.TF, GATA1sitesinindividualcells,histogramofcellsshowningrey,densityprofile
transcriptionfactor.b,Analysisinfrastructure,whichusesacalculated showninpurple(seeMethods).e,ImmunostainingofGATA1(green)and
backgroundsignal(BS;seeSupplementaryMethods,section3.2)tocalculate GATA2(red)showsproteinexpressioninK562cells.f,Principalcomponents
transcriptionfactordeviationsandvariabilityfromscATAC-seqdata.The rankedbyfractionofvarianceexplainedfromobserveddeviationdata(purple)
transcriptionfactorvalueiscalculatedbysubtractingthenumberofexpected andpermuteddata(orange).Barplotofobserveddatashowningrey.
fragmentsfromtheobservedfragmentspercell(seeSupplementaryMethods, g,Calculatedchangesinassociatedvariabilityoffactorswhenpresenttogether
section3.1).c,Observedcell-to-cellvariabilitywithinsetsofgenomicfeatures versusindependently,depictingacontext-specifictrans-factorvariability
associatedwithChIP-seqpeaks,transcriptionfactormotifs,andreplication landscape(seeMethods).Venn-diagramsshowvariabilityassociatedwith
timing(errorestimatesshowningrey,seeMethodsfordetails).Variability GATA1and/orGATA2andCTCFand/orSMC3(co-)occurringChIP-seqsites.
488 | NATURE | VOL 523 | 23 JULY 2015
G2015 MacmillanPublishersLimited.Allrightsreserved
1 Max
a b d
c
6
–6
K562 rep.1
K562 rep.2
K562 rep.3
H1 ES cells
GM rep.1 GM rep.2 GM rep.3
GM rep.4
Single-cell epigenomes
whereaccessibilityco-varieswithinindividualcells,yieldsmegabase- in situ hybridization (FISH) measurements of interactions between
scalecorrelationdomainshighlyconcordantwithpreviouslyobserved DNAloci28.
chromosomecompartments27(Fig.4b–dandExtendedDataFig.9c–i) UsingscATAC-seq,wedissectedsingle-cellepigenomicheterogen-
(R50.61forchromosome1).Thesedataprovideindependentbio- eity and linked cis- and trans-effectors to variability in accessibility
logicalvalidationoflarge-scalecompartmentalizationofhigher-order profiles within individual epigenomes. We identify trans-factors
chromatinstructure10,27.Moreover,theseresultssuggestthathigher- associated with increased accessibility variance, which we call high-
order chromatin interactions may drive regulatory variability in cis variancetrans-factors.Additionally,othertrans-factorssuchasCTCF
(elementsthatareproximaltogethertendtobeaccessibletogether). appeartobuffervariability,perhapsbyprovidingastableanchorof
Thus, ensemble chromosome conformation data may arise in part chromatinaccessibilityorinsulatorfunctionthatdampenspotential
fromthestatisticalpropertiesofsinglecellvariationinco-regulated fluctuations.Conversely,co-occurancewithotherfactorssuchasP300
accessibility, a hypothesis also supported by single-cell fluorescent appearstoamplifyvariability,perhapsduetosynergisticinteractions.
Deviation
Low variance factor
High variance factor
Treatment:
cell cycle inhibitor (CDK4/6)
0 100 200 300 400 500
Rank sorted change in variability
GATA
H1 ES cell
motifs
GM motifs
JUN NF-κB
ytilibairav
ni
egnahC
)lortnoc
– tnemtaert(
1.5 1.5 1.51
1.48
1.88
1.44
JUN factors NF-κB motifs 4 3 . . 1 8 8 0
3.52
2.44
0 0 1 1 . . 7 7 3 3
1.83 1.77
Repli-Seq 1 2 . . 6 2 7 0
(cell cycle) Treatment: 1 2 . . 6 6 2 9
TNF-α (NF-κB) 2.65
–1.5 –1.5 2.72
0 100 200 300 400 2.63
Rank sorted change in variability 2 2 . . 5 4 2 8
2.02
1.54
1.59
1.70 1.64
1.49
1.60 1.78
1.75
1.71
1.50 1.46 1.82
1.54
1.52
1.58
1.77 1.48 1.55 1.52
1.54
1H sllec
SE
MG 265K LME 1FT esuoM sllec
SE
06LH JB
TEAD1
MYCN
YY1
RREB1
NFKB1 RELA
REL
CTCF
ELF1 GATA2
GATA4 GATA1
GATA3 TAL1
NFE2 FOSL1
JUNB
FOSL2
JUND
JUN FOS
BATF
RFX1
RFX2
RUNX1 SPI1
ZEB1
EHF ERG
ETS1
FLI1
FEV RUNX2 BACH1
NFE2L2
NR4A2
ESRRA
ESRRB NANOG SOX9 SOX2
SOX6
Figure3|Cell-type-specificepigenomicvariability. a,b,Changeofcellular trans-factors(rows)andofsinglecells(columns)from3celltypes.Bottom
variabilityduetochemicalperturbationsusingCDK4/6cell-cycleinhibitor colourmaprepresentsassignmentclassificationfromhierarchicalclustering.
(K562)(a)orTNF-astimulation(GM12878)(b).Errorbars(showningrey) d,Variabilityassociatedwithtrans-factormotifsacross7celltypes.Eachrowis
representonestandarddeviationofbootstrappedcellsacrossthetwo normalizedtothemaximumvariabilityforthatmotifacrosscelltypes(left).
conditions.c,Heatmapofdeviationsfromexpectedaccessibilitysignalacross
Chomosome conformation capture c
(ref. 27) Permuted chr1
d
918,679 Chr1 (bp)
7.0
1.0–
a Chr1 Deviation
Single-cell epigenomes –3.5 3.5
Calculate
correlation
b
918,679
0.5
–0.1
Correlation
scATAC-seq
cis-correlation
Chr1 (bp)
0.5
–0.1
Correlation
249,040,706 249,040,706
noitalerroC
LETTER RESEARCH
Figure4|Structuredcis-variabilityacrosssingleepigenomes. a,Per-cell normalizeddeviationsofscATAC-seq(right)fromchromosome1(see
deviationsofexpectedfragmentsacrossaregionwithinchromosome1(see Methods).Datainwhiterepresentsmaskedregionsduetohighlyrepetitive
Methods).Fordisplay,onlylargedeviationcellsareshown(n5186cells). regions.c,Permutedcis-correlationmapforchromosome1(analysed
b,Pearsoncorrelationcoefficientrepresentingchromosomecompartment identicallytob).d,Boxhighlightsarepresentativeregiondepictinglong-range
signal(seeMethods)ofinteractionfrequencyfromachromatinconformation covariability.
captureassay(left,analysiscarriedoutofdatafromref.27)ordoublycorrelated
23 JULY 2015 | VOL 523 | NATURE | 489
G2015 MacmillanPublishersLimited.Allrightsreserved
RESEARCH LETTER
Lineage-specificmasterregulatorsareassociatedwithcell-typespecific 12. ENCODEProjectConsortium.AnintegratedencyclopediaofDNAelementsinthe
humangenome.Nature489,57–74(2012).
single-cellepigenomicvariabilityacrossseveralcelltypes,suggesting
13. Thurman,R.E.etal.Theaccessiblechromatinlandscapeofthehumangenome.
thatcontrolofsingle-cellvarianceisafundamentalcharacteristicof Nature489,75–82(2012).
differentbiologicalstates.Finally,variationofchromatinaccessibility 14. Goryshin,I.Y.&Reznikoff,W.S.Tn5invitrotransposition.J.Biol.Chem.273,
7367–7374(1998).
incisishighlycorrelatedwithpreviouslyreportedchromosomecom-
15. Adey,A.etal.Rapid,low-input,low-biasconstructionofshotgunfragmentlibraries
partments,openingtheintriguingpossibilitythatthiscomponentof byhigh-densityinvitrotransposition.GenomeBiol.11,R119(2010).
epigenomic noise has its roots in higher-order chromatinorganiza- 16. ENCODEProjectConsortium.User’sguidetotheEncyclopediaofDNAElements
tion. Together these data provide a new hypothesis of regulatory (ENCODE).PLoSBiol.9,e1001046(2011).
17. Gerstein,M.B.etal.Architectureofthehumanregulatorynetworkderivedfrom
mechanismsthatgiverisetosingle-cellheterogeneity. ENCODEdata.Nature489,91–100(2012).
WeenvisionthatfuturestudieswillenhancetheutilityofscATAC- 18. Xie,D.etal.Dynamictrans-actingfactorcolocalizationinhumancells.Cell155,
seqbyfurtherimprovingtherecoveryofDNAfragments,increasing 713–724(2013).
19. Hansen,R.S.etal.SequencingnewlyreplicatedDNArevealswidespreadplasticity
throughput, and refining methods of data analysis (Supplementary
inhumanreplicationtiming.Proc.NatlAcad.Sci.USA107,139–144(2010).
Discussion). Improvements to throughput and new statistical tools 20. Parelho,V.etal.CohesinsfunctionallyassociatewithCTCFonmammalian
willenablesingle-cellstobepartitionedbycell-stateandanalysedin chromosomearms.Cell132,422–433(2008).
21. Tay,S.etal.Single-cellNF-kBdynamicsrevealdigitalactivationandanalogue
aggregatetofindtheindividualpeaksthatdrivevariability(Extended
informationprocessing.Nature466,267–271(2010).
DataFig.10).Inaddition,weanticipatescATAC-seqmaybepaired 22. Gru¨n,D.,Kester,L.&vanOudenaarden,A.Validationofnoisemodelsforsingle-cell
with existing approaches in microscopy and single-cell RNA-seq to transcriptomics.NatureMethods11,637–640(2014).
23. Singer,Z.S.etal.DynamicheterogeneityandDNAmethylationinembryonicstem
provideopportunitiesforsystemsanalysisofindividualcells.Suchan
cells.Mol.Cell55,319–331(2014).
approachwilllinkregulatoryvariationtodetailsofphenotypicvari- 24. Cai,L.,Dalal,C.K.&Elowitz,M.B.Frequency-modulatednuclearlocalization
ation, providing new insights into the molecular underpinnings of burstscoordinategeneregulation.Nature455,485–490(2008).
25. Levine,J.H.,Lin,Y.&Elowitz,M.B.Functionalrolesofpulsingingeneticcircuits.
cellular heterogeneity. We believe scATAC-seq will also enable the
Science342,1193–1200(2013).
interrogationoftheepigenomiclandscapeofsmallorrarebiological 26. Ernst,J.etal.Mappingandanalysisofchromatinstatedynamicsinninehuman
samplesallowingfordetailed,andpotentiallydenovo,reconstruction celltypes.Nature473,43–49(2011).
ofcellulardifferentiationordiseaseatthefundamentalunitofinvest- 27. Kalhor,R.,Tjong,H.,Jayathilaka,N.,Alber,F.&Chen,L.Genomearchitectures
revealedbytetheredchromosomeconformationcaptureandpopulation-based
igation—thesinglecell. modeling.NatureBiotechnol.30,90–98(2012).
28. Giorgetti,L.etal.Predictivepolymermodelingrevealscoupledfluctuationsin
Received12January;accepted26May2015. chromosomeconformationandtranscription.Cell157,950–963(2014).
Publishedonline17June2015. SupplementaryInformationisavailableintheonlineversionofthepaper.
1. Chang,H.H.,Hemberg,M.,Barahona,M.,Ingber,D.E.&Huang,S.Transcriptome- AcknowledgementsThisworkwassupportedbyNationalInstitutesofHealth(NIH)
widenoisecontrolslineagechoiceinmammalianprogenitorcells.Nature453, P50HG007735(toH.Y.C.andW.J.G.),UH2AR067676andLifespanExtension
544–547(2008). Foundation(H.Y.C.),U19AI057266(toW.J.G.)andtheRitaAllenFoundation(to W.J.G.)
2. Imayoshi,I.etal.Oscillatorycontroloffactorsdeterminingmultipotencyandfatein andtheBaxterFoundationFacultyScholarGrant(toW.J.G);H.Y.C.isanEarlyCareer
mouseneuralprogenitors.Science342,1203–1208(2013). ScientistoftheHowardHughesMedicalInstitute.J.D.B.acknowledgessupportfrom
3. Patel,A.P.etal.Single-cellRNA-seqhighlightsintratumoralheterogeneityin theNationalScienceFoundationGraduateResearchFellowshipsandNIHtraining
primaryglioblastoma.Science344,1396–1401(2014). grantT32HG000044forsupport.M.P.S.acknowledgestheNIHandtheNational
4. Bendall,S.C.etal.Single-cellmasscytometryofdifferentialimmuneanddrug HumanGenomeResearchInstitute(NHGRI)forfundingthrough5U54HG00455805.
responsesacrossahumanhematopoieticcontinuum.Science332,687–696 WethankmembersofGreenleafandChanglaboratories,aswellastheFluidigmteam,
(2011). includingL.Xifordiscussions.WeacknowledgetheS.Kimlaboratoryforassistance
5. Raj,A.,Rifkin,S.A.,Andersen,E.&vanOudenaarden,A.Variabilityingene withFACSsortingandtheC.Bustamantelaboratoryforhelpwithsequencing.Wealso
expressionunderliesincompletepenetrance.Nature463,913–918(2010). thankR.Nichols,C.Mazumdar,V.SebastianoandV.Riscaforcells.
6. Jaitin,D.A.etal.Massivelyparallelsingle-cellRNA-seqformarker-free
AuthorContributionsJ.D.B.,H.Y.C.andW.J.G.conceivedofthemethod.J.D.B.,B.W.,
decompositionoftissuesintocelltypes.Science343,776–779(2014).
M.G.andD.R.developedtheFluidigmC1microfluidicprotocols.B.W.performedall
7. Smallwood,S.A.etal.Single-cellgenome-widebisulfitesequencingforassessing
scATAC-seqexperimentswithsupervisionfromJ.D.B.U.M.L.conductedtheflow
epigeneticheterogeneity.NatureMethods11,817–820(2014).
analysis,immunostainsanddrugtreatments.J.D.B.developedandimplementedthe
8. Zong,C.,Lu,S.,Chapman,A.R.&Xie,X.S.Genome-widedetectionofsingle-
analysisinfrastructurewithinputfromW.J.G.Allauthorsinterpretedthedataandwrote
nucleotideandcopy-numbervariationsofasinglehumancell.Science338,
themanuscript.W.J.G.andH.Y.C.supervisedallaspectsofthiswork.
1622–1626(2012).
9. Buenrostro,J.D.,Giresi,P.G.,Zaba,L.C.,Chang,H.Y.&Greenleaf,W.J. AuthorInformationAlldatahasbeendepositedinGEOundertheaccessionnumber
Transpositionofnativechromatinforfastandsensitiveepigenomicprofilingof GSE65360.FluidigmC1scriptsforperformingscATAC-seqareavailableathttps://
openchromatin,DNA-bindingproteinsandnucleosomeposition.NatureMethods www.fluidigm.com/c1openapp/scripthub/script/2015-06/single-cell-chromatin-
10,1213–1218(2013). accessib-1433443631246-1.Reprintsandpermissionsinformationisavailableat
10. Lieberman-Aiden,E.etal.Comprehensivemappingoflong-rangeinteractions www.nature.com/reprints.Readersarewelcometocommentontheonlineversionof
revealsfoldingprinciplesofthehumangenome.Science326,289–293(2009). thepaper.Theauthorsdeclarecompetingfinancialinterests:detailsareavailableinthe
11. Michor,F.etal.Dynamicsofchronicmyeloidleukaemia.Nature435,1267–1270 onlineversionofthepaper.Correspondenceandrequestsformaterialsshouldbe
(2005). addressedtoW.J.G.(wjg@stanford.edu)orH.Y.C.(howchang@stanford.edu).
490 | NATURE | VOL 523 | 23 JULY 2015
G2015 MacmillanPublishersLimited.Allrightsreserved
b
d
0 20 40 60 80
Cell Barcode
sdaer
etacilpud
noitcarF
0.75
0.5
0.25
0
0 20 40 60 80
Cell Barcode
501xdecneuqes
sdaeR
c
Tn5-DNA DNA purification EDTA (mM) Temperature (°C) Fragments released
complex - - RT 1.00
+ - RT 6.72
- 10 RT 3.80
- 20 RT 1.99
- 50 RT 2.65
- 10 50 6.46
- 20 50 11.21
- 50 50 12.79 *
- 50 70 8.98
Tn5 - + + + + 50 70 8.13
R a e g le e a n s t e - - EDTA SDS * Optimal conditions
e f
15
10
5
0
5 10 15 20
Number of PCR cycles
ecnecseroulF
evitaleR
LETTER RESEARCH
a
On-IFC steps Off-IFC steps
Cell capture
& L A y T s A e C Tra R [ n E e s D l p e T o a A s s a e ] se Q [M E u D g e C T n A c l h ] T E n5 xt e e n n d ds PCR dua 9 w l- 6 i i t n - h w d e c e u l x l s P p to C ri m m R ers pu P ri o fy o & l l i s b e ra q r u ie e s n , ce
2
ATAC Ly 5 se 0 k & cells C p e e n ll t e ri t f u c g e e lls & T c e o s n t d re it l i e o a n s s e Que M n g c C h l w 2 ith fro f m r q a P g in m C s R o e l n u t t o b s l q e re u c l a e e n a ll t s i p f e y e d llet
free DNA
1
0.8
0.6
0.4
0.2
0
ExtendedDataFigure1|Methodsdevelopmentforassayingsingle protocol,showingconditionsthatmarkedlyimprovefragmentyieldoverno
epigenomes.a,scATAC-seqworkflowforstepsperformedbothonandoffthe releaseconditionsorpurifyingDNA.Fragmentsreleasedrepresentsthefold
integratedfluidicchip(IFC).b,c,ThedevelopmentofanefficientTn5release gaininlibrarydiversity,asmeasuredbyquantitativePCR(qPCR).d,qPCR
protocoldesignedtopermitdownstreamenzymaticreactionswithoutDNA fluorescencetracesof96librariesgeneratedusingscATAC-seq.Forall
purification.b,Aninvitroelectrophoreticmobilitygelshiftassayusinga subsequentlibrariesweusedatotalof14PCRcycles(dottedline).e,f,Abar
fluorescentlylabelledPCRproduct(lane1),showingastableTn5-DNA plotofper-celllibrarysequencingdepth(e)andfractionofduplicatereads
complex(lane2)dissociatedwith50mMEDTA(lane3)or0.1%SDS(lane4). (f),showingeachlibrarywassequencedtovaryingdepthstoasimilarfraction
c,Workflowandassociatedtableofconditionsusedtooptimizerelease ofduplicatereads.
G2015 MacmillanPublishersLimited.Allrightsreserved
R value = 0.73
7 8 9 10 11 12
Bulk log2(reads)
)sdaer(2gol
llec-elgniS
b c
9
8
7
6
Density
0.2
5
0
0 200 400 600 800 1000
Insert-size (bp)
ytisneD
a
0.012 Single Cells Average Cell
0.008
0.004
0
d
Cell #4
g Cell #83
0 200 400 600 800 1000
Insert-size (bp)
tnuoC
daeR
0 200 400 600 800 1000
Insert-size (bp)
200
150
100
50
0
tnuoC
daeR
80
60
40
20
0
-2000 -1000 0 1000 2000
Distance to TSS (bp)
dnuorgkcab
revo
tnemhcirnE
dloF
-2000 -1000 0 1000 2000
Distance to TSS (bp)
20
15
10
5
dnuorgkcab
revo
tnemhcirnE
dloF
e f
20
15
10
5
h i
-2000 -1000 0 1000 2000
Distance to TSS (bp)
dnuorgkcab
revo
tnemhcirnE
dloF
20
15
10
5
0 200 400 600 800 1000
Insert-size (bp)
tnuoC
daeR
-2000 -1000 0 1000 2000
Distance to TSS (bp)
j k l
250 Cell #33
200
150
100
50
0
dnuorgkcab
revo
tnemhcirnE
dloF
RESEARCH LETTER
14 DNase-seq ATAC-seq (50k cells) 12 A sc T A A T C A - C se -s q e ( q 500 cells)
10
8
6
4
2
ExtendedDataFigure2|scATAC-seqdatarecapitulatebulkATAC-seq livecellstain(Calcein)andexclusionofethidiumbromide.e,Histogramofread
characteristics. a,Fragmentsobservedinopenchromatinpeaksidentified startsaroundTSSsforcellno.4showshighenrichment.f,DNAfragmentsize
fromaggregatescATAC-seqdata(n5384libraries)arehighlycorrelatedwith distributionforcellno.4showingnucleosomalperiodicity.g,Imagessimilarto
readsobservedfrombulkATAC-seqinGM12878cells.b,Histogramof dshowingstainingofcellno.83,suggestinglowviabilityduetoethidium
aggregatedreadstartsaroundalltranscriptionstartsites(TSS)(inK562cells) bromidestaining.h,Histogramofreadstartsaroundtranscriptionstartsites
comparingensembleapproaches,including500cellATAC-seqreportedina showslowerenrichmentthancellno.4.i,DNAfragmentsizedistributionfor
previouspublication,toscATAC-seqshowshighenrichmentabove cellno.83.j,Imagessimilartodshowingstainingofcellno.33suggesting
backgroundlevelofreads.c,DNAfragmentsizedistributionofATAC-seq viability.k,Histogramofreadstartsaroundtranscriptionstartsitesofthiscell
fragmentsfromsinglecells(grey)andtheaverageofallsinglecells(red)display showslowlevelsofenrichment.l,DNAfragmentsizedistributionshowingno
characteristicnucleosome-associatedperiodicity.d,Phase-contrast(left)and nucleosome-associatedperiodicity.
epifluorescenceimages(right)ofcapturedcellno.4displayingcharacteristic
G2015 MacmillanPublishersLimited.Allrightsreserved
0 2 4 6 8 10
Accessibility, log2(fragments)
tnuoc
kaeP
2500
2000
1500
1000
500
0
-1 -0.5 0 0.5 1 1.5
% promoters with >0 fragments, log10(%)
tnuoc
lleC
b
Typical promoter
c d
100 8.4%
75
50
25
0
-1 -0.5 0 0.5 1 1.5 2 2.5
Theoretical, assuming sequencing to saturation
% promoters with >0 fragments, log10(%)
tnuoc
lleC
0 0.25 0.5 0.75
Mean number of fragments for each peak in 1 cell
100 9.4%
75
50
25
0
tnuoc
kaeP
LETTER RESEARCH
a
15000 Mean of all peaks = 0.10 fragments
10000
5000
0
ExtendedDataFigure3|FragmentrecoverymetricswithinscATAC-seq c,d,Recoveryoftypicalpromotersshowninawithinsinglecellswithin
libraries. a,Accessibilityacrossallpeaks(n550,000)inGM12878cells. observed(c)andextrapolated(d)datausingmeasuresofpredictedlibrary
b,AccessibilityacrossallannotatedpromotersinGM12878cells.Typical complexity.
promotersusedforsubsequentanalysisareboxedwithdottedlines.
G2015 MacmillanPublishersLimited.Allrightsreserved
a
1 2 3 4 5 6 7 8 9 10
Rank sorted peak intensity bins
ytilibairav
llec-lleC
2
1.5
1
0.5
0
0 10,000 20,000 30,000 40,000
Number of associated peaks
ytilibairaV
d e
1 2 3 4 5 6 7 8 9 10
Rank sorted GC bias bins
3 GATA1:ChIP-seq
G1/S:RepliSeq JUND:motif
P300:ChIP-seq
2 CJUN:ChIP-seq
1
ytilibairav
llec-lleC
b
1 2 3 4 5 6 7 8 9 10
Rank sorted Tn5 bias bins
2
1.5
1
0.5
0
fo
noitaived
dradnatS
)detceepxe/devresbo(2gol
0.6 0.7
0.5 0.6
0.5
0.4
0.4
0.3
0.3
0.2
0.2
0.1 0.1
0 0
1 2 3 4 5 6 7 8 9 10
Rank sorted peak intensity bins
fo
noitaived
dradnatS
)detceepxe/devresbo(2gol
1 2 3 4 5 6 7 8 9 10
Rank Sorted Tn5 bias bins
ytilibairav
llec-lleC
c
f
2
1.5
1
0.5
0
i j
GATA1:ChIP-seq
0 0.2 0.4 0.6 0.8 1
Fraction of total fragments
,noitalerroc
nosraeP
tesatad
etelpmoc
eht
ot
evitaler
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
Fraction of total fragments
,langis
latot
fo noitcarF
tesatad
etelpmoc
eht
ot
evitaler
10 30 50 70
Mean accessibility per peak (fragments)
k l
1
0.8
0.6
0.4
0.2
0
ytilibairaV
Without
Bias correction
1 2 3 4 5 6 7 8 9 10
Rank sorted GC bins
With
Bias correction
g
3 GATA1:ChIP-seq
G1/S:RepliSeq JUND:motif
P300:ChIP-seq
CJUN:ChIP-seq 2
1
h
fo
noitaived
dradnatS
)detceepxe/devresbo(2gol
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
-8 -6 -4 -2 0 2 4 6 8
Deviation
Nanog:motif
)detcepxe/devresbo(2gol 1 R = 0.90
0.5
0
-0.5
-1
-8 -6 -4 -2 0 2 4 6 8
Deviation
)detcepxe/devresbo(2gol
RESEARCH LETTER
Relative density
0 1
1 R = 0.80
0.5
0
-0.5
-1
ExtendedDataFigure4|scATAC-seqdataanalysispipelineandvalidation (g)andpeaks(h)containingaNanogmotif.i,j,Variabilityscoresforfactors
ofbiasnormalization. a–c,Standarddeviationoflog-foldchangeinreads (purple)andthepermutedbackground(grey)rankedbynumberofpeak
acrosscellswithinpeaksbinnedbydecilesofpeakintensity(a),Tn5bias associations(i)andthemeanaccessibilityperannotatedpeak(j).k,l,K562
(b)andGCbias(c).d–f,Variabilityscores(incorporatingbiasnormalization) single-celldatasetsshowingtheeffectonvariabilityscoresasafunctionof
withinthesamepeaksshownina–c,peaksarebinnedbydecilesofpeak downsamplingfragments.Fidelityafterdownsamplingismeasuredwith
intensity(d),Tn5bias(e)andGCbias(f).g,h,Log-foldchangeversus correlation(k)anddynamicrange(l)relativetothecompletedataset.
deviationscoresacrosssingleK562cellsforGATA1ChIP-seqtargetsites
G2015 MacmillanPublishersLimited.Allrightsreserved
0 0.05 0.1 0.15 0.2 0.25
Measurement errors, estimated
using permutations of bias signal
yb
srorre
deppartstooB
sllec
gnilpmas-bus
0.25
0.2
0.15
0.1
Variability
0.05 3
0 1
0 0.05 0.1 0.15 0.2
Measurement errors, estimated
using permutations of bias signal
serocs
ytilibairav
fo
noitaived
dradnatS
)3
= n(
setacilper
lacigoloib
morf
R = 0.86 0.4 R = 0.66
0.3
0.2
Variability
0.1 3
0 1
serocs
ytilibairav
fo
noitaived
dradnatS
)3
= n(
setacilper
lacigoloib
morf
a
Low variance factor
High variance factor
0 100 200 300 400 500
Rank sorted change in variability
d e f
Variability
3
1
ytilibairav
ni
egnahC
1.5
1
0.5
0
-0.5
-1
Biological replicate 1
-1.5
0 100 200 300 400 500
Rank sorted change in variability
ytilibairav
ni
egnahC
1.5
1
0.5
0
-0.5
-1
-1.5
0 100 200 300 400 500
Rank sorted change in variability
ytilibairav
ni
egnahC
LETTER RESEARCH
b c
1.5
1
0.5
0
-0.5
-1
Biological replicate 2 Biological replicate 3
-1.5
0.4 R = 0.78
0.3
0.2
0.1
0
0 0.05 0.1 0.15 0.2 0.25
Bootstrapped errors by
sub-sampling cells
ExtendedDataFigure5|Biologicalreplicatesandmeasurementerror onestandarddeviationofthevariabilityscoresafterbootstrappingcellsfrom
analysis. a–c,Observedchangesinvariabilitycomparingthemergedsetof eachreplicate.d–f,Correlationoferrorscomputedusingthreedistinct
replicates(K562)toeachindividualbiologicalreplicate.Errorbarsrepresent approaches.
G2015 MacmillanPublishersLimited.Allrightsreserved
e
-0.1 -0.05 0 0.05 0.1 0.15
Principal component 1
5
tnenopmoc
lapicnirP
a b
300
200
100
0
f g
0.5
G1/S:RepliSeq
0.4
0.3
0.2
0.1
0 G2/M:RepliSeq
-0.1 S S 4: 1 R :R ep e l p iS liS eq eq
-0.2
-0.3 S3:RepliSeq S2:RepliSeq -0.4
tnuoC
300
200
100
0
tnuoC
400
10 10 10 10 10 10 10 10
GATA1 fluorescence GATA2 fluorescence
Permuted data
Polymerase
STAT
GATA
JUN/FOS 5
Histone CTCF -5 cell-cycle
Single-cell Epigenomes Single-cell Epigenomes
noitaiveD
300
200
100
0
tnuoC
400
300
200
100
0
10 10 10 10 10 10
ACTIN fluorescence CTCF fluorescence
tnuoC
c d
400
0 2 4 0 2 4
h
CJUN GATA2
CEBPB GATA2
4
1
Variability
GATA1 Shared GATA2
)stnemgarf(
ytilibissecca
naeM
45
40
35
30
25
20
0 50 100 150 200 250 300
Accessibility (Fragments)
ytisneD
0.05
GATA1
shared GATA2 0.04
0.03
0.02
0.01
0
i j
ZNF143
CTCF
SUZ12
GATA1 Shared GATA2 SMC3
n=270 n=2,722 n = 3,554 CBX2
var=1.01 var=3.08 var=1.74 CBX8
error=0.07 error=0.08 error=0.21 POL3
BDP1
POL2
CJUN
ATF
STAT2
CEBPB
k l BRG1
ZNF274
INI1
SIRT6 STAT1
MAFK
MAFF ARID3A
TAL1
GATA1
GATA2
COREST
COREST
P300
TBLR1
-log10(p-value)
zScore = 6.22
pValue ~ 4.88x10-10
5
0
1RLBT 003P TSEROC TSEROC 2ATAG 1ATAG 1LAT A3DIRA FFAM KFAM 1TATS 6TRIS 1INI 472FNZ 1GRB BPBEC 2TATS FTA NUJC 2LOP 1PDB 3LOP 8XBC 2XBC 3CMS 21ZUS FCTC 341FNZ
RESEARCH LETTER
ExtendedDataFigure6|Characterizationofhigh-variancetrans-factorsin differentreplicationtimings(Repli-Seq)havestrongvariationalongthisaxis.
K562cells. a–d,DistributionofGATA1(a),GATA2(b),actin(c)andCTCF h,i,VenndiagramsshowingvariabilityofGATA1and/orGATA2(h),cJUN
(d)fluorescenceobservedbyflowcytometry.Distributionsingreydepict and/orGATA2andCEBPBand/orGATA2(co-)occurringChIP-seqsites
isotypecontrols.e,Bi-clusteredheatmapofsingle-celldeviationsasobserved (i).j,The2log (Pvalues)ofcalculatedchangesinco-occurringChIP-seqsites
10
withinK562cells(n5239).Labelsonrightidentifyco-clusteringofrelated showninFig.2g.k,DistributionofaccessibilityamongGATA1only,GATA2
factors.f,Bi-clusteredheatmapofsingle-celldeviationsobservedfrom only,andsharedsites.l,MeanaccessibilityfromGATA1only,GATA2only,
permuteddata.g,Projectionoffactorloadingsontoprincipalcomponent1 andsharedsitesink,errorbarsrepresentonestandarddeviationgeneratedby
versus5fromprincipalcomponent(PC)analysisofheatmapshownine.Factor bootstrappingChIP-seqpeaks.
loadingsdonotvaryalongPC5,althoughpeaksassociatedwithregionswith
G2015 MacmillanPublishersLimited.Allrightsreserved
0 100 200 300 400 500
Rank sorted change in variability
ytilibairav
ni
egnahC
1.5
1 ( R ce e l p l c liS yc e le q )
0.5
0
-0.5
-1
-1.5
0 100 200 300 400 500
Rank sorted change in variability
ytilibairav
ni
egnahC
a
90
60
30
Imatinib (BCR-ABL) 0
b
2
G1/S:RepliSeq
1.5
1 s-phase:RepliSeq
JUN factors
0.5
0
JUN inhibitor -0.5
tnuoC
120
150
100
50
tnuoC
250
200
0
60
40
20
0
tnuoC
80
150
100
50
tnuoC
LETTER RESEARCH
c d
Control Cell cycle inhibitor (CDK4/6)
50K 100K 150K 200K 50K 100K 150K 200K
Fluorescence (PI) Fluorescence (PI)
e f
Imatinib (BCR-ABL) 200 JUN inhibitor
0
50K 100K 150K 200K 50K 100K 150K 200K 250K
Fluorescence (PI) Fluorescence (DAPI)
ExtendedDataFigure7|Drugtreatmentsmodulatefactorvariability. cytometrydatadepictingDNAcontent,usingDAPIorpropidiumiodide,in
a,b,ChangeinvariabilityofuntreatedK562cellsversuscellstreatedwith controlK562cells(c)orcellsshowingalteredcell-cyclestatusaftertreatment
imatinib(a)andJUNinhibitor(b)showincreaseofvariabilityinfactors withcell-cycleinhibitor(d),imatinib(e)orJUNinhibitor(f).
associatedwiththecellcycleorSphaseandJUNfactors,respectively.c–f,Flow
G2015 MacmillanPublishersLimited.Allrightsreserved
a b
H1ESC K562 GM
1-Active-Promoter
2-Weak-Promoter
3-Poised-Promoter
4-Strong-Enhancer
5-Strong-Enhancer
7-Weak-Enhancer
8-Insulator
9-Txn-Transition
10-Txn-Elongation
11-Weak-Txn
12-Repressed
13-Heterochrom/lo
1 2 1 2 1 2
Variability Variability Variability
c
H1ESC K562 GM
H2AZ
H3K4me1
H3K4me2
H3K4me3
H3K9ac
H3K27ac
1 H3K27me3
H3K36me3
0 H3K79me2
H4K20me1
EZH2
1 2 1 2 1 2
Variability Variability Variability
noitalerroC
1.7740AM-1LSOF 1.0940AM-BNUJ 1.8740AM-2LSOF 1.1940AM-DNUJ 1.6740AM-SOF 1.9840AM-NUJ 1.2640AM-NUJ-FTAB 1.1050AM-FAM-2EFN 2.0510AM-2l2efN 1.1950AM-kfaM-1hcaB 3.0800AM-1ipS 1.3740AM-1FLE 1.5740AM-1ILF 2.8900AM-1stE 1.4740AM-grE 1.8950AM-FHE 1.6510AM-VEF 1.1010AM-LER 1.7010AM-ALER 3.5010AM-1BKFN 1.0060AM-2XFR 1.9050AM-1xfR 1.0610AM-2A4RN 2.1410AM-brrsE 1.2950AM-ARRSE 2.2000AM-1XNUR 1.1150AM-2XNUR 1.3700AM-1BERR 2.3010AM-1BEZ 3.4010AM-ncyM 1.0900AM-1DAET 2.5900AM-1YY 1.9310AM-FCTC 1.7700AM-9XOS 3.3410AM-2xoS 1.5150AM-6xoS GONAN-8002.nehC 2.0410AM-1ATAG-1LAT 2.6300AM-2ATAG 1.2840AM-4ataG 3.5300AM-1ataG 2.7300AM-3ATAG
RESEARCH LETTER
GATA3-MA0037.2
Gata1-MA0035.3
Gata4-MA0482.1
GATA2-MA0036.2 TAL1-GATA1-MA0140.2
Chen.2008-NANOG
Sox6-MA0515.1 Sox2-MA0143.3
SOX9-MA0077.1
CTCF-MA0139.1 YY1-MA0095.2
TEAD1-MA0090.1
Mycn-MA0104.3
ZEB1-MA0103.2
RREB1-MA0073.1 RUNX2-MA0511.1
RUNX1-MA0002.2
ESRRA-MA0592.1 Esrrb-MA0141.2
NR4A2-MA0160.1 Rfx1-MA0509.1
RFX2-MA0600.1
NFKB1-MA0105.3
RELA-MA0107.1
REL-MA0101.1
FEV-MA0156.1
EHF-MA0598.1
Erg-MA0474.1
Ets1-MA0098.2
FLI1-MA0475.1
ELF1-MA0473.1 Spi1-MA0080.3
Bach1-Mafk-MA0591.1
Nfe2l2-MA0150.2
NFE2-MAF-MA0501.1
BATF-JUN-MA0462.1 JUN-MA0489.1
FOS-MA0476.1 JUND-MA0491.1
FOSL2-MA0478.1
JUNB-MA0490.1 FOSL1-MA0477.1
ExtendedDataFigure8|Transcriptionfactormotifcorrelationand b,c,Variabilityofregionsassociatedwithchromatinstates(b),asidentifiedin
variabilityacrosschromatinstate. a,Hierarchicalbi-clusteringofhigh- ref.26,andhistonemodifications(c).
variancetranscriptionfactormotifannotationsusingthePearsoncorrelation.
G2015 MacmillanPublishersLimited.Allrightsreserved
c
521,709 158,700,605 chr7 (bp)
d e
201
chr11
258,562 chr11 (bp) 134,480,584 490,074 chr12 (bp) 133,272,777 711,130 chr17 (bp) 80,571,026
g h
303,655 62,668,136
chr20 (bp) Chromosome
)nosraep(
.la
te
rohlaK
ot
noitalerroC
1rhc 2rhc 3rhc 4rhc 5rhc 6rhc 7rhc 8rhc 9rhc 01rhc 11rhc 21rhc 31rhc 41rhc 51rhc 61rhc 71rhc 81rhc 91rhc 02rhc 12rhc 22rhc Xrhc
i
0.75
0.5
0.25
0.4
0
-0.1
Correlation
0.4
-0.1
Correlation
0.4
-0.1
Correlation
0.4
-0.1
Correlation 0.4
-0.1
Correlation
Chromosome
)nosraep(
.la
te
aM
ot
noitalerroC
1rhc 2rhc 3rhc 4rhc 5rhc 6rhc 7rhc 8rhc 9rhc 01rhc 11rhc 21rhc 31rhc 41rhc 51rhc 61rhc 71rhc 81rhc 91rhc 02rhc 12rhc 22rhc Xrhc
-0.4 -0.2 0 0.2 0.4 0.6 0.8 1
Correlation (Pearson)
0.75
0.5
0.25
0
ytisneD
25
20
15
10
0.2 5
0
-0.2
918,679 249,040,706 chr1 (bp)
Correlation
LETTER RESEARCH
a b
Intrachromosomal devitation correlation
f
GM12878 K562
ExtendedDataFigure9|Cis-variabilityanalysiswithinsinglecells. a.c–g,Analysisofcis-correlation(identicaltoFig.4)forrepresentative
a,Interchromosomalchromosome1co-correlationsofdeviationscoreswithin chromosomes7,11,12,17and20.CorrelationbetweenscATAC-seqcis-
singlecellscalculatedforbinsof25peakswithinGM12878cells. correlationandchromosomeconformationcapturemethodsforeach
b,Distribution,usingdensityestimation,ofcorrelationvaluesshownin chromosomeinGM12878(h)andK562(i)cells.
G2015 MacmillanPublishersLimited.Allrightsreserved
a
-15 -10 -5 0 5 10 15
Deviation
tnuoc
lleC
b c
GATA1 GATA1
40 inaccessible cells accessible cells
30
20
10
0
-15 -10 -5 0 5 10 15
Deviation
tnuoc
lleC
-5 -2.5 0 2.5 5
log2 fold change
d e f
NFKB NFKB
inaccessible cells accessible cells 50
40
30
20
10
0
eulav-p
2gol-
15
10
5
0
-5 -2.5 0 2.5 5
log2 fold change
eulav-p
2gol-
15
10
5
0
-5 -2.5 0 2.5 5
log2 fold change
eulav-p
2gol-
30
25
20
15
10
5
0
-5 -2.5 0 2.5 5
log2 fold change
eulav-p
2gol-
Relative density
0 1
Non-GATA1:ChIP-seq targets (n=47,008) Direct GATA1:ChIP-seq targets (n=2,992)
n=94 n=124 n=1 n=179
Non-NFKB targets (n=44,811) Direct NFKB targets (n=5,189)
30
25
20
15
n=13 n=162 n=2 n=264 10
5
0
stnemgarf
naeM
Chromosome chr15 (bp)
0.6 20 kb hg19 NFKB low NFKB high
0
Scale
chr15: RefSeq Genes
ANP32A
MIR4312 MIR548H4
ANP32A-IT1
sllec
deknaR
)wol
ot
hgih(
2
0
Fragments
69,069,373 69,129,735
sllec
detros
modnaR
g
10
-10
Deviation
RESEARCH LETTER
NFKB site
ExtendedDataFigure10|Measurementsofindividualpeakswithinsingle binomialtest.Insetnumbersshowthenumberofpointsinupperleftorupper
cells. a,ThedistributionofGATA1deviationscoresforsingleK562cells. rightquadrantsofthepanel.g,Accessibilityatagenomiclocus,showing(top)
b,c,Volcanoplotsofnon-GATA1(b)andGATA1(c)peaksinK562cells,P aggregateNF-kBlow(blue)andNF-kBhigh(red)profiles,(middle)single
valueswerecalculatedusingabinomialtest.d,ThedistributionofNF-kB GM12878cellsrankedbyNF-kBdeviationsscoresand(bottom)unranked
deviationscoresforsingleGM12878cells.e,f,Volcanoplotsofnon-NF-kB singlecells.
(e)andNF-kB(f)peaksinGM12878cells,Pvalueswerecalculatedusinga
G2015 MacmillanPublishersLimited.Allrightsreserved
