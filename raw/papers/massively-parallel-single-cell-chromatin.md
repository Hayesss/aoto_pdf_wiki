---
source_path: /mnt/c/Users/Administrator/Zotero/storage/GYHFW453/Satpathy 等 - 2019 - Massively parallel single-cell chromatin landscapes of human immune cell development and intratumora.pdf
ingested: 2026-04-23
sha256: 1bc894344df01153
---

Articles
https://doi.org/10.1038/s41587-019-0206-z
Massively parallel single-cell chromatin
landscapes of human immune cell development
and intratumoral T cell exhaustion
Ansuman T. Satpathy 1,2,11, Jeffrey M. Granja1,3,4,11, Kathryn E. Yost1,5,6,
Yanyan Qi1,6, Francesca Meschi7, Geoffrey P. McDermott7, Brett N. Olsen7, Maxwell R. Mumbach1,3,
Sarah E. Pierce 3,5, M. Ryan Corces1,6, Preyas Shah7, Jason C. Bell7, Darisha Jhutty7, Corey M. Nemec7,
Jean Wang7, Li Wang7, Yifeng Yin7, Paul G. Giresi7, Anne Lynn S. Chang 6, Grace X. Y. Zheng 7*,
William J. Greenleaf 1,3,8,9* and Howard Y. Chang 1,3,6,10*
Understanding complex tissues requires single-cell deconstruction of gene regulation with precision and scale. Here, we assess
the performance of a massively parallel droplet-based method for mapping transposase-accessible chromatin in single cells
using sequencing (scATAC-seq). We apply scATAC-seq to obtain chromatin profiles of more than 200,000 single cells in
human blood and basal cell carcinoma. In blood, application of scATAC-seq enables marker-free identification of cell type-
specific cis- and trans-regulatory elements, mapping of disease-associated enhancer activity and reconstruction of trajectories
of cellular differentiation. In basal cell carcinoma, application of scATAC-seq reveals regulatory networks in malignant, stromal
and immune cells in the tumor microenvironment. Analysis of scATAC-seq profiles from serial tumor biopsies before and after
programmed cell death protein 1 blockade identifies chromatin regulators of therapy-responsive T cell subsets and reveals a
shared regulatory program that governs intratumoral CD8+ T cell exhaustion and CD4+ T follicular helper cell development. We
anticipate that scATAC-seq will enable the unbiased discovery of gene regulatory factors across diverse biological systems.
C
ell type-specific gene expression in eukaryotic cells is regu- the single-cell chromatin accessibility landscape of blood formation
lated by millions of cis-acting DNA elements (for example, in bone marrow and blood samples from healthy humans, which
enhancers and promoters) and thousands of trans-acting revealed chromatin states of progenitor cells and the regulatory tra-
factors (for example, transcription factors (TFs))1. We previously jectories of their differentiation into effector cell types. Second, we
developed the assay for transposase-accessible chromatin using performed scATAC-seq in primary tumor biopsies from patients
sequencing (ATAC-seq), which identifies active DNA regula- with basal cell carcinoma (BCC) receiving anti-programmed cell
tory elements by transposition of sequencing adapters into acces- death protein 1 (PD-1) immunotherapy (PD-1 blockade). Single-
sible chromatin with the hyperactive transposase Tn5 (ref. 2). This cell deconvolution of the tumor microenvironment (TME) revealed
method can reveal several layers of gene regulation in a single assay, distinct types of immune, stromal and malignant cells, and analysis
including genome-wide identification of cis-elements, inference of of intratumoral T cells identified regulators of therapy-responsive
TF binding and activity, and nucleosome positions2–4. ATAC-seq T cell subtypes, including CD8+ exhausted (TEx) and CD4+ T fol-
is applicable to low-cell-number samples5, and even single cells6,7, licular helper (Tfh) cells. Altogether, we report scATAC-seq pro-
which has enabled epigenomic profiling of primary samples with files of over 200,000 cells, demonstrating that this platform enables
newfound precision. To date, scATAC-seq has been used to map the unbiased discovery of cell types and regulatory DNA elements
cell-to-cell variability and rare cell phenotypes, including in healthy across diverse biological systems.
and malignant immune cells8–12. However, the widespread adoption
of this technique has been hindered by the difficulty and cost of Results
performing the assay at scale. Droplet-based platform for scATAC-seq. We performed scATAC-
Here, we used a commercial system to perform scATAC-seq seq in droplets using the Chromium platform (10x Genomics) pre-
in nanoliter-sized droplets, which enables the generation of high- viously employed to measure single-cell transcriptomes13,14 (Fig. 1a
quality single-cell chromatin accessibility profiles at massive scale. and Supplementary Fig. 1a). In this approach, nuclei are first isolated
To systematically benchmark the performance of this method, we from a single-cell suspension and transposed in bulk with the trans-
analyzed primary cells in two biological contexts. First, we mapped posase Tn5. Transposed nuclei are then loaded onto a microfluidic
1Center for Personal Dynamic Regulomes, Stanford University School of Medicine, Stanford, CA, USA. 2Department of Pathology, Stanford University
School of Medicine, Stanford, CA, USA. 3Department of Genetics, Stanford University School of Medicine, Stanford, CA, USA. 4Biophysics Program,
Stanford University School of Medicine, Stanford, CA, USA. 5Cancer Biology Program, Stanford University School of Medicine, Stanford, CA, USA.
6Department of Dermatology, Stanford University School of Medicine, Redwood City, CA, USA. 710x Genomics, Inc., Pleasanton, CA, USA. 8Department
of Applied Physics, Stanford University, Stanford, CA, USA. 9Chan Zuckerberg Biohub, San Francisco, CA, USA. 10Howard Hughes Medical Institute,
Stanford University School of Medicine, Stanford, CA, USA. 11These authors contributed equally: Ansuman T. Satpathy, Jeffrey M. Granja.
*e-mail: grace@10xgenomics.com; wjg@stanford.edu; howchang@stanford.edu
NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology 925
Articles Nature BiotechNology
a b
Linear Pool
Collect amplification Remove oil
Oil Barcoded
gel beads
Transposition of Single nuclei Barcoded accessible
nuclei in bulk GEMs DNA fragments
c d
20 kb
200
Omni-ATAC-seq
(50,000 cells)
0
200
scATAC-seq
(4,484 cells)
0
200
scATAC-seq
(282 cells)
0
e
100
scATAC-seq
(100 of 4,484 cells)
75
scATAC-seq
(100 of 282 cells) 50
Strand 25
COX6B1 UPK1A−AS1 KMT2B U2AF1L4 PROSER3 +
ETV2 UPK1A ZBTB32 IGFLR1 ARHGAP33 −
PSENENHSPB6 0
0 25 50 75 100
chip for gel bead in emulsion (GEM) generation. Each gel bead is human (GM12878) and mouse (A20) B cell nuclei. Libraries were
functionalized with single-stranded barcoded oligonucleotides that sequenced and processed to de-multiplex reads, assign cell barcodes,
consist of a 29-base pair (bp) sequencing adapter, a 16-bp barcode align fragments to the human and mouse reference genomes and
selected from ~750,000 designed sequences to index GEMs and deduplicate fragments generated by PCR (Cell Ranger ATAC; see
the first 14 bp of read 1N, which serves as the priming sequence in Methods). We filtered scATAC-seq data using previously described
the linear amplification reaction to incorporate barcodes to trans- cut-offs of 1,000 unique nuclear fragments per cell and a transcrip-
posed DNA (Supplementary Fig. 1a and Supplementary Table 1). tion start site (TSS) enrichment score of 8 to exclude low-quality
Approximately 100,000 GEMs are formed in each channel, resulting cells15. Cells passing filter yielded on average 27.8 × 103 unique frag-
in the encapsulation of tens of thousands of nuclei in GEMs per ments mapping to the nuclear genome, and approximately 38.1% of
experiment. After GEM generation, gel beads are dissolved and Tn5 insertions were within peaks present in aggregated profiles from
the oligonucleotides are released for linear amplification of trans- all cells, comparable to published high-quality ATAC-seq profiles
posed DNA. Finally, the emulsion is broken, and barcoded DNA is (Fig. 1b, c and Supplementary Fig. 1b)6,10,15. scATAC-seq profiles exhib-
pooled for PCR amplification to generate indexed libraries for high- ited fragment size periodicity and a high enrichment of fragments
throughput sequencing. at TSSs, and aggregate profiles from multiple independent experi-
To assess the performance of this method, we generated scATAC- ments were highly correlated (Fig. 1d and Supplementary Fig. 1c).
seq libraries from species-mixing experiments, in which we pooled Finally, we observed a low rate of estimated multiplets (12 of 1,159
)301×(
stnemgarf
qes-CATA
02A
20
15
10
5
0
GM12878 unique fragments
1.04% estimated multiplets
1,159 Cells
GM12878 ATAC-seq fragments (×103)
tnemhcirne
SST
87821MG
00.050.10
Density
20
15
10
5
0
102 103 104 105 102 103 104 105
A20 unique fragments
tnemhcirne
SST
02A
0 0.050.10
Density
12
10
8
6
4
2
0
)%(
stelpitlum
detamitsE
6
5
4
3
2
2 3 4 5 6
0 3,000 6,000 9,000
Cells captured
)sllec
484,4(
MPC
gol 2
0 0.10.2 0 0.050.15
Density Density
GM12878 A20
r = 0.941 r = 0.944 6
4
2
2 4 6
log CPM (282 cells)
2
)sllec
981,2(
MPC
gol 2
log CPM (348 cells)
2
Fig. 1 | Massively parallel scATAC-seq in droplets. a, Schematic of scATAC-seq in droplets. b, ATAC-seq data quality control filters in human (GM12878)
and mouse (A20) B cells at 5,000 cell loading. Shown are the number of unique ATAC-seq nuclear fragments in each single cell (each dot) compared
with TSS enrichment of all fragments in that cell. Dashed lines represent the filters for high-quality single-cell data (1,000 unique nuclear fragments
and TSS score greater than or equal to 8). Density is given in arbitrary units. Data are representative of four independent experiments. c, Genome tracks
showing the comparison of aggregate scATAC-seq profiles with bulk Omni-ATAC-seq profiles from GM12878 B lymphoblasts (top panel). scATAC-seq
profiles were obtained from 2 independent mixing experiments, in which either 4,484 (from 10,000 cell loading) or 282 (from 500 cell loading) cells were
assayed, as indicated. The bottom panel shows accessibility profiles of 100 random single GM12878 cells from each experiment. Each pixel represents a
100-bp region. d, One-to-one plots of log-normalized reads in ATAC-seq peaks in aggregate scATAC-seq profiles (n = 100,000 ATAC-seq peaks, Pearson
correlation). Aggregate profiles in GM12878 (left) and A20 (right) cells are derived from two individual mixing experiments as in b, in which the indicated
numbers of cells were assayed. ATAC-seq peaks were identified in Omni-ATAC-seq profiles from 50,000 cells5. e, Human (GM12878)/mouse (A20) cell
mixing experiment showing proportion of single-cell libraries with both mouse and human ATAC-seq fragments (left). The right panel shows proportion
of mouse/human multiplets detected when cell-loading concentration was varied (n = 4 biologically independent experiments). The center line indicates
linear fit, and shaded lines indicate 95% confidence interval.
926 NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology
Nature BiotechNology Articles
cells, ~1%; Fig. 1e). A cell titration experiment with four cell-loading Single-cell chromatin landscape of human hematopoiesis. To
concentrations showed a linear relationship between the observed demonstrate this method in primary samples, we performed exper-
multiplet rate and the number of recovered cells (Fig. 1e). iments in human immune cells (Fig. 2a). We generated scATAC-
seq libraries from peripheral blood and bone marrow cells from
Rare cell detection and performance in archival samples. We sub- 16 healthy individuals and sampled cells in an unbiased fash-
sampled scATAC-seq data in silico, which showed that aggregate ion, or after enrichment for surface phenotypes (Supplementary
profiles from ~200 cells could achieve the confident discovery of Fig. 3a and Supplementary Table 4). In total, we generated scATAC-
~80% of ATAC-seq peaks from total profiles and a Pearson correla- seq profiles from 61,806 cells, which yielded on average 15.6 × 103
tion of r ~ 0.9 for all reads in peaks (Supplementary Fig. 1d,e). Using unique fragments mapping to the nuclear genome, and approxi-
this information, we devised an analysis workflow for peak calling mately 40.5% of Tn5 insertions were within aggregate ATAC-seq
and clustering (Supplementary Fig. 1f and see Methods). Single-cell peaks (Supplementary Fig. 3b,c). The quality of scATAC-seq profiles
libraries were first processed with Cell Ranger and filtered, and then was highly uniform across individuals, samples and cell types, and
we performed an ‘initial’ clustering by partitioning the genome into on a par with scATAC-seq profiles generated with other technolo-
2.5-kb windows and counting Tn5 insertions in each window, as gies (Supplementary Fig. 3d–f)11,12. We identified 31 scATAC-seq
described previously7,9. We then performed latent semantic index- clusters and visualized single-cell profiles with uniform manifold
ing (LSI) and clustered cells using shared nearest neighbor (SNN) approximation and projection (UMAP)18. We classified each clus-
clustering (Seurat16) with the top 20,000 accessible windows, requir- ter using three parallel approaches: (1) chromatin accessibility of
ing that each cluster contain at least 200 cells. These ‘initial’ clusters cis-elements (ATAC-seq peaks); (2) gene activity scores, computed
were used to identify ATAC-seq peaks (using MACS2 (ref. 17)) and from the accessibility of several enhancers linked to a single gene
to generate a merged peak set. Finally, a cell-by-peak counts matrix promoter19; and (3) TF activity, computed from the accessibil-
was created and used for ‘final’ clustering and downstream analysis, ity of TF binding sites genome-wide in each single cell4. All three
in which each cluster could contain any number of cells. approaches represent a ‘bottom-up’ analysis of scATAC-seq data
We tested this analysis approach with two quality-control experi- and do not require previous knowledge from RNA sequencing or
ments. First, we generated synthetic cell mixtures, in which human bulk ATAC-seq profiles.
monocytes and T cells were isolated from peripheral blood mono- Using the first approach, we identified 571,400 cis-elements
nuclear cells (PBMCs) and mixed in various ratios (Supplementary across all clusters, and approximately 20.4% of elements (116,713)
Fig. 2a,b and Supplementary Table 2). We then performed scATAC- exhibited cell type-specific accessibility (mean, 6,208 peaks per
seq and attempted to resolve each population in an unsupervised cluster; false discovery rate (FDR) < 0.01). Annotation of cell types
analysis. As expected, analysis of 50:50 mixtures identified 2 dis- using neighboring genes to cluster-specific cis-elements demon-
tinct populations of cells, which demonstrated accessibility of open strated that scATAC-seq profiles spanned the continuum from early
chromatin regions linked either to monocyte-specific genes (that is, progenitors to end-stage cell types (Fig. 2b, c and Supplementary
CD14, CSF1R, TREML4) or to T cell-specific genes (that is, CD3E, Fig. 4a). For example, clusters 2–4 demonstrated accessibility at cis-
CD4, CD8A; Supplementary Fig. 2a). Importantly, this analysis elements neighboring myeloid progenitor genes, including GATA1,
could also resolve populations that represented either 1 of 100 or TAL1 and SPI1, while clusters 14–16 demonstrated accessibility at
1 of 1,000 total cells (Supplementary Fig. 2b and Supplementary cis-elements neighboring B cell genes, including CD19, EBF1 and
Table 3). Second, we compared the performance of scATAC-seq in LYN (Fig. 2c). Clustering of scATAC-seq profiles could identify
fresh versus frozen PBMCs (Supplementary Fig. 2c–f). We isolated known cell type distinctions, such as CD4+ and CD8+ T cells, the
nuclei from either fresh PBMCs, viably frozen PBMCs or viably fro- presence of phenotypically distinct cell subsets, such as regula-
zen PBMCs sorted for live cells, and performed scATAC-seq. We tory CD4+ T cells (Tregs), and even relatively rare cell types, such
confirmed that scATAC-seq profiles passing filter yielded approxi- as basophils (Fig. 2b,c). Moreover, scATAC-seq analysis identified
mately the same quantity and quality of data, regardless of sample cell type-specific cis-elements even within a single gene locus. For
origin (Supplementary Fig. 2c)11. Namely, aggregate profiles from example, we observed unique accessibility of the +85 kb and +87 kb
fresh and frozen cells were highly correlated, frozen samples reca- enhancers in the IRF8 locus in myeloid cells, and of the +54 kb and
pitulated the majority of ATAC-seq peaks discovered in fresh sam- +56 kb enhancers in plasmacytoid dendritic cells (pDCs), while
ples (area under the curve, 0.809) and scATAC-seq profiles across the +37 kb enhancer was accessible in nearly all immune lineages
batches clustered together (Supplementary Fig. 2d–g). (Fig. 2d). These findings are in line with previously identified Irf8
Fig. 2 | Single-cell chromatin accessibility of human hematopoiesis. a, Schematic of progenitor and end-stage cell types in human hematopoiesis.
MPP, multipotent progenitor; LMPP, lymphoid-primed multipotent progenitor; CLP, common lymphoid progenitor; MEP, megakaryocyte-erythroid
progenitor; BMP, basophil-mast cell progenitor; N CD4, naïve CD4 T cell; N CD8, naïve CD8 T cell; M CD4, memory CD4 T cell; CD8 CM, CD8 central
memory T cell; CD8 EM, CD8 effector memory T cell; Imm NK, immature natural killer cell; Mat NK, mature natural killer cell; Neut, neutrophil;
Meg, megakaryocyte; Ery, erythrocyte; Eos, eosinophil; Baso, basophil. Lightly shaded cells were not sampled in the current study. b, UMAP projection
of 63,882 scATAC-seq profiles of bone marrow and peripheral blood immune cell types. Dots represent individual cells, and colors indicate cluster
identity (labeled on the right). Bar plot indicates the number of scATAC-seq profiles in each cluster of cells. Cells include those generated in this study
(61,806) and cells from a previous study11 (2,076). c, Heatmap of Z-scores of 116,713 cis-regulatory elements in scATAC-seq clusters derived from
b. Gene labels indicate the nearest gene to each regulatory element. d, Single-cell chromatin accessibility in the IRF8 locus. Each box shows scATAC-
seq profiles from 100 representative single cells from each cluster. Each pixel represents a 200-bp region. The top genome track shows the aggregate
accessibility profile from all cells combined. e, UMAP projection colored by log-normalized gene scores demonstrating the accessibility of cis-regulatory
elements linked (computed from linked accessibility of distal peaks to peaks at gene promoters using Cicero) to the indicated gene. Gene scores are
calculated as log 2 (GA*1000000 + 1), which we refer to as log 2 (GA + 1). For example, the top left plot demonstrates the accessibility score for cis-elements
linked to the promoter of the hematopoietic progenitor gene CD34. f, Example TF footprints of GATA2 and EBF1 with motifs in the indicated scATAC-seq
clusters. The Tn5 insertion bias track is shown below. g, Heatmap representation of ATAC-seq chromVAR bias-corrected deviations in the 250 most
variable TFs across all scATAC-seq clusters. Single-cell cluster identities are indicated at the top of the plot. h, UMAP projection of scATAC-seq profiles
colored by chromVAR TF motif bias-corrected deviations for the indicated factors.
NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology 927
Articles Nature BiotechNology
super-enhancers in dendritic cells (DCs)20 and may inform the cel- genome-wide with Cicero, an algorithm that links DNA elements
lular impact of disease variants in this locus21. based on co-accessibility in scATAC-seq data. This method identi-
Although cis-element analysis can be informative, this measure- fied 149,309 E-P connections across all scATAC-seq clusters, with a
ment is sparse in single cells, as it is limited by the DNA copy number. median of 6 enhancers linked to each promoter (Methods). We inde-
Therefore, in the second analysis approach, we used gene activity pendently validated E-P connections using two orthogonal datasets.
scores (referred to as ‘gene scores’), which represent the aggregate First, we compared E-P connections to chromosome conformation
accessibility of several enhancers linked to a single gene promoter19. signal obtained from H3K27ac HiChIP in T cells22 and found signif-
We first identified all enhancer–promoter (E-P) connections icant enrichment for HiChIP enhancer interaction signal in linked
a
1-HSC/MPP 2-MEP
3-CMP/BMP
4-LMPP 5-CLP 6-Pro-B 7-Pre-B 10 8-GMP 9-MDP 10-pDC 11-cDC 12-Monocyte 1 13-Monocyte 2
14-Naive B 15-Memory B
16-Plasma cell 17-Basophil 0 18-Immature NK 19-Mature NK1 20-Mature NK2 21-Naive CD4 T1 22-Naive CD4 T2
–10
–10 0 10
UMAP dimension 1
2 noisnemid
PAMU
b c
Human bone marrow and blood (63,882 cells; 31 clusters) Cis-regulatory elements
23-Naive Treg 24-Memory CD4 T 25-Treg 26-Naive CD8 T1 27-Naive CD8 T2
28-Naive CD8 T3 29-Central memory CD8 T 30-Effector memory CD8 T
31-Gamma delta T
04,0008,000
Number of cells
skaep qes-CATA
deifissalc 317,611
Z-score
2
–2
d e
IRF8
1-HSC/MPP
2-MEP
3-CMP/BMP
4-LMPP
5-CLP
6-Pro-B
7-Pre-B
8-GMP
9-MDP
10-pDC
11-cDC
12-Mono1
13-Mono2 14-Naive B
15-Memory B
16-Plasma B
17-Basophil
18-Imm NK
19-Mat NK1
20-Mat NK2 21-N CD4 T1
22-N CD4 T2
23-N Treg
24-M CD4 T
25-Treg
26-N CD8 T1
27-N CD8 T2 h
28-N CD8 T3
29-CM CD8 T
30-EM CD8 T
31-GDelta T
Rheumatoid arthritis SNPs
Systemic sclerosis SNPs
sfitom
FT
elbairav
052
Trans-regulatory factors
MEP
HSC/MPP CMPGMPMonocytesGamma delta Baso LMPP MDPcDC NKNKEM-8 Naive T
4
–4
erocs
noitaiveD
Memory B Pro-B
CM-8 Plasma pDCPre-B Memory 4TregNaive BCLP ZEB1 TCF4 ID3/4
LEF1 TCF7
TBX21
EOMES
NR4A1
PPARA IRF4
IRF8
NFKB1 RELA
PAX5 EBF1
RUNX GATA TAL1 TCF3
EHF BCL11A
SPI1
AP-1
CEBP MAF
NFIL3
10
0
−10
2
noisnemid
PAMU
Basophils
(17)
Progenitors (1-9) CD4+ T cells (21-25)
B cells (14-16) CD8+ T cells Myeloid cells (26-31)
(10-13) NK cells (18-20)
Aggregate
267
0
10
0
–10
–10 0 10
UMAP dimension 1
f g
p P
50 kb
2 noisnemid
PAMU
10
0
–10
2 noisnemid
PAMU
log (GA + 1) log (GA + 1) log (GA + 1) log (GA + 1)
0 8 0 9 0 8 0 8
CD34 CD14 MS4A1(CD20) IL13
log (GA + 1) log (GA + 1) log (GA + 1) log (GA + 1)
0 9 0 11 0 8 0 8
CD4 CD8A NCR1(NKp46) IFNG
−10 0 10 −10 0 10 −10 0 10
UMAP dimension 1 UMAP dimension 1 UMAP dimension 1
3
2
1
1
Deviation score Deviation score Deviation score Deviation score
–4 8 –3 3 –3 5 –3 7
GATA2 IRF8 EBF1 EOMES
−10 0 10 −10 0 10 −10 0 10 −10 0 10
UMAP dimension 1 UMAP dimension 1 UMAP dimension 1 UMAP dimension 1
detcepxe/devresbO
detcepxe/devresbO
snoitresni
detcepxE
snoitresni
detcepxE
GATA2
3-CMP/BMP 2-MEP 17-Bas 1-HSC/MPP
EBF1
2 15-Memory B 6-Pro-B 14-Naive B 7-Pre-B 5-CLP
1
2
1
−200−100 0 100 200
Distance to motif center
5490167321889064506723514789123 222332222221121111 1 111
FOXP3 Treg HSC BATF Memory T
NFATC1
CD34+ MPP I S L E 7 L R L Naive T B p o r n o e g e m n a it r o r r o s w LMPP CMP I E T C F B O C N X R M G 2 7 E 1 S N G K am / ma delta T CLP GMP MEP BMP C EB D F 1 1 9 B/pDC Pro-B LYN
Pre-T MDPNeut Meg Eos IRF8 pDC
Pre-B Eryy Mast I R L A 7 G R 2 P P r r o e - - B B TAL1 GATA1 MEP/CMP Naive B N CD4N CD8Imm NKpDC cDCMono2Baso SPI1 KIT L H M S P C P /M /C P L P P IL13 Memory B Treg CD8 CMMat NK Mono1 GATA2 Basophil CSF3R GMP/MDP CSF1R
BATF3 Plasma B M CD4CD8 EM HLA-DR cDC/ TREML4Monocyte
MAFB
+37+54+56 +85+87
928 NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology
Nature BiotechNology Articles
contacts (Supplementary Fig. 4b). Second, we compared E-P con- nominate causal cell types for each disease (chromVAR;
nections with expression quantitative trait loci (eQTLs23) and found Supplementary Fig. 5c,d). Several diseases, such as celiac disease,
enrichment of eQTLs in linked contacts, particularly when eQTLs type 1 diabetes, Crohn’s disease and juvenile arthritis, showed
were also identified in immune cells (Supplementary Fig. 4c). We high accessibility of variant-enhancers in T-cell populations
next projected gene scores for immune lineage-defining genes onto (Supplementary Fig. 5d)21. Other diseases, such as Kawasaki dis-
scATAC-seq profiles, which supported cis-element-defined cluster ease, multiple sclerosis and systemic lupus erythematosus, showed
identities (Fig. 2e). For example, the CD34 gene score identified high accessibility of variant-enhancers in B cells—either specifically
hematopoietic progenitors, the CD14 gene score identified mono- or in addition to accessibility in T cells (Supplementary Fig. 5d)21.
cytes and classical dendritic cells (cDCs) and the CD20 gene score scATAC-seq data also enabled the discovery of patterns in addi-
identified B cells (Fig. 2e and Supplementary Fig. 4d,e). Again, this tional cell types. For example, variant-enhancers associated with
analysis identified immune cell subsets, for example demonstrating systemic sclerosis showed high accessibility in NK cells and pDCs,
high FOXP3 gene scores in Tregs, and rare cell types, for example and variant-enhancers associated with ulcerative colitis showed high
demonstrating high IL13 gene scores in basophils (Supplementary accessibility in cDCs and monocytes, consistent with the roles of
Fig. 4e). Across all single cells, we identified 5,977 gene scores that these cell types in murine models of each disease27,28. Additional dis-
exhibited cluster-specific activity, reflecting markers for each cell eases with high variant-enhancer signals in myeloid cells included
type (Supplementary Fig. 4d). metabolic traits and diseases, such as fasting glucose, high-density
Finally, in the third analysis approach, we measured chroma- lipoprotein cholesterol levels and type 2 diabetes, suggesting regula-
tin accessibility at cis-elements sharing a TF binding motif using tory roles for myeloid cells in these processes as well. We confirmed
chromVAR4. To validate this method, we analyzed accessibility associations of disease variants with cell type-specific enhancers
changes in binding sites for known cell type-specific TFs (referred using H3K27ac HiChIP (Supplementary Fig. 5e).
to as TF deviation scores). Indeed, TF deviation scores for GATA2,
a lineage-determining factor for megakaryocyte, erythrocyte and Regulatory trajectories of immune cell lineages. We used
basophil lineages24, were increased in megakaryocyte-erythroid scATAC-seq to reconstruct cellular developmental trajectories in an
progenitors, basophils and common myeloid progenitors (CMPs; unbiased manner. As a test case, we reconstructed the lineage tra-
Fig. 2f). Similarly, the TF deviation scores for EBF1, a lineage- jectory of plasma B cell differentiation, since: (1) the developmental
determining factor for B cells25, were increased in naïve, memory program occurs in the bone marrow and blood and thus ought to be
and plasma B cells, as well as in early B cell progenitors (Fig. 2f). captured in our dataset, and (2) the regulatory mechanisms of this
Since DNA bound by TFs is protected from transposition by Tn5, process are well-defined for comparison (Fig. 3a). To achieve this,
visualization of each TF profile showed local chromatin acces- we used a nearest-neighbor approach on existing cluster definitions
sibility changes surrounding the binding ‘footprint’ (Fig. 2f and (Fig. 3a, b). We started with the plasma B cell cluster (cluster 16) and
Supplementary Fig. 5a). Deviation scores for all TF motifs revealed attempted to return to the hematopoietic stem cell (HSC) cluster
shared and unique regulatory programs across immune cell types (cluster 1) by sequentially selecting precursor cells with the most
(Fig. 2g,h and Supplementary Fig. 5b). For example, cDCs and B epigenetic similarity (Euclidean distances of ATAC-seq profiles; see
cells shared activity of BCL11A, SPI1 and IRF factor motifs, but Methods). Indeed, this reverse reconstruction process identified the
demonstrated unique activity of CEBP factors and EBF1, respec- well-established cellular trajectory of plasma B cell development as
tively (Fig. 2g, h). Similarly, TBX21 and EOMES were active in natu- the most significant among all tested trajectories (P < 0.0002; 5,000
ral killer (NK) and T cell populations; however, only T cells showed permutations). Finally, we generated an ordering of single cells
activity of the T cell lineage-determining factor TCF7 (Fig. 2g,h)26. (referred to as ‘pseudotime’) along this trajectory by computing a
We also grouped cis-elements according to the presence of causal vector across lineage clusters and aligning each cell to the vector in
risk variants associated with 21 autoimmune diseases and 18 non- the UMAP projection (Fig. 3c). An analysis of ~10,000 cis-elements
immune diseases21 and generated a feature set of variant-containing with dynamic accessibility patterns across the trajectory revealed
ATAC-seq peaks and their co-accessible elements for each disease cis-elements near known regulators of every stage of B cell devel-
(referred to as ‘variant-enhancers’; Supplementary Fig. 5c). We opment (Fig. 3d). For example, cis-elements that were accessible
then measured chromatin accessibility in variant-enhancers to early in the trajectory included enhancers for EBF1, RUNX1, IL7R,
Fig. 3 | Epigenomic differentiation trajectories of human immune cell types. a, Differentiation trajectory of HSCs to terminal plasma B cells (left).
Reverse reconstruction of B cell differentiation trajectory using scATAC-seq profiles (right; see Methods). Differences between the aggregate plasma B
cell scATAC-seq profile and all other clusters are calculated. Trajectory is tested against a nearest-neighbor approach; the cluster with the most similarity
(lowest trajectory distance) to the cluster of interest is identified as the immediate precursor cluster. b, Trajectory distance calculations for the terminal
plasma B cell cluster (cluster 16). Dots represent comparisons between the cluster of interest (labeled at the bottom) and every cluster not previously
identified. P < 0.0002 calculated as one-sided empirical P value from 5,000 random simulations of trajectory ordering. c, Pseudotime representation
of plasma B cell differentiation from HSCs. The dashed line represents a double-spline fitted trajectory across pseudotime. d, Pseudotime heatmap
ordering of the top 10,000 variable cis-regulatory elements across B cell differentiation (left). Zoom-in genome tracks show representation of behavior
of cis-elements accessible early (top) and late in B cell differentiation (bottom). e, Pseudotime heatmap ordering of chromVAR TF motif bias-corrected
deviations across B cell differentiation (left). TF motifs are filtered for genes that are highly active (defined as the average percentile between total gene
score and variability) that also demonstrate similarly dynamic gene scores across differentiation (R > 0.35 and FDR < 0.001 across 1,000 incremental
groups). Heatmap of TF gene scores is shown on the right. f, chromVAR bias-corrected deviation scores for the indicated TFs across B cell pseudotime.
Each dot represents the deviation score in an individual pseudotime-ordered scATAC-seq profile. The line represents the smoothed fit across pseudotime
and chromVAR deviation scores. g, Subclustering UMAP projection of 18,489 CD34+ bone marrow progenitors and DCs (cells within clusters 1–6 and
8–11 from full hematopoiesis). scATAC-seq profiles are colored by cluster identity, as labeled on the right. h, UMAP projection of progenitor populations;
highlighted are the sorted progenitor populations from Buenrostro et al.11. Grayed out are the cells assayed in this study. CMPs (green dots) were sorted as
lineage−CD34+CD38+CD10−CD45RA−CD123mid, and GMPs (light blue dots) were sorted as lineage−CD34+CD38+CD10−CD45RA+CD123mid. i, Confusion
matrix of sorted progenitor populations showing the proportion of each population in clusters defined in g. j, Lineage trajectories for the indicated cell
types, calculated as described in a. Lines represent double-spline fitted trajectories across pseudotime. k, Pseudotime heatmap ordering of chromVAR TF
motif bias-corrected deviations in the indicated lineage trajectory. TF motifs are filtered for genes as described in e.
NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology 929
Articles Nature BiotechNology
RAG2 and MEF2C, factors that are critical for B cell lineage speci- Since TF deviation scores can reflect the activity of many TFs with
fication (Fig. 3d)25,29,30. Cis-elements that were accessible late in the similar DNA-binding motifs, we integrated chromVAR deviations
trajectory included elements proximal to PRDM1, a critical TF for with gene scores to prune the data for relevant TFs within a motif
plasma cell fate, and the plasma cell-specific marker SDC1 (CD138). family (Fig. 3e). Indeed, this method accurately identified TFs that
a
HSC B cell lineage trajectory
MPP
LMPP CMP
10 CLP GMP MEP
Pro-B Meg
Pre-T MDP Neut
Pre-B Ery 0
Naive B N CD4 N CD8Imm NKpDC cDCMono1
Memory B Treg CD8 CMMat NK Mono2 −10
Plasma B M CD4CD8 EM
−10 0 10
UMAP dimension 1
2
noisnemid
PAMU
b c
P value < 0.0002
Plasma B
(Cluster 16)
400
Cluster 15 Cluster n
300
Cluster 14 Cluster n 200
. .
.
100
Cluster 1 Cluster n
d
TF motif accessibility TF gene score
HSC/MPP
LMPP/CLP
Pro-/Pre-B
Naive B
Memory B
)MPCgol
tsiD(
ecnatsid
yrotcejarT
∆C16 ∆C15 ∆C14 ∆C7 ∆C6 ∆C5 ∆C4
Index cluster
g h
10
0
−10
2 noisnemid
PAMU
e
Sorted CD34+ populations CD34+ cells and DCs (18,489 cells; 16 Clusters) (Buenrostro et al.11; 2,074 cells) Cluster 1 HSC Cluster 2 MPP
Cluster 3 10 CMP
Cluster 4 MEP
Cluster 5 LMPP
Cluster 6 CLP Cluster 7 GMP
Cluster 8 BM pDC
Cluster 9 0
Cluster 10
Cluster 11
Cluster 12
Cluster 13
Cluster 14
Cluster 15 −10
Cluster 16
−10 −5 0 5
UMAP dimension 1
2 noisnemid
PAMU
i
CD34+ C D ce 3 l 4 ls + R c e e p ll 1 s Rep H 2 SC MPP CMP ME S P o L r M t P I P D CLP GMP cDCs BM pDC
Cluster 1
Cluster 2
Cluster 3
Cluster 4 Cluster 5 Cluster 6
Cluster 7
Cluster 8
Cluster 9
Cluster 10
Cluster 11
Cluster 12
Cluster 13
Cluster 14
Cluster 15
Cluster 16
−10 −5 0 5
UMAP dimension 1
j k
Cluster
ID
f
Cis-element accessibility
HSC/MPP H C IK L D Z F 3 F 8 1 P G B A X T 1 A2 0 2 4 6
HOXA9 −2
RUNX1
LMPP/CLP IILL77RR ETS2 5 EBF1 0
Pro-/Pre-B B V R C M C A A X E V L G C F 2 3 R 2 2 C 4 M T E R C B U Y F F N B 3 1 X1/2 − 1 1 2 5 0 5 0 5
PLCG2 MEF2C 0
LYN BCL11A Naive B BLNK IRF4/8
PAX5
CD23 BACH1
CXCR4
Memory B HLA-DRB5 FOXO1 NFATC1
Plasma B S P D R C D 1 M1 Plasma B
Fraction of cells 1
0
serocs
noitaived RAVmorhC
Pseudotime order
Pseudotime order
HOXA9
MEF2C
EBF1
15 PAX5
10
5
0
10 IRF4 5
0 −5
Pseudotime Pseudotime Pseudotime Pseudotime
10
0
−10
2 noisnemid
PAMU
8 kb
75
0
RAG2 6 kb
120
0
PRDM1
0 100 0 100
0 100 Percentage Percentage
Percentage maximum maximum maximum
Meg/Ery Bas/Eo B LMPP pDC CMP pDC cDC Neut
Lineage trajectories
cDC
pDC
B TCF7
Neut G LM FI O 1 2 MAFK FOXO1 MYB S S R PI F 1 GFI1 ZBTB7B GATA2 CEBP SPI1
Meg/Ery Bas/Eo P m e 1 a rc 0 x e 0 im nt u a m ge M N G G F A A Y I T T B C A A 1 2 H LM ES O 2 2 S I E P B R P B A C F I F X L 8 1 1 1 5 1A I S R B R P C U F I L N 8 B 1 X 1A J S C R U P E A N I B R B P A I I S K H B S R R P L C T E F F F A I S L 8 4 1 4 1 T 1 1 5 A A J M C R U E A Y N B R B P A
KLF1 S G P A I T 1 A2 TCF3 TCF4 I B R C F L 8 11A J R U B N PJ
0 CEBPA TCF4
−10 −5 0 5
UMAP dimension 1
ytilibissecca
fitom FT
HSC
∆ ATAC ∆ ATAC
Plasma B
∆ ATAC ∆ ATAC
∆ ATAC ∆ ATAC
930 NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology
Nature BiotechNology Articles
a b
BCC TME (37,818 cells; 20 clusters)
1-Naive CD4 T
Pre- anti-PD-1 2-Th17 BCC biopsy 3-Tfh
4-Treg
5-Naive CD8 T
10 6-Th1
7-Memory CD8 T 8-CD8 TEx 9-Effector CD8 T
10-NK1
11-NK2
12-B
0 13-Plasma B
14-Myeloid
15-Endothelial
16-Fibroblasts
17-Tumor 1
18-Tumor 2
−10 19-Tumor 3 20-Tumor 4
−10 −5 0 5 10 04,0008,000
UMAP dimension 1 Number of cells
SU010 pre-treatment
SU010 post-treatment
2 noisnemid
PAMU
c
Post- anti-PD-1 B cells Myeloid cells Endothelial cells BCC biopsy
Fibroblasts
NK cells
CD8+ T cells
Tumor cells
CD4+ T cells
d e
log (GA + 1)
0 11
CD3E
2 noisnemid
PAMU
log (GA + 1) log (GA + 1)
0 11 0 7
CD8A KLRC1
10
0
−10
log (GA + 1)
0 6
UMAP dimension 1
2 noisnemid
PAMU
10
0
−10
−10 −5 0 5 10
UMAP dimension 1
log (GA + 1) log (GA + 1)
0 7 0 8
COL1A2 KRT14
10
0
−10
−10 −5 0 5 10 −10 −5 0 5 10 −10 −5 0 5 10
UMAP dimension 1 UMAP dimension 1
2 noisnemid
PAMU
SU001
SU005 SU006
SU007
SU008
SU009
Dissociate SU010 to single cells and FACS
Droplet
scATAC-seq
TME and TIL
Epigenetics
7 patients with BCC
CD86
f g
sfitom
FT
elbairav
052
Deviation
score
4
–4 AP-1
B
amsalP-31
1hT-6 1KN-01 xET
8DC-8
2KN-11 T
8DC
yromeM
-7
T
8DC
rotceffE-9
T
8DC
eviaN-5
T
4DC
eviaN-1
B-21 gerT-4 hfT-3 71hT-2 stsalborbiF-61 dioleyM-41 lailehtodnE-51 4
romuT-02
1
romuT-71
3
romuT-91
2
romuT-81
CNV score (log2(fold change))
–2 2
Stromal
(107 cells)
Tumor
(709 cells)
Stromal
(101 cells)
Tumor
(169 cells)
1 2 3 4 56 7 8 9 10 11 12 13141516 17-22
Chromosome
Distal enhancers Distal enhancers Distal enhancers
B S C PI L 1 11A +103+97 50 kb –35 +32+30+29 10 kb +5 +9 10 kb +43
IRF8 100 100 50
ETV2 12-B
0 0 0
13-Plasma B
RUNX
14-Myeloid
TBX21
EOMES 15-Endothelial
16-Fibroblasts
NFκB
17-Tumor 1
KLF4
CEBP 18-Tumor 2
p63 19-Tumor 3
BATF
20-Tumor 4
CD47 TGFB1 PDL1
Fig. 4 | Single-cell regulatory landscape of the BCC TME. a, Schematic of analysis of BCC samples. b, UMAP projection of 37,818 scATAC-seq profiles
of BCC TME cell types. Dots represent individual cells, and colors indicate cluster identity (labeled on the right). Bar plot indicates the number of cells in
each cluster of cells. T cell clusters showed high CD3E, CD8A and CD4 gene scores; NK cell clusters: high KLRC1 and NCR1 gene scores; B cells and plasma
cells: high CD19 and SDC1 gene scores, respectively; myeloid cells: high CD86, CSF1R and FLT3 gene scores; stromal endothelial cells and fibroblasts: high
CD31 and COL1A2 gene scores, respectively; and tumor cell clusters: high KRT14 gene score. c, UMAP projection colored by patient of origin, as indicated
on the right. d, UMAP projection colored by log-normalized gene scores demonstrating the accessibility of cis-regulatory elements linked (using Cicero)
to the indicated gene. e, Estimated copy-number variation (log(fold change) to GC-matched background) from scATAC-seq data. Stromal cells include
2
endothelial cells and fibroblasts. f, Heatmap representation of ATAC-seq chromVAR bias-corrected deviations in the 250 most variable TFs across all
scATAC-seq clusters. Cluster identities are indicated at the bottom of the plot. g, Genome tracks of aggregate scATAC-seq data, clustered as indicated in b.
Arrows indicate the position and distance (in kb) of distal enhancers in each gene locus.
NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology 931
Articles Nature BiotechNology
are critical for B cell differentiation and resolved the timing of TF differentiated pDCs, while a second trajectory traversed CMP, GMP,
activity (Fig. 3e). For example, MEF2C activity was observed early MDP and CDP stages before pDC differentiation (Fig. 3k). Each
in B cell development, consistent with its role in lymphoid fate spec- pathway relied on the same regulatory program, which included
ification30, followed by the sequential activity of EBF1, PAX5 and RUNX, IRF8, SPIB, BCL11A and TCF4 factors33. Moreover, we did
IRF4, recapitulating the known order of their functions in pro-B not observe significant epigenomic heterogeneity within terminal
cells, pre-B cells and naïve B cells, respectively (Fig. 3f)25. pDCs, suggesting that divergent cellular trajectories can achieve
We applied trajectory analysis to early stages of hematopoiesis identical cell states through common regulatory programs.
to identify regulators of myeloid fate decisions, particularly of DCs.
We re-clustered 16,415 progenitor and DC scATAC-seq profiles, Single-cell chromatin landscape of intratumoral immunity. BCC
and 2,074 profiles of surface marker-defined progenitors generated is the most common cancer in humans worldwide, and recent stud-
in a previous study (Fig. 3g)11. We identified 16 subclusters, and ies demonstrated that patients with advanced BCC can obtain clini-
projection of sorted scATAC-seq profiles onto de novo-defined cal benefit from immunotherapies that block the T cell inhibitory
clusters revealed significant heterogeneity in marker-defined states receptor PD-1 (ref. 37). However, as in many other cancers, PD-1
(Fig. 3h,i). Globally, immune lineages appeared to diverge early via blockade is clinically ineffective in more than half of patients with
three distinct branches to: (1) megakaryocyte/erythroid (Meg/E) BCC37,38. Thus, our goal was to use scATAC-seq to identify cell types
and basophil/eosinophil (Bas/Eo) fates, (2) lymphoid fates or (3) that were responsive to therapy and the regulatory mechanisms con-
neutrophil/monocyte/DC fates. However, sorted progenitors did trolling their activity. In addition, these experiments demonstrated
not always occupy a single de novo-defined regulatory state. For the feasibility of applying scATAC-seq to sparse samples from
example, CMPs were present in 4 de novo-defined clusters, includ- clinical biopsies. We performed scATAC-seq on site-matched serial
ing in committed pathways leading to neutrophil/monocyte/DC tumor biopsies pre- and post-PD-1 blockade (pembrolizumab)
fates (clusters 2 and 11), Meg/E fates (clusters 4 and 5) or Baso/ from five patients, plus post-therapy biopsies from two additional
Eo fates (clusters 3 and 4; Fig. 3h,i). Similarly, granulocyte-macro- patients (Fig. 4a and Supplementary Table 5). We dissociated
phage progenitors (GMPs) were present in 4 clusters downstream tumors into single-cell suspensions and sampled cells in an unbi-
of the CMP (clusters 11–14), including those leading to neutrophil ased fashion or after cell sorting to enrich for T cells (CD45+CD3+),
differentiation, as well as clusters leading to cDC and pDC fates non-T immune cells (CD45+CD3−) and/or stromal and tumor cells
(Fig. 3h,i). (CD45−; Supplementary Fig. 6a). In total, we generated scATAC-
Analysis of TF activity revealed shared and unique TF programs seq profiles from 37,818 cells. Cells passing filter yielded on aver-
across myeloid trajectories (Fig. 3j). For example, Meg/E and Bas/Eo age 15 × 103 unique fragments mapping to the nuclear genome,
progenitors shared accessibility at GATA2 motifs, but Bas/Eo com- and approximately 62.5% of Tn5 insertions were within aggregate
mitment was characterized by SPI1 (PU.1) and CEBPA motif activ- ATAC-seq peaks (Fig. 4b and Supplementary Fig. 6b–d).
ity, while Meg/E commitment was characterized by MYB, GATA1 Classification of scATAC-seq clusters using cis-elements
and KLF1 motif activity (Fig. 3k)31,32. Similarly, neutrophil progeni- and gene scores revealed a diverse ecosystem of cell types in the
tors shared accessibility at SPI1 motifs with Bas/Eo progenitors, but BCC TME, including nine T cell clusters, two NK cell clusters,
neutrophil commitment was accompanied by additional activity of B cells and plasma cells, myeloid cells that comprised cDCs and
AP-1, CEBP and RARA motifs (Fig. 3k). Finally, the analysis of tra- macrophages, stromal endothelial cells and fibroblasts, and four
jectories toward DC fates revealed three pathways. The cDC pathway tumor cell clusters (Fig. 4b–d and Supplementary Fig. 6e). Notably,
transitioned through CMP and GMP clusters, and then to cluster 13 stromal and immune cells from different patients largely clus-
(monocyte-dendritic cell progenitor; MDP) and cluster 14 (common tered together, demonstrating that these clusters did not repre-
dendritic progenitor; CDP), before terminal cDC differentiation. sent patient-specific cell states or batch effects. In contrast, tumor
This trajectory showed accessibility at IRF8, IRF4, BCL11A, SPI1, cell clusters were largely patient-specific, consistent with earlier
AP-1 and RBPJ motifs, consistent with roles of each factor in DC single-cell RNA sequencing studies in melanoma and head and
differentiation33. IRF8, BCL11A and SPI1 motifs exhibited accessibil- neck cancer39,40 (Fig. 4c and Supplementary Fig. 6f). To iden-
ity early in CDPs, while AP-1 and RBPJ factors exhibited late acces- tify potential genome alterations in tumor cells, we estimated
sibility (Fig. 3k). For pDCs, two possible trajectories were observed, copy number variation (CNV) from scATAC-seq data (Fig. 4e
supporting reports that this lineage can arise from both myeloid- and and see Methods). This analysis revealed CNVs in tumor clus-
lymphoid-committed progenitors34–36. One pDC trajectory transi- ters 17–20, compared with other stromal cell populations. For
tioned directly from lymphoid-primed multipotent progenitors to example, tumor cells in patient SU010 showed ATAC-seq
Fig. 5 | Epigenomic regulators of T cell exhaustion after PD-1 blockade. a, Subclustering UMAP projection of 28,274 tumor-infiltrating T cells (clusters
1–9 from TME UMAP). scATAC-seq profiles are colored by cluster identity, as labeled on the right. For CD8+ T cells, naïve T cells showed high CCR7 and
TCF7 gene scores; effector T cells: high EOMES and IFNG gene scores; memory T cells: high EOMES gene score, but low effector gene scores; and exhausted
T cells: high gene scores for inhibitory receptors PDCD1, CTLA4 and HAVCR2, and T cell dysfunction genes, CD101 and CD38. For CD4+ T cells, Tregs showed
high FOXP3 and CTLA4 gene scores; Th1 cells: high IFNG and TBX21 gene scores; Th17 cells: high IL17A and CTSH gene scores; and Tfh cells: high CXCR5,
IL21 and BTLA gene scores. Bar plot indicates the number of cells in each cluster of cells. b, UMAP projection colored by log-normalized gene scores
demonstrating the accessibility of cis-regulatory elements linked (using Cicero) to the indicated gene. c, UMAP projection of tumor-infiltrating T cells
colored by pre- and post-PD-1 blockade samples. d, Genome tracks of aggregate scATAC-seq data, clustered as indicated in a. Arrows indicate the position
and distance (in kb) of intragenic or distal enhancers in each gene locus. e, Lineage trajectories of Tfh and CD8+ T cell states. Lines represent double-spline
fitted trajectories across pseudotime. f, Pseudotime heatmap ordering of chromVAR TF motif bias-corrected deviations in effector and memory CD8+ T
lineage trajectory. TF motifs are filtered for genes that are highly active (defined as the average percentile between total TF activity and variability > 0.75)
that also demonstrate similarly dynamic gene scores across differentiation (R > 0.35 and FDR < 0.001 across 1,000 incremental groups). Heatmap of TF
gene scores is shown on the right. g, Pseudotime heatmap ordering of cis-regulatory elements (left) and chromVAR TF motif bias-corrected deviations
(right) in the CD8+ TEx lineage trajectory. h, Pseudotime heatmap ordering of cis-regulatory elements (left) and chromVAR TF motif bias-corrected
deviations (right) in the CD4+ Tfh lineage trajectory. i, UMAP projection of scATAC-seq profiles colored by chromVAR TF motif bias-corrected deviations
for the indicated factors. j, UMAP projection of tumor-infiltrating T cells colored by pre- and post-PD-1 in representative individual responder and
nonresponder patients. k, Schematic of regulatory modules controlling TEx and Tfh differentiation.
932 NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology
Nature BiotechNology Articles
signal consistent with amplifications of regions of chromosomes 3 patterns of activity in immune cells, compared with stromal
and 6, which were present in both pre- and post-therapy sam- or tumor cells (Fig. 4f and Supplementary Fig. 7a,b). In par-
ples (Fig. 4e). Finally, we analyzed TF activity and found distinct ticular, tumor cells showed high accessibility of GLI1 motifs,
TCF7 LEF1 BACH2
EOMES RUNX3
NR4A1
TFAP4 NR3C1 MAF
NFKB2 NFKB1
BATF IRF4 NFATC1
3
–3
–6 TBX21/EOMES
2 noisnemid
PAMU
0
3
–3
–6 NFATC1 NFKB1
−10 −5 0 5
UMAP dimension 1
2 noisnemid
PAMU
3
–3
−6
0
–10 –5 0 5
UMAP dimension 1
2 noisnemiD
PAMU
a
Tumor-infiltrating T cells (28,274 cells; 19 clusters)
3
–3
−6
Deviation score Deviation score Deviation score –3 6 –3 5 –6 6
0
NR4A1 BATF
Deviation score Deviation score Deviation score
–4 2 –6 5 –3 3
IRF4
−10 −5 0 5
UMAP dimension 1
2
noisnemid
PAMU
b
Effector CD8+ T 1-Naive CD4 T CD4+ Treg Naive CD4+ T 2 3 - - A Th ct 1 ivated CD4 T 3
4-Memory CD4 T
5-Th17
6-Tfh 1 –3 7-Tfh 2
8-Treg 1
0 Memory CD8+ T 9-Treg 2 −6 CD8A
10-Treg 3
11-Treg 4
12-Effector CD8 T
CD4+ Th17 13-Naive CD8 T
14-Memory CD8 T
15-Early TEx
16-Intermediate TEx
CD4+ Tfh 17-Terminal TEx
Exhausted CD8+ T 18-Other T
19-Other T
−10 −5 0 5 0 4,000
UMAP dimension 1 Number of cells
2 noisnemid
PAMU
0
3
–3
−6 CD4
2 noisnemid
PAMU
PDCD1 CTLA4 HAVCR2
0
TCF7 CD101 CD38
−10 −5 0 5 −10 −5 0 5 −10 −5 0 5 −10 −5 0 5
UMAP dimension 1 UMAP dimension 1 UMAP dimension 1 UMAP dimension 1
3
–3
−6
2 noisnemid
PAMU
c d
Pre-treatment Post-treatment
0
−10 −5 0 5 0 100
UMAP dimension 1 Fraction of cells
e
3
–3
−6
2 noisnemid
PAMU
log (GA + 1) log (GA + 1) log (GA + 1) log (GA + 1)
0 11 0 10 0 11 0 10
CD4+ Th1
Naive CD8+ T
log (GA + 1) log (GA + 1) log (GA + 1) log (GA + 1)
0 11 0 11 0 7 0 8
TEx distal enhancers TEx distal enhancers
TEx +5 kb enhancer –37 –14–6 +19+24+27 +36+34+32 +9 +2
5 10 kb
2 100 100 100
3
13 13-Naive CD8 T
14 0 0 0
11
9 14-Memory 8 CD8 T
19
1
15 15-E T a E rly x
10
4
18 16-Intermediate
12 TEx
6
16
7 17-Term T in E a x l 17
PDCD1 CXXC11 10 kb CTLA4 5 kb HAVCR2
f g h
Tfh and CD8+ T cell trajectories TF motif accessibility Naive T TEx N T a F i v M e o T tif accessib T i E lit x y Naive T Tfh Naive T Tfh
Effector T
Naive CD4+ T TCF7 LEF1 Naive CD8+ T
Memory T NR3C1 0 I N R F F A 4 TC1
NFKB2 BATF
MAF
TFAP4
CD4+ Tfh Exhausted T RUNX3
TBX21
−10 −5 0 5
UMAP dimension 1
i j k
etaidemretnI
eviaN
yromeM
xET
xET.mreT
Cis-element accessibility Naive T Effector T Naive T Memory T
RBPJ TCF7 LEF1
TCF7 NR4A1
LEF1
PRDM1 E TB O X M 2 E 1 S NR3C1
RBPJ
YY1 EOMES FOXO3
HIF1A
TFAP4 TCF3 STAT5A
0 100 0 100
Percentage maximum Percentage maximum
SU009-responder SU001-responder
SU008-non-responder SU006-non-responder
3
–3
−6
2 noisnemiD
PAMU
Cis-element accessibility TF motif accessibility
C C C D R 28 7 CCR7 ETS1 CD28 ETS1
BACH2
IFNG
STIM2 IFNG IL12A ID2 RORA IFNG
I I P F L T 1 N P 2 A R R R C B 1 2 I B C L T D 2 L 1 2 A 00
CTLA4
PDCD1 PDCD1 CTLA4 HAVCR2 ENTPD1 ENTPD1 HAVCR2 CD101
ITGAE CD38 CTLA4
TOX PRDM1 GZMB IRF4 CD101
0 100 0 100 0 100
Percentage maximum Percentage maximum Percentage maximum
Pre-treatment Post-treatment
Anti-tumor T cell response
Naive CD8+ T Naive CD4+ T
RUNX3
NR4A1 EOMES NFKB1/2
MAF TBX21 BATF TFAP4 IRF4
NFATC1
Intermediate Intermeditate
TEx Memory T Tfh
NFKB1/2 RUNX3 BATF NR3C1
IRF4 MAF
0 NFATC1 TFAP4
Shared regulatory program
Reciprocal signals?
Terminal TEx Terminal Tfh
−10 −5 0 5 −10 −5 0 5
UMAP Dimension 1 UMAP Dimension 1
NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology 933
Articles Nature BiotechNology
consistent with the critical role of the Hedgehog pathway in BCC of cis-elements near inhibitory receptors, as well as elements near
(Supplementary Fig. 7b)41. genes associated with tissue residency, such as ITGAE (CD103)59.
Accordingly, this stage was accompanied by accessibility of NR3C1
Chromatin landscape of intratumoral TEx after PD-1 blockade. and NR4A1 motifs, factors immediately downstream of T cell recep-
Since T cells can be activated by targeting inhibitory receptors on tor (TCR) signaling that also induce exhaustion60,61, and the RUNX3
T cells or inhibitory receptor ligands on stromal cells, we examined motif, a factor that programs tissue residency of CD8+ T cells
both cell populations. First, we analyzed cis-elements near genes (Fig. 5g)62. The second stage (terminal TEx) showed accessibility of
encoding the known inhibitory ligands, CD47, TGFβ and PD-L1 cis-elements near genes associated with terminal T cell dysfunction,
(ref. 42–44), and identified distinct patterns of accessibility across stro- such as CD101 and TOX49,52,63–65, as well as of additional elements in
mal and tumor clusters (Fig. 4g). We identified three cis-elements stage 1 gene loci, such as CTLA4 (Fig. 5g). Importantly, this stage
in the CD47 locus, consistent with previously identified functional was accompanied by accessibility of a core set of TF motifs, which
enhancers controlling CD47 expression (Fig. 4g)45. The tumor included NFKB1 and NFKB2, BATF, IRF4 and NFATC1, factors
necrosis factor- and NFκB-responsive +97 kb and +103 kb enhanc- that are downstream of TCR signaling and have been demonstrated
ers were only accessible in tumor cells, supporting previous reports to play crucial roles in T cell exhaustion in mice66–68.
that tumor CD47 expression is responsive to inflammatory signals Finally, we examined the epigenetic relationship between TEx
and contributes to escape from immune surveillance45. Similarly, we and Tfh cells. Tfh cells have previously been observed in tumors and
identified three cis-elements in the TGFB1 locus that were acces- are a prognostic indicator of response to checkpoint blockade69–71.
sible in stromal cells, consistent with the expression pattern of this The differentiation trajectory from CD4+ naïve T cells to Tfh cells
gene in primary tumors (Fig. 4g)43. We also identified three known showed accessibility of cis-elements neighboring Tfh-specific
cis-elements in the PDL1 locus46, which demonstrated shared acces- genes, such as IL21 and BTLA, but also of elements near genes
sibility in tumor cells, stromal cells, and myeloid and B cells, sup- typically associated with TEx cells, such as inhibitory receptors,
porting the broad expression pattern of this ligand and common consistent with the known, but unexplained, expression of these
cis-regulatory elements in each cell type (Fig. 4g). genes in human Tfh cells (Fig. 5h and Supplementary Fig. 8c–e)72.
We next re-clustered 28,274 T cells and identified 19 subclusters, Strikingly, differentiation was accompanied by the accessibility of
revealing a rich diversity of T cell phenotypes in the TME (Fig. 5a). Tfh regulators, but also of the same core set of TF motifs associ-
CD8+ T cell states included naïve T cells, effector T cells, memory ated with TEx differentiation, including NFKB2, BATF, IRF4 and
T cells and TEx (Fig. 5b and Supplementary Fig. 8a,b). We also iden- NFATC1, suggesting a common program driving the development
tified an intermediate TEx cluster (cluster 16) that exhibited gene of TEx and Tfh cells downstream of PD-1 blockade (Fig. 5h,i and
scores of both TEx and memory T cells (Fig. 5b). CD4+ T cell states Supplementary Fig. 8f). Indeed, the +5 kb PDCD1 enhancer also
included naïve T cells, Tregs, T helper 1 (Th1) cells, T helper 17 showed high accessibility in Tfh cells and contained TF binding sites
(Th17) cells and Tfh cells (Fig. 5b and Supplementary Fig. 8a–c). for the core TEx factors, IRF4 and BATF (Supplementary Fig. 8e).
We focused on CD8+ TEx cells since this population is enriched for Finally, the abundance of TEx and Tfh cells was similar post-ther-
clonally expanded tumor-specific T cells39,47,48, and the irreversibil- apy, and, in our small cohort, the expansion of these cell types was
ity of the TEx epigenetic state may limit re-invigoration of T cells greater in responder patients compared with nonresponder patients
after PD-1 blockade49. Indeed, a comparison of pre- and post-PD-1 (Fig. 5j and Supplementary Fig. 9a, b). Altogether, these results map
blockade profiles showed that TEx cells were highly expanded the epigenetic landscape of intratumoral TEx cells in humans and
after therapy; more than 90% of TEx cells were derived from post- suggest that chronic TCR signals drive a shared regulatory program
therapy biopsies, whereas memory and effector CD8+ clusters were in TEx and Tfh cells after PD-1 blockade (Fig. 5k).
equally derived from both time points (Fig. 5c). Notably, we also
observed an expansion of Tfh cells post-therapy, suggesting that Discussion
PD-1 blockade impacts both CD4+ and CD8+ cell states in the TME The adoption of single-cell chromatin accessibility profiling has
(Fig. 5c). Across all T cell states, we identified 35,147 cis-elements been hindered by trade-offs between data quality, throughput and
that exhibited cell type-specific accessibility (mean, 3,361 peaks cost. Here, we performed a droplet-based method for highly mul-
per cluster; FDR < 0.01; Supplementary Fig. 8d). In TEx cells, we tiplexed single-cell chromatin accessibility profiling. scATAC-seq
identified 4,598 such elements, demonstrating that human T cell libraries generated using this method are high-quality, have a lower
exhaustion is accompanied by global remodeling of the chromatin multiplet rate compared with previous methods, do not require cell
accessibility landscape, consistent with previous studies in mice49–52. sorting or noncommercial reagents and cost ~$0.4 per cell. The
Analysis of individual TEx-specific enhancers identified regula- massive scale of cell type and cell state information generated by this
tory elements in inhibitory receptor loci (Fig. 5d). For example, the method affords three key advantages: (1) comprehensive deconvo-
PDCD1 locus (encoding PD-1) contained an intragenic cis-element lution of all cells in a tissue, including rare cells; (2) analysis of active
(+5 kb) with specific accessibility in TEx cells, suggesting that the regulatory DNA at the level of individual genes and cis-elements
persistent expression of PD-1 in exhausted T cells is controlled by a in single cells; and (3) unbiased reconstruction of developmental
single state-specific enhancer, and that the regulation of persistent trajectories, without the use of predefined markers.
PD-1 expression may be different in humans and mice50. CTLA4 We used a data-driven approach to iteratively group single cells
and HAVCR2 loci showed TEx-specific activity of several distal in the immune system together based on their accessible genomes,
cis-elements, compared with other CD8+ T cell states (Fig. 5d). to reconstruct cell type-specific cis-and trans-regulatory maps and
We compared TEx differentiation trajectories with effector or to highlight disease-associated enhancers that are active in spe-
memory CD8+ T cell trajectories (Fig. 5e). The differentiation of cific cell types. Moreover, the density of single-cell clusters enabled
naïve CD8+ T cells to either effector or memory cells identified the computational inference of developmental trajectories, for example
critical roles of EOMES and TBX21 (T-bet) motifs in each path- recapitulating decades of research on B cell and DC development.
way53–55 (Fig. 5f). Effector cell pseudotime also demonstrated the Importantly, scATAC-seq of tumor-infiltrating lymphocytes from
accessibility of other known regulator sites, including TFAP4 and patient biopsies identified regulatory programs controlling T cell
YY1 (ref. 56,57). Similarly, memory cell pseudotime showed acces- exhaustion and a shared program with Tfh cells. Previous stud-
sibility at HIF1A and E protein sites58. In contrast, TEx cells showed ies have demonstrated that chronic antigen stimulation drives the
a distinct regulatory program, which progressed through two stages development of both TEx and Tfh cells73–75. Therefore, we speculate
(Fig. 5g). The first stage (intermediate TEx) showed accessibility that this shared program may reflect an evolutionarily conserved
934 NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology
Nature BiotechNology Articles
pathway to synchronize CD4+ and CD8+ T cell responses to chronic 24. Crispino, J. D. & Weiss, M. J. Erythro-megakaryocytic transcription factors
pathogen infection, such that CD4+ Tfh cells support antibody for- associated with hereditary anemia. Blood 123, 3080–3088 (2014).
25. Nutt, S. L. & Kee, B. L. The transcriptional regulation of B cell lineage
mation as well as long-term activation of CD8+ T cells, perhaps
commitment. Immunity 26, 715–725 (2007).
through IL-21 (ref. 76–78). In summary, we describe the performance 26. Johnson, J. L. et al. Lineage-determining transcription factor TCF-1 initiates
of a method for generating large-scale single-cell chromatin acces- the epigenetic identity of T cells. Immunity 48, 243–257.e10 (2018).
sibility profiles on a widely distributed single-cell platform, enabling 27. Gerber, E. E. et al. Integrin-modulating therapy prevents fibrosis and
unbiased discovery of cell types and regulatory DNA elements in autoimmunity in mouse models of scleroderma. Nature 503, 126–130 (2013).
28. Castellanos, J. G. et al. Microbiota-Induced TNF-like ligand 1A drives group
complex tissues.
3 innate lymphoid cell-mediated barrier protection and intestinal T cell
activation during colitis. Immunity 49, 1077–1089.e5 (2018).
Online content 29. Niebuhr, B. et al. Runx1 is essential at two stages of early murine B-cell
Any methods, additional references, Nature Research reporting development. Blood 122, 413–423 (2013).
30. Stehling-Sun, S., Dade, J., Nutt, S. L., DeKoter, R. P. & Camargo, F. D.
summaries, source data, statements of code and data availability and
Regulation of lymphoid versus myeloid fate ‘choice’ by the transcription
associated accession codes are available at https://doi.org/10.1038/
factor Mef2c. Nat. Immunol. 10, 289–296 (2009).
s41587-019-0206-z. 31. Kerenyi, M. A. & Orkin, S. H. Networking erythropoiesis. J. Exp. Med. 207,
2537–2541 (2010).
Received: 21 January 2019; Accepted: 1 July 2019; 32. Fulkerson, P. C. Transcription factors in eosinophil development and as
Published online: 2 August 2019 therapeutic targets. Front. Med. 4, 115 (2017).
33. Satpathy, A. T., Wu, X., Albring, J. C. & Murphy, K. M. Re(de)fining the
dendritic cell lineage. Nat. Immunol. 13, 1145–1154 (2012).
References 34. Manz, M. G., Traver, D., Miyamoto, T., Weissman, I. L. & Akashi, K.
1. Roadmap Epigenomics Consortium. Integrative analysis of 111 reference Dendritic cell potentials of early lymphoid and myeloid progenitors. Blood 97,
human epigenomes. Nature 518, 317–330 (2015). 3333–3341 (2001).
2. Buenrostro, J. D., Giresi, P. G., Zaba, L. C., Chang, H. Y. & Greenleaf, W. J. 35. Becker, A. M. et al. IRF-8 extinguishes neutrophil production and promotes
Transposition of native chromatin for fast and sensitive epigenomic profiling dendritic cell lineage commitment in both myeloid and lymphoid mouse
of open chromatin, DNA-binding proteins and nucleosome position. progenitors. Blood 119, 2003–2012 (2012).
Nat. Methods 10, 1213–1218 (2013). 36. Rodrigues, P. F. et al. Distinct progenitor lineages contribute to
3. Schep, A. N.et al. Structured nucleosome fingerprints enable high-resolution the heterogeneity of plasmacytoid dendritic cells. Nat. Immunol. 19,
mapping of chromatin architecture within regulatory regions. Genome Res. 711–722 (2018).
25, 1757–1770 (2015). 37. Chang, A. L. S. et al. Pembrolizumab for advanced basal cell carcinoma: an
4. Schep, A. N., Wu, B., Buenrostro, J. D. & Greenleaf, W. J. chromVAR: investigator-initiated, proof-of-concept study. J. Am. Acad. Dermatol. 80,
inferring transcription-factor-associated accessibility from single-cell 564–566 (2019).
epigenomic data. Nat. Methods 14, 975–978 (2017). 38. Ribas, A. & Wolchok, J. D. Cancer immunotherapy using checkpoint
5. Corces, M. R. et al. An improved ATAC-seq protocol reduces background blockade. Science 359, 1350–1355 (2018).
and enables interrogation of frozen tissues. Nat. Methods 14, 959–962 (2017). 39. Tirosh, I. et al. Dissecting the multicellular ecosystem of metastatic
6. Buenrostro, J. D. et al. Single-cell chromatin accessibility reveals principles of melanoma by single-cell RNA-seq. Science 352, 189–196 (2016).
regulatory variation. Nature 523, 486–490 (2015). 40. Puram, S. V. et al. Single-cell transcriptomic analysis of primary
7. Cusanovich, D. A. et al. Multiplex single cell profiling of chromatin and metastatic tumor ecosystems in head and neck cancer. Cell 171,
accessibility by combinatorial cellular indexing. Science 348, 910–914 (2015). 1611–1624.e24 (2017).
8. Corces, M. R. et al. Lineage-specific and single-cell chromatin accessibility 41. Atwood, S. X., Li, M., Lee, A., Tang, J. Y. & Oro, A. E. GLI activation by
charts human hematopoiesis and leukemia evolution. Nat. Genet. 48, atypical protein kinase C ι/λ regulates the growth of basal cell carcinomas.
1193–1203 (2016). Nature 494, 484–488 (2013).
9. Cusanovich, D. A. et al. The cis-regulatory dynamics of embryonic 42. Jaiswal, S. et al. CD47 is upregulated on circulating hematopoietic stem cells
development at single-cell resolution. Nature 555, 538–542 (2018). and leukemia cells to avoid phagocytosis. Cell 138, 271–285 (2009).
10. Satpathy, A. T. et al. Transcript-indexed ATAC-seq for precision immune 43. Mariathasan, S. et al. TGFβ attenuates tumour response to PD-L1 blockade
profiling. Nat. Med. 24, 580–590 (2018). by contributing to exclusion of T cells. Nature 554, 544–548 (2018).
11. Buenrostro, J. D. et al. Integrated single-cell analysis maps the continuous 44. Okazaki, T. & Honjo, T. The PD-1-PD-L pathway in immunological tolerance.
regulatory landscape of human hematopoietic differentiation. Cell 173, Trends Immunol. 27, 195–201 (2006).
1535–1548.e16 (2018). 45. Betancur, P. A. et al. A CD47-associated super-enhancer links pro-
12. Cusanovich, D. A. et al. A single-cell atlas of in vivo mammalian chromatin inflammatory signalling to CD47 upregulation in breast cancer. Nat.
accessibility. Cell 174, 1309–1324.e18 (2018). Commun. 8, 14802 (2017).
13. Zheng, G. X. Y. et al. Massively parallel digital transcriptional profiling of 46. Corces, M. R. et al. The chromatin accessibility landscape of primary human
single cells. Nat. Commun. 8, 14049 (2017). cancers. Science 362, pii: eaav1898 (2018).
14. Neal, J. T. et al. Organoid modeling of the tumor immune microenvironment. 47. Li, H. et al. Dysfunctional CD8 T cells form a proliferative,
Cell 175, 1972–1988.e16 (2018). dynamically regulated compartment within human melanoma. Cell 176,
15. Rubin, A. J. et al. Coupled single-cell CRISPR screening and 775–789.e18 (2018).
epigenomic profiling reveals causal gene regulatory networks. Cell 176, 48. Yost, K. E. et al. Clonal replacement of tumor-specific T cells following PD-1
361–376.e17 (2018). blockade. Preprint at bioRxiv https://doi.org/10.1101/648899 (2019).
16. Satija, R., Farrell, J. A., Gennert, D., Schier, A. F. & Regev, A. Spatial 49. Pauken, K. E. et al. Epigenetic stability of exhausted T cells limits durability
reconstruction of single-cell gene expression data. Nat. Biotechnol. 33, of reinvigoration by PD-1 blockade. Science 354, 1160–1165 (2016).
495–502 (2015). 50. Sen, D. R. et al. The epigenetic landscape of T cell exhaustion. Science 354,
17. Zhang, Y. et al. Model-based Analysis of ChIP-Seq (MACS). Genome Biol. 9, 1165–1169 (2016).
R137 (2008). 51. Scott-Browne, J. P. et al. Dynamic changes in chromatin accessibility occur in
18. Becht, E. et al. Dimensionality reduction for visualizing single-cell data using CD8+ T cells responding to viral infection. Immunity 45, 1327–1340 (2016).
UMAP. Nat. Biotechnol. 37, 38–44 (2018). 52. Philip, M. et al. Chromatin states define tumour-specific T cell dysfunction
19. Pliner, H. A. et al. Cicero predicts cis-regulatory dna interactions from and reprogramming. Nature 545, 452–456 (2017).
single-cell chromatin accessibility data. Mol. Cell 71, 858–871.e8 (2018). 53. Pearce, E. L. et al. Control of effector CD8+ T cell function by the
20. Grajales-Reyes, G. E. et al. Batf3 maintains autoactivation of Irf8 for transcription factor eomesodermin. Science 302, 1041–1043 (2003).
commitment of a CD8α(+) conventional DC clonogenic progenitor. Nat. 54. Sullivan, B. M., Juedes, A., Szabo, S. J., von Herrath, M. & Glimcher, L. H.
Immunol. 16, 708–717 (2015). Antigen-driven effector CD8 T cell function regulated by T-bet. Proc. Natl
21. Farh, K. K.-H. et al. Genetic and epigenetic fine mapping of causal Acad. Sci. USA 100, 15818–15823 (2003).
autoimmune disease variants. Nature 518, 337–343 (2015). 55. Intlekofer, A. M. et al. Effector and memory CD8+ T cell fate coupled by
22. Mumbach, M. R. et al. Enhancer connectome in primary human cells T-bet and eomesodermin. Nat. Immunol. 6, 1236–1244 (2005).
identifies target genes of disease-associated DNA elements. Nat. Genet. 49, 56. Chou, C. et al. c-Myc-induced transcription factor AP4 is required for host
1602–1612 (2017). protection mediated by CD8+ T cells. Nat. Immunol. 15, 884–893 (2014).
23. GTEx Consortium et al. Genetic effects on gene expression across human 57. Yu, B. et al. Epigenetic landscapes reveal transcription factors that regulate
tissues. Nature 550, 204–213 (2017). CD8+ T cell differentiation. Nat. Immunol. 18, 573–582 (2017).
NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology 935
Articles Nature BiotechNology
for sorting cells, J. Chevillet for training, Z. Bent and M. Dodge for reagents
58. Phan, A. T. et al. Constitutive glycolytic metabolism supports CD8+ T cell
development, R. Gerver and W. Wang for microfluidics and A. Gallegos, A. Gonzales,
effector memory differentiation during viral infection. Immunity 45,
N. Keivanfar, S. Maheshwari, P. Marks, J. Mellen, R. Rico and K. Wu for computational
1024–1037 (2016).
and software support. We thank X. Ji, D. Wagh and J. Coller at the Stanford
59. Mackay, L. K. et al. The developmental pathway for CD103(+)CD8+
Functional Genomics Facility and C. Bruce at 10x Genomics for sequencing support,
tissue-resident memory T cells of skin. Nat. Immunol. 14, 1294–1301 (2013).
and A. Valencia for assistance with clinical specimen processing. This work was
60. Au-Yeung, B. B. et al. A sharp T-cell antigen receptor signaling threshold for
supported by the National Institutes of Health grant nos. P50HG007735 (H.Y.C.
T-cell proliferation. Proc. Natl Acad. Sci. USA 111, E3679–E3688 (2014).
and W.J.G.), K08CA230188 (A.T.S.), K99-AG059918 (M.R.C.), UM1HG009442
61. Chen, J. et al. NR4A transcription factors limit CAR T cell function in solid
(H.Y.C. and W.J.G.) and S10OD018220 (Stanford Functional Genomics Facility),
tumours. Nature 567, 530–534 (2019).
the Parker Institute for Cancer Immunotherapy (A.T.S. and H.Y.C.), the Michelson
62. Milner, J. J. et al. Runx3 programs CD8+ T cell residency in non-lymphoid
Foundation (A.T.S.) and the Scleroderma Research Foundation (H.Y.C.). A.T.S.
tissues and tumours. Nature 552, 253–257 (2017).
was supported by a Bridge Scholar Award from the Parker Institute for Cancer
63. Khan, O. et al. TOX transcriptionally and epigenetically programs CD8+
Immunotherapy, a Career Award for Medical Scientists from the Burroughs Wellcome
T cell exhaustion. Nature 571, 211–218 (2019).
Fund and the Human Vaccines Project Michelson Prize for Human Immunology and
64. Scott, A. C. et al. TOX is a critical regulator of tumour-specific T cell
Vaccine Research. K.E.Y. was supported by the National Science Foundation Graduate
differentiation. Nature 571, 270–274 (2019).
Research Fellowship Program (NSF DGE-1656518) and a Stanford Graduate Fellowship.
65. Alfei, F. et al. TOX reinforces the phenotype and longevity of exhausted
W.J.G. is a Chan Zuckerberg Biohub investigator and acknowledges grant nos. 2017–
T cells in chronic viral infection. Nature 571, 265–269 (2019).
174468 and 2018–182817 from the Chan Zuckerberg Initiative. H.Y.C. is an investigator
66. Quigley, M. et al. Transcriptional analysis of HIV-specific CD8+ T cells shows
of the Howard Hughes Medical Institute.
that PD-1 inhibits T cell function by upregulating BATF. Nat. Med. 16,
1147–1151 (2010).
67. Martinez, G. J. et al. The transcription factor NFAT promotes exhaustion of Author contributions
activated CD8+ T cells. Immunity 42, 265–278 (2015). A.T.S., J.M.G., G.X.Y.Z., W.J.G. and H.Y.C. conceived the project. A.T.S., J.M.G.,
68. Man, K. et al. Transcription factor IRF4 promotes CD8+ T cell exhaustion Y.Q., K.E.Y., M.R.C., M.R.M., S.E.P., F.M., G.P.M., J.C.B., D.J., C.M.N., J.W. and Y.Y.
and limits the development of memory-like T cells during chronic infection. performed experiments. J.M.G. led the analysis of scATAC-seq data. B.N.O., P.S. and
Immunity 47, 1129–1141.e5 (2017). L.W. contributed to the Cell Ranger ATAC software and contributed to data analysis with
69. Bindea, G. et al. Spatiotemporal dynamics of intratumoral immune cells P.G.G. A.L.S.C. obtained clinical specimens. A.T.S., H.Y.C., W.J.G. and G.X.Y.Z. guided
reveal the immune landscape in human cancer. Immunity 39, 782–795 (2013). experiments and data analysis. A.T.S., J.M.G., G.X.Y.Z., W.J.G. and H.Y.C. wrote the
70. Gu-Trantien, C. et al. CD4+ follicular helper T cell infiltration predicts breast manuscript with input from all authors.
cancer survival. J. Clin. Invest. 123, 2873–2892 (2013).
71. Zappasodi, R. et al. Non-conventional inhibitory CD4+ Foxp3-PD-1hi T cells Competing interests
as a biomarker of immune checkpoint blockade activity. Cancer Cell 33,
H.Y.C. is a cofounder of Accent Therapeutics and Epinomics and is an adviser to 10x
1017–1032.e7 (2018).
Genomics and Spring Discovery. W.J.G. is a cofounder of Epinomics and an adviser to
72. Locci, M. et al. Activin a programs the differentiation of human TFH cells.
10x Genomics, Guardant Health and Centrillion. A.T.S. is an advisor to Immunai. F.M.,
Nat. Immunol. 17, 976–984 (2016).
G.P.M., B.N.O., P.S., J.C.B., D.J., C.M.N., J.W., L.W., Y.Y., P.G.G. and G.Y.Z. are employees
73. Baumjohann, D. et al. Persistent antigen and germinal center B cells sustain T
of 10x Genomics. A.L.S.C. was an advisory board member and clinical investigator for
follicular helper cell responses and phenotype. Immunity 38, 596–605 (2013).
studies sponsored by Merck, Regeneron, Novartis, Galderma and Genentech Roche.
74. Wherry, E. J. & Kurachi, M. Molecular and cellular insights into T cell
Stanford University holds patents on ATAC-seq, on which P.G., W.J.G. and H.Y.C. are
exhaustion. Nat. Rev. Immunol. 15, 486–499 (2015).
named as inventors.
75. Crawford, A. et al. Molecular and transcriptional basis of CD4+ T cell
dysfunction during chronic infection. Immunity 40, 289–302 (2014).
76. Elsaesser, H., Sauer, K. & Brooks, D. G. IL-21 is required to control chronic Additional information
viral infection. Science 324, 1569–1572 (2009). Supplementary information is available for this paper at https://doi.org/10.1038/
77. Yi, J. S., Du, M. & Zajac, A. J. A vital role for interleukin-21 in the control of s41587-019-0206-z.
a chronic viral infection. Science 324, 1572–1576 (2009).
Reprints and permissions information is available at www.nature.com/reprints.
78. Fröhlich, A. et al. IL-21R on T cells is critical for sustained functionality and
control of chronic viral infection. Science 324, 1576–1580 (2009). Correspondence and requests for materials should be addressed to G.X.Y.Z., W.J.G.
or H.Y.C.
Acknowledgements Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in
We thank members of the Chang and Greenleaf laboratories and 10x Genomics published maps and institutional affiliations.
for helpful discussions. We thank the following people at 10x Genomics: A. Puleo © The Author(s), under exclusive licence to Springer Nature America, Inc. 2019
936 NATuRE BiOTECHNOLOGY | VOL 37 | AUGUST 2019 | 925–936 | www.nature.com/naturebiotechnology
Nature BiotechNology Articles
Methods Nuclei isolation. Isolation, washing and counting of nuclei suspensions
were performed according to the Demonstrated Protocol: Nuclei Isolation
Human subjects. This study was approved by the Stanford University
for Single Cell ATAC Sequencing (10x Genomics). Briefly, 100,000 to
Administrative Panels on Human Subjects in Medical Research. Written informed
1,000,000 cells were added to a 2-ml microcentrifuge tube and centrifuged
consent was obtained from all participants, and all relevant ethical regulations
(300g for 5 min at 4 °C). The supernatant was removed without disrupting
regarding human research participants were followed.
the cell pellet, and 100 µl chilled Lysis Buffer (10 mM Tris-HCl (pH 7.4), 10 mM
NaCl, 3 mM MgCl, 0.1% Tween-20, 0.1% Nonidet P40 Substitute, 0.01%
Cell lines and PBMC/bone marrow samples. Human (GM12878) and Mouse 2
digitonin and 1% BSA) was added and pipette-mixed 10 times.
A20 (ATCC TIB-208) B lymphocytes were acquired and cultured according to
The microcentrifuge tube was then incubated on ice, with the length of
guidelines from Coriell and the American Type Culture Collection, respectively.
time optimized for each cell type: GM12878 and A20 cell lines were incubated
Fresh PBMCs, GM12878 and A20 cells were frozen according to the instructions
for 5 min, peripheral blood and bone marrow cells were incubated for 3 min and
outlined here: https://assets.ctfassets.net/an68im79xiti/2ptJYphPcPGfSPisq0c
BCC cells were incubated for 3 min. Following lysis, 1 ml chilled Wash Buffer
Vuu/c8a83f93383c2fd1ce7cc49abc837992/CG000169_DemonstratedProtocol_
(10 mM Tris-HCl (pH 7.4), 10 mM NaCl, 3 mM MgCl, 0.1% Tween-20 and 1%
NucleiIsolation_ATAC_Sequencing_Rev_B.pdf. Briefly, PBMCs were 2
BSA) was added and the resulting solution was pipette-mixed 5 times. Nuclei
cryopreserved in IMDM + 40% FBS + 15% dimethylsulfoxide. GM12878 and were centrifuged (500g for 5 min at 4 °C) and the supernatant removed without
A20 cells were cryopreserved in RPMI + 15% FBS + 5% dimethylsulfoxide. disrupting the nuclei pellet. Nuclei were resuspended in chilled Diluted Nuclei
For monocyte and T cell mixing experiments, nuclei were first extracted and
Buffer (10x Genomics; 2000153) at approximately 5,000–7,000 nuclei per µl
transposed, then mixed at indicated ratios. To avoid pipetting errors, a large
based on the starting number of cells. The resulting nuclei concentration was
number of nuclei were mixed after nuclei extraction and transposition, and a
then determined using a Countess II FL Automated Cell Counter. Nuclei were
smaller number of nuclei were loaded onto the microfluidics chip for scATAC
then immediately used to generate scATAC-seq libraries as described in the
library generation. We also conducted a similar mixing experiment using naïve
methods and table below. For low-cell-number BCC samples (less than 20,000
and memory T cells (Supplementary Table 2), which performed similarly and is
cells), 2 modifications were made to the nuclei isolation protocol. First, 50 µl
included in the Data availability section.
chilled Lysis Buffer was used instead of 100 µl chilled Lysis Buffer. Second,
Healthy volunteer PBMC and bone marrow samples were obtained
isolated nuclei were resuspended in 7 µl chilled Diluted Nuclei Buffer; 2 µl
from AllCells or the Stanford Blood Center. Mononuclear cells from each
was used for cell counting, and 5 µl was used in the downstream library
sample were isolated by Ficoll separation and cryopreserved in IMDM + 40% construction protocol.
FBS + 15% dimethylsulfoxide. Samples were then thawed at 37 °C for 5 min and
resuspended in media before cell enrichment using magnetic-activated cell sorting
(MACS) or FACS (Supplementary Table 4). All MACS-enriched populations Library construction. scATAC-seq libraries were prepared according to
were obtained from AllCells and isolated per manufacturer recommendations the Chromium Single Cell ATAC Reagent Kits User Guide (10x Genomics;
(as outlined in Supplementary Table 4). FACS-isolated populations were CG000168 Rev B). Briefly, after counting, nuclei concentrations were
obtained from AllCells or the Stanford Blood Center and sorted as follows. adjusted to the desired capture number, based on the number of available nuclei
CD4+ T cells were sorted as naïve T cells (CD4+CD25−CD45RA+) or memory and the desired multiplet rate (described in the table below). A slightly higher
T cells (CD4+CD25−CD45RA−) using the following antibodies: anti-CD45RA- number of nuclei were used to account for losses in subsequent
PERCPCy5.5 (clone HI100, cat. no. 304107, lot no. B213966, BioLegend), anti- steps. To minimize potential multiplets, we typically aimed to capture <6,000
CD4-APC-Cy7 (clone OKT4, cat. no. 317417, lot no. B207751, BioLegend) and nuclei per channel. Next, 5 µl of the resulting resuspended nuclei were
anti-CD25-FITC (clone BC96, cat no. 302603, lot no. B168869, BioLegend). combined with ATAC Buffer (10x Genomics; 2000122) and ATAC Enzyme
DCs and basophils were sorted as CD3−CD19−CD11c+HLA-DR+ (DCs) and (Tn5 transposase, 10x Genomics; 2000123/2000138) to form a transposition
CD3−CD19−CD123+ (basophils) using the following antibodies: anti-CD11C- mix, which was then incubated for 60 min at 37 °C. The ATAC Buffer
PECy7 (clone B-ly6, cat. no. 561356, lot no. 4125556, BD Biosciences), anti-HLA- composition was derived from the Omni-ATAC buffer and designed based
DR-APC-Cy7 (clone G46-6, cat. no. 335796, BD Biosciences), anti-CD123-BV421 on quality control experiments in bulk cells, as previously described5. Mild
(clone 6H6, cat. no. 306018, lot no. B156518, BioLegend), anti-CD3-FITC (clone detergent conditions were chosen to keep nuclei intact during tagmentation,
OKT3, cat. no. 11-0037-41, lot no. 2007722, Invitrogen; dump gate) and anti- as previously described5,8. A master mix composed of Barcoding Reagent
CD19-AlexaFluor 488 (clone HIB19, cat. no. 302219, lot no. B238185, BioLegend; (10x Genomics; 2000124), Reducing Agent B (10x Genomics; 2000087) and
dump gate). All antibodies were validated by the manufacturer in human Barcoding Enzyme (10x Genomics; 2000125/2000139) was then added to
peripheral blood samples, used at a 1:200 dilution, and compared with isotype and the same tube as transposed nuclei. The resulting solution was loaded onto a
no staining control samples. Chromium Chip E (10x Genomics; 2000121) in a Chip Holder (10x Genomics;
330019). Vortexed Chromium Single Cell ATAC Gel Beads (10x Genomics;
BCC sample collection and cell sorting. All patients recruited for this study 2000132) and Partitioning Oil (10x Genomics; 220088) were also loaded onto
had locally advanced or metastatic BCC and were poor candidates for surgical the same Chromium Chip E before attaching a 10x Gasket (10x Genomics;
resection. To minimize non-therapy-related immune cell variation, we excluded 370017/3000072) and placing into a Chromium Single Cell Controller instrument
patients with previous exposures to checkpoint blockade, or to systemic immune (10x Genomics).
suppressants within 4 weeks of biopsy. Fresh BCC biopsies were collected and Approximately 100,000 GEMs are formed in each channel (8 channels per
digested in 5 ml DMEM/F12 + 250 μg ml−1 Liberase TL and 200 U ml−1 DNAse I microfluidic chip), and approximately 80% of GEMs contain a single gel bead.
with the gentleMACS Octo system at 37 °C for 3 h at 20 r.p.m. After tissue pieces Gel beads oligos were newly designed to consist of a 29-bp sequencing adapter,
were fully digested, 50 μl 500 mM EDTA was added and samples were collected a 16 bp barcode selected from ~750,000 designed sequences (to index droplets)
by centrifugation at 300g for 5 min. Single-cell suspensions were filtered through and the first 14 bp of read 1N (primers of the linear amplification reaction).
70-μm mesh and pelleted by centrifugation at 300g at 4 °C for 10 min. Finally, cells Oligonucleotide sequences are provided below and in Supplementary Table 1
were resuspended in 1 ml RPMI and cryopreserved in FBS supplemented with 10% and are not chemically modified. Resulting single-cell GEMs were collected at
dimethylsulfoxide. the completion of the run (~7 min) and linear amplification was performed in
Cells were gently thawed at 37 °C for 5 min and resuspended in RPMI + 15% a C1000 Touch Thermal cycler with 96-Deep Well Reaction Module (Bio-Rad;
FBS before FACS. Cells were stained with anti-CD45 V500 (clone HI30, cat. no. 1851197): 72 °C for 5 min, 98 °C for 30 s, cycled 12×: 98 °C for 10 s, 59 °C for 30 s
560779, lot no. 7172744, BD Biosciences), anti-CD3 FITC (clone OKT3, cat. no. and 72 °C for 1 min. Emulsions were coalesced using the Recovery Agent (10x
11-0037-41, lot no. 2007722, Invitrogen), anti-CD8 Pacific Blue (clone 3B5, cat. no. Genomics; 220016), then subjected to Dynabeads (2000048) and SPRIselect
MHCD0828, lot no. 1964935, Invitrogen), anti-PD-1 APC/Cy7 (clone EH12.2H7, reagent (Beckman Coulter; B23318) bead clean-ups. Indexed sequencing libraries
cat. no. 329921, lot no. B245235, BioLegend) and anti-HLA-DR eVolve 605 (clone were constructed by combining the barcoded linear amplification product with a
LN3, cat. no. 83-9956-41, lot no. 1949784, Affymetrix-eBioscience). All antibodies sample index PCR mix comprising SI-PCR Primer B (10x Genomics; 2000128),
were used at a 1:200 dilution, with the exception of anti-CD45 and anti-HLA-DR Amp Mix (10x Genomics; 2000047/2000103) and Chromium i7 Sample Index
antibodies, which were used at a 1:100 dilution. Propidium iodide (cat. no. P3566, Plate N, Set A (10x Genomics; 3000262). Amplification was performed in a
Invitrogen) was used for live/dead staining at a final concentration of 2.5 μg ml−1. C1000 Touch Thermal cycler with 96-Deep Well Reaction Module: 98 °C for 45 s,
Propidium iodide-negative live cells were sorted as T cells (CD45+CD3+), non-T cycled variable amounts depending on cell load: 98 °C for 20 s, 67 °C for 30 s,
immune cells (CD45+CD3−) or tumor/stromal cells (CD45−CD3−) and further 72 °C for 20 s, with a final extension of 72 °C for 1 min. The sequencing libraries
processed using scATAC-seq. were subjected to a final bead clean-up SPRIselect reagent and quantified by
quantitative PCR (KAPA Biosystems Library Quantification Kit for Illumina
scATAC-seq using the 10x Chromium platform. All protocols to platforms; KK4824). Sequencing libraries were loaded on an Illumina sequencer
generate scATAC-seq data on the 10x Chromium platform, including with 2 × 50 paired-end kits using the following read length: 50 bp read 1N, 8 bp
sample preparation, library preparation and instrument and sequencing i7 index, 16 bp i5 index and 50 bp read 2N. In the sequencing reaction, reads 1N
settings, are described below and are also available here: https:// and 2N contain the DNA insert, while the index reads, i5 and i7, capture the cell
support.10xgenomics.com/single-cell-atac. barcodes and sample indices, respectively.
NATuRE BiOTECHNOLOGY | www.nature.com/naturebiotechnology
Articles Nature BiotechNology
scATAC-seq nuclei capture and sequencing specifications ‘original’ and the other read pairs in the group were marked as duplicates of the
fragment in the BAM file.
Nuclei capture Resuspension concentration before Volume used in
desired ATAC reaction (nuclei per µl) ATAC reaction (µl) scATAC-seq data analysis. Filtering cells by TSS enrichment and unique fragments.
500 153 5 Enrichment of ATAC-seq accessibility at TSSs was used to quantify data quality
without the need for a defined peak set. Calculating enrichment at TSSs was
1,000 306 5
performed as previously described46, and TSS positions were acquired from the
2,000 612 5 Bioconductor package from ‘TxDb.Hsapiens.UCSC.hg19.knownGene’. Briefly,
3,000 918 5 Tn5-corrected insertions were aggregated ±2,000 bp relative to each unique TSS
genome-wide (TSS strand-corrected). Then, this profile was normalized to the
4,000 1,224 5
mean accessibility ±1,900–2,000 bp from the TSS and smoothed every 51 bp in R.
5,000 1,530 5 The calculated TSS enrichment represents the maximum of the smoothed profile
6,000 1,836 5 at the TSS. We then filtered all scATAC-seq profiles to keep those that had at least
1,000 unique fragments and a TSS enrichment of 8. To minimize the contribution
7,000 2,142 5
of potential doublets to our analysis, we removed scATAC-seq profiles that had
8,000 2,448 5 more than 45,000 unique nuclear fragments.
9,000 2,754 5
10,000 3,060 5 Generating a counts matrix. To make a cell by feature counts matrix, we first read
each fragment into R using readr. Next, we converted fragment GenomicRanges
into Tn5 insertion GenomicRanges by concatenating GenomicRanges for each
instrument Loading concentration (pM) PhiX (%) ‘start’ and ‘end’ of the fragments (1 bp width). Next, we used ‘findOverlaps’ to
NextSeq 500 1.7 1 find all overlaps with the feature by insertions. Then we added a column with the
unique identity (ID) (integer) cell barcode to the overlaps object and fed this into a
HiSeq 2500 (RR) 11 1
sparseMatrix in R. To calculate the fraction of Tn5 insertions in peaks, we used the
HiSeq 4000 180 1 colSums of the sparseMatrix and divided it by the number of insertions for each
NovaSeq 250 1 cell ID barcode using ‘table’ in R. The counts matrix was then log-normalized using
edgeR’s ‘cpm(matrix, log = TRUE, prior.count = 3)’ in R. The prior count is used
to lower the contribution of variance from elements with lower count values. This
Name Sequence (5ʹ–3ʹ) normalization assumes that differences in total chromatin accessibility across cell
Read 1N TCGTCGGCAGCGTCAGATGTGTA types are minor.
TAAGAGACAG
Read 2N GTCTCGTGGGCTCGGAGATGTG Generating union peak sets with LSI. We created a union peak set by adapting
TATAAGAGACAG a previous workflow12 as follows. Before calling peaks, we constructed 2.5-kb
windows that were tiled across the genome by using ‘tile(hg19chromSizes,
Gel Bead Oligo Primer AATGATACGGCGACCACCGAGATCTA
width = 2500)’ in R. Next, a cell-by-window sparse matrix was computed by
(PN-2000132) CAC-NNNNNNN
counting the Tn5 insertion overlaps for each cell using ‘findOverlaps’ in R, as
NNNNNNNNN-TCGTCGGCAGCGTC
described above. This matrix was then binarized and pruned to the top 20,000
SI-PCR Primer B (PN- AATGATACGGCGACC most accessible sites across all cells. We then reduced the dimensionality as
2000128) ACCGAGA previously described by computing the term frequency-inverse document
i7 Sample Index Plate N, Set CAAGCAGAAGACGGC frequency (TF-IDF) transformation9. Briefly, we divided each index by the colSums
A (PN-3000262) ATACGAGAT-NNNNNNNN-GTC of the matrix to compute the cell ‘term frequency’. Next, we multiplied these
TCGTGGGCTCGG values by log(1 + ncol(matrix)/rowSums(matrix)), which represents the ‘inverse
document frequency’. This normalization resulted in a TF-IDF matrix that was
used as the input to irlba’s singular value decomposition (SVD) implementation
Availability of data processing and analysis software. All data processing steps in R. We then retained only the 2nd to 25th dimensions (first dimension was
and methods used in the manuscript are described in detail below. We also have associated with cell read depth12) and created a Seurat object and identified
designed and made the following tools freely available: crude clusters using Seurat’s SNN graph clustering (v.2.3) with ‘FindClusters’
Cell Ranger ATAC: This software performs initial data processing of scATAC- with a default resolution of 0.8. If the minimum cluster size was below 200 cells,
seq reads (including de-multiplexing, genome alignment and read deduplication), the resolution was decreased until this criterion was reached, leading to a final
as described below and used in this manuscript. This software will also perform resolution of 0.8 × N (where N represents the iterations until the minimum cluster
additional downstream analysis, including the identification of open chromatin size is 200 cells).
regions, motif annotations and differential accessibility analysis, similar to what The rationale for the 200-cell cut-off was to generate an initial cell clustering
was performed in this manuscript and described at https://support.10xgenomics. to identify confident ATAC-seq peaks (using MACS2 (ref. 17)) on grouped cells.
com/single-cell-atac/software/pipelines/latest/what-is-cell-ranger-atac. It is important to note that this cut-off is only used for peak calling, and not
Loupe Cell Browser: This is an interactive visualization software that shows for identifying cell types, and therefore rare cell types can still be clustered and
ATAC-seq peak profiles for scATAC-seq cell clusters, similar to the analysis done analyzed in the final round of clustering. The theoretical ideal cluster size for the
in this manuscript and described at https://support.10xgenomics.com/single-cell- purpose of peak calling is the least number of cells required to recapitulate a bulk
atac/software/visualization/latest/what-is-loupe-cell-browser. profile. In other words, the cluster should be large enough to capture bulk peaks,
but small enough to preserve rare cell type clusters and peaks. To determine this
Data processing using Cell Ranger ATAC software. The Cell Ranger Software number, we performed the down-sampling analyses shown in Supplementary Figs. 1d
(v.1.0; https://support.10xgenomics.com/single-cell-atac/software/pipelines/latest/ and 3f, which identified ~200 cells as a threshold at which ~70–80% of bulk peaks
algorithms/overview) was used for alignment, deduplication and identification of could be recovered in cell lines and primary cells. In samples where cell types of
transposase cut sites. First, the 16-bp barcode sequence was processed to fix the interest are likely to be significantly less frequent than 200 cells, we suggest the
occasional sequencing error in barcodes. Barcode sequences were obtained from following workflow. A preliminary analysis of final clusters could be performed to
the i5 index reads. An observed barcode not present in the whitelist of barcodes determine the presence and frequency of rare cell types. If the cell type of interest is
can be corrected to a whitelist barcode if it is within 2 Hamming distance away indeed less frequent than 200 cells, the number of cells sampled could be increased,
and has >90% probability of being the real barcode (based on the abundance of or rare cells could be enriched before scATAC-seq to obtain a more accurate
the barcode and quality value of incorrect bases). Then, the cutadapt tool was used representation of accessible sites in this population.
to identify and trim any adapter sequence in each read. Third, the trimmed read Peak calling for each cluster was performed independently to get high-quality,
pairs were aligned to a reference using BWA-MEM (Burrows-Wheeler Aligner fixed-width, nonoverlapping peaks that represent the epigenetic diversity of all
Maximal Exact Matches algorithm) with default parameters. Reads less than 25 bp samples46. For each cluster, peak calling was performed on Tn5-corrected single-
were not aligned and flagged as unmapped. Fragments were identified as read pairs base insertions (each end of the Tn5-corrected fragments) using the MACS2
with mapping quality (MAPQ) > 30, nonmitochondrial reads and not chimerically callpeak command with parameters ‘–shift -75–extsize 150–nomodel–call-
mapped. The start and end of the fragments were adjusted (+4 for +strand and −5 summits–nolambda–keep-dup all -q 0.05’. The peak summits were then extended
for −strand) to account for the 9-bp region that the transposase enzyme occupies by 250 bp on either side to a final width of 501 bp, filtered by the ENCODE hg19
during the transposition. Lastly, fragments with identical start and end positions blacklist (https://www.encodeproject.org/annotations/ENCSR636HFF/) and then
were counted once. The most common barcode sequence was assigned to the filtered to remove peaks that extended beyond the ends of chromosomes.
fragments, with ties broken by picking the barcode sequence with the highest Overlapping peaks called within a single sample were handled using an
read counts. One of the read pairs with that barcode sequence was labeled as the iterative removal procedure as previously described46. First, the most significant
NATuRE BiOTECHNOLOGY | www.nature.com/naturebiotechnology
Nature BiotechNology Articles
peak was kept and any peak that directly overlapped with that significant peak intervals across the genome and comparing read counts in each interval with the
was removed. Then, this process was iterated to the next most significant peak average read count in 100 GC-matched intervals. To overcome the sparsity of
and so on until all peaks were either kept or removed due to direct overlap with a scATAC-seq data, we made two modifications. First, we increased the interval size
more significant peak. This was performed on each cluster’s peak set, and the top to 10 Mb (rather than 2 Mb). Second, in each sample, we compared CNV signals in
200,000 extended summits (ranked by MACS2 score) were retained, generating a tumor cells with those in nontumor cells. CNVs present in both groups are unlikely
‘cluster-specific peak set’ for each cluster. We then normalized the MACS2 peak to represent tumor-relevant CNVs. To do this, we first tiled the genome into 10-Mb
scores (−log10(Q value)) for each sample and converted them to a ‘score quantile’ windows using ‘slidingWindows’ of GenomicRanges for chromosome sizes in R
by converting each individual score to a quantile using ‘trunc(rank(v))/length(v)’ with a step size of 2 Mb. These window positions were then filtered against regions
in R (where v represents the vector of MACS2 peaks scores). This normalization with known artifactual mapping issues using the ENCODE hg19 blacklist with the
method allowed for direct comparisons of peaks across clusters, enabling the ‘setdiff’ function in R. Then, a cell-by-window binarized matrix was constructed,
generation of a union peak set for each dataset. as described above. Next, the insertions per bp was determined within each filtered
We next compiled a union peak set containing the important peaks observed 10-Mb window. The percentage GC nucleotide content was computed for each
across all clusters. First, all cluster peak sets were combined into a cumulative filtered 10-Mb window using the hg19 BSgenome in R. To estimate whether a
peak set and trimmed for overlap using the same iterative procedure mentioned region is amplified, we identified the 100 nearest neighbors based on GC content
above. Again, this procedure kept the most significant (in this case, score quantile) and computed the average log(fold change). If this was above 1, we considered
2
peak and discarded any peak that overlapped directly with the most significant this region a candidate for amplification. This approach was previously validated
peak. Lastly, we removed any peaks that spanned a genomic region containing ‘N’ in bulk ATAC-seq data46. However, we also validated its accuracy with matched
nucleotides and any peaks mapping to the Y chromosome. whole exome sequencing data from an earlier study in two patient samples (SU006
and SU008 pretreatment)48. Indeed, CNVs identified using scATAC-seq were
Reads-in-peaks-normalized bigwigs and sequencing tracks. To visualize ATAC- confirmed by whole exome sequencing.
seq cluster data, we created ATAC-seq signal tracks that were normalized by the
number of reads in peaks, as previously described46. Briefly, we created fragment TF footprinting. We characterized relative TF occupancy through TF footprints, as
files that contained all cells belonging to a specific cluster and then counted the previously described46. For each peak set, we used Catalog of Inferred Sequence
number of Tn5 insertions in the corresponding peak set. The numbers of Tn5 Binding Preferences (CIS-BP) motifs (from chromVAR motifs human_pwms_v1)
insertions were computed in windows genome-wide using ‘slidingWindows(chro to calculate motif positions using motifmatchr ‘matchMotifs(positions = “out”)’.
mSizes,100,100)’. Next, we created a run-length encoding using ‘coverage’ in R and Next, we computed the Tn5 bias for each sample by constructing a hexamer bias
normalized the total reads to a scale factor that normalized the reads-in-peaks to table using ‘oligonucleotidefrequency’ function from Biostrings in R. Then, we
10 million reads within peaks. This object was then converted into a bigwig using calculated a hexamer table for each TF by counting the hexamers relative to each
rtracklayer ‘export.bw’ in R. For plotting tracks, the bigwigs were read into R using stranded motif position ±250 bp from the motif center. Using the sample’s hexamer
rtracklayer ‘import.bw(as = ”Rle”)’ and plotted within R or visualized with WashU frequency table, we could then compute the expected Tn5 insertions by multiplying
Epigenome browser (public browser session links included below). All track figures the hexamer position frequency table by the observed/expected Tn5 hexamer
in this study show groups of tracks with matched normalized y axis scales. frequency. For analysis of TF motifs present in the +5 kb enhancer of PDCD1, we
To visualize scATAC-seq data, we read the fragments into a GenomicRanges searched for CIS-BP motifs with a LogOdds threshold greater than 10.
object in R. We then computed 100-bp sliding windows across each visualized To assess the reproducibility of footprints, we subsampled fragments in each
region with ‘slidingWindows(region,100,100)’. We computed a counts matrix for cluster 2 times at a sampling rate of 60% to have maximum variability. To calculate
Tn5-corrected insertions as described above and then binarized this matrix. We the insertions around these sites, we converted the Tn5-corrected insertions
then returned all nonzero indices from the matrix (cell × 100 bp intervals) and GenomicRanges (see above) into a coverage run-length encoding using ‘coverage’.
plotted them in ggplot2 in R with ‘geom_tile’. For each individual motif, we iterated over the chromosomes, computing a
‘Views’ object using ‘Views(coverage, motif positions)’. This ‘Views’ object was
ATAC-seq-centric LSI clustering and visualization. We clustered scATAC-seq converted to a matrix using ‘as.matrix’ and the colSums for ‘- stranded’ motifs
data using an approach that did not require bulk data or previous knowledge. were reversed and the colSums for not ‘- stranded’ motifs were summed. To better
To achieve this, we adopted the strategy by Cusanovich et. al.9, to compute the compare footprints across samples, we normalized these footprints by the mean
TF-IDF transformation. Briefly, we divided each index by the colSums of the values ±200–250 bp from the motif center. Next, we divided the footprints by
matrix to compute the cell ‘term frequency’. Next, we multiplied these values by the expected Tn5 bias to attempt to account for the inherent Tn5 bias. While this
log(1 + ncol(matrix)/rowSums(matrix)), which represents the ‘inverse document strategy is effective, it does not fully account for all of Tn5’s sequence bias. We then
frequency’. This resulted in a TF-IDF matrix that was used as input to irlba’s SVD plotted the mean and standard deviation for each footprint pseudo-replicate.
implementation in R. We then used the first 50 reduced dimensions as input into
a Seurat object, and crude clusters were identified using Seurat’s (v2.3) SNN graph ChromVAR. In addition to TF footprinting, we measured global TF activity using
clustering ‘FindClusters’ with a default resolution of 0.8. We found that there was chromVAR4. As input we used the raw insertion counts for all peaks and the CIS-
detectable batch effect that confounded further analyses. To attenuate this batch BP motif (from chromVAR motifs ‘human_pwms_v1’) matches within these peaks
effect, we calculated the cluster sums from the binarized accessibility matrix and from motifmatchr. We then computed the GC bias-corrected deviation scores
then log-normalized using edgeR’s ‘cpm(matrix, log = TRUE, prior.count = 3)’ using the chromVAR ‘deviationScores’ function. All plots used the ‘deviationScores’
in R. Next, we identified the top 25,000 varying peaks across all clusters using in R and variability was computed by using ‘rowVars’ in R.
‘rowVars’ in R. This was done on the cluster log-normalized matrix rather than the
sparse binary matrix because: (1) it reduced biases due to cluster cell sizes, and (2) Computing gene activity scores using Cicero co-accessibility. We calculated gene
it attenuated the mean-variability relationship by converting to log space with a activity scores (gene scores) using the R package Cicero, as previously described19.
scaled prior count. The 25,000 variable peaks were then used to subset the sparse Briefly, Cicero calculates peak-to-peak links based on their co-accessibility across
binarized accessibility matrix and recompute the TF-IDF transform. We used SVD groups of cells that are aggregated using a nearest-neighbor approach (k = 50).
on the TF-IDF matrix to generate a lower dimensional representation of the data After peak-to-peak links are identified using cell groups, ATAC-seq counts within
by retaining the first 50 dimensions. We then used these reduced dimensions as co-accessible sites (for example, linked to a specific gene) can be calculated and
input into a Seurat object and crude clusters were identified using Seurat’s (v.2.3) visualized in each single cell in the total dataset. We first used the sparse binary
SNN graph clustering ‘FindClusters’ with a default resolution of 0.8. These same matrix and created cellDataSet, detectedGenes and estimatedSizeFactors. Next,
reduced dimensions were used as input to Seurat’s ‘RunUMAP’ with default we created a ‘cicero_cds’ with k = 50 and the ‘reduced_coordinates’ from the
parameters and plotted in ggplot2 using R. corresponding UMAP coordinates. This function returns aggregated accessibility
For subclustering analyses (hematopoiesis: CD34+ bone marrow and DCs; across groupings of cells based on nearest-neighbor rules. We then used this
tumor: T cells), we computed the cluster sums again and log-normalized using aggregated accessibility matrix to identify all peak-to-peak linkages that were
edgeR’s ‘cpm(matrix, log = TRUE, prior.count = 3)’ in R. We identified the top within 250 kb by resizing the peaks to 250 kb and then overlapping them with the
10,000 and 5,000 varying peaks for CD34+ cells and T cells, respectively. These peak summits/centers. We removed all duplicates and same peak-to-peak links.
variable peaks were then used to subset the sparse binarized accessibility matrix Next, we calculated the Pearson correlation for each peak-to-peak link and created
and recompute the TF-IDF transform. We then used SVD on the TF-IDF matrix a connections data.frame where the first column was peaki, the second column
to generate a lower dimensional representation of the data by retaining the first 25 was peakj and the third column was co-accessibility (Pearson correlation). We then
dimensions. We then used these reduced dimensions (1–25 and 2–25, respectively) created a gene data.frame by retrieving genes from the TxDb ‘TxDb.Hsapiens.
as input into a Seurat object, and then crude clusters were identified using Seurat’s UCSC.hg19.knownGene’ in R. We altered the start of ‘MEF2C’ to 88014057,
(v2.3) SNN graph clustering ‘FindClusters’ with a default resolution of 0.8. These since this alternative TSS demonstrated stronger promoter accessibility. We then
same reduced dimensions were used as input to Seurat’s ‘RunUMAP’ and plotted resized each gene to its TSS and created a window ±2.5 kb from the TSS and
in ggplot using R. then annotated the ‘cicero_cds’ using ‘annotate_cds_by_site’. We then calculated
gene scores for each scATAC-seq profile using ‘build_gene_activity_matrix’
Inferring copy number amplification. To infer DNA copy number amplifications with a co-accessibility cut-off of 0.35. Lastly, we normalized the gene scores
from scATAC-seq data, we adapted an approach previously used for bulk ATAC- using ‘normalize_gene_activities’ and the read depth of the cells. We adapted
seq data46,79,80. This method estimates CNVs by determining read counts in large gene activity (GA) scores to be more interpretable by further log normalizing by
NATuRE BiOTECHNOLOGY | www.nature.com/naturebiotechnology
