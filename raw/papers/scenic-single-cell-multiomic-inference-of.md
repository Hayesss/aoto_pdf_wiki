---
source_path: /mnt/c/Users/Administrator/Zotero/storage/JSEMK8BT/Bravo González-Blas 等 - 2023 - SCENIC+ single-cell multiomic inference of enhanc.pdf
ingested: 2026-04-23
sha256: 86d7488f9ce73fc3
---

nature methods
Article https://doi.org/10.1038/s41592-023-01938-4
SCENIC+: single-cell multiomic inference of
enhancers and gene regulatory networks
Received: 19 August 2022 Carmen Bravo González-Blas1,2,4, Seppe De Winter 1,2,4, Gert Hulselmans1,2,
Nikolai Hecker 1,2, Irina Matetovici 1,3, Valerie Christiaens1,2,
Accepted: 6 June 2023
Suresh Poovathingal1, Jasper Wouters 1,2, Sara Aibar1,2 & Stein Aerts 1,2
Published online: 13 July 2023
Check for updates Joint profiling of chromatin accessibility and gene expression in individual
cells provides an opportunity to decipher enhancer-driven gene
regulatory networks (GRNs). Here we present a method for the inference
of enhancer-driven GRNs, called SCENIC+. SCENIC+ predicts genomic
enhancers along with candidate upstream transcription factors (TFs) and
links these enhancers to candidate target genes. To improve both recall
and precision of TF identification, we curated and clustered a motif
collection with more than 30,000 motifs. We benchmarked SCENIC+ on
diverse datasets from different species, including human peripheral
blood mononuclear cells, ENCODE cell lines, melanoma cell states and
Drosophila retinal development. Next, we exploit SCENIC+ predictions
to study conserved TFs, enhancers and GRNs between human and mouse
cell types in the cerebral cortex. Finally, we use SCENIC+ to study the
dynamics of gene regulation along differentiation trajectories and
the effect of TF perturbations on cell state. SCENIC+ is available at
scenicplus.readthedocs.io.
Cell identity is encoded by gene regulatory networks (GRNs), in which Computational modeling is an alternative for identifying
transcription factors (TFs) interact with sets of cis-regulatory ele- TFBSs. For example, SCENIC combines single-cell RNA-sequencing
ments (CREs) to control transcription of target genes. CREs are often (scRNA-seq) coexpression networks with TF motif discovery11,12, but it
cell-type-specific and consist of specific TF-binding site (TFBS) com- cannot identify the exact CRE targeted by the TF and it only uses a small
binations. In-depth knowledge of GRNs is important for mechanistic proportion of a gene’s putative regulatory space13,14. With single-cell
understanding of biological aspects underlying development1,2, evolu- chromatin-accessibility data, the accuracy of TFBS predictions can be
tion3,4 and disease5; however, knowledge of TF–target relationships at improved substantially15. In fact, genomic regions that are specifically
the cis-regulatory level is still limited. accessible in a cell type often represent enhancers and are enriched for
Experimental techniques, including chromatin immunoprecipita- TFBS combinations2,14,16–18.
tion and sequencing (ChIP-seq), have yielded a wealth of TF-binding Here, we developed SCENIC+, a computational framework that
datasets. Nevertheless, for tissues with high cell-type diversity combines single-cell chromatin accessibility and gene expression data
it remains challenging to map TFBSs because of the need for large with motif discovery to infer enhancer-driven GRNs (eGRNs).
amounts of homogenous cells. In addition, for most TFs, high-quality
antibodies are lacking. Alternative approaches have recently been SCENIC+ uses more than 30,000 TF motifs to
described that have increased cellular resolution (for example, predict eGRNs
single-cell CUT&Tag6, nano-CT7 and NTT-seq8) or that rely on genetic SCENIC+ is a three-step workflow that involves identifying candidate
tagging (for example, DamID9 and nanoDam10), yet such methods are enhancers, identifying enriched TF-binding motifs and linking TFs
still difficult to scale to all TFs. to candidate enhancers and target genes (Fig. 1a and Supplementary
1VIB Center for Brain & Disease Research, Leuven, Belgium. 2Department of Human Genetics, KU Leuven, Leuven, Belgium. 3VIB Tech Watch, VIB
Headquarters, Ghent, Belgium. 4These authors contributed equally: Carmen Bravo González-Blas, Seppe De Winter. e-mail: stein.aerts@kuleuven.be
Nature Methods | Volume 20 | September 2023 | 1355–1367 1355
Article https://doi.org/10.1038/s41592-023-01938-4
Single-cell multiomics preprocessing : pycisTopic
DR1
TF motif enrichment analysis : pycisTarget
Enhancer-driven GRN inference : SCENIC+
Visualization
Nature Methods | Volume 20 | September 2023 | 1355–1367 1356
2RD
Motif collection database
Motif clustering
PPP WWW MMM 123 TTT FFF77 929 2
t-SNE1
cisTarget databases
TF
r1 r4
r2 r3
g3
g1 g2
pycisTarget DEM
2ENS-t
Wilcoxon, P < 0.05
NES = ((AUC − µ) / σ)
+ + Cumulative recovery of input regions
Average recovery
across all motifs
Set1 Set2
Genomic regions ranked Region set
by motif score
erocs
MRC
Bergman c2h2_zfs cisbp dbtfbs desso elemento factorbook fantomflyfactorsurvey hdpi
62 64 11,491 389 2,786 619 6,921 169 688 191
HOCOMOCO Homer idmmpmm Jaspar kznf neph nitta predrem scertf stark
1,302 436 39 1,956 938 683 426 2,684 196 232
swissregulon taipale taipale_c.m. taipale_t.p. tfdimers tiffin transfac_pub. transfac_pro yetfasco
2,202 820 1,787 664 603 120 398 9,944 244
Leiden clustering based on Cluster-based scoring with
Tomtom similarity STAMP subclustering HMMs
Motif collection
...
Sequences
erocS
Cluster-Buster Motifs
CRM
CRM Motif Motif
Sequences
Region set
snoigeR
Background
Motif 1 0.5
0.5 Motif 2
Cluster-Buster
CRM
scores
database
CRM ranking database
Cluster
1
Cluster
2
Cluster
3
Motifs
snoiger
fo rebmuN
snoigeR
Region sets
Motifs
snoigeR
Set1 versus Set2
Motifs
snoigeR
Cell clustering Enhancer identification Gene expression
>30,000 PWMs
TF annotations
Curated Direct
motif-to-TF TF TF TF Orthology
annotations
eRegulon
Effector TF TF + motif + accessibility + gene expression TF TF TF
Single cell viewer Genome Browser Network app
SCope UCSC Cytoscape
500
400
300
200
100
0
0 25 50 75 100
Number of topics
)s(
emiT
1,500 K562 CGS - cisTopic
HCT116 1,000
CGS - pycisTopic MCF7 Signac DARs 500
ArchR
WarpLDA - cisTopic DARs pycisTopic
HepG2 DARs
Mallet - pycisTopic pycisTopic Topic 0
0 0.03 0.06 0.09 0.12 Human Mouse Fly
Enhancer recovery Species
sFT
fo
rebmuN
Annotation Direct Orthology
200
100
0
0 25 50 75 100
Rank
stih
fo
rebmuN
a d
b c e f
1,553 2 # 8 h 5 its 272 1,357 265 251
240 234 225
206 198
cisTarget (archetype) cisTarget (clustered) 467 cisTarget (unclustered)
cisTarget (SCENIC)
DEM (archetype) DEM (clustered)
DEM (unclustered)
DEM (SCENIC) Homer
Fig. 1 | The SCENIC+ workflow and motif collection. a, SCENIC+ workflow. analysis. d, Workflow to create motif databases for SCENIC+. The SCENIC+ motif
Topics and DARs inferred with pycisTopic are transformed into cistromes collection includes 34,524 unique motifs gathered from 29 motif collections,
of directly bound regions by identifying modules that present significant which were clustered with a two-step strategy. Input regions are scored for each
enrichment of the regulator’s binding motif using pycisTarget. SCENIC+ cluster of motifs using hidden Markov models (HMMs), where each motif of the
integrates region accessibility, TF and target gene expression and cistromes cluster is used as a hidden state. The score-based motif database is used in the
to infer eGRNs, in which TFs are linked to their target regions and these to their DEM algorithm, whereas the ranking-based database is used for cisTarget. NES,
target genes. PWM, position weight matrix; UCSC, University of California, Santa normalized enrichment score. e, Number of TFs in the SCENIC+ motif collection
Cruz. b, Running-time comparison per topic model using cisTopic with Collapsed annotated by direct evidence or orthology. f, Recovery of TFs from 309 ENCODE
Gibbs Sampling or WarpLDA (blue) and pycisTopic with Collapsed Gibbs ChIP-seq datasets using different databases and motif enrichment methods,
Sampling or MALLET (red) for parameter optimization. c, Bar-plots showing the namely Homer, pycisTarget and DEM. The unclustered databases include all
area under the recovery curve (AUC; enhancer recovery) on the top 10% of the annotated motifs before clustering (singlets), the archetype databases use the
ranking based on STARR-seq signal, for the top 5,000 DARs identified by Signac, consensus motifs of the clusters based on STAMP and the clustered databases use
pycisTopic and ArchR and top 5,000 regions from the cell-line-specific topics the motif clusters, scoring regions using all motifs in the cluster. The x axis shows
identified by pycisTopic. The AUC value is scaled by dividing by the maximum the positions in which the TFs targeted in the ChIP-seq experiment can be found
possible AUC at 10% of the ranking. Promoter regions were excluded from the and the y axis shows the cumulative number of TFs that are found at that position.
Article https://doi.org/10.1038/s41592-023-01938-4
Note 1). The output is a set of enhancer-driven regulons (eRegulons) PC3, K562, Panc1 and HCT116) to validate the quality of TFs, target
that form an eGRN. regions, region-to-gene relationships and target genes predicted by
To find candidate enhancers, single-cell analysis of accessible SCENIC+. We benchmarked these predictions to other tools that predict
chromatin (scATAC-seq) data is preprocessed using pycisTopic, a faster (e)GRNs using multiomics data, namely CellOracle31, Pando32, FigR33
Python reimplementation of cisTopic16 (Fig. 1b and Extended Data and GRaNIE34, and included SCENIC11,12 as a baseline (Supplementary
Fig. 1a–f). SCENIC+ uses both differentially accessible regions (DARs) Note 4). SCENIC+ identified 178 TFs. GRaNIE, FigR, SCENIC and Pando
and topics, sets of co-accessible regions, across cell types or states as identified fewer TFs (39, 71, 108 and 157 TFs, respectively), while Cel-
enhancer candidates. Topics are more enriched for functional enhancer lOracle identified 235 TFs (Fig. 3b). On average SCENIC+ predicts 471
regions compared to DARs (Fig. 1c and Extended Data Fig. 1g). and 1,152 target genes and regions per eRegulon (Fig. 3b).
To discover potential TFBSs in candidate enhancers we make use To assess whether the predicted GRNs contain enough infor-
of motif enrichment analysis. For this we created the largest motif mation to recapitulate all biological cell states we performed
collection to date (Supplementary Note 2) and built a Python package principal-component analysis (PCA) based on regulon enrichment
called pycisTarget. pycisTarget implements two algorithms for motif scores. SCENIC+ was able to separate all cell lines, whereas other meth-
enrichment analysis: the cisTarget ranking-and-recovery-based algo- ods mixed two or more cell lines (Fig. 3c).
rithm11,19–21 and a Wilcoxon rank-sum test called differential enrichment Next, we evaluated to what extent the identified TFs are biologically
of motifs (DEM) (Supplementary Note 3). relevant by quantifying the recovery of highly differentially expressed
The motif collection is a secondary database containing 32,765 TFs and TFs with many direct ChIP-seq peaks35,36. SCENIC+ achieved
unique motifs collected from 29 collections (Fig. 1d and Extended the best recovery for both metrics, followed by SCENIC (Fig. 3d,
Data Fig. 2a,b) along with TF annotations. The collection spans a total Extended Data Fig. 4a–c). Notably, TFs identified by SCENIC+ include
of 1,553 TFs, 1,357 TFs and 467 TFs, respectively in human, mouse and most of the known lineage TFs, such as GATA1, TAL1, MYB and LMO2
fly (Fig. 1e and Extended Data Fig. 2c). We clustered all motifs based for K562 (refs. 37–40) or HNF1A, HNF4A, FOXA2 and CEBPB for HepG2
on motif-to-motif similarity and found that scoring candidate regions (ref. 40) or ESR1 and GRHL2 for MCF7 (ref. 41). CellOracle had little
using all motifs within a cluster yields a significantly higher precision recovery of differentially expressed TFs, whereas it recovers a large
and recall compared to using a single ‘archetype’ motif per cluster fraction of non-cell-line-specific TFs (for example GABPA, YY1 and SP1;
(Fig. 1f and Extended Data Fig. 2d–h). Both the cisTarget and DEM Extended Data Fig. 4d).
algorithm outperform Homer22 (Fig. 1f and Extended Data Fig. 2d), As a third criterion, we evaluated the precision and recall of the
with the DEM algorithm enabling detection of differential motifs in predicted target regions of each TF based on TF ChIP-seq data in the
sets of regions with a similar motif content (Extended Data Fig. 2i–j). ENCODE cell lines. For this, we used both unprocessed ChIP-seq peaks
SCENIC+ next uses GRNBoost2 (ref. 23) to quantify the importance of as well as direct ChIP-seq peaks from UniBind35,36 and predicted TF bind-
both TFs and enhancer candidates for target genes and it infers the direc- ing by Enformer42. Overall, the predicted target regions of SCENIC+
tion of regulation (activating/repressing) using linear correlation. Motif and GRaNIE have the highest precision and recall, followed by Pando
enrichment analysis results are combined with GRNBoost2 inferences and CellOracle (Fig. 3e and Extended Data Fig. 4e–g). Furthermore, the
using a second enrichment analysis to recover the best TF for each set of predicted target regions by SCENIC+ have the highest enhancer activity
motifs. This forms the eRegulon, a TF with its set of target regions and genes. as measured by STARR-seq (Extended Data Fig. 4h).
The overall running time and memory of the workflow ranges As a fourth criterion, we assessed the quality of predicted
from 1 h and 21 Gb to 44 h and 461 Gb for the smallest and largest tested region-to-gene associations making use of deeply sequenced Hi-C
dataset, respectively (Extended Data Fig. 3). data on five of the cell lines. SCENIC+ predicts a total of 402,838 links
and has an average correlation coefficient of 0.25 with the Hi-C data
Illustration of SCENIC+ on PBMC multiome data (Fig. 3f and Extended Data Fig. 4i,j). The other methods identify fewer
We first analyzed a publicly available single-cell multiomics dataset links, ranging from 13,123 to 311,168, and have a lower correlation with
containing 9,409 human peripheral blood mononuclear cells (PBMCs) Hi-C data (Fig. 3f and Extended Data Fig. 4i,j).
to showcase and validate SCENIC+. Dimensionality reduction based on Next, we evaluated target gene predictions using three meth-
eRegulon enrichment scores separates the main biological cell states ods. First, we reasoned that correct target gene predictions would
(Fig. 2a). SCENIC+ identified 53 activator eRegulons, targeting a total allow for accurate estimation of target gene expression given the
of 23,470 regions and 6,142 genes. A total of 89% of genes have between expression of the upstream TFs. To this end, we trained a regression
1–10 predicted enhancers and 49% of enhancers are predicted to most model using each method’s predicted eGRN as a scaffold. Predicted
likely regulate the most proximal gene (Fig. 2b). gene expression values using links from SCENIC+ had an average
SCENIC+ recovers well-known master regulators of B cells (EBF1, correlation coefficient of 0.61 with real expression values; this cor-
PAX5 and POU2F2/POU2AF1), T cells (TCF7, GATA3 and BCL11B), natural relation was lower for Pando, GRaNIE, FigR and CellOracle (Extended
killer (NK) cells (EOMES, RUNX3 and TBX21), dendritic cells (SPIB and Data Fig. 5a). Second, we quantified recovery of genes that change
IRF8) and monocytes (SPI1 and CEBPA) (Fig. 2c)24–28. The majority of after knockdown of TFs. Across 157 TF perturbation datasets on the
the top five cell-type-specific TFs show co-binding to shared enhanc- ENCODE cell lines, predicted target genes of SCENIC+ had the high-
ers. Such cooperativity is not observed for TFs that are not specific for est enrichment score per TF (Extended Data Fig. 5b) and the highest
the same cell type (Fig. 2d). In particular, for B cells SCENIC+ suggests precision and recall (Fig. 3g and Extended Data Fig. 5c). Finally, to
cooperativity between EBF1(+), PAX5(+) and POU2F2/AF1(+) (Fig. 2e), better account for indirect effects of TF knockdown experiments
with a strong overlap of most of their predicted target enhancers with either due to indirect interactions or cooperativity (Extended Data
EBF1, PAX5 and POU2F2 ChIP-seq data (Fig. 2f–g). Fig. 5d,e), we performed in silico TF perturbations based on the GRNs
In conclusion, SCENIC+ infers key regulators of different inferred by each method. While only a fraction of the variation in gene
PBMC types and genomic target regions of these regulators in a expression can be explained by any of the GRNs, eGRNs inferred by
high-throughput manner. This can be exploited to infer cooperativity. SCENIC+ agree the best with the experimental data (Extended Data
Fig. 5f and Supplementary Table 1).
Validation of SCENIC+ predictions using ENCODE We performed these benchmark analyses using either motif (or
data ChIP-seq based) databases derived from all consensus peaks or derived
We next used simulated single-cell multiome data from eight ENCODE from the SCREEN43 regions, resulting in similar performance (data
deeply profiled cell lines (Fig. 3a)29,30 (GM12878, IMR90, MCF7, HepG2, not shown). We also assessed the effect of sample size and coverage
Nature Methods | Volume 20 | September 2023 | 1355–1367 1357
Article https://doi.org/10.1038/s41592-023-01938-4
t-SNE1
on the predictions of SCENIC+. SCENIC+ does not perform well with Finally, to test whether the same conclusions can be drawn from a
very few cells with low coverage (80 cells, 3,000 ATAC-seq fragments real single-cell multiome dataset we repeated the benchmark analyses
and 5,000 RNA-seq reads), but works accurately at standard coverage on the PBMC data (Extended Data Fig. 7). GRaNIE is not present in this
(Extended Data Fig. 6). benchmark as it was developed for bulk datasets and did not scale
Nature Methods | Volume 20 | September 2023 | 1355–1367 1358
2ENS-t
B cells
CD4 T cells
CD14+ monocytes
CD8 T cells
Conventional
dendritic cells
NK cells
TBX21(+)
EOMES(+)
RUNX3(+) BNC2(+)
TCF7(+)
LEF1(+)
BCL11B(+)
ZEB1(+)
GATA3(+)
RORA(+)
TCF4(+)
EBF1(+)
PAX5(+)
0.4 POU2AF1(+)
MEF2A(+)
MEF2C(+)
BACH1(+) JDP2(+)
KLF4(+)
0 NR4A1(+)
palrevo
.rf
)+(1FA2UOP
POU2AF1(+)
EBF1(+)
PAX5(+)
)+(1FBE
)+(5XAP
1,000
500
1 11 21
1
eRegulon1 eRegulon2
POU2F2 ChIP-seq EBF1 ChIP-seq
PAX5 ChIP-seq
0 –750 750 1 1
0 0 –750 750 –750 750
1 1 1
0 0 0 –750 750 –750 750 –750 750
ycneuqerF
No. of regions per gene
.rpxe FT erocs z 2 –2 SSR CUA eneG
a b e
c d
EBF1(+)
PAX5(+)
POU2AF1(+)
GATA3(+)
NFATC2(+)
f g
RUNX3(+)
IRF8(+)
TCF4(+)
RARA(+)
SPI1(+)
STAT2(+)
0 0.25 0.50 0.75 1.00
ycneuqerF
nth. gene per region
10,000
Second First
7,500
5,000
2,500
1 11 21
EBF1(+)
PAX5(+)
POU2AF1(+) BCL11B(+)
ETS1(+) 05’
GATA3(+)
KLF12(+)
LEF1(+)
TCF7(+)
ZEB1(+)
IKZF3(+)
RORA(+)
BNC2(+)
EOMES(+)
NFATC2(+)
RUNX3(+)
TBX21(+)
ARID3A(+) BCL11A(+)
IRF8(+)
MYB(+) PPARA(+)
RUNX2(+)
SPIB(+) 130 TCF4(+) B cells
ZBTB18(+) CD14+ ATF3(+) Mono B C A R C EB H 5 1 ( ( + + ) ) CD4+ T
F E O TV SB 6 ( ( + + ) ) CD8+ T
FOS(+) FOXN2(+) cDC
FOXN3(+) FOXO3(+) pDC JDP2(+) FCGR3A+
KLF4(+) Mono
MEF2A(+) NK cells
MEF2C(+) 0 RXRA(+) PAX5 24 STAT1(+)
CEBPA(+) ChIP
CEBPB(+) EBF1 85
IRF5(+) ChIP
MAFB(+) POU2F2 79 MBD2(+) ChIP NR4A1(+)
POU2F2(+) EBF1 PAX5 PAX5 POU2AF1
RARA(+)
SPI1(+) 0.07
STAT2(+) e
STAT6(+) ro
TCF7L2(+) c S C B D c 4+ e C l T l D s c 8+ e l T ls c C N el D K ls 1 c 4+ e F l m l C s p o G D n R C o 3 s c A y + t e m s c o D n C o s cytes 0 96,225,000 B c L h N r1 K 0 position (kb) 96,300,000
1 2 3 4 5 6 7 8 9 3’
stiB
2.0
1.0
05’ 1 2 3 4 5 6 7 8 9 01 3’
stiB
2.0
1.0
05’ 1 1 1 7 7 2 2 2 3 3 8 8 6 6 9 9 0 0 5 5 4 4 1 2 1 1 2 1 1 1 1 1 1 1 2 3’
stiB 2.0 1.0
05’ 1 1 7 2 2 3 3 8 6 90 5 5 4 4 11 1 11 1 3’
stiB
05’
2.0 1.0
1 2 3 4 5 6 7 8 9 3’ stiB
2.0
1.0
05’ 1 2 3 4 5 6 7 8 3’
stiB 2.0 1.0
05’ 1 2 3 4 5 6 7 8 3’ stiB
05’
2.0
1.0
1 2 3 4 5 6 7 8 9 01 3’
stiB 2.0 1.0
05’ 1 2 3 4 5 6 7 8 9 01 3’
stiB
05’
2.0
1.0
1 2 3 4 5 6 7 8 3’
stiB
2.0
1.0
05’ 1 2 3 4 5 3’
stiB
B cells
CD4+ T cells
CD14+ monocytes
pDCs
CD8+ T cells
cDCs
NK cells FCGR3A+
monocytes
2.0
1.0
Fig. 2 | SCENIC+ analysis on peripheral blood mononuclear cells. of the eRegulon in each row. fr., fraction. e, Visualization of the eGRN formed
a, t-SNE dimensionality reduction of 9,409 cells based on target gene and by EBF1, PAX5, POU2AF1 and POU2F2. TF target nodes are restricted to highly
target region enrichment scores of eRegulons. pDC, plasmacytoid dendritic variable genes and regions. f, Aggregated ChIP-seq signal of EBF1, PAX5 and
cell; cDC, conventional dendritic cell. b, Top: distribution of the number of POU2F2 in GM12878 on target regions of either EBF1, PAX5 or POU2AF1 and
regions linked to each gene. Bottom: distribution showing whether the nth combinations of two of these factors. g, Chromatin-accessibility profiles across
closest region to the target gene has the highest region-to-gene importance cell types and ChIP-seq signal together with peak calls of EBF1, PAX5 and POU2F2
score. c, Heat map/dot-plot showing TF expression of the eRegulon on a color in GM12878 on chr10:96226082–96316945. Region–gene links are shown as arcs.
scale and cell-type specificity (RSS) of the eRegulon on a size scale. Cell types Region–gene gradient-boosting machine feature importance scores are encoded
are ordered on the basis of their gene expression similarity. d, Overlap of target as colors (from light to dark blue). Predicted target sites of eRegulons are shown
regions of eRegulons. The overlap is divided by the number of target regions using colored ticks and semi-transparent boxes.
Article https://doi.org/10.1038/s41592-023-01938-4
to this larger (10,000 cells) dataset. GRNs from all methods were SCENIC+ simulates phenotype switching of
able to recapitulate all biological cell states, except the GRN inferred cancer cell states
by FigR (Extended Data Fig. 7d). SCENIC+ and Pando performed Gene regulatory network analysis of cancer cells holds promise to
best in terms of identifying biologically relevant TFs, with Pando identify stable (attractor) cell states and their regulators. As a case study
finding additional TFs compared to SCENIC+ (Extended Data we performed scATAC-seq on nine melanoma cell lines that represent
Fig. 7e,j). SCENIC+ had the highest precision and recall in terms of different melanoma states47,48 and combined these data with previously
target region predictions (Extended Data Fig. 7f). Note that even published scRNA-seq data for the same lines48.
when only scATAC-seq is used to identify TFs per cell type (for exam- Cells clustered in three states based on eRegulon enrichment
ple, ArchR44 and Signac45), the majority of known cell-type-specific scores (Fig. 4a). Furthermore, a Boolean model49 based on the top 25%
TFs could still be recovered with accurate target region predictions TF-to-TF edges from the SCENIC+ network was sufficient to recapitulate
(Extended Data Fig. 7g,h), showing that motif discovery is a powerful all the main cell states (Extended Data Fig. 8a,b).
means for cell-type-specific TF prediction; however, using scATAC-seq SCENIC+ recovered the known regulators for the melanocytic
alone resulted in large amounts of false-positive TF predictions, rep- (MEL) state (MITF, SOX10, TFAP2A and RUNX3), the mesenchymal
resenting TFs that are not expressed in the cell type but have a similar (MES) state (JUN, NFIB and ZEB1) and the intermediate sub-state of
motif (Extended Data Fig. 7i). MEL governed by the MEL TFs supplemented with SOX6, EGR3 and
ETV4 (Fig. 4b and Extended Data Fig. 8c–g)48,50,51. It was previously
SCENIC+ prioritizes functional enhancers suggested that RUNX motifs are part of the MEL enhancer code17,48
SCENIC+ uses automatic thresholding procedures, on the TF–gene, but which member of the RUNX family was unclear. Using SCENIC+,
region–gene and region–motif scores, to obtain discrete sets of eReg- we predict that it is most likely RUNX3 (Fig. 4b).
ulons; however, in some circumstances it may be beneficial to obtain It is known that melanoma cells can dynamically shift state from
a ranking of TFs, regions and genes based on their importance. For MEL to MES and vice versa, driving metastasis and therapeutic resist-
this reason, we implemented a ranking that quantitatively ranks TF– ance, a process called phenotype switching52. Knockouts of specific
region–gene triplets. This ranking is the aggregated ranking46 of the TFs can drive this process48.
TF–region scores, TF–gene scores and region–gene scores (Fig. 3h). To simulate phenotype switching and to prioritize TFs that under-
We tested whether the triplet ranking can be used to prioritize lie this process, we took inspiration from CellOracle31 and GRaNPA34, by
potential enhancers. Indeed, regions in the top 10% of triplets have using SCENIC+ as a feature selection method and training a random for-
a higher ChIP-seq signal, as measured experimentally and in silico by est (RF) regression model for each gene to predict its expression based
Enformer and higher enhancer activity as measured by STARR-seq on the expression of their upstream TFs. After fitting the model, we use
(Fig. 3i). it to predict the effect of a TF perturbation by setting the expression
To further illustrate this, we focused on three master regulators of the TF to zero. To account for indirect effects (TFs targeting other
of HepG2 cells: HNF4A, FOXA2 and CEBPB. Predicted target regions TFs), perturbed gene expression values are propagated over several
of these TFs have a high ChIP-seq coverage for these TFs, as measured iterations. The effect of the simulated perturbation can be visualized by
experimentally and in silico by Enformer (Fig. 3j–l). Regions with high co-embedding the simulated gene expression matrix with the original
ChIP-seq coverage also have a higher TF-to-region ranking, compared one (Fig. 4c).
to those with low coverage (Fig. 3j–l). In comparison, the predicted As proof of principle, we simulated the effect of SOX10 KD on
target regions of the same TFs by GRaNIE, Pando or CellOracle are the MEL state. Notably, the simulated cells, after SOX10 KD, suggest
very sparse. Only for HNF4A the predicted target regions by GRaNIE that they switch to a more MES-like state, whereby MES genes are
correspond well to those of SCENIC+; however, GRaNIE identified a upregulated and MEL genes are downregulated and this effect stabilizes
subset of target regions that have a low Enformer score, even though after four iterations of simulation (Fig. 4d). This predicted effect of
they overlap with a ChIP-seq peak (Fig. 3j). SOX10 knockdown was strongest in the intermediate cell lines and is
Next, we zoomed in on the target region of HNF4A that was pre- fully recapitulated by experimental SOX10 KD, followed by RNA-seq48
dicted to be most important according to the triplet ranking. This (Fig. 4e and Extended Data Fig. 8d).
region is also predicted to be targeted by FOXA2 and CEBPB and is Encouraged by this result, we simulated perturbations of all the
predicted to regulate SPP1 (Fig. 3m), a marker gene of HepG2 cells (aver- identified TFs. Simulated knockdowns of RUNX3, SOX10 and MITF
age log fold change (FC) of 9.24). The region is specifically accessible show the strongest potential to switch cells from MEL to MES; whereas
in HepG2 cells and has a high ChIP-seq signal for HNF4A, FOXA2 and knockdowns of ZEB1, SOX4 or SMAD3 are predicted to cause the reverse
CEBPB (Fig. 3n). Altogether, this region is a strong enhancer candidate switch from MES to MEL (Fig. 4f–g), consistent with the role of these TFs
for SPP1 in HepG2. in epithelial-to-mesenchymal transition (EMT)48,53–57. We also identified
Fig. 3 | Benchmark of SCENIC+ and other single-cell multiomics GRN ChIP-seq coverage on the union of predicted target regions per method with
inference methods using ENCODE deeply profiled cell lines. a, Diagram binary heat map indicating regions found per method and scatter-plot showing
of benchmarking strategy. b, Number of TFs identified per method and TF-to-region (TF2R) ranking of SCENIC+ target regions, for the TFs HNF4A
distributions of the number of target genes and regions per regulon and method. (j), FOXA2 (k) and CEBPB (l). m, Network for top ten edges, targeted by any of
c, PCA based on target gene and region enrichments and ARI quantification FOXA2, HNF4A or CEBPB. Open and closed circles represent regions and genes
(4,000 cells). d, Cumulative recovery, per method, of TFs ranked in descending and their color is proportional to the accessibility/gene expression logFC,
order by maximum logFC based on differential gene expression between all cell respectively. Region-to-gene edges width and color represent importance scores.
lines. e, F1 score distributions from the comparison of regulon target regions, Arrow indicates the highlighted SPP1 enhancer (chr4:88107462–88107963).
per method and UniBind. f, Correlation between Hi-C links for top 100 marker n, Chromatin-accessibility profiles across cell lines and HNF4A, FOXA2 and
genes and region–gene scores per method. Two-sided Wilcoxon rank-sum test CEBPB ChIP-seq coverage on the SPP1 locus, with region-to-gene links and the
comparing mean correlation of links versus shuffled links. The Holm method SPP1 enhancer highlighted. For box-plots in b, e–g and i, the top/lower hinge
was used to correct for multiple testing. g, F1 score distributions from the represents the upper/lower quartile and whiskers extend from the hinge to the
comparison of regulon target genes, per method and TF perturbation data. largest/smallest value no further than 1.5 × interquartile range from the hinge,
h, Diagram of triplet ranking. i, Distributions of experimental and predicted respectively. The median is used as the center. NA, data are not available for the
TF ChIP-seq coverage and STARR-seq logFC target regions and other consensus method. GRaNIE* was run with simulated single-cell data instead of bulk.
peaks (not in eRegulon). j–l, Heat maps showing experimental and predicted
Nature Methods | Volume 20 | September 2023 | 1355–1367 1359
Article https://doi.org/10.1038/s41592-023-01938-4
MXI1 and ZNF487 as potential EMT regulators, warranting further Although several marker TFs have been described for some of these cell
research. This strategy can thus be used to prioritize TFs regulating types, little is known about how precise TF combinations, their binding
cell state and state transitions. sites and their target genes underlie neuronal identity. We reasoned that
two independent SCENIC+ analyses on human and mouse cortex could
Conservation and divergence of eGRNs in the reveal conserved, and thereby, high-confidence eGRNs underlying
mammalian brain cortical cell types. This evaluation, using comparative genomics, also
The mammalian cortex consists of a highly diverse but evolutionary serves as a benchmark for robustly detecting eGRNs despite potential
conserved set of excitatory (pyramidal) and inhibitory neurons58–60. species and dataset-specific biases.
SCENIC+
GRaNIE
PC1
Nature Methods | Volume 20 | September 2023 | 1355–1367 1360
2CP
309 109 5 Bulk RNA 200 No. TFs 235 SCENIC FigR TF ChIP-seq TF perturbationHi-C& bulk ATAC 178 157 MCF7 Panc1 Panc1 IMR90
8 ENCODE deeply profiled cell lines 3,000 0 No. genes 1 p 0 e 8 r regu 3 lo 9 n 71 GM1287 K 8 562 HCT116 IMR P 9 C 0 3 GM K 12 5 8 6 7 2 8 M H C C F T 7 116 I P M C R 3 90 MCF7P P a H C n C c 3 T 1 116
HepG2 GM12878
369 K562
Simulate single-cell multiomes 221 108 42 157 81 HepG2 HepG2
CellOracle Pando
30 PC3 MCF7
No. regions per regulon Panc1 K562 IMR90
Methods benchmark 1,000 NA 42 157 369 NA GM128 H 7 K 8 C 5 T 6 1 2 16 IMR90 MCF7 PC3 Panc1 GM12878 HepG2
PC3
TF
S
r
P C
e
a
c
E n
o
N d
v
IC o
er
+
y/TF–reg
S
io
C F
n
i E
/
g N
R
R
e
IC
gion–gen
C
e
e G
/
l R
T
lO
F
a
–
r N a
g
I c E
e
l
n
e
e
S
10 CENIC+ 221 SCENIC GRaNIE
C
*
ell
Oracle Pando FigR HepG2 HepG2 HCT I 1 M 16 R90 GM12878 HC M T C 1
K
F 16
5
7 P
6
a
2
nc1
56
54
60
19
erocs
1F
TF-to-region 1 × 10–1
NA NA
1 × 10–4
sknil
C-iH
htiw
noitalerroC
a b c
d e f g
1.0 2.0 × 10–21 6.2 × 10–98.5 × 10–2 Region-to-gene 4.7 × 10–23
1 × 10–1
NA NA
0
254
3 × 10–3
358 291
–1.0 342
erocs
1F
TF-to-gene
TF1
TF–region
TF–gene r1 r3
r2 Region–gene
g4 g1 g2
g3
Triplet Aggregated ranking
TF1;r1;g1
TF1;r3;g4
TF1;r1;g2
TF1;r2;g3
0 2 4 6 8 10
0 002 004 0 652 215 EINaRG odnaP +CINECS elcarOlleC
10
0
1 2.5 × 104
TF2R
egarevoc
qes-PIhC
30
10
erocs
remrofnE
HNF4A
0 002 004 0 652 215 EINaRG odnaP +CINECS elcarOlleC
10
5
432.4 × 104
TF2R
egarevoc
qes-PIhC
30
10
erocs
remrofnE
FOXA2
0 002 004 0 652 215 EINaRG odnaP +CINECS elcarOlleC
7.5
2.5
202 × 104
TF2R
egarevoc
qes-PIhC
15
5
erocs
remrofnE
CEBPB
qes-PIhC
remrofnE
egarevoc
erocs
Top Bottom Not 10% 10% in eRegulon
n = 8,248 n = 8,248 n = 507,249
qes-RRATS
CFgol
15 6
100
8
37
21
5 0
0 300
h j k l
i m n
104 SERPINF2 HepG2 (0–5)
PC3
IMR90
100 HCT116
HNF4A GM12878
102 FOXA2 TAB3 Panc1
MCF7
K562
CEBPB HNF4A (0–25)
10–1
FO
C
X
h
A
IP
2
104 SLC7A1 CE C B h P I B P
ChIP
SPP1 GK SPP1 PKD2 ABCG2
100
WDR81 87,980,000 88,110,000 SERPINF1 chr4 position (bp)
yrevocer
FT
SCENIC+
Pando
SCENIC
GRaNIE* FigR
CellOracle
TF ranking by logFC
0.4
0
SCENIC+ Pando SCENIC GRaNIE* Fig
C
R
ell
Oracle SCENIC+ GRaNIE* Pand
C
o
ell
Oracle FigR SCENIC SCENIC
C
+
ell
Oracle GRaNIE* FigR Pando SCENIC SCENIC+ SCEN
C
IC
ell
Oracle GRaNIE* FigR Pando
CUA
ARI: 1.00 ARI: 0.96 ARI: 0.95
ARI: 0.92 ARI: 0.85 ARI: 0.69
Article https://doi.org/10.1038/s41592-023-01938-4
PCA1
c d e f
g
For the mouse cortex, we performed 10x single-cell multiome and for types (Extended Data Fig. 9a), implying that cell-type identity can be
the human cortex we re-used a previously published multiome dataset60. decomposed into these 60 eRegulons. Eight out of 60 conserved TFs
We were able to identify matching cell types in both species, including have not been described before in the context of the cortex. These
layer-specific excitatory neurons, interneurons derived from the medial include Smad3/SMAD3 in the excitatory neurons of the upper cortical
and caudal ganglionic eminences (MGEs and CGEs, respectively) and layers, Pparg/PPARG and Bhlhe40/BHLHE40 in L4 excitatory neurons,
non-neuronal populations (microglia, astrocytes, endothelial cells, oli- Etv5/ETV5 and Nfat5/NFAT5 in L5/6 excitatory neurons, Thrb/THRB
godendrocytes and oligodendrocyte progenitor cells (OPCs); Fig. 5a,b). and Pbx1/PBX1 in L6 excitatory neurons and Meis1/MEIS1 in oligo-
SCENIC+ identified 125 and 142 high-quality eRegulons for mouse dendrocytes (Fig. 5c,d and Extended Data Fig. 9b–d). Projection of
and human, respectively, out of which 60 are found in both species SCENIC+ regulons onto spatial transcriptomics data further validated
(Fig. 5c,d). Notably, we observed a high correlation of the specific- layer-specific GRNs in the mammalian cortex (Extended Data Fig. 9e–j
ity scores of eRegulons for these orthologous TFs in matching cell and Supplementary Note 5).
Nature Methods | Volume 20 | September 2023 | 1355–1367 1361
2ACP
Melanocytic MM001
Mesenchymal
MM031 MM047
MM011 MM029
MM074 MM099
MM087
MM057 Intermediate
Train models
TF1 TF2 TF3 TF4 TF5
TF1 TF4
G1 G3 RF regression G2 Predict perturbation
TF’1 TF2 TF3 TF4 TF5 TF’1 TF4
G’1 G3
G’2
Embed perturbation
Original expression matrix Perturbed expression matrix
seneG
Cells DR1
snoitareti
n
2RD
0.6
0
–0.6 Iteration no.
CFgol
detciderP
2
FOSL1
NFE2L3
JUN FOSL2 MITF IRF4 TFAP2A
0 4 8 12
MM001
MM011
MM031
MM087
MM074
MM057 MM047
MM029
MM099
R U N S X O 3 X1 0 B M H IT L F H T E F 4 A 1 Z P N 2 F A 48 S 7 O X S 6 O X5 M XI E 1 T V5 NFIB NFI C IR M F E 1 F2 S C O X E 9 GR3 N S F M I X A D S 3 O X4 ZEB1
PC
1 shift
SOX10 knockdown simulation
PCA1
ZEB1 knockdown simulation
0.4
–0.4
2ACP
PCA1 2ACP
MM099
MM029
MM047
MM057
MM087
MM074
MM031
MM011
MM001
MM001
MM047 MM031 MM029 MM011 MM074 MM099 MM087
MM057
MM001
MM047 MM031
MM029 MM011
MM074 MM099
MM087
MM057
)+(2CIZ )+(1BEZ )+(4FCT )+(XIFN )+(CIFN )+(3L2EFN )+(7FLK )+(NUJ )+(3KLE )+(3DAMS )+(BYFN )+(BIFN )+(3AXOH )+(1FXOF )+(1AXOF )+(2STE )+(4FLE )+(RHA )+(286FNZ )+(34FNZ )+(3RGE )+(5XLD )+(6XOS )+(5XOS )+(01XOS )+(2F3UOP )+(5VTE )+(6FLK )+(SEMOE )+(784FNZ )+(483FNZ )+(3XNUR )+(A2PAFT )+(5LFCT )+(4XOS )+(2XRRP )+(1A4RN )+(CYM )+(FTIM )+(31FLK )+(XLH )+(14EHLHB
a b
Scaled RSS Scaled expression
0 1 0 1
MM001 MEL s r
MES s r
MM011 M M E E S L s s r r
MM031 MEL s r
MES s r MM057 M M E E S L s s r r MM074 M M E E S L s s r r MM087 M M E E S L s s r r
Real (r) –2 0 2 Simulated (s) logFC
Fig. 4 | SCENIC+ analysis using separate scATAC-seq and scRNA-seq data on a on cell states. d, Predicted logFC of mesenchymal (red shades) and melanocytic
mix of human melanoma lines. a, PCA of 936 pseudo-multiome cells based on (yellow shades) marker genes over several iterations of SOX10 knockdown
target gene and target region enrichment scores. b, Heat map/dot-plot showing simulation. e, Simulated (s) and actual (r) distribution of logFCs of melanocytic
TF expression of the eRegulon on a color scale and cell-type specificity (RSS) of (n = 523) and mesenchymal (n = 722) marker genes after SOX10 knockdown
the eRegulon on a size scale. c, Illustration of how predictions from SCENIC+ can across several melanoma lines. Upper/lower hinge represents upper/lower
be used to simulate TF perturbations. Top: SCENIC+ is used as a feature selection quartile, whiskers extend from the hinge to the largest/smallest value no further
method and RF regression models are fitted for each gene using TF expressions than 1.5 × interquartile range from the hinge respectively. The median is used
as predictors for gene expression. Middle: the expression of TF(s) is altered in as the center. f, Simulated shift after SOX10 and ZEB1 knockdown represented
silico and the effect on gene expression is predicted using the regression models, using arrows. Arrows are shaded based on the distance traveled by each cell
which is repeated for several iterations to simulate indirect effects. Bottom: the after knockdown simulation. g, Heat map representing the shift along the first
original and simulated gene expression matrices are co-embedded in the same principal component of each melanoma line after simulated knockdown of
dimensionality reduction to visualize the predicted effect of the perturbation several TFs.
Article https://doi.org/10.1038/s41592-023-01938-4
UMAP1
Nature Methods | Volume 20 | September 2023 | 1355–1367 1362
2PAMU
0.5
0
RSS
<0.80
0.85
0.90
0.95
1.00
Expression
2
0
−2
eneG
devresnoc
0.15
0
noigeR devresnoc
CGE (Lamp5)
CGE (Sncg)
CGE (Vip)
MGE (Pvalb)
MGE (Sst)
L2/3 IT
L4 IT
L5 IT L5 PT
L6 IT L6CT
L6b
AST
OPC
OL
MGL
CGE (LAMP5) CGE (SNCG)
CGE (VIP)
MGE (PVALB)
MGE (SST) L2/3 IT
L4 IT
L5 IT
L5 PT
L6 IT
L6CT L6b
AST OPC
OL
MGL
)+(6XLD )+(1XLD )+(GRRSE )+(XRA )+(6XHL )+(1BTAS )+(3DAMS )+(3XFR )+(GRAPP )+(2LSOF )+(2XUC )+(C2FEM )+(LTNRA )+(2SIEM )+(FLH )+(1XUC )+(3RGE )+(AROR )+(BROR )+(1VTE )+(1C3RN )+(A11LCB )+(1RBT )+(1XBP )+(AIFN )+(1L7FCT )+(9XOS )+(3SILG )+(2L7FCT )+(6XAP )+(1XRRP )+(2GILO )+(4XOS )+(6XOS )+(2XOS )+(5BERC )+(8XOS )+(1SIEM )+(01XOS )+(1XNUR )+(6VTE )+(1FZKI )+(8FRI )+(4FLE )+(1IPS )+(1ILF
a c
b
CGE (LAMP5) L6b L6CT MGE (PVALB)
CGE (SNCG)
MGE (SST)
NP
L5 IT
L6 IT
CGE (VIP)
L4 IT-like L5 PT MGL
ENDO
OL
L2/3 IT
AST
Human
d e f
Dlx1(+) DLX1(+)
Lhx6(+) LHX6(+) (0–10)
OPC
Rfx3(+) RFX3(+) Rb S m o D x s A p 5 3 m p6 G ot l l is D 1 3 lgK T R ac m b pn f 1 c S c o c A 1 u Nx 3 l f1k f a 2 a p in 1 4 Py S g S o o h x 1 1 3 A G 3 d t r p 1 ik 9 1 3 b E C 2 r K a b l c h b n l 4 A 5 a2 d Ad a s m 2tn t A s 2 9 lkEtv F G 6 r f m ra d 1 4b D M o a c r k c 1 ksPr B tg cas C R1 u in e S 2 d rg c1 a C P p h d 1 s e t 1 3 cSlit E C 2 p o n b A 2 l b l D L 1 t s i b m c 2 a s m 2 P M dl a im m 5 l2 H P G t a r l p a ld r 1 3 C 7 C l n s 1 p n3 g4 Olig2 Megf11 Pdgfra Lhfpl3 L T T O i F F n P B B k C S S s (0–10)
R Tb o r r 1 b ( ( + + ) ) R TB O R R 1 B (+ (+ ) ) A N N F T b t c N m a n c h c 4 a a e s T c v H 1 m d c 2 1 i Tf 2 p 1 4m 3 1r 2 e c m108 Sox6 Z O c l c G ig h p c 1 H r I2t 1 4g F 7 r i b m S Tp 8 S g m d h fa 5 o 1 3 D G cb P N e 1p l t i n f p 2 4 i n a rz d 1 X 2 y a lt1 Ch S s tk t1 3 P 1 l 2 p a p4 G L e i n n e k s s 8,700,000 mm Ch 1 d 0 7 chr4 position (kb) 8,950,000
Rftn2Tnr
Tns3 C1ql1 (0–10)
H P i t f p 3a Zrmeb S 2 lc6a1 Chd7Gpsm2 Cacng4 OPC
Nck M ap m 5 d2 Sas N h p 1 as3 Wscd1 TFBS
S M o e x is 9 1 ( ( + + ) ) S M O EI X S 9 1 ( ( + + ) ) Li P m lx a nS 1 bir1t2 Prr5l Sox8 Prrx1 Links
Fli1(+) FLI1(+) HepacaCmdh20 Zbtb20 Kank1 Nxn OPC (0–10)
Notch1
Sox2 Lrp4 TFBS
Plscr4 Links
Bmp7
PrimaP1rox S 1 em A a6 d a ar M b2 etap1d S P e l l e e k n h o g pD 1 oc H kP1 ip 0le k2 kh E b rb 1 bG3lul Nkd1 Cd82 Fads2 Plpp3 Gene 1 s 35,450,000 mm10 chr H 5 i p p 1 osition (kb) 135,550,000
Standardized eGRN AUC Atp1 P 0 le b khg3Clic4
0 1 0 1 0 1 Ddr1Itgb4 0 1
esuoM namuH
esuoM
namuH
Mouse
Human
UMAP1
SCENIC+ rho
Sox8 Sox6 Sox2 Sox8 Sox6 Sox2
Prrx1 Olig2 Prrx1 Olig2
2PAMU
L6b NP
L6CT L2/3 IT
L4 IT
PER L6 IT
OL L5 IT
ABC L6 IT Car3
VEC L5 PT CGE (Vip)
CGE (Sncg)
VLMC PVM
CGE (Lamp5)
MGL MGE (Sst)
MGE (Pvalb) OPC
AST Mouse
Fig. 5 | SCENIC+ reveals regulatory lexicon conservation across mammalian are shown in blue and regions only found in the mouse analysis are shown in gray.
brains. a, Uniform Manifold Approximation and Projection (UMAP) Genes are shown as a circular shape and their color and size represent the logFC
dimensionality reduction of 19,485 mouse cortex cells based on target gene of the gene expression in OPCs compared to the rest of the cells. TF–region links
and region enrichment scores. b, UMAP dimensionality reduction of 84,159 are colored by TF and region–gene links are colored by region–gene correlation
human motor cortex cells based on target gene and region enrichment scores. coefficients. f, OPC coverage, TFBSs and region–gene links in two loci, Chd7 and
c, Heat map/dot-plot showing TF expression of the eRegulon on a color scale Hip1. Data are shown in the mouse genome (mm10) and human data have been
and cell-type specificity (RSS) of the eRegulon on a size scale. The bar-plot above lifted over (mm10). Peaks found in both human and mouse are highlighted in
indicates the percentage of the regulon that is conserved in the other species, blue, whereas peaks only accessible in one of the species are highlighted in gray.
for predicted target regions (top) and target genes (bottom). d, Mouse and ABC/VLMC, vascular leptomeningeal cell; AST, astrocyte; CT, cortico-thalamic;
human UMAPs colored by enrichment scores for selected regulons using RGB ENDO, endothelial cell; IT, intratelencephalic; MGL, microglia; NP, near-
encoding. e, Mouse-based OPC eGRNs with conserved TFs. Regions are shown as projecting; PER, pericyte; PVM, perivascular macrophage; PT, pyramidal-tract;
a diamond shape and their size represents the logFC of the region accessibility OL, oligodendrocyte; VEC, vascular endothelial cell.
in OPCs compared to the rest of the cells. Regions conserved in the human brain
Article https://doi.org/10.1038/s41592-023-01938-4
Pseudotime ordering
DR1
eRegulons identified in only one of the two species can be either This indicates that these regulators are likely conserved, but were
species-specific TFs or false negatives in one of the two analyses. missed in the human analysis. For example, while Pou3f1/POU3F1
To distinguish one from the other, we assessed the correlation and Fezf2/FEZF2, previously described regulators of L5 PT and L5/6
coefficient of cell-type-specificity scores of each mouse eRegulon neurons, respectively59, were only found in the mouse analysis, the
to its human orthologous matching eRegulon by converting the human-based mouse eRegulons are enriched in the corresponding
mouse predicted target genes to human orthologous genes. We cell types in the human dataset, matching the expression of these
found an additional 51 eRegulons with a correlation coefficient >0.6. TFs (Extended Data Fig. 9b).
Nature Methods | Volume 20 | September 2023 | 1355–1367 1363
2RD
Differentiation trajectory eGRN dynamics
0 Max
Pseudotime
Pseudotime
eulav
dezilamroN
Match to future cell
DR1
2RD
Differentiation trajectory eGRN dynamics
Pseudotime
eulav
dezilamroN
DR1
2RD
Olig2(+) Bcl6(+) Prrx1(+) Tcf7l2(+)
TF expression
Target regions accessibility
Target genes expression
Sox10(+) Zeb2(+) Meis1(+) Tcf12(+)
UMAP1
Arrow grid Differentiation force
Differentiation trajectory TF differentiation strength
TF1
TF2
Differentiation
force TF3
Max 0 TF4
2PAMU
PR HVMF
Antenna
MF A1
A2
A3
Arista
SMW
Precursors
Progenitors PRs & INT INT
Optix(+) ey(+) ato(+) sens(+)
gl(+) svp(+) onecut(+) lz(+)
UMAP1
2PAMU
scVelo MultiVelo
UMAP1
2PAMU
UMAP1
2PAMU
UMAP1
2PAMU
svp dynamics in PR branch
svp expression
svp targets expression
Path penalization
svp dynamics in INT branch
Pseudotime
elacs
dezilamroN
a b
c d e
Progenitors
&
Precursors
f g
Pseudotime
Fig. 6 | Identification of differentiation drivers from SCENIC+ eGRNs. MultiVelo velocity arrows (e). f, Representation of svp dynamics along the two
a, Computational approach to infer differentiation drivers from a SCENIC+ analysis. paths in eye disc differentiation. The gray horizontal line represents the TF
First, differentiating cells are ordered by pseudotime. Second, for each eRegulon, expression threshold for arrows to be drawn. For cells below this threshold, the
a standardized GAM is fitted along the pseudotime axis for its expression and its GRN velocity values are set to 0. The gray dashed line represents the penalization
target genes (or regions) enrichment scores and each cell in a certain quantile of curve, which is the GAM fitted curve drawn using the standardized data across
the GAM TF expression curve is mapped to its future cells in the same quantile all possible paths for the cells in that path. Those points where the penalization
in the GAM regulon enrichment curve. Finally, the differentiation force of a and the TF expression curve disagree are considered artifacts (the TF gene seems
cell and regulon is defined as the distance from the TF expression curve to its to be expressed even if there is low expression, due to the standardization of the
future cell in the regulon enrichment curve. b, Arrow grid representation along TF curve in that specific path). The red curve represents the GAM fitted curve
the differentiation of OPCs to mature oligodendrocytes in the mouse cortex using the standardized TF expression data (along the path) and the blue curve
(4,435 cells). c–e, UMAP dimensionality reduction of 3,104 pseudocells from represents the GAM fitted curve using the standardized gene enrichment scores
the fly eye based on target gene and region enrichment scores, with a schematic (along the path). g, Arrow grid representation along the eye disc differentiation.
representation of the fly eye-antennal disc (c), scVelo velocity arrows (d) and
Article https://doi.org/10.1038/s41592-023-01938-4
Next, we assessed the conservation of predicted target genes and For example, the expression of a TF may precede accessibility of its
regions across human and mouse. Out of the 102,746 regions found binding sites and chromatin accessibility in turn may precede target
within human eGRNs, 84,861 could be lifted over (82%), whereas only gene expression67 (Fig. 6a). Therefore, we have developed a procedure
69% of all accessible regions (697,721) could be lifted over. Out of these to quantify the putative differentiation force of a TF. In this approach,
84,861 conserved mouse regions, 61,973 were accessible in the mouse cells are ordered along a pseudotime axis and each cell is matched to
cortex. In addition, 312,591 (out of 379,749) region–gene links from the its future cell based on its current TF expression value and the cell with
human cortex could be lifted over, of which 283,900 corresponded the best-matching future target gene expression. The differentiation
to the same region–gene pair in the mouse cortex. On average, 28% force of a TF in each cell is then defined as the distance to its future cell,
and 6% of eRegulon target genes and regions, respectively, for each along the pseudotime axis. These forces can be plotted as arrows on a
orthologous TF were conserved between the two species (Fig. 6c). grid in any cell embedding (Fig. 6a).
We observed a strong correlation (0.68) of the fraction of conserved We first applied this approach to a linear differentiation trajec-
regions to the fraction of conserved genes per regulon. Thus, despite tory from OPCs to mature oligodendrocytes in the mouse brain. This
high conservation of TFs per cell type, the target genes (and even more revealed a set of TFs (Olig2, Bcl6 and Prrx1) that maintain OPC iden-
so the target regions) are less conserved. This has also been observed tity. On the other hand, Tcf7l2 and Sox10 had a delay between TF and
in previous studies. For example, Bakken et al. reported 25% and 5% target gene expression. This can be seen as arrows pointing toward
conservation of differentially expressed genes and DARs, respectively, newly forming oligodendrocytes (NFOLs). A final set of TFs (Zeb2,
across cell types in the human and marmoset cortex60. Stergachis et al. Meis1 and Tcf12) were identified as potential drivers of the matura-
performed DNase I footprinting across 25 mouse tissues, finding that tion from NFOLs to oligodendrocytes (Fig. 6b). Notably, Meis1 has
only around 20% of TF footprints are conserved in human, whereas been previously described to be involved in early neurogenesis and
95% of the TF code is shared61. Genomic relocation and turnover of hematopoiesis68 but not in oligodendrocyte maturation. In line with
TFBSs and enhancers may partly explain these observations; however, this, SCENIC+ also identified Meis1 as a conserved TF in human and
the sparsity of the single-cell datasets may also contribute to these mouse oligodendrocytes (Fig. 5c).
findings, as we are only capturing a fraction of the transcriptome and Next, we applied GRN velocity to a branched differentiation tra-
epigenome in each cell. Overall, we identify 4,798 and 8,318 conserved jectory from progenitor cells to photoreceptors or interommatidial
TF–region and TF–gene relationships, respectively (Supplementary cells in the developing fly retina. For this, we performed single-cell (sc)
Table 2). Given the sparsity of direct TF–enhancer and TF–target gene ATAC-seq on the eye field and integrated these data with scRNA-seq and
relationships in the literature, this is the largest set of conserved TF– scATAC-seq data on the developing eye (Fig. 6c)14. SCENIC+ identified
target interactions in the mammalian cortex. 105 eRegulons that are active in the eye part. Of note, SCENIC+ found
We further studied eGRN conservation in OPCs. While mature a repressor eRegulon for Cut (Ct) that is expressed in the antennae. It
oligodendrocytes are driven by SOX10 (see further below), OPCs show has been already shown that this acts as a repressor of the eye field69
higher activity of Sox2/SOX2, Sox6/SOX6 and Sox8/SOX8, alongside and here we predict that it directly represses 13 other TFs, including
Olig2/OLIG2 and Prrx1/PRRX1 (Fig. 5e). These TFs have indeed been Spineless (ss), Eyeless (ey), Twin of eyeless (toy) and Optix.
described previously in the literature as key drivers of OPC prolifera- As inferred by scVelo and MultiVelo, cells follow a differentiation
tion, migration, quiescence and differentiation62,63. Out of 636 regions trajectory from progenitors to the morphogenetic furrow (MF) and to
predicted to be targeted by at least one of these five TFs in mouse and the second mitotic wave (SMW), which forms a branch point to either
linked to at least one conserved target gene in both human and mouse, photoreceptor cells (PRs) or interommatidial cells (INTs) (Fig. 6d,e).
102 TFBS are conserved across the two species (16%). GRN velocity revealed strong differentiation arrows for Optix,Toy and
To further examine the relationship between target region con- Ey in progenitors, followed by Hairy (hry), Anterior open (aop), Rotund
servation and TFBS presence, we zoomed in on two example loci, Chd7 (rn) and Atonal (ato) in the MF. BarH1 (B-H1), BarH2 (B-H2), Sine oculis
and Hip1. We observed three distinct scenarios related to enhancer (so) and Glass (gl) were found to trigger the differentiation from MF
turnover: (1) a chromatin-accessibility peak and TFBSs are present in toward both PRs and INTs. Lozenge (lz) was found to be the key driver
one of the species, whereas in the other species there is no accessibility of INT identity and Tramtrack (ttk) as the key driver for their matura-
and no TFBSs (two cases in the Chd7 loci); (2) a chromatin-accessibility tion. In the photoreceptor branch, Senseless (sens) and Rough (ro)
peak and the same TFBSs are found in both species (two cases in the were identified as key regulators of differentiation. These are followed
Hip1 loci); and (3) a chromatin-accessibility peak and at least one TFBS first by Asense (ase), Lola, Seven up (svp) and Scratch (scrt) and later by
are shared across the two species, but additional non-shared TFBSs Shaven (sv) and Onecut (onecut) in mature photoreceptors (Fig. 6f,g).
can be found. For the latter case, we also observed cross-species vari- Notably, these findings are consistent with a previously described dif-
ations in the peak shape and size for peaks where different/additional ferentiation cascade in the eye disc14.
TFBSs are found (for example, more accessibility in the species where
additional TFBSs are found or a different peak shape when different Discussion
TFBSs are found), whereas peaks with the same TFBSs have a similar CREs are key to control differential gene expression across cell types,
shape (Fig. 5e). during development, in evolution and in disease1–5,70. Yet, only few
Altogether, comparative analysis with SCENIC+ reveals TF lexicon GRNs have been characterized to the level of detail where they include
conservation across mammalian brains, but divergence of their target CREs as nodes2,14. We lack such GRNs mainly due to challenges associ-
genes and target regions. ated with high-throughput experimental identification and validation
of TFBSs. For this reason, we need computational methods that can
Predicting TFs driving differentiation using GRN identify TFBSs on a genome-wide scale and at the cell-type-specific
velocity level. Single-cell chromatin accessibility and gene expression pro-
Single-cell omics data are often used to sample cells during a dynamic filing combined with sequence analysis is ideally suited for this and
biological process such as differentiation. Models, such as RNA veloc- led to the concept of eGRNs2,14,31–34. In this work we present SCENIC+,
ity64,65 and MultiVelo66, which try to reconstruct the most likely trajec- a computational method to efficiently infer eGRNs.
tory from such data are available; however, these approaches do not By applying SCENIC+ to single-cell multiome data across a range
include gene regulatory information to model dynamics. of biological systems and across species we showed that SCENIC+
We reasoned that regulatory relationships derived by SCENIC+ can accurately identify key TF combinations for each cell type. More
could provide additional intrinsic cues to predict cell-state dynamics. notably, it can confidently link these TFs to CREs and target genes.
Nature Methods | Volume 20 | September 2023 | 1355–1367 1364
Article https://doi.org/10.1038/s41592-023-01938-4
By comparing SCENIC+ to other methods, we could identify several 4. Erwin, D. H. The origin of animal body plans: a view from fossil
elements that improve the quality of eGRN inference. First, the use of evidence and the regulatory genome. Development 147,
topic modeling improves unsupervised prioritization of informative dev182899 (2020).
regions. Second, the use of multiple motifs per TF and the use of a large 5. Rickels, R. & Shilatifard, A. Enhancer logic and mechanics in
motif collection improve the recall to identify important TFs. Finally, the development and disease. Trends Cell Biol. 28, 608–630 (2018).
use of motif enrichment analysis instead of motif scanning that is used in 6. Bartosovic, M., Kabbe, M. & Castelo-Branco, G. Single-cell
alternative methods reduces the false-positive rate of TFBS predictions. CUT&Tag profiles histone modifications and transcription factors
One biological application where eGRN inference plays a pivotal in complex tissues. Nat. Biotechnol. 39, 825–835 (2021).
role is in evolutionary genomics. For example, within the mammalian 7. Bartosovic, M. & Castelo-Branco, G. Multimodal chromatin
cortex, the majority of cell types were found to be conserved60,71–73; profiling using nanobody-based single-cell CUT&Tag. Nat.
however, hundreds of genes are differentially expressed between Biotechnol. https://doi.org/10.1038/s41587-022-01535-4 (2022).
orthologous cell types60. Comparison of eGRNs inferred across species 8. Stuart, T. et al. Nanobody-tethered transposition enables
can provide insights into these discrepancies. By mapping human and multifactorial chromatin profiling at single-cell resolution. Nat.
mouse eGRNs in the cortex, we found that cell-type-specific TF combi- Biotechnol. https://doi.org/10.1038/s41587-022-01588-5 (2022).
nations are strongly conserved; however, TFBSs and enhancers show 9. van Steensel, B., Delrow, J. & Henikoff, S. Chromatin profiling
high turnover in line with earlier experimental findings61,74. This alludes using targeted DNA adenine methyltransferase. Nat. Genet. 27,
to the fact that the unique combination of TFs and their interactions 304–308 (2001).
(the core regulatory complex75) define a cell type. 10. Tang, J. L. Y. et al. NanoDam identifies Homeobrain (ARX) and
Another biological application is to study the regulatory underpin- Scarecrow (NKX2.1) as conserved temporal factors in the
nings of dynamic cell-state changes. For this, we developed two down- Drosophila central brain and visual system. Dev. Cell 57, 1193–
stream methods that exploit the inferred eGRN. One method predicts 1207.e7 (2022).
the effect of a TF perturbation on the transcriptome, which can be used 11. Aibar, S. et al. SCENIC: single-cell regulatory network inference
to screen for the most important TFs needed to maintain a certain cell and clustering. Nat. Methods 14, 1083–1086 (2017).
state. Another method, called GRN velocity, models the effect of each 12. Van de Sande, B. et al. A scalable SCENIC workflow for single-cell
TF in a differentiation trajectory. This technique is complementary to gene regulatory network analysis. Nat. Protoc. 15, 2247–2276
other methods that infer directionality in differentiation trajectories (2020).
(such as scVelo65 and MultiVelo66). 13. Fulco, C. P. et al. Activity-by-contact model of enhancer–promoter
There are limitations with this study and eGRN inference methods regulation from thousands of CRISPR perturbations. Nat. Genet.
in general that may be overcome with future technological advances. 51, 1664–1669 (2019).
Benchmarking these methods is challenging due to the lack of stand- 14. Bravo González‐Blas, C. et al. Identification of genomic enhancers
ardized ground-truth data. For example, to evaluate the predicted through spatial integration of single‐cell transcriptomics and
target genes we relied on transcriptome changes after the perturbation epigenomics. Mol. Syst. Biol. 16, e9438 (2020).
of a TF, which also causes indirect downstream effects and requires 15. Argelaguet, R. et al. Decoding gene regulation in the mouse
one experiment per targeted TF. Another challenge is the validation embryo using single-cell multi-omics. Preprint at bioRxiv
of enhancer–gene relationships, for which we used Hi-C data. Hi-C has https://doi.org/10.1101/2022.06.15.496239 (2022).
a limited resolution and the relationship between physical enhancer– 16. Bravo González-Blas, C. et al. cisTopic: cis-regulatory topic
promoter distance and gene expression is still unclear76–78 and warrants modeling on single-cell ATAC-seq data. Nat. Methods 16,
further research79. Furthermore, even though we show that eGRNs can 397–400 (2019).
be used to model transcriptome changes upon perturbation, their 17. Minnoye, L. et al. Cross-species analysis of enhancer logic using
power is still limited. Further improvements may require more sophis- deep learning. Genome Res. 30, 1815–1834 (2020).
ticated models, for example using deep neural networks42, to yield 18. Mauduit, D. et al. Analysis of long and short enhancers in
both quantitative and biologically explainable predictions80. Finally, melanoma cell states. eLife 10, e71735 (2021).
eGRN inference is still biased toward activation and is less accurate in 19. Janky, R. et al. iRegulon: from a gene list to a gene regulatory
identifying repressive interactions (Extended Data Fig. 10 and Sup- network using large motif and track collections. PLoS Comput.
plementary Note 6). Biol. 10, e1003731 (2014).
In conclusion, in this study we present SCENIC+, a tool to infer 20. Imrichová, H., Hulselmans, G., Kalender Atak, Z., Potier, D.
eGRNs from single-cell multiomics data. SCENIC+ and the code for & Aerts, S. i-cisTarget 2015 update: generalized cis-regulatory
downstream analyses is available at https://github.com/aertslab/ enrichment analysis in human, mouse and fly. Nucleic Acids Res.
scenicplus. 43, W57–W64 (2015).
21. Verfaillie, A., Imrichova, H., Janky, R. & Aerts, S. iRegulon and i‐
Online content cisTarget: reconstructing regulatory networks using motif and
Any methods, additional references, Nature Portfolio reporting sum- track enrichment. Curr. Protoc. Bioinforma. 52, 2.16.1–2.16.39 (2015).
maries, source data, extended data, supplementary information, 22. Heinz, S. et al. Simple combinations of lineage-determining
acknowledgements, peer review information; details of author contri- transcription factors prime cis-regulatory elements required for
butions and competing interests; and statements of data and code avail- macrophage and B cell identities. Mol. Cell 38, 576–589 (2010).
ability are available at https://doi.org/10.1038/s41592-023-01938-4. 23. Moerman, T. et al. GRNBoost2 and Arboreto: efficient and scalable
inference of gene regulatory networks. Bioinformatics 35,
References 2159–2161 (2019).
1. Davidson, E. H. et al. A genomic regulatory network for 24. Rothenberg, E. V. Transcriptional control of early T and B cell
development. Science 295, 1669–1678 (2002). developmental choices. Annu. Rev. Immunol. 32, 283–321 (2014).
2. Janssens, J. et al. Decoding gene regulation in the fly brain. Nature 25. Hodson, D. J. et al. Regulation of normal B-cell differentiation and
601, 630–636 (2022). malignant B-cell survival by OCT2. Proc. Natl Acad. Sci. USA 113,
3. Long, H. K., Prescott, S. L. & Wysocka, J. Ever-changing E2039–E2046 (2016).
landscapes: transcriptional enhancers in development and 26. Wang, D. & Malarkannan, S. Transcriptional regulation of natural
evolution. Cell 167, 1170–1187 (2016). killer cell development and functions. Cancers 12, 1591 (2020).
Nature Methods | Volume 20 | September 2023 | 1355–1367 1365
Article https://doi.org/10.1038/s41592-023-01938-4
27. Chopin, M., Allan, R. S. & Belz, G. T. Transcriptional regulation of 51. Caramel, J. et al. A switch in the expression of embryonic
dendritic cell diversity. Front. Immunol. 3, 26 (2012). EMT-inducers drives the development of malignant melanoma.
28. Pundhir, S. et al. Enhancer and transcription factor dynamics Cancer Cell 24, 466–480 (2013).
during myeloid differentiation reveal an early differentiation block 52. Hoek, K. S. & Goding, C. R. Cancer stem cells versus
in cebpa null progenitors. Cell Rep. 23, 2744–2757 (2018). phenotype-switching in melanoma: phenotype-switching in
29. The ENCODE Project Consortium. An integrated encyclopedia of melanoma. Pigment Cell Melanoma Res. 23, 746–759 (2010).
DNA elements in the human genome. Nature 489, 57–74 (2012). 53. Yang, H., Fu, J., Yao, L., Hou, A. & Xue, X. Runx3 is a key modulator
30. Luo, Y. et al. New developments on the Encyclopedia of DNA during the epithelial-mesenchymal transition of alveolar type II cells
Elements (ENCODE) data portal. Nucleic Acids Res. 48, D882– in animal models of BPD. Int. J. Mol. Med. 40, 1466–1476 (2017).
D889 (2020). 54. Dilshat, R. et al. MITF reprograms the extracellular matrix and
31. Kamimoto, K. et al. Dissecting cell identity via network inference focal adhesion in melanoma. eLife 10, e63093 (2021).
and in silico gene perturbation. Nature 614, 742–751 (2023). 55. Zhang, P., Sun, Y. & Ma, L. ZEB1: at the crossroads of
32. Fleck, J. S. et al. Inferring and perturbing cell fate regulomes in epithelial-mesenchymal transition, metastasis and therapy
human brain organoids. Nature https://doi.org/10.1038/s41586- resistance. Cell Cycle 14, 481–487 (2015).
022-05279-8 (2022). 56. Tiwari, N. et al. Sox4 is a master regulator of
33. Kartha, V. K. et al. Functional inference of gene regulation using epithelial-mesenchymal transition by controlling Ezh2 expression
single-cell multi-omics. Cell Genom. 2, 100166 (2022). and epigenetic reprogramming. Cancer Cell 23, 768–783 (2013).
34. Kamal, A. et al. GRaNIE and GRaNPA: inference and evaluation 57. Meng, F., Li, J., Yang, X., Yuan, X. & Tang, X. Role of Smad3
of enhancer‐mediated gene regulatory networks. Mol. Syst. Biol. signaling in the epithelial-mesenchymal transition of the
https://doi.org/10.15252/msb.202311627 (2023). lens epithelium following injury. Int. J. Mol. Med. https://doi.
35. Puig, R. R., Boddie, P., Khan, A., Castro-Mondragon, J. A. & org/10.3892/ijmm.2018.3662 (2018).
Mathelier, A. UniBind: maps of high-confidence direct TF–DNA 58. Tasic, B. et al. Shared and distinct transcriptomic cell types across
interactions across nine species. BMC Genom. 22, 482 (2021). neocortical areas. Nature 563, 72–78 (2018).
36. Gheorghe, M. et al. A map of direct TF–DNA interactions in the 59. BRAIN Initiative Cell Census Network (BICCN). A multimodal cell
human genome. Nucleic Acids Res. 47, e21 (2019). census and atlas of the mammalian primary motor cortex. Nature
37. Han, G. C. et al. Genome-wide organization of GATA1 and TAL1 598, 86–102 (2021).
determined at high resolution. Mol. Cell. Biol. 36, 157–172 (2015). 60. Bakken, T. E. et al. Comparative cellular analysis of motor cortex in
38. Lemma, R. B. et al. Chromatin occupancy and target genes of human, marmoset and mouse. Nature 598, 111–119 (2021).
the haematopoietic master transcription factor MYB. Sci. Rep. 11, 61. Stergachis, A. B. et al. Conservation of trans-acting circuitry during
9008 (2021). mammalian regulatory evolution. Nature 515, 365–370 (2014).
39. Inoue, A. et al. Elucidation of the role of LMO2 in human erythroid 62. Wittstatt, J., Reiprich, S. & Küspert, M. Crazy little thing called
cells. Exp. Hematol. 41, 1062–1076 (2013). sox—new insights in oligodendroglial sox protein function. Int. J.
40. Smith, R. P. et al. Massively parallel decoding of mammalian Mol. Sci. 20, 2713 (2019).
regulatory sequences supports a flexible organizational model. 63. Wang, J. et al. Paired related homeobox protein 1 regulates
Nat. Genet. 45, 1021–1028 (2013). quiescence in human oligodendrocyte progenitors. Cell Rep.
41. Holding, A. N. et al. VULCAN integrates ChIP-seq with https://doi.org/10.1016/j.celrep.2018.11.068 (2018).
patient-derived co-expression networks to identify GRHL2 as a 64. La Manno, G. et al. RNA velocity of single cells. Nature 560,
key co-regulator of ERa at enhancers in breast cancer. Genome 494–498 (2018).
Biol. 20, 91 (2019). 65. Bergen, V., Lange, M., Peidli, S., Wolf, F. A. & Theis, F. J.
42. Avsec, Ž. et al. Effective gene expression prediction from Generalizing RNA velocity to transient cell states through
sequence by integrating long-range interactions. Nat. Methods dynamical modeling. Nat. Biotechnol. 38, 1408–1414 (2020).
18, 1196–1203 (2021). 66. Li, C., Virgilio, M. C., Collins, K. L. & Welch, J. D. Multi-omic
43. The ENCODE Project Consortium et al. Expanded encyclopaedias single-cell velocity models epigenome–transcriptome
of DNA elements in the human and mouse genomes. Nature 583, interactions and improves cell fate prediction. Nat. Biotechnol.
699–710 (2020). https://doi.org/10.1038/s41587-022-01476-y (2022).
44. Granja, J. M. et al. ArchR is a scalable software package for 67. Ma, S. et al. Chromatin potential identified by shared single-cell
integrative single-cell chromatin accessibility analysis. Nat. profiling of RNA and chromatin. Cell 183, 1103–1116 (2020).
Genet. 53, 403–411 (2021). 68. Isogai, E., Okumura, K., Saito, M., Tokunaga, Y. & Wakabayashi,
45. Stuart, T., Srivastava, A., Madad, S., Lareau, C. A. & Satija, R. Y. Meis1 plays roles in cortical development through regulation
Single-cell chromatin state analysis with Signac. Nat. Methods 18, of cellular proliferative capacity in the embryonic cerebrum.
15 (2021). Biomed. Res. 43, 91–97 (2022).
46. Aerts, S. et al. Gene prioritization through genomic data fusion. 69. Wang, C.-W. & Sun, Y. H. Segregation of eye and antenna fates
Nat. Biotechnol. 24, 537–544 (2006). maintained by mutual antagonism in Drosophila. Development
47. Hoek, K. S. et al. Metastatic potential of melanomas defined by 139, 3413–3421 (2012).
specific gene expression profiles with no BRAF signature. Pigment 70. Zaugg, J. B. et al. Current challenges in understanding the role of
Cell Res. 19, 290–302 (2006). enhancers in disease. Nat. Struct. Mol. Biol. 29, 1148–1158 (2022).
48. Wouters, J. et al. Robust gene expression programs underlie 71. Tarashansky, A. J. et al. Mapping single-cell atlases throughout
recurrent cell states and phenotype switching in melanoma. Nat. Metazoa unravels cell type evolution. eLife 10, e66747 (2021).
Cell Biol. 22, 986–998 (2020). 72. Bakken, T. E. et al. Single-cell and single-nucleus RNA-seq
49. Pratapa, A., Jalihal, A. P., Law, J. N., Bharadwaj, A. & Murali, T. M. uncovers shared and distinct axes of variation in dorsal LGN
Benchmarking algorithms for gene regulatory network inference neurons in mice, non-human primates, and humans. eLife 10,
from single-cell transcriptomic data. Nat. Methods 17, 147–154 (2020). e64875 (2021).
50. Verfaillie, A. et al. Decoding the regulatory landscape of 73. Sebé-Pedrós, A. et al. Cnidarian cell type diversity and regulation
melanoma reveals TEADS as regulators of the invasive cell state. revealed by whole-organism single-cell RNA-seq. Cell 173,
Nat. Commun. 6, 6683 (2015). 1520–1534 (2018).
Nature Methods | Volume 20 | September 2023 | 1355–1367 1366
Article https://doi.org/10.1038/s41592-023-01938-4
74. Schmidt, D. et al. Five-vertebrate ChIP-seq reveals the Publisher’s note Springer Nature remains neutral with regard
evolutionary dynamics of transcription factor binding. Science to jurisdictional claims in published maps and institutional
328, 1036–1040 (2010). affiliations.
75. Arendt, D. et al. The origin and evolution of cell types. Nat. Rev.
Genet. 17, 744–757 (2016). Open Access This article is licensed under a Creative Commons
76. Alexander, J. M. et al. Live-cell imaging reveals Attribution 4.0 International License, which permits use, sharing,
enhancer-dependent Sox2 transcription in the absence of adaptation, distribution and reproduction in any medium or format,
enhancer proximity. eLife 8, e41769 (2019). as long as you give appropriate credit to the original author(s) and the
77. Xiao, J. Y., Hafner, A. & Boettiger, A. N. How subtle changes in source, provide a link to the Creative Commons license, and indicate
3D structure can create large changes in transcription. eLife 10, if changes were made. The images or other third party material in this
e64320 (2021). article are included in the article’s Creative Commons license, unless
78. Zuin, J. et al. Nonlinear control of transcription through enhancer– indicated otherwise in a credit line to the material. If material is not
promoter interactions. Nature 604, 571–577 (2022). included in the article’s Creative Commons license and your intended
79. Hafner, A. & Boettiger, A. The spatial organization of use is not permitted by statutory regulation or exceeds the permitted
transcriptional control. Nat. Rev. Genet. 24, 53–68 (2023). use, you will need to obtain permission directly from the copyright
80. Novakovsky, G., Dexter, N., Libbrecht, M. W., Wasserman, W. W. holder. To view a copy of this license, visit http://creativecommons.
& Mostafavi, S. Obtaining genetics insights from deep learning org/licenses/by/4.0/.
via explainable artificial intelligence. Nat. Rev. Genet. 24, 125–137
(2023). © The Author(s) 2023
Nature Methods | Volume 20 | September 2023 | 1355–1367 1367
Article https://doi.org/10.1038/s41592-023-01938-4
Methods HMMs to score clusters of motifs given a set of DNA sequences. Each
SCENIC+ workflow motif within a cluster is used as a separate hidden state in the model.
The SCENIC+ workflow consists of three main analysis steps: (1) unsu- Cluster-Buster was run separately for each (cluster of) motif(s) on the
pervised identification of enhancers with shared accessibility patterns DNA sequence of all consensus peaks and the maximum cis-regulatory
from scATAC-seq data; (2) prediction of TFBSs via motif enrichment module score per region was used as the score for each region.
analysis; and (3) prediction of eGRNs combining TF expression, TFBSs, cisTarget algorithm. For the cisTarget algorithm19–21, for each
region accessibility and gene expression. These steps are performed (cluster of) motif(s) a recovery curve approach was used using a set
using three Python modules: pycisTopic, pycisTarget and SCENIC+. of regions, for which to calculate motif enrichment and the ranking
Detailed explanations are described in Supplementary Note 1. Links database containing ranked (cluster of) motif(s) scores in descending
to the tools, SCENIC+ code and tutorials are available at scenicplus. order for the (cluster of) motif(s) of interest. The recovery curve was
readthedocs.io. defined as the cumulative number of regions within the region set
found at each position of the ranking. Enrichment was calculated as a
pycisTopic. Consensus peak calling. Pseudobulk fragment bed files per normalized AUC at the top 0.5% ranking (NES).
cell type were generated using the fragments file and cell-type anno-
tations provided by the user. Peaks were called using MACS2 (ref. 81) AUC−mean(AUC)
NES=
with parameters –format BEDPE –keep-dup all–shift 73 –ext_size 146. s.d.(AUC)
An iterative approach described by Corces et al.82 was used to obtain where
a consensus peak set. Briefly, each peak’s summit was extended with a
‘peak_half_width’ (default 250 bp) in each direction and overlapping mean(AUC)istheaverageAUCvalueacrossallmotifs
and less-significant peaks were filtered out. The original peak was kept
if there was only a single peak. The original peak with the highest score s.d.(AUC)isthestandarddeviationofAUCvaluesacrossallmotifs
was kept if there were two or more overlapping peaks. This process was
repeated until there were no more overlapping peaks. The process of By default, motifs that obtain an NES >3.0 are kept. To obtain
consensus peak generation was repeated twice: first for each cell type the target regions for each motif (motif-based cistrome) the regions
separately and, second, after peak score normalization within the cell at the top of the ranking (leading edge) are retained. The top of the
type, using the union of peaks across cell types. ranking is defined by an automated thresholding method that retains
Quality control. The sample-level statistics that we used to assess regions with a ranking below the rank at max, which is defined by the
the overall quality of the sample were: following formula:
• Barcode rank plot RankAtMax=max(rccmotif−[μ(rccallmotifs)+2×s.d.(rccallmotifs)])
• Insertion size
• Sample transcription start site (TSS) enrichment where
• Fraction of reads in peaks (FRiP) distribution
• Duplication rate rccmotifistherecoverycurveofthemotifofinterest.
The barcode-level statistics that we used to differentiate good μ(rccallmotifs)istheaveragerecoverycurveoverallmotifs.
quality cells versus the rest were:
• Total number of unique fragments per cell barcode
s.d.(rccallmotifs)isthestandarddeviationoftherecoverycurve
• TSS enrichment per cell barcode overallmotifs.
• FRiP per cell barcode
DEM algorithm. For each (cluster of) motif(s) a Wilcoxon rank-sum
Fragment count matrices were generated from the fragments test was performed between a foreground and a background set of
files by counting the number of fragments that overlap with consensus regions using the score distributions for the (cluster of) motif(s).
peaks per high-quality cell barcodes. Motifs with an adjusted P value < 0.05 (Bonferroni) and logFC > 0.5
Topic modeling was performed either using the serial Latent were kept. Regions containing the motif (motif-based cistrome) were
Dirichlet allocation (LDA) algorithm with a collapsed Gibbs sampler83 obtained by taking regions with a cis-regulatory module score >3 for
or using MALLET84 using the same default parameters as in cisTopic16. each enriched motif.
The model with the optimal number of topics was selected as the
model based on the topic selection metrics, namely coherence, SCENIC+. Generation of pseudo-multiome data. In cases of non-
log-likelihood and the metrics described in refs. 85 and 86 (Supple- multiome data, pseudo-multiome data were generated by sampling a
mentary Note 1). predefined number of cells from each data modality within the same
Region–topic probabilities were binarized either using the Otsu cell-type annotation label and averaging the raw gene expression and
method or by taking the top-n regions per topic. imputed chromatin-accessibility data across these cells to create a
Dropouts in scATAC-seq data were imputed by matrix multiplica- multiome meta-cell containing data of both modalities.
tion of the region–topic and cell–topic matrices. Calculating TF-to-gene and region-to-gene scores. The Arboreto
DARs were calculated using a Wilcoxon rank-sum test on the Python package (v.0.1.6) was used to calculate importance scores.
imputed probability matrix and selecting regions with a logFC > 0.5 TF-to-gene importance scores were calculated using gradient-boosting
and Benjamini–Hochberg adjusted P values < 0.05. machine regression by predicting raw TF expression from raw gene
expression counts and using the importance score of each feature
pycisTarget. Generation of cisTarget database. For the generation (gene) as the TF-to-gene importance score. Pearson correlation was
of the cisTarget database, a matrix with regions as rows (clusters of) used to separate positive (>0.03) from negative (<−0.03) interac-
motifs as columns and either raw scores (DEM) or ranking of these tions. The importance score of a TF for itself was set to the maximum
scores (cisTarget) was generated by scoring the DNA sequence of importance score across all genes added with an arbitrary small value
consensus peaks using Cluster-Buster87. Briefly, Cluster-Buster uses of 1 × 10−5. Region-to-gene importance scores were calculated using
Nature Methods
Article https://doi.org/10.1038/s41592-023-01938-4
gradient-boosting machine regression by predicting TF expression Seurat91 (v.4.0.3) was used to normalize, scale and perform PCA. Leiden
from imputed region accessibility, using all regions within a gene’s clustering was performed on the top 100 principal components with a
search space and using the importance score of each feature (region) resolution of 25, resulting in 199 clusters. Sub-clustering was performed
as the region-to-gene importance score. Spearman rank correlation was using STAMP92 (v.1.3; using the -cc -sd –chp options) resulting in 1,986
used to separate positive (>0.03) from negative (<−0.03) interactions. subclusters. TF annotations per subcluster were merged based on
A gene’s search space was defined as a minimum of 1 kb and a maximum direct and orthology evidence. These subclusters together with singlets
of 150 kb upstream/downstream of the start/end of the gene or the and dimer motifs form the clustered motif collection.
promoter of the nearest upstream/downstream gene. The promoter of
a gene was defined as the transcription starting site of that gene ±10 bp. Benchmarking pycisTarget
Binarizing region-to-gene importance scores. Region-to-gene Four different cisTarget databases were generated: (1) a database was
importance scores were binarized by taking the 85th, 90th and 95th generated using the unclustered motif collection; (2) a database was
quantile of the region-to-gene importance scores, the top 5, 10 and 15 generated using the STAMP-consensus motif per cluster; (3) a database
regions per gene based on the region-to-gene importance scores and was generated using the clustered motif collection; and (4) a database
a custom implementation of the BASC88 method on the region-to-gene was generated using the clustered motif collection but Transfac Pro
importance scores. motifs were removed. Motif enrichment analyses using these databases
eRegulon creation. For each TF, TF–region–gene triplets were and the cisTarget and DEM algorithm and Homer22 were performed
generated by taking all regions that are enriched for a motif annotated on 309 ChIP-seq datasets from ENCODE29,30 that were also included
to the TF and all genes linked to these regions, based on the binarized in UniBind35,36 (Supplementary Note 3). The enrichment of motifs
region-to-gene links. Gene set enrichment analysis (GSEA) was per- annotated to the TFs for which ChIP-seq was performed was assessed.
formed by ranking all genes based on their TF-to-gene importance score
and calculating enrichment of the set of genes within the TF–region– DEM on SOXE cistromes
gene triplet using the gsea_compute function from GSEApy (v.0.10.8). cisTarget and DEM were run on regions enriched for motifs anno-
Genes in the top of the ranking (leading edge) were retained and were tated to SOX10 in melanoma cell lines (see Melanoma cell line analysis;
the target genes of the eRegulon. This analysis was run separately for n = 18,506), SOX10 in oligodendrocytes (see Comparative analysis in
TF–gene and region–gene relationships with positive and negative cor- the mammalian brain using SCENIC+; n = 2,553) and SOX9 in astrocytes
relation coefficients. eRegulons with fewer than ten predicted target (see Comparative analysis in the mammalian brain using SCENIC+;
genes or obtained from region–gene relationships with a negative n = 6,817). For DEM, one-versus-all comparisons were made.
correlation coefficient were discarded.
eRegulon enrichment. All consensus peaks and all genes were Comparison of cisTopic and pycisTopic
ranked respectively by their imputed chromatin accessibility and A simulated single-cell epigenomics dataset from five melanoma cell
raw gene expression counts per cell. Enrichment for eRegulon target lines (three melanocytic and two mesenchymal) with 100 cells16 was
regions and target genes is defined as the AUC at 5% of the ranking and downloaded from https://github.com/aertslab/cisTopic. cisTopic
calculated using the AUCell function from the ctxcore Python package (v.2.1.0) using Collapsed Gibbs Sampling and WarpLDA and pycisTopic
(v.0.1.2.dev2+g1ffcf0f). (v.1.0.1.dev21+g8aa75d8) using Collapsed Gibbs Sampling and MALLET,
eRegulon dimensionality reduction. The eRegulon enrichment using 150 iterations and 21 cores for 21 models (starting from 2 topics
scores for regions and genes were normalized for each cell and used and from 5–100, increasing by 5), were run. For all models α was set to
as input into the UMAP, t-distributed stochastic neighbor embedding 50 divided by the number of topics and β was set to 0.1, as previously
(t-SNE) or PCA from the Python package UMAP (v.0.5.2), fitsne (v.1.2.1) described16,93.
or Scikit-Learn (v.0.24.2), respectively.
eRegulon specificity scores. eRegulon specificity scores were calcu- Cell-type discovery benchmark with ArchR, Signac and
lated, per cell type and eRegulon, using the RSS algorithm as described pycisTopic
elsewhere12,89 using target region or target gene eRegulon enrichment scATAC-seq datasets from ENCODE deeply profiled cell lines were
scores as input. Briefly, the Jensen–Shannon divergence was calculated simulated (see Benchmark of GRN inference methods), with different
by comparing the distribution of enrichment scores per cell type to the coverages (20,000, 10,000 and 3,000 fragments per cell) and num-
distribution that was set to all zeros, except for the cell type of interest, bers of cells (25,000, 10,000, 1,000 and 80 cells). In all cases, the bulk
where it was set to one. consensus peaks were used to generate the fragment count matrix
Triplet ranking. For all TF–region–gene triplets from eRegulons, (see Benchmark of GRN inference methods). pycisTopic was run as
rankings of TF-to-gene importance scores, region-to-gene importance described in the corresponding sections. ArchR and Signac were run
scores and the best-ranked position of the region across all motifs using default parameters. Briefly, Signac (v.1.9.0) was run using latent
annotated to the TF were aggregated as described by Aerts et al.46 semantic indexing (LSI), using the top 30 PCs (excluding the first PC
as recommend) for dimensionality reduction and clustering. ArchR
SCENIC+ motif collection (v.1.0.2) was run with default parameters, using iterative LSI, using the
The SCENIC+ motif collection includes more than 49,504 motifs from 29 top 30 PCs for dimensionality reduction and clustering. Dimensionality
motif collections (Supplementary Note 2 and Supplementary Table 3). reduction was performed using UMAP, using the PC matrix (ArchR and
Identical motifs across collections (after rescaling) were merged, Signac) or the topic contribution matrix (pycisTopic). To calculate the
resulting in 34,524 motifs. Motif-to-motif similarities using TomTom90 adjusted Rand index (ARI) in the power analysis based on simulated
(MEME v.5.4.1). Motifs with equal length and similarity q value < 10−40 data from ENCODE, hierarchical clustering was performed on these
were merged, resulting in 32,766 motifs (unclustered motif collection). matrices, making eight partitions based on the hierarchical tree using
For motif clustering, motifs, with an information content >5 that were the cutree() function from the stats R package. In the mouse cortex,
similar to at least on other motif with q value < 10−5 and not one of 1,265 batch correction (per sample) was performed using the recommended
dimer motifs nor part of the Factorbook and Desso collection, were approaches from each method. For pycisTopic, data were corrected
used (11,526 motifs), and the remaining were kept as singlets (9,685 using harmonypy (v.0.0.5) on the scaled cell–topic matrix (see Com-
motifs). Motif similarity q values were transformed as follows: parative analysis in the mammalian brain using SCENIC+). For Signac,
the integrated LSI approach was used, as described in the scATAC-seq
−45
−log 10 (TomTomq value )+10 data integration vignette from the package. Briefly, LSI was performed
Nature Methods
