---
source_path: /mnt/c/Users/Administrator/Zotero/storage/NYNAELSY/The Tabula Muris Consortium 等 - 2020 - A single-cell transcriptomic atlas characterizes ageing tissues in the mouse.pdf
ingested: 2026-04-23
sha256: 41e1abb68fd9f133
---

Article
A single-cell transcriptomic atlas
characterizes ageing tissues in the mouse
https://doi.org/10.1038/s41586-020-2496-1 The Tabula Muris Consortium*
Received: 5 June 2019
Accepted: 7 May 2020 Ageing is characterized by a progressive loss of physiological integrity, leading to
impaired function and increased vulnerability to death1. Despite rapid advances over
Published online: 15 July 2020
recent years, many of the molecular and cellular processes that underlie the
Check for updates
progressive loss of healthy physiology are poorly understood2. To gain a better insight
into these processes, here we generate a single-cell transcriptomic atlas across the
lifespan of Mus musculus that includes data from 23 tissues and organs. We found
cell-specific changes occurring across multiple cell types and organs, as well as
age-related changes in the cellular composition of different organs. Using single-cell
transcriptomic data, we assessed cell-type-specific manifestations of different
hallmarks of ageing—such as senescence3, genomic instability4 and changes in the
immune system2. This transcriptomic atlas—which we denote Tabula Muris Senis, or
‘Mouse Ageing Cell Atlas’—provides molecular information about how the most
important hallmarks of ageing are reflected in a broad range of tissues and cell types.
We performed single-cell RNA sequencing on more than 350,000 cells a wealth of new information about their characteristic gene expression
from male and female C57BL/6JN mice belonging to six age groups, profiles. Out of 529,823 total cells sequenced, 110,824 cells for FACS and
ranging from 1 month (the equivalent of human early childhood) to 30 245,389 cells for droplet passed our strict filtering criteria (Extended
months (the equivalent of a human centenarian) (Fig. 1a). For all mice, Data Fig. 4b) and were annotated (Extended Data Fig. 2a, b), which was
we prepared single-cell suspensions of the bladder, bone marrow, brain carried out separately for each tissue and method. The remaining cells
(cerebellum, cortex, hippocampus and striatum), fat (brown, gonadal, are also included in the online dataset but were not used for further
mesenteric and subcutaneous), heart and aorta, kidney, large intestine, analysis here. To investigate whether cell annotations were consist-
limb muscle and diaphragm, liver, lung, mammary gland, pancreas, ent across the entire organism, we used the bbknn batch-alignment
skin, spleen, thymus, tongue and trachea. Data were collected for all six algorithm6 to correct for method-associated batch effects (Supple-
age groups using a microfluidic droplet method (droplet); the 3-month, mentary Table 3). After batch correction, we clustered all cells using an
18-month and 24-month time points were also analysed using single unbiased, graph-based clustering approach7,8 (Fig. 1c, d) and assessed
cells sorted in microtitre well plates (fluorescence-activated cell sort- the co-occurrence of similarly annotated cells in the same clusters. For
ing; FACS) (Extended Data Figs. 1–3, Supplementary Tables 1, 2). Owing example, cells annotated as B cells or endothelial cells tend to occupy
to technical constraints, not every tissue was analysed at all time points; the same clusters irrespective of their tissue of origin or the method
a complete list is provided in Extended Data Fig. 4a. The droplet data with which they were processed (Fig. 1e, f, Extended Data Fig. 1g–l).
enable large numbers of cells to be analysed using 3′ end counting, The Tabula Muris Senis enables the discovery of ageing-related
whereas the FACS data allow for higher-sensitivity measurements over changes in specific cell types. Single-cell data enables us to resolve
smaller numbers of cells as well as enabling the acquisition of sequence whether gene expression changes observed in bulk experiments are due
information across the entire transcript length. The analysis of multiple to changes in gene expression in each cell of the population, or whether
organs from the same mouse enables us to obtain data that is controlled the gene expression in each cell stays constant but the number of cells
for age, environment and epigenetic effects. of that type changes, or both. In a global analysis of gene expression
Data from the 3-month time point—which has previously been changes using the Tabula Muris Senis and bulk RNA sequencing from
published and constitutes the Tabula Muris5—represents approxi- tissues9, we observed that—in many cases—changes in gene expression
mately 20% of the cells in the entire dataset, and was used as a basis are due to both changes in the numbers of cells in a population and
from which to perform semi-automated cell-type annotation of the changes in the gene expression levels in each cell (Extended Data Fig. 5a,
data from the additional time points (Fig. 1b, Extended Data Fig. 4b). b). As one specific example, we investigated how the fraction of cells
Using this approach, we were able to automatically annotate more than that express Cdkn2a changes with age. The expression of Cdkn2a and
70% of the cells. All the automated cell annotations were reviewed and its protein product p16 is one of the most frequently used markers of
approved by human experts, and the remaining cells were annotated senescence10 and is an important hallmark of ageing11. The proportion
by hand, creating one of the largest manually curated single-cell tran- of cells expressing Cdkn2a more than doubled in older mice compared
scriptomic resources in existence. Many of these cell types have not with younger mice according to analysis by both FACS (Fig. 2a) and
previously been obtained in pure populations, and these data provide droplet (Fig. 2b) methods; this was accompanied by a twofold increase
*A list of members and their affiliations appears at the end of the paper.
590 | Nature | Vol 583 | 23 July 2020
a
A B or A t T a Droplet P0 Tabula Muris
Bladder FACS 1 m 3 m 18 m 21 m 24 m 30 m
Brain myeloid n = 19 n = 2 n = 7 n = 2 n = 4 n = 4
Brain non-myeloid
Diaphragm
K H id G e n F a A e a r T y t t n = 1 b 1 Uncla n ss = ifi 4 ed data n se = t 4 n = 3 Tabula Muris Senis
Large intestine
Limb muscle
Liver
Lung
MAT
Mammary gland
Marrow Expert
Pancreas curation
SCAT
Skin
Spleen
Thymus
Tongue
Trachea
0 20,000 40,000 60,000 Tabula Muris Automatically classified dataset
Number of cells
c d
UMAP1
in the expression levels of p16 in cells in which it was expressed (Fig. 2c, are upregulated, supporting the compositional observations (Fig. 2f,
d). Notably, in 30-month-old mice the fraction of cells that expressed Supplementary Table 6). The decline of the endothelial population
p16 was smaller than in 24-month-old mice, perhaps because long-living suggests that bladder ageing in mice might be associated with lower
animals have a slower rate of senescence. Using a list of previously organ vascularization, which is consistent with recent findings26,27 and
characterized senescence markers12–15, we plotted the fraction of cells with the observed downregulation of vasculature-associated genes
expressing each marker across all age groups (Supplementary Table 4). Htra1 and Fos (Fig. 2f, Supplementary Table 6). The increase in the
Cdkn2a has the highest correlation between ageing and the fraction leukocyte population could indicate an inflammatory tissue micro-
of cells in which it is expressed; other genes with positive correlation environment, a common hallmark of ageing that is consistent with
include E2f216, Lmnb117,18, Tnf and Itgax19. For some genes, including literature on overactive bladders28 and is supported by a significant
members of the Sirt family (Sirt3, Sirt4 and Sirt5), the fraction of cells overexpression of Lgals3, Igfbp2 and Ly6d across the tissue (Fig. 2f,
in which they were expressed was found to decrease with age; this is Supplementary Table 6), as well as by the overexpression of genes
consistent with previous literature finding that sirtuins—the protein associated with immune response—such as Tnfrsf12a and Cdkn1a—in
products of Sirt genes—are essential in delaying cellular senescence20,21. both bladder (mesenchymal) cells and bladder urothelial cells (Supple-
The cellular composition of each tissue type tends to vary with age. mentary Table 6). Moreover, when comparing across ages, we observed
We investigated changes in the cellular composition of tissues for which that old leukocytes show increased expression of pro-inflammatory
data from at least three time points was available (Supplementary markers—such as Cd14, Lgals3 and Tnfrsf12a—and decreased expression
Table 5). Because dissociation does not affect all cell types in a tissue of anti-inflammatory markers such as Cd9 and Cd81 (Supplementary
equally, changes in the relative composition of a given cell type with Table 6).
age are more meaningful than comparing proportions of different Age-related changes in the kidney include a decrease in the relative
cell types at a single age22–24. The bladder shows pronounced changes abundance of mesangial cells, capillary endothelial cells, loop of Henle
in cell-type composition with age (Fig. 2e): whereas the mesenchymal ascending limb epithelial cells and loop of Henle thick ascending limb
compartment of this tissue decreases by a factor of three over the life- epithelial cells (Fig. 2g). Both mesangial cells and capillary endothelial
time of the mouse (Fig. 2e, left), the urothelial compartment increases cells are core glomerular cells, and the reduction in their relative abun-
by a similar amount (Fig. 2e, right). The observation that the propor- dances with age (Fig. 2g, top)—together with a tissue-wide reduction of
tion of bladder urothelial cells increases with age is concordant with Egf and Atp1a1 expression (Fig. 2h, Supplementary Table 6)—suggest an
known age-related urothelial changes25. Using differential gene expres- impaired glomerular filtration rate29,30. Notably, local Atp1a1 expression
sion analysis to assess overall changes in tissues with age, we found increases with age in both capillary endothelial cells and mesangial cells,
that stromal-associated genes (Col1a1, Col1a2, Col3a1 and Dcn) are suggesting that a compensation mechanism counteracts the effects of
downregulated while epithelial-associated genes (Krt15, Krt18 and Sfn) the declining proportion of these cells with age. This finding is reinforced
Nature | Vol 583 | 23 July 2020 | 591
2PAMU
UMAP1
2PAMU
1 m e
33 mm
13 1188 mm
34 23 31 41 25 1 17 49 2 3 2 2 3 2 0 4 0 1 4 1 m m m m m m 0 B cell
28
14 33 3050 35 8 10 19 7
2 2 4 7 5 18 3 3 9 8 2 1 6 4 6 642 6 4 3 7 7 4 44 32 40 5 2 2 9 3 1 5 5 322 4 3 5 6 f 7
48 2
21 0 43 Endothelial
51 11 19 cell 35
20 12 9
53
10
Fig. 1 | Overview of the Tabula Muris Senis. a, A total of 23 organs from 19 male time point) as a reference for the automated pipeline and the annotations were
and 11 female mice were analysed at 6 different time points. The bar plot shows manually curated by tissue experts. c, d, Uniform manifold approximation and
the number of sequenced cells per organ prepared by FACS (n = 23 organs) and projection (UMAP) plot of all cells, coloured by organ and overlaid with the
by microfluidic droplets (n = 16 organs). For the droplet dataset the fat Louvain cluster numbers (c) and age (d); n = 356,213 individual cells. See
sub-tissues were processed together (Fat = BAT + GAT + MAT + SCAT; BAT, Extended Data Fig. 4c, d for the colour dictionaries. e, f, B cells (e) and
brown adipose tissue; GAT, gonadal adipose tissue; MAT, mesenteric adipose endothelial cells (f) independently annotated for each organ cluster together
tissue; SCAT, subcutaneous adipose tissue). b, Annotation workflow. Data were by unbiased whole-transcriptome Louvain clustering, irrespective of the organ
clustered together across all time points. We used the Tabula Muris (3-month in which they were found.
Article
e 0.7 0.6
0.5
0.4
0.3 0.2
0.1
0 5 10 15 20 25 Age (months)
f h j
Bladder Kidney Spleen
Sprr1a Cd74 Rbm3
Ly6d Tmsb4x Apoe Lgals3 B2m Lgals1
Wfdc2 Rps4x Txn1 Gsta4 Rps7 Ly6a
Gsto1 Rpl10 Ccl5 Krt18 Rps19 AW112010 Sfn Rps13 S100a6 Krt8 Rpl12 Gapdh
Areg Rplp0 Cybb Aqp3 H2-Ab1 H2afz
Igfbp2 Ly6e Igj Krt15 Rpl13a S100a11
Gstm1 Rps3a Gpx4
Krt19 H2-D1 Prr13
Fxyd3 Rps15a Sec61g
Akr1b8 Rpl17 Itgb1 Foxq1 Rps9 Hbb-bs
Cldn4 Rps6 Txndc5
Krt7 Rpsa Hmgb2
Pcolce Sostdc1 Dapl1
Ppic Id1 Cd79b Id3 Rn45s Klf2
Col6a2 Fabp3 Pyhin1
Gadd45g Tm4sf1 Cd53
Tuba1a Kng2 Fcer2a
Fos Atp1b1 Tmsb10 Dcn Mt1 Satb1
Col5a2 Enpp2 Ddit4
Htra1 Klk1 Vpreb3 Car3 Defb1 Btg1
Rcn3 Spp2 Ly6d Mgp Slc5a3 Ltb
Lgals1 Pck1 Limd2 Col6a1 Atp1a1 Ets1 Col1a1 Ppp1r1a Sell
Serpinh1 Wfdc15b Shisa5
Sparc Umod Tsc22d3
Col1a2 Slc12a1 Zfp36l2
Col3a1 Egf Ifi27l2a
–0.10 –0.05 0.00 0.05 –0.050 –0.025 0.000 0.025 –0.02 0.00 0.02
Age coefficient Age coefficient
by the results of differential gene expression analysis, suggesting that In the spleen, the proportion of T cells decreases with age while the
the expression of Umod—which encodes uromodulin, the most abun- relative amount of plasma cells increases (Fig. 2i). This is supported
dant protein in urine31—is also reduced across the tissue. The protein by the upregulation of B cell and plasma cell marker genes (Cd79a and
uromodulin is produced by the epithelial cells that line the thick ascend- Jchain (also known as Igj), respectively; Fig. 2j, Supplementary Table 6)
ing limb, and therefore—given the relative decrease in the proportion and the downregulation of Cd3d (Fig. 2j, Supplementary Table 6). Simi-
of epithelial cells in the ascending and the thick ascending limb—our larly, in the mammary gland we observed a decline of the T cell popula-
results suggest that normal kidney functions are impaired32 (Fig. 2g, tion (Extended Data Fig. 5c). Age-related decline of T cell populations
bottom, Fig. 2h, Supplementary Table 6). As with Atp1a1, we see that the has been associated with increased risk of infectious disease and can-
expression of Umod increases in a cell type that becomes less abundant cer33, and our results suggest that such a decline might also occur in
with age, leading to an overall reduction of its expression in the organ. the spleen and the mammary gland. Moreover, genes encoding AP1
592 | Nature | Vol 583 | 23 July 2020
noitroporp
epyt
llec evitaleR
Bladder cell Bladder urothelial cell 0.8 0.7
0.6
0.5
0.4 0.3
0.2
0 5 10 15 20 25 Age (months)
0.05
0.04 0.03
0.02
0.01
0.00
0 5 10 15 20 25 30
noitroporp
epyt
llec
evitaleR
Kidney capillary endothelial cell Kidney mesangial cell
0.04
0.03
0.02
0.01
0.00
0 5 10 15 20 25 30
0.025
0.020
0.015
0.010
0.005
0.000
0 5 10 15 20 25 30
Age (months)
noitroporp
epyt
llec
evitaleR
Kidney loop of Henle ascending limb epithelial cell Kidney loop of Henle thick ascending limb epithelial cell
0.200
0.175
0.150
0.125 0.100
0.075
0.050
0.025
0.000
0 5 10 15 20 25 30
Age (months)
0.07
0.06
0.05
0.04
0.03
0.02 0.01
0.00
0 5 10 15 20 25 30
Age (months)
noitroporp
epyt
llec
evitaleR
a
c
i Spleen plasma cell Spleen T cell
0.25
0.20
0.15
0.10
0.05
0.00
0 5 10 15 20 25 30
Age (months)
sllec
fo noisserpxe
naeM
SCAF
ni a2nkdC
gnisserpxe
b
1 3 18 21 24 30 Age (months)
d g
gnisserpxe
sllec
fo noitcarF
telpord
ni
a2nkdC
P = 1.6 × 10–4 P = 2.3 × 10–7 P = 6.5 × 10–7 P = 0.51 P = 1.1 × 10–4
1 3 18 21 24 30
sllec
fo noisserpxe
naeM
telpord
ni a2nkdC
gnisserpxe
P = 4.7 × 10–3
P = 2.4 × 10–10 P = P 7. 3 = × 1 . 1 6 0 × –5 10–5
P = 2.3 × 10–15 P = 0.41 P = 1.7 × 10–3
10 10
8 8 6 6
4 4
2 2
0 0
3 18 24
Age (months)
gnisserpxe
sllec
fo noitcarF
SCAF
ni
a2nkdC
P = 1.6 × 10–9 100 P = 1.8 × 10–14 100
10–1 10–1
10–2 10–2
3 18 24 Age (months)
Age (months)
Age coefficient
Fig. 2 | Cellular changes during ageing. a, b, Bar plot showing the fractions of (i, right) change significantly with age. P < 0.05 and r2 > 0.7 for a hypothesis test
cells expressing Cdkn2a in each age group for FACS (a) and droplet (b) with the null hypothesis that the slope is zero, using two-sided Wald test with
experiments. c, d, Bar plot of the median expression of Cdkn2a for the cells that t-distribution of the test statistic. f, h, j, Top 20 upregulated and top 20
do express the gene at each age group for FACS (c) and droplet (d) experiments. downregulated genes in bladder (f), kidney (h) and spleen (j) computed using
The y axis shows log-transformed and scaled values. All data are expressed as MAST51, treating age as a continuous covariate while controlling for sex and
mean ± s.d. with individual data points shown. P values were obtained using a technology. Genes were classified as significant under a false-discovery rate
Mann–Whitney–Wilcoxon rank-sum two-sided test. n = 44,518, 34,027 and (FDR) threshold of 0.01 and an age coefficient threshold of 0.005
31,551 individual cells for FACS at 3, 18 and 24 months, respectively; n = 25,980, (corresponding to an approximately 10%-fold change). For f, n = 970, 3,804,
45,602, 44,645, 35,828, 37,660 and 55,674 individual cells for droplet at 1, 3, 18, 2,739 and 3,864 individual cells for bladder at 1, 3, 18 and 24 months,
21, 24 and 30 months, respectively. e, g, i, The relative abundances of bladder respectively; for h, n = 2,488, 2,832, 3,806, 2,257, 6,384 and 5,713 individual
cells (e, left) and bladder urothelial cells (e, right), kidney capillary endothelial cells for kidney at 1, 3, 18, 21, 24 and 30 months, respectively; for j, n = 2,986,
cells (g, top left), mesangial cells (g, top right), loop of Henle ascending limb 8,839, 7,141, 6,395, 5,245 and 8,946 individual cells for spleen at 1, 3, 18, 21, 24
epithelial cells (g, bottom left) and loop of Henle thick ascending limb and 30 months, respectively. The P values for the cell type compositional
epithelial cells (g, bottom right), and spleen plasma cells (i, left) and T cells changes are shown in Supplementary Table 5.
transcription factors34 (Junb, Jund and Fos) were upregulated with age 18 m–3 m gene set 18 m–3 m ERCC 24 m–3 m gene set 24 m–3 m ERCC
(Extended Data Fig. 5d, Supplementary Table 6), consistent with the a All cells b Endothelial cells c Immune cells
4.0 4.0 4.0
observation that normal involution of the mammary gland is accom-
3.0 3.0 3.0
panied by increased expression of this gene family35.
The tissue composition of the liver also changes with age. We 2.0 2.0 2.0
observed an age-related decrease in the relative number of hepato- 1.0 1.0 1.0
cytes (Extended Data Fig. 6a–d), which is supported by the reduction in 0.0 0.0 0.0
−1.0 0.0 0.5 1.0 1.5 2.0 −1.0 0.0 0.5 1.0 1.5 2.0 −1.0 0.0 0.5 1.0 1.5 2.0
the expression of albumin (Alb; Extended Data Fig. 6e, Supplementary
Table 6). Differential gene expression analysis revealed an increased d Parenchymal cells e Stem/progenitor cells f Stromal cells
immune signature, as illustrated by the overexpression of H2-Aa, 4.0 4.0 4.0
H2-Ab1, H2-D1, H2-Eb1, Cd74, Lyz2 and others (Extended Data Fig. 6e). 3.0 3.0 3.0
Previous findings suggested that pro-inflammatory macrophages drive 2.0 2.0 2.0
cellular senescence, and identified the gene Il1b as showing markedly
1.0 1.0 1.0
different expression in the liver with age12 (Extended Data Fig. 6f). We
0.0 0.0 0.0
performed in situ RNA staining in liver Kupffer cells (Extended Data −1.0 0.0 0.5 1.0 1.5 2.0 −1.0 0.0 0.5 1.0 1.5 2.0 −1.0 0.0 0.5 1.0 1.5 2.0
Fig. 6g) with Clec4f and found that the number of Clec4f-positive cells Pairwise difference of mean number of mutations in gene set and ERCC spike-in
controls across all tissues
does not change with age, consistent with the results of the tissue com-
position analysis (Extended Data Fig. 6h, Supplementary Table 7). How- Fig. 3 | Mutational burden across tissues in ageing mice. a–f, Distribution of
ever, when co-staining with Il1b, we found that the number of cells the difference of the mean mutation in the gene set (and ERCC spike-in
expressing both Clec4f and Il1b increased with age (Extended Data controls) per cell between 24 months and 3 months and between 18 months and
Fig. 6h–j). The expression of Il1b is low under normal physiological 3 months for all tissues and cells (a) and with the cell types split into five
conditions36. Specific blocking of IL1-RI in hepatocytes has been shown functional groups: endothelial cells (b), immune cells (c), parenchymal cells (d),
stem/progenitor cells (e) and stromal cells (f). Filled and solid line distributions
to attenuate cell death after injury, supporting the idea that increased
correspond to the mean mutation difference in gene set. White and dashed line
expression of Il1b in Kupffer cells is typically a poor prognostic37. Liver
distributions correspond to the mean mutation difference in ERCC spike-in
sinusoidal endothelial cells (LSECs) have a unique role in immune
controls. Note that the mean mutation difference in ERCC spike-in controls
defence, being the main carriers of the mannose receptor (MRC1) in
overlaps for both age groups. The y axis corresponds to the kernel density
this organ38 (Extended Data Fig. 6k). We identified increased expression estimation (arbitrary units).
of Mrc1 with age in Kupffer cells, whereas the overall expression of Mrc1
in liver endothelial cells decreased with age (Supplementary Table 6).
By performing in situ RNA staining for Mrc1 alongside the classical assembled for 6,050 cells (Fig. 4a, Extended Data Fig. 9a) and T cell
LSEC marker Pecam1 (Extended Data Fig. 6l, Supplementary Table 7), receptors for 6,000 cells (Fig. 4b, Extended Data Fig. 9b). The number
we found that the number of Mrc1-expressing LSECs increased with age of cells with assembled B cell receptors was 1,818 for 3-month-old,
(Extended Data Fig. 6m–o). Although Mrc1 expression did not increase 1,356 for 18-month-old and 2,876 for 24-month-old mice. We parsed
with age in LSECs (Supplementary Table 6), the overall number of cells the singlecell-ige43 output to define B cell clonotypes on the basis of
expressing Mrc1 did increase significantly with age (Extended Data the sequence of the assembled B cell receptor (Supplementary Table 9)
Fig. 6n). LSECs have been found to have a reduced endocytic capacity and found that, whereas most of the cells at 3 months were not part of
in aged livers, and it has been suggested that LSECs proliferate after a clone (9% were part of a clonal family), the number of B cells belong-
injury or that bone-marrow-derived LSEC progenitors are recruited to ing to a clonotype doubled at 18 months (20%) when compared to
the liver. This suggests that changes in the gene signatures of LSECs 3 months, and doubled again from 18 months to 24 months (around
with age are closely linked with the function of these cells in immune 38%). The number of cells with assembled T cell receptors was roughly
response. equal between 3-month-old, 18-month-old and 24-month-old mice
Genomic instability is among the most widely studied hallmarks of (2,076, 2,056 and 1,868 cells, respectively). Clonotype assignment
ageing1, and full-length transcript data enables analysis of the accumu- is part of the output obtained by TraCeR44 (Supplementary Table 9).
lation of somatic mutations with age. We used the Genome Analysis Notably, only around 3% (55 out of 1,895) of the cells at 3 months were
ToolKit39 to identify single-nucleotide polymorphisms across all FACS part of a clone. At 18 months and 24 months, this value increased to
samples simultaneously40,41 (Supplementary Table 8). We focused on around 23% (479 out of 2,056) and around 20% (348 out of 1,780) of
genes that were expressed in at least 75% of cells for each age group the cells, respectively, again indicating an increase in clonality of the
within a particular tissue, and observed an age-related increase in T cell repertoire at later ages. These changes in clonality for both
the number of mutations across all of the organs we analysed (Fig. 3, B cell and T cell repertoires are noteworthy, because they suggest
Extended Data Fig. 7a, c, e)—tongue and bladder were the most affected. that the immune system of a 24-month-old mouse is less likely to
We controlled for sequencing coverage and gene expression levels respond to new pathogens. This corroborates literature reports sug-
(Extended Data Fig. 8a, c, e), and verified that the number of muta- gesting that older individuals have a higher vulnerability to new infec-
tions exceeded those expected from amplification and sequencing tions and lower benefits from vaccination compared with younger
errors, which can be estimated using External RNA Controls Consor- individuals45,46.
tium (ERCC) controls that were spiked into each well42 (Fig. 3, Extended Finally, we computed an overall diversity score to identify which
Data Figs. 7b, d, f, 8b, d, f). Despite the fact that it is difficult to infer cell types were more susceptible to changes with age (Extended Data
absolute genome-wide mutation rates from the transcriptome, which Fig. 10). The diversity score is computed as the Shannon entropy of
is known to overstate apparent mutational rates for various reasons42, the cluster assignment and then regressed against age to provide a
the observed trend is a useful indirect estimate of mutational frequency P value (see Methods). We observed significant changes in diversity
and genome stability. for cells of the immune system that originate from the brain and the
Ageing also affects the immune system2, so we analysed clonal rela- kidney (Fig. 4c, Extended Data Fig. 11a, b). These results were not con-
tionships between B cells and T cells throughout the organism. We founded by the number of genes expressed per cell (Extended Data
computationally reconstructed the sequence of the B cell receptor Fig. 11c, d). In brain myeloid microglial cells, the majority of young
and the T cell receptor for B cells and T cells present in the FACS data (3 month) microglia occupy clusters 1 and 6, whereas old (18 month and
using singlecell-ige and TraCeR, respectively43,44. B cell receptors were 24 month) microglia constitute the vast majority of cells in clusters 10,
Nature | Vol 583 | 23 July 2020 | 593
Article
a 6,050 cells with assembled BCR b 6,000 cells with assembled TCR c
38% 91% 3 m Si n (n g l = et o 1, n 8 1 B 8 c c e e ll lls) 81% 19% 97% 3 m Si n (n g l = e t 2 o , n 0 7 T 6 c c e e ll lls) Kidney macr (d o r p o h p a le g t e ) * * * *
Clonal families Clonal families Brain myeloid
18 m (n = 1,356 cells) 18 m (n = 2,056 cells) Microglial cell (FACS) * **
9% Singleton B cell Singleton T cell 0.025 Resolution 0.3 0.5 0.7
62% 80% 24
C
S m
l
i
o
n g
n
(n
a
le
l
= t
f
o
a
2 n
m
, 8 B
il
7
i e
c 6
s
e c ll ells) 23% 3% 24
C
S m
l
i
o
n g
n
(n
a
le
l
= t
f
o
a
1 n
m
, 8 T
i
6
l i
c 8
e
e
s
c ll ells) 0
0
.
.
0
0
0
1
5
5
Method
Louvai
L
n eide
L
n ouvai
L
n eide
L
n ouvai
L
n eiden
20% Clonal families 77% Clonal families
d
UMAP1
12 and 14 (Fig. 4d). Trajectory analysis suggests that young microglia for understanding many aspects of the changes in cell biology that
go through an intermediate state, represented by the clusters mostly occur in mammals during their lifespan.
occupied by 18-month microglial cells, before acquiring the signature
of old microglia (Extended Data Fig. 11e). Clusters 10, 12 and 14 mainly
Online content
comprise 18-month and 24-month microglia. These cells upregulate
major histocompatibility complex (MHC) class I genes (H2-D1, H2-K1 Any methods, additional references, Nature Research reporting sum-
and B2m), along with genes associated with degenerative disease (for maries, source data, extended data, supplementary information,
example, Fth1)47,48. When compared with clusters 1 and 6—which con- acknowledgements, peer review information; details of author con-
tain mostly 3-month microglia—gene expression in clusters 10, 12 and tributions and competing interests; and statements of data and code
14 is enriched with interferon responsive or regulatory genes (for exam- availability are available at https://doi.org/10.1038/s41586-020-2496-1.
ple, Oasl2, Oas1a, Ifit3, Rtp4, Bst2, Stat1, Irf7, Ifitm3, Usp18, Ifi204 and
Ifit2), suggesting an expansion of this small pro-inflammatory subset 1. López-Otín, C., Blasco, M. A., Partridge, L., Serrano, M. & Kroemer, G. The hallmarks of
of microglia in the ageing brain49. Moreover, the list of differentially aging. Cell 153, 1194–1217 (2013).
expressed genes between ‘young’ and ‘old’ clusters resembles the pre- 2. Nikolich-Žugich, J. The twilight of immunity: emerging concepts in aging of the immune
system. Nat. Immunol. 19, 10–19 (2018).
viously reported Alzheimer’s disease-specific microglial signature47, 3. Campisi, J. Aging, cellular senescence, and cancer. Annu. Rev. Physiol. 75, 685–705
with 55 out of the top 200 differential expressed genes shared between (2013).
4. Vijg, J. & Suh, Y. Genome instability and aging. Annu. Rev. Physiol. 75, 645–668 (2013).
the two differential gene expression lists (Fig. 4e, Supplementary
5. The Tabula Muris Consortium. Single-cell transcriptomics of 20 mouse organs creates a
Table 10). Regarding kidney macrophages, we found two clusters for Tabula Muris. Nature 562, 367–372 (2018).
which the composition changed markedly with age. Cluster 10 is pri- 6. Polański, K. et al. BBKNN: fast batch alignment of single cell transcriptomes.
Bioinformatics 36, 964–965 (2020).
marily composed of cells from 1-month-old and 3-month-old mice,
7. Blondel, V. D., Guillaume, J.-L., Lambiotte, R. & Lefebvre, E. Fast unfolding of communities
whereas cluster 13 is mostly composed of cells from18-month-old, in large networks. J. Stat. Mech. P10008 (2008).
21-month-old, 24-month-old and 30-month old mice (Fig. 4f). Dif- 8. Traag, V. A., Waltman, L. & van Eck, N. J. From Louvain to Leiden: guaranteeing
well-connected communities. Sci. Rep. 9, 5233 (2019).
ferential gene expression revealed that cluster 10 is enriched for an
9. Schaum, N. et al. The murine transcriptome reveals global aging nodes with organ-specific
M2-macrophage gene signature (for example, Il10, H2-Eb1, H2-Ab1, phase and amplitude. Preprint at https://www.biorxiv.org/content/10.1101/662254v1
H2-Aa, Cd74, C1qa, Cxcl16, Hexb, Cd81, C1qb and Cd72) whereas cluster (2019).
13 resembles a M1-proinflammatory macrophage state50 (for example, 10. Rayess, H., Wang, M. B. & Srivatsan, E. S. Cellular senescence and tumor suppressor gene
p16. Int. J. Cancer 130, 1715–1725 (2012).
Hp, Itgal, Msrb1 and Gngt2) (Extended Data Fig. 11f, Supplementary 11. Hernandez-Segura, A., Nehme, J. & Demaria, M. Hallmarks of cellular senescence. Trends
Table 10). Cell Biol. 28, 436–453 (2018).
12. Covarrubias, A. J. et al. Aging-related inflammation driven by cellular senescence
The Tabula Muris Senis is a comprehensive resource for the
enhances NAD consumption via activation of CD38+ pro-inflammatory macrophages.
cell biology community that offers a detailed molecular and Preprint at https://www.biorxiv.org/content/10.1101/609438v2 (2019).
cell-type-specific portrait of ageing. We view such a cell atlas as an 13. Nagano, T. et al. Identification of cellular senescence-specific genes by comparative
transcriptomics. Sci. Rep. 6, 31758 (2016).
essential companion to the genome: the genome provides a blue-
14. Carnero, A. in Cell Senescence. Methods in Molecular Biology (Methods and Protocols)
print for the organism, but does not explain how genes are used in Vol. 965 (eds Galluzzi, L., Vitale, I., Kepp, O. & Kroemer, G.) (Humana, 2013).
a cell-type-specific manner or how the usage of genes changes over 15. Wang, A. S. & Dreesen, O. Biomarkers of cellular senescence and skin aging. Front. Genet.
9, 247 (2018).
the lifetime of the organism. The cell atlas provides a deep charac-
16. Vernier, M. et al. Regulation of E2Fs and senescence by PML nuclear bodies. Genes Dev.
terization of phenotype and physiology and serves as a reference 25, 41–50 (2011).
594 | Nature | Vol 583 | 23 July 2020
2PAMU
FACS: brain myeloid microglial cell e FACS: brain myeloid microglial cell f Droplet: kidney macrophage
Cluster 12 Cluster 1
(98 cells) (2,464 cells)
Cluster 13
(513 cells)
Cluster 6
(1,004 cells)
Cluster 14 Cluster 10
(88 cells) (753 cells)
3 m Alzheimer’s disease signature Young (1 m, 3 m)
1 2 8 4 m m Healthy microglia signature Old (18 m, 21 m, 24 m, 30 m)
UMAP1 UMAP1
2PAMU 2PAMU
Fig. 4 | The ageing immune system. a, b, B cell (a) and T cell (b) clonal families. change with age; that of the coloured clusters does change with age. e, UMAP
The pie charts show the proportion of singleton B cells and B cells and that are plot of the brain myeloid microglial cells when scored using the microglia
part of clonal families (a) and singleton T cells and T cells that are part of clonal Alzheimer’s disease signature (Supplementary Table 10). n = 4,532, 4,461 and
families (b) at 3 months, 18 months and 24 months. See Extended Data Fig. 9 for 4,424 individual microglia cells for brain myeloid at 3 months, 18 months and
clonal networks. BCR, B cell receptor; TCR, T cell receptor. c, Diversity scores 24 months, respectively. f, UMAP plot of the kidney macrophage Leiden
for the two cell types for which this score changes significantly with age. clusters (numbers) coloured by age group. n = 62, 139, 264, 105, 284 and 553
d, UMAP plot of the brain myeloid microglial cell Leiden clusters (numbers) individual macrophage cells for kidney at 1, 3, 18, 21, 24 and 30 months,
coloured by age. The relative cell composition of faded clusters does not respectively.
17. Dreesen, O. et al. Lamin B1 fluctuations have differential effects on cellular proliferation The Tabula Muris Consortium
and senescence. J. Cell Biol. 200, 605–617 (2013).
18. Shah, P. P. et al. Lamin B1 depletion in senescent cells triggers large-scale changes in Nicole Almanzar1, Jane Antony2, Ankit S. Baghel2, Isaac Bakerman2,3,4, Ishita Bansal2, Ben A.
gene expression and the chromatin landscape. Genes Dev. 27, 1787–1799 (2013).
Barres5, Philip A. Beachy2,6,7,8, Daniela Berdnik9, Biter Bilen10, Douglas Brownfield6, Corey
19. Li, P. et al. The inflammatory cytokine TNF-α promotes the premature senescence of
rat nucleus pulposus cells via the PI3K/Akt signaling pathway. Sci. Rep. 7, 42938 Cain11, Charles K. F. Chan12, Michelle B. Chen13, Michael F. Clarke2, Stephanie D. Conley14,
(2017). Spyros Darmanis14 ✉, Aaron Demers14, Kubilay Demir2,7, Antoine de Morree10, Tessa Divita14,
20. Saunders, L. R. & Verdin, E. Sirtuins: critical regulators at the crossroads between cancer Haley du Bois9, Hamid Ebadi14, F. Hernán Espinoza6, Matt Fish2,7,8, Qiang Gan10, Benson M.
and aging. Oncogene 26, 5489–5504 (2007). George2, Astrid Gillich6, Rafael Gòmez-Sjöberg14, Foad Green14, Geraldine Genetiano14,
21. Lee, S.-H., Lee, J.-H., Lee, H.-Y. & Min, K.-J. Sirtuin signaling in cellular senescence and Xueying Gu8, Gunsagar S. Gulati2, Oliver Hahn10, Michael Seamus Haney10, Yan Hang8,
aging. BMB Rep. 52, 24–34 (2019). Lincoln Harris14, Mu He15, Shayan Hosseinzadeh14, Albin Huang10, Kerwyn Casey Huang13,14,16,
22. van den Brink, S. C. et al. Single-cell sequencing reveals dissociation-induced gene Tal Iram10, Taichi Isobe2, Feather Ives14, Robert C. Jones13, Kevin S. Kao2, Jim Karkanias14,
expression in tissue subpopulations. Nat. Methods 14, 935–936 (2017).
Guruswamy Karnam17, Andreas Keller10,18, Aaron M. Kershner2, Nathalie Khoury10, Seung K.
23. Tung, P.-Y. et al. Batch effects and the effective design of single-cell gene expression
studies. Sci. Rep. 7, 39921 (2017). Kim8,19, Bernhard M. Kiss2,20, William Kong2, Mark A. Krasnow6,7, Maya E. Kumar21,22, Christin S.
24. Nguyen, Q. H., Pervolarakis, N., Nee, K. & Kessenbrock, K. Experimental considerations for Kuo1, Jonathan Lam8, Davis P. Lee9, Song E. Lee10, Benoit Lehallier10, Olivia Leventhal9, Guang
single-cell RNA sequencing approaches. Front. Cell Dev. Biol. 6, 108 (2018). Li4,23, Qingyun Li5, Ling Liu10, Annie Lo14, Wan-Jin Lu2,6, Maria F. Lugo-Fagundo9, Anoop
25. Daly, D. M. et al. Age-related changes in afferent pathways and urothelial function in the Manjunath2, Andrew P. May14, Ashley Maynard14, Aaron McGeever14, Marina McKay14, M.
male mouse bladder. J. Physiol. (Lond.) 592, 537–549 (2014). Windy McNerney24,25, Bryan Merrill16, Ross J. Metzger26,27, Marco Mignardi13, Dullei Min1,
26. Burmeister, D. M., AbouShwareb, T., Bergman, C. R., Andersson, K.-E. & Christ, G. J. Ahmad N. Nabhan6, Norma F. Neff14, Katharine M. Ng6, Patricia K. Nguyen2,3,4, Joseph Noh2,
Age-related alterations in regeneration of the urinary bladder after subtotal cystectomy. Roel Nusse6,7,8, Róbert Pálovics10, Rasika Patkar17, Weng Chuan Peng8,38, Lolita Penland14,
Am. J. Pathol. 183, 1585–1595 (2013).
Angela Oliveira Pisco14, Katherine Pollard28, Robert Puccinelli14, Zhen Qi2, Stephen R.
27. A bl n a d d e d r e s r s o is n c , h K e . m -E i . a , , B a o n e d d t a k g je in r, g D b . l B a . d & d e Fo r r d m ys a f n u , n A c . t i T o h n e . l T in h k e r b . e A t d w v e . U en ro v l. a 9 sc , u 11 l – a 2 r 7 d ( y 2 s 0 fu 17 n ) c . tion, Quake13,14 ✉, Thomas A. Rando9,10,29, Eric J. Rulifson8, Nicholas Schaum2,10, Joe M. Segal17,
28. Suskind, A. M. The aging overactive bladder: a review of aging-related changes from the Shaheen S. Sikandar2, Rahul Sinha2,30,31,32, Rene V. Sit14, Justin Sonnenburg14,16, Daniel
brain to the bladder. Curr. Bladder Dysfunct. Rep. 12, 42–47 (2017). Staehli10, Krzysztof Szade2,33, Michelle Tan14, Weilun Tan14, Cristina Tato14, Krissie Tellez8,
29. Zhang, D. et al. Downregulation of ATP1A1 promotes cancer development in renal cell Laughing Bear Torrez Dulgeroff2, Kyle J. Travaglini6, Carolina Tropini16,39,40,41, Margaret Tsui17,
carcinoma. Clin. Proteomics 14, 15 (2017). Lucas Waldburger14, Bruce M. Wang17, Linda J. van Weele2, Kenneth Weinberg1, Irving L.
30. Isaka, Y. Epidermal growth factor as a prognostic biomarker in chronic kidney diseases. Weissman2,30,31,32, Michael N. Wosczyna10, Sean M. Wu2,3,23, Tony Wyss-Coray9,10,29,34 ✉, Jinyi
Ann. Transl. Med. 4, S62 (2016). Xiang1, Soso Xue13, Kevin A. Yamauchi14, Andrew C. Yang13, Lakshmi P. Yerra10, Justin
31. Devuyst, O., Olinger, E. & Rampoldi, L. Uromodulin: from physiology to rare and complex
Youngyunpipatkul14, Brian Yu14, Fabio Zanini13, Macy E. Zardeneta9, Alexander Zee14, Chunyu
kidney disorders. Nat. Rev. Nephrol. 13, 525–544 (2017).
32. Tokonami, N. et al. Uromodulin is expressed in the distal convoluted tubule, where it is Zhao14, Fan Zhang26,27, Hui Zhang9, Martin Jinye Zhang35,36, Lu Zhou5 & James Zou14,35,37
critical for regulation of the sodium chloride cotransporter NCC. Kidney Int. 94, 701–715
(2018). 1Department of Pediatrics, Pulmonary Medicine, Stanford University School of Medicine,
33. Palmer, S., Albergante, L., Blackburn, C. C. & Newman, T. J. Thymic involution and rising Stanford, CA, USA. 2Institute for Stem Cell Biology and Regenerative Medicine, Stanford
disease incidence with age. Proc. Natl Acad. Sci. USA 115, 1883–1888 (2018). University School of Medicine, Stanford, CA, USA. 3Stanford Cardiovascular Institute,
34. Shen, Q. et al. The AP-1 transcription factor regulates postnatal mammary gland
Stanford University School of Medicine, Stanford, CA, USA. 4Division of Cardiovascular
development. Dev. Biol. 295, 589–603 (2006).
Medicine, Department of Medicine, Stanford University School of Medicine, Stanford, CA,
35. G co ir n n t i r u ib s, u N te ., s E t d o w m a o rd u s s , e Y m . J a . m K. m & a D r a y v g is la , n R d . J r . e T m he o d c e JU lin N g N d H u 2 r - i t n e g rm in in vo a l l u k t i i n o a n s . e C ( e JN ll K D ) e p a a th th D w if a f y e r. USA. 5Department of Neurobiology, Stanford University School of Medicine, Stanford, CA,
25, 1702–1715 (2018). USA. 6Department of Biochemistry, Stanford University School of Medicine, Stanford, CA,
36. Tan, Q. et al. The role of IL-1 family members and Kupffer cells in liver regeneration. USA. 7Howard Hughes Medical Institute, Chevy Chase, MD, USA. 8Department of
BioMed Res. Int. 2016, 6495793 (2016). Developmental Biology, Stanford University School of Medicine, Stanford, CA, USA. 9Veterans
37. Gehrke, N. et al. Hepatocyte-specific deletion of IL1-RI attenuates liver injury by blocking Administration Palo Alto Healthcare System, Palo Alto, CA, USA. 10Department of Neurology
IL-1 driven autoinflammation. J. Hepatol. 68, 986–995 (2018). and Neurological Sciences, Stanford University School of Medicine, Stanford, CA, USA. 11Flow
38. Liu, Y., Gardner, C. R., Laskin, J. D. & Laskin, D. L. Classical and alternative activation of rat
Cytometry Core, Veterans Administration Palo Alto Healthcare System, Palo Alto, CA, USA.
hepatic sinusoidal endothelial cells by inflammatory stimuli. Exp. Mol. Pathol. 94, 160–167
12Department of Surgery, Division of Plastic and Reconstructive Surgery, Stanford University,
(2013).
39. McKenna, A. et al. The Genome Analysis Toolkit: a MapReduce framework for analyzing Stanford, CA, USA. 13Department of Bioengineering, Stanford University, Stanford, CA, USA.
next-generation DNA sequencing data. Genome Res. 20, 1297–1303 (2010). 14Chan Zuckerberg Biohub, San Francisco, CA, USA. 15Department of Physiology, University of
40. DePristo, M. A. et al. A framework for variation discovery and genotyping using California, San Francisco, CA, USA. 16Department of Microbiology & Immunology, Stanford
next-generation DNA sequencing data. Nat. Genet. 43, 491–498 (2011). University School of Medicine, Stanford, CA, USA. 17Department of Medicine and Liver Center,
41. Auwera, G. A. et al. From FastQ data to high-confidence variant calls: the Genome University of California San Francisco, San Francisco, CA, USA. 18Clinical Bioinformatics,
Analysis Toolkit best practices pipeline. Curr. Protoc. Bioinformatics 43, 11.10.1–11.10.33 Saarland University, Saarbrücken, Germany. 19Department of Medicine and Stanford Diabetes
(2013). Research Center, Stanford University, Stanford, CA, USA. 20Department of Urology, Stanford
42. Zook, J. M., Samarov, D., McDaniel, J., Sen, S. K. & Salit, M. Synthetic spike-in standards
University School of Medicine, Stanford, CA, USA. 21Sean N. Parker Center for Asthma and
improve run-specific systematic error analysis for DNA and RNA sequencing. PLoS ONE 7,
e41356 (2012). Allergy Research, Stanford University School of Medicine, Stanford, CA, USA. 22Department of
43. Croote, D., Darmanis, S., Nadeau, K. C. & Quake, S. R. High-affinity allergen-specific human Medicine, Division of Pulmonary and Critical Care, Stanford University School of Medicine,
antibodies cloned from single IgE B cell transcriptomes. Science 362, 1306–1309 Stanford, CA, USA. 23Department of Developmental Biology, University of Pittsburgh School
(2018). of Medicine, Pittsburgh, PA, USA. 24Mental Illness Research Education and Clinical Center,
44. Stubbington, M. J. T. et al. T cell fate and clonality inference from single-cell Veterans Administration Palo Alto Healthcare System, Palo Alto, CA, USA. 25Department of
transcriptomes. Nat. Methods 13, 329–332 (2016). Psychiatry, Stanford University School of Medicine, Stanford, CA, USA. 26Vera Moulton Wall
45. Goronzy, J. J. & Weyand, C. M. Understanding immunosenescence to improve responses
Center for Pulmonary and Vascular Disease, Stanford University School of Medicine, Stanford,
to vaccines. Nat. Immunol. 14, 428–436 (2013).
CA, USA. 27Department of Pediatrics, Division of Cardiology, Stanford University School of
46. Goronzy, J. J. & Weyand, C. M. Successful and maladaptive T cell aging. Immunity 46,
364–378 (2017). Medicine, Stanford, CA, USA. 28Department of Epidemiology and Biostatistics, University of
47. Keren-Shaul, H. et al. A unique microglia type associated with restricting development of California, San Francisco, CA, USA. 29Paul F. Glenn Center for the Biology of Aging, Stanford
Alzheimer’s disease. Cell 169, 1276–1290.e17 (2017). University School of Medicine, Stanford, CA, USA. 30Department of Pathology, Stanford
48. Li, Q. et al. Developmental heterogeneity of microglia and brain myeloid cells revealed by University School of Medicine, Stanford, CA, USA. 31Ludwig Center for Cancer Stem Cell
deep single-cell RNA sequencing. Neuron 101, 207–223.e10 (2019). Research and Medicine, Stanford University School of Medicine, Stanford, CA, USA.
49. Hammond, T. R. et al. Single-cell RNA sequencing of microglia throughout the mouse 32Stanford Cancer Institute, Stanford University School of Medicine, Stanford, CA, USA.
lifespan and in the injured brain reveals complex cell-state changes. Immunity 50, 33Department of Medical Biotechnology, Faculty of Biochemistry, Biophysics and
253–271.e6 (2019).
Biotechnology, Jagiellonian University, Krakow, Poland. 34Wu Tsai Neurosciences Institute,
50. Jablonski, K. A. et al. Novel markers to delineate murine M1 and M2 macrophages. PLoS
ONE 10, e0145342 (2015). Stanford University School of Medicine, Stanford, CA, USA. 35Department of Electrical
51. Finak, G. et al. MAST: a flexible statistical framework for assessing transcriptional changes Engineering, Stanford University, Palo Alto, CA, USA. 36Department of Epidemiology, Harvard
and characterizing heterogeneity in single-cell RNA sequencing data. Genome Biol. 16, T.H. Chan School of Public Health, Boston, MA, USA. 37Department of Biomedical Data
278 (2015). Science, Stanford University, Palo Alto, CA, USA. 38Princess Máxima Center for Pediatric
Oncology, Utrecht, The Netherlands. 39School of Biomedical Engineering, University of British
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in Columbia, Vancouver, British Columbia, Canada. 40Department of Microbiology and
published maps and institutional affiliations. Immunology, University of British Columbia, Vancouver, British Columbia, Canada. 41Humans
and the Microbiome Program, Canadian Institute for Advanced Research, Toronto, Ontario,
© The Author(s), under exclusive licence to Springer Nature Limited 2020 Canada. ✉e-mail: spyros.darmanis@czbiohub.org; steve@quake-lab.org; twc@stanford.edu
Nature | Vol 583 | 23 July 2020 | 595
Article
Methods Module. Twelve cycles were used for cDNA amplification and sample
index PCR. Amplified cDNA and final libraries were evaluated on a Frag-
All data, protocols, analysis scripts and an interactive data browser ment Analyzer using a High Sensitivity NGS Analysis Kit (Advanced
are publicly available. Analytical). The average fragment length of 10x cDNA libraries was
quantitated on a Fragment Analyzer (AATI), and by qPCR with the Kapa
Experimental procedures Library Quantification kit for Illumina. Each library was diluted to 2
Mice and organ collection. Male and virgin female C57BL/6JN mice nM, and equal volumes of 16 libraries were pooled for each NovaSeq
were shipped from the National Institute on Ageing colony at Charles sequencing run. Pools were sequenced with 100 cycle run kits with 26
River (housed at 19–23 °C) to the Veterinary Medical Unit (VMU; housed bases for Read 1, 8 bases for Index 1, and 90 bases for Read 2 (Illumina
at 20–24 °C)) at the VA Palo Alto (VA). At both locations, mice were 20012862). A PhiX control library was spiked in at 0.2 to 1%. Libraries
housed on a 12 h/12 h light/dark cycle and provided with food and water were sequenced on the NovaSeq 6000 Sequencing System (Illumina).
ad libitum. The diet at Charles River was NIH-31, and at the VA VMU was
Teklad 2918. Littermates were not recorded or tracked, and mice were In situ RNA hybridization and quantification. In situ RNA hybridiza-
housed at the VA VMU for no longer than 2 weeks before euthanasia, tion was performed using the Advanced Cell Diagnostics RNAscope
with the exception of mice older than 18 months, which were housed Multiplex Fluorescent Detection kit v2 (323110, Bio-Techne) accord-
at the VA VMU beginning at 18 months of age. Before tissue collec- ing to the manufacturer’s instructions. Staining of mouse liver speci-
tion, mice were placed in sterile collection chambers at 8:00 for 15 mens was performed using 5-μm paraffin-embedded thick sessions.
min to collect fresh fecal pellets. After anaesthetization with 2.5% v/v Mouse livers were fixed in 10% formalin buffer saline (HT501128,
Avertin, mice were weighed, shaved, and blood was drawn via cardiac Sigma-Aldrich) for 24 h at room temperature before paraffin embed-
puncture before transcardial perfusion with 20 ml PBS. Mesenteric ding. For multiplex staining the following probes were used; Clec4f
adipose tissue was then immediately collected to avoid exposure to (Mm-Clec4f 480421, Il1b (Mm-Il1b 316891-C2), Pecam1 (Mm-Pecam-1
the liver and pancreas perfusate, which negatively affects cell sorting. 316721), Mrc1 (Mm-Mrc1 437511-C3). Slides were counterstained with
Isolating viable single cells from both the pancreas and the liver of the Prolong gold antifade reagent with DAPI (P36931, Life Technologies).
same mouse was not possible; therefore, two males and two females Mounted slides were imaged on a Leica DM6 B fluorescent microscope
were used for each. Whole organs were then dissected in the following (Leica Biosystems). Image quantification was performed using the
order: large intestine, spleen, thymus, trachea, tongue, brain, heart, starfish open source image-based transcriptomics pipeline (see Star-
lung, kidney, gonadal adipose tissue, bladder, diaphragm, limb muscle fish: Open Source Image Based Transcriptomics and Proteomics Tools,
(tibialis anterior), skin (dorsal), subcutaneous adipose tissue (ingui- available from http://github.com/spacetx/starfish and ref. 58).
nal pad), mammary glands (fat pads 2, 3 and 4), brown adipose tissue
(interscapular pad), aorta and bone marrow (spine and limb bones). Computational methods
Organ collection concluded by 10:00. After single-cell dissociation as Data extraction. Sequences from the NovaSeq were de-multiplexed us-
described below, cell suspensions were used either for FACS of indi- ing bcl2fastq v.2.19.0.316. Reads were aligned to the mm10plus genome
vidual cells into 384-well plates, or for preparation of the microfluidic using STAR v.2.5.2b with parameters TK. Gene counts were produced
droplet library. All animal care and procedures were carried out in using HTSEQ v.0.6.1p1 with default parameters, except ‘stranded’ was
accordance with institutional guidelines approved by the VA Palo Alto set to ‘false’, and ‘mode’ was set to ‘intersection-nonempty’. Sequenc-
Committee on Animal Research. es from the microfluidic droplet platform were de-multiplexed and
aligned using CellRanger v.2.0.1, available from 10x Genomics with
Tissue dissociation and sample preparation. All tissues were pro- default parameters.
cessed as previously described5.
Data pre-processing. Gene count tables were combined with the meta-
Sample size, randomization and blinding. No sample size choice was data variables using the Scanpy56 Python package v.1.4.2. We removed
performed before the study. Randomization and blinding were not genes that were not expressed in at least 3 cells and then cells that did
performed: the authors were aware of all data and metadata-related not have at least 250 detected genes. For FACS we removed cells with
variables during the entire course of the study. fewer than 5,000 counts, and for the droplet method we removed cells
with fewer than 2,500 unique molecular identifiers (UMIs). The data
Single-cell methods. All protocols used in this study are described was then normalized using size factor normalization such that every
in detail elsewhere5. These include: preparation of lysis plates; FACS cell has 10,000 counts and log transformed. We computed highly
sorting; cDNA synthesis using the Smart-seq2 protocol52,53; library variable genes using default parameters and then scaled the data to a
preparation using an in-house version of Tn554,55; library pooling and maximum value of 10. We then computed principal component analy-
quality control; and sequencing. For further details please refer to sis, neighbourhood graph and clustered the data using Louvain7 and
https://doi.org/10.17504/protocols.io.2uwgexe. Leiden8 methods. The data was visualized using UMAP projection.
When performing batch correction to remove the technical artefacts
Microfluidic droplet single-cell analysis. Single cells were captured introduced by the technologies, we replaced the neighbourhood graph
in droplet emulsions using the GemCode Single-Cell Instrument (10x computation with bbknn6. Step-by-step instructions to reproduce the
Genomics) and scRNA-seq libraries were constructed as per the 10x pre-processing of the data are available from GitHub.
Genomics protocol using GemCode Single-Cell 3′ Gel Bead and Library
V2 Kit. In brief, single cell suspensions were examined using an inverted Cell type annotation. To define cell types we analysed each organ
microscope, and if sample quality was deemed satisfactory, the sample independently but combining all ages. In brief, we performed principal
was diluted in PBS with 2% FBS to a concentration of 1,000 cells per μl. component analysis on the most variable genes between cells, followed
If cell suspensions contained cell aggregates or debris, two additional by Louvain and Leiden graph-based clustering. Next we subset the data
washes in PBS with 2% FBS at 300g for 5 min at 4 °C were performed. Cell for 3 months (Tabula Muris5) and computed how many cell types map
concentration was measured either with a Moxi GO II (Orflo Technolo- to each individual cluster. For the clusters that had a single 1:1 mapping
gies) or a haemocytometer. Cells were loaded in each channel with a (cluster:cell type) we propagated the annotations for all ages; in case
target output of 5,000 cells per sample. All reactions were performed there is a 1:many mapping we flagged that cluster for manual valida-
in the Biorad C1000 Touch Thermal cycler with 96-Deep Well Reaction tion. Step-by-step instructions to reproduce this method are available
from GitHub. For each cluster, we provide annotations in the controlled -RGID 4 -RGLB lib1 -RGPL illumina -RGPU unit1 -RGSM 20. Finally we used
vocabulary of the cell ontology57 to facilitate inter-experiment com- GATK HaplotypeCaller to call the mutations. We disabled the following
parisons. Using this method, we were able to annotate automatically read filters: MappingQualityReadFilter, GoodCigarReadFilter, NotSec-
(around 1 min per tissue) more than 70% of the dataset. The automatic ondaryAlignmentReadFilter, MappedReadFilter, MappingQualityA-
annotations were then reviewed by each of the tissue experts leading vailableReadFilter, Non-zeroReferenceLengthAlignmentReadFilter,
to a fully curated dataset for all the cell types in the Tabula Muris Senis. NotDuplicateReadFilter, PassesVendorQualityCheckReadFilter, and
WellformedReadFilter, but kept all other default settings. The results
Tissue cell composition analysis. For each tissue and age, we com- were summarized per gene in the form of a mutation count per cell
puted the relative proportion of each cell type. Next we used scipy.stats table. We started by removing genes mutated in more than 60% of cells,
linregress to regress the relative tissue-cell type changes against age to eliminate the possible bias of germline mutations. Then for each
and considered significant the changes with P < 0.05 for a hypothesis tissue we selected genes expressed in at least 75% of the cells for all the
test with the null hypothesis that the slope is zero, using two-sided Wald time points to avoid confounding the mutation results with differential
test with t-distribution of the test statistic and a r2 > 0.5. gene expression associated with age. Next we computed the average
number of mutations in the gene set (or ERCC spike-in controls) per cell
Differential gene expression. We performed differential gene expres- and also the average number of raw counts (Supplementary Table 8)
sion analysis on each tissue with a well-powered sample size (more than and plotted the different distributions. Step-by-step instructions to
100 cells in both young (1 month and 3 month) and old (18 months, reproduce the processing of the data are available from GitHub.
21 months, 24 months and 30 months) age groups). We used a linear
model51 treating age as a numerical variable while controlling for sex Trajectory analysis. We used partition-based graph abstraction
and technology. We applied a false-discovery rate (FDR) threshold of (PAGA60) to reconstruct the ageing trajectory in brain microglial cells.
0.01 and an age coefficient threshold of 0.005 (corresponding to an Step-by-step instructions to reproduce the processing of the data are
approximately 10% fold change). available from GitHub.
Comparison between bulk and single-cell datasets. The differential Diversity score. The raw FACS or droplet dataset were used as the
gene analysis was defined on a per tissue basis. First, we investigated input. We filtered genes expressed in fewer than 5 cells, filtered cells if
genes on the basis of the single-cell data. We considered only cells from expressing fewer than 500 genes and discarded cells with total number
male mice and perform our analysis on the log (1 + counts per million of counts less than 5,000. Next we performed size factor normalization
(cpm)) transformed single-cell count matrices. Note that normaliza- such that every cell had 1× 104 counts and performed a log1p transfor-
tion of the single-cell data was done on a per cell basis. We defined two mation. This was followed by clustering, in which we clustered every
groups of cells on the basis of age: young cells with age ≤ 3 months (Y) tissue and every tissue-cell type for every mouse separately using 6 dif-
and old cells with age >3 months (O). For each gene we compute the ferent configurations: resolution parameters (0.3, 0.5, 0.7) × clustering
log fold change of cell and read counts between O and Y. We defined method (Louvain, Leiden). This is to provide a robust clustering result.
2
cell count as the fraction of cells that express the gene. Similarly, we For each combination (each tissue–mouse and each tissue–cell_type–
defined read count as the mean read count of the gene in the cells that mouse), we computed the clustering diversity score as the Shannon
express it. The calculated log fold-changes of a gene reflect its expres- entropy of the cluster assignment. We then regressed the diversity score
2
sion changes with ageing within the single-cell data. Next we analysed against age to detect the systematic increase or decrease of clustering
each gene on the basis of the bulk data. We computed the Spearman diversity with respect to age. FDR was used to correct for multiple
correlation (ρ) of bulk DESeq2 normalized gene expression with ageing. comparisons. A tissue or a tissue–cell type was selected if the slope was
We defined two groups of genes on the basis of the bulk data, increas- consistent (having the same sign) in all six clustering configurations
ing with age ρ > 0.7 (U) and decreasing with age ρ < −0.7 (D). Finally, we and at least two out of six clustering configurations had FDR <0.3. For
compared the log fold-changes based on the single-cell data between each selected tissue or tissue–cell type, a separate UMAP was computed
2
the bulk data defined groups U and D. Specifically, we ran a Wilcoxon– using cells from all mice for visualization using Leiden clustering with
Mann–Whitney test to understand whether log fold-changes of cell or resolution parameter 0.7.
2
read counts could distinguish between the two groups. We used the U
statistic for effect size. Reporting summary
Further information on research design is available in the Nature
T cell processing. We used TraCeR44 v.0.5 to identify T cell clonal popu- Research Reporting Summary linked to this paper.
lations. We ran tracer assemble with–species Mmus set. We then ran
tracer summarize with –species Mmus to create the final results. We
Data availability
used the following versions for TraCeR dependencies: igblast v.1.7.0,
kallisto v.0.43.1, Salmon v.0.8.2, Trinity v.2.4.0, GRCm38 reference The entire dataset can be explored interactively at http://
genome. Step-by-step instructions to reproduce the processing of the tabula-muris-senis.ds.czbiohub.org/. Gene counts and metadata are
data are available from GitHub. available from figshare (https://doi.org/10.6084/m9.figshare.8273102.
v2) and the Gene Expression Omnibus under accession code GSE132042;
B cell processing. We used singlecell-ige43 v.eafb6d126cc2d6511faae the raw data files are available from a public AWS S3 bucket (https://
3efbd442abd7c6dc8ef (https://github.com/dcroote/singlecell-ige) to registry.opendata.aws/tabula-muris-senis/).
identify B cell clonal populations. We used the default configuration
settings, except we set the species to mouse. Step-by-step instructions
Code availability
to reproduce the processing of the data are available from GitHub.
The code used for the analysis is available from GitHub at https://github.
Mutation analysis. We used samtools59 v.1.9 and GATK39 v.4.1.1.0 for com/czbiohub/tabula-muris-senis.
mutation analysis. We used samtools faidx to create our index file.
Then we used GATK CreateSequenceDictionary and GRCm38, as the 52. Picelli, S. et al. Smart-seq2 for sensitive full-length transcriptome profiling in single cells.
Nat. Methods 10, 1096–1098 (2013).
reference, to create our sequence dictionary. Next we used GATK Ad-
53. Darmanis, S. et al. A survey of human brain transcriptome diversity at the single cell level.
dOrReplaceReadGroups to create a single read group using parameters Proc. Natl Acad. Sci. USA 112, 7285–7290 (2015).
Article
54. Picelli, S. et al. Tn5 transposase and tagmentation procedures for massively scaled experiments were performed with instruments in the VA Flow Cytometry Core, which is
sequencing projects. Genome Res. 24, 2033–2040 (2014). supported by the US Department of Veterans Affairs (VA), Palo Alto Veterans Institute for
55. Hennig, B. P. et al. Large-scale low-cost NGS library preparation using a robust Tn5 Research (PAVIR), and the National Institutes of Health (NIH). This work was supported by the
purification and tagmentation protocol. G3 (Bethesda) 8, 79–89 (2018). Chan Zuckerberg Biohub, Department of Veterans Affairs grant IK6 BX004599 (T.W.-C.) and
56. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell gene expression data NIH/NIA DP1 grant AG053015 (T.W.-C.). We thank B. Tojo for the artwork, and C. Xu and J. Batson
analysis. Genome Biol. 19, 15 (2018). for discussions.
57. Diehl, A. D. et al. The Cell Ontology 2016: enhanced content, modularization, and
ontology interoperability. J. Biomed. Semantics 7, 44 (2016). Author contributions A full list of author contributions can be found in the Supplementary
58. McQuin, C. et al. CellProfiler 3.0: Next-generation image processing for biology. PLoS Information.
Biol. 16, e2005970 (2018).
59. Li, H. et al. The Sequence Alignment/Map format and SAMtools. Bioinformatics 25, Competing interests The authors declare no competing interests.
2078–2079 (2009).
60. Wolf, F. A. et al. PAGA: graph abstraction reconciles clustering with trajectory inference Additional information
through a topology preserving map of single cells. Genome Biol. 20, 59 (2019). Supplementary information is available for this paper at https://doi.org/10.1038/s41586-020-
2496-1.
Correspondence and requests for materials should be addressed to S.D., S.R.Q. or T.W.-C.
Acknowledgements We thank Sony Biotechnology for making an SH800S instrument Peer review information Nature thanks Fan Zhang and the other, anonymous, reviewer(s) for
available for this project. Some of the cell sorting and flow cytometry analysis for this project their contribution to the peer review of this work.
was done on a Sony SH800S instrument in the Stanford Shared FACS Facility. Some FACS Reprints and permissions information is available at http://www.nature.com/reprints.
Extended Data Fig. 1 | See next page for caption.
Article
Extended Data Fig. 1 | UMAP visualizations of the whole Tabula Muris Senis. transcriptome Louvain clustering, irrespective of the organ from which they
a, b, UMAP plot of all cells collected for FACS coloured by tissue (a) or age (b). originated. h, B cells (left) and endothelial cells (right) in droplet independently
c, UMAP plot of all cells collected by FACS, coloured by organ (Extended Data annotated for each organ cluster together by unbiased whole-transcriptome
Fig. 4c), overlaid with the Louvain cluster numbers. n = 110,824 individual cells Louvain clustering, irrespective of the organ from which they originated.
for FACS. d, e, UMAP plot of all cells collected for droplet coloured by tissue (d) i, j, UMAP plot of all cells collected coloured by method (i) or tissue (j).
or age (e). f, UMAP plot of all cells collected by droplet, coloured by organ n = 356,213 individual cells for FACS and droplet combined. k, l, B cells (k) and
(Extended Data Fig. 4c), overlaid with the Louvain cluster numbers. n = 245,389 endothelial cells (l) cluster together by unbiased whole-transcriptome Louvain
individual cells for droplet. g, B cells (left) and endothelial cells (right) in FACS clustering, irrespective of the technology by which they were found.
independently annotated for each organ cluster together by unbiased whole-
Extended Data Fig. 2 | Tabula Muris Senis quality control statistics overall for FACS. For c, d, all data are expressed as mean ± s.d. Individual data points
summary and detailed for the FACS dataset. a, Pie chart with the summary (black diamonds) correspond to outliers outside of the quantile distribution.
statistics for FACS. b, Pie chart with the summary statistics for droplet. c, Box The sample size (number of cells for each tissue and age) is available in
plot of the number of genes detected per cell for each organ and age for FACS. Supplementary Table 1.
d, Box plot of the number of reads per cell (log-scale) for each organ and age
Article
Extended Data Fig. 3 | Tabula Muris Senis quality control statistics detailed mean ± s.d. Individual data points (black diamonds) correspond to outliers
for the droplet dataset. a, Box plot of the number of genes detected per cell outside of the quantile distribution. The sample size (number of cells for each
for each organ and age for droplet. b, Box plot of the number of UMIs per cell tissue and age) is available in Supplementary Table 2.
(log scale) for each organ and age for droplet. All data are expressed as
Extended Data Fig. 4 | Number of cells in Tabula Muris Senis across age, sex, per sex per age. b, Schematic of the analysis workflow. c, d, Tabula Muris Senis
tissue and technology and schematic the of data processing. a, Balloon plot colour dictionary for organs and tissues (c) and ages (d).
showing the number of sequenced cells per sequencing method per organ
Article
g
0.20
0.18
0.16
0.14
0.12
0.10
0.08
18.0 18.5 19.0 19.5 20.0 20.5 21.0
Age (months)
noitroporp
epyt
llec
evitaleR
0.40
0.35
0.30
0.25
0.20
0.15
2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
Age (months)
Skin keratinocyte stem cell
noitroporp
epyt
llec
evitaleR
c
Mammary Gland T cell
0.08
0.07
0.06
0.05
0.04
0.03
0.02
0.01
0 5 10 15 20 25 30
Age (months)
noitroporp
epyt
llec
evitaleR
a
FACS
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
Read count based effect size
e
Marrow precursor B cell
ezis
tceffe
desab
tnuoc
lleC
18 BAT
Brain Myeloid
16 Brain Non-Myeloid
14 GAT
12 Heart
10 Kidney
8 Limb Muscle Liver 6
Lung
4 MAT
2 SCAT
0 Skin
0 2 4 6 8 1012141618
Read count based -log (p-value)
10
)eulav-p(
gol-
desab
tnuoc
lleC
01
b
Droplet
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
Read count based effect size
ezis
tceffe
desab
tnuoc
lleC
30
25
20
15
10
5
0
0 5 10 15 20 25 30
Read count based -log10(p-value)
)eulav-p(01gol-
desab
tnuoc
lleC
Brain Non-Myeloid
Kidney
Limb Muscle
Liver
Lung
SCAT
Spleen
bulk signal explained neither by bulk signal explained by bulk signal explained by bulk signal explained by both
single-cell read nor by cell count read count only cell count only single-cell read and cell count
Marrow
8a001S 9a001S 2ncL pgN pmaC glnteR 6a001S kiR02G1000011 1prylgP ftL iplS 6mtifI 2mtifI s-ateB 3slagL abyC 9dC opsT 31rrP 1lfC nuJ 1lnbM e6yL 2psuD 2l63pfZ 5xdD pnC 1cpbaP byM 4xoS 1a1feE 2feE 1nihyP yfa2H 8calP upnrnH 8apsH 3cnireS 3berpV a2l72ifI
520.0
000.0520.0−
tneiciffeoc
egA
Skin
6lcC ncD glnteR a31lpR 2l4afudN ahawoS masE 1lfC m2B dnuJ 7gkN a2altC gaM 41a001S d6yL a3cl1paM sstC aA-2H smtP ldohC 1gtcA 1cdS 1teN 1b8dC bh4P nuJ ppA ibfgT 3aidP kpnrnH 3cdcC 2brdA 3pqA nsG pbcdS 8apsH pinxT preP tmnI a8dC
01.0
50.0
00.0
50.0−
tneiciffeoc
egA
Mammary Gland
dnuJ 1tM 6a001S nsG 2tM bsoF 11a001S anmL soF 3mtifI 4flK bnuJ b2mtI 2mtifI 1pirC eopA pasP 1rgE 63pfZ 1psuD 1mpN a1oroC 3pmaR 42spR 1ahmH 2dC b73spV 6pamiG 3dmarG ngrS 1feL 2dmiL r12lI 1epsH 0239mG 35dC d3dC 4sp-a51spR 7rcC 1btaS
50.0
00.0
tneiciffeoc
egA
d
f
h
Extended Data Fig. 5 | See next page for caption.
