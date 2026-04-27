---
source_path: /mnt/c/Users/Administrator/Zotero/storage/MIXLTV8E/Kucinski 等 - 2024 - A time- and single-cell-resolved model of murine bone marrow hematopoiesis.pdf
ingested: 2026-04-23
sha256: 3044b065f4620258
---

Resource
A time- and single-cell-resolved model of murine
bone marrow hematopoiesis
Graphical abstract Authors
IwoKucinski,JoanaCampos,
MelaniaBarile,...,Do´nalO’Carroll,
KamilR.Kranc,BertholdGo¨ttgens
Correspondence
donal.ocarroll@ed.ac.uk(D.O.),
kamil.kranc@icr.ac.uk(K.R.K.),
bg200@cam.ac.uk(B.G.)
In brief
Kucinskiandcolleaguesconstructa
quantitativeandreal-timemodelof
mousebonemarrowhematopoiesisby
combiningscRNA-seqandpersistent
HSClabelingtechnologies.Themodel
revealslineage-andstage-specificself-
renewalanddifferentiationproperties
andexplainshowthesearealteredina
transplantationsetting.
Highlights
d Labelingandtime-seriesscRNA-seqrevealkineticsofHSC
multilineagedifferentiation
d
Modelcapturesinvivoreal-timecellbehaviorconnectedwith
geneexpressionpatterns
d Progenitorsubpopulationsdisplaydiverseself-renewaland
differentiationproperties
d TransplantedHSCsdisplayacceleratedstage-andlineage-
specificdifferentiation
rebmun
llec
.leR
HSC
Meg
HSC
MPP
Ery B cells
CMP LMPP
GMP CLP Bas/
Mast
Mono/DC
Meg Mono Gr Neu
B cell T cell
Ery
Tree model Static scRNA-Seq landscape
Time
Cellular flow model
(differentiation and self-renewal rates)
Kucinskietal.,2024,CellStemCell31,244–259
February1,2024ª2023TheAuthor(s).PublishedbyElsevierInc.
ll
https://doi.org/10.1016/j.stem.2023.12.001
ll
OPENACCESS
Resource
A time- and single-cell-resolved model
of murine bone marrow hematopoiesis
IwoKucinski,1,7JoanaCampos,2,6,7MelaniaBarile,1,3,7FrancescoSeveri,4,5,7NatachaBohin,2PedroN.Moreira,4,5
LewisAllen,2,6HannahLawson,2,6MyriamL.R.Haltalli,1SarahJ.Kinston,1Do´nalO’Carroll,4,5,*KamilR.Kranc,2,6,*
andBertholdGo¨ttgens1,8,*
1Wellcome–MRCCambridgeStemCellInstitute,DepartmentofHaematology,JeffreyCheahBiomedicalCentre,UniversityofCambridge,
Cambridge,UK
2CentreforHaemato-Oncology,BartsCancerInstitute,QueenMaryUniversityofLondon,LondonEC1M6BQ,UK
3CentreforTranslationalStemCellBiology,HongKongSAR,China
4CentreforRegenerativeMedicine,UniversityofEdinburgh,EdinburghEH164UU,UK
5WellcomeCentreforCellBiology,UniversityofEdinburgh,EdinburghEH93BF,UK
6InstituteofCancerResearch,LondonSM25NG,UK
7Theseauthorscontributedequally
8Leadcontact
*Correspondence:donal.ocarroll@ed.ac.uk(D.O.),kamil.kranc@icr.ac.uk(K.R.K.),bg200@cam.ac.uk(B.G.)
https://doi.org/10.1016/j.stem.2023.12.001
SUMMARY
Theparadigmatichematopoietictreemodelisincreasinglyrecognizedtobelimited,asitisbasedonhetero-
geneous populations largely defined by non-homeostatic assays testing cell fate potentials. Here, we
combine persistent labeling with time-series single-cell RNA sequencing to build a real-time, quantitative
model of invivotissue dynamicsformurine bonemarrowhematopoiesis.Wecouplecascading single-cell
expressionpatternswithdynamicchangesindifferentiationandgrowthspeeds.Theresultingexplicitlink-
age between molecular states and cellular behavior reveals widely varying self-renewal and differentiation
properties across distinct lineages. Transplanted stem cells show strong acceleration of differentiation at
specific stages of erythroid and neutrophil production, illustrating how the model can quantify the impact
of perturbations. Our reconstruction of dynamic behavior from snapshot measurements is akin to how a
kinetoscopeallowssequentialimagestomergeintoamovie.Wepositthatthisapproachisgenerallyappli-
cabletounderstandingtissue-scaledynamicsathighresolution.
INTRODUCTION geneous. For instance, common myeloid progenitors (CMPs)4,5
andlymphoid-primedmultipotentprogenitors(LMPPs)6,7arehet-
A continuous flow of cells replenishes blood throughout life to erogeneous at functional and RNA level. Further scRNA-seq
maintainhematopoietichomeostasis.Thisfloworiginatesfrom studies suggested gradual molecular transitions from HSCs to-
hematopoieticstemcells(HSCs)andprogressesthroughacom- ward8distinctlineages,8–10includingspecificstagesoferythroid
plexhierarchyofprogenitors,collectivelycalledhematopoietic differentiation.10Nonetheless,althoughmolecularstatescaptured
stem and progenitor cells (HSPCs). Decades of research have byscRNA-seqcanbepredictiveofprogenitorfatepotentialwhen
revealed immunophenotypically defined HSPCs and their fate assessedinvitro,11–13gaininginsightsintosingle-cellfatesinvivo
potentials,thuspositioningthemwithinthehematopoietichier- duringhomeostasishasremainedmorechallenging.14
archy and establishing the hematopoietic tree model.1,2 Lineage tracing in non-hematopoietic tissue combined with
Although scRNA-seq introduced high-resolution and resolved scRNA-seqhasprovidedinsightsintoprogenitorcelldifferentia-
HSPC heterogeneity, scRNA-seq typically provides snapshot tion to the airway epithelial lineage.15 Nevertheless, such an
measurementswithlimitedtemporalinformation.Thus,thehe- approachhasneverbeenappliedtoacomplexmultilineagedif-
matopoietic tree model, even complemented by scRNA-seq ferentiationprocess,suchashematopoiesis.Furthermore,itre-
data, remains static and qualitative and does not capture the mains unclear whether predictive tissue-scale computational
highlydynamicHSPCbiologyinrealtime. modelsofsteady-statetissuehomeostasisatsingle-cellresolu-
Tofacilitatereal-timemodelingofHSPCdynamics,aprevious tioncanbeconstructedbasedonsuchapproaches.Here,we
study3inducedapersistentfluorescentreporterwithintheHSC reveal high-resolution HSPC kinetics of multilineage bone
compartment and assessed label propagation into progeny by marrow (BM) hematopoiesis in vivo. We combined inducible
flowcytometry.However,immunophenotypinghaslimitedresolu- HSC-labelingtotracklabelpropagationtodownstreamprogeny
tion,andflow-cytometry-definedHSPCsarefunctionallyhetero- duringsteady-statehematopoiesiswithscRNA-seqatdifferent
244 CellStemCell31,244–259,February1,2024ª2023TheAuthor(s).PublishedbyElsevierInc.
ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).
ll
Resource OPENACCESS
timepointsafterlabelinduction.Thisenabledustorevealreal- latingindownstreamcellcompartmentsovertime(Figures1D–
time dynamics and build quantitative cellular flow models of 1F). Internal controls (i.e., vehicle-treated Hoxb5-Tom mice or
BM hematopoiesis. These models describe numbers of cells those lacking Hoxb5CreERT2) showed no labeling (Figure E3A).
produced and transported across the HSPC compartment, Labeled differentiated cells were detectable in PB within 1–
properties thathave sofar only beenmeasured for a selected 2 months post-treatment, with particularly fast contribution to
few subpopulations. Notably, the ample molecular information theplateletlineage,followedbyerythrocytesandmyeloidcells,
allowed us to construct continuous models to associate gene andTandBcellsappearinglater(Figures1E,1F,andE3B–E3D).
expressionchangeswithcellbehaviors,suchasincreasedpro- Weobservednon-decreasinglabelingforatleast9monthspost-
liferationoraccelerateddifferentiation,thusdirectlyconnecting treatment(Figures1D,1E,S1F,andS1G),indicatingthatthela-
tissueandcellularbehaviorwiththeunderpinninglayerofmolec- belispersistentandinert.
ularprocesses.Finally,wedemonstratethatourdynamicHSPC Computational inference of population dynamics relies on a
modelistransferableandabletopredictHSPCfateoutcomes simple principle (Figure 2A): as heritable label propagates
basedonpublisheddatasets. downfromthelabel-richupstreamcompartment,thespeedof
differentiation is proportional to label equilibration (Figure 2B,
RESULTS see STAR Methods). To benchmark our experimental model,
we compared flow cytometry data obtained from tamoxifen-
Hoxb5-CreERT2-TomatoreportertracksHSC treated Hoxb5-Tom mice with previously published results of
differentiationovertime analogous label propagation obtained with Tie2-YFP mice.3
To analyze HSPC dynamics, we aimed to employ a labeling OurdataarehighlyconsistentforbothMPP/HSC andHPC-1/
approach (based on principles from Busch et al.3), in which an HSC relative abundances across the entire time range (Fig-
inducible HSC-specific CRE excises a STOP cassette in the ure 2C), thus validating our transgenic models and unlocking
Rosa26-LoxP-STOP-LoxP-tdTomato(R26LSL-tdTomato)reporterto ournextgoal—modelingofpopulationdynamics.
permanently label HSCs and their subsequent progeny. We
hypothesized that Hoxb5, which is specifically expressed in AunifiedreferenceHSPClandscapewithtime-resolved
HSCs,16 is a suitable driver locus. To validate the specificity of differentiation
Hoxb5 expression at the protein level, first we generated TocapturescRNA-seqprofilesofcellstraversingtheHSPCland-
Hoxb5mKO2mice,whereHOXB5andmKO2fluorescentreporter scapeovertime(Figure3A), weharvestedBMfromtamoxifen-
expressionisdrivenbytheendogenousHoxb5locus(FigureS1A). treatedmiceat9timepointsrangingbetween3days(providing
mKO2 expression was selectively confined to the BM just enough time for Tom protein expression) and 269 days,
Lin(cid:1)Sca-1+c-Kit+ (LSK) HSPC compartment (Figures S1B–S1D, whenthelabelismostlyequilibrated.Next,wesortedandpooled
extendeddataFigureE1A,extendeddatafigures‘‘E’’areavail- together cells from two overlapping Lin(cid:1)cKit+ and Lin(cid:1)Sca1+
ableinMendeleyData,seekeyresourcestable).Althoughhigh populations, which contain all HSPCs9 (Figure E3E). To ensure
mKO2expressionwasexclusivetotheLSKCD48(cid:1)CD150+HSC accuracy and reproducibility, we profiled multiple independent
fraction and enriched for this population (Figures S1B–S1D), biological replicates for each time point (36 animals in total).
low-level expression was also detected in LSKCD48(cid:1)CD150(cid:1) Although our focus was labeled Tom+ cells, we also profiled
multipotentprogenitors(MPPs)(FiguresS1B–S1D).Atthefunc- Tom(cid:1) cells at each time point to obtain accurate background
tionallevel,weobservedrobustlong-termmultilineagerepopula- celldensityincaseitchangesovertime.Wegeneratedacommon
tionactivityofmKO2+HSCsuponserialtransplantation.Notably, referencelandscapebyintegratingalldatafollowedbyclustering,
chimerism in the HSC compartment of primary recipients was UMAPembedding,andmanualannotation(Figures3B,3C,and
significantlylowerinthemKO2(cid:1)cohort,andmKO2(cid:1)HSCsfailed S2A–S2E). Clusters disjointed from the main landscape body
to efficiently sustain all lineages in secondary recipients (mostlymaturecelltypes)andthoserepresentingtechnicalarti-
(Figures S1E and E1B–E1D). Furthermore, scRNA-seq demon- facts (e.g., doublets or dying cells) were excluded (unfiltered
stratedthatmKO2+cellsexpresscanonicalHSC-affiliatedgenes, datainFiguresS2FandS2G).Therefinedlandscape(>115,000
displaythehighestHSC-score (FiguresE2A–E2C),17andtightly cells)servedasthebasisforouranalysis.Toplaceourdatawithin
occupytheregionofthemostimmaturestemcellsonhigh-reso- thebroaderscopeofhematopoiesisresearchandextenditsinter-
lutionHSPClandscape7(FiguresE2D–E2F).Altogether,HOXB5 pretability,weprovidemultiplelayersofannotation.Manualanno-
selectivelymarksHSCswiththelong-termmultilineagereconsti- tation9,12 used lineage marker expression, cell-cycle phases,
tutionpotentialandstemcellsignature. HSC-score (molecular signature of long-term repopulating
Having validated Hoxb5 as a suitable locus, we generated HSCs—LT-HSCs17),andpseudotime(Figures3A–3D;TableS1)
Hoxb5CreERT2 mice16 and crossed them with R26LSL-tdTomato to highlight the upstream cluster containing HSCs (Figure S2C)
reporter18 to establish the Hoxb5CreERT2;R26LSL-tdTomato mice (cluster0)and8terminalclusters(Figure3C),whereclearexpres-
(referredtoasHoxb5-Tom,Figure1A),whichallowforinducible sionofdefinitivemarkersisobserved.Pleasenotethatwereferto
labelingofHSCsinsitubytamoxifenadministrationandsubse- thepopulationsasterminalwithintheconstraintsofourstemand
quenttrackingofHSCprogenyovertime(Figure1B).Tovalidate progenitorlandscape,butmostofthemarenotmaturecells,and
thissystem,weusedflowcytometrytotracklabelpropagation cellsdifferentiatebeyondourlandscape.Toaddfunctionalinfor-
acrossBMHSPCsubpopulationsanddifferentiatedperipheral mation,wemappedexternalscRNA-seqdatasetsusingourCell-
blood (PB) cells at indicated intervals (Figures 1B–1F, S1F, projectpackage.First,weoverlaidcanonicalimmunophenotypic
S1G,andE3).Upontamoxifenadministration,weobservedspe- subpopulationswithourscRNA-seqlandscape(Figures3D,3E,
cificlabelingof1.8%ofHSCs,withthelabelgraduallyaccumu- S3A, and S3B) (data from Nestorowa et al.7) comprising highly
CellStemCell31,244–259,February1,2024 245
A B
Hoxb5-Cre-ERT
Rosa26>STOP>Tom
8-12 weeks
0.5-9 months
old
Tamoxifen BM/PB collection
(7 days) + flow cytometry
C
D
40
30
20
10
3
2
1
0
0.5 1 2 3 5 9
E
)%(sllecMB+moT
LSK HSCs MPPs HPC-1 HPC-2
0.5 1 2 3 5 9 0.5 1 2 3 5 9 0.5 1 2 3 5 9 0.5 1 2 3 5 9
Timepost-labelling(months)
12
10
8
6
4
2
0
0 1 2 3 4 5 6 7 8 9
Timepost-labelling(months)
)%(sllec+moT
ATG STOP 1kb
Hoxb5 locus Hoxb5 coding region
UTR
P2A
ssDNA ERT2-RCI CRE-ERT2
ATG STOP
Hoxb5CreERT2
F
Peripheralblood 12
10
Granulocytes 8
Monocytes 6
B cells
T cells 4
2
0
0.5 1 2
Timepost-labelling(months)
)%(
sllec
BP+moT
HPC-1 HPC-2
K+S- S+K+
Lin-
MPP HSC
FSC-A FSC-A
HSC MPP HPC-1 HPC-2
Erythrocytes Platelets
0.5 1 2
Timepost-labelling(months)
H-CSF
IPAD/niL
tiK
FSC-A Sca1 CD150
Tomato Tomato Tomato
A-CSS
K+S- S+K+
(LSK)
Tomato Tomato
A-CSS
Tomato
A-CSS
84DC
ll
OPENACCESS Resource
Figure1. Hoxb5-Tompersistentlabelingenablestime-resolvedtrackingofHSCsandtheirprogeny
(A)TargetingstrategytogeneratetheHoxb5CreERT2allele.
(B)Hoxb5-TommiceweretreatedwithtamoxifenandlabelfrequencywasanalyzedinBMandPBcellswithin0.5–9monthspost-treatment.
(C)RepresentativeflowcytometrygatesusedforisolationofHSPCsubpopulationsandTom+cellsfrommouseBM.Tomlabeling(red)isshownineach
populationcomparedwithcontrolcells(blue).FACSplotscorrespondtomouseanalyzed3monthsafterlabelinduction.
(D)PercentageofTom+cellsintheBMHSPCsubpopulationsat0.5(n=5),1(n=3),2(n=8),3(n=10),5(n=4),and9(n=7)monthsafterlabelinduction.Dots
representindividualmice,barsindicatemean±SEM.
(EandF)PercentageofTom+cellsinPBoflymphoid/myeloidcellcompartments(E)anderythrocytes/platelets(F).Datarepresentmean±SEM(n=4–32
animals).LSK,Lin(cid:1)Sca1+cKit+;HSCs,LSKCD150+CD48(cid:1);MPP,LSKCD150(cid:1)CD48(cid:1);HPC-1,LSKCD150(cid:1)CD48+;HPC-2,LSKCD150+CD48+cells.
246 CellStemCell31,244–259,February1,2024
A
n
slope
Differentiation Flux
rate n cells * slope
C
purifiedLT-HSCs,MPPs1and3,ST-HSCs,granulocyte-mono- reference for the latter, a more advanced continuous modeling
cyteprogenitors(GMPs),LMPPs,andmegakaryocyte-erythroid approach, which focuses on specific trajectories, but provides
progenitors(MEPs).Second,wehighlightedcellstatesassociated cellular flux parameter estimates for each single cell and thus
withspecificcellfateoutcomesbasedoninvitrolineagetracing directly connects single-cell transcriptomic profiles with tissue-
experiments12(Figures3FandS3C).Importantly,theinvitrocell scalecellularbehavior.
potency is broadly aligned with the manual cluster annotation.
Finally, we included information about the active/inactive HSC DiscretemodelrevealsHSPCswithlineage-specific
status under proliferative challenge based on lineage tracing patternsofself-renewalanddifferentiation
datafromBowlingetal.20(Figure3G).Together,theseannotations TocapturetheflowofcellsthroughtheHSPCcompartmentin
placecellclustersintoafunctionalframeworkfacilitatinginterpre- realtime,weutilizedtheconceptsfrompreviouslabelpropaga-
tationofthepopulationdynamicsmodelsdiscussedbelow. tionstudies3,22tobuildadiscretemodelconsistingofmultiple,
TheHSPClandscapesplitbytimepointshowsclearpropaga- interconnected cell clusters (Figures 4A–4C). We explain two
tionoflabeledcells(Figure3H),afullquantificationoflabeled/un- variables changing over time: number of labeled cells (Tom+
labeledcellratiosforalltimepointsisprovidedinFigureS4Aand cells, Figures 4D and E4; Table S2) and size (Tom(cid:1) cells, Fig-
followstheexpectedbehavior3(Figure2A).Certainclusters(e.g., ure E5; Table S2) for each cluster (labeling frequency in Fig-
8and7)veryquicklyaccumulatelabeledcells,othersareslower ureE6).Eachclusterhastwobasicproperties:netproliferation
(clusters 11 or 10) and some very slow (clusters 13 or 14) (numberofdivisionsreducedbythenumberofcellslost,e.g.,
(Figures 3H and S4A). Eventually, the label largely equilibrated, by cell death) and differentiation rates (number of ingoing and
ascomparedwiththeTom(cid:1)population(FiguresS4AandS4B). outgoing cells between clusters per day, scaled to a single
Importantly,scRNA-seqclusteringresolvesheterogeneitywithin cell).Thus,ourmodelsimultaneouslyestimates(net)proliferation
cell populations defined by conventional flow cytometry gates balancing it with the influx, efflux, and time-dependent cluster
(FiguresS3AandS3B)4,7,21andispredictiveofcellfate.12Topro- size.Importantlyacommonsetofparametersfitsbothlabeled
videa quantitativedescription ofpopulationdynamics, weem- andunlabeledcells(exceptcluster0,seethenextsection)indi-
ployedtwotypesofmodels:discreteandcontinuous,eachbuilt catingsimilardynamics.Additionally,weintroducetwoderived
forspecificpurposes.Theformercapturesdynamicsacrossthe parametersusefulforinterpretingcellbehavior(Figure2B).Resi-
entire compartment and intuitively combines hierarchical tree dence time, which corresponds to a half-time of one cell in a
models of hematopoiesis with a quantitative view based on cluster,isthetimerequiredfortheclustertoshrinkby63%(to
morepreciselydefinedcelltypes.Italsoservesasanecessary 1/e of original size, where e is the Euler’s number) in absence
ycneuqerf
lebal
.leR
ycneuqerf
lebal
.leR
Proliferation rate
1 1
MPP/HSC HPC-1/HSC
0.8 0.8
0.6 0.6
0.4 0.4
0.2 0.2
0 0
0 200 400 0 200 400
Time (days) Time (days)
Tie2 data
Hoxb5 data
emiT
Progenitor 1
Tom+ %
Stem cells
Progenitor 2
metS 1.gorP 2.gorP
Progenitor 1
tr
F
a
a
n
s
s
t ition Tom+ %
Progenitor 2
tran S
s
l
i
o
ti
w
on
metS 1.gorP 2.gorP
ll
Resource OPENACCESS
B
Population parameters slope in
slope
out slope
Self-renewal
slope = 0
in
Prolif. -slope
out
Figure2. Labelpropagationcontainsinformationaboutpopulationdynamics
(A)Diagramportrayingtheconceptofinferringpopulationdynamicsfromheritablelabelpropagation.Therateoflabelaccumulationinthedownstreamcom-
partmentsisproportionaltothedifferentiationratebetweenthecompartments.
(B)DiagramsprovidinganalogybetweentheshapeoftheWaddingtonlandscapeandthekeypopulationparametersestimated:differentiationrateisakintothe
slopeofthelandscape;self-renewal(andrelatedresidencetimeorhalf-life)dependontheinput,output,andproliferation;fluxthenumberofcellsmultipliedby
theslope.
(C)ComparisonofTie2-YFPandHoxb5-TomlabelprogressiondisplayedasrelativelabelingfrequencybetweenMPPorHPC-1andHSCcompartments.Red
dots,Hoxb5-Tomdatapoints(seeFigure3)withSEMerrorbars;blacklineandgrayshades,rollingaverageandrollingSEMformatchingTie2-YFPdata.19
CellStemCell31,244–259,February1,2024 247
Lin-
A
((cKit OR Sca1))+
Hoxb5-Cre-ERT
Rosa26>STOP>Tom Tom+
8-12 weeks BM collection
old (3-269 days) Cells isolation QC Discrete model
and sorting Tom-
HSPC scRNA-Seq
Tamoxifen
(7 days) Sca1 Integration landscape Modelling
scRNA-Seq
timepoint mice timepoint mice
days no. (days) no. Batch
correction
3 4 76 2
7 6 112 4
12 4 161 4 Label frequency
27 4 269 4 10x Smart-Seq2 over time Continuous models
49 4
Meg prog HSC
B 7 0 19 C B prog DD
8 4 5 14 Int prog Ly prog
13 pDC GMP
9
1
12
2
6 16 Ery
prog
DC prog
L
M
M
E
P
P
P
15 11 17
10
3
M
C
prog
Eos
Mono/DC prog MPP3
18 Bas/
Neu prog Bas
E FF GG
Mono
LTHSC
(ESLAM) Mono Inactive
MPP1 & Neu Active
STHSC
Neu
HH
3 days 12 days 27 days 269 days
Tom+ Tom+ Tom+ Tom+
tiKc
ll
OPENACCESS Resource
Figure3. Time-resolvedreferenceHSPClandscapeatsingle-celllevel
(A)Hoxb5-Tommicewereadministeredwithtamoxifen.TableindicatestimepointsandmousenumbersusedforTom+HSPCscRNA-seq.Twomicepertime
pointwereusedfortheTom(cid:1)scRNA-seq.
(B)UMAPprojectionoftheintegratedHSPCscRNA-seqlandscape(allTom+andTom(cid:1)cellscombined)withcolor-codedclusters.Outlieroraberrantclusters
wereremovedforclarity(seeFiguresS2FandS2G).
(C)Manualannotationofthelandscapein(B).Mostdifferentiatedclusterswithclearlydefinedlineagemarkersarecolor-coded,intermediateundifferentiated
statesareshowningray(Intprog),clustercontainingHSCsisshowninpink.
(DandE)Projectionfrom(B)ingray,withembeddedandcolor-codedimmunophenotypicpopulationsfromNestorowaetal.data.7Upto60randomlyselected
cellsineachcategoryareplotted.AllcellsareplottedinFigureS3A.
(F)Projectionfrom(B)ingray,withembeddedandcolor-codedcKit+progenitors,basedontheiroutputinlineagetracinginvitrocultures.DatafromWeinrebetal.12
(G)Projectionfrom(B)ingray,withembeddedandcolor-codedHSCswithnodetectedcellularoutput(inactive)orcontributingtohematopoiesis(active)
following5-FUchallengeinmice(datafromBowlingetal.20).
(H)Projectionfrom(B),withHoxb5-Tom+cellsatindicatedtimepointsshowninblue.Nestorowaetal.7populationdefinitions:LT-HSC,lin-cKit+Sca1+CD34(cid:1)Flt3(cid:1);
MPP1, lin-cKit+Sca1+Flt3(cid:1)CD34+CD150+CD48(cid:1); ST-HSC, Lin(cid:1)cKit+Sca1+Flt3(cid:1)CD34+CD150(cid:1)CD48(cid:1); GMP, Lin(cid:1)cKit+Sca1+CD16/32+CD34+; LMPP,
Lin(cid:1)cKit+Sca1+Flt3+CD34+;MEP,Lin(cid:1)cKit+Sca1+CD16/32(cid:1)CD34(cid:1);MPP3,Lin(cid:1)cKit+Flt3(cid:1)CD34+CD150(cid:1)CD48+;CMP,Lin(cid:1)cKit+Sca1+CD16/32(cid:1)CD34+cells.
Prog,progenitors;B,Bcell;Bas,basophils;Bas/MC,basophilandmastcell;DC,dendriticcellprogenitors;Eos,eosinophils;Ery,erythroid;Int,intermediate;Ly,
lymphoid;Meg,megakaryocyte;Mono/DC,monocyteanddendriticcell;Neu,neutrophil;pDC,plasmacytoiddendriticcells.
248 CellStemCell31,244–259,February1,2024
1
0.75
0.50
0.25
0
0103050 100 200
time (days)
ezis
retsulc
.leR
D
7 Meg progenitor 11 Late Ery progenitor
E F G
sllec
dellebal
.leR
sllec
dellebal
.leR
8 Ery/Meg progenitor
data
10 Neu progenitor 12 Bas/MC progenitor 14 Lymphoid progenitor
model
95% conf.
interval
Time (days) Time (days) Time (days)
10 100
Day 3 Day 12 Day 27 Day 269
A B 3.5
3.0
2.5
Static population hierarchy 2.0
(connectivities) 1.5
1.0
7 0 0.5
19
0.0
8 4 5 14
13 C Discrete cellular
1 2 flow model
12 9 6 16
11 3
15 17 10
18
B prog Bas Bas/MC prog
DC prog Eos Int prog
HSC Ery prog Mono/DC prog
Meg prog Ly prog
Neu prog pDC
1 1.5 0.6
0.8 0.4
1
0.6 0.2
0.5
0.4 0
0.2 0 -0.2
1 10 100 1 10 100 1 10 100
0.8 0.5 0.25
0.6 0.4 0.2
0.3 0.15
0.4
0.2 0.1
0.2
0.1 0.05
0 0 0
-0.2 1 10 100 -0.1 1 10 100 -0.05 1 10 100
11 Late Ery prog.
14 Ly prog. 7 Meg. prog
10 Neu prog.
time (days)
log10(cell
number
+
1)
+Time
0b 0a
7 0c
19
8 4 5 14
13 Relative population size
1 2
12
9 6 16
15 11 3
17
10
18
Residence time (days)
1.00 10.00 100.00
<0.5 0.7 11.7 46.9187.5>750
Differentiation flux
(* 1000 cells/day)
2
0
−2
−4
−6
−8
−10
−6 −4 −2
log10(pseudotime change)
)setar
noitaitnereffid(01gol
ll
Resource OPENACCESS
8_7 0_8 3_10 9_11
0_4 2_12 2_3
2_6 4_5 4_2 8_1 1_9
8_4 2_5
0_5
4_8 4_12
2_4
5_4
Figure4. QuantitativediscretemodeloftheHSPCshighlightsprogenitor-specificself-renewalanddifferentiationproperties
(A)AnnotatedUMAPprojectionoverlaidwithPAGAgraphabstractionviewoftheHSPClandscape.Thegraphshowsputativetransitionsbetweenclusters
(relatedtoFigure3B).
(legendcontinuedonnextpage)
CellStemCell31,244–259,February1,2024 249
ll
OPENACCESS Resource
ofanyincomingcells.Residencetimeisdefinedastheinverseof states (Figures 4E and S6G), indicating that discovery of real-
([death+differentiation](cid:1)proliferation)andthusresidencetime time dynamics requires temporal information. Moreover, the
increases as proliferation rate rises, and death/differentiation compartment-wide view clearly shows lineage-specific dy-
ratesdecreaseandviceversa.Finally,fluxdepictsthetotalnum- namics(Figure4C).Megakaryocyteprogenitorsemergethrough
berofcellstransportedbetweenclustersinaunitoftime(i.e.,dif- arapidtransitionviathefast-proliferatingcluster8,whichalso
ferentiationratemultipliedbyclustersize).Welimitedthenum- generateserythroidcells,albeitmoreslowly(cluster1).Substan-
ber of differentiation parameters by assuming that cells travel tial erythroid output is achieved via sequential cell states with
onlybetweenadjacentclusters(i.e.,withhighestPAGA23con- considerable self-renewal (clusters 1 and 9) and proliferation
nectivities—Figure 4A). Although PAGA is a robust method (cluster 9), followed by fast differentiation between clusters 9
withrelativelyfewassumptions,thereiscurrentlynoconsensus and11.Furthermore,myeloidprogenitorstransitionfromcluster
intrajectoryinferencemethodology.Thus,wealsoprovidetools 0eitherintocluster4orviaasharedroutewiththeerythroidand
toexplorealternativetopologies(seeSTARMethods)andapply megakaryocytic progenitors into cluster 8, with gradually
acluster-independent,continuousmodel(seelater). increasing differentiation rates from cluster 2 onward. The
Ofnote,weobservedchangesinrelativeclustersizeovertime myeloidbranchthereforeemploysadditionalprogenitorpopula-
(i.e., the background unlabeled cells), in particular a quick in- tions analogously to the erythroid trajectory, albeit with lower
creaseinrelativeabundance(comparedwithcluster0)ofclus- proliferationrates(FigureS6F).
ters 7 and 8 (>50% in <20 days) and a coordinated relative Thelymphoidtrajectoryisaltogetherdifferentshowingexclu-
decrease in other major clusters (Figures E5 and S5A–S5C). sivelyslowtransitionsviaclusters5and2intocluster14(which
Cluster 0 size also modestly increases size in the same time overlaps mostly with a subset of MPP4 cells). Cluster 5,
frame. Previous tamoxifen-based label propagation studies comparedwiththemoremyeloid-biasedcluster4,proliferates
also observed a quick rise in ST-HSC, MPP2, and MPP3 total and differentiates more slowly, while expressing higher levels
numbers(FigureS5D),butnoexplanationswereprovided.19It of key lymphoid factors, including Flt3, Satb1, Pou2f2 (and to
hadpreviouslybeensuggestedthatapplicationoftamoxifenin- some extent the monocytic factor Irf8, discussed later) (Fig-
terferes with JAK-STAT signaling.24 Consistent with recovery ure E7A). The lymphoid program therefore displays restricted
fromcelldepletioncausedbytamoxifeninterferencewithJAK/ proliferationanddifferentiationratesalreadyfromitsimmature
STAT,thispathwaywasmostactiveinthedepletedclusters7, stages.Plasmacytoiddendriticcell(cluster13,pDCs)differenti-
8inadditiontocluster0(FigureS6A).Toassesshowrecovery ationthroughthelymphoidcluster14andmyeloidclusters6and
fromshort-termcelldepletionmayinfluencemodelparameters, 16issimilarlyslow.Theemergenceofmastcell,basophil,and
wecomparedourmainmodelwithabi-phasicfit,whichpermits eosinophilprogenitorsintheadultBMisunclear.25,26Ourresults
aswitchindifferentiation/proliferationratesbetweentherecov- areconsistentwithamodelwherebybasophilandmastcellpro-
eryandhomeostasisphases,albeitatsomecostofincreased genitors(cluster12)arecontinuouslygeneratedandoriginateat
parameter uncertainty (Figures S6B and S6C). We observed leastbyatransitionfromtheearlymyeloidcluster2butmayalso
changes in 14 out of 58 rates between the two phases have some contributions from other clusters (dashed lines).
(FiguresS6DandS6E;TableS3).Ofnote,allbaroneoftheho- Furthermore, despite limited cell numbers, we observed some
meostasisratesinthebi-phasicmodelareessentiallythesame label accumulation in eosinophil progenitors (cluster 17), most
astheratesinthemainmodel.Wethusexplainandaccountfora likelyoriginatingfromneutrophilprogenitors(cluster10).
previously overlooked side-effect of using tamoxifen for label Interestingly,residencetime(self-renewal)varieswidelyacross
induction. the HSPClandscape,withlineage-specific patterns(Figure4C;
WeformulatedourmainmodelintoagraphinFigures4Cand Table S3). As expected, cluster 0 contains the only perfectly
S6F, where node sizes are proportional to the average cluster self-sustainingpopulation;intermediatepopulationsshowarange
size,nodecolorindicatesresidencetime(ornetproliferationin ofresidencetimes,fromjust2.5daysforerythroid/megakaryo-
Figure S6F) and arrows indicate cell flux (differentiation rate in cytic progenitor (cluster 8), 11 days for monocyte/granulocyte
FigureS6F).Pleasenotethatsometransitionsoccurinfrequently progenitors (cluster2)and upto 53daysfor the medialcluster
(transition rates and their confidence intervals are provided in 4.Thelatterfallsclosetotheresidencetimepreviouslyestimated
TableS3),andwecannotexcludethatsomemayberedundant forMPPs(70days)3andhighlightsthatprogenitorscanalsoshow
(for the discussion on the minimal model, please see the considerableself-renewal.Importantly,cellsinclusters8,2,and4
methodssection‘‘Modelselection’’).Interestingly,differentiation fall within the immunophenotypic CMP and MPP definitions
ratespoorlycorrelatewithsimilaritiesbetweengeneexpression (Figures3D,3E,S3A,andS3B),illustratinghowhistoricallyused
(B)Graphfrom(A)color-codedbytheabsolutenumberoflabeledcellsobservedineachcluster.fouroutof9timepointsareshownforclarity.
(C)Graphabstractionviewofthediscretecellularflowmodel.Sizeofthenodesisproportionaltosquarerootsofrelativeclustersize,nodecolorisproportionalto
theresidencetime(log-scale),arrowsindicatedifferentiationdirections,arrowstemthicknessisproportionaltocellflux.Note:cluster0aisfullyself-renewingand
thusexhibitsinfiniteresidencetime.
(D)Bestdiscretemodelfit(with95%confidenceintervals)forTom+cellnumberinchosenclustersrelativetocluster0.ErrorbarsindicatepooledSEM.
(E)Scatterplotshowingrelationofpseudotimedistancetodifferentiationrates,eachpointcorrespondingtoatransitionbetweenclusters.Onlytransitionsamong
clusters0–12anddifferentiationratesgreaterthan10(cid:1)12areshown.Pleasenotethatinthecaseofthetransitionsbetweenclusters4and8twodifferentiation
ratesareplotted(eachdirection).Bluelineindicateslinearmodelfitwithshaded95%confidenceinterval.
(F)UMAPprojectionoftheHSPClandscape,withcellscolor-codedbysimulatedtimerequiredfor1celltoaccumulateinthecorrespondingclusterstartingfrom
cluster0.Pleasemindthatthecolorislogarithmscaled.
(G)Simulatedrelativeclustersizeofchosenclustersfollowingcompleteablationofcluster0.
250 CellStemCell31,244–259,February1,2024
0.8
0.4
0.0
emitoduesp
A Pseudotime Pf4
0.10 6
0.08 5
4 0.06
3
0.04
2
0.02 1
0.00 0
Day 3 Day7 Day12 Day27 Day49-269
(equilibrated)
15
Pseudodynamics
Diff. rate Net prolif. 10
Parameters Partial differential
0.10 0.5 per cell equation model
5
0.08
0.0 0
0.06 Differentiation rate 0 0.025 0.050 0.075 0.100
−0.5 Pseudotime
0.04
Net prolif. Differentiation
0.02 −1.0
Net proliferation
B Neu. prog. fate probability Pseudotime Elane
0.16 6
0.8 0.14 5
0.4 0.12 4 0.0 0.10 0.08 3
0.06 2
0.04
1 0.02
0
C E
D
F
ytisned
lleC
1.0 0.10
0.5 0.05
0.0 0.00
−0.5 −0.05
−1.0 −0.10
0.000 0.025 0.050 0.075 0.100
Pseudotime
.filorp
teN
Diff.
rate
Cell transitions Meg. prog. fate probability
0.8
0.4
0.0
Diff. rate Net prolif.
0.016
0.6
0.014 0.4
0.012 0.2 0.0 0.010
−0.2
0.008 −0.4
0.006 −0.6
−0.8
Megakaryocyte progenitors Neutrophil progenitors
0.5 0.01
0.0 0.00
−0.5 −0.01
−1.0 −0.02
0.00 0.05 0.10 0.15
Pseudotime
Gene categories
Reactome
Cell cycle
MSigDB Hallmark
G2−M checkpoint
E2F targets
Pseudotime
.filorp
teN
Diff.
rate
4
3
2
1
0
−1
−2
Scaled
expression
4 0.02
2 0.01
0 0.00
noisserpxe
delacS
Diff.
rate
Neu_genes
Cebpe
Clec4a2
Cst7
Elane
Fcgr3
Gfi1
Prtn3
S100a8
Wfdc21
3
2 0.01
1
0 0.00
−1
noisserpxe
delacS
Diff.
rate
TF group 1
Aff3
Dach1
Hhex
Hmga2
Ikzf2
Irf8
Pou2f2
Sox4
Ssbp2
3
2 0.01
1
0 0.00
−1
0.00 0.05 0.10 0.15
Pseudotime
noisserpxe
delacS
Diff.
rate
ll
Resource OPENACCESS
TF group 2
Cebpe
Chd7
Cited4
Gfi1
Med21
Mlx
(legendonnextpage)
CellStemCell31,244–259,February1,2024 251
ll
OPENACCESS Resource
flowcytometrygatescapturepopulationswithvastlydifferentdy- Ofnote,cluster0b showshigh self-renewal (residencetimeof
namics.Wealsonotethatamongsomeintermediateclusters,our 180 days), consistent with high repopulation potential of line-
modelpermitsadegreeofforwardandbackwarddifferentiation age-biasedHSCs.30Altogether,ourdiscretemodelfaithfullyre-
suggesting that some states may exist in an equilibrium, with capitulates cell flux through the HSPC compartment and pro-
each cluster having distinct differentiation properties. Thus, vides a possible explanation of aging-associated changes in
diverse hematopoietic progenitors exhibit widely different, line- HSCbehavior.
age-specificdynamicsconsistentwithdistinctmechanismsmain-
tainingcelloutput. Continuousmodelofhematopoiesisconnectsdynamics
ofgeneexpressionwithcellbehavior
CompositionofthetopHSPCcompartmentchanges Although the discrete model provides compartment-wide dy-
overtime namics,acomplementarymodelisrequiredtoassociategene
Basedonimmunophenotypeannotations(Figures3C–3E),thetop expression changes at the single-cell level with cell behavior,
cluster0containsvirtuallyallLT-HSCandalargesubsetofST- such as increased proliferation or accelerated differentiation.
HSC and MPP1 cells. The overall cluster size increases over For this purpose, we employed a continuous model based on
time (Figures S5B and S5C), reminiscent of previous reports the Pseudodynamics framework.31 For tractability, we consid-
notingtheexpansionofST-HSCsandMPP3sasmiceage(Fig- eredonelineageatatime,basedoncellswithhighestfateprob-
ureS5D).19Ofnote,theHoxb5-Tom-labeledcellswithincluster abilities toward each lineage32,33(Figures 5A, 5B, E8, and E9).
0growalmostexponentially(FigureS5A),whichmirrorstheprevi- Thecontinuousmodelassignsdifferentiationandnetprolifera-
ously reported behavior of Tie2-YFP labeled LT-HSCs19 and is tion rates to each cell (Figure 5A) by solving partial differential
consistent with the observation of dramatic expansion of equationsdescribingcelldensitiesalongpseudotimeoverreal
Hoxb5-,Tie2-,orFgd5-labeledcellsinaginganimals.27Thissug- time. Hence, model parameters and gene expression share a
geststhattheHoxb5andTie2systemsmark,inadditiontothe commonpseudotime(andreal-time)axis,enablingdirectcom-
canonicallyquiescentLT-HSCs,asubsetofimmaturecellswith parison. Of particular interest are states (pseudotime ranges)
highself-renewalorproliferationcapacity. withchangesinproliferationordifferentiationrates.Anincrease
Toinvestigatetheapparentheterogeneitywithincluster0,we in proliferation rates indicates an expansion stage, whereas a
testedmultiplemodelsandputforwardapotentialexplanation, riseindifferentiationratesmarksapotentiallyirreversiblemolec-
whichassumesalogisticgrowthforcluster0andthreesubclus- ulartransition.
ters within in it: a top, perfectly self-renewing cluster 0a, the Wesetouttoanalyzegeneexpressiondynamicsoccurringat
megakaryocyte&myeloid-biasedcluster0b,andthemultipotent suchchangesincellbehavior.Forinstance,correlatingthefirst
cluster 0c(Figure4C,dashed box). Weconstrained cluster0a derivativeofthedifferentiationratesandgeneexpressionhigh-
size and differentiation rate to match previously reported LT- lightscomplexmatchingpatternsandshortlistspotentialregula-
HSCnumbersbutleftclusters0band0csizesunconstrained. torsdrivingcelldifferentiationinanunbiasedmanner(FigureE11,
Wedefinedthetipclusterbyfinelysubclusteringcluster0and extended data Table E1, extended data tables ‘‘E’’ available in
pickingascluster0athesubclusterwiththehighestHSC-score Mendeley Data, see key resources table). A more targeted
(subcluster 8,FiguresS5EandS5F). Reassuringly, thiscluster approachtestsfordifferentialexpressionaroundspecificstages
size is compatible with our model prediction, is enriched for ofdifferentiation(matchingchangesincellbehavior).Forbrevity,
HSC markers Procr and Ly6a, and, most importantly, has a weshowcasethemegakaryocyteandneutrophiltrajectories(Fig-
non-growinglabelingfrequency,asonewouldexpectfromthe ures 5, E9, 10) but also provide analogous analyses for the
candidatetipcluster(FiguresS5G–S5I).Cluster0cremainssta- erythroid and monocytic/dendritic lineages (Figure E9;
ble over time but it proliferates quickly and feeds both down- TablesS4,S5,extendeddataTableE2).AsshowninFigure5A,
stream progenitors and cluster 0b, which in turn grows over megakaryocyte progenitors display characteristic changes in
time (Figures S5B and S5C). Hence, the flux between clusters growth and differentiation rates. Cells rapidly increase their net
0b and 8 increases with mouse age. This is in line with the proliferation early on, ahead of the peak in differentiation and
increasedmyeloidoutput28,29andrelativeproportionofmega- aroundthestagewherePf4(megakaryocytemarker)mRNAbe-
karyocyte-biasedandmyeloid-biasedHSCsinagedanimals.30 comes detectable. In this growth phase, we identified 170
Figure5. Continuousmodelscapturesingle-cellgrowthanddifferentiationratesalongsidetheirmolecularstate
(A)Diagramofmegakaryocytetrajectoryanalysis.Followingthearrows:putativecelltransitions(pseudotimekernel)wereusedtoestimatecellfate,fromwhich
trajectorywasisolated(dashedline).Alongthepseudotimecelldensitieswerecomputedforeachtimepoint(color-codedlines)andanalyzedusingthe
pseudodynamicsframeworkprovidingdifferentiationandnetproliferationrateestimatesforeachcell.
(B)(Left)UMAPprojectionoftheHSPClandscapecolor-codedbycellfateprobabilityofneutrophillineage(estimatedwithpseudotimekernel,seeA).Panelson
therightshowUMAPprojectionsofisolatedneutrophiltrajectorycolor-codedbyindicatedparametersorgeneexpression.
(C)Pseudodynamicsfittednetproliferationparameter(red)anddifferentiationrateparameters(blue)alongpseudotimeformegakaryocytetrajectory.Vertical
linesindicatetheregionofinterestwithincreasingproliferation.
(D)Heatmapofgenesdifferentiallyexpressedaroundtheregionofinterestshownin(C).Leftcolumnsindicategenesbelongingtoenrichedcategories:E2Ftarget
(FDR<10(cid:1)38),G2-Mcheckpoint(FDR<10(cid:1)24),andcellcycle(FDR<10(cid:1)38).
(E)Pseudodynamicsfittednetproliferation(red)anddifferentiationrate(blue)parametersalongpseudotimeforneutrophiltrajectory.Verticallinesindicatethe
regionofinterestwithincreasingdifferentiation.
(F)FittedgeneexpressionvaluesalongpseudotimeforneutrophilmarkersandtwoTFgroupsshownin(fullanalysisinFigureE10).Gray,dashedlineindicated
differentiationratesshownin(E).Geneexpressionwasscaledaroundthemean.
252 CellStemCell31,244–259,February1,2024
ll
Resource OPENACCESS
dynamicallyexpressedgeneswithdistinctpatternsalongpseu- in Figures 4F and S6H, average journey time widely varies be-
dotime(Figures5Cand5D,similaranalysisofthedifferentiation tween terminals states of different lineages (Table S3). For
phase is showed in Figures E9C and E9D). These genes are instance, accumulating a cell in Meg progenitors (cluster 7) re-
strongly enriched for cell growth and proliferation genes with quires27days,neutrophilprogenitors(cluster10)orlateerythroid
almostallofthemshowinganupwardtrendintherelevantpseu- progenitors (cluster 11) >80 days and finally producing pDCs
dotimerange.Thisservesasaproofofprinciple,asthemodel takesabout150days. Second,wepredictwhatwouldhappen
based solely on total cell numbers, predicts the growth stage if,undernormalconditions,theself-renewingcluster0wasabla-
matchingtherespectivegenesignature. ted. As expected, without cluster 0 input, downstream cluster
While following the neutrophil differentiation kinetics sizeswouldgraduallydeclineovertime(Figure4G),duetolimited
(Figures5Band5E),wefoundgraduallyincreasingdifferentia- self-renewalofintermediateprogenitors.Aswedescribedabove,
tionratesaccompaniedbyacomplexpatternofgeneexpres- progenitorself-renewalislineagespecific,hencecorresponding
sion. Indeed, we observed two phases of neutrophil-affiliated clusterswaneatdifferentrates,withmegakaryocyteprogenitors
gene expression (Figure 5F), with Cebpe, Cst7, Elane, Fcgr3, depletedto50%after2–3days,whereaslymphoidprogenitors
andGfi1appearingalmostsimultaneouslyattheonsetofdiffer- are maintained for >50 days. Of note, the substantial effect of
entiation, while Clec4a2, Wfdc21, and S100a8 increasing at the depletion insomecompartmentsisdue tothe factthatwe
different intervals later. To gain insight into potential mecha- aresimulatingablationofallcellsincluster0,whichincludespro-
nismsregulatingtheprocess,wescrutinizedtranscriptionfac- genitorsimmediatelydownstreamofHSCs.Forcomparison,we
torswithdynamicexpressionalongthetrajectory(FigureE10A) alsosimulatedtheeffectofthedepletionofjustcluster0aandas-
and classified them into 4 groups based on expression pat- certainedthattheeffectonthedownstreampopulationsisbarely
terns. Group 2 (Figure 5F) largely mirrored the expression of noticeable(FigureE7B).
early neutrophil markers described above and reassuringly Predictionsrevealedbyourmodelagreewiththeorderofline-
containedGfi1,akeydeterminantoftheneutrophilfate,which age emergence inferred from transplantation12,30,41–43 or cell
indeedsuppressesIrf8expression,34amemberofthedownre- culture12,41 experiments. The time frame of the process is
gulatedgroup1TFs.Group3(FigureE10B)containedfactors expectedlymuchlongerbutiscompatiblewithpreviousstudies
with the highest expression in the most immature HSPCs ofHSPCdynamicsinvivo.3Ourapproachisthereforeanchored
(e.g.,Gata2,Hlf,andMeis1)andshowedearlyandnearlysyn- firmlyinthelongtraditionofhematopoiesisresearchandopens
chronousdecayinexpression,suggestinginvolvementinself- the opportunity to serve as a predictive framework for in vivo
renewal.Finally,Group1(Figure5F)TFsexhibituniquepatterns experiments.
of expression with peaks at different stages, all of which ulti-
mately decaying as late neutrophil markers appear. These Integrativemodelispredictiveandresolvestheeffects
contain multiple TFs associated with specific lineages such oftransplantationonHSPCdynamics
as:Irf8(Monocyte/DCfate34),Aff3(lymphoid/Bcells35),Dach1 To demonstrate the predictive capabilities of our models, we
(myeloid36), Hmga2 (myeloid, erythroid, megakaryocytic,37 utilized data from an independent study (Upadhaya et al.44). In
Pou2f2 (lymphoid/B cells38) or are important for HSPC self- thissetting,HSCsandtheirdescendantswerelabeledusingthe
renewal, including Ikzf239 or Ssbp2.40 Thus, our analysis indi- Pdzk1ip1-CreER;tdTomato system (analogous to Hoxb5-Tom
catesthatprogenitorsexhibittransientexpressionofmajorline- but using a different HSC-specific driver) and analyzed after 3,
agedeterminantsatspecificdifferentiationstagesontheirway 7,and14days.Upadhayaetal.44profiledcellsbyscRNA-seq;
tobecomingneutrophils(seeGfi1,Flt3,Irf8inFiguresE10Dand thus, wewereabletointegrate themintoourHSPClandscape
E10E). Early accumulation of these factors is correlated with (TableS6).Asthelimitednumberofcellsandreplicateswasinsuf-
increaseddifferentiationrate,buteventually,asingleprogram ficienttobuildastandalonemodel,weusedtheHoxb5modelpa-
takes over and accelerates the differentiation even further. rameterstopredictexpectedcellnumbersusingtheday3time
Thus, the continuous model unlocks access to full single-cell pointasinitialconditionandcomparedourpredictionswiththe
transcriptome data and thus enables integrated analysis of observed data. As shown in Figures S7A and E12, both the
cellularandmoleculardynamics,revealingmechanisticinsights discrete model and continuous models faithfully predict the
intocellbehaviorduringdifferentiation. evolutionofthe systemovertimeformostofthe large clusters
andtrajectories.Curiously,ourmodelindicatesfasterdifferentia-
HSPCmodelssimulatecelljourneysinreal-time tiontowardmegakaryocytes(seeclusters7and8)attheexpense
consistentwithbasicpropertiesofhematopoiesis oferythroid(clusters9and1).WenotedthatUpadhayaetal.44
Mathematical models combined with our new datasets offer used a milder tamoxifen treatment than our study, hence con-
uniquepredictioncapabilitiesallowingustounravelfundamental sultedtheHoxb5bi-phasicmodel(FigureS6E)forpotentialexpla-
facetsofhematopoiesis.Specifically,wefocusedoncomputing nation.Reassuringly,thebi-phasicparametersshowthatshortly
celljourneysinrealtimeandconsequencesofclusterablation. afterourtamoxifentreatmentmegakaryocyticdifferentiationoc-
First, weestimate the ’average journey times’ with the discrete curs faster while erythroid slower, thus suggesting that the
model. We placed a single cell in cluster 0 and computed the discrepancy is associated with the difference in tamoxifen
averagetimerequiredtoaccumulateonecellforeachtargetclus- dosage. Thus, our model, with some uncertainty, is able to
ter.The requiredtimedependsonthe specific influx/efflux and quantitatively predict dynamics of adult in vivo hematopoiesis.
proliferationrates,includingthe lossofcellsoutofthe terminal Furthermore, our approach paves the way for future studies,
populations (via differentiation/death). Highly transient popula- which,avoidingthetransienttamoxifeneffect,willprovideeven
tionscanthereforetakelongertobepopulatedstably.Asshown moreaccuratemodels.
CellStemCell31,244–259,February1,2024 253
A B CC
Dong et al., NCB, 2020 experiment
ESLAM LSK
(GFP+)
Day 1 Day 3 Day 5 Day 7
GFP+ cells
9.5 Gy
scRNA-Seq
Source Day 1
D E FF
Day 3 Day 5 Day 7
G 8 Ery/Meg progenitor 10 Neu progenitor 11 Late ery progenitor
3
2
1
0
3 4 5 6 7 8
Time (days) Time (days) Time (days)
HSC Ery/Meg HSC Neu HSC Ery
Dong et al. 2020 data HSPC dynamics model (this work) 95% conf.interval
Wenextemployedthesameapproachtopredictmulti-lineage megakaryocyte and erythrocyte differentiation is accelerated
differentiationtrajectoriesinvitro(FiguresE13)usingpreviously upontransplantation(Figure6G,cluster8),lateerythroidprogen-
publisheddata.12Wefoundthatalmostallclustersandtrajec- itorcellemergenceisdelayed,comparedwiththesteady-state
toriesaccumulatedifferentiating cellsmuchfasterinvitrothan counterparts (Figure 6G, cluster 11). To go beyond qualitative
in vivo, though interestingly megakaryocytic differentiation oc- interpretation, we performed combinatorial model re-fit of the
cursatroughlythesamespeedasinvivo. transplantation data to pinpoint the changes in differentiation
We analyzed a previous study (Dong et al.45), which used ratesandproliferationratesineachcluster/transitionmostlikely
scRNA-seqtotracktheprogenyofhighlypurifiedHSCsintrans- toberesponsibleforalteredtransplantationlandscapedynamics
plantedanimalsovertime(Figure6A).AfterintegratingthescRNA- (FigureE14A).Thisprocedurehighlightedstageandlineage-spe-
seq profiles into our reference landscape (Figures 6B–6F), we cific effects. For instance, the erythroid lineage differentiates
derivedcellfrequenciesperclusteratday3andusedthediscrete around10timesfasterbetweenclusters1and9,whereasmyeloid
modeltopredictthecellabundanceexpectedundernon-trans- progenitor cluster 2 exhibits 2-fold higher net proliferation and
plantationconditions(Figures6GandS7B).Althoughsomegen- 7-fold faster differentiation toward neutrophil progenitors and
eralfeaturesmatchnormalhematopoiesis,forinstance,megakar- 3-fold higher toward monocyte/DC progenitor (Figure E14B). In
yocyteprogenitors being the firstemerginglineage,cells under conclusion, we demonstrated that our model can be easily
transplantationconditionsdifferentiatemuchfasterinmostdirec- applied to other datasets and provide quantitative predictions
tions, particularly toward the neutrophil fate (Figure 6G, cluster andinterpretation,whichwouldnotbeavailablefromstaticmea-
10). The erythroid lineage behaves differently, whereas early surementsalone.
ezis
retsulc
.leR
ll
OPENACCESS Resource
WT
6 0.015
4 0.01
2 0.005
0 0
3 4 5 6 7 8 3 4 5 6 7 8
Figure6. GrowthanddifferentiationratesofHSPCsadapttocellularstressconditions
(A)DiagramoftheexperimentperformedbyDongetal.,45withHSCtransplantedintoanirradiatedanimalandfollowedovertimewithscRNA-seq.
(B–F)UMAPprojectionsoftheHSPClandscape(gray)withembeddedcellsfromDongetal.45inblue.
(G)Relativeclustersize,pointsindicateobserveddatafromDongetal.45Redlineindicatesourdiscretemodelprediction(shadedarea:95%confidenceinterval)
startingfromtheday3timepoint.ErrorbarsindicatepropagatedSEM.
254 CellStemCell31,244–259,February1,2024
ll
Resource OPENACCESS
AA Figure 7. The quantitative model of HSPC
dynamicsinthemouseBM
Diagram highlighting the transferable information
andthemodelutility.
+Time
accelerated differentiation.3 In vitro as-
says,performedundercytokine-richcon-
ditionsalsodriverapiddifferentiation,and
ssccRRNNAA-SSeeqq llaannddssccaapppe Discrete & continuous again CMPs also rarely show combined
analysis population models megakaryocyte, erythroid, granulocyte,
andmonocyteoutput.12,47However,ifthe
Molecular states Differentiation rates differentiation is slowed down and cells
Transferable
Putative trajectories Self-renewal/growth rates given the opportunity to expand (for ap-
information
Pseudotime Real-time
prox.3divisions)undercytokine-restricted
conditions (SCF, IL-11, TPO only), >50%
Quantitative model of normal state
CMP clones generate multipotent output
afterswitchingtoacytokine-richsecond-
aryculture.47Similarly,LMPPshavebeen
Prediction/interpretation Insights into stem/ Molecular mechanisms
of perturbation effects progenitor dynamics underlying cell dynamics described as largely unipotent cells in
transplantationassays48butcanproduce
multipotent output in two-phase cultures
analogous to the CMPs,49 i.e., given the
DISCUSSION opportunitytogrowfirstunderslowerdifferentiationconditions.
Our model, suggests that intermediate clusters 8, 4, 5, which
Quantitative models describing cell differentiation (e.g., Wad- largely overlapwith CMPs, areable to slowly transition among
dingtonlandscape)wereconceptualizeddecadesago.46How- eachother.Inparticular,cellscanshiftfrom8to4betweenthe
ever, the generation of dynamic and quantitative abstractions transient megakaryocyte/erythroid-biased cluster 8 and the
ofnativehematopoiesishasbeenhamperedbyalackofsuitable long-lived myeloid-biased cluster 4, but potential bidirectional
experimentalapproaches,particularlyreachingsingle-cellreso- transitions are also permitted by our model. This prediction is
lution.Here,wereportamajoreffort,combiningpersistentHSC consistent with cell fates estimated from the static data (using
labeling, time-series scRNA-seq analyses, and mathematical cellrank),whereonlyasmallsubsetofcellsisassignedtoasingle
modelingtobuildapredictivemodelofinvivohematopoiesisdy- lineage(e.g.,(cid:3)5%toneutrophilfate,FigureE14C),thussuggest-
namics.Analogouslytothemovingimagesinakinetoscope,our ingthatatleastasubsetofCMPcellsarebalancedandproduce
approachemploysmultiplehigh-resolutionsnapshotsofdiffer- multi-linageoutput.Thisisalsoconsistentwiththeinvivoobser-
entiationtoreconstructthereal-timecellularflowbetweensin- vation of progenitors with combined myeloid and megakaryo-
gle-cell states within the BM multilineage hematopoiesis. Our cytic/erythroid outputs.14,21,50 Importantly, we find that transi-
modeldescribescellbehaviorwithself-renewalanddifferentia- tions between clusters 4 and 8 are slow. Under strong
tionrates,whichintuitivelycanberepresentedastheshapeofa differentiationconditions(e.g.,transplantationordifferentiation-
Waddington-like landscape (Figure 7). Using this analogy, the promotingmedia),progenitorcellsthereforesimplydonothave
discretemodelisasetoffixedplatformsconnectedwithslides, time to ‘explore’ the multipotent states, thus emphasizing the
whereas the continuous model follows the curvature for all obvious,butattimeunderappreciatednotion,thatifamolecularly
observedstates(here:singlecells).Differentiationrateindicates multipotent progenitor cell does not divide before being chan-
the slope between two states, with steeper slopes indicating neled down a particular lineage, alternative fates can never be
fastertransition.Inturn,stablestates,theflatareas,havelittle realized(asillustratedinFigureE14D).
ornodownwardslopeandcombinedwithproliferation,consti- AlthoughtamoxifenhasbroadlybeenusedtoactivateCREin
tuteareasofhighself-renewal(Figure2B). multiple studies,3,19,51,52 we found that hematopoiesis upon
Differentiationrateandcellfatearenaturallyconnected,but, tamoxifentreatmentperturbsthesteadystateintheshortterm
crucially, exist in specific experimental contexts. CMPs have (i.e.,firsttwoweeks).Indeed,weobservedchangesinclustersizes
beenoriginallyproposedasamultipotentpopulationwithcom- and differentiation rates associated with tamoxifen treatment,
binederythroid,megakaryocytic,neutrophilic,andmonocyticpo- which we teased apart using a bi-phasic model (Figures S6B–
tential.47 However, later studies reported that most CMPs are S6E). Development of tamoxifen-independent models will help
transcriptionallyandepigeneticallyprimedtowardspecificline- avoid suchconfounding effects.Inthe long-term,asmice age,
ages,4exhibitlineagebias,andareprimarilyunipotent5intrans- weobservedonlymodestdifferences ofmostcluster sizes but
plantation cell fate assays. Importantly, transplantation, as we observedstrikingdifferencesincluster0composition.Although
showinthiswork,isassociatedwithgreatlyincreaseddifferenti- furtherworkwillberequiredtobetterresolvetheHSCsubpopula-
ation rates, most likely due to high cellular demand, as other tions(incluster0)andtheirage-relateddynamics,weconsiderthe
means of ablating cells, similar to 5-FU treatment, also cause tentativesub-structureprovidedhereasacriticalfirststepinthis
CellStemCell31,244–259,February1,2024 255
ll
OPENACCESS Resource
endeavor,asitfitsbothourdataandexperimentalevidenceof Unshackling the field from the static transplantation-defined
HSCbehaviorinagingmice.3,19,27,30 viewofhematopoiesisshiftstheparadigmfromqualitativemodels
We fully leverage the scRNA-seq approach to extend our withlimitedpredictivecapabilitiestointegrative,quantitative,and
model’s applicability. To ensure broad accessibility and inter- predictivemodels.Thelatterarehighlytransferableandthuskeyto
pretability, we integrated published annotation from multiple providinginsightintohumanhematopoiesis,whereexperimental
sources.7,12,20 This places our unified landscape (and its sub- options are limited. As recently demonstrated scRNA-seq can
populations)inthebiologicalcontextofpreviousimmunopheno- beintegratedacrossspecies,53–55thuspotentiallyenablemap-
typing and lineage tracing experiments. Moreover, static cell ping HSPC dynamics onto human counterparts. Self-renewal
properties (cluster, pseudotime) and model parameters (differ- anddifferentiationcapacitiesareparticularlyrelevanttoleukemia
entiation rates, self-renewal) are transferable. Crucially, new researchbecausetheyaretheprecisecellularbehaviorswhose
scRNA-seqdatacanbereadilyincorporatedintoourlandscape dysregulation causes the malignant phenotype. As we show
andourmodeliscapableofpredictingdifferentiationoutcomes hereandsupportedbypreviousstudies,3,22progenitorscanalso
for chosen time points given initial conditions, as we demon- operateclosetoself-renewalandasmallproliferativeadvantage
strated using an independent time course data.44 Finally, our maybesufficienttoimmortalizethem.Finally,populationdynamic
modelcanbeusedtosimulateputativeexplanationsforchanges modelsareuniversallyapplicableacrossbiologicalfields,asadult
in cell abundance, e.g., between healthy and disease tissues, tissues are commonly replenished from their own stem cell
even if only few snapshot measurements are available. We pools.56Toinspiresuchfutureendeavors,weshowcasehowto
showcasedthiscapabilitybysheddinglightonchangescelldy- build a model connecting high-resolution molecular information
namicsafterHSCtransplantation,whichdisplaysstageandline- withtissue-scalecellbehavior.
age-specific acceleration of differentiation in the erythroid and
neutrophilic/monocytic-DC lineages (see transitions 1–9 and Limitationsofthestudy
2-3/2-6respectively). Despite vastly improved resolution over immunophenotyping,
Differentiationandgrowthinvolvecoordinatedup-anddown- scRNA-seq does not capture cellular states in full. Additional
regulationofthousandsofgenes,whereitremainsunknownfor variables such as chromatin state, protein levels, metabolism,
thevastmajorityofthosegeneswhetherand,ifso,howtheyplay and environmental factors also affect cell behavior and may
aroleincontrollingcellbehavior.Toaccesstherelevantmolec- manifest in unappreciated heterogeneity and dynamic proper-
ular states with high precision, we introduce the continuous ties.Thesecharacteristicsmaybeheritableinwhichcasethey
model of near-native hematopoiesis, which includes per-cell may be tractable with lineage tracing approaches. In addition,
growthanddifferentiationrates,thusprovidingadirectcompar- the discrete model relies on hard clustering, which averages
isonbetweencellularbehaviorandunderlyinggeneexpression. anyfinercellheterogeneity.Althoughmostoftheearlycellfate
We observed complex, sequential gene expression patterns, decisions will occur within the landscape presented in this
some of which overlap with increasing differentiation rates, work, with increased throughput a BM-wide landscape could
implying irreversible molecular changes. For example, we be generated, thus providing better insight into the entire
show that neutrophil differentiation is coupled with expression lymphoid and myeloid differentiation trajectories. More work
ofmultiplelineagedeterminants(Irf8,Flt3,Pou2f2,andGfi1)fol- will also be required to better understand hematopoiesis dy-
lowedbyasingleprogramtakingoverandafurtherincreasein namics in a wide-range of non-homeostatic settings such as
differentiation. inflammationorchemotherapy.
Thecurrentandpredominantviewofhematopoiesishasbeen
constructedthroughtheidentificationofprogenitorpopulations STAR+METHODS
byFACSanddefinitionoftheirpotentialbytransplantation.1This
approach not only lacks resolution, but more importantly, re-
Detailedmethodsareprovidedintheonlineversionofthispaper
searchersendupdescribinghomeostatichematopoiesiswithin
andincludethefollowing:
a framework derived from assays that measure potential in a
non-homeostatic context3; transplantation defines potential in d KEYRESOURCESTABLE
a non-homeostatic assay and therefore does not reveal the d RESOURCEAVAILABILITY
actualcontributionofanygivenpopulationtosteady-statehe- B Leadcontact
matopoiesis. The revolution of single-cell transcriptomics has B Materialsavailability
provided evidence for additional progenitor populations,4,6,7,21 B Dataandcodeavailability
butsofarhadbeenseverelylimitedbyhavingtoplacethosepu- d EXPERIMENTAL MODEL AND STUDY PARTICIPANT
tativepopulationsonastatictransplantation-definedmapofhe- DETAILS
matopoiesis. Here we have overcome these shortcomings by B Animals
observingnear-nativehematopoiesisinsituandovertime. d METHODDETAILS
Thecombinationoflineagetracingwithasinglecelltranscrip- B Hoxb5CreERT2andHoxb5mKO2mouselines
tomicschasedeliveredatrulyquantitativeanddynamicmodelof B Transplantationassaysandhematopoieticreconstitu-
hematopoiesisincludingpreviouslyunknowndynamicrelation- tionanalysis
ships between precisely defined stem and progenitor cells. B Inductionofreportergeneexpressionbytamoxifen
Themodelalsorevealsfundamentalquantitativesystemproper- B Flowcytometry
tiesfromcelltrajectories,celldivisionrates,andnumberofcell B CellisolationforthescRNA-Seqexperiments
divisionstoindividuallineage-specificdifferentiationrates. B scRNA-seqdatageneration
256 CellStemCell31,244–259,February1,2024
ll
Resource OPENACCESS
B 10Xgenomics DECLARATIONOFINTERESTS
B scRNA-Seqdataanalysis
N.B.isnowanemployeeofAstraZeneca.I.K.isnowanemployeeofXap
B mKO2cellanalysis
Therapeutics.
B Subclusteringofcluster0
B EmbeddingexternaldatasetsintotheintegratedHSPC Received:September7,2023
landscape Revised:September25,2023
B Trajectoryinferenceandselection Accepted:December4,2023
B Differentialexpressionanalysis Published:January5,2024
d QUANTIFICATIONANDSTATISTICALANALYSIS
B Flowcytometrydataanalysis REFERENCES
B Discretepopulationmodelanalysis
1.Seita,J.,andWeissman,I.L.(2010).Hematopoieticstemcell:self-renewal
B Generalizedmodelfortestingalternativetopologies
versusdifferentiation.WileyInterdiscip.Rev.Syst.Biol.Med.2,640–653.
B Modelselectionforperturbedsystems
2.Reya,T.,Morrison,S.J.,Clarke,M.F.,andWeissman,I.L.(2001).Stem
B Continuouspopulationmodelanalysis
cells,cancer,andcancerstemcells.Nature414,105–111.
B Transplantationdataanalysis
3.Busch, K., Klapproth, K., Barile, M., Flossdorf, M., Holland-Letz, T.,
Schlenner, S.M., Reth, M., Ho¨fer, T., and Rodewald, H.R. (2015).
Fundamentalpropertiesofunperturbedhaematopoiesisfromstemcells
SUPPLEMENTALINFORMATION invivo.Nature518,542–546.
4.Paul,F.,Arkin,Y.,Giladi,A.,Jaitin,D.A.,Kenigsberg,E.,Keren-Shaul,H.,
Supplemental information can be found online at https://doi.org/10.1016/j.
Winter, D., Lara-Astiaso, D., Gury, M., Weiner, A., et al. (2015).
stem.2023.12.001.
Transcriptionalheterogeneityandlineagecommitmentinmyeloidprogen-
itors.Cell163,1663–1677.
ACKNOWLEDGMENTS 5.Perie´,L.,Duffy,K.R.,Kok,L.,deBoer,R.J.,andSchumacher,T.N.(2015).
The branching point in erythro-myeloid differentiation. Cell 163,
TheauthorsthankReinerSchulte,ChiaraCossetti,andGabrielaGrondys- 1655–1662.
KotarbafromtheCambridgeInstituteforMedicalResearchFlowCytometry 6.Klein,F.,Roux,J.,Cvijetic,G.,Rodrigues,P.F.,vonMuenchow,L.,Lubin,
Corefacilityfortheirassistancewithcellsorting.Wewouldalsoliketothank R.,Pelczar,P.,Yona,S.,Tsapogas,P.,andTussiwand,R.(2022).Dntt
KatarzynaKaniaandothersattheCancerResearchUKCambridgeInstitute expressionrevealsdevelopmentalhierarchyandlineagespecificationof
GenomicsCoreFacilityforgeneratingthe10xGenomicslibrariesandper- hematopoieticprogenitors.Nat.Immunol.23,505–517.
forminghigh-throughputsequencing.Theauthorsarealsogratefultoallstaff
7.Nestorowa,S.,Hamey,F.K.,PijuanSala,B.,Diamanti,E.,Shepherd,M.,
oftheBiologicalServicesUnitatQueenMaryUniversityofLondonfortheir
Laurenti,E.,Wilson,N.K.,Kent,D.G.,andGo¨ttgens,B.(2016).Asingle-
technical support. Work in the Kranc Laboratory is supported by Cancer
cellresolutionmapofmousehematopoieticstemandprogenitorcelldif-
ResearchUK(C29967/A14633andC29967/A26787)andBartsCharityand
ferentiation.Blood128,e20–e31.
BloodCancerUK.TheO’CarrolllaboratoryissupportedbytheWellcomeTrust
8.Velten,L.,Haas,S.F.,Raffel,S.,Blaszkiewicz,S.,Islam,S.,Hennig,B.P.,
InvestigatorAward(106144),theWellcomeCentreforCellBiology(203149),
andaWellcomemulti-userequipmentgrant(108504).WorkintheGo¨ttgens Hirche,C.,Lutz,C.,Buss,E.C.,Nowak,D.,etal.(2017).Humanhaemato-
poieticstemcelllineagecommitmentisacontinuousprocess.Nat.Cell
laboratory is supported by Wellcome (206328/Z/17/Z and 203151/Z/16/Z),
Biol.19,271–281.
BloodCancerUK(18002),CancerResearchUK(C1163/A21762),andUKRI
MedicalResearchCouncil(MC_PC_17230).Forthepurposeofopenaccess, 9.Dahlin,J.S.,Hamey,F.K.,Pijuan-Sala,B.,Shepherd,M.,Lau,W.W.Y.,
the author has applied a CC BY public copyright license to any Author Nestorowa,S.,Weinreb,C.,Wolock,S.,Hannah,R.,Diamanti,E.,etal.
AcceptedManuscriptversionarisingfromthissubmission. (2018).Asingle-cellhematopoieticlandscaperesolves8lineagetrajec-
toriesanddefectsinKitmutantmice.Blood131,e1–e11.
10.Tusi,B.K.,Wolock,S.L.,Weinreb,C.,Hwang,Y.,Hidalgo,D.,Zilionis,R.,
AUTHORCONTRIBUTIONS Waisman, A., Huh, J.R., Klein, A.M., and Socolovsky, M. (2018).
Populationsnapshotspredictearlyhaematopoieticanderythroidhierar-
Part1(Hoxb5-mKO2andHoxb5-Tommodel:conceptualization,generation,
chies.Nature555,54–60.
and characterization): Conceptualization, K.R.K. and D.O.; methodology,
J.C.,F.S.,N.B.,P.N.M.,K.R.K.,andD.O.;software,M.B.;validation,J.C., 11.Wang, S.W., Herriges, M.J., Hurley, K., Kotton, D.N., and Klein, A.M.
F.S., N.B., P.N.M., L.A.,H.L., K.R.K., and D.O.; formal analysis, I.K., J.C., (2022).CoSparidentifiesearlycellfatebiasesfromsingle-celltranscrip-
M.B., F.S., N.B., K.R.K., D.O., and B.G.; investigation, J.C., F.S., N.B., tomicandlineageinformation.Nat.Biotechnol.40,1066–1074.
P.N.M.,L.A.,andH.L.;resources,J.C.,F.S.,N.B.,P.N.M.,L.A.,H.L.,K.R.K., 12.Weinreb, C., Rodriguez-Fraticelli, A., Camargo, F.D., and Klein, A.M.
andD.O.;datacuration,J.C.,F.S.,N.B.,L.A.,H.L.,K.R.K.,andD.O.;writing– (2020).Lineagetracingontranscriptionallandscapeslinksstatetofate
originaldraft,I.K.,writing–review&editing,I.K.,J.C.,M.B.,K.R.K.,D.O.,and duringdifferentiation.Science367,eaaw3381.
B.G.;visualization,I.K.,J.C.,M.B.,F.S.,N.B.,K.R.K.,D.O.,andB.G.;supervi-
13.Yeo,G.H.T.,Saksena,S.D.,andGifford,D.K.(2021).Generativemodeling
sion,J.C.,H.L.,K.R.K.,D.O.,andB.G.;projectadministration,J.C.,F.S.,N.B.,
ofsingle-celltimeserieswithprescientenablespredictionofcelltrajec-
P.N.M.,L.A.,H.L.,K.R.K.,D.O.,andB.G.;fundingacquisition,K.R.K.andD.O.
torieswithinterventions.Nat.Commun.12,3222.
Part2(scRNA-seqanddynamicsmodelingconceptualization,datagenera-
tion,andanalysis):Conceptualization,I.K.,M.B.,andB.G.;methodology,I.K., 14.Pei,W.,Shang,F.,Wang,X.,Fanti,A.K.,Greco,A.,Busch,K.,Klapproth,
M.B.,andB.G.;software,I.K.andM.B.;validation,I.K.,M.B.,andB.G.;formal K.,Zhang,Q.,Quedenau,C.,Sauer,S.,etal.(2020).Resolvingfatesand
analysis, I.K., M.B.,and B.G.; investigation, I.K., J.C., N.B., M.L.R.H.,and single-cell transcriptomes of hematopoietic stem cell clones by
S.J.K;resources,I.K.,J.C.,M.B.,K.R.K.,D.O.,andB.G.;datacuration,I.K., PolyloxExpressbarcoding.CellStemCell27,383–395.e8.
M.B.,andB.G.;writing–originaldraft,I.K.andM.B.;writing–review&editing, 15.Montoro,D.T.,Haber,A.L.,Biton,M.,Vinarsky,V.,Lin,B.,Birket,S.E.,
I.K.,M.B.,K.R.K.,D.O.,andB.G.;visualization,I.K.,M.B.,andB.G.;supervi- Yuan,F.,Chen,S.,Leung,H.M.,Villoria,J.,etal.(2018).Arevisedairway
sion,I.K.andB.G.;projectadministration,I.K.,J.C.,M.B.,K.R.K.,andB.G.; epithelial hierarchy includes CFTR-expressing ionocytes. Nature 560,
fundingacquisition,K.R.K.andB.G. 319–324.
CellStemCell31,244–259,February1,2024 257
