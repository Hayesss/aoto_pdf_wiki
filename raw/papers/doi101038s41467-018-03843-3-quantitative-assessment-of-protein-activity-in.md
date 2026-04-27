---
source_path: /mnt/c/Users/Administrator/Zotero/storage/CSHAK3WG/Ding - 2018 - Quantitative assessment of protein activity in orp.pdf
ingested: 2026-04-23
sha256: 21ed07fe366f74df
---

ARTICLE
OPEN
DOI:10.1038/s41467-018-03843-3
Quantitative assessment of protein activity in
orphan tissues and single cells using the
metaVIPER algorithm
Hongxu Ding1,2, Eugene F. DouglassJr.1, Adam M. Sonabend3, Angeliki Mela3, Sayantan Bose1,9,
Christian Gonzalez1,10, Peter D. Canoll3, Peter A. Sims1, Mariano J. Alvarez1,4 & Andrea Califano1,4,5,6,7,8
Weandothershaveshownthattransitionandmaintenanceofbiologicalstatesiscontrolled
bymasterregulatorproteins,whichcanbeinferredbyinterrogatingtissue-specificregulatory
models(interactomes)withtranscriptionalsignatures,usingtheVIPERalgorithm.Yet,some
tissuesmaylackmolecularprofilesnecessaryforinteractomeinference(orphantissues),or,
as for single cells isolated from heterogeneous samples, their tissue context may be unde-
termined.Toaddressthisproblem,weintroducemetaVIPER,analgorithmdesignedtoassess
proteinactivityin tissue-independent fashionbyintegrative analysisofmultiple, non-tissue-
matched interactomes. This assumes that transcriptional targets of each protein will be
recapitulated by one or more available interactomes. We confirm the algorithm’s value in
assessingproteindysregulationinducedbysomaticmutations,aswellasinassessingprotein
activityin orphan tissuesand, most critically, in singlecells, thusallowing transformation of
noisyandpotentiallybiasedRNA-Seqsignaturesintoreproducibleprotein-activitysignatures.
1DepartmentofSystemsBiology,ColumbiaUniversity,NewYork,NY10032,USA.2DepartmentofBiologicalSciences,ColumbiaUniversity,NewYork,NY
10027,USA.3DepartmentofPathologyandCellBiology,ColumbiaUniversity,NewYork,NY10032,USA.4DarwinHealthInc,NewYork,NY10032,USA.
5HerbertIrvingComprehensiveCancerCenter,ColumbiaUniversity,NewYork,NY10032,USA.6J.P.SulzbergerColumbiaGenomeCenter,Columbia
University,NewYork,NY10032,USA.7DepartmentofBiomedicalInformatics,ColumbiaUniversity,NewYork,NY10032,USA.8Departmentof
BiochemistryandMolecularBiophysics,ColumbiaUniversity,NewYork,NY10032,USA.9Presentaddress:GlaxoSmithKline,KingofPrussia,PA19406,
USA.10Presentaddress:AmsterdamNeuroscience,Amsterdam1081,TheNetherlands.Correspondenceandrequestsformaterialsshouldbeaddressedto
M.J.A.(email:malvarez@darwinhealth.com)ortoA.C.(email:andrea.califano@columbia.edu)
NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications 1
;,:)(0987654321
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
M
ostbiologicaleventsarecharacterizedbythetransition Supplementary Fig. 1 when a protein regulon is incorrectly
between two cellular states representing either two assessed for a specific tissue, it is not consistent with the tissue-
stable physiologic conditions, such as during lineage specific gene expression signature, thus producing no significant
specification1,2oraphysiologicalandapathologicalone,suchas enrichment. Taken together, these observations constitute the
during tumorigenesis3,4. In either case, cell state transitions are basisfortheimplementationofacontext-independentalgorithm
initiatedbyacoordinatedchangeintheactivityofkeyregulatory for protein activity assessment (metaVIPER).
proteins,typicallyorganizedintohighlyinterconnectedandauto- MetaVIPER implements a statistical framework for evidence
regulated modules, which are ultimately responsible for the integration across a large repertoire of context-specific inter-
maintenance of a stable endpoint state. We have used the term actomes, see Methods for details. The algorithm is based on the
“master regulator” (MR) to refer to the specific proteins, whose assumption that only regulons that accurately represent the
concertedactivityisnecessaryandsufficienttoimplementagiven transcriptionaltargetsofspecificproteinsinthetissueofinterest
cell state transition5. Critically, individual MR proteins can be will produce statistically significant enrichment in genes that are
systematicallyelucidated bycomputational analysisof regulatory differentially expressed in that tissue (Fig. 1a).
models (interactomes) using MARINa (Master Regulator Infer- To assess whether metaVIPER can effectively assess protein
encealgorithm)6and itsmostrecent implementationsupporting activity in context-independent fashion weperform a number of
individual sample analysis, VIPER (Virtual Inference of Protein distinct benchmarks.First,weassessedwhetherresultsproduced
activity by Enriched Regulon)7. These algorithms prioritize the by analysis of context-specific interactomes (e.g., inferred from
proteinsrepresentingthemostdirectmechanistic regulatorsof a breastcancersamples)couldbeeffectivelyreproducedwhenonly
cell state transition, by assessing the enrichment of their tran- interactomes from other tissues are used in integrative fashion.
scriptional targets in genes that are differentially expressed. For Wealsotestwhethertheabilitytoassessdysregulationofproteins
instance,aproteinwouldbeconsideredsignificantlyactivatedin whoseencodinggeneharboredarecurrentsomaticalterationwas
a cell-state transition if its positively regulated and repressed improvedbymetaVIPER.Finally,weassessthealgorithm’sability
targets were significantly enriched in overexpressed and under- totransformlow-depthsinglecellRNA-Seq(scRNA-Seq)profiles
expressed genes, respectively. The opposite would, of course, be into highly reproducible protein activity profiles that accurately
the case for an inactivated protein. As proposed in7, this reflect cell state, while removing technical artifacts and batch
enrichment can be effectively quantitated as Normalized effects, compared to state of the art gene expression based
Enrichment Score (NES) using the Kolmogorov–Smirnov statis- methods.Theseimprovementssignificantlyincreasetheabilityto
tics8.WehaveshownthattheNEScanthenbeeffectivelyusedas analyze the biological function and relevance of gene products
a proxy for the differential activity of a specific protein7. Criti- whose mRNAs are undetectable in low-depth, scRNA-Seq data
cally, such an approach requires accurate and comprehensive (dropout effect), without any a priori knowledge of the single
assessment of protein transcriptional targets. This can be cell’s lineage. In particular, it allows more stringent analysis of
accomplished using reverse-engineering algorithms, such as critical lineage markers, for which no mRNA reads may be
ARACNe9 (Accurate Reverse Engineering of Cellular Networks) detectable in individual cells, either individually or as a set,
and others (reviewed in ref. 10), as also discussed in ref. 7. supporting a “virtual FACS” analysis.
MARINa and VIPERhavehelped elucidate MRproteins for a
variety of tumor
related11–17, neurodegenerative18–20,
stem
cell21,22, developmental6, and neurobehavioral23 phenotypes that Results
have been experimentally validated. The dependency of this Overview of metaVIPER. Let us assume a tissue context T for
algorithm on availability of tissue-specific models, however, which a matched tissue-specific interactome was not available.
constitutes a significant limitation because use of non-tissue- Furthermore,withoutlossofgenerality,letusfocusonaspecific
matched interactomes severely compromises algorithm perfor- protein of interest P and on its T-specific regulon R . Given a
T
mance11. Since ARACNe requires N≥100 tissue-specific gene sufficient number of additional tissues T … T for which
1 N
expression profiles, representing statistically independent sam- accurate, context-specific interactomes are available, we hypo-
ples, some tissue contexts may lack adequate data for accurate thesize that R will be at least partially recapitulated in one or
T
interactome inference. These “orphan tissues” include, for more of them. Based on previous results7, VIPER can accurately
instance, rare or poorly characterized cancers, as well as pro- infer differential protein activity, as long as 40% or more of its
genitor states during lineage differentiation. In addition, the transcriptional targets are correctly identified. As a result, even
specific tissue lineage of a sample may be poorly defined, thus partial regulon overlap may suffice. Indeed, paradoxically, there
preventing selection of appropriate interactome models. Con- are cases where a protein’s regulon may be more accurately
sider, for instance, a single cell isolated from a heterogeneous represented in a non-tissue matched interactome than in the
sample, such as whole brain or stroma-infiltrated tumor, where tissue-specificone.Thismayoccur,forinstance,whenexpression
many highly distinct and often uncharacterized cell lineages are of the gene encoding for the protein of interest has little varia-
inextricably commingled. bility in the tissue of interest and greater variability in a distinct
To address this challenge, we reasoned that while regulatory tissue context where the targets are relatively well conserved. A
models are clearly lineage specific, due to the distinct epigenetic keychallenge,however,isthatonedoesnotknowaprioriwhich
state of the cells, the transcriptional targets of a specific protein of the tissue-specific interactomes may provide reasonable vs.
(i.e.,itsregulon)maybeatleastpartiallyconservedacrossasmall poor models for R .
T
subset of distinct lineages. Thus, once a sufficient number of Toaddressthischallenge,weleveragepreviousstudiesshowing
tissue-specificinteractomesisavailable,thelikelihoodthatoneor that if an interactome-specific regulon provides poor R
T
more of them may represent a good model for the regulon of a representation, approaching random selection in the limit, then
specificproteinincreases,eventhoughonemaynotknowapriori it willalsonotbestatistically significantlyenrichedingenes that
which model may represent the best match for each protein. aredifferentiallyexpressedinatissue-specificsignatureS .Thus,
T
Indeed, the regulons of different proteins may be optimally if one were to compute the enrichment of all available regulons
represented within different interactomes. This is further helped fortheproteinPinthesignatureS ,onlythoseprovidingagood
T
by the fact that VIPER analysis is robust if at least 40% of a representation willproduce statisticallysignificantenrichment,if
protein’sregulonisaccuratelyinferred7.Conversely,asshownin Pisdifferentiallyactiveinthetissueofinterest.Conversely,ifthe
2 NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications
a b
BRCA
c
protein is not differentially active in T, then no regulon R … To objectively evaluate the performance of these alternative
T1
R should produce statistically significant enrichment. If these integrative methods, we considered a comprehensive set of
TN
assumptions were correct, given a sufficient number of tissue- proteins, whose genes harbor recurrent somatic mutations, as
specific interactomes, this would provide an efficient way to reported by both TCGA and COSMIC (see Methods). These
integrate across them to compute the differential activity of mutations drive tumorigenesis by altering the activity of key
arbitrary proteins in tissue contexts for which a suitable oncogenesandtumorsuppressorsandhavebeenusedtoidentify
interactome model may be missing. proteinsfortargetedinhibitors,basedontheoncogeneadditional
To determine the best strategy for integrating the statistics of paradigm25. We thus assessed method performance by assessing
the enrichment across multiple interactomes, we compared thestatisticalsignificanceofthecorrelationbetweenmetaVIPER-
several approaches. Specifically, for each protein, we first inferred protein activity and the presence of a recurrent genetic
computed enrichment using a tissue-matched interactome alterations in the corresponding gene locus (p<0.01), under the
(tissueMatch). This corresponds to the original implementation assumption that better methods would yield higher significance.
oftheVIPERalgorithm.Wethencomparedtheseresultstothose To produce an optimal metric across all recurrent mutational
obtained using different metrics to integrate across the regulons events, we assessed correlation as a function of recurrence
of all non-tissue-matched interactomes, including (a) the NES (Fig. 1b). Indeed, the more recurrent a mutation is, the more
with the most statistically significant absolute value (maxScore), likely it is to be functionally relevant and thus affect the
(b)theaverageofallNESscores(avgScore),and(c)theweighted- corresponding protein’s activity. Recurrence is reported as the
average of all NES scores, weighed by the NES absolute value numberofsamplesinTCGAandCOSMICwhereaspecificgene
(NESScore). For these tests, we used a total of 24 interactomes locus was mutated, see Methods. As shown in Fig. 1b, there is a
generated from TCGA cohorts, see Supplementary Table24. clear trend showing that the more recurrently mutated a gene
1XUC
RA
...
2BAG
BPBEC
maxScore
50
avgScore
0.9 0.54 2 3.7 NESScore
40 tissueMatch
randomMatch
30
stnatum
detceted
fo
noitcarF
CESC ... GBM UCEC
1.1 6.6 5.1 3.4
20
1 10
0
0 5 10 15 20 25 30
Mutated samples
snolugeR
1 5.5 2.8
0.15 0.097
Interactomes
1.0
0.9
0.8
0.7
)nosraeP(
r 0.6
0.5
DAER LMAL DAUL CSUL DATS DAOC CRAS CSEC ACSE DARP CSNH ACLB ACRB CECU CRIK MCKS ACHT MBG VO MYHT PRIK GPCP TCGT CHIL
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
6.8 0.22
All interactomes vs. non-matching interactomes
Fig.1InferringproteinactivitywithmetaVIPER.aOverviewofmetaVIPER.Thesetoftranscriptionaltargetsforeachregulatoryprotein(itsregulon)
constitutesthefundamentalbuildingblocksofaninteractome,whichreflectitsoverall,context-specificregulatorycontrolstructure.MetaVIPERidentifies
theregulonthatbestrecapitulatestheregulatorytargetsofaproteinbyassessingitsenrichmentinthetissue-specificdifferentialexpressionsignature.In
theexampleshownhere,forinstance,theregulonforproteinCUX1inanunknownororphantissueisbetterrecapitulatedbytheuterinecorpus
endometrialcarcinoma(UCEC)-basedregulon,whilethetranscriptionalprogramfortheandrogenreceptorprotein(AR)isbetterrecapitulatedbythe
cervicalsquamouscellcarcinomaandendocervicaladenocarcinoma(CESC)andglioblastoma(GBM)-basedregulons.Thenumbersindicate–log10(p-
value)forenrichmentoftheregulonsonthegeneexpressionsignature,ascomputedbyVIPER.bImpactofrecurrentcodingsomaticmutationson
metaVIPER-inferredproteinactivity.FractionofproteinsshowingsignificantassociationbetweenmetaVIPER-inferredproteinactivityandsomatic
mutations(p<0.01)ispresented.VIPERanalysiswasperformedusingthetissue-matchednetwork(tissueMatch),metaVIPERwasperformedby
integratingtheresultsfromindividualinteractomesusingmaxScore,avgScore,andNESScoremethods;thebaselinecontrolwascomputedbyusing
intercatomesselectedatrandom(randomMatch).TheX-axisrepresentstheminimumnumberofTCGAsamplespresentingthespecificgenemutation
requiredforinclusionoftheencodedproteinintheanalysis.cInferenceofproteinactivityfororphantissues.MetaVIPERcaneffectivelyreproduce
differentialproteinactivityinTCGAtissues,evenwhenthecorrespondingmatchedinteractomeisremovedfromtheanalysis.Theonlypartialexceptionis
representedbytwotissuelineages—liverhepatocellularcarcinoma(LIHC)andtesticulargermcelltumors(TGCT)—whicharedefinedbyhighlyspecific
regulatoryprograms.Theprobabilitydensitydistributionforthecorrelationbetweenproteinactivities(NES)inferredbymetaVIPERusingallavailable
interactomesvs.metaVIPERusingall,butthetissue-matchedinteractome(Pearson’scorrelation)acrossallsamplesisshownbytheviolinplots
NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications 3
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
locus is, the larger the fraction of proteins showing statistically Results show extremely strong average correlation (ρ>0.97)
significant correlation between metaVIPER-inferred protein betweenthetwoanalysesfor22outof24tissues(excludingliver
activity and mutational state. For instance, about 50% of the hepatocellularcarcinoma(LIHC)andtesticulargermcelltumors
genes harboring locus-specific mutations in at least 30 TCGA (TGCT)). This suggests that, even in the absence of a tissue-
samples could be detected as producing differentially active matched model, most tissues may be studied virtually without
proteins by metaVIPER analysis (p<0.01). loss of resolution using metaVIPER (Fig. 1c, Supplementary
Surprisingly,basedonthismetric,allfourstrategies forcross- Fig. 2). Thus most orphan tissues can be studied using
tissue integration (metaVIPER) significantly outperformed the metaVIPER with virtually no notable result quality degradation.
use of tissue-specific interactomes, i.e., the original VIPER Not surprisingly, the two outlier tissues have a rather unique
algorithm (tissueMatch). This suggests that integrating the nature. Indeed, LIHC is originated from hepatocytes, which are
structure of regulatory networks across a large number of unique endoderm derived secretory cells27. Similarly, TGCT
representative tissue types provides a more informative regulon originate from testicular germ cells, which are specialized
representationonanindividualproteinbasis.TherandomMatch pluripotent cells that give rise to gametes28. Hepatocytes and
method serves as a baseline negative control, in which for each testicular germ cells are thus highly specialized tissues with no
sample, protein activity was computed using VIPER with an other related tissues among the 24 in TCGA. However, as the
interactome selected at random. As discussed in the following numberofinteractomesinourrepertoiregrowstheprobabilityof
sections, we performed several additional benchmarks to having true outlier tissues will decrease. Note, however that,
comprehensively and systematically assess the method’s perfor- despite their specialized nature even the two outlier tissues
mance in orphan tissues, as well in single cells. presented high average correlation with the results of the tissue-
matched analysis (ρ>0.95).
Thisraisestheimportantissueofanobjectivemetrictoassess
MetaVIPER-basedproteinactivityinferenceinorphantissues. whether metaVIPER—when used with a specific repertoire of
Small sample size severely undermines the performance of tissue-specific interactomes—is adequate for inferring protein
ARACNe, which typically requires at least 100 independent activity in tissues lacking a matched interactome (i.e., orphan
samples, representative of the same tissue lineage26 to perform tissues).Toachievethisgoal,asproposedinref.9,wewillusethe
accurate regulon inference for VIPER analysis. This significantly EmpiricalCumulativeDistributionFunctionoftheabsolutevalue
limitstheabilitytoaccuratelymeasureproteinactivityinorphan oftheVIPERNES(ECDF )ofallproteinsinanorphantissue
|NES|
tissues, defined as rare or poorly characterized tissue types, for sample or samples11. In Supplementary Fig. 7, we show violin
which the number of available gene expression profiles is not plots for the ECDF of each TCGA cohort, using the
|NES|
sufficient to produce an accurate interactome model. For corresponding tissue-matched interactome. The rightmost plot
instance,considering tumor cohortsinthe TCGArepository,we (TCGA) shows the average of all cohort-specific probability
identified Cholangiocarcinoma (N=36) and Uterine Carcino- densities. This provides a useful reference to assess whether a
sarcoma (N=57) could be considered orphan tissues for which specific interactome repertoire is adequate for the metaVIPER-
an accurate ARACNe network could not be generated. Orphan based analysis of an orphan tissue. For instance, we analyzed
tissues also include a variety of normal or non-cancer, disease- LAML samples using only a GBM interactome, which would be
related cell states that lack appropriate gene expression profile clearly inappropriate since LAML and GBM cells belong to
characterization, including many of the intermediate states of epigeneticallydistinctlineages.Theresultisshowninthefirst-to-
differentiation representing multipotent or progenitor last violin plot (Neg.Ctrl.). As shown this ECDF is clearly an
population. outlierwithrespecttoAll-TCGA.Thus,bycomparingtheECDF
Since metaVIPER is designed to infer protein activity without for a tissue of interest against the All TCGA reference, one can
requiring a tissue-specific regulatory model, we designed an effectively assess the quality of the analysis.
objective benchmark to assess metaVIPER’s ability to accurately
measure protein activity in orphan tissues. We first assembled a
gold-standard set using metaVIPER to assess the activity of all Single cell analysis. The last few years have seen tremendous
proteins for which an ARACNe regulon was generated (see development of single cell profiling methodologies and in parti-
Methods), in each sample of each TCGA cohort, using all cular of scRNA-Seq. The advent of these technologies provides
available TCGA interactomes including the tissue-matched one. new insight in understanding transition, maintenance, and
This is preferred to using only the tissue-matched interactome cell–cell communication processes, across cell states and at an
becausefromtheobjectivebenchmarkusingmutationaldatathis individual cell resolution29. However, a major challenge of these
methodology has emerged as being more accurate than the approachesisrelatedtotheverylowdepthofsequencingranging
original VIPER analysis. However, for completeness, we also between 10 and 200K reads per cell. While this is sufficient to
report results of this analysis using the tissue-matched inter- perform coarse analyses, such asmulti-dimensional clustering to
actomes as gold-standard, see Supplementary Fig. 2. We then identify molecularly distinct sub-populations, it is extremely
performed the same analysis using metaVIPER with all available ineffective in precisely quantitating the expression of individual
TCGA interactomes, except for the tissue-matched one. For genes. Indeed, the vast majority of genes lack even one mRNA
instance, consider Rectum Adenocarcinoma (READ) as a tumor read in individual cells (dropouts) and a large number have a
for which an ARACNe interactome could not be accurately single read. Due to these significant dropout effects, elucidating
inferred.WewouldthencomputetheVIPER-inferredactivityof biologicalmechanismsatthesinglecelllevelremainschallenging.
allproteinsineachTCGAREADsampleusingeitherallavailable In contrast, as shown in ref. 7, VIPER analysis is largely unaf-
TCGAinteractomes(gold-standardreference)orallinteractomes fectedbysequencingdepthbecausedifferentialproteinactivityis
except for the READ interactome, exactly as if it were not assessed based on the differential expression of hundreds of
available. We then measure overall protein activity correlation transcriptional targets. Thus, measurement and biological noise
between the two analyses as a quality metric for metaVIPER sources are effectively averaged out, resulting in highly repro-
abilitytocorrectlyinferproteinactivityintheabsenceofatissue- ducible measurements. Indeed, we have shown that VIPER-
matchedinteractome.Thisbenchmarkwasperformedforeachof inferred protein activity profiles from FFPE samples were extre-
the all 24 tissue types in TCGA, see Supplementary Table24. mely well correlated to those from fresh-frozen samples, despite
4 NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
a b
Activity Expression
Detected?
Yes
No
−5 Zscore 5 −5 Zscore 5
T S N M Z Z Z L P ZZ B Z Z E D Z H D C C Z C S D D D H Z Z P P S SS O E F H N N N Z Z N N N ZZZ Z Z Z ZZ ZZZ ZZZ Z Z Z Z Z Z ZZZ Z Z Z ZZZ Z Z ZZZZ ZZZZZZZZ ZZ ZZ W H C U FP F C M S MD C CH C H M R N S O FB P P S F C A R R U 2 F M MT T H N H H A A O H A P T NH Z T E CC O R F A F A M U F T B T F L Z Z T ZZ Z Z K K S Z Z Z NNN N N N NN NNN NNN N N N N N N NNN N N N NNN N N NNNN NNNNNNNN NN NN F K O F FO A M P S S D G M I O R R D N M A MH M O A O E M N M C S E E SS O O O O O U R A R M R M C N D M H R E B P D C R O A M A H R J M G V O Y O X E T H B B R T H H HR T C S S B E L AA F S R O E H B B P E Y Y X N N C NN N N A A AJ U T E E EEE E T FK F F 5 H X X E P2 2 8 S I LFFF F F F FF FFF FFF F F F F F F FFF F F F FFF F F FFFF FFFFFFFF FF FF N M 3 N N M L L R I Z O D C U V D Y I A P4 X P M M B I I O B B OO F G F C H T X X N H N R R M U F H A D A E R A Y N N E S A J S P B P E K X B E X X B B B R A PT A R R L C T D C NN C F T C Y T C C F 1 T B 2B S P S P P L S L 6 B X X 2 8 0 L B B E P B T T F T L 2 222 L L FL F F L FF F F X F4 6 2 1 2 6 236 2 6 5 65 276 555 6 3 5 4 7 5 536 7 6 6 411 5 7 8116 45275757 22 67 I P I I I O A A R G G U D C I N S Y M R M R M R M N P G P P Y G G G H C R C H C D D D D F C C D C D 0 X 3 X 2 2 S P X X 9 B X X X X L X 9 X S V L B X 0 4 XX P K P 1 B B BX P X X B E B X A T T F F F F FFF F F F F F F F F F T T F F − − 3 L 3 L 3 3 L 4 L 3 L 22 L L L L 7 8 2 1 2 11L 47 9 2 2 2 1 L L 580 1 0 9 57 237 645 3 6 2 8 8 8 108 9 2 9 983 5 3 2047 66830191 58 74 4 1 1 J I I I G G C C C N R N D A B B A B X B X A X B A A P X E B A A B A B F F T F 1 9 1 1 2 2 6 1 7 0 3 82 0 1 1 1 2 1 L 4 1 2 2 90 11 1 2 1 1 1 2 21 1 3 5 4 1 1 3 2 7 812 3 4 46 3 2 6 1 2 0 2 1 41 3 1 4 1L 2 9 2 7 51 37 3 28 4 1 2 3 2 2 2 2 1 1 1 2 1 647 7 4 6 7 34 777 790 8 27 2 91 6 1 4 4 3 901 0 5 2441 3 915 0 12 9700 16526658 3 44 69 2 2 0 2 L1 8 1 1 1 1 4 1 4 3 A T A T S S P T A T C M R N S T A DS T A P RZ F T C B G C A C T S S F N E L R G U M A S D D P M M N P H 2 H P E T E N C F F E R F N R O K A R S C S PCC FE L A C F V P N B P 4 I A S S K A F R R R O A YB Z L K LP C A Z N UZ P W M S S G K R C T Q I RP A A P S D 0 B C P E VA D TC U S R G G N A A A P A C M R D C D A L H P B G P E GE O E R R R S C E A G B K S B C H D A M E C B GD E P G AG E M E R L A C M I C T O OO K P S F C L C H C W C UT L L R T B T A P S N S N F N N N L O R D P R C M L 1 1 2 K B L I P F M o CNP N N H A L G P O M M L G ME S H C A B E E D A G G M S BA C C C H R I G S B G S N M M H D S C N T M U L B I P P P P R N K R U A R P B C U T P N C Z C SA A S X P T T F C R C R C I D G C T F F T Z C B T M A M K S T A S R S C N C P S R C L AM K P P A P P B A K S S 6 T F S F H C P A A 1 L T 3 S T F 1 P P 1 1 P3 L 10 0 LL A 1 5 F I IF F F F F r N O I Q 3 A I I IL G I D R M L W M L B I P AQ M M C D U N M C A M M G R A O M M G N C CM C I G B A G S N C R R T D N M C T R C A A fB D A C H A P R UCR D U B C B MN E P B C H S E P A C R D B T P S O A S S A A S P A E B P O A S E K T T C N T R N D 8 5F C I S E SS H D Y T C D D S S 1 A N 5 R B 9 L8 L B L 7 9 1Y 1 5P 0B S 0 1 PL 6 A 2 S44 3 9 A B J I T T T L 2 L T L 1 1 4 2 1 2 L 7 1 1 8 1 L 1 I W I I G I I O Y G M G C O P I U M M P N S C C M A M M G P G G B A O G O T N R F D D 1 D D R D N 3 D3 N R R D N N C NH N H D R D D SA T F R N N R S L D N C D D A X A B B 5 S B K E P S K A P A S BAS P P S 0S P AS B A E AA A3 A A E S S AP B X L 1 5B AA K KK 1 3 6 P P P X A P 5 T Z T FFT T T T F F T T F F F FL 1 2 2 1 1 0 3 1 L 7 6 6 1 4 1 9 1 L L 52 6 L L L 8L 1 4 1 L 1 L 2 4 2 4 L 9 1 2 L M Q G G H D N C C R C N D N R N U R B P K E A S B A P A K K PP B B B A A A F F ZT F T 2 4 1 2 3 1 1 3 4 2 1 9 5 0 0 9 1 1 1 6 6 4 0 7 2 132 L 3 2 8 1 L 2 24 1 1 3 411 3 11 2 1 1 3 3 24 L 21 2 3 1 21 3 1 125 43 1 6 3 24 3 2 4 73 72 115 1 21 11 3 532 4 3 5 48 2 04 3 6 4 1 03 2 1 1 2 1 2 8 3 1 6 1 1 1 312 3 1 1 21 6 2 1 1 4 8 1 18 2 1 1 11 4 2 4 1 2 3 3 5 4 1 4 1 0 1
Fig.2InferenceofproteinactivityforsinglecellsfromGBMmousemodel.aMetaVIPER-basedproteinactivityanalysisofsinglecellsfromamouseGBM
model27,28byunsupervisedclusteringusingallannotatedtranscriptionalfactors,co-transcriptionalfactors,andsignalingproteins.Twomajorclusters
wereidentified,correspondingtoestablishedmesenchymal(MES,blue)andproneural(PN,turquoise)subtypes,withvaryingproliferative(Prolif)
potential11.Indeed,amongthetop200transcriptionalfactors(i.e.,withthehighestinter-clusteractivityvariability),wefoundestablishedmaster
regulatorytranscriptionalfactorsoftheMES(FOSL1,FOSL2,RUNX1,CEBPB,CEBPD,MYCN,ELF4),PN(OLIG2,ZNF217),andProlif(HMGB2,SMAD4,PTTG1,
E2F1,E2F8,FOXM1)subtypes13.bSubtyperepresentationislostwhenclusteringisperformedbasedongeneexpressionprofiles
dramaticlossofcorrelationatthegeneexpressionlevel7,leading activityefficientlyseparatedsinglecellsintwomajorgroups,with
toNYSCLIAapprovaloftwoVIPER-basedtests.Asaresult,one ~40%ofthecellsrecapitulatingtheactivitypatternofpreviously
would expect VIPER to be well suited to performing analysis of describedMRproteinsofMES(FOSL1,FOSL2,RUNX1,CEBPB,
single cell populations in a way that is amenable to quantitative CEBPD, MYCN, ELF4), and the remaining ~60% recapitulating
protein activity assessment. those of the PN, such as OLIG2 and ZNF217. In sharp contrast,
Unfortunately, however, when dealing with heterogeneous unsupervised, gene expression based cluster analysis could not
samples,thespecifictissuecontextofeachindividualcellcannot effectivelyseparateindividualcellsindistinctclusters(Fig.2a,b).
be determined a priori. Even if this were possible, it is unlikely Indeed, ~40% of the critical subtype-related proteins were
that context specific interactomes would be available for rare undetectable at the gene expression level in any of the single
lineages and progenitor states that are captured by single cell cells (black horizontal bars in Fig. 2a). Expression profiles from
profiling methodologies. MetaVIPER represents a useful alter- single cells are very noisy, due to low sequencing depth, thus
native in these cases, because, while preserving the robustness of reducing the ability to study their biology. Indeed, low depth of
VIPER,itisagnostictotissuetypeandshouldthusbewellsuited sequencing represents a major confounding factor that can be
to analysis of single cell gene expression profiles from hetero- effectively remedied by metaVIPER analysis.
geneous tissues. Quality of single cell gene expression profiles is generally
To illustrate metaVIPER applicability to single cell expression reflected bythenumberof detectedgenes29.Higherqualitygene
profiledata,we specificallyprofiled 85single cells(see Methods) expression profiles, as identified by higher transcriptome com-
from a mouse glioblastoma (GBM) model30,31. Previous studies plexity,tendtoresultinhighercorrelationbetweentheprofilesof
have demonstrated that GBM comprises two major subtypes, single cells in the same sub-population clusters (Supplementary
mesenchymal (MES) and Proneural (PN), which may present Fig. 3A, B).Once processedwithmetaVIPER, however,notonly
different proliferation capability
(Prolif)13,32–34.
We inferred intra-population correlation between individual cells increases
protein activity at the single cell level by metaVIPER analysis significantly but it also becomes virtually independent of
across5braintumorinteractomes,and24TCGAhumancancer transcriptome complexity (Supplementary Fig. 3C). This is
tissue interactomes (see Methods and Supplementary Table). because protein activity inference is based on the expression of
Contrarytogeneexpressionprofileanalysis,theinferred protein manytargetgenesandisthusmuchmorerobustthanestimating
activity signatures clearly captured single cells representing MES gene expression from a single measurement, thus improving
and PN subtypes. Indeed, unsupervised metaVIPER analysis resilience to low-quality data.
recapitulatedpreviouslyreportedsubtype-specificMRproteins13, We further tested our methodology on single cell data from
which were identified among the most dysregulated on a single tissue representing a complex mixture of melanoma cells and
cell basis (Fig. 2a). Such level of resolution could not be infiltrating B and T lymphocytes35. By integrating interactomes
recapitulated by differential gene expression analysis, largely representative of skin cutaneous melanoma (SKCM, see Meth-
due to transcript-level noise in individual cells (Fig. 2b). ods),B9andT36lymphocytes,aswellas24TCGAhumancancer
Unsupervised clustering analysis of metaVIPER-inferred protein tissue24 (Supplementary Table), metaVIPER was able to infer
NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications 5
b e h
a
metaVIPER
50
c f i
0
−50
d g j
−40 0 20 40 60
Dim1
2miD
PAX5
ACT EXP
−3
B
M
T
erocsZ
6
EBF1
ACT EXP
−3
erocsZ
6
E2A
ACT EXP
−3
erocsZ
MITF BCL11B
ACT EXP ACT EXP
CTNNB1 FOXP3
ACT EXP ACT EXP
HMGB1 TBET
6
ACT EXP ACT EXP
Fig.3InferenceofproteinactivityforsinglecellsprofiledbyTiroshetal.35.aAnnotatedcelltypes(B:Blymphocyte,T:Tlymphocyte,M:melanomacell)
wereseparatedbyt-SNEanalysis,usingmetaVIPER-inferredactivityforallannotatedtranscriptionalfactors,co-transcriptionalfactors,andsignaling
proteins.BoxplotsshowmetaVIPER-inferredactivity,aswellasgeneexpressionfortissue-specificlineagemarkers,includingPAX537,EBF138,andE2A39for
Blymphocyte(b–d),MITF40,CTNNB141,andHMGB142formelanocyte(e–g),BCL11B43,FOXP344,andTBET45forTlymphocyte(h–j).Whilethesemarkers
aresignificantlydifferentiallyactiveinthesetissues,theycouldnotbeeffectivelyassessedatthesinglecelllevel,eitherbecausenomRNAreadswere
detectedorbecausemarkerswerenotstatisticallysignificantintermsofdifferentialgeneexpression.Boxplotsshowedthemedian,lower/upperwhiskers,
andhingesofz-scores
Synthetic bulk, expression
500
0
−500
−1000 −500 0 500
Dim1
2miD
Synthetic bulk, activity
1000 500
0
−500
−800 −400 0 200 400
Dim1
2miD
Significant markers
1
0.5
0
0 20 40 60 80 100
% Single cells
B M T
FDCE−1
p < 1e−11
Pairs among significant markers
1 0.5
0
0 20 40 60 80 100
% Pairs
FDCE−1
Expression of lineage markers
6
4
2
0
0 1 2 3 4 5 6
PAX5
p < 1e−11
3PXOF
Activity of lineage markers
4
2
0
−2
−1 0 1 2 3 4
PAX5
3PXOF
Expression of predicted markers
8
6
4
2
0
0 1 2 3 4 5 6 7
POU2F2
4TATS
Activity of predicted markers
4
2
0
−2
−4
−2 −1 0 1 2 3 4
POU2F2
4TATS
Expression of cell surface markers
8
6
4
2
0
0 2 4 6 8 10
CD3
91DC
Activity of cell surface markers
3 2
1
0
−1
−2
−3
−2 0 2 4
CD3
91DC
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
a c e g i
b d f h j
Overexpressed genes Activated proteins
B
M
T
Fig.4ComparativeanalysisofsinglecellmetaVIPERperformancecomparedtogeneexpressionbasedmethods.Weidentifiedthe100mostdifferentially
expressedgenesanddifferentiallyactiveproteinsbasedontheanalysisoffivesyntheticbulksamplescreatedbyaveragingtheexpressionof100randomly
selectedsinglecellsfromthemelanoma,Bcell,andTcellpopulationclusters,respectively.a,bBasedont-SNEanalysis,syntheticbulksamplesclustered
moretightlywhenanalyzedbasedonVIPER-inferredproteinactivitythanbasedongeneexpression.cThispanelshowsthepercentofthetop100most
differentiallyexpressedgenes/activeproteinsrecapitulatedassignificantlydifferentiallyexpressed/activeinagivenfractionofindividualcellsagainstthe
averageexpression/activityinadistinctcluster(e.g.,aTcellvs.theaverageofallBcells).Theyellowandturquoisecurves(1-ECDF)andboxplots
(median,lower/upperwhiskers,andhinges)summarizedtheresultsofRSEMandmetaVIPER-basedanalyses,respectively.dThesameanalyseswere
repeatedtoassessreproducibledifferentialexpression/activityofagene/proteinpair,asrelevantforvirtualFACSanalyses.e,fVirtualFACSanalyses
usingexpressionandactivityofestablishedlineagemarkerTFsbyRSEMandmetaVIPER-basedanalysis(seemaintextandFig.3fordetails).g,hVirtual
FACSanalysisusingexpressionandactivityofSTAT4andPOU2F—bothidentifiedasdifferentiallyexpressedandactivecandidatebiomarkersfrombulk
sampleanalyses—usingthesamemethods.i,jVirtualFACSanalysisbasedonexpressionandactivityofCD3andCD19cellsurfacemarkers,asusedin
standardFACSanalyses,usingthesamemethods
6 NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
proteinactivityprofilesthateffectivelydiscriminatebetweenthese selectedmarkerpairsatthegeneexpressionlevel.Indeed,mostof
differentcelltypes.Furthermore,itrevealeddifferentialactivityof the cellsarefound eitheron thex-axis (nodetectable expression
establishedlineagemarkersthatcouldnotbedetectedatthegene oftheY-marker)oronthey-axis(nodetectableexpressionofthe
expressionlevel(Fig.3b–j).Thisrepresentsacriticalvalueofthis X-marker) or at the intersection of the two axes (no detectable
approach, as many important lineage markers and other expression of either marker). In contrast, metaVIPER analysis
transcriptional regulators may yield no scRNA-Seq reads, due generatesvirtualFACSplotsthatareconsistentwithwhatwould
to their relatively low transcript abundance combined with low be produced by an actual FACS assay. For instance, consider
sequencingdepth.Basedonametricassessingthedynamicrange CD19 and CD3, which are classic B and T cells markers,
of protein activity in different sub-clusters, metaVIPER signifi- respectively. From metaVIPER analysis (Fig. 4j), one can clearly
cantlyoutperformedsingle-regulon-basedVIPERanalysisonthis identifyaCD19+/CD3−clustercorrespondingtoBcells,aCD19
dataset (Supplementary Fig. 4). Most importantly, metaVIPER −/CD3+ cluster corresponding to T cells, and a CD19−/CD3−
correctly inferred the differential, tissue-specific activity of clustercorrespondingtomelanomacells.Yet,thisisnotpossible
establishedlineagedeterminantsatthesinglecelllevel(Fig.3b–j). when considering single cell gene expression (Fig. 4i).
For instance, PAX537, EBF138, and E2A39 showed significantly Finally an additional value of the algorithm is that processes
higher activity in B lymphocytes (one-tail, p<10 −10); MITF40, that are not consistent with the transcriptional regulatory
CTNNB141,andHMGB142showedsignificantlyhigheractivityin architecture of the cells of interest are effectively filtered out by
melanomacells(one-tail,p<10
−10);finally,BCL11B43,FOXP344,
the interactome analysis. This is useful, for instance, in
andTBET45showedsignificantlyhigheractivityinTlymphocytes eliminatingbiasduetodifferentchemistryofsinglecellprofiling
(one-tail, p<10 −10). Conversely, we could not detect significant or batch effects due to use of different gene expression
geneexpressiondifferencesformostofthesegenes(e.g.,p quantification methodologies(Supplementary Fig. 5and 6). This
HMGB1
>0.9)inmelanomacells,orexpressionwasbarelydetectedatall is helpful as these biases and batch effects represent a major
(averagetranscriptspermillion<1),seeE2AinBlymphocytesor obstacle to the integrative analysis of gene expression data
FOXP3 and TBET in T lymphocytes, for instance (Fig. 3b–j). generated in different labs or using slightly different reagent
Toprovideamoresystematiccomparisonoftheimprovements batches.
offeredbymetaVIPER analysisofsinglecellsagainstapproaches Taken together, these data show that metaVIPER represents a
based on state-of-the-art gene expression analysis algorithms, useful methodology for the analysis of single cell data and, in
usingthesamemixtureofT,B,andmelanomacellsdescribedin particular, for the identification of lineage-specific regulatory
theprevioussection.Mostmethodsdesignedtoaddressthegene programs and lineage markers in samples comprising a hetero-
dropoutissueinscRNA-Seqprofilesarenotintendedtoperform geneous mixture of single cells.
differential expression analysis of two individual cells but rather
only of single cell subsets representing molecularly distinct
clusters/subtypes46–48.
To perform this analysis, we thus Discussion
quantified single cell gene expression using RSEM49, which pre- We have shown that integration of multiple interactomes using
assemblessequencingreadsintotranscripts,thusprovidingmore an evidence integration platform (metaVIPER) can provide
accurate single cell gene expression quantification50. We then accurate assessment of protein activity independent of tissue
assessedthefractionofsinglecellpairsfromtwodistinctclusters lineage.Bysystematic,wemeanthatactivityof6000proteinscan
(e.g., B and T cell related) that could recapitulate differentially be reproducibly assessed from any tissue, independent of their
expressed genes and differentially active proteins, as originally gene expression; this is especially valuable in single cell analyses.
detectedfromtheircorrespondingbulkcellpopulations.Foreach MetaVIPER can thus help infer activity of key regulators in tis-
cluster, we generated “synthetic bulk” expression profiles by sues lacking a matched interactome—either due to low sample
averaging 100 randomly selected single cells, based on which we availability (orphan tissues) or to lack of tissue lineage informa-
generated “synthetic bulk” protein activity profiles. As shown in tion—as well as in highly heterogeneous single cell populations
the corresponding t-SNE plots, synthetic bulk profiles from isolated from bulk tissue. We propose a specific metric (ECDF
|
metaVIPER-inferredproteinactivityanalysis(Fig.4b)weremuch ) to assess whether a specific repertoire of interactomes is
NES|
tighterthanthoseproducedbygeneexpressionanalysis(Fig.4a), adequate for the metaVIPER analysis of an unknown or orphan
suggesting that VIPER-inferred protein activity is more repro- tissue.
ducible across samples than mRNA expression. Finally, we MetaVIPER is especially useful for the study of single cell
assessed the fraction of the 100 most differentially expressed biology,asitsresultsarelargelyindependentofsequencingdepth
genes and differentially active proteins (as assessed from bulk andallowquantitativeinferenceofproteinactivityevenwhenthe
sampleanalysis)thatcouldberecapitulatedinagivenfractionof correspondingmRNAisundetectable.Indeed,differentialactivity
single cells when compared to the bulk expression of a different ofestablishedlineagemarkersofT,B,andmelanomacellscould
cluster (e.g., a single T-cell vs. all cells in the melanoma cluster). be clearly assessed in single cells from a complex mixture, even
As shown in Fig. 4c, differential activity (turquoise curve) though most of these markers were either not detected or could
significantly outperformed RSEM-based differential gene expres- not be identified as statistically significantly differentially
sion analysis (yellow curve). This becomes even more evident expressed at the mRNA level. The reduction in bias and batch
whenconsideringpairsofdifferentiallyexpressedgenesoractive effectsisanadditionaladvantage,allowingintegrationofdatasets
proteins(e.g.,geneXandYbeingbothdifferentiallyexpressedin frommultiplelabsorgeneratedatdifferenttimes,thusaddressing
a single cell if they are both differentially expressed in the bulk) the important issue of single cell data reproducibility.
(Fig.4d).ThelatterisimportantasitsupportsuseofmetaVIPER Among the most obvious limitations of the method, metaVI-
togenerateanalysessimilartowhatisnormallyaccomplishedby PER cannot accurately measure activity of proteins whose reg-
FACS, using two or more markers, using any of the ~6000 ulons are not adequately represented in at least one of the
proteins assessed by the algorithm not limited by antibody available interactomes. This includes proteins whose targets are
availability. This is shown in Fig. 4e–j, where virtual FACS plots exceedingly tissue-specificwithinrare tissuetypes and singlecell
areshownforcriticallineage markersofthesepopulationsusing sub-populations, for instance in LIHC and TGCT. As more
geneexpression(topplots)orproteinactivity(bottomplots).As interactomes are assembled, including by ARACNe analysis of
shown, it isvirtually impossible to identify cellclusters based on single cell data from homogeneous sub-populations, this
NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications 7
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
limitation will be increasingly mitigated. This suggests that a harboringrecurrentsomaticmutationforthatspecificproteinasenrichingset.We
concerted effort toward the generation of regulatory models considerproteinswithsignificantenrichmentscore(p<0.01)asshowingsig-
representing distinct cellular compartments should be
nificantassociationbetweeninferredproteinactivityandrecurrentsomatic
mutations.Thenwecheckedthefractionofproteinsthatcanbeassociatedwith
undertaken.
recurrentsomaticmutations,andusedthatascriteriainevaluatingtheperfor-
It should be noted that, while we used ARACNe as a metho- mancebetweenVIPERandmetaVIPER.Inordertogetenoughmutatedpatient
dology for interactome generation, there are many alternative/ samplesforeachprotein,thisanalysisisdoneinatumortypenon-specificmanner.
complementary methods to accomplish the same goal, ranging
from DNA binding-site analysis51,52, to correlation-based53 and Preparationofglioblastomamousemodel.PDGFB–IRES–CREexpressingret-
graphical-model-based54, to literature-based approaches55. roviruswasinjectedintotherostralsubcorticalwhitematterofadultPtenlox/lox/
p53lox/lox/luciferase-stop-loxtransgenicmice30,31.Micedevelopedbraintumorswith
Comparison of VIPER performance using several of these
thehistopathologicalfeaturesofglioblastomaby28dayspostinjectionwith
methods was already discussed in ref. 7 and is thus not repeated retrovirus.
here.IntermsoftheVIPERalgorithm,asalsodiscussedinref.7,
alternativealgorithmstotransformageneexpressionprofileinto GeneratingscRNA-Seqprofilesforglioblastomamousemodel.Following
a protein activity profile are still lacking but a thorough perfor- IACUCguidelines,animalsweresacrificedatthefirstsignofmorbidity.Exvivo
mance comparison can be easily performed once they become grosstotalresectionofthetumorwasperformedandtumorcellswereisolated
usingenzymaticdigestion62.Theisolatedcellswereculturedina2:1ratioofbasal
available.Ingeneral,themetaVIPERapproachisindependentof
media(DMEM,N2,T3,0.5%FBS,andpenicillin/streptomycin/amphotericin)in
the specific algorithms used for either interactome reverse engi- B104conditionedmedia63.ThismediawasfurthersupplementedwithPDGF–AA
neering or analysis and should thus be still fully applicable once (Sigma-Aldrich;St.Louis,MO)andFGFb(Gibco;GrandIsland,NY)toacon-
VIPER alternatives emerge.
centrationof10ng/ml.Wethenobtained85scRNA-SeqprofilesusingtheFlui-
digmC1system.WeloadeddissociatedcellsintoaFluidigmIntegratedFluidic
WehaveshownthatVIPER-basedelucidationofMRproteins
Circuitwithcapturesitesdesignedfor10–17μmdiametercellsafterstainingthe
using tissue lineage-specific interactomes can effectively identify singlecellsuspensionwithCalceinAM(LifeTechnologies).Wethenimagedthe
reprogramming and pluripotency factors13,21,22,56, as well as cellsthathadbeencapturedon-chipwithbothbrightfieldandfluorescence
determinants of tumor states11–13 and resistance to targeted microscopyusinganinvertedNikonEclipseTi–Uepifluorescencemicroscopewith
therapy17,36. As a result, application of metaVIPER to single cell a×20,0.75NAairobjective(PlanApoλ,Nikon),a473nmdiodelaser(Dragon
populations identified by cluster analysis could help identify Lasers),andanelectronmultiplyingchargecoupleddevice(EMCCD)camera
(iXON3,AndorTechnologies).Thisallowedustoidentifycapturesiteswithzero,
critical determinants of lineage development, as well as distinct one,andmorethanonecellandalsotoidentifycapturesitescontaininglivingcells,
dependencies within molecularly heterogeneous sub-population basedontheCalceinAMfluorescence.Wethenlysedthecells,reversetranscribed
in cancer tissues. For instance, it may help identify critical
mRNAintocDNA,andpre-amplifiedfull-lengthcDNAbyPCRautomatically
usingtheFluidigmC1Autoprepinstrumentaccordingtothemanufacturer’s
dependenciesinchemoresistantcellniches,includingraretumor- instructions.Finally,weharvestedindividualcDNAlibrariesfromthemicrofluidic
initiating and tumor stem cell niches that have been shown to deviceandconvertedthemintoindexed,Illuminasequencinglibrariesbyinvitro
have poor sensitivity to standard chemotherapy and targeted transposition,andPCRusingtheNexterasystem(Illumina).Thepooledlibraries
therapy. Similarly, it could help identify drivers leading to aber- weresequencedonasinglelaneofanIlluminaHiSeq2000withsingle-end100-bp
reads.Afterdemultiplexing,theresultingrawreadswerealignedtothemurine
rant reprogramming of physiologic cell states, such as recently
genomeandtranscriptomeannotation(mm10,UCSCannotationfromIllumina
reported in type II diabetes57. iGenomes)withTophat2.Uniquelyaligned,exonicreadswerethenquantifiedfor
eachgeneusingHTSeq.
Methods
Regulatorynetworks.AllregulatorynetworkswerereverseengineeredbyARA- Codeavailability.metaVIPERisimplementedinviperfunctionfromBio-
CNe9andsummarizedinSupplementaryTable.Twenty-fourcoreTCGARNA- conductorR-packageVIPER:https://www.bioconductor.org/packages/release/bioc/
SeqderivedinteractomesareavailableinR-packagearacne.networksfromBio- html/viper.html.ARACNealgorithm:http://califano.c2b2.columbia.edu/aracne.
conductor24.TheTCGAhumanSKCMnetworkwasassembledfromRNA-Seq Customscriptswillbeprovideduponrequesttothecorrespondingauthors.
profiles.TCGARNA-Seqlevel3data(countspergene)wereobtainedfromthe
TCGSAdataportal,andnormalizedbyVarianceStabilizationTransformation Dataavailability.scRNA-Seqdataforthemouseglioblastomamodeldescribedin
(VST),asimplementedintheDESeqpackagefromBioconductor58.ThehumanB thepaperhavebeendepositedattheGeneExpressionOmnibus(GEO)under
lymphocyteinteractomewasreportedbyBassoetal.9.ThehumanTlymphocyte accessionnumberGSE95157.R-packagearacne.networksisavailableonBio-
interactomewasreportedbyPiovanetal.36.Thehumanbraintumorregulatory conductor(10.18129/B9.bioc.aracne.networks).SKCM,B,andTlymphocyte
networkswereassembledfromfourmoregeneexpressiondatasetsbesidesthe interactomes(10.6084/m9.figshare.4833704).Braintumorinteractomes(10.6084/
TCGAglioblastomaRNA-Seqdataset.FortheRembrandt,Phillips32,TCGA- m9.figshare.4648765.v1).TCGAexpressionandsomaticmutationprofile:http://
Agilent,andTCGA-Affymetrix,informativeprobeclusterswereassembledwith cancergenome.nih.gov/.REMBRANDTdataset:https://gdoc.georgetown.edu/
thecleaneralgorithm59andtheexpressiondataweresummarizedandnormalized gdoc/.COSMICsomaticmutationprofile:http://cancer.sanger.ac.uk/cosmic.Fil-
withtheMAS5algorithm,asimplementedintheaffyR-packagefromBio- teredPBMCscRNA-Seqexpressionprofilesgeneratedusing10×GenomicsV2
conductor60.Differencesinsampledistributionswereremovedwiththerobust chemistry:https://support.10xgenomics.com/single-cell-gene-expression/datasets/
splinenormalizationprocedureimplementedinthelumiR-packagefromBio- 2.0.1/pbmc4k.FilteredPBMCscRNA-Seqexpressionprofilesgeneratedusing10×
conductor61.Inasimilarway,differencesinsampledistributionfortheTCGA- GenomicsV1chemistry:https://support.10xgenomics.com/single-cell-gene-
Agilentdatasetwereremovedbytherobustsplinenormalizationmethod.ARA- expression/datasets/1.1.0/pbmc3k.Allrelevantdataareavailablefromtheauthors.
CNewasrunwith100bootstrapiterationsusing1813transcriptionfactors(genes
annotatedingeneontologymolecularfunctiondatabase,asGO:0003700,“tran-
scriptionfactoractivity”,orasGO:0003677,“DNAbinding”,andGO:0030528, Received: 22 May2017 Accepted: 13March 2018
“transcriptionregulatoractivity”,orasGO:00034677andGO:0045449,“regulation
oftranscription”),969transcriptionalcofactors(amanuallycuratedlist,not
overlappingwiththetranscriptionfactorlist,builtupongenesannotatedas
GO:0003712,“transcriptioncofactoractivity”,orGO:0030528orGO:0045449),
and3370signalingpathwayrelatedgenes(annotatedinGObiologicalprocess
databaseasGO:0007165“signaltransduction”andinGOcellularcomponent References
databaseasGO:0005622,“intracellular”,orGO:0005886,“plasmamembrane”).
1. Clevers,H.Wnt/beta-cateninsignalingindevelopmentanddisease.Cell127,
ParametersweresettozeroDPI(DataProcessingInequality)toleranceandMI 469–480(2006).
(MutualInformation)p-value(usingMIcomputedbypermutingtheoriginal
datasetasnullmodel)thresholdof10
−8. 2.
m
Th
e
i
s
e
e
r
n
y
c
,
h
J
y
.
m
P.
a
,
l
A
t
c
ra
lo
n
q
s
u
it
e
io
,
n
H
s
.,
in
H
d
u
e
a
v
n
e
g
l
,
op
R
m
.Y
en
.
t
&
an
N
d
ie
d
to
is
,
e
M
as
.
e.
A
C
.
e
E
ll
pi
1
t
3
h
9
el
,
ia
8
l
7
-
1–890
(2009).
AssociatingsomaticmutationswithmetaVIPERinference.Weconsider 3. Hanahan,D.&Weinberg,R.A.Hallmarksofcancer:thenextgeneration.Cell
somaticmutationsthathappeninthesameaminoacidofaproteinwithinatleast
144,646–674(2011).
threepatientsasrecurrentsomaticmutations.Thenforeachprotein,wedid 4. Thiery,J.P.Epithelial-mesenchymaltransitionsintumourprogression.Nat.
enrichmentanalysiswithactivityprofileforeachpatientassignature,andpatient Rev.Cancer2,442–454(2002).
8 NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
5. Califano,A.&Alvarez,M.J.Therecurrentarchitectureoftumourinitiation, 35. Tirosh,I.etal.Dissectingthemulticellularecosystemofmetastaticmelanoma
progressionanddrugsensitivity.Nat.Rev.Cancer17,116–130(2017). bysingle-cellRNA-seq.Science352,189–196(2016).
6. Lefebvre,C.etal.AhumanB-cellinteractomeidentifiesMYBandFOXM1as 36. Piovan,E.etal.DirectreversalofglucocorticoidresistancebyAKTinhibition
masterregulatorsofproliferationingerminalcenters.Mol.Syst.Biol.6,377 inacutelymphoblasticleukemia.CancerCell24,766–776(2013).
(2010). 37. Nutt,S.L.,Heavey,B.,Rolink,A.G.&Busslinger,M.CommitmenttotheB-
7. Alvarez,M.J.etal.Functionalcharacterizationofsomaticmutationsincancer lymphoidlineagedependsonthetranscriptionfactorPax5.Nature401,
usingnetwork-basedinferenceofproteinactivity.Nat.Genet.48,838–847 556–562(1999).
(2016). 38. Lin,Y.C.etal.Aglobalnetworkoftranscriptionfactors,involvingE2A,EBF1
8. Subramanian,A.etal.Genesetenrichmentanalysis:aknowledge-based andFoxo1,thatorchestratesBcellfate.Nat.Immunol.11,635–643(2010).
approachforinterpretinggenome-wideexpressionprofiles.Proc.NatlAcad. 39. Bain,G.etal.E2AproteinsarerequiredforproperBcelldevelopmentand
Sci.USA102,15545–15550(2005). initiationofimmunoglobulingenerearrangements.Cell79,885–892(1994).
9. Basso,K.etal.ReverseengineeringofregulatorynetworksinhumanBcells. 40. Levy,C.,Khaled,M.&Fisher,D.E.MITF:masterregulatorofmelanocyte
Nat.Genet.37,382–390(2005). developmentandmelanomaoncogene.TrendsMol.Med.12,406–414(2006).
10. Hecker,M.etal.Generegulatorynetworkinference:dataintegrationin 41. Rubinfeld,B.etal.Stabilizationofbeta-cateninbygeneticdefectsin
dynamicmodels—areview.Biosystems96,86–103(2009). melanomacelllines.Science275,1790–1792(1997).
11. Aytes,A.etal.Cross-speciesregulatorynetworkanalysisidentifiesa 42. Lotze,M.T.&Tracey,K.J.High-mobilitygroupbox1protein(HMGB1):
synergisticinteractionbetweenFOXM1andCENPFthatdrivesprostate nuclearweaponintheimmunearsenal.Nat.Rev.Immunol.5,331–342
cancermalignancy.CancerCell25,638–651(2014). (2005).
12. Bisikirska,B.etal.Elucidationandpharmacologicaltargetingofnovel 43. Li,L.,Leid,M.&Rothenberg,E.V.AnearlyTcelllineagecommitment
moleculardriversoffollicularlymphomaprogression.CancerRes.76, checkpointdependentonthetranscriptionfactorBcl11b.Science329,89–93
664–674(2016). (2010).
13. Carro,M.S.etal.Thetranscriptionalnetworkformesenchymal 44. Hori,S.,Nomura,T.&Sakaguchi,S.ControlofregulatoryTcelldevelopment
transformationofbraintumours.Nature463,318–325(2010). bythetranscriptionfactorFoxp3.Science299,1057–1061(2003).
14. Chen,J.C.etal.Identificationofcausalgeneticdriversofhumandisease 45. Szabo,S.J.etal.Anoveltranscriptionfactor,T-bet,directsTh1lineage
throughsystems-levelanalysisofregulatorynetworks.Cell159,402–414 commitment.Cell100,655–669(2000).
(2014). 46. Kharchenko,P.V.etal.Bayesianapproachtosingle-celldifferential
15. Chudnovsky,Y.etal.ZFHX4interactswiththeNuRDcorememberCHD4 expressionanalysis.Nat.Methods11,740–742(2014).
andregulatestheglioblastomatumor-initiatingcellstate.CellRep.6,313–324 47. Vu,T.N.etal.Beta-Poissonmodelforsingle-cellRNA-seqdataanalyses.
(2014). Bioinformatics32,2128–2135(2016).
16. DellaGatta,G.etal.ReverseengineeringofTLXoncogenictranscriptional 48. Finak,G.etal.MAST:aflexiblestatisticalframeworkforassessing
networksidentifiesRUNX1astumorsuppressorinT-ALL.Nat.Med.18, transcriptionalchangesandcharacterizingheterogeneityinsingle-cellRNA
436–440(2012). sequencingdata.GenomeBiol.16,278(2015).
17. Rodriguez-Barrueco,R.etal.InhibitionoftheautocrineIL-6-JAK2-STAT3- 49. Li,B.&Dewey,C.N.RSEM:accuratetranscriptquantificationfromRNA-Seq
calprotectinaxisastargetedtherapyforHR-/HER2+breastcancers.Genes datawithorwithoutareferencegenome.BMC.Bioinforma.12,323(2011).
Dev.29,1631–1648(2015). 50. Vallejos,C.A.etal.Normalizingsingle-cellRNAsequencingdata:challenges
18. Aubry,S.etal.AssemblyandinterrogationofAlzheimer’sdiseasegenetic andopportunities.Nat.Methods14,565–571(2017).
networksrevealnovelregulatorsofprogression.PLoSONE10,e0120352 51. Lachmann,A.etal.ChEA:transcriptionfactorregulationinferredfrom
(2015). integratinggenome-wideChIP-Xexperiments.Bioinformatics26,2438–2444
19. Brichta,L.etal.Identificationofneurodegenerativefactorsusingtranslatome- (2010).
regulatorynetworkanalysis.Nat.Neurosci.18,1325–1333(2015). 52. Bussemaker,H.J.etal.Regulatoryelementdetectionusingcorrelationwith
20. Ikiz,B.etal.Theregulatorymachineryofneurodegenerationininvitro expression.Nat.Genet.27,167–171(2001).
modelsofamyotrophiclateralsclerosis.CellRep.12,335–345(2015). 53. Butte,A.J.&Kohane,I.S.Mutualinformationrelevancenetworks:functional
21. Kushwaha,R.etal.Interrogationofacontext-specifictranscriptionfactor genomicclusteringusingpairwiseentropymeasurements.PacificSymposium
networkidentifiesnovelregulatorsofpluripotency.StemCells33,367–377 onBiocomputing5,415–426(2000).
(2015). 54. Friedman,N.Inferringcellularnetworksusingprobabilisticgraphicalmodels.
22. Talos,F.,Mitrofanova,A.,Bergren,S.K.,Califano,A.&Shen,M.M.A Science303,799–805(2004).
computationalsystemsapproachidentifiessynergisticspecificationgenes 55. Kramer,A.etal.Causalanalysisapproachesiningenuitypathwayanalysis.
thatfacilitatelineageconversiontoprostatetissue.Nat.Commun.8,14662 Bioinformatics30,523–530(2014).
(2017). 56. Dutta,A.etal.IdentificationofanNKX3.1-G9a-UTYtranscriptional
23. Repunte-Canonigo,V.etal.Identifyingcandidatedriversofalcohol regulatorynetworkthatcontrolsprostatedifferentiation.Science352,
dependence-inducedexcessivedrinkingbyassemblyandinterrogationof 1576–1580(2016).
brain-specificregulatorynetworks.GenomeBiol.16,68(2015). 57. Talchai,C.etal.Pancreaticbetacelldedifferentiationasamechanismof
24. Giorgi,F.M.aracne.networks:ARACNe-inferredgenenetworksfromTCGA diabeticbetacellfailure.Cell150,1223–1234(2012).
tumordatasets.Rpackageversion1.4.0.https://doi.org/10.18129/B9.bioc. 58. Anders,S.&Huber,W.Differentialexpressionanalysisforsequencecount
aracne.networks(2017). data.GenomeBiol.11,R106(2010).
25. Weinstein,I.B.Cancer.Addictiontooncogenes--theAchilleshealofcancer. 59. Alvarez,M.J.etal.Correlatingmeasurementsacrosssamplesimproves
Science297,63–64(2002). accuracyoflarge-scaleexpressionprofileexperiments.GenomeBiol.10,R143
26. Margolin,A.A.etal.ARACNE:analgorithmforthereconstructionofgene (2009).
regulatorynetworksinamammaliancellularcontext.BMC.Bioinform.7,S7 60. Gautier,L.etal.affy--analysisofAffymetrixGeneChipdataattheprobelevel.
(2006). Bioinformatics20,307–315(2004).
27. Thorgeirsson,S.S.&Grisham,J.W.Molecularpathogenesisofhuman 61. Du,P.etal.lumi:apipelineforprocessingIlluminamicroarray.
hepatocellularcarcinoma.Nat.Genet.31,339–346(2002). Bioinformatics24,1547–1548(2008).
28. Bosl,G.J.&Motzer,R.J.Testiculargerm-cellcancer.N.Engl.J.Med.337, 62. Gensert,J.M.&Goldman,J.E.Heterogeneityofcyclingglialprogenitorsin
242–253(1997). theadultmammaliancortexandwhitematter.J.Neurobiol.48,75–86(2001).
29. Kolodziejczyk,A.A.etal.SinglecellRNA-Sequencingofpluripotentstates 63. Canoll,P.D.etal.GGF/neuregulinisaneuronalsignalthatpromotesthe
unlocksmodulartranscriptionalvariation.CellStemCell17,471–485(2015). proliferationandsurvivalandinhibitsthedifferentiationofoligodendrocyte
30. Lei,L.etal.Glioblastomamodelsrevealtheconnectionbetweenadultglial progenitors.Neuron17,229–243(1996).
progenitorsandtheproneuralphenotype.PLoSONE6,e20041(2011).
31. Sonabend,A.M.etal.Murinecelllinemodelofproneuralgliomafor
evaluationofanti-tumortherapies.J.Neurooncol.112,375–382(2013). Acknowledgements
32. Phillips,H.S.etal.Molecularsubclassesofhigh-gradegliomapredict ThisworkwassupportedbyUSNationalInstitutesofHealthgrantsR35CA197745-
prognosis,delineateapatternofdiseaseprogression,andresemblestagesin 03andU01CA217858.
neurogenesis.CancerCell9,157–173(2006).
33. Verhaak,R.G.etal.Integratedgenomicanalysisidentifiesclinicallyrelevant
Author contributions
subtypesofglioblastomacharacterizedbyabnormalitiesinPDGFRA,IDH1,
EGFR,andNF1.CancerCell17,98–110(2010). A.C.andM.J.A.conceivedandinitiatedtheproject.H.D.,M.J.A.,andE.F.D.performed
34. Ceccarelli,M.etal.Molecularprofilingrevealsbiologicallydiscretesubsets theanalysis.A.M.S.,A.M.,andP.D.C.preparedGBMmousemodel.S.B.,C.G.,andP.A.S.
andpathwaysofprogressionindiffuseglioma.Cell164,550–563(2016). generatedscRNA-Seqprofiles.H.D.,M.J.A.,andA.C.preparedthemanuscript.
NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications 9
ARTICLE
NATURECOMMUNICATIONS|DOI:10.1038/s41467-018-03843-3
Additional information Open Access This article is licensed under a Creative Commons
SupplementaryInformationaccompaniesthispaperathttps://doi.org/10.1038/s41467- Attribution 4.0 International License, which permits use, sharing,
018-03843-3. adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
Competinginterests:M.J.A.ischiefscientificofficerofDarwinHealthInc.A.C.is Commonslicense,andindicateifchangesweremade.Theimagesorotherthirdparty
founderandequityholderofDarwinHealthInc.,acompanythathaslicensedsomeof materialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unless
thealgorithmsusedinthismanuscriptfromColumbiaUniversity.ColumbiaUniversity indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
isalsoanequityholderinDarwinHealthInc.Theremainingauthorsdeclareno article’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutory
competinginterests. regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
thecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/
Reprintsandpermissioninformationisavailableonlineathttp://npg.nature.com/ licenses/by/4.0/.
reprintsandpermissions/
Publisher'snote:SpringerNatureremainsneutralwithregardtojurisdictionalclaimsin ©TheAuthor(s)2018
publishedmapsandinstitutionalaffiliations.
10 NATURECOMMUNICATIONS| (2018) 9:1471 |DOI:10.1038/s41467-018-03843-3|www.nature.com/naturecommunications
