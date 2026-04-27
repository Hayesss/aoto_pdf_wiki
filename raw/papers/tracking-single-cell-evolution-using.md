---
source_path: /mnt/c/Users/Administrator/Zotero/storage/89FADWIA/s41587-024-02241-z.pdf
ingested: 2026-04-23
sha256: 1529ed5045a00851
---

nature biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
Tracking single-cell evolution using
clock-like chromatin accessibility loci
Received: 10 May 2022 Yu Xiao 1,2,8, Wan Jin2,3,8, Lingao Ju 2,8, Jie Fu 4,8, Gang Wang 1,2,
Mengxue Yu2, Fangjin Chen5, Kaiyu Qian 2,6, Xinghuan Wang 1,6,7 &
Accepted: 10 April 2024
Yi Zhang 3
Published online: xx xx xxxx
Check for updates Single-cell chromatin accessibility sequencing (scATAC-seq) reconstructs
developmental trajectory by phenotypic similarity. However, inferring
the exact developmental trajectory is challenging. Previous studies
showed age-associated DNA methylation (DNAm) changes in specific
genomic regions, termed clock-like differential methylation loci
(ClockDML). Age-associated DNAm could either result from or result in
chromatin accessibility changes at ClockDML. As cells undergo mitosis,
the heterogeneity of chromatin accessibility on clock-like loci is reduced,
providing a measure of mitotic age. In this study, we developed a method,
called EpiTrace, that counts the fraction of opened clock-like loci from
scATAC-seq data to determine cell age and perform lineage tracing in
various cell lineages and animal species. It shows concordance with known
developmental hierarchies, correlates well with DNAm-based clocks and
is complementary with mutation-based lineage tracing, RNA velocity
and stemness predictions. Applying EpiTrace to scATAC-seq data reveals
biological insights with clinically relevant implications, ranging from
hematopoiesis, organ development, tumor biology and immunity to
cortical gyrification.
Single-cell chromatin accessibility sequencing (scATAC-seq) is a mutation-based lineage tracing methods—for example, using mito-
powerful technique for interrogating the epigenomic landscape at chondrial single-nucleotide polymorphisms (SNPs)7–9, which track
single-cell resolution1. However, inferring the exact developmental the phylogeny of cells over divisions—are highly accurate, yet their
trajectory of cells from scATAC-seq data is challenging. Although tools temporal resolution is restrained by the low natural mutation rate.
such as RNA velocity, stemness prediction and metabolic labeling2–5 The concept of mitotic age refers to the accumulative counts
exist for determining cell evolution trajectories on the manifold of of mitosis that a cell undergoes after the ground state of cell divi-
phenotypes from single-cell RNA sequencing (scRNA-seq) datasets, no sion or fertilization. The first proposed mitotic (replicational) age
similar methods exist for scATAC-seq. State-of-the-art, similarity-based biomarker was telomere length, which is genetic10,11, and the concept
lineage deduction methods6 would be limited when phenotypes are quickly extended to epigenetic replication errors on DNA methylation
fluidic, such as in dedifferentiation or oncogenesis. On the other hand, (DNAm)12,13. During DNA replication, epigenetic covalent modifications
1Department of Urology, Zhongnan Hospital of Wuhan University, Wuhan, China. 2Department of Biological Repositories, Human Genetic Resources
Preservation Center of Hubei Province, Hubei Key Laboratory of Urological Diseases, Zhongnan Hospital of Wuhan University, Wuhan, China. 3Euler
Technology, ZGC Life Sciences Park, Beijing, China. 4Hong Kong University of Science and Technology, Hong Kong, China. 5High Performance Computing
Center, Peking-Tsinghua College of Life Sciences, Peking University, Beijing, China. 6Medical Research Institute, Frontier Science Center for Immunology
and Metabolism, Taikang Center for Life and Medical Sciences, Wuhan University, Wuhan, China. 7Wuhan Research Center for Infectious Diseases and
Cancer, Chinese Academy of Medical Sciences, Wuhan, China. 8These authors contributed equally: Yu Xiao, Wan Jin, Lingao Ju, Jie Fu.
e-mail: wangxinghuan@whu.edu.cn; zy@eulertechnology.com
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
are not faithfully replicated to the daughter strand, resulting in stochas- blood mononuclear cells (PBMCs) from a panel of donors of different
tic DNAm changes. Stochastic DNAm fluctuation has been applied to ages and determined the correlation coefficient between age and
infer the mean mitotic count of the cell population14–16. On the popula- the methylation level (beta) on each locus (Supplementary Table 1:
tion scale, irreversible, stochastic DNAm changes were thought to be ClockDML). The DNAm status of these ClockDML showed excellent
underlying age-associated DNAm changes. A vast number of studies correlation with age in the training cohort (Fig. 1b). Both the general
have documented age-associated DNAm changes17, including hypo- linear model (GLM) and the probability model (TimeSeq)31 built upon
methylation and hypermethylation, in specific genomic regions. We beta values of our ClockDML predict donor age with good precision
term such genomic regions clock-like differential methylation loci in an additional validation cohort of samples (R = 0.85 (GLM) / 0.7998
(ClockDML) because their DNAm exhibits timekeeper-like behavior. (TimeSeq); Supplementary Fig. 1a–c), indicating that the DNAm status
The DNAm-based regression model predicts the age of biological of these loci stably drifts over age.
samples with extremely high precision in many organisms18–24 and cor- Functional annotation suggests that ClockDML are enriched in
relates with rejuvenation or accelerated aging in various scenarios25. the open, accessible chromatin region of the genome across different
A similar age association of DNAm was conserved across mammalian cell types and organs39–41 (Fig. 1c). In correlation with DNAm status, the
species in homologous genomic regions26, suggesting that it is con- fraction of opened ClockDML (hereafter, in short: ClockAcc) shifts in
trolled by a defined, possibly functional, molecular mechanism27. correlation with cell aging (Supplementary Notes and Supplementary
Interestingly, a predictor model was built to estimate the mitotic Figs. 2–5; GSE74912 (ref. 42), GSE89895 (ref. 43) and GSE179606 (ref. 44)).
age of samples from the DNAm state of a defined set of CpG loci28,29, We established an algorithm, called EpiTrace, that predicts sample
indicating that mitosis is associated with clock-like DNAm changes age by counting the fraction of opened ClockDML in bulk ATAC-seq
at specific genomic loci. Introducing population statistics into the datasets (Supplementary Notes). Validation experiments using bulk
DNAm-based age prediction model enabled single-cell age prediction ATAC-seq of FACS-sorted blood cells, induced pluripotent stem cell
from single-cell methylation sequencing data30,31, suggesting that (iPSC) induction experiments and native immune cells showed that
clock-like DNAm changes are not merely a statistical phenomenon at EpiTrace accurately predicted sample age in concordance with known
the population scale but also occur at the single-cell level. developmental trajectories (Supplementary Notes and Supplementary
Based on the intrinsic link between chromatin accessibility and Figs. 2–5). We then adopted the algorithm for scATAC-seq data. In brief,
DNAm32–37, we hypothesized that age-dependent DNAm could either a reference ClockDML set was provided to the algorithm. ClockAcc,
result from or result in chromatin accessibility changes at ClockDML. If the total chromatin accessibility on this reference ClockDML set, is
so, the derived mitotic age of single cells from scATAC-seq data would measured for each cell. The measurement was performed using a hid-
serve as a powerful tool to delineate developmental trajectory. In den Markov model (HMM)-mediated diffusion-smoothing approach,
theory, mitotic age is a ‘timekeeper’ tracker: the mitotic age of an ances- borrowing information from similar single cells to reduce noise in the
tor cell is lower than that of its progeny, and cells originating earlier in single-cell measurement: cells were clustered via correlation of top
time should show lower mitotic age than those originating later. Such variable ATAC peaks to form a cell‒cell similarity matrix, which was then
a measure of cell age, if it exists, would provide a precise temporal ref- used for diffusion-regression iterations of ClockAcc until convergence.
erence of the cell birth sequence to help delineate the developmental After iteration, the regularized and smoothened ClockAcc of each
trajectories in a complex organism. single cell were then ranked. Such rank denotes the relative mitotic
To develop a mitotic age estimator for scATAC-seq data, we deter- cell age. To overcome sampling sparseness in scATAC-seq, we reasoned
mined ClockDML across the human genome and characterized the that it might be unnecessary for age-dependent chromatin accessibility
chromatin accessibility changes in these loci associated with cell (ChrAcc) to always be accompanied by DNAm changes (Supplemen-
mitotic age. The heterogeneity of chromatin accessibility at these loci tary Notes). Thus, we perform stepwise iterations by extracting addi-
reduces across cell division. Through genomic synteny mapping, we tional open regions with a high correlation coefficient with estimated
showed that the age-dependent chromatin accessibility is conserved single-cell age and then include them together with the reference loci to
on these loci across evolution. Such clock-like chromatin accessibil- form a new set of reference clock-like loci for the next round of analysis
ity is independent from DNAm. Even in species without active DNAm, until the age prediction converges (Fig. 1d). During the computation
clock-like chromatin accessibility exists on these loci. Hence, we term of EpiTrace algorithm, known sample age information is not required.
these regions as ‘clock-like loci’. We leveraged this phenomenon to The algorithm simply leverages the fact that heterogeneity of given
develop a computational framework, called EpiTrace, which infers cell reference ClockDML reduces during cell replication and then uses such
mitotic age from scATAC-seq data by counting the opened fraction of information as an intermediate tool variable to infer cell age.
clock-like loci in single cells. We first validated the EpiTrace algorithm on in vitro models.
ChrAcc in single mouse cells was profiled with the simultaneous high-
Results throughput ATAC and RNA expression with sequencing (SHARE-seq)
Chromatin accessibility enables single-cell age estimation assay (Supplementary Fig. 6), and DNAm age (in batch) was determined
Although the molecular mechanism that generates age-associated by DNAm sequencing (Supplementary Fig. 1d–g). In asynchronized
DNAm changes is unclear, it is possible that the methylation state immortal mouse embryonic fibroblast (MEF) cells, progression in
of ClockDML might be affected by chromatin accessibility. Alterna- the cell cycle results in a reduction in EpiTrace-predicted age (Sup-
tively, the methylation state of ClockDML might reversely regulate plementary Fig. 7), suggesting that EpiTrace tracks an epigenomic
chromatin accessibility. In either case, the chromatin accessibility modification that dilutes during genome replication (as newly syn-
on ClockDML could be used to deduce cell age (Fig. 1a). However, the thesized copy of genome emerges). In primary MEF (pMEF) cells, this
dynamics of chromatin accessibility on ClockDML during aging are phenomenon persists (Supplementary Fig. 8a,b,d,h). However, as
currently unknown. the cells were passaged in vitro, the EpiTrace age stably increased
Literature-documented ClockDML18,25,26,38 were found mainly (Supplementary Fig. 8b,i). Such a mitosis age-dependent increase in
with methylation-specific microarrays and, thus, represent only a EpiTrace age overwhelms the genome replication-mediated dilution
tiny fraction of possible genome-wide DNAm variation during aging. effect (Supplementary Fig. 8) and correlates well with DNAm-based
However, ATAC-seq—and, more so, scATAC-seq—data are too sparse to age prediction of the same batch of samples (Supplementary Fig. 9).
fully cover these loci. To enable accurate tracking of cell mitotic age by Finally, for cells that are pharmacologically blocked in a specific cell
ATAC signal, we determined 126,420 ClockDML in the human genome cycle (GSE65360 (ref. 1)), EpiTrace age increases from G1 to S and G2/M
by bisulfite capture sequencing the CpG island regions of peripheral phase (Supplementary Fig. 10), suggesting that accumulation of error
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
R = –0.978, P < 2.2 × 10–16
Nature Biotechnology
sisotiM
a ClockDML ChrAcc b Negative ClockDML × age
Progenitor
Loci: +++; ChrAcc: +
Gradual accumulation of
ChrAcc
on clock-like loci
0.4
Human donor age
Irreversible DNAm change
downstream of ChrAcc
Terminal Loci: +
ChrAcc: +++
ateb
mAND
LMDkcolC
c Enrichment of CRE on ClockDML
0.7
0.6
0.5
30 40 50 60 70 ATAC dataset vs clock type
d
f
hESC, primed
hESC, naive
Cultured tropho.
TE
ICM
Morula
8 cell
4 cell
2 cell
Zygote
Sperm
Oocyte
7,500 12,500 17,500 1 2 3 4 0 0.25 0.5 0.75 1 0 0.25 0.5 0.75 1
UMAP1 ClockAcc Smoothed ClockAcc EpiTrace age Iterative EpiTrace
)tnemhcirne(
oitar
sddO
30
10
3
Normal cell scATAC
Hemapoietic cell scATAC
1 Placenta scATAC
Pan-cancer scATAC
Bladder cancer scATAC
Mitosis Chronology Solo_WCGW
e Embryo ATAC
ZGA ICM
hESC
Zygote / TE
pre-ZGA
Trophoblast
2PAMU
4
2
0
–2
–6 –3 0 3 6
Oocyte Sperm Zygote 2 cell 4 cell 8 cell Morula ICM
hESC, naive hESC, primed TE PE trophoblast Normal trophoblast
Age-associated
loci
Similarity-
based
feature expansion
ClockDML
and
other
loci
Cell × loci matrix
(with random dropoff)
ClockDML
and
clock-associated
loci
Single
C
-c
e
e
ll
ll age
Updated
age
1
Updated
age
2 …….
Final
sc age
Censor Age × loci
normalization correlation
Accessibility
measurement Iteration
HMM-based Until
smoothing convergence
Ranking
to output
Fig. 1 | ChrAcc change associated with irreversible DNAm drift on ClockDML of the human early embryonic development scATAC dataset. Color indicates
enables cell age estimation. a, Schematic diagram of the underlying epigenetic the developmental stage of human embryo. f, The total chromatin accessibility
mechanism of cell mitotic age tracing using ChrAcc on ClockDML. b, Correlation on ClockDML (ClockAcc), HMM-smoothened ClockAcc and initial and iterative
between the DNAm level on G8-group ClockDML and sample age in human EpiTrace ranking result (EpiTrace age) corresponding to the embryonic dataset.
PBMCs. 95% CI is shown as a gray area around the linear regression line. Sample numbers of biologically independent samples: n = 1 (Oocyte); 1 (Sperm);
R = −0.978, P < 2.2 × 10−16. c, Enrichment of mitosis-associated ClockDML (Mitosis, 2 (Zygote); 5 (two-cell); 1 (four-cell); 6 (eight-cell); 2 (Morula); 5 (ICM); 4 (Naive
size = 1,934 bp), actual age-associated ClockDML (Chronology, size = 58,7801 bp) hESC); 7 (Primed hESC); 2 (TE); and 3 (Differentiated trophoblast). The upper
and solo-WCGW loci (size = 5 Mbp) in each class of ATAC peaks (size = 281 Mbp and lower bounds of boxes show 25% and 75% percentiles of the data. The median
(TCGA Pan-cancer); 164 Mbp (bladder cancer); 462 Mbp (normal cell); 218 Mbp of data is shown as the horizontal line in the box. The distribution minima and
(placenta); and 295 Mbp (hematopoietic cell)). Two-sided Fisher’s exact test maxima, defined as farthest data point distanced ≤1.5 IQR from the box bounds,
was performed for the expected against observed overlapped region size. The are shown by the whiskers. Correlation R and P value: Pearson’s. Tiny P values
points show the resulting odds ratio of observed size over expected size, and resulting in numerical underflow are shown as ‘<2.2 × 10−16’. tropho., trophoblast.
the 95% CI is shown as whiskers. d, Overview of the EpiTrace algorithm. e, UMAP
Article https://doi.org/10.1038/s41587-024-02241-z
during copying of epigenomic modification to the newly synthesized assembles their time of emergence (Fig. 2c). Similar results were
copy of genome results in an increase in EpiTrace age prediction over obtained for ‘mouse-guided’ clock-like loci (Supplementary Fig. 13c;
mitosis. In large in vivo single-cell datasets without cell phase syn- GSE152423 (ref. 50)).
chronization, the cell cycle had little effect on EpiTrace age prediction For many animal species, active DNAm is not present in the
(Supplementary Fig. 11; GSE163579). Together, these data indicate that genome. For example, the Drosophila melanogaster genome has
EpiTrace reports mitosis age. less than 1% of CpG being methylated51,52. We hypothesized that if
As a proof of concept, we gathered ATAC data from various studies clock-like chromatin accessibility is a universal phenomenon in
of early human embryonic development from gametes to blastula19,45 ClockDML-homologous genomic regions, then identification of
(Fig. 1e and Supplementary Fig. 12; PRJNA494280 and PRJNA394846), ClockDML-homologous genomic regions in such species might be
which were generated from only a few cells each, and subjected them to sufficient for age prediction using EpiTrace.
EpiTrace analysis without batch correction (Fig. 1f). The total ClockAcc Because these animal species are evolutionarily too distant from
in sample positively correlates with known cell mitotic age. Although the humans, only gene-level orthologous relationships could be reliably
initial EpiTrace age prediction is noisy, iterative optimization improved identified between their genomes and humans. To overcome this prob-
the signal-to-noise ratio to draw a biologically plausible trajectory of age lem, we used an orthology-guided approach to first identify human–
resetting during early embryonic development: starting from zygote, animal orthologous genes whose promoters encompassed ClockDML
cell mitotic age gradually reduces to near ground state at the time of in the human genome and then to identify the corresponding promoter
zygotic genome activation (ZGA) at morula, before its rebound in inner genomic loci in the distant animal genome (Fig. 2d). For the D. mela-
cell mass (ICM), trophectoderm (TE) and embryonic stem cell (ESC). nogaster genome, we identified 1,556 such loci (Fig. 2e). We then used
this as ‘human-guided’ clock-like loci in the Drosophila genome for
Inferring cell age across cell types and animal species reference in EpiTrace age prediction in a Drosophila embryonic devel-
For many cell types and animal species, ClockDML have not been experi- opment scATAC-seq dataset. The prediction result showed high con-
mentally determined. The fact that ClockDML derived from human cordance with the known sampling time (Fig. 2f; GSE190130 (ref. 53)).
PBMCs could be used to predict the sample age not only of human
blood cells but also of cells of the non-hematopoietic lineage (Fig. 1 and ChrAcc change is upstream of DNAm shift on ClockDML
Supplementary Fig. 5) suggests that clock-like ChrAcc on the Clock- Drosophila is an invertebrate species that lacks canonical DNA methyl-
DML genomic region might be universal across cell lineages. To test transferase. Only 0.4% (1 hour post-fertilization (hpf)) to 0.1% (12 hpf)
whether we could extend known ClockDML to other species or cell types of cytosine in the Drosophila genome was methylated52 compared to
for EpiTrace prediction, we mapped human ClockDML to the mouse 6–8% in humans, and most Drosophila methylated C was CpT/CpA. The
genome using genomic synteny and computed EpiTrace age for the fact that EpiTrace can work on the Drosophila genome suggests that
mouse scATAC-seq dataset using mouse ClockDML or ‘human-guided’ clock-like chromatin accessibility might be independent of clock-like
clock-like loci (Supplementary Fig. 13a). We found that the EpiTrace DNA methylation. To validate this model, we first tracked ChrAcc and
prediction results using the reference ‘human-guided’ clock-like loci DNAm on the same DNA molecule using the human embryonic develop-
closely approximated the prediction results using the reference mouse ment single-cell chromatin overall omic-scale landscape sequencing
ClockDML (R = 0.81; Supplementary Fig. 13b; GSE137115 (ref. 46)). (scCOOL-seq) dataset (Supplementary Fig. 15; GSE100272 (ref. 54)) and
To further validate the concordance between EpiTrace prediction a long-read nanopore sequencing of nucleosome occupancy and methy-
starting from different reference loci, we tested a mouse scATAC-seq lome (nanoNOME) dataset (Supplementary Fig. 16; GSE183760 (ref. 55)).
dataset of T cells under chronic or acute virus infection (Supplementary In both datasets, ChrAcc shifts before ClockDML DNAm changes on
Fig. 14a; GSE164978 (ref. 47)). EpiTrace age prediction using the mouse the same molecule, indicating that clock-like DNAm is not necessary
reference ClockDML agrees with the known developmental trajectory for clock-like ChrAcc.
of these immune cells (Supplementary Fig. 14b). In concordance with We then performed forced transcriptional activation around
their tissue of origin, clock-like loci inferred from genomic synteny of ClockDML to test whether changes in ChrAcc would influence DNAm in
human PBMC ClockDML overlap with known immune cell exhaustion these regions. We transfected single guide RNA (sgRNA) lentivirus tar-
genes, such as Pdcd1, Havcr2, Tox and Eomes, whereas mouse Clock- geting human G8-group ClockDML loci (shown in Fig. 1b) into HEK293
DML48 (derived from pan-body DNAm interrogation) do not (Supple- cells stably expressing the dCas9–p300 transactivator (Supplementary
mentary Fig. 14c). However, single-cell age inferred by EpiTrace with Fig. 17a). Gain of ChrAcc around these loci results in DNA hypomethyla-
mouse ClockDML as reference correlates well with that inferred with tion on neighboring ClockDML (Supplementary Fig. 17b,c), indicating
‘human-guided’ clock-like loci as reference (Supplementary Fig. 14d). that clock-like DNAm could be driven by ChrAcc shift.
The association of ATAC peak chromatin accessibility and single-cell In another conceptually similar scenario, we measured the DNAm
ages from the two predictions shows extremely high concordance changes under forced transcription activation around mouse Sox1 loci
(R = 0.92; Supplementary Fig. 14e), with the identification of many and found them to linearly correlate with the age-dependent DNAm
known immune exhaustion genes being positively correlated with cell shift coefficient of corresponding loci in the human genome (Supple-
age (Supplementary Fig. 14e). Such correlation is not dependent on mentary Fig. 18; PRJNA490128 (ref. 56)). Hence, changes of ChrAcc on
whether the loci are previously overlapping with a reference clock-like ClockDML are sufficient to drive clock-like differential DNAm.
loci (Supplementary Fig. 14f). Furthermore, peaks overlapping with To validate whether changes in DNAm would affect ChrAcc on
both ‘human-guided’ clock-like loci and mouse ClockDML showed the ClockDML, we tracked ChrAcc in a dataset where forced DNAm was
greatest age-dependent ChrAcc shift (Supplementary Fig. 14g). These performed with a ZNF-DNMT3A artificial methylator (Supplementary
results indicate that EpiTrace can use ClockDML from different tissues Fig. 19a; GSE102395 (ref. 57)). Although ZNF-DNMT3A induction results
of origin to predict single-cell age, even in a cross-species scenario. in irreversible DNAm on ClockDML around its binding site (Supple-
We then mapped human ClockDML to the zebrafish genome using mentary Fig. 19b,e), it does not change the overall ChrAcc on these loci
a similar synteny-guided approach (Fig. 2a) and tested EpiTrace pre- (Supplementary Fig. 19c,d; GSE102395 (ref. 57) and GSE103590 (ref. 58))
diction on a zebrafish scATAC-seq dataset spanning from fertilization nor does it change the EpiTrace age on these cells (Supplementary
to the adult stage (GSE178969 (ref. 49)) using this ‘human-guided’ Fig. 19f,g; GSE102395 (ref. 57) and GSE103590 (ref. 58)).
clock-like loci as reference. The mean EpiTrace age prediction from Together, these data indicate that clock-like ChrAcc occurs
each stage closely approximated the known sample age (R = 0.97; upstream of the DNAm shift on ClockDML. In animals without active
Fig. 2b). For each single-cell type, the EpiTrace prediction closely DNAm, genomic region exhibiting clock-like ChrAcc could also be
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
a b c
Human genome
Human ClockDML
Zebrafish genome Genomic
synteny
Putative clock-like loci Putative clock-like loci
by synteny by synteny
d
Promoter ClockDML
Human genome Ortholog human gene
Human ClockDML
Protein
Fly genome orthology
Non-mapped gene Ortholog fly gene
Fly scATAC peaks
Putative clock-like loci by orthologous mapping
e
126,240 91,935
5,157 10,057 3,134 1,556
All ClockDML All scATAC peak
TSS ClockDML TSS scATAC peak
H-D ortholog TSS ClockDML H-D ortholog TSS scATAC Peak
identified. In other words, clock-like ChrAcc is an innate property measured EpiTrace age in single cells and compared the EpiTrace
on the clock-like loci, which usually harbor ClockDML. Furthermore, prediction with biological age predicted by whole-genome bisulfite
clock-like ChrAcc is independent from DNAm. sequencing (WGBS) of the same cultures59. Both DNAm-based predic-
tion of sample age (Fig. 3b) and single-cell age predicted by EpiTrace
The reversal of epigenetic age during iPSC induction (Fig. 3c) suggest that mitotic age increases as cells undergo transforma-
We tested EpiTrace on a single-cell multiome (scMultiomic) sequencing tion, with single-cell age gradually increasing across the evolutionary
dataset (CNP0001454 (ref. 59)) of primed human embryonic stem cell trajectory toward the 8CL state (Supplementary Fig. 20). Furthermore,
(‘Primed’ hESC) cultures undergoing chemical reprogramming through the biological age estimation of DNAm and EpiTrace was precisely
a ‘4CL naive PSC’ state toward an eight-cell-like (‘8CL’) state (Fig. 3a), correlated (correlation coefficient of mean single-cell (sc) EpiTrace
Nature Biotechnology
Developmental
time
EpiTrace age (single cell)
)gniyal
gge
retfa
sruoh(
emit
noitcelloc
oyrbmE
f Drosophila embryonic development
GSE190130
00–02
01–03
02–04
03–07
04–08
06–10
08–12
10–14
12–16
14–18
16–20
0 0.25 0.5 0.75 1
w
2
EpiTrace age
(single cell)
sepyt
lleC
Sample
time
Cell
no.
(Z)
UN
Gill.progenitor
Gill.stroma
Dor.mesenchyme
Front.mesenchyme Dor.stroma
Ven.stroma
Perichondrium
Dermal.FB
Cartilage
Bone Mesenchyme
Stroma
Perivascular
Teeth
Periosteum
Tendon
Stroma/teeth
Ven.stroma2
Gill
0 0.5 1
5.1 2 3 5 m
2
m
7
2
–2
Sample time: days post fertilization (dpf, log-ed)
)llec
elgnis
naem(
ecarTipE
0.8 R = 0.97, P = 0.00035
0.7
0.6
0.5
0.4
3 10 30 100
Fig. 2 | Mapping ClockDML orthologous genomic regions across species counterparts of human clock genomic loci in the Drosophila genome. Human
facilitates single-cell age estimation using ChrAcc. a, Schematic of the ClockDML falling within ±100 bp of the gene transcription start site (TSS) were
experiment. Human ClockDML are mapped to the zebrafish genome by defined as ‘Promoter ClockDML’. For human genes that simultaneously have a
homology to produce ‘human-guided reference clock-like loci’ and are then used promoter ClockDML and one or more Drosophila ortholog gene(s), we define any
to infer zebrafish neural crest cell mitotic age. Because the data were provided Drosophila scATAC peaks falling within ±100 bp of the TSSs of these Drosophila
as a one-hot matrix, we adopted the bulk ATAC-like algorithm output. b, Linear orthologs as putative clock-like genomic loci. These loci were subsequently used
regression of predicted mean mitotic age (y axis) against log-transformed for EpiTrace analysis in the Drosophila dataset. e, Diagram showing the number
(log-ed) days post-fertilization (dpf) of the sample (x axis). 95% CI is shown of ClockDML and scATAC falling in each category. H-D: human-drosophila pair.
as a gray area around the linear regression line. c, Single-cell mitotic age of f, EpiTrace age of Drosophila embryonic development time series samples taken
each cell type (left) and cell-type-specific prevalence (Z-scaled, Z) in samples every 2 hours after egg laying (GSE190130 (ref. 53)). Corresponding embryo
of different ages (right). Sample numbers of biological independent cells: sketches are shown on the right. Sample number of biological independent
n = 11,234 (UN, undefined); 2,223 (gill progenitor); 2,408 (gill stroma); 2,877 cells: n = 20,000 for each time slot. For box plots, the upper and lower bounds
(dorsal mesenchyme); 1,363 (frontal mesenchyme); 2,060 (dorsal stroma); 1,412 of boxes show 25% and 75% percentiles of the data. The median of data is shown
(ventral stroma); 2,373 (perichondrium); 265 (dermal FB); 3,252 (cartilage); as the horizontal line in the box. The distribution minima and maxima, defined
1,656 (bone); 1,716 (mesenchyme); 1,262 (stroma); 382 (perivascular); 623 as farthest data point distanced ≤1.5 IQR from the box bounds, are shown by the
(teeth); 2,123 (periosteum); 2,825 (perichondrium); 1,329 (stroma/teeth); whiskers. The violin plot shows the empirically estimated density distribution of
1,009 (ventral stroma 2); and 7,127 (gill). d, Schematic of defining putative datam. m, months; w, weeks.
Article https://doi.org/10.1038/s41587-024-02241-z
age × mean DNAm age: 0.998 (P = 0.04); scEpiTrace age × mean DNAm day 14 (D14) and day 20 (D20). Cells were clustered by their transcrip-
age: 0.526 (P = 1.9 × 10−38)) (Fig. 3d). While RNA velocity projections on tomic (scRNA) phenotype as progenitor (Prog) cells, differentiated
these cells showed erroneous evolution trajectories rooted at single (Diff) cells or terminally (Terminal) differentiated cells, which gradu-
cells of a differentiated state (Supplementary Fig. 21), combining RNA ally emerged over days in culture (Fig. 4b and Supplementary Fig. 22).
velocity and EpiTrace age of the same cell results in more biologically Furthermore, they were segregated into lineages (clones) arising from
plausible evolution trajectories with the primed hESC as the root of all the same progenitor by mitochondrial single-nucleotide variant (SNV).
other cells (Fig. 3e and Supplementary Fig. 21). These results suggest We used EpiTrace to predict mitosis age in these cells, separately
that ChrAcc on ClockDML predicts single-cell biological age at least as for myeloid lineage and erythroid lineage cells. Because the single-cell
well as the DNAm-based age estimator, even in an age-reverse scenario. age prediction by EpiTrace could be affected by highly biased cell
We measured EpiTrace age in an additional scATAC-seq dataset composition (Supplementary Fig. 23), we selected a relatively bal-
of cells undergoing the early stages of chemical reprogramming from anced CD34_800 dataset for erythroid lineage cell age prediction.
differentiated endodermal cells (fibroblast (FB) or mesenchymal stem Both CD34_500 and CD34_800 datasets were used for myeloid lineage
cell (MSC)) toward iPSCs (Fig. 3f; GSE178324 (ref. 60)) and compared cell age prediction.
them with WGBS-predicted ages from the same study. EpiTrace age The age prediction shows high concordance with known sampling
prediction of single cells significantly decreased at stage II compared days across cell types and enables tracking the mitosis age of individual
to the uninduced state (Fig. 3g), indicating that these cells are ‘rejuve- cells derived from the same clone (Fig. 4g). For the myeloid lineage, the
nated’ as expected. Compared to uninduced cells, the EpiTrace age of EpiTrace age of cells from the same clone increased from progenitor
stage II reprogrammed C6NYSA + T5J cells is significantly rejuvenated to terminal myeloid cells (Fig. 4c,d). Forced differentiation increased
(decreased). Removal of 5-azaC from the treatment result only slightly the age of differentiated cells as expected but decreased the age of
impairs the ChrAcc age rejuvenation as reflected by EpiTrace age. On terminal cells (Fig. 4c,d). To explore this phenomenon in depth, we
the contrary, removal of the JNK inhibitor from the treatment resulted classified clones according to the relative age change between days of
in more significant impairment of rejuvenation (Fig. 3g). The age–peak culture (Supplementary Fig. 24): clones that exhibited an age increase
association from the MSC reprogramming experiment is highly similar from D8 to D14 in a cluster were classified as ‘Aged’, and those that
to that from the FB reprogramming experiment. (Fig. 3h). These results exhibited an age decrease from D8 to D14 were classified as ‘Rejuve-
suggest relevance between the observed mitotic age resetting and cell nated’. Although most progenitor and differentiated cells show clonal
fate reprogramming. aging during induction, clonal rejuvenation dominates the terminally
The DNAm-predicted age of cells during the chemical induction differentiated clusters (Fig. 4c,d). The proportion of clones showing
procedure shows that the biological age first increases at induction a rejuvenation increase in terminal cells (Fig. 4d), in correlation with
stage II (Fig. 3i; GSE178966 (ref. 60)) before decreasing to near zero in the their differentiation state, suggests that these terminally differentiated
pluripotent state. Removal of 5-azaC from the induction formula blocks cells were derived from younger hematopoietic progenitors instead of
the DNAm age increase at stage II, indicating that the apparent DNAm existing intermediate differentiated cells.
age increase is a result of global DNA demethylation31. Similar to our To validate this hypothesis, we analyzed the expansion capabil-
previous observations, comparing the DNAm age and EpiTrace age ity of different cell clones, which processes different types of pro-
prediction of the same cell sets suggests that ChrAcc on ClockDML is liferating cells, including progenitor (Prog) cells and intermediate
independent from ClockDML DNAm change (Fig. 3j). (Int) differentiated cells, from the CD34_800 experiment (which was
sequenced on all three timepoints). We first classified the cell clones
Epigenetic age determines future cell expansion potential according to their cell composition on D8 (the first timepoint): at
To test EpiTrace age estimation in genetically defined cell lineages, this time, clones with only Prog cells but no Int cells were classified as
we took advantage of a mitochondria-enhanced scATAC-seq dataset ‘Prog-only’; clones with only Int cells but no Prog cells were classified
(GSE142745 (ref. 8)) of cultured CD34 hematopoietic stem cells (HSCs) as ‘Int-only’; and clones with both Int and Prog cells were classified as
that underwent in vitro expansion for 14 d before being forced into ‘Both’ (Supplementary Fig. 25a). The mean EpiTrace age of the clones
differentiation under SCF/IL3/EPO toward myeloid/erythroid lineages at the initial timepoint was measured as mean EpiTrace age of cells
for an additional 6 d (Fig. 4a). These cells were sequenced at day 8 (D8), from D8 (Supplementary Fig. 25b,d). We then tracked their clonal
Fig. 3 | Inferring single-cell age reversal in iPSC induction with EpiTrace. estimated with EpiTrace from f. The induced cultures were either subjected to
a, Schematic overview of the in vitro chemical induction of human pluripotent the full induction paradigm (+Chem: C6NYSA + T5J) or had 5-azaC or JNKin8
stem cells (‘Primed’) back to 8-cell like cell (8CLC) state, through serially culturing removed (−5aza, −JNKin8). Sample numbers of biologically independent cells:
in 4-cell-like medium (4CL, three passages (P3)) and the enhanced 4CL-medium n = 8,826 (uninduced); 4,667 (+Chem, −JNKin8); 10,257 (+Chem, −5aza); and
(e4CL). b, DNAm age of D0 (day 0, Primed) and D12 (day 12, 4CL) cultures and 8,671 (+Chem stage II). Statistical comparisons are shown between groups by
sorted 8CLCs from D17 (day 17) culture, from WGBS data. n = 2 independent two-sided Wilcoxon test. h, Correlation coefficient between the ChrAcc on
biological repeats in each group. c, Single-cell age estimated with EpiTrace from each ATAC peak and EpiTrace age estimated from the MSC experiment (x axis)
the D17 scMultiomic dataset. Sample numbers of biologically independent cells: or the FB experiment (y axis). Peaks of interest are labeled, colored by their
n = 483 (primed); 33 (interim); and 61 (8CLC). d, Correlation of inferred age from genomic location class. i, Prediction of sample age by DNAm from WGBS data of
DNAm (whiskers denote minimum/maximum, central point denotes median chemical induction of iPSCs. Chemical reprogramming induces genome-wide
value, y axis) or single-cell EpiTrace age (whiskers denote 25%/75%, central point demethylation and an increase in DNAm age, as reported previously31, whereas
denotes median value, x axis) from the same set of cells. Correlation R and the addition of 5-azaC globally reduces DNAm to increase DNAm age. Removal
P value: Pearson’s. Sample numbers of WGBS and single cells were as in b and c. of 5-azaC blocks DNAm age from increasing. Sample numbers of biologically
e, UMAP of scMultiomic-sequenced D17 culture with single-cell evolution independent samples: n = 4 (uninduced); 2 (C6NYSA); 1 (−JNKIN8); 1 (−5azaC);
trajectories built with kernels combining EpiTrace age and RNA velocity 2 (C6NYSA + T5J); and 4 (iPSC/hESC). j, Scatter plot of WGBS DNAm age (x axis)
information. f, Schematic overview of the in vitro chemical induction of human and mean single-cell EpiTrace age (y axis) of the same sample. For box plots,
adult fibroblasts toward chemically induced pluripotent stem cells (CiPSC). Both the upper and lower bounds of boxes show 25% and 75% percentiles of the data.
the uninduced and intermediate stage II cultures were sequenced by scATAC. The median of data is shown as the horizontal line in the box. The distribution
5-azaC, 5-azacytidine; C6NYSA, combination of CHIR99021, 616452, TTNPB, minima and maxima, defined as farthest data point distanced ≤1.5 IQR from the
Y27632, SAG and ABT869; hADSC, human adipose stromal cell (mesenchymal box bounds, are shown by the whiskers. The violin plot shows the empirically
stromal cell); HEF, human embryonic fibroblast; JNKIN8, c-Jun N-terminal estimated density distribution of data. Corr.coef., correlation coefficient.
kinase inhibitor; T5J, tranylcypromine, JNKIN8 and 5-azaC. g, Single-cell age
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
derivatives at the next timepoints (D14 and D20) to see if a clone was At both D14 and D20, the log clonal expansion ratio was inversely
expanded (defined as an increased terminally differentiated cell num- correlated with the initial EpiTrace age of the clone (Fig. 4f,i and Sup-
ber at later timepoints compared to D8). For each expanded clone, we plementary Fig. 25c,e): the correlation between the log clonal expan-
calculated the clonal expansion ratio, defined as the increased num- sion ratio and initial clonal age was R = −0.66 (P = 2.3 × 10−8) for D14 and
ber of terminally differentiated cells divided by the total cell number R = −0.57 (P = 0.00058) for D20. Although Int-only clones expanded
on D8. better than Prog-only clones at earlier timepoints (Supplementary
a
D0 D12 D17
Primed 4CL 8CLC
Nature Biotechnology
)qeSemiT(
ega
mAND
60
40
20
0
8CLC
Interim/4CL
Primed
Corr.coef:
0.998 (P = 0.04) (mean) 0.526 (P = 2 × 10–38) (sc vs mean)
:xam–naidem–nim(
ega
mAND
)%001–%05–%0
b
D17 D17 D17
Primed Interim 8CLC
d Correlation DNAm × EpiTrace
60
40
20
0
0.25 0.5 0.75
EpiTrace age (min–median–max:
25%–50%–75%)
)cs(
ega
ecarTipE
c
1
0.75
0.50
0.25
0
Velocity + age trajectory
UMAP1
2PAMU
e
PPrriimmeedd
8CLC
IInntteerriimm
1
Age
0
Fibroblast
-> Dedifferentiate
Cell age reset
Fibroblasts scATAC
8–10 d
C6NYSA
Stage I Lin28A+
16–20 d Stage II
C6NYSA
Lin28A+
+
SALL4+ T5J –JNKIN8
-5–azaC WGBS
…
CiPSC
)qeSemiT(
ega mAND
Reprogramming stage
)naem(
ega ecarTipE
60
40 20
0
Uninduced Stage I Stage II CiPSC
BF ,)delacs-z(
noitalerroC
f g h
4 SOX4 GATA4 TET2 NANOG KLF4 SOX4 TET1 GATA6 GATA6 SOX4
2 KLF4 TET2
KLF4 KLF4 DNMT3A KLF4
SOX4 SALL4 Peak type
0 Distal
Exonic
LIN28A Intronic
–2 LIN28A Promoter -2 0 2 4 Correlation (z-scaled), MSC
i j
Cell
hADSCs_0618
HEFs_1117
HEFs_0127 Treatment Uninduced C6NYSA
–JNKIN8
–5azaC
C6NYSA+T5J
iPSC/hESC
+ rotibihni
KNJ
rotibihni
noitalyhtemed
4K3H
)enimorpyclynart(
hESC
-> 8-cell-like
Cell age not reset
Primed PSC WGBS
12 d
4CL, P3
scMultiomic
4CL naive PSC
5 d
e4CL
Others 8CLC
DNA methylation inhibitor (5azaC)
0.7 Treatment
–5azaC
–JNKIN8
0.6 sta R g e e p I r I ogram C Un 6 i N n Y d S u A ce + d T5J 0.5 m ing
to
0.4
30 40 50 60 70
DNAm age (TimeSeq)
ega
ecarTipE
8CLC
Wilcoxon test P < 2.22 × 10–16
P < 2.22 × 10–16
P < 2.22 × 10–16
P < 2.22 × 10–16 P < 2.22 × 10–16 1
0.5
0 Uninduced +C – h J e N m Kin8 +Che – m 5aza +C S h t e a m ge II
Reprogramming stage
Article https://doi.org/10.1038/s41587-024-02241-z
a b
Day 8
Day 14
Day 20
Prog
My4
Ery5–6
UMAP1
Nature Biotechnology
2PAMU
c
800 CD34+ HSC
My1–2
D0 Prog
Expanded clones
Ery1–3
D8
My1–3
Prog
Expanded clones
Ery1–4
D14
+SCF/IL3/EPO
Induced differentiation
D20
Prog Diff Terminal
ega
ecarTipE
naem
lanolC
d
Prog Diff Term.
1
0.9
0.8
0.7
0.6
0.5
8 14 20
Da
8
ys in
1 4
cul
2
tu
0
re
8 14 20 Prog
Prog_
my My1 My2 My3 My4
g
EpiTrace
age
e
Per-clone EpiTrace age
Myeloid spec Bipotent Erythroid spec
CD34_800_42 CD34_800_8 CD34_800_10
Day 8 Day 8 Day 8
h
Day 14 Day 14 Day 14
Day 20 Day 20 Day 20 1
0
.on
llec
lanimreT
1,500
1,000
500
0
D8 D14 D20
Derived
Old progenitor
from
clone with Young progenitor
)02D(
oitar
noisnapxe
gol
)41D(
oitar
noisnapxe
gol
f
Clone type
Both
10 Int
Prog
1
0.1
R = –0.66, P = 2.3 × 10–8
0.01
0.5 0.6 0.7 0.8 0.9
Mean initial age (D8)
i
Clone type
Both
Int
10
Prog
1
0.1 R = –0.57, P = 0.00058
0.5 0.6 0.7 0.8
Mean initial age (D8)
)%(
sllec
lanimreT
Prog
Diff
Terminal
100%
75%
50%
25%
0%
D8 D14 D20
oitar
enolc
detanevujeR
100%
75%
50%
25%
0%
Cell type
Derived
Old progenitor
from
clone with Young progenitor
Fig. 4 | Single-cell age estimation revealed that epigenomic age determines clonal EpiTrace age of the same clone (x axis). Clonal types are color-labeled.
clonal expansion potential. a, Schematic of the experiment. CD34+ HSCs g, EpiTrace age (color) of the single cells derived from a similar clone. Three
were used in the in vitro expansion/differentiation experiment. Cells were first clones with different fates are shown for example. The CD34_800_42 clone was a
expanded to D8 (CD34_500) or D14 (CD34_800) and then differentiated by SCF, myeloid-specific clone that generated only myeloid cells. The CD34_800_8 clone
IL-3 and EPO until D20. Mitochondrial mutations from the scATAC experiment was a bipotent clone that generated both myeloid and erythroid decedents. The
were used for tracking cells derived from similar clones. Cell phenotypes were CD34_800_10 clone was an erythroid-specific clone that generated predominantly
determined by the scATAC profile. b, Cells from experiments performed on D8, erythroid cells. h, Relative contribution of young proliferator clones (mean initial
D14 and D20, showing a gradual transition toward terminally differentiated clonal EpiTrace < 0.7) and old proliferator clones (mean initial clonal EpiTrace
myeloid (my4) and erythroid (ery6) cells. c, Tracking the mean EpiTrace age of age ≥ 0.7) in the terminal myeloid cell population at three timepoints. i, Scatter
each myeloid cell clone at each timepoint. Sample numbers of independent plot of the log clonal expansion ratio on D20 (y axis) compared to the mean initial
biological clones: n = 35 (Prog D8–D20); 10 (Diff D8–D20); and 67 (Terminal clonal EpiTrace age of the same clone (x axis). Clonal types are color-labeled.
D8–D20). d, Ratio of rejuvenated (clone age decrease over time) clones in all Correlation statistics (R and P value): Pearson’s. Group statistics: t-test, two-sided.
clones for the myeloid cells. The terminally differentiated cells are dominated For box plots, the upper and lower bounds of boxes show 25% and 75% percentiles
by rejuvenated clones. e, Number of terminal myeloid cells derived from young of the data. The median of data is shown as the horizontal line in the box. The
proliferator clones (mean initial clonal EpiTrace age < 0.7) and old proliferator distribution minima and maxima, defined as farthest data point distanced ≤1.5
clones (mean initial clonal EpiTrace age ≥ 0.7) at three timepoints. f, Scatter plot IQR from the box bounds, are shown by the whiskers. The violin plot shows the
of the log clonal expansion ratio on D14 (y axis) compared to the mean initial empirically estimated density distribution of data.
Article https://doi.org/10.1038/s41587-024-02241-z
Fig. 25c), the Prog-only clones caught up at the latter timepoint and HAVCR2) and tumor-reactive T cells (ENTPD1) were segregated into dif-
showed improved expansion potential (Supplementary Fig. 25e). ferent clusters. T cell markers (TOX2, ID2 and MAFA) and tissue-resident
We then re-classified the clones by their mean clonal age at D8 marker CXCR6 belong to the group of scATAC peaks that are mainly
into ‘young progenitor-derived clones’ (defined as the mean EpiTrace associated with age but are not associated with PD1 response (Fig. 5c,d).
age < 0.7) or ‘old progenitor-derived clones’ (defined as the mean Epi- The anti-PD1 response is not associated with cell age but, instead,
Trace age ≥ 0.7). The number of terminal cells derived from young clones with C1 peak expression. In contrast, cell age is associated with C2/C3
steadily increased during the stimulation timecourse, outnumbering the peaks, which are related to no response under anti-PD1. Gene Ontology
terminal cells derived from old clones on D20 (Fig. 4e). As a result, the rela- (GO) enrichment of this C1 cluster, in contrast to C2/C3 cluster genes,
tive contribution of terminal cells from young clones steadily increased showed particular enrichment in the ‘cytokine receptor’ and ‘immune
during the stimulation timecourse (Fig. 4h and Supplementary Fig. 25f,g), receptor’ pathways (Fig. 5e and Supplementary Fig. 26), highlighting
explaining the observed decrease in terminal cell EpiTrace age (Fig. 4c,d). genes such as IL4R, CD74, IFNGR2 and IFNAR2, which might be impli-
Combining the observations, we conclude that the clonal expan- cated in the anti-PD1 response. Finally, we identified that cis-regulatory
sion potential is better explained by clonal epigenetic age instead of loci of a co-receptor and negative regulator of TGF-β, CD109 (Fig. 5f),
the initial phenotype of proliferating cells in the clone. Interestingly, and the nicotinic acetylcholine receptor CHRNA1 (Fig. 5g), are specifi-
the initial clonal age in clones with both Prog and Int cells was signifi- cally activated in response-associated T cells, suggesting targets for
ex
cantly older than that in Prog-only or Int-only clones (Supplementary future research.
Fig. 25b,d). These clones expanded the least at both timepoints (Fig. 4f,i
and Supplementary Fig. 25c,e). This result indicates that cells in these Revealing developmental history during cortical gyrification
clones, although phenotypically classified as capable of proliferation, To test how mitotic age estimation might complement RNA-based
are at the end of their expansion potential. development analysis, we applied EpiTrace to a scMultiomic dataset
Together, these results support the model that, during in vitro from the post contraception week (pcw) 21 human fetal brain cortex
HSC-stimulated expansion, terminally differentiated cells are prefer- (GSE162170 (ref. 65)) to study the trajectory of glutaminergic neuron
entially derived from younger progenitors. In other words, younger (GluN) development (Fig. 6a). GluNs develop from radial glia (RG)
hematopoietic progenitor cells are much more capable of expansion through the cycling progenitor (Cyc. Prog) cells into neuronal inter-
and differentiation. In the seminal study in which Hayflick determined mediate progenitor cells (nIPCs), before undergoing a cascade of matu-
the in vitro passage limit of cultured cells61, he co-cultured 46,XX and ration (GluN1 > GluN2 > GluN3 > GluN4 > GluN5)65–67. We modeled the
46,XY cells with different in vitro passage numbers together. By count- cell fate transition by CellRank68 with kernels built with RNA velocity,
ing the karyotypes of cells in the final passage population, he found that CytoTRACE (an RNA-based index of cell differentiation state), EpiTrace
the ‘younger’ cells with less starting passage number always dominated age or a combined kernel with all three estimators. Although RNA veloc-
the final passage population. Our current experiment is, by design, ity and CytoTRACE produced inconsistent transition trajectories that
similar to Hayflick’s original experiment by using a genetic marker, pointed toward a group of nIPCs (Fig. 6b, i and ii), kernels with EpiTrace
mitochondrial mutation, to track each clone. By measuring the ‘clonal age revealed a correct direction of development from the nIPCs toward
age’ of these single cells, EpiTrace derived a quantitative measure of terminally differentiated neurons (Fig. 6b, iii). The combined kernel
future expansion potential against the current age of the clone. A pio- of all three estimators resulted in a biologically plausible transition
neering study showed that the genome-wide DNAm level decreases dur- trajectory that starts from RG to bifurcate into two different branches,
ing cell culture passage62. This phenomenon was later used to propose each giving rise to a distinct nIPC population that differentiates into
a method to infer Hayflick’s limit for individual cell lines63. This result mature neurons (Fig. 6a).
provided experimental evidence for the pioneering theoretical works. Two transcription factors, TCF4 and NR2F1 (encoding the tran-
scription factor COUP-TFI), were differentially expressed between
Elucidating T cell markers underlying anti-PD1 response the branches. They exhibit significant differential binding activities
The CD34 dataset demonstrated above is based on an ideal in vitro sce- in these neurons (Fig. 6c). Interestingly, NR2F1 is mainly expressed in
nario with cells cultured in an isolated dish. The cultures start at a similar the gyrus of the human cortex, and hereditary NR2F1 loss-of-function
starting point. They proliferate and die in the dish, without exchange with mutations are associated with mental retardation and the polymicro-
the external environment. To test EpiTrace in a more complex cell popu- gyri phenotype69–71. NR2F1 TFBS-associated peaks are open in a branch
lation in an in vivo setting, with possible influx, efflux and proliferation, (Fig. 6d) that is NR2F1 negative (Fig. 6e) and LMO3 positive (Fig. 6f),
we applied EpiTrace to an scATAC-seq dataset comprising biopsies from suggesting that NR2F1 turned into a transcriptional repressor in nIPCs.
basal cell carcinoma pre-anti-PD1 and post-anti-PD1 treatment (Fig. 5a; The EpiTrace age of the NR2F1+ branch nIPC was significantly higher
GSE129785 (ref. 64)). After anti-PD1 treatment, cytotoxic T cells with than that of the LMO3+ nIPC, suggesting increased mitotic activity
exhaustion markers are significantly increased in anti-PD1 responders (R) (Fig. 6g). In concordance with this, the CytoTRACE score of NR2F1+ nIPC
but not in non-responders (NR). More immature exhausted T (T ) cells was lower than that of LMO3+ nIPC (Fig. 6h), suggesting increased dif-
ex
were present in non-responders, and this phenomenon was exaggerated ferentiation. These results indicate that nIPCs are divided into NR2F1+
after anti-PD1 treatment. However, overall maturity did not change in clones that support earlier neurogenesis and LMO3+/NR2F1− clones that
responders. The EpiTrace age of interim and mature T cells in responders expand relatively later, linking the gyrus-specific expression pattern
ex
did not change after the anti-PD1 treatment, suggesting that the increased of NR2F1 to its function in cortical gyrification69.
cell number might not be solely due to local proliferation of pre-anti-PD1 We compared the EpiTrace age of the neurons with their CytoTRACE
mature T cells (Fig. 5b). score (Fig. 6i). Although the CytoTRACE score of GluNs correlates with
ex
New post-anti-PD1 mature T cells could be derived either from their differentiation, the EpiTrace age of these cells is inversely corre-
ex
pre-anti-PD1 immature T cells or from the influx of peripheral T cells. lated with their maturity. To explain this inconsistency, we built a ‘phy-
ex
To test these alternatives, we performed a correlation of ChrAcc on T logenetic tree’ of single cell clusters with ClockDML ChrAcc (EpiTrace
ex
differentially expressed peaks and cell age. Hierarchical clustering of phylogeny). We reasoned that cells traverse on the phenotype manifold
the peak openness of pseudobulk cells from similar age and pheno- on branched trajectories while they undergo mitosis. As they evolve,
type segregated peaks into three clusters: C1: response-specific and ChrAcc on ClockDML converges into a specific state that should be
age-independent; C2: response-irrelevant and age-associated; and lineage dependent because of the irreversible nature of such change.
C3: non-response-specific peaks that were weakly associated with age Hence, it is possible to infer cell lineage trees using phylogenetic-like
(Fig. 5c,d). Interestingly, known markers of activated (TIGIT, LAYN and methods. Such analysis revealed a birth sequence of GluNs: GluN5 is
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
a Basal cell carcinoma b Cell binned by phenotypic maturity and treatment response
CD8 T ex early CD8 T ex early Biopsy
Treatment
naive
intermedi T a e t x e l T a e t x e intermedia T t e e x T la e t x e
scATAC
Anti-PD1
After
treatment
Biopsy
Non-responder Responder
Nature Biotechnology
rebmun
lleC
ega
ecarTipE
Treatment
Pre-PD1 Post-PD1
NR NR NR R R R Immature Interim Mature Immature Interim Mature
1,000
100
10
1
NR NR NR R R R
Immature Interim Mature Immature Interim Mature
1.00
0.75
0.50
0.25
0
D1D1 D1D1 D1D1 D1D1 D1D1 D1D1
Pre-P Post-P Pre-P Post-P Pre-P Post-P Pre-P Post-P Pre-P Post-P Pre-P Post-P
c Cell binned by age and sample
C1
Response-specific
Age-independent
CD109;
CHRNA1;
ADORA2A;
MCHR1 HAVCR2; IL4R
C2
Age-associated
TOX2; ID2;
CBX8; IZUMO4;
IRF4; MAFA;
LAYN; SKI;
CD74; CXCR6
kaep
no
CATAcs
d f
Cell Response-specific CD109 peak
PD1 R age
PD1 R C3 C2 C1
Age 0.5
1 – –
PD1
+ –
R 0.1
C3 – + 0 1.00
–1 C2 Cell age X: insignificant + +
Pre-PD1, responder
Post-PD1, non-responder
e Pre-PD1, non-responder
Post-PD1, responder
CD109
g
Cell Response-specific CHRNA1 peak
PD1R age
C3
No-response-specific
weak age-associated – – 0.6
CD80; SKI; + –
TIGIT; DPP8; 0.2 CASP9; IRF4
– +
NR Pre-PD1
R Post-PD1 + +
0 0.3 Correlation age × peak Pre-PD1, responder
Post-PD1, non-responder
0 100 sc EpiTrace age Pre-PD1, non-responder
CHRNA1 Post-PD1, responder
feoc
.rroC
Treatment
Pre-PD1 Post-PD1
GO:C1
Cytokine receptor
Immune receptor
TF activity, Pol2-spec
TF activity
Chromatin DNA binding
Cytokine binding
Coreceptor activity
Pol2-spec TF binding
Count 6 8 10 12
–log P value
6 5 4 3 2 0 1.00
–log q value Cell age
8 6 4
Fig. 5 | Single-cell age estimation facilitates the discovery of molecular clusters. d, Correlation coefficient between clusters of peaks and treatment
markers of peripheral influx T cells underlying the anti-PD1 response. (PD1: pre/post = 0/1), response (R: NR/R = 0/1) and cell age (Age). Non-significant
a, Schematic overview of the experiment. Biopsies were taken from patients correlations are labeled with ‘X’. e, GO enrichment of the C1 cluster peaks
with basal cell carcinoma before (pre) and after (post) anti-PD1 treatment and as in c. Enrichment was tested by one-sided Fisher’s exact test. −logP values
subjected to scATAC-seq. b, Cell number (above) and EpiTrace age (below) of T were adjusted by multiple comparison. f, ChrAcc (top) and cross-correlation
ex
cells, separated by treatment response (R: responder; NR: non-responder) and between peaks (bottom) of CD109 loci from pseudobulk single cells grouped
T cell phenotypic maturity (Immature/Interim/Mature). Sample numbers of with phenotype (R/NR), sample (pre-PD1 or post-anti-PD1) and EpiTrace age
independent biological cells: n = 322 (NR group, Immature cell, Pre-PD1); (Young/Interim/Mature). The association of the CD109 promoter ChrAcc across
596 (NR group, Immature cell, Post-PD1); 77 (NR group, Interim cell, Pre-PD1); age is shown in the right panel. g, ChrAcc (top) and cross-correlation between
108 (NR group, Interim cell, Post-PD1); 97 (NR group, Mature cell, Pre-PD1); peaks (bottom) of CHRNA1 loci from pseudobulk single cells grouped as in f.
14 (NR group, Mature cell, Post-PD1); 77 (R group, Immature cell, Pre-PD1); 237 The association of the CHRNA1 promoter ChrAcc across age is shown in the right
(R group, Immature cell, Post-PD1); 222 (R group, Interim cell, Pre-PD1); 923 panel. Correlation test: Pearson’s. For box plots, the upper and lower bounds of
(R group, Interim cell, Post-PD1); 378 (R group, Mature cell, Pre-PD1); and boxes show 25% and 75% percentiles of the data. The median of data is shown as
2,452 (R group, Mature cell, Post-PD1). c, Heatmap showing scATAC peak activity the horizontal line in the box. The distribution minima and maxima, defined as
in pseudobulk single cells grouped by phenotype (R/NR), sampling time (pre- farthest data point distanced ≤1.5 IQR from the box bounds, are shown by the
PD1 or post-anti-PD1) and EpiTrace age. Correlations between peak activity whiskers. The violin plot shows the empirically estimated density distribution of
and EpiTrace age are shown on the left. Peaks were clustered according to their data. Corr.coef., correlation coefficient.
activity profile into response-specific, non-response-specific and age-associated
Article https://doi.org/10.1038/s41587-024-02241-z
a NR2F1 scATAC TF activity
High
Low
–logP of differential
gene exp
Nature Biotechnology
laitnerdffid
fo
Pgol–
ccArhC
SBFT
c d
150 scMultiome TCF4
100
scATAC > EpiTrace + UMAP NR2F1
scRNA > velocity + CytoTRACE
cell fate deduction: CellRank 50
pcw21 0
0 50 100
e NR2F1 scRNA expression f LMO3 scRNA expression
2PAMU
In1
Cyc.prog In3
RG
nIPC In2
GluN2
OPC
GluN3
GluN5
Trajectory with EpiTrace GluN4 combined with
RNA velocity and CytoTRACE
UMAP1
b
CytoTRACE only RNA velocity only EpiTrace age
nnIIPPCC nnIIPPCC AAccttiivvee
pprroolliiff.. ssiinnkk ssiinnkk nnIIPPCC 1
GGlluuNN
ssaaddddllee
0
i
EC/peric
EpiTrace phylogeny
IN1
IN2
GluN3
IN3
mGPC/OPC nIPC/GluN1
SP
GluN2
GluN5
GluN4 GluN4
GluN3 GluN5
GluN2
RG
nIPC/GluN1
Cyc. prog SP
RG
0 0.5 1 1 0.5 0
EpiTrace age CytoTRACE
epyt
lleC
j k
ega
ecarTipE
P < 2.2 × 10–16
1.00 1.00
0.75
0.75
0.50
0.50
0.25
0.25
0
LMO3+ NR2F1+ LMO3+ NR2F1+
ECARTotyC
High High
Low Low
g h
P = 0.017
G
yru
s
N
R
2F1+
N
R2F1+
Sulcus
Early expanding
maintains P N Early generated: GluN4/5
division
Post mitotic
maturation
Late expanding
switch to N N
Late generated: GluN2/3
division later
LMO3+
Fig. 6 | EpiTrace reveals the developmental history during human cortical and 1,198 (NR2F1+). P < 2.2 × 10−16 (Wilcoxon test, two-sided; the P value resulted
gyrification. a, UMAP projected cell evolution trajectory built with CellRank in numerical underflow). h, CytoTRACE of cells belong to the LMO3+ population
by using a hybrid kernel of EpiTrace, CytoTRACE and RNA velocity of an or NR2F1+ population. Sample numbers as in g. P = 0.017 (Wilcoxon test, two-
scMultiomic-seq dataset from a pcw21 human brain. EC, endothelial cell; sided). i, Mitotic clock (EpiTrace) and differentiation potential (CytoTRACE) of
IN, inhibitory GABAergic neuron; mGPC/OPC, medial ganglionic eminence the same cell in scMultiomic-seq. The CytoTRACE score was reversed to show
progenitor/oligodendrocyte precursor cell; SP, subplate neuron. SPs and ECs are differentiation from left to right to facilitate comparison with EpiTrace. Sample
not shown in the figure due to space limitations. b, Trajectories built with only numbers of biologically independent cells: n = 646 (RG); 341 (Cyc. Prog.); 2,348
CytoTRACE (i) or RNA velocity (ii) resulted in unrealistic ‘sinks’ and ‘saddles’ on (nIPC/GluN1); 1,546 (GluN2); 798 (GluN3); 459 (GluN4); 223 (GluN5); 190 (SP);
the map. In contrast, EpiTrace age (iii) provided a unidirectional reference of time 359 (mGPC/OPC); 301 (IN3); 780 (IN2); 959 (IN1); and 31 (EC/Peric.). j, Excitatory
to reveal that the ‘sink’ nIPC population is mitotically active to resolve the ‘nIPC neuron phylogeny built with mitotic clock, showing that GluN4/GluN5 are likely
stall’. c, Scatter plot of the differential gene expression estimate (−logP value, direct, early-born progenies of RG, whereas GluN2/GluN3 are likely late-born,
x axis) and differential TFBS-specific ChrAcc estimate (−logP value, immature progenies of nIPC. k, Overall model of corticogenesis in the light of
y axis) in the GluN cells. Most significantly differential expressed transcription EpiTrace. Data source: Trevino et al.65. For box plots, the upper and lower bounds
factors NR2F1 and TCF4 are highlighted in the figure. Differential expression of boxes show 25% and 75% percentiles of the data. The median of data is shown
was estimated by non-parametric Wilcoxon rank-sum test. d, UMAP of TFBS- as the horizontal line in the box. The distribution minima and maxima, defined
specific ChrAcc of NR2F1. e, Expression of NR2F1 on UMAP. f, Expression of LMO3 as farthest data point distanced ≤1.5 IQR from the box bounds, are shown by the
on UMAP. g, EpiTrace age of cells belong to the LMO3+ population or NR2F1+ whiskers. The violin plot shows the empirically estimated density distribution of
population. Sample numbers of biologically independent cells: 808 (LMO3+) data.
Article https://doi.org/10.1038/s41587-024-02241-z
first divided from RG, followed by GluN4, GluN2, GluN3 and GluN1/nIPC a pre-malignant cluster (7) that is younger than all malignant clones
(Fig. 6j), indicating that neurons that formed earlier undergo longer (4/6/5/0/3) but shows accelerated aging/mitosis count compared to
post-mitotic maturation (Supplementary Fig. 27). In concordance the ‘normal clones’ (1/9) (Extended Data Fig. 2b,f), has lower MDM4
with this observation, by analyzing scRNA expression of the same cells, amplification (Extended Data Fig. 2c) and is without either EGFR or
we found that, whereas the late-aged nIPC/GluN1 and GluN2 cells still PDGFRA amplification (Extended Data Fig. 2d–e).
showed reminiscent RNA expression of the proliferating cells, such as Interestingly, some MDM4+ cells had both EGFR and PDGFRA ampli-
SOX11, SOX4, MALAT1 and NFIB, the earlier-aged, ‘more mature’ GluN5 fication (Supplementary Fig. 32). EpiTrace age analysis revealed that the
and GluN4 cells showed significantly increased expression of mature MDM4+-only cells are ancestral to triple-positive, EGFR+/PDGFRA+ cells,
neuron markers, including synaptic proteins, including SYT4, SYT11, followed by loss of either EGFR or PDGFRA in the progeny (Extended
FABP7, APP, GAP43 and PCDH17; mature neuron cytoskeleton proteins, Data Fig. 2f). This is further supported by EpiTrace phylogeny analysis
such as TUBB2A and NEFL; and post-mitotic functioning transcription (Extended Data Fig. 2g). Branched evolution of MDM4+/EGFR+ and
factors, such as MEF2C (Supplementary Fig. 28). Furthermore, in con- MDM4+/PDGFRA+ cells was initiated at the beginning of malignant
cordance with the known ‘inside-out’ developmental paradigm of the transformation (Supplementary Fig. 32). Together, these results char-
cortex72, the earlier-aged GluN5 specifically expresses the layer V/VI acterized the evolutionary trajectory of malignancy from the MDM4+
marker genes SCUBE1 and SEMA3E73, whereas the younger GluN4 popu- pre-malignant clone to the earliest malignant cell population with
lation expresses similarly higher levels of the layer III/IV marker genes amplification of MDM4, PDGFRA and EGFR in a catastrophic genomic
NTNG1 and MME73 (Supplementary Fig. 29). Hence, the dynamics of instability event, which bifurcated into heterogeneous clones with
post-mitotic neurons undergoing continuous differentiation could be either PDGFRA or EGFR addiction (Extended Data Fig. 2h). EpiTrace age
captured by combining mitotic age with other modality measurements. analysis revealed the pre-malignant state of this tumor and suggested
Together, this analysis demonstrated that EpiTrace age analysis branching evolution of this tumor to indicate that heterogeneous
complements RNA velocity and stemness prediction in characterizing cancer clones arise early in malignancy transformation.
complex organ development; indicated a long post-mitotic maturation It was previously known that telomere crisis and mitotic
of neurons; and revealed the molecular mechanism of NR2F1 control- mis-segregation can cause catastrophic events in a single mitosis,
ling human nIPC proliferation to underlie cortical gyrification (Fig. 6k). most importantly chromothripsis77,78, chromoplexy79 and kataegis80.
Multiple structural variations over the genome can occur simultane-
Inferring gene function in kidney from a static snapshot ously during such events, resulting in a synchronous, punctuated burst
We already demonstrated that EpiTrace can track development using of chromosomal copy number aberration77,81. By timing the occurrence
developing tissues. To test whether EpiTrace can recover epigenomic time of these mutational events, it was identified that such events occur
changes during development from a single, terminally developed, early during oncogenesis82,83. PDGFRA and EGFR amplifications were
static snapshot from adult tissue, we applied EpiTrace to an scATAC-seq reported to exist in different single-cell clones that coexist in a mosaic
dataset from adult human kidney (Extended Data Fig. 1a; GSE166547 manner in GBM tumors84. Although most reports suggest that these
(ref. 74)). The birth sequence of kidney cells by EpiTrace phylogeny mutations are mutually exclusive in single GBM-derived cell lines or
analysis suggests an endothelial origin of kidney tubules and deline- tumor sphere cultures85, these clones coexist within the same tumor
ates a cell-type-specific generation cascade during nephrogenesis and share common somatic mutations, such as deletion of PTEN and
(Extended Data Fig. 1b), with correlation to their spatial position (Sup- CDKN2A84,86, indicating that they were derived from the same ancestral
plementary Fig. 30). The distribution of EpiTrace age for each cell type clone. scRNA-seq87,88 suggests that PDGFRA+/EGFR+ double-positive
suggests a distal-to-proximal genesis cascade of nephron tubules with cells exist in GBM. Single-positive PDGFRA+ or EGFR+ descendent clones
a late expansion of proximal tubules (PTs) (Extended Data Fig. 1c). could emerge from double-positive parental clones without specific
In the PT lineage, EpiTrace age-derived phylogeny could be orthog- selection86. These observations are similar to our observation with Epi-
onally validated with small nuclear RNA (snRNA)-derived phylogeny Trace. In our analysis, although we sampled only a fraction of the tumor,
(Supplementary Fig. 31; GSE121862 (ref. 75)). The correlation between the similar cell age estimated for MDM4+/EGFR+ and MDM4+/PDGFRA+
EpiTrace age and peak openness showed clear segregation of peaks clones suggested that neither of these clones gained selective advan-
opened in progenitor or differentiated PT cells (Extended Data Fig. 1d). tage during tumor growth. Instead, they are under neutral evolution.
Notably, such association is not guided by known cell type informa- Further experiments with higher-resolution clonal tracing, putatively
tion, indicating the power of EpiTrace in positioning single cells along with a genetic marker, are necessary to confirm this observation.
their evolutionary trajectory. Interestingly, the translocation renal
cell carcinoma (TRCC) driver gene TFEB is specifically activated in Discussion
progenitor cells and shows an age-dependent decrease in activity. In We formulated a model of clock-like ChrAcc change during cell mitotic
contrast, all hereditary renal dysgenesis (CAKUT) genes, FGF8, FGFR2, aging, leading to the discovery of a universal epigenomic hallmark dur-
SLIT3, GDNF and NHS, are associated with differentiated cell-specific, ing cellular development: ChrAcc across clock-like loci. The heterogene-
age-dependent increased peaks. These results suggest that CAKUT is ity of ChrAcc across clock-like loci is reduced at each mitosis, resulting
linked to genes functioning in terminal PT cell fate determination and in a converged, homogeneous activity pattern. We showed that ChrAcc
function, whereas TRCC oncogenesis is linked to the mis-expression of changes act upstream of clock-like DNAm changes. Counting the frac-
progenitor-specific transcription factors, possibly forcing the dedif- tion of opened clock-like loci of each cell gives a simple, phenotypic
ferentiation of terminally differentiated PT cells into a stem-like state. measure of cell mitotic age. We leveraged this measure to build a tool,
called EpiTrace, to predict cellular mitotic age. Furthermore, we showed
Tracking glioblastoma clonal evolution that the similarity across clock-like loci ChrAcc between single-cell clus-
Finally, we analyzed an individual tumor sample (CGY2349) in a human ters can serve as an accurate distance measure for phylogenetic analysis.
glioblastoma (GBM) scATAC-seq dataset to study whether EpiTrace age The DNAm shift in ClockDML is widely accepted as a hallmark of
analysis could work for cell evolution in oncogenesis (Extended Data aging. However, the molecular mechanism generating age-dependent
Fig. 2a; GSE139136, GSE163655 and GSE163656 (ref. 76)). In this tumor, DNAm is yet unknown. Our data indicated that sample ages predicted
copy number variation (CNV) analysis showed that MDM4 amplifica- by ChrAcc and DNAm were significantly correlated, suggesting that
tion dominates the malignant clones, which additionally have either they are possibly under the control of a similar biological process.
EGFR or PDGFRA amplifications, resulting in increased ChrAcc around ChrAcc changes accompany development and cell fate transition.
these genes (Extended Data Fig. 2b–e). With EpiTrace, we identified However, we noticed that ChrAcc on clock-like loci is phenotypically
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
neutral—that is, irrelevant to cell phenotype—based on several lines of References
evidence. First, EpiTrace age measured on the same set of clock-like loci 1. Buenrostro, J. D. et al. Single-cell chromatin accessibility
generated from one tissue lineage (for example, the ClockDML from reveals principles of regulatory variation. Nature 523, 486–490
human PBMCs) works for different lineages. Second, the EpiTrace age of (2015).
a single cell correlates with its accumulative mitosis number instead of 2. La Manno, G. et al. RNA velocity of single cells. Nature 560,
developmental maturity (for example, in the case of neuronal develop- 494–498 (2018).
ment). Third, clock-like loci derived from one species could be used to 3. Gulati, G. S. et al. Single-cell transcriptional diversity is a hallmark
predict single-cell age in another species. The exact molecular mecha- of developmental potential. Science 367, 405–411 (2020).
nism controlling how clock-like differential DNAm occurs on clock-like 4. Teschendorff, A. E. & Enver, T. Single-cell entropy for accurate
loci (to generate ClockDML), and how clock-like ChrAcc emerges on estimation of differentiation potency from a cell’s transcriptome.
these loci, is an interesting question awaiting future investigation. Nat. Commun. 8, 15599 (2017).
It is unexpected to us that the phylogenetic tree built with ChrAcc 5. Erhard, F. et al. scSLAM-seq reveals core features of transcription
on clock-like loci (EpiTrace phylogeny) for single-cell clusters of the dynamics in single cells. Nature 571, 419–423 (2019).
same developmental lineage is highly accurate. EpiTrace-inferred age 6. Granja, J. M. et al. ArchR is a scalable software package for
is similar to pseudotime-inferred cell ‘developmental time’ but with integrative single-cell chromatin accessibility analysis. Nat.
higher resolution and less variation (Supplementary Fig. 33). In fact, Genet. 53, 403–411 (2021).
we noticed that such phylogenetic trees sometimes outperform those 7. Ludwig, L. S. et al. Lineage tracing in humans enabled by
built with the highly variable peaks from scATAC-seq data in terms of mitochondrial mutations and single-cell genomics. Cell 176,
accuracy. Despite the fact that ClockDML (and clock-like loci) are highly 1325–1339 (2019).
enriched in cis-regulatory regions, there is no functional enrichment of 8. Lareau, C. A. et al. Massively parallel single-cell mitochondrial
them in specific developmental pathways or specific types of genomic DNA genotyping and chromatin profiling. Nat. Biotechnol. 39,
elements (in addition to active cis-regulatory elements). Furthermore, 451–461 (2021).
this phenomenon is also phenotypically neutral. These results not 9. Xu, J. et al. Single-cell lineage tracing by endogenous mutations
only suggest a consistent birth sequence of cell types within the line- enriched in transposase accessible mitochondrial DNA. eLife 8,
age but also indicate that senescence is a defined molecular process e45105 (2019).
across cell types. 10. Vaziri, H. et al. Evidence for a mitotic clock in human
Our study is not without limitations. We noticed that the quality of hematopoietic stem cells: loss of telomeric DNA with age. Proc.
inferred mitotic age by the current EpiTrace algorithm is dependent on Natl Acad. Sci. USA 91, 9857–9860 (1994).
sequencing depth (Supplementary Figs. 34–36). EpiTrace could be less 11. Hills, M., Lucke, K., Chavez, E. A., Eaves, C. J. & Lansdorp, P. M.
accurate when working on cells with low sequencing depth. Addition- Probing the mitotic history and developmental stage of
ally, EpiTrace could be inaccurate when the starting cell population hematopoietic cells using single telomere length analysis
is highly imbalanced (Supplementary Fig. 23). This phenomenon is (STELA). Blood 113, 5765–5775 (2009).
related to single-cell population heterogeneity across development, 12. Yatabe, Y., Tavare, S. & Shibata, D. Investigating stem cells in
the nature of ChrAcc shifts during mitotic aging, the statistical model human colon by using methylation patterns. Proc. Natl Acad. Sci.
underlying our algorithm and the limitations of the sequencing tech- USA 98, 10839–10844 (2001).
nique. Finally, the estimation accuracy and computational efficiency 13. Kim, J. Y., Tavare, S. & Shibata, D. Human hair genealogies and
of EpiTrace rely heavily on the enrichment of clock-like loci in the stem cell latency. BMC Biol. 4, 2 (2006).
initial reference loci set. In this view, the full set of scATAC-seq peaks 14. Lopez-Garcia, C., Klein, A. M., Simons, B. D. & Winton, D. J.
or solo-WCGW sites, although they may contain clock-like loci, are not Intestinal stem cell replacement follows a pattern of neutral drift.
sufficiently enriched (Supplementary Fig. 37). As a result, inferring cell Science 330, 822–825 (2010).
age from these reference loci is not as accurate as using the ClockDML 15. Snippert, H. J. et al. Intestinal crypt homeostasis results from
set that we provided for the algorithm (Supplementary Fig. 38). Fur- neutral competition between symmetrically dividing Lgr5 stem
thermore, using these loci as references is extremely computationally cells. Cell 143, 134–144 (2010).
inefficient and renders single-cell dataset analysis virtually impossible. 16. Gabbutt, C. et al. Fluctuating methylation clocks for cell lineage
Future improvement of the algorithm might require in-depth study tracing at high temporal resolution in human tissues. Nat.
of molecular mechanisms driving age-dependent ChrAcc changes on Biotechnol. 40, 720–730 (2022).
clock-like loci, improvements in the algorithm to adapt with low-quality 17. Bell, C. G. et al. DNA methylation aging clocks: challenges and
and highly imbalanced datasets and improvements in computational recommendations. Genome Biol. 20, 249 (2019).
efficiency. 18. Bocklandt, S. et al. Epigenetic predictor of age. PLoS ONE 6,
In conclusion, we showed mitosis-associated, age-dependent e14821 (2011).
ChrAcc on clock-like loci, which usually harbor ClockDML. Based on 19. Liu, L. et al. An integrated chromatin accessibility and
this phenomenon, we developed computational method EpiTrace to transcriptome landscape of human pre-implantation embryos.
track single-cell age using ChrAcc. By comparison studies, we showed Nat. Commun. 10, 364 (2019).
that the ChrAcc-based mitosis age measure complements somatic 20. Meer, M. V., Podolskiy, D. I., Tyshkovskiy, A. & Gladyshev, V. N.
mutation, RNA velocity and stemness predictions to predict the cell A whole lifespan mouse multi-tissue DNA methylation clock. eLife
evolution trajectory with improved precision and power. We expect 7, e40675 (2018).
EpiTrace to be a useful tool for single-cell studies for delineation of 21. Stubbs, T. M. et al. Multi-tissue DNA methylation age predictor in
cellular hierarchies and organismal aging. mouse. Genome Biol. 18, 68 (2017).
22. Thompson, M. J. et al. A multi-tissue full lifespan epigenetic clock
Online content for mice. Aging (Albany NY) 10, 2832–2854 (2018).
Any methods, additional references, Nature Portfolio reporting sum- 23. Petkovich, D. A. et al. Using DNA methylation profiling to evaluate
maries, source data, extended data, supplementary information, biological age and longevity interventions. Cell Metab. 25,
acknowledgements, peer review information; details of author con- 954–960 e956 (2017).
tributions and competing interests; and statements of data and code 24. Mayne, B. et al. A DNA methylation age predictor for zebrafish.
availability are available at https://doi.org/10.1038/s41587-024-02241-z. Aging (Albany NY) 12, 24817–24835 (2020).
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
25. Horvath, S. DNA methylation age of human tissues and cell types. 52. Lyko, F., Ramsahoye, B. H. & Jaenisch, R. DNA methylation in
Genome Biol. 14, R115 (2013). Drosophila melanogaster. Nature 408, 538–540 (2000).
26. Lu, A. T. et al. Universal DNA methylation age across mammalian 53. Calderon, D. et al. The continuum of Drosophila embryonic
tissues. Nat. Aging 3, 1144–1166 (2023). development at single-cell resolution. Science 377, eabn5800
27. Williams, G. C. Pleiotropy, natural-selection, and the evolution of (2022).
senescence. Evolution 11, 398–411 (1957). 54. Li, L. et al. Single-cell multi-omics sequencing of human early
28. Yang, Z. et al. Correlation of an epigenetic mitotic clock with embryos. Nat. Cell Biol. 20, 847–858 (2018).
cancer risk. Genome Biol. 17, 205 (2016). 55. Battaglia, S. et al. Long-range phasing of dynamic, tissue-specific
29. Youn, A. & Wang, S. The MiAge Calculator: a DNA methylation- and allele-specific regulatory elements. Nat. Genet. 54, 1504–1513
based mitotic age calculator of human tissue types. Epigenetics (2022).
13, 192–206 (2018). 56. Baumann, V. et al. Targeted removal of epigenetic barriers during
30. Kerepesi, C., Zhang, B., Lee, S. G., Trapp, A. & Gladyshev, V. N. transcriptional reprogramming. Nat. Commun. 10, 2119 (2019).
Epigenetic clocks reveal a rejuvenation event during embryo- 57. de Mendoza, A. et al. Large-scale manipulation of promoter DNA
genesis followed by aging. Sci. Adv. 7, eabg6082 (2021). methylation reveals context-specific transcriptional responses
31. Trapp, A., Kerepesi, C. & Gladyshev, V. N. Profiling epigenetic age and stability. Genome Biol. 23, 163 (2022).
in single cells. Nat. Aging 1, 1189–1201 (2021). 58. Parry, A. J. et al. NOTCH-mediated non-cell autonomous regulation
32. Klemm, S. L., Shipony, Z. & Greenleaf, W. J. Chromatin accessibility of chromatin structure during senescence. Nat. Commun. 9, 1840
and the regulatory epigenome. Nat. Rev. Genet. 20, 207–220 (2019). (2018).
33. Wiench, M. et al. DNA methylation status predicts cell 59. Mazid, M. A. et al. Rolling back human pluripotent stem cells to an
type-specific enhancer activity. EMBO J. 30, 3028–3039 (2011). eight-cell embryo-like stage. Nature 605, 315–324 (2022).
34. Pott, S. Simultaneous measurement of chromatin accessibility, 60. Guan, J. et al. Chemical reprogramming of human somatic cells
DNA methylation, and nucleosome phasing in single cells. eLife 6, to pluripotent stem cells. Nature 605, 325–331 (2022).
e23203 (2017). 61. Hayflick, L. The limited in vitro lifetime of human diploid cell
35. Lee, H. J. et al. Regenerating zebrafish fin epigenome is strains. Exp. Cell. Res. 37, 614–636 (1965).
characterized by stable lineage-specific DNA methylation and 62. Mazin, A. L. [Loss of total 5-methylcytosine from the genome
dynamic chromatin accessibility. Genome Biol. 21, 52 (2020). during cell culture aging coincides with the Hayflick limit]. Mol.
36. Pandiyan, K. et al. Functional DNA demethylation is accompanied Biol. (Mosk.) 27, 895–907 (1993).
by chromatin accessibility. Nucleic Acids Res. 41, 3973–3985 (2013). 63. Mazin, A. L. Life span prediction from the rate of age-related DNA
37. Thurman, R. E. et al. The accessible chromatin landscape of the demethylation in normal and cancer cell lines. Exp. Gerontol. 30,
human genome. Nature 489, 75–82 (2012). 475–484 (1995).
38. Zhou, W. et al. DNA methylation loss in late-replicating domains is 64. Satpathy, A. T. et al. Massively parallel single-cell chromatin
linked to mitotic cell division. Nat. Genet. 50, 591–602 (2018). landscapes of human immune cell development and intratumoral
39. Corces, M. R. et al. The chromatin accessibility landscape of T cell exhaustion. Nat. Biotechnol. 37, 925–936 (2019).
primary human cancers. Science 362, eaav1898 (2018). 65. Trevino, A. E. et al. Chromatin and gene-regulatory dynamics of
40. Zhang, K. et al. A single-cell atlas of chromatin accessibility in the the developing human cerebral cortex at single-cell resolution.
human genome. Cell 184, 5985–6001 e5919 (2021). Cell 184, 5053–5069 (2021).
41. Xiao, Y. et al. lntegrative single cell atlas revealed intratumoral 66. Llinares-Benadero, C. & Borrell, V. Deconstructing cortical folding:
heterogeneity generation from an adaptive epigenetic cell state genetic, cellular and mechanical determinants. Nat. Rev. Neurosci.
in human bladder urothelial carcinoma. Adv. Sci. (Weinh.) 20, 161–176 (2019).
https://doi.org/10.1002/advs.202308438 (2024). 67. Kriegstein, A. & Alvarez-Buylla, A. The glial nature of embryonic and
42. Corces, M. R. et al. Lineage-specific and single-cell chromatin adult neural stem cells. Annu. Rev. Neurosci. 32, 149–184 (2009).
accessibility charts human hematopoiesis and leukemia 68. Lange, M. et al. CellRank for directed single-cell fate mapping.
evolution. Nat. Genet. 48, 1193–1203 (2016). Nat. Methods 19, 159–170 (2022).
43. Banovich, N. E. et al. Impact of regulatory variation across human 69. Bertacchi, M. et al. NR2F1 regulates regional progenitor dynamics
iPSCs and differentiated cells. Genome Res. 28, 122–131 (2018). in the mouse neocortex and cortical gyrification in BBSOAS
44. Giles, J. R. et al. Human epigenetic and transcriptional T cell patients. EMBO J. 39, e104163 (2020).
differentiation atlas for identifying functional T cell-specific 70. Bosch, D. G. et al. NR2F1 mutations cause optic atrophy with
enhancers. Immunity 55, 557–574 (2022). intellectual disability. Am. J. Hum. Genet. 94, 303–309 (2014).
45. Wu, J. et al. Chromatin analysis in human early development reveals 71. Naka, H., Nakamura, S., Shimazaki, T. & Okano, H. Requirement for
epigenetic transition during ZGA. Nature 557, 256–260 (2018). COUP-TFI and II in the temporal specification of neural stem cells
46. Zhu, Q. et al. Developmental trajectory of prehematopoietic stem in CNS development. Nat. Neurosci. 11, 1014–1023 (2008).
cell formation from endothelium. Blood 136, 845–856 (2020). 72. Cadwell, C. R., Bhaduri, A., Mostajo-Radji, M. A., Keefe, M. G. &
47. Pritykin, Y. et al. A unified atlas of CD8 T cell dysfunctional states Nowakowski, T. J. Development and arealization of the cerebral
in cancer and infection. Mol. Cell 81, 2477–2493 (2021). cortex. Neuron 103, 980–1004 (2019).
48. Zhou, W. et al. DNA methylation dynamics and dysregulation 73. Hodge, R. D. et al. Conserved cell types with divergent features in
delineated by high-throughput profiling in the mouse. Cell human versus mouse cortex. Nature 573, 61–68 (2019).
Genom. 2, 100144 (2022). 74. Wang, Q. et al. Single-cell chromatin accessibility landscape
49. Fabian, P. et al. Lifelong single-cell profiling of cranial neural crest in kidney identifies additional cell-of-origin in heterogenous
diversification in zebrafish. Nat. Commun. 13, 13 (2022). papillary renal cell carcinoma. Nat. Commun. 13, 31 (2022).
50. McGarvey, A. C. et al. Single-cell-resolved dynamics of chromatin 75. Lake, B. B. et al. A single-nucleus RNA-sequencing pipeline to
architecture delineate cell and regulatory states in zebrafish decipher the molecular anatomy and pathophysiology of human
embryos. Cell Genom. 2, 100083 (2022). kidneys. Nat. Commun. 10, 2832 (2019).
51. Deshmukh, S., Ponnaluri, V. C., Dai, N., Pradhan, S. & Deobagkar, D. 76. Nikolic, A. et al. Copy-scAT: deconvoluting single-cell chromatin
Levels of DNA cytosine methylation in the Drosophila genome. accessibility of genetic subclones in cancer. Sci. Adv. 7,
PeerJ 6, e5119 (2018). eabg6045 (2021).
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02241-z
77. Maciejowski, J., Li, Y., Bosco, N., Campbell, P. J. & de Lange, T. 87. Patel, A. P. et al. Single-cell RNA-seq highlights intratumoral
Chromothripsis and kataegis induced by telomere crisis. Cell 163, heterogeneity in primary glioblastoma. Science 344, 1396–1401
1641–1654 (2015). (2014).
78. Shoshani, O. et al. Chromothripsis drives the evolution of gene 88. Johnson, K. C. et al. Single-cell multimodal glioma analyses
amplification in cancer. Nature 591, 137–141 (2021). identify epigenetic regulators of cellular plasticity and
79. Baca, S. C. et al. Punctuated evolution of prostate cancer environmental stress response. Nat. Genet. 53, 1456–1468 (2021).
genomes. Cell 153, 666–677 (2013).
80. Alexandrov, L. B. et al. Signatures of mutational processes in Publisher’s note Springer Nature remains neutral with regard to
human cancer. Nature 500, 415–421 (2013). jurisdictional claims in published maps and institutional affiliations.
81. Leibowitz, M. L., Zhang, C. Z. & Pellman, D. Chromothripsis: a new
mechanism for rapid karyotype evolution. Annu. Rev. Genet. 49, Open Access This article is licensed under a Creative Commons
183–211 (2015). Attribution 4.0 International License, which permits use, sharing,
82. ICGC/TCGA Pan-Cancer Analysis of Whole Genomes Consortium. adaptation, distribution and reproduction in any medium or format,
Pan-cancer analysis of whole genomes. Nature 578, 82–93 (2020). as long as you give appropriate credit to the original author(s) and the
83. Gerstung, M. et al. The evolutionary history of 2,658 cancers. source, provide a link to the Creative Commons licence, and indicate
Nature 578, 122–128 (2020). if changes were made. The images or other third party material in this
84. Snuderl, M. et al. Mosaic amplification of multiple receptor tyrosine article are included in the article’s Creative Commons licence, unless
kinase genes in glioblastoma. Cancer Cell 20, 810–817 (2011). indicated otherwise in a credit line to the material. If material is not
85. De Bacco, F. et al. Coexisting cancer stem cells with heterogeneous included in the article’s Creative Commons licence and your intended
gene amplifications, transcriptional profiles, and malignancy are use is not permitted by statutory regulation or exceeds the permitted
isolated from single glioblastomas. Cell Rep. 42, 112816 (2023). use, you will need to obtain permission directly from the copyright
86. Szerlip, N. J. et al. Intratumoral heterogeneity of receptor tyrosine holder. To view a copy of this licence, visit http://creativecommons.
kinases EGFR and PDGFRA amplification in glioblastoma defines org/licenses/by/4.0/.
subpopulations with distinct growth factor response. Proc. Natl
Acad. Sci. USA 109, 3041–3046 (2012). © The Author(s) 2024
Nature Biotechnology
