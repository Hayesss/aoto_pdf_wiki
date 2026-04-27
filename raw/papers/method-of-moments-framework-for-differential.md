---
source_path: /mnt/c/Users/Administrator/Zotero/storage/YD6IQBXK/Kim 等 - 2024 - Method of moments framework for differential expression analysis of single-cell RNA sequencing data.pdf
ingested: 2026-04-23
sha256: 6df50c77ab88c085
---

Resource
Method of moments framework for differential
expression analysis of single-cell RNA
sequencing data
Graphical abstract Authors
MinCheolKim,RachelGate,
DavidS.Lee,...,AlexanderMarson,
VasilisNtranos,ChunJimmieYe
Correspondence
jimmie.ye@ucsf.edu
In brief
Mementoimplementsastatisticalmodel
andafastresamplingprocedureto
estimateandcomparethemean,
variability,andcorrelationofgene
expression,allowingforthestudyof
transcriptioninadeeperyetaccurate
fashioncomparedwithtraditional
differentialexpression.
Highlights
d AstatisticalmodelforscRNA-seqdecouplesmeasurement
andexpressionnoise
d Highlyefficientresamplingallowsforwell-calibrated
hypothesistesting
d Mementoenablesstudyingcoordinatedexpressionofgenes
inresponsetoperturbations
d Mementomapslociassociatedwithgeneexpressionmean,
variability,andcorrelation
Kimetal.,2024,Cell187,6393–6410
October31,2024ª2024TheAuthor(s).PublishedbyElsevierInc.
ll
https://doi.org/10.1016/j.cell.2024.09.044
ll
OPENACCESS
Resource
Method of moments framework
for differential expression analysis
of single-cell RNA sequencing data
MinCheolKim,1,2,3RachelGate,3DavidS.Lee,3AndrewTolopko,4AndrewLu,3ErinGordon,5EricShifrut,6,7
PabloE.Garcia-Nieto,4AlexanderMarson,7,12,13VasilisNtranos,6,8andChunJimmieYe3,8,9,10,11,12,13,14,15,*
1MedicalScientistTrainingProgram,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
2UCBerkeley-UCSFGraduatePrograminBioengineering,SanFrancisco,CA,USA
3InstituteforHumanGenetics,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
4ChanZuckerbergInitiative,RedwoodCity,CA,USA
5DivisionofPulmonaryandCriticalCare,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
6DiabetesCenter,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
7DivisionofInfectiousDiseases,DepartmentofMedicine,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
8BakarComputationalHealthSciencesInstitute,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
9DepartmentofBioengineeringandTherapeuticSciences,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
10DepartmentofEpidemiologyandBiostatistics,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
11ChanZuckerbergBiohub,SanFrancisco,CA,USA
12ParkerInstituteforCancerImmunotherapy,SanFrancisco,CA,USA
13Gladstone-UCSFInstituteofGenomicImmunology,SanFrancisco,CA,USA
14DivisionofRheumatology,DepartmentofMedicine,UniversityofCalifornia,SanFrancisco,SanFrancisco,CA,USA
15Leadcontact
*Correspondence:jimmie.ye@ucsf.edu
https://doi.org/10.1016/j.cell.2024.09.044
SUMMARY
Differentialexpressionanalysisofsingle-cellRNAsequencing(scRNA-seq)dataiscentralforcharacterizing
how experimental factorsaffectthe distribution ofgene expression. However, distinguishingbetween bio-
logicalandtechnicalsourcesofcell-cellvariabilityandassessingthestatisticalsignificanceofquantitative
comparisonsbetweencellgroupsremainchallenging.WeintroduceMemento,atoolforrobustandefficient
differentialanalysisofmeanexpression,variability,andgenecorrelationfromscRNA-seqdata,scalableto
millionsofcellsandthousandsofsamples.WeappliedMementoto70,000trachealepithelialcellstoidentify
interferon-responsive genes, 160,000 CRISPR-Cas9 perturbed T cells to reconstruct gene-regulatory net-
works, 1.2 million peripheral blood mononuclear cells (PBMCs) to map cell-type-specific quantitative trait
loci (QTLs), and the 50-million-cell CELLxGENE Discover corpus to compare arbitrary cell groups. In all
cases, Memento identified more significant and reproducible differences in mean expression compared
with existing methods. It also identified differences in variability and gene correlation that suggest distinct
transcriptionalregulationmechanismsimpartedbyperturbations.
INTRODUCTION lished, maintained, and may be broken. These insights could
illuminate mechanisms underlying phenomena where geno-
Gene expression, inherently determined by a cell’s genetic type-phenotype relationships are not completely explained,
constitutionanditsenvironmentalinteractions,canexhibitfluc- suchasdestabilization,3incompletepenetrance,5andvariable
tuationsduetobothintrinsicnoise(stemmingfrommRNAtran- expressivity.6
scriptionanddegradation)andextrinsicnoiserelatedtoacell’s Thedistributionofgeneexpressionwithinapopulationofcells
specificstate.1,2Whilegeneticsandenvironmentalhistorysignif- isprimarilycharacterizedbyitsmeanandvarianceandrelated
icantlycontributetoexpressionvariabilityacrossapopulationof derived measures.7 Constitutively expressed housekeeping
cells,stochastictranscriptionalnoisecanalsoinfluencecellular genes, which undergo transcription and degradation at
responsestoperturbations,aswellascellulardevelopmentand constantrates,arepredictedtoconformtoaPoissondistribu-
differentiation.2–4Characterizinghowdeterministicandstochas- tion.Nonetheless,mostgenesdisplayover-dispersion,exhibit-
ticfactorsjointlyinfluencethedistributionofgeneexpressionis inghighervariancethanexpected,8andgeneswithinthesame
central to understanding how transcriptional control is estab- biologicalpathwayareoftentranscriptionallycorrelated.5These
Cell187,6393–6410,October31,2024ª2024TheAuthor(s).PublishedbyElsevierInc. 6393
ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-nc-nd/4.0/).
ll
OPENACCESS Resource
A
B
C
(legendonnextpage)
6394 Cell187,6393–6410,October31,2024
ll
Resource OPENACCESS
observationsareconsistentwithamodelwheretheexpression brated p values. This is particularly problematic for studies
ofrelatedgenesisregulatedbysimilarcis-regulatoryelements necessitating thousands of comparisons, as inadequately
thatinteractwithacommonsetoftranscriptionfactorsthatcycle calibrated p values violate assumptions for multiple testing
between‘‘on’’and‘‘off’’states.9Untilrecently,studyingthedis- correction. Moreover, most existing methods require an exact
tributionofgeneexpression,inparticularthejointdistributionof specificationoftheparametricmodelandlackflexibilityinincor-
multiple genes, has been technologically challenging and has poratinghierarchicalstructuresandcontinuouscovariateseffec-
beenmostlypursuedinmodelorganismsthatcanbegenetically tively. Thus, they do not explicitly account for biological and
modified.10,11 technicalreplicatesinherentlygeneratedfrommultiplexedwork-
Single-cell RNA sequencing (scRNA-seq) has emerged as a flows that accommodate a growing number of individuals or
systematic and efficient approach for profiling the transcrip- conditions.13,15,28–30MethodslikeDESCEND,whichutilizeflex-
tomesof cellsacross experimental factors,including extracel- ibly defined generalized linear models, are notable exceptions
lular stimuli,12 genetic perturbations,13,14 and natural genetic andaretheoreticallyequippedtoeffectivelyaddressthisissue.
variation.15–18 In theory, the analysis of scRNA-seq data can However, these models often encounter significant computa-
revealhowdeterministicandstochasticfactorstogethershape tionalhurdleswhenmodelingthecomplexhierarchicalstructure
the distribution of gene expression. Yet, there remains a need inherentinscRNA-seqdataandarelimitedtoaspecificmodelof
fordifferentialanalysismethodsthatcomparedistributionalpa- cell-cellvariability.31Indeed,recentstudieshavereportedastar-
rameters between cell groups, including the mean, variability, tlingunderperformanceofscRNA-seqmethodsrelativetopseu-
andgenecorrelation.Toassessdifferencesinmeanexpression, dobulkmethodswhentestingmeandifferences.19
itiscommonpracticetoperformdifferentialexpressionanalysis To address these statistical and methodological challenges,
on pseudobulk profiles, generated by aggregating transcript we present Memento, an end-to-end method that implements
countsforcellgroupsdefinedbyclustering.Whilepseudobulk a hierarchical model for estimating mean, residual variance,
approachesdonotfullyleveragesinglecellsasrepeatedmea- andgenecorrelationfromscRNA-seqdataandprovidesasta-
sures, they surprisingly outperform methods that explicitly tistical framework for hypothesis testing of these parameters
model the distribution of observed scRNA-seq data.19 More- (Figure 1B). Memento employs a multivariate hypergeometric
over,veryfewmethodsexistforassessingdifferencesingene sampling process and leverages the sparsity of scRNA-seq
expressionvariabilityandcorrelationbetweenpairsofgenes. datatoimplementabootstrappingstrategyfortheefficientsta-
Generalized differential expression analysis of scRNA-seq tisticalcomparisons oftheestimated parametersbetweencell
dataremainsaformidablechallengeduetotwopivotalstatistical groups. Through simulations and analyses of real data, we
limitations. First, decomposing the observed cell-to-cell vari- demonstratethatMementoproducesaccurateparameteresti-
abilityintoitsconstituentcomponents—biologicalandmeasure- matesoverarangeofgeneexpressiondistributionsandsam-
ment noise—presents a significant obstacle.20 This difficulty pling efficiencies, computes well-calibrated test statistics suit-
stems from the small numbers of molecules involved in the able for multiple testing correction, and achieves sublinear
biochemical reactions of both gene transcription and the runtimes. Wedemonstrate the broad applicability of Memento
scRNA-seq sampling process (Figure 1A).21 Most existing infourapplicationsaimedatelucidatinghowexperimentaland
methodsimplementparameterizedmodelsdesignedtoaccount genetic factors affect the distribution of gene expression in
for the higher-than-expected variance in the observed sparse human cells (Figure 1C). First, we conducted scRNA-seq on
transcript counts. However, these models do not explicitly 70,000trachealepithelialcellsstimulatedwithextracellularinter-
modelmeasurementnoise,abyproductoftheinherentunder- ferons (IFNs) and investigated how stimulation modulates the
sampling characteristics of scRNA-seq workflows.22–27 Impor- variability and correlation of response genes temporally. Sec-
tantly, accurately estimating biological variability is crucial for ond,weperformedPerturb-seqon170,000Tcellsandmapped
effectivelymodelingthecorrelationbetweengenepairs.22Sec- gene-regulatory networks that define aspects of broad T cell
ond,establishingthestatisticalsignificanceofaspecificcom- activation.Third,wereanalyzed1.2millioncellscollectedfrom
parison of mean, variability, or gene correlation between cell 250 individuals to identify genetic variants associated with
groups remains a largely unsolved problem. Many existing mean, variability, and gene correlation in specific cell types.
methodsutilizeasymptotictheorytodeterminethesignificance Finally,weimplementedanapproximatebootstrappingstrategy
of hypothesis tests comparing means, often producing uncali- utilizing the Chan Zuckerberg Initiative (CZI) CELLxGENE
Figure1. Mementoworkflowfordifferentialmean,variability,andgenecorrelationtesting
(A)Experimentalworkflowforsingle-cellRNAsequencing(scRNA-seq)samplesRNAtranscriptsinsideeachcellduringlibrarypreparationandsequencing.After
scRNA-seq sampling, patterns of mean, variability, and correlation of gene expression in the observed transcript counts no longer resemble the actual
distribution.
(B)MementomodelsscRNA-seqasahypergeometricsamplingprocess,estimatesexpressiondistributionparameters(mean,residualvariance,andcorrelation)
usingmethod-of-momentsestimators,implementsefficientbootstrappingforestimatingconfidenceintervals(CIs),andtestsfordifferencesinexpression
parametersbetweentwogroupsofcells.
(C)FourapplicationsofMementotocharacterizetheresponseof(cid:1)70,000humantrachealepithelialcellstoextracellularcytokines,reconstructgene-regulatory
networksfrom(cid:1)170,000humanCD4+ TcellsperturbedbyCRISPR-Cas9,mapthegeneticdeterminantsofgeneexpressionin1.2Mperipheralblood
mononuclearcells(PBMCs)from162systemiclupuserythematosus(SLE)patientsand99healthycontrols,andcomparisonsofarbitrarygroupsofcellswithin
theCELLxGENEDiscoverdatacorpus.
SeealsoFigureS1.
Cell187,6393–6410,October31,2024 6395
ll
OPENACCESS Resource
DiscoverCensusApplicationProgrammingInterface(API),facil- (MoM) estimators for the first (mean), second (variance), and
itatingthedeploymentofMementofornearreal-timecompari- mixed(covariance)momentsofX givenY undertheassump-
c c
sons of any arbitrary cell groups within the 50-million-cell tionofhypergeometricsampling(seeSTARMethodsforderiva-
CELLxGENE data corpus. Across these diverse applications, tionanddetails):
Mementoconsistentlyidentifiedmoresignificantandreproduc-
ible differences in mean expression between experimental mb =P 1 r(cid:3);wherer(cid:3)istheGood-Turingcorrected
groupscomparedwithexistingmethods.Italsoidentifieddiffer- g;memento N c g g
c
ences in expression variability and gene correlation, thereby
revealing distinct modes of transcriptional regulation imparted countofgeneg
b co y m p p e a r t t i u b r le ba w ti i o th ns s . ca M n e p m y,3 e 2 nt a o nd is ca i n mp b l e em do e w nt n e l d oad in ed P a y t th h o tt n p , s: i / s / bs2 g;memento = n 1 c Y c 2 g (cid:4) N Y 2 cg q ð 2 1 (cid:4) qÞ (cid:4) mb2 g
github.com/yelabucsf/scrna-parameter-estimation. cells c
X
RESULTS
bs
gigj ;memento
=
n
1 Y
N
cg
2
i Y
q
c
2
gj (cid:4) mb
gi
mb
gj
cells c c
StatisticalmodelofscRNA-seq While the mean can be directly used to test for differential
Since its advent, scRNA-seq has yielded sparse data despite meanexpression(DM),thevarianceneedstobeadjustedtoac-
continuous advancements in molecular biology, manifesting in countfortheexpecteddependencebetweenmeanandvariance
ahighdegreeofcell-to-cellvariabilityeveningeneticallyiden- incountdata,therebyenablingthetestingfordifferentialexpres-
ticalcellsexposedtothesameenvironment(Figure1A).Decom- sionvariability(DV)independentofDM.33,34Todoso,weintro-
posing this variability into components of biological and mea- ducetheresidualvariances~ asameasureofexpressionvari-
g
surement noiseispivotal fordifferential expressionanalysis of abilitys (STARMethods),definedasthevariancecomponent
g
scRNA-seqdata. unexplained by the mean (STAR Methods). Consequently,
Here, we propose a statistical framework that models gene correlations are the covariance terms (off diagonal ele-
observed scRNA-seq counts as the result of hypergeometric ments) scaled by the variance terms (diagonal elements) from
samplingoftheexpressedtranscriptswithinacell.Themotiva- thevariance-covariancematrixestimatedabove.
tion to implement the hypergeometric model stems from the WeperformedextensivesimulationstocompareMemento’s
observation that the capture of poly-adenylated mRNA for hypergeometricestimatorstothenaiveplug-inestimatorsem-
reverse transcription (RT) and sequencing of resultant libraries ployedbyscHOT,35empiricalBayesestimatorsunderthePois-
are processes that sample molecules from each cell without sonapproximationintroducedbyZhangetal.36(aspecialcase
replacement, thereby introducing measurement noise into the of the Memento estimator for setting q = 0), and estimates
finaldataset.Centraltoourmodelistheflexibilitytoaccommo- derived from BASiCS27 (see STAR Methods for forms of the
datearbitrarydistributionsofgeneexpressionwithinacellprior naive and Poisson estimators). Across a range of q values,
tomeasurement.Formally,letX c = N Z c c denoteanm-dimensional Memento’s hypergeometric estimator produced accurate esti-
random variable representing thenormalized transcript counts mates of mean (Lin’s concordance correlation coefficient—
ofmgenesincellc,whereZ definesavectoroftheexpressed r >0:8with10cellsand>0:98with100cells),residualvariance
c c
transcriptcountsandN thetotaltranscriptcountswithinacell. (r >0:98,100cells),andgenecorrelation(r >0:98,100cells)
c c c
We model scRNA-seq as a multivariate hypergeometric sam- (Figure2A).Inaddition,Mementoproducesstableresidualvari-
plingprocess,whereintheobservedtranscriptcountsY origi- anceandgenecorrelationestimatesacrossqs,outperforming
c
natefromX :Y (cid:1)MultiHGðN X ;N ;N qÞ.Inthisrepresenta- other estimators for both low- and high-efficiency scRNA-seq
c c c c c c
tion, q signifies the overall transcript sampling efficiency of workflows.Whileallestimatorshavehigheraccuracyforhighly
scRNA-seq and is associated with measurement noise intro- expressed genes, Memento outperforms other methods even
duced during library preparation and sequencing (see STAR forlowlyexpressedgenes(FigureS1C).Thesesimulationsare
Methods for detailed exploration). Importantly, we empirically basedona single-step samplingapproach, which,asdemon-
substantiate that thetwo-step noise process involving RT (hy- stratedabove,effectivelyapproximatesthetwo-stepsampling
pergeometric) and sequencing (binomial) can be well repre- processmodelingRTandsequencing.
sentedwithasinglestepofhypergeometricsamplingwiththe To further validate the accuracy of Memento’s parameter
overallq(FigureS1A).Acrossmanysimulatedvaluesofcapture estimates,wereanalyzedadatasetcomprisingpaireddroplet-
efficiencyandsequencingsaturation,thesingle-stephypergeo- basedscRNA-seq(DropSeq)andsingle-moleculefluorescence
metric sampling closely approximates the two-step process insituhybridization(smFISH)data.37Thisdatasetwaspreviously
(nonsignificantKolmogorov-Smirnovtest;FigureS1B). analyzedusingSAVER,38animputationmethodthatborrowsin-
formationfromsimilargenesandcellsforestimatinggenecorre-
Estimatingdistributionalparametersofgene lations that has been shown to outperform other approaches
expressionfromscRNA-seq (Figure2B).ForgenesprofiledusingbothDropSeqandsmFISH,
To our knowledge, this is the first use of the hypergeometric Memento’s mean estimates exhibited modest improvements
samplingprocessformodelingscRNA-seqdata,alikelyresult overthenaiveestimatorusedbyothermethodswhenveryfew
of the complexity in estimating distribution parameters via cellsareused(21genesconsidered;r=0.58andr=0.54,using
maximum likelihood. Here, we derive method of moment 100 cells). For residual variance, Memento’s estimates were
6396 Cell187,6393–6410,October31,2024
0.8
0.6
0.4
0.0 0.1 0.2
0.7
0.6
0.5
0.4
500 1000 5000 8000
0.8
0.6
0.4
0.2
0.0 0.2 0.4 0.6 0.8
FDR
rewoP
0.4
0.3
memento 0.2
BASiCS
0.1
0.0 0.2 0.4 0.6
FDR
rewoP
ll
Resource OPENACCESS
A
1.0
0.8
memento memento memento
memento (q=0) memento (q=0)
naive 0.6 BASiCS BASiCS (N/A)
naive naive
0.2 0.4
B
0.62
memento
memento (q=0)
SAVER
0.60 BASiCS (N/A) naive
SCVI
0.58 memento m m e e m m e e n n t t o o (q=0)
SAVER (N/A)
naive BASiCS
memento (q=0) naive
0.56 BASiCs SCVI (N/A)
100 500 1000 5000 8000
C
memento
scHOT
D E
(legendonnextpage)
Cell187,6393–6410,October31,2024 6397
ll
OPENACCESS Resource
(cid:2) (cid:3)
significantlymorecorrelatedwiththoseobtainedbysmFISH(14 Multinomial N;n1.nK , proportional to the observed frequency
N N
genesconsidered;r=0.71)thanthenaiveestimator(r=0.56) ofeachcount(FigureS2C),asopposedtoresamplingindividual
and BASiCS (r = 0.61) using all available 8,498 cells. Finally, cells’ counts froma multinomial distribution comprising N ele-
(cid:2) (cid:3)
forgenecorrelation,Memento(r=0.53)alsosignificantlyout- ments(cells)(Multinomial N;1.1 39).Thisapproachculminates
N N
performsthenaiveestimator(r=0.29),SAVER(r=0.38),and infittingamarkedlysmallweighteddatasetðK (cid:5) NÞforeachre-
scVI (r = 0.23) using all cells. Importantly, Memento produces
samplingiteration.Toaccommodatemultiplexedexperiments,
better estimatesof gene correlation withoututilizing additional
we extend our boostrapping strategy using a meta-regression
genesrequiredbyimputationmethods(e.g.,SAVER)andvaria-
framework,consideringeachreplicateasaseparatesubgroup
tionalinferencemethods(e.g.,scVI).Thisadvantagetranslates
of the data, thereby enabling hierarchical resampling. This
not only to computational efficiency in estimation (Memento,
approachallowsustoquantifyuncertaintywhilerespectingthe
17 s vs. SAVER, 30 min for 14 gene pairs) but also produces
processwithwhichthedataweregenerated,suchassampling
estimates that might be better suited for specific downstream
ofcellsfromdifferentindividuals.Insimulation,Memento’sboot-
analyses, such as genetic mapping, where imputation could
strapping strategy yields highly accurate estimates of the null
inadvertently introduce confounding effects. These results un-
distribution for mean, residual variance, and gene correlation
derscore the accuracy of Memento’s parameter estimates,
comparabletothoseobtainedwithnaivebootstrapresampling
demonstrated through both simulations and comparative ana-
acrossawiderangeofgenes(FiguresS2DandS2E).Utilizing
lysesagainstbenchmarksmFISHdata.
bootstrapping to quantify the CI in parameter estimates, Me-
mento computes well-calibrated empirical p values for DM,
Hypothesistestingusinghighlyefficientbootstrapping DV,anddifferentialcorrelation(DC),suitableformultipletesting
The goal for hypothesis testing is to determine if an observed correction(FigureS2F).
difference in estimated parameters between cell groups, such ToshowthatMementoproducesaccurateestimatesoffalse
asmean,variability,andgenecorrelation,isstatisticallysignif- positiveswhilemaintaininghighstatisticalpower,wesimulated
icant in comparison to a null hypothesis. A primary concern adatasetencompassingtwodistinctcellpopulations.Tomain-
whentestingthousandsofgenes,typicalinscRNA-seqexper- tainrelevancetoactualdata,parametersextractedfromareal
imentsprofilingtheentiretranscriptome,isthemultipletesting datasetofCD4+ Tcellspre-andpost-stimulationwithrecombi-
problem: nominating a feasible set of candidate genes for nant IFN-b (rIFNB) were employed. Weshow that for DM, DV,
experimental follow-up while predicting the expected number andDC,Mementoestimatedtheexpectednumberoffalsepos-
of validations. Consequently, the appropriate calibration of itivesataspecifiedsignificancecutoffwhileachievingthehigh-
theteststatisticsunderthenullhypothesisamenabletomulti- estpowerfordetectingtrueparameterdifferences(Figure2C).
pletestingcorrectionbecomesimperative.Althoughemploying Moreover,weobservedthatexistingscRNA-seqDMmethods
MoMsestimationofferscomputationalefficiencyandmodeling aretooliberal(ttest,Wilcoxonrank-sumtest)whilepseudobulk
flexibility, establishing the statistical significance of estimated DMmethodsarefartooconservative(edgeR,DESeq2),consis-
parameters necessitates the computation of confidence inter- tentwithresultsfromSquairetal.19(FigureS3A).Squairetal.
vals (CIs) through bootstrapping of the data. Bootstrapping previouslyattributed thisresult to replicate-level heterogeneity
large numbers of cells using a standard scheme that samples presentinmostscRNA-seqdatasetsandrecommendedpseu-
cells with replacement would require extensive computational dobulk methods to simplify the hierarchical structure.19 By
resourcesthatarebothtimeandmemoryprohibitive,especially directlyaccountingforthehierarchicalstructure,Mementopro-
for largedatasets. ducedexpectedfalsepositiverates(FPRs)ateachsignificance
Mementoimplementsashufflingschemethatcapitalizeson thresholdevenwhenvaryingdegreesofheterogeneouseffects
the sparsity of scRNA-seq data to facilitate fast, memory-effi- are present. In addition to simulations, we also benchmarked
cient, and highly parallelizable bootstrapping. Our scheme is Memento using paired single-cell and bulk RNA-seq samples,
based on the key observation that the number of unique employingdatasetsusedbySquairetal.19(Figure2D,left)and
observedtranscriptcountsissubstantiallysmallerthanthenum- anadditionaldatasetfromsystemiclupuserythematosus(SLE)
ber of cells (Figure S2A), and this held true even for unique patients (Figure 2D, right).40 In both datasets, Memento pro-
observedpairsofcounts(FigureS3B),albeittoalesserextent. duced DM results from the scRNA-seq data most concordant
Therefore,eachbootstrapiterationnecessitatesmerelythere- with those obtained from analyses of bulk RNA-seq. Finally,
sampling of K unique transcript counts for each gene from Memento identified the greatest number of concordantly
Figure2. PerformanceofMementoinsimulationandonrealdata
(A)Lin’sconcordanceofestimatesofmeanusing10cells(left),variabilityusing100cells(middle),andgenecorrelationusing100cells(right)withsimulated
groundtruthvalues(yaxis)forarangeofoveralltranscriptcaptureefficiencies(xaxis).Shadedregionindicatesthestandarderror.
(B)PearsoncorrelationofMementoestimatesfromDropSeqdatavs.smFISHestimatesofthesamepopulationofmelanomacells(yaxis)formean(left),
variability(middle),andgenecorrelation(right)acrossdifferentnumbersofDropSeqcellsused(xaxis).Shadedregionindicatesthestandarderror.
(C)Power(yaxis)vs.falsediscoveryrate(FDR)(xaxis)comparingexistingmethodswithMementoforDM(left),DV(middle),andDC(right)analyses.
(D)ConcordanceAreaUndertheCurve(AUC)(xaxis)ofsingle-cellDManalysis(green)comparedwithpseuobulkDManalysis(red)usingdatasetsinSquair
etal.19andPerezetal.17
(E)Runtime(yaxis)ofthreemethodsacrossnumberofcells(xaxis)forDMandDVanalyses.
SeealsoFiguresS2andS3.
6398 Cell187,6393–6410,October31,2024
2
1
0
−1
canon non
canon
ytivitisneS
cinoT
ll
Resource OPENACCESS
A C
B
D
E F G
Figure3. MappingtranscriptionalresponseofHTECstoextracellularinterferonusingMemento
(A)UMAPsoftheentireHTECdatasetcoloredbyidentifiedcelltypes(left),zoomedinciliatedcellscoloredbystimulation(center),andtimelabels(right).
(B)Logfold-change(LFC)ofmeanexpressioninresponsetoIFN-a(xaxis)againstLFCinresponsetoIFN-b(left),IFN-g(middle),andIFN-l(right)after6h.
(C)HierarchicallyclusteredheatmapsofLFCinresponsetothefourtypesofinterferons(columnswithineachheatmap)across5timepoints.Type-1-(green)and
type-2-specific(blue)responsesarehighlighted.
(legendcontinuedonnextpage)
Cell187,6393–6410,October31,2024 6399
ll
OPENACCESS Resource
differentiallyexpressedgenesinciliatedcellsstimulatedbyIFN- changes (FCs) across DMGs compared with IFN-b and IFN-l
aandIFN-b,bothofwhichareknowntobeligandsofthetype-1 ðr = 0:96Þ.Bycontrast,comparedwithIFN-g,theoverallcorre-
IFNreceptor(FigureS3B). lationinFCwaslower(r = 0:70;Figure3B)duetothepresence
Compared with existing methods for DM, DV, and DC, Me- ofbothtype-1andtype-2IFN-specificDMGs.Herein,wedefine
mentoachieveshypothesistestingatcomputationalspeedsor- DMGsthatareupregulatedinresponsetoanyIFNasIFN-stim-
dersofmagnitudefaster,allowingscalabilitytomillionsofcells ulatedgenes(ISGs).HierarchicalclusteringoftheISGsacross
(Figure 2E). In a simulation comparable in scale to emerging timepointsrevealedadynamictranscriptomicresponseshared
scRNA-seqdatasets(twogroupseachcontaining106cells)con- acrossIFNs,includingtheearlyinductionofmajorhistocompat-
ductingDMandDVanalysesfor1,000genesusing10,000boot- ibilitycomplex(MHC)classIIgenesandadistinctgenecluster,
strappingiterationspergenerequiredonly13minusingasingle comprisingPLAAT2,BTN3A1,andDUOX2(Figure3C).Wealso
CPU. A multicore implementation of Memento facilitated the identifiedpatternsspecifictoeachIFN,exemplifiedbyasubset
parallelizationofmultiplegenes,furtherreducingtheruntimeto of canonical ISGs (IFIT2, IFITM2, and ISG15) that exhibited
2–3minwith6CPUs.ParticularlyforDVandDCanalyses,Me- late induction in response to IFN-l but sustained induction
mentoachievescomputationalspeedgainsupto1,0003using throughout the time course in response to type-1 IFNs (Fig-
equivalentcomputeresourcescomparedwithexistingmethods. ure 3C). Interestingly, some genes that were more induced by
TheseresultssubstantiatethatMemento’sbootstrappingstrat- oneoftheIFNs(e.g.,theMHCclassIIgenesbyIFN-g)showed
egyyieldsaccurateCIestimatesforeffectsizesathighcompu- similar temporal behavior across the other IFNs, suggesting
tationalefficiency.Thisculminatesinwell-calibratedteststatis- bothuniqueandsharedregulatorymechanisms.
tics,facilitatinghypothesistestingofscRNA-seqdatascalable While DM analysis revealed the induction of canonical and
to groups containing millions of cells (see STAR Methods for non-canonical ISGs, it did not decipher whether these genes
detaileddescriptionoftheresamplingstrategyandhypothesis weresubjecttothesametranscriptionalregulatorycontrol.To
testing). maptheIFNgenecorrelationnetworkanditssubcomponents,
weusedMementotoidentifyDCbetweenISGpairsacrossstim-
Differentialvariabilityandgenecorrelationinresponse ulationsandtimepoints(Figure3D).Agglomerativeclusteringof
toexogenousIFN theresultinggenecorrelationmatrixrevealeddistinctISGsub-
WhileIFNsarepotentcytokinesthatpromoteantiviralimmunity, setsinresponsetoIFN-b,formingclustersinunstimulatedcells,
they also play a role in the pathogenesis of inflammatory and stimulatedcells,orboth—distinctionsthatwerenotdiscernible
autoimmune diseases.41 Their action—inducing gene expres- through DM analysis alone. For example, canonical ISGs,
sionviaautocrineandparacrinesignaling—iswelldocumented; including MX1, OAS1, and IFI6, maintained high correlation
however,theheterogeneityoftranscriptomicresponsesinstim- evenwithoutexogenousIFNpresence(Figure3D,cyannodes).
ulated cells remains largely unexplored. Using Memento, we UponIFN-bstimulation,thecorrelationnetwork,initiallyconsist-
investigatedtheimpactofIFNstimulationonthedistributionof ingofcanonicalISGs,expandedtoincludenon-canonicalISGs,
geneexpressioninhumantrachealepithelialcells(HTECs).We suchastheMHCclassImoleculesandothergenesassociated
used multiplexed scRNA-seq (mux-seq) to analyze 69,958 withantigenpresentation,whichwerenotcorrelatedinunstimu-
HTECsfromtwohealthydonors,exploringconditionsincluding latedcells(Figure3D,magentanodes).Consistentwiththeclus-
unstimulated control and stimulation with various IFNs: type-1 teringanalysis,Mementoidentifiedmoredifferentiallycorrelated
(IFN-aandIFN-b),type-2(IFN-g),andtype-3(IFN-l).Analyses gene pairs (DCGs, FDR < 0.1) among non-canonical ISGs
wereconductedatseveralpost-stimulationtimepoints:3,6,9, (860 DCGs, 34% of total pairs) than canonical ISGs (421
24,and48h.Dimensionalityreduction,nearestneighboridenti- DCGs,16%of total pairs). Notably, the increase in correlation
fication, andLeidenclusteringyielded 7identifiable celltypes, between gene pairs was not explained by an increase in their
visualizedusinguniformmanifoldapproximationandprojection mean expression when considering all pairs of genes and
(UMAP): neuroendocrine cells, ionocytes, tuft cells, basal when only considering pairs with significant changes in mean
cells,basal/clubcells,gobletcells,andciliatedcells(Figure3A). (FigureS4A).
Our subsequent analyses focused solely on ciliated cells, WehypothesizedthatcanonicalISGsarecorrelatedinunsti-
which are known to be the primary target of viral infections, mulatedcellsduetothesensingoftonicIFNandthecoordinated
including SARS-CoV2, and are recognized fortheir robust IFN induction of ISGswithina select groupof cells. Tonic IFNhas
response.42–44 beendescribedasinducinganaturalgradientofISGexpression
Weidentified5,018genesexhibitingdifferentialmeanexpres- acrosscells45,46andplaysanimportantroleinviraldefense,46
sion(DMGs,falsediscoveryrate[FDR]<0.01)betweenunstimu- immunecellhomeostasis,andautoimmunity.45Withinourdata-
latedciliatedcellsandthosestimulatedbyanyoffourIFNsat6h. set,canonicalISGsexhibitedgreatervariabilitycomparedwith
AcomparativeanalysisrevealedthatIFN-ainducessimilarfold non-canonical ISGs in unstimulated cells (Figure 3E), aligning
(D)Genecoexpressionnetworkovertime,wherecyannodesdepictcanonicalISGsandmagentanodesdepictnon-canonicalISGs.Pairsofgeneswithhigh
correlation(Mementor>0.6)areconnected.
(E)Baselineexpressionvariability(yaxis)vs.mean(xaxis)inciliatedcells.
(F)Tonicsensitivity(yaxis)forcanonicalandnon-canonicalISGs(xaxis).***p<0.001.
(G)Changeinvariability(yaxis)vs.thechangeinthemean(xaxis)inresponsetoIFN-b(left)andIFN-g(right).BluedotsrepresentcanonicalISGs.
SeealsoFigureS4.
6400 Cell187,6393–6410,October31,2024
ll
Resource OPENACCESS
(legendonnextpage)
Cell187,6393–6410,October31,2024 6401
ll
OPENACCESS Resource
withpreviouslydocumenteddifferencesinexpressionvariability multiple rounds of selection and proliferation, activated CD4+
betweencytokinesandnon-cytokines(FigureS4B).47Outofthe Tcellsfrom9donorswereprofiledusingmux-seq.
761differentiallyvariablegenes(DVGs,FDR<0.1)identifiedus- ToevaluatethecuttingefficiencyofeachsgRNA,weconduct-
ing Memento between unstimulated ciliated cells and those ed targeted amplification sequencing of 268 out of 280 loci in
stimulatedbyanyofthefourIFNsat6h,394werehighlyvariable both the sgRNA pool and the DNA of edited cells from each
inunstimulatedcells(FDR<0.005)andwereenrichedforcanon- donor.Themeancuttingefficiencyacross268sgRNAs,defined
ical ISGs (GSEA IFN-a/IFN-b signaling adjusted p = 3.35 3 as the fraction of sequencing coverage of edited cells at the
10(cid:4)12),includingIFIT1,IFIT3,andMX1. targetlocustosequencingcoverageofitsrespectivesgRNAin
WenextassessedthesensitivityofeachISGtotonicIFN,esti- the pool, was estimated at 21%, with a standard deviation of
matedastheFCingeneexpressionbetweenmacrophagesfrom 15% (Figure S5A). Fourteen sgRNAs, exhibiting cutting effi-
Ifnar knockout and wild-type (WT) mice without exogenous ciencies below 2.0% (standard deviation 1.7%; Z score,
IFN.48 This analysis revealed that canonical ISGs are signifi- pP<0.05),were designated asuncut negativecontrols (WT).
cantly more sensitive to tonic IFN than non-canonical ISGs The robustness and efficacy of our screen were substantiated
(pP<2.73310(cid:4)10;Figure3F).Notably,uponstimulationwith throughtwoqualitycontrolanalyses.First,weutilizedMemento
IFN-b(and,toalesserextent,withIFN-g),thevariabilityofsub- toconfirmthattargetgenesincellstransducedwiththerespec-
stantial proportion of canonical ISGs reduced (78% and 39%, tivesgRNA were significantly downregulated (Figure4B).Sec-
respectively; Figure 3G, FDR < 0.1), implying that exogenous ond, a higher correlation in average gene expression was
stimulation homogenizes the cellular environment, removing observedbetweeneitherWTcells(r=0.50)orcellstransduced
theeffectsofheterogeneousresponsetotonicIFN. withsgRNAstargetingthesamegene(r=0.44),ascompared
Our findings underscore the power of Memento to analyze withcellstransducedwithsgRNAstargetingtwodistinctgenes
geneexpressiondistributionsanduncovertranscriptionalreg- (r=0;KStestP < 2:2x10(cid:4)16forboth;FigureS5B).
ulatory networks influenced by IFN signaling. By leveraging UtilizingMemento,weidentified7,641genes(FDR<0.05)with
Memento to dissect effects on mean, variance, and correla- DMGswhencomparingWTcellswithcellsperturbedbyatleast
tion in gene expression, we have illuminated complex onesgRNA.Hierarchicalclusteringofmeangeneexpressionfor
regulatory interactions that dictate cellular behavior in the DMGs across sgRNAs revealed clusters of sgRNAs exerting
presence and absence of IFN, offering new perspectives on similar transcriptomic effects and clusters of genes similarly
how cells modulate their transcriptomic response to environ- responsivetosuchperturbations(Figure4C).Weidentifiedfive
mental cues. clusters of DMGs distinctly associated with ribosomes
(FDR<5.35310(cid:4)24),cytotoxicity(FDR<0.014),antigenpre-
DifferentialexpressionanalysisofperturbedCD4+ sentation(FDR<0.0011),andproliferation(FDR<0.001).More-
Tcellsmapsgene-regulatorynetworksinTcell over, the pairwise correlation matrix of DMGs, as computed
activation using Memento, revealed additional sub-clusters within each
IntegratingCRISPR-Cas9-mediatedgenomicperturbationswith oftheinitialfiveDMGclusters,persistinginbothWTandper-
scRNA-seq profiling creates new opportunities for conducting turbed cells (Figure 4C). Intriguingly, while antigen processing
forwardgeneticscreensindiverseinvitrosystems.UtilizingMe- genes’ mean expression is modulated by a shared set of
mento,weanalyzed(cid:1)173,000CRISPR-Cas9perturbedhuman sgRNAs,asubsetofMHCclassIIgenes—namelyHLA-DPA1,
CD4+Tcellstomaptranscriptionalregulatorynetworksmodu- HLA-DRA,HLA-DRB1,andHLA-DPB1—exhibitedstrongcorre-
latingtheiractivationandpolarization.Cellswereperturbedus- lation, suggesting that their coordinated expression may be
ing pooled single-guide RNA (sgRNA) lentiviral infection with controlledbyadditionaltransregulators.
Cas9proteinelectroporation(SLICE),49followedbymux-seq.15 InexploringtheutilityofMementofordetectingalterationsin
Utilizing a set of 280 sgRNAs, we targeted 140 transcriptional genecorrelations,wehypothesizedthatidentificationofgenetic
regulators (TRs), chosen for their high expression (within the interactionsbetweenTRsmightbepossiblewithoutconducting
topquartilefrombulkRNA-seq)orthedifferentialaccessibility combinatorial perturbations. To test this hypothesis, we per-
of their binding sites (as detected by bulk assay for transpo- formedageneticinteractionanalysisfocusedonpairsconsisting
sase-accessiblechromatinwithsequencing[ATAC-seq])inacti- of DMGs and their TRs, referred to as TR-DMGs (see STAR
vatedCD4+Tcells50(Figure4A).AfterCas9electroporationand Methods). Specifically, we focused on regulators that, when
Figure4. Reconstructinggene-regulatorynetworksofTcellactivationusingPerturb-seqandMemento
(A)Selectioncriteriaforperturbedregulatorsinthisstudy,basedonexpression(top)andbindingsiteenrichment(bottom).
(B)Heatmapofaveragegeneexpressionforeachgene(row)acrosscellsperturbedbythecorrespondingsgRNA(columns).
(C)Left:heatmapofaveragegeneexpressionforDMGs(row)acrosscellsperturbedbyeachsgRNA(columns).Right:gene-genecorrelationmatrixforthesame
DMGsestimatedfromWTcells.
(D)CorrelationbetweeneachregulatoranditsdownstreamtargetsinWTcells.
(E)Bipartitegene-regulatorynetworkthatdonotaccountforinteractionsbetweenregulatorsconstructedfromDManalysisofPerturb-seqdata.
(F)Gene-regulatorynetworkincludinggeneticinteractionsbetweenregulatorsconstructedutilizingbothDMandDCanalysis.
(G)Numberofgeneswithbindingsitesforpairsofinteractingornon-interactingregulatorsacrossvaryingwindowsaroundtheTSS.Errorbarindicatesthe
standarderror.
(H)ChromosomallocationofLGALS3BPandbindingsitesforIRF1andPRDM1,predictedtointeractusingDMandDCanalysis.
SeealsoFigureS5.
6402 Cell187,6393–6410,October31,2024
B C
D E
skaeP
qes-CATA
A
1.0
0.8
0.6
0.4
0.0 0.5 1.0
False positive rate
F
H
rewoP
0.5
0.4
memento 0.3
pseudobulk
0.2
50607080
50.0=αtarewoP
memento
pseudobulk
memento pseudobulk
T4 B cM NK
0.5 0.7 0.4
0.6
0.4 0.3
0.5
0.3
0.2 0.4
0.2
0.3
50607080 50607080 50607080
Number of individuals
memento pseudobulk
ncM / mye
cM / mye
NK / nk
T8 / nk
T8 / T
T4 / T
B / B
B T4 T8 NK cM ncM
0 5
cell type
zscore of rank sum statistic
G
G/G G/A A/A
G/G G/A A/A
I
A/A A/G G/G
A/A A/G G/G
B
T
kn
dioleym
Memento
B T4 T8 NK cM ncM
cell type
B
T
kn
dioleym
Pseudobulk
6
5
4
3
2
1
Enrichment
-Log10(P)
ll
Resource OPENACCESS
(legendonnextpage)
Cell187,6393–6410,October31,2024 6403
ll
OPENACCESS Resource
knocked out, lead to decreased expression of the DMGs. they are hampered by computational inefficiency, a restricted
Consistent with our expectations, TR-DMGs typically show a focusonmeancomparisons,andsusceptibilitytomisspecifica-
positive correlation with each other within WT cells (Binomial tionintheunderlyingparametricmodel.52Wepositthat,incom-
test,p<0.00668;Figure4D). parisontopseudobulkmethods,Memento’ssuperiorparameter
Intheabsenceofageneticinteraction,twoTRs(R1andR2) estimationaccuracyandcapacitytoaccountforintra-andinter-
could independently regulate the target gene (G); therefore, a individualvariationduringinferencewillresultinincreasedpower
knockoutofoneregulatorshouldostensiblynotimpairthefunc- to detect cis-eQTLs and the discovery of novel variability and
tionalityoftheother(Figure4E).Bycontrast,inthepresenceof correlation QTLs (vQTLs and cQTLs, respectively). Moreover,
an interaction, a knockout of one regulator (e.g., R1) could the implementation of a highly efficient hierarchical bootstrap-
impactR2’sregulatorycapacityoverG.Thiseffectcouldbede- ping strategy promises applicability to expansive, population-
tectedasachange inthe genecorrelation betweenR2 andG scale scRNA-seq datasets, which could be computationally
when R1 is perturbed (Figure 4F). Employing this strategy, we insurmountableforparametriclinearmixedmodels.Todemon-
identified564geneticinteractionsamidst432uniqueregulator strate, we applied Memento to reanalyze a pre-existing
pairs(FDR<0.1,Figure4F).Validatingtheseinteractions,ana- scRNA-seq dataset, comprising 1.2 million peripheral blood
lysesincorporatingchromatinimmunoprecipitationsequencing mononuclearcells(PBMCs)derivedfrom162SLEpatientsand
(ChIP-seq)datafromENCODE51showthatinteractingTRpairs 99healthydonors.
are more likely to have co-localized binding sites proximal to Thedatawereanalyzedseparatelyforeachofthereportedcell
thetranscriptionstartsite(TSS)oftargetgenesthannon-interac- types:CD4+ Tcells(T4),CD8+ Tcells(T8),naturalkiller(NK)
tionpairs(Figure4G). cells,classicalmonocytes(cMs),andnon-classicalmonocytes
Asanexample,weidentifiedthatIRF1regulatesLGALS3PB (ncMs).17 Individuals of East Asian and European ancestries
(evidentfromDMexpressionanalysis)andretainsastrongcor- were separately analyzed, with subsequent comparisons
relationwithLGALS3PBinWTcells(r =0.28).Aknockoutof enabling a replication analysis between these populations.
WT
PRDM1precipitatedasignificantdecreaseinthecorrelationbe- Foreverydistinctcelltypeandancestrygroup,Mementomap-
tween IRF1 and LGALS3PB (Dr = (cid:4)0.38), implying a potential pedcisgeneticvariants—specifically,thosewithin100kbfrom
interaction between PRDM1 and IRF1 in the regulation of the TSS—associated with mean expression, expression vari-
LGALS3PB. Consistent with these observations, LGALS3BP ability,andgenecorrelation,producingwell-calibratedpvalues
hasbindingsitesforbothIRF1andPRDMB1intheimmediatevi- (Figure5A).
cinityofitsTSS(Figure4H). Acomparative analysisbetweenthepowerand FPRofMe-
TheseresultsdemonstratethecapabilityofMementoforthe mentoandMatrixeQTLindetectingcis-eQTLswasestablished
analysesofforwardgeneticPerturb-seqscreens.Wehighlight against benchmarks provided by the OneK1K study, which
the potential for DC analyses in delineating gene sets sharing comprised of 1,000 non-overlapping individuals.18 Notably, in
regulatoryelements—albeitparticipatingindiversepathways— both East Asian and European cohorts, Memento exhibited
and to reconstruct the genetic interactions of trans regulators higherpowerinidentifyingcis-eQTLs(AUC=0.85),surpassing
orchestratingTcellactivation. Matrix eQTL (AUC = 0.81) while maintaining equivalent FPR
(Figures 5A and 5B). Overall, Memento outperformed Matrix
Geneticanalysisofpopulation-scalescRNA-seq eQTL in both populations, replicating 1,606 vs. 855 cis-eQTLs
TheincreasingavailabilityofscRNA-seqdatasetsonapopula- acrosscelltypesinEastAsiansand,similarly,1,778vs.958in
tionscalehaspavedthewayformappinggeneticvariantsasso- Europeans.Moreover,spanningarangeofcohortsizescommon
ciated with changes in the expression distribution of proximal formux-seqexperiments,Mementoachievedanaveragepower
genes (cis) in specific cell types. Prevailing studies predomi- gainof15%for80individuals—ametricthatincreasedto32%
nantly utilize pseudobulk methods, such as matrix expression for 50 individuals, given an average of 440 cells per individual
quantitativetraitloci(eQTLs),toidentifyciseQTLs(cis-eQTLs) (Figure5C).
impacting mean expression. While linear mixed models have Wesubsequentlyexploredwhethertheincreasednumberof
been recently applied to map cis-eQTLs in scRNA-seq data, cis-eQTLsdetectedbyMementoalsoimprovestheenrichment
Figure5. MappingofmeanQTL(eQTL),vQTL,andcQTLusingMemento
(A)Quantile-quantile(QQ)plotsforexpectedpvalues(yaxis)computedbyMementovs.theoreticalpvalues(xaxis)foreQTLs,vQTLs,andcQTLs.ForeQTLs,the
QQ-plotofpvaluesfrompseudobulkapproach(matrixeQTL)isoverlayed.
(B)Receiveroperatingcharacteristic(ROC)curvesforrecoveryofeQTLsidentifiedfromamuchlargercohort(OneK1K)forMementoandpseudobulk-based
matrixeQTL.
(C)PowerofeQTLrecovery(yaxis)ofMementoandmatrixeQTLacrossdifferentnumbersofindividuals.AnalyseswereperformedonCD4+Tcells(T4),Bcells
(B),classicalmonocytes(cMs),andnaturalkillercells(NKs).
(D)Enrichmentofcell-type-specificeQTLsincell-type-specificATACpeaks.EachentryrepresentstheenrichmentforeQTLsdetectedinonecelltype(column)in
ATACpeaksdetectedinanothercelltype(row).Intensityis(cid:4)log10(pvalue).
(E)EnrichmentofeQTLsdetectedineachcelltypeforcell-type-specificATACpeaksdetectedinthesamecelltype.Errorbarindicatesthestandarderror.
(F)AnexampleofavQTL.Expressionvariability(yaxis)foreachindividualofvaryinggenotypesatchr6:31326612.
(G)HistogramshowingdistributionofHLA-Cexpressionforarepresentativeindividualofeachgenotype.
(H)AnexampleofacQTL.JUNB-LYZgenecorrelation(yaxis)forindividualsofvaryinggenotypesatchr12:69688073.
(I)ScatterplotofexpressionofLYZ(yaxis)againsttheexpressionofJUNB(xaxis)acrosssinglecellsfromalldonors(gray)andarepresentativeindividual(black).
6404 Cell187,6393–6410,October31,2024
ll
Resource OPENACCESS
withinregionsofopenchromatinandassociationswithdisease. niques that can efficiently compare datasets while ensuring
IntheEastAsiancohort,cis-eQTLsidentifiedbyMementowithin properly calibrated statistical behavior. As of November 2023,
specificcelltypesweremoreenrichedforcell-type-specificre- CELLxGENE Discover includes 50 million unique cells across
gions of open chromatin, as annotated by an unrelated study 1,102 datasets and thousands of individuals, with its Census
thatconductedATAC-seqonbulksortedimmunecells(pvalues APIprovidingaccesstomostofthesedata.53UnlikeascRNA-
formatchedcelltypes:B,9.0310(cid:4)9vs.0.04;T4,9.3310(cid:4)4vs. seq dataset generated by a single research project with a
0.11;T8,0.03vs.0.58;NK,6.67310(cid:4)8vs.0.03;cM,2.1310(cid:4)11 focused hypothesis, users of CELLxGENE Discover access
vs.0.67;ncM,1.0310(cid:4)6vs.0.46;Figures5Dand5E).Similar this resource with a diverse array of comparative analyses in
gainsinenrichmentwereobservedintheEuropeancohort(Fig- mind. For example, one user may be interested in differences
ure S5C). Linkage disequilibrium (LD) score regression (LDSC) inexpressionbetweenthesamecelltyperesidingindifferentor-
analysisfoundthatcis-eQTLsidentifiedbyMementoalsowere gan systems.Another user may beinterested in differencesin
moreenrichedforgenome-wideassociationstudy(GWAS)as- expressionforthesamecelltypebetweenindividualsofdifferent
sociations to immune-mediated diseases, thereby suggesting disease statuses. In any scRNA-seq dataset with labeled cell
improvedfine-mappingperformance(FigureS5D). types,thereisalargenumberofpossiblecomparisonsbetween
Inadditiontomappingcis-eQTLs,Mementoenablestheiden- cellgroups(Figures6Aand6B).Furthermore,multipledatasets
tificationofgeneticvariantsassociatedwithexpressionvariability may be combined to improve the power of comparisons be-
and gene correlation, offering insights into alternative mecha- tweenthesamecellgroupsthatexistacrossdatasets.
nismsbywhichgeneticvariantsmightinfluencegeneexpression. Differential expression methods powering queries within the
Utilizing Memento, we identified 10,607 expression vQTLs im- census need to efficiently perform accurate, well-calibrated
pacting733genesacrossallcelltypes.Forinstance,thevariability comparisonsbetweenuser-definedcellgroupsacrossdatasets,
inHLA-Cexpressiondifferedamonggenotypesofchr6:31326612 deliveringresultsnearreal-timespeedforwebportalintegration.
(Figure5F),withtheAalleleamplifyingtheexpressionvariabilityof Although Memento demonstrates excellent scalability with
HLA-Cwithoutnotablyaffectingitsmean(Figure5G).Formap- increasing cell numbers, as shown in Figure 2F, its real-time
pingcQTLs,wefocusedontestingthecorrelationbetweengenes result delivery is constrained by the necessity of performing
possessingatleastonesignificantcis-eQTLandknowntranscrip- bootstrapoperationsforeachcomparison,alimitationthatbe-
tion factors,thereby specifically testing the hypothesis thatge- comesmorepronouncedwhensubsetscontainmultiplebiolog-
netic variantsmight modulatethe effectof transcription factors icalandtechnicalreplicates.Toextendthebroadapplicabilityof
ongeneexpression.Wemapped3,726cQTLsfor238genepairs Memento, we collaborated with CZI to utilize the CELLxGENE
acrossallcelltypes.Forexample,theSNPatchr12:69688073is DiscoverCensusAPItoperformbootstrapoperationsandquan-
associatednotonlywiththemeanexpressionofLYZbutalsothe tify uncertainty for predefined cell groups across the entire
correlationbetweenJUNBandLYZ.Intriguingly,aJUNBbinding corpus(seeSTARMethods).Thisextensionallowsforthepre-
siteexistswithin1kbp oftheSNP,suggestingthatJUNBmay computationofstandarderrors,whicharethenutilizedtoenable
serveasatransregulatorforLYZ,withtheregulatorystrengthbe- nearreal-timedifferentialexpressionanalysisviaweightedleast
inginfluencedbythegenotypeatthisSNP. squares. Consequently, the standard errors derived from this
ThesefindingsunderscoreMementoasascalableapproach precomputed mode provide an effective approximation of the
forgeneticanalysesofpopulation-scalescRNA-seqdata,deliv- bootstrap method employed in the full mode, streamlining the
eringhigherstatisticalpowerforidentifyingcis-eQTLsandintro- analysisprocess.
ducing the capability for mapping vQTLs and cQTLs. These ToevaluatetheagreementbetweenMementoinitsprecom-
advancesnotonlyimprovethefinemappingofdiseaseassoci- puted mode and the full mode, we conducted a differential
ationsbutalsounveilnovelmechanismswherebygeneticvari- expression analysis comparing CD4+ T cells and cMs from a
antsmaymodulategeneexpression. singledonor inthe lupusdataset (referenced in Figure5), also
included in CELLxGENE Discover. Given that the analysis
Census-scaledifferentialexpressionanalysisacross involvedthesameunderlyingdata,weanticipatedhighlysimilar
celltypes,individuals,anddiseasestates results. The primary difference would be attributed to the two
The above applications showcased the broad applicability of Memento versions, with the precomputed mode utilizing esti-
Memento for generalized differential expression analysis matedcellsizesfromtheentireCELLxGENEDiscoverdataset.
acrossdiversedatasets,includingtheanalysisofthetemporal Ourexpectationswereconfirmedbyobservingarobustcorrela-
responseoftrachealepithelialcellsstimulatedbyIFNs,themap- tionintheeffectsizeestimates(FigureS6)betweenthefulland
ping of gene-regulatory networks from Peturb-seq data of approximate,precomputedmodes.Asimilarlystrongcorrelation
CD4+ T cells, and large-scale genetic analysis of scRNA-seq wasnotedinthesignificancelevels,indicatedby(cid:4)log (pvalue)
10
data collected across a population cohort. These applications (Figures6Cand6D).Importantly,thecomputationtimefordeter-
andsimulationsdemonstratethatMementoconsistentlyoutper- mining effect size and p value was significantly reduced
formsexistingmethods,deliversauniquefeaturesettocompare comparedwithexecutingMementoinfullmodeforvariouscell
variancesandcorrelationsinadditiontomeans,andisextremely groupcomparisons(Figure6E).
efficient, allowing for scalability to millions of cells and tens of AuniqueapplicationofMementoonlarge-scalecensusdata
thousandsofreplicates. lies in its improved power to compare cell groups, particularly
The emergence of massive repositories of scRNA-seq data beneficialforthosethatarerareinindividualdatasets.Toillus-
worldwide has created new demands for computational tech- trate this, we utilized Memento in its precomputed mode to
Cell187,6393–6410,October31,2024 6405
ll
OPENACCESS Resource
A B Figure6. ExtendingMementofornearreal-
time differential expression analysis within
CZICELLxGENEDiscover
(A) UMAP of the SLE PBMC dataset within
CELLxGENE.
(B)Enumerationofdifferentcomparisonsthatcan
bemadewithinandbetweengroupsofcells.
(C and D) Comparisons of significance (p value)
C D E
between the precomputed and full modes for
(C)differentialmeanand(D)differentialvariability
analyses.
(E)Runtimeasafunctionofthenumberofcom-
parisons made at query time (excluding pre-
computation).
(F)Schematicofmultiple datasets analyzed with
CELLxGENEidentifyingDMGsbetweenpDCsand
F G cDCs.
(G)QQ-plotofpvaluesfromcomparingpDCsand
cDCscombiningmanydatasets(cyan)andusing
eachdatasetalone(gray).
SeealsoFigureS6.
Here,weintroducedMemento,anend-
to-endmethodforthequantitativeanalysis
of scRNA-seq data theoretically scalable
tomillionsofcells.Mementoisdeveloped
with two pivotal innovations: MoMs esti-
identifyDMgenesbetweenconventional(cDC)andplasmacy- mators modeling scRNA-seq via a hypergeometric sampling
toiddendriticcells(pDC).Thesecelltypesconstitute5.8%and processandanefficientbootstrappingstrategytoconstructpre-
4.0%,respectively,ofthescRNA-seqdatasetsofimmunecells ciseCIs around parameter estimates, exploitingthe sparsityof
within the CELLxGENE Discover (Figure 6F). In analyzing 23 scRNA-seq data. The utilization of MoMs estimators imparts
separatedatasetsintheCELLxGENEDiscover,encompassing 2-foldadvantagesoverotherapproaches.First,ourapproachde-
362,619totalcells,wefoundthatajointanalysisacrossthese lineates biological and technicalsources of noise, enabling the
datasetssignificantlyincreasedthestatisticalpowercompared accurate characterization of biological variation. This feature of
with analyses of any single dataset (Figure 6G). These results Memento addresses recent calls for hierarchical parametric
highlight the efficiency of Memento’s moment estimators and modeling of the measurement noise of scRNA-seq while only
the adaptability of its bootstrap approach enable its effective considering biological variation for estimation and inference.22
applicationinexpansivecensusrepositories. Second, our approach circumvents the need to repetitively
computetheoveralllikelihood,enablinginstantaneouscomputa-
DISCUSSION tionofthepertinentparameters.Themultinomialapproximation
ofhypergeometricsamplinghasbeenusedtotheoreticallyderive
Fueled by the development of scalable workflows, there is an thebaselinenoiseinscRNA-seq33andtodesigndimensionality
emergenceofscRNA-seqdatasetswherethequantitativecom- reductiontechniquesforcountdata.55ThePoissonapproxima-
parisonofgeneexpressiondistributionsbetweengroupsofcells tionofthebinomial(whichinturnapproximatesthehypergeomet-
isacriticaltask.Theseincludeendeavorstocomparesingle-cell ric)hasbeenusedtoderiveempiricalBayesestimatorstoinform
expression profiles between experimental conditions,12 dispa- theoptimaldesignofscRNA-seqexperiments.36Whileouresti-
rategeneticperturbationsinducedbygenomeediting,14,54and mators are derived focusing on scRNA-seq workflows where
individuals inheriting different alleles.16–18 Initial observations cell-to-cell differences in transcript sampling frequencies q are
that experimental and genetic perturbations predominantly small, the hypergeometric formulation is amenable to models
inducesubtleshiftsingeneexpressionratherthanunequivocal where q varies significantly between compartments (e.g.,
cell states have highlighted the need for methods adept at scRNA-seq30),providedthatN and q can beestimated sepa-
c
comparing gene expression distributions. However, scalable rately.BecauseofthemodularandflexiblenatureofMemento,
computational methods that facilitate hypothesis testing over we further anticipate that our modeling framework could be
large numbers of cells and an extensive array of covariates extendedtoalternativescRNA-seqworkflowsthatusehybridiza-
(e.g., hundreds of in vitro perturbations or millions of genetic tioninsteadofreversetranscription56andspatialtranscriptomics
polymorphisms)arestillscarce.Moreover,evenfewermethods data.57Analysesofemergingmultimodalworkflows(e.g.,ATAC-
currentlytestfordifferencesinthevariabilityofgeneexpression seq and CITE-seq) should also be possible by modifying the
and gene correlations, unique parameters captured by method-of-momentsestimatorstocorrectlycapturesourcesof
scRNA-seq. technicalvariationuniquetoeachassay.
6406 Cell187,6393–6410,October31,2024
