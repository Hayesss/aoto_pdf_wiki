---
source_path: /mnt/c/Users/Administrator/Zotero/storage/QQEUUZSI/Cerezo-Wallis 等 - 2025 - Architecture of the neutrophil compartment.pdf
ingested: 2026-04-23
sha256: 3df1f6896d8271f4
---

Article
Architecture of the neutrophil compartment
https://doi.org/10.1038/s41586-025-09807-0 Daniela Cerezo-Wallis1,2,29, Andrea Rubio-Ponce1,2,29, Mathis Richter3, Emanuele Pitino4,
Immanuel Kwok5, Giovanni Marteletto1, Ana Cristina Guanolema-Coba2, Changming Shih6,
Received: 16 August 2024
Run-Kai Huang6, Ana Moraga2,7, Natalia Borbaran Bravo8, Samuel Doré9, Sergio Callejas2,
Accepted: 24 October 2025 David G. Aragonés10, Daniel Jiménez-Carretero2, Daniel Martin2, Samuel Ovadia1,
Tommaso Vicanolo2, Georgiana Crainiciuc2, Jon Sicilia2, Tong Deng1, Anjelica Martin1,
Published online: xx xx xxxx
Jing Zhang11, Maria Isabel Cuartero2,12, Diego Moncada Giraldo13, Alicia Garcia-Culebras2,6,
Open access Alejandra Aroca-Crevillen2, Sandra Martín-Salamanca2, Carlos Torroja2, Max Ruiz4,
Irene Ruano4, Melissa S. F. Ng5, Jian Hou14, You Wang15,16, Ming Zhang17, Jun Pu18,
Check for updates
Ana Herruzo19, David Chang van Oordt20, Seokyoon Chang20, Alexander E. Downie20,
Fei Chen21, Andrea L. Graham20, William C. Gause21, Pierre O. Fiset22, Jonathan D. Spicer23,
Holger Heyn4,24, Maria A. Zuriaga2, Juan A. Bernal2, Irina A. Udalova25, Maria A. Moro2,
Katrien de Bock10, Ana Dopazo2, Jose J. Fuster2,26, Fátima Sánchez-Cabo2, Juan C. Nieto4,
Gabriel F. Calvo9, Julia Skokowa7, Oliver Soehnlein3, Daniela F. Quail8, Logan A. Walsh8,
Lai Guan Ng6,27,30 ✉, Andrés Hidalgo1,2,30 ✉ & Iván Ballesteros2,28,30 ✉
Neutrophils exhibit remarkable phenotypic and functional diversity across tissues
and diseases1,2, yet the lack of understanding of how this immune compartment is
globally organized challenges translation to the clinic. Here we performed single-cell
transcriptional profiling of neutrophils spanning 47 anatomical, physiological and
pathological scenarios to generate an integrated map of the global neutrophil
compartment in mice, which we refer to as NeuMap. NeuMap integrates and expands
existing models3,4 to generate fundamental new insights; it reveals that neutrophils
organize in a finite number of functional hubs that distribute sequentially during
maturation to then branch out into interferon-responsive an d im mu no s upp r essive
states, as well as a functionally silent state that dominates in the healthy circulation.
Computational modelling and timestamp analyses identify prototypical trajectories
that connect these hubs, and reveal that the dynamics and preferred paths vary during
health, inflammation and cancer. We show that TGFβ, IFNβ and GM-CSF push
neutrophils along the different trajectories, and projection of chromatin accessibility
sites onto NeuMap reveals that the transcription factor JUNB controls angiogenic and
immunosuppressive states and promotes tissue revascularization. The architecture
of NeuMap appears to be conserved across sex, environmental and genetic
backgrounds, as well as in humans. Finally, we show that NeuMap enables inference
of th e p ath ophysiological state of the host by profiling blood neutrophils. Our study
delineates the global architecture of the neutrophil compartment and establishes a
framework for exploration and exploitation of neutrophil biology.
Millions of neutrophils are produced every day by the bone marrow suggested active reprogramming of granulopoiesis by disease7,8. It is
through a well-defined series of differentiation steps before their release unlikely, however, that these profiles encompass the entire transcrip-
into the circulation as terminally differentiated, non-proliferative cells tional diversity of neutrophils, given the vast variety of microenviron-
that eventually infiltrate most tissues5,6. Work over the past decade has ments, infectious agents and malignant cells that inhabit or invade
unveiled substantial heterogeneity of neutrophils and delineated a mammalian tissues, their transcriptional plasticity, and the wealth of
vast array of transcriptional and phenotypic states, of which only a few functional states already identified across healthy and disease con-
have been assigned functional roles2. Paradoxically, the fundamental ditions2. Thus, fundamental questions remain about the following:
organization of the neutrophil compartment remains uncharacterized, (1) the actual number of possible transcriptional and functional states
a limitation that hinders their functional classification, knowledge of that neutrophils can acquire; (2) how these phenotypic states relate to
their physiological relevance, and clinical value. each other; (3) the specific stage(s) that are reprogrammed by disease;
Previous efforts to define the transcriptional organization of this and (4) the signalling and transcriptional programmes that instruct the
compartment has reported linear trajectories when profiling neutro- diversity of neutrophils in living tissues. We posited that understanding
phils from the bone marrow, spleen, blood and inflamed tissues, and the global architecture of the neutrophil compartment might provide
A list of affiliations appears at the end of the paper.
Nature | www.nature.com | 1
Article
insights into these unknowns and facilitate the conversion of this phe- states of neutrophils in health, inflammation, infection and cancer.
nomenal army of cells into therapeutic allies. These hubs included the following: (1) pre-neutrophil (PreNeu)-like
neutrophils10,13, defined by expression of mKi67 and Ltf, and oxidative
respiration14,15 (Supplementary Table 3); (2) an ‘immature hub’ undergo-
Transcriptional cartography of neutrophils
ing active maturation and granule synthesis that was positive for Mmp8
To generate a comprehensive transcriptional map of neutrophil and Cebpe, a regulator of granule synthesis10,16; (3) Cd52+ neutrophils
diversity in C57BL/6J mice, we conducted single-cell RNA sequencing that lacked a distinct transcriptional signature, had low mRNA content
(scRNA-seq) of lineage-negative (B220, CD3, CD19, NK1.1, Ter119) cells (Extended Data Fig. 2a), and were enriched in blood (immuno-silent
isolated from the bone marrow and CD11b+LY6G+ cells obtained from hub); (4) a conspicuous interferon-response signature (IFN-response
13 tissues of C57BL/6J mice housed in specific pathogen-free condi- hub) marked by expression of Ifit1 and Cd274, which featured signatures
tions at different developmental stages, sex, age and pathological of antiviral response (Fig. 1c) and was similar to the G5b state reported
perturbations (Fig. 1a, Extended Data Fig. 1a, Supplementary Fig. 1 in mice and humans during infection3 (Extended Data Fig. 1h); (5) and
and Supplementary Table 1). We used the BD Rhapsody platform9 and (6) hubs that shared signatures associated with immunosuppression
included blood from healthy adult male mice as an internal reference to and angiogenesis—one featured expression of Cd14 and Ptgs2 and was
assess integration quality and control for batch effects across datasets typical of lung and liver neutrophils1 (immunosuppression I hub (IS-I)),
(Methods). We then applied dimensionality reduction techniques to and the other expressed high levels of Vegfa and Cd274 and was promi-
visualize the transcriptional diversity of 129,829 neutrophils collected nent in tumoural neutrophils (immunosuppression II hub (IS-II)); and
across 47 biological conditions (Fig. 1a and Extended Data Fig. 1b). (7) a final hub (antigen (Ag) presentation hub) featuring increased
The resulting transcriptome embedding, which we refer to as a Neu- expression of genes associated with MHCII (H2 and Cd74), reminiscent
Map (Fig. 1a,b), enabled visualization of the transcriptional space of of neutrophils reported to mediate antigen presentation1,17,18, connected
the entire neutrophil compartment and revealed general properties the PreNeu and IS-I hubs (Fig. 1e), and is not explored further here.
by examining its topology. For example, granulopoiesis was identifi- Neutrophils from different tissues or pathophysiological conditions
able as a linear structure spanning genes associated with prolifera- were associated with the different functional hubs (Fig. 1f). For example,
tion, maturation and granule formation3,10 (Fig. 1c and Extended Data Cd14+Ptgs2+ IS-I neutrophils were abundant in the gut, liver and lungs,
Fig. 1c,d) that was enriched in neutrophils from the bone marrow and interferon-responsive neutrophils dominated in infected, inflamed
spleen (Fig. 1b and Extended Data Fig. 1e). The transcriptional map and ischaemic conditions irrespective of the tissue, and Cd274+ and
expanded and lost its linear topology as we incorporated neutrophils Vegfa+ IS-II neutrophils were prominent in tumours but were largely
from healthy peripheral tissues (blood, lung, liver and intestine) absent from healthy tissues (Fig. 1e,f and Extended Data Fig. 2f–h).
and a broad set of pathological conditions (Extended Data Fig. 1b). By analysing multiple other conditions, we found that the basic
Finally, this map converged in a defined end structure featuring pro- structure of NeuMap in defined hubs was conserved across relevant
grammes associated with hypoxia and cancer (Fig. 1c), without gen- biological variables, including sex, housing conditions and genetic
erating transcriptional areas that are separated from the main body strains (Balb/c), and in the presence of Tet2-associated clonal haemat-
of the map. NeuMap also revealed a separate path connecting the ini- opoiesis19, both at baseline and during atherosclerosis (Extended Data
tial and end states that was independent of the main granulopoietic Fig. 3a–e). Profiling of neutrophils from 10 human tissues, including
path and was abundant in the lungs and inflamed tissues (Fig. 1b and samples from healthy individuals, colorectal cancer and blood from a
Extended Data Fig. 1e). The integration of all neutrophils in a single, patient with systemic lupus (Supplementary Table 4 and Supplemen-
interconnected structure is consistent with the constant production tary Fig. 2), also revealed substantial conservation of the transcriptional
and maturation of neutrophils11 and suggests that most transcrip- structure of the neutrophil compartment in humans (Extended Data
tional programmes are accessible by neutrophils emanating from the Fig. 4a,b). We could identify six hubs (H1–H6; Extended Data Fig. 4c,d),
granulopoietic programme. each enriched in neutrophils from the different tissues and conditions
We found that the anatomical and pathophysiological context (Extended Data Fig. 4e). Notably, cross-species comparison revealed
(including age and sex) dictated the distribution of cells in different strong conservation between the six human and seven mouse hubs.
regions of NeuMap (Fig. 1b,d and Extended Data Fig. 1e–g). These dis- The main difference was that the human hub 6 combined features of
tributions were also consistent with those obtained by mapping neu- mouse IS-II and APC hubs and was enriched in human lung and tumour
trophils from existing datasets of healthy and tumour-bearing mice tissues (Extended Data Fig. 4f, g).
onto NeuMap3,4,12 (Extended Data Fig. 1h). Finally, this ‘cartographic’ In summary, NeuMap offers insights into the transcriptional struc-
inspection of NeuMap revealed that neutrophils from healthy individu- ture of the neutrophil compartment across multiple tissues and physi-
als were sufficiently diverse to build the general scaffold of NeuMap, ological conditions at single-cell resolution, enables the integration
whereas those from inflammatory or tumoural conditions extend of profiles and signatures from existing datasets, and uncovers a con-
from these homeostatic states rather than creating new programmes served and limited set of transcriptional states across different ana-
(Extended Data Fig. 1b). tomical sites, disease conditions, genetic backgrounds, microbiome
By scoring NeuMap cells against various gene signatures, we identi- statuses and species.
fied physiologically relevant regions within the NeuMap embedding
(Fig. 1c, Extended Data Fig. 2a and Supplementary Table 2), including
Molecular, functional and spatial profiling
the proliferative and granule-synthesis regions described above, dis-
tinct metabolic states (oxidative phosphorylation, hypoxia and glyco- We next explored the potential of this integrative map to uncover new
lysis), chemotactic and antimicrobial functions, antiviral responses biological properties of neutrophils. NeuMap indicated that most
and signatures associated with cancer, which overlapped with areas of neutrophils from the lungs, liver and intestine localized within the
predicted immunosuppression and angiogenesis (Fig. 1c and Extended Cd14+ Ptgs2+ IS-I hub, predicting immunosuppressive and angiogenic
Data Fig. 2a). functions in these organs (Fig. 1f, Extended Data Fig. 1e and Fig. 2a).
To define functional regions more precisely, we performed unbiased To validate this prediction, we isolated neutrophils from the lung and
clustering (Extended Data Fig. 2b–e) and optimal grouping of clusters compared their angiogenic and immunosuppressive properties with
and functional signatures. We identified seven distinct transcriptional neutrophils from the blood, bone marrow and spleen, which local-
regions, or hubs, distributed in NeuMap (Fig. 1e and Extended Data ized in different hubs (Fig. 1e). Using an in vivo Matrigel plug model,
Fig. 2f), which we interpreted as predictive of the main functional we found that co-injection of lung neutrophils potently induced
2 | Nature | www.nature.com
a b d
Placenta
Bone marrow
Young
scRNA-seq neutrophils Old
47 conditions Cancer (LLC, PDAC)
LPS Female and male
Embryo, adult, aged Brain
Health and disease Meninges
Spleen
Acute and chronic Stroke
Young
Old
LPS Gut
Cancer Young
Old
Mammary gland
Breast cancer Liver Lung
Young Embryo Lung cancer (LLC)
Old Young Fibrosis
LPS Old Flu
Biliary injury LPS Cancer (PDAC) e
Cancer
c Proliferation Granules OxPhos Hypoxia Chemotaxis Antibacterial
Programmed death Antiviral Tumour Immunosuppression Angiogenesis APC
Low High
f
neovascularization compared with neutrophils from the other tissues To gain insights into transcriptional regulators of the IS-I hub, we
(Fig. 2b). Similarly, co-incubation of lung neutrophils with activated performed single-cell assay for transposase-accessible chromatin
CD8+ OT-I T cells had the most potent suppressive activity in a cytotox- (ATAC) sequencing combined with RNA sequencing (Dogma-seq)20
icity assay against ovalbumin (OVA)-expressing B16 melanoma target of neutrophils from the same four tissues at steady-state or during
cells (Fig. 2c), together confirming the predicted functional properties conditions of inflammation and cancer. A genome-wide search for tran-
of neutrophils on the basis of their distribution in NeuMap. scription factor binding sites revealed that the IS-I hub was enriched in
Nature | www.nature.com | 3
2PAMU
Bone marrow Spleen
Blood Embryo Health
Lung Disease
Liver
UMAP1 Ltf+ mKi67+
PreNeu
Immunosuppression Proliferation, OxPhos
Angiogenesis
Cancer
Immunosuppresion
Angiogenesis
Lungs
Immuno-silent
Circulating
Immature
Granule synthesis
1.00
PreNeu
Immature
Immuno-silent
IFN-response
0.50
IS-I
IS-II
Ag presentation
noitcarf
lleC
MB dlO CADP CLL SPL segnineM 71E
doolB
71E
gnuL
sititaercnaP neelpS dlO SPL CADP doolB dlO tnangerP CADP SPL h
27
sitinotireP
reviL dlO SPL gnuL dlO SPL ulF CADP CLL sisorbiF atnecalP tuG dlO H2
sitinotireP
0
CDD CADP h
42
IM
h
27
IM
h
42
ekortS
CADP recnac
tsaerB
Heart
Peritoneum Myocardial
Pancreas Peritonitis infarction
Pancreatitis
PDAC
Blood
Young
Old
Pregnant
Cancer
LPS
Embryo
Cd274+ Vegfa +
Cd14+ Ptgs2+
H2+ Cd74+
Antigen
presentation
Cd52+
Cebpe+ Mmp8+
Ifit1+ Cd274+
IFN response
Infection, inflammation
Fig. 1 | NeuMap, an integrative map of the neutrophil transcriptome. compartmentalization of NeuMap. Each hub is defined by areas containing the
a, Scheme of the tissues and biological conditions used to generate NeuMap top 85% K-mass score. f, Stacked bars showing the proportion of cells from
using scRNA-seq. Further details in Supplementary Table 1. b, UMAP visualization different organs and conditions in each transcriptional hub. Please note that
by tissue of origin. c, Score value of gene sets for specific biological processes. not all 47 conditions are included in the panel. Tissues from healthy young male
Complete gene lists in Supplementary Table 2. APC, antigen-presenting cell; and female mice are labelled in red, and treatments or disease for each tissue
OxPhos, oxidative phosphorylation. d, UMAP visualization of neutrophils are indicated at the bottom of each bar.
extracted from health or diseased conditions. e, Scheme of the functional
Article
a b Flux variation vs c d
blood (%)
0 100 200 300
VascGF
IS
Hypoxia
Granules OxPhos
Proliferation
Ag present.
Antiviral
TAN Min Max
Mean flux e f
Day 0 Day 3 Day 10 Day 14 Day 18
0.6
0.4
0.2
0
0 5 10 15 20
Time after surgery (days)
Normalized
g expression h i
15 High
Naive LLC 0 Low
j k l m
motifs bound by the AP-1 complex, SMAD and NF-κB isoforms (Fig. 2d sites were accessible in most hubs of NeuMap (Extended Data Fig. 5a,b),
and Extended Data Fig. 5a, b), suggesting control of the angiogenic and suggesting broad control of neutrophil transcription by these factors.
immunosuppressive properties of lung neutrophils by these factors. To investigate the predicted role of AP-1 in regulating the properties of
By contrast, the immature and immuno-silent hubs were enriched in neutrophils in the IS-I hub, we generated mice with neutrophil-specific
motifs for members of the CEBP and KLF families, consistent with their deletion of Junb (MRP8cre; Junbfl/fl or JunbΔN mice), a component of the
roles in neutrophil maturation13,21. IRF- and STAT-related binding sites AP-1 complex. Bulk transcriptome analysis of lung neutrophils from
were largely restricted to the IFN-response hub, AP-1 and Bhlhe sites control versus JunbΔN mice revealed enrichment in genes associated with
dominated in IS-II neutrophils, and SMAD and AP-1 binding motifs in immunosuppression, angiogenesis and cancer, and this signature pro-
the antigen-presenting hub. Finally, CEBP, NF-κB and SMAD binding jected over the IS-I and IS-II hubs of NeuMap (Extended Data Fig. 5c), and
4 | Nature | www.nature.com
erocS
15 High
0 Low
erocS
Cluster ID
1
2
3
4
5
6 7
8
Healthy Tumour-bearing Flu infection Adjacent Intra-
Naive tumoral
)lortnoc/cimeahcsi(
oitar
IPDL
enilesab
detcartsbus
Junbfl/fl
Junbfl/fl JunbN
fl/flbnuJ
JunbN
NbnuJ
CXCR2hi
CD14low
CD11bhi IFIT1low Ly6G+
CD14+
MHC-IIhi PD-L1+
Ly6Chi
IFIT1+
PD-L1hi
CD14hi
Naive Flu IFIT1hi
2PAMU
UMAP1
Intravascular
Extravasc.
eviaN ruomuT
ulF
Min Max
100
80
60
40
20
0
)%(
noitroporp
retsulC
LY6G MHC-II CD14
CD11b IIFFIITT11 Vessel
DA TI artnI artxE
Junb
Merge Merge LY6G MHC-II CD14 Merge LY6G MHC-II CD14
PD-L1 PD-L1 CD11b IIFFIITT11 Vessel PD-L1 CD11b IIFFIITT11 Vessel

Junbfl/fl
Cd14 Ptgs2
Il1a
Gdf15
Trem1
Thbs1
Npr2 Adam8 Aqp1
Tnfaip2 Bmp4
N Nr4a1
Tnfaip3
noisserppusonummi
,sisenegoignA
Max
Min
–3 3
liN
8
6
4
2
0
)slexip
401×(
egarevoc
aerA
Angiogenesis,
immunosuppression Enrichment
P < 0.0001 High Motif FC
P = 0.568 P < 0.0001 JUN::JUNB 4.20
P = 0.0061 P = 0.028 FOSL2::JUN 4.18 Low
P = 0.754 FOSL1::JUN 4.17 FOSL2::JUND 4.16
FOS::JUN 4.14
P = 0.0136 FOS::JUND 4.07 PreNeu Immature
IS-I Immuno-silent JUN:JUNB All adjusted P < 0.05 IS-II IFN response
OTI + neutrophils Ag presentation
P = 0.0201 P = 0.0282
Fig. 2 | NeuMap illuminates molecular and functional properties of lung Right, heat map of differentially expressed genes (DEGs) (Supplementary
neutrophils. a, Heat map showing contribution of bone marrow, spleen, blood Table 6). f, K-mass projection of neutrophils from ischaemic hindlimbs and
and lung neutrophils to the top 5% of cells for the indicated functional gene kinetics of revascularization in control and JunbΔN mice. Data are mean ± s.e.m.
signatures. Cell number was downsampled to 1,000 per tissue. Ag present., Ag from n = 7–9 biologically independent mice per group. Two-way ANOVA
presentation; IS, immunosuppression; max, maximum; min, minimum; TAN, with Tukey correction. LDPI, laser doppler perfusion imaging. g,h, Spatial
tumour-associated neutrophils; VascGF, vascular growth factors. b, In vivo transcriptomics of immunosuppression scores (g) and interferon-response
Matrigel plug assay assessing angiogenic potential of neutrophils from indicated scores (h) in neutrophils from naive, LLC and flu-infected lungs. i, UMAP
tissues. Left, representative Doppler imaging; right, quantification. Data are clustering of lung neutrophils from tumour-bearing, flu-infected and
mean ± s.e.m. from n = 8 (lung) and n = 4 (spleens and bone marrow) biologically healthy mice by multiparametric staining. j–l, UMAP and representative
independent mice. Two-tailed t-test. c, OT-I T cell killing of B16OVA cells in the immunofluorescence of lung sections from naive mice (j), tumour-bearing
presence of tissue neutrophils. Dashed line, OT-I only; nil, untreated OT-I. Data mice (k) and flu-infected mice (l), showing cluster-defining markers. Data are
are mean ± s.e.m. from n = 6 control and 9 independent experiments. One-way from n = 3 biologically independent mice per condition (one section per
ANOVA with Dunnett’s multiple comparisons. d, Dogma-seq analysis mapping mouse). Scale bars: 50 µm (main image (top)); 20 µm (expanded view (middle
neutrophils onto NeuMap. Left, top transcription factor motifs that are enriched and bottom)). m, Distribution of neutrophil clusters from i in intratumoural (IT),
in the IS-I hub. Right, enrichment score for JUNB binding sites. e, Left, contour tumour-adjacent (AD), intravascular (intra) and extravascular (extra) tissue.
plots of control Junbfl/fl and JunbΔN lung neutrophils mapped onto NeuMap.
scRNA-seq analyses revealed altered distribution of lung and liver neu- lung sections under the same conditions of infection and cancer. We
trophils onto NeuMap, as predicted (Fig. 2e and Extended Data Fig. 5d). selected a panel of eight antibodies that were predicted to identify
These alterations, however, were partial, suggesting the contribution of neutrophils from the different hubs present in the lungs (Extended Data
other transcriptional regulators in the IS-I hub. These alterations were Fig. 6g, h) and performed unbiased clustering and uniform manifold
cell-intrinsic because transfer of bone marrow neutrophils to the lungs approximation and projection (UMAP) embedding to identify eight
of wild-type mice induced expression of genes involved in immunosup- patterns of neutrophils by protein content (clusters 1–8 in Fig. 2i–l).
pression and angiogenesis only in control, but not in JUNB-deficient Each phenotypic cluster identified neutrophils associated with differ-
neutrophils (Extended Data Fig. 5e). Of note, although JunbΔN neutro- ent perturbations and regions of the tissue (Fig. 2m and Extended Data
phils differentiated normally (Extended Data Fig. 5f), their capacity Fig. 6h,i). For example, cluster 1 lacked specific markers and was typical
to suppress T cell activity in vitro and to promote Matrigel vasculari- of neutrophils from naive lungs and non-affected tissue adjacent to
zation in vivo was lost (Extended Data Fig. 5g,h). Consistently, lungs tumours (Fig. 2j,k), MHCII+CD14+CD11bhi neutrophils (cluster 5) were
from JunbΔN mice showed reduced endothelial cell proliferation and intratumoural, and PD-L1+IFIT1+ neutrophils (clusters 6 and 7) were
numbers (Extended Data Fig. 5i,j) during young age or after irradiation1, abundant in flu-infected sites (Fig. 2k,l and Extended Data Fig. 6i,j).
and subcutaneous Lewis lung carcinoma (LLC) tumours in these mice Overall, these findings highlight the potential of NeuMap to integrate
recruited neutrophils with reduced expression of cancer-associated transcriptional, phenotypic, anatomical and functional profiles of
markers, including CD14, Sca1 and PD-L1 (Extended Data Fig. 5k,l). This neutrophils across tissue microenvironments and physiological states.
correlated with blunted endothelial cell proliferation and increased
T cell infiltration in the tumours, and reduction in tumour growth in
JunbΔN mice (Extended Data Fig. 5m–o), indicating that neutrophils also Transcriptional trajectories in NeuMap
require active JUNB signalling to acquire a pro-tumoural state (IS-II hub). To explore the transcriptional dynamics in NeuMap, we examined the
We used a model of hindlimb ischaemia to examine JUNB-dependent distribution of neutrophils from several tissues across the different
reprogramming of neutrophils during neovascularization in a different transcriptional hubs in conditions of health, cancer (PDAC) and acute
tissue. scRNA-seq of neutrophils from ischaemic limbs showed that inflammation (from lipopolysaccharide (LPS) injection) (Fig. 3a–c).
they distributed between the IS-I and IS-II hubs (Fig. 2f) and JunbΔN mice The distribution of the neutrophils in NeuMap varied for each condi-
showed impaired restoration of blood flow in the ischaemic limb com- tion; neutrophils from healthy mice distributed through the imma-
pared with littermate controls (Fig. 2f), together demonstrating that ture, immuno-silent, IS-I and IFN-response hubs (Fig. 3a). By contrast,
AP-1 regulates the regenerative properties of neutrophils across tissues. tumour-bearing mice had few neutrophils in the immuno-silent and
To further explore the idea that NeuMap classifies neutrophils by IFN-response hubs, and instead shifted towards the IS-I and IS-II hubs
functional state, rather than only by anatomical location, we profiled (Fig. 3b). Finally, most neutrophils from LPS-treated mice localized in
neutrophils from the same tissue subjected to different challenges. the IFN-response hub (Fig. 3c). Of note, the distribution of neutrophils
Indeed, whereas neutrophils from naive lungs localized mainly in the in NeuMap remained relatively constant for each tissue across all con-
IS-I hub, those from influenza virus (flu)-infected lungs shifted towards ditions (Extended Data Fig. 7a), suggesting that both tissue and physi-
the IFN-response and Ag presentation hubs, and those exposed to LLC ological state determine the transcriptional diversity of neutrophils.
tumours moved towards the IS-II hub (Extended Data Fig. 6a), indicat- We utilized RNA velocity analysis24 to infer the transcriptional tra-
ing that both tissue and physiological context shape the phenotype and jectories of neutrophils in NeuMap in conditions of health, cancer and
function of neutrophils. We then used spatial transcriptomics of lung inflammation. Whereas the transition vectors from the PreNeu to the
sections from naive, flu-infected and tumour-bearing mice to directly immature hub were present in all groups, the downstream trajectories
associate the distribution of neutrophils in different transcriptional hubs varied across conditions. Healthy mice favoured the transition from
with their microanatomical localization. We annotated cell types and the immature to the immuno-silent hub, tumour-bearing mice transi-
functional signatures in different regions of the lung samples (Extended tioned towards the IS-I and IS-II hubs, and inflamed mice transitioned
Data Fig. 6b–d) and identified the spots that contained neutrophils. towards the IFN-response hub (Fig. 3a–c). We validated these predicted
Using similarity scores for the IFN-response and IS-I hubs (Fig. 2g,h), we trajectories by genetic-tracing experiments using iLy6GtdTomato mice1 to
found a high immunosuppression signature in neutrophils from border label neutrophils with tdTomato in the marrow and tracking potential
tumour areas compared with those from the tumour core, adjacent tis- alterations in granulopoiesis and neutrophil fates in tissues1 (Extended
sue or naive lungs. By contrast, the interferon-response score was high Data Fig. 7b–d). Maturation paths were similar for the three condi-
in neutrophils around infected bronchioles but was almost undetect- tions in the bone marrow, but they followed separate trajectories in the
able in naive lungs (Fig. 2g,h and Extended Data Fig. 6c). Conversely, other tissues (Fig. 3d and Extended Data Fig. 7c). Notably, neutrophils
projection of the signature of the spatially identified neutrophils onto from LPS-treated mice activated an additional route of maturation
NeuMap revealed that neutrophils from tumours distributed in areas directed towards the IFN-response hub (maturation path II; Fig. 3e
that included the IS-I and IS-II hubs, whereas those from the flu-infected and Extended Data Fig. 7c). This trajectory was similar to the canoni-
lungs overlapped with the IFN-response hub (Fig. 2g,h). The association cal maturation path I (shown in Fig. 3e) but lacked activation of genes
between the IS-II hub and neutrophils in border areas of tumours may typically associated with homeostatic maturation (Cd101, Cxcr4, Sell
explain the aggressive nature of the invasive tumour front22, and we con- or Csf3r), whereas the expression of inflammatory genes (Icam1 and
firmed these spatial associations in a pancreatic ductal adenocarcinoma Cd274) was increased (Extended Data Fig. 7c), suggesting an accelerated
(PDAC) spatial dataset7 (Extended Data Fig. 6e). Notably, IFN-response, and activated type of granulopoiesis. Consistently, we found reduced
IS-I and IS-II neutrophil signatures could also be detected in the bor- frequency and intensity of CD101 expression and increased presence
der zone of infarcted areas of the myocardium (dataset from ref. 23; of PD-L1+ICAM1+ neutrophils in the bone marrow after LPS treatment
Extended Data Fig. 6e), suggesting that different stresses can elicit similar (Extended Data Fig. 7e), and accelerated transit of neutrophils across
responses in neutrophils. These analyses also revealed that neutrophils tissues in mice treated with LPS (Extended Data Fig. 7f).
from different hubs have distinct spatial associations with various types When comparing the trajectories in peripheral tissues, we noticed
of T cells, macrophages and fibroblasts (Extended Data Fig. 6f), provid- that tdTomato+ neutrophils from all conditions transited between the
ing insights into where these neutrophils are educated in the tissue and different transcriptional hubs defined in NeuMap (Fig. 1e) and began
their potential effect on other immune and non-immune cells. branching out into two separate trajectories by 36 h (Fig. 3d). How-
To examine the association of the hubs in NeuMap with protein ever, the preferred pathways differed between conditions; neutro-
expression and spatial distribution, we performed cyclic labelling of phils in healthy and tumour-bearing mice favoured the IFN-response
Nature | www.nature.com | 5
Article
a d e
Healthy Immunosuppresion
Cancer path path
iLy6gtdTomato mice 0 24 36 72 Time (h) B B h as lh p e 1 40I C c d am 27 1 4 C Ve c g l3 fa I P l1 tg b s2 N Fo r4 s a b 1T C r d e 1 m 4 1
Steady state
Immuno-silent
24 h 36 h 72 h path Granulopoiesis
C C d d 5 1 2 01 L S t 1 f 00a8
Cst3 Ly6g
Dusp6 Mmp8
Tmsb4x Cstb
b Cancer Selenop
Maturation path II
Maturation path I Isg20Zfp36Ly6e
Cancer Il1b Dusp1 Ifitm1 Ifit1 Irf7 Isg15
Nlrp3 Wfdc17Cxcl2 IFN response path
24 h 36 h 72 h 24h Ifit3 Ifit1 Slfn5
Oasl1Ly6eIsg15
f Steady state Cancer (PDAC) Inflammation (LPS)
c
Inflammation
Inflammation
24 h 36 h
hub by 72 h, whereas inflammation favoured their transition to GM-CSF and APRIL directed them to the IS-II hub, and IL-1β, IL-1α and
the immuno-silent hub. We confirmed this pattern in a model of TNF directed them to a region between the IS-I and IS-II hubs (Fig. 4a,b).
zymosan-induced peritonitis (Extended Data Fig. 7g). Notably, only We validated these observations by exposing bone marrow neutro-
neutrophils from tumour-bearing mice transited from the IS-I hub to phils to eight different cytokines or conditioned media from two cancer
the IS-II hub (Fig. 3d and Extended Data Fig. 7d). cell lines (LLC and FC1242). We profiled the cells using a custom panel of 21
We modelled these findings in a network of transcriptional transitions targeting markers associated with different areas of NeuMap (Fig. 4c) to
and hubs in NeuMap, and used pseudotime analysis to identify genes categorize neutrophils into 5 possible profiles (Fig. 4c and Extended Data
that were specifically activated in those transitions (Fig. 3e and Extended Fig. 8a–c). We found that TGFβ favoured maturation (CD101hiLY6Ghi);
Data Fig. 7h). We found, for example, that the canonical maturation pro- IFNβ induced an inflammatory-like phenotype (PD-L1hiCD14lowCX3CR1hi);
gramme (path I) involved the simultaneous activation of inflammatory, and GM-CSF induced a cancer-associated profile (CD101lowPD-L1hiCD14hi
anti-inflammatory and interferon-regulated genes (for example, Dusp1, dcTRAIL-R1hiMHC-II+). Finally, tumour-conditioned media induced
Nlrp3 and Ifitm1; Fig. 3e). This profile was consistent with this path split- phenotypes that resembled GM-CSF treatment but were milder and
ting into at least two trajectories, one leading to the immuno-silent hub more biased towards the immunosuppressive phenotype (Fig. 4c–e and
and the other leading to the IFN-response hub, suggesting that at this Extended Data Fig. 8a–d). Notably, we confirmed that these phenotypes
early stage, neutrophils activate broad genetic programmes without mirrored the predicted transcriptional states in NeuMap by scRNA-seq
committing to only one. Representation of the preferred trajectories of of the cultured bone marrow neutrophils and projection onto NeuMap
neutrophils onto NeuMap suggested that, although the global structure (Fig. 4f), suggesting that these cytokines drive the different transcrip-
of this network of trajectories is conserved, each condition has preferred tional trajectories identified in NeuMap (Fig. 3e).
transcriptional paths that are followed by neutrophils (Fig. 3f). Thus, To formally demonstrate this, we generated mice with neutrophil-
mapping of temporal series onto NeuMap infers transcriptional dynam- specific deficiency in receptors for TGFβ (TgfbrΔN mice), type I inter-
ics of neutrophils as they mature in the bone marrow and transition into feron (IfnarΔN) and GM-CSF (Csf2rΔN). In vitro treatment of bone marrow
peripheral tissues to acquire new properties. neutrophils from these mutant mice prevented the phenotypic changes
elicited by their respective cytokines, resulting in reduced maturation-,
inflammation- and cancer-associated phenotypes (Fig. 4g and Extended
Deterministic signalling drives NeuMap trajectories
Data Fig. 8e). We then performed scRNA-seq of neutrophils from the rel-
We sought to identify cues that controlled the transition of immature evant tissues of TgfbrΔN (bone marrow), IfnarΔN(blood) and Csfr2ΔN(LLC
neutrophils to the main hubs. We first took advantage of a dataset tumour) mice and their respective controls and mapped their distri-
containing the single-cell transcriptomes of lymph node leukocytes bution in NeuMap. Neutrophils from TgfbrΔN mice showed delayed
exposed to 86 different cytokines25 and performed in silico screening by maturation, loss of the IFN-response hub in IfnarΔN mice and a shift away
mapping the neutrophils from this dataset onto NeuMap (Fig. 4a). Most from the IS-II hub in Csf2rΔN mice (Fig. 4h and Extended Data Fig. 8f),
cytokines induced profiles associated with a single hub; for example, confirming that these cytokines reprogramme neutrophils to defined
interferons and IL-36 directed neutrophils to the IFN-response hub, transcriptional states in vivo.
6 | Nature | www.nature.com
2PAMU
TAM
Cell density Velocity
REL, CEPBA KLF5, REL, JUN
CEBPB
Cell density Velocity
STAT1, IRF1 SMAD3
STAT1
Cell density Velocity Cell density Min Max
72 h
UMAP1
Fig. 3 | Transcriptional trajectories in NeuMap. a–c, K-mass score (representing 72 h (blood, spleen and lung, orange-red scale) after tamoxifen-induced
cell density) of neutrophils from the bone marrow, blood, spleen, lungs and labelling of Ly6g-tdTomato cells. e, Network model highlighting the trajectories
livers of naive mice (a), tumour-bearing mice (PDAC tumours) (b) and LPS-treated identified in a–d, showing genes and transcription factors enriched for each
mice (c), projected onto NeuMap. RNA velocity analyses were performed for trajectory. Transcription factors were selected when identified by both
each of the conditions and the main developmental trajectories are highlighted EnrichR and chromatin accessibility analyses. Note that we did not find any
with red arrowheads. d, K-mass score of the mapped time-stamped neutrophils transcription factor enriched in the immuno-silent path. For a complete list see
from steady-state, inflammation (LPS) and tumour-bearing (LLC) mice onto Supplementary Table 7. f, Inference of preferred trajectories for neutrophils
NeuMAP. Neutrophils were tracked at 24 h (bone marrow, black dots), 36 h and from healthy, tumour-bearing and inflamed mice from the data in a–d.
a b
IL-1α , IL-1β TNF GM-CSF IL-36α
c
d e
f
g h
i
Nature | www.nature.com | 7
))4202(
.la
te
iuC( senikotyc
fo
gnineercs
ocilis
nI
Flow cytometry (21 markers)
Vehicle
IFNβ
GM-CSF G-CSF CXCL12
CM LLC
CM PDAC
23-61DC 5RCC 1acS 1MACI 1L-DP IICHM 41DC b11DC
TIK
54DC 47DC G6YL 601DC
1RLIARTcd
051DC 101DC 4RLT C6YL 44DC 511DC 1RC3XC
0 1
recnaC erutaM
Inflammation/infection
100 5500 0
TgfbrN IfnarN Csf2rN
Cre– TgfbrN IfnarN Csf2rN
+TGFβ Mature
+IFNβ Infl./Infec.
+GM-CSF Cancer
–0.5 0 0.5
Normalized cell
fraction
I-SI
Immature
Mature
Inflammation/infection
Immunosuppression
Cancer (IS-II)
DI
buH
ueNerP
erutammI
tnelis-onummI esnopser
NFI II-SI
noitatneserp
gA
2PAMU
Min
Max
Vehicle GCSF TGFβ IL-1β CXCL12
IFNβ CM LLC CM PDAC GM-CSF
TGFβ
UMAP1
TGFβ IFNβ GM-CSF
scRNA-seq
TGFβ
IFNβ
GM-CSF
Min Max
Cell density
Migration Bacterial killing Phagocytosis NET formation Immune suppression Angiogenesis
CXCL1
2
Vehicle 1 TGFβ
IFNβ
0 GM-CSF
–1
–2
Min Max
Cell percentage
(scaled by hub)
)elcihev
sv CF(gol
GM-CSF
4-1BBL
APRIL
IL-1β
IL-1α
TNF IL-36α
IL-15
IL-12
IFNκ
IL-18
TSLP
C5a
IL-10
FGFB
Decorin
ApN OSM
CT-1
BAFF
IL-Y G-CSF
TRAIL
Noggin IL-1β
IL-31 Resistin IL-17A
PBS
Persephin
IL-24
IL-27
IL-19
IL-20 GITRL
LTα1/β2
EGF
C3a
IFNε Immunosuppression
CD30L
IL-17B IL30
TWEAK
TGFβ Culture 24–48 h
IL-17F
IL-6
IL-23
IFNλ2
SCF
GDNF
VEGF
IL-4
IL-21 IL-1Ra
HGF
IL-17D
IL-7 PP << 00..00000011
IL-22
IL-33 PP << 00..00000011
TL1A PP << 00..00000011
NP
Leptin
IL-3
CD40L
IL-5
LTα2/β1
FasL
IL-11
CD27L
IL-9 TPO
Prolactin
IL-2 I F L L - T 1 3 3 L P = 0.0002 P = 0.0042 P = 0.0404
IL-17C P < 0.0001P < 0.0001
I I L L - - 1 3 7 6 E Ra P = P 0 = . 0 0 0 .0 7 2 8 35 P < 0.0001P < 0.0001 * LIGHT P < 0.0382
OX40L
RANKL L M IF -CSF P = 0.0013 P < 0.0001
IGF1 P = 0.04 P = 0.0054
IFNβ
IFNα1
IFNγ IL-34
2PAMU
IFNα, IFNβ,
IFNγ
UMAP1
Fig. 4 | Signals that drive neutrophil maturation along the different paths. morphologies (immature ringed versus multilobulated). Scale bars, 10 µm.
a, In silico screening of cytokine induction of transcriptional profiles25. Heat g, Heat map visualization of the proportion of bone marrow neutrophils
map shows lymph node-derived neutrophils treated in vivo with cytokines from TgfbrΔN, IfnarΔNand Csf2rΔN mutants and Cre− controls in the mature,
or PBS (arrowhead). Cells were classified into NeuMap hubs using Seurat inflammation/infection (infl./infect.) and cancer phenotypic clusters after
LabelTransfer; proportions are colour-coded by hub. b, Distribution of treatment with the indicated cytokines for 24 h, determined by flow cytometry.
transcriptomes from cytokine-treated neutrophils projected onto NeuMAP. Data are mean ± s.e.m. from n = 3 biologically independent mice per group.
c, Heat map of 21 markers in bone marrow-derived neutrophils (left) and UMAP One-way ANOVA followed by Dunnett’s multiple comparison test. h, Contour
projection (right) defining five states (immature, mature, inflammation/ plots showing distribution of neutrophils from indicated genotypes in NeuMAP;
infection, IS-I and IS-II). Data from n = 4 independent experiments. d, Contour shifts (arrowheads) are quantified in Extended Data Fig. 8f. i, Functional assays
plots of neutrophils from c after 24 h treatment with cytokines or conditioned of neutrophils treated with vehicle or cytokines, measuring migration (n = 3–4),
media from LLC (CM LLC) and PDAC (CM PDAC). e, Radar chart summarizing bacterial killing (n = 6–7), phagocytosis (n = 4), NET formation (n = 10–13),
neutrophil distributions from d. f, Scheme, haematoxylin and eosin (H&E) immunosuppression (n = 4–6) and angiogenesis (n = 7–8). Data are mean ± s.e.m.
staining and NeuMAP projection (K-mass) of bone marrow neutrophils cultured from n = 2 independent experiments. One-way ANOVA followed by Dunnett’s
with TGFβ, IFNβ or GM-CSF. Micrographs show representative nuclear multiple comparison test. FC, fold change.
Article
We then used multimodal profiling of chromatin accessibility and with distinct cell lineages (Extended Data Fig. 9e), together support-
gene expression at single-cell resolution20 to identify transcription fac- ing the transcriptional, phenotypic and functional conservation of
tors that are potentially involved in the induction of these programmes, the mouse and human neutrophil compartments (Extended Data
which we validated using the HOXB8 system with CRISPR-mediated Fig. 4).
deletion of selected transcription factors21 (Extended Data Fig. 8g,h). Finally, we investigated whether the precise distribution of blood
Deletion of Cebpb, Rfx2 and Runx1 impaired neutrophil maturation and neutrophils in NeuMap could help predict the pathophysiological state
subsequent cytokine-driven polarization. By contrast, Irf5 was required of the host. We performed scRNA-seq analysis of neutrophils from the
for the infection/inflammation profile, and Relb was required for the blood of mice exposed to 18 different conditions, including cancer,
acquisition of the cancer/immunosuppressive phenotype in response microbial infections (viral and bacterial), sterile inflammation and
to GM-CSF or PDAC-conditioned medium. Finally, Junb deletion had physiological states (pregnancy, embryos and old age) (Fig. 5f). We
broad effects on differentiation, including the IS-I/IS-II phenotype found that projecting these neutrophils onto the full NeuMap markedly
(Extended Data Fig. 8g,h), and this could be rescued by its enforced reduced their transcriptional overlap, as quantified using the Bhat-
expression in Junb−/− HOXB8 cells (Extended Data Fig. 8i–k). tacharyya index (Fig. 5g and Extended Data Fig. 10a,b). Thus, we used
We finally used this in vitro strategy to enrich for neutrophils in NeuMap as a scaffold to project the distributions of blood neutrophils
transcriptional states associated with different regions of NeuMap and generated ten ‘diagnostic regions’ to enhance the spatial resolution
and assess their core functional properties, including chemotaxis, and separability of the samples (Extended Data Fig. 10c). Using the over-
phagocytosis and neutrophil extracellular trap (NET) formation, as well lap of blood neutrophils over these ten regions (Extended Data Fig. 10d),
as bactericidal, immunosuppressive, or angiogenic activities (Fig. 4i measured by their Bhattacharyya indices, we generated distribution
and Supplementary Fig. 3a–f). TGFβ induced moderate migratory and ‘barcodes’ for each sample (Fig. 5h). Notably, these barcodes could
immunosuppressive activities. IFNβ, by contrast, impaired migration discriminate between young and old male mice, pregnant female mice,
but activated phagocytosis and NET formation, suggesting activation of atherosclerosis-prone Apoe−/− mice and those with early stages of cancer.
an antimicrobial programme. Finally, GM-CSF impaired migration and Similarly, we could discriminate between different types of tumours or
enhanced phagocytosis, but additionally activated immunosuppres- infections, as well as mice with active liver cholestasis versus those in
sive and angiogenic properties (Fig. 4i and Supplementary Fig. 3e,f), remission (Fig. 5h and Extended Data Fig. 10c). Thus, NeuMap captures
consistent with scenarios of tissue repair and cancer1,26,27. the transcriptional diversity of neutrophils with sufficient resolution
Thus, these data suggest that the transcriptional transitions and to enable inference of host physiology by assessing the distribution of
functional states (hubs) defined in NeuMap are elicited by defined blood neutrophils, a feature with considerable diagnostic potential.
signals and transcription factors.
Discussion
Conservation and predictive properties of NeuMap
NeuMap provides a transcriptional and functional map of the neutro-
We speculated that the rich transcriptional resolution of NeuMap could phil compartment across organs, developmental stages and pathophys-
be harnessed to visualize neutrophil states across species, pathophysi- iological conditions. It reveals that, despite the wealth of transcriptional
ological conditions and response to therapies. We first examined sig- states reported in the literature1–3,9,18,31,34, the neutrophil compartment is
natures associated with a favourable response to immunotherapy in a organized as a finite collection of transcriptional states—or hubs—that
mouse model of lung cancer27. Visualization of these signatures onto can be associated with recognizable biological properties and appears
NeuMap revealed altered trajectories and a shift from the IS-II hub to be conserved between mice and humans (Supplementary Fig. 4).
towards the IFN-response hub in the responding group (Fig. 5a). Further expansion and exploration of NeuMap should be a collective
We then explored whether the transcriptional hubs defined in Neu- effort for the field.
Map persisted across species and pathological states, as suggested by We highlight three salient features of our study. First, the transcrip-
our profiling of the human neutrophil compartment (Extended Data tome of the neutrophil compartment is organized as a single structure
Fig. 4). Projection of neutrophil signatures extracted from published without obvious branching or separated clusters, both in mice and
human datasets of infection, autoimmunity and cancer12,28–30 (Fig. 5b humans, possibly reflecting the short lifespan of neutrophils and the
and Extended Data Fig. 9a) onto the mouse NeuMap revealed that severe continuous replenishment of the entire compartment1,7. Second, Neu-
COVID-19 was associated with the PreNeu hub (Fig. 5b), in line with previ- Map reveals several functional hubs, mirroring the heterogeneity of
ous reports31. By contrast, active flu infection or systemic lupus localized neutrophil states reported in multiple studies1,3,7,9,18,33,34. The relatively
in the IFN-response hub, and neutrophils from lung tumours localized in small number of hubs, however, contrasts with the remarkable diver-
the IS-II hub (Fig. 5b and Extended Data Fig. 9a), in agreement with stud- sity of scenarios in which neutrophils have important roles. It aligns,
ies in humans28,32,33. Integration of neutrophil signatures from multiple however, with the observation that many of the populations reported
human and mouse cancer types revealed a preferential association with in different studies converge into similar signatures and functions, as
the IS-II, Ag-presenting and IFN-response hubs (Extended Data Fig. 9a–c). shown, for example, in the context of cancer1,7,12,26,35,36. Thus, NeuMap
Validating this finding, we found that exposure of human neutrophils can be used as a reference platform to uncover core properties of neu-
differentiated from CD34+ progenitors to IFNβ- and GM-CSF-elicited trophils across environments and diseases. Third, we emphasize the
responses that strongly mirrored those in mice (Extended Data Fig. 9d). transcriptional dynamism of the neutrophil compartment, as captured
We then examined human neutrophils in situ by high-resolution by NeuMap and validated in the timestamp analyses that illuminate
spatial transcriptomic analysis of 12 human lung specimens from trajectories connecting the different hubs. This suggests that inter-
healthy and lung adenocarcinoma samples (Fig. 5c). We identified fering with these trajectories may be more effective than targeting
five neutrophil transcriptomic profiles (clusters 1–5) that matched terminally differentiated neutrophils, a strategy that still dominates
with the various hubs in the mouse NeuMap (Fig. 5d). For example, the neutrophil-based therapies5.
healthy lung tissue was enriched in cluster 1 and cluster 2 neutrophils, Our study is limited by the relatively small number of pathophysi-
which associated with the IS-I and Ag-presenting hubs, respectively, ological conditions analysed. Perturbations associated with allergy,
reflecting the findings in mice (Fig. 1f). By contrast, tumoural regions autoimmunity, mucosal inflammation or diseases associated with old
were enriched in cluster 4 and cluster 5, which shared features with age32,37–40, as well as developmental processes remain uncharted in our
the IS-II and Ag-presenting hubs (Fig. 5c,d). Neighbourhood analyses NeuMap. It is also likely that additional cues not explored here (includ-
revealed differential associations of neutrophils from each cluster ing cytokines, chemokines, signalling lipids, metabolites or mechanical
8 | Nature | www.nature.com
a b
Healthy Severe COVID-19 Influenza Lupus Lung cancer
KP1.9 KP1.9 + anti-CD40 Low Hi
c d
e
f g h
Ag present.
Immuno-silent
PreNeu
Naive E17.5 IS-I
Apoe–/– HFD Influenza IFN-resp.
Apoe–/– S. aureus Immature
LPS Early LLC
PDAC Mid-LLC Ag present.
Peritonitis Late LLC Immuno-silent
Colitis 80 w.o. PreNeu
IS-I
Cholestasis C.albicans IFN-resp.
Post- Pregnant Immature
cholestasis
0 0.7 Bhattacharyya index
Nature | www.nature.com | 9
1R 2R 3R 4R 5R 6R 7R 8R 9R
01R
Healthy Adjacent Tumour
Hub
Neutrophils
Scaled AUCell
0 1
Cluster/Hub
B
Only blood Post-cholestasis
Cholestasis
18 physiological conditions PDAC
Influenza
Pregnant
80 w.o.
Naive
Early LLC
Apoe–/–
Full NeuMap C. albicans
Mid-LLC
Late LLC
LPS
Apoe–/– HFD
Peritonitis
Colitis
S. aureus
E17.5
Bhattacharyya index 0 1
2PAMU
Cluster ID
1
2
3
4
5
UMAP1
1/IS-I
2/Ag present.
3/PreNeu
4/IS-II
5/IS-II,
Ag present.
yhtlaeH tnecajdA ruomuT
Fraction 1 2 3 4 5
1.0
PreNeu
Immature
Immuno-silent
0.5 IFN-response
IS-I
IS-II
Ag present.
0
Gene score
–1 0 1
7,240 8,402 10,133 5,993
100
75
50
25
0
1 2 3 4 5
egatnecreP
2,514
AT2
B cells
Endothelial
Fibroblasts
Macrophages
Myofibroblasts
Neutrophils
Stromal
TAMs
Fig. 5 | Predictive potential of NeuMAP. a, K-mass score of neutrophils from bar plot showing relative abundance of each neutrophil state in healthy, adjacent
mouse lung cancer with or without with anti-CD40 immunotherapy27, mapped and tumour areas. Right, heat map showing mean score per hub for each human
onto NeuMAP. b, Signature scores from human neutrophils isolated from cluster gene set (scaled by signature). Kruskal–Wallis test,P < 0.001 for all hubs.
blood of healthy individuals or patients with severe COVID-19 (ref. 31, influenza e, Percentage of nearest neighbouring cells to neutrophils from different
A28 or systemic lupus29, or from lungs of patients with cancer12. c, Representative clusters or hubs. Numbers indicate cells scored per group. AT2, alveolar type 2
images from spatial transcriptomics of lung sections from patients with lung cell; TAM, tumour-associated macrophage. f, Overview of 18 physiological and
adenocarcinoma, with healthy tissue, adjacent tissue and tumour lesion from pathological conditions from which single-cell blood neutrophil transcriptomes
the same individual. Top, H&E-stained sections. Middle, spatial distribution of were obtained. 80 w.o., 80 weeks old. g, Top, UMAP analysis of blood neutrophils
neutrophil gene signature scores. Bottom, enlarged views of indicated regions from f, coloured by sample origin. Overlap across samples and NeuMap hubs
showing neutrophils from different clusters or hubs. Data are from n = 8 (defined in Fig. 1) measured by Bhattacharyya index. Bottom, projection of
patients, with 2 formalin-fixed paraffin-embedded (FFPE) tumour sections and blood neutrophil transcriptomes onto reference NeuMAP embedding; overlap
1 adjacent non-tumorous section per patient. Representative images are shown. is quantified in a correlation matrix. h, Bhattacharyya indices showing overlap
Scale bar: 200 µm (main image); 50 µm (expanded view). d, Left, UMAP of each sample with NeuMap regions (Extended Data Fig. 10C), represented as a
embedding of neutrophil transcriptomes from the spatial transcriptomic barcode for each condition in a hierarchical tree. Drawings in a–c,f were created
dataset across all regions, identifying transcriptional clusters shown in c. Middle, in BioRender. Cerezo Wallis, D. (2025) https://BioRender.com/pfm336w.
Article
cues) and other transcriptional regulators contribute to the specifica- 30. Espinet, E. et al. Aggressive PDACs show hypomethylation of repetitive elements and the
tion of neutrophils. Finally, our study highlights the collective nature execution of an intrinsic IFN program linked to a ductal cell of origin. Cancer Discov. 11,
638–659 (2021).
of the compartment and hints that some properties of the collective 31. Schulte-Schrepping, J. et al. Severe COVID-19 is marked by a dysregulated myeloid cell
differ from the sum of its individual components, a notion that may have compartment. Cell 182, 1419–1440.e23 (2020).
32. Bennett, L. et al. Interferon and granulopoiesis signatures in systemic lupus
a major impact on understanding its evolutionary logic and defining
erythematosus blood. J. Exp. Med. 197, 711–723 (2003).
how neutrophils contribute to health and disease. 33. Wang, L. et al. Single-cell RNA-seq analysis reveals BHLHE40-driven pro-tumour
neutrophils with hyperactivated glycolysis in pancreatic tumour microenvironment. Gut
72, 958–971 (2023).
Online content 34. Xue, R. et al. Liver tumour immune microenvironment subtypes and neutrophil
heterogeneity. Nature 612, 141–147 (2022).
Any methods, additional references, Nature Portfolio reporting summa- 35. Veglia, F. et al. Fatty acid transport protein 2 reprograms neutrophils in cancer. Nature
569, 73–78 (2019).
ries, source data, extended data, supplementary information, acknowl-
36. Fridlender, Z. G. et al. Polarization of Tumor-Associated Neutrophil Phenotype by TGF-β:
edgements, peer review information; details of author contributions “N1” versus “N2” TAN. Cancer Cell 16, 183–194 (2009).
and competing interests; and statements of data and code availability 37. Van Avondt, K. et al. Neutrophils in aging and aging-related pathologies. Immunol. Rev.
314, 357–375 (2023).
are available at https://doi.org/10.1038/s41586-025-09807-0.
38. Gupta, S. & Kaplan, M. J. The role of neutrophils and NETosis in autoimmune and renal
diseases. Nat. Rev. Nephrol. 12, 402–413 (2016).
39. Woytschak, J. et al. Type 2 interleukin-4 receptor signaling in neutrophils antagonizes
1. Ballesteros, I. et al. Co-option of neutrophil fates by tissue environments. Cell 183, their expansion and migration during infection and inflammation. Immunity 45, 172–184
1282–1297.e18 (2020). (2016).
2. Ng, L. G., Ostuni, R. & Hidalgo, A. Heterogeneity of neutrophils. Nat. Rev. Immunol. 19, 40. Özcan, A. & Boyman, O. Mechanisms regulating neutrophil responses in immunity,
255–265 (2019). allergy, and autoimmunity. Allergy 77, 3567–3583 (2022).
3. Xie, X. Single-cell transcriptome profiling reveals neutrophil heterogeneity in homeostasis
and infection. Nat. Immunol. 21, 1119–1133 (2020). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
4. Grieshaber-Bouyer, R. et al. The neutrotime transcriptional signature defines a single published maps and institutional affiliations.
continuum of neutrophils across biological compartments. Nat. Commun. 12, 2856
(2021). Open Access This article is licensed under a Creative Commons Attribution-
5. Aroca-crevillén, A., Vicanolo, T., Ovadia, S. & Hidalgo, A. Neutrophils in physiology and NonCommercial-NoDerivatives 4.0 International License, which permits any
pathology. Annu. Rev. Pathol. Mech. Dis. 19, 227–259 (2024). non-commercial use, sharing, distribution and reproduction in any medium or
6. Casanova-Acebes, M. et al. Neutrophils instruct homeostatic and pathological states in format, as long as you give appropriate credit to the original author(s) and the source, provide
naive tissues. J. Exp. Med. 215, 2778–2795 (2018). a link to the Creative Commons licence, and indicate if you modified the licensed material.
7. Ng, M. S. F. et al. Deterministic reprogramming of neutrophils within tumors. Science You do not have permission under this licence to share adapted material derived from this
383, eadf6493 (2024). article or parts of it. The images or other third party material in this article are included in the
8. Quail, D. F. et al. Neutrophil phenotypes and functions in cancer: a consensus statement. article’s Creative Commons licence, unless indicated otherwise in a credit line to the material.
J. Exp. Med. 219, 1–23 (2022). If material is not included in the article’s Creative Commons licence and your intended use is
9. Salcher, S. et al. High-resolution single-cell atlas reveals diversity and plasticity of tissue- not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
resident neutrophils in non-small cell lung cancer. Cancer Cell 40, 1503–1520.e8 (2022). permission directly from the copyright holder. To view a copy of this licence, visit http://
10. Kwok, I. et al. Combinatorial single-cell analyses of granulocyte-monocyte progenitor creativecommons.org/licenses/by-nc-nd/4.0/.
heterogeneity reveals an early uni-potent neutrophil progenitor. Immunity 53, 303–318.e5
(2020). © The Author(s) 2025
11. Hidalgo, A., Chilvers, E. R., Summers, C. & Koenderman, L. The neutrophil life cycle.
Trends Immunol. 40, 584–597 (2019).
1Vascular Biology and Therapeutics Program and Department of Immunobiology, Yale
12. Zilionis, R. et al. Single-cell transcriptomics of human and mouse lung cancers reveals
University, New Haven, CT, USA. 2Centro Nacional de Investigaciones Cardiovasculares Carlos
conserved myeloid populations across individuals and species. Immunity 50, 1317–1334.
e10 (2019). III, Madrid, Spain. 3Institute for Experimental Pathology (ExPat), Centre for Molecular Biology
13. Evrard, M. et al. Developmental analysis of bone marrow neutrophils reveals populations of Inflammation (ZMBE), University of Münster, Münster, Germany. 4Centre Nacional d’Anàlisi
specialized in expansion, trafficking, and effector functions. Immunity 48, 364–379.e8 Genòmica, Barcelona, Spain. 5Singapore Immunology Network (SIgN), Agency for Science,
(2018). Technology and Research (A*STAR), 8 A Biomedical Grove, Immunos, Singapore, Singapore.
14. Grassi, L. et al. Dynamics of transcription regulation in human bone marrow myeloid 6Shanghai Immune Therapy Institute, Shanghai Jiao Tong University School of Medicine
differentiation to mature blood neutrophils. Cell Rep. 24, 2784–2794 (2018). Affiliated Renji Hospital, Shanghai, China. 7Departamento de Biología Celular e Histología,
15. Morrison, T., Watts, E. R., Sadiku, P. & Walmsley, S. R. The emerging role for metabolism in Facultad de Medicina, Universidad Complutense de Madrid, Madrid, Spain. 8Department of
fueling neutrophilic inflammation. Immunol. Rev. 314, 427–441 (2023).
Oncology, Haematology, Clinical Immunology and Rheumatology, University Hospital,
16. Morosetti, R. et al. A novel, myeloid transcription factor, C/EBPε, is upregulated during
granulocytic, but not monocytic, differentiation. Blood 90, 2591–2600 (1997). Tübingen, Germany. 9Rosalind and Morris Goodman Cancer Institute, McGill University,
17. Singhal, S. et al. Origin and role of a subset of tumor-associated neutrophils with Montreal, Quebec, Canada. 10Department of Mathematics and MOLAB-Mathematical
antigen-presenting cell features in early-stage human lung cancer. Cancer Cell 30, Oncology Laboratory, Universidad de Castilla-La Mancha, Ciudad Real, Spain. 11Department
120–135 (2016). of Health Sciences and Technology, Laboratory of Exercise and Health, ETH Zürich, Zurich,
18. Wu, Y. et al. Neutrophil profiling illuminates anti-tumor antigen-presenting potency. Cell Switzerland. 12Unidad de Investigación Neurovascular, Departamento de Farmacología y
187, 1422–1439.e24 (2024). Toxicología, Facultad de Medicina, Universidad Complutense and Instituto de Investigación
19. Fuster, J. J. et al. Clonal hematopoiesis associated with TET2 deficiency accelerates Hospital 12 de Octubre, Madrid, Spain. 13Department of Pediatrics, Emory University School of
atherosclerosis development in mice. Science 355, 842–847 (2017).
Medicine, Atlanta, GA, USA. 14Department of Hematology, Renji Hospital, Shanghai Jiao Tong
20. Mimitou, E. P. et al. Scalable, multimodal profiling of chromatin accessibility, gene
expression and protein levels in single cells. Nat. Biotechnol. 39, 1246–1258 (2021). University School of Medicine, Shanghai, China. 15Department of Obstetrics and Gynecology,
21. Khoyratty, T. E. et al. Distinct transcription factor networks control neutrophil-driven Renji Hospital, School of Medicine, Shanghai Jiao Tong University, Shanghai, China.
inflammation. Nat. Immunol. 22, 1093–1106 (2021). 16Shanghai Key Laboratory of Gynecologic Oncology, Renji Hospital, School of Medicine,
22. Horrée, N., van Diest, P. J., Sie-Go, D. M. D. S. & Heintz, A. P. M. The invasive front in Shanghai Jiao Tong University, Shanghai, China. 17Department of Urology, Renji Hospital,
endometrial carcinoma: higher proliferation and associated derailment of cell cycle School of Medicine, Shanghai Jiao Tong University, Shanghai, China. 18State Key Laboratory
regulators. Hum. Pathol. 38, 1232–1238 (2007). for Systems Medicine for Cancer, Division of Cardiology, Shanghai Cancer Institute, Renji
23. Yamada, S. et al. Spatiotemporal transcriptome analysis reveals critical roles for Hospital, School of Medicine, Shanghai Jiao Tong University, Shanghai, China. 19Media and
mechano-sensing genes at the border zone in remodeling after myocardial infarction.
Immersive Experience Center, The Design School, Arizona State University, Arizona State
Nat. Cardiovasc. Res. 1, 1072–1083 (2022).
24. La Manno, G. et al. RNA velocity of single cells. Nature 560, 494–498 (2018). University, Temple, AZ, USA. 20Ecology and Evolutionary Biology, Princeton University,
25. Cui, A. et al. Dictionary of immune responses to cytokines at single-cell resolution. Nature Princeton, NJ, USA. 21Department of Medicine, Center for Immunity and Inflammation, New
625, 377–384 (2024). Jersey Medical School, Rutgers, The State University of New Jersey, Newark, NJ, USA.
26. Veglia, F. et al. Analysis of classical neutrophils and polymorphonuclear myeloid-derived 22Department of Pathology, McGill University, Montreal, Quebec, Canada. 23Department of
suppressor cells in cancer patients and tumor-bearing mice. J. Exp. Med. 218, e20201803 Surgery, McGill University Health Center, Montreal, Quebec, Canada. 24Universitat de
(2021). Barcelona (UB), Barcelona, Spain. 25Kennedy Institute of Rheumatology, University of Oxford,
27. Gungabeesoon, J. et al. A neutrophil response linked to tumor control in immunotherapy. Oxford, UK. 26CIBER en Enfermedades Cardiovasculares (CIBER-CV), Madrid, Spain. 27School
Cell 186, 1448–1464.e20 (2023).
of Medicine, Westlake University, Hangzhou, China. 28Department of Neuroscience and
28. Zhang, Y. et al. A single-cell atlas of the peripheral immune response in patients with
influenza A virus infection. iScience 26, 108507 (2023). Biomedical Sciences, Universidad Carlos III de Madrid, Madrid, Spain. 29These authors
29. Wither, J. E. et al. Identification of a neutrophil-related gene expression signature that is contributed equally: Daniela Cerezo-Wallis, Andrea Rubio-Ponce. 30These authors jointly
enriched in adult systemic lupus erythematosus patients with active nephritis: clinical/ supervised this work: Lai Guan Ng, Andrés Hidalgo, Iván Ballesteros. ✉e-mail: nglaiguan@
pathologic associations and etiologic mechanisms. PLoS ONE 13, e0196117 (2018). renji.com; andres.hidalgo@yale.edu; ivballes@salud.uc3m.es
10 | Nature | www.nature.com
Methods for 3 weeks before sample collection, housed with a 12 h:12 h light:dark
cycle, and permitted ad libitum consumption of water as described46.
Mice An additional group of mice was fed a 0.1% DDC-supplemented diet
All experiments were performed on 6-to-24-week-old C57BL/6 male for three weeks and afterward allowed to recover for three days
and female mice. Young mice were defined as 8 to 12 weeks old, and old under standard mouse diet to study the reversibility of the cholestatic
mice were defined as 22 to 24 months old at the time of analysis. Mice phenotype.
were maintained under specific pathogen-free conditions with chow
and water provided ad libitum. mouse lines used were on the C57B1/6 J Influenza A infection. A stock of the virus strain A/PR8/34 (H1N1) was
background and housed under specific pathogen-free conditions at the diluted, and 100 plaque-forming units were administered intranasally
Centro Nacional de Investigaciones Cardiovasculares Carlos III, Singa- to isoflurane-anaesthetized 8-to-12-week-old male mice in 50 µl of
pore Immunology Network or Yale University. All mouse husbandry PBS. Mouse weight was monitored daily after infection and mice that
and experimentation was conducted using protocols approved by local presented weight loss of more than 20% of their initial body weight
animal ethics committees and authorities. Mice (Mus musculus) were were euthanized and considered deceased. For transcriptomic studies,
maintained in racks with individual ventilation cages according to cur- blood and lungs were collected on day 4 after infection.
rent Spanish, Singapore and US legislation (RD 53/2013 and EU Directive
63/2010, respectively). Mice have access to dust- and pathogen-free Pancreatitis. Acute pancreatitis was induced by intraperitoneal injec-
bedding, as well as sufficient nesting and environmental enrichment tions of 50 µg kg−1 of cerulein (Sigma-Aldrich), every hour, for a total of
materials, to facilitate nesting. All mice were kept in environmental con- 7 administrations. Mice were euthanized 24 h after the first injection.
ditions of 45–65% of relative humidity, temperature of 21–24 °C, and a
light:dark cycle of 12 h:12 h. Mice with neutrophil-specific deficiency in Orthotopic pancreatic tumour model. Mice were anaesthetized with
Tgfbr2 (TgfbrΔN) were generated by crossing MRP8CRE mice with Tgfbr2fl/fl ketamine/xylazine, and had their abdomen shaved and swabbed with
mice41. Similarly, we generated neutrophil-specific mutants by crossing antiseptic. A 5 mm vertical incision was made in the skin and abdominal
Junb-floxed42, Csf2r-floxed43 and Ifnar1-floxed mice44 with the MRP8CRE layer at a point 1 cm down from the xiphoid process of the sternum, and
driver. Apoe–/– mice (B6.129P2-Apoetm1Unc; Taconic M&B). Ly6gcreERT2 1 cm to the right of the midline. The pancreas was exposed, 105 FC1242
mice were crossed with Rosa26Tdtomato mice as in ref. 1, resulting in the cells were resuspended in phosphate-buffered saline (PBS) and mixed
iLy6gtdTom mice used in our fate mapping experiments. Gavage admin- with Matrigel (BD) in a 1:1 ratio and were injected as a volume of 50 µl
istration of tamoxifen (2 mg per mouse) was performed to induce CRE into the body of the pancreas to form a visible bolus using a 30G insulin
recombinase activity in 6-to-12-week-old male iLy6gtdTom mice. JAXBoy needle. The pancreas was then returned to the abdominal cavity. The
(PtprcK302E) from Jackson laboratories and Tet2−/− mice19 were used for abdominal layer was closed with absorbable 5/0 sutures, while the
adoptive bone marrow cell transfer. Eight-week-old male Germ-free mice skin was closed with non-absorbable 5/0 sutures. Superglue was ap-
(C57Bl/6) were kindly provided by the laboratory of N. Palm. In brief, plied over the sutures to ensure that they did not come undone after
Germ-free C57BL/6 mice were bred and maintained under sterile condi- surgery. Mice were resuscitated with saline and were subcutaneously
tions in flexible film isolators (Class Biologically Clean) in the Palm labora- administered Buprenorphine (10 mg kg−1) and Enrofloxacin (Baytril,
tory Gnotobiotic Facility at Yale School of Medicine. Mice were housed in 1.5 mg kg−1) for the 2 days following surgery. Mice were euthanized at
a temperature- and humidity-controlled room under a dark:light cycle week 5 following surgery and tissues were collected for transcriptomic
of 12 h:12 h. All animal protocols were approved by the Yale University analysis.
Institutional Animal Care and Use Committee (protocol 11513).
For the rewilding experiments, litters of mice were generated from Orthotopic breast tumour model. Mice were implanted orthotopically
multiple breeding pairs and randomly assigned to either remain in with 5 × 105 E0771 breast cancer cells in 50 µl Matrigel into the thoracic
the institutional vivarium (laboratory mice) or be released into the mammary gland of C57BL6/J mice. Additionally, the same procedure
outdoor enclosures (rewilded mice) to control for the microbiota was followed using the BALB/c-derived 4T1 breast tumour cell cancer
at the onset of the experiment. Outdoor enclosures were previously in BALB/c mice. Mice were euthanized at week 4 after implantation and
described45 and the protocols for releasing laboratory mice into the tumours were collected for transcriptomic analysis.
outdoor enclosure facility and then returning them to vivaria were
approved by Princeton University (protocol 1982) and Rutgers Uni- Orthotopic lung cancer model. We administered 2 × 105 LLC cells in
versity (protocol PROTO999900794). All protocols were approved 100 µl PBS intravenously into the lateral tail vein of 8-week-old C57BL6/J
by the corresponding local authorities of Madrid, Singapore, Rutgers, mice. Mice were euthanized at week 1, 2 or 3 after the implantation and
Princeton and Yale University. bloods and lungs were used for transcriptomics analysis.
Mouse models of disease Subcutaneous lung cancer model. Mouse LLC1 implants were gen-
Stroke. Thrombotic occlusion of the middle cerebral artery was erated in 8-week-old C57BL/6 mice by subcutaneous implantation of
induced by the ferric chloride (FeCl) stroke model. In brief, mice 0.5 × 106 cells (1 injection site per mouse). Tumour growth was followed
3
were anaesthetized and maintained at 2% sevoflurane in a mixture of every 2 days by measuring the 2 orthogonal external diameters using
0.2 l min−1 O:0.8 l min−1 air and temperature was kept at 36.5–37 °C us- a calliper. Tumour volume was calculated as V = π/6 × L × W × H, where
2
ing a heating blanket. The scalp was opened, and the middle cerebral L, W and H represent length, width, and height, respectively. Tumours
artery was visualized with a stereomicroscope (PZMIV, World Precision were excised and processed for flow cytometry analysis when they
Instruments). A piece of Whatman filter paper strip soaked in freshly reached 0.5 cm3.
prepared FeCl (20%) was placed over the intact dura mater on the artery
3
for 10 min and then removed to allow the formation of a thrombus. Caecal ligation and puncture-induced sepsis. Caecal ligation and
Following surgery, individual mice were returned to their cages with puncture were performed as described47. In brief, the peritoneal cav-
free access to water and food. Brains were collected 24 h after surgery ity of ketamine/xylazine-anaesthetized mice was exposed with a small
to perform transcriptomics analysis. incision and the caecum was exteriorized. 80% of the caecum distal
to the ileo-caecal valve was ligated using non-absorbable 7-0 suture.
Liver cholestasis. For the liver injury model, mice were fed a 0.1% of A 23G needle was then used to puncture both walls of the distal end
3,5-diethoxycarbonyl-1,4-dihydrocollidine (DDC)-supplemented diet of the caecum, and a small drop of faeces was extruded through the
Article
perforation. The ligated and punctured caecum was relocated inside haematopoiesis, we performed an adoptive bone marrow transfer
the peritoneal cavity and both peritoneum and skin were closed. Blood without pre-conditioning. Ten-week-old unirradiated JAXBoy (Pt-
was extracted three days after the puncture. prcK302E) recipient mice were intravenously injected with a total of
1.5 × 107 unfractionated CD45.2+ Tet2−/− bone marrow cells, adminis-
Peritonitis. Male 8-to-12-week-old mice were injected intraperitoneally tered as 3 consecutive daily doses of 5 × 106 cells51. Donor cells were
with zymosan (1 mg, intraperitoneal injection, Sigma). After 2 h and 72 h collected from age-matched littermate Tet2−/− mice (8 to 10 weeks
we performed a peritoneal lavage for transcriptomic studies. old) by flushing femurs and tibias following euthanasia. To induce
hypercholesterolaemia, a recombinant AAV vector encoding a
Myocardial infarction. Male 8-to-12-week-old mice were intubated, gain-of-function form of mouse PCSK9 (pAAV/D377Y-mPCSK9)
and temperature controlled throughout the experiment at 36.5 °C to was delivered via a single tail vein injection52. One week later, mice
prevent hypothermic cardioprotection. Thoracotomy was then per- were placed on either a high-cholesterol western diet (Envigo,
formed, and the left anterior descending artery was ligated with a nylon TD.88137; 42% calories from fat, 0.2% cholesterol) or a matched con-
8/0 monofilament suture for 45 min. At the end of the ischaemia, the trol diet for 13 weeks. At endpoint, adoptive bone marrow transfer
chest was closed, and mice were kept with 100% O and given analgesia mice were euthanized and Tet2–/– (CD45.2+) or wild-type (CD45.1+)
2
with buprenorphine (subcutaneous injection, 0.1 mg kg−1) as described neutrophils were isolated from peripheral blood and bone marrow
previously47. Mice were euthanized 24 h or 72 h h after surgery and the by cell sorting. Cells were processed for scRNA-seq as described
heart was isolated for transcriptomics studies. below.
Bleomycin-induced fibrosis. We administered 1 mg kg−1 of bleomycin Sample preparation and flow cytometry-assisted cell sorting
sulfate to 8-to-12-week-old mice as previously described48. In brief, Mice were euthanized and Blood was taken through cardiac puncture
bleomycin was dissolved in saline and was instilled into the tracheal with a 1 ml syringe attached to a 26G needle filled with 50 ml of 0.5 M
lumen through a cannula under isoflurane (2.5% in oxygen) anaesthesia. EDTA. After blood collection, mice were perfused via the right ventricle
Bleomycin was injected at day 0 and at day 4. Mice were euthanized with 10 ml of PBS to remove circulating blood cells. Tissues, including
three weeks after bleomycin injection and lungs were collected for lung, tumours, muscle, heart, placenta and pancreas, were collected,
transcriptomics analysis. cut into small pieces, and digested with Liberase TM (Sigma) and DNase
I (Sigma) for 30 min at 37 °C. Following digestion, tissues were passed
Staphylococcus aureus Infection. Mice were intravenously infected through 70-µm nylon mesh sieves using syringe plungers to obtain
with 2.5 × 107 CFU of S. aureus (RNU4220 strain) and monitored for single-cell suspensions.
weight loss. For single-cell transcriptomic studies, blood was collected Bone marrow cells were obtained by flushing femurs with PBS
five days after infection. containing 2 mM EDTA and 2% FBS using a 23G needle. Spleens were
mechanically dissociated through 70-µm mesh filters. For colon iso-
Candida infection. Mice were intravenously infected with 1.5 × 105Can- lation, intestines were cleaned, cut longitudinally and washed in PBS.
dida albicans conidia (SC5314 strain), blood for single-cell transcrip- After a 30-min incubation in 100 mM EDTA at 37 °C with shaking to
tomic studies was extracted at day 6 after infection47. remove epithelial cells, colon tissue was cut and digested in Liberase TM
and DNase I for 30 min at 37 °C. Ear (skin) samples were processed by
LPS-induced inflammation. For transcriptomic studies, 400 ng of LPS separating the dorsal and ventral sides, cutting them into small pieces,
(Sigma) were injected intravenously. Blood and tissues were collected and digesting them in Liberase TM and DNase I for 90 min at 37 °C. The
24 h after injection. An intraperitoneal lethal dose of LPS (40 mg kg−1) resulting suspensions were filtered as above. Peritoneal lavage was
was used as a model of endotoxic shock. Mice were monitored daily for performed by injecting 10 ml of cold PBS into the peritoneal cavity,
weight loss. A weight loss of more than 20% of initial body weight was con- followed by gentle massage of the abdomen and careful aspiration of
sidered a lethal event and mice were euthanized at humane endpoints. the fluid using a syringe and needle. The collected fluid was centrifuged,
and the pellet was resuspended in fluorescence-activated cell sorting
High-fat diet. Apoe−/− mice were fed for 6 weeks with a control or (FACS) buffer for staining.
high-fat diet (HFD, 10.7% total fat, 0.75% cholesterol; Sniff) before For meninges isolation, mice were euthanized and decapitated.
blood extraction. The skull was opened along the sagittal midline, and the brain was
removed to expose the dura. The meninges were peeled off using fine
Dextran sulfate sodium colitis. To induce colitis, mice received for forceps and placed directly into digestion solution on ice. For the brain,
9 days water with 1.5% dextran sulfate sodium salt (MP Biomedicals) infarcted regions were dissected and digested for 30 min at 37 °C in an
as previously described49. Blood was collected on day 9 after dextran enzyme cocktail containing: 50 U ml−1 collagenase; 8.5 U ml−1 dispase;
sulfate sodium treatment. 100 µg ml−1 Nα-tosyl-L-lysine chloromethyl ketone hydrochloride;
5 U ml−1 DNase I in 9.64 ml HBSS without calcium, magnesium, or phenol
Hindlimb ischaemia. Hindlimb ischaemia experiments were per- red (Fisher Scientific, 14175-095). After digestion, brains were ground
formed as described50. In brief, mice were anaesthetized with isoflurane, using a 2 ml glass-glass grinder, filtered through a 70-µm filter, and cen-
the hindlimb was shaved, and, following a small incision in the skin, trifuged. Cell pellets were resuspended in 7 ml of 35% Percoll, overlaid
both the proximal end of the femoral artery and the distal portion of the with 5 ml HBSS to form a gradient, and centrifuged at 800g for 30 min
saphenous artery were ligated. The artery and all side-branches were at 4 °C (no brake). The myelin layer and supernatant were discarded,
dissected free; after this, the femoral artery and attached side-branches and the final cell pellet was washed and resuspended in FACS buffer.
were excised. Immediately after surgery, perfusion was measured by All single-cell suspensions were lysed in RBC lysis buffer (eBiosci-
laser Doppler imaging of plantar regions of interest (ROIs) (Moor Instru- ence) for 4 min and stained with the following antibodies: CD11b-PE
ments) and calculated as ratio of left (ligated) versus right (unligated) (Clone M1/70, BioLegend, 1:200); LY6G-AF647 (Clone 1A8, eBioscience,
values. Ischaemic muscle samples for transcriptomics analysis were 1:200); DAPI (1:10,000). Neutrophils were sorted as live (DAPI-negative),
collected one day after surgery. CD11b+LY6G+ cells using a FACS Aria sorter (BD Biosciences) at the Cen-
tro Nacional de Investigaciones Cardiovasculares (CNIC) Cytometry
Model of clonal haematopoiesis and PCSK9-induced hyper- Unit. Bone marrow neutrophils were captured as lineage-negative
cholesterolemia. To model TET2 loss-of-function-driven clonal (B220, CD18, NK.1.1, Ter119, CD3).
5′-GTGTACCCGTCCATGAAGGTG-3′; Il1b: forward 5′-AGTGAG
Cancer cell culture GAGAATGACCTGTTC-3′, reverse 5′-CGAGATGCTGCTGTGAGATT-3′;
The C57BL6/J syngeneic mouse LLC, E0771 breast luminal B and the Tnfaip3: forward 5′-GAACAGCGATCAGGCCAGG-3′, reverse 5′-GG
BALB/c-derived 4T1 breast tumour cell cancer cell lines were from the ACAGTTGGGTGTCTCACATT-3′; Cebpe: forward 5′-GCAGCCA
American Type Culture Collection. The pancreatic adenocarcinoma CTTGAGTTCTCAGG-3′, reverse 5′GATGTAGGCGGAGAGGTCGAT-3′;
FC1242 cell line (gift from D. Engle) was derived from Pdx1cre; KrasG12D/+; Ltf: forward 5′-TGAGGCCCTTGGACTCTGT-3′, reverse 5′-ACCCAC
null/+ (KPC) mice. B16-OVAGFP cells were provided by the laboratory TTTTCTCATCTCGTTC-3′.
of D. Sancho. All cells were cultured in DMEM (Thermofisher) sup-
plemented with 10% FBS (Thermofisher) and 100 µg ml−1 penicillin/ Functional assays
streptomycin (Thomas Sci). T cell cytotoxicity assay. B16F10–OVA-GFP (104 cells) were seeded
in 96-well culture dishes for 24 h, in RMPI medium with glutamine
In vitro mouse neutrophil culture and analysis (Thermofisher) containing 10% heat-inactivated FBS (Thermofish-
Primary mouse neutrophils were obtained from the femurs and tibias of er), 100 µg ml−1 penicillin/streptomycin (Thomas Sci); 200 nM glu-
healthy C57BL/6J mice, or indicated genetically modified mouse model, tamine, 1% non-essential amino acids (MEM amino acids; Gibco),
by centrifugation. Erythrocytes were lysed using Red Blood Cell Lysis 1% sodium pyruvate (Gibco) and 0.01% β-mercaptoethanol (Gib-
Solution (Qiagen; 79217). Cell strainer-filtered single-cell solutions co). Neutrophils from sorting or in vitro cultures were co-culture
were sorted in BD Aria Cell Sorter as DAPI− CD45+CD11b+LY6G+CD101+ at a 2:1 ratio with SIINFEKL-activated OT-1 T effector cells for 3 h.
mature, and DAPI− CD45+CD11b+LY6G+CD101− immature neutrophils. Neutrophil-OT-I cells were then seeded on top of B16F10-OVAGFP
Cells were seeded in 96-well plates, 50,000 cells per well, and cultured target cells 1:2 ratio. After 24 h, live cells were stained with 0.4 g l−1
with complemented DMEM medium (vehicle), or with the indicated crystal violet (Sigma-Aldrich, HT90132). The area covered by target
treatments. G-CSF (574606, BioLegend), TGFβ (7666-MB-005/CF, R&D), cells was quantified from micrographs of the plates using the ImageJ
IFNβ (581302, BioLegend), CXCL12 (578704, BioLegend), IL-1β (401-ML, software.
R&D Systems), and GM-CSF (315-03-20UG, Thermofisher) were used at
a concentration of 10 ng ml−1. Conditioned medium of LLC or KP-PDAC In vivo Matrigel plug assay. Fifty thousand neutrophils sorted from tis-
cells was obtained after 24 h culture of 80% confluence cells. Neutro- sues of interest were resuspended in 500 µl of growth-factor-depleted
phils were collected after 24 h or 48 h of treatment, and flow cytometry Matrigel (Corning) and injected subcutaneously in the lower back of
was performed using the following antibodies, all diluted 1:200 unless anaesthetized mice to form plugs. At days 3 and 7 after implantation,
indicated otherwise: CCR5-BUV615-P (BD Biosciences, 752321, clone the same number of sorted neutrophils was resuspended in 50 µl of PBS
C34-3448), CD101-PE-Cy7 (eBioscience, 25-1011-82, clone MOUSHI 101), and injected directly into the plug respectively. On day 9 after implan-
CD106-BUV563 (BD Biosciences, 741246, clone 429), CD115-BUV737 tation, Doppler laser perfusion imaging was performed at the lower
(BD Biosciences, 750948, clone AFS98), CD11b-BV510 (BioLegend, back region that contained the Matrigel plugs. One ROI was defined
101263, clone M1/70), CD11b-PE (BioLegend, 101208, clone M1/70), for each observable Matrigel plug, and the amount of flux variation
CD14-APC-Cy7 (BioLegend, 123318, clone Sa14-2), CD150-PE-Cy5 (Bio- in each ROI was quantified. Only ROIs that were not obscured by hair
Legend, 115911, clone TC15-12F12.2), CD16/32-PerCP-Cy5.5 (BioLegend, regrowth were used.
101324, clone 93), CD274-BV421 (BioLegend, 124315, clone 10F-9G2),
CD44-BV570 (BioLegend, 103037, clone IM7), CD45-APC (BioLegend, Chemotaxis assay. Chemotaxis assays were performed as described47.
103112, clone 30F11), CD74-BUV661 (BD Biosciences, 741572, clone In brief, bone marrow neutrophils were plated in 6.5 mm polycarbon-
In-1), KIT-BV605 (BioLegend, 135121, clone ACK2), CX3CR1-FITC (Bio- ate transwells with 5-mm pores (Corning) in RPMI medium 48 h after
Legend, 149020, clone SA011F11), DC-Trail-R1-biotinylated (R&D Sys- cytokine treatment. 20 ng ml−1 CXCL1 (R&D) was added to the bottom
tems, BAF2378, polyclonal), I-A/I-E-BUV496 (BD Biosciences, 750281, well. Transwells were incubated for 2 h at 37 °C and transmigrated cells
clone M5/114.15.2), ICAM1-PE-Dazzle 594 (BioLegend, 1161130, clone were collected from the bottom well and stained for cytometric analy-
YN1/1.7.4), LY6C-BV711 (BioLegend, 128037, clone HK1.4), LY6G-PE sis. The number of transmigrated cells was assessed by the presence of
(BioLegend, 127608, clone 1A8), Sca1-BUV395 (BD Biosciences, 563990, a known number of Truecount beads (BD Biosciences).
clone D7), TLR4-BV786 (BD Biosciences, 741015, clone MTS510).
Streptavidin-BV650 (BioLegend, 405231) was included at 1:500. 3D Doppler imaging of tumour vascularization. Subcutaneous LLC
Secondary staining was performed with Streptavidin-BV650 (Biole- tumour vascularization was imaged using Vevo Imaging Systems once
gend). Cells were analysed in a SymphonyA4 Flow Cytometer. The data they reached 500 mm3. In brief, mice were anaesthetized in an isoflu-
were analysed using FlowJo v.10 software. FlowAI53 was used for quality rane vapourizer chamber, and the backs were thoroughly shaved. The
control of flow data, followed by dimensionality reduction using the mice were placed in the imaging platform and images were captured
UMAP_R plugin54. Initial clusterization was performed with FlowSOM55 using the power colour Doppler-3D mode. A total of 100 images were
and ClusterExplorerPlugin, and UMAP parameters were embedded in captured to generate a 3D reconstruction of the vasculature. Vevo LAB
each sample for statistical analysis of neutrophil phenotypes. software was used to calculate the Volume and per cent vascularization
of tumours. Per cent vascularization is determined by calculating the
RNA isolation, reverse transcription PCR percentage of pixels in the volume that have a power Doppler signal
Total RNA was prepared with the RNA Extraction RNeasy Plus Mini-kit associated with them, the presence of this signal indicates the pres-
(QIAGEN) and RNA was reverse-transcribed with the High-Capacity cDNA ence of blood flow.
Reverse Transcription kit (Applied Biosystems) according to the manu-
facturer’s protocol. Real-time quantitative PCR (SYBR-green, Applied NET formation assay. Forty-eight hours after cytokine treatment,
Biosystems) assays were performed with an Applied Biosystems 7900HT 5 × 104 bone marrow neutrophils were plated with RPMI medium on
Fast Real-Time PCR System sequencer detector. Expression was normal- poly-l-lysine-covered 8-well µ-Slides (Ibidi), and left 30 min to adhere.
ized to the expression of the 36b4 housekeeping gene. Primer sequences Subsequently, cells were incubated for 2 h with 100 nM PMA or vehicle.
are as follows: 36b4: forward 5′-ACTGGTCTAGGACCCGAGAAG-3′, Cells were then fixed using 4% PFA for 10 min, permeabilized with PBS
reverse 5′- TCCCACCTTGTCTCCAGTCT-3′; Ptgs2: forward 5′-TGAGC with 0.1% Triton X-100, 1% goat serum plus 5% BSA and stained with
AACTATTCCAAACCAGC-3′, reverse 5′-GCACGTAGTCTTCGATCA antibodies against cit-H3, DNA (Sytox-green, Molecular Probes) and
CTATC-3′; Nr4a1: forward 5′-TTGAGTTCGGCAAGCCTACC-3′, reverse MPO. Whole-slide z-stack tilescan images were acquired with a Leica
Article
SP5 confocal microscope, and analysed using Imaris software (v.9.5, and exons: Cebpb (exon 1; gRNA: AGGCTCACGTAACCGTAGT); Klf6
Bitplane)47. (exon 1; gRNA: TCGCTGTCGGGAAAACAGGG); Runx1 (exon 3; gRNA:
TAGCGAGATTCAACGACCTC); Rfx2 (exon 5; gRNA: CTGCTGGGGGCGT
Bacterial killing assay. Forty-eight hours after cytokine treatment, AAAGCTG); Relb (exon 4; gRNA: CTGCACGGACGGCGTCTGCA); Irf5
bone marrow neutrophils were resuspended in fresh medium along (exon 2; gRNA: ACCCTGGCGCCATGCCACGAGG); and Junb (exon 1;
with live S. aureus (ATCC) that were grown in tryptic soy broth. For gRNA: GGAACCGCAGACCGTACCGG).
the in vitro assays, neutrophils and bacteria (104 CFU in 200 µl) were
incubated at 37 °C for 60 min. The cells are then plated onto tryptic soy JUNB overexpression. Lentiviral vectors for JUNB overexpression were
plates in a serial dilution. Bacterial colonies on the plates were counted generated by transient transfection of HEK293T cells using the calcium
the following day. phosphate precipitation method. Cells were co-transfected with: (1) a
transfer plasmid containing the Junb cDNA under the control of the
Phagocytosis assay. Forty-eight hours after cytokine treatment, bone human PGK promoter; (2) packaging plasmid psPax2; and (3) envelope
marrow neutrophils were resuspended in fresh medium along with plasmid pMD2.G encoding VSV-G. The medium was replaced 24 h af-
fluorescent latex beads (SIGMA) followed by flow cytometric analyses. ter transfection. At 72 h, virus-containing supernatant was collected,
clarified by centrifugation (2,000 rpm, 5 min, 4 °C), filtered (0.45 µm),
Analysis of human neutrophils and concentrated via ultracentrifugation (26,000 rpm, 2 h, 4 °C). Viral
Isolation and expansion of human bone marrow CD34+ HSPCs. Bone pellets were resuspended in cold PBS, aliquoted, and stored at −80 °C.
marrow samples were obtained from healthy donors under informed
consent approved by the ethics committee of the University Hospital Lentiviral transduction of HOXB8. HOXB8 progenitors were trans-
Tübingen. CD34+ haematopoietic stem and progenitor cells (HSPCs) duced by spinoculation. In brief, 5 × 105 cells were plated per well in 6-well
were isolated through Ficoll gradient centrifugation followed by mag- plates with 1 ml of medium. Lentiviral particles were added at a multiplic-
netic bead-based separation using the EasySep Human CD34+ Cell ity of infection (MOI) of 11.24 for the vector pRRL-hPGK-JUNB-IRES-eGFP
Selection Kit II (Stem Cell Technologies, 17856). CD34+ cells (n = 4; purity and MOI = 1.8 for the pRRL-hPGK-IRES-eGFP empty vector, and cells
95.4 ± 1.9%) were cultured at a density of 5 × 105 cells per ml in StemSpan were centrifuged at 1,000g for 90 min at 30 °C. Following transduc-
SFEM II haematopoietic stem cell medium (Stem Cell Technologies, tion, cells were collected, washed, and resuspended in fresh culture
09655), supplemented with 1% penicillin/streptomycin, 20 ng ml−1 IL-3, medium at a final concentration of 5 × 104 cells per ml.
20 ng ml−1 IL-6, 20 ng ml−1 TPO, 50 ng ml−1 SCF and 50 ng ml−1 FLT-3L (all
cytokines purchased from R&D Systems). Cells were cultured under Plasmid construction. To construct the JUNB expression vector, the hu-
standard conditions (37 °C, 5% CO) and frozen for future use. man PGK (hPGK) promoter was PCR-amplified with ClaI and XbaI restric-
2
For granulocytic differentiation in vitro, cells were seeded at a density tion sites and cloned into the ClaI/XbaI sites of the pRRL-CMV-IRES-eGFP
of 2 × 105 cells per ml. During the first 8 days of differentiation (days vector, replacing the CMV promoter. The Junb coding sequence was
0–7), cells were maintained in a myeloid cell expansion medium—RPMI amplified from mouse cDNA using primers containing BglII and XhoI
1640 supplemented with 10% FCS, 1% penicillin/streptomycin, 5 ng ml−1 sites and inserted into the BamHI and XhoI sites of the modified vector.
SCF, 5 ng ml−1 IL-3 and 1 ng ml−1 G-CSF. The medium was changed every Cloning was performed using the following primers: hPGK forward
two days. On day 8 of culture, the medium was replaced with a granulo- (ClaI): 5′-TTTTTTATCGATGGGTAGGGGAGGCGCTTT-3′; hPGK reverse
cytic cell differentiation medium (RPMI 1640 supplemented with 10% (XbaI): 5′-TTTTTTTTAGACGAAAGGCCCGGAGATGA-3′; Junb forward
FCS, 1% penicillin/streptomycin and 1 ng ml−1 G-CSF). The medium was (BglII): 5′-TTTTTTAGATCTGCCACCATGTGCACGAAAATGGAACA-3′;
changed every 2 days until day 14. On day 13 of differentiation, cells were Junbreverse (XhoI): 5′-TTTTTTCTCGAGTCAGAAGGCGTGTCCCTT-3.
collected and counted. 800,000 cells were lysed for RNA isolation,
50,000 cells for FACS, and 40,000 cells for cytospins. The remaining Culture of HOXB8 cells. For the flow cytometry and bulk
cells were resuspended in fresh granulocytic differentiation medium RNA-sequencing experiments, HOXB8 progenitors at day 3.5 of dif-
at a seed density of 2 × 105 cells per ml and divided into 4 groups. Group ferentiation were seeded in 96-well plates at a density of 50,000 cells
one was maintained in granulocytic differentiation medium, group two per well. Cells were cultured in complete RPMI medium (vehicle) or
was treated with 10 ng ml−1 TGFβ, group three was treated with 10 ng ml−1 treated with GM-CSF (10 ng ml−1) for 48 h, following the same condi-
IFNβ (refreshed after 24 h), and group 4 was treated with 10 ng ml−1 tions described for primary bone marrow neutrophil cultures. Vehicle
GM-CSF. RNA-seq analyses were performed 48 h after stimulation. or GM-CSF treated cells were collected at 48 h after treatment for the
analysis.
HOXB8 cell cultures and differentiation. HOXB8-immortalized my-
eloid progenitors were routinely tested for mycoplasma contamination Bulk RNA sequencing of mice and human-derived neutrophils
and cultured in RPMI 1640 medium supplemented with 10% fetal calf RNA from isolated mouse neutrophils was extracted using RNAeasy
serum (FCS), 10 µM β-mercaptoethanol (Thermo Fisher Scientific), micro kit (Quiagen). RNA quality was checked using capillary electro-
4% supernatant from SCF-producing CHO cells, 1% penicillin/strep- phoresis (Agilent). Samples were submitted for whole RNA next genera-
tomycin and 1 µM β-oestradiol (Sigma-Aldrich) to maintain the pro- tion sequencing in the Genomics Unit of CNIC. Total RNA (200 ng) was
genitor state. Neutrophil differentiation was initiated by β-oestradiol used to generate barcoded RNA-sequencing libraries using the NEBNext
withdrawal and continued culture in medium supplemented with 1% Ultra RNA Library preparation kit (New England Biolabs). Libraries were
SCF-containing supernatant. Differentiation into neutrophils was sequenced with HiSeq2500 (Illumina) to generate 50-nucleotide single
achieved by culturing cells in RPMI 1640 medium containing 10% FCS, reads, with a minimum of 8 million reads per sample. For RNA-seq of
30 µM β-mercaptoethanol, 4% SCF supernatant, and 20 ng ml−1 granu- human-derived neutrophils, we isolated RNA from a total of 800,000
locyte colony-stimulating factor (G-CSF) under standard tissue culture differentiated neutrophils collected on day 13 and 15. We used the
conditions (37 °C, 5% CO). NucleoSpin RNA Mini Kit (Macherey-Nagel, 740955.50), following the
2
manufacturer’s instructions. RNA concentration was assessed with
CRISPR–Cas9-mediated knockout. Knockouts of selected transcrip- Qubit 2.0 (Thermo Fisher), and a total of 400 ng RNA was sequenced.
tion factors in HOXB8 progenitors have been previously described21. In RNA integrity was assessed using Agilent Bioanalyzer 2100, with RNA
brief, HOXB8 progenitors were transduced with lentiCas9-v2 lentiviral integrity number (RIN) between 9.8 and 10.0. RNA samples were pro-
vectors encoding guide RNAs (gRNAs) targeting the following genes cessed by Novogene for library preparation and sequencing, and all
samples passed the quality control criteria. Strand-specific libraries were discarded. Cell Annotation was performed using R package Sin-
were generated on the basis of Novogene’s standard protocol. Samples gleR and the Immgen database for each dataset individually. All sub-
were sequenced on an Illumina platform to produce 150 bp pairwise sequent downstream analyses were implemented using R (v.4.0.3) and
reads (PE150) per sample. the package Seurat (v.4.0.5)61. The Seurat suite was used to integrate
FastQ files for each sample were obtained using CASAVA (v.1.8) soft- the neutrophils from all datasets using Seurat’s integration imple-
ware (Illumina). Reads were further processed with RTA (v.1.18.66.3). mentation. This method uses common sources of variation across
FastQ files for each sample were obtained using bcl2fastq (v.2.20.0.422) the different datasets and aligns the cells so those in similar biological
software (Illumina). Sequencing reads were further processed as fol- states cluster together. The integrated dataset was used to perform the
lows: Illumina adapters were trimmed and low-quality reads removed unbiased cluster analysis and the construction of NeuMap. Additionally,
with Cutadapt (v.4.9)56 (mismatch rate = 1 mismatch every 10 bp, over- we used the integrated NeuMap to generate a reference which we later
lap = 5 bp, minimum read length = 30 bp). Quality control of the pro- used to analyse additional and external datasets by projecting cells
cessed reads was done with fastQC (v.0.12.1). RSEM (v.1.3.1) was used onto our reference and annotate the new data using our custom labels
to quantify expression levels against the mouse genome reference using Seurat’s MapQuery and TransferData. This method is technol-
GRCm38 or the human genome reference GRCh38, depending on the ogy agnostic, so we could reliably project cells from external datasets
analysis57 (default options). The processing of the counts and differ- sequenced in different platforms onto NeuMap62,63.
ential expression analysis was performed using limma (v.3.32.2)58 and
EdgeR (v.3.20.1)59) which were also used to perform pairwise differential Definition of hubs. Functional hubs were selected by performing
expression analyses. To identify genes whose expression significantly unbiased clustering at different resolutions using Seurat’s function
varies across conditions, we applied a Likelihood Ratio Test (LRT) using FindClusters(). Resolutions used ranged between 0.05 and 0.3. Clusters
DESeq2 (v.1.30.1)60, allowing the detection of global effects of a factor from different resolutions were selected because they best represented
without the need to specify individual contrasts. The resulting signifi- the expression of functional signatures projected onto NeuMap. Ar-
cant genes were then clustered using the k-means algorithm from the eas shown in the figures correspond to the q15 quantile of the KMASS
stats package (v.4.0.3). algorithm, which calculates the density of cells in specific areas. For
clarity, hubs in figures are shown as the area with the accumulation of
Single-cell transcriptomics on mouse neutrophils 85% of cells for each selected cluster/hub. Analyses were performed on
scRNA-seq of sorted tissue neutrophils. For single-cell analysis, all the complete set of cells for each cluster or hub. The FindAllMarkers()
samples were collected between ZT1 and ZT5. Tissues were dissected function from Seurat was used to calculate DEGs across the hubs. Only
and dissociated into a single-cell suspension by enzyme digestion. genes detected in a minimum of 25% of the cells and with an average of
The resulting suspensions were filtered through cell strainers, and at least 0.25-fold difference (log scale) between the groups in either of
sorted in BD Aria Cell Sorter as DAPI−CD11b+LY6G+ cells, and load- the groups were tested.
ed into a BD Rhapsody cartridge. For the generation of single-cell
whole-transcriptomes, we used a BD Rhapsody system according to Kernel density estimation. The MASS R package (v.7.3.61) was used
the manufacturer’s instructions. In brief, cell suspensions from each for two-dimensional kernel density estimation (K-mass score), with
condition were incubated with Sample Tags (BD) for 20 min at room n = 100 grid points in each direction.
temperature. Cells were then washed three times and pooled in a single
tube. Cell viability and concentration were assessed using a Countess Signature projection. The signatures used for illustration of func-
III cell counter (Thermo Fisher). Sixty thousand cells were loaded into a tional states are contained in Supplementary Table 2. All signatures
Rhapsody Single Cell Analysis System cartridge. Cell capture and cDNA were calculated by Seurat’s AddModuleScore() function. We used two
synthesis were performed according to manufacturer’s instructions; different sources for the functional signatures: (1) previous publica-
cells were isolated into nanowells by gravity, then cells were lysed and tions, for which we provide the whole list of genes reported and used
mRNAs together with sample tags oligonucleotides were released and in Supplementary Table 2; and (2) public databases such as gene ontol-
captured by the beads present in the nanowells. Each bead contained ogy (GO) and gene set enrichment analysis (GSEA). In those cases the
a unique oligonucleotide named ‘cell label’ to identify each individual whole gene list from the functional category was tested. For signatures
bead. All beads present in the cartridge were collected and cDNA syn- from human data, human genes were mapped to their correspond-
thesis took place in a single reaction. At this point, each cDNA and Sam- ing mouse homologue to calculate the enrichment score using the
ple Tag oligonucleotide were attached to its corresponding cell label Mouse Genome Informatics (MGI) database. We used Seurat R package
oligonucleotide. Two separated indexed libraries were prepared for (v.5.2.1) AddModuleScore() function to calculate the scores. To gener-
whole-transcriptome analysis and sample tag demultiplexing following ate visualization heat maps across NeuMap hubs, we first calculated
the manufacturer’s instructions. The average size of the libraries was enrichment scores for each cell. Scores were then averaged by hub
calculated using the 2100 Bioanalyzer (Agilent), and the concentration and scaled per signature for comparison. To assess whether gene sig-
was determined using the Qubit fluorometer (Thermofisher). Finally, nature scores significantly differed across NeuMap hubs, we applied
libraries were combined and sequenced together in a paired-end run the Kruskal–Wallis test to each signature, testing the null hypothesis
(60 × 42) using a NextSeq 2000 system (Illumina) and a P2 flow cell. that score distributions were identical across hubs. The resulting test
Output files were processed with NextSeq 1000/2000 Control Soft- statistics were compared to a chi-squared distribution, with degrees of
ware Suite v.1.4.1. FastQ files for each sample were obtained using BCL freedom equal to the number of hubs minus one. To correct for multiple
Convert v.3.6.3 software (Illumina). comparisons, we adjusted P values using the Benjamini–Hochberg false
discovery rate method.
Construction of NeuMap and projection of external data. Rhap-
sody analysis pipeline v.1.9.1 was run locally. This pipeline includes Velocyto analysis. The analysis of expression dynamics in scRNA-seq
steps for, alignment to mouse genome reference (GRCm38 with the data was performed using velocyto (v.0.17.17)24, a package that allows es-
gencodevM19-20181206) quantification and filtering of low-quality timating RNA velocities distinguishing between spliced and unspliced
cells and tagging of doublets, which were also filtered out of the down- mRNAs in standard scRNA-seq protocols. The command line tool in
stream analyses61. After BD Rhapsody’s pipeline automatic quality Python implementation was adapted to be able to work with BAM files
filtering, a second round was performed manually, where cells with generated by BD Rhapsody, using samtools64 to format the files, mainly
a mitochondrial content over 20% or with over 300 total gene counts by removing all possible alignments with antibodies and renaming the
