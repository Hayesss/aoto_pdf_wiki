---
source_path: /mnt/c/Users/Administrator/Zotero/storage/FIYFFSTU/Conesa 等 - 2016 - A survey of best practices for RNA-seq data analys.pdf
ingested: 2026-04-23
sha256: 70bf68a0f9218754
---

Conesaetal.GenomeBiology (2016) 17:13
DOI10.1186/s13059-016-0881-8
REVIEW Open Access
A survey of best practices for RNA-seq data
analysis
Ana Conesa1,2*, Pedro Madrigal3,4*, Sonia Tarazona2,5, David Gomez-Cabrero6,7,8,9, Alejandra Cervera10,
Andrew McPherson11, Michał Wojciech Szcześniak12, Daniel J. Gaffney3, Laura L. Elo13, Xuegong Zhang14,15
and Ali Mortazavi16,17*
published,makingitchallengingfornewuserstoappreci-
Abstract
ateallofthestepsnecessarytoconductanRNA-seqstudy
RNA-sequencing (RNA-seq) has a widevariety of properly.
applications, but no single analysis pipeline can be Thereis no optimal pipeline for the variety ofdifferent
used in allcases. We review allof themajorsteps in applications and analysis scenarios in which RNA-seq
RNA-seq data analysis,including experimental design, can be used. Scientists plan experiments and adopt dif-
quality control, read alignment, quantification ofgene ferent analysis strategies depending on the organism be-
and transcript levels, visualization,differential gene ing studied and their research goals. For example, if a
expression, alternative splicing, functional analysis, genome sequence is available for the studied organism,
gene fusion detection and eQTL mapping. We it should be possible to identify transcripts by mapping
highlight the challenges associated with each step. RNA-seq reads onto the genome. By contrast, for organ-
We discuss the analysis of small RNAs and the isms without sequenced genomes, quantification would
integration of RNA-seq with other functional be achieved by first assembling reads de novo into con-
genomics techniques. Finally, we discuss theoutlook tigs and then mapping these contigs onto the transcrip-
for novel technologies that are changing thestate of tome. For well-annotated genomes such as the human
theart in transcriptomics. genome, researchers may choose to base their RNA-seq
analysis on the existing annotated reference transcrip-
tome alone, or might try to identify new transcripts and
Background
their differential regulation. Furthermore, investigators
Transcript identification and the quantification of gene
might be interested only in messenger RNA isoform ex-
expression have been distinct coreactivities inmolecular
pression or microRNA (miRNA) levels or allele variant
biology ever since the discovery of RNA’s role as the key
identification. Boththe experimentaldesign andtheana-
intermediate between the genome and the proteome.
lysis procedures will vary greatly in each of these cases.
The power of sequencing RNA lies in the fact that the
RNA-seq can be used solo for transcriptome profiling or
twin aspectsofdiscovery andquantification can be com-
in combination with other functional genomics methods
bined in a single high-throughput sequencing assay
to enhance the analysis of gene expression. Finally, RNA-
called RNA-sequencing (RNA-seq). The pervasive adop-
seq can be coupled with different types of biochemical
tion of RNA-seq has spread well beyond the genomics
assaytoanalyzemanyotheraspectsofRNAbiology,such
communityandhasbecomea standardpartofthetoolkit as RNA–protein binding, RNA structure, or RNA–RNA
usedbythelifesciencesresearchcommunity.Manyvaria-
interactions. These applications are, however, beyond the
tions of RNA-seq protocols and analyses have been scopeofthisreviewaswefocuson‘typical’RNA-seq.
Every RNA-seq experimental scenario could poten-
tially have different optimal methods for transcript
*Correspondence:aconesa@ufl.edu;pm12@sanger.ac.uk;ali.mortazavi@uci.edu
1InstituteforFoodandAgriculturalSciences,DepartmentofMicrobiology quantification, normalization, and ultimately differential
andCellScience,UniversityofFlorida,Gainesville,FL32603,USA expression analysis. Moreover, quality control checks
3WellcomeTrustSangerInstitute,WellcomeTrustGenomeCampus,Hinxton,
should be applied pertinently at different stages of the
CambridgeCB101SA,UK
16DepartmentofDevelopmentalandCellBiology,UniversityofCalifornia, analysis to ensure both reproducibility and reliability of
Irvine,Irvine,CA92697-2300,USA the results. Our focus is to outline current standards
Fulllistofauthorinformationisavailableattheendofthearticle
©2016Conesaetal.OpenAccessThisarticleisdistributedunderthetermsoftheCreativeCommonsAttribution4.0
InternationalLicense(http://creativecommons.org/licenses/by/4.0/),whichpermitsunrestricteduse,distribution,and
reproductioninanymedium,providedyougiveappropriatecredittotheoriginalauthor(s)andthesource,providealinkto
theCreativeCommonslicense,andindicateifchangesweremade.TheCreativeCommonsPublicDomainDedicationwaiver
(http://creativecommons.org/publicdomain/zero/1.0/)appliestothedatamadeavailableinthisarticle,unlessotherwisestated.
Conesaetal.GenomeBiology (2016) 17:13 Page2of19
and resources for the bioinformatics analysis of RNA- andsecondbyplanning anadequateexecutionofthese-
seq data. We do not aim to provide an exhaustive com- quencing experiment itself, ensuring that data acquisi-
pilation of resources or software tools nor to indicate tion does not become contaminated with unnecessary
one best analysis pipeline. Rather, we aim to provide a biases.In thissection, wediscussboth considerations.
commentedguidelineforRNA-seqdataanalysis.Figure1 One important aspect of the experimental design is
depicts a generic roadmap for experimental design and the RNA-extraction protocol used to remove the highly
analysis using standard Illumina sequencing. We also abundant ribosomal RNA (rRNA), which typically con-
briefly list several data integration paradigms that have stitutes over 90 % of total RNA in the cell, leaving the
beenproposedandcommentontheirpotentialandlimi- 1–2 % comprising messenger RNA (mRNA) that we are
tations. We finally discuss the opportunities as well as normally interested in. For eukaryotes, this involves
challenges provided by single-cell RNA-seq and long- choosing whether to enrich for mRNA using poly(A) se-
read technologies when compared to traditional short- lection or to deplete rRNA. Poly(A) selection typically
readRNA-seq. requiresarelativelyhighproportion ofmRNA withmin-
imal degradation as measured by RNA integrity number
Experimental design (RIN), which normally yields a higher overall fraction of
A crucial prerequisite for a successful RNA-seq study is reads falling onto known exons. Many biologically rele-
that the data generated have the potential to answer the vant samples (such as tissue biopsies) cannot, however,
biological questions of interest. This is achieved by first be obtained in great enough quantity or good enough
defining agood experimental design, that is, by choosing mRNA integrity to produce good poly(A) RNA-seq li-
the library type, sequencing depth and number of repli- braries and therefore require ribosomal depletion. For
cates appropriate for the biological system under study, bacterialsamples,inwhichmRNA isnotpolyadenylated,
Fig.1AgenericroadmapforRNA-seqcomputationalanalyses.Themajoranalysisstepsarelistedabovethelinesforpre-analysis,coreanalysis
andadvancedanalysis.Thekeyanalysisissuesforeachstepthatarelistedbelowthelinesarediscussedinthetext.aPreprocessingincludes
experimentaldesign,sequencingdesign,andqualitycontrolsteps.bCoreanalysesincludetranscriptomeprofiling,differentialgeneexpression,
andfunctionalprofiling.cAdvancedanalysisincludesvisualization,otherRNA-seqtechnologies,anddataintegration.Abbreviations:ChIP-seq
Chromatinimmunoprecipitationsequencing,eQTLExpressionquantitativeloci,FPKMFragmentsperkilobaseofexonmodelpermillionmapped
reads,GSEAGenesetenrichmentanalysis,PCAPrincipalcomponentanalysis,RPKMReadsperkilobaseofexonmodelpermillionreads,sQTL
Splicingquantitativetraitloci,TFTranscriptionfactor,TPMTranscriptspermillion
Conesaetal.GenomeBiology (2016) 17:13 Page3of19
theonlyviablealternativeisribosomaldepletion.Another biological variability of the system under study, as well as
consideration is whether to generate strand-preserving li- on the desired statistical power (that is, the capacity for
braries. The first generation of Illumina-based RNA-seq detecting statistically significant differences in gene ex-
used random hexamer priming to reverse-transcribe pressionbetweenexperimentalgroups).Thesetwoaspects
poly(A)-selected mRNA. This methodologydid not retain arepartofpoweranalysiscalculations(Fig.1a;Box1).
information contained onthe DNA strandthat is actually The adequate planning of sequencing experiments so
expressed [1] and therefore complicates the analysis and as to avoid technical biases is as important as good
quantificationofantisenseoroverlappingtranscripts.Sev-
eral strand-specific protocols [2], such as the widely used Box1.Numberofreplicates
dUTPmethod,extendtheoriginalprotocolbyincorporat-
ing UTP nucleotides during the second cDNA synthesis Threefactorsdeterminethenumberofreplicatesrequiredina
step, prior toadapter ligation followedbydigestionofthe RNA-seqexperiment.Thefirstfactoristhevariabilityinthe
strand containing dUTP [3]. In all cases, the size of the measurements,whichisinfluencedbythetechnicalnoiseand
finalfragments(usuallylessthan500bpforIllumina)will thebiologicalvariation.WhilereproducibilityinRNA-seqisusually
be crucial for proper sequencingand subsequent analysis.
highatthelevelofsequencing[1,45],otherstepssuchasRNA
Furthermore, sequencing can involve single-end (SE) or
extractionandlibrarypreparationarenoisierandmayintroduce
paired-end(PE)reads,althoughthelatterispreferablefor
biasesinthedatathatcanbeminimizedbyadoptinggood
de novo transcript discovery or isoform expression ana-
experimentalprocedures(Box2).Biologicalvariabilityisparticular
lysis [4, 5]. Similarly, longer reads improve mappability
and transcript identification [5, 6]. The best sequencing toeachexperimentalsystemandishardertocontrol[189].
option depends on the analysis goals. The cheaper, short Nevertheless,biologicalreplicationisrequiredifinferenceonthe
SEreadsarenormallysufficientforstudiesofgeneexpres- populationistobemade,withthreereplicatesbeingtheminimum
sion levels in well-annotated organisms, whereas longer foranyinferentialanalysis.Foraproperstatisticalpoweranalysis,
and PE reads are preferable to characterize poorly anno-
estimatesofthewithin-groupvarianceandgeneexpressionlevels
tatedtranscriptomes.
arerequired.Thisinformationistypicallynotavailablebeforehand
Another important factor is sequencing depth or li-
butcanbeobtainedfromsimilarexperiments.Theexactpowerwill
brary size, which is the number of sequenced reads for a
dependonthemethodusedfordifferentialexpressionanalysis,
givensample.Moretranscriptswillbedetectedandtheir
quantification will be more precise as the sample is se- andsoftwarepackagesexistthatprovideatheoreticalestimateof
quenced to a deeper level [1]. Nevertheless, optimal se- poweroverarangeofvariables,giventhewithin-groupvarianceof
quencing depth again depends on the aims of the thesamples,whichisintrinsictotheexperiment[190,191].Table1
experiment. While some authors will argue that as few showsanexampleofstatisticalpowercalculationsoverarangeof
as five million mapped reads are sufficient to quantify
fold-changes(oreffectsizes)andnumberofreplicatesinahuman
accurately medium to highly expressed genes in most
bloodRNA-seqsamplesequencedat30millionmappedreads.It
eukaryotic transcriptomes, others will sequence up to
shouldbenotedthattheseestimatesapplytotheaveragegene
100 million reads to quantify precisely genes and tran-
expressionlevel,butasdynamicrangesinRNA-seqdataarelarge,
scripts that have low expression levels [7]. When study-
ing single cells, which have limited sample complexity, theprobabilitythathighlyexpressedgeneswillbedetectedas
quantification is often carried out with just one million differentiallyexpressedisgreaterthanthatforlow-countgenes
reads but may be done reliably for highly expressed [192].Formethodsthatreturnafalsediscoveryrate(FDR),the
genes with as few as 50,000 reads [8]; even 20,000 reads proportionofgenesthatarehighlyexpressedoutofthetotalset
havebeenusedtodifferentiate celltypesinsplenictissue
ofgenesbeingtestedwillalsoinfluencethepowerofdetection
[9]. Moreover, optimal library size depends on the com-
aftermultipletestingcorrection[193].Filteringoutgenesthatare
plexityofthetargetedtranscriptome.Experimentalresults
expressedatlowlevelspriortodifferentialexpressionanalysis
suggest that deepsequencingimprovesquantification and
reducestheseverityofthecorrectionandmayimprovethepower
identification but might also result in the detection of
transcriptional noiseandoff-targettranscripts[10].Satur- ofdetection[20].Increasingsequencingdepthalsocanimprove
ation curves can be used to assess the improvement in statisticalpowerforlowlyexpressedgenes[10,194],andforany
transcriptome coverage to be expected at a given sequen- givensamplethereexistsalevelofsequencingatwhichpower
cingdepth[10]. improvementisbestachievedbyincreasingthenumberof
Finally, a crucial design factor is the number of repli-
replicates[195].ToolssuchasScottyareavailabletocalculatethe
cates.Thenumberofreplicatesthatshouldbeincludedin
besttrade-offbetweensequencingdepthandreplicatenumber
a RNA-seq experiment depends on both the amount of
givensomebudgetaryconstraints[191].
technical variability in the RNA-seq procedures and the
Conesaetal.GenomeBiology (2016) 17:13 Page4of19
Table1Statisticalpowertodetectdifferentialexpressionvaries section, we address all of the major analysis steps for a
witheffectsize,sequencingdepthandnumberofreplicates typical RNA-seq experiment, which involve quality con-
Replicatespergroup trol,readalignmentwithandwithoutareferencegenome,
3 5 10 obtaining metrics for gene and transcript expression, and
approaches for detecting differential gene expression. We
Effectsize(foldchange)
also discuss analysis options for applications of RNA-seq
1.25 17% 25% 44%
involving alternative splicing, fusion transcripts and small
1.5 43% 64% 91%
RNA expression. Finally, we review useful packages for
2 87% 98% 100% datavisualization.
Sequencingdepth(millionsofreads)
3 19% 29% 52% Quality-controlcheckpoints
The acquisition of RNA-seq data consists of several
10 33% 51% 80%
steps — obtainingraw reads, read alignment and quanti-
15 38% 57% 85%
fication. At each of these steps, specific checks should
Exampleofcalculationsfortheprobabilityofdetectingdifferentialexpression
beapplied tomonitor thequality ofthedata (Fig.1a).
inasingletestatasignificancelevelof5%,foratwo-groupcomparisonusing
aNegativeBinomialmodel,ascomputedbytheRNASeqPowerpackageof
Hartetal.[190].Forafixedwithin-groupvariance(packagedefaultvalue),the
Rawreads
statisticalpowerincreaseswiththedifferencebetweenthetwogroups(effect
size),thesequencingdepth,andthenumberofreplicatespergroup.This Quality control for the raw reads involves the analysis of
tableshowsthestatisticalpowerforagenewith70alignedreads,whichwas sequence quality, GC content, the presence of adaptors,
themediancoverageforaprotein-codinggeneforonewhole-bloodRNA-seq overrepresented k-mers and duplicated reads in order to
samplewith30millionalignedreadsfromtheGTExProject[214]
detect sequencing errors, PCR artifacts or contamina-
experimental design, especially when the experiment in- tions. Acceptable duplication, k-mer or GC content
volves a large number of samples that need to be proc-
levels are experiment- and organism-specific, but these
essed in several batches. In this case, including controls,
values should be homogeneous for samples in the same
randomizing sample processing and smart management
experiments. We recommend that outliers with over
of sequencing runs are crucial to obtain error-free data
30 % disagreement to be discarded. FastQC [11] is a
(Fig. 1a;Box2).
popular tool to perform these analyses on Illumina
reads, whereas NGSQC [12] can be applied to any plat-
Analysis of the RNA-seq data
form. As a general rule, read quality decreases towards
The actual analysis of RNA-seq data has as many varia- the 3’ end of reads, and if it becomes too low, bases
tions as there are applications of the technology. In this
should be removed to improve mappability. Software
tools such as the FASTX-Toolkit [13] and Trimmomatic
Box2.Experimentexecutionchoices [14] can be used to discard low-quality reads, trim
adaptor sequences,andeliminatepoor-quality bases.
RNA-seqlibrarypreparationandsequencingproceduresinclude
anumberofsteps(RNAfragmentation,cDNAsynthesis,adapter
Readalignment
ligation,PCRamplification,bar-coding,andlaneloading)that
Readsaretypicallymappedtoeither agenomeoratran-
mightintroducebiasesintotheresultingdata[196].Including scriptome, as will be discussed later. An important map-
exogenousreferencetranscripts(‘spike-ins’)isusefulbothfor ping quality parameter is the percentage of mapped
qualitycontrol[1,197]andforlibrary-sizenormalization[198]. reads, which is a global indicator of the overall sequen-
Forbiasminimization,werecommendfollowingthesuggestions cing accuracy and of the presence of contaminating
DNA. For example, we expect between 70 and 90 % of
madebyVanDijketal.[199],suchastheuseofadapterswith
regular RNA-seq reads to map onto the human genome
randomnucleotidesattheextremitiesortheuseofchemical-based
(depending on the read mapper used) [15], with a sig-
fragmentationinsteadofRNaseIII-basedfragmentation.Ifthe
nificant fraction of reads mapping to a limited number
RNA-seqexperimentislargeandsampleshavetobeprocessedin of identical regions equally well (‘multi-mapping reads’).
differentbatchesand/orIlluminaruns,cautionshouldbetakento When reads are mapped against the transcriptome, we
randomizesamplesacrosslibrarypreparationbatchesandlanesso expect slightly lower total mapping percentages because
astoavoidtechnicalfactorsbecomingconfoundedwith reads coming from unannotated transcripts will be lost,
experimentalfactors.Anotheroption,whensamplesareindividually and significantly more multi-mapping reads because of
reads falling onto exons that are shared by different
barcodedandmultipleIlluminalanesareneededtoachievethe
transcript isoformsofthesamegene.
desiredsequencingdepth,istoincludeallsamplesineachlane,
Other important parameters are the uniformity of read
whichwouldminimizeanypossiblelaneeffect.
coverage on exons and the mapped strand. If reads
Conesaetal.GenomeBiology (2016) 17:13 Page5of19
primarily accumulate at the 3’ end of transcripts in clear standard exists for biological replicates, as this de-
poly(A)-selected samples, this might indicate low RNA pends on the heterogeneity of the experimental system.
quality in the starting material. The GC content of If gene expression differences exist among experimental
mapped reads may reveal PCR biases. Tools for quality conditions, it should be expected that biological repli-
control in mapping include Picard [16], RSeQC [17] and cates of the same condition will cluster together in a
Qualimap[18]. principalcomponentanalysis(PCA).
Quantification Transcriptidentification
Once actual transcript quantification values have been When a reference genome is available, RNA-seq analysis
calculated, they should be checked for GC content and will normally involve the mapping of the reads onto the
gene length biases so that correcting normalization reference genome or transcriptome to infer which tran-
methods can be applied if necessary. If the reference scripts are expressed. Mapping solely to the reference
transcriptome is well annotated, researchers could transcriptome of a known species precludes the discov-
analyze the biotype composition of the sample, which is ery of new, unannotated transcripts and focuses the ana-
indicative of the quality of the RNA purification step. lysis onquantification alone. By contrast, ifthe organism
For example, rRNA and small RNAs should not be does not have a sequenced genome, then the analysis
present in regular polyA longRNA preparations [10, 19]. path is first to assemble reads into longer contigs and
A number of R packages (such as NOISeq [19] or EDA- then to treat these contigs as the expressed transcrip-
Seq [20]) provide useful plots for quality control of tome to which reads aremappedback again forquantifi-
count data. cation. In either case, read coverage can be used to
quantify transcript expression level (Fig. 1b). A basic
Reproducibility choice is whether transcript identification and quantifi-
The quality-control steps described above involve indi- cation aredonesequentiallyorsimultaneously.
vidual samples.In addition, itis also crucial to assess the
global quality of the RNA-seq dataset by checking on Alignment
the reproducibility among replicates and for possible Two alternatives are possible when a reference sequence
batch effects. Reproducibility among technical replicates is available: mapping to the genome or mapping to the
should be generally high (Spearman R2>0.9) [1], but no annotated transcriptome (Fig. 2a, b; Box 3). Regardless
Fig.2Readmappingandtranscriptidentificationstrategies.ThreebasicstrategiesforregularRNA-seqanalysis.aAnannotatedgenomeis
availableandreadsaremappedtothegenomewithagappedmapper.Next(novel)transcriptdiscoveryandquantificationcanproceedwithor
withoutanannotationfile.Noveltranscriptsarethenfunctionallyannotated.bIfnonoveltranscriptdiscoveryisneeded,readscanbemapped
tothereferencetranscriptomeusinganungappedaligner.Transcriptidentificationandquantificationcanoccursimultaneously.cWhenno
genomeisavailable,readsneedtobeassembledfirstintocontigsortranscripts.Forquantification,readsaremappedbacktothenovelreference
transcriptomeandfurtheranalysisproceedsasin(b)followedbythefunctionalannotationofthenoveltranscriptsasin(a).Representative
softwarethatcanbeusedateachanalysisstepareindicatedinboldtext.Abbreviations:GFFGeneralFeatureFormat,GTFgenetransferformat,
RSEMRNA-SeqbyExpectationMaximization
Conesaetal.GenomeBiology (2016) 17:13 Page6of19
Transcriptdiscovery
Box3.Mappingtoareference
Identifying novel transcripts using the short reads pro-
Mappingtoareferencegenomeallowsfortheidentificationof vided by Illumina technology is one of the most challen-
ging tasks in RNA-seq. Short reads rarely span across
novelgenesortranscripts,andrequirestheuseofagappedor
several splice junctions and thus make it difficult to dir-
splicedmapperasreadsmayspansplicejunctions.The
ectly infer all full-length transcripts. In addition, it is dif-
challengeistoidentifysplicejunctionscorrectly,especially
ficult to identify transcription start and end sites [21],
whensequencingerrorsordifferenceswiththereferenceexist
and tools such as GRIT [22] that incorporate other data
orwhennon-canonicaljunctionsandfusiontranscriptsare such as5’endsfrom CAGEorRAMPAGEtypicallyhave
sought.OneofthemostpopularRNA-seqmappers,TopHat, a better chance of annotating the major expressed iso-
followsatwo-stepstrategyinwhichunsplicedreadsarefirst forms correctly. In any case, PE reads and higher cover-
mappedtolocateexons,thenunmappedreadsaresplitand age help to reconstruct lowly expressed transcripts, and
replicates are essential to resolve false-positive calls (that
alignedindependentlytoidentifyexonjunctions[200,201].
is, mapping artifacts or contaminations) at the low end
SeveralothermappersexistthatareoptimizedtoidentifySNPs
of signal detection. Several methods, such as Cufflinks
orindels(GSNAP[202],PALMapper[203]MapSplice[204]),
[23], iReckon [24], SLIDE [25] and StringTie [26], in-
detectnon-canonicalsplicejunctions(STAR[15],MapSplice
corporate existing annotations by adding them to the
[204]),achieveultra-fastmapping(GEM[205])ormaplong-reads possible list of isoforms. Montebello [27] couples iso-
(STAR[15]).Importantparameterstoconsiderduringmapping form discovery and quantification using a likelihood-
arethestrandednessoftheRNA-seqlibrary,thenumberof based Monte Carlo algorithm to boost performance.
mismatchestoaccept,thelengthandtypeofreads(SEorPE), Gene-finding tools such as Augustus [28] can incorpor-
ate RNA-seq data to better annotate protein-coding
andthelengthofsequencedfragments.Inaddition,existing
transcripts, but perform worse on non-coding tran-
genemodelscanbeleveragedbysupplyinganannotationfile
scripts [29]. In general, accurate transcript reconstruc-
tosomereadmapperinordertomapexoncoordinates
tion from short reads is difficult, and methods typically
accuratelyandtohelpinidentifyingsplicingevents.Thechoice
showsubstantialdisagreement [29].
ofgenemodelcanalsohaveastrongimpactonthequantification
anddifferentialexpressionanalysis[206].Wereferthereaderto Denovotranscriptreconstruction
[30]foracomprehensivecomparisonofRNA-seqmappers.Ifthe When a reference genome is not available or is incom-
transcriptomeannotationiscomprehensive(forexample,inmouse plete, RNA-seq reads can be assembled de novo (Fig. 2c)
intoatranscriptomeusingpackagessuchasSOAPdenovo-
orhuman),researchersmaychoosetomapdirectlytoa
Trans [30], Oases [31],Trans-ABySS [32] or Trinity [33].
Fasta-formatfileofalltranscriptsequencesforallgenesofinterests.
In general, PE strand-specific sequencing and long reads
Inthiscase,nogappedalignmentisneededandunspliced
are preferred because they are more informative [33]. Al-
mapperssuchasBowtie[207]canbeused(Fig.2b).Mappingto
though it is impossible to assemble lowly expressed tran-
thetranscriptomeisgenerallyfasterbutdoesnotallowde scripts that lack enough coverage for a reliable assembly,
novotranscriptdiscovery. too many reads are also problematic because they lead to
potential misassembly and increased runtimes. Therefore,
of whether a genome or transcriptome reference is used, in silico reduction of the number of reads is recom-
reads may map uniquely (they can be assigned to only mendedfordeeplysequencedsamples[33].Forcompara-
one position in the reference) or could be multi-mapped tive analyses across samples, it is advisable to combine all
reads (multireads). Genomic multireads are primarily reads from multiple samples into a single input in order
due to repetitive sequences or shared domains of paralo- to obtain a consolidated set of contigs (transcripts),
gous genes. They normallyaccount for a significant frac- followed by mapping back of the short reads for expres-
tion of the mapping output when mapped onto the sionestimation[33].
genome and should not be discarded. When the refer- Either with a reference or denovo, the complete recon-
ence is the transcriptome, multi-mapping arises even structionoftranscriptomesusingshort-readIlluminatech-
more often because a read that would have been nology remains a challenging problem, and in many cases
uniquely mapped on the genome would map equally denovoassemblyresultsintensorhundredsofcontigsac-
well to all gene isoforms in the transcriptome that share counting for fragmented transcripts. Emerging long-read
the exon. In either case — genome or transcriptome technologies,suchasSMRTfromPacificBiosciences,pro-
mapping — transcript identification and quantification vide reads that are long enough to sequence complete
become important challenges for alternatively expressed transcripts for most genes and are a promising alternative
genes. thatisdiscussedfurtherinthe“Outlook”sectionbelow.
Conesaetal.GenomeBiology (2016) 17:13 Page7of19
Transcriptquantification uniform read distribution along the gene length.
The most common application of RNA-seq is to esti- Cufflinks was designed to take advantage of PE reads,
mate gene and transcript expression. This application is and may use GTF information to identify expressed
primarily based on the number of reads that map to transcripts, or can infer transcripts de novo from the
each transcript sequence, although there are algorithms mapping data alone. Algorithms that quantify expression
such as Sailfish that rely on k-mer counting in reads from transcriptome mappings include RSEM (RNA-Seq
without the need for mapping [34]. The simplest ap- by Expectation Maximization) [40], eXpress [41], Sailfish
proach to quantification is to aggregate raw counts of [35] and kallisto [42] among others. These methods allo-
mapped reads using programs such as HTSeq-count cate multi-mapping reads among transcript and output
[35] or featureCounts [36]. This gene-level (rather than within-sample normalized values corrected for sequen-
transcript-level) quantification approach utilizes a gene cing biases [35, 41, 43]. Additionally, the RSEM algo-
transfer format (GTF) file [37] containing the genome rithm uses an expectation maximization approach that
coordinates of exons and genes, and often discard multi- returns TPM values [40]. NURD [44] provides an effi-
reads. Raw read counts alone are not sufficient to com- cient way of estimating transcript expression from SE
pare expression levels among samples, as these values reads withalowmemoryandcomputing cost.
are affected by factors such as transcript length, total
number of reads, and sequencing biases. The measure Differentialgeneexpressionanalysis
RPKM (reads per kilobase of exon model per million Differential expression analysis (Fig. 1b) requires that
reads) [1] is a within-sample normalization method that gene expression values should be compared among sam-
will remove the feature-length and library-size effects. ples. RPKM, FPKM, and TPM normalize away the most
This measure and its subsequent derivatives FPKM important factor for comparing samples, which is se-
(fragments per kilobase of exon model per million quencing depth, whether directly or by accounting for
mapped reads), a within-sample normalized transcript the number of transcripts, which can differ significantly
expression measure analogous to RPKs, and TPM (tran- between samples. These approaches rely on normalizing
scripts per million) are the most frequently reported methods that are based on total or effective counts, and
RNA-seq gene expression values. It should be noted that tend to perform poorly when samples have heteroge-
RPKM and FPKM are equivalent for SE reads and that neous transcript distributions, that is, when highly and
FPKM can be converted into TPM using a simple differentially expressed features can skew the count dis-
formula [38]. The dichotomy of within-sample and tribution [45, 46]. Normalization methods that take this
between-sample comparisons has led to a lot of confu- into account are TMM [47], DESeq [48], PoissonSeq
sion in the literature. Correcting for gene length is not [49] and UpperQuartile [45], which ignore highly vari-
necessary when comparing changes in gene expression able and/or highly expressed features. Additional factors
within the same gene across samples, but it is necessary that interfere with intra-sample comparisons include
for correctly ranking gene expression levels within the changes in transcript length across samples or condi-
sample to account for the fact that longer genes accu- tions [50], positional biases in coverage along the tran-
mulate more reads. Furthermore, programs such as script (which are accounted for in Cufflinks), average
Cufflinks that estimate gene length from the data can fragment size [43], and the GC contents of genes (cor-
find significant differences in gene length between rected in the EDAseq package [21]). The NOISeq R
samplesthatcannotbeignored.TPMs,whicheffectively package [20] contains a wide variety of diagnostic plots
normalizeforthedifferencesincompositionofthetran- to identify sources of biases in RNA-seq data and to
scripts in the denominator rather than simply dividing applyappropriatenormalizationproceduresineachcase.
by the number of reads in the library, are considered Finally, despite these sample-specific normalization
more comparable between samples of different origins methods, batch effects may still be present in the data.
and composition but can still suffer some biases. These These effects can be minimized by appropriate experi-
must be addressed with normalization techniques such mental design [51] or, alternatively, removed by batch-
asTMM. correction methods such as COMBAT [52] or ARSyN
Several sophisticated algorithms have been developed [20, 53]. These approaches, although initially devel-
to estimate transcript-level expression by tackling the oped for microarray data, have been shown to work
problem of related transcripts’ sharing most of their wellwithnormalizedRNA-seqdata(STATegraproject,
reads. Cufflinks [39] estimates transcript expression unpublished).
from a mapping to the genome obtained from mappers As RNA-seq quantification is based on read counts
such as TopHat using an expectation-maximization that are absolutely or probabilistically assigned to tran-
approach that estimates transcript abundances. This scripts, the first approaches to compute differential ex-
approach takes into account biases such as the non- pression used discrete probability distributions, such as
Conesaetal.GenomeBiology (2016) 17:13 Page8of19
the Poisson or negative binomial [48, 54]. The negative the differential expression methods to leverage reprodu-
binomial distribution (alsoknown asthegamma-Poisson cibility between replicates.
distribution) is a generalization of the Poisson distribu- Recent independent comparison studies have demon-
tion, allowing for additional variance (called overdisper- strated that the choice of the method (or even the ver-
sion) beyond the variance expected from randomly sion of a software package) can markedly affect the
samplingfromapoolofmoleculesthatarecharacteristic outcome of the analysis and that no single method is
of RNA-seq data. However, the use of discrete distribu- likely to perform favorably for all datasets [56, 63, 64]
tions is not required for accurate analysis of differential (Box 4). We therefore recommend thoroughly docu-
expressionaslongasthesamplingvarianceofsmallread menting the settings and version numbers of programs
countsistakenintoaccount(mostimportantforexper- used and considering the repetition of important ana-
iments with small numbers of replicates). Methods for lyses usingmorethanonepackage.
transforming normalized counts of RNA-seq reads
while learning the variance structure of the data have Alternativesplicinganalysis
been shown to perform well in comparison to the Transcript-level differential expression analysis can po-
discrete distribution approaches described above [55, tentially detect changes in the expression of transcript
56]. Moreover, after extensive normalization (including isoformsfrom thesame gene, and specific algorithmsfor
TMM and batch removal), the data might have lost alternative splicing-focused analysis using RNA-seq have
their discrete nature and be more akin to a continuous been proposed. These methods fall into two major cat-
distribution. egories. The first approach integrates isoform expression
Some methods, such as the popular edgeR [57], take estimation with the detection of differential expression
as input raw read counts and introduce possible bias to reveal changes in the proportion of each isoform
sources into the statistical model to perform an inte- within thetotalgeneexpression.Onesuchearlymethod,
grated normalization as well as a differential expression BASIS, used a hierarchical Bayesian model to directly
analysis.In othermethods, thedifferential expression re- infer differentially expressed transcript isoforms [65].
quires the data to be previously normalized to remove CuffDiff2 estimates isoform expression first and then
all possible biases. DESeq2, like edgeR, uses the negative compares their differences. By integrating the two steps,
binomial as the reference distribution and provides its the uncertainty in the first step is taken into consider-
own normalization approach [48, 58]. baySeq [59] and ation when performing the statistical analysis to look for
EBSeq [60] are Bayesian approaches, also based on the differential isoform expression [66]. The flow difference
negative binomial model, that define a collection of metric (FDM) uses aligned cumulative transcript graphs
models to describe the differences among experimental from mapped exon reads and junction reads to infer iso-
groups and to compute the posterior probability of each forms and the Jensen-Shannon divergence to measure
one of them for each gene. Other approaches include thedifference[67].Recently,ShiandJiang[68]proposed
data transformation methods that take into account the a new method, rSeqDiff, that uses a hierarchical likeli-
sampling variance of small read counts and create hood ratio test to detect differential gene expression
discrete gene expression distributions that can be ana- without splicing change and differential isoform expres-
lyzed by regular linear models [55]. Finally, non- sion simultaneously. All these approaches are generally
parametric approaches such as NOISeq [10] or SAMseq hampered by the intrinsic limitations of short-read se-
[61] make minimal assumptions about the data and esti- quencing for accurate identification at the isoform level,
mate the null distribution for inferential analysis from as discussed in the RNA-seq Genome Annotation As-
the actual data alone. For small-scale studies that com- sessmentProject paper[30].
pare two samples with no or few replicates, the estima- The so-called ‘exon-based’ approach skips the estima-
tion of the negative binomial distribution can be noisy. tion of isoform expression and detects signals of alterna-
In such cases, simpler methods based on the Poisson tive splicing by comparing the distributions of reads on
distribution,such asDEGseq [62],oronempiricaldistri- exons and junctions of the genes between the compared
butions (NOISeq [10]) can be an alternative, although it samples. This approach is based on the premise that dif-
should be strongly stressed that, in the absence of bio- ferences in isoform expression can be tracked in the sig-
logical replication, no population inference can be made nals of exons and their junctions. DEXseq [69] and
and hence any p value calculation is invalid. Methods DSGSeq [70] adopt a similar idea to detect differentially
that analyze RNA-seq data without replicates therefore splicedgenesbytesting forsignificantdifferencesinread
only have exploratory value. Considering the drop in counts on exons (and junctions) of the genes. rMATS
price of sequencing, we recommend that RNA-seq ex- detects differential usage of exons by comparing exon-
periments have a minimum of three biological replicates inclusion levels defined with junction reads [71]. rDiff
when sample availability is not limiting to allow all of detects differential isoform expression by comparing
Conesaetal.GenomeBiology (2016) 17:13 Page9of19
read counts on alternative regions of the gene, either
Box4.Comparisonofsoftwaretoolsfordetecting
with or without annotated alternative isoforms [72].
differentialgeneandtranscriptexpression
DiffSplice uses alignment graphs to identify alternative
Manystatisticalmethodsareavailablefordetectingdifferentialgene splicing modules (ASMs) and identifies differential spli-
ortranscriptexpressionfromRNA-seqdata,andamajorpractical cing using signals of the ASMs [73]. The advantage of
exon or junction methods is their greater accuracy in
challengeishowtochoosethemostsuitabletoolforaparticular
identifying individual alternative splicing events. Exon-
dataanalysisjob.Mostcomparisonstudieshavefocusedon
based methods are appropriate if the focus of the study
simulateddatasets[56,208,209]oronsamplestowhichexogenous
isnot onwhole isoforms buton theinclusion and exclu-
RNA(‘spike-in’)hasbeenaddedinknownquantities[63,196].This
sion of specific exons and the functional protein do-
enablesadirectassessmentofthesensitivityandspecificityofthe mains (or regulatory features, in case of untranslated
methodsaswellastheirFDRcontrol.Assimulationstypicallyrely regionexons) thatthey contain.
onspecificstatisticaldistributionsoronlimitedexperimental
datasetsandasspike-indatasetsrepresentonlytechnicalreplicates Visualization
Visualization of RNA-seq data (Fig. 1c) is, in general
withminimalvariation,comparisonsusingsimulateddatasetshave
terms, similar to that of any other type of genomic se-
beencomplementedwithmorepracticalcomparisonsinreal
quencing data, and it can be done at the level of reads
datasetswithtruebiologicalreplicates[64,210,211].
(using ReadXplorer [74], for example) or at the level of
Asyet,noclearconsensushasbeenreachedregardingthebest
processed coverage (read pileup), unnormalized (for ex-
practicesandthefieldiscontinuingtoevolverapidly.However, ample, total count) or normalized, using genome
somecommonfindingshavebeenmadeinmultiplecomparison browsers such as the UCSC browser [75], Integrative
studiesandindifferentstudysettings.First,specificcautionis Genomics Viewer (IGV) [76] (Figure S1a in Additional
neededwithallthemethodswhenthenumberofreplicate file 1), Genome Maps [77], or Savant [78]. Some
visualization tools are specifically designed for visualiz-
samplesisverysmallorforgenesthatareexpressedatverylow
ing multiple RNA-seq samples, such as RNAseqViewer
levels[55,64,209].Amongthetools,limmahasbeenshownto
[79], which provides flexible ways to display the read
performwellundermanycircumstancesanditisalsothefastestto
abundances on exons, transcripts and junctions. Introns
run[56,63,64].DESeqandedgeRperformsimilarlyinrankinggenes
can be hidden to better display signals on the exons, and
butareoftenrelativelyconservativeortooliberal,respectively,in the heatmaps can help the visual comparison of signals
controllingFDR[63,209,210].SAMseqperformswellintermsof on multiple samples (Figure S1b, c in Additional file 1).
FDRbutpresentsanacceptablesensitivitywhenthenumberof However,RNAseqViewer isslowerthanIGV.
replicatesisrelativelyhigh,atleast10[20,55,209].NOISeqand Some of the software packages for differential gene ex-
pression analysis (such as DESeq2 or DEXseq in Biocon-
NOISeqBIO(theadaptationofNOISeqforbiologicalreplication)
ductor) have functions to enable the visualization of
aremoreefficientinavoidingfalsepositivecallsatthecostof
results, whereas others have been developed for
somesensitivitybutperformwellwithdifferentnumbersof
visualization-exclusive purposes, such as CummeRbund
replicates[10,20,212].CuffdiffandCuffdiff2haveperformed
(for CuffDiff [66]) or Sashimi plots, which can be used
surprisinglypoorlyinthecomparisons[56,63].Thisprobably to visualize differentially spliced exons [80]. The advan-
reflectsthefactthatdetectingdifferentialexpressionatthe tage of Sashimi plots is that their display of junction
transcriptlevelremainschallengingandinvolvesuncertaintiesin reads is more intuitive and aesthetically pleasing when
assigningthereadstoalternativeisoforms.Inarecentcomparison, the number of samples is small (Figure S1d in Add-
itional file 1). Sashimi, structure, and hive plots for spli-
BitSeqcomparedfavorablytoothertranscript-levelpackagessuch
cing quantitative trait loci (sQTL) can be obtained using
asCuffdiff2[196].Besidestheactualperformance,otherissues
SplicePlot [81]. Splice graphs can be produced using
affectingthechoiceofthetoolincludeeaseofinstallationand
SpliceSeq[82],andSplicingViewer [83]plotssplice junc-
use,computationalrequirements,andqualityofdocumentation
tions and alternative splicing events. TraV [84] is a
andinstructions.Finally,animportantconsiderationwhenchoosing visualization tool that integrates data analysis, but its
ananalysismethodistheexperimentaldesign.Whilesomeofthe analyticalmethodsarenotapplicabletolargegenomes.
differentialexpressiontoolscanonlyperformapair-wisecomparison, Owing to the complexity of transcriptomes, efficient
otherssuchasedgeR[57],limma-voom[55],DESeq[48],DESeq2 display of multiple layers of information is still a chal-
lenge. All of the tools are evolving rapidly and we can
[58],andmaSigPro[213]canperformmultiplecomparisons,
expect more comprehensive tools with desirable features
includedifferentcovariatesoranalyzetime-seriesdata.
to be available soon. Nevertheless, the existing tools are
of great value for exploring results for individual genes
Conesaetal.GenomeBiology (2016) 17:13 Page10of19
of biological interest to assess whether particular ana- alternative splicing between adjacent genes. Where
lyses’ results can withstand detailed scrutiny or to reveal possible, fusions should be filtered by their presence in
potential complications caused by artifacts, such as 3’ a set of control datasets [87]. When control datasets
biases or complicated transcript structures. Users should are not available, artifacts can be identified by their
visualize changes in read coverage for genes that are presence in a large number of unrelated datasets, after
deemed important or interesting on the basis of their excludingthepossibilitythattheyrepresenttruerecur-
analysis results to evaluate the robustness of their rentfusions[90,91].
conclusions. Strong fusion-sequence predictions are characterized
by distinct subsequences that each align with high speci-
Genefusiondiscovery ficity to one of the fused genes. As alignment specificity
The discovery of fused genes that can arise from is highly correlated with sequence length, a strong pre-
chromosomal rearrangements is analogous to novel iso- diction sequence is longer, with longer subsequences
form discovery, with the added challenge of a much lar- fromeachgene.Longerreadsandlarger insert sizespro-
ger search space as we can no longer assume that the duce longer predicted sequences; thus, we recommend
transcript segments are co-linear on a single chromo- PE RNA-seq data with larger insert size over SE datasets
some. Artifacts are common even using state-of-the-art or datasets with short insert size. Another indicator of
tools, which necessitates post-processing using heuristic prediction strength is splicing. For most known fusions,
filters [85]. Artifacts primarily result from misalignment the genomic breakpoint is located in an intron of each
ofreadsequences dueto polymorphisms,homology, and gene [92] and the fusion boundary coincides with a
sequencing errors. Families of homologous genes, and splice site within each gene. Furthermore, fusion iso-
highly polymorphic genes such as the HLA genes, pro- forms generally follow the splicing patterns of wild-type
duce reads that cannot be easily mapped uniquely to genes. Thus, high confidence predictions have fusion
their location of origin in the reference genome. For boundaries coincident with exon boundaries and exons
genes with very high expression, the small but non- matching wild-type exons [91]. Fusion discovery tools
negligible sequencing error rate of RNA-seq will pro- often incorporate some of the aforementioned ideas to
duce reads that map incorrectly to homologous loci. rank fusion predictions [93, 94], though most studies
Filtering highly polymorphic genes and pairs of homolo- apply additional custom heuristic filters to produce a list
gous genes is recommended [86, 87]. Also recom- of high-quality fusion candidates [90,91,95].
mended is the filtering of highly expressed genes that
are unlikely to be involved in gene fusions, such as ribo- SmallRNAs
somal RNA [86]. Finally, a low ratio of chimeric to wild- Next-generation sequencing represents an increasingly
type reads in the vicinity of the fusion boundary may in- popular method to address questions concerning the
dicate spurious mis-mapping of reads from a highly biological roles of small RNAs (sRNAs). sRNAs are usu-
expressed gene (the transcript allele fraction described ally 18–34 nucleotides in length, and they include miR-
byYoshihara et al.[87]). NAs, short-interfering RNAs (siRNAs), PIWI-interacting
Given successful prediction of chimeric sequences, the RNAs (piRNAs), and other classes of regulatory mole-
next step is the prioritization of gene fusions that have cules. sRNA-seq libraries are rarely sequenced as deeply
biological impact over more expected forms of genomic as regular RNA-seq libraries because of a lack of com-
variation. Examples of expected variation include plexity, with a typical range of 2–10 million reads. Bio-
immunoglobulin (IG) rearrangements in tumor samples informatics analysis of sRNA-seq data differs from
infiltrated by immune cells, transiently expressed trans- standard RNA-seq protocols (Fig. 1c). Ligated adaptor
posons and nuclear mitochondrial DNA, and read- sequences are first trimmed and the resulting read-
through chimeras produced by co-transcription of adja- length distribution is computed. In animals, there are
cent genes [88]. Care must be taken with filtering in usually peaks for 22 and 23 nucleotides, whereas in
order not to lose events of interest. For example, remov- plants there are peaks for 21- and 24-nucleotide redun-
ing all fusions involving an IG gene may remove real IG dant reads. For instance, miRTools 2.0 [96], a tool for
fusions in lymphomas and other blood disorders; filter- prediction and profiling of sRNA species, uses by default
ing fusions for which both genes are from the IG locus reads that are 18–30 bases long. The threshold value de-
is preferred [88]. Transiently expressed genomic break- pends on the application, and in case of miRNAs is usu-
point sequences that are associated with real gene fu- allyintherangeof19–25nucleotides.
sions often overlap transposons; these should be filtered As in standard RNA-seq, sRNA reads must then be
unless they are associated with additional fusion iso- aligned to a reference genome or transcriptome se-
forms from the same gene pair [89]. Read-through chi- quences using standard tools, such as Bowtie2 [97],
meras are easily identified as predictions involving STAR [15], or Burrows-Wheeler Aligner (BWA) [98].
Conesaetal.GenomeBiology (2016) 17:13 Page11of19
There are, however, some aligners (such as PatMaN [99] transcriptome assembly or reconstruction would lack at
and MicroRazerS [100]) that have been designed to map least some functional information and therefore annota-
short sequences with preset parameter value ranges tion is necessary for functional profiling of those results.
suited for optimal alignment of short reads. The map- Protein-coding transcripts can be functionally annotated
ping itself may be performed with or without mis- using orthology by searching for similar sequences in
matches, the latter being used more commonly. In protein databases such as SwissProt [114] and in data-
addition, reads that map beyond a predetermined set bases that contain conserved protein domains such as
number of locations may be removed as putatively ori- Pfam [115] and InterPro [116]. The use of standard vo-
ginating from repetitive elements. In the case of miR- cabularies such as the Gene Ontology (GO) allows for
NAs, usually 5–20 distinct mappings per genome are some exchangeability of functional information across
allowed. sRNA reads are then simply counted to obtain orthologs. Popular tools such as Blast2GO [117] allow
expression values. However, users should also verify that massive annotation of complete transcriptome datasets
their sRNA reads are not significantly contaminated by against a variety of databases and controlled vocabular-
degraded mRNA, for example, by checking whether a ies. Typically, between 50 and 80 % of the transcripts re-
miRNA libraryshowsunexpected readcoverageover the constructed from RNA-seq data can be annotated with
body of highly expressed genes such as GAPDH or functional terms in this way. However, RNA-seq data
ACTB. also reveal that an important fraction of the transcrip-
Further analysis steps include comparison with known tome is lacking protein-coding potential. The functional
sRNAs and de novo identification of sRNAs. There are annotationoftheselongnon-codingRNAsismore chal-
class-specific tools for this purpose, such as miRDeep lenging as their conservation is often less pronounced
[101] and miRDeep-P [102] for animal and plant miR- than that of protein-coding genes. The Rfam database
NAs, respectively, or the trans-acting siRNA prediction [118] contains most well-characterized RNA families,
tool at the UEA sRNA Workbench [103]. Tools such as such asribosomalor transferRNAs,while mirBase[119]
miRTools 2.0 [96], ShortStack [104], and iMir [105] also or Miranda [120] are specialized in miRNAs. These re-
exist for comprehensive annotation of sRNA libraries sources can be used for similarity-based annotation of
andforidentificationofdiverse classesofsRNAs. short non-coding RNAs, but no standard functional an-
notation procedures are available yet for other RNA
FunctionalprofilingwithRNA-seq types suchasthelongnon-codingRNAs.
Thelaststepinastandardtranscriptomicsstudy(Fig.1b)
is often the characterization of the molecular functions Integration with other data types
or pathways in which differentially expressed genes The integration of RNA-seq data with other types of
(DEGs) are involved. The two main approaches to func- genome-wide data (Fig. 1c) allows us to connect the
tional characterization that were developed first for regulation of gene expression with specific aspects of
microarray technology are (a) comparing a list of DEGs molecular physiology and functional genomics. Integra-
against the rest of the genome for overrepresented func- tive analyses that incorporate RNA-seq data as the pri-
tions, and (b) gene set enrichment analysis (GSEA), mary gene expression readout that is compared with
which is based on ranking the transcriptome according other genomic experiments are becoming increasingly
to a measurement of differential expression. RNA-seq prevalent. Below, we discuss some oftheadditional chal-
biases such as gene length complicate the direct applica- lengesposedbysuch analyses.
tions of these methods for count data and hence RNA-
seq-specific tools have been proposed. For example, DNAsequencing
GOseq[106]estimatesabiaseffect(suchasgenelength) The combination of RNA and DNA sequencing can be
on differential expression results and adapts the trad- usedforseveralpurposes,suchassinglenucleotidepoly-
itional hypergeometric statistic used in the functional morphism (SNP) discovery, RNA-editing analyses, or ex-
enrichment test to account for this bias. Similarly, the pression quantitative trait loci (eQTL) mapping. In a
Gene Set Variation Analysis (GSVA) [107] or SeqGSEA typical eQTL experiment, genotype and transcriptome
[108] packages also combine splicing and implement en- profiles are obtained from the same tissue type across a
richmentanalyses similar toGSEA. relatively large number of individuals (>50) and correla-
Functional analysis requires the availability of suffi- tions between genotype and expression levels are then
cient functional annotation data for the transcriptome detected. These associations can unravel the genetic
under study. Resources such as Gene Ontology [109], basis of complex traits such as height [121], disease sus-
Bioconductor [110], DAVID [111, 112] or Babelomics ceptibility [122] or even features of genome architecture
[113] contain annotation data for most model species. [123, 124]. Large eQTL studies have shown that genetic
However, novel transcripts discovered during de novo variationaffectstheexpressionofmostgenes[125–128].
Conesaetal.GenomeBiology (2016) 17:13 Page12of19
RNA-seq has two major advantages over array-based verifying the expression status of genes that overlap
technologies for detecting eQTLs. First, it can identify a region of interest [150]. DNase-seq can be used for
variants that affect transcript processing. Second, reads genome-wide footprinting of DNA-binding factors,
that overlap heterozygous SNPs can be mapped to ma- and this in combination with the actual expression
ternal and paternal chromosomes, enabling quantifica- of genes can be used to infer active transcriptional
tion of allele-specific expression within an individual networks [150].
[129]. Allele-specific signals provide additional informa-
tion about a genetic effect on transcription, and a num- MicroRNAs
ber of computational methods have recently become Integration of RNA-seq and miRNA-seq data has the
available that leverage these signals to boost power for potential to unravel the regulatory effects of miRNAs on
association mapping [130–132]. One challenge of this transcript steady-state levels. Thisanalysisischallenging,
approach is the computational burden, as billions of however, because of the very noisy nature of miRNA
gene–SNP associations need to be tested; bootstrapping target predictions, which hampers analyses based on
or permutation-based approaches [133] are frequently correlations between miRNAs and their target genes.
used [134, 135]. Many studies have focused on testing Associations might be found in databases such as mir-
only SNPs in the cis region surrounding the gene in Walk [151] and miRBase [152] that offer target predic-
question, and computationally efficient approaches have tion according to various algorithms. Tools such as
been developed recently to allow extremely swift map- CORNA [153], MMIA [154, 155], MAGIA [156], and
ping of eQTLs genome-wide [136]. Moreover, the com- SePIA [157] refine predictions by testing for significant
bination of RNA-seq and re-sequencing can be used associations between genes, miRNAs, pathways and GO
both to remove false positives when inferring fusion terms, or by testing the relatedness or anticorrelation of
genes[88]andtoanalyze copy number alterations[137]. the expression profiles of both the target genes and the
associated miRNAs. In general, we recommend using
DNAmethylation miRNA–mRNA associations that are predicted by sev-
Pairwise DNA-methylation and RNA-seq integration, for eral algorithms. For example, in mouse, we found that
the most part,hasconsisted ofthe analysis ofthe correl- requiring miRNA–mRNA association in five databases
ation between DEGs and methylation patterns [138– resulted in about 50 target mRNA predictions per
140]. General linear models [141–143], logistic regres- miRNA (STATegraobservations).
sion models [143] and empirical Bayes model [144] have
been attempted among other modeling approaches. The Proteomicsandmetabolomics
statistically significant correlations that were observed, Integration of RNA-seq with proteomics is controversial
however, accounted for relatively small effects. An inter- because the two measurements show generally low cor-
esting shift away from focusing on individual gene–CpG relation (~0.40 [158, 159]). Nevertheless, pairwise inte-
methylation correlations is to use a network-interaction- gration of proteomics and RNA-seq can be used to
based approach to analyze RNA-seq in relation to DNA identify novel isoforms. Unreported peptides can be pre-
methylation. This approach identifies one or more sets dictedfromRNA-seqdataandthenusedtocomplement
of genes (also called modules) that have coordinated dif- databases normally queried in mass spectrometry as
ferentialexpression anddifferential methylation[145]. done by Low et al. [160]. Furthermore, post-translational
editing events may be identified if peptides that are
Chromatinfeatures present in the mass spectrometry analysis are absent
The combination of RNA-seq and transcription factor from the expressed genes of the RNA-seq dataset. Inte-
(TF) chromatin immunoprecipitation sequencing (ChIP- gration of transcriptomics with metabolomics data has
seq) data can be used to remove false positives in ChIP- been usedto identifypathways that areregulated atboth
seq analysis and to suggest the activating or repressive the gene expression and the metabolite level, and tools
effect of a TF on its target genes. For example, BETA are available that visualize results within the pathway
[146] uses differential gene expression in combination context (MassTRIX [161], Paintomics [162], VANTED
with peaks from ChIP-seq experiments to call TF tar- v2[163],andSteinerNet[164]).
gets. In addition, ChIP-seq experiments involving his-
tone modifications have been used to understand the Integrationandvisualizationofmultipledatatypes
general role of these epigenomic changes on gene ex- Integration of more than two genomic data types is still
pression [147, 148]. Other RNA-ChIP-sequencing inte- atitsinfancyandnotyetextensivelyappliedtofunctional
grative approaches are reviewed in [149]. Integration of sequencing techniques, but there are already some tools
open chromatin data such as that from FAIRE-seq and that combine several data types. SNMNMF [165] and
DNase-seq with RNA-seq has mostly been limited to PIMiM [166] combine mRNA and miRNA expression
Conesaetal.GenomeBiology (2016) 17:13 Page13of19
data with protein–protein, DNA–protein, and miRNA– justa single cell.Theresultingsingle-cell libraries enable
mRNA interaction networks to identify miRNA–gene the identification of new, uncharacterized cell types in
regulatory modules. MONA [167] combines different tissues.Theyalso makeit possible to measurea fascinat-
levels of functional genomics data, including mRNA, ing phenomenon in molecular biology, the stochasticity
miRNA, DNA methylation, and proteomics data to dis- of gene expression in otherwise identical cells within a
cover altered biological functions in the samples being defined population. In this context, single cell studies
studied. Paintomics can integrate any type of functional are meaningful only when a set of individual cell librar-
genomics data into pathway analysis, provided that the ies are compared with the cell population, with the aim
features can be mapped onto genes or metabolites [162]. of identifying subgroups of multiple cells with distinct
3Omics [168] integrates transcriptomics, metabolomics combinations of expressed genes. Differences may be due
andproteomicsdataintoregulatorynetworks. to naturally occurring factors such as stage of the cell
In all cases, integration of different datasets is rarely cycle, or may reflect rare cell types such as cancer stem
straightforwardbecauseeachdatatypeisanalyzedsepar- cells. Recent rapid progress in methodologies for single-
ately with its own tailored algorithms that yield results cell preparation, including the availability of single-cell
in different formats. Tools that facilitate format conver- platforms such as the Fluidigm C1 [8], has increased the
sions and the extraction of relevant results can help; ex- numberofindividualcellsanalyzedfromahandfulto50–
amples of such workflow construction software packages 90perconditionupto800cellsatatime.Othermethods,
include Anduril [169], Galaxy [170] and Chipster [171]. such as DROP-seq [175], can profile more than 10,000
Anduril was developed for building complex pipelines cellsatatime.Thisincreasednumberofsingle-celllibrar-
with large datasets that require automated parallelization. iesineachexperimentdirectlyallowsfortheidentification
The strength of Galaxy and Chipster is their usability; ofsmallersubgroupswithinthepopulation.
visualizationisakeycomponentoftheirdesign.Simultan- The small amount of starting material and the PCR
eous or integrative visualization of the data in a genome amplification limit the depth to which single-cell librar-
browser is extremely useful for both data exploration and ies can be sequenced productively, often to less than a
interpretation of results. Browsers can display in tandem million reads. Deeper sequencing for scRNA-seq will do
mappings from most next-generation sequencing tech- little to improve quantificationas the number of individ-
nologies,whileaddingcustomtrackssuchasgeneannota- ual mRNA molecules in a cell is small (in the order of
tion, nucleotide variation or ENCODE datasets. For 100–300,000 transcripts) and only a fraction of them are
proteomics integration, the PG Nexus pipeline [172] con- successfully reverse-transcribed to cDNA [8, 176]; but
verts mass spectrometry data to mappings that are co- deeper sequencing is potentially useful for discovering
visualizedwithRNA-seqalignments. and measuring allele-specific expression, as additional
reads couldprovideusefulevidence.
Outlook Single-cell transcriptomes typically include about
RNA-seqhasbecomethestandardmethodfortranscrip- 3000–8000 expressed genes, which is far fewer than are
tome analysis, but the technology and tools are continu- counted in the transcriptomes of the corresponding
ing to evolve. It should be noted that the agreement pooled populations. The challenge is to distinguish the
between results obtained from different tools is still un- technical noise that results from a lack of sensitivity at
satisfactory and that results are affected by parameter the single-molecule level [173] (where capture rates of
settings, especially for genes that are expressed at low around 10–50 % result in the frequent loss of the most
levels. The two major highlights in the current applica- lowly expressed transcripts) from true biological noise
tion of RNA-seq are the construction of transcriptomes where a transcript might not be transcribed and present
from small amounts of starting materials and better inthe cellfor acertainamountof time while the protein
transcript identification from longer reads. The state of is still present. The inclusion of added reference tran-
the art in both of these areas is changing rapidly, but we scripts and the use of unique molecule identifiers
will briefly outline what can be done now and what can (UMIs) have been applied to overcome amplification
beexpected inthenearfuture. bias and to improve gene quantification [177, 178].
Methods that can quantify gene-level technical variation
Single-cellRNA-seq allow us to focus on biological variation that is likely to
Single-cell RNA-seq (scRNA-seq) is one of the newest be of interest [179]. Typical quality-control steps involve
and most active fields of RNA-seq with its unique set of setting aside libraries that contain few reads, libraries
opportunities and challenges. Newer protocols such as that have a low mapping rate, and libraries that have
Smart-seq [173] and Smart-seq2 [174] have enabled us zero expression levels for housekeeping genes, such as
to work from very small amounts of starting mRNA GAPDH and ACTB, that are expected to be expressed at
that, with proper amplification, can be obtained from adetectablelevel.
Conesaetal.GenomeBiology (2016) 17:13 Page14of19
Depending on the chosen single-cell protocol and the [186], and for determining allele-specific expression
aims of the experiment, different bulk RNA-seq pipe- from single reads [187]. Nevertheless, long-read sequen-
lines and tools can be used for different stages of the cing has its own set of limitations, such as a still high
analysis as reviewed by Stegle et al. [180]. Single-cell li- error rate that limits de novo transcript identifications
braries are typically analyzed by mapping to a reference and forces the technology to leverage the reference gen-
transcriptome (using a program such as RSEM) without ome [188]. Moreover, the relatively low throughput of
any attempt at new transcript discovery, although at SMRTcells hampers the quantification of transcript ex-
least one package maps to the genome (Monocle [181]). pression. These two limitations can be addressed by
While mapping onto the genome does result in a higher matching PacBio experiments with regular, short-read
overall read-mapping rate, studies that are focused on RNA-seq. The accurate and abundant Illumina reads
gene expression alone with fewer reads per cell tend to can be used both to correct long-read sequencing errors
use mapping to the reference transcriptome for the sake andtoquantifytranscriptlevels[189].UpdatesinPacBio
of simplicity. Other single-cell methods have been devel- chemistry are increasing sequencing lengths to produce
oped to measure single-cell DNA methylation [182] and reads with a sufficient number of passes over the
single-cell open chromatin using ATAC-seq [183, 184]. cDNAmoleculeto autocorrect sequencing errors. This
Atpresent,we canmeasureonlyonefunctional genomic will eventually improve sequencing accuracy and allow
data-type at a time in the same single cell, but we can for genome-free determination of isoform-resolved
expect that in the near future we will be able to recover transcriptomes.
the transcriptome of a single cell simultaneously with
additionalfunctionaldata. Additional file
Long-readsequencing Additionalfile1:FigureS1.ScreenshotsofRNA-seqdatavisualization.
The major limitation of short-read RNA-seq is the diffi- aIntegrativeGenomicsViewer(IGV)[77]displayofagenedetectedas
differentiallyexpressedbetweenthetwogroupsofsamplesbyDEGseq
culty in accurately reconstructing expressed full-length
[62].Thebottomtrackintherightpanelisthegeneannotation.The
transcripts from the assembly of reads. This is particu- tracksarefivesamplesfromeachgroup.bRNAseqViewer[80]displayof
larly complicated in complex transcriptomes, where dif- thesamedataasin(a).cRNAseqViewerheatmapdisplayofagene
detectedasdifferentiallysplicedbetweentwogroupsbybothDSGSeq
ferent but highly similar isoforms of the same gene are
[70]andDEXSeq[69].Intronsarehiddeninthedisplaytoemphasizethe
expressed, and for genes that have many exons and pos- signalsontheexons.dMISO[81]displayofanothergenedetectedas
sible alternative promoters or 3’ ends. Long-read tech- differentiallyspliced,withjunctionreadsillustrated.(PDF1152kb)
nologies, such as Pacific-Biosciences (PacBio) SMRTand
Oxford Nanopore, that were initially applied to genome Abbreviations
ASM:Alternativesplicingmodule;ChIP-seq:Chromatinimmunoprecipitation
sequencing are now being used for transcriptomics and
sequencing;DEG:Differentiallyexpressedgenes;eQTL:Expression
have the potential to overcome this assembly problem. quantitativeloci;FDR:Falsediscoveryrate;FPKM:Fragmentsperkilobaseof
Long-read sequencing provides amplification-free, single- exonmodelpermillionmappedreads;GO:GeneOntology;GSEA:Geneset
enrichmentanalysis;GTF:Genetransferformat;IG:Immunoglobulin;
molecule sequencing of cDNAs that enables recovery of
IGV:IntegrativeGenomicsViewer;miRNA:MicroRNA;mRNA:Messenger
full-length transcripts without the need for an assembly RNA;PCA:Principalcomponentanalysis;PEread:Paired-endread;
step.PacBioaddsadapterstothecDNAmoleculeandcre- RNA-seq:RNA-sequencing;RPKM:Readsperkilobaseofexonmodelper
millionreads;rRNA:RibosomalRNA;RSEM:RNA-SeqbyExpectation
ates a circularized structure that can be sequenced with
Maximization;scRNA-seq:Single-cellRNA-seq;SEread:Single-endread;
multiple passes within one single long read. The Nano- siRNA:Short-interferingRNA;SNP:Singlenucleotidepolymorphism;
pore GridION system can directly sequence RNA strands sQTL:Splicingquantitativetraitloci;sRNA:SmallRNA;TF:Transcription
factor;TPM:Transcriptspermillion.
by using RNA processive enzymes and RNA-specific
bases. Another interesting technology was previously Competinginterests
known as Moleculo (now Illumina’s TruSeq synthetic Theauthorsdeclarethattheyhavenocompetinginterests.
long-read technology), where Illumina library preparation Authors’contributions
is multiplexed and restricted to a limited number of long ACo,PMandAMconceivedtheideaandshapedthestructureofthe
DNA molecules that are separately bar-coded and pooled manuscript.ACodraftedtheexperimentaldesign,alignmentandfunctional
profilingsectionsandintegratedcontributionsfromallauthors.PMdrafted
back for sequencing. As one barcode corresponds to a
thevisualizationanddenovotranscriptreconstructionsections,and
limited number of molecules, assembly is greatly simpli- coordinatedauthorcontributions.STdraftedthequality-controlanddifferential
fied and unambiguous reconstruction to long contigs is expressionsections.DGCdraftedtheexperimentaldesignandintegration
sections.ACecontributedtodraftingtheintegrationsection.AMPdraftedthe
possible. This approach has recently been published for
transcriptfusionsection.MWSdraftedthesmallRNAsection.DGdraftedthe
RNA-seqanalysis[185]. eQTLsection.LLEdraftedthesoftwarecomparisonfordifferentialexpression
PacBio RNA-seq is the long-read approach with the section.LLEandXZdraftedthetranscriptisoformanalysissections.XZcontributed
todraftingthevisualizationsection.AMdraftedtheintroductionandoutlook
most publications to date. The technology has proven
sectionsandgloballyeditedthemanuscript.Allauthorsreadandapprovedthe
useful for unraveling isoform diversity at complex loci finalmanuscript.
Conesaetal.GenomeBiology (2016) 17:13 Page15of19
Acknowledgements 10. TarazonaS,Garcia-AlcaldeF,DopazoJ,FerrerA,ConesaA.Differential
TheauthorswouldliketothankMichaelLoveandHaroldPimentelfor expressioninRNA-seq:amatterofdepth.GenomeRes.2011;21:2213–23.
helpfulsuggestionsontheinitialdraftofthemanuscript.AC,ST,AM,DGC 11. AndrewsS.FASTQC.Aqualitycontroltoolforhighthroughputsequence
weresupportedbytheFP7STATegraproject(grant36000).ResearchinAC’s data.http://www.bioinformatics.babraham.ac.uk/projects/fastqc/.Accessed
laboratorywassupportedbyMINECOgrantBIO2012-40244andco-funded 29September2014.
withEuropeanRegionalDevelopmentFunds(ERDF).ResearchinPM’s 12. DaiM,ThompsonRC,MaherC,Contreras-GalindoR,KaplanMH,Markovitz
laboratoryissupportedbyERCstartinggrantRelieve-IMDsandbyacore DM,etal.NGSQC:cross-platformqualityanalysispipelinefordeep
supportgrantfromtheWellcomeTrustandMRCtotheWellcomeTrust- sequencingdata.BMCGenomics.2010;11Suppl4:S7.
MedicalResearchCouncilCambridgeStemCellInstitute.XZwassupported 13. FASTX-Toolkit.http://hannonlab.cshl.edu/fastx_toolkit/. Accessed12
bytheNationalBasicResearchProgramofChina(2012CB316504).LLEwas January2016.
supportedbyJDRF(grantnumber2-2013-32)andbytheSigridJuselius 14. BolgerAM,LohseM,UsadelB.Trimmomatic:aflexibletrimmerforIllumina
Foundation. ACewassupportedby theAcademyofFinland(Centerof sequencedata.Bioinformatics.2014;30:2114–20.
ExcellenceinCancerGeneticsResearch). 15. DobinA,DavisCA,SchlesingerF,DrenkowJ,ZaleskiC,JhaS,etal.STAR:
ultrafastuniversalRNA-seqaligner.Bioinformatics.2013;29:15–21.
Authordetails 16. Picard.http://picard.sourceforge.net/.Accessed12January2016.
1InstituteforFoodandAgriculturalSciences,DepartmentofMicrobiology 17. WangL,WangS,LiW.RSeQC:qualitycontrolofRNA-seqexperiments.
andCellScience,UniversityofFlorida,Gainesville,FL32603,USA.2Centrode Bioinformatics.2012;28:2184–5.
InvestigaciónPríncipeFelipe,GenomicsofGeneExpressionLaboratory, 18. García-AlcaldeF,OkonechnikovK,CarbonellJ,CruzLM,GötzS,TarazonaS,
46012Valencia,Spain.3WellcomeTrustSangerInstitute,WellcomeTrust
etal.Qualimap:evaluatingnext-generationsequencingalignmentdata.
GenomeCampus,Hinxton,CambridgeCB101SA,UK.4Wellcome Bioinformatics.2012;28:2678–9.
Trust-MedicalResearchCouncilCambridgeStemCellInstitute,AnneMcLaren 19. TarazonaS,Furió-TaríP,TurràD,PietroAD,NuedaMJ,FerrerA,etal.Data
LaboratoryforRegenerativeMedicine,DepartmentofSurgery,Universityof qualityawareanalysisofdifferentialexpressioninRNA-seqwithNOISeq
Cambridge,CambridgeCB20SZ,UK.5DepartmentofAppliedStatistics,
R/Biocpackage.NucleicAcidsRes.2015;43:e140.
OperationsResearchandQuality,UniversidadPolitécnicadeValencia,46020 20. RissoD,SchwartzK,SherlockG,DudoitS.GC-contentnormalizationfor
Valencia,Spain.6UnitofComputationalMedicine,DepartmentofMedicine,
RNA-seqdata.BMCBioinformatics.2011;12:480.
KarolinskaInstitutet,KarolinskaUniversityHospital,17177Stockholm, 21. SteijgerT,AbrilJF,EngströmPG,KokocinskiF,HubbardTJ,GuigóR,etal.
Sweden.7CenterforMolecularMedicine,KarolinskaInstitutet,17177
AssessmentoftranscriptreconstructionmethodsforRNA-seq.NatMethods.
Stockholm,Sweden.8UnitofClinicalEpidemiology,DepartmentofMedicine, 2013;10:1177–84.
KarolinskaUniversityHospital,L8,17176Stockholm,Sweden.9ScienceforLife
22. BoleyN,StoiberMH,BoothBW,WanKH,HoskinsRA,BickelPJ,etal.
Laboratory,17121Solna,Sweden.10SystemsBiologyLaboratory,Instituteof
Genome-guidedtranscriptassemblybyintegrativeanalysisofRNA
BiomedicineandGenome-ScaleBiologyResearchProgram,Universityof sequencedata.NatBiotechnol.2014;32:341–6.
Helsinki,00014Helsinki,Finland.11SchoolofComputingScience,Simon
23. RobertsA,PimentelH,TrapnellC,Pachter L.Identificationofnovel
FraserUniversity,BurnabyV5A1S6BC,Canada.12Departmentof
transcriptsinannotatedgenomesusingRNA-Seq. Bioinformatics.
Bioinformatics,InstituteofMolecularBiologyandBiotechnology,Adam 2011;27:2325–9.
MickiewiczUniversityinPoznań,61-614Poznań,Poland.13TurkuCentrefor
24. MezliniAM,SmithEJ,FiumeM,BuskeO,SavichGL,ShahS,etal.iReckon:
Biotechnology,UniversityofTurkuandÅboAkademiUniversity,FI-20520
simultaneousisoformdiscoveryandabundanceestimationfromRNA-seq
Turku,Finland.14KeyLabofBioinformatics/BioinformaticsDivision,TNLIST
data.GenomeRes.2013;23:519–29.
andDepartmentofAutomation,TsinghuaUniversity,Beijing100084,China.
25. LiJJ,JiangCR,BrownJB,HuangH,BickelPJ.Sparselinearmodelingof
15SchoolofLifeSciences,TsinghuaUniversity,Beijing100084,China.
next-generationmRNAsequencing(RNA-Seq)dataforisoformdiscovery
16DepartmentofDevelopmentalandCellBiology,UniversityofCalifornia,
andabundanceestimation.ProcNatlAcadSciUSA.2011;108:19867–72.
Irvine,Irvine,CA92697-2300,USA.17CenterforComplexBiologicalSystems,
26. PerteaM,PerteaGM,AntonescuCM,ChangTC,MendellJT,SalzbergSL.
UniversityofCalifornia,Irvine,Irvine,CA92697,USA.
StringTieenablesimprovedreconstructionofatranscriptomefromRNA-seq
reads.NatBiotechnol.2015;33:290–5.
27. HillerD,WongWH.Simultaneousisoformdiscoveryandquantificationfrom
RNA-Seq.StatBiosci.2013;5:100–18.
References 28. StankeM,KellerO,GunduzI,HayesA,WaackS,MorgensternB.AUGUSTUS:
1. MortazaviA,WilliamsBA,McCueK,SchaefferL,WoldB.Mappingand abinitiopredictionofalternativetranscripts.NucleicAcids Res.
quantifyingmammaliantranscriptomesbyRNA-Seq.NatMethods.2008;5:1–8. 2006;34:W435–9.
2. LevinJZ,YassourM,AdiconisX,NusbaumC,ThompsonDA,FriedmanN, 29. EngströmPG,SteijgerT,SiposB,GrantGR,KahlesA,RätschG,etal.
etal.Comprehensivecomparativeanalysisofstrand-specificRNA SystematicevaluationofsplicedalignmentprogramsforRNA-seqdata.Nat
sequencingmethods.NatMethods.2010;7:709–15. Methods.2013;10:1185–91.
3. ParkhomchukD,BorodinaT,AmstislavskiyV,BanaruM,HallenL,KrobitschS, 30. XieY,WuG,TangJ,LuoR,PattersonJ,LiuS,etal.SOAPdenovo-Trans:de
etal.Transcriptomeanalysisbystrand-specificsequencingof novotranscriptomeassemblywithshortRNA-Seqreads.Bioinformatics.
complementaryDNA.NucleicAcidsRes.2009;37:e123. 2014;30:1660–6.
4. KatzY,WangET,AiroldiEM,BurgeCB.AnalysisanddesignofRNAsequencing 31. SchulzMH,ZerbinoDR,VingronM,BirneyE.Oases:robustdenovoRNA-
experimentsforidentifyingisoformregulation.NatMethods.2010;7:1009–15. seqassemblyacrossthedynamicrangeofexpressionlevels.Bioinformatics.
5. GarberM,GrabherrMG,GuttmanM,TrapnellC.Computationalmethodsfor 2012;28:1086–92.
transcriptomeannotationandquantificationusingRNA-seq.NatMethods. 32. GrabherrMG,HaasBJ,YassourM,LevinJZ,ThompsonDA,AmitI,etal.
2011;8:469–77. Full-lengthtranscriptomeassemblyfromRNA-seqdatawithoutareference
6. ŁabajPP,LeparcGG,LinggiBE,MarkillieLM,WileyHS,KreilDP. genome.NatBiotechnol.2011;29:644–52.
CharacterizationandimprovementofRNA-Seqprecisioninquantitative 33. HaasBJ,PapanicolaouA,YassourM,GrabherrM,BloodPD,BowdenJ,etal.
transcriptexpressionprofiling.Bioinformatics.2011;27:i383–91. DenovotranscriptsequencereconstructionfromRNA-sequsingtheTrinity
7. SimsD,SudberyI,IlottNE,HegerA,PontingCP.Sequencingdepthandcoverage: platformforreferencegenerationandanalysis.NatProtoc.2013;8:1494–512.
keyconsiderationsingenomicanalyses.NatRevGenet.2014;15:121–32. 34. PatroR,MountSM,KingsfordC.Sailfishenablesalignment-freeisoform
8. PollenAA,NowakowskiTJ,ShugaJ,WangX,LeyratAA,LuiJH,etal.Low- quantificationfromRNA-seqreadsusinglightweightalgorithms.Nat
coveragesingle-cellmRNAsequencingrevealscellularheterogeneityand Biotechnol.2014;32:462–4.
activatedsignalingpathwaysindevelopingcerebralcortex.NatBiotechnol. 35. AndersS,PylPT,HuberW.HTSeq-aPythonframeworktoworkwith
2014;32:1053–8. high-throughputsequencingdata.Bioinformatics.2015;31:166–9.
9. JaitinDA,KenigsbergE,Keren-ShaulH,ElefantN,PaulF,ZaretskyI,etal. 36. LiaoY,SmythGK,ShiW.featureCounts:anefficientgeneralpurpose
Massivelyparallelsingle-cellRNA-seqformarker-freedecompositionof programforassigningsequencereadstogenomicfeatures.Bioinformatics.
tissuesintocelltypes.Science.2014;343:776–9. 2014;30:923–30.
