---
source_path: /mnt/c/Users/Administrator/Zotero/storage/6DFRICW3/Wang 等 - 2025 - Proteotoxic stress response drives T cell exhaustion and immune evasion.pdf
ingested: 2026-04-23
sha256: 42e1b16fa075eb88
---

Article
Proteotoxic stress response drives T cell
exhaustion and immune evasion
https://doi.org/10.1038/s41586-025-09539-1 Yi Wang1, Anjun Ma1,2, No-Joon Song1, Ariana E. Shannon1,2, Yaa S. Amankwah1,
Xingyu Chen3, Weidong Wu2, Ziyu Wang1, Abbey A. Saadey4, Amir Yousif4, Gautam Ghosh2,
Received: 12 June 2024
Jay K. Mandula1, Maria Velegraki1, Tong Xiao1, Haitao Wen1,4, Stanley Ching-Cheng Huang4,
Accepted: 15 August 2025 Ruoning Wang5, Christian M. Beusch6,7, Abdelhameed S. Dawood6, David E. Gordon6,
Mohamed S. Abdel-Hakeem6, Hazem E. Ghoneim1,4, Gang Xin1,4, Brian C. Searle1,2 &
Published online: xx xx xxxx
Zihai Li1,8 ✉
Open access
Check for updates
Chronic infections and cancer cause T cell dysfunction known as exhaustion. This cell
state is caused by persistent antigen exposure, suboptimal co-stimulation and
a plethora of hostile factors that dampen protective immunity and limit the efficacy
of immunotherapies1–4. The mechanisms that underlie T cell exhaustion remain
poorly understood. Here we analyse the proteome of CD8+ exhausted T (T )
ex
cells across multiple states of exhaustion in the context of both chronic viral
infections and cancer. We show that there is a non-stochastic pathway-specific
discordance between mRNA and protein dynamics between T effector (T ) and T
eff ex
cells. We identify a distinct proteotoxic stress response (PSR) in T cells, which we
ex
term T -PSR. Contrary to canonical stress responses that induce a reduction in
ex
protein synthesis5,6, T -PSR involves an increase in global translation activity and
ex
an upregulation of specialized chaperone proteins. T -PSR is further characterized
ex
by the accumulation of protein aggregates and stress granules and an increase in
autophagy-dominant protein catabolism. We establish that disruption of proteostasis
alone can convert T cells to T cells, and we link T -PSR mechanistically to persistent
eff ex ex
AKT signalling. Finally, disruption of T -PSR-associated chaperones in CD8+ T cells
ex
improves cancer immunotherapy in preclinical models. Moreover, a high T -PSR in
ex
T cells from patients with cancer confers poor responses to clinical immunotherapy.
Collectively, our findings indicate that T -PSR is a hallmark and a mechanistic driver
ex
of T cell exhaustion, which raises the possibility of targeting proteostasis pathways as
an approach for cancer immunotherapy.
T cell exhaustion represents a hypofunctional state characterized by Although transcriptomic profiling has provided insights into T
ex
reduced effector function and increased inhibitory receptor expres- cell biology, mRNA abundance is not always a faithful proxy of protein
sion that arises from persistent antigen exposure and a hostile micro- expression across various organisms18–22. Previous studies have revealed
environment7. T cells observed in cancer fail to eliminate malignant poor mRNA–protein correlation in T cells regardless of functional
ex
cells, and this limitation mediates a key mechanism of resistance to status23–25 and the importance of post-transcriptional regulation in
immunotherapies1–3. The exhaustion program generates a heterogene- T cell differentiation and function26. In this context, a high-resolution
ous T cell population. Progenitor T (T ) cells retain stemness and proteomic map of T cells would be valuable. In this study, we define
ex ex prog ex
self-renewal capacity that respond to immune checkpoint blockade the proteomic landscape of T cells across various settings, including
ex
(ICB) therapies and differentiate into intermediate T (T ) cells with an in vitro exhaustion model, in vivo chronic lymphocytic choriomen-
int
cytolytic capacity8–10. Conversely, terminal T (T ) cells accumulate ingitis virus (LCMV) infection in mice, and colon tumour and bladder
ex tex
over time and respond poorly to ICB therapies8,11–13. T cell exhaustion tumour mouse models. We demonstrate that there is pathway-specific
also limits the efficacy of chimeric antigen receptor (CAR) T cell therapy discordance between transcript and protein levels.
against solid tumours14–17. Consequently, a better understanding of We also elucidate the intricate layers of protein-level regulation per-
T cell exhaustion is essential to overcome the limitations of current taining to a PSR that is specific to T cells. We show that PSR in T cells
ex ex
immunotherapies. shares similarities to unfolded protein responses and integrated stress
1Pelotonia Institute for Immuno-Oncology, The Ohio State University Comprehensive Cancer Center–The James, Columbus, OH, USA. 2Department of Biomedical Informatics, College of
Medicine, The Ohio State University, Columbus, OH, USA. 3Johns Hopkins University, Baltimore, MD, USA. 4Department of Microbial Infection and Immunity, College of Medicine, The Ohio State
University, Columbus, OH, USA. 5Center for Childhood Cancer, Hematology/Oncology and BMT, Abigail Wexner Research Institute at Nationwide Children’s Hospital, Department of Pediatrics,
The Ohio State University, Columbus, OH, USA. 6Department of Pathology and Laboratory Medicine, Emory University, Atlanta, GA, USA. 7Department of Surgical Sciences, Uppsala University,
Uppsala, Sweden. 8Division of Medical Oncology, Department of Medicine, College of Medicine, The Ohio State University, Columbus, OH, USA. ✉e-mail: Zihai.li@osumc.edu
Nature | www.nature.com | 1
Article
responses. However, a marked difference is that PSR in T cells is char- T cells from Armstrong infection; and SLAMF6+CX3CR1– T , CX3CR1+
ex prog
acterized by increased global protein synthesis. This T cell-associated T and SLAMF6–CX3CR1– T cells from clone 13 infection (Extended
ex int tex
PSR signature, which we term T -PSR, is further marked by the selective Data Fig. 3a). We applied a previously defined transcriptomic signa-
ex
activation of chaperone proteins such as gp96 (also known as GRP94; ture for T cell exhaustion30 to analyse our proteomic data. Notably, in
encoded by Hsp90b1) and BiP (encoded by Hspa5) and the accumula- addition to increased expression of protein signatures associated with
tion of protein aggregates that are predominantly driven by sustained exhaustion and pro-apoptosis, T cells exhibited a marked enrichment
tex
activation of the AKT pathway. The introduction of misfolded proteins of proteins in the PSR pathway (Fig. 1b). We applied the same gene sig-
alone could convert T cells to T cells, which demonstrates the cau- natures to a single-cell RNA sequencing (scRNA-seq) dataset of mouse
eff ex
sality of dysregulated proteostasis in T cell exhaustion. Finally, we gp33+CD8+ T cells after LCMV clone 13 infection31. The upregulation of
demonstrate that T -PSR is also a hallmark of human T cells in cancer PSR in T cells was readily discerned at the protein but not the transcript
ex ex ex
and that it may contribute to resistance to cancer immunotherapy. level (Extended Data Fig. 3b). We also generated a proteomic dataset of
transgenic T cells against a Db-restricted gp33 epitope of LCMV (called
P14) at days 8, 15 and 30 after infection32 (Extended Data Fig. 3c). PSR
Discordance between RNA and protein levels
was similarly upregulated in P14 cells after clone 13 infection but not
To determine whether gene expression levels reflect protein expres- Armstrong infection (Extended Data Fig. 3d).
sion levels in T cells, we used an established in vitro exhaustion model To further investigate proteome dynamics and PSR in T cell exhaus-
that induces T cell exhaustion through repeated T cell receptor (TCR) tion, we performed proteomic analyses of T and T cells generated
eff ex
stimulation27,28. We then performed parallel RNA sequencing and in vitro, which enabled us to achieve increased proteome coverage.
quantitative proteomics by mass spectrometry (MS) (Extended Data T cells were collected on days 2, 4, 6 and 8 after initial activation to
Fig. 1a). Compared with acutely activated T cells (T cells), chronically track proteomic dynamics during T cell activation and exhaustion
eff
stimulated cells (T cells) exhibited impaired survival, proliferation and as described above (Extended Data Fig. 1a). T cells exhibited distinct
ex
cytokine production, which were accompanied by increased expression protein expression dynamics depending on the differentiation state
levels of exhaustion markers, including PD1 and TIM3 (Extended Data (Fig. 1c). The expression dynamics of key activation, exhaustion and
Fig. 1b,c). To improve detection sensitivity, quantification and repro- stemness markers, such as TCF1, SLAMF6, PD1 and TIM3, obtained
ducibility, we applied the chromatogram library approach for all prot- by MS analyses aligned well with T cell states (Extended Data Fig. 4a).
eomic data collection (Extended Data Fig. 1d). The expression dynamics Overall, eight distinct clusters of proteins were identified (Fig. 1c and
of key activation, exhaustion and stemness markers of T cells, such as Extended Data Fig. 4b). Notably, proteins in cluster 6 were specifically
CD25, PD1, CD39 and TCF1, obtained from the MS results aligned well upregulated in T cells, which typically expressed exhaustion markers
ex
with data obtained by spectral flow cytometry (Extended Data Fig. 1e). such as TIM3, CD39 and LAG3 (Fig. 1c), as well as molecules involved
We then ascertained whether transcript levels are a reliable surrogate in protein transport, modification and quality control (Fig. 1d). In par-
for protein expression levels in T cells. In both T and T cells, mRNA ticular, proteins involved in the endoplasmic reticulum (ER) stress
eff ex
and protein expression levels were weakly correlated, as indicated response were significantly increased as T cells became more exhausted
by Pearson’s correlation coefficients of 0.31 and 0.38, respectively (Fig. 1e). An increase in the expression of proteins integral to transla-
(Extended Data Fig. 2a). Moreover, the degree of correlation between tion, transport and quality control in T cells compared with T cells
ex eff
RNA and protein levels did not seem to be stochastic but were function- indicates that there is an induction of a distinct PSR during the T cell
ally related (Extended Data Fig. 2b,c). A group of proteins that exhibited exhaustion process (Fig. 1e).
comparable mRNA and protein expression levels in >300 cancer cell We next performed a proteomic study of T cells isolated ex vivo
lines29, termed ‘housekeeping’ in this context, aligned well with RNA from the tumour milieu of mouse models of MC38 colon cancer and
expression levels in T cells (Extended Data Fig. 2b). Proteins involved MB49 bladder cancer (Fig. 1f). Antigen-experienced CD44hiCD8+ T cells
in the regulation of TCR signalling, cell death and cytokine responses were sorted by flow cytometry into T , T and T cells8,11 (Fig. 1g).
prog int tex
exhibited a similarly strong correlation with RNA expression levels, with In the MC38 tumour model, the T population exhibited upregulated
tex
correlation coefficient values of around 0.7. By comparison, transcrip- proteins associated with the ER stress response and proteins associ-
tion factors (TFs) exhibited a moderate correlation between mRNA and ated with autophagy and transport (Fig. 1h). The upregulation of ER
protein expression levels, with some TFs showing detectable changes stress proteins was also observed in T cells isolated from MB49 bladder
exclusively at the protein level, including FOXO1 and T-bet (Extended tumours (Fig. 1h).
Data Fig. 2c,d). Furthermore, the levels of proteins associated with Chaperone proteins are crucial for ensuring protein quality con-
metabolic processes, post-transcriptional regulation and epigenetic trol. Notably, we observed a heterogeneous expression of chaperones
regulation aligned poorly with mRNA levels (Extended Data Fig. 2c). (Fig. 1i). On the basis of their expression patterns, we categorized them
The three major metabolic pathways—glycolysis, oxidative phospho- into three groups: quiescence, activation and PSR chaperones (Fig. 1i).
rylation and fatty acid metabolism—showed discrepancies between The quiescence-related chaperones showed the highest expression in
RNA and protein levels, with most of the changes in mRNA levels not naive T cells. The second group of chaperones, compromising cyto-
reflected at the protein level (Extended Data Fig. 2e). These results solic HSP90α and HSP90β, TRiC complex subunits (TCP1α–TCP1θ)
underscore the importance of directly defining the proteome rather and mitochondrial chaperone HSP75 (also known as TRAP1), were
than inferring it from the transcriptome. induced by TCR stimulation but reduced in T cells, which implicated
ex
a link with T cell activation. Conversely, proteins in the third group,
including several ER chaperones such as BiP and gp96, were overex-
PSR and specialized chaperone enrichment
pressed in T cells, which indicated that they may have specialized
ex
We next generated a kinetic proteomic landscape of T cells during T cell roles in T cell exhaustion. These exhaustion-associated chaperones
exhaustion by leveraging the LCMV infection model. Antigen-specific were significantly upregulated in the T cell population from both
tex
CD8+ T cell subpopulations were isolated after acute (Armstrong strain) MC38 and MB49 tumours (Fig. 1j). We performed additional analyses of
or chronic LCMV (clone 13 strain) infection and analysed (Fig. 1a). The proteomes of LCMV-specific T cells and tracked the expression kinetics
following endogenous CD8+ T cell subpopulations specific for viral anti- of these chaperones during chronic infection (Extended Data Fig. 3c).
gens (gp33 and gp276) were sorted for MS analysis at days 8 and 30 after Consistently, BiP, gp96 and HSPA13 were upregulated in P14 cells from
infection: short-lived effector T cells (SLECs), memory precursor effec- mice infected with clone 13, whereas the expression of TRiC complex
tor cells (MPECs) and central memory (T ) and effector memory (T ) subunits was downregulated (Extended Data Fig. 3e). Together, these
CM EM
2 | Nature | www.nature.com
106 50 105 0 M Co C lo 3 n 8 10 0 4 –50
–104 –100
–104 0 104 105 –100–50 0 50
PC1 (32.1%)
106 105
Bladder 104
MB49 0
–104
0 104105106
Nature | www.nature.com | 3
)%6.81( 2CP
Teff Tex
50
0
–50
–100
–100–50 0 50100
PC1 (32.7%)
)%4.81(
2CP
TIM3–BV711
Protein folding chaperone (GO: 0044183)
CPA–6FMALS
ER to Golgi vesicle-mediated transport
Response to ER stress
Organelle organization
Protein N-linked glycosylation through asparagine
Protein glycosylation
Endomembrane system organization
Protein N-linked glycosylation
Protein insertion into ER membrane
ERAD pathway
Co-translational protein targeting to membrane
0 5 10 15 20
–log[adjusted P]
Naive D2 D4 D6 D8 D4 D6 D8
Response to ER stress
Protein quality control
Cytoplasmic translation
Mitochondrial translation
Translation
Protein transport
TCR stimulation
mRNA processing
Epigenetic regulation
Glycolytic process
Fatty acid catabolism
Oxidative phosphorylation
Activation score
CD44hiCD8+ Colon Bladder
Tprog Ttex Tprog M T C in 3 t 8 Ttex Tprog M T B in 4 t 9 Ttex Response to ER stress Tint Intracellular protein transport
Tint
Autophagy
Cytoplasmic translation
CD44hiCD8+ Mitochondrial translation
Oxidative phosphorylation Tprog
Fatty acid catabolism
Glycolytic process
Tint
Ttex
TIM3–BV711
Colon MC38
Tprog Tint Ttex
Quiescence
Activation
Tex-PSR
Bladder MB49
Tprog Tint Ttex
Quiescence
Activation Tex-PSR
Activation score
–2 0 2
CPA–6FMALS
a b
L A C rm M s V trong S K C L L D E R 1 C G 27 1 – + M K C L D P R 1 E G 2 C 7 1 + – T CCDM62L+ T C C ED D M6 1 2 2 L 7 – hi SLE D C 8 A M rm PEC Tpro D g 8 Cl13 Tint T D CM 30 A T rm EM Tprog D30 T i C nt l13 Ttex
Naive or memory
Activation or effector function
Exhaustion
Day 8 Day 30 TCR signalling
Gated on CD44higp33 and gp276 tetramer+ Cytokine or cytokine re A c n e e p r t g o y r
L cl C o M ne V 13 T S C pL X roA 3 gM CR F 1 6 – + T CinXt3CR1+ T S C pL X roA 3 gM CR F 1 6 – + T CinXt3CR1+ T StLexAMF6– Proteotoxic N M s F t A r - e P κ s B K s A s s re i i d g g s h n n p e a a o s l l n l l i i i o n n s g g n e
CX3CR1– Pro-apoptosis
Activation score
Day 8 Day 30
–2–1012
c Teff Tex d
Naive D2 D4 D6 D8 D4 D6 D8
CD25
1
T-bet
GZMA 2
RUNX3
3 SLAMF6
TCF1
IFNγ e PD1
4
5 CPT1A
GZMB
6
TIM3
7
TFAM
8 CD28
z score
–4 0 4
–2 –1 0 1 2
f g h
M M B C 4 3 9 8 b c la o d lo d n er Tprog (s.c.) TIL isolation Ttex 14 days
Cell sorting MS
Tprog Tint
Activation score
Ttex
–1 0 1
i j
Quiescence Activation Tex-PSR
Naive
D2
z score
D4 4
Teff D6
2 D8
D4 0
Tex D6 −2
D8
D D F N FA AJB F 1 UB P P D 2 C T L a 3 p H a a s m in arti W n IPF1 TCP1 T β CP T 1 C γP T 1 C δP T 1 C εP T 1 C ζ P1 T ζ C 2 P1 T η CP H 1 S θ P H 84 S H P S 8 P 6 A H 1 S B PA H 1 S L PA H 2 SP H A4 SP H A S 8 P H 1 S 0 P P H F 1 D P N F 1 DN TC 2 P1 H α SP75 ZPR A 1 P A L N C F P a 3 lr 2 e E tic C u C l C i D n C C D 4C 712 C 3 D L N PX AJB FK 6 BP8 gp H 9 S 6 PA14B H IP S H P S A P 9A H 4L S G P R 60 P17 M 0 ES R T D ic o - r 8 s A in-1A −4
Fig. 1 | PSR is triggered in T cells with a dynamic expression of chaperone proteomic analysis of CD8+ T cells in different exhaustion states from the MC38
ex
proteins. a, Schematic of the experiment to isolate mouse splenic LCMV colon cancer mouse model and the MB49 bladder tumour mouse model. s.c.,
antigen-specific CD8+ T cell subpopulations in LCMV acute (Armstrong (Arm)) subcutaneous. g, Principal component analysis plots of proteomes of T , T
prog int
and chronic (clone 13 (Cl13)) infection models. b, Heatmap of expression levels and T cells (n = 3, each biological replicate was pooled from 12–13 mice).
tex
of proteins belonging to 11 T cell signatures across 9 groups (n = 3–4, representing h, Heatmap of protein expression across eight gene ontologies in three CD8+
pooled 5–15 mice per replicate). D, day. c, Heatmap of the expression profiles of T cell subpopulations from MC38 and MB49 tumour models. i, Bubble plot of
5,284 proteins quantified in naive T cells, acutely activated T cells (T ) and the expression levels of protein-folding chaperones in naive, T and T CD8+
eff eff ex
chronically activated T cells (T ) at 2, 4, 6 and 8 days after initial activation, as T cells generated in vitro as described in Extended Data Fig. 1a. The bubble
ex
described in Extended Data Fig. 1a, with k-means clustering identifying 8 distinct colour intensity is proportional to the protein expression level. The bubble size
expression patterns (n = 4, each replicate was pooled from 3 mice). d, Enrichment is proportional to the absolute z score value. j, Heatmap of the expression
analysis of proteins from cluster 6 defined in c (one-sided Fisher’s exact test levels of chaperone proteins (defined in i) in three CD8+ T cell subpopulations
with Benjamini–Hochberg correction). e, Heatmap of expression levels of from MC38 and MB49 tumours. The diagrams in a and f were created using
proteins belonging to 12 gene ontology terms. f, Schematic of MS-based BioRender (https://www.biorender.com).
Article
findings indicate that the activation of PSR and the associated upregu- T cells also exhibited increased proteasome and lysosome activ-
ex
lation of PSR chaperones are a common hallmark of T cell exhaustion. ity (Extended Data Fig. 7g,h). We therefore investigated the kinetics
of global protein catabolism in T cells. Cells were labelled with HPG
ex
for 30 min, then changed to regular culture conditions without HPG.
Dysregulated proteostasis in T cells
ex Although nascent proteins were produced in high levels, they were
Our proteomic data indicated that PSR is activated in T cells. We next rapidly degraded in T cells (Extended Data Fig. 7i). This protein catabo-
ex ex
examined whether proteostasis in T cells is disrupted. We stained T lism in T cells was driven largely by autophagy (Extended Data Fig. 7j).
ex eff ex
and T cells with the fluorescent dye NIAD-4 or its derivative CRANAD-2, Taken together, these results show that T cells have a distinct
ex ex
which bind to amyloid-like structures enriched in misfolded proteins non-canonical PSR, which we term T -PSR. T -PSR is characterized
ex ex
and aggregates33. T cells showed a significant accumulation of protein by the induction of PSR and the formation of SGs, protein aggregate
ex
aggregates compared with T cells (Fig. 2a,b). In tumour-infiltrating accumulation and increased protein catabolism, coupled paradoxically
eff
T cells (TILs) isolated from MC38 and MB49 tumours, protein aggre- by enhanced global protein synthesis.
gates progressively increased as T cells became more exhausted
(Fig. 2c,d). This result suggests that the protein quality control system
Molecular definition of protein aggregates
is significantly impaired in T cells.
ex
The activation of PSR, the upregulation of specialized chaperone We next asked what proteins were prone to aggregation in T cells. To
ex
proteins and the accumulation of protein aggregates in T cells led that end, we used native gel electrophoresis to analyse the migration
ex
us to initially predict that T cell exhaustion is associated with attenu- pattern of proteomes (Fig. 2g). On the basis of proteome characteriza-
ated translation to prevent further protein overload. However, this tion, we focused on the following three differentiation states of T cells:
prediction was incorrect based on the following considerations. First, T cells (day 4 acutely activated T cells); early T cells (day 4 chronically
eff ex
proteins with internal ribosome entry sites (IRES) that are not subject activated T cells); and late T cells (day 8 chronically activated T cells)
ex
to EIF2α-mediated translation attenuation should be enriched rela- (Extended Data Fig. 4c,d). Both early and late T cells showed upregu-
ex
tive to proteins without IRES in T cells34. However, this was not the lation of ER stress responses compared with T cells (Extended Data
ex eff
case (Extended Data Fig. 5a). Second, we did not observe enrichment Fig. 4e,f). To define aggregation-prone proteins, T , early and late T
eff ex
of proteins that rely on the alternative translation initiation factor cells were first lysed with mild lysis buffer to maintain their native con-
EIF2A owing to the presence of an unconventional 5′ upstream open formation followed by high-speed centrifugation to remove nucleoli
reading frame35 (Extended Data Fig. 5b). Third, proteins with concur- and other insoluble materials. Supernatants were then subjected to
rent upregulation at RNA and protein levels in T cells were overrep- native PAGE electrophoresis. Proteins that migrated below 140 kDa (low
ex
resented in translation initiation, elongation and stress-response molecular weight (LMW) species) and above (high molecular weight
pathways (Extended Data Fig. 5c). Fourth, levels of the translation (HMW) species) from the gel were then defined by MS. We detected
repressor PDCD4 (refs. 36,37) were significantly reduced in T cells and quantified 3,889 proteins, and 2,878 of these proteins (74%) shifted
ex
both in vitro and in vivo (Extended Data Fig. 5d). Fifth, our proteomic from LMW to HMW species in T cells. This finding indicated that there
ex
analysis revealed an upregulation of translation but not transcriptional was a large-scale level of protein aggregation in the exhaustion state
machinery in T cells (Extended Data Fig. 5e–g). Proteins involved in (Fig. 2h). We next examined whether proteins associated with specific
ex
translation were upregulated in T cells induced by chronic LCMV pathways were preferentially aggregated in T cells. However, there was
ex ex
clone 13 infection (Extended Data Fig. 6a). Moreover, the translation no such preference, which suggested that protein aggregation occurred
initiation factors EIF2D and EIF4G3 exhibited sustained high expression globally (Fig. 2i). Still, effector molecules, including granzyme B, gran-
in P14 cells from mice with chronic infection but were reduced over zyme C and perforin, in T cells showed significant enrichment in HMW
ex
time in mice with acute infection (Extended Data Fig. 6b). species compared with T cells (Fig. 2j). The T -PSR chaperones gp96
eff ex
These findings prompted us to directly assess translation rates by and BiP also showed a trend in moving towards HMW species. Notably,
measuring the incorporation of l-homopropargylglycine (HPG), a AKT1 did not demonstrate signs of aggregation in T cells (Fig. 2j). We
ex
methionine analogue, into newly synthesized proteins. Notably, T also resuspended and profiled proteins in insoluble material through
ex
cells exhibited a significantly increased rate of protein synthesis additional harsh lysis (Extended Data Fig. 8a). We observed an enrich-
compared with acutely stimulated T cells (Fig. 2e). We also meas- ment of granzyme B in T cells compared with T cells (Extended Data
eff ex eff
ured translation changes in vivo in different TIL subsets by injecting Fig. 8b). The inhibitory receptor PD1, despite being a transmembrane
O-propargyl-puromycin (OPP) into mice with MC38 tumours to label protein, was retained in the soluble fraction (Extended Data Fig. 8c).
elongating polypeptide chains during active translation38. T cells Next, we used immunoblotting to validate the aggregation state of
tex
showed significantly higher OPP incorporation than T and T cells some of the identified proteins (Fig. 2k). In T cells, granzyme B and
prog int ex
(Fig. 2f). We validated this result by isolating TILs into single-cell sus- perforin showed a migration pattern above 242 kDa, which was in con-
pensions followed by ex vivo HPG translation assays. This experiment trast to T cells (Fig. 2l,m). The T -PSR chaperone gp96 also formed
eff ex
was performed to further exclude the possibility that different spatial more abundant and distinct HMW species in T cells, which was not the
ex
distributions of T cell subpopulations caused inconsistent access to case with cytosolic HSP90α (Fig. 2l,m). The aggregation-prone proteins
OPP. Consistently, T cells showed increased protein translation rates in T cells were also enriched in the insoluble fraction (Fig. 2n). Taken
tex ex
in both MC38 and MB49 tumour models (Extended Data Fig. 6c,d). together, these data indicate that protein quality control is severely
Next, we characterized important subcellular events typically asso- compromised in T cells, which showed a tendency of protein aggre-
ex
ciated with PSR. Stress granules (SGs) are dynamic, reversible protein gation at the global level.
and RNA granules that form under cellular stress and are evident during
T cell activation39,40. The formation of SGs in T cells was increased,
ex
Misfolded proteins drive exhaustion
as evidenced by both analyses of morphology and expression of the
SG marker G3BP1 (Extended Data Fig. 7a–c). We further explored the An important question is whether protein aggregation is the cause or a
functional roles of SGs in T cells. Disruption of SGs by knocking out consequence of T cell exhaustion. We induced protein aggregation in
ex
G3bp1 resulted in an increased production of the cytokines IFNγ and T cells using two approaches and then programmed these cells under
TNF (Extended Data Fig. 7d,e). However, loss of G3bp1 significantly non-exhaustion conditions. First, we treated T cells with the l-proline
eff
compromised the survival of chronically stimulated T cells (Extended analogue l-azetidine-2-carboxylic acid (AZC) (Fig. 3a) to cause protein
ex
Data Fig. 7f). misfolding through the four-membered ring41,42. l-Proline was not
4 | Nature | www.nature.com
HPG–AF488
Nature | www.nature.com | 5
)IFM(
884FA–GPH
MC38 TIL ex vivo 1 × 104
8 × 103
T tex
6 × 103
Tint
4 × 103
Tprog
Spleen CD8+ 2 × 103
0 104105106
CRANAD-2
Spleen
CD8+TprogTintTtex
MB49 TIL ex vivo 4 × 103 2.0 × 105
Ttex 3 × 103 1.5 × 105
Tint 2 × 103 Teff 1.0 × 105
Tprog
Spleen CD8+ 1 × 103 Tex 5.0 × 104
0 104105 0 –105 0 105 106 0 0 104 105 106 CRANAD-2 Teff Tex
Native PAGE
Teff Tex
)IFM(
2-DANARC
P < 0.0001
P < 0.0001
P = 0.0337
CD44hiCD8+
MC38 TIL in vivo 80,000
No OPP 60,000
Tprog 40,000
Tint
20,000 Ttex
0 OPP–AF647 Tprog Tint Ttex
)IFM(
PPO
a b c
Bright field ER tracker NIAD-4 DAPI Merged 250,000
200,000
Teff
150,000
100,000
Tex 50,000
0
d e f P = 0.0074 P = 0.0067
P = 0.0166
g i
h
j k l m
n
)IFM(
2-DANARC
P = 1.86 × 10–7
Teff Tex
P = 1.63 × 10–5
ffeT
ffeT
ffeT
x x e e T T y e l t r a a L E
x x e e T T
y e l t r a a L E
x x e e T T
e yl t r a a L E
ffeT
ffeT
ffeT
xeT ylraE
xeT
ylraE
xeT
ylraE
xeT etaL
xeT
etaL
xeT
etaL
10 8 6 4 2
0
egnahc dlof[gol
egnahc
dlof[gol
egnahc
dlof[gol
])WML sv WM2H(
])WML
sv WM2H(
])WML
sv WM2H(
egnahc dlof[gol
egnahc
dlof[gol
egnahc
dlof[gol
])WML sv WM2H(
])WML
sv WM2H(
])WML
sv WM2H(
TCR signalling
Stress response
Senescence Pro-apoptosis
Oxidative phosphorylation
NF-κB signalling Naive
MAPK signalling
IFN response
Glycolysis
Fatty acid metabolism
Exhaustion
Cytotoxicity
Cytokine or cytokine receptor
Chemokine or chemokine receptor
Anti-apoptosis Anergy
Adhesion
Activation effector function
GZMB gp96
10 8 6 4 2
0
10 GZMC 0 BiP
8 –2 6 –4 4 –6
2 –8
0 –10
10 Perforin 0 AKT1
8 –2
6 –4 4 –6 2 –8
0 –10
0 0.50 0.75 1.00
HMW→LMW
HMW→LMW→HMW
LMW→HMW→LMW
LMW→HMW
Not detected
Proportion
0.25
log[fold change (HMW vs LMW)] 2 z score
Cluster 1.0
Teff 0.5
Early Tex 0
−0.5
Late Tex −1.0
GZMB Perforin Teff T ex Teff T ex Teff T ex Day2 4 6 8 4 6 8 Day2 4 6 8 4 6 8 Day2 4 6 8 4 6 8 37 1,048 1,048 GZMB
75
Perforin 100 gp96 100
480 480 75 HSP90α
2 1 4 4 2 6 2 1 4 4 2 6 37 Actin
gp96 HSP90α
Teff T ex Teff T ex Teff T ex Day2 4 6 8 4 6 8 Day2 4 6 8 4 6 8 Day2 4 6 8 4 6 8
1,048 1,048 40 GZMB
75 Perforin
480 10 7 0 5 gp96 480 100 242 242 75 HSP90α
146 146 37 Actin
)IFM(
2-DANARC
P = 0.0043
HMW
LMW
Retention time
(min)
Native PAGE SDS–PAGE
Soluble
• Protein • Biomolecular complexes
• Aggregates
Insoluble
• Aggregates
SDS–PAGE
)601×(
2SM
3444
1705
Spleen
CD8+TprogTintTtex
MS
20
140 kDa 10
0 20 20.5 21
Fig. 2 | Chronic TCR stimulation disrupts proteostasis during T cell between aggregation tendency of proteins and their functional pathways. Bar
exhaustion. a, ImageStream analysis of protein aggregates in T and T cells colours depict the migration pattern of proteins as indicated in h. j, Fold changes
eff ex
8 days after initial activation in vitro. Numbers are identifiers of representative of indicated protein abundances in HMW and LMW species. k, Schematic of
cells within the samples. Scale bar, 7 µm. b, Flow cytometry quantification of cell lysate fractionation based on protein solubility. l, Immunoblot analysis of
protein aggregates (n = 8 for T and n = 7 for T , two-tailed t-test). MFI, mean granzyme B (GZMB), perforin, gp96 and HSP90α in the soluble fractions of cell
eff ex
fluorescence intensity. c,d, Protein aggregates in CD8+ T cell subpopulations lysates separated by native PAGE. m, Immunoblot analysis of the indicated
from mouse MC38 tumours (c) and MB49 tumours (d) (n = 4 for spleens, n = 7 proteins in soluble fractions separated by SDS–PAGE. n, Immunoblot analysis
for TILs, one-way analysis of variance (ANOVA)). e, Flow cytometry histogram of the indicated proteins in insoluble fractions resolved by SDS–PAGE. For l–n,
and bar plot of HPG incorporation in T and T cells in vitro (n = 4, two-tailed the values on the left of the blots are kDa. For immunoblot source data, see
eff ex
t-test). f, Flow cytometry histogram and bar plot of OPP incorporation in CD8+ Supplementary Fig. 1. Data in h–j are representative of two independent
T cell subpopulations from mouse MC38 tumours (n = 7, one-way ANOVA). g, experiments. Experiments in l–n were repeated at least three times. Data are
Schematic of native PAGE and determination of the proteome by MS. T and T presented as the mean ± s.d. (b–f). The diagrams in g and k were created using
eff ex
cells were generated as described in Extended Data Fig. 4d. h, Heatmap showing BioRender (https://www.biorender.com).
the fold change of 3,889 proteins in HMW and LMW species. i, Lack of association
Article
a b
L-proline AZC
O H
N O
N OH
H OH
c d
106 106
105 105
104 104
0 0
0 104 105 106 0 104 105 106
TIM3–BV711
e f g
106 106
105 105
104 104
0 0
0 104 105 0 104 105
h i
j k
106 106
106 106 105 105
105 105 104 104
104 104
103 103
0 0 0 0
0 0 104105106 0 104105106
6 | Nature | www.nature.com
608eriF
pcreP–1DP
Vehicle AZC
IFNγ-PE-Cy7
CPA–FNT
Vehicle AZC 80
70
60
50
40
Vehicle AZC
)evil
%(
+FNT+γNFI
P = 0.0408
elciheV
CZA
CD8–Super Bright 436
7yC–CPA–93DC
50 EV
40
30
20
10
0
C
E
F
V TR(ΔF508)
+3MIT+1DP
)sllec
+8DC
+PFG
fo
%(
EV CFTR(ΔF508) P = 1.27 × 10–5 CFTR(ΔF508)
TIM3–BV711
608eriF
pcreP–1DP
40
30
20
10
0
Vehicle AZC
)evil
%(
+3MIT+1DP
DAPI NIAD-4 Merged
P = 1.48 × 10–6
VE
)805FΔ(RTFC
15
10
5
0
N
V
T ehicle AZC
DAPI CFTR Merged
sllec
+8DC
1-TO
fo .oN
)601×(
ruomut
fo
g rep
P = 0.0310
P = 0.0184
P < 0.0001
TIM3–BV711
EP–6FMALS
Vehicle AZC
50
40
30
20
10
0 Vehicle AZC Vehicle AZC
–3MIT+6FMALS
)sllec
+8DC
1-TO
fo
%(
P = 0.0002 40
30
20
10
0
+3MIT–6FMALS
)sllec
+8DC
1-TO
fo
%(
P = 0.0003
20
15
10
5
0
C
E
F
V TR(ΔF508)
+93DC
)sllec
+8DC
+PFG
fo
%(
140
135
130
125
Vehicle AZC
P = 0.0002
)IFM(
4-DAIN
P = 0.0006
107 107
4.48 9.73 5.83 30.2 8.68 71.8 7.70 60.8
106 106
105 105
104 104
103 103
53.3 32.5 29.2 34.8 0 14.2 5.34 0 25.1 6.37
–103 –103
0 104105106107 0 104105106107
39.8 31.9 30.4 22.6
AZC or B16-OVA (s.c.)
vehicle
3 days
10.6 17.7 16.5 30.6
Activated OT-1 cells Rag2–/–
pMIG (EV)
or T eff
pMIG-CFTR(ΔF508) 4–8 days Analysis
11.5 15.7 14.6 32.1
8.57 17.1
55.9 17.0 31.4 21.9
–104 104105106 –104 0 104105106
Fig. 3 | Protein misfolding promotes T cell exhaustion without chronic TCR tumour-infiltrating OT-1 cells (n = 7, two-tailed t-test). h, Schematic of
stimulation. a, Structure of l-proline and its analogue AZC. b–d, Mouse T introducing a model aggregation-prone protein, CFTR(ΔF508), into T cells by
eff eff
cells were treated with AZC for 6 days in vitro 2 days after optimal activation. retrovirus transduction. i, Confocal imaging analysis of CFTR expression in
b, Confocal imaging analysis (left) and quantification (right) of protein cells transduced with CFTR(ΔF508) or empty vector (EV). Scale bars, 5 µm.
aggregates (n = 8, two-tailed t-test. Experiments were repeated at least 3 times). j, Percentages of PD1+TIM3+ cells over total mouse CD8+ T cells transduced with
Scale bars, 5 µm. c, Percentages of PD1+TIM3+ cells out of the total live CD8+ CFTR(ΔF508) or EV (n = 4 for EV and n = 6 for CFTR(ΔF508), two-tailed t-test).
T cells (n = 4, two-tailed t-test). d, Percentages of IFNγ+TNF+ cells over the total k, Percentages of CD39+ cells out of the total transduced human CD8+ T cells
live CD8+ T cells (n = 4, two-tailed t-test). e, Schematic of adoptive transfer of 10 days after transduction (n = 3, two-tailed t-test. Experiments were repeated
AZC-pulsed or vehicle-pulsed OT-1 cells into Rag2–/– mice with B16-OVA tumours. 3 times with cells from different donors with similar results). Data are presented
NT, no transfer. f, Absolute number of tumour-infiltrating OT-1 CD8+ T cells as the mean ± s.d. (b–d,f,g,j,k). The diagrams in e and h were created using
normalized by tumour weight (n = 6 for NT and n = 7 for vehicle and AZC, BioRender (https://www.biorender.com).
one-way ANOVA). g, Percentages of SLAMF6+TIM3– and SLAMF6–TIM3+
15,000
10,000
5,000
0 AKT(Ser473)–PE Teff Tex
depleted in the culture medium to avoid metabolic disruption. After OT-1 cells were activated and transiently pulsed with AZC for 3 days
6 days of treatment of T cells with AZC, apparent protein aggregation before adoptive transfer into mice with B16-OVA tumours (Fig. 3e).
was observed (Fig. 3b). Despite culturing T cells in the non-exhaustion AZC-treated OT-1 cells showed reduced numbers in the tumours and an
conditions, AZC treatment caused them to develop into the T cell increased SLAMF6–TIM3+ T population (Fig. 3f,g). Second, we geneti-
ex tex
state, with a significantly increased PD1+TIM3+ population and impaired cally induced the expression of an aggregation-prone and functionally
cytokine production (Fig. 3c,d). As expected, T cells were vulner- inert protein into acutely activated T cells by retroviral transduction
ex
able to AZC treatment, with significantly more cell death (data not (Fig. 3h). Cystic fibrosis transmembrane conductance regulator (CFTR)
shown). We also analysed AZC-treated cells in the tumour environment. is an ion channel protein expressed primarily in epithelial cells, with
Nature | www.nature.com | 7
)IFM(
TKAp
)IFM(
TKAp
P = 0.0061
DMSO MK2206
TIM3–BV711
EP–6FMALS
40
2.85 4.51 32.7 15.5 5.32 34.6 30
20
10
15.4 77.3 25.3 26.6 38.3 21.7
0
D
MSO MK2206
–3MIT+6FMALS )sllec
+8DC
evil fo %(
+FNT+γNFI
)sllec
+8DC
evil fo %(
P = 2.39 × 10–7 DMSO MK2206 60 P = 0.0012
40
20
0
IFNγ–PE-Cy7 D
MSO MK2206
CPA–FNT
1.5 × 105
1.0 × 105
5.0 × 104
0
HPG–AF488
D
MSO MK2206 CRANAD-2
)IFM(
GPH
P = 4.33 × 10–5 40,000
30,000
20,000
10,000
0
D
MSO MK2206
)IFM(
2-DANARC
a Teff Early Tex Late Tex b c
1 × 104 P < 0.0001
TOR signalling
PI3K–PKB signal transduction 8 × 103 P = 0.0001
MAPK cascade Teff 6 × 103 P = 0.0016
SMAD protein signalling transduction Nitric oxide-mediated signal transduction A sc c o ti r v e ation 4 × 103
Cyclic nu
C
cl
a
e
l
o
c
t
iu
id
m
e
-
-
m
m
e
e
d
d
i
i
a
a
t
t
e
e
d
d
s
s
i
i
g
g
n
n
a
a
l
l
l
l
i
i
n
n
g
g
2
1
Tex 2 × 103
Small G C T a P n a o s n e ic -m al e N d F ia - t κ e B d s s i i g g n n a a l l t t r r a a n n s s d d u u c c t t i i o o n n 0 – – 2 1 0 104105106 0 Splee
P
n D1–TI M
P
3– D1+TI M
P
3
D
– 1+TI M3+
d e
f g h
P = 0.0003 6 × 105
DMSO 4 × 105 DMSO
2 × 105
MK2206 MK2206
0
D
MSO MK2206
i
)IFM(
69pg
P = 1.54 × 10–5
DMSO
MK2206
gp96–PE
EV MyrAKT
EV
MyrAKT
EP–6FMALS
j
30
20
10
0
TIM3–BV711
k l m
EV EV
MyrAKT MyrAKT
MyrAKT
n
)evil
fo
%( +3MIT–6FMALS
P = 1.06 × 10–5
300,000
200,000
100,000
0 EV MyrAKT EV MyrAKT
)IFM(
)374reS(TKAp
P = 0.0001
400,000
300,000 200,000
100,000
0 EV
)IFM( 69pg
P = 6.46 × 10–5
100,000
80,000 60,000
40,000
20,000
0 EV MyrAKT
)IFM( GPH
P = 0.0013
40,000
30,000 20,000
10,000
0 EV MyrAKT
4-DAIN )aera egami
rep
IFM(
P = 0.0014
EV MyrAKT
P = 0.0046 P = 0.0023 60 30
40 20
20 10
0 0
EVMyrAKT EV MyrAKT
EP–6FMALS
1.5
1.0
0.5
0
EVMyrAKT TIM3–BV711
evil fo %( sllec
+8DC
)sllec +54DC )401×( +8DC
fo .oN
o p
900 8 P = 0.0029 P = 0.0754
6 600 4
300 2
0 0
0 4 8 12 16 EVMyrAKT
Time after tumour implantation (days)
)3mm( emulov
ruomuT
NT (n = 7)
EV (n = 8) MyrAKT (n = 7) 0610.0 = P 6400.0 = P
107 107
13.8 51.7 106 106 106 106
105 105 105 105
104 104
104 104 103 103 0 0 0 0 –103 –103
–104 –104 21.2 13.3
–104 0 104 105 106 –104 0 104 105 106 –104 0 104 105 107 –104 0 104 105 107
0 105 106 0 104 105 106 0 105 106 107
pMIG
EV
106 106
105 105
104 104
pMIG-myrAKT
MyrAKT 0 0
–104 –104
0 104 105 106 –104 0 104105 –104 0 104105
pAKT(Ser473)–PE
0 104 105 106 0 105 106
HPG–AF594 gp96–PE
106 106
105 105 104 104 ACT
0 0
–104 0 104 105106 –104 0 104 105106
–3MIT+6FMALS )sllec +8DC
fo %(
+3MIT–6FMALS )sllec +8DC
fo %(
79.0 12.5 24.5 14.9
6.83 1.64 33.2 27.4
55.9 9.35 30.9 10.1
29.3 5.48 31.9 21.7
Fig. 4 | See next page for caption.
Article
Fig. 4 | Sustained AKT signalling induces T -PSR and underlies T cell transduction, and the flow cytometry quantification of pAKT(Ser473) in
ex
exhaustion. a, Expression levels of proteins in major signalling pathways in mouse T cells transduced with myrAKT or EV (n = 3 for EV, n = 4 for myrAKT).
T and T cells in vitro as described in Extended Data Fig. 4d. b, Levels of j–m, Quantification of SLAMF6–TIM3+ cells (j), HPG incorporation (k), protein
eff ex
phosphorylated AKT (pAKT(Ser473)) in mouse T and T cells in vitro (n = 3). aggregation by live-cell imaging (l) and gp96 expression (m) in T cells transduced
eff ex
c, pAKT staining in splenic CD8+ T cells and TIL subsets from MC38 tumours (n = 3 with myrAKT or EV (n = 4 (j,k,m) or n = 9 (l) per group). n, Tumour growth curves
for spleen, n = 6 for TILs, one-way ANOVA). d, Percentages of SLAMF6+TIM3– (two-way ANOVA). OT-1 cells transduced with myrAKT or EV were transferred
cells in T cells treated with chronic TCR stimulation together with MK2206 into Rag2–/– mice with B16-OVA tumours. o, Percentages and absolute number
or dimethyl sulfoxide (DMSO) for 6 days (n = 4). e, Percentages of IFNγ+TNF+ of OT-1 T cells transduced with myrAKT or EV from tumours 5 days after adoptive
cells after re-stimulation in T cells treated as in d and rested for 2 days (n = 4). cell transfer (ACT) (n = 7). p, Percentages of SLAMF6+TIM3– and SLAMF6–TIM3+
f, Quantification of HPG incorporation in T cells treated as in d (n = 4). OT-1 cells from tumours (n = 7). Two-tailed t-test for comparisons between two
g, Quantification of protein aggregation in T cells treated as in d (n = 4). h, gp96 groups. Data are the mean ± s.d. (b–m,o,p) or the mean ± s.e.m. (n). The diagram
expression in T cells treated with MK2206 for 2 days (n = 3). i, Schematic in i was created using BioRender (https://www.biorender.com).
ex
of packaging MSCV-GFP (pMIG) retrovirus expressing myrAKT for T cell
low levels of expression in T lymphocytes43. Deletion of phenylalanine in controlling the growth of B16-OVA tumours in mice compared with
at the 508th position (CFTR(ΔF508)) in human CFTR leads to protein wild-type (WT) OT-1 cells (Fig. 4n). MyrAKT-expressing T cells in the
misfolding and ER retention44,45. Transduction of the folding-deficient tumour microenvironment showed less tumour infiltration and more
mutant CFTR(ΔF508) resulted in the intracellular accumulation of exhausted phenotypes compared with control T cells (Fig. 4o,p). We con-
CFTR aggregates in mouse CD8+ T cells (Fig. 3i). Moreover, overex- clude that sustained AKT activation drives T -PSR and T cell exhaustion.
ex
pression of CFTR(ΔF508) induced bona fide T cell exhaustion with-
out repetitive TCR stimulation (Fig. 3j). CFTR(ΔF508) also increased
CD39+ populations in acutely activated human CD8+ T cells (Fig. 3k). T ex -PSR chaperones underlie exhaustion
Together, these results suggest that protein aggregation has a causal We next asked whether the T cell exhaustion program can be altered
role in T cell exhaustion. through the manipulation of T -PSR chaperones. We initially
ex
selected ten genes that encode the following proteins that showed
increased expression in T cells and represent diverse molecular
ex
Sustained AKT activity causes exhaustion
functions: ADAM8; annexin A2; cathepsin D (which is associated with
We next aimed to elucidate the upstream signalling hub that is respon- cell death); ACADL (a fatty acid metabolic enzyme); the cytotoxic
sible for mediating T -PSR and promoting T cell exhaustion. We exam- granzymes granzyme C and granzyme A; the temperature-sensitive
ex
ined the expression level of components of key signalling pathways channel protein TRPV2; and the three chaperone proteins BiP, gp96
defined in the Gene Ontology database in our T cell proteome dataset. and ERO1A (Extended Data Fig. 10a). The roles of these proteins on
The AKT pathway was specifically upregulated in the late T cell popula- T cell exhaustion have not been previously defined. We knocked out
ex
tion (Fig. 4a). Flow cytometry analysis further showed that AKT phos- these genes individually by CRISPR–Cas9 after T cell activation and
phorylation was enhanced in T cells (Fig. 4b). Chronic AKT signalling then performed repetitive TCR stimulation. Gene deletion was con-
ex
was also observed in T cells isolated from MC38 tumours (Fig. 4c). firmed by PCR with reverse transcription (RT–PCR) or flow cytometry
ex
AKT often operates in the same signalling axis as PI3K and mTOR (Extended Data Fig. 10b,c). Deleting each of the three chaperone genes
and has an important role in mediating T cell proliferation, survival Hspa5, Hsp90b1 and Ero1a with single guide RNAs (sgRNAs sgHspa5,
and function46,47. Low-dose treatment with the AKT inhibitor MK2206 sgHsp90b1 and sgEro1a, respectively) significantly enhanced cytokine
(0.2 µM and 1 µM) significantly increased the SLAMF6+TIM3– popula- production, whereas individual knockout of the other seven genes had
tion and cytokine production without impairing cell viability or prolif- minimal effects (Fig. 5a and Extended Data Fig. 10d). Cells deficient in
eration (Fig. 4d,e and Extended Data Fig. 9a–d,f). However, treatment BiP, ERO1A or gp96 also showed increased SLAMF6 expression, along
with the mTOR inhibitor rapamycin or the PI3K inhibitor LY294002 at with reduced levels of TIM3 and CD39 (Extended Data Fig. 10e–g).
any dose did not block T cell exhaustion, as indicated by the compara- Although chaperone proteins are responsible for facilitating protein
ble proportion of SLAMF6+TIM3– populations to the untreated group folding, knocking out Hsp90b1 resulted in the most significant reduc-
(Extended Data Fig. 9c). PI3K and mTOR inhibition also did not rescue tion in protein aggregation, which indicated its potentially pivotal
cytokine production in T cells (Extended Data Fig. 9d,f). All inhibitors role in mediating T -PSR-associated protein aggregate formation
ex ex
directed cells to differentiate into the CD44+CD62L+ population, which (Fig. 5b).
validated that the dose levels used had pharmacological activities in To validate whether Hsp90b1 deletion has the same effect in
chronically stimulated T cells (Extended Data Fig. 9e). We therefore counteracting T cell exhaustion in vivo, we generated CD8+-specific
focused on AKT in subsequent studies. Moderate attenuation of AKT Hsp90b1 knockout (KO: E8i-cre-Hsp90b1flox/flox) and knockdown (Het:
signalling was sufficient to reduce the protein synthesis rate in T cells E8i-cre-Hsp90b1flox/WT, with 50% reduction in gp96 levels) mouse
ex
and to reduce protein aggregation and T -PSR chaperone gp96 expres- models, which were subjected to chronic LCMV clone 13 infection
ex
sion (Fig. 4f–h). These results strongly suggest that AKT has a key role (Fig. 5c,d). Thirty days after infection, gp96 expression was upreg-
in driving T -PSR and T cell exhaustion. ulated in antigen-experienced CD8+ T cells from WT mice, with T
ex tex
To further determine whether AKT signalling is the upstream driver cells demonstrating the highest level of expression (Extended Data
of T -PSR and T cell exhaustion, we expressed myristoylated AKT Fig. 10h). Hsp90b1 deletion resulted in a significant expansion of total
ex
(myrAKT), a constitutively active form of AKT, in T cells48,49 (Fig. 4i). and antigen-specific CD8+ T cells in spleens (Fig. 5e). There was clear
MyrAKT expression converted T cells into T cells with a significant evidence of reprogramming of T cells after Hsp90b1 deletion (Fig. 5f,g),
eff ex
induction of SLAMF6–TIM3+ terminal exhausted phenotype under with enrichment of TCF1+CX3CR1– progenitor cells and CX3CR1+ inter-
non-exhaustion conditions (Fig. 4j). This constitutively active AKT mediate populations, along with reduced expression of TIM3 and CD39
also upregulated protein translation, increased protein aggregation (Fig. 5h,i).
and induced the expression of the PSR chaperone gp96, which are all Similarly, we assessed whether deleting chaperone Hspa5 or Ero1a in
hallmarks of T -PSR (Fig. 4k–m). To assess its functional impact, we P14 CD8+ T cells improves their antitumour effect in a gp33-expressing
ex
transduced myrAKT into activated OT-1 cells and transferred them into MB49 tumour model (Fig. 5j). Mice receiving Hspa5 or Ero1a KO P14
mice with B16-OVA tumours. MyrAKT OT-1 T cells were no longer effective cells showed significantly better tumour control compared with those
8 | Nature | www.nature.com
a b
Control sgHspa5
107 106
105
104
0
0 104105106 0 104105106 0 104105106 0 104105106 IFNγ–PE–Cy7
c d e
0 104 105 106
f g
h i
104
103
0
–104 0 104 105106 –104 0 104 105106 –104 0 104 105106
j k l
m n o 106 65.7 20.1 106 48.5 38.0
105 105 104 104
0 0
0 104105106 0 104105106
–103 0 103 104
that received WT P14 cells (Fig. 5k,l). We also analysed the impact of BiP by increased TCF1 expression, compared with WT cells (Fig. 5m,n).
deficiency on P14 cells in the tumour microenvironment 5 days after These data collectively suggest that targeting T -PSR chaperones offer
ex
adoptive transfer. BiP-null P14 T cells were more enriched in the cytol- a potential approach for improving adoptive T cell transfer therapy
ytic CX3CR1+ population and showed improved stemness, as indicated for cancer.
Nature | www.nature.com | 9
CPA–FNT
sgHsp90b1 sgEro1a
15,000
10,000
5,000
0
WT Het KO
)IFM(
69pg
100 80
60
40
20
0 Contro
sg
l Hspa
s
5 gEro
sg
1
H
a sp90b1 0 104 105 106
P < 0.0001
P = 0.0047
P = 0.0233
+FNT+γNFI
)sllec
+8DC
evil
fo %(
P < 0.0001 P < 0.0001
P = 0.0009
Control sgHspa5
CX3CR1–APC Fire750
EP–6FMALS
500
400 300
200 100
0 TCF1–PE–Cy7 Control sgHspa5
)IFM(
1FCT
0.29 32.8 107 0.17 75.8 107 0.64 64.3 107 7.12 53.7 60,000 106 106 106
105 105 105 40,000
104 104 104
20,000
0 0 0 3.61 63.3 4.52 19.5 4.00 31.1 13.4 25.8
0 Contro
s
l gHspa
s
5 gEr
s
o
g
1
H
a sp90b1
gp96–PE
MB49–gp33 (s.c.) Irradiation
Day 0 Day 4 Day 6 Day 7 Day 8
Activation CRISPR
P14
P = 0.0001
)IFM(
2-DANARC
P < 0.0001
P = 0.0085
Control P = 0.0072
sgHspa5
sgEro1a
sgHsp90b1
CRANAD-2
WT
Het
KO
Tet+CD8+ CD44 CD62L PD1 TCF1 CX3CR1 KI67
WT
Het
KO
TIM3 GZMB KLRG1 CD39 T-bet EOMES
P = 2.049 × 10–5
NR R NR R
CAR T Anti-PD1
erocs
RSP-
T xe
30
20
10
0
WT Het KO
P = 3.248 × 10–71 0.20 0.15
0.15 0.10
0.10
0.05 0.05
0 0
–1RC3XC+1FCT
)sllec
+8DC+teT
fo
%(
+1RC3XC
)sllec
+8DC+teT
fo
%(
–1RC3XC–1FCT
)sllec
+8DC+teT
fo
%(
P < 0.0001
60 P < 0.0001 8
6 40
4
20 2
0 0
WT Het KO WT Het KO
P = 0.0042 P < 0.0001 P = 0.0028
P = 0.0009 P = 0.0024 P < 0.0001
80 90
60 P = 0.0024
60
40
30
20
0 0
WT Het KO WT Het KO
+8DC
)sllec
+54DC
fo
%(
+8DC+teT
)sllec
+54DC
fo
%(
P < 0.0001
P < 0.0001
WT Het KO
CX3CR1–APC Fire750
7yC–EP–1FCT
UMAP1
2PAMU
120 80
40
0
6 12 18 24
Time after tumour implantation
(days)
33pg–94BM )2mm(
aera ruomut
P14 No transfer Control
Hspa5 KO Ero1a KO
P = 6.42
× 10–5
P = 6.76
× 10–6
P = 0.0163P
= 0.0028
P = 0.0004 100
50
0
0 20 40 60
Time after tumour implantation (days)
)%(
lavivruS
P14 No transfer Control Hspa5 KO
Ero1a KO
P = 0.0097 P = 0.0047
LCMV
Cl13
WT: Hsp90b1flox/flox
Het: E8i-cre-Hsp90b1flox/WT
KO: E8i-cre-Hsp90b1flox/flox
60 Control
40
20 sgHspa5
0 Control sgHspa5
)41P
+2αV
fo(
+1RC3XC
12.6 2.36 22.9 12.2 22.4 14.2
104 104
103 103
0 0
62.8 22.3 50.8 14.0 19.4 44.1
P = 8.02 ×10–5
Fig. 5 | See next page for caption.
Article
Fig. 5 | Targeting T -PSR chaperones prevents T cell exhaustion and KO, Ero1a KO or control cells. k, Tumour growth curves (n = 4 for NT, n = 5 for the
ex
enhances cancer immunotherapy. a, Frequencies of IFNγ+TNF+ cells (n = 3, other groups, two-way ANOVA). l, Kaplan–Meier survival curves (n = 4 for NT,
one-way ANOVA) in cells with indicated genes knocked out. b, Quantification of n = 5 for the other groups, Mantel–Cox test). Results represent three independent
protein aggregation by flow cytometry (n = 4, one-way ANOVA). c, Experimental experiments. m,n, Representative flow cytometry plots (left) and quantification
scheme of using CD8+ T cell-specific deletion of Hsp90b1 in mice infected with (right) of CX3CR1+ percentages (m) and TCF1 expression (n) in tumour-infiltrating
LCMV clone 13. d, gp96 expression in total splenic CD8+ T cells (n = 8 for WT, P14 T cells 6 days after ACT (n = 8, two-tailed t-test). o, T -PSR scores in scRNA-seq
ex
n = 3 for Het, n = 5 for KO, one-way ANOVA). e, Frequencies of total CD8+ (left) CD8+ T cells from non-responders (NR) and responders (R) to anti-CD19 CAR
and gp33-specific and gp276-specific (Tet+) CD8+ T cells (right) in spleens T cell therapy for diffuse large B cell lymphoma61 (left, NR: n = 63,482 cells from
30 days after infection (n = 8 for WT, n = 3 for Het, n = 5 for KO, one-way ANOVA). 57 patients; R: n = 59,351 cells from 52 patients) and anti-PD1 therapy for non-
f, Uniform manifold approximation and projection (UMAP) of Tet+ CD8+ T cells small cell lung cancer62 and renal cell carcinoma (RCC)63 (right, NR: n = 5,672
profiled by 25-marker multispectral flow cytometry. g, Expression of selected cells from 6 patients, R: n = 37,884 cells from 18 patients). Two-sided Wilcoxon
markers mapped on UMAP. h,i, Representative flow cytometry (h) and rank-sum tests. Data are the mean ± s.d. (a,b,d,e,i,m,n) or mean ± s.e.m. (k,o). The
quantification (i) of TCF1+CX3CR1–, CX3CR1+ and TCF1–CX3CR1– cells (n = 8 for diagrams in c and j were created using BioRender (https://www.biorender.com).
WT, n = 3 for Het, n = 5 for KO, one-way ANOVA). j, Schematic of ACT using Hspa5
proteostasis can be a viable target for immunotherapeutic purposes.
Clinical relevance of T -PSR in cancer
ex In this regard, it is worth noting that the HSP90 inhibitor ganetespib,
Finally, we investigated the human relevance of T -PSR in cancer. We which also inhibits the T -PSR chaperone gp96, has been shown to
ex ex
performed pan-cancer CD8+ T cell analyses with publicly available promote ICB efficacy51.
single-cell transcriptomic datasets that encompass 17 cancer types Our work identified AKT signalling as a central regulator of T -PSR
ex
(Extended Data Fig. 11a). These T cells were isolated directly from and T cell exhaustion. It is well established that PI3K–AKT–mTOR signal-
samples taken from patients with cancer and did not have any other ling is essential for T cell activation and differentiation by upregulat-
in vitro manipulations. To determine whether T -PSR is also a feature ing metabolic programs and supporting their bioenergetic needs46,47.
ex
of tumour-associated T cells in humans, we generated a T -PSR sig- However, the implications of AKT in T cell exhaustion are controversial
ex ex
nature based on our in vivo and in vitro proteomic data (Extended Data and under-explored52,53. We demonstrated here that T cells maintain
ex
Fig. 11b). The T -PSR signature consisted of genes associated with pro- chronic AKT signalling. Enforced expression of constitutively active
ex
teostasis regulation that are concurrently upregulated in T cells at the AKT drives T -PSR and a bona fide T cell exhaustion program. We
ex ex
mRNA and protein levels (Extended Data Fig. 11c). The expression level therefore posit that AKT signalling is required for T cell survival, but
of mRNAs encoding T -PSR signature proteins was the highest in T its persistent activation disrupts the proteostatic equilibrium, which
ex tex
cells compared with all other T cell subsets from the tumour samples triggers T -PSR and promotes exhaustion. Meanwhile, although often
ex
(Extended Data Fig. 11d). We also performed pseudotime trajectory thought to operate on the same axis, mTOR inhibition by rapamycin
analysis based on RNA velocity on pan-cancer CD8+ T cells (Extended did not show a substantial effect on preventing T cell exhaustion in
Data Fig. 11e). We observed two opposing differentiation trajectories: our study. It may be because mTOR signalling is already suppressed
effector and exhaustion. The T -PSR gene signature appeared early in in T cells47,52,54. The plasticity of these signalling pathways suggests
ex ex
the exhaustion trajectory, which increased proportionally as T cells that the crosstalk of these signalling hubs in T cell exhaustion warrants
become progressively exhausted (Extended Data Fig. 11f). By contrast, further investigation.
T -PSR was significantly reduced during the effector trajectory. We Another intriguing aspect of T -PSR activation in T cells is the selec-
ex ex ex
analysed the T -PSR score in CD8+ T cells from patients with liver cancer. tive upregulation of T -PSR chaperones. The role of T -PSR chaperones
ex ex ex
Patients with a lower T -PSR signature in CD8+ T cells showed better presents a conundrum here in T cells. Previous studies have reported
ex ex
overall survival (Extended Data Fig. 11g). Moreover, a higher T -PSR that chaperones extend their impact beyond protein folding55–58.
ex
signature in patients with cancer also correlated with poor responses Moreover, AKT is a known client of HSP90 (ref. 59). Furthermore, ER
to immunotherapies, including both CAR T cells and ICBs (anti-PD1, chaperones such as BiP can translocate into the nucleus and function
and anti-PD1 with anti-CTLA4) (Fig. 5o and Extended Data Fig. 11h). as TFs60. It is possible that the actions of T -PSR chaperones in T cells
ex ex
go beyond the fundamental role of protein folding and instead mediate
signal transduction. An alternative and more simplistic explanation is
Discussion
that the chaperone machinery in T cells is qualitatively suboptimal
ex
The question of how protein quality control might differ between T cell owing to the upregulation of some but not all chaperones. In T cells,
ex
activation and the exhaustion program has not been clearly answered. the T -PSR chaperone stoichiometry is in disarray because of chap-
ex
A key finding of our study was the activation of a distinct PSR in T erone imbalance as well as substrate accumulation, which all result in
ex
cells, which we term T -PSR. This PSR is characterized by a high rate of pathological proteotoxic stress.
ex
protein translation, accumulation of SGs and global protein aggrega- Under chronic stimulation, T cells must navigate a delicate balance
tion despite increased protein catabolism (Extended Data Fig. 12). The between effector function and self-survival. We demonstrated that
high translational rate in T cells was not associated with the produc- modulation of T -PSR can enhance effector cytokine production at
ex ex
tion of functional molecules. Our study provides an explanation to the expense of survival. Meanwhile, maintaining a high rate of protein
this paradox in that many proteins, such as granzymes and perforin, synthesis might be advantageous for T cells. This strategy ensures the
ex
in T cells aggregate instead of being properly folded, which may be production of essential proteins for their survival, albeit in a manner
ex
a consequence of an overwhelmed protein quality control system. that is not cost-effective. Our study molecularly characterized the
We also demonstrated that the introduction of misfolded proteins aggregation proteome. We demonstrated that protein aggregation
to T cells under optimal conditions for T cell differentiation caused in T cells is a global event without selectivity, a result that highlights
eff ex
exhaustion. It has previously been reported50 that tumour cells can that it is the protein quality control machinery itself that is defective
evade T cell immunity by competing for methionine to alter T cell his- in T cells. Our findings indicate that increased protein expression of
ex
tone modifications. This result suggests that amino acid metabolism T cell effector molecules per se without correcting the pathological
might have important roles in regulating T cell function by concurrently T -PSR in T cells will not lead to functional improvement or reversal
ex ex
affecting translation and the epigenetic landscape50. Nonetheless, the of the exhaustion phenotype. Moreover, we showed that the introduc-
causal relationship between PSR and T suggests that dysregulated tion of misfolded proteins alone, even in the absence of persistent
ex
10 | Nature | www.nature.com
TCR stimulation, effectively induced a T cell exhaustion phenotype. 33. Nesterov, E. E. et al. In vivo optical imaging of amyloid aggregates in brain: design of
Thus, the fate of T cells is intricately linked to protein quality control. fluorescent markers. Angew. Chem. Int. Ed. Engl. 44, 5452–5456 (2005).
ex 34. Gebauer, F. & Hentze, M. W. Molecular mechanisms of translational control. Nat. Rev. Mol.
How T cells sense aggregates and subsequently reprogram T eff cells to Cell Biol. 5, 827–835 (2004).
T cells remains an open question that warrants further exploration. 35. Sendoel, A. et al. Translation from unconventional 5′ start sites drives tumour initiation.
ex
Nature 541, 494–499 (2017).
36. Suzuki, C. et al. PDCD4 inhibits translation initiation by binding to eIF4A using both its
MA3 domains. Proc. Natl Acad. Sci. USA 105, 3274–3279 (2008).
Online content 37. Marchingo, J. M. & Cantrell, D. A. Protein synthesis, degradation, and energy metabolism
in T cell immunity. Cell. Mol. Immunol. 19, 303–315 (2022).
Any methods, additional references, Nature Portfolio reporting summa-
38. Signer, R. A., Magee, J. A., Salic, A. & Morrison, S. J. Haematopoietic stem cells require a
ries, source data, extended data, supplementary information, acknowl- highly regulated protein synthesis rate. Nature 509, 49–54 (2014).
edgements, peer review information; details of author contributions 39. Franchini, D. M. et al. Microtubule-driven stress granule dynamics regulate inhibitory
immune checkpoint expression in T cells. Cell Rep. 26, 94–107 (2019).
and competing interests; and statements of data and code availability
40. Curdy, N. et al. The proteome and transcriptome of stress granules and P bodies during
are available at https://doi.org/10.1038/s41586-025-09539-1. human T lymphocyte activation. Cell Rep. 42, 112211 (2023).
41. Trotter, E. W. et al. Misfolded proteins are competent to mediate a subset of the responses
to heat shock in Saccharomyces cerevisiae. J. Biol. Chem. 277, 44817–44825 (2002).
1. Zajac, A. J. et al. Viral immune evasion due to persistence of activated T cells without 42. Qian, S. B. et al. mTORC1 links protein quality and quantity control by sensing chaperone
effector function. J. Exp. Med. 188, 2205–2213 (1998). availability. J. Biol. Chem. 285, 27385–27395 (2010).
2. Chow, A., Perica, K., Klebanoff, C. A. & Wolchok, J. D. Clinical implications of T cell 43. Yoshimura, K. et al. Expression of the cystic fibrosis transmembrane conductance
exhaustion for cancer immunotherapy. Nat. Rev. Clin. Oncol. 19, 775–790 (2022). regulator gene in cells of non-epithelial origin. Nucleic Acids Res. 19, 5417–5423 (1991).
3. Wherry, E. J. T cell exhaustion. Nat. Immunol. 12, 492–499 (2011). 44. Rommens, J. M. et al. Identification of the cystic fibrosis gene: chromosome walking and
4. Blank, C. U. et al. Defining ‘T cell exhaustion’. Nat. Rev. Immunol. 19, 665–674 (2019). jumping. Science 245, 1059–1065 (1989).
5. Hetz, C., Zhang, K. & Kaufman, R. J. Mechanisms, regulation and functions of the unfolded 45. Riordan, J. R. CFTR function and prospects for therapy. Annu. Rev. Biochem. 77, 701–726
protein response. Nat. Rev. Mol. Cell Biol. 21, 421–438 (2020). (2008).
6. Costa-Mattioli, M. & Walter, P. The integrated stress response: from mechanism to disease. 46. Chi, H. Regulation and function of mTOR signalling in T cell fate decisions. Nat. Rev.
Science https://doi.org/10.1126/science.aat5314 (2020). Immunol. 12, 325–338 (2012).
7. McLane, L. M., Abdel-Hakeem, M. S. & Wherry, E. J. CD8 T cell exhaustion during chronic 47. Huang, H., Long, L., Zhou, P., Chapman, N. M. & Chi, H. mTOR signaling at the crossroads
viral infection and cancer. Annu. Rev. Immunol. 37, 457–495 (2019). of environmental signals and T-cell fate decisions. Immunol. Rev. 295, 15–38 (2020).
8. Hudson, W. H. et al. Proliferating transitory T cells with an effector-like transcriptional 48. Pellman, D., Garber, E. A., Cross, F. R. & Hanafusa, H. An N-terminal peptide from p60src
signature emerge from PD-1+ stem-like CD8+ T cells during chronic infection. Immunity 51, can direct myristylation and plasma membrane localization when fused to heterologous
1043–1058 (2019). proteins. Nature 314, 374–377 (1985).
9. Siddiqui, I. et al. Intratumoral Tcf1+PD-1+CD8+ T cells with stem-like properties promote 49. Kharas, M. G. et al. Constitutively active AKT depletes hematopoietic stem cells and
tumor control in response to vaccination and checkpoint blockade immunotherapy. induces leukemia in mice. Blood 115, 1406–1415 (2010).
Immunity 50, 195–211 (2019). 50. Bian, Y. et al. Cancer SLC43A2 alters T cell methionine metabolism and histone methylation.
10. Im, S. J. et al. Defining CD8+ T cells that provide the proliferative burst after PD-1 therapy. Nature 585, 277–282 (2020).
Nature 537, 417–421 (2016). 51. Mbofung, R. M. et al. HSP90 inhibition enhances cancer immunotherapy by upregulating
11. Miller, B. C. et al. Subsets of exhausted CD8+ T cells differentially mediate tumor control interferon response genes. Nat. Commun. 8, 451 (2017).
and respond to checkpoint blockade. Nat. Immunol. 20, 326–336 (2019). 52. Staron, M. M. et al. The transcription factor FoxO1 sustains expression of the inhibitory
12. Kurtulus, S. et al. Checkpoint blockade immunotherapy induces dynamic changes in receptor PD-1 and survival of antiviral CD8+ T cells during chronic infection. Immunity 41,
PD-1–CD8+ tumor-infiltrating T cells. Immunity 50, 181–194 (2019). 802–814 (2014).
13. Schietinger, A. et al. Tumor-specific T cell dysfunction is a dynamic antigen-driven 53. Utzschneider, D. T. et al. Active maintenance of T cell memory in acute and chronic viral
differentiation program initiated early during tumorigenesis. Immunity 45, 389–401 infection depends on continuous expression of FOXO1. Cell Rep. 22, 3454–3467 (2018).
(2016). 54. Ando, S. et al. mTOR regulates T cell exhaustion and PD-1-targeted immunotherapy
14. Lynn, R. C. et al. c-Jun overexpression in CAR T cells induces exhaustion resistance. response during chronic viral infection. J. Clin. Invest. https://doi.org/10.1172/JCI160025
Nature 576, 293–300 (2019). (2023).
15. Chen, J. et al. NR4A transcription factors limit CAR T cell function in solid tumours. Nature 55. Liu, B. & Li, Z. Endoplasmic reticulum HSP90b1 (gp96, grp94) optimizes B-cell function
567, 530–534 (2019). via chaperoning integrin and TLR but not immunoglobulin. Blood 112, 1223–1230 (2008).
16. Seo, H. et al. TOX and TOX2 transcription factors cooperate with NR4A transcription 56. Xu, Y. et al. Heat shock protein gp96 drives natural killer cell maturation and anti-tumor
factors to impose CD8+ T cell exhaustion. Proc. Natl Acad. Sci. USA 116, 12410–12415 immunity by counteracting Trim28 to stabilize Eomes. Nat. Commun. 15, 1106 (2024).
(2019). 57. Zhang, Y. et al. GP96 is a GARP chaperone and controls regulatory T cell functions. J. Clin.
17. Long, A. H. et al. 4-1BB costimulation ameliorates T cell exhaustion induced by tonic Invest. 125, 859–869 (2015).
signaling of chimeric antigen receptors. Nat. Med. 21, 581–590 (2015). 58. Amankwah, Y. S. et al. Structural transitions modulate the chaperone activities of Grp94.
18. Vogel, C. & Marcotte, E. M. Insights into the regulation of protein abundance from Proc. Natl Acad. Sci. USA 121, e2309326121 (2024).
proteomic and transcriptomic analyses. Nat. Rev. Genet. 13, 227–232 (2012). 59. Basso, A. D. et al. Akt forms an intracellular complex with heat shock protein 90 (Hsp90)
19. Schwanhausser, B. et al. Global quantification of mammalian gene expression control. and Cdc37 and is destabilized by inhibitors of Hsp90 function. J. Biol. Chem. 277,
Nature 473, 337–342 (2011). 39858–39866 (2002).
20. Maier, T., Guell, M. & Serrano, L. Correlation of mRNA and protein in complex biological 60. Liu, Z. et al. ER chaperone GRP78/BiP translocates to the nucleus under stress and acts as
samples. FEBS Lett. 583, 3966–3973 (2009). a transcriptional regulator. Proc. Natl Acad. Sci. USA 120, e2303448120 (2023).
21. Jiang, L. et al. A quantitative proteome map of the human body. Cell 183, 269–283 (2020). 61. Haradhvala, N. J. et al. Distinct cellular dynamics associated with response to CAR-T
22. Taniguchi, Y. et al. Quantifying E. coli proteome and transcriptome with single-molecule therapy for refractory B cell lymphoma. Nat. Med. 28, 1848–1859 (2022).
sensitivity in single cells. Science 329, 533–538 (2010). 62. Liu, B. et al. Temporal single-cell tracing reveals clonal revival and expansion of precursor
23. Hukelmann, J. L. et al. The cytotoxic T cell proteome and its shaping by the kinase mTOR. exhausted T cells during anti-PD-1 therapy in lung cancer. Nat. Cancer 3, 108–121 (2022).
Nat. Immunol. 17, 104–112 (2016). 63. Bi, K. et al. Tumor and immune reprogramming during immunotherapy in advanced renal
24. Cuadrado, E. et al. Proteomic analyses of human regulatory T cells reveal adaptations in cell carcinoma. Cancer Cell 39, 649–661 (2021).
signaling pathways that protect cellular identity. Immunity 48, 1046–1059 (2018).
25. Nicolet, B. P. & Wolkers, M. C. The relationship of mRNA with protein expression in CD8+
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
T cells associates with gene class and gene characteristics. PLoS ONE 17, e0276294
published maps and institutional affiliations.
(2022).
26. Chang, C. H. et al. Posttranscriptional control of T cell effector function by aerobic
Open Access This article is licensed under a Creative Commons Attribution-
glycolysis. Cell 153, 1239–1251 (2013).
NonCommercial-NoDerivatives 4.0 International License, which permits any
27. Vardhana, S. A. et al. Impaired mitochondrial oxidative phosphorylation limits the self-
non-commercial use, sharing, distribution and reproduction in any medium or
renewal of T cells exposed to persistent antigen. Nat. Immunol. 21, 1022–1033 (2020).
format, as long as you give appropriate credit to the original author(s) and the source, provide
28. Belk, J. A. et al. Genome-wide CRISPR screens of T cell exhaustion identify chromatin
a link to the Creative Commons licence, and indicate if you modified the licensed material.
remodeling factors that limit T cell persistence. Cancer Cell 40, 768–786 (2022).
You do not have permission under this licence to share adapted material derived from this
29. Nusinow, D. P. et al. Quantitative proteomics of the Cancer Cell Line Encyclopedia. Cell
article or parts of it. The images or other third party material in this article are included in the
180, 387–402 (2020).
article’s Creative Commons licence, unless indicated otherwise in a credit line to the material.
30. Chu, Y. et al. Pan-cancer T cell atlas links a cellular stress response state to immunotherapy
If material is not included in the article’s Creative Commons licence and your intended use is
resistance. Nat. Med. 29, 1550–1562 (2023).
31. Zander, R. et al. CD4+ T cell help is required for the formation of a cytolytic CD8+ T cell not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
permission directly from the copyright holder. To view a copy of this licence, visit http://
subset that protects against chronic infection and cancer. Immunity 51, 1028–1042 (2019).
creativecommons.org/licenses/by-nc-nd/4.0/.
32. Beusch, C. M. et al. Longitudinal proteomic profiling of T cell differentiation in vivo
unveils dynamic proteome remodeling. Preprint at bioRxiv https://doi.org/10.1101/2024.
05.14.593504 (2024). © The Author(s) 2025
Nature | www.nature.com | 11
Article
Methods RPMI-1640 for 30 min at 37 °C with gentle agitation. After digestion, 2%
BSA in PBS was added to cell suspensions to neutralize collagenase. Cell
Cell lines suspensions were washed with PBS and filtered through a 70 µm nylon
The MC38 cell line was purchased from Kerafast (ENH204-FP). The filter. Single-cell suspensions were centrifuged and resuspended in PBS
MB49 cell line was purchased from Sigma-Aldrich (SCC148). The for downstream assays. For cell sorting, immune cells were enriched
HEK293T cell line was purchased from the American Type Culture using a mouse TIL CD45 positive selection kit (Stemcell, 100-0350).
Collection (CRL-3216). The MB49-gp33 cell line was shared by W. Cui
(Northwestern University). The B16-OVA cell line was generated as Flow cytometry
previously described64 and shared by L. Deng (Memorial Sloan Ket- Cells were washed with PBS twice. Dead cells were stained using Live/
tering Cancer Center). HEK293T, MC38 and MB49 cells were cultured Dead fixable blue (Invitrogen, L23105) or Zombie UV (BioLegend,
in Dulbecco’s modified Eagle medium (DMEM; Gibco, 11965-092) with 423108) at 4 °C for 15 min. Cells were washed with FACS buffer twice and
10% FBS (Gibco, 10082-147) and 1% penicillin–streptomycin (Gibco, a surface molecule staining antibody cocktail was applied for 30 min
15140-122) at 37 °C and 5% CO. B16-OVA cells were cultured in RPMI- at 4 °C. After incubation, cells were washed twice with FACS buffer and
2
1640 (Gibco, 11875-093) with 10% FBS and 1% penicillin–streptomycin. then fixed and permeabilized using a FOXP3 fixation and permeabiliza-
Cell lines were regularly tested for mycoplasma contamination. tion kit (eBioscience, 00-5523-00) overnight. After overnight fixation,
cells were washed twice in permeabilization buffer and an intracellular
Mice staining antibody cocktail was added to the cells. After 2 h of incuba-
WT C57BL/6J mice (strain 000664) were purchased from The Jack- tion at room temperature, cells were washed twice with FACS buffer
son Laboratory. CD8-specific gp96-deficient mice were generated by and analysed using Cytek Aurora. Acquired data were analysed with
crossing E8i-Cre mice (The Jackson Laboratory, strain 008766) and FlowJo software (v.10.10, BD Life Sciences) or OMIQ (Dotmatics) for high
Hsp90b1flox/flox mice, previously generated and described by our group65. dimensional analysis. The gating strategy for TIL analysis is provided
The P14 mouse strain was a gift from W. Cui (Northwestern University). in Supplementary Fig. 2. A list of antibodies used for the multispectral
OT-1 (strain 003831) and Rag2–/– (strain 033526) mice were purchased flow cytometry study is provided in Supplementary Table 1.
from The Jackson Laboratory. These mice were maintained in the animal For protein aggregation staining, cells were washed with HBSS
facility at the Ohio State University under standard conditions (ambi- (Sigma-Aldrich, H6648) twice and stained with 100 nM NIAD-4 (Cay-
ent temperature of 20–24 °C, relative humidity of 30–70% and a 12-h man, 18520) or 50 µM CRANAD-2 (Cayman, 19814) in HBSS for 30 min
dark–light cycle (lights on from 6:00 to 18:00)). Mice aged 6–8 weeks at 37 °C and 5% CO. Cells were stained using Live/Dead fixable Near
2
were used for experiments. All procedures were performed in strict IR (Invitrogen, L34975) at 4 °C for 15 min, followed by fixation (BD
accordance with the recommendations in the Guide for the Care and Biosciences, 554655) for 15 min and DAPI staining for 5 min at room
Use of Laboratory Animals of the National Institutes of Health (NIH). temperature. Cells were then analysed by ImageStream for acquiring
The protocol was approved by the Committee on the Ethics of Animal fluorescent images or Cytek Aurora for quantification.
Experiments of the Ohio State University. For SG analysis, cells were collected and stained using Live/Dead
fixable NIR, followed by fixation in BD Cytofix fixation buffer (BD
T cell isolation, stimulation and drug treatment Biosciences, 554655) for 15 min and permeabilization using a FOXP3
Spleens were isolated from C57BL/6J mice and minced into single-cell fixation and permeabilization kit for 30 min at room temperature.
suspensions. CD8+ T cells were isolated using an immunomagnetic Cells were then stained with anti-G3BP1 antibody (Proteintech, 13057-
negative selection kit (Stemcell, 19853). Isolated CD8+ T cells were first 2-AP) in permeabilization buffer for 1 h at room temperature and then
stimulated with 3 µg ml–1 plate-bound anti-CD3 (BioLegend, 100359) FITC-conjugated anti-rabbit antibody for 30 min. DAPI was added to
and 1 µg ml–1 anti-CD28 (BioLegend, 102121) antibodies in T cell medium the cell suspension and incubated for 5 min. Data were collected by
made with RPMI-1640 with 10% FBS, 1% penicillin–streptomycin, 1 mM ImageStream and analysed using IDEAS (v.6.2). Live cells were gated for
sodium pyruvate (Gibco, 11360-070), 1× MEM NEAA (Gibco, 11140- SG analysis. Cells with SG loci were determined by gating on the Bight
050), 10 mM HEPES (Gibco, 15630-080) and 50 µM 2-mercaptoethanol Detail Intensity feature high population on the FITC–G3BP1 channel.
(Gibco, 21985-023) supplemented with 100 U ml–1 recombinant human
IL-2 (acquired from the Biological Resources Branch at the NIH) in Protein synthesis rate measurement
12-well plates at a density of 106 cells per well for 48 h at 37 °C and 5% Nascent proteins were labelled using a Click-iT HPG Alexa Fluor 488
CO. For chronic stimulation, CD8+ T cells were re-stimulated every Protein Synthesis Assay kit (Thermo Fisher, C10428). Cells were incu-
2
2 days by passaging to new plates with plate-bound anti-CD3 in T cell bated with 50 µM HPG (Thermo Fisher, C10186) in T cell medium made
medium with IL-2. For acute stimulation, CD8+ T cells were passaged with methionine-free RPMI (Gibco, A14517-01) for 30 min at 37 °C and 5%
every 2 days and maintained in T cell medium with IL-2. In some experi- CO. Cycloheximide (Sigma-Aldrich, 239763) was added to the negative
2
ments, cells were treated with MK2206 (Cayman, 11593), LY294002 control group at 50 µg ml–1 to inhibit translation. In some experiments,
(Sigma-Aldrich, 440202) or rapamycin (Sigma-Aldrich, 553210) 2 days 2.5 µM MG132 (Sigma-Aldrich, M7449-1ML) or 10 nM bafilomycin A1
after initial activation and replenished concurrently with cell passage. (Sigma-Aldrich, SML1661) was added to cells after HPG incubation.
To measure cytokine production, activated cells were collected, Cells were then labelled following the manufacturer’s protocol and
plated and re-stimulated with 0.5× cell stimulation cocktail (Thermo analysed using Cytek Aurora.
Fisher, 00-4970-93) in T cell medium for 3 h at 37 °C and 5% CO. For measuring translation in TIL subsets in vivo, 50 mg kg–1 OPP (Vec-
2
tor Laboratories, CCT-1407-25) was administered into tumour-bearing
Tumour challenge and TIL isolation mice by intraperitoneal injection. Mice were killed exactly 1 h after
For the MC38 tumour model, 1 × 106 cells were subcutaneously injected injection. Tumours were isolated and processed into single-cell suspen-
into the right flank of shaved C57BL/6J mice. Mice were euthanized for sions. Cells were stained with surface markers and OPP was labelled
tumour collection 16 days after tumour implantation for cell sorting. using a Click-iT reaction kit following the manufacturer’s protocol
For the MB49 tumour model, 5 × 105 cells were subcutaneously injected (Thermo Fisher, C10457).
into the right flank of shaved C57BL/6J mice. Tumours were collected
13 days after tumour implantation. To prepare single-cell suspensions, Cell sorting
isolated tumours were chopped and washed with PBS before incubation Single-cell suspensions were stained using Live/Dead fixable blue
with collagenase I (200 U ml–1, Worthington, LS004196) in serum-free (Invitrogen, L23105) at 4 °C for 15 min. Cells were then washed twice
with FACS after viability dye staining. Tumour cells were enriched for was added onto plates coated with RetroNectin (Takara, T100B) and
CD45+ lymphocytes using a mouse TIL positive selection kit (Stemcell, spun at 1,800g at 32 °C for 2 h. Virus supernatant was removed after
100-0350) and spleen samples from mice infected with LCMV were centrifugation and washed with PBS twice. Polyclonal, P14 cells and
enriched for CD8+ T cells with a negative selection kit (Stemcell, 19853) OT-1 CD8+ T cells that have been activated for 16–48 h were added to
before viability staining. Cells were then incubated with a surface stain- the virus-coated plate and cultured for 24 h. Cells were washed twice
ing antibody cocktail for 30 min at 4 °C. Cells were washed twice with and plated into new plates for another 3–6 days for downstream analy-
FACS buffer and filtered through a 70 µm nylon filter immediately ses. For the generation of retrovirus for human T cell transduction, a
before loading into a Cytek Aurora CS for sorting. For sorting, a 100 µm similar approach to that used for mouse cells was used, with the key
nozzle was used for tumour-derived samples and a 70 µm nozzle for modification of using the Plat-A cell line for virus packaging. To trans-
spleen-derived samples. duce human CD8+ T cells, CD8+ T cells were magnetically isolated from
peripheral blood mononuclear cells (Stemcell, 17953) and activated
LCMV infection model with Dynabeads (Gibco, 11131D) for 1 day. After activation, the cells were
For acute LCMV infection, 8–10-week-old male mice were intraperito- transduced with the indicated virus. In brief, the cells were spinoculated
neally inoculated with 2 × 105 p.f.u. LCMV Armstrong. For chronic LCMV at 1,000g in a RetroNectin-virus-coated plate. After 24 h, the virus was
infection, 8–10-week-old male mice were intravenously inoculated with removed, and subsequent analyses were performed after an additional
2 × 106 p.f.u. LCMV clone 13 in 400 µl RPMI-1640. Mice were euthanized 6–8 days of activation and maintenance.
on day 8 and day 30 after infection.
ACT experiment
Gene editing in T cells by CRISPR–Cas9 P14 cells were isolated from the spleens of P14 mice and activated with
The sgRNAs targeting each candidate were designed and purchased 1 µg ml–1 gp33 peptide. Two days after activation, cells were edited by
from IDT. The sequences of sgRNAs are provided in Supplementary CRISPR–Cas9 as described above and expanded for another 2 days with
Table 2. Two days before electroporation, splenic CD8+ T cells were 100 U ml–1 IL-2. Next, 1 × 106 P14 cells were intravenously transferred per
isolated and activated with 3 µg ml–1 plate-bound anti-CD3 and 1 µg ml–1 mouse. Then 5 × 105 MB49-gp33 cells were subcutaneously injected
anti-CD28 antibodies in T cell medium supplemented with 100 U ml–1 into the right flank of shaved WT C57BL/6J mice or Rag2–/– mice. WT
IL-2. On the day of electroporation, RNPs were assembled by mixing mice were lymphodepleted using 5 Gray of total body irradiation on
1.5 µl sgRNA and 1 µg Cas9 nuclease V3 (IDT, 1081059) and incubated the day before cell transfer and randomized for treatment groups. OT-1
at room temperature for 20 min. Electroporation was prepared using cells were activated and transduced with retroviral vector as described
a P4 Primary Cell 4D-Nucleofector kit (Lonza, V4XP-4032). The acti- above. Transduced OT-1 cells were purified by cell sorting on the basis of
vated T cells were washed with PBS twice and resuspended with P4 positive GFP expression. In total, 2.5 × 105 OT-1 cells were intravenously
nucleofector solution with supplement provided by the kit. RNPs and transferred to B16-OVA tumour-bearing Rag2–/– mice. For OT-1 ACT
1 µl HDR Enhancer (IDT, 10007921) were added to the cell suspensions. experiments, 5 × 105 cells B16-OVA cells were subcutaneously injected
The reaction mix was loaded into a Nucleocuvette after incubation at into the right flank of Rag2–/– mice 8 days before adoptive transfer and
room temperature for 2 min. 4D-Nucleofector and program CMT137 randomized into treatment groups.
were used for electroporation. Cells were rested in T cell medium
with 50 U ml–1 IL-2 for 2 days and received re-stimulation every 2 days Immunofluorescence analysis by confocal microscopy
afterwards. At 8 days after electroporation, cells were collected for T cells were collected and spun onto glass coverslips in a 12-well plate.
downstream analyses. For protein aggregation staining, cells were stained with NIAD-4 and
fixed as described above. For CFTR staining, cells were fixed with fixa-
Protein electrophoresis and western blotting tion buffer (BD, 554655) for 15 min, permeabilized with 0.5% Triton
Cells were pelleted and lysed in NP-40 buffer (50 mM Tris 7.4, 150 mM X-100 in PBS for 20 min and blocked with 2% BSA for 1 h. Cells were
NaCl, 1% NP-40 and 0.1% sodium deoxycholate) supplemented with stained with primary anti-CFTR antibody (Proteintech, 20738-1-AP)
protease and phosphatase inhibitor cocktail (Thermo Fisher, 78440) and then Alexa Fluor 647-conjugated goat anti-rabbit IgG antibody
and incubated on a roller for 30 min at 4 °C. Samples were centrifuged (Thermo Fisher, A-21244). After staining, coverslips were mounted
at 18,000g, 4 °C for 15 min and supernatant was transferred to fresh onto glass slides with mountant and DAPI (Thermo Fisher, P36962).
tubes as the detergent-soluble fraction. The detergent-insoluble frac- Images were taken using an Olympus FV3000 microscope with ×60
tion was resuspended in NP-40 buffer supplemented with 4% SDS. The magnification and processed with Olympus OlyVIA (v.4.2). For analysis,
protein concentration was quantified using a BCA assay (Pierce, 23227). images were imported into ImageJ as .tiff files and adjusted to RGB stack
Native samples were diluted with native sample buffer (Thermo format for downstream processing. Thresholds for positive detection
Fisher, NP) and run on 3–8% Tris-acetate gels (Thermo Fisher, EA0378) of aggregates were determined through normalized autodetection
with Tris-glycine native running buffer (Thermo Fisher, LC2672). Sam- and maintained across all images with a lower threshold of 100 and
ples were electrophoresed at 150 V for 3 h at 4 °C. SDS–PAGE samples an upper threshold of 255 to generate binary image masks. The area,
were boiled in NuPAGE LDS sample buffer (Thermo Fisher, NP0007) average size per particle, percentage of area and mean fluorescence
and resolved on 4–12% Bis-Tris gels (Thermo Fisher, NP0335) with MOPS intensity were analysed using the Analyze Particles function selected
SDS running buffer (Thermo Fisher, NP0001). Samples were electro- for area, area fraction, fluorescence intensity, particle count and aver-
phoresed at 150 V for 1 h at room temperature. A list of antibodies used age particle size.
for western blot analyses is provided in Supplementary Table 1.
MS sample processing
Retrovirus packaging and T cell transduction Cell samples were collected and washed with PBS once. Cell pellets
The retroviral EV plasmid pMIG and pMIG-myrAKT were purchased were frozen at −80 °C if not immediately processed. Cells were lysed in
from Addgene (52107, 65063). The open-reading frame for CFTRΔF508 lysis buffer made with 5% SDS (Thermo Fisher, AM9820), 50 mM TEAB
was synthesized and cloned into the pMIG plasmid for this study. To (Thermo Fisher, 90114) and 2 mM MgCl (Thermo Fisher, AM9530G)
2
generate retrovirus for mouse T cell transduction, HEK293T cells were with HALT protease inhibitor cocktail (Thermo Fisher, 78441). Lysates
transfected with pMIG and pCL-Eco in Opti-MEM. The cell culture super- were homogenized using either a probe sonicator or a Biorupter. DNA
natant was collected 48 h after transfection and concentrated overnight was removed by centrifugation at 13,000g for 10 min and the pellet
with Retro-X Concentrator (Takara, 631456). Concentrated retrovirus discarded. For in vitro cell samples, the protein concentration was
Article
quantified using a BCA assay (Pierce, 23227) and 50 µg protein of each were compiled into the chromatogram library. Quantitative DIA injec-
sample was used for subsequent steps. For in vivo samples, total lysates tions were searched against this chromatogram library, again filtered
were used assuming accurate FACS cell counts. Cell lysates were then to a 1% peptide-level FDR. A normalized protein expression matrix for
treated with 20 mM DTT (Sigma-Aldrich, 10197777001) at 95 °C for all proteomics generated in this study is provided in Supplementary
10 min, followed by the addition of 40 mM iodoacetamide (Pierce, Table 3. Bubble plots of protein expression were generated using the
A39271) at room temperature for 30 min in the dark and then quenched R package tidyverse (v.1.3.1)71 based on z score-normalized protein
with 20 mM DTT for 15 min at room temperature. Phosphoric acid (1.2%; expression values. Gene set enrichment analysis for protein clusters
Sigma-Aldrich, 345245) was used to acidify proteins. Binding buffer was performed using Enrichr72–74.
with 100 mM TEAB in methanol (Thermo Fisher, A4581) was added to
samples that were then loaded onto S-traps (ProtiFi, C01-micro-80) Bulk RNA-seq sample preparation and data analysis
and washed with binding buffer 3 times. Proteins were digested with Acutely and chronically stimulated T cells were collected on day 8 after
trypsin (Pierce, 90058) at 47 °C for 2 h. Digested peptides were eluted initial activation. Cells were washed with PBS twice and pelleted. RNA
from S-traps with 0.2% formic acid (Thermo Fisher TS-28905) followed was first extracted using TRIzol and chloroform and then cleaned up
by a second elution with 50% acetonitrile (Sigma-Aldrich, T7408) in 0.2% using a RNeasy Micro kit (Qiagen, 74004). Sample library prepara-
formic acid. Eluates were pooled and lyophilized for storage at −80 °C. tion and sequencing were performed by Azenta Life Sciences. Poly(A)
selection was used for library preparation. Sequencing was performed
MS acquisition using an Illumina NovaSeq platform with a depth of 50 million reads
Peptides were reconstituted with 2% acetonitrile in 0.1% formic acid per sample. The raw bulk sequences were checked, trimmed and fil-
and separated using either an Easy-nLC 1200 coupled to an Thermo tered using Fastp (v.0.23.4)75. The filtered reads were mapped to the
Exploris 480 tandem mass spectrometer (Thermo Fisher) or an UltiMate mouse reference genome mm10 using HISAT2 (v.2.2.1)76, and samtools
3000 UHPLC coupled to a Thermo Fusion tandem mass spectrometer (v.1.17)77 was used to convert and sort BAM files. Last, the subread tool
(Thermo Fisher). In both set ups, peptides were first desalted online (v.2.0.6)78 was used for gene quantification and generating the raw
using an Acclaim PepMap 100 Trap column (75 µm inner diameter, expression matrix. Raw expression data were first log-normalized, and
150 mm length, 3 µm C18 packing) and then separated and ionized the R package Limma (v.3.56.2)79 was used to fit the model and perform
using either a 50 cm (Easy-nLC) or 25 cm (Ultimate 3000) Easy-Spray differential expression analysis. To avoid NA values, a pseudo count of
HPLC column (75 µm inner diameter, 2 µm C18 packing) with a 90-min 1 was added to the raw count matrix. Genes with an absolute log[fold
linear gradient. change] value greater than 1.5 and FDR-adjusted P value smaller than
All data-independent acquisition (DIA) measurements were con- 0.05 are considered as differentially expressed genes.
figured in a staggered window pattern using boundaries optimized to
place window boundaries in forbidden zones. The Thermo Fusion was Statistical comparison of protein expression and gene
configured to use two DIA injections (covering peptide precursors from expression
400 to 700 m/z and from 700 to 1,000 m/z) of 38 ×8 m/z-wide windows To accurately compare protein and gene expression levels, we created a
in a staggered window pattern. These windows were configured to have hash table (Supplementary Table 4) that included the protein accession
17,500 resolution and an automatic gain control (AGC) target of 4 × 105. number, protein name, gene name and Mouse Genome Informatics
Precursor spectra were placed every 38 scans (1 per cycle) using 35,000 (MGI) number. Each protein and RNA matrix needed to match the hash
resolution and an AGC target of 4 × 105. Similarly, the Thermo Exploris table, and only the overlapped proteins and genes were kept.
480 was configured to use single-injection DIA measurements (cover- We compared the normalized and log-transformed protein expres-
ing peptide precursors from 400 to 1,000 m/z) of 38 × 16 m/z-width sion and gene expression levels in samples of the sample condition (for
windows. These windows were configured to have 30,000 resolution example, day 8 T samples). Only proteins and genes that overlapped
ex
and an AGC target of 1 × 106. Precursor spectra were placed every 38 in both protein and RNA data were retained for comparison. A Pearson’s
scans (1 per cycle) using 60,000 resolution and an AGC target of 1 × 106. correlation test was applied to calculate the correlation coefficient
For each dataset, a sample pool was made from subaliquots and between protein expression and gene expression levels. We also com-
used for library generation. We used gas-phase fractionation (GPF) pared the log[fold change] of proteins and genes between different
DIA following the chromatogram library approach66,67. For this, we conditions. The log[fold change] of proteins and genes were calculated
injected each peptide pool 6 times using different 100 m/z regions in the analysis of differentially expressed genes described above.
(400–500 m/z, 500–600 m/z, 600–700 m/z, 700–800 m/z, 800– We generated a functional gene list to further evaluate the expres-
900 m/z and 900–1,000 m/z). Each injection was configured to use sion level of proteins and genes undergoing specific cell functions,
4 m/z staggered DIA windows and appropriate precursor windows. including 13 gene ontology terms, one EIF2A-dependent and one
Otherwise, all measurements were performed as for normal DIA above EIF2A-independent gene list. Specifically, the EIF2A-dependent
on their respective instrument. and EIF2A-independent genes were determined according to the
EIF2A-regulated upstream open reading frames35. As previously
Proteomic data analysis described35, EIF2A-regulated upstream open reading frames were
Raw files were demultiplexed using MSConvert in the Proteowiz- defined as the ratio of 5′ untranslated region (UTR) translation in con-
ard package (v.3.0.20169)68 and then searched using EncyclopeDIA trol/5′ UTR translation in Eif2a KO > 4. The remaining mRNAs with a
(v.2.12.31). EncyclopeDIA was configured with the default settings for ratio <4 were defined as non-EIF2A regulated (EIF2A-independent).
Orbitraps: 10 ppm precursor, fragment and library tolerances. Encyclo- The 5′ UTR translation rate was quantified for mRNAs with an average
peDIA was allowed to consider both B and Y ions, and trypsin digestion of more than 16 reads over all replicates. Genes in each of the 26 lists
was assumed. Searches were performed using a two-step procedure. are highlighted on the scatter plot to compare the protein and gene
First, the GPF-DIA injections were searched using a Prosit69,70 predicted expression/log[fold change].
spectrum library to generate a chromatogram library based on the Mus
musculus UniProt FASTA database (downloaded on 22 October 2019, Gene signature score analysis
containing 17,025 entries). All z = +2 or z = +3 peptides from 396.4 to For each of the gene lists mentioned above, we also calculated a gene
1002.7 m/z (with a maximum of one missed cleavage) were predicted signature score based on the single-sample gene set enrichment
assuming a normalized collision energy of 33. Peptides detected in the analysis (ssGSEA) method. An in-house script was used to perform
six GPF-DIA injections at a 1% peptide-level false discovery rate (FDR) the ssGSEA analysis. The R package heatmaply (v.1.4.2)80 or Morpheus
(https://software.broadinstitute.org/morpheus) was used to draw
the heatmap. For gene signature score analysis for scRNA-seq data, RNA velocity and trajectory inference
the raw expression matrix of LCMV scRNA-seq data was downloaded RNA velocity analysis was performed to infer the directionality of cel-
from GSM3701181 (ref. 31). Cells were divided into three categories lular state transitions using spliced and unspliced transcript counts.
on the basis of gene expression levels: progenitor state (Slamf6 > 0 Velocities were computed using the scVelo toolkit (v.0.3.3)103,104, which
and Cx3cr1 = 0); intermediate state (Cx3cr1 > 0); and terminal state estimates transcriptional dynamics across single cells. The resulting
(Slamf6 = 0 and Cx3cr1 = 0). Cells in each category were randomly velocity vectors were projected onto the UMAP embedding to visual-
divided into three equal subgroups. Pseudo bulk gene expression was ize the flow of differentiation. To infer developmental trajectories, the
defined by the average expression of genes in each cell subgroup. Then, Slingshot algorithm was applied to the UMAP coordinates, incorporat-
the same ssGSEA method was performed on the pseudo bulk expression ing RNA velocity information to identify lineage structures. Slingshot
data to calculate the gene signature scores and to generate the heatmap. fit smooth curves (principal curves) through the data and assigned
pseudotime values along each inferred lineage. Two dominant lineages
Pan-cancer scRNA-seq data collection were identified: one progressing towards a T cell phenotype (line-
ex
To construct a comprehensive pan-cancer scRNA-seq dataset, we com- age 1) and the other towards an effector-like phenotype (lineage 2).
piled transcriptomic profiles from 346 tumour samples derived from Signature scores for naive, exhaustion and T -PSR gene modules were
ex
251 individuals across 20 publicly available scRNA-seq datasets81–100 calculated across pseudotime for each lineage using averaged normal-
(Supplementary Table 5). To ensure data consistency and to minimize ized expression of predefined marker genes.
platform-related biases, only datasets generated using the 10x Genom-
ics droplet-based platform were included for our analyses. Validation of the T ex -PSR signature in CD8+ T cells and its
prognostic impact
Quality control and preprocessing of the pan-cancer scRNA-seq To assess the clinical significance of the T -PSR signature in CD8+ T cells,
ex
data. We applied rigorous quality control measures using the pack- we analysed public processed scRNA-seq data from 116 liver cancer
age Scanpy (v.1.9.5)101 to filter and preprocess single-cell transcrip- samples obtained from 94 male patients105. Survival analyses were
tomic data. The following inclusion criteria were applied: (1) each cell restricted to primary tumours and metastatic samples. After quality fil-
expressed at least 200 genes; and (2) mitochondrial gene content tering, batch correction and cell-type annotation using the established
remained below 20% of total counts. Further filtering steps removed preprocessing pipeline, CD8+ T cells were isolated and T -PSR signature
ex
the following data: (1) low-quality barcodes indicative of debris (<400 scores were computed using the scanpy.tl.score_genes function from
detected genes, <500 unique molecular identifiers); and (2) potential the Scanpy package (v.1.9.5).
duplicate cells (>5,500 detected genes or >30,000 unique molecular
identifiers). After quality control, raw count matrices and AnnData T -PSR signature expression in CD8+ T cells and its impact on
ex
objects were concatenated, and counts were normalized to transcripts patient survival. To evaluate the prognostic significance of T -PSR
ex
per million using sc.pp.normalize_total, followed by log-transformation expression levels in CD8+ T cells, we performed survival analyses using
with sc.pp.log1p. Non-tumour cells were excluded before normaliza- Kaplan–Meier curves, with statistical comparisons conducted using
tion, which produced 1,030,968 high-quality single cells and 14,090 the log-rank test and univariate Cox proportional hazards (Cox PH)
genes for downstream analyses. models, as specified in each figure. Two additional multivariable Cox
PH models were fitted to account for potential confounders. The hazard
Batch correction and data integration. To harmonize datasets across ratio and 95% confidence intervals were reported on the basis of these
studies while preserving biological signals, we used the Python package models. Kaplan–Meier survival curves were generated to compare
scVI (scvi-tools v.1.0.4)102 for batch-effect correction and data integra- high versus low T -PSR expression in liver cancer scRNA-seq datasets,
ex
tion. The scVI model was trained with sample identity as a covariate, with P values computed using univariate Cox PH models. To determine
mitigating inter-sample technical variability while ensuring robust the optimal cut-off value for T -PSR signature expression in relation
ex
integration of multiple datasets. The efficiency of batch correction was to survival outcomes, we used the surv_cutpoint function from the
assessed by quantifying the reduction in batch-specific effects while R package survminer. This approach uses maximally selected rank
maintaining key biological variance. After correction, downstream statistics from the R package maxstat106 to stratify patients into low-risk
analyses—including clustering, differential gene expression and trajec- and high-risk groups. Moreover, continuous variables included in the
tory inference—were performed on the integrated dataset. UMAP was Cox PH107 models were assessed for linearity to ensure model validity.
used for visualization, depicting cellular heterogeneity across batches,
datasets, sex, organ origins and cancer types. T ex -PSR expression in immunotherapy-treated patients
We further investigated T -PSR expression in responders and
ex
Cell-type annotation of pan-cancer scRNA-seq data. To anno- non-responders across independent scRNA-seq datasets from patients
tate cell populations, we leveraged the scANVI algorithm (scVI-tools receiving diverse immunotherapy treatments, including CAR T cell
v.1.0.4), which provided pre-labelled reference annotations for epi- therapy for refractory B cell lymphoma61, anti-PD1 therapy for lung
thelial, endothelial, fibroblast, lymphoid, myeloid and plasma cells. cancer and advanced renal cell RCC62,63, and anti-CTLA-4 with anti-PD1
Initial clustering was performed in the scANVI latent space, followed combination therapy for RCC64,108. For each dataset, we applied the
by Leiden clustering to assign cell identities. The scANVI model was same preprocessing pipeline, including quality filtering, batch cor-
trained with max_epochs=20, and cluster annotations were transferred rection and cell-type annotation, as described for the pan-cancer
with n_samples_per_label=100. For detailed characterization of T cell scRNA-seq dataset.
subpopulations, we further integrated corresponding AnnData objects
and applied scVI-based batch correction. Statistical analysis
Statistical analyses were performed using GraphPad Prism (v.10).
Functional signature calculation for scRNA-seq data. We used Two-tailed unpaired Student’s t-test was used for comparison between
the scanpy.tl.score_genes function from the Python package Scanpy two groups. One-way ANOVA was used for comparisons among three
(v.1.9.5) to compute gene set scores across individual cells, which or more groups. Two-way ANOVA was used to compare curves of
enabled the quantification of functional signatures in the scRNA-seq time-course studies, including cell and tumour growth curves. P < 0.05
dataset. was considered significant.
