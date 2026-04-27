---
source_path: /mnt/c/Users/Administrator/Zotero/storage/72LFKR35/Zeng 等 - 2024 - OmicVerse a framework for bridging and deepening insights across bulk and single-cell sequencing.pdf
ingested: 2026-04-23
sha256: 077276d0a6e6ecbd
---

Article https://doi.org/10.1038/s41467-024-50194-3
OmicVerse: a framework for bridging and
deepening insights across bulk and single-
cell sequencing
Received:19June2023 ZehuaZeng 1,2,9 ,YuqingMa3,4,9,LeiHu 1,5,9,BowenTan 6,7,PengLiu1,
YixuanWang1,CencanXing 1,2 ,YuanyanXiong 8 &HongwuDu 1,2
Accepted:28June2024
Single-cellsequencingisfrequentlyaffectedby“omission”duetolimitations
Checkforupdates insequencingthroughput,yetbulkRNA-seqmaycontaintheseostensibly
“omitted”cells.Here,weintroducethesinglecelltrajectoryblendingfrom
BulkRNA-seq(BulkTrajBlend)algorithm,acomponentoftheOmicVersesuite
thatleveragesaBeta-VariationalAutoEncoderfordatadeconvolutionand
graphneuralnetworksforthediscoveryofoverlappingcommunities.This
approacheffectivelyinterpolatesandrestoresthecontinuityof“omitted”cells
withinsingle-cellRNAsequencingdatasets.Furthermore,OmicVerseprovides
anextensivetoolkitforbothbulkandsinglecellRNA-seqanalysis,offering
seamlessaccesstodiversemethodologies,streamliningcomputationalpro-
cesses,fosteringexquisitedatavisualization,andfacilitatingtheextractionof
significantbiologicalinsightstoadvancescientificresearch.
Single-cell RNA sequencing (scRNA-seq) and bulk RNA sequencing requiredtoadapttovarioussystems.Moreover,foranalysesinvolving
(RNA-seq)haveemergedasessentialtechniquesforexploringcellular lowdataquantities,researcherscommonlyemploywebserversand
heterogeneity, differentiation, and disease mechanisms1–6. These the R language17, whereas Python is preferred for processing large-
technologies facilitate numerous applications, including converting scaledatasets18.
bulk-seq data into single-seq analyses7, performing differential Integrating single-celland bulk sequencing results can be intri-
expression analysis8, pathway enrichment9, gene co-expression net- cate,producing complex,multi-layered data sets thatchallenge the
work analysis in bulk RNA-seq10, cell annotation11, cell interaction extractionofmeaningfulbiologicalinsights.Arecognizedimpediment
analysis12,cell-trajectoryinference13,evaluatingcell-stateingenesets, insingle-cellsequencingisthe“omission”—theomissionofcertaincell
andpredictingdrugresponseinscRNA-seq14.Manyoftheseapproa- typesduetotechnologicalconstraintsonthesequencingplatformand
ches rely on open-source algorithms contributed by the research interruptionofthetrajectoryofcelldifferentiation,suchastheenzy-
community15,16. matic lysis-related loss of podocytes and intercalated cells19. For
Nevertheless, the growing diversity and abundance of omics example, the differentiation from hematopoietic cells (HPC) to
algorithmsposechallengesinselectingtoolsthatareaccurate,user- podocyteswasinterrupted,andthefiltering-inducedabsenceofneu-
friendly,andappropriateforspecificanalyses.Learningtousevarious trophils,cardiomyocytes,neuronalcells,andmegakaryocytesandthe
algorithms often leads to computational inefficiencies, as users are differentiation from neural intermediate progenitor cells (nIPC) to
1SchoolofChemistryandBiologicalEngineering,UniversityofScienceandTechnologyBeijing,Beijing,China.2DaxingResearchInstitute,Universityof
ScienceandTechnologyBeijing,Beijing,China.3CenterofPrecisionMedicineandHealthcare,Tsinghua-BerkeleyShenzhenInstitute,Shenzhen,Guangdong
Province,China.4InstituteofBiopharmaceuticsandHealthEngineering,TsinghuaShenzhenInternationalGraduateSchool,Shenzhen,GuangdongProvince,
China.5SchoolofLifeSciences,WestlakeUniversity,Hangzhou,Zhejiang,China.6AcademyofMathematicsandSystemsScience,ChineseAcademyof
Sciences,Beijing,China.7SchoolofMathematicsandPhysics,UniversityofScienceandTechnologyBeijing,Beijing,China.8KeyLaboratoryofGene
EngineeringoftheMinistryofEducation,InstituteofHealthyAgingResearch,SchoolofLifeSciences,Sun-Yat-SenUniversity,Guangzhou,
Guangdong,China.9Theseauthorscontributedequally:ZehuaZeng,YuqingMa,LeiHu. e-mail:starlitnightly@gmail.com;cencanxing@ustb.edu.cn;
xyyan@mail.sysu.edu.cn;hongwudu@ustb.edu.cn
NatureCommunications|( 2024)1 5:5983 1
;,:)(0987654321 ;,:)(0987654321
Article https://doi.org/10.1038/s41467-024-50194-3
neuronswasinterrupted20,21.TheBDRhapsody™single-cellplatform clusteringtofilterout“noisy”cells,whichareidentifiedusingcom-
overcomes granulocyte loss by accommodating their natural munitysize.
sedimentation22. Conversely, bulk RNA-seq of whole tissues intrinsi- Another notable limitation of β-VAE lies in the unconstrained
callyincludesthese“omitted”cells.Itshouldbeacknowledgedthat nature of the decoder’s output. This contrasts with the real Bulk
thereisnoexistingalgorithmthatcandirectlysolvethe“omitted”cell environment,wherethecellularratiosarenotstrictlyfixed.Toaddress
problem.However,similartothisproblem,therearesomedeconvo- thisdiscrepancy,asimulatedBulkenvironmentisconstructedthrough
lutionalgorithms,suchasTAPE23,CIBERSORT(CS)24,MuSiC25,CIBER- thesamplingofsingle-celldata,withtheproceduraldetailsoutlinedin
SORTx(CSx)26,andBisque27,whicharenotreallyeffectiveinsolving the “Methods” section. This process is facilitated by a deep neural
the“omitted”cellproblembecausetheylackagenerativecapability. network(DNN)-basedautoencodermodel,wherethesimulatedBulk
ThissuggeststhatGenerativeAdversarialNetworks(GANs)maybethe servesasinput,theencoder’soutputreflectstheproportionsofactual
bestsolutiontothe“omitted”cellproblem. cells,andthesimulatedBulkconstitutesthedecoder’soutput.Mean
To address these challenges, we have developed OmicVerse absolute error (MAE) is used as the evaluation metric for both the
(https://omicverse.readthedocs.io/), a comprehensive Python library encoderanddecoder.Subsequenttomodelconvergence,therealBulk
designedfortranscriptomicresearch.OmicVersestreamlinesaccessto dataisutilizedasinputfortheAEmodel,withthecriticalrequirement
a spectrum of models and algorithms for bulk-seq and scRNA-seq beingthealignmentofthegeneration,basedonthebest-pretrained
analyses,improvingcomputationalefficiencyandvisualengagement. decoder,with the real Bulkdata.Atthis point,the cell proportions
Rewritten models and algorithms and integrated different pre- outputbytheencoderaccuratelyreflectthecellproportionsofthe
processing options stem from benchmark testing28 (Supplementary actualBulk(Fig.1a).
Note1).Moreover,OmicVersefeaturessinglecelltrajectoryblending GiventhatBulkTrajBlend’sprimaryobjectiveistointerpolatedata
from Bulk RNA-seq (BulkTrajBlend), a specialized algorithm for fromoriginalscRNA-seqdata,thefocusshiftstothetargetedextrac-
addressing “omission” in single-cell data. BulkTrajBlend employs a tion of cells from the generated single-cell data. Considering the
beta-variational autoencoder and graph neural network-based algo- inherentchallengesassociatedwithcellannotation,theinputsingle-
rithmtodeconvolvesingle-celldatafrombulkRNA-seq,facilitatingthe celldatacontainingdiversecelltypesisexpectedtoexhibitoverlapsin
identification of “omitted” cells within the reconstructed single-cell real-worldscenarios.The“omitted”cellsweneedtorecovershould
landscape. maintainthecontinuousstateofthecells,thetraditionalcommunity
discovery algorithms cannot identify the overlapping cell commu-
Results nities.Cellsgeneratedbyβ-VAEaredirectlyrestoredtotheoriginal
DesignconceptofBulkTrajBlendandBenchmarking single-cell data, which will lose the continuous state of the cell. To
The conceptualization of BulkTrajBlend draws upon prior research, solvethisproblem,weintroduceNOCD,aGNN-basedalgorithmfor
proposingthatBulkRNA-seqdataisacompositeofscRNA-seqdata identifying overlapping communities that achieves the best perfor-
through a nonlinear superposition mechanism29,30. Central to this manceamongexistingbaselines33.UtilizingNOCDenablestheidenti-
notionistheimplementationofthebeta-variationalautoencoder(β- ficationofoverlappingcellcommunities.Wealsousethe“omitted”
VAE),apotenttoolforapproximatingBulkRNA-seqdatatoscRNA-seq cellintheoverlappingcommunitystateasthetargetcellsforrecovery.
representation31,32.Integratingtheβ-VAEenablestheconstructionof This insight is crucial for the subsequent task of recovering and
an encoder and decoder from single-cell data, traditionally char- reconstructing cell differentiation trajectories within the single-cell
acterizedbyunconstrainedattributes. sequencingdata(Fig.1b).
BulkTrajBlend advances the foundational structure of auto- ToassesstheefficacyandaccuracyofBulkTrajBlendinthecon-
encoders(AE)andβ-VAE.Theseenhancementsinvolve(1)employing textofcelldifferentiationtrajectoryrecovery,arigorousbenchmark-
anAEtoconstructaBulkRNA-seqgeneratoranalogoustorealBulk ingexerciseisundertaken.TheVAEmodulewithinBulkTrajBlendis
RNA-seqinspiredbyTAPE23.Wemodeledthecellularproportionspace systematically compared against alternative generative models,
of Bulk RNA-seq on the output of the Encoder, the input of the including conditional generative adversarial networks (CGAN)34 and
Decoder.SubsequentlyutilizinggroundtruthbulkRNA-seqgenerated auxiliary conditional GANs (ACGAN)35. This benchmarking exercise
fromsinglecellRNA-seqasinputofEncoderforcalculatingthetrue involves assessing a range of performance metrics for generating
cellularfractions.(2)Whenwetrainedβ-VAEusingrealsinglecellRNA- scRNA-seqfeaturesandtrajectoryinference features.These metrics
seq,theEncoderoutputswereV(celltypefraction)andW(celltype includethecorrelationofcell-type markergeneexpression,marker
correlatedgenerativefactor).Weaddedalossfunctiontominimize genesimilarity(quantifiedviacosinesimilarity),probabilityoftrajec-
therelationshipbetweenVandtherealcelltypefraction.Weobtained toryconversionpost-interpolation,andthedegreeofdatavariability
WforeachcellattheendofmodeltrainingandaveragedWforeach following interpolation. Notably, the findings consistently demon-
cell type to represent that cell type. (3) We used the true cell type strateBulkTrajBlend’ssuperiorperformance,characterizedbyheigh-
fraction V calculated by AE with the celltype-associated generating tenedcorrelationsinmarkergeneexpression,markergenesimilarity,
factorWobtainedbyβ-VAEasinputtoβ-VAEforgeneratingsingle-cell trajectory conversion probabilities, and minimal post-interpolation
data,anddeployingunsupervisedclusteringtodenoiseandrefinethe data variability in the generated single-cell data (Fig. 1c–f, Supple-
outcomes of the β-VAE. (4) We employed a graph neural network mentaryNote2,SupplementaryFigs.2–4).
(GNN) to sample the generated single-cell data, thereby identifying
overlappingcellcommunities.Samplingtheoverlappingcommunities Impactofvariedhyperparametersoninterpolationperfor-
ofcellshelpsustoinsert“omitted”cellswithoutlosingcellcontinuity. manceinBulkTrajBlend
The methodology based on β-VAE approximates the joint dis- Thisstudyexplorestheeffectofvaryinghyperparametersettingson
tributionofdataxandlatentgeneratingfactorszbyestimatingthe the performance of BulkTrajBlend, a tool reconstruction OPC tra-
probabilitydistributionqθ ðzjxÞrelativetothetrueposteriorqθ ðxjzÞ: jectories in the Dentate gyrus dataset and interpolating Basophil
Here, x denotes gene expression data,and z characterizes the nor- withintheHPCdataset.Weanalyzedtheimpactofhyperparameter
mallydistributedparametersofxpost-sampling.Itisnoteworthythat variations by examining five key factors: (1) the number of inter-
thisapproximationintroducesalevelofnoiseandbiasintothegen- polatedcells,(2)thecorrelationofmarkergeneexpressionbetween
erated data (Supplementary Fig. 1e). Consequently, unsupervised interpolatedandactualcells,(3)markergenesimilarity,(4)transition
clusteringisemployedasadatarefinementstrategytomitigatethe probabilitiesfollowinginterpolation,and(5)theprevalenceofnoise
impactofnoiseandenhancedatarobustness.Weuseunsupervised clusters.
NatureCommunications|( 2024)1 5:5983 2
a
Single Cell Profile
Simulated Bulk
Ground Truth
Encoder Decoder
Real Bulk Predicted
Fractions
Noisy Generate Filtered by Self-Cluster
Cell 1->J Cell 1->K
b
Initially,theeffectofchangingthesizeoftheinputsingle-cell cells.Markergenecorrelationandsingle-cellsimilarityimprovedsig-
data, ranging from 1000 to 20,000 cells, was investigated. An nificantlywithinthe1-4xinterpolationrange,outperformingthe6-10x
increaseindatasizeresultedinhighercorrelationsofmarkergene range. Conversely, larger interpolation sizes were correlated with a
expression and improved single-cell similarity as performed by notableincreaseinnoiseclusters(Fig.2e–h).
BulkTrajBlend(Fig.2a,b).Thetransitionprobabilities,however,were Contrary to expectations, a detailed analysis of the number of
only slightly better (Fig. 2c). Notably, an inverse relationship was neuronsinBulkTrajBlend’shiddenlayer,witharangefrom64to1024,
foundbetweenthesaturationofcellnumbersandthefrequencyof revealedthatahiddenlayerwithonly64neuronsexhibitedthehighest
noiseclusters(Fig.2d). marker gene correlation, similarity, and transition probability for
Next, the effect of interpolation size was examined, with sizes interpolatedsinglecells,whilealsoreducingnoiseclusteroccurrences
ranging from 1 to 10 times the original number of target “omitted” (Fig.2i–l).
Gene
1->N
Cell Cluster
Gene
1->N
Gene
1->N
Gene
1->N
Celltypes
Celltypes
Gene
1->N
Generate Single Cell Matrix and Noisy Cell Cluster Filtered
Cell Cluster Aggregation
min MAE
V (Cell type fraction)
Fine-tuning
W (Cell type correlated
generative factor)
min MAE
The Clustering Space of each Celltypes
“Omission” Cell Detection and Interpolation
Attr: overlap-Celltype
c d e f
Expression Correlation Marker Similarity Interpolation Density of
(Unique) (Unique) Transformation pseudotime
Gene
1->N
Continuous Matrix
Attr: Celltype
Cell 1->J
Cell 1->J
Generate RNA-seq
Inference Predicted
Cell 1->M+j (j<J)
Connectivities network Community
Gene
1->N
- Cell 1 - Cell 2
- Cell 3 - Cell 4
Continuous cell
m θ ax log p (A|F) interpolation
Cell
1->K
Article https://doi.org/10.1038/s41467-024-50194-3
Step1: Simulated Bulk
Step2: AE training and fine-tuning
Step3: VAE training
Step4: Noisy Filtered
NatureCommunications|( 2024)1 5:5983 3
Article https://doi.org/10.1038/s41467-024-50194-3
Fig.1|ArchitectureoftheBulkTrajBlendframework.aSingle-CellProfileGen- celltypesfortheoverlappingCelltypes.cCorrelationScoreofCell-TypeMarker
erationinBulkTrajBlend:Thisstageoutlinesthecreationofsingle-cellprofiles.An GeneExpression:Thiscomponentdisplayscorrelationscoresforcell-typemarker
initialsingle-cellprofile,representingthegroundtruthforcellfractions,and geneexpressionacrossthreemodelswithintheDentateGyrusandHematopoietic
simulatedbulktranscriptomedataareinputintoanautoencoder(AE).Simulta- datasets.dCell-TypeMarkerSimilarityAssessmentUsingCosineSimilarity:This
neously,realbulktranscriptomedataserveastheoptimalinputfortheAE.TheAE’s partaddressestheassessmentofsimilaritiesbetweencell-typemarkergenesusing
predictedcellfractionsdefinetheclusteringspaceoftheresultingsingle-cell cosinesimilarity.eProbabilityofCellConversion:Theframeworkevaluatesthe
profile,whichisthenprocessedbyaβ-VAEtogenerateaprofilesimilartothatof likelihoodofnIPC(neurogenicintermediateprogenitorcells)becomingOPC(oli-
realbulkdata.Anynoiseinthisprofileisreducedusingunsupervisedclustering. godendrocyteprogenitorcells)againstthebackdropofinterpolatedOPCcellsin
b“Omitted”CellDetectioninBulkTrajBlend:Here,aneighborhoodgraphcon- theDentateGyrusdataset,andthecorrespondinglikelihoodfortheconversionof
structedviaUMAPbasedonthegeneratedsingle-celldataidentifiesnodescorre- HSC(hematopoieticstemcells)toBasophilcellswithinterpolatedBasophilcellsin
spondingtoindividualcellsanddelineatesdistinctcommunitiesbycelltype.The theHematopoieticdataset.fPseudotimeDensityforOPCCells:Thisfinalcompo-
annotatedgraphistheinputforaGraphNeuralNetwork(GNN)thatdetects nentillustratesthepseudotimedensityofOPCcellsincorporatinginterpolated
overlappingcommunitiesandidentifiesmixedcelltypes,whicharethenreinte- OPCcellsintheDentateGyrusdataset,coupledwithananalogousrepresentation
gratedintotheoriginalsingle-cellprofile.Overlap-CellType:aone-hotmatrixof forBasophilcellspost-interpolationintheHematopoieticdataset.
a The size of scRNA-seq b The size of scRNA-seq The size of scRNA-seq c The size of scRNA-seq d The size of scRNA-seq
Interpolation Expression Correlation (Unique) Marker Similarity (Unique) Interpolation Transformation Noisy clusters
e Interpolation Scale Size f Interpolation Scale Size Interpolation Scale Size g Interpolation Scale Size h Interpolation Scale Size
Interpolation Expression Correlation (Unique) Marker Similarity (Unique) Interpolation Transformation Noisy clusters
i Hidden Layer Size j Hidden Layer Size Hidden Layer Size k Hidden Layer Size l Hidden Layer Size
Interpolation Expression Correlation (Unique) Marker Similarity (Unique) Interpolation Transformation Noisy clusters
m Dentategyrus (BulkTrajBlend) HPC (BulkTrajBlend) n PAGA Dentategyrus PAGA HPC (BulkTrajBlend) o The size of scRNA-seq
(BulkTrajBlend)
Fig.2|Thesystematichyperparametertestingforinterpolationperformance. single-cellprofiles,withtheHematopoieticdatasetontheleftandDentateGyrus
Thetestsexaminevaryingsizesofrawsingle-cellprofilesasinputina–d:(a)The ontheright.e–hThescalesizesofthegeneratedtargetcellsutilizedasinputis
quantityof“omitted”cellsgeneratedfromBasophilcellsintheHematopoietic scrutinized.i–lThesizesofneuronsinthehiddenlayervaryasinput.mTheflow
datasetandOPCcellsintheDentateGyrusdataset,respectively.bTheanalysis trendofcelldevelopmentaltrajectoriesofneurogenicintermediateprogenitor
juxtaposestwoaspects:ontheleftpanel,theexpressiontrends’correlationof cells(nIPC)isvisualizedonUMAPplotsfortheDentateGyrusontheleftandthe
markergenesbetweenthereferenceandgeneratedsingle-cellprofiles;andon Hematopoieticdatasetontheright.nCell-statetransitiondirectedgraphswithin
therightpanel,thesimilaritybetweenmarkergenesofthetwoprofiles.cThe thetrajectoryofPartition-basedGraphAbstraction(PAGA)graphsarepresented
transitionprobabilityofthegeneratedtargetcellsiscomputedalongthecellular fortheDentateGyrusontheleftandHematopoieticdatasetontheright.oThe
developmentaltrajectories,withBasophilcellsintheHematopoieticdatasetand model’sruntimeinrelationtodifferentsizesofrawsingle-cellprofileinputsis
OPCcellsintheDentateGyrusdataset.dTheextentofnoiseclusterspresentin illustrated.
NatureCommunications|( 2024)1 5:5983 4
Article https://doi.org/10.1038/s41467-024-50194-3
a Pancreas (Raw) b Pancreas c Pancreas (BulkTrajBlend) g Transitions Confidence
(Dropouts of Ngn3 high EP) of Dropouts Celltype
h Variance of Pesudotime Between
d PAGA Pancreas (Raw) e PAGA Pancreas f PAGA Pancreas (BulkTrajBlend) Raw, Dropouts and BulkTrajBlend
(Dropouts of Ngn3 high EP)
Fig.3|Reconstructionofcelldevelopmentaltrajectoriesinsimulated“omis- datasetpost-BulkTrajBlendinterpolationbasedonpyVIA’sdropoutassessments.
sion”withinsingle-cellProfiles.a–cSequentiallydepictedaretherawpancreas gTheconfidenceincellstatetransitionsasdeterminedbypyVIAispresentedfor
dataset’svelocitystream,theeffectofsimulatedomissionviacelldropouts,andthe variousdatasetsandexperimentalconditions.Thecorrespondingcolorbarssignify
refineddatasetpost-interpolationwithBulkTrajBlendfordropoutimputationas themethodologyemployed.Specifically,forthepancreasdatasetwithNgn3HighEP
determinedbypyVIA.TheUMAPembeddingiscolor-codedbycelltype,consistent dropouts,thedisplayedconfidenceindicatesthetransitionfromNgn3HighEPtopre-
withtheinitialclusterannotations.Explainedarethefollowingcelltypes:Ngn3High endocrinecells.InthebonemarrowdatasetwithHSCdropouts,thevaluesrepre-
EP,Ngn3Highendocrineprogenitor-precursor;Ngn3LowEP,Ngn3Lowendocrinepro- sentthetransitionconfidencefromHSCtoMonocytes.Likewise,theDentateGyrus
genitor-precursor,Alpha,glucagon-producingα-cells;Beta,insulin-producingβ- datasetwithdropoutsofGranuleImmaturecellsindicatesthetransitioncon-
cells;Delta,somatostatin-producingδ-cellsandEpsilon,ghrelin-producingε-cells. fidencefromGranuleimmaturetoGranulematurecells.hThevarianceinpseu-
d–fDisplayedinsequenceisthedirectedgraphoverlaidontheUMAPembeddings dotime,asestimatedbypyVIA,isdocumentedacrossdifferentdatasetsand
fortherawpancreasdataset,thedatasetwith“omission”incelldropouts,andthe experimentalmanipulations.
Inconclusion,theidealhyperparametersettinginvolvesusingthe differentiatingintoPre-endocrine cells.In the corresponding“omis-
entire single-cell dataset, interpolating at a scale of 2x or 4x, and sion” dataset, this probability was 0. BulkTrajBlend interpolation
configuring a hidden layer with 64 neurons. Under these optimal increased the probability to 0.035 (Fig. 3d–g, Supplementary Fig.
hyperparameters, BulkTrajBlend effectively reconstructs the nIPC- 6a–c). In the mouse dentate gyrus neurons development, Granule
OPC developmental flow pattern in dentate gyrus datasets and the Immature cells had baseline differentiation probability to Granule
HSC-Basophil flow pattern in hematopoietic system development Maturecellsof0.018,whilenoprobabilitywasobservedinsimulated
datasets(Fig.2m,n).Itisimportanttonotethatusingthefullsingle-cell “omission”dataset.BulkTrajBlend’sinterpolationresultedinaprob-
datasetimprovesaccuracy,whichalsosignificantlyincreasescompu- ability increase to 0.019 (Fig. 3g, Supplementary Fig. 5d–f, Supple-
tationaldemands(Fig.2o). mentary Fig. 6d–f). In human bone marrow development,
hematopoieticstemcellsstage2(HSC2)cellsshowedadifferentiation
Proficientreconstructionofcelldevelopmentaltrajectoriesin probabilityintomonocytesof0.082,comparedto0inthesimulated
simulated“omission”single-cellprofiles “omission”dataset.FollowingBulkTrajBlendinterpolation,theprob-
Our study extended beyond evaluating BulkTrajBlend’s ability to ability increase to 0.079 (Fig. 3g, Supplementary Fig. 5j–l, Supple-
reconstruct developmental trajectories in real datasets, by also mentaryFig.6g–i).Notably,theoriginalpseudotimevariabilityinthe
examiningitsperformancewithinsimulateddatasets.Wecraftedthree threedatasetswaspreservedafterinterpolation(SupplementNote3).
simulateddatasetswithspecific“omission”:thefirstomittedasubset TheseanalysescollectivelyhighlightBulkTrajBlend’seffectivenessin
of Ngn3High endocrine progenitor-precursor (Ngn3High EP) cells in accuratelyreconstructingauthenticdevelopmentaltrajectories.
mousepancreasdevelopment,thesecondremovedimmaturegran-
ulesfrommousedentategyrusneuronsdevelopment,andthethird OmicVerseprovidesacomprehensiveanalysisplatformforBulk
excluded hematopoietic stem cells (HSC) mesomorphic cells from RNA-seqdata
human bone marrow development. These cells were successfully Bulk RNA-seq is an established method for investigating the tran-
recognized in the reconstructed developmental trajectories within scriptomeofcombinedcellularsamples,tissueorbiopsies6.Itprobes
these simulated “omission” datasets (Fig. 3a–c, Supplementary Fig. gene expression,isoform variations, alternative splicing, and single-
5a–c,SupplementaryFig.5g–i). nucleotide polymorphisms, revealing critical biological information
In the mousepancreaticdevelopment dataset, PAGA plots illu- such as copy number variations, microbial contamination, transpo-
strated a baseline probability of 0.04 for Ngn3High EP cells sableelements,cell-typesdeconvolution,andneoantigens.Advances
NatureCommunications|( 2024)1 5:5983 5
Article https://doi.org/10.1038/s41467-024-50194-3
in bioinformatics have enhanced the ability to reveal these hidden minimizing single cell profile noise52. Importantly, the data format
dimensionsinBulkRNA-seqdata,expandingitsanalyticalapplications. inputforalltheaforementionedmethodsisconsistent,enablingusers
OmicVerse integrates an extensive collection of Bulk RNA-seq toconductanalysesusingAnndataformat,withsignificantlyimproved
analysis algorithms, previously developed mostly in R but now visualizationformoreelegantresults.OmicVerse’suser-friendlynat-
increasingly in Python, to promote their utilization and ureandstraightforwardapplicationareexemplifiedinFig.5b.
interconnectivity36.Ourintegrationenhancestheexistingrepertoireof Illustrating Omicverse’s practical application in scRNA-seq, we
analysisalgorithmscateringtosingle-cell,spatialtranscriptomics,as analyzed a colorectal cancer (CRC) dataset, emphasizing the tumor
wellasmachinelearninganddeeplearningmodels37. microenvironment (TME) cell atlas integration53,54. Beginning with
TheplatformhostsacomprehensiveassortmentofBulkRNA-seq automaticcellannotationviapySCSA,theresultsshowedhighcon-
algorithms, including pyComBat38 for batch correction, pyDEG for cordancewithmanualannotations(Fig.5c),withanf1_scoreof0.856,
differential expression analysis using Deseq239, t-test, and Wilcoxon highlightingOmicVerse’sannotationaccuracy(Fig.5d).UsingAUCell,
tests,pyPPIforprotein-proteininteractionnetworkusingSTRINGweb we confirmed the expected signaling pathway enrichment in cell-
API40,pyWGCNAforgeneco-expressionnetwork41,pyGSEAforgene specificreceptorpathways:theB-cellreceptorsignalingpathwaywas
setenrichmentanalysis42,andpyTCGAforTheCancerGenomeAtlas prominenceinBcells,whiletheT-cellreceptorsignalingpathwaywas
(TCGA)dataanalysis,completewithsurvivalanalysis(Fig.4a). mostpronouncedinTcellsandNKcells(Fig.5e).Inaddressingthe
To evaluate the OmicVerse’s analytical pipeline, we analyzed sparsity inherent in previous CRC single-cell data analysis and
Alzheimer’sdisease(AD)data,beginningwithpyDEGtoidentifydif- to enhance resolution and depth, we utilized SEACells to extract
ferential expressed genes between AD patients and controls, high- metacells from the scRNA-seq data. After 39 epochs, the metacell
lightingthetop10foldchangegenes.Then,weconductedGeneSet aggregationiterationconverged,attainingahighcellpurityof0.98,
EnrichmentAnalysisatthegenelevelusingpyGSEA,orderinggenes withcompactnessandseparationvaluescloselyapproximating0(Fig.
according to p-values derived from pyDEG’s differential expression 5f, SupplementaryFig. 7a–c).The SEACellsalgorithm enhanced cell
analysis.Wefurtherbuiltaco-expressionnetworkfromthetop5000 type differentiation, with the signal intensity for receptor pathways
genes exhibiting the highest absolute median difference (MAE), beingsignificantlyaccentuated(SupplementaryFig.7d).
selecting the most differential expression module for visualization Furthermore,wetracedepithelial-to-cancercelldifferentiation
(SeeSupplementaryNote4forMethods). trajectoriesusingpyVIAandannotatedcancercelltypeswithinthe
OmicVerse’s workflow simplifies Bulk RNA-seq analyses with epithelial population with pySCSA, identifying distinct pathways
minimal coding required (Fig. 4b). Parameter adjustments may including Epithelial-to-Mesenchymal Transition (EMT) and Metas-
enhancevisualoutputs.Ouranalysisrevealed56genesdifferentially tasis. This analysis provided deep insights into cancer progression
expressed in AD: 48 upregulated and 8 downregulated. Box plots (Fig.5g).Bycommencingthetrajectorywithstemnessasthestarting
showcasedthemostalteredgenes(Fig.4c–e).GeneSetEnrichment point, we delineated the pseudotime trajectory of cancer cell dif-
Analysisexposedover-representedpathwaysrelevanttoAlzheimer’s, ferentiation,revealingthreedistinctivedirections:EMT-Differentia-
consistentwithestablishedliterature(Fig.4f,g).Moreover,wefocused tionandMetastasis,representingtwostagesinthetransitionfrom
onthemostvariablegenesfromthetop5000,discerning12modules epithelialcellstocancercells.Thisanalysisprovideddeepinsights
through pyWGCNA at 5 soft threshold. Notably, modules 4 and into the dynamics of cancer evolution. In a parallel approach,
5showedthehighestratesofdifferentialgeneexpression,withmod- metacellswithintheepithelialcellsubpopulationweresubjectedto
ule5containingAPPproteins.Furtherprobingofthesemodulespro- furtheraggregativeanalysis.Duetotheinherentsimilaritiesamong
videsinsightintotheirnetworkconnectivity(Fig.4h–j). epithelial cells, the average cell purity of the metacells obtained
was reduced to 0.9, while compactness and separation values
OmicVerseprovidesaversatilemultifacetedframeworkfor remainedincloseproximityto0(SupplementaryFig.7e,f).Conse-
Single-CellRNA-SeqAnalysis quently, we extrapolated the metacells of epithelial cells into tra-
Single-cell RNA-seq is a powerful high-throughput technique that jectories,revealingthatEMT-differentiationandMetastasisservedas
enablesthemeasurementofgeneexpressionpatternsandcelltypesat thetwoprimarydifferentiationpathways,aligningwiththeanalysis
thesingle-celllevel.Ithasbecomeacrucialtechniquefordelineating conductedonallcells(SupplementaryFig.7g–i).
cellularheterogeneity,differentiation,anddiseasemechanisms,par- Finally,toinvestigatetheinteractionnetworkbetweenepithelial
ticularlyincancerresearch.scRNA-sequnravelstumorcelldiversity cellsandotherTMEcells,weestablishedaCRCcellcommunication
and tracks tumor progression to anticipate cellular deterioration43. networkusingCellPhoneDB(Fig.5h).Theanalysisincludedimmune
The breadth of scRNA-seq data analysis facilitated by OmicVerse cells, including B-cells, T-cells, NK-cells, and plasma cells, exploring
includes cell annotation, examinationof cellinteractions, trajectory theirinteractionswitheightsubtypesofepithelialcells.Theanalysis
inference, states evaluation within gene sets, and drug responses revealedthatPPIA-BSGandLTB-LTBRwererecurrentligand-receptor
prediction44. The framework supports Anndata-standardized data pairsmediatingtherecognitionofcancerepithelialcellsbyimmune
processing for integrated downstream analysis and benefits from cells(Fig.5i).Notably,PPIA-BSGandLTB-LTBRhavebeenlinkedtoa
benchmarked data transformations28. Preprocessing methods in positivecorrelationinvariouscancersandareassociatedwithpoor
OmicVersefeatureoptimallogarithmictransformationwithpseudo- prognosis55,56. OmicVerse’s data harmonization significantly stream-
count addition, principal-component analysis (PCA), and Pearson linesthiscomprehensiveanalysis,enablingresearcherstodelveinto
residualnormalization.Forvisualizingreduceddimensions,itemploys personalizedexplorationsasoutlinedinourdetailedtutorial(Referto
GPU-accelerated Uniform Manifold Approximation and Projection SupplementaryNote5fortheMethods).
(UMAP)throughpymde45.
Incorporating a suite of state-of-the-art scRNA-seq algorithms, OmicVerseperformedmulti-omicsanalysiswithMOFA
OmicVerse’s integrated toolset includes pyHarmony46, pyCombat38, andGLUE
scanorama47 for batch correction, pySCSA48, updated with Single-cellsequencingadvancementsenabletheinvestigationofbio-
CellMarker492.0andCancerSEA50forenhancedcell-typeannotation, logicalsystemsacrossdifferenttissuelevels.AkeyelementinscRNA-
CellPhoneDB12forcell-cellinteractionsanalysispyVIA13fortrajectory seqisunderstandingtheimpactofchromatinaccessibilityvariation,
inference,AUCellforgenesetscoreevaluatesbasedonAreaUnderthe which is quantified by Single-cell sequencing assay for transposase-
Curve51, and scDrug for drug prediction14 (Fig. 5a). The OmicVerse accessiblechromatin(scATAC-seq).TheconjoinedanalysisofscATAC-
frameworkalsointroducesSEACellsformetacellanalysis,effectively seq and scRNA-seq data is critical for unraveling transcriptional
NatureCommunications|( 2024)1 5:5983 6
a b
c
Neuropath.Dx.1
d e
f
g
h
0.0
-0.2
-0.4
i
j
regulatory complexities. While scNMT-seq can capture both mod- WithinOmicVerse,theGLUE_pairalgorithmleveragesthePearson
alitiessimulaneously,obtainingunpaireddatafromidenticaltissuesis correlationcoefficienttocomputecellsimilaritybetweenscRNA-seq
morecommon57.Addressingthisdisparity,GraphicalLinkageUnified andscATAC-seqbaseonembeddingfromGLUE(Fig.6a).Theaccuracy
Embedding (GLUE) offers a Graphical Linkage Unified Embedding ofGLUE_pairisverifiedusingtheAdjustedRandScore(ARI)toconfirm
solutionforintegratingunpaireddata58,andMulti-OmicsFactorAna- celltypecongruencepost-normalization.Fortheanalysisofpairedcell
lysis(MOFA)elucidatesthevariationswithinomicsdata59.OmicVerse modalities, OmicVerse applies MOFA’s core algorithm, simplifying
utilizes both GLUE and MOFA to reveal transcriptional regulatory ensuingdataanalysisandvisualizationtasks(Fig.6a),allachievable
dynamics. withminimalcoding(Fig.6b).
erocS
tnemhcirnE
NES: -1.967
Pval: 0.000
FDR: 0.004
4.0
2.0
0.0
-2.0
-4.0
0 5000 10000 15000
Rank in Ordered Dataset
cirtem
tsil
deknaR
Electron Transport Chain
0.0
-0.2
-0.4
-0.6
Zero score at 8423
erocS
tnemhcirnE
NES: -1.874
Pval: 0.000
FDR: 0.011
4.0
2.0
0.0
-2.0
-4.0
0 5000 10000 15000
Rank in Ordered Dataset
cirtem
tsil
deknaR
Article https://doi.org/10.1038/s41467-024-50194-3
pyDEG-Different Expression Analysis
1 #Different expression gene analysis
2 data=ov.utils.read('expression.csv', index_col=0)
3 dds=ov.bulk.pyDEG(data)
4 dds.normalize()
5 dds.deg_analysis(treatment_groups, control_goups, method='wilcox')
6 dds.foldchange_set(fc_threshold=0.15, pval_threshold=0.05, logp_max=6)
pyGSEA-Pathway Enrichment Analysis
1 #Pathway Enrichment
2 deg_genes=result.loc[result['sig']!='normal'].index.tolist()
3 pathway_dict=ov.utils.geneset_prepare('WikiPathway_2021_Human.txt',
4 organism='Human')
5 enr=ov.bulk.geneset_enrichment(gene_list=deg_genes,
6 pathways_dict=pathways_dict, pvalue_type='auto',
7 background=result.index.tolist(), organism='Human')
pyWGCNA-Weight Gene Co-expression Network Analysis
1 #Weight Gene Co-expression Network Analysis
2 gene_wcgna=ov.bulk.pyWGCNA(data, save_path='result')
3 gene_wcgna.calculate_correlation_direct(method='pearson', save=False)
4 gene_wcgna.calculate_correlation_indirect(save=False)
5 gene_wcgna.calculate_soft_threshold(save=True)
6 gene_wcgna.calculate_corr_matrix()
7 gene_wcgna.calculate_distance()
8 gene_wcgna.calculate_geneTree()
9 gene_wcgna.calculate_dynamicMods()
10 module=gene_wcgna.calculate_gene_module()
11 gene_wcgna.plot_matrix()
DEG Analysis Gene Expression
Sphingolipid Metabolism
Zero score at 8423
NatureCommunications|( 2024)1 5:5983 7
Article https://doi.org/10.1038/s41467-024-50194-3
Fig.4|AcomprehensiveoverviewofBulkRNA-seqdataanalysisutilizing comparisons.Theenrichmentscoreswereevaluatedastwo-sided,considering
OmicVerse.aAgraphicaldepictionillustratesvariousanalyses:differential bothpositiveandnegativedeviationsfromtheexpecteddistributionunderthenull
expressionanalysis(pyDEG),genesetenrichmentanalysis(pyGSEA),protein- hypothesis).gGenesetenrichmentanalysis(GSEA)isexecutedusingWikiPathways
proteininteractionanalysis(pyPPI),andweightedgeneco-expressionnetwork genesets,withenrichmentscoresandp-valuesderivedfromaweightedtwo-sided
analysis(pyWGCNA).bAcodesnippetdemonstrateshowtoimportdataand Kolmogorov–Smirnov-likestatisticandnormalizedforgenesetsize,producingthe
executepyDEG,pyGSEA,andpyWGCNA,incorporatingcontinuouscovariates. NormalizedEnrichmentScore(NES).hTheoptimalsoftthresholdisdetermined,
cPrincipalComponentAnalysis(PCA)embeddingsdistinguishsampleswithin wherethehorizontalaxisrepresentsthesoftthresholdgradient,theleftvertical
Alzheimer’sandcontrolgroups.dAvolcanoplothighlightsdifferentiallyexpressed axiscorrespondstothescale-freefitindex(withhighervaluespreferred),andthe
genes;thoseupregulatedaremarkedinred,whiledownregulatedgenesareindi- rightverticalaxisreflectstheaveragenodeconnectivity(withlowervaluespre-
catedinblue.eAboxplotrevealsthetop10geneswiththemostsignificantfold ferred).iAgeneclusteringdendrogramillustratesdissimilaritybasedontopolo-
changebetweenAlzheimer’s(n=44)andcontrolgroups(n=46)(Boxplotisdis- gicaloverlap,combinedwithmodulecolorassignments.Consequently,twelveco-
playedwiththecenter-lineasmedian,theboxlimitsaslowerandupperquartiles, expressionmodulesareidentified,eachdisplayedinadistinctcolor.Anaccom-
andwithwhiskerscoveringthemostextremevalueswithin1.5xInterquartile- panyingheatmapdepictsthecorrelationamongthe5000geneswithineach
Range).fWikiPathwaysenrichmentresultsarevisualized,withdotsizecorrelating module.jModules4and5,whicharescale-freenetworks,areshownwhereeach
tothegenecountforeachfunctionandcolorintensityreflectingp-valuesig- noderepresentsagene.Thenodesizecorrespondstogeneconnectivity,andcolor
nificance–darkerhuesindicatehigherpathwayenrichment(top10ofpositiveand denotesthemoduleaffiliation,withthefivemostcentralgenesineachmodule
negativeNES,padj<0.05,padjcalculatedbyGSEApypythonpackage,Forthe labeled.
statisticalanalysis,weusedthepvalueadjustmenttocontrolformultiple
DemonstratingtheintegrationofGLUEandMOFA,weanalyzed thereferenceBulkRNA-seqdata.Wesuggestthatuserscanadoptan
simultaneoussingle-nucleusRNA-seq(snRNA-seq)andsingle-nucleus additionalcomprehensivesingle-cellprofiletotrainBulkTrajBlendand
ATAC-seq (snATAC-seq) data from cortical regions of Alzheimer’s thenperforminterpolationoftheirdata,therebyavoidinggenerating
diseasepatients60.Ouranalysisofalignedcelltypesuncoveredcon- BulkTrajBlendwithoutinformationaboutthetargetcells.
sistentpatternsindicativeofcommoncellularstates(Fig.6c,d).Froma Upon devising the interpolation algorithm for Bulk RNA-seq in
random subset of 5000 paired cells, MOFA unveiled 13 factors scRNA-seq,itbecameapparentthataunifiedPython-basedframework
(Fig.6e,f).Thefactors1-6accountedforRNA-relatedvariance,while forcomprehensivedualanalysisoftheseplatformswasmissing.Tofill
thesecond for ATAC-related variance.The interaction among these thisvoid,wedevelopedOmicVerse,seamlesslyintegratingsingle-seq
factorsand celltypes revealed significantassociations:EX-signature andbulk-seq.OmicVerseintroducesaspecializedanalysisobjectfor
with Factor 1, PER.END-signature with Factor 5, ASC-signature with each omics layer, facilitating streamlined analysis and ensuring an
Factor 2, MG-signature with Factor 3, and INH-signature jointly intuitiveuserexperience.OmicVersenotonlyhasawell-established
detailedbyFactors6and4.Additionally,geneweightsforeachfactor scRNA-seq ecosystem like Seurat, which complements Scanpy, but
uncovered genes with the most considerable influence on their alsofeaturesauniqueBulkRNA-seqecosystem,thusofferingacon-
respectivesignatures(RefertoSupplementaryNote6fortheMethods, sistentanduser-friendlyinterface(SupplementNote7).
SupplementaryFig.8a–c). AsanintegratedframeworkforbothBulkandsingle-cellRNA-seq
analysis,OmicVerseoffersasuiteofanalyticaltoolsthatinclude,but
Discussion arenotlimitedto:
Theinnovativefusionofthevariationalautoencoderandgraphneural (1)BulkRNA-seq:OmicVerseprovidescomprehensivefunction-
networkscombinedinthecreationoftheBulkTrajBlendframework. alities, including multi-sample integration, batch effect correction,
ThisframeworkaimstodeconvolvescRNA-seqdatawithinBulkRNA- differential gene expression analysis, gene set enrichment analysis,
seq and elucidate precise cell-specific developmental trajectories in protein interaction networkconstruction, the identification of gene
scRNA-seq.Itdemonstratessignificantaccuracyandrobustness,due co-expressionmodules,andTCGAdatabasepreprocessing.
in large part to the unique integration of the topological overlap (2) Single-cell RNA-seq: OmicVerse offers robust features,
community in graph neuralnetworks,whichskillfully addresses the including multi-sample quality control, batch effect removal and
potentialbiasintroducedbyunsupervisedclusteringinthesingle-cell integration,automatedcelltypeannotation(withmultipledatabases
dataoutcomes. support)andmigrationannotation,celltypeandgenesetenrichment
A conceptual parallel exists between back-calculating cell pro- analysis, developmental trajectory reconstruction, metacell identifi-
portionsinBulkRNA-seqfromscRNA-seqandusingBulkRNA-seqasa cation,cellularinteractionnetworkanalysis,anddrugresponsepre-
scaffoldforinterpolatingscRNA-seq.However,thelatterisinherently diction. It also covers scATAC-seq integration and multi-omics
morechallengingduetotheneedtoaccuratelyinterpolattheinade- analysis,inherentlylinkedtoRNA-seq.
quatetargetcelltype.Whilenumeroussingle-cellgeneratorsperform (3) Bulk RNA-seq to scRNA-seq: OmicVerse enhances the
well in generating scRNA-seq data, the incorporation of unknown deconvolution of Bulk RNA-seq, cell proportions estimation, inter-
informationremainsanintrinsicchallenge.Forexample,scDesign3isa polationthescRNA-seqdataandtherecoveryofdevelopmentaltra-
proficientstatisticalsimulatorthatcreatesrealisticsingle-celldataby jectorieswithinscRNA-seq.Actingasacriticalbridgeinthetransition
learning interpretable parameters from actual scRNA-seq data. fromBulktosingle-cellRNA-seq.
Nevertheless, reconstructing cell developmental trajectories often The OmicVerse documentation provides a detailed Applica-
requireselusiveparameters,whichnecessarilyleveragesknowndata tion Programming Interface (API) reference for each algorithm,
from Bulk RNA-seq61. Hence, BulkTrajBlend is meticulously crafted coupledwithtutorialsthatclarifytheirfunctions,limitations,and
basedontheprinciplesofscDesign361andscGen32,withthestatespace synergies with other bulk and single-seq analysis tools. These
andparametersbeinginformedbyBulkRNA-seq.Notably,cellcate- resourcesareaccessibleviaGoogleColab,offeringafreecompu-
gorizationintheresultingsingle-celldataoftenreliesonunsupervised tationalworkspaceforpipelineexaminations.OmicVersealsohas
annotation. By introducing GNN, BulkTrajBlend effectively reduces comprehensive developer documentation that makes it easy for
resolution-dependentissuesassociatedwithunsupervisedclustering. users to add tools to the ecosystem following a consistent
WhileBulkTrajBlendcanefficientlyextractthestatespaceofcells developmentlogic.
fromBulkRNA-seqandinterpolatetheoriginalscRNA-seqdata,this Our primary goal was to foster an ecosystem replete with
interpolationreliesontheselectionofthereferencescRNA-seqversus visually engaging and insightful visualizations, fully integrated
NatureCommunications|( 2024)1 5:5983 8
Meta cells CRC
X_umap1
within the Python programming environment. OmicVerse allows community.WeanticipatethatOmicVersewillcontinuetogrow,
userstoperformextensive transcriptome analysisusing asingle with updates introducing additional algorithms, features, and
programming language, tapping into the collective machine- models.Ultimately,OmicVerseaimstoactasadrivingforceforthe
learning knowledge and models available within the Python bulk and single-seq community, encouraging the prototyping of
2pamu_X
X_umap1
B cell
Endothelial cell
Epithelial cell
Fibroblast
Mast cell
Myeloid cell
Natural killer cell
Plasma cell
T cell
pDC
2pamu_X
MaunalAnnotation CRC
X_umap1
2pamu_X
a Cells c d
B cell receptor signaling pathway
b e
0.06
0.03
0.00
f
g
seneG
Matrix SCSA annotation Trajectory inference Celltype1 Celltype2
Celltype3
Celltype4 Celltype5
Cell interaction Drug response predictPathway analysis
X_umap1
i
2pamu_X
Automatic Annotation CRC F1 score with average=weighted:0.86 AMI score:0.79
T cell receptor signaling pathway
0.08
0.04
0.00
Epithelial Streamplot Epithelial PAGA-Graph
MMeettaassttaassiiss--22
SStteemmnneessss QQuuiieesscceennccee CCeellll CCyyccllee
IInnffllaammmmaattiioonn
MMeettaassttaassiiss--11
EEMMTT
DDiiffffeerreennttiiaattiioonn
llec
B
llec
T
llec
amsalP
llec
rellik
larutaN
Fraction of cells in group (%)
1020304050
Mean expression
in group
0.5 1.0 2PLPA 55DC AIPP BTL AIPP D4AMES D4AMES BTL 01FSFNT FNT D4AMES A01TNW D4AMES 1LZPM 2PLPA 6SAG AIPP PBORYT D4AMES D4AMES 21FSFNT 061DC
B cell
Natural killer cell
Plasma cell
T cell
Fraction of cells
in group (%)
1020304050
Mean expression
in group
0.0 0.5 1.0
RGIP 5ERGDA GSB RBTL GSB 1BNXLP 2BNXLP RBTL
B01FSRFNT A1FSRFNT
1BNXLP 5DZF 2BNXLP 1LZPM RGIP LXA GSB 44DC 1BNXLP 2BNXLP
A21FSRFNT 41FSRFNT
Article https://doi.org/10.1038/s41467-024-50194-3
pySCSA-Celltype Automatical Annotation
1 import omicverse as ov
2 adata=ov.read('epi.h5ad')
3 #Autmatical annotation
4 scsa=ov.single.pySCSA(adata, foldchange=1.5, pvalue=0.05,
5 celltype='cancer', target='cancersea', tissue='All')
6 scsa.cell_anno(clustertype='leiden', cluster='all')
7 scsa.cell_auto_anno(adata)
pyAUCell-Pathway Enrichment Analysis
1 ##Assest one genesets
2 ov.single.geneset_aucell(adata, geneset_name='Sox',
3 geneset='Sox17', 'Sox4', 'Sox7', 'Sox18', 'Sox5')
4 ##Assest all pathways
5 pathway_dict=ov.utils.geneset_prepare('KEGG_2021_Human.txt',
6 organism='Human')
7 adata_aucs=ov.single.pathway_aucell_enrichment(adata,
8 pathway_dict=pathway_dict, num_workers=8)
pyVIA-Trajectory Inference
1 #Trajectory inference
2 v0=ov.single.pyVIA(adata=adata, adata_key='X_pca', basis='X_uamp',
3 clusters='celltype', knn=30, oot_user=['Stemness'])
4 v0.run() 5 v0.get_pseudotime(adata)
6 #PAGA Graph
7 ov.utils.cal_paga(adata, use_time_prior='pt_via', vkey='paga', groups='celltype')
CellphoneDB-Cell Cell Interaction
1 #cell-cell interaction 2 cpdb=ov.single.cpdb(cpdb_file_path, adata, cluster_key='celltype')
3 interaction=cpdb.network_cal(cluster_key='celltype') 4 cpdb.submeans_exacted(cell_names='Epithelial cell', cell_type='receptor')
5 cpdb.submeans_exacted(cell_names='Epithelial cell', cell_type='ligand')
SEAcells-Metacells Analysis
1 #Metacells analysis
2 model=ov.single.SEAcells(adata_sea, build_kernel_on=build_kernel_on,
3 n_SEACells=n_SEACells, n_waypoint_eigs=n_waypoint_eigs,
4 convergence_epsilon=1e-5)
5 model.fit(min_iter=10, max_iter=100)
6 model.save('epi_meta.pkl')
7 model.load('epi_meta.pkl')
8 model.computer_celltype_purity()
9 model.summarize_by_soft_SEACell(celltype_label='major_celltype',
10 minimun_weight=0.05)
Cell Cycle
Differentiation
EMT
Inflammation Metastasis-1
Metastasis-2
Quiescence
Stemness
Fig.5|OmicVerseacomprehensiveanalyticalplatformforsingle-cellRNA-seq enrichmentwithinCRCcellsiselucidatedinaUMAPvisualization,withtheleftside
analysis.aAgraphicaloverviewhighlightscrucialanalysismodules:celltype indicatingBcellreceptorsignalingandtherightsidedetailingTcellreceptor
annotation(pySCSA),cellularinteractions(CellPhoneDB),trajectoryinference signaling,asanalyzedbyAUCell.fMetacellcompositionwithintheCRCdatasetis
(pyVIA),pathwayanalysis(AUCell),anddrugresponseprediction(scDrug).bAn revealedinaUMAPplot.gEpithelialcellsubpopulationsinCRCaredisplayedina
examplecodesnippetillustratestheprocessforloadingdataandconducting UMAPplot;automatedannotationsbypySCSAaredemonstratedontheleft,
analysesusingpySCSA,CellPhoneDB,pyVIA,AUCell,andSEACells,withtheinclu- complementedbyacellstatetransitiondirectedgraphderivedfromaPartition-
sionofcontinuouscovariates.cUMAPplotvisualizessingle-cellRNAsequencing basedGraphAbstraction(PAGA)trajectoryontheright.hCellPhoneDBcomputes
(scRNA-seq)datafromcolorectalcancer(CRC)patients.Theplotcontrastsmanual aninteractionnetworkbetweenCRCcelltypes,offeringinsightsintointercellular
celltypeannotations,shownintheleftpanel,withautomaticannotationsdepicted communication.iScaledmeanexpressionlevelsofgenesthatcodeforinteracting
intherightpanel.dTheconcordancebetweenmanualandpySCSA-generated ligand-receptorproteins,identifiedbyCellPhoneDB,areshownindotplotsto
annotationsispresentedinarow-normalizedconfusionmatrix.ePathway underscorethesupportinginteractionsbetweenimmuneandepithelialcells.
NatureCommunications|( 2024)1 5:5983 9
Article https://doi.org/10.1038/s41467-024-50194-3
a
c e
Cell Type
Varience
AA AA A A AAA AA AAA AA A AA AA A AA AA A AA A A A A A A
d Domain
b
pyMOFA-Paired the omics using GLUE f Correlation
1 #Paired the Cell from two-omics
2 import omicverse as ov
3 rna=ov.read("chen_rna-emb.h5ad")
4 atac=ov.read("chen_atac-emb.h5ad")
5 pair_obj=ov.single.GLUE_pair(rna, atac)
6 pair_obj.correlation()
7 res_pair=pair_obj.find_neighbor_cell(depth=20)
8 rna, atac=pair_obj.pair_omic()
pyMOFA-Multi omics factor analysis
1 #MOFA calculated with omicverse
2 mofa_obj=ov.single.pyMOFA(omics=[rna1, atac1],
3 omics name=['RNA', 'ATAC'])
4 mofa_obj.mofa_preprocess()
5 mofa_obj.mofa_run(outfile='models/chen_rna_atac.hdf5')
6 mofaart_obj=ov.single.pyMOFAART(
7 model path='models/chen_rna_ atac.hdf5')
8 mofaart_obj.get_factors(rna1)
Fig.6|Theintegrationofmulti-omicsdataanalysisbyOmicVerse,utilizing Alzheimer’sDisease.dIntegratedcellembeddingsfromvariousomicslayersare
bothMOFAandGLUE.aTherepresentationincludesagraphicalmodelofcelltype displayedinUMAPvisualizations,withcolor-codingreflectingtherespectiveomic
correlationsusingGLUE,alongsideanillustrationofcellvariancecapturedby strata.eAheatmapillustratesthepercentageofvarianceaccountedforbyeach
MOFA,asindicatedbytheEvidenceLowerBound(ELBO).bAsamplecodesnippet factor(displayedasrows)acrossdifferentomicslayers.fAnotherheatmapexhibits
isprovidedfortheimportandprocessingofdataviapyMOFAtools.cAUMAPplot theresultsofcorrelationanalysesbetweencelltypesandtheMOFAfactors.Colors
showsthedistributionofcelltypesidentifiedinscRNA-seqdatafrompatientswith representtestsofsignificance.
various models, establishing standards for RNA-omics analysis, Proportion,bytrainingAE.Wethendefinetheoutputofthegen-
andexpandingthepotentialforscientificexploration. eratorasGandwemakeGandB closetoeachotherbyMAE
simulated
asanevaluation.AftertrainingtheoptimalAE,wechangetheinput
Methods to real Bulk RNA-seq B , at which time the output of the
groundtruth
MethodsforBulkTrajBlend encoder,T,istheCellProportioncorrespondingtorealBulk,which
BulkTrajBlendisprimarilydesignedtoaddresstheissueof“omitted” we use as the range of the generator space for the subsequent
cells in single-cell data, making the inference of developmental or β-VAE.
differentiation trajectories continuous. To achieve this goal, we
designedBulkTrajBlendtogeneratepotential“missing”cellsfrombulk Generationofsingle-celldata.GivenadatasetfX,V,Wg,wherethe
RNA-seqdataforinferringpseudo-timecelltrajectories.Thisprocess vector x2RM in the gene expression matrix X represents gene
consists of the following four steps (where communities represent expressionvectorofacell,thevectorv2RKiPnthemat(cid:2)rixV(cid:3)represents
celltypes): celltypeproportion,satisfyinglogðpðvjxÞÞ= logðp v jx Þ,wherev
k k
isrestrictedbyalossfunction:
Cellproportioncalculation.Toestimatetheproportionofcellsin X(cid:4) (cid:4)
BulkRNA-seq,wefirstannotatedthesingle-celldatawithrespective MAE= (cid:4) v(cid:2)v^(cid:4) ð1Þ
celltypesandaggregatethegenecountsofsinglecellsbycelltype, v
resultinginanN*Mmatrix,whereMrepresentsthenumberofcell
typesandNrepresentsthenumberofgenes.WedefinethisN×M Herev^isthepredictedproportionsofcertaincelltype.
matrixasthesimulatedBulkRNA-seqcelltypematrix,andthenwe The vector w2RK in the matrix W represents conditionally
sum M columns of each row to get the simulated Bulk RNA-seq correlatedgenerativefactor.Thefactorwisobtainedfromthesame
B , and we input the simulated Bulk RNA-seq into the self- classofcellsthroughtheβ-VAEEncoder.Foreachclassofcells,the
simulated
encoder of AE. In the self-encoder, we define the output of the averagevalueaftermodeltrainingrepresentsaclassofcell-specificw,
encoder as T, and we make T close to Numberofthecell, i.e., Cell anditisnotrestriectedbyaddingalossfunction.AccordingtoHiggins
Numberofallcells
NatureCommunications|( 2024)1 5:5983 10
Article https://doi.org/10.1038/s41467-024-50194-3
etal.26,wehypothesizethatgeneexpressionvectorsxaregenerated cellcommunities33.GNNcanlearnrelationshipsbetweennodesand
byaprobabilitymodelpθ ðxjv,wÞ,whereθrepresentsthegenerative divide them into different communities based on their similarities.
modelparameters.Themodellearnsthejointdistributionofthedatax Specifically,weusedGCN,whichisoneofthebasicmodelsinGNN,to
andasetoflatentvariablesz (z2RM,whereM≥K)forgenerating generate an affinity matrix G, which represents the degree of asso-
observed data x, i.e., pθ ðxjzÞ≈pðxjv,wÞ, and approximates the true ciationbetweencells.Thecomputationisasfollows:
posteriordistributionpθ ðzjxÞwithanapproximateposteriordistribu-
tionqϕ ðzjxÞthatiseasiertocompute.Ourgoalistoensurethatthe G: =GNNθ ðA,XÞ ð6Þ
inferredlatentvariablesz capturethegenerativefactorsw inadis-
Here,Aistheadjacencymatrixofthecellneighborhoodgraph,
entangledmanner.Adisentangledrepresentationimpliesthatindivi-
and X represents cell type as the node feature. To ensure non-
duallatentunitissensitivetovariationsinasinglegenerativefactor
negativityofG, weapplied element-wise ReLUnon-linearactivation
whilebeingrelativelyinvarianttovariationsinotherfactors.Inadis-
functiontotheoutputlayer.FordetailedinformationabouttheGNN
entangledrepresentation,knowledgeofonefactorcanbegeneralized
architecture,
tonewconfigurationsofotherfactors.Theconditionallycorrelated
generativefactorswcanremainentangledinaseparatesubsetofzand (cid:7) (cid:7) (cid:8) (cid:8)
arenotusedtorepresentv. G: =GCNθ ðA,XÞ=ReLU A ^ ReLU AA ^ XWð1Þ Wð2Þ ð7Þ
To achieve this, we minimize the KL divergence between the ^ ^(cid:2)1e^(cid:2)1 e
approximateposteriorandthetrueposterior:
Here,A=D 2AD 2isthenormalizedadj
^
acenPcym
e
atrix,A=A+I
N
is
the adjacency matrix with self-loops, and D = A is the diagonal
ii j ij
X
degreematrixoftheadjacencymatrixwithself-loops.Weconsidered
KLðqϕ ðzjxÞjjpθ ðzjxÞÞ= (cid:2) qϕ ðzjxÞlogðpθ ðxjzÞqϕ ðzjxÞÞ+ logðpθ ðxÞÞ
otherGNNarchitecturesanddeepermodelsbutdidnotobservesig-
z nificantimprovements.Twomaindifferencesbetweenourmodeland
ð2Þ
thestandardGCNare:(1)batchnormalizationappliedafterthefirst
Here,KLðqϕ ðzjxÞjjpθ ðzjxÞÞisthevariationallowerboundandcan graph convolutional layer, and (2) L2 regularization applied to all
bewrittenas: weight matrices. We found that both modifications significantly
X improvedtheperformance.
Lðθ,ϕ,xÞ= qϕ ðzjxÞlogðpθ ðxjzÞÞ(cid:2)KLðqϕ ðzjxÞjjpθ ðzjxÞÞ ð3Þ WemeasuredthefitbetweenthegeneratedaffinitymatrixFand
z theneighborhoodgraphusingthenegativelog-likelihoodfunctionof
Weintroduceaconstrainttoshapetheinferredposteriorqϕ ðzjxÞ theBernoulli-Poissonmodel:
andmatchitwithapriorpθ ðzÞthatcontrolsthecapacityofthelatent X X
informationbottleneck.WesetthepriorasanisotropicunitGaussian, (cid:2)logpðAjFÞ= (cid:2) logð1(cid:2)expð(cid:2)F FTÞÞ+ F FT
u v u v ð8Þ
pðzÞ∼Nð0,IÞ.Theconstrainedoptimizationproblemcanbewrittenas: ðu,vÞ2E ðu,vÞ2=E
(cid:5) (cid:2) (cid:3)(cid:6) Here,Erepresentsthesetofedgesinthegraph.Sinceneighbor-
maxϕ,θ E
qϕðzjxÞ
log pθ ðxjzÞ s.t.KLðqϕ ðzjxÞjjpðzÞÞ<ϵ ð4Þ
hoodgraphsofsingle-celldataaretypicallysparse,thesecondtermin
Here,ϵisthestrengthoftheappliedconstraint.Withthisopti- the third sum contributes more to the loss. To balance these two
mizationbasedonMLE,thelatentvariablezcanreflectthecharacter terms, we adopted a standard technique known as balanced
ofthegroundtruthdatawithlowererror.Accordingtoβ-VAEmodel31,
classification18,anddefinedthelossfunctionasfollows:
wecanrewritetheprobleminLagrangianform: h (cid:7) (cid:7) (cid:8)(cid:8)i h i
(cid:5) (cid:2) (cid:3)(cid:6) (cid:7) (cid:7) (cid:8) (cid:8) LðFÞ= (cid:2)E ðu,vÞ∼PE log 1(cid:2)exp (cid:2)F u FT v +E ðu,vÞ∼PN F u FT v ð9Þ
Fðθ,ϕ,β,x,zÞ=E
qϕðzjxÞ
log pθ ðxjzÞ (cid:2)β KLðqϕ qϕ ðzjxÞjjpðzÞ (cid:2)ϵ
Here,P andP representuniformdistributionsoveredgesand
E N
ð5Þ non-edges,respectively.
InsteadofdirectlyoptimizingtheaffinitymatrixFasintraditional
whereβistheregularizationcoefficientoftheconstraint,whichlimits methods,wesearchfortheoptimalneuralnetworkparametersθ* to
thecapacityofzandimposesanimplicitpressureforindependencein minimizethe(balanced)negativelog-likelihoodfunction:
learningtheposteriordistributionduetotheisotropicnatureofthe (cid:2) (cid:3)
Gaussianpriorpθ ðzÞ.Inthismodel,differentvaluesofβcanalterthe θ*=argminθL GCNθ ðA,XÞ ð10Þ
leveloflearningpressureimposedduringtraining,encouragingthe
Through these steps, the BulkTrajBlend model computes over-
learning of different representations. We assume a disentangled
lapping communities in single-celldata, whichcan be used to infer
representationoftheconditionalindependentdatagenerativefactors
“omission”cellsintheoriginalsingle-celldata.Itcanhelprevealcell
vandthereforesetβ>1toapplyastrongerconstraintonthelatent
typetransitionsanddynamics,andmodelandanalyzecelldevelop-
variableinformationbottleneck,exceedingtheconstraintoftheori-
mentaltrajectories.
ginalVAE.Theseconstraintsrestrictthecapacityofzand,combined
withthepressuretomaximizethelog-likelihoodofthetrainingdatax,
Communitytrajectoryinference.Here,weinsertedtheoverlapping
encourage the model to learn the most efficient representation of
communitiesoftargetcellsintotheoriginalsingle-celldataandused
thedata.
PyVIAtoinferpseudo-temporaltrajectoriesofcelldifferentiation.For
detailed inference methods, please refer to the mathematical
Computationofsingle-cellneighborhoodgraph.Here,weusedthe
descriptionofPyVIA.Additionally,researcherscanalsouseCellRank
scanpy.pp.neighbors function from Scanpy to compute the cell
forcommunitytrajectoryre-inference.
neighborhood graph. For detailed mathematical description, please
refertotherelevantpapersanddocumentationofnearestneighbor
descentinScanpyandPyNNDescent62. CGANandACGANmodeldescription
CGAN(ConditionalGenerativeAdversarialNets)isaGAN(Generative
Communitydetectionandgenerationofoverlappingcellcommu- Adversarial Nets) based model that generates data by training the
nities.Weperformedcommunitydetectiononthecellneighborhood generatoranddiscriminatorwiththedataandcorrespondinglabels.
graphusingaGraphNeuralNetwork(GNN)modeltofindoverlapping Thetrainingprocesscanbesplitinto2parts.Inthefirstpart,latent
NatureCommunications|( 2024)1 5:5983 11
Article https://doi.org/10.1038/s41467-024-50194-3
variables z2RMðM=100Þ are generated by standardized normal the priority time with the neighborhood graph as the input of
distributionanditsgeneratedclasslabelsl areinputintothegen- “omicverse.utils.cal_paga”.
g
eratortogetthegenerateddata.Herethegeneratorcanbesummar- (5) The number of noise clusters, we used “scanpy.tl.leiden” in
izedasafunctiongθ,whereθaretheparametersoftheMLPandthere scanpytoperformunsupervisedclusteringonthegeneratedsingle-
are6layersinthateachlayerisnormalized.Thethehiddendimensions cellprofiles,withtheresolutionsetto1.0,andweidentifiedthecate-
are128*256*512*1024andtheactivationfunctionisLeakyRelu.After gories with less than 25 cells after clustering as noisy clusters and
gettingthegenerateddatag=gθ ðz,l
g
Þ,therewillbeadiscriminatordϕ, counted the number ofnoisy clustersasanassessmentofthe gen-
whereϕaretheparametersoftheMLPandthereare4layersineach erationquality.
layerthehiddendimensionis512,dropoutrateis0.4andtheactiva- (6) Density assessment of pseudotime, after we obtained the
tionfunctionisLeakyRelu,judgingwhethergaccordswithitslabell . pseudotime of single-cell profiles using pyVIA as the default para-
g
Therefore,inthesecondpart,dϕwillbetrainedbytherealdatarand meters,specificallysettingKto15intheneighborhoodgraphofthe
itslabell
r
withAdamoptimizertoimprovethejudgementlevelofdϕ. KNNandconfiguringuse_reptoX_pca.Weassessedthevarianceofthe
Then the lossof gθ judged bydϕ willbeemployedtoenhancethe pseudotimeoftargetinterpolatedcellsasoneofthemetricsforthe
generationabilityofgθwiththesameoptimizer.Thelossfunctionsfor assessmentofdevelopmentaltrajectoryreconstruction.
gθ anddϕ arebothMSElossandtheweightsofthelossofthegen-
erativedataandtherealdataareboth0.5. Datasets
Inaddition,ACGAN(AuxiliaryClassifierGAN),whichmakesthe Dentate Gyrus. Single-cell RNA-seq: Data from Hochgerner et al.65.
generativedatamoreauthentic,keepsthesamestructureofthegen- Dentategyrus(DG)ispartofthehippocampusinvolvedinlearning,
eratorastheoneintheCGAN,butitaddstheclassifierthatoffersthe episodicmemoryformationandspatialcoding.Theexperimentfrom
label of the input data on the output of the discriminator. In the thedevelopingDGcomprisestwotimepoints(P12andP35)measured
training process, the loss function for the added classifier is using droplet-based scRNA-seq (10x Genomics Chromium). The
CrossEntropy. dominatingstructureisthegranulecelllineage,inwhichneuroblasts
developintogranulecells.Simultaneously,theremainingpopulation
Datapre-processing formsdistinctcelltypesthatarefullydifferentiated(e.g.,Cajal-Retzius
Allsingle-celldatausedforBulkTrajBlendtrainingunderwentthesame cells)orcelltypesthatformasub-lineage(e.g.,GABAcells)(Accession
qualitycontrolsteps:Cellswithlowsequencingcounts(<1000)anda IDGSE95753).
highmitochondrialfraction(>0.2)wereexcludedinfurtheranalysis. BulkRNA-seq:DatafromCembrowskietal.66.Dentategyrus(DG)
Thefiltered countmatrixwas normalizedbydividing the countsof ismeasuredbyRNAsequencing(RNA-seq)toproduceaquantitative,
eachcellbytotalmoleculecountsdetectedinthatparticularcelland wholegenomeatlasofgeneexpressionforeveryexcitatoryneuronal
logarithmised with Python library scanpy63. All Bulk RNA-seq were classinthehippocampus;namely,granulecellsandmossycellsofthe
normalized using DEseq2 and “numpy.log1p” logarithmised using dentate gyrus, and pyramidal cells of areas CA3, CA2, and CA1
Python’sNumpy64package.ItisworthnotingthatbothBulkandsingle- (AccessionIDGSE74985).
celldatauserawcountsduringAEestimationofthecellfractionstate
space, whereas both Bulk and single-cell data use normalized and Pancreatic endocrinogenesis. Single-cell RNA-seq: Data from
logarithmiseddataduringtrainingofβ-VAE. Bastidas-Ponce et al.67. Pancreatic epithelial and Ngn3-Venus fusion
(NVF) cells during secondary transition with transcriptome profiles
Performanceevaluation sampledfromembryonicday15.5.Endocrinecellsarederivedfrom
To evaluated the generated and interpolation performance of our endocrineprogenitorslocatedinthepancreaticepithelium.Endocrine
model,acomprehensiveanalysiswasconducted,encompassingthe commitmentterminatesinfourmajorfates:glucagon-producingα-
examinationoffivecriticaldimensions: cells, insulin-producing β-cells, somatostatin-producing δ-cells and
(1)Thecountofinterpolatedcells,wecountedthenumberofcells ghrelin-producingε-cells(AccessionIDGSE132188).
thatwereeventuallyusedtointerpolateintotherawsingle-cellprofile. Bulk RNA-seq: Data from Bosch et al.68. RNA-sequencing was
(2) The correlation in marker gene expression between inter- performed of pancreatic islets (islets of Langerhans) from mice on
polatedandauthenticcells,wefirstusescanpy’s“scanpy.tl.rank_gen- PLX5622 or control diet for 5.5 or 8.5 months (Accession ID
es_groups”functiontocalculatethemarkergenesforeachtypeofcell GSE189434).
subpopulationintherawsingle-cellprofile(takingthetop200marker
genes).Then,weusethePearsoncoefficienttocalculatethepercen- Humanbonemarrow.Single-cellRNA-seq:DatafromSettyetal.69.The
tageofthese200markergenesintheexpressioncorrelationbetween bone marrow is the primary site of new blood cell production or
thegeneratedsingle-cellprofileandtherawsingle-cellprofile. haematopoiesis.Itiscomposedofhematopoieticcells,marrowadi-
(3) Marker gene similarity, we first used scanpy’s “scanpy.tl.- posetissue,andsupportivestromalcells.Thisdatasetservedtodetect
rank_genes_groups”functiontocalculatethemarkergenesforeach importantlandmarksofhematopoieticdifferentiation,toidentifykey
typeofcellsubpopulation(takingthefirst200markergenes)inthe transcriptionfactorsthatdrivelineagefatechoiceandtocloselytrack
rawsingle-cellprofileversusthegeneratedsingle-cellprofile,respec- when cells lose plasticity (https://data.humancellatlas.org/explore/
tively. Then, we treated marker genes as words and all the marker projects/091cf39b-01bc-42e5-9437-f419a66c8a45).
genes of each cell class as sentences, and used cosine similarity to BulkRNA-seq:DatafromMyersetal(2018).RNA-SeqofCD34+
calculatethesimilarityofmarkergenesofeachcellsubpopulation. Bone Marrow Progenitors from Healthy Donors (Accession ID
(4) Transition probabilities post-interpolation We firstwrapped GSE118944).
“omicverse.pp.scale” and “omicverse.pp.pca” in omicverse, “omic-
verse.utils.cal_paga”,andcomputedtheprincipalcomponentPCAof Maturation of murine liver. Single-cell RNA-seq: Data from Liang
thesingle-cellprofile.Wetookthefirst50principalcomponentsand etal.70.Atotalof52,834singlecelltranscriptomes,collectedfromthe
used the scanpy’s “scanpy.pp.neighbour” to compute the neighbor- newborntoadultlivers,wereanalyzed.Weobserveddramaticchanges
hoodmapofthesingle-cellprofile.Immediatelyafterthat,wecalcu- in cellular compositions during liver postnatal development. We
lated the developmental trajectory of single-cell profile with characterizedtheprocessofhepatocytesandsinusoidalendothelial
pseudotime using pyVIA, and we calculated the state transfer con- cellzonationestablishmentatsinglecellresolution.WeselectedPro-B,
fidenceforeachtypeofcellsubpopulationbytakingpseudotimeas Large Pre-B, SmallPre-B, B, HPC, GMP, iNP, imNP, mNP, Basophil,
NatureCommunications|( 2024)1 5:5983 12
Article https://doi.org/10.1038/s41467-024-50194-3
Monocyte,cDC1,cDC2,pDC,aDC,Kupffer,Proerythroblast,Erythro- fromGSE178318.Allprocesseddatainthismanuscriptareavailableat
blast, erythrocyte (Annotation could be found in metadata of Data https://github.com/Starlitnightly/omicverse-reproducibility.
fromLiangetal.)toperformedHPCdifferentiationanalysis(Accession
IDGSE171993). Codeavailability
Bulk RNA-seq: Data from Renaud et al.71. We analyze gene Thecodetoreproducetheexperimentsofthismanuscriptisavailable
expressionpatternsinthedevelopingmouseliverover12distincttime at https://github.com/Starlitnightly/omicverse-reproducibility. The
points from late embryonic stage (2 days before birth) to maturity OmicVerse package can be found on GitHub at https://github.com/
(60 days after birth). Three replicates per time point (Accession ID Starlitnightly/omicverseDocumentationandtutorialscanbefoundat
GSE58827). https://omicverse.readthedocs.io.
ConstructionofSimulated“omission”single-cellprofile References
To simulate the cell “omission” in single-cell sequencing, we con- 1. Kharchenko,P.V.Thetriumphsandlimitationsofcomputational
ductedcelldropoutexperimentsacrossdiversedatasets.InthePan- methodsforscRNA-seq.Nat.Methods18,723–732(2021).
creasdataset,weemployedLeidenclusteringandmanuallyexcluded 2. Peng,L.etal.Single-cellRNA-seqclustering:datasets,models,and
specificclustersofNgn3highEP,resultinginareductionofconfidence algorithms.RNABiol.17,765–783(2020).
in the transition from Ngn3 high EP to Pre-endocrine to 0. In the 3. Xu,X.,Hua,X.,Mo,H.,Hu,S.&Song,J.Single-cellRNAsequencing
Dentategyrus dataset, we applied Leiden clustering and manually toidentifycellularheterogeneityandtargetsincardiovascular
removed specific clusters of Granule Immature, leading to a con- diseases:frombenchtobedside.BasicRes.Cardiol.118,7(2023).
fidencereductioninthetransitionfromGranuleImmaturetoGranule 4. Derakhshan,T.,Boyce,J.A.&Dwyer,D.F.Definingmastcelldif-
Matureto0.Furthermore,intheBoneMarrowdataset,werandomly ferentiationandheterogeneitythroughsingle-celltranscriptomics
eliminated80%ofthecellsfromHSC-2,causingaconfidencedropin analysis.J.AllergyClin.Immunol.150,739–747https://doi.org/10.
thetransitionfromHSC-2toMonocyte-2to0. 1016/j.jaci.2022.08.011(2022).
ToemployBulkTrajBlendforgenerating“omission”cellsacross 5. Zeng,L.etal.Researchprogressofsingle-celltranscriptome
variousdatasets,wegeneratedsingle-celldatafromthebulkRNA-seq sequencinginautoimmunediseasesandautoinflammatorydis-
datausingBulkTrajBlendandfilteredoutnoisycellsusingthesizeof ease:areview.J.Autoimmun133,102919https://doi.org/10.1016/j.
the Leiden as a constraint. In configuring the model for different jaut.2022.102919(2022).
datasets,wesetthehyperparameter“cell_target_num”tobe1.5times,1 6. Thind,A.S.etal.DemystifyingemergingbulkRNA-Seqapplica-
time,and6timesthenumberofdropped-outcelltypes,aligningwith tions:theapplicationandutilityofbioinformaticmethodology.
Pancreas,Dentategyrus,andBoneMarrow,respectively.Subsequently, Brief.Bioinform.22,bbab259(2021).
BulkTrajBlendcalculatedtheoverlappingcelltypesinthegenerated 7. Liao,J.etal.DenovoanalysisofbulkRNA-seqdataatspatially
single-celldata,andweannotatedtheoverlappingcellcommunities. resolvedsingle-cellresolution.Nat.Commun.13,6498(2022).
Specifically,weselectedthesingle-celldatainwhichdropped-outcell 8. Love,M.I.,Huber,W.&Anders,S.Moderatedestimationoffold
typeswereassociatedwithadjacentcelltypes. changeanddispersionforRNA-seqdatawithDESeq2.GenomeBiol.
15,550(2014).
MethodsofOmicVerseintegration 9. Subramanian,A.etal.Genesetenrichmentanalysis:aknowledge-
WeunifiedthedownstreamanalysesofBulkRNA-seq,singlecellRNA- basedapproachforinterpretinggenome-wideexpressionprofiles.
seqinOmicVerse.Sincethedownstreamanalysesareindependentof ProcNatl.Acad.Sci.USA102,15545–15550https://doi.org/10.
theparameterevaluationofBulkTrajBlendandtheanalysismodulesof 1073/pnas.0506580102(2005).
eachpartareindependentofeachother,wehaveplacedthedatasets 10. Langfelder,P.&Horvath,S.WGCNA:anRpackageforweighted
andmethodsusedineachpartinSupplementary,anindexofwhichis correlationnetworkanalysis.BMCBioinformatics9,559(2008).
providedhere. 11. Hu,C.etal.CellMarker2.0:anupdateddatabaseofmanually
(1) Bulk RNA-seq: All datasets selected, parameter setting, and curatedcellmarkersinhuman/mouseandwebtoolsbasedon
methodscouldbefoundinSupplementaryNote4. scRNA-seqdata.NucleicAcidsRes.51,D870–D876(2023).
(2) scRNA-seq:Alldatasetsselected,parametersetting,andmethods 12. Efremova,M.,Vento-Tormo,M.,Teichmann,S.A.&Vento-Tormo,R.
couldbefoundinSupplementaryNote5. CellPhoneDB:inferringcell–cellcommunicationfromcombined
(3) Multi-omics:Alldatasetsselected,parametersetting,andmeth- expressionofmulti-subunitligand–receptorcomplexes.Nat.Pro-
odscouldbefoundinSupplementaryNote6. toc.15,1484–1506(2020).
13. Stassen,S.V.,Yip,G.G.K.,Wong,K.K.Y.,Ho,J.W.K.&Tsia,K.K.
Reportingsummary Generalizedandscalabletrajectoryinferenceinsingle-cellomics
Further information on research design is available in the Nature datawithVIA.Nat.Commun.12,5528(2021).
PortfolioReportingSummarylinkedtothisarticle. 14. Hsieh,C.-Y.etal.scDrug:fromsingle-cellRNA-seqtodrug
responseprediction.Comput.Struct.Biotechnol.J.21,150–157
Dataavailability https://doi.org/10.1016/j.csbj.2022.11.055(2022).
TheDentateGyrusdatausedinthisstudyhavebeendepositedinthe 15. Amezquita,R.A.etal.Orchestratingsingle-cellanalysiswithBio-
Gene Expression Omnibus (GEO) database under accession code conductor.Nat.Methods17,137–145(2020).
GSE95753andGSE74985,Datarelatedtopancreaticendocrinogenesis 16. Virshup,I.etal.TheScverseprojectprovidesacomputational
are accessible via accession codes GSE132188 and GSE189434, the ecosystemforsingle-cellomicsdataanalysis.Nat.Biotechnol.41,
maturationofmurineliverdatacanbefoundunderaccessioncode 604–606(2023).
GSE171993andGSE58827,Humanbonemarrowdataareavailablein 17. Giorgi,F.M.,Ceraolo,C.&Mercatelli,D.TheRLanguage:anengine
theHumanCellAtlas(HCA)databaseathttps://data.humancellatlas. forbioinformaticsanddatascience.Life(Basel)12,648https://doi.
org/explore/projects/091cf39b-01bc-42e5-9437-f419a66c8a45 and in org/10.3390/life12050648(2022).
theGEOdatabaseunderaccessioncodeGSE118944.TheAlzheimer’s 18. Brittain,J.,Cendon,M.,Nizzi,J.&Pleis,J.Datascientist’sanalysis
Disease snRNA-seq and snATAC-seq used in this study are available toolbox:comparisonofPython,R,andSASPerformance.SMUData
from GSE174367. The colorectal cancer scRNA-seq data is available Sci.Rev.1,7(2018).
NatureCommunications|( 2024)1 5:5983 13
Article https://doi.org/10.1038/s41467-024-50194-3
19. Wu,H.,Kirita,Y.,Donnelly,E.L.&Humphreys,B.D.Advantagesof 42. Fang,Z.,Liu,X.&Peltz,G.GSEApy:acomprehensivepackagefor
single-nucleusoversingle-cellRNAsequencingofadultkidney: performinggenesetenrichmentanalysisinPython.Bioinformatics
rarecelltypesandnovelcellstatesrevealedinfibrosis.J.Am.Soc. 39,btac757(2023).
Nephrol.30,23(2019). 43. Zhang,Y.etal.Single-cellRNAsequencingincancerresearch.J.
20. Mereu,E.etal.Benchmarkingsingle-cellRNA-sequencing Exp.Clin.CancerRes.40,81(2021).
protocolsforcellatlasprojects.Nat.Biotechnol.38,747–755 44. Mo,Z.etal.Single-celltranscriptomicsrevealstheroleof
(2020). Macrophage-Naıv̈ eCD4+Tcellinteractionintheimmunosuppres-
21. Denyer,T.&Timmermans,M.C.P.Craftingablueprintforsingle- sivemicroenvironmentofprimarylivercarcinoma.J.Transl.Med.
cellRNAsequencing.TrendsPlantSci.27,92–103(2022). 20,466(2022).
22. Gao,C.,Zhang,M.&Chen,L.Thecomparisonoftwosingle-cell 45. Agrawal,A.,Ali,A.,Boyd,S.&others.Minimum-distortionembed-
sequencingplatforms:BDrhapsodyand10xgenomicschromium. ding.FoundationsandTrends®inMachineLearning14,211–378.
Curr.Genomics21,602–609(2020). 46. Korsunsky,I.etal.Fast,sensitiveandaccurateintegrationofsingle-
23. Chen,Y.etal.Deepautoencoderforinterpretabletissue-adaptive celldatawithHarmony.Nat.Methods16,1289(2019).
deconvolutionandcell-type-specificgeneanalysis.Nat.Commun. 47. Hie,B.,Bryson,B.&Berger,B.Efficientintegrationofhetero-
13,6735(2022). geneoussingle-celltranscriptomesusingScanorama.Nat.Bio-
24. Chen,B.,Khodadoust,M.S.,Liu,C.L.,Newman,A.M.&Alizadeh,A. technol.37,685–691(2019).
A.ProfilingtumorinfiltratingimmunecellswithCIBERSORT.Cancer 48. Cao,Y.,Wang,X.&Peng,G.SCSA:acelltypeannotationtoolfor
Syst.Biol.MethodsProtocols,1711,243–259(2018). single-cellRNA-seqdata.Front.Genet.11,490(2020).
25. Fan,J.etal.MuSiC2:cell-typedeconvolutionformulti-condition 49. Zhang,X.etal.CellMarker:amanuallycuratedresourceofcell
bulkRNA-seqdata.Brief.Bioinforma.23,bbac430(2022). markersinhumanandmouse.NucleicAcidsRes.47,D721–D728
26. Steen,C.B.,Liu,C.L.,Alizadeh,A.A.&Newman,A.M.Profilingcell (2019).
typeabundanceandexpressioninbulktissueswithCIBERSORTx. 50. Yuan,H.etal.CancerSEA:acancersingle-cellstateatlas.Nucleic
StemCellTranscr.Netw.MethodsProtoc.2117,135–157(2020). AcidsRes.47,D900–D908(2019).
27. Jew,B.etal.Accurateestimationofcellcompositioninbulk 51. VandeSande,B.etal.AscalableSCENICworkflowforsingle-cell
expressionthroughrobustintegrationofsingle-cellinformation. generegulatorynetworkanalysis.Nat.Protoc.15,2247–2276
Nat.Commun.11,1971(2020). (2020).
28. Ahlmann-Eltze,C.&Huber,W.Comparisonoftransformationsfor 52. Persad,S.etal.SEACellsinferstranscriptionalandepigenomic
single-cellRNA-seqdata.Nat.Methods20,665–672(2023). cellularstatesfromsingle-cellgenomicsdata.NatBiotechnol41,
29. Frishberg,A.etal.Cellcompositionanalysisofbulkgenomicsusing 1746–1757(2023).
single-celldata.Nat.Methods16,327–332,https://doi.org/10.1038/ 53. Che,L.-H.etal.Asingle-cellatlasoflivermetastasesofcolorectal
s41592-019-0355-5(2019). cancerrevealsreprogrammingofthetumormicroenvironmentin
30. Wang,X.,Park,J.,Susztak,K.,Zhang,N.R.&Li,M.Bulktissuecell responsetopreoperativechemotherapy.CellDiscov.7,80(2021).
typedeconvolutionwithmulti-subjectsingle-cellexpression 54. AlMusawi,S.,Ahmed,M.&Nateri,A.S.Understandingcell-cell
reference.Nat.Commun.10,380(2019). communicationandsignalinginthecolorectalcancermicro-
31. Higgins,I.etal.beta-VAE:LearningBasicVisualConceptswitha environment.Clin.Transl.Med.11,e308(2021).
ConstrainedVariationalFramework.ICLR(Poster),3.(2017). 55. Han,J.M.&Jung,H.J.CyclophilinA/CD147interaction:apromising
32. Lotfollahi,M.,Wolf,F.A.&Theis,F.J.scGenpredictssingle-cell targetforanticancertherapy.Int.J.Mol.Sci.23,9341https://doi.
perturbationresponses.Nat.Methods16,715–721(2019). org/10.3390/ijms23169341.
33. Shchur,O.&Günnemann,S.Overlappingcommunitydetection 56. Scarzello,A.J.etal.LTβRsignallingpreferentiallyaccelerates
withgraphneuralnetworks.DeepLearningonGraphs,KDD. oncogenicAKT-initiatedlivertumours.Gut65,1765–1775,
https://doi.org/10.48550/arXiv.1909.12201(2019). https://doi.org/10.1136/gutjnl-2014-308810.
34. Mirza,M.&Osindero,S.Conditionalgenerativeadversarialnets. 57. Clark,S.J.etal.scNMT-seqenablesjointprofilingofchromatin
arXivpreprintarXiv:1411.1784(2014). accessibilityDNAmethylationandtranscriptioninsinglecells.Nat.
35. Odena,A.,Olah,C.&Shlens,J.inInternationalconferenceon Commun.9,781(2018).
machinelearning.2642-2651(PMLR). 58. Cao,Z.-J.&Gao,G.Multi-omicssingle-celldataintegrationand
36. Dimitrov,D.&Gu,Q.BingleSeq:auser-friendlyRpackageforbulk regulatoryinferencewithgraph-linkedembedding.NatureBio-
andsingle-cellRNA-Seqdataanalysis.PeerJ8,e10469,https://doi. technology40,1458–1466(2022).
org/10.7717/peerj.10469(2020). 59. Argelaguet,R.etal.MOFA+:astatisticalframeworkforcompre-
37. Flores,M.etal.Deeplearningtacklessingle-cellanalysis—asurvey hensiveintegrationofmulti-modalsingle-celldata.GenomeBiol.
ofdeeplearningforscRNA-seqanalysis.Brief.Bioinform.23, 21,1–17(2020).
bbab531(2022). 60. Morabito,S.etal.Single-nucleuschromatinaccessibilityand
38. Behdenna,A.etal.pyComBat,aPythontoolforbatcheffectscor- transcriptomiccharacterizationofAlzheimer’sdisease.Nat.Genet.
rectioninhigh-throughputmoleculardatausingempiricalBayes 53,1143(2021).
methods.bioRxiv,2020.2003.2017.995431,https://doi.org/10. 61. Song,D.etal.scDesign3generatesrealisticinsilicodataformul-
1101/2020.03.17.995431(2023). timodalsingle-cellandspatialomics.Nat.Biotechnol.https://doi.
39. Muzellec,B.,Telenczuk,M.,Cabeli,V.&Andreux,M.PyDESeq2:a org/10.1038/s41587-023-01772-1(2023).
pythonpackageforbulkRNA-seqdifferentialexpressionanalysis. 62. Dong,W.,Moses,C.&Li,K.Efficientk-nearestneighborgraph
bioRxiv,2022–2012. constructionforgenericsimilaritymeasures.InProceedingsof
40. Szklarczyk,D.etal.TheSTRINGdatabasein2021:customizable the20thinternationalconferenceonWorldwideweb.577–586
protein–proteinnetworks,andfunctionalcharacterizationofuser- (2011)
uploadedgene/measurementsets.NucleicAcidsRes.49, 63. Wolf,F.A.,Angerer,P.&Theis,F.J.SCANPY:large-scalesingle-cell
D605–D612(2021). geneexpressiondataanalysis.GenomeBiol.19,1–5(2018).
41. Langfelder,P.&Horvath,S.WGCNA:anRpackageforweighted 64. Harrisetal.ArrayprogrammingwithNumPy.Nature585,357–362
correlationnetworkanalysis.BMCBioinforma.9,1–13(2008). (2020).
NatureCommunications|( 2024)1 5:5983 14
Article https://doi.org/10.1038/s41467-024-50194-3
65. Hochgerner,H.,Zeisel,A.,Lönnerberg,P.&Linnarsson,S.Con- pyMOFAwasimplementedandtestedbyL.H.,Y.W.andZ.Z.P.L.handled
servedpropertiesofdentategyrusneurogenesisacrosspostnatal theimplementationandtestingofthemetacellsanalysisinSEACells.
developmentrevealedbysingle-cellRNAsequencing.Nat.Neu- B.T.wasresponsibleforwritingthemethodsforCGANandACGAN,as
rosci.21,290–299(2018). wellasreviewingthemethodsofBulkTrajBlend.H.D.,Y.X.andZ.Z.jointly
66. Cembrowski,M.S.,Wang,L.,Sugino,K.,Shields,B.C.&Spruston, conceived,implemented,andtestedthebulkRNA-seqpipeline.C.X.
N.Hipposeq:acomprehensiveRNA-seqdatabaseofgeneexpres- andY.X.providedtheconceptualizationoffalseoverlaprateforeva-
sioninhippocampalprincipalneurons.eLife5,e14997(2016). luationofBulkTrajBlend.Y.X.,H.D.,C.X.andZ.Z.providedsupervision
67. Bastidas-Ponce,A.etal.ComprehensivesinglecellmRNAprofiling andcontributedtotheconceptualizationoftheOmicVerseplatform.
revealsadetailedroadmapforpancreaticendocrinogenesis. ThemanuscriptwascollaborativelywrittenbyZ.Z.,Y.M.,L.H.,H.D.
Development146,dev173849(2019). andY.X.
68. Bosch,A.J.T.etal.CSF1RinhibitionwithPLX5622affectsmultiple
immunecellcompartmentsandinducestissue-specificmetabolic Competinginterests
effectsinleanmice.Diabetologia66,2292–2306(2023). Theauthorsdeclarenocompetinginterests.
69. Setty,M.etal.Characterizationofcellfateprobabilitiesinsingle-
celldatawithPalantir.Nat.Biotechnol.37,451–460(2019). Additionalinformation
70. Liang,Y.etal.Temporalanalysesofpostnatalliverdevelopment SupplementaryinformationTheonlineversioncontains
andmaturationbysingle-celltranscriptomics.Dev.Cell57, supplementarymaterialavailableat
398–414.e395(2022). https://doi.org/10.1038/s41467-024-50194-3.
71. Renaud,H.J.etal.Ontogenyofhepaticenergymetabolismgenes
inmiceasrevealedbyRNA-sequencing.PloSOne9,e104560 Correspondenceandrequestsformaterialsshouldbeaddressedto
(2014). ZehuaZeng,CencanXing,YuanyanXiongorHongwuDu.
Acknowledgements PeerreviewinformationNatureCommunicationsthanksRunminWei,
ThisworkwassupportedbythegrantsfromtheNationalNaturalScience andtheother,anonymous,reviewer(s)fortheircontributiontothepeer
FoundationofChina(32300682toC.X.),theNationalKeyResearch& reviewofthiswork.Apeerreviewfileisavailable.
DevelopmentalProgramofChina(92249303toY.X.),theFundamental
ResearchFundsfortheCentralUniversities(FRF-TP-22-007A1toC.X.), Reprintsandpermissionsinformationisavailableat
theStudentResearchTrainingProgram(SRTP)ofUniversityofScience http://www.nature.com/reprints
andTechnologyBeijing(202010008107toZ.Z.).WethankProfessorGe
GaoofPekingUniversityforhisguidanceontheOmicVerseopen-source Publisher’snoteSpringerNatureremainsneutralwithregardtojur-
copyrightinthesummerof2021.Wearegratefulfortheexperienceof isdictionalclaimsinpublishedmapsandinstitutionalaffiliations.
studyingepigenomicsintheXieLabatTsinghuaUniversity,andfor
XiaotongWu’sguidanceinenablingOmicVerse'smulti-omicsanalyses OpenAccessThisarticleislicensedunderaCreativeCommons
tobesuccessfullydesigned.WethankalltheGithubuserswhocon- Attribution4.0InternationalLicense,whichpermitsuse,sharing,
tributedcodeandissuetoOmicVerseovertheyears.Wewouldliketo adaptation,distributionandreproductioninanymediumorformat,as
thankthefollowingWeChatOfficialAccountsforpromotingOmicVerse: longasyougiveappropriatecredittotheoriginalauthor(s)andthe
pythonicbiologists,biotrainee.PythonicbiologistandBiotrainee’sarti- source,providealinktotheCreativeCommonslicence,andindicateif
cleinspiredsomeofthechartingintheOmicVerse. changesweremade.Theimagesorotherthirdpartymaterialinthis
articleareincludedinthearticle’sCreativeCommonslicence,unless
Authorcontributions indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnot
Z.Z.,Y.M.andL.H.contributedequallytothiswork.Z.Z.wasresponsible includedinthearticle’sCreativeCommonslicenceandyourintended
fordesigningtheOmicVerseapplicationprogramminginterfaceand useisnotpermittedbystatutoryregulationorexceedsthepermitted
designingthewholeBulkTrajBlendframework.Y.M.playedakeyrolein use,youwillneedtoobtainpermissiondirectlyfromthecopyright
designingandimplementingtheoverlapcellcommunityofBulkTraj- holder.Toviewacopyofthislicence,visithttp://creativecommons.org/
Blend,whileZ.Z.wasresponsibleforimplementingandconducting licenses/by/4.0/.
testingofthesingle-cellRNA-seqpipeline.L.H.conductedsimulated
single-cellprofiletestsforBulkTrajBlend.Themulti-omicsmoduleof ©TheAuthor(s)2024
NatureCommunications|( 2024)1 5:5983 15
