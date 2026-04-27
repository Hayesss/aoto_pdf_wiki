---
source_path: /mnt/c/Users/Administrator/Zotero/storage/BCSCF8SN/S0092867425006907.pdf
ingested: 2026-04-23
sha256: d408f5631416fafa
---

Article
Optogenetics-enabled discovery of integrated stress
response modulators
Graphical abstract Authors
FelixWong,AliciaLi,SatotakaOmori,...,
HahnKim,JamesJ.Collins,
MaxwellZ.Wilson
Correspondence
felix@integratedbiosciences.com(F.W.),
jimjc@mit.edu(J.J.C.),
max@integratedbiosciences.com (M.Z.
W.)
In brief
Anoptogenetics-enableddrugscreening
platformfacilitatestargetingofthe
integratedstressresponse,leadingtothe
identificationofcompoundsthat
selectivelypotentiateISRsignaling
acrossdiversestressorsandexhibit
broad-spectrumantiviralactivity.
Highlights
•
Anoptogeneticsplatformspecificallyinducestheintegrated
stressresponse
•
Thisplatformenablesahigh-throughputscreenof370,830
compounds
•
IdentifiedcompoundsselectivelyeliminateISR-highcells
acrossdiversestressors
•
Thesecompoundsdemonstratebroad-spectrumantiviral
activityinvitroandinmice
Wongetal.,2025,Cell188,1–18
September4,2025©2025ElsevierInc.Allrightsarereserved,includingthose
fortextanddatamining,AItraining,andsimilartechnologies.
ll
https://doi.org/10.1016/j.cell.2025.06.024
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
Optogenetics-enabled discovery of integrated
stress response modulators
Felix Wong,1 ,13, * Alicia Li, 1,13 Satotaka Omori, 1,13 Ryan S. Lach, 1,13 Jose Nunez, 1 Yunke Ren, 1 Sean P. Brown, 1
Vipul Singhal,1 Brent R. Lyda, 1 Taivan Batjargal, 1 Ethan Dickson, 2,3,4,5 Jose Roberto Rodrigues Reyes, 2,3,4,5
Juan Manual Uruena Vargas, 6 Shalaka Wahane,7 Hahn Kim,8 ,9 James J. Collins, 10,11,12,14, * and Maxwell Z. Wilson 1,2,3,4,5, *
1 Integrated Biosciences, Redwood City, CA 94065, USA
2 Center for BioEngineering, University of California, Santa Barbara, Santa Barbara, CA 93106, USA
3 Biomolecular Science and Engineering Program, University of California, Santa Barbara, Santa Barbara, CA 93106, USA
4 Department of Molecular, Cellular, and Developmental Biology, University of California, Santa Barbara, Santa Barbara, CA 93106, USA
5 Neuroscience Research Institute, University of California, Santa Barbara, Santa Barbara, CA 93106, USA
6 NSF BioPACIFIC Materials Innovation Platform, California NanoSystems Institute, University of California, Santa Barbara, Santa Barbara, CA
93106, USA
7 Illumina Ventures, Foster City, CA 94404, USA
8 Princeton University Small Molecule Screening Center, Princeton University, Princeton, NJ 08544, USA
9 Department of Chemistry, Princeton University, Princeton, NJ 08544, USA
10 Infectious Disease and Microbiome Program, Broad Institute of MIT and Harvard, Cambridge, MA 02142, USA
11 Institute for Medical Engineering & Science and Department of Biological Engineering, Massachusetts Institute of Technology, Cambridge,
MA 02139, USA
12 Wyss Institute for Biologically Inspired Engineering, Harvard University, Boston, MA 02115, USA
13 These authors contributed equally
14 Lead contact
*Correspondence: felix@integratedbiosciences.com (F.W.), jimjc@mit.edu (J.J.C.), max@integratedbiosciences.com (M.Z.W.)
https://doi.org/10.1016/j.cell.2025.06.024
SUMMARY
The integrated stress response (ISR) is a conserved stress response that maintains homeostasis in eukary-
otic cells. Modulating the ISR holds therapeutic potential for diseases including viral infection, cancer, and
neurodegeneration, but few known compounds can do so without toxicity. Here, we present an optogenetic
platform for the discovery of compounds that selectively modulate the ISR. Optogenetic clustering of PKR
induces ISR-mediated cell death, enabling the high-throughput screening of 370,830 compounds. We iden-
tify compounds that potentiate cell death without cytotoxicity across diverse cell types and stressors. Mech-
anistic studies reveal that these compounds upregulate activating transcription factor 4 (ATF4), sensitizing
cells to stress and apoptosis, and identify GCN2 as a molecular target. Additionally, these compounds exhibit
antiviral activity, and one compound reduced viral titers in a mouse model of herpesvirus infection. Structure-
activity and toxicology studies highlight opportunities to optimize therapeutic efficacy. This work demon-
strates an optogenetic approach to drug discovery and introduces ISR potentiators with therapeutic
potential.
INTRODUCTION 2 subunit 1 (eIF2α), leading to downstream production of acti-
vating transcription factor 4 (ATF4) and other ISR components,
Cellular stress responses consist of diverse signaling cascades including C/EBP homologous protein (CHOP) and protein phos-
that regulate fundamental cellular processes, including proteo- phatase 1 regulatory subunit 15A (GADD34). Ultimately, the ISR
stasis, metabolism, and cell division. As a central regulator of results in either an adaptive response in which cells attenuate
cellular homeostasis, the integrated stress response (ISR) is global protein synthesis to overcome the stressor or a terminal
conserved across metazoan cells and responds to diverse response in which apoptosis is induced (Figure 1A).
stressors, including viral infection, endoplasmic reticulum (ER) Dysregulation of the ISR and related stress responses, such as
stress, amino acid deprivation, oxidative stress, and heme defi- the unfolded protein response (UPR)4 —in which PERK is also a
ciency.1 –3 These stressors are detected by four stress sensor ki- sensor kinase—has been shown to contribute to the pathology
nases—HRI, PKR, PERK, and GCN2—that regulate translation of various diseases, including viral infection, 5,6 pulmonary
through phosphorylation of eukaryotic translation initiation factor fibrosis,7 ,8 cognitive decline,9 ,10 and prion disease.1 1 Given the
Cell 188, 1–18, September 4, 2025 © 2025 Elsevier Inc. 1
All rights are reserved, including those for text and data mining, AI training, and similar technologies.
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
A C D E
F G H
B
I J K
L M N
Figure 1. An optogenetics-based virtual stress platform for the chemical screening of ISR modulators
(A) Schematic of ISR signaling.
(B) Optogenetic clustering of PKR with the opto-PKR construct.
(C) Opto-PKR fluorescence intensity in single cells in response to optogenetic illumination. Cells were treated with either DMSO (0.5%) vehicle or 10 μM ISRIB at
0 h, and results are representative of two biological replicates. Points indicate mean values, and error bars indicate SEM. Cell counts for each time point: 1,683,
1,709, 1,383, 982, 616, 1,277, 1,160, 1,141, 965, and 1,274 for vehicle-treated 0–9 h; 1,635, 1,701, 1,702, 1,566, 1,826, 1,645, 1,399, 1,190, 1,556, and 1,424 for
ISRIB-treated 0–9 h.
(D) Global protein synthesis, as measured by OPP fluorescence, in the same cells as in (C). Points indicate mean values, and error bars indicate SEM.
(E) Representative OPP staining images from the experiment shown in (D). Scale bar, 10 μm.
(F) (Left) Anti-CHOP fluorescence in single opto-PKR cells in response to optogenetic illumination. Results are representative of two biological replicates. Points
indicate values for individual cells, and horizontal lines indicate mean values. Cell counts for each group, from left to right: 827 and 766. (Right) Representative
anti-CHOP fluorescence images. Scale bar, 30 μm.
(G) (Left) Anti-CHOP fluorescence in single opto-PKR cells in response to compound treatment. Cells were treated with either DMSO (0.5%) vehicle or 10 μM
ISRIB and incubated in light for 10 h, and results are representative of two biological replicates. Points indicate values for individual cells, and horizontal lines
indicate mean values. Cell counts for each group, from left to right: 343 and 555. (Right) Representative anti-CHOP fluorescence images. Scale bar, 30 μm.
(H) Cell viability dose-response curves for opto-PKR cells treated with ISRIB for 24 h in light and in dark (cyan and black points, respectively). Colored points
represent the means of two biological replicates (gray points). Values were normalized against those of DMSO (0.5%) vehicle-treated cells in dark, and the dashed
line indicates the baseline cell viability value of vehicle-treated cells in light. Cell viability increases are highlighted in green.
(I–M) Similar to (H) but for other known ISR modulators. Decoupled cell viability decreases, in which cell viability decreases more in dark than in light for the same
concentration of compound or vice-versa, are highlighted in yellow and red, respectively.
(N) Schematic of the screening approach.
See also Figure S1.
central role of the ISR in these diseases, previous efforts exhibit poor pharmacokinetic properties and cardiovascular
have aimed to identify and develop small-molecule modulators toxicity, respectively.1 9,20 Discovering ISR-modulating com-
of the ISR as drug candidates. These efforts have resulted in pounds without such limitations would facilitate the development
the discovery and characterization of ISR activators, including of drug candidates capable of targeting diseases through their ef-
guanabenz,1 2,13 Sephin1,1 4 PKR inhibitor C16,1 5 and salubrinal,1 6 fects on cellular proteostasis.
as well as ISR inhibitors, including ISRIB1 7 and 2BAct.1 8 Neverthe- Concurrent with these discovery efforts, advances in
less, the platforms used to discover these compounds have largely synthetic biology have enabled precise control of cellular stress re-
relied on screens against specific targets,1 5 against specific sponses,2 1,22 facilitating phenotypic drug discovery approaches.
disease presentations, 12 or using small-molecule stressors, We recently engineered an optogenetic system that triggers PKR
such as tunicamycin,1 6,17 that induce pleiotropic cytotoxic ef- phase separation upon exposure to blue light, mimicking PKR’s
fects.1 8 Furthermore, multiple ISR activators exhibit cytotoxic natural activation and inducing the ISR without the off-pathway
liabilities or adverse effects, and ISRIB and 2BAct are known to cytotoxicity associated with small-molecule stressors.2 2 Given
2 Cell 188, 1–18, September 4, 2025
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
the ability to activate the ISR in the absence of damage, we exposure alone do not obfuscate detection of ISR modulation
reasoned that our optogenetic tool could provide an efficient and (Figures 1D–1H). ISRIB treatment at high concentrations
on-pathway approach to detecting the effects of small-molecule (∼50 μM) did not completely rescue cells, whereas the effects
modulators of the ISR. This screening approach would be pheno- of treatment at low concentrations (∼10 pM) could still be
typic by design, enabling the rapid identification of compounds resolved. Although light pulsing experiments suggest that selec-
with potentially diverse mechanisms of action but necessitating tive activation of the ISR occurs with minimal light dosing
downstream target deconvolution using complementary methods. (Figure S1C), blue light phototoxicity or ISRIB’s limiting cytotox-
Here, we tested this hypothesis by performing the largest optoge- icity at high concentrations may contribute to ISR-independent
netic screen to date,2 3 in which the ISR-modulating effect of each decreases in cell viability. Nevertheless, experimental replicates
of 370,830 small molecules was quantified by co-treating engi- suggest that our measurements of cell viability are robust, with
neered cells with blue (450 nm) light and compound. typical coefficient of variation values < 10%, and can identify
other ISR-specific inhibitors, including 2BAct (Figures 1I
RESULTS and S1B).
Although activators, including halofuginone, salubrinal, and
Optogenetics-based analysis of ISR-modifying Sephin1, have been shown to activate the ISR, treatment with
compounds these compounds did not substantially alter cell viability in light
We first characterized a synthetic gene circuit enabling light- relative to dark (Figures 1J–1L and S1D). An exception is halofu-
inducible clustering of PKR in the presence of known small-mole- ginone, which exhibited selective cytotoxicity against cells in
cule modulators of the ISR. We have previously shown that phys- dark at concentrations of ∼100 nM: this effect was abrogated
iological activation of PKR depends on its oligomerization 24–26 in cells pretreated with light for 24 h, suggesting that adaptive
and can be mimicked by replacing PKR’s double-stranded ISR activation might protect cells from treatment (Figure S1E).
RNA (dsRNA) binding domains (dRBM1 and dRBM2) with Overall, our observations indicate that the ISR-activating effects
Cry2Olig (E490G; Figure 1B). We thus transduced human H4 neu- of these compounds are not additive with opto-PKR stimulation
roglioma cells, chosen for their relative ease of expansion and in the terminal cell fate decision. In fact, all compounds were
neural epithelial origin, with a citrine-tagged Cry2Olig-PKR cytotoxic to cells kept in the dark at higher concentrations, and
(hereafter referred to as opto-PKR), and isolated a pseudo-clonal some of these compounds may act on pathways other than
population to reduce heterogeneity in the cellular response. We the ISR, consistent with the results for salubrinal presented
previously found that, in response to non-phototoxic levels of further below. Additionally, SP600125, an ATP-competitive in-
blue light, opto-PKR cells exhibited cytoplasmic condensates, hibitor of c-Jun N-terminal kinase (JNK),3 0 selectively decreased
elevated levels of phosphorylated eIF2α (peIF2α), and decreased cell viability in light without being acutely cytotoxic to control
puromycin incorporation in nascent peptides on a timescale of 1 cells at a dose of 12.5 μM, suggesting that it may further activate
h.2 2 We reasoned that capturing the temporal dynamics of ISR the ISR at a narrow range of concentrations (Figure 1M). Taken
activation would provide a precise quantitative baseline for together, our results suggest that an optogenetic approach, us-
assessing pharmacologic modulators. Accordingly, here we sub- ing opto-PKR cells co-treated with light and a test compound,
jected opto-PKR cells to blue light for up to 10 h and quantified could enable screening for small-molecule modulators of the
both the incorporation of o-propargyl-puromycin (OPP) 27 —a pu- ISR by assessing cell viability after 24 h (Figures 1N and S1A).
romycin analog detectable using click chemistry—into nascent
peptides and the expression of CHOP with immunofluorescence. Optogenetic screening of 370,830 compounds reveals
Consistent with previous work, 22 we observed receptor-level putative ISR modulators
negative feedback wherein opto-PKR fluorescence intensity de- We assembled a small-molecule library of 370,830 compounds
cayed with activation time (Figure 1C). Compared with control that, relative to known chemical modulators of the ISR, samples
opto-PKR cells maintained in the dark, cells illuminated for 3 h an expanded chemical space, as visualized through t-distributed
showed an average decrease of up to 4-fold in OPP levels stochastic neighborhood embedding (t-SNE) on the Morgan fin-
(Figures 1D and 1E) and moderately (∼20%) increased levels of gerprints of each chemical structure (Figure 2A; Data S1). This li-
CHOP after 10 h of light (Figures 1F and 1G). brary included the Pharmakon library of clinically evaluated
Upregulation of CHOP is known to induce a terminal apoptotic drugs, natural products, metabolites, and other smaller, previ-
stress response, 1–3,28,29 and hence we hypothesized that longer- ously described libraries. 31–33 We screened this library of com-
duration (>10 h) activation of opto-PKR would result in ISR-asso- pounds at a final concentration of 10 μM—a concentration
ciated cell death. Consistent with this hypothesis, we found a informed by prior compound screens 32–34 —by scaling up the
substantial decrease in cell viability as measured using resazurin high-throughput approach outlined in Figure 1N and measuring
(a metabolic activity indicator), with ∼60% cell death occurring the viability of opto-PKR cells after 24 h of light in the presence
after 24 h of light—a time point chosen to integrate the effects of each compound (Figure 2B).
of ISR signaling across earlier time points while providing a As a counterscreen for cytotoxicity, we measured the viability
high dynamic range of cell viability decreases (Figures S1A and of IMR-90 human lung fibroblasts—chosen to represent a non-
S1B). In the presence of light, ISRIB treatment increased cell cancerous cell type—after 3 days of compound treatment at a
viability, elevated OPP levels, and reduced CHOP levels, consis- final concentration of 10 μM in ambient lighting (Figure 2C). As
tent with the hypothesis that extended ISR activation contributes a starting point for defining putative ISR-modifying compounds,
to cell death and that pleiotropic, off-pathway effects of light we shortlisted compounds for which treatment resulted in a
Cell 188, 1–18, September 4, 2025 3
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
A B
C
D E F G
H I J K
L M N
Figure 2. Optogenetics-driven discovery of compounds that selectively kill ISR-high cells
(A) t-SNE plot of the screening library of 370,830 compounds relative to known ISR-modulating compounds.
(B and C) Histograms of relative cell viability values obtained from screening the 370,830-compound library shown in (A) at a final concentration of 10 μM.
(D–K) Cell viability dose-response curves for opto-PKR cells treated with IBX-200 to IBX-207 for 24 h in light and in dark (cyan and black points, respectively).
Colored points represent the means of two biological replicates (gray points). Values were normalized against those of DMSO (0.5%) vehicle-treated cells in dark,
and the dashed line indicates the baseline cell viability value of vehicle-treated cells in light. Decoupled cell viability decreases are highlighted in red.
(L) Chemical scaffolds represented by IBX-200 to IBX-207.
(M) Molecular weights and Tanimoto similarity of IBX-200 to IBX-207 with respect to the known ISR modulators shown in (A).
(N) Half-maximal cytotoxic concentration (CC
50
) values of IBX-200, IBX-202, IBX-204, and other ISR-modulating compounds against different cell types. As-
terisks indicate values >200 μM, and values shown are from one biological replicate.
See also Figures S2 and S6.
4 Cell 188, 1–18, September 4, 2025
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
relative opto-PKR cell viability < 0.3 or >1.5 and a relative IMR-90 to wild-type H4 and Vero cells, with CC
50
values of ∼70 and
cell viability > 0.7, leading to a set of 3,599 compounds with pu- ∼100 μM, respectively. Because compounds IBX-200 through
tative ISR-activating (relative opto-PKR cell viability < 0.3) or ISR- IBX-207 are selective against opto-PKR cells in light and do
inhibiting (relative opto-PKR cell viability > 1.5) activity. We not exhibit collateral cytotoxicity, to distinguish these com-
chose these thresholds to prioritize selective and non-cytotoxic pounds from ISR activators that have tonic activity, we hypothe-
compounds, given that typical coefficient of variation values in sized that they comprise a unique modality of ISR-modifying
our cell viability measurements were <10%, and ISRIB, 2BAct, compounds—ISR potentiators.
and SP600125 treatment at ∼10 μM resulted in similar effect
sizes (Figures 1H, 1I, 1M, and S1B). Repeating the experiment Phenotypic characterization of compounds
measuring cell viability in duplicate for each of the shortlisted To investigate whether these compounds indeed increase ISR
compounds, we retained 306 compounds for which both repli- activity in the presence of diverse ISR-related stressors—and
cates validated for further study. not only in response to opto-PKR-induced activity—we first
co-treated cells with compounds and ISR-activating poisons.
Small molecules selectively increase cell death Thapsigargin and sodium arsenite have been used to induce
To identify compounds with selective ISR-modulating activity, ER stress and oxidative stress, respectively: thapsigargin inter-
we compared cell viability dose-response experiments in light feres with calcium homeostasis to deplete ER calcium and acti-
versus dark at concentrations ranging from 0.2 to 50 μM. Of vate PERK, whereas sodium arsenite activates HRI. 17,39–42 We
the shortlisted compounds, we found that compounds that again focused on one compound representing each structural
increased the viability of opto-PKR cells in light did so only at class—IBX-200, IBX-202, and IBX-204—and performed check-
limited concentration ranges (∼1–10 μM). However, 85 com- erboard cell viability measurements of wild-type H4 cells (not
pounds (0.02% of all compounds screened) potently and selec- containing opto-PKR) co-treated with stressor for 24 h. We
tively decreased the viability of opto-PKR cells in light, with found that the compounds synergistically induced cell death
selectivity windows—the ratio of the half-maximal effective con- with thapsigargin and sodium arsenite across a range of com-
centration (EC
50
) value in dark to that in light—greater than 10 pound and stressor concentrations (Figures 3A–3F). Consistent
(Data S1). Among these compounds, we focused on eight with with the observed cell death being ISR-associated, treatment
the highest selectivity windows (Figures 2D–2K). These com- with 20 μM ISRIB or 5 mM n-acetylcysteine, an antioxidant,
pounds—herein renamed from IBX-200 to IBX-207—were not largely rescued cells from thapsigargin and sodium arsenite,
acutely cytotoxic to opto-PKR cells in dark at concentrations respectively. Notably, typical concentrations of IBX-200, IBX-
up to 50 μM but exhibited EC
50
values ∼0.1 to ∼1 μM in light, 202, and IBX-204, at which cell viability substantially decreased
indicating strong selectivity. Notably, these compounds have in the true stressor experiments (∼10 μM), were higher than
not been previously characterized and share three distinct corresponding concentrations for opto-PKR cells (≤1 μM;
chemical scaffolds (Figure 2L). All eight compounds were Figures 2D–2K), suggesting that the ISR is more potently acti-
Lipinski-conforming, 35 exhibited molecular weights between vated in opto-PKR cells. Salubrinal also potentiated thapsigargin
370 and 550 Da, had calculated topological polar surface area and sodium arsenite against wild-type H4 cells, consistent with
(TPSA) values < 120 A˚ 2 and often <90 A˚ 2 —suggesting that its known mechanism of ISR activation 16 ; yet, underscoring
they likely penetrate the blood-brain barrier 36 —and displayed salubrinal’s single-agent cytotoxicity, we found cell viability
no pan-assay interference substructures (PAINS) or Brenk sub- decreases of ∼20% at the lowest concentration tested
structures, 37,38 which are associated with unfavorable pharma- (6.25 μM) in the absence of any stressor (Figure S2A), consistent
cokinetic properties (Figure 2M; Table S1). Furthermore, their Ta- with our dose-response experiments for opto-PKR cells in dark
nimoto similarity values were <0.2 with respect to any known (Figure 1K). Thus, salubrinal treatment did not decrease cell
ISR-modifying compound. Thus, these compounds represent viability selectively in these stressed cells.
chemical series of putative ISR-modulating small molecules Although our experiments have focused on H4 neuroglioma
with favorable drug-like properties. cells, the ISR is conserved across metazoan cells, and we antici-
Building on our characterization of these compounds in opto- pated that synergy with ISR-activating poisons would be recapitu-
PKR cells treated in dark, we investigated the cytotoxicity of lated in diverse cell types and species. Consistent with this hypoth-
these compounds against different cell types, including wild- esis, we found that our compounds were synergistic with
type H4, IMR-90, and Vero (African green monkey kidney epithe- thapsigargin against Vero cells (Figures S2B and S2C). Further-
lial) cells. We selected one compound to represent each struc- more, in addition to optogenetically, clustering of PKR may be
tural class—IBX-200, IBX-202, and IBX-204—and found that, induced chemically.4 3 To this end, we transduced H4 cells with a
across all three cell types, each compound exhibited half- chemically inducible PKR construct, mCherry-DmrB-PKR, using
maximal cytotoxic concentration (CC
50
) values > 200 μM after an inducible homodimer system (hereafter referred to as chem-
3 days of treatment, supporting that the discovered compounds PKR cells; Figure 3G). Treating chem-PKR cells with B/B homodi-
are largely not cytotoxic (Figures 2N and S2A). In contrast, merizer to induce PKR activation, we observed on-pathway
known ISR activators, including Sephin1, Raphin1, halofugi- increases in peIF2α, ATF4, and CHOP levels, as measured by
none, SP600125, C16, and CCT020312, exhibited CC
50
values immunofluorescence staining (Figures S2D–S2F). Consistent
largely ≤50 μM, and often in the single-digit micromolar range, with increased ISR activation leading to cell death in chem-PKR
across most or all tested cell types, indicating that these com- cells, we measured decreases in cell viability after treatment with
pounds are cytotoxic. Salubrinal was also modestly cytotoxic B/B homodimerizer for 24 h, and B/B homodimerizer treatment
Cell 188, 1–18, September 4, 2025 5
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
A B C
D E F
G H I
Figure 3. True stressor and chemically inducible PKR potentiation experiments
(A–C) Checkerboard cell viability measurements of wild-type H4 cells treated with IBX-200 (A), IBX-202 (B), and IBX-204 (C) in combination with thapsigargin for
induction of ER stress. Values are normalized against those corresponding to vehicle treatment only (bottom-right value of each checkerboard). Results shown
are representative of two biological replicates.
(D–F) Similar to (A)–(C) but for cells treated with IBX-200 (D), IBX-202 (E), and IBX-204 (F) in combination with sodium arsenite for induction of oxidative stress.
(G) Chemical dimerization of PKR with the chem-PKR construct.
(H) Cell viability measurements of wild-type and chem-PKR H4 cells treated with B/B homodimerizer. Values were normalized against those of DMSO (0.5%)
vehicle-treated chem-PKR cells, and error bars show the range of values obtained from two biological replicates.
(I) Checkerboard cell viability measurements of chem-PKR H4 cells treated with IBX-200, IBX-202, and IBX-204 in combination with B/B heterodimerizer for ISR
induction. Values are normalized against those corresponding to vehicle treatment only (bottom-right value of each checkerboard). Results shown are repre-
sentative of two biological replicates.
See also Figure S2.
by itself was non-cytotoxic against wild-type H4 cells at concen- (Figures 4A–4C). Cells treated with IBX-200 and IBX-202 ex-
trations below 500 nM (Figure 3H). Performing checkerboard cell hibited ∼2- to 3-fold increases in anti-ATF4 fluorescence—larger
viability assays as above with B/B homodimerizer combined with than that resulting from treatment with salubrinal—and ∼2-fold
IBX-200, IBX-202, or IBX-204, we found that the compounds increases in anti-CHOP fluorescence (Figures 4A–4C). In
potentiated cell death across a range of homodimerizer and com- contrast, cells treated with IBX-204 displayed less substantial
pound concentrations (Figure 3I). Altogether, these findings indi- fluorescence increases for both ATF4 and CHOP. These obser-
cate that our discovered compounds selectively enhance cell vations were qualitatively similar for opto-PKR H4 cells incu-
death across different cell types and modes of ISR induction, bated in dark; additionally, we found that these observations
including optogenetic clustering of PKR, chemical dimerization were robust to varying the treatment time and concentration,
of PKR, and thapsigargin and sodium arsenite treatment. as qualitatively similar changes in ATF4 and CHOP fluorescence
occurred after treatment with these compounds at 10 or 100 μM
Phenotypic mechanism of action for times between 1 and 30 h (Figures S3A and S3D). Additional
As IBX-200, IBX-202, and IBX-204 enhance cell death across immunofluorescence experiments labeling peIF2α and OPP in
different stressors, we aimed to further elucidate their mecha- treated wild-type H4 cells indicate that IBX-200 and IBX-202
nisms of action. We treated wild-type H4 cells with each of these modulate these factors to a lesser extent than their effects on
compounds at 100 μM, a concentration chosen to exceed the ATF4 and CHOP, with <1.6-fold increases in relative mean fluo-
levels required for observing cell-death-enhancing effects to rescence values after 24 h (Figure S3B). The increased levels of
result in ISR-related changes without additional stressors. peIF2α and OPP suggest that IBX-200 and IBX-202 may
Immunofluorescence imaging indicated that treatment with strengthen endogenous negative feedback from high ATF4
each compound increased ATF4 and, to a lesser extent, CHOP levels on the ISR and induce ATF4-associated increases in
6 Cell 188, 1–18, September 4, 2025
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
A B D E
C
F G H
I J K
Figure 4. Phenotypic effects of compounds
(A and B) Anti-ATF4 and CHOP fluorescence in the same single wild-type H4 cells in response to compound treatment. Cells were treated with either DMSO
(0.5%) vehicle or 100 μM of each indicated compound for 24 h, and results are representative of two biological replicates. Points indicate values for individual
cells, and values are normalized to the mean value of cells treated with vehicle (dashed lines). Cell counts for each group, from left to right: 1,513, 1,535, 1,215,
549, 1,568, and 1,425.
(C) Representative anti-ATF4 and CHOP fluorescence images from the experiment shown in (A) and (B). Scale bar, 20 μm.
(D and E) Similar to (A) and (B) but for single opto-PKR cells treated with 10 μM of IBX-200 or salubrinal and 25 nM thapsigargin and incubated for 24 h in dark. Cell
counts for each group, from left to right: 1,146, 820, 1,063, 831, 693, and 915.
(F and G) Relative ROS levels (F) and ATP levels (G) in bulk culture wild-type H4 cells treated with either DMSO (1%) vehicle or 100 μM of each indicated
compound, with the exception of 50 nM of thapsigargin, for 24 h. Data are from three (F) or two (G) biological replicates (black points), and bars shown mean
values.
(H) Proposed phenotypic mechanism of action of IBX-200, IBX-202, and IBX-204, with relevant components highlighted by blue arrows.
(I) Uniform manifold approximation and projection (UMAP) cellular transcriptomics plots for untreated opto-PKR cells and opto-PKR cells treated with DMSO
vehicle, IBX-200, IBX-202, IBX-204, or salubrinal (10 μM of each compound) in the presence of light for 1 and 3 h (1L and 3L, respectively) and in dark for 1 and 3 h
(1D and 3D, respectively). Pointers indicate centroids of all UMAP points for each population.
(J) Plots of relative mean expression for the top 20 differentially expressed genes in IBX-200-, IBX-202-, and IBX-204-treated cells for 3 h in light and 3 h in dark
relative to vehicle-treated cells. For comparison, the same genes in salubrinal-treated cells are shown. Dashed lines indicate no relative enrichment compared
with cells kept in dark.
(K) Plots of relative expression in single cells for four ISR-related genes in compound-treated cells for 3 h in light relative to 3 h in dark. Values are normalized to the
mean value of cells treated with vehicle for 3 h in dark (dashed lines). Cell counts for each group, from left to right: DDIT3, 115, 111, 67, 88, 77, 232, 79, 458, 178,
and 296; ATF4, 217, 158, 142, 167, 119, 317, 80, 497, 201, and 398; ATF3, 38, 33, 26, 26, 27, 161, 79, 493, 195, and 265; KLF6, 38, 40, 30, 29, 38, 187, 78, 435,
158, and 341.
See also Figure S3.
Cell 188, 1–18, September 4, 2025 7
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
protein production, consistent with prior work.4 4 In contrast, IBX- Molecular mechanism of action
204 treatment decreased mean peIF2α and OPP fluorescence Given that the compounds upregulate ATF4 and CHOP
after 24 h by 1.5- and ∼3-fold, respectively, suggesting that it (Figures 4A–4C), we first examined upstream components of the
might act on ISR-related feedback differently than do IBX-200 ISR to identify potential binding targets. We found that IBX-200
and IBX-202 (Figure S3C). and IBX-204 (but not IBX-202) selectively decreased GCN2’s ki-
Building on these results, we hypothesized that alterations in nase activity, with half-maximal inhibitory concentration (IC
5 0
)
ATF4 homeostasis are associated with increased sensitivity to values ∼50 μM (Figures 5A and S4A–S4D). IBX-202 did not reduce
ISR stress. Focusing on IBX-200, we repeated our immunoflu- GCN2 kinase activity, and cellular thermal shift assays (CETSAs)
orescence experiments and treated cells with low but synergis- identified no binding target for IBX-202 (Figure S4E). This con-
tic concentrations of IBX-200 (10 μM) and thapsigargin (25 nM) trasted with IBX-200 and IBX-204, for which two proteins (GPX4
for 24 h. We found that anti-ATF4 and anti-CHOP fluorescence and FECH) appeared as additional shared potential binding tar-
was only modestly (∼10%) increased by treatment with either gets. However, follow-up assays—including differential scanning
compound alone but, on average, increased >2-fold in the fluorimetry, enzymatic inhibition, and cell viability assays—indi-
presence of both compounds, similar to treatment with the cated that these proteins were not involved in ISR potentiation
combination of salubrinal and thapsigargin (Figures 4D and (Figures S4F–S4H; STAR Methods). Further studies revealed that
4E). These observations indicate that, in IBX-200-treated cells, IBX-202 chemically converts into an IBX-200-family compound
increased expression of ATF4 is associated with increased cell that may act on GCN2 similarly to IBX-200 (Figure S4I). We there-
death in the presence of a stressor. Prior work has shown that fore investigated GCN2 to study a plausible mechanism of action
forced expression of ATF4 increases protein synthesis, causing of all the compounds.
oxidative stress and ATP depletion in mouse embryo fibro- Human GCN2 is a complex, ∼190-kDa protein with multiple
blasts (MEFs).4 4 We additionally measured reactive oxygen functional pseudokinase and kinase domains. 46–48 GCN2 kinase
species (ROS) and ATP levels in cells treated with each of domain inhibitors, including GCN2iB and GCN2-IN-1, have pre-
IBX-200, IBX-202, and IBX-204 (Figures 4F and 4G). Dichloro- viously been characterized. 49–51 Nevertheless, we found that
fluoroscein staining suggested that wild-type H4 cells treated GCN2iB and GCN2-IN-1 do not increase cell death in opto-
with IBX-200 and IBX-204 for 24 h exhibited increases in PKR cells in the presence of light; neither do these compounds
ROS levels; cells treated with IBX-202, in contrast, did not— increase cell death in wild-type H4 cells in the presence of thap-
similar to treatment with salubrinal. In contrast, quantification sigargin and sodium arsenite (Figures S4J and S4K). These
of ATP levels indicated that ATP was decreased in cells treated divergent phenotypic results suggested that our compounds
with IBX-200, IBX-202, and IBX-204, similar to treatment with might act differently on GCN2 than do GCN2iB and GCN2-IN-
salubrinal. Despite potential compound-specific variation in 1. We therefore performed surface plasmon resonance (SPR)
altering cellular phenotypes, these findings suggest that IBX- measurements to further study this interaction, which indicated
200, IBX-202, and IBX-204 increase ATF4 and CHOP expres- that IBX-200 and IBX-204 selectively bound GCN2 with K
d
sion, resulting in ATF4- and CHOP-mediated sensitivity to thap- values of 25.2 and 3.2 μM, respectively (Figures 5B and S4L).
sigargin stress and ATP depletion as a hallmark of high ATF4 In contrast, IBX-202 did not bind GCN2, and GCN2iB bound
expression (Figure 4H). GCN2 with a lower K
d
value of 1.7 μM. These findings were qual-
To further investigate compound-induced phenotypes, we itatively consistent with our kinase activity measurements in
performed a single-cell transcriptomic analysis of opto-PKR that they indicated binding; nevertheless, the lower K
d
values
cells treated with each of IBX-200, IBX-202, and IBX-204 at of IBX-200 and IBX-204 relative to their kinase inhibition IC
5 0
10 μM in light and in dark (Figures 4I and S3E). Distinct alter- values suggested that kinase inhibition might be auxiliary to
ations to population-averaged transcriptomes occurred in compound binding. Additional molecular docking simulations
response to both light and compound treatment (Figure 4I), using AutoDock Vina and AlphaFold3’s prediction of GCN2’s ter-
with DDIT3 (CHOP) showing substantial (>2-fold) enrichment tiary structure 52,53 suggested the specific hypothesis that bind-
relative to DMSO in compound-treated cells in light—in ing occurs proximal to an activating C-lobe subdomain—result-
contrast to salubrinal, for which no similar enrichment was ing in phosphorylation at Thr899, a canonical active form of
observed (Figure 4J). Additionally, salubrinal-treated cells GCN2 54–56 (Figure 5C; STAR Methods).
kept in dark overexpressed SLC2A1, SLC7A5, SLC3A2, As IBX-200 and IBX-204 might activate GCN2 to confer their
HERPUD1, and CYP1B1 (Figure S3E), whereas IBX-200-, phenotypic effects on stressed cells, we engineered a knockout
IBX-202- and IBX-204-treated cells did not, consistent with sa- (KO) of EIF2AK4 (GCN2) in opto-PKR H4 cells for cell viability as-
lubrinal exhibiting a different mechanism of action from these says. We first validated decreases in GCN2 protein levels,
compounds. Focusing on ISR-adjacent genes, we found that finding an ∼70% decrease in GCN2 levels in these cells
IBX-200-, IBX-202-, and IBX-204-treated cells in light also (Figure 5D). Repeating our experiments using optogenetic acti-
overexpressed ATF4, ATF3, and KLF6. 45 Consistent with the vation of PKR, we found that cell viability was increased after
selectivity of these compounds against stressed cells, the com- treatment with IBX-200, IBX-202, and IBX-204 in GCN2-KO cells
pounds had little discernable effect on these transcripts in cells compared with cells bearing opto-PKR only (Figure 5E). These
kept in dark (Figure 4K). Overall, these findings indicate that our cells exhibited an ∼20%–100% rescue of cell death across a
compounds upregulate ATF4 and DDIT3 (CHOP), along with range of compound concentrations. Intriguingly, although IBX-
those of several ISR-adjacent genes, in an ISR-pathway-spe- 202 was not evidenced to target GCN2 in our experiments,
cific manner. decreasing GCN2 levels partially rescued opto-PKR cells from
8 Cell 188, 1–18, September 4, 2025
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
A B D F
C E G
Figure 5. GCN2 targeting of compounds and proposed mechanism of action
(A) GCN2 kinase activity of reconstituted GCN2 treated with each of the indicated compounds at the indicated final concentrations. Shown are the mean of two
biological replicates, and error bars indicate the full range of values measured.
(B) Binding affinity (K
d
) values against GCN2 for each of the indicated compounds, as measured by SPR. Values are inferred from curve fitting to one biological
replicate. Asterisks indicate a degenerate response curve (Figure S4L).
(C) Molecular docking poses for each of the indicated compounds and the predicted tertiary structure of GCN2. A schematic of various GCN2 domains is shown
at top. Binding affinities were calculated from AutoDock Vina (see STAR Methods), and compounds are shown in different colors.
(D) GCN2 protein levels in baseline (opto-PKR) and GCN2-KO cells. Bars indicate the mean of three biological replicates, and error bars indicate the full range of
values measured.
(E) Cell viability dose-response curves for opto-PKR and opto-PKR GCN2-KO cells treated with IBX-200, IBX-202, and IBX-204 for 24 h in light (cyan and blue
points, respectively). Points indicate the means of two biological replicates. Values were normalized against those of DMSO (0.5%) vehicle-treated opto-PKR
cells in light. Differences in cell viability are highlighted in purple.
(F) Ratios of pGCN2 Thr899 to total GCN2 levels in opto-PKR cells treated with the indicated compounds for the indicated durations in light (blue and cyan bars)
and in dark (gray and black bars), as measured by AlphaLISA. Values are normalized to those of DMSO (0.5%) vehicle and represented in log
10
. Results are
representative of one of two independent experiments performed on different occasions.
(G) Proposed mechanism of action of IBX-200 and IBX-204 (as well as cyclized forms of IBX-202 resulting in IBX-200 analogs). Additional mechanisms may
contribute to the observed activity.
See also Figure S4.
IBX-202 treatment as well, consistent with IBX-202’s conversion Building on our observations, we directly measured levels of
into an IBX-200 analog. Importantly, in GCN2-KO cells, all com- GCN2 phosphorylated at Thr899 (pGCN2 Thr899) in opto-PKR
pounds continued to enhance cell death compared with light and cells treated with each of IBX-200, IBX-202, and IBX-204
vehicle-only treatment but only at higher concentrations (>1 μM). (Figure 5F). These measurements indicated that GCN2 was
This observation suggests that residual GCN2 levels, compen- activated in opto-PKR cells treated with varying concentrations
satory or cooperative activation of other stress sensor kinases, 2 (0.4–40 μM) of compound, with ∼2- to 6-fold increased ratios
or other uncharacterized targets might contribute to cell death, of pGCN2 Thr899 to total GCN2 levels 3 h post treatment and
especially at higher compound concentrations. Indeed, consis- higher ratios observed in cells co-treated with blue light. Impor-
tent with these possibilities, we found that ATF4 and CHOP tantly, these results demonstrate that compound treatment at
levels were still increased in GCN2-KO cells after compound sub-K
d
concentrations activates GCN2, consistent with the low
treatment (Figure S4M). Additional kinase binding panels and cell-based EC
50
values observed in our opto-PKR experiments.
the observation of no differential change in cell viability in PKR/ To further test the role of activated GCN2 independently of opto-
GCN2 double-KO opto-PKR H4 cells relative to GCN2-KO cells PKR, we co-treated chem-PKR cells with GCN2iB (10 μM) in the
further support that IBX-200 and IBX-204 act selectively on presence of B/B homodimerizer (1 nM) and IBX-200 or IBX-204.
GCN2 (Figures S4N and S4O). We observed rescue of cell death similar to co-treatment with
Cell 188, 1–18, September 4, 2025 9
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
2BAct (10 μM; Figure S4P), supporting that GCN2 is a functional ZKV (and for IBX-200 and IBX-202 against RSV) than HSV-1. This
target of IBX-200 and IBX-204. overall difference in potency might be explained in part by PKR’s
Together, our results suggest a proposed mechanism in which sensing of dsRNA and the fact that dsRNA intermediates are
IBX-200 and IBX-204 (as well as cyclized forms of IBX-202 result- generated as part of the replication process of ssRNA viruses
ing in IBX-200 analogs) potentiate the ISR in part by increasing the (as opposed to being generated by a different mechanism
active form of GCN2 (Figure 5G). Compound binding proximal to thought to involve bidirectional transcription in the case of
the C-lobe of GCN2 may contribute to activation of GCN2, as dsDNA viruses 60 ). Although further work is needed clarify how
measured by trans-autophosphorylation at Thr899. This is consis- the replication of different viruses is affected by ISR potentiation,
tent with the observation that a single amino acid mutation (R794G) these findings consistently suggest that IBX-200, IBX-202, and
in GCN2 has been shown to make it hyperactive by ∼75-fold,5 4 IBX-204 represent structural classes of compounds with selec-
suggesting that pharmacologic modulation may sustain GCN2 tive and broad-spectrum antiviral activity.
activation at low compound concentrations. Canonically activated
GCN2 (pGCN2 Thr899)5 4,55 results in ISR signaling, leading to in- In vivo efficacy in a mouse model of ocular herpesvirus
creases in ATF4 and CHOP expression.1 –3 In the presence of infection
ISR stress, the compounds increase ATF4 expression to poten- We next tested for efficacy in treating viral infections in vivo. For
tiate terminal ISR signaling, thereby decreasing cell viability; in our initial experiments, we focused on testing the most potently
the absence of stress, increases in ATF4 lead to an adaptive ISR, antiviral compound, IBX-200, in a mouse model of ocular
manifesting in no substantive decrease in cell viability. It is also herpesvirus infection 16 (Figure 6B), a well-established viral infec-
important to underscore that cell viability decreases are observed tion model. 61,62 C57BL/6J mice were treated topically with
in GCN2-KO cells incubated in light. Given that IBX-200 and IBX- vehicle, IBX-200 (10 mM), or acyclovir (10 mM) eyedrops daily,
204 heighten oxidative stress, which is also known to activate starting after infection. On the day of infection, scars were in-
HRI and PERK1 –3 and potentially ATF4,5 7 it is possible that com- flicted on the right corneas and each eye was infected with
pound treatment alters phenotypes (including cellular redox state) ∼10 5 PFU of HSV-1 strain KOS. Overall disease burden was
sensed by ISR components to indirectly and further activate the not severe in this model, consistent with previous work 61 ; never-
ISR, and GCN2 may be redundant for sensing the stress imparted theless, we found that mice treated with IBX-200 exhibited
by the compounds. improved disease scores compared with vehicle treatment,
similar to treatment with acyclovir (Figure 6C). We titered viral
Broad-spectrum antiviral activity PFUs from tear swabs collected at 3 days post infection and
Viral stress is detected by PKR.2 ,3 Small-molecule activators of the found that, despite variability in PFU/mL values, IBX-200 treat-
ISR, including salubrinal and Sephin1, have been shown to ment significantly reduced the average viral titer by approxi-
decrease viral replication,1 6,58 and viral infection has been shown mately 5-fold (Figure 6D). Acyclovir treatment also resulted in
to increase ATF4 signaling.5 9 Building on these observations, we similar mean decreases in PFU/mL relative to vehicle. Addition-
hypothesized that ISR potentiators could inhibit viral replication ally, we observed mean decreases of ∼20% in the levels
without collateral cytotoxicity. To investigate this hypothesis, we of CXCL10/IP-10, a chemokine expressed during HSV-1 infec-
focused on herpes simplex virus type 1 (HSV-1) strain KOS, Zika tion,6 3 in the eye homogenates of IBX-200 and acyclovir-treated
virus (ZKV) strain MR766, and respiratory syncytial virus (RSV) mice as compared with vehicle-treated mice, consistent with
strain B WV/14617/85. These viral strains were chosen as a start- potentially decreased inflammation and the lower mean disease
ing point to sample diverse viruses: HSV-1 is a double-stranded scores in these mice (Figure S5E). These results indicate that
DNA (dsDNA) virus, whereas ZKV and RSV represent different pos- IBX-200 is effective at decreasing HSV-1 titers in vivo and sug-
itive-sense and negative-sense families of single-stranded RNA gest that the discovered compounds may be further developed
(ssRNA) viruses. for the therapeutic treatment of viral infections.
We infected host cells with each virus and treated the infected
cells with varying concentrations of compound, finding that, Toxicology and structure-activity relationship analyses
across all viruses, compound treatment largely decreased viral As a preliminary step toward further development, we character-
plaque-forming units (PFUs). Most antiviral IC
50
values were be- ized hemolysis, iron chelation, genotoxicity, and liver damage
tween ∼1 and ∼100 μM, indicating that these compounds main- markers induced by IBX-200, IBX-202, and IBX-204 treatment,
tain selectivity against viruses relative to their mammalian cell finding favorable toxicity profiles for all compounds (Figures
CC
50
values (Figures 6A and S5A–S5D). For HSV-1, plaques S6A–S6E; STAR Methods). We next performed structure-activity
formed in the presence of compound were consistently smaller relationship (SAR) analyses of the three scaffolds shown in
than untreated controls, indicating that the compounds specif- Figures 7A–7C, which generalize the three structural classes of
ically impair viral replication rather than initial host cell entry compounds identified in this study. By varying the functional
(Figure S5A). IBX-204 decreased HSV-1 titers less effectively groups of the 1-(3-aminothieno[2,3-b]pyridin-2-yl)ethanone, nico-
than IBX-200 and IBX-202 and failed to decrease RSV titers at tinonitrile, and quinoline/1,2,4-oxadiazole-containing scaffolds as
concentrations as high as 100 μM. This reduced antiviral effect shown, we procured and tested 95, 72, and 36 chemical analogs of
may stem from IBX-204’s weaker ability to elevate ATF4 levels IBX-200, IBX-202, and IBX-204, respectively (Data S2). In dose-
at early incubation times, as supported by our immunofluores- response experiments measuring the selective killing of opto-
cence data (Figures 4A–4C). In contrast, all compounds were PKR H4 cells incubated in light as opposed to dark, we found
similarly effective and more potent (IC
50
values < 10 μM) against that 14, 6, and 13 compounds in each respective structural group
10 Cell 188, 1–18, September 4, 2025
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
A
B C D
Figure 6. Antiviral activity of compounds
(A) Antiviral IC
50
values for IBX-200, IBX-202, and IBX-204 against three viruses. Values were inferred by curve fitting for data generated from two biological
replicates (Figures S5B–S5D). Asterisks indicate values ≥100 μM.
(B) Schematic of the in vivo study. Mice were ocularly infected with ∼10 5 PFU of HSV-1 strain KOS, then treated with vehicle (70% DMSO:30% PBS), IBX-200, or
acyclovir eyedrops daily after infection. Thirty mice (10 for vehicle, 10 for IBX-200, and 10 for acyclovir) were used in the study.
(C) Distribution of disease scores 2 days post infection for all mice, where scores of 1 indicate symptomatic viral infections (see STAR Methods for details). Two-
sample exact permutation test for lower mean disease score relative to vehicle: *p < 0.05.
(D) Distribution of viral PFU/mL in tear swabs 3 days post infection for all mice. Boxplots indicate 25 th percentile, median, and 75 th percentile values, whiskers
indicate minimum and maximum values, and points indicate outliers. Red dashed lines indicate mean values. Two-sample exact permutation test for lower mean
PFU/mL relative to vehicle: *p < 0.05.
See also Figures S5, S6, and S7.
exhibited high potency against cells incubated in light (EC
5 0
< 1 μM) ory formation. 3 The compounds discovered here may be appli-
as opposed to dark (CC
5 0
> 50 μM; Figures 7D–7F; Data cable to diseases driven by loss of homeostasis, which, in addi-
S2). Several compounds exhibited lower EC
5 0
values against tion to viral infections, may include cancer, metabolic disorders,
cells in light than did IBX-200, IBX-202, and IBX-204, respectively and neurodegeneration. Inhibition of the ISR transforms mouse
(Figure S7A). Notably, IBX-210, IBX-211, and IBX-212 (Figures 7G– fibroblasts and increases tumor formation in immunodeficient
7I) were chemically diverse and highly selective analogs, with mice, 3 while oncogenic stress also activates the ISR. 64 ATF4 is
corresponding EC
5 0
values between 200 and 500 nM. Further- frequently upregulated in cancer cells 57 and has context-depen-
more, we tested the antiviral activity of multiple selective structural dent pro-survival and pro-apoptotic effects. Using ISR potentia-
analogs representing each scaffold and found that these analogs tors to selectively trigger apoptosis of these stressed cells may
were also effective at reducing HSV-1 replication in vitro permit a disease-modifying approach to cancer. Additionally,
(Figure S7B). Taken together, these results indicate that the chem- the ISR regulates amino acid metabolism and oxidative stress
ical series described in this study can be further optimized for responses, 1,3,65 and aberrant ISR phenotypes have been shown
higher potency, increased efficacy in disease models, and poten- to lead to neurodegeneration. 66,67 Selectively targeting stressed
tially other favorable medicinal chemistry properties. cells in these contexts may help to ameliorate disease
pathology.
DISCUSSION Our findings indicate that putative ISR potentiators are effec-
tive against different viruses, including HSV-1, ZKV, and RSV.
Dysregulation of the ISR contributes to numerous diseases, and In contrast to cancer, metabolic disorders, and neurodegenera-
the ISR has been viewed as a rheostat important to fundamental tion, viral infections can be acute, and developing drug candi-
processes, including cellular homeostasis and long-term mem- dates capable of treating systemic viral infections, including
Cell 188, 1–18, September 4, 2025 11
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
A B C
E
D F
G H I
Figure 7. Structure-activity relationship analyses
(A–C) Functional group modifications (R1–R4) to three scaffolds considered in our analyses.
(D–F) Rank-ordered EC
50
values for all tested structural analogs against opto-PKR cells incubated in light in the presence of compound for 24 h. Red bars indicate
selective compounds for which EC
50
< 1 μM in light and CC
50
> 50 μM in dark. Results are representative of one biological replicate.
(G–I) Cell viability dose-response curves for opto-PKR cells treated with selective and structurally diverse compounds from each of (D)–(F). Cells were incubated
for 24 h in light or in dark (cyan and black points, respectively). Colored points represent the means of two biological replicates (gray points). Values were
normalized against those of DMSO (0.5%) vehicle-treated cells in dark, and the dashed line indicates the baseline cell viability value of vehicle-treated cells in
light. Decoupled cell viability decreases are highlighted in red.
See also Figure S7.
those leading to viral encephalitis, remains a challenge. Target- spaces of ISR modulators remain to be discovered. These com-
ing the ISR as a highly conserved host cell stress response to pounds may exhibit less cytotoxicity and fewer pleiotropic effects
viral infection offers an attractive avenue toward developing than known small-molecule modulators of the ISR, several of
broad-spectrum antiviral compounds. Because they modulate which have been appreciated to have questionable mechanisms
host cell phenotypes without collateral cytotoxicity and do not of action.7 0,71 The optogenetic platform developed in this study al-
directly target viral nucleic acid replication, ISR potentiators lows us to activate and target the ISR in an on-pathway, tunable,
can promote organismal homeostasis and avoid antiviral resis- and time-resolved manner, overcoming the disadvantages of
tance. Indeed, due to these features, host-directed antiviral administering small-molecule stressors to cells. Although we
compounds have been a long sought-after modality of drug can- have not leveraged this feature as part of our screening, our plat-
didates. 68,69 We anticipate that further studies of ISR potentia- form also enables dynamic control of the ISR, which may be rele-
tors as antiviral drug candidates will lead to additional insights vant to simulating the chronic stress that underlies neurodegener-
on the phenotypic effects of these compounds and how these ef- ative and other diseases.2 ,72,73 Due to their selectivity against
fects translate to disease modification. stressed cells, the compounds discovered here might be effica-
More broadly, the structural dissimilarity and mechanisms of ac- cious when administered at low doses chronically, similar to previ-
tion of the compounds identified here, as compared with known ously considered ‘‘hit-and-run’’ dosing regimens for senolytics, for
compounds that modulate the ISR, suggest that vast chemical which selectively killing a subpopulation of senescent cells suffices
12 Cell 188, 1–18, September 4, 2025
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
to be disease modifying.7 4,75 Thus, optogenetic manipulation of- Limitations of the study
fers a broadly applicable approach for precisely controlling cellular Although our engineered optogenetic construct, opto-PKR, re-
stress states in vitro, significantly enhancing the identification of sponds specifically to blue light and our approach identifies ISR
therapeutic agents. modulators, it is possible that blue light can activate other cellular
Our optogenetic platform is phenotypic by design: this en- pathways, induce cell cytotoxic effects, or generate ROS to
ables the discovery of previously unknown mechanisms of ac- contribute to ISR signaling.9 5–98 Although the intensity of light
tion but requires downstream target deconvolution. Although required to activate opto-PKR is relatively low, at ∼100 μW/cm2
we have characterized GCN2 activation as a factor relevant to (three to four orders of magnitude lower than required for typical
the mechanism(s) of action of the identified compounds, detailed confocal imaging of fluorescent proteins), we cannot completely
studies are needed to fully elucidate the specificity of target discount the possibility of these and other off-target effects
engagement. Crystal structures of IBX-200 and IBX-204 in com- caused by light exposure. These possibilities emphasize the
plex with GCN2 would further support our proposed model of importance of performing detailed control experiments to validate
GCN2 binding proximal to the C-lobe, and GCN2 agonism and any optogenetic tool before deploying it in large screens and of
hyperactive mutant studies could enable more detailed explora- mechanistically validating any identified hit compound. Our
tions of compound effects. Functional CRISPR screens 76 incor- construct also relies on clustering of PKR, and how well optoge-
porating measures of ISR pathway activation as readouts may netic control generalizes to other proteins and pathways will
identify alternative targets. More recent technologies, such as vary depending on how well optogenetic induction can mimic
photocatalytic proximity labeling, 77 could enhance target decon- physiological activation. For many proteins, we anticipate that
volution sensitivity, further clarifying the mechanisms of action of the development and characterization of specific optogenetic
the compounds identified here. constructs is needed to address this issue. Finally, the ISR has
Overall, our findings suggest that optogenetics, a technique still been implicated in many diseases due to its role as a highly
nascent for many biological applications,2 3,78–84 can be leveraged conserved and central cellular stress response,2 ,3 but drug candi-
to identify classes of ISR-modifying compounds. We anticipate dates that modulate the ISR should be tested for efficacy on a dis-
that compounds modulating other pathways (for instance, Wnt/ ease-by-disease basis to further support this hypothesis.
β-catenin and Ras/Erk signaling) in unexpected ways remain to
be discovered using similar optogenetic approaches.7 8,85–87 RESOURCE AVAILABILITY
These pathways are known for their molecular complexity,
context-dependent activity, and rich temporal dynamics. Tradi-
Lead contact
Further information and requests for resources should be directed to, and will
tional activation methods often involve compounds with pleio-
be fulfilled by, the lead contact, James J. Collins (jimjc@mit.edu).
tropic effects (e.g., lithium for Wnt/β-catenin signaling), but
optogenetics provides unique advantages—such as enhanced Materials availability
specificity, precise timing, and spatial control—which could Cell lines generated in this study are available on request, but we may require a
address these challenges. Additionally, the use of optogenetics materials transfer agreement and/or payment if there is potential for commer-
to simultaneously activate multiple signaling pathways would be cial application.
an attractive approach to studying the crosstalk and combinatorial
effects of these pathways, and leveraging orthogonal light-respon-
Dat
•
a a
A
n
ll
d
d
c
a
o
ta
d e
re p
a
o
va
rt
i
e
la
d
b
in
il i
t
t
h
y
is paper will be shared by the lead contact upon
sive systems (e.g., PhyB and Cry2) would allow for the precise con-
request. Data from single-cell RNA sequencing reads have been
trol of different pathways with distinct wavelengths of light.8 8 deposited on BioProject under accession PRJNA1213751 (BioSample
Elegant advances in engineering phytochrome-based optogenetic accessions SAMN46345881, SAMN46345882, SAMN46345883, and
tools, including ΔPhyA (REDMAP)8 3 and Fn-/Pn-BphP (REDLIP),8 9 SAMN46345884).
have demonstrated high (>150-fold) induction of target genes, • This paper does not report original code.
rapid response times (seconds), deep tissue penetration, long-
• Any additional information required to reanalyze the data reported in this
paper is available from the lead contact upon request.
duration stimulus memory (tens of hours), and reduced phototox-
icity. Such systems could enhance the discovery of selective mol-
ecules against intended signaling pathways, reducing potential ACKNOWLEDGMENTS
confounding factors (such as blue light phototoxicity or unintended
off-target effects) and enabling precise spatiotemporal and in vivo We thank Neosome Life Sciences for assistance with in vivo experiments,
MBC BioLabs for assistance with instrumentation, and Shannon Bryant
analysis.
for assistance with SPR experiments. J.M.U.V. was supported by the
Recent works have emphasized the importance of generating
BioPACIFIC Materials Innovation Platform of the National Science Foundation
high-quality on-pathway data, free of confounding variables, for under award no. DMR-1933487. J.J.C. was supported by the Defense Threat
productive drug discovery efforts, especially those leveraging ma- Reduction Agency (grant number HDTRA12210032). M.Z.W. was supported
chine-learning approaches and recent screening modalities.9 0–92 by the US Army Research Office under contract W911NF-19-D-0001 and
Optogenetics—and, more broadly, synthetic biology—enables cooperative agreement W911NF-19-2-0026 for the Institute for Collaborative
control over biological systems that will help to generate accurate
Biotechnologies.
phenotypic data. As a field originating from the phenotypic control
of bacteria over two decades ago,9 3,94 synthetic biology may be
AUTHOR CONTRIBUTIONS
particularly well-suited to enabling next-generation phenotypic F.W. conceived research, performed or directed all experiments, wrote the
approaches to drug discovery. paper, and supervised research. A.L., S.O., R.S.L., J.N., Y.R., and S.P.B.
Cell 188, 1–18, September 4, 2025 13
Please cite this article in press as: Wong et al., Optogenetics-enabled discovery of integrated stress response modulators, Cell (2025), https://
doi.org/10.1016/j.cell.2025.06.024
ll
Article
conceived research and performed experiments. V.S. performed data anal- ○ Chemical analogs and synthesis
ysis. B.R.L., T.B., E.D., and J.R.R.R. performed experiments. J.M.U.V. contrib- • QUANTIFICATION AND STATISTICAL ANALYSIS
uted to the design of the optogenetic illumination system. S.W. assisted with
experiments. H.K. contributed to conceiving research and experiments. J.J.
C. supervised research. M.Z.W. conceived research, directed experiments, SUPPLEMENTAL INFORMATION
and supervised research. All authors assisted with manuscript editing.
Supplemental information can be found online at https://doi.org/10.1016/j.cell.
DECLARATION OF INTERESTS 2025.06.024.
F.W. and M.Z.W. are co-founders of Integrated Biosciences. J.J.C. is the Received: March 25, 2024
founding scientific advisory board chair of Integrated Biosciences and an Revised: January 21, 2025
academic co-founder and board member of Cellarity. F.W., A.L., S.O., R.S. Accepted: June 17, 2025
L., Y.R., S.P.B., V.S., B.R.L., H.K., J.J.C., and M.Z.W. may hold equity
interest in Integrated Biosciences. S.W. is an employee of Illumina Ventures. REFERENCES
F.W., A.L., S.O., R.S.L., S.P.B., B.R.L., and M.Z.W. have filed a patent based
on the results of this work. 1. Harding, H.P., Zhang, Y., Zeng, H., Novoa, I., Lu, P.D., Calfon, M., Sadri,
N., Yun, C., Popko, B., Paules, R., et al. (2003). An integrated stress
STAR★METHODS response regulates amino acid metabolism and resistance to oxidative
stress. Mol. Cell 11, 619–633. https://doi.org/10.1016/s1097-2765(03)
Detailed methods are provided in the online version of this paper and include
00105-9.
the following: 2. Pakos-Zebrucka, K., Koryga, I., Mnich, K., Ljujic, M., Samali, A., and Gor-
• KEY RESOURCES TABLE man, A.M. (2016). The integrated stress response. EMBO Rep. 17, 1374–
• EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS 1395. https://doi.org/10.15252/embr.201642195.
○ Cell culture 3. Costa-Mattioli, M., and Walter, P. (2020). The integrated stress response:
○ Viral culture From mechanism to disease. Science 368, eaat5314. https://doi.org/10.
○ Mouse models 1126/science.aat5314.
• METHOD DETAILS 4. Hetz, C., Zhang, K., and Kaufman, R.J. (2020). Mechanisms, regulation
○ Construction of opto-PKR cells and functions of the unfolded protein response. Nat. Rev. Mol. Cell
○ Illumination system for optogenetics Biol. 21, 421–438. https://doi.org/10.1038/s41580-020-0250-z.
○ Chemical compounds
5. Rabouw, H.H., Visser, L.J., Passchier, T.C., Langereis, M.A., Liu, F.,
○ Immunofluorescence staining and imaging
Giansanti, P., van Vliet, A.L.W., Dekker, J.G., van der Grein, S.G., Sau-
○ Image analysis and quantification
cedo, J.G., et al. (2020). Inhibition of the integrated stress response by
○ Cheminformatics, t-SNE, and similarity
viral proteins that block p-eIF2-eIF2B association. Nat. Microbiol. 5,
○ High-throughput screening
1361–1373. https://doi.org/10.1038/s41564-020-0759-0.
○ Cellular viability assay
○ Halofuginone with light pre-exposure 6. Ruggieri, A., Dazert, E., Metz, P., Hofmann, S., Bergeest, J.P., Mazur, J.,
○ True stressor experiments Bankhead, P., Hiet, M.S., Kallis, S., Alvisi, G., et al. (2012). Dynamic oscil-
○ Construction of chem-PKR cells lation of translation and stress granule formation mark the cellular
○ Chem-PKR activation response to virus infection. Cell Host Microbe 12, 71–85. https://doi.
○ Reactive oxygen species detection org/10.1016/j.chom.2012.05.013.
○ Cellular ATP detection 7. Emanuelli, G., Nassehzadeh-Tabriz, N., Morrell, N.W., and Marciniak,
○ Single-cell transcriptomics S.J. (2020). The integrated stress response in pulmonary disease.
○ HRI kinase assay Eur. Respir. Rev. 29, 200184. https://doi.org/10.1183/16000617.
○ PKR kinase assay 0184-2020.
○ PERK kinase assay 8. Watanabe, S., Markov, N.S., Lu, Z., Piseaux Aillon, R., Soberanes, S.,
○ GCN2 kinase assay Runyan, C.E., Ren, Z., Grant, R.A., Maciel, M., Abdala-Valencia, H.,
○ PP1 enzymatic assay et al. (2021). Resetting proteostasis with ISRIB promotes epithelial differ-
○ CETSA selectivity profiling assay entiation to attenuate pulmonary fibrosis. Proc. Natl. Acad. Sci. USA 118,
○ Differential scanning fluorimetry e2101100118. https://doi.org/10.1073/pnas.2101100118.
○ GPX4 and FECH studies 9. Chou, A., Krukowski, K., Jopson, T., Zhu, P.J., Costa-Mattioli, M., Walter,
○ Chemical conversion of IBX-202 P., and Rosi, S. (2017). Inhibition of the integrated stress response re-
○ Surface plasmon resonance verses cognitive deficits after traumatic brain injury. Proc. Natl. Acad.
○ Molecular docking simulations Sci. USA 114, E6420–E6426. https://doi.org/10.1073/pnas.1707661114.
○
○
○
○
○
G
K
M
M
G
i
e
C
e
e
n
n
a
a
a
N
e
s
s
s
2
r
u
u
e
a
iB
r
r
t
p
e
e
i o
m
m
a
p
n
n
h
e
e
e
a
o
n
n
l
r
f
t
t
m
e
s
s
G
x
a
o
o
p
C
c
f
f
e
N
o
G
p
r
l
2
i
G
o
m
C
g
a
C
N
e
i
n
c
N
n
2
d
t
2
a
s
a
P
n
n
T
t
K
d
h
a
R
r
g
P
8
o
K
9
K
n
9
O
R
is
p
m
c
p
r
e
r
o
o
e
l
t
l
t
e
x
l
e
i
p
i
n
n
in
e
e
l
r
s
e
l
i
e
m
v
v
e
e
e
l
n
s
l
ts
10. K
a
m
m
d
r
o
i
u
c
in
l
k
e
e
i
o
,
.
c
w
M
e
u
L
l
s
e
.
i
S
k
f e
i
c
.
,
,
o
9
K
E
g
,
.
l
,
i
n
e
z
N
i
6
a
ti
o
2
r
v
r
0
l
e
a
a
4
r
n
a
e
8
,
s
n
.
A
,
h
h
.
E
a
t
,
t
n
.
F
p
,
c
r
s
D
i
e
a
:/
e
r
s
/
l
d
,
g
r e
E
o
a
v
i
.
d
.
S
e
o
o
.
r
r
,
,
s
g
B
e
L
/1
s
.
o
,
0
o
B
a
.
n
7
g
e
e
5
e
r
,
n
5
-
M
a
r
4
e
l
/
e
.
l
e
,
a
s
L
U
t
,
e
i f
r
S
d
e
e
.
.
t
,
6
a
m
e
2
,
t
e
0
G
m
a
4
.
l
,
8
.
o
G
.
(
r
2
y
r
0
u
d
2
e
0
e
,
)
c
K
.
l
.
i
S
,
n
m
P
e
a
a
i
l
n
l
-
l
○ Viral plaque and proliferation assays 11. Moreno, J.A., Radford, H., Peretti, D., Steinert, J.R., Verity, N., Martin, M.
○ Mouse model of ocular herpesvirus infection G., Halliday, M., Morgan, J., Dinsdale, D., Ortori, C.A., et al. (2012). Sus-
○ CXCL10/IP-10 measurements tained translational repression by eIF2α-P mediates prion neurodegener-
○ Toxicity studies ation. Nature 485, 507–511. https://doi.org/10.1038/nature11058.
○ Hemolysis assay 12. Tribouillard-Tanvier, D., Be´ ringue, V., Desban, N., Gug, F., Bach, S., Vois-
○ Iron chelation assay set, C., Galons, H., Laude, H., Vilette, D., and Blondel, M. (2008). Antihy-
○ Ames genotoxicity assay pertensive drug guanabenz is active in vivo against both yeast and
○ Mouse AST/ALT measurements mammalian prions. PLoS One 3, e1981. https://doi.org/10.1371/jour-
○ Prior knowledge for identified compounds nal.pone.0001981.
14 Cell 188, 1–18, September 4, 2025
