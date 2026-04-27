---
source_path: /mnt/c/Users/Administrator/Zotero/storage/XIYPLXTJ/Yu 等。 - 2021 - Bulk and single-cell transcriptome profiling revea.pdf
ingested: 2026-04-23
sha256: 9b2e4592d6f55bf8
---

Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
Original Article
Bulk and single-cell transcriptome
profiling reveal the metabolic
heterogeneity in human breast cancers
Tian-Jian Yu,1,2,3,4 Ding Ma,1,2,4 Ying-Ying Liu,1,2,3 Yi Xiao,1,2 Yue Gong,1,2 Yi-Zhou Jiang,1,2 Zhi-Ming Shao,1,2
Xin Hu,1,2 and Gen-Hong Di1,2
1DepartmentofBreastSurgery,FudanUniversityShanghaiCancerCenter,Shanghai200032,China;2KeyLaboratoryofBreastCancerinShanghai,FudanUniversity
ShanghaiCancerCenter,FudanUniversity,Shanghai200032,China;3DepartmentofOncology,ShanghaiMedicalCollege,FudanUniversity,Shanghai200032,China
Anemergingviewregardingcancermetabolismisthatitishet- uncontrolledcellulargrowth.Moreover,reprogrammingthemicro-
erogeneousandcontext-specific,butitremainstobeelucidated environmenttosatisfytheenergydemandsoftumorcellsisanother
in breast cancers. In this study, we characterized the energy- outstanding feature.4,5 Metabolic transformation enables the initia-
relatedmetabolicfeaturesofbreastcancersthroughintegrative tionandprogressionofcancercells.6Thedifferencesinthedepen-
analyses of multiple datasets with genomics, transcriptomics, denceonandutilizationofthemajorenergysources,suchasglucose,
metabolomics, and single-cell transcriptome profiling. En- fattyacids,andglutamine,arelinkedtoaseriesoffactors,suchasge-
ergy-related metabolic signatures were used to stratify breast neticalterationsandtheacquisitionofnutrientsandoxygen.7Recent
tumors into two prognostic clusters: cluster 1 exhibits high studieshighlightingtheplasticityandflexibilityofcancermetabolism
glycolytic activity and decreased survival rate, and the signa- betweenandwithintumorshaverevealedatherapeuticallyactionable
turesofcluster2areenrichedinfattyacidoxidationandglu- vulnerability.8,9
taminolysis. The intertumoral metabolic heterogeneity was
reflectedbytheclusteringamongthreeindependentlargeco- The intrinsic and extrinsic features of tumor cells can be precisely
horts,andthecomplexitywasfurtherverifiedatthemetabolite capturedusingsingle-cellRNAsequencing(scRNA-seq)technology.
level.Inaddition,wefoundthatthemetabolicstatusofmalig- scRNA-seqenablesthediscoveryofdifferentcellsubsets,thedepic-
nant cellsratherthanthat ofnonmalignant cellsisthemajor tion of clonal diversity, and, importantly, the identification of the
contributor at the single-cell resolution, and its interactions critical factor of tumor heterogeneity. The identification of cancer
with factors derived from the tumor microenvironment are metabolic subtypes has the potential to improve patient outcomes
unanticipated.Notably,amongvariousimmunecellsandtheir andindicatetreatmentresponse.10,11Previousstudieshavestratified
clusters with distinguishable metabolic features, those with several tumor types into distinct metabolic subgroups, including
immunosuppressive function presented higher metabolic ac- ovarian cancers, hepatic carcinomas, and pancreatic cancers.11–14
tivities.Collectively,weuncoveredtheheterogeneityinenergy However,thederegulationofcellularenergeticmechanismsinbreast
metabolismusingaclassifierwithprognosticandtherapeutic cancersisunknown,andadetailedmetabolicclassifierforbreastcan-
value.Single-celltranscriptomeprofilingprovidednovelmeta- certissuesislacking.
bolicinsightsthatcouldultimatelytailortherapeuticstrategies
basedonpatient-orcelltype-specificcancermetabolism. Herein,wedefinedadistinctenergymetabolicclassifierandidentified
promisingsubtype-selectivemetabolicvulnerabilities.Inadditionto
providing a single-cell sequencing dataset, we further revealed rea-
INTRODUCTION sons underlying the metabolic heterogeneity in breast cancer. We
alsoidentifiedmetabolicfeaturesbetweenmalignantandnonmalig-
Overtheprecedingdecades,researcheffortshaveledtoremarkable
nant cells and among immune cell subtypes. These findings begin
progress in our understanding of the molecular heterogeneity of
breastcancer.1,2Clinically,thisheterogeneousdiseasehasbeenclas-
sifiedintofourgroupsbasedonthehormonereceptor(HR)andhu-
Received2November2020;accepted2March2021;
man epithelial growth factor receptor-2 (HER2) status: luminal A https://doi.org/10.1016/j.ymthe.2021.03.003.
(HR+/HER2 (cid:1) ), luminal B (HR+/HER2+), HER2-positive (HR (cid:1) / 4Theseauthorscontributedequally
HER2+),andtriple-negativebreastcancer(HR (cid:1) /HER2 (cid:1) [TNBC]). Correspondence:Gen-HongDi,DepartmentofBreastSurgery,FudanUniversity
ShanghaiCancerCenter,Floor8,No.270Dong’anRoad,Shanghai200032,China.
Metabolicreprogramminghasbeenconsidered1ofthe10hallmarks E-mail:genhongdi@163.com
Correspondence: Xin Hu, Department of Breast Surgery, Fudan University
ofcancerfornearlyadecade.3Tumorsshareacommonphenotypeof
ShanghaiCancerCenter,Floor8,No.270Dong’anRoad,Shanghai200032,China.
efficiently generating the energy and macromolecules required for E-mail:xinhu@fudan.edu.cn
MolecularTherapy Vol.29No7 July2021ª2021TheAmericanSocietyofGeneandCellTherapy. 1
100
80
60
40
20
0
0 60 120 180 240 300 360
Time in months
SO
100 Cluster 1
80 Cluster 2
60
40
20 P < 0.001
0
0 60 120 180 240 300 360
Time in months
SSCB
100 Cluster 1
Cluster 2 90
80
70
P < 0.001
60
0 12 24 36 48 60 72 84
Time in months
SO
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
MolecularTherapy
A
B C
D
E F
Cluster 1
P < 0.001 P < 0.001 PP << 00..000011 Cluster 2
G H
(legendonnextpage)
2 MolecularTherapy Vol.29No7 July2021
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
www.moleculartherapy.org
tounravelthemetabolicheterogeneityinbreastcancersatboththe confirmedthemetabolicheterogeneityofbreastcanceranditsprog-
bulkandsingle-celllevels. nosticsignificance.
RESULTS Furthervalidationusinganenergymetabolicclassifier
Breastcancerhastwotypesofmetabolicstatusesaccordingto Wethensoughttovalidatetherobustnessoftheclassifier.Thedistri-
theenergymetabolicclassifier butionofcluster1-and2-relatedgeneexpressionbetweensubgroups
Aflowchartwasdevelopedtosystematicallydescribeourstudy(Fig- wasexamined.Ourenergymetabolism-basedclassificationreflected
ure S1). To identify differences in the energy metabolism of breast theexpressionlevelsofglycolysis-andPPP-associatedgenes,which
cancers,wedeterminedfourcentralmetabolicpathways:glycolysis, were enriched in cluster 1 (Figure 2A, top). Several genes involved
the pentose phosphate pathway (PPP), fatty acid oxidation (FAO), inFAOandglutaminolysisshowedsignificantlyhighermRNAlevels
and glutaminolysis (Materials and methods; Figure 1A; Table S2). incluster2(Figure2A,bottom).Inaddition,comparablepatientsub-
We then calculated the single-sample gene set enrichment analysis groupswereidentifiedinTheCancerGenomeAtlas(TCGA)-breast
(ssGSEA)scorestoestimatetheabundanceoffourmetabolicpathway invasive carcinoma (BRCA) cohort using the same bioinformatics
activities in each sample from the Molecular Taxonomy of Breast method (Figure 2B; Figure S5). Approximately 40% of the patients
CancerInternationalConsortium(METABRIC)database.Allbreast wereallocatedtocluster1.Asimilarrelationshipwasalsoobserved
cancermetabolicphenotypeswereclassifiedintotwoheterogeneous between our classifier and molecular subtype (Figure 2C). Finally,
clusters(Figure1B).Ouranalysisrevealedthattwowastheoptimal we analyzed the association of the metabolite distribution between
and robust clustering number (Figure 1C; Figure S2A), indicating the two clusters using previously published metabolomics data,
twoenergymetabolicpatternsasfollows:(1)dependentonglycolysis including data from 23 patients in TCGA-BRCA cohort.15 As ex-
and PPP and (2) FAO and glutaminolysis enrichment (Figure 1B). pected,therawmaterialofglycolysis,glucose,wasgreatlyconsumed
Importantly, analysis from the Sweden Cancerome Analysis inthesamplesbelongingtocluster1(Figure2D).Thedownstream
Network-Breast (SCAN-B) cohort externally validated the repeat- metabolites ofthe glycolytic pathway, lactate and alanine,were en-
ability of our clustering results (Figure 1D; Figure S2B). A prin- richedincluster1,andasimilaraccumulationofribosewasfound
cipal-component analysis (PCA) further supported the substantial in the PPP (Figure 2D). Nevertheless, tumors dependent on FAO
intertumoral metabolic heterogeneity (Figure S3),and classification andglutaminolysiswereinclinedtoconsumeglutamineandfreefatty
intotwoclusterswasfoundtobethemostrobustclassification. acids (Figure 2E). Specifically, long-chain fatty acids (e.g., palmito-
leate),glutamine,andglutamatewereactivelycatabolizedintheclus-
Kaplan-Meieranalysisshowedthatthecasesincluster1wereassoci- ter2tumors.Altogether,ourenergymetabolicclassifierwasrobust
ated with poorer breast-cancer-specific survival (BCSS) and overall andestablishedtwosubgroups.
survival(OS)(Figure1E).SimilarresultswereobtainedforOSwith
theSCAN-Bcohort(Figure1F).ThemultivariateCoxproportional Metabolicclassifier-specificclinical,genomic,and
hazards model also revealed that cluster 1 independently predicted transcriptomiccharacteristicsofbreastcancers
poorersurvivalinbreastcancers(hazardratio[HR],1.67forBCSS To reveal relevant clinical features, we analyzed the distribution of
in METABRIC; HR, 1.4 for OS in SCAN-B; Figure S4). Previous clinical characteristics between the clusters in the SCAN-B cohort
studieshaveidentifiedbreastcancergeneexpressionsignaturesasso- duetoitsclinicaldataintegrity(FigureS6).Histologicgrade3(G3)
ciated with survival and treatment targets.2 To determine whether (p < 0.001), absence of estrogen receptor (ER) expression (p <
expressionpatternsaccordingtotheenergymetabolicclassifiercould 0.001), high Ki-67 index (p < 0.001), large tumor size (p < 0.001),
underliethedifferencesbetweenpreviouslyestablishedsubtypes,we andincreasednumberofinvolvedlymphnodes(p<0.001)wereasso-
investigated the various breast cancer molecular subtypes for each ciatedwithcluster1.Elderlypatients(p<0.001)andnon-basal-like
sampleinourstudycohorts.ForMETABRICandSCAN-Bcohorts, subtypes(p<0.001)wereenrichedincluster2.
wefoundthatthecluster1subgroupcontainedahigherfrequencyof
HER2-enriched and basal-like tumors, whereas cluster 2 predomi- WethenusedbreastcancercelllinesfromtheCancerCellLineEncy-
nantly included the luminal A subtype. Approximately equal clopedia (CCLE) to estimate the power of the energy metabolic
frequenciesoftheluminalBandnormalsubtypeswereobservedbe- classifier.Ourmetabolicstratificationofthecelllinesorderedbymo-
tweenclusters,whichsuggestedapotentialconnectionbetweenthe lecularsubtypeisshowninFigureS7A.Thesetwoclustersprovideda
two types of classification (Figures 1G and 1H). These results useful and interpretable basis for further metabolic analysis. More
Figure1.Breastcancersexhibitmetabolicheterogeneity
(A)Schematicdiagramoftheenergymetabolicpathways.(B)k-meansclusteringofbreastcancerenergymetabolismbasedonfourmetabolicpathwayscalculatedthrough
assGSEAoftheMETABRICcohort.(C)Heatmapdisplayingconsensusclusteringwiththerobustclassification(k=2).(D)k-meansclusteringofbreastcancerenergy
metabolismbasedonfourmetabolicpathwayscalculatedthroughassGSEAoftheSCAN-Bcohort.(E)Kaplan-MeiercurvesofBCSSandOSbetweenclustersinthe
METABRICcohort.Log-ranktestpvaluesareshown.(F)Kaplan-MeiercurvesofOSbetweenclustersintheSCAN-Bcohort.Thelog-ranktestpvalueisshown.(G)Overlay
ofourenergymetabolicclassifierwithpreviousPAM50subclassesintheMETABRICcohort.(H)OverlayofourenergymetabolicclassifierwithpreviousPAM50subclassesin
theSCAN-Bdataset.TCA,tricarboxylicacid;PPP,pentosephosphatepathway;FAO,fattyacidoxidation.
MolecularTherapy Vol.29No7 July2021 3
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
MolecularTherapy
A
B C
D E
(legendonnextpage)
4 MolecularTherapy Vol.29No7 July2021
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
www.moleculartherapy.org
lactate production was observed in the cells belonging to cluster 1 Moreover, the knockdown of S100A8 impaired the growth rate of
thaninthosebelongingtocluster2(FigureS7B).Overall,theseresults MDA-MB-468andAU-565cells(Figures3J;FigureS10C).
represented subgroups with special clinicopathological features and
provide a basis for defining molecular subtypes for the assessment To explore the relationship between tumor immunity and
ofbreastcancerheterogeneity. metabolism,wecalculated theabundance of10immune-and stro-
mal-relatedcelltypesusingthemicroenvironmentcellpopulations-
Molecular events such asmutations oramplifications inoncogenes counter (MCP-counter) algorithm.22 A significant difference was
canstimulatecell-autonomousmetabolicreprogramming.8,16Onco- observedbetweenthetwoclustersinmostcelltypes,withtheexcep-
gene-driven liabilities encourage exploration of the genomic alter- tion of neutrophils and endothelial cells (Figure S11A). The higher
ationsthatcouldbecorrelatedwiththeglycolyticphenotypeofcluster enrichmentforimmunecellsincluster1wasquantifiedinboxplots
1inTCGA-BRCAcohort.Wenotedthatseveralglycolyticgeneswere (Figure S11B). Moreover, diverse immune signatures, including tu-
specificallyamplifiedincluster1(Figure3A).Thehighexpressionof mor-infiltrating lymphocytes (TILs), immune cytolytic activity
theseglycolyticgenescouldbeexplainedbycopynumbervariations (CYT),andtheinterferon(IFN)response,wereincreasedintheclus-
(FiguresS8AandS8B).Fiveofsixselectedgenesalsoshowedahighly ter1subgroup(FigureS11C).Similarly,aseriesofpotentiallytarget-
positive correlation with the corresponding protein levels (Fig- ableimmunecheckpointgenesthatweredesignedforinhibitorswere
ureS8C).However,wedidnotnoticethesetypesofchangesingenes allupregulatedintheclusterinclinedtotheglycolyticphenotype(Fig-
in cluster 2 that are involved in FAO or glutaminolysis (data not ure S11D). Although it was reported that tumor cells prefer to in-
shown). We then referred to signatures to evaluate the enrichment creaseglycolyticflux,wefoundthatsampleslocatedincluster1did
score of 10 classical oncogenic pathways (Figure 3B). Consistent notshowthehigherproportionoftumorcellsbutwerecharacterized
with the findings of published studies related to the glycolytic ten- byimmuneinfiltration(FigureS11E).Thesedatahighlightourdata-
dency of cancer, oncogenic pathways such as phosphatidylinositol setasaresourcefortheidentificationofpotentialdriversofmetabolic
3-kinase(PI3K),MYC,andHippo-relatedsignalinghadhigherscores features and their relationship with immune infiltration in patients
incluster1(Figure3C).Additionalvalidationwasperformedwiththe withbreastcancer.
METABRIC cohort to illustrate the repeatability of the classifier
(FigureS9A).Wealsocomparedtwofactorsdeterminingtumorpro- Malignantcellspredominantlyleadtometabolicheterogeneity
liferationandmetastasis.Bothfactorsweresignificantlyenrichedin We then sought to determine whether the metabolic difference be-
cluster1(Figure3D;FigureS9B). tween the two clusters can be distinguished at the single-cell level.
The single-cell resolution level assists in understanding the precise
Todeterminewhethercluster1tumorspossessuniquetranscriptome nature of subclonal diversity and the tumor microenvironment. In
programs that might facilitate their glycolytic phenotype, we con- contrasttobreastcancercellsculturedinvitro,tumorcellscollected
structedvolcanoplotstocomparethegeneexpressioninthesamples frompatientswereaffectedatthesingle-celllevelbythenumberof
belongingtoclusters1and2(Figure3E).Theintersectionsofthetop nonmalignantcells(Figure4A).Wefirstinvestigatedwhethermalig-
upregulated genesin the two databases revealed S100A8 as the top nantcellsarecapableoffacilitatingmetabolicheterogeneity,andwe
candidate(Figure3F).S100A8isanEF-handcalcium-bindingpro- testedourhypothesisusingscRNA-seq.TheGEO:GSE75688data-
tein belonging to the S100 family. Although S100A8 is reportedly base23included11primarybreastcancertumorsandtwometastatic
associated with the tumor microenvironment,17,18 the downregula- lymph node samples representing four molecular subtypes. All of
tion of intratumoral S100A8 also impairs tumor
progression.19–21
thesesamplesweresubjectedtobulkRNA-seqandscRNA-seq.We
However, the relationship between S100A8 and glycolysis remains first classified 10 primary breast tumors (one case was excluded
unknown.OursurvivalanalysisshowedthatS100A8wassignificantly because no malignant cells were detected by scRNA-seq) at the
predictiveofincreasedrelapse(p=2.6(cid:3)10 (cid:1)11;HR,1.45)inbreast bulk RNA-seq level using the established metabolic classifier (Fig-
cancerpatients(Figure3G).TheknockdownofS100A8resultedin ure 4B). We also analogouslystratified these 10samples bymixing
decreasedlactatelevelscomparedwiththoseinthecontrolcells(Fig- allmalignantcellsfromeachpatienttogether(Figure4C).Interest-
ures3H;FigureS10A).S100A8silencingdownregulatedtheprotein ingly,allofthepatients werestablyallocatedintotwoclusters.We
expression of hexokinase 2 (HK2) and slightly reduced the level thenevaluatedtheclusterscoreofeachtumoratthebulkRNA-seq
of lactate dehydrogenase A (LDHA) (Figures 3I; Figure S10B). level. The customized cluster score accurately reflected the energy
Figure2.Validationofthemetabolicclassifierbasedonmetabolicgeneandmetabolitelevels
(A)QuantificationofselectedgenesoftheglycolyticpathwayandPPP(log intensitylevels,top)andselectedgenesbelongingtotheFAOpathwayandglutaminolysis(log
2 2
intensitylevels,bottom)intheMETABRICcohort.Eachboxplotshowsthemedianandinterquartilerange(IQR,25th–75thpercentiles);whiskersindicatethehighestand
lowestvalueswithin1.5timestheIQR,andtheoutliersarelabeledasdots.SignificancewasdeterminedusingaWilcoxonrank-sumtests.(B)k-meansclusteringofbreast
cancerenergymetabolismbasedonfourmetabolicpathwayscalculatedthroughassGSEAofTCGA-BRCAdataset.(C)Distributionofbreastcancermolecularsubtypes
amongtheclusters.(DandE)Levelsofrepresentativemetabolitesinvolvedinglycolysis/PPP(D)andFAO/glutaminolysis(E)fromTang’smetabolomicsdatasetof23
patients.EachboxplotshowsthemedianandIQR;thewhiskersindicatethehighestandlowestvalueswithin1.5timestheIQR,andtheoutliersarelabeledasdots.The
significancewasdeterminedusingtheWilcoxonrank-sumtest.*p<0.05,**p<0.01,***p<0.001.ns,notsignificant.
MolecularTherapy Vol.29No7 July2021 5
1.2
1.0
0.8
0.6
0.4
0.2
0.0
level
etatcal
evitaleR
shCTRL shS100A8-1
shS100A8-2 6
4
2
0
1 2 3 4 5 6
Days
etar
htworg
evitaleR
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
MolecularTherapy
A
B
C D
E F
G H I J
MDA-MB-468
shCTRL
shS100A8-1 shS100A8-2
(legendonnextpage)
6 MolecularTherapy Vol.29No7 July2021
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
www.moleculartherapy.org
metabolicpathwayactivities(Figure4D).Basedontheclusterscore, celllines)(Figure4H,left).Unexpectedly,althoughsignificantposi-
we assigned cluster scores of 1 or 2 to each malignant cell. For tive correlations were found for FAO and OXPHOS with hypoxia
example, if the cluster 1 score was higher than the cluster 2 score, andangiogenesisinmalignantcells(forFAOandhypoxia,Pearson’s
themetabolictendencyofthecorrespondingtumorbelongstocluster R=0.40;forFAOandangiogenesis,Pearson’sR=0.27;forOXPHOS
1.AsshowninFigure4E,mostmalignantcellshavethesamepattern and hypoxia, Pearson’s R = 0.52; for OXPHOS and angiogenesis,
ofmetabolismasthatdetectedatthebulktumorlevel.Notably,only Pearson’s R = 0.22), breast cancer cell lines showed a markedly
approximately 30%–40% of malignant cells from two patients different trend (for FAO and hypoxia, Pearson’s R = (cid:1)0.18; for
(BCR07 and BCR10, TNBC) showed the same metabolic tendency FAOandangiogenesis,Pearson’sR=(cid:1)0.07;forOXPHOSandhyp-
asthemetabolicclassifier.Wespeculatedthatforcertaintumors,a oxia,Pearson’sR=(cid:1)0.34;forOXPHOSandangiogenesis,Pearson’s
smallfractionofmalignantcellscouldreflectthemetabolicactivity R=(cid:1)0.41).Weconsideredtheexistenceofapotentialconnectionbe-
asawhole.Anotherreasonforthisphenomenoncouldbethesub- tween mitochondrial activity and the microenvironment. In sum-
stantial heterogeneity ofTNBC. Importantly, we observed a cluster mary,malignantcellsplayaleadingroleintumormetabolism,and
transformationduringregionallymphnodemetastasis,whichindi- factorsofthemicroenvironmentalsoplayarole.
catesthatthemetabolicphenotypeevolvesastumorsprogressfrom
localtometastaticcancer(Figure4F). Metabolicfeaturesofmalignantandnonmalignantcellsinthe
tumormicroenvironment
Inaddition,weexploredthemetabolicpathwayactivitiesbetweenthe Tobetterunderstandthemetaboliclandscapeofthetumormicroen-
twoclustersinGEO:GSE75688.Afterevaluationoffourmethodsfor vironment,wecomparedthemetabolicpathwayactivityamongfive
normalization,deconvolutionwasused(FigureS12A).Wefoundthat cell types. Malignant cells showed the highest metabolic pathway
thecluster1sampleshadahigherlevelofmetabolicactivity,regard- activity(Figure5A),andthisactivitywascharacterizedbytheupre-
lessofthenumberofgenesdetected(FiguresS12BandS12C).After gulationofmostmetabolicpathways(Figure5B).Toexploretherela-
imputation, which is a method for reducing the dropout rates of tionshipbetweenthemetabolicclassifierandnonmalignantcells,we
genes, the same result was reached (Figures S12D and S12E). This comparedtheclusterscoresbetweenthetwoclustersamongmalig-
resultsuggestedthattheglycolytictendencysignifiedahighertumor nant cells. As expected, the malignant cells in any of the clusters
metabolicactivity. were significantly enriched in the corresponding cluster score (Fig-
ure5C,top).Incontrast,nocorrelationwasfoundbetweenthecluster
Althoughmalignantcellsdominatetheenergymetabolicpatternof anditsrelatedscoreinnonmalignantcells(Figure5C,bottom).Thus,
tumors,weaimedtoidentifytheroleofthetumormicroenvironment we concluded that malignant cells exhibited the closest correlation
and determine whether it influences the metabolism of malignant withthemetabolicphenotype.
cells.However,environmentalfactorscannotbedirectlyincorporated
into a metabolic analysis. Thus, we used two factors, hypoxia and Strikingly,wealsounraveledabriefviewofimmunecellmetabolism
angiogenesis,forfurtherstudy.Weusedtheaverageexpressionlevels inbreastcancers.Theclassificationofvariouscelltypesinthetumor
ofgenesetsrelatedtohypoxiaandangiogenesisassubstitutionsfor microenvironmentisschematicallydescribedinFigure5D.Alarge-
theoxygenandnutrientsupply.Wefirstexaminedthecorrelationbe- scaleanalysisofintratumoralimmunecellswaspreviouslyperformed
tweenFAOandtheoxidativephosphorylation(OXPHOS)pathway using scRNA-seq.24 We were able to recognize most expected im-
inGEO:GSE75688andfoundapositivecorrelationinbothmalig- munecelltypesfrombreasttumorandnormaltissuesintheGEO:
nant breast cells and breast cancer cell lines, which indicated that GSE114727 dataset, and these cell types included T cells, B cells,
both pathways could imply mitochondrial activity (Figure 4G). myeloid cells, natural killer (NK) cells and mast cells24 (Figure 5E;
Consistent with a previously reported concept, glycolysis exhibited FiguresS13andS14).However,wecouldnotdeterminethemetabolic
asignificantpositivecorrelationwithhypoxiaandangiogenesis(for classificationofeachcaseduetolimiteddata.Toinvestigatethemeta-
hypoxia,Pearson’sR=0.73formalignantcellsand0.69forcelllines; bolic features of nonmalignant cells from breast tumor tissues, a
forangiogenesis,Pearson’sR=0.35formalignantcellsand0.60for Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway
Figure3.Distinctgenomicandtranscriptomicfeaturesofthemetabolicclassifierrevealingpotentialtargets
(A)Comparisonofcopynumbervariations(CNVs)betweenclusters.Apparentpeaksofamplificationsforglycolyticgenesareshownbyarrows.(B)Heatmapdepictingthe
normalizedenrichmentscoresof10oncogenicpathwaysbetweenclusters.(C)Quantificationofoncogenicpathwaysenrichedincluster1.Eachboxplotshowsthemedian
andIQR;thewhiskersindicatethehighestandlowestvalueswithin1.5timestheIQR,andtheoutliersarelabeledasdots.ThesignificancewasdeterminedusingWilcoxon
rank-sumtests.(D)Boxplotsofthecellcycleprogression(CCP)andepithelial-mesenchymaltransition(EMT)scorefortwoclustersinTCGA-BRCAdataset.Eachboxplot
showsthemedianandIQR;thewhiskersindicatethehighestandlowestvalueswithin1.5timestheIQR,andtheoutliersarelabeledasdots.Thesignificancewasdetermined
usingaWilcoxonrank-sumtests.(E)Volcanoplotsshowinggenesthataredifferentiallyexpressedincluster1orcluster2samples.Reddotsindicategenesupregulatedin
cluster1;greendotsindicategenesupregulatedincluster2.(F)VenndiagramshowingS100A8asthecandidate.(G)Kaplan-Meiersurvivalcurveshowingthedecreased
relapse-freesurvivalofpatientswithhighS100A8expression.Thepvaluewasdeterminedusingalog-ranktest.(H)Lactateproductionbytheindicatedcells(n=3).
SignificancewasdeterminedbyaStudent’sttest.**p<0.01.(I)ProteinlevelsoftheaerobicglycolysisenzymesHK2andLDHAfollowingtheknockdownofS100A8.(J)CCK-
8assaysofMDA-MB-468cellsexpressingcontrolorS100A8shRNAs.ThesignificancelevelwasdeterminedusingaStudent’sttest.**p<0.01,***p<0.001.
MolecularTherapy Vol.29No7 July2021 7
7.5
7.0
6.5
6.0
4.0 4.5 5.0 5.5
FAO
SOHPXO
5.0
4.5
4.0
3.5
3.0 3.5 4.0 4.5 5.0
Hypoxia
sisylocylG
5.5
5.0
4.5
4.0
3.0 3.5 4.0 4.5 5.0
Hypoxia
OAF
7.5
7.0
6.5
6.0
3.0 3.5 4.0 4.5 5.0
Hypoxia
SOHPXO
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
MolecularTherapy
A B
C D
E
F H
G
(legendonnextpage)
8 MolecularTherapy Vol.29No7 July2021
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
www.moleculartherapy.org
analysis showed that CD8+ T cells, compared to CD4+ T cells, are marker genes of M2-like tumor-associated macrophages (TAMs)
foundtohavehigherOXPHOSactivity(Figure5F).Comparisonof and exhibited significantly higher levels of metabolism compared
the metabolism between lymphocytes and myeloid cells showed a with M-C3-S100A9, a conventional-type macrophage (Figure 6F).
moremetabolicallyactivestatusamongmyeloidcells(FigureS15A). TheupregulationofthesepathwaysinM-C4-TREM2mightsupport
The comparison between T cells and B cells revealed that T cells thefunctionandadaptationofM2-likeTAMsinthetumormicroen-
exhibit ahigher energymetabolicstatus (FigureS15B). Incontrast, vironment. Consistent with previous studies, immunosuppressive
arginineandprolinemetabolismwastheonlymetabolicpathwayen- immunecellswereprimarilylocatedintumortissues(FigureS16D).
richedinBcells(p<0.05).Overall,malignantcellsexhibitedthehigh- Takentogether,theseresultsindicatefeasiblemeasuresfortargeting
est metabolic activity and dominated thecluster score, whereas the theenergymetabolicpathwaytoeliminateimmunosuppressiveim-
metabolicphenotypeofnonmalignantcellsappearedtobedependent munecells.
ontheirtypesandclusters.
DISCUSSION
Metaboliccharacteristicsofimmunecellclusters The causes of metabolic heterogeneity are multifaceted. The emer-
Toinvestigatethepossibilityofapplyingametabolism-basedtreat- genceofhigh-contentdatasets andnewsequencing techniquesand
mentstrategytononmalignantcellsinthetumormicroenvironment, toolsfortheanalysisofthesedatasets,togetherwithmetabolicpheno-
we further distinguished nonmalignant cells (CD8+ T cells, CD4+ type experiments, make it possible to explore the metabolic
Tcells,andmyeloidcells)frombothbreasttumorsandnormaltis- complexityofcancer.Toourknowledge,thisstudyisthefirsttoestab-
sues.AmongtheCD45+cellsdetected,CD8+Tcellswerethemost lishanovelmetabolicclassifierforseveralbreastcancercohortsbased
prevalentimmunecelltype.Thesecellswereclassifiedintothreesub- onthreeenergysources:glucose,glutamine,andfattyacids.Cluster1
groups.AsshowninFigures6AandS16A,cellsfromC1werenaive is characterized by an increasing dependence on glycolysis and the
CD8+Tcells,whereasCD8-C3-PDCD1(exhaustedCD8+Tcells)and PPP.Incontrast,cluster2tumorsprefertoutilizeFAOandglutami-
CD8-C2-CX3CR1 (cytotoxic CD8+ T cells) cells were located in nolysis for survival. An assessment of the variations between these
differentcellclusters.Interestingly,increasesinthemetabolicactivity clustersrevealedspecificchangesingenomics,transcriptomics,and
ofglycolysisandOXPHOSweredetectedfromCD8-C1toCD8-C3 metabolomics,whichsuggestedthatmetabolicheterogeneityshould
(Figure 6B). These phenomena highlighted that functionally ex- beconsideredwhendevelopingpersonalizedtherapies.Importantly,
haustedTcellsarenotmetabolicallyexhausted.Todiscussthehetero- throughtheuseofsingle-celltranscriptomics,weconfirmedthatma-
geneityamongCD4+Tcells,CD4+Tcellswereclusteredintothree lignantcellsprofoundlycontributetothemetabolicheterogeneityof
subgroups: CD4-C1-IL7R, CD4-C2-GZMA, and CD4-C3-FOXP3 breastcancerandthatthemicroenvironmentalsoplaysaroleinmeta-
(Figure 6C). CD4-C2-GZMA constitutes the key CD4+ subtype bolicplasticity.Wealsofoundthatthemetabolicdifferencebetween
responsible for antigen presentation, which is known as T helper. immuneandstromalcellsubtypescanbedetectedatthesingle-cell
CD4-C3-FOXP3expressedmarkersassociatedwithimmunosuppres- level, and the results suggested that immunosuppressive cells (e.g.,
sive reactions, such as FOXP3, CD25, and CTLA4 (Figure S16B). dysfunctionalCD8+Tcells)weremetabolicallyactive.Theseresults
CD4+TcellsfromCD4-C3-FOXP3weremoremetabolicallyactive will aid the understanding of the metabolic heterogeneity in breast
thanCD4-C1-IL7RandCD4-C2-GZMA(Figure6D). cancersandwillprovidenovelcomprehensionfortargetedtherapy.
Wethendetected5,304myeloidcellsthatcouldbedividedintofour It has become increasingly clear that cancer cells exhibit heteroge-
clusters(Figure6E;FigureS16C).Oftheseclusters,M-C1-CD1Cand neousmetabolicpreferencesanddependencies.4Understandingthe
M-C2-LILRA4 consist of dendritic cells, whereas macrophages emergence and evolution of metabolic variability and flexibility is
comprise M-C3-S100A9 and M-C4-TREM2. We then analyzed the importantbecauseitinfluenceshowwethinkaboutexploitingmeta-
myeloidcellmetabolisminthreemetabolicpathways.M-C2-LILRA4, bolicreprogrammingforthetreatmentofcancer.Similartogenomic
whichisassociatedwithhighexpressionofLILRA4andGZMB,indi- or immune alterations, the metabolic adaptations of cancer are
cated a distinct population of plasmacytoid dendritic cells (pDCs). foundedontheinfluenceofaseriesoffactors(intrinsicandextrinsic)
ComparedwiththeM-C1-CD1Csubgroup,M-C2-LILRA4exhibited andtheiraccompanyingimpactsonthetumor.Previously,Daemen
upregulation of the glycolysis, FAO, and OXPHOS pathways (Fig- etal.13conductedbroadmetaboliteprofilingandidentifiedthreesub-
ure 6F). M-C4-TREM2 preferentially expressed a series of classic types based on 38 pancreatic cancer cell lines. Additionally, the
Figure4.Malignantcellsarethemajorcontributortobreastcancerenergymetabolicheterogeneity
(A)Discrepancyofgeneexpressionintumorsunderthreedifferentcircumstances.(B)Classificationof10breasttumorsamplesbasedonbulkRNA-seqresultsfromGEO:
GSE75688usingourenergymetabolicclassifiers.(C)Classificationof10breasttumorsamplesbasedonamixtureofrespectivemalignantcellsfromGEO:GSE75688using
ourenergymetabolicclassifiers.(D)Therobustnessofthescoresofclusters1and2indefiningourmetabolicclassifier.Theclusterscoreisdefinedastheaverageleveloftwo
relevantmetabolicpathwayssubtractedbytheaverageleveloffourmetabolicpathwaysafternormalization.(E)Comparisonofsinglemalignantcellswithbulktumorswith
respecttothemetabolicpattern.(F)Evaluationofclusterscoresbetweenprimarytumorsandpairedmetastaticlymphnodes.(G)CorrelationsofOXPHOSandFAOin
malignantbreastcellsandcelllines.Eachpointisanindividualsample.R,Pearsoncorrelationcoefficient.(H)Comparisonofthepathwayactivitiesofglycolysis,FAO,and
OXPHOSwiththoseofangiogenesisandhypoxiainmalignantbreastcells(top)andbreastcelllinesfromtheCCLEdatabase(bottom).
MolecularTherapy Vol.29No7 July2021 9
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
MolecularTherapy
A B
C
D
E F
(legendonnextpage)
10 MolecularTherapy Vol.29No7 July2021
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
www.moleculartherapy.org
glycolysis-cholesterolsynthesisaxiswaspreviouslyutilizedtoidentify suchasS100A8,couldbeanactionabletherapeuticstrategytoreverse
foursubgroupsinpancreaticcancers.14Bidkhorietal.12stratifiedhe- theglycolyticphenotype.
patocellular carcinomaintothree distinct tumor subtypesbased on
metabolicnetworks.Combiningproteomicsandmetabolomics,Gen- Aphase3randomizedclinicaltrialshowedthatthePD-L1inhibitor
tricetal.11constructedlow-andhigh-OXPHOSmodelstovalidate atezolizumab combined with nab-paclitaxel prolongs progression-
the variation in metabolism in high-grade serous ovarian cancer freesurvival(PFS)amongmetastaticTNBCpatients.28Inaddition,
(HGSOC). The main differences between our study and other the connection between immune infiltration and metabolism has
recentlypublishedworksarethefollowing.(1)Weperformedaninte- been noted. We found that the cluster 1 subgroup included more
grativeanalysisofmultiomicsdata(genomics,transcriptomics,and TNBCpatientsthandidthecluster2subgroup.Theheatmapdepicted
metabolomics) and used multiple datasets (TCGA-BRCA, META- thatcluster1wasassociatedwithimmunesignaturesandhighexpres-
BRIC,SCAN-B,andCCLE)tovalidateourclassifier.(2)Weproposed sionofimmunecheckpointgenes,whichindicatedthepossibleclin-
focusing on metabolic-related pathways or genes to target unique icalbenefitsofimmunecheckpointinhibitorsforthiscluster.
metabolic dependencies. (3) The metabolic tendency was clarified
byasingle-celllevelanalysis.(4)Themetabolicdifferenceswereun- Inparticular,wedeepenedourstudybyutilizingsingle-celltranscrip-
maskedfornonmalignantcellmetabolism. tomicsdatafromtwodatabases.WefirstprovedthatbothbulkRNA-
seq and scRNA-seq data from malignant cells lead to the same
Warburg25proposedthattumorcellsareinclinedtouseglucosefor classificationasthatobtainedusingourmetabolicclassifier.Although
glycolysis even in the presence of sufficient oxygen. It is gradually thereweresomeexceptions,mostsinglemalignantcellsmaintaineda
becoming accepted that aggravated glycolysis facilitates tumor pro- consistentmetabolicpatternasthatfoundatthebulklevel.Interest-
gression and immune escape. The findings obtained in this study, ingly,weobservedclustertransformationduringlymphnodemetas-
i.e., the breast cancer cases in cluster 1 had worse outcomes and tasis.Furthermore,metabolicreprogrammingallowscancercellsto
higherglycolyticgenelevels,indicatethatglycolysisdoesnotactsyn- notonlymaintainunlimitedproliferationbutalsowithstandmeta-
ergistically with fatty acids and glutamine to accelerate tumor pro- bolic challenges that are associated with variation of oxygen and
gression.Moreover,themetabolomicsanalysisshowedthefollowing nutrient. Although the definition of “tumor microenvironment” is
trend: reductions in upstream metabolites and accumulation of somewhatnotappropriateforcultureofcancercelllines,ourfindings
downstream metabolites. Therefore, different therapeutic strategies alsoshedlightonthemetabolicimpactcausedbysurvivalenviron-
targetingmetabolicvulnerabilitiesarenecessary. mentandcell-cellinteractions.Throughthereplacementofnutrients
and oxygen factors with angiogenesis and hypoxia signatures, the
Genomic and transcriptomic analyses have previously identified differentrelationshipbetweenmitochondrialmetabolicactivityand
severalmolecularentitiesinbreastcancers.1,2,26Basedonthesefind- microenvironmentalfactorssupportedtheproposalthattheconclu-
ings,wehighlightedtheinherentdifferencesinbreastcancermeta- sionfrominvitrometabolicanalysisissomewhatdifferentfroman
bolism.Thegenomicamplificationofmetabolicgenesformsacore invivometabolicanalysis.Wehereproposedseveralpossiblereasons
partofmetabolicreprogramminginvariouscancers.7Weobserved behind this perplexing phenomenon: (1) the understanding of the
that cluster 1 had a higher proportion of genomic amplification fundamentals of in vivo metabolism. Metabolic vulnerabilities
among glycolytic genes, whereas similar amplification patterns be- observedinvivoareabsentfromculturedcellmodelsinsomesitua-
tweenlow-andhigh-OXPHOSmodelswerereportedinHGSOCs.11 tions.Tumorcellsheavilyrelyonatimelysupplyofnutrients,which
Hence,wespeculatedthattheamplificationofglycolyticgenesisage- candifferdependingonthelocationofthecellwithinthemicroenvi-
neticpropertyofcluster1tumors.Recentstudieshavesuggestedthat ronmentofatumor,andthusmodelsystemsrecapitulatingthetumor
theactivationofoncogenicpathwaysmightupregulatesomemeta- microenvironment of tumors, especially in humans, remain neces-
bolicpathways.8,16Indeed,wefoundthatcasesincluster1exhibited sary.(2)lackofknowledgeaboutcell-cellinteractioninducedmeta-
severaloncogenicpathwaysrelatedtoglycolysis,suchasthePI3Kand bolic features as well as mitochondria biological characteristics at
Hippopathways.Thedifferentiallyexpressedgenes(DEGs)analysis thecurrentstate.Dupuyetal.29revealedthathighlymetastaticbreast
suggested that S100A8 could be involved in anaerobic glycolysis cancer cells engage both glycolytic and oxidative metabolism,
andthatitsmRNAlevelisupregulatedinthemostmalignantcells indicatingtherequirementofbothpathwaysforsurvival.Thisphe-
belongingtocluster1(TableS3).Interestingly,S100A8canactasa nomenonisstilltobefurtherextendedbyperformingtargetedme-
transcriptional coactivator.27 Thus, we proposed that the blockage tabolomicsandfluxomics,orevenincorporatingmorerepresentative
of metabolism-associated oncogenic pathways or specific genes, experimentalsubjects.Importantly,developingsingle-cellmetabolite
Figure5.Metaboliccomparisonsbetweencellsubtypesinthetumormicroenvironment
(A)MetabolicpathwayactivitylevelsamongfivecelltypesintheGEO:GSE75688dataset.(B)MetabolicpathwaysextractedfromKEGGamongfivecelltypesintheGEO:
GSE75688dataset.(C)Clusterscoresamongmalignantcells(top)andnonmalignantcells(bottom)betweentwoclustersintheGEO:GSE75688dataset.pvalueswere
determinedusingaWilcoxonrank-sumtest.(D)Schematicofdifferentcelltypesinthetumormicroenvironment.(E)t-distributedstochasticneighborembedding(t-SNE)of
immunecellsfromtwoselectedbreasttumorsamplesasexamplesfromGEO:GSE114727.(F)MetabolicpathwaysenrichedinCD4+Tcells(red)orCD8+Tcells(blue).Light
colors(redandblue)indicatenonsignificantdifferences.AGSEApvalue<0.05wasconsideredtoindicateasignificantlyenrichedpathway.
MolecularTherapy Vol.29No7 July2021 11
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
MolecularTherapy
A C E
B D F
Figure6.Metaboliccomparisonsamongimmunecellclusters
(A)t-SNEplotofCD8+cellsacrosstumorandnormalbreasttissues,whicharecolor-codedbasedontheirassociatedclusters.(B)Violinplotsoftheexpressionofglycolysis
(top),FAO(middle),andoxidativephosphorylation(bottom)signaturesacrossCD8+Tcellsfromthreeclusters.(C)t-SNEplotofCD4+cellsacrosstumorandnormalbreast
tissues,whicharecolor-codedbasedontheirassociatedclusters.(D)Violinplotsoftheexpressionofglycolysis(top),FAO(middle),andoxidativephosphorylation(bottom)
signaturesacrossCD4+Tcellsfromthreeclusters.(E)t-SNEplotofmyeloidcellsacrosstumorandnormalbreasttissues,whicharecolor-codedbasedontheirassociated
clusters.(F)Violinplotsoftheexpressionofglycolysis(top),FAO(middle),andoxidativephosphorylation(bottom)signaturesacrossmyeloidcellsfromthreeclusters.The
significancelevelwasdeterminedusingaWilcoxonrank-sumtest.*p<0.05,**p<0.01,***p<0.001.
profilingorspatialtranscriptometechnologypossessesthepowerto tothemetabolicactivityidentifiedinothercancers.31Importantly,
addresstheabovequestions. nonmalignantcellsdonotexhibitthecorrelationofourdefinedclus-
terscore.Amongimmunecells,myeloidcellsexhibitedthehighest
Given the complexity of the tumor microenvironment and its metabolicactivity.However,contradictingthefindingsofaprevious
complicatedcell-cellinteractions,itwillbeinterestingtostudythe studyfocusingonmelanomaandheadandnecksquamouscellcar-
overviewofnonmalignantcellmetabolism.30Incontrasttomalig- cinoma(HNSCC),31wefoundthatCD8+TcellsbutnotCD4+Tcells
nant cells, nonmalignant cells are less metabolically active, similar have enhanced OXPHOS levels, indicating that subpopulations of
12 MolecularTherapy Vol.29No7 July2021
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
www.moleculartherapy.org
Tcellsinthetumormicroenvironmenthavethemetabolicfeatures SignaturesDatabase(MSigDB),40andthentailoredthemetabolicgene
thatdifferfromhistologicorigin. setsintofourcorepathways:glycolysis,PPP,FAO,andglutaminolysis
(TableS1).Subsequently,weperformedthessGSEA41(GSVAfunc-
TheupregulationofaerobicglycolysisandOXPHOSarebothcritical tioninR)tocalculatetheenrichmentlevelofeachmetabolicpathway
aspects of CD4+ and CD8+ cell activation.30 Consistent with this ineachcasethroughtranscriptomics.
concept, both CD4-C2 and CD8-C2 cells showed higher glycolysis
andOXPHOSsignaturescoresthandidCD4-C1andCD8-C1cells, Weperformedk-means(kmeansfunctioninR)clusteringtodeter-
respectively. Of note, we revealed that the metabolic levels of ex- minetheoptimalclusternumberfortheenergymetabolicclassifier.
haustedCD8+Tcells(CD8-C3-PDCD1),regulatoryTcells(Tregs) To cluster samples based on the constituent patterns of metabolic
(CD4-C3-FOXP3), andM2-likeTAMs(M-C4-TREM2)wereupre- pathways,wescaledeachsamplebeforeclustering.Forheatmapplot-
gulatedcomparedwiththoseoftheirclustercounterparts.Although ting (pheatmap function in R), we utilized the k-means clustering
CD8+Tcellexhaustionoccurredinresponsetocontinuousantigenic resulttoreorderthesamplesandscaledtheoriginalssGSEAresults
stimulation,thesedysfunctionalcellsunexpectedlyexhibitedanupre- beforeplotting.Moreover,consensusclustering(ConsensusCluster-
gulated metabolic pattern. A similar phenomenon has also been PlusfunctioninR)wasperformedtofurtherverifytheoptimalnum-
observed in macrophages (M-C4-TREM2 versus M-C3-S100A9). berofclustersusing1,000iterationsandresamplingof80%.Tobetter
These findings will help us further understand the metabolic land- understandthevariationsbetweenclusters,PCAwasalsoapplied.
scapeofthetumormicroenvironment.
FortheclassificationofcelllinesandsamplesinGEO:GSE75688,we
Inconclusion,weprovideacompletelynewperspectiveforunravel- calculated the abundance of the four above-mentioned metabolic
ingtheenergymetabolicheterogeneityofbreastcancers.Ourrobust pathwaysforeachsampleusingssGSEAandthenusedk-meansclus-
metabolic classifier demonstrated that reprogrammed metabolic teringaftercombiningthepathwayenrichmentresultswithTCGA-
pathwaysarerelevanttoclinicaloutcomesandrevealedthepotential BRCAtranscriptomicdatabecauseallofthedatawereobtainedby
therapeutic significance of targeting unique metabolic dependency. RNA-seq.
The latest generation of single-cell transcriptomics has opened the
door to describe the complexity of breast cancer metabolism. Humanbreastcancercelllines
Emerging technologies, including proteomics- or metabolomics- We used the human epithelial ovarian cancer cell lines MDA-MB-
based single-cell profiling, will further complement the recognition 468, AU565,MCF7,BT549, SKBR3, DU4475,ZR-75-1,and BT474
ofthecharacterizationofthesecellstates. fromtheTypeCultureCollectionoftheChineseAcademyofSciences
(Shanghai,China)andHCC1143,JIMT1,EFM192A,andHCC1599
MATERIALSANDMETHODS from Nanjing Cobioer (China). These cell lines were authenticated
Patientsandsamples byshorttandemrepeatprofiling.Thecellswereculturedfollowingin-
Multiple data repositories, including the METABRIC database,26 structionsfromtheAmericanTypeCultureCollection(ATCC)and
TCGA database, and SCAN-B dataset (GEO: GSE96058),32 were Cobioer. Culture media and supplements (e.g., penicillin) were ob-
searched for available breast cancer genomics,transcriptomics, and tained from BasalMedia (Shanghai, China), and fetal bovine serum
clinical information. scRNA-seq data from GEO: GSE7568823 and (FBS)wasobtainedfromGibco.
GSE11472724wereselectedfortheanalysisofmalignantandnonma-
lignant cells in the tumor microenvironment. Bulk RNA-seq data Measurementoflactate
fromGEO:GSE75688wereextractedforindependentanalysis.The Alactateassaykit(colorimetricmethod)(NanjingJiancheng,China)
above-mentioned datasets were downloaded from various websites wasusedtomeasurelactateproduction.Cellswerecollected,andpro-
(http://www.cbioportal.org/; https://portal.gdc.cancer.gov/; https:// teinwasquantified.Thelactatelevelwasnormalizedtotheprotein
www.ncbi.nlm.nih.gov/geo/). concentration of the sample. Triplicate independent assays were
performed.
Proteindatafrom45breastcancerspecimenswereobtainedfroma
published article.33Themetabolomicprofilereferredto23samples Lentivirusconstructsandcellproliferation
withpairedtranscriptomicsinTCGA-BRCAcohort.15 pLKO.1lentiviralplasmidsencodingshorthairpinRNAs(shRNAs)
targetingtheS100A8geneweredesignedbasedonsequencingper-
RNA-seqdataofbreastcancercelllinesweredownloadedfromthe formedbySigma-Aldrich(shS100A8-1,50-TCAACACTGATGGTG-
CCLE(https://portals.broadinstitute.org/ccle).Thematchedmolecu- CAGTTA-30;shS100A8-2,50-GTGTCCTCAGTATATCAGGAA-30).
larsubtypewassuccessfullyassignedto47of50breastcancercells.34–
Lentiviruses were generated using pLKO.1 plasmids and packaging
36ThesummaryofthesedatasetsisshowninTableS1. plasmids(psPAX2andpMD2.G)throughtransfectioninto293Tcells
cultured to 80% confluence in a 100-mmdish using Lipofectamine
Constructionoftheenergymetabolicclassifier 2000(Invitrogen,USA).Viruseswereharvested48haftertransfection
Toidentifyoptimalenergymetabolicpathwaysfordelineatingbreast andfilteredthrougha0.45-mmfilter.ThebreasttumorcelllineMDA-
cancermetabolism,wesearchedforpapers14,37–39andintheMolecular MB-468 was infected with the viruses in the presence of 6 mg/mL
MolecularTherapy Vol.29No7 July2021 13
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
MolecularTherapy
Polybrene(SantaCruzBiotechnology,USA).Stablytransducedcells Differentialgeneexpressionanalysis
werefilteredviapuromycin(1mg/mL)selectionfor5–7daysstarting Differentialgeneexpressionanalysiswasconductedusingthelimma
48hafterinfection. packageforMETABRICandtheDESeq2packageforTCGA-BRCA
in R software, and protein-coding genes with an absolute log fold
2
TheinvitroproliferationofMDA-MB-468cellswasmeasuredusing change(FC)>1(adjustedpvalue<0.05)weredefinedasDEGs.
CellCountingKit-8(CCK-8)(Dojindo,Japan).Briefly,thecellswere
seeded in 96-well plates (2,000 cells/well) in triplicate. At the indi- scRNA-seqdataprocessing
cated time points, 10 mL of CCK-8 solution was added to cultured TheGEO:GSE75688datasetcontainsannotatedcelltypesfromeach
cells in each well, and the plates were then incubated at 37(cid:4)C for sample. We determined diverse immune cell types in GEO:
90min.Theopticaldensity(OD)valuesweremeasuredat450nm. GSE114727withtheSeuratanalysispackage.47Theimmunemarkers
usedforcelltypingweredescribedpreviously.24,48Specifically,Tcells
Westernblotting (CD4+ and CD8+), B cells, myeloid cells, mast cells, and NK cells
Thecellswereharvestedandlysedusingtissueproteinextractionre- couldberecognizedbyt-distributedstochasticneighborembedding
agent(ThermoFisherScientific,USA)withacocktailofproteinase (t-SNE).CD8+Tcells,CD4+Tcells,andmyeloidcellswereclassified
andphosphataseinhibitors(Bimake.com,USA).Theproteinconcen-
andrecognizedbasedonpreviouslyreportedmarkers.49–53Theraw
trationsweremeasuredusingthebicinchoninicacid(BCA)protein counts were transformed into transcripts per kilobase million
assay kit (Solarbio, China). The protein lysates were separated by (TPM)values forsubsequent analysis. ThescImpute method54was
SDS-PAGEandtransferredtopolyvinylidenefluoride(PVDF)mem- usedforimputingdropoutgeneswhennecessary.
branes(Millipore,USA).Afterblockingwith5%bovineserumalbu-
min(BSA),themembraneswereincubatedwithprimaryantibodies Evaluationofmetabolicactivity
againstS100A8(15792-1-AP,Proteintech),HK-2(22029-1-AP,Pro- Theapplicationoffournormalizationmethodsandthecalculationof
teintech), LDHA (3582T, Cell Signaling Technology), and b-actin metabolicpathwayactivitywereperformedaspreviouslydescribed.31
(8457T,CellSignalingTechnology)andthenspecies-specificsecond- The metabolic profiles were then compared between different cell
aryantibodiesfromJacksonImmunoResearch. types using GSEA. The metabolic pathways with GSEA nominal p
values <0.05 were considered statistically significant. In addition,
Calculationofsignaturescores theOXPHOSsignaturegenesetwasextractedfromtheKEGGdata-
Weusedavalidatedsetof31genesrelatedtocellcycleprogression base. The hypoxia and angiogenesis signature genes were obtained
(CCP)42andthegenesetHALLMARK_EPITHELIAL_MESENCHY- fromthehallmarkgenesetslistedinMSigDB.
MAL_TRANSITIONretrievedfromMSigDBtoestimatetherateof
cellproliferationandmetastaticability.Severalimmunesignatures,43 Survivalanalysis
suchasthoserelatedtoTILs,CYT,andtheIFNresponse,wereuti- Kaplan-MeierplotsofBCSSandOSweregeneratedusingGraphPad
lized to assess the immune filtration level. The ssGSEA score was Prism7software.Alog-ranktestp<0.05wasusedtodefinediffer-
usedtoquantifytheabundancelevelsofthesesignatures.Moreover, ences in survival time. The KM Plotter database55 was utilized to
theimmunescorewascalculatedusingtheESTIMATEalgorithm.44 generatetherelapse-freesurvival(RFS)rates.
MCP-counter,22 a methodology based on transcriptomic data, was
used to evaluate the abundance of eight immune and two stromal SUPPLEMENTALINFORMATION
cellpopulations. SupplementalInformationcanbefoundonlineathttps://doi.org/10.
1016/j.ymthe.2021.03.003.
Theclusterscorewascalculatedastheaverageexpressionleveloftwo
relatedpathwaysbysubtractingthemeanleveloffourpathwaysafter ACKNOWLEDGMENTS
scalingthevaluesofeachmetabolicpathwayforallpatients. ThisresearchwasfundedbytheNationalNaturalScienceFoundation
ofChina(nos.81872137and82072917)andtheMinistryofScience
Theclusterscorewascalculatedastheaverageexpressionleveloftwo andTechnologyofChina(no.2018YFE020160).Wethankallofthe
relatedpathwaysafterscalingthevaluesofeachmetabolicpathway study participants who contributed to this study and all of the re-
forallpatients.Forheatmapdepiction,theclusterscorewasobtained searchers who have uploaded and shared their databases to make
bysubtractingthemeanleveloftwoscoresforeachpatient.Forthe thisworkpossible.
single-cell sequencing data of GEO: GSE75688, the corresponding
malignantcellsareassignedtocluster1ifthecluster1scoreisgreater AUTHORCONTRIBUTIONS
thanthecluster2scoreandviceversa. All authors made substantial contributions to the manuscript.
Conceptionanddesign,T.-J.Y.,Y.-Z.J.,X.H.,andG.-H.D.;develop-
Comparisonofenrichedoncogenicpathways ment of methodology, T.-J.Y., D.M., Y.X., and Y.G.; acquisition of
Tenoncogenicpathways45wereselectedtoevaluatetheenrichment data (e.g., provided animals, acquired and managed patients, pro-
score using ssGSEA.The activated score minus the repressed score vided facilities), T.-J.Y.; analysis and interpretation of data, T.-J.Y.,
representsthefinalscoreofeachpathwayaspreviouslysuggested.46 D.M., Y.-Y.L., Y.-Z.J., and X.H.; writing, review, and/or revision of
14 MolecularTherapy Vol.29No7 July2021
Pleasecitethisarticleinpressas:Yuetal.,Bulkandsingle-celltranscriptomeprofilingrevealthemetabolicheterogeneityinhumanbreastcancers,Mo-
lecularTherapy(2021),https://doi.org/10.1016/j.ymthe.2021.03.003
www.moleculartherapy.org
the manuscript, T.-J.Y., D.M., Y.-Y.L., Y.X., Y.G., Y.-Z.J., Z.-M.S., 17.Wagner, N.B., Weide, B., Gries, M., Reith, M., Tarnanidis, K., Schuermans, V.,
X.H., and G.-H.D.; administrative, technical, or material support Kemper,C.,Kehrel,C.,Funder,A.,Lichtenberger,R.,etal.(2019).Tumormicroenvi-
ronment-derivedS100A8/A9isanovelprognosticbiomarkerforadvancedmelanoma
(i.e., reporting or organizing data, constructing databases), T.-J.Y.,
patients and during immunotherapy with anti-PD-1 antibodies. J. Immunother.
Y.-Z.J., Z.-M.S., X.H., and G.-H.D.; study supervision, Y.-Z.J., Z.- Cancer7,343.
M.S.,X.H.,andG.-H.D. 18. Sinha,P.,Okoro,C.,Foell,D.,Freeze,H.H.,Ostrand-Rosenberg,S.,andSrikrishna,G.
(2008).ProinflammatoryS100proteinsregulatetheaccumulationofmyeloid-derived
DECLARATIONOFINTERESTS
suppressorcells.J.Immunol.181,4666–4675.
Theauthorsdeclarenocompetinginterests. 19. Lim,S.Y.,Yuzhalin,A.E.,Gordon-Weeks,A.N.,andMuschel,R.J.(2016).Tumor-
infiltratingmonocytes/macrophagespromotetumorinvasionandmigrationbyup-
regulatingS100A8andS100A9expressionincancercells.Oncogene35,5735–5745.
REFERENCES
20. Reeb,A.N.,Li,W.,Sewell,W.,Marlow,L.A.,Tun,H.W.,Smallridge,R.C.,Copland,
1.Perou,C.M.,Sørlie,T.,Eisen,M.B.,vandeRijn,M.,Jeffrey,S.S.,Rees,C.A.,Pollack, J.A.,Spradling,K.,Chernock,R.,andLin,R.Y.(2015).S100A8isanoveltherapeutic
J.R.,Ross,D.T.,Johnsen,H.,Akslen,L.A.,etal.(2000).Molecularportraitsofhuman targetforanaplasticthyroidcarcinoma.J.Clin.Endocrinol.Metab.100,E232–E242.
breasttumours.Nature406,747–752.
21. Moon,A.,Yong,H.Y.,Song,J.I.,Cukovic,D.,Salagrama,S.,Kaplan,D.,Putt,D.,Kim,
2.Parker,J.S.,Mullins,M.,Cheang,M.C.,Leung,S.,Voduc,D.,Vickery,T.,Davies,S., H.,Dombkowski,A.,andKim,H.R.(2008).Globalgeneexpressionprofilingunveils
Fauron,C.,He,X.,Hu,Z.,etal.(2009).Supervisedriskpredictorofbreastcancer S100A8/A9ascandidatemarkersinH-ras-mediatedhumanbreastepithelialcellin-
basedonintrinsicsubtypes.J.Clin.Oncol.27,1160–1167. vasion.Mol.CancerRes.6,1544–1553.
3.Hanahan,D.,andWeinberg,R.A.(2011).Hallmarksofcancer:Thenextgeneration. 22. Becht,E.,Giraldo,N.A.,Lacroix,L.,Buttard,B.,Elarouci,N.,Petitprez,F.,Selves,J.,
Cell144,646–674.
Laurent-Puig,P.,Sautès-Fridman,C.,Fridman,W.H.,anddeReyniès,A.(2016).
4.Kim,J.,andDeBerardinis,R.J.(2019).Mechanismsandimplicationsofmetabolic Estimating the population abundance of tissue-infiltrating immune and stromal
heterogeneityincancer.CellMetab.30,434–446. cellpopulationsusinggeneexpression.GenomeBiol.17,218.
5.Pavlova,N.N.,andThompson,C.B.(2016).Theemerginghallmarksofcancermeta- 23. Chung,W.,Eum,H.H.,Lee,H.O.,Lee,K.M.,Lee,H.B.,Kim,K.T.,Ryu,H.S.,Kim,S.,
bolism.CellMetab.23,27–47. Lee,J.E.,Park,Y.H.,etal.(2017).Single-cellRNA-seqenablescomprehensivetumour
andimmunecellprofilinginprimarybreastcancer.Nat.Commun.8,15081.
6.DeBerardinis,R.J.,Lum,J.J.,Hatzivassiliou,G.,andThompson,C.B.(2008).The
biology of cancer: Metabolic reprogramming fuels cell growth and proliferation. 24. Azizi,E.,Carr,A.J.,Plitas,G.,Cornish,A.E.,Konopacki,C.,Prabhakaran,S.,Nainys,
CellMetab.7,11–20. J.,Wu,K.,Kiseliovas,V.,Setty,M.,etal.(2018).Single-cellmapofdiverseimmune
phenotypesinthebreasttumormicroenvironment.Cell174,1293–1308.e36.
7.VanderHeiden,M.G.,andDeBerardinis,R.J.(2017).Understandingtheintersections
betweenmetabolismandcancerbiology.Cell168,657–669. 25. Warburg,O.(1956).Ontheoriginofcancercells.Science123,309–314.
8.Jin,N.,Bi,A.,Lan,X.,Xu,J.,Wang,X.,Liu,Y.,Wang,T.,Tang,S.,Zeng,H.,Chen,Z., 26. Curtis,C.,Shah,S.P.,Chin,S.F.,Turashvili,G.,Rueda,O.M.,Dunning,M.J.,Speed,
etal.(2019).Identificationofmetabolicvulnerabilitiesofreceptortyrosinekinases- D.,Lynch,A.G.,Samarajiwa,S.,Yuan,Y.,etal.;METABRICGroup(2012).The
drivencancer.Nat.Commun.10,2701. genomicandtranscriptomicarchitectureof2,000breasttumoursrevealsnovelsub-
groups.Nature486,346–352.
9.Brown,K.K.,Spinelli,J.B.,Asara,J.M.,andToker,A.(2017).Adaptivereprogram-
mingofdenovopyrimidinesynthesisisametabolicvulnerabilityintriple-negative 27. Song,R.,andStruhl,K.(2021).S100A8/S100A9cytokineactsasatranscriptionalco-
breastcancer.CancerDiscov.7,391–399. activatorduringbreastcellulartransformation.Sci.Adv.7,eabe5357.
10.Peng,X.,Chen,Z.,Farshidfar,F.,Xu,X.,Lorenzi,P.L.,Wang,Y.,Cheng,F.,Tan,L., 28. Schmid,P.,Adams,S.,Rugo,H.S.,Schneeweiss,A.,Barrios,C.H.,Iwata,H.,Diéras,
Mojumdar, K., Du, D., et al.; Cancer Genome Atlas Research Network (2018). V.,Hegg,R.,Im,S.A.,ShawWright,G.,etal.;IMpassion130TrialInvestigators
Molecularcharacterizationandclinicalrelevanceofmetabolicexpressionsubtypes (2018).Atezolizumabandnab-paclitaxelinadvancedtriple-negativebreastcancer.
inhumancancers.CellRep.23,255–269.e4. N.Engl.J.Med.379,2108–2121.
11.Gentric,G.,Kieffer,Y.,Mieulet,V.,Goundiam,O.,Bonneau,C.,Nemati,F.,Hurbain, 29. Dupuy,F.,Tabariès,S.,Andrzejewski,S.,Dong,Z.,Blagih,J.,Annis,M.G.,Omeroglu,
I.,Raposo,G.,Popova,T.,Stern,M.H.,etal.(2019).PML-regulatedmitochondrial A.,Gao,D.,Leung,S.,Amir,E.,etal.(2015).PDK1-dependentmetabolicreprogram-
metabolismenhanceschemosensitivityinhumanovariancancers.CellMetab.29, mingdictatesmetastaticpotentialinbreastcancer.CellMetab.22,577–589.
156–173.e10. 30. Leone,R.D.,andPowell,J.D.(2020).Metabolismofimmunecellsincancer.Nat.Rev.
12.Bidkhori,G.,Benfeitas,R.,Klevstig,M.,Zhang,C.,Nielsen,J.,Uhlen,M.,Boren,J.,
Cancer20,516–531.
andMardinoglu,A.(2018).Metabolicnetwork-basedstratificationofhepatocellular 31. Xiao,Z.,Dai,Z.,andLocasale,J.W.(2019).Metaboliclandscapeofthetumormicro-
carcinomarevealsthreedistincttumorsubtypes.Proc.Natl.Acad.Sci.USA115, environmentatsinglecellresolution.Nat.Commun.10,3763.
E11874–E11883.
32. Brueffer,C.,Vallon-Christersson,J.,Grabau,D.,Ehinger,A.,Häkkinen,J.,Hegardt,
13.Daemen,A.,Peterson,D.,Sahu,N.,McCord,R.,Du,X.,Liu,B.,Kowanetz,K.,Hong, C.,Malina,J.,Chen,Y.,Bendahl,P.O.,Manjer,J.,etal.(2018).ClinicalvalueofRNA
R.,Moffat,J.,Gao,M.,etal.(2015).Metaboliteprofilingstratifiespancreaticductal sequencing-basedclassifiersforpredictionofthefiveconventionalbreastcancerbio-
adenocarcinomasintosubtypeswithdistinctsensitivities tometabolicinhibitors. markers: A report from the population-based multicenter Sweden Cancerome
Proc.Natl.Acad.Sci.USA112,E4410–E4417. AnalysisNetwork-Breastinitiative.JCOPrecis.Oncol.2,1–18.
14.Karasinska,J.M.,Topham,J.T.,Kalloger,S.E.,Jang,G.H.,Denroche,R.E.,Culibrk,L., 33. Johansson,H.J.,Socciarelli,F.,Vacanti,N.M.,Haugen,M.H.,Zhu,Y.,Siavelis,I.,
Williamson,L.M.,Wong,H.L.,Lee,M.K.C.,O’Kane,G.M.,etal.(2020).Alteredgene Fernandez-Woodbridge, A., Aure, M.R., Sennblad, B., Vesterlund, M., et al.;
expressionalongtheglycolysis-cholesterolsynthesisaxisisassociatedwithoutcome ConsortiaOsloBreastCancerResearchConsortium(OSBREAC)(2019).Breastcan-
inpancreaticcancer.Clin.CancerRes.26,135–146. cerquantitativeproteomeandproteogenomiclandscape.Nat.Commun.10,1600.
15.Tang,X.,Lin,C.-C.,Spasojevic,I.,Iversen,E.S.,Chi,J.-T.,andMarks,J.R.(2014).A 34. Neve,R.M.,Chin,K.,Fridlyand,J.,Yeh,J.,Baehner,F.L.,Fevr,T.,Clark,L.,Bayani,
jointanalysisofmetabolomicsandgeneticsofbreastcancer.BreastCancerRes.16, N.,Coppe,J.P.,Tong,F.,etal.(2006).Acollectionofbreastcancercelllinesforthe
415. studyoffunctionallydistinctcancersubtypes.CancerCell10,515–527.
16.Xia,Y.,Ye,B.,Ding,J.,Yu,Y.,Alptekin,A.,Thangaraju,M.,Prasad,P.D.,Ding,Z.C., 35. Riaz,M.,vanJaarsveld,M.T.M.,Hollestelle,A.,Prager-van derSmissen, W.J.C.,
Park,E.J.,Choi,J.H.,etal.(2019).MetabolicreprogrammingbyMYCNconfers Heine,A.A.J., Boersma,A.W.M., Liu,J.,Helmijr, J.,Ozturk,B.,Smid,M.,etal.
dependence on the serine-glycine-one-carbon biosynthetic pathway. Cancer Res. (2013).miRNAexpressionprofilingof51humanbreastcancercelllinesrevealssub-
79,3837–3850. typeanddrivermutation-specificmiRNAs.BreastCancerRes.15,R33.
MolecularTherapy Vol.29No7 July2021 15
