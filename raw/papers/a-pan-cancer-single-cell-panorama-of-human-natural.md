---
source_path: /mnt/c/Users/Administrator/Zotero/storage/LG45W59F/Tang 等 - 2023 - A pan-cancer single-cell panorama of human natural killer cells.pdf
ingested: 2026-04-23
sha256: c8666f5cc5441bbf
---

Resource
A pan-cancer single-cell panorama of human natural
killer cells
Graphical abstract Authors
FeiTang,JinhuLi,LuQi,...,HuiPeng,
DongfangWang,ZeminZhang
Correspondence
zhuln@pku.edu.cn(L.Z.),
huipeng@ustc.edu.cn(H.P.),
wangdf19@pku.edu.cn(D.W.),
zemin@pku.edu.cn(Z.Z.)
In brief
Integrativesingle-cellRNAsequencing
analysesonnaturalkiller(NK)cellsfrom
over700patientsacross24tumortypes
depictsharedandtumor-type-specific
NKcellfeaturesandhighlightthe
potentialofspecificmyeloidcell
subpopulationsinregulatingNKcellanti-
tumorfunction.
Highlights
d HumanNKcellsexhibittumor-type-specificsubgroup
heterogeneity
d
RGS1expressionisareliablemarkeroftissue-infiltrating
NKcells
d Transcriptomicfeaturesoftumor-associatedNKcells
indicateimpairedcytotoxicity
d
LAMP3+DCsappeartoregulateNKcellfunctionsintumors
basedonspatialanalyses
Tangetal.,2023,Cell186,4235–4251
September14,2023ª2023TheAuthor(s).PublishedbyElsevierInc.
ll
https://doi.org/10.1016/j.cell.2023.07.034
ll
OPENACCESS
Resource
A pan-cancer single-cell panorama
of human natural killer cells
FeiTang,1,7JinhuLi,1,7LuQi,1,2DongfangLiu,3YufeiBo,1ShishangQin,1YuhuiMiao,4KezhuoYu,1WenhongHou,4
JiananLi,1JirunPeng,3,5ZhigangTian,6LinnanZhu,1,*HuiPeng,6,*DongfangWang,1,*andZeminZhang1,4,8,*
1BiomedicalPioneeringInnovationCenter(BIOPIC),AcademyforAdvancedInterdisciplinaryStudies,SchoolofLifeSciences,Peking
University,Beijing100871,China
2ChangpingLaboratory,Beijing102206,China
3DepartmentofSurgery,BeijingShijitanHospital,CapitalMedicalUniversity,Beijing100038,China
4InstituteofCancerResearch,ShenzhenBayLaboratory,Shenzhen518132,China
5NinthSchoolofClinicalMedicine,PekingUniversity,Beijing100038,China
6TheCASKeyLaboratoryofInnateImmunityandChronicDisease,SchoolofBasicMedicalSciences,DivisionofLifeSciencesandMedicine,
UniversityofScienceandTechnologyofChina,Hefei230027,China
7Theseauthorscontributedequally
8Leadcontact
*Correspondence:zhuln@pku.edu.cn(L.Z.),huipeng@ustc.edu.cn(H.P.),wangdf19@pku.edu.cn(D.W.),zemin@pku.edu.cn(Z.Z.)
https://doi.org/10.1016/j.cell.2023.07.034
SUMMARY
Naturalkiller(NK)cellsplayindispensablerolesininnateimmuneresponsesagainsttumorprogression.To
depicttheirphenotypicandfunctionaldiversitiesinthetumormicroenvironment,weperformintegrativesin-
gle-cellRNAsequencinganalysesonNKcellsfrom716patientswithcancer,covering24cancertypes.We
observedheterogeneityinNKcellcompositioninatumor-type-specificmanner.Notably,wehaveidentified
agroupoftumor-associatedNKcellsthatareenrichedintumors,showimpairedanti-tumorfunctions,and
areassociatedwithunfavorableprognosisandresistancetoimmunotherapy.Specificmyeloidcellsubpop-
ulations,inparticularLAMP3+dendriticcells,appeartomediatetheregulationofNKcellanti-tumorimmu-
nity.OurstudyprovidesinsightsintoNK-cell-basedcancerimmunityandhighlightspotentialclinicalutilities
ofNKcellsubsetsastherapeutictargets.
INTRODUCTION killing of target cells by secreting perforin and granzymes,11
whereastheCD56brightCD16loNKcellpopulationexhibitsimmu-
Although T cell-centric immunotherapies have achieved indis- noregulatory and cytokine-producing capacity.12 Recently,
putable clinical successes, the limited number of patients single-cell RNA sequencing (scRNA-seq) technologies have
achieving durable response presses for complementary thera- facilitated the characterization of the heterogeneity of tumor-
peutic strategies.1 Natural killer (NK) cells, as one important infiltratingimmunecells,providinggreatopportunitiestoeluci-
componentinthetumormicroenvironment(TME),areinvolved datethespectrumoftumor-infiltratingNKcellsubpopulations.13
inmultipleprocessesoftumorcontrol,suchasdirectcellkilling For example, we have identified a CD160+HSPA1A+ liver-resi-
and secretion of proinflammatory cytokines.2,3 A plethora of dentNKcellsubsetspecificallyenrichedinhepatocellularcarci-
strategies, characterized with promising properties including noma (HCC),14 and others have reported specialized NK cell
their safety and efficacy, have been proposed to harness NK populationsinfiltratedinmelanomawithregionalvariation.15In
cellsforcancertreatment.4Ofparticularnoteistheremarkable parallel,thedistributionandfunctionofhumanNKcellpopula-
clinical success achieved by chimeric antigen receptor (CAR)- tionshavebeeninvestigatedinhealthytissuesandblood.16–18
NKcelltherapiesinlymphoma,myeloma,andleukemia.5,6How- However, for tumor-infiltrating NK cells, the scale of most
ever,NK-cell-basedtherapiesarehinderedinsolidtumorspartly scRNA-seq analyses is limited, and it is still unclear to what
due to the incomplete understanding of tumor-infiltrating NK extent they acquire heterogeneous phenotypes in malignant
cells,especiallytheirinfiltrationtotumor,phenotypicheteroge- conditions.19–21
neities,anddysregulationwithintheTME.7,8 Compared with CD8+ T cells, NK cells serve as alternative
Inhumans,NKcellscanbesubdividedintotwomajorgroups, sourcesofcytotoxicactivitiesandcombattumorcellswithlow
CD56dimCD16hi and CD56brightCD16lo, based on the expres- mutationloadandaberrantexpressionofmajorhistocompatibil-
sion levels of CD56 (NCAM1) and CD16 (FCGR3A).9,10 The itycomplex(MHC)classI.22,23Althoughthedysfunctionalstate
CD56dimCD16hiNKcellpopulationpredominantlymediatesthe ofCD8+Tcellsiswell-characterizedwithreducedcytotoxicity
Cell186,4235–4251,September14,2023ª2023TheAuthor(s).PublishedbyElsevierInc. 4235
ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).
ll
OPENACCESS Resource
A B
C D
E
F
G
(legendonnextpage)
4236 Cell186,4235–4251,September14,2023
ll
Resource OPENACCESS
andhighexpressionofmultipleinhibitoryreceptors,24theNKcell approximately7,000NKcellsfromhumanbloodandspleen,17
dysfunction has not been studied in detail. Previously, NK cell ourdatascalehasexpanded>20-fold,representingmostmajor
hypofunctionhasbeenreportedinHCC,buttheimmunoregula- cancertypesandmultipletissues.
torymechanismshavenotbeenanalyzed,25,26andwhetherthis To unbiasedly define the pan-cancer population structure
phenomenonexistsinothercancertypesisnotclear.Inaddition, of NK cells, we integrated scRNA-seq data with minimal
althoughtheinhibitoryrolesofTIGITandTIM3havebeenestab- batcheffectsamongdatasetsandperformedtworoundsofun-
lished in tumor-infiltrating NK cells,27,28 it is still controversial supervised clustering (Figure S1E; STAR Methods). The first-
whetherotherimmunecheckpoints,suchasPD-1andCTLA4, round analysis pertained to distinguishing two well-character-
play the same role or are even expressed in those cells.28,29 ized major cell types, CD56brightCD16lo and CD56dimCD16hi,
Furthermore,NKcellsaresensitivetoimmunosuppressivefac- based on the high expression of canonical cell markers,
tors of the TME, which may contribute to their dysfunctional NCAM1 and FCGR3A, which corresponded to the previously
phenotype,4 but how distinct regulatory processes influence reported ‘‘NK_1’’ and ‘‘NK_2’’ populations,17 respectively. The
the function and abundance of NK cells within the TME of CD56brightCD16lo compartment can be further subdivided into
differentcancertypesremainsunclear.Together,thesepromp- 5 subsets, whereas 9 CD56dimCD16hi subsets were identified
tedustoconductadeepinvestigationofNKcellstoelucidate during the second-round clustering (Figures 1C and 1D). We
theirheterogeneityanddysfunctionatthepan-cancerlevel. didnotobservenotabledifferencesintheexpressionofKLRF1
Here,wecollectedabroadspectrumofpublishedandnewly in either of the two major populations across cancer types or
generated scRNA-seq data to construct a comprehensive tu- differentsubsets(FiguresS1FandS1G).Notably,previouslyre-
mor-infiltratinghumanNKcellatlasandexploredtheheteroge- portedinnatelymphoidcell(ILC)signaturegeneswerehardlyex-
neityofNKcellsacrosscancertypesandtissues.Weuncovered pressedintheseNKcellsubsets,30furthersuggestingthepurity
thetumor-infiltratingNKcellstatetransitionsandhighlightedthe ofourdata(FigureS1H).Thesesubsetswereallcharacterizedby
components of the TME that presumably led to the NK cell thehighexpressionofdistinctsignaturegeneswithineachmajor
dysfunction. These data will serve as a rich resource for population(FiguresS2AandS2B;TableS2).Asexpected,pre-
advancingtheunderstandingoftheglobalpropertiesofNKcells viously described subsets were readily identified in our atlas,
inmajorcancertypesandprovidevaluableinsightsintoNK-cell- such as CD56brightCD16lo c5-CREM with high expression of
basedimmunotherapydevelopment. CREM31(FigureS2B).CD56dimCD16hic8-KLRC2NKcellswith
high expression of KLRC2 (NKG2C) were regarded adaptive
RESULTS NKcells.32,33Ouratlasadditionallyuncoveredseveralunderap-
preciated NK cell subsets with unique transcriptional pheno-
Constructionofahumanpan-cancerNKcelllandscape types. For example, CD56dimCD16hi c5-MKI67 was distin-
atsingle-cellresolution guishedbyhighexpressionofproliferationmarkerslikeMKI67
Toconstructacomprehensivepan-cancersingle-celltranscrip- and STMN1, and CD56dimCD16hi c6-DNAJB1 specifically ex-
tome atlas for tumor-infiltrating NK cells, we first compiled pressed genes related to stress response (Figure S2A). Our
scRNA-seq data from both our newly generated dataset with atlasalsocapturedalowfractionofCD56brightCD16hiNKcells
47 patients diagnosed with one of the 8 cancer types and 70 in almost all cancer types, simultaneously expressing high
additional published datasets (Table S1). These data covered levels of NCAM1 and FCGR3A (Figures S1I and S2D).
24 cancer types, including 1,223 samples from 716 patients CD56brightCD16hi NK cells displayed intermediate features
across the tumor, adjacent non-tumor tissue, peripheral between CD56brightCD16lo and CD56dimCD16hi NK cells (Fig-
blood,andothertissuessuchaslymphnodes,and60healthy ureS2E),potentiallyrepresentingdevelopmentalintermediates
controls(Figures1A,1B,S1A,andS1B).Afterstringentquality in analogy to mouse CD27+CD11b+ NK cells, which have also
control and a combinative strategy of computational gating been thought to be a transient maturation stage in mice yet
(CD3(cid:1)CD56+/KLRF1+)andunsupervisedclustering(FigureS1C; barelydetectablebyscRNA-seq.17Wenextexaminedthetissue
STARMethods),weobtainedacollectionof160,011high-quality distribution of all subsets, with distinct tissue enrichment pat-
NKcellsincluding11,963newlygeneratedNKcellsinthisstudy. ternsobserved,indicatingthatourintegrativeanalysescanpre-
Notably,itisessentialandchallengingtobuildsuchalarge-scale servetheheterogeneityofdifferenttissues(Figures1E,1F,and
humanNKcellatlas,giventhatwithinthetumortissue,NKcells S2C). To further corroborate the stability of the clustering, NK
arerelativelyrareamongCD45+cells(FigureS1D),andtheirhet- cells from blood, tumor, and adjacent non-tumor tissues were
erogeneityisstillpoorlyunderstood.Comparedwiththeprevi- re-clusteredseparately,withhighlyconsistentresultsrevealed
oussingle-celltranscriptomeatlasofNKcellsconstructedwith (Figure S3F). Finally, leveraging the Ratio of Global Unshifted
Figure1. Pan-cancersingle-cellatlasofNKcellsandtheircharacteristics
(A)Cancertypesinvolvedinthepan-cancerNKcellanalysis.*,cancertypeswithnewlygenerateddata.
(B)Thenumberofpatientsacrosscancertypes.Theyaxisisscaledbyasquareroottransformation.
(CandD)Uniformmanifoldapproximationandprojection(UMAP)visualizationsof(C)CD56brightCD16loand(D)CD56dimCD16hiNKcells.
(EandF)Compositionsof(E)CD56dimCD16hiand(F)CD56brightCD16loNKcellsubsetsacrosstissues.Kruskal-Wallistest.
(G)TheexpressionpatternoffunctionalgenesinNKcells.ScorerepresentstheAUCellindexofsignaturegenes(STARMethods).Eachdashedlineindicatesthe
medianofthecorrespondingscore.
SeealsoFiguresS1,S2,andS7andTablesS1,S2,andS7.
Cell186,4235–4251,September14,2023 4237
ll
OPENACCESS Resource
A D
B
C
E
(legendonnextpage)
4238 Cell186,4235–4251,September14,2023
ll
Resource OPENACCESS
Entropy (ROGUE) index that can measure the cell cluster pu- althoughnotspecifically, andLAG3andTIGITwere highlyex-
rity,34weillustratedthatallthesepopulationswererobustacross pressedinc8-KLRC2.Notably,comparedwithothertissue-en-
variouscancertypes(FigureS1J). riched CD56dimCD16hi subsets (c4-NFKBIA, c5-MKI67, and
NK cell subsets were involved in different developmental c7-NR4A3), c6-DNAJB1 NK cells showed the highest stress
stagesasrevealedbytheirexpressionofcommonlineage-spe- scoreandtheweakestcytotoxicity,indicatingtheirdramatically
cific genes. Cells from both the tumor-enriched CD56bright differenttranscriptionalandfunctionalphenotypes(Figures1G
CD16lo c4-IL-7R and the blood-enriched c2-IL-7R-RGS1lo, andS2F).Takentogether,weprovideadetailedtranscriptome
highly expressing signature of NK cell precursors including profile of NK cells at a fine-grained subset resolution. Rather
KIT and IL7R,16,19,20 were mapped at the early developmental thananalyzingNKcellsasasinglepopulation,wedissectsub-
stage. By contrast, other immature CD56brightCD16lo subsets set-specificmolecularpropertiesofNKcellsandrevealtheirun-
exhibited a progressive reduction of the precursor signature derappreciatedheterogeneities.
and substantial gain of CD160 expression. The more mature
CD56dimCD16hi subsets, especially c6-DNAJB1 and c7- TissueheterogeneityofNKcellsacrosscancertypes
NR4A3,exhibitedconcomitantupregulationofthekillerimmu- We next assessed the preference of tumor-infiltrating NK cell
noglobulin-like receptor (KIR) family in addition to FCGR3A population among different cancer types, observing clear dis-
and B3GAT1 (CD57) (Figure S2E). NK cell subsets in varied crepancies(Figure2A;STARMethods).Forexample,theimma-
developmental states were concurrent in tumors, indicating ture CD56brightCD16lo NK cells were largely predominant in
thatNKcellmigrationtothetumormaybedecoupledwithNK nasopharyngealcancerandbasalcellcarcinoma,whereasthe
cellmaturation. matureCD56dimCD16hiNKcellsoccupiedrenalcarcinomaand
Wefurtherinspectedthegeneexpressionsignaturetodeci- lung cancer, consistent with previous reports38–42. Others,
pher the functional divergence between different populations suchascolorectalcancerandHCC,showednoobviouspropen-
(Figures 1G and S2F). CD56dimCD16hi NK cells exhibited high sity(Figures2A,S3A,andS3B).Toexaminewhethertheafore-
expression of cytotoxic effector genes including perforin mentioned tendency could be explained by the organ contex-
(PRF1) and most granzyme (GZMB, GZMA, and GZMH) ture, we analyzed the intrinsic composition of major NK cell
except GZMK, which was instead exclusively expressed in types in adjacent non-tumor tissues and their corresponding
CD56brightCD16lo NK cells.35 CD56brightCD16lo NK cells ex- changes in tumors. In certain cancer types such as colorectal
pressedvariouscytokinegenessuchasIL18.Wealsoobserved cancer, the NK cell composition of tumor tissues resembled
thatbothCD56brightCD16loc2andc4simultaneouslyexpressed thatofadjacentnon-tumortissues(FigureS3C).Asforcancer
IL18anditsreceptorIL18R1,implyingapotentiallycrucialroleof types including lung cancer and renal carcinoma, despite the
IL-18-dependentautocrinepathwayinthesesubsets.Strikingly, conservationofmajorNKcelltypesbetweentumorandadjacent
CD56dimCD16hi NK cell subsets could also exhibit specific non-tumortissues,theproportionsofCD56dimCD16hiNKcells
expressionofcertaincytokines,butwithadistinctpatternfrom significantly decreased (Figure 2B). Intriguingly, the dominant
those CD56brightCD16lo subsets. In particular, the CD56dim NK cell population in breast cancer and esophageal cancer
CD16hisubsetc4-NFKBIAexhibitedarelativelyhighinflamma- was reversed compared with their adjacent non-tumor tissues
toryscoreamongallNKcellsubsets,predominantlyexpressing (Figure2C).Theseobservationssuggestedthattheintrinsicor-
CCL3, CCL4, and CCL4L2, indicating their ability to recruit gan properties and malignancy-associated factors have com-
otherimmunecellssuchasTcells.36Recentstudieshaveasso- poundedeffectsonshapingthecontentofNKcellpopulations.
ciated the recruitment of type 1 conventional dendritic cells We further explored the cancer-type specificity for NK cells
(cDC1s) into tumor with NK cells by secreting XCL1, XCL2, fromthesubsetperspectiveandperformedunsupervisedclus-
and CCL5.37 Our results identified various NK cell subsets teringtostratifytheanalyzedcancertypesbyNKcellsubsetpro-
involved in the cDC1 recruitment through cell-type-specific portions. NK cell subsets such as c2-CX3CR1 showed strong
complementary strategies. CD56brightCD16lo c2 and c4 ex- preferenceinpancreaticcancer,breastcancer,andmelanoma.
pressed primary levels of XCL1 and XCL2, whereas another Highvariabilitieswereobservedacrosscancertypesforcertain
cDC1chemoattractantgeneCCL5waspreferentiallyproduced subsets. For example, c4-NFKBIA and c7-NR4A3 showed
by both CD56brightCD16lo (c1-GZMH and c3-CCL3) and dramatically decreased median frequencies from head and
CD56dimCD16hi(c1-IL-32andc8-KLRC2)NKcells.Additionally, necksquamouscellcarcinomaandthyroidcarcinomatoesoph-
we depicted the profile of activating and inhibitory receptors, agealcancerandnasopharyngealcancer(Figure2D).Although
observing clear variations across NK cell subsets (Fig- clear variations were observed, cancer types including uterine
ureS2G).Forexample,KLRC1wasexpressedatahigherlevel corpus endometrial carcinoma, basal cell carcinoma, and
in CD56brightCD16lo NK cells than CD56dimCD16hi NK cells, esophageal cancer were clustered together, all with abundant
Figure2. Heterogeneityoftumor-infiltratingNKcellsacrosscancertypes
(A)RelativeratiosofCD56dimCD16hiandCD56brightCD16loNKcellsinmultiplecancertypes.
(BandC)BoxplotscomparingtheproportionsoftwomajorNKpopulationsdividedbythetotalNKcellnumberbetweentumorandadjacentnon-tumortissues,
respectively.Two-sidedunpairedWilcoxontest.
(D)BoxplotsshowingthefrequenciesofselectedNKcellsubsetsintumors.Foreachsubset,onlythecancertypeswithtumorsamples>3areshown.
(E)HeatmapsshowingscoresofinhibitoryandactivatingreceptorsinNKcellsubsets(STARMethods).
SeealsoFigureS3.
Cell186,4235–4251,September14,2023 4239
ll
OPENACCESS Resource
(legendonnextpage)
4240 Cell186,4235–4251,September14,2023
ll
Resource OPENACCESS
CD56brightCD16hic5-CREMandminimalc4-IL-7RNKcells(Fig- whereas the RGS1/CD69 combination could further increase
ureS3D).OfparticularnoteisthattherareCD56brightCD16hiNK the positive detection rate in tissues (Figures 3F and S4E).
cell subset with the hypomaturation stage as aforementioned Furthermore, the RGS1/CD69 combination could achieve a
wasabundantinmelanomaandleukemia,especiallyintheacute higherareaunderthecurve(AUC)valuethaneitheraloneindis-
myeloidleukemia(AML)subtype(Figures2DandS3E).Suchhy- tinguishingbloodandnon-bloodNKcells(FigureS4D).Notably,
pomaturation stage of NK cells has been associated with the RGS1waswidelyexpressedacrossanalyzedpatientsandcan-
reductionofoverallsurvivalandrelapse-freesurvivalofpatients certypes(Figures3G,3H,andS4F).
withAML.43,44ComparedwithotherNKcellpopulations,these In summary,these characteristics imply the potential role of
CD56brightCD16hi cells exhibited distinctive phenotypic and RGS1 alone, or its combination with CD69, to be a superior
functional shifts in terms of their extremely low activating and markerfortissue-infiltratingNKcellsatthetranscriptomelevel.
inhibitory receptor scores (Figure 2E). Current NK cell-based We speculate that the expression of RGS1 may attenuate the
therapies are focused on augmenting the activation and signaling activity of G-proteins,48 leading to the weakness of
longevityofNKcellsbutgenerally disregardtheheterogeneity NKcellchemotacticmigrationabilityandpromotingNKcellres-
among cancer types and the suppressive impact of the TME idency. Further studies are required to demonstrate the func-
on NK cell cytotoxic functions, which should be considered in tionalmechanismofRGS1inNKcells.
futuretherapeuticstrategies.
Tumor-associatedNKcellprogramsandtheir
RGS1isahallmarkoftissue-infiltratingNKcells characteristics
As aforementioned, NK cell components significantly altered Wenext soughtto elucidate the specific characteristics ofNK
fromthebloodtotissues.Likewise,widespreadtranscriptional cells in tumors. Aside from the tumor-specific enrichment of
changesweredetectedbetweentissue-infiltratingNKcellsand certain subsets as described above, we found that compared
their blood counterparts (Figures 3A and 3B; Table S3). Prior withtheadjacentnon-tumortissue,intumors,thecytokinepro-
studies have identified several markers of tissue-resident NK ductionofCD56brightCD16loc3-CCL3NKcellswaslowerasindi-
cells,suchasCD69,CD103,CXCR6,andCD49a.45–47However, catedbythediminishedexpressionofCCL3andCCL4,andthe
wefoundthatITGA1(CD49a),ITGAE(CD103),andCXCR6were expressionofXCL1andXCL2inc5-CREMNKcellsdecreasedin
poorlydetectedatthesingle-celltranscriptomelevel,andCD69 mostcancertypes(FiguresS5AandS5B;TableS5),implicating
wasexpressedwidelyinNKcellsincludingthosefromtheblood theirfunctionalshiftsintumors.Wethenidentifiedactivatedreg-
(Figure 3E). Additionally, preferential expression of these ulons for both tumor-infiltrating CD56brightCD16lo and CD56dim
markersinNKcellpopulationsofparticulartissueshasbeenre- CD16hi NK cell subsets using SCENIC.49 Importantly, the tu-
ported.16 These motivated us to discover robust NK cell resi- mor-enrichedc6-DNAJB1subsetexhibitedmuchhigherexpres-
dencymarkersfromthepan-cancerperspectiveinanunbiased sionoftranscriptionfactorssuchasKLF6andEGR3,whichare
manner. associated with the inhibition of cytotoxicity functions50–52
We selected differentially expressed genes between blood (FigureS5C).
andtissueandfurtherassessedtheirsensitivityandspecificity Using RNA velocity,53,54 we decoded the transcriptional dy-
to distinguish the tissue origin of NK cells. Consequently, namics of NK cells, observing a clear directional flow from
RGS1 (regulator of G protein signaling 1) was pronouncedly blood-enriched subsets to tumor-infiltrating populations both
recognized,whichwasexclusivelyexpressedinNKcellswithin in CD56brightCD16lo and CD56dimCD16hi NK cells (Figures 4A
tumorandadjacentnon-tumortissues,butbarelydetectablein and S5D). Correspondingly, the expression of RGS1 was
the blood (Figures 3C and 3D). In addition, the expression of elevated along the velocity flow (Figure S5E). We found that
RGS1 was opposite to migration signals including KLF2 and CD56dimCD16hi c6-DNAJB1 NK cells were located at the end
SELL(Figure3E).Compared withtheaforementioned conven- ofthevelocity,therebyinferredastheterminalstate(Figure4A).
tional tissue-resident markers, RGS1 showed much higher Notably,CD56dimCD16hiNKcellsfromtheadjacentnon-tumor
sensitivity and specificity (Figures S4A–S4D). We next directly tissueweremainlyobservedintheuniformmanifoldapproxima-
compared the expression patterns of RGS1 with ITGAE and tionandprojection(UMAP)areaenrichedwithc7-NR4A3cells;
CD69 as well as their combinations in the blood, observing by contrast, tumor-derived CD56dimCD16hi NK cells were pre-
that RGS1 alone had the lowest detection rate in the blood, dominant in the UMAP area enriched with c6-DNAJB1 cells
Figure3. IdentificationofRGS1asakeytissue-infiltratingmarkerforNKcells
(AandB)Heatmapshowingdifferentiallyexpressedgenesfor(A)CD56brightCD16loand(B)CD56dimCD16hiNKcellsbetweenbloodandnon-bloodtissue.Rows
representsignaturegenesandcolumnsrepresentdifferentpatients.
(CandD)UMAPplotsshowingtheRGS1expressionanditstissuedistributionin(C)CD56brightCD16loand(D)CD56dimCD16hiNKcells.
(E)Theexpressionpatternoftissue-residentandmigrationsignalsofCD56brightCD16loandCD56dimCD16hiNKcellsinvariedtissues.Bluelinesmarkthetissue-
residentsignalsandredlinesmarkthemigrationsignals.
(F)TheperformanceofCD69,ITGAE,andRGS1aswellastheircombinationsindistinguishingtissue-derivedNKcellsbasedoninsilicofluorescence-activated
cellsorting(FACS).ReddotsdenotetheNKcellsderivedfromblood,andgraydotsdenotetissue-derivedNKcells.Dashedlinesindicatethepredictedboundary
ofbloodandnon-bloodNKcellsbasedontheexpressionlevel.
(G)ViolinplotsshowingRGS1expressionamongtissuesatthepan-cancerlevel.Two-sidedunpairedWilcoxontest.
(H)HeatmapshowingthemeanexpressionofRGS1withintheblood,tumor,andadjacentnon-tumortissuesacrossanalyzedcancertypes.
SeealsoFigureS4andTableS3.
Cell186,4235–4251,September14,2023 4241
ll
OPENACCESS Resource
Figure4. Characteristicsoftumor-associatedNKcells
(A)RNAvelocitiesoverlaidontheUMAPofCD56dimCD16hiNKcells(STARMethods).ArrowsshowtheRNAvelocityfield.DotsarecoloredbyCD56dimCD16hiNK
cellsubsets.Onlyournewlygenerateddataareused.
(B)DensityplotsofCD56dimCD16hiNKcellsfromthetumorandadjacentnon-tumortissue.Dashedlinesrepresenttheenrichedareaofc6-DNAJB1cells.
(C)VolcanoplotshowingdifferentiallyexpressedgenesforCD56dimCD16hiNKcellsbetweentumorandadjacentnon-tumortissues.Geneswithanadjusted
pvalue<0.05aresignificant.Two-sidedunpairedWilcoxontest.
(D)RepresentativeexampleofanHCCtumorstainedbymultipleximmunofluorescencetoshowTaNKcells(arrows).Thescalebarrepresents20mm.
(E)ThepercentageofCD56dimCD16hiHSP40+NKcellsamongCD56dimCD16hiNKcellsintumorandadjacentnon-tumorregionsoflivercancerpatientsusing
flowcytometry.*p<0.05,**p<0.01,***p<0.001,pairedttest.
(F)Thegeneexpressionsplottedalongthepseudotime(STARMethods).
(G)BoxplotsshowingsignaturescoresamongCD56dimCD16hic4(cid:1)NFKBIA,c6-DNAJB1,andc7-NR4A3cells.Two-sidedunpairedWilcoxontest.
(H)RepresentativeexampleofanHCCtumorstainedbymultipleximmunofluorescencetoshowtheexpressionofgranzymeBinHSP40+(whitearrows)and
HSP40(cid:1)NKcells(redarrows).Thescalebarrepresents20mm.
(IandJ)Comparisonof(I)cytotoxicgranulesand(J)inhibitorreceptorsforCD56dimCD16hiHSP40+andHSP40(cid:1)NKcellsinthetumorregionoflivercancer
patientsusingflowcytometry.*p<0.05,**p<0.01,***p<0.001,pairedttest.
SeealsoFigureS5andTablesS4andS5.
(Figure 4B). Consistently, markers of tumor-enriched c6- ThepresenceofTaNKcellsincancerswasfurthersubstanti-
DNAJB1NKcellssuchasDNAJB1andHSPA1Awerehighlyex- ated by multiplex immunofluorescence staining (Figures 4D
pressedinthetumor-infiltratingCD56dimCD16hiNKcellpopula- andS5G).WealsovalidatedthetumorenrichmentofTaNKcells
tion (Figure 4C). In addition, we observed similar expression (CD56dimCD16hiHSP40+)invivousingflowcytometry.Inonein-
levelsofmitochondrialgenesinc6-DNAJB1andc7-NR4A3NK trahepatic cholangiocarcinoma and six HCC samples, TaNK
cells, indicating that the stress phenotype of c6-DNAJB1 NK cells were identified, and their proportion in tumor-infiltrating
cellswasunrelatedtocellquality(FigureS5F).Sincec6-DNAJB1 CD56dimCD16hi NK cells was higher than that in the matched
cellswerespecificallyenrichedintumors,wetermedthispopu- adjacent liver tissue, consistent with our scRNA-seq data
lationastumor-associatedNK(TaNK)cells. (Figures4EandS5H;TableS4).
4242 Cell186,4235–4251,September14,2023
ll
Resource OPENACCESS
Wethenusedthepseudotimeinferenceanalysis55toinvesti- quency indicated an unfavorable prognosis of cancer patients
gate the dynamic of CD56dimCD16hi NK cells and found that (Figures S5M and S5N). We additionally examined whether
TaNKcellsincreasinglyappearedalongtheinferredpseudotime TaNKcellswerelinkedwithICBtreatmentresponsebyanalyzing
of CD56dimCD16hi NK cells and were enriched in the terminal scRNA-seqdataofpretreatmenttumorsfrompreviousICBther-
stage (Figure S5I), consistent with results of the RNA velocity apy studies of breast cancer and melanoma15,59 (Figure 5F).
analysis. To examine the emerging characteristics of TaNK Strikingly, a higher proportion of TaNK cells was observed in
cells, we fitted the gene expression profile to the pseudotime nonresponsive patients than responsive ones for both cancer
(STARMethods).Interestingly,CD56dimCD16hiNKcellsshowed types.Furtherexploitingpublishedbulkdatafromawidevariety
decreasedcytotoxicityandelevatedexpressionofinhibitoryre- ofcancersincludingmelanoma,60lungcancer,61andmetastatic
ceptorsandstressgenesalongthetransitionprocess(Figure4F). urothelialcarcinoma,62wevalidatedthatnonresponsivepatients
Ofnote,theterminalTaNKcellshadthelowestcytotoxicityand exhibited stronger TaNK cell signals than responsive patients
highest stress scores among all tumor-infiltrating CD56dim (Figure5G).
CD16hi NK cell subsets. By contrast, the corresponding c7- We speculate that the long-term infiltration could confer the
NR4A3enrichedinadjacentnon-tumortissueswashighlycyto- functionalstateofTaNKcellsintumors,leadingtotheirineffec-
toxic (Figure 4G). By performing the multiplex immunofluores- tive killing of malignant cells. The enrichment of TaNK cells is
cence staining on several cancer types, we observed that linked to impaired immune responses against the tumor as
TaNK cells exhibited a lower level of GZMB (Figures 4H, S5J, well as hyposensitivity to current ICB therapy. Our findings
andS5K).Furtherconfirmedbyflowcytometryanalysesofliver revealthepotentialroleofTaNKcellsintumorsandprovidea
cancer patients, TaNK cells had lower expression of cytotoxic reference to facilitate the rational design of NK cell-based
granules (granzyme B and perforin) and higher expression of immunotherapies.
inhibitory receptors including CD158a (KIR2DL1) and CD158e
(KIR3DL1)comparedwiththeCD56dimCD16hiHSP40(cid:1)NKcells PotentialmediatorsintheTMEshapingtumor-
atthetumorsite(Figures4Iand4J).Theseresultssuggestthat infiltratingNKcellfunctions
TaNKcellsmaybeassociatedwithdysfunctionalstatus.Further- TogaininsightsintotheregulatoryprogramsofNKcellsinthe
more,wealsoobservedthedifferentialdynamictendencyofthe TME,weutilizedCellPhoneDB63toprobepotentialcell-cellinter-
NR4Anuclearreceptorfamilyasthepseudotimeincreases(Fig- actionsbetweenNKandotherCD45+immunecells,includingT
ure4F).c7-NR4A3NKcellsexpressedhighlevelsofNR4A2and andmyeloidcells13,64(STARMethods).ComparedwithTcells,
NR4A3, whereas TaNK cells highly expressed NR4A1 (Fig- most myeloid cell types except mast cells exhibited strong
ureS5L).Intriguingly,NR4A1hasbeenidentifiedasakeymedi- potential interactions with CD56dimCD16hi NK subsets (Fig-
atoroftheTcelldysfunction56andpostulatedtocontributetore- ure6A).OfparticularinterestisthatTaNKcellswerepredicted
strictingtheCARTcellfunctioninsolidtumors.57Insummary,our toregulatemultiplemyeloidcelltypesviaANXA1,aproteinasso-
data suggested that TaNK cells in tumors might be terminally ciated with immunosuppression and induction of macrophage
dysfunctionalandpotentiallyplaycriticalrolesintheTME. reprogrammingduringinflammatoryresponses65,66(Figure6B;
Table S6). This implied that dysfunctional NK cells might have
TheassociationofTaNKcellswithunfavorable thepotentialtosuppressproinflammatorymacrophagesinthe
prognosisandimmunotherapyresistance TME.TofurtherclarifytheroleofNKcell-derivedANXA1inmac-
Since NK cells and CD8+ T cells exhibit extensive phenotypic rophages,weperformedmultipleximmunofluorescencestaining
and functional similarities,4,19 we next examined whether im- oftumorsamplesfromlungcancerandlivercancerandidenti-
mune checkpoint blockade (ICB) therapies targeting CD8+ fiedapopulationofANXA1+NKcells(FigureS6A).Macrophages
TcellswouldalsoimpactNKcells.Withintumor-infiltratingNK closetoANXA1+NKcellswerefoundtoexhibitlowerexpression
cellsandCD8+Tcells,TaNKcellsandexhaustedTcells(Tex) levelsofactivationmarkerCD86(Figures6C,6D,S6B,andS6C)
exhibitedaprominentstressstate(Figure5A),suggestingtheir andhigheranti-inflammatorymarkertransforminggrowthfactor
involvement in the tumor immune response. Both highly ex- b(TGF-b)thanthosefarfromANXA1+NKcells(Figures6E,6F,
pressed a series of inhibitory receptor molecules; however, S6D,andS6E).
they held divergent expression profiles over various immune Notably,amongdendriticcell(DC)subsets,LAMP3+DCs,the
modulatory genes. Conventional immune checkpoint genes mature cDCs recently characterized (also called mregDC),14,67
such as PDCD1 and CTLA4 were barely expressed on TaNK showed the strongest interaction potential with CD56dimCD16hi
cells (Figure 5A), implying that they are not direct targets of NKcells(Figure6A).Themultipleximmunofluorescenceanalyses
anti-PD-1/CTLA-4therapies.Thus,TaNKcellsmayplaydifferent showed that LAMP3+ DCs were co-localized with NK cells
rolesfromTexcellsintheTMEandcurrentICBtreatments. (Figures 6J and S6L). In addition, interactions between them
WeobservedaremarkablediscrepancyintheTaNKcellabun- werepredictedtobemediatedviatheIL-15-IL-15receptorand
danceacrosscancertypes(Figure5B),andtumorstagesmade NECTIN2-TIGIT interaction axes (Figure 6B). Importantly,
marginal impacts on the proportion of TaNK cells (Figure 5C). LAMP3+ DCs expressed the highest level of IL15, PVRL2
Notably, in The Cancer Genome Atlas (TCGA) datasets, the (NECTIN2),andPVRamongimmunepopulationsatthetranscrip-
highTaNKcellsignalintumorswasassociatedwithpoorsurvival tomelevel(Figures6GandS6F).ThehighexpressionofIL-15in
formostcancertypes(Figures5Dand5E).Wefurtherapplieda LAMP3+ DCs was also demonstrated by flow cytometry
deep learning-based model to perform deconvolution and cell (Figures6H,S6G,andS6H;TableS4).IL-15hasbeenidentified
composition analyses,58 finding that the high TaNK cell fre- asahomeostasis-relatedcytokineforthelongevitymaintenance
Cell186,4235–4251,September14,2023 4243
ll
OPENACCESS Resource
A D
E
B
C F G
Figure5. TherelationshipbetweenTaNKcellsandclinicaloutcomes
(A)ExpressionpatternsofselectedgenesinspecificNKcellandTcellsubsetsfromtumors.
(B)ProportionsofCD56dimCD16hic6-DNAJB1NKcellsinallNKcellsacrosscancertypes.Kruskal-Wallistest.
(C)BoxplotscomparingtheproportionofTaNKcellsinallNKcellsamongdifferenttumorstages.Two-sidedunpairedWilcoxontest.
(D)ForestplotshowingtheeffectofTaNKcellsonoverallsurvival.Theyaxisisscaledbyalog10transformation.*p<0.05,**p<0.01,***p<0.001.Pvaluesare
adjustedbyBenjamini-Hochberg.
(E)Kaplan-MeierplotsshowingtheassociationofthesignatureactivityofTaNKcellsintumorswithprognosis(STARMethods).+,censoredobservations;log-
ranktest.
(F)BoxplotscomparingproportionsofTaNKcellsinCD56dimCD16hiNKcellsbetweennon-responders(NRs)andresponders(Rs)inICBtherapydatasets(STAR
Methods).
(G)BoxplotsshowingthatNRexhibitedahigherTaNKcellsignalthanRinbulkRNA-seqdatasets(STARMethods).
SeealsoFigureS5.
ofNKcellsandutilizedforNKcellinfusionandinvitropropaga- gested the abnormal regulation of CD56dimCD16hi NK cells by
tion.4,68 By contrast, TIGIT contributes to suppressing NK cell- LAMP3+DCsintheTME.
mediated immune responses as an inhibitory receptor.28,69,70
Furthermore,inTCGAdatasets,theabundanceofLAMP3+DCs DistincttranscriptomepatternsofperipheralbloodNK
was correlated with CD56dimCD16hi NK cells (Figures 6I, S6I, cellsubsets
and S6J). Wenext investigated the specific regulatory process NK cells comprise a sizable proportion of the lymphoid cell
of LAMP3+ DCs in tumors and found that tumor-infiltrating compartmentintheblood,buttheirroleinthetumor-inducedpe-
LAMP3+DCsexhibitedlowerexpressionofIL15comparedwith ripheralimmunesystemisrelativelyopaque.Ouratlascontains
those in the adjacent non-tumor tissue (Figure S6K), indicating ninescRNAdatasetsofblood-derivedNKcellsfrom35healthy
that LAMP3+ DCs might have impaired activation effects on donors (Table S7), enabling us to probe specific alterations of
CD56dimCD16hiNKcellsintheTME.Indeed,NKcellswithclose NKcellsintheperipheralbloodoftumorpatients.
physicalproximitytoLAMP3+DCsexpressedgranzymeBata We first compared the transcriptome features of circulating
lowerlevel(Figures6J,6K,andS6L).Together,ouranalysessug- NK cells from healthy donors with those from tumor patients.
4244 Cell186,4235–4251,September14,2023
ll
Resource OPENACCESS
Figure6. TherelationshipofLAMP3+DCswithCD56dimCD16hiNKcellsacrosscancertypes
(A)Heatmapshowingthenumberofsignificantligand-receptorpairsforeachcluster(STARMethods).
(B)Bubbleheatmapshowingselectedligand-receptorpairsforinteractionsofCD56dimCD16hiNKandotherimmunecellclustersintumors.Dotsizeindicatesthe
pvaluegeneratedbypermutationtest,andcolorthemeanexpressionofeachligand-receptorpair.
(C–F)Representativeimagesandquantificationoffluorescenceintensityof(CandD)CD86or(EandF)TGF-bexpressiononmacrophagesadjacenttoand
distantfromANXA1+NKcellsinHCCtumors.WhitearrowsrepresentmacrophagesadjacenttoANXA1+NKcells,whereasredarrowsfarfromANXA1+NKcells.
Scalebarrepresents20mm.Dataarerepresentedasmean±SEM.Two-sidedttest.
(legendcontinuedonnextpage)
Cell186,4235–4251,September14,2023 4245
ll
OPENACCESS Resource
Circulating NK cells displayed high similarities among healthy ILCsignaturegeneswerehardlyexpressedinallidentifiedNK
donors from different datasets (Figure S7B). By contrast, for cellsubsets(FigureS1H).However,anycomputationalstrategy
circulating CD56brightCD16lo cells from tumor patients, we mayinevitablyleavecertainNKcellsout,andtheeffectsofour
observed substantial transcriptome deviations from those in strategyonNKcellsderivedfromdifferenttissuesanddevelop-
healthydonors;evenmoredramaticdifferenceswerefoundfor mental stages as well as the potential induced bias should be
circulatingCD56dimCD16hicellsinallanalyzedcancertypes(Fig- exploredfurther.
ureS7A).Notably,tumorpatientsexhibitedremarkablecompo- Basedonourhigh-dimensionalscRNA-seqdataonalarge
sitionalchangesinNKcellsubsets,andsuchpatternsappeared scale, we separately explored CD56brightCD16lo and CD56dim
tobecancer-type-specific(FigureS7C).Forexample,thefrac- CD16hi subsets, which corresponded to the previously re-
tionofcirculatingCD56brightCD16loc3-CCL3NKcellsincreased ported NK_1 and NK_2,17 respectively, and revealed that tu-
incolorectalcancer,headandnecksquamouscellcarcinoma, mor-infiltrating NK cells were structured with heterogeneous
renal carcinoma, and HCC, but not in other analyzed can- populations accompanying phenotypic variation and func-
certypes. tionaldiversity.TheseNKcellsappeartoinvolveinextensive
Next,wefocusontheCD56dimCD16hic8-KLRC2adaptiveNK anti-tumor responses such as direct killing of cancerous
cells,whichwereenrichedincertaincancertypessuchascolo- cells,secretionofproinflammatorycytokines,andrecruitment
rectalcancerandgastriccancer(FigureS7D).AdaptiveNKcells of other immune components (Figures 7A and 7B). NK cell
havebeenviewedasanattractivesourceofCARNKcells,dueto populations exhibited substantial cancer-type preferences,
their effector characteristics of augmented cytokine response which were associated with both intrinsic organ properties
and intrinsic resistance to theimmunosuppressive effects.4 Of and factors from the TME. Particularly, the reduction of
particular interest is that these cells specifically expressed CD56dimCD16hi NK cells in tumors observed for most cancer
MHC class II genes, compared with other circulating NK cells types represents a potential mechanism of tumor escaping
basedonourdata(FigureS7E).Weadditionallyexaminedfunc- from the NK cell immunosurveillance. Previously, higher NK
tionalshiftsoftheseNKcellsintumorpatientsandfoundthat cell activity has been associated with the response to trastu-
comparedwiththoseinhealthydonors,patient-derivedadaptive zumab, an anti-HER2 antibody, for breast cancer patients,71
NKcellshadsignificantlyhigherexpressionoffunctionalgenes which inspires us that the function of tumor-infiltrating NK
and MHC class IIgenes (FiguresS7F and S7H), implying their cellsmayaffecttheclinicalefficacyofantibodydrugsthrough
highly activated state in tumor patients. We further confirmed antibody-dependent cellular cytotoxicity.
the high expression of MHC class II molecules on circulating FacilitatingNKcellinfiltrationinsolidmalignancieshasbeena
NKcellsfromHCCpatientscomparedwiththosefromhealthy keyfocusofdevelopingtherapeuticNKcellproducts.Werecog-
donorsbyflowcytometry(FigureS7G).Accordingly,genesupre- nizedRGS1asakeymarkeroftissue-infiltratingNKcellsatthe
gulated in patient-derived adaptive NK cells were involved in transcriptome level (Figure 7C). Analogously, RGS1 is highly
pathwayssuchaspositiveregulationoftheimmuneeffectorpro- correlatedwithTcellfunctionandtissueresidency,72,73butthe
cess (Figure S7I). Taken together, our analyses revealed that functional effect on NK cells is still unclear and needs further
circulating NK cellswere involved in the systematic change of investigation.Itisstilldifficulttoaccuratelydiscriminatewhether
theperipheralimmuneenvironmentduringtumorprogression. RGS1marksallNKcellsenteringtissuesoronlybonafidetissue-
residentNKcells.
DISCUSSION We identified a tumor-enriched NK cell subset in potentially
dysfunctionalstates,namedTaNKcells(Figure7D).Analogous
Inthisstudy,wecollectedawidevarietyofNKcellscovering24 totheexhaustionofTcells,24,74thedysfunctionofNKcellssug-
cancer types and systematically explored the unappreciated gests the impairment of natural cytotoxicity.75,76 Notably,
complexityoftumor-infiltratingNKcells.Itisindeedchallenging although TaNK cells are not always the dominant component
tosimultaneouslyachievehighpurityandcompletenessofthe of tumor-infiltrating NK cells in all cancers, the enrichment of
assembled NK cell atlas due to the heterogeneity of datasets TaNKcellsintumorsisrobustinvariouscancersincludingthose
from different labs and the similar transcriptional phenotype dominatedbyCD56brightCD16loNKcells.Thehighabundanceof
amongNKcells,effectorTcells,andotherILCs.Ourcomputa- thesecellswasrelatedtounfavorableprognosisandimmuno-
tionalstrategycanensureapureNKcellatlaswithaminimalef- therapy resistance in multiple cancer types, implicating their
fectonthedownstreamproportioncomparisonsandotherana- rolesin clinical settings. Wespeculated thatTaNK cell enrich-
lyses.Inparticular,weconfirmedthatwell-characterizedhuman mentmayreflectoraffectthetumorimmuneresponsesinthe
(G)TheexpressionpatternsofIL15,PVR,andPVRL2inmajorimmunepopulationsbasedonscRNA-seqdata.Dotsizerepresentspercentage,andcolorthe
meanexpression.
(H)ArepresentativeplotofIL-15expressioninthetumortissueofanHCCpatient,analyzedbyflowcytometry.
(I)ScatterplotsshowingcorrelationsofCD56dimCD16hiNKcellswithLAMP3+DCsintheTCGAdataset(STARMethods).Pearsoncorrelationtest.
(J)Multipleximmunofluorescencestainingtoshowtheco-localizationofLAMP3+DCs(DC-LAMP3+)andNKcells(CD3(cid:1)CD56+).Thescalebarrepresents20mm.
(K)QuantificationofthefluorescenceintensityforgranzymeBinNKcellsneartoLAMP3+DCs(n=19)orfarfromLAMP3+DCs(n=26)from(D)usingtheHalov3.3
imageanalysisplatform(IndicaLabs).Dataarerepresentedasmean±SEM.Two-sidedunpairedWilcoxontest.
(A),(B),and(G)areplottedusingournewlygenerateddata.
SeealsoFigureS6andTablesS4andS6.
4246 Cell186,4235–4251,September14,2023
ll
Resource OPENACCESS
Figure7. SummaryofNKcellfeaturesanddynamicsinthisstudy
Sketchmapshowingthephenotypicshiftsofdifferenttumor-infiltratingNKcellsubsets
(A)CD56brightCD16loc5-CREMNKcellsdownregulatedXCL2andXCL1intumors,possiblyleadingtoattenuatedcDC1recruitment.
(B)CD56brightCD16loc3-CCL3NKcellsexhibitedreducedcytokineproductionintumors,includingCCL3andCCL4.
(C)IncontrasttocirculatingNKcells,tumor-infiltratingNKcellsconsistentlyexpressedRGS1.
(D)c6-DNAJB1NKcells,exhibitinghigherexpressionofKIRs,elevatedstressresponse,andreducedcytotoxicity,wereconsideredthepotentiallydysfunctional
stateoftumor-infiltratingCD56dimCD16hiNKcells.
(E)CellularinteractionswithLAMP3+DCsshapetumor-infiltratingCD56dimCD16hiNKcellfunctions.
TME, although those cells may be not the direct target of ICB CD56dimCD16hi c8-KLRC2 adaptive NK cell population that is
therapies. Further exploration of larger cohorts is expected to characterizedbytheupregulationofcertainproinflammatorycy-
corroboratethefunctionalrolesofTaNKcellsinbothtumorpro- tokinesandMHCclassIIgenesintheperipheralbloodoftumor
gressionandICBtreatment.Wealsoexploredthemechanismof patients. Although the mechanism underlying their phenotypic
howtheseNKcellsareaffectedintumors.Weidentifiedinternal shiftsintumorpatientsremainsunclear,apossibleexplanation
regulatorsforTaNKcells,includingNR4A1,whichhasbeenre- isthatthemalignancy-inducedreleaseofcytokinesmightresult
ported to inhibit effector T cell differentiation and play critical inaninflammatorycontextofperipheralbloodandthenactivate
roles in T cell exhaustion.56,57 External factors from other cell NKcells accompaniedbyMHCclassIImolecule expressions.
populations in the TME including myeloid-derived suppressor We expect future studies to pay more attention to the role of
cells,Tregs,andtumor-associatedmacrophagescanalsosup- adaptive NK cells in the systemic immunity and elucidate the
presstheanti-tumorfunctionofNKcells.4,77Ouranalysesand connection between circulating NK cells and intra-tumoral im-
experimentalevidencesupportmyeloidcellsascoremediators muneresponses.
of NK cells. Specifically, LAMP3+ DCs can serve as a crucial In summary, our comprehensive analyses enhance the cur-
regulatorandpotentiallyinhibitCD56dimCD16hiNKcellfunction rentunderstandingofNKcellsfromapan-cancer view,illumi-
in the TME, whereas further direct functional validation is still natinginsightsintoNKcellpopulationstructuresaswellastu-
imperative(Figure7E).Overall,ourresultsprovidecuestomain- mor-inducedlocalandsystemicNKcellresponses.Tofacilitate
taintheanti-tumoractivityofNKcellsinvivoviasearchingfor the usage of our data for the wide research community, an
cell-intrinsicandTME-associatedfactors. interactive portal (http://pan-nk.cancer-pku.cn/) has been
Emergingstudieshaveunveiledthealterationofsystemicim- developed for analyzing and visualizing our single-cell data.
munity during tumor progression.78 Our study revealed a We envision that our large-scale data can further promote the
Cell186,4235–4251,September14,2023 4247
ll
OPENACCESS Resource
application of NK cell-based immunotherapy to more cancer SUPPLEMENTALINFORMATION
patients.
Supplementalinformationcanbefoundonlineathttps://doi.org/10.1016/j.cell.
2023.07.034.
Limitationsofthestudy
Welackdetailedclinicalinformationonpatientsfrompublicda- ACKNOWLEDGMENTS
tasets. Further investigating the functional and compositional
WethankY.Zhang,Y.He,S.Cheng,Q.Zhang,C.Li,Z.Li,andX.Chenfordis-
variancesofNKcellsinspecificcontextsincludingdifferenttu-
cussions.PartoftheanalysisinthisstudywasperformedontheHighPerfor-
mor stages, metastatic positions, and expression status of manceComputingPlatformoftheCenterforLifeScience(PekingUniversity).
MHCclassIclassgenes,ischallenginginourstudy.Epigenetic This project was supported by funding from the National Natural Science
characteristicsofTaNKcellsarestillunexplored,andthefunc- Foundation of China (81988101, 31991171, 91959000, 592259205,
tionalvalidationforthesecellsislimitedduetothedifficultyof 62203019, and 92159305) and Beijing Municipal Science and Technology
Commission(Z221100007022002).
in vitro culturing. Estimations about the clinical significance of
TaNK cells are not conditioned on other possibly confounding
AUTHORCONTRIBUTIONS
immune cell types. Nevertheless, this first pan-cancer single-
cell NK cell atlas captures the complex tumor-infiltrating NK Z.Z.,D.W.,andL.Z.designedthisstudy.F.T.,J.L.,andS.Q.performeddata
cellcharacteristicsandinformsfuturedevelopmentaldirections analysis.Z.Z., L.Z.,H.P.,andZ.T. contributed totheexperimentaldesign.
ofNKcell-basedimmunotherapystrategiesthatcanbeperson- L.Q.,L.Z.,andY.B.performedtheexperiments.Y.M.,K.Y.,andJ.L.provided
alizedforthemaximalclinicalbenefit. experimentalmethods.D.L.andJ.P.providedclinicalsamples.F.T.,J.L,L.Z.,
H.P.,D.W.,andZ.Z.wrotethemanuscript,withallauthorscontributingto
providingfeedback.
STAR+METHODS
DECLARATIONOFINTERESTS
Detailedmethodsareprovidedintheonlineversionofthispaper
Z.Z.isafounderofAnalyticalBioscienceandalsoservesontheAdvisory
andincludethefollowing: BoardofCell.Allfinancialinterestsareunrelatedtothisstudy.
d KEYRESOURCESTABLE
Received:November15,2022
d RESOURCEAVAILABILITY Revised:March28,2023
B Leadcontact Accepted:July28,2023
B Materialsavailability Published:August21,2023
B Dataandcodeavailability
REFERENCES
d EXPERIMENTAL MODEL AND STUDY PARTICIPANT
DETAILS
1.Waldman,A.D.,Fritz,J.M.,andLenardo,M.J.(2020).Aguidetocancer
B Humanparticipants immunotherapy:fromTcellbasicsciencetoclinicalpractice.Nat.Rev.
d METHODDETAILS Immunol.20,651–668.https://doi.org/10.1038/s41577-020-0306-5.
B Samplecollectionandflowcytometry 2.Huntington,N.D.,Vosshenrich,C.A.J.,andDiSanto,J.P.(2007).Develop-
B Multipleximmunofluorescentstaining mentalpathwaysthatgeneratenatural-killer-celldiversityinmiceandhu-
B SinglecellRNAlibrarypreparationandsequencing mans.Nat.Rev.Immunol.7,703–714.https://doi.org/10.1038/nri2154.
B Single-cellRNA-seqdatapreprocessing 3.Freud,A.G.,andCaligiuri,M.A.(2006).Humannaturalkillercelldevelop-
B Batcheffectcorrectionandunsupervisedclustering ment. Immunol. Rev. 214, 56–72. https://doi.org/10.1111/j.1600-065X.
2006.00451.x.
B The proportion and tissue distribution of NK cell
4.Myers,J.A.,andMiller,J.S.(2021).ExploringtheNKcellplatformforcan-
subsets
cerimmunotherapy.Nat.Rev.Clin.Oncol.18,85–100.https://doi.org/10.
B Calculationofsignaturescore
1038/s41571-020-0426-7.
B Definition of cytotoxicity, inflammatory and stress
5.Li,Y.,Hermanson,D.L.,Moriarity,B.S.,andKaufman,D.S.(2018).Human
genesets
iPSC-derivednaturalkillercellsengineeredwithchimericantigenrecep-
B Definition of HLA-dependent and -independent torsenhanceanti-tumoractivity.CellStemCell23,181–192.e5.https://
receptors doi.org/10.1016/j.stem.2018.06.002.
B Hierarchicalclusteringofcancertypes 6.Zhang,L.,Meng,Y.,Feng,X.,andHan,Z.(2022).CAR-NKcellsforcancer
B Specificityandsensitivityassessment immunotherapy:frombenchtobedside.Biomark.Res.10,12.https://doi.
B RNAvelocityanalysis org/10.1186/s40364-022-00364-6.
B Pseudotimetrajectoryinference 7.Habif,G.,Crinier,A.,Andre´,P.,Vivier,E.,andNarni-Mancinelli,E.(2019).
B SCENICanalysis Targeting natural killer cells in solid tumors. Cell. Mol. Immunol. 16,
415–422.https://doi.org/10.1038/s41423-019-0224-2.
B Cell-cellinteractionanalysisbyCellPhoneDB
B Analysisofimmunotherapydatasets 8.Melaiu,O.,Lucarini,V.,Cifaldi,L.,andFruci,D.(2019).Influenceofthetu-
mormicroenvironmentonNKcellfunctioninsolidtumors.Front.Immunol.
B TCGARNA-seqdataanalysis
10,3038.
B Survivalanalysis
9.Lanier,L.L.,Le,A.M.,Civin,C.I.,Loken,M.R.,andPhillips,J.H.(1986).The
B ComparisonwithhumanperipheralbloodforNKcells
relationshipofCD16(Leu-11)andLeu-19(NKH-1)antigenexpressionon
d QUANTIFICATIONANDSTATISTICALANALYSIS human peripheral blood NK cells and cytotoxic T lymphocytes.
B Statisticalanalysis J.Immunol.136,4480–4486.
4248 Cell186,4235–4251,September14,2023
