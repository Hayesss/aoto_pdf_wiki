---
source_path: /mnt/c/Users/Administrator/Zotero/storage/W6NDTUWS/Wu 等。 - 2021 - Single-cell profiling of tumor heterogeneity and t.pdf
ingested: 2026-04-23
sha256: 76236a1d27ee4771
---

ARTICLE
OPEN
https://doi.org/10.1038/s41467-021-22801-0
fi
Single-cell pro ling of tumor heterogeneity and the
microenvironment in advanced non-small cell lung
cancer
FengyingWu1,6,JueFan2,6,YayiHe1,AnwenXiong1,JiaYu1,YixinLi2,YanZhang2,WenchengZhao1,FeiZhou1,
Wei Li1, Jie Zhang1, Xiaosheng Zhang1, Meng Qiao1, Guanghui Gao1, Shanhao Chen1, Xiaoxia Chen1, Xuefei Li1,
Likun Hou3, Chunyan Wu3, Chunxia Su1, Shengxiang Ren1, Margarete Odenthal 4,5, Reinhard Buettner 4,5,
✉ Nan Fang 2,7 & Caicun Zhou 1,7
Lung cancer is a highly heterogeneous disease. Cancer cells and cells within the tumor
microenvironmenttogetherdeterminediseaseprogression,aswellasresponsetoorescape
from treatment. To map the cell type-specific transcriptome landscape of cancer cells and
their tumor microenvironment in advanced non-smallcell lungcancer (NSCLC), weanalyze
42 tissue biopsy samples from stage III/IV NSCLC patients by single cell RNA sequencing
andpresentthelargescale,singlecellresolutionprofilesofadvancedNSCLCs.Inadditionto
celltypesdescribedinprevioussinglecellstudiesofearlystagelungcancer,weareableto
identify rare cell types in tumors such as follicular dendritic cells and T helper 17 cells.
Tumors from different patients display large heterogeneity in cellular composition, chro-
mosomal structure, developmental trajectory, intercellular signaling network and phenotype
dominance. Our study also reveals a correlation of tumor heterogeneity with tumor asso-
ciated neutrophils, which might help to shed light on their function in NSCLC.
1DepartmentofMedicalOncology,ShanghaiPulmonaryHospital,TongjiUniversitySchoolofMedicine,Shanghai,China.2SingleronBiotechnologies,
Nanjing,Jiangsu,China.3DepartmentofPathology,ShanghaiPulmonaryHospital,TongjiUniversitySchoolofMedicine,Shanghai,China.4Instituteof
Pathology,UniversityHospitalofCologne,Cologne,Germany.5CenterforMolecularMedicineCologne,UniversityofCologne,Cologne,Germany.6These
✉
authorscontributedequally:FengyingWu,JueFan.7Theseauthorsjointlysupervisedthiswork:NanFang,CaicunZhou. email:caicunzhoudr@163.com
NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications 1
;,:)(0987654321
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
T
umorecosystemsarecomprisedofcancercells,infiltrating Results
immune cells, stromal cells, and other cell types together Establishment of advanced NSCLC cell atlas. We applied
with noncellular tissue components, which interact and scRNA-seqanalysestobiopsysamplesfrom42advancedNSCLC
collectively determine disease progression as well as response to patients with diverse histological and molecular phenotypes and
therapy1,2. It is well known that cancer patients elicit very indi- treatment history (Fig. 1a, Supplementary Table 1). Following
vidualized responses to different treatments, demanding better multiple qualitycontroland filteringsteps, atotalof90,406cells
characterization of the whole tumor ecosystem beyond currently were analyzed with respect to their transcriptomes. By char-
applied clinical typing of somatic mutations in cancer cells. acteristic canonical cell markers, eleven major cell types were
Furthermore, precisely targeted therapies against well-defined detected, classified as carcinoma cell types, epithelial cells others
oncogenicdriversrevealawidespectrumofresponsesindifferent thancarcinoma cells,immunecelltypes (T cells,Blymphocytes,
settings. For example, the KRAS G12C inhibitors seemed to myeloid cells, neutrophils, mast cells, and follicular dendritic
inducetumorresponsesinthemajorityoflungcancersbutmuch cells) and stromal cell types (fibroblasts and endothelial cells)
lessinpancreaticcancers,whichdifferintheirtumormicromilieu (Fig. 1b, c and Fig. S1). Similar to the observations in previous
dominatedbycancer-associatedfibroblasts3.Antibodiestargeting studies, stromal and immune cells of different patients clustered
PD1 or PD-L1 have achieved substantial overall survival together by cell types, while cancer cells showed higher hetero-
improvementsinadvancednon-smallcelllungcancer(NSCLC). geneity and patient-specific expression signatures (Fig. 1d)14,15.
The 5-year survival rate could be prolonged from less than Similartotheobservationsfrompreviousstudies8,12,theportions
5–29.6% in PD-L1-positive patients4,5. However, major chal- of cancer, stromal, and immune cells varied greatly among
lenges still remain, including low response rate in unselected samples, which could be intrinsic to different tumor phenotypes
patients,lackofreliablepredictivebiomarkers,andidentification or related to locations within the tumor where biopsies were
of more immunotherapeutic targets. Thus, comprehensive taken (Fig. 1e and Supplementary Data 1). For example, tumor
understanding of NSCLC ecosystems holds the promise to specimen P42 (lung adenocarcinoma mixed with sarcomatoid
improve personalized treatment strategies6. carcinoma)andP7revealedastronglyinflammatorymicromilieu
Conventional‘bulk’RNA-sequencingmethodsprocessamixture withalmost50%TcellsincontrasttospecimenP2,P3,andP17,
ofallcells,averagingoutunderlyingdifferencesincell-type-specific which were practically T cell depleted.
transcriptomes. In contrast, single-cell RNA-sequencing (scRNA-
seq)profilesthegeneexpressionpatternofeachindividualcelland
decodes its intercellular signaling networks. This unbiased char- Lung Squamous Carcinoma has higher inter- and intratumor
acterizationprovidesclearinsightsintotheentiretumorecosystem, heterogeneity than lung adenocarcinoma. Based on single-cell
such as mechanisms of intratumoral and intertumoral hetero- expression levels of genes commonly used as markers for
geneity, as well as cell–cell interactions through ligand-receptor immunohistochemistry-basedNSCLCclassification,namelyNAPSA,
signaling7. Thus, several studies deeply characterized the lung TTF-1(NKX2-1)forlungadenocarcinoma(LUAD),andTP63,CK5
tumor microenvironment (TME) at single-cell resolution. An (KRT5) for lung squamous carcinoma (LUSC), subtype classifica-
extensivetaxonomyofstromalcellswithdifferentpathwayactivities tionsalignedwellwiththehistopathologicalclassifications(Fig.S2).
in NSCLC patients presented a first-ever lung cancer TME cell Next,weusedthescRNA-seqdatatoinfercopynumberalterations
atlas8. Isolated infiltrating T cells in NSCLC were classified (CNAs)incancercellpopulations.TheinferredCNAprofilesof42
according to their functional states and dynamics and a subset of patients showed both interpatient and intrapatient heterogeneity
regulatory T cells (Tregs) was found to correlate with the poor (Fig. 2a). For LUAD patients, prominent arm-level insertions were
prognosis in lung adenocarcinoma9. Tumor-infiltrating myeloid foundinchromosome7and8q,withdeletionsinchromosome10.
cells (TIMs), including monocyte, macrophage, dendritic, and Noteworthy, LUAD with known driver mutations have additional
granulocytecelllineages,werecategorizedintoatleast25different amplifications in the 1q and 5p arms. In contrast, LUSC patients
statesbyscRNA-seq10.SubsetsofTIMsdefinedbyuniquemarkers mostlyhave3qinsertionsand5qdeletions.Interestingly,someofthe
have been associated with patient prognosis. Heterogeneity of LUADpatientswithoutdrivermutationshavesimilarCNAprofiles
tumor endothelial cells was also studied for both human and to LUSC. Although expression profiles and composition of the
mouse11. All reports mentioned above focused on early stage, cancer cell transcriptomes were largely patient-specific, carcinoma
resectablelungcancers,whichmaynotreflectthecellularprofilesof cellsfromsomepatientsweremoresimilarthanothers(Fig.2band
tumors at advanced stages that have undergone intense and Fig. S3A, B). In most cases, cancer cells from LUAD and LUSC
exhaustiveinteractionswithstromalandimmunecells.Focusingon patients partitioned into separate clusters. More than half of the
theevolutionaldynamicsoflungadenocarcinoma,Kim’sstudywas LUADpatientsclusteredintoonegroup,whilemostLUSCtumors
performed on the lung adenocarcinoma samples from early-stage formed patient-specific clusters, indicating higher intertumor dif-
tissues to advanced stage biopsies including both primary and ferences in LUSC than in LUAD. Most patients, especially patients
metastatic sites12. Another recent study uncovered transcriptional withLUADe.g.,P16,P20,andP32,haddominantclones,whileina
signatures specific to various targeted therapies and clinical states few LUSC such as P27 and P37 the malignant cells spread across
onprimaryandmetastaticlungbiopsiesbylowthroughputSmart- multiple clusters (Fig. 2b and Fig. S3C). LUSC patients showed
seq2 technology, which only included one squamous carcinoma significantlyhigherclonalitythanLUADpatients(Fig.S3D).
patient13. Until now, the late-stage landscape of lung squamous To quantifytheintratumoral heterogeneity, wedefinedboth a
carcinomawas mostly absent. CNA-based and an expression-based intratumor heterogeneity
In this study, we apply scRNA-seq to analyze the cancer and score, denoted as ITH and ITH (see Methods for their
CNA GEX
TME landscape of advanced NSCLC for both lung adenocarci- definitions).Weobservedvariousdegreesofheterogeneitywithin
noma and squamous carcinoma. We identify distinct cell popu- thetumor(Fig.S4A,B).ITH andITH showedamoderate
CNA GEX
lations and cellular signals that are differentially enriched in correlation (Fig. 2d), potentially due to the nondriver genomic
tumorsdependingonthepathologicaltypes,presenceorabsence alternationsorthemicroenvironmentshapedtumorphenotypes.
ofdrivermutations,anddegreeoftumorheterogeneity.Ourdata We further divided patients into three groups according to both
provideacomprehensivescRNA-seqprofilingonalargenumber the cancer type and mutation: LUAD patients with driver
of small biopsies and may be used to improve diagnostics and mutation (n=12), denoted as LUADm, LUAD patients without
prognosis in clinical settings. driver mutation (n=6), denoted as LUADn, and LUSC patients
2 NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
Fig.1AdvancedNSCLCsingle-cellatlas.aGraphillustrationofthebaselineinformationofthe42patients,includingsubtypes,stages,mutationstatus,
andsmokinghistory.bUMAPplotof90,406cellsfrom42patients,coloredbytheir11majorcelltypes.cHeatmapofcanonicalcell-typemarkersof11
majorcelltypes.dUMAPplotofallcells,coloredbypatients.eMajorcell-typecompositionofeachpatient.Biopsieswerealltakenfromtheprimarylung
tumors.SourcedataareprovidedasaSourceDatafile.
without driver mutation (n=16), denoted as LUSCn. Interest- AT2-1 expressed cell proliferation and cell migration related
ingly,LUSCnpatientshavesignificanthigherITH comparing genes, such as CEACAM6, KITLG, and FOXC1, implying a
CNA
topatientsofLUADm,whiletherewasnostatisticalsignificance phenotypic change towards malignancy. Epithelial cells could
intermsofITH (Fig.2e).Thisfindingalsosuggestedpatients befurtherseparatedintociliatedepithelialcells,clubcells,and
GEX
with driver mutations may be phenotypically influenced beyond basal cells (Fig. 3c, d).
genomicalternations.Thecomparisonbetweenthiscohortanda Previous studies showed that AT2 cells and club cells could
cohortfrompublicdatarevealedincreasedITH scoresoflate- both develop into LUAD cells, while basal cells and club cells
GEX
stage patients12 (Fig. S4C). are potential progenitors of LUSC16,17. Therefore, we orga-
nizedAT2cells,clubcellsandLUADcancercellsaccordingto
Plasticity of lung epithelial cells and their developmental tra- their developmental trajectories (Fig. 3e). The inferred
jectories into malignant tumor cells. All identified alveolar pseudotime paths showed AT2 cells and club cells transited
cells express the canonical markers (CLDN18, SFTPA1, into LUAD tumors independently. In contrast, basal cells
SFTPC) of Alveolar Type 2 cells (AT2) without expressing seemed to act as a transitional state between club cells and
Alveolar Type 1 cell markers (CAV1, AGER). Further clus- LUSC tumor cells (Fig. 3f). Besides such distinct signatures,
tering analysis unveiled two distinct cluster of AT2 cells, we found tumor cells of some patients clustered closely at the
denoted as AT2-1 and AT2-2 (Fig. 3a). AT2-2 resembled a end of the branches, implying a homogeneous and terminal
normal AT2 phenotype with common AT2 markers SFTPA phenotype,whileothershavemorediverseandheterogeneous
and transporter ABCA3 upregulated (Fig. 3b). In contrast, profiles spreading along cancer developmental trajectories.
NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications 3
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
Fig.2Inter-andintratumorheterogeneityofcancercells.aHeatmapofCNAprofilesinferredfromscRNA-seqoftumorcellsofpatients.Redindicated
genomicamplificationsandblueindicatedgenomicdeletions.Thex-axisshowedallchromosomesinthenumericalorder.They-axiswasmarkedbyboth
patientsubgroups.bHeatmapdisplayingproportionsofcancercellsofeachpatientincancerclusters.Theclusteringresultsofcancercellsweregenerated
usingresolution0.4inSeurat.Thearrangementofthepatientsonthey-axiswerebasedontheirsimilaritiesusinghierarchicalclustering.cUMAP
visualizationofcancercellclusters.TheclusterIDscorrespondedtoclusterIDsshowninb.dCorrelationbetweenITH andITH for42patients.
CNA GEX
Shadedareascorrespondedtothe0.95confidenceintervalanalyzedbytwo-sidedt-test.eStatisticaltestsofITH andITH betweenpatientsin
CNA GEX
differentgroups,LUSCn,LUADmandLUADn(LUSCn:n=16,LUADn:n=6,LUADm:n=12biologicalindependentsamples.*p≤0.05;ns:p>0.05).Two-
sidedunpairedWilcoxontestwasperformedtocomparebetweengroups.Thelowerhinge,middleline,andupperhingerofboxplotsrepresentedthefirst,
second,andthirdquartilesofthedistributions.Theupperandlowerwhiskerscorrespondedtothelargestandsmallestdatapointswithinthe1.5
interquartilerange.Allactualdatavalueswerealsoplottedasdotsalongsidetheboxplots.
AdvancedNSCLCTMErevealedarichprogramofstromaland DetailedanalysisofTcellsuncoveredTh17-likecellsandtheir
immune components. To further identify subgroups of each potential interconversion with Tregs. Within tumor-infiltrating
stromalandimmunecelltypes,weclusteredandannotatedthem T cells, we identified CD4+ naïve T cells, CD4+ Tregs, CD4+ T
individually.Weidentifiedfivesubtypesofendothelialcells(EC) helper 17-like T cells (Th17-like), CD8+ effector T cells, CD8+
including lymphatic, venous, and arterial endothelial cells (LEC, exhausted T cells, and Natural Killer (NK) cells according to
VECs, and AECs), tip cells, and an EC cluster enriched with expressionoftheirrespectivemarkers(Fig.4a).Tcellsubtypeswere
interferon induced genes (Fig. S5 and Supplementary Data 2). confirmed by supervised cell-type annotation based on previously
Furthermore,wedividedfibroblastsintopericytesandfibroblasts, studied T subtype expression profiles9 (Fig. 4a). To further char-
including six subclusters of fibroblasts (Fig. S6 and Supplemen- acterizetwoNKclusters(CD3D−,KLRD1+,NKG7+),wereferred
tary Data 3). For immune cells, our data revealed two B cell to the CD16+ (FCGR3A) cluster as NK-1 and CD16− cluster as
subgroups and seven different plasma cells (Fig. S7). Myeloid NK-2 (Fig. 4b). NK-1 contains upregulated transcripts encoding
cells, especially macrophages, have a broad range of phenotypes fractalkinereceptor(CX3CR1)andfibroblastgrowthfactorbinding
andcouldbedividedinto10differentgroups(Fig.S8).Dendritic protein 2 (FGFBP2), both involved in lymphocyte cytotoxic func-
cells (DCs), including plasmacytoid dendritic cells (pDCs), con- tions. NK-2 had higher expression of tissue-resident markerssuch
ventional type 1 and 2 DCs (cDC1 and cDC2), and mature DCs as CD49a (ITGA1), CD103 (ITGAE), and ZNF683. Co-inhibitory
were also discovered. Neutrophils have two distinct clusters, immunecheckpointsincludingCTLA4andTIGITwereenrichedin
expressing potential polymorphonuclear myeloid-derived sup- CD4+ Tregs and CD8+ exhausted T cells (Fig. 4c). However,
+
pressorcells(PMN-MDSCs)relatedgenessuchasLOX-1(OLR1) LAG3 was mainly expressed in CD8 exhausted T cells, which is
to different extents (Fig. S9). consistentwithprevious findings9.
4 NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
Fig.3Phenotypesoflungepithelialcellsandtheirevolutionarytrajectoryintocancercells.aUMAPprojectionofalveolarcells.Alveolarcellscouldbe
furtherdividedintotwoclusters,bothofwhichareAT2cells.TheyweredenotedasAT2-1andAT2-2.bVolcanoplotofdifferentiallyexpressedgenesbetween
AT2-1andAT2-2cells.Differencebetweenpercentageofcellsexpressedintwoclusterswasplottedagainstlogfoldchangeofaverageexpressions.cUMAP
visualizationofepithelialcellsubtypes.Epithelialcellscouldbefurtherannotatedintobasalcells,clubcells,andciliatedcells.dHeatmapofcanonicalmarker
genesofepitheliallungsubtypes.eDevelopmentaltrajectoriesofAT2cells,clubcells,andLUADtumorcells.Normalcellswereshownasawholeforeach
type,andcancercellswereshownseparatelyforeachpatient.fDevelopmentaltrajectoriesofbasalcells,clubcells,andLUSCtumorcells.
+
We then performed trajectory analysis on CD4 T cells to macrophage cluster expressing the scavenger receptor MARCO
determinetheirdevelopmentalpathwayswithinTMEusingboth and CXCL5, and cDCs also exhibited significant differences
Slingshot18 and Monocle19. Slingshot revealed a transitional among the three groups (Fig. 5b). Interestingly, cDC2 displayed
relationship between Tregs and Th17-like cells, originated from Langerin (CD207) expression, which was inferred to be dictated
naïve cells (Fig. 4d). Uncovered by Monocle, naïve cells by the environment23. TCGA survival analysis revealed that
differentiated intotwomajorbranches, Tregsand aproliferating CD207 is a prognostic marker for LUAD, but not for LUSC
population(Fig.4e,f).Interestingly,Th17-likecells,confirmedby (Fig. 5c). However, MARCO is not associated with clinical out-
expression of their master transcription factor RORC, showed a comesofbothLUSCandLUAD.Sinceweidentifiedtwosubtypes
transitional phenotype spreading along the developmental path- of MARCO+ alveolar macrophages, these results combined
+
way from naïve cells to Tregs (Fig. 4f). The CD4 Th17-like impliedthemultifunctionalrolesoftissue-residentmyeloidcells.
populationmarkedbyhighexpressionofgeneKLRB120is,toour WenextinvestigatedthecorrelationbetweenITHscoresandthe
knowledge,thefirstreportofTh17-likecellsidentifiedinNSCLC immune cell compositions. We found neutrophils and two sub-
tumorenvironmentsbyscRNA-seq.Assupportedbyliterature21, types of macrophages were positively correlated with ITH ,
GEX
natural Tregs (nTregs), a subset of Tregs, are believed to while plasma cells were negatively correlated with ITH
GEX
interconvert with Th17-like cells. This result revealed a complex (Fig. 5d). This finding potentially suggested high immunosup-
and delicate interplay between Tregs and Th17-like cells and pressive environment and low cancer killing ability for patients
highlighted the importance of their balance in adaptive immune withhighITH .Overall,wefoundthemyeloidcompartmentis
GEX
responses to tumor antigens22. the mostly affected by tumor subtypes and ITH levels instead of
tumor-infiltrating lymphocytes.
BothNSCLCsubtypesandITHshapedtheimmunelandscape
in TME. To investigate if tumor subtypes and their ITH levels Divergent intercellular networks observed among LUADn,
affect their microenvironment, we compared the cell-type com- LUADm,andLUSC.Inordertoexploretheinterplayamongcell
position of NSCLC by their histology and their driver mutation types within the tumor microenvironment, we performed a
status. We found that neutrophils were significantly depleted in cell–cell interaction analysis and showeda prominent interaction
all LUAD patients (Fig. 5a). While comparing LUAD patients between cancer cells and endothelial cells, fibroblasts and mac-
with and without oncogenic driver mutations, a macrophage rophages (Fig. 6a). Analysis of the interacting molecules across
clusterwithhighlyexpressedCCL13wasenrichedinthegroupof cells showed a complex network with the interplay of oncogenic
mutated tumors (Fig. 5b). The proportions of the tissue-resident pathways as EGFR, NOTCH, WNT, with PDGF and
NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications 5
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
Fig.4SubtypesanddevelopmentaltrajectoryofTcells.aUMAPvisualizationof6Tcellsubtypesand2NKcellsubtypes(left)andpredictedTcell
subtypesbysingleR(right).bHeatmapofselectedmarkersfor2NKclusters.cHeatmapofTsubtypemarkersandselectedfunctionalgenes.
dTransitionalrelationshipamongCD4TcellspredictedbySlingshot.Rainbowcoloringfromredtobluerepresentedthebegintoendofthetrajectory.
eIllustrationofCD4TcelldifferentiationpathwaysinferredbyMonocleandtherelativelocationsofeachCD4Tsubtypesalongthedevelopment
pathways.Theredandbluearrowsindicatedthetwopseudotimedirectionsofcelldevelopment.Thegreysectionrepresentedthebeginningofthe
trajectorybeforethebranchingpoint.fHeatmapshowingrelativeexpressionsofcanonicalmarkersofCD4Tcellsalonginferredtrajectories.Theredand
bluebranchescorrespondtothetwodevelopmentaldirectionsine.
inflammatory signaling pathways, in particular affecting TNF-a subgroups showed different dominant pathways. For example,
and chemokine responsive pathways (Fig. 6b). Notably, VEGFA- LUADmhavehighlevelsofactivationoftheTIGITpathwaybut
mediatedprotein–proteininteractionsandtwoanalogousimmune lowlevelsofactivationofTIM3(HAVCR2)pathway.Wedidnot
checkpoint pathways CD226-TIGIT-CD96 and CD274 (PD-L1)- detectanysignificantactivationofthePD1/PD-L1axisexceptfor
CTLA4-CD28werealsoidentifiedwithintheinteractionnetwork. a few LUSC patients, potentially due to the low expression of
Cancer cells expressed high levels of ligands CXCL1, CXCL2, PD1/PD-L1 on the transcriptomic level. Interaction analysis
CXCL3, and CXCL8, signaling to the receptors CXCR1 and performed on a public dataset confirmed the similar activation
CXCR2 expressed by neutrophils (Fig. 6c). Some of the LUSCn state of checkpoint pathways for late-stage LUAD (Fig. S10A).
andLUADnpatientsshowedincreasedinteractionsbetweenDCs Interestingly, an early-stage LUAD patient in the same dataset
andTcells,includingCXCR3anditspartners,suggestingstrong showed opposite activation status of TIGIT and TIM3 with
effector T cell trafficking and recruiting24. We also confirmed respect to the late-stage patient (Fig. S10B). Nevertheless, by
activation of the CXCL12-CXCR4 pathway between tumor and cellular network analysis of the scRNA-seq data, we generated a
sprouting endothelial cells (AECs and tip cells) described in Fig. comprehensive view of patients’ TME including angiogenesis,
S5. Regarding growth factors, the majority of tumors, regardless CAF activation, recruitment of immunosuppressive cells, T cell
ofsubtypes,hadverystrongsignalsofVEGFinteractionsbetween activation, and detailed activation profiles of checkpoint path-
tumor and various types of endothelial cells (Fig. 6d). PDGF ways. Therapeutics related interactions were heterogeneous even
signaling, on the other hand, was activated between tumor and withinthesamesubtypeoflungcancer,highlightingtheneedsfor
cancer-associated fibroblast (CAF) cells. A distinct pattern for more precise biomarkers to increase the drug efficacies.
LUSC patientsis theactivationof FGF pathways among stromal
cellsand tumorcells,also supportedbypreviousstudies25.Since
only a portion of LUSC patients have FGF pathways activated, Discussion
patient stratification may be important for the usage of drugs Inthisstudy,wepresentthevaluablecomprehensivelandscapeof
targeting FGF pathways. cancercells,immunecells,andstromalcellsinadvancedNSCLC
For patients’ immune environment, we found macrophages, by scRNA-seq analysis. We were able to identify 11 major cell
instead of cancer cells, played a major role in inhibiting T cell types from advanced NSCLC, including 48 subtypes besides
functions through checkpoint pathways (Fig. 6e). Different cancer cells, the majority of which are consistent with previous
6 NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
Fig.5Correlationanalysisofcellularcomposition,tumorsubtypes,andITH.Cellularcompositionanalysisofcelltypebetweenpatientgroupsfor
aneutrophilsandbmacrophagesubtypes.Two-sidedunpairedWilcoxontestwasperformedtocomparebetweengroupsfortestsinaandb(LUSCn:n=
16,LUADn:n=6,LUADm:n=12forbothaandb.**p≤0.01;*p≤0.05;ns:p>0.05).Thelowerhinge,middleline,andupperhingerofboxplots
representedthefirst,second,andthirdquartilesofthedistributions.Theupperandlowerwhiskerscorrespondedtothelargestandsmallestdatapoints
withinthe1.5interquartilerange.Allactualdatavalueswerealsoplottedasdotsalongsidetheboxplots.cSurvivalanalysisfortissue-residentmacrophage
markers(MARCOandCD207)ofLUADandLUSC.dCorrelationanalysisbetweenITH andthecellularcompositionofpatients.Onlysignificantly
GEX
associatedcelltypeswereshown.Thetumorsubtypes(LUAD,LUSC,andNSCLC)wereshownindifferentcolorsandp-valueswereobtainedbytwo-side
t-tests(LUAD:n=18,LUSC:n=22,andNSCLC:n=2).
studies. We focused on the cancer cells, which were not studied We also identified rare cell types such as FDC and Th17-like
extensively at single-cell level in the previous literature. The lymphocytes. The existence of FDC indicated the formation of
shared arm-level CNAs were consistent with the observations lymphoidfollicles,whichusuallycorrelateswithfavorableclinical
from previous genomic sequencing data26, indicating a repre- outcomes27. In tumor-infiltrating CD8 + T cells, there are more
sentative cohort of advanced NSCLC tumor types. Based on a exhaustedTcellsthancytotoxicTcells,whichisoppositetowhat
quantitative approach to define inter- and intratumor hetero- is observed in early stage, resectable NSCLC patients9. Notably,
geneity, we unmasked a broad range of clonality, homogeneity, themyofibroblasttofibroblastratioinourstudywasremarkably
and the complexity beyond current classification systems of high compared to healthy or asthma lungs28. Thus, CAFs with
advancedNSCLC.Ingeneral,LUSChashigherITHthanLUAD. myofibroblast characteristics may act as an important malignant
However, our data call for a more precise profiling of individual signature for advanced stage lung cancer. Certain cell subtypes
patientsonthecellularlevelsbeyondthetraditionalpathological identified in this study were previously determined to be asso-
definitions. For example, specimen P7 is a LUSC tumor with ciated with drug responses. For example, CXCL9+ Mac was
strong TP63/CK expressions and weak NAPSA expression (Fig. enriched in patients responding to immunotherapy29.
S2A).Interestingly,themajorcloneofthispatientonlyrepresents Fromthecellularcompositionanalysis,weshowedneutrophils
less than 75% of its cancer cells (Fig. S3C). Further investigation to be enriched in LUSC. This phenomenon has been demon-
showed one of its minor clones clustered together with many strated by previous studies in NSCLC that neutrophils are more
LUAD patients. abundantinhumanLUSCcomparedtoLUADduetodifferences
NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications 7
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
Fig.6Cellandgeneinteractionnetworks.aThecellularinteractionnetworkamongcelltypesofNSCLCpatients.Thelinewidthandcolorwere
proportionaltonumbersofinteractionsbetweencelltypes.bInteractingmolecularnetworks.Withineachconnectednetwork,node(gene)sizeswere
proportionaltothenumberofneighbors(interactinggenes)ofeachnode.HeatmapsshownselectedinteractingpairsforselectedcelltypesinLUADm,
LUADn,andLUSCngroups.Z-scoresofexpressionlevelswererepresentedbycolor,anddotsizedisplayedtheproportionofpatientswhohavesignificant
interactionforthegivenligand-receptorpair.cchemokineandchemokinereceptorsbetweencancercells,TcellsandDCs.dselectedgrowthfactors
betweencancercellsandstromalcells.eselectedcheckpointsbetweencancercells,macrophages,andTcells.
inTME30.Inasubsequentstudy,themastertranscriptionfactor different neutrophil infiltration features were proposed to be
SOX2,alineage-specificoncogeneforsquamouscellcarcinomas, regulated by tumor-intrinsic driver mechanisms. On the other
wasfoundtobe overexpressedand topromotetumor associated hand,cancerandneutrophilshavestrongerinteractionsinLUAD
neutrophil (TANs)-accumulation by upregulating CXCL5 (the patients. The combined observations suggested complex and
mouse homolog of human CXCL6) expression31. Therefore, diverse functions of neutrophils within TME. Our study also
8 NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
revealed a correlation of tumor heterogeneity and neutrophil analysis.Weobtained1673genesand5238UMIspercellonaverage.Weoptedout
contents. Given that separate studies showed high neutrophil thebatcheffectcorrectionalgorithmbasedonthehighlyconsistentresultsamong
contentsandhightumorheterogeneityrelatedtoimmunotherapy patientsandtheundesirableremovalofheterogeneityamongcancercellsof
failurerespectively32–34,ourdatafurtherbridgedthegapbetween individualpatients(Fig.S1b).Harmonywasusedasthebatcheffectremoval
method.
high neutrophil contents and high tumor heterogeneity. The WeusedSeurat2.3tofirstnormalizeexpressionmatricesbyfunction
mechanismofinterplaybetweentumorheterogeneityandtumor- NormalizeDataandScaleData.ThenFindVariablefunctionwasappliedtoselect
infiltrating neutrophils might be a key element to explain the thetop600variablegenesandperformprinciplecomponentanalysis.Thefirst20
difference in immunotherapy efficacy. principlecomponentsandresolution1.0wereusedwithFindClustersfunctionto
generate37cellclusters.Toassignoneofthe11majorcelltypestoeachcluster,we
By mapping cells in TME and their possible functions, by scoredeachclusterbythenormalizedexpressionsofthefollowingcanonical
identifying more cell types and their marker genes, and by markers:Endothelialcells(CLDN5,VWF,PECAM1),Epithelialcells(CAPS,
highlightingintratumorcell–cellinteractions,wepresentedherea SNTN),Alveolarcells(CLDN18,AQP4,FLOR1),Fibroblasts(COL1A1,COL1A2,
DCN),Tcells(CD2,CD3D,CD3E,CD3G),Bcells(CD79A,CD79B),Myeloidcells
comprehensivecollectionofdatasets,whichprovidedeepinsights
(CD14,LYZ),Neutrophils(CSF3R,S100A8,S100A9),Folliculardendriticcells
on advanced NSCLC. Some of our findings are unreported and (FDCSP),Mastcells(GATA2,TPSAB1,TPSB2).Thehighestscoredcelltypewas
will need further functional validation. Despite this limitation, it assignedtoeachcluster.Cancercellclusterswerenegativefornormallung
can serve as valuable resources and a proof-of-concept study for epithelialmarkersandpositiveforEPCAM.Theclustersassignedtothesamecell
typewerelumpedtogetherforthefollowinganalysis.Thefinalresultswere
future research to identify biomarkers and targets for treatment
manuallyexaminedtoensurethecorrectnessoftheresultsandvisualizedby
and enable personally tailored therapeutic decisions for patients
UniformManifoldApproximationandProjection(UMAP).The11majorcell
with advanced NSCLC. typeswerechosenbyinitialexploratoryinspectionofthedifferentiallyexpressed
genes(DEGs)ofeachclustercombinedwithliteraturestudy.TheDEGswere
generatedbySeuratFindMarkersfunction.
Methods
Patients.Allspecimensanalyzedinthisstudywereobtainedfrompatientswith
histologicallyprovenadvanced,unresectableNSCLC.Smokinghabitswerecate-
LUADandLUSCclassificationbasedonscRNA-seqexpression.Wedefineda
gorizedintosmokers(individualssmoke>20packs/yearor<10yearsofsmoking LUADandaLUSCscoreforeachpatient.Thescorewascalculatedbasedonthe
cessationhistorypriortoenrollment)andnon-smokers(individualssmoke<100 averagepercentageofmarkerexpressionsoftumorcellsforLUAD(NAPSAand
cigarettesintheirlifetime).Allsampleswerecollectedfromprimarylungtumorby TTF-1)orLUSC(KRT5,DSG,andTP63),andthehigherscoredsubtypewas
diagnosticproceduresincludingtranscutaneousneedlebiopsyorbronchoscopy assignedtoeachpatient.Ifbothscoresarelessthan0.05,translatingto5%ofcells
fromNovember2018toAugust2019andallsubjectshaveprovidedtheirwritten expressinggivenmarkers,weassignedthepatienttoNSCLC.Consideringboth
informedconsent.Histopathologicalreviewofhematoxylin-eosinstainedsections pathologicalsubtypeassignmentandscRNAsubtypeassignment(Fig.S2A),we
wasperformedbyseniorlungpathologists.Immunohistochemistrywasdonefor
determinedafinalclassificationuponthereviewofexperts.Allthefollowing
furtherhistologicalsubtypeclassification.ReversetranscriptionPCR(RT-PCR) groupingwasbasedonthefinalclassificationofpatients.
wasperformedfortestingofEGFRmutation,KRASmutation,ALKfusion,ROS1
fusion,RETfusion,HER2mutation,BRAFmutation,andMETexon14skipping scRNA-seq-basedCNAdetection.WeinferredCNAsof42patientsby
foralladenocarcinoma,somesquamouscarcinomaandsomeNSCLCpatients.The InferCNV14usingsingle-celltranscriptomicprofiles.AsdescribedinInferCNV,we
studywasapprovedbytheEthicalCommitteeofShanghaiPulmonaryHospital usednon-malignantcellsincludingimmunecellsandstromalcellsasbaselinesto
(K18-089-1). estimatetheCNAofmalignantcells.Briefly,genesweresortedbytheirgenomic
CharacteristicsofpatientsaresummarizedinFig.1aandSupplementary locationsoneachchromosome.Wethenused101genesasaslidewindowto
Table1.Ofall42patients,35werebiopsiedbeforesystemictreatment,2after smooththerelativeexpressiononeachchromosometoremovegene-specific
failureofTKI,3afterfailureofimmunotherapy,and2afterfailureof expressioninfluence.Geneexpressedinlessthan20cellswerefiltered.Wecentered
chemotherapy. therelativeexpressionvaluesto1andused1.5standarddeviationoftheresidual
normalizedexpressionvaluesastheceilingandfloorforvisualizationusingR
Tissuedissociationandsingle-cellsuspensionpreparation.Freshsampleswere packagePheatmap.Forvisualization,randomlysampled100malignantcellsof
storedintheGEXSCOPETissuePreservationSolution(SingleronBiotechnologies,
eachpatientwereshownastheirrepresentativeCNAprofiles.
Nanjing,China)at2–8°Cimmediatelyafterbeingcollectedbyneedlebiopsyor
bronchoscopy.Priortodissociation,tissuesampleswerewashedwithHanks IntratumoralheterogeneityscoresbasedonCNAsandgeneexpressions.The
BalancedSaltSolution(HBSS)forthreetimes,mincedintosmallpieces,and calculationsofintratumoralheterogeneityscoreswereinspiredbyapreviousstudy
digestedin2mlGEXSCOPETissueDissociationSolution(SingleronBiotechnol- andmodifiedasfollows35.First,tocalculateITH ,weusedtherelative
ogies)followingmanufacturer’sinstructions.Briefly,thespecimensweredigested
expressionvaluematrixgeneratedbyinferCNVa
C
n
N
d
A
calculatedthepairwise
at37°Cfor15minwithcontinuousagitation.A40-micronsterilestrainer cell–celldistancesusingPearson’scorrelationcoefficientsforeachpatient.ITH
CNA
(Corning)wasusedtoseparatecellsfromimpuritiesafterdigestion.Thecellswere wasdefinedasinterquartilerange(IQR)ofthedistributionforallmalignantcell
thencentrifugedat300×g4°Cfor5minandcellpelletswereresuspendedin1ml pairs’Pearson’scorrelationcoefficients.Similarly,wealsousedgeneexpression
PBS(HyClone).CellsuspensionswerecountedwithTC20automatedcellcounter profilesofcancercellsofeachpatienttoconstructthedistributionoftheintra-
(Bio-Rad)todeterminecellconcentrationandviability. tumoraldistances.ITH wasassignedastheIQRofthedistribution.Public
GEX
single-celllungcancerdatasetsGSE131907andE-MTAB-6149wereusedtocal-
Single-cellRNA-sequencinglibrarypreparation.Theconcentrationofsingle-cell culatetheITH GEX scoresofearly-stageandadvancedstagelungcancer.
suspensionwasadjustedto1×105cells/mLinPBS.Single-cellsuspensionwasthen
loadedontoamicrofluidicchip(GEXSCOPESingleCellRNA-seqKit,Singleron Cellsubtypeidentification.WefurtherclusteredTcells,Bcells,neutrophils,
Biotechnologies)andscRNA-seqlibrarieswereconstructedaccordingtothe myeloidcells,fibroblasts,endothelialcells,alveolarcells,epithelialcells,andcancer
manufacturer’sinstructions(SingleronBiotechnologies).TheresultingscRNA-seq
cellsindividually.Wesettheresolutionto0.8forTandBcells.Formyeloidcells,
librariesweresequencedonanIlluminaHiSeqX10instrumentwith150bppaired endothelialcellsandalveolarcells,theresolutionwas0.6.Forfibroblasts,neu-
endreads. trophilsandepithelialcells,wesetresolutionto0.4,0.2,and1.2,respectively.
Withineachlineage,weappliedaniterativeprocesstoremoveputativedoublet
Generationofsingle-cellgeneexpressionmatrices.Rawreadswereprocessed clusters,ifany,andreclusteredtheremainingcells.Putativedoubletswereiden-
tifiedbydoublepositiveexpressionsofthecanonicalmarkergenesof11majorcell
togenerategeneexpressionmatricesbyscopetools(https://anaconda.org/
singleronbio/scopetools).First,readonewithoutpolyTtailswerefiltered,thencell typesdiscussedabove.WithinTlineage,weusedthefollowingmarkersforsubtype
barcodesanduniquemolecularidentifiers(UMI)wereextracted.Adaptersand
identification:CD8+exhaustedT(CD8A,LAG3,andTIGIT),CD8+effector
T(CD8A,GNLY,GZMA,GZMK,GZMB,GZMH),CD4+naïveT(CCR7,LEF1,
polyAtailsweretrimmedbeforealigningreadtwotoGRCh38withensemble
IL7R,andSELL),CD4+Tregs(FOXP3,IL2RA,andIKZF2),CD4+proliferating
version92geneannotation.Second,readswiththesamecellbarcode,UMIand
(TOP2A,MKI67),andCD4+Th17-like(KLRB1,RORC).NotethatCD4itselfhas
geneweregroupedtogethertocountthenumberofUMIspergenepercell.Cell
numberwasthendeterminedbasedonthe‘knee’method. lowRNAexpressionlevelsandCD4TcellsweredeductedbyCD3positiveand
CD8negative.KLRC1,KLRD1,andNKG7wereusedasthemarkersofNKcells.
TcellsubtypeswerealsopredictedbysingleRbasedonTcellannotationsofpublic
Qualitycontrol,cell-typeclustering,andmajorcell-typeidentification.We datasetGSE992549,36.Similarly,wedistinguishedfollicularBcells(MS4A1,MHC-
removedcellsthathadeitherlowerthan200orhigherthan5000expressedgenes. II,CXCR4)fromplasmacells(MZB1,JCHAIN,IgH)amongtheBcelllineage.
Furthermore,wediscardedcellswithmorethan30,000UMIsandmitochondria PlasmacytoidDC(IL3RA,LILRA4,CLEC4C)wasclusteredintheBcelllineage.For
contenthigherthan30%.Finally,90,406cellswereobtainedforthedownstream themyeloidclusters,macrophageswerepositiveforcanonicalmarkerCD68,and
NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications 9
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
M2-likemacrophagemarkersCD163andMRC1/CD206.Othermyeloidcelltypes Received: 9 April2020;Accepted: 24 March2021;
wereconfirmedbyspecificmarkergenesincludingclassicalmonocytes(CD14,
LYZ,VCAN),cDC1(XCR1,CLEC9A),cDC2(FCER1A,CD1C),andmatureDC
(LAMP3).
Withinfibroblasts(DCNandCOL1A1),RGS5andCSPG4wasusedtomarkthe
pericytes.MyofibroblastswereidentifiedbyupregulationofACTA2andMYH11.
Forendothelialcells(PECAM1,VWFandENG),tipcellsarecharacterizedbytheir References
markersandangiogenesis-relatedgenes(KCNE3,ESM1,ANGPT2,andAPLN).
VascularcellsmainlyconsistedofVECsandAECs,respectivelyidentifiedbytheir 1. Binnewies,M.etal.Understandingthetumorimmunemicroenvironment
(TIME)foreffectivetherapy.Nat.Med.24,541–550(2018).
markersACKR1andGJA5.Asubsetofthecellsexpressinglymphaticmarkerssuch
asPDPNandPROX1weredefinedasLECs-like.Usingrepresentativemarkersfor 2. Ostman,A.Thetumormicroenvironmentcontrolsdrugsensitivity.Nat.Med.
classicalairwayepithelialcelltypes,weidentifiedalveolarType2cells(SFTPC,
18,1332–1334(2012).
SFTPA1,andABCA3),clubcells(SCGB1A1andSCGB3A1),basalcells(KRT5, 3. Dominguez,C.X.etal.Single-cellRNAsequencingrevealsstromalevolution
KRT6A,andKRT14),andciliatedcells(FOXJ1,TPPP3,andPIFO)foralveolarcells
intoLRRC15+myofibroblastsasadeterminantofpatientresponsetocancer
andotherlungepithelialcells.Specificgenesforcell-typeidentificationare immunotherapy.CancerDiscov.10,232–253(2020).
providedinSupplementaryTable2.Forcancerclusters,clusteringresolutions0.2, 4. Gandhi,L.etal.Pembrolizumabpluschemotherapyinmetastaticnon-small-
0.4,and0.6wereallusedtotesttherobustnessofcellgrouping.
celllungcancer.N.Engl.J.Med.378,2078–2092(2018).
5. Nadal,E.etal.Immunotherapywithcheckpointinhibitorsinnon-smallcell
lungcancer:insightsfromlong-termsurvivors.CancerImmunol.
T
of
ra
c
j
e
e
ll
ct
s
o
u
r
b
y
ty
a
p
n
e
a
s
ly
w
s
i
i
t
s
h
.W
po
e
te
a
n
p
t
p
ia
li
l
e
d
d
e
M
ve
o
lo
n
p
o
m
cl
e
e
n
2
t
t
a
o
l
d
re
e
l
t
a
e
t
r
i
m
on
in
sh
e
ip
th
.
e
F
l
o
in
r
e
C
ag
D
e
4
d
+
iff
T
ere
c
n
el
t
l
i
s
a
,
ti
w
o
e
n Immunother.68,341–352(2019).
6. Herbst,R.S.,Morgensztern,D.&Boshoff,C.Thebiologyandmanagementof
usedSeurat2.3FindVariableFeaturesfunctiontoselecttop1500highvariable non-smallcelllungcancer.Nature553,446–454(2018).
genesoffourCD4clusterstoordercells.DDRTreewasusedtolearntree-like
7. Baslan,T.&Hicks,J.Unravellingbiologyandshiftingparadigmsincancer
trajectories.Theheatmapalongthedevelopmentaltrajectorywasonlyshownfor withsingle-cellsequencing.Nat.Rev.Cancer17,557–569(2017).
markergenesofTsubtypes.ForCancercellsandnormalepithelialcells,weused
8. Lambrechts,D.etal.Phenotypemoldingofstromalcellsinthelungtumor
AT2cells,clubcells,andLUADcancercellclusterstoinfertheevolutionalpaths
microenvironment.Nat.Med.24,1277–1289(2018).
forLUADtumors.ForLUSCtumors,weselectedbasalcells,clubcells,andLUSC
9. Guo,X.etal.GlobalcharacterizationofTcellsinnon-small-celllungcancer
cancercellclusters.Top1000highvariablegeneswereusedforbothLUADand
LUSCtrajectories.WealsoappliedSlingshottouncovertheCD4+Tcelldevel- bysingle-cellsequencing.Nat.Med.24,978–985(2018).
opmenttrajectory.TheidentifiedpathsweremappedtoUMAPprojectionfor 10. Zilionis,R.etal.Single-celltranscriptomicsofhumanandmouselungcancers
visualization. revealsconservedmyeloidpopulationsacrossindividualsandspecies.
Immunity50,1317–1334(2019).
11. Goveia,J.etal.Anintegratedgeneexpressionlandscapeprofilingapproachto
Cellularcompositionanalysisbetweenpatientgroups.Toassesswhethercell-
identifylungtumorendothelialcellheterogeneityandangiogeniccandidates.
typecompositionsweresignificantlydifferentbetweengroupsofpatients,weused
CancerCell37,21–36(2020).
Rpackageggpubrforthestatisticaltestingandvisualization.Forthecomparisonof
twogroups,t-testwasappliedtotestthestatisticalsignificance.P-values<0.05were 12. Kim,N.etal.Single-cellRNAsequencingdemonstratesthemolecularand
cellularreprogrammingofmetastaticlungadenocarcinoma.Nat.Commun.
consideredstatisticallydifferent.ToassessthecorrelationbetweenITHandcellular
11,2285(2020).
composition,ggscatterfunctioninggpubrwasappliedtocalculatethePearson
correlationcoefficientsandtheassociatedp-values. 13. M
by
a
S
y
i
n
n
a
g
r
l
d
e
,
-c
A
e
.
ll
e
R
t
N
al.
A
T
s
h
e
e
q
r
u
a
e
p
n
y
c
-i
i
n
n
d
g.
u
C
ce
e
d
ll
e
1
v
8
o
2
lu
,
t
1
io
23
n
2
o
–
f
1
h
25
u
1
m
(
a
2
n
02
lu
0
n
).
gcancerrevealed
14. Tirosh,I.etal.Dissectingthemulticellularecosystemofmetastaticmelanoma
Intercellularinteractionanalysis.WeusedCellphoneDB37toperformthe bysingle-cellRNA-seq.Science352,189–196(2016).
interactionanalysisbetweencelltypesineachsample.Wesettheiterationto1000 15. D’Angelo,F.etal.Themolecularlandscapeofgliomainpatientswith
andotherwisefollowedthedefaultsettingsofthesoftware.Thecellularnetwork Neurofibromatosis1.Nat.Med.25,176–187(2019).
wasconstructedbasedoninteractionsexistinginmorethanfivepatients.The 16. Sarode,P.etal.Epithelialcellplasticitydefinesheterogeneityinlungcancer.
interactionpairswithranklargerthan0.1werediscardedtoincreasethespecificity.
Cell.Signal.65,109463(2020).
Forcellinteractionnetwork,celltypeswereconsiderednodes,andthenumberof 17. Cheung,W.K.&Nguyen,D.X.Lineagefactorsanddifferentiationstatesin
interactionsbetweentwocelltypesweretreatedasedgeweights.Thenetworkwas lungcancerprogression.Oncogene34,5771–5780(2015).
visualizedbyCytoscape38.Forthecell-typeinteractionnetworks,wefilterthecell
18. Street,K.etal.Slingshot:celllineageandpseudotimeinferenceforsingle-cell
typeswithinteractionlowerthan500.Thelinewidthandcolorscalewerepro-
transcriptomics.BMCGenomics19,477(2018).
portionaltotheedgeweights.Geneinteractionnetworksweregeneratedasfol-
19. Trapnell,C.etal.Thedynamicsandregulatorsofcellfatedecisionsare
lowing.First,amasternetworkcontainingbothcelltypesandgeneswas
revealedbypseudotemporalorderingofsinglecells.Nat.Biotechnol.32,
constructed.Bothligand-receptorrelationshipbetweengenesandexpression 381–386(2014).
relationshipbetweencelltypesandgeneswereconsiderededges.Fromthemaster
20. Cosmi,L.etal.Humaninterleukin17-producingcellsoriginatefromaCD161
n
fir
e
s
tw
tf
o
o
r
u
k
r
,
m
ce
a
ll
jo
n
r
o
c
d
o
e
n
s
n
w
ec
e
t
r
e
e
d
t
c
h
o
e
m
n
p
re
o
m
ne
o
n
v
t
e
s
d
w
t
e
o
re
ge
e
n
xt
e
r
r
a
a
c
t
t
e
ed
th
t
e
o
g
r
e
e
n
p
e
re
o
se
n
n
ly
tt
n
h
e
e
tw
in
o
t
r
e
k
rc
s.
el
T
lu
h
l
e
ar
+CD4+Tcellprecursor.J.Exp.Med.205,1903–1916(2008).
21. Zheng,S.G.RegulatoryTcellsvsTh17:differentiationofTh17versusTreg,
geneinteractionnetworks.Next,weanalyzedimportantintercellularsignals
arethemutuallyexclusive?Am.J.Clin.Exp.Immunol.2,94–106(2013).
includingcytokines,growthfactors,andimmunecheckpoints.Weshowedthe
22. Omenetti,S.&Pizarro,T.T.TheTreg/Th17axis:adynamicbalanceregulated
relativeexpressionlevels(z-scores)ofligandsorreceptors,againstthepercentages
ofpatientswithsignificantinteractionsforeachgroupbetweencell-typepairs.We bythegutmicrobiome.Front.Immunol.6,639(2015).
usedpublicdatasetGSE131907tocomparecellularinteractionbetweenearly-stage 23. Amon,L.,Lehmann,C.H.K.,Heger,L.,Heidkamp,G.F.&Dudziak,D.
andlate-stageLUAD.
Theontogeneticpathofhumandendriticcells.Mol.Immunol.120,122–129
(2020).
24. Groom,J.R.&Luster,A.D.CXCR3inTcellfunction.Exp.CellRes.317,
TCGAsurvivalanalysis.WeusethewebserverofGeneExpressionProfiling
620–631(2011).
InteractiveAnalysis(GEPIA)39forTCGAsurvivalanalysis.Specifically,aninter-
25. Salgia,R.Fibroblastgrowthfactorsignalingandinhibitioninnon-smallcelllung
estedgenenameandcancersubtypewerechosenastheinputstogeneratethe cancerandtheirroleinsquamouscelltumors.CancerMed.3,681–692(2014).
survivalcurvesforpatientoverallsurvival(OS)andthestatisticaltestingresults.
Weused‘median’asthegroupcutoffmetrictoassignthelowerandhigherhalfof 26. Zhang,X.C.etal.Comprehensivegenomicandimmunological
characterizationofChinesenon-smallcelllungcancerpatients.Nat.
thepatientsasthelowandhighgroup,respectively.P-values<0.05wasconsidered
statisticallysignificant. Commun.10,1772(2019).
27. Hou,W.etal.Thedegreeofoverlapbetweenthefolliculardendriticcell
meshworkandtumorcellsinmantlecelllymphomaisassociatedwith
Reportingsummary.FurtherinformationonresearchdesignisavailableintheNature prognosis.Pathol.Res.Pract.214,513–520(2018).
ResearchReportingSummarylinkedtothisarticle. 28. Nam,Y.H.,Lee,S.K.,Sammut,D.,Davies,D.E.&Howarth,P.H.
Preliminarystudyofthecellularcharacteristicsofprimarybronchial
Data availability
fibroblastsinpatientswithasthma:expressionofalpha-smoothmuscleactin,
fibronectincontainingextratypeIIIdomainA,andsmoothelin.J.Invest.
TherawsequencingdataweredepositedatGeneExpressionOmnibusGSE148071.The Allergol.Clin.Immunol.22,20–27(2012).
publisheddatausedforvalidationorcomparationinthisstudywereretrievedfromthe
NCBIGeneExpressionOmnibusdatabaseaccessioncodeGSE13190712,GSE992549,and 29. House,I.G.etal.Macrophage-derivedCXCL9andCXCL10arerequiredfor
ArrayExpressunderAccessionsE-MTAB-61498.Theremainingdataareavailablewithin a
C
n
a
t
n
it
c
u
e
m
rR
or
es
i
.
m
2
m
6,
u
4
n
8
e
7–
re
5
s
0
p
4
on
(2
s
0
es
20
f
)
o
.
llowingimmunecheckpointblockade.Clin.
theArticle,SupplementaryInformationoravailablefromtheauthorsuponrequest.
10 NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-22801-0
30. Kargl,J.etal.Neutrophilsdominatetheimmunecellcompositioninnon- J.F.,Y.Z.,M.O.,R.B.,andN.F.interpretedthedatawithhelpfromX.S.Z.,X.X.C.,X.F.L.,
smallcelllungcancer.Nat.Commun.8,14381(2017). C.X.S.,andS.X.R.L.K.H.andC.Y.W.reviewedpathology.M.O.andR.B.helped
31. Mollaoglu,G.etal.Thelineage-definingtranscriptionfactorsSOX2and reviewingthepaperandprovidedcriticaldatainterpretation.F.Y.W.andJ.F.wrotethe
NKX2-1determinelungcancercellfateandshapethetumorimmune manuscriptwithinputfromallauthors.Allofauthorshavereadandapprovedthe
microenvironment.Immunity49,764–779(2018). manuscript.
32. Wolf,Y.etal.UVB-inducedtumorheterogeneitydiminishesimmune
responseinmelanoma.Cell179,219–235(2019).e221.
Competing interests
33. McDonald,K.A.etal.Tumorheterogeneitycorrelateswithlessimmune
Theauthorsdeclarenocompetinginterests.
responseandworsesurvivalinbreastcancerpatients.Ann.Surg.Oncol.26,
2191–2199(2019).
34. Kargl,J.etal.Neutrophilcontentpredictslymphocytedepletionandanti-PD1 Additional information
treatmentfailureinNSCLC.JCIInsight4,e130850(2019). SupplementaryinformationTheonlineversioncontainssupplementarymaterial
35. Ma,L.etal.Tumorcellbiodiversitydrivesmicroenvironmental availableathttps://doi.org/10.1038/s41467-021-22801-0.
reprogramminginlivercancer.CancerCell36,418–430(2019).
36. Aran,D.etal.Reference-basedanalysisoflungsingle-cellsequencingrevealsa CorrespondenceandrequestsformaterialsshouldbeaddressedtoC.Z.
transitionalprofibroticmacrophage.Nat.Immunol.20,163–172(2019).
37. Vento-Tormo,R.etal.Single-cellreconstructionoftheearlymaternal-fetal PeerreviewinformationNatureCommunicationsthanksDietherLambrechtsandthe
interfaceinhumans.Nature563,347–353(2018). other,anonymous,reviewer(s)fortheircontributiontothepeerreviewofthiswork.
38. Shannon,P.etal.Cytoscape:asoftwareenvironmentforintegratedmodelsof
biomolecularinteractionnetworks.GenomeRes.13,2498–2504(2003). Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
39. Tang,Z.etal.GEPIA:awebserverforcancerandnormalgeneexpression
profilingandinteractiveanalyses.NucleicAcidsRes.45,W98–W102(2017). Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
publishedmapsandinstitutionalaffiliations.
Acknowledgements
Wethankallthepatientsfortheirgenerousdonationoftissuesamplesforanalysisinthis Open Access This article is licensed under a Creative Commons
study.WethankFangChenandXiaoyuanZiforperformingscRNA-seqexperiments Attribution 4.0 International License, which permits use, sharing,
anddiscussingexperimentresults.ThisworkwassupportedbyNationalNatureScience adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
FoundationofChina(81871865),ClinicalResearchPlanofSHDC(No. appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
SHDC2020CR4001),andFundingfromShanghaiScienceandTechnologyCommission Commonslicense,andindicateifchangesweremade.Theimagesorotherthirdparty
(19411950301).Thefundershadnoroleinstudydesign,datacollectionandanalysis, materialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unless
decisiontopublish,orpreparationofthemanuscript.
indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
article’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutory
Author contributions regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
thecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/
F.Y.W.,J.F.,N.F.,andC.C.Z.conceivedandsupervisedthestudy.F.Y.W.supervised
licenses/by/4.0/.
samplecollectionandclinicalannotation,withhelpfromY.Y.H.,A.W.X.,J.Y.,W.C.Z.,
F.Z.,W.L.,J.Z.,M.Q.,G.H.G.,andS.H.C.J.F.andY.X.L.performeddataanalysis.F.Y.W.,
©TheAuthor(s)2021
NATURECOMMUNICATIONS| (2021) 12:2540 |https://doi.org/10.1038/s41467-021-22801-0|www.nature.com/naturecommunications 11
