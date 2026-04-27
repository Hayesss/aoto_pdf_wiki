---
source_path: /mnt/c/Users/Administrator/Zotero/storage/CCQYJ26M/Quijada 等 - 2021 - Coordination of endothelial cell positioning and fate specification by the epicardium.pdf
ingested: 2026-04-23
sha256: a7d9d9a53d8f4ebe
---

ARTICLE
https://doi.org/10.1038/s41467-021-24414-z OPEN
Coordination of endothelial cell positioning and fate
fi
speci cation by the epicardium
Pearl Quijada 1,8, Michael A. Trembley1, Adwiteeya Misra1,2, Jacquelyn A. Myers 3,4,
Cameron D. Baker 3,4, Marta Pérez-Hernández 5, Jason R. Myers3,4, Ronald A. Dirkx Jr.1,
✉
Ethan David Cohen6, Mario Delmar5, John M. Ashton 3,4 & Eric M. Small 1,2,7
The organization of an integrated coronary vasculature requires the specification of immature
endothelialcells(ECs)intoarterialandvenousfatesbasedontheirlocalizationwithintheheart.
It remains unclear how spatial information controls EC identity and behavior. Here we use
single-cellRNAsequencingatkeydevelopmentaltimepointstointerrogatecellularcontributions
to coronary vessel patterningand maturation. We perform transcriptional profilingto definea
heterogenous population of epicardium-derived cells (EPDCs) that express unique chemokine
signatures. We identify a population of Slit2+ EPDCs that emerge following epithelial-to-
mesenchymal transition (EMT), which we term vascular guidepost cells. We show that the
expression of guidepost-derived chemokines such as Slit2 are induced in epicardial cells
undergoing EMT, while mesothelium-derived chemokines are silenced. We demonstrate that
epicardium-specific deletion of myocardin-related transcription factors in mouse embryos
disrupts the expression of key guidance cues and alters EPDC-EC signaling, leading to the
persistenceofanimmatureangiogenicECidentityandinappropriateaccumulationofECsonthe
epicardial surface. Our study suggests that EC pathfinding and fate specification is controlled
byacommonmechanismandguidedbyparacrinesignalingfromEPDCslinkingepicardialEMT
to EC localization and fate specification in thedeveloping heart.
1DepartmentofMedicine,AabCardiovascularResearchInstitute,UniversityofRochesterSchoolofMedicineandDentistry,Rochester,NY,USA.
2DepartmentofBiomedicalEngineering,UniversityofRochester,Rochester,NY,USA.3GenomicsResearchCenter,UniversityofRochesterSchoolof
MedicineandDentistry,Rochester,NY,USA.4DepartmentofMicrobiologyandImmunology,UniversityofRochesterSchoolofMedicineandDentistry,
Rochester,NY,USA.5LeonH.CharneyDivisionofCardiology,DepartmentofMedicine,NewYorkUniversitySchoolofMedicine,NewYork,NY,USA.
6DepartmentofPediatrics,UniversityofRochesterSchoolofMedicineandDentistry,Rochester,NY,USA.7DepartmentofPharmacologyandPhysiology,
UniversityofRochester,Rochester,NY,USA.8Presentaddress:DepartmentofIntegrativeBiologyandPhysiology,MolecularBiologyInstitute,Eli&Edythe
BroadCenterofRegenerativeMedicineandStemCellResearch,UCLACardiovascularTheme,DavidGeffenSchoolofMedicine,UniversityofCalifornia,Los
✉
Angeles,CA,USA. email:eric_small@urmc.rochester.edu
NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications 1
;,:)(0987654321
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
C
oronary endothelial cells (ECs) organize into an intricate enrichment (Aldh1a2, Tbx18, Tcf21, Wt1) and did not express
vascular network that provides the heart with oxygen and highlevelsofcardiomyocytegenes(Tnnt2,Myh7)(Supplementary
nutrientsandremovesmetabolicwaste.Duringembryonic Fig. 1e). Increased expression of the mesenchymal cell marker
development,localizedspecificationofimmatureECsintoarterial PdgfrawasobservedinanumberofGFP + cellsatE16.5,consistent
andvenousfatesoccurswithinthecompactmyocardiumandsub- withtheacquisitionofamotilephenotypeanddifferentiationinto
epicardium,respectively1.ECfatespecificationandmaturationare interstitial cell types (Supplementary Fig. 1f–h).
accomplished through cell-intrinsic transcriptional programs that Single-cell RNA-sequencing (scRNA-seq) was performed on
facilitate appropriate interconnections of the blood-supplying and EPDCscapturedusingthe10×Genomicsplatform(Fig.1d).We
blood-drainingvascularbeds2.Analysesofintersomiticandretinal excluded cell doublets based upon unique molecular identifier
vessel development identified a population of endothelial tip cells counts, and mitochondrial and ribosomal gene expression
that are particularly responsive to secreted angiogenic factors patterns were analyzed and filtered to obtain 3405 (E12.5) and
such as vascular endothelial growth factor (Vegf), highlighting 2436(E16.5)singleEPDCs(SupplementaryFig.2a,b).Todefine
the functional heterogeneity of ECs and revealing mechanisms the cellular heterogeneity within the epicardium, we performed
governing vascular pathfinding, remodeling, and maturation3. an integration of E12.5 and E16.5 data sets using canonical
Clinicalstudiesaimedatimprovingperfusionoftheischemicheart correlation analysis (CCA) followed by uniform manifold
and skeletal muscle have attempted to recapitulate these develop- approximation and projection (UMAP) using Seurat to rule out
mental angiogenic programs4. However, the mechanisms through batch effects (Supplementary Fig. 3a–d), and present a merged
which coronary ECs coordinate positional information and fate analysisofE12.5andE16.5cells(Fig.1e).Thisanalysisrevealed
specificationremainelusive,andcurrenttherapeuticstrategieshave 8distinctpopulations(C1-C8)withaconsiderablecontribution
failedto generate a robust, functional vascular network. of proliferation state and developmental age to cellular
Theepicardiumconsistsofa singlelayer ofmesothelialcellson phenotype(Fig.1e,fandSupplementaryFig.4a,b).Tofacilitate
the surface of the heart that harbors a population of multipotent theidentificationofepicardial cellphenotypes,E12.5andE16.5
progenitors. Following epithelial-to-mesenchymal transition data were merged and a CCA was performed with previously
(EMT),epicardium-derivedcells(EPDCs)migrateintothecompact published scRNA-seq data obtained from the postnatal day 1
myocardium and differentiate into cardiac fibroblast and vascular mouse heart17 (Supplementary Fig. 4c, d). Within these
muralcelllineages5–7.Constructionofthecoronaryplexusrequires populations, five broad identities emerged, consistent with
theintegrationofepicardium-derived muralcellswith arterialand marker genes identified by hierarchical clustering and gene
venous ECs derived from the sinus venosus and endocardium5,8,9. ontology (GO) analysis (Fig. 1g–k and Supplementary 5a, b;
Genetic or mechanical disruption of the epicardium has also Supplementary Dataset 1): (1) early developmental stage
revealed important paracrine contributions to cardiomyocyte progenitor(C1,C3);(2)earlyEMT(C5);(3)latedevelopmental
growth10 and coronary plexus formation11,12. Our previous study stage mesothelial (C2, C4); (4) late developmental stage EMT/
found that epicardial EMT is required for coronary blood vessel mesenchymal (C6, C7); and (5) a rare population of approxi-
maturationandintegrity,atleastpartiallyviacontributingvascular mately 40 cells (C8, 1.64% of total) that display an enrichment
pericytes to the growing plexus7. inIGFpathwaygenesandexpresshighlevelsofCav1previously
In this study, we performed single-cell RNA-sequencing of implicated in zebrafish heart regeneration13.
EPDCs and coronary ECs at critical developmental stages to EPDCsinC1andC3arecharacterizedbyrobustexpressionof
gain insight into the mechanisms responsible for patterning of epicardial gene markers Tbx18 and Upk3b18,19, and GO terms
the developing coronary vasculature via distinct epicardial cell associated with proliferation and epithelial cell differentiation,
populations13–15. We found that epicardial EMT is not only defining populations of self-replicating E12.5 mesothelial cells
responsible for the differentiation of EPDCs into vascular mural (Fig. 1g, h). In contrast, C5 is enriched in E12.5 EPDCs that
lineages7, but also restricts the expression of chemotactic signals exhibitapredispositiontowardsEMTpriortotheacquisitionofa
to discrete populations of mural cells that provide detailed posi- motilegeneprogram,basedontheexpressionofearlymarkersof
tional information, reminiscent of the guidepost neuron16. the mesenchymal and smooth muscle phenotype, including
Genetic disruption of epicardial EMT in mice leads to profound Pdgfra, Itgb5, Sox9, and Tagln220,21 (Fig. 1g, i). C2 and C4
alterations in EC developmental trajectory, which includes the contain an over-abundance of E16.5 EPDCs that express genes
accumulation of an immature EC population within the sub- relatedtomaintenanceofmesothelialcharacteristics(Maf,Btg2),
epicardium. Importantly, EC maturationand migration are both likely representing cells that remain on the cardiac surface22,23
directly controlled by angiogenic chemokines, providing a para- (Fig. 1g, j). Genes encoding extracellular matrix proteins such as
digm that coordinates EC localization and arteriovenous (AV) Postn, Dpt, and Col3a1 are robustly expressed in E16.5 EPDCs
specification. Harnessing the principles that define the spatial inC6andC7,consistentwiththeacquisitionofamesenchymal
architecture of the developing coronary vasculature may provide phenotype20(Fig.1g,k).Ofnote,thesedataalsorevealedunique
strategies to stimulate angiogenesis and improve perfusion of vascular programs based upon the emergence of angiogenesis
ischemic heart tissue, a limiting aspect of regenerative medicine among the most enriched GO terms at E16.5, and the
approaches. enrichment of Hspb1 and Dlk124,25 in mesothelial cells and
Ramp2 and Sfrp226,27 in mesenchymal cells (Fig. 1g, j, k and
Supplementary Fig. 5a).
Results
Single-cell analysis of epicardium-derived cell heterogeneity.
Coronary endothelial cell AV specification and integration of Distinct epicardium-derived vascular guidance programs. We
the arterial and venous vasculature coincides temporally with next evaluated the divergence of mesothelium and mesenchyme
epicardial EMT, between embryonic day (E) 12.5 and E16.59 from a common epicardial progenitor, and the potential contribu-
(Fig. 1a). To investigate epicardial contributions to the growing tionofthesedistinctcellularpopulationstoangiogenicprocesses,by
+
coronary plexus at these timepoints, GFP-positive (GFP ) assessing pseudotime trajectory using Monocle, an unsupervised
EPDCs were isolated from Wt1CreERT2/+ ;RosamTmG mouse learning algorithm that identifies branch points and cell commit-
embryosbyfluorescence-activatedcellsorting(FACS)(Fig.1b,c mentdecisions28,29.WeobservedanabundanceofE12.5progenitor
andSupplementaryFig.1a–d).GFP + cellsdisplayedepicardialgene cellsatthestartofpseudotime(primarilyC1,C3),thattransitionto
2 NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications
a
GFP DAPI
E12.5 E16.5
tdTomato+
cell states ultimately dominated by E16.5 EPDCs (Fig. 2a, b and across cell states revealed that mesothelial cells within state 2
Supplementary Fig. 6a, b). Cell state 2 is enriched in E16.5 meso- maintain expression of genes such as Wt1, Msln, and Upk3b18,
thelialcells(C2,C4),whilecellstate3iscomposedofmesenchymal while cells in state 3 show downregulated expression Msln and
cells(C6,C7)followinganearlyEMTintermediate(C5)(Fig.2b). Upk3,b as well as Pdpn and Pdgfa30,31, markers that are generally
Analysis of pseudotime kinetics of differentially regulated genes associatedwiththemesothelium(Fig.2c).Instead,state3cellsare
+PFG
4
FACS
cDNA Library Cells Oil Sequencing 10x Barcoded Beads GEMs
-5.0 0.0 2.5
UMAP 1
2 PAMU
E12.5
E16.5 4
2
0
-2
-2.5 5 -5.0 0.0 2.5
UMAP 1
2 PAMU
b c
2 100 90 80 70
0 60
50
40
30 -2 20
10
0
E12.5 E16.5
-2.5 5.0
)%( noitroporp
retsulc
d
2,2,2 40 519 301 153 355 702 41
94 414
81
1043
1931 161
Progenitor
E12.5 Progenitor EMT Mesothelial Mesenchymal
E16.5 (C1 & C3) (C5) (C2 & C4) (C6 & C7) Rare regulation of cell cycle
(C8)
mesodermal cell differentiation
Tbx18 negative regulation of gene expression
Upk3b pulmonary valve development
Pdgfra
Itgb5 glomerular visceral epithelial cell differentiation
Sox9
Tagln2
0 1 2 3 4 5 6
Hspb1 log10 (p-value)
Btg2
Apoe
P D os lk t 1 n Rel.
Expression
Dpt
2
Ptn 1 Col3a1 0
Ebf1 -1
Cav1 -2 Igf1
Csrp2
tnemhcirnE
mreT
OG
ssecorP
lacigoloiB
EMT
positive regulation of cell proliferation
positive regulation of cellular process
regulation of apoptotic process
negative regulation of transcription
mesenchyme morphogenesis
0 2 4 6 8 10
log10 (p-value)
tnemhcirnE
mreT
OG
ssecorP
lacigoloiB
e f
g h i
Hmga2
j Mesothelial Mesenchymal
Maf
extracellular matrix organization extracellular matrix organization
regulation of cell migration cellular response to cytokine stimulus
positive regulation of cell differentiation embryonic organ morphogenesis
regulation of cell proliferation positive regulation of epithelial cell proliferation
regulation of IGFR signaling pathway regulation of angiogenesis
regulation of angiogenesis retinal ganglion cell axon guidance
0 5 10 15 0 5 10 15 20 25 30
log10 (p-value) log10 (p-value)
tnemhcirnE
mreT
OG
ssecorP
lacigoloiB
tnemhcirnE
mreT
OG
ssecorP
lacigoloiB
Wt1CreERT2
E12.5 E16.5 x
Aorta Rosa26 m-tdTom m-eGFP LA Epi
RA LA
+TAM
Vascular
Plexus EMT Rosa26 m-eGFP RA
Epi LV RV
RV
RV LV Epi
EPDC Artery Vein
1 2 3 4 5 6 7 8
Mesothelial
Progenitor
EMT
5.0
M
TA
5.9 5.01 5.21 5.61
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
Harves
H
t arvest
Birth
Embryonic Day
Mesenchymal
k
Fig.1Characterizationofepicardialcellheterogeneityinthefetalheart.aSchematicofepicardiumandvasculaturedevelopment.bExperimental
strategyforlineagetracingepicardium-derivedcellsinWt1CreERT2;R26mTmGembryos.TAMwasadministeredtopregnantdamsatembryonicday(E)9.5
andE10.5andembryoswereharvestedatE12.5andE16.5.cRepresentativeimagesofmouseembryosatembryonicstageE12.5andE16.5usedfor
collectionofGFP+epicardialcells(green).DAPIstainingwasutilizedtovisualizenuclei(blue).Scalebaris100μm(E12.5)and50μm(E16.5).
Immunostainingwasrepeatedindependently3timeswithsimilarresults.dFACS-basedenrichmentofWt1-lineage-derivedepicardialcellspriortosingle-
cellcaptureusing10×GenomicsChromiumController.RefertoSupplementaryFig.1c,dforFACSsequentialgatingandenrichmentofepicardialcells.
eandfUMAPofsingle-celltranscriptomesofE12.5(3405cells)andE16.5(2436cells)epicardialcellspresentedbyedevelopmentalstageandfcell
identity,withtherelativecontributionofeachcellclusterwithineachdevelopmentalstageindicatedontheright.Thenumberofcellspercluster(C)is
listednexttothecorrespondingcolorinthegraph.gHierarchicalclusteringofdifferentiallyexpressedgenesbycellidentityrepresentedasaheatmap.
Relative(Rel.)expressionrepresentsscalednormalizedexpression.h–kGOanalysisindicatesmostenrichedbiologicalprocesseswithincellsdefinedas
hprogenitor(C1andC3),iEMT(C5),jmesothelial(C2andC4),andkmesenchymal(C6andC7).GO-termenrichmentsignificancewasdetermined
usingFisherexacttest.Epiepicardium,EMTepithelial-to-mesenchymaltransition,RArightatrium,RVrightventricle,LAleftatrium,LVleftventricle,
m-tdTommembranetdTomato,m-eGFPmembrane-enhancedgreenfluorescentprotein,TAMtamoxifen,GEMsGelBead-in-Emulsion.
NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications 3
a
5
0
-5
-10
-10 -5 0 5 10
pseudotime 1
2
emitoduesp
3.4%
67.7%
55%
28.5%
16.5% E12.5
E16.5
28.9%
5
0
-5
-10
-10 -5 0 5 10
pseudotime 1
2
emitoduesp
Mesothelial
Vim
Pdgfra
Zeb2
Postn
Serpine2
Mest
Sept11
Ptn
Tgm2
S100a6
Fbln2
Upk3b
Plxna4
Pdgfa
Progenitor Pdpn 1
Mesothelial 2
3 Nbl1
4
Col1a2 5
Rspo1
6
7 S100a1
8 Fabp3
Mesenchymal Angptl7 Cluster
Mesenchymal
c BP
State 1
State 2 Tagln2
Raph1
BP Vcam1
Lhfp
Emilin1
H2afz
Hmgb1
Mdk
State 3 Glipr2
Tnni1
Arhgap29
Smim1
Lrrn4
Fmod
b
Npnt
Adam33 Rel.
Igfbp5 Expression
Fras1 3
Gm12840
Tnnt2 2
Fabp5
Atf3 1
EMT
Vamp8 0
Jun
Tcea3 -1
Hspb1 -2 Btg2
Cebpb -3 Gm20186
d
Snai2 *
10.0
1.0
0.1
0 5 10 15 20
Zeb2 *
10.0
1.0
0.1
0 5 10 15 20
Sox9 *
10.0
1.0
0.1
0 5 10 15 20
Slit2 *
10.0
1.0
0.1
0 5 10 15 20
noisserpxE
evitaleR
Mesothelial Mesenchymal
Wt1
10.0
1.0
0.1
0 5 10 15 20
Msln *
10.0
1.0
0.1
0 5 10 15 20
Upk3b *
10.0
1.0
0.1
0 5 10 15 20
Wnt5a * 10.0 Angptl2 *
10.0
1.0 1.0
0.1 0.1
0 5 10 15 20 0 5 10 15 20
Sema3c * 10.0 Tnc *
10.0
1.0 1.0
0.1 0.1
0 5 10 15 20 0 5 10 15 20
Sema3d
10.0
1.0
0.1
0 5 10 15 20
Pseudotime Pseudotime
1 2 3 4 5 6 7 8
noisserpxE
evitaleR
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
Fig.2Epicardial-to-mesenchymaltransitionrestrictsexpressionofsecretedligandsgenes.aMonocle-generatedpseudotimetrajectoryrevealsthe
compositionofthreecellstatesbasedonthedevelopmentalstage(%).Cellsinstate1areatthebeginningofpseudotime.Cellstates2and3diverge
atacommonbranchpoint(BP).bPseudotimetrajectoryrevealsthecompositionofcellidentitywithincellstates.State1containsepicardialprogenitor
cellsfromCluster1(C1)/C3.State2ispopulatedbymesothelialcellsfromC2/C4.State3emergesfromacommonprogenitorthroughatransient
statecharacterizedbycellsinC5activelyundergoingEMTandculminatesinmesenchymalcellsofC6/C7.cHierarchicalclusteringvisualizationof
genesthatdefinepseudotimestates.Relative(Rel.)expressionrepresentsthescaledexpressionofrlognormalizeddata.dPseudotime-dependent
genesaugmentedinmesenchymalversusmesothelialcells.Cellsarecoloredaccordingtocellclusteridentity.*Geneswithsignificantcorrelationwith
pseudotimestate.
4 NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
enrichedinEMTandmesenchymegenessuchasSnai2,Zeb2,Sox9, (Fig.4e).RNAscopeFISHalsoconfirmedthereductionofSema3d
Postn,andPtn20(Fig.2c,dandSupplementryFig.6c).Tofurther and Slit2 in EPDCs of MRTFepiDKO hearts, compared to controls
interrogate the angiogenic programs we identified in mature (Supplementary Fig. 10a–c). These findings corroborated our
mesothelialandmesenchymalcells,weprobedpseudotimekinetics scRNA-seq results revealing the restriction of vascular guidance
forgenes encodingaxonguidancecuesthatregulateneuronaland cues to distinct populations of epicardium-derived cells, and pro-
vascularmigrationandpathfindingduringdevelopment32.Among vided evidence that EMTcontributes to the expression and locali-
the more restricted guidance genes, we found epicardium-derived zationof these factors.
mesenchymal cells express an over-abundance of Angptl2, Tnc,
and Slit2, whereas epicardium-derived mesothelial cells display
EMT regulates the expression of genes encoding vascular gui-
an enrichment in Wnt5a, Sema3c, and Sema3d (Fig. 2d and
dance cues. In order to further examine the effect of EMT on
SupplementaryFig.6c;Supplementary Dataset 2).
ToconfirmthatexpressionofSlit2andSema3disenrichedin v
ce
a
l
s
l
c
s
u
i
l
s
a
o
r
la
g
t
u
e
i
d
da
f
n
ro
ce
m
ge
E
n
1
e
1.
e
5
xp
e
r
m
es
b
s
r
io
yo
n
s
,w
w
e
it
t
h
re
T
at
G
ed
Fβ
p
1
rim
an
a
d
ry
P
e
D
p
G
ica
F
r
-
d
B
i
B
al
,
epicardium-derived mesenchyme and mesothelium, respec-
tively, we performed RNAscope multiplex fluorescence in situ which resulted in the downregulation of epicardial/mesothelial
genes and upregulation of EMT-associated and mesenchymal
hybridization (FISH) on heart sections obtained from genes (Fig. 5a)34. Sema3c and Sema3d were both significantly
Wt1CreERT2;R26RmTmG embryos labeled at E9.5/E10.5 and
suppressed upon induction of epicardial EMT, whereas Tnc and
collected at E12.5 (pre-EMT), E14.5 (mid-EMT), and E16.5
+ Slit2 were upregulated (Fig. 5a). These gene expression changes
(post-EMT). Sema3d is observed broadly within GFP
are consistent with their in vivo distribution within mesothelial
mesothelial cells on the epicardial surface at all time points
cellsandmesenchymalcells,respectively.Wealsofoundevidence
examined(Fig.3a,bandSupplementaryFig.7a,b).Incontrast,
that EMT induces the mural cell phenotype based on the
Slit2 is observed on the epicardial surface at E12.5, and is
expression of pericyte marker genes Pdgfrb and Cspg4 (Fig. 5a).
also expressed within a discrete population of epicardium-
We, therefore, re-evaluated EPDC populations 5, 6, and 7 (from
derived mesenchymal cells that are closely associated with
Fig.1)toestablishtheidentityofWt1-lineagemesenchymalcells
Pecam1-expressing EC as early as E14.5, and most notably at and define the source of epicardium-derived guidance cues
E16.5 (Fig. 3a, c and Supplementary Fig. 7a, c). Of note, th
+
e (Fig.5b).Wewereabletoidentifyfibroblasts(Fb-1,Fb-2,Acta2 +
expression of key angiogenic factors often increased in GFP
Fb) based on increased expression of Col1a1, Postn, and Tnc;
EPDCs between E12.5 and E16.5, regardless of localization to
smooth muscle cells (SMC-1, SMC-2) based on increased
mesothelial or mesenchymal cell populations (Supplementary
expression Tagln; and pericytes (PC) based on increased
Fig. 7d). The striking restriction of genes encoding secreted
expression of Pdgfrb (Fig. 5c). Slit2 and Angptl2 are enriched
vascularguidancecuestodistinctpopulationsofEPDCsledus
in FB1 and FB2, and Slit2 is especially pronounced in peri-
tospeculatethatangiogeniccuesmaybecoordinatelyregulated
cytes (Fig. 5c). The Cspg4CreERT2 mouse line has been used to
with epicardial cell fate.
lineage trace vascular mural cells, including pericytes35. FISH
using probes against Gfp and Slit2 on heart sections obtained
from Cspg4CreERT2;R26RmTmG embryos obtained at E17.5
Disruption of epicardial EMT alters expression of vascular
revealed Slit2 transcripts within some Cspg4 lineage-derived
guidance cues. Myocardin-related transcription factors (MRTFs)
muralcells(Fig.5d).Collectively,thesedatadescribeaparadigm
are mechanosensitive transcriptional co-activators of serum
whereby epicardial EMT is responsible for the restriction of
response factor (SRF) that facilitate induction of cell contractility
individual chemotactic cues to distinct epicardium-derived
and motility gene programs33. We previously reported that
epicardium-specific Cre-mediated deletion of Mrtf-a and Mrtf-b lineages, including coronary mural cells, which may represent a
vascular guidance cell reminiscent of the guidepost neuron16.
(MRTFepiDKO) or Srf (SRFepiKO) during development impedes
epicardial EMT, precipitating epicardium detachment and defects
in coronary plexus formation and EC integrity7. This phenotype Single-cell transcriptomics defines the EC response to epi-
was attributed to a depletion of microvascular pericytes, which cardial dysfunction. Coronary EC re-specification into arterial
partiallyphenocopiedtheSRF-dependentemergenceofmuralcells and venous fates occurs at around E14.51,2. In order to inter-
from the epicardium19. In order to evaluate whether epicardial rogate the impact of epicardial EMT on individual ECs, we iso-
EMT controls the angiogenic programs identified by scRNA-seq, latedCD31 + /CD45 − cellsfromMRTFepiDKOandControlhearts
−
weusedFACStoisolateGFP non-EPDCs(enrichedinmyocytes), atE14.5byFACSfollowedbysingle-cellcaptureandscRNA-seq
+
and GFP EPDCs from wild-type (control) and mutant embryos using the 10× Genomics platform (Fig. 6a and Supplementary
forRNA-sequencing(Fig.4aandSupplementaryFig.8a–d).EPDCs Figs. 11a–c and 12a, b). CCA defined 9 unique EC populations
obtained from MRTFepiDKO and SRFepiKO mice are tran- that were enriched in Pecam1 (Supplementary Fig. 13a, b), and
scriptionally indistinguishable based on principal component ana- alleviated concerns of batch effects based on genotype and cell
lysis (PCA), but diverge from control EPDCs stemming from the cycle analysis (Supplementary Fig. 13c, d; Supplementary Data-
dysregulationof2,518genes(Fig.4b,candSupplementaryFig.9a, set3and4).Sincecellcycleisreportedtounderlietranscriptional
b). MRTFepiDKO EPDCs display a significant reduction in genes differences during ECdifferentiation9,36,we performed unbiased
associated with biological processes such as cell migration (Mylk, clustering without regression of cell cycle to allow for identifi-
Vin), ECM production (Col1a2, Col3a1), and mesenchymal cell cation of EC phenotypes that emerge upon disruption of epi-
differentiation (Pdgfra, Acta2, Tagln) (Supplementary Fig. 9c–i). cardial EMT (Fig. 6b and Supplementary Fig. 13e). This analysis
Surprisingly, MRTFepiDKO EPDCs also exhibit a significant down- defined9uniquecellpopulationsconsistingofECscategorizedas
regulation of genes associated with paracrine regulation of che- sinusvenosus(SV),coronaryplexus,angiogenic,venous,arterial,
motaxisandaxonguidance(SupplementaryFig.9c,j).Indeed,axon endocardial, and general endothelial (Fig. 6b). UMAP plots of
guidancewasthemostsignificantlydysregulatedbiologicalprocess filtered and typed ECs showed that cell clusters C3-C5 and C9
in MRTFepiDKO EPDCs, represented by secreted ligands such as weresignificantlyenrichedwithMRTFepiDKOECs(Fig.6b,cand
Efna5, Sema3d, Slit2, Slit3, and Wnt5a (Fig. 4c, d). qRT-PCR Supplementary Fig. 13f, g). Violin gene expression plots defined
confirmed genes encoding select guidance cues are enriched in MRTFepiDKO-enriched sub-populations of SV and coronary
EPDCs, and significantly downregulated upon MRTF deletion plexusECsthatexhibitdifferentialexpressionofAplnr,Apln,and
NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications 5
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
a b c
Sema3dSlit2 Gfp DAPI Pecam1 Sema3d Gfp DAPI Pecam1 Slit2 Gfp DAPI
E12.5 E12.5 E12.5
Endo Endo Endo
E14.5 E14.5 E14.5
Endo Endo Endo
E16.5 E16.5 E16.5
Endo Endo Endo
a’ b’ c’
Fig.3Insituanalysisconfirmstheexpressionandlocalizationofvascularguidancegenesinepicardium-derivedcells.aFISHusingprobesagainstGfp
(green)todetectepicardium-derivedcellsandSema3d(white)orSlit2(red)revealsdiverginglocalizationofvascularguidancecueswithintheepicardiumand
interstitiumbetweenembryonic(E)12.5andE16.5.a′,3×zoomofE16.5.bExpressionofSema3d(red)inWt1lineage-derivedcells(Gfp+,green)relativeto
Pecam1+(plateletendothelialcelladhesionmolecule-1,white)endothelialcells.b′,3×zoomofE16.5.cExpressionofSlit2(red)inWt1lineage-derivedcells
(Gfp+,green)relativetoPecam1+(white)endothelialcells.c′3×zoomofE16.5.Yellowarrowhead,Gfp+/Sema3d+cells.Orangearrowhead,Gfp+/Slit2+cells.
Dashedyellowlinerepresentstheendocardium–myocardiumborder.DAPIstainingwasutilizedtovisualizenuclei(blue).Scalebar,20μm.Scalebar3×zoom,
10μm.Endoendocardium.
6 NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications
a b c
EPDCcTNTDAPI
E12.5 hearts1) Mrtf-a-/- ; Mrtf-bfl/fl GFP
Hrs: 0 24 48
+ad-GFP +TGFβ2
+ad-βgal or Cre +PDGF-BB
Axon Guidance
(GO: 0007411)
A bli m A 1 lc a m C ac n C a o 1 l c 3 a C 1 ol 4 a C 5 ol 5 a C 2 ol 6 a C 3 ol 9 a C 2 xcl 1 E 2 f n a E 5 gr 2 E p h a E 7 p h a 8 Ezr Flrt 2 G as 1 My h 1 N 0 e o 1 Nfi b R g m b R ps 6 R k a p 3 s 6k S a e 6 m a S 3 l d it 2 Slit 3 W nt 5 a
MRTFepiDKO
Control
the proliferative marker Cdk19,37 (Fig. 6d). Angiogenic genes then identified epicardium-derived vascular guidance genes that
Sparcl1 and Cd4738 and pre-arterial genes Dll4 and Sox179 were areinfluencedbyepicardialEMTbycross-referencingtoourbulk
alsoenrichedinMRTFepiDKOdominatedclusters(Supplementary RNA-sequencingofMRTFepiDKOEPDCs(SupplementaryFig.16a
Fig. 14a–c). However, genes associated with the endocardium and Supplementary Dataset 5). We identified 99 genes encoding
(Npr3,Nfatc1)8,39,venous(Nr2f2)9ormaturearterial(Gja4,Gja5, ligands that are dysregulated upon Mrtf deletion, potentially
Fbln5)9,38 were similarly expressed in UMAP clusters of Control impacting pathways related to proliferation, growth factor signal-
and MRTFepiDKO ECs (Fig. 6d and Supplementary Fig. 14c, d). ing,non-canonicalWntsignaling,ECM–receptorinteractions,and
Overall,thesedatarevealthatdisruptionofepicardialEMTleads axon guidance (Supplementary Fig. 16a–c); a total of 52 ligands
totheemergenceofapopulationofECsthatexhibitanimmature thatarenormallyrestrictedtothemesotheliumormesenchymein
vascular cell phenotype. control mice are disrupted (Supplementary Fig. 17a–c). Notably,
34 genes encoding receptors that are detected in ECs were sig-
Identification of potential receptor–ligand pairings between nificantly altered following Mrtf deletion within the epicardium
the endothelium and epicardium. Coordination of cell-to-cell (SupplementaryFig.18),whichledtothepotentialdisruptionof87
signalingiscriticaltobuildingvascularnetworksandunderliesthe receptor–ligandpairs(SupplementaryFig.15bandSupplementary
acquisition of arterial and venous cell identity. To characterize Dataset6).
the intercellular signaling between EPDCs and coronary ECs Wenextre-evaluatedthesingleECtranscriptomeandconducted
that influence developmental angiogenesis, we constructed a RNAFISHtoevaluatethedistributionofkeycellsurfacereceptors
receptor–ligand visualization by matching EC-expressed receptors within the fetal heart, focusing on candidate receptors for
toepicardium-derivedligandsidentifiedbyscRNA-seq,indicating Sema3d (mesothelium-derived) and Slit2 (guidepost cell-derived).
whetheraparticularligand isenrichedwithinepicardium-derived We detected the semaphorin co-receptor Nrp1 within all EC
mesothelial or mesenchymal cells (Supplementary Fig. 15a). We clusters(Fig.6e).RNAFISHconfirmedthewidespreadexpression
CSS
Non-EPDCs Control EPDCs
FACS MRTFepiDKO EPDCs SRFepiKO EPDCs
250K GFP GFP
91.2% 7.92%
200K
150K
100K
50K
0
-103 0 103 104 105
PC1: 49% variance
ecnairav
%32
:2CP
20
0
-20
-40
2) Srf fl/fl
-60
-25 0 25 50
d
Rel. Expression
1 0 1
Biological
Process
GO
Term
Enrichment
Control EPDCs vs MRTFepiDKO EPDCs
DEGs = 2,518
Axonal Guidance Signaling
Hepatic Fibrosis / Stellate Cell Activation
Glioblastoma Multiforme Signaling
IL-8 Signaling
Aryl Hydrocarbon Receptor Signaling
Integrin Signaling
RhoA Signaling
eNOS Signaling
Phagosome Maturation
Protein Kinase A Signaling
0 2 4 6 8 10
-log10 (p-value)
e
qRT-PCR: Vascular Guidance Genes
p=9.2E-04
60 Control EPDCs 50 MRTFepiDKO EPDCs
40
30 p=0.0018 20
12
10
8
6
4 non-EPDC
2
0
Efna5 Sema3d Slit2 Slit3 Wnt5a
ANRm
s81 /
noisserpxe
.ler
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
p=7.6E-04 p=0.0135 p=0.0140
p=2.6E-04 p=1.64E-06
p=4.1E-07
Fig.4Geneticdisruptionofepithelial-to-mesenchymaltransitionalterstheexpressionofvascularguidancecues.aSchematicofexperimentaldesign
toisolateepicardialcells(EPDC)ofindicatedgenotypesforbulkRNA-seq.Embryonicday(E)12.5heartswereremovedfromMrtf-a−/−;Mrtf-bfl/fl,
andSrffl/flmiceandincubatedwithadenovirus(ad)expressingGFPtolabelepicardium(green),andeitherad/βgalactosidase(βgal)orad/Cre.Hearts
wereculturedexvivoinTGFβ2[2ng/mL]andPDGF-BB[20ng/mL]toinduceEMT,andGFP+epicardialcellswerecollectedusingFACS.GFP−cells
werecollectedasnon-EPDCs.cTNT,cardiactroponinT(red),andDAPIstainingwereutilizedtovisualizenuclei(blue).Scalebar,50μm.Referto
SupplementaryFig.8eforFACSsequentialgatingandenrichmentofepicardialcells.bPrincipalcomponentanalysis(PCA)ofGFP−non-EPDCsandGFP+
EPDCsfromcontrol,Mrtf-a;Mrtf-bdoubleknockout(MRTFepiDKO)orSrfknockout(SRFepiKO)mice.cAnalysisofdifferentiallyexpressedgenes(DEGs)
revealsbiologicalprocessesthatareenrichedbetweenMRTFepiDKOandcontrolEPDCs.GO-termenrichmentsignificancewasdeterminedusingFisher
exacttest.dHeatmaphighlightingtherelativeexpressionofgenesinvolvedinaxonguidancesignalinginEPDCsoftheindicatedgenotype.Relative(Rel.)
expressionrepresentsthescaledexpressionofrlognormalizeddata.eExpressionofgenesencodingaxonguidancecueswasvalidatedbyqRT-PCR.
Valuesarerepresentedasafoldchangeinexpressionrelativetonon-EPDCs(dashedlineat1).nrepresentssamplesacquiredfromindependentembryos,
whichwereanalyzedin1experiment.n=3non-EPDCs,n=4forEfna5,Sema3d,Slit3,Wnt5a,andn=3forSlit2inControlEPDCs;n=3MRTFepiDKO
EPDCswereanalyzed.Dataarepresentedasmeanvalues±SEM.Statisticalsignificancewasdeterminedbyatwo-sampleunpairedStudent’st-test.TGFβ2
transforminggrowthfactorbeta-2,PDGF-BBplatelet-derivedgrowthfactorBB,m-tdTommembranetdTomato,m-eGFPmembrane-enhancedgreen
fluorescentprotein,TAMtamoxifen.
NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications 7
a
Pecam1 Slit2 Gfp DAPI
ofNrp1withinamajorityofPecam1-expressingECs,whileSema3d Supplementary Dataset 7). While each pseudotime state is com-
is restricted to mesothelial cells on thecardiac surface(Fig. 6f and posed of ECs obtained from animals of both genotypes, states 5
Supplementary Figs. 19, 20a). In contrast, Nrp2 and Robo4 are and 7 are enriched in ECsfrom control mice, and states 1–4 are
primarily restricted to angiogenic and coronary plexus EC within enriched in MRTFepiDKO ECs (Fig. 7a and Supplementary
clusters 2, 5, and 9 (Fig. 6e). FISH confirmed the expression of Fig. 21b, c). Cell state also correlates with cell cycle activity
+
Robo4withina distinct populationPecam1 ECs that oftenreside (Fig. 7b), consistent with reports that EC maturation coincides
+
in close proximity to Slit2 cells (Fig. 6g and Supplementary with reduced proliferation9,36. Pseudotime originates in state 1
Figs. 19, 20b). These data reveal the potential for complex with SV and angiogenic coronary progenitors, marked by the
intercellular cross-talk between EPDC and EC that may influence expressionofAplnr,Apln,andSparcl1,andanover-abundanceof
coronaryangiogenesis. cells in the G2/M and S phases of the cell cycle (Fig. 7b, c). ECs
obtainedfromcontrolheartsprimarilyfollowedatrajectoryfrom
Disruption of epicardial EMT alters EC developmental trajec- progenitor state 1 through a mixed venous/primed arterial EC
tory.TodefinehowECdevelopmentaltrajectoryisalteredupon state 5 (represented by Nr2f2, Ephb4, Dab2) towards terminal
disruptionofepicardium-derivedparacrinesignaling,weordered states 6 and 7. State 6 displays immature arterial-like character-
ECs obtained from control and MRTFepiDKO mice at E14.5 istics,withrelativelylowerlevelsofthevenousmarkersNr2f2and
in pseudotime using Monocle (Supplementary Fig. 21a and Ephb4, elevated levels of the early arterial gene Efnb2, and
5.0 5.9 5.01 5.51 5.61 5.71
b
20 Vehicle
15 TGFβ1/PDGF-BB
10
6
4
2
0
Upk3b Wt1 Zeb2 Sox9
Se
ma3c
Se
ma3d Slit2 Tnc Pdgfrb Cspg4
d Cspg4 Cre
x
ERT2
TAM TAM
Harvest
Rosa26 m-tdTom m-eGFP Birth
+TAM
Rosa26 m-eGFP Embryonic Day
ANRm
s81
/ ANRm
.ler
2
0
p=2.7E-05 -2
-4
-2 2
Epicardial Mesenchymal Vascular Guidance Genes Mural Cells UMAP 1
2
PAMU
4
-6
2
1
0
leveL
noisserpxE
EMT / Mesenchymal Clusters
-4 0
Tcf21 Col1a1 Postn
5 4 4 3
3 2
2 1 1
0 0
Tagln Acta2 Pdgfrb
3 4 2.0
3 1.5
2
2 1.0
1 1 0.5
0 0 0.0
Tnc Slit2
2.0
2 1.5
1.0 1
0.5
0
leveL
noisserpxE
FB-1
FB-2
SMC-1
SMC-2
PC
Acta2+ FB
c
Angptl2
2.0
1.5
1.0
0.5
0.0 0.0
leveL
noisserpxE
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
p=6.0E-04
p=0.0217
p=0.0017 p=7.3E-05 p=0.0068
p=0.0011
p=0.0080 p=0.0016 p=0.0327
FB-1 FB-2 SMC-1
SMC-2
PC Acta2+ FB
Fig.5VascularguidancecuesaredifferentiallyexpresseduponinvitroinductionofEMT.aPrimaryepicardialcellswerecultured±TGFβ1[10ng/mL]
andPDGF-BB[20ng/mL]toinduceEMT.RelativeexpressionofgenesencodingaxonguidancecueswasevaluatedbyqRT-PCR,alongwithmarkersof
epicardial,mesenchymal,andmuralcells.nrepresentssamplesisolatedfromindependentembryos,whichwereanalyzedover2experiments.Vehiclen=
6forSox9,Sema3c,Tncandn=7forUpk3b,Wt1,Zeb2,Sema3d,Slit2,Pdgfrb,Cspg4;andTGFβ1/PDGF-BBn=7forWt1,Sema3c,Sema3d,Slit2,Pdgfrb,Cspg4
andn=9forUpk3b,Zeb2,Sox9,Tnc.Dataarepresentedasmeanvalues±SEM.Statisticalsignificancewasdeterminedbyatwo-sampleunpaired
Student’st-test.bSeuratwasusedtore-clustercellsundergoingEMT(cluster5)andmesenchymalcells(clusters6/7)definedinFig.1f.cViolinplots
representingselectgenesassociatedwithfibroblastormuralcellidentity.Expressionlevelrepresentslognormalizedexpression.dExperimentalstrategy
forlineagetracingvascularmuralcellsinCspg4CreERT2;R26mTmGembryos.FISHwasperformedonheartswithprobesdirectedagainstGfp(green)and
Slit2(red)asdemonstratedinlow(left)andhigh(right)magnificationimagesandrelativetoPecam1+(plateletendothelialcelladhesionmolecule-1,white)
endothelialcells.Yellowarrowheads,Slit2expressioninCspg4lineage-derivedcells.Scalebar,25μm(leftimage)and10μm(zoomrightimage).DAPI
stainingwasutilizedtovisualizenuclei(blue).Immunostainingwasrepeatedindependently3timeswithsimilarresults.EMTepithelial-to-mesenchymal
transition,TAMtamoxifen,FBfibroblast,SMCsmoothmusclecell,PCpericyte.
8 NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications
c EC - Control EC - MRTFepiDKO
100
90 *
80
70
60 50 40
30
20
10
0
1 2 3 4 5 6 7 8 9
Cluster
f g
Mesothelial Cell Pairings Mesenchymal Cell Pairings
E14.5 Pecam1 Sema3d Nrp1 DAPI E14.5 Slit2 Robo4 DAPI
)%(
sllec
fo noitroporP
61-E02.2=p
NS NS NS
3
0
-3
-6
0 5
UMAP 1
2 PAMU
a 6 3 9
5
Control MRTFepiDKO
6
EPDCs EPDCs
4 EMT EMT 2 8 7
ECs ECs
1
-5
3
0
-3
-6
0 5
UMAP 1
e
Epi Epi
*
*
Sub-Epi Sub-Epi
*
*
2
PAMU
6 9-Sinus Venosus/ 3-Sinus Venosus
Coronary Plexus 2
5-Angiogenic/
Coronary Plexus
6-Endocardial/
Venous 4-Endocardial Nfatc1+/ Arterial
2-Angiogenic
8-Mixed Arterial/ Venous/Endocardial 7-Late Arterial
1-General Endothelial
-5
leveL
noisserpxE
Cdk1 Gja4 Aplnr
4 3
3
2
2
1 1
1
0 0 0
123456789 123456789 123456789
Npr3
3
2
1
0
123456789
Cluster
leveL
noisserpxE
d
Nr2f2 Apln
3 3
2 2
1 1
0 0
123456789 123456789
Cluster Cluster
Nrp1 Nrp2 Robo4
3 3 2.0
1.5
2 2
1.0
1 1 0.5
0 0 0.0
1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
Cluster Cluster Cluster
leveL
noisserpxE
b
60-E24.5=p
40310.0=p
90-E93.6=p
90-E54.1=p
Pecam1
61-E02.2=p
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
Fig.6DisruptionofepicardialEMTaltersintercellularcross-talkbetweentheepicardiumandcoronaryvasculature.aSchematicofvasculature
developmentrepresentingdisruptionofintercellularsignalinghypothesizedinMrtf-a;Mrtf-bdoubleknockout(MRTFepiDKO)hearts.b,cUMAP
representationofsingle-celltranscriptomesofembryonicday(E)14.5endothelialcells(ECs)representedbybcellidentitiesandcgenotypewith
theproportionofeachcellcluster(%)contributingtoeithertheControlorMRTFepiDKOgenotypeisgraphedontheright.Atwo-sampleStudent’st-test
wasperformedtodeterminethesignificanceoftheproportionofcellsinsingle-cellclusters.RefertoSupplementaryFig.11b,cforFACSsequential
gatingandenrichmentofECs.dViolinplotsshowingexpressionofselectgenesassociatedwithECidentity.eViolinplotsshowingexpressionofselect
receptorsforSema3dandSlit2ligandsinthe9ECclusters.Expressionlevelindanderepresentslognormalizedexpression.f,gExpressionofselect
ligand–receptorpairswithinepicardialcellsandPecam1+ECs(plateletendothelialcelladhesionmolecule-1,white)atE14.5visualizedbyFISH.
fMesothelialligandSema3d(red)isobservedontheepicardialsurfaceandNrp1(green)expressionisinECs.gThemesenchymalenrichedligandSlit2
(red)isexpressedininterstitialepicardialcells,oftenassociatedwithRobo4-positive(green)ECs.Yellowasterisks,developingcoronaryvessels.Yellow
arrowheads,Slit2expressingcells.Dashedlinessignifytheepicardialborder.Scalebars,20μm.DAPIstainingwasutilizedtovisualizenuclei(blue).
Immunostainingwasrepeatedindependently3timeswithsimilarresults.NSnot-significant,EMTepithelial-to-mesenchymaltransition,Epiepicardium,
Sub-Episub-epicardium.
NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications 9
1 5 5 7
0
-5
4 -10 3
2 emitoduesp
a
Genotype
G1 S G2/M
5
0
6 -5
-10
-10 0
pseudotime 1
2 emitoduesp
b Cell Cycle Activity
EC - Control EC - MRTFepiDKO
1 > S/G2/M p=2.20E-16 5 (NS) 7 (NS)
6 > G1 2 p= 2 0 > .0 0 G 7 1 05 p=2.20E-16
4 > G1 3 > G1 p=0.00170 p=2.20E-16
10 -10 0 10
pseudotime 1
c
5
0
-5
-10
2 emitoduesp
5
0
-5
-10
Nfatc1 Npr3 Emcn
5 5
0 0
-5 -5
2.0 3 3
1 1 0 0 . . . . 5 0 5 0 -10 2 1 0 -10 2 1 0
-10 0 10 -10 0 10 -10 0 10
2
emitoduesp
Aplnr Apln Sparcl1
5 5
0 0
-5 -5
2 1 -10 2 1 -10 3 2 1 0 0 0
-10 0 10 -10 0 10 -10 0 10
5
0
-5
-10
2
emitoduesp
Nr2f2 Ephb4 Dab2
5 5
0 0
2 3 -5 1 2 . . 5 0 -5 2
1 0 -10 1 0 0 . . . 0 5 0 -10 1 0
-10 0 10 -10 0 10 -10 0 10
5
0
-5
-10
2
emitoduesp
Dll4 Efnb2 Sox17
5 5
0 0
2.0 -5 3 -5 3
1 0 1 . . . 0 5 5 -10 2 1 -10 2 1
0.0 0 0
-10 0 10 -10 0 10 -10 0 10
5
0
-5 -10
2
emitoduesp
100
90
80 70 60
50
40 30
20
10
0
1 2 3 4 5 6 7
Cell State
Fbln5 Gja4 Aqp1
5 5
0 0
3 2 1 4 5 -1 -5 0 1 3 2 0 -1 -5 0 3 2 1 4 0
0
-10 0 10 -10 0 10 -10 0 10
sllec fo
noitroporP
Sinus Venosus/Coronary Plexus
Venous
Early Arterial
Arterial
Endocardium
70-E51.5=p 44000.0=p
NS
d
e
f
g
61-E02.2=p
90-E84.1=p
91000.0=p
pseudotime 1 pseudotime 1 pseudotime 1
61-E02.2=p
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
Fig.7DisruptionofepicardialEMTaltersarteriovenousdifferentiationandmaturation.a,bMonocle-generatedpseudotimetrajectoryofECsfromcontrol
andMrtf-a;Mrtf-bdoubleknockout(MRTFepiDKO)hearts.Developmentaltrajectoriesrepresentedbyagenotypewiththeproportion(%)ofcontrolor
MRTFepiDKOECsrepresentedineachcellstate(right)andbcellcycleactivitywitharepresentationofcellsintheG1,S,orG2/Mphaseofthecellcycle.Atwo-
sampleStudent’st-testwasperformedtodeterminesignificanceoftheproportionofcellsinsingle-cellclusterspresentedinaandb.c–gPseudotimefeature
plotsrepresentingtheexpressionofgenesrelatedtothecsinusvenosus/coronaryplexus,dvenous,eearlyarterial,flatearterial,andgendocardialcell
identity.Thescalerepresentsrelative(Rel.)expression.NSnot-significant,EMTepithelial-to-mesenchymaltransition.
10 NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
intermediate levels of the mature arterial gene marker Gja4 which resided deeper within the myocardium of MRTFepiDKO
(Fig. 7d–f and Supplementary Fig. 22a, b). In contrast, terminal hearts (Fig. 9f, h; Supplementary Fig. 25). Collectively, these
state 7 is represented by cells with more venous-like character- findings reveal a contribution of epicardium-derived pathfinding
istics,expressinghigherlevelsofNr2f2,Ephb4,andDab2(Fig.7d cues to EC localization and AV specification.
and Supplementary Fig. 22a, b). The start of pseudotime is
enriched in ECs obtained from MRTFepiDKO hearts, which
transitionthroughauniquedevelopmentaltrajectory(states2–4), Discussion
characterized by ECs that have exited the cell cycle (Fig. 7a, b). Insummary,ourdataestablishepicardialEMTasadrivingforcein
State2representsatransientECphenotypeleadingtowardsstate thegenerationofdistinctexpressiondomainsofvascularpatterning
4, which is defined by early (Efnb2, Sox17) and mature (Fbln5, cues characterized by: (1) Mesothelial cells on the surface of the
Gja4, and Aqp1) arterial markers (Fig. 7e, f and Supplementary heart expressing angiogenic chemokines such as Sema3d; and (2)
Epicardium-derived mesenchymal cells that express chemokines
Fig.22a,b).Cellstate3iscomposednearlyentirelyofECsfrom
MRTFepiDKO hearts that have exited the cell cycle and express such as Slit2 and Angptl2. Our data also reveal the coordinated
regulation of coronary EC localization and AV specification by
intermediate levels of angiogenic and arterial genes as well and
epicardium-derived vascular patterningcues.
endocardial markers (Fig. 7f, g and Supplementary Fig. 22a, b).
We previously reported that deletion of MRTFs in the epi-
EndocardialgenemarkersNfatc1andNpr3aremostenrichedin
cardiumpreventsEMT,andinhibitscoronaryplexusformation7.
terminal states 3, 6, and 7, whereas Emcn was detected broadly
The current transcriptome analyses further establish the epi-
across cells ordered in pseudotime (Fig. 7g and Supplementary
cardiumasanimportantsourceofvascularguidancecuesinthe
Fig. 22a, b). Collectively, ECs from MRTFepiDKO hearts lack
embryo, which is disrupted in MRTF mutant mice. Here, we
obvious venous identity markers and show a bias towards define the specific role of epicardial EMT in establishing the
immature arterial fate, indicating epicardial EMT-dependent
spatial pattern of vascular cues that control EC patterning. We
EPDC-EC signaling may directly impact EC maturation.
found that EMT induces the expression of secreted ligands that
are found in epicardium-derived mesenchyme, while silencing
Disruption of epicardial EMT alters EC maturation and loca- those ligands that are restricted to the mesothelium. Slit2 is
lization.Coronaryvesselmaturationrequiresthere-specification especiallyinduceduponepicardialEMT,andlocalizestoaminor
ofimmatureECstowardsarterialfateindeepermyocardium,and population of epicardium-derived fibroblasts and pericytes that
venousfateinsub-epicardialmyocardium.Tobegininvestigating wetermvascular“guidepostcells”.Thispopulationisreminiscent
thepotentialimpactofguidepostcell-derivedligandsoncoronary oftheguidepostneuroninaxonpatterning,whichprovidesnon-
EC differentiation, we used an adenoviral-vector to express Slit2 continuous landmarks that act as “stepping stones” for growing
in E13.5 hearts cultured ex vivo (Fig. 8a and Supplementary axons16. While the regulation of vascular guidance molecules
Fig. 23a). This method allowed for specific targeting of Slit2, or seemslargelydependentonEMT,reductionofthemesothelium-
GFP control, to the epicardium (Fig. 8b). Following 24h of restricted Sema3d in MRTF mutant mice suggests general epi-
+
infection, CD31 ECs were isolated from hearts using FACS cardial dysfunction, supported by the suppression of canonical
(Fig. 8a), and EC differentiation and maturation markers were epicardial genes Aldh1a2, Tbx18, Tcf21, and Wt115,46,47.
evaluatedbyqRT-PCR.Slit2overexpressionledtoareductionin Priorstudieshaverevealedtheimportanceofindividualfactors
the expression of arterial markers Gja4, Efnb2, and Apln, and such as Sema3d and Slit2 in patterning of coronary venous cells
increased expression of the venous/angiogenic endothelium and supporting cardiomyocyte cytokinesis48,49. Here, we found
+ +
marker Aplnr, although key venous markers (Nr2f2 and Ephb4) Slit2 guidepost cells in close proximity to Robo4 ECs in the
were unchanged9,38,40,41 (Fig. 8c–f and Supplementary 23b, c). sub-epicardium; thus, Slit2-Robo4 interactions are positioned to
Our data are consistent with reports of Slit2 regulating control angiogenesis and vascular stability, as described in other
angiogenesis42,43, and suggest a common mechanism may guide contexts37,43,50,51.Indeed,ourstudyfoundthatoverexpressionof
vascular pathfinding and arteriovenous fate specification. Slit2 suppressed the arterial EC phenotype in ex vivo heart cul-
EC maturation is also characterized by cell polarization, ture, based on the expression of arterial (Gja4 and Efnb2) and
induced by the connection of the nascent vasculature to arterial angiogenicvenousmarkers(Aplnr).Thisresultisconsistentwith
blood flow, which increases hemodynamic shear stress and the accumulation of ECs that exhibit an immature arterial phe-
supportsECalignmentandmigrationagainstflow44.Inorderto notype upon suppression of Slit2 expression in MRTFepiDKO
+
evaluate EC maturation and polarization, we immuno-stained hearts.However,Cx40 arterialECsbecomemislocalizedandfail
sections from control and MRTFepiDKO hearts obtained atE14.5 to consistently form lumens in MRTFepiDKO embryos at E17.5,
and E17.5 with antibodies directed against EMCN and ERG, a revealing a defect in EC maturation. Evidence for improper
pan-EC ETS-family transcription factor45. The length-to-width arterial cell differentiation upon epicardial disruption is con-
ratio of ERG + nuclei was quantified as an indicator of cell sistentwiththeretentionofasinusvenosusandcoronaryplexus
polarity, revealing considerable elongation between E14.5 and EC phenotype, represented by the expression of Aplnr, Apln,
E17.5 in control hearts, an alteration that was not observed in Vegfa,Vegfc,Cd47.Ofnote,AVspecificationisinpartregulated
ERG + nucleiofMRTFepiDKOhearts(Fig.9a–c).Quantificationof by COUP-TFII (also known as Nr2f2), which inhibits Notch
ERG + nucleus localization also revealed an inappropriate activity in ECs and blocks differentiation into arterial cells52.
accumulation of ECs near the epicardial surface in MRTFepiDKO However, Nr2f2 expression was not altered by Slit2 over-
hearts at E14.5 and E17.5 (Fig. 9a, d, e and Supplementary expression in heart cultures; therefore, it appears the impact of
Fig.24a,b).TofurtherinterrogatethedistributionofmatureECs, Slit2 on EC identity is only partial, suggesting additional factors
immunostaining was performed to visualize venous EC (EMCN, arerequiredfornormalECmaturation.Therefore,futurestudies
green) and arterial EC (Cx40, red), which display sub-epicardial shouldinterrogatethecombinatorialparacrinecodethatgoverns
and mid-myocardial localization in control E17.5 hearts. In normal AV specification.
+
contrast,EMCN venouscellsdisplayedanabnormalaccumula- Importantly, acquired and developmental vascular abnormal-
tionneartheepicardialsurfaceinMRTFepiDKOhearts(Fig.9f,g; ities underlie many human diseases, including stroke and heart
+
Supplementary Fig. 25). We also often found Cx40 arterial EC disease. For example, coronary artery disease (CAD) disrupts
as discontinuous patches of cells without a discernable lumen, the vascular network that supplies the heart with oxygen and
NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications 11
nutrients. Although environmental factors including a sedentary collateralization must complement new muscle formation.
lifestyle and a high-fat diet contribute to CAD progression, Single-cell transcriptomic analysis has identified populations
accumulating evidence suggests a considerable genetic compo- of neovasculogenic ECs that emerge following MI57, and
nenttodiseaserisk53.Oneofthestrongestgeneticriskfactorsfor limited angiogenesis of the injured adult heart is reported to
CAD is the Tcf21 gene, which is highly expressed in the fetal occur through the activation of developmental angiogenic
epicardium and is essential for normal cardiac fibroblast and programs58,59. Indeed, the epicardium induces a fetal gene
coronaryvesselformation46,47.Therefore,abetterunderstanding program after myocardial infarction that includes a paracrine
ofepicardium-directedcoronaryvesselformationindevelopment signature60,61. Unfortunately, the reactivation of endogenous
may provide insight into CAD mechanisms. angiogenicprogramsintheadultheartisinsufficienttosupport
Regenerative therapeutic strategies for cardiac repair meaningful collateralization of ischemic tissue. Therefore, our
include approaches to promote cardiomyocyte proliferation54 study describing the paracrine cues underlying developmental
and sympathetic innervation55,56; however, strategies to stimu- coronaryangiogenesismayprovideaframeworktoestablishre-
late re-vascularization such as through enhancing coronary vascularization strategies for cardiac regenerative medicine.
IPAD
PFG
a
Epi
Epi
ANRm
s81
/ +13DC
ot
ANRm
.ler
ANRm
s81
/ +13DC
ot
ANRm
.ler
250K
200K
150K
100K
50K
0
-103 0 103 104 105
CD31-APC
b
c d ad/βgal
ad/Slit2
CSS
Gja4 Efnb2 Apln Aplnr
2.0 1.5 2.0 6
5
1.5 1.5
1.0 4
1.0 1.0 3
0.5 2
0.5 0.5
1
0.0 0.0 0.0 0
ANRm
s81
/ +13DC
ot
ANRm
.ler
ANRm
s81
/ +13DC
ot
ANRm
.ler
E13.5
CD31+
EC
4.03%
Vascular
FACS
Plexus
24hrs
Epicardium
+ad/GFP+ad/βgal
+ad/GFP+ad/Slit2
p=0.0521
p=0.0303
AH-2TILS
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
+ad/GFP+ad/βgal +ad/GFP+ad/Slit2
e f
p=0.0190 p=0.0325
Fig.8SLIT2expressionintheepicardiuminhibitsarteryspecification.aSchematicofexperimentaldesigntoisolateECsfollowingadenovirusinfection
oftheepicardium.Heartswereextractedatembryonicday(E)13.5andinfectedwithadenovirus(ad)toexpressβ-galactosidase(ad/β-gal)orSLIT2-HA
(ad/Slit2,red).AdexpressingGFPwasaddedtoheartstoconfirmthespecificityofinfectiontocellsoftheepicardium(green).Following24-h,hearts
weredigestedandsubjectedtoFACStoacquireCD31expressingECs.RefertoSupplementaryFig.23d,eforFACSsequentialgatingandenrichmentof
ECs.bRepresentativeimagesofembryonicheartsfollowinginfectionwithadenoviruses.SLIT2proteinexpressionwasdetectedintheepicardiumusingan
anti-HAantibody.Scalebar,20μm.DAPIstainingwasutilizedtovisualizenuclei(blue).Immunostainingwasrepeatedindependently3timeswithsimilar
results.c–fGeneexpressionrepresentedasfoldchangerelativetoCD31+cellsacquiredfromad/βgal-treatedhearts.nrepresentssamplesacquiredfrom
independentembryos.ad/β-galn=6forEfnb2,Apln,Aplnrandn=7forGja4;andad/Slit2n=5forAplnandAplnrandn=6forGja4andEfnb2.Dataare
presentedasmeanvalues±SEM.Statisticalsignificancewasdeterminedbyatwo-sampleunpairedstudent’st-test.
12 NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications
ERG+ Nuclei
Length to Width Ratio
p=0.0043
Control
MRTFepiDKO
Total Nuclei
Length to Width Ratio
NS
d e
E14.5: ERG+ Nuclei
10 10
MRTFepiDKO =34.7μm (N=3) WT = 37.6μm (N=4) MRTFepiDKO = 29.9μm (N=3) WT = 33.9 μm (N=5)
4 p=0.0187 4 p=2.5E-05
3 3
2 2
1 1
0 0
0 14 28 42 0 14 28 42
μm to surface
Methods (stocknumber007576).Rosa26tdTomatomicewerepurchasedfromTheJackson
Animalmodels.Allanimalexperimentswereconductedinaccordancewiththe Laboratory(stocknumber007909).TheWt1CreERT2mousestrainexpressesthe
ethicalregulationsfortestingandresearchandapprovedbytheUniversity CreERT2fusionproteininthepresenceoftamoxifenandunderthecontrolofWt1
CommitteeonAnimalResourcesattheUniversityofRochester(UCAR-2011- promoter.Wt1CreERT2micewereusedtoefficientlylabeltheepicardiumandits
026E).C67BL/6JmicewerepurchasedfromTheJacksonLaboratory(stock derivativesandaspreviouslydescribed6andwerepurchasedfromTheJackson
number000664)andallmouselinesweremaintainedontheC57BL/6Jback- Laboratory(stocknumber010912).Cspg4CreERT2miceexpressthetamoxifen-
ground.Rosa26mTmG/mTmGmicewerepurchasedfromTheJacksonLaboratory inducibleCre-recombinaseunderthecontrolofCspg4promoter.Cspg4CreERT2
langiS
+GRE
fo
%
Control MRTFepiDKO
ERG ERG
EMCN EMCN
DAPI DAPI
ERG ERG
EMCN EMCN
DAPI DAPI
KO Enriched KO Enriched
Control Enriched
Control Enriched
5.41E
5.71E
a b
1.75
1.70
1.65
1.60
1.55
1.50
1.45
E14.5 E17.5
c
1.75
1.70 p=5.5E-05 Control
MRTFepiDKO
1.65
1.60
1.55
1.50
1.45
E14.5 E17.5
E17.5: ERG+ Nuclei
μm to surface
Epicardium Interstitium Epicardium Interstitium
g
MRTFepiDKO = 19.41μm (N=4) WT = 20.49μm (N=5)
f Control - E17.5
p=0.00016
h MRTFepiDKO = 26.43μm (N=4) WT = 23.05μm (N=5)
p=2.2E-16
langiS
+NCME
fo
%
langiS
+04XC
fo
%
Cx40 2.0 KO Enriched
1.5
Control Enriched
EMCN 1.0
0.5
DAPI
0.0
0 12.4 24.8 37.2 49.6
Cx40
1.0
EMCN
0.5
DAPI
0.0
0 12.4 24.8 37.2 49.6
langiS
+GRE
fo
%
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
p=0.0027
μm to surface
Epicardium Interstitium
MRTFepiDKO - E17.5
Control Enriched KO Enriched
μm to surface
Epicardium Interstitium
NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications 13
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
Fig.9Epicardialdysfunctionaltersendothelialcelllocalizationandmaturation.aImmunofluorescencestainingofsectionsfromheartsisolatedat
embryonicstage(E)14.5andE17.5.AntibodiesaredirectedagainstERG(red,pan-EC)andEMCN(green,venous,andendocardialEC).Scalebar,20μm.
bQuantitationofthelength-to-widthratioofERG+nuclei(top)orctotalnuclei(bottom).nrepresentsamplesacquiredfromindependentembryos.At
E14.5,n=5Controlheartsandn=4Mrtf-a;Mrtf-bdoubleknockout(MRTFepiDKO)hearts.AtE17.5,n=6Controlheartsandn=3MRTFepiDKOhearts.For
eachheart,atleastthreefieldsofviewwereassessed.Dataarepresentedasmeanvalues±SEM.Statisticalsignificancewasdeterminedbyatwo-sample
unpairedStudent’st-test.d,eQuantitationofERG+nucleilocalization,reportedasapercentageofcellswithinaparticularbinrepresentingthedistance
fromtheepicardialsurfaceoftheheartatdE14.5andeE17.5.fImmunofluorescencestainingofsectionsfromheartsisolatedatE17.5withantibodies
directedagainstEMCN(green)andCx40(red,arterial).Scalebar,25μm.g,hQuantitationofgEMCN+celllocalizationandhCx40+celllocalization,
reportedasapercentageofcellswithinaparticularbinrepresentingthedistancefromtheepicardialsurfaceoftheheart.Forlocalizationexperiments,
nrepresentsdataacquiredfromindependentembryos,whichwasanalyzedin1experiment.ForERG+nucleuslocalizationn=4Controlheartsandn=3
MRTFepiDKOheartsatE14.5;andn=5Controlheartsandn=4MRTFepiDKOheartsatE17.5.ForCx40andEmcnlocalization,n=5Controlheartsandn=
4MRTFepiDKOheartsatE17.5.SignificantaccumulationofECsinparticularregionsoftheheartaremarkedbybracketsthatindicatetheover-represented
genotype.Foreachheart,atleastthreefieldsofviewwereassessed.DAPIstainingwasutilizedtovisualizenuclei(blue).Fordataind,e,g,hstatistical
significancewasdeterminedbyatwo-tailedMann–Whitneytest.NSnot-significant,WTwild-type,KOknockout.
micewereusedtolabelcardiacpericytesduringembryonicdevelopmentandisa HBSSfromwellsandreplacingmediawithadigestionsolutioncontaining0.08%
validatedmodeltolabelCspg4expressingcells35andwerepurchasedfromThe CollagenaseIV(MilliporeSigma,C5138),0.05%TrypsinProtease(ThermoFisher
JacksonLaboratory(stocknumber008538).Mrtfa−/−andMrtfbflox/floxmicewere Scientific,SH30042.01),1%chickenserum(VectorLaboratories,S-3000)dilutedin
previouslydescribed7andweregiftsfromDr.EricOlson(UTSouthwestern, pre-warmedHBSSbeforeplacingheartsina37°Chybridizationovenwithgentle
Dallas,TX,USA).TheSrfflox/floxmicewerepreviouslydescribed62andwereagift shakingfor5minintervals.Followingincubation,heartsweredissociatedbygentle
fromDr.JosephMiano(AugustaUniversity,Augusta,GA,USA). pipetting(3timeswithaP1000pipette)andundigestedtissuewasallowedtosettle
Timedpregnanciesweredeterminedafterplacingonemalewithuptotwo for30s.Aftersettlementoftissue,mediawascollectedandaddedtoaseparatetube
femalesinasinglecageinthelateafternoon.Thenextmorning,aconfirmedplug containinghorseserum(VectorLaboratories,S-2000)toneutralizedigestion,and
wastermedasembryonicday(E)0.5.InordertoinduceCre-basedrecombination, digestedcellswerethensavedonice.Digestion,pipetting,andcollectionofmedia
4-Hydroxytamoxifen(4-OHT,MilliporeSigmaH6278)wasdissolvedinsunflower wererepeated3-5moretimes,andcellswerethenfilteredthrougha70μmfilterand
seedoilfromhelianthusannus(MilliporeSigmaS5007)atafinalconcentrationof centrifugedat200×gfor5minat4°C.Theresultingpelletwasplacedin10%FBSin
10mg/mLwith10%ethanol.4-OHTwasadministeredbyoralgavageat75mg/kg DMEM(withoutphenolred,ThermoFisherScientific,SH30284.01)andsavedonice
topregnantdams. beforeperformingfluorescence-activatedcellsortingFACSusingaBDFACSAriaII
4-OHTadministrationanddissectionschedulesforindividualexperimentswere: usinga100μmnozzle(BDBiosciences).DAPI(4′,6-Diamidino-2-Phenylindole,
(1)Thebreedingstrategytogeneratedevelopmentallystagedembryosforsingle-cell Dihydrochloride)wasaddedtocellsimmediatelybeforesorting(0.5μg/mL;
RNA-sequencingofepicardialcellsandisolationofheartsforimmunostainingand ThermoFisherScientific,D1306)toexcludedeadcells.Cellsweresorteddirectlyinto
insituhybridizationassays:Wt1CreERT2/+maleswerecrossedtoRosamTmG/mTmG 1.5mLEppendorftubescontaining0.5%bovineserumalbumin(BSA,Millipore
females.4-OHTwasadministeredatE9.5andE10.5andembryoswereisolatedat Sigma,A9647)inDPBSat4°Candimmediatelyprocessed.
E12.5andE16.5.(2)Thebreedingstrategytogeneratedevelopmentallystaged
embryosforgeneexpressionanalysisinepicardialcells:Wt1CreERT2/+malesto
RosamTmG/mTmGfemalesorRosatdTomato/tdTomatofemales.4-OHTwasadministered C co e l l l l ec is te o d la f t r i o o m no W fe t1 p C ic re a E r R d T ia 2/ l + c ; e R ll 2 s 6 a m t T E m 1 G 2 / . + 5 e a m nd br E y 1 o 6 s .5 th f a o t r w s e c r R e N a A dm -s i e n q is . t E er P e D d C 4 s -O w H er T e
atE9.5andE10.5andembryoswereisolatedatE12.5,E14.5,andE16.5.(3)The
atE9.5andE10.5viapregnantdams.Atotalof7E12.5stagedheartswerepooled
breedingstrategytogeneratedevelopmentallystagedembryosfortheanalysisof
c to ar R d o ia s c am p T er m ic G y / t m e T s m b G y f i e n m s a it l u es h .4 yb -O rid H i T zat w io a n sa a d ss m ay in s: is C te s r p e g d 4 a C t re E E 9 R . T 5 2 /E /+ 10 m .5 a a le n s d w E e 1 r 5 e .5 c / r E o 1 ss 6 e . d 5 f o r n om vis 2 ua d l am co s n , fi a r n m d a a ti t o o n ta o l f of gr 1 e 7 en E1 fl 6 u .5 or s e t s a c g e e n d t h p e r a o r t t e s in we (G re F p P o ) o e le x d pr f e r s o s m ion 4 i d n am th s e b e a p s i e - d
cardiumusingaZOEFluorescentCellImager(Bio-Rad).Heartsnegativeforthe
andembryoswereisolatedatE17.5.(4)Thebreedingstrategytogenerate expressionoftheWt1CreERT2allele,exhibitedtdTomatofluorescencealone,and
developmentallystagedembryosforsingle-cellRNA-sequencingofendothelialcells wereeitherdiscardedorusedastdTomatopositivefluorescencecontrolsforflow
andisolationofheartsforimmunostainingandinsituhybridizationassays:
W W Mr t t t 1 1 f C C -b r r e e fl E E o R R x T T /fl 2 2 o / / + + x ; fe m M m a r a l t e l f e s - s a w − to e /− r g e ; e c n M r e o r r s t a f s t - e e b d fl M o t x o R /fl T C o F x 5 e 7 m p B iD a L K l / e O 6 s J e w m m e i r b c e r e y c t o r o o s. s g s 4 e e - n d O e H r to a T te M w C r a t o f s - n a a t − d ro m /− l i ; e n m is b te r r y e o d s. at b f c fl r y y u o t o m o P r m C e a s e R c l t l e r g n e y e m . c n e D b o c r e t o y y v o n p el s t i o n r , o p g a l m n s u d e f s o n i W n r t g a fl t l 1 l o t y r C w a r s n e t c E a s y R g g t T e e o n d 2 m ; e C - R e s t 5 2 p r 7 6 y e B m . ci L A T fi / m d c 6 d G J p i / t e r + i i m o m p n b e o a r r s l y s l i y o . ti , s F v g o e w e l n l e e o m r o w e m b i c n r i o c y g l o l D e t s h c N w t e e A e d d r i e w a g s e a c s s o n t n i i o o s fi n o n r - l m at e e d d
E9.5andE10.5andembryoswereisolatedatE14.5andE17.5.(5)Thebreeding
protocoldescribed,EPDCsweregatedassinglecells(basedonFSC×SSC
strategytogeneratedevelopmentallystagedembryosforisolationofControland
dimensions),DAPInegative,tdTomatonegative,andGFP-positive.TdTomato
MRTFmutantepicardialcellsforbulkRNA-sequencingandgeneexpressionstudies:
Mrtf-a−/−;Mrtf-bflox/floxmaleswerecrossedtoMrtf-a−/−;Mrtf-bflox/floxtogenerate positivecellsweresortedfordownstreamgeneexpressionanalysis.EPDCscol-
Mrtf-a−/−;Mrtf-bflox/floxembryos.SRFflox/floxmaleswerecrossedtoSRFflox/flox lectedbyFACSwereimmediatelyprocessedforsingle-cellcapture,librarypre-
femalestogenerateSRFflox/floxembryos.EmbryosweredissectedatE12.5forheart paration,andsequencing,asdescribedbelow.
cultureandepicardium-derivedcelllabelingandgenedeletionwasconductedvia
adenoviral-vectormediateddeliveryofGFPandCre-recombinase,asdescribedbelow. CellisolationofepicardialcellsatE12.5,E14.5,andE16.5forgeneexpression
(6)Thebreedingstrategytogeneratedevelopmentallystagedembryosforexvivo analysis.EPDCswerecollectedfrombothWt1CreERT2/+;R26mTmG/+and
expansionofprimaryepicardialcellsandgeneexpressionstudies:C57BL/6Jmales Wt1CreERT2/+;R26tdTomato/+embryosthatwereadministered4-OHTatE9.5and
werecrossedtoC57BL/6JfemalesandembryoswereisolatedatE11.5.(7)The E10.5viapregnantdams.FluorescencewasconfirmedusingtheZOEFluorescent
breedingstrategytogeneratedevelopmentallystagedembryosforisolationof CellImager(Bio-Rad).HeartsnegativefortheexpressionoftheWt1CreERT2allele,
endothelialcellsfollowingexvivoheartcultureandinfectionwithadenoviruses: exhibitedtdTomatofluorescence(R26mTmG/+)orwerenon-fluorescent
C57BL/6JmaleswerecrossedtoC57BL/6Jfemalesandembryoswereisolated (R26tdTomato/+)andwereeitherdiscardedorusedasfluorescencecontrolsforflow
atE13.5. cytometry.Followingthedigestionprotocoldescribed,EPDCsweregatedassingle
cells(basedonFSC×SSCdimensions),DAPInegative,tdTomatonegative,and
GFP-positiveifthecrosswastotheR26mTmGfluorescentreporter.Ifthe
E
en
m
d
b
o
r
t
y
h
o
el
n
ia
ic
lc
h
e
e
ll
a
s
r
(
t
E
d
C
i
s
g
)
e
w
st
e
i
r
o
e
n
is
p
o
r
l
o
at
t
e
o
d
co
fr
l.
om
Ep
d
ic
e
a
v
r
e
d
l
i
o
u
p
m
m
-
e
d
n
e
t
r
a
iv
ll
e
y
d
st
c
a
e
g
ll
e
s
d
(
h
E
e
P
a
D
rt
C
s
s
a
)
s
a
d
n
e
d
fined
R26tdTomatofluorescentreporterwasused,DAPInegativeandtdTomatopositive
EPDCswerecollected.EPDCscollectedbyFACSwerethenprocessedforRNA
above.Onthedayofisolation,pregnantdamswereanesthetizedwithanintra-
isolationpriortoconductingquantitativeRT-PCR.
peritonealinjectionof0.5mLofketamine-xylazinecocktail(13mg/mLketamine
in0.88mg/mLxylazineinDPBS)followedbycervicaldislocation.Aftertheuseof
70%ethanoltosterilizetheabdominalarea,anincisiontoenterandremove CellisolationofendothelialcellsatE14.5forscRNA-seq.ECswerecollected
deciduaawayfromthemesometriumwasperformed,andembryoswereplacedin fromWt1CreERT2/+(Control)andWt1CreERT2/+;Mrtf-a−/−;Mrtf-bflox/flox
pre-warmedHBSS(ThermoFisherScientific,SH30031.02).Aftertheremovalof (MRTFepiDKO)miceafteradministrationof4-OHTatE9.5andE10.5viaoral
extraembryonictissueandtheyolksac,theheartwasremovedfromtheembryo gavageofpregnantdams.Atotalof10Controlheartswerepooledfrom2dams.A
andplacedinacellculturewell-containingculturemediamadeupofM199 totalof7MRTFepiDKOheartswerepooledfrom2dams.Priortodigestion,hearts
(ThermoFisherScientific,SH3025301)supplementedwith10%FBS(GeminiBio- wereplacedinHBSSat37°Cand5%CO andgenomicDNAfromallembryos
Products,100106)and1%Penicillin/Streptomycin(Pen-Strep;ThermoFisher weresubjectedtogenotypingtodetectthe 2 Wt1CreERT2/+allelewithin2h.
Scientific,SV30010).Digestionofembryonicheartsbeganbyremovingresidual Followingconfirmationofpositiveembryos,heartsweresubjectedtothedigestion
14 NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-021-24414-z
protocoldescribed.Afterfilteringandcentrifugingcells,ECswereincubatedwith ()functionwereusedastheorderinggenesinMonocle,8principlecomponents
fluorescentlyconjugatedantibodiesdirectedagainstCD31-APC(dilutionat1:100; wereusedforfurthernon-linearreductionusingtSNE,andnum_clusterswasset
BDBiosciences551262)andCD45-FITC(dilutionat1:50;BDBiosciences553079) to5intheclusterCells()Monoclefunction.TheresultingMonocletrajectorywas
for30minin0.5%BSAinDPBSonice.Afterantibodylabeling,cellswerewashed coloredbasedonMonocleState,Pseudotime,developmentalorigin(E12.5or
andcentrifugedat200gfor5minandplacedin10%FBS/DMEMbuffer.ECswere E16.5),andSeuratclusterspreviouslyidentified.Genesthataredynamically
gatedassinglecellsthatareDAPInegative,CD45-FITCnegative,andCD31-APC expressedattheoneidentifiedbranchpointwereanalyzedusingtheBEAM()
positive.ECscollectedbyFACSwereimmediatelyprocessedforsingle-cellcapture, function.Thetop50genesthataredifferentiallyexpressedatthebranchpointwere
librarypreparation,andsequencing. visualizedusingtheplot_genes_branched_heatmap()functioninMonocle.
IntegrationwithMouseCellAtlas.Neonatalheartsfromone-day-oldpupswere
downloadedfromtheMouseCellAtlas(https://figshare.com/articles/
Exvivoembryonicheartcultureforisolationofendothelialcellsfollowing
MCA_DGE_Data/5435866)andre-analyzedusingSeuratv3followingstandard
adenovirusinfection.ECswerecollectedfromC57BL/6heartsthatwereextracted
procedurespreviouslyoutlined.Epicardial(E12.5andE16.5)andneonatal-heart
atE13.5andplacedinculturemedia(DMEM:M199with10%FBSand1%Pen-
(1dayold)wereintegratedusingtheFindIntegegrationAnchors()and
Strep)containingadenovirustoexpressβ-galactosidase(VectorBiolabs,1080)or
IntegrateData()functionsusingSeuratv3.Datawerevisualizedinthe2-
SLIT2-HA(AppliedBiologicalMaterials,132844A)for24hat37°Cand5%CO 2 dimensionalUMAPspace.Markergeneswereidentifiedfortheintegratedclusters
andsubjectedtothedigestionprotocoldescribed.Thismethodprimarilytrans- andEnrichr(enrichR_2.1)wasusedtoidentifiedsignificantlyenrichedBiological
ducessurfaceepicardialcellswithadenovirus.Afterfilteringandcentrifugingcells,
Processes(GeneOntology2018).
ECswereincubatedwithfluorescentlyconjugatedantibodiestoselectforvascular
EC(CD31-APC;BDBiosciences551262)for30minin0.5%BSAinDPBSonice.
Afterantibodylabeling,cellswerewashedandcentrifugedat200×gfor5minand Single-celltranscriptomesequencingofendothelialcells.Cellfiltering,cell-
placedin10%FBS/DMEMbuffer.ECsweregatedassinglecellsthatareDAPI typeclusteringanalysis,andcreationofcellulartrajectories:Seurat(3.0.2)wasused
negativeandCD31-APCpositive.ECscollectedbyFACSwereimmediatelypro- tofilterlow-qualitycells,scorethecellsbythecellcycle,andintegratetheE14.5
cessedforRNAisolationpriortoconductingquantitativeRT-PCR. MRTFepiDKOandControldatasetsusingthemergefunction.Cellswereclustered
usingthefirst36dimensionsofPCAtotheresolutionof0.7andvisualizedusing
UMAP.Monocle(2.10.1)wasusedtoinfercellulartrajectoryaftertheremovalof
ExvivoembryonicheartcultureforisolationofepicardialcellsforbulkRNA-
s E e P q D u C e s n , c a in n g d . n H o e n a - r E ts PD we C r ) e a c n o d lle M ct r e t d f- f a r − o / m −; S M rf rt fl f o - x b / fl fl o o x x /fl ( o fo x r (f c o o r n M tro r l tf E -d P K D O C ) , e S m rf- b K ry O os c p e r l o l p c o y r c t l i e o - n re s la o t f ed M g R e T ne F s e . p T iD h K e O d a e n te d rm C i o n n e t d ro c l el a l n s d tat id es en w t e if r y e p u o se te d n t t o ia d l e m te a r r m ke in rs e f c o e r ll t s h t e a s t e e
cellstates.Originatingdatasets,pseudotimestates,andcellcyclestatecolorings
thatwereextractedatE12.5andplacedinculturemedia(M199with10%FBS
and1%Pen-Strep)containingTGF-β2(2ng/mL;R&DSystems)andPDGF-BB wer
R
e
e
u
c
s
e
e
p
d
to
w
r–
it
l
h
ig
i
a
n
n
g
d
en
ex
e
p
ra
r
t
e
e
s
d
sio
g
n
rap
an
h
a
ic
ly
s.
sis:Usingpublishedlistsofpairingsfrom
( e 2 x 0 pl n a g n / t m sw L; e R re & t D ran S s y d s u te c m ed s) w t i o th in a d d u e c n e ov ep ir i u th s e t l o ial e - x m p e re se ss nc a h g y r m ee a n lt fl ra u n o s r i e t s io ce n n . t A p ll rotein s R y a m m b il o o l w fr s o k m iet H a G l.6 N 3, C th g e en r e ec s e y p m to b r o – l li u g s a i n n d g p b a io ir m in a g R s t w (2 er .4 e 2 c .0 o ) n 6 v 4 e ,6 r 5 t . ed Lig to an M ds G t I h g a e t n w e ere
(GFP,VectorBiolabs,1060)ontheepicardialsurface.Controlheartswereco-
transducedwithadenovirusexpressingβ-galactosidase(VectorBiolabs,1080) s
th
h
e
ow
M
n
R
t
T
o
F
b
e
e
pi
d
D
i
K
ff
O
er
e
e
p
n
i
t
c
i
a
a
r
ll
d
y
ia
e
l
xp
ce
r
l
e
l
s
s
se
in
d
c
w
o
i
m
th
p
in
ar
t
i
h
so
e
n
w
t
h
o
ol
t
e
h
-
e
tr
C
an
o
s
n
c
t
r
r
i
o
p
l
to
w
m
er
e
e
se
fl
q
a
u
gg
en
ed
cin
fo
g
r
of
whilegenedeletionwasaccomplishedbyco-transductionwithadenovirus
expressingCre-recombinase(VectorBiolabs,1045)toexcisefloxedalleles(all late
B
r
o
c
t
o
h
n
t
s
h
id
e
e
e
r
n
at
d
i
o
o
t
n
h
.
elialandepicardialdatasetswerefilteredforexpressedreceptors
adenovirustreatmentswereat1×106pfu/mL).Following48hofcultureat37°C
andligands,respectively.Ligandsexpressedwithintheepicardialdatasetwere
and5%CO,heartsweredissociatedandEPDCswereisolatedviaFACSbygating
2 categorizedasbeingdifferentiallyexpressedbetweenmesothelialandmesenchymal
forsinglecells,andseparatedasGFPnegative(non-EPDCs)orGFP-positive cellpopulations.ReceptorsexpressedwithintheE14.5MRTFepiDKOandControl
(EPDCs)fromeachgroupandcollectedin5mLFACStubescontaining0.5mL
combineddatasetwerecharacterizedasdifferentiallyexpressedbetweenthetwo
H
no
B
n
S
-
S
flu
su
o
p
re
p
s
l
c
e
e
m
nc
e
e
nt
g
e
a
d
ti
w
ng
ith
co
1
n
0
t
%
rol
F
s
B
d
S
u
.
r
H
in
e
g
ar
fl
t
o
s
w
no
c
t
yt
t
o
re
m
a
e
te
t
d
ry
w
a
i
n
th
aly
a
s
d
is
-
.
G
S
F
o
P
rt
w
ed
er
c
e
el
u
ls
se
w
d
e
a
re
s conditions.Seurat’sDotPlotanddoHeatMapfunctionswereusedtovisualize
differentialexpressionacrossbothdatasets.
t
R
h
e
e
a
n
ge
p
n
e
t
ll
(
e
T
te
h
d
er
a
m
t
o
2
F
00
ish
×
er
g
S
fo
ci
r
en
5
t
m
ifi
i
c
n
,1
a
5
t
5
4
9
°
6
C
0
.
18
T
)
ot
p
a
e
l
r
R
m
N
a
A
nu
w
fa
a
c
s
tu
is
r
o
e
l
r
a
’s
te
i
d
ns
u
t
s
r
i
u
n
c
g
tio
T
n
R
s
Iz
a
o
n
l
d
Fornetworkvisualization,tidyverse(1.3)66wasusedfordataanalysis,viridis
cleanedupwithcolumnpurification.RNAqualitywasevaluatedusingabioana- (0.5.1)(https://cran.r-project.org/web/packages/viridis/index.html)wasusedfor
colormapping,andbothigraph(1.2.4.2)(https://igraph.org/)andggraph(2.0.1)
lyzerandpreparedintoNGSlibrariesforbulkRNA-sequencingorwasusedfor
(https://cran.r-project.org/web/packages/ggraph/index.html)wereusedtogenerate
conductingquantitativeRT-PCR.
andplotthenetworkmap.Epicardialligandsandendothelialreceptorswere
groupedtogetherandcoloredbasedondifferentialregulation;greeniftheywere
Singlelibrarypreparationandprocessingofsingleepicardialcellsand solelydifferentiallyregulatedwithinthatdatasetorrediftheyhadacorresponding
endothelialcells.Single-celllibrariesweregeneratedfromepicardialcellsand differentiallyregulatedligandorreceptor.Red-linesconnectreceptorsandligand
endothelialcellsacquiredbyFACS.Priortocaptureusingthe10×Genomics pairs,whichwerebothconfirmedtobedifferentiallyexpressed.Theepicardial
Chromiumcontroller(10×Genomics),thenumberofcellswasquantitated ligandswerefurthercoloredbyexpressioninspecificcellpopulationsidentifiedas
(TC20AutomatedCellCounter,Bio-Rad)andcellviabilitywasassessedviathe mesothelial,mesenchymal,orgeneralepicardial.
trypanblueexclusiontestofcellviability.Onlycellpopulationsexhibitinggreater
than80%viabilitywereused.Allcellswereloadedinordertomaximizethe
numberofsinglecellsacquiredusingtheChromiumsingleCell3′ReagentKit. Whole-transcriptomesequencingofepicardialcells.TheClontechUltralow
Librarieswerepreparedaccordingtothemanufacturer’sinstructionsusingthe RNAKitinconjunctionwithNexteraXTDNALibraryPrepKit(Illumina)was
v C 2 h .2 ro .0 m w iu a m su S s i e n d gl t e o C d e e l m l3 u ′ lt L ip ib le ra x r e y a a c n h d c G ap e t l u B re e , ad pr K oc it es v s .2 b ( a 1 s 0 e × -ca G ll en fi o le m s i t c o s) f . a C st e q ll f R o a r n m g a e t r , u fa s c e t d ur f e o r r ’s n p e r x o t- to ge c n ol e s r . a B ti r o i n efl s y e , q m ue R n N ci A ng w l a ib s ra p r u y ri c fi o e n d st f r r u o c m tio 1 n n a g c t c o o t r a d l in R g N t A o w th i e th m o a li n g u o - -
andperform3′genecountingforeachindividualcellbarcodewithmouserefer- dTmagneticbeadsandfragmented.First-strandcDNAsynthesiswasperformed
withrandomhexamerprimingfollowedbysecond-strandcDNAsynthesisusing
encedataset(mm10,v2.1.0). dUTPincorporationforstrandmarking.Endrepairand3′adenylationwasthen
performedonthedoublestrandedcDNA.Illuminaadaptorswereligatedtoboth
Single-celltranscriptomesequencingofepicardialcells.Cellfilteringandcell- endsofthecDNA,purifiedusingAmpurebeads,andamplifiedwithPCRprimers
typeannotationandclusteringanalysis:Qualitycontrol,identificationofvariable specifictotheadaptorsequencestogeneratecDNAampliconsof~200–500bpin
genes,principlecomponentanalysis,andnon-linearreductionusingUMAPwere size.TheamplifiedlibrarieswerehybridizedtotheIlluminasingle-endflowcell
performedusingSeurat(v3.0.0.9000andRv3.5.1)foreachindividualtimepoint andamplifiedusingthecBot(Illumina).Single-endreadsof100ntweregenerated
separately.TheintegrationfunctionRunCCAwasutilizedtoidentifycelltype- foreachsampleusingIllumina’sHiSeq2500v4.Rawreadsweregeneratedfrom
specificclusterswithoutrespecttodevelopmentaltime.Cell-typeannotationswere IlluminaHiSeq2500sequencinganddemultiplexedusingbcl2fastqversion1.8.4.
identifiedbasedonsignificantcluster-specificmarkergenesandtheMouseGene QualityfilteringandadapterremovalwereperformedusingTrimmomaticversion
AtlasusingEnrichr(enrichR_2.1).Inordertounderstandtheeffectofdevelop- 0.32withthefollowingparameters:“TRAILING:13LEADING:13ILLUMINA-
mentaltime,theSeurat(v3.0.0.9150)functionmerge()wasusedtocombinethe CLIP:adapters.fasta:2:30:10SLIDINGWINDOW:4:20MINLEN:15”.Processed/
E12.5andE16.5capturestomaintainthevariationintroducedbydevelopmental cleanedreadswerethenmappedtotheGRCm38referencegenomeusingthe
time.Cellcyclescoringwasperformedandthevariationintroducedasanumberof SHRiMPversion2.2.3andthefollowingparameters:“–qv-offset33–all-contigs”.
genesinvolvedinmitochondrialtranscription,andcellcyclephasesSandG2/M Uniquelyalignedandmulti-mappedreadswerecountedwithinthegencode
wereregressedoutduringdatascaling.DatawasvisualizedinUMAPspaceand GRCm38geneannotations,inastrand-specificmanner,usingthecuffdifftool
clusteredweredefinedusingaresolutionof0.5. fromthecufflinks-2.0.2packageandthefollowingparameters:“–FDR0.05-u-b
Developmentaltrajectoryandpredictionofcell-fatedeterminants:The GENOME”.Differentialexpressionanalysesanddatanormalizationwereper-
GetAssayData()functioninSeurat(v3.0.0.9150)wasusedtoextracttherawcounts formedusingDESeq2-1.14.1R/Bioconductorpackagewithanadjustedp-value
toconstructtheMonocleobject.Toconstructthetrajectorythedefaultfunctions (Benjamini–Hochberg)thresholdof0.05withintheRversion3.3.1environment
andparametersassuggestedbyMonocle(v2.10.1)wereusedalongwiththe (https://www.R-project.org).ThePCAplotwascreatedgiventhetop500genes
followingdeviations:thehypervariablegenesdefinedusingSeuratVariableFeatures withthemostvariationusingthestats-3.4.0(prcomp)andrgl-0.98.1Rpackages.
NATURECOMMUNICATIONS| (2021) 12:4155 |https://doi.org/10.1038/s41467-021-24414-z|www.nature.com/naturecommunications 15
