---
source_path: /mnt/c/Users/Administrator/Zotero/storage/69ECKBZD/Lambo 等 - 2023 - A longitudinal single-cell atlas of treatment response in pediatric AML.pdf
ingested: 2026-04-23
sha256: 0a74aed0fcffb2a7
---

Article
A longitudinal single-cell atlas of treatment response
in pediatric AML
Graphical abstract Authors
SanderLambo,DianeL.Trinh,
RhondaE.Ries,...,
SuzanneM.Vercauteren,
SoheilMeshinchi,MarcoA.Marra
Correspondence
mmarra@bcgsc.ca
In brief
Lamboetal.usesinglecellsequencing
analysesofclinicaltrialsamplesto
identifymolecularchangesassociated
withrelapsedpediatricacutemyeloid
leukemia.Comparedtotumorsat
diagnosis,theyfindthatrelapsedtumors
areenrichedinprimitivecellsand
typicallylosemyeloidtranscriptional
programswhileadoptingthe
transcriptionalprogramsofothercell
lineages.
Highlights
d Comprehensivesingle-cellanalysisoflongitudinally
collectedpAMLpatientsamples
d Malignantcellpopulationsassumeamoreprimitivestate
uponrelapse
d Primitivecellpopulationcharacteristicsdependonthedriver
alteration
d Transcriptionalnetworksshiftfrommyeloidtowardlymphoid
programsuponrelapse
Lamboetal.,2023,CancerCell41,2117–2135
December11,2023ª2023TheAuthor(s).PublishedbyElsevierInc.
ll
https://doi.org/10.1016/j.ccell.2023.10.008
ll
OPENACCESS
Article
A longitudinal single-cell atlas
of treatment response in pediatric AML
SanderLambo,1DianeL.Trinh,1RhondaE.Ries,2DanJin,1AudiSetiadi,3,4,5MichelleNg,1,8VeroniqueG.Leblanc,1
MichaelR.Loken,6LisaE.Brodersen,6FangyanDai,6LauraM.Pardo,6XiaotuMa,7SuzanneM.Vercauteren,3,4,5
SoheilMeshinchi,2andMarcoA.Marra1,8,9,*
1Canada’sMichaelSmithGenomeSciencesCentre,BCCancer,Vancouver,BC,Canada
2ClinicalResearchDivision,FredHutchinsonCancerResearchCenter,Seattle,WA,USA
3BritishColumbiaChildren’sHospitalResearchInstitute,Vancouver,BC,Canada
4DepartmentofPathology&LaboratoryMedicine,DivisionofHematopathology,Children’sandWomen’sHealthCentreofBritishColumbia,
Vancouver,BC,Canada
5DepartmentofPathology&LaboratoryMedicine,UniversityofBritishColumbia,Vancouver,BC,Canada
6Hematologics,Incorporated,Seattle,WA,USA
7DepartmentofComputationalBiology,St.JudeChildren’sResearchHospital,Memphis,TN,USA
8DepartmentofMedicalGeneticsandMichaelSmithLaboratories,UniversityofBritishColumbia,Vancouver,BC,Canada
9Leadcontact
*Correspondence:mmarra@bcgsc.ca
https://doi.org/10.1016/j.ccell.2023.10.008
SUMMARY
Pediatricacutemyeloidleukemia(pAML)ischaracterizedbyheterogeneouscellularcomposition,driveral-
terations and prognosis. Characterization of this heterogeneity and how it affects treatment response re-
mains understudied in pediatric patients. We used single-cell RNA sequencing and single-cell ATAC
sequencingtoprofile28patientsrepresentingdifferentpAMLsubtypesatdiagnosis,remissionandrelapse.
At diagnosis, cellular composition differed between genetic subgroups. Upon relapse, cellular hierarchies
transitioned toward a more primitive state regardless of subtype. Primitive cells in the relapsed tumor
weredistinctcomparedtocellsatdiagnosis,withunder-representationofmyeloidtranscriptionalprograms
andover-representationofotherlineageprograms.Insomepatients,thiswasaccompaniedbytheappear-
anceofaB-lymphoid-likehierarchy.Ourdatathusrevealtheemergenceofapparentsubtype-specificplas-
ticityupontreatmentandinformonpotentiallytargetableprocesses.
INTRODUCTION tiveinmultiplemyeloma,14,15myelodysplasticsyndrome(MDS)
andlow-riskaAML,16,17failedtoincreasesurvivalinpAMLpa-
Pediatric AML (pAML) is a heterogeneous disease frequently tients as shown by recent phase II clinical trials such as
driven by genomic rearrangements.1 Despite advances in pa- AAML1031.12
tientstratification,patientprognosishasnotimproved,andover- Development and evaluation of new therapeutic strategies
allsurvival(OS)ratesremainat(cid:1)75%.2,3Frequent relapsere- havebeenhamperedbyanincompleteunderstandingofthemo-
sults in event-free survival (EFS) rates of only (cid:1)50%.2,4 In lecular changes that accompany pAML relapse. While studies
contrasttoadultAML(aAML),thereisanabsenceofeffective haveinvestigatedmoleculardifferencesbetweenpAMLatdiag-
targeted therapies for most pAML cases,5 since tumors are nosisandrelapse,18–21thedistinctsubpopulationsofcellsthat
molecularlydistinctfromadultsandlacktargetabledriveralter- shaperelapsedtumorsremainunderstudied.Cellularheteroge-
ations, such as IDH.6–8 Common driving aberrations found in neityiscrucialtostudyinbothpAMLandaAMLsincethetumors
pAML include translocations involving MLL ((cid:1)20%), RUNX1 partially recapitulate normal hematopoietic development,22–24
((cid:1)15%) and CBFB ((cid:1)10%), internal tandem duplications in complicating the identification of targetable features. Consid-
FLT3((cid:1)20%;FLT3-ITD),andsinglenucleotidevariants(SNVs) ering the lack of mutations thatmight suggest a genetic basis
within CEBPA and genes involved in MAPK signaling (e.g., forrelapse9,25astudyofcellularhierarchiesinpAMLmayyield
NRASandKIT).7,9 valuable insights into how relapse in pediatric malignancies
pAML patients are typically treated using chemotherapies occurs.
such as daunorubicin and cytarabine. Additions to standard WesoughttoidentifychangesinpAMLtranscriptionalpro-
chemotherapy,suchassorafenibandmidostaurin,haveshown grams accompanying relapse, prioritizing the capture of
some effectiveness in patients harboring FLT3 alterations.10,11 cellularheterogeneitywithintumors.Toachievethis,wechar-
Theproteasomeinhibitorbortezomib(BTZ),12,13whichiseffec- acterized28patientsfromtheAAML1031trial,12representing
CancerCell41,2117–2135,December11,2023ª2023TheAuthor(s).PublishedbyElsevierInc. 2117
ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).
ll
OPENACCESS Article
A B
C
E
D
Figure1. Longitudinalsingle-cellprofilingofpediatricAML
(A)Schematicoverviewofpatientsandtimepointsincludedinthestudy.
(B)OncoplotshowingsomaticalterationsidentifiedusingWGS.
(C)UMAPrepresentationsofscRNA-seqorscATAC-seqdatafromcellsderivedfrompatientPAVJXG.Cellsarecoloredbybiopsy.
(D)UMAPrepresentationasper(C),colorsindicatedetectionofsomaticSNVswithineachcell.
(E)CopynumberprofilinginferredfromscATAC-seqdataconfirmstrisomy21inmalignantcellsfrompatientPAVJXG.Dotsrepresent10MBbins.Yaxis
representstheaveragefold-changecomparedtothepairedremissionsample.AlsoseeFigureS1,TablesS1andS2.
majorpAMLgeneticsubgroups.Thesepatientswereprofiled RESULTS
usingsingle-cellRNAsequencing(scRNA-seq)andsingle-cell
ATAC sequencing (scATAC-seq) of matched tumors at diag- Longitudinalsingle-cellprofilingofpediatricAML
nosis, remission and relapse. To characterize cellular We profiled diagnosis, remission and relapse samples from
heterogeneitybeforeandaftertreatment,weclassifiedtumor 28 pAML patients (Figures 1A, S1A, and S1B) with rearrange-
cells into distinct states of hematopoietic differentiation ments in MLL (MLL; n = 11), RUNX1 (RUNX; n = 5), CBFB
and compared cellular hierarchies between subgroups. We (CBFB; n = 4), FLT3-ITD (FLT; n = 4), and other alterations
found an enrichment of primitive states in relapsed samples, (e.g., CEBPA and NPM1 mutations; Other; n = 4). Patients
andtranscriptionalnetworkanalysisintheseprimitivepopula- wereenrolledintheAAML1031trialanduniformlytreatedwith
tions revealed that tumor-specific transcriptional programs BTZandstandardchemotherapy,exceptforpatientsharboring
and developmental priming may occur in response to FLT3-ITDalterations,whoweretreatedwithsorafenibandstan-
treatment. dard chemotherapy (Table S1). For 24 patients, previously
2118 CancerCell41,2117–2135,December11,2023
ll
Article OPENACCESS
A
B C
D
E F
(legendonnextpage)
CancerCell41,2117–2135,December11,2023 2119
ll
OPENACCESS Article
generated whole-genome sequencing (WGS)data9allowedus marked it by recapitulating the annotations of the reference
toidentifysomaticmutationsanddriveralterations(onaverage (Figure S2B) with 5-fold cross-validation as previously
236SNVsgenome-wide;Figure1B;TableS2).Whileweidenti- described22,28(FigureS2C;TableS3).Misclassificationsmostly
fiedmutationspreviouslylinkedtorelapse(e.g.,WT1andTP53 occurredincloselyrelatedcelltypesofthesamelineage(Fig-
mutations), most patients had no obvious genetic basis for ureS2D).Whenperformingsupervisedclustering,using30iden-
relapse.18 We thus sought other correlates of relapse in tran- tifiedmarkergenesforeachcellpopulation(TableS3),wefound
scriptomeandepigenomeprofiles.Wegenerated146libraries thatevencelltypeswithsimilarexpressionpatterns,whichcan
from 75 blood and peripheral blood biopsies at different time- bedifficulttodistinguishusingmarkergenesalone(e.g.,HSCs
points, which yielded data for 684,031 high-quality cells (Fig- andprogenitorcells),wereproperlyidentifiedusingourclassifier
ureS1A;STARMethods).Cellsderivedfromtumorsatdiagnosis (FigureS2E).
andrelapseclusteredseparatelyinallcases(Figure1C).Toiden- We next performed cell type projection and classification of
tifymalignantandnon-malignantclustersofcells,weusedthe themalignantcellsatdiagnosistoidentifysubgroup-specificdif-
scATAC-seqandscRNA-seqdatatoscorecellsforthepresence ferences in pAML cell type composition (Figure 2A). We
of somatic mutations previously identified using WGS data. observeddistinctcellularhierarchiesbetweenthedifferentsub-
Clusters of cells relatively abundant in mutation-bearing cells groups:MLL-rearrangedtumorsresembledmorematurecells;
wereinferredtobemalignant(Figures1DandS1C–S1N;STAR RUNX1-rearranged tumors were enriched for progenitor-like
Methods).Wealsoinferredcopynumberalterations(CNAs)us- and early GMP-like populations; CBFB-rearranged tumors
ingthescATAC-seqdata,26whichconfirmedthepresenceoftu- wereenrichedinmonocyte-likeandprimitivecells,andtumors
mor specific CNAs in the inferred malignant cells (Figure 1E, with FLT3-ITD alterations were enriched for HSC-like popula-
STARMethods). tions,similartoaAML.22Toensurethattheinferredcellpopula-
tionswerenotbiasedbypatient-specificfeatures,weperformed
PediatricAMLtumorshavesubgroup-specificcelltype thesameanalysisonnon-malignantcellsfrommatchedremis-
compositions sionsamplesandfoundthatthedistributionswerecomparable
With malignant cells identified, we next sought to specifically betweensubgroups(FigureS2F).
characterizemalignantcellprofiles.Leukemiacellsexistinhier- To extend these observations into a larger population, we
archiesthatresemblenormalhematopoieticdevelopment,22–24 analyzed 974 patients enrolled in AAML1031 using bulk RNA-
andthereforeweusedthescRNA-seqdatatoclassifymalignant seq data (Table S1; Figure 2B). Using marker genes identified
cells from each patient according to the hierarchy they most from normal bone marrow (Table S3), we calculated signature
closely resembled and compared these hierarchies across scores across samples using gene set variation analysis
pAMLsubgroups.Weusedareferenceofnormalbonemarrow27 (GSVA)30 and observed patterns similar to those observed in
(FigureS2A)toannotatecellsaccordingtotheirsimilaritytohe- scRNA-seq data (Figure 2C). Using a flow cytometry panel of
matopoietic cell types via three complementary methods: (1) 15 markers commonly used to diagnose pAML (Figure S2G),
identification of marker genes, (2) generation of a machine weprofiledasubsetof789tumorstoconfirmourobservations.
learning-basedcelltypeclassifier,28and(3)projectionofcells29 MLL-rearrangedtumorsindeedshowedlowsurfaceexpression
ontothereference(STARMethods). ofbothCD34andCD117,whicharecommonlyusedtoidentify
Using the normal bone marrow reference, we identified 30 primitive populations, but abundantly expressed the myeloid
markergenesforcelltypescommonlyfoundinAML,22including markers CD11b and CD3331 (Figure 2D). Both CD34 and
granulocyte-monocyteprogenitors(GMPs)andmonocytes,and CD117surfaceexpression correlated withtheHSC-like signa-
primitivepopulations,suchashematopoieticstemcells(HSCs), turescorederivedbyGSVA(Figure2E).Therelativeabundance
andearlyprogenitors.Wealsoidentifiedmarkergenesinline- of primitive cells has been shown tobe predictive of outcome
age-committed progenitors of non-monocytic cell types, within AML.32,33 Therefore, we tested whether abundance of
including common lymphoid progenitors (CLPs), early erythro- primitive signatures within each subgroup was predictive of
cytesandnaiveTcells(TableS3). outcome and found that, especially within the more differenti-
Toenhancecell-typeidentification,wetrainedaclassifierus- ated MLL subgroup, higher expression of primitive markers
ingmachinelearningonthenormalbonemarrow28andbench- correlatedwithinferioroutcomes(Figure2F).
Figure2. PediatricAMLtumorshavesubgroupspecificcelltypecompositionsatdiagnosis
(A)Projectionofmalignantcellsfromtumorsatdiagnosisontoahealthybonemarrow.27ColorsonthereferenceUMAPdenoteannotatedcelltypes.Cells
projectedonthereference,foreachsubgroup,weresummarizedintohexagonswiththecolordenotingthenumberofmalignantcellswithineacharea.Bars
underprojectionssummarizecelltypeassignmentsfromtheclassifiertrainedonnormalbonemarrow.
(B)Overviewof974patientsprofiledusingbulkRNA-seq.Circlesdepict,frominnertoouterring,thegeneticsubgroup,treatmentarmandoutcomeofeach
patient.
(C)SupervisedclusteringofbulkRNA-seqdatafrom422samplesatdiagnosiswithblastcellcontent>40%.UpperpanelshowsGSVA-derivedsignaturescores
forindicatedcelltypes,inferredusingmarkersidentifiedinnormalbonemarrow(TableS3).Lowerpanelshowsnormalizedgeneexpressionvaluesforthesame
markers.
(D)Log10-transformedmeanfluorescenceintensity(MFI)valuesofmarkers,measuredusingflowcytometryfrom789tumorsatdiagnosis.
(E)SpearmancorrelationofHSC-likeGSVAsignaturescoresandmeanfluorescenceofCD34andCD117from782patientswithbothbulkRNA-seqandflow
cytometrydata.
(F)Kaplan-Meiercurvesshowingfive-yearOSandfive-yearEFSforallpatientsorpatientscategorizedbysubgroup.Forsubgroupcomparisons,sampleswitha
blastcellcontent>40%wereincludedandsplitbyHSCsignaturescores(high=top50%;low=remaining50%).AlsoseeFigureS2,TablesS1andS3.
2120 CancerCell41,2117–2135,December11,2023
ll
Article OPENACCESS
A
B C
D F
E
G H
(legendonnextpage)
CancerCell41,2117–2135,December11,2023 2121
ll
OPENACCESS Article
Cellularhierarchiesareenrichedforamoreprimitive lignantremissioncells(n=60,531),derivedfromallsamples,to
stateuponrelapse placeinferredtranscriptionalnetworkswithinmalignantcellsin
Given the correlation between primitive populations and thecontextofnormalhematopoiesis(FigureS4A).Wefirstiden-
outcome, we investigated how cellular hierarchies changed tifiedopenchromatinpeaksandtheninferredTFbindingusing
upon relapse. We identified distinct cellular compositions be- motifenrichmentinthesepeakregionsacrossallcells.Toiden-
tween tumors at diagnosis and relapse using both the normal tify processes upregulated in myeloid, lymphoid, and erythro-
bone marrow27 (Figures 3A, S3A, and S3B) and a fetal bone cytic lineages, we identified differentiation trajectories using
marrow34(FigureS3C).GMP-likecellsandearlymonocytesap- Monocle36and determinedthelinkedgeneexpression andTF
peared depleted upon relapse, particularly in subgroups with motif enrichment in peaks along the trajectory (Figure S4B).
relatively high levels of GMPs at diagnosis, such as the MLL Linked geneexpression confirmed the gradualupregulation of
and RUNX subgroups (Figure 3B). Meanwhile, cellular hierar- knownlineagemarkers(FigureS4B),andmotifsofmasterline-
chiesinrelapsedtumorsweresimilarlyenrichedinprimitivecells age-determining TFs (CEBPA for myeloid,37,38 TCF3 (E2A) for
acrosssubgroups,includingtheMLLsubgroupwhichcontained lymphoid39andGATA1forerythrocytic40)wereenrichedinthe
moredifferentiatedcellsatdiagnosis(Figure3C). respectivelineages(FigureS4C).41–43Motifsofthestemcellfac-
To study the distinct shifts in cellular hierarchies within the torsRUNX1andCBFBwerealsoenrichedintheHSC-likepop-
MLL subgroup, we directly compared all biopsied cells for ulation,44suggestingthatourinferredlineagetrajectoriesresem-
eachpatient(Figure3D).Therelapsesamplescontainedsignifi- bled normal hematopoiesis. We extended this approach to
cantly more cells expressing HSPC markers (i.e., CD34 and identifythefullspectrumofTFspotentiallyinvolvedineachline-
IGLL)andfewercellsexpressingGMPandmonocytemarkers agebycomparingTFexpressionandmotifenrichmenttoHSPC-
(i.e.,ELANEandS100A9)(Figure3E),apatternwhichwasvisible likecells(FigureS4D).OuridentifiedTFsweregenerallyspecific
throughout the markers identified in each cell population from totheircorrespondinglineageanddownregulatedinotherline-
normal bone marrow (Figure 3F; Table S3). Interestingly, cell ages(FigureS4E),characteristicsthatweleveragedtoidentify
type markers were among the most differentially expressed changesinmalignanttumorpopulations.
genes between diagnosis and relapse. In particular, the MLL
and RUNX subgroups showed marked downregulation of Transcriptionalnetworksinrelapsedtumorstransition
myeloidmarkersuponrelapse(Figure3G;TableS4).Toconfirm awayfromthemyeloidlineage
theincreaseinprimitivecellsuponrelapse,flowcytometrywas Having identified TF expression and inferred activity along es-
used to analyze matched diagnosis and relapse sample pairs tablishedlineagesinnon-malignantcells,wecomparedmalig-
fromMLL-rearrangedtumors.Indeed,anincreasedproportion nant cells from each diagnostic and relapse pair. First, we
of CD34+cells and CD117+ cellswas observed in the relapse used linked expression data to annotate malignant cell types
samples compared to the matched samples at diagnosis (FiguresS5AandS5B),confirmingtheshifttowardmoreprimi-
(Figures3HandS3D–S3F). tive cell states in the relapsed tumor within scATAC-seq data
(Figure4A).Weidentifieddifferentiallyenrichedopenchromatin
Identifyinglineage-associatedtranscriptionalnetworks peaks between malignant cells from paired diagnosis and
To identify transcriptional changes underlying the identified relapse samples (Figure 4B)45 and performed TF motif enrich-
shiftsincellpopulations,weusedthescATAC-seqdatatoinfer mentanalysistoinferdifferencesinTFactivity(Figure4C).46,47
theactivityoftranscriptionfactors(TFs)withintumorcells.First, InMLL-rearrangedrelapsedsamples,weobserveddecreased
weidentifiedcellpopulationswithinscATAC-seqdatabyinfer- activity of CEBP TFs and their dimerization partners, such as
ring gene expression from open promoters and linking this to ATF/CREB,MAFandAP-1TFs(Figure4D).Theseheterodimers
scRNA-seq derived gene expression data,29,35 allowing us to arepivotalinmyeloidcellfatespecification,37,48supportingour
transfer cell type classifications (STAR Methods). We applied finding that myeloid cells were diminished upon relapse.
thismethodtoareferencecontroldatasetconsistingofnon-ma- Conversely,CBFcomplexactivityappearedtobegainedupon
Figure3. Cellularhierarchiesareenrichedforamoreprimitivestateuponrelapse
(A)Projectionofmalignantcellsfromrelapsedtumorsontoahealthybonemarrow.27ColorsonthereferenceUMAPdenoteannotatedcelltypes.Cellsprojected
onthereference,foreachsubgroup,weresummarizedintohexagonswiththecolordenotingthenumberofmalignantcellswithineacharea.Barsunder
projectionssummarizecelltypeassignmentsfromtheclassifiertrainedonnormalbonemarrow.Colorlegendasin(F).
(B)ComparisonofthepercentageofmalignantcellsclassifiedasGMP-likeinmatcheddiagnosis(Dx)andrelapse(R)samplesforeachsubgroup.
(C)Densityofprojectedcellsfromtumorsatdiagnosisandrelapseonthereference,separatedbysubgroup.
(D)UMAPrepresentationofallcells(diagnosis,relapse,andremission)fromPAVDYE(MLLsubgroup).Colorsindicatecelltypesasassignedusingthehighest
predictionscorefromourclassificationapproach.Colorlegendin(F).
(E)UMAPrepresentation(D)coloredbyexpressionofCD34,IGLL1,ELANE,andS100A9.Violinplotsshownormalizedexpressionvaluesforthesegenesin
malignantcellsfromtumorsatdiagnosisandrelapse.AdjustedpvalueswerecalculatedusingBenjamini-Hochberg(BH)-correctedtwo-sidedWilcoxontests.
(F)Heatmapshowingexpressionofmarkergenes(TableS3),withcellssortedbycelltypeandclassificationscore(upperpanel).Middlebarshowsbiopsy
timepoint.Lowerpanelshowsclassificationscores.BarunderclassificationscoresshowsdetectionofsomaticSNVsidentifiedinmatchedWGSdatain
eachcell.
(G)Differentialgeneexpressioncomparingcellsfrommatchedtumorsforeachsubgroup.AdjustedpvalueswerecalculatedusingMASTandcorrectedusing
BH.Diagnosisandrelapsecellsweredownsampledto1,000cellstocorrectforoverlysmallpvalues.
(H)FlowcytometryofsurfaceexpressioninblastsfrommatchedsamplesatdiagnosisandrelapsefromPAVDYE.DistributionofMFIvalues(left),densitycontour
plotsoverlayingthematchedpair(middle),andhistogramsoverlayingCD34andCD117signals(right)areshown.GatingstrategyisdetailedinFigureS3D.Also
seeFigureS3,TablesS3andS4.
2122 CancerCell41,2117–2135,December11,2023
ll
Article OPENACCESS
A B C
D E
25 50 75
F G H
Figure4. Transcriptionalnetworkstransitionuponrelapse
(A)UMAPrepresentationofdimensionalityreductionusingiterativeLatentSemanticIndexing(LSI)ofscATAC-seqprofilesfromPAVJXG(MLLsubgroup).Cells
arecoloredbybiopsy(left)andinferredcelltypebasedonlabeltransferfrommatchedscRNA-seqdata(right).Inferrednon-malignantcellsaregreyedout(left).
(B)Volcanoplotshowingpeaksdifferentiallyenrichedbetweenmalignantcellsatdiagnosisandrelapse.Falsediscoveryrate(FDR)valueswerecalculatedusing
two-sidedWilcoxontestscorrectedfortranscriptionstartsite(TSS)biasfollowedbyBHcorrection.
(C)TFmotifenrichmentcalculatedbetweenpeaksenrichedindiagnosisorrelapsesamples.HypergeometrictestsfollowedbyBHcorrectionwereappliedto
calculateadjustedpvalues.
(legendcontinuedonnextpage)
CancerCell41,2117–2135,December11,2023 2123
ll
OPENACCESS Article
relapse,aswerefactorsfoundinprimitivecellsandlymphoidlin- tively.Theco-regulatedclusterwasenrichedformyeloidspeci-
eagessuchasLMO2,LYL1,TCF12,andEBF1.42,49–51Wefound ficationfactors(e.g.,CEBPfamilymembersandSP1),whilethe
subgroup-specificshiftsfromdiagnosistorelapse:CBFfactors anti-regulatedclusterwasenrichedforlymphoiddifferentiation
wereupregulatedinMLL-rearrangedtumors,STATfactorswere factors(e.g.,TAL1,LYL1,andTCF12)andTFsthatareenriched
upregulated in RUNX1-rearranged tumors and AP-1 factors inHSPCs(e.g.,RUNX1,RUNX2,andGATA2)(FiguresS4Dand
wereupregulatedinRUNX1-andCBFB-rearrangedtumors(Fig- S4E).42–44 Factors whose inferred activity correlated with that
ureS5C).AP-1factorshavebeenimplicatedascofactorsofthe ofRELA,suchasCEBPA,weredownregulatedtoasimilarextent
fusionproteininRUNX1-RUNX1T1-relatedmalignancies,52indi- as RELA upon relapse, while anti-correlated factors, such as
catingthattheirincreasedactivityuponrelapsemaybefunction- TCF factors, showed similar or slightly elevated activity (Fig-
ally related to the driver alteration in RUNX1- and CBFB-rear- ure 4H). These results support the notion that NF-kB factors
rangedtumors.Somefactorssharedsimilarpatternsacrossall maybeco-regulatedwithmyeloiddifferentiationinpAML.
subgroups:CEBPactivitywaslostandTCFactivitywasgained SincecorrelationbetweenNF-kBsignalingandmyeloiddiffer-
at relapse compared to diagnosis. To further examine this entiationmaybebiasedbytumor-specificexpressionpatterns,
apparent shift in TF activity, we inferred trajectories from we investigated this relationship in non-malignant remission
matched diagnosis and relapsed tumor cells to determine samples along inferred lineage trajectories (Figure S4F). Along
gradual changes in lineage marker expression, TF expression themyeloidaxis,weobservedincreasedactivityofNF-kBfac-
andTFmotifenrichment(Figure4E).Weconfirmedthatmyeloid tors toward the center of the trajectory (corresponding to
lineagemarkers(MPO,LYZ,ELANE,andS100A)weredownre- GMPsandpromonocytes)butreducedactivityintheHSPCpop-
gulatedandtheactivityofTFsinvolvedinmyeloidspecification ulation(FigureS4G).Inthelymphoidanderythroidtrajectories,
(RARA and CEBPA)37,53 were lost upon relapse. Conversely, inferred NF-kB activity gradually decreased during differentia-
markersforlymphoidanderythroidcells(CD9andGATA1)and tion from HSPCs (Figure S4G). Furthermore, expression of
HSPCs(CD34andSPINK2)andinferredactivityofTFsinvolved both canonical (RELA and NFKB1) and non-canonical (RELB
in primitive cells and lymphoid specification, such as RUNX1, and NFKB2) NF-kB signaling factors were reduced in HSPCs
GATA2,MEF2C,andTCF3,wereelevatedincellsfromrelapsed compared to myeloid cells (Figure S4H). Therefore, despite
tumors.41–43 elevated NF-kB expression and activity in pAML blasts
comparedtonormalbonemarrow,27NF-kBmaynotbeaneffec-
tivetherapeutictargetinpAMLsincetheexpressionandactivity
Potentialtherapeutictargetsarerestrictedtospecific
ofthepathwayarerestrictedtomoredifferentiatedmyeloidcells
cellularlineages
butaregenerallylowerinprimitivecellsandotherlineagesthat
We next explored whether shifts in cell populations between
are present upon relapse.33,57 Indeed, knockout of RELA in
diagnosis and relapse could explain the lack of response to
mousemodelshasbeenshowntocauseashiftincellpopula-
BTZintheAAML1031trial.OnerationaleforadministeringBTZ
waspotentialinhibitionofNF-kBsignaling,54,55whichisconsti- tions toward more primitive fates,58 resembling the shifts we
tutivelyactiveinAMLblasts.56Wecomparedexpressionandin- observedbetweendiagnosisandrelapsesamples.
ferred activity of TFs involved in NF-kB signaling (e.g., RELA,
RELB, and NFKB1) and found both elevated expression and Primitivecellsinrelapsedtumorsshowlessmyeloid
motifenrichmentatdiagnosisbutdepletionuponrelapse(Fig- priming
ure4F).Toidentifyfactorspotentiallyco-regulatedwithNF-kB SinceNF-kBactivityappearsdepletedinthemoreprimitivecell
signaling,wecorrelatedmotifenrichmentscoresforRELAand populations in relapsed tumors, we wondered whether there
otherTFsintheCisBPdatabaseacrossmalignantandnon-ma- wereotherdifferentiallyactivegenesortranscriptionalprograms
lignantcells.Hierarchicalclusteringofthesecorrelationsidenti- betweenmalignantHSPC-likecellscomparedtonon-malignant
fiedfactorswithsimilarordistinctpatternsinmotifenrichment HSPC-likecellsthatcouldbecandidatesfortargetedtherapy.
compared to TFs involved in NF-kB signaling (Figure 4G), Tothisend,wecombinednon-malignantcellsthatwereclassi-
implying co- or anti-regulation with NF-kB signaling, respec- fiedasHSPC-likefromallremissionsamplesintoasinglecluster
(D)NetworkofdifferentiallyenrichedTFBSmotifsbetweentumorsatdiagnosisandrelapseintheMLLsubgroup.TFsweregroupedbasedonannotationsinAssi
etal.65andlinesdenoteinteractionsinferredbystringDB.90OnlyTFsexpressedin>10%ofcellsandwith-log10pvalues>10ineitherdiagnosisorrelapse
samplesareshown.HypergeometrictestsfollowedbyBHcorrectionwereappliedtocalculateadjustedpvalues.
(E)Topleft:UMAPshowingatrajectoryinferredusingMonocle,36projectedoncellsfromtumorsatdiagnosisandrelapse(PAVJXG).Lowerleft:scRNA-seq
derivednormalizedexpressionofprimitive(yellow),myeloid(blue),lymphoid(green),anderythroid(pink)markersalongthetrajectory(expressionsmoothed
usingLOESS).Right:HeatmapsshowscaledTFmotifenrichmentscores(calculatedusingChromVAR;deviationscore)andscalednormalizedscRNA-seq
basedgeneexpressionvaluesforcorrespondingTFsalongthetrajectory.OnlyTFswheremotifenrichmentcorrelatedwithgeneexpression,asdeterminedby
quantileregression(r>0.5),areshown.
(F)UMAPprojectionofdiagnosisandrelapsecellscoloredbynormalizedgeneexpressionvalues(left)andTFmotifenrichment(right)offactorsbelongingtothe
NF-kBpathway.
(G)GlobalSpearmancorrelationsofTFmotifenrichmentscoresinbothmalignantandnon-malignantcells(PAVJXG).OnlyTFmotifscorrelatedoranti-correlated
withRELAareshown.Blueandgreenclustersarecomposedoffactorswhoseinferredactivityiscorrelatedoranti-correlatedwithNF-kBactivity,respectively.
RedclusteriscomposedoffactorsrelatedtoNF-kBactivity.Upperright:analysisofregressionbetweenRELAandCEBPAmotifenrichments.Eachdotdepictsa
singlecell,coloredbykerneldensityestimation.
(H)VisualizationofcombinedscATAC-seqprofilesofallmalignantcellsfromtumorsatdiagnosis(red)andrelapse(blue)in400bpregionsflankingTFBSmotifs.
TCF12wasincludedtocontrasttheprofilesaroundCEBPAandRELAmotifs.AlsoseeFiguresS4andS5.
2124 CancerCell41,2117–2135,December11,2023
ll
Article OPENACCESS
A B
C
D F G
E
Figure5. MalignantHSPCshavealteredtranscriptionalnetworksuponrelapse
(A)UMAPrepresentation(scRNA-seq)ofHSPC-likecellsfromallpatients.Cellsarecoloredbypatient.Outlinesshowmalignantcellsfromtumorsatdiagnosisor
relapseornon-malignantHSPCs(NH).Coloredlinesdenotesubgroups.
(legendcontinuedonnextpage)
CancerCell41,2117–2135,December11,2023 2125
ll
OPENACCESS Article
that we used for comparison to malignant HSPCs, leveraging towardthemyeloidlineageand,intheMLLandCBFBsubgroup,
both the scRNA-seq (Figure 5A) and scATAC-seq (Figure 5B) weredevoidofunprimedHSPCs,whicharepresumedtobemul-
data. We rationalized that non-malignant HSPC-like cells from tipotent(FigureS6G).Whilethenumberofsamplesfrompatients
remissionsampleswouldbeasuitablecomparisontoidentifytu- thatdidnotrelapseissmallinourcohort(n=4),ourresultsare
mor-specifictranscriptionalprogramsinmalignantpopulations consistent with the finding that HSC signatures are especially
becausethecellsexperiencedthesametreatmentasrelapsed predictiveintheMLLandCBFBsubgroups(Figure2F).These
HSPC-likecells. datasuggestthatHSPCsinrelapsedtumorsaremoremultipo-
We first developed an approach to assess whether lineage tentthanthosefoundatdiagnosis,consistentwithpreviousfind-
priming of HSPC-like cells was similar between different sub- ingsthatprimitivemultipotentcellsaremorechemoresistantand
groupsandbetweendiagnosisandrelapsestates,usingthedif- aremorelikelytodominateinrelapsedtumors.33,57
ferentiation trajectories we previously inferred from matched
non-malignant remission samples (Figures S4A and S6A). For HSPC-likepopulationsshowdistinctchromatinstates
eachlineage,weidentifiedthe5,000mostvariablepeakswhose basedondriveralterations
accessibilitywasincreasedcomparedtotheHSPCpopulation Theshiftin‘‘priming’’betweendiagnosisandrelapsedtumorsin
(Figure S6B; Table S5). Based on these peaks, we calculated HSPC-likecellsindicatesthatlongitudinalchangesinopenchro-
myeloid, lymphoid, and erythroid scores for each cell, which matinoccurredwithinasubpopulationofcells,distinctfromse-
correlated with the inferred activity of the respective lineage- lection-relatedshiftsduetolineagerestrictedexpression(e.g.,
determining TFs (Figure S6C), and calculated the fold change activity of NF-kB in myeloid cells). Important oncogenes in
over the median in HSPCs to infer bias or ‘‘priming’’ toward a pAMLsuchasMEIS1,adownstreamtargetof theMLLfusion
lineage (Figure S6D; STAR Methods). These scores were anti- oncoprotein,59 are aberrantly activated within malignant cells
correlated between each lineage (Figure S6E). Thus, this comparedtonon-malignantcells.However,incontrasttoNF-
approachcapturedthegradientoftranscriptionalstatesduring kBsignaling,MEIS1isalsoupregulatedinspecificsubpopula-
lineage commitment acrossthreelineages,inaway thatdoes tions such as HSPC-like populations (Figure 5D). To identify
notdependonpriorknowledgeofTFnetworksthatcouldpoten- other important factors that are aberrantly activated within
tiallybeinfluencedbydriveralterations. HSPC-likepAMLcells,weusedanapproachakintotheidenti-
Weusedthisapproachtoassesslineage‘‘priming’’inmalig- fication of super-enhancers, which are enhancer regions
nant HSPC-like populations across different subgroups and stitched together and ranked by TF activity.60 We rationalized
identify potential differences between diagnosis and relapse that increased chromatin accessibility typically results from
samples. Cells were considered ‘‘primed’’ toward the lineage higherTFactivity,andthusscATAC-seqpeakscanbegrouped
forwhichtheyscoredhighest(Figures5BandS6F).Compared togetherinasimilarfashiontoidentifyenrichedopenchromatin
tonon-malignantHSPCs,pAMLHSPCswere‘‘primed’’toward regions(eOCRs)withinmalignantHSPCpopulations(TableS6;
themyeloidlineagetoanextentwhichdependedonthedriving STARMethods).Similarlytosuper-enhancers,genesassociated
alteration(Figure5C).Consistentwiththecellularhierarchiesof witheOCRs(i.e.,thosethatcorrelatedwiththeaccessibilityofan
each subgroup at diagnosis (Figure 2), HSPC-like cells from eOCR within 250kb; n = 3,457) were typically more highly ex-
MLL-rearranged tumors exhibited stronger ‘‘priming’’ toward pressed than those that were not associated with eOCRs
the myeloid lineage, compared to RUNX-rearranged or FLT3- (n = 25,713) (Figure 5E), supporting the regulatory relevance
ITDtumors.Uponrelapse,allsubgroupsexhibitedashiftinline- ofeOCRs.
age scores toward a more balanced distribution between Weclustered the ATACsignal of eOCRs that were linked to
myeloid, lymphoid and erythrocytic ‘‘priming’’ (Figure 5C). expression of a nearby gene (Figure 5F) and identified seven
HSPCsfrompatientsthatdidnotrelapsewerestronglyaligned clusters largely consistent with the different driver alterations
(B)UMAPrepresentation(scATAC-seq)ofHSPC-likecells,determinedusinglabeltransfer,fromallpatients.Cellsarecoloredbypatient.Outlinesshowma-
lignantcellsfromtumorsatdiagnosisorrelapseornon-malignantHSPCs(NH).
(C)CircularrepresentationofscATAC-seq-derivedlineagescores(seealsoFigureS6)inNHandmalignantcellsfromdiagnosisandrelapsetumors,separatedby
geneticsubgroup.ScoreswerecalculatedforindividualcellsbydividingtotalATACreads(insertions)inlineage-associatedpeaksbytotalinsertionsinpeaks
associatedwithotherlineages,comparedtothemedianscoreacrossthe4,983non-malignantHSPC-likecells.Cellsarecoloredbythehighestscoringlineage.
(D)CombinednormalizedinsertionsaroundtheMEIS1locusinHSPC-likeandnon-HSPC-likepopulationsfromPAVJXG,comparedbetweennon-malignant
remissioncellsandmalignantcellsprofiledatdiagnosis(Dx)andrelapse(R).AnnotationsshowpeakscalledinscATAC-seqdata,enrichedopenchromatin
regions(eOCR)andcorrelationsbetweentheATACscoreineachpeakandMEIS1expression.Linesareshadedbythestrengthofthecorrelation.Correlations
>0.5areshown.
(E)Untransformedexpressioncountsofgenesthatare(n=3,457)andarenot(n=25,713)associatedwitheOCRsinnon-malignantandmalignantHSPC-likecells
fromallpatients.pvalueswerecalculatedusingatwo-sidedWilcoxontest.
(F)Unsupervisedclusteringofinsertionswithinthe1,000mostvariableeOCRswithanassociatedgenewithin250kb(left),andgeneexpressionoftheassociated
genes(right).Columnsdepictconstituentcells(n=1,000),formedbymedianprofilesof100similar(asdefinedbynearestneighbor)HSPC-likecells,hierarchically
clusteredusingEuclideandistanceandcompletelinkage.Theannotationofeachconstituentcell(i.e.,patient,geneticsubgroupandbiopsy)wasdeterminedby
theannotationofthemajoritycellsthatformedit.Themedianmyeloidprimingscore(asshownin(C))wascalculatedacrossthe100cellsthatformedthe
constituent.eOCRannotationsshowwhethertheregionoverlapswithanyofthelineage-associatedpeaks(FigureS6).
(G)Volcanoplotsshowingthedifference(log2foldchange)innormalizedinsertionswithineOCRsbetweenHSPC-likecellsatdiagnosisandrelapseforMLL
relatedeOCRclusters.eOCRsarecoloredbywhethertheeOCRoverlappedlineage-associatedpeaks.FDRswerecalculatedusingtwo-sidedWilcoxontests
followedbyBHcorrection.AlsoseeFigureS6,TablesS5andS6.
2126 CancerCell41,2117–2135,December11,2023
ll
Article OPENACCESS
A B C
D
E
F G I
H
Figure6. RegulationofeOCRsdiffersaccordingtogeneticdriveralteration
(A)7-wayVenndiagram(top)showingoverlapbetweeneOCRsthatwereupregulatedcomparedtonon-malignantHSPCs(log2foldchange>1.5,-log10FDR
<0.001)ineachcluster(Figure5F).LowerdiagramshowsthenumberofclusterseacheOCR(n=2,398)isupregulatedin.
(legendcontinuedonnextpage)
CancerCell41,2117–2135,December11,2023 2127
ll
OPENACCESS Article
found in our cohort: RUNX (1) and CBFB tumors (2) formed specifying peaks within each subgroup (Figure S6I). For
distinct clusters while the MLL subgroup formed rearrange- example,inclusters2,3,and4,drivenbyCBFBandMLLrear-
ment-specificclusters,includingMLL-AFF3(3),MLL-AF10and rangements, a high proportion of eOCRs overlapping myeloid
other rearrangements (4),and MLL-AF9 (5) clusters.The other lineage-definingpeakswereupregulatedinmalignantcompared
twoclusterswereformedbyonepatientwithbothaFLT3-ITD to non-malignant HSPCs. In contrast, in clusters 6 and 7, few
alteration and a NPM1 mutation and one patient with a eOCRsoverlappedpeaksofanylineage,indicatingthateOCRs
NAP1L1-AF10 rearrangement (6), and the last cluster was implicatedindifferentiationareregulatedinasubgroupspecific
composed of non-malignant HSPCs, other FLT3-ITD cases manner.
andaCEBPA-mutanttumor(7;TableS1).Consistentwithprevi- To identify TFs potentially binding in eOCRs, we analyzed
ousreportsdescribingsuper-enhancersneargeneswhoseac- TFBSenrichmentusingscATAC-seqpeaksthatoverlappedup-
tivity is enriched in distinct pAML subgroups,61,62 we found regulated eOCRs in malignant HSPCs (Table S7). Two sets of
eOCRsnearHOXA9,MEIS1,andZEB2thatdisplayedincreased related factors emerged from comparing the most enriched
accessibility in MLL-rearranged tumors, while eOCRs near TFBSsineachcluster.AP-1-relatedsiteswereenrichedinclus-
ASXL1, ATF3, and GATA2 were more accessible in RUNX or ters1,2,3,6,and7,whileMEF,ARID,andFOXsiteswereen-
CBFB tumors (Figure 5F). eOCRs tended to cluster by patient riched in the MLL driven clusters 3, 4, and 5 (Figures 6B and
ratherthanbyrelapsestatus,indicatingthatdifferencesinregu- 6C), consistent with reports implicating MEF factors as the
lationwerepatient-specificandnotrelatedtotherelapsestate. main drivers of the oncogenic network in MLL-rearranged tu-
However, when comparing eOCRs between diagnosis and mors,63,64whileAP-1hasbeenassociatedwithotherpAMLsub-
matchedrelapsesamples,ATACsignalsforeOCRsoverlapping groups.65Coincidentally,MEFfamilymemberMEF2Cwaspri-
lymphoid lineage-associated peaks were enriched at relapse, marily expressed in HSPCs from MLL tumors, while AP-1
while eOCRs overlapping myeloid specification peaks were familymemberJUNwasprimarilyexpressedinHSPCsfromtu-
depleted (Figures 5G and S6H). These results indicate that morslackingMLLrearrangements(Figure6D).
reduced myeloid priming is common in relapse samples, but Compared to diagnosis samples, MEF2C expression
the regulatory mechanisms thatunderlie thisreduction appear increasedwhileJUNexpressiondecreasedatrelapse(Figure6E).
tovarybetweenpatientsanddepend,tosomeextent,ontheal- Withinthecontextofhematopoiesis,MEF2Cregulatesthedeci-
terationsdrivingthetumor. sionbetweenmyeloidversuslymphoidfatebypotentiallydown-
regulatingCEBPfactors,66whileAP-1drivesmyeloidprimingin
DistinctpatternsofeOCRregulationassociatedwith conjunction with CEBP factors.52,67 Since we observed
differentdriveralterations decreased myeloid priming in malignant HSPC-like cells upon
We next investigated how eOCR accessibility differs between relapse, we investigated whether MEF2C and JUN may be
malignant and non-malignant HSPCs and how regulation of involved in regulating myeloid priming in the context of treat-
those regions compares across subgroups. Across the seven ment-resistantHSPCs.Indeed,AP-1andCEPBmotifenrichment
clusters(Figure5F),weidentified2,398eOCRswithincreased correlatedwithmyeloiddifferentiation(definedusingthemyeloid
accessibility compared to non-malignant HSPCs (Figure 6A; score described previously) across all HSPCs (Figure 6F;
TableS6).Ofthese,themajority(59.4%)wasupregulatedina Table S8); however,wedidnot observe stronganti-correlation
singleclusterandnonewerecommonlyupregulatedinallclus- between myeloid scores and MEF2C motif enrichment, likely
ters. Since the clusters mostly corresponded to the different duetoredundancyinMEFmotifs68(Figures6CandS4D).There-
driveralterations(Figure5F),itappearsthatmalignancy-associ- fore, to further investigate the role of MEF2C withinpAML, we
ated regulatory changes in HSPC-like populations differs pre- usedMEF2CChIP-seqdatafromapAMLcellline64anddeter-
dominantlyasaresultofthegeneticbackground.Similarly,ge- minedthatMEF2Cbinding wasindeed enrichedin openchro-
netic background may influence lineage definition, as shown matin regions containing MEF2C motifs (Figures S7A–S7C),
by the proportions of upregulated eOCRs overlapping lineage including promoters of proposed downstream factors such as
(B)UpperheatmapshowsdifferencesinTFmotifoccupancy(percentageofpeakscontainingamotif)incluster-specificeOCRs.Differenceswerecompared
betweenTFmotifoccupancyinpeaksoverlappingupregulatedeOCRsineachclusteragainstpeaksoverlappingeOCRsupregulatedinotherclusters.Theunion
ofthetop10TFswiththelargestdifferencesineachclusterisshown.Lowerheatmapshowsadjustedpvaluescalculatedusinghypergeometrictestsforeach
comparison,followedbyBHcorrection.
(C)SpearmancorrelationsofTFmotifenrichmentacrossallmalignantandnon-malignantHSPC-likecells(n=92,993)usingTFsidentifiedin(B).
(D)UMAPrepresentationofcellsclassifiedasHSPC-likebasedonscRNA-seqdata(n=117,276;Figure5A),coloredbynormalizedcountsofMEF2C(left)and
JUN(right).OutlinescorrespondtoclustersidentifiedinFigure5F(colorkeyas(E)).
(E)ViolinplotsshowingdistributionsofnormalizedMEF2C(top)andJUN(bottom)countsinHSPC-likecellsatdiagnosisandrelapse.MalignantHSPCsfromall
clusters(left)foreachclusterseparately(middle),andallnon-malignantHSPCs(right),areshown.AdjustedpvalueswerecalculatedusingBH-correctedtwo-
sidedWilcoxontests.
(F)ScatterplotsshowingSpearmancorrelationsbetweenscaledmotifenrichmentsofAP-1(top)andCEBPD(bottom)andmyeloidlineagescores(Figure5C)
acrosscombinedmalignantandnon-malignantHSPC-likecells(n=92,993).Cellsarecoloredbykerneldensityestimation.
(G)ScatterplotsshowingcorrelationbetweenscaledMEF2CexpressionagainstthatofJUN,CEBPD,andLMO2.Expressionvaluesweretransformedusing
Markovaffinity-basedgraphimputationofcells(MAGIC)91toreducenoiseandcorrectfordatasparsity.Spearmancorrelationsareshownintheupperleftcorner.
(H)ViolinplotshowingthedistributionofscaledCEBPDmotifenrichmentinallmalignantHSPCswithMLLrearrangements(clusters3,4,and5)atdiagnosisand
relapse.pvaluewascalculatedusingatwo-sidedWilcoxontest.(I)Simplifiedmodelofthepathwaysthatregulatemyeloidprimingandhowthesepathways
changeuponrelapse.Linethicknessindicatesactivityoftheupstreamfactororcluster-associateddrivingalteration(asdefinedinFigure5F).AlsoseeFigureS7,
TablesS7andS8.
2128 CancerCell41,2117–2135,December11,2023
ll
Article OPENACCESS
A C
B
D E
F G
H I J
Figure7. LineageswitchinguponrelapseisassociatedwithactivationofB-ALL-likeprograms
(A)ProjectionofscRNA-seqprofilesofmalignantcellsfromPAWHKKandPAUZRTontonormalbonemarrowreference(gray).27Cellsarecoloredbybiopsy.
Referenceiscoloredbycellannotation.Colorlegendasin(C).
(legendcontinuedonnextpage)
CancerCell41,2117–2135,December11,2023 2129
ll
OPENACCESS Article
LMO2 and TCF369,70 (Figure S7D). Using qRT-PCR, we (CD14+CD64+) and an increase of lymphoid cells
confirmedthatLMO2andMEF2Cwere upregulatedatrelapse (CD19+CD79+)uponrelapse(Figure7E).Theseresultsindicate
in seven patients (Figure S7E). LMO2 features in both aAML thatatleastsomepAMLtumorsappeartoundergo amyeloid
and pAML stem cell signatures71–73 and high expression of tolymphoidlineageswitchuponrelapse.
LMO2atdiagnosisindicatespoorprognosis,particularlyinthe We then investigated whether transcriptional networks
MLLsubgroup(FigureS7F).TodeterminewhetherMEF2Cfunc- undergo a similar switch in PAWHKK, by analyzing the scA-
tionssimilarlyinthecontextofpAMLcomparedtonormalhema- TAC-seq data and calculating ‘‘priming’’ scores in the HSPC
topoiesis (i.e., by repressing myeloid differentiation),66,74–76 we populationsbeforeandafterrelapse.Asexpected,theprimitive
correlated expression of MEF2C with JUN, CEBP, and LMO2 populationsshiftedfrompredominantlymyeloid-primedatdiag-
(Figure 6G).69 This analysis confirmed that MEF2C expression nosistopredominantlylymphoid-primedatrelapse(Figure7F).
was anti-correlated with key CEBP- and AP-1-related genes Toidentifyfactorsthatcorrelatedwiththislineageshift,wein-
but positivelycorrelated with LMO2. Coincidentally,CEBP and ferred a trajectory from the tumor at diagnosis toward relapse
AP-1activity,inferredfromCEBPmotifenrichment,weredown- (Figure 7G). Lymphoid lineage-associated TFs inferred from
regulatedinMLLcasesuponrelapse(Figure6H).Wethusimpli- the non-malignant remission cells (Figure S4D) (e.g., EBF1,
cate MEF2C in regulating the decision between lymphoid and TCFfactors.andPAX5)wereupregulatedinmalignantcellsat
myeloidpriminginpAMLprimitivecellpopulations,similartoits relapse comparedtodiagnosis (Figure 7G)andresembledthe
proposed role in normal bone marrow.66 Our data imply that TF profile of pediatric B cell acute lymphoblastic leukemia (B-
reducedmyeloidpriminginrelapsedpAMLsmayresultfromup- ALL).51MEF2Cexpressionandinferredactivitywasalsoupregu-
regulationofMEF2CinMLL-rearrangedtumors,whilereduced lated at relapse (Figure 7G), showing a pattern comparable to
AP-1 signaling may underlie this change in other subgroups non-malignant lymphoid cells (Figure S7G). In addition, both
(Figure6I). MEF2C expression and motif enrichment were correlated with
lymphoidpriminginPAWHKKHSPC-likecells,whileanti-corre-
LineageswitchingmayunderpinpAMLrelapse lationswereobservedwithmyeloidpriming(FigureS7H).Inter-
We observedthat malignant HSPC-like cellsappeared toshift estingly, PAUZRT cells also showed elevated MEF2C motif
towardamultipotentphenotypeafterrelapse.Althoughlineage enrichment upon relapse, despite harboring a RUNX1 rather
switching has been infrequently reported in pAML,77 two pa- than an MLL rearrangement (Figure S7I), while the expression
tients within our cohort (PAWHKK; MLL-AFF3 and PAUZRT; andinferredactivityofMEF2CwaslowinHSPC-likecellsfrom
RUNX1-RUNX1T1)presentedwithmyelomonocytic-likecellsat other RUNX1-rearranged tumors (Figure S7J). Together, these
diagnosisbutcontainedanabundanceoflymphoidcells,span- data indicate that lineage switching may occur upon relapse
ningCLP-liketopre-Bcell-likecells,atrelapse(Figures7Aand and,atleastinthetwocasesdescribedhere,thatB-lymphoid
S3A). Relapse cells in both patients expressed B-lymphoid pathwaysappeartobeinvolvedinthisswitch,possiblythrough
markers,includingCD79AandCD19(Figure7B).Furthermore, activationofMEF2C.Toinvestigatewhetherthisisacommon
analysisofmarkergenes(TableS3)confirmedthatrelapsecells occurrence in relapsed pAML, we analyzed 156 bulk pAML
from PAWHKK also expressed other lymphoid markers, in RNA-seq profiles from different samples at diagnosis and
contrast to the myelomonocytic expression profile of cells at relapse,seekingtomatchtheblastcellcontentanddriveralter-
diagnosis (Figure 7C). To verify that these observations were ations between primary and relapse groups to limit potential
not a result of technical artifacts, we confirmed that the cells confounding effects (Figure 7H). We used GSVA to calculate
contained pAML-associated SNVs and were not doublets signature scores for different cell type markers (Table S3) and
(Figure 7D). Furthermore, flow cytometry on biopsies from a lymphoid signature associated with poor prognosis in infant
PAWHKK confirmed a loss of myelomonocytic cells pAML78(Figure7I).Besidessignificantupregulationofprimitive
(B)UMAP(scRNA-seqdata)ofcellsfromPAWHKK(left)andPAUZRT(right),coloredbybiopsy,predictedcelltype(top)andbynormalizedCD79AandCD19
counts(bottom).Colorlegendasin(C).
(C)Heatmapshowingexpressionofmarkergenes(TableS3)inPAWHKK,withcellssortedbycelltypeandclassificationscore(upperpanel).Middlebarshows
biopsytimepoint.Lowerpanelshowsclassificationscores.BarunderclassificationscoresshowsdetectionofsomaticSNVsidentifiedbymatchedWGSdata.
(D)UMAPsofcellsfromPAWHKK,colorsindicatedetectionofsomaticSNVswithineachcellandthedensityofsimulateddoublets(STARMethods).Jitterplots
showthedoubletenrichmentscoreforeachcell,splitbycellspositive(scaledexpression>0.5)ornegative(scaledexpression<0.5)forCD19andCD79A,with
colorsindicatingdetectionofsomaticSNVswithineachcell.
(E)FlowcytometryofsurfaceexpressioninblastsfrommatchedsamplesatdiagnosisandrelapsefromPAWHKK.DistributionofMFIvalues(left),densitycontour
plotsoverlayingthematchedpair(middle)andhistogramsoverlayingCD14,CD64,CD19,andCD79Asignals(right)areshown.Gatingstrategyisdetailedin
FigureS3D.
(F)Lineagescores(Figure5C)areshownforHSPC-likecellsfromPAWHKKatdiagnosis(top)andrelapse(bottom).Cellsarecoloredbythehighestscoring
lineage.Percentagesofcellsassociatedwitheachlineageareshown.
(G)UMAPs(scATAC-seqdata)showallcellsfromPAWHKK(left)orPAUZRT(right),colored(fromtoptobottom)bybiopsy,inferredcelltypeandinferred
trajectorybyMonocle.36HeatmapsshowscaledTFmotifenrichment(calculatedusingChromVAR47)andscalednormalizedexpressionvaluesforcorresponding
TFsalongthetrajectory.OnlyTFswheremotifenrichmentcorrelatedwithgeneexpression,asdeterminedbyquantileregression(r>0.5),areshown.
(H)Distributionofblastcellcontentbetweenbulksequencingcohortsfrombiopsiesatdiagnosisandrelapse.Diagnosisandrelapsesampleswerenotmatched.
(I)DistributionofGSVAsignaturescoresbetweenbulk-sequencedtumorsatdiagnosis(n=156)andrelapse(n=156).Adjustedpvalueswerecalculatedusing
BH-correctedtwo-sidedWilcoxontests.
(J)Boxplotsshowingexpressionvalues(intranscriptspermillion)oflymphoidmarkerswithinbulk-sequenceddiagnosisandrelapsesamples.Adjustedpvalues
werecalculatedusingBH-correctedtwo-sidedWilcoxontests.AlsoseeFigureS7.
2130 CancerCell41,2117–2135,December11,2023
