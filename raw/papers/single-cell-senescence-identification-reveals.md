---
source_path: /mnt/c/Users/Administrator/Zotero/storage/L3EWQI8E/Tao 等 - 2024 - Single-cell senescence identification reveals senescence heterogeneity, trajectory, and modulators.pdf
ingested: 2026-04-23
sha256: 1b5f36d9e9e22526
---

Resource
Single-cell senescence identification reveals
senescence heterogeneity, trajectory, and
modulators
Graphical abstract Authors
WanyuTao,ZhengqingYu,
Jing-DongJ.Han
Correspondence
jackie.han@pku.edu.cn
In brief
Taoetal.developedacomputational
programthatidentifiesandtracks6types
ofsenescentcellsbasedonsingle-cell
transcriptomesfromtensofthousands
ofcells.
Highlights
d TheSenCIDprogramisdevelopedtoidentifysenescentcells
frombulkorscRNA-seq
d SenCIDfindssixmodesofsenescenceamongcelltypeswith
differentcharacteristics
d SenCIDfindsvariedtrajectoriesinaginganddiseaseto
commonsenescentendpoint
d SenCIDidentifiesgenome-widesenescencemodulatorsand
theirhierarchies
Taoetal.,2024,CellMetabolism36,1126–1143
May7,2024ª2024ElsevierInc.Allrightsreserved.
ll
https://doi.org/10.1016/j.cmet.2024.03.009
ll
Resource
Single-cell senescence identification reveals
senescence heterogeneity, trajectory,
and modulators
WanyuTao,1ZhengqingYu,1andJing-DongJ.Han1,2,3,*
1Peking-TsinghuaCenterforLifeSciences,AcademyforAdvancedInterdisciplinaryStudies,CenterforQuantitativeBiology(CQB),Peking
University,Beijing,China
2PekingUniversityChengduAcademyforAdvancedInterdisciplinaryBiotechnologies,Chengdu,China
3Leadcontact
*Correspondence:jackie.han@pku.edu.cn
https://doi.org/10.1016/j.cmet.2024.03.009
SUMMARY
Cellular senescence underlies many aging-related pathologies, but its heterogeneity poses challenges for
studyingandtargetingsenescentcells.Wepresenthereamachinelearningprogramsenescentcellidentifi-
cation (SenCID), which accurately identifies senescent cells in both bulk and single-cell transcriptome.
Trainedon602samplesfrom52senescencetranscriptomedatasetsspanning30celltypes,SenCIDidentifies
sixmajorsenescenceidentities(SIDs).DifferentSIDsexhibitdifferentsenescencebaselines,stemness,gene
functions,andresponsestosenolytics.SenCIDenablesthereconstructionofsenescenttrajectoriesunder
normal aging,chronic diseases, and COVID-19. Additionally,when applied to single-cell Perturb-seq data,
SenCIDhelpsrevealahierarchyofsenescencemodulators.Overall,SenCIDisanessentialtoolforprecisesin-
gle-cellanalysisofcellularsenescence,enablingtargetedinterventionsagainstsenescentcells.
INTRODUCTION cells,18makingitanurgentneedtoidentifythesedifferentialpat-
ternsandtheirspecificregulators,thustoenhancetreatmentef-
Cellular senescence is a state of permanent cell cycle arrest1 ficacyandspecificity.
inducedbymultipletypesofstresses,includingover-replication, Tobettertargetthesenescentcells,itisessentialtoaccurately
DNA-damage-stress-like radiation,oxidativestress,andonco- identifysenescentcellsindifferentbiologicalenvironments.Un-
gene activation.2,3 Both proliferating and post-mitotic cells fortunately,thereiscurrentlynosinglemarkerthatisuniquefor
(e.g.,fullydifferentiatedcells)canbeinducedtosenescence,3,4 senescent cells.19 Experimentally, SA-b-gal staining20 and
which exhibit various senescence-related phenotypes, like expression of cyclin-dependent kinase (CDK) inhibitors like
increasedsizeofnucleoli,enlargedandoverloadedlysosome, p16 and p21 are commonly used to characterize senescence.
and secretion of senescence-associated secretory phenotype Whilethesemarkersidentifysenescentcellsinmostofthebio-
(SASP)factors.5–7Senescentcellsaccumulateinsidethebody logicalcontexts,theyarenotuniversal,assomecelltypesex-
duringaging4,8andcontributetotheinitiationandprogression pressthesemarkersatnon-senescentstage.7,19,21Also,tech-
of various aging-related chronic diseases.9–11 Treatments to nical issues may bring inconsistency when detecting these
targetandkillsenescentcells,likesenolytics,haveshownprom- markers.Atthetranscriptomelevel,usingdatabaseswithanno-
isingresultsinextendinglifespansandamelioratingvariousdis- tated senescence-related genes (SRGs)7,22–24 to estimate the
eases.12,13Thetargetspecificityandtoxicitytonon-senescent levelofcellularsenescencebyeithertallythenormalizedvalue25
cellsisstillabighurdleforclinicalapplicationsofthecurrentse- ortherankingofthesegenes26providessomecrudeestimation
nolyitc treatments.14,15 Wrongly targeting quiescent (a state ofsenescentversusdedifferentiatedproliferatingcellsandhas
wherethecellstemporarilyarrestforgrowthbutreversible8)or beenappliedmainlyontumortissues.26,27However,thesecrude
differentiatedcellsassenescentcellsobviouslyhasdireconse- estimationsarestilllimitedinapplicationsduringnormalaging
quences.Furthermore,therearebeneficialeffectsofsenescent and tissue degeneration, as quiescent or differentiated cells
cellsincertaincircumstances,whichbringsmorecriticalrequire- dominate in such cases instead of proliferating cancer cells.
mentstostudytherighttimeandconditionforsenolyticstoover- With the advance of single-cell transcriptome sequencing,
come the harmful effects.16 Besides, senescence patterns are computationaltoolstoidentifyandquantifysingle-cellstemness
variableacrosscelltypes,tissues,andinductions.17Someseno- becomeessentialfordelineatingthedifferentiationtree,hierar-
lyticdrugsareeffectiveinsomecelltypesbutnotothers,sug- chy, and their regulations.28–32 Likewise, a robust metrics for
gestiveofdifferentialpatternsormodesofsenescenceamong senescenceidentificationandquantificationatsingle-celllevel,
1126 CellMetabolism36,1126–1143,May7,2024ª2024ElsevierInc.Allrightsreserved.
ll
Resource
A
B
C D
E
F
G H
(legendonnextpage)
CellMetabolism36,1126–1143,May7,2024 1127
ll
Resource
overcomingthehighdrop-outrateandheterogeneity,willfacili- them applicable to normal aging and degenerative processes,
tate reconstruction of cellular senescence trajectories and ratherthanbeinglimitedtocancersandproliferatingcelllines.
regulatory hierarchies,33,34 thus a deeper understanding of Amongthethreemachinelearningmethodswetested,SVM
senescence. performsthebest,withAUCover0.9in96.7%ofcelltypes(Fig-
Toaddressthesechallenges,wedevelopamachinelearning- ure S1C). Therefore, we use SVM to develop the SenCID pro-
basedprogramsenescentcellidentification(SenCID)trainedon gramanddefineabasalsenescentscore(BSS)foreachsample
acompendiumof52senescencetranscriptomedatasetsof602 basedonitsdecisionvaluesfromSVM,representingthesenes-
samples, 30 cell types. SenCID reveals 6 major senescence cence-relatedgeneexpressionlevel.WefindthatBSSdoesnot
identities (SIDs) for different cell types that have overlapping vary across different cell lines or after different senescence-
butdifferentialfunctionalbiasesandsensitivitytocertainseno- inducing methods for one cell type (Figures S1E and S1F) but
lytics. SenCIDperforms wellon both bulk and single-cell RNA variesacrossdifferentcelltypesandincreasesaftersenescence
sequencing data and enables reconstruction of single-cell induction (Figure S1G). Some cell types, like vascular smooth
senescencetrajectoriesinnormalaginganddiseaseconditions, musclecells,havehighBSSevenwithoutsenescenceinduction
aswellasmappinggenome-widesenescencemodulatingland- (averageof0.88),whileothers,likedopaminergicneuroncells,
scapebasedonsingle-cellperturbationscreens. have low absolute BSS even after senescence induction
(averageof(cid:1)1.28),makingitdifficulttouseauniformstandard
RESULTS toidentifysenescenceindifferentcelltypes.
Heterogeneityofsenescencesignaturesacross 6SIDmodelstocharacterizesenescenceofdifferent
celltypes celltypes
To develop a program applicable to a broad range of cellular Todeterminethesenescencesignaturesofdifferentcelltypes,
senescence identification, we collect published transcriptome weemploytherecursivefeatureelimination(RFE)method81to
data from 602 samples across 52 senescence-related eliminate the unimportant feature genes from the initial 1,290
studies, including 306 senescent and 296 non-senescent la- SRGs (Figures 1A and S2A, STAR Methods). We conduct the
bels.17,21,27,35–80 The bulk transcriptome dataset (BTD) contain trainingoftheRFE-SVMmodelindependentlyforeachdistinct
57typesofcelllinesand30celltypeswithvarioussenescencein- celltype.Ifamodeltrainedonaspecificcelltypedemonstrates
ductions(Figures S1A and S1B; Table S1). We first compare 3 accuraciesover0.95onothercelltypes,theseothercelltypes
different machine learningmethods,supportingvectormachine are categorized into the same senescent identity (SID) group,
(SVM), random forest, and deep-neural-network-based multi- and the respectivemodel isregarded asone SID model. As a
layerperceptronclassifier(MLPC),alongwitharoutinegeneset result,weidentify6suchSIDsthatcover28ofthe30celltypes.
rankingmethod(genesetvariationanalysis,GSVA),26basedon LogisticregressionisthenusedtonormalizeeachSIDmodel’s
a gene set with 1,290 SRGs collected from literature (STAR senescencescorestobewithintherangeof0to1(FiguresS2A
Methods). We implement a leave-one-cell-type-out strategy for andS2B,STARMethods),witheachSIDmodelcorrectlysepa-
allthemachinelearningmethods(STARMethods)anduseareas rating all senescent and non-senescent cells using the same
underreceiveroperatorcharacteristic(ROC)curves(AUCs)from threshold of SID score 0.5 (Figure 1B), except a few samples
predictions on each test set. The machine learning algorithms that were reported abnormal by the original publication.27 The
generally perform better (with ROC AUCs over 0.9 in 88.9% of remaining two cancer cell types (liver cancer and melanoma
celltypesinaverage)thanGSVA(withAUCover0.9in76.6%of cells) can be partly but not fully characterized by SID1 and
celltypes)(FigureS1C).Furthermore,whenonlyconsideringthe SID6models,respectively(FiguresS2CandS2D).
abilitytodistinguishsenescentcellsfromquiescentcells,machine
learning methods (with AUC over 0.9 in 80% of cell types in DifferentSIDshaveoverlappingbutdifferentialgene
average)performmuchbetterthanGSVA(withAUCover0.9in functionsanddifferentresponsetosenolytics
only20%ofcelltypes)(FigureS1D),suggestingthatthemachine The RFE-selected feature numbers are different among SIDs
learningmodelsaremorespecifictothesenescencestate,making (Figure S2E). Notably, we find that none of the RFE-selected
Figure1. Identificationofsixdistinctsenescence-associatedSIDtypesbySenCID
(A)SchematicdiagramoftheSenCIDmodelconstructionanditsapplicationtobulkandsingle-celltranscriptomes.
(B)PerformanceevaluationofeachSIDmodelonitsrespectivecelltypes.Forthetrainingdata(red-label),SIDscoresareobtainedfrom5-foldcross-validation,
whileforindependentvalidationdata(black-label),SIDscoresarepredictedbySenCID.
(C)Heatmapshowingnormalizedexpressionvaluesofhighlyexpresseddifferentiallyexpressedgenes(DEGs)(rows)amongnon-senescentsamples(columns)
inallsixSIDs.ThetopenrichedgenefunctionsonGeneOntology(GO)-termareannotatedontheright.
(D)RepresentativeGSEAGOtermsenrichedbysenescent-versus-non-senescentDEGsuniqueineachSID.
(E)Distributionofbasalsenescencescores(BSS),ribosomalproteins,inflammation,andsignalingentropyofallBTDsamplesineachSID,calculatedbyGSVA.
Centraldotanderrorbarsrepresentthemeanvalueandthe95%confidenceinterval.Significancebetweensenescentversusnon-senescentsamplesismarked
above(*p<0.05;**p<0.01;***p<0.001;****p<0.0001;two-tailedStudent’sttest).
(F)Negativecorrelation(SpearmancorrelationRCC=(cid:1)0.52,p<2.2e(cid:1)16)betweensignalingentropyandBSSacrossdifferentcelltypes,coloredbySIDtypes.
(G)ReductionofSID5scoresuponsenolytictreatmentswithcardiacglycosides(Ouabian50nM,digoxin100nM,treatedfor36h)onlungfibroblasts(**p<0.01,
two-tailedStudent’sttest).
(H)ReductionofSID5scoresuponsenolytictreatmentswithprocyanidinC1(PCC,50mM)onprostatestromalcells(**p<0.01,two-tailedStudent’sttest).
SeealsoFiguresS1–S3.
1128 CellMetabolism36,1126–1143,May7,2024
ll
Resource
A
B
C
D
E
F
Figure2. PerformanceevaluationofSenCIDonsinglecells
(A–D)tSNEembeddingofdifferentcelllinesbasedonhighvariablegenes,coloredbySIDscores(left)andsenescence-inductiontreatments(middle),andthe
violinplotofSIDscoresunderdifferenttreatments(right).
(legendcontinuedonnextpage)
CellMetabolism36,1126–1143,May7,2024 1129
ll
Resource
featuregenesaresharedbyallsixSIDmodels,evenforsome pendentdatasets85andshowsignificantlyreducedscoresafter
well-known senescence indicators (such as CDKN2A, the varioussenolytictreatments(Figures1Gand1H).SID5scores
p16-encoding gene, and CDKN1A, the p21-encoding gene), aftersenolytic treatments do notdrop back to the non-senes-
indicating that there is no single common determinant marker cencelevel,similartotheSA-b-galstainingresultsintheoriginal
ofsenescence(FigureS2F).Interestingly,theSIDgroupingdid studyunderthesamedrugconcentration.86Overall,ouranalysis
notfullyoverlapwithtissuetypes,althoughthereispartialover- also reveals the heterogeneity of senescence response to
lapwithcelllineagesrepresentedbytheircellularfunctions(Fig- differenttreatmentsacrossthedifferentSIDs.
ure1C;TableS2),e.g.,thegeneshighlyexpressedinSID2are
related to epidermal development. We also construct an SVM SenCIDdistinguishessenescencefromother
multi-classifiertrainedbyBTDtoautomaticallydeterminewhich resemblingcellularstates
SIDacellbelongsto,withahighaccuracyof0.998by10-fold Besides quiescence, there are some other cellular states that
cross-validation(FiguresS2AandS2G). resemblesenescenceincertainaspects.Forexample,activated
The canonical senescence signatures, including lysosome, fibroblasts are known to express many pro-inflammatory fac-
secretome transportation, and inflammatory response, are tors,87andmacrophagesgenerallyexpressp16.88,89Tovalidate
commonly enriched in the differentially expressed genes SenCID’sspecificity,wetestedwhetherSenCIDwouldgivefalse
(DEGs) of senescent versus non-senescent cells in different positive predictions under such conditions. Multiple datasets
SIDgroups(FiguresS3AandS3B).However,mostgenefunc- were employed to test SenCID’s responsiveness to various
tions are specifically enriched in a single SID (Figures 1D and fibroblast activations, such as eosinophil-degranulation prod-
S3A; Table S3), indicating that different SIDs may represent ucts,87 transforming growth factor b (TGF-b) treatment,90 and
different aspects of senescence. For example, SID2 shows cancercellco-culture.91SIDscoresremainedstablylowacross
enrichmentforlipidsandnucleotidessynthesis,SID3formito- these conditions (Figures S4A–S4C). Similarly, SenCID pre-
chondria and redox reactions, and SID4 for unfolded protein dicted low senescence levels in macrophages92 and induced
response. As expected, cell cycle checkpoint-related genes pluripotent stem cell (iPSC)-derived T cells,93 despite slight
aregenerallydownregulatedwithsenescence,exceptforG1/S score elevations post-T cell activation (Figures S4D and S4E).
checkpointgenesinSID4andSID6,wheretheyareexpressed Furthermore, although persistent DNA damage response is
at low levels in both senescent and non-senescent samples widelyacceptedastheoriginofsenescence,2itshouldnotbe
(FiguresS3CandS3E). confused with acute genotoxic response and short-term DNA
Senescent cells typically experience inactivated ribosomal repairthatfinallyrecoverthecells.Weshowinatime-seriesda-
biogenesisduetothelossofproliferationandnormalcellfunc- tasetthatSIDscoreshardlychangeat2hrightafterlow-orhigh-
tions.However,theover-secretionofSASPsconsumesexces- dose of bleomycin treatments, when almost all cells had DNA
siveribosomes.82Wefindasignificantdownregulationofoverall damage foci in both groups.45 Moreover, the SID scores of
ribosomal protein levels in SID1, 5, and 6 upon senescence, low-dosebleomycintreatedcellsarestillcomparabletothecon-
whereas there is no significant change in other SIDs (Fig- trol group within days after the treatment, while the high-dose
ure 1E). Intriguingly, cell differentiation potency, as measured group get into senescence, revealing that SenCID does not
bysignalingentropy,issignificantlydownregulateduponsenes- taketheacuteresponseorsuccessfulrepairprocessassenes-
cence in SID1, 2, 4, and 5 (Figure 1E), whereas inflammation cence (Figure S4F). Similarly, the SID scores hardly change in
scoresshowtheoppositetrend(Figure1E).Thereisasignificant TK6 cells 4 h after treatments with different genotoxic com-
negative correlation between signaling entropy and ribosome pounds (Figure S4G), when their clastogen or aneugenic bio-
expression levels with BSS (Spearman correlation (cid:1)0.52 and markers(g-H2AX,p-H3,etc.)aresignificantlyincreased.94Over-
(cid:1)0.26,respectively,p<2.2e(cid:1)16,Figures1FandS3F),indicating all, SenCID accurately identifies senescence distinguishing it
thatsenescenceheterogeneityexistsacrossdifferentcelltypes fromothercellularstatespartiallyresemblingsenescence.
andthatcelltypeswithhigherpluripotencyandribosomelevels
exhibitlower‘‘senescencebaselines.’’ SenCIDforsinglecells
Senolytictreatmentstargetinganti-apoptoticmembersofthe We evaluate the performance of the SID models on single-cell
BCL2familyhaveshownpromiseinselectivelyeliminating se- data of three cell types, which correspond to SID3, SID4, and
nescent cells.18,83,84 Our analysis finds that anti-apoptotic SID5 in BTD.44,53,95,96 To correct for drop-out reads, we use
BCL2 family genes are most significantly upregulated in SID5 deep count autoencoder (DCA)97 for imputation. SenCID gave
cells upon senescence (Figure S3G), indicating a potential for the same SID classification on the single-cell data as on the
morespecifictargetingofsenescentcellsinSID5withBCL2in- respectiveBTDforeachcelltype(FiguresS4Hand1B)andeffec-
hibitors.Wealsofindthatlungfibroblastsandprostatestromal tivelydistinguishedcellswithandwithoutsenescenceinduction,
cells, commonly used as models for senolytic drug develop- withAUCsover0.9(Figures2A–2D).Weconductedacomprehen-
ment,areclassifiedasSID5bySenCID(FigureS3H)intwoinde- sive comparison with alternative methodologies,24,26,27,95,98–103
(E)BenchmarkingSenCIDagainstsinglecanonicalmarker(CDKN2A),senescentgenemodulescores,andvariouscellannotatorsinclassifyingsenescentcellsin
single-cellsenescencedatasets.
(F)UMAPembeddingcoloredbySIDscores(left),theviolinplotoftheSIDscoreswithincreasingnumberofpassages(PDL)orwithimmortalization(htert)
(middle),andlinearregression(p<0.001)ofsenescenceratios(determinedbybinarizationthresholdof0.5)withthecorrespondingSA-b-galstainingpositive
ratios(right).AUContopoftheviolinplotsdenotestheareaundertheROC-curvesfortheSIDmodeltodiscriminatethesenescentversusnon-senescentcells.
SeealsoFigureS4.
1130 CellMetabolism36,1126–1143,May7,2024
TN V A E I F E E D C F I S G G L G A N F 2 I E F A F I M R T T A 1 C R R D R G B E G 0 1 5 R B G G B I 5 B N B 1 R EE E 1 2 S 3 E RR G R 5 BB F S R BB R P I la C 33 iliate s d P a N B A I K L D B C 2 1 R l R ub B G F C 2 P D R 5 3 E 5 P D H e A E n P 2 d I H C r A A i 3 t M T i N c 1 F H S 4 S F P 1 9 0 0 q AA1 F E _ PH B i 6 N 2 b A MPT r T A o D G R E A 5 b A NXA1 las EGFR tM ADAM 28 a C R1 c AARR r EEGG o IL2 p R G E h F 3 N B V a 2 2 E q G g T F IC _ B e A A M M 4 I 2 T a G q E A s _ R M S B t 2 P B T M N 3 E T A on R N o B F c 1 E I q y T B S _ P t 2 e 3 G F T N H E A m a K 1 B 1T B A F S 0 P 1 la V s 4 N P T E A N N l G I F 1 T o F G F E G A S g A A B V R F I A R A F L T T I F E R B I T A E 1 4 2 T D E G 2 2 3 C B 0 G R R G G G G _ _ 3 F A E G F B R B q q L G R 1 E 4 1 5 1 o o I A E I T E v v T E R G e e G P I G G L E r r H F 4 B I 2 A T S F I G R A A B 2 T R V G A P R G T T 6 G R I A N L A 2 2 E V 2 I 9 V T I R _ _ G T G G G q q B d EE e A C t l a u 1 4 PP 2 b il X iC I HH L D 2 BB e R EE l 44 n a I GG G T d s G FF r a i RR A t II B i TT X c GGBB E 22 t A n II h LL R 4 22 d e E RR G q o GG lia _ EE l S FF 2 P NN M N BB22 T a A IT II G CC A AA c V MM11 ro ITG p AL C OL4 h A3 a IL2 R G 3 g q e EG F M _ R 2 S o P N T EP n H B A 4 o IT G I c T A G 2 L A y V q IT tN G _ e A 2 K X E T G F A S R P E N 1 P I q H T _ I B G 2 P T 4 T la A G A sm X A I B 1 T a TA 2 R G S E A E P G V I G 0 N T I G T F I G I T G T R I e A G E T G I B I L I 0 L C n G T G A T 2 A 2 . e D G X G A F M 5 R 4 M R B B E G 7 2 2 x 1 p EE r I I II e T RR G I TT T 1 E s G EE GG BB F PP G T . G s GG E 5 A 1 BB VV BB H B F i G R FF I 2 44 RR 11 o B G 1 R V F RR F S F n E R N 2 C 1 1 G D R 1 IT F 4 G E A M F n 4 do B G I t 4 h F 1 e F q lia F F l R _ MM i N b 2 1 r NN MM T 1 C o A EE b PP D CC la 4 77 TT s 4 I II t T NN s G 33 TT B GG 1 MM N M R 22 p P1 GG a NN h AA C II c a 22 D 74 rg oe E R s BB4 3 IT M G A9 q E G a F R _ s 2 t C D44 cM T NECTIN3 y A o C t D74 en 2 2 soN q T ER BB4 _ A e NE C u E TI G N 1 F 3 2 R r I G q o T F1 _ n R A F I a G T G F l R B P E 2 1 I G T e F G r R 1 i A c T 9 y I A T E te G D m s B u I N s T I c S 6 G l l a e i m R l G eh o tip F N o T e A I _ A t N h T K 1 y R a 3 wr I G R iA E T P B G G 2 E 1 I G B F I T G N 1 R F G N F R C R E B I E R 1 C I T P D R G 1 R G P G D 1 4 B F 2 F 4 2 B B 1 R 2 1 R 4 6
Trajectory Associated Functions
focal adhesion cell−substrate junction cadherin binding vacuolar membrane melanosome −logP_adj pigment granule coated vesicle 5 lysosomal membrane 10 respirator c y e c ll h − a c i e n l l c ju o n m c p ti l o e n x 15 inner mitochondrial membrane protein complex 20 oxidoreduction−driven active transmembrane transporter activity mitochondrial respirasome respirasome Generatio
mitochondrial protein−containing complex 0.05 generation of precursor metabolites and energy oxidative phosphorylation 0.10 aerobic respiration 0.15
primary ac a ti e ve ro t b ra ic n e s l m ec e t m ro b n r a tr n a e n s tr p a o n r s t p c o h r a te in r 0.20
activity clathrin−coated endocytic vesicle
clathrin−coated vesicle Gene_cluster lamellar body clathrin−coated endocytic vesicle membrane Down cytoplasmic translation Inter cytosolic ribosome Up structural constituent of ribosome protein serine/threonine/tyrosine kinase activity protein serine kinase activity actin binding protein serine/threonine kinase activity Aging_ I u P p F_ C u H O p P V _ ID u A p 1 g 9 i _ n u g p _ I i P nt F e _ C r i H n O t P e V _ r ID in 1 A te 9 g r _ in in g t _ e I d r P o F w _ C n d H O o P V w _ I n D do 1 w 9_ n down Group
AT2 in Lung Aging AT2 in Chronic Lung Diseases AT2 in COVID-19 1.00 **** ****
0.75
0.50
0.25
0.00
Healthy HP IPF
AT2 Senescent Trajectory in AgingAT2 Senescent Trajectory in IPF
SID2 Score D C C on 1 dition 4
CEIBNUEBCSPRSCRTRCEIMMSSSSGHJMSZ K R
U
F
B
L A PD OO P N PR
O
TT U H RS R B L AE
ER
AA
X
Z F AA D
N
F O
T
C 3 3 I X
X
F P B DBO E
S
N D 3 E U FZ
H D
F 1 1 TT 1
B
0 ( P
(
C2 H 6
4
1 P C P B
1
B 2 B( X 2 1 2 1( (
L 1
+
+
12 ( + 0 + + (
7
(
(
1 (
(
1 ( 1 +( F5 D( F 1 1 K (
1 (
3 )
)
(( + +
+
+
+
( ) + + +) ) +
+ A
( ++ ( ( ( ( ) ( 2 1
(
+ (( ( ) + )
)
)
)
+ + + + ) ) ) +
+
+ )
)
+ +
(
)) ( ( ) )
+
) ) ) ) + + )
)
)) )
)
) )
C C
SI
e o
D − − 0 2
l
0 0
A n
4 2
l
2
T t
. .
d
8 1
y 2
S
i p ti
c
e o
o
n
re
AT2 Senescent Trajectory in HP AT2 Senescent Trajectory in COVID-19 Healthy SID2 Score Aging
Condition HP DC1 IPF
CEIBNUEBCSPRSCRTRCEIMMSSSSGHJMSZ K R U F B L A PD OO P N PR O TT U H RS R B L AE ER AA X Z F AA D N F O T C 3 3 I X X F P B DBO E S N D 3 E U FZ H D F 1 1 TT 1 B 0 ( P ( C2 H 6 4 1 P C P B 1 B 2 B( X 2 1 2 1( ( L 1 + + 12 ( + 0 + + ( 7 ( ( 1 ( ( 1 ( 1 +( F5 D( F 1 1 K ( 1 ( 3 ) ) (( + + + + + ( ) + + +) ) + + A ( ++ ( ( ( ( ) ( 2 1 ( + (( ( ) + ) ) ) ) + + + + ) ) ) + + + ) ) + + ( )) ( ( ) ) + ) ) ) ) + + ) ) )) ) ) ) ) G C C C ro o o o D m m m u C p m m m 0 − C 1 . 0 O o o o 0 . n n n 6 0 V 8 I D I U D n o p te w r n
erocS
2DIS
1.00 ****
0.75
0.50
0.25
0.00
Young Old
erocS
2DIS
1.00 ****
0.75
0.50
0.25
0.00
non
C
- OVID COVID
erocS
2DIS
2_CD
SID2 Score
0.75 0.50
0.25
2_CD
SID2 Score
0.6
0.4
0.2
2_CD
SID2 Score
0.8
0.6 0.4
0.2
DC_1
2_CD Condition Healthy
HP
IPF
DC_1
2_CD Condition non-COVID
COVID
DC_1
2_CD
ll
Resource
A
B C
D
Condition Young
Old
E F
Figure3. Quantificationandtrajectoriesofsingle-cellsenescenceinhumanlungaginganddiseases
(A)DistributionofSID2scoresinAT2cellsoflungsinagedhumans(left),humanswithchronicdiseases(IPFandHP,middle),andthosewithCOVID-19(right),
alongwiththeirrespectivecontrols.SignificanceofdifferencefromrespectivecontrolsisdeterminedbyWilcoxontest(****p<0.0001).
(legendcontinuedonnextpage)
CellMetabolism36,1126–1143,May7,2024 1131
ll
Resource
suchasthesinglecanonicalmarker(CDKN2A),modulescoresof diffusion maps with SID2-related in BTD (SID2-up and SID2-
differentsenescence-relatedgenesets,andvariouscellannota- down, STAR Methods). The embeddings of the trajectories
tors(Figures2EandS4B–S4M).Notably,althoughthegeneset clearlytrackalongwithSID2scores(Figure3C)andthepartition
ofDEGsfromTeoetal.demonstratesremarkableaccuracyon ofagegroupsordiseaseorigins(Figure3D),withgeneexpres-
itsowndata(GEO:GSE115301),theperformanceispooronother sion patterns dynamically changing at different pseudo-time
datasets,especiallyondifferentcelltypes.Conversely,SenCID points(FigureS5D).Notably,celljunctionandlysosomecompo-
consistentlyemergesasthetop-performingmethodacrossallda- sitionsarecommonlyenrichedintheendpointofalltrajectories,
tasets, showcasing its proficiency in terms of accuracy and whilegenesrelatedtocellrespirationandactivetransportation
robustness.Furthermore,onasingle-celldataoflungfibroblasts are transiently elevated in the middle of trajectories, common
covering a time course toward replicative senescence,104 SID to aging, chronic lung diseases, and COVID-19 (Figure 3E;
scoresshowaprogressiveincreasewithcellpassageandreach TableS5).Onthecontrary,genesthataredownregulatedalong
alargespikeatpassage50,consistentwiththeratioofSA-b-gal- thetrajectorydonotshowconsistentpatternsacrossdifferent
positivecellsintheoriginalstudy(Figure2F).104Ouranalysisre- senescence inductions, indicating that senescent cells under
veals that the BTD-trained SenCID is applicable to both Drop- different conditions may lose different gene functions. For
seq- (Figures 2A, 2C, 2D, and 2F) and Smart-seq- (Figure 2B) example, clathrin-coated vesicle, ribosome, or specific amino
generatedsingle-celldata. acid activation functions are specifically lost during aging,
chroniclung diseases andCOVID-19, respectively (Figure 3E).
SenCIDrevealsheterogeneoussingle-cellsenescence ThesefindingssuggestthatSID2isareliablemarkerfortracking
trajectoriesduringlungaginganddiseases theprogression ofsenescence inAT2cellsandthat despitea
In order to investigate the contribution of senescence to age- common endpoint of senescence, the functions lost during
relatedanddisease-relatedchangesinhumantissues,weapply differentstressesaredifferent.
SenCIDtosingle-cellRNAsequencingdatafromlungsamplesof Weconductananalysisofthechangingpatternsoftranscrip-
individualswithnormalaging,chroniclungdiseasessuchasidio- tion factor (TF) regulons along the senescent trajectories (Fig-
pathicpulmonaryfibrosis(IPF)andhypersensitivitypneumonitis ure3F).Consistentwithcommonupregulatedfunctionsacross
(HP), and COVID-19.25,105–107 As expected, SenCID classifies differentsenescenceinductions,weobservethatthefourtrajec-
differentcelltypesintodifferentSIDs,andwefindthatagedor tories exhibit many common upregulated regulons such as
diseased lungs have significantly higher SID scores compared inflammation-responsiveTFs(CEBPD,SPI1);interferonsystem
withtheircontrolsinmostcelltypes,especiallyalveolartypeII (IRF1, STAT family); and other stress-induced factors (ENO1,
epithelial(AT2)cellsinSID2(FiguresS5A–S5Cand3A).Further- JUN),beingcharacteristicfeaturesofsenescentAT2cellsinall
more,AT2cellswithtop25%SID2scores(AT2_q4)exhibitsignif- cases. The downregulated and transiently up (intermediate)
icantlyhigherlevelsofcell-cellinteractions,particularlyinvolving TFs,however,aremoreheterogeneous.Notably,thetrajectory
inflammation ligand-receptor pairs, than those with low SID2 ofnormalaging-senescencedidnotexhibitthedownregulation
scores(AT2_q1)(Figure3B;TableS4).Notably,autocrineactions ofCHD2,ELF1,andIKZF1regulons,aswellasthetransientup-
accountforhigherproportionsoftheelevatedinteractionpairsin regulation patterns of many factors such as CREB/p300 and
IPFAT2_q4cells(11outof121pairs)andCOVID-19AT2_q4cells CLOCK, suggestiveof a rolein circadianregulation indisease
(26outof399pairs)thaninnormalagedAT2_q4cells(4outof71 inducedsenescencebutnotinnormalagingconditions.These
pairs), suggesting that senescent cells might trigger forward- findingssuggestthatdifferentinductionsofsenescenceofthe
loopsthatexacerbatediseasepathology.However,theseauto- samecelltypesmightbemediatedthroughdifferentregulations.
crine loops are different under different senescence inductions
(aging, chronic lung diseases, and COVID-19) even for the SenCIDrevealsheterogeneoussingle-cellsenescence
samecelltype(Figure3B).ThesefindingssuggestthatSenCID trajectoriesduringmultipletissueaginganddiseases
caneffectivelyidentifysenescentcellsincomplextissueenviron- WeextendtheapplicationofSenCIDtodetectsenescentcellsin
mentsandrevealtheirpotentialcontributiontoage-relatedand multipletissuesduringagingandaging-relateddiseases.108–111
disease-relatedchanges. OurresultsdemonstratethatSenCIDcanaccuratelydistinguish
Toobservethecontinuousprogressionofsenescenceatthe aged or damaged tissues from their controls with high signifi-
single-cell level, we construct trajectories of AT2 cells using canceandAUCs(FiguresS6andS7),forexample,chondrocytes
(B)Circosplotdisplayingthetop50protein-proteininteractionsthatdiffersignificantlybetweenmostsenescent(AT2_q4)andleastsenescentAT2cells(AT2_q1)
inpatientswithnormalaging(left),IPF(middle),andCOVID-19(right).Theexpressionofproteinsisindicatedbytheouterring,whilethecelltypesarerepresented
bytheinnerring.Thelinewidthscorrespondtotheabsolutevalueoflogfoldchanges,andlinecolorsindicatethesign.Thecolorintensityoflinesrepresents
significance,allwithp<0.05(Wilcoxontest).Autocrinepairsarehighlightedbyredfont.
(C)TrajectoriesofAT2cellsconstructedbydiffusionmapbasedonSID2-upandSID2-downgenesets,coloredbySID2scores.Senescenttrajectoriesare
indicatedbygam-smoothedlines.
(D)Sametrajectoriesin(C)coloredbyagegroupsordiseasestates.
(E)GOtermsenrichedfromtheupregulated,intermediate,anddownregulatedgenegroupsalongthesenescenttrajectoryin(C).Thetop5termsrankedby(cid:1)log
BH-correctedpforeachgroupareshown.
(F)Heatmapsofregulonswithsimilardynamicpatternsalongthetrajectories.Row-scaledgam-smoothedregulonactivitiesareindicatedbythemaincolorbar.
Onlyupregulatedregulonswithsignificantupregulationsinallfourtrajectoriesaredisplayed,whiledownregulatedandintermediateregulonswithcommon
patternsinatleastthreetrajectoriesarepresented.
SeealsoFigureS5.
1132 CellMetabolism36,1126–1143,May7,2024
C
D
C
C
C
C
L
D C
D
D
C C
L E
D
M R C
9
3
R F
G
D
K
3
2 6
C
F
L 1
F
R
L 1
2 D
R
E
R
1 3
C
G
1
6
D
F C
3 L
R D
R 6 yeloid C
M
h
9
P o
T
c n
3
D 1 y d
L
t r e D o _
R C
q R 3
I 2 T I
2 I
o
T
G
G
r A P
A
4
2 C
C
C E
L
R
C
L C
F
2
1
C
C
L
M
C
K
F
L
1
R1
E C
HH
G c
LL
F
AA
R
−− DD
y
RR
h
BB11
t oe n C M _ KLR 1 dq
EE GGFF RR
r2 o
4q CC RR LLFF
C
11 _
L CF1
et OO y
C
GG
D
NN
S 9
c
3 M
o N
E
r G
G C
d F
FR
n
N
C o O
G
h L
F
3
R
C A
S L
S 1
R
E
IF P
R
1
P
S
TT IN
S
NN
C F
E CC
L
1 2 q
M
_ CC
C
e
a
t
E
y
s
o c
t
r LL d
F T
n
G
oh CC C
1
C
F
FF
C
O
R
11 VV
L
L
E
CC
C
1
G
C A AA
L F
E
F
2
C
M
R
NN
1
R
I
C G
R T C P
K A L
G
F
R 1
L R C R R
A L
R F 1
2 5
E 1 S2B
I
M
L T I
I
T
A T
I R G T
P
G B
C G
P G A
R
M
I V
A
A T
6 1 A
2
P
R
9
5 G
V R
B L 1 A M R
2 L
3 P
S
P
L
R
R
6
R
E 1 R
E P C
A
_
B
6 q2 C
b B iF
D
2
44
B
IT
M
G
P
A
R
3
2
IT
L
G
R
A
P
9
6
E
B
C
M
AC
P
V
R
R _
1
1
A C
q3
M E
IT
R
G
B
A
B
2
2 S E
BM P
G
R 2
F RTH BS1
M B MP R2 ye IT l G
BB
o
MM
A
PP
5
RR
i
22
d IT
II
G
TT
A
GG
V
BB
M
33
S
4 LL
B
RR q
C M
PP _ 66
P
C
q R
BB
P
E
1 2
MM
L E A
PP
C m I U
GG RR
a _ T P R
11
l M
DD
a G as s
AA
t
FF C
A I
66
V
O
T
BB
G
L
C
MM 8
A
FF
D
A
L
PP
2
NN DD
3
1
S I
66 N
6
11
T I
KK G
R T
R
G
KK D
G
G 22
A
F
A
1
9
7
4A C C
A
T C C
L
M V
N C
H O
T D
D
O
R
K
F R
B
L
D
A A 4
T
2
R
1 C B
R
C 0
R C
P
F
A 1 M
4
1 K
Z
5 A
H 1
P
L D
R 1
1
R
R
4
6
1
P L
L A
T
T
1 B
B
T
3q_biF
R
R
F ff
F
id R
L ib
_
T
C
_
e
B
t
q
y T
1 R
c T
C
F o N R n
D
F it
4
C R a
0
S re
T
F K
F K
1
R
4
C e
d L
r
T
L a
i B
R
o R
P t 1
l
i
e
n
y
o FZ
N M
D
O
c 6
T C
y
H1
t N e O TC
C
H 1 _
L RP5
u
E
n
_
D D R 1 d
DPP4
i
c
ff
ita
cP
T
T
N
F
F h R
R
S
C
F
y
14
e
p
ter L
m
T
LT
B i
B
R
R
F
y
i
L T
b
FR
A
C
_ CK q R
A
4
C
L 2 T
K
B
R2
R E D C
L
P
TT
P
BB
4 M
4 RR CC
e
q
T l
_
a
DD
N n
b
o
44 i
F L
A F
c
00
y T R t
CC
e T B S
C KK
R L F
RR X
T 1
A 44 C
V 4 B
P B L
L L R
O 2 M TT
D R F
E CC
F
NN
L
P
Z
TT
P T
C
R Z
CC FF 2
D
NN
1 F
C
D
SS LL
3
FF
R
22 L FF
6
SS
C
1 11 FF 33 9 11 BB 44
SID3 Score SID4 Score
Celltype Celltype
Condition Condition
DC1 DC2
ATF3(+) FLI1(+)
F F J B E E M T U B E E G H F S C T E C E H A U O O O C C G L A 2 P T M R S I U R I S E F V F A N F F C X F 3 S S L F G X E R C F X 1 E T 7 2 3 0 ( 4 A O 2 H ( B 2 1 B 1 ( A 2 ( + 1 ( P + ( ( 0 + ( + ( F + C ( ( ( + + ( 1 1 3 + ( ) ( + ) + 1 ( + + + ) ) + + 1 ) ( ) ) ( ( + ( ) ) ( ) + ) ) ) + + + ) ( ) + ) + ) ) ) ) ) ) E H B F B E E M T U B I N R T E S I M M C E H R R A O F M B C C G L R M R U E S R R I E E S F F V F D F X F S L L F C G N F E R X F A C C 5 6 E 7 2 P 3 3 A O 2 1 5 2 A B X 2 1 ( D ( ( O ( ( P ( + + + ( ( + ( ( 1 ( F + C ( ( + 1 1 3 2 + + + 6 + + M 1 + + ) ) ) ) ( 1 ) ) ( ( ( ( ( ) ) ( ) + ) ) ( ) ) + + + + + + ( ( + ) + + ) ) ) ) ) ) ) ) ) KLF3(+) KLF3(+) ZBTB7A(+) ZBTB7A(+)
SID5 Score SID Score Condition Celltype 0.8 Young / Adjacent 4 D Co C n 1 dition Old / Diseased
T S T T H B C E T O A X F F X T ( 1 1 A + 2 2 5 1 ) ( ( ( + 0 + + ) ( ) ) +) 0.2 DC1 0.04 0 2
B E C G L R A 1 F (+ 1 ) (+) Celltype
E M T U A L S E F F F F 7 2 2 2 ( ( ( + C + + ) ) ( ) +) p F r C eFC −0.02 −2 K P L R F R 6 X (+ 2 ) (+) preHTC −4 S C P R I E 1 B (+ 5 ) (+) HTC Group Z N N F F IL 4 3 8 ( ( + + ) ) RegC Down−regulated B IR C F L 1 3 (+ (+ ) ) RepC Common Down T F C E H K G O R L R IV F I S G E F E 3 L B ( 1 P ( + 1 + 3 ( 1 ) + ( ) ( + ( + ) + ) ) ) E H Fi C o b m ro C blast I U C n o p te m − r r m m eg e o u d n l i a a U t t e e p d ZBTB7A(+) Group
1.00 ****
0.75
0.50
0.25
AT2_q4 over AT2_q1 Gene Expression AT2_q1 over AT2_q4 logFC 1 4 9 0 0.5 1 1.5 2
Chondrocyte Senescence ArteryEC Senescence
Trajectory Associated Functions Trajectory in Osteoarthritis Trajectory in Atherosclerosis
collagen−containing extracellular matrix
extracellular matrix structural constituent
extracellular matrix organization
external encapsulating structure organization endoplasmic reticulum lumen −logP_adj cell−substrate junction focal adhesion 5 ATP metabolic process 10 mitochondrial protein−containing complex inner mitochondrial membrane protein complex 15 cytop cy la to sm so ic lic t r r a ib n o s s la o t m ion e 20 structural constituent of ribosome response to hydrogen p p o e ly r s o o x m ide e Gene_cluster receptor ligand activity down signaling receptor activator activity morphogenesis of a branching epithelium inter negat b iv l e o o r d e g v u e l s a s ti e o l n e o n f d l o y t m he p l h ia o l c c y e te ll m m i i g g r r a a t t i i o o n n up vascular endothelial growth factor receptor
ne n g e a g ti a ve tiv r e e g re u g la u t l i a o s t n i i o g o n n f a o c l f e i n c ll g e m l p l i a m g t r h o a w t t i i l o a it n y y Generatio Tr S a k je in c F to B r y S i e n n S e k s i c n e A nc g e in g DNA−binding transcription factor binding 0.05 regulation of intrinsic apoptotic signaling pathway intrinsic apoptotic signaling pathway 0.10
positive regulation of ce o ll s a s d if h ic e a s t i i o o n n 0.15 fat cell differentiation embryonic organ development
large ribosomal subunit
respiratory chain complex mitochondrial respirasome SID3 r _ e C s S h p I o D ir n a 4 d S _ s r S A o I o D c I r m D 3 t y e t _ 5 e e r C _ y _ S E S h u I o C k p D i n _ n 4 d u F _ S r p B S A o I c _ D I r D t y u e 3 t 5 p e r _ _ y _ C E S S i h n C k I o t D i e _ n n r 4 i F d n _ B r t S A o e _ c r I r i D n t y e t t 5 e e r _ y _ r E S d C k o i w _ n d F n o B w _ n down C Su h b o t n y d p r e o s cyte
erocS
4DIS
Aortic Endothelial Cell 1.00 ****
0.75
0.50
0.25
0.00
Adjacent Atherosclerotic
Area Core
erocS
3DIS
Cartilage Chondrocyte 1.00 ****
0.75
0.50
0.25
0.00
Adjacent Damaged
Area Area
erocS
5DIS
Skin Fibroblast Cell
Young Old
2_CD
SID3 Score
0.75
0.50
0.25
2_CD
SID4 Score
0.75
0.50
0.25
2_CD
SID5 Score
0.75
0.50
0.25
DC_1
2_CD Condition
Adjacent
Atherosclerotic
Core
DC_1
2_CD Condition
Young
Old
DC_1
2_CD
ll
Resource
A
B
C
D
Condition
Adjacent
Damaged
Area
E
F
Figure4. Quantificationandtrajectoriesofsingle-cellsenescenceinhumantissueaginganddiseases
(A)DistributionofSID3scoresincartilagechondrocytesofosteoarthritis(left),SID4scoresinaorticECsofatherosclerosis(middle),andSID5scoresinskin
fibroblastsofaged(right)humanwiththeirrespectivecontrols,asdeterminedbyWilcoxontest(p<0.0001).
(legendcontinuedonnextpage)
CellMetabolism36,1126–1143,May7,2024 1133
ll
Resource
(SID3) in osteoarthritis, aortic endothelial cells (ECs, SID4) in thebroadsenescencefeaturesofthesetwofactors,theyhave
atherosclerosis,andfibroblasts(SID5)inskinaging(Figure4A). beenprimarilyreportedtoinducesenescenceinprostatecancer
Similar to senescent AT2 cells, these cells with highest SID and repress senescence in mice primary tail fibroblast cells,
scores (Cell_q4) have significantly higher level in various cell- respectively,113,114whichisconsistentwithourfindings.Overall,
cell interactions than those with bottom SID scores (Cell_q1). the various senescence trajectories revealed by SenCID high-
Amongthem,thereareagainanincreaseinautocrine interac- lightthedynamicsandheterogeneityofsenescencetrajectories
tions to the same cell types (40/383 pairs for chondrocytes in evenwhensharingcommonendpoints.
osteoarthritis,e.g.,VCAN-EGFRrelatedtoextracellularmatrix; Consistent with the notion that senescence as a progressive
26/385 pairs for aortic ECs in atherosclerosis, e.g., DKK2- processtowardanendpoint,4,59thesingle-cellsenescencetrajec-
LRP6relatedtoWNTpathway112;and10/143pairsfornormal toriesshowgradualincreaseinSIDscores(Figures2Fand3A,
agedskinfibroblasts,e.g.,CCL2-ACKR4relatedtochemokine etc.),suggestingthatitmightbearbitrarytodefineabinarizedse-
signaling)(Figure4B;TableS4). nescentstateatsingle-celllevel.However,togiveanintuitiveyes-
We construct senescent trajectories for these different cell or-nojudgment,onecanestimateathresholdfortheSIDscoresto
types using their respective SID-related senescent markers in binarizethe senescent states, where the senescence-up genes
BTD(SID3/4/5-upsandSID3/4/5-downs)(Figure4C),whichalso begin to increase sharply along a senescence trajectory (STAR
track along the partition of disease states or age groups (Fig- Methods).The expression increaseofthese upregulated genes
ure4D).Wefinddistinctgeneexpressionpatternsalongthetrajec- often accelerates around the endpoint of the trajectories (e.g.,
tories among cells from different SIDs (Figures 4E and S6C). FiguresS5DandS6C).Intheskinfibroblasttrajectory,weidenti-
Senescentchondrocytes(SID3)inosteoarthritisupregulateextra- fiedtheelbowpointofthisacceleration,correspondingtoaSID
cellularmatrix-relatedgenesanddownregulatedifferentiationand scorearound0.549(FigureS6D),whichiscloseto0.5,thecutoff
development-relatedgenes.Cellsintheintermediatestageofthe employed to classify the senescent samples in bulk-seq data.
trajectoryhighlyexpressedgenesrelatedtoligand-receptoractiv- Applicationofthreshold0.5revealsanestimatedsenescenceratio
ity,whichmaypromotechondrocytesenescencethroughcell-cell of53.2%foragedskinsamples(FigureS6E),consistentwiththe
interactions.AorticECs(SID4)upregulategenesrelatedtomito- reported 20%–60% senescent range of geriatric sun-protected
chondrialrespirasomeanddownregulateribosome-relatedgenes skinfibroblasts.40,115Moreover,thethresholdof0.5-derivedse-
alongthetrajectory,whereasskinfibroblasts(SID5)downregulate nescentcellratiosinChanetal.’sdata(GEO:GSE175533)isnearly
genesrelatedtorespirasomeandupregulateribosomalproteins perfectlylineartoSA-b-galstrainingsignals,104witharegression
andoxidativestressresponse.Transient-upgenes(intermediate) slopeof0.986andpvalueof0.00028,indicatingitsabilitytofaith-
areenrichedinendothelialcellmigration/growthfactorsignaling fullybinarizethesenescentstate(Figure2F).Thesamemethodon
foraorticECsandTFbinding/apoptosisregulationforskinfibro- AT2 senescent trajectoriesgives similar thresholdsclose to0.5
blasts,respectively.Theseresultshighlighttheheterogeneityof (0.496 from COVID19 trajectory and 0.485 from IPF trajectory,
senescenceinitiationandendpointindifferenttissuesandunder Figures S6F and S6G). Meanwhile, using the threshold 0.5, we
differentstressconditions. findallthenormalcontrolsamples,eventhosefromagedindivid-
ThepatternsofTFregulonsalongthesenescenttrajectories uals, have low abundance of senescent AT2 cells (<5%, Fig-
alsoexhibitvariations,suchastheupregulationofFOXO1regu- ure S6H), consistent with the reported quantification in mouse
loninchondrocytesenescencebutdownregulationinECsenes- lungs.116Thus,abinarizationoptionforlabelingsenescentcells
cenceinatherosclerosis,bothshowinghighlinearity(Figure4F). atSIDscoreof0.5isprovidedintheSenCIDprogram.
Ontheotherhand,severalTFregulonsdisplaysimilarpatterns
across chondrocytes (SID3) in osteoarthritis, aortic ECs (SID4) SenCIDenablesgenome-widemappingofsenescence
in atherosclerosis, and fibroblasts (SID5) in skin aging trajec- triggersandsuppressorsfromsingle-cell
tories. Notably,amongthem,ZBTB7Aregulonalsosharesthe perturbationdata
same upregulation in all the lung epithelial cell AT2 senescent Next, we investigate whether SenCID can be used in high-
trajectories,andUSF2regulonsharesthesamedownregulation throughput single-cell CRISPR screens, such as CROP-
inthreeofthefour(excepttheCOVID-19)AT2senescenttrajec- seq117,118orPerturb-seq119,120toidentifygenome-widesenes-
tories(Figure3F).Whilethereisnopreviousevidencesupporting cence trigger and suppressor genes. To test this, we apply
(B)Circosplotdisplayingthetop50protein-proteininteractionsthatdiffersignificantlybetweenmostsenescent(Cell_q4)andleastsenescentcells(Cell_q1)of
cartilagechondrocytesofosteoarthritis(left),aorticECsofatherosclerosis(middle),andskinfibroblastsofaged(right)humantissues.Annotationsarethesame
asinFigure3B.
(C)TrajectoriesconstructedbydiffusionmapofcartilagechondrocytesbasedonSID3-upandSID3-downgenesets(left),aorticECsbasedonSID4-upand
SID4-downgenesets(middle),andskinfibroblastsbasedonSID5-upandSID5-downgenesets(right),coloredbytheirrespectiveSIDscores.Senescent
trajectoriesareindicatedbygam-smoothedlinesofdotcoordinates.
(D)Sametrajectoriesin(C)coloredbydiseasestatesoragegroups.
(E)GOtermsenrichedintheupregulated,intermediate,anddownregulatedgenegroupsalongthesenescenttrajectoryin(C).Thetop5termsrankedby(cid:1)log
BH-correctedpforeachgroupareshown.
(F)Heatmapsofregulonswithspecificandsimilardynamicpatternsalongtrajectories.Row-scaledgam-smoothedregulonactivitiesareindicatedbythemain
colorbar.Upregulatedanddownregulatedregulonswithtop5significantlinearity(minimumBH-correctedANOVApforparametriceffects),intermediate
regulonswithtop5significantnon-linearity(minimumBH-correctedANOVApfornon-parametriceffects),andup-anddownregulatedregulonswithsignificant
commonpatternsinallthreetrajectories.
SeealsoFiguresS6andS7.
1134 CellMetabolism36,1126–1143,May7,2024
0.8
0.6
0.4
0.2
0.0
Unassigne
N
d onTargeting BRCA1 PTPRD RB1 ARID1B TP53 MultiTargeting OtherTargets
RPE1 Perturbed GSEA
vacuolar proton−transporting V−type ATPase
complex
vacuolar membrane
structural constituent of ribosome
structural constituent of cytoskeleton
sister chromatid segregation ribosomal subunit
response to unfolded protein response to topologically incorrect protein
respira re to s r p y o n ch se a in to c h o y m p p ox le ia x |NES| proton−transporting V−type ATPase complex 1.5 protein localization to endoplasmic reticulum
proteasome complex 2.0 primary active transmembrane trans a p c o ti r v t i e ty r 2.5 positive regulation of cell−substrate adhesion 3.0 nuclear division nuclear chromosome segregation mitotic sister chromatid segregation Sign
mitotic nuclear division
mitochondrial respirasome Up extracellular G st o r l u g c i t v u e re si c o l r e g a tr n a i n z s a p ti o o r n t Down
extracellular matrix structural constituent
external enca e p x s t u ra la c t e in ll g u l s a t r r u m c a tu tr r i e x o o r r g g a a n n i i z z a a t t i i o o n n −logP_adj endoplasmic reticulum m e to d i G at o e l d g i t r v a e n s s ic p l o e r − t 2
cytos e o n l d ic o s c m yt a ic l l v r e ib s o ic s l o e m m a e l m su b b ra u n n e it 4 cytosolic ribosome 6
cytosolic large ribosomal subunit 8 cytoplasmic translation
COPII−coated ER to Golgi transport vesicle
condensed chromosome
coated vesicle membrane
chromosome segregation
basement membrane
autophagosome
Grou
G
p1 rou
G
p2 rou
G
p3 rou
G
p4 rou
G
p5 rou
G
p6 rou
G
p7 rou
R
p
e
8 press
erocS
2DIS
Dox-treated MCF10A CROP−seq
ns * * *** ** **** ** ns
6
3
0
−3
−6
−10 −5 0 5 10
UMAP_1
2_PAMU
RPE1 Perturb−seq
SID3 Score
0.75
0.50
0.25
1.00
0.75
0.50
0.25
0.00
non−targeting 1 2 3 4 5 6 7 8 OtherTargets
erocS
3DIS
RPE1 Senescence-Promoting Perturbation
PerturbGene Group
Senescence-Suppressing Perturbation Targets
30 ADAT2 LP E A FR3A
ACTR1AGSDMA Golgi vesicle transport THRAP3 20 CABIN1GAPDHYRDCARL4D
MCL1 10 c ri y b t o o s s o o m lic e ZR O S T R X 2 1 ACT P R S 1 M B C E D L 2 K D F 2 X B 1 L W 9 IM B D 1 R TW T 54 IM F N 1 M AG 8A LU TFRC PG S D H A 2 R A S F P 2 Z A T C E T N B
HIST1H2AI S100A1 0 FBXO42 CDK2 CCDC6
−10 RNA splicing AARS2
R bi i o b g o e s n o e m s e is Proteasome
−20 HNRNPA1 DNA replication, Chromosome Segregation COMTD1
−20 −10 0 10 20 −5 0 5
tSNE1 Top GO Term tSNE1
nucleosome binding locomotor rhythm
dynactin complex tRNA binding
TSEN54 SF3A3SNRPE UTP18
SRSF3PTBP1
PSMG1 CTPS1 BUB1B RBBP7SUPT16H KIF14 HNRNPD
PA2G4 PIF1 MELK TRIP13 NUDC RAD51 VRK1 M RR C M M M 1 6 C P M M O C L 3 M A 5 S2KA D 3 UT A N S C F1 L B RA R D F 5 C 1A 3 P1E P I A F R 2 P S 1 1 U E H 2 R F F 1 1 C B D U C B A 3 8 P SS C R B P P 1 1 N S U T D I C P D 1 2 P G A T F F 1 2H3 MCM2 RFC4 XPO1 POLD3 MCM10PTGES3 NEK2
GINS2 CDT1 DTL TCP1 AURKB KIF20AEXOSC2CAPRIN1CHEK1
HNRNPA2B1GDI2 MAD2L1 CDC6 CCT3 MRPL41
TIMELESSTOE1 CDC45RAB8A CENPA RFC5 FKBP5 RRP7A
EXOSC9 NOL11
TRAPPC5 EXOS E C X 8 OSC10
PSMA3 GNL3DKC C 1 CT5
Perturbation Positive correlation Shared by Networks
Group Negative correlation 1 2
1 5
Node Type
2 6 3 5
Source 3 7
Mediator 4 8
2ENSt
Senescence-Promoting Perturbation Targets
Translation &
Post-translation modification / Transportation
RNA PolII transcription regulator complex
Perturbation 1 3 5 7
Group 2 4 6 8
no enriched function
20
15
10
5
0 NC NC SARS2 HNRNPA1
P
GD PTEN ACTB
siRNA KD
)%(
aerA
evitisoP
lagß−AS
20
15
10
5 0 NC UTP11 P WP1 AA MP MAK16 NEPRO WDR12
siRNA KD
**** ns ns *** * ns
+Bleomycin
)%(
aerA
evitisoP
lagß−AS
ll
Resource
A B
C
E
D
F Senescence-Promoting Perturbation Targets * * *** ** * ***
siNC H
siWDR12 100μm
G
Senescence-Suppressing Perturbation Targets
siNC
siPGD +Bleomycin
siPTEN
100μm
(legendonnextpage)
CellMetabolism36,1126–1143,May7,2024 1135
ll
Resource
SenCID to CROP-seq data from the MCF10A immortalized itiveforSA-b-galstaining(Figures5F,S8I,andS8J),whiletwoof
breastepithelialcellline,118whichisaSID2celltypeaccording thetopsenescence-suppressingperturbationtargets,phospho-
toourclassification(FiguresS8AandS8B).Ouranalysisshows gluconate dehydrogenase (PGD) and PTEN, when knocking
a significant increase in senescence probabilities in cells downamelioratedtheSA-b-galelevationinducedbybleomycin
treatedwithDNA-damagingreagents(FiguresS8CandS8D), (Figures5G,S8I,andS8J).
whileknockdownoftumorsuppressor,particularlyTP53,leads In order to decipher the molecular pathways mediating the
toasignificantdecreaseinSIDscores(Figure5A).Thesefind- perturbationstosenescencesignatures,weemployeResponse-
ingsconfirmthatSenCIDcancapturechangesinsenescence Netanalysis,121whichidentifiessubnetworkswiththelargestin-
levelsinducedbychemicaltreatmentorgeneeditinginsingle formationflowbetweenthesourceandeffectgenesets(STAR
cells. We further apply SenCID to Perturb-seq datasets from Methods).Usingalleightgroupsofsenescence-promotingper-
single retinal pigment epithelial cells (RPE1) and chronic turbedgenesasthesource,wefindthatthelargestsubnetwork
myeloidleukemiacells(K562)withthousandsofgenesindivid- fromeResponseNetprimarilycontainsgroup2perturbedgenes
uallysilenced.120 (Figures5DandS8K),indicatingthatgroup2perturbationsare
We find that RPE1 cells are classified as SID3 (Figure S8E, themostdirectcauseofsenescence.Thisisfurthersupported
sameasinBTD,Figure1B)andexhibitanoverallsenescence byindividualeResponseNetsforeachperturbationgroup,which
rateof38.3%inperturbedcellscomparedwith18.8%innon- showmanygroup2genesasmediators(Figures5HandS9A).
targeted control cells (Figures 5B, 5C, and S8F). We identify The top enriched functions of all eight eResponseNets are
839 senescence-promoting and 36 senescence-suppressing DNA replication and chromosome segregation (Figure S9B),
genetic perturbations (Figures S8G and S8H, STAR Methods), while pathways such as telomere lengthening, telomere
with the senescence-promoting perturbations targeting mainly capping,and rRNAand tRNAmetabolisms areenriched when
8 groups of different essential cellular machineries, including onlyconsideringtheflowsbetweenperturbationsandmediators
the cytosolic ribosome, ribosome biogenesis, DNA replication (FigureS9C).FactorssuchasAURKB,NCL,ASF1B,andCDC45
and chromosome segregation, proteasome, RNA splicing, are common mediators in multiple networks (Figures 5H and
RNApolymeraseIItranscriptionregulatorcomplex,Golgivesicle S9A).Thesefindingssuggestthatgroup2genesarethecentral
transport,andproteintranslationandpost-translationmodifica- determinators for cellular senescence, while all other senes-
tion and transports. These perturbations induce senescence cencemodulatorgroupsactthroughthem.
through similar changes to transcription profiles within the K562,thep53-deficientcancercellline,isdifficulttobecome
samefunctionalgroup(Figure5D).Genesetenrichmentanalysis senescent,despitesenescence-inducible bycertaintherapies,
(GSEA) reveals senescence-related functional terms, such as such as imatinib.122,123 SenCID classifies it into SID6 (Fig-
commonly reduced chromosome segregation and elevated ure S10A) and as expected, reveals very few senescent cells,
lysosome components and autophagy, and different changing regardless of perturbation (0.031%) or not (0%) (Figures 6A,
patternsofstressresponsesandribosomalproteins(Figure5E; S10A,andS10B). Only37perturbations arefoundtopromote
Table S6). The senescence-suppressing perturbed genes are senescence(Figures6B,S10C,andS10D),whichclusterinto6
scatteredinvariousfunctions(Figure5D)andinduceopposite, functionalgroupssimilartothoseobservedinRPE1cells,except
though not-so-strong effects, compared withthe senescence- fortheESCRTcomplexgenesformingauniquegroup.Different
promotinggroups(Figure5E;TableS6). perturbation group induces DEGs commonly enriched for
To validate the identified senescence triggers and suppres- upregulated actin-related functions, myeloid cell activation,
sors, we did SA-b-gal staining experiment on a similar normal and downregulated cytosolic ribosomal proteins; these re-
RPE1cellline,ARPE19.ConsistentwithourSenCIDresult,we sponses are very different from the responses observed in
foundthatknocking downof thetop6senescence-promoting RPE1 cells (Figure 6C; Table S6). The difference in ribosomal
perturbationtargetssignificantlyincreasednumberofcellspos- proteinchangesbetweenSID3and6areconsistentlyobserved
Figure5. SenCIDanalysisofPerturb-seqdata
(A)ViolinplotcomparingSID2scoresofdoxorubicin-treatedMCF10AcellsunderdifferentCROP-seqperturbations.Cellshavingmultiplegene-targetingUMIs
are marked as MultiTargeting, and cells perturbed with non-senescence-inhibiting perturbations are marked as OtherTargets. Significance between
NonTargetinggroupandothergroupsisdeterminedbyWilcoxontest(*p<0.05;**p<0.01;***p<0.001;****p<0.0001).
(B)UMAPvisualizationofPerturb-seqdataofRPE1cellsbasedonhighvariablegenes.
CellsarecoloredbySID3score.
(C)DistributionofSID3scoresofnon-perturbedcellsandcellsperturbedbysenescence-promotingperturbationgroups.
(D)tSNEplotforthetargetgenesofsenescence-promoting(left)andsenescence-suppressingperturbations(right).Eachdotrepresentsoneperturbation,and
theirpositionsonthemaparebasedontheireffectonthecellulartranscriptome.Thedotsarecoloredandcircledbygroupsoftheirmajorgenefunctions.
(E)GSEAresultsofthetranscriptomechangesinducedbydifferentsenescence-promotingperturbationgroupsandsenescence-suppressingperturbationsin
(D).GOtermswithtopandbottom5NESscoresineachperturbationgroup.|NES|>1.
(FandG)SA-b-galstainingofARPE-19cellstransfectedwithsiRNAstargetingsenescence-promotingperturbationtargetswithtopSID3scores(F)and
senescence-suppressingperturbationtargetswithbottomSID3scores(G)in(D),withorwithoutinductionwith20mg/mLbleomycin.QuantificationsofSA-b-gal
positivepercentage(left)andrepresentativeimages(right)areshown.Significancebetween3perturbationandcontrolbiologicalreplicatesisdeterminedbytwo-
tailedStudent’sttest(*p<0.05;**p<0.01;***p<0.001;****p<0.0001).
(H)Summaryofsourceandmediatorgenesfromeachsenescence-promotingperturbationgroup-initiatedeResponseNetofRPE1cells.Nodesarecoloredby
thesenescence-promotingperturbationtargetgenegroupin(D).LinecolorsshowthesignsofPearsoncorrelationbetweengenes.Sizeoftheroundnodes
(mediatorsresultedfromeResponseNet)showsthenumberofnetworksinwhichitisamediator.
SeealsoFiguresS8andS9.
1136 CellMetabolism36,1126–1143,May7,2024
5.0
2.5
0.0
−2.5
−5.0
−7.5
−5 0 5
UMAP_1
K562 Perturbed GSEA
translation elongation factor activity
tertiary granule
structural constituent of ribosome rRNA processing
rRNA metabolic process
ribosome biogenesis
ribosome
ribosomal subunit
ribosomal large subunit biogenesis
ribonucleoprotein complex biogenesis Sign
regulation of actin cytoskeleton organization
proteasome regulatory particle Up
proteasome complex Down
proteasome accessory complex
preribosome
phagocytic vesicle membrane phagocytic vesicle |NES|
peptidase complex
organelle inner membrane 2.0 organellar small ribosomal subunit organellar ribosome 2.5
myeloid cell activation involved in immune
response 3.0
mitochondrial small ribosomal subunit mitochondrial ribosome
mitochondrial protein−containing complex mitochondrial large ribosomal subunit −logP_adj
mitochondrial inner membrane large ribosomal subunit 2
extracellular matrix 4
external encapsulating structure
endopeptidase complex 6
endocytic vesicle membrane
cytosolic small ribosomal subunit 8 cytosolic ribosome
cytosolic large ribosomal subunit
cytoplasmic translation
collagen−containing extracellular matrix actin filament organization
actin filament binding
actin filament−based process
actin cytoskeleton organization actin binding
Group1 Group2 Group3 Group4 Group5 Group6
inBTD(Figure1D).Notably,unlikeinRPE1cells,differentsenes- DISCUSSION
cence-promotingperturbationgroupsinK562cellselicitnearly
nooverlapineResponseNet flows,withtheirmediators enrich In summary, our SenCID program is an innovative machine
fordifferentfunctions(Figures6DandS10E).Nevertheless,the learning algorithm capable of identifying senescence in both
mostcommonlyenrichedfunctionsoftheeResponseNetnodes bulkandsingle-celltranscriptomedata.Itquantitativelyassesses
are ribosomal function related (Figures S10F and S10G), indi- senescencestatesandheterogeneityincelllinesorprimarytis-
cating that ribosomal function decline is a central pathway for sues in aging and aging-related diseases. Our models reveal
senescence in SID6 cells, where cell cycle checkpoint genes that cells can be classified into six different SID categories,
likep53aredisabled(FiguresS3FandS10H). with differing baselines of senescence inversely correlated to
2_PAMU
K562 Perturb−seq
Transcription
coregulator
activity
50
SID6 Score
0.75
0.50 0 ESCRT
0.25 complex
−50 Cytosolic
Proteasome ribosome
−100
−100 −50 0 50 100
tSNE_1
Perturbation Positive correlation Shared by Networks
Group Negative correlation 1
1 4
2 5 Gene Expression 2
Source 3 6
Mediator
2_ENSt
ll
Resource
A B Senescence-Promoting Perturbation Targets
RNA splicing,
Protein modification
/ Transportation
PerturbGene
Group 1
2
3
DNA replication, 4
Chromosome Segregation 5
6
C
D MCM10 VPS28
DHX9 EEF2 SYNCRIPGTF2B RAC2 GINS2 EIF3I RUVBL1HSPA8 SLBP
RPS3APOLR2CPTBP1 UBE2M CCNA2COPS5SNRPC DTYMK RXRB PAICS
PSMB7 TPT1 NEDD8 ERH SRSF2 TMOD1GABARAPMRPL47 SOD1 SLC25A6
CCT8 NDUFS3 PTMA CUL1MAP1LC3BUBA52 PWP1 MCM3 RPL26 PSMA6
RPL10A PSMC4
MCM7 PSMA3PSMD8EIF3G CDC45 SF3B1 POLR2JPRKDCCHMP4ANCOA3 PSMD7
RPL27AEP300 IDH3A RPL7 RBX1 GMNN MTHFD1 LYAR CCT2 WDR33 MED1 PSMC6
AHSA1 TSG101 RPL3 MCM4 CCT7 NIFK YBX1 TYMS RAD23B VCP PSMC P 2 SMD6
RPL13A UBC ENO1 NUDC EEF1A1GTPBP4RPS18 RPS6 PARK7 SNRPB
COMMD3PSMC5 DUT PCNAEBNA1BP2HIST1H4CCDC25AUCHL5 CCT3 XPA
GAR1 HNRNPDPSMB6HSPA1A KIF11 CENPMPSMC3 SNF8 UBE2V2PTGES3
TAX1BP1RANBP1UBE2D2EEF1G RRM2 RAN NASP MRPL21HSPA4RAD23A
CSE1L RPS11
MED17 GPS1
Figure6. SenCIDanalysisofPerturb-seqdatainK562cells
(A)UMAPvisualizationofPerturb-seqdataofK562cellsbasedonhighvariablegenes,withcellscoloredbySID6score.
(B)tSNEplotforthetargetgenesofsenescence-promotingperturbationsonK562cellline.Eachdotrepresentsoneperturbation,andtheirpositionsonthemap
arebasedontheireffectonthecellulartranscriptome.Thedotsarecoloredandcircledbygroupsoftheirmajorgenefunctions.
(C)GOtermswithtopandbottom7GSEANESscoresforeachperturbationgroup.Only|NES|>1.5andp_adj(BH-correctedp)<0.05termsarepresented.
(D)Summaryofsourceandmediatorgenesfromeachsenescence-promotingperturbationgroup-initiatedeResponseNetofK562cells.Nodesarecoloredby
thesenescence-promotingperturbationtargetgenegroupin(B).FormatisthesameasinFigure5F.
SeealsoFigureS10.
CellMetabolism36,1126–1143,May7,2024 1137
ll
Resource
stemness, distinct senescence signatures, and varying re- STAR+METHODS
sponsestosenolytics.SenCIDalsoenablesthedissectionofhet-
erogeneityandreconstructionofsenescenttrajectoriesandhas Detailedmethodsareprovidedintheonlineversionofthispaper
uncoveredpotentialregulonsforchronichumandiseases,normal andincludethefollowing:
humantissueaging,andCOVID-19.Wehavefoundthatsenes-
d KEYRESOURCESTABLE
cent cells in each pathological condition not only upregulate
d RESOURCEAVAILABILITY
SASPgenestoinfluenceothercellsbutalsoenhanceSASPau-
tocrineloop,asfoundinmultiplepreviousstudies,124–127further B Leadcontact
B Materialsavailability
highlighting the potential for self-perpetuating regulation as a
B Dataandcodeavailability
targetforbreakingtheviciouscycleofcellsenescence,similar
tothecaseforfibrosis.128Lastly,ouranalysisofsingle-cellPer- d EXPERIMENTALMODELS
B Cellcultureandtreatment
turb-seq data reveals that senescence can be induced by the
d METHODDETAILS
disruptionofeightessentialcellularmachineries,withthemajority
B siRNAtransfection
of senescence-promoting perturbationschanneledthroughcell
B Senescence-associatedb-galactosidasestainingand
cycle and chromatin-segregation-related group 2 to induce
quantitation
senescence.Ourfindingsindicateaclearmodularityandhierar-
B Datacollectionandpre-processing
chyamongsenescencemodulators.
B Machine learning and non-machine learning-based
Our study provides deep insights into the ubiquity and
senescenceestimator
complexity of senescence in human tissues during aging and
B SenCIDpackageconstruction
diseases,revealingthefundamentalrelationshipbetweenbasal
B RNA-seqdataanalysisandgenesetenrichment
senescencelevelandstemnessandelucidatingthemodularna-
B Singlecellanalysis
tureofsenescencetriggersconvergingonacoremoduleleading
B eResponseNetnetworkanalysis
to similar senescence endpoints. Importantly, our SenCID tool
d QUANTIFICATIONANDSTATISTICALANALYSIS
allows characterizing senescent patterns that are specific to
certain disease and aging processes, tissues, and cells. Such
patternshavethepotentialtobecomesenolytictargetsiffurther SUPPLEMENTALINFORMATION
verified to be uniquely associated with senescence in at least
one cell type and absent in all others. Therefore, our findings Supplemental information can be found online at https://doi.org/10.1016/j.
cmet.2024.03.009.
and program have practical implications for the development
of targeted senolytics to minimize off-target effects on normal
ACKNOWLEDGMENTS
cellsandmaximizetherapeuticefficacy.
ThisworkwassupportedbygrantsfromtheNationalNaturalScienceFounda-
Limitationsofthestudy tionofChina(92374207,92049302,32088101,and32330017)andtheChina
Currently,Perturb-seqisperformedonimmortalizedorcancer MinistryofScienceandTechnology(2020YFA0804000)toJ-D.J.H.
cell lines,129 and thus, few or no cells undergoing senescence
before perturbation, biasing our analysis toward identifying AUTHORCONTRIBUTIONS
senescence triggers than suppressors. Thus, fold changes of
J.-D.J.H.conceivedtheproject.W.T.performedallanalysisundertheguid-
SIDscoresinsenescence-suppressingperturbationsaremuch
anceofJ.-D.J.H.,andZ.Y.helpedwithfiguredesign.J.-D.J.H.andW.T.wrote
lowerthanthepromotingperturbations.Consistently,compared
themanuscript.
with 6 out 6 experimentally validated senescence-promoting
perturbations, only 2 out of the 5 experimentally tested sup-
DECLARATIONOFINTERESTS
pressingperturbationswerevalidatedunderbleomycininduced
senescence.Thiscouldalsobeduetoalackoffullcoverageof Theauthorsdeclarenocompetinginterests.
senescence-induction conditions by bleomycin treatment.
Received:August18,2023
FuturePerturb-seqonprimarycellsundervarioussenescence
Revised:December15,2023
inductionswouldrevealamorecompletepictureofsenescence
Accepted:March13,2024
suppressors.Nevertheless,westillcanidentifytwoexperimental Published:April10,2024
validatedsenescence-suppressingtargetsfromthecurrentda-
taset. One of which, PTEN, is a well-known anti-cancer gene REFERENCES
that inhibits cell growth. While the other, PGD, is a crucial
enzyme in the oxidative pentose phosphate pathway. Multiple 1.Hayflick,L.,andMoorhead,P.S.(1961).Theserialcultivationofhuman
studiesregardPGDasananti-cancertargetasPGDdownregu- diploidcellstrains.Exp.CellRes.25,585–621.https://doi.org/10.1016/
0014-4827(61)90192-6.
lation selectively inhibits the growth of various cancer cells
throughAMPKpathway,130–132butnoresearchhasstudiedits 2.DiMicco,R.,Krizhanovsky,V.,Baker,D.,andd’AddadiFagagna,F.
(2021).Cellularsenescenceinageing:frommechanismstotherapeutic
regulationofsenescenceinnormal,non-tumorcells.Ourresults
opportunities. Nat. Rev. Mol. Cell Biol. 22, 75–95. https://doi.org/10.
show that knocking down PGD significantly reduced senes-
1038/s41580-020-00314-w.
cence at least in SID3 normal RPE1 cells. This indicates that
3.von Zglinicki, T.,Wan, T.,andMiwa,S.(2021).SenescenceinPost-
PGD reduction might have dual effect of anti-cancer and anti- MitoticCells:ADriverofAging?Antioxid.RedoxSignal.34,308–323.
senescence,makingitaninterestingtargetforfuturestudy. https://doi.org/10.1089/ars.2020.8048.
1138 CellMetabolism36,1126–1143,May7,2024
ll
Resource
4.vanDeursen,J.M.(2014).Theroleofsenescentcellsinageing.Nature 21.Schwartz,R.E.,Shokhirev,M.N.,Andrade,L.R.,Gutkind,J.S.,Iglesias-
509,439–446.https://doi.org/10.1038/nature13193. Bartolome,R.,andShadel,G.S.(2021).Insightsintoepithelialcellsenes-
5.Coppe´,J.P.,Patil,C.K.,Rodier,F.,Sun,Y.,Mun˜oz,D.P.,Goldstein,J., cencefromtranscriptomeandsecretomeanalysisofhumanoralkerati-
Nelson, P.S., Desprez, P.Y., and Campisi, J. (2008). Senescence- nocytes.Aging(Albany,NY)13,4747–4777.https://doi.org/10.18632/
Associated Secretory Phenotypes Reveal Cell-Nonautonomous aging.202658.
Functions of Oncogenic RAS and the p53 Tumor Suppressor. PLOS 22.Avelar,R.A.,Ortega,J.G.,Tacutu,R.,Tyler,E.J.,Bennett,D.,Binetti,P.,
Biol.6,2853–2868.https://doi.org/10.1371/journal.pbio.0060301. Budovsky,A.,Chatsirisupachai,K.,Johnson,E.,Murray,A.,etal.(2020).
A multidimensional systems biology analysis of cellular senescence
6.Rodier,F.,andCampisi,J.(2011).Fourfacesofcellularsenescence.
in aging and disease. Genome Biol. 21, 91. https://doi.org/10.1186/
J.CellBiol.192,547–556.https://doi.org/10.1083/jcb.201009094.
s13059-020-01990-9.
7.Gorgoulis, V., Adams, P.D., Alimonti, A., Bennett, D.C., Bischof, O.,
23.Chatsirisupachai,K.,Palmer,D.,Ferreira,S.,anddeMagalha˜es,J.P.
Bishop,C.,Campisi,J.,Collado,M.,Evangelou,K.,Ferbeyre,G.,etal.
(2019).Ahumantissue-specifictranscriptomicanalysisrevealsacom-
(2019). Cellular Senescence: Defining a Path Forward. Cell 179,
plex relationship between aging, cancer, and cellular senescence.
813–827.https://doi.org/10.1016/j.cell.2019.10.005.
AgingCell18,e13041.https://doi.org/10.1111/acel.13041.
8.He,S.,andSharpless,N.E.(2017).SenescenceinHealthandDisease.
24.Zhao,M.,Chen,L.,andQu,H.(2016).CSGene:aliterature-baseddata-
Cell169,1000–1011.https://doi.org/10.1016/j.cell.2017.05.015.
baseforcellsenescencegenesanditsapplicationtoidentifycriticalcell
9.Childs,B.G.,Baker,D.J.,Wijshake,T.,Conover,C.A.,Campisi,J.,and
aging pathways and associated diseases. Cell Death Dis. 7, e2053.
vanDeursen,J.M.(2016).Senescentintimalfoamcellsaredeleterious
https://doi.org/10.1038/cddis.2015.414.
atallstagesofatherosclerosis.Science354,472–477.https://doi.org/
25.Reyfman, P.A., Walter, J.M., Joshi, N., Anekalla, K.R., McQuattie-
10.1126/science.aaf6659.
Pimentel, A.C., Chiu, S., Fernandez, R., Akbarpour, M., Chen, C.I.,
10.Childs,B.G.,Zhang,C.,Shuja,F.,Sturmlechner,I.,Trewartha,S.,Fierro Ren, Z., et al. (2019). Single-Cell Transcriptomic Analysis of Human
Velasco, R.F., Baker, D.J., Li, H., and van Deursen, J.M. (2021). Lung Provides Insights into the Pathobiology of Pulmonary Fibrosis.
Senescent cells suppress innate smooth muscle cell repair functions Am. J. Respir. Crit. Care Med. 199, 1517–1536. https://doi.org/10.
in atherosclerosis. Nat. Aging 1, 698–714. https://doi.org/10.1038/ 1164/rccm.201712-2410OC.
s43587-021-00089-5.
26.Wang,X.,Ma,L.,Pei,X.,Wang,H.,Tang,X.,Pei,J.F.,Ding,Y.N.,Qu,S.,
11.Borghesan, M., Hoogaars, W.M.H., Varela-Eirin, M., Talma, N., and Wei, Z.Y., Wang, H.Y., et al. (2022). Comprehensive assessment of
Demaria,M.(2020).ASenescence-CentricViewofAging:Implications cellular senescence in the tumor microenvironment. Brief. Bioinform.
forLongevityandDisease.TrendsCellBiol.30,777–791.https://doi. 23,bbac118.https://doi.org/10.1093/bib/bbac118.
org/10.1016/j.tcb.2020.07.002.
27.Jochems,F.,Thijssen,B.,DeConti,G.,Jansen,R.,Pogacar,Z.,Groot,
12.Baker,D.J.,Childs,B.G.,Durik,M.,Wijers,M.E.,Sieben,C.J.,Zhong,J., K.,Wang,L.,Schepers,A.,Wang,C.,Jin,H.,etal.(2021).TheCancer
Saltness,R.A.,Jeganathan,K.B.,Verzosa,G.C.,etal.(2016).Naturally SENESCopedia:Adelineationofcancercellsenescence.CellRep.36,
occurringp16Ink4a-positivecellsshortenhealthylifespan.Nature530, 109441.https://doi.org/10.1016/j.celrep.2021.109441.
184–189.https://doi.org/10.1038/nature16932.
28.Gulati,G.S.,Sikandar,S.S.,Wesche,D.J.,Manjunath,A.,Bharadwaj,A.,
13.Baker,D.J.,Wijshake,T.,Tchkonia,T.,LeBrasseur,N.K.,Childs,B.G., Berger,M.J.,Ilagan,F.,Kuo,A.H.,Hsieh,R.W.,Cai,S.,etal.(2020).
vandeSluis,B.,Kirkland,J.L.,andvanDeursen,J.M.(2011).Clearance Single-celltranscriptionaldiversityisahallmarkofdevelopmentalpoten-
ofp16Ink4a-positivesenescentcellsdelaysageing-associateddisor- tial.Science367,405–411.https://doi.org/10.1126/science.aax0249.
ders.Nature479,232–236.https://doi.org/10.1038/nature10600.
29.Malta, T.M., Sokolov, A., Gentles, A.J., Burzykowski, T., Poisson, L.,
14.Song,S.,Lam,E.W.,Tchkonia,T.,Kirkland,J.L.,andSun,Y.(2020). Weinstein,J.N.,Kamin(cid:1)ska,B.,Huelsken,J.,Omberg,L.,Gevaert,O.,
SenescentCells:EmergingTargetsforHumanAgingandAge-Related et al. (2018). Machine Learning Identifies Stemness Features
Diseases.TrendsBiochem.Sci.45,578–592.https://doi.org/10.1016/j. Associated with Oncogenic Dedifferentiation. Cell 173, 338–354.e15.
tibs.2020.03.008. https://doi.org/10.1016/j.cell.2018.03.034.
15.Chaib,S.,Tchkonia,T.,andKirkland,J.L.(2022).Cellularsenescence 30.Guo,M.,Bao,E.L.,Wagner,M.,Whitsett,J.A.,andXu,Y.(2017).SLICE:
andsenolytics:thepathtotheclinic.Nat.Med.28,1556–1568.https:// determiningcelldifferentiationandlineagebasedonsinglecellentropy.
doi.org/10.1038/s41591-022-01923-y. NucleicAcidsRes.45,e54.https://doi.org/10.1093/nar/gkw1278.
16.Reyes,N.S.,Krasilnikov,M.,Allen,N.C.,Lee,J.Y.,Hyams,B.,Zhou,M., 31.Teschendorff,A.E.,andEnver,T.(2017).Single-cellentropyforaccurate
Ravishankar, S., Cassandras, M., Wang, C., Khan, I., et al. (2022). estimation ofdifferentiationpotency froma cell’s transcriptome.Nat.
Sentinelp16INK4a+cellsinthebasementmembraneformareparative Commun.8,15599.https://doi.org/10.1038/ncomms15599.
niche in the lung. Science 378, 192–201. https://doi.org/10.1126/sci- 32.Gru€n, D., Muraro, M.J., Boisset, J.C., Wiebrands, K., Lyubimova, A.,
ence.abf3326. Dharmadhikari,G.,vandenBorn,M.,vanEs,J.,Jansen,E.,Clevers,
17.Hernandez-Segura,A.,deJong,T.V.,Melov,S.,Guryev,V.,Campisi,J., H.,etal.(2016).DeNovoPredictionofStemCellIdentityusingSingle-
and Demaria, M. (2017). Unmasking Transcriptional Heterogeneity in CellTranscriptome Data.CellStemCell19,266–277.https://doi.org/
SenescentCells.Curr.Biol.27,2652–2660.e4.https://doi.org/10.1016/ 10.1016/j.stem.2016.05.010.
j.cub.2017.07.033. 33.Kim, S., and Kim, C. (2021). Transcriptomic Analysis of Cellular
18.Zhu,Y.,Doornebal,E.J.,Pirtskhalava,T.,Giorgadze,N.,Wentworth,M., Senescence: One Step Closer to Senescence Atlas. Mol. Cells 44,
Fuhrmann-Stroissnigg,H.,Niedernhofer,L.J.,Robbins,P.D.,Tchkonia, 136–145.https://doi.org/10.14348/molcells.2021.2239.
T.,andKirkland, J.L.(2017).Newagentsthattargetsenescentcells: 34.Cohn,R.L.,Gasek,N.S.,Kuchel,G.A.,andXu,M.(2023).Theheteroge-
the flavone, fisetin, and the BCL-X(L) inhibitors, A1331852 and neityofcellularsenescence:insightsatthesingle-celllevel.TrendsCell
A1155463.Aging(Albany,NY)9,955–963.https://doi.org/10.18632/ag- Biol.33,9–17.https://doi.org/10.1016/j.tcb.2022.04.011.
ing.101202.
35.Sati, S., Bonev, B., Szabo, Q., Jost, D., Bensadoun, P., Serra, F.,
19.Gil,J.(2023).Thechallengeofidentifyingsenescentcells.Nat.CellBiol. Loubiere,V.,Papadopoulos,G.L.,Rivera-Mulia,J.C.,Fritsch,L.,etal.
25,1554–1556.https://doi.org/10.1038/s41556-023-01267-w. (2020). 4D Genome Rewiring during Oncogene-Induced and
20.Lee,B.Y.,Han,J.A.,Im,J.S.,Morrone,A.,Johung,K.,Goodwin,E.C., Replicative Senescence.Mol. Cell 78,522–538.e9.https://doi.org/10.
Kleijer,W.J.,DiMaio,D.,andHwang,E.S.(2006).Senescence-associ- 1016/j.molcel.2020.03.007.
atedbeta-galactosidaseislysosomalbeta-galactosidase.AgingCell5, 36.Wang,R.W.,Vigano`,S.,Ben-David,U.,Amon,A.,andSantaguida,S.
187–195.https://doi.org/10.1111/j.1474-9726.2006.00199.x. (2021). Aneuploid senescent cells activate NF-kB to promote their
CellMetabolism36,1126–1143,May7,2024 1139
