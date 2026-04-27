---
source_path: /mnt/c/Users/Administrator/Zotero/storage/MSVSLYF7/Xu 等 - 2022 - Subtype-specific 3D genome alteration in acute myeloid leukaemia.pdf
ingested: 2026-04-23
sha256: e269f4c636e296d9
---

Article
Subtype-specific 3D genome alteration in
acute myeloid leukaemia
https://doi.org/10.1038/s41586-022-05365-x Jie Xu1,2,13, Fan Song1,3,13, Huijue Lyu1, Mikoto Kobayashi1, Baozhen Zhang1,12, Ziyu Zhao4,
Ye Hou1, Xiaotao Wang1, Yu Luan1, Bei Jia5, Lena Stasiak1, Josiah Hiu-yuen Wong1,
Received: 10 July 2020
Qixuan Wang1, Qi Jin1, Qiushi Jin1, Yihao Fu1, Hongbo Yang1, Ross C. Hardison6, Sinisa Dovat5,
Accepted: 20 September 2022 Leonidas C. Platanias7,8, Yarui Diao9, Yue Yang4, Tomoko Yamada4, Aaron D. Viny10,
Ross L. Levine11, David Claxton5, James. R. Broach2, Hong Zheng5 ✉ & Feng Yue1,7 ✉
Published online: 26 October 2022
Check for updates
Acute myeloid leukaemia (AML) represents a set of heterogeneous myeloid
malignancies, and hallmarks include mutations in epigenetic modifiers, transcription
factors and kinases1–5. The extent to which mutations in AML drive alterations in
chromatin 3D structure and contribute to myeloid transformation is unclear. Here we
use Hi-C and whole-genome sequencing to analyse 25 samples from patients with AML
and 7 samples from healthy donors. Recurrent and subtype-specific alterations in A/B
compartments, topologically associating domains and chromatin loops were
identified. RNA sequencing, ATAC with sequencing and CUT&Tag for CTCF, H3K27ac
and H3K27me3 in the same AML samples also revealed extensive and recurrent
AML-specific promoter–enhancer and promoter–silencer loops. We validated the role
of repressive loops on their target genes by CRISPR deletion and interference.
Structural variation-induced enhancer-hijacking and silencer-hijacking events were
further identified in AML samples. Hijacked enhancers play a part in AML cell growth,
as demonstrated by CRISPR screening, whereas hijacked silencers have a
downregulating role, as evidenced by CRISPR-interference-mediated de-repression.
Finally, whole-genome bisulfite sequencing of 20 AML and normal samples revealed
the delicate relationship between DNA methylation, CTCF binding and 3D genome
structure. Treatment of AML cells with a DNA hypomethylating agent and triple
knockdown of DNMT1, DNMT3A and DNMT3B enabled the manipulation of DNA
methylation to revert 3D genome organization and gene expression. Overall, this
study provides a resource for leukaemia studies and highlights the role of repressive
loops and hijacked cis elements in human diseases.
AML is a myeloid neoplasm characterized by differentiation blockade domains (TADs)11,12 and chromatin loops. Notably, key chromatin struc-
and clonal proliferation of abnormal myeloblasts in the bone mar- ture proteins such as STAG2, RAD21, SMC1 and SMC3 are recurrently
row. The clinical course of AML is highly heterogeneous, with vari- mutated in AML13–15. Furthermore, in B cell and T cell acute lympho-
able molecular characteristics that are essential for risk stratification, blastic leukaemia, altered chromatin conformation is associated
prognosis and therapeutic options1–4. Previous work has shown that with lymphoid malignancies16–19. Therefore, it is important to study
different AML subtypes adopt a specific landscape of chromatin acces- 3D genome organization changes in AML and their relationship with
sibility, histone modifications and binding of various transcription gene dysregulation and pathogenesis.
factors5–9. However, the study of the 3D genome in AML and other cancers is
The study of the spatial organization of chromatin in AML has impeded by the presence of frequent large structural variations (SVs),
been limited. Recent work using chromosome conformation capture including inversions, deletions, duplications and translocations. SVs
techniques has suggested that there are multiple layers of chromatin can induce enhancer hijacking in developmental diseases and different
organization, including A/B compartments10, topologically associating types of cancer20–22. In particular, inv(3) can activate the oncogene EVI1
1Department of Biochemistry and Molecular Genetics, Feinberg School of Medicine, Northwestern University, Chicago, IL, USA. 2Department of Biochemistry and Molecular Biology, Penn State
College of Medicine, Penn State University, Hershey, PA, USA. 3Bioinformatics and Genomics Graduate Program, Huck Institutes of Life Sciences, Penn State University, State College, PA, USA.
4Department of Neurobiology, Northwestern University, Evanston, IL, USA. 5Department of Medicine, Division of Hematology and Oncology, Penn State Cancer Institute, Penn State University,
Hershey, PA, USA. 6Department of Biochemistry and Molecular Biology, Huck Institutes of Life Sciences, Penn State University, State College, PA, USA. 7Robert H. Lurie Comprehensive Cancer
Center, Feinberg School of Medicine, Northwestern University, Chicago, IL, USA. 8Department of Medicine, Jesse Brown Veterans Affairs Medical Center, Chicago, IL, USA. 9Department of Cell
Biology, Duke University School of Medicine, Durham, NC, USA. 10Division of Hematology/Oncology and Columbia Stem Cell Initiative, Columbia University Irving Medical Center, New York, NY,
USA. 11Memorial Sloan Kettering Cancer Center, New York, NY, USA. 12Present address: Key Laboratory of Carcinogenesis and Translational Research (Ministry of Education/Beijing), Division of
Etiology, Peking University Cancer Hospital and Institute, Beijing, China. 13These authors Contributed equally: Jie Xu, Fan Song. ✉e-mail: hzheng@pennstatehealth.psu.edu; yue@northwestern.edu
Nature | Vol 611 | 10 November 2022 | 387
Article
a d e
Samples Assays in primary samples
Primary AML samples Genome topology 60,000 20 P = 6.7 × 10−5 (n = 25) (Hi-C; n = 32) 15
Healthy donors Gene expression 15
(CD34+ HSPC, n = 4 (RNA-seq; n = 28) 40,000
PBMC, n = 3) Chromatin accessibility 10 10 AML cell lines (ATAC-seq; n = 20) (Kasumi-1, THP-1, HL-60, U937) 20,000
DNA methylation 5 5
Assays in cell lines (WGBS; n = 20)
Histone modification, transcription factor 0 0 0 (H3K27ac, H3K27me3, CTCF, IgG; n = 74)
HSPC AML
Mutation (WGS; n = 25)
b
c
through enhancer hijacking in AML21. However, genome-wide enhancer its derivative decitabine are commonly used as therapeutic agents in
hijacking in AML has not been studied. AML. In this study, we also sought to delineate the relationship between
AML is also characterized by a global aberrant DNA methylation DNA methylation and the 3D genome structure and whether a HMA can
profile. The hypomethylating agent (HMA) 5-azacytidine (5-AZA) and restore normal chromatin organization and gene regulation in AML cells.
388 | Nature | Vol 611 | 10 November 2022
)MPT(
noisserpxe
eneG
)MPT(
noisserpxe
eneG
HSPC AML
)bk
04(
snib
fo rebmuN
)965,6 =
n(
274 639 1701 099 720 861 694 424 062 645 810 6191 1201 3591 665 377 4231 339 0631 405 897 926 838 072 868 Hi-C, HiChIP; n = 4 RNA-seq; n = 2
WGBS; n = 5
H3K27ac, H3K27me3, IgG; n = 20 CTCF, EZH2; n = 3
Total libraries; n = 34 Total libraries; n = 199
Chr. 2: 100,150,000–101,150,000 10
Hi-C 0
100.2 100.4 100.6 100.8 101.0
TBC1DB
PC1 correlation
−0.5 1.0 Consensus mutations Other mutations
Normal CD34+ HSPC
Normal CD34+ HSPC
Normal CD34+ HSPC
Normal CD34+ HSPC
STAG2KRAS, NRAS +8, GATA1, IDH1, KMT2C, KMT2D
STAG2KRAS, NRAS –7, IDH2, KMT2D
STAG2 SRSF2, CEBPA
RUNX1 DNMT3A, KMT2C
RUNX1t(9;22) ASXL1, GATA1, NOTCH1
RUNX1t(9;22) ASXL1 DNMT3A JAK1 NOTCH1 TP53 KMT2C, KMT2E
RUNX1t(9;22) TP53, DNMT3A,
TET2 NPM1 IDH1, PTPN1, NRAS/KRAS, CEBPA TET2 NPM1 GATA1, IDH1, MYC, PTPN11, KMT2C
TET2 FLT3-ITD
TET2 NPM1; FLT3-ITDDNMT3A, KMT2C, KMT2E
TET2 FLT3-ITD +8 TET2 FLT3-ITD t(6;9)
CEBPAKMT2A
CEBPAKMT2A WT1, KMT2C
CEBPA GATA2, KMT2C
CEBPA GATA2, RUNX1, SRSF2, STAG2
CEBPA; FLT3-ITD t(8;21)
FLT3-ITD
KMT2B, inv(16)
inv(16)
KMT2B, inv(16) PTPN11, KMT2C, KMT2D
KMT2B NRAS, FLT3-TKD, IDH1, NPM-1, DNMT3A, TET2
KMT2B ASXL1, GATA1, TP53
KMT2B t(9;22)
Normal PBMC
Normal PB MC
No rmal PBMC
312 228 050 143 274 639 1701 099 720 861 694 424 062 645 810 6191 1201 3591 665 377 4231 339 0631 405 897 926 838 072 868 376 675 301
selpmas
yramirp
LMA
Chr. 10: 12,000,000–18,000,000
eulav
1CP
f KRAS t(9;22) FLT3-ITD inv(16) Consensus PC1
mutation 0.04
ENPP2
0
−0.04
DST
ETS1
JAK1
NRAS MEIS1
GATA3
IGF1R
TP63
FGF13
CDKN2A
CDKN2B
MECOM
312 228 050 143 274 639 1701 099 720 861 694 424 062 645 810 6191 1201 3591 665 377 4231 339 0631 405 897 926 838 072 868 376 675 301
Stable A Stable B A-to-B B-to-A
P = 0.009
AML sample no.
HSPC STAG2RUNX1 TET2 CEBPA KMT2B PBMC
Mb
CHST10 PDCL3 NPAS2 Genes 2 LONRF2 NNMMSS PRL31 ATAC-seq0
1
.4
6
H3K27ac 0
5
H3K27me3 0
10
CTCF 0
0.8
RNA-seq (+) 0 0.8
RNA-seq (–) 0
1
WGBS 0
AML sample no.
AML sample no.
Fig. 1 | Genome organization and compartment analysis in primary AML switching in each AML sample compared with HSPCs. e, Gene expression
samples. a, Summary of the AML samples and the genomic profiling assays alterations associated with changes in the A/B compartment. n = 1,724 genes for
performed in this study. b, Snapshot of an example region showing Hi-C, ATAC-seq, A-to-B (left) and n = 867 for B-to-A (right). Genes are located inside recurrent
RNA-seq, WGBS and CUT&Tag for H3K27ac, H3K27me3 and CTCF data in the same compartment switch regions (in at least two AML samples). P values calculated
patient (AML-027). Values for the y axis for the ATAC-seq, CUT&Tag and Hi-C data using two-sided Wilcoxon rank-sum test. For the box plots, the centre line denotes
were normalized to sequencing depths. c, Left, unsupervised hierarchical the median, the top and bottom of the boxes denote the first and third quartiles,
clustering of AML and control samples based on the top 10% most variable PC1 of respectively, and the whiskers extend to 1.5-times the interquartile range of the
the Hi-C matrices. Middle, mutation profiles of the known AML-relevant genes. first and third quartile. f, Clustering analysis of genomic regions (40-kb bins) with
Consensus mutations were not pre-selected but summarized from the clustering differential Hi-C PC1 values, selected by one-way analysis of variance (ANOVA)
result. Right, an example region showing PC1 values and A/B compartment with P < 0.05. Samples were grouped on the basis of gene mutation patterns.
variations (A, red; B, blue) across samples. Squares on the heatmap demarcate Representative COSMIC cancer census and AML-related genes in the
samples with similar mutations. d, Number and proportion of A/B compartment corresponding regions are marked on the right.
Genomic and 3D genome data generation AML-specific chromatin loops
We first performed in situ Hi-C (a derivative of the chromosome con- We predicted chromatin loops at 10-kb resolution using Peakachu27.
formation capture technique) and RNA sequencing (RNA-seq) in 32 On average, we identified approximately 200 AML-specific loops in
primary samples. These samples consisted of 25 AML samples with each AML sample (Fig. 2a and Supplementary Table 1). In Fig. 2b, we
more than 80% of myeloblasts, 4 samples of normal CD34+ haema- show the aggregate peak analysis (APA) for 283 unique loops in the
topoietic stem progenitor cells (HSPCs) and 3 samples of normal AML-1021 sample, which did not occur in any of the HSPC samples.
peripheral blood mononuclear cells (PBMCs) (Fig. 1a). The AML sam- Less than 4.8% of the AML-specific loops were in the copy number
ples covered major driver genetic abnormalities, including muta- variation (CNV) regions (Extended Data Fig. 4a,b), which suggests
tions in NPM1, DNMT3A, TET2, KMT2B and RUNX1, internal tandem that the loops were not confounded by CNVs. The AML-specific loops
duplication of FLT3 (FLT3-ITD), biallelic CEBPA, DEK-NUP214 t(6;9), also showed subtype-specific patterns and contained many known
RUNX1-RUNX1T1 t(8;21), BCR-ABL1 t(9;22) and CBFB-MYH11 inv(16). AML proto-oncogenes (such as MYCN, WT1, ERG, MEIS1 and RUNX1)
On average, we generated around 600 million paired-end reads in in the loop anchors (Fig. 2c). Gene set enrichment analysis showed
each Hi-C library. To identify AML and its subtype-specific enhanc- that genes on AML-specific loops were enriched in haematopoiesis
ers and silencers, we performed assay for transposase-accessible and myeloid transformation pathways28,29 (Extended Data Fig. 4c). For
chromatin with sequencing (ATAC-seq) and CUT&Tag for histone 3 example, MYCN formed a subtype-specific interaction with a cluster
lysine 27 acetylation (H3K27ac) and histone 3 lysine 27 trimethyla- of co-occurring enhancers around 650 kb downstream. Moreover,
tion (H3K27me3). To identify the single nucleotide mutations (SNVs) this loop was only observed in AML samples with TET2 and FLT3-ITD
and SVs, we performed PCR-free whole-genome sequencing (WGS) mutations, with CEBPA mutations or with STAG2, KRAS and NRAS muta-
at about 40 times coverage in 25 AML samples. To profile and study tions (Fig. 2d). Similarly, we observed sample-specific enhanced gene
the impact of aberrant DNA methylation on the chromatin struc- expression and loops for other oncogenes such as MEIS1 and ERG,
ture in AML, we performed whole-genome bisulfite sequencing which link their promoters with AML-specific enhancers (Extended
(WGBS) in 2 PBMC and 18 AML samples at about 30 times coverage. Data Fig. 5).
In addition, we performed CUT&Tag for CTCF in 10 AML samples. Next, we studied the expression profiles of the genes located in the
In total, 199 genomic datasets from primary AML samples were gener- AML-specific loops. As shown in Fig. 2e, 220 genes were significantly
ated (Extended Data Fig. 1). An exemplary region containing all the upregulated in AML and 88 genes were downregulated. By compar-
epigenetic data in the same patient is shown in Fig. 1b. ing these with H3K27ac and H3K27me3 peaks, we identified loop
anchors that contained enhancers or silencers (Fig. 2f). Furthermore,
the majority of AML-specific loops also occurred with the establish-
Subtype-specific compartmentalization
ment of specific enhancer or silencer marks (Fig. 2f). Across all sam-
To investigate whether AML samples possess specific chromatin com- ples, 42.4% of AML-specific loops were between gene promoter and
partmentalization, we performed unsupervised hierarchical clustering enhancers (P-E) and 11.2% were between promoter and silencers (P-S)
using the first principal component (PC1) of the Hi-C matrices. The sam- (Fig. 2g and Supplementary Table 2). P-S loops accounted for 9.2% of
ples were clustered into different groups, which accurately reflected the all loops, with an average size of 169 kb (Extended Data Fig. 6a,b). The
AML genetic subtypes (Fig. 1c), such as RUNX1 and CEBPA mutations. subtype-specific P-S and P-E loops are reported in Supplementary
HSPC and PBMC samples were also grouped together. We noted that a Table 3.
cluster of samples contained mutations in KMT2B, a gene that has not
been used as a dominant AML subtyping classifier before. On average,
Characterizing P-S loops
there was 3.2% A-to-B compartment switch and 2.9% B-to-A switch when
comparing AML samples with HPSC controls (Fig. 1d). Genes located in A total of 70.45% of the P-S loops contained at least one CTCF-binding
the A-to-B or B-to-A switching regions showed decreased or increased site at their anchors (30.38% for both anchors and 40.07% for one
expression, respectively (Fig. 1e). anchor), which suggests that CTCF might play a part in P-S loops
The A/B compartment switching regions were also grouped by their (Extended Data Fig. 6c). Next, we performed CUT&Tag for EZH2, a subu-
genetic mutation profile (Fig. 1f). For example, WT1 showed a B-to-A nit of polycomb repressive complex II, in THP-1 cells. We observed that
switch and expression activation exclusively in samples with TET2 EZH2-binding sites mostly overlapped with H3K27me3 peaks in the P-S
and/or FLT3-ITD mutations, accompanied by the gain of ATAC-seq loop anchors (Extended Data Fig. 6d), which is consistent with the pre-
and H3K27ac peaks (Extended Data Fig. 2a,b). This is consistent with viously reported P-S loops30,31. Genes at AML-specific P-E loop anchors
previous studies showing the association between WT1 activation and had higher expression levels than those at P-S loop anchors (Extended
FLT3-ITD mutation23. Similarly, we observed other compartment-switch Data Fig. 6e; P = 2.2 × 10–16). For the same set of genes across different
regions specific to AML or AML subgroups containing known AML samples, they had higher expression levels when in P-E loops compared
genes such as POUA2F1, FGF13 and BCL11 (Extended Data Fig. 2c). with samples in which they were not in P-E or P-S loops (Fig. 2h, left;
P = 3.72 × 10–21). A similar observation was made for genes in P-S loops
(Fig. 2h, right; P = 5.24 × 10–22).
TAD alteration and gene expression
To further confirm that the decrease in gene expression is due
We predicted TADs at 40-kb resolution in all the samples using the to P-S loops, we performed the following stratification. For each
DomainCaller pipeline11. Alterations in TAD boundaries were deter- RefSeq gene that was expressed in at least one sample, we stratified
mined by comparing the span of each TAD in AML samples to HSPCs. the samples into five categories on the basis of distance between the
We defined three forms of TAD boundary alteration: expansion, shrink transcription start site (TSS) and the nearest non-looping H3K27me3
and shift (Extended Data Fig. 3a). We identified 391 out of the 622 peaks: <10 kb, 10–50 kb, 50–100 kb, 100–200 kb and 200 kb–1 Mb.
curated COSMIC cancer-related and AML-related genes located inside As shown in Extended Data Fig. 6f, local enrichment of H3K27me3
the altered TADs in at least one sample, and more than 100 were recur- peaks correlated with decreased expression when they were within
rent across multiple samples4,24,25 (Extended Data Fig. 3b). However, as 100 kb of the gene promoters. However, for the non-looping
shown in Extended Data Fig. 3c, the majority of TAD alterations did not H3K27me3 peaks that were more than 100 kb away from the gene
affect the expression of genes, which is consistent with a recent study TSS, they did not show significant association with the decreased
of multiple cancer types26. expression of the gene.
Nature | Vol 611 | 10 November 2022 | 389
Article
a
300
200
100
0
(4C) and fluorescence in situ hybridization (FISH) experiments. We first
Validating P-S loops
tested the P-S loops that included IKZF2, a gene frequently deleted in
To validate the P-S loops predicted by the Hi-C data, we performed lymphoblastic leukaemia32. There were two chromatin loops linking
multiple high-resolution circular chromosome conformation capture the IKZF2 promoter with two downstream silencers in multiple samples
390 | Nature | Vol 611 | 10 November 2022
rebmuN
)%(
spool
cfiiceps-LMA
AML-1021 HSPC-213 HSPC-822 HSPC-050 HSPC-341
dezilamroN
stcatnoc
d
PBMC-103
AML-018
AML-773
AML-472
AML-168
AML-629
PBMC-103
AML-018
AML-773
AML-472
AML-168
AML-629
PBMC-103
AML-018
AML-773
AML-472
AML-168
AML-629
PBMC-103
AML-018
AML-773
AML-472
AML-168
AML-629
PBMC-103
AML-018
AML-773
AML-472
AML-168
AML-629
ANR
ca72K3H
CATA
3em72K3H
FCTC
Hi-C surrounding MYCN Chr. 2: 15.50–16.80 Mb
MYCN
lortnoc
lamroN
2TET
APBEC
2GATS
1XNUR
B2TMK
Chr. 2: 15.54–16.65 Mb
PBMC CD34 HSPC
018 260
773 1,953
472 936
168 027
629 270
f
MYCN
8
4
0
100
80
60 8
4 274 1701 720 861 694 424 645 810 6191 377 4231 339 0631 405 897 926 838 072
40 20
0
0
ca72K3H
3em72K3H
H3K27ac H3K27me3
HSPC AML-168 HSPC AML-168
spool
cfiiceps-861-LMA
ni skaeP
e
log(fold change)
2
)eulav
P(
gol− 01
IDH1
WT1
MEIS1
ERG
PLD1
MYB
MYCN
RUNX1
NUP98
)487,5
= n(
spool
laitnereffiD
ytilibaborp
pooL
c
t(9;22) FLT3-ITD inv(16)
1
0
312 228 050 143 274 639 1701 720 861 694 424 062 645 810 6191 1201 6651 377 4231 339 0631 405 897 926 838 072 376 675 301
3
0
KRAS
HSPC RUNX1 TET2 CEBPA KMT2B PBMC
382
=
n
b
20
10
0
P-E Non P-E/P-S
P-E P-P P-S Other
noisserpxe
eneG
)MPT(
P = 3.72 × 10–21
20
15 10
5
0
P-S Non P-E/P-S
noisserpxe
eneG
)MPT(
P = 5.24 × 10–22
stcatnoc
dezilamroN
9
0
h
3 Downregulated Upregulated n = 88 n = 220
2
1 0
−5 0 5
g
1201 0631 861 810 6191 062 720 072 424 274 695 405 645 665 926 377 897 838 339 639 1701 4231
–3 0 3 kb –3 0 3 kb
02
= n
811
=
n
71 = n
14 =
n
AML sample no.
STAG2
AML sample no.
AML sample no.
Fig. 2 | AML and subtype-specific chromatin loops. a, Number of t-test. f, Heatmap of H3K27ac and H3K27me3 peaks in the anchors of AML-
AML-specific loops by comparing with four CD34+ HSPC samples using the specific loops (AML-168 versus HSPC). g, Enhancer and silencer annotations
Gaussian mixture model of Peakachu (false discovery rate < 5%). A total of 22 AML were based on H3K27ac and H3K27me3 signals. When enhancers and silencers
samples that have more than 100 million uniquely mapped reads and minimally are present in the same 10-kb loop anchor, the annotation was determined by
20 million long-range reads (>20 kb) were included for this analysis. b, APA plot the ratio of H3K27ac/H3K27me3 signals. Details are provided in the Methods.
for AML-1021-specific loops compared with four HSPC controls. c, Subtype- P-P, promoter–promoter. h, For each gene in a P-E or P-S loop anchor, AML
specific loop analysis for AML samples. Each row is a loop and the values are the samples were grouped into two categories: with the P-E/P-S loop and without
loop probabilities from Peakachu. d, Left, Hi-C matrix surrounding MYCN. either P-E or P-S loop for this gene. Then the average gene expression (TPM)
Right, from top to bottom, genome browser tracks for RNA-seq, ATAC-seq and within each category was calculated. P values were calculated using two-sided
CUT&Tag for H3K27ac, H3K27me3 and CTCF. The purple arc marks the loop Kruskal–Wallis H-test. n = 4,948 (upper) or 1,508 (lower) genes. For the box
anchors, which link the MYCN promoter to distal enhancers in samples with TET2 plots, the centre line denotes the median, the top and bottom of the boxes
and CEBA mutations. e, Differential expression analysis for genes in recurrent denote the first and third quartiles, respectively, and the whiskers extend to
AML-specific loops compared with HSPCs. P value calculated using two-tailed 1.5-times the interquartile range of the first and third quartile.
b
P = 6.51 × 10–8
IKZF2 silencer (Chr. 2: 212,710,078)
IKZF2 promoter (Chr. 2: 213,155,081)
Equal distance control to promoter IKZF2 promoter to silencer
(Chr. 2: 213,595,735) IKZF2 promoter to equal distance control
Hoechst
c
1.00 + ++
+
0.75 + P = 0.032
+
0.50 ++
+
++++ ++++ + + +
0.25 ++ +
0
0 1,000 2,000 3,000
Days
Nature | Vol 611 | 10 November 2022 | 391
ytilibaborp
lavivruS
d
P = 0.004 + IKZF2 FPKM ≤ 25%
P = 0.001 +IKZF2 FPKM ≥ 75%
Normal AML AML
HSPC and PBMC w/o P-S loop with P-S loop
)MPT(
noisserpxe
2FZKI
a
h
i
j
HSPC-050
CPSH
301-CMBP
861-LMA 810-LMA
PBMC-103
AML-018 AML-168
rohcna
epirtS
AML-546
n = 2,577 All HSPC All PBMC
2.0
1.5
1.0
0.5
0
Nor ma a l n H d S P P B C M C w/o P- A S M s L tr ip
w
e ith P-S A s M tr L ip es
noisserpxe
4FLK
)1+MPT(gol
3.0
P2LL=1.91 P2LL=1.38 P2LL=1.29 2.5
2.0
1.5
1.0
0.5
Stripe anchor
P = 0.02
P = 0.15
35.3
40
30
20
10
1.0 1.3 0 Control sgRNA
noisserpxe
evitaleR
P-S loop
Non-looped genes Looped genes
n = 12,715 n = 2,280
noisserpxe
eneG
)MPT(gol
2
f g
P = 1.7 × 10–4
P = 1.8 × 10–4 H3K27me3
10 0
1 100 100 100 10 Normalized
sgRNA sgRNA for for
S1–S3 S4–S5 Non-loopedLooped
genes genes
3em72K3H
)mμ(
ecnatsiD
Chr. 2: 212.4 212.6 212.8 213.0 213.2 213.4 213.6 213.8 Mb
Probe
AML-546
0.6
0.4
Kasumi-1
0.2
0
Chr. 2
Gene IKZF2 8,000
4C of IKZF2
0
AML-546 0
AML cell line
AM-798
AML-798
e
sgRNA targeting or 500 kb
212.5 Mb hg38 213.2 Mb
P-S loops
Kasumi-1 cells treated with dCas9–VP64 IKZF2
466 kb 336 kb 556 kb
>200 kb
10 KLF4
P = 6.87 × 10–27
8
6
4
2 0
3em72K3H
Chr. 2
S1 S2 S3 S4 S5
40,000]
4C 0 sgControl 0. 5 5]
sgS1–sgS3 0. 5 5]
sgS4, sgS5 0. 5 5]
627 kb
<1 Mb >200 kb <1 Mb
3em72K3H
40
0
40
0
5 μm
212.4 Mb 212.6 Mb 212.8 Mb 213.0 Mb 213.2 Mb
10 25
10 20 0
10
15
0
10
40 5
0 0
Fig. 3 | Identification and validation of repressive loops. a, Hi-C and whereas S1–S3 were not. Lower panel shows the linear distance. f, qPCR data of
H3K27me3 CUT&Tag data in AML samples and the Kasumi-1 cell line. IKZF2 P-S IKZF2 expression (n = 3 technical replicates in 2 biological replicates). P values
loops are marked by black arrows. AML-798 did not have the P-S loops. Orange calculated using two-sided Student’s t-test. Data show the mean ± s.e.m. g, Top,
track indicates 4C data for the IKZF2 promoter. b, Left, DNA FISH image from a schematic defining two categories: genes looped to a silencer 200 kb to 1 Mb
representative THP-1 cell. Labels IKZF2 promoter (green, chromosome 2: away (n = 2,280) versus genes with silencers at the same distance but not looped
213,048,640–213,261,522), silencers (pink, chromosome 2: 212,609,118– to them (n = 12,715). Bottom, RNA expression of the two groups. P value calculated
212,811,039) and the control region (red, chromosome 2:213,495,758– using two-sided Wilcoxon rank-sum test. h, APA plot for AML-specific stripes
213,695,712). Right, distance distribution (n = 98 alleles). P value calculated and the same regions in four combined HSPCs and three combined PBMCs.
using two-sided Wilcoxon rank-sum test. c, IKZF2 expression in normal HSPCs i, A repressive stripe involving the KLF4 gene. j, KLF4 expression across normal
and PBMCs (n = 6), AML samples with the loop (n = 8) and AML samples without samples (n = 6), AML samples with the P-S stripe on KLF4 (n = 13) and AML
(w/o) the loop (n = 17). P value calculated using two-sided Student’s t-test. samples without the stripe (n = 12). P values were calculated using two-sided
d, Kaplan–Meier plot for IKZF2 expression in TCGA AML GDC cohort (n = 152). Student’s t-test. For the boxplots (b,c,g,j), the centre line denotes the median,
P value was calculated using log-rank test. e, H3K27me3 CUT&Tag data in the top and bottom of boxes denote the first and third quartiles, respectively,
Kasumi-1 cells in different conditions. Two clusters of silencers separately and the whiskers extend to 1.5-times the interquartile range.
targeted CRISPR dCas9–VP64. S4 and S5 were looped to the IKZF2 promoter,
Article
from patients with AML and in Kasumi-1 cells (Fig. 3a). 4C sequencing predominantly repressive regions (Extended Data Fig. 8c). In each sam-
data from THP-1 cells confirmed the chromatin interactions between ple, genes located in P-S stripe anchors had significantly lower expres-
the IKZF2 promoter and the silencers (Fig. 3a, orange tracks). Further- sion than those in P-E stripes (Extended Data Fig. 8d; P = 8.74 × 10–22,
more, FISH confirmed that the 3D distance between the IKZF2 promoter Kruskal–Wallis test). For the same genes across different samples, they
and the downstream silencers was significantly shorter than the dis- were expressed at higher or lower levels when located in P-E or P-S stripes
tance between the promoter and an upstream equidistant region in compared with when they were in neither type of stripe (Extended Data
THP-1 and Kasumi-1 cell lines (Fig. 3b and Extended Data Fig. 6g). Across Fig. 8e; P = 0.024 and P = 8.45 × 10–13, respectively).
all samples, IKZF2 expression was significantly lower in samples with P-S
loops (Fig. 3c). Analysis of data from The Cancer Genome Atlas (TCGA)33
Detecting enhancer hijacking in AML
showed that lower expression levels of IKZF2 was associated with poorer
prognosis in AML (Fig. 3d). We performed similar 4C sequencing and To detect enhancer-hijacking events22, we used WGS to identify SVs in 25
DNA FISH experiments to validate another P-S loop that involved RTTN AML samples. In addition, as we have previously demonstrated that certain
in both Kasumi-1 and THP-1 cells (Extended Data Fig. 7a,b). Again, RTTN aberrant Hi-C signals are indicative of SVs such as translocations and inver-
was expressed at lower levels in samples with the P-S loop than in other sions (Extended Data Fig. 9a), we predicted SVs using Hi-C breakfinder20.
samples (Extended Data Fig. 7c). SVs detected by WGS and Hi-C were then merged. On average, each AML
To examine the impact of silencers on their target genes, we per- sample had 1.7 large deletions (>1 Mb), 2.1 inversions (>1 Mb) and 13.2
formed multiple CRISPR deletion and CRISPR interference (CRISPRi) inter-chromosomal translocations (Supplementary Table 5). Permuta-
experiments. First, we deleted about 50 kb in a silencer region (chromo- tion analysis showed that translocations and deletions were enriched in
some 18: 70,411,815–70,460,159) that looped to the RTTN promoter in proximity to AML-related or cancer-related genes (Extended Data Fig. 9b).
Kasumi-1 cells (Extended Data Fig. 7d). We confirmed a heterozygous We predicted SV-induced neo-loops using the software NeoLoop-
deletion in a single-cell-derived clone by PCR and Sanger sequencing Finder36. This program reconstructed the Hi-C maps surrounding the SV
(Extended Data Fig. 7e,f). Deletion of this silencer region increased breakpoints according to SV types, loci and directions, and normalized
RTTN expression by threefold (Extended Data Fig. 7g; P = 5 × 10–5) and the CNV effect. A representative example is shown in Extended Data
slowed cell proliferation (Extended Data Fig. 7h) such that sizes of the Fig. 9c, which shows a fusion between chromosome 7 and chromosome 11
colonies formed by colony-formation assay were substantially reduced in AML-270 but not in HSPCs. This neo-loop connected CDK5 (located
(Extended Data Fig. 7i,j). on chromosome 7) to several enhancers on chromosome 11. By contrast,
Next, we performed additional validation experiments for the P-S there were no such inter-chromosomal Hi-C signals in HSPCs. We per-
loops. There were two distal silencers linked to IKZF2 (S4 and S5; Fig. 3e). formed the neo-loop analysis for all the AML samples, three AML cell
We used CRISPR dCas9–VP64 to de-repress these silencers. In addi- lines (HL60, Kasumi-1 and THP-1) and a chronic myeloid leukaemia cell
tion to nonspecific single guide RNAs (sgRNAs), we used CRISPRi to line (K562)37. The number of neo-loops varied among the samples and
disrupt three nearby silencers not looped to IKZF2 (S1–S3; Fig. 3e) as depended on the number and the types of SV (Supplementary Table 2).
an additional control. Following dCas9–VP64 expression with target- To systematically identify recurrent enhancer-hijacking events, we
ing of S4 and R5, IKZF2 RNA expression was significantly increased by defined three scenarios. One, the same gene and hijacked enhancer
more than 35-fold (Fig. 3f; P = 0.00017). CUT&Tag data confirmed that pairs across different samples. Such events were usually formed across
H3K27me3 signals at the targeted silencers were reduced (Fig. 3e). recurrent SVs, such as t(9;22) and inv(16). For example, we observed a
By contrast, disrupting the non-looping S1–S3 silences did not increase recurrent enhancer-hijacking event involving HSF4 in samples AML-629
IKZF2 expression. This result indicates that the chromatin loop is crucial and AML-798 due to inv(16) (Fig. 4a). Two, the same gene links with
for distal silencers to affect their target genes. different enhancers in different samples. For example, MYC (located
Finally, we examined the genome-wide effect of P-S loops com- on chromosome 8) was looped with a cluster of enhancers on chro-
pared to the linear effect of heterochromatin compaction. To define mosome 14 in sample AML-1360 due to t(8;14), but was looped with
high-resolution P-S loops, we performed Hi-C with chromatin immuno- a different set of enhancers on chromosome 11 in HL-60 cells due
precipitation (HiChIP) for H3K27me3 in Kasumi-1 cells. We compared to t(8;11) (Fig. 4b). Similarly, CBL was linked to enhancers on chro-
the expression between genes with looped silencers and genes with mosome 7 in sample AML-270, but in THP-1 cells, it was linked with
silencers at the same range of distance (200 kb to 1 Mb) but not looped enhancers on chromosome 9 (Extended Data Fig. 9d). Three, the same
to them. Genes with looped silencers had significantly lower expression enhancer links to different genes. Fig. 4c shows such an example, in
than those without looped silencers (Fig. 3g; P = 6.87 × 10–27). Taken which the same enhancer was linked to different genes in different
together, these data suggest that distal silencers can negatively affect samples (ST7 and WNT2 on chromosome 7 of sample AML-773, and
the expression of their target gene through repressive loops. POU2F3 on chromosome 11 in sample AML-270). We summarize all
recurrent enhancer-hijacking events across samples and cell lines in
Supplementary Table 6 and list the subtype-specific enhancer-hijacking
Architectural stripes
events in Supplementary Table 7. Furthermore, HSF4, MYC and CBL
Stripes were recently observed in Hi-C maps and proposed as evidence showed increased expression in samples that exhibited enhancer hijack-
of the loop extrusion model34. On average, we found 509 AML-specific ing (Fig. 4d,e and Extended Data Fig. 9e). Moreover, genome-wide,
stripes (length >300 kb; Supplementary Table 4). APA plots indicated genes with hijacked enhancers had significantly higher expression
that the stripe anchor interacts with a sliding zone in both directions (Fig. 4f). To find which transcription factors (TFs) might be involved
(Fig. 3h). The stripes were enriched in super enhancers (Extended Data in enhancer hijacking, we performed a motif search for the recurrently
Fig. 8a,b), which is consistent with previous findings34. Notably, we also hijacked enhancers from scenarios one and three. This identified TFs
identified stripes that connected promoters with silencers. For exam- such as ERG, FLI1, SOX2, RUNX2 and CTCF (Fig. 4g). A motif analysis
ple, we observed a repressive stripe for KLF4 in multiple AML samples for all hijacked enhancers of each sample also confirmed the ETS (EHF,
(Fig. 3i). The entire sliding zone of this stripe was enriched in H3K27me3 ELF4, GABPA, ERG and FLI1) family motifs (Extended Data Fig. 10a).
signals in AML samples but not in controls (Fig. 3i, left), and this stripe
was associated with decreased KLF4 expression (Fig. 3j). This is of note
because previous work35 has suggested that KLF4 promotes myeloid cell Function of hijacked enhancers
differentiation and its downregulation contributes to AML leukaemo- To investigate the impact of hijacked enhancers on AML cell sur-
genesis. Overall, 10% of AML stripes were between gene promoters and vival and proliferation, we performed CRISPRi screening38 with the
392 | Nature | Vol 611 | 10 November 2022
PBMC HSPC
Other AML
AML with
neo P-E
P = 0.002
HL-60 cells
Chr. 8: 127–129.2 Mb Chr. 14: 96.5–99.3 Mb Chr. 8: 129–127 Mb Chr. 11: 94–96.6 Mb
dCas9–KRAB–MeCP2 system. There were 74 neo P-E loops involv- screening library (Fig. 4h and Supplementary Table 8). In total, 14
ing 44 non-redundant enhancers in Kasumi-1 cells. We designed up sgRNAs targeting 13 enhancers were significantly depleted in the
to 6 sgRNAs for each enhancer and used 50 control sgRNAs in the post-screening library (Fig. 4i). We performed luciferase reporter
Nature | Vol 611 | 10 November 2022 | 393
)MPT(
noisserpxE
a
b g
Motif Transcription factor P value
ERG 1 × 10–11
FLI1 1 × 10–6
SOX2 1 × 10–4
RUNX2 1 × 10–3
CTCF 1 × 10–3
c j
AML-773 AML-270
ST7 WNT2 POU2F3 Chr. 7: 116.4–117.4 Mb Chr. 7: 148.9–149.9 Mb Chr. 11: 120.5–118.5 Mb Chr. 7: 150.9–148.9 Mb
Vector II Gene
Translocation
Sequence for
sgRNA abundance
Vector I
Vector II
3ECMSN fo
erocs
tceffe
eneG
senil
llec
LMA
ni
htworg gnitomorP
lavivrus ot laitnessE
h i m
Kasumi-1 Blasticidine Puromycin Remove
for 2 weeks for puromycin 10 days for 1 week
)MPT(
noisserpxE
d e
15 15
AML-629 AML-798
200
20 0 0 150
100
10
Gene 50
20
H3K27ac
0 0 0
0.1
Virtual 4C
0
Chr. 16: 162.3–157.3 Mb Chr. 16: 67.1–67.6 Mb
f
AML-1360
Gene MYC MYC
20
H3K27a 0 c AML with HSPC and
0.01 neo-loop PBMC
Virtual 4C
0
Gene 20 H3K27ac 0
dCas9–KRAB–MeCP2
Spacer library sgRNA library
Transfection Transfection Vector I
)MPT(
noisserpxE
Chr. 16: 162.2–157.2 Mb Chr. 16: 67.1–67.6 Mb
sgRNA
Enhancer Enhancer targeting
Nonspecific control
Depleted enhancer targeting ANRgs
fo egnahc
dloF
)gol(
ecnadnuba
2
30 25.6 25 18.9 20
15
10 7.06.8
5 1.0 0
4
2
0
–2
–4
1,000 2,000 3,000 4,000 5,000 6,000
Normalized read count
ytivitca esareficul
evitaleR
0
1.2 1.00 1.0
0.8
0.52
0.6 0.36
0.4 –1.0
0.2 0
noisserpxe
evitaleR
k
P = 4 × 10–4
P = 2 × 10–3
pGL4.23 I II III IV V sgRL c e o n n t t s i ro g l R e N n A h 1 an f c o s e r g r R I e N n A h 2 an f c o e r r I
1.5
1.0
0.5
0
)mn 054(
ecnabrosbA
HSF4 HSF4
15 15 20
15
0 0
10
5
0
l
25.8 15 15
0 0
Enhancer
sgLenti control P = 7 × 10–3
sgRNA 1
sgRNA 2
2.0 P = 3 × 10–4
1.6
1.2
SFFV dCas9 KRAB MeCP2 P2A BSD 0.8
0.4
hU6 sgRNA scaffold EF-1a PuroR 0
BsmbI BsmbI 0 1 2 3 4 5
Days
Enhancer-targeting
spacer library
Fig. 4 | Identification, characterization and screening of enhancer sgRNAs. Red dots indicate the significantly depleted sgRNAs in the after-
hijacking in AML. a–c, Different scenarios of recurrent enhancer-hijacking screening library. j, Luciferase/Renilla readout for five depleted enhancers
events induced by neo-loops (black circles). a, Recurrent gene (HSF4, orange from screening results (n = 3 technical replicates in 2 biological replicates).
bar) and enhancer (blue bar) pairs in different samples. NeoLoopFinder was Data show the mean ± s.e.m. k, qPCR for NSMCE3 following disruption of
used to reconstruct the Hi-C map surrounding the SV. Virtual 4C was anchored enhancer I separately by two sgRNAs in Kasumi-1 cells (n = 3 technical replicates
at the gene promoter. b, Recurrent gene (MYC) but with different enhancers in in 2 biological replicates). P value calculated using two-sided Student’s t-test.
different samples. c, Recurrent enhancer linked to different genes in different Data show the mean ± s.e.m. l, CERES gene dependency score by CRISPR–Cas9
samples. d,e, Expression of HSF4 (d) and MYC (e) across all AML samples. essentiality screens (DepMap 21Q2 Public). Grey dot indicates AML cell lines,
f, Expression of all genes on neo P-E loops with hijacked enhancers (n = 141 n = 26. Score < 0: perturbation of a gene impairs cell growth. m, CCK-8 assay
genes). P value calculated using one-sided Wilcoxon rank-sum test. g, Homer for proliferation of Kasumi-1 targeting enhancer I. P values were calculated
motif analysis of recurrently hijacked enhancers across all samples. P value using two-sided Student’s t-test (n = 3 biological replicates). Data show the
calculated using binomial test. h, Design of the CRISPR screening experiment. mean ± s.e.m. For boxplots (f,l), the centre line denotes the median, the top
This figure was created with BioRender.com. i, Fold change of each sgRNA and bottom of the boxes denote the first and third quartiles, respectively, and
abundance in Kasumi-1 cells in the pre-screening and post-screening libraries. the whiskers extend to 1.5-times the interquartile range.
Each dot represents one sgRNA. Black dots indicate nonspecific control
Article
assays to test the activity of five of them, and all increased luciferase compared with normal PBMCs and HSPCs (Fig. 6a), which is consist-
expression (Fig. 4j). ent with previous findings46. Sample AML-773 exhibited substantially
To validate the CRISPRi screening result, we performed six indi- high methylation at CpG islands, which may be due to the missense
vidual CRISPRi experiments (Extended Data Fig. 10b). First, we tested mutation (c.146A>G, p.Asp49Gly) in SDHA, which has been associated
enhancer I, which was predicted to regulate NSMCE3. When we dis- with demethylation defects42. Therefore, we removed it from further
rupted enhancer I with dCas9–KRAB–MeCP2 and two different sgRNAs, downstream analysis. Across all samples, we observed subtype-specific
NSMCE3 expression was reduced to 52% and 36% (Fig. 4k). The CUT&Tag DNA hypermethylation patterns (Fig. 6b).
data showed specific depletion of H3K27ac signals at the two targeted We observed that genes in the A compartment had lower methyla-
loci (Extended Data Fig. 10c), whereas there was no reduction in signals tion at TSSs but higher methylation at gene bodies than genes in the
at the NSMCE3 promoter. As an additional control, we performed the B compartment (Extended Data Fig. 11b). This characteristic is consist-
CRISPRi experiment with the same sgRNAs in THP-1 cells, in which ent with the distinct roles of DNA methylations at different regions47.
there is no SV in this region and no enhancer hijacking. As expected, the We observed that CTCF-binding sites in AML samples were hypomethyl-
CRISPRi experiment in THP-1 cells did not reduce NSMCE3 expression ated (Extended Data Fig. 11c). We also identified the loss of CTCF-binding
(Extended Data Fig. 10d). Enhancer II was predicted to upregulate both sites in AML samples that were potentially due to hypermethylation
KBTBD7 and WBP4 expression, whereas enhancers III, IV and V were (Extended Data Fig. 11d). There were on average 76 such sites in each
predicted to upregulate CYP20A1. CRISPRi for each hijacked enhancer AML sample. Overall, 32.4% of hypermethylation-associated loss of CTCF
significantly reduced the expression of their target genes (Extended binding overlapped with TAD boundary switching in patient samples.
Data Fig. 10e). The current loop-extrusion model suggests that a loop is mainly
To investigate the role of NSMCE3 and its hijacked enhancers in pro- driven by the cohesin complex and stops at convergent CTCF sites48.
liferation, we first examined the data from the Achilles Project (https:// Therefore, we investigated whether loss of CTCF binding correlated
depmap.org/portal/achilles/), which has systematically identified with changes in local chromatin interactions (Extended Data Fig. 11e).
essential genes across hundreds of cancer cell lines. As shown in As shown in Extended Data Fig. 11f, we collated the lost CTCF-binding
Fig. 4l, disruption of NSMCE3 impaired cell growth in all of AML cell sites and plotted aggregated differential Hi-C maps (AML-424 com-
lines tested. We then performed CCK-8 assays in cells with sgRNAs pared with HSPC-213), centred at the 142 lost CTCF sites associated
targeting enhancer 1. The results confirmed that both sgRNAs led to with hypermethylation. We observed increased interactions across
significant slower cell growth and proliferation (Fig. 4m). These data the lost CTCF-binding sites, which suggested that disruption of CTCF
provide further evidence that hijacked enhancers might promote AML sites might lead to loss of insulation and change the local chromatin
cell expansion by increasing the expression levels of their target gene. interaction profile. For example, in four AML samples (424, 018, 546
and 472), we observed lost binding of CTCF, and the motif of this was
hypermethylated in these samples (Extended Data Fig. 11g, bar plot).
Silencer hijacking
Correspondingly, we observed multiple gained chromatin loops that
We noted that SV-induced neo-loops could also link silencers with their appeared in these AML samples across the lost CTCF-binding sites,
target genes, and we define such events as silencer hijacking, similar including a loop linking the WDR66 promoter with distal regions. These
to the concept of enhancer hijacking21,22. For example, we observed data suggest that DNA hypermethylation-induced loss of the CTCF
silencer hijacking for two AML-related genes, JAK1 and KMT2C (Fig. 5a,b), insulator can contribute to the gain of chromatin interactions in AML.
both of which were associated with lower expression (Fig. 5c,d). Overall,
5.7% of all the neo-loops in this study led to silencer hijacking, whereas
HMA and DNMT knockout reverses chromatin
17.2% of the neo-loops induced enhancer hijacking (Fig. 5e). Genes
topology
linked with hijacked silencers showed decreased expression (Fig. 5f).
We validated the function of hijacked silencers using the CRISPR To study whether the effects of DNA methylation on the 3D genome
dCas9–UTX (histone demethylase) system (Fig. 5g). First, we structure is reversible, we first created a cell line in which triple knock-
de-repressed a cluster of silencers that were predicted to regulate EXD1 down (TKD) of DNMT3A, DNMT3B and DNMT1 was simultaneously
in Kasumi-1 cells (Fig. 5h). We also de-repressed another silencer, which induced (Fig. 6c). TKD in U937 AML cells was achieved by sequential
was predicted to regulate ALG10, in THP-1 cells (Fig. 5i). Following tar- selection by puromycin (DNMT3A), sorting by GFP (DNMT3B) and RFP
geted de-repression of the hijacked silencers, the expression levels of (DNMT1) and fully inducing by doxycycline. We performed western
EXD1 and ALG10 were increased by 5.97-fold and 2.70-fold, respectively blotting in the TKD cells and confirmed that their protein expression
(Fig. 5j). This result confirmed the repressive role of these hijacked levels were reduced (Fig. 6d).
silencers on their target genes. In a parallel effort, we treated the U937 cells with the DNA HMA 5-AZA,
Overall, we found 261 cancer-related genes for which promoters at a low but effective dosage (0.5 μM for 12 days), to mimic drug delivery
were located in the neo-loop anchors, and 44 of these were recurrent regimens that are more physiologically tolerable and relevant to clini-
across different samples. A detailed analysis is summarized in Fig. 5k, cal dosing. The treatment slowed down cell proliferation (Extended
in which we categorized them according to whether they were linked Data Fig. 12a). We then performed a series of experiments to exam-
to hijacked enhancers or silencers and by the types of SVs, including ine whether such treatment induces adverse side effects. A dosage of
deletion, inversions and inter-chromosomal translocations. 0.5 μM did not induce significant apoptosis (Extended Data Fig. 12b),
DNA double-strand break (Extended Data Fig. 12c) or cell cycle arrest
(Extended Data Fig. 12d). By contrast, higher dosages (from 1 μM to
Altered DNA methylation and the 3D genome
8 μM) led to cell cycle arrest (from G2/M to G1/S phases) (Extended
DNA methylation alteration has been widely reported in cancer and it Data Fig. 12e).
has been shown to displace CTCF binding and induce pathogenic chro- WGBS analysis of the 5-AZA-treated cells confirmed that global meth-
matin interactions in cancer39–43. To understand its relationship with ylation was decreased from 74% to 39% (Extended Data Fig. 13a.b).
chromatin organization in AML, we performed WGBS in 18 AML samples We stratified the genome into CpG islands (CpGi), shores (<2 kb to
and 2 PBMC samples. We also downloaded WGBS and CTCF-binding CpGi), shelves (2–4 kb to CpGi) and open sea (the rest of the genome).
data obtained from HSPCs44,45 for analysis. We observed variable 5-AZA treatment substantially decreased DNA methylation levels for
methylation levels globally in AML samples (Extended Data Fig. 11a) all four regions, with the biggest changes in open sea (Extended Data
and significantly higher methylation at CpG islands in AML samples Fig. 13c), as well as on CTCF-binding motifs (Extended Data Fig. 13d).
394 | Nature | Vol 611 | 10 November 2022
j
Clustering analysis by Hi-CRep49 showed that 5-AZA-treated cells and to the A compartment after 5-AZA treatment. We defined the A-to-B
DNMT TKD cells were more similar to each other than cells treated with reversion in a similar way. Genome-wide, we found high consistency
dimethylsulfoxide (DMSO) (Fig. 6e). We defined B-to-A compartment of the A/B compartment dynamics between the DNMT TKD cells and
reversion as a region in the B compartment under DMSO treatment but 5-AZA-treated cells. Specifically, 865 out of the 905 (95.5%) TKD-induced
in the A compartment in normal HSPCs, and this region switched back A-to-B reversion regions overlapped with the A-to-B revision regions
Nature | Vol 611 | 10 November 2022 | 395
noisserpxe
evitaler
1DXE
P = 4.5 × 10–4
noisserpxe
evitaler
01GLA
g
20
0
Control sgRNA for
5 70 sgRNA hijacked
H3K27me3 0 H3K27me3 0 silencer
0.2 0.2
Virtual 4C Virtual 4C P = 4.6 × 10–5
0 0
2.70
28.72 Mb 29.17 Mb Chr. 15 29.48 C h M r. b 15 41.28 Mb Chr. 15 40.82 M 29 b .57 Mb 34.16 Mb Chr. 12 33.66 Mb 44.92 Mb Chr. 12 44.42 Mb 1.00
Control sgRNA for sgRNA hijacked silencer
stcatnoc
dezilamroN
20
0
stcatnoc
dezilamroN
Transfection: Transfection: UTX Translocation Vector I Vector II Me3Me3Me3
dCas9
Puromycin Silencer
Kasumi-1 fo c r e 7 ll d s a o y rt s in a g n d Stably expressing Gene cells for RFP+ sgRNA Neo P-S loop
Vector I Vector II
mU6 Silencer-targeting sgRNA EF-1A PuroR mCherry UbC dCas9 UTX
1-imusaK 06-LH 265K 1-PHT
AML samples
noisserpxe
C2TMK
)MPT(
a
30
0
Gene Gene 50 KMT2C 50
H3K27me3 H3K27me3
0 0
Chr. 7: 153–151 Mb Chr. 11: 118.5–116.5 Mb
P = 0.083
AML with HSPC and
neo-loop PBMC
pooL
P-E
P-S
Not E/S or unknown
VS
Deletion
30 Inversion
Translocation
0
JAK1
Chr. 1: 64.6–68.6 Mb Chr. 1: 70.1–74.1 Mb
noisserpxe
1KAJ
)MPT(
15
10
5
0
)MPT(
noisserpxE
b k
RPRM
GFI1B
TSC1
RALGDS
VAV2
PRAME
ZEB2 PRRX2 ABL1
EHMT1
MIR126
EHMT2
SLC44A4
KCNJ5
c e f CDH17
PBMC AML with neo P-S P-P ADAMTS15
GTF2A1
HSPC Other AML P-E NFIB
P-S MYC 30 Other CEP57
MAML2
20 SEL1L
17.2% BCR 10 34.9% RAPGEF1
MIF
0 5.7% RND3 d BRD3
60 MCAM
H2AFX
40 42.1% BCL9L
MIR100
20 MIR125B1
EZH2
0 ARHGEF12
FOXR1
CBL
SORL1 KMT2C ABCB8
CDK5
MNX1
SNCG
RUNX1T1 DUSP10
h i
7 5.97
6
5
4
3
2 1.01
1
0
EXD1 ALG10 3
44.855 Mb Chr. 12 44.895 Mb 2 H3K27me3 (sgLenti control) 8 0 H3K27me3 (sgLenti control) 70 0 1
H3K27me3 (targeting S-EXD1) 8 0 H3K27me3 (targeting S-ALG) 70 0 0
dCas9 (sgLenti control)10 0 dCas9 (sgLenti control) 15 0 dCas9 (targeting S-EXD1)1 0 0 dCas9 (targeting S-ALG) 1 0 5
Fig. 5 | Identification and validation of silencer hijacking in AML. a,b, Two that were targeted by dCas9–UTX in Kasumi-1 (h) and THP-1 (i) cells. Top,
examples of silencer hijacking: KMT2C in AML-270 (a) and JAK1 in AML-168 (b). reconstructed Hi-C maps for the regions surrounding the translocation
Below the Hi-C maps are the H3K27me3 CUT&Tag data. c,d, KMT2C (c) and JAK1 breakpoints. Neo-loops are marked by blue circles. Promoters are marked by
(d) expression across all AML and normal samples. e, Pie chart showing orange vertical bars, and the green vertical bars highlight the hijacked
percentages of different types of neo-loops. When enhancers and silencers are silencers. Bottom, CUT&Tag for H3K27me3 and dCas9 after CRISPRi treatment.
present in the same 10-kb loop anchor, annotation of P-E versus P-S loops is The grey vertical bars highlight the regions with the most reduced H3K27me3
determined by the ratio of H3K27ac/H3K27me3 signals (details in the Methods). signals. j, qPCR results of EXD1 in Kasumi-1 cells (left) and ALG10 mRNA
f, Expression of genes on neo P-S loops with hijacked silencers (n = 33 genes). expression in THP-1 cells (right) when the hijacked silencers were de-repressed
P value calculated using one-sided Wilcoxon rank-sum test. For the boxplot, the (n = 3 technical replicates in 2 biological replicates). The control group
centre line denotes the median, the top and bottom of the boxes denote the underwent the same procedures with non-human genome targeting sgRNA.
first and third quartiles, respectively, and the whiskers extend to 1.5-times the P values were calculated using two-sided Student’s t-test. Data show the
interquartile range. g, Design of the CRISPRi experiment for the hijacked mean ± s.e.m. k, List of the recurrent cancer-related genes for which promoters
silencers. This figure was created with BioRender.com. h,i, Hijacked silencers were located in the anchors of neo-loops.
Article
a c
DNMT TKD
Lentiviral transfection DNMT3B, DNMT1 DNMT3A
Tet
D
R
N
-D
M
N
T
M
3B
T3
s
A
h R
sh
N
R
A
N
-E
A
G
-P
F
u
P
roR P
s
u
e
r
l
o
e
m
ct
y
io
c
n
in C
G
el
F
l
P
so
a
r
n
ti
d
ng D
i
o
n
x
d
y
u
c
c
y
t
c
io
li
n
ne Hi-C
DNMT1 shRNA-mCherry 10 days RFP 12 days
Changes in
compartment
DNA HMA treatment and loops
AML cells
1 5 2 - A d Z ay A s Test 5-AZA side effects A D p N o A p t d o a s m is: a c g a e s : p γH as 2 e A - X 3 W W B B Hi-C
Cell cycle arrest: flow cytometry
b
d DNMT TKD
e
Revert to A Revert to B
DMSO SCC TKD 5-AZA TKD 5-AZA
0.78
5-AZA 40 865 379 372 1,399 194
TKD 0.7
h
AML-specific loops
HSPC DMSO treated 5-AZA treated DNMT TKD
AML cell line
compared with HSPC
DMSO 5-AZA
Shared loops with HSPC
i
HSPC DMSO treated 5-AZA treated DNMT TKD
induced by 5-AZA treatment, and the overlap was 79% for the B-to-A A-to-B altered compartments in the AML cell line were reminiscent of
reversion regions (Fig. 6f). As expected, genes in the B-to-A switching the same compartment switching event in patient samples (Fig. 6h).
regions were significantly upregulated (Fig. 6g). Notably, 84% of the Following 5-AZA treatment, 55% of the A-to-B altered compartments
396 | Nature | Vol 611 | 10 November 2022
ytisned
ytilibaborP
TRC Ctrl DNMT T T K R D C Ctrl DNMT T T R K C D Ctrl
k
P = 7 × 10–3
3.0
2.5
2.0
1.5
1.0
0.5
0
j
B DMSO B 5-AZA Loop 2.0
0.68 0.54 5-AZA
DMSO 1.5
1.0
P = 6 × 10–9
0.5
–1.10 0.59 –0.72 0.45
A A 0
B A B A
)MPT(2gol
Control STAG2 RUNX1 TET2 CEBPA KMT2B
slevel
noitalyhtem
dezilamroN
4
2
0
−2 −4
904,21
=
n
1.00
0.75
0.50
0.25
CMBP
CMBP
CMBP
CMBP
CPSH*
CPSH*
274
274
1701
1701
720
720
861
861
694
694
424
424
062
062 645
645
810
810
665
665
4231
377
339
4231
405
339
897
405
926
897
838
926
072
838 072
0
AML sample no.
Control STAG2RUNX1 TET2 CEBPA KMT2B
MW markers MW markers MW markers
DNMT3A150
DNMT3B
100
DNMT1
100
(140 kDa)100 (97 kDa) 75 (200 kDa) 75
GAPDH 37 GAPDH 37 GAPDH 37
(36 kDa) (36 kDa) (36 kDa)
25 25 25
f
AML sample no.
g Compared with
patients with AML Also B
4 in patient
A-to-B
3 4% 84% Stable B
49%
2
Stable A 5-AZA treatment
41% B-to-A
1 6%
RemainRevert
B to A
0 45% 55%
4
3
2
1
0
5.00 5.25 5.50 5.75 6.00
Loop distance (log10)
Fig. 6 | Inhibition of DNA methylation restores chromatin structure and first and third quartiles, respectively, and the whiskers extend to 1.5-times the
gene expression. a, CG methylation levels for the top 10,000 most-variably interquartile range. h, Left, percentage of A/B compartment switching in AML
methylated CpGi across all samples. b, Hierarchical clustering of 12,409 cell lines compared with normal HSPCs. Top right, percentage of switched
differentially methylated regions (Z-score normalized). *, downloaded compartments in the cell line that are consistent with samples from patients with
methylation data (see Methods). c, Experimental design for the DNMT TKD AML. Bottom right, percentage of the stored compartments in AML cell lines
and 5-AZA treatment. WB, western blotting. d, Western blots for DNMT3A, after 5-AZA treatment compared with normal HSPCs. i, Compartmentalization
DNMT3B and DNMT1. MW, molecular weight. e, Stratum adjusted correlation saddle plots for DMSO and 5-AZA treatment. Top left, B–B interaction; bottom
coefficient (SCC) analysis for Hi-C data by HiCRep. f, Venn diagrams comparing right, A–A interaction. Top right and bottom left, A–B interactions. The values
A/B compartment reversion between TKD and 5-AZA. A-to-B reversion was are the average of each quarter square. j, Size distribution of chromatin loops.
defined as a 40-kb bin in the B compartment in normal HSPCs, in the A P values calculated using two-sided Wilcoxon rank-sum test. k, APA plots for
compartment under DMSO treatment and in the B compartment after 5-AZA the different types of loops in different cells and conditions. AML-specific
treatment or TKD. Vice versa for B-to-A reversion. g, Expressions of the genes loops (n = 1,824); shared loops (n = 8,127). A significantly dissociated loop is
in B-to-A reversion regions after 5-AZA treatment for 12 days (n = 80 genes). determined when its fold-change of PEAKACHU probability deviates from the
P value calculated using two-sided Wilcoxon rank-sum test. For boxplots, the Gaussian mixture model (mixture = 2) with a P value < 0.05.
centre line denotes the median, the top and bottom of the boxes denote the
were reversed to the A compartment. We also performed saddle plot
Online content
analysis to examine the interactions between compartments. The
results showed that after 5-AZA treatment, A–A and B–B interactions Any methods, additional references, Nature Research reporting summa-
were decreased, whereas the interactions between the A–B compart- ries, source data, extended data, supplementary information, acknowl-
ment were increased (Fig. 6i). edgements, peer review information; details of author contributions
We investigated the relationship between compartment switches and competing interests; and statements of data and code availability
and CpG density. The stable A compartments were slightly enriched are available at https://doi.org/10.1038/s41586-022-05365-x.
for CpGi, whereas the stable B compartment regions were depleted of
CpGi (Extended Data Fig. 13e). Notably, A-to-B compartment switching 1. Dohner, H. et al. Diagnosis and management of AML in adults: 2017 ELN recommendations
regions under 5-AZA treatment had a lower density of CpGi. We further from an international expert panel. Blood 129, 424–447 (2017).
2. Dohner, H., Weisdorf, D. J. & Bloomfield, C. D. Acute myeloid leukemia. N. Engl. J. Med.
compared changes in methylation levels in different A/B compartment
373, 1136–1152 (2015).
switching regions for CpGi and open sea regions. We noted that the 3. Arber, D. A. et al. The 2016 revision to the World Health Organization classification of
CpGi originally in the A compartment (A-to-A and A-to-B) were hypo- myeloid neoplasms and acute leukemia. Blood 127, 2391–2405 (2016).
4. Papaemmanuil, E. et al. Genomic classification and prognosis in acute myeloid leukemia.
methylated, whereas CpGi originally in the B compartment (B-to-B and
N. Engl. J. Med. 374, 2209–2221 (2016).
B-to-A) were hypermethylated. After 5-AZA treatment, methylation in all 5. Assi, S. A. et al. Subtype-specific regulatory network rewiring in acute myeloid leukemia.
categories were reduced (Extended Data Fig. 13f). We observed similar Nat. Genet. 51, 151–162 (2019).
6. McKeown, M. R. et al. Superenhancer analysis defines novel epigenomic subtypes of
patterns of compartment switching regions in open seas.
non-APL AML, including an RARα dependency targetable by SY-1425, a potent and
Finally, we studied how 5-AZA or DNMT TKD affected chromatin selective RARα agonist. Cancer Discov. 7, 1136–1153 (2017).
loops. There were more long-range interactions in the 5-AZA-treated 7. Harris, W. J. et al. The histone demethylase KDM1A sustains the oncogenic potential of
MLL-AF9 leukemia stem cells. Cancer Cell 21, 473–487 (2012).
cells compared with cells treated with DMSO (Fig. 6j). A comparison
8. Luo, H. et al. CTCF boundary remodels chromatin domain and drives aberrant HOX gene
with HSPCs further identified 1,824 AML-specific loops and 8,127 transcription in acute myeloid leukemia. Blood 132, 837–848 (2018).
shared loops (Supplementary Table 9). Notably, after the treatment, 9. Ghasemi, R., Struthers, H., Wilson, E. R. & Spencer, D. H. Contribution of CTCF binding to
transcriptional activity at the HOXA locus in NPM1-mutant AML cells. Leukemia 35,
the AML-specific loops were more weakened (31.6% significantly disso-
404–416 (2020).
ciated) compared with the shared loops (2.5% significantly dissociated) 10. Lieberman-Aiden, E. et al. Comprehensive mapping of long-range interactions reveals
(Fig. 6k). Consistently, we observed a similar loop dissociation pattern folding principles of the human genome. Science 326, 289–293 (2009).
11. Dixon, J. R. et al. Topological domains in mammalian genomes identified by analysis of
in the TKD cells (34.1% dissociated for AML-specific loops and 6.3%
chromatin interactions. Nature 485, 376–380 (2012).
for shared loops). Compared with stable loops, the dissociated loop 12. Nora, E. P. et al. Spatial partitioning of the regulatory landscape of the X-inactivation
anchors had a higher percentage of CpGi at anchors (Extended Data centre. Nature 485, 381–385 (2012).
13. Yan, J. et al. Histone H3 lysine 4 monomethylation modulates long-range chromatin
Fig. 13g) and higher methylation levels at CpGi in the DMSO-treated
interactions at enhancers. Cell Res. 28, 204–220 (2018).
group and a wider decrease in methylation after 5-AZA treatment 14. Rao, S. S. P. et al. Cohesin loss eliminates all loop domains. Cell 171, 305–320.e24 (2017).
(Extended Data Fig. 13h). 15. Viny, A. D. et al. Cohesin members Stag1 and Stag2 display distinct roles in chromatin
accessibility and topological control of HSC self-Renewal and differentiation. Cell Stem
Cell 25, 682–696.e8 (2019).
16. Yang, M. et al. Proteogenomics and Hi-C reveal transcriptional dysregulation in high
Discussion hyperdiploid childhood acute lymphoblastic leukemia. Nat. Commun. 10, 1519 (2019).
17. Diaz, N. et al. Chromatin conformation analysis of primary patient tissue using a low input
In summary, through large-scale genomic study of primary AML sam-
Hi-C method. Nat. Commun. 9, 4938 (2018).
ples, we identified subtype-specific distal enhancers and silencers, and 18. Kloetgen, A. et al. Three-dimensional chromatin landscapes in T cell acute lymphoblastic
changes in 3D genome features such as compartments, TAD boundaries leukemia. Nat. Genet. 52, 388–400 (2020).
19. Yang, H. et al. Noncoding genetic variation in GATA3 increases acute lymphoblastic
and chromatin loops. In particular, we showed that repressive loops
leukemia risk through local and global changes in chromatin conformation. Nat. Genet.
are widespread in the genome. Moreover, through CRISPR and CRISPRi 54, 170–179 (2022).
experiments, we demonstrated long-range P-S loops as a new mecha- 20. Dixon, J. R. et al. Integrative detection and analysis of structural variation in cancer
genomes. Nat. Genet. 50, 1388–1398 (2018).
nism of tumour suppression in AML. An interesting future experiment 21. Groschel, S. et al. A single oncogenic enhancer rearrangement causes concomitant EVI1
would be to dissolve the chromatin interactions without changing the and GATA2 deregulation in leukemia. Cell 157, 369–381 (2014).
local chromatin status at the cis-regulatory elements. 22. Northcott, P. A. et al. Enhancer hijacking activates GFI1 family oncogenes in
medulloblastoma. Nature 511, 428–434 (2014).
By integrating WGS and Hi-C data, we identified hundreds of 23. Spassov, B. V. et al. Wilms’ tumor protein and FLT3-internal tandem duplication expression
SV-induced neo-loops that linked the hijacked enhancers or silenc- in patients with de novo acute myeloid leukemia. Hematology 16, 37–42 (2011).
ers to their target genes. We showed that disruption of the hijacked 24. Sondka, Z. et al. The COSMIC Cancer Gene Census: describing genetic dysfunction
across all human cancers. Nat. Rev. Cancer 18, 696–705 (2018).
enhancers affected the expression of their target gene and impaired 25. Metzeler, K. H. et al. Spectrum and prognostic relevance of driver gene mutations in
cell proliferation and colony formation. It is important to study the acute myeloid leukemia. Blood 128, 686–698 (2016).
phenotypic effects in greater depth in the future, and animal mod- 26. Akdemir, K. C. et al. Disruption of chromatin folding domains by somatic genomic
rearrangements in human cancer. Nat. Genet. 52, 294–305 (2020).
els will be desirable to provide further biological and translational 27. Salameh, T. J. et al. A supervised learning framework for chromatin loop detection in
insights. genome-wide contact maps. Nat. Commun. 11, 3428 (2020).
28. Jaatinen, T. et al. Global gene expression profile of human cord blood-derived CD133+
Finally, we showed that aberrant DNA methylation is associated with
cells. Stem Cells 24, 631–641 (2006).
3D genome alterations in AML. We demonstrated that exposure to a 29. Diaz-Blanco, E. et al. Molecular signature of CD34+ hematopoietic stem and progenitor
HMA partially restored the chromatin structure, including reverting cells of patients with CML in chronic phase. Leukemia 21, 494–504 (2007).
30. Ngan, C. Y. et al. Chromatin interaction analyses elucidate the roles of PRC2-bound
switched compartment and dissociating AML-specific loops. These
silencers in mouse development. Nat. Genet. 52, 264–272 (2020).
results suggest that treatment with a HMA may achieve therapeutic 31. Cai, Y. et al. H3K27me3-rich genomic regions can function as silencers to repress gene
efficacy, at least in part, through restoration of normal chromatin expression via chromatin interactions. Nat. Commun. 12, 719 (2021).
architecture. Our finding is complementary to a recent study50 that 32. Kataoka, K. et al. Integrated molecular analysis of adult T cell leukemia/lymphoma. Nat.
Genet. 47, 1304–1315 (2015).
showed altered DNA methylation in HCT116 colon cancer cells led to 33. Goldman, M. J. et al. Visualizing and interpreting cancer genomics data via the Xena
changes in H3K9me3 levels and affected CTCF loop-extrusion barriers. platform. Nat. Biotechnol. 38, 675–678 (2020).
34. Vian, L. et al. The energetics and physiological impact of cohesin extrusion. Cell 173,
As we showed that DNA methylation could influence chromatin topol-
1165–1178.e20 (2018).
ogy, combining HMA therapy with other agents that complement the 35. Morris, V. A., Cummings, C. L., Korb, B., Boaglio, S. & Oehler, V. G. Deregulated KLF4
restoration of normal genome architecture might increase therapeutic expression in myeloid leukemias alters cell proliferation and differentiation through
microRNA and gene targets. Mol. Cell. Biol. 36, 559–573 (2016).
responses and inform new mechanism-based therapeutic approaches
36. Wang, X. et al. Genome-wide detection of enhancer-hijacking events from chromatin
to improve treatment outcomes in AML and other cancers. interaction data in rearranged genomes. Nat. Methods 18, 661–668 (2021).
Nature | Vol 611 | 10 November 2022 | 397
Article
37. Phanstiel, D. H. et al. Static and dynamic DNA loops form AP-1-bound activation hubs 47. Neri, F. et al. Intragenic DNA methylation prevents spurious transcription initiation. Nature
during macrophage development. Mol. Cell 67, 1037–1048.e6 (2017). 543, 72–77 (2017).
38. Joung, J. et al. Genome-scale CRISPR–Cas9 knockout and transcriptional activation 48. Sanborn, A. L. et al. Chromatin extrusion explains key features of loop and domain
screening. Nat. Protoc. 12, 828–863 (2017). formation in wild-type and engineered genomes. Proc. Natl Acad. Sci. USA 112,
39. Achinger-Kawecka, J. et al. Epigenetic reprogramming at estrogen-receptor binding sites E6456–E6465 (2015).
alters 3D chromatin landscape in endocrine-resistant breast cancer. Nat. Commun. 11, 49. Yang, T. et al. HiCRep: assessing the reproducibility of Hi-C data using a stratum-adjusted
320 (2020). correlation coefficient. Genome Res. 27, 1939–1949 (2017).
40. Bell, A. C. & Felsenfeld, G. Methylation of a CTCF-dependent boundary controls imprinted 50. Spracklin, G. et al. Heterochromatin diversity modulates genome compartmentalization
expression of the Igf2 gene. Nature 405, 482–485 (2000). and loop extrusion barriers. Preprint at bioRxiv https://doi.org/10.1101/2021.08.05.455340
41. Figueroa, M. E. et al. DNA methylation signatures identify biologically distinct subtypes in (2021).
acute myeloid leukemia. Cancer Cell 17, 13–27 (2010).
42. Flavahan, W. A. et al. Altered chromosomal topology drives oncogenic programs in
SDH-deficient GISTs. Nature 575, 229–233 (2019). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
43. Flavahan, W. A. et al. Insulator dysfunction and oncogene activation in IDH mutant published maps and institutional affiliations.
gliomas. Nature 529, 110–114 (2016).
44. Tovy, A. et al. Tissue-biased expansion of DNMT3A-mutant clones in a mosaic individual is
Springer Nature or its licensor holds exclusive rights to this article under a publishing
associated with conserved epigenetic erosion. Cell Stem Cell 27, 326–335.e4 (2020).
agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted
45. Zhang, X. et al. Large DNA methylation nadirs anchor chromatin loops maintaining
manuscript version of this article is solely governed by the terms of such publishing
hematopoietic stem cell identity. Mol. Cell 78, 506–521.e6 (2020).
agreement and applicable law.
46. Akalin, A. et al. Base-pair resolution DNA methylation sequencing reveals profoundly
divergent epigenetic landscapes in acute myeloid leukemia. PLoS Genet. 8, e1002781
(2012). © The Author(s), under exclusive licence to Springer Nature Limited 2022
398 | Nature | Vol 611 | 10 November 2022
Methods 700 μl of 80% ethanol. The dried DNA pellet was dissolved in 130 μl of
10 mM Tris-HCl, pH 8. The solution was sonicated to shear the DNA
Materials and experiments to an average size of 300–500 bp using a Covaris sonicator with the
Primary sample collection. Human blood samples were obtained following parameters: PIP 140, duty factor 10, burst 200 and duration
with consent from patients with AML or from healthy donors under 58–80 s. Next, 4 μl of sheared DNA was run in 16 μl of water on a 2%
a protocol approved by the Institutional Review Board of Penn State agarose gel to verify the size.
Hershey (STUDY00005272). Peripheral blood or bone marrow aspirates Biotin-labelled DNA was pulled down by washing 150 μl of 10 mg ml–1
from patients with AML and peripheral blood from healthy donors were Dynabeads MyOne Streptavidin T1 beads (Life Technologies, 65602)
collected and immediately subjected to selection for mononuclear cells with 400 μl of 1× Tween washing buffer (TWB: 5 mM Tris-HCl (pH 7.5),
using Ficoll-Paque PLUS density gradient medium (GE Healthcare, 17- 0.5 mM EDTA, 1 M NaCl and 0.05% Tween-20) and the solution was dis-
1440-02) per the manufacturer’s instruction. Myeloblasts accounted carded. The beads were resuspended in 300 μl of 2× binding buffer
for more than 90% of purified PBMCs for most samples, and samples (10 mM Tris-HCl (pH 7.5), 1 mM EDTA and 2 M NaCl) and added to
with blast cell concentrations of less than 80% were further subjected the sheared DNA. The DNA–bead mixtures were incubated at room
to CD34+ selection as described in previous work5. Bone marrow HSPCs temperature for 15 min with rotation. Beads were separated using a
were purchased from Lonza (4M-105). We also utilized eight datasets magnetic rack and the supernatant was discarded. Beads were washed
of HSPCs from previous publications for analysis44,45,51,52. with 600 μl of TWB buffer twice. Sheared DNA was end-repaired by
resuspending the beads in 100 μl of 1× NEB T4 DNA ligase buffer (NEB,
Cell culture. Kasumi-1 cells (American Type Culture Collection (ATCC), B0202), separating the beads, resuspending in end-repair master mix
CRL-2724), HL-60 cells (ATCC, CCL-240), THP-1 cells (ATCC, TIB-202) and (88 μl of 1× NEB T4 DNA ligase buffer with 10 mM ATP (NEB, B0202S),
U937 cells (CRL-1593) were purchased from ATCC. Cells were cultured 2 μl of 25 mM dNTP mix, 5 μl of 10 U μl–1 NEB T4 PNK (NEB, M0201), 4 μl
following the manufacturer’s culture method. Kasumi-1 cells were of 3 U μl–1 NEB T4 DNA polymerase I (NEB, M0203) and 1 μl of 5 U μl–1
cultured in RPMI-1640 growth medium (Gibco, 11875093) containing NEB DNA polymerase I, large (Klenow) fragment (NEB, M0210)) and
20% FBS. HL-60 cells were cultured in IMDM containing 20% FBS (Ther- incubating at room temperature for 30 min. Beads were washed twice
moFisher 12440053). THP-1 cells were cultured in RPMI-1640 containing with 500 μl of TWB buffer, resuspended in 100 μl of 1× Quick ligation
10% FBS. U937 cells were cultured in RPMI-1640 containing 10% FBS. reaction buffer (NEB, B6058) and collected. To proceed with dATP
attachment, beads were resuspended in 100 μl of master mix (90 μl of
In situ Hi-C. One to two million cryopreserved primary samples or cell 1× NEBuffer 2, 5 μl of 10 mM dATP and 5 μl of 5 U μl–1 NEB Klenow exo
lines in a cell culture were spun down at 500g and resuspended in 1 ml minus (NEB, M0212)) and incubated at 37 °C for 30 min. Beads were
per million of RPMI-1640 medium and 10% FBS. Samples were imme- washed twice with 500 μl of TWB buffer, resuspended in 100 μl of 1×
diately crosslinked with 37% formaldehyde (Millipore Sigma, 252549) Quick ligation reaction buffer (NEB, B6058) and collected. To proceed
to a final concentration of 2% and incubated at room temperature for with adaptor ligation, beads were resuspended in 50 μl of 1× NEB Quick
10 min on a tube revolver at 16 r.p.m. to mix. The resulting solution ligation reaction buffer, 2 μl of NEB DNA Quick ligase (NEB, M2200), 3 μl
was quenched with a 2.5 M glycine solution to a final concentration of Illumina adaptor of choice and incubated at room temperature for
of 0.2 M and incubated at room temperature for 5 min on a revolver. 15 min. Beads were washed with 600 μl of TWB buffer and 100 μl of 1×
Cells were pelleted by centrifuging at 500g and 4 °C for 5 min. The pel- Tris buffer, resuspended in 50 μl of 1× Tris buffer and heated at 98 °C for
let was washed once with 1 ml of cold 1× PBS by centrifuging at 500g 10 min to elute the DNA off the beads. Beads were discarded. Size selec-
and 4 °C for 5 min and the supernatant was discarded. Cells were lysed tion was performed to remove small DNA fragments by adding 0.8–0.9×
with 250 μl of lysis buffer to extract nuclei (10 mM Tris-HCl pH 8.0, KAPA beads to the DNA elution, incubating at room temperature for
10 mM NaCl, 0.2% IGEPAL CA630), mixed with 50 μl of 50× protease 5 min and collecting the beads while discarding the supernatant. Beads
inhibitor (Sigma, P8340), and incubated on ice for 15 min. Lysed cells were washed twice with 500 μl of 80% ethanol and eluted in 50 μl of 1×
were pelleted by centrifuging at 2,500g and 4 °C for 5 min and washed Tris buffer. Library amplification was performed with 4–12 cycles of PCR
with 500 μl of lysis buffer. Cell pellets were resuspended in 50 μl of with KAPA 2× library mix. Size selection was performed to remove small
0.5% SDS, incubated at 62 °C for 10 min and then quenched with 145 μl and large fragments using KAPA beads and to maintain DNA fragments
of water and 25 μl of 10% Triton X-100 (Sigma, 93443). Samples were of 150–500 bp. Libraries were sequenced as 150-bp paired-end reads
incubated at 37 °C for 15 min, and 25 μl of 10× NEBuffer2 (NEB, B7207) with a raw sequencing depth between 300 and 700 million read pairs
and 100 units of MboI restriction enzyme (NEB, R0147) were added to per sample on a platform Hiseq Xten or Novaseq.
the reaction for overnight DNA digestion at 37 °C on a tube revolver. The
digestion was then quenched by incubating at 62 °C for 20 min. DNA CUT&Tag. The CUT&Tag experiments were performed exact-
was then end-repaired and biotin-labelled with 50 μl of fill-in master ly per the online protocol53: https://www.protocols.io/view/
mix (37.5 μl of 0.4 mM biotin-14-dATP (Life Technologies, 19524-016), bench-top-cut-amp-tag-z6hf9b6?version_warning=no. For each tar-
1.5 μl of 10 mM dCTP, 1.5 μl of 10 mM dGTP, 1.5 μl of 10 mM dTTP, 8 μl geted protein, 0.1 million cells were used. The following primary anti-
of 5 U μl–1 DNA polymerase I, large (Klenow) fragment (NEB, M0210)) bodies were used at 1:50 dilution: CTCF (Active Motif, 61311), H3K27ac
and incubated at 37 °C for 1.5 h. DNA was then ligated with 900 μl of (Active Motif, 39133), H3K27me3 (Cell Signaling, C36B11), dCas9
ligation master mix (669 μl of water, 120 μl of 10× NEB T4 DNA ligase (Sigma-Aldrich, SAB4200701) and rabbit IgG (Cell Signaling, 2729).
buffer (NEB, B0202), 100 μl of 10% Triton X-100, 6 μl of 20 mg ml–1 BSA We used guinea pig anti-rabbit IgG (H+L) secondary antibody (NBP1-
(Millipore Sigma, B8667) and 5 μl of 400 U μl–1 T4 DNA ligase (NEB, 72763) with 1:50 dilution. pA–Tn5 was bought from EpiCypher
M0202)) and incubated at room temperature for 4 h with slow rotation. (15-1117). The earlier batch pA–Tn5 fusion protein was a gift from
DNA was decrosslinked with 50 μl of 20 mg ml–1 proteinase K (Qiagen, S. Henikoff’s Lab. Final libraries were sequenced as 150-bp paired-end
19133) and 120 μl of 10% SDS and incubated at 55 °C for 30 min. The reads on a platform Novaseq or Hiseq Xten, with raw sequencing depths
reaction was quenched by adding 130 μl of 5 M sodium chloride and between 10 and 20 million read pairs.
incubating at 68 °C overnight. DNA was precipitated by adding 1.6×
the volume of pure ethanol and 0.1× the volume of 3 M pH 5.2 sodium ATAC-seq. ATAC-seq was performed per a published protocol54, but
acetate (Millipore Sigma, S7899). The precipitate was incubated at with minimal modification. In brief, we centrifuged down 50,000
−80 °C for at least half an hour and centrifuged at maximum speed at cells, washed the cells with PBS and performed nuclei extraction with
2 °C for 15 min to remove the supernatant. DNA was washed once with cold lysis buffer. We added an extra step of washing of the nuclei with
Article
another 500 μl of lysis buffer to further remove mitochondrial DNA. Illumina HiSeq X sequencer as 150-bp paired-end reads with an output
We then proceeded with the transposition reaction (Illumina Tagment of 40 million reads per sample.
DNA Enzyme and Buffer Large kit, 20034198) and purification steps
(Qiagen MinElute PCR Purification kit, 28004). We eluted the DNA in CRISPRi (derepression) for silencer loops and neo-loops. CRISPR
20 μl of elution buffer instead of the recommended 10 μl of elution activation was used to validate the predicted silencer loops and repres-
buffer to increase the recovery rate. Then we proceeded with the PCR sive neo-loops. The sgRNA sequences were designed using CRISPick from
amplification step, in which 20 μl of transposed DNA, 2.5 μl of Nextera the Broad institute (https://portals.broadinstitute.org/gppx/crispick/
PCR primer 1, 2.5 μl of Nexteral primer 2 and 25 μl of KAPA HiFi HotStart public), targeting the silencer regions. The best sgRNAs were determined
Ready Mix master mix (KAPA, KR0370) were used. We applied the PCR as the top-ranking sequences based on factors including on-target scores
parameters indicated by the standard protocol with 11 cycles. We then and off-target scores. To generate sgRNA expression vectors, each pair
performed size selection to remove small fragments using KAPA pure of the oligonucleotides for spacers (Integrated DNA Technologies (IDT))
beads, in which 45 μl of KAPA beads was added to 50 μl of PCR solution, was annealed into double-stranded DNA (Supplementary Table 10).
incubated for 15 min at room temperature and a magnet was used to The pool of the library for each were cloned into a sgLenti plasmid
capture the beads and discard the supernatant. The beads were washed (Addgene, 105996), which had been digested using AarI (Thermo Fisher
with 200 μl of 80% ethanol twice and the residual ethanol was removed. Scientific) and gel-purified. The constructs were then transformed to
We resuspend the beads in 20–50 μl of pre-warmed 10 mM Tris-HCl Stbl3-competent cells for expansion (Invitrogen, C737303). Plasmids
pH 8.0, incubated at 37 °C for 10 min, and used a magnet to collect the were extracted using a Qiagen Midi-prep plus kit (12941), and proper
supernatant as the final library. We ran 1 μl of the library on a 2% agarose insertion was confirmed through Sanger sequencing. The sgRNA were
gel to verify the footprint nucleosomes and confirm a successful assay. packed into lentivirus. In brief, pMD2.G, psPAX2 and desired vectors
Libraries were sequenced as 150-bp paired-end reads on a platform were co-transfected into HEK293 T cells using a Lipofectamine 3000
Hiseq 4000 with 20 million raw read pairs per sample. Transfection kit (Thermo Fisher Scientific, L3000015). The medium
was removed the next day, and 10 ml of fresh DMEM + 10% FBS medium
PCR-free WGS. Genomic DNA was isolated using Qiagen DNeasy Blood was added. Lentiviruses were collected for 3 days and condensed using
& Tissue kits (69504) using 0.5 million cells. Concentration was de- Amicon Ultra-15 Centrifugal Filter units (Sigma, UFC901024). The lenti-
tected with a fluorometer or a microplate reader (for example, Qubit virus was then transfected into Kasumi-1 or THP-1 cells, and viable cells
fluorometer, Invitrogen). Sample integrity and purity were detected by that were also RFP+ were selected by FACS 6 days later.
agarose gel electrophoresis. Next, 1 μg of genomic DNA was fragmented pLV hUbC-VP64 dCas9 VP64-T2A-GFP (Addgene, 59791) and dCas9–
using Covaris. KAPA pure magnetic beads (KK8000) were used to select UTX (a gift from S. M. Offer, Mayo Clinic) were also separately packed
DNA fragments with an average size of 300–400 bp. DNA was quantified into lentivirus using the above-described procedures. The lentivirus
using a Qubit fluorometer. The fragments were subjected to end-repair was transfected into Kasumi-1 or THP-1 cells stably expressing the
and were then 3′ adenylated. Adaptors were ligated to the ends of these sgRNA. Three days later, expression of the dCas9–UTX fusion protein
3′ adenylated fragments. The double-stranded products were heat was tested by western blotting (Sigma-Aldrich, SAB4200701), with an
denatured and circularized using the splint oligonucleotide sequence. expected shift to a larger size (around 130–300 kDa). Cells were then
The single-stranded circle DNA was formatted as the final library. The grown to sufficient numbers and the resulting changes in gene expres-
library was qualified using an Agilent Technologies 2100 bioanalyzer. sion were quantified by quantitative PCR (qPCR) with reverse tran-
The library was amplified to make DNA nanoballs, which have more scription. The primers for qPCR are listed in Supplementary Table 10.
than 300 copies of each molecule. The DNA nanoballs were loaded into
the patterned nanoarray and sequenced as 150-bp paired-end reads by CRISPR deletion for Kasumi-1 RTTN silencer loop. sgRNAs for the
combinatorial probe-anchor synthesis. CRISPR–Cas9 system were designed using a combination of bench-
ling (https://www.benchling.com/), CHOPCHOP (https://chopchop.
WGBS. DNA bisulfite treatment was performed using an EZ DNA cbu.uib.no/) and CRISPick (https://portals.broadinstitute.org/gppx/
Methylation-Gold kit (D5005, Zymo Research) according to the crispick/public). The best sgRNAs were determined by selecting
manufacturer’s instructions. The recovered bisulfite-converted sequences that ranked highly in all three public databases (Supplemen-
single-stranded DNA was processed for library construction using an tary Table 11). Factors such as on-target binding efficiency, off-target
Accel-NGS@Methyl-seq DNA Library kit (30024, Swift BioSciences) per unspecific binding, GC content and self-complementarity were also
the manufacturer’s instructions. In brief, using the adaptase module, considered. Sequences were given overhangs to facilitate sticky-end
truncated adapter sequences were incorporated to the single-stranded ligation with digested backbone. The left cut site used a BsmbI-V2 (NEB,
DNA in a template-independent reaction through sequential steps. R0580) digested LentiCRISPRv2GFP plasmid (Addgene, 82416), and the
DNA was then enriched using six cycles of PCR with primers compat- right cut site used an AarI (Thermo Fisher Scientific) digested sgLenti
ible with Illumina sequencing. The quantity and molecular size of the plasmid (Addgene, 105996). The sequences for sgRNA cloning were
library were confirmed with a Qubit HS DNA assay (ThermoFisher) annealed, ligated, transformed and positively selected using LB medi-
and a Tapestation 2200 system coupled with High Sensitivity D1000 um + 1% ampicillin plates. Plasmids were extracted from positive clones,
ScreenTapes (Agilent). Illumina 8-nt dual indices were used for multi- and proper insertion was confirmed through Sanger sequencing.
plexing. Samples were pooled and sequenced on an Illumina NovaSeq Lentiviruses were made using a Lipofectamine 3000 Transfection
S4 sequencer for 150-bp read lengths in paired-end mode with an output Kit (ThermoFisher, L3000015). A mixture of Lipofectamine 3000 with
of 580 million reads per sample. Opti-Mem and a mixture of P3000 with pMD136 plasmid, pAX2 plasmid
and the desired virus plasmid were combined. After a 15-min incubation,
RNA-seq. RNA was extracted using a Qiagen RNeasy Plus kit (74034). the mixture was added dropwise to a 10-cm plate of HEK293T cells with
RNA quality was assessed using Agilent RNA ScreenTape on an Agilent 5 ml of DMEM + 10% FBS. The plates were incubated at 37 °C for 4–6 h
2200 Tapestation and quantified by Qubit. The mRNA was enriched by before adding 3 ml of medium. The next day, the medium was removed
poly-A selection, and second-strand synthesis was performed with the and 10 ml of fresh DMEM + 10% FBS medium was added. The medium
NEBNext Ultra II Non-Directional RNA Second Strand Synthesis Module was collected for the next 3 days, storing the collection at 4 °C and
following the manufacturer’s instructions (E6111S). The average final avoiding light exposure. After three collections, the virus-containing
library size was between 380 and 400 bp. Illumina 8-nt dual indices medium was condensed using Amicon Ultra-15 centrifugal filter units
were used for multiplexing. Samples were pooled and sequenced on an (Sigma, UFC901024). Kasumi-1 cells were initially transfected by adding
the condensed virus and polybrene (Millipore Sigma, TR1003G), recovery in blasticidine-free medium. The selected cells were tested
incubating for 6 h and then adding additional virus and polybrene to for stable expression of dCas9–KRAB–MeCP2 by western blotting. In
increase the transfection rate. The cells were checked for both GFP two separate replicates of experiments, lentiviruses of sgRNA plasmids
and RFP fluorescence before selecting for double-positive cells by flow were then transfected into 2 million of the treated Kasumi-1 cells with
cytometry. The cells were single-cell sorted into 96-well plates as well a multiplicity of infection of <0.3. Cells were selected with 1.5 μg ml–1
as pooled into 15-ml tubes and replated into 24-well plates. For the next puromycin for 10 days and recovered in puromycin-free medium for
week or two, cells were maintained and expanded as necessary. After one more week. Cells were then collected for DNA extraction using
sufficient proliferation, single-cell clones and pooled cells were lysed a Qiagen DNeasy Blood & Tissue kit (69504). The screening library
for genomic DNA, amplified by PCR and analysed by gel electrophoresis was then constructed using the extracted DNA as a template and the
to determine successful cuts. PCR primers were designed such that the NGS-Lib-Fwd and NGS-Lib-Rev as PCR primers. The PCR product from
PCR product size was approximately 250 bp for wild-type and 700 bp a bright band of 270–280 bp was gel purified using a Qiagen purifica-
when successfully deleted. The clones that appeared with the 700 bp tion kit, and it was sequenced on an Illumina HiSeq Xten platform. The
band were further verified by Sanger sequencing. The clone with a suc- primary screening results were analysed using RIGER38 and MAGECK56.
cessful deletion was expanded in culture. qPCR was performed for RTTN
RNA expression with the primer listed in Supplementary Table 11, using CRISPRi screening validation. Enhancer reporter assay. We used
CRISPR-processed Kasumi-1 cells without the deletion as the control. reporter assays to validate gene upregulation activity of five of the
putative hijacked enhancers, for which the sgRNAs were significantly
CRISPRi screening. CRISPR screening was carried out following depleted during CRISPR screening. The enhancers were amplified using
previously published protocols38,55. In brief, the library for spacer se- genomic DNA of Kasumi-1 cells as template, using the primers sum-
quences (Supplementary Table 4) was designed using design_library. marized in Supplementary Table 12. PCRs were performed using Q5
py and synthesized at IDT. In total, 44 non-redundant enhancers in 74 High-Fidelity 2× master mix (M0492S), and the amplicon was cloned into
pairs of P-E neo-loops from Kasumi-1 cells were targeted by 211 sgR- pGL4.23[luc2/minimal promoter] purchased from Promega (E8411) with
NAs, with each enhancer targeted by up to 6 sgRNAs. The library was NEBuilder HiFi DNA Assembly master mix (E2621S). All insertions were
PCR-amplified with 12 cycles using primer GTAACTTGAAAGTATTTC verified by Sanger sequencing. Around 0.5 million Kasumi-1 cells were
GATTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC (forward), transfected with 2 μg of pGL4 constructs, 100 ng Renilla for data normal-
and ACTTTTTCAAGTTGATAACGGACTAGCCTTATTTTAACTTGC ization and 100 ng GFP as transfection control using 6 μl of TransIT-2020
TATTTCTAG CTCTAAAAC (reverse), and was purified with a QIAquick transfection reagent (MIR5404) per the manufacturer’s instructions.
Gel Extraction kit (28706). Plasmid lentiGuide-Puro (Addgene, 52963) After 48 h of transfection, luciferase activity was measured using a
was digested with BsmBI-V2 (NEB, R0580) at 50 °C for 15 min and 42 °C Dual-Glo Luciferase Assay system (E2920) according to the manufac-
for 15 min, and purified with a QIAquick Gel Extraction kit. Gibson as- turer’s instructions. Measurements were taken in triplicate. To control
sembly (NEB, E2611S) was then performed to ligate the plasmid and for cell number and transfection efficiency, firefly luciferase activity was
the amplified library, with the product purified by isopropanol pre- normalized to renilla luciferase. Measurements are presented as a ratio
cipitation. The pooled sgRNA library was electroporated into Endura relative to the activity of the pGL4.23-mini/P empty vector.
ElectroCompetent cells (Lucigene, 60242) with a final concentration
of 25 ng μl–1 according to the user manual. Transformed cells were CRISPRi and qPCR of the predicted regulated gene. The five
transferred to large low-salt LB agar plates. Transformation efficiency enhancer-hijacking events were separately validated by first cloning
was quantified by 1,000 times dilution. A total of 47,000 colonies were their screening sgRNA into a sgLenti plasmid (Supplementary Table 13),
acquired, with each sgRNA covered by more than 200 colonies. Colo- and the plasmid was packed for lentivirus generation. The original
nies were collected from large plates by scraping and washing five times sgLenti plasmid with a stuffer sequence was also packaged for lentivirus
into ampicillin-containing LB medium and pelleting by centrifugation. generation as a control. Two million Kasumi-1 cells stably expressing
The plasmid was extracted using a Qiagen Plasmid Plus Midi kit (12943). dCas9–KRAB–MeCP2, as mentioned above, were transfected with this
The before-screening library was constructed by PCR using the pooled sgRNA or the control lentivirus. Transfected cells were selected by
plasmid as template and NGS-Lib primers (NGS-Lib-Fwd-1: AATGA puromycin (1.5 μg ml–1) for 6 days, and viable RFP+ cells were collected
TACGGCGACCACCGAGATCTA CACTCTTTCCCTACACGACGCTCTTCCG through fluorescence cell sorting. qPCR was performed to measure the
ATCTTAAGTAGAGGCTTTATATATCTTGTGGAAAGGACGAAACACC; NGS- impact on predicted gene expression, using the primers listed in Sup-
Lib-Fwd-2: AATGATACGGCGACCACCGAGATCTACACTC TTTCCCTA plementary Table 13. Cell phenotypic change associated with CRISPRi
CACGACGCTCTTCCGATCTACATGCTTAGCTTTATATATCTTGTGGAA was tested using CCK-8 assays per the manufacturer’s instructions
AGGACGAAACACC; NGS-Lib-Rev-1: CAAGCAGAAGACGGCATACGA (ab228554). Cell dependence to a gene was summarized by curating
GATTCGCCTTGGTG ACTGGAGTTCAGACGTG TGCTCTTCCGATCTCCG the DepMap 21Q3 gene effect score of this gene in all AML cell lines
ACTCGGTGCCACTTTTTCAA; NGS-Lib-Rev-2: CAAGCAGAAGACGG (https://depmap.org/portal/).
CATACGAGATAT AGCGTCGTGACTGGAGTTCAGACGTG TGCTCTTCCG
ATCTCCGACTCGGTGCC ACTTTTTCAA), purified using a Qiagen gel 3D DNA FISH. DNA FISH assays were performed as previously de-
purification kit and sent for sequencing on an Illumina HiSeq Xten scribed57 but with modification. THP-1 and KASUMI-1 cells were fixed
platform to assess the abundance and distribution of each sgRNA with 2% formaldehyde solution and nuclei extracted as described
using python script count_spacers.py. The library passed quality con- for the Hi-C method. The pellet was washed with PBS and stored at
trol using the following parameters: skew ratio = 2.53 (criterial < 10); −80 °C. Crosslinked cells were thawed on ice and lysed in cold lysis
perfect match = 91.5 (>70%); undetected guides = 0 (<0.5%); and cov- buffer (10 mM Tris-HCl, pH 8.0, 10 mM NaCl and 0.2% Triton-X with
erage = around 5,500 per sgRNA (>100). Lentivirus was then gener- proteinase inhibitor) for 10 min, followed by washing with PBS. The
ated from the pooled plasmid as described in the method for CRISPR pellet was resuspended in PBS and attached to glass plates (Super-
deletion. frost Plus Microscope Slides, Fisher Scientific) by centrifugation at
In parallel to the sgRNA library construction, lentiviruses were gener- 300g for 3 min. Cells were permeabilized in buffer containing 0.1%
ated for Lenti_dCas9-KRAB-MeCP2 (Addgene, 122205) as mentioned saponin and 0.1% Triton X-100 in PBS for 10 min at room temperature,
above. Viruses were transfected into Kasumi-1 cells as described above. incubated for more than 20 min at room temperature with 20% glyc-
Cells underwent 15 days of selection with 10 μg ml–1 blasticidine S erol in PBS and freeze–thawed in liquid nitrogen three times. Then,
hydrochloride (Millipore Sigma, CAS number 3513-03-9) and 1 week cells were treated with 0.1 M HCl for 30 min at room temperature and
