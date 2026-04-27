---
source_path: /mnt/c/Users/Administrator/Zotero/storage/QYFWZM6I/Troiani 等。 - 2022 - Single-cell transcriptomics identifies Mcl-1 as a .pdf
ingested: 2026-04-23
sha256: e15c3fba11f21c3c
---

ARTICLE
https://doi.org/10.1038/s41467-022-29824-1 OPEN
fi
Single-cell transcriptomics identi es Mcl-1 as a
target for senolytic therapy in cancer
Martina Troiani1,2,3,12, Manuel Colucci1,2,4,12, Mariantonietta D’Ambrosio1,2,4, Ilaria Guccini5,
Emiliano Pasquini1,2, Angelica Varesi1,2, Aurora Valdata1,2, Simone Mosole1,2, Ajinkya Revandkar1,2,6,
Giuseppe Attanasio1,2, Andrea Rinaldi1,2, Anna Rinaldi7,8, Marco Bolis 1,2,3,9, Pietro Cippà7,8 &
✉
Andrea Alimonti 1,2,10,11
Cellssubjectedtotreatmentwithanti-cancertherapiescanevadeapoptosisthroughcellular
senescence. Persistent senescent tumor cells remain metabolically active, possess a secre-
toryphenotype,andcanpromotetumorproliferationandmetastaticdissemination.Removal
of senescent tumor cells (senolytic therapy) has therefore emerged as a promising ther-
apeuticstrategy.Here,usingsingle-cellRNA-sequencing,wefindthatsenescenttumorcells
rely on the anti-apoptotic gene Mcl-1 for their survival. Mcl-1 is upregulated in senescent
tumorcells,includingcellsexpressinglowlevelsofBcl-2,anestablishedtargetforsenolytic
therapy. While treatment with the Bcl-2 inhibitor Navitoclax results in the reduction of
metastases in tumor bearing mice, treatment with the Mcl-1 inhibitor S63845 leads to
complete elimination of senescent tumor cells and metastases. These findings provide
insightsonthemechanismbywhichsenescenttumorcellssurviveandrevealavulnerability
that can be exploited for cancer therapy.
1InstituteofOncologyResearch(IOR),OncologyInstituteofSouthernSwitzerland(IOSI),CH6500Bellinzona,Switzerland.2UniversitàdellaSvizzera
Italiana,CH6900Lugano,Switzerland.3BioinformaticsCoreUnit,SwissInstituteofBioinformatics,TI,6500Bellinzona,Switzerland.4FacultyofBiologyand
Medicine,UniversityofLausanneUNIL,CH1011Lausanne,Switzerland.5InstituteofMolecularHealthSciences,ETHZurich,CH8093Zurich,Switzerland.
6MassachusettsGeneralHospitalCancerCenter,HarvardMedicalSchool,Charlestown,MA02129,USA.7DepartmentofMedicine,DivisionofNephrology,
EnteOspedalieroCantonale,Lugano,Switzerland.8LaboratoriesforTranslationalResearch,EnteOspedalieroCantonale,Bellinzona,Switzerland.
9ComputationalOncologyUnit,DepartmentofOncology,IstitutodiRicercheFarmacologiche‘MarioNegri’IRCCS,20156Milano,Italy.10Departmentof
HealthSciencesandTechnology(D-HEST)ETHZurich,8093Zurich,CH,Switzerland.11DepartmentofMedicine&VenetoInstituteofMolecularMedicine,
✉
UniversityofPadova,Padova,Italy.12Theseauthorscontributedequally:MartinaTroiani,ManuelColucci. email:andrea.alimonti@ior.usi.ch
NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications 1
;,:)(0987654321
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
C
ells subjected to elevated stress such as treatment with metastatic prostate cancer, respectively. As previously reported,
anti-cancer therapies can react in two ways: either die or
bothPtenpc−/− andthePtenpc−/−
;Timp1
−/−
prostatetumorsare
remain suspended in between life and death, a condition characterized by the presence of both a proliferative and a
known as cellular senescence1–4. Cellular senescence is a stable senescent compartment, as detected by positivity to SA-β-
cellgrowtharrestthatoccursintumorcellssubjectedtodifferent Galactosidase (SA-β-Gal) staining and the expression of differ-
insults including treatment with chemo-radiotherapy or targeted ent senescence markers (Fig. 1a, Supplementary Fig. 1a)6,20.
therapies1,2,4–6.
Although arrested, senescent tumor cells remain Epithelialtumorcells(Epcam
+
)wereFACS-sortedandanalyzed
metabolicallyactiveandsecreteinthetumormicroenvironmenta by 10× Genomics single-cell RNA sequencing to obtain the
variety of cytokines and inflammatory factors, known as the transcriptomic profiles of almost 4000 cells (Fig. 1b, Supple-
senescence-associated secretory phenotype (SASP)1,2,5,7. Several mentary Fig. 1b).By using a graph-based clustering method and
findings in vivo demonstrate that senescence limits tumor pro- Uniform Manifold Approximation and Projection (UMAP), we
gression by arresting cancer cells and promoting immune identified ten cancer cell clusters (Supplementary Fig. 2a–d). In
surveillance4,5,7. However, after an initial beneficial phase, per- order to identify senescent tumor cells at single-cells resolution,
sistent senescent tumor cells can promote tumor growth, wedefinedasenescencesignaturebycombiningtheexpressionof
migration, and even metastases2,6,7. These deleterious cancer p16INK4a, p15INK4b, p19Arf, p21Waf1/Cip1, p27Kip1, and PAI-1, the
phenotypes have been described, particularly in tumor cells most upregulated senescent markers in whole tumors lysates, as
treatedwiththerapy-inducedsenescence(TIS).Cancercells,that detected by western blot analysis1,21 (Fig. 1c, Supplementary
have entered TIS can, in fact, escape the senescent growth arrest Fig. 1a). Between the different identified clusters, clusters 3, 4, 5,
and acquire more aggressive phenotypes associated with and 7 showed the higher expression levels of this senescence
increasedstemnessanddrugresistance8,9.Moreover,theSASPof signature (Supplementary Fig. 2e). Of note, while cluster 3, 4, 5
senescent tumor cells can promote the proliferation and migra- defined luminal prostate tumor cells, cluster 7 represented basal
tion of neighboring tumor cells. Thus, the selective removal of prostate tumor cells, thereby demonstrating that senescence can
senescentcells,knownassenolytictherapy,hasbeenproposedas equally occur in cells of both compartments (Supplementary
astrategytoimprovetheefficacyofcurrentlyavailabletreatments Fig.2b).Amajorfeatureofsenescenttumorcellsistheabsenceof
in tumors where immunosuppression hinders the clearance of cellular proliferation, being these cells stably arrested1,2,21,22. By
senescent cells3,6,10. However, several reports examining the using different available gene sets (K, R, WP), through single-
effectivenessofdifferentsenolyticagentsincombinationwithTIS sampleGeneSetEnrichmentAnalysis(GSEA)wefurtherdefined
in cancer models have raised significant issues and potential threecellcyclearrestsignatures(Fig.1d,SupplementaryFig.2f).
concerns. Navitoclax, a BH3 mimetic that binds and neutralizes The combination of the senescence signature (Fig. 1c) with each
Bcl-2 and Bcl-xL, is the most promising of this class of ofthethreecellcyclearrestsignaturesallowedustodefinethree
compounds11–13.However,theefficacyofNavitoclaxdependson
different Senescence Scores (SK, SR, SWP) (Fig. 1e, Supplemen-
the genetic background of the senescent tumor cells, being only taryFig.2g).Wedefinedsenescentcancercellsasthecellshaving
partiallyeffectiveinsometumortypes.Moreover,Bcl-2inhibitor the highest score level in SK, SR, and SWP (Senescence Index
treatment is associated to severe toxicity that limits their clinical Tool,namedSITforshort)(Fig.1f).Tovalidatethereliabilityof
application when used either alone or in combination with the SIT, we next investigated the differences between senescent
TIS6,13–16.
Single-cell RNA-sequencing (scRNA-seq) technology and non-senescent prostate tumor cells at gene expression level.
hascreatedunprecedentedopportunitiestosimultaneouslyassess GSEA of the biologicalprocesses from GeneOntology collection
thousands of cells within a sample, enabling the evaluation of revealed selective activation and suppression of different path-
heterogeneity among tumor cells17,18. Furthermore, scRNA-seq ways. Within the pathways with higher normalized-enrichment-
provides unique opportunities to assess the regulation, evolution score(NES),severalwererelatedtowoundhealingandmigration
and interaction of individual cells and the identification of spe- (locomotion,cellmotility,epitheliummigration,tissuemigration),
cific cell types17,19. Although scRNA-seq has been increasingly all features characteristic of senescent cells1,5,7. On the contrary,
adopted, its application to senescence in cancer is still limited. oxidative phosphorylation and mitochondrial respiration were
Inthispaper,weshowthatscRNA-seqisareliableapproachto themostdown-regulatedpathways,inlinewithpreviousreports
define, characterize, and identify common vulnerabilities in demonstrating that senescent cells have dysfunctional mito-
senescenttumorcellsofdifferentgeneticbackgroundstodevelop chondria and rely for their survival on the tricarboxylic acid
morespecificsenolyticstobeusedincombinationwithstandard cycle23–25 (Fig. 1g, Supplementary Data 1). Differential expres-
of therapy in future clinical trials. In this work by using single sion analysis between senescent and non-senescent prostate
cells analysis, we find that senescent prostate tumor cells are tumor cells showed that genes involved in transcription regula-
heterogenous, but rely on common pro-survival pathways. tion, wound healing, SASP and oxidative phosphorylation were
Interestingly,wefindthattheMyeloidCellLeukemia1(Mcl-1)is the most regulated (Fig. 1h, Supplementary Data 1). Among
the most expressed anti-apoptotic gene in senescent tumor cells, genes involved in transcriptional regulation, we found c-Jun, a
beingoverexpressedeveninBcl-2-negativesenescentcancercells. pioneer transcription factor recently described as a master reg-
In line with these findings, pharmacological inhibition of Mcl-1 ulatorofsenescence,andadditionalgenesencodingproteinsthat
eliminates senescent prostate tumor cells, blocking tumor pro- heterodimerize with c-Jun to form AP-1 complex, such as c-Fos
gression and metastases. andAtf326(Fig.1i–k,SupplementaryFig.2h).Accordingly,AP-1
downstream target genes were significantly upregulated in
senescentcells(SupplementaryFig.2i).Finally,weobservedthat
Results senescent tumor cells overexpressed gene signatures involved in
Identificationofsenescentprostatecancercellsacrossdifferent autophagy, NF-kB pathways activation, the SASP and previously
mousemodels.Tocharacterizesenescentprostatecancercellsat validated senescence signatures, such as Fridman_senescence_up
single-cell resolution we collected the epithelial fraction of four (SupplementaryFig.2j).RelA/p65,asubunitofNF-kBandakey
prostate tumors from two different mouse models of prostate regulator oftheSASP27,28,wasthemostupregulated geneofthe
cancer, the Pten-null prostate conditional
(Ptenpc−/−
) and NF-kB pathway, whereas Cxcl1, Il6, Il1a and Cxcl15 were the
the Ptenpc−/− ; Timp1 −/− mouse models6,20. These mice most enriched SASP genes, in line with previous data from our
develop prostate tumors that evolve into locally invasive and anddifferentresearchteams5,27,28(Fig.1l–o).Moreover,different
2 NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications
a
0.2
.0.1
out-of-clustering methods, such as scmap and SingleR29,30 using Senescent tumor cells differently segregate at single-cell RNA-
12 different senescent datasets (from both available single cells seqlevelbasedontheirtranscriptionalprofile.Wethenapplied
and bulk RNA seq, Supplementary Table 1) validated the con- theSITtoexplorethepotentialheterogeneityofsenescenttumor
sistence of our tool (Supplementary Fig. 3a–f). Taken together, cells and we found that these cells clustered in eight distinct cell
these data demonstrate that the SIT is a reliable tool to identify subpopulations, regardless of the genetic background (Fig. 2a).
senescent tumor cells at single-cell level. Differential expression analysis of these eight subpopulations
TW
-/-cpnetP
-/-cpnetP
; -/-1pmiT
c
Pten pc-/-
Pten pc-/- ; Timp1 -/-
FACS
SORTING
Epcam + cells
LIBRARY
PREPARATION
Sequencing
DATA
PROCESSING
UMAP_1
2_PAMU
Transcriptomic profiles for 4000 cells
ACTIVATED SUPPRESSED
m tis o s v u e e m d e e n v t e o lo f p c m el e l n o t r subcellular component NES 2
l l o o c c a o l m iz o a t t i i o o n n of cell 0
cell motility
biological adhesion -2
cell adhesion
regulation of cell cycle
regulation of locomotion
epithelium migration
tissue migration
response to wounding
negative regulation of ERK1 and ERK2 cascade
response to mechanical stimulus
circadian rhythm
ribonucleotide biosynthetic process
ATP synthesis coupled proton transport
energy coupled proton transport, down electrochemical gradient
mitochondrial respiratory chain complex assembly
oxidative phosphorylation
respiratory electron transport chain electron transport chain
mitochondrial ATP synthesis coupled electron transport
ATP synthesis coupled electron transport
ATP metabolic process
oxidation-reduction process
0 20 40 60 80 20 40 60 80
Significance
Cxcl1
Cxcl2
Csf1
Il6
Cxcl13
Not senescent Senescent Cxcl10
J J u u n nb Icam1 Avera 0 g . e 8 Expression Fosb Ccl2 0.4 0.0 E S g o r x 1 9 Cxcl15 - - 0 0 . . 8 4 S K o lf4 x4 Ccl20 Perce 5 n 0 t Expressed Foxp1 60
Irf9 Vegfa 70
80
90 Inhba 100
migration
Ier2 TF Il1a
Sdc4 Oxydative phosphorylation
Thbs1 SASP Bmp2 Lmna Senescence Cd44 A W P o I u -1 n d T i F ng family Gdf15
Cldn4 Dst Tgfb1
Pdgfa
Uqcrq Nfkb1 Cox7c
F P t r h d 1 x6 Senescent cells Not Senescent cellsSenescent cells
Not Senescent cells
leveL
noisserpxE
5 4
3
2
1
0
Atf3
0.10
0.05
0.00
-0.05
erocs avsg-ss
p65
0.6 0.4 0.2 0.0
SASP score
leveL noisserpxE
REACTOME_SENESCENCE_ ASSOCIATED_SECRETORY_PHENOTYPE
pvalue = <2e-16 pvalue = <2e-16
0.4
0.3
0.2
0.1
erocs avsg-ss
Jun
leveL noisserpxE
d
e g
f
i j Egr1 o
h
k l
4
3 High 2 1 0
Low m n
z-score
4
3
2
1
0
leveL
noisserpxE
5
0
-5
-10 0 10 20
UMAP_1
Senescence Index Tool (SIT)
Senescent cells Not Senescent cells
2_PAMU
Senescence_signature
5
0
-5
-10 0 10 20
UMAP_1
2_PAMU
Cell_cycle_arrest_signatureR
-0.2
-0.4
5
0
-5
-10 0 10 20
UMAP_1
2_PAMU
Senescence_scoreR
1.9
0
5
0
-5 -10 0 10
UMAP_1
2_PAMU
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
b
0
NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications 3
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
Fig.1Overviewoftheidentificationofsenescentcellsinprostatecancer.aRepresentativeimagesofSA-β-GalinWT,Ptenpc−/−andPtenpc−/−;Timp1−/−
genotypes(Scalebar300μm).Dataarerepresentativeoftwoindependentexperiments.bSchematicrepresentationofsinglecellsisolationandsequencing
(n=4mice).cUMAPplotofcancerepithelialcellscoloredbySenescence_signature.dUMAPplotofcancerepithelialcellscoloredby
Cell_cycle_arrest_signatureR.eUMAPplotofcancerepithelialcellscoloredbySenescence_scoreR.fUMAPplotofcancerepithelialcellsshowingsenescent
cells(blue)andnotsenescentcells(orange)foundthroughSIT.gBarplotshowingenrichmentpathwayanalysisofsenescentcellscomparedtonot
senescentcells.gseGOfunctionresults:WeightedKolmogorovSmirnov(WKS)testfollowedbyFDRcorrection.hHeatmapofdifferentiallyexpressedgenes
betweensenescentandnotsenescentcells.Rowannotationshowingthefunctionsofdifferentgenes(migration,SASP,wounding,TF).WilcoxonRankSum
testfollowedbyFDRcorrection.iViolinplotofthemostupregulatedgeneinsenescentcells:Jun.j,kViolinplotofkeytranscriptionfactorsinvolvedin
senescencetranscriptionalprogram:Egr1,andAtf3.lViolinplotshowingexpressionofp65/RelAinsenescentcells.mBoxplotshowingtheSASPscoreof
senescentandnotsenescentcells(twosidedWilcox-test:pvalue<2.2e−16;N=3992cells,Notsenescentcells(left)minimum=−0.0537,lower-
quartile=−0.0146,median=−0.0088,upper-quartile=−0.0039,maximum=0.0408,Senescentcells(right)minimum=−0.0353,lower-
quartile=0.0018,median=0.0154,upper-quartile=0.0466,maximum=0.1172).nBoxplotshowingss-gsvascoreofpublishedgenesetofReactome
collection77(senescence_associated_secretory_phenotype)insenescentandnotsenescentcells(twosidedWilcox-test:pvalue<2.2e−16;N=3992cells,
Notsenescentcells(left)minimum=0.0634,lower-quartile=0.1183,median=0.1363,upper-quartile=0.1607,maximum=0.2952,Senescentcells
(right)minimum=0.0527,lower-quartile=0.1527,median=0.2183,upper-quartile=0.2768,maximum=0.4215).oExpressionoffundamentalSASP
geneswheredotsizeandcolorrepresentthepercentageofcellexpressingandtheaveragedscaledexpressionvalue,respectively.Sourcedataareprovided
asaSourceDatafile.
outlined commonalities and key differences. Sene_1, Sene_3 and clusters when compared to additional pro-survival genes
Sene_5werecharacterizedbytheover-expressionofdistinctgene (Fig. 3f–h, Supplementary Fig. 4d). Both Bcl2 + Mcl1 + and
− +
expression programs compared to the other populations Bcl2 Mcl1 senescent cells overexpressed genes involved in the
(Fig. 2b–d and Supplementary Data 2). Interestingly, the senes- regulationofangiogenesis,migrationandwereenrichedinSASP
centclustersexpresseddifferentsenescencesignaturesatdifferent genes(Fig.3i,j,SupplementaryFig.4e–g,SupplementaryData3).
levels (Fig.
2e)31–35.
Pathway analysis showed that JAK-STAT, Altogether, these data suggest that the majority of senescent
NF-kB, p53, MAPK and TNFα signaling, known to be upregu- tumor cells rely on Mcl-1 over-expression and that this cell
lated in senescent tumor cells, were mostly activated in the population upregulates gene pathways that may contribute to
Sene_1–5 clusters. Instead, Sene_0 and Sene_6 clusters were tumor progression through different mechanisms.
characterized by the upregulation of WNT and PI3K
patways27,36–42
(Fig. 2f). Interestingly, among the secretome of
Inhibition of Mcl-1 works as a potent senolytic therapy.
the different clusters, we found that Tnf, Cxcl2, Cxcl17, Gas6, Intrigued by these findings, we next checked whether Mcl-1 was
Wnt5a and Tgfb1 were specifically expressed by some of the
also overexpressed in cells treated with drugs that cause TIS.
Sene_clustersbeingundetectableinothers(Fig.2g).Previousdata
Human(PC3,PC3shTIMP1andLNCaP)andmouse(TrampC1,
demonstratedthatCxcl2andCxcl17arekeychemokinesinvolved
TC1,
TrampC1Pten−/−
,
TC1Pten−/−
, and RapidCap) prostate
in the recruitment of myeloid cells, which arethe most enriched
immune population in prostate
cancers43–45.
In sum, these data
t
t
u
o
m
tr
o
ig
r
g
c
e
e
r
ll
a
s
s
w
e
e
n
r
e
e
sc
t
e
re
n
a
t
t
r
e
e
d
sp
w
o
i
n
th
se
D
(
o
F
c
ig
e
.
ta
4
x
a
e
–
l
d
a
,
n
S
d
up
P
p
a
l
l
e
b
m
oc
e
i
n
cl
t
i
a
b
r
,
y
in
Fi
o
g
r
.
d
5
e
a
r
,
revealed that senescent tumor cells are heterogeneous at tran-
b and Supplementary Data 4). Establishment of senescence in
scriptional level.
these cells was associated to Mcl-1 and Bcl2 upregulation (Sup-
plementaryFig.5a,b).ToassesswhetherMcl-1contributedtothe
Mcl-1isthekeyfactorthatantagonizescelldeathinsenescent survivalofsenescenttumorcells,wetreatedthemwithS63845,a
prostate tumor cells. We next focused on common genetic potentMcl-1inhibitor52,53inparalleltotheBcl2inhibitorNavi-
pathways expressed by these cells. Senescent tumor cells are toclax(ABT263)50,51.Ofnote,wefoundthatS63845wascapable
known to be resistant to programmed cell death due to the todrivesenolysismoreefficientlythanABT263,bothintermsof
upregulationofBCL2andBCL-XL1,2,46,47.However,anextensive selectivity and potency, as visualized by SA-β-Gal staining and
analysis of the pro-survival pathways upregulated in senescent quantification of proliferation by crystal violet and Incucyte
prostatetumorcellshasnotbeenperformedbefore.Wetherefore imaginganalysis(Fig.4a–d,SupplementaryFig.5c).Theremoval
tookadvantageoftheSITtoannotatepro-survivalgenepathways of senescent cells by S63845 was accompanied by apoptosis as
deregulatedinsenescentprostatetumorcellsinordertoidentifya shown by upregulation of Cleaved Caspase 3 (Supplementary
common vulnerability (Fig. 3a). We found that senescent tumor Fig. 5d). These data were further validated by using two addi-
cells upregulate pathways involved in necroptosis and apoptosis. tional inhibitors of Mcl-1, UMI77 and AZD599154,55 (Supple-
Byseparatinggenesinvolvedinpro-apoptoticandanti-apoptotic mentary Fig. 5e–h). Interestingly, after ABT263 treatment we
pathways,wefoundthatthelatterweresignificantlyupregulated foundapopulationofABT263resistant(ABT263R)cellsthatwas
in senescent tumor cells (Fig. 3b, c). Among the identified pro- still SA-β-Gal positive, whereas S63845 treatment resulted in a
survival genes (n=47) (Supplementary Fig. 4a), we found 12 smaller fraction of surviving senescent tumor cells (S63845R)
genes that positively correlated (Pearson’s coefficient>0.4) with (Fig.4a,c).WenextcheckedwhetherABT263Rhumancellsalso
the senescence scores (SK, SR, SWP). Among these, Mcl-1, a expressed Mcl-1. RT-qPCR analysis confirmed that ABT263R
member of the BCL2 gene family, was the most correlated cellsupregulatedMcl-1whereasS63845Rcellsdidnot(Fig.4e,f).
gene48,49 (Fig. 3d, Supplementary Fig. 4b). Of note, Mcl-1 was We next used an inducible shMCL1 in LNCaP and RapidCap
more upregulated than Bcl2, a well-known target of senolytic cellstovalidateMcl-1assenolytictarget(SupplementaryFig.5i).
therapy50,51(SupplementaryFig.4c).Wenextclassifiedsenescent Doxycycline administration efficiently decreased the levels of
tumor cells in two subpopulations based on Bcl2 expression Mcl-1 in both cell lines (Supplementary Fig. 5j, m). Of note,
(Bcl2 + and Bcl2 − ) (Fig. 3e). Surprisingly, we found that roughly inactivation of Mcl-1 in cells treated with TIS efficiently elimi-
50% of senescent tumor cells were not expressing Bcl2 at high nated senescent tumor cells (Supplementary Fig. 5k, l, n, o). In
+
levels. On the contrary, Mcl-1 was expressed both in the Bcl2 cellstreatedwithDoxycycline and S63845alone,theelimination
−
andBcl2 clustersanditwasthemostupregulatedgeneinthese of senescent cells was comparable (Supplementary Fig. 5l, o).
4 NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications
5
0 -5 -4 0 4
UMAP_1
However, in cells treated with Doxycycline and S6384 in com- Thus, we took advantage of this model to assess whether
bination, we did not find an increased percentage of dead cells senescent tumor cells resistant to senolytic therapy could impact
(SupplementaryFig.5l,o).Thesedatademonstratethatsenescent on tumor cells proliferation and migration. In line with our
cellsrelyonMcl-1fortheirsurvivalandthatS63845isaspecific previous findings6, while condition media (c.m.) from senescent
Mcl-1 inhibitor. PC3 shTIMP1 cells treated with Docetaxel increased the
2_PAMU
2 1 0 -1 -2 Sene_0 Sene_4 Sene_1 Sene_5 Sene_2 Sene_6
Sene_3 Sene_7
noisserpxE
Sene_2
Sene_1
51
300 30
34 Sene_3
92
Sene_7
40 15 332
6
5 48
53 91
7 16
3 7 169
31 2 136 28 1 96 Sene_4 Sene_6 239 Sene_5
1.00
0.75 5 0.50
0.25
0.00
0
-5
-8 -4 0 4
UMAP_1
2_PAMU
Tnf
5 1.0
0.5
0
-5
-8 -4 0 4
UMAP_1
2_PAMU
Gas6
5 0 0 . . 4 5 0.3 0.2
0.1 0
-5
-8 -4 0 4
UMAP_1
2_PAMU
Tgfb1
5 0 0 . . 5 7 0 5 0.25
0.00 0
-5
-8 -4 0 4
UMAP_1
2_PAMU
Wnt5a
5 1.00 0.75 0.50
0.25 0
-5
-8 -4 0 4
UMAP_1
2_PAMU
1.0 5
0.5
0
-5
-8 -4 0 4
UMAP_1
Cxcl17
2_PAMU
a b c Sene_0 Sene_1 Sene_2 Sene_3 Sene_4 Sene_5 Sene_ S 6 ene_7
Senescence_scoreK Senescence_scoreR Senescence_scoreWP 2 1.8 1.6 1.4 1.2 1 0.8
e
0
0
0
f
Cxcl2
Trail
WNT
Estrogen
PI3K
TGFb
EGFR
MAPK
VEGF
NFkB
TNFa
Androgen p53
Hypoxia
JAK-STAT
Sene_ S 0 ene_1 Sene_2 Sene_3 Sene_ S 4 ene_5 Sene_ S 6 ene_7
Not
sene S s e c n e e n s t cent
erocS JJBSICNZKAPHPCHTTITCARTDPPSHGSZKPSNDSSNBIREAPCSSBIJAAZIDDCPSPSSKTTCAHMTVPMEIRHNAADCH e t
d f t
q uu
u
c c
a
g
r g
p h
f n
f f
p e
l f
l
l i
c
t k mu
t r
to n b fo i ipa ogt
n ld d n i f pn
p k c te a o d s iy f h d
ssx d b tif c s
n r
e
a
y a
r
1
g f
f
k k
pd
p p r f
e k
p
f
n r
p
g p
g n
n e
s n e
i f 4 nn
n c
b
a
4
5
r
t
3 b i
fm
4 n
g
n p n
tpa 1 n p
c r n k x x pf xk
x c c x ox
m px s s c x o k
9 e
r
a
7
h
d 2 1 l
c3
a
b31 r
3 3
c
t b
f r
2 q a
1 b
n a 2
4 2 s
n a b
d
1
v
6 s r 1 4 91
a 1 4 a a
g 2
f
l 1 t k 3 a 2 c n
d 5 s a b e
1 b
f g c
l
9 f
d
c
p 1
1 6
6 6
a
l d 2
t
h
2
b l
l 1
p 1 1 2 1
f 1 2 3
1 x 1 e 1 1
r 2 1a d
r
f 2
4 1
1
l l 1 1 1 1u 1 2 h b a
m 2 a
5
2
7 b 0 1 b
a 1
1
d
noitomocol
gnidnuow ot esnopser noitargim eussit
Sene_0 Sene_1 Sene_2 Sene_3 Sene_4 Sene_ S 5 ene S _ e 6 ne_7
Cell fracion (%) 0 25 50 75 100 Ptenpc-/- Ptenpc-/-;Timp1-/-
Sene_7
Sene_6
2
1
Sene_5 0
-1
Sene_4 -2
Sene_3
Sene_2
Sene_1
Sene_0
Casella_sign H a e tu rn re amdez_ F s R ig ID n M at A ur N e _S R E E N A E C S T C O E M N E C _ E N C _ D E U R U L P L E C U A E L C D A T _ R O S _ E M S N E E E _ N B S O E a C N s S E i C C s N t O E y C _ G N E s E C ig N E n G E a O _ tu B re P_CELLU P L u A rc R e _ ll_ S s E ig N n E a S tu C re ENCE
z-score
noisserpxE
egarevA
desserpxE
tnecreP
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
0
25
50
75
100
g
1 0 -1
NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications 5
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
Fig.2Senescentcellsareaheterogeneouspopulation.aUMAPviewofonlysenescentcells,coloredbyclustersfoundwithFindClusterfunction
(res=0.5)(top)andpercentageofclustersinthetwogenotypes(bottom).bHeatmapshowingexpressionofdifferentiallyexpressedgenesfoundintotal
senescentcellsrelatedtopathwaysactivatedintotalsenescentcells.cHeatmapshowingdifferentiallyexpressedgenesbetweenvarioussenescent
clusters(Sene_clusters)usingFindAllMarkerfunction.WilcoxonRankSumtestfollowedbyFDRcorrection.dVenndiagramsshowingthedifferentially
expressedgenesineachSene_cluster.Overlappingareasindicatethenumberofgenescommonlymodulatedamongsubpopulations.Thenumbersreport
onlyuniquedifferentiallyexpressedgenesortranscriptscommonbetweentwoclusters.eDotplotshowingssGSEAofpreviouslypublishedsenescence
signature(Casella_signature31,Hernandez_signature32,Fridman_senescence_up33,Basisty_signature34,Purcell_signature35,Cellularsenescencefrom
GeneOntologycollection,Oncogene-inducedsenescenceandCellularsenescencegenesetsfromReactomecollection)inallthesenescentclusters.
fHeatmapshowingpathwayactivityof14relevantsignalingpathwayscalculatedusingPROGENy80betweendifferentsenescentsubpopulations(left)and
betweensenescentandnotsenescentcells(right).gFeaturePlotshowingexpressionlevelsofdifferentsecretedfactorsupregulatedinspecific
Sene_clustersandnotexpressedintheothersenescentcells.SourcedataareprovidedasaSourceDatafile.
migration and proliferation of parental PC3 cells, c.m. from in the expression levels of genes involved in metastases in mice
S63845 treated cells completely arrested the proliferation and treated with Docetaxel and S63845 was further validated by RT-
migration of PC3 parental cells. This effect was superior to the qPCR in whole tumor lysates (Supplementary Fig. 7c, d). These
one observed in cells treated with ABT263 (Fig. 4g–j). Intrigu- data were further validated in Ptenpc−/− mice (Supplementary
ingly,co-cultureexperimentsusingDocetaxeltreatedGFP + -PC3 Fig. 8a). Mice treated with the combination of Docetaxel+
ShTIMP1 cells and untreated parental PC3 showed that a small S63845 showed a marked reduction in the number of prostate
fraction (15%) of senescent cells was capable to migrate. glands affected by tumors when compared to mice treated with
However, this was not observed in S63845 treated cells DocetaxelandDocetaxel+ABT263(SupplementaryFig.8band
(Supplementary Fig. 6a–e). The effect on proliferation enhance- SupplementaryFig.9a).Next,weevaluatedtheefficiencyofboth
ment induced by c.m. derived from senescent cells was further S63845 and ABT263 in eliminating senescent cells in these
validated in Tomato + -RapidCap cells treated either with c.m. or tumors. Immunohistochemistry analysis for p16, SA-β-Gal and
co-cultured with untreated parental cells. Also, in this case RT-qPCR for p21 and PAI-1 showed a reduction of senescent
S63845 treatment was superior to ABT263 (Supplementary cells in mice treated with both S63845 and ABT263 (Supple-
Fig. 6f–n). In sum, these data demonstrate that senescent tumor mentary Fig. 8c–e). However, S63845 had a stronger senolytic
cells treated with TIS can migrate and induce the proliferation effect and promoted a stronger apoptotic response when
and migration of neighboring prostate tumor cells. These pro- compared to ABT263. Decrease in senescence markers was
tumorigenic effects can be efficiently abrogated by senolytic accompanied by MCL-1 and BCL2 reduction (Supplementary
therapy with S63845. Fig. 8e). Treatment with S63845 and ABT263 also decreased the
number of tumor infiltrating MDSCs and TAMs, the two most
Mcl-1 inhibition enhances the efficacy of standard of therapy represented immune populations in prostate tumors character-
inprostatecancer.Tofurthercorroboratethesefindingsinvivo, ized by loss of PTEN46,56 (Supplementary Fig. 8f, g and
Supplementary Fig. 9b).Interestingly, wealsodetected a marked
we subcutaneously injected PC3 Luc-shTIMP1 in NRG mice. As
upregulation of Perforin, a marker of T and NK cells activation
previously shown, PC3 Luc-shTIMP1 tumor cells can migrate,
(Supplementary Fig. 8h).
invade the surrounding tissues and metastasize upon TIS due to
the increased activity of MMPs6. When tumors reached the
volumeof100mm3,miceweretreatedwithDocetaxelfollowedby Discussion
eitherS63845orABT263treatments(Fig.5a,b).WhileDocetaxel The mechanism behind cellular senescence establishment,
increased senescence in primary prostate tumors, S63845 treat- maintenance and survival remains an object of intense
ment promoted an efficient elimination of senescent prostate investigation1,2. Indeed, contrary to cell death, whose mechan-
tumorcells,asassessedbySA-β-GalandMCL-1positivecellsand isms of induction have been fully characterized, little is known
the increased positivity for Cleaved Caspase 3 (Fig. 5c, d). Note about the mechanism by which tumor cells undergo senescence
that S63845 treatment was more effective than ABT263 in elim- and remain alive in the tumor microenvironment. Recent data
inating senescent tumor cells. demonstrate that senescent tumor cells, which initially suppress
Importantly, while mice treated with Docetaxel developed tumor growth7,57,58, if not promptly removed by the tumor
metastases to the lungs and the liver, mice treated with the immune response, can promote the proliferation, migration and
combination of Docetaxel and S63845 showed a stronger metastatization of bystander
cells1,4–6.
These effects have been
reduction in metastases formation. This effect was superior than ascribed to the SASP of the senescent tumor
cells1,4–6.
Indeed,
in mice treated with Docetaxel in combination with ABT263 although arrested, senescent cells can secrete in the tumor
(Fig. 5e, f). 10× Genomics bioinformatic analysis using SIT in microenvironment a variety of factors that can stimulate non-
primary senescent prostate tumors cells showed that S63845 senescent tumor cells to migrate or proliferate6,10,12,21. As
treatment resulted in a stronger elimination of senescent tumor recently shown, the genetic background of tumor cells can
cells when compared to ABT263 treatment (Fig. 5g, Supplemen- influence the SASP, that determines whether these cells act in
tary Fig. 7a). Of note, in prostate tumor treated with Docetaxel tumor-suppressive or tumor-promoting processes5,12,22,49,59. By
and ABT263, the remaining senescent tumor cells upregulated using single cell technology, we have now contributed with an
MCL-1 and genes related to angiogenesis, cell migration and additional piece of information to these previous findings,
wound healing (Fig. 5h, i, Supplementary Fig. 7b). Moreover, demonstrating that in tumors of the same genetic backgrounds,
these senescent tumor cells co-existed with a population of non- senescent tumor cells can be heterogeneous in terms of gene
senescent cells that were more proliferative and pro-migratory expression. This can pose challenges for the design of therapies
than in tumors treated with Docetaxel and S63845 (Fig. 5j–l). thatremovesenescenttumorcellsandforthefuturedevelopment
This explains the reduction in Ki67 staining and the decreased of senolytics in clinical trials.
number of metastases found in mice treated with S63845 Most of the currently available senotherapies for cancers are
(Fig. 5c–f). Elimination of senescent tumor cells and reduction still restricted to Bcl-2 targeting2,3,50,51. Here, we describe a
6 NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications
Bcl2 Cflar
Bcl2l1
Mcl1
Ptpn13 Gadd45a
Birc3
Bcl2l11
Bbc3
Apaf1
Pmaip1
Trpm7
Ripk1
Map1lc3a
Lpcat3
Gpx4 Vdac2
Ncoa4
Gclc
Parg
ANTI_APOPTOSIS
PRO_APOPTOSIS NECROPOPTOSIS
FERROPOPTOSIS
PARTHANATOS
10.0
7.5 5.0 2.5
24Bc6l2810
population of senescent tumor cells that do not rely on Bcl-2 to Mcl-1 is a BH3 protein that belongs to the BCL2 family, which
survive. This population of cells upregulates Mcl-1 and after controlsapoptosistogetherwithBcl-2,Bcl2-L-10,Bcl-WandBcl-
treatment with the Bcl-2 inhibitor Navitoclax, remains still cap- xL. Mcl-1 has a different structure compared to the other
able to promote tumorigenesis through the SASP. Thus, regard- members of the BCL2 family60. While ABT263 can efficiently
lessofsenescenceheterogeneity,ouranalysisidentifiedMcl-1asa block Bcl-2 and Bcl-xL, it cannot block Mcl-160. On the other
ubiquitous target to effectively remove senescent tumor cells. hand,secondandthirdgenerationofMcl-1inhibitorsarehighly
1lcM
5
0
-5
-8 -4 0 4
UMAP_1
2_PAMU
5
0
-5
-8 -4 0 4 UMAP_1
Bcl2 - cells 5 Bcl2 + cells
0
-5
Bcl2_Mcl1
2_PAMU
Bcl2
Ptpn13 Mcl1
0.3 Birc3 0.2 Cflar 0.1 0.0 Bcl2l11
Apaf1
Pmaip1 Bbc3
Trpm7
Ripk1
Gclc
1.0
0.5
0.0
noisserpxe_ANRm
Not senescent Senescent
Bcl2 + cells Bcl2 - cells
1.5
1.0
0.5
0.0
0.4 0.8 1.2
Senescence_scoreK
noisserpxe
ANRm
seneG
c
hgiH woL
z-score
d e f
Ptpn13 Bcl2
Mcl1 Birc3 Cflar
Apaf1
Bcl2l11 Pmaip1
Bbc3
Trpm7
Ripk1 Gclc
g
h
1.5
1.0
0.5
0.0
noisserpxe_ANRm
Bcl2 Ptpn13 Mcl1 Birc3 Cflar Bcl2l11 Apaf1 Pmaip1 Bbc3 Trpm7 Ripk1 Gclc
ANTI_APOPTOSIS
PRO_APOPTOSIS NECROPOPTOSIS FERROPOPTOSIS
j
-8 -4 0 4
UMAP_1
i
2_PAMU
2lcB
a b
Pro-apoptotic pathway
0.4
0.3
0.2
0.1
0.0
Apoptotic pathway Anti-apoptotic pathway
0.5
0.4
0.4
0.3
0.3
0.2
0.2
negative regulation of proteolysis
Bcl2 - cells germ cell development
developmental maturation
anatomical structure maturation negative regulation of peptidase activity
spermatid differentiation
spermatid development
cell maturation
fertilization
sperm capacitation negative regulation of immune system process
regulation of immune effector process negative regulation of protein phosphorylation myeloid cell differentiation
negative regulation of nervous system development n p e o g s a i t t i i v v e e r r e e g g u u l l a a t t i i o o n n o o f f n a e n u g r i o o g g e e n n e e s s i i s s p.adjust negative regulation of cell development 0.020
threonine kinase signaling pathway regulation of epithelial cell migration 0.015
positive regulation of vasculature development
multicellular organismal homeostasis 0.010
gland development
regulation of hemopoiesis 0.005 regulation of cell-cell adhesion regulation of angiogenesis
positive regulation of cell projection organization
positive regulation of establishment of protein localization
muscle organ development
regulation of binding
Bcl2 + cells regulation of supramolecular fiber organization
regulation of vasculature development positive regulation of cellular protein localization tissue migration epithelium migration
epithelial cell migration regulation of cell growth
negative regulation of hydrolase activity cell junction assembly
regulation of actin cytoskeleton organization symbiotic process
reproductive system development
synapse organization
reproductive structure development
cellular response to drug positive regulation of cell adhesion
negative regulation of phosphorylation
regulation of peptidase activity
muscle cell differentiation
positive regulation of catabolic process
regulation of cellular component size
wound healing intrinsic apoptotic signaling pathway response to inorganic substance
mitochondrion organization
actin filament organization regulation of actin filament-based process
regulation of epithelial cell proliferation
striated muscle tissue development
ameboidal-type cell migration
RNA splicing epithelial cell proliferation
response to wounding muscle tissue development
mRNA processing
regulation of apoptotic signaling pathway
Bcl2+Mcl1+ Bcl2-Mcl1+ Bcl2-Mcl1- Bcl2+Mcl1-
erocs
avsg-ss
erocs
avsg-ss
erocs
avsg-ss
erocs
avsg-ss
erocs
avsg-ss
erocs
avsg-ss
erocs
avsg-ss
Ferropoptosis pathway Necroptosis pathway Parthanatos pathway
0.4 0.6
0.3 0.5
0.5
0.2 0.4
0.4 0.1 0.3
0.0 0.2
0.3 -0.1 0.1
Pyroptosis pathway
0.0
-0.1
-0.2
Senescent cells
-0.3 Not Senescent cells
-0.4
5
0
-5 Bcl2+ Mcl1+
Bcl2+ Mcl1-
Bcl2- Mcl1+
Bcl2-Mcl1-
-4 0 4
hgiH woL
z-score
UMAP_1
2_PAMU
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications 7
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
Fig.3Survivalmechanismsofsenescentcells.aViolinplotshowingss-GSVAscoreactivationofdifferentcelldeathmodalitiesbetweensenescentand
notsenescentcells.bViolinplotshowingss-GSVAscoreactivationofapoptosisbetweensenescentandnotsenescentcells,separatinginproandanti-
apoptoticgenes.cHeatmapof20differentiallyexpressedgenesofdifferentcelldeathmodalities.FDR<0.05.dCorrelationplotbetween
Senescence_scoreKandsurvivalrelated-geneswithPearsoncorrelationcoefficienthigherthan0.4andFDR<0.05.eUMAPplotshowingBcl2expression
levelsinsenescentcells(top)andclassificationoftheminBcl2+orBcl2-(bottom).fHeatmapshowingz-scoreexpressionlevelsof12survivalrelated-
genes,positivelycorrelatedwithSenescence_scoreK,WP,R,inBcl2+andBcl2-senescentcells.gmRNAexpressionlevelsof12survivalrelated-genesin
Bcl2+andBcl2-senescentcells(N=862cells,Bcl2-cells:Bcl2median=0.0596;Ptpn13median=0.1857;Mcl1median=0.654;Birc3median=0.234;
Cflarmedian=0.160;Bcl2l11median=0.140;Apaf1median=0.068;Pmaip1median=0.165;Bbc3median=0.091;Trpm7median=0.331;Ripk1
median=0.169;Gclcmedian=0.175.Bcl2+cells:Bcl2median=0.169;Ptpn13median=0.324;Mcl1median=1.045;Birc3median=0.274;
median=0.314;Bcl2l11median=0.145;Apaf1median=0.083;median=0.178;Bbc3median=0.113;Trpm7median=0.402;Ripk1median=0.261;
Gclcmedian=0.179).hCo-expressionofBcl2andMcl1insenescentcells.iUMAPplotshowingtheclassificationofsenescentcellsbasedonBcl2and
Mcl1expressionlevels.jDotplotshowingover-representationresultsofbiologicalprocess(GO)pathwayanalysisbyconsideringsenescentcell
subclassification.HypergeometrictestfollowedbyFDRcorrection.SourcedataareprovidedasaSourceDatafile.
selectiveandnowadaystheyareusedinsomeclinicaltrials61.We culturedaccordingtothemanufacturer’sinstructions.CellswereculturedinRPMI
show that the efficacy of Docetaxel treatment, a standard of 1640supplementedwith10%FBSand1%P/S.HEK-293T(humanembryonic
therapy for metastatic castration-resistant prostate cancer
kidneys,Cat.NCRL-3216™)andTrampC1(Cat.NCRL-2730™)cellswereobtained
fromATCC.RapidCapwereobtainedfromTrottmanlaboratory63.Cellswere
patients, can be enhanced by the concomitant administration of
culturedinDMEMsupplementedwith10%FBSand1%P/S.Allcelllineswere
Mcl-1 inhibitors both in vitro and in vivo. Furthermore, treat- keptundercontrolledtemperature(37°C)andCO (5%)andusedforexperiments
2
ment with different Mcl-1 inhibitors resulted in the effective atearlypassages.AllthecelllinesweretestednegativeforMycoplasma
removalofsenescenttumorcellsandthecompleteabrogationof (MycoAlertTMmycoplasmadetectionkit,LT07-418,LONZA).
thebystandermigratoryphenotype,orchestratedbytheSASPon
non-senescent tumor cells, both in transgenic and xenograft Invitrotreatments.Palbociclibwasusedattheconcentrationof10μM;Docetaxel
models.Moreover, thiscombinationof compoundswas superior
wasusedat1nM;ABT263wasusedatthedosageof2.5μM;S63845wasusedat
in terms of efficacy to the combination of Docetaxel with
10μM;UMI-77wasusedat10μM;AZD5991wasusedat10μM.
ABT263.Ofnote,inthetransgenicmousemodel,eliminationof
GenerationofshTIMP1humanprostatecancercellline.PC3celllinewas
senescenttumorcellswasassociatedtoreactivationofthetumor
transfectedwithshRNAusingthehumanTIMP1-directedshRNARHS4430-
immuneresponseasdemonstratedbythedecreasedinfiltrationof
200284918-V3LHS_317110.Topreparelentiviralparticles,HEK-293Tcellswere
MDSCs and upregulation of perforin, a marker of T cells transfectedusingJetPRIMEtransfectionreagents(JetPRIME,Polyplustransfection,
activation. 114-07/712-60)asperthemanufacturer’sinstructions.PC3cellswereinfectedwith
thefilteredlentiviralsupernatantobtainedfromtransfectedHEK-293Tcells.
Insum,senescentcellsarehighlyheterogenous,butultimately
InfectedhumanprostatecancercellsweresubsequentlyselectedusingPuromycin
rely on a common pro-survival factor, Mcl-1. Importantly, this
(3mg/ml).
study endorses Mcl-1 inhibitors as a class of highly effective
senolytics. Interestingly, a previous study on breast cancer GenerationofPten−/−TrampC1murineprostatecancercellline.TrampC1cells
showed that the senolytic sensitivity of ABT263 is controlled by werepurchasedfromATCCandculturedaccordingtomanufacturer’sinstructions
NOXA,aninhibitorofMcl-162.Whilesenescentcellswithahigh (DMEM,10%heat-inactivatedFBS,100U/mlpenicillin,0.1mg/mlstreptomycin).
level of NOXA respond to ABT263, cells with a low level are ThetransfectionofthePTENCRISPR/Cas9KOplasmid(SantaCruzBiotechnology
sc-422475)wasperformedusingjetPRIME®transfectionreagentaccordingtothe
resistant to ABT263 and respond to Mcl-1 inhibitor thereby manufactoryprotocolattheratioof1:2DNA/jetPRIME®.24haftertransfection,the
validating our results in a different system62. Finally, senescent
GFPtransducedcellsweresortedtopurity99%andplatedassinglecellon96-well
tumor cells share common features with aged cells. Thus, if plates.Atday7aftercellsortingtheresultingcellcoloniesweremovedinto24-well
validatedinothermodels,thesefindingscouldberelevantalsoto platesforfurtherexpansion.
ameliorate aging and age-related pathologies.
GenerationofshMCL-1humanandmurineprostatecancercelllines.LNCaP
Methods andRapidCapcelllinesweretransfectedwithshRNAusingthehumanandmouse
MCL-1-directedshRNARHS4696-200751526andRMM4431-200332978,respec-
Mousemodels.Allmiceweremaintainedunderspecificpathogen-freeconditions
tively.Topreparelentiviralparticles,HEK-293TcellsweretransfectedusingJet-
intheanimalfacilitiesoftheIRBinstitute.Experimentswereperformedaccordingto
PRIMEtransfectionreagents(JetPRIME,Polyplustransfection,114-07/712-60)as
thestateguidelinesandapprovedbythelocalethicalcommittee(“Dipartimentodella
perthemanufacturer’sinstructions.BothLNCaPandRapidCapcellswereinfected
SanitàeSocialità,Esperimentisuanimali”,CantonTicino),authorizationnumber
withthefilteredlentiviralsupernatantobtainedfromtransfectedHEK-293Tcells.
TI-51/2018(Maximumtumorvolumeauthorized=1500mm3,notexceeded).
Prostate-specificPtenpc−/−transgenicmice20werecrossedwithTimp1−/−mice InfectedprostatecancercellsweresubsequentlyselectedusingPuromycin(3mg/ml).
(JacksonLaboratory,6243)togenerateTimp1knockoutinPtenpc−/−6.NRGmale TheshRNAwasactivatedinbothcelllinesaddingDoxycyclineinthecellculture
media(1mg/ml).
mice,at12weeksofage,wereusedforsubcutaneouscellinjectionofPC3shCtrland
shTIMP1.Prostate-specificPtenpc−/−transgenicmalemiceat12weeksofagewere
usedforinvivoexperiments.Miceusedfor10×scRNAsequencingwereeuthanized Immunohistochemistry(IHC).IHCtissuesectionswereprocessedasfollows:
at10weeksofage.NRGmicewere challengedwithPC3shTIMP1at8weeksofage deparaffinizaction,unmasking,pre-staining,blockingsandsecondarystainings.
andthenmonitoredandkeptundertreatmentupto42dayspost-injection.Finally, Deparaffinizationwasperformedusingthree-stepprocedure.Inthefirstandsec-
Ptenpc−/−miceweretreatedat10weeksofageandeuthanizedupon6weeksof ondstep,theslideswereimmersedinOTTIXplussolution(Diapath,CatNo.
treatment. X0076)for5mineachfollowedbythirdandlaststepofOTTIXshapersolution
(Diapath,CatNo.X0096)for5min.Theslidesweredrainedofftheexcesssolution
andwerethenimmersedinionizedwaterfor5min.Further,un-maskingor
Invivotreatments.Docetaxel(TEVAPharmaAG6984894)intraperitoneallyat
antigenretrievalprocedurewasfollowedwhichinvolvedimmersingthesection
10mg/kgonceaweek.ABT263(MedChemExpressHY-10087)byoralgavage
slidesinpHsolutions(dependingupontheantibodies)ateitherpH6(Citrate,
50mg/kg,daily.S63845(MedchemExpressHY-100741)atthedoseof25mg/kgby
Company:Diapath,CatNo.T0050)orpH9(DAKO,CatNo.K800421-2)inwater
oralgavage.Miceweremonitoredforanysufferingofdistressorweightlossby bathat98°Cfor20–25min.Theslideswereallowedtocoolatroomtemperature
measuringweeklytotalbodyweightofmiceandmonitoringthebehavioral for20–25min.Thesectionslideswerewashedwith1xPBST(0.5%Tween20),two
changeseverydayforatotalof4weeksoftreatment.
timesfor3mineach,followedbystainingprocedure.Blockingprocedurebeganby
incubatingtheslideswith3%HO (VWRchemicals,Catno:23615.248)for
2 2
Prostatecancercellculture.PC3andLNCaPhumanprostatecancercellswere 10minfollowedby1xPBSTwashesasbeforeandperformingproteinblock.Pro-
purchasedfromATCC(Cat.NCRL-1435™andCRL-1740™respectively)andwere teinblockingwasperformedusingProtein-Blocksolution(DAKOAgilent
8 NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications
Vehicle S63845
ABT263
S63845
technologies,CatNo.X0909)for10minatroomtemperature.Dependingupon stainingfor30minatroomtemperature.AfterABC,slideswerewashedthree
antibodies,iftheyweredevelopedinmousehost,thetissueswereblockedfor timeswith1xPBSTandfinalstepsofIHCstainingswereperformed.DABstaining
mousecross-reactivityusingbiotinylatedAnti-Mouseantibody(VectorLabora- wasperformedusingDABsolution(Company:Vectorlaboratories,CatNo.SK-
tories,CatNo.BP-9200).Sectionswerestainedwithrespectiveprimaryantibodies 4105.OnedropofChromogenin1mlofDiluentsolution)andallowedtostainfor
atroomtemperaturefor1hfollowedbythreewasheswith1xPBSTasbefore. nomorethan3–4minatroomtemperature.Immediatelyslideswerewashedthree
Theseslideswerefurtherincubatedwithrespectivesecondaryantibodies,Anti- timeswith1xPBSTandcounterstainingwasperformedusinghematoxylinsolu-
Mouse(VectorLaboratories,CatNo.BP-9200),Anti-Rabbit(VectorLaboratories, tion(Diapath,C0303).AttheendofIHCstaining,sectionsweredehydratedusing
CatNo.BP-9100).Duringsecondaryantibodyincubation,VectastainABCsolu- deparaffinizationprocedureafterwhichslidesweremountedwithcoverslipusing
tionwasprepared(Company:Vectorlaboratories,CatNo.PK-6100)atthedilution aqueousmountingmedia(Diapath,060200).Tumortissuesampleswerefixedin
of1:150ofbothSolutionAandSolutionBin1xPBSsolutionfollowedby30min 10%neutral-bufferedformalin(ThermoScientific,CatNo.5701)overnight.Tis-
incubationatroomtemperature.Uponcompletionofsecondaryantibodystain- sueswerewashedthoroughlyunderrunningtapwaterfollowedbyprocessing
ings,slideswerewashedforthreetimeswith1xPBSTfollowedbyABCsolution usingethanolandembeddedinparaffinaccordingtostandardprotocols.Sections
-
ecoD
oblaP
a
PC3 shTIMP1 LNCaP
ABT263 Vehicle S63845 ABT263
-
ecoD
oblaP
c
b d
e f
Docetaxel ABT263R c .m.
Wound healing assay PC3 ShTimp1 S63845R PC3 ShTimp1
Proliferation
g i
c.m. Docetaxel c.m. ABT263R c.m. S63845R
h j
100
50
0
0 6 12 18 24 30 36 42 48
Time (hours)
ecneulfnoc
dnuow
fo
%
Docetaxel Docetaxel
- S63845 ABT-263 - S63845 ABT-263
Palbociclib Palbociclib
- S63845 ABT-263 - S63845 ABT-263
100
80
60
40
20
0 Veh D i o c D c le o e c ta e x S el 6 D 38 o 4 c 5 e P a A l P B b a o T l c b i o c l S ib 6 P 3 a 8 l 4 b 5 o ABT
c.m. Docetaxel c.m. ABT263R c.m. S63845R
p<1e-04
sllec
evitisop
laG
β AS
fo %
p<1e-04
p<1e-04 p<1e-04 p<1e-04 p<1e-04 80 p<1e-04
p<1e-04 p = 0.0241
60
40
20
0 Vehicle D D o o c c e e S D 6 o 3 c 8 e 4 5 ABT263 P P a a lb lb o o P S a 6 l 3 b 8 o 4 5 ABT263
slleC
evitisop
laG
β-AS
%
p<1e-04
p<1e-04 p<1e-04 1.5 p<1e-04 p<1e-04 p<1e-04
1.0 p = 0.007 p = 0.01
0.5
0.0 Doce
095
DO
ni
egnahc
dloF
p<1e-04 p = 0.006 p<1e-04 p<1e-04 1.5
p = 0.0018 p = 0.002
1.0
0.5
0.0
095
DO
ni egnahc
dloF
100μm 100μm
p<1e-04 p<1e-04 p<1e-04 p<1e-04
p=0.0153
p = 0.0021
2.5
2.0
1.2
1.0
noitarefilorp
ni
egnahC
dloF
3300.0
= p
40-e1<p
40-e1<p
Doce S6 D 3 o 8 c 4 e 5 ABT263 P P a a lb lb o o S6 P 3 a 8 lb 4 o 5 ABT263 D D o o c c e e S6 D 3 o 8 c 4 e 5 ABT263 P P a a lb lb o o S6 P 3 a 8 lb 4 o 5 ABT263
p <0.0001 p <0.0001
p = 0.8338 p = 0.0104
p = 0.0003 p <0.0001
6 Vehicle
4 ABT263R
S63845R
2
0
BCL2 MCL1
c.m. Docetaxel c.m. ABT263R c.m. S63845R
c.m. Docetaxel c.m. ABT263R c.m. S63845R
0 6 12 18 24 30 36 42 48 54 60 66 72 78
Time (hours)
slevel
ANRm
ni egnahc
dloF
sllec detertnu
no
.mron
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
Docetaxel
NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications 9
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
Fig.4Mcl-1targetingassenolyticanti-migratorytherapy.aRepresentativepicturesofcrystalvioletandSA-βGalofPC3shTIMP1treatedcells(Scale
bar100μm).Dataarerepresentativeofthreeindependentexperiments.bCristalvioletandSA-βGalquantification(Cristalvioletn=4forDocetaxeland
Palbociclib,n=5forDocetaxelABT263,PalbociclibS63845andPalbociclibABT263,n=7forDocetaxelS63846;SA-βGaln=4forVehicle,Docetaxel,
DocetaxelS63845,n=3forPalbociclib,n=6forPalbociclibABT263andn=7forDocetaxelABT263andPalbociclibS63845,n=biologicalindependent
samplesfromthreeindependentexperiments).cRepresentativepicturesofcrystalvioletandSA-βGalofLNCaPtreatedcells(Scalebar100μm).Dataare
representativeofthreeindependentexperiments.dQuantificationofcrystalvioletandSA-βGalstaining(Cristalvioletn=6forDocetaxel,Palbocicliband
PalbociclibABT263,n=7forDocetaxelS63845,DocetaxelABT263andPalbociclibS63845;n=biologicalindependentsamples,SA-β-Galn=6for
Vehicle,DocetaxelABT263andPalbociclib,n=7forDocetaxel,DocetaxelABT263andPalbociclibS63845,n=4forPalbociclibABT263,n=biological
independentsamplesfromthreeindependentexperiments).eSchematicrepresentationoftheexperimentaldesign.fRT-qPCRanalysisofDocetaxel
treatedcellsandtheremainingclonesuponABT263(ABT263R)andS63845(S63845R)treatment(forBcl2n=5forVehicleandABT263R,n=6for
S63845R;forMcl1n=6forVehicleandS63845Randn=4forABT263R,n=biologicalindependentsamplesfromthreeexperiments).Thepvalueswere
determinedbyonewayANOVAfollowedbyTukey’smultiplecomparisontest.gRepresentativepicturesofwoundhealingassay(Scalebar600μm).Data
arerepresentativeoftwoindependentexperiments.hPercentageofwoundconfluenceovertimenormalizedtotime0(forc.m.Docetaxelandc.m.
ABT263Rn=8,forc.m.S63845Rn=6,n=biologicalindependentsamplesfromtwoindependentexperiments).iRepresentativepicturesofproliferation
assay(Scalebar600μm).Dataarerepresentativeoftwoindependentexperiments.jFoldchangeinproliferationnormalizedtotime0(forc.m.Docetaxel,
c.m.ABT263Randc.m.S63845Rn=6,n=biologicalindependentsamplesfromtwoindependentexperiments).b,d,h,jThepvaluesweredeterminedby
onewayANOVAfollowedbyTukey’smultiplecomparisontest.ThewholeAnovaresultsweregivenintheSupplementaryData4.b,d,fDataare
representedasmean±SD.h,jDataarerepresentedasmean±SEM.Sourcedataareprovidedasa SourceDatafile.
(5mm)werepreparedforantibodydetectionandhematoxylinandeosinstaining. signalling#5453)anti-HSP90(Cellsignalling#4874),p27kip1(Cellsignalling
ImageswerescannedwithAperioandopenedwithImageScopev12.3.2.8013(Leica #3698S),p15ink4b(Abcam#53034),p16ink4a(Abcam#211542),p21(Abcam
Biosystem). #107099),p19ARF(5-C3-1)(SantaCruzBiotechnology#SC-32748),PAI-1
(Abcam#66705),Mcl-1(Cellsignaling#5453),secondaryAnti-Rabbit(Promega
S S A en -β e - s g c a e l n a c s e sa a y s , s tu o m ci o a r te s d am β p -g le a s la w c e t r o e s i i m da m se ed ( ia S t A el - y β f - r g o a z l e ) n a i s n s O ay C . T Fo so r l t u is ti s o u n e- a s t p − ec 8 ifi 0 c °C # (E W pC 40 A 1 M 1) ) ,s M ec o o n n o d c a lo ry na A l n A t n i- t M ib o o u d s y e ( ( G P 8 r . o 8 m ), e F g I a TC #W ,e 4 B 0 i 2 o 1 sc ) i . e F n o c r e™ F ( A 1 C 1- S 57 so 91 rt - i 8 n 2 g ). C F D u 3 rt 2 h 6 er
andsectionsof4mmwereprepared.Senescence-associatedSA-β-galstainingwas informationaboutdilutionsandclonesareavailableinSourceData.
performedusingSenescenceβ-GalactosidaseStainingKit(CellSignalingCat.No
9860)accordingtothemanufacturer’sinstructions.Counterstainingwasper- Quantitativereal-timePCR(RT-qPCR).RNAextractionfromcellsortissues
formedusingEosinstaining(Alcohol-basedDiapath,C0352).Forinvitro sampleswasperformedusingTrizol(Ambion,lifetechnologies,15596026),
experiment,SA-β-galstainingwasperformedusingSenescenceβ-Galactosidase accordingtothemanufacturer’sinstructions.cDNAwasobtainedusingImPROM
StainingKit(CellSignalingTechnology,Cat.No9860)accordingtothemanu- IIkit(Promega,A3800)accordingtothemanufacturer’sinstructions.RT-qPCR
facturer’sinstructions. wasperformedusingGotaq®qPCRMasterMix,Promega®(A6002)onStepOne
Real-TimePCRsystems(AppliedBiosystems).PrimersusedforRT-qPCRare
Proliferationandcelldeathassay.ProliferationassayinPC3,TrampC1,Pten−/− l
m
is
e
te
th
d
o
i
d
n
64
S
.
upplementaryTable2.ExpressionlevelswerecalculatedusingtheddCT
TrampC1andRapidcapcelllineswasperformedbyplating1×104cellsperwellof
a96-wellplateinatleastsextuplicate.Proliferationwasmonitoredandanalyzedby
usingIncucyteS3invitrosystem(Essenbioscience).
Singlecellsequencinganalysis.ProstatetumorswereresectedfromPtenpc−/−
andPtenpc−/−;Timp1−/−mice(allthreelobes,AP,DLPandVP)andfromNRG
miceinjectedsubcutaneouslywith2.5*106PC3ShTIMP1(see“Dataavailability”
Migrationassay.MigrationassaywasperformedinPC3byplating20×104cells
section).SamplewereprocessedforsinglecellsuspensionfollowedbyRNA
perwellof96-wellplateinatleastsextuplicate.Woundwasperformedusing sequencingandanalysisusingthefollowingprocedures:
IncucyteWoundMakerandcellmigrationwasmonitoredandanalyzedbyusing
IncucyteS3invitrosystem(Essenbioscience).
Singlecellsuspension.Prostatetumorsorxenograftstumorswereisolated,
mincedandprocessedforsinglecellsuspension.Tissuesweredigestedin2mlof
Conditionmediaassay.Cellsupernatantswereharvestedandspundownat453g DigestionBuffercomposedbyRPMI10%FBS+1%P/S,500mLofCollagenaseD
for10minandthesupernatantwasfilteredusing0.22mmfilters.Conditioned (1mg/mL),50mLofDNAse(100U/mL)and125mLofHEPES(25mM).Thecell
mediumwasadministeredtoparentalcellsattimezeroor48hpriortheassayfor suspensionwasincubatedfor50minat37°Conarocker.Then,thedigestionwas
proliferationandmigrationassay,respectively.Theconditionedmediuminallthe stoppedbyadding1mLofRPMI10%FBS+1%P/S.Thecellssuspensionwas
experimentswasnormalizedbasedonthenumberofcellspresentinthewellatthe filteredthrougha100μmcellstrainerandkeptonicefor4min.Thencellssus-
momentoftheharvesting. pensionwasfilteredagainthrougha40μmcellstrainerandspundownat453gfor
5minat4°C.FACSstainingwasperformedusingEPCAM-FITC(anti-MoCD326,
eBioscience,cloneG8.8#11-5791-82)forthemurineprostatetumors,while
Westernblot.Prostatetissues,tumorsamplesorcellswerelysedusing1xRIPA
buffer(Cellsignaling,9806)supplementedwithPhenylmethanesulfonylfluoride PC3shTIMP1weresortedthankstoGFPpositivity.Sampleswereacquiredona
BDsorterAriaIII(BDBiosciences).ThesoftwareusedwasBDFaCSDivav9.0.No
(PMSF;MilliporeSigma,catalog329-98-6)andincubatedonicefor30min.
furtheranalyseswereneededforthisstudy.Thegatingstrategyusedintransgenic
Sampleswerecentrifugedat46357gfor15min.Proteinconcentrationwas
mousemodelshavebeendoneasitfollows:FSC-H/FSC-A,SSC-A/FSC-A,7AAD/
determinedbytheBCAkit(ThermoFisher23227).Equalamountsofproteins FSC-A,EPCAM+/FSC-A(SupplementaryFig.1).Whileinxenograftmodels
w
tra
er
n
e
sf
s
e
u
rr
b
e
je
d
ct
o
e
n
d
t
t
o
o
0
S
.
D
45
S-
m
p
m
oly
n
ac
it
r
r
y
o
l
c
a
e
m
ll
i
u
d
l
e
os
g
e
el
m
e
e
l
m
ec
b
tr
r
o
a
p
n
h
e
o
(
r
T
es
h
i
e
s
r
(
m
SD
o
S
S
-
c
P
ie
A
n
G
ti
E
fic
),
,
1
8
0
8
%
018
a
)
n
.
d FSC-H/FSC-A,SSC-A/FSC-A,GFP+/FSC-A(SupplementaryFig.6a).
Single-celltranscriptomeswasperformedusing10×Chromiumsinglecell
Afterproteintransfer,membraneswereblockedin5%milksolutionandmem- platform(10×Genomics,Pleasanton,CA.USA).FACS-sortedEpcam+prostate
braneswereprobedwiththeindicatedantibodiesovernightat4°C.Themem-
cellswereusedastheinputsourceforthescRNA-seq.Cellsweresuspendedina
braneswereincubatedwithhorseradishperoxidase-conjugated(HRP-linked)
phosphatebuffersolutioncontaining0.04%weight/volumebovineserumalbumin
secondaryantibodiesanti-rabbitIgG(Promega,W4011,1:5000)oranti-mouseIgG
(BSA).Therecommendedvolumeofsinglecellsuspensionwasloadedona
(Cellsignaling,W4021,1:5000)anddevelopedusingenhancedchemolumines-
cence(ECL)substrate(ThermoScientific,32106).Membraneswereexposedto ChromiumSingleCellController(10×Genomics)targeting~10,000cellsper
murineprostatesampleswhileforxenograftstumorsweusedatargetcellrecovery
FusionSoloSimagingsystem(Vilber).Blotsweresemi-quantitativelyanalyzedby
between5000and10000cellspersample.Barcodedsingle-cellgelbeadsin
densitometryusingImageJ1.52v(NationalInstitutesofHealth).
emulsion(GEMs)werecreatedby10×Genomics!ChromiumTMandthenreverse
transcribedtogeneratesingle-cellRNA-seqlibrariesusingChromiumSingleCell3′
Antibodies.ForIHCanti-CleavedCaspase3(Cellsignalling#9661),anti-Ki67 LibraryandGelBeadKitv2(10×Genomics)accordingtomanufacturer’s
(RTU-LabVision#RM-9106-R7DilutionReadytouse),anti-Luciferase(Abcam instructions.Resultingshortfragmentlibrarieswerecheckedforqualityand
#ab181640),Mcl-1(Cellsignaling#5453)Ly-6G(GR1),Clone1A8(RUO);551459 quantityusinganAgilent2100BioanalyzerandInvitrogenQubitFluorometer.
BDPharmigen,F4/80(BM8)RatMono,14-4801-82eBioscience™(ThermoSci- Uniquemolecularidentifiers(UMIs),whichwereincorporatedintothe5′endof
entific),p16(Abcam#ab211542)wereused.ForWesternblotanti-CleavedCaspase cDNAduringreversetranscription,wereusedtoquantifytheexactnumberof
3(Cellsignalling#9664),anti-Bcl-2(Cellsignalling#3498S),anti-Mcl-1(Cell transcriptsinacell.
10 NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications
Docetaxel
Vehicle Docetaxel S63854
a Docetaxel c
treatment
PC3
Luc-ShTimp1 Senolytic
Injection treatment
b
Single-cellsequencingdatapreprocessingandqualitycontrol.Sequencingdata analysiswasperformedinepithelialcellspurifiedfrombothPtenpc−/−andPtenpc−/−;
wereprocessedbyCellRanger65(version3.1.0formurinealignmentandversion6.0.0 Timp1−/−tumorsoronGFP+cellsinPC3shTIMP1xenograft.Foreachcell,we
forxenograftderived-samples)andreadswerealignedtomousegenome(mm10 calculateddifferentqualitymeasures:percentageofmitochondrialgenes,numberof
v3.0.0)orhumangenome(GRCh38)withSTAR66(v.2.5.1b).Toreducethe‘dropout’ genesandgenebiotype.Weremovedcellsthathadmorethan25%expressionon
phenomenon,RMagicpackagewasusedongene-counts67.Singlecellsequencing mitochondrialgenes,fewerthan100totalgenesexpressedandweconsideredonly
3CC
76-iK
Docetaxel
ABT-263
laG-
β
-AS
Vehicle
ABT263
S63845
Docetaxel
Docetaxel ABT263
Docetaxel S63845
d
e f
Docetaxel
Not Senescent Senescent
4
4
3 0 2 1
-4 0
1lcM
4
0
-4
2_PAMU
g Docetaxel Docetaxel
ABT263 S63845 l
Average Expression Percent Expressed
1.5 1.0 25
0.5 50
- 0 0 .0 .5 75
-1.0 -1.5
-5 0 5 10 -5 0 5 10 -5 0 5 10
UMAP_1
Senescent cells j k
Percent Expressed Percent Expressed Percent Expressed
Docetaxel
S63845 3 4 0 0 2 2 4 6 8 9 8 0 50 28 92 60 30 94 Docetaxel 70
ABT263 Average Expression Average Expression Average Expression
0.5 1.0 0.5
0.0 0.5 0.0
Docetaxel -0.5 0.0 -0.5
-1.0 -0.5 -1.0
MCL1 G2M Tissue migration
sesatsateM
Docetaxel Docetaxel ABT263 Docetaxel S63845
h
i Not senescent cells
gnuL
reviL
Docetaxel Docetaxel ABT263 Docetaxel S63845
Luciferase pS6 H&E Luciferase pS6 H&E Luciferase pS6 H&E
CD44
VEGFA
SOX4
SOX9
IGFBP7 COL1A2
CXCL8
CCL20
PI3
MMP10
NENF
IGFBP4
C4orf48
MDK
MANF
PTX3
TFPI
C5orf46 SERPINE1 TNFRSF6B C5
SERPIND1
PCOLCE2 PRSS2
THBS1
CXCL1
CXCL2 CXCL3
Docetaxel D AB oc T e 2 t 6 a 3 xel D S6 o 3 ce 8 t 4 a 5 xel
1LCM
p = 0.0021
60 p = 0.005
p = 0.0202
40
20
0 CC3 SA-β-Gal
Vehicle Docetaxel Docetaxel ABT263 Docetaxel S63845
slleC
evitisoP
%
p <0.0001
p = 0.0053
p = 0.0003
p = 0.0039
60 p = 0.0011 p = 0.0174
40
20
0
slleC
evitisoP
%
p <0.0001
p <0.0001
80 p <0.0001
p <0.0001 p <0.0001
60
40
20
0 Ki67
slleC
evitisoP
%
p <0.0001
p = 0.019
p <0.0001 p = 0.0442
40
30
20
10
0 MCL1
²mm/sllecevitisoplaGβAS
p <0.0001 p <0.0001
p <0.0001 p = 0.0001
200 p = 0.0045 60 p <0.0001
150
100
50 40
4 20
2
0 0
Lungs Liver # Foci mm3
gnuL
ni
3mm
rep
icofcitatsateM
1500
1000
600
400
200
0
0 15 17 19 22 24 26 30 35 37 39 42 Days
3mm
emulov
romuT
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
p < 0.0001
p = 0.0023
p = 0.77
NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications 11
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
Fig.5S63845isanefficientsenolytictherapyinvivo.aSchematicrepresentationoftheexperimentaldesign.bGrowthcurveoftumorsinvivoinmm3
(n=5forUntreated,ABT263,S63845,Docetaxel,Docetaxel+ABT263,Docetaxel+S63845,n=independentanimalsfromoneexperiment).Thep
valuesweredeterminedbytwo-wayANOVAfollowedbyTukey’smultiplecomparisontestattimepoint39dayspostinjection,separatelyforsingle
treatment(Untreated,Docetaxel,ABT263,S63845)andDocetaxeltreatedgroups(Docetaxel,Docetaxel+ABT263,Docetaxel+S63845).Dataare
representedasmean±SEM.cRepresentativepicturesofimmunohistochemistryforCleavedCaspase3(CC3),Ki67,MCL-1andSA-βGal.Dataare
representativeofoneexperiment.dFromleft,quantificationinpercentage(CC3n=6,Ki67n=6,MCL-1n=9andSA-βGaln=6;n=multipleareasof
fouranimalsfromoneexperiment.ThepvaluesweredeterminedbyOne-wayANOVAtestfollowedbyTukey’smultiplecomparisonstest).Dataare
representedasmean±SD.eH&E,Luciferaseandphospho-S6immunohistochemicalstaininginlungandlivermetastasesinDocetaxel,
Docetaxel+ABT263andDocetaxel+S63845treatedNRGmice.Dataarerepresentativeofoneexperiment.fBargraphrepresentingmetastases
quantification(n=9forDocetaxelandDocetaxelABT263,n=6forDocetaxelS63845;=multipleareasof4animalsfromoneexperiment).For
metastasescountthepvaluesweredeterminedbyTwo-wayANOVAfollowedbyŠídák’smultiplecomparisons,whileforthecountofmetastasesfociper
mm3,thepvaluesweredeterminedbyoneWayANOVAfollowedbyTukey’smultiplecomparisonstest.Dataarerepresentedasmean±SDgUMAPplot
ofsenescentandnotsenescentcells,definingusingSIT,inxenograftPC3shTIMP1cellstreatedwithDocetaxelaloneorincombinationwithABT263or
S63845(Docetaxel%senescentcells=35.5%,Docetaxel+ABT263%senescentcells=15.6%,Docetaxel+S63845%senescentcells=14%).
hUMAPplotofsenescentcellsshowingMCL-1expressioninxenograftPC3shTIMP1cellstreatedwithDocetaxelaloneorincombinationwithABT263or
S63845.iMCL-1expressionforeachtreatment,wheredotsizeandcolorrepresentthepercentageofcellsexpressingtheindicatedgeneandtheaverage
scaledexpressionvalue,respectively.jG2Msignatureforeachtreatment,wheredotsizeandcolorrepresentpercentageofcellsexpressingandthe
averagedscaledexpressionvalue,respectively.kss-GSVAoftissuemigrationsignatureforeachtreatment,wheredotsizeandcolorrepresentpercentage
ofcellexpressingandtheaveragedscaledexpressionvalue,respectively.lMarkergenesexpressionsforeachtreatment,wheredotsizeandcolor
representpercentageofcellexpressingandtheaveragescaledexpressionvalue,respectively.SourcedataareprovidedasaSourceDatafile.Thewhole
AnovaresultsweregivenintheSupplementaryData4.
proteincodinggenesdefinedusinggetBM(biomaRtpackage).Allthesampleswere PathwayanalysiswereperformedusingclusterProfiler79package:for
integratedusingSeurat68–71package(FindIntegrationAnchorsandIntegrateData enrichmentanalysisweusedgseGO(ont=“BP”)functionwhileforover-
functionafterlibrary-sizenormalizationofeachcellusingNormalizeDatafunction representationanalysisweusedenrichGOfunction.Theoutputsofpathway
withdefaultparameters). analysisweresimplifiedusingsimplifyfunctionwithcutoff=0.6andgenesets
WeidentifyfeaturesthatarevariableinthesampleswithFindVariableFeatures wereconsideredsignificantwithFDR<0.05.Incaseofmultiplecomparisonsof
functionandPrincipalcomponentanalysis(PCA)dimensionalityreductionwasrun pathway,weusedcompareClusterResultfunction.Toanalyzetheactivityof14
usingthetop2000featuresidentified.Numberoftheincludedcomponents(PCs)was relevantsignalingpathways,weusedPathwayRespOnsiveGENes(PROGENy80)
assessedusingtheElbowPlotfunctionandfifteenPCswereconserved.Graph-based analysis.Tostudysenescenceheterogeneity,alltheanalyseswereperformedusing
clusteringapproachwasusedtoclusterthecellsusingFindNeighbours(k=20)and exclusivelythegenesfoundupregulatedintotalsenescentcellscomparedtonon
FindClustersfunctions(0.25<res<2with0.25difference).Tovisualizethedata,the senescentcells(3757genes).
dimensionalreductiontechniquet-distributedstochasticneighborembedding(t-SNE) ss-GSVAscoresfordifferentpublishedgenesetsandcelldeathpathwayswere
andUMAP72wereappliedusingtheRunTSNEandRunUMAPfunctionsfromSeurat. calculatedusinggsva81function(method=“ssgsea”).Correlationanalysiswas
Inmurinesinglecellsequencing,cellspositiveforCD45(Ptprcgene)andnegative performedusingcor.testfunction(alternative=two.sided,method=“pearson”,
forEpcamwereremoved.InsidetheEpcam+cells,wedefinedepithelialsubtypes conf.level=0.95)andadjustedpvalueswerecalculatedwithp.adjustfunction
basedoncanonicalmarkers:Cd24a,Krt8andKrt18forluminalcells;Trp63,Krt5and using(method=“BH”).ForclassificationofcellsbasedonMcl1expressionlevels
Krt14forbasalcellsandPax2,Pate4andCalml3forsemi-vesicalcells73.For weclassifiedintoquartiles:Mcl1+correspondstofirst,secondandthirdquartiles,
xenograftsc-RNAseqdata,alltheanalysiswereperformedafterregressionof whileforBcl2expressionweusedthemedianlevelstoclassifyinBcl2+andBcl2-.
nCount_RNAandnFeature_RNAfeatures,duetodifferencesbetweenthesamples. AllplotsweredesignedusingSeuratpackageandggplot2package.
Forout-of-clusteringmethods,cellswereprojectedtothecombinationof12
S ri e th n m esc b e a n se c d e o in n d c e o x m t m oo o l n (S fe I a T t ) u . r T es o o d f e s fi e n n e es s c e e n n e t sc c e e n ll t s: c o e v ll e s r , e w x e pr d e e ss v i e o l n op o e f d s a p n ec a ifi lg c o- s a e v n a e il s a c b e i n li c ty e- ” re se la c t t e io d n a ) v u a s il i a n b g le sc d m at a a p se -c ts lu ( s S te u r pp v1 le . m 16 e .0 nt ( a t r h y re T s a h b o l l e d 1 = ,s 0 e .1 e 5 “ ) D a a n t d a the
genesandcellcyclearrest.Thetoolwascomposedoffoursteps:(a)definitionof functionSingleRfromSingleRpackagewithdefaultparameters.
thesenescencesignature;(b)definitionofcellcyclearrestsignatures;(c)co-
occurenceof(a)and(b)definedbysenescencescoresK,WPandR;(d)identifi- Signatures.Apoptoticpathway:Bcl2,Bcl2l1,Mcl1,Bcl2l12,Bcl2a1a,Cflar,
cationofsenescentcellsbasedonsenescencescoreK,WPandR. Gadd45a,Traf1,Ptpn13,Birc3(anti-apoptosis),Bbc3,Bcl2l11,Pmaip1,Bak1,Bax,
Pidd1,Bid,Apaf1,Fas,Tnfrsf10b(pro-apoptosis);Ferroptosispathway:Map1lc3a,
Definitionofsenescencesignature.AddModuleScorefunction(Seuratpackage)to Atg5,Atg7,Ncoa4,Alox15,Lpcat3,Acsl4,Vdac2,Vdac3,Cybb,Gpx4,Gss,Gclc;
definetheaverageexpressionofknownsenescentmarkers(p16,p15p19,p21,p27 Necroptosispathway:Mlkl,Trpm7,Ripk1,Ripk3;Parthanatospathway:Aifm1,
andPAI-1)ineachcell. Rnf146,Parp1,Parg;Pyroptosispathway:Gsdmd,Nlrp3,Nlrc4,Aim2,
Casp1,Pycard,Mefv;Saspsignature:Cxcl1,Cxcl2,Hc,Csf3,Csf2,Csf1,Il10,
Definitionofcellcyclearrestsignatures.ss-GSVAscorewascalculatedforeachcell Il13,Il6,Cxcl13,Cxcl10,Icam1,Ccl2,Cxcl15,Ccl20,Vegfc,Vegfa,Inhba,Il1a,Il1b,
withGSVApackagebyusingthreedifferentgenesets(KEGGCELLCYCLE74–76; Bmp2,Gdf15,Tgfb1,Tgfb2,Tgfb3,Bmp6,Ogg145,82.
REACTOMECELLCYCLEandWPCELLCYCLE78).Todefinethecellcycle
arrestweinvertedthedirectionofscores: Quantificationandstatisticalanalysis.Allexperimentswereperformedonbio-
logicalreplicatesasmentionedintherespectivefigurelegends.Samplesizeforeach
ð1ÞCellCyclearrestsignature i ¼(cid:2)ssGSVAscore i withði¼K;WP;RÞ experimentalgroup/conditionisreportedintheappropriatefigurelegend.Alldata
DefinitionofsenescencescoresK,WPandR.Wecombinedthedifferentcellcycle
pointsarepresentedforquantitativedata,withanoverlayofthemeanwithSEM.
arrestsignatureswiththesenescencesignaturesbyusingtheseformula: Statisticallysignificantdifferencesbetweencontrolandexperimentalgroupswere
ð2ÞSenescencescore
i
¼Cellcyclearrestsignature
inormð0(cid:2)1Þ
þSenescencesignature
normð0(cid:2)1Þ
d
w
e
i
t
t
e
h
rm
Tu
in
k
e
e
d
y
u
m
s
u
in
lt
g
ip
M
le
u
c
lt
o
i
m
ple
pa
S
r
t
i
u
s
d
on
en
d
t’
i
s
ff
t
er
t
e
e
n
st
c
s
e
(t
t
w
es
o
t,
-t
W
ail
i
e
lc
d
o
,
x
u
o
n
n
pa
te
ir
s
e
t,
d
a
),
n
o
d
n
l
e
o
w
g-
a
r
y
an
A
k
NOVA
(Mantel–Cox)testasindicatedintheappropriatefigurelegendandtext.Allstatistical
withði¼K;WP;RÞ
analyseswereperformedusingGraphPadPrism8,MicrosoftExcel2016orR-Studio.
Identificationofsenescentcells:wedividedthesenescencescoreK,WPandR
basedonquantiledivision(quantilefunction)andweconsideredassenescentcells
Reportingsummary.FurtherinformationonresearchdesignisavailableintheNature
theoneinwhichthesenescencescoreK,WPandRwerebelongedtothefourth
quartile(highestvalue). ResearchReportingSummarylinkedtothisarticle.
Data availability
Single-cellsequencingdataprocessing.Differentiallyexpressedgeneswere
identifiedusingFindAllMarkersorFindMarkerfunctions.Geneswereidentifiedas Thesingle-cellRNAsequencingdatageneratedinthisstudyhavebeendepositedinthe
differentiallyexpressedinaparticularsetofcellsifFDR<0.05andminimum GeneExpressionOmnibus(GEO)databaseunderaccessioncodeGSE189519for
expressioninatleast30%ofcells. xenograftprostatecancermodelandGSE189307formurineprostatecancermodels.The
12 NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
publiclyavailableRNA-seqdatausedinthisstudyareavailableinGEO(Gene 28. Lesina,M.etal.RelAregulatesCXCL1/CXCR2-dependentoncogene-induced
ExpressionOmnibus),andEMBL-EBIdatabasesunderaccessioncodesGSE11530183, senescenceinmurineKras-drivenpancreaticcarcinogenesis.J.Clin.Investig.
GSE6113084,GSE13072731,GSE10263985,GSE13236986,GSE9844087,GSE10927088, 126,2919–2932(2016).
GSE15874389andE-MTAB-997090.ThesourcedataofthefiguresareprovidedasSource
29. Kiselev,V.Y.,Yiu,A.&Hemberg,M.scmap:projectionofsingle-cellRNA-
Datafiles.Sourcedataareprovidedwiththispaper. seqdataacrossdatasets.Nat.Methods15,359–362(2018).
30. Aran,D.etal.Reference-basedanalysisoflungsingle-cellsequencingrevealsa
Code availability transitionalprofibroticmacrophage.Nat.Immunol.20,163–172(2019).
31. Casella,G.etal.Transcriptomesignatureofcellularsenescence.NucleicAcids
ThecodeforSenescenceIndexTool(SIT)isavailableasSupplementaryData5.Allthe
Res.47,7294–7305(2019).
otheranalysesaredonewithstandardpipelinesandarefullydescribedintheMethods
32. Hernandez-Segura,A.etal.UnmaskingTranscriptionalHeterogeneityin
section.Sourcedataareprovidedwiththispaper.
SenescentCells.Curr.Biol.27,2652–2660.e4(2017).
33. Fridman,A.L.&Tainsky,M.A.Criticalpathwaysincellularsenescenceand
Received: 16July2021; Accepted: 24March2022; immortalizationrevealedbygeneexpressionprofiling.Oncogene27,
5975–5987(2008).
34. Basisty,N.etal.Aproteomicatlasofsenescence-associatedsecretomesfor
agingbiomarkerdevelopment.PLOSBiol.18,e3000599(2020).
35. Purcell,M.,Kruger,A.&Tainsky,M.A.Geneexpressionprofilingof
replicativeandinducedsenescence.CellCycle13,3927–3937(2014).
References 36. Yamane,M.etal.Senescence-associatedsecretoryphenotypepromotes
1. Hernandez-Segura,A.,Nehme,J.&Demaria,M.HallmarksofCellular chronicoculargraft-vs-hostdiseaseinmiceandhumans.FASEBJ.34,
Senescence.TrendsCellBiol28,436–453(2018). 10778–10800(2020).
2. Calcinotto,A.etal.Cellularsenescence:aging,cancer,andinjury.Physiol.Rev. 37. Mavrogonatou,E.,Konstantinou,A.&Kletsas,D.Long-termexposureto
99,1047–1078(2019). TNF-αleadshumanskinfibroblaststoap38MAPK-andROS-mediated
3. Scudellari,M.Tostayyoung,killzombiecells.Nature550,448–450(2017). prematuresenescence.Biogerontology19,237–249(2018).
4. Muñoz-Espín,D.&Serrano,M.Cellularsenescence:fromphysiologyto 38. Chen,H.etal.TGF-β1/IL-11/MEK/ERKsignalingmediatessenescence-
pathology.Nat.Rev.Mol.CellBiol.15,482–496(2014). associatedpulmonaryfibrosisinastress-inducedprematuresenescencemodel
5. Coppé,J.-P.,Desprez,P.-Y.,Krtolica,A.&Campisi,J.Thesenescence-
ofBmi-1deficiency.Exp.Mol.Med.52,130–151(2020).
associatedsecretoryphenotype:thedarksideoftumorsuppression.Ann.Rev. 39. Salminen,A.,Kauppinen,A.&Kaarniranta,K.EmergingroleofNF-κB
Pathol.:Mech.Dis.5,99–118(2010). signalingintheinductionofsenescence-associatedsecretoryphenotype
6. Guccini,I.etal.SenescenceReprogrammingbyTIMP1DeficiencyPromotes (SASP).Cell.Signalling24,835–845(2012).
ProstateCancerMetastasis.CancerCell39,68–82.e9(2021). 40. Rovillain,E.etal.Activationofnuclearfactor-kappaBsignallingpromotes
7. Lau,L.&David,G.Pro-andanti-tumorigenicfunctionsofthesenescence-
cellularsenescence.Oncogene30,2356–2366(2011).
associatedsecretoryphenotype.Exp.Opin.Ther.Targets23,1041–1051 41. Bent,E.H.,Gilbert,L.A.&Hemann,M.T.Asenescencesecretoryswitch
(2019). mediatedbyPI3K/AKT/mTORactivationcontrolschemoprotective
8. Duy,C.etal.ChemotherapyInducesSenescence-LikeResilientCellsCapable
endothelialsecretoryresponses.GenesDev.30,1811–1821(2016).
ofInitiatingAMLRecurrence.CancerDiscov.11,1542–1561(2021). 42. Liu,S.etal.ThePI3K-Aktpathwayinhibitssenescenceandpromotesself-
9. Saleh,T.etal.Tumorcellescapefromtherapy-inducedsenescence.Biochem.
renewalofhumanskin-derivedprecursorsinvitro.AgingCell10,661–674
Pharmacol.162,202–212(2019). (2011).
10. Serrano,M.&Barzilai,N.Targetingsenescence.Nat.Med.24,1092–1094 43. Oka,T.etal.CXCL17AttenuatesImiquimod-InducedPsoriasis-likeSkin
(2018).
InflammationbyRecruitingMyeloid-DerivedSuppressorCellsand
11. Zhu,Y.etal.Identificationofanovelsenolyticagent,navitoclax,targetingthe RegulatoryTCells.J.Immunol.198,3897–3908(2017).
Bcl-2familyofanti-apoptoticfactors.AgingCell15,428–435(2016). 44. Zhang,H.etal.CXCL2/MIF-CXCR2signalingpromotestherecruitmentof
12. Kirkland,J.L.&Tchkonia,T.Senolyticdrugs:fromdiscoverytotranslation.J. myeloid-derivedsuppressorcellsandiscorrelatedwithprognosisinbladder
Inter.Med.288,518–536(2020). cancer.Oncogene36,2095–2104(2017).
13. Wyld,L.etal.SenescenceandCancer:AReviewofClinicalImplicationsof 45. Toso,A.etal.EnhancingChemotherapyEfficacyinPten-DeficientProstate
SenescenceandSenotherapies.Cancers(Basel)12,2134(2020). TumorsbyActivatingtheSenescence-AssociatedAntitumorImmunity.Cell
14. Bollard,J.etal.Palbociclib(PD-0332991),aselectiveCDK4/6inhibitor,
Rep.9,75–89(2014).
restrictstumourgrowthinpreclinicalmodelsofhepatocellularcarcinoma. 46. DiMitri,D.etal.Tumour-infiltratingGr-1+myeloidcellsantagonize
Gut66,1286–1296(2017). senescenceincancer.Nature515,134–137(2014).
15. Yuan,L.,Alexander,P.B.&Wang,X.-F.Cellularsenescence:fromanti-cancer 47. Lasry,A.&Ben-Neriah,Y.Senescence-associatedinflammatoryresponses:
weapontoanti-agingtarget.Sci.ChinaLifeSci.63,332–342(2020). agingandcancerperspectives.TrendsImmunol.36,217–228(2015).
16. Pandey,K.etal.CombinedCDK2andCDK4/6InhibitionOvercomes 48. Glaser,S.P.etal.Anti-apoptoticMcl-1isessentialforthedevelopment
PalbociclibResistanceinBreastCancerbyEnhancingSenescence.Cancers12,
andsustainedgrowthofacutemyeloidleukemia.GenesDev.26,120–125
3566(2020). (2012).
17. Gao,S.DataAnalysisinSingle-CellTranscriptomeSequencing.MethodsMol. 49. Davalos,A.R.,Coppe,J.-P.,Campisi,J.&Desprez,P.-Y.Senescentcellsasa
Biol.1754,311–326(2018). sourceofinflammatoryfactorsfortumorprogression.CancerMetastasisRev.
18. Ziegenhain,C.etal.ComparativeAnalysisofSingle-CellRNASequencing
29,3421–3428(2008).
Methods.Mol.Cell65,631–643.e4(2017). 50. Tse,C.etal.ABT-263:APotentandOrallyBioavailableBcl-2Family
19. Chen,S.etal.Single-cellanalysisrevealstranscriptomicremodellingsin
Inhibitor.CancerRes.68,3421–3428(2008).
distinctcelltypesthatcontributetohumanprostatecancerprogression.Nat. 51. Chang,J.etal.ClearanceofsenescentcellsbyABT263rejuvenatesaged
CellBiol.23,87–98(2021). hematopoieticstemcellsinmice.Nat.Med.22,78–83(2016).
20. Lee,Y.-R.,Chen,M.&Pandolfi,P.P.Thefunctionsandregulationofthe 52. Li,Z.,He,S.&Look,A.T.TheMCL1-specificinhibitorS63845acts
PTENtumoursuppressor:newmodesandprospects.Nat.Rev.Mol.CellBiol. synergisticallywithvenetoclax/ABT-199toinduceapoptosisinT-cellacute
19,547–562(2018). lymphoblasticleukemiacells.Leukemia33,262–266(2019).
21. Collado,M.&Serrano,M.Senescenceintumours:evidencefrommiceand 53. Kotschy,A.etal.TheMCL1inhibitorS63845istolerableandeffectivein
humans.Nat.Rev.Cancer10,51–57(2010). diversecancermodels.Nature538,477–482(2016).
22. Lee,S.&Schmitt,C.A.Thedynamicnatureofsenescenceincancer.Nat.Cell 54. Tron,A.E.etal.DiscoveryofMcl-1-specificinhibitorAZD5991and
Biol.21,94–101(2019). preclinicalactivityinmultiplemyelomaandacutemyeloidleukemia.Nat.
23. Kaplon,J.etal.Akeyroleformitochondrialgatekeeperpyruvate Commun.9,5341(2018).
dehydrogenaseinoncogene-inducedsenescence.Nature498,109–112(2013). 55. Abulwerdi,F.etal.ANovelSmall-MoleculeInhibitorofMcl-1Blocks
24. Shyh-Chang,N.,Daley,G.Q.&Cantley,L.C.Stemcellmetabolismintissue PancreaticCancerGrowthInVitroandInVivo.Mol.CancerTher.13,
developmentandaging.Development140,2535–2547(2013). 565–575(2014).
25. Korolchuk,V.I.,Miwa,S.,Carroll,B.&vonZglinicki,T.MitochondriainCell 56. Calcinotto,A.etal.IL-23secretedbymyeloidcellsdrivescastration-resistant
Senescence:IsMitophagytheWeakestLink?EBioMedicine21,7–13(2017). prostatecancer.Nature559,363–369(2018).
26. Martínez-Zamudio,R.I.etal.AP-1imprintsareversibletranscriptional 57. Calcinotto,A.&Andrea,A.Agingtumourcellstocurecancer:“pro-
programmeofsenescentcells.Nat.CellBiol.22,842–855(2020). senescence”therapyforcancer.SwissMed.Wkly147,w14367(2017).2017.
27. Mongi-Bragato,B.etal.PivotalroleofNF-κBincellularsenescenceof 58. Nardella,C.,Clohessy,J.G.,Alimonti,A.&Pandolfi,P.P.Pro-senescence
experimentalpituitarytumours.J.Endocrinol.245,179–191(2020). therapyforcancertreatment.Nat.Rev.Cancer11,503–511(2011).
NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications 13
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-022-29824-1
59. Birch,J.&Gil,J.SenescenceandtheSASP:manytherapeuticavenues.Genes 87. Zirkel,A.etal.HMGB2LossuponSenescenceEntryDisruptsGenomic
Dev.34,1565–1576(2020). OrganizationandInducesCTCFClusteringacrossCellTypes.Mol.Cell70,
60. Basu,A.Theinterplaybetweenapoptosisandcellularsenescence:Bcl-2family 730–744.e6(2018).
proteinsastargetsforcancertherapy.Pharmacol.Ther.230,107943(2022). 88. Mainardi,S.etal.SHP2isrequiredforgrowthofKRAS-mutantnon-small-
61. Wang,H.,Guo,M.,Wei,H.&Chen,Y.TargetingMCL-1incancer:current celllungcancerinvivo.Nat.Med.24,961–967(2018).
statusandperspectives.J.Hematol.Oncol.14,67(2021). 89. Kolesnichenko,M.etal.TranscriptionalrepressionofNFKBIAtriggers
62. Shahbandi,A.etal.BH3mimeticsselectivelyeliminatechemotherapy- constitutiveIKK-andproteasome-independentp65/RelAactivationin
inducedsenescentcellsandimproveresponseinTP53wild-typebreast senescence.EMBOJ.40,e104296(2021).
cancer.CellDeathDiffer.27,3097–3116(2020). 90. Jochems,F.etal.TheCancerSENESCopedia:adelineationofcancercell
63. Cho,H.etal.RapidCaP,aNovelGEMModelforMetastaticProstateCancer senescence.CellRep.36,109441(2021).
AnalysisandTherapy,RevealsMycasaDriverofPten-MutantMetastasis.
CancerDiscov.4,318–333(2014).
Acknowledgements
64. Livak,K.J.&Schmittgen,T.D.AnalysisofRelativeGeneExpressionData
UsingReal-TimeQuantitativePCRandthe2−ΔΔCTMethod.Methods25, WeacknowledgeallthemembersofAlimontilabandIOR/IRBinstitutes.Thisworkwas
402–408(2001). supportedbyERCconsolidator(683136),aSwissCancerLeague(KFS4267-08-2017)grant,
65. Zheng,G.X.Y.etal.Massivelyparalleldigitaltranscriptionalprofilingof theDr.JosefSteinerFoundation,aSwissCard-Onco-GrantofAlfredandAnnemarievon
singlecells.Nat.Commun.8,14049(2017). Sickgrant,andtheHelmutHortenFoundation,SNSF(310030B_201274),SwissCancer
66. Dobin,A.etal.STAR:ultrafastuniversalRNA-seqaligner.Bioinformatics29, Leaguegrant(#5262),SNSFSinergiagrant(CRSII5_202302/1),PCFChallengeAward
15–21(2013). (#19CHAL08)andIBSAFoundation.
67. vanDijk,D.etal.RecoveringGeneInteractionsfromSingle-CellDataUsing
DataDiffusion.Cell174,716–729.e27(2018).
Author contributions
68. Satija,R.,Farrell,J.A.,Gennert,D.,Schier,A.F.&Regev,A.Spatial
M.T.,M.C.,andA.A.developedtheconceptanddesignedtheexperiments;M.T.per-
reconstructionofsingle-cellgeneexpressiondata.Nat.Biotechnol.33,
495–502(2015). formedbioinformaticanalysesandstatisticalanalyses;M.C.,M.DA.,An.V.,Au.V.per-
formedinvitroexperimentsandmolecularcharacterization;M.DA.,E.P.,G.A.
69. Butler,A.,Hoffman,P.,Smibert,P.,Papalexi,E.&Satija,R.Integratingsingle-
performedinvivoexperiments;S.M.performedimmunohistochemicalexperiments;I.G.,
celltranscriptomicdataacrossdifferentconditions,technologies,andspecies.
Nat.Biotechnol.36,411–420(2018). A.R.developedmousemodelsandcontributedtodatainterpretation;M.DA.,And.R.,
An.R.,P.C.tookcareofsampleprocessingandsequencing;M.B.supervisedbioinfor-
70. Stuart,T.etal.ComprehensiveIntegrationofSingle-.CellData.Cell177,
1888–1902.e1821(2019). maticanalysesandcontributedtodiscussthedata;M.T.,M.C.,A.A.wrotethepaperwith
inputsfromalltheotherauthors.
71. Hao,Y.etal.Integratedanalysisofmultimodalsingle-celldata.Cell184,
3573–3587.e3529(2021).
72. McInnes,L.,Healy,J.,Saul,N.&Großberger,L.UMAP:Uniform Competing interests
ManifoldApproximationandProjection.J.OpenSourceSoftw.3,861 A.A.isacofounderofandownsstockinOncoSenseandA.A.,M.C.,andA.R.are
(2018). inventorsofthepatentWO2019142095A1(Title:newalkinhibitorsenolyticdrugs).The
73. Karthaus,W.R.etal.Regenerativepotentialofprostateluminalcellsrevealed remainingauthorsdeclarenocompetinginterests.
bysingle-cellanalysis.Science368,497–505(2020).
74. Kanehisa,M.KEGG:KyotoEncyclopediaofGenesandGenomes.Nucleic Additional information
AcidsRes.28,27–30(2000).
SupplementaryinformationTheonlineversioncontainssupplementarymaterial
75. Kanehisa,M.Towardunderstandingtheoriginandevolutionofcellular
organisms.ProteinSci.28,1947–1951(2019). availableathttps://doi.org/10.1038/s41467-022-29824-1.
76. Kanehisa,M.,Furumichi,M.,Sato,Y.,Ishiguro-Watanabe,M.&Tanabe,M.
CorrespondenceandrequestsformaterialsshouldbeaddressedtoAndreaAlimonti.
KEGG:integratingvirusesandcellularorganisms.NucleicAcidsRes.49,
D545–D551(2021).
PeerreviewinformationNatureCommunicationsthankstheanonymousreviewer(s)for
77. Jassal,B.etal.Thereactomepathwayknowledgebase.NucleicAcidsRes.48,
D498–D503(2020). theircontributiontothepeerreviewofthiswork.
78. Kelder,T.etal.WikiPathways:buildingresearchcommunitiesonbiological
pathways.NucleicAcidsRes.40,D1301–1307(2012). Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
79. Yu,G.,Wang,L.-G.,Han,Y.&He,Q.-Y.clusterProfiler:anRPackagefor Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
ComparingBiologicalThemesAmongGeneClusters.OMICS:J.Integ.Biol. publishedmapsandinstitutionalaffiliations.
16,284–287(2012).
80. Holland,C.H.etal.Robustnessandapplicabilityoftranscriptionfactorand
pathwayanalysistoolsonsingle-cellRNA-seqdata.GenomeBiol.21,36(2020).
81. Hänzelmann,S.,Castelo,R.&Guinney,J.GSVA:genesetvariationanalysis Open Access This article is licensed under a Creative Commons
formicroarrayandRNA-Seqdata.BMCBioinform.14,7(2013). Attribution 4.0 International License, which permits use, sharing,
82. Acosta,J.C.etal.Acomplexsecretoryprogramorchestratedbythe adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
inflammasomecontrolsparacrinesenescence.Nat.CellBiol.15,978–990(2013). appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
83. Teo,Y.V.etal.NotchSignalingMediatesSecondarySenescence.CellRep.27, Commonslicense,andindicateifchangesweremade.Theimagesorotherthirdparty
997–1007e1005(2019). materialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unless
84. Herranz,N.etal.mTORregulatesMAPKAPK2translationtocontrolthe indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
senescence-associatedsecretoryphenotype.Nat.CellBiol.17,1205–1217 article’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutory
(2015). regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
85. Wang,L.etal.High-ThroughputFunctionalGeneticandCompoundScreens thecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/
IdentifyTargetsforSenescenceInductioninCancer.CellRep.21,773–783 licenses/by/4.0/.
(2017).
86. Vizioli,M.G.etal.Mitochondria-to-nucleusretrogradesignalingdrives
formationofcytoplasmicchromatinandinflammationinsenescence.Genes ©TheAuthor(s)2022
Dev.34,428–445(2020).
14 NATURECOMMUNICATIONS| (2022) 13:2177 |https://doi.org/10.1038/s41467-022-29824-1|www.nature.com/naturecommunications
