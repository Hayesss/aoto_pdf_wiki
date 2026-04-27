---
source_path: /mnt/c/Users/Administrator/Zotero/storage/SBN3GVZM/s41586-024-07517-7.pdf
ingested: 2026-04-23
sha256: 32623f5242c64044
---

Article
Single-cell nascent RNA sequencing unveils
coordinated global transcription
https://doi.org/10.1038/s41586-024-07517-7 Dig B. Mahat1, Nathaniel D. Tippens1, Jorge D. Martin-Rufino2, Sean K. Waterton1,3, Jiayu Fu1,4,
Sarah E. Blatt1,5 & Phillip A. Sharp1 ✉
Received: 15 September 2023
Accepted: 3 May 2024
Transcription is the primary regulatory step in gene expression. Divergent
Published online: xx xx xxxx
transcription initiation from promoters and enhancers produces stable RNAs from
Open access genes and unstable RNAs from enhancers1,2. Nascent RNA capture and sequencing
Check for updates assays simultaneously measure gene and enhancer activity in cell populations3.
However, fundamental questions about the temporal regulation of transcription and
enhancer–gene coordination remain unanswered, primarily because of the absence
of a single-cell perspective on active transcription. In this study, we present scGRO–
seq—a new single-cell nascent RNA sequencing assay that uses click chemistry—and
unveil coordinated transcription throughout the genome. We demonstrate the
episodic nature of transcription and the co-transcription of functionally related
genes. scGRO–seq can estimate burst size and frequency by directly quantifying
transcribing RNA polymerases in individual cells and can leverage replication-
dependent non-polyadenylated histone gene transcription to elucidate cell cycle
dynamics. The single-nucleotide spatial and temporal resolution of scGRO–seq
enables the identification of networks of enhancers and genes. Our results suggest
that the bursting of transcription at super-enhancers precedes bursting from
associated genes. By imparting insights into the dynamic nature of global transcription
and the origin and propagation of transcription signals, we demonstrate the ability
of scGRO–seq to investigate the mechanisms of transcription regulation and the role
of enhancers in gene expression.
Transcription is a discontinuous process characterized by short bursts causal variants to genes remains challenging. Although low through-
and long inter-burst silent periods4,5. Decoding the origin and circuits put, genome-editing tools can potentially map enhancer–gene pairs,
of burst signals is crucial for understanding the mechanisms of tran- but the pleiotropic nature6 and weak effect of individual enhancers
scription regulation during the cell cycle, development and disease. hinder their utility.
Core promoter elements, transcription factors and enhancers are Existing genomic tools that probe the coding and non-coding
implicated in the regulation of burst kinetics, but their precise role in genome without perturbation by assessing chromatin conformation,
determining overall transcription output remains unsettled6,7. Whether histone modifications and chromatin accessibility have shed light on
the widely accepted view of stochastic transcription of individual genes the molecular events that lead up to enhancer-mediated gene activa-
conceals co-transcription of functionally related genes and coordina- tion. However, these tools do not fully confirm the actual activation
tion between enhancer–gene pairs holds broad significance in under- event12. Despite having similar chromatin features, the distinguish-
standing gene regulation. From a clinical perspective, assessing the ing feature of an active enhancer from its inactive counterpart is its
contribution of enhancers in the regulation of protein-coding genes transcription13. Nascent RNA sequencing assays, such as global run-on
can unlock a largely unexplored genomic landscape for therapeutics. and sequencing (GRO–seq)2 and precision run-on and sequencing
Active enhancers are occupied by transcription factors and RNA (PRO–seq)14, enable the simultaneous quantification of transcription
polymerase, similar to the gene promoters they regulate, which results in genes and enhancers. However, these bulk cell assays average the
in the synthesis of non-coding, non-polyadenylated and unstable discontinuous transcription from individual cells, which makes it chal-
RNA3,8. Enhancers are highly specific to cell types and states9, and exert lenging to decipher transcription dynamics and to assign enhancer–
cis-regulatory effects over long genomic distances10. Genome-wide gene relationships.
association studies further underscore the role of enhancers in gene Here we present a new single-cell nascent RNA sequencing method,
regulation, showing that more than 90% of genomic loci associated which we term scGRO–seq, that uses copper(I)-catalysed azide-alkyne
with traits and diseases are found in non-coding regions with many cycloaddition (CuAAC or click chemistry)15 to assess genome-wide
overlapping enhancers11. However, linking enhancers that harbour nascent transcription in individual cells in a quantitative manner. Our
1Koch Institute for Integrative Cancer Research and Department of Biology, Massachusetts Institute of Technology, Cambridge, MA, USA. 2Broad Institute of MIT and Harvard, Cambridge,
MA, USA. 3Present address: Department of Biology, Stanford University, Stanford, CA, USA. 4Present address: Interdisciplinary Biological Sciences Graduate Program, Northwestern University,
Evanston, IL, USA. 5Present address: Exact Sciences, Madison, WI, USA. ✉e-mail: sharppa@mit.edu
Nature | www.nature.com | 1
Article
analyses of genes and enhancers across 2,635 individual mouse embry- were sorted individually into 96-well plates. Each well contained
onic stem (ES) cells provide a comprehensive view of the dynamic nature a small volume of 8 M urea, which lyses the nuclear membrane and
of transcription. We leverage elongating RNA polymerases as built-in denatures RNA polymerase and releases propargyl-labelled nascent
clocks and measure the distance travelled from the transcription start RNA. The addition of CuAAC reagents led to the covalent linkage of
site (TSS) to estimate transcriptional burst kinetics. Using a class of propargyl-labelled nascent RNA to a unique 5′-AzScBc DNA molecule
cell-cycle-phase-specific genes undetected by most single-cell meth- in each well. After CuAAC, single-cell-barcoded nascent RNAs from
ods, we quantify the dynamics of transcription during the cell cycle. 96 wells were pooled, reverse transcribed in the presence of a tem-
We use the single-nucleotide temporal resolution of genome-wide plate switching oligonucleotide (TSO), PCR amplified and sequenced
transcription in individual cells to reveal the co-transcribed gene–gene (Extended Data Fig. 6). Despite a span of more than 3 years between
and enhancer–gene networks that are turned on within a few minutes the generation of various scGRO–seq library replicates, the differ-
of each other. Using a set of validated enhancer–gene pairs, our data ent batches showed strong correlation at the level of the 96-well plate
suggest that transcription initiates at enhancers before the activation (Extended Data Fig. 7a).
of transcription at the associated genes. Overall, scGRO–seq bridges a The scGRO–seq results recapitulated the inAGTuC and PRO–seq
gap in the study of temporal control of transcription and the functional profiles at both genes and enhancers (Fig. 1b) and provided a compre-
association of enhancers and genes. These insights will shed light on hensive map of nascent transcription in individual cells. We performed
gene regulatory mechanisms in essential cellular processes and disease. 17 batches of scGRO–seq experiments with 39 96-well plates and 3,744
cells, of which 36 plates and 2,635 cells passed the threshold (Meth-
ods). We captured an average of 3,665 reads and 1,503 features (genes
Development of scGRO–seq
and enhancers) per cell (Fig. 1c and Extended Data Fig. 7b). Moreover,
The primary challenge in capturing and sequencing nascent RNA from pseudo-bulk scGRO–seq counts from collapsed single cells in genes and
individual cells is attaching unique single-cell tags onto nascent RNA. enhancers correlated well with bulk counts from inAGTuC (Fig. 1d). An
Existing nascent RNA sequencing methods selectively capture tagged analysis of the sequencing depth indicated the possibility that more
nascent RNA from a cell population, which makes single-cell deconvolu- reads and features per cell could be discovered with further develop-
tion impossible. By contrast, single-cell RNA sequencing (scRNA-seq) ment of the technology and deeper sequencing (Extended Data Fig. 7c).
methods capture mRNA by annealing with the poly(A) tail and attaching However, scGRO–seq is less efficient in capturing nascent RNA from
single-cell barcode sequences by reverse transcription (RT). Nascent promoter–proximal pause sites. We attribute this limitation to the
RNA lacks a terminal poly(A) tract or any other consensus sequence reduced run-on efficiency of paused RNA polymerase II (PolII) in the
and must be selectively labelled and enriched from abundant total absence of a high concentration of strong detergent16. This difference
cellular RNA. in promoter–proximal run-on efficiency was reflected in the reduced
We designed a new strategy to selectively label nascent RNA through correlation between scGRO–seq and PRO–seq libraries (Extended Data
a nuclear run-on reaction in the presence of modified nucleotide Fig. 7d), as well as in the metagene profiles around the TSS of genes and
triphosphates (NTPs) compatible with CuAAC conjugation. CuAAC is enhancers (Extended Data Fig. 7e,f).
highly efficient and selective, robust under diverse reaction conditions, After confirming that scGRO–seq recapitulates results from bulk
enzyme-free and compatible with automation. First, we developed, nascent RNA sequencing methods, we benchmarked scGRO–seq
optimized and systematically characterized an assay for genome-wide against other RNA-based single-cell assays. The closest single-cell
transcriptome using click chemistry (AGTuC): a cell-population-based method that probes nascent transcription is intron seqFISH, which is
nascent RNA sequencing method that uses 3′-(O-propargyl)-NTPs in a multiplexed single-molecule in situ nascent RNA hybridization and
mouse ES cells (Extended Data Figs. 1a–f and 2a–d). It takes about 8 h imaging method17. We confirmed that the correlation between scGRO–
to prepare an AGTuC library. However, the high concentration of ionic seq and intron seqFISH is similar to the correlation reported between
detergent in AGTuC disrupts nuclear membranes during the run-on intron seqFISH and GRO–seq (Fig. 1e). By contrast, scGRO–seq poorly
reaction, which makes RNA from individual cells indistinguishable for correlated with scRNA-seq (Extended Data Fig. 1g), which is probably
single-cell barcoding. We therefore developed an iteration of AGTuC due to differences in mRNA stability and capture methods. Neverthe-
whereby nascent RNAs in individual nuclei are labelled with alkyne less, as expected, scGRO–seq reads were more likely to be intronic or
through run-on with 3′-(O-propargyl)-NTPs but without disrupting the intergenic than scRNA-seq reads (Fig. 1f). Overall, the suite of genomic
nuclear membrane (termed intact-nuclei AGTuC (inAGTuC)) (Extended assays presented here utilizes a new biochemical approach to provide
Data Figs. 3a–j and 4a–h). We prepared inAGTuC libraries in 96-well a snapshot of genome-wide transcription at various cell resolutions,
plates with 12 cells per well (c.p.w.), 120 c.p.w. and 1,200 c.p.w. (which is including individual cells.
roughly equivalent to 1,000, 10,000 and 100,000 nuclei, respectively).
We tested for correlation between this method and with PRO–seq
Direct measurement of burst kinetics
(Extended Data Fig. 5a–d), and the results demonstrated the feasibility
of profiling nascent RNA with small sample sizes. Based on the cor- Estimates of transcriptional kinetics primarily come from
relation slope, the inAGTuC library with as low as about 1,000 nuclei low-throughput live-cell imaging or fluorescent in situ hybridization
showed similar efficiency as PRO–seq in detecting nascent transcrip- in fixed cells18,19. The intron seqFISH method is limited to predefined
tomes. The higher efficiency, lower cost, shorter library preparation gene targets, requires specialized probes and assumes that all intronic
time and lower sample input make AGTuC and inAGTuC viable alterna- RNAs have the same kinetic fate. Approaches based on next-generation
tives to existing methods such as PRO–seq. By enabling the compart- sequencing (NGS) are comprehensive and technically more acces-
mentalization of intact nuclei that contain click-compatible nascent sible. However, the current methods measure polyadenylated mRNA
RNA and 5′-azide single-cell-barcoded (5′-AzScBc) DNA molecules from single cells20 and fit a simple two-state mathematical model to
using fewer nuclei, inAGTuC laid the ground for single-cell nascent infer transcriptional kinetics7. Bridging this gap, scGRO–seq combines
RNA sequencing. high-throughput measurement of transcription with NGS, thereby
Building on this foundation, we applied our newly developed chem- enabling the detection of transcribing RNA polymerases genome-wide
istry to single cells (Fig. 1a). For congruence with the original nascent at single-nucleotide resolution (Fig. 2a).
RNA sequencing method of GRO–seq, we named this single-cell version With this new approach, we examined the evidence of bursting
scGRO–seq. Intact nuclei containing nascent RNA labelled with prop- de novo without previous assumptions by quantifying the incidence
argyl, following a nuclear run-on reaction with 3′-(O-propargyl)-NTPs, of transcribing RNA polymerases. If transcription occurs in bursts, we
2 | Nature | www.nature.com
Isolation
of nuclei Nascent RNA Single-nuclei
sorting
+
RNA polymerase
Each well contains:
Denaturing agent (urea)
TSO Single-cell barcode
Unique 5′-AzScBc DNA
5′- GGG -3′ UMI
CCC
RT primer p5 5′- -C C + N 3 - -3′ Alkyne nascent RNA 5′-AzScBc DNA
p7 p5 -3′
-5′
5′- -3′
Chr. 19: 38923054–38999071
scGRO–seq
collapsed
inAGTuC
PRO–seq
p300
ATAC–seq
H3K4me3
H3K27Ac
H3K4me1
would anticipate a higher occurrence of more than one RNA polymerase (FDR) = 0.05) and a greater number of multiplets (n = 828, FDR = 0) in
per burst (multiplets) than would be expected by chance. Based on the the real data, which provided evidence for the bursting nature of tran-
approximately 10% capture efficiency of scGRO–seq estimated from scription (Fig. 2b). This result represents a significant 2.4% excess of
comparison with intron seqFISH (Methods), the probability of detect- multiplets in real data compared with permuted data. Transcriptional
ing two consecutive RNA polymerases on a gene is 1%. To account for bursting would also result in more closely spaced RNA polymerases
differences in unique molecular identifiers (UMIs) per cell, we devised than what would be observed by random chance. When examining the
a null model using permutation. We permuted reads among cells while distance between multiplets, we observed enrichment of closely spaced
keeping UMIs per cell and polymerase position unchanged (Methods; RNA polymerases (P < 0.05, two-sample Kolmogorov–Smirnov (KS)
n = 200 permutations). We then compared the real data to the permuted test) (Fig. 2c and Extended Data Fig. 8a), which further strengthened
control data and observed fewer singlets (n = 1,052, false discovery rate the evidence of bursting.
Nature | www.nature.com | 3
qes–ORGcs sllec
elgnis
sdnarts
esnes
10 kbp
dREG
Hells
qes–ORGcs sllec
elgnis
sdnarts
esnesitna
a
b
500 bp 10 kbChr. 3: 96434539–96439297
scGRO–seq
collapsed
inAGTuC
PRO–seq
p300
ATAC–seq
H3K4me3
H3K27Ac
H3K4me1
dREG
Enhancer
esreveR noitpircsnart
[0–3] [0–3]
[–3–0] [–3–0]
[0–3] [0–3]
[–3–0] [–3–0]
[0–6] [0–6]
[–6–0] [–6–0]
[0–46] [0–20]
[0–24] [0–6.5]
[0–4.5] [0–0.63]
[0–1.9] [0–0.24]
[0–0.5] [0–0.48]
y = 0.94x, r2 = 0.93 1,000
100
10 4,000 3,000 1 2,000 1,000
1 10 100 1,000
)ydob
eneg(
qes–ORGcs
noillim
rep sIMU sruobhgien fo .oN
1.00
0.75
0.50 0.25
0
inAGTuC (gene body)
UMIs per million
noitcarF
3′ UTR Intergenic
5′ UTR Intronic
CDS
1 × 105
1 × 104
1 × 103 1 × 102 5,000 4,000 3,000 1 × 101 1 2 , , 0 0 0 0 0 0
1 × 101 1 × 103 1 × 105
)recnahne(
qes−ORGcs
noillim
rep sIMU
y = 0.5x, r2 = 0.99 1.000
0.100
0.010 2,000 0.001 1,000
0.01 0.10 1.00
Intron seqFISH
(counts per cell)
)llec
rep sIMU(
qes–ORGcs
y = 0.26x, r2= 0.58 200
150
100 50
0
0 2,500 5,000 7,500 10,000
Reads per cell
sllec
fo rebmuN
O O O Base
HO P O P O P O O
OH OH OH
O OH
Run-on with 3′-(O-propargyl)-NTPs
3′-
-5′ PCR amplification
CuAAC 5′-
3′-
c d e f
Batch Exp156 Exp160
Exp208 Exp211 Exp236
Exp246 Exp260 Exp260b Exp263 Exp264a
scGRO scRNA
–seq –seq
inAGTuC (enhancer)
UMIs per million
qes–ORGcs
qes–ORGcs
sllec
elgnis
sllec
elgnis
sdnarts
esnes
sdnarts
esnesitna
sruobhgien fo .oN sruobhgien fo .oN
Fig. 1 | Schematics and benchmarking of single-cell nascent RNA sequencing. and 250 bp regions from each end of the enhancers analysed were removed to
a, A summary of the scGRO–seq workflow. b, Representative genome browser only include nascent RNA from elongating RNA polymerases. Data are plotted
screenshots showing scGRO–seq UMIs at a single-cell resolution, the aggregate on a log–log scale to show the range of data distribution. e, Correlation
scGRO–seq profile, the inAGTuC profile, the PRO–seq profile and chromatin between scGRO–seq UMIs per cell from up to the first 20 kb of genes and intron
marks around a gene (left) and an enhancer (right). c, Distribution of scGRO–seq seqFISH counts per cell in the body of genes used in the intron seqFISH study
UMIs per cell. d, Correlation between aggregate scGRO–seq and inAGTuC UMIs (n = 9,666). f, Distribution of scGRO–seq and scRNA-seq UMIs in various
per million sequences in the body of genes (left, n = 19,961) and enhancers genomic regions.
(right, n = 12,542). UMIs from the 500 bp regions from each end of the genes
Article
1.050 Observed Permuted
1.025
1.000
0.975
0.950
Singlets Multiplets
(n = 1) (n > 1)
RNA polymerase per burst
1,500
1,000
500
0
0.01 0.10 1.00 10.00
Npm1 (10.7 kb) Burst frequency (per h)
With confidence in the ability of scGRO–seq to discern bursting, we tested our model by simulation and observed robust performance
directly measured burst kinetics using scGRO–seq counts and their (Extended Data Fig. 8c). Burst frequency results from scGRO–seq data
genomic positions. We estimated burst size as the average number of correlated well with intron seqFISH data (Fig. 2f), and the correlation
RNA polymerases per burst, whereas burst frequency was calculated was even stronger for genes with a higher burst frequency (Extended
as the number of bursts per allele per unit of time required for RNA Data Fig. 8d). However, we observed a poor correlation between burst
polymerase to traverse through the burst window (Fig. 2d), corrected frequencies from scGRO–seq and scRNA–seq data, as well as between
for capture efficiency (Methods). We considered genes longer than 11 kb intron seqFISH and scRNA-seq data (Extended Data Fig. 8e). This find-
(n = 13,564) and excluded 500 bp regions at either end that are known ing highlights potential limitations in kinetic estimates derived from
to harbour paused polymerases21, thereby using the remaining 10 kb as mature transcripts. In contrast to a previous report18, we did not find
the burst window. We assigned reads to a single allele based on previous an impact of gene length on kinetic estimates (Extended Data Fig. 8f).
evidence showing that alleles in mouse ES cells burst independently to We further confirmed that the burst frequencies calculated from 10 kb
generate monoallelic RNA22. With an average RNA PolII elongation rate and 5 kb burst windows showed strong agreement (Extended Data
of 2.5 kb min–1 (ref. 23), using a 10 kb region limited the burst detection Fig. 8g), which indicated the reliability of burst kinetic calculations
window to 4 min. This short burst window was consistent with bursts from scGRO–seq data.
from one allele and aligned with previous reports24. We simulated Core promoter elements can modulate burst parameters7,25. We
kinetic measurements using synthetic data to validate the accuracy observed a significant variation in core promoter elements with burst
of the model and observed robust performance (Extended Data Fig. 8b). kinetics (Fig. 2g). Specifically, genes with the TATA element exhibited a
We then estimated the kinetic parameters of transcriptional bursts for larger burst size than genes lacking it (P = 4.6 × 10−9), and the presence
expressed genes (Fig. 2e and Supplementary Table 1). Burst sizes ranged of the initiator sequence further increased the burst size (P = 2.5 × 10−13).
primarily between 1 and 4 RNA polymerases per burst, with a mean The higher burst size but lower burst frequency of genes with TATA
burst size of 1.23. The mean duration of approximately 2 h until the next elements agreed with previous findings26.
burst obtained using scGRO–seq data matched the 2 h of the global Transcription factors are also thought to regulate burst kinetics.
nascent transcription oscillation cycle reported using intron seqFISH. Using a curated transcription factor binding database27,28, we exam-
Using the burst parameters estimated from scGRO–seq data, we again ined the effect of transcription factors on burst parameters. Gene set
4 | Nature | www.nature.com
detumrep
ro
devresbo
fo oitaR
detumrep
revo
857,157
= n
018,257
= n
079,53
= n
241,53
= n
1.2
1.0
0.8
0 0.5 1.0 1.5 2.0 2.5
Distance between RNA polymerases
within a pair (kb)
sriap
esaremylop
ANR
fo oitaR
)detumrep/devresbo(
C1 Burst window
C3
C5 C7
C9
Cn – 6
scGRO–seq Cn – 4
single cells Cn – 2 st s ra e n n d se s Cn
Burst size = Average reads per burst
Number of bursts per allele Burst frequency =
Burst window length/transcription rate
scGRO–seq
collapsed
1.00 PRO–seq
p300 ATAC–seq 0.10
H3K4me3 H3K27Ac 3,000
H3K4me1 2,000 Cdk9 0.01 1,000
RNA PolII
dREG Chr. 11: 33143012–33166451 0.01 0.10
Npm1
ycneuqerf
tsrub
qes–ORGcs
)h rep(
a
y = 2.34x, r2 = 0.66
900
600
300
0
0.1 1.0 10.0 1.00
Time until burst (h) Intron seqFISH burst
frequency (a.u.)
3
2
1
ezis stsruB
10
1
0.1
TATA No Inr No TATA No TATA No Inr No TATA No
TATA Inr +Inr TATA+Inr TATA Inr +Inr TATA+Inr
)h rep(
ycneuqerf
tsruB
0.5
0.4 0.3 0.2
0.1 0
6
4 2
0
0 4,000 8,000
Burst size rank
erocs
tnemhcirnE
cirtem
tsil deknaR
MYC targets
0.7
0.5 0.3 NES: 3.86
q value: 0 0
15 Enrichment profile
10 H Ra it n s king metric scores 5
0
12,000
erocs
tnemhcirnE
cirtem
tsil deknaR
b c d
e f
10,000
1,000
100
10
1
0 2 4 6
g h
AFF4 targets
NES: 1.99
q value: 0
Enrichment profile
Hits Ranking metric scores
0 4,000 8,000 12,000
Burst frequency rank
serutaef
fo rebmuN
[0–3]
[–3–0]
[0–6]
[–6–0]
[0–34]
[0–4.88] [0–1.85]
[0–17]
[0–131]
Burst size
sruobhgien
fo .oN
[[00––5533]]
[[00––00..4433]]
E ihh
Fig. 2 | Inference of transcription kinetics using scGRO–seq. a, Single-cell up to 2.5 kb are shown in 50 bp bins. d, Illustration of the model used for direct
view of multiplet RNA polymerase (blue dots) in Npm1. A yellow line connects inference of burst kinetics from scGRO–seq data. e, Histogram of burst size (left),
RNA polymerases within the same cell. Randomly sampled 75 single cells burst frequency (middle) and duration until the next burst (1/burst frequency)
containing more than one RNA polymerase are shown on the top, followed (right) for genes that are at least 10 kb long (n = 13,142). f, Correlation of burst
by the aggregate scGRO–seq, PRO–seq, chromatin marks and transcription- frequency of genes between scGRO–seq and intron seqFISH data. g, Effect of
associated factors profiles. b, Ratio of observed or permuted burst sizes promoter elements in burst size greater than 1 (left) and burst frequency (right).
compared against the average burst sizes from 200 permutations. c, Ratio Inr, the initiator motif. The centre line indicates the median of the distribution.
of the observed distance between consecutive RNA polymerases in the first h, Gene set enrichment analyses showing the role of transcription factors in
10 kb of gene bodies in individual cells against the permuted data. Distances determining burst frequency and burst size.
a
10,000
14%
29% 7,500
5,000
57% 2,500
G1/S S G2/M 0
G1/S S G2/M
G1/S
S
G2/M
enrichment analysis indicated that some transcription factors regulate lengths of cell cycle phases (Fig. 3b). Notably, cells in G1/S and G2/M
burst size, whereas others regulate burst frequency (Supplementary phases exhibited higher transcription levels compared with cells in
Table 2). MYC and AFF4 are examples of each category. Genes bound by the S phase (Wilcoxon rank-sum test, P = 6.3 × 10−07 and P = 1.2 × 10−06,
MYC had larger burst sizes, whereas AFF4 target genes were enriched respectively) (Fig. 3c). We observed an approximately 40% decrease in
for higher burst frequencies (Fig. 2h). Our observation supports a total transcription when cells transition from the G1/S phase to the
previous report whereby MYC increased the burst size by increasing S phase, with a subsequent 20% increase after exiting the S phase to the
the burst duration29, and the association of the AFF4 transcription G2/M phase. This observation indicates that transcription continues
factor correlated with burst frequency30. Overall, we show that direct during DNA replication, albeit at a reduced level. The transition from the
and comprehensive observation of transcription using scGRO–seq G2/M phase to the G1 phase is marked by an increase in transcription38,
facilitates the study of transcription kinetics at the single-cell level. which restores the transcription level observed during the G1 phase,
thereby completing the cycle. An analysis of differentially expressed
genes in cell cycle phases also revealed that certain genes restore tran-
Cell cycle inference from histone genes
scription levels to those observed in the G1/S phase as they transitioned
Investigating gene programs during cell cycle stages is essential for from the S phase to the G2/M phase, whereas others regained partial
understanding biology and disease31. Polyadenylated RNA-dependent transcription (Fig. 3d and Supplementary Table 3). At the same time,
scRNA-seq methods rely on mature transcripts of cell cycle marker some did not recover their transcription until exiting from G2/M to
genes to determine the cell cycle state. However, the time required G1/S. By quantifying the active transcription of non-polyadenylated
for mRNA processing, export and accumulation introduces a time lag. histone genes and a small subset of marker genes, scGRO–seq reveals
Except for a few total RNA-based single-cell methods32,33, scRNA-seq fails a dynamic transcription program throughout the cell cycle.
to detect replication-dependent histone genes—the best character-
ized cell-cycle-phase-specific genes exclusively transcribed during the
S phase34—owing to the lack of polyadenylation35. scGRO–seq enabled Co-transcription of interdependent genes
the detection of active transcription of replication-dependent histone Co-expression of functionally related genes, as measured by accumu-
genes in the histone locus body (Extended Data Fig. 9a) that could be lated mRNA, is widely reported39. However, assessing whether these
used to classify cells in S phase. For G1/S and G2/M phase-specific genes, genes are transcriptionally coordinated in steady-state has been chal-
we used a set of transcriptionally characterized genes from a RNA veloc- lenging. By utilizing nascent transcription within the first 10 kb of the
ity and deep-learning study of mouse ES cells36. Hierarchical clustering gene body, thereby limiting the co-transcription detection window
based on the expression of these three sets of cell-cycle-phase-specific to 4 min, we calculated pairwise Pearson correlation values between
genes revealed three significant clusters of individual cells (Fig. 3a). expressed genes (Fig. 4a). Gene pairs with a correlation coefficient
Mouse ES cells have a short G1 phase and an extended S phase37. greater than 0.1 and a q value of less than 0.05, and an empirical FDR of
De novo classification of mouse ES cells based on the nascent tran- less than 5% from 1,000 permutations, were considered co-transcribed
scription of these newly integrated marker genes recapitulated the (Supplementary Table 4). These stringent criteria controlled for
Nature | www.nature.com | 5
)DR(
senotsiH
c2piD 22rtalP 2lnmF fncC 1eeW 1kdC akruA 2ancC 1pasuN lboC ikgD a04fprP 3a1clS 2hctapG 25niL 1gmS 2stuA 1pisP 2espH 43psU 1smP 2encC xteS 6mcM 1encC 1crO 2vaN 1fluS 3ffA b3boM noS kiR61P7030162 3tilS 2lhrG 1smiR 93ktS 2xepA 6ppD 1baD 2glcuS 4coxE 21pirT 3yfdW b6coxE 1tacB 2igaM 1ntK l1mpP 2xofbR a12fhP crpprL 3kiS d231memT 1mdaC 75memT 2rceC b2piD 2l14bpE 6sreC adahT ppneC rwaP 1croM 1seY pacrS 71lxbF acacA 31a52clS 33rdW 1fsR adE 1omlE b82niL 2l7cuL 1ftE d082pfZ kdA 2cnB 2lbA sdmG 1sprT erB 1dsN 2hcaB 1dbrS 2e2ebU lydC ytU 5goC 264pfZ 1ccramS 1l7fcT 11fgeM 3dohF
1
e
0c or
z
s
−1
llec
rep
sIMU
b c
Counts
14
G1/S 12
10
S 8
6
4
G2/M 2
0
d
Fig. 3 | Cell cycle inference by non-polyadenylated replication-dependent by cell-cycle-phase-specific gene transcription. The centre line indicates
histone gene expression. a, Heatmap of hierarchical clustering of single cells the median, the box represents the data between the first and third quantiles,
representing transcription of G1/S-specific, S-specific and G2/M-specific genes. the whiskers indicate the 1.5 interquartile range, and points outside the
The dendrogram colours represent cell clusters with cell-cycle-phase-specific whiskers indicate outliers. d, Differentially expressed genes among the three
gene transcription. b, Fraction of cells in the three primary clusters distinguished clusters of cells defined by transcription of G1/S-specific, S-specific and
by transcription of G1/S-specific, S-specific and G2/M-specific genes. G2/M-specific genes. The genes used to classify cells are denoted in bold and
c, Distribution of scGRO–seq UMIs per cell in the three clusters of cells coloured boxes. Histones (RD) represent aggregate reads from replication-
(n = 122, 479 and 244 cells, respectively, from 10 independent batches) defined dependent histone genes.
Article
a
0.004 0.003
0.002 0.001
0.05 0.10
Enrichment fraction
sampling biases and other confounding effects. We identified about genes and enhancers to avoid paused polymerase. We also included
0.7% of the 112,807,710 gene pairs tested (n = 800,888) as signifi- clusters of enhancers known as super-enhancers (SEs) that do not
cantly co-transcribed. We generated a graphical network from these overlap with gene regions41.
significant pairs and identified 59 modules (genes per module > 10) We used stringent criteria in permutation and correlation tests to
of co-transcribed genes. This gene–gene transcriptional correlation identify enhancer–gene pairs that exhibit co-transcription (Methods).
probably reflects common temporal gene activation by a transcription Out of 6,985,904 test pairs, 0.6% (n = 44,361) passed the threshold of
factor or could reflect mechanistic coupling of transcription activation the pairwise correlation coefficient, multiple hypothesis corrected
by clusters of genes separated across regions of chromosomes. chi-square P value and empirical FDR from 1,000 permutations (Supple-
Conducting gene ontology analysis on these co-transcribed mod- mentary Table 6). We observed a significant enrichment (two-sample
ules compared with all transcribed genes, we found enrichment of KS test, P = 5.5 × 10−09) of enhancer–gene co-transcription primar-
several related molecular functions, including cell cycle regulation, ily within 200 kb of each other compared with uncorrelated pairs
RNA splicing, translational control, DNA repair and circadian rhythm (Fig. 5a). SE–gene pairs were similarly enriched (two-sample KS test,
(Fig. 4b, Extended Data Fig. 9b and Supplementary Table 5). By scanning P = 1.3 × 10−09) within 400 kb of each other (Extended Data Fig. 10a).
the promoters of co-transcribed genes, we discovered an enrichment When examining functionally related genes clustered together on the
of known transcription factor motifs, such as FOXO3 enriched in the same chromosome42, we found multiple enhancers correlated with
promoters of co-transcribed genes associated with the ‘regulation of each gene (Extended Data Fig. 10b), probably a further manifestation
cell-cycle phase transition’ gene ontology term. A previous study40 of cell cycle regulation.
showed that FOXO3, in coordination with the DNA replication fac- We investigated a set of validated enhancers known to regulate
tor CDT1, is crucial in regulating cell cycle progression. We compared pluripotency transcription factors43–46. We observed significant cor-
the co-transcription patterns of gene pairs obtained from scGRO–seq relations between the transcription of Sox2 and Nanog and their dis-
with those from intron seqFISH, and the results revealed concordant tal enhancers (Extended Data Fig. 10c). If enhancers and their target
co-transcription profiles (Fig. 4c). This high-throughput and capabil- genes are temporally coupled and co-transcribed, we speculated that
ity of scGRO–seq to directly examine transcriptional coordination co-transcription of the pair could be even more prominent at finer
between any gene pair or network of genes provides valuable insights temporal resolution. To test this idea, we divided enhancers and genes
into the functional organization of the genome. into 5 kb bins (representing a 2-min transcription window) and found
that at least 1 enhancer bin correlated significantly with its target gene
for all 4 genes (Fig. 5b). Notably, the correlated enhancer bin generally
Enhancer–gene temporal coordination
appeared further from its TSS than the gene bin, which implied that
Regulation of gene expression by distal regulatory elements is an area enhancer transcription may initiate before promoter transcription.
of broad interest. scGRO–seq captures transcripts from both genes and To test the enhancer–gene timing hypothesis, we examined a set of
active enhancers, thereby enabling the measurement of co-activation seven non-intronic mouse ES cell SEs validated by CRISPR perturba-
in single cells. We analysed scGRO–seq reads within the first 10 kb of tion47. CRISPR-mediated knockout of Sall1 SE reduced Sall1 expres-
genes and at least 3 kb on each strand transcribing outwards around sion by 92%, and we found a correlation between multiple enhancer
enhancers (Methods). We excluded 500 bp regions around the TSS of bins and this gene (Fig. 5c). Overall, four out of seven SE–gene pairs
6 | Nature | www.nature.com
eulav
q
Gene A |||| Nuclear pore (Smarcc1) Ubiquitin-dependent protein catabolic process Cell cycle checkpoint signalling
DNA integrity checkpoint signalling Heterochromatin formation
PML body
Circadian rhythm Telomere organization Foxo3
mRNA splice site selection
Regulation of histone methylation
Regulation of cell cycle phase transition Gene B Inactivation of X chromosome (Prkdc) Stress granule assembly
0 10 20 30 Histone acetylation
Translation initiation factor activity Distance from TSS (kb) Cellular response to LIF
U1 snRNP
Regulation of cell cycle process 1
Cytoplasmic stress granule
DNA repair
Translational initiation mRNA 3′ UTR binding 0.1
RNA localization Nuclear speck Histone modification Chromatin organization Regulation of translation 0.01 40,000 RNA transesterification reactions 30,000
RNA splicing 20,000 Ribonucleoprotein complex 10,000 mRNA binding 0.001
0 0.001 0.01 0.1 1
noitpircsnart-oc
qes–ORGcs
1.00
0.75
0.50 0.25
0
0 0.2 0.4 0.6
Pearson correlation coefficient Intron seqFISH co-transcription
eulav
P erauqs-ihC
detcerroc-RDF
eulav P
b
Mdm2 Prkdc Mnat1 Ino80 Taok1 Larp7 Zwint
Smarcc1 Thoc1
Ankrd17
Ddx3x Senp2
Ddx39b
Npm1
Fem1b Dbf4 Chfr Orc1Anp32b Trp53
c Jade1
y = 0.29x, r2 = 0.59
1.00
0.75 0.50 0.25 0 sruobhgien
fo .oN
Fig. 4 | Coordinated transcription of functionally related genes. a, Top, The transcription factor motif enriched in the promoters of genes associated
a pair of co-transcribed genes. Reads within the first 10 kb of the gene pair with the GO term and the co-transcribed genes that contributed to the
(blue circle) expressed in the same cells are connected by a yellow line. Reads enrichment of the GO term is shown as an example on the right (red line
beyond the first 10 kb (grey circles and lines) were not used in the gene–gene indicating ρ > 0.15). A complete list of GO terms and the co-transcribed genes
correlation. Bottom, pair-wise Pearson correlation was calculated from a contributing to the enrichment of the GO terms is provided in Supplementary
binarized genes by cells matrix. The relationship among the Pearson correlation Table 5. c, Correlation of co-transcription of significantly co-transcribed gene
coefficient, uncorrected chi-square P value and the FDR-corrected P value using pairs (n = 164,380) between scGRO–seq and intron seqFISH data. Axes represent
the Benjamini–Hochberg correction method for pairwise gene–gene correlation. the fraction of cells in which a gene pair is co-transcribed.
b, Gene ontology (GO) terms enriched in co-transcribed gene modules.
a
0.00100 C N o o - t t c ra o n -t s r c a r n ib s e c d rib p e a d ir s pairs Chr. 3
0.00075
Sox2
0.00050 108 kb
0.00025
Chr. 6
0 5 kb
0 500 1,000 1,500 2,000 2,500
45 kb 58 kb
Scrambled random pairs CRISPR-verified pairs
Chr. 17
Pou5f1
2 kb
Chr. 4
Bin 4 Bin 2 Bin 1 Bin 3 Bin 4 Bin 2 Bin 1 Bin 3
Bin 3 Bin 1 Bin 2 Bin 4 Bin 3 Bin 1 Bin 2 Bin 4
Klf4 68 kb
showed correlations of at least one bin. Notably, we observed that in current single-cell protocol. To streamline the process and to ensure
most cases, enhancer transcription began earlier or around the same compatibility with future automation, we optimized the biochemical
time as the transcription of their target genes (Fig. 5d). This temporal steps by replacing multiple rounds of nascent RNA purification and
pattern could have mechanistic implications for enhancer–gene regu- nucleic acid ligation with click chemistry. Further adaptations, includ-
lation. However, any conclusions will require a much deeper dataset. ing high-throughput droplet encapsulation and enhanced capture
Nevertheless, our findings offer a glimpse into the temporal order in efficiency, will extend the applicability of our scGRO–seq method in
enhancer–gene transcription. both research and clinical settings.
For clinical specimens, particularly for challenging tissues such
as the brain and pancreas, which contain high levels of RNase, isola-
Discussion
tion of nuclei is preferred over intact cells. Single-cell methods such
We developed scGRO–seq to enable the assessment of co-transcription as sNuc-seq49 profile polyadenylated RNA inside the nucleus of such
and prediction of enhancer–gene regulatory networks in their native tissues, but paint an incomplete view of single-cell gene expression. By
context. By reporting the activity of genes and distal regulatory ele- contrast, the entire scGRO–seq substrate is present inside the nucleus.
ments—and therefore the functional consequences of transcrip- Furthermore, the compatibility of CuAAC-based nascent RNA sequenc-
tional signals and networks—scGRO–seq is inherently multimodal ing methods with bulk low-input samples and single cells makes them
for understanding transcription regulation in high detail. We illus- desirable methods for clinical investigations. The adaptability and effi-
trated these advantages by determining burst size and frequency for ciency of scGRO–seq introduce new avenues for investigating transcrip-
expressed genes, transcription dynamics during cell cycle phases and tional dynamics and regulatory mechanisms across diverse biological
genome-wide gene–gene and enhancer–gene co-transcription detec- contexts, enriching our understanding of gene expression regulation
tion. We restricted this study to mouse ES cells for comparison with and its ramifications in physiological and pathological conditions.
large available datasets for validation.
The current scGRO–seq methodology has its limitations. The pres-
Online content
ervation of nuclear integrity, achieved through a low sarkosyl concen-
tration, failed to promote the run-on of RNA polymerases in the pause Any methods, additional references, Nature Portfolio reporting summa-
complex, thereby limiting the detection of promoter–proximal paused ries, source data, extended data, supplementary information, acknowl-
polymerases. The read depth and cell numbers limited our analyses edgements, peer review information; details of author contributions
of burst kinetics and co-transcription of gene–gene and enhancer– and competing interests; and statements of data and code availability
gene pairs. Improved efficiency in future iterations will facilitate more are available at https://doi.org/10.1038/s41586-024-07517-7.
precise evaluation of these phenomena.
scGRO–seq is also limited by the abundance of nascent RNA per cell at
any given time, which is considerably lower than that of mature mRNA. 1. Birney, E. et al. Identification and analysis of functional elements in 1% of the human
genome by the ENCODE pilot project. Nature 447, 799–816 (2007).
Nascent RNA detection requires technology that does not depend
2. Core, L. J., Waterfall, J. J. & Lis, J. T. Nascent RNA sequencing reveals widespread pausing
on a polyadenylated terminus, which initially raised doubts about and divergent initiation at human promoters. Science 322, 1845–1848 (2008).
the feasibility of nascent RNA sequencing in single cells48. However, 3. Core, L. J. et al. Analysis of nascent RNA identifies a unified architecture of initiation
regions at mammalian promoters and enhancers. Nat. Genet. 46, 1311–1320 (2014).
implementing highly efficient CuAAC has overcome this limitation,
4. Chubb, J. R., Trcek, T., Shenoy, S. M. & Singer, R. H. Transcriptional pulsing of a
enabling the capture of approximately 10% of nascent RNA with the developmental gene. Curr. Biol. 16, 1018–1025 (2006).
Nature | www.nature.com | 7
ytisneD
b c
Chr. 8: 88975800–89072000 10 kb
scGRO-seq[0–3]
(collapsed)
[–3–0]
[0–6]
PRO–seq
[–6–0]
Nanog p300 [0–641]
Enhancer to gene distance (kb) ATAC–seq[0–39]
d H3K4me3[0–4.04]
H3K27ac[0–2.57]
0.3 H3K4me1
Oct4[0–145]
0.2 Sox2[0–145]
Nanog[0–145]
Cdk9[0–25]
0.1 RNA PolII[0–44]
5-kb bins
0
−4 −2 0 2 4 −4 −2 0 2 4
Difference in correlated bin position from TSS Sall1 SE Sall1
(Enhancer − gene)
ytisneD
[[00––00..7755]]
Fig. 5 | Spatial and temporal coordination between genes and enhancers. distance bars. For finer time resolution correlation, features are extended up
a, Distance between correlated and non-correlated enhancer–gene pairs to the end of the transcription signal and divided into 5 kb bins. Correlated
within 2.5 Mb of each other. b, Co-transcription between pluripotency genes bins are represented by a red arch, except for Sox2 and its distal enhancer bins,
(filled blue arrows indicate sense gene bins, open blue arrows indicate which are shown in different colours for visual aid. c, Co-transcription between
antisense gene bins) and their enhancers (represented by green arrows, Sall1 and its CRISPR-verified SE. Correlated SE–gene bins are denoted by arches.
and the arrow directions indicate sense and antisense directions). Correlated d, Summary of correlated bin positions in CRISPR-verified SE–gene pairs.
full-length enhancer–gene pairs (Sox2 and Nanog) are shown with purple Scrambled random pairs served as a control.
Article
5. Raj, A., Peskin, C. S., Tranchina, D., Vargas, D. Y. & Tyagi, S. Stochastic mRNA synthesis in 32. Salmen, F. et al. High-throughput total RNA sequencing in single cells using VASA-seq.
mammalian cells. PLoS Biol. 4, e309 (2006). Nat. Biotechnol. 40, 1780–1793 (2022).
6. Fukaya, T., Lim, B. & Levine, M. Enhancer control of transcriptional bursting. Cell 166, 33. McKellar, D. W. et al. Spatial mapping of the total transcriptome by in situ polyadenylation.
358–368 (2016). Nat. Biotechnol. 41, 513–520 (2023).
7. Larsson, A. J. M. et al. Genomic encoding of transcriptional burst kinetics. Nature 424, 34. Robbins, E. & Borun, T. W. The cytoplasmic synthesis of histones in HELA cells and
147 (2019). its temporal relationship to DNA replication. Proc. Natl Acad. Sci. USA 57, 409–416
8. Hah, N. et al. A rapid, extensive, and transient transcriptional response to estrogen (1967).
signaling in breast cancer cells. Cell 145, 622–634 (2011). 35. Marzluff, W. F., Wagner, E. J. & Duronio, R. J. Metabolism and regulation of canonical
9. Long, H. K., Prescott, S. L. & Wysocka, J. Ever-changing landscapes: transcriptional histone mRNAs: life without a poly(A) tail. Nat. Rev. Genet. 9, 843–854 (2008).
enhancers in development and evolution. Cell 167, 1170–1187 (2016). 36. Riba, A. et al. Cell cycle gene regulation dynamics revealed by RNA velocity and
10. Levo, M. et al. Transcriptional coupling of distant regulatory genes in living embryos. deep-learning. Nat. Commun. 13, 2865 (2022).
Nature 605, 754–760 (2022). 37. Waisman, A. et al. Cell cycle dynamics of mouse embryonic stem cells in the ground
11. Hindorff, L. A. et al. Potential etiologic and functional implications of genome-wide state and during transition to formative pluripotency. Sci Rep. 9, 8051 (2019).
association loci for human diseases and traits. Proc. Natl Acad. Sci. USA 106, 9362–9367 38. Beyrouthy, M. J. et al. Identification of G1-regulated genes in normally cycling human
(2009). cells. PLoS ONE 3, e3943 (2008).
12. Shlyueva, D., Stampfel, G. & Stark, A. Transcriptional enhancers: from properties to 39. van Dam, S., Võsa, U., van der Graaf, A., Franke, L. & de Magalhães, J. P. Gene co-expression
genome-wide predictions. Nat. Rev. Genet. 15, 272–286 (2014). analysis for functional classification and gene–disease predictions. Brief. Bioinform. 19,
13. Tippens, N. D. et al. Transcription imparts architecture, function and logic to enhancer units. 575–592 (2017).
Nat. Genet. 52, 1067–1075 (2020). 40. Zhang, Y. et al. Regulation of cell cycle progression by forkhead transcription factor
14. Kwak, H., Fuda, N. J., Core, L. J. & Lis, J. T. Precise maps of RNA polymerase reveal how FOXO3 through its binding partner DNA replication factor Cdt1. Proc. Natl Acad. Sci. USA
promoters direct initiation and pausing. Science 339, 950–953 (2013). 109, 5717–5722 (2012).
15. Kolb, H. C., Finn, M. G. & Sharpless, K. B. Click chemistry: diverse chemical function from 41. Whyte, W. A. et al. Master transcription factors and mediator establish super-enhancers at
a few good reactions. Angew. Chem. Int. Ed. 40, 2004–2021 (2001). key cell identity genes. Cell 153, 307–319 (2013).
16. Core, L. J. et al. Defining the status of RNA polymerase at promoters. Cell Rep. 2, 1025–1035 42. Ohtsuka, M., Inoko, H., Kulski, J. K. & Yoshimura, S. Major histocompatibility complex
(2012). (Mhc) class Ib gene duplications, organization and expression patterns in mouse strain
17. Shah, S. et al. Dynamics and spatial genomics of the nascent transcriptome by intron C57BL/6. BMC Genomics 9, 178 (2008).
seqFISH. Cell 174, 363–376.e16 (2018). 43. Agrawal, P. et al. Genome editing demonstrates that the −5 kb Nanog enhancer regulates
18. Levsky, J. M., Shenoy, S. M., Pezo, R. C. & Singer, R. H. Single-cell gene expression profiling. Nanog expression by modulating RNAPII initiation and/or recruitment. J. Biol. Chem. 296,
Science 297, 836–840 (2002). 100189 (2021).
19. Femino, A. M., Fay, F. S., Fogarty, K. & Singer, R. H. Visualization of single RNA transcripts 44. Tesar, P. J. et al. New cell lines from mouse epiblast share defining features with human
in situ. Science 280, 585–590 (1998). embryonic stem cells. Nature 448, 196–199 (2007).
20. Erhard, F. et al. scSLAM-seq reveals core features of transcription dynamics in single cells. 45. Li, Y. et al. CRISPR reveals a distal super-enhancer required for Sox2 expression in mouse
Nature 571, 419–423 (2019). embryonic stem cells. PLoS ONE 9, e114485 (2014).
21. Muse, G. W. et al. RNA polymerase is poised for activation across the genome. Nat. Genet. 46. Xie, L. et al. A dynamic interplay of enhancer elements regulates Klf4 expression in naive
39, 1507–1511 (2007). pluripotency. Genes Dev. 31, 1795–1808 (2017).
22. Deng, Q., Ramsköld, D., Reinius, B. & Sandberg, R. Single-cell RNA-seq reveals dynamic, 47. Moorthy, S. D. et al. Enhancers and super-enhancers have an equivalent regulatory role in
random monoallelic gene expression in mammalian cells. Science 343, 193–196 (2014). embryonic stem cells through regulation of single or multiple genes. Genome Res. 27,
23. Jonkers, I., Kwak, H. & Lis, J. T. Genome-wide dynamics of Pol II elongation and its interplay 246–258 (2017).
with promoter proximal pausing, chromatin, and exons. eLife 3, e02407 (2014). 48. Mahat, D. B. et al. Base-pair-resolution genome-wide mapping of active RNA polymerases
24. Suter, D. M. et al. Mammalian genes are transcribed with widely different bursting kinetics. using precision nuclear run-on (PRO-seq). Nat. Protoc. 11, 1455–1476 (2016).
Science 332, 472–474 (2011). 49. Habib, N. et al. Div-Seq: single-nucleus RNA-seq reveals dynamics of rare adult newborn
25. Ramalingam, V., Natarajan, M., Johnston, J. & Zeitlinger, J. TATA and paused promoters neurons. Science 353, 925–928 (2016).
active in differentiated tissues have distinct expression characteristics. Mol. Syst. Biol. 17,
e9866 (2021). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
26. Pimmett, V. L. et al. Quantitative imaging of transcription in living Drosophila embryos published maps and institutional affiliations.
reveals the impact of core promoter motifs on promoter state dynamics. Nat. Commun.
12, 4504 (2021). Open Access This article is licensed under a Creative Commons Attribution
27. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based approach for 4.0 International License, which permits use, sharing, adaptation, distribution
interpreting genome-wide expression profiles. Proc. Natl Acad. Sci. USA 102, 15545–15550 and reproduction in any medium or format, as long as you give appropriate
(2005). credit to the original author(s) and the source, provide a link to the Creative Commons licence,
28. Xie, X. et al. Systematic discovery of regulatory motifs in human promoters and 3′ UTRs and indicate if changes were made. The images or other third party material in this article are
by comparison of several mammals. Nature 434, 338–345 (2005). included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
29. Patange, S. et al. MYC amplifies gene expression through global changes in transcription to the material. If material is not included in the article’s Creative Commons licence and your
factor dynamics. Cell Rep. 38, 110292 (2022). intended use is not permitted by statutory regulation or exceeds the permitted use, you will
30. Ochiai, H. et al. Genome-wide kinetic properties of transcriptional bursting in mouse need to obtain permission directly from the copyright holder. To view a copy of this licence,
embryonic stem cells. Sci. Adv. 6, eaaz6699 (2020). visit http://creativecommons.org/licenses/by/4.0/.
31. Whitfield, M. L. et al. Identification of genes periodically expressed in the human cell
cycle and their expression in tumors. Mol. Biol. Cell 13, 1977–2000 (2002). © The Author(s) 2024
8 | Nature | www.nature.com
Methods To achieve single-nucleotide resolution of transcribing polymer-
ases and efficient RT, we identified two click-chemistry-compatible,
scGRO–seq conceptualization chain-terminating nucleotides with a relatively small functional group:
Capturing nascent RNA with sufficient efficiency from single cells for 3′-(O-propargyl)-ATP and 3′-azido-3′-dATP (Extended Data Fig. 1a). Nas-
meaningful analysis was deemed challenging. However, recognizing cent RNA labelled with 3′-(O-propargyl)-NTPs forms a 1,4-disubstituted
the potential insights into transcription mechanisms that single-cell 1,2,3-triazole junction with azide-labelled DNA through CuAAC, as
nascent RNA sequencing could offer, we set out to develop a single-cell shown in Click-Code-Seq50, whereas nascent RNA labelled with 3′-azido-
version of the GRO–seq method a decade after its use in cell popula- 3′-dNTPs forms a slightly bulkier junction with dibenzocyclooctyne
tions. Our efforts were met with two significant challenges: selectively labelled DNA through strain-promoted alkyne-azide cycloadditions
capturing a small fraction of nascent RNA among various RNA spe- (Extended Data Fig. 1b). Nuclear run-on with 3′-(O-propargyl)-ATP
cies within a cell and accurately distinguishing nascent RNAs from and CuAAC showed superior efficiency compared with 3′-azido-
individual cells. 3′-dATP and strain-promoted alkyne-azide cycloadditions (Extended
The primary limitation we encountered was capture efficiency. The Data Fig. 1c).
quantity of nascent RNA from transcribing RNA polymerases in an To convert the clicked RNA–DNA conjugate to cDNA, we tested eight
individual cell, mainly due to the intermittent nature of transcription different reverse transcriptase enzymes, varied the temperature and
with short bursts and long latency periods, is significantly lower than duration of RT and evaluated three TSOs (Extended Data Fig. 1d–f,
the mRNA copies that accumulate over time. Traditional nascent RNA some results not shown). Our optimized method, which we AGTuC, was
capture methods yield only a meagre number of nascent RNAs from then performed in 5 million mouse ES cell nuclei. AGTuC nascent RNA
single cells. Miniaturizing GRO–seq using strategies derived from profiles closely resembled PRO–seq profiles (Extended Data Fig. 2a)
scRNA-seq was not feasible because nascent RNA lacks the consen- and exhibited strong correlations at both gene and enhancer levels
sus polyadenylation sequence used in RNA-seq. Instead, GRO–seq (Extended Data Fig. 2b,c). Notably, the AGTuC library protocol involved
and related methods selectively label nascent RNA in bulk cells using significantly fewer steps than PRO–seq and could be completed in a sin-
modified nucleotides and use single-stranded RNA–RNA ligation with gle day (Extended Data Fig. 2d). AGTuC is a simpler, faster and cheaper
PCR handles on both ends. This ligation process proved unsuitable for alternative to GRO–seq and PRO–seq for nascent RNA sequencing
scGRO–seq owing to its low efficiency and the need for nascent RNA from cell populations.
purification before ligation, which risks depleting the already scarce
nascent RNA from single cells. Development of inAGTuC
To overcome these challenges, we devised a strategy that involved To adapt CuAAC-mediated nascent RNA sequencing to single cells, we
labelling nascent RNA in cells and attaching single-cell barcodes to explored the feasibility of performing AGTuC in single cells. Implement-
the labelled nascent RNA without requiring purification from other ing AGTuC at the single-cell level presented challenges as the nuclear
cellular RNA. After exploring several approaches without success, run-on reaction with 0.5% sarkosyl disrupts the nuclear membrane
we turned to click chemistry, specifically CuAAC. We speculated that before cell barcodes could be attached during the post-run-on CuAAC
by sourcing or synthesizing CuAAC-compatible chain-terminating step, which leads to unintended mixing of nascent RNA from different
nucleotide triphosphate analogues and performing nuclear run-on cells. One potential solution was to perform AGTuC in single tubes,
with the modified nucleotides to selectively label nascent RNA, we which would prevent nascent RNA mixing. However, this approach
could label nascent RNA from individual cells with 5′-AzScBc DNA with requires RNA purification after the run-on reaction, but purification
a PCR handle. Then, we could pool the barcoded nascent RNA from results in further depletion of exceedingly low amounts of nascent
multiple cells for selective RT in the presence of a TSO and subsequent RNA in single cells. Alternatively, omitting RNA purification would
PCR amplification for sequencing. lead to an abundance of 3′-(O-propargyl)-NTPs supplied in excess
To successfully implement this strategy, we identified three important during the run-on reaction, which could outcompete 5′-AzScBc DNA
biochemical hurdles to address. First, we needed to demonstrate the during CuAAC.
ability of native RNA polymerase to incorporate 3′-(O-propargyl)-NTPs To address this challenge, we developed inAGTuC, a new strategy
during nuclear run-on reactions. Second, preserving the intactness of that enables labelling nascent RNA with 3′-(O-propargyl)-NTPs while
nuclei during the run-on reaction was essential to enable the separa- preserving nuclear integrity. This approach overcomes the issues
tion of individual nuclei for single-cell barcoding. Finally, we had to associated with nascent RNA mixing before single-cell barcoding. We
confirm the ability of reverse transcriptase to traverse the triazole proposed that performing the run-on reaction without disrupting
ring junction formed during CuAAC. Successful resolution of the first the nuclear membrane would facilitate the easy removal of excess
and third hurdles would pave the way for CuAAC-based nascent RNA nucleotides through a few centrifugation and resuspension steps
sequencing in cell populations, whereas overcoming the second hurdle while retaining propargyl-labelled nascent RNA within the nuclei. This
would establish the foundation for scGRO–seq. approach would produce clean nuclei with labelled nascent RNA, free
from excess reactive nucleotides, which could be compartmentalized
Development of AGTuC with 5′-AzScBc DNA for CuAAC. We could minimize further RNA loss
To develop a nascent RNA tagging method suitable for capturing a small by pooling and processing the single-cell-barcoded nascent RNA from
fraction of RNA from single cells, we initiated our approach by focusing multiple cells.
on a cell-population-based strategy. We aimed to develop an enhanced To achieve an efficient run-on reaction, PRO–seq and AGTuC disrupt
nascent RNA tagging method that optimally integrates selective label- the polymerase complex with 0.5% sarkosyl detergent, of which nuclear
ling and single-cell barcode tagging, bypassing the need for RNA puri- membrane lysis is collateral damage. We sought to identify the lowest
fication. Among the tested methods, we identified click chemistry as sarkosyl concentration that maintains nuclear membrane integrity
the most suitable option because of its high selectivity, efficiency, while maximizing run-on efficiency and found that a 20× reduction in
robustness in diverse experimental conditions, cost-effectiveness and sarkosyl concentration preserved nuclear intactness, with only a 20%
speed. Our goal was to selectively label nascent RNA through a nuclear reduction in run-on efficiency (Extended Data Fig. 3a,b). To maximize
run-on reaction, conjugate a single-stranded DNA PCR handle (that the capture efficiency of nascent RNA, we optimized the molecular
can accommodate a single-cell barcode for future use in single-cell crowding effect of PEG 8000 and the ratio of Cu(I) to the CuAAC accel-
analysis), reverse transcribe the RNA–DNA conjugate and prepare a erating ligand BTTAA (Extended Data Fig. 3c). Although a low sarko-
NGS library. syl concentration preserves nuclear integrity, it also retains the RNA
Article
polymerase complex intact, thereby shielding the propargyl-labelled 5′ iodo-dT was synthesized through solid-support phosphoramidite
3′ end of nascent RNA from reacting with 5′-AzScBc DNA. We investi- oligonucleotide synthesis, and subsequent replacement of the iodo
gated nascent RNA release from the RNA polymerase complex using group with an azide group was achieved through a reaction with sodium
common denaturants and found that 6 M urea and TRIzol was efficient azide at 60 °C for 1 h. The sequences of three different 5′-AzScBc DNA
(Extended Data Fig. 3d). However, the denaturant in TRIzol hindered are available in Supplementary Table 7.
CuAAC reaction (Extended Data Fig. 3e). Notably, urea also offered The hairpin structure of the 86-nucleotide 5′-AzScBc DNA (Supple-
the added benefit of retaining the RNA–DNA conjugate in the aqueous mentary Fig. 3a) is formed through self-folding. The RT process is initi-
phase during TRIzol clean-up to remove PEG 8000 from the CuAAC ated using the 3′ end of the oligonucleotide, which serves as a built-in
reaction (Extended Data Fig. 3f). For reaction clean-up, we assessed vari- primer. This design ensures a 1:1 stoichiometry between the PCR handle
ous methods, finding cellulose membrane to be effective in removing and the RT primer, minimizing mispriming and nonspecific amplifica-
CuAAC reagents (Extended Data Fig. 3g), whereas silica matrix columns tion during RT. The folded hairpin structure also generates a restriction
performed well in retaining RNA and ssDNA (Extended Data Fig. 3h). site for the EagI enzyme, which is digested before PCR amplification.
Subsequently, we evaluated DNA polymerase for library preparation Undesired extension by reverse transcriptase is effectively prevented
and DNA size-selection methods (Extended Data Fig. 3i,j). by a three-carbon spacer at the 3′ end of the 43-nucleotide 5′-AzScBc
Considering the goal of working with single cells, we performed DNA52. This version of the azide adaptor harbours a 5-nucleotide ACAGG
inAGTuC with cell numbers between 5 million used in AGTuC and 1 cell sequence after the azide-dT at its 5′ end (Supplementary Fig. 3b). Dur-
planned for scGRO–seq. Specifically, we placed 100 to 1,000 intact ing RT, the extension of primers annealing to unclicked 5′-AzScBc, the
nuclei in each well of a 96-well plate containing urea. Nascent RNA in addition of non-templated CCC and the incorporation of TSO results
each well was barcoded with a unique 5′-AzScBc DNA by CuAAC and in undesired cDNA that are preferred substrates for PCR amplifica-
pooled from the 96 wells, and a sequencing library was prepared as in tion. If unaddressed, these amplicons can overwhelm the sequencing
AGTuC. The inAGTuC libraries exhibited similar profiles in gene bodies library. The ACAGG sequence plays a crucial role in depleting these
compared with PRO–seq and AGTuC. However, they could not capture PCR amplicons.
the paused peaks at the 5′ end of genes and enhancers (Extended Data A previously described method named DASH uses recombinant Cas9
Fig. 4a–c). This observation is consistent with the need for a higher protein and gRNA complex to digest and deplete undesired dsDNA53.
sarkosyl concentration for efficient run-on of paused polymerase com- The ACAGG sequence is necessary to generate a gRNA target sequence
plexes. The four inAGTuC libraries correlated well with each other in the undesired PCR amplicons (underlined sequence). In PCR ampli-
(Extended Data Fig. 4d), with the potential to discover more insights cons formed between nascent RNA and 5′-AzScBc DNA, the comple-
with deeper sequencing (Extended Data Fig. 4e,f). Despite only partially mentation of gRNA is interrupted by the presence of a nascent RNA
capturing nascent RNA from a paused complex, the inAGTuC libraries sequence, which makes the desired products incompatible with DASH.
correlated well with those from AGTuC and PRO–seq (Extended Data AGG serves as the protospacer adjacent motif.
Fig. 4g).
To systematically characterize the compatibility of inAGTuC with Cell line
even fewer cells, we prepared four inAGTuC libraries in a 96-well plate, The V6.5 mouse ES cells used in this study were established by the Jae-
with 12 c.p.w., 120 c.p.w. and 1,200 c.p.w., which is roughly equivalent nisch Laboratory (Whitehead Institute, Massachusetts Institute of
to 1,000, 10,000 and 100,000 nuclei, respectively. We also included a Technology) from the inner cell mass of a 3.5-day-old mouse embryo
1,200 c.p.w. plate, omitting Cu(I) as a negative control. Despite lower from a C57BL/6(F) × 129/sv(M) cross.
coverage, the inAGTuC library with 12 c.p.w. (total of about 1,000 cells)
successfully captured the overall nascent RNA profile. It exhibited Cell culture
a good correlation with 120 c.p.w. (total of about 10,000 cells) and Mouse ES cells were cultured in Dulbecco’s modified Eagle medium
1,200 c.p.w. (total of around 100,000 cells) (Extended Data Fig. 5a–c). (Gibco, 11995), plus 10% fetal bovine serum (HyClone, SH30070.03),
supplemented with 1× penicillin–streptomycin (Gibco, 15140), 1×
3′-(O-propargyl)-nucleotide synthesis non-essential amino acids (Gibco, 1140), 1× l-glutamine (Gibco, 25030),
For this study, several CuAAC-compatible nucleotide analogues modi- 1× β-mercaptoethanol (Sigma, M6250) and 1,000 U ml–1 leukaemia
fied with azide or alkyne functionalities were evaluated. Ultimately, inhibitory factor (Sigma, ESG1107) on tissue-culture-treated 10 cm
3′-(O-propargyl)-NTPs were selected for three main reasons: (1) these plates (Corning, CLS430167) pre-coated with 0.2% gelatin (Sigma,
analogues lack 3′ hydroxyl groups, making them chain-terminating and G1890) prepared in PBS (Fisher, MT21031CV). Cells were grown at 37 °C
enabling single-nucleotide resolution of the 3′ end of nascent RNA; (2) and 5% CO and passed with HEPES buffered saline solution (Lonza,
2
the CuAAC reaction produces a compact junction due to the presence CC-5024) and 0.25% trypsin-EDTA (Gibco, 25200) when 70% confluency
of a single carbon bond between the sugar group of the nucleotide and was reached (every 2 days).
the propargyl group at the 3′ end position; and (3) they are relatively
cost-effective compared with biotin-modified nucleotides commonly Sample preparation
used in PRO–seq. Tissue culture cells were prepared for nuclear run-on reaction by either
3′-(O-Propargyl)-ATP (NU-945) was offered by Jena Biosciences. nuclei isolation or cell permeabilization as described below. All centrifu-
To complete the set, custom synthesis requests were made for gation steps were performed at 1,000g for 5 min. Cells were collected
3′-(O-propargyl)-CTP (NU-947), 3′-(O-propargyl)-GTP (NU-946) and by removing the tissue culture medium, rinsing with PBS and placing
3′-(O-propargyl)-UTP (NU-948), all of which are now available for pur- the plates on ice. Cells were scraped while still on ice. The cells were
chase from Jena Biosciences. collected into a 15 ml conical tube and centrifuged at 1,000g for 5 min.
For nuclei isolation, the pellet was resuspended in ice-cold dounc-
Single-cell barcoded DNA adaptors ing buffer (10 mM Tris-Cl pH 7.4, 300 mM sucrose, 3 mM CaCl, 2 mM
2
During scGRO–seq development, 3 sets of 96 5′-AzScBc DNA were syn- MgCl, 0.1% Triton X-100, 0.5 mM DTT, 0.1× Halt protease inhibitor and
2
thesized by GeneLink. Each design encompassed four components: a 0.02 U µl–1 RNase inhibitor) and transferred to a 7 ml dounce homog-
5′ azide positioned at the 5′ terminus, a 10–12 nucleotide sequence for enizer (Wheaton, 357542). After incubation on ice for 5 min, the cells
the single-cell barcode, a 4–6 nucleotide sequence for the UMI and a were dounced 25 times with a tight pestle, transferred back to the 15 ml
PCR handle. The 5′ azide modification was obtained following a previ- conical tube and centrifuged to pellet the nuclei. The pellet was washed
ously described method51. Specifically, an oligonucleotide containing twice in a douncing buffer.
For cell permeabilization, the pellet was resuspended in ice-cold template switching (Thermo Fisher, EP0751). RT reaction (1× RT buffer,
permeabilization buffer (10 mM Tris-Cl pH 7.4, 300 mM sucrose, 10 mM 0.5 mM dNTPs, 0.8 U µl–1 RNase inhibitor, 16% PEG 8000, 1 µM RT primer
KCl, 5 mM MgCl, 1 mM EGTA, 0.05% Tween-20, 0.1% NP-40, 0.5 mM (except for hairpin-forming 5′-AzScBc DNA), and 1 µm TSO) was incu-
2
DTT, 0.1× Halt protease inhibitor and 0.02 U µl–1 RNase inhibitor). After bated with the RNA–DNA conjugate for 2 h at 50 °C. The cDNA was
incubation on ice for 5 min, the cells were centrifuged to pellet the size-selected in 10% denaturing PAGE away from the unclicked 5′-AzScBc
nuclei. The pellet was washed twice in the permeabilization buffer. DNA and empty cDNA formed between the 5′-AzScBc DNA and TSO.
The washed pellet was resuspended in storage buffer (10 mM Tris-Cl The purified cDNA was PCR amplified for 6 cycles to generate dsDNA
pH 8.0, 5% glycerol, 5 mM MgCl, 0.1 mM EDTA, 5 mM DTT, 1× Halt pro- with NEBNext Ultra II Q5 High-Fidelity 2× master mix (NEB, M0544)
2
tease inhibitor and 0.2 U µl–1 RNase inhibitor) at a concentration of and 0.5 µM PCR primers with unique dual index using the PCR cycles
5 × 106 nuclei per 50 µl of storage buffer, flash-frozen in liquid nitrogen presented in Supplementary Table 8.
and stored at −80 °C. The nuclei and permeabilized cells in the storage
buffer can be stored for up to 5 years at −80 °C, making them readily Removal of empty adaptors using DASH
available for nuclear run-on experiments. The dsDNA from the pre-amplification of cDNA was subjected to
DASH to remove the undesired amplicons formed by RT of unclicked
Nuclear run-on with 3′-(O-propargyl)-nucleotides 5′-AzScBc DNA and TSO, as described above. Cas9–gRNA complex
A volume of 50 µl of 2× nuclear run-on buffer (20 mM Tris-Cl (6.6 µM Streptococcus pyogenes Cas9 nuclease (NEB, M0386T),
pH 8.0, 10 mM MgCl, 400 mM KCl, 50 µM 3′-(O-propargyl)-ATP, 20 µM gRNA, 1× NEBuffer r3.1 and nuclease-free duplex buffer
2
50 µM 3′-(O-propargyl)-CTP, 50 µM 3′-(O-propargyl)-GTP, 50 µM (IDT, 11-05-01-04)) was prepared by incubation for 15 min at 25 °C.
3′-(O-propargyl)-UTP, 0.05% Sarkosyl, 1 mM DTT, 2× Halt protease The incubated complex was added to the cleaned PCR reaction and
inhibitor and 0.4 U µl–1 RNase inhibitor) was prepared per sample and incubated for 1 h at 37 °C.
heated to 37 °C. Once thawed from −80 °C, permeabilized cells or nuclei
were added to the heated tube containing nuclear run-on buffer and PCR amplification and NGS
incubated for 5 min at 37 °C with gentle tapping at the incubation mid- The DASHed library was PCR amplified with NEBNext Ultra II Q5
point. Permeabilized cells or nuclei were centrifuged at 500g for 2 min High-Fidelity 2× master mix (NEB, M0544) and 0.5 µM PCR primers
at 4 °C, and the supernatant was aspirated off. The pellet was washed with a unique dual index using the two-step PCR cycles presented in
3 times in 150 µl resuspension buffer (5 mM Tris-Cl pH 8.0, 2.5% glyc- Supplementary Table 9.
erol, 2.5 mM MgAc, 0.05 mM EDTA, 1.25 mM MgCl, 60 mM KCl, 3 mM The NGS library was sequenced on Illumina NovaSeq SP100 flow
2 2
DTT, 0.2× Halt protease inhibitor and 0.2 U µl–1 RNase inhibitor). After cells with 64 nucleotides forward read, 43 nucleotides reverse read, 8
the final wash, the permeabilized cells or nuclei were resuspended in nucleotides index 1 and 8 nucleotides index 2.
a 2 ml resuspension buffer and passed through a 35 µm nylon mesh
(Falcon, 352235). Alignment and pre-processing
Adaptor sequences were removed from paired-end fastq files using Cut-
Single-cell sorting and nuclei sorting adapt54. In brief, the read 1 sequence CCCCTGTCTCTTATACACAT and
For single-cell and nuclei sorting, 96-well plates with 2.5 µl 8 M urea were the read 2 sequence AGATCGGAAGAGCGTCGTGT were trimmed with a
prepared using a multichannel or 96-well pipettor (Avidien MicroPro maximum error rate of 0.15, requiring a minimum overlap of 12 nucleo-
300, 30835029). Single cell and nuclei populations characterized by tides between the read and adapter. The resulting adapter-trimmed
forward and side scattering were sorted by FACS into the 96-well plate reads were demultiplexed using Flexbar55. Cell barcodes and UMIs
containing urea. The sorted plates can be used in CuAAC directly or were extracted from the 5′ end of read 1, applying a barcode error
sealed with aluminium foil or a plastic seal and stored at −80 °C. rate of 0.15 and retaining reads of at least 14 nucleotides in length.
The adapter-clipped and demultiplexed reads were first mapped to
CuAAC the mouse ribosomal genome using bowtie2 (ref. 56) in --very-sensitive
A 96-well plate containing 5′-AzScBc DNA with a unique cell barcode mode. The reads unmapped to the ribosomal genome were mapped
in each well previously synthesized and aliquoted was thawed from to the mouse genome (mm10 build) in --very-sensitive mode. After
−80 °C. Sodium ascorbate, PEG 8000, CuSO and accelerating ligand mapping, duplicate reads were identified and removed utilizing UMI
4
BTTAA were prepared and dispensed into each well of the 96-well and mapping coordinates with UMI-tools57.
plate containing 5′-AzScBc DNA. The CuAAC reaction mix was dis-
pensed into individual wells containing single cells in urea using a Filtering experimental batches and cells
multichannel or 96-well pipette. The final concentration of CuAAC The scGRO–seq batches with r2 values of at least 0.6 against at least 60%
reaction in each well was 30 nM 5′-AzScBc DNA, 800 mM sodium ascor- of all batches were selected for further analysis. Cells were required to
bate, 15% PEG 8000, 1 mM CuSO, 5 mM BTTAA and 2.66 M urea in a contain a minimum of 1,000 UMIs and 750 features for further analysis.
4
7.5 µl volume. The 96-well plates were sealed, vortexed for 10 s in an Our study involved 17 batches of scGRO–seq experiments across 39
orbital vortexer and centrifuged for 1 min at 500g before incubation 96-well plates, encompassing a total of 3,744 cells. Of these, 36 plates
for 2 h at 50 °C. (each containing a minimum of 24 high-quality cells) and 2,635 cells
After incubation, the CuAAC reaction was quenched with 5 mM EDTA met the threshold.
and pooled from 96 wells into a 1.5 ml Eppendorf tube. PEG 8000 was
removed using TRIzol. The remaining CuAAC reagents (sodium ascor- Estimation of capture efficiency
bate, CuSO and BTTAA) were removed with a centrifugal filter with The average capture efficiency of scGRO–seq was estimated to be
4
3 kDa cellulose membrane (Amicon, 2020-04). The purified RNA was approximately 10%. We used data from the intron seqFISH study17,
fragmented with 10 mM ZnCl for 5 min at 65 °C. which quantified the abundance of 34 introns by single-molecule fluo-
2
rescent in-situ hybridization (smFISH). Based on the slope of the line of
RT through the triazole link and pre-amplification best fit between data from smFISH and intron seqFISH, the detection
RT of the clicked RNA–DNA conjugate was performed with highly efficiency of intron seqFISH was estimated to be 44%. When scGRO–
processive Moloney murine leukaemia virus (M-MuLV) reverse tran- seq was compared with intron seqFISH, the detection efficiency of
scriptase lacking RNase H activity but capable of RNA-dependent and scGRO–seq was 26% of intron seqFISH. Based on these two detection
DNA-dependent polymerase activity, non-templated addition and efficiencies, the estimated capture efficiency of scGRO–seq is about
Article
10% (26% of 44% is approximately 10%). This estimate is based on the
8 min of median time required for intron to be spliced out once it is Burst kinetics
transcribed, which ranges from 5 to 10 min according to several stud- Genes over 11 kb (n = 13,564) were selected for studying transcriptional
ies using diverse methods58–64. Thus, the capture efficiency of 10% is an bursting kinetics, and 500 nucleotide regions at both ends known to
average approximation and can vary among cells and batches. harbour paused polymerases were truncated. In cases in which genes
exceeded 10 kb after trimming, they were shortened to 10 kb starting
Enhancer annotation from the initiation site of the gene. With an average transcription rate of
Active transcription regulatory elements (TREs) in mouse ES cells 2.5 kb min–1, this 10 kb burst window served an average burst duration
were identified with PRO–seq data using dREG65. Further filtering of of 4 min. The calculation of burst size and burst frequency proceeded
the dREG results, carried out to eliminate TREs within or proximal to as described below.
1,500 bp of the RefSeq annotated genes (n = 23,980), identified 68,299
high-confidence TREs. The remaining TREs within 500 bp of each other Burst size. For each gene, the number of cells with at least one read
were combined, which resulted in the final list of 12,542 enhancers. To within the 10 kb burst window (number of bursts) was identified, and
capture nascent RNA derived from elongating RNA polymerases at then the average UMIs per burst was computed. If a consistent single
these enhancers, the TREs were extended at least 1500 bp from the TSS read per burst was observed, the burst size of that gene was set to 1. How-
in both directions. The overlapping enhancers were stitched together ever, if the average burst size was 1.2, the residual burst above 1 indicated
after extension. a higher burst size. Accounting for the 10% capture efficiency, wherein
the likelihood of capturing paired reads within a burst window is 1%, the
Transcription unit calling residual burst was proportionally adjusted by the capture efficiency.
groHMM (https://www.bioconductor.org/packages/release/bioc/ The equation for the burst size is shown in Supplementary Fig. 4 (top).
vignettes/groHMM/inst/doc/groHMM.pdf) was used to call de novo
transcription unit on PRO–seq data. All combinations of tuning param- Burst frequency. For each gene, the burst frequency was determined
eters (−50, −100, −200, and −400 for LP and 5, 10, and 15 for UTS) were as the number of bursts per allele (two alleles in autosomal and one in
tested. LP represents the ‘log-transformed transition probability of sex chromosomes) per transcription time. The transcription time was
switching from transcribed state to non-transcribed state’, and UTS calculated as the duration needed to traverse the 10 kb burst window
represents ‘the variance of the emission probability for reads in the with a uniform transcription rate of 2.5 kb min–1, translating to 4 min. The
non-transcribed state’. In our test, −50 LP and 10 UTS performed best calculated burst frequency was normalized by the capture efficiency, tak-
for optimal transcription unit calling. ing the burst size into account. Although burst events with a larger burst
size, like ten, would be consistently detected even with 10% capture effi-
Evidence of bursting ciency, normalization was applied for cases in which a burst size like four
Transcriptional bursting was examined de novo using scGRO–seq data would result in a 60% false negative rate, which indicated a non-existent
by measuring two parameters: the multiplicity of RNA polymerases burst despite active bursting. Thus, burst frequency normalization was
and the distance between the RNA polymerases. The bursting model scaled by burst size to ensure accurate quantification. The equation for
suggests that transcription occurs in short bursts punctuated by the burst frequency is shown in Supplementary Fig. 4 (bottom).
long silent periods, which results in on and off states. The alternative Genes with core promoter elements like TATA and Initiator sequences
model is the relatively uniform transcription initiation by primarily were retrieved from the Eukaryotic Promoter Database (http://epd.
solitary RNA polymerase. We expected two observations under the vital-it.ch)66. Genes containing a pause button, a sequence associated
bursting model. with promoter–proximal paused RNA polymerase, were recovered
First, we expected a higher incidence of more than one RNA polymer- from the CoPRO dataset67.
ase per burst and a concurrent depletion of single RNA polymerases.
To test the evidence of bursting, we selected genes longer than 11 kb Simulation of idealized burst kinetics
(n = 13,564) and trimmed 0.5 kb regions from the 5′ and 3′ ends of the We simulated read counts for populations of single cells to evaluate
gene that are known to harbour paused polymerases. With an average the performance of our estimators for burst rate and size. In the first
transcription rate of 2.5 kb min–1, the remaining 10 kb region resulted simulation, we randomly generated the true burst size (T ) for all
size
in an observation window of 4 min. Based on the evidence of monoal- human genes from a normal distribution (mean = 2, standard devia-
lelic transcription described in the main text and a short observation tion = 3). Similarly, we generated true burst rates (T ) for all human
rate
window of 4 min, we assigned all signals for a gene in individual cells to genes from a normal distribution (mean = 1, standard deviation = 1).
one allele. We quantified the observed incidence of zero, one (singlets) T less than 1 was corrected to 1, and T less than 0.1 burst per hour
size rate
and more than one RNA polymerase (multiplets) per allele. The majority was corrected to 0.1. These parameters were used to simulate UMIs
of alleles had zero polymerase. To calculate the expected incidences per gene per cell as follows:
of RNA polymerases under the non-bursting model, we permuted the 1. For each cell and each gene, a sample from a Poisson distribution
cell identity of scGRO–seq reads 200 times without changing the read with rate parameter λ = T .
rate
positions. The permutation maintains the number of UMIs per cell, 2. Scale the sampled burst by T and round to the nearest integer.
size
breaks the bursting-mediated association between RNA polymerases, 3. After generating molecule counts for all genes and all cells, randomly
and mimics the RNA polymerases distribution under the non-bursting subsample to a specified level (for example, 10% sampling efficiency)
model. We quantified the permuted incidences of zero, singlets and without replacement.
multiplets.
Second, if more than one RNA polymerase is observed in the burst In the second simulation, T and T were taken from our genome-
size rate
window, either due to transcriptional bursting or random chance, we wide estimates described in Fig. 2, and UMIs per gene per cell were
expected the transcription bursting model would result in more closely similarly generated. Simulations were performed ten times to ensure
spaced molecules than expected by the random chance. We took all consistent results.
multiplets in observed or permuted data and calculated the distance
between RNA polymerase molecules within each pair. We binned the Cell cycle analysis
distances in 50 bp bins and calculated the ratio of RNA polymerase Three sets of transcriptionally characterized genes were used to
pairs between the observed and permuted data. characterize the cell cycle phase in individual cells. Transcription of
68 replication-dependent histone genes on chromosome 3, chromo- and sequencing (ChIP–seq) peaks. The precise position was deter-
some 6, chromosome 11 and chromosome 13 were used to determine mined by evaluating the divergent transcription around them. The
the S phase collectively. Transcription of four genes (Orc1, Ccne1, Ccne2 reads from corresponding bins in sense and antisense directions
and Mcm6) were used to assign G1/S phase, and six genes (Wee1, Cdk1, were combined.
Ccnf, Nusap1, Aurka and Ccna2) were used to assign G2/M phase. Cells
with more than a read in one of the genes or reads in more than one CRISPR-validated SEs
gene were hierarchically clustered, which revealed three major clus- A set of validated SEs and their target genes were used from a previ-
ters of the cell-cycle-phase-specific transcription pattern. The other ously published study referenced in the main text. SEs in gene introns
three smaller clusters without distinct transcription patterns were not or associated with miRNA were excluded due to the ambiguity in
considered for downstream analyses. Differentially expressed genes assigning reads and short gene length, respectively. For the time bin
among G1/S, S and G2/M phases of the cell cycle were identified using analyses, genes and SEs were divided into four 5 kb bins (2-min with the
the ‘FindAllFeatures’ function of Seurat68 (single-cell analysis package). 2.5 kb min–1 constant transcription rate of elongating polymerases)
in the sense and antisense direction, limiting the analyses to the first
Gene–gene co-transcription 20 kb. Using a 20 kb region in this analysis yields four 5 kb bins. The TSS
The co-transcription of genes was determined using two criteria: cor- was first determined based on the strongest OCT4, SOX2 and Nanog
relation and permutation. scGRO–seq reads were collected from up to ChIP–seq peaks, and precise position was determined by evaluating the
the first 10 kb of genes after 500 bp regions at both ends were trimmed divergent transcription around them. The reads from corresponding
(n = 15,666). The genes by cells expression matrix was binarized. For the bins in sense and antisense directions were combined. The scrambled
correlation approach, pairwise correlation was performed for all gene random pairs in SE–gene time bin analysis represent the co-transcribed
pairs, and the P value was calculated using the chi-square test. It was bins between SEs and genes that are not the verified pairs.
adjusted for multiple hypothesis tests using the Benjamini–Hochberg
correction method. External data
Permutation was performed by shuffling the cell identifiers of reads Various data types were analysed, compared and benchmarked
while maintaining their gene assignments. The permutation method against this study. PRO–seq data (GSE169044), ChIP data for p300
accounts for several unknown and known biases and, more importantly, (GSM2360934), ATAC–seq (GSE169044), CDK9 (GSM1082347), RNA
maintains the number of reads in each cell. The observed and permuted PolII (GSM318444), H3K4me1 (GSM281695), H3K4me3 (GSM1082344),
co-transcription frequencies of gene pairs were calculated. The empiri- H3K27Ac (GSM594579), OCT4 (GSM1082340), SOX2 (GSM1082341)
cal P value for a gene pair was determined by counting the incidence and Nanog (GSM1082342) were downloaded from the Gene Expres-
of equal or higher co-transcription frequency in 1,000 permutations sion Omnibus database. PRO–seq libraries were prepared using the
compared with the observed co-transcription frequency. same cells used for scGRO–seq under identical conditions70. Intron
Gene pairs with correlation coefficients of greater than 0.1 and seqFISH data on mouse ES cells were downloaded from table S1 of
multiple hypothesis corrected P values of less than 0.05 from the cor- ref. 17. The genes-by-cells intron seqFISH matrix was binarized, and
relation approach and an empirical P value of less than 0.05 from the burst frequency was calculated assuming the signal in each gene comes
permutation approach were considered co-transcribed. A network of from a burst equivalent to the 10 kb region used in scGRO–seq, given
pairwise co-transcribed genes was created using the Leiden algorithm, the probes were designed against the introns at the 5′ regions of genes.
and the modules were selected for gene ontology analyses using the Mouse ES cell scRNA-seq was used from a previous study7, and the burst
clusterProfiler R package. kinetics was downloaded from 41586_2018_836_MOESM5_ESM.xlsx file
associated with this study.
Enhancer–gene co-transcription
Enhancer–gene co-transcription was determined following the logic Reporting summary
of gene–gene co-transcription, substituting genes on one arm with Further information on research design is available in the Nature
enhancers. scGRO–seq reads were collected from up to the first 10 kb Portfolio Reporting Summary linked to this article.
of genes after 500 bp regions at both ends were trimmed, and from
at least a 3 kb region around enhancers (1,500 bp sense and 1,500 bp
Data availability
antisense) after a 500 bp region around the TSS was removed to
avoid paused polymerases. Strand-specific reads on either side of the Sequencing files for scGRO–seq, inAGTuC and AGTuC experiments have
enhancer TSS were combined to determine enhancer expression. The been deposited into the NCBI’s Gene Expression Omnibus database
features (genes + enhancers) by cell expression matrix was binarized, and are accessible through GEO series accession number GSE242176.
and the co-transcribed enhancer–gene pairs were determined using The published datasets used in this study were obtained from the
the correlation and permutation tests, similar to the approach used GEO repository (identifiers GSE169044, GSM2360934, GSM1082347,
in the gene–gene co-transcription calculation. The UMIs per cell are GSM318444, GSM281695, GSM1082344, GSM594579, GSM1082340,
maintained in each permutation. Enhancer–gene pairs only from the GSM1082341 and GSM1082342), supplementary table S1 of ref. 17, and
same chromosomes were retained for downstream analyses. We also 41586_2018_836_MOESM5_ESM.xlsx file of ref. 7.
included non-overlapping SEs identified in mouse ES cells.
Enhancers of pluripotency factors Code availability
Validated enhancers associated with pluripotency transcription fac- The code used in this study is available from GitHub (https://github.
tors OCT4 (also known as POU5F1), SOX2, Nanog and KLF4 were col- com/jaymahat/scGROseq).
lected from studies referenced in the main text. To define time bins
within genes, genes were divided into 5 kb bins (2-min bins calculated 50. Wu, J., McKeague, M. & Sturla, S. J. Nucleotide-resolution genome-wide mapping of
using the 2.5 kb min–1 constant transcription rate of elongating RNA oxidative DNA damage by Click-Code-Seq. J. Am. Chem. Soc. 140, 9783–9787 (2018).
51. Miller, G. P. & Kool, E. T. Versatile 5′-functionalization of oligonucleotides on solid support:
polymerases) in the sense and antisense direction until the end of the amines, azides, thiols, and thioethers via phosphorus chemistry. J. Org. Chem. 69,
transcription wave called by groHMM69, or they overlapped bins from 2404–2410 (2004).
52. Zhou, L., Myers, A. N., Vandersteen, J. G., Wang, L. & Wittwer, C. T. Closed-tube genotyping
other genes. For enhancers, the TSS was first determined based on the
with unlabeled oligonucleotide probes and a saturating DNA dye. Clin. Chem. 50,
strongest OCT4, SOX2 and Nanog chromatin immunoprecipitation 1328–1335 (2004).
Article
53. Gu, W. et al. Depletion of abundant sequences by hybridization (DASH): using Cas9 to 70. Hu, S. et al. Transcription factor antagonism regulates heterogeneity in embryonic stem
remove unwanted high-abundance species in sequencing libraries and molecular cell states. Mol. Cell 82, 4410–4427.e12 (2022).
counting applications. Genome Biol. 17, 2408 (2016).
54. Marcel, M. Cutadapt removes adapter sequences from high-throughput sequencing
reads. EMBnet J. 17, 10–12 (2011). Acknowledgements We are grateful to the current and past members of the Sharp Laboratory,
55. Dodt, M., Roehr, J. T., Ahmed, R. & Dieterich, C. FLEXBAR—flexible barcode and adapter especially to A. Whipple, S. Garg, V. P. Chauhan, G. Shamu, J. Liberman and R. Shah for
processing for next-generation sequencing platforms. Biology 1, 895–905 (2012). discussion and critical review of the manuscript; S. Bose for his help with FACS and A. Bhutkar
56. Langmead, B. & Salzberg, S. L. Fast gapped-read alignment with Bowtie 2. Nat. Methods for his help with computational analyses; and D. Ribeiro and J. Weber for their insight on
9, 357–359 (2012). statistical tests on co-transcriptional measurement. We thank the Koch Institute’s Robert
57. Smith, T., Heger, A. & Sudbery, I. UMI-tools: modeling sequencing errors in unique A. Swanson (1969) Biotechnology Center for technical support, specifically the Flow
molecular identifiers to improve quantification accuracy. Genome Res. 27, 491–499 (2017). Cytometry Facility, for help with FACS; and S. Levine and the staff at BioMicro Center for
58. Audibert, A., Weil, D. & Dautry, F. In vivo kinetics of mRNA splicing and transport in their help with NGS. This work was supported in part by Koch Institute support (core) grant
mammalian cells. Mol. Cell. Biol. 22, 6706–6718 (2002). 5P30-CA014051 from the National Cancer Institute. This work was supported by Program
59. Clement, J. Q., Qian, L., Kaplinsky, N. & Wilkinson, M. F. The stability and fate of a spliced Project grant P01-CA042063 from the NCI (P.A.S.) and by the United States Public Health
intron from vertebrate cells. RNA 5, 206–220 (1999). Service grants R01-GM034277 from the NIH (P.A.S.). The Emerald Foundation Postdoctoral
60. Coulon, A. et al. Kinetic competition during the transcription cycle results in stochastic Transition Award currently supports D.B.M. The Gertrude B. Elion Research Fellowship from
RNA processing. eLife 3, e03939 (2014). GSK and the Ludwig Cancer Institute at MIT previously supported him.
61. Neugebauer, K. M. Nascent RNA and the coordination of splicing with transcription.
Cold Spring Harb. Perspect. Biol. 11, a032227 (2019). Author contributions D.B.M. and P.A.S. conceived the study. D.B.M., S.K.W. and J.F. optimized
62. Rabani, M. et al. Metabolic labeling of RNA uncovers principles of RNA production and click chemistry, library preparation methods and prepared NGS libraries. D.B.M. and N.D.T.
degradation dynamics in mammalian cells. Nat. Biotechnol. 29, 436–442 (2011). analysed the data with the help of S.E.B. on pre-processing and J.D.M.-R. on scRNA-seq analysis.
63. Rabani, M. et al. High-resolution sequencing and modeling identifies distinct dynamic D.B.M. and P.A.S. wrote the manuscript, and all co-authors provided feedback. P.A.S. supervised
RNA regulatory strategies. Cell 159, 1698–1710 (2014). the project.
64. Singh, J. & Padgett, R. A. Rates of in situ transcription and splicing in large human genes.
Nat. Struct. Mol. Biol. 16, 1128–1133 (2009).
Competing interests US patent number US-11519027-B2 on ‘Single-cell RNA sequencing using
65. Danko, C. G. et al. Identification of active transcriptional regulatory elements from
click-chemistry’ was granted on 6 December 2022 to the Massachusetts Institute of Technology,
GRO-seq data. Nat. Methods 12, 433–438 (2015).
Cambridge, MA, USA, on which P.A.S. and D.B.M. are named inventors. The other authors
66. Dreos, R., Ambrosini, G., Groux, R., Cavin Périer, R. & Bucher, P. The eukaryotic promoter
declare no competing interests.
database in its 30th year: focus on non-vertebrate organisms. Nucleic Acids Res. 45,
D51–D55 (2017).
67. Tome, J. M., Tippens, N. D. & Lis, J. T. Single-molecule nascent RNA sequencing identifies Additional information
regulatory domain architecture at promoters and enhancers. Nat. Genet. 322, 1845 (2018). Supplementary information The online version contains supplementary material available at
68. Satija, R., Farrell, J. A., Gennert, D., Schier, A. F. & Regev, A. Spatial reconstruction of https://doi.org/10.1038/s41586-024-07517-7.
single-cell gene expression data. Nat. Biotechnol. 33, 495–502 (2015). Correspondence and requests for materials should be addressed to Phillip A. Sharp.
69. Chae, M., Danko, C. G. & Kraus, W. L. groHMM: a computational tool for identifying Peer review information Nature thanks Matthew Pratt and the other, anonymous, reviewer(s)
unannotated and cell type-specific transcription units from global run-on sequencing for their contribution to the peer review of this work. Peer reviewer reports are available.
data. BMC Bioinformatics 16, 222 (2015). Reprints and permissions information is available at http://www.nature.com/reprints.
Extended Data Fig. 1 | click-chemistry mediated nascent RNA conjugation represents the quantified gel region. d, Relative quantification of reverse
to single-stranded DNA and optimization of reverse transcription. transcription (RT) efficiency of two commercial enzymes traversing through
a, Click-chemistry compatible nucleotides tested in AGTuC development. the triazole link formed between the alkyne-labeled RNA and azide-labeled
A few nucleotide triphosphates were custom synthesized or sourced with few DNA by CuAAC. RT was performed in the presence of either native dCTP or
properties in mind - smaller size, chain termination ability, and the possibility radioisotope a-32P dCTP, and the RT reaction was resolved in denaturing PAGE
of incorporation by native RNA polymerases. b, Structure of the triazole and imaged sequentially for nucleic acid signal (top gel) and radioisotope
linkage formed by CuAAC between the nascent-RNA terminally labeled with signal (bottom gel). e, Quantification of aborted intermediate and completed
3′-(O-Propargyl)-NTPs and the azide-labeled DNA (top left), the linkage formed desired products (RT through triazole and TSO used) formed during the one hour
by SPAAC between the nascent-RNA terminally labeled with 3′-Azido-3′-dNTPs or three hours of RT using TSO with terminal Locked-Nucleic-Acid-Guanosine
and DBCO DNA (right). The phosphodiester linkage in a native oligonucleotide (LG) or 2′-Fluoro-Guanosine (FG). f, Confirmation and relative quantification of
is shown for comparison (bottom left). c, Incorporation efficiency of CuAAC, RT, and PCR of clicked product formed between the alkyne-labeled RNA
3′-(O-Propargyl)-ATP or 3′-Azido-3′-dATP by native RNA polymerase in nuclear and azide-labeled DNA by three commercial Reverse transcriptase enzymes.
run-on reaction. The propargyl or azide labeled nascent RNA is clicked with Note: The blue bar, line, or border represents the “winner” condition.
Cy5 via CuAAC (Azide-Cy5 or Alkyne-Cy5) or SPAAC (DBCO-Cy5), resolved Polyacrylamide gel electrophoresis for c, d, and f was repeated at least twice
in a denaturing polyacrylamide gel electrophoresis (PAGE), and quantified with the addition or subtraction of some conditions presented here. For gel
by measuring the Cy5 fluorescent from the gel image. The blue dotted line source data, see Supplementary Fig. 1.
