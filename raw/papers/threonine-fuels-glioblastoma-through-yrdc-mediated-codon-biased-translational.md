---
source_path: /mnt/c/Users/Administrator/Zotero/storage/Q76QR8WC/Wu 等 - 2024 - Threonine fuels glioblastoma through YRDC-mediated.pdf
ingested: 2026-04-23
sha256: 1882f81ebdfd4dc1
---

nature cancer
Article https://doi.org/10.1038/s43018-024-00748-7
Threonine fuels glioblastoma through
YRDC-mediated codon-biased translational
reprogramming
Received: 8 May 2023 Xujia Wu 1,2, Huairui Yuan1, Qiulian Wu1, Yixin Gao2, Tingting Duan 1,
Kailin Yang3, Tengfei Huang1, Shuai Wang1, Fanen Yuan1, Derrick Lee1,
Accepted: 23 February 2024
Suchet Taori1, Tritan Plute4,5, Søren Heissel6, Hanan Alwaseem 6,
Published online: xx xx xxxx Michael Isay-Del Viscio6, Henrik Molina6, Sameer Agnihotri4,5, Dennis J. Hsu1,7,
Nu Zhang 2 & Jeremy N. Rich 1,8
Check for updates
Cancers commonly reprogram translation and metabolism, but little
is known about how these two features coordinate in cancer stem cells.
Here we show that glioblastoma stem cells (GSCs) display elevated
protein translation. To dissect underlying mechanisms, we performed
a CRISPR screen and identified YRDC as the top essential transfer RNA
(tRNA) modification enzyme in GSCs. YRDC catalyzes the formation of
N6 -t hr eo ny lc ar ba mo yladenosine (t6A) on ANN-decoding tRNA species
(A denotes adenosine, and N denotes any nucleotide). Targeting YRDC
reduced t6A formation, suppressed global translation and inhibited tumor
growth both in vitro and in vivo. Threonine is an essential substrate of
YRDC. Threonine accumulated in GSCs, which facilitated t6A formation
through YRDC and shifted the proteome to support mitosis-related genes
with ANN codon bias. Dietary th r eon ine restriction (TR) reduced tumor t6A
formation, slowed xenograft growth and augmented anti-tumor efficacy of
chemotherapy and anti-mitotic therapy, providing a molecular basis for a
dietary intervention in cancer treatment.
Glioblastoma (GBM) represents the most common primary malignant Failure to achieve cure for patients with GBM is multifactorial, including
brain tumor with a median survival of less than 2 years1. GBM was originally the presence of GSCs, a stem-like population that exhibits resistance to
designated as GBM multiforme due to marked intratumoral morphologic radiotherapy and chemotherapy and generates a hierarchy of cell types
variation. Modern molecular analyses have shown that GBMs display within tumors3. Although the impact of GSCs remains controversial,
striking spatial and temporal variation in genomic and epigenomic states defining their molecular regulation may offer therapeutic paradigms to
and the tumor microenvironment, including the vasculature and immune improve the clinical care of patients afflicted with GBM.
responses2. Most GBMs recur within 2 to 3 cm of the original resection cav- Many cancers, including GBM, display accelerated protein syn-
ity often with a nodular pattern of growth, suggesting clonal recurrence. thesis4. However, a deep understanding of translational adaptation
1Hillman Cancer Center, University of Pittsburgh Medical Center, Pittsburgh, PA, USA. 2Department of Neurosurgery, the First Affiliated Hospital of
Sun Yat-sen University, Guangdong Provincial Key Laboratory of Brain Function and Disease, Guangdong Translational Medicine Innovation Platform,
Guangzhou, China. 3Department of Radiation Oncology, Taussig Cancer Center, Cleveland Clinic, Cleveland, OH, USA. 4Department of Neurological
Surgery, University of Pittsburgh School of Medicine, Pittsburgh, PA, USA. 5John G. Rangos Sr. Research Center, Children’s Hospital of Pittsburgh, Pittsburgh,
PA, USA. 6Proteomics Resource Center, the Rockefeller University, New York, NY, USA. 7Department of Medicine, University of Pittsburgh, Pittsburgh, PA,
USA. 8Department of Neurology, University of Pittsburgh, Pittsburgh, PA, USA. e-mail: zhangnu2@mail.sysu.edu.cn; drjeremyrich@gmail.com
Nature Cancer
Article https://doi.org/10.1038/s43018-024-00748-7
in response to oncogenic signaling is lacking, especially in cancer cells, as measured by the higher frequency of OPPhi cells (Fig. 1e,f and
stem cells. Although normal embryonic and tissue-resident stem cells Extended Data Fig. 1d,e). To address the limitations of using CD133
display low global translation rates5, mounting evidence suggests that alone as a GSC marker14, we included SOX2, a fate-determining GSC
translational regulation in cancer stem cells depends upon tumor type marker15, for validation. Most CD133+ GSCs displayed high SOX2 levels
and cell-specific oncogenic signals6,7. Protein translation requires fine (Fig. 1g). CD133+SOX2hi tumor cells showed higher OPP incorporation
tuning of multiple components and factors, including messenger RNA than CD133−SOX2lo/− tumor cells (Fig. 1h,i), supporting the idea that
(mRNA), ribosomes, tRNA and other regulators4,5. Post-transcriptional GSCs are relatively translationally active.
modifications of tRNA permits modulation of not only global efficiency Next, we mined a large single-cell RNA sequencing (scRNA-seq)
in translation of transcripts but also selective efficiency of codons. The dataset that included GSC cultures and tumor cells from patients with
human genome encodes ~500 tRNA species that recognize 61 codons GBM16 (Extended Data Fig. 1f). Stemness marker PPP1R14B and differen-
for 20 amino acids, for which over 40 types of tRNA modifications tiation marker GFAP distinguished GSCs from other tumor cells in two
have been identified8. Dysregulation of tRNA modifications is preva- principal components (Extended Data Fig. 1g). A translational signature
lent in cancer9, but how cancer stem cells co-opt tRNA modifications from the Gene Ontology (GO) database (GO biological process (GOBP):
and metabolism to fulfill their translational needs remains largely positive regulation of translation) was used to infer translational activ-
unexplored. ity, which was higher in GSCs than in bulk tumor cells (Fig. 1j). To rule
Among tRNA modifications, t6A is highly conserved across evolu- out the potential bias of comparison between in vitro GSC cultures
tion10. This modification localizes to position 37 in the anticodon stem and in vivo tumor cells, we segregated each cell population into two
loop and is exclusively found in tRNA species that decode ANN codons. parts with distinct differentiation states (Methods) and reperformed
Modified tRNA species are locked in a three-dimensional structure that the comparison (Extended Data Fig. 1h,i). Consistently, most GSCs
defines translational efficiency of codons. Impaired t6A biosynthesis showed higher translational activities than tumor-like GSCs (Fig. 1k),
causes an autosomal recessive disease, Galloway–Mowat syndrome, and GSC-like tumor cells exhibited higher translational activities than
characterized by defective nervous system development11. Despite differentiated tumor cells (Fig. 1l).
the requirement of t6A in the nervous system, the role of t6A in brain To explore whether GSCs display increased translation in vitro,
cancer remains poorly characterized. we analyzed transcriptomes of a panel of cultured GSCs and matched
Based on this background, we hypothesized that cancer stem differentiated tumor cells (differentiated glioma cells; DGCs)15. Gene set
cells in brain tumors differentially regulate translation through enrichment analysis (GSEA) revealed enriched translational signature in
post-transcriptional tRNA modifications to reveal potential thera- GSCs (Fig. 1m). To measure protein synthesis in vitro, we pulse-treated
peutic paradigms. Indeed, we found that GSCs display preferential cells with puromycin for 30 min and detected puromycin incorporation
regulation of protein synthesis with selective dependency on YRDC, a by immunoblotting. GSCs exhibited greater puromycin incorporation
rate-limiting enzyme in t6A generation. Concordant with the effects of than DGCs or neural stem cells (NSCs) (Fig. 1n,o and Extended Data
t6A locking tRNA tertiary structures, GSCs display a YRDC-dependent Fig. 1j,k). Increased protein translation was not restricted to a specific
codon bias in translation to sustain mitosis. Leveraging the role of subcellular compartment, as indicated by upregulation of OPP signals
threonine as an enzymatic substrate for YRDC to generate t6A, we throughout cells (Fig. 1p). Together, GSCs exhibit accelerated transla-
developed a strategy to translate these observations into a targeting tion in vivo, which can be recapitulated in vitro.
strategy by restricting dietary threonine, resulting in inhibition of Cancer stem cells, including GSCs, are not obligatorily quies-
tumor proliferation and in vivo growth. cent and actively divide in dedicated niches17. We confirmed that
GSCs proliferate faster than paired DGCs in vitro (Extended Data
Results Fig. 1l,m). To rule out the possibility that the increased translation
GSCs exhibit high translation rates in GSCs is simply a byproduct of increased proliferation, we used a
To examine the rate of protein synthesis of GSCs, we first injected pan-cyclin-dependent kinase (CDK) inhibitor, alvocidib18, to reduce
O-propargyl-puromycin (OPP), an alkyne analog of puromycin that the proliferation of GSCs to a level comparable to that of paired DGCs
is used for quantification of protein synthesis12, into the contralat- (Extended Data Fig. 1n,o). Under similar proliferation rates, GSCs
eral hemispheres of mice bearing patient-derived xenografts. Brains treated with alvocidib still exhibited higher global translation rates
were harvested after 30 min, and different cell populations were sepa- than paired DGCs (Extended Data Fig. 1p), indicating the existence
rated by flow cytometry. Human CD147 was employed to enrich for of other translational regulators. Also, the increased translation in
patient-derived tumor cells13, and CD133 and SRY-box transcription GSCs is not simply attributable to increased metabolic activity, as we
factor (TF) 2 (SOX2) were used to distinguish stem cell populations14. did not observe a consistent alteration of metabolic markers, includ-
OPP signal intensity represented global protein synthesis rates (Fig. 1a). ing mammalian target of rapamycin (mTOR), AMPKα and eIF2α, in
Tumor cells displayed higher percentages of rapidly translating cells GSCs compared to DGCs (Extended Data Fig. 1q). Together, neither
(OPPhi) than non-neoplastic cells (Fig. 1b–d and Extended Data Fig. 1a–c). increased proliferation nor metabolic activity appear to account for
CD133+ GBM cells exhibited higher translation rates than CD133− tumor increased translation in GSCs.
Fig. 1 | GSCs exhibit high translation rates. a, Graphic illustration of in vivo seq data of matched GSCs and DGCs (GSE54791). NES, normalized enrichment
protein translation measurement in different cell populations. Human (h) score. n,o, Immunoblots showing puromycin incorporation in the indicated cells.
CD147 is used to mark patient-derived tumor cells; CD133 and SOX2 are used NSC11, neural stem cell 11; HNP1, human neural progenitor 1. p, Representative
to distinguish GSCs. b–i, Gating strategy (b,g), representative histogram images of in vitro OPP incorporation in the indicated cells. Scale bar, 20 μm. DAPI,
plot (c,e,h) and statistical quantification (d,f,i) (n = 6 mice per group) of OPP 4,6-diamidino-2-phenylindole. In d,f,i, boxes represent data within the 25th to
flow cytometric analysis of the indicated cell populations in GSC23-derived 75th percentiles, whiskers depict the range of all data points, and horizontal lines
intracranial tumors. The cutoff used to define high (OPPhi) and low (OPPlo) OPP within boxes represent median values. In j–l, violin plots represent the overall
signal is 103 on the logarithmic scale. j–l, Quantification of translational activities distribution of data points. Box plots show median, upper and lower quartiles;
in scRNA-seq data of 28 early-passage GSC cultures derived from 24 patients and whiskers depict 1.5 times the interquartile range. In n–p, immunoblots and
14,207 malignant cells from seven patients with GBM. In j, n = 65,655 for all GSCs images are representative of three independent experiments with similar results.
and n = 14,207 for all tumor cells. In k, n = 64,417 for GSCs and n = 1,238 for tumor- Two-tailed paired t-test for d,f,i. Two-tailed unpaired t-test for j–l. Weighted
like GSCs. In l, n = 1,971 for GSC-like tumor cells and n = 12,236 for differentiated Kolmogorov–Smirnov statistic test for m.
tumor cells. m, GSEA analysis of GOBP: positive regulation of translation in RNA-
Nature Cancer
Article https://doi.org/10.1038/s43018-024-00748-7
CRISPR screening of tRNA modifiers in GSCs translational activation, we performed CRISPR knockout screening
Dysregulation of tRNA modifications serves essential roles in in two patient-derived GSCs targeting 111 genes reported or predicted
translational regulation and cancer progression8,9. To investi- to regulate tRNA modification from the GO database, the Reactome
gate potential tRNA modifiers that contribute to GSC growth and database and prior reports8,19 (Fig. 2a and Supplementary Table 1).
a
NES = 1.5039
P = 0.0055
n
Nature Cancer
erocs
tnemhcirnE
GOBP: positive regulation of translation
0.30
0.25
0.20 0.15
0.10
0.05
0
–0.05
GSCs DGCs
RKI 456 468 23 3028 387
GSCs + – + – + – + – + – + – DGCs – + – + – – + – + – +
nicymoruP
)sisehtnys
nietorp(
GSCs OPP
Tumor digestion + CD133+SOX2hi tumor cells
Tumor propagation 3 in 0 c - o m rp in o r in a t v io iv n o flow analysis hCD147+ tumor cells CD133–SOX2–/lo tumor cells
hCD147– non-neoplastic cells
b c d
e CD133– tumor cells CD133+ tumor cells
h
OPP/DAPI
+
Tubulin
ladoM
Non-neoplastic cells
Tumor cells
100
80
60 OPPhi
40
20
0
ladoM
100
80
OPPhi 60
40
20
0
CD133–SOX2–/lo tumor cells
CD133+SOX2hi tumor cells
OPP–Alexa Fluor 647
ladoM
C
D133–
C
D133+
100
80
60 OPPhi
40
20
0
)%(
ihPPO
fo
tnecreP
100
80
60
40
20
0
)%(
ihPPO
fo tnecreP
100
80
60
40
20
0
Non-neoplastic
Tu
mor
)%(
ihPPO
fo
tnecreP
f
g
100
80
60
40
20
0
C
D133–S
C
O D X 1 2 3
–/
3
l
+
o
S
OX2hi
746
roulF
axelA–PPO
GSC23
Isotype Single cells 106
0.019 0.039
106
3.46 67.2
105 105 hCD147+
104 104 tumor cells
103 103 73.8%
102 102
101 101
100 99.6 0.31 100 20.8 8.50
100101102103104105106 100101102103104105106
hCD147–FITC
Isotype Tumor cells 106 106 0.031 0.027 73.8 5.40
105 105 CD133+
104 104 6.07%
103 103
102 102 CD133–
101 101 90.9%
100 99.8 0.10 100 20.1 0.67
100101102103104105106 100101102103104105106
hCD133–PE
106 106
105 105 104 104
103 103
102 102
101 101
100 100
100101102103104105106 100101102103104105106
SOX2–Pacific Blue
EP–331DCh
Isotype Tumor cells
i 0.031 0.050 0.42 5.86 CD133+
SOX2hi 5.86%
CD133–
SOX2–/lo
99.7 0.21 51.0 42.7 51.0%
j
ytivitca
lanoitalsnarT
All single cells
1.0
0.9
0.6 0.5
0.3
0 0
All GS Cs All tu m c o e r lls GS Cs Tu mor-l G ik S e Cs
ytivitca
lanoitalsnarT
k l m
All GSCs
o p
NSCs GSCs
NS C1 H 1 NP1 RKI 456 468 23 3 028 387
nicymoruP
)sisehtnys
nietorp(
scRNA-seq
0.9
0.6
0.3
0
t G u S m C o - D r l i i c k ff e e e l r t ls u en m t o ia r t e c d ells
GSC456 DGC456
NSC11
GSC23 DGC23
Tubulin
ytivitca
lanoitalsnarT
P = 0.0112
100101102103104105106
OPP–Alexa Fluor 647
P = 0.0101
100101102103104105106
OPP–Alexa Fluor 647
P = 0.0078
100101102103104105106
All tumor cells
P < 2.22 × 10−16 P < 2.22 × 10−16 P < 2.22 × 10−16
kDa kDa
180 180
15 15
55 55
Article https://doi.org/10.1038/s43018-024-00748-7
Depletion of guide RNA (gRNA) content of GSCs on day 14 compared potentially associated with YRDC (Supplementary Table 5), of which 36
to day 1 (baseline) identified YRDC as the top essential tRNA modifier in TFs were enriched in GSCs compared to both DGCs and NSCs (Extended
both GSC screens (Fig. 2b,c and Supplementary Tables 2 and 3). By con- Data Fig. 2d). OLIG1 and OLIG2 were the top two TFs based on their
trast, most gRNA species enriched on day 14 were specific for each GSC expression patterns (Extended Data Fig. 2e). Loss of OLIG2, but not
(Extended Data Fig. 2a), which may reflect the heterogeneity of GSCs. OLIG1, reduced YRDC expression (Extended Data Fig. 2f–i), suggest-
We identified nine significant hits in the screen of GSC456 cells and 12 ing that OLIG2 plays a more important role in driving YRDC transcrip-
significant hits in the screen of GSC23 cells, of which YRDC and RPUSD2 tion. We further identified peaks enriched within the YRDC promoter
were the only two genes overlapping (Fig. 2d). YRDC encodes an enzyme in OLIG2 ChIP–seq data15 (Extended Data Fig. 2j). We predicted two
that functions with the downstream KEOPS complex (LAGE3, OSGEP, potential OLIG2-binding sites, which we verified by ChIP followed by
TP53RK, TPRKB and GON7) and O-sialoglycoprotein endopeptidase-like quantitative PCR (qPCR) (ChIP–qPCR) analysis in two GSCs (Extended
1 (OSGEPL1) to catalyze the biosynthesis of t6A on cytoplasmic and Data Fig. 2k,l), indicating that OLIG2 directly binds to the YRDC locus.
mitochondrial tRNA species, respectively10. In the GSC23 screen, three OLIG2 expression positively correlated with YRDC expression in the
of the five subunits of the KEOPS complex (encoded by TPRKB, GON7 Chinese Glioma Genome Atlas (CGGA) and the Mack_GBM dataset25
and TP53RK) were depleted on day 14 (Fig. 2d), highlighting the crucial (Extended Data Fig. 2m,n).
role of cytoplasmic t6A in GSC propagation. Next, we interrogated YRDC contributions to GSC maintenance
To confirm these observations, we mined published genome-wide and protein translation. Targeting YRDC (Extended Data Fig. 3a)
GSC screens16,20,21 with the BAGEL algorithm22, using higher Bayer fac- decreased GSC viability (Fig. 3f–h) and 5-ethynyl-2′-deoxyuridine
tor (BF) scores to indicate greater confidence of gene essentiality. (EdU) incorporation (Fig. 3i and Extended Data Fig. 3b). Depleting
Among the tRNA modification enzymes, YRDC ranked as one of the YRDC diminished GSC self-renewal, as assayed by impaired sphere for-
top essential genes in multiple GSC screens (Fig. 2e–i). To explore mation frequency using extreme limiting dilution assays (Fig. 3j–l) and
GSC-specific dependencies, we compared BF scores between GSCs reduced sphere size (Fig. 3m and Extended Data Fig. 3c), demonstrat-
and NSCs for each gene. YRDC ranked as the second most GSC-specific ing the crucial role of YRDC in GSC maintenance. By contrast, loss of
tRNA modifying gene by fitness relative to NSCs (Fig. 2j). To inves- YRDC did not substantially diminish NSC proliferation (Extended Data
tigate the pan-cancer essentiality of YRDC, we next explored screen Fig. 3d,e), demonstrating the specific requirement for YRDC in GSCs.
results from the Cancer Dependency Map (DepMap) project23. YRDC As YRDC catalyzes the formation of t6A on tRNA, we hypothe-
was essential in the majority of cancer cell lines, while the dropout sized that YRDC functions through t6A to regulate protein transla-
effects of YRDC in non-neoplastic cells were only modest (Fig. 2k). We tion in GSCs. Mass spectrometry (MS) showed that targeting YRDC
found similar results in another genome-wide screen dataset24, as YRDC reduced t6A on tRNA (Fig. 3n,o), consistent with its enzymatic activ-
was essential across different carcinoma cell lines but non-essential ity. YRDC-depleted GSCs exhibited slower translation rates (Fig. 3p).
in non-transformed epithelial cells (Fig. 2l). Collectively, these data mTOR signaling26 and the eukaryotic initiation factor (eIF)2α-mediated
suggest a specific requirement for YRDC in GSCs and other cancer integrated stress response (ISR)27 are two essential pathways in trans-
cells, providing the rationale for targeting YRDC in GBM and other lational regulation. YRDC deprivation did not substantially diminish
malignancies. the phosphorylation of mTOR or induce activation of eIF2α (Extended
Data Fig. 3f), suggesting that reduced translation was not mediated
YRDC is essential for GSC maintenance and translation through these two pathways.
In the transcriptomic data of GSCs versus matched DGCs15 and GBM
versus normal brain cortex, tRNA modification enzymes were differ- Threonine dynamically regulates t6A and translation
entially expressed, as we identified 19 enzymes enriched in GSCs and Threonine is an essential substrate of YRDC10 (Fig. 4a). We traced threo-
17 enzymes enriched in GBM (Fig. 3a,b and Supplementary Table 4). nine using stable isotope-labeled threonine ([13C,15N]l-threonine) for
4
Overlap between these two sets highlighted YRDC as one of the two 6 h, resulting in about 30% labeled t6A in GSCs, with lower labeled levels
enzymes upregulated in both GSCs and GBM (Fig. 3c). Preferential in DGCs (Fig. 4b), which suggests the rapid influx of threonine to t6A for-
expression of YRDC in GSCs compared to both DGCs and NSCs was mation. To test whether threonine availability dynamically regulates t6A
further confirmed by immunoblotting (Fig. 3d,e). Analysis of chro- levels, we modulated threonine concentrations in culture medium and
matin immunoprecipitation (ChIP)–sequencing (ChIP–seq) data15,25 analyzed t6A by MS. Threonine supplementation increased t6A without
showed extensive enrichment of acetylation of histone H3 on lysine affecting total adenosine levels at 72 h. By contrast, TR decreased t6A
27 (H3K27) (H3K27ac) on the YRDC promoter in GSCs (Extended Data without reducing total adenosine levels (Fig. 4c). Consistent with the
Fig. 2b), indicating that YRDC is actively transcribed in GSCs. Proneural changes in t6A, threonine supplementation facilitated protein synthe-
(PN) DGCs are reprogrammed to GSCs by expressing a set of core neu- sis, while TR reduced protein synthesis (Fig. 4d,e). These results dem-
rodevelopmental TFs: POU3F2, SOX2, SALL2 and OLIG2 (ref. 15). Upon onstrate that there is a concentration-dependent relationship between
reprogramming, the H3K27ac signal increased on the YRDC promoter threonine levels and t6A biosynthesis and rates of protein translation.
(Extended Data Fig. 2c). As threonine is an essential amino acid, we next asked whether
To understand the upstream regulator of YRDC, we scanned the inhibitory effect of TR on protein translation was nonspecific due
TF-binding motifs on the YRDC promoter and identified 568 TFs to cellular sensing of an amino acid deficiency. Mammalian cells sense
Fig. 2 | CRISPR screening of tRNA modifiers in GSCs. a, Graphic illustration of differences of average quantile normalized BF (qBF) scores for each tRNA
CRISPR knockout screening targeting tRNA modification genes. sgRNA, single- modification enzyme between GSCs and NSCs. Data are from genome-wide
guide RNA. RRA, robust ranking aggregation. b,c, Gene rank of negative selection CRISPR knockout screens of 24 GSCs and four NSCs. Data are z transformed.
results for GSC456 (b) and GSC23 (c) cells in CRISPR screens. Values lower on the Top hits and YRDC are highlighted. Diff, difference. k, Chronos analysis of YRDC
y axis indicate greater gene essentiality. The top three ranked genes are labeled. dependency in different cell lines in DepMap CRISPR knockout screens (n = 1,077
d, Significant hits (P < 0.05, two sided, calculated with the MAGeCK algorithm) in independent screens in total). Score < −0.6 is used as the cutoff of essentiality.
negative selection results from b,c. Red color labels the enzymes involved in t6A Boxes represent data within the 25th to 75th percentiles, whiskers depict the
biosynthesis. The Venn diagram shows hits overlapping in both screens. range of all data points, and horizontal lines within boxes represent median
e–i, Gene rank of tRNA modification genes in genome-wide CRISPR knockout values. l, Heatmap showing z-transformed BF scores of YRDC in genome-wide
screens of five GSCs. More positive BF scores indicate higher confidence of CRISPR knockout screens of five carcinoma cell lines and one non-transformed
essentiality. Top hits and YRDC are highlighted. j, Gene rank plot showing epithelial cell line.
Nature Cancer
Article https://doi.org/10.1038/s43018-024-00748-7
amino acid levels mainly through mTOR complex 1 (mTORC1)-mediated mTOR and eIF2α phosphorylation levels did not change (Fig. 4f). As
signaling28 and the general control nonderepressible 2 (GCN2)– arginine has been reported to activate mTOR activity29,30, we included
eIF2α-mediated ISR pathway27. Upon threonine supplementation, arginine as a control. Arginine supplementation increased puromycin
a
Nature Cancer
knar
eneg
noitceles
evitageN
d
Significant hit
GSC456 GSC23
1 YRDC YRDC
2 TRMT61A NFS1
3 DALRD3 TPRKB
4 KTI12 CIAO1
5 TRMO THUMPD2
6 NUBP1 RPUSD2
7 RPUSD2 PRORP
8 ADAT3 TRMT12
9 ISCU GON7
10 HSD17B10
11 TP53RK
12 PUSL1
7 2 10
YRDC
RPUSD2
b c
GSC456
0
–5 DALRD3 TRMT61A
–10 YRDC
–15
0 100 200 300 400
Rank
evitagen(
gol 01
)erocs
ARR
GSC23
0
–5 TPRKB
NFS1
–10 YRDC
–15
0 100 200 300 400
Rank
evitagen(
gol 01
)erocs
ARR
G523_L
30
20
10
0
–10
–20
erocs
FB
e
ELP5
YRDC
Rank
G532_L
100
50
0
–50
erocs
FB
G691_L
40
ELP5
20
YRDC
0
Rank
–20
–40
erocs
FB
G620_L
30 TRMT5
YRDC
20
Rank
10
0
–10
erocs
FB
f g h
KTI12
YRDC
Rank
GSCs vs. NSCs
6
4
2
0 Rank –2
–4
FBq
erocs
Z
)CSN–CSG(
ffiD
BT67_L
60 TRMT5
40 YRDC
20
0 –20
–40
erocs
FB
tRNA modification
sgRNA library
(1,310 gRNAs) Selection
Infection
Propagation
GSCs
Day –5 Day 1 Day 14
gDNA extraction and
sequencing
i j l
Carcinoma lines
Non-transformed epithelial cell ELP5
YRDC
2
Rank YRDC − 0 1 1 B (Z F s s c c o o r r e e ) HT H 29 CT116 DL D H 1 P AFII HeLa RPE1 −2
k
1.0
0
–1.0
–2.0
–3.0
erocs
sonorhC
–0.6 Essential
0
–5
–10
–15
0 100200300400
Rank
YRDC dependency in DepMap
n = 1
n = 8 n = 6 n = 8 n = 13 n = 31 n = 31 n = 4 n 1 = 67 n = 11 n = 4 n 7 = 16 n = 58 n = 3 n 4 = 32 n = 9 n = 35 n = 6 n 9 = 29 n = 58 n = 2 n 2 = 13 n 3 = 37 n = 2 n 1 = 34 n = 5 n 8 = 47 n = 9 n = 15 n = 2 n 8 = 69
Non- B c i a le n c d e u r B c o l t u a c s d a d n e c r e B c r a o n n c e O e c r t a h n e c r e G b r r li a o in m B C c r a o e a E l a C n o n s c n e d t e r / o c v c r a m i o c n l e a o c t l r e r c e i r a a c l n t / a u c l E t e e c s r r o a i n p n c e h e a c r g a e n a c G l e c a r a E ll n y b c e la e c d r H a d n e e G c a r e a d c r s a a t n r n i c c d e c n r a e n c c K k e id c r a n n e c y e c r an L c e e u L r i k p e o m sa ia L rc iv o e m r L c a u a n n g ce c r a L n y m ce p r ho N M m e y u a e r l o o O b m l v a P a a s a r t i n o a c m n r c e a a a P n ti r c c o e c s r t a a n t c e e c r an R c h e a r bd S o a id r S c k o in m c a an T T c e h e r y r a r t o o id m c a ancer
)erocs
ARR(
gol 01
YRDC
gRNA counting and
MAGeCK analysis
Article https://doi.org/10.1038/s43018-024-00748-7
a b d
e
c
f i
Nature Cancer
ytilibaiv
llec
evitaleR
6 shNT
shYRDC.1 4 shYRDC.2
2
0
0 2 4 6
Time (d)
GSC456
0
−1 −2 shNT
shYRDC.1
−3 shYRDC.2
0 20 40 60 80100
Number of cells
fo
noitcarf
goL
gnidnopsernon
6 shNT
shYRDC.1 4 shYRDC.2
2
0
0 2 4 6
Time (d)
ytilibaiv
llec
evitaleR
GSC468
0
−1 −2 shNT
shYRDC.1
−3 shYRDC.2
0 20 40 60 80100
Number of cells
fo
noitcarf
goL
gnidnopsernon
g h
8 shNT
shYRDC.1 6 shYRDC.2 4
2
0
0 2 4 6
Time (d)
j k l m
n p
ytilibaiv
llec
evitaleR
GSC23
0
−1 −2 shNT
−3 shYRDC.1
shYRDC.2
−4
0 20 40 60 80100
Number of cells
fo
noitcarf
goL
gnidnopsernon
o
)%(
evitisop
UdE
40 20
30 15 20 10
10 5
0 0
)%(
evitisop
UdE
)%(
evitisop
UdE
GSC456 GSC468 GSC23
P = 0.0002 P < 0.0001 20 P = 0.0004 P < 0.0001
15 10
5
0
2.5
2.0 1.5 1.0
0.5
0
erehps
evitaleR ezis
2.5
2.0 1.5 1.0
0.5
0
erehps
evitaleR ezis
2.0
1.5 1.0
0.5
0
erehps
evitaleR ezis
4 GBM (n = 166) 2 Normal (n = 293)
0
−2 −4
METTL1 TRMT2B THADA
QTRT2
C9orf64
BCDIN3D
METTL2A
GON7
CDKAL1
PRORP
THG1L HSD17B10 KTI12
NUBP1
YRDC
LCMT2
TP53RK
GSC456 GSC468 GSC23
P < 0.0001 P < 0.0001 P < 0.0001 P < 0.0001 P < 0.0001 P < 0.0001
s s h h Y
N
R s
T
h D Y
C
R
.1
D
C.2
s s h h Y
N
R
T
s D hY
C
R
.1
D
C.2
s s h h Y
N
R s
T
h D Y
C
R
.
D
1 C.2
GSC456 GSC468 GSC23
P < 0.0001 P < 0.0001 P < 0.0001 P < 0.0001 P < 0.0001 P < 0.0001
P = 0.0019 P = 0.0340 P < 0.0001 P = 0.0006 P = 0.0321 P < 0.0001
s s h h Y
N
R s
T
D hY
C
R
.1
D
C.2
s s h h Y
N
R s
T
h D Y
C
R
.1
D
C.2
s s h h Y
N
R s
T
D hY
C
R
.1
D
C.2
erocs
Z
GSCs vs. DGCs
3 2
1 0
1 2 3 4 5 –1
–2 –3 –log 10 (FDR)
)CF(
gol 2
PUS7 YRDC
Up in GSCs 17 2 15 Up in GBM
(19) (17)
Co-upregulated
YRDC
HSD17B10
4
3
2
1
0
sh
NT
shYR D
C.2
ANRt
gµ/gn
t6A
1.5 P = 0.0001
1.0
0.5
0
sh
NT
shYR D
C.2
slevel
ANRm
evitaleR
t6A YRDC
P < 0.0001
NT C.1
sh shYR D
ANRt
gµ/gn
1.5 P < 0.0001
1.0
0.5
0
NT C.1
sh shYR D
slevel
ANRm
evitaleR
456 468 23 RKI 3028 387
GSCs + – + – + – + – + – + – DGCs – + – + – + – + – + – + kDa
35 YRDC 25
GFAP 55
40 OLIG2
Tubulin 55
NSCs GSCs
N S C11 H N P1 R KI 4 5 6 4 6 8 2 33 02 8 3 87 kDa
35
YRDC
25
Tubulin 55
YRDC
4 P = 0.0029
3
2
1
0
nicymoruP
)sisehtnys
nietorp(
P = 0.0004 P = 0.0005
GSC456 GSC468 GSC23
siNT + – – – + – – – + – – –
siYRDC.1 – + – – – + – – – + – –
siYRDC.2 – – + – – – + – – – + – siYRDC.3 – – – + – – – + – – – + kDa
180
15
35
YRDC 25
Tubulin 55
Fig. 3 | YRDC is essential for GSC maintenance and translation. a, Volcano plot (shRNA). j–m, Extreme limiting dilution assay (j–l) and quantification of sphere
showing differentially expressed tRNA modification enzymes (cutoff, |log (fold formation (m) (GSC456, n = 51 (shNT), 52 (shYRDC.1), 50 (shYRDC.2); GSC468,
2
change (FC))| > 0.8, false discovery rate (FDR) < 0.05) in RNA-seq data of GSCs n = 51 (shNT), 51 (shYRDC.1), 56 (shYRDC.2); GSC23, n = 53 (shNT), 34 (shYRDC.1),
versus DGCs (GSE54791). Red dots indicate upregulation, and blue dots indicate 50 (shYRDC.2) spheres) in GSCs with or without YRDC knockdown. n,o, MS analysis
downregulation in GSCs. b, Heatmap showing expression of genes encoding tRNA of t6A levels (n, n = 3 per group; o, n = 6 in shNT and n = 5 in shYRDC.2) and qPCR
modification enzymes in RNA-seq data of TCGA_GBM and the Genotype–Tissue analysis of YRDC expression (n = 3 per group) in GSC456 cells transfected with the
Expression (GTEx) brain cortex. Upregulated genes encoding enzymes in GBM are indicated shRNA species. The number of n indicates biologically independent
labeled (cutoff, |log (fold change)| > 1, FDR < 0.05). C9orf64 is also known as QNG1. samples. p, Immunoblots showing puromycin incorporation and YRDC expression
2
c, Venn diagram showing genes encoding tRNA modification enzymes that are in GSCs transfected with the indicated small interfering RNA (siRNA) species. In
upregulated in both GBM and GSCs. d,e, Immunoblots showing YRDC, GFAP and f–i,m–o, data are presented as mean ± s.d. In d,e,p, immunoblots are
OLIG2 expression in the indicated cells. GFAP is a differentiation marker, and OLIG2 representative of three independent experiments with similar results. In i–m, data
is a stem cell marker. f–i, Cell viability (f–h, n = 4 independent experiments) and are presented from three independent experiments. Two-way ANOVA followed by
quantification of EdU incorporation (i, n = 5 randomly selected fields per group) multiple comparisons for f–h. One-way ANOVA followed by multiple comparisons
in GSCs with or without YRDC knockdown. shNT, non-targeting short hairpin RNA for i,m. Two-tailed likelihood-ratio test for j–l. Two-tailed unpaired t-test for n,o.
Article https://doi.org/10.1038/s43018-024-00748-7
a c
d
g h i
j k l
GSC456 GSC23 60
Thr (µM) 5×2×1× (80 8 0) 41× (800) 5×2×1× (80 8 0) 41× (800) 40
Ctrl medium – – + – – + – – + – – + 20 P < 0.0001
Suppl. medium + + – – – – + + – – – –
0
D T e R a m cy e l d at iu io m n – – – – – – – + – + – + – – – – – – – + – + – + NS C1 H 1 G N S P C 1 D 4 G 56 C G 4 S 5 C 6 D 4 G 6 C 8 4 G 68 S C D 23 G C23
tRNAThr
AGT
a
tR
a
N
t
A
RNA a
tR
a
N
t
A
RNA
tRNAThr CGT a tR a N t A RNA a tR a N t A RNA
tRNAThr aa tRNA aa tRNA
TGT tRNA tRNA
aa tRNA aa tRNA
Total tRNA tRNA tRNA
incorporation as well as mTOR phosphorylation, while threonine a different mechanism than arginine. Increased puromycin incorpo-
supplementation accelerated translation without affecting mTOR ration under threonine supplementation was reversed upon YRDC
phosphorylation levels (Extended Data Fig. 4a), supporting the loss (Fig. 4g,h), indicating that threonine supplementation is unable
notion that threonine abundance promotes increased translation by to promote increased translation when t6A biosynthesis is impaired.
Nature Cancer
level
rhT ralullecartnI
)nietorp
latot
gµ/lomp(
P < 0.0001
P < 0.0001
P < 0.0001
m n
t6A
ANRt
gµ/gn
4 P < 0.0001 EV
OE SDS 3 –3× Flag
2
1
0
level
rhT
evitaleR
t6A
Control medium + – –
5×T medium – + –
TR medium (4 µM) – – +
Threonine
1.5 EV
P = 0.0001
OE SDS 1.0 –3× Flag
0.5
0
ANRt
gµ/gn
+ – –
– + –
– – +
aera SM
evitaleR
L threonine Threonine tracing Adenosine
OH O YRDC 1.5 H 3 C OH CO 2 TC AMP NH 1.0 2 ATP PPi
Acceptor tRNA
stem 0.5
D arm T arm AMP
0
t6A37 KEOPS complex or OSGEPL1 Anticodon arm
A6t delebal
tnecreP
)%( )A6t latot/A6t]N51,C31[(
4
b
40 P < 0.0001 30
20
10
0 C23 C23
GS
D
G
e f
GSC456 GSC468 GSC23
Ctrl medium + – – + – – + – –
2×T medium – + – – + – – + –
5×T medium – – + – – + – – +
nicymoruP
)sisehtnys
nietorp(
GSC456 GSC23
Ctrl medium + – – – – + – – – –
TR medium – + + + + – + + + +
kDa Thr (µM)
800
8 4 2 0
800
8 4 2 0
180
15
Tubulin 55
nicymoruP
)sisehtnys
nietorp(
GSC456 GSC468 GSC23
Ctrl medium + – – + – – + – –
2×T medium – + – – + – – + –
5×T medium – – + – – + – – + kDa
kDa
p mTORS2448
180
180
mTOR
180
p eIF2αS51 40
15 eIF2α 40
Tubulin 55
Tubulin 55
GSC23
+ – + –
– + – +
+ + – –
– – + +
nicymoruP
)sisehtnys
nietorp(
P = 0.0003
4 P = 0.0017 P = 0.2574 3
2
1
0
GSC456 GSC456 GSC23
siNT + – + – Ctrl medium + – – – – + – – – –
siYRDC.1 – + – + 2.0 TR medium – + + + + – + + + + 0 0
Ctrl medium + + – – Thr (µM) 8 0 842 0 8 0 84 2 0 kDa
1.5 5×T medium – – + + kDa p mTORS2448
1.0 180
180
0.5 mTOR
180
0 p eIF2αS51 40
15 siNT + – + – + – + –
35 siYRDC.1 – + – + – + – + eIF2α 40
YRDC
25 Ctrl medium + + – – + + – –
5×T medium – – + + – – + + Tubulin 55
Tubulin 55
GSC456
EV + –
OE SDS – + –3× Flag kDa 40
Flag
40
SDS
Tubulin 55
nicymorup
evitaleR
GSC456 GSC23
P = 0.9422 P = 0.4018
2.0 P = 0.0393 P = 0.0366
1.5
1.0
0.5
0
150 nt 150 nt
150 nt 150 nt
150 nt 150 nt
150 nt 150 nt
Article https://doi.org/10.1038/s43018-024-00748-7
Fig. 4 | Threonine dynamically regulates t6A and translation. a, Graphic in two GSC samples cultured in the indicated medium for 72 h. j, Northern blot
illustration of t6A biosynthesis. Red color indicates the focus of this study. showing tRNAThr charging levels in two GSCs cultured in the indicated medium
PPi, inorganic pyrophosphate. TC-AMP, L-threonylcarbamoyladenylate. for 72 h. Deacylated tRNA runs faster than aminoacyl-tRNA (aa-tRNA). nt,
b, MS analysis of labeled t6A in [13C,15N]l-threonine tracing experiments for nucleotides. Suppl., supplementation. k, Threonine assay detecting intracellular
4
6 h (n = 4 biologically independent samples per group). c, MS analysis of t6A threonine levels in the indicated cells (n = 3 biologically independent samples
(left) and total adenosine (right) on tRNA extracted from GSC456 cells cultured per group). l–n, Immunoblots showing Flag and SDS expression (l), relative
in the indicated medium for 72 h (n = 3 biologically independent samples per intracellular threonine levels (m) and MS analysis of t6A levels (n) in GSC456 cells
group). d,e, Immunoblots showing puromycin incorporation in GSCs cultured with or without SDS–3× Flag overexpression (n = 3 independent experiments).
in the indicated medium for 72 h. Ctrl, control. f, Immunoblots showing Control medium, 800 μM threonine; 5×T medium, 4,000 μM threonine; 2×T
phosphorylated (p)-mTORS2448, mTOR, p-eIF2αS51 and eIF2α expression in three medium, 1,600 μM threonine; TR medium, threonine-restricted medium.
GSC samples cultured in the indicated medium for 72 h. g,h, Representative EV, empty vector; OE, overexpressed. In b,c,h,k,m,n, data are presented
immunoblots (g) and quantification (h, n = 3 independent experiments) of as mean ± s.d. In d–g,i,j,l, blots are representative of three independent
puromycin incorporation and YRDC expression in GSC456 and GSC23 cells experiments with similar results. Two-tailed unpaired t-test for b,m,n. One-way
with or without YRDC knockdown cultured in the indicated medium for 72 h. ANOVA followed by multiple comparisons for c,h,k.
i, Immunoblots showing p-mTORS2448, mTOR, p-eIF2αS51 and eIF2α expression
Unlike arginine, TR in general did not alter mTOR activity (Fig. 4i and quantitative proteomic analysis in patient-derived GSCs upon either
Extended Data Fig. 4b), supporting the idea that the effect of threonine YRDC deprivation or TR. GSCs cultured in control medium and
was independent of mTOR signaling. Although phosphorylation of threonine-restricted medium displayed strong differences as mapped
eIF2α was increased at threonine concentrations lower than 2 μM, TR by principal-component analysis (PCA), while targeting YRDC decreased
from 800 μM to 4 μM for 72 h in culture medium did not affect eIF2α the distances induced by TR (Fig. 5a,b), suggesting that the effect of TR
phosphorylation (Fig. 4i and Extended Data Fig. 4b), yet translation was partially diminished by YRDC loss. To explore YRDC-dependent
was reduced in this range of TR (Fig. 4e). Furthermore, we observed threonine effects, we defined differentially expressed genes (DEGs)
stable charging levels in all three detectable tRNAThr species (tRNAThr , induced by TR in cells with intact YRDC expression and then compared
AGT
tRNAThr , tRNAThr )31 over this range of threonine manipulation them to those in cells with YRDC depletion. Most TR DEGs were no
CGT TGT
(Fig. 4j), which reinforces the notion that translational effects were not longer differentially expressed compared to baseline conditions upon
mediated by alteration of tRNAThr charging and decoding. Together, targeting YRDC expression (Fig. 5c–f), indicating that these altera-
these findings suggest that threonine availability fuels translation tions were mostly dependent on YRDC. GO enrichment analysis based
through YRDC and t6A biosynthesis with limited contributions from on the YRDC-dependent downregulated genes identified pathways
nonspecific effects of threonine deficiency. mainly related to cell cycle regulation, including ‘mitotic cell cycle’,
Given the impact of threonine on GSC growth, we hypothesized ‘DNA-templated DNA replication’, ‘nuclear chromosome segregation’,
that GSCs reprogram their metabolism to augment threonine avail- ‘regulation of chromosome separation’ and ‘attachment of spindle
ability. Indeed, GSCs displayed higher levels of intracellular threonine microtubules to kinetochore’. YRDC-dependent upregulated genes
than DGCs and NSCs (Fig. 4k and Extended Data Fig. 4c), which could be were associated with cell differentiation and metabolic processes of
derived either from greater uptake or lower degradation. In mammalian multiple biomolecules, including ‘cellular nitrogen compound’, ‘metal
cells, ASCT1 (SLC1A4) and ASCT2 (SLC1A5) are the major transporters con- ion’, ‘fatty acid’ and ‘carbohydrate’ (Fig. 5g–j). Together, these results
tributing to threonine uptake32. However, neither SLC1A4 nor SLC1A5 was demonstrate that the metabolic function of threonine is mainly medi-
consistently preferentially expressed by GSCs (Extended Data Fig. 4d,e). ated through YRDC in GSCs, which facilitates cell cycle progression
Threonine is mainly catabolized through three independent pathways and involves in multiple cellular metabolic processes.
involving threonine dehydrogenase (TDH), threonine aldolase (TA) and
serine dehydratase–threonine deaminase (SDS)33. TDH is a pseudogene Threonine and YRDC fuel mitosis with ANN codon bias
in humans34, and TA has minimal enzymatic activity in mammals35, sug- Dysregulation of tRNA modifications often leads to alterations in tRNA
gesting that SDS is the major downstream catabolic enzyme in human abundance or function9. In human cytoplasm, the t6A moiety exclusively
cells (Extended Data Fig. 4f). GSCs express low SDS levels (Extended Data decorates ANN-decoding tRNA species36. To understand the role of t6A
Fig. 4g), suggesting that reduced catabolism in GSCs likely contributes for its carriers, we performed transcriptome-wide tRNA sequencing
to threonine accumulation. To test this hypothesis, we overexpressed (tRNA-seq) under YRDC knockdown or TR. Most tRNA isodecoders
the degradative enzyme SDS in GSCs, resulting in reduced intracellular remained stable (Extended Data Fig. 5a,b) without differences in the
threonine levels and impaired t6A biosynthesis (Fig. 4l–n). Together, expression levels of either ANN-decoding or non-ANN-decoding tRNA
these results support the idea that high threonine levels in GSCs are due isodecoders (Fig. 6a and Extended Data Fig. 5c), suggesting that t6A
to reduced degradation, which facilitates t6A formation. does not contribute to the stability or abundance of tRNA. We next
asked whether t6A contributed to the function of ANN-decoding tRNA in
Threonine functions mainly through YRDC in GSCs GSCs, as revealed by structural analysis37. Based on the codon specificity
To better understand the underlying mechanism, we per- of the t6A carriers, we hypothesized that t6A regulates translation not
formed matched RNA-seq and tandem mass tag (TMT)-labeled only at a global level but also in an ANN codon-biased manner. First, we
Fig. 5 | Threonine functions mainly through YRDC in GSCs. a,b, PCA analysis of Those DEGs and differentially expressed proteins from c,e that turned stable in
transcriptomic (a) and proteomic (b) data of GSC456 cells with or without YRDC d,f are defined as YRDC-dependent alterations. Cutoff, log |fold change| > 1 and
2
knockdown cultured in control or threonine-restricted (TR, 4 μM, 72 h) medium. adjusted (adj.) P < 0.05. g–j, GO enrichment analysis of biological process (GOBP)
Solid circles indicate cells with normal YRDC expression. Dashed circles indicate of YRDC-dependent downregulated and upregulated genes upon TR (4 μM, 72 h)
cells with YRDC knockdown. Dim., dimension. c–f, Volcano plot showing DEGs in transcriptomic data (g,h) and proteomic data (i,j) of GSC456 cells. IMP, inosine
and differentially expressed proteins between GSC456 cells with intact YRDC monophosphate; miRNA, microRNA; ncRNA, noncoding RNA; rRNA, ribosomal
expression cultured in control and threonine-restricted media (4 μM, 72 h) in RNA; snRNP, small nuclear ribonucleoprotein. In a,c,d,g,h, transcriptomic
transcriptomic data (c) and proteomic data (e). All genes were projected to the data are from three biologically independent samples per group. In b,e,f,i,j,
same comparison in GSC456 cells with YRDC knockdown in transcriptomic data proteomic data are from four biologically independent samples per group.
(d) and proteomic data (f), and coloring indicates the status of these genes in c,e.
Nature Cancer
Article https://doi.org/10.1038/s43018-024-00748-7
calculated ANN codon usage frequencies across the principal coding suggesting that YRDC facilitates the translation of ANN codon-enriched
sequences (CDS) annotated by APPRIS38 for each coding gene (Sup- transcripts. GO enrichment analysis of those downregulated proteins
plementary Table 6). In proteomic analysis, loss of YRDC tended to upon YRDC targeting identified top pathways specifically related to cell
decrease the quantity of proteins enriched with ANN codons (Fig. 6b), cycle progression and cell division (Extended Data Fig. 5d). Consistent
a c d
Transcriptomics
100
0
–100
–200 –100 0 100 200
Dim.1 (26.6%)
Nature Cancer
)%5.31(
2.miD
Stable (n = 12,263)
Down (n = 652) 250
TR Up (n = 1,172) 200
shNT 150
TR Ctrl Ctrl 100
shYRDC.1 50
0
–10 –5 0 5 10
log (FC)
2
)eulav
P
.jda(
gol– 01
250
200
150
100
50
0
–10 –5 0 5 10
log (FC)
2
)eulav
P
.jda(
gol– 01
shNT cell shYRDC.1 cell
TR vs. Ctrl TR vs. Ctrl
b e f
Proteomics
100
50 0
–50
–100
–100 –50 050 100
Dim.1 (45.3%)
)%8.13(
2.miD
15
Ctrl
Ctrl 10 shNT shYRDC.1 TR
TR 5
0
–6 –4 –2 0 2 4 6
log (FC)
2
)eulav
P(
gol–
01
15
10
5
0
–6 –4 –2 0 2 4 6
log (FC)
2
)eulav
P(
gol–
01
YRDC-dependent
DEGs in shNT cell
Project all genes Down (n = 471)
Label DEGs from shNT cell Up (n = 1,137)
shNT cell shYRDC.1 cell
TR vs. Ctrl Stable (n = 7,563) TR vs. Ctrl
Down (n = 89) YRDC-dependent
Up (n = 209) DEGs in shNT cell
Project all genes Down (n = 78) Label DEGs from shNT cell Up (n = 206)
g h
Transcriptomics: YRDC-dependent downregulated genes Transcriptomics: YRDC-dependent upregulated genes
DNA-directed 5 a ′ c – t 3 iv ′ i R ty NAP opsoitlyivme erreagsuel a a t c io ti n vi t o y f DNA primase c R o i m bo p n le u x c l b e i o o p g r e o n t e e s in is Cel c lu o l m ar p n o it u r n o d gen
DNA-templated Po si D tiDveN N rAe gp A uollaytm ioenr aosfe D aNcAti D -vd o it bi u ry re bec lae tke --s ditn rdanudce bdr ereapk lri N cepa e ta g ioi a rn t v i v ia e regulation of DNA ncRNA metabolic process System development metabolic process
replication Regulation of D D N N A A r u e n p w lic in ar d eti i po n ln g ic i a n t v io o n lved in DNA repl D ic N at A io - N t n e e m ga p t l i a v t e e d re D g N ul A a t r i e o p n l o ic f a tion Cell projection organization Organic subpstraoncceess biosynthetic
ncRNA processing Regulation of RNA metabolic process
Cellula R r e r g es u p la s o t t n i i o m s n e u o t lu o f s D D D N N ho A A ou mb m d l a oe e m l- t os a a D gt b r g o N o a e un l A i sd c r r e p beD c r rc o e o No c a m mA k e b s bg r s i e D i n enp o a N aa t mt A i ii o ro e r n vnt e i r R a p ic e li g c c u a h l t a a io Dn ti n gN o e n A o d r f e u p D p l N l i e c A x a - t u t i e o n m n w p in l C a d t i e e n l d g l c D y N N c D u A le c N l A D e a N r r e A D p r l N e ic A p a l t r i i c e o a p n t l i i i o D c n n a N it t i A i a o t n r i e o p n licatio a n s s p r e R re m N in b A i l t y m ia e ti t o a n b c o o lic m R i p p b r l o o e s x c o e m srs a R l N s A m p a r ll o s c u e b s u si n n i g t b R io ib g o e s n o e m si e s biogenesis Nervous syst P em las d mp N e ra v e o G e u mje l e r No e o c n pe mt g e C i mu o r eC b e a r n n e l o e r t le a n i l n o o d ls n t r n im d e eg s v i o a Cff o N b e C n f r e o e e l C p e i n d o rl uz u le e l h e p i a u nl r ff n l o uo m t l m ld e i at g rn ome i r n o e ra o eN n e d p e n n tc o r nn e i p u N t rs oo rc et u o pr h i m e n e sa o r R j h o e iu l o ts n e p lo g c i r n o g o oi g t d e n n i u d n n e n o i v ff l e e n e n o a p e n v e s t lr d r ev i t i s o o e s e el i m d jo n ns e v d e p t o c e i o inv im a t r l n f v o e i p t o n i e ol p h o o nn e l m o nvp u tm g em e r e d o o n e n n r t i A n p n e pt x s h r o i o s o ng j e e O g c nu r t e g i i d o s a n ai n sn ic c e c R yc e l g i c c uo p l T c am r r oo t a R ip mc o n e o e n s pg u s c ou o s n r ul f i d a p n n t t m di u i o o C ce mn n e lt e , oe al l o D b tf u a b N o b l b a al i A M r o i o sc e b sl t a i e - y p c i c c o n m r r o so t o p y h nc m n e l te a a t t o s t h i i sn l c e e e i d p n c ti u g r c o H l p e c e r e b t o s e i c o s r e o s s y c s n y R t c h e l N e e g t u b u ic c l io a l p e t s i o r y o o bb n n c ia t o e h o ss s e e f y p s t - c n i c r c eo to h lc p l ne ue r tt l o a s i a c s c i r n e pi b n s r i s g o o s cc y eo n sm t s h p e o ti u c n d
DNA metabolic process Small-molecule biosynthetic process
RNA capping
Anatomical structure morphogenesis
CelluMlaer taarboomliact ipcr coocmesps o
G
u
e
n
n
d
e expression
Chromosome organization Double
D
-s
N
tr
A
a n
re
d
p
b
a
r
i
e
r
ak repai D r NA m -te a m in p te la n t a e n d c D e N o A f
D
R f
N
e r id e p
A
p e l i l l
r
c i i
e
t c a y
p
a t i
l
t o
i
i
c
o n
a
n
t
f
i
o
o
r
n
k
c
p
h
ro
e
c
c
e
kp
ss
o
in
in
g
t s
A
ig
lc
n
o
a
h
li
o
n
l
g
bSiotesryon Sidt e h cbe oiton icsd yp anr r y oth c aee ltc sico s hporol mceestsabolic process Spliceosomal snRNP assembly Multicellular organism deveClopmeenltl diRffeguelatrione ofn d
R
e
e
tv
g
e
u
il
l
oa
a
p
ti
m
o
t
n
ei n
o
ot
f
a
m
l n
p
p
ur
r
lo
o
tic
c
ce
e
es
s
lsl
s
u
L
lar
i
o
p
rga
i
n
d
ism al
l ocalizat
Re
i
g
o
ublai
n
otsioynn tohfe mtica cprroomceoslesR cu
l
l
e
e
o g c u o l m at o io t n io o n f
Nuclear chromosoRme C ge e us l le l a g c tir y oe c ng l e ao tf c i o h c N ne e Nl ce el kg gc pa ya ot ct i i iv lv n e e e tp p M rsh r e r i e agi o g t g sno c u e u at e l l i a tl sa cir tn st a i c i og o ne n n sl il o t o ic f o C f y D c n c e c N e e l l l l e A l l l c c c c i y n h y y cR t c e c l e l ee c l e g e g k G r p u it 2 o l y a/ i Mt n c io t h pn s e h i c g oa k n fs p t a ce r o l a e i t i n n n lrla g s t c i n s t y i s i o g cit n l n ieo a nG lin 2 g /M phase S tero Iso l p p e b n r te i o n o yl c d s ip e p h y r o o s s c n p e h s s a s t te h bi e osy t nt i h c e c tic o P o m r r o p g t l a e e n x in i z s – a u D t b i N o u A n nit Sy C nap h t M ic o s e d t ig u n r l m a a t a l i i o ntn g n r i ao C c nf e s sc l m a l h – m ie c sm l e si l oi l c n s s i a ig l s y s n y a s n l n i a n i p g o t a ic n p C t eald i l–h c cees Cl ilo aana ldc p d vhiu l hie a a m e s sC spi m -o e i d loan la e l ns – p m m c m m e ee a n o l om l d lm l e a eb e ce d c n r um ah u t l ne l e c b ees s e r s i a l oa l n d – n S e c hv y e e c i n l as e l a i l o p l n s e organization Re M g R u e l g a e t u io la t n t i a o o f n t l o ra f n i i o s C o p n a o t t r r n i t a o n n s t p r t o a r n r t sp a or n t s C p ell o mig r ra t ti e on o n r c s g E t a x a r p u t n e s c i u z r t n a u la a t r i t e l o in n g
Re M g e u i l o a t t i s i c o e n c g e r o e l f l g c c a h y t c r io o l O e n mrogsao N nme e l g ele a t f i i v s e si C o re e n g l p l u c r l o a y c t c i e l o e Cs n M se p ol ri l t f o o cc ct ye ei c c l s ll s e c c e py l Mch l l c a iet y s o R e c t e i l c t e g r a u c p n l e r a s o l t l i c i t c o i e o y n R s n c s e o le g R f u e c p l g e h a l ua t l i ls o c ae n y t i c to o r l na e f t n P r m o as of ni i s t t c si o i o te i t i tnlv i i l c o e c np c ry e h ec l a gl l es u c e lp y a t c ht r i l aa o e sn nes o i R t f io c n N e ll c A ycle localiza L o t i i p r o g i n d a n d i r z o a p ti l o e n t I MP p m ro e c t e ab ss olic a p d l H h a o e a sm d m si h o a o e n p m s h m io e il o n m ic l v e b c i c r a e a u l n l l e e s C o e rg ll a j n u i n z c a t t i i o o n n
Mitotic cell cycle
i j
Proteomics: YRDC-dependent downregulated genes Proteomics: YRDC-dependent upregulated genes
Regulation of tissue
Nuclear Mitotic nuclear division remodeling
chromosome
segregation Bone remodeling
Mitotic spindle assembly
Regulation of checkpoint signaling
chromosome de C xa e m llu e l t a h r a r s e o s n p e o n st s i e m t u o l us miRNA transcription
separation Metapha m se it / o a t n ic ap c h e a ll s e c y t c ra le n sition of
Cellular respFonsae tto tkeyton eacid c Glu a co t ne a og b ene o sis lic Positive rCeardgiacu mulsaclet cielol prnolif eration
Positive regulation of chromosome process of miRNA
separation Chromosome separation Regulation of mitotic nuclear division transcription
Positive reg s u e la g t r i e o g n a o ti f o c n hromosome Mitotic ce s ll i g c n y a c l l i e n g checkpoint Fatty acid oxidation
Cell–cell adhesion
Positive reg c u o l n a d ti e o n n s o a f t i c o h n romosome Negative regulation mediator activity c R y e c g la u s l e a t a io ct n i v o it f y
Mitotic chromosome condensation Mitotic sister chromatid separation of biomineral tissue Cellular
Chromo i s n o m m e e i o o t r i g c a c n e iz ll a c ti y o c n l e in volved m A i t c t r a o s c p t h u i m n b d u e l l n e e t s o t f o tr u a b n R s i e q f g e u u r it a l i a s n t e i p o a r n c o t o t i e v f i i n ty development Telen m ce ig p r h a a ti l o o n n cell c b a i r o p b s r o y o h n c y t e h d s e r s a ti t c e
kinetochore
Article https://doi.org/10.1038/s43018-024-00748-7
with YRDC-knockdown effects, we observed that the downregulated loss were also enriched with cell cycle regulation pathways (Extended
proteins in TR tended to possess higher ANN codon frequencies, Data Fig. 7c,d), further supporting the role of t6A in cell cycle regulation.
although the difference was not statistically significant (P = 0.0797) During translation, tRNA pairs with three binding sites within the ribo-
(Extended Data Fig. 5e). Overlap of YRDC-knockdown and TR effects some, specifically, the A site (aminoacyl), the P site (peptidyl) and the E
identified 18 co-downregulated proteins enriched with ANN codons site (exit), with enrichment of ribosome footprints at the A site indicat-
(Fig. 6c,d), which were related to mitotic cell cycle regulation in GO ing longer ribosome dwell time and ribosome stalling. To investigate
enrichment analysis (Fig. 6e). GO enrichment analysis of the downregu- ribosome stalling events, we leveraged the CONCUR pipeline43 to infer
lated proteins exclusively associated with YRDC knockdown identified the ribosome A site codon occupancy for each codon. YRDC loss and
the ‘cerebral cortex cell migration’ pathway. By contrast, the down- TR showed a similar distribution of ANN codon occupancy at the A site
regulated proteins exclusively associated with TR were enriched with (based on the correlation coefficient and significant P value in Fig. 6j).
proteins encoded by mitosis-related genes, indicating the complexity of We further observed that five ANN codons were increased under both
TR in cell cycle regulation (Extended Data Fig. 5f). Together, threonine YRDC loss and TR (AAA, AGT, ATG, AGG and AGC) (Fig. 6j), suggesting
and YRDC fuel the translation of cell cycle-related transcripts in an ANN that inhibition of t6A biosynthesis and threonine limitation both result
codon-dependent manner, which was consistent with increased G0/ in similar patterns of ribosome stalling. By contrast, this pattern of
G1 phase and decreased S/M phases under YRDC deprivation and TR codon stalling was completely lost at the A + 1 site (Fig. 6k). YRDC loss
(Extended Data Fig. 5g,h). and TR were more likely to affect frequently used ANN codons in human
By combined analysis of matched proteomic and transcriptomic CDS (Fig. 6l,m). Amino acid deprivation leads to ribosome stalling at
data, we observed that nine of the 18 co-downregulated proteins were specific codons encoding related amino acids44,45. We observed no ribo-
unchanged at the RNA level upon YRDC targeting (Fig. 6f), indicating some stalling at threonine codons under TR (4 μM at 72 h) (Fig. 6m),
that their protein levels were likely regulated by translational buffering. which is consistent with the minimal alteration of tRNAThr charging lev-
The majority of these genes (six of nine) harbor ANN codon frequencies els (Fig. 4j) and further supports the idea that ribosome stalling under
greater than the 75th percentile across the whole human CDS (Fig. 6g). threonine limitation was mediated by t6A instead of impaired tRNAThr
These six targets decreased at the protein level upon YRDC loss or TR charging and decoding. At the protein level, downregulated proteins
(Fig. 6h,i), while alterations at the RNA level were minimal (Extended under YRDC targeting and TR were enriched with the overlapping
Data Fig. 5i,j). Collectively, we identified six proteins as the most promi- stalled ANN codons (Fig. 6n,p), and the six t6A downstream targets also
nent translational targets of t6A in GSCs: SPC25 component of NDC80 exhibited high levels of overlapping ANN codon frequencies (Fig. 6q).
kinetochore complex (SPC25), microtubule-associated serine–threo- By contrast, although we identified 21 overlapping non-ANN codons
nine kinase like (MASTL), Rac GTPase-activating protein 1 (RACGAP1), stalled under both conditions (Extended Data Fig. 7e), they were not
cellular inhibitor of PP2A (CIP2A), centrosomal protein 55 (CEP55) and enriched in the differentially expressed proteins of proteomic data
non-SMC condensin I complex subunit G (NCAPG). In published screen (Extended Data Fig. 7f–h). Additionally, the previously identified t6A
datasets16,20,21,39, SPC25, MASTL, RACGAP1 and NCAPG were essential in downstream targets possessed low frequencies of these overlapping
both GSCs and GBM generally, with CIP2A essential in a subset of GSCs non-ANN codons (Extended Data Fig. 7i), suggesting that the effects
and variable dependencies of CEP55 in different screens (Extended Data on non-ANN codons are nonspecific to YRDC- and threonine-mediated
Fig. 6a). In clinical datasets, the protein abundance of these targets t6A function. Collectively, these findings reveal the function of t6A at
positively correlated with YRDC protein abundance and with each a single-codon resolution, providing a better understanding of the
other in the Proteomic Data Commons (PDC) GBM cohort40 (Extended interplay between threonine, t6A and their requirement for decoding
Data Fig. 6b,c). High expression levels of these targets were associated specific ANN codons.
with higher glioma grade in the Cancer Genome Atlas (TCGA) and CGGA We next developed two synonymous reporters with different
datasets (Extended Data Fig. 6d,e). Together, these results indicate the ANN codon frequencies in one of our target genes, SPC25 (that is, ANN
requirement of the t6A downstream targets in GSCs and GBM. hi-SPC25 and ANN lo-SPC25). These sequences were placed upstream
To gain deeper insight into the regulation of t6A at a single-codon of that for luciferase, followed by the sequence for internal ribosome
resolution, we performed ribosome profiling41 of GSCs with YRDC entry site (IRES)-driven Renilla luciferase as an internal control (Fig. 6r).
targeting or TR. The isolated ribosome footprints were about 30 Despite achieving similar levels of YRDC knockdown, the translation
nucleotides in length (Extended Data Fig. 7a) and showed a strong of ANN hi-SPC25 was more sensitive to YRDC loss that that of ANN
three-nucleotide periodicity on the CDS frame (Extended Data Fig. 7b), lo-SPC25, as measured by lower luciferase activity (Fig. 6s) with com-
which is consistent with the characteristics of ribosome profiling data42. parable transcript expression (Extended Data Fig. 7j). Similarly, the
The transcripts with downregulated translation efficiency upon YRDC translation of ANN hi-SPC25 was more sensitive to TR than that of ANN
Fig. 6 | Threonine and YRDC fuel mitosis with ANN codon bias. a, Expression of regression. Ribosome profiling data are from two biologically independent
ANN-decoding and non-ANN-decoding tRNA isodecoders in tRNA-seq of GSC456 samples per group. l,m, Codon frequencies of each ANN codon in humans.
cells upon YRDC knockdown. Data are from three biologically independent Coloring indicates the stalling status of ANN codons in j. n–p, Overlapping ANN
samples per group. CPM, counts per million. b–d, ANN codon frequencies codon frequencies of differentially expressed proteins in proteomics of GSC456
of differentially expressed proteins (b), Venn diagram of downregulated cells with the indicated treatments. q, Distribution of overlapping ANN codon
proteins (c) and ANN codon frequencies of overlapping differentially expressed frequencies in CDS. Orange dots indicate six t6A targets. r, Graphic illustration of
proteins (d) in proteomics of GSC456 cells with the indicated treatments. two synonymous reporters. MSCV, murine embryonic stem cell virus promoter.
e, GO enrichment of co-downregulated proteins from c. KD, knockdown; GOCC, Luc, luciferase; Rluc, Renilla luciferase. s,t, Luciferase activities of the indicated
GO cellular component. f, Comparison of transcriptomics and proteomics reporters and qPCR analysis of YRDC in 293T cells with the indicated treatments
upon YRDC knockdown in GSC456 cells. Colored dots indicate translational (n = 3 independent experiments). Data are presented as mean ± s.d. In a,b,d,n–p,
dysregulation. Orange labels nine of 18 co-downregulated proteins that are boxes represent data within the 25th to 75th percentiles, whiskers depict the
downregulated at the translation level. g, Distribution of ANN codon frequencies range of all data points, and horizontal lines within boxes represent median
in CDS. Orange dots indicate the nine proteins from f. h,i, Representative values. In b–d,f,n–p, proteomic data are from four biologically independent
immunoblots from three independent experiments showing t6A targets in GSCs samples per group. In f, transcriptomic data are from three biologically
with the indicated treatments. j,k, Correlations between ANN codon occupancy independent samples per group. Two-tailed unpaired t-test for a,s,t. Two-tailed
alteration upon YRDC knockdown and TR at the ribosome A site (j) and the A + 1 Mann–Whitney test for b,d,n–p. Over-representation test corrected by FDR for e.
site (k). Red dots show overlapping stalled codons. The black line shows linear Two-tailed Pearson correlation for j,k.
Nature Cancer
Article https://doi.org/10.1038/s43018-024-00748-7
lo-SPC25 (Fig. 6t and Extended Data Fig. 7k). These results further sup- Dietary TR inhibits tumor growth
port the notion that threonine and YRDC regulate ANN codon-biased We next asked whether YRDC expression and threonine abundance
translation and that one possible advantage of upregulating YRDC in promote tumor growth in vivo. Targeting YRDC in patient-derived xeno-
GSCs is to facilitate the synthesis of ANN-rich genes that promote cell grafts resulted in reduced tumor growth (Fig. 7a,b and Extended Data
cycle progression. Fig. 8a–e), which translated into prolonged survival of tumor-bearing
Nature Cancer
)CF(
gol
ANR
2
a b c d
e f
shYRDC.1 vs. shNT
Down at translation level (n = 48)
Up at translation level (n = 32)
SPC25
MASTL RACGAP1
CIP2A CEP55
NCAPG
SPAG5
IQGAP3
SLC35C2
g
Protein log (FC) 2
i
ycneuqerf
nodoc
NNA
j
A + 1 site
ANN codon occupancy (n = 16)
0.2
P = 0.3500
0.1
0 AGTAA A G ACAGG
All principal CDS A A T G G C AAA
ATC
h –0.1
–0.2
–0.10–0.05 0 0.05 0.10
log (TR/NT) 2
)TN/DK
CDRY(
gol 2
A site
ANN codon occupancy (n = 16)
0.2
R = 0.6471
P = 0.0067 AAA
0.1 AGT
AGG ATC ATG AGC 0
AAG
–0.1
AAC
–0.2
–0.10–0.05 0 0.05 0.10
)TN/DK
CDRY(
gol 2
log (TR/NT) 2
1.5 1.0
0.5
0
evitaleR culR/cuL
Overlapping for YRDC KD + TR: downregulated proteins
GOBP GOCC
Mitotic cell cycle Condensed chromosome, centromeric region
Mitotic cell cycle process Chromosome, centromeric region
Cell cycle process Condensed chromosome Cell division Kinetochore
Nuclear chromosome segregation Chromosomal region Mitotic sister chromatid segregation Spindle
Cell cycle Mitotic checkpoint complex
Sister chromatid segregation Microtubule cytoskeleton
0 5 10 15 0 2 4 6 810
–log (P value) –log (P value) 10 10
k
l m
0.5
0.4
0.3
SPC25 0.2 MASTL
RACG C A E P P 1 55 75th percentile
0.1 NCAPG CIP2A
0
All principal CDS
Luciferase activity
ANN hi-SPC25 + + – –
ANN lo-SPC25 – – + +
Ctrl medium + – + –
TR medium – + – +
NNA
gnippalrevO
ycneuqerf
nodoc
p q
1.5 1.0
0.5
0
evitaleR culR/cuL
Luciferase activity
1.5 1.0
0.5
0
ANN hi-SPC25 + + – –
ANN lo-SPC25 – – + +
shNT + – + –
shYRDC.1 – + – +
evitaleR slevel
CDRY
0.04
0.03
0.02
0.01
0
r s t
YRDC-KD efficiency
ANN hi-SPC25 Luc Rluc
MSCV IRES
(ANN, 0.413%; overlapping ANN, 0.187%)
ANN lo-SPC25 Luc Rluc
++ ––
MSCV IRES –– ++
(ANN, 0.307%; overlapping ANN, 0.093%) +– +–
–+ –+
ycneuqerf
nodoC
Threonine codons
0.04
0.03
0.02
0.01
0
ycneuqerf
nodoC
)syL(
GAA
)syL(
AAA
)teM(
GTA
)elI(
CTA
)reS(
CGA
)nsA(
CAA
)rhT(
CCA
)nsA(
TAA
)elI(
TTA
)rhT(
ACA
)rhT(
TCA
)reS(
TGA
)grA(
AGA
)grA(
GGA
)elI(
ATA
)rhT(
GCA
Overlapping stalled codons Overlapping stalled codons
Stalled codon in YRDC KD/NT Stalled codons in TR/NT
)syL(
GAA
)syL(
AAA
)teM(
GTA
)elI(
CTA
)reS(
CGA
)nsA(
CAA
)rhT(
CCA
)nsA(
TAA
)elI(
TTA
)rhT(
ACA
)rhT(
TCA
)reS(
TGA
)grA(
AGA
)grA(
GGA
)elI(
ATA
)rhT(
GCA
Only down in KD 18 overlapping proteins SPC25 MAD2L1
YRDC KD 57 TTK EIF4EBP3 MASTL UBE2C 18 RACGAP1 BUB1B
TR 71 C PB IP K 2A S S C PA D G5
CEP55 CKS1B NCAPG IQGAP3 Only down in TR KIF2C SLC35C2
P = 0.0007 P < 0.0001
P < 0.00 P 0 = 1 0.0047 P = 0.0 P 16 = 9 0.0025 P < 0.00 P 0 = 1 0.0008
ycneuqerf
nodoc
NNA
Proteomics
shYRDC.1 vs. shNT
20 15 0.5 P = 0.0450
0.4 10 0.3
5 0.2
0 0.1 0
DownUp
)1 +
MPC(
gol 2
tRNA-seq
ANN Non-ANN
shNT + – + –
shYRDC.1 – + – +
scimoetorP
0.4
0.3
0.2
0.1 0
DownUp
ycneuqerf
nodoc
NNA
Proteomics
Overlapping for YRDC KD & TR
P = 0.3214 P = 0.0224 P = 0.9064
GSC456 GSC468
shNT + – – + – – GSC456GSC468
shYRDC.1 – + – – + – Ctrl medium + – + –
shYRDC.2 – – + – – + kDa TR medium – + – + kDa
SPC25 25 SPC25 25
MASTL 1 1 3 0 0 0 MASTL 130
100
RACGAP1
70 RACGAP1
70
CIP2A 100
CIP2A 100
CEP55 55
CEP55 55
NCAPG 130 NCAPG 130
YRDC 35
25 Actin 40
Tubulin 55
n
YRDC-KD effect
shYRDC.1 vs. shNT
P = 0.4949
NNA
gnippalrevO
ycneuqerf
nodoc
o
TR effect
TR vs. Ctrl medium
0.20 P = 0.0153
0.15
0.10
0.05
0
DownUp
NNA
gnippalrevO
ycneuqerf
nodoc
0.20 P = 0.0146
0.15
0.10
0.05
0
DownUp
NNA
gnippalrevO
ycneuqerf
nodoc
n = 18
n = 68 n = 130 n = 74 n = 16 n = 99
8
4
0
–4
–8
–8 –4 0 4 8
0.8
0.6 SPC25
MASTL RACGAP1
CIP2A 0.4 CEP55 75th percentile
NCAPG
0.2 SPAG5 IQGAP3
SLC35C2 0
Overlapping for YRDC KD + TR
0.20 P = 0.0113
0.15
0.10
0.05
n = 74n = 99 n = 89 n = 206 0 n = 18 n = 16
DownUp
Article https://doi.org/10.1038/s43018-024-00748-7
a b c
GSC468
4,000
3,000 2,000
1,000 0 Time (d)
mice (Fig. 7c). Analysis of tumor-bearing brains revealed that loss of the downstream enzymes involved in t6A biosynthesis are not cur-
YRDC diminished tumor cell mitosis (Extended Data Fig. 8f–i). These rently available. We therefore asked whether TR could be an alterna-
results support the development of agents targeting t6A biosynthesis tive approach to target t6A and tumor growth. Strict TR in vitro with
in GBM treatment. However, inhibitors directly targeting YRDC or 2 μM threonine in the medium inhibited proliferation of GSCs and
Nature Cancer
)s/p
401×(xulf
latoT
GSC456 GSC468
P = 0.0309
shNT shNT shNT shYRDC.1 shYRDC.1
shYRDC.1
3
s
7
hYR
1
D
4
C.
P P
2
< < 0 0 2 . . 4 0 0 0 0 0 0 3 1 1 0 Pr o b a bilit y
of
s ur vi v
al
10
50
0
0 0
sh
2
Y
0
RDC
4
.2
0 P
P
= 6
=
0 0 .
0
0
.
0
0
6
0
8 1
6
0
1
Pr o b a bilit y
of
s ur vi v
al
10
50
0
0 0
s
1
h
0
YRD
20
C.2
P
P 3
=
0 =
0
0
.
.
0
0 4
0
0 0
1
1
9
9 50
Time (d) Time (d)
d e
250 200 150 100 50 0
Ctrl
die
T
t
R
diet xulf latoT )s/p 501×(
GSCs DGCs GSCs DGCs GSCs DGCs Non-malignant
2.5 P = 0.0220 2.0 1.5 1.0 0.5
0
ytilibaiv llec evitaleR 0394 Control P = 0 P . 0 = 1 4 0 6 . 0 0 01 P = 0. P 0 0 = 2 0 8 . 0 0 07 P = 0. 0333 P = 0 P . 0 = 0 0 1 . 8 0 0 02 P = 0. T T R R ( ( P 4 2 = 0 . 0 µ µ 0 0 M M 4 ) )
GS
C456
D G
C456
GS
C468
D G
C468
GS
C23
D G
C23
N
M176
N
M177 Astrocytes
NS
C11
i j
GSC468
100
50
0
0 10 20 30 40
Time (d)
fo
ytilibaborP lavivrus
GSC456
100
50
0
0 10 20 30 40
Time (d)
fo
ytilibaborP lavivrus
Control diet Control diet
TR diet TR diet
P = 0.0035 P = 0.0023
slevel
A6t
evitaleR
GSC456
1.5 P = 0.0260 1.5 P = 0.0505
1.0 1.0
0.5 0.5
0 0
Ctrl
diet
TR
diet
slevel
A6t
evitaleR
f g h
GSC468
Ctrl
diet
TR
diet
xulf
latoT
)s/p
501×(
200
P = 0.0083 GSC468
150
100 Control diet TR diet
50
0
Ctrl
die
T
t
R
diet
k
2.0
1.5
1.0
0.5
0
IFM
PPO
evitaleR
GSC456 P = 0.0216
Ctrl
diet
TR
diet
2.0
1.5
1.0
0.5
0
IFM PPO
evitaleR
Isotype Control diet TR diet hCD147+ hCD147+
tumor cells tumor cells
hCD147–FITC
GSC468
P = 0.0417
Ctrl
diet
TR
diet
654CSG
746
roulF
axelA–PPO
Isotype Control diet TR diet
hCD147–FITC
746 roulF
axelA–PPO
hCD147+ hCD147+ tumor cells tumor cells 864CSG
ladoM
TR diet Ctrl diet 100
80
60
40
20
0
ladoM
200
150
100
50
0 s s h h N Y T R s D h C Y . R 1 D C.2
l m
TR diet Ctrl diet
100 80
60
40
20
0
OPP–Alexa Fluor 647
)s/p
401×(
xulf
latoT
GSC456
4 × 104 P = 0.0453
shNT
4.5 × 103 shYRDC.1 (p/s
/c/m2/sr)
P > 0.9999 shYRDC.2
GSC456 1 × 106 Ctrl diet TR diet 2 × 104
(p/s
/c/m2/sr)
GSC468 GSC456
1 × 106
Control diet TR diet Ctrl diet
TR diet 2 × 104
(p/s
/c/m2/sr)
106 0 0.017 106 5.81 74.8 106 1.32 31 105 105 105
104 104 104
103 103 103
102 102 102
101 101 101
100 100 0.008 100 13.4 6.4 100 5.75 62
100101102103104105106 100101102103104105106 100101102103104105106 100101102103104105106
OPP–Alexa Fluor 647
106
0 0
106
2.05 66.9
106
0.67 13.0 105 105 105 104 104 104
103 103 103
102 102 102
101 101 101
100 100 0.008 100 12.6 18.5 100 10.3 76.0
100101102103104105106 100101102103104105106 100101102103104105106 100101102103104105106
Article https://doi.org/10.1038/s43018-024-00748-7
Fig. 7 | Dietary TR inhibits tumor growth. a, Representative in vivo 1 mm) of tumor-bearing mice fed the indicated diets. Data were acquired on day
bioluminescence imaging (left) and quantification (right, n = 6 mice per group) 21. i, Kaplan–Meier survival curves of tumor-bearing mice fed the indicated diet
of mice bearing the indicated xenografts. Images were acquired when the first (n = 5 mice per group). j, MS analysis of tissue t6A levels of xenografts with the
neurological sign occurred in any cohort. Scale bar, 1 cm. b, Tumor growth curve indicated dietary treatment (GSC456, n = 9 mice on the control diet and n = 8
from in vivo bioluminescence analysis of mice bearing the indicated xenografts mice on the TR diet; GSC468, n = 8 mice per group). k–m, Gating strategy (k),
(n = 5 mice per group). Data are presented as mean ± s.e.m. c, Kaplan–Meier representative histogram plot (l) and statistical quantification (m) (GSC456, n = 5
survival curves of mice bearing the indicated xenografts (n = 6 mice per group mice on the control diet and n = 4 mice on the TR diet; GSC468, n = 4 mice per
for GSC456 cells and n = 5 mice per group for GSC468 cells). d, Cell viability of group) of in vivo OPP flow cytometric analysis of tumor cells from tumor-bearing
the indicated cells cultured in control or TR medium for 72 h. Data are from four mice fed the indicated diet. MFI, median fluorescence intensity. In a,d–f,j,m, data
independent experiments. e–h, Representative in vivo bioluminescence imaging are presented as mean ± s.d. One-way ANOVA followed by multiple comparisons
and quantification (e,f, n = 5 mice per group; scale bars, 1 cm) and representative for a. Two-way ANOVA followed by multiple comparisons for b,d. Log-rank test
images of hematoxylin and eosin (H&E)-stained brain sections (g,h; scale bars, for c,i. Two-tailed unpaired t-test for e,f,j,m.
NSCs, but TR at slightly less restriction (4 μM) substantially reduced Fig. 9n). To further understand the interplay between threonine and
cell viability of GSCs with minimal effects on matched DGCs and other YRDC in vivo, we performed dietary TR with or without targeting YRDC
non-malignant cells (Fig. 7d), demonstrating that threonine and t6A expression in xenografts, revealing suppressed protein synthesis in
availability are especially limiting in GSCs. tumors with loss of YRDC expression (Extended Data Fig. 9o–q). Upon
Next, we investigated the safety and efficacy of dietary TR in vivo. YRDC loss, dietary TR only slightly decreased the fraction of OPPhi cells
According to the minimal requirement of dietary threonine (about and had no further effect on the median fluorescence intensity of the
0.18%, wt/wt) for rat maintenance46, we fed mice either a control diet OPP signal (Extended Data Fig. 9p,q). Collectively, these data sug-
(0.82% threonine, wt/wt) or a TR diet (0.2% threonine, wt/wt) and gest that dietary TR functions mostly through YRDC and limitation of
monitored body weight. We did not observe significant weight loss threonine impairs protein translation and proliferation of GSCs in vivo.
in mice fed the TR diet (Extended Data Fig. 9a), despite 50% reduction
of serum threonine concentrations within 3 d, which was maintained Dietary intervention potentiates standard therapeutics
(Extended Data Fig. 9b). The TR diet did not cause significant weight We next asked whether dietary TR could improve outcomes in combina-
loss or pathological abnormalities in any organ examined, including tion with standard treatment modalities. To better mimic the clinical
the brain, liver, heart, spleen, lung and kidney (Extended Data Fig. 9c,d). use of the TR diet, we initiated dietary intervention and drug treat-
As multiple similarities are shared between GSCs and NSCs3, we asked ment 7 d after GSC implantation (Fig. 8a). GSCs display therapeutic
whether the TR diet was toxic to NSCs. In adult mammalian brains, resistance, including to chemotherapy49. Temozolomide, the standard
ventricular–subventricular zone GFAP+ astrocytes have been charac- first-line chemotherapeutic drug, only modestly improved the survival
terized as the largest NSC population47, which give rise to intermedi- of GSC-bearing mice as a monotherapy, but combining temozolomide
ate progenitors and DCX+ neuroblasts in neurogenesis48. Dietary TR with dietary TR provided combinatorial benefit with longer survival
did not alter the numbers of ventricular–subventricular zone GFAP+ in vivo (Fig. 8b,c and Extended Data Fig. 10a). As no YRDC inhibitors
cells (NSCs) (Extended Data Fig. 9e–g). The numbers of DCX+ cells have been developed, we interrogated drug sensitivity data from the
(neuroblasts) remained unchanged (Extended Data Fig. 9h,i), indicat- Cancer Therapeutics Response Portal (version 2)50 and gene expression
ing that the neurogenic function of NSCs was intact. Together, these data from the Cancer Cell Line Encyclopedia51 to identify compounds
results demonstrate the negligible toxicity of dietary TR on NSCs and for which efficacy tracked with YRDC expression. High YRDC expression
different tissues. in cancer cell lines correlated with high sensitivity to an H3K27 trimeth-
To determine the value of dietary TR as a therapeutic approach, ylation (H3K27me3) demethylase inhibitor (GSK-J4) and CDK inhibitors
we initiated either a TR diet or maintained a control diet for 7 d before (BRD-K30748066, dinaciclib and alvocidib) (Fig. 8d). Although the CDK
GSC implantation intracranially and then maintained diets throughout inhibitor alvocidib is no longer under active clinical development, we
the study. Tumor-bearing mice fed the TR diet showed reduced tumor previously demonstrated that it is an active agent against GSCs52. We
volume and extension of survival (Fig. 7e–i). Consistent with in vitro thus sought to investigate the potential combinatorial benefit with
effects, TR in vivo suppressed t6A formation (Fig. 7j), inhibited tumor TR and observed that dietary TR potentiated the efficacy of alvocidib
protein synthesis (Fig. 7k–m) and reduced tumor cell cycle progression and prolonged the survival of tumor-bearing mice (Fig. 8e). These
(Extended Data Fig. 9j–m). Similarly, suppression of translation was not studies suggest that dietary manipulation of threonine can augment
due to inhibition of mTOR signaling or activation of the ISR pathway, the efficacy of targeted therapeutics.
as we did not observe differential mTOR and eIF2α phosphorylation In multiple clinical datasets, including TCGA, the CGGA, Rem-
in tumor tissues from mice exposed to different diets (Extended Data brandt and Gravendeel, YRDC expression positively correlated with
Fig. 8 | Dietary intervention potentiates standard therapeutics. a–c, Graphic colored red in i and compared in j. k,l, Violin plot of translational activity in RNA-
illustration (a), tumor growth curve from in vivo bioluminescence analysis seq data of TCGA_LGG, GBM (grade II, n = 216; grade III, n = 241; grade IV, n = 152)
(b, n = 5 mice per group) and Kaplan–Meier survival curves (c, n = 5 mice (k) and the CGGA (grade II, n = 188; grade III, n = 255; grade IV, n = 249) (l). m,
per group) of GSC468-bearing mice with the indicated treatment. TMZ, Kaplan–Meier survival curves of CGGA_GBM (IDH wild type) based on YRDC mRNA
temozolomide. d, Therapeutic efficacy prediction of drugs for YRDC (Methods). expression. The top 25% and the bottom 25% are defined as high and low groups,
The blue dot shows the top resistance drug, and red dots show the top sensitive respectively. MST, median survival time; m, months. n, Pearson correlation of
drugs for high YRDC expression. e, Kaplan–Meier survival curves (n = 5 mice per YRDC expression and translational activity in RNA-seq data of CGGA_GBM (IDH
group) of GSC468-bearing mice with the indicated treatment. f,g, Immunoblots wild type) (n = 183). The red line shows linear regression. o, Graphic abstract of this
showing YRDC expression in GBM (T), matched peripheral tissues (P), non- study. In b, data are presented as mean ± s.e.m. In j–l, violin plots represent the
neoplastic epilepsy tissues (N), benign meningioma (BM) and glioma with overall distribution of data points. In i–n, the n number indicates patients. In
different grades. h, Representative immunohistochemistry staining showing f–h, data are representative of three independent experiments with similar
YRDC expression in LGG and GBM. Scale bar, 100 μm. i,j, Heatmap showing the results. Two-way ANOVA followed by multiple comparisons for b. Log-rank test
activities of translational regulation pathways in RNA-seq data of TCGA_GBM and for c,e,m. Two-tailed Pearson correlation for d,n. Two-tailed unpaired t-test for j.
the GTEx brain cortex (i). The pathway used for inferring translational activity is One-way ANOVA followed by multiple comparisons for k,l.
Nature Cancer
Article https://doi.org/10.1038/s43018-024-00748-7
glioma grade (Extended Data Fig. 10b–e). YRDC was preferentially and genomic dimensions: PN, mesenchymal and classical53. YRDC
expressed in GBM tissues at the protein level compared to in paired expression was slightly higher in the PN subtype, without differences
peripheral brain tissues (Fig. 8f), non-neoplastic brain tissue, meningi- between mesenchymal and classical subtypes (Extended Data Fig. 10f).
omas and low-grade gliomas (LGGs) (Fig. 8g,h). GBM can be classified The PN subtype expresses high levels of OLIG2 and often harbors PDG-
into three molecular subtypes based on its intrinsic transcriptomic FRA alterations and isocitrate dehydrogenase 1 (IDH1) mutations54.
a b c
GSC468
2,000 Tumor
implantation
Treatment Diet: control diet or TR diet 1,500
start Drug: vehicle or TMZ 1,000
500
Time (d)0 3 7 14 21 24
Imaging 0
Time (d)
Nature Cancer
xulf
latoT
)s/p
401×(
Control
TR diet
TMZ
100 Combination
P = 0.0004
P = 0.0002 50
Treatment
P < 0.0001 0
3 7 14 21 24 0 10 20 30 40
fo ytilibaborP lavivrus
Control
TR diet P = 0.0023
TMZ P = 0.0023
Combination P = 0.0023
Treatment
Time (d)
Therapeutic efficacy prediction
High YRDC expression = resistance
5
Canertinib
0 200 400 600
Ranking
Alvocidib Dinaciclib
–5 BRD-K30748066
GSK-J4
High YRDC expression = sensitive
tneiciffeoc
noitalerroC
erocs
Z
100
50
0
0 10 20 30 40
fo
ytilibaborP lavivrus
d e f
Control
TR diet P = 0.0026
Alvocidib P = 0.0026
Combination P = 0.0026
g
Treatment
Time (d)
LGG1 LGG1
Normal (n = 293) GBM (n = 166)
GOBP: positive regulation of translation in response to endoplasmic reticulum stress
GOBP: positive regulation of translation in response to stress
GOBP: negative regulation of translational initiation 3
GOBP: positive regulation of translation 2
GBM1 GBM2 GOBP: positive regulation of translational initiation 1
0
GOBP: positive regulation of cytoplasmic translation
−1
GOBP: positive regulation of mitochondrial translation −2
GOBP: negative regulation of cytoplasmic translation −3
GOBP: negative regulation of translational elongation
erocs
Z
h i
CGGA_GBM (IDH wild type)
100
50
0
0 50 100 150
Time (months)
lavivrus
fo
ytilibaborP
CGGA_GBM (IDH wild type)
4 R = 0.5255
High translation (n = 45, MST = 12.7 m) P < 0.0001
Low translation (n = 45, MST = 17.8 m) 2
P = 0.0286 0
–2
–2 –1 0 1 2 3
Translational activity
Z score
noisserpxe
CDRY
erocs
Z
GTEx brain, TCGA_GBM
3 2
1 0 –1
–2
Nor
mal
GB
M
ytivitca
lanoitalsnarT erocs Z
l
TCGA
P < 0.0001
4
2
0 –2
–4
II III IV
m
ytivitca
lanoitalsnarT erocs Z
CGGA
P < 0.0001
P < 0.0001 P = 0.0001 4
2
0 –2 –4
–6
–8
II III IV
n
ytivitca
lanoitalsnarT erocs Z
P > 0.9999
P1T1P2T2P3T3P4T4P5T5P6T6P7T7
kDa
35 YRDC
25
Tubulin 55
Glioma
NB M I II II IIII V I V kDa
35
YRDC 25
Tubulin 55
j k o
P < 0.0001
P < 0.0001 P = 0.4721
Threonine YRDC t6A modified tRNA
tRNA
ANN codon-specific Cell cycle
translation control progression
Dietary
TR
Article https://doi.org/10.1038/s43018-024-00748-7
However, YRDC expression did not correlate with PDGFRA expression, t6A formation may be regulated by environmental cues such
PDGFRA copy number alterations, IDH mutations or MGMT methylation as CO and bicarbonate59. Here, we found that t6A levels can be gov-
2
in GBM (Extended Data Fig. 10g–j). Additionally, we assigned a panel of erned by threonine availability. Aside from serving as a building
patient-derived GSCs into the three subtypes using a well-recognized block, threonine is also required in mouse embryonic stem cells
classifier53, but no correlation between YRDC expression and GSC for S-adenosylmethionine production and histone methylation
subtype was observed (Extended Data Fig. 10k). Overall, these data through a TDH-mediated catabolic pathway60. However, because
suggest that YRDC is generally upregulated in GSCs and GBM instead TDH is a pseudogene with no corresponding enzymatic function in
of being restricted to any molecular subtype. humans34, the importance of threonine to humans is likely unrelated to
To better understand translational activation in GBM, we per- S-adenosylmethionine production and histone methylation. Here, our
formed single-sample GSEA (ssGSEA) to assign tissues with a score studies identified a metabolic role of threonine in t6A biosynthesis and
based on a panel of translational regulation signatures in bulk RNA translational reprogramming, which translates into a well-tolerated
sequencing data. Positive translational regulation pathways were dietary therapy. We recently found that dietary restriction of another
upregulated, and most of the negative translational regulation path- amino acid, lysine, inhibits tumor growth through epigenetic remod-
ways were downregulated in GBM (Fig. 8i). Both positive and negative eling of endogenous immune responses in preclinical studies61. These
regulation of translational initiation signatures were enriched in GBM. findings collectively contribute to additional layers of metabolic
Translational activity increased in GBM compared to in normal tissue regulation during tumorigenesis, offering therapeutic paradigms to
(Fig. 8j), accelerated as glioma progressed from LGG to GBM (Fig. 8k,l) improve the clinical care of patients afflicted with GBM.
and predicted poor survival in IDH-wild-type GBM (Fig. 8m). YRDC
expression positively correlated with increased translational activity Methods
(Fig. 8n). This study complies with all relevant ethical regulations and was
approved by the Clinical Research Ethics Committee of the First Affili-
Discussion ated Hospital of Sun Yat-sen University, the Institutional Review Board
Crosstalk among microenvironmental cues, amino acid metabolism, of the Case Western Reserve University and the Institutional Animal
tRNA post-transcriptional modification and translational reprogram- Care and Use Committee of the University of Pittsburgh.
ming remains poorly understood in tumor biology. Here, we report
that cancer stem cells in GBM (that is, GSCs) are characterized by high Human glioma and non-neoplastic brain tissues
translation rates, which are driven by YRDC- and threonine-mediated t6A All pathologically diagnosed glioma samples, their adjacent brain tis-
modification on ANN-decoding tRNA. Rewired metabolism in GSCs leads sues, benign meningioma and non-neoplastic brain tissue (epilepsy)
to threonine accumulation, which facilitates t6A biosynthesis through used in this study were collected from excess surgical resection samples
YRDC and causes ANN codon-dependent translational reprogramming from the Department of Neurosurgery at the First Affiliated Hospital
to fuel cell cycle progression. Depletion of YRDC or dietary restriction of Sun Yat-sen University with written informed consent. The study
of threonine dampens t6A levels, leading to suppressed translation and was approved by the Clinical Research Ethics Committee of the First
compromised GSC survival and GBM growth (Fig. 8o). In clinical data, Affiliated Hospital of Sun Yat-sen University ([2020]322). All patient
YRDC is enriched in GBM and correlates with translational activity. studies comply with the Declaration of Helsinki.
Embryonic stem cells maintain low levels of translation5. Mecha-
nisms underlying the disparity in translation levels between normal and Glioblastoma stem cell derivation and cell culture
cancer stem cells have been unclear. One possibility is that oncogenic GBM tissues were obtained from excess surgical resection samples
mutations in cancer stem cells drive active translation, as oncogenic from patients at the Case Western Reserve University with written
pathways required for cancer stem cell maintenance, including RTK– informed consent from patients and in accordance with an institu-
RAS, PI3K–AKT, MYC and β-catenin–WNT, promote translation in many tional review board-approved protocol (090401). All samples were
malignancies3,4. Another possibility is that, in addition to a dormant examined by neuropathologists. All patient studies were carried out
state shared with normal stem cells, GBM harbors a second active pro- in accordance with the Declaration of Helsinki. Patient-derived GSCs
liferating population of GSCs, as revealed by scRNA-seq analysis from were obtained and maintained as previously described52. The GSC23
IDH-mutant oligodendrogliomas and astrocytomas55,56. Collectively, sample was derived from a recurrent GBM biopsy specimen from a
our observations support the complexity of translational regulation 63-year-old male patient and was provided as a generous gift from E.
in cancer stem cell biology. Sulman (NYU Langone Health)52. The GSC456 sample was derived from
t6A localizes at position 37, which is next to the anticodon (posi- a GBM biopsy from an 8-year-old female patient and was provided as
tions 34, 35 and 36). Structural analysis reveals that t6A regulates tRNA a generous gift from D. Bigner (Duke University)62. The GSC468 sam-
function through stabilizing anticodon loop conformation, facilitat- ple was derived from a GBM in our laboratory and transferred via a
ing codon–anticodon pairing and enhancing domain closure of the material transfer agreement from Case Western Reserve University63.
ribosome around the codon–tRNA complex37. However, increasing The GSCRKI line was derived from a GBM and transferred via a mate-
evidence suggests that functions of t6A are more complex with cell rial transfer agreement from the MD Anderson Cancer Centre63. The
type- and context-specific effects11,36,57. Here, we found that t6A does GSC3028 line was derived from a recurrent GBM from a 65-year-old
not contribute to the stability and abundance of tRNA. Instead, t6A female patient52. The GSC387 line was derived from a GBM from a
modifications promote the decoding ability of ANN-decoding tRNA in 76-year-old female patient52. To minimize in vitro cell culture-based
GSCs, resulting in an ANN codon-biased proteomic shift. The effects of artifacts, patient-derived xenografts were propagated as a renewable
t6A modification vary among different tRNA species. Loss of t6A tends source of GSCs. The NSC11 line (hNSC11, Alstem) was derived from
to cause ribosome stalling on ANN codons that are frequently used in human IPS cells. HNP1 human neural progenitors (HN60001, ArunA
human CDS. Codon usage and tRNA abundance have coevolved such Biomedical) are fully differentiated and were derived as adherent
that preferentially used codons correlate with the abundance of cog- cells from the hESC WA09 line. All GSC and NSC lines were cultured
nate tRNA species within cells58. Thus, ANN-decoding tRNA species that in Neurobasal medium (21103049, Gibco) supplemented with B27
are frequently used during translation may serve as the main executors without vitamin A (12587010, Gibco), 20 ng ml−1 recombinant human
of t6A signaling, so that cells need not control every ANN-decoding EGF (236-EG-01M, R&D Systems), 20 ng ml−1 recombinant human bFGF
tRNA, enabling an economical and robust strategy for t6A signaling in (4114-TC-01M, R&D Systems), sodium pyruvate (11360070, Gibco),
translational regulation. GlutaMAX (35050061, Gibco) and streptomycin–penicillin (15140122,
Nature Cancer
