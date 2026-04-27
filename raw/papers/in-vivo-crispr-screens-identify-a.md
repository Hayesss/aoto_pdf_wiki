---
source_path: /mnt/c/Users/Administrator/Zotero/storage/U7VRTDI3/Su 等 - 2024 - In vivo CRISPR screens identify a dual function of MEN1 in regulating tumor–microenvironment interac.pdf
ingested: 2026-04-23
sha256: 188e62eb8c1aa60c
---

nature genetics
Article https://doi.org/10.1038/s41588-024-01874-9
In vivo CRISPR screens identify a
dual function of MEN1 in regulating
tumor–microenvironment interactions
Received: 10 November 2023 Peiran Su1,2,13, Yin Liu3,13, Tianyi Chen2,13, Yibo Xue2, Yong Zeng 2,
Guanghui Zhu 2,12, Sujun Chen 2,12, Mona Teng1,2, Xinpei Ci2, Mengdi Guo2,4,
Accepted: 18 July 2024
Michael Y. He 2, Jun Hao 2, Vivian Chu1,2, Wenxi Xu2, Shiyan Wang2,5,
Published online: 3 September 2024 Parinaz Mehdipour 6, Xin Xu 2, Sajid A. Marhon 2, Fraser Soares 2,
Nhu-An Pham 2, Bell Xi Wu1,2, Peter Hyunwuk Her1,2, Shengrui Feng1,2,
Check for updates Najd Alshamlan2, Maryam Khalil2,7, Rehna Krishnan2, Fangyou Yu3,
Chang Chen 8, Francis Burrows9, Razqallah Hakem1,2, Mathieu Lupien1,2,
Shane Harding1,2, Benjamin H. Lok1,2, Catherine O’Brien1,2, Alejandro Berlin 2,
Daniel D. De Carvalho1,2, David G. Brooks2,4, Daniel Schramek 10,11,
Ming-Sound Tsao 1,2,7 & Housheng Hansen He 1,2
Functional genomic screens in two-dimensional cell culture models
are limited in identifying therapeutic targets that influence the tumor
microenvironment. By comparing targeted CRISPR–Cas9 screens in a
two-dimensional culture with xenografts derived from the same cell
line, we identified MEN1 as the top hit that confers differential dropout
effects in vitro and in vivo. MEN1 knockout in multiple solid cancer types
does not impact cell proliferation in vitro but significantly promotes or
inhibits tumor growth in immunodeficient or immunocompetent mice,
respectively. Mechanistically, MEN1 knockout redistributes MLL1 chromatin
occupancy, increasing H3K4me3 at repetitive genomic regions, activating
double-stranded RNA expression and increasing neutrophil and CD8+ T cell
infiltration in immunodeficient and immunocompetent mice, respectively.
Pharmacological inhibition of the menin–MLL interaction reduces tumor
growth in a CD8+ T cell-dependent manner. These findings reveal tumor
microenvironment-dependent oncogenic and tumor-suppressive functions
of MEN1 and provide a rationale for targeting MEN1 in solid cancers.
Tumor masses are mixtures of cancerous and normal cells that cancer management5,6. Indeed, in recent years, an increasing number of
collectively form the tumor microenvironment (TME)1. Within the TME, studies has focused on targeting components of the TME, particularly
various cell populations communicate through cytokines, chemokines the immune microenvironment7,8.
and growth factors, further recruiting additional infiltrating cells, The CRISPR screen is a powerful tool to identify vulnerabilities
leading to increased tumor heterogeneity2–4. Advances in single-cell in cancer cells9,10. Although CRISPR screens have been extensively
RNA sequencing (scRNA-seq) technology allow for the characteriza- conducted in in vitro cell culture systems11–13, including the Cancer
tion of individual components within the TME, offering significant Dependency Map (DepMap) project14–16, the absence of the TME in these
opportunities to enhance our understanding of tumor biology and models has limited the ability to identify gene targets that modulate
A full list of affiliations appears at the end of the paper. e-mail: Ming.Tsao@uhn.ca; hansenhe@uhnresearch.ca
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1890
Article https://doi.org/10.1038/s41588-024-01874-9
interactions between tumor and the TME. A few recent studies of in vivo (Extended Data Fig. 1g,h and Supplementary Table 2). Twenty-two
CRISPR screens have identified targets that regulate immunotherapy dropout genes were found to be common to both screens (Supplemen-
resistance, highlighting the feasibility and significance of functional tary Table 2), including DepMap core essential genes POLE and POLE2
genomic screens in the context of physiologic TME12,17,18. (ref. 23). Although no significantly enriched genes were found in vitro,
In this study, we set out to identify modulators of the tumor–TME 40 were found in the in vivo screens (Extended Data Fig. 1g,h and Sup-
interactions. By directly comparing parallel in vitro and in vivo CRISPR plementary Table 2). To further identify genes that confer differential
screens, we identified MEN1 as the top candidate gene that confers essentialities in vitro and in vivo, we used MAGeCK to compare the D21
differential effects in cell culture versus xenograft tumors. We found cell culture and xenograft tumor screens directly. This analysis identi-
that MEN1 knockout resulted in increased tumor growth in immuno- fied 12 in vivo specific dropout genes and 13 enriched genes (Fig. 1b and
deficient mice but decreased growth in immunocompetent mice, Supplementary Table 2). Among these genes, the top hit, MEN1, which
revealing both TME-dependent oncogenic and tumor-suppressive encodes menin, is of particular interest. Genetic loss of MEN1 drives
functions. Our findings underscore the effectiveness of in vivo func- tumorigenesis in multiple solid cancer types. However, the depend-
tional genomic screens in identifying clinically relevant drug targets ency score of MEN1 from DepMap showed that it is not an enriched
and provide a rationale for the therapeutic targeting of MEN1, either gene in in vitro screens for 953 of 954 cell lines from solid tumor types
alone or in combination with immunotherapy, in multiple solid and (Extended Data Fig. 1i). The in vivo specific enrichment in A549 suggests
hematologic cancer types. that MEN1 may function through regulating tumor–TME interactions.
Results MEN1 regulates cytokine genes both in vitro and in vivo
Parallel in vitro and in vivo CRISPR screens in lung cancer To validate our findings, we designed two sgRNAs for MEN1 deletion
The number of cells that can be injected in mice to form xenograft (Extended Data Fig. 2a). Tumor growth significantly increased with
tumors is limited. Therefore, we designed a targeted single guide both MEN1 knockout sgRNAs (Fig. 1c). By contrast, no obvious effect on
RNA (sgRNA) library to ensure sufficient coverage of each sgRNAs in colony formation or cell proliferation was observed in 2D cultures upon
an in vivo screen. This library, referred to as Epi-Drug19,20, comprises genetic ablation of MEN1 (Fig. 1d and Extended Data Fig. 2b). These data
12,472 sgRNAs targeting 317 epigenetic regulators and 657 DrugBank further confirm the in vivo restricted function of MEN1 in this context.
targets, with an average of 10 sgRNAs per gene (Extended Data Fig. 1a To investigate the mechanisms underlying the function of MEN1,
and Supplementary Table 1). A549 lung adenocarcinoma (LUAD) cells we conducted RNA sequencing (RNA-seq) in 2D cultured A549 cells
with stable Cas9 expression were transduced with the sgRNA library with and without MEN1 knockout. Differential gene analysis using
and cultured in Petri dishes for 3 days with puromycin selection (D0). DESeq2 (ref. 24) identified 357 upregulated and 252 downregulated
Subsequently, the transduced cells were split into equal aliquots for genes on MEN1 knockout (P ≤ 0.01 and abs(log(fold change)) > 1;
adj 2
either Petri dish culture or establishing xenograft tumors via subcu- Extended Data Fig. 2c). Kyoto Encyclopedia of Genes and Genomes
taneous injection into immunodeficient NOD scid gamma (NSG) mice (KEGG) pathway analysis revealed ‘cytokine–cytokine receptor inter-
(Fig. 1a). Two-dimensional (2D) cultured cells and xenograft tumors action’ as the most significantly enriched pathway in the upregu-
were collected at day 21 (D21) for DNA extraction and next-generation lated genes (Fig. 1e, Extended Data Fig. 2d and Supplementary
sequencing (NGS). Table 3). Although a smaller number of differential genes were identi-
We observed high overall sgRNA coverages, with 99.98% and fied in xenograft tumors (Extended Data Fig. 2e), likely because of the
97.49% of the 12,472 sgRNAs detected in D21 cultured cells and xeno- heterogeneity of tumor samples, ‘cytokine–cytokine receptor inter-
graft tumors, respectively (Extended Data Fig. 1b). Xenograft tumors action’ remained the top enriched pathway in the upregulated genes
demonstrated greater variation in sgRNA representation compared (Fig. 1f and Supplementary Table 3). Quantitative real-time polymer-
with cultured cells (Extended Data Fig. 1c,d), consistent with a previ- ase chain reaction with reverse transcription (RT–qPCR) analysis of
ous report21. In both the in vitro and in vivo screens, MAGeCK22 analysis representative genes in the ‘cytokine–cytokine receptor interaction’
revealed significantly higher dropout rates for the positive control signature, including CXCL1, IL33, CXCL8 and IL1B, showed marked upreg-
genes (Mann–Whitney U-test; P = 2.10 × 10−21), compared with nega- ulation upon MEN1 depletion in A549 and NCI-H1792, an additional
tive controls (Extended Data Fig. 1e,f), suggesting the high efficacy human LUAD cell line (Fig. 1g and Extended Data Fig. 2f,g). Notably,
of the screens. through reanalysis of five RNA-seq datasets from recent publications
We then applied MAGeCK to identify genes with sgRNAs that were on MEN1 functions25–29, we consistently observed cytokine-related
depleted or enriched in D21 compared with D0 (referred to as dropout signatures as top enriched terms in response to MEN1 perturbation in
and enriched genes hereafter). This led to the identification of 47 four of the datasets, utilizing both cancer cell line and patient-derived
and 72 dropout genes in the in vitro and in vivo screens, respectively xenograft (PDX) models (Extended Data Fig. 3a–d).
Fig. 1 | Parallel in vivo and in vitro CRISPR screens in A549 and in vivo analysis of differential genes in MEN1 knockout versus control A549 cells in vitro
specific function of MEN1 in lung cancer. a, Schematic representation of the (e) and in vivo (f). The x axis represents the number of genes. Wald tests defined
CRISPR screen experiment design. A549 cells with stable Cas9 expression were in DEseq2 were used to calculate P values. g, RT–qPCR showing the expression
transduced with Epi-Drug sgRNA library and selected with puromycin for 3 days of representative cytokine-related genes in MEN1 knockout A549 cells relative
(D0). Parallel in vitro and in vivo screens were performed for 3 weeks (D21). to control. Housekeeping gene TBP was used as a control. Mean ± s.e.m. of three
Samples were collected for PCR amplification and NGS. b, Dropout (genes with biological replicates is shown (unpaired two-tailed Student’s t-test). h, KEGG
sgRNA reduced in D21; blue dots) and enriched (genes with sgRNA increased in analysis of differential genes in MEN1-low versus MEN1-high patients from the
D21; red dots) genes in LUAD A549 xenograft compared with A549 2D cultured TCGA LUAD cohort. Wald tests defined in DEseq2 were used to calculate
cells. The P values of positive and negative selections and log(fold change) were P values. i, Boxplot showing the abundance of representative cytokine genes in
2
defined and calculated using MAGeCK. MEN1 is the top ranked enriched gene. MEN1-high versus MEN1-low patient tumors in the TCGA LUAD cohort. Twenty
c, Xenograft tumor growth curve in immunodeficient mice inoculated with patients with the highest and the lowest MEN1 expression were assigned to
control (sgCtrl) or MEN1 knockout (sgMEN1-1, sgMEN1-2) A549 cells. Each data each group. Horizontal lines in the box represent the upper quartile, median
point represents mean ± s.e.m. tumor volumes (n = 5 in sgCtrl, sgMEN1-1 and and lower quartile from top to bottom. Vertical extending lines mark the 5th to
sgMEN1-2 groups). Two-way ANOVA was used for the growth curves. *P < 0.05, 95th percentile (unpaired two-tailed Student’s t-test). *P < 0.05, **P < 0.01.
**P < 0.01. d, Colony formation of A549 cells with (sgMEN1) and without (sgCtrl) IgA, immunoglobulin A; IL, interleukin; P , adjusted P value; Rep, replicate.
adj
knockout of MEN1. Cells were seeded in six-well plates in duplicate and allowed a, Created with BioRender.com.
to grow for 8 days before staining with crystal violet. Scale bars, 7 mm. e,f, KEGG
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1891
Article https://doi.org/10.1038/s41588-024-01874-9
a
sgRNA library virus
Cell line screen
(~12,500 sgRNAs)
Lentiviral
infection
A549 cells Cells after NGS mouse screen
expressing Cas9 selection
(D0) –log 4 3 –4
10(negative
2
P val
1
ue) 0 6
–6
–log (positive P value)
10
c
e
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1892
log2(fold
change)
b
6
MEN1
UBE2A 4
EHMT1 RY J B U P N E M ED SL2L A E R O ID 1 4B TBL1X GABRA2 KLKB1 2
UBE2USLC7A11
ALPPL2
0
GGCX MTR
F S T A R A S C D P K J 1 1 O 3 C 3 H N R 0 2 A C 1 3 YT C H R D M D C K C R 3 4 M 1 H 1 1 –2
1 2 3 4 5
A549 xenograft growth d
2,000
1,500
1,000
500
0
0 10 20 30 40 50
Time (days)
)3mm(
emulov
romuT
sgCtrl
sgMEN1-1
sgMEN1-2
**
*
Enriched pathways in A549 cell line f Enriched pathways in A549 xenograft g
50
Cytokine–cytokine Cytokine–cytokine receptor interaction receptor interaction 30
P P 10
NOD-like receptor adj adj
signaling pathway 6 4 × × 1 1 0 0 – – 4 4 IL-17 signaling pathway 0 0 . . 1 2 5 0
IL-17 signaling pathway 2 × 10–4 Viral protein interaction with 0 0 . . 1 0 0 5 cytokine and cytokine receptor 5
Rheumatoid arthritis Hematopoietic cell lineage
Amoebiasis Rheumatoid arthritis 0
14 16 23 2 4 9 C X
CL1 IL33
C X
CL8 IL1B TBP
noisserpxe
evitaleR
A549 cytokine gene expression
*
sgCtrl
**
sgMEN1-1 sgMEN1-2
* ** ** * * *
h Enriched pathways in TCGA MEN1 low versus high
10,000
Cytokine−cytokine receptor interaction
Intestinal immune network 7,500
for IgA production P
adj
Viral protein interaction with 5,000
cytokine and cytokine receptor 1 × 10–4
2 × 10–4
Malaria 2,500
3 × 10–4
Inflammatory bowel disease
0
0 20 40 60
IL33 IL1B
C X
CL1
C X
CL8
2qeSED
stnuoc
dezilamron
sgCtrl sgMEN1-1 sgMEN1-2
i Cytokines expression in TCGA LUAD
**
** Type
MEN1 high
MEN1 low
*
**
1
peR
2
peR
13 15 19 3 5
Gene number Gene number
Article https://doi.org/10.1038/s41588-024-01874-9
We extended the gene expression analysis to patient tumors in H3K4me3 peak regions, and 55.6% of MLL1 binding overlap with these
The Cancer Genome Atlas (TCGA) LUAD RNA-seq dataset, contrasting regions (Supplementary Fig. 1c,d). Differential binding analysis using
the top and bottom 10% of patients based on MEN1 mRNA abundance MACS2 bdgdiff identified 1,857 regions with increased MLL1 binding
(Extended Data Fig. 3e). In concordance with our observations in the and H3K4me3 signal, and 1,017 regions with decreased signal, in MEN1
A549 cell line, KEGG analysis identified ‘cytokine–cytokine recep- knockout cells (Fig. 2d and Supplementary Fig. 1e–g).
tor interaction’ as the top enriched term in the upregulated genes in BETA indicated that the differential binding sites of H3K4me3
MEN1-low patients (Fig. 1h,i, Extended Data Fig. 3f,g and Supplementary were not enriched near the upregulated genes upon MEN1 knockout
Table 4). These results suggest that MEN1 regulates the expression of (Supplementary Fig. 1h), suggesting an indirect mechanism of regula-
cytokine-related genes in cell lines, PDX models and patient tumors. tion. Although the majority of the MLL1 binding sites were shorter than
500 bp and enriched in the promoter regions, we observed regions in
MEN1 loss leads to MLL1 chromatin redistribution the genome with strong binding intensities that exceeded 2 kb (Supple-
Given that menin is a scaffolding protein involved in epigenetic regula- mentary Fig. 1g). Because MACS is designed to identify short peaks, we
tion30, we conducted a genome-wide cleavage under targets and release used CREAM software to identify broad peaks35. This led to the identifi-
using nuclease (CUT&RUN)31 assay to determine menin chromatin bind- cation of 422 broad regions ranging from 2 kb to 8 Mbp, most of which
ing in A549 cells. The efficiency and specificity of the menin antibody harbor repetitive elements and showed increased MLL1 occupancy upon
was confirmed by immunoprecipitation and western blot analysis, as MEN1 knockout (Extended Data Fig. 5a and Supplementary Table 5).
well as by chromatin immunoprecipitation–quantitative PCR (ChIP– To determine whether loss of MEN1 led to altered transcription
qPCR) analysis of representative menin binding regions (Extended Data of repetitive elements, we reanalyzed the A549 RNA-seq data by map-
Fig. 4a,b, left). A total of 26,507 menin chromatin binding sites were ping the reads to repetitive genomic regions. Differential expression
identified using MACS32 (Extended Data Fig. 4c,d and Supplementary analysis identified 2,737 repeat loci with upregulated expression, and
Table 5). Binding and Expression Target Analysis (BETA)33 revealed 865 repeat loci with downregulated expression (Fig. 2e). Most of the
that although genes whose expression decreased upon menin deple- upregulated loci contained short interspersed nuclear elements(SINE),
tion were significantly associated with menin binding, no enrichment long interspersed nuclear elements (LINE) and simple repeats, with 740
was observed for upregulated genes, including the cytokine-related of 2,737 located in the 442 CREAM peak regions (Fig. 2f and Extended
genes (Fig. 2a). Similar trends were obtained when applying BETA to Data Fig. 5b,c). Furthermore, the genomic regions with elevated MLL1
differentially expressed genes in MEN1-low compared with MEN1-high and H3K4me3 signals following MEN1 depletion were significantly
subjects from the TCGA LUAD cohort (Extended Data Fig. 4e). These enriched in proximity to upregulated repeats, whereas the decreased
data suggest that the regulation of cytokine-related genes is not directly ones were not (Fig. 2g and Extended Data Fig. 5d). ChIP–qPCR analysis
controlled by cis-regulation of menin. of representative repeat regions showed that, whereas the binding of
Menin is known to interact with MLL1 to regulate target gene menin, UTX and H3K27me3 diminished upon MEN1 depletion, there
expression. Silencing of MLL1 expression with two separate small was a substantial increase in MLL1 binding and H3K4me3 signal at these
interfering RNAs in A549 wild-type cells resulted in significant reduc- repeat regions (Extended Data Fig. 5e–i).
tions in CXCL1, IL33, CXCL8 and IL1B (Fig. 2b). Unlike MLL1, silencing Transcripts from repetitive genomic regions tend to form double-
of other methyltransferases or subunits within the MLL or DOT1L1 stranded RNA, such as inverted Alu repeat (Extended Data Fig. 5j).
complexes29,34, including MLL2, MLL3/4, UTX and DOT1L, did not con- A significant induction of dsRNA staining was observed in MEN1
sistently activate the cytokine genes tested (Extended Data Fig. 4f–i). knockout compared with control A549 cells (Fig. 2h,i and Extended
These data collectively suggest that menin-mediated regulation of Data Fig. 5k, left). Transcription from repetitive genomic regions has
these cytokine genes predominantly relies on MLL1. Indeed, induction been reported to induce DNA damage36. Indeed, significantly higher
of these cytokines in MEN1 knockout cells was completely attenuated DNA damage, as indicated by stronger γ-H2AX staining, was observed
by silencing of MLL1 (Fig. 2c). upon MEN1 knockout (Fig. 2j and Extended Data Fig. 5k (right)). dsRNA
We next expanded the CUT&RUN analysis to MLL1 in A549 cells expression is known to induce interferon signaling. MEN1-low sub-
with and without knockout of MEN1 (Extended Data Fig. 4a,b, right). jects in the TCGA LUAD cohort demonstrated a significantly higher
We identified more than 10,000 MLL1 chromatin binding sites in the level of interferon signaling genes compared with MEN1-high patients
control condition, with 68% overlapping with those of menin (Extended (Extended Data Fig. 5l). Furthermore, MEN1 knockout significantly
Data Fig. 4d (right), Supplementary Fig. 1a and Supplementary Table 5). induced the expression of ISG15 and IRF7 (Extended Data Fig. 5m).
Because MLL1 is a H3K4-specific methyltransferase, we extended our Together, these data suggest that MEN1 knockout increases MLL1
analysis to H3K4me3 histone modification (Supplementary Fig. 1b). occupancy at repetitive genomic regions, leading to the activation of
H3K4me3 ChIP-seq in A549 cells identified approximately 30,000 dsRNA transcription.
Fig. 2 | MEN1 regulates MLL1 binding at repetitive genomic regions and upregulated upon MEN1 knockout. Background are randomly selected repeat
transcription of dsRNA. a, Correlation between menin binding sites and regions that did not show differential expression upon MEN1 knockout.
target gene expression as evaluated by software BETA. b, RT–qPCR showing the The P value was calculated by one-sided paired t-test. h, Northern dot blot
abundance of representative cytokine-related genes with and without siRNA showing dsRNA staining in control and MEN1 knockout A549 xenograft tumors.
silencing of MLL1 in A549 cells. Housekeeping gene TBP was used as a control. The upper panel demonstrates dsRNA staining using the J2 antibody, and the
Mean ± s.e.m. of two biological replicates is shown (unpaired two-tailed Student’s lower panel illustrates staining of total RNA, serving as a loading control. The
t-test). *P < 0.05, **P < 0.01, ***P < 0.001. c, RT–qPCR performed in A549 cells with experiment was conducted using four biological replicates for each condition.
and without MEN1 deletion coupled with siRNA silencing of MLL1. Mean ± s.e.m. i, Immunofluorescence imaging of control (sgCtrl) or MEN1 knockout (sgMEN1-1,
of four biological replicates is shown (unpaired two-tailed Student’s t-test). sgMEN1-2) A549 cells or A549 cells treated with poly(I:C) for the detection
**P < 0.01, ***P < 0.001, ****P < 0.0001. d, Pileup plots showing H3K4me3 of dsRNA (red). Red, dsRNA (J2 antibody); blue, DAPI. Scale bars, 20 μm.
ChIP-seq and MLL1 CUT&RUN signal at 1,857 increased peak regions called by j, Immunofluorescence imaging of γ-H2AX of control or MEN1 knockout
MACS2 bdgdiff. e, Heatmap showing repeat loci with differential expression in A549 cells or A549 cells. Green, γ-H2AX (γ-H2AX-antibody); blue, DAPI. Scale
MEN1 knockout and control A549 cells in 2D culture. f, Donut plot showing the bars, 20 μm. ERV, endogenous retroviruses; ERVL, endogenous retroviral-like
categories of upregulated repeats in MEN1 knockout A549 cells. g, Number of elements; hAT, hobo, Ac and Tam3; LTR, long terminal repeat; MaLR, mammalian
upregulated repeats within a given distance of the 1,857 peaks with increased apparent LTR-retrotransposons; TcMAR, Tc1/mariner .
H3K4me3 and MLL binding. Up-repeats are repeats that are significantly
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1893
Article https://doi.org/10.1038/s41588-024-01874-9
MEN1 regulates tumor growth depending on mammalian Silencing of MAVS or cGAS/STING significantly attenuated the induc-
apparent retroviral-like vesicles (MAVS) and cyclic GMP-AMP tion of cytokines in MEN1 knockout cells (Fig. 3a and Extended Data
synthase (cGAS)–stimulator of interferon genes (STING) Fig. 6a). In addition, MEN1 knockout resulted in induction of p-TBK1 in
dsRNA can induce a viral mimicry response via the RIG-1/MDA5-MAVS MEN1 knockout compared with control cells, whereas total TBK1 levels
RNA sensing pathway or cGAS–cGAMP STING reverse-transcribed DNA remained unchanged (Extended Data Fig. 6b).
sensing pathway37–39, with Phosphorylation of TBK1 (p-TBK1) serving In vivo analysis showed that MAVS or cGAS knockout in control
as an indicator of MAVS and/or cGAS–STING pathway activation40. cells had no noticeable effect on tumor growth (Extended Data Fig. 6c),
b A549 siMLL1
1.5
1.0
0.5
0
TBP MLL1
C X
CL1 IL33
C X
CL8 IL1B
d
j
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1894
noisserpxe
evitaleR
siNC 60 sgCtrl
siMLL1-1
sgMEN1
siMLL1-2 40
6 sgMEN1 + * siMLL1 ** 4
**
*** 2
**** ***** ****
0
TBP MLL1
C X
CL1 IL33
C X
CL8 IL1B
noisserpxe
evitaleR
c A549 sgMEN1 + siMLL1
****
100
80 **** 60 ****
40
**
20 *** ****
**** **** **** **** 0
0 4,000 8,000 12,000 Rank of genes based on
regulatory potential score
noitcarf
evitalumuC )%( seneg
fo
a Menin activating/repressive
function prediction
Static (background)
Upregulate (0.772) Downregulate (6.24 × 10–33)
e Differential repeats in A549
H3K4me3 MLL1 10 Samples
20 sgCtrl
0.8 sgCtrl sgCtrl 5
sgMEN1-1 sgMEN1-1 sgMEN1
0
al 0.6 sgMEN1-2 15 sgMEN1-2
g n −5
si RepeatsType
a g e 0.4 10 −10 DNA
er LINE
v
A 0.2 LTR/ERV
5
Others
0 0 Simple-repeat
–3.0 kb Center 3.0 kb –1.0 kb Center 1.0 kb
SINE
f DNA/TcMar− g
Tigger Up-repeats number to
2.76% up-H3K4me3 distance
LTR/ERVL−MaLR O 9. t 7 h 4 e % rs 250
3.12% SINE/Alu 200
30.95% DNA/hAT
−Charlie 150
4.67% LINE/L2
10.06%
100
LINE/L1 Simple
50 10.42% repeat
SINE/MIR 14.66% 13.62% 0
0 20 40 60 80 100
Distance (kb)
i
rebmun
taepeR
Up-repeats
Background
Paired t-test
P value = 0.0009078
IPAD
ANRsd
degreM
sgCtrl Poly I:C sgMEN1-1 sgMEN1-2
XA2H-γ
sgCtrl sgMEN1-1 sgMEN1-2
IPAD
degreM
h
A) sgCtrl
N
R s d
2 ( sgMEN1-1 nti-J
A
sgMEN1-2
sgCtrl
A N
al R sgMEN1-1 ot
T
sgMEN1-2
Article https://doi.org/10.1038/s41588-024-01874-9
a b
1,000
800
600
400
200
0
0 10 20 30
Time (days)
c d e
Positive regulation of
leukocyte chemotaxis
Monocyte chemotaxis
log(OR)
2
Myeloid leukocyte migration
1
2
Leukocyte migration 4
Regulation of vasculature
development
0.01 10–2.8 10–2.9 ≤10–3
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1895
)3mm(
emulov
romuT
sgCtrl
sgMEN1
sgMEN1 + cGAS
sgMEN1 + MAVS ***
**** **** ****
sgMEN1 + cGAS + MAVS
8
6
4
2
0
sg
Ctrl
ME
N1-1
ME
N1-2
sg sg
egatnecreP
***
***
800
600
400
200
0
0 10 20 30
Time (days)
)3mm(
emulov
romuT
f g
Anti-menin Anti-myeloperoxidase Anti-CD8
sgCtrl + IgG
sgCtrl + anti-Ly6G
sgMEN1 + IgG
sgMEN1 + Ly6G ****
****
hgih-1NEM
wol-1NEM
120
100
15
10
5
0
TBP
C X
CL1 IL33
C X
CL8 IL1B
noisserpxe
evitaleR
sgLacZ
sgMEN1
**
sgMEN1 +
cGAS
sgMEN1 +
MAVS
sgMEN1 +
MAVS +
** cGAS
*
** *
** ** *
*** ** ** ** *
CD8+ T cell in TMA
50
40
30
20
10
0
ME
N1-high
ME
N1-lo w
egatnecreP
Neutrophil in TMA
30
20
10
0
ME
N1-high
ME
N1-lo w
egatnecreP
A549 sgMEN1 + sgcGAS + sgMAVS A549 sgMEN1 + sgMAVS + sgcGAS xenograft growth
Enriched pathways (mouse genes) A549 xenograft neutrophil
A549 xenograft neutrophil neutralization
Fig. 3 | Antagonizing function of MEN1 and MLL1 in regulating cytokine without MEN1 deletion. Mean ± s.e.m. of neutrophil percentage from 12 tumors is
gene signature and TME infiltration. a, RT–qPCR performed in A549 cells shown (unpaired two-tailed Student’s t-test). e, IHC staining showing percentage
with and without MEN1 deletion coupled with deletion of MAVS and/or cGAS. of neutrophil or CD8+ T cells in MEN1-high versus MEN1-low tumor samples from
Mean ± s.e.m. of two biological replicates is shown (unpaired two-tailed a LUAD microarray (TMA). Mean ± s.e.m. of 20 tumors with the highest and the
Student’s t-test). *P < 0.05, **P < 0.01. b, A549 xenograft tumor growth rate in lowest MEN1 TMA scores were assigned to each group. **P < 0.01, ***P < 0.001.
immunodeficient mice with and without knockout of MEN1 or in combination f, Representative IHC staining images for MEN1, myeloperoxidase (neutrophil)
with MAVS and/or cGAS knockout. Each data point represents mean ± s.e.m. and CD8 (CD8+ T cell). Scale bars, 200 μm. g, A549 xenograft tumor growth rate
tumor volumes (n = 10 for each arm). Two-way ANOVA was used for statistical in immunodeficient mice with and without knockout of MEN1 or in combination
analysis. ***P < 0.001, ****P < 0.0001. c, Dot plot showing enriched KEGG with anti-Ly6G antibody injection. Each data point represents mean ± s.e.m.
terms of mouse differential genes from MEN1 knockout A549 xenografts. tumor volumes (n = 5 for each arm). Two-way ANOVA was used for statistical
d, Quantification of neutrophil infiltration in A549 xenograft tumors with and analysis. OR, odds ratio.
Article https://doi.org/10.1038/s41588-024-01874-9
but significantly reduced the induction of tumor growth in the MEN1 compared with control conditions (Fig. 4f). Pathway analysis revealed
knockout condition (Fig. 3b). These data suggest that MEN1 regulates activation of antiviral immune response pathways in Men1-deficient
cytokine-related genes and tumor growth through a MAVS- and cGAS– tumors (Fig. 4g and Extended Data Fig. 8f,g), indicating increased
STING-dependent viral mimicry mechanism. tumor immunogenicity. Cytokine-related genes with high expression
levels in the MEN1-low colon cancer patient tumors were highly upregu-
MEN1 knockout induces neutrophil infiltration lated in Men1-deficient tumors of CT26, HKP1 and DKO (Extended Data
To determine whether and how MEN1 knockout modulates TME cell Fig. 8h,i). The strong enrichment of virus response-related signatures
infiltration and interaction with tumor cells, we identified reads that further supports the role of Men1 in suppressing viral mimicry, as
specifically mapped to the mouse genome in the A549 xenograft tumor observed in A549 cells. Indeed, Men1 knockout exhibited strong upreg-
RNA-seq data. Differential gene and KEGG pathway analysis revealed ulation of dsRNA species compared with control CT26 cells (Fig. 4h,i).
a strong enrichment of terms related to leukocyte function in genes
upregulated in MEN1 knockout tumors (Fig. 3c and Extended Data Men1 knockout increases CD8+ T cell infiltration
Fig. 6d). Pathway analysis further demonstrated that the function of To systematically investigate the TME populations affected by
neutrophils, a subtype of leukocytes, is enriched in MEN1 knockout Men1 knockout, we conducted scRNA-seq and mass cytometry by
conditions (Extended Data Fig. 6e). time-of-flight (CyTOF) analysis of Men1-proficient and -deficient CT26
Immunohistochemistry (IHC) staining of anti-myeloperoxidase, tumors grown in immunocompetent mice (Extended Data Fig. 9a),
a marker for neutrophil, revealed profound induction of neutrophil using standard data processing and quality control procedures42,43.
infiltration in MEN1 knockout tumors compared with controls (Fig. 3d Analysis of transcriptomic profiles of 7,595 cells identified 7 cell types
and Extended Data Fig. 6f). In addition, reanalysis of a publicly available with 16 distinct sub-clusters (Fig. 5a, Extended Data Fig. 9b,c and Sup-
RNA-seq dataset of leukemia xenograft tumors41 revealed that menin plementary Fig. 2). The proportion of macrophages and T cells sig-
inhibition induces cytokine gene expression and neutrophil infiltration nificantly increased in Men1 knockout tumors (Fig. 5b and Extended
in immunodeficient mice (Extended Data Fig. 6g,h). Data Fig. 9d). These data suggest that Men1 knockout impacts immune
To validate immune cell infiltrations in patient tumors, we cell infiltration.
performed IHC staining for neutrophil and CD8+ T cells in a tissue To further characterize the enhanced immune response upon
microarray of the LUAD cohort. Tumors with lower MEN1 expression Men1 knockout in immunocompetent mice, we profiled 606,301 CD45+
indeed exhibited much stronger neutrophil and CD8+ T cell infiltra- immune cells from CT26 tumors with CyTOF using an antibody panel
tion (Fig. 3e,f). Neutrophil neutralization with an antibody against targeting 35 immune markers (Fig. 5c, Extended Data Fig. 9e and Sup-
myeloperoxidase significantly attenuated tumor growth induced plementary Table 6). We observed an overall increase in the percentage
by MEN1 knockout in A549 xenografts (Fig. 3g), indicating that the of immune cells in Men1-deficient tumors (Fig. 5d and Extended Data
tumor-promoting effect of MEN1 knockout is dependent on neutro- Fig. 9f). In addition to the overall increase in CD45+ cells, the rela-
phils. Consistent with this, the percentage neutrophil infiltration in tive composition of the immune cells also changed, with a significant
A549 xenograft tumors significantly increased with MEN1 knockout enrichment of CD8+ T cells, dendritic cells and a subset of macrophages
but was reduced to baseline levels with knockout of cGAS or/and MAVS (Fig. 5d and Extended Data Fig. 9g). To further validate the impact of
(Extended Data Fig. 6i). MEN1 knockout on CD8+ T cells, we established A549 xenografts in
humanized NSG mice, which were reconstituted with a human immune
MEN1 regulates tumor growth in an immune cell-dependent system. MEN1 knockout resulted in significantly reduced tumor growth
manner (Extended Data Fig. 9h), in contrast to the increased tumor growth in
Pan-cancer analysis using the TCGA datasets revealed that the nonhumanized NSG mice (Fig. 1c). IHC staining revealed significantly
‘cytokine–cytokine receptor interaction’ gene signature is significantly increased CD8+ T infiltration in MEN1 knockout tumors compared
higher in MEN1-low compared with MEN1-high patients in 26 of the 32 with control tumors (Extended Data Fig. 9i,j). Similarly, IHC analysis
cancer (sub-)types analyzed (Extended Data Fig. 7a). The number and of CT26 tumors with Men1 depletion also showed increased CD8+ T cell
types of cytokine genes activated varied across different cancer types infiltration (Fig. 5e), findings that are consistent with the scRNA-seq
(Extended Data Fig. 7b). and CyTOF analysis.
Similar to A549 lung cancer cells, knockout of MEN1 in colon cancer
cell line HCT116 did not alter cell proliferation in vitro but significantly Pharmacological inhibition of menin reduces tumor growth
increased tumor growth in immunodeficient NSG mice (Fig. 4a,b and Pharmacologic inhibition of the menin–MLL interaction is an effective
Extended Data Fig. 7c). Next, we extended our analysis to the CT26 treatment in preclinical models and clinical trials of MLL1-rearranged
mouse colon cancer cell line (Fig. 4c). Genetic ablation of Men1 did and NPM1-mutant leukemias44–46. To assess the efficacy of inhibiting
not alter CT26 cell proliferation in vitro but led to significantly faster menin in solid cancer types, we treated CT26 cancer cells with the
tumor growth in immunodeficient NSG mice (Fig. 4d and Extended Data clinical stage menin inhibitor ziftomenib (KO-539)46. In line with the
Fig. 7d,e). Furthermore, significantly higher neutrophil infiltration was Men1 knockout phenotype, we observed a dose-dependent induc-
observed in Men1 knockout tumors compared with controls (Extended tion of representative cytokine genes in CT26 following ziftomenib
Data Fig. 7f). By contrast, loss of Men1 resulted in significantly reduced treatment (Fig. 6a), validating the on-target effect of ziftomenib in
tumor growth in immunocompetent mice (Fig. 4e). A similar effect was these cells. In addition, cGAS or MAVS deletion attenuated ziftomenib
also observed in the syngeneic breast cancer model 4T1, with increased treatment-induced upregulation of cytokine genes (Extended Data
and decreased tumor growth upon Men1 knockout in immunodeficient Fig. 10a). Consistently, ziftomenib treatment also results in an increase
and immunocompetent mice, respectively (Extended Data Fig. 8a,b). in phosphorylated Tbk1 (Extended Data Fig. 10b). Enhanced cytokine
We further extended the Men1 knockout study to pancreatic cancer expression was consistently detected in lung and pancreatic cancer
model HKP1 and prostate cancer model DKO, and consistently observed explant PDX tissues and organoid models following treatment with
decreased tumor growth following Men1 depletion in immunocompe- ziftomenib (Extended Data Fig. 10c–f). To further confirm the effect of
tent mice (Extended Data Fig. 8c–e). ziftomenib on chromatin dynamics, we conducted MLL1 and H3K4me3
To elucidate how the loss of Men1 restricts CT26 tumor growth in ChIP assays in wild-type A549 cells treated with either dimethyl sulfox-
immunocompetent mice, we transcriptionally profiled Men1-proficient ide or ziftomenib. Ziftomenib treatment significantly reduced menin
and -deficient tumors. Differential gene analysis identified 350 upregu- abundance (Extended Data Fig. 10g). ChIP–qPCR analysis validated
lated and 309 downregulated genes, respectively, in the knockout significantly increased MLL1 and H3K4me3 signals at selected repeat
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1896
Article https://doi.org/10.1038/s41588-024-01874-9
Immune-deficient
a NGS mice
Immune-competent
BALB/c mice
e BALB/c CT26 tumor growth
1,500
1,000
500
0
0 5 10 15
Time (days)
g h i
regions tested, consistent with that observed with CRISPR mediated a similar growth inhibitory effect in the syngeneic 4T1 breast cancer
MEN1 depletion (Extended Data Fig. 10h). allograft model in immunocompetent mice (Extended Data Fig. 10i,j).
In concordance with Men1 knockout, drug treatment signifi- A significantly increased tumor growth rate was observed in the pan-
cantly reduced tumor growth compared with the control treatment creatic cancer PDX model OCIP200 in immunodeficient mice follow-
in a dosage-dependent manner (Fig. 6b). Ziftomenib treatment had ing ziftomenib treatment (Extended Data Fig. 10k), consistent with
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1897
)3mm(
emulov
romuT
HCT116 xenograft growth
1,000
600
200
0
0 5 10 15 20 25
Time (days)
Differential CT26 genes
Sample
sgCtrl sgMen1-1
sgMen1-2
2
1
0
–1
–2
)3mm(
emulov
romuT
HCT116 cell proliferation
15 million
10 million
5 million
0
0 5 10 15 20 25
Time (days)
tnuoc
lleC
Enriched pathways (GO) CT26 Men1 KO dsRNA
Defense response 300,000
to virus
Response to virus 200,000
Response to
interferon-beta
100,000
Cellular response to
interferon-beta
Regulation of immune 0 effector process
sg
Ctrl Men1-1 Men1-2
0 10 20 30 40 sg sg
FCTC
d
1,000
500
0
0 5 10 15
Time (days)
**
***
)3mm(
emulov
romuT
b c
NSG CT26 tumor growth
dsRNA DAPI Merge
lrtCgs
1-1neMgs
2-1neMgs
Murine-derived
sgCtrl sgCtrl CT26 tumor
cell line
sgMEN1-1 sgMEN1-1
sgMEN1-2 NS sgMEN1-2
f
sgCtrl sgCtrl
sgMen1-1 sgMen1-1
sgMen1-2 sgMen1-2
Gene number
** **
P
adj 2.72 × 10–31
1.51 × 10–20
3.02 × 10–20
4.54 × 10–20
6.05 × 10–20
*** ***
**
*
Fig. 4 | Immunocompetence-dependent tumor-promoting and -inhibiting arm). Two-way ANOVA was used for statistical analysis. ***P < 0.001. f, Heatmap
function of MEN1 in colon cancer. a, Cell proliferation rate of HCT116 in 2D showing expression value (z-score based on DESeq normalized RNA-seq
cell culture with and without knockout of MEN1. NS, not significant. Each data counts) of differential genes from Men1 knockout versus control tumors in
point represents mean ± s.e.m. cell counts (n = 3 for each arm). Two-way ANOVA immunocompetent mice. Two control samples and four Men1 knockout tumors
was used for statistical analysis. b, HCT116 xenograft tumor growth rate in were subjected to RNA-seq analysis. g, GO analysis of differentially expressed
immunodeficient mice with and without knockout of MEN1. Each data point genes in Men1 knockout versus control cells was performed and the top five
represents mean ± s.e.m. tumor volumes (n = 5 for each arm). Two-way ANOVA terms are shown. The x axis represents the number of genes. Wald tests defined in
was used for statistical analysis. *P < 0.05, **P < 0.01. c, Schematic view of murine DEseq2 were used to calculate P values. h,i, Quantification (h) and representative
CT26 engraftment experiment design. d, Tumor growth in immunodeficient immunofluorescence images (i) of control (sgCtrl) or Men1 knockout (KO)
NSG mice inoculated with control (sgEV) or Men1 knockout (sgMen1-1, sgMen1-2) CT26 cells for the detection of dsRNA. Red signal, dsRNA (J2 antibody); blue
CT26 cells. Each data point represents mean ± s.e.m. tumor volumes (n = 12 signal, DAPI. Scale bars, 20 μm. Each bar in the left-hand panel represents the
for each arm). **P < 0.01. e, Tumor growth in immunocompetent BALB/c mice mean of quantifications from 30 randomly picked fields (unpaired two-tailed
inoculated with control (sgEV) or Men1 knockout (sgMen1-1, sgMen1-2) CT26 Student’s t-test). **P < 0.01, ***P < 0.001. CTCF, corrected total cell fluorescence.
cells. Each data point represents mean ± s.e.m. tumor volumes (n = 5 for each
Article https://doi.org/10.1038/s41588-024-01874-9
a
d
the TME-dependent effects observed with MEN1 genetic depletion. CT26 xenograft tumors and MEN1-low patient tumors in the TCGA
Furthermore, treatment with ziftomenib resulted in a marked increase LUAD cohort (Fig. 6e), likely due to increased immune cell infiltra-
in CD8+ T cell infiltration, with stronger induction observed at a higher tions. scRNA-seq and CyTOF showed that a subset of tumor and
dosage (Fig. 6c). Although CD8+ T cell neutralization alone had no macrophage cells express PD-L1, and the CD8+ T cells express high
obvious effect on tumor growth in the control condition, it com- levels of PD-1, with a modest increase in the knockout tumors (Sup-
pletely abolished the tumor-suppressive effect of ziftomenib (Fig. 6d), plementary Fig. 3a–e). Ziftomenib or anti-PD-1 treatment alone
suggesting that MEN1 regulation of tumor growth depends on CD8+ substantially reduced the CT26 tumor growth and the combination
T cells and that menin blockade might constitute a new immunothera- demonstrated a significantly stronger effect (Fig. 6f). These data sug-
peutic approach. gest that pharmacological inhibition of menin alone or in combination
Bulk RNA-seq showed significantly higher levels of Cd274/PD-L1 with immunotherapy may benefit patients with functional menin
and a trend of increased Pdcd1/PD-1 expression in Men1-depleted protein (Fig. 6g).
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1898
sllec
T
+8DC
b
T cell
in CT26 tumors
10
8
6 4
2
0
sg
Ctrl
sg
Men1
c
e sgCtrl sgMen1-1 sgMen1-2
egatnecreP
Macrophage
in CT26 tumors
* 25
20
15 10
5
0
sg
Ctrl
sg
Men1
egatnecreP
*
5 *
4
3
2
1
0
sg
Ctrl
sg
Men1
egatnecreP
CD8+ T cells in all
live cells
30
20
10
0
sg
Ctrl
sg
Men1
egatnecreP
CD45+ cells in all
live cells
*
15 ***
**
10
5
0
sg
Ctrl Men1-1 Men1-2
sg sg
egatnecreP
15 12
10
13
8 11 5 2
9
0 0
15 7 4 6 10 5 14 1
–5 3
–10 0 10
UMAP 1
CD8+ T cell in CT26 tumors
2 PAMU
Myofibroblast
Mast cell
NK cell Tumor cells CD4 T cell CD8
B/Plasma cell
M1
M2
Macrophage
11
5
5 29 25
26 15
21 1 3
0 13
1720 18
6 9
23 4 –5
2 10 14 27
24 16
–10 12 7
22
–10 –5 0 5 10
UMAP 1
200 µm 200 µm 200 µm
2
PAMU
0 8
1 9
2 10 3 11 4 12 5 13
6 14
7 15
DC
monoDC
Monocyte 1 16 2 17
3019 3 18 4 19
Neutrophil 8 5 20 6 21
Eosinophil 7 22
M1 M2 8 23
Macrophage 9 24 Unknown 10 25 T cell 11 26 reg 12 27
CD8 T cell 13 28 28 14 29
CD4 15 30
T cell NK cell
Fig. 5 | scRNA-seq, CyTOF and IHC analysis confirmed increased immune cell of CD45+ cells (left) and CD8+ T cells (right) of live cells captured by CyTOF.
infiltration in Men1 knockout CT26 tumors. a, UMAP view of 7,595 single cells Mean ± s.e.m. of four biological replicates (sgCtrl) for control and six biological
from scRNA-seq profiling of CT26 tumors with and without depletion of Men1, replicates for Men1 knockout (sgMen1) are shown (unpaired two-tailed Student’s
color coded by assigned clusters. Dotted circles mark cell types as determined t-test). e, Representative IHC images (left) and quantifications (right) showing
by relevant marker genes. b, Percentages of T cells and macrophages in control the abundance of CD8+ T cells in control (sgCtrl) and Men1 knockout (sgMen1-1,
(sgCtrl) and Men1 knockout (sgMen1-1, sgMen1-2) CT26 tumor samples. sgMen1-2) CT26 tumors. Mean ± s.e.m. of quantifications from 10 tumor IHC
Mean ± s.e.m. of two to four biological replicates are shown (unpaired two-tailed sections are shown (unpaired two-tailed Student’s t-test). **P < 0.01, ***P < 0.001.
Student’s t-test). *P < 0.05 c, UMAP view of 606,301 single cells from CyTOF Scale bars, 200 μm. DC, dendritic cells; NK cell, natural killer cell.
profiling of 10 CT26 tumors with and without depletion of Men1. d, Percentage
Article https://doi.org/10.1038/s41588-024-01874-9
350
80
25
20
15
10
5
0
Il33 Cxcl1 0 Cxcl9 Cd4 0 Ccl4 Tbp
Discussion interactions. We found that the epigenetic regulator MEN1 markedly
Tumors develop within a complex microenvironment and identify- influences tumor growth under certain conditions in vivo, but does
ing clinically relevant therapeutic targets amid such complexity is a not affect cell growth in vitro.
daunting task. In this study, we used parallel in vitro and in vivo CRISPR MEN1 plays a complex multifaceted role in cancer. It is a well-
knockout screens to identify genes that modulate tumor and TME characterized tumor suppressor, loss of which causes multiple
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1899
noisserpxe
evitaleR
a b CT26 ziftomenib treatment
CT26 ziftomenib treatment 1,000
**
DMSO
* 500 nM 800
1,000 nM
*
**
600
400
*
* 200
* ** ** **
0
0 4 8 12
Time (days)
c d
e f
g
MLL1 Menin mRNA Tumor promoting
Neutrophils
+
Increased tumor
burden
Immunodeficient
TME
Menin
MLL1
+ dsRNA Cytokines
com
Im
pe
m
te
u
n
n
t
o
T
-
ME
Decreased tumor
burden
MAVS
+ +
cGAS–STING Tumor inhibiting
CD8+ T cells
)3mm(
emulov
romuT
Vehicle
Ziftomenib (100 mg kg–1)
Ziftomenib (150 mg kg–1)
1,500
1,000
500
0 0 4 8 13 Time (days)
)3mm(
emulov
romuT
CT26 anti-CD8 and ziftomenib treatment
Vehicle + IgG
Vehicle + anti-CD8
Ziftomenib + IgG
Ziftomenib + anti-CD8 ****
1,500
1,000
500
0
0 5 8 13
Time (days)
)3mm(
emulov
romuT
CT26 anti-PD1 and ziftomenib treatment
Vehicle + IgG
Vehicle + anti-PD1 Ziftomenib + IgG
Ziftomenib + anti-PD1
****
**
Cd274/PD-L1 level
in CT26
4,000
3,000
2,000
1,000
0
sg
Ctrl Men1-1 Men1-2
sg sg
dezilamron
qeSED
stnuoc
daer
CD274/PD-L1 level in
TCGA COAD
400 *
** 300
200
100
0
ME
N1
high
ME
N1
lo
w
dezilamron
qeSED
stnuoc
daer
CT26 ziftomenib
treatment
30
20
10
0
Veh Z ( i 1 c i 0 f l t e 0 o m m e g n k ib g– Z ( 1 1 i ) 5 ft 0 o m m e g n k ib g–1)
***
egatnecreP
Anti-CD8
***
*
binemotfiZ
binemotfiZ
)1–gk
gm
001(
)1–gk
gm 051(
elciheV
**
****
Article https://doi.org/10.1038/s41588-024-01874-9
Fig. 6 | Pharmacological inhibition of MEN1 reduces tumor growth in a CD8+ e, Relative abundance of Cd274/PD-L1 in CT26 tumors with and without deletion
T cell-dependent manner and demonstrates additive effect with anti-PD-1 of Men1 from bulk RNA-seq data (left). Mean ± s.e.m. of two biological replicates
treatment. a, RT–qPCR showing the relative expression of cytokine-related are shown (unpaired two-tailed Student’s t-test). Relative abundance of CD274/
genes in CT26 cells treated with different dosages of menin inhibitor ziftomenib. PD-L1 in MEN1-high and MEN1-low patient tumors in the TCGA COAD cohort
Mean ± s.e.m. of two biological replicates are shown (unpaired two-tailed (right). Mean ± s.e.m. of 50 patient tumors with the highest and the lowest MEN1
Student’s t-test). b, CT26 tumor growth with vehicle control or ziftomenib expression were shown (unpaired two-tailed Student’s t-test). *P < 0.05, **P < 0.01,
treatment at dosages of 100 and 150 mg kg−1. Each data point represents ***P < 0.001. f, Tumor growth rate in immunocompetent mice inoculated with
mean ± s.e.m. tumor volumes (n = 5 for each arm). Two-way ANOVA was used CT26 cells following IgG or PD-1 antibody treatment in combination with vehicle
for statistical analysis. *P < 0.05, **P < 0.01, ***P < 0.001. c, Representative IHC control or ziftomenib (150 mg kg−1). Each data point represents mean ± s.e.m.
images (left) and quantifications (right) showing the infiltration of CD8+ T tumor volumes (n = 10 in each group). **P < 0.01, ****P < 0.0001. g, Schematic
cells in CT26 tumors with vehicle control and KO5-39 treatment. Scale bars, view of the dual function of MEN1 in modulating tumor–microenvironment
100 μm. Mean ± s.e.m. of quantifications from 10 tumor IHC sections are shown interactions. MEN1 suppression reshapes MLL1 chromatin binding, triggering
(unpaired two-tailed Student’s t-test). *P < 0.05, ***P < 0.001. d, Tumor growth cytokine gene expression via MAVS- and cGAS-dependent viral mimicry
rate in immunocompetent mice inoculated with CT26 cells following IgG or response. Consequently, this leads to increased infiltration of tumor-promoting
CD8 antibody treatment in combination with vehicle control or ziftomenib neutrophils and tumor-inhibiting CD8+ T cells in immunodeficient and
(150 mg kg−1). Each data point represents mean ± s.e.m. tumor volumes (n = 10 immunocompetent conditions, respectively. DMSO, dimethyl sulfoxide.
in each group). Two-way ANOVA was used for statistical analysis. ***P < 0.001. g, Created with BioRender.com.
endocrine neoplasia type 1 and development of lung, prostate, skin References
and central nerve system tumors47–50. Paradoxically, however, MEN1 also 1. Jin, M.-Z. & Jin, W.-L. The updated landscape of tumor
functions as an oncogene, notably in acute myeloid leukemia with NPM1 microenvironment and drug repurposing. Signal Transduct.
mutations of MLL1-rearrangements46,51. As a chromatin adapter, Target Ther. 5, 166 (2020).
menin is known to directly interact with the N-terminal domain of 2. Mantovani, A., Allavena, P., Sica, A. & Balkwill, F. Cancer-related
H3K4-specific methyltransferase MLL1/MLL2. Our study reveals the inflammation. Nature 454, 436–444 (2008).
existence of an antagonist role for menin, distinct from its previously 3. Hanahan, D. & Weinberg, R. A. Hallmarks of cancer: the next
described cofactor functions. Menin accomplishes this role potentially generation. Cell 144, 646–674 (2011).
by squelching MLL1 in the COMPASS complex, resulting in reduced 4. Balkwill, F. R., Capasso, M. & Hagemann, T. The tumor
MLL1–chromatin interactions at repetitive genomic regions and sub- microenvironment at a glance. J. Cell Sci. 125, 5591–5596
sequent suppression of cytokine-related gene expression. In addi- (2012).
tion, although menin–MLL1 coactivated target genes vary in different 5. Qian, J. et al. A pan-cancer blueprint of the heterogeneous tumor
tissues, the suppression of cytokine signaling is highly consistent microenvironment revealed by single-cell profiling. Cell Res. 30,
across different tissues and species, suggesting a highly conserved 745–762 (2020).
and common mechanism. 6. Wu, S. Z. et al. A single-cell and spatially resolved atlas of human
Insertion of transposable elements resulted in a complex distri- breast cancers. Nat. Genet. 53, 1334–1347 (2021).
bution of interspersed repeats comprising almost half of the human 7. Thorsson, V. et al. The immune landscape of cancer. Immunity 48,
genome52,53. The transcribed interspersed repeats form dsRNA, 812–830.e14 (2018).
which is sensed by the RIG-1/MDA5-MAVS signaling pathway or 8. Tang, L. et al. Nanoparticle-mediated targeted drug delivery
reverse-transcribed and detected via the cGAS–cGAMP STING path- to remodel tumor microenvironment for cancer therapy. Int. J.
way37, leading to increased innate immune responsiveness through Nanomed. 16, 5811–5829 (2021).
a viral mimicry mechanism38,39,54–57. Our data show that upon MEN1 9. Shalem, O. et al. Genome-scale CRISPR–Cas9 knockout
depletion, MLL1 activates cytokine signals at least partially via the screening in human cells. Science 343, 84–87 (2014).
MAVS and cGAS–STING pathways. The potential cooperative effects 10. Wang, T., Wei, J. J., Sabatini, D. M. & Lander, E. S. Genetic screens
of these epigenetic regulators warrant further exploration. in human cells using the CRISPR–Cas9 system. Science 343,
The immunocompetence-dependent tumor-inhibiting and 80–84 (2014).
-promoting function provides a mechanism underlying the paradoxi- 11. Henriksson, J. et al. Genome-wide CRISPR screens in T helper
cal function of MEN1. Several inhibitors that block menin–MLL interac- cells reveal pervasive crosstalk between activation and
tions have entered clinical development in acute myeloid leukemia25,26. differentiation. Cell 176, 882–896.e18 (2019).
Our data suggest that menin inhibition may also offer therapeutic 12. Manguso, R. T. et al. In vivo CRISPR screening identifies Ptpn2 as a
value related to activation of the immune response in solid tumors. cancer immunotherapy target. Nature 547, 413–418 (2017).
Because infiltrating immune cells may have both tumor-promoting 13. Shifrut, E. et al. Genome-wide CRISPR screens in primary human
and -inhibiting effects, the efficacy of menin inhibition will likely be T cells reveal key regulators of immune function. Cell 175,
context-specific. Additional studies identifying biomarkers predicting 1958–1971 (2018).
the efficacy are warranted. 14. Tsherniak, A. et al. Defining a cancer dependency map. Cell 170,
In summary, our study presents a mechanism contributing to the 564–576.e16 (2017).
paradoxical tumor-suppressive and oncogenic function of MEN1 and 15. Jin, V., Wang, J. & Tang, B. Integration of Multisource Heterogenous
provides a strong rationale for targeting menin alone or in combination Omics Information in Cancer (Frontiers Media SA, 2020).
with immunotherapy for both hematologic and solid cancer. 16. Pacini, C. et al. Integrated cross-study datasets of genetic
dependencies in cancer. Nat. Commun. 12, 1661 (2021).
Online content 17. Wang, X. et al. In vivo CRISPR screens identify the E3 ligase
Any methods, additional references, Nature Portfolio reporting sum- Cop1 as a modulator of macrophage infiltration and cancer
maries, source data, extended data, supplementary information, immunotherapy target. Cell 184, 5357–5374.e22 (2021).
acknowledgements, peer review information; details of author contri- 18. Li, F. et al. In vivo epigenetic CRISPR screen identifies Asf1a as an
butions and competing interests; and statements of data and code avail- immunotherapeutic target in Kras-mutant lung adenocarcinoma.
ability are available at https://doi.org/10.1038/s41588-024-01874-9. Cancer Discov. 10, 270–287 (2020).
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1900
Article https://doi.org/10.1038/s41588-024-01874-9
19. Gao, S. et al. CRISPR screens identify cholesterol biosynthesis as 42. Chen, S. et al. Single-cell analysis reveals transcriptomic
a therapeutic target on stemness and drug resistance of colon remodellings in distinct cell types that contribute to human
cancer. Oncogene 40, 6601–6613 (2021). prostate cancer progression. Nat. Cell Biol. 23, 87–98 (2021).
20. Soares, F. et al. CRISPR screen identifies genes that sensitize 43. Xu, W. et al. Early innate and adaptive immune perturbations
AML cells to double-negative T-cell therapy. Blood 137, 2171–2181 determine long-term severity of chronic virus and Mycobacterium
(2021). tuberculosis coinfection. Immunity 54, 526–541.e7 (2021).
21. Chen, S. et al. Genome-wide CRISPR screen in a mouse model of 44. Krivtsov, A. V. et al. A Menin-MLL inhibitor induces specific
tumor growth and metastasis. Cell 160, 1246–1260 (2015). chromatin changes and eradicates disease in models of
22. Li, W. et al. MAGeCK enables robust identification of essential MLL-rearranged leukemia. Cancer Cell 36, 660–673.e11 (2019).
genes from genome-scale CRISPR/Cas9 knockout screens. 45. Grembecka, J. et al. Menin-MLL inhibitors reverse oncogenic
Genome Biol. 15, 554 (2014). activity of MLL fusion proteins in leukemia. Nat. Chem. Biol. 8,
23. Meyers, R. M. et al. Computational correction of copy number 277–284 (2012).
effect improves specificity of CRISPR–Cas9 essentiality screens in 46. Davis, J. A. et al. Clinical-stage menin inhibitor KO-539 is
cancer cells. Nat. Genet. 49, 1779–1784 (2017). synergistically active with multiple classes of targeted agents in
24. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold KMT2A-r and NPM1-mutant AML models. Blood 138, 3357 (2021).
change and dispersion for RNA-seq data with DESeq2. Genome 47. Al-Salameh, A., Cadiot, G., Calender, A., Goudet, P. & Chanson, P.
Biol. 15, 550 (2014). Clinical aspects of multiple endocrine neoplasia type 1. Nat. Rev.
25. Perner, F. et al. MEN1 mutations mediate clinical resistance to Endocrinol. 17, 207–224 (2021).
menin inhibition. Nature 615, 913–919 (2023). 48. Qiu, H. et al. MEN1 deficiency leads to neuroendocrine
26. Issa, G. C. et al. The menin inhibitor revumenib in differentiation of lung cancer and disrupts the DNA damage
KMT2A-rearranged or NPM1-mutant leukaemia. Nature 615, response. Nat. Commun. 11, 1009 (2020).
920–924 (2023). 49. Chandrasekharappa, S. C. et al. Positional cloning of the gene
27. Sparbier, C. E. et al. Targeting Menin disrupts the KMT2A/B and for multiple endocrine neoplasia-type 1. Science 276, 404–407
polycomb balance to paradoxically activate bivalent genes. Nat. (1997).
Cell Biol. 25, 258–272 (2023). 50. Jiao, Y. et al. DAXX/ATRX, MEN1, and mTOR pathway genes are
28. Soto-Feliciano, Y. M. et al. A molecular switch between frequently altered in pancreatic neuroendocrine tumors. Science
mammalian MLL complexes dictates response to Menin-MLL 331, 1199–1203 (2011).
inhibition. Cancer Discov. 13, 146–169 (2023). 51. Yokoyama, A. & Cleary, M. L. Menin critically links MLL proteins
29. Lin, J. et al. Menin ‘reads’ H3K79me2 mark in a nucleosomal with LEDGF on cancer-associated target genes. Cancer Cell 14,
context. Science 379, 717–723 (2023). 36–46 (2008).
30. La, P. et al. Tumor suppressor menin: the essential role of nuclear 52. Lander, E. S. et al. Initial sequencing and analysis of the human
localization signal domains in coordinating gene expression. genome. Nature 409, 860–921 (2001).
Oncogene 25, 3537–3546 (2006). 53. Payer, L. M. & Burns, K. H. Transposable elements in human
31. Skene, P. J. & Henikoff, S. An efficient targeted nuclease strategy genetic disease. Nat. Rev. Genet. 20, 760–772 (2019).
for high-resolution mapping of DNA binding sites. eLife 6, e21856 54. Babaian, A. & Mager, D. L. Endogenous retroviral promoter
(2017). exaptation in human cancer. Mob. DNA 7, 24 (2016).
32. Zhang, Y. et al. Model-based analysis of ChIP-Seq (MACS). 55. Deblois, G. et al. Epigenetic switch-induced viral mimicry evasion
Genome Biol. 9, R137 (2008). in chemotherapy-resistant breast cancer. Cancer Discov. 10,
33. Wang, S. et al. Target analysis by integration of transcriptome and 1312–1329 (2020).
ChIP-seq data with BETA. Nat. Protoc. 8, 2502–2515 (2013). 56. Sheng, W. et al. LSD1 ablation stimulates anti-tumor immunity and
34. Soto-Feliciano, Y. M. et al. Molecular switch between mammalian enables checkpoint blockade. Cell 174, 549–563.e19 (2018).
MLL complexes dictates response to Menin-MLL inhibition. 57. Chiappinelli, K. B. et al. Inhibiting DNA methylation causes an
Cancer Discov. 13, 146–169 (2023). interferon response in cancer via dsRNA including endogenous
35. Madani Tonekaboni, S. A., Haibe-Kains, B. & Lupien, M. Large retroviruses. Cell 162, 974–986 (2015).
organized chromatin lysine domains help distinguish primitive
from differentiated cell populations. Nat. Commun. 12, 499 (2021). Publisher’s note Springer Nature remains neutral with regard to
36. Chen, R., Ishak, C. A. & De Carvalho, D. D. Endogenous jurisdictional claims in published maps and institutional affiliations.
retroelements and the viral mimicry response in cancer
therapy and cellular homeostasis. Cancer Discov. 11, 2707–2725 Open Access This article is licensed under a Creative Commons
(2021). Attribution-NonCommercial-NoDerivatives 4.0 International License,
37. Gao, D. et al. Cyclic GMP–AMP synthase is an innate immune which permits any non-commercial use, sharing, distribution and
sensor of HIV and other retroviruses. Science 341, 903–906 reproduction in any medium or format, as long as you give appropriate
(2013). credit to the original author(s) and the source, provide a link to the
38. Roulois, D. et al. DNA-demethylating agents target colorectal Creative Commons licence, and indicate if you modified the licensed
cancer cells by inducing viral mimicry by endogenous transcripts. material. You do not have permission under this licence to share
Cell 162, 961–973 (2015). adapted material derived from this article or parts of it. The images
39. Morel, K. L. et al. EZH2 inhibition activates a dsRNA–STING– or other third party material in this article are included in the article’s
interferon stress axis that potentiates response to PD-1 checkpoint Creative Commons licence, unless indicated otherwise in a credit
blockade in prostate cancer. Nat. Cancer 2, 444–456 (2021). line to the material. If material is not included in the article’s Creative
40. Liu, S. et al. Phosphorylation of innate immune adaptor proteins Commons licence and your intended use is not permitted by statutory
MAVS, STING, and TRIF induces IRF3 activation. Science 347, regulation or exceeds the permitted use, you will need to obtain
aaa2630 (2015). permission directly from the copyright holder. To view a copy of this
41. Borkin, D. et al. Pharmacologic inhibition of the Menin-MLL licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.
interaction blocks progression of MLL leukemia in vivo. Cancer
Cell 27, 589–602 (2015). © The Author(s) 2024
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1901
Article https://doi.org/10.1038/s41588-024-01874-9
1Department of Medical Biophysics, University of Toronto, Toronto, Ontario, Canada. 2Princess Margaret Cancer Centre, University Health Network,
Toronto, Ontario, Canada. 3Department of Laboratory Medicine, Shanghai Pulmonary Hospital, Tongji University School of Medicine, Shanghai, China.
4Department of Immunology, University of Toronto, Toronto, Ontario, Canada. 5Institute of Precision Medicine, The First Affiliated Hospital, Sun Yat-sen
University, Guangzhou, China. 6Ludwig Institute for Cancer Research, Nuffield Department of Medicine, University of Oxford, Oxford, UK. 7Department of
Laboratory Medicine and Pathobiology, University of Toronto, Toronto, Ontario, Canada. 8Department of Thoracic Surgery, Shanghai Pulmonary Hospital,
Tongji University School of Medicine, Shanghai, China. 9Kura Oncology Inc, San Diego, CA, USA. 10Department of Molecular Genetics, University of
Toronto, Toronto, Ontario, Canada. 11Centre for Molecular and Systems Biology, Lunenfeld-Tanenbaum Research Institute, Mount Sinai Hospital, Toronto,
Ontario, Canada. 12Present address: West China School of Public Health and West China Fourth Hospital, and State Key Laboratory of Biotherapy, Sichuan
University, Chengdu, China. 13These authors contributed equally: Peiran Su, Yin Liu, Tianyi Chen. e-mail: Ming.Tsao@uhn.ca; hansenhe@uhnresearch.ca
Nature Genetics | Volume 56 | September 2024 | 1890–1902 1902
Article https://doi.org/10.1038/s41588-024-01874-9
Methods Following sonication, the cell lysate was precleared with 40 μl of
All samples obtained in this study complied with the relevant ethi- protein A/G beads before incubation with antibody-coated beads at
cal regulations approved by the institutional ethics committee and 4 °C overnight. To prepare the antibody-coated beads, 5 μg of target
Research Ethics Board at the University Health Network (UHN). antibody of interest were incubated with 11 μl of protein A and 11 μl
of protein G beads (Thermo Fisher Scientific, cat. no. 10002D and
Western blotting 10004D) with rotation for at least 6 h at 4 °C. Antibodies used for ChIP
Cells were lysed in RIPA buffer containing phosphatase and protease assays included anti-menin (Bethyl Laboratories, cat. no. A300-105A),
inhibitor cocktails (Roche, cat. no. 11697498001). Protein was quanti- anti-MLL1 (Abcam, cat. no. ab272023), anti-H3K27me3 (Abcam, cat.
fied using a bicinchoninic acid assay. Secondary antibodies were used no. ab6002), anti-H4K4me3 (Abcam, cat. no. ab8580) and anti-UTX
at a 1:5,000 dilution. Primary antibodies were diluted according to (Bethyl Laboratories, cat. no. A302-374A).
the manufacturers’ recommended ratios. Used antibodies included After incubation, beads underwent a series of washes: once with
anti-menin (Bethyl Laboratories, cat. no. A300-105A), anti-MLL1 0.5 ml of modified RIPA buffer, once with high salt modified RIPA buffer
(Abcam, cat. no. ab272023), anti-H4K4me3 (Abcam, cat. no. ab8580), (NaCl increased to 500 mM), once with LiCl buffer (10 mM Tris–HCl pH
anti-UTX (Bethyl Laboratories, cat. no. A302-374A), anti-cGAS (Cell 8, 1 mM EDTA, 250 mM LiCl, 0.5% NP-40, 0.1% sodium deoxycholate) on
Signaling Technology, cat. no. 151025), anti-MAVS (Abcam, cat. no. a rotator for 5 min each at 4 °C, and finally twice with 0.5 ml of TE buffer
ab89825), anti-TBK1 (Cell Signaling Technology, cat. no. 3504T), (pH 8). The beads were then resuspended in 100 μl of de-crosslinking
anti-pTBK1 (Cell Signaling Technology, cat. no. 5483T), GAPDH (Santa buffer (1% SDS, 0.1 M NaHCO). Subsequently, 1 μl of RNase A (Thermo
3
Cruz Biotechnology, cat. no. sc-47724) and Vinculin (Cell Signaling Fisher Scientific, cat. no. EN0531) was added, and the mixture was
Technology, cat. no. 13901S), H3 (Cell Signaling Technology, cat. no. incubated at 37 °C for 30 min with shaking, followed by incubation at
4499L) and β-tubulin (Cell Signaling Technology, cat. no. 2128S). 55 °C for 30 min with shaking in the presence of 2 μl of Proteinase K
(Thermo Fisher Scientific, cat. no. AM2546). The crosslinking was
CUT&RUN assays reversed by incubating at 65 °C overnight with shaking. DNA purifica-
In total, 250,000 cells per condition were washed twice with 1 ml of tion was carried out using the PCR purification kit (Qiagen, cat. no.
wash buffer by pelleting for 3 min at 600g. As previously described58, 28004), and the purified DNA was then subjected to qPCR or Illumina
the cells were bound to Concanavalin A magnetic beads (Cell Signaling ChIP-Seq library construction using the ThruPLEX DNA-seq kit (Takara,
Technology, cat. no. 93569S) using nuclear binding buffer and incu- cat. no. R400676).
bated at room temperature on a rotator at 15 rpm for 10 min. Antibodies
(anti-menin (Bethyl Laboratories, cat. no. A300-105A) and anti-MLL1 sgRNA pooled library design and synthesis
(Abcam, cat. no. ab272023)), were diluted to a ratio of 1:100 using anti- The Epi-Drug library consists of ~12,500 sgRNAs targeting 317 epi-
body buffer. After the 10-min incubation, the samples were placed on a genetic regulators, 657 US Food and Drug Administration-approved
magnetic separator. The nuclear binding buffer was removed and the drug targets based on DrugBank 4.3 (ref. 60), and control genes, with
antibody mixture was added to the bead-bound samples. Samples were 10 sgRNAs per gene on average (Supplementary Table 1). The sgRNAs
incubated overnight at 4 °C on a rotator. Following overnight incuba- were designed using the CRISPR-DO tool that accounted for sgRNA
tion, pAG-MNAse enzyme (Cell Signaling Technology, cat. no. 40366S) specificity and cutting efficiency61. sgRNAs were synthesized as 73-base
was diluted 1:1,000 in digitonin buffer. The samples were placed on a polymer/oligonucleotides (CustomArray). After being amplified by
magnetic separator, supernatant was removed and pAG-MNAse buffer PCR, the PCR product was purified and cloned in the lentiGuide-Puro
was added. The samples were mixed on a rotator (15 rpm) and incubated vector using BsmBI (NEB). Ligation was performed using the NEBuilder
at 4 °C for 1 h. To activate the pAG-MNAse, 3 μl of cold 100 mM CaCl was HiFi DNA Assembly Cloning Kit and transformed into an electrocompe-
2
added and the samples were incubated on ice for 30 min. After 30 min, tent stain (Stbl4; Thermo Fisher Scientific) to achieve ~300× coverage.
stop buffer was immediately added to quench the pAG-MNAse reaction. Colonies were scraped off agar plates with LB medium. Plasmid DNA
DNA fragments were released from the cells by incubating at 37 °C for was extracted using a NA0310 Sigma GenElute HP Plasmid Maxiprep
10 min with 700 rpm shaking, followed by a 5-min centrifugation at Kit and adequate library representation of each sgRNA was confirmed
16,000g at 4 °C. Supernatant containing DNA fragments was moved to a by NGS.
new tube containing 3 μl of 10% SDS and 2.5 μl of Proteinase K (Thermo
Fisher Scientific, cat. no. EO0492) then incubated for 10 min at 70 °C. CRISPR–Cas9 screening, sequencing and analysis
The DNA fragments were purified using phenol–chloroform extraction. Library viruses were produced in HEK293FT cells and multiplicity of
Purified DNA was quantified via Qubit and 7.5 ng was used for input into infection was determined for the A549 cell line as previously described9.
the library preparation. Library preparation was completed following The Cas9-expressing A549 cell line was infected with the library at
the Takara SMARTer ThruPLEX DNA-Seq protocol (Takara Bio, cat. no. an multiplicity of infection of ~0.3 and coverage of >200×. At 24 h
R400676). Samples were amplified using 11 PCR cycles as determined post-infection, cells were selected with puromycin for 72 h (1 μg ml−1)
via qPCR. Final library traces were generated using the Agilent 2100 and then cultured for ~21 days in Petri dishes or subcutaneously inocu-
Bioanalyzer and quantified via qPCR before sequencing. Libraries lated into mice for ~21 days. Day 0 genomic DNA was harvested after
were sequenced to a depth of 50–60 million reads per sample using 3 days of puromycin selection. Genomic DNA was extracted and sgRNA
paired-end 50 sequencing configuration on Illumina’s NovaSeq 6000. inserts were amplified by PCR as previously described62. Screens were
performed in duplicate, and the libraries were sequenced on an Illumina
Chromatin immunoprecipitation assay HiSeq2500.
ChIP assays on A549 cells were conducted as previously described59, both The NGS data from CRISPR screens were first aligned to the library
with and without MEN1 knockdown. In brief, 5 million cells underwent sgRNAs using bowtie. The resulting count matrix was the input to
crosslinking with 1% formaldehyde for 10 min at room temperature, fol- the tool MAGeCK22, which estimates the enrichment/depletion of
lowed by quenching with 125 mM glycine. Subsequently, the cell pellets individual sgRNAs using a negative binomial model and estimates
were twice washed with cold PBS buffer and resuspended in 300 μl of the enrichment of genes using the robust ranking aggression model.
modified RIPA buffer (10 mM Tris–HCl pH 8, 1 mM EDTA, 140 mM NaCl, 1%
Triton X-100, 0.1% SDS, 0.1% sodium deoxycholate) supplemented with Mouse tumor growth experiments
protease inhibitor. The resuspended pellet underwent sonication for 18 Four- to six-week-old male NSG, C57BL6 and BALB/c mice were main-
cycles (30 s on, 30 s off) at 4 °C using Bioruptor (Diagenode). tained at the UHN Animal Resources Centre. NSG, C57BL6 or BALB/c
Nature Genetics
Article https://doi.org/10.1038/s41588-024-01874-9
mice were injected subcutaneously with 50 μl of a single-cell sus- scaled to reads per 10 million for both plus and minus strands. The
pension containing 5 × 105 MEN1/Men1 knockout and control A549, bedGraph files were converted to bigwig format using the bedGraph-
HCT116, CT26, 4T1, HKP1 or DKO cells. Syngeneic CT26, 4T1 models ToBigWig function in the BLAT suite.
were injected subcutaneously in 50 μl of a single-cell suspension into
BALB/c mice. Cryo-preserved OCIP200 PDX tissues were implanted CUT&RUN and ChIP-seq mapping and data processing
subcutaneously in NSG mice. The tumors were expanded in mouse CUT&RUN and ChIP-seq reads were mapped to the human genome
replicates (n = 10) to evaluate the agent ziftomenib. Once tumors had (hg38) using bowtie. MACS2 callpeak was used for peak calling with
initiated growth, the vehicle or drug was administered daily by oral the parameter ‘–SPMR’ on. MACS232 bdgdiff was used to call differential
gavage. To generate humanized mice, human peripheral blood mono- peaks. Resultant bedgraph files were converted to big wiggle files with
nuclear cells were engrafted into NSG pups after the pups had been the bedGraphToBigWig function. CREAM67 was applied to call broad
irradiated at 1 Gy. Ten to twelve weeks after the injection, blood samples peak regions followed by the removal of ENCODE blacklist regions.
were collected from the mice, and human immune cell engraftment
was determined by flow cytometry. Humanized mice with engraftment Gene Ontology analysis
efficiency (percent human CD45+/(percent human CD45+ + percent Gene Ontology (GO) and KEGG analyses were performed using R pack-
mouse CD45+)) values between 20% and 50% were used in subsequent age clusterProfiler v.3.10.1 (ref. 68). Terms with a false discovery rate
A549 xenograft experiments. Mouse weight and tumor volume were <0.01 were considered significantly enriched. A complete list of terms
measured twice weekly. Xenograft (tum) or sizes were measured twice enriched can be found in the supplementary datasets.
per week. Tumor volumes were calculated using the formula: tumor vol-
ume (mm3) = L × W2/2, where L is the major axis (largest cross-sectional BETA analysis
diameter) of the tumor and W is the minor axis. The data are presented BETA (v.1.0.7)33 software was used to predict menin directly regulated genes
as the mean ± s.e.m. Mice were sacrificed when the diameter of the by combining menin binding peaks and differentially expressed genes.
tumor reaches 1.5 cm. All procedures were performed in accordance
with the International Guidelines for the Use of Animals and approved Repeats analysis
by the Animal Care Committee at UHN. The human repeat masker file was downloaded from the website
(http://www.repeatmasker.org/genomes/hg38/RepeatMasker-
Gene knockout and transfection rm405-db20140131/hg38.fa.out.gz). The reference file was con-
Guide RNA plasmids targeting MEN1 was constructed into a lentiC- verted to bed format using bedops/2.4.37. RNA-seq reads were
RISPR V2-Blast vector (Addgene, cat. no. 83480). Guide RNA plasmids remapped to genome hg38 by STAR (v.2.4.2a)63 with parameter –
targeting MAVS and cGAS were constructed in a lentiCRISPR V2 vector outFilterMultimapNMax set to 100 and –winAnchorMultimapNmax
(Addgene, cat. nos. 83480, 98291, 98290). siRNAs were transfected into set to 100. Exon reads were calculated by HTSeq (v.0.11.0)66. Exons with
the cancer cells by RNAiMAX reagent (Thermo Fisher Scientific, cat. no. more than five reads were subtracted from the repeats masker file by
13778075), following the manufacturer’s protocol. siRNAs used in this running bedtools (v.2.27.1)69 subtract. Read counts on repeat regions
study were ordered from Thermo Fisher Scientific and sequences are were calculated by bedtools (v.2.27.1)69 multicov. DESeq2 was used to
listed in Supplementary Table 7. call differential repeats.
Statistical analyses and reproducibility Immunofluorescence confocal microscopy
Statistical analyses for in vitro and in vivo assays were performed using A549 cells constitutively expressing Cas9 protein were infected with
GraphPad Prism v.6 (GraphPad Software). Data were expressed as lentivirus containing sgRNA targeting LacZ or MEN1. A round cov-
mean ± s.e.m. Two-tailed unpaired Student’s t-test and one-way analysis erslip was loaded to a 24-well plate and incubated with 1 ml of 100%
of variance (ANOVA) were performed to identify significant differences ethanol for 5 min at room temperature. After one wash with PBS buffer,
between groups in our experiments. R v.3.3.0 was used to perform sta- 75,000 cells in growth media were seeded to each well. The plates were
tistical analysis. Details of the test method used for statistical analysis incubated at 37 °C overnight to allow attachment of the cells to the
is specified in the relevant figure captions and Methods. All values coverslip. The next day, the medium was aspirated, and the cells were
were considered significantly different at P < 0.05. Western blotting washed once with PBS and fixed with ice cold methanol for 15 min at
for MEN1 knockout samples was performed in biological replicates. −20 °C. The cells were washed three times with PBS and blocked with
1% bovine serum albumin in PBS at room temperature for 1 h. Primary
RNA-seq mapping and data processing antibody targeting dsRNA (J2; Scicons, cat. no. 10010500) and γ-H2AX
RNA was extracted with TRIzol reagent (Thermo Fisher Scientific, (EMD Millipore, cat. no. JBW30) diluted with blocking solution at a
cat. no. 15596026) and processed using a RNA-seq library prepara- ratio of 1:500 was added to each well, and the plates were incubated at
tion kit (Illumina, cat. no. RS-122-2101) to produce libraries for deep 4 °C overnight with shaking. The next day, the diluted antibodies were
sequencing on NextSeq. Library preparation and sequencing were aspirated, and the cells were washed three times with PBS for 10 min
performed according to the manufacturer’s protocol. RNA-seq raw at room temperature with shaking. The cells were then incubated
reads were first filtered by trim_galore (v.0.5.0) then mapped to the with the secondary antibody (anti-mouse immunoglobulin G (IgG)
human genome (hg38) using STAR (v.2.4.2a)63 software with default (H+L), F(ab′) fragment (Alexa Fluor 647 conjugate; Cell Signaling
2
parameters. The hg38 GENCODE gene list was used for all transcrip- Technology, cat. no. 4410s) diluted with blocking solution at a ratio of
tion level analysis. RNA-seq reads strands were determined by RSeQC 1:1,000 in a dark environment for 1 h at room temperature with shak-
(v.2.6.1)64,65. HTSeq (v.0.11.0)66 was used to obtain gene-level read counts ing. The cells were washed three times with PBS in a dark environment
from STAR-mapped bam files. The resultant gene read count table was at room temperature for 10 min with shaking. The coverslips were
subjected to DESeq2 (v.1.22.2)24 for differential gene analysis and a false mounted to glass slides with ProLong Gold Antifade Mountant with
discovery rate cutoff of 0.01 was chosen to identify significant differen- 4′,6-diamidino-2-phenylindole (DAPI) (Thermo Fisher Scientific, cat.
tial genes. A log(fold change) value less than −1 and a log(fold change) no. P36935). Confocal microscopy was performed with Zeiss LSM700
2 2
value above 1 were chosen as upregulated genes and downregulated (oil ×40 magnification) and ImageJ software was used to analyze the
genes, respectively. images acquired. Corrected total cell fluorescence was calculated
For visualization of RNA-seq data, we generated bedGraph files as: corrected total cell fluorescence = integrated density − (area of
using genomeCoverageBed function in the BEDTools suite with signal selected cell × mean fluorescence of background readings).
Nature Genetics
