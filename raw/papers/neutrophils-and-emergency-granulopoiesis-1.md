---
source_path: /mnt/c/Users/Administrator/Zotero/storage/G3QVWQGS/s41590-023-01490-5 (1).pdf
ingested: 2026-04-23
sha256: 921b44b319745393
---

nature immunology
Article https://doi.org/10.1038/s41590-023-01490-5
Neutrophils and emergency granulopoiesis
drive immune suppression and an extreme
response endotype during sepsis
Received: 2 October 2022 Andrew J. Kwok1, Alice Allcock1, Ricardo C. Ferreira 1, Eddie Cano-Gamez1,2,
Madeleine Smee1, Katie L. Burnham2, Yasemin-Xiomara Zurke 3,
Accepted: 13 March 2023
Emergency Medicine Research Oxford (EMROx)*, Stuart McKechnie4,
Published online: 24 April 2023 Alexander J. Mentzer 1,4,5, Claudia Monaco 3, Irina A. Udalova 3,
Charles J. Hinds6, John A. Todd 1,5, Emma E. Davenport2 &
Check for updates Julian C. Knight 1,4,5,7
Sepsis arises from diverse and incompletely understood dysregulated
host response processes following infection that leads to life-threatening
organ dysfunction. Here we showed that neutrophils and emergency
granulopoiesis drove a maladaptive response during sepsis. We
generated a whole-blood single-cell multiomic atlas (272,993 cells, n = 39
individuals) of the sepsis immune response that identified populations
of immunosuppressive mature and immature neutrophils. In co-culture,
CD66b+ sepsis neutrophils inhibited proliferation and activation of CD4+
T cells. Single-cell multiomic mapping of circulating hematopoietic
stem and progenitor cells (HSPCs) (29,366 cells, n = 27) indicated altered
granulopoiesis in patients with sepsis. These features were enriched in a
patient subset with poor outcome and a specific sepsis response signature
that displayed higher frequencies of IL1R2+ immature neutrophils,
epigenetic and transcriptomic signatures of emergency granulopoiesis
in HSPCs and STAT3-mediated gene regulation across different infectious
etiologies and syndromes. Our findings offer potential therapeutic targets
and opportunities for stratified medicine in severe infection.
The multiple dynamic host pathophysiological mechanisms that result 20–30%4. Axes of immune dysregulation in sepsis have typically been
in organ dysfunction following infection are incompletely understood examined by peripheral blood bulk transcriptomic studies, which lack
and, while often aggregated into the clinical syndrome of sepsis, overlap the resolution to identify cell type-specific signatures5–7 or single-cell
with other critical illness syndromes1–3. There is an urgent need to better interrogation of peripheral blood mononuclear cells (PBMCs)8, which
delineate such extreme responses to infection, given the COVID-19 pan- omits neutrophils (Neu).
demic and the wider, global burden of all-cause sepsis, which accounts Data from animal models demonstrate key protective and path-
for 11 million deaths per year and has a persistently high mortality of ogenic roles for Neu in sepsis, in some instances involving specific
1Wellcome Centre for Human Genetics, Nuffield Department of Medicine, University of Oxford, Oxford, UK. 2Wellcome Sanger Institute, Wellcome
Genome Campus, Cambridge, UK. 3Kennedy Institute of Rheumatology, University of Oxford, Oxford, UK. 4John Radcliffe Hospital, Oxford Universities
Hospitals NHS Foundation Trust, Oxford, UK. 5NIHR Oxford Biomedical Research Centre, Oxford, UK. 6William Harvey Research Institute, Faculty of
Medicine and Dentistry, Queen Mary University, London, UK. 7Chinese Academy of Medical Science Oxford Institute, University of Oxford, Oxford, UK.
*A list of authors and their affiliations appears at the end of the paper. e-mail: julian.knight@well.ox.ac.uk
Nature Immunology | Volume 24 | May 2023 | 767–779 767
Article https://doi.org/10.1038/s41590-023-01490-5
UMAP1
subsets9,10. In humans, the clinical observation of a ‘left shift’ in com- Sepsis is highly heterogeneous2 and immune suppression associ-
plete blood count to increased immature Neu in severe infection is well ated with apoptosis, epigenetic reprogramming and downregulation
recognized11. Neu abundance varies between septic and non-infectious of activating cell surface molecules in multiple cell types2 is a predomi-
inflammation12, while single-cell transcriptomics indicates that they nant feature in many patients. Sepsis subphenotypes are reported2,5–7,16,
are important in the pathogenesis of severe COVID-19 (ref. 13) and but their relationship with mechanisms of immune dysfunction is not
acute respiratory distress syndrome (ARDS)14. Expansion of subsets well defined. Sepsis response signatures (SRSs) from whole-blood
of immunosuppressive granulocytes associate with a higher risk of transcriptomics identify dynamic response states, with assignments
nosocomial infection15. in the SRS1 group or a high likelihood of SRS1 group (SRSq), associated
Nature Immunology | Volume 24 | May 2023 | 767–779 768
2PAMU
a Discovery Validation
scWB atlas mmV WB-CID datasets
Whole blood
UMAP1
−2.5 0 2.5 5.0
log FC
CS Sepsis
2PAMU
scHSPC atlas
HC CS Sepsis HC Sepsis HC Sepsis Patients with infectious disease
CD34+ HSPCs Whole blood Plasma Whole blood
scRNA-seq + Functional scRNA-seq + scATAC-seq Bulk timsTOF Bulk transcriptomics scRNA-seq
AbSeq assays CyTOF RNA-seq proteomics
Abundance Gene expression
MOFA deconvolution profiles
b c
Mature Neu log FC Nhood size
Mast cells/ B cells/ S100A8/9hi Neu 50
eosinophils plasmablasts Degranulating Neu Sepsis 3 100
IL1R2+ immature Neu 0 150
PADI4+ immature Neu 200
MPO+ immature Neu/progenitors HC –3 250
Cycling Neu progenitors
Apoptosing Neu Overlap size
Mast cells/eosinophils
20
Eosinophils
40
Platelets
Monocytes/DCs HSCs 60
Classical Mo 80
Non-classical Mo
T/NK cells cDCs
Neutrophils pDCs
Plasmablasts
B cells
NK cells
Cycling T/NK cells Neutrophil Naive CD8+ T cells
progenitors CD8+ T cells
Naive CD4+ T cells
Memory CD4+ T cells
d e
Mature Neu Mature Neu
S100A8/9hi Neu S100A8/9hi Neu
Degranulating Neu Degranulating Neu
IL1R2+ immature Neu IL1R2+ immature Neu
PADI4+ immature Neu PADI4+ immature Neu
MPO+ immature Neu/progenitors MPO+ immature Neu/progenitors
Cycling Neu progenitors Cycling Neu progenitors
Apoptosing Neu Apoptosing Neu
Eosinophils Eosinophils
Mast cells/eosinophils Mast cells/eosinophils
Platelets Platelets
HSCs HSCs
Classical Mo Classical Mo
Non-classical Mo Non-classical Mo
cDCs cDCs
pDCs pDCs
Plasmablasts Plasmablasts
B cells B cells
Cycling T/NK cells Cycling T/NK cells
NK cells NK cells
CD8+ T cells CD8+ T cells
Naive CD8+ T cells Naive CD8+ T cells
Memory CD4+ T cells Memory CD4+ T cells
Naive CD4+ T cells Naive CD4+ T cells
−6 −3 0 3 6
log FC
HC Sepsis
Fig. 1 | Whole-blood single-cell census in sepsis. a, Study design showing CS, n = 7; sepsis, n = 26) scRNA-seq (272,993 cells) annotated for differential cell
patients and analytical approaches applied. Discovery phase: scWB atlas for HCs populations. DC, dendritic cell; cDCs, classical DCs; pDCs, plasmacytoid DCs.
(n = 6), sterile inflammation controls after CS (n = 7) and patients with sepsis c, UMAP for scWB scRNA-seq differential abundance in samples from patients
(n = 26) by joint scRNA-seq and cell-surface protein profiling; scHSPC atlas for with sepsis (n = 26) compared to HCs (n = 11), with sampled neighborhoods
HCs (n = 7) and patients with sepsis (n = 15) (multiome scRNA-seq and scATAC- colored by statistical significance (spatial FDR < 0.05). Nhood, neighborhood.
seq). Validation phase: mmV in HCs (n = 11) and patients with sepsis (n = 36), d,e, Beeswarm plots of differential cell abundance in scWB with cluster labels of
including CyTOF and bulk RNA-seq of whole blood and timsTOF proteomics neighborhoods depicted and compared for patients with sepsis (n = 26) versus
in plasma; WB-CID datasets (n = 1,595) with deconvolution using scWB. HCs (n = 11) (d) and patients with sepsis (n = 26) versus after CS (n = 7) (e).
b, Uniform Manifold Approximation and Projection (UMAP) for scWB (HCs, n = 6;
Article https://doi.org/10.1038/s41590-023-01490-5
with immunosuppression, differential response to steroid therapy, of patients with sepsis by immunomagnetic selection) with alloge-
more severe disease and higher early mortality5,17–19. Here we identified neic CD4+ T cells isolated from healthy donor leukocyte cones at a
differences in Neu function and subset abundance during sepsis, which 4:1 Neu:T cell ratio in medium supplemented with interleukin (IL)-2
were a consequence of altered granulopoiesis. We demonstrated these and CD3/CD28 Dynabeads. After 72–96 h of culture, the fraction of
immunosuppressive granulocytic and granulopoietic disturbances proliferating CD4+ T cells (calculated using non-bead-stimulated
were the functional basis of the SRS1 subphenotype of sepsis. T cells cultured without Neu as the baseline proliferative fraction
of cells in each sample) and the percentage of either PD-1+ or CD69+
Results CD4+ T cells (calculated relative to the CD3/28 bead-stimulated, no
Immature and cycling neutrophils are increased in sepsis T cells control culture, to account for donor variation) was lower when
To generate an unbiased single-cell whole-blood (scWB) atlas of the co-cultured with CD66b+ Neu from patients with sepsis compared
sepsis response for all peripheral blood leukocyte populations, includ- to HCs (Fig. 2a), indicating sepsis CD66b+ Neu inhibited CD4+ T cell
ing Neu, we assayed freshly sampled whole blood from 26 patients proliferation and activation. There was no difference in the percent-
with all-cause sepsis with a change in quick sequential organ failure age of live, non-apoptotic CD4+ T cells on far-red DNA staining after
assessment (SOFA) score of ≥2 points, indicating organ dysfunction 72–96 h of co-culture with either HCs or sepsis CD66b+ Neu (Extended
and a physiological measure of acute illness severity score (national Data Fig. 2e). For samples on which both single-cell sequencing and
early warning score 2; NEWS2) of ≥7, indicating patients who required functional co-culture assays were performed, we correlated MPO+
an urgent critical care response (Supplementary Table 1 and Methods); Neu, PADI4+ Neu, IL1R2+ Neu, S100A8/9+ Neu, degranulating CEACAM8+
9 sepsis convalescents (sampled 1–3 months after hospital discharge); Neu and mature CD10+CD16+ Neu frequency with the fraction of pro-
6 age- and sex-matched healthy controls (HCs); and 7 patients after car- liferative CD4+ T cells, PD-1 expression and CD69 expression. None
diac surgery (CS) as a sterile inflammation control (Fig. 1a and Methods). showed statistically significant correlation (Extended Data Fig. 2f),
We performed joint single-cell RNA and cell surface protein profiling of suggesting that all Neu subsets might be involved in the observed
272,993 cells (Fig. 1b, Extended Data Fig. 1 and Supplementary Table 2). effect of CD66b+ Neu on CD4+ T cell proliferation and PD-1 and
After clustering and annotation of major immune cell types (Extended CD69 expression.
Data Fig. 1a–c and Methods), we observed recognized hallmarks of Depletion of arginine by increased arginase-1 activity and upreg-
peripheral blood sepsis immunophenotypes, including neutrophilia, ulation of T cell immune checkpoint PD-1–PD-L1/PD-L2 pathways
lymphopenia and reduced HLA-DR expression in CD14+CD16− classical can modulate the immunosuppressive properties of granulocytic
monocytes (cMo)20 (Extended Data Fig. 1d). myeloid-derived suppressor cells (G-MDSCs)12,15. Inhibition with argi-
We performed fine-resolution clustering and annotation nine and an Arg1 inhibitor, or antibodies to PD-L1/PD-L2 applied to
(Extended Data Fig. 1e–i and Supplementary Table 3). RNA velocity and the CD66b+ Neu-CD4+ T co-cultures, did not reverse the effects on
partition-based graph abstraction showed annotated Neu subpopu- proliferation, PD-1 and CD69 expression compared to co-cultures
lations followed the expected maturation sequence from immature without inhibitors (Extended Data Fig. 2g). Addition of a prosta-
MPO+ Neu to PADI4+ Neu to IL1R2+ Neu to S100A8/9+ Neu to mature glandin EP2 receptor antagonist (TG6-10-1) increased CD69 expres-
CD10+CD16+ Neu (Extended Data Fig. 1j,k). We identified that degranu- sion compared to no inhibitor (Extended Data Fig. 2g), whereas
lating CEACAM8+ Neu, S100A8/9hi Neu, IL1R2+ Neu, PADI4+ Neu, MPO+ the cyclo-oxygenase inhibitor indomethacin or a selective prosta-
Neu and cycling MK167+CYP1B1+ Neu were all proportionally increased glandin EP4 receptor competitive antagonist (GW-627368) did not
in sepsis compared to HCs, whereas all mononuclear cell subsets, (Extended Data Fig. 2g), suggesting effects at the level of pre-formed
except CD19+CD38+CD71+ plasmablasts, were reduced (Fig. 1c,d). The prostaglandin E2.
increase in degranulating CEACAM8+ Neu and S100A8/9hi Neu and the To understand how sepsis CD66b+ Neu mediated CD4+ T cell sup-
reduction in all mononuclear cell subsets, was also seen in CS compared pression, we analyzed differential gene expression (DGE) of mature
to HCs (Extended Data Fig. 2a,b), suggesting they represented nonspe- CD10+CD16+ Neu, S100A8/9hi Neu, degranulating CEACAM8+ Neu and
cific features of inflammation. By contrast, higher abundance of the IL1R2+ Neu in the scWB dataset (Fig. 2b). We tested for and observed
immature IL1R2+ Neu, PADI4+ Neu and MPO+ Neu subsets and cycling statistically significant enrichment of prostaglandin regulation or
MK167+CYP1B1+ Neu were specific to sepsis (Fig. 1c–e and Extended synthesis pathways in all tested Neu subsets from patients with sepsis
Data Fig. 2c,d). These findings demonstrated differential abundance compared to HCs (Extended Data Fig. 2h). We investigated the suppres-
of specific immature and cycling Neu subsets in sepsis. sive capacity by analyzing DGE indicative of experimentally validated
G-MDSCs21–23 and found increased expression of this gene set (including
Neutrophils in sepsis and recovery are immunosuppressive SLC2A6, MMP8 and DUSP6) in both CD10+CD16+ Neu and IL1R2+ Neu and
To functionally test the immunosuppressive properties of sepsis Neu, PADI4+ Neu and MPO+ Neu from patients with sepsis compared to HCs
we co-cultured bulk CD66b+ Neu (isolated from fresh whole blood (Extended Data Fig. 2i).
Fig. 2 | Neutrophil function in sepsis and convalescence. a, Percentage of (Pearson r, FDR < 0.05, 95% confidence interval) of days after acute sepsis and the
eFluor450 cell proliferation dye+ CD4+ T cells (top) and activated PD-1+ (middle) proportion of mature CD10+CD16+ Neu in convalescent samples (n = 9) collected
and CD69+ (bottom) CD4+ T cells in co-cultures of bulk CD66b+ Neu isolated by at 1–6 months after hospital discharge. d, Consensus DGE analysis stacked bar
immunomagnetic selection from whole blood of patients with sepsis (n = 22) plots of all Neu in convalescent samples compared to all Neu in HC samples.
or HCs (n = 10) and allogeneic CD4+ T cells from healthy donor leukocyte cones Downreg, downregulated; upgreg, upregulated. e, Frequency of PD-1+ (left) and
cultured at a 4:1 Neu:CD4+ T cell ratio in medium supplemented with IL-2 and CD69+ (right) CD4+ T cells at 72–96 h of co-culture with bulk CD66b+ Neu isolated
CD3 + CD28 Dynabeads for 72–96 h relative to healthy CD4+ T cells cultured by immunomagnetic positive selection from whole blood from convalescent
with beads and without Neu. Non-bead-stimulated T cells cultured without patients (n = 9) and HCs (n = 10). Box plots denote minimum and maximum
Neu were used as the baseline proliferative fraction of cells in each sample as with whiskers and bottom quartile, median and upper quartile with the box.
a readout of proliferation. CD3 + CD28 bead-stimulated, no co-culture T cells f, Assessment of phagocytosis by ingestion of pHrodo Green Escherichia coli
were used to account for donor variation for PD-1+ and CD69+CD4+ T cells. Box bioparticles stained with 7-AAD, CD66b-AF700 and Siglec-8-APC in bulk CD66b+
plots denote minimum and maximum with whiskers and bottom quartile, Neu isolated from convalescent patients (n = 9) and HCs (n = 10) as in e. Box plots
median and upper quartile with the box. b, Heat maps showing DGE for mature denote minimum and maximum with whiskers and bottom quartile, median and
CD10+CD16+ Neu, S100A8/9hi Neu, degranulating CEACAM8+ Neu and IL1R2+ upper quartile with the box. Conv, convalescence. Functional assays were tested
Neu comparing patients with sepsis (n = 22) versus HCs (n = 10). c, Correlation with two-sided Wilcoxon rank-sum tests. *P < 0.05, **P < 0.01, ***P < 0.001.
Nature Immunology | Volume 24 | May 2023 | 767–779 769
Article https://doi.org/10.1038/s41590-023-01490-5
To test whether the increased abundance of immature Neu Neu (Fig. 2c), suggesting that recovery involved gradual resump-
populations in sepsis and their immunosuppressive features were tion of mature Neu production over 6 months. Consensus DGE of
linked to increased bone-marrow release of immature Neu, we ana- all Neu showed genes, including IL1B and type I interferon pathway
lyzed samples at 1–6 months after hospital discharge (n = 9) (scWB (IFIT1, IFIT2, IFIT3, IFI6 and MX1) were downregulated in convales-
cohort). Although no individual Neu subset was differentially abun- cence compared to HCs (Fig. 2d). Using the same cell isolation and
dant between convalescent and HC samples (Extended Data Fig. 3a), co-culture system as for acute sepsis, we found convalescent CD66b+
we observed a strong correlation in convalescent samples between Neu sampled at 1–6 months did not suppress CD4+ T cell proliferation
time from acute sampling and increasing proportion of CD10+CD16+ (Extended Data Fig. 3b), but expression of CD69 and PD-1 on CD4+
f
Nature Immunology | Volume 24 | May 2023 | 767–779 770
evitaler noitarefilorp llec T ot evitaler sllec T +1-DP
ot evitaler sllec T +96DC
)%( ueN tuohtiw erutluc ot )%( ueN tuohtiw erutluc
)%( ueN tuohtiw erutluc
a b
d
5
0
−5
−10
Percentage of all cells
e
)CF(gol
egareva
evitalumuC
9A001S 2SRI 5MTPAL 1HDPMI 1GRICT 1CRNP ACAKRP INCC 2G1KNSC AC3PPP 1TKA XYZ 661FNR 4AOCN A021MAF A1OROC 6PNES 1FCN 2TESANR SRBF 1CPBAP B9R1PPP AC1PPP 2PAGQI MIV 2DMIL 55DC 73A52CLS 3CDRRA 1SA−1B2PTA 41CELGIS BPBEC 1.863210CA 52MIMS 1PMIT 5PBG 4PAMIG B2RGCF DFC 2TIFI 1RCC C−ALH 1TIFI B1LI MDA BSTC SOF 1XM 3TIFI 1FAX ZYL 6IFI A21CELC
1_Conv
2_Conv
3_Conv 4_Conv
5_Conv 6_Conv 7_Conv 8_Conv 9_Conv
gerpU
gernwoD
vnoc
ni
vnoc ni
Mature CD10+CD16+ Neu
100 r = 0.75, FDR = 0.04
75
50
30 35 40
etuca
morf
syaD
ot evitaler
sllec
T +1-DP
elpmas
)%( ueN
tuohtiw
erutluc
ot evitaler
sllec
T +96DC
)%( ueN
tuohtiw
erutluc
c
ecnecseroulf
naideM
ytisnetni
Mature CD10+CD16+ Neu S100A8/9hi Neu
1 1 0 6 4 8 5 5 20 0 0 0 0 0 0 0 * * * F C F P I S P N O P M H L K S H C C L T H M C R C M T P P B C H N A A A A A A A T I C A A R S C T R 2 N C T L H P P P R L C N D E K D D C H S L P R L L L L G S S Y R G C B P B 1 M M K G C 0 K E A A C M M O G X N A R F 3 H A K 0 1 3 O L I 4 4 2 A 3 Y A D C 7 A C 3 1 E − − 0 3 P D B R 5 H U M A G 8 2 M 0 D 4 A A L C 1 A 5 7 R L 7 1 N D D R R 9 1 1 X − 9 9 4 I 3 0 C 9 B D B 4 1 0 9 6 C 2 1 1 P 1 A 1 1 2 A P R 1 D 8 A 0 2 A 1 A 1 A 1 6 E 8 A 1 B 3 1 A B 8 5 2 8 2 8 − 1 . 1 B 6 2 A 1 . . S 1 1 1 F N P C M M S P S K M C C P I O K G C C P T M H S C P H C T C P F B A A A A A A L A C B S C D L F N 2 C L T M L U D P D C L N E Y C D A D D H S L L P L 1 M S E O A R 4 F C C B P 3 M R C A A G E C M O P L N F R F A A C K 0 1 8 H T N I 4 A K 1 P 3 V Y C A D 5 7 L R T 1 1 M 1 1 − − D 1 T U M M A A F 8 M 0 A 4 N L D 2 A A A 8 9 D R L 7 1 1 3 1 5 1 N D D 1 8 1 L C C 9 B D B 4 0 4 9 6 C 1 B 1 T 2 1 A 1 A A 3 8 7 2 7 Q R 1 A 1 1 A 1 6 E 8 A S 4 B 3 4 4 1 1 8 B B A 2 8 3 1 1 1 . 2 2 .1 S ex c p a H S − − 0 1 2 r l 2 1 e e C e p d s s s i i s on
0 Degranulating CEACAM8+ Neu Immature IL1R2+ Neu
6 4 20 0 0 0 *** H Se C psis C S S H P T H L P P M O T M P N G N S N G T C R C C M C B H M P P C A A A A A A D R B I L D L D 2 N T P E S P O P N C D L E E K D C X L H S G P L P N L G T Y O Y A I R C B P L 3 T G L 3 P E A G E D C M G C X A R F A G N 0 R 1 O O N I C L F D R 1 3 Y C R S S D 5 7 N C 4 B 1 1 − 3 1 R D H M A Y R F L 0 D 2 L A P 3 1 1 5 N 3 D R L 7 1 3 5 S 1 D D 2 8 1 − 9 8 C I 0 3 B 4 T 0 9 6 C 2 1 P 1 8 7 8 3 A 1 R A 1 1 6 8 A 1 B 8 B 8 1 1 . 2 2 .1 C S M C P H I G I H M P C V R C G E T P F R L M P L C F T M D R P F H G J J A A L R U U E R O A O N U M L F E P H T A H G N N C P D A C E L P K S A A A 1 M E P T A N A N N K L I R O M R G C B E F A O 3 H O N S S S X 0 S N D S T 1 T B H F N K I P F C C 7 G 2 A B D P 1 C 1 A T B M A T 2 1 7 1 1 1 2 D S D O B 3 D 8 0 B 7 2 1 2 I 8 6 L 8 2 D 1 A P P 4 2 7 B 2 S 3 9 M H 8 A P 5 P P 6 2 A O 1 1 H 8 8 . 1 8 1
80 * 60 * 800 *** HC Conv
60 600
40
40 400
20
20 200
0 0 0
Article https://doi.org/10.1038/s41590-023-01490-5
ZBTB20−AS1
AL353147.1
MED12L 60
FLT3
ELMO1 AL033519.5
PBX1 IGFBP7−AS1
40 RAPGEF2 FNDC3B
FREM1 FO393414.3 AREG
PRKG2 PIK3R1 AL512658.2
20
0
−4 0 4
log FC
2
T cells were reduced and phagocytosis was increased in sepsis con- (FDR = 0.0002) (Extended Data Fig. 3h,i), suggesting lymphoid deple-
valescence samples compared to HCs (Fig. 2e,f). These observations tion and an erythro-myeloid bias in sepsis.
demonstrated immunosuppressive features of sepsis Neu on CD4+ Multimodal clustering on 29,336 hematopoietic stem cells (HSCs)
T cells, acutely and in convalescence, which involved multiple Neu retained after excluding progenitor cells identified seven clusters
subsets with a potential role for prostaglandins. (Fig. 3a). Comparing patients with sepsis to HCs, clusters C3, C4, C5 and
C7 were enriched in sepsis, whereas C6 was enriched in HCs (Fig. 3b and
Sepsis alters granulopoietic profile of circulating HSPCs Extended Data Fig. 3j). To understand whether any expanded clusters
To further investigate granulopoiesis, we performed single-cell RNA-seq represented HSCs with a granulopoietic bias, we leveraged Human Cell
(scRNA-seq) and single-cell assay for transposase-accessible chromatin Atlas (HCA) annotated HSCs and progenitor scRNA-seq bone-marrow
with sequencing (scATAC-seq) on sorted live, singlet, CD34+CD45+ data26 to define genes upregulated in granulopoietic cells, including
hematopoietic stem and progenitor cells (HSPCs) from PBMCs isolated MPO, RNASE2, ELANE and FKBP2 (Methods and Extended Data Fig. 3k).
from 15 patients with sepsis and 7 HCs. We assigned HSPC identity by Clusters C5 and C7 had the highest expression of this gene set (Fig. 3c).
mapping scRNA-seq data to healthy donor reference bone-marrow Granulopoiesis is driven by transcriptional circuits mediated by CEBP
mononuclear cell scRNA-seq datasets24,25, performed clustering after transcription factors, where CEBPA is important during steady-state
multidimensional reduction by combining scRNA-seq and scATAC-seq, granulopoiesis (SSG) and CEBPB is a key regulator of emergency gran-
with assignment using majority RNA mapping (Extended Data ulopoiesis (EG)27,28. CEBPA/CEBPB binding motifs were enriched in
Fig. 3c–f). Multimodal clustering identified five clusters of progeni- accessible chromatin sites in both C5 and C7 (Fig. 3d), consistent with
tor cells (Extended Data Fig. 3g). In patients with sepsis compared to upregulated SSG and EG. Comparison of gene expression profiles of
HCs, cluster P4 (representing lymphocyte progenitors CDNTThi, FLT3hi, C3, C4, C5 or C7 with C6 identified genes, including SETBP1 and FLT3,
CD79hi and HOPXhi) was reduced (false discovery rate (FDR) = 0.002) which are involved in expanded myelopoiesis29,30, as upregulated in C5
(Extended Data Fig. 3h,i), whereas cluster P3 (defined by erythroid and C7, respectively (Fig. 3e,f). These data provide evidence for altered
lineage progenitor genes HBBhi, HBDhi, KLF1hi and AC1hi) was increased granulopoiesis in sepsis that involved specific HSC clusters.
Nature Immunology | Volume 24 | May 2023 | 767–779 771
RDF
gol– 01
SETBP1
DLGAP2
90 NEAT1
AL033519.5
TCF4
MED12L MCTP2
ZBTB20−AS1 INPP4B
60 ITGA4 AL138963.4 AREG
AC010880.1
AL353147.1 PTPRC KIAA1211
30
0
−6 −3 0 3 6
log FC
2
RDF
gol– 01
b
C1
C2
C3
C4
C5
C6
C7 HSC clusters
UMAP1
2PAMU
a
Overlap size
20
40
60
Nhood size
100
200
Log FC
Sepsis 6 3
HC 0
–3
–6
CEBPA motif CEBPB motif
chromVAR z score chromVAR z score
UMAP1
2PAMU
UMAP1
2PAMU
0.8
0.6
0.4
0.2
0
C1 C3 C4 C5 C6 C7
Cluster
d
z score
−2.502.55
fo
noisserpxe
dezilamroN
tes
eneg
rotinegorp
etycolunarg
C7
C6
C5
C4
C3
C2
C1
−4 0 4
c log FC
NS
**** Downregulated Upregulated f Downregulated Upregulated
**** **** in C5 in C6 in C7 in C6
****
z score
−20 2 4 6
sretsulc
CSH
HC Sepsis
UMAP1
Upregulated Upregulated
Downregulated Downregulated
Not differential Not differential
2PAMU
e
Fig. 3 | Circulating HSC atlas confirms heightened granulopoiesis in sepsis. c, Granulopoiesis gene set scores per HSC cluster with differential cluster scoring
a, UMAP of scRNA-seq- and scATAC-seq-defined HSC clusters (29,336 cells) tested with Kruskal–Wallis and post hoc Dunn’s tests. Violin plot with median,
after exclusion of progenitor cells, with data arising from sorted live, singlet, 95% confidence interval and interquartile range. ****FDR < 0.0001 comparing C5
CD34+CD45+ HSPCs from the PBMCs of patients with acute sepsis (n = 15), or C7 versus other clusters. NS, not significant. d, chromVAR transcription factor
convalescent sepsis patients (n = 5) and HCs (n = 7). b, Differential abundance motif z score deviation for CEBPA (left) and CEBPB (right) in HSC from acute
of HSCs between patients with sepsis and HCs as in a, with corresponding sepsis samples (n = 15) and HCs (n = 7). e,f, DGE between cluster C5 versus C6 (e)
beeswarm plot (right) and UMAP visualization of sampled neighborhoods and C7 versus C6 (f) in sepsis samples (n = 15).
colored by statistically significant enrichment (spatial FDR < 0.05) (left).
Article https://doi.org/10.1038/s41590-023-01490-5
a
log FC Nhood size
6 50
SRS1 4 100
2 150
Non- 0 200
SRS1 –2 250
–4
Overlap size
20
40
60
80
−5.0 −2.5 0 2.5 5.0
log FC
UMAP1
Non-SRS1 SRS1
Altered granulopoiesis drives a sepsis subphenotype Data Fig. 4c–e). IL1R2+ Neu and cycling MK167+CYP1B1+ Neu were
We next investigated whether the altered Neu-granulopoietic profile increased in patient samples assigned as SRS1 compared to non-SRS1,
observed here was related to a previously identified SRS1 subphenotype whereas mononuclear cells, including CD14+CD16− cMo, CD56+ nat-
in patients with sepsis5,17. Based on the expression of a seven-gene set ural killer (NK) and LTB+IL7R+memory CD4+ T cells, were depleted
(DYRK2, CCNB1IP1, TDRD9, ZAP70, ARL14EP, MDC1 and ADGRE3), the (Fig. 4a,b). Large numbers of differentially expressed genes were
SRS1 subphenotype was assigned to 16 out of 26 patients in the scWB detected in mature CD10+CD16+ Neu (EBI3, MYOSLID and SLC1A3),
cohort (Extended Data Fig. 4a,b), in agreement with consensus or unsu- S100A8/9hi Neu (SLC1A3, KLF14 and SGPP2), degranulating CEACAM8+
pervised clustering of the pseudobulked scRNA-seq data (Extended Neu (SFXN1, HS3ST3B1 and PDE4D) and IL1R2+ Neu (NAIP, IDI1 and
Nature Immunology | Volume 24 | May 2023 | 767–779 772
2PAMU
d
30
20
10 e
0
−10
−20
−20 0 20 40
PC1 (22.66% of variance)
)ecnairav
fo
%70.11(
2CP
20
10
0
−10
−20
−20 0 20
PC1 (24.68% of variance)
)ecnairav
fo
%88.9(
2CP
20
10
0
−10
−20
−30
−40 −20 0 20
PC1 (16.34% of variance)
)ecnairav
fo
%19.01(
2CP
20
0
−20
−40 −20 0 20 40
PC1 (22.65% of variance)
)ecnairav
fo
%2.11(
2CP
b
c Mature CD10+CD16+ Neu S100A8/9hi Neu
50
40
30
20
10
0
50
40
30
Degranulating CEACAM8+ Neu Immature IL1R2+ Neu 20
10
0
SRS1
Non-SRS1
ot
evitaler
sllec
T
+1-DP
ot
evitaler
sllec
T +96DC
)%(
ueN
tuohtiw
erutluc
)%(
ueN
tuohtiw
erutluc
600
500
400
300
200
100
0
selcitrapoib
neerG
ecnecseroulf
naidem(
)ytisnetni
Mature Neu
S100A8/9hi Neu
Degranulating Neu
IL1R2+ immature Neu PADI4+ immature Neu
MPO+ immature Neu/progenitors
Cycling Neu progenitors
Apoptosing Neu
Eosinophils
Mast cells/eosinophils
Platelets
HSCs
Classical Mo
Non-classical Mo
cDCs
pDCs
Plasmablasts
B cells
Cycling T/NK cells
NK cells
CD8+ T cells
Naive CD8+ T cells
Memory CD4+ T cells
Naive CD4+ T cells
* SRS1
Non-SRS1
*
SRS1
*
Non-SRS1
Fig. 4 | Immature and immunosuppressive neutrophils drive the SRS1 co-culture with CD66b+ Neu isolated from samples assigned as SRS1 (n = 6)
subphenotype. a, Differential cell abundance from whole-blood scRNA-seq and non-SRS1 (n = 13). Box plots denote minimum and maximum with
UMAP with sampled neighborhoods colored by statistical significance (spatial whiskers and bottom quartile, median and upper quartile with the box.
FDR < 0.05) in patient samples in the scWB cohort (n = 26 patients with sepsis) e, Assessment of phagocytosis in CD66b+ Neu isolated from samples assigned
assigned as SRS1 (n = 16) or non-SRS1 (n = 10). b, Beeswarm plot of differential SRS1 (n = 15) and non-SRS1 (n = 14) and incubated with pHrodo Green E. coli
cell abundance in scWB with cluster labels of neighborhoods depicted and bioparticles stained with 7-AAD, CD66b-AF700 and Siglec-8-APC. Box plots
compared for patients assigned as SRS1 and non-SRS1 as in a. c, First two principal denote minimum and maximum with whiskers and bottom quartile, median and
components from PCA of pseudobulked Neu states colored by SRS assignment. upper quartile with the box. Functional assays tested with two-sided Wilcoxon
d, Percentage of PD-1+ (top) and CD69+ (bottom) CD4+ T cells after 72–96 h of rank-sum tests. *P < 0.05.
Article https://doi.org/10.1038/s41590-023-01490-5
CLEC4D) in samples assigned as SRS1 compared to non-SRS1 (Extended Fig. 7g–i), consistent with gene modules and cell clusters, rather than
Data Fig. 5a), with a corresponding separation by SRS status on plasma proteins, being associated with SRS. Overall, the results show
principal-component analysis (PCA) for these populations (Fig. 4c). that differences in immature Neu populations, assayed using different
By contrast, there were minimal differences in mononuclear cell sub- modalities and Neu-granulopoietic dysfunction, were enriched in the
sets between SRS1 and non-SRS1 (Extended Data Fig. 5b), consistent SRS1 patient subphenotype.
with SRS groupings being driven by Neu. Cell surface expression of
IL-1R2, measured by flow cytometry, showed a moderate correla- STAT3 and granulopoiesis regulators define SRS1
tion with expression of IL1R2 in CD66b+ Neu isolated from patient Next we investigated the specific pathways and mediators that con-
samples assigned SRS1 (Extended Data Fig. 5c). In co-cultures, SRS1 tributed to observed differences in the SRS1-associated Neu subsets.
CD66b+ Neu suppressed CD4+ T cell activation more than non-SRS1 Consensus non-negative matrix factorization of Neu subsets in the
CD66b+ Neu (Fig. 4d), but not CD4+ T cell proliferation (Extended Data scWB cohort identified gene expression programs (GEPs) specific
Fig. 5d). Moreover, SRS1 CD66b+ Neu displayed reduced phagocytosis to Neu populations (Neu-GEP) that positively correlated with SRSq,
compared to non-SRS1 (Fig. 4e), which was not restored by the addi- namely CD10+CD16+ Neu_program_3 (enriched for IL-6 activation
tion of granulocyte–macrophage colony-stimulating factor (GM-CSF) and the JAK–STAT3 signaling pathway (IL-6–JAK–STAT3), prostaglan-
(Extended Data Fig. 5e). These data indicated that SRS1 represented an din (PG) synthesis and regulation, hereafter ‘PG’) and CD10+CD16+
immunosuppressed state driven, at least in part, by Neu dysfunction. Neu_program_8 (tumor necrosis factor (TNF) signaling via nuclear
To investigate this further in a multimodal validation (mmV) factor (NF)-κB, hereafter ‘TNF’); S100A8/9hi Neu_program_8 (IL-6–JAK–
cohort, we reanalyzed whole-blood bulk RNA-seq and mass cytom- STAT3, PG); degranulating_CEACAM8+ Neu_program_9 (PG); PADI4 +
etry (CyTOF) immunophenotyping data31 in 42 samples from 36 Neu_program_7 (hypoxia); and IL1R2+ Neu_program_5 (metabolic
individuals with all-cause sepsis and 11 age- and sex-matched HCs regulator MTORC1 signaling, hypoxia) and IL1R2+ Neu_program_8
(Supplementary Table 1). SRS assignment of the 36 patients reca- (TNF) (Fig. 5a; Supplementary Tables 3 and 4). We predicted master
pitulated higher early mortality in SRS1 compared to non-SRS1 regulators per GEP and found granulopoiesis transcription factors,
patients (Extended Data Fig. 6a,b). We identified eight Neu clusters including CEBPB and STAT3 (CD10+CD16+ Neu_program_3, S100A8/9hi
in the CyTOF dataset (Extended Data Fig. 6c–f). More immature Neu_program_8 and IL1R2+ Neu_program_8) and CEBPA (S100A8/9hi
CD64+CD10loCD16loCD15lo Neu and CD71hiCD38+Ki-67+ pro-Neu or Neu_program_8) were highly enriched (Fig. 5b). STAT3 and SPI1 were
CD71loKi-67+ pre-Neu were detected in patient samples assigned highly enriched for the CD64+CD10loCD371lo Neu correlated module
SRS1 compared to non-SRS1 (Extended Data Fig. 6g,h). Pseudotime 10 (mmV cohort) (Fig. 5c).
trajectory analysis, which arranged cells in a progression of sequen- Given the role of STAT3 in EG and enrichment for STAT3 in
tial maturation stages, demonstrated over-representation of SRS1 SRSq-correlated Neu-GEP, we investigated whether cytokines known
samples earlier in the trajectory (Extended Data Fig. 6i–l). PCA of to induce granulopoiesis and signal through STAT3 differed in plasma
CyTOF data showed separation of Neu subsets, but not mononuclear abundance (mmV cohort). Granulocyte colony-stimulating factor
cell compartments, between samples assigned as SRS1 compared to (G-CSF) and IL-6 were elevated in patient samples assigned as SRS1
non-SRS1 (Extended Data Fig. 6m), indicating changes in Neu subsets compared to non-SRS1, whereas macrophage colony-stimulating fac-
drove the patient SRS grouping. tor (M-CSF) and GM-CSF showed no statistically significant difference
To further investigate drivers of the SRS subphenotype, we (Fig. 5d). Consistent with G-CSF priming of Neu in cancer increasing
reduced mmV RNA-seq dimensionality to 33 gene modules using NETosis33, we found that CD66b+ Neu from patient samples assigned
weighted gene coexpression network analysis (WGCNA) and identi- as SRS1 underwent more NETosis than non-SRS1 samples on live-cell
fied 13 differentially expressed modules between SRS1 and non-SRS1 imaging for DNA-bound Cytotox Green reagent when stimulated
assigned samples (FDR < 0.01) (Extended Data Fig. 7a). The SRS1 with phorbol 12-myrisate 13-acetate (PMA) (Fig. 5e,f). These data
upregulated modules were enriched for gene expression signatures of demonstrated elevated STAT3-driven GEP in different SRS1-correlated
differentiating Neu32. Module 10 (bone-marrow Neu and stage 1 differ- Neu subsets and increased levels of circulating cytokines that sig-
entiating Neu gene sets, including ALOX5, CYBB and LCN2) (Extended nal through STAT3 and control granulopoiesis in SRS1 compared to
Data Fig. 7b) correlated with immature CD64+CD10loCD16loCD15lo Neu non-SRS1 patients.
frequency (Extended Data Fig. 7c) and a gene expression signature
defining IL1R2+ Neu (in the scWB cohort) including IL1R2, PFKFB2 and STAT3 processes in HSC cluster drive EG in SRS1
RETN genes (Extended Data Fig. 7d and Methods). To further validate To test whether the SRS1 patient subphenotype represented a state of
enrichment of IL1R2+ Neu in SRS1, we performed cell type and cell maladaptive granulopoiesis that involved heightened STAT3-mediated
state deconvolution on an independent total leukocyte microarray EG, we investigated whether there was any difference in circulating
dataset5,17,18 consisting of 542 patients with all-cause sepsis, using HSCs between SRS1 and non-SRS-1 subphenotypes, specifically the cell
the scWB single-cell multiomics dataset as a reference. We observed clusters differentially associated with granulopoiesis (C5 and C7), in 15
that IL1R2+ Neu and cycling MK167+CYP1B1+ Neu were increased in patients with sepsis from the single-cell hematopoietic stem and pro-
patient samples assigned as SRS1 compared to non-SRS1 (Extended genitor cell (scHSPC) atlas cohort. Cluster C5, but not C7, was enriched
Data Fig. 7e). in patient samples assigned SRS1 compared to non-SRS1 (Fig. 6a,b and
Next, we performed multiomics factor analysis (MOFA) to inte- Extended Data Fig. 8a). We characterized the differentially accessible
grate cell cluster (CyTOF), gene module (RNA-seq) and plasma prot- regions (DARs) of chromatin that defined the clusters and found 184
eomic data (Extended Data Fig. 7f and Methods). Of all factors, 1 and and 718 DAR in C5 and C7, respectively compared to other clusters
2 were most divergent between patient samples assigned as SRS1 (FDR < 0.05, fold change (FC) > 1.5) (Extended Data Fig. 8b,c and Supple-
compared to non-SRS1 (Extended Data Fig. 7g–k). The SRS1 direc- mentary Table 5). The chromatin profiles for C5 and C7 were enriched
tion in both factors was driven by immature Neu and progenitor Neu for publicly available myeloid progenitor cell chromatin profiles
cell abundance (including CD71hiCD38+Ki-67+ pro-Neu, CD71loKi-67+ (C5, HSC multipotential progenitor; C7, megakaryocyte progenitor)
pre-Neu and CD64+CD10loCD16loCD15lo immature Neu), together with (Extended Data Fig. 8d,e), suggesting their myelopoietic bias. CEBP
SRS1 upregulated gene modules and accounted for most variance in motifs were identified within the DARs in both C5 and C7 (Extended
the cell and gene module datasets, but not proteomics (Extended Data Data Fig. 8f,g), whereas STAT motifs were enriched in C5, but not C7
Fig. 7i). Factor 5 was most strongly related to differences in plasma pro- DARs (Extended Data Fig. 8f,g). To differentiate which transcription
tein abundance, but showed no difference across SRS (Extended Data factors governed the identities of clusters C5 and C7, we overlapped
Nature Immunology | Volume 24 | May 2023 | 767–779 773
Article https://doi.org/10.1038/s41590-023-01490-5
SPI1
MEIS1 STAT3 TEAD1
MAFK KDM4E BCL6
RFC3
POLR2A BATF
TAF1
MEF2A ZNF350 GRHL1 FOXB1
NFKB2 IL24 FOS
MAZ
Nature Immunology | Volume 24 | May 2023 | 767–779 774
SEN 0 20 40 60
***
10,000
1,000
100
10
1
)Lm/gp(
6-LI
*
100,000
10,000
1,000
100
)Lm/gp(
FSC-G
NS
10,000
1,000
100
10
1
)Lm/gp(
FSC-MG
100,000 NS SRS1
Non-SRS1
10,000
1,000
100
)Lm/gp(
FSC-M
S100A8/9hi Neu Immature IL1R2+ Neu
(program 8) (program 8) Cohort 3 (module 10)
CEBPB STAT3
RUNX1 CEBPB POLR2A NKX2−5 MZFZ1 CREB1 YOD1
STAT3 TBX21 MAFK TGIF1 CNOT4 CBFB BATF ELF5 NES
NR3C1 H1FX 6
ST T A FE T C 6 ZIC2 5 SPI1 NR3C1
AR EGR1 4
ZNF217 FOSL2 3 BCL6 RELB POU2F1 EP300 THRA ATF5 RARG ARID5B
SMAD4 MAFA SND1 JUND ANKZF1 GRHL1 HELT
SRY RAD21
SEN
a
SRS SRS1 Non-SRS1
Mature CD10+CD16+ Neu_program_8
IL1R2+ Neu_program_5
Mature CD10+CD16+ Neu_program_3
S100A8/9hi Neu_program_8
Degranulating CD66b+ Neu_program_9
IL1R2+ Neu_program_8
PADI4+ Neu_program_7
S100A8/9hi Neu_program_3
S100A8/9hi Neu_program_2
Mature CD10+CD16+ Neu_program_2
Degranulating CD66b+ Neu_program_8
Degranulating CD66b+ Neu_program_11
IL1R2+ Neu_program_3
PADI4+ Neu_program_8
Scaled expression −1 0 1
Correlation
−4 −2 0 2 4 with SRSq
b c
STAT3
POLR2A STAT6 HSF2 SOX15
CEBPB HNF1B ATF4 NES RARγ NES NES JUND
7 CEBPA 6 7
6 PP N A F R I G C 5 6 5 STAT5A 5
4 TBX21 4 4
3 M M Y E O F2 D A 1 3 3 NFATC3 MAFA AP3B1 SOX10
FOS ABCF2 IZKF2 ERM
EP300
0 102030
Targets
d
e f
2.0 × 107 *
1.5 × 107
1.0 × 107
5.0 × 106
SRS1 Non-SRS1
evitaler(
neerG
xototyC
)ytisnetni
ecnecseroulf
Mature CD10+CD16+ Neu
(program 3)
SEN 0102030
Targets
SEN 01020
Targets Targets
0 µm 200 0 µm 200
0.88 × 0.65 mm, 0.57 mm2 0 d 4 h 0m 0.88 × 0.65 mm, 0.57 mm2 0 d 4 h 0m
Fig. 5 | GEPs in SRS1 neutrophils and expression of plasma granulopoiesis and non-SRS1 patients with sepsis (n = 36, mmV cohort) (two-sided Wilcoxon
mediators. a, Heat map of Neu subset GEPs and correlation with SRSq rank-sum test). e,f, Representative live-cell imaging of Neu NETosis (e) and
(Spearman’s Rho on the right of the heat map, FDR < 0.05) in whole-blood relative fluorescence intensity (f) in CD66b+ Neu from whole blood of SRS1
samples from patients with sepsis (n = 26, scWB cohort). b, Transcription factor (n = 10) and non-SRS1 (n = 10) patient samples 4 h after stimulation with PMA and
prediction analysis (top 50 genes per program) for CD10+CD16+ Neu_program_3, incubation with DNA-bound Cytotox Green reagent. Green fluorescence denotes
S100A8/9hi Neu_program_8 and IL1R2+ Neu_program_8 that positively correlated cells undergoing NETosis. A total of 20 runs were performed (two-sided Wilcoxon
with SRSq, as in a. c, Transcription factor prediction analysis for bulk RNA-seq rank-sum test). Box plots denote minimum and maximum with whiskers and
module 10 in whole-blood samples from patients with sepsis (n = 36, mmV bottom quartile, median and upper quartile with the box. NES, normalized
cohort) using as input the top 1% genes showing correlation with module 10 enrichment score. *FDR < 0.05; *** FDR < 0.001.
eigengene. d, Expression of IL-6, G-CSF, GM-CSF and M-CSF in plasma from SRS1
Article https://doi.org/10.1038/s41590-023-01490-5
a c
200
150
100
50
CEBP S D T A C T R 3 EBBP HES2 LY C L E 1 BP M B E D E 12 P3 0 0 T A N L F 1 E2L2 BR D4 F J M LI J 1 D R 1 C U M N A X R 1 C B C A 1 C H2 ME D1 J U NPR ER G
S
f
Nature Immunology | Volume 24 | May 2023 | 767–779 775
)ytiralimis(
erocs
ELGGIG
e
0.5
0.4
0.3
0.2
0.1
0 25 50 75 100 Pseudotime
BPBEC
2.4
2.2
2.0
1.8
1.6
1.4
0 25 50 75 100
Pseudotime
3TATS
Pseudotime
UMAP1 25 50 75100
2PAMU
SRS1 Non-SRS1
4 C7
C6
0 C5
C4
−4 C3
C2
−8
−4 0 4 8
−4 0 4 8 −4 0 4 8 log FC
UMAP1
sretsulc
CSH
Non-SRS1 SRS1
2PAMU
UMAP1
Gene expression TF motif accessibility
chr3:GATA2 z:GATA2_388
chr6:SOX4 z:SOX4_754
chr6:MYB z:MYB_648
chr4:REST z:REST_168
chr19:RELB z:RELB_718
chr10:ZEB1 z:ZEB1_157
chr6:FOXO3 z:FOXO3_354
chr1:NFIA z:NFIA_742
chr20:CEBPB z:CEBPB_140
chr2:NFE2L2 z:NFE2L2_115
chr17:HOXB4 z:HOXB4_549
chr11:ETS1 z:ETS1_332
chr2:KLF7 z:KLF7_189
chr1:ATF3 z:ATF3_132
chr11:FOSL1 z:FOSL1_142
chr19:KLF2 z:KLF2_846
chr5:EGR1 z:EGR1_195
chr1:JUN z:JUN_143
chr2:FOSL2 z:FOSL2_105
chr17:HOXB3 z:HOXB3_447
chr19:JUNB z:JUNB_139
chr19:FOSB z:FOSB_121
chr2:STAT4 z:STAT4_775
chr22:MAFF z:MAFF_147
chr17:STAT3 z:STAT3_777
chr17:FOXK2 z:FOXK2_360
chr18:NFATC1 z:NFATC1_720
Pseudotime Pseudotime
−1.5 1.5 −1.5 1.5
2PAMU
b
z score
−2 −1 0 1 2
d
UMAP1
2PAMU
g
C5
STAT3 KO
C6
C7
STAT3 overexpression
Fig. 6 | Heightened STAT3-mediated EG in SRS1. a,b Differential HSC abundance of HSCs with supervised pseudotime trajectory from cluster C6 to cluster C5
between patients with sepsis assigned as SRS1 (n = 6) or non-SRS1 (n = 9) assessed showing STAT3 and CEBPB gene expression with pseudotime. f, Correlation
using density-based distribution UMAP visualization (a) and the corresponding of genes (left) and transcription factor (TF) motifs (right) along the C6–C5
beeswarm plots with sampled neighborhoods colored by statistically significant pseudotime trajectory (Pearson’s r > 0.5, FDR < 0.05). g, UMAP of in silico effects
enrichment (spatial FDR < 0.05) (b). c, chromVAR transcription factor motif of knockout (top) and overexpression (bottom) of STAT3 in clusters C5, C6 and C7
z score deviation for STAT3 in HSC from patients with sepsis (n = 15). d, ChIP-seq of HSCs from patients with sepsis (n = 15). Arrows display predicted changes in
overlap analysis for differentially open peaks in cluster C5 versus other clusters. cell fate after gene of interest is perturbed.
The GIGGLE score denotes a composite significance and effect size. e, UMAP
Article https://doi.org/10.1038/s41590-023-01490-5
Mature Neu S100A8/9hi Neu
Degranulating Neu IL1R2+ immature Neu
PADI4+ immature Neu MPO+ immature Neu/progenitors
Cycling Neu/progenitors
Mast cells/eosinophils
Platelets
HSPCs
Classical Mo
Non-classical Mo
cDCs
pDCs Plasmablasts B cells NK cells Cycling T/NK cells
Naive CD8+T cells CD8+T cells
Naive CD4+T cells
Memory CD4+T cells
UMAP1
DARs with public chromatin immunoprecipitation (ChIP)-seq datasets To identify transcription factors relevant to HSC clusters, we inte-
to match transcription factor occupancy profiles. Enrichment of bind- grated RNA and chromatin accessibility from the scHSPC data. We
ing profiles for both CEBPA and CEBPB was detected in C7 (Extended constructed supervised pseudotemporal trajectories from cluster C6
Data Fig. 8h), whereas only CEBPB was enriched in C5, indicating that (enriched in HCs) to C5 (enriched in SRS1) and C7 (enriched in sepsis,
C5 was more biased toward EG while C5, but not C7, exhibited overlap but not SRS1) (Fig. 6e and Extended Data Fig. 9a). STAT3 and CEBPB
with STAT3 binding profiles (Fig. 6c,d). expression increased along the C6–C5 trajectory (Fig. 6e), but not the
Nature Immunology | Volume 24 | May 2023 | 767–779 776
2PAMU
ARDS
Scaled expression
Scaled
expression
Scaled
expression
smargorp
3TATS
lihportueN
)noisserpxe
dezilamron(
seneg
)8P(
ueN
+2R1LI
seneg
)8P(
ueN
ih9/8A001S
)3P(
ueN
+61DC+01DC
erutaM
noisserpxe
dezilamron
noisserpxe
dezilamron
noisserpxe
dezilamron
seneg
a
e
ueN
+2R1LI
ueN
ih9/8A001S
ueN
+61DC+01DC
erutaM
seneg
8
margorp
seneg
8
margorp
seneg
3
margorp
SRS1 b
COVID-19 Influenza Non-SRS1
6
20 4
10 2
0 0
CAP FP
20 P < 2.2 × 10–16 40 P < 2.2 × 10–16 30 20 20
10 10
0 0
Pediatric septic shock
30
30
20
20
10 10
0 0
c d
1.5
6
4 1.0 4
2
2 0
0.5 −2
0 −4
0
1.5 1.5
1.0 1.0 4
2
0
0.5 0.5 −2
−4
0 0
1.5
1.0
2
1
0.5 0
−1
−2
0
)%(
ueN
+2R1LI
** ***
**** ****
**** ****
****
**** ****
****
)%( ueN
+2R1LI
)%(
ueN
+2R1LI
)%(
ueN
+2R1LI
)%( ueN
+2R1LI
)%(
ueN
+2R1LI
SRS1
Non-SRS1
SRS1
Non-SRS1
)%(
ueN
+2R1LI
P = 0.0016 P = 0.00052
P = 6.9 × 10–8 P = 7.7 × 10–5
SRS1
Non-SRS1
Fig. 7 | SRS1 signatures are consistent across differing clinical contexts of median and upper quartile with the box. d, Heat maps of expression of STAT3
infectious disease. a, Frequency of IL1R2+ Neu following whole-blood bulk GEPs (CD10+CD16+ Neu_program_3, S100A8/9hi Neu_program_8 and IL1R2+
transcriptomics (brWB-CID) deconvolution in patients with sepsis infected with Neu_program_8) in the corresponding Neu subsets from patients with ARDS
SARS-CoV-2 (n = 77), influenza (n = 109), CAP (n = 438), FP (n = 229), ARDS (n = 77) (n = 9) with violin plots on each side. Two-sided Wilcoxon rank-sum test
and pediatric septic shock (n = 106). Box plots denote minimum and maximum comparing SRS1 and non-SRS1 groups. e, Violin plots of expression of a combined
with whiskers and bottom quartile, median and upper quartile with the box. Two- set of GEPs involving STAT3 (CD10+CD16+ Neu_program_3, S100A8/9hi Neu_
sided Wilcoxon rank-sum test comparing SRS1 and non-SRS1 groups. b,c UMAP program_8 and IL1R2+ Neu_program_8) from scWB Neu subsets in pseudobulked
(b) and frequency of immature IL1R2+ Neu in samples assigned as SRS1 or non- Neu from patients with ARDS (n = 9) assigned as SRS1 or non-SRS1. Two-sided
SRS1 in adult ARDS patients (n = 9) (c) after reference mapping of scRNA-seq data Wilcoxon rank-sum test comparing SRS1 and non-SRS1 groups. *P < 0.05;
from whole blood to reference single-cell atlas derived from the scWB showing. **P < 0.01; ***P < 0.001; ****P < 0.0001.
Box plots denote minimum and maximum with whiskers and bottom quartile,
Article https://doi.org/10.1038/s41590-023-01490-5
C6–C7 trajectory (Extended Data Fig. 9b). We then identified transcrip- Discussion
tion factor genes and chromatin transcription factor motifs that both Here, we showed that Neu-granulopoietic disturbances in sepsis
changed along a trajectory and were correlated across modalities. involved expansion of specific populations of immature Neu, sup-
While the C6–C5 trajectory involved CEBPB and STAT3 (Fig. 6f), the pression of CD4+ T cells in co-culture and altered granulopoiesis, and
C6–C7 trajectory highlighted CEBPA (Extended Data Fig. 9c,d), demonstrated these features were enriched in a subset of patients
indicating the role of C7 and C5 in SSG and EG, respectively and that (SRS1). These results defined SRS1 as a specific immunocompromised
STAT3-driven EG was increased in the SRS1 subphenotype. disease endotype.
To validate the importance of CEBPB–STAT3 and CEBPA in Our fresh whole-blood single-cell multiomic atlas, with no cellu-
governing the identities of C5 and C7, respectively, transcription lar enrichments or depletions, ensured faithful recapitulation of the
factor-mediated gene regulatory networks were constructed with sepsis cellular landscape. Previous single-cell -omic profiling focused
CellOracle from RNA-seq and ATAC-seq HSC data for all HSC clus- on PBMCs, identifying an immature, bone-marrow-derived monocyte
ters. In silico knockout of CEBPA led to C7 loss of identity and transi- state (MS1), expanded in and predictive of sepsis8. The immature Neu
tion toward C6, whereas C5 cells were not affected (Extended Data populations defined here, in particular IL1R2+ Neu, exhibit similar gene
Fig. 9e), while in silico CEBPB knockout disrupted C5 cell differen- expression profiles to MS1 cells8. Direct comparison between MS1 and
tiation (Extended Data Fig. 9e). In silico overexpression of CEBPA or IL1R2+ Neu could potentially reveal similar myelopoietic processes
CEBPB reversed the directions of cell fate transitions in C5 and C7, leading to their generation. The extent to which mobilization of IL1R2+
respectively (Extended Data Fig. 9e), suggesting that C7 was a SSG Neu may occur elsewhere in systemic inflammation, such as reported
cluster and C5 was an EG cluster. In silico knockout or overexpres- in mice37 and whether IL1R2+ Neu and other Neu subsets may drive
sion of STAT3 had similar effects as CEBPB (Fig. 6g), suggesting that immune suppression in these contexts, remains unclear.
STAT3 was driving EG. An independent methodology, using scRNA While altered myelopoiesis in sepsis has been described in
splicing information and vector field analysis of HSCs C5, C6 and C7, mice38,39 and modeled in vitro40 here we presented evidence for
showed the same effects on EG and SSG reversal following in silico amplified granulopoiesis in humans during sepsis and specifically,
knockout of CEBPB, CEBPA and STAT3 (Extended Data Fig. 9f–j). These a dysregulated form of EG in the SRS1 endotype. Our data, together
observations established C7 as a CEBPA SSG HSC cluster and C5 as a with the reported increased risk of infections in patients with clonal
CEBPB–STAT3 EG cluster, with SRS1 enrichment of C5 highlighting EG hematopoiesis, including sepsis41, triangulate on the bone marrow
in SRS1. as foundational for the maladaptive response to infection, with the
caveat that our samples derive from circulating HSPCs rather than
Dysregulated granulopoiesis associates with SRS bone-marrow tissue.
across infections Going forward, it will be important to understand determinants
We next investigated whether cellular (for example, IL1R2+ Neu expan- of differential bone-marrow responses to infection and the mye-
sion) and molecular (for example, STAT3 GEP) properties of the SRS1 lopoietic legacy of severe infection, for example, through trained
patient subphenotype were seen across other severe infectious immunity42 or hematopoietic exhaustion43. Published reports sug-
disease contexts. We reanalyzed publicly available bulk transcrip- gest that previous exposures and inflammatory comorbidity may
tomics whole-blood cross-infectious disease (brWB-CID) datasets be important in influencing subsequent myelopoietic responses
for four contexts: infectious organism (SARS-CoV-2 (ref. 31), n = 77 to infection44. Meanwhile, our observations of persistent granulo-
and influenza34, n = 109); source of infection (community acquired cytic alterations in convalescence, both phenotypic and functional,
pneumonia (CAP), n = 438 and fecal peritonitis (FP), n = 229)17; clini- add to the evidence that infectious and inflammatory stimuli have
cal syndrome (ARDS35, n = 77); and age group (pediatric sepsis36, long-lasting myelopoietic and therefore innate immune ramifica-
n = 106). All samples were assigned to SRS1 or non-SRS1 based on tions42,45. CEBPB has a key role in induction of trained immunity in
the expression of the seven-gene set. Cell type and state deconvolu- HSCs46 and STAT3 drives specific immunosuppressive properties in
tion demonstrated expansion of IL1R2+ Neu (Fig. 7a) and, to a lesser MDSCs21. We found that STAT3-CEBPB-driven EG was pathognomonic
degree, expansion of cycling MK167+CYP1B1+ Neu (Extended Data of SRS1, with STAT3 underpinning the granulopoietic–granulocytic
Fig. 10a) in patient samples assigned as SRS1 compared to non-SRS1 axis, raising the hypothesis that SRS1 represents a state of maladap-
for all contexts. DGE testing showed enrichment of a combined set tive innate immune reprogramming and memory, with a potential
of all GEPs from scWB Neu subsets involving STAT3 (CD10+CD16+ opportunity for manipulating STAT3 activation to alleviate sepsis-
Neu_program_3, S100A8/9hi Neu_program_8 and IL1R2+ Neu_pro- and SRS1-associated immunosuppression. For example, G-CSF and
gram_8) (denoted ‘STAT3_combined_program’) in patient samples IL-6 show increased expression in SRS1, canonically signal through
assigned as SRS1 compared to non-SRS1 across all contexts (Extended STAT3 and are key contributors to EG47,48 with inhibition specifically
Data Fig. 10b). in patients with SRS1 or high SRSq subphenotypes a possible immu-
We also analyzed published whole-blood transcriptomic data- notherapeutic strategy1. This is further supported by Mendelian rand-
sets of patients with ARDS14 (n = 9) or COVID-19 (ref. 13) (n = 8) at a omization work, where lower IL-6R expression associated with reduced
single-cell resolution (scWB-CID) using scWB as a reference for cell mortality in sepsis49 and the therapeutic benefit of targeting IL-6 in
type and cell state annotation (Fig. 7b). IL1R2+ Neu were expanded in severe COVID-19 (ref. 50).
patients with SRS1 subphenotype compared to non-SRS1 (Fig. 7c and Limitations of our study include the extent that our single-cell-
Extended Data Fig. 10c). The STAT3 GEP (CD10+CD16+ Neu_program_3, analysis patient cohorts are fully representative of the breadth of the
S100A8/9hi Neu_program_8 and IL1R2+ Neu_program_8) showed enrich- sepsis syndrome. Further work is needed to understand the differential
ment in patient samples assigned as SRS1 compared to non-SRS1 in immunosuppressive properties and role of prostaglandins in Neu,
ARDS (Fig. 7d) and COVID-19 (Extended Data Fig. 10d). Total Neu, as altered granulopoiesis through study of patient bone marrow and
defined by the original authors13,14, showed higher expression of the experimental gene manipulation of transcription factors to verify in
STAT3_combined_program genes in patient samples assigned as SRS1 silico knockouts. Relevant animal model and experimental medicine
compared to non-SRS1 in ARDS (Fig. 7e) and COVID-19 (Extended Data studies to manipulate candidate therapeutic targets are needed to
Fig. 10e) providing cross-validation. These analyses indicated that better understand cytokine inhibition strategies.
the biological basis of the SRS patient subphenotype was independ- Collectively, our work identified a common innate immune and
ent of infectious organism, source of infection, clinical syndrome hematopoietic axis that contributes to the maladaptive immune
and age. response to infection during sepsis and specifically a poor outcome,
Nature Immunology | Volume 24 | May 2023 | 767–779 777
Article https://doi.org/10.1038/s41590-023-01490-5
immunocompromised, extreme response SRS1 patient endotype, 21. Veglia, F., Perego, M. & Gabrilovich, D. Myeloid-derived
advancing opportunities for personalized medicine. suppressor cells coming of age. Nat. Immunol. 19, 108–119 (2018).
22. Bayik, D. et al. Myeloid-derived suppressor cell subsets drive
Online content glioblastoma growth in a sex-specific manner. Cancer Discov. 10,
Any methods, additional references, Nature Portfolio reporting sum- 1210–1225 (2020).
maries, source data, extended data, supplementary information, 23. Alshetaiwi, H. et al. Defining the emergence of myeloid-derived
acknowledgements, peer review information; details of author contri- suppressor cells in breast cancer using single-cell
butions and competing interests; and statements of data and code avail- transcriptomics. Sci. Immunol. 5, eaay6017 (2020).
ability are available at https://doi.org/10.1038/s41590-023-01490-5. 24. Hao, Y. et al. Integrated analysis of multimodal single-cell data.
Cell 184, 3573–3587 (2021).
References 25. Granja, J. M. et al. Single-cell multiomic analysis identifies
1. Maslove, D. M. et al. Redefining critical illness. Nat. Med. 28, regulatory programs in mixed-phenotype acute leukemia.
1141–1148 (2022). Nat. Biotechnol. 37, 1458–1465 (2019).
2. van der Poll, T., Shankar-Hari, M. & Wiersinga, W. J. The 26. Hay, S. B., Ferchen, K., Chetal, K., Grimes, H. L. & Salomonis, N.
immunology of sepsis. Immunity 54, 2450–2464 (2021). The Human Cell Atlas bone marrow single-cell interactive web
3. Singer, M. et al. The third international consensus definitions for portal. Exp. Hematol. 68, 51–61 (2018).
sepsis and septic shock (Sepsis-3). JAMA 315, 801–810 (2016). 27. Hirai, H. et al. C/EBPβ is required for ‘emergency’ granulopoiesis.
4. Rudd, K. E. et al. Global, regional, and national sepsis incidence Nat. Immunol. 7, 732–739 (2006).
and mortality, 1990-2017: analysis for the Global Burden of 28. Manz, M. G. & Boettcher, S. Emergency granulopoiesis. Nat. Rev.
Disease Study. Lancet 395, 200–211 (2020). Immunol. 14, 302–314 (2014).
5. Davenport, E. E. et al. Genomic landscape of the individual host 29. Böiers, C. et al. Expression and role of FLT3 in regulation of the
response and outcomes in sepsis: a prospective cohort study. earliest stage of normal granulocyte-monocyte progenitor
Lancet Resp. Med. 4, 259–271 (2016). development. Blood 115, 5061–5068 (2010).
6. Scicluna, B. P. et al. Classification of patients with sepsis 30. Makishima, H. et al. Somatic SETBP1 mutations in myeloid
according to blood genomic endotype: a prospective cohort malignancies. Nat. Genet. 45, 942–946 (2013).
study. Lancet Resp. Med. 5, 816–826 (2017). 31. COMBAT Consortium. A blood atlas of COVID-19 defines hallmarks
7. Sweeney, T. E. et al. Unsupervised analysis of transcriptomics of disease severity and specificity. Cell 185, 916–938 (2022).
in bacterial sepsis across multiple datasets reveals three robust 32. Giladi, A. et al. Single-cell characterization of haematopoietic
clusters. Crit. Care Med. 46, 915–925 (2018). progenitors and their trajectories in homeostasis and perturbed
8. Reyes, M. et al. An immune-cell signature of bacterial sepsis. haematopoiesis. Nat. Cell Biol. 20, 836–846 (2018).
Nat. Med. 26, 333–340 (2020). 33. Demers, M. et al. Cancers predispose neutrophils to release
9. Qi, X. et al. Identification and characterization of neutrophil extracellular DNA traps that contribute to cancer-associated
heterogeneity in sepsis. Crit. Care 25, 50 (2021). thrombosis. Proc. Natl Acad. Sci. USA 109, 13076–13081 (2012).
10. Shen, X., Cao, K., Zhao, Y. & Du, J. Targeting neutrophils 34. Dunning, J. et al. Progression of whole-blood transcriptional
in sepsis: from mechanism to translation. Front. Pharm. 12, signatures from interferon-induced to neutrophil-associated
644270 (2021). patterns in severe influenza. Nat. Immunol. 19, 625–635 (2018).
11. Farkas, J. D. The complete blood count to diagnose septic shock. 35. Bos, L. D. J. et al. Understanding heterogeneity in biologic
J. Thorac. Dis. 12, S16–S21 (2020). phenotypes of acute respiratory distress syndrome by
12. Meghraoui-Kheddar, A. et al. Two new immature and leukocyte expression profiles. Am. J. Respir. Crit. Care Med. 200,
dysfunctional neutrophil cell subsets define a predictive 42–50 (2019).
signature of sepsis useable in clinical practice. Am. J. Respir. Crit. 36. Wong, H. R. et al. Identification of pediatric septic shock
Care Med. 205, 46–59 (2020). subclasses based on genome-wide expression profiling. BMC
13. Schulte-Schrepping, J. et al. Severe COVID-19 is marked by a Med. 7, 34 (2009).
dysregulated myeloid cell compartment. Cell 182, 1419–1440 (2020). 37. Martin, P. et al. Mouse neutrophils express the decoy type
14. Sinha, S. et al. Dexamethasone modulates immature neutrophils 2 interleukin-1 receptor (IL-1R2) constitutively and in acute
and interferon programming in severe COVID-19. Nat. Med. 28, inflammatory conditions. J. Leukoc. Biol. 94, 791–802 (2013).
201–211 (2022). 38. Weber, G. F. et al. Interleukin-3 amplifies acute inflammation
15. Uhel, F. et al. Early expansion of circulating granulocytic and is a potential therapeutic target in sepsis. Science 347,
myeloid-derived suppressor cells predicts development of 1260–1265 (2015).
nosocomial infections in patients with sepsis. Am. J. Respir. Crit. 39. Kwok, I. et al. Combinatorial single-cell analyses of
Care Med. 196, 315–327 (2017). granulocyte-monocyte progenitor heterogeneity reveals an early
16. Reddy, K. et al. Subphenotypes in critical care: translation into uni-potent neutrophil progenitor. Immunity 53, 303–318 (2020).
clinical practice. Lancet Resp. Med. 8, 631–643 (2020). 40. Reyes, M. et al. Plasma from patients with bacterial sepsis or
17. Cano-Gamez, E. et al. An immune dysfunction score for severe COVID-19 induces suppressive myeloid cell production
stratification of patients with acute infection based on whole- from hematopoietic progenitors in vitro. Sci. Transl. Med. 13,
blood gene expression. Sci. Transl. Med. 14, eabq4433 (2022). eabe9599 (2021).
18. Burnham, K. L. et al. Shared and distinct aspects of the sepsis 41. Zekavat, S. M. et al. Hematopoietic mosaic chromosomal
transcriptomic response to fecal peritonitis and pneumonia. Am. alterations increase the risk for diverse types of infection. Nat.
J. Respir. Crit. Care Med. 196, 328–339 (2017). Med. 27, 1012–1024 (2021).
19. Antcliffe, D. B. et al. Transcriptomic signatures in sepsis and a 42. Mitroulis, I. et al. Modulation of myelopoiesis progenitors is an
differential response to steroids. From the VANISH randomized integral component of trained immunity. Cell 172, 147–161 (2018).
trial. Am. J. Respir. Crit. Care Med. 199, 980–986 (2019). 43. Pietras, E. M. et al. Chronic interleukin-1 exposure drives
20. Cazalis, M. A. et al. Decreased HLA-DR antigen-associated haematopoietic stem cells towards precocious myeloid
invariant chain (CD74) mRNA expression predicts mortality after differentiation at the expense of self-renewal. Nat. Cell Biol. 18,
septic shock. Crit. Care 17, R287 (2013). 607–618 (2016).
Nature Immunology | Volume 24 | May 2023 | 767–779 778
Article https://doi.org/10.1038/s41590-023-01490-5
44. Li, X. et al. Maladaptive innate immune training of myelopoiesis 50. The REMAP-CAP Investigators. Interleukin-6 receptor antagonists
links inflammatory comorbidities. Cell 185, 1709–1727 (2022). in critically ill patients with COVID-19. N. Engl. J. Med. 384,
45. Naik, S. & Fuchs, E. Inflammatory memory and tissue adaptation 1491–1502 (2021).
in sickness and in health. Nature 607, 249–255 (2022).
46. de Laval, B. et al. C/EBPβ-dependent epigenetic memory induces Publisher’s note Springer Nature remains neutral with regard to
trained immunity in hematopoietic stem cells. Cell Stem Cell 26, jurisdictional claims in published maps and institutional affiliations.
793 (2020).
47. Zhang, H. et al. STAT3 controls myeloid progenitor growth during Springer Nature or its licensor (e.g. a society or other partner) holds
emergency granulopoiesis. Blood 116, 2462–2471 (2010). exclusive rights to this article under a publishing agreement with
48. Walker, F. et al. IL6/sIL6R complex contributes to emergency the author(s) or other rightsholder(s); author self-archiving of the
granulopoietic responses in G-CSF- and GM-CSF-deficient mice. accepted manuscript version of this article is solely governed by the
Blood 111, 3978–3985 (2008). terms of such publishing agreement and applicable law.
49. Hamilton, F. et al. Therapeutic potential of IL6R blockade for the
treatment of sepsis and sepsis-related death: findings from a © The Author(s), under exclusive licence to Springer Nature America,
Mendelian randomisation study. PLoS Med. 20, e1004174 (2023). Inc. 2023
Emergency Medicine Research Oxford (EMROx)
Alex Novak4, Melanie Darwent4, Tanya Baron4, Charlotte Brown4, Sally Beer4, Alexis Espinosa4, Tine Panduro4,
Dominique Georgiou4, Jose Martinez4, Hannah Thraves4, Elena Perez4, Rocio Fernandez4, Alberto Sobrino4, Veronica Sanchez4,
Rufino Magallano4, Karen Dineen4 & Jean Wilson4
Nature Immunology | Volume 24 | May 2023 | 767–779 779
Article https://doi.org/10.1038/s41590-023-01490-5
Methods Whole-blood single-cell RNA and cell surface protein profiling
Study ethics, patient cohorts and sample sets scRNA and cell surface protein sequencing was performed with the
scWB atlas. Volunteers self-reporting as healthy (HCs) and with no BD Rhapsody platform (633731/633733, whole transcriptome assay
history of infection in the past 14 d were recruited into the Genetic diver- (633801)) using 30 AbSeq antibodies (1 μl per antibody) (Supplemen-
sity and gene expression in white blood cells study following informed tary Table 2). Cells were stained following the manufacturer’s rec-
consent and under ethical approval (South Central Oxford REC B, ref- ommendations before single-cell capture targeting 6,000 cells per
erence 06/Q1605/55). Samples from patients with acute sepsis were sample. Reverse transcription, complementary DNA amplification and
collected from patients ≥18 years of age who were admitted to Oxford library construction (633801) were performed following the manufac-
University Hospitals NHS Foundation Trust, UK. Patients were recruited turer’s recommendations in six batches. Libraries were sequenced on
from the intensive care unit (ICU) if they had symptoms and signs of a NovaSeq6000 (Illumina).
established sepsis (suspected infection with an acute change in total
SOFA score ≥2 points)3 or from the emergency department and medical Whole-blood single-cell multiomic analysis
wards if they had a change in quick SOFA score by ≥2 points and a NEWS2 Analysis was performed with v.4.0.0 R and Python 3.8.6.
(ref. 51) score ≥7 or intensive care review requested. Exclusion crite-
ria were as previously reported in the UK Genomic Advances in Sep- Preprocessing and quality control. Gene expression data were aligned
sis (GAinS) study (NCT00121196)5: patients or consultees unwilling or using STARsolo53 (v.2.7.9a) (GRCh38) and spliced and unspliced counts
unable to give consent; advanced directive to withhold or withdraw were produced. Unfiltered files were used for cell calling (emptyDrops
life-sustaining treatment; admission for palliative care only; pregnancy function, DropletUtils (v.1.10.3)54) with a unique molecular identifier
and 6 weeks post-partum; or severe acquired immunodeficiency includ- (UMI) threshold of 100 and FDR of 0.5%. AbSeq reads were trimmed
ing systemic high-dose steroid therapy (prednisolone 0.5 mg kg−1 d−1 for with Trimmomatic (v.0.39) to the 12 bp UMI+ 36 bp AbSeq nucleotide
14 d or equivalent), HIV infection, known regular therapy with immuno- sequence and aligned to an artificial reference of the AbSeq nucleotide
suppressive agents such as azathioprine or neutrophil counts <1,000 ml−1 sequences using STARsolo.
due to any cause, including metastatic disease and hematological Cells expressing <100 or >4,000 genes, >10% mitochondrial reads,
malignancies or chemotherapy, but excluding severe sepsis and solid >2% hemoglobin reads or a log (UMI per gene) <0.6 were removed.
10
organ/bone-marrow transplant recipient receiving immunosuppressive Genes expressed in <10 cells or with a total count <3 were removed.
therapy. Convalescent sepsis samples were collected 1–6 months after Scrublet (v.0.2.3) and doublet detect (v.3.0) were both used on default
hospital discharge from individuals with acute sepsis samples already settings to remove doublets with automatic thresholds.
taken. Post-CS samples were collected from patients older than 18 years
of age who were admitted to Oxford University Hospitals NHS Founda- Normalization, dimensionality reduction and clustering. Data were
tion Trust, UK. Patients were eligible if they were (1) undergoing cardiac log normalized and 4,000 highly variable genes (HVGs) were identified
bypass surgery, (2) required postoperative ICU stay and (3) did not have using the Seurat vst algorithm (scanpy v.1.7.2).
an infection before surgery. Exclusion criteria were identical to those for Multimodal dimensionality reduction was performed with TotalVI
patients with sepsis. Patients with sepsis and CS were recruited into the (scvi-tools v.0.10.0)55 on default settings with all 30 proteins and HVGs
Sepsis Immunomics Study following informed consent and under ethical with each individual sample set as a batch (as all samples were pro-
approval (South Central Oxford REC C, reference:19/SC/0296) between cessed separately).
May and November 2021. Sepsis samples were collected on days 1, 3 or 5 Unsupervised clustering was performed on the 20 TotalVI latent
of hospital or ICU admission, whereas CS samples were collected 1 d after dimensions (Seurat FindNeighbors (k = 30) and FindClusters (smart
surgery. Written informed consent was obtained from adults or from local moving algorithm)). Clustering resolution was evaluated by
personal/nominated consultees for patients lacking capacity, with retro- cluster neighborhood purity, cluster average silhouette width and a
spective consent obtained from the patient once capacity was regained. 30-iteration bootstrap to determine cluster stability with respect to
sampling noise (bluster v.1.0). Additionally, we inspected top markers
scHSPC atlas. This included samples from 15 patients with sepsis per cluster to match with known biology and understand potential
and 7 age and sex-matched HCs recruited under the same studies as in value in merging versus splitting clusters. Combining these elements,
scWB and mmV (see below), with one and eight acute sepsis samples the default clustering resolution 0.8 was chosen, with one immature
overlapping with scWB and mmV, respectively and six acute sepsis sam- neutrophil cluster split into two (MPO+ immature neutrophils/pro-
ples not analyzed in either cohort. Eight convalescent sepsis samples genitors and PADI4+ immature neutrophils) based on resolution 1.1.
were included. Of the HCs, five were the same HCs as in mmV. HCs and
patients with sepsis were recruited into the same studies as described Cell annotation and RNA velocity/trajectory analysis. Cell clusters
under whole-blood single-cell atlas31. were merged for protein marker-based annotation of major known
immune cell types at a broad level and kept at the clustering resolu-
Bulk RNA-seq and single-cell RNA-seq WB cross-infectious disease tion of choice for fine annotation. Lineage assignment was confirmed
datasets (brWB-CID/scWB-CID). Publicly available data of infectious with SingleR (v.1.6.1) assignments. Fine annotation was conducted by
disease cohorts recruited with different clinical approaches were reana- inspecting biologically meaningful gene markers for T cell and neutro-
lyzed. Bulk transcriptomic data were obtained for adult sepsis based on phil populations (Supplementary Table 3).
microarray5,18 and bulk RNA-seq17, COVID-19 (ref. 31) (https://zenodo. RNA velocity and partition-based graph abstraction analysis of the
org/record/6120249#.YrLY_OzML0o), influenza34 (GSE111368), CAP neutrophils (without degranulating or apoptosing neutrophils) was
and FP (EGAD00001008730), ARDS35 (GSE65682) and pediatric septic performed with scVelo (v.0.2.3, default settings of stochastic model)56.
shock36 (GSE13904). Single-cell transcriptomic data were reanalyzed Moments were estimated using TotalVI reduced dimensions.
for ARDS52 and COVID-19 (ref. 13).
scRNA-seq pseudobulk unsupervised analysis (consensus clus-
Fresh whole-blood sample processing for single-cell sequencing tering, PCA, hierarchical clustering) and SRS assignment/scor-
Blood samples were drawn into EDTA tubes (BD Biosciences) and pro- ing. Gene expression was aggregated per individual for all cells and
cessed within 1 h of collection. Then, 1 ml whole blood was lysed with normalized (EdgeR trimmed mean of M-values; TMM). The top 10%
9 ml 1× eBioscience red blood cell lysis buffer (Thermo Fisher) twice most variable genes by mean absolute deviation were taken for unsu-
and 200,000 cells were transferred for antibody staining. pervised analysis.
Nature Immunology
Article https://doi.org/10.1038/s41590-023-01490-5
Consensus clustering was performed with the ConsensusClus- using EasySep HLA Chimerism Whole Blood CD66b positive selection
terPlus package (v.1.54.0) (ConsensusClusterPlus function, 1,000 kit (StemCell) following the manufacturer’s instructions.
repetitions, pItem = 0.95, pFeature = 0.1, inner/finallinkage = ward.D2
and distance = euclidean). Unsupervised hierarchical clustering was Phagocytosis assay. Neutrophils were incubated for 20 min in com-
performed with Ward’s linkage and Euclidean distance. plete medium with or without (fluorescence minus one) pHrodo Green
The relevant genes (DYRK2, CCNB1IP1, TDRD9, ZAP70, ARL14EP, E. Coli bioparticles (Invitrogen) (1 neutrophil:10 bioparticles). Cells
MDC1 and ADGRE3) were used for sepsis sample SRS assignment and were washed and stained for surface markers for 30 min with 7-AAD,
SRSq score calculation by SepstratifieR (v.0.0.0.9)57. CD66b-AF700 (G10F5) and Siglec-8-APC (7C9) antibodies from BioLeg-
end and acquired with a BD LSRFortessa X-20 analyzer. The phagocytosis
Differential abundance analysis. Cell type/state DA across conditions median fluorescence intensity for single 7-AAD−CD66b+Siglec-8− cells
was identified by sampling neighborhoods of cells from a k-nearest was determined by subtracting the median fluorescence intensity of
neighbors (k-NN) graph and looking for enrichment of either con- the fluorescence minus one control sample.
dition in each neighborhood as implemented in MiloR58. The 20
batch-corrected latent dimensions from TotalVI were used for MiloR Neutrophil-allogeneic CD4+ T cell co-culture. Cryopreserved CD4+
(v.0.99.19) k-NN graph construction (k = 30) and neighborhood index- T cells from healthy donor leukocyte cones were thawed and stained
ing (proportion = 0.1). DA testing was performed with generalized with 10 μM eBioscience Cell Proliferation Dye eFluor450 (Invitro-
linear models, including age and sex as covariates (neighborhoods gen) following the manufacturer’s recommendations. T cells were
significant if spatial corrected FDR < 0.05). co-cultured with CD66b+ neutrophils in 96-well U-bottom plates
(200,000 cells per well) at 37 °C 5% CO at a 4:1 neutrophil to T cell ratio
2
DGE analysis. For pseudobulk DGE, gene expression was aggregated in complete medium supplemented with 50 IU ml−1 recombinant human
per individual and per cell type/state into pseudobulks. Genes were IL-2 (BioLegend) and anti-CD3/CD28 Dynabeads (Gibco) added at a 1:1
filtered per pseudobulk based on minimum expression of n counts bead:T cell ratio. As controls, T cells were plated without neutrophils in
in at least X samples, where X was the smallest comparator group and every run, with and without anti-CD3/CD28 beads. To reverse T cell inhi-
n was defined for each pseudobulk based on histograms of logged bition, we tested co-cultures with 1 mM l-arginine (Sigma-Aldrich), 1 μM
count distributions. Pseudobulks were normalized by the EdgeR TMM arginase-1 inhibitor CB-1158 (Fisher Scientific), 10 ng ml−1 anti-CD274
method (v.3.30.3)59. DGE was performed with generalized linear models (eBioscience clone MIH1), 10 ng ml−1 anti-CD273 (PD-L2) (eBioscience
as implemented in EdgeR with age, sex and sequencing batch included clone MIH18), 20 μg ml−1 PGE (Sigma-Aldrich), 10 μM indomethacin
2
in the model. (Sigma-Aldrich), 15 μM EP inhibitor TG6-10-1 (MedChemExpress) or
2
Consensus DGE for acute sepsis versus HC IL1R2+ immature neu- 15 μM EP inhibitor GW-627368 (MedChemExpress).
4
trophils (as cells were too sparse to run pseudobulk DGE) and conva- After 72–96 h of co-culture, cells were stained for surface mark-
lescent versus HC total neutrophils was performed as described in ers followed by annexin V and 7-AAD to exclude dead/apoptosing
ref. 60. Genes were filtered for those that showed reproducible change cells. Samples were analyzed using the BD LSRFortessa X-20. All anti-
in the same direction in a minimum of six samples (smallest comparator bodies were purchased from BioLegend unless otherwise stated:
group size, HC = 6 samples). CD3-APC (UCHT1), CD4-BUV395 (BD Biosciences, SK3), CD66b-AF700
(G10F5), PD-1-PE (NAT105), CD69-PECy7 (FN50), 7-AAD, annexin V−
Consensus non-negative matrix factorization of neutrophil gene FITC. T cells were gated as singlet CD66b−CD4+CD3+annexin V−7-AAD−
expression. The 1,000 HVGs for each neutrophil state were selected cells. Proliferation analysis by dye dilution was established using the
(Seurat SelectIntegrationFeatures) followed by cNMF (v.1.2) as previ- non-bead-stimulated T cells cultured without neutrophils as the base-
ously described (100 factorizations)61 for 4–15 GEPs. The final GEP line proliferative fraction of cells in each sample. The proliferative
number per neutrophil state was chosen based on a tradeoff between fraction and percentage of cells expressing PD-1 and CD69 were calcu-
stability versus error as recommended by the original authors. Mean lated as a percentage relative to the anti-CD3/28 bead-stimulated, no
GEP usage per sample for each neutrophil state was correlated with co-culture T cells control to account for donor variation.
sample SRSq scores with FDR adjustment. The top 50 genes per GEP
were taken for downstream analysis. Flow cytometry data analysis. Flow cytometry data were analyzed
using FlowJo (v.10), GraphPad Prism (v.9) and R (v.4.0.0). The flow
Transcription factor prediction analysis. GEPs positively correlated cytometry gating strategy for neutrophil functional assays is described
with SRSq were used for TF prediction analysis with the Cytoscape in Supplementary Note 1.
(v.3.9.1) plugin iRegulon (v.1.3)62 (default settings). The same analysis
was performed for the top 1% genes correlating with module 10 eigen- NETosis assay. Neutrophils were plated at 20,000 cells per well (100 μl
gene from mmV cohort RNA-seq WGCNA (below). per well) in Ham’s F-12K medium (Gibco) using 96-well flat-bottom
plates coated with 0.01% poly-l-ornithine solution (Sigma). Then,
IL1R2+ neutrophil defining gene set. Genes specific to IL1R2+ neu- 250 nM IncuCyte Cytotox Green Dye was added to measure NETosis.
trophils were identified with Wilcoxon tests (Seurat FindMarkers) for Cells were treated with 100 nM PMA as per the manufacturer’s recom-
sepsis IL1R2+ neutrophils, filtering to only retain genes with adjusted mendations then imaged with the IncuCyte Live-Cell Analysis System
P value <0.01 and average logFC > 1. for up to 4 h.
2
Gene set and pathway enrichments. Gene sets for G-MDSCs22,23 were PBMC isolation and cryopreservation
scored in the scWB neutrophils (Seurat AddModuleScore). Pathway PBMCs were isolated from sepsis (acute and convalescent) and HC
analysis was performed against MSigDB Hallmark pathways and whole blood using density gradient centrifugation with Leucosep
prostaglandin-related pathways from the MsigDB C2 curated gene tubes (Greiner) and lymphoprep (StemCell) and cryopreserved in 10%
sets in ClusterProfiler (v.4.1.4)63. dimethylsulfoxide (Cell Signaling Technology).
Neutrophil functional assays CD34+ hematopoietic stem and progenitor cell enrichment
Isolation of neutrophils from whole blood. Neutrophils were isolated PBMCs from 15 patients with acute sepsis, 7 age and sex-matched HCs
from 5–10 ml whole blood from EDTA Vacutainer tubes (BD Biosciences) and 8 convalescent sepsis samples were used for CD34+ HSPC isolation.
Nature Immunology
