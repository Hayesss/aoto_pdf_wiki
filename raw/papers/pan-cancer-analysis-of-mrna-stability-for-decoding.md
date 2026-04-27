---
source_path: /mnt/c/Users/Administrator/Zotero/storage/S83CZWE8/Perron 等 - 2022 - Pan-cancer analysis of mRNA stability for decoding tumour post-transcriptional programs.pdf
ingested: 2026-04-23
sha256: 2a76bd8cf1c3dfdf
---

ARTICLE
https://doi.org/10.1038/s42003-022-03796-w OPEN
Pan-cancer analysis of mRNA stability for decoding
tumour post-transcriptional programs
Gabrielle Perron 1,2, Pouria Jandaghi2, Elham Moslemi2, Tamiko Nishimura2, Maryam Rajaee2,
✉
Rached Alkallas 1,2,3, Tianyuan Lu 1,2,4, Yasser Riazalhosseini 1,2 & Hamed S. Najafabadi 1,2
MeasuringmRNA decayin tumours isa prohibitive challenge, limitingourabilitytomapthe
post-transcriptional programs of cancer. Here, using a statistical framework to decouple
transcriptionalandpost-transcriptionaleffectsinRNA-seqdata,weuncoverthemRNAstability
changes that accompany tumour development and progression. Analysis of 7760 samples
across 18 cancer typessuggests that mRNA stability changes are ~30% as frequent as tran-
scriptional events, highlighting their widespread role in shaping the tumour transcriptome.
Dysregulationofprogramsassociatedwith>80RNA-bindingproteins(RBPs)andmicroRNAs
(miRNAs) drive these changes, including multi-cancer inactivation of RBFOX and miR-29
families. Phenotypic activation or inhibition of RBFOX1 highlights its role in calcium signaling
dysregulation,whilemodulationofmiR-29showsitsimpactonextracellularmatrixorganiza-
tionandstemness genes.Overall,our studyunderlinestheintegralroleofmRNAstabilityin
shaping the cancer transcriptome, and provides a resource for systematic interrogation of
cancer-associatedstabilitypathways.
1DepartmentofHumanGenetics,McGillUniversity,Montreal,QCH3A1B1,Canada.2McGillGenomeCentre,Montreal,QCH3A0G1,Canada.3Rosalind
andMorrisGoodmanCancerInstitute,Montreal,QCH3A1A3,Canada.4QuantitativeLifeSciencesProgram,McGillUniversity,Montreal,QCH3A1E3,
✉
Canada. email:hamed.najafabadi@mcgill.ca
COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio 1
;,:)(0987654321
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
W
idespread disruption of gene expression programs is a transcription and processing rate constants, whereas values
hallmark of cancer and underlies the extensive trans- smallerthan1indicatethatastranscriptionincreases,processing
formationoftumourcellidentityandbehavior.Among rateconstantdecreases,potentiallyduetosaturationoftheRNA
theleastunderstoodaspectsofthisgeneexpressionremodelingis processing machinery (Supplementary Fig. 1a). To use this
theregulationofmRNAstabilityanddecay.Previousstudieshave power-lawrelationshipfortheinferenceofdifferentialstability,it
found specific programs that are involved in tumourigenesis or is essentialto correctly model thevariability in RNA-seq counts.
metastasisthroughmodulationofmRNAstability1–8;however,the
For this purpose, we developed DiffRAC (https://github.com/
extent to which mRNA stability contributes to cancer cell tran- csglab/DiffRAC),aframeworkthatconvertstheunspliced-spliced
scriptome has notbeen systematicallystudied, and the associated relationship to a generalized linear model whose parameters can
regulatory networks are mostly unknown. A key limitation in thenbeinferredfromsequencingcountdatausinganappropriate
studying these post-transcriptional programs stems simply from error model of choice (Fig. 1b, c and Supplementary Fig. 1c, d).
ourlackofabilitytomeasuremRNAdecayrateinvivo:traditional We evaluated the performance of DiffRAC for estimating
methodsthatmeasuremRNAdecayrelyoninvitromanipulations differential mRNA stability using a previously published
such as transcriptional inhibition with chemical inhibitors (e.g. dataset18,19, consisting of RNA-seq data from mouse embryonic
actinomycin D) or metabolic labeling with nucleoside analogues stem cells and terminal neurons, along with experimentally
(e.g. 4-thiouridine), combined with time series measurements of measured transcript half-life measurements after transcriptional
transcripts9–11. Despite recent improvements12,13, these methods blockagewithactinomycinD,whichhereweconsideras“ground-
areresource-intensive,haveinherentlimitationsandbiasessuchas truth”measurementsforbenchmarkingpurposes.Weobservedan
triggering cellular stress and pleiotropic effects14, and, most overall Pearson correlation of 0.22 between RNA-seq-based
importantly,areonlyapplicabletoinvitromodels.Asaresult,the stability estimates from DiffRAC and ground-truth stability
mRNA stability landscape of tumour remains almost completely measurements (Fig.1d and Supplementary Data 1a), in line with
unchartedacrossdifferentcancertypes. previous reports on RNA stability estimation using this specific
A potential solution comes from recent studies showing that benchmarking dataset15,17. However, for transcripts that had
tissue RNA-seq data contain enough information to disentangle narrowconfidenceintervalsasestimatedbyDiffRAC,thePearson
transcription rate from mRNA decay rate. Briefly, under the correlation between RNA-seq-based estimates and ground truth
assumptionthatRNAprocessingrateisconstant15,16,anychange exceeded 0.5 (Fig. 1d–f), indicating that the confidence intervals
in unspliced (pre-mature) mRNA abundance (estimated from estimated by DiffRAC indeed reflect the true uncertainty in
intronic reads) must reflect a proportional change in transcrip- estimating differential mRNA stability. Based on (adjusted) P
tionrate,whileanychangeinspliced(mature)mRNAabundance values associated with DiffRAC differential stabilityestimates, we
(estimated from exonic reads) reflects the combined effect of identified 79 transcripts with higher stability in embryonic stem
transcriptionrateandmRNAdecay(Fig.1a).Thismodelenables cells and 37 transcripts with higher stability in terminally
the estimation of differential mRNA stability based on how the differentiated neurons (FDR<0.05), which closely correspond to
ratioofexonicandintronicreadschangesacrossconditions15.A differentiallystabletranscriptsbasedontheground-truth(Fig.1g).
recent improvement on this model generalizes the unspliced- WeperformedadditionalbenchmarkingusingRNA-seqdatafrom
splicedrelationshipasapower-lawfunction,withthepower-law NAT10-deficient HeLa cells with matched stability data from
exponent reflecting the coupling between transcription rate and metaboliclabeling-basedBRIC-seqmeasurements20.Usingsimilar
splicing rate17 (Supplementary Fig. 1a, b). analysismethodsasthosedescribedabove,weobservedthatRNA-
Here,webuildonthesemethodstoobtainapan-cancermapof seq-based DiffRAC estimates for transcripts with narrow con-
mRNA stability changes between tumour and normal tissues, as fidence intervals correlate with BRIC-seq stability measurements
well as the mRNA stability changes that accompany tumour (SupplementaryFig.2andSupplementaryData1b).Overall,these
progression.Todoso,wefirstintroduceageneralframeworkfor results suggest that DiffRAC can properly estimate not just the
statistical analysis of differential mRNA stability that takes into mean differential mRNA stability, but also its uncertainty and
account the distributional properties of count data. We bench- statisticalsignificance.
mark this method using experimental measurements of mRNA One limitation of the model described above is that, with
decay rate, and then apply it to the RNA-seq data from The increasing sample sizes, the number of latent variables that need
Cancer Genome Atlas (TCGA) to map the mRNA stability to be estimated by regression also increases, which can become
landscapes of 18 cancer types. We identify thousands of tran- prohibitively expensive in terms of computational times. To
scriptswhosestabilityisalteredduringtumourformationand/or overcomethechallengesassociatedwithfittingthemodelinlarge
progression––experimental measurements in cancer cell line sample cohorts, we developed a simplified DiffRAC model that
models support these findings and suggest a role for mRNA assumesmostofthevarianceintranscriptioncanbeexplainedby
stability alterations in tumour progression and invasiveness. the experimental variables (see Methods and Supplementary
Finally, using network modeling and functional experiments, we Fig. 3a–c). This assumption greatly reduces the number of
identify key microRNAs (miRNAs) and RNA-binding proteins parameters; however, we observed that it does not considerably
(RBPs) that mediate these changes, providing new insights into alter the differential stability estimates in the benchmarking
the post-transcriptional mechanisms of transcriptome remodel- dataset (Supplementary Fig. 3d).
ling in cancer.
DiffRAC identifies cancer-associated changes in mRNA stabi-
Results lity. To investigate the post-transcriptional changes responsible
A generalized linear model for statistical testing of mRNA for transcriptome remodeling in cancer, we performed a pan-
stability. The spliced and unspliced transcripts of each gene canceranalysisofdifferentialmRNAstabilityacrossTCGA(The
followapower-lawrelationship,withdeviationsfromthispower- CancerGenomeAtlas,availableathttps://www.cancer.gov/tcga.),
lawtrendreflectingchangesinthedegradationrateofthemature encompassing 7760 samples from 18 cancer types. We used
mRNA17 (Supplementary Fig. 1a, b). The power-law exponent DiffRAC to identify transcripts that were differentially stabilized
reflects the coupling between transcription rate and RNA pro- or destabilized in tumour compared to normal tissues in each
cessing rate–an exponent of 1 indicates no coupling between cancer type. This analysis revealed an average of 3954 mRNAs
2 COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio
a Condition 1 Condition 2 b Mean read count for gene i in sample j
Abundance for gene i in sample j
Gene-specific scaling factor
Spliced RNA Sample-specific scaling factor
Unspliced RNA Intronic λint = p i,j × l i × sint f m u R nc N ti A o n s t o a f b t i h li e ty c f o o n r d g i e ti n o e n i f ( a j) s a
- Slower transcription - Faster transcription
- Higher stability - Lower stability Exonic λexo= m × l'× sexo
i,j (Overall higher (Overall lower
c mRNA abundance) mRNA abundance) Bias term
that were differentially stabilized/destabilized per cancer type stabilityprofilesclusteredbyorganoforigin(Fig.2b),providingan
(FDR-adjustedp<0.05)(Fig.2a,b,SupplementaryFigs.4and5, internal validation for the robustness of stability inferences.
and Supplementary Data 2), suggesting widespread post- Secondly,weobservedthatpost-transcriptionallyderegulatedgenes
transcriptional remodeling in cancer, with the majority of tran- ineachcancertypearefunctionallyrelated(Fig.2d),consistentwith
scripts showing highly cancer-specific stability profiles (Fig. 2b). previously reported relationship between post-transcriptional
Interestingly, across TCGA samples, the degree of stability dys- regulons and functional gene modules21,22. This analysis also
regulation, calculated as the number of differentially stabilized highlights the role of mRNA stability in shaping the functional
mRNAs per patient, was associated with reduced disease-free landscape of the cancer cell. For example, epithelial-mesenchymal
survival (log hazard ratio of 0.36, P<0.005, using Cox transition genes and MYC targets are enriched among stabilized
proportional-hazardsmodelcorrectingfortheconfoundingeffect mRNAsacrossseveralcancertypes,whilemetabolicpathwayssuch
of patient age, sex, tumour purity and cancer type). Per-cancer- as oxidative phosphorylation and lipid metabolism are highly
type associations were also mostly positive (Fig. 2c), indicating enriched among destabilized mRNAs, most noticeably in cholan-
that a greater disruption of mRNA stability is overall associated giocarcinoma (CHOL), liverhepatocellular carcinoma (LIHC) and
with worse patient outcomes. head-neck squamous cell carcinoma (HNSC).
Several lines of evidence support the reliability of the stability Thirdly, we found that cancer-associated stability changes
profiles we have inferred. First, we observed that tumour mRNA inferred from tissue RNA-seq data are highly consistent with
naem
fo
rorre
dradnatS
0.1
2.0
+4
0
–4
–4 0 +4
Measured differential mRNA stability
(TN vs. ES)
ytilibats
laitnereffid
CARffiD
)SE
.sv
NT
fo
egnahc
dlof
gol( 2
d
r = 0.22
n=2707 genes
+4
+2
0
–2
–2 0 +2
ytilibats
laitnereffid
CARffiD
)egnahc
dlof
gol( 2
e
f
1
0
r = 0.52 r = –0.10
–2 0 +2 0.3
noitalerroc
nosraeP
)ytilibats
derusaem
.sv
CARffiD(
+2
0
–2
0.6 0.9 1.2
Measured differential mRNA stability DiffRAC standard error of mean
(TN vs. ES) (average for bins of 50 genes)
ytilibats
laitnereffid
derusaeM
i,j j
m = (p )b × γ
i,j i j i,j i,j i,f(j)
1 0 0 0 0 0
1 1 0 0 0 0
1 0 1 0 0 0
1 0 0 1 0 0 = + ×
1 0 0 0 1 0
1 b 0 0 1 0
1 0 b 0 1 1
1 0 0 b 1 1
g 0.01 < FDR ≤ 0.05
FDR ≤ 0.01
DiffRAC statistical
significance
decilpsnU
decilpS
1
2
3
4
1
2
3
4
j elpmaS
1
2
1
2
)j(f
noitidnoC
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
log(λint) ii,,j log(λeeexo)
ii,,j
log( sint )
j
log( sexo )
j
log( p ) + log( l ) i,1 i
log( p ) – log( p )
i,2 i,1
log( p ) – log( p ) i,3 i,1
log( p ) – log( p )
i,4 i,1 log( l ') – log( l ) + log( γ )
i i i,1 log( γ ) – log( γ )
i,2 i,1
Differential stability between
Design matrix conditions 1 and 2
Fig.1InferenceofdifferentialmRNAstabilityusingDiffRAC.aSchematicrepresentationoftheeffectoftranscriptionandstabilityontheabundancesof
unsplicedandsplicedRNA.bDiffRACmodelsthemean(λ)ofintronic(int)andexonic(exo)readdistributionasafunctionofpre-mature(p)andmature
(m)transcriptabundances,inadditiontogene-specific(l)andlibrary-specific(s)scalingfactors.MaturemRNAabundanceismodeledasafunctionofthe
pre-matureRNAabundanceandmRNAstability(γ),whichisinturnafunction(f)oftheexperimentalvariables.AlsoseeSupplementaryFig.1.cAn
examplecasewithfoursamplesandtwoexperimentalconditions,showinghowDiffRAC’smodelcanbeimplementedinaregressionwithalog-link
function,alongwiththeinterpretationofregressioncoefficients(alsoseeMethods).dComparisonofDiffRACstabilityestimatesagainstexperimental
mRNAhalf-life(stability)measurementsinmouseEScellsdifferentiatedtoterminalneurons(TN)15,18,19.Eachdatapointstandsforonegene,withthe
pointscolouredaccordingthestandarderrorofthemean(SEM)forDiffRACestimates.eComparisonofDiffRACestimatesvs.measuredmRNAstability
forthe100geneswiththesmallest(left)andlargest(right)DiffRACSEMs.Errorbarsrepresentthestandarderrorofthemean(SEM).fThePearson
correlationbetweenDiffRACestimatesandmeasuredmRNAstabilityforbinsof50genessortedbytheirSEM.gDistributionofexperimentalmRNAhalf-
lifemeasurementsforgenesthatDiffRAChasidentifiedassignificantlydestabilized(blueboxplots)orstabilized(redboxplots)inTNvs.EScells,atFDR
cutoffsof0.05(dashedline)or0.01(solidline).GenesthatarenotcalledassignificantbyDiffRACarerepresentedwiththegreyboxplot.
COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio 3
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
Fig.2Pan-canceranalysisofdifferentialmRNAstability.aVolcanoplotofdifferentialRNAstabilitybetweentumourandnormaltissues(Tvs.N)for18
TCGAcancertypes.SeeSupplementaryFig.4forvolcanoplotsofindividualcancertypes.bHeatmapofdifferentialmRNAstabilityprofilesacrossTCGA
cancers.GeneswithsignificantDiffRACresultsinatleastonecancer(FDR<0.05)areincluded.Thecolourgradientrepresentsacombinationofthelog
2
fold-changeofmRNAstabilityandtheFDR.BLCAbladderurothelialcarcinoma,BRCAbreastinvasivecarcinoma,CHOLcholangiocarcinoma,COADcolon
adenocarcinoma,ESCAesophagealcarcinoma,GBMglioblastomamultiforme,HNSCheadandnecksquamouscellcarcinoma,KICHkidneychromophobe,
KIRCkidneyrenalclearcellcarcinoma,KIRPkidneyrenalpapillarycellcarcinoma,LIHCliverhepatocellularcarcinoma,LUADlungadenocarcinoma,LUSC
lungsquamouscellcarcinoma,PRADprostateadenocarcinoma,READrectumadenocarcinoma,STADstomachadenocarcinoma,THCAthyroid
carcinoma,UCECuterinecorpusendometrialcarcinoma.cAssociationsbetweenthedegreeofdisruptionofmRNAstability,definedasahighorlow
numberofdifferentiallystabilizedtranscripts(relativetothemedian),anddisease-freesurvival,testedusingaCoxproportional-hazardsmodeland
correctingforpatientage,sexandtumourpurity.ThebarheightrepresentstheCoxregressioncoefficient,whilethecolourgradientrepresentsthep
values,withredrepresentingaworseprognosis,andbluerepresentingaprotectiveeffect.Theerrorbarsrepresentthestandarderrorofthemean(SEM).
dPathwayenrichmentanalysisofgeneswithsignificantdifferentialmRNAstabilityineachcancertype.CircleswithblackoutlinecorrespondtoMSigDB
hallmarkgenesetsthataresignificantlyenrichedamongcancer-stabilized(red)andcancer-destabilized(blue)mRNAs(FDR<0.05,Fisher’sexacttest).
Log-oddsandPvaluesarerepresentedusingthecolourgradientandcirclesizes,respectively.eVolcanoplotshowingtheexperimentallymeasured
differentialstabilitybetweenhighlymetastaticMDA-LM2celllinerelativetoitsparentalMDA-MB-231line(seeMethods).fGenesetenrichmentanalysis
(GSEA)(Subramanianetal.,2005)forhighlymetastaticrelativetopoorlymetastaticPDXmodelsofbreastcancer24–26.Genes(x-axis)aresortedby
WaldteststatisticofdifferentialstabilitybetweenmetastaticandprimaryPDXs.Theredlinerepresentstheenrichmentcurveforthetranscriptsthatwere
stabilizedinMDA-LM2relativetoMDA-MB-231,whilethebluelinerepresentstheenrichmentcurveforthedestabilizedtranscripts.gRelativeenrichment
oftranscriptsthatwerestabilized(red)ordestabilized(blue)inTCGA-BRCAtumourscomparedtonormalsamples,overlaidonthevolcanoplotfrom(e).
KerneldensityestimationwasusedtocalculatethedensityofBRCA-stabilizedanddestabilizedmRNAsacrosstheplot,withthedifferencebetweenthe
estimateddensitiesofthetwogroupsshownusingthecolourgradient.hVenndiagramsillustratingtheoverlapbetweentranscriptsthataresignificantly
stabilizedinBRCAtumours(relativetonormal)andMDA-LM2(relativetoMDA-MB-231),andgenesthatarepartofthemTORC1signalling(top)orMYC
targets(bottom).PvaluesarebasedonFisher’sexacttest.iTranscriptioninhibitiontime-coursegraphsfortwoexamplegenes,oneinvolvedin
mTORC1signaling(RAB1A)andoneamongMYCtargets(ODC1).They-axisshowsmRNAabundanceafterapplyingvariance-stabilizedtransformationand
correctingformRNAabundancedifferencesbetweenthetwocelllinesattimezero.Time-coursemeasurementsinMDA-LM2andparentalMDA-MB-231
cellsareshowninredandblue,respectively,withtheslopeofeachfittedlinerepresentingtherateofdegradation.
experimentally measured mRNA stability changes in cancer measurements) are also overall more stable in the highly
celllinemodels.Specifically,weusedtime-seriesmeasurementsof metastaticPDXscomparedtothepoorlymetastaticPDX(based
4-thiouridine-labeled RNA23 from the MDA-MB-231 cell line, a onDiffRACanalysisoftissueRNA-seqdata).Similarly,mRNAs
modelofbreastcancer,aswellasthehighlyinvasiveMDA-LM2 that are less stable in the MDA-LM2 cell line are overall less
cells to identify mRNAs that are differentially stable between stable in the poorly metastatic PDX (Fig. 2f; measurements are
these two cell lines (Fig. 2e, see Methods for details; measure- provided in Supplementary Data 3b).
ments are provided in Supplementary Data 3a). We then Interestingly,wefoundthatthemRNAsthataremorestablein
compared these experimental stability measurements to RNA- primary breast tumours compared to normal tissue (based on
seq-based differential stability estimates between highly meta- DiffRACanalysisofTCGAdata)arealsooverallmorestableinthe
static and poorly metastatic PDX models of breast
cancer24–26.
highlyinvasiveLM2linecomparedtotheparentalMDAline,and
We observed that the mRNAs that are more stable in the tumour-destabilizedmRNAsareoveralllessstableintheLM2line
invasive MDA-LM2 cell line (based on experimental stability (Fig. 2g). This concordance can also be observed at the pathway
4 COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
level: two of the three pathways that were upregulated in breast bindingtoeachtranscript(seeMethods).Figure4ashowsanexample,
tumours based on DiffRAC estimates also appear to be enriched wherethebindingtargetsoftheRBFOX1proteinareenrichedamong
among mRNAs that are stabilized in MDA-LM2 compared to transcripts that are destabilized in glioblastoma multiforme (GBM),
MDA-MB-231 cell lines (MYC targets and mTORC1 signaling, relative to the binding targets of other RBPs. We can quantify this
Fig.2h;examplegenesareshowninFig.2i),supportinga roleof enrichment by statistical modeling of the relationship between the
mRNAstabilityinderegulationofthesekeypathways. binding of a specific RBP to the 3ʹ UTR of a transcript and the
SincetheMDA-LM2lineismoreinvasivethanMDA-MB-231, tumour-specific stability status of that transcript (Fig. 4b). We per-
theaboveanalysissuggeststhat,atleastinbreastcancer,normal- formedasystematicquantificationoftheserelationshipsfor35RBPs
to-tumour stability changes persist during the progression of the whose stability target sets (regulons) have been previously mapped
disease to metastasis. To understand whether normal-to-tumour basedonthepresenceoftheirpreferredbindingsequencesinthe3ʹ
stability changes are correlated with progression-associated UTRsaswellastheexpressionpatternofthecandidatetargetgenes28.
stabilitychangesacrossothercancers,weusedDiffRACtoexamine Thisanalysisrevealedsignificantlyenrichedregulonsamongtumour-
the effect of tumour stage and grade on mRNA stability in each stabilized or destabilized mRNAs across different cancer types,
TCGA cancer type, by including stage/grade (as numerical representing deregulation of 17 out of the 35 examined RBPs in at
variables) in DiffRAC’s GLM design while controlling for the least one cancer type (Fig. 4c). Importantly, we observed excellent
confoundingeffectsofage,sexandtumourpurity(Supplementary agreement between cancer-associated RBP expression changes and
Data4).Thedifferentialstabilityresultsthereforereflectthechange RBP target enrichments, after taking into account the expected
in stability that occurs as tumour stage or grade increases. We functionofeachRBPinstabilizingordestabilizingitstargets(Pearson
identified a total of 1966 transcripts with significant stability correlation 0.61; Fig. 4d). For example, SNRPA, which is an RNA-
changes associated with tumour stage in at least one of the 11 destabilizing factor28, is upregulated in multiple cancers, consistent
cancerstypesthatweanalysed(SupplementaryData5a),and2013 withtheobserveddestabilizationofitsregulon(Fig.4c,d).Thisstrong
transcriptswhosestabilitywasassociatedwithtumourgradeinat correlationhighlightsthereliabilityofourregulonanalysisapproach
least one of the four cancer types for which this type of for identifying dysregulated RBPs, and suggests that aberrant
classificationwas available (Supplementary Data 6). We observed expressionofRBPsincancerdrivescoordinatedchangesinthesta-
highly cancer-specific associations both for stage and grade bilityoftheirregulons.
(Fig.3a).Importantly,wefoundthatinmostcasesthestage-and AmongtheRBPsweanalysed,twoRBPs,namelyRBFOX1and
grade-associatedstabilitychangescorrelatewithnormal-to-tumour RBFOX3,standoutasbeingconsistentlyderegulatedacrossseveral
stabilitychanges(Fig.3bshowsanexample,withtheoverallresults cancer types. Specifically, the targets of these RBPs are enriched
summarizedinFig.3c). amongdestabilizedmRNAsinalmosthalfofallthecancertypeswe
We note that disease progression is often accompanied by analysed(Fig.4c).ConsistentwiththeroleofRBFOXproteinsin
substantial cell composition changes, which may confound the promoting mRNA stability28,31, both RBFOX1 and RBFOX3 are
estimation of stage/grade-associated stability changes from bulk downregulatedacrossmultiplecancers(Fig.5a,b),suggestingthat
RNA-seq data. However, previous research has shown that cell downregulationofRBFOXproteinsleadstodestabilizationoftheir
type-specificgeneexpressionchangescanbeidentifiedfrombulk targets.ForbothRBFOX1andRBFOX3,thehighestexpressionin
RNA-seq data27. We implemented a similar design using normal tissues can be seen in the brain tissue; subsequently, the
DiffRAC to deconvolve the stage-associated stability changes mostprominent caseof their downregulation aswell as the most
occurringspecificallyinthemalignantcellsfromthoseoccurring significantchangesinthestabilityoftheirregulonscanbeseenin
inthetumourmicroenvironment, aswellaschanges thatsimply GBM, suggesting a major role in determining tumour transcrip-
reflect cell composition differences (Fig. 3d, see Methods for tome in this cancer type. However, their effect is not limited to
details). We identified 275 genes whose stage-associated mRNA GBM, especially for RBFOX3, which shows a broader range of
stability changes were confidently attributed to dysregulation in expressioninnormaltissuesandisalsodownregulatedinagreater
malignant cells (Fig. 3e and Supplementary Data 5b). With the numberofcancers(Fig.5b).
exception of one cancer type, the stage-associated stability To confirm that the downregulation of RBFOX proteins
changes inferred from the tumour bulk were better correlated accompanies destabilization of their direct binding targets in
with the deconvoluted changes attributed to malignant cells cancer,weusedHITS-CLIPdataofRbfoxproteinsinwholebrain
compared to those of tumour microenvironment (Fig. 3f, g). tissuelysateofmice32tobuildahigh-confidencestabilitynetwork
Stage-associated changes that could be attributed to malignant oftranscriptsthathavethestrongestbindingsitesintheir3ʹUTRs
cells were also positively correlated with tumour-to-normal (seeMethods).WeconfirmedthatRBFOXbindingsitesidentified
changes in most cancer types (Fig. 3h). Taken together, these frommouseHITS-CLIPdataareconservedinhuman(Fig.5c),and
resultshighlightwidespreadmRNAstabilitychangesintumours, observed overall destabilization of the associated targets across
which affect key cancer-related pathways and continue to differentcancers(Fig.5d).WenoticedasubsetofmRNAsthatare
remodeling of the transcriptome in malignant cells through consistently destabilized across the same cancers in which either
disease progression. RBFOX1 or RBFOX3 is downregulated (Fig. 5d). Interestingly, a
subgroupofthesemRNAsisstabilizedinthefewcancertypesin
which RBFOX1 is upregulated (e.g. genes with positive mRNA
RNA-binding proteins play a key role in shaping the tumour stability values for LUSC, LUAD and THCA in Fig. 5d), further
mRNAstabilityprofile.RNA-bindingproteins(RBPs)andmicro- supportingthenotionthattheircancer-associatedstabilitychanges
RNAs (miRNAs) are the key regulators of mRNA stability. These aredrivenbyRBFOXproteins.
sequence-specific factors primarily affect RNA stability through To verify that the stability of these mRNAs is regulated by
binding to the 3ʹ untranslated region (UTR) of their targets–RBPs RBFOX1, we examined the RNA-seq data from differentiated
eitherstabilizeordestabilizetheirtargets28,whilemiRNAsprimarily primaryhumanneuralprogenitor(PHNP)cellsinwhichRBFOX1
destabilizetheirtargetmRNAs29,30.StartingwithRBPs,wesetoutto is knocked down33,34. As expected, cancer-destabilized mRNAs
examinewhetherthesefactorsunderliethemRNAstabilitychangesin thatwereassociatedwithRBFOX1werealsodownregulatedupon
cancer.Wespecificallytestedfortheenrichmentofthetargetsofeach RBFOX1 knockdown (Supplementary Data 7a and Fig. 5e). In
RBPamongmRNAsthataredifferentiallystablebetweentumourand contrast,whenRBFOX1expressionisrestoredectopicallyinmouse
normaltissues,aftercorrectingforthebackgroundfrequencyofRBP neuronslackingRBFOXproteins31,35,theexpressionofthesegenes
COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio 5
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
Fig.3Stage-andgrade-associatedmRNAstabilitychanges.aThemRNAstabilitychangesassociatedwithtumourstage(left)andgrade(right)across
TCGAcancers.GeneswithsignificantchangesinatleastonecanceratFDR<0.05areincluded.ThecolourgradientisthesameasinFig.2b.
bComparisonofthedifferentialmRNAstabilitybetweentumourandnormal(x-axis)andstage-associateddifferentialmRNAstability(y-axis),inthe
TCGA-LIHCdatasetasanexample.GeneswithsignificantchangesalongbothaxesatFDR<0.05arecolouredinblue.Pearsoncorrelationcoefficientsand
confidenceintervalsforallgenes(black)andsignificantones(blue)areshownontop.Panel(c)summarizesthePearsoncorrelationsforsignificantgenes
inothercancertypes(errorbarsrepresenttheconfidenceintervals).dSchematicillustrationofthemodelusedfordeconvolvingthestage-associated
changesinmalignantandnon-malignantcells.Theequationontoprepresentsthemodelused,withtheinterpretationofmodelcoefficientsshownonthe
plot.SeeMethodsfordetails.eStabilitychangesassociatedwithtumourstageacrossTCGAcancersthatcouldbeassignedtocancerous/pre-cancerous
cells.GeneswithsignificantDiffRACresultsinatleastonecancer(FDR<0.05)areincluded.ThecolourgradientisthesameasinFig.2b,withthe
exceptionthatthelog fold-changeofmRNAstabilityrangesfrom−1to1here.fComparisonofthestage-associateddifferentialmRNAstabilityinnon-
2
cancerouscells(x-axis,left)orcancerous/pre-cancerouscells(x-axis,right)tothenon-deconvolutedestimates(y-axis)intheTCGA-KIRCdataset.
Pearsoncorrelationcoefficientsandpvaluesareshownontheplot.Panel(g)showsthisPearsoncorrelationsacrossallcancertypesfornon-cancerous
(gray)andcancerous/pre-cancerouscells(red).Errorbarsrepresentthe95%confidenceintervals.hThePearsoncorrelationbetweentumourvs.normal
(T/N)differentialstabilityandthedeconvolutedstage-associateddifferentialmRNAstability.Onlycancertypeswithatleast5significantdeconvoluted
stage-associatedgenesareshown.Errorbarsrepresentthe95%confidenceintervals.
isalsorescued(Fig.5f).Weidentifiedacoresetofeighttranscripts Finally, to validate the role of RBFOX1 downregulation in
that have RBFOX binding site in their 3ʹ UTRs, are concurrently mediating mRNA stability changes in human glioblastoma cells
destabilizedacrosscancers,areinhibitedwhenRBFOX1isknocked and toinvestigate whetherrestoring RBFOX1activity canrescue
down, and are upregulated when RBFOX1 expression is rescued the destabilization of its target transcripts, we overexpressed
(Fig. 5g). Interestingly, half of these genes belong to the calcium RBFOX1 in the human glioblastoma cell line A172 (Supplemen-
signalingpathway(basedonKEGGpathways36,Fisher’sexacttest tary Fig. 6) and performed RNA-seq. As expected, we observed
P<10
−6),
suggesting that deregulation of RBFOX proteins widespread changes in gene expression (Fig. 5h and Supplemen-
primarilyaffectscalciumsignalingincancercells. tary Data 7b), with overall upregulation of the RBFOX1 regulon
6 COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
Fig.4EnrichmentofRBPbindingsitesamongdifferentiallystabilizedmRNAsincancer.aAnexamplecaseshowingtheenrichmentofRBFOX1binding
sitesamongdifferentiallystabilizedmRNAsinTCGA-GBM.GenesarebinnedbyFDRoftheirDiffRACdifferentialmRNAstabilitybetweentumourand
normal,withdestabilizedmRNAsontheleftandstabilizedmRNAsontheright.TherelativefrequencyofRBFOX1targets(circles)andtargetsofallother
RBPs(solidline)isshownforeachbin.bSchematicrepresentationofthelogisticregressionapproachformodelingtheenrichmentofRBFOX1targets
(relativetootherRBPs)asafunctionofdifferentialstability.cHeatmapsummarizingtheresultsofapplyingthemodelinpanel(b)toallRBPs.Positive
(red)andnegative(blue)regressioncoefficientsindicateenrichmentofRBPtargetsamongmRNAsthatarestabilizedanddestabilizedincancer,
respectively.Thecirclesizerepresentsthesignificancelevel.SignificantassociationsbetweenRBPbindingandstabilitystatusareshownusingblack
outlines(FDR<0.05).dComparisonofthedifferentialRBPexpression(tumourvsnormal)andcancer-associatedregulonactivity.Regulonactivityis
definedtobethesameastheenrichmentcoefficientsfrompanel(c),withthesignofthecoefficientinvertedforRBPswhosebindingleadstoRNA
destabilization(basedonref.28).EachdotrepresentsoneRBPinonecancertype.RBFOX1regulonactivitiesarehighlighted.Pearsoncorrelationof
differentialexpressionvs.differentialregulonactivityis0.61.
intheRBFOX1-overexpressingA172cellline(Fig.5i).Consistent cholangiocarcinoma, and acts as a tumour suppressor via sup-
with the pathway analysis described above, we observed pressionofcellproliferationandinductionofapoptosis38,39.As
significantupregulationofcalciumsignalingpathwaygenesafter expected, our regulon analysis indicates that miR-122 targets
RBFOX1 overexpression (Fig. 5j). Furthermore, the majority of are predominantly stabilized specifically incholangiocarcinoma
pan-cancer destabilized mRNAs that are bound by RBFOX1 are tumours compared to normal tissue (Fig. 6a), consistent with
upregulatedinA172cellsafterRBFOX1overexpression(Fig.5k). reducedactivityofmiR-122.Thisobservationisconsistentwith
These results suggest that RBFOX1 downregulation in glioblas- TCGA miRNA expression data, which show specific down-
tomacellsleadstodestabilizationofitstargets,includingcalcium regulation of miR-122 expression in cholangiocarcinoma
signalingpathwaysgenes,whichcanbepartiallyrescuedthrough (Supplementary Fig. 7). Systematic application of this network-
RBFOX1 overexpression. based approach revealed that, out of 153 broadly conserved
miRNAfamilies,theregulonsof63miRNAs arederegulatedin
Dysregulation of miRNA regulons shapes the cancer tran- at least one cancer type, suggesting widespread disruption of
scriptome. To examine the contribution of miRNAs to the miRNA networks (Fig. 6b).
dysregulation of mRNA stability in cancer, we systematically Of interest, we observed that miR-29 targets are recurrently
searched for miRNAs whose targets are disproportionately stabilized across more than half of the cancer types we analysed,
dysregulated at the stability level in cancer, similar to the RBP suggesting a pan-cancer decrease in miR-29 activity. Among these
analysis above (Methods). Figure 6a shows miR-122 as an cancer types, the miR-29 regulon showed the most significant
example; miR-122 is the most abundant miRNA expressed enrichmentamongstabilizedmRNAsinUCECandKIRC(clearcell
in liver cells37, was previously shown to be downregulated in renalcellcarcinoma),suggestingamajorroleinpost-transcriptional
COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio 7
remodeling in these cancer types. To understand whether restoring binding site in their 3ʹ UTRs. Conversely, miR-29 inhibition in the
miR-29 activity can reverse these post-transcriptional changes, we ACHNcellline(alsoamodelforKIRC)reversedthesepatterns,with
expressed a miR-29 mimic in 786-O and A-498 cells, which are aglobalupregulationofmiR-29targets(SupplementaryFig.10and
modelsforKIRC(SupplementaryFig.8).Asexpected,expressionof Supplementary Data 8c), and upregulation of transcripts that are
miR-29 mimic resulted in global downregulation of the miR-29 stabilized in KIRC and potentially targeted by miR-29 (Fig. 6e).
regulon(Fig.6c,SupplementaryFig.9a,andSupplementaryData8a, Together, these results suggest that miR-29 downregulation has a
b).Importantly,miR-29mimicexpressionleadstodownregulationof widespread effect on the stability of transcripts in cancer, while
the majority of mRNAs that are significantly stabilized in KIRC restoring its activity partially rescues the normal mRNA stability
(Fig.6dandSupplementaryFig.9b),mostofwhichhavea miR-29 landscapeofthecell.
MBG ACLB DAER ACSE DATS DAOC CECU HCIK DARP CSNH CRIK PRIK ACRB CHIL ACHT DAUL CSUL
10
5
ecnadnuba
1XOFBR
skaep
3/2/1xofbR
fo seugolohtro
namuH
0
10
5
ecnadnuba
3XOFBR
+3
0
–3
–6
0
)N
.sv
T(
egnahc-dlof
2goL
+3
0
–3
–6
)N
.sv
T( egnahc-dlof
2goL
a
Sequence
b
RBFOX1 motif (RNAcompete)
MBG ACLB DAER ACSE DATS DAOC CECU HCIK DARP CSNH CRIK PRIK ACRB CHIL ACHT DAUL CSUL
srecnac
ssorca
dezilibatseD
P < 0.0006 citsitats
tseT
lrtC
.sv
DK
1XOFBR
+20
0
–20
12837 genes
P < 0.001
citsitats
tseT
lrtC
.sv eucser
1XOFBR
+5
0
–5
13134 genes
erocs
tnemhcirnE
0
–0.2
–0.4
–0.6
erocs
tnemhcirnE
d Log2 fold change (T vs. N) e
–2 0 +2
f 0.6
0.4 0.2
0
g
Leading-edge genes
down-regulated by RBFOX1 KD
9 SNAP25
CPLX2 FUT9
SHANK1 8 CAMK2A
CAMK4 Calcium
2 P AT R P K 2 C B B 2 s p i a g t n h a w li a n y g
Leading-edge genes
up-regulated by RBFOX1 rescue
stiB 1
0
stiB
c
1 2 3 4 5 6 7
1
0
+10
+5
0
–5
–10
egnahc
dlof
2goL
)lortnoc
.sv
EO
1XOFBR(
n = 2203
n = 1601
1 10–100 10–200 10–300
P-value
x
P < 0.00005
erocs
tnemhcirnE
+10 Calcium signaling pathway
0.6
+5 0.4
0.2
0 0
–5
–10
3855 genes
egnahc
dlof
2goL
)lortnoc
.sv
EO
1XOFBR(
P < 0.007
erocs
tnemhcirnE
+10 RBFOX1 direct targets
0.6
+5 0.4
0.2
0 0
–5
–10
9889 genes
egnahc
dlof
2goL
)lortnoc
.sv
EO
1XOFBR(
4PCP 1LCRAPS 2B2PTA 2XLPC A6MPG 1NTR A5FIK 5GCS 1N2KMAC C5FIK 4KMAC B6BAR RXTPN 1NTNC 1KNAHS A2KMAC 1TYS
******
+6
+4
*** ***
+2
* *****
0
***
egnahc
dlof
2goL
)lortnoc
.sv
EO
1XOFBR(
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
h i j k
***FDR < 0.0005
**FDR < 0.005
*FDR < 0.05
Fig.5AberrantactivityofRBFOXproteinsmediatesstabilitychangesacrossmultiplecancers.aRBFOX1expressionacrossTCGAcancertypes.Thebox
plot(top)showstheRBFOX1log (RSEM)geneexpression,retrievedfromFirebrowse(http://firebrowse.org/),innormaltissuesamples.Thebarplot
2
(bottom)illustratestheaveragelogfold-changeofRBFOX1expressionintumourscomparedtonormalsamples(Tvs.N;errorbarsrepresentSEM).
bRBFOX3expressioninnormaltissuesamplesanddifferentialexpressionintumours,similartopanela.cConservationofmouseRBFOX1bindingsitesin
humansforhigh-confidenceRbfoxHITS-CLIPtargets32.TheheatmapshowsthesequencesofhumanorthologsofthemouseRbfoxbindingsites(Rbfox
motifhitsonthemousesequenceswereidentified,andtheorthologousregionswereextractedusingliftOver69.Theconsensussequencefromthehuman
orthologsisshownunderneaththeheatmap.TheRBFOX1motiffromRNAcompete28isalsoshownatthebottom.dHeatmapshowingthestabilityof
RBFOXHITS-CLIPtargets(asdefinedabove).Rowscorrespondtogenesandcolumnstocancertypes,withthelattersortedinthesameorderaspanels
(a,b).eGenesetenrichmentanalysis(GSEA)70forRBFOX1inhibitioninterminallydifferentiatedneurons.Genes(x-axis)aresortedbytheWaldtest
statisticofdifferentialexpressionbetweenRBFOX1knockdown(KD)andcontrol(Ctrl)cells,withverticalblacklinesdemarcatingthepan-cancer-
destabilizedsetofRBFOX1targets.Thebluelinerepresentstheenrichmentcurveforthisgeneset70.fGSEAforRBFOX1rescueinmouseneuronsdeficient
forRBFOXproteins,similartopanel(e).gVenndiagramillustratingtheoverlapbetweentheleading-edge70setofgenesdownregulatedbyRBFOX1
knockdown(frome)andtheleading-edgesetofgenesupregulatedbyRBFOX1rescue(fromf).hVolcanoplotofdifferentialgeneexpressioninRBFOX1-
overexpressing(OE)A172cells.iGenesetenrichmentanalysis(GSEA)(Subramanianetal.,2005)forRBFOX1overexpression(OE)intheA172human
glioblastomacellline.Genes(x-axis)aresortedbythelog foldchangeofdifferentialmRNAstabilitybetweenRBFOX1overexpressingandcontrolcells.
2
ThebluelinerepresentstheenrichmentcurveforRBFOX1directtargets.jSimilartopaneli,withthebluelinerepresentingtheenrichmentcurveforgenes
involvedinthecalciumsignallingpathway.kDifferentialgeneexpressioninRBFOX1-overexpressingA172cells(n=3biologicalreplicates)relativeto
controls(n=3biologicalreplicates),shownforpan-cancerdestabilizedmRNAsthatareboundbyRBFOX1(frompaneld).ErrorbarsrepresenttheSEM.
8 COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
Fig.6DysregulationofmiRNAregulonsincancer.aAnexamplecaseshowingtheenrichmentofmiR-122targetsamongmRNAsstabilizedinTCGA-
CHOLtumours(relativetonormal),similartoFig.4a.NotethatsincemiRNAsareexpectedtodestabilizetheirtargets,enrichmentindifferentiallystable
mRNAsindicatesdownregulationofmiRNAactivity.bHeatmapsummarizingenrichmentanalysisforallmiRNAsacrossallcancertypes,similartoFig.4c.
cEnrichmentofmiR-29targetsamonggenesthataredownregulatedaftertransfectionofmiR-29mimicin786-Ocells(n=1)relativetocontrol(n=1).
Thevolcanoplot(bottom)summarizesdifferentialexpressionresultsbetweenmiR-29mimicandcontrol;thedotplotatthetopshowsenrichmentofmiR-
29targetsatbinsofdifferentiallyexpressedgenes,similartopanel(a).Inthevolcanoplot,significantlydifferentiallyexpressedgenes(FDR<0.05)are
showninred.dEnrichmentofmiR-29bindingsites,relativetoothermiRNAbindingsites,ingenescategoriesdefinedbytheirdifferentialmRNAstabilityin
TCGA-KIRCanddifferentialexpressionaftermiR-29mimicexpressionin786-Ocells.Eachdotrepresentsagene,andthosewithablackoutlinecontainat
leastonemiR-29bindingsite.Thecolourgradientrepresentsthelog-oddsofmiR-29bindingsiteenrichmentineachquarter.PvaluesarebasedonFisher’s
exacttest.AlsoseeSupplementaryFig.8formiR-29mimicexpressionin786-Ocells.eSimilartopanel(d),butusingdifferentialexpressionaftermiR-29
inhibitioninACHNcells.fVenndiagramillustratingtheoverlapofgenesthatareboundbymiR-29,upregulatedinKIRC,downregulatedaftermiR-29-
mimictreatmentof786-OandA-498cells,andupregulatedaftermiR-29inhibitioninACHNcells.gDifferentialexpressionofthe53genesidentifiedin
panel(f),in786-OorA-498cellsexpressingamiR-29mimic,orinACHNcellsexpressingamiR-29inhibitor.ErrorbarsrepresenttheSEM.Genesthat
areboldcorrespondtoECMgenes(basedonoverlapwithGO),andthosewithanasteriskaremarkersofembryonalcarcinoma(basedonStemCheker
(Pintoetal.,2015)).
Discussion roleofpost-transcriptionalregulationinshapingthecancertran-
By quantifying differential mRNA stability patterns across 18 scriptome. We note that this resource also provides an approx-
cancertypes,ourstudypresentsasystematicresourceformining imation for the relative contribution of transcriptional and post-
the post-transcriptional landscape of cancer. Importantly, our transcriptionaleventsinshapingcancertranscriptome:onaverage,
results uncovered recurrent changes in the stability of >13,000 19% of genes that are significantly upregulated at the expression
mRNAs in at least one cancer type, highlighting the widespread levelaredetectedbyDiffRACassignificantlystabilizedintumours,
COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio 9
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
and23%ofgeneswithsignificantlyreducedexpressionaredetected In addition to RBPs, our results also highlight cancer type-
assignificantlydestabilized.Incomparison,66%and61%ofgenes specific deregulation of mRNA stability by miRNAs, with miR-
whoseexpressionissignificantlyup-ordownregulatedaredetected 29standingoutasapan-cancerstabilityfactor.Ourobservations
astranscriptionallyactivatedorinhibitedintumours,respectively are in line with previous studies showing that different miR-29
(SupplementaryFig.11).Wenotethatabout57%ofthevariability isoforms act as tumour suppressors and are downregulated in
in the number of differentially stabilized genes across cancer several cancer types51,52,affectingcell proliferation, differentia-
types appears to be attributed to sample size, suggesting that our tionandapoptosis53.Thisdownregulationcorrelateswithmore
analysis may be underpowered for smaller cancer cohorts (Sup- aggressive forms of cancer, characterized by increased metas-
plementary Fig. 12). Nonetheless, these results suggest an impor- tasis,invasionandrelapse54,andtherapeuticrestorationofmiR-
tant role for post-transcriptional changes in shaping the cancer 29 was suggested to improve disease prognosis55. In line with
transcriptome,withrecurrentchangesthatare~30%asfrequentas these reports, we observed pan-cancer stabilization of miR-29
transcriptionalevents. targets, suggesting widespread reduction in miR-29 activity in
Our study also highlights the coordinated post-transcriptional cancer,whichcouldbepartiallyreversedbymiR-29rescue.We
deregulation of genes that are involved in the same pathways. note that our results highlight a core set of 53 mRNAs that are
Notably, we observed recurrent stabilization of mRNAs that miR-29 targets, stabilized at least in KIRC, downregulated after
encode epithelial-mesenchymal transition (EMT) proteins and restoringmiR-29activityintheKIRCmodelcelllines786-Oand
MYCtargetsacrossmultiplecancertypes.EMTistheprocessby A-498, and upregulated after miR-29 inhibition in ACHN cells
which epithelial cells lose their apical-basal polarity and cell–cell (Fig. 6f). Importantly, seven of these genes are markers of
adhesion, and instead acquire mesenchymal properties such as embryonal carcinoma, suggesting that miR-29 inhibition is
migratory and invasive potentials40; our results suggest that essential for activation of an embryonic-like program in cancer
activation of the EMT pathway in cancer is at least partly (Fig. 6g). In addition, we observed a significant enrichment of
mediated by post-transcriptional upregulation. Similarly, we the extracellular matrix (ECM) genes (Fig. 6g), suggesting that
observedpost-transcriptionalupregulationofMYCtargets,which miR-29 inhibition also contributes to ECM remodeling in
include growth-related genes that directly contribute to cancer, consistent with previous reports on ECM regulation by
tumourigenesis41.MYCisawell-definedtranscriptionfactorand miR-2956.
represents one of the most frequently amplified oncogenes42, It should be noted that various pathways may affect mRNA
leading to transcriptional activation of its targets in cancer. stability and its estimates. For example, disruptions in the
Therefore, our intriguing observation that MYC targets are also nonsense-mediateddecay(NMD)pathwayaffectsthetranslation-
upregulated at the mRNA stability level suggests the presence of dependentstabilityofawiderangeofmRNAs57.Sincemostofthe
convergent transcriptional and post-transcriptional mechanisms affectedtranscriptsarelikelyspliced58,suchchangesareexpected
that modulate overlapping gene sets. Furthermore, we observed tobeproperlycapturedbyouranalysisofspliced/unsplicedtran-
coordinated destabilization of mRNAs for genes implicated in script ratios. However, analysis of spliced/unspliced transcript
oxidativephosphorylation(OXPHOS)andrelatedpathwayssuch ratiosmaynotbesuitableforstudyingNMD-dependentclearance
as fatty acid metabolism and adipogenesis, consistent with the ofunsplicedcytoplasmictranscripts59.Otherproteinsinvolvedin
well-documented Warburg effect in which upregulation of glu- the RNA decay pathway are also expected to influence mRNA
cose consumption and glycolysis is accompanied by a down- stability, although we were not able to detect a significant asso-
regulation of OXPHOS43. ciationbetweenthedegreeofRNAstabilitydisruptionandsomatic
In addition, we observed widespread and coordinated post- alterations in RNA decay pathway proteins (Supplementary
transcriptional modulation of the targets of RNA-binding pro- Fig. 14). While RNA surveillance pathways such as NMD and
teins(RBPs)incancer,withtheRBFOXfamilyofRBPsstanding generalRNAdecayproteinsaffectmRNAstabilityglobally,inthis
outashavingthemostrecurrentlydownregulatedregulonacross workwechosetofocusonregulon-specificdisruptionscausedby
multiple cancer types. RBFOX proteins are known regulators of abnormal activity of RBPs and miRNAs. We note that different
alternative splicing and mRNA stability28 and have been impli- mechanisms may underlie the observed disruption in the RBP/
catedinanumberofneurologicaldiseases17,31,44,buttheirrolein miRNA regulons in cancer, including changes in the expression
cancer is less characterized. Nonetheless, at least the RBFOX1 levels of these regulatory factors, mutations, post-translational
locusappearstobeamongthemostfrequentlydeletedlociacross modificationsinthecaseofRBPs,disruptionofmiRNAbiogenesis,
different cancer types45,46, with its deletion47 or other genetic competition/cooperation with other regulatory factors, and
defects48 beingassociatedwithpoorsurvival.Our studysuggests enhanced/restricted access to binding sites on target transcripts.
that downregulation of RBFOX proteins leads to destabilization However, at least in the case of RBPs, we observed a strong cor-
of their target transcripts in tumours; many of these transcripts relation between their expression and regulon activity in cancer
encode proteinsinvolvedincalciumsignaling,a criticalpathway (Fig. 4d), suggesting that disruption of the expression of RBPs is
that affects a wide range of cancer-associated processes such as mostlikelythedominantmechanismunderlyingthedysregulation
proliferation, invasion, and apoptosis49. The association between oftheirregulons.
RBFOX1 and calcium signaling is also supported by previous Together, these results highlight a key role for mRNA stability
literature that shows a positive effect of RBFOX1 on the expres- programs,mediatedbyRBPsandmiRNAs,inregulationofpath-
sion of some of the genes involved in this pathway50. We note ways that are integral to cancer development and progression.
that the RBFOX family of proteins includes RBFOX1, RBFOX2, Whilethevastmajorityofcurrentliteratureisfocusedontherole
andRBFOX3;however,RBFOX1andRBFOX3showthegreatest oftranscriptionalmechanismsinreprogrammingcancercells,this
extent of downregulation across different tumours (>60-fold, studyunderlinesacriticalandlargelyuncharacterizedroleforpost-
Fig. 5a, b), whereas RBFOX2 shows comparatively moderate transcriptional remodeling of the cancer cell transcriptome, and
downregulation (~3-fold, Supplementary Fig. 13). Furthermore, provides a resource for exploring post-transcriptional pathways
RBFOX2 does not show significant correlation with the expres- incancer.
sion of the mRNAs that contain the RBFOX-binding consensus
sequence28. Taken together, these observations suggest that
Methods
RBFOX1/3arethemostlikelycandidatesdrivingdysregulationof JointmodellingofintronicandexonicreadcountsandmRNAstability.Our
the RBFOX regulon in cancer. approachforstatisticalmodelingofintronicandexonicreadcountsbuildson
10 COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
previousresearchthatconnectstheabundanceofpre-mRNAandmaturemRNA andexonicreadcountsacrossallgenesinamodelthatassumesthemRNAstabilityis
tomRNAstability(SupplementaryFig.1a,b): agene-specificconstant.Specifically,weusethebelowdesignmatrixDtofitthe
modelusingDESeq2,whilevaryingthevalueofbintheinterval[0,1]toselecttheb
logm¼b´logpþlogφþlogγ ð1Þ
thatmaximizesthesumoflog-likelihoodofthedataacrossallgenes:
(cid:2) (cid:3)
h ac e r r o e s , s m d c if o f r e r r e e s n p t o s n a d m s p to les th , e p v is ec t t h o e ro ab f u th n e d m an a c t e ur o e f m th R e N p A re- a m bu a n tu d r a e nc m e R fo N r A a , g γ iv i e s n th ge e ne D0¼ I n 0 n´1 ð8Þ
mRNAstabilityacrosssamples,φisthemaximumprocessingrateofRNA,andbis b´I n 1 n´1
thebias-term(SupplementaryFig.1b).Vectorsaredifferentiatedfromscalarsusing weusethe‘optimize’functioninRtoselecttheoptimalvalueofb.Oncethisoptimal
boldtypeface. valueisidentified,itisusedinthematrixX’(seeabove),whichisthenusedasthe
WefurthermodelthelogarithmofmRNAstabilityasalinearfunctionofaset designmatrixinDESeq2toestimatethelatentvariables,includingβ(i.e.theeffectof
ofsample-levelvariables: eachvariableonstability).ThisprocedureisimplementedinDiffRAC(https://github.
logγ¼X´βþα ð2Þ com/csglab/DiffRAC).
here,Xisthen×kmatrixofsample-levelvariables(fornsamplesandkvariables), Amodifieddesigntoaccommodatelargersamplesizes.Amajorlimitationof
βisthevectorofcoefficientsthatquantifytheeffectofeachvariableonthemRNA
thisapproachistheconsiderableincreaseincomputingtimewithlargersample
stability,andαisanintercept(matricesaredifferentiatedfromvectorsusing
sizeswhenDESeq2isusedtofitthemodel,sincethemodelincludessample-
capitalletters).Thisleadsto: specificlatentvariablesforpre-mRNAabundance.Toaccommodatethesecases,
logm¼b´logpþcþX´β ð3Þ wehavealsoimplementedamodelthatassumesthatmostofthevarianceinpre-
mRNAabundancecanbeexplainedbytheexperimentalvariables,insteadof
wherec=logφ+α.Wemodelthemeanofintronicreadcountsforagivengene includingsample-specificlatentvariables:
acrosssamplesasafunctionofthepre-mRNAabundanceforthatgene,agene-
levelscalingfactorthatcanbeinterpretedastheeffectivelength,andasample-
logp¼X´ωþρ ð9Þ
specificscalingfactorthatcanbeinterpretedaslibrarysize(Fig.1b):
Here,ωisthevectorofcoefficientsthatrepresenttheeffectofeachvariableonthe
λint¼p´l´sint ð4Þ pre-mRNAabundanceofagivengene,andρisagene-specificintercept.There,we
alsohave:
here,intstandsforintronic,λrepresentsthemeanreadcount,listhegene-specific (cid:4) (cid:5)
scalingfactor,andsisthesample-specificscalingfactor.Similarly,themeanof logm¼b´ X´ωþρ þcþX´β ð10Þ
exonicreadcountsforagivengeneacrosssamplescanbeexpressedas: Thisleadstoamodifiedsetofmatrixequations(SupplementaryFig.3a–c)that
λexo¼m´l0´sexo ð5Þ connectintronic/exonicreadcountstosamplevariables:
2 3
ρ0
Theaboveequationsc
l
a
o
n
g
" b λ e in c t o # lle
¼
cti
l
v
o
e
g
l (cid:2) y s e i x nt p (cid:3) re
þ
sse
X
d
0
2 6
4
by lo m g
c0
p at 0 r 3 7
5
ixoperationsas:
ð6Þ
log " λ λ e in xo t # ¼log (cid:2) s s e in xo t (cid:3) þX0 6 6 6 4 ω c0 7 7 7 5 ð11Þ
λexo sexo β
β
where
where (cid:2) (cid:3)
X0¼ (cid:2) b´ I n I n 0 1 n n ´ ´ 1 1 X 0 n n ´ ´ k k (cid:3) ð7Þ andρ‘=ρ+logl,an X d 0 c’ ¼ =c+ 1 1 n n l ´ ´ o 1 1 g(l’ b /l) ´ X + X n´ n ρ k ´ × k (b– 0 1 n n 1 ´ ´ ). 1 1 Sim X 0 i n n la ´ ´ r k k totheprevioussect ð i 1 o 2 n Þ ,
andp’=p×l,c’=c+log(l’)−b×log(l),andIistheidentitymatrix(matrix X’canbeusedasthedesignmatrixforDESeq2toestimatethelatentvariables,
dimensionsareindicatedassubscripts).Theseequationsconnectpre-/mature includingωandβ.
mRNAabundanceandmRNAstabilitytotheobservedintronicandexonicread ToconstructX’,thebias-termbischosensothatitmaximizesthesumoflog-
countsforeachgivengene(seeSupplementaryFig.1c,dformatrixequationsthat likelihoodofdataacrossallgenesinamodelthatassumesgene-specificconstant
considerallgenesatthesametime).Thisformulationenablestheestimationof stability,i.e.withthebelowdesignmatrixD’:
unknownparametersusingageneralizedlinearmodelwithalog-linkfunction.In (cid:2) (cid:3)
thisstudy,weuseDESeq260tofittheunknownparametersofthismodel,as D0¼ 1 n´1 X n´k 0 n´1 ð13Þ
explainedbelow. 1 n´1 b´X n´k 1 n´1
Itshouldbenotedthatchangesintheratioofspliced/unsplicedmRNAs,and ThissimplifiedmodelisalsoimplementedinDiffRAC.Overall,weseestrong
ultimatelyintheobservedintronicandexonicreadcounts,mayarisefromawide agreementbetweenDiffRAC’sestimateswhenusingthetwodifferentmodels(i.e.
arrayofpathwaysaffectingdecayofpre-mRNAsormaturemRNAsindifferent sample-specificpre-mRNAabundancesvs.condition-specificpre-mRNA
manners.However,previousresearchhasdemonstratedthatnucleardecayofpre-
mRNAsdoesnotaffecttheratioofexonic/intronicreads17(Supplementary abundances)onthesamedata(SupplementaryFig.3d).
Fig.1b).Thisindicatesthatmechanismsaffectingpre-mRNAlevelsdonotleadtoa
substantialchangeinthefinalratioofspliced/unsplicedmRNAsaslongasthepre- DifferentialRNAstabilitybetweenNAT10knockoutandparentalcells.Raw
mRNAremainsapotentialsubstrateforthesplicingmachinery,sinceachangeat BRICsequencing(BRIC-seq)(5′-bromo-uridine[BrU]immunoprecipitation
thepre-mRNAlevelleadstoanequivalentchangeatthematuremRNAleveland, chase-deepsequencinganalysis)readsfortime-seriesmeasurementsofBrU-pulsed
therefore,doesnotaffecttheratio.Theestimatesofdifferentialstabilitygenerated RNAsinparentalandNAT10−/−HeLacells20,61wereobtainedfromGEO
inthisstudythereforerepresentmostlytheeffectofchangeindegradation accessionGSE102113(SRAaccessionSRP114504).ThisRNA-seqdatasetrepre-
occurringatthematuremRNAlevels. sentstimepoints0,2,4,8and16haftera24-hourtreatmentofcellswithBrU(two
DifferentRNAselectionmethodscanalsoaffecttheintronicreadcounts. replicatesforeachcelllineateachtimepoint).ReadsweremappedtotheGRCh38
Poly(A)-selectedRNAwillleadtoalowerproportionofintronicreadscompared genomeassemblyusingHISAT262,andgene-levelreadcountsforeachsample
torRNA-depletedRNA.Inthecurrentstudy,wemadeuseofseveralpoly(A)- wereobtainedusingHTSeq-count63(“intersection-strict”mode)basedonEnsembl
selecteddatasets,includingtheRNA-seqdatafromTCGA.However,sinceall GRCh38v87geneannotations.Ground-truthDifferentialmRNAstabilitybetween
samplesineachdatasetwereanalysedusingthesamemethod,theestimatesareall thecontrolandNAT10KOcellswasobtainedusingDESeq260bymodelingthe
affectedinasimilarmanneracrossthesampletypesandcancertypes.Wenotethat RNAabundancesasafunctionof~c+t+c:t,wherecisthecelltype(0forControl
poly(A)-selectedRNAhaspreviouslybeenshowntoproducesufficientintronic and1forNAT10KO),tisthetimepoint,andc:tistheinteractionbetweencelltype
readsforstabilityestimation15.Inaddition,thelargenumberofsamplesincluded andtime.Inthismodel,thecoefficientofcwouldrepresentthedifferential
inthisstudymostlikelymitigatesanystatisticalpowerlossthatresultsfromlower expressionbetweenthetwocelltypes(i.e.differenceinabundanceattimezero);
amountofintronicreads. thecoefficientoftwouldrepresentthestabilityofeachgene’smRNAinthe
referencecellline(relativetotheaverageofallgenes);andthecoefficientofthe
interactiontermc:twouldrepresentthedifferentialmRNAstabilitybetweenthe
e
E
q
s
u
ti
a
m
ti
a
o
t
n
i
s
on
all
o
o
f
w
th
u
e
st
e
o
ff
e
e
st
c
i
t
m
o
a
f
te
s
t
a
h
m
e
p
d
l
i
e
str
v
i
a
b
r
u
ia
ti
b
o
l
n
es
of
o
l
n
ate
m
n
R
t
N
va
A
ria
s
b
t
l
a
e
b
s
i
l
l
o
it
g
y.
p’
T
,
h
c’
e
,a
a
n
b
d
ov
β
e
by
twocelllines.Foreachgene,thecoefficientofc:tandassociatedstatisticswere
fittingthemodeltoobservedintronicandexonicreadcounts.Forthispurpose,we retrievedusingDESeq2.
usethematrixX’asthedesignmatrixinaDESeq2model.Inpractice,wereplace
thefirstcolumnofX’withanintercept(Fig.1c),whichisanequivalentdesign TCGARNA-seqdataprocessing.RNA-seqBAMfilesfor7078tumoursamples
matrixanddoesnotchangetheinterpretationofβ,butenablestheusertoemploy and682adjacentnormalsamplesfromthe18cancertypeswithatleast5normal
abetaprior(ifdesired)whenfittingtheDESeq2model. samplesinTCGAwereacquiredfromtheNationalCancerInstitute(NCI)
InordertobeabletoconstructX’,thebiastermbneedstobefirstestimated.We GenomicDataCommons(GDC)dataportal(https://portal.gdc.cancer.gov/GDC;
dothisbyfirstoptimizingbinordertomaximizethelikelihoodofobservedintronic dbGaPstudyaccessionphs000178.v1.p1).AllTCGARNA-seqdatausedinthis
COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio 11
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
studywasgeneratedfrompoly(A)-selectedRNA.Inordertoquantifythenumber numberofbindingsitesofRNA-bindingfactors(ratherthanaspecificRBPor
ofreadscorrespondingtopre-mRNAandmaturemRNAfortheestimationof miRNA;e.g.3ʹUTRlength),weusedthetotalnumberofbindingsitesofeach
mRNAstability,wegeneratedcustomannotationsforexonsandintronsforthe mRNAforRBPsormiRNAsasthebackground.Specifically,weusedageneralized
transcriptssupportedbybothEnsemblandHavanaconsortia,usingGTFfor- linearmodelofthebinomialfamily,inwhichthepresenceofabindingsiteforthe
mattedannotationsacquiredfromEnsemblGRCh38version87. specificRBPormiRNAofinterestisconsideredas“success”,andthepresenceof
Wenotethat,inadditiontomRNAstability,aberrantalternativesplicingmay bindingsitesforotherRBPsormiRNAsconsideredas“failures”.Thesesuccess/
affecttheexonicreadprofiles.Toavoidthepotentialconfoundingeffectof failurecountsweremodeledasafunctionofthestabilitystatusofthetranscript
alternativesplicingonmaturemRNAquantification,weexclusivelyretainedexonic usingtheglmfunctioninR.
readsmappingtoconstitutiveexonsthatarepresentinallEnsembl/Havana
transcripts.Evenwhenonlyconstitutiveexonsareusedforreadcounting,there
mightbecaseswhereasplicingshiftleadstotranscriptsthathavereducedor HITS-CLIPdataanalysis.PooledHITS-CLIPpeaksofRBFOX1/2/3proteinsin
enhancedstability.Insuchcases,DiffRACshouldstilldetecttheoverallchangein
wholebraintissuelysateofmicewereretrievedfromapreviousstudy32.Peaks
stability,eventhoughitiscausedbytheinteractionbetweenabnormalalternative
occurringinthe3ʹUTRwithaheightgreaterorequalto200overlappingCLIPtags
splicingandisoform-specificdecaymechanisms.Similartoref.17,welimitedour wereretained(peakheightwasextractedfromSupplementaryTable1ofthesource
analysisofRBPandmiRNAregulonstothegenesthatsharedthesame3′UTR publication).ThemRNAsthathadatleastone3ʹUTRhigh-confidencepeakwere
acrossalltheirisoforms,withthe3ʹUTRcomposedofasingleexon,tomitigatethe consideredhigh-confidenceRBFOXtargets,whichwerefurtherfilteredtoinclude
potentialconfoundingeffectofalternative3ʹUTRusage/splicingonmRNA onlythosewhoseorthologshadexpressionmeasurementsinTCGA.Thisresulted
stability.
in58genes,54ofwhichalsohavea3ʹUTRRBFOXbindingsitebasedonCIMS
Intronicregionswereincludedinourannotationsonlyiftheydidnotoverlap analysisofCLIPdata.
withanyexon,regardlessofwhethertheexonwasconcordantlyannotatedby
EnsemblorHavanaconsortia.ThestrandednessofRNA-seqdatawasdetermined
usingRSeQC64.Subsequently,BAMfilesweresortedbyreadnameusing
CellcultureandtransienttransfectionofmiRNAmimicsandinhibitors.The
establishedrenalcancercellline786-O,A-498andACHNaswellastheglio-
SAMtools,andexonicandintronicreadswereseparatelycountedusingHTSeq-
c u o si u n n g t6 t 3 h , e li H m T it S in e g q t “ o in r t e e a r d se s ct w io it n h -s a tr M ict A ” P m Q od sc e o , r w e h ≥ e 3 re 0 a . s E i x n o t n ro ic ni r c ea r d ea s d w s e w re er c e ou co n u te n d ted b le l c a t s i t o o n m ( a A c T e C ll C li ; n R e o A ck 1 v 7 i 2 lle w , e M re D p , u U rc S h A a ) se a d nd fro c m ultu th r e ed A i m n e D ri u c l a b n ec T c y o p ’s e M C o u d lt i u fi r e e d C E o a l g - le
usingthe“union”mode.Theexonic/intronicreadcountswerethenusedasinput Medium(DMEM)supplementedwith10%fetalbovineserum(FBS)and1%
penicillin/streptomycin(Lifetechnologies)at37°Cwith5%CO2.Fortransient
toDiffRACforstabilityanalysis.Weremovedthecellcyclegenes(basedonGO
transfection,786-OandA-498cells(100,000cells/wellin6-wellplates)were
termGO:000704)fordownstreamanalyses,giventhatthesegenesarenotatsteady
reverse-transfectedinantibiotic-freemediumwith10nMofmiRNA-29mimic
state,whichisrequiredforestimatingstabilityfrompre-/maturemRNA
(stem-loopsequence:UGGUUUCGUAUUGGUGCAUAGAAGUAUUAAUUU
abundances.
UGUAACUUGUCUAGCACCAUUUGAAACCAGU(twobiologicalreplicatesfor
A-498,andonefor786-O),maturemiRNAsequence:UAGCACCAUUUGAA
Deconvolutionofcellularoriginfromdifferentialstabilityestimates.We ACCAGU,ThermoFisher,4464066)orcontrolmimic(ThermoFisher,4464058)
inferredstage-associatedchangesinstabilityspecificallyoriginatingfromthe (twobiologicalreplicatesforA-498,andonefor786-O)usingLipofectamine
cancerous(orpre-cancerous)cellsusingDiffRACwithadesignmatrixthatmodels
RNAiMAXReagent(ThermoFisher,13778075)accordingtothemanufacturer’s
theexonic/intronicreadratioasafunctionofthetumourstage(dichotomizedinto recommendations.ACHNcellsweretransfectedeitherwithmiR-29inhibitor
low-stageandhigh-stagecategories),theimpurity(fractionofnon-malignantcells) (ThermoFisher,4464084,AssayID:MH10103)ornegativecontrol(ThermoFisher
ofthetumourasmeasuredbyABSOLUTE65,andaninteractiontermbetween 4464076)usingthesameprotocoldescribedabove,withthreebiologicalreplicates
stageandimpurity,similartoref.27.AsshowninFig.3d,differentcoefficients each.TwoadditionalRNA-seqsamplesrelatedtothemiR-29mimicexperiment
retrievedfromthismodelrepresentthestage-associatedchangesinstabilityori- performedinA-498cellswereexcludedduetopotentialmislabelingofthesamples.
ginatingfromcancerousorpre-cancerouscellsspecifically.Specifically,thecoef-
ficientofthetumourstagevariablerepresentsdifferenceinstabilitybetweenhigh-
RNAisolationandqRT-PCRanalysisofmiRNAs.TotalRNAwasextracted
andlow-stagetumourswhenimpurityiszero,andthuscanbeinterpretedasthe
stage-associateddifferentialstabilitythatisconfidentlyattributedto usingAllPrepDNA/RNA/miRNAUniversalkit(Qiagen)48haftertransient
transfection.RT-PCRwasdoneusingTaqManMicroRNAreversetranscriptionkit
malignantcells.
(AppliedBiosystems,4366596).TheLightCycler480instrument(Roche)wasused
toperformqRT-PCRanalysisofmiR-29andmiR-26usingTaqManFast
Pathwayanalysis.MSigDBhallmarkgene-sets66wereretrievedusingthemsigdbr AdvancedmiRNAAssays(ThermoFisher,4444557)followingguidelinesprovided
Rpackage(https://cran.r-project.org/web/packages/msigdbr/index.html).Foreach bythemanufacturer.ExpressionwasreportedasCtvalues(SupplementaryFig.8).
TCGAcancertype,Fisher’sexacttestwasusedtoexaminetheassociationbetween
eachpathwayandthesetsofsignificantlystabilizedordestabilizedmRNAs,
separately.
StablecellsexpressingRBFOX1.TogeneratestableA172celllines,
HEK293Tcellsweretransfectedwithlentiviralpackagingplasmids(psPAX2and
MD2.g)togetherwithalentiviralexpressionplasmidforeitherGFPorRBFOX1
DifferentialRNAstabilitybetweenMDA-MB-231andMDA-LM2cells. (threebiologicalreplicateseach)usingLipofectamine3000.PlasmidspLX317-GFP
RawRNA-seqreadsfortime-seriesmeasurementsof4-thiouridine(4sU)- andpLX317-RBFOX1wereobtainedfromtheTRC3ORFcollectionfromSigma
labeledRNA23,67fromMDA-MB-231andMDA-LM2cellswereobtainedfrom providedbyMcGillPlatformforCellularPerturbation(MPCP)atMcGillUni-
GEOaccessionGSE49608(SRAaccessionSRP028570).ThisRNA-seqdataset versity.After48h,mediacontaininglentiviralparticleswerecollected,filtered
representstimepoints0,2,4,and7haftera2-hourtreatmentofcellswith througha0.45μmsyringefilter,andimmediatelyaddedtoA172cellswith8μg/ml
4sU(fourreplicatesforeachcelllineateachtimepoint).Rawdatawas polybrene.Over-expressionofGFPandRBFOX1wereconfirmedbyfluorescence
processedanddifferentialmRNAstabilitybetweentheMDA-MB-231and microscopy(forGFP)orqPCR(forRBFOX1).TotalRNAwasextractedusingthe
MDA-LM2cellswasobtainedinthesamewayastheNAT10KOBRIC-seqdata AllPrepDNA/RNA/miRNAUniversalkit(Qiagen).
(seeaboveMethods).
RNA-sequencingandanalysis.LibrarypreparationfromtotalRNAwasper-
RBPandmiRNAregulonanalysis.Thestabilityregulonsof35RBPs(i.e.theset formedusingNEBrRNA-depleted(HMR)strandedlibrarypreparationkit
ofmRNAsboundandregulatedbyeachRBP)wereobtainedfromaprevious accordingtomanufacturer’sinstructions,andsequencedusingIlluminaNovaSeq
publication28.TheregulonsofmiRNAfamilieswereobtainedbyidentifyingexact
6000(100bppaired-end).RNA-seqreadswerealignedtotheGRCh38genome
miRNAseedmatchesinmRNA3ʹUTRs.Specifically,3ʹUTRsequencesofprotein-
assemblyusingHISAT262,andgene-levelreadcountswereobtainedusingHTSeq-
codinggeneswereretrievedusingtheEnsemblGRCh38version87annotations. count63(“intersection-strict”mode)basedonEnsemblGRCh38v87geneanno-
Welimitedtheanalysistothegenesforwhichasingle3ʹUTR,composedofa
tations.DESeq260wasusedtocomputedifferentialgeneexpression.
singleexon,wassharedacrossallisoforms,inordertoavoidthepossiblecon-
foundingeffectsofalternativesplicing.ThemiRNAseedsequences(8nt)were
retrievedfromTargetScanv7.268,limitingtoasetof153broadlyconserved Statisticsandreproducibility.Allstatisticalanalysiswereperformedusingby
miRNAfamilies(familyconservationscore≥1).Exactseedsequencematchesin3ʹ BioconductorpackagesinR(version4.1.2).Thespecificstatisticaltestsusedfor
UTRsequenceswereidentifiedwhilelimitingthesearchspacetoamaximumof eachanalysisandtheassociatedmeasuresofstatisticalsignificanceareindicated
2000ntdownstreamofthestopcodon. withinthemaintext,methods,inthefigure,orintheirlegends.Statisticalsig-
Theregulonenrichmentamongupregulatedordownregulatedgeneswas nificancewassetatP<0.05forallanalysesandmultipletestingcorrectionwas
quantifiedusingalogisticregressionapproach.Specifically,foreachcancertype, performedwhenapplicableusingtheFDRmethod.SamplesizeforTCGAcohort
wemodeledthelikelihoodofbeingboundbyeachRBP/miRNAasafunctionof analysisdependedonpubliclyavailabledata.Nostatisticalanalysiswasperformed
status,with–1correspondingtosignificantlydestabilizedmRNAs(FDR≤0.05), toselectthesamplesizesforRNA-seqexperiments.Toensurereproducibilityfor
+1correspondingtosignificantlystabilizedmRNAs,and0correspondingtonon- RNA-seqexperiments,biologicalreplicateswereusedand/orthefindingswere
significantmRNAs.Toaccountfortheconfoundingfactorsthatgenerallyaffectthe replicatedinothercelllines.
12 COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
Reportingsummary.FurtherinformationonresearchdesignisavailableintheNature 22. Joshi,A.,VandePeer,Y.&Michoel,T.Structuralandfunctionalorganization
ResearchReportingSummarylinkedtothisarticle. ofRNAregulonsinthepost-transcriptionalregulatorynetworkofyeast.
NucleicAcidsRes39,9108–9117(2011).
23. Goodarzi,H.etal.Metastasis-suppressortranscriptdestabilizationthrough
TARBP2bindingofmRNAhairpins.Nature513,256–260(2014).
Data availability
24. Fish,L.etal.AprometastaticsplicingprogramregulatedbySNRPA1
Datageneratedduringthisstudyareincludedinthispublishedarticleandits interactionswithstructuredRNAelements.Science372,eabc7531(2021).
supplementaryfiles.Additionaldataandanalysisfilesareavailableathttp://csg.lab.
25. Welm,A.IlluminaHiSeqSequencingonBreastcancerPDXsamples.GEO
mcgill.ca/sup/pancancer_stability/and/orviaZenodo(doi:10.5281/zenodo.4404547). https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE113986(2018).
RNA-seqdatafromthemiR-29mimicandinhibitorexpressionexperimentsare 26. Welm,A.&Lum,D.RNAseqofBreastcancerPDXsamples.GEOhttps://
availableviaGEOunderaccessionGSE145088.RNA-seqdatafromtheRBFOX1 www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE113476(2018).
overexpressionexperimentarealsoavailableviaGEOunderaccessionGSE201639.The 27. Kim-Hellmuth,S.etal.Celltype-specificgeneticregulationofgeneexpression
resultspublishedhereareinpartbasedondatageneratedbytheTCGAResearch acrosshumantissues.Science369,https://doi.org/10.1126/science.aaz8528(2020).
Network:https://www.cancer.gov/tcga.Otherdatausedinthispaperareavailablevia 28. Ray,D.etal.AcompendiumofRNA-bindingmotifsfordecodinggene
theirsourcepublicationsasindicatedinthearticle. regulation.Nature499,172–177(2013).
29. Jonas,S.&Izaurralde,E.TowardsamolecularunderstandingofmicroRNA-
mediatedgenesilencing.Nat.Rev.Genet16,421–433(2015).
Code availability 30. Guo,H.,Ingolia,N.T.,Weissman,J.S.&Bartel,D.P.Mammalian
microRNAspredominantlyacttodecreasetargetmRNAlevels.Nature466,
DiffRACisavailableviaGitHubathttps://github.com/csglab/DiffRAC. 835–840(2010).
31. Lee,J.A.etal.CytoplasmicRbfox1regulatestheexpressionofsynapticand
Received: 15February 2021; Accepted: 4August 2022; autism-relatedgenes.Neuron89,113–128(2016).
32. Weyn-Vanhentenryck,S.M.etal.HITS-CLIPandintegrativemodelingdefine
theRbfoxsplicing-regulatorynetworklinkedtobraindevelopmentand
autism.CellRep.6,1139–1152(2014).
33. Fogel,B.L.etal.RBFOX1regulatesbothsplicingandtranscriptionalnetworks
inhumanneuronaldevelopment.Hum.Mol.Genet21,4171–4186(2012).
References 34. Fogel,B.,Wexler,E.,Friedrich,T.,Konopka,G.&Geschwind,D.RBFOX1
SplicingandTranscriptionalRegulationinNeurons.GEOhttps://www.ncbi.
1. s F p is li h c , in L g .e a t n a d l. d N ec u a c y l . ea M r o T l. A C R e B ll P 7 2 5 d , r 9 i 6 v 7 es –9 o 8 n 1 co e g 9 e 6 n 9 ic (2 d 0 y 1 s 9 r ) e . gulationofRNA 35. n Le lm e, .n J. i , h L .g in ov , / C g . e , o M /q a u r e t r in y/ , a K cc . .c & gi B ?a la c c c k = , G D S . E G 3 e 6 n 7 e 10 ex ( p 20 re 1 s 2 s ) i . onprofilingofneurons
2. Fish,L.etal.CancercellsexploitanorphanRNAtodrivemetastatic
progression.Nat.Med24,1743–1751(2018). w
Rb
it
f
h
ox
R
1
b
i
f
s
o
o
x
f
1
or
a
m
nd
.G
R
E
b
O
fox
h
3
tt
k
p
n
s:
o
//
c
w
kd
w
o
w
w
.n
n
cb
an
i.n
d
lm
re
.
s
n
c
i
u
h
e
.g
w
ov
it
/
h
ge
c
o
y
/
t
q
o
u
p
e
la
ry
sm
/a
i
c
c
c.
o
cg
r
i
n
?a
u
c
c
c
l
=
ear
3. Goodarzi,H.etal.EndogenoustRNA-derivedfragmentssuppressbreast
cancerprogressionviaYBX1displacement.Cell161,790–802(2015). GSE71916(2015).
4. e G x o p o r d es a s r i z o i n ,H an . d et c a a l n . c M er od p u ro la g t r e e d ss e io x n pr . e C ss e i l o l n 16 o 5 f , s 1 p 4 e 1 c 6 ifi – c 14 tR 27 N ( A 2 s 01 d 6 r ) iv . esgene 3 3 7 6 . . J K N o a u p n c li l e e n h i g c is , A a C , c . M id L s . iv & R er e - s G s 2 p o 8 e to c , , i 2 fi S 7 c . – m K 30 E ic G ( r 2 o G 0 R : 0 N 0 k ) A y . o - t 1 o 22 e : n b cy io c g lo e p n e e d si i s a a o n f d ge fu n n es ct a io n n d . g R e N no A m B e i s o . l.
5.
p
P
r
e
o
rr
g
o
ra
n
m
,G
s
.
id
e
e
t
n
a
t
l
i
.
fi
A
es
g
R
e
N
ne
A
r
-
a
b
l
i
f
n
r
d
am
in
e
g
w
p
o
r
r
o
k
te
f
i
o
n
r
s
i
t
n
h
t
a
e
t
rr
g
o
o
g
v
a
e
t
r
i
n
on
ca
o
n
f
c
m
er
R
tr
N
a
A
nsc
s
r
ta
ip
b
t
i
o
li
m
ty
es.
9,137–142(2012).
CellRep.23,1639–1650(2018). 38. Wu,C.,Zhang,J.,Cao,X.,Yang,Q.&Xia,D.EffectofMir-122onhuman
cholangiocarcinomaproliferation,invasion,andapoptosisthroughP53
6. Png,K.J.etal.MicroRNA-335inhibitstumorreinitiationandissilenced expression.MedSci.Monit.22,2685–2690(2016).
throughgeneticandepigeneticmechanismsinhumanbreastcancer.Genes
Dev.25,226–231(2011). 39. Liu,N.etal.TherolesofmicroRNA-122overexpressionininhibiting
proliferationandinvasionandstimulatingapoptosisofhuman
7. Tavazoie,S.F.etal.EndogenoushumanmicroRNAsthatsuppressbreast
cancermetastasis.Nature451,147–152(2008). cholangiocarcinomacells.Sci.Rep.5,16566(2015).
40. Ribatti,D.,Tamma,R.&Annese,T.Epithelial-mesenchymaltransitionin
8. Vanharanta,S.etal.LossofthemultifunctionalRNA-bindingproteinRBM47
cancer:ahistoricaloverview.Transl.Oncol.13,100773(2020).
asasourceofselectablemetastatictraitsinbreastcancer.Elife3,https://doi. 41. Meyer,N.&Penn,L.Z.Reflectingon25yearswithMYC.Nat.Rev.Cancer8,
org/10.7554/eLife.02734(2014). 976–990(2008).
9. s G ta o b o i d li a t r y zi o , f H m . a e m ta m l. a S li y a s n te m m e a s t s ic en d g i e s r co R v N er A y s o . f N s a tr tu u r c e tu 4 r 8 al 5, el 2 e 6 m 4 e – n 2 t 6 s 8 g ( o 2 v 0 e 1 r 2 n ) i . ng 42. Dang,C.V.MYConthepathtocancer.Cell149,22–35(2012).
43. Warburg,O.,Wind,F.&Negelein,E.TheMetabolismofTumorsintheBody.
10. Y
ch
a
a
n
r
g
a
,
ct
E
e
.
ri
e
s
t
ti
a
c
l
s
.
a
D
n
e
d
ca
s
y
eq
r
u
at
e
e
n
s
ce
of
a
h
tt
u
ri
m
bu
a
t
n
es
m
.G
RN
en
A
om
s:
e
co
R
r
e
r
s
e
.
la
1
t
3
io
,
n
18
w
6
i
3
t
–
h
1
f
8
u
7
n
2
ct
(
i
2
o
0
n
0
a
3
l
).
J.Gen.Physiol.8,519–530(1927).
44. Lal,D.etal.ExtendingthephenotypicspectrumofRBFOX1deletions:
11. Wada,T.&Becskei,A.ImpactofmethodsonthemeasurementofmRNA Sporadicfocalepilepsy.Epilepsia56,e129–e133(2015).
turnover.IntJMolSci18,https://doi.org/10.3390/ijms18122723(2017).
12. Schofield,J.A.,Duffy,E.E.,Kiefer,L.,Sullivan,M.C.&Simon,M.D. 45. H gli u o , m J. a e g t en a e l. si F s r . o P m roc th . e Na C t o l v A e c r: ad N . e S u c t i r . a U liz S a A tio 1 n 10 o , f 1 t 4 e 5 rm 20 i – n 1 a 4 l 5 d 2 i 7 ffe ( r 2 e 0 n 1 t 3 ia ) t . ionin
TimeLapse-seq:addingatemporaldimensiontoRNAsequencingthrough
nucleosiderecoding.Nat.Methods15,221–225(2018). 46. Rajaram,M.etal.Twodistinctcategoriesoffocaldeletionsincancergenomes.
PLoSOne8,e66264(2013).
13. Blumberg,A.etal.CharacterizingRNAstabilitygenome-widethrough
47. Andersen,C.L.etal.Frequentgenomiclossatchr16p13.2isassociatedwith
combinedanalysisofPRO-seqandRNA-seqdata.https://doi.org/10.1101/ poorprognosisincolorectalcancer.IntJ.Cancer129,1848–1858(2011).
690644(2019).
48. Huang,Y.T.etal.Genome-wideanalysisofsurvivalinearly-stagenon-small-
14. L
on
ug
a
ow
tr
s
a
k
n
i
s
,
c
A
ri
.
p
,
t
N
om
ich
e-
o
w
ls
i
o
d
n
e
,
s
B
c
.
al
&
e.
R
M
is
e
s
t
l
h
a
o
n
d
d
s
,
1
O
3
.
7
S
,
.
9
D
0–
e
9
te
8
rm
(2
i
0
n
1
in
8
g
).
mRNAhalf-lives celllungcancer.J.Clin.Oncol.27,2660–2667(2009).
49. Monteith,G.R.,Prevarskaya,N.&Roberts-Thomson,S.J.Thecalcium-
15. Gaidatzis,D.,Burger,L.,Florescu,M.&Stadler,M.B.Analysisofintronicand cancersignallingnexus.Nat.Rev.Cancer17,367–380(2017).
exonicreadsinRNA-seqdatacharacterizestranscriptionalandpost-
transcriptionalregulation.Nat.Biotechnol.33,722–729(2015). 50. Shen,F.etal.Rbfox-1contributestoCaMKIIalphaexpressionand
16. LaManno,G.etal.RNAvelocityofsinglecells.Nature560,494–498(2018). intracerebralhemorrhage-inducedsecondarybraininjuryviablockingmicro-
RNA-124.JCerebBloodFlowMetab,271678X20916860,https://doi.org/10.
17. Alkallas,R.,Fish,L.,Goodarzi,H.&Najafabadi,H.S.InferenceofRNAdecay
r A a l t z e h f e r i o m m er t ’s ra d n i s s c e r a i s p e t . io N n a a t l . p C r o o m fil m in u g n h . i 8 g , h 9 li 0 g 9 ht ( s 20 th 1 e 7) r . egulatoryprogramsof 51. i H 1 d 1 e e 7 , n 7 H t / i 0 fi . 2 c e 7 a t 1 t a i 6 o l. 7 n M 8X a i n 2 c d r 0 o 9 f R 1 u N 6 n 8 c A 6 ti 0 o ex n ( p 2 a 0 r l e 2 v s 0 a s ) l i i . o d n at p io ro n fi o li f n k g e i y n m cl i e R ar N c A e s ll . r P e L n o a S lc O el n l e ca 1 r 0 c , inoma:
18. Tippmann,S.C.etal.Chromatinmeasurementsrevealcontributionsof
e0125672(2015).
synthesisanddecaytosteady-statemRNAlevels.Mol.Syst.Biol.8,593(2012).
19. Tippmann,S.etal.Chromatinbasedmodelingoftranscriptionratesidentifies 52. Y sig an n , al B in . g e . t O al n . c T o h T e a r r o g l e e ts o T f h m er iR . - 8 2 , 9 5 b 39 in –5 c 4 a 8 nc ( e 2 r 0 : 1 r 5 e ) g . ulation,function,and
thecontributionofdifferentregulatorylayerstosteady-statemRNAlevels.
GEOhttps://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE33252(2012). 53. Park,S.Y.,Lee,J.H.,Ha,M.,Nam,J.W.&Kim,V.N.miR-29miRNAs
activatep53bytargetingp85alphaandCDC42.Nat.Struct.Mol.Biol.16,
20. A ef r fi a c n ie g n o c , y D . . C e e t ll a 1 l. 7 A 5, c 1 et 8 y 7 l 2 at – i 1 o 8 n 8 o 6 f e c 1 y 8 t 2 id 4 in (2 e 0 i 1 n 8) m . RNApromotestranslation 54. H 23 e – in 29 ze ( lm 20 a 0 n 9 n ). ,J.etal.SpecificmiRNAsignaturesareassociatedwith
21. Zanzoni,A.,Spinelli,L.,Ribeiro,D.M.,Tartaglia,G.G.&Brun,C.Post-
metastasisandpoorprognosisinclearcellrenalcellcarcinoma.WorldJ.Urol.
transcriptionalregulatorypatternsrevealedbyprotein-RNAinteractions.Sci. 29,367–373(2011).
Rep.9,4302(2019).
COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio 13
ARTICLE
COMMUNICATIONSBIOLOGY|https://doi.org/10.1038/s42003-022-03796-w
55. Garzon,R.etal.MicroRNA29bfunctionsinacutemyeloidleukemia.Blood Research,theFondsderechercheduQuébec–Santé(FRQS),andOncopole.T.L.hasbeen
114,5331–5341(2009). supportedbyaVanierCanadaGraduateScholarshipandatrainingscholarshipfromthe
56. Sengupta,S.etal.MicroRNA29cisdown-regulatedinnasopharyngeal FRQS.Y.R.isaresearchscholaroftheFRQS.Theresultspublishedhereareinpartbased
carcinomas,up-regulatingmRNAsencodingextracellularmatrixproteins. ondatageneratedbytheTCGAResearchNetwork:https://www.cancer.gov/tcga.Len-
Proc.NatlAcad.Sci.USA105,5874–5878(2008). tiviralORFexpressionplasmidswereprovidedbytheMcGillPlatformforCellular
57. Kurosaki,T.,Popp,M.W.&Maquat,L.E.Qualityandquantitycontrolof Perturbation(MPCP).WethankDr.JanuszRakforprovidingtheA172cellline.
geneexpressionbynonsense-mediatedmRNAdecay.Nat.Rev.Mol.CellBiol.
20,406–420(2019).
Author contributions
58. Clark,T.A.,Sugnet,C.W.&Ares,M.Jr.GenomewideanalysisofmRNA
processinginyeastusingsplicing-specificmicroarrays.Science296,907–910 G.P.andH.S.N.conceivedthestudy,developedthecomputationalmethods,analysedthe
data,andwrotethemanuscript.P.J.,E.M.,T.N.,andM.R.performedthemiRNA
(2002).
inhibition/mimicandRBPoverexpressionexperiments.R.A.contributedtodatapro-
59. Sayani,S.,Janis,M.,Lee,C.Y.,Toesca,I.&Chanfreau,G.F.Widespread
cessing.T.L.contributedtodeconvolutionanalyses.Y.R.contributedtoexperimental
impactofnonsense-mediatedmRNAdecayontheyeastintronome.Mol.Cell
31,360–370(2008). designanddatainterpretation.H.S.N.directedthestudy.
60. Love,M.I.,Huber,W.&Anders,S.Moderatedestimationoffold
changeanddispersionforRNA-seqdatawithDESeq2.GenomeBiol.15,550 Competing interests
(2014). Theauthorsdeclarenocompetinginterests.
61. Arango,D.etal.AcetylationofcytidineinmessengerRNA.GEO
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102113(2018).
Additional information
62. Kim,D.,Paggi,J.M.,Park,C.,Bennett,C.&Salzberg,S.L.Graph-based
genomealignmentandgenotypingwithHISAT2andHISAT-genotype.Nat. SupplementaryinformationTheonlineversioncontainssupplementarymaterial
Biotechnol.37,907–915(2019). availableathttps://doi.org/10.1038/s42003-022-03796-w.
63. Anders,S.,Pyl,P.T.&Huber,W.HTSeq–aPythonframeworktoworkwith
high-throughputsequencingdata.Bioinformatics31,166–169(2015). CorrespondenceandrequestsformaterialsshouldbeaddressedtoHamedS.Najafabadi.
64. Wang,L.,Wang,S.&Li,W.RSeQC:qualitycontrolofRNA-seqexperiments.
Bioinformatics28,2184–2185(2012). PeerreviewinformationCommunicationsBiologythanksYutakaSuzukiandtheother,
65. Carter,S.L.etal.AbsolutequantificationofsomaticDNAalterationsin anonymous,reviewer(s)fortheircontributiontothepeerreviewofthiswork.Primary
humancancer.Nat.Biotechnol.30,413–421(2012). HandlingEditors:VivianLuiandLukeR.Grinham.Peerreviewerreportsareavailable.
66. Liberzon,A.etal.TheMolecularSignaturesDatabase(MSigDB)hallmark
genesetcollection.CellSyst.1,417–425(2015). Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
67. Goodarzi,H.etal.DifferentialtranscriptstabilitymeasurementsinMDA- Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
M
acc
B
.
-
c
2
g
3
i?
1
ac
v
c
s
=
.M
GS
D
E
A
49
-L
6
M
08
2
.(
c
2
e
0
ll
1
s
4
.
)
G
.
EOhttps://www.ncbi.nlm.nih.gov/geo/query/ publishedmapsandinstitutionalaffiliations.
68. Agarwal,V.,Bell,G.W.,Nam,J.W.&Bartel,D.P.Predictingeffective
microRNAtargetsitesinmammalianmRNAs.Elife4,https://doi.org/10.7554/
eLife.05005(2015). Open Access This article is licensed under a Creative Commons
69. BioconductorPackageMaintainer(2021).liftOver:Changinggenomic Attribution 4.0 International License, which permits use, sharing,
coordinatesystemswithrtracklayer::liftOver.Rpackageversion1.19.0, adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
https://www.bioconductor.org/help/workflows/liftOver/. appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
70. Subramanian,A.etal.Genesetenrichmentanalysis:aknowledge-based Commonslicense,andindicateifchangesweremade.Theimagesorotherthirdparty
approachforinterpretinggenome-wideexpressionprofiles.Proc.NatlAcad. materialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unless
Sci.USA102,15545–15550(2005). indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
article’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutory
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
Acknowledgements
thecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/
ThisworkwassupportedbyfundsfromCanadianInstitutesofHealthResearch(PJT- licenses/by/4.0/.
155966),andresourceallocationsfromComputeCanadatoH.S.N.H.S.Nholdsa
CanadaResearchChairfundedbytheCanadianInstitutesofHealthResearch.G.P.and
R.A.aresupportedbytrainingscholarshipsfromtheCanadianInstitutesofHealth ©TheAuthor(s)2022
14 COMMUNICATIONSBIOLOGY| (2022) 5:851 |https://doi.org/10.1038/s42003-022-03796-w|www.nature.com/commsbio
