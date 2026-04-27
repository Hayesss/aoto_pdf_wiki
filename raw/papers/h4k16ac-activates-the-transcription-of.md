---
source_path: /mnt/c/Users/Administrator/Zotero/storage/H74H5Y39/Pal 等 - 2023 - H4K16ac activates the transcription of transposable elements and contributes to their cis-regulatory.pdf
ingested: 2026-04-23
sha256: 29585c756128c049
---

nature structural & molecular biology
Article https://doi.org/10.1038/s41594-023-01016-5
H4K16ac activates the transcription of
transposable elements and contributes
to their cis-regulatory function
Received: 8 June 2022 Debosree Pal1,7, Manthan Patel1,7, Fanny Boulet1, Jayakumar Sundarraj1,2,
Olivia A. Grant1,3, Miguel R. Branco 1, Srinjan Basu 4, Silvia D. M. Santos 5,
Accepted: 5 May 2023
Nicolae Radu Zabet1, Paola Scaffidi 5,6 & Madapura M. Pradeepa 1
Published online: 12 June 2023
Check for updates Mammalian genomes harbor abundant transposable elements (TEs)
and their remnants, with numerous epigenetic repression mechanisms
enacted to silence TE transcription. However, TEs are upregulated
during early development, neuronal lineage, and cancers, although the
epigenetic factors contributing to the transcription of TEs have yet to
be fully elucidated. Here, we demonstrate that the male-specific lethal
(MSL)-complex-mediated histone H4 acetylation at lysine 16 (H4K16ac)
is enriched at TEs in human embryonic stem cells (hESCs) and cancer
cells. This in turn activates transcription of subsets of full-length
long interspersed nuclear elements (LINE1s, L1s) and endogenous
retrovirus (ERV) long terminal repeats (LTRs). Furthermore, we show
that the H4K16ac-marked L1 and LTR subfamilies display enhancer-like
functions and are enriched in genomic locations with chromatin features
associated with active enhancers. Importantly, such regions often reside
at boundaries of topologically associated domains and loop with genes.
CRISPR-based epigenetic perturbation and genetic deletion of L1s reveal
that H4K16ac-marked L1s and LTRs regulate the expression of genes in
cis. Overall, TEs enriched with H4K16ac contribute to the cis-regulatory
landscape at specific genomic locations by maintaining an active chromatin
landscape at TEs.
Dysregulation of TEs and their insertions into gene exons are usu- H3 K9 (H3K9me3), TRIM28 and Krüppel-associated box-containing
ally disruptive and have been implicated in cancer and neurological zinc finger proteins (KRAB-ZFPs), and the human silencing hub
disorders1,2. When inserted into noncoding DNA, including introns, (HUSH) complex5–9. Apart from these repressive mechanisms, sev-
they can affect the host gene expression in cis or trans. Most TEs eral pluripotency-associated transcription factors (TFs), namely SP1,
cannot transpose owing to acquired mutations and epigenetic and SP3, LBP9, DUX4, DUX, GATA2 and YY1, are enriched at ERV LTRs, and
post-transcriptional silencing mechanisms (reviewed in refs. 3,4). Tran- SOX11, RUNX3 and YY1 are enriched at the 5′ untranslated regions
scription of TEs is repressed by DNA methylation, trimethylated histone (UTRs; containing promoters) of L1 (reviewed in ref. 10). Interestingly,
1Blizard Institute, Faculty of Medicine and Dentistry, Queen Mary University of London, London, UK. 2Bhabha Atomic Research Centre, Mumbai, India.
3School of Life Sciences, University of Essex, Colchester, UK. 4Wellcome-MRC Cambridge Stem Cell Institute, University of Cambridge, Cambridge, UK.
5Francis Crick Institute, London, UK. 6Department of Experimental Oncology, European Institute of Oncology, Milan, Italy. 7These authors contributed
equally: Debosree Pal, Manthan Patel. e-mail: p.m.madapura@qmul.ac.uk
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 935
Article https://doi.org/10.1038/s41594-023-01016-5
most species-specific DNase hypersensitive sites (which are on acces- linked to these TEs, confirming the significance of H4K16ac-mediated
sible chromatin) are occupied by remnants of TEs11,12, suggesting activation of TEs in rewiring the regulatory landscape of a substantial
that TEs have been co-opted, becoming tissue- and species-specific fraction of the mammalian genome.
cis-regulatory elements (CREs). TEs are transiently upregulated during
early development13, in the neuronal lineage14, and in cancer1. The ERV Results
superfamily of LTRs (LTR/ERV) and Alu family of short interspersed We aimed to investigate the role of MSL-mediated H4K16ac in human
nuclear elements (SINE/Alu) often exhibit chromatin features associ- genome regulation. We performed two to three replicates of cleavage
ated with active CREs15–17 and function either as enhancers to regulate under targets and tagmentation (CUT&Tag)39 in human embryonic
genes in cis or act as alternative promoters15. The 5′ UTR of L1 repeats stem cells (H9-hESCs) for histone modifications associated with active
are also bound by tissue-specific TFs, are enriched with chromatin regulatory elements (H3K27ac, H3K122ac, H4K12ac, H4K16ac, mono-
features that are associated with CREs18, and can function as nuclear methylated H3 K4 (H3K4me1) and H3K4me3), polycomb repressed
noncoding RNAs13,19; still, it is unclear whether they can act as CREs. domains (H3K27me3) and heterochromatin (H3K9me3) (Extended
Although TEs have been suggested to contribute to nearly one-quarter Data Fig. 1a and Supplementary Table 1). We evaluated overall data
of the regulatory epigenome10,13,20,21, the chromatin-based mecha- quality and similarity among our CUT&Tag replicates (Extended Data
nisms contributing to regulatory activity in the vast number of TEs Fig. 1a). We generated peaks by merging the replicates, and we used
are unclear. reproducible peaks in at least two replicates to validate our findings
Chromatin features, such as a combination of H3K4me1 and (Extended Data Figs. 1 and 2 and Supplementary Tables 2 and 3). To
H3K27ac, bidirectional transcription of enhancer RNAs (eRNAs), and prevent the same reads from mapping to multiple regions in the repeat
accessible chromatin (determined, for example, using the assay for elements, uniquely mapped CUT&Tag sequencing reads were used for
transposase-accessible chromatin with sequencing (ATAC-seq)) are the analyses. Except for the analysis in Figure 5e, we used multi-mapping
widely used to predict enhancer activity, including for TE-derived reads for L1 subfamily-level enrichment analysis.
enhancers17,22–25. Yet the level of H3K27ac does not correlate with and is
dispensable for enhancer activity, suggesting that other uncharacter- H4K16ac and H3K122ac are enriched at TEs
ized chromatin features could contribute to regulatory activity26–28. Chromatin-state discovery and genome annotation analysis (Chrom-
H4K16ac and H3K122ac are particularly interesting among many his- HMM)40 of CUT&Tag peaks revealed the expected enrichment of
tone acetylations, because they alter chromatin structure directly and H3K4me1, H3K4me3, H3K27ac and H4K12ac at chromatin features
increase transcription in vitro29,30. H4K16ac and H3K122ac are enriched associated with active transcription, including active promoters and
at enhancers, and they identify new repertoires of active enhancers enhancers. Intriguingly, H4K16ac and H3K122ac, but not H3K27ac or
that lack detectable H3K27ac27,31. However, it is challenging to decipher H4K12ac, were enriched at heterochromatin, insulator and transcrip-
the causal role of specific histone acetylations, as many acetylations, tion elongation states (Fig. 1a). Further analysis revealed specific enrich-
including H3K27ac, are catalyzed by multiple lysine acetyltransferases ment of H4K16ac and H3K122ac at the 5′ UTR of full-length L1s and ERV/
(KATs), and KATs also have a broad substrate specificity. H4K16ac is an LTR elements, compared with gene promoters (Fig. 1b–e). H4K16ac
exception, as it is catalyzed explicitly by KAT8 when associated with was also detected at gene bodies, consistent with previous findings
the MSL complex. showing its role in transcription elongation41 (Fig. 1a,b). Interestingly,
Nevertheless, when KAT8 is associated with non-specific lethal however, H4K16ac shows a very low level of enrichment at the gene
(NSL), it catalyzes H4K5ac, H4K8ac and H4K12ac (refs. 32–35). promoters (Fig. 1b,d,e and Supplementary Table 3), similar to recent
In mouse embryonic stem cells (mESCs), KAT8 and H4K16ac mark chromatin immunoprecipitation and sequencing (ChIP–seq) data in
active enhancers and promoters of genes that maintain the identity human cell lines34. Fifty-one percent of full-length L1s (n = 10,000)
of the mESCs27,36. Loss-of-function mutations in KAT8 or MSL3 lead to have reproducible H4K16ac peaks (Supplementary Table 3),
reduced H4K16ac levels and are known to cause neurodevelopmental and although H4K16ac and H3K9me3 are enriched at L1s (Fig. 1b),
disorders37,38. However, the mechanism through which KAT8 containing they are anti-correlated at L1 subfamilies (Extended Data Fig. 1c).
MSL complex-mediated acetylation of H4K16 contributes to genome Less than 10% of the H4K16ac peaks at TEs overlapped with H3K9me3
regulation during normal development is less clear, especially in the (Extended Data Fig. 1b). The H3K9me3 level was also lower at H4K16ac
human genome. peaks that overlapped with L1 5′ UTRs, and the H4K16ac level was lower
Here, we show that H4K16ac is enriched at L1s and LTRs and is at L1s with H3K9me3 peaks (Extended Data Fig. 1c). Reanalysis of public
depleted at gene promoters, and that H4K16ac regulates transcrip- ChIP–seq datasets showed enrichment of H4K16ac at the 5′ UTRs of
tion across the L1 and ERV LTR superfamily of TEs. TEs marked with L1s in human brain tissue (Extended Data Fig. 3a)42. H4K16ac is also
acetylations loop with the neighboring genes and regulate their expres- enriched at the 5′ UTRs of L1s in neuroblastoma (SH-SY5Y), erythro-
sion. CRISPR interference and genetic deletion of H4K16ac-marked leukemia (K562), and transformed dermal fibroblast (TDF) cell lines
(H4K16ac+) TEs leads to the downregulation of genes in cis, demonstrat- and mESCs (Extended Data Fig. 3b–e). This analysis suggests that
ing that H4K16ac+ TEs function as enhancers. Furthermore, depletion H4K16ac enrichment at TEs is not unique to hESCs, but is conserved
of H4K16ac is sufficient for downregulation of L1 and LTRs and genes in cancer cells, human brain tissue and mice. Although H3K27ac and
Fig. 1 | H4K16ac and H3K122ac are enriched at the 5′ UTR of L1 and ERV/LTRs (long interspersed nuclear elements 2), MIRs (mammalian inverted repeats)
in hESCs. a, Bar chart showing the percentage distribution (y axis) of histone and TcMar-Tigger (TcMar-Tigger DNA transposon, Tigger2 subfamily) for
PTMs CUT&Tag peaks across ChromHMM chromatin features. Low signal CUT&Tag peaks. d, Illustration showing the structure of human L1s (above), two
(Lo), transcription (Txn) b, Dot plot showing the ratio (observed/expected) of open reading frames (ORF1 and ORF2), along with endonuclease (EN), reverse
enrichment of CUT&Tag peaks across gene transcription start sites, TE families transcriptase (RT) and carboxyl terminal segment (C) within the ORF2 are
(L1, ERVLTRs, SINE/Alu-Alu family of short interspersed nuclear elements) shown. Heatmap displaying the histone modification CUT&Tag signal (counts
and the gene body. The circle size represents the log value for the ratio, and per million, CPM) at 10,538 (n) full-length L1s (>5 kb, left) and NCBI Ref-seq
2
the color range represents the enrichment ratio. c, Percentage distribution of genes (right); data for three replicates, R1, R2, and R3, are plotted separately.
repeat elements: Alu, ERV_classI & ERV_classII (endogenous retrovirus class e, UCSC Genome Browser tracks (Hg38) showing signal density (CPM) of histone
I & II), ERVL_MaLRs (endogenous retrovirus type-L mammalian apparent modifications (individual replicates) at L1PA10, a representative L1 subfamily,
retrotransposon, hAT_Charlie (member of hAT superfamily of DNA transposon), (left) and the L1PA4, ERV1, and USP38 genes (right).
L3/CR1 (long interspersed nuclear elements 3/chicken repeat1), LINE1, LINE2
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 936
Article https://doi.org/10.1038/s41594-023-01016-5
H4K12ac were detected at some L1 5′ UTRs, they were enriched at a H4K16ac+ L1 5′ UTRs are enriched with enhancer features
much higher level at the promoters of genes (Fig. 1b). Interestingly, LTR subfamilies function as enhancers to regulate genes in a
along with H4K16ac and H3K122ac, L1 5′ UTRs were also enriched with tissue-specific manner in humans and mice (reviewed in ref. 16). LTR5-
H3K4me1 but were depleted of H3K4me3 (Fig. 1d), suggesting that and LTR7-related subfamilies function as enhancers in hESCs21,43,44.
these elements could function as CREs. However, whether L1 elements can act as enhancers to regulate genes
a b
100
Active promoter
Heterochromatin/Lo
Insulator
75
Poised promoter
)% Repetitive/CNV
(
n o Repressed
itu 50
b Strong enhancer
irtsiD
Txn elongation
Txn transition
25
Weak enhancer
Weak promoter
Weak Txn
d
Full-length human LINE1 (>5 kb, n = 10,538)
SP ORF1 ORF2
5′ UTR EN RT C 3′ UTR
ASP
e
R1
H4K16ac
R2
R1
H3K122ac R2
R1
H3K27ac R2
R1
H4K12ac R2
R1
H3K4me1
R2
R1 H3K9me3
R2
H3K4me3
IgG
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 937
ca61K4H
ca221K3H
1em4K3H
3em4K3H
ca72K3H
ca21K4H
3em72K3H
GgI
R1 R2 R3 R1 R2 R3
–1,500 6,500 000,1– 000,1
H4K16ac
H3K122ac
H3K9me3
H3K27ac
H4K12ac
H3K4me1
H3K4me3
H3K27me3
IgG
c
60 Ref-seq genes
y lim ALUs (90,888 transcripts)
a f
E T
fo
n
40 E
E
E
R
R
R
V
V
V
L
_
_
C
C
l
l
a
a
s
s
s
s
I
II
0
0
0
.
.
.
1
2
3
o itu ERVL_MaLRs 0
b hAT-Charlie 0.3
irtsid
L3/CR1 0.2
% 20 LINE1 0.1
LINE2 0
MIRs 0.3
TcMar-Tigger 0.2
0
0.1
0 10
4
10 kb
1.5 chr4:143,070,000 143,180,000 Hg38 3 2.5 0
e 1.5 m
9 K 1.0
2.0 3 H
0 2.0 1.0
1.5 0.6
1.5
1.5 0
0.8
1.5
1.5 0.4
1.5 0
3 1.5
2
1.5 1
R1 1.5 0
R2 1.5 3
1.5 2
1
L1PA10 L1PA4 ERV1 USP38 0
MPC
log(observed/ 2
expected ratio)
4
2
0
−2
−2
0
2
4
Gene body TSS LTR LINE1 Alu
H3K9
me
H
3 4K16
H
a
3
c K122
H
ac 3K27a
H
c 4K12
H
a
3
c
K4
m
H
e
3
1
K4
m
H3
e
K
3
27
H
m
3
e
K
3
36
me3
R
P M
H3K9
m
H
e3 4K16
H
a
3
c K122
H
ac 3K27
H
a
4
c K12
H
a
3
c
K4
m
H3
e
K
1
4 H
m
3
e
K
3
27 H
m
3
e
K
3
36
me3 Ig G
SST SET
Article https://doi.org/10.1038/s41594-023-01016-5
in cis is not known. Here we found that H4K16ac is particularly enriched L1s and LTRs with acetylation marks loop with genes
at the 5′ UTR of full-length L1 subfamilies and correlates with chromatin YY1, enriched at acetylated L1s, functions as a looping factor that facili-
features associated with active enhancers, such as H3K27ac, H3K4me1, tates interaction between enhancers and promoters50. Compared with
BRD4 and ATAC-seq signal (Fig. 2a,d). L1s with acetylation marks, LTRs and Alu elements marked with his-
Interestingly, not all L1 subfamilies are enriched with active tone acetylations are enriched with USF1, REST and a looping factor
enhancer features at the same level. The evolutionarily younger L1s ZNF143 (Fig. 3a and Extended Data Fig. 5). Meta-analysis confirmed the
(L1HS, L1PA2 and L1PA3, 3–12.5 million years) are enriched with active enrichment of CTCF, RAD21 and YY1 at both H3K27ac+ and H4K16ac+ L1
enhancer features, including H4K16ac. These L1s are known to be tran- 5′ UTRs and LTRs (Fig. 3b). Analysis of published Hi-C data revealed
scriptionally active. Despite evolutionarily older L1s being transcrip- that, compared with TEs that lack acetylation marks, TEs with such
tionally inactive, the 5′ UTRs of these L1 subfamilies (L1PA7–L1PA16, marks are enriched at topologically associated domain (TAD) borders
31–80 million years) are enriched with H4K16ac, along with other active (Fig. 3c). Moreover, H4K16ac levels are relatively higher at TEs overlap-
enhancer features, but H3K9me3 is less enriched (Fig. 2a), suggesting ping with the TAD borders than at TEs that do not overlap with TAD
that the 5′ UTRs of older full-length L1s have been co-opted to function borders (Fig. 3d,e). Furthermore, to identify whether TEs with histone
as functional regulatory elements. acetylations loop with genes, we called significant loops from publicly
Analysis of genome-wide enhancer activity data (using self- available micro-C data from H1 hESCs51. This revealed that the fraction
transcribing active regulatory region sequencing, or STARR-seq), of TEs (L1, LTRs and Alu elements) with acetylation marks that form
generated by ENCODE45 from neuroblastoma (SH-SY5Y) and erythro- chromatin loops with genes is significantly higher than the fraction of
leukemia (K562) cell lines, showed enhancer activity specifically at the TEs lacking these marks (Fig. 3f,g). These analyses provide evidence
5′ UTR of L1s (Fig. 2b) in a cell-type-specific manner. The presence of that transcribed TEs enriched with histone acetylation marks could
active enhancer chromatin features (Fig. 2a) and the ability of L1 5′ UTR contribute to three-dimensional (3D) chromatin folding and looping
to drive transcription of the minimal promoter in an in vitro enhancer interactions with genes.
reporter assay (Fig. 2b) further confirmed that 5′ UTRs of full-length
L1s could function as transcriptional enhancers. H4K16ac+ LTR/HERVs act as enhancers
We aimed to use CRISPR interference (CRISPRi) to investigate the
LTRs with H4K16ac process higher enhancer activity role of H4K16ac+ TEs in regulating genes in cis, by recruiting KRAB
Our data show that, apart from the LTR5 and LTR7 elements that show repressor domain (dCAS9-KRAB) to TEs. We performed CRISPRi
clear enrichment of active enhancer chromatin features, some of the for individual LTRs of human endogenous retrovirus (HERV) or L1 5′
subfamilies of LTR16 and LTR33 may also serve as enhancers in hESCs, UTRs by co-transfecting two independent guide RNAs that recruit
because they are enriched with H4K16ac and other active enhancer dCAS9-KRAB to specific TEs enriched with H4K16ac in hESCs. We
chromatin features (Fig. 2c,d). Interestingly, analysis of STARR-seq then performed quantitative reverse transcription PCR (RT–qPCR) for
data from K562 and SH-SY5Y cells revealed that H4K16ac+ LTRs in these nearby expressed genes or genes that show the looping interaction in
cell lines show significantly higher enhancer activity than LTRs that the RAD21-HiChIP data (Fig. 4a)52. CRISPRi targeting an H4K16ac+ LTR7/
overlap with only H3K4me1 or H3K27ac peaks (Fig. 2e,f and Extended HERV-H (HERV type H family) element located ~50 kb away from PEX1
Data Fig. 4a). These results further support the notion that H4K16ac+ and ~30 kb from the GATAD1 promoter led to downregulation of PEX1,
LTRs function as enhancers. The rest of the LTR and Alu families are but not GATAD1 (Fig. 4b,d). CRISPRi targeting another H4K16ac+ LTR7/
not likely to act as enhancers in hESCs, as they lack known enhancer HERV-H element located ~50 kb away from the NUS1 promoter led to
chromatin features (Extended Data Fig. 4b). the downregulation of the NUS1, but not of GOPC (Fig. 4c,d). However,
CRISPRi targeting H4K16ac+ LTRs/HERV-L-18 (HERV type L-18 family)
TEs marked with H4K16ac are bound by looping factors and HERV-L-18 int (internal portion of HERV-L-18) that are close to
We aimed to identify TFs bound at H4K16ac+, H3K27ac+ and H3K122ac+ TAD borders (Figs. 3d and 4d) did not show downregulation of nearby
TEs using TF ChIP–seq data from ENCODE. Expectedly, EP300 is genes ZC3H15 and ODF2L, suggesting that some but not all H4K16ac+
enriched at LTRs marked with H3K27ac (Fig. 3a). YY1 is enriched at L1s HERV/LTR loci function as enhancers. However, it is possible that such
marked with all three marks, supporting the known role of YY1 in activat- H4K16ac+ TEs could contribute to LTR/HERV transcription and 3D
ing L1 transcription46. CTCF and RAD21 showed higher enrichment at genome folding (Fig. 3c–e)53.
H4K16ac+ and H3K122ac+ L1s and LTRs than at H3K27ac+ L1s and LTRs.
MYC and KDM1A were depleted at H4K16ac+ and H3K27ac+ L1s. These H4K16ac+ L1 5′ UTRs function as enhancers
observations are consistent with previous reports showing the role We next focused on L1s and asked whether L1 5′ UTRs enriched with
of CTCF and RAD21 in activating L1 transcription47,48, and of MYC and H4K16ac regulate genes in cis by performing CRISPRi for H4K16ac+ L1 5′
KDM1A in repressing L1 transcription49. SP1, TCF12 and NANOG binding UTRs, together with two L1 5′ UTRs that lack detectable histone acety-
was also specifically enriched at H3K27ac+ L1 and LTRs, suggesting that lation marks. CRISPRi for the H4K16ac+ 5′ UTR of an L1PA10 located
they have a role in transcription at these elements. ~110 kb upstream of USP38 led to specific downregulation of USP38
Fig. 2 | H4K16ac+ TEs are enriched with chromatin features associated with below each panel. e, Violin plots showing STARR-seq signal from K562 cells
enhancer activity. a, Heatmap of CUT&Tag signals for histone modifications (n = 2 biological replicates, signal normalized to input) across LTRs intersecting
and BRD4 (n = 2 or 3 biological replicates), normalized to IgG and ATAC-seq signal H3K4me1 peaks; H4K16ac but not H3K4me1 peaks; H3K4me1 and H4K16ac
at TE subfamilies; –1.5 kb to +6.5 kb from the full-length L1 start sites (>5 kb). peaks; and H3K4me1 and both H3K27ac and H4K16ac peaks. f, Like e, but for
b, Heatmap showing H4K16ac and H3K27ac CUT&Tag and STARR-seq signal, SH-SY5Y cells (n = 2 biological replicates, signal normalized to control) across
normalized to input, in K562 and SH-SY5Y cells. c, Like a, but for ±2.5 kb around LTRs that intersect with no H4K16ac or H3K27ac peaks (n = 40,000 LTRs);
the ERV/LTR center for subfamilies of LTR5, LTR7, LTR9, LTR16 and LTR33. The H3K27ac but not H4K16ac peaks (n = 22,447 LTRs); H4K16ac but not H3K27ac
number of LTRs in each subfamily are shown below. Data for the Alu subfamily peaks (n = 35,349 LTRs); and H4K16ac and H3K27ac peaks (n = 15,602 LTRs).
and the rest of the LTR subfamilies are in Extended Data Figure 5. d, Genome In all box plots, center lines indicate the median, bounds indicate the 25th and
browser tracks (Hg38) showing the average (n = 2 or 3 biological replicates) CPM 75th percentiles, and whisker limits show 1.5 × interquartile range; P values for
for two replicates of H4K16ac, H3K122ac, H3K27ac, H3K4me1 and H3K4me3 all the violin and box plots were calculated using the pairwise two-sided multi-
CUT&Tag data from hESCs. RepeatMasker tracks showing L1 (L1PA7, top), LTR5, comparison Dunn test for post hoc testing, following the Kruskal–Wallis test
LTR16 and LTR33 (bottom), and ENCODE-layered H3K27ac and CREs are shown with Bonferroni correction.
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 938
Article https://doi.org/10.1038/s41594-023-01016-5
but not other nearby genes GAB1 and SMARCA5. Notably, CRISPRi for specificity of the H4K16ac+ L1PA10 element in regulating USP38
two H4K16ac– 5′ UTRs of L1s, located ~30 kb and ~85 kb from the USP38 (Fig. 4e,j). Similarly, CRISPRi for the H4K16ac+ 5′ UTR of L1PA10, located
promoter, led to no change in the USP38 transcript level, showing the ~270 kb from the TANC2 promoter, led to downregulation of TANC2,
a b
hESC K562 SH-SY5Y
L1HS
L1PA2
L1PA3
L1PA4
L1PA5
L1PA6
L1PA7–16
L1P1–4
L1M1–4
0 0.3 0.3 0.3 0.3 0.3 1.6 1.6 0.30 5
L1 5′ UTRs
c d
LTR5Hs
717
LTR16A
4,299
LTR16A1 2,751
LTR16A2
1,844
LTR16B
721
LTR16B1
1,220
LTR16B2
1,685
LTR16E1 e f
K562 STARR-seq at LTRs SH-SY5Y STARR-seq at LTRs
2,579
LTR16E2 ****P = 1.03 × 10–11
2,300 ****P = 1.28 × 10–12
LTR16D ****P = 1.53 × 10–10
1,117 n.s. n.s.
1,000
100
10
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 939
005,2– RTL 005,2
–1.5L1 –6.5 0 0.30 0.30 2.5
Start
LTR5B
496
LTR7
2,485
LTR9
866
LTR16
3,112
chr5:5,768,000
H4K16ac
H3K122ac
H3K27ac
H3K4me1
H3K4me3
H3K9me3
H3K27ac (ENCODE layered)
CREs (ENCODE)
LTR16C
LTR5
6,782
LTR33_A_
1,610
LTR33_A
1,982
LTR33_C
924
LTR33
9,335
Center 0 0.30 0.30 0.3 0.3 0.3 1.6 1.6 0.3 4
MPC
10 kb
Hg38
chr6:132,310,000
2
H4K16ac
2
H3K122ac
2 H3K27ac
H3K4me1 2
2
H3K4me3
2 H3K9me3
H3K27ac
CREs
(ENCODE)
L1PA7
MOXD1
1 kb Hg38
145,934,000 chr7:152,898,000
2
2
2
2
2
2
0
LTR16 LTR33
MPC
****P < 0.0001
****
****
**** **** **** ****
2,000
1,500
1,000
500
0
tupni
revo
egnahc
dloF
H4K16ac H4K12ac H3K122ac H3K27ac
H3K4
me1
H3K4
me3
H3K9
me3
BR
D4
AT A
C-seq H4K16ac H3K27ac
ST
ARR-seq H4K16ac H3K27ac
ST
ARR-seq
RPM
H4K16ac H4K12ac H3K122ac H3K27ac
H3K4
me1
H3K4
me3
H3K9
me3
BR
D4
AT A
C-seq
(ENCODE layered)
0 0 0 0 0 0 H H 3 3 K K 4 4 m m e e H 1– 1+ 3 H K 4 4 K m 16 e a 1 H + c+ 3 H K 4 4 K m 16 e a 1+ c+ H4 H K 3 16 K a 2 c 7 + ac+ H3K27ac H –H 3K 4 2 K 7 1 a 6 c a + H c H – 3 4 K K 2 1 7 6 a a c– H c– H 3 4 K K 27 16 a a c+ c+ H4K16ac+
Article https://doi.org/10.1038/s41594-023-01016-5
0.3
0
but not CYB561 (Fig. 4f,j). CRISPRi for H4K16ac+ L1PA7, located ~24 kb between MOXD1 and STX7 genes with the H4K16ac+ L1PA8, located
from the COMMD10 promoter, also led to a significant downregulation ~100 kb away from the MOXD1 promoter (Fig. 4h,j). CRISPRi for the
of COMMD10, but not the nearby gene SEM6A (Fig. 4g,j). RAD21-HiChIP 5′ UTR of this L1PA8 led to significant downregulation of both MOXD1
data and the micro-C analysis revealed significant looping interactions and STX7. However, the expression of ENPP1, which does not loop
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 940
Thousands
Thousands
LTRs
LTR Alu LINE1
LTR Alu LINE1 500 5.5 0.6 250 H4K16ac+ 2.75
0 0
500 2.8 2
250 1.4 1
H3K27ac+
0 0 0
MPC
seneg
htiw gnipool
sET
fo
%
H3K27ac+ H4K16ac+ LINE1
LTR Alu LINE1
1.0 CTCF
0.9 RAD21 ZNF143 YY1
REST 0.8
USF1 0.7 USF2
ATF3 0.6
POLR2A 0.5
KDM1A –2.5 Center 2.5 kb–2.5 Center 2.5 kb
EP300
5
JUND
TBP 4
MYC 1 3
EGR1
KDM4A 2
0
BACH1 1 SP1 −1 0
TCF12
NANOG –1.5 6.5 kb –1.5 6.5 kb
ASH2L
TAF1
RBBP5
YY1
CTCF
RAD21
MAFK
25
20
*** 15 *** *** 10
5
0
)lortnoc/egnahc
dlof(
langis
naeM
)snib
gol(
sDAT
ot
ecnatsiD
01
a b c
LTRs Alu
**** **** ****
**** **** ****
3 **** **** ****
2
1
LINE1 (>5 kb)
0
T T E E ( ( H H 3 3 K K 1 1 2 6 2 a a c c +) +) T T E E – ( a H c 3 e K t 2 yl 7 a a t c io +) ns **** <2.2 × 10–16
d
1 Mb 1 Mb
50 kb hg38 20 kb hg38
chr2:186,450,000 186,500,000 chr1:86,390,000 86,420,000
1 1
H4K16ac
2.5 2.5
H3K122ac
1 1
H3K27ac
RAD21 RAD21 RAD21
HERVL-int HERVL-18 ZC3H15 ODF2L HERVL-18 int
e f g
H4K16ac CUT&Tag signal
LTRs intersecting with TAD border
LTRs outside TAD border
0.084
0.076
0.07
LTR start
MPC
P = 0.00099 P = 2.2 × 10–16 P = 2.2 × 10–16
P = 2.2 × 10–16 P = 2.2 × 10–16 P = 2.2 × 10–16
P = 2.2 × 10–16 P = 7.8 × 10–14 P = 2.2 × 10–16
P = 1.31 × 10–311
***
P = 2.07 × 10–268
P = 1.69 × 10–68 P = 3. * 03 * * × 10–35 P = 1.13 × 10–8 P = 4.9 × 10–93 P = 5.63 × 10–96 P = 3.89 * × * 1 * 0–5 *** ***
P = 8.04 × 10–5
***
+ca72K3H +ca61K4H +ca221K3H +ca72K3H +ca61K4H +ca221K3H +ca72K3H +ca61K4H +ca221K3H
L1 Start L1 Start
ca
oN
ca221K3H ca61K4H ca72K3H ca
oN
ca221K3H ca61K4H ca72K3H ca
oN
ca221K3H ca61K4H ca72K3H
Fig. 3 | H4K16ac+ L1 and LTRs are enriched at TAD borders and loops with for the violin plots were calculated by Mann–Whitney U test. d, Example UCSC
genes. a, Heatmap shows the difference/sum (details in Methods) ratio for Genome Browser tracks showing H4K16ac, H3K122ac and H3K27ac signals at
observed and expected occurrences of TF-binding sites in H4K16ac, H3K27ac TAD borders (arrow marks) (micro-C data from H9 hESC). CRISPRi was used for
and H3K122ac peaks at the 5′ UTR of L1, ERV/LTR or SINE/Alu, over the random some of these HERV/LTRs for validation (Fig. 4d). e, Average type summary plot
background. Looping factors that are known to be enriched at enhancer- depicting IgG-normalized H4K16ac signal (CPM), with standard error (shaded
promoter loops are in bold; a complete list of TFs is in Extended Data Figure 6. area), at the LTRs overlapping the TAD border (blue) and LTRs elsewhere in the
b, Average type summary plots showing the mean signal distribution (fold genome (red). f, Bar graph showing the percentage of H4K16ac+, H3K27ac+ and
change/control) of YY1 (green), RAD21 (red), and CTCF (blue) at LTRs (top) and H3K122ac+ TEs and TEs that lack these marks (full-length L1, LTR and Alu) that
full-length L1 (>5 kb, bottom) that overlaps with H3K27ac (left) or H4K16ac contact genes through chromatin loops (P values were calculated by Fisher’s
(right). c, Violin plot showing the distance to TAD borders (y axis, log bins) exact test). (# same as in c). g, Aggregate peak analysis (APA) plots for H4K16ac+
10
for LTR (H4K16ac+ #10258, H3K27ac+ #8063, H3K122ac+ #17132), Alu element and H3K27ac+ LTRs, Alu elements, and L1s that contact genes through loops.
(H4K16ac+ #7394, H3K27ac+ #4659, H3K122ac+ #61312) and L1 (H4K16ac+ #892, The number of contacts (in thousands) are shown in the scale bars. In all box
H3K27ac+ #550, H3K122ac+ #1439) marked with H3K27ac, H4K16ac or H3K122ac, plots, center lines indicate the median, bounds indicate the 25th and 75th
and for TEs that lack these marks (LTR #31678, Alu #31589 and L1 #452). P values percentiles, and whisker limits show 1.5 × interquartile range.
Article https://doi.org/10.1038/s41594-023-01016-5
with this L1, was not altered (Fig. 4h,j), demonstrating the specific L1-ORF1p foci in H4K16ac-depleted MSL1-KO hESCs (Fig. 5d). Like hESC
cis-regulatory function of these L1s. data, MSL3 KO in TDFs reduced the bulk of H4K16ac (Extended Data
To further confirm that H4K16ac+ L1 5′ UTRs regulate genes in cis, Fig. 7a) and at L1 5′ UTRs and LTRs (Extended Data Fig. 7d).
we used CRISPR–CAS9 to delete full-length L1 elements in H1 hESCs. RNA-seq data analysis from MSL3-KO TDFs showed significant
Owing to the difficulty of specific deletion of L1 5′ UTRs, we nucleo- downregulation of L1 and LTR transcripts (Extended Data Fig. 7b,c).
fected the cells with pairs of synthetic guide RNAs along with CAS9 Notably, H4K16ac+ L1s, but not H4K16ac– L1s, are significantly down-
(ribonucleocomplex) that target the flanking region of four full-length regulated in MSL1-KO TDFs (Extended Data Fig. 7b). All these results
L1s (~7 kb deletions). We generated two independent clonal lines with confirm the direct role of MSL mediated H4K16ac in the transcrip-
heterozygous deletions for L1PA10 and one clone for L1PA7; both are tional activation of L1. MSL3-KD RNA-seq analysis in hESCs showed
H4K16ac+ and are located upstream of USP38 (Fig. 4e and Extended Data that pluripotency and differentiation-associated genes were unaf-
Fig. 6a,b). In accordance with CRISPRi data, RT–qPCR data showed that fected (Extended Data Fig. 8a,b). However, H4K16ac+ genes were
the deletion of L1PA10 and L1PA7 led to the downregulation of USP38, more affected than were H4K16ac– genes (Extended Data Fig. 8c).
but not other nearby genes that were tested, namely GAB1 and SMARCA5 Further analysis of L1s and LTRs showed significant downregulation
(Fig. 4k). For deletion of L1s located at the MOXD1 and RLN2 loci of both human-specific (L1HS) and primate-specific (L1PA2 to L1PA16)
(Fig. 4g,i), we nucleofected gRNA–CAS9 ribonucleoprotein complexes full-length L1 and LTR subfamily transcripts (Fig. 5b,g). L1, LTRs, HERV-K
and used two independent pools of hESCs that showed ~50% dele- and HERV-L transcripts and protein-coding genes also show small but
tion efficiency (Extended Data Fig. 6c). Although CRISPRi for L1PA8 significant downregulation in MSL3-KD cells (Fig. 5e,f and Extended
resulted in the downregulation of both MOXD1 and STX7, genetic dele- Data Fig. 8d).
tion led to specific downregulation of MOXD1, but not STX7 and ENPP1
(Fig. 4h,k). Deletion of another H4K16ac+ L1PA7 located downstream of MSL/H4K16ac at TEs maintain active cis-regulatory landscape
RLN2, ~12 kb away from the RLN2 promoter, led to the downregulation H4K16ac causes chromatin decompaction in vitro, and depletion of
of RLN2 but not a nearby gene PLGRKT (Fig. 4i,k). Overall, CRISPRi and H4K16ac has been shown to reduce chromatin accessibility29,55. There-
genetic deletion experiments confirmed that H4K16ac+ L1s and LTRs fore, we asked whether the lack of H4K16ac leads to altered accessibility
are involved in regulation of transcription of genes in cis. at TEs. ATAC-seq data showed a specific reduction in accessible DNA
at the 5′ UTR of L1s in MSL3-depleted hESCs (Fig. 5g). In particular,
MSL and H4K16ac activate transcription of TEs evolutionarily younger L1s show a decrease in DNA accessibility, accom-
Next, we aimed to deplete H4K16ac to investigate whether it regulates panied by reduced transcriptional activity at these elements (Fig. 5g).
TE transcription. H4K16ac is catalyzed explicitly by KAT8 when asso- Genes closer to H4K16ac+ L1 and H4K16ac+ LTRs are significantly
ciated with the MSL complex, but not the NSL complex32–35 (Fig. 5a). highly expressed compared with genes farther away from these L1s and
Because depletion of the individual MSL complex proteins MSL1, MSL2 LTRs. By contrast, genes closer to H4K16ac– L1 and H4K16ac– LTRs show
and MSL3 is sufficient to reduce H4K16ac level54, we knocked down MSL3 significantly lower expression levels than farther genes (Fig. 6a,b). Next,
using two independent lentiviral small hairpin RNAs (shRNAs) in H9 we asked whether depletion of MSL/H4K16ac at L1 and LTRs affects
hESCs; we first validated the depletion by RT–qPCR, which showed ~50% the expression of genes located near these TEs marked with H4K16ac+
downregulation of MSL3. RT–qPCR with primers recognizing full-length TEs. MSL3 depletion led to a small but significant downregulation of
L1 subfamilies, such as human-specific (L1HS), mammalian-wide (L1M) many transcripts (n = 3,312) closer (<10 kb) to H4K16ac+ L1s (Fig. 6c).
and primate-specific (L1PA and L1PB) full-length L1s, showed significant Similarly, many transcripts that are closer (<10 and <25 kb) to H4K16ac+
downregulation upon MSL3 knockdown (KD). Similarly, RT–qPCR with LTRs are significantly downregulated compared to transcripts that are
primers recognizing HERV-K and HERV-H transcripts showed signifi- 25 to 50 kb away (Fig. 6d).
cant downregulation of HERV-H and HERV-K in MSL3-depleted hESCs Overall, our results confirm the role of MSL/H4K16ac at L1 and
(Fig. 5b). Western blotting confirmed that MSL3 depletion led to a spe- LTRs in transcriptional activation of TEs (Fig. 5b,d–f) and in regulating
cific reduction in H4K16ac but not H3K27ac (Fig. 5c and Supplementary genes that they are associated in linear distance or 3D space (Figs. 4 and
Fig. 1). Like the transcript data, L1-ORF1 protein (L1-ORF1p), encoded 6a–e). Therefore, we conclude that MSL complex-mediated acetylation
by full-length L1s (Fig. 1d) and HERV envelope protein (antibody raised of H4K16 leads to the opening of chromatin structure and increased
against ERVW-1) were also reduced upon MSL3 and H4K16ac deple- transcriptional activity at L1 and LTRs in a cell-type-specific manner.
tion (Fig. 5c), consistent with the high level of H4K16ac at L1 5′ UTRs The permissive local chromatin environment at H4K16ac+ TEs shapes
(Fig. 1d) and ERVW-1 locus (Fig. 4c). the cis-regulatory landscape across the mammalian genome (Fig. 6e).
We further used doxycycline-inducible Cas9 (iCAS9)-mediated
knockout (KO) of MSL1 in H1 hESCs (Fig. 5d) and in TDFs (Extended Data Discussion
Fig. 7) to confirm our findings from the shRNA-mediated MSL3 deple- TEs are repressed by many epigenetic pathways, such as DNA methyla-
tion. Immunofluorescence for H4K16ac and L1-ORF1 protein followed tion, H3K9me3, KRAB-ZNF, HUSH complex and piwi-interacting RNA
by high-content imaging revealed a significantly reduced number of (piRNAs). We have discovered that the MSL-H4K16ac axis functions as
Fig. 4 | H4K16ac+ L1 5′ UTRs function as enhancers to regulate genes in cis. as controls. j, Same as d, but for H4K16ac+ or H4K16ac– putative target genes
a, Illustration showing CRISPRi and CRISPR-mediated deletion strategy for for L1s (L1PA2 and L1MA2). TANC2, COMMD10, MOXD1, STX7, and USP38 were
TEs. Genes that show looping interaction (in RAD21-HiChIP data) and that are selected as putative target genes, along with CYB561, SEMA10A, ENPP1, GAB1, and
expressed in hESCs were chosen as putative targets for RT–qPCR, and other SMARCA5 were selected as putative non-targets. k, Same as j, but RT–qPCR was
nearby expressed genes were chosen as controls. b,c, Genome browser tracks done upon CRISPR–CAS9-mediated deletion of full-length L1. Two independent
showing H4K16ac and H3K27ac CUT&Tag data (CPM) at LTR7/HERV-H-int and clones for L1PA10 (H4K16ac+) and one for L1PA7 (H4K16ac+), L1PA2 (H4K16ac–)
LTR/ERV1 loci and their putative target genes. d, RT–qPCR data showing relative and L1MA2 (H4K16ac–) located at the upstream of USP38 were tested, and for
fold change (normalized to ACTB) in the expression of putative target genes L1PA7 located at MOXD1 and RLN2, the pools of cells were tested. For all RT–qPCR
NUS1 and PEX1 upon CRISPRi for HERV/LTRs, but not other nearby genes (GOPC experiments, data are shown as mean ± s.d. from n = 3 independent experiments;
and GATAD1). e–i. Like b and c, the genome browser track shows CUT&Tag data P values are from unpaired t-test with Welch correction; the two-stage step-up
at L1PA10 at the TANC2 locus, L1PA7 at the COMMD10 locus, L1PA7 at the MOXD1 (Benjamini, Krieger and Yekutieli) method was used, and the false-discovery rate
locus, L1PA10 and L1PA7 at the USP38 locus, and L1PA7 at the RLN2 locus. L1PA2 (FDR) was 1.00% for multiple comparisons. n.s., not significant.
and L1MA27 at the USP38 locus, which lack histone acetylation marks, were used
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 941
Article https://doi.org/10.1038/s41594-023-01016-5
a transcriptional activator of TEs, particularly L1s and LTRs. TEs have tissue-specific enhancers. Here, we have demonstrated that L1 5′ UTRs
contributed substantially to the evolution of mammalian genomes by and LTR/ERVs enriched with acetylated histones loop with genes, and
helping to shape both the coding and noncoding regulatory landscape. L1s and LTRs marked with H4K16ac function as enhancers to regulate
Several ERV/LTR subfamilies have been demonstrated to function as genes in cis.
a b c
CRISPR interference and deletions
30 kb (hg38) chr 6:117,650,000, 20 kb
CRISPRi: dCAS9-KRAB+ TE gRNAs chr7:92,470,000 92,500,000 117,660,000 (hg38)
HERVH-int
C C R A I S S 9 P R + g d R el N e A ti s ons: RAD21 HiChIP L H T E R R 7 V / H E - R in V t 1 PEX1 (60,00 G 0 O f P ro C m LTR LT ) R ERV1 NUS1
H4K16ac+ H4K16ac– 0.9 GATAD1 ERVW-1 H4K16ac 1.0
(exp c r i e s s n s o e n d - t in ar h g E e S t Cs; (exp T r a e r s g s e e t d g in e n h e E ? SCs; 1.8 H3K27ac 1.7
no 3D contact) LINE1, HERV/LTR 3D contact)
d
CRISPRi for H4K16ac+ HERV/LTRs
Non-target control
B 2.0 dCas9-KRAB + TE-gRNA
T C 0.041 n g e/ A 1.5 0 * .0 * 0 * 0 * 31 n.s. 0 * .0 * 17 *
h a 1.0
c d
ol 0.5
F
0
RT–qPCR NUS1 GOPC PEX1GATAD1 ZC3H15 ODF2L
CRISPRi HERVH-int HERVH-int HERVL- HERVL18
LTR ERV1 LTR7 / ERV1 LTR18 LTR18
f g h
100 kb (hg38)
chr6: 132,305,000
100 kb (hg38) chr17: 63,100,000 63,200,000 chr5: 116,090,000 116,110,000 20 kb (hg38) ENPP1 MOXD1 STX7
(500,000
COMMD10 from L1PA7) L1PA7 CAS9 cuts
0.6 H4K16ac TANC2 L1PA10 fro (2 C m 0 Y 0 L B , 1 5 0 P 6 0 A 1 0 10) 0.9 L1PA7 L1PB4 fr ( o S 13 m E 0 M L , A 0 1P 6 0 A A 0 7) 2. 1 5 H4K16ac
H3K122ac 0.9 H3K27ac 2.5 1 H3K27ac
1
H3K4me1
i j
n.s. CRISPR interference for L1 5′ UTRs
5 kb hg38
chr9:5,297,000 5,306,000
B 2.0
1 L1PA7 CAS R 9 L c N u 2 ts PLGRKT H 14 4 0 K ,0 1 0 6 0 a fr c om TE h a n g e/ A C T 1 1 . . 0 5 0 * .0 * 11 n.s. 0 * .0 * 0 * 0 * 01 0. * P 0 1 * = 0 30. * 0 P 0 * = 0 * 50 P = * 0 * .0 * 050 0. * 0 P 0 * = 0 * 69 n.s. n.s. n.s. n.s.
c
2.5 H3K122ac d ol 0.5
1 H3K27ac F
1 H3K4me1 0
RT–qPCR TANC2CYB561COMMD10SEMA6A MOXD1 STX7 ENPP1 USP38 GAB1SMARCA5 USP38USP38
CRISPRi L1PA10 L1PA7 L1PA7 L1PA10 L1PA2 L1MA2
H4K16ac–
k
CRISPR deletion of H4K16ac+ L1
P = 0.033
T B 1.5 ** * P P = = 0 0 . . 0 0 2 0 5 81 n.s n . .s n . .s. n.s n . .s. P = 0.000663 P = 0.000001
A C * P = 0.035 *** ****
e/ 1.0
g
n
a
h
c 0.5
d
ol
F
0
USP38 GAB1 SMARCA5 MOXD1 STX7 ENPP1 RLN2 PLGRKT
Control clone USP_L1PA10 Del-cl.2 MOXD_L1PA7 Del RLN2_L1PA7 Del
USP_L1PA10 Del-cl.1 USP_L1PA7 Del
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 942
MPC
MPC
MPC
MPC
HERVH/LTR – NUS1
HERVH/LTR7 – PEX1
100 kb (hg38)
USP38 CAS9 cuts CAS9 cuts
L1PA10 L1PA2 L1PA7 L1MA2
1.5
2.0
1.5
1
L1PA7 – MOXD1
L1PA10 – TANC2 L1PA7 – COMMD10
L1PA7 – RLN2
MPC
e
L1PA10/L1PA7/L1PA2/L1MA2 – USP38
chr4:143,100,000 143,200,000
n.s.
dCAS9-KRAB GAB1 SMARCA5 (270,000(440,000 n.s. from from L1PA10) L1PA10)
H4K16ac
H3K122ac
H3K27ac
H3K4me1
dCAS9-KRAB
* n.s. n.s. n.s.
Article https://doi.org/10.1038/s41594-023-01016-5
a b
1.0
0.5
0
c d
e
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 943
nitca-β/egnahc
dlof
evitaleR
P = 0.0221 P = 0.0109 P = 0.0101 P = 0.0535 P = 0.015 P = 0.00007 P = 0.023
WDR5 HCFC1
NSL2 KAT8 P = 0.0083 P = 0.0042 P = 0.0131 P = 0.0083 P = 0.0081 P = 0.00006 P = 0.040
MCRS1 hESC
KAT8 NSL1 NSL3 shControl
MSL2
MSL3 PHF20 shMSL3-1
MSL1 H4K8ac shMSL3-2
H4K5ac
H4K16ac H4K12ac
TEs? Gene
MSL1/H4K16ac depletion leads to reduced number of L1 ORF1 foci kDa
HERV/ P = 1.19 × 10–5
ERVW-1 55
L1 ORF1
7.5
35
55 α-Tubulin
5.0
15
H4K16ac
2.5
15 H3K27ac
iCAS9 hESC + Dox MSL1 gRNA DAPI L1-ORF1p H4K16ac
(H4K16ac+ cells (H4K16ac– cells
n = 800) n = 800)
C)
(F
L1 subfa m T il o y tal in H N G o 3 . 8 in clu F s r t a e c r t 1 i o a n n d o f 2 total AT A C-seq W H T 4 /K K D 16 l a o c g R 2 N l A o - g se ( 2 F q C) L1HS 0.45 I II L1PA2 0.55
L1PA3 0.31
L1PA4 0.20
L1PA5 0.16
L1PA6 0.13 III re d L1PA7 0.11
lO L1PA8 0.09
IV
–0.2 0.2 0.3–1 0 1
llec
rep
icof
1FRO
1L
1 × 101 1 × 10–1 1 × 10–3
log10(RPKM)
iCAS9 hESC iCAS9 hESC
+Dox +MSL1 gRNAs +Dox
13 µm
f g
P = 1.17 × 10–12 Genes L1 LTR P = 2.32 × 10–11 P = 1.28 × 10–30 P = 0 n.s. P = 1.21 × 10–6 1 × 101 1 × 104
1 × 10–1
1 × 102 1 × 10–3 P = 7.8 × 10–23
1 × 101
0 1 × 10–1
1 × 10–3
1 × 10–2 P = 1.39 × 10–7
1 × 101
1 × 10–1
1 × 10–3
)MKPR(
gol 01
* ** ** * * **** *
** ** ** ** ** **** *
MSL3 L1Hs L1PB L1M L1PA HERV-K HERV-H
Control MSL3-1 MSL3-2
sh sh sh
shControl shMSL3 shControl shMSL3 HERV-H HERV-K HERV-L n = 1,216 **** **** **** n = 2,405 1.8 * 5 P * × = * 10 * –11 P = n * 1 * = . 3 * 9 6 3 * 2 × 10–6
1 × 101
0
1 × 10–1
1 × 10–2
1 × 10–3
regnuoY 353 158 1,144 634
1,717 532
1,524 298
1,138 179
950 125 1,096 121
396 37
–1,500 Start 6,500
Fig. 5 | MSL activates transcription of TEs. a, Illustration showing that KAT8 wells. Data are representative of n = 2 independent experiments; P values were
catalyzes H4K16ac only when bound to the MSL complex, not the NSL complex. calculated using Welch’s t-test with 95% confidence interval. Scale bar, 13 µm.
b, RT–qPCR data from hESCs showing mean fold change (normalized to e, Violin plots showing RNA-seq for genes, full-length L1s, and LTRs for control
β-actin) in MSL3, L1 and HERV subfamilies upon lentiviral shRNA-mediated KD and MSL3-KD hESCs (n = 4). f, RNA-seq signal at HERV subclasses HERV-K,
of MSL3 using two independent shRNAs, versus hESCs transfected with a non- HERV-H, and HERV-L. g, Left, heatmaps showing H4K16ac (CPM), ATAC-seq (CPM)
targeted control shRNA. Data are shown as mean ± s.d. from n = 3 independent and RNA-seq (log(fold change)) for control/MSL3 KD in hESCs, n = 4) across
2
experiments; P values were calculated using an unpaired t-test with Welch full-length L1 with K-means clusters. The distribution of L1 subfamily members in
correction; the two-stage step-up (Benjamini, Krieger and Yekutieli) method was clusters 1 and 2 is shown on the left; multi-mapped reads were retained for these
used, and the FDR was 1% for multiple comparisons. c, Western blots showing heatmaps. Right, violin plots showing RNA-seq signal (log (reads per kilobase
10
HERV, L1-ORF1, and H4K16ac levels after shRNA-mediated knockdown of of transcript, per million mapped reads, RPKM), control and MSL3-KD hESCs)
MSL3 described in b; α-tubulin and H3K27ac served as controls in control and at four L1 clusters. In all box plots, center lines indicate the median, bounds
MSL3-KD hESCs (data are representative of n = 2 independent experiments; indicate the 25th and 75th percentiles and whisker limits show 1.5 × interquartile
uncropped images are in Supplementary Data Fig. 1). d, Representative images range. P values for all the violin and box plots were calculated using the pairwise
(right) and quantification of high-content (automated microscopy) imaging two-sided multi-comparison Dunn test, used for post-hoc testing following the
data (left) showing the number of L1 ORF1p foci per cell in H4K16ac+ and Kruskal–Wallis test, with Bonferroni correction.
H4K16ac– MSL1-KO cells. Eight hundred cells per condition were analyzed in two
Article https://doi.org/10.1038/s41594-023-01016-5
a
LTR K16ac–
P = 1.07 × 10–58
**** P = 2.96 × 10–91 P = 1.34 × 10–4 **** *** P = 5.42 × 10–14P = 3.04 × 10–21P = 4.86 × 10–28 **** **** ****
1 × 102
0
1 × 10–2
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1
0,
1 0, 0 0
0–25,
25, 0 0
0–5
0,
5 0, 0 0
0–1
0
0,
1
0,
1 0, 0 0
0–25,
25, 0 0
0–5
0,
5 0, 0 0
0–1
0
0,
1
0,
1 0, 0 0
0–25,
25, 0 0
0–5
0,
5 0, 0 0
0–1
0
0,
1
0,
1 0, 0 0
0–25,
25, 0 0
0–5
0,
5 0, 0 0
0–1
0
0,
n = 24,846 n = 9,888 n = 7,222
c d
e
MSL/KAT8
MSL/KAT8
Genes L1/LTR LINE1
Roadmap epigenomics data have shown that TEs are depleted of be independent of H3K27ac. Our CUT&Tag data show that the level of
H3K27ac and accessible chromatin; only 3% of TE bases are annotated H3K27ac is much higher at genes and promoters than at TEs. However,
with active regulatory chromHMM states, compared with 32% of pro- H4K16ac is enriched explicitly at the L1 5′ UTRs, along with several other
moter bases56. Despite that, TEs contribute up to 40% of TF-binding chromatin features associated with active enhancers. We now dem-
sites; hence, TEs have been proposed to contribute to species- and onstrate that L1 5′ UTRs marked with H4K16ac along or together with
tissue-specific rewiring of gene regulatory networks57–59. This suggests H3K122ac and H3K27ac function as enhancers to regulate the expres-
that an unknown chromatin pathway could contribute to the enhancer sion of genes in cis. Although L1s are expressed at higher levels during
activity of TEs in a cell-type- or species-specific manner, which could early development, including stem cells, they are also upregulated in
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 944
)MKPR(
gol
01
LINE1 K16ac+ LINE1 K16ac–
P = 9.74 × 10–5
**** ****
P = 3.28 × 10–1 n.s. P = 1.59 × 10–3 ** P = 3.28 × 10–1 P = 2.25 × 10–5 n.s. P = 7.81 × 10–1 n.s. **** 1 × 105
1 × 102
1 × 101
n = 1,303 n = 596 n = 980 n = 1,921 n = 1,054 n = 1,140 n = 2,072
)MKPR(
gol
01
b
LTR K16ac+
P = 6.10 × 10–69 P = 0
P = 9.76 × 10–1 n.s. **** P = 3.21 × 10–72 P P = = 6 3 * .4 .2 * 3 4 * × × * 1 1 0 0 – – 4 3 6 0 P = 9. n 76 .s . × 10–1P = 5. n 4 . 4 s . × 10–1 P = 1.43 × * 10 P * – = 2 * 4 0 7 * P = 7 * .5 * 0 * × * 10–14 P * * = 2 * * . * 3 * 8 * × * 10–25 **** ****
n = 18,998 n = 7,619 n = 7,607 n = 7,943
shControl shMSL3 shControl shMSL3
Distance from full-length L1 Distance from H4K16ac+ LTRs
P = 0.028 P = 0.20 P = 0.42 P = 5.12 × 10–8 P = 7.95 × 10–5 P = 0.053
n.s. n.s. 1 × 104 n.s.
1 × 102
1 × 102
0
0
1 × 10–2 1 × 10–2
<10 kb 10−25 kb 25−50 kb <10 kb 10−25 kb 25−50 kb
(n = 3,312) (n = 1,823) (n = 2,864) (n = 39,617) (n = 18,499) (n = 9,356)
)MKPR(
gol
01
n = 659 n = 12,503
* **** ****
LTR
H4K16ac H3K27ac H3K122ac H3K4me1 H3K4me3 H3K9me3 DNA methylation TFs
Fig. 6 | H4K16ac maintains an active chromatin landscape at TEs. a, Violin overlapping LTRs. e, The working model shows MSL/KAT8-mediated H4K16ac
plots showing the distance-dependent effect on the expression of genes from maintains accessible chromatin, activates transcription at TEs, and contributes
L1 with H4K16ac peaks (H4K16ac+) (left). Genes close to L1 that lack detectable to their enhancer activity to regulate genes in cis. In all box plots, center lines
H4K16ac peaks (H4K16ac–) are in TDF cells (right). X–axis shows the distance indicate the median, bounds indicate the 25th and 75th percentiles, and whisker
from the TEs. b, Like a, but for LTRs. c, hESC RNA-seq signals for control limits show 1.5 × interquartile range. P values for all the violin and box plots were
(shControl) and MSL3 knockdown (shMSL3) at genes that lie 10 kb, 10–25 kb, or calculated using the pairwise two-sided multi-comparison Dunn test, used for
25–50 kb away from the H4K16ac-overlapping full-length L1s. d, Like c, RNA-seq post hoc testing following the Kruskal–Wallis test with Bonferroni correction.
signals at genes that lie in 10 kb, 10–25 kb or 25–50 kb away from the H4K16ac-
Article https://doi.org/10.1038/s41594-023-01016-5
cancer and the neuronal lineage. Consistently, we found that H4K16ac the specific role of H4K16ac in neuronal cell types will reveal whether
is enriched at L1 5′ UTRs in human and mouse stem cells, cancer cell H4K16ac dysregulation could contribute to neuronal-specific dysregu-
lines, and post mortem brain tissues, suggesting that 5′ UTRs of L1s lation of TEs and gene expression, contributing to neurodevelopmental
bound by tissue-specific TFs and enriched with histone acetylations and neurodegenerative disorders.
could function as tissue-specific enhancers. Enrichment of H4K16ac In yeast, H4K16ac regulates lifespan and cellular senescence70.
at TEs, which constitute a major part of the mammalian genome, is Senescent cells show enrichment of H4K16ac in promoter regions
consistent with findings showing that nearly 30% of the histone H4 is of expressed genes71. Analysis of publicly available H4K16ac ChIP–
acetylated at H4K16 (ref. 34). seq data showed a dramatic loss of H4K16ac across L1s and LTRs in
Many LTR subfamilies are enriched with active enhancer associ- senescent cells in comparison with proliferating cells (Extended Data
ated chromatin features indicating that they could function as active Fig. 9), suggesting that proliferating cells, compared with replicative
enhancers. It has been proposed that some of the LTR subfamilies are senescent cells, have adapted to the permissive chromatin state at TEs.
essential in driving the expression of lineage-specific genes43,57. How- However, by contrast, L1 elements are known to be transcriptionally
ever, only a minority of putative RLTR13D6 subfamily-derived enhanc- derepressed during cellular senescence and to activate the interferon
ers identified through epigenomic analyzes have been experimentally I (IFN-I) response72. Further investigation will be needed to understand
validated to function as enhancers17. This highlights the importance of the direct role of the H4K16ac pathway in regulating L1 transcription
functional validations using CRISPR-based perturbation of candidate linked to aging and senescence.
TEs enriched with enhancer chromatin features. Although we found all In summary, we show that H4K16ac-marked L1s and LTRs act as
of the tested CRISPR-edited H4K16ac+ L1s downregulated their putative enhancers to regulate genes in cis. The act of transcription at L1 5′
target genes in cis. Genome-wide enhancer reporter assays, in combina- UTRs and LTRs mediated by H4K16ac could contribute to chromatin
tion with systematic genome-scale perturbation, are needed to identify topology and enhancer-mediated regulation of host gene expression
what fraction of L1s and LTRs with H4K16ac function as enhancers. in cis, as L1 and LTRs that are marked with histone acetylations are
TEs with acetylation marks, including H4K16ac, are bound by located within the regulatory elements, or they interact with genes. The
looping factors, including CTCF, RAD21, YY1, and ZNF143. Moreover, permissive chromatin structure mediated by H4K16ac and H3K122ac
the fraction of these TEs that loop with genes is significantly larger could counteract the epigenetic repressive environment at TEs within
than the fraction of TEs without acetylation marks that do so, further the regulatory elements (Fig. 6e)73.
supporting the role of transcriptionally active TEs in rewiring the regu-
latory landscape in a species- and cell-type-specific manner.53. Since Online content
our results show that the MSL-H4K16ac axis drives transcription at TEs, Any methods, additional references, Nature Portfolio reporting sum-
including HERVs (Fig. 5b,f and Extended Data Fig. 4b), we hypothesize maries, source data, extended data, supplementary information,
that MSL-H4K16ac-mediated transcription at TEs likely contributes to acknowledgements, peer review information; details of author contri-
the rewiring of 3D chromatin organization at transcriptionally active butions and competing interests; and statements of data and code avail-
TEs, as RNA polymerase II transcription drives enhancer-promoter con- ability are available at https://doi.org/10.1038/s41594-023-01016-5.
tact60. The factors contributing to the recruitment of the MSL complex
to the specific genomic region are unknown in mammals. Intriguingly, References
the role of MSL complex in co-opting TEs to rewire cis-regulatory ele- 1. Hancks, D. C. & Kazazian, H. H. Roles for retrotransposon
ments appears to have been conserved during the evolution of dosage insertions in human disease. Mob. DNA 7, 9 (2016).
compensation in Drosophila miranda, in which a mutant helitron TE has 2. Burns, K. H. Transposable elements in cancer. Nat. Rev. Cancer 17,
been shown to recruit the MSL complex to the evolutionarily young X 415–424 (2017).
chromosome to increase transcription61. In Drosophila dosage compen- 3. Molaro, A. & Malik, H. S. Hide and seek: how chromatin-based
sation, expression of most X-linked genes is increased approximately pathways silence retroelements in the mammalian germline.
twofold by H4K16ac, specifically in males62. This MSL-mediated X Curr. Opin. Genet. Dev. 37, 51–58 (2016).
upregulation appears to be conserved in mammals, in which H4K16ac 4. Almeida, M. V., Vernaz, G., Putman, A. L. K. & Miska, E. A. Taming
has been shown to upregulate genes on the single active X chromosome transposable elements in vertebrates: from epigenetic silencing
to balance expression with two copies of the autosomes63. Interestingly, to domestication. Trends Genet. 38, 529–553 (2022).
X chromosomes have a higher number of L1s than autosomes64, sug- 5. Karimi, M. M. et al. DNA methylation and SETDB1/H3K9me3
gesting that MSL-H4K16ac at L1s in the X chromosome could contribute regulate predominantly distinct sets of genes, retroelements,
to X upregulation. and chimeric transcripts in mescs. Cell Stem Cell 8, 676–687
TFs enriched at H4K16ac+ TEs (Fig. 3a and Extended Data Fig. 5) (2011).
could contribute to maintaining MSL-H4K16ac and transcription at TEs. 6. Robbez-Masson, L. et al. The HUSH complex cooperates with
Notably, the MSL complex recruits YY1 to the Tsix promoter to activate TRIM28 to repress young retrotransposons and new genes.
its expression in mESCs32, suggesting a possible interplay between MSL Genome Res. 28, 836–845 (2018).
and YY1 in regulating L1 transcription. Interestingly, MAFK, which has 7. Rowe, H. M. et al. KAP1 controls endogenous retroviruses in
previously been reported to be enriched at TEs59, is enriched explicitly embryonic stem cells. Nature 463, 237–240 (2010).
at H4K16ac+ L1 5’ UTRs, suggesting a potential interplay between MAFK 8. Bulut-Karslioglu, A. et al. Suv39h-dependent H3K9me3 marks
and MSL complex. intact retrotransposons and silences LINE elements in mouse
Neuronal cells have high L1 expression and retrotransposition65; embryonic stem cells. Mol. Cell 55, 277–290 (2014).
retrotransposon dysregulation is also linked with neurological dis- 9. Walsh, C. P., Chaillet, J. R. & Bestor, T. H. Transcription of IAP
orders1. TEs and their transcriptional regulators play wider roles in endogenous retroviruses is constrained by cytosine methylation.
shaping transcriptional networks during early human development66 Nat. Genet. 20, 116–117 (1998).
Loss of function mutations in genes encoding KAT8 containing protein 10. Hermant, C. & Torres-Padilla, M. E. TFs for TEs: the transcription
complexes such as KANSL1, MSL3 and KAT8 lead to neurodevelopmental factor repertoire of mammalian transposable elements. Genes
disorders37,67–69. Enrichment of H4K16ac at the 5′ UTRs of L1s in human Dev. 35, 22–39 (2021).
brain tissues suggests that altered gene expression programme due 11. Jacques, P. É., Jeyakani, J. & Bourque, G. The majority of
to TE dysregulation in the nervous system could be a possible mecha- primate-specific regulatory sequences are derived from
nism for these disorders (Extended Data Fig. 3)42. Further studies on transposable elements. PLoS Genet. 9, e1003504 (2013).
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 945
Article https://doi.org/10.1038/s41594-023-01016-5
12. Vierstra, J. et al. Mouse regulatory DNA landscapes reveal 34. Radzisheuskaya, A. et al. Complex-dependent histone
global principles of cis-regulatory evolution. Science 346, acetyltransferase activity of KAT8 determines its role
1007–1012 (2014). in transcription and cellular homeostasis. Mol. Cell 81,
13. Jachowicz, J. W. et al. LINE-1 activation after fertilization regulates 1749–1765 (2021).
global chromatin accessibility in the early mouse embryo. Nat. 35. Chatterjee, A. et al. Acetyl transferase regulates transcription and
Genet. 49, 1502–1510 (2017). respiration in mitochondria. Cell 167, 722–738 (2016).
14. Upton, K. R. et al. Ubiquitous L1 mosaicism in hippocampal 36. Li, X. et al. The histone acetyltransferase MOF is a key regulator of
neurons. Cell 161, 228–239 (2015). the embryonic stem cell core transcriptional network. Cell Stem
15. Fueyo, R., Judd, J. & Feschotte, C. Roles of transposable elements Cell 11, 163–178 (2012).
in the regulation of mammalian transcription. Nat. Rev. Mol. Cell 37. Basilicata, M. F. et al. De novo mutations in MSL3 cause an
Biol. 24, 19–24 (2022). X-linked syndrome marked by impaired histone H4 lysine 16
16. Sundaram, V. & Wysocka, J. Transposable elements as a acetylation. Nat. Genet. 50, 1 (2018).
potent source of diverse cis-regulatory sequences in 38. Li, L. et al. Lysine acetyltransferase 8 is involved in cerebral
mammalian genomes. Philos. Trans. R. Soc. B Biol. Sci. 375, development and syndromic intellectual disability. J. Clin. Invest.
20190347 (2020). 130, 1431–1445 (2020).
17. Todd, C. D, Taylor, D. & Branco, M. R. Functional evaluation of 39. Kaya-okur, H. S. et al. CUT&Tag for efficient epigenomic
transposable elements as enhancers in mouse embryonic and profiling of small samples and single cells. Nat. Commun. 10,
trophoblast stem cells. eLife 8, e44344 (2019). 1930 (2019).
18. He, J. et al. Transposable elements are regulated by 40. Ernst, J. & Kellis, M. ChromHMM: automating chromatin-state
context-specific patterns of chromatin marks in mouse discovery and characterization. Nat. Methods 9, 215–216 (2012).
embryonic stem cells. Nat. Commun. 10, 34 (2019). 41. Larschan, E. et al. X chromosome dosage compensation via
19. Percharde, M. et al. A LINE1-nucleolin partnership regulates early enhanced transcriptional elongation in Drosophila. Nature 471,
development and ESC identity. Cell 174, 391–405 (2018). 115–118 (2011).
20. Schmidt, D. et al. Waves of retrotransposon expansion remodel 42. Nativio, R. et al. Dysregulation of the epigenetic landscape
genome organization and CTCF binding in multiple mammalian of normal aging in Alzheimer’s disease. Nat. Neurosci. 21,
lineages. Cell 148, 335–348 (2012). 1018 (2018).
21. Chuong, E. B., Elde, N. C. & Feschotte, C. Regulatory activities of 43. Fuentes, D. R., Swigut, T. & Wysocka, J. Systematic perturbation of
transposable elements: from conflicts to benefits. Nat. Rev. Genet. retroviral LTRs reveals widespread long-range effects on human
18, 71–86 (2017). gene regulation. eLife 7, 1–29 (2018).
22. Creyghton, M. P. et al. Histone H3K27ac separates active from 44. Pontis, J. et al. Hominoid-specific transposable elements and
poised enhancers and predicts developmental state. Proc. Natl KZFPs facilitate human embryonic genome activation and
Acad. Sci. USA 107, 21931–21936 (2010). control transcription in naive human ESCs. Cell Stem Cell 24,
23. Buenrostro, J. D., Giresi, P. G., Zaba, L. C., Chang, H. Y. & Greenleaf, 724–735 (2019).
W. J. Transposition of native chromatin for fast and sensitive 45. Lee, D. et al. STARRPeaker: uniform processing and accurate
epigenomic profiling of open chromatin, DNA-binding proteins identification of STARR-seq active regions. Genome Biol. 21,
and nucleosome position. Nat. Methods 10, 1213–1218 (2013). 298 (2020).
24. Andersson, R. et al. An atlas of active enhancers across human 46. Athanikar, J. N., Badge, R. M. & Moran, J. V. A YY1-binding site
cell types and tissues. Nature 507, 455–461 (2014). is required for accurate human LINE-1 transcription initiation.
25. Deniz, Ö. et al. Endogenous retroviruses are a source of Nucleic Acids Res. 32, 3846–3855 (2004).
enhancers with oncogenic potential in acute myeloid leukaemia. 47. Macfarlan, T. S. et al. Endogenous retroviruses and neighboring
Nat. Commun. 11, 3506 (2020). genes are coordinately repressed by LSD1/KDM1A. Genes Dev. 25,
26. Kheradpour, P. et al. Systematic dissection of regulatory motifs 594–607 (2011).
in 2000 predicted human enhancers using a massively parallel 48. Xu, H. et al. Cohesin Rad21 mediates loss of heterozygosity and is
reporter assay. Genome Res. 23, 800–811 (2013). upregulated via Wnt promoting transcriptional dysregulation in
27. Taylor, G., Eskeland, R., Hekimoglu-Balkan, B., Pradeepa, M. gastrointestinal tumors. Cell Rep. 9, 1781–1797 (2014).
& Bickmore, W. A. H4K16 acetylation marks active genes and 49. Sun, X. et al. Transcription factor profiling reveals molecular
enhancers of embryonic stem cells, but does not alter chromatin choreography and key regulators of human retrotransposon
compaction. Genome Res. 23, 2053–2065 (2013). expression. Proc. Natl Acad. Sci. USA 115, E5526–E5535 (2018).
28. Wang, Z. et al. Prediction of histone post-translational 50. Weintraub, A. S. et al. YY1 is a structural regulator of
modification patterns based on nascent transcription data. Nat. enhancer-promoter loops. Cell 171, 1573–1588 (2017).
Genet. 54, 295–305 (2022). 51. Krietenstein, N. et al. Ultrastructural details of mammalian
29. Shogren-Knaak, M. et al. Histone H4-K16 acetylation controls chromosome architecture. Mol. Cell 78, 554–565 (2020).
chromatin structure and protein interactions. Science 311, 52. Lyu, X., Rowley, M. J. & Corces, V. G. Architectural proteins and
844–847 (2006). pluripotency factors cooperate to orchestrate the transcriptional
30. Tropberger, P. et al. Regulation of transcription through response of hESCs to temperature stress. Mol. Cell 71, 940–955
acetylation of H3K122 on the lateral surface of the histone (2018).
octamer. Cell 152, 859–872 (2013). 53. Zhang, Y. et al. Transcriptionally active HERV-H retrotransposons
31. Pradeepa, M. M. et al. Histone H3 globular domain acetylation demarcate topologically associating domains in human
identifies a new class of enhancers. Nat. Genet. 48, 681–686 pluripotent stem cells. Nat. Genet. 51, 1380–1388 (2019).
(2016). 54. Monserrat, J. et al. Disruption of the MSL complex inhibits tumour
32. Chelmicki, T. et al. MOF-associated complexes ensure stem cell maintenance by exacerbating chromosomal instability. Nat. Cell
identity and Xist repression. eLife 3, e02024 (2014). Biol. 23, 401–412 (2021).
33. Ravens, S. et al. Mof-associated complexes have overlapping and 55. Samata, M. et al. Intergenerationally maintained histone H4 lysine
unique roles in regulating pluripotency in embryonic stem cells 16 acetylation is instructive for future gene activation. Cell 182,
and during differentiation. eLife 2014, 1–23 (2014). 127–144 (2020).
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 946
Article https://doi.org/10.1038/s41594-023-01016-5
56. Pehrsson, E. C., Choudhary, M. N. K., Sundaram, V. & Wang, T. The 68. Shaw-Smith, C. et al. Microdeletion encompassing MAPT
epigenomic landscape of transposable elements across normal at chromosome 17q21.3 is associated with developmental
human development and anatomy. Nat. Commun. 10, 1–16 (2019). delay and learning disability. Nat. Genet. 38, 1032–1037 (2006).
57. Kunarso, G. et al. Transposable elements have rewired the core 69. Koolen, D. A. et al. Mutations in the chromatin modifier gene
regulatory network of human embryonic stem cells. Nat. Genet. KANSL1 cause the 17q21.31 microdeletion syndrome. Nat. Genet.
42, 631–634 (2010). 44, 639–641 (2012).
58. Sundaram, V. et al. Functional cis-regulatory modules encoded 70. Dang, W. et al. Histone H4 lysine 16 acetylation regulates cellular
by mouse-specific endogenous retrovirus. Nat. Commun. 8, lifespan. Nature 459, 802–807 (2009).
14550 (2017). 71. Rai, T. S. et al. HIRA orchestrates a dynamic chromatin landscape
59. Sundaram, V. et al. Widespread contribution of transposable in senescence and is required for suppression of neoplasia. Genes
elements to the innovation of gene regulatory networks. Genome Dev. 28, 2712–2725 (2014).
Res. 24, 1963–1976 (2014). 72. De Cecco, M. et al. L1 drives IFN in senescent cells and promotes
60. Zhang, S., Übelmesser, N., Barbieri, M. & Papantonis, A. age-associated inflammation. Nature 566, 73–78 (2019).
Enhancer-promoter contact formation requires RNAPII and 73. Liu, N. et al. Selective silencing of euchromatic L1s revealed
antagonizes loop extrusion. Nat. Genet. 55, 832–840 (2023). by genome-wide screens for L1 regulators. Nature 553,
61. Christopher, E. E. & Bachtrog, D. Dosage compensation via 228–232 (2018).
transposable element mediated rewiring of a regulatory network.
Science 342, 846–850 (2013). Publisher’s note Springer Nature remains neutral with
62. Conrad, T. & Akhtar, A. Dosage compensation in Drosophila regard to jurisdictional claims in published maps and
melanogaster: epigenetic fine-tuning of chromosome-wide institutional affiliations.
transcription. Nat. Rev. Genet. 13, 123–134 (2011).
63. Deng, X. et al. Mammalian X upregulation is associated Open Access This article is licensed under a Creative Commons
with enhanced transcription initiation, RNA half-life, and Attribution 4.0 International License, which permits use, sharing,
MOF-mediated H4K16 acetylation. Dev. Cell 25, 55–68 (2013). adaptation, distribution and reproduction in any medium or format,
64. Boyle, A. L., Ballard, S. G. & Ward, D. C. Differential distribution as long as you give appropriate credit to the original author(s) and the
of long and short interspersed element sequences in the mouse source, provide a link to the Creative Commons license, and indicate
genome: chromosome karyotyping by fluorescence in situ if changes were made. The images or other third party material in this
hybridization. Proc. Natl Acad. Sci. USA 87, 7757–7761 (1990). article are included in the article’s Creative Commons license, unless
65. Macia, A. et al. Engineered LINE-1 retrotransposition in indicated otherwise in a credit line to the material. If material is not
nondividing human neurons. Genome Res. 27, 335–348 (2017). included in the article’s Creative Commons license and your intended
66. Pontis, J. et al. Primate-specific transposable elements shape use is not permitted by statutory regulation or exceeds the permitted
transcriptional networks during human development. Nat. use, you will need to obtain permission directly from the copyright
Commun. 13, 7178 (2022). holder. To view a copy of this license, visit http://creativecommons.
67. Sharp, A. J. et al. Discovery of previously unidentified genomic org/licenses/by/4.0/.
disorders from the duplication architecture of the human
genome. Nat. Genet. 38, 1038–1042 (2006). © The Author(s) 2023
Nature Structural & Molecular Biology | Volume 30 | July 2023 | 935–947 947
Article https://doi.org/10.1038/s41594-023-01016-5
Methods (Thermo Fisher Scientific, NW04120BOX, NW00122BOX), blotted on
Cell culture and transduction a polyvinylidene fluoride (PVDF) membrane (BioRad, 1704156) and
The H9 hESC line was a gift from L. Vallier’s lab with the MTA from immunoblotted with antibodies to MSL3 (Merck Millipore, ABE467,
WiCell. hESCs were grown on geltrex-coated plates (Thermo Fisher 1:1,000 dilution), L1 ORF1 (Merck Millipore, MABC1152, 1:1,000 dilu-
Scientific, A1413302) in mTeSR Plus medium (Stem Cell Technologies, tion), H4K16ac (Abcam, ab109463, 1:5,000 dilution), H3K27ac (Abcam,
100-0276) supplemented with 100 U ml–1 penicillin–streptomycin ab4729, 1:5,000 dilution), ɑ-tubulin (Sigma, T9026, 1:5,000 dilution),
(Gibco, 15140122) and passaged every 3–4 d with ReLeSR (StemCell and HERV (Novus Biologicals, NB100-93579, 1:500 dilution), and horse-
Technologies, 100-0484), according to the manufacturer’s protocols. radish peroxidase (HRP)-conjugated goat anti-rabbit IgG H&L (Abcam,
The doxycycline-inducible SpCas9 (iCas9-H1) hES cells were generated ab6721) and HRP-conjugated goat anti-mouse H&L (Thermo Fisher
using parental H1-hESCs from WiCell. Briefly, H1 cells were transfected Scientific, 31430) secondary antibodies.
with plasmids from the Genome-CRISP Inducible Cas9 human AAVS1
Safe Harbor Knock-in Kit (GeneCopoeia) using Fugene HD (Promega) Immunofluorescence and imaging
and selected with Puromycin (500 ng ml–1). Cells were single-cell sorted Cells were grown on 24-well cell culture plates, fixed with 4% formalde-
using FACS and grown in mTESR to make monoclonal lines. The result- hyde, incubated for 5 min with permeabilization buffer (PBS containing
ing SpCas9 line was confirmed to be karyotypically normal and was 0.1% Triton X-100), and blocked with PBS containing 0.1% Triton X-100
tested for mycoplasma every 3 weeks. and 2% BSA) for 1 h. Primary antibodies to H4K16ac (Abcam, Ab109463,
Transformed dermal fibroblasts (TDF) expressing guide RNAs (3 1:500) and L1 ORF1 (Merck Millipore, MABC1152, 1:500 dilution) were
guides per pool) targeting MSL1 and MSL3 and parental (WT) TDF lines added overnight at 4 °C, washed three times with PBS (10 min each) and
were generated in P. Scaffidi’s lab (The Crick Institute). Cells were grown incubated with anti-rabbit secondary antibodies (Abcam, Ab150080,
in MEM (Gibco, 11095080) supplemented with 10% FBS (Sigma, F7524), 1:500) and DAPI (1:1000). After washing 3 times with PBS (10 min each),
1× Glutamax (Gibco, 35050061), 1× non-essential amino acid solution the cells were left in PBS and imaged with Incell2000.
(Sigma, M7145) and 100 U ml–1 penicillin–streptomycin.
iCAS9 cells were transduced with three lentiviral guide RNAs tar- CUT&Tag
geting MSL1 and MSL3 (ref. 54). Parental iCAS9 H1, iCAS9 with MSL CUT&Tag was performed according to Kaya-Okur et al.39 protocol with
guide RNAs, TDF iCas9 transduced with MSL1, and MSL3 guide RNA modifications to tissue processing, as described below. Experiments
pools were treated with 1 µg ml–1 doxycycline (Sigma) to generate were performed in biological duplicates from each cell type. Approxi-
the inducible MSL-KO lines. After 4 to 7 d of doxycycline induction, mately 100,000 cells were pelleted by centrifugation for 3 min at 600g
the knockout was validated by immunofluorescence followed by at room temperature and resuspended in 500 µl of ice-cold NE1 buffer
high-content microscopy and western blot using antibodies to H4K16ac (20 mM HEPES-KOH pH 7.9, 10 mM KCl, 0.5 mM spermidine, 1% Triton
and H3K27ac. X-100, and 20 % glycerol and cOmplete EDTA free protease inhibitor
HEK293T cells were grown in DMEM, high glucose (Lonza, BE12- tablet) and were left to sit for 10 min on ice. Nuclei were pelleted by
614Q), supplemented with 10% FBS (Sigma, F7524), 1× Glutamax (Gibco, centrifugation for 4 min at 1,300g at 4 °C, resuspended in 500 µl of wash
35050061) and 100 U/ml penicillin–streptomycin. HEK293 and HeLa buffer, and held on ice until beads were ready. The required amount
cells were grown in DMEM, high glucose (Lonza, BE12-614Q) supple- of BioMag Plus Concanavalin-A-conjugated magnetic beads (ConA
mented with 10% FBS (Sigma, F7524), 1× Glutamax (Gibco, 35050061) beads, Polysciences) was transferred into the binding buffer (20 mM
and 100 U ml–1 penicillin–streptomycin. PC3 and LNCaP cells were HEPES-KOH pH 7.9, 10 mM KCl, 1 mM CaCl and 1 mM MnCl) and washed
2 2
grown in RPMI medium (Gibco, 21875034) supplemented with 10% FBS once in the same buffer; each time they were placed on a magnetic rack
(Sigma, F7524) and 100 U ml–1 penicillin–streptomycin. RWPE1 cells to allow the beads to separate from the buffer and resuspended in bind-
were grown in a keratinocyte serum-free medium (Gibco, 10724011) ing buffer. Then, 10 µl of beads was added to each tube containing cells
supplemented with 100 U ml–1 penicillin–streptomycin. K562 cells were and rotated on an end-to-end rotator for 10 min. After a quick spin to
grown in Iscove’s Modified Dulbecco’s Medium (Lonza, BE12-722F) sup- remove liquid from the cap, tubes were placed on a magnet stand to be
plemented with 10% FBS (Sigma, F7524) and 100 U ml–1 penicillin–strep- cleared, the liquid was withdrawn, and 800 µl of antibody buffer con-
tomycin. SH-SY5Y cells were grown in DMEM/F12 (1:1) medium (Gibco, taining 1 µg of the following primary antibodies was added: normal rab-
11320033) supplemented with 10% FBS (Sigma, F7524) and 100 U ml–1 bit IgG (Santa Cruz Cat no sc-2027), H3K27ac (Abcam, ab4729), H4K16ac
penicillin–streptomycin. All the cell lines were tested for mycoplasma (Abcam, ab109463), H3K122ac (Abcam, ab33309), H3K4me1 (Abcam,
contamination using EZ-PCR Kit (Geneflow, K1-0210). ab8895), H3K36me3 (Abcam, ab9050)) H3K4me3 (Millipore, 07-473),
For the generation of MSL3 stable knockdown H9 hESCs, cells were H3K27me3 (Abcam, ab192985) and H3K9me3 (Abcam, ab176916)). The
transduced with lentiviral particles (Sigma, Mission shRNAs, MSL3 sh1 mixture was incubated at 4 °C overnight in a nutator. Secondary anti-
TRCN0000022105, MSL3 sh2 TRCN0000022107) and mammalian bodies (guinea pig α-rabbit antibody, Antibodies online, ABIN101961)
nontargeting shRNA (SHC002V) at an MOI of 6. At 48 h after transduc- were added 1:100 in Dig-wash buffer (5% digitonin in wash buffer), and
tion, cells were selected with 0.5 µg ml–1 puromycin (Gibco, A1113803) 100 µl was squirted in per sample while they were gently vortexed, to
for 48 h, and surviving cells were then allowed to recover until they allow the solution to dislodge the beads from the sides, followed by
formed viable colonies. incubation for 60 min on a nutator. Unbound antibodies were washed
in 1 ml of Dig-wash buffer three times. Then, 100 µl of (1:250 diluted)
Western blotting protein-A-Tn5 loaded with adapters in Dig-300 buffer (20 mM HEPES
Cells were pelleted by centrifugation at 228g for 5 min at 4 °C and pH 7.5, 300 mM NaCl, 0.5 mM spermidine with Roche cOmplete EDTA
resuspended in RIPA buffer (150 mM sodium chloride, 1.0% NP-40, or free protease inhibitor) was added to the samples, placed on nutator
Triton X-100, 0.5% sodium deoxycholate, 0.1% SDS (sodium dodecyl for 1 h and washed three times in 1 ml of Dig-300 buffer to remove
sulfate) and 50 mM Tris, pH 8.0) and protease inhibitors with ben- unbound pA-Tn5. Next, 300 µL Tagmentation buffer (Dig-300 buffer +
zonase (Novagen; final concentration, 1.25 U µl–1) and incubated for 5 mM MgCl) was added while being gently vortexed, and samples were
2
30 min on ice with intermittent mixing. Extracts were sonicated for 5 incubated at 37 °C for 1 h on an incubator. Tagmentation was stopped by
cycles with Bioruptor (Diagenode) with the 30 s on and 30 s off cycles, adding 10 µl 0.5 M EDTA, 3 µl 10% SDS, and 2.5 µl 20 mg ml–1 Proteinase
and were cleared by centrifugation at 15,500g for 10 min at 4 °C. Equal K to each sample. Samples were mixed by full-speed vortexing for ~2 s
amounts of protein extract were denatured in 1× Bolt LDS sample buffer and incubated for 1 h at 55 °C to digest proteins. DNA was purified by
(Thermo Fisher Scientific, B0007) and separated on Bolt Bis-Tris gels phenol:chloroform extraction using phase-lock tubes (Quanta Bio)
Nature Structural & Molecular Biology
Article https://doi.org/10.1038/s41594-023-01016-5
followed by ethanol precipitation. Libraries were prepared using NEB- (PB_tre_dCas9_KRAB, Addgene ID 126030) (ref. 74), a kind gift from J.
Next HiFi 2× PCR Master mix (M0541S) with a 72 °C gap-filling step, Mauro Calabrese, was mixed with the piggyBac-transposase plasmid
followed by 13 cycles of PCR with 10-second combined annealing and in a 1:1 ratio (2 µg in each well of a 6-well plate) into opti-MEM, along
extension for the enrichment of short DNA fragments. Libraries were with TransIT-LT1 in a 1:3 ratio (Mirus, MIR2300), and reverse transfected
sequenced in Novaseq 6000 (Novogene) with 150 bp paired-end reads. into H9 hESCs according to manufacturer’s protocol. The next day, the
cells were allowed to recover from the transfection for 24 h and then
RT–qPCR selected with 100 µg ml–1 hygromycin B for 5 d. Surviving colonies were
Total RNA was isolated from H9 hESCs using TRIzol reagent (Ther- then expanded and reverse-transfected with various gRNA-expressing
moFisher Scientific, 15596026). For RT–qPCR, cDNAs were prepared plasmids (cloned into pSLQ1371 as described in ref. 75, kind gift from
with LunaScript RT SuperMix Kit (NEB, E3010). For CRISPRi experi- S. Qi) with TransIT-LT1. Then, 1.25 × 106 cells were reverse transfected
ments, RNA isolation was done using a kit (Monarch, T2040S) followed with 1 µg of the gRNA-expressing plasmid (per well of a 24-well plate).
by reverse transcription using LunaScript RT SuperMix Kit (NEB, E3010), To improve the efficiency of plasmid delivery, the transfection was
qPCR using qPCRBIO SyGreen Mix Lo-ROX (PCRBio) in LightCycler repeated the next day (forward transfection). At 48 h after the first
480 instrument (Roche). The list of specific primers used is given in transfection, cells were briefly selected with puromycin (0.5 µg ml–1)
Supplementary Table 4. RT–qPCR was done with three independent bio- for 24 h and left to recover for 96 h. Cells were collected for RNA isola-
logical replicates, each of control shRNA and two independent shRNAs tion and RT–qPCR.
targeting MSL3 or relevant empty vector controls and dCAS9 systems
for CRISPRi, on a StepOnePlus Real-Time PCR System (Applied Biosys- CRISPR–Cas9 deletion of LINE1 elements in hESCs
tems). Data were normalized to β-actin from three biological replicates. Two crRNAs performed LINE1 element deletions and were designed
to target nonrepetitive flanking sites of the LINE1 elements (Supple-
RNA sequencing mentary Table 5). Individual crRNAs were mixed with tracerRNAs Alt-R
RNA was isolated using Monarch RNA mini prep kit (NEB) with genomic CRISPR–Cas9 tracrRNA, ATTO 550, and with CAS9 protein (Alt-R S.p.
DNA elimination column and on-column DNase treatment. MSL3 KD HiFi Cas9 Nuclease V3) to form ribo-nucleocomplex. Then, 200,000
RNA sequencing libraries were prepared by spiking in equal amounts H1 hESCs per well were nucleofected in the presence of Alt-R Cas9
of The External RNA Controls Consortium (ERCC) Spike-in RNA Variant Electroporation Enhancer in 16 strips format using primary cell kit (P3).
Control Sets (SIRV set 3, Lexogen), and 500 ng of RNA was used for deple- hESCs were electroporated using a 4D nucleofector, the P3 Primary
tion of rRNA using RiboCOP kit (Lexogen), followed by RNA-seq library Cells 4D-Nucleofector X kit S (Lonza, LOV4XP3032), with the pulse pro-
preparation using CORALL Total RNA-Seq Library Prep Kit (Lexogen). gram. After nucleofection, cells were resuspended in an hESC medium
Libraries were sequenced as 150 bp paired-end reads using Novaseq supplemented with ROCK inhibitors and seeded to geltrex-coated 96
6000. In the case of H1 iCAS9 and MSL1 KO RNA-seq, Ribosomal RNAs wells for 2 d at 37 °C in a humidified incubator with 5% CO. hESCs were
2
were depleted using NEBNext rRNA Depletion Kit (Human/Mouse/Rat) split into 96 wells and 6-well plates for picking of single-cell colonies.
(NEB no. E7400) followed by library preparation using NEBNext Ultra II The pool of cells 5 d after nucleofection was collected to check the
Directional RNA Library Prep Kit for Illumina (NEB no. E7765). deletion efficiency and for RT–qPCR. Cells were seeded in 6-well plates
for picking single-cell colonies; the deletion was assessed by rapid
ATAC-seq DNA lysis and PCR using PCRBIO Rapid Extract PCR kit (PB10.24-40).
ATAC-seq was performed as described in ref. 23, with modifications. The For deletion of L1s at MOXD1 and RLN2 locus, pools of cells that were
freshly collected 50,000 cells were washed in PBS and resuspended in a collected 5 d after nucleofection were used for RT–QPCR. PCR prod-
resuspension buffer (10 mM Tris-HCl, 10 mM NaCl, 3 mM MgCl2). Cells ucts were subjected to Sanger sequencing. Primer sequences used for
were resuspended and incubated on ice for 3 min in 50 µl of cold lysis screening are listed in Supplementary Table 4.
buffer (0.1% NP-40, 0.1% Tween-20, 0.01% digitonin in resuspension
buffer). Nuclei were washed in 1 ml of wash buffer (990 µl resuspension Analysis of CUT&Tag-seq data
buffer, 0.1% Tween-20) by inversion three times. Nuclei were pelleted Mapping. For the CUT&Tag-seq, 150-bp paired-end reads were
by centrifugation at 500g for 10 min at 4 °C. The nuclei were resus- trimmed for adapters using the Trimmomatic tool and aligned to
pended in 47.5 ml of Nextera Tagmentation buffer (Nextera DNA Sam- the hg38 genome through local Bowtie2 (version 2.4.5) with these
ple Preparation Kit) and incubated with 2.5 µl of the Tn5 transposase parameters for pair-end mapping:–very-sensitive-local–no-unal–
(Nextera kit, Illumina) at 37 °C for 30 min. The resulting DNA fragments no-mixed–no-discordant–phred33 -I 10 -X 700 (ref. 76). For analyzes,
were purified using a miniElute column (Qiagen) and amplified by multi-mapped reads were filtered out, and only uniquely mapped
NEBNext High-Fidelity PCR Master Mix in a total volume of 50 µl. The reads were retained with the samtools flag of -q 2 -f 0x200 (ref. 77). For
thermocycling protocol for this reaction was 72 °C for 5 min, 98 °C for Figure 5e, total reads, including multi-mapped reads, were retained
30 s and five cycles of 98 °C for 10 s, 63 °C for 30 s, and 72 °C for 1 min. for plotting heatmaps of ATAC-seq, CUT&Tag, and RNA-seq reads. For
The universal adapter primer and a unique barcoded adapter primer individual replicates, the bam files were sorted, indexed, and used for
(same as CUT&Tag primers) were used. To avoid over-amplification, generating bedgraphs (for peak calling) and bigwigs. The bam files
after the initial five cycles, the number of remaining cycles required were sorted and indexed using the samtools (version 1.9) sort and the
was estimated for each sample using qPCR by adding SYBRGreen and samtools index. Merging of multiple replicates was performed using
using 5 µl of the previous PCR as a template. The number of additional samtools merge. The sorted bam files were used to generate bed, bed-
cycles was determined to be the number that it took for the qPCR to graph and bigwig formats for individual modifications.
reach one-third of maximal fluorescence. The original PCR was then
resumed, and each sample was cycled as necessary. After amplifica- Peak calling and analyzes. The reads were extracted from the bam to
tion, the samples were purified using AMPure XP beads. The libraries bed by the bedtools bamtobed option78. Further reads were processed
were sequenced as a minimum of 50 million 150 bp paired-end reads as mentioned in the SEACR (version 1.3) manual to get the bedgraph79.
in Novoseq (Novogene PLC). These bedgraph files were subjected to peak calling through SEACR
with a stringent P of ≤1 × 10–6 with the norm and relaxed options.
CRISPRi with dCAS9-KRAB Further bedtools with various options were used for transforming
CRISPRi using dCAS9-KRAB was performed as described in bed files, such as intersect, closest, sample, or shuffle. GNU awk editor
ref. 31, with the following modifications. The CRISPR-Bac plasmid was used for processing the bed files wherever required. Chromatin
Nature Structural & Molecular Biology
