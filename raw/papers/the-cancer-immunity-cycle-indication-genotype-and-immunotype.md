---
source_path: /mnt/c/Users/Administrator/Zotero/storage/WTIHV43F/Mellman 等 - 2023 - The cancer-immunity cycle Indication, genotype, and immunotype.pdf
ingested: 2026-04-23
sha256: 8c246085f28f58c9
---

ll
OPENACCESS
Review
The cancer-immunity cycle:
Indication, genotype, and immunotype
IraMellman,1,*DanielS.Chen,2,3ThomasPowles,4andShannonJ.Turley1
1Genentech,SouthSanFrancisco,CA,USA
2EngenuityLifeSciences,Burlingame,CA,USA
3SyntheticDesignLab,Burlingame,CA,USA
4BartsCancerInstitute,London,UK
*Correspondence:mellman.ira@gene.com
https://doi.org/10.1016/j.immuni.2023.09.011
SUMMARY
The cancer-immunity cycle provides a framework to understand the series of events that generate anti-
cancer immune responses. It emphasizes the iterative nature of the response where the killing of tumor
cells by T cells initiates subsequent rounds of antigen presentation and T cell stimulation, maintaining
active immunity and adapting it to tumor evolution. Any step of the cycle can become rate-limiting,
renderingtheimmunesystemunabletocontroltumorgrowth.Here,weupdatethecancer-immunitycycle
based on the remarkable progress of the past decade. Understanding the mechanism of checkpoint inhi-
bitionhasevolved,ashasourviewofdendriticcellsinsustaininganti-tumorimmunity.Weadditionallyac-
count for the role of the tumor microenvironment in facilitating, not just suppressing, the anti-cancer
response, and discuss the importance of considering a tumor’s immunological phenotype, the ‘‘immuno-
type’’. While these new insights add some complexity to the cycle, they also provide new targets for
research and therapeutic intervention.
INTRODUCTION L1-PD-1.1Resultsfromtrialswiththeseagentsfocusedattention
onthekeyroleofTcellsinanti-cancerimmunity,andinthecase
In only 15 years, the advent of cancer immunotherapy has ofthePD-L1-PD-1axis,thephenomenonofTcellexhaustion.2–4
revolutionized both the clinical practice of oncology and our Theintroductionofthecancer-immunitycycle(CIcycle)in2013
understanding of cancer biology. An increasing proportion of illustratedthatTcellsneitherrespondnorworkontheirown,but
cancer patients now receive immunotherapeutic agents as existinthecontextofaseriesofsteps,someofwhichareeven
standard-of-care in early and late disease. These patients extrinsictotheimmunesystemandthecancer(Figure1).5These
represent an increasingly broad range of cancer indications stepsarelinkedinacycle,implyingthat(1)anyindividualstep
andgenotypes,attestingtothelikelihoodthattheimmunesys- hasthepotentialtoberatelimitingforgeneratingoptimalimmu-
templaysafundamentalroleinvirtuallyalltypesandstagesof nity and (2) successful anti-cancer immunity has the potential
cancer. This generality, combined with the potential for long- to be self-reinforcing during the course of response. Even
term benefit and safety, has driven the field’s remarkable therapeutic strategies that create ‘‘synthetic immunity’’, such
growth,andpromisestodosoforyearstocome.Italsodistin- asadoptivecelltherapy,theuseofimmunecellengaginganti-
guishescancerimmunotherapyfromalmostallothertherapeu- bodies,orCAR-Tcelltherapy,mustworkwithinthecontextof
tic strategies, which usually rely on targeting tumor cells theCIcycle.
directly. Direct targeting creates selection pressures that typi- Overthepast10years,greaterattentionhasbeenpaidtothe
cally drive rapid resistance and tumor progression. Although mechanismsunderlyingeachoftheCIcycle’ssteps,withwork
patients can and do become resistant to immunotherapies, in some cases altering some long-held assumptions (e.g., the
by treating the immune system, the selection pressure on the significance of T cell exhaustion). Yet, basic understanding of
tumor is indirect. Moreover, the anti-cancer immune response thesestepsisonlynowbeginningtocatchupwiththeclinical
isinherentlyadaptive,presentingagreaterchallengetothetu- data that both invigorated the field and provided significant
mor and likely accounting for the extended overall survival mechanistic insights. The gap is also closing because the
benefit observed when immunotherapy is successful. Never- rate of progress in identifying effective therapeutic agents
theless, it is still the case that a majority of patients fail to beyondthePD-1axishasslowed.Thereisneverthelessexcep-
achieve durable responses, a limitation that represents our tionalpotentialforthediscoveryofnewtherapies,buttherate
greatest continuingtherapeutic challenge. ofdiscoverywillbeenhancedaswelearnmoreabouteachof
Althoughtheroleoftheimmunesystem incancerhasbeen thecycle’sstepsandhowtheyfittogether.Thisreviewaimsto
studied for decades, the current surge in interest was driven summarize our progress in understanding each step and to
byresultsobservedintheclinic,initiatedfrompatientstreated identify key unknowns, challenges, and opportunities for the
with antibodies to the immune ‘‘checkpoints’’ CTLA4 and PD- nextdecade.
2188 Immunity56,October10,2023ª2023TheAuthors.PublishedbyElsevierInc.
ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-nc-nd/4.0/).
ll
Review
OPENACCESS
Figure1. Thecancer-immunitycycle
Thesevenstepsofthecancer-immunitycycleasit
wasoriginallyconceivedandpublishedin2013.5
These fundamental steps continue to serve as
criticalbiologicstepsincancerimmunity.
cations; this is true for all types of solid
tumors,regardlessoforigin.Asaresult,
immunotypes continue to represent a
useful framework to understand the
mechanistic basis of response and lack
ofresponseandtodirectfutureinvestiga-
tion. Because most patient responses
occurwhenatumorexhibitstheinflamed
immunotype, uncovering the factors
that contribute to the formation of the
excluded or desert immunotypes will
facilitate targeted discovery efforts and
hopefullygreatlyexpandthepercentage
of responsive patients. As the mecha-
nisms responsible for these immuno-
types are critical to developing better
immunotherapies,itisanoversimplifica-
tion and indeed misleading to refer to
tumorsassimplybeinghot(presenceof
T cells) or cold (absence of T cells). For
example,immuneexcludedtumorshave
T cells, but the T cells are spatially
restricted from the tumor cells and are
therefore generally resistant to check-
pointblockade.
Itseemslikelythatthetumorstroma,or
more broadly the tumor microenviron-
THECICYCLEFRAMEWORKANDTHETUMOR ment (TME), plays a key role in determining immunotype and
ENVIRONMENT the immunetrajectory andfate of tumors.Not justTcells, but
cells of the innate immune system (e.g., monocytes, granulo-
ThebasicframeworkoftheCIcycleremainsunchangedsinceits cytes,naturalkiller[NK]cells)andnon-immunecells(e.g.,cancer
introduction,includingasubsequentmodificationtoemphasize associated fibroblasts or CAFs) are of exceptional impor-
thatblood-derivedTcellsmustoftentraverseastromalbarrier tance.10–13 These cell types collaborate to form collagen-rich
beforereachingthetumoritself.5Basedonrecentwork,howev- fibrotic stroma that restricts T cell immunity by suppressing
er,anumberofimportantnewconceptsrequirehighlighting. Tcellfunctionandphysicallyrestrainingtheirmigrationintotu-
Evenwithinindividualcancerindications,tumorscanstillbe mornests.14
viewed as assuming different immunological phenotypes, or Somewhat paradoxically, the TME can also promote anti-
‘‘immunotypes’’.Thethreeclassicalimmunotypes,immunein- cancer immunity, in part by generating peri-tumoral lymphoid
flamed, immune excluded, and immune desert, are defined, aggregates or tertiary lymphoid structures (TLSs), which are
respectively, as tumors containing abundant immune infiltrate, associated with better T cell responses and clinical out-
tumors where T cell infiltrate is limited to tumor stroma as comes.15ThecompositionandfrequencyofTLSsareemerging
opposed to the tumor parenchyma, and tumors that do not as key features that associate with response to immuno-
exhibitimmuneinfiltrate(Figure2).6–8Althoughtheimmunotypes therapy, perhaps reflecting their role in amplifying the anti-tu-
are likely an oversimplification of what may to be a dynamic mor T cell response in the TME. These points will be consid-
featureoftumors,whichmayalsobealteredduringtumorevo- ered furtherbelow.
lutionorbytherapeuticintervention,9theydorepresentauseful, Cancerandgermlinegeneticsarealsoimportantdeterminants
mechanism-basedclassificationsystem.Immunotypesoccurat ofimmunotherapyoutcomeandadverseevents;theyalsorepre-
different frequencies in different indications. For example, un- sentpotentialdriversofimmunotype.Tumorsgenerategenetic
treated prostate cancer, colon cancer, and melanoma most diversity thatrelates tocelltypeof originandtumor evolution.
often exhibit desert, excluded, and inflamed phenotypes, Itisnowappreciated,especiallyfromhumandata,thatthischar-
respectively.7Nevertheless,itiscriticaltorecognizethatallthree acteristicisintimatelyconnectedtothefunctionoftheCIcycle
immuntypesalsooccurindifferentpatientsinanyoftheseindi- andmustbeconsideredasadeterminingfactor.16
Immunity56,October10,2023 2189
ll
Review
OPENACCESS
Figure2. Immunotypes
Three primary immunotypes—immune desert
(blue), immune excluded (yellow), and inflamed
(red)—aredescribed.Inanimmunedesert,thereis
aclearpaucityofanyimmunecellswithintheTME.
This may relate to a repulsion or emigration of
immunecells(ormorepassively,throughalackof
attractive chemokines). In immune-excluded tu-
mors,thepresenceofinhibitorystromaandECM
may prevent effective migration of T cells into
direct contact with cancer cells, leaving them
excludedfromtheactualcancercellnests.Inin-
flamed tumors, the presence of stimulatory im-
munecells,includingperitumoralorintratumoral
TLS,mayprovideadditionalstimulationtotumor
infiltratinglymphocytes,increasingtheirfunctional
capacity,survivalandproliferation.
ECM, extracellular matrix; TLS, tertiary lymph
nodestructure.
target of checkpoint blockade. In addi-
tion, in the case of PD-1, perhaps the
most important source of PD-L1 may
notbethetumorcell,butrathertheanti-
gen-presenting DCs that stimulate tu-
mor-specific T cells in the first place.22
Thus, rather than acting to reverse
exhaustion, checkpoint blockade may
acttopreventthedevelopmentoftheex-
hausted phenotype and do so at a time
earlierintheTcellterminaldifferentiation
pathway. In addition, these findings
emphasize that DCs may play critical
roles not only in priming or activating
Tcellresponsesindraininglymphnodes
Perhapsthemostdramaticconceptualalterationinourunder- (dLNs) but also in support of T cell responses after arrival in
standingofthe cyclepertainstooneofitsmostelementalfea- thetumor.1
tures: the function of the T cellcompartment and its regulation Apartfromcheckpointinhibitors,ofwhichthreebiologictar-
bydendriticcells(DCs).Tcelldysfunctionintumorsisoftenasso- getshavebeenapprovedforclinicaluse(targetingCTLA4,PD-
ciatedwiththeaccumulationofexhaustedTcells(Texcells),cells L1/PD-1, Lag-3) or are in late-stage clinical trials (targeting
thatarealivebutexhibitreducedeffectoractivity.2Firstdefinedfor TIGIT),therehavenotbeenanytruetherapeuticbreakthroughs
Tcellsinchronicvirusinfectionandlaterextendedtotumors,Tex inthepastdecadethatactbymodifyingendogenouscancerim-
cellsarethoughttoaccumulatewhentheamountofantigenex- munity.Recentprogressincancervaccinesinthepre-metasta-
ceedstheabilityforittobeclearedbyantigen-specificTcells. ticsettingmayportendthenextsignificantadvance.23,24
Texcellsarecharacterizedbytheincreasedexpressionofvarious GiventhatDCsarenowseenasbeingkeynotonlyforinitiating
coinhibitoryreceptors,themostimportantofwhichisPD-1but T cell responses early in the CI cycle (both endogenous and
also includes LAG3, TIM3, and TIGIT; these receptors are also followingvaccination)butalsoformaintainingthem,theregula-
markersofTcellactivation.Giventheirincreasedexpressionin tion of DC activation or ‘‘maturation’’ is re-emerging as a key
theexhaustedstate,however,itwaswidelypresumedthatblock- elementindrivingtheCICycle.Tothispoint,typeIinterferons
ing the ability of coinhibitory receptors to bind their respective (IFNs)areprobablythemostimportantcomponents,asarethe
receptorswouldreverseexhaustion,reinvigoratinganti-tumorac- variousagentsthatinducetheIFNresponse(e.g.,STING,immu-
tivity.17ThiswasespeciallytrueforPD-1andTIGIT,whoseligands nogenic lipids, certain TLR ligands, cytosolic sensors such as
areoftenincreasedontumorcells.Withoutthisreversal,itwas MDA5andRIG-I,DNAdamageresponseelements).25–27
assumedthatTexcellswouldremainsuboptimallyactiveaseffec- Intheareaofsyntheticimmunity,CARTcellsaswellasCD3-
torsduetotheirlowcontentofcytolyticfactors(e.g.,granzymes) directedTcellengagers28haveemergedaseffectiveandwidely
andcytokines. approvedapproachestomodifytheCIcycleinhematologicma-
Overthepastfewyears,however,viewsregardingtheroleof lignanciesbybypassingtheneedtoproduceendogenousTcells
checkpoint blockadehaveevolvedconsiderably. Texcellsac- responses.29Theseapproachesmuststillnegotiatetheeffector
quire a heavily altered epigenetic state that cannot be easily sideoftheCIcycle,beingsubjecttomechanismsofimmuno-
reversed.18–21Therefore,theyarelikelytoreflectaterminaldif- suppressionandanapparentrequirement,atleastinthecase
ferentiationpaththatisunlikelytobetheonlyormostrelevant of adoptive cell therapy, for DCs to optimize activity.30 The
2190 Immunity56,October10,2023
ll
Review
OPENACCESS
Figure3. Thecancer-immunitycycleandthetumormicroenvironmentcancer-immunitysubcycle
Progressinthefieldofcancerimmunitysince2013hashighlightedtheimportanceTcellmigrationthroughtumorstroma,interactionwithintratumoralimmune
cells,persistence,andfunctionwithinthetumormicroenvironment.TcellswithintheTMEcanrespondinaseriesofstepsthatareamicrocosmofwhatoccurs
systemicallybeyondthetumor.ThesesubcyclestepsrepresentanimmunologiceddyintheTME,whichwerefertoasthecancer-immunitysubcycle.When
cancerimmunityisactive,stimulation,proliferation,andfunctionalkillingofcancercellsispossible.However,inhibitoryimmunecellsandstroma,metabolic
derangements,andlossofTcellfunctioncanoccurwithintheTME,haltingthecancer-immunitycycle.
APCs,antigen-presentingcells;CTLs,cytotoxicTlymphocytes;TLS,tertiarylymphnodestructure.
most impressive activity is currently limited to certain lym- atedlymphoidaggregates,ormorphologicallyidentifiableTLSs.
phomas,leukemiasandmyelomaalthoughtherearehintsthat TheTcellsmaythenexpandanddifferentiate(e.g.,effector,mem-
solidtumorsmayalsoeventuallyyieldtocellorengagerthera- ory,orexhaustion)leadingtodirecttumorcellkillingandperhaps
pies,particularlywhentargetedtocancercellsviatumor-spe- initiatingalocalTME‘‘eddy’’oftheCIcycle.Thisviewemphasizes
cificTcellreceptors.31–33Indeed,adoptivelytransferredTcells afarmoreimportantandcomplexrolefortheTMEinbothsupport-
(in mouse models) can lead to the generation of endogenous ingandsuppressingcancerimmunity(CIcyclesteps5,6,and7).
T cell responses to antigens not specific to the injected cells Conceivably,thisroleimpliesarangeofnewpotentialtherapeutic
(‘‘antigenspreading’’).34,35Thisobservationisconsistentwitha targets.Figure4highlightssomeofthemoleculesorinteractions
corepredictionoftheCIcycle:Tcellkillingleadingtothepersis- knowntoinfluenceTcellbehaviorsthroughouttheCIcycleand
tenceandprimingofneworexistingTcellresponses. subcycletoexemplifytherangeofpotentialsitesforintervention.
Inviewofthesemajoradvances,webelieveitisnecessaryto
modifytheinitialviewoftheCIcycletoincludeakeyroleforthe IMMUNOSUPPRESSIONBYCANCER-ASSOCIATED
TME,particularlyDCs,inregulatingandsustainingtheanti-tumor FIBROBLASTS
Tcellresponse.Asdepictedhere(Figure3),thisisbestillustrated
bya‘‘subcycle’’thatoccursatthetumorsiteuponentryofdLN- Probablythemostimportantconceptualadvanceistheapprecia-
derivedTcellsintothetumor(atstep5oftheCIcycle).Wepropose tionofthekeyrolelikelyplayedbythefibroblastcompartment,
thattheseTcellsencounterantigen-presentingcells(inparticular cancer-associatedfibroblastsor‘‘CAFs’’.CAFsdevelopfromfi-
DCs)interspersedwithinthetumorparenchyma,intumor-associ- broblasts upon exposure to activating signals from tumor cells
Immunity56,October10,2023 2191
ll
Review
OPENACCESS
Figure4. Thecancer-immunitycyclewithstimulatoryandinhibitoryfactors
Amultitudeofstimulatoryandinhibitoryfactorscaninfluencesuccessorfailureofeachstepofthecancer-immunitycycle.Here,weprovideselectedexamplesat
eachstep.Stimulatoryfactorsshowningreenpromoteimmunity,whereasinhibitorsshowninredhelprestraintheresponse.Factorsshowninblackmaybe
eitherstimulatoryorinhibitory.Theselistedfactorsdonotrepresentacomprehensivelist.
TAAs,tumor-associatedantigens;ERVs,endogenousretrovirusproteins;STING,stimulatorofinterferongenes;ATP,adenosinetriphosphate;TME,tumor
microenvironment;IFN,interferon;DAMPs,damage-associatedmolecularpattern;TLRs,toll-likereceptors;TNF,tumornecrosisfactor;CCL,CXCL,CCR,
CXCR,chemokineligandsandreceptors;TCR,Tcellreceptor;pMHC,MIC,MHCclassIpolypeptide-relatedsequenceprotein;PD-L1,programmeddeath-
ligand1;CTLA-4,cytotoxicT-lympocyteantigen-4;LFA,lymphocytefunction-associatedantigen;ICAM,intracellularadhesionmolecule;VLA,verylateantigen;
VCAM,vascularcelladhesionprotein;VEGF,vascularendothelialgrowthfactor;MMP,matrixmetallopeptidase;LAIR,Leukocyte-associatedimmunoglobulin-like
receptor;TGF,transforminggrowthfactor;CAF,cancer-associatedfibroblast;NET,neutrophilextracelllartraps;TLS,tertiarylymphoidstructure;APC,antigen-
presentingcell;Tregs,regulatoryTcell;MDSC,myeloid-derivedsuppressorcell;TREM,triggeringreceptorexpressedonmyeloidcells;VSIG4,v-setand
immunoglobulindomaincontaining;PGE,prostaglandinE;B2M,b microglobulin;LAG-3,lymphocyte-activationgene3protein;TIM-3,Tcellimmunoglobulin
2 2 2
domainandmucindomain-3;TIGIT,TcellimmunoreceptorwithIgandITIMdomains;HLA,humanleukocyteantigen.
2192 Immunity56,October10,2023
ll
Review
OPENACCESS
aswellasalterationsinoxygenandmetabolitegradientsandavail- their ability to effectively respond to checkpoint blockade
abilityandplayakeyroleinestablishingthematrixarchitectureof inhibitorsandinfiltrateintodirecttumorcontact.14,63,65Further-
the TME.13,36–38 CAFs exhibit remarkable functional pleiotropy, more, CAF-deposited matrix is associated with reduced lung
influencingvarioushallmarksofcancersuchastumorinitiation, tumor infiltration by T cells and DCs as well as alterations in
metabolism, progression and metastasis, anti-cancer immunity, TAMstates.66Preclinicalstudiessuggestthatlackoftherapeutic
angiogenesis,drugpenetration,andtherapeuticresponses.39–45 responsetoimmunecheckpointblockadeandchemotherapyis
Thesefunctionsaredueinparttotheirdecisiverolesinshaping drivenatleastinpartbytheeffectsofTGF-bsignaling.9,14,66–68
thecomplexmatrixmilieuandmechanicsofthetissueinwhichtu- FurthermechanisticworkisneededtounderstandhowTGF-b
morsgrowandmetastasize. and myCAFs modulate CD8 T cells in the peritumoral stromal
WhileCAFshavebeenstudiedfordecades,thefieldstilllacks niche.69,70Whilemanyquestionsremainunansweredregarding
aconsensusframework thatcapturescellsubsetsandstates, the immune-excluded immunotype, a few features are clear.
cell surface markers, lineage defining transcription factors, First, CD8 T cells are neither immobile in this niche nor ob-
developmentalorigins,localizationpatterns,andfunctions.Sin- structed by a wall of matrix.63 Second, excluded CD8 T cells
gle-cellomicstechnologies,particularlytheadventofsingle-cell can be rescued by interventions that disturb stromal architec-
RNAsequencing(scRNA-seq),hasrapidlyadvancedourunder- ture,enablingtheTcellstoinfiltratedirectlyintotumorcellcon-
standingofCAFs,providinggranularityonnewmarkers,subset tactanderadicatecancercells14;thus,theexcludedTcellsdo
identities, and tool generation for mechanistic studies. Three notrepresentadysfunctionalorterminalstate.TheCD8Tcell
majorclassesofCAFsareobservedacrossmosthumansolidtu- ‘‘problem’’inimmune-excludedtumorsrelatesmoretofeatures
mors: myofibroblastic CAFs (myCAFs), inflammatory CAFs oftheperitumoralmicroarchitecturethatfavortheirretentionin
(iCAFs), and antigen-presenting CAFs (apCAFs).13 MyCAFs thestromalcompartmentratherthanastrictlyintrinsicandirre-
compriseaprominentCAFsubtypeinmosthumansolidcancers versiblerewiringofCD8Tcellphysiology.
and produce large amounts of extracellular matrix (ECM) and
otherfibrosis-associatedmolecules,particularlyinlate-stagetu- IMMUNOSUPPRESSIONBYTHEMYELOID
mors.CAFpatterningofmatrixarchitectureaffectscancercell COMPARTMENT
invasiveness, immune cell infiltration, vascularization, organ
stiffnessanddrugpenetration.46–50MyCAFsarealsoimmuno- Myeloidcellsarethemostabundantcell typeinsolid cancers
modulatory,exhibitingpotentialtosuppressandcompartmen- beyondthecancercellsthemselves,withmacrophages,mono-
talize CD8 T cells and other immunocytes.51,52 Producing a cytesandimmaturemyeloidcells(alsoreferredtoasmyeloid-
breadthofcytokinesandchemokines,iCAFssecreteinterleukin derived suppressor cells or MDSC’s) comprising nearly half of
(IL)-6 and the chemokine ligands CCL2 and CXCL12 and may allcellsthetumormicroenvironment.71–73NeutrophilsandDCs
playanimmunosuppressiverole;thesecellsdominatetheCAF are also present in most human solid cancers but represent a
compartment in select metastatic settings.53–56 Antigen-pre- much smaller fraction (<10%) of the tumor myeloid compart-
sentingCAFsaresimilartoiCAFsinexpressingimmunomodula- ment.MyeloidcellsthriveintheTMEdueinparttoanabundance
tory factors but also express relatively high levels of major of growth factors, nutrients, cytokines, and chemokines
histocompatibility complex class II (MHC class II) molecules secreted by tumor cells (e.g., M-CSF/CSF-1, IL-6, GM-CSF,
andinducerecruitmentregulatoryT(Treg)cells.57,58 G-CSF,CCL2,CCL5).71Tumor-associatedmyeloidcellsasso-
MyCAFdevelopmentisdependentonfibroblast-intrinsicTGF- ciate with reduced patient survival and lack of response to
b signaling, mechanical force-driven activation, and increased anti-cancer therapies although associations with better out-
contractility, whereas IL-1 and TNFa are thought to induce comeshavealsobeenreported.74
iCAFs. Interestingly, iCAFs may arise from mesothelial cells Tumor-associated macrophages, or TAMs, are a mixture of
through a mesothelial-to-mesenchymal transition.58 Paradoxi- embryonically derived tissue-resident macrophages as well as
cally,thesameCAFsubsetsmayexhibittumorpromotingand macrophagesderivedfromcirculatingbonemarroworiginating
tumor-restrictingfunctionsindistinctsettings,emphasizingthe monocytes.75,76 Tumor-infiltrating myeloid cells as well as tis-
needforadditionalmechanisticresearchtosystematicallyeluci- sue-residentmonocytesandmacrophagesco-evolvewithcan-
datetheunderlyingfunctionalanddevelopmentalcomplexities cer cells, adopting distinct features in response to factors
ofthesecells.13,59–62 derivedfromcancercellsharboringdiversemutationsandun-
In clinical data, myCAF-specific gene signatures associate dergoing changes with tumor progression, metastasis and
withreducedpatientsurvivalandpoorresponsetochemo-,im- responsetotherapy.Inaddition,developingmyeloidprogenitors
mune- and tumor-targeted therapies. iCAFs and apCAFs are in a tumor-bearing subject are often exposed to tumor-cell-
moredifficulttostudyinthecontextofcancerpatientoutcome derivedfactorsthatactremotelyonmyeloidprogenitorsinthe
due to a lack of discrete markers and robust gene signatures. bone marrow long before their differentiated progeny reach
Nevertheless,CAFsgenerallyassociatewithbothpromotionof bloodandtumor.71,77
tumorprogressionandlackofresponsetocancertherapeutics Comprising a plethora of subsets and states, the TAM
althoughanti-tumorassociationshavealsobeenobserved. compartmentismoreheterogeneousthanmacrophagesofthe
A hallmark of immune excluded tumors is the densely surroundingnormaltissue.Single-cellatlasesofhumantumors
packed, highly aligned network of matrix fibers organized cir- demonstrate myeloid diversity with 5–10 macrophage subsets
cumferentially around tumors together with myCAFs and CD8 and2–4monocytesubsetsdependingonclusteringmethodol-
Tcells.63,64Withinthisstromalniche,CD8Tcellsmigratealong ogy.72,73 These subsets, largely identified based on transcrip-
collagen fibers and exhibit functional deficiencies that impede tionalprofiles,mayrepresentdevelopmentallydiscretesubsets,
Immunity56,October10,2023 2193
ll
Review
OPENACCESS
interconvertibleactivationstatesoramixofboth.Thelifecycle secretion,althoughwhether thisisa tumor-specific defectora
of myeloid cells, which can involve continuous migration from failure of NK cell infiltration is unclear.87 The release of prosta-
bloodintotissues,fromtissuesintolymph,orresidencywithin glandinE2,aregulatorofTcellsandotherimmunecells,associ-
diversetissueniches,requiresaphysiologicadaptabilityinorder ateswiththeactivationofthecyclooxygenasepathwayintumors
to thrive. Within tumors, monocytes, neutrophils, and macro- and resistance to immunotherapy.88,89 Similarly, tumors (espe-
phagesadapttohypoxic,acidic,andnutrient-poorgradients,re- ciallygliomas)thatharbormutationsinIDH1orIDH2overproduce
sultinginmetabolicallydistinctphenotypesfromthoseofmacro- 2-hydroxyglutarate,whichsuppressesTcellfunction.90
phages in more hospitable conditions of healthy non-tumor Other suppressive metabolites such as kyneurenine (due to
tissue.78–80 Furthermore, TAM subsets differ from one another overexpressedIndoleamine2,3-dioxygenase1(IDO)andtrypto-
intheirmetabolicprofilesandnutrientdependencies. phan2,3-dioxygenase(TDO)bytumorcells)andadenosine(pro-
TAMs play both pro-tumor and anti-tumor functions and ducedextracellularlyfromATPreleasedbydyingtumorcells)are
contribute to multiple hallmarks of cancer.71 Furthermore, alsoreleasedbytumors,buttheimpactofthesemetabolitesre-
TAMsexhibitingpro-tumorpropertiesappeartofaroutnumber quiresclinicalvalidation.Conceivably,thetumor(andTME)re-
thosewithanti-tumorfunction,andyettheprecisephenotypic leasesapanoplyofsuchmetabolitesorfacilitatesthedepletion
identity and functional contributions of TAM subtypes remain ofaminoacidssuchastryptophan thatareessential forTcell
incompletely understood. In general, anti-tumor functions of function. Together, these metabolic alterations would create
TAMsincludekillingandphagocytosisoftumorcells,MHCclass creating a distinctly immunosuppressive environment,91 sug-
IIantigenpresentation,andexpressionofproinflammatorycyto- gestingthattherapeutictargetinganyonecomponentmayprove
kines.Pro-tumorfunctionsofTAMsincludeexpressionoffactors ineffective.Indeed,inhibitorsofIDOoradenosinesignalinghave
thatpromoteangiogenesis,ECMremodeling,andsuppression notyetprovedsuccessfulintheclinic.Thereleaseofoxidized
ofanti-tumorimmunitybyinducingTregcells.81TAMsexpress lipids bymany tumors, especially after cell death, presents an
PD-L1andothermoleculesthatrestrainTcellresponsestotu- interesting paradigm with some of these being suppressive to
mors.82,83 TAM expression of MHC class II can also serve to T cells92 while others are strong activators of innate immunity
drivetoleranceratherthanimmunitydependingontheirexpres- and anti-tumor responses.4,93 Understanding these features
sion of costimulatory molecules and cytokines. TAMs also willbekeytounderstandingfactorsregulatingtheprogression
secrete factors that promote blood vessel growth and tumor oftheCIcycle.
cellmetastasis.Newgeneticandpharmacologictoolsthattarget TGF-b release by many tumors can also be expected to be
discretemyeloidsubsetswillmarkedlyadvanceourunderstand- immunosuppressive given that this cytokine promotes a T cell
ingofthislineageanditssignificanceintumorprogressionand exclusionarystromalreaction,14,67facilitatesTregcelldifferenti-
therapeuticresponse.Preclinicalstudiesinmousetumormodels ation,94 and restricts the expansion of T stem-like memory
have generated diverse TAM targeting approaches that over- cells.68,95 Several TGF-b antagonists have been evaluated in
cometheirpro-tumorandimmunosuppressivefunctions.71,78,84 theclinicwithoutobviousbenefit,perhapsreflectingtheatten-
Given the sheer size, developmental complexity, and func- dant toxicities associated with the sequestration of this
tionalimpactofthemacrophagecompartmentoncancercells, pleiotropiccytokinefamilyortheincompletereversalofinhibi-
theTME,andanti-tumorimmunity,itisreasonabletothinkthat toryfactorsthataretheresultofprolongedTGF-bsignaling.In
breakingtheefficacyceilingforcancertreatmentsmayrequire addition, it is unclear whether the three TGF-b cytokines have
strategies that target myeloid cells. A number of approaches interchangeable or even antagonistic functions in the tumor
havebeenevaluatedinclinicaltrials,suchastotalmacrophage context,makingitdifficulttoknowwhetherone,two,orallthree
depletion,withoutsuccesstodate.71,85However,additionalnew isoformsshouldbetargeted.
therapeutics that aim to selectively deplete pro-tumor TAMs, Activation of oncogenic pathways may also directly or indi-
directlyinhibittheirpro-tumorfunctionsorreprogramTAMsub- rectly oppose T cell immunity. For example, increased Ras/
typesawayfrompro-tumorstatesandtowardanti-tumorstates MAPK signaling reduces the expression of MHC class I gene
areindevelopment.Oneattractiveideaistoutilizepotentinnate products, which would reduce a tumor cell’s susceptibility to
activatorssuchastypeIIFNs,eitherbytargeteddeliveryorap- T cell attack.96,97 There are also rare instances where loss of
proaches that induce in situ formation in the tumor.27 Since typeIIIFNsignalingbytumorsconfersprotection,presumably
innateactivationiskeytofiringuptheCIcyclebothsystemically by limiting the cytotoxicity of IFN release by T cell effectors.98
and intratumorally (in the case of the subcycle), this strategy Finally, tumor cells may protect themselves from T cell killing
shouldgarnerconsiderableinterest. byrapidlyrepairingtheplasmamembraneporescreatedbyper-
forinuponTcellgranulerelease.99Othercellautonomousde-
IMMUNOSUPPRESSIONBYTHETUMOR fensemechanismslikelyawaittobediscovered.
Inadditiontothemyriadofsuppressionmechanismsattributable IMMUNOSTIMULATIONINTHETME:DCs
totheTME,tumorcellsthemselvesharbortheabilitytorestrict
T cell immunity. While several enticing mechanisms have been DCsremainindispensableintheCIcycleduetotheirunparal-
described,mainlyinpreclinicalmodels,fewhavebeenvalidated leled ability to prime and expand antigen-specific CD4 and
intheclinicorprovidednewtherapeutictargets.Forexample,in CD8 T cell responses.1,100 Over the past decade, there has
melanoma models, activation of b-catenin signaling associates beengreatprogressinthedefinitionandfunctionalcharacteriza-
with immune deserts and resistance to checkpoint inhibitors.86 tionofvariousDCsubsetsandpopulations.101–103Theconven-
ThiseffecthasbeenattributedtoapaucityofTcellchemokine tionalDC1(cDC1)populationcontinuestobethemostimportant
2194 Immunity56,October10,2023
ll
Review
OPENACCESS
initiatorofCD8Tcelltumorimmunity,reflectingatleastinpart tantroleincontrollingTcellresponses22,114andalsoservesasa
theirabilitytotrafficfromthetumorbedtodLNs,theirabilityto moreeffectivepredictorofresponseinhumancancerpatients
crosspresentinternalizedtumorantigensonMHCclassI,and thantotalPD-L1expression(includingtumorcellexpression).115
theircapacityforstimulatingnaiveCD8Tcells.Italsoremains Finally,theonsetofTcellexhaustionintumorsmaybecontrolled
possible that these or other migrating cells somehow ‘‘hand inthetumoritselfasaconsequenceofantigenpresentationby
off’’tumorantigenstodLNresidentDCs,representingasecond DCs.116Takentogether,theseconsiderationsstronglysuggest
option for antigen cross-presentation to T cells on both MHC thattheroleofDCsintheTMEisnotlimitedtothetransferofan-
classIandclassIImolecules.104,105Twoothergeneralclasses tigensfromtumortodLNsbutalsotoensuretheactivationand
ofDCsalsoexist,althoughtheirrolesareabitlesswelldefined. expansionofantigen-specificTcellsinthetumoritself.
As reviewed by Pittet and colleagues,106 cDC2’s are typically
associated with presentation on MHC class II molecules and TLSsINCANCER
stimulation of CD4 responses. cDC3’s, also known as CCR7
DCs or mRegDCs, are also found intratumorally as well as in TLSs are essentially proto-LNs containing germinal-center-like
dLN,canbemigratoryandmaymediateimmunostimulatoryor structuresthathavelongbeenappreciatedtooccurintumors,
regulatoryfunctionsdependingoncontext. ashasthepresenceofpoorlyorganizedlymphoidaggregates.
ThepositioningofDCsintumorsisclearlyaprimarydetermi- Onlyoverthepastfewyears,however,hastheirlikelyroleintu-
nantoftheanti-cancerimmuneresponse.Patientswhosetumors morimmunitybecomeclear.5Humanclinicalstudieshavedocu-
are‘‘immunedeserts’’arealmosttotallyunresponsivetoimmu- mentedthefactthatresponsetocheckpointtherapiesgenerally
notherapyandlackanyTcellinfiltrate,suggestingtheabsence associateswiththepresenceofTLSsintheTME.117–120Espe-
ofanongoingimmuneresponse.ThesetumorsalsolackDCs, cially given the accumulating evidence that DCs in the TME
whichmaybetheprimaryreasonforthelackofresponse.This may work in situ, the clinical data suggest that there is also a
possibility that has received some experimental support in functionalassociation.Byprovidinganorganized,LN-likestruc-
mousemodels.9,86IfafailureofDCinfiltrationistheculpritfor tureforTcellstimulation,TLSsmaybethesiteatwhichTcells
producingtheimmunedesertimmunotype,thenunderstanding areactivatedandexpandedbytumor-associatedDCs.
the reasons for this failure and possible mechanistic solutions ThisassociationhasalsoinvigoratedinterestintheroleofB
shouldrevealpotentialpathsfortherapeuticintervention. cellandanti-tumorantibodiesincancerimmunity,aswellasin
DCs maintain a balance between immunity and toler- understanding the role of the CD4 T cell response. Recent
ance,107,108 a dual responsibility that may be a double-edged work has implicated both possibilities, with CD4 T cells now
sword in the cancer context. DCs, regardless of subset, must seen as possibly having their own cytotoxic properties or as
receive an activating signal to initiate a terminal differentiation harboringtheabilitytoprovide‘‘help’’tothegenerationofanti-
processof‘‘maturation’’thatconvertsDCsfromantigenaccu- tumor CD8 responses.121 These considerations also provide
mulationmodetoantigenpresentationmode.100,109Whenthis aninterestingmechanisticbasisforunderstandingthefunction
isaproinflammatoryorinflammatorystimulus,thematureDCs of the coinhibitory receptor Lag-3, whose presumed ligand is
promoteimmunity,tunedtotheprecisenatureofthestimulus; theMHCclassIImolecule.122
whenitisnot,DCspromotetolerance.Togenerateaneffective TherelevanceofTLSshasenhancedtheconceptthattheTME
anti-cancer response, therefore, antigen-accumulating DCs can be immunostimulatory in addition to immunosuppressive
mustreceiveanappropriateactivatingsignal,oradjuvant.1,4If and that T cell stimulation by DCs is not limited to secondary
theTMEisinsufficientlyinflammatory,theDCswillbelesslikely lymphoidorgans(e.g.,dLN)buthasanessentialcomponentin
tomatureortoproduceanti-tumorTcells.Althoughtheidentity thetumoritself.ThisactivityislikelynotlimitedtotheTLSbut
ofthetoleragenicDCsremainsuncertain,maturationdoesoccur to DCs (and perhaps other antigen-presenting cells) found
at the steady state even in the absence of overt inflammatory distributed throughouttheTME andintratumorally. Thismodel
stimuli as phenotypically mature DCs (elevated MHC class II indicatesthatDCscanworktostimulateTcellsinsitu,inaddition
and CD86) can be found in dLNs and the spleen. These DCs totheirwell-establishedroleafterlymphaticmigrationtodLN.
maylackcertainfeatures(cytokineproduction,highcostimula-
toryreceptorligands)thatresultintolerance.Thediscoveryof THECICYCLEDIRECTST CELLDIFFERENTIATIONAND
a mature DC with immunoregulatory properties (mRegDCs, FUNCTIONATMULTIPLESTEPS
CCR7DCs)maybeofparticularinterestinthisregard.106,110
IthasbecomeincreasinglyclearthatDCs,especiallythoseinthe ThelikelihoodthatTcellscanbeprimedandfurtherstimulatedin
TME,provideanadditionalessentialfunctioninthetumor,namely bothdLNandtheTMEraisesimportantquestionsregardingthe
thestimulationandexpansionofantigen-committedmemoryor control of T cell differentiation and trajectory. The original
effectorTcells.Earlyevidencecamefromadoptivecelltransferex- assumptionthatTcellactivationandexpansionoccurredonly
periments in mice, where anti-tumor efficacy was substantially indLN(step3oftheCIcycle)suggestedthatallsubsequentfea-
diminished in animals whose DCs were conditionally ablated.30 tures of T cell function were determined at that site. Thus,
Similarly,aDC-directedmRNA‘‘vaccine’’encodingaCARTtarget whether a T cell was destined for the exhaustion, effector, or
(claudin-6)enhancesCARTfunction.111Insituapproachesreveal memorypathwayswouldbespecifiedbytheconditionsofanti-
a close association of intratumoral DCs with CD4 and/or CD8 gen presentation in dLN. As this simple assumption no longer
Tcells(orallthree)inbothhumansandmice.112,113 seemscorrect,itispossiblethatonlyprimingoractivationisiniti-
Intheimmunotherapycontext,italsoappearstobethecase atedindLN,whileterminaldifferentiationoccursatthetumorsite
thatPD-L1expressionbyDCsplaysadisproportionatelyimpor- (the ‘‘subcycle’’ at step 5). It is also possible that all of these
Immunity56,October10,2023 2195
ll
Review
OPENACCESS
activitiescanoccurinbothsites,withTLSperhapsfunctioning Understanding features to predict response or understanding
asasiteforTcellprimingintheTME,incertaincases. mechanisms of resistance continues to be a major focus of
ThepossibilitythatTcellstimulationbyDCsinthetumorplays investigationbothpre-clinicallyandintheclinic.Thesefactors
akeyroleinTcellfunctionhasreceivedsupportfromrecentex- maybeintrinsictothetumor,theTME,orareflectionofpatient
perimentsinmousemodels.116Itisalsoconsistentwithworkin genetics,microbiome,metabolism,orpharmacologicstatusbut
humancancershowingthatexpandedTcellclonotypesfoundin ineachcasemustreflectthesiteofaratelimitingstepintheCI
the blood are also found in the tumor bed, albeit distributed cycle.8 The expression of PD-L1 on tumor cells or on immune
among different T cell phenotypes.123 Unpublished work in cells(DCsinparticular)continuestobethemostusefulparam-
mouse has provided further support for this interpretation by eterforpatientselection,butitisonethatisincompletelypredic-
showing that dLN-derived CD8 T cells are polyclonal with tive perhaps because it may not necessarily be indicative of
respecttotheirTCRspecificities,butarecontainedwithinasin- a particular rate limiting step in the CI cycle. Mechanistically,
glecellstatethatdifferentiatesaftertumorarrival(K.Nutsch,K. PD-L1 expression is thought to denote patients harboring an
Banta, T. Wu, E. Chiang, and I.M., unpublished data). Further, ongoing anti-tumor response, with IFN-g released by effector
studiesofhumancancerhavedemonstratedthatTcells(CD4 T cells in the tumor bed causing increased expression of PD-
and CD8) can form clusters or ‘‘triads’’ together with DCs in L1bysurroundingcells,especiallyDCsthatarelikelyinvolved
thetumor.112,113Inallofthesestudies,Tcellscanbeshownto indirectingtheterminaldifferentiationofnewlyarrivedorlocally
achieve terminal differentiation (e.g., exhaustion) only after generated T cells. Even assuming that this idea is correct,
reachingthetumor. and PD-L1-positive patients do have a pre-existing immune
AlthoughadetailedconsiderationofTcelldifferentiationand response,itdoesnotnecessarilyfollowthatblockadeofcoinhi-
trajectory cannot be considered here, the development of Tex bitoryreceptorssuchasPD-1willovercometheCIcycle’srate-
cells is obviously relevant to the function of the CI cycle. The limitingstepinagivenpatient.
revisedviewwouldsuggestthatTcellsbecomecommittedto Alltumors,regardlessoforigin,exhibitabasicimmunotype:
the exhaustion pathway at the level of the tumor, and not at immuneinflamed,immuneexcluded,orimmunedesert.Itseems
the time of initial stimulation in dLN (K. Nutsch, K. Banta, T. likelythattheseclassificationswillproveusefulinidentifyingthe
Wu,E.Chiang,andI.M.,unpublisheddata).116,124Asdiscussed factors that limit or promote T cell responses to tumors.8 For
earlier, the fact that terminal Tex cells are characterized by a example, in immune excluded tumors, the proliferation of
largelyirreversibleepigeneticstateitselfstronglysuggeststhat immunosuppressive stromal investments around a tumor has
therapeutic checkpoint inhibition does not act to reverse but focusedattentionontheroleofperitumoralcollagen-richfibrotic
rathertopreventthedevelopmentoftheexhaustedphenotype matrix,theroleofCAFsandtheirregulationbyTGF-bsignaling:
withinthetumor.InthecaseofthecoinhibitoryreceptorsPD-1 blockadeofTGF-bsignalingcanalterstromalarchitectureand
andTIGIT,theirbiochemicalmechanismappearstoinvolvethe permit T cell entry in preclinical models.14 Excluded tumors
inhibition of costimulatory signaling via CD28 and CD226, canbescoredasPD-L1-positive,yettheyrespondpoorlydue
respectively.125 This in turn suggests that blockade of PD-1 totheirabilitytolimitTcellinfiltration.
(andTIGIT)maypreventexhaustionbypromotingcostimulation. Althoughindividualindicationsexpressallthreephenotypes,
DCsmayprovidethemostrelevantsourceofPD-L1aswellasof their ratio can vary in characteristic ways: colorectal cancers
theCD28ligandsB7.1andB7.2(CD80andCD86,respectively) generally exhibit up to 70%–75% immune excluded tumors
andresideinbothdLNandthetumor.Lag-3-mediatedcoinhibi- andonly10%immuneinflamed,whilenon-smallcelllungcancer
tionmayactinadistinctfashionbutistriggeredbybindingMHC (NSCLC) can exhibit 30%–35% inflamed and only 40%
classII,whichisalsoabundantlyexpressedbyDCs.(Figure4). excluded.7Further,immuneexclusionincolorectalcancermay
Recentevidencehassuggestedthatthesetwogeographically differ from immune exclusion in an inflamed tumor such as
separate populations of DCs can play distinct roles in T cell NSCLC,andthesmallpercentageofimmuneinflamedincolon
development and exhaustion. Although the identities and pre- cancer may reflect the MSIhi population. Indication-related
cisetrajectoriesoftheTcellpopulationsinvolvedremainpoorly immunologiccontextisrelevant.Althoughresponsetotherapy
characterized,oneattractivemodelmightbethattumor-specific maynotbepredictedmoreaccuratelybyrevealingatumor’sim-
T cells leave the dLN in a relatively multipotent state that un- mune phenotype, the point is that the mechanistic basis of
dergoesfinaldifferentiationinthetumor,includingtheformation responseorlackthereofmaybehidinginplainsight.Ifthebasis
oftissueresidentmemoryTcellsandcentralmemoryTcellsthat forthesephenotypescanbeunderstood,thepathtofuturepo-
maythenrecirculate.126Regardlessofthemodel,wepredictthat tentialtherapeutictargetsmaybecomeclearer.
TcellsaredirectedbyintratumoralDCstodifferentiatealongthe Whatdoesappearcertain,however,isthatthedifferentpheno-
effector, memory, or exhaustion pathways. Much additional types define immunologicallydistincttumorpopulationsthat, in
workwillberequiredtofullyunderstandtheissue,buttheearly turn,helpdetermineresponsetotherapybetterthanaconsider-
evidenceissufficientlycompellingtoincorporateasubcycleto ationofindicationortumorgeneticsaloneorcombined.There-
step 5 of the CI cycle that captures this second stage of DC- fore,intheageofimmunotherapy,itmakessensetotakethese
dependentTcelldifferentiationintheperiphery. immunologicalclassifiersintoaccountwhendescribingtumors.
Thetermimmunotypecapturesthisaspect,representingafeature
THEDETERMINATIVEROLEOFTUMORIMMUNOTYPE thatforprecisionguidingofimmunotherapiesmaybemorerele-
vantthan‘‘indication’’or‘‘genotype’’alone.Wepropose,there-
It remains the case that far fewer than half of patients have fore,thatimmunotypebeconsideredforinclusionasanewand
durable outcomes with immunotherapy, even in combination. informative classifier when characterizing a patient’s tumor, as
2196 Immunity56,October10,2023
ll
Review
OPENACCESS
eachimmunotypebydefinition mustreflectthe locationofrate adequately.ExistingTcellimmunitypriortostartingtherapyap-
limitingstepsontheCICycleforeachpatient’stumor. pearscrucialinpredictingresponseandwhiledynamicchanges
to the TME occur with ICI therapy, their relevance remains
HOST-RELATEDFACTORSINFLUENCETUMOR uncertain and will require further study both pre-clinically
IMMUNITY andinpatients.131RechallengewithPD-(L)1therapyafterrecent
progression on ICI therapy does not appear to be associated
HostandenvironmentalfactorsarelikelytoinfluencetheCIcy- with clinical benefit, suggesting that the loss of response re-
cle and response to immune therapy therapy.8 High vitiligo or flected the development of another rate limiting step in the CI
psoriasis polygenic risk scores, derived from germ-line SNPs, cycle.132
are associated with longer OS under anti-PD-L1 monotherapy TheonlyestablishedICIcombinationisPD-1andCLTA4inhi-
ascomparedtochemotherapy.Thisindicatesthehostresponse bition, although it has only shown efficacy in specific cancers
totumorogenesisisrelevantinpredictingoutcomes.Theseare and is associated with higher toxicity that cannot be tolerated
also likely to epigenetic factors, such as chromatin structure bymany patients. CLTA-4’smechanism of action remains un-
regulating expression of key immune related proteins. Finally certainandcanacteithertofacilitatetheprimingofnewTcell
the influence of the gut microbiome on the immune repertoire responsesorremoveTregs,whicharehighinCTLA4expression
iswell established, but working to understand where in the CI andwouldbeexpected tosuppressanti-cancerTcells.Thus,
Cycle the microbiome plays a role (positive or negative) will anti-CTLA4couldfunctionattwositesontheCIcycle(Figure5).
greatlyassistinunderstandingunderlyingmechanisms. TargetingdifferentpointsintheCIcyclewithcombinationisan
Concomitantmedicationsalsoplayaroleindeterminingthe establishedstrategy,althoughtheresultshavebeenmixed.The
outcomeofimmunotherapies.Apartfromthepredictedeffects secondgenerationofimmunetherapies,aloneorincombination,
of lympho-ablative chemotherapies, prior treatment with have not yet successfully built on the initial success of PD-L1/
antibioticsthatdepletethegutmicrobiotaalsohaveagenerally CTLA-4basedtherapy.Thereareafewexceptionstothis,one
negativeeffect.127Theantibioticeffectpresumablyatteststoa ofwhichisLAG-3,whichhasrecentlyattractedattentioninmela-
positiveinfluenceofthemicrobiomeonanti-cancerimmunere- noma with a progression-free survival advantage and FDA
sponses.Certainclassesofbenzodiazapenes,whichareoften approval.133LAG-3isexpressedonaspectrumofimmunecells
describedaspalliativestocancerpatients,associatewithpoor includingDCs.ItsmajorligandisMHCclassII,furtherimplicating
response to immunotherapy.128 This effect may reflect the Thelperimmunityincancerimmunityandthemodificationstothe
mobilization of the neurotransmitter GABA, which has intrinsic immunecyclesuggestedinthisarticle.TIGITisasecondareaof
immunsuppressiveproperties. interestattractingrenewedattention.134
Ontheotherhand,variousoncogene-targetedtherapies,such Other areas for optimism include personalized cancer vac-
asRas-MAPKinhibitorsandCdk4/6inhibitors,mayenhanceanti- cines (usually mRNA) with encouraging combination data in
cancerimmuneresponsesbyincreasingantigenpresentationby melanoma and pancreatic adenocarcinoma, the latter being a
tumorsorbyfacilitatingTcellfunction.96,129Understandingwhere cancer type that is generally refractory to ICI.24 Interestingly,
onthe CIcycle these various manipulationsworkshouldprove both ofthesepositive resultshavebeeninthe adjuvant(post-
mostusefulinunderstandingthebasisfortheseeffects. surgical) setting, suggesting that the vaccines alone cannot
generatesufficientTcellresponsestoexertclinicalbenefitunder
CLINICALAPPLICATIONOFTHECICYCLEANDITS conditionsofhightumorburdenorentrenchednon-permissive
MODIFICATIONS immunotypes that may be re-programmed at least transiently
followingsurgery.Otherlessspecificorpotentvaccineplatforms
Immunecheckpointinhibition(ICI),especiallywithPD-L1/PD-1 havestruggledinsolidtumorspreviously,duetotumorhetero-
therapy,hasachievedsuccessacrossabroadspectrumofcan- geneity, manufacturing challenges, and possible inhibition by
cer, with many patients benefitting from durable remissions. theTME.135CombinationsthataddresstheTME,potentiallyby
These agents have successfully moved from the advanced re-wiring the inhibitory myeloid compartment may potentially
settingintotheperioperativesetting,reducingrelapseratesafter addressthislimitation.136Understandingthenatureofthesteps
surgery and transforming outcomes in specific tumor types. oftheCIcyclethatlimitvaccineefficacyisimportanttomaximize
Theiractivityintheperioperativesettingisunderintenseinvesti- thechancesforthispotentiallycurativeapproach.
gationwithrandomizedtrials.Inmelanoma,itappearstheneo- Single-agentCAR-TcelltherapyorTcellengagershavehad
adjuvantapproachispreferabletoadjuvanttherapy.130Although excellent success in hematopoietic tumors, where the target is
the mechanistic basis for this effect has not been studied, relativelyclear:CD19orCD20inlymphomaandcertainleukemias
applyingthelogicoftheCIcyclemightpredictthatneo-antigen andBCMAinmyeloma.However,inmoreheterogeneoussolidtu-
loadatthetimeoftherapyallowscheckpointblockadetofacili- mors,wherethetargetsareoftenexpressedonhosttissuesand
tate T cell responses, with subsequent surgery reducing the the TME can be immunologically challenging, results are less
overall tumor burden thereby enabling the T cell numbers that impressive.CAR-Tcellsinsolidtumorsmayrequirenoveltarget-
wereinsufficienttoyieldadurableresponseintheneoadjuvant ing,moresophisticatedcellengineering,andcombination-based
setting to control the growth in the adjuvant setting. In this approaches.Successwilllikelybepredicateonattentiontothe
example,tumorburdenmaybeseenasbeingratelimitingprior relevant steps of the CI cycle. As mentioned above, preclinical
tosurgeryandTcellactivityratelimitingaftersurgery. datahaveshownthatprogrammingtheexpressionbyDCsofa
IssuesaroundtheoptimaldurationofICItherapyandimmune CAR-T target antigen (claudin-6) increases the efficacy of the
memory after cessation of therapy have not been addressed cognate cell therapy, presumably reflecting the role of DCs in
Immunity56,October10,2023 2197
ll
Review
OPENACCESS
Figure5. Approvedandselectedinvestigationaltherapiesthattargetthecancer-immunitycycle
Since2013,thousandsofclinicaltrialstestingcancerimmunotherapyagentshavebeenconducted.Thishasledtonumerousapprovalsofimmunotherapyand
immunotherapyregimensinmanydifferentcancerindications,highlightingthemostefficaciousimmunotherapeuticapproaches.Theseapprovedagentsand
severalselectothersthatareinclinicaltestingareshownatthestepofthecancer-immunitycyclewheretheirprimaryactionoccurs.
dLNandintratumorallyinsupportingTcellresponses(evenafter dressed the immune excluded phenotype. Moreover, TGF-b is
adoptivecelltherapy). highlypleiotropicwithitspaninhibitionbeingassociatedwithava-
Attemptingtotransformtumorsintoimmuneresponsivecan- rietyoftoxicitiesthathavelimitedthedose.Attemptsthusfarthat
cersbyalteringtheTMEwithnon-immunetherapyshouldbean have targeted all three TGF-b isoforms or the receptor have
effective approach, but the limited attempts thus far have had provedunsuccessfulincancerindications.Mostnotably,alarge
mixedresults.VEGFtargetedtherapyhashadsomesuccessin trial using a soluble TGF-b receptor (TGF-b ‘‘trap’’) fused to an
alteringtheimmuneinfiltrateandpossiblyfavoringDCmaturation, anti-PD-L1 antibody failed to exhibit efficacy without much
butthemechanismofthisstrategyispoorlyunderstood.137There toxicity,althoughthedistributionandpharmacodynamicactivity
hasbeenmuchinterestinusingTGF-bantagonists(anti-TGF-b atrelevantsiteswasnotreported.138Itisalsopossiblethatinhib-
antibodies,inhibitorsoftheTGF-breceptorkinase),althoughthe itingtwoormoreisoformssimultaneouslymayitselfhavenegative
therapeutic hypothesisinthese trialsmay not havedirectlyad- consequences for efficacy. TGF-b may be important at several
2198 Immunity56,October10,2023
ll
Review
OPENACCESS
sitesontheCIcyclebeyondcontrollingstromalarchitecturesuch drug under study, as different drugs address different stages
as Treg and Tscl production,139 so further study would appear oftheCIcycle.
warranteddespitethelackofsuccessthusfar. Afurtherchallengethathaslimitedprogressintheclinicisthat
Chemotherapy/PD-L1 combinations have had success, many combinations have been tested in suboptimal circum-
potentially by targeting immune resistance within the TME, stances, in small single arm trials with heterogeneous patient
but results have been inconsistent across tumor types.140,141 populationspreviouslyexposedtoimmunetherapy.Manycom-
ThereisarationaleforexploringnewagentssuchasPARPin- binations,potentiallyactiveinspecificclinicalsettings,mayhave
hibition or CDK4/6 inhibition or antibody-drug conjugates beendiscardedprematurely.However,examplesofunsuccess-
(ADCs) in combination with immune therapy. Many trials are fuldrugdevelopmentsuchasIDOinhibition,whichprogressed
ongoing and should be explored not only with efficacy goals quickly from phase I to phase III combinations without single
but also to learn more about the immune modulatory effects agent activity, genetics, or activity in pre-clinical models high-
oftheseagents. lights the difficulty associated with unbridled enthusiasm.149
Therehasalsobeenpreliminarysuccessintargetingthemi- Robustinitialtestingishighlydesirable,andifdrugs areto be
crobiome,whichadjuststhehostsimmunerepertoire.Theprin- developedabsentsingleagentactivity,theremustbeatestable
cipleofthehostimmunefitnessisgainingmomentum.Thelink therapeutic hypothesis that one can evaluate during a trial, so
betweenthisfitness,thegutmicrobiome,andimprovingimmune that important mechanistic and pharmacodynamic information
therapyefficacyisbeingclinicallytested.Encouragingrandom- canbeobtainedregardlessofthetrial’sefficacyoutcome.This
izedphaseIIdatashowedenhancedactivityofimmunecombi- returnsus,again,tothedevelopmentofconceptssuchasthe
nations, by altering the microbiome with oral agents such as CI cycle: having a clear framework within which one can view
CBM-588havebeenpublished.142 the steps that must occur to mount and sustain an effective
Many novel immune combinations have failed. They have anti-cancerresponseisessentialtointerpretingcomplexclinical
beentestedinvariouscancertypeswithdistinctimmunological outcomes.
features but without attention paid to the immunotypes under
investigation.Thishasledtothehypothesisofimmunerespon- CONCLUDINGREMARKS
siveandresistanthistologicaltumor(melanomavs.pancreas).
While this is true at one level, it is an over generalization that Adecadeafteritspublication,thebasicfeaturesoftheCIcycle
couldberefinedbyconsideringtheimmunotypesofthepatients remainanaccuratereflectionofourunderstandingoftheimmune
under investigation. Tumor and TME heterogeneity show im- response in cancer. Yet, understanding the cycle’s individual
munerepertoirevariabilityeveninclassicnon-immunerespon- stepsandhowtheyinterconnectdoesnotbyitselfensureanun-
sivecancers,suchasprostatecancer,suggestingthatindeed derstandingoftheirmechanismsofaction.Wehavenotedhow
immuneresponseshavebeengeneratedbutrenderedineffec- initial mechanistic assumptions, even of successful therapies,
tive.TherandomizedtrialsforPD-(L)1-basedtherapyinprostate such as exhaustion reversal by checkpoint inhibitors, have
cancer are negative in unselected patients, but those rare pa- changedasaconsequenceofdetailedstudy.Wehavealsonoted
tients with tumor immune infiltration exhibited increased newinformationthatTcellactivationcanbeinfluencednotonlyin
responserates.143Moreover,experimentsinmice,andpossibly dLNbutinthetumorandtumor-associatedlymphoidstructures
humans,havedemonstratedtheimmunosuppressiveaspectsof suchasTLSs.Suchinsightsshouldimpacthowwethinkabout
androgenson(male)CD8Tcells.144–146 objectivesforsculptingthemosteffectiveTcellresponses:qual-
Together,theseconsiderationssuggestthattheoverallmech- ity,trajectory,andpersistencemaybeasimportantasquantity.
anismofresponseismultifactorialbutbiologicallysimilaracross Similarly,suchconsiderationsshouldimpactourunderstanding
tumortypes.Animportantstepwouldbetocategorizepatients ofTcell-basedimmune-relatedtoxicities.
according to immunotype (e.g., immune excluded vs. immune Thefactthatonlyaboutone-thirdofpatientsrespondtoimmu-
inflamed can both be PD-L1 positive) although it is likely that notherapy remains a major challenge, one that is even more
thereisfurtherheterogeneityevenwithinimmunotypethatcould dauntingthanacquiredresistancetotherapy.Giventheimpor-
contributetoresponsevariability. tanceoftheTMEand,especially,oftumorimmunotypesinregu-
Overthelastdecade,therehasbeenampleclinicalresearchto latingTcellresponses, farmoreattentionneedstobepaidto
showthatinnate,adaptiveandimmuneindependentbiomarker these factors when searching for ways to further leverage
(suchasstromalbiomarkers)allplayaroleinresponse.147Thisis Tcellimmunityincancer.Althoughnext-generationcheckpoint
inadditiontotumorrelatedfactorssuchasoncogeneallelesand inhibitorsarelikelytobringsomebenefit,itseemsunlikelythat
tumormutationburden.Themultifactorialmechanismsofsensi- they alone will overcome the barriers endemic to the immune
tivityandresistancemeanthatnosinglebiomarkersuchasPD- excluded and immune desert immunotypes. Solving the basis
L1 or tumor mutational burden (TMB) will account solely for fortheseimmunerestrictivesituationsandgeneratingtherapeu-
response.148Aswedevelopnewerimmunetherapiesatdifferent tics that render these immunotypes more permissive to T cell
points of the CI cycle, alternative biomarkers will be needed. activityrepresentthegreatestopportunitiesforthenexttransfor-
Indeed, the modified cycle increases the chances to discover mativestepforward:perhapsasmanyas60%–70%ofallcancer
unifiedbiomarkersasitnowcallsoutadditionalcriticalactivities patients have tumors that exhibit immune-restrictive pheno-
(e.g., the requirement for T cell stimulation by DCs or other types,andthislargegroupcontainsthebulkofindividualswho
antigen-presenting cells in the tumor) that had not been proverefractorytoICI.
previously considered. Clearly, these will go beyond PD-L1 Transferringimmunotherapiestoearlydiseaseortheadjuvant
expression or TMB and may even be specific to the class of settingwhereimmunotypesmaybelessrestrictiveandpossibly
Immunity56,October10,2023 2199
ll
Review
OPENACCESS
moreplasticcouldalsorepresentachanceforsignificantclinical 11.vanVlerken-Ysla,L.,Tyurina,Y.Y.,Kagan,V.E.,andGabrilovich, D.I.
advances.Buthere,too,mechanisticunderstandingwillbekey. (2023). Functional states of myeloid cells in cancer. Cancer Cell 41,
490–504.https://doi.org/10.1016/j.ccell.2023.02.009.
In the end, the challenges of developing immune therapies
reflectthecomplexityofhumanimmunity,specificallythearray 12.Barrett,R.L.,andPure´,E.(2020).Cancer-associatedfibroblastsandtheir
of mechanisms responsible for creating rate limiting steps at influence on tumor immunity and immunotherapy. Elife 9, e57243.
https://doi.org/10.7554/elife.57243.
each successive step of the CIcycle. Thisconsideration goes
beyondeventheexistenceofpermissiveorrestrictiveimmuno- 13.Caligiuri,G.,andTuveson,D.A.(2023).Activatedfibroblastsincancer:
types and can include immunotype-agnostic features that can
Perspectivesandchallenges.CancerCell41,434–449.https://doi.org/
10.1016/j.ccell.2023.02.015.
best be described as mechanisms of shared immune escape.
Suchmechanismswouldincludetheinvolvementofbothcancer 14.Mariathasan,S.,Turley,S.J.,Nickles,D.,Castiglioni,A.,Yuen,K.,Wang,
intrinsicandextrinsicfactors,suchasclassIlossordownregu- Y.,Kadel,E.E.,Koeppen,H.,Astarita,J.L.,Cubas,R.,etal.(2018).TGFb
attenuates tumour response to PD-L1 blockade by contributing to
lation, neoantigen loss, an accumulation of multiple immune exclusion of T cells. Nature 554, 544–548. https://doi.org/10.1038/
checkpoints, mounting populations of suppressive cells in the nature25501.
TME,andthelossoftheappropriatecellpopulations.Earlydis-
15.Fridman,W.H.,Meylan,M.,Pupier,G.,Calvez,A.,Hernandez,I.,and
easesettingsmayavoidatleastsomeofthesemechanisms;ma- Saute`s-Fridman,C.(2023).TertiarylymphoidstructuresandBcells:An
chinelearningmodelsinformedbyrelevantbiomarkerdatamay intratumoralimmunitycycle.Immunity56,2254–2269.https://doi.org/
10.1016/j.immuni.2023.08.009.
help mitigate them or suggest new therapeutic combinations
whentheydooccur.Whatevertheapproach,thegoalwillremain 16.Ghorani,E.,Swanton,C.,andQuezada,S.A.(2023).Cancercell-intrinsic
taking appropriate steps to ensure the continued revolution of mechanisms driving acquired immune tolerance. Immunity 56, 2270–
2295.https://doi.org/10.1016/j.immuni.2023.09.004.
thecancer-immunitycycle.Declarationofinterests
Theauthorsdeclarenocompetinginterests. 17.Wherry,E.J.,andKurachi,M.(2015).Molecularandcellularinsightsinto
Tcellexhaustion.Nat.Rev.Immunol.15,486–499.https://doi.org/10.
1038/nri3862.
REFERENCES
18.Philip,M.,Fairchild,L.,Sun,L.,Horste,E.L.,Camara,S.,Shakiba,M.,
Scott,A.C.,Viale,A.,Lauer,P.,Merghoub,T.,etal.(2017).Chromatin
1. Sharma,P.,Goswami,S.,Raychaudhuri,D.,Siddiqui,B.A.,Singh,P., statesdefinetumour-specificTcelldysfunctionandreprogramming.Na-
Nagarajan,A.,Liu,J.,Subudhi,S.K.,Poon,C.,Gant,K.L.,etal.(2023). ture545,452–456.https://doi.org/10.1038/nature22367.
Immune checkpoint therapy—current perspectives and future direc-
tions.Cell186,1652–1669.https://doi.org/10.1016/j.cell.2023.03.006.
19.Sen, D.R., Kaminski, J., Barnitz, R.A., Kurachi, M., Gerdemann, U.,
Yates,K.B.,Tsao,H.-W.,Godec,J.,LaFleur,M.W.,Brown,F.D.,etal.
2. Hashimoto, M., Kamphorst, A.O., Im, S.J., Kissick, H.T., Pillai, R.N., (2016). The epigenetic landscape of T cell exhaustion. Science 354,
Ramalingam,S.S.,Araki,K.,andAhmed,R.(2018).CD8TCellExhaus- 1165–1169.https://doi.org/10.1126/science.aae0491.
tion in Chronic Infection and Cancer: Opportunities for Interventions.
Annu. Rev. Med. 69, 301–318. https://doi.org/10.1146/annurev-med- 20.Delacher,M.,Simon,M.,Sanderink,L.,Hotz-Wagenblatt,A.,Wuttke,M.,
012017-043208. Schambeck,K.,Schmidleithner,L.,Bittner,S.,Pant,A.,Ritter,U.,etal.
(2021). Single-cell chromatin accessibility landscape identifies tissue
3. Philip, M.,and Schietinger,A. (2022).CD8+ Tcell differentiation and repairprograminhumanregulatoryTcells.Immunity54,702–720.e17.
dysfunctionincancer.Nat.Rev.Immunol.22,209–223.https://doi.org/ https://doi.org/10.1016/j.immuni.2021.03.007.
10.1038/s41577-021-00574-3.
21.Youngblood, B., Oestreich, K.J., Ha, S.-J., Duraiswamy, J., Akondy,
4. Wherry, E.J. (2011). T cell exhaustion. Nat. Immunol. 12, 492–499. R.S.,West,E.E.,Wei,Z.,Lu,P.,Austin,J.W.,Riley,J.L.,etal.(2011).
https://doi.org/10.1038/ni.2035. ChronicVirusInfectionEnforcesDemethylationoftheLocusthatEn-
codesPD-1inAntigen-SpecificCD8+TCells.Immunity35,400–412.
5. Chen,D.S.,andMellman,I.(2013).OncologyMeetsImmunology:The https://doi.org/10.1016/j.immuni.2011.06.015.
Cancer-Immunity Cycle. Immunity 39, 1–10. https://doi.org/10.1016/j.
immuni.2013.07.012. 22.Oh,S.A.,Wu,D.-C.,Cheung,J.,Navarro,A.,Xiong,H.,Cubas,R.,Totpal,
K.,Chiu,H.,Wu,Y.,Comps-Agrar,L.,etal.(2020).PD-L1expressionby
6. Herbst,R.S.,Soria,J.-C.,Kowanetz,M.,Fine,G.D.,Hamid,O.,Gordon, dendriticcellsisakeyregulatorofT-cellimmunityincancer.Nat.Cancer
M.S.,Sosman,J.A.,McDermott,D.F.,Powderly,J.D.,Gettinger,S.N., 1,681–691.https://doi.org/10.1038/s43018-020-0075-x.
etal.(2014).Predictivecorrelatesofresponsetotheanti-PD-L1antibody
MPDL3280Aincancerpatients.Nature515,563–567.https://doi.org/10. 23.Topalian,S.L.,Forde,P.M.,Emens,L.A.,Yarchoan,M.,Smith,K.N.,and
1038/nature14011. Pardoll,D.M.(2023).Neoadjuvantimmunecheckpointblockade:Awin-
dowofopportunitytoadvancecancerimmunotherapy.CancerCell41,
7. Hegde,P.S.,andChen,D.S.(2020).Top10ChallengesinCancerImmu- 1551–1566.https://doi.org/10.1016/j.ccell.2023.07.011.
notherapy.Immunity52,17–35.https://doi.org/10.1016/j.immuni.2019.
12.011. 24.Rojas,L.A.,Sethna,Z.,Soares,K.C.,Olcese,C.,Pang,N.,Patterson,E.,
Lihm,J.,Ceglia,N.,Guasp,P.,Chu,A.,etal.(2023).PersonalizedRNA
8. Chen,D.S.,andMellman,I.(2017).Elementsofcancerimmunityandthe neoantigenvaccinesstimulateTcellsinpancreaticcancer.Nature618,
cancer–immunesetpoint.Nature541,321–330.https://doi.org/10.1038/ 144–150.https://doi.org/10.1038/s41586-023-06063-y.
nature21349.
25.Baharom,F.,Ramirez-Valdez,R.A.,Tobin,K.K.S.,Yamane,H.,Dutertre,
9. Ortiz-Mun˜oz,G.,Brown,M.,Carbone,C.B.,Pechuan-Jorge,X.,Rouilly, C.-A.,Khalilnezhad,A.,Reynoso,G.V.,Coble,V.L.,Lynn,G.M.,Mule`,
V.,Lindberg,H.,Ritter,A.T.,Raghupathi,G.,Sun,Q.,Nicotra,T.,etal. M.P., et al. (2021). Intravenous nanoparticle vaccination generates
(2023).Insitutumourarraysrevealearlyenvironmentalcontrolofcancer stem-likeTCF1+neoantigen-specificCD8+Tcells.Nat.Immunol.22,
immunity. Nature 618, 827–833. https://doi.org/10.1038/s41586-023- 41–52.https://doi.org/10.1038/s41590-020-00810-3.
06132-2.
26.Baharom,F.,Ramirez-Valdez,R.A.,Khalilnezhad,A.,Khalilnezhad,S.,
10. Davidson,S.,Coles,M.,Thomas,T.,Kollias,G.,Ludewig,B.,Turley,S., Dillon, M., Hermans, D., Fussell, S., Tobin, K.K.S., Dutertre, C.-A.,
Brenner,M.,Buckley,C.D.,andChristopher.(2021).Fibroblastsasim- Lynn,G.M.,etal.(2022).SystemicvaccinationinducesCD8+Tcells
muneregulatorsininfection,inflammationandcancer.Nat.Rev.Immu- and remodels the tumor microenvironment. Cell 185, 4317–4332.
nol.21,704–717.https://doi.org/10.1038/s41577-021-00540-z. https://doi.org/10.1016/j.cell.2022.10.006.
2200 Immunity56,October10,2023
ll
Review
OPENACCESS
27.Cao,L.L.,andKagan,J.C.(2023).Targetinginnateimmunepathwaysfor 42.Sanford-Crane,H.,Abrego,J.,andSherman,M.H.(2019).Fibroblastsas
cancer immunotherapy. Immunity 56, 2206–2217. https://doi.org/10. ModulatorsofLocalandSystemicCancerMetabolism.Cancers11,619.
1016/j.immuni.2023.07.018. https://doi.org/10.3390/cancers11050619.
28.Arvedson,T.,Bailis,J.M.,Britten,C.D.,Klinger,M.,Nagorsen,D.,Coxon, 43.Mukhopadhyay, S., Encarnacion-Rosado, J., and Kimmelman, A.C.
A.,Egen,J.G.,andMartin,F.(2022).TargetingSolidTumorswithBispe- (2023). Autophagy fuels mitochondrial function through regulation of
cificTCellEngagerImmuneTherapy.Annu.Rev.CancerBiol.6,17–34. ironmetabolisminpancreaticcancer.Autophagy,1–2.https://doi.org/
https://doi.org/10.1146/annurev-cancerbio-070620-104325. 10.1080/15548627.2023.2223473.
29.Singh,N.,andMaus,M.V.(2023).Syntheticmanipulationofthecancer 44.Su,S.,Chen,J.,Yao,H.,Liu,J.,Yu,S.,Lao,L.,Wang,M.,Luo,M.,Xing,
immunitycycle:CAR-Tcelltherapy.Immunity56,2296–2310.https:// Y.,Chen,F.,etal.(2018).CD10+GPR77+Cancer-AssociatedFibroblasts
doi.org/10.1016/j.immuni.2023.09.010. PromoteCancerFormationandChemoresistancebySustainingCancer
Stemness. Cell 172, 841–856.e16. https://doi.org/10.1016/j.cell.2018.
01.009.
30.Broz,M.L.,Binnewies,M.,Boldajipour,B.,Nelson,A.E.,Pollack,J.L.,
Erle,D.J.,Barczak,A.,Rosenblum,M.D.,Daud,A.,Barber,D.L.,etal.
45.Kumar,V.,Donthireddy,L.,Marvel,D.,Condamine,T.,Wang,F.,Lavilla-
(2014).DissectingtheTumorMyeloidCompartmentRevealsRareActi-
Alonso,S.,Hashimoto,A.,Vonteddu,P.,Behera,R.,Goins,M.A.,etal.
vatingAntigen-PresentingCellsCriticalforTCellImmunity.CancerCell
26,638–652.https://doi.org/10.1016/j.ccell.2014.09.007. (2017).Cancer-AssociatedFibroblastsNeutralizetheAnti-tumorEffect
ofCSF1ReceptorBlockadebyInducingPMN-MDSCInfiltrationofTu-
mors.CancerCell32,654–668.e5.https://doi.org/10.1016/j.ccell.2017.
31.Tran,E.,Turcotte,S.,Gros,A.,Robbins,P.F.,Lu,Y.-C.,Dudley,M.E.,
10.005.
Wunderlich, J.R., Somerville, R.P., Hogan, K., Hinrichs, C.S., et al.
(2014). Cancer Immunotherapy Based on Mutation-Specific CD4+ T
46.Chakravarthy,A.,Khan,L.,Bensler,N.P.,Bose,P.,andDeCarvalho,D.D.
CellsinaPatientwithEpithelialCancer.Science344,641–645.https://
(2018).TGF-Iˆ2-associatedextracellularmatrixgeneslinkcancer-associ-
doi.org/10.1126/science.1251102.
atedfibroblaststoimmuneevasionandimmunotherapyfailure.Nat.Com-
mun.9,4692–4710.https://doi.org/10.1038/s41467-018-06654-8.
32.Tran,E.,Robbins,P.F.,Lu,Y.-C.,Prickett,T.D.,Gartner,J.J.,Jia,L.,Pa-
setto,A.,Zheng,Z.,Ray,S.,Groh,E.M.,etal.(2016).T-CellTransfer 47.Attieh,Y.,Clark,A.G.,Grass,C.,Richon,S.,Pocard,M.,Mariani,P.,El-
Therapy Targeting Mutant KRAS in Cancer. N. Engl. J. Med. 375, khatib,N.,Betz,T.,Gurchenkov,B.,andVignjevic,D.M.(2017).Cancer-
2255–2262.https://doi.org/10.1056/nejmoa1609279. associatedfibroblastsleadtumorinvasionthroughintegrin-b3–depen-
dentfibronectinassembly.J.CellBiol.216,3509–3520.https://doi.org/
33.Rohaan,M.W.,Borch,T.H.,vandenBerg,J.H.,Met,O¨.,Kessels,R., 10.1083/jcb.201702033.
Geukes Foppen, M.H., Stoltenborg Granhøj, J., Nuijen, B., Nijenhuis,
C.,Jedema,I.,etal.(2022).Tumor-InfiltratingLymphocyteTherapyor 48.Lo,A.,Wang,L.-C.S.,Scholler,J.,Monslow,J.,Avery,D.,Newick,K.,
IpilimumabinAdvancedMelanoma.N.Engl.J.Med.387,2113–2125. O’Brien,S.,Evans,R.A.,Bajor, D.J.,Clendenin,C.,etal.(2015).Tu-
https://doi.org/10.1056/nejmoa2210233. mor-Promoting Desmoplasia Is Disrupted by Depleting FAP-
ExpressingStromalCells.CancerRes.75,2800–2810.https://doi.org/
34.Conde,E.,Vercher,E.,Soria-Castellano,M.,Suarez-Olmos,J.,Man- 10.1158/0008-5472.can-14-3041.
chen˜o,U.,Elizalde,E.,Rodriguez,M.L.,Glez-Vaz,J.,Casares,N.,Rodrı´-
guez-Garc´ıa,E.,etal.(2021).Epitopespreadingdrivenbythejointaction 49.Nguyen,E.V.,Pereira,B.A.,Lawrence,M.G.,Ma,X.,Rebello,R.J.,Chan,
ofCARTcellsandpharmacologicalSTINGstimulationcounteractstumor H., Niranjan,B., Wu,Y.,Ellem,S., Guan,X.,et al.(2019).Proteomic
escape via antigen-lossvariants.J.Immunother. Cancer 9,e003351. ProfilingofHumanProstateCancer-associatedFibroblasts(CAF)Re-
https://doi.org/10.1136/jitc-2021-003351. veals LOXL2-dependent Regulation of the Tumor Microenvironment*
[S].Mol.Cell.Proteomics18,1410–1427.https://doi.org/10.1074/mcp.
35.Ma,L.,Hostetler,A.,Morgan,D.M.,Maiorino,L.,Sulkaj,I.,Whittaker, ra119.001496.
C.A.,Neeser,A.,Pires,I.S.,Yousefpour,P.,Gregory,J.,etal.(2023).
Vaccine-boostedCARTcrosstalkwithhostimmunitytorejecttumors 50.Ligorio,M.,Sil,S.,Malagon-Lopez,J.,Nieman,L.T.,Misale,S.,DiPilato,
with antigen heterogeneity. Cell 186, 3148–3165.e20. https://doi.org/ M.,Ebright,R.Y.,Karabacak,M.N.,Kulkarni,A.S.,Liu,A.,etal.(2019).
10.1016/j.cell.2023.06.002. Stromal Microenvironment Shapes the Intratumoral Architecture of
Pancreatic Cancer. Cell 178, 160–175.e27. https://doi.org/10.1016/j.
36.Plikus,M.V.,Wang,X.,Sinha,S.,Forte,E.,Thompson,S.M.,Herzog, cell.2019.05.012.
E.L., Driskell, R.R., Rosenthal, N., Biernaskie, J., and Horsley, V.
(2021).Fibroblasts:Origins,definitions,andfunctionsinhealthanddis-
51.Dominguez,C.X.,Mu€ller,S.,Keerthivasan,S.,Koeppen,H.,Hung,J.,
ease.Cell184,3852–3872.https://doi.org/10.1016/j.cell.2021.06.024. Gierke, S., Breart, B., Foreman, O., Bainbridge, T.W., Castiglioni, A.,
et al. (2020). Single-Cell RNA Sequencing Reveals Stromal Evolution
intoLRRC15+MyofibroblastsasaDeterminantofPatientResponseto
37.Santi,A.,Kugeratski,F.G.,andZanivan,S.(2018).CancerAssociatedFi-
broblasts: The Architects of Stroma Remodeling. Proteomics 18, Cancer Immunotherapy. Cancer Discov. 10, 232–253. https://doi.org/
10.1158/2159-8290.cd-19-0644.
1700167.https://doi.org/10.1002/pmic.201700167.
52.Krishnamurty,A.T.,Shyer,J.A.,Thai,M.,Gandham,V.,Buechler,M.B.,
38.Schwo¨rer,S.,Cimino,F.V.,Ros,M.,Tsanov,K.M.,Ng,C.,Lowe,S.W.,
Yang,Y.A., Pradhan, R.N.,Wang, A.W.,Sanchez,P.L., Qu, Y.,etal.
Carmona-Fontaine,C.,andThompson,C.B.(2023).HypoxiaPotentiates
(2022).LRRC15+myofibroblastsdictatethestromalsetpointtosuppress
theInflammatoryFibroblastPhenotypePromotedbyPancreaticCancer tumourimmunity.Nature611,148–154.https://doi.org/10.1038/s41586-
Cell–DerivedCytokines.CancerRes.83,1596–1610.https://doi.org/10.
022-05272-1.
1158/0008-5472.can-22-2316.
53.Kraman,M.,Bambrough,P.J.,Arnold,J.N.,Roberts,E.W.,Magiera,L.,
39.Pure´,E.,andBlomberg,R.(2018).Pro-tumorigenicrolesoffibroblast Jones,J.O., Gopinathan, A.,Tuveson, D.A., andFearon, D.T. (2010).
activationproteinincancer:backtothebasics.Oncogene37,4343–
SuppressionofAntitumorImmunitybyStromalCellsExpressingFibro-
4357.https://doi.org/10.1038/s41388-018-0275-3. blast Activation Protein–a. Science 330, 827–830. https://doi.org/10.
1126/science.1195300.
40.Sahai,E.,Astsaturov,I.,Cukierman,E.,DeNardo,D.G.,Egeblad,M.,
Evans,R.M.,Fearon,D.,Greten,F.R.,Hingorani,S.R.,Hunter,T.,etal. 54.Feig,C.,Jones,J.O.,Kraman,M.,Wells,R.J.B.,Deonarine,A.,Chan,
(2020).Aframeworkforadvancingourunderstandingofcancer-associ- D.S., Connell, C.M., Roberts, E.W., Zhao, Q., Caballero, O.L., et al.
atedfibroblasts.Nat.Rev.Cancer20,174–186.https://doi.org/10.1038/ (2013).TargetingCXCL12fromFAP-expressingcarcinoma-associated
s41568-019-0238-1. fibroblasts synergizes with anti–PD-L1 immunotherapy in pancreatic
cancer. Proc. Natl. Acad. Sci. 110, 20212–20217. https://doi.org/10.
41.Helms,E.J.,Berry,M.W.,Chaw,R.C.,DuFort,C.C.,Sun,D.,Onate,M.K., 1073/pnas.1320318110.
Oon,C.,Bhattacharyya,S.,Sanford-Crane,H.,Horton,W.,etal.(2021).
MesenchymalLineageHeterogeneityUnderliesNon-RedundantFunc- 55.Koncina,E.,Nurmik,M.,Pozdeev,V.I.,Gilson,C.,Tsenkova,M.,Begaj,
tionsofPancreaticCancer-AssociatedFibroblasts.CancerDiscov.12, R.,Stang,S.,Gaigneaux,A.,Weindorfer,C.,Rodriguez,F.,etal.(2023).
484–501.https://doi.org/10.1158/2159-8290.cd-21-0601. IL1R1+ cancer-associated fibroblasts drive tumor development and
Immunity56,October10,2023 2201
ll
Review
OPENACCESS
immunosuppression in colorectal cancer. Nat. Commun. 14, 4251. 70.Liu,Q.,Chen,G.,Moore,J.,Guix,I.,Placantonakis,D.,andBarcellos-
https://doi.org/10.1038/s41467-023-39953-w. Hoff,M.H.(2022).ExploitingCanonicalTGFbSignalinginCancerTreat-
ment.Mol.CancerTher.21,16–24.https://doi.org/10.1158/1535-7163.
56. Biffi,G.,Oni,T.E.,Spielman,B.,Hao,Y.,Elyada,E.,Park,Y.,Preall,J., mct-20-0891.
andTuveson,D.A.(2019).IL-1-inducedJAK/STATsignalingisantago-
nized by TGF-beta to shape CAF heterogeneity in pancreatic ductal 71.Cassetta,L.,andPollard,J.W.(2023).Atimelineoftumour-associated
adenocarcinoma.CancerDiscov.9,282–301.https://doi.org/10.1158/ macrophagebiology.Nat.Rev.Cancer23,238–257.https://doi.org/10.
2159-8290.cd-18-0710. 1038/s41568-022-00547-1.
57. Elyada,E.,Bolisetty,M.,Laise,P.,Flynn,W.F.,Courtois,E.T.,Burkhart, 72.Ren,X.,Zhang,L.,Zhang,Y.,Li,Z.,Siemers,N.,andZhang,Z.(2021).
R.A.,Teinor,J.A.,Belleau,P.,Biffi,G.,Lucito,M.S.,etal.(2019).Cross- InsightsGainedfromSingle-CellAnalysisofImmuneCellsintheTumor
SpeciesSingle-CellAnalysisofPancreaticDuctalAdenocarcinomaRe- Microenvironment. Annu. Rev.Immunol. 39, 583–609. https://doi.org/
veals Antigen-Presenting Cancer-Associated Fibroblasts.Cancer Dis- 10.1146/annurev-immunol-110519-071134.
cov.9,1102–1123.https://doi.org/10.1158/2159-8290.cd-19-0094.
73.Mulder,K.,Patel,A.A.,Kong,W.T.,Piot,C.,Halitzki,E.,Dunsmore,G.,
58. Huang,H.,Wang,Z.,Zhang,Y.,Pradhan,R.N.,Ganguly,D.,Chandra,R., Khalilnezhad,S.,Irac,S.E.,Dubuisson,A.,Chevrier,M.,etal.(2021).
Murimwa,G.,Wright,S.,Gu,X.,Maddipati,R.,etal.(2022).Mesothelial Cross-tissue single-cell landscape of human monocytes and macro-
cell-derived antigen-presenting cancer-associated fibroblasts induce phagesinhealthanddisease.Immunity54,1883–1900.e5.https://doi.
expansionofregulatoryTcellsinpancreaticcancer.CancerCell40, org/10.1016/j.immuni.2021.07.007.
656–673.e7.https://doi.org/10.1016/j.ccell.2022.04.011.
74.Pittet,M.J.,Michielin,O.,andMigliorini,D.(2022).Clinicalrelevanceof
59. Zuo,C.,Baer,J.M.,Knolhoff,B.L.,Belle,J.I.,Liu,X.,AlarconDeLaLas- tumour-associatedmacrophages.Nat.Rev.Clin.Oncol.19,402–421.
tra,A.,Fu,C.,Hogg,G.D.,Kingston,N.L.,Breden,M.A.,etal.(2023). https://doi.org/10.1038/s41571-022-00620-6.
Stromal and therapy-induced macrophage proliferation promotes
PDACprogressionandsusceptibilitytoinnateimmunotherapy.J.Exp. 75.Franklin, R.A., Liao, W., Sarkar, A., Kim, M.V., Bivona, M.R., Liu, K.,
Med.220,e20212062.https://doi.org/10.1084/jem.20212062. Pamer,E.G.,andLi,M.O.(2014).Thecellularandmolecularoriginoftu-
mor-associated macrophages.Science344,921–925.https://doi.org/
60. Chen,Y.,McAndrews,K.M.,andKalluri,R.(2021).Clinicalandtherapeu- 10.1126/science.1252510.
ticrelevanceofcancer-associatedfibroblasts.Nat.Rev.Clin.Oncol.18,
792–804.https://doi.org/10.1038/s41571-021-00546-5. 76.Zhu,Y.,Herndon,J.M.,Sojka,D.K.,Kim,K.-W.,Knolhoff,B.L.,Zuo,C.,
Cullinan,D.R.,Luo,J.,Bearden,A.R.,Lavine,K.J.,etal.(2017).Tissue-
61. McAndrews,K.M.,Chen,Y.,Darpolor,J.K.,Zheng,X.,Yang,S.,Cars- ResidentMacrophagesinPancreaticDuctalAdenocarcinomaOriginate
tens,J.L.,Li,B.,Wang,H.,Miyake,T.,CorreadeSampaio,P.,etal. fromEmbryonicHematopoiesisandPromoteTumorProgression.Immu-
(2022). Identification of Functional Heterogeneity of Carcinoma- nity47,323–338.e6.https://doi.org/10.1016/j.immuni.2017.07.014.
AssociatedFibroblastswithDistinctIL6-MediatedTherapyResistance
inPancreaticCancer. Cancer Discov.12,1580–1597.https://doi.org/ 77.Kloosterman,D.J.,andAkkari,L.(2023).Macrophagesattheinterfaceof
10.1158/2159-8290.cd-20-1484. theco-evolvingcancerecosystem.Cell186,1627–1651.https://doi.org/
10.1016/j.cell.2023.02.020.
62. Kerdidani,D.,Aerakis,E.,Verrou,K.-M.,Angelidis,I.,Douka,K.,Maniou,
M.-A., Stamoulis, P., Goudevenou, K., Prados, A., Tzaferis, C., et al. 78.Zhang,X.,Ji,L.,andLi,M.O.(2023).Controloftumor-associatedmacro-
(2022).LungtumorMHCIIimmunitydependsoninsituantigenpresenta- phageresponsesbynutrientacquisitionandmetabolism.Immunity56,
tion by fibroblasts. J. Exp. Med. 219, e20210815. https://doi.org/10. 14–31.https://doi.org/10.1016/j.immuni.2022.12.003.
1084/jem.20210815.
79.Veglia,F.,Tyurin,V.A.,Blasi,M.,DeLeo,A.,Kossenkov,A.V.,Donthir-
63. Salmon,H.,Franciszkiewicz,K.,Damotte,D.,Dieu-Nosjean,M.-C.,Val- eddy,L.,To,T.K.J.,Schug,Z.,Basu,S.,Wang,F.,etal.(2019).Fatty
idire,P.,Trautmann,A.,Mami-Chouaib,F.,andDonnadieu,E.(2012). acidtransportprotein2reprogramsneutrophilsincancer.Nature569,
Matrixarchitecturedefinesthepreferentiallocalizationandmigrationof 73–78.https://doi.org/10.1038/s41586-019-1118-2.
T cells into the stroma of human lung tumors. J. Clin. Invest. 122,
899–910.https://doi.org/10.1172/jci45817. 80.Li,W.,Tanikawa,T.,Kryczek,I.,Xia,H.,Li,G.,Wu,K.,Wei,S.,Zhao,L.,
Vatan,L.,Wen,B.,etal.(2018).AerobicGlycolysisControlsMyeloid-
64. Grout,J.A.,Sirven,P.,Leader,A.M.,Maskey,S.,Hector,E.,Puisieux,I., DerivedSuppressorCellsandTumorImmunityviaaSpecificCEBPBIso-
Steffan,F.,Cheng,E.,Tung,N.,Maurin,M.,etal.(2022).SpatialPosi- form in Triple-Negative Breast Cancer. Cell Metab. 28, 87–103.e6.
tioningandMatrixProgramsofCancer-AssociatedFibroblastsPromote https://doi.org/10.1016/j.cmet.2018.04.022.
T-cellExclusioninHumanLungTumors.CancerDiscov.12,2606–2625.
https://doi.org/10.1158/2159-8290.cd-21-1714. 81.Casanova-Acebes,M.,Dalla,E.,Leader,A.M.,LeBerichel,J.,Nikolic,J.,
Morales,B.M.,Brown,M.,Chang,C.,Troncoso,L.,Chen,S.T.,etal.
65. Salmon,H.,andDonnadieu,E.(2012).Withintumors,interactionsbe- (2021).Tissue-residentmacrophagesprovideapro-tumorigenicniche
tweenTcellsandtumorcellsareimpededbytheextracellularmatrix.On- to early NSCLC cells. Nature 595, 578–584. https://doi.org/10.1038/
coImmunology1,992–994.https://doi.org/10.4161/onci.20239. s41586-021-03651-8.
66. Herzog, B.H., Baer, J.M., Borcherding, N., Kingston, N.L., Belle, J.I., 82.Nixon,B.G.,Kuo,F.,Ji,L.,Liu,M.,Capistrano,K.,Do,M.,Franklin,R.A.,
Knolhoff, B.L., Hogg, G.D.,Ahmad, F., Kang, L.-I., Petrone, J.,et al. Wu,X.,Kansler,E.R.,Srivastava,R.M.,etal.(2022).Tumor-associated
(2023). Tumor-associated fibrosis impairs immune surveillance and macrophagesexpressingthetranscriptionfactorIRF8promoteTcell
responsetoimmunecheckpointblockadeinnon–smallcelllungcancer. exhaustion in cancer. Immunity 55, 2044–2058.e5. https://doi.org/10.
Sci. Transl. Med. 15,eadh8005. https://doi.org/10.1126/scitranslmed. 1016/j.immuni.2022.10.002.
adh8005.
83.Kersten,K.,Hu,K.H.,Combes,A.J.,Samad,B.,Harwin,T.,Ray,A.,Rao,
67. Tauriello, D.V.F., Palomo-Ponce, S., Stork, D., Berenguer-Llergo, A., A.A.,Cai,E.,Marchuk,K.,Artichoker,J.,etal.(2022).Spatiotemporalco-
Badia-Ramentol,J.,Iglesias,M.,Sevillano,M.,Ibiza,S.,Can˜ellas,A., dependencybetweenmacrophagesandexhaustedCD8+Tcellsincan-
Hernando-Momblona,X.,etal.(2018).TGFbdrivesimmuneevasionin cer. Cancer Cell 40, 624–638.e9. https://doi.org/10.1016/j.ccell.2022.
genetically reconstituted colon cancer metastasis. Nature Publishing 05.004.
Group554,538–543.https://doi.org/10.1038/nature25492.
84.Klemm, F.,Mo¨ckl,A.,Salamero-Boix, A.,Alekseeva,T.,Scha€ffer,A.,
68. Castiglioni,A.,Yang,Y.,Williams,K.,Gogineni,A.,Lane,R.S.,Wang, Schulz,M.,Niesel,K.,Maas,R.R.,Groth,M.,Elie,B.T.,etal.(2021).
A.W., Shyer,J.A., Zhang, Z.,Mittman,S.,Gutierrez,A.,etal. (2023). CompensatoryCSF2-drivenmacrophageactivationpromotesadaptive
CombinedPD-L1/TGFbblockadeallowsexpansionanddifferentiation resistancetoCSF1Rinhibitioninbreast-to-brainmetastasis.Nat.Cancer
ofstemcell-likeCD8Tcellsinimmuneexcludedtumors.Nat.Commun. 2,1086–1101.https://doi.org/10.1038/s43018-021-00254-0.
14,4703.https://doi.org/10.1038/s41467-023-40398-4.
85.Quail,D.F.,andJoyce,J.A.(2017).MolecularPathways:Deciphering
69. Tauriello, D.V.F., Sancho, E., and Batlle, E. (2022). Overcoming Mechanisms of Resistance to Macrophage-Targeted Therapies. Clin.
TGFb-mediated immune evasion in cancer. Nat. Rev. Cancer 22, Cancer Res. 23, 876–884. https://doi.org/10.1158/1078-0432.ccr-
25–44.https://doi.org/10.1038/s41568-021-00413-6. 16-0133.
2202 Immunity56,October10,2023
