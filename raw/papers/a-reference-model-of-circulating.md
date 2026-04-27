---
source_path: /mnt/c/Users/Administrator/Zotero/storage/XPDLC64L/s41591-025-03716-5.pdf
ingested: 2026-04-23
sha256: f784c78059427c51
---

nature medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
A reference model of circulating
hematopoietic stem cells across the lifespan
with applications to diagnostics
Received: 1 May 2024 N. Furer1,17, N. Rappoport2,3,17, O. Milman 3,17, S. Tavor4,5, A. Lifshitz 3,
A. Bercovich 3, O. Ben-Kiki3, A. Danin1, M. Kedmi6, Z. Shipony7, D. Lipson7,
Accepted: 11 April 2025
E. Meiri7, G. Yanai7, S. Shapira8, N. Arber8, S. Berdichevsky9, J. Tyner 10,11,
Published online: xx xx xxxx S. Joshi 10,11, D. Landau 12,13,14,15, S. Ganesan12,13,14,15, N. Dusaj 12,13,14,15,
P. Chamely12,13,14,15, N. Kaushansky1, N. Chapal-Ilani1, R. Shamir 2,
Check for updates A. Tanay 3,17 & L. Shlush 1,5,16,17
With aging, deviation of human blood counts from their normal range
accompanies the transition from health to disease. Hematopoietic stem
and progenitor cells (HSPCs) deliver life-long multi-lineage output, but
their variation across healthy humans with aging, and their diagnostic utility,
haven’t been characterized in depth thus far. To address this, we introduced
an HSPC reference model using single-cell RNA profiling of circulating CD34+
HSPCs from 148 healthy age- and sex-diverse individuals. We characterized
physiological circulating HSPC composition, showed that age-related myeloid
bias is predominant in older men and defined age-related transcriptional
signatures in lymphoid progenitors. We further demonstrated the potential
of this resource to facilitate the diagnosis of myelodysplastic syndrome (MDS)
from peripheral blood without bone marrow sampling, defining classes
of patients with MDS and abnormal lymphocyte, basophil or granulocyte
progenitor frequencies. Our resource provides insights into HSPC reference
ranges across the lifespan and has the potential to facilitate the clinical
applications of single-cell genomics in hematology.
The basis for understanding and defining human pathophysiologi- cells (HSPCs) has not been established so far. As HSPCs reside mainly
cal states is a detailed description of interindividual heterogeneity in the bone marrow (BM), access to these cells, especially in the healthy
among healthy individuals. Large population studies have identified population, has been problematic, whereas their general paucity in the
wide interindividual differences in complete blood counts (CBCs) of circulation made it quite challenging to characterize them efficiently
healthy individuals1 and exposed different age-related blood count from the blood. This has become feasible given modern technologies
changes, such as high red blood cell (RBC) distribution width (RDW), such as single-cell RNA sequencing (scRNA-seq).
macrocytic anemia and a reduction in absolute lymphocyte counts2. Individual heterogeneity in the frequency of circulating HSPCs
The establishment of reference values, or population-wide normal (cHSPCs) has been reported in the past and was linked to age, sex, smok-
ranges for certain blood parameters, has been crucial for patient evalu- ing status, lipid profiles and hereditary factors3, as well as to different
ation, diagnosis and treatment. pathological states4. Few studies have analyzed HSPC heterogeneity
Although CBC reference ranges are used in the clinic daily, the in higher resolution, but their sample size was limited5,6. Previous
equivalent reference range for hematopoietic stem and progenitor studies, including some based on scRNA-seq analysis7, demonstrated
A full list of affiliations appears at the end of the paper. e-mail: amos.tanay@weizmann.ac.il; liranshlush3@gmail.com
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
that most HSPC subpopulations can be identified in the peripheral (Extended Data Fig. 3c,d). Altogether, the data suggest that cHSPCs,
blood (PB)8 and functional stem cells were identified in the PB of mice9 although not fully reflecting BM hematopoiesis, can serve as a highly
and humans7. accessible proxy for hematopoietic dynamics.
We have developed a reference model for healthy cHSPC distribu-
tions and provided proof-of-concept evidence supporting potential HLF, GATA3, HOXB5 and TLE4 as HSC TFs
diagnostic applications. We applied scRNA-seq analysis to cHSPCs from One of the hallmarks of our cHSPC model is a distinct HSC state that
148 healthy age- and sex-diverse individuals, to capture a spectrum of is transcriptionally linked with two major differentiation gradients:
states, from hematopoietic stem cells (HSCs), through early common the first represents a continuum of common lymphoid progenitors
myeloid and lymphoid progenitor states and more specific progenitor (CLPs; subdivided into early (E) mid (M) and late (L) states). The second,
populations. All data can be explored in https://apps.tanaylab.com/ more common branch, represents multipotent progenitor (MPP) states
MCV/blood_aging. We discovered extensive interindividual heteroge- and their differentiation toward granulocyte–monocyte progenitors
neity in the frequency of cHSPC subtypes and found that these correlate (GMPs), erythrocyte progenitors (ERYPs) and basophil, eosinophil or
with certain CBC parameters, aging and the presence of clonal hemat- mast progenitors (BEMPs). Platelet contamination prevented precise
opoiesis (CH). We then developed tools for projecting new samples on megakaryocyte progenitor modeling (Extended Data Fig. 3e), such
our reference model and analyzed 73 additional samples from patients that states at the base of the myeloid trajectory were annotated as
with cytopenia and myelodysplastic syndrome (MDS), to demonstrate megakaryocyte, erythrocyte, basophil, eosinophil or mast progenitors
our model’s potential applications in MDS diagnosis. The healthy (MEBEMPs, subdivided into early (E) and late (L) states).
reference model and methodologies used in the present study provide Early HSCs are marked by high AVP and HLF expression and were
a framework for the deployment of single-cell genomics in hematology, previously shown to represent a rare cell population enriched with
for the diagnosis of MDS, and possibly other stem cell-related blood self-renewal capacity in both the BM and cord blood13. Our model
malignancies, from the PB, reducing the need for BM analysis. included data on 14,440 HLF and AVP expressing HSCs that could be
matched with cells from independent BM atlases14, suggesting that,
Results under a steady state, HSCs with potential self-renewal capacity are
HSPC states observed across humans in PB present in the PB (Extended Data Fig. 3f). Further functional studies
To evaluate interpersonal diversity in subtype distribution and regu- are needed to establish this finding. Together with HLF and AVP, we dis-
lation of cHSPCs, we combined multiplexed scRNA-seq, bulk DNA covered 14 genes expressed at least 1.75-fold higher in HSCs compared
genotyping and integrated clinical data (Fig. 1a). Multiplexing was with their 2 immediate differentiation branches (Extended Data Fig. 3g
resolved using SNPs identified in the 3′-UTR of cHSPCs’ RNA, facili- and Supplementary Table 2). We identified several transcription fac-
tating precise matching of cells to individuals and improving control tors (TFs) enriched in HSCs, including HOXB5, TLE4 and GATA3 (Fig. 1c).
for batch effects and doublets. Altogether, we collected cHSPCs from GATA3 was previously reported to regulate self-renewal in murine
79 men and 69 women between the ages of 23 years and 91 years long-term HSCs15. Its role in human HSCs has not been studied thus far.
(median 61.5 years) (Extended Data Fig. 1a and Supplementary Table 1). We note that, although the HSC state is defined by unique markers that
We performed deep targeted somatic mutation analysis to identify are symmetrically downregulated on exiting to the CLP and MEBEMP
cases of CH (Supplementary Table 1)10. After quality control and filter- trajectories (Fig. 1c), it also expresses several lineage-specific regula-
ing, we retained 840,104 single-cell profiles, which were normalized tors at intermediate levels, which are bifurcating anti-symmetrically
to control for sequencing-platform batch effects and combined to on exiting the HSC state to the CLP and MEBEMP trajectories (Fig. 1d
construct and annotate a metacell manifold model11 (Extended Data and Extended Data Fig. 3g). This may suggest that the multipotent
Fig. 1b,c). We retained 626,966 CD34+ single cells for downstream analy- capacity of HSCs is associated with intermediate expression of multiple
sis (Extended Data Fig. 1d). These formed a rich repertoire of states, regulators, which is resolved with differentiation.
associated with cHSPCs and their differentiation trajectories (Fig. 1b
and Extended Data Fig. 1e,f). The derived model recapitulated and BEMPs and NKTDPs are enriched in cHSPCs
deepened earlier characterization efforts of HSPC states from the BM. The cHSPC atlas was enriched for BEMPs. Although classic studies
We noted that, although we could not assume that cHSPCs fully reflect linked these cells with a GMP origin, more recent studies suggested that
BM HSPC dynamics, previous studies, as well as our own BM scRNA-seq these emerge, at least in part, from erythroid progenitors in both mice
comparisons, supported at least partial compatibility between the two12 and humans7,16. Our analysis identified a small population of metacells
(Extended Data Figs. 2 and 3a). One notable characteristic specific to linking BEMPs with their MEBEMP-L precursors (Fig. 1e). This high-
cHSPCs was, however, the repression of cell-cycle gene expression lighted TFs (Fig. 1f) and other factors (Extended Data Fig. 4a) positively
(Extended Data Fig. 3b), previously demonstrated by others7. Impor- or negatively regulated in this postulated early stage of BEMP speci-
tantly, we found our cHSPC model to be consistent across individuals. fication. Another interesting cHSPC population included lymphoid
The median number of individuals contributing cells to each metacell states with high ACY3 expression and intermediate-to-low DNTT levels,
was 84 and all metacells included cells from at least 47 individuals. a combination rarely found in human BM but present in PB (Extended
Expression differences between cell states were greater than between Data Fig. 4b). We observed co-variation of key T cell regulators within
individuals, limiting individually specific differential expression when this population and anti-correlation of these factors with some Hall-
controlling for each sample’s cell distribution over the atlas states mark plasmacytoid dendritic cell (pDC) regulators, as demonstrated
Fig. 1 | Mapping cHSPCs. a, Experimental design. b, Annotated two- their MEBEMP-L precursors. f, Positively and negatively regulated TFs involved
dimensional Uniform Manifold Approximation and Projection (UMAP) of our in early BEMP differentiation. g, Gene–gene plot of IRF8 against TCF7 expression
metacell manifold after filtration of metacells with low CD34 expression. as Hallmark markers of DC and T cell differentiation, respectively. The high
For all subsequent panels in Figs. 1–3, metacell color denotes cell state as here. ACY3 NKTDP metacell population of interest is depicted (dashed line). h, This
c,d, Symmetrical (c) and asymmetrical (d) regulation of specific HSC TFs on population exhibits high expression of both T cell and DC regulators, forming a
bifurcation to the CLP (right) and MEBEMP (left) lineages. Each panel shows gradient consisting of NK or T cell-like progenitors exhibiting a high TCF7:IRF8
the expression of one gene (y axis). Metacells in all panels are ordered (left to expression ratio along with high expression of other T cell Hallmarks such as CD7,
right) by increasing AVP expression in the MEBEMP lineage and decreasing AVP MAF, IL7R, TRBC2 and DC-like progenitors exhibiting a low TCF7:IRF8 expression
expression in the CLP lineage. The y axes denote log(fractional expression) of ratio, along with high expression of other DC Hallmarks, such as the myeloid TF
2
each gene. e, The metacell population of interest (dashed line) linking BEMPs to PU.1 and the MHC-II gene CD74. Panel a created with BioRender.com.
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
HSC
MPP
CLP-E
CLP-M
GMP
CLP-L
ERYP
MEBEMP-L
NKTDP
BEMP
c
–13 –14 GATA3 –14 HOXB5 –12 TLE4
–16 –17 –17 –16
HSC HSC HSC HSC
d
–13 TCF7L2 –13 RUNX3 –13 TAL1 –11 MYC
–16 –17 –16 –16
–10 HOPX –13 ZEB1 –11 GATA2 –11 MYB
–16 –16 –16 –16
–10 KLF6 –11 HOXA9 –12 NFE2 –13 PDLIM1
–15 –15 –16 –16
MEBEMP HSC CLP MEBEMP HSC CLP MEBEMP HSC CLP MEBEMP HSC CLP
Nature Medicine
)noisserpxe(gol
)noisserpxe(gol
2
2
HLF
MEBEMP CLP MEBEMP CLP MEBEMP CLP MEBEMP CLP
GATA2 CREB3L2
LMO2
POU2F2 TLE4
KLF1
)noisserpxe(gol
2
e f
log(HBD expression) 2
)noisserpxe
4OML(gol
2
–10 –12
–13
–8
BEMP early
–12
–15 –15
–12
–12
–13
–14 –15
–15
–15
–16 –10 –14 –7 –14 –7 –14 –7
log(LMO4 expression) log(LMO4 expression) log(LMO4 expression) 2 2 2
–13 NKTDP
–16
)noisserpxe
7FCT(gol
2
g h
–12 CD7 –10 MAF –12
–15 –16 –15 SPI1/PU.1
–12 TRBC2 IL7R –13 –8
–9
–15 –16
CD74 (MHC-II)
–16 –11 –4 +2 –4 +2 –4 +2
log(IRF8 expression) log(TCF7/IRF8) log(TCF7/IRF8) log(TCF7/IRF8)
2 2 2 2
)noisserpxe(gol
2
a b
Study cohort
1 ml for DNA Targeted sequencing
production genotyping + CH panels
×148
23–91 y + ears old 50 m p l a o ti f e P n B t per P1(98.34%)
Complete CBC PBMC Sample Magnetic bead- CD34+ fraction scRNA library prep
history isolation pooling based CD34 enriched from (10×) and
(Ficoll) enrichment 0.1% to >90% sequencing
(Illumina/Ultima) MEBEMP-E
Resource https://doi.org/10.1038/s41591-025-03716-5
by comparison of TCF7 and IRF8 expression (Fig. 1g,h and Extended Our previous work19 and the work of others20 correlated high RDW with
Data Fig. 4c). We therefore termed this population natural killer (NK) CH and predisposition to acute myeloid leukemia. Our data suggest
cell, T cell and DC progenitors (NKTDPs)17,18. To summarize, our map that reduction in CLP frequencies is associated with CH (Extended Data
of cHSPCs showed a rich spectrum of progenitor states, which refined Fig. 6a). A similar trend was suggested by genotyping of transcriptomes
previous analyses and a remarkable consistency of these states across (GoT)21 performed on one of our DNMT3A R882H cases, showing a
individuals. This provided an opportunity for deciphering interindi- lower fraction of CLP cells within the mutant clone (P < 0.005, Fisher’s
vidual hematopoietic variability based on our solid and quantitative exact test; Extended Data Fig. 6b). Although this trend was suggested in
definition of cHSPC subtypes. other GoT data22, sample size is insufficient to prove it statistically and
explore the clonal mechanisms underlying it. To further explore the
Interindividual variation in cHSPC state composition association between CH and RDW, we studied a cohort of 18,147 healthy
To study interindividual cHSPC variation, we first analyzed cell-state individuals for whom we had both longitudinal CBCs and DNA avail-
compositions by quantifying cell-state relative frequencies within each able. We identified 602 individuals with a high RDW (>15%, not meeting
individual’s single-cell ensemble (Fig. 2a). These frequencies varied minimal criteria for MDS diagnosis) and 602 age- and sex-matched
extensively between individuals as shown in Fig. 2b. For example, HSCs normal RDW controls. We performed deep targeted sequencing to
and CLP-Ms, representing 2.4% and 12.6% of the CD34+ population on identify leukemia-associated mutations on both high-RDW individuals
average, showed s.d. values of 1.0% and 6.8%, respectively. The abun- and controls, and found a significant enrichment of CH+ cases in the
dant MPP and MEBEMP-E states (mean frequencies of 20.7% and 37.6%) high-RDW group (Fisher’s exact test, P < 0.002; Fig. 2f and Supplemen-
showed smaller relative variations (s.d. values of 4.9% and 5.8%, respec- tary Tables 3 and 4). Altogether, the data suggest associations across
tively). To analyze the stability of cell-state frequencies across time decreased CLP frequencies and elevated RDW and CH. Determination
and sampling instances, we re-sampled 20 individuals 1 year after their of the existence of a direct (and perhaps three-way) linkage for these
original sampling date. Both CLP (CLP-E, CLP-M, CLP-L and NKTDP) and variables requires further investigation.
MEBEMP (MEBEMP-E, MEBEMP-L, ERYP and BEMP) frequencies were
stable within the same individual across time (Fig. 2c). Age-related myeloid bias is predominantly observed in men
To analyze composition in higher resolution, we profiled each indi- Analysis of age-linked compositional changes in cHSPCs within
vidual’s enrichment over the CLP and MEBEMP trajectories. Clustering CH-negative individuals showed a remarkable increase in myeloid
of these enrichment profiles yielded six archetypes of cHSPC composi- (MEBEMP) to lymphoid (CLP) progenitor ratios in men (when compar-
tion within the healthy population (classes I–VI, Fig. 2d). These were ing <50 to >60-year-old individuals; Fig. 3a and Extended Data Fig. 6c).
composed of individuals with relative lymphoid enrichment (classes I This effect was insignificant in women. Of note, although both men and
and II) or depletion (classes V and VI), further subdivided by a stemness women experience a decline in lymphocyte counts with aging, it occurs
gradient, enriched in classes II, IV and VI and depleted in classes I, III and at an older age in women, as confirmed by recent analyses2. Notably,
V. Analysis of technical and biological replicates confirmed this varia- women show a temporary postmenopausal surge in lymphocyte counts,
tion to be robust and individual-specific (Extended Data Fig. 5a,b). To which delays their decline. Within the MEBEMP differentiation trajec-
summarize, we constructed cHSPC subtype normal reference ranges tory, aging was correlated with over-representation of more differen-
and showed that, although HSPC cell states are consistent among tiated states, once again only in men (Fig. 3b). Of note, the frequency
healthy individuals, their compositions are highly variable. of cHSCs did not significantly change with age (Fig. 3c). Although
previous studies suggest that aging is linked with an increase in HSC
Circulating HSPC frequencies correlate with CBCs and CH frequency23,24, this was not observed with the restrictive definitions
To extract an initial clinical annotation for the observed interindi- employed in the present study. We further identified an age-related
vidual variation in cHSPC state frequencies, we correlated individual decline in CD34+ HSPC frequency in a cohort of 1,000 healthy individu-
compositions with longitudinal CBC data (Methods). We observed als undergoing peripheral blood mononuclear cell (PBMC) scRNA-seq25
a significant positive correlation (P < 0.01) between PB mature lym- (Fig. 3d and Extended Data Fig. 6d), which has also been reported by
phocyte counts (%) and CLP frequencies (Fig. 2e, left). Given the high fluorescence-activated cell sorting (FACS) in the past3. The sex-specific
variability in female RBC counts and volumes during menstruation, correlation between age and cHSPC myeloid bias could be related to
pregnancies and prolonged perimenopausal periods, we analyzed RBC cell intrinsic properties, such as male-specific leukemia-associated
indices (count, hematocrit (HCT), mean corpuscular volume (MCV) mutations predisposing to myeloid differentiation26. This is less likely
and RDW) separately for men and women. We observed a significant because canonical CH-positive cases were excluded from this analysis.
negative correlation (P < 0.02) between CLP frequencies and HCT Alternatively, this predominantly male myeloid bias could be related
(men, Fig. 2e, middle) and a significant positive correlation (P < 0.01) to cell extrinsic factors such as age-related hormonal and BM micro-
between increased RDW and relative CLP depletion (men, Fig. 2e, right). environmental changes27,28.
Fig. 2 | Normal cHSPC composition. a, Characterization of interindividual in healthy individuals. The dashed lines represent the median (black) and the
cHSPC compositional variation and its correlation to clinical parameters 5th and 95th percentiles (gray) of the studied population. Bottom: cell-state
(scheme). b, Boxplots of cHSPC state frequency distributions across 148 enrichment map over 15 differentiation bins (rows), for all studied individuals
healthy individuals (logarithmic scale). The percentage was calculated from (columns) clustered into six classes (Methods). Classes I and II represent
all CD34+ cells within each individual’s single-cell ensemble. Boxplot centers, individuals relatively enriched in lymphoid progenitors, whereas classes V
hinges and whiskers represent the median, first and third quartiles and 1.5× the and VI represent individuals with relative depletion of lymphoid progenitors.
interquartile range, respectively. Outliers are marked by circles. The numbers Individuals are sorted by stemness within each class. Age and sex are denoted
represent the mean ± s.d. for each distribution. c, Comparison of cell-state for each individual. e, CBC correlations to cell-state frequencies: %lymphocytes
frequencies between 19 biological replicates and their original samples, for CLP (from white blood cells, calculated for the entire cohort, left), HCT (men only,
(CLP-E, CLP-M, CLP-L and NKTDP) populations (top) and MEBEMP (MEBEMP-E, center) and RDW (men only, right). Missing individuals lacked sufficient cells for
MEBEMP-L, ERYP and BEMP) populations (bottom). The diagonal y = x is shown analysis. Two-sided permutation test P values are displayed for each correlation.
in red. All biological replicates were sampled 1 year after their original sampling See Methods for details on the permutation-based test. f, CH frequency (by gene)
date. d, Top: cell-state frequency profiles over the HSC-MEBEMP and HSC- in age- and sex-matched high (red, n = 602) and normal (black, n = 602) RDW
CLP differentiation gradients of six sampled individuals (colored lines), each individuals selected from a cohort of 18,147 individuals. Panel a created with
representing one of six archetypes (classes) of cHSPC composition observed BioRender.com.
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
Composition-controlled cHSPC expression correlates with age individuals, filtering out sex-linked signatures and those showing strong
As shown above, individual cHSPC compositions provide an initial batch effects. The most prominent of these signatures included Lamin-A
blueprint of hematopoietic dynamics along the stemness and CLP or (LMNA) as well as ANXA1, AHNAK, MYADM, TSPAN2 and VIM, among
MEBEMP axes, with age-dependent changes. Composition-normalized others (Fig. 3f, Extended Data Fig. 6f and Supplementary Table 7). Indi-
gene expression profiles were further correlated with age, enabling age vidual LMNA signature expression varied across a range of more than
prediction based on normalized gene expression alone (Fig. 3e and twofold (Extended Data Fig. 6g), exhibiting high expression variability
Extended Data Fig. 6e; see Supplementary Tables 5 and 6 for additional in HSCs and early myeloid and lymphoid cell states, and a homogene-
screening for age-, CBC-, CH- and sex-associated gene expression). ously low expression in late MEBEMPs and CLPs (Extended Data Fig. 6h).
We next looked for gene groups (signatures) that co-variate between Individual LMNA signature expression was consistent in myeloid and
N115 N165 N84 N261 N107 N179
MEBEMP HSC
Nature Medicine
ycneuqerF
a b
d
CLP MEBEMP HSCCLP MEBEMP HSCCLP MEBEMP HSC CLP MEBEMP HSCCLP MEBEMP HSC CLP
f
)%(
ycneuqerF
1.2
0.8
0.4
0
A3TMND 2KAJ 1B3FS LBC 1XNUR 2TET 1LXSA 2FSRS 1BNG 1HDI D1MPP
High RDW (>15%)
Normal RDW control
ycneuqerf
etats-lleC
)%
,elacs
gol(
2HDI
37.6 ± 5.8
20.7 ± 4.9 12.6 ± 6.8
8.4 ± 2.3
2.3 ± 1.5 3.0 ± 1.5 10 3.5 ± 0.9 2.4 ± 1.0 2.5 ± 1.2
2.8 ± 0.8
1
PMEB PYRE L-PMEBEM E-PMEBEM E-PMG PPM CSH E-PLC M-PLC L-PLC PDTKN
4.3 ± 1.8
Age
CSH
Sex
Stemness
PMEBEM
PLC
Class I Class II Class III Class IV Class V Class VI
)tnemhcirne(gol
2
+1
–1
Class
erocs
ylraE
c
Age (years)
85+
20
Sex
0.65
Female
Male
0.40
lacigoloib
ni ycneuqerf
etats-lleC
etacilper
CLPs
0.5
0.3
0.1 0.1 0.3 0.5
MEBEMPs
0.7
0.5
0.3
0.3 0.5 0.7
Cell-state frequency in
original sample
95th percentile
Median
5th percentile
%lymphocytes, all individuals HCT, males (n = 76), RDW, males (n = 76),
(n = 140), P = 0.008 P = 0.018 P = 0.005
PMEB PYRE L-PMEBEM E-PMEBEM E-PMG PPM CSH E-PLC M-PLC L-PLC PDTKN
e
noitalerroC
PMEB PYRE L-PMEBEM E-PMEBEM E-PMG PPM CSH E-PLC M-PLC L-PLC PDTKN PMEB PYRE L-PMEBEM E-PMEBEM E-PMG PPM CSH E-PLC M-PLC L-PLC PDTKN
MPP HSC
CLP-E
CLP-M
MEBEMP-E MYE (GM ER P Y ) P CLP-L MEBEMP-L BEMP NKTDP n = 148 n = 1
Age Sex
0.4
0.3
0.2
0 0 0
–0.2 –0.3 –0.4
ycneuqerF
1. Quantify individual cHSPC state frequencies
95%
5% MEBEMP HSC CLP
2. Correlate individual frequencies with
clinical parameters
CBC CH
Resource https://doi.org/10.1038/s41591-025-03716-5
lymphoid cell states (Fig. 3g) and was stable in our follow-up cohort in situ hybridization, microscopy and flow cytometry of BM specimens.
(Extended Data Fig. 6i). We observed an age-linked increase in LMNA In Fig. 4a we described a stepwise approach for analysis of myeloid
signature expression in lymphoid, but not myeloid, cHSPCs (Fig. 3h). disorders based on sampling of cHSPCs and comparison of their
Future studies on larger cohorts, enriched with clinical data, could compositions, normalized expression and copy number variations
further explore the age-related LMNA signature overexpression in (CNVs) to our normal reference (Extended Data Fig. 7a–c). As proof
CLPs and how it correlates with disease and immune function. Taken of concept, we focused on MDS diagnosis. First, we reconstructed
together, we show that, in addition to the accumulation of leukemic the reference model using data from 79 healthy individuals, putting
mutations in HSPCs, aging is linked with changes in the distribution aside some normal samples for classifier training. We then performed
of progenitor cell states within the PB and with notable expression additional sequencing to obtain data from 44 patients with MDS and
differences in certain gene signatures. The mechanistic basis for this 29 patients with cytopenia (Supplementary Tables 9–11). We devel-
variation and its clinical impact remain unresolved. oped a streamlined in silico sorting scheme for quantifying the cHSPC
composition of a new PB sample given the reference (Extended Data
Coordination of stemness and myeloid signatures Fig. 7a,b) and used it to identify cases with abnormal compositions
The differentiation of HSPCs toward MEBEMP and CLP fates involves (Fig. 4b,c, Extended Data Fig. 8a and Methods). Classification included
coordinated activation and repression of specific transcriptional subpopulations (GMP-L, pre-B, pro-B and MkP) that were rare in the
programs which are conserved across individuals. Yet, our screen for normal reference model and were not shown in Fig. 1. We then marked
interindividual variation in gene signature expression suggested that MDS or cytopenic samples with normal compositions (matching the
individuals differed in the way in which they synchronized the opposing reference model, group 1) and organized them along the myeloid and
effects of these stemness and differentiation programs. To quantify this lymphoid spectrum. The remaining cases were clustered into distinc-
variation, we compared AVP (stemness) and GATA1 (MEBEMP differen- tive subclasses. Although most cases of MDS showed significantly lower
tiation) signatures (Supplementary Table 8) on a 20 × 20 bin expression CLP frequencies (groups 3 and 4; Extended Data Fig. 8b), we identified
matrix (Fig. 3i). Although most individuals displayed dynamics close a subclass of MDS and cytopenia with high CLP frequencies (group 2).
to the diagonal line (individuals N16 and N86, for example), following Other subclasses included high MPP (group 4.2), high BEMP (group
the typical transition from stemness to differentiation, some individu- 4.1) and high GMP (group 3) frequencies. This sorting scheme partially
als deviated from the diagonal, indicating skewed synchronization separated MDS from other, non-MDS-related, cases of cytopenia, with
between AVP and GATA1 signatures. We quantified this deviation (that most cytopenia cases exhibiting normal (group 1) compositions. Cases
is, off-diagonal frequency) using a synchronization-score (sync-score). of MDS with abnormal CNVs (Methods) were enriched in groups 2–4
This facilitated the identification of individuals with sync-scores as low (P < 0.004, Fisher’s exact test; Fig. 4d and Supplementary Table 12)
as 0.12 (N122 and N172, for example, Fig. 3i, top), indicating delayed and patients with high RDW were enriched in group 4 (Extended Data
activation of GATA1 relative to AVP repression. In contrast, individuals Fig. 8c). In summary, cHSPC compositions reveal molecular features
exhibiting a high sync-score (N98 and N121, for example, Fig. 3i, bottom) that offer possibilities for identifying MDS subclasses and pathophysi-
show early activation of GATA1 expression, which precedes AVP repres- ology. Classification of MDS cases with normal cHSPC compositions
sion. Interindividual sync-score variability (Extended Data Fig. 6j) was (group 1) depends on further analysis of genetic and transcriptional
positively correlated with RBC levels and consistently anti-correlated states within specific cHSPC subtypes.
with MCV in men (P < 0.01 (Spearman’s) for both RBC and MCV; Fig. 3j).
Analysis of the correlation between individual sync-scores and cHSPC PB-based MDS diagnosis with CBC, mutation and cHSPC
compositions in men demonstrated a negative correlation with ERYPs RNA data
(Fig. 3k). In summary, variation in the coordination of stemness and To improve our diagnostic accuracy, we next derived specific gene
MEBEMP differentiation programs correlated with RBC counts and signatures showing additional variation within cell types, from the
volumes. More studies on larger cohorts are needed to explore how reference model (Supplementary Table 13), and scored these signatures
this coordination relates to age-related macrocytic anemia. based on their ability to separate patients with MDS and cytopenia
from healthy donors. A group of major histocompatibility complex
Circulating HSPC composition abnormality in cytopenia class II (MHC-II) genes in MEBEMP-L, multi-potency genes in BEMP
and MDS and S-phase genes in MEBEMP-L (Fig. 4e) emerged as top-ranking.
Diagnosis of myeloid malignancies requires the identification of These signatures were overall consistent across different samples of
clonal markers (mutations or structural variants) and the detec- the same individuals (Extended Data Fig. 8d). We then combined CBCs,
tion and quantification of blasts and dysplasia, by next-generation maximum variant allele frequency (VAF), cHSPC compositions and all
sequencing, polymerase chain reaction, cytogenetics, fluorescence afore-mentioned expression signatures into a feature set that formed
Fig. 3 | Age- and sex-linked changes in cHSPC composition. a, Frequency of in red. f, Gene–gene correlation heatmap, calculated over individual-level MPP
MEBEMP (MEBEMP-E, MEBEMP-L, ERYP and BEMP, left) and CLP (CLP-E, CLP-M gene expression controlled for MPP composition. g, Individual LMNA signatures
and CLP-L, right) populations, out of a total CD34+ population, in young (<50 (log(observed:expected ratios)) in lymphoid (CLPs) and early myeloid (MPPs)
2
years) versus old (>60 years) individuals without CH, in men (blue) and women cell states. h, Analysis of age-linked differences in LMNA signature expression
(red). The two-sided Kruskal–Wallis P values for differences among groups are for CLP (right) and MPP (left) populations in young (<50 years) versus old
denoted. The number of individuals per group is (left to right): 31, 15, 24 and (>60 years) individuals. The y axis denotes log(observed:expected expression)
2
31. b, Analysis of age-linked compositional differences within the MEBEMP normalized for composition. The number of individuals is 66 young, 65 old on
differentiation trajectory, comparing abundance of more (MEBEMP-L) with the left and 48 young, 53 old on the right. The two-sided Mann–Whitney U-test
less (MPP) differentiated states in young versus old individuals. The two-sided P values are indicated. i, Individual heatmaps of single-cell counts over 20 bins of
Kruskal–Wallis P value for difference among groups is denoted. The number stemness (AVP signature, y axis) and MEBEMP differentiation (GATA1 signature,
of individuals is as in a. c, As in a, for the HSC population. d, cHSPC frequency x axis). Individual identifier, MCV and RBC are denoted at the top. The diagonal
per age decimal in an scRNA-seq PBMC dataset of 1,000 healthy individuals25. is indicated in black for reference. j, MCV versus RBC in male donors, with
For each decade, mean CD34+ cell frequency is shown (Methods). The 95% colors indicating high (red) and low (black) sync-scores. k, Correlation between
confidence intervals are indicated as error bars. The number of individuals in individual sync-scores and cell-state compositions in men. The two-sided
each decade is indicated (top). e, True age (x axis) versus age predicted based permutation test P value is denoted. All boxplots are as in Fig. 2b.
on composition-controlled MPP expression (y axis). The diagonal y = x is shown
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
the basis for construction of an MDS diagnostic classifier using stand- Analysis of classifier performance showed very high specificity and
ard machine learning tools. We created two cohorts: the first (cohort sensitivity (Fig. 4f; area under the curve (AUC) = 0.93 in leave-one-out
1), composed of 28 patients with MDS, 20 patients with cytopenia cross-validation for cohort 1 separation of MDS from cytopenia). Per-
and 41 healthy individuals, and the second (cohort 2) composed of 16 formance of the cohort 1 model on cohort 2 (which was not used during
patients with MDS and 9 patients with cytopenia. We observed classi- classifier training) was even higher (AUC = 0.97). Although cohort 2 data
fier training performance (even when aiming to separate MDS from was not used in classifier training or feature selection, it was accessible
cytopenia cases) was better when including normal cases in the dataset. to us during project analysis phases, such that we were cautious not to
j
100
75
3.5 6.5
RBC
Nature Medicine
VCM
a b c
%MEBEMPs in CH- %CLPs in CH- Myeloid differentiation %HSCs in
negative individuals negative individuals in CH-negative individuals CH-negative individuals
0
60 40 5
50 30 –1
3
40 20 –2
30 10 1
–3
f
Age (years)
cHSPC composition
versus sync-score
0.4 males (n = 78), P = 0.0003
0
–0.4
High sync
Low sync
)sraey(
ega
detciderP
Young Old Young Old Young Old Young Old
e cHSPC RNA clock, R2 = 0.7
(normalized for composition)
90
70
50
30
30 50 70 90
)elacs
gol(
sllec
+43DC%
0.4
0.1
Age decimals
98–08
d
1,000 PBMC profiles
0.2
0.05
92–02 94–04 96–06
g
Myeloid LMNA signature
erutangis
ANML
diohpmyL
erutangis
ANML
dioleyM
erutangis
ANML
diohpmyL
0.5
–0.5
–0.5 0.5
PMEB PYRE L-PMEBEM E-PMEBEM E-PMG PPM CSH E-PLC M-PLC L-PLC PDTKN
Signatures:L
MNA
G
MP
Fe
male
Ly
mph
M
o
y
id eloid Histones Male
RPS4Y, UTY, 8 more
Histones
CEBPA, MZB1,
7 more
–1 1
DNTT, IL7R, MME, Residual CCR7, ACY3, 9 more
gene
correlation XIST, TSIX, 2 more
MPO, CD38, 3 more
S100A10, 11, LMNA,
CRIP2, CAMK1D, EHD2,
12 more
h i
N172 (MCV 93.5,
RBC 4.5)
P = 0.88 P = 0.01
0.4
0.5 Low
0
0
sync-score
–0.4
–0.5
N16 (MCV 90, N86 (MCV 87,
Young Old Young Old RBC 5.0) RBC 4.8)
k
N121 (MCV 92, N98 (MCV 76,
RBC 4.7) RBC 6.6)
H igh
sync-score
erutangis
PVA
N122 (MCV 92,
RBC 5.0)
GATA1 signature
erutangis
PVA
erutangis
PVA
1 1 0.80
Low
sync-score
0
0
.
.
0
20
5
0 0
0 1 0 1
GATA1 signature
1 1
0 0
0 1 0 1
GATA1 signature GATA1 signature
1 1
H igh
sync-score
0 0
0 1 0 1
GATA1 signature GATA1 signature
)%(
ycneuqerF
Male Male Male Female Female Female
Male
Female
)%(
ycneuqerf
lleC
noitalerroC
)PPM
fo
.on/L-PMEBEM
fo
.on(gol
2
)%(
ycneuqerf
CSH
P = 0.0014 P = 0.0037 P = 0.88 P = 0.014
5 44 95 47 711 442 252 131 31
Resource https://doi.org/10.1038/s41591-025-03716-5
a
1. scRNA-seq on
patient-derived
cHSPCs
2. Analyze patient 3. Score patient cell type- 4. Infer sub-clonal copy 5. Estimate %blasts 6. Perform PB
cHSPC composition specific RNA signatures number alterations from specific cell states mutational analysis
b GRP2 GRP4 GRP3
4.1 high 4.2 high
GRP1: normal-like composition
HighCLP BEMP HSC/MPP High GMP
pre-B?
pro-B?
NKTDP
CLP
HSC_MPP
GMP-L
MEBEMP-L
high_MPP_sig_ERYP
ERYP
BEMP
MKP
4
Cytopenia
MDS
MDS/MPN
MEBEMP-L MHC-II signature BEMP early signature MEBEMP-L S-phase signature
*** ** ****** * ** ** ** *** ** * Normal
Cytopenia
MDS
MDS/MPN
M F M F M F M F M F M F M F M F M F M F M F M F M F M F M F
Normal GRP1 GRP2 GRP3 GRP4 Normal GRP1 GRP2 GRP3 GRP4 Normal GRP1 GRP2 GRP3 GRP4
MDS versus cytopenia classification
***** * Complex
n = 48, AUC=0.93 karyotype
n = 25, AUC=0.97
M F M F M F M F M F
Normal GRP1 GRP2 GRP3 GRP4 Complex
karyotype
treat this as formal validation. The most informative feature used by data using the fraction of cells showing a mixed HSC and CLP state
the MDS classifier was the maximum VAF (Extended Data Fig. 9a). Yet, (Fig. 4g,h and Extended Data Fig. 9d). All in all, this implies that, with
classifier performance was high even when excluding VAF information further validation and testing, cHSPC profiling has the potential to
(Extended Data Fig. 9b,c). replace BM analysis for MDS diagnosis and risk stratification, offer-
Diagnosis and risk stratification of MDS rely on quantification of ing substantial benefits, such as noninvasive follow-ups and watchful
BM blast fractions. Our analysis of cohort 1 and cohort 2 samples, with waiting protocols. We present two case studies supporting this idea
the addition of three cases of MDS exhibiting complex karyotypes, sug- in Extended Data Fig. 10a,b. The first is an 82-year-old man showing
gests that we can predict this percentage quantitatively from cHSPC progressive clonal expansion over a span of 3 years, accompanied by
Nature Medicine
)ycneuqerf
ekil-E-PLC(gol
2
c
d
e
f g h
CLP-E-like state
–1
–2 –2
–3 –3
–4 –4
–5 –5
–6
–7
–5 –4 –3 –2
log(CLP-E-like frequency) 2
noitisopmoC ytilamronba
erocs
)ycneuqerf
stsalb
MB(gol
2
r = 0.73 P = 3 × 10–5
)noisserpxe
erutangis(gol
2
Diagnosis
DNMT3A
TET2
SF3B1
Other CH
CNA
–7.0 –7.50
–8 –7.75
–7.5
–8.00
–9 –8.0
–8.25
–8.5
–10 –8.50
–9.0 –8.75
0 0.2 0.4 0.6 0.8 1.0
FPR
RPT
Composition
abnormality
score
CH VAF
0 0.5
1.0
0.8
0.6
0.4
0.2
0
ycneuqerf
etats
CPSHc
CD34 CD34
CD34 CD34 *** ********
CD34
7. Classify
MDS/cytopenia,
stratify MDS risk
1
0
4
2
0 2
0
Patient Patient
Cohort 1
Cohort 2
Resource https://doi.org/10.1038/s41591-025-03716-5
Fig. 4 | Applying the cHSPC reference model to MDS diagnosis and Individuals exhibiting insufficient cell counts for the population of interest
subclassification. a, Schematics of a diagnostic approach to cytopenia and MDS were excluded. Color denotes clinical diagnosis. Mann–Whitney Benjamini–
using scRNA-seq of cHSPCs and a reference model. b–d, Cytopenia and MDS Hochberg-adjusted significance of difference from healthy donors of the
patient cHSPC compositions and mutations. b, Each bar represents a patient’s same sex is indicated by asterisks (*q < 0.05, **q < 0.01, ***q < 0.001). f, Receiver
cHSPC composition. Patients exhibiting normal compositions (Methods) are operator curve for a classification model predicting MDS status based on cHSPC
ordered by lymphoid cHSPC frequency (left) and those exhibiting abnormal scRNA-seq, CH VAF and CBC values. FPR, false-positive rate; TPR, true-positive
compositions are ordered by composition hierarchical clustering (right). rate. g, Frequency of a CLP-E-like cell state across healthy donors and cytopenia
Cytopenia or MDS subclasses suggested by composition are marked (top). and MDS groups, as in e. h, Comparison of BM blast counts measured by FACS and
c, Patient composition abnormality scores, depicted by both bar height and frequency of a CLP-E-like cHSPC population across individuals. Color denotes
color, as coded on the right. d, Patient diagnosis and CH VAF for three specific clinical diagnosis, as in e. Samples excluded from b–g due to the presence of
mutations and the maximal VAF over all other detected mutations, as color a complex karyotype (as detected by scRNA-seq) are highlighted (arrows).
coded on the right. Presence of copy number alterations (CNAs) as detected by Linear fit across all individuals (n = 26) is shown (dashed line), as well as the
scRNA, color coded in black. e, Transcriptional signatures across healthy donors corresponding r and (two-sided) P value.
and patient groups as in b, further subdivided by sex (men, left; women, right).
deteriorating anemia. The second is a 65-year-old woman presenting pathophysiology and drug design strategies. Importantly, further
with clonal del5q showing complete cytogenetic remission after lena- follow-up, validation in prospective studies and cohort expansion to
lidomide treatment. Additional follow-up examples (Extended Data ethnically diverse populations are needed to prove that the tools intro-
Fig. 10c) suggest small changes in (normal or abnormal) composition duced here can become a clinical standard. The diagnostic potential
across time, further supporting the idea of using cHSPCs for noninva- of our reference model may be further enhanced upon acquisition
sive assessment of disease progression. and analysis of additional blood subpopulations and disease states
in contrast with the reference. Practically, application of scRNA-seq
Discussion for diagnostics would have to rely on stable and minimally biased
The present study characterizes interindividual heterogeneity in cell acquisition and processing technologies that can be deployed
cHSPCs across 148 healthy individuals using scRNA-seq analysis of PB across diverse clinical settings and provide consistent and trustworthy
CD34+ cells. The magnitude of our cohort, along with the potency and results. Development in this domain is promising, but more work must
resolution of modern single-cell technologies and the computational be done to reach clinical standards.
methods used in the present study, allowed us to characterize in detail To conclude, our study delves into the basic molecular physiology
the transcriptional programs of diverse, sometimes rare (NKTDP and of cHSPCs at the population level, uncovering age-related phenotypes
BEMP), HSPC subpopulations, refining and augmenting previous find- and proposing a platform for mechanistic and diagnostic insights into
ings from smaller cohorts (Fig. 1). We defined a normal reference range blood malignancies. This resource, along with various other tools for
for cHSPC subpopulation frequencies within an age- and sex-diverse profiling genetics and epigenomics in the blood, has the potential to
healthy population and showed that cHSPC subtype compositions were redefine normal versus pathological states in hematology and provide
highly variable between individuals, whereas the cell states themselves both clinicians and researchers the means for mapping the transition
were remarkably general (Fig. 2). These compositions remained sta- from health to disease.
ble over a 1-year follow-up period. Future studies will need to further
explore and better define the mechanistic and genetic basis for this Online content
compositional heterogeneity. With current sample size, we showed Any methods, additional references, Nature Portfolio reporting sum-
that the known age-related myeloid bias in HSPCs is predominantly maries, source data, extended data, supplementary information,
male driven and that composition-controlled RNA expression can be acknowledgements, peer review information; details of author con-
used to infer chronological age (Fig. 3). tributions and competing interests; and statements of data and code
Our data show that cHSPCs are transcriptionally similar to their availability are available at https://doi.org/10.1038/s41591-025-03716-5.
BM counterparts (Extended Data Figs. 2 and 3), except for reduced
cell-cycle gene expression. Although not a complete model for BM References
hematopoiesis, cHSPCs serve as a highly accessible proxy for key 1. Osgood, E. E. Normal hematologic standards. Arch. Intern. Med.
hematological processes. Interindividual differences in cHSPC com- 56, 849–863 (1935).
positions and states can thus serve as a tool for capturing key aspects 2. Cohen, N. M. et al. Personalized lab test models to quantify
of a patient’s hematopoietic state. The relevance and importance of a disease potentials in healthy individuals. Nat. Med. https://doi.
cHSPC normal reference (Fig. 2b) can perhaps be better understood in org/10.1038/S41591-021-01468-6 (2021).
view of the normal CBC reference range, developed in the 1930s1. The 3. Cohen, K. S. et al. Circulating CD34+ progenitor cell frequency is
development of a population-wide CBC reference enabled the identi- associated with clinical and genetic factors. Blood 121, e50–e56
fication of numerous pathological blood states that characterize dis- (2013).
tinct clinical entities. In a similar fashion, our cHSPC reference can be 4. Mende, N. & Laurenti, E. Hematopoietic stem and progenitor cells
used to characterize physiological and pathological states. In Fig. 4 we outside the bone marrow: where, when, and why. Exp. Hematol.
describe a pipeline for the identification and characterization of blood 104, 9–16 (2021).
pathologies based on our normal cHSPC reference and show how this 5. Ainciburu, M. et al. Uncovering perturbations in human
can be applied to MDS diagnostics (including inference of cytogenetics hematopoiesis associated with healthy aging and myeloid
and blast counts from the PB). We present scRNA-seq data on cHSPCs malignancies at single-cell resolution. eLife 12, e79363 (2023).
from 73 cases of cytopenia and MDS, greatly extending currently avail- 6. Quaranta, P. et al. Circulating hematopoietic stem/progenitor cell
able BM MDS scRNA-seq datasets5,29–32. The data described supports subsets contribute to human hematopoietic homeostasis. Blood
MDS diagnosis (over non-MDS-related cytopenia) and suggests the 143, 1937–1952 (2024).
possibility of MDS subclassification based on over-representation 7. Mende, N., Dresden, T. U., Santoro, A. & Lidonnici, M. R.
of distinct HSPC progenitor populations. The MDS-related gene Unique molecular and functional features of extramedullary
expression signatures identified in the present study open avenues hematopoietic stem and progenitor cell reservoirs in humans.
for research that might contribute to better understanding of MDS Blood https://doi.org/10.1182/blood.2021013450 (2022).
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
8. Bender, J. et al. Identification and comparison of CD34-positive cells 25. Yazar, S. et al. Single-cell eQTL mapping identifies cell type–
and their subpopulations from normal peripheral blood and bone specific genetic control of autoimmune disease. Science 376,
marrow using multicolor flow cytometry. Blood 77, 2591–2596 (1991). eabf3041 (2022).
9. Goodman, J. W. & Hodgson, G. S. Evidence for stem cells in the 26. De-Morgan, A., Meggendorfer, M., Haferlach, C. & Shlush, L. Male
peripheral blood of mice. Blood 19, 702–714 (1962). predominance in AML is associated with specific preleukemic
10. Biezuner, T. et al. An improved molecular inversion probe based mutations. Leukemia 35, 867–870 (2021).
targeted sequencing approach for low variant allele frequency. 27. Zioni, N. et al. Inflammatory signals from fatty bone marrow
NAR Genom. Bioinform. 4, lqab125 (2022). support DNMT3A driven clonal hematopoiesis. Nat. Commun.
11. Ben-Kiki, O., Bercovich, A., Lifshitz, A. & Tanay, A. Metacell-2: a 14, 2070 (2023).
divide-and-conquer metacell algorithm for scalable scRNA-seq 28. Bacharach, T., Kaushansky, N. & Shlush, L. I. Age-related
analysis. Genome Biol. 23, 100 (2022). micro-environmental changes as drivers of clonal hematopoiesis.
12. Setty, M. et al. Characterization of cell fate probabilities in Curr. Opin. Hematol. 31, 53–57 (2024).
single-cell data with Palantir. Nat. Biotechnol. 37, 451–460 (2019). 29. Serrano, G. et al. Single-cell transcriptional profile of CD34+
13. Lehnertz, B. et al. HLF expression defines the human hematopoietic progenitor cells from del(5q) myelodysplastic
hematopoietic stem cell state. Blood 138, 2642–2654 (2021). syndromes and impact of lenalidomide. Nat. Commun. 15, 5272
14. Regev, A. A single cell immune cell atlas of human hematopoietic (2024).
system. Human Cell Atlas Data Explorer https://data.human- 30. Wu, Z. et al. Sequencing of RNA in single cells reveals a distinct
cellatlas.org/explore/projects/cc95ff89-2e68-4a08-a234- transcriptome signature of hematopoiesis in GATA2 deficiency.
480eca21ce79?catalog=dcp1 (2022). Blood Adv. 4, 2702–2716 (2020).
15. Frelin, C. et al. GATA-3 regulates the self-renewal of long-term 31. Liu, Y. et al. Single-cell RNA sequencing identifies the properties
hematopoietic stem cells. Nat. Immunol. 14, 1037–1044 (2013). of myelodysplastic syndrome stem cells. J. Transl. Med.
16. Weinreb, C., Rodriguez-Fraticelli, A., Camargo, F. D. & Klein, A. M. https://doi.org/10.1186/s12967-022-03709-9 (2022).
Lineage tracing on transcriptional landscapes links state to fate 32. Ganan-Gomez, I. et al. Stem cell architecture drives
during differentiation. Science 367, eaaw3381 (2020). myelodysplastic syndrome progression and predicts
17. Lavaert, M. et al. Integrated scRNA-seq identifies human response to venetoclax-based therapy. Nat. Med. 28, 557–567
postnatal thymus seeding progenitors and regulatory dynamics (2022).
of differentiating immature thymocytes. Immunity 52, 1088–1104
(2020). Publisher’s note Springer Nature remains neutral with regard to
18. Scoville, S. D. et al. A progenitor cell expressing transcription jurisdictional claims in published maps and institutional affiliations.
factor RORγt generates all human innate lymphoid cell subsets.
Immunity 44, 1140–1150 (2016). Open Access This article is licensed under a Creative Commons
19. Abelson, S. et al. Prediction of acute myeloid leukaemia risk in Attribution-NonCommercial-NoDerivatives 4.0 International License,
healthy individuals. Nature 559, 400–404 (2018). which permits any non-commercial use, sharing, distribution
20. Kar, S. P. et al. Genome-wide analyses of 200,453 individuals and reproduction in any medium or format, as long as you give
yield new insights into the causes and consequences of clonal appropriate credit to the original author(s) and the source, provide a
hematopoiesis. Nat. Genet. 54, 1155–1166 (2022). link to the Creative Commons licence, and indicate if you modified
21. Nam, A. S. et al. Somatic mutations and cell identity linked by the licensed material. You do not have permission under this licence
genotyping of transcriptomes. Nature 571, 355–360 (2019). to share adapted material derived from this article or parts of it. The
22. Nam, A. S. et al. Single-cell multi-omics of human clonal images or other third party material in this article are included in the
hematopoiesis reveals that DNMT3A R882 mutations perturb article’s Creative Commons licence, unless indicated otherwise in a
early progenitor states through selective hypomethylation. Nat. credit line to the material. If material is not included in the article’s
Genet. 54, 1514–1526 (2022). Creative Commons licence and your intended use is not permitted
23. Sudo, K., Ema, H., Morita, Y. & Nakauchi, H. Age-associated by statutory regulation or exceeds the permitted use, you will need
characteristics of murine hematopoietic stem cells. J. Exp. Med. to obtain permission directly from the copyright holder. To view
192, 1273–1280 (2000). a copy of this licence, visit http://creativecommons.org/licenses/
24. Pang, W. W. et al. Human bone marrow hematopoietic stem cells by-nc-nd/4.0/.
are increased in frequency and myeloid-biased with age. Proc.
Natl Acad. Sci. USA 108, 20012–20017 (2011). © The Author(s) 2025
1Department of Molecular Cell Biology, Weizmann Institute of Science, Rehovot, Israel. 2Blavatnik School of Computer Science, Tel Aviv University,
Tel Aviv, Israel. 3Department of Computer Science and Applied Mathematics, and Department of Molecular Cell Biology, Weizmann Institute of Science,
Rehovot, Israel. 4Hemato-Oncology Department, Assuta Medical Center, Tel Aviv, Israel. 5Maccabi Healthcare Services, Tel Aviv, Israel. 6Department of
Life Sciences Core Facilities, Weizmann Institute of Science, Rehovot, Israel. 7Ultima Genomics, Fremont, CA, USA. 8Integrated Cancer Prevention Center,
Tel Aviv Sourasky Medical Center, Tel Aviv, Israel. 9Clalit Health Services, Tel Aviv, Israel. 10Department of Cell, Developmental and Cancer Biology, Knight
Cancer Institute, Oregon Health and Science University, Portland, OR, USA. 11Division of Hematology and Medical Oncology, Knight Cancer Institute,
Oregon Health and Science University, Portland, OR, USA. 12New York Genome Center, New York, NY, USA. 13Sandra and Edward Meyer Cancer Center,
Weill Cornell Medicine, New York, NY, USA. 14Division of Hematology and Medical Oncology, Department of Medicine, Weill Cornell Medicine,
New York, NY, USA. 15Institute for Computational Biomedicine, Weill Cornell Medicine, New York, NY, USA. 16Division of Hematology, Rambam Healthcare
Campus, Haifa, Israel. 17These authors contributed equally: N. Furer, N. Rappoport, O. Milman, A. Tanay, L. Shlush. e-mail: amos.tanay@weizmann.ac.il;
liranshlush3@gmail.com
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
Methods (Supplementary Table 9). Of the 83 patients with cytopenia, 17 who
Patient recruitment presented with asymptomatic, mild cytopenia, were also included in
All healthy reference model individuals (n = 148, analyzed in Figs. 1–3 the original healthy cohort of 148 individuals.
and Extended Data Figs. 1–6) volunteered to participate in our study
and donated blood at the Weizmann Institute of Science (WIS) between Sampling of cHSPCs
November 2020 and December 2023. They were recruited from the We drew 50 ml of PB from each individual into lithium–heparin tubes
WIS community and primary care clinics and consisted of 79 men and and put aside 1 ml of blood for DNA production. The remaining volume
69 women aged 23–91 (median 61.5) years. Their demographic data was used for PBMC isolation via Ficoll using Lymphoprep-filled Sep-
and CBCs are included in Supplementary Table 1. Written informed mate tubes (STEMCELL Technologies), followed by CD34 magnetic
consent allowing access to their demographic, longitudinal CBC and bead-based enrichment using the EasySep human CD34+ selection
sequencing data (CH and genotyping panels) was obtained from all kit II (STEMCELL Technologies). We found this enrichment strategy
participants in accordance with the Declaration of Helsinki. All relevant to be simple and reproducible and chose it for a couple of reasons:
ethical regulations were followed and all protocols were approved (1) RNA-seq data were most reproducible when cells were not sorted,
by the WIS ethics committee (under Institutional Review Board (IRB) but rather enriched for using beads (lower mitochondrial gene frac-
protocol no. 283-1). tion); and (2) CD34 purity could be highly regulated by this method,
For the main reference model (Figs. 1–3), recruitment was intended to achieve anywhere between 50% and 95% enrichment of CD34+ cells,
to allow characterization of the normal variation in cHSPC states. As no which could later be easily distinguished based on their single-cell
such profiling had been previously performed, we could not assume expression data.
much about the variance in the population a priori. Participants were
therefore required to lack any known hematological condition, includ- ScRNA-seq of cHSPCs
ing hematological malignancy or premalignant state, or any prior ScRNA libraries were generated using the 10x Genomics scRNA-seq
evidence of blood clonality. An Illumina-sequenced subset of these platform (Chromium Next Gem single-cell 3ʹ reagent kit v.3.1). Chip
148 individuals (n = 79) was used for constructing the healthy reference loading was preceded by flow cytometry to verify that enrichment was
model used in Fig. 4 (‘Fig. 4 reference model’), filtering out individuals successful and that enough CD34+CD45int live cells were gathered. All
with any blood count abnormality (up to 5 years before sampling) and blood samples were either drawn at WIS or transferred from partici-
putting aside 41 healthy samples for classifier training. pating clinics on the morning of each experiment day, and time from
Recruitment of the cytopenic cohort (including patients with MDS blood draw to 10x loading was restricted to 5 h. The motivation for
and non-MDS-related cytopenia, analyzed in Fig. 4 and Extended Data working with fresh samples was based on our previous experience with
Figs. 7–10) took place between November 2021 and February 2024. PB CD34+ cells being vulnerable to freezing–thawing rounds and long
These patients were recruited from several outpatient hematological manipulation times. The 10x libraries were sequenced on two alterna-
clinics by collaborating physicians to represent the wide clinical spec- tive platforms (Illumina and Ultima Genomics). Twelve libraries were
trum of MDS, from patients with moderate anemia and mild dysplasia simultaneously sequenced on both platforms for comparison purposes
as their sole BM abnormality to those with severe cytopenia and excess and to demonstrate the scalability of our approach. We observed the
blasts on BM analysis. Key patient characteristics, including CBCs, Ultima-sequenced data to be highly similar to the Illumina-sequenced
BM FACS blasts and mutational data, are included in Supplementary data (Extended Data Fig. 5a).
Tables 9 and 11. Median age for the cytopenic cohort was 73 years (range
27–93 years), with men representing 53% of patients. Patient PB samples DNA production and sequencing
were either drawn at WIS or transported to WIS within <2 h of blood All healthy and patient DNA was produced from PB at sampling. DNA
drawing. All cytopenic samples were processed in an identical fashion sequencing was performed on two targeted panels: the first a rich
to the healthy ones (described below). Longitudinal CBCs, mutational myeloid CH panel (InfiniSeq Myeloid Malignancies Panel, Sequentify,
data and most recent BM analyses were collected from patients and Israel) covering all known pre-leukemic mutations10 and the second a
analyzed along with their scRNA-seq data. genotyping panel specifically designed to capture polymorphic sites
The cytopenic cohort included a total of 83 individuals, 50 of prevalently expressed by RNA molecules from all cell types in our data.
whom were labeled as cases of ‘MDS’, based on BM morphology and/or This allowed demultiplexing of individual pools based on individual
mutational and karyotypic abnormalities (as detected in the clinic or by specific SNP combinations and replaced previous, antibody-based
our CH panel and scRNA CNA analysis). The remaining 33 patients with multiplexing methods. Three to six individual samples were pooled on
cytopenia not satisfying MDS criteria were labeled as cases of ‘cytope- each experiment day after extraction of DNA aliquots, such that CD34
nia’. We note that, consistent with common medical practice in Israel, enrichment was performed on the entire pool of PBMCs produced. As
most of these 33 patients with cytopenia did not undergo BM examina- with other methods of sample multiplexing, genotype-based multiplex-
tion, which may have resulted in missed MDS diagnoses. To address ing allows for robust doublet detection during data analysis, which
this limitation, we collected the most recent clinical data available for enabled loading of 30,000–40,000 cells on each Chromium Chip lane.
patients with cytopenia, with a median follow-up period exceeding Both our CH and genotyping panels are Molecular Inversion
600 d after cHSPC sampling (Extended Data Fig. 10d and Supplemen- Probe (MIP) panels described in detail previously10. For the healthy
tary Table 9). Importantly, no new diagnoses of myeloid malignancy cohort we used our CH panel v.3, containing 705 probes, covering
were recorded in any of the cytopenic cases, except for N193 who was leukemia-related SNVs and insertions/deletions (indels) in 47 genes,
diagnosed with VEXAS syndrome 1 year after cHSPC sampling, exhibit- complemented by two amplicon-sequencing reactions to cover GC-rich
ing a UBA1 mutation c.121A>G;p.Met41Val, but had not been diagnosed regions in SRSF2 and ASXL1. For the cytopenic cohort, we used our CH
with MDS yet. In addition, during this follow-up, median change in panel v.4 (Supplementary Table 10). For alignment of reads we used
RDW% was zero. In contrast, over a similar period (looking at histori- Burrow–Wheeler Aligner (BWA)-MEM v.2 (ref. 33). As MIP sequencing
cal records before cHSPC sampling; Extended Data Fig. 10e), median is cost-effective yet noisy, we developed an in-house variant calling
RDW% change in cases of MDS was 0.75, significantly higher than in method to reliably identify low-VAF CH events10. For the genotyp-
patients with cytopenia (Extended Data Fig. 10f; P = 0.001, two-sided ing panel we used Varscan for variant calling34. Each DNA sample was
Mann–Whitney U-test). Overall, these data support the accurate clas- sequenced twice with a minimum depth of 106 paired-end reads on an
sification of cytopenic cases. Eleven cHSPC samples were acquired Illumina Novaseq machine. Variant calling was performed as previ-
from patients under treatment, six of which were included in Fig. 4 ously reported10. Our genotyping panel allows for the simultaneous
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
detection of >2,000 SNVs. It includes heterozygous sites with at least they belonged. To this end, we correlated the genotypes of each cell
a 5% minor allele frequency from the 1,000 Genomes project, which cluster, as inferred by Vireo, to all genotypes that we measured using
were extensively covered in our data (at least 80 unique molecular the MIP panel (only using sites with sufficient sequencing depth). As a
modifiers (UMIs) across all cells in a test 10x library), excluding sites in control, this matching was performed against the MIP genotypes of all
repetitive elements and sex chromosomes. Both panels were designed individuals in the cohort and not only those from the specific library
using MIPgen35 to ensure capture uniformity and specificity. analyzed. We observed clear matchings between Vireo clusters and
individuals from the expected libraries in all cases. This method also
CH sequencing of high-RDW samples and controls correctly identified related individuals. The sex of all matched individu-
To compare propensity for CH and high-risk CH mutations in high-RDW als was confirmed by expression of XIST in the RNA data.
cases and normal RDW controls, we performed deep targeted sequenc-
ing of DNA samples from 602 high-RDW (>15%) individuals, whose Removal of droplets with megakaryocyte signatures
blood count did not meet MDS criteria (11.5 g dl−1 ≤ Hg ≤ 15.5 g dl−1 (F), Droplets with complete or partial megakaryocyte expression (at least
13 g dl−1 ≤ Hg ≤ 17 g dl−1 (M), 80 fL ≤ MCV ≤ 96 fl, PLT ≥ 100 × 109 l−1, Abs 5% of UMIs coming from a megakaryocyte gene program including
Neut ≥ 1.8 × 109 l−1) and 602 normal RDW, age- and sex-matched con- PF4, PPBP and 131 additional genes) were removed from our model as
trols. Case–control matching was performed using the R MatchIt pack- a result of their overall high doublet rate, and a final metacell model
age, balanced on age and sex, method = ‘nearest’, ratio = 1, from a total was constructed from the retained cells ((1) not marked as doublets,
of 18,147 individuals with longitudinal blood counts and available DNA (2) confidently assigned to an individual and (3) not exhibiting mega-
at the Tel Aviv Sourasky Medical Center (TASMC) Integrated Cancer karyocyte expression).
Prevention Center. All DNA samples were collected after obtaining writ-
ten informed consent in accordance with the Declaration of Helsinki Correcting for sequencing-platform bias
and were received de-identified from the TASMC. All relevant ethical Our 10x libraries were sequenced on Ultima Genomics and Illumina
regulations were followed and all protocols were approved by the sequencers. To minimize batch effects related to these sequencing-
TASMC ethics committee (under IRB protocol no. 02-130). platform variations, we used libraries that were sequenced on both plat-
forms to calculate an Illumina–Ultima correction factor per gene as the
ScRNA-seq processing mean log(fold-change) in expression of the gene across re-sequenced
2
We processed fastq files by executing cell-ranger (v.3.1.0) with an hg-38 libraries. We then normalized each Ultima-sequenced library by down-
reference genome. We filtered out cells with at least 20% mitochondrial sampling genes with at least 0.28 log(fold) Ultima overexpression
2
expression, then removed mitochondrial genes (as well as few other and resampling genes with at least 0.2 Illumina overexpression. The
batch-prone genes) and further filtered cells with ≤500 UMIs. downsampling and resampling were performed for each gene indepen-
dently, across all cells in each Ultima library. The thresholds for down-
Doublet calling sampling and resampling were chosen such that the overall number of
We performed several steps to assign cells to individuals and to detect UMIs per cells remained similar; 87 genes with at least 4-fold-change
doublets. Our pipeline included the following steps: between Ultima and Illumina were excluded from further processing.
(1) Demultiplexing cells and calling doublets based on SNPs
Computing the reference metacell model
found in the scRNA-seq data
Our metacell model was built using metacell2, with a target meta-
(2) Building a metacell model using cells from all libraries,
cell size of 200 cells, deriving 4,253 metacells. We marked histone,
including cells previously marked as doublets, identifying and
cell-cycle, ribosomal, sex-linked and stress response genes (including
removing metacells made of doublets
FOS and JUN) as forbidden genes, as well as genes with high technical
(3) Identifying doublet metacells based on expression of marker
variation, such as those with high or inconsistent differences between
genes
Illumina- and Ultima-sequenced technical replicates. These genes were
(4) Building the final metacell model and marking metacells as
not used for calculating gene–gene similarities but were included in
doublets based on expression markers
downstream analyses. We annotated metacells using known markers
In the first step, we identified doublets and assigned cells to indi- as illustrated in Extended Data Fig. 1c. We excluded metacells with low
viduals using Vireo v.0.3.2 (ref. 36) and Souporcell v.2.4 (ref. 37), which CD34 expression, such as mature monocytes, B cells, T cells, natural
cluster cells based on SNPs found in sequenced RNA molecules. We killer (NK) cells, dendritic cells (DCs) and endothelial cells, as well as
executed Vireo (preceded by running cellsnp v.0.3.0) and Souporcell 20 GMP-L metacells, from most downstream analyses. We used UMAP
on each library separately. Both methods used SNPs from our geno- projections of the metacell expression vector over genes with specific
typing panel10 which were covered by at least 20 UMIs in the library enrichment over cell types for visualization of the metacell manifold.
(in Souporcell—at least 10 from the major and minor allele each). We
observed high agreement in doublet calling between the two methods. BM comparisons and projections
In the next step, we built a metacell model with cells from all librar- We used three BM datasets for comparison purposes: a dataset includ-
ies. This model included cells that we already identified as doublets. ing CD34-enriched cells from two individual BM samples collected
The model was built with metacell2 (ref. 11), with a target metacell size by us and processed similarly to PB (Fig. 1a), the Human Cell Atlas
of 200 cells. We then marked all metacells, where at least 35% of the (HCA) BM dataset14 and a CD34+CD38− bead-based enriched BM data-
cells were already marked as doublets, and all metacells that expressed set12. We previously processed and annotated the HCA dataset in a
key markers of distinct cell types as doublet metacells. All cells that metacell model. We further constructed a metacell model for the two
belonged to a doublet metacell were then marked as doublets. We then CD34-enriched BM samples collected by us using metacell2, in a similar
built an additional metacell model (see below), without cells that were fashion to that described previously, and downloaded the Setty et al.
marked as doublets. sequencing data12, processed it by running cell-ranger, and created
a third BM metacell model from their data. To project our own PB
Assignment of cells to individuals data, our own BM data and the Setty CD34-enriched BM data on the
Vireo and Souporcell both cluster cells based on SNPs found in the HCA model, we correlated projected metacells from each of these
sequenced RNA, such that cells in the same cluster belong to the same models with HCA metacells over genes showing high variance in the
individual. We next assigned clusters of cells to the individual to whom HCA model. We annotated each Setty metacell using the mode of its
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
five most correlated HCA metacells. We annotated our own BM data CD34+ cell states into 11 bins from late MEBEMP differentiation through
using both the mode of the five most correlated HCA metacells and HSCs to late CLP differentiation (as ordered in Fig. 2b). We correlated
expression of gene markers. We projected metacells from each of these each of the 11 cell-state frequency vectors to the numerical label vec-
models on the HCA UMAP using the mean x and y values of the five most tor. We then looked at triplets of adjacent cell states in this order and
correlated HCA metacells. To compare S-phase genes between PB and calculated the mean correlation for each triplet to obtain nine mean
BM (Extended Data Fig. 3b), we calculated the S-phase signature (mean correlation values and took the maximal absolute correlation value
expression of six cell-cycle genes: TYMS, H2AFZ, PCNA, MCM4, HELLS as a test statistic. We repeated this process after permuting the label
and MKI67) for each PB and HCA metacell and plotted the distribution vector 10,000× and used the test statistics from the permutations to
of these scores across metacells for each cell type. derive a P value.
HSC differentiation gene programs CD34+ cell frequency in the OneK1K dataset
To visualize transcriptional dynamics in HSCs, we sorted MEBEMP and We built a metacell model for the cells from Yazar et al.25. We labeled
CLP metacells based on their AVP expression. To calculate differential all cells in metacells with high CD34 expression (log (fraction of
2
expression (DE) between HSCs and neighboring cell types (Extended UMIs > −14.3)) as CD34+ cells. We then selected individuals with at
Data Fig. 3g), we took the geometric mean expression of each gene least 800 cells in the model and randomly sampled 800 cells from
across each of these cell states (within HSC or CLP-M or MEBEMP-E each (Supplementary Table 14). To produce Fig. 3d, we pooled these
metacells) and calculated the difference of means between HSC and sampled cells by the decade of their individuals’ age and calculated the
MEBEMP-E and between HSC and CLP-M metacells. fraction of CD34+ cells in each decade. The 95% confidence intervals
shown in the figure assume a binomial distribution, given the very
DE between individuals unexplained by the metacell model sparse nature of the data.
We compared each individual’s pooled expression profile to a matched
expression profile based on the individual’s distribution across meta- Variably expressed gene modules
cells. We performed this analysis separately for MPPs or MEBEMPs We detected gene modules with high variance across individuals while
(MPP, GMP-E, MEBEMP-E/-L, ERYP and BEMP) and CLPs (CLP-E/-M/-L controlling for compositional variation. This was performed separately
and NKTDP). In each of these cell states, we downsampled each cell to for myeloid and lymphoid states, in the following manner:
have 500 UMIs and summed the UMIs across all cells of each individual,
normalized the sum to 1 and calculated the log(value) to obtain the (1) For each individual, we calculated the 5th percentile of their
2
observed expression. To compute matched expression, we downsam- number of UMIs across all MPP metacell cells and downsam-
pled each metacell to have 90,000 UMIs and summed all UMIs of the pled all cells to this number. We then pooled all downsampled
metacell to which each cell belongs for each individual. We normal- cells, normalized to sum to 1 and took the log(value). This
2
ized this matched expression to sum to 1 and took the log(value). For gave us the observed expression profile of each individual.
2
Extended Data Fig. 3c,d, we plotted all genes that were expressed in (2) We then created the expected expression profile for each
either the observed or the matched expression in at least one individual individual as follows: we partitioned all MPP metacells into 30
(log(expression) > 2−14.5 for MPPs or MEBEMPs, > 2−13.5 for CLPs), with equal size bins based on their AVP expression, and downsam-
2
at least a twofold change between matched and observed in at least pled metacells to 90,000 UMIs. We then took the average
one individual. We excluded genes exhibiting strong batch effects. expression of each gene across downsampled metacells in
each bin. This defined an expression profile for each of the
HSPC compositional analysis 30 bins. To obtain an individual’s expected expression, we
To explore variance in cell-type composition between individuals, calculated the weighted average expression profile of bins,
we first calculated the distribution of each individual’s cells across where the weight of each bin is proportional to the fraction
the CD34+ cell states. We further partitioned cells from the CD34+ cell of the individual’s cells from that bin, normalized to sum to
states into finer-grained bins, using one HSC, four CLPs and ten MPP 1 and took the log(value). We then calculated the difference
2
or MEBEMP bins, for a total of fifteen bins. We assigned HSC cells to bin between the observed and expected expression profiles.
0, CLP-E cells to CLP bin 1 and CLP-M/-L cells to CLP bins 2–4 based on (3) Our data showed some batch effect distinguishing sam-
an AVP expression gradient, such that each of these bins consisted of ples collected in two calendric periods. As this effect could
an equal number of cells. We similarly assigned MPP and MEBEMP-E/-L introduce co-variation between genes across individuals, we
cells into equal size MPP or MEBEMP bins 1–10 based on decreasing applied a correction controlling for it. This was performed
AVP expression. using a linear model fitting each gene to the sample collection
The bottom panel of Fig. 2d shows individual enrichment across period. We then subtracted the inferred period factor from
bins (log(ratio of each individual’s cell frequency in each bin to the the samples that were collected in the second period. We
2
median cell frequency in that bin across individuals)). We partitioned found that this approach substantially reduced emergence of
individuals into three groups based on their mean enrichment across gene clusters linked with sample collection date bias.
CLP bins 2–4—those with mean enrichment >0.5 are high CLP, those (4) We screened for genes with high variance that were unlikely
with <−0.5 are low and the rest are intermediate. We next defined the to be affected residually by the main manifold differentia-
stemness score as the ratio between the number of cells in MPP or tion process. We removed genes with high batch effects,
MEBEMP bins 1–5 and the total MPP or MEBEMP cells (bins 1–10). Indi- genes with high AVP correlation (absolute value Pearson’s
viduals with stemness score >0.5 had enriched stemness. Individuals correlation >0.65), and genes highly correlated (absolute
within each cluster were further sorted based on their stemness score. value Pearson’s correlation >0.5) with a module of differen-
The combination of CLP enrichment and stemness defines the six tially expressed genes between the first and second collec-
classes shown in the figure. tion periods. We then calculated each gene’s variance in
the difference between observed and expected expression
Test for association between cell-state compositions and a across individuals. As some of this variance can be explained
numerical label by sampling noise, we plotted each gene’s variance across
We used permutation tests to test for an association between cell-state individuals against its mean expression across individuals. We
distributions and a label, such as CBC indices or sync-scores. We sorted sorted genes by this expression value and subtracted from the
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
variance of each gene a rolling mean of the variances of 100 cells by their fraction of UMIs from the AVP and GATA1 signatures and
neighboring genes in that ordering. We chose genes with vari- partitioned them into 20 equal size bins of AVP signature expression
ance at least 0.08 higher than the rolling mean variance. and 20 equal size bins of GATA1 signature expression. The sync-score
(5) We calculated a gene–gene Spearman’s correlation matrix for is then defined as the fraction of cells in GATA1 bins 13 and above
the high variance genes and clustered correlation profiles us- (upper two quintiles of GATA1) that are in AVP bins 9 and above (upper
ing hierarchical clustering. We removed genes with low mean three quintiles of AVP expression). To visualize sync-scores (Fig. 3i),
correlation (<0.2) to their cluster and then removed gene we normalized this 20 × 20 bin matrix to sum to 1, smoothed the
clusters with low mean correlation between their genes obtained matrix by averaging cells using a running window of length
(≤0.25 mean correlation for all gene pairs). We further 3 and took the log(value).
2
computed gene–gene correlations using only samples from
our first library collection period and required gene clusters Differential gene expression with respect to age and CBC
to have a high mean correlation (>0.25) between their genes DE was performed separately for MPP and CLP cells as well as for men
when using only these samples. We removed additional gene and women. The MPP and CLP-M matrices previously used to detect
modules arising from this analysis resulting from batch effects variant gene modules were used here as well. Individual gene expres-
or traces of MEBEMP differentiation not normalized by this sion levels were correlated with age, maximal VAF of CH mutations
approach. This resulted in Fig. 3f. and 20 CBC indices using Spearman’s correlation; the correlation was
then tested for significance. The P values were false discovery rate
We performed a similar analysis for CLPs, with few differences. (FDR)-corrected (Benjamini–Hochberg) for each label separately. For
The analysis included all cells from CLP-M metacells. The cells were maximal VAF we additionally performed a Mann–Whitney U-test com-
partitioned into six equal size bins and partitioning was based on the paring individuals with and without detected mutations. DE between
average of their DNTT and VPREB1 expression. Genes with high absolute men and women was performed using a Mann–Whitney U-test on the
correlation to the average DNTT and VPREB1 expression were excluded. same expression matrices.
This was followed by hierarchical clustering of the gene–gene correla-
tion profiles and removal of genes as described for MPPs. Reconstruction of MDS classification models using improved
cell mapping and filtering
Age regression For analyzing MDS classification we re-analyzed sequenced libraries
We developed age-regression models for MPP and CLP expression of all disease cases and healthy individuals in two groups, separated
separately. To predict age, we used the difference between an indi- by sequencing platform (Illumina and Ultima). Cell filtering was then
vidual’s observed and expected gene expression as described above applied for each of the two datasets using the process described above
(‘Variably expressed gene modules’). We used genes with minimal with the following minor modifications:
expression ≥2−14.5 for MPPs and ≥2−15.5 for CLPs across individuals. We
trained a LASSO (least absolute shrinkage and selection operator) – Re-mapping all cells using cell-ranger v.7.0.1
model using nested leave-one-out cross-validation. For each left-out – Both Vireo and Souporcell were limited to 7.4 M SNPs with minor
sample, we performed cross-validation on the remaining samples to allele frequency >0.05 according to the 1,000 Genome project,
select LASSO’s λ parameter, trained a model using the selected λ and rather than SNPs from our genotyping panel
made a prediction on the left-out sample. – Refined filter for cell exclusion, excluding 10× particles (cells)
with high mitochondrial content (>20%), platelet signature
The LMNA signature (PPBP > 0.2%), neutrophil signature (LCN2, CAMP and LTF) or
We used the difference between an individual’s observed and expected erythrocyte signature (HBB, HBA1 and HBA2), and also excluding
gene expression and correlated this difference to the difference in cells with low signature of nuclear RNAs (Supplementary Table 9
LMNA expression separately for MPPs and CLPs. We then summed includes number of excluded cells)
the MPP and CLP correlation values and kept genes with summed cor- – Adjusting the doublet detection algorithm described above with
relation >0.7. We further removed genes with high technical variance, an additional filter involving clustering cells and removal of cells
retaining 17 genes in the LMNA signature. To calculate individual LMNA with UMI count that is higher than 2.5-fold of their computed clus-
signatures, we took the average value of these 17 genes in the observed– ter median (thereby compensating for variable cell sizes across
expected matrix of each individual for MPPs and CLPs separately. To types). In addition, cells with high expression of both monocyte
plot Extended Data Fig. 6g, we calculated the geometric mean of LMNA and MEBEMP markers were filtered out. Such extra steps were
signature gene expression for each individual in each one of the ten needed because, in some disease batches, highly specific cell
MPP or MEBEMP bins described earlier in Fig. 2d. states could contaminate other samples more than in standard
reference batches.
GoT analysis
GoT21 performed on sample N122 allowed us to mark this individu- In silico sorting for inferring sample cHSPC compositions
al’s cells as wild-type or mutated. As a result of the low VAF of N122’s To estimate cHSPC state for a given single-cell transcriptional profile,
DNMT3A mutation, and to increase power, we marked cells with a an in silico sorting scheme was developed (Extended Data Fig. 7a). First,
DNMT3A mutation status that could not be determined by GoT as our original reference model was used to compile gene signatures.
wild-type cells. For Extended Data Fig. 6b, we examined sample N122’s Each signature was based on genes differentially expressed in a given
cell distribution across cell states. cell type, such that the total number of UMIs for the signature is suf-
ficiently high to allow classification at single-cell resolution (selected
Sync-score gene sets in Supplementary Table 13). Extended Data Fig. 7a shows the
We defined the AVP signature to include genes with high correlation gating strategy used for classification using signature scores (log(total
2
(>0.6) to AVP across HSC, MPP and MEBEMP metacells and the GATA1 signature UMI in cell) − log(total cell UMI)). Cells with ambiguous gat-
2
signature to include those with high correlation (>0.7) to GATA1. ing were defined as unassigned. We confirmed that the gating strategy
We filtered out genes with mean relative expression >2−10 in these yields classification that is consistent with the annotation derived by
metacells, to preclude a small number of genes from dominating the applying metacell analysis to the new Fig. 4 reference model (see below)
signatures. We then scored all HSC, MPP, MEBEMP-E and MEBEMP-L by projecting inferred classes on the metacell model UMAP projection
Nature Medicine
Resource https://doi.org/10.1038/s41591-025-03716-5
(Extended Data Fig. 7b). We noted that sorting may reduce the manifold the appropriate biasGCbin value, generating eo
gm
bs′, which is used to obtain
resolution compared with metacell analysis, but it provides robust a per-gene and metacell observed:expected expression log(ratio)
results for downstream MDS classification purposes. δgm=log
2
(ϵ+eo
gm
bs′ )−log
2
(ϵ+ep
gm
roj), whereas ϵ=10 −5.
We split each chromosome to contiguous bins encompassing
Healthy donor reference model for MDS analysis 20 genes (ignoring filtered genes). For each chromosome bin
Samples from 79 individuals who were sequenced on the Illumina bchrom and each metacell m, the median log ratio was computed:
platform and showed no evidence for disease were considered as the δm,bchrom=Medg∈bchrom(δgm).
reference model for MDS classification (Fig. 4). This cohort was used for The matrix δm,bchrom of metacells and 20-gene bins describing
defining the normal distribution of cHSPC composition. It was also the estimated DE was then normalized by subtracting the median of each
basis for constructing a reference metacell model used for projecting row (metacell) and visualized in a heatmap, where metacells were
patient data. This model includes 287,000 cells and 2,090 metacells, re-ordered using hierarchical clustering. Heatmaps of the derived
constructed using metacell2 with a target metacell size of 140 cells matrices (see, for example, Extended Data Fig. 10a,b) were examined
and other parameters similar to the original normal reference model. manually to identify CNAs (Extended Data Fig. 7c and Supplementary
Table 12).
Grouping MDS and cytopenia patients by composition
We used the inferred cHSPC compositions of 70 donors in the Fig. 4 Within-state gene signatures
reference model to score each composition abnormality of patients Within-state correlated gene sets were inferred from the reference
with MDS and cytopenia. Composition vectors p over cell types were metacell model by clustering the gene–metacell expression matrix of
log-transformed first as lp=log (ϵ+p) where ϵ = 0.02. The distance each annotated cell type, while considering only highly variable genes
2
between two samples was then defined using a Euclidean distance within the cell type. Clusters were evaluated and selected manually
between their lp vectors. The abnormality score of a new sample was and expanded by adding correlated genes, resulting in the final gene
defined as the average distance for the four nearest neighbors in the sets (Supplementary Table 13). An MHC-II gene set was added after
reference model. The 0.98 quantile of the abnormality score of healthy observation of MDS DE compared with the reference. The signature
donors (excluding reference donors) was used as a threshold (Extended score per cell was estimated as the log-transformed normalized total
Data Fig. 8a) for classifying patient compositions (excluding four UMI count for each gene set.
patients exhibiting complex karyotypes) as normal or abnormal Signature scores per patient were extracted using the median
(Fig. 4b; GRP1 or GRP2-4, respectively). Patients with abnormal com- signature of cells within a respective cell type (following the in silico
positions were further grouped using hierarchical clustering of their sorting process described above). In the case of too few such cells, the
lp vectors. Patients with normal compositions were ordered along a signature score was considered missing (NA).
CLP frequency gradient in Fig. 4b (left), in analogy with Fig. 2d. After classification of patients with cytopenia and MDS into groups
1–4 (Fig. 4b), we performed, for each within-state gene signature (and
Estimating patients’ CNAs using scRNA projection on the each relevant state), a Kruskal–Wallis test comparing signature expres-
reference sion levels between groups 1–4 and healthy donors. The signatures
We constructed a metacell model from the filtered cells of each patient with the lowest P values were the MEBEMP-L MHC-II, S-phase and BEMP
separately. This model was projected over the Fig. 4 reference model, early signatures, which were accordingly shown in Fig. 4e and Extended
using MCProj38. The result was a set of metacells for the patient, such Data Fig. 8d.
that each metacell m was defined by its observed gene expression eobs
gm
and projected gene expression eproj, as determined by MCProj using Features for MDS classification
gm
best matching reference behavior. Expression values were calculated The following features were collected to facilitate MDS classification:
using the geometric mean. Genes were filtered to remove sex-specific
and sequencing-platform-specific genes (559 genes overall; Supple- – CBC values: we used the values with minimal time gap from the
mentary Table 15). Further filtering was done for 107 genes showing a cHSPC sampling date
consistent difference between observed and projected values over all – Maximal CH VAF across mutations detected in the same blood
individuals, as well as 27,317 lowly expressed genes (Supplementary sample that was used for scRNA-seq
Table 15). – The cHSPC compositions as inferred through in silico sorting
To correct for batch effects leading to small GC content preference – Twenty-one signature scores
per library, we grouped genes into ten equal size bins according to – Composition abnormality score (ʽGrouping MDS and cytopenia
the average GC content of 3′-scRNA-sequenced tags in representative patients by compositionʼ)
sequenced libraries. For each gene g, we computed total observed and – Number of CNAs.
expected UMI counts, given the model’s projection on the reference:
We noted that signature scores might be missing (as a result of
no g bs=∑nc×eo gm bs (c) insufficient number of cells). In addition, a few individuals were miss-
c ing CBC values.
All feature values per scRNA sample are included in Supplemen-
np
g
roj=∑nc×ep
gm
ro
(
j
c)
tary Table 9.
c
MDS classifier training and testing
where nc is the total number of UMIs for the cell c and m(c) is its metacell. XGBoost (xgboost Python package, v.2.0.3) training was performed on
The bias per GC bin biasGCbin is now approximately defined as the cohort 1 including 89 samples (41 normal, 20 cytopenia and 28 MDS).
median of no g bs across genes in the GC bin. In practice, we calculated All of the samples in cohort 1 were sequenced on the Ultima platform.
np
g
roj
MDS (including MDS or myeloproliferative neoplasms) samples were
the ratio no g bs after normalizing nobs and nproj by ∑ nobs and considered positive, whereas cytopenia and normal samples were
np
g
roj g g g′ g′
considered negative.
∑ nproj, respectively, and adding a regularization term of 10 −5. We applied feature selection separately in each leave-one-out
g′ g′
We corrected each observed gene expression value eobs by dividing by fold, selecting a subset of the features for which the FDR-corrected
gm
Nature Medicine
