---
source_path: /mnt/c/Users/Administrator/Zotero/storage/8BEL8HEF/Tusi 等 - 2018 - Population snapshots predict early haematopoietic .pdf
ingested: 2026-04-23
sha256: ba253e52e709a032
---

ARTicLE
doi:10.1038/nature25741
Population snapshots predict early
haematopoietic and erythroid hierarchies
Betsabeh Khoramian Tusi1*, Samuel L. Wolock2*, caleb Weinreb2*, Yung hwang1, Daniel hidalgo1, Rapolas Zilionis2,
Ari Waisman3, Jun R. huh4, Allon m. Klein2 & merav Socolovsky1,5
The formation of red blood cells begins with the differentiation of multipotent haematopoietic progenitors.
Reconstructing the steps of this differentiation represents a general challenge in stem-cell biology. Here we used
single-cell transcriptomics, fate assays and a theory that allows the prediction of cell fates from population snapshots
to demonstrate that mouse haematopoietic progenitors differentiate through a continuous, hierarchical structure
into seven blood lineages. We uncovered coupling between the erythroid and the basophil or mast cell fates, a global
haematopoietic response to erythroid stress and novel growth factor receptors that regulate erythropoiesis. We defined
a flow cytometry sorting strategy to purify early stages of erythroid differentiation, completely isolating classically
defined burst-forming and colony-forming progenitors. We also found that the cell cycle is progressively remodelled
during erythroid development and during a sharp transcriptional switch that ends the colony-forming progenitor stage
and activates terminal differentiation. Our work showcases the utility of linking transcriptomic data to predictive fate
models, and provides insights into lineage development in vivo.
The abundance of erythroid progenitors in haematopoietic tissue pro- on the basis of their similarity to differentiated cell types16, which may
vides a unique opportunity to dissect how multipotent progenitors overlook progenitors that do not resemble mature cells. Fluorescence-
(MPPs) differentiate into a single lineage in situ, a process of fundamen- activated cell sorting (FACS) may also introduce bias into reconstructed
tal biological interest and of clinical relevance. Erythropoiesis has two developmental trajectories, through overly restrictive gates15 and the
principal phases: erythroid terminal differentiation (ETD), in which loss of sensitive cells28. It is still not clear how to reconcile cell fate
GATA1-driven transcription remodels erythroid precursors into red assays with the cell-state maps proposed from the results of single-cell
blood cells through several well-described stages1–3; and an earlier, less- profiling, and this remains a general challenge in stem-cell biology.
well-delineated phase of early erythropoiesis, in which haematopoietic Here we investigated the derivation and subsequent development
stem cells (HSCs) differentiate through poorly defined intermediates of erythroid progenitors by undertaking single-cell RNA sequencing
into erythroid progenitors. Erythroid progenitors have been identi- (scRNA-seq) of a broad set of haematopoietic progenitors, using the
fied by their colony-forming potential in semi-solid medium, as either inDrops platform29. We developed an analytical tool, population bal-
burst-forming (BFU-e) or colony-forming (CFU-e) progenitors4,5. ance analysis (PBA), which can be used to predict cell fate probabilities
A direct, complete and high-purity isolation of adult mouse BFU-e and from static snapshots of single-cell transcriptomes through dynamic
CFU-e from haematopoietic tissue has not, to our knowledge, been inference. PBA allowed us to define a FACS strategy to isolate cells in
attained6–9. More broadly, there are no known strategies that system- progressive stages of early erythropoiesis. Using single-cell fate assays,
atically identify the entire cellular and molecular trajectory of the early we then confirmed a number of detailed predictions regarding the early
erythroid lineage as it first arises from the HSC compartment and pro- haematopoietic hierarchy and erythroid developmental progression.
gresses to the point at which ETD is activated. The insights obtained into early erythropoietic fate control may be
Probing the earliest stages of erythropoiesis requires exploring how applicable to other differentiation models, and include novel erythro-
MPPs diversify into progenitors for each of the haematopoietic lineages. poietic regulators with potential therapeutic relevance.
Single-cell approaches have recently challenged established models of
haematopoiesis, showing that progenitor populations that were thought scRNA-seq of Kit+ progenitors
to be similar in their developmental stage and fate potentials are in fact We performed scRNA-seq on Kit+ haematopoietic progenitor cells
highly heterogeneous in both respects10–17. Alternative models replaced (HPCs) isolated using magnetic beads from the bone marrow of adult
the classic haematopoietic tree18–20 with a ‘flatter’ hierarchy, in which mice (Fig. 1a). Kit is expressed on all haematopoietic stem and early
unilineage progenitors derive directly from a heterogeneous set of progenitor cells30,31, enabling an inclusive approach that preserves the
lineage-biased multipotent progenitors. These new models are highly relative abundance of progenitor cell states. After filtering, we carried
dependent on the tools used in the analysis of high-dimensional cell forward 4,763 HPC transcriptomes for analysis (see ‘Data availability’
transcriptional states, which are currently undergoing intense innova- in Methods for interactive tools).
tion21–26. Descriptions of the haematopoietic hierarchy structure have We visualized the scRNA-seq data using the SPRING algorithm32
so far relied on clustering12, which may fail to capture continuums; dif- (Fig. 1b), which generates a graph of cells (graph nodes) connected to
fusion maps26,27, which are powerful for branching models but provide their nearest neighbours in gene expression space and projected into
less detail of highly complex processes; and the ordering of progenitors two dimensions using a force-directed graph layout. This visualization
1Department of Molecular, Cell and Cancer Biology, University of Massachusetts Medical School, Worcester, Massachusetts, USA. 2Department of Systems Biology, Harvard Medical School,
Boston, Massachusetts, USA. 3Institute for Molecular Medicine, University Medical Center of the Johannes Gutenberg-University Mainz, Mainz, Germany. 4Division of Immunology, Department of
Microbiology and Immunobiology and Evergrande Center for Immunological Diseases, Harvard Medical School and Brigham and Women’s Hospital, Boston, Massachusetts, USA. 5Department of
Pediatrics, Hematology/Oncology Division, University of Massachusetts Medical School, Worcester, Massachusetts, USA.
*These authors contributed equally to this work.
54 | NATURE | VOL 555 | 1 mARch 2018
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
a The probabilities obtained by PBA represent formal biophysical pre-
dictions for the fate of cells under simplified assumptions, but they
can also be treated heuristically as encoding graph distances. Applied
to our data, PBA defines seven putative commitment probabilities
for each haematopoietic progenitor (Fig. 1c, Extended Data Fig. 1e),
as well as the distance from the undifferentiated CD34highSca1high
b Ba Meg Ly c d MPPs (Fig. 1d).
D
The transcriptional continuum of HPCs is hierarchical
M
MPP We used PBA-predicted commitment probabilities to compute a cou-
pling score that reflects whether any two fate potentials occur concur-
Marker gene PBA-predicted PBA-predicted
expression fate probability differentiation rently in single progenitors at higher rates than would be expected by
ordering chance (Fig. 1e). A transcriptional-state hierarchy was formalized by
identifying correlated pairs of terminal fates and joining them itera-
E GN Ordering tively until a multipotent state was reached (Fig. 1e, f). The resulting
topology firmly supports the hierarchical view of haematopoiesis,
f with MPPs diverging into progenitors with either correlated eryth- roid, Ba/Mast and megakaryocytic fates, or with correlated lymphoid
and myeloid fates (Fig. 1f). However, the transcriptional-state hier-
archy emerges from correlations on a continuum, rather than from
discrete populations. Additionally, it predicts two refinements over
current models. First, the erythroid fate is correlated with the Ba/Mast
fates. Second, among myeloid progenitors we identified dendritic–
monocyte and granulocytic–monocyte coupling, but no dendritic–
granulocytic coupling, suggesting that monocyte differentiation
may occur through two distinct trajectories, a prediction that was
very recently independently confirmed34. The PBA-formalized HPC
hierarchy also allowed us to identify genes for which expression
closely correlates with each cell fate choice (Extended Data Fig. 2,
Supplementary Table 2).
Isolation of putative erythroid progenitors
To test PBA predictions (Fig. 1e–f), we developed a FACS strategy that
isolates haematopoietic subpopulations defined by scRNA-seq. Guided
by the single-cell expression patterns, we combined Kit expression with
CD55, a marker of megakaryocytic and erythroid bias10; Kit+CD55+
cells were divided into subpopulations (P1–P5), using CD49f
(encoded by Itga6) and megakaryocytic and erythroid markers6,9,10
(Fig. 2a). Using reverse transcription with quantitative PCR (qRT–
suggested that HPCs occupy a continuum of transcriptional states, PCR) (Extended Data Fig. 3a), and scRNA-seq (11,241 cells post-
rather than discrete metastable states, a result that contrasts with filter) (Fig. 2b, Extended Data Fig. 3b–e), we mapped cells from each
single-cell data from mature blood lineages and is supported by formal of the sorted subpopulations back to regions of the SPRING graph.
tests of graph interconnectivity (Extended Data Fig. 1a). When SPRING We found that P1 and P2 represent high-purity subpopulations on
plots were coloured on the basis of the expression of lineage-specific the putative erythroid branch, with P1 predicted to be committed,
markers (Fig. 1b, Supplementary Table 1), the cells were found to and P2 mostly committed, to the erythroid fate (Fig. 1c). P3 and P4
organize around an undifferentiated core, from which seven distinct are enriched for the Ba/Mast and megakaryocytic branches, respec-
branches emerge, corresponding to progenitors of the basophil or mast tively; P3 bifurcates into separate basophil and mast cell branches. P5
cell (Ba/Mast), granulocytic neutrophil, monocytic, dendritic, lym- contains erythroid-biased oligopotent and multipotent cells. Myeloid,
phoid, megakaryocytic and erythroid lineages. Although this structure lymphoid and some MPP states are within the CD55− region of
depends critically on collecting cells using a broad selection marker, the plot.
SPRING visualization of data from previous studies12,15 revealed the
same lineage relationships (Extended Data Fig. 1b). Functional identification of correlated cell fates
We next examined the differentiation potential of the sorted P1–P5
PBA of the HPC continuum populations, and by extension, the predicted fate probabilities for their
To understand the differentiation trajectories that cells might follow, corresponding transcriptional states. Colony-forming assays showed
we developed the PBA33 approach for studying single-cell continua that P1 and P2 contain all of the unipotential erythroid progenitors
(Extended Data Fig. 1c, d). PBA maps each cell to a low-dimensional and no other progenitors (Fig. 2c–e). P1 colonies were small and uni-
space that encodes the cell-graph topology in the form of predicted focal, maturing on day 3 or later (CFU-e) (Fig. 2c), whereas P2 colonies
cell fate probabilities. The derivation and limitations of PBA have were largely multifocal, maturing on day 4 or later (BFU-e) (Fig. 2d).
been detailed elsewhere33. The core of PBA can be understood as the Thus, P1 is closer to erythroid maturation than P2, consistent with
reconstruction of the memoryless stochastic dynamics of cells, which, PBA predictions (Figs 1c, 2b). Furthermore, the transcriptional
through ongoing cell turnover, explains the observed steady-state state of progenitors as defined by the SPRING map determines their
distribution of cell states. PBA approximates the dynamics of cells ability to form either multifocal or unifocal colonies. Consistent with
as following the gradient of a potential landscape, which itself can the SPRING plot, the less-differentiated P5 population gave rise to
be inferred through an asymptotic relationship between diffusion– mixed myeloid colonies, and P4 was enriched for megakaryocytic
drift processes and the spectral properties of the SPRING graph33. progenitors (Fig. 2e, Extended Data Fig. 4a).
1 mARch 2018 | VOL 555 | NATURE | 55
*
10 GN
EBaMeg LyDM
MGN
E Ba Meg LyD M EBa
L
M
y
eg
M DM DMGN
D Ly Ly MPP
5 Ly Meg
Meg
0 Ba
E BaMegLyD MGN EBaMegLy D M GN
erocs-z
gnilpuoC
inDrops
Kit+ haematopoietic
progenitors from
mouse bone marrow
scRNA-seq 4,763 cells
e
E BaMegLyD MGNE BaMegLyD MGN
Figure 1 | The early haematopoietic hierarchy predicted by scRNA-
seq. a, Schematic for scRNA-seq of Kit+ mouse bone marrow. b, SPRING
plot of single-cell transcriptomes. Each point is one cell. Colours
indicate lineage-specific gene expression. Ba, basophilic or mast cell;
D, dendritic; E, erythroid; GN, granulocytic neutrophil; Ly, lymphocytic;
M, monocytic; Meg, megakaryocytic; MPP, multipotential progenitors.
c, d, Parameterization of the cell-state graph using PBA, encoding the
graph position of each cell by a set of predicted fate probabilities (c)
(colours as in b), and pseudo-temporal ordering with MPPs at the origin,
terminating with the most mature cells observed for each lineage (d).
e, f, A cell-state hierarchy encodes the cell-graph topology. e, Lineage-
biased states were identified by comparing the fraction of cells with
PBA-predicted bilineage coupling with expected values from fate
randomization. f, Iteratively joining fates on the basis of pairwise coupling
revealed the cell-state hierarchy.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
CD105
The erythroid differentiation trajectory
Integrating the cell fate assays and scRNA-seq analysis, we partitioned
the continuum of cell states between MPPs and ETD into three stages
To test HPC fate potential further, we sorted single Kit+ cells into (Fig. 4a): (1) erythroid–basophil–megakaryocyte-biased progenitors
liquid culture wells in the presence of cytokines that support myeloid (EBMPs), (2) early erythroid progenitors (EEPs) and (3) committed
and erythroid differentiation (Fig. 3a). We assayed the clonal output of erythroid progenitors (CEPs). EBMPs are oligopotent cells near the
1,158 single cells by FACS (Fig. 3b, Extended Data Fig. 4b). Unipotential branch points of the megakaryocytic and basophil lineages, which are
clones for the erythroid, Ba/Mast, megakaryocytic, and granulocytic biased away from the GN/M fates and strongly represented in the P5
neutrophil and monocytic (GN/M) lineages largely originated in the and P2 subpopulations (Fig. 2b). EEPs occupy a narrow region of the
P1/P2, P3, P4 and CD55− subpopulations, respectively, consistent with graph, just past the final non-erythroid fate branch point; they form
predictions (Figs 1c, 2b, 3b). Many clones contained multiple lineages, most of the P2 subpopulation and are functionally BFU-e (Fig. 2b–d).
with strong, statistically significant couplings between the erythroid, CEPs constitute the majority of unipotential erythroid progenitors, form
Ba/Mast and megakaryocytic cell fates on the one hand, and the GN/M most of the P1 subpopulation, and are functionally CFU-e (Fig. 2b–d).
fates on the other (Fig. 3c; absolute z-score value of more than 10 when To establish the transcriptional events of the erythroid trajectory,
compared to randomized data), consistent with both known (erythroid we created a smoothed time series for every gene from MPP to ETD,
and megakaryocytic, GN/M) and novel (erythroid and Ba/Mast) PBA akin to published pseudotemporal-ordering algorithms35–37 (Fig. 4b).
predictions (Fig. 1c, e, f). Progenitors with erythroid and Ba/Mast out- Known erythroid regulators recapitulated the expected expression
put were enriched in the P2 and P5 subpopulations (Fig. 3d), which dynamics (Fig. 4c). Gata1 and the erythropoietin (EPO) receptor,
map close to the erythroid and Ba/Mast branch point in the scRNA-seq Epor, were induced early, concurrent with suppression of Spi1 (which
data (Figs 1c, 2b), and were depleted in the CD55− population, as pre- encodes PU.1) and Gata2 (ref. 38). The transition to ETD was marked
dicted. We found similar results in bulk liquid cultures (Extended Data by a sharp induction of erythroid genes such as α-globin (Hba-a1). We
Fig. 4c). Notably, the new Ba/Mast differentiation pathway suggested by validated the expression of canonical transcription factors in sorted
our data does not rule out Ba/Mast formation by the traditional route, P1–P5 subpopulations, including the early expression of Gata1
as some clones gave rise to both granulocytic neutrophil and Ba/Mast (Extended Data Fig. 5a, b). We further established that a graded increase
lineages. These results suggest that erythroid, Ba/Mast and megakaryo- in Tfrc (which encodes CD71) is a reliable marker of continuous pro-
cytic fates are coupled transcriptionally and functionally, while being gression through the EEP and CEP stages; transcriptomes of sorted
anti-coupled to the GN/M fates, and that scRNA-seq data can be used CD71high P1 cells map to late CEP stage and CD71 gradually increases in
to generate successful predictions of HPC states and fates. sorted P2 and P1 cells differentiating in vitro (Extended Data Fig. 5c, d).
56 | NATURE | VOL 555 | 1 mARch 2018
f94DC
CD150
14DC
17DC
a b
103 P4
Kit+CD55+ 102 n = P 3 1 ,104 n = P 2 2 ,435
103 0
P3 P5
102
0 1 1 0 0 3 2 P1 P3 P4
n = 2,032 n = 1,210 101
0101 102 103 10 0 0 ≥5 P2
0101 102 103 0.5
P5 n = 2,460
0
e
CFU-e
day 3 CFU-MK
0
CFU-GM CFU-e
day 7
P1P2P3P4
C
P5 D55– CFU-GEMM
d P1P2P3P4P
C
5 D55–
Late BFU-e f day 4 P5
BFU-e – + –
– + ++ CFU-e
Erythroid committed – + +
P1P2P3P4
C
P5 D55– in colony assays
)%( sllec
deppaM
MPP
E
Ba Meg
c
50 μm
50 μm
100 μm
50 μm
sllec
000,01
rep
seinoloC
sllec
000,01
rep
seinoloC
sllec
000,01
rep
seinoloC
a Kit+ bone marrow cells b
FACS
CD55– P1 P2 P3 P4 P5
Sort single cells into wells
Culture for 3–10 days
Analytical FACS
E(TER119) Meg(CD41) M(MAC-1)
Ba(FCER1A) GN(GR-1) E Ba MegM GN
250
3,300
c d
0 1,800 2,000 E
Ba
0 0 20 Meg
GN
0 BaMegGN M
Co-occurrence, z-score 250
P2 P1
0 300 Early BFU-e
day 7
0
Figure 2 | A novel sorting scheme isolates erythroid progenitors.
a, Kit+CD55+ bone marrow cells were sorted into gates P1–P5, and
profiled using scRNA-seq. b, P1–P5 single-cell transcriptomes localized
to their most similar counterparts on the SPRING graph. c–e, Colony
formation by unifocal-erythroid (c), multifocal-erythroid (d) and non-
erythroid (e) P1–P5 and Kit+CD55− cells. Bars represent the mean of two
independent experiments (individual circles), each performed in triplicate.
Images show representative erythroid colonies, stained for haemoglobin
with diaminobenzidine. Colonies: CFU-MK, megakaryocytic (Extended
Data Fig. 4a); CFU-GM, granulocytic/monocytic; CFU-GEMM, mixed
myeloid. f, Summary of erythroid colony potential of FACS subsets.
)851,1
=
n(
senolc
llec-elgniS
CD55–
64
P5 16
4 P4
P3 0
P2
P1
senolc
fo egatnecreP
15
10
5
)sllec
fo rebmun(gol
2
Fate output Clone size
e
E BaMeg GNM
(Lymphoid and dendritic
not measured)
–40 0 40
)%(
serutluc
llec-elgniS
35 Replicate
30 Mean
25 20
15
10
5
0 P1P2P3P4P5 D55–
C
Figure 3 | Predicted fate couplings confirmed by single-cell fate assays. a, Schematic of single-cell liquid cultures, measuring clonal output with the
indicated antibodies. b, Lineage output (left) and size (cell number, right)
of each clone (rows). c, Concurrently occurring fates in single-cell culture,
computed by comparing the number of clones from b that produce a pair
of fates to the number expected following randomization. d, Fraction of
bipotent erythroid–Ba/Mast clones in P1–P5, containing erythroid and
either basophil or mast cells, but no other fates. Individual points and
error bars show the expected value and s.e.m. from independent single-
cell sorting experiments. Bars represent the mean of two (P1, P2, P3) or
three (P5) independent experiments; a single experiment was performed
for P4 and CD55−. e, A cell-state hierarchy that is based on the concurrent
occurrence of fates in single-cell cultures.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
200
150
100
50
Excluded cells
(low abundance
in stress condition)
A further, sharp induction of Tfrc takes place at the transition to ETD Erythroid stress generates a broad response
(Fig. 4c). Using scRNA-seq, we examined two model systems of accelerated,
Of the approximately 4,500 genes that varied significantly along or stress, erythropoiesis: the mid-gestation fetal liver (n = 7,182 cells
the erythroid trajectory (Supplementary Table 3), a large group was post-filter), in which erythropoiesis is a rate-limiting factor of fetal
induced at the onset of the CEP stage, and sharply suppressed at the growth; and bone marrow from mice treated with EPO for 48 h, stimu-
CEP to ETD transition (Fig. 4b). It contained the most dominant lating red blood cell production (n = 2,611 cells post-filter). SPRING
dynamic gene clusters and was enriched for cell cycle and growth- graphs revealed a remarkable conservation of the key features of the
related genes, including those involved in mTOR signalling, nucleotide haematopoietic hierarchy and erythroid differentiation during stress
metabolism and DNA replication (Extended Data Figs 5e, 6a, b, (Fig. 4d). The proportion of erythroid-trajectory cells increased with
Supplementary Table 4). These pathways suggest that CEPs, which are stress (Fig. 4d, e). In the fetal liver, the increase was predominantly
the most abundant cells in early erythropoiesis, act as an ‘amplification’ in CEPs, whereas in EPO-stimulated bone marrow, all erythroid-tra-
module. Our analysis predicts new epigenetic and transcriptional jectory cells increased in abundance, including uncommitted MPPs
regulators of the erythroid lineage (Extended Data Fig. 6, Supplementary and EBMPs. We found that the absolute number of Kit+ cells in EPO-
Table 4), and shows that although GATA1 is expressed early in the stimulated bone marrow did not change, indicating that the increase
erythroid trajectory, most of its canonical targets are induced only at in erythroid-trajectory cells came at the expense of other cell lineages
the transition to ETD. Taken together, the temporal ordering of the (Fig. 4e, Extended Data Fig. 7). A number of mechanisms could account
single-cell transcriptomes recapitulates known events of early eryth- for this, including altered intrinsic fate bias of MPPs39,40.
ropoiesis and uncovers a dedicated CEP transcriptional program that EPO addition altered gene expression principally in EEPs and
is distinct from the ETD program. CEPs, but also in EBMPs and MPPs (Fig. 4f), in which targets of
1 mARch 2018 | VOL 555 | NATURE | 57
No.
DE
genes
EPO-stimulated
bone marrow
DTE
4
3
2
1
0
MPP/ EEP CEP
EBMP
+EPO CEP EEP MPP
EBMP
Basal
lanoitcarf
ni
egnahc
dloF
MBb
sv
ecnadnuba
llec
600
400
200
Ba
d Ly Meg M Meg Ly eBM
MPP FL
MPP
M Ba
EPO-stimulated
bone marrow Fetal liver
2,611 cells 7,182 cells
GN E GN E
f
)MPT(
noisserpxE
Low Kit
Spi1
Transcription factors Gata2
Ldb1
Gata1 Tal1
Zfpm1
Klf1
×105
600 Surface receptors 3 Cd34 + haemoglobin Kit
400 2 Itga2b
Epor
200 1 Tfr2
Tfrc
0 0 Hba-a1 0 20 40 60 80 100
MPP-to-erythroid cell order (%)
DTE
{
a
EBMP EEP
CEP MPP
0%
MPP to
erythroid
cell order
100%
4
3
2
1
0
marg
rep
rebmun
lleC
e Committed: Meg
Ba Ly
M
GN E
Uncommitted: Erythroid-biased
Not erythroid-
–EPO+EPO biased
g
Erythroid
fate
probability
1.0
0.8
0.6
0.4
0.2
MPP
100
10
1
×104
etar
ffo/no
eneG
rep
seneg
fo
.on(
)gniredro
llec
%
b
MPP-to-erythroid cell order (%)
seneG
Expression
(z-score)
1 c
0
–1
EB MP EEP CEP ETD
0 3 15 28 86 100
MPP
EBMP
GN/M/D/Ly
EEP
CEP
eBM/ ETD
fetal liver
Figure 4 | Stages of early erythropoiesis and the global erythroid bone marrow (eBM) and fetal liver samples. Cells coloured as in Fig. 1b.
stress response. a, Stages of the erythroid trajectory between MPPs and e, Left, erythroid lineage expansion at the expense of non-erythroid cells
ETD. EBMPs, erythroid–basophil–megakaryocyte-biased progenitors. (see Extended Data Fig. 7). Among uncommitted cells, erythroid-biased
The SPRING plot shows PBA-predicted erythroid fate probability. progenitors increased, whereas the remainder diminished. Committed
b, Top, dynamically varying genes (rows), ordered by peak expression, cells were defined by a PBA-predicted erythroid fate probability greater
in cells (columns) ordered from MPP to ETD. Gene expression data than 0.5. Right, change in abundance of each progenitor stage relative to
were smoothed using a Gaussian kernel. Bottom, the number of genes basal bone marrow. Error bars are the sampling s.e.m. (one sample per
turning on or off (density of expression inflection points) throughout condition). f, EPO-stimulated differential gene expression. Cells from
the progression from MPP to ETD. The x axis represents PBA-predicted EPO-stimulated bone marrow were first mapped onto the basal bone
differentiation ordering of cell transcriptomes, uniformly spaced from marrow SPRING plot, and then differentially expressed (DE) genes were
the least (0%) to the most (100%) differentiated. c, Gene expression traces analysed. g, Summary of the stress erythropoiesis response.
for established erythroid genes. d, SPRING plots of EPO-stimulated
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
a b colony formation in both the fetal liver and bone marrow samples. By
Mst1r Ryk Il17ra contrast, IL-17A mediated a marked potentiation of adult bone marrow
CFU-e colony formation, quadrupling colonies at low levels of EPO Test
ligands (50 mU ml−1), and increasing them by approximately 50% at high levels of EPO (500 mU ml−1).
The stimulatory effect of IL-17A required endogenous IL-17RA
(Fig. 5c) and was also evident in human bone marrow (Fig. 5d).
Furthermore, IL-17A stimulation was saturable, with a low half-
maximum effective concentration (EC ) (60 pM), consistent with e 50
high-affinity binding of IL-17A to IL-17RA. IL-17A induced rapid
100 phosphorylation of the intracellular signalling mediators STAT3 and
50 54% 50% EPO STAT5 in CEPs and EEPs (Fig. 5e), and western blotting of freshly
0
100 sorted CEP P1 and EEP P2 cells revealed expression of IL-17RA
61% 43%
50 (Extended Data Fig. 9d). Taken together, our findings suggest previ- IL-17A
10 0 0 ously unknown regulation of EEPs and CEPs through the expression 74% 72%EPO + 50 of a number of growth factor receptors. IL-17A
0 100
50 Overlay Cell cycle remodelling during erythroid development
0 In a final analysis, we asked what governs progression through the
CEP stage and its termination during ETD. We previously reported
that the onset of ETD in the fetal liver occurs within a single S phase,
and is dependent on S-phase progression47; furthermore, this unique
S phase is shorter and faster than the S phase in pre-ETD cells48,49.
These conclusions, which are based on the analysis of large fetal liver
subpopulations, predict that CEP exit should show an S phase signature.
In our scRNA-seq data, we found that the expression levels of genes that
mark the G1/S, S, G2 and G2/M cell cycle phases form a sequence of
close, sharp peaks during CEP exit, probably representing a single cell
cycle (Fig. 6a, b). This and the following results hold even when cell
cycle genes are omitted for ordering the erythroid trajectory (Extended
Data Fig. 10a–c). Notably, by reversibly inhibiting DNA replication,
we found that the CEP-to-ETD transition in adult bone marrow not
only synchronized with, but also depended on, S phase progression
(Extended Data Fig. 10d–f).
The scRNA-seq data revealed that changes to cell cycle machinery
occur throughout the CEP stage, perhaps in preparation for the
switch to ETD. Genes with expression levels that most closely cor-
relate with CEP progression (Supplementary Table 6) are enriched
for Gene Ontology terms associated with DNA replication. Notably,
CCAAT-enhancer-binding protein β (C/EBPβ), a transcription regulators of S phase and the G1/S-phase transition increase stead-
factor that biases differentiation away from erythroid and megakaryo- ily through the CEP stage, including cyclin E1 (encoded by Ccne1),
cytic fates41, were downregulated. We identified both known42,43 and cyclin A2 (Ccna2) and MCM helicase subunits (Mcm2–Mcm7).
new stress-responsive genes, together with their precise localization Conversely, regulators of the G1 phase such as cyclin D2 (Ccnd2)
within the erythroid trajectory (Extended Data Fig. 8, Supplementary and cyclin-dependent kinase 6 (Cdk6) decrease steadily (Fig. 6c).
Table 5). To investigate these findings, we labelled S-phase cells in vivo with
Taken together, we found that the cell-state branching structure is the nucleotide analogue BrdU, and analysed the cell cycle distri-
maintained during accelerated erythropoiesis. In MPPs and through- bution of cells as they progressed through the EEP and CEP stages
out the ensuing erythroid progression, we identified changes in gene (Fig. 6d–f). We found a graded but notable increase in the fraction
expression and in cell abundance in response to EPO well beyond of cells in S phase, whereas the number of G1 cells correspondingly
the currently known mechanism of EPO-driven erythropoietic decreased. Results were similar in both EPO-stimulated bone mar-
expansion42,44. row and fetal liver samples (Extended Data Fig. 10g). There was
no significant change in the length or speed of S phases, as evi-
Growth factor regulators of early erythropoiesis denced by stable intra-S-phase levels of BrdU48 (Fig. 6f), suggesting
We screened EEPs and CEPs for gene expression of cell-surface recep- that cells spend more time in S phase as a result of G1 shortening.
tors with known ligands using qRT–PCR, identifying three such Western blotting of sorted P1 and P2 fractions confirmed that the
receptors encoded by Ryk, Mst1r and Il17ra (Fig. 5a, Extended Data expression of key S-phase regulators increased with developmen-
Fig. 9a, b). RYK and MST1R have previously been reported in CFU-e, tal progression in EEPs and CEPs (Extended Data Fig. 10h). Taken
but their function remains unknown45,46. However, the expression of an together, our data suggest that progression through the erythroid
IL-17A receptor by EEPs has not, to our knowledge, been documented. trajectory is associated with extensive remodelling of the cell cycle
We stimulated RYK, MST1R and IL-17RA with their respective (Fig. 6g).
ligands, WNT5A, macrophage-stimulating protein (MSP) and IL-17A,
using erythroid colony formation as a readout (Fig. 5b, Extended Data Discussion
Fig. 9c). In the fetal liver sample, in the presence of low levels of EPO Our scRNA-seq analysis reveals that HPCs occupy a continuum of
(50 mU ml−1), MSP doubled the number of CFU-e colonies, equiva- transcriptional cell states, branching towards seven fates. Certain
lent to a tenfold increase in EPO concentration. MSP was inhibitory cell fate potentials are correlated, supporting a hierarchical view of
in other contexts, and WNT5A was a potent inhibitor of erythroid haematopoiesis, with MPPs diverging either towards myeloid and
58 | NATURE | VOL 555 | 1 mARch 2018
)%(
ytisned
lleC
c
f
BM
FL Erythroid output BM
Ligands Receptors
seinoloc
e-UFC
Wild type
Il17ra–/–
3,500
3,000
2,500
2,000
0 5 10 15 20 500
400
300
200 0 5 10 15 20
IL-17A (ng ml–1)
seinoloc
e-UFC
100 250 150
0 0 0
TPM TPM TPM MSP
50
P2 P1-CD71low
MSP MST1R
d WNT5A RYK IL17A IL17RA
102103 104102103 104
pSTAT3 pSTAT5
(FU) (FU)
egnahc
dlof
e-UFC
EPO U ml–1
0.05 4 BM 0.5
0.05 3 FL 0.5
2
1
0 ND
WNT5A IL-17A
100 10 ng ml–1
Figure 5 | Novel growth factor regulators of early erythropoiesis.
a, Expression patterns for Mst1r, Ryk and Il17ra (see Extended Data
Fig. 9a, b). TPM, transcripts per million. b, Effect of MSP, WNT5A or
IL-17A on EPO-dependent CFU-e colony formation. Bars represent the
mean of two or three independent experiments (individual data points),
each performed in quadruplicate (for full analysis see Extended Data
Fig. 9c). c, The IL-17A response is lost in Il17ra−/− bone marrow. Data
are mean ± s.d. per 500,000 bone marrow cells plated in triplicate in the
presence of EPO (0.05 U ml−1) and are representative of two independent
experiments. d, IL-17A stimulates CFU-e formation in freshly isolated
human bone marrow mononuclear cells. Data are mean ± s.d. per 85,000
cells plated in triplicate. e, IL-17A-mediated phosphorylation of STAT3
and STAT5 (pSTAT3 and pSTAT5). Fresh bone marrow cells were starved
of cytokines for 3 h, and then stimulated with EPO, IL-17A or both;
FACS profiles are for baseline (starved, shown in grey), and 60 min after
stimulation (in colour). Profiles are representative of two independent
experiments, each performed in duplicate. FU, fluorescence units.
f, Summary of growth factor effects on erythroid output.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
a We delineated the continuous differentiation trajectory of the eryth-
roid lineage, from its origins in MPPs, through EBMPs, to unipotential
EEPs and CEPs, which we show correspond to the unipotential BFU-e
and CFU-e, respectively. The dominant CEP stage expresses a dis-
tinct transcriptional program and is probably a regulator of erythroid
output, as evidenced by both its expansion under stress, and by novel
growth factor receptors that regulate CFU-e numbers. In particular,
our finding of strong stimulation by the pro-inflammatory IL-17RA
f contributes to the growing evidence of a complex interplay between
erythropoiesis and inflammation50,51. We further identified the cell
cycle as a key process in both the progression and termination of the CEP stage. Developing CEPs spend an increasing fraction of their time
in S phase, as a result of G1 shortening; their transition to ETD in an
abrupt transcriptional switch is dependent on a single, short S phase. We speculate that the cell cycle may set the context for activation of
transcription factors that are induced earlier in the erythroid trajectory.
Taken together, our single-cell approach allowed us to make detailed
c predictions that we validated to reveal novel fundamentals of early hae-
Ccna2 Ccne1 E2f4 matopoietic differentiation, as well as practical methods for further
250 150 150 isolation and study of these cells.
0 0 0 Mcm2 Mcm3 Orc6
Online Content Methods, along with any additional Extended Data display items and 250 150 25
0 0 0 Source Data, are available in the online version of the paper; references unique to
Rrm1 Ccnd2150 0 these sections appear only in the online paper.
250 0
received 17 October 2016; accepted 11 January 2018.
Published online 21 February 2018.
1. Fujiwara, Y., Browne, C. P., Cunniff, K., Goff, S. C. & Orkin, S. H. Arrested
development of embryonic red cell precursors in mouse embryos lacking
transcription factor GATA-1. Proc. Natl Acad. Sci. USA 93, 12355–12358
(1996).
2. Liu, Y. et al. Suppression of Fas–FasL coexpression by erythropoietin mediates
erythroblast expansion during the erythropoietic stress response in vivo. Blood
108, 123–133 (2006).
3. Chen, K. et al. Resolving the distinct stages in erythroid differentiation based on
dynamic changes in membrane protein expression during erythropoiesis.
Proc. Natl Acad. Sci. USA 106, 17413–17418 (2009).
4. Hara, H. & Ogawa, M. Erythropoietic precursors in mice under erythropoietic
stimulation and suppression. Exp. Hematol. 5, 141–148 (1977).
5. Gregory, C. J., McCulloch, E. A. & Till, J. E. The cellular basis for the defect in
haemopoiesis in flexed-tailed mice. III. Restriction of the defect to
erythropoietic progenitors capable of transient colony formation in vivo.
Br. J. Haematol. 30, 401–410 (1975).
6. Pronk, C. J. et al. Elucidation of the phenotypic, functional, and molecular
topography of a myeloerythroid progenitor cell hierarchy. Cell Stem Cell 1,
428–442 (2007).
7. Flygare, J., Rayon Estrada, V., Shin, C., Gupta, S. & Lodish, H. F. HIF1α
synergizes with glucocorticoids to promote BFU-E progenitor self-renewal.
Blood 117, 3435–3444 (2011).
8. Li, J. et al. Isolation and transcriptome analyses of human erythroid
progenitors: BFU-E and CFU-E. Blood 124, 3636–3645 (2014).
9. Mori, Y., Chen, J. Y., Pluvinage, J. V., Seita, J. & Weissman, I. L. Prospective
isolation of human erythroid lineage-committed progenitors. Proc. Natl Acad.
Sci. USA 112, 9638–9643 (2015).
10. Guo, G. et al. Mapping cellular hierarchy by single-cell analysis of the cell
surface repertoire. Cell Stem Cell 13, 492–505 (2013).
11. Sun, J. et al. Clonal dynamics of native haematopoiesis. Nature 514, 322–327
(2014).
12. Paul, F. et al. Transcriptional heterogeneity and lineage commitment in myeloid
progenitors. Cell 163, 1663–1677 (2015).
lymphoid fates, or towards the erythroid, megakaryocyte and Ba/Mast 13. Busch, K. et al. Fundamental properties of unperturbed haematopoiesis from
cell fates. Yet unlike the classical models of haematopoiesis, HPCs do stem cells in vivo. Nature 518, 542–546 (2015).
14. Notta, F. et al. Distinct routes of lineage development reshape the human blood
not separate into discrete and homogenous stages. The coupling of
hierarchy across ontogeny. Science 351, aab2116 (2016).
specific cell fates, which we validated with single-cell fate assays, is 15. Nestorowa, S. et al. A single-cell resolution map of mouse hematopoietic stem
a critical feature by which our model differs from recent models of and progenitor cell differentiation. Blood 128, e20–e31 (2016).
16. Velten, L. et al. Human haematopoietic stem cell lineage commitment is a
haematopoiesis, in which unilineage progenitors arise directly from
continuous process. Nat. Cell Biol. 19, 271–281 (2017).
MPPs. Our model also explains historical hierarchical interpreta- 17. Mercier, F. E. & Scadden, D. T. Not all created equal: lineage hard-wiring in the
tions of haematopoiesis, which were based on fate assays of FACS- production of blood. Cell 163, 1568–1570 (2015).
18. Kondo, M., Weissman, I. L. & Akashi, K. Identification of clonogenic common
gated populations, averaging the fate couplings of their constituent
lymphoid progenitors in mouse bone marrow. Cell 91, 661–672 (1997).
progenitors. Of note, the continuous nature of the scRNA-seq data 19. Akashi, K., Traver, D., Miyamoto, T. & Weissman, I. L. A clonogenic common
does not rule out the existence of discrete epigenetic or signalling myeloid progenitor that gives rise to all myeloid lineages. Nature 404,
states among HPCs, if their lifetime in single cells is comparable to, or 193–197 (2000).
20. Adolfsson, J. et al. Identification of Flt3+ lympho-myeloid stem cells lacking
shorter than, the lifetime of mRNA molecules (in the range of hours erythro-megakaryocytic potential a revised road map for adult blood lineage
to approximately 1 day). commitment. Cell 121, 295–306 (2005).
1 mARch 2018 | VOL 555 | NATURE | 59
)MPT(
noisserpxE
104
103
102
102 103 104
375 0
Cdk6
0 28 100
MPP-to-erythroid cell order (%)
d
)UF(
UdrB
e P2 P1
ETD
CD71 (FU)
800
0
Expression
(TPM)
2
1
0 0 3 15 28 86 100
MPP-to-erythroid cell order (%)
erocs
esahp
elcyc
lleC
b G1/S Tfrc/CD71 S Klf1 G2
G2/M M/G1
Expression
(z-score):
2
–2
S/1G
S
2G
M/2G
1G/M
*
10 30 50 70 90
g
EEP CEP ETD
G1 S G1 S G1S
G1 shortening Faster S
)%(
slleC
P2 P1
ETD
S G1 100 G2/M
80
60
40
20
0
Developmental progression
(consecutive CD71 gates)
)UF( 17DC
6
4 2
0
deeps
esahp-S
)UF
,UdrB
esahp-S-artni(
×103
S
G1 G2/M
24×103 DNA content
18
12
6
0 0 5 10 15
BrdU
BrdU pulse Collect Analytical FACS
30 min bone marrow
Kit+CD55+
CD49Flow
CD105+
051DC
P2
BrdU
DNA
P1
CD71
Figure 6 | Extensive remodelling of the cell cycle during erythroid
development. a, Cell cycle phase-specific genes52, ordered by peak
expression, reveal cell cycle synchronization with the CEP to ETD
transition (indicated by an asterisk). b, Mean expression of all genes
specific to each cell cycle phase (as in a), traced along the erythroid
trajectory. The transition to ETD is marked by a sharp induction of Tfrc.
c, Representative cell cycle genes that are correlated or anti-correlated
with progression along the erythroid trajectory. d, Schematic for cell cycle
analysis of erythroid progenitors in vivo. Bone marrow was collected and
fixed 30 min after BrdU injection; P1 and P2 cells were analysed for BrdU
incorporation and DNA content. e, BrdU-labelled S-phase cells, as in d.
Cell colouring represents consecutive 7-percentile gates of increasing
CD71, reflecting progression through the EEP (P2) and CEP (P1) stages
(Extended Data Fig. 5c, d). The transition to ETD (red arrow) is marked
by a sharp increase in CD71, and synchronization in the S phase (BrdU+).
f, CD71 expression (top), cell cycle phase distribution (middle), and
intra-S-phase DNA synthesis rate (bottom), for all gates in e. Insets show
representative FACS plots of cell cycle distribution. Data are representative
of three independent experiments. For similar analyses of EPO-stimulated
bone marrow and fetal liver samples, see Extended Data Fig. 10g.
g, Summary of cell cycle remodelling during early erythropoiesis and the
S-phase-dependent switch to ETD.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
21. Huang, W., Cao, X., Biase, F. H., Yu, P. & Zhong, S. Time-variant clustering 43. Agosti, V., Karur, V., Sathyanarayana, P., Besmer, P. & Wojchowski, D. M. A KIT
model for understanding cell fate decisions. Proc. Natl Acad. Sci. USA 111, juxtamembrane PY567-directed pathway provides nonredundant signals for
E4797–E4806 (2014). erythroid progenitor cell development and stress erythropoiesis. Exp. Hematol.
22. Marco, E. et al. Bifurcation analysis of single-cell gene expression data reveals 37, 159–171 (2009).
epigenetic landscape. Proc. Natl Acad. Sci. USA 111, E5643–E5650 (2014). 44. Koury, M. J. & Bondurant, M. C. Erythropoietin retards DNA breakdown and
23. Shin, J. et al. Single-cell RNA-seq with waterfall reveals molecular cascades prevents programmed death in erythroid progenitor cells. Science 248,
underlying adult neurogenesis. Cell Stem Cell 17, 360–372 (2015). 378–381 (1990).
24. Ji, Z. & Ji, H. TSCAN: pseudo-time reconstruction and evaluation in single-cell 45. Yee, K., Bishop, T. R., Mather, C. & Zon, L. I. Isolation of a novel receptor tyrosine
RNA-seq analysis. Nucleic Acids Res. 44, e117 (2016). kinase cDNA expressed by developing erythroid progenitors. Blood 82,
25. Welch, J. D., Hartemink, A. J. & Prins, J. F. SLICER: inferring branched, nonlinear 1335–1343 (1993).
cellular trajectories from single cell RNA-seq data. Genome Biol. 17, 106 46. van den Akker, E. et al. Tyrosine kinase receptor RON functions downstream of
(2016). the erythropoietin receptor to induce expansion of erythroid progenitors. Blood
26. Haghverdi, L., Buttner, M., Wolf, F. A., Buettner, F. & Theis, F. J. Diffusion 103, 4457–4465 (2004).
pseudotime robustly reconstructs lineage branching. Nat. Methods 13, 47. Pop, R. et al. A key commitment step in erythropoiesis is synchronized with the
845–848 (2016). cell cycle clock through mutual inhibition between PU.1 and S-phase
27. Moignard, V. et al. Decoding the regulatory network of early blood development progression. PLoS Biol. 8, e1000484 (2010).
from single-cell gene expression measurements. Nat. Biotechnol. 33, 269–276 48. Hwang, Y. et al. Global increase in replication fork speed during a p57KIP2-
(2015). regulated erythroid cell fate switch. Sci. Adv. 3, e1700298 (2017).
28. Khoramian Tusi, B. & Socolovsky, M. High throughput single-cell fate potential 49. Shearstone, J. R. et al. Global DNA demethylation during mouse erythropoiesis
assay of murine hematopoietic progenitors in vitro. Ex. Hematol. https://doi. in vivo. Science 334, 799–802 (2011).
org/10.1016/j.exphem.2018.01.005 (2018) 50. Nemeth, E. & Ganz, T. Anemia of inflammation. Hematol. Oncol. Clin. North Am.
29. Klein, A. M. et al. Droplet barcoding for single-cell transcriptomics applied to 28, 671–681 (2014).
embryonic stem cells. Cell 161, 1187–1201 (2015). 51. Liang, R. et al. A systems approach identifies essential FOXO3 functions at key
30. Morrison, S. J. & Weissman, I. L. The long-term repopulating subset of steps of terminal erythropoiesis. PLoS Genet. 11, e1005526 (2015).
hematopoietic stem cells is deterministic and isolatable by phenotype. 52. Whitfield, M. L. et al. Identification of genes periodically expressed in the
Immunity 1, 661–673 (1994). human cell cycle and their expression in tumors. Mol. Biol. Cell 13, 1977–2000
31. Papayannopoulou, T., Brice, M., Broudy, V. C. & Zsebo, K. M. Isolation of c-kit (2002).
receptor-expressing cells from bone marrow, peripheral blood, and fetal liver:
functional properties and composite antigenic profile. Blood 78, 1403–1412 Supplementary Information is available in the online version of the paper.
(1991).
32. Weinreb, C., Wolock, S. & Klein, A. SPRING: a kinetic interface for visualizing
Acknowledgements This work was funded by a Leukemia and Lymphoma
high dimensional single-cell expression data. Bioinformatics (2017).
Society Scholar award (1728-13) and R01DK100915 and R01099281 (M.S.).
33. Weinreb, C., Wolock, S., Khoramian Tusi, B., Socolovsky, M. & Klein, A. M.
A.M.K. is supported by a BW Fund CASI award and an Edward J Mallinckrodt
Fundamental limits on dynamic inference from single cell snapshots. Proc. Natl
Foundation Grant. S.L.W. and C.W. are supported by National Institutes of Health
Acad. Sci. USA. http://doi.org/10.1073/pnas.1714723115 (2018).
(NIH) training grant 5T32GM080177-07.
34. Yanez, A. et al. Granulocyte-monocyte progenitors and monocyte-dendritic cell
progenitors independently produce functionally distinct monocytes. Immunity
47, 890–902.e4 (2017). Author Contributions M.S. and A.M.K. designed the experiments and supervised
the project. B.K.T., S.L.W., Y.H., D.H. and R.Z. performed experiments including
35. Magwene, P. M., Lizardi, P. & Kim, J. Reconstructing the temporal ordering of
inDrops (B.K.T., R.Z., S.L.W.), FACS and antibody screening (B.K.T., D.H.), single-
biological samples using microarray data. Bioinformatics 19, 842–850 (2003).
cell fate assays and cell cycle analysis (B.K.T.), western blotting (Y.H.), qRT–PCR
36. Bendall, S. C. et al. Single-cell trajectory detection uncovers progression and
(B.T.K.), pSTAT3/5 (Y.H., D.H.) and colony assays for novel growth factors (Y.H.).
regulatory coordination in human B cell development. Cell 157, 714–725
S.L.W. and C.W. performed single-cell data analysis, informatics and PBA
(2014).
37. Trapnell, C. et al. The dynamics and regulators of cell fate decisions are
modelling. A.W. and J.R.H. provided Il17ra−/− mice. B.K.T., S.L.W., C.W., Y.H., D.H.,
A.M.K. and M.S. prepared figures and wrote the manuscript.
revealed by pseudotemporal ordering of single cells. Nat. Biotechnol. 32,
381–386 (2014).
38. Bresnick, E. H., Lee, H.-Y., Fujiwara, T., Johnson, K. D. & Keles, S. GATA switches Author Information Reprints and permissions information is available at
as developmental drivers. J. Biol. Chem. 285, 31087–31093 (2010). www.nature.com/reprints. The authors declare competing financial interests:
39. Li, P. et al. Regulation of bone marrow hematopoietic stem cell is involved in details are available in the online version of the paper. Readers are welcome
high-altitude erythrocytosis. Exp. Hematol. 39, 37–46 (2011). to comment on the online version of the paper. Publisher’s note: Springer
40. Grover, A. et al. Erythropoietin guides multipotent hematopoietic progenitor Nature remains neutral with regard to jurisdictional claims in published
cells toward an erythroid fate. J. Exp. Med. 211, 181–188 (2014). maps and institutional affiliations. Correspondence and requests for
41. Mancini, E. et al. FOG-1 and GATA-1 act sequentially to specify definitive materials should be addressed to A.M.K. (allon_klein@hms.harvard.edu) or
megakaryocytic and erythroid progenitors. EMBO J. 31, 351–365 (2012). M.S. (merav.socolovsky@umassmed.edu).
42. Koulnis, M., Porpiglia, E., Hidalgo, D. & Socolovsky, M. in A Systems Biology
Approach to Blood, Vol. 844 (eds Corey, S. J.et al.) Ch. 3, 37–58 (Springer reviewer Information Nature thanks B. Göttgens, F. Hamey and the other
New York, 2014). anonymous reviewer(s) for their contribution to the peer review of this work.
60 | NATURE | VOL 555 | 1 mARch 2018
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
MethOdS n = 698; P1, n = 2,629; P1-CD71high, n = 879; P2, n = 195; P3, n = 69; P4, n = 379;
No statistical methods were used to predetermine sample size, the experiments P5, n = 62).
were not randomized and the investigators were not blinded to allocation during After cell filtering, we detected the following median number of transcripts and
experiments and outcome assessment. genes per cell, respectively: bBM, 2,989 and 1,539; eBM, 3,082 and 1,552; FL, 8,859
Ethical compliance. All mouse experiments described in this project fully comply and 2,834; P8, 3,339 and 1,637; P8-CD71high, 4,740 and 2,174; P9, 2,712 and 1,393;
with the mouse protocol issued to the Socolovsky laboratory by the Institutional P10, 4,641 and 2,158; P11, 1,783 and 1,023; P12, 2,139 and 1,195.
Animal Care and Use Committee (IACUC) of the University of Massachusetts The gene expression counts of each cell were then normalized using a variant
Medical School. of total-count normalization that avoids distortion from very highly expressed
Mice for scRNA-seq. For the basal bone marrow (bBM) sample, and for the sorted genes. Specifically, we calculated xˆi,j, the normalized transcript counts for gene j
P1–P5 populations, bone marrow was collected from 8-week-old adult BALB/cJ in cell i, from the raw counts xi,j as follows: xˆi,j =xi,jX/Xi, in which Xi = ∑
j
xi,j
female mice (Jackson Laboratories). For the EPO-stimulated bone marrow (eBM) and X is the average of Xi over all cells. To prevent very highly expressed genes (for
sample, 8-week-old adult BALB/cJ female mice were injected with EPO (Procrit, example, haemoglobin) from correspondingly decreasing the relative expression
Amgen) subcutaneously once every 24 h for a total of 48 h, at 100 U per 25 g body of other genes, we excluded genes comprising >10% of the total counts of any cell
weight. For the fetal liver (FL) sample, BALB/cJ female mice were set up for timed when calculating X and Xi.
pregnancies, and fetal livers were collected on embryonic day 13.5. Exclusion of contaminating cell types and putative cell doublets. To clean up the
Cell preparation for scRNA-seq. Tissue collection. For bone marrow preparation, data for the Kit+ samples, we clustered the single-cell transcriptomes and excluded
femurs and tibiae were collected immediately following euthanasia, and placed in clusters that were identified as contaminating (non-HPC) cell types and putative
cold (4 °C) ‘staining buffer’ (PBS containing 0.2% bovine serum albumin (BSA) cell doublets. No such clusters were detected in the P1–P5 samples. Clustering
and 0.08% glucose). Bones were flushed using a 2-ml syringe with a 26-gauge was performed as follows: we identified the principal variable genes across the
needle and then crushed with a pestle and mortar to obtain all cells. Collected bone entire dataset, as described29, that is, genes that were highly variable (top 2,000
marrow cells were filtered through a 40-μm strainer and washed in cold ‘Easy Sep’ most variable by v-score, a measure of above-Poisson noise (variability)), expressed
buffer (PBS; 2% fetal bovine serum (FBS); 1 mM EDTA). Fetal livers were prepared at non-negligible levels (at least five unique molecular identifier (UMI)-filtered
by mechanical dissociation in staining buffer and a washing in ‘Easy Sep’ buffer. mapped reads (UMIFM) in at least three cells), and which contributed to principal
Positive selection for Kit+ cells. Bone marrow and fetal liver cell samples were each components with eigenvalues greater than those obtained after data randomization
enriched for Kit-expressing cells using magnetic beads, with the Mouse Biotin (n = 59, n = 35 and n = 71 principal components for bBM, eBM and FL samples,
Selection Kit (STEMCELL Technologies, 18556) and Biotin Rat Anti-Mouse respectively). The expression level for each gene was standardized by a z-score
CD117 Antibody (clone 2B8, BD Bioscience), following the manufacturer’s transform (mean-subtraction, scaling by s.d.), followed by density-based clustering
protocol. (DBSCAN)54,55 on a 2D PCA–tSNE plot (principal component analysis (PCA) fol-
Density gradient centrifugation. Following magnetic bead selection, dead cells and lowed by t-distributed stochastic neighbour embedding (tSNE56), as described29,57).
debris were removed from the bone marrow and fetal liver samples using density The tSNE algorithm perplexity parameter was set to 30. Examination of the expres-
centrifugation in OptiPrep (Sigma, D1556). In brief, cells were re-suspended in sion of marker genes in each cluster was then used to identify putative doublets
0.5 ml staining buffer, mixed with 1 ml of 40% of OptiPrep in PBS, and placed and contaminating cell types.
in a 5-ml tube. The cell suspension was carefully over-layered with 2 ml of 20% In the bBM sample, two doublet clusters were identified: one co-expressed
OptiPrep solution, and 1 ml of 5% OptiPrep solution, and centrifuged at 800g for markers of mature macrophages and erythrocytes (n = 38 cells), and the other
15 min (centrifuge break off). The top visible cell band that formed during centrifu- co-expressed markers of granulocyte and erythroid progenitors (n = 75 cells).
gation contained the live, Kit+ single cells (confirmed by flow cytometric analysis). The eBM sample included a cluster of mature macrophages (n = 40 cells) but
This layer was carefully aspirated and used directly in the inDrops29 platform. no identifiable cluster of doublets. The FL sample contained four contaminating
Single-cell transcriptome droplet microfluidic barcoding using inDrops. For cell types: vascular endothelium, hepatocytes, mesenchymal cells and mature
scRNA-seq, we used inDrops29 following a previously described protocol53 with macrophages (n = 769 cells total), in addition to a small cluster of doublets
the modifications summarized in Supplementary Table 7. Following droplet (n = 18 cells). Doublets and contaminant cells were excluded from downstream
barcoding reverse transcription, emulsions were split into aliquots of approximately analyses.
1,000 single-cell transcriptomes and frozen at −80 °C. Two batches of Kit+ libraries To increase confidence that putative doublet clusters were indeed combina-
were prepared, referred to as batch 1 (bBM, n = 840 cells; eBM, n = 1,141 cells; tions of two single cells, rather than true intermediate or transitional states, we
FL, n = 1,953 cells) and batch 2 (bBM, n = 4,592 cells; eBM, n = 1,314 cells; FL, generated simulated ‘artificial’ doublets by randomly sampling and combining
n = 7,529 cells) in Supplementary Table 7. These cell numbers correspond to the observed transcriptomes.
final number of transcriptomes detected upon sequencing (see ‘Cell filtering and We then applied PCA–tSNE clustering as described earlier to the union of
data normalization’), and were in agreement with estimated inputs. observed and simulated cells, and identified clusters that were primarily com-
For the FACS subsets P1, P1-CD71high, P2, P3, P4, and P5 (referred to posed of cells with a large number of doublet neighbours (two clusters in bBM,
collectively as ‘P1–P5’), all libraries were prepared in parallel, with a total of 16,206 one in FL). These clusters were the same putative doublet clusters identified in the
cell barcodes detected in the sequencing data before filtering (P1, n = 5,733 cells; previous paragraph.
P1-CD71high, n = 1,631 cells; P2, n = 2,630 cells; P3, n = 2,101 cells; P4, n = 1,589 Batch correction. Within each Kit+ sample, we observed batch effects between
cells; P5, n = 2,522 cells). the first and second sequencing runs, with slightly fewer genes detected per cell
Sequencing and read mapping. The first batch of Kit+ (bBM, eBM and FL) libra- in the second run compared to the first run. This was consistent with the choice
ries was sequenced on a HiSeq 2000, the remaining Kit+ libraries were sequenced of lower sequencing depth used in the second set of runs, but could also reflect
on three NextSeq 500 runs, and all P1–P5 libraries were sequenced on a single differences in library preparation despite all cells being collected in a single droplet
NextSeq 500 run. Raw sequencing data (FASTQ files) were processed using the run. To prevent batch effects from distorting subsequent data analysis, for each
previously described53 inDrops.py bioinformatics pipeline (available at https:// sample we used the second (larger) batch to select variable genes and to calculate
github.com/indrops/indrops), with a few modifications. Bowtie v.1.1.1 was used principal component gene loadings. Cells from all batches were then projected
with parameter -e 100; all ambiguously mapped reads were excluded from analysis into the reduced space, and all subsequent analysis was performed on the reduced
and reads were aligned to the Ensemble release 81 mouse mm10 cDNA reference. principal component space.
Cell filtering and data normalization. Each sample (bBM, eBM, FL and P1–P5) Data visualization and construction of k-nearest neighbour graphs. After cell fil-
was processed separately. The bBM, eBM and FL samples (referred to collectively tering, data were prepared for visualization and PBA33 by constructing a k-nearest
as Kit+) were initially filtered to include only abundant barcodes, on the basis of neighbour (kNN) graph, in which cells correspond to graph nodes and edges con-
visual inspection of the histograms of total reads per cell (see cell numbers reported nect cells to their nearest neighbours. A kNN graph was constructed separately for
in ‘Single-cell transcriptome droplet microfluidic barcoding using inDrops’). An each of the three Kit+ samples and for the merged P1–P5 samples (note that the
additional filtering step removed cells with transcript count totals in the bottom kNN graph for P1–P5 was used only for the visualization in Extended Data Fig. 3).
fifth percentile (bBM, n = 271 cells; eBM, n = 148; FL, n = 473). Subsets P1–P5 For the Kit+ samples, genes with mean expression > 0.05 and coefficient of
were filtered only by total transcript counts, with thresholds set by visual inspection variation (s.d./mean) > 2 were used to perform PCA down to 60 dimensions
of the total counts histograms (see cell numbers reported in ‘Single-cell transcrip- (bBM, eBM and FL). For all analyses in this paper, data were z-score normalized
tome droplet microfluidic barcoding using inDrops’). Next, we excluded putatively at the gene level before PCA (qualitatively similar results were also obtained with-
stressed or dying cells with >10% (bBM, eBM and FL) or >20% (P1–P5) of their out z-score normalization, which weights highly expressed genes more heavily
transcripts coming from mitochondrial genes (bBM, n = 165 cells; eBM, n = 45; FL, than lowly expressed genes). After PCA, a kNN graph (k = 5) was constructed by
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
connecting each cell to its five nearest neighbours (using Euclidean distance in the (3) Apply the script ‘compute_fate_probabilities.py -S S.csv -V V.npy -e A.csv -D 1’,
principal component space). here inputting the lineage-specific exit rate matrix (flag ‘-S’), the potential (flag
For P1–P5, highly variable genes were filtered using the v-score statistic ‘-V’) computed in step (2), the same edges (flag ‘-e’) used in step (1) and a diffusion
(above-Poisson noise) rather than the coefficient of variation, keeping the top constant (flat ‘-D’) of 1. This step yields fate probabilities for each cell.
25% most variable genes and requiring at least three UMIFM to be detected in Figures 1–6 make use of PBA analyses of bBM data. For Fig. 4e and Extended
at least three cells (n = 3,459 genes). Additionally, a strong cell cycle signature Data Fig. 8, a temporal ordering of erythroid differentiation was generated for
was observed in the initial graph visualization, manifested by the co-localization the FL dataset using the same steps, with input files that are also provided in
of cells expressing G2/M genes (Ube2c, Hmgb2, Hmgn2, Tuba1b, Mki67, Ccnb1, Supplementary Data.
Top2a, Tubb4b). Therefore, we constructed a G2/M signature score by summing Estimation of net source/sink rate vector R. A complete definition of the vector
the average z-score of these genes, then removed genes that were highly correlated R in terms of biophysical quantities has been published previously33. In brief, for
(Pearson r > 0.2) with the signature (n = 31 genes). Finally, the kNN graph was a gene expression space described by a vector x = (x1, x2,…, xN) giving the expres-
constructed with k = 4 using the first 30 principal components. sion of each of N genes, R(x) gives the net imbalance between cell division and cell
The kNN graphs were visualized using a force-directed layout using a custom loss locally for cells with gene expression profile x. R(x) is corrected for cell enrich-
interactive software interface called SPRING58. For the Kit+ samples, several man- ment and loss resulting from experimental procedures such as sample enrichment,
ual steps were taken to improve visualization. It is important to emphasize that as follows. In this experiment, all progenitors including HSCs express Kit, but
the manipulations affect visualization only. All subsequent analyses depend on eventually downregulate it as they terminally differentiate. Thus, no cells enter the
the graph adjacency matrix, which is not affected by any of the changes to the experimental system other than through proliferation of existing Kit+ HPCs, but
graph layout. For visualization purposes, we manually extended the length of the the selection for Kit+ cells during sample isolation induces a net sink on cells
megakaryocytic, basophilic and monocytic branches by pinning the position of downregulating Kit expression. For a self-renewing system, cell division and cell
cells at the end of each branch, and allowing the remaining structure to follow. In loss are precisely balanced, so ∫R(x)dx=0. To apply PBA, one does not need to
the bBM sample, we compressed the CEP ‘bulge’ region of the graph by bringing estimate R(x), but only its value at points xi at which the M cells i = 1,…, M are
its bounding cells together. observed in the scRNA-seq measurement. Thus R is a vector over the cells in
Smoothing over the kNN graph. We smoothed data over the kNN graph for the system. For a self-renewing system, the sum over all cells satisfies the same
gene expression visualization and for one analysis (see ‘Global changes in gene constraint, ∑
i
Ri =0.
expression in stress conditions’). Smoothing was done by diffusing the property Estimation of R. We assigned negative values to R for the ten cells with the highest
of interest (for example, gene expression counts or number of mapped cells) over expression of marker genes for each of the seven terminal lineages (see
the graph, as described59. In brief, let A be the adjacency matrix of the kNN graph, Supplementary Table 1 for marker genes), which were separately confirmed to
in which Ai,j = 1 if an edge in the graph connects nodes i and j. Define A*as the show reduced Kit expression. We assigned different exit rates to each of the seven
transition matrix, obtained by row-normalizing A: lineages using a fitting procedure that ensured that cells identified as putative HSCs
would have a uniform probability to become each fate. Putative HSCs were iden-
A ⁎ = Ai,j tified by the similarity of their transcriptomes to microarray profiles from the
i,j ∑
j
Ai,j ImmGen database (we used SC.LT34F.BM (long-term bone marrow HSCs) for
bBM and SC.STSL.FL (short-term FL HSCs) for FL; for more details, see section
Let Ei be the quantity of interest (for example, expression level) in cell i. Then E*, ‘ImmGen Bayesian classifier’). We assigned a single positive value to all remaining
the smoothed vector of E, is computed as follows: cells, with the value chosen to enforce the steady-state condition ∑
i
Ri =0. In the
fitting procedure, all exit rates are initially set to one and iteratively incremented
E⁎=γ(I−(1−γ)A⁎)−1E
or decremented until the average fate probabilities of the putative HSCs were within
1% of uniform. The resulting vector R is provided in the Supplementary Data. The
in which γ is a diffusion constant (γ = 0.05 in all presented analyses) and I is the
separate lineage exit rates were then used to form the lineage-specific exit rate
identity matrix.
matrix S, also provided in the Supplementary Data.
Formal measure of the continuity of transcriptional states. To demonstrate that
Assignment of PBA fate probabilities and temporal ordering to eBM dataset.
the continuous appearance of the Kit+ transcriptomes was not a trivial outcome
For each of the eBM cells we assigned the average temporal order (or potential V)
of our analysis methods, we used the same tools to analyse an scRNA-seq data-
and average fate probabilities of the 20 mostly similar bBM cells. To do this, we
set of mature blood cells (peripheral blood mononuclear cells, PBMCs) (https://
first carried out a PCA on the bBM cells into 60 dimensions. We then used the gene
support.10xgenomics.com/single-cell-gene-expression/datasets/2.0.1/pbmc8k),
loadings of the 60 principal components to project the eBM data into the same
which consist of several distinct cell types (Extended Data Fig. 1a). In addition
principal component space. The distance of each eBM cell to each bBM neighbour
to generating a SPRING plot of the data, we also assessed the interconnectivity of
was then measured by cosine distance in the 60-dimensional sub-space.
each dataset by examining the behaviour of random walks over the kNN graphs, as ImmGen Bayesian classifier. We used a published microarray profile60 to search
previously described16. In detail, after subsampling the PBMC data to contain the
for similar cells in our own dataset using a naive Bayesian classifier, implemented
same number of cells as the bBM dataset, we applied PCA and constructed a kNN
as follows.
graph (k = 10) for each dataset. We then simulated 1,000 random walks for each
The Bayesian classifier assigns cells to microarray profiles on the basis of the
graph and plotted the fraction of nodes (cells) visited as a function of the number
likelihood of each microarray profile for each cell, with the likelihood calculated
of steps (Extended Data Fig. 1a).
by assuming that individual mRNA molecules in each cell are multinomially
PBA. The PBA algorithm calculates a scalar ‘potential’ for each cell that is analo-
sampled with the probability of each gene proportional to the microarray expres-
gous to a distance, or pseudotime, from an undifferentiated source, and a vector
sion value for that gene. Consider a matrix E of mRNA counts (UMIs) with n
of fate probabilities that indicate the distance to fate branch points. These fate
rows (for cells) and g columns (for genes), and also a matrix M with m rows (for
probabilities and temporal ordering were computed using the Python imple-
microarray profiles) and g columns (for genes). M was quantile normalized and
mentation of PBA (available online from https://github.com/AllonKleinLab/
then each microarray profile was normalized to sum to one. Normalization of E
PBA), as described33.
was performed as described earlier (see ‘Cell filtering and data normalization’).
The inputs to the PBA scripts are a set of comma-separated value (.csv) files The n × m matrix, Sij, giving the likelihood of each microarray profile j for each
encoding: the edge list of a kNN graph of the cell transcriptomes (A.csv); a vector
cell i is,
assigning a net source/sink rate to each graph node (R.csv); and a lineage-
specific binary matrix identifying the subset of graph nodes that reside at the tips of g
branches (S.csv). These files are provided in the Supplementary Data for the bBM
Sij =Zi ∏M
j
E
k
ik
and FL datasets. PBA is then run according to the following steps:
k=1
(1) Apply the script ‘compute_Linv.py -e A.csv’, here inputting edges (flag ‘-e’) where Zi is a normalization constant that ensures that ∑
i
Sij =1.
from the SPRING kNN graph (see above). This step outputs the random-walk Computing the haematopoietic lineage tree. We used the fate probabilities from
graph Laplacian, Linv.npy. PBA to infer the topology of the haematopoietic lineage tree using an iterative
(2) Apply the script ‘compute_potential.py -L Linv.npy -R R.csv’, here inputting approach (Fig. 1e, f). Each iteration began with a set of fates and a probability
the inverse graph Laplacian (flag ‘-L’) computed in step (1) and the net source/sink distribution over those fates for each cell. For every pair of fates, we computed a
rate to each graph node (flag ‘-R’). This step yields a potential vector (V.npy) that is fate coupling score (see later) and merged pairs with a score significantly higher
used for temporal ordering (cells ordered from high to low potential). The vector R than expected under a null model. The merged fates inherited probabilities from
provided in the Supplementary Data was estimated as described in the next section. the starting fates by simple pairwise addition.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
The coupling score between two fates A and B is the number of cells with The inflection point density is the number of genes turning on or off at a given
P(A)P(B) > ε, in which we used a value ε = 1/14 throughout. To generate a point on the trajectory. For each gene, inflection points were identified as the points
null distribution for each fate pair, we computed pairwise coupling scores for with maximally increasing or decreasing expression as follows. First, the trajec-
1,000 permutations of the original fate probabilities. The heat maps in Fig. 1e show tory of each dynamically varying gene was smoothed using Gaussian smoothing
z-scores with respect to these null distributions. with a width σ = 5% of total trajectory. The gene expression derivative for gene
Analysis of fate-correlated genes at haematopoietic choice points. To discover k, denoted xk, was then computed by taking a ten-cell moving average of the dif-
fate-associated genes at key choice points in haematopoiesis (Extended Data ference between consecutive smoothed gene expression values. Inflection points
Fig. 2, Supplementary Table 2), we ranked transcription factors and cell-surface were then identified as the points with maximum or minimum derivatives for each
markers (transcription factors from http://genome.gsc.riken.jp/TFdb/tf_list. gene. To exclude maxima or minima resulting from relatively small fluctuations
html, cell-surface markers from https://www.thermofisher.com/us/en/home/life- in gene expression, only appreciably large extrema were kept for further analysis.
science/cell-analysis/cell-analysis-learning-center/cell-analysis-resource-library/ Specifically, the point with the maximum derivative for gene k, max(xk), was kept
ebioscience-resources/mouse-cd-other-cellular-antigen.html) by their correlation only if
with PBA-predicted fate probability, restricting to cells that were bipotent for the
given choice. Specifically, to find transcription factors associated with fate A at max(x′ k)
>Q
an A/B choice point, we first selected cells with P(A) × P(B) > ε, and then ranked median(abs(x′ k))
the transcription factors by their correlation with the fate bias (P(A) − P(B)). In
Supplementary Table 2, we report all genes with Bonferroni-corrected P < 0.01 Minima were similarly filtered, requiring the ratio to be <−Q. We chose a
(Pearson correlation coefficient). In Extended Data Fig. 2, we show at most ten threshold Q = 6, but results do not qualitatively change over a range of Q. We
genes for any one choice point. then plotted the density of these inflection points over the MPP-to-erythroid axis.
Mapping P1–P5 subsets to the Kit+ graphs. For Fig. 2b, cells from subsets P1–P5 Regions with large-scale changes in gene expression have a high density of inflec-
were projected into the same principal component space as the bBM data, then tion points, whereas a low density characterizes relatively stable states.
mapped to their most similar Kit+ neighbours. In detail, counts were first converted Dynamic gene clustering. Dynamically varying genes were clustered on the basis
to TPM for all samples. Then, using only the bBM cells, the 3,000 most variable of their behaviour at the transition points. To prevent overfitting, we used only
genes (measured by v-score) with at least three UMIFM in at least three cells were three transitions (3%, 18% and 86%) by splitting the EEP state and assigning the
z-score normalized and used to find the top 50 principal components. Next, the first and second halves to the EBMP and CEP states, respectively. At each transi-
P1–P5 subset cells were z-score normalized using the gene expression means and tion, genes were classified as increasing, decreasing or unchanging, giving a total
s.d. from the bBM data and transformed into the bBM principal component space. of 33 = 27 possible patterns. After smoothing gene expression traces, the data were
Lastly, each P1–P5 cell was mapped to its closest bBM neighbour in principal binned by calculating the mean expression in each of the four stages. To remove
component space (Euclidean distance). noisy genes or genes that varied little across bins, we calculated the range of binned
Extracting MPP-to-erythroid trajectory cells. To isolate the erythroid trajectory, expression values, range(xi,binned) = max(xi,binned) – min(xi,binned), for each gene
we defined an MPP-to-erythroid axis in each of the three Kit+ datasets by ordering and proceeded with the top 50% most variable genes. Next, to place all genes on a
cells on the basis of their graph distance from unbiased MPPs (cells identified on similar scale, the binned expression values of each gene were divided by the max-
the basis of the ImmGen classifier as described earlier), and keeping only cells for imum binned value of that gene. Finally, the differences between consecutive bins
which the probability of erythroid fate increased or remained constant with graph were thresholded: differences that were greater than 0.15 were called increasing,
distance. Graph distance was measured by PBA potential, and starting with the differences that were less than −0.15 were called decreasing and differences that
cell closest to the HSC origin, we added the cell with next highest potential to the were between −0.15 and 0.15 were called unchanging.
trajectory if the PBA-predicted erythroid probability for cell i was at least 95% of Gene set enrichment analysis. Each of the 27 gene clusters was used as input for
the average erythroid probability of the cell(s) already in the trajectory. gene set enrichment analysis (GSEA) (hypergeometric test), using all genes as back-
More formally the procedure is as follows: order all N cells in the experiment ground. Ribosomal genes were excluded from the input, as were predicted genes
from highest to lowest PBA potential V, with decreasing potential correspond- (gene names starting with ‘Gm’). Gene sets from the following lists of the MSigDB
ing to increasing distance from MPPs33. Let Ei be an indicator variable for the v5.1 (ref. 61) dataset were tested for enrichment: Hallmark (h.all.v5.1.symbols.
membership of ordered cell i in the erythroid trajectory (Ei = 1 if cell i is in the gmt), C2 curated canonical pathways (c2.cp.v5.1.symbols.gmt), C3 transcription
trajectory; otherwise, Ei = 0). If Pi is the PBA-predicted erythroid probability for factor targets (c3.tft.v5.1.symbols.gmt), and C5 Gene Ontology (c5.all.v5.1.sym-
ordered cell i, then Ei = 1 if bols.gmt). Additionally, for the transcription factor target enrichment analysis, we
used gene sets from the ChEA database62.
Pi >0.95× ∑ k
∑
<i
k
P
<
k
i E
×
k
Ek C
ce
e
ll
l l
c
c
y
y
c
c
le
le
i n
p h
H
a
e
s
L
e
a
a
c
n
e
a
ll
l
s
y
5
s
2
i s
w
.
e
G
re
e n
u
e
s
s
e d
w
t
i
o
th
g
p
en
er
e
i
r
o
a
d
te
ic
a
e
c
x
e
p
ll
r e
c
s
y
s
c
i
l
o
e
n
p
c
h
o
a
r
s
r
e
e
s
la
c
t
o
e
r
d
e
w
fo
i
r
t h
e a
th
ch
e
cell. The list of phase-specific genes was filtered to exclude genes with a mean
Cells on the erythroid trajectory were then ordered by decreasing potential. expression > 25 TPM in cells on the MPP-to-erythroid trajectory. For Fig. 6a,
Defining tj as the index of the jth erythroid-trajectory cell, a sliding window average was computed using a window size of 10% MPP-to-
erythroid progression (~200 cells) and a jump size of 5%. For Fig. 6b, counts
tj = 1+∑Ek
were normalized by the mean expression at the gene level, and smoothed using
k<j
a Gaussian kernel. Then, a phase score was calculated for each phase (G1/S, S,
Throughout this Article, we report this cell order (akin to the ‘pseudotime’ in other G2/M, M, M/G1) by averaging the smoothed gene expression traces for the genes
publications) as a percentage of ordered cells, with the first, least differentiated cell specific to that phase.
at 0% and the most mature cell at 100%. This is not meant to suggest that erythroid Testing the influence of cell cycle genes on the MPP-to-erythroid cell order. To
differentiation ends with this final observed cell. test the extent to which cell cycle genes influenced the ordering of cells along the
Identifying dynamically varying genes. For each gene, a sliding window (n = 100 MPP-to-erythroid trajectory, we excluded annotated cell cycle genes as described63
cells) across the MPP-to-erythroid ordering was used to identify the windows with (cell cycle genes were extracted from the Gene Ontology database (GO:0007049)
maximum and minimum average expression as previously described57. A t-test was and Cyclebase64), and repeated kNN graph construction and PBA. As shown in
then performed to assess the statistical significance of the difference in expression Extended Data Fig. 10, the resulting cell order was largely unchanged, as were the
levels. To estimate the false discovery rate (FDR), we permuted the order of the dynamics of cell cycle genes.
cells and repeated the above analysis57. For a P value generated by the observed Identifying genes that change steadily in the CEP stage. To identify genes that
(non-permuted) ordering, the FDR-corrected P value is the fraction of genes from are steadily up- or downregulated throughout the CEP (Fig. 6c, Supplementary
the permuted ordering with that P value or less. Any gene with an FDR-corrected Table 6), we tested the magnitude of change (slope) and the linearity of change
P < 0.05 was considered significantly variable. (the error of the actual gene trace from a straight line) for each gene. Restricting
Identifying stage transitions in the MPP-to-erythroid trajectory. Transition analysis to cells in the CEP stage and genes with at least two UMIFM in at least
points between stages of erythropoiesis were defined using the frequency of gene five cells, we fit a linear regression to the ordered gene expression values and also
inflection points (Fig. 4b), patterns of PBA-predicted fate probabilities (Fig. 1c), generated a smoothed expression trace using a Gaussian kernel (width σ = 5%).
and the fate potentials of FACS subsets P1–P5 (Figs 2, 3). However, owing to the We then computed a ‘linearity score’ for each gene by dividing the slope of the
continuous nature of the transcriptional states, the locations of these transitions regression line by the root-mean-square error between the regression line and the
should be considered approximate. smoothed trace. Steadily increasing genes receive large positive scores, whereas
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
steadily decreasing genes are assigned large negative scores. Genes that do not After mapping stress cells to their single closest neighbour in the bBM sam-
change much or that change nonlinearly (for example, sharply increasing only at ple (as described in the previous section), we selected bBM cells in the ROI and
the end of the stage) receive scores close to 0. the stress cells mapping to them. We first identified genes differentially expressed
Global changes in gene expression in stress conditions. Cells from eBM and FL within the ROI by performing a binomial test for differential expression65, which
(stress samples) were mapped to their most similar bBM counterparts, and dif- tests the probability that a gene is expressed more frequently in one population than
ferentially expressed genes were identified. Mapping was carried out by applying another. After correcting for multiple hypothesis testing (Benjamini–Hochberg
PCA to the bBM and stress samples and finding the closest 20 bBM neighbours procedure66), we proceeded with genes with an FDR-corrected P < 0.05.
for each stress cell. Specifically, the input genes were the principal variable genes To identify genes differentially expressed specifically within the ROI and not
described in the ‘Cell filtering and data normalization’ section. Count matrices were elsewhere, we calculated the mean-normalized expression difference for ROI cells
z-score normalized separately for each sample, and PCA was performed on the and non-ROI cells for the genes found to be significant in the binomial test. For
basal sample to obtain the gene loadings. Using the top 60 principal components, two samples, A (stress) and B (basal), the mean-normalized expression difference
each sample was then transformed using these coefficients, thereby projecting the of gene i within the ROI, yin,i, is
cells into the same PCA space. To validate this mapping method, we performed the
same procedure using different subsets of bBM data as training and test sets (see y = x i A n,i −x i B n,i
‘Validation of cross-sample cell mapping’ section) in,i (x a A ll,i +x a B ll,i) /2
The 20 closest bBM neighbours (Euclidean distance) of each stress cell were
found, and for the purpose of comparing gene expression, each of these k (20) in which xA is the average expression of gene i within the ROI in sample A.
in,i
neighbours inherited 1/k (1/20) of the transcript counts from the mapped stress A simi lar score was calculated for cells outside the ROI:
cell. To enable the comparison of regions of gene expression space (as opposed to
comparing single mapped cells to single basal cells), the mapped and original gene y = x o A ut,i −x o B ut,i
expression values were smoothed over the kNN graph, as described in ‘Smoothing out,i (x a A ll,i +x a B ll,i) /2
over the kNN graph’. To avoid comparing gene expression patterns in regions that
were relatively unpopulated in the stress sample (for example, parts of the granulo- Plotting yin,i against yout,i clearly reveals genes that are more highly differentially
cyte branch), we smoothed the number of mapped stress cells per basal cell over the expressed within the ROI than without. A single score per gene was computed
graph and then excluded basal cells with few mapped stress cells (number mapped as follows:
cells ≤ 9 for eBM and ≤ 20 for FL).
ma A xi m di u ff m er - e n n o t r i m al a e l x iz p e r d e s d s i i f o fe n r e s n c c o e r e b e fo tw r e e e a n c h m c a e p l p l e i d a n a d n d g e b n as e a j l w ex a p s r d es e s f i i o n n e , d xˆ a ⁎ i, s j a t n h d e scorei =       m m i a n x ( ( y y i i n n , , i i − − m m i a n x ( ( y y o o u u t t , , i i , , 0 0 ) ) , , 0 0 ) )i i f f y y i i n n , , i i > < 0 0
xˆi,j, respectively:
Intuitively, this score is large and positive if a gene is more strongly upregulated
di,j =
0.5×(ma
xˆ
x
⁎ i,
(
j
xˆ
−
⁎
j
)
xˆ
+
i,j
max(xˆj))
w
re
i
g
t
u
h
l
i
a
n
t e
th
d
e
w
R
it
O
h
I
in
th
th
an
e R
w
O
ith
I
o
th
u
a
t,
n
l a
w
r
i
g
t
e
h o
an
u
d
t a
n
n
e
d
g a
c
t
lo
iv
s
e
e
i
t
f
o
a
0
g
o
en
th
e
e
i
r
s
w
m
is
o
e
r
.
e strongly down-
To build gene lists for GSEA input, we first selected genes with
A gene level score, Dj, was created by summing over the cells, Dj =∑
i
di,j. Genes scorei > 0.1 × max(score) (for upregulated genes) or scorei < 0.1 × max(score) (for
were considered differentially expressed if Dj >D+2×σ DorDj <D−2⋅σ D, downregulated genes) and then used the top 100 genes by binomial test P value.
in which D is the average over all gene level scores Dj and σ D is the standard deviation. Flow cytometric sorting for P1–P5 subsets. A detailed protocol of this procedure
Then, for each differentially expressed gene, the gene was counted as differen- can be found at the Protocol Exchange67.
tially expressed at a given cell if di,j > 0.5 × δ high or di,j < 0.5 × δ low, in which δ high is Bone marrow cells from adult BALB/cJ male or female mice (aged 8–12 weeks)
the 99th percentile of Dj and δ low is the 1st percentile of Dj. were lineage-depleted using the Mouse Streptavidin RapidSpheres Isolation Kit
Validation of cross-sample cell mapping. To test the accuracy of the method (STEMCELL Technologies 19860A), with the following biotinylated antibod-
for mapping eBM and FL cells to bBM cells, we divided the bBM sample into a ies: anti-CD11B (clone M1/70, BD Biosciences 557395), anti-LY-6G and LY-6C
training set (random sample of 75% of the cells) and test set (the remaining 25%). (clone RB6-8C5, BD Biosciences 553125), anti-CD4 (clone RM4-5, BD Biosciences
The mapping procedure described in the previous section was then used to map 553045), anti-CD8A (Ly-2) (clone 53-6.7, BD Bioscience 553029), anti-CD19
the test set to the training set. As one measure of the accuracy of the mapping, we (clone 1D3, BD Biosciences 553784), anti-TER119 (clone TER119, BD Biosciences
assigned the test cells the average PBA-predicted fate probabilities and differen- 553672).
tiation ordering of the training cells to which they mapped. Both measures were Lineage-depleted cells were then labelled with the following antibodies in the
relatively unchanged from their original values (Spearman correlation of 0.97 for presence of 1% rat serum: streptavidin Alexa Fluor 488 (Molecular Probes) to mark
the differentiation ordering and >0.95 for each fate probability). As a second meas- lineage-positive cells, CD117–APC Cy7 (clone 2B8, Biolegend 105826), TER119–
ure, we repeated the test for finding global changes in gene expression, using the BUV395 (clone TER-119, BD Biosciences 563827), CD71–PE Cy7 (clone RI7217,
same gene level score (Dj) cut off as for the eBM sample. This revealed no signifi- Biolegend 113812), CD55–AF647 (clone RIKO-3, Biolegend 131806), CD105–
cantly differentially expressed genes between the training and test sets. PE (clone MJ7/18, Biolegend 120408), CD150–BV650 (clone TC15-12F12.2,
Region-specific differential expression. Before identifying differentially expressed Biolegend 115931), CD41–BV605 (clone MWReg30, Biolegend 133921), CD49f
genes, we excluded genes with large batch effects. Although different sequencing (also known as ITGA6)–BV421 (clone GoH3, Biolegend 313624)
depths led to a small change in the average expression of many genes from the first After washes, cells were re-suspended in DAPI-containing buffer and sorting
batch to the second, a small number of genes showed major batch effects beyond was performed using a BD FACSAria II with a 100-μm nozzle. Sorted populations
this, presumably owing to differences in library preparation. We performed a bino- were defined as in Fig. 2a.
mial test for differential expression65 between the two batches of cells and excluded qRT–PCR on sorted populations. RNA was prepared from sorted cell subsets
genes with P < 10−50, resulting in the removal of 461 genes. using the RNeasy Micro Kit (Qiagen 74004) or TRIzol reagent (Ambion 15596026),
In general, genes can be differentially expressed globally or only in specific and measured with RiboGreen RNA reagent kit (Thermo Fisher Scientific) on
cell populations. Particularly when comparing FL to bBM samples, many genes the 3300 NanoDrop Fluorospectrometer. cDNA was synthesized using the same
showed global up- or downregulation. To identify differentially expressed genes amount of input RNA for all samples in a parallel reaction, using the Super Script
that are likely to be important specifically for erythropoiesis (or in a particular III first-strand synthesis system for RT–PCR (Invitrogen) with random hexamer
stage of erythropoiesis), we created a region-specific differential expression score. primers. The ABI 7300 sequence detection system, TaqMan reagents and TaqMan
This score measures the magnitude of the expression difference within a region MGB probes (Applied Biosystems) were used following the manufacturer’s instruc-
of interest (ROI) relative to the magnitude outside the region; genes with a larger tions. Quantitative PCR was carried on four serial dilutions of each cDNA sample,
difference within the ROI than outside of it receive a high score (positive for upreg- and the linear part of the template dilution/signal response curve was used to
ulation, negative for downregulation). For the analyses described here, we tested calculate relative mRNA concentrations following normalization to Actβ, using
for differential expression in five ROIs: the stages of the erythroid trajectory, EBMP, the ΔCt method.
EEP, CEP, and ETD and an expanded selection of MPP cells, which included cells The following TaqMan MGB probes were used: Mst1r (Mm00436382_m1), Ryk
with a maximum PBA-predicted lineage probability (for all lineages) less than 0.4, (Mm01238551_m1), Il17ra (Mm00434214_m1), Mt2 (Mm00809556_s1), Slc26a1
with the exception of cells already included in one of the stages of the erythroid (Mm01198850_m1), Slc4a1 (Mm00441492_m1), Trib2 (Mm00454876_m1), Cd34
trajectory. (Mm00519283_m1), Meis1 (Mm00487664_m1), Hpn (Mm01152654_m1), Pf4
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
(Mm00451315_g1), Dntt, (Mm00493500_m1), Ms4a2 (Mm00442778_m1), Elane s.e.m.(p)= E(p)(1−E(p)) , in which p is the fraction of bipotent cells, n is the
(Mm00469310_m1), S100a9 (Mm00656925_m1), F13a1 (Mm00472334_m1),
N+3
observed number of bipotent cells, and N is the total number of cells assayed.
Egr1 (Mm00656724_m1), Apoe (Mm01307193_g1), Ldb1 (Mm00440156_m1),
Growth factor perturbations of erythroid colony formation. CFU-e and BFU-e
Zfpm1 (Mm00494336_m1), Tfrc (Mm00441941_m1), Hbb-b1 (Mm01611268_g1),
colony-formation assays in MethoCult (STEMCELL Technologies M3234) were
Alas2 (Mm01260713_m1), Band3 (also known as Slc4a1) (Mm01245920_g1), Nfe2
carried out on either freshly isolated adult bone marrow or on fetal liver cells
(Mm00801891_m1), Gata1 (Mm01352636_m1), Gata2 (Mm00492300_m1), Klf1
extracted at embryonic day 13.5 from BALB/cJ mice. The following growth fac-
(Mm00516096_m1) and Spi1 (also known as PU.1) (Mm00488393_m1).
tors were tested: MSP/MST1 (R&D Systems 6244-MS-025), recombinant human/
Colony-formation assays in methylcellulose for P1–P5 and Kit+CD55−
mouse WNT5A (R&D Systems 645-WN-010) and recombinant murine IL-17A
cells. From each freshly sorted cell population, 10,000 cells were mixed with
(PeproTech 210-17). In each experiment, a range of EPO concentrations was tested,
1 ml MethoCult (M3234, STEMCELL Technologies) supplemented with EPO
with or without additional growth factors (MSP, WNT5A or IL-17A) as indicated
(2 U ml−1), stem-cell factor (SCF) (50 ng ml−1), IL-3 (10 ng ml−1) and IL-6 in Fig. 5 and Extended Data Fig. 9. In the BFU-e assays, IL-3 (10 ng ml−1) and SCF
(10 ng ml−1). Erythroid (CFU-e or BFU-e) and granulocytic/monocytic colo- (50 ng ml−1) were added to the MethoCult in addition to EPO. Each condition was
nies were scored from triplicate plates on days three, four and seven of culture.
tested in quadruplicate in at least two separate experiments. Colonies were scored
Haemoglobin expression in erythroid colonies was verified by staining with
on day 3 (for CFU-e), day 4 (for late BFU-e) and day 7 (for early BFU-e) following
diami nobenzidine in situ before scoring.
staining with diaminobenzidine, to highlight haemoglobin expression.
For megakaryocytes, the colony-formation assay was carried out using Il17ra−/− mice. To generate the Il17ra−/− line, Il17raflox/+ mice68 were bred with
MegaCult-C Complete Kit (04970/04972) with added thrombopoietin (TPO) CMV-Cre mice (Jackson Laboratory 003465). The generation of the Il17ra− allele
(50 ng ml−1), IL-3 (10 ng ml−1), IL-6 (20 ng ml−1) and IL-11 (50 ng ml−1). From in the F1 generation of Il17raflox/+ and CMV-Cre mating pairs was screened by
each freshly sorted subset, 10,000 cells were plated in double chamber slides. On PCR of tail DNA. To remove the CMV-cre allele present in the F1 generation,
day seven of culture, the slides were dehydrated, fixed in ice-cold acetone, and Il17ra−/+CMV-cre+/− mice were outcrossed with B6 mice.
stained for acetylcholinesterase. Colony-formation assays with human bone marrow. Human bone marrow
Bulk liquid cultures of sorted cell populations. Sorted cells were cultured in mononuclear cells (85,000 cells, STEMCELL Technologies 70001.1) were mixed
IMDM medium in the presence of 20% FCS supplemented with SCF (50 ng ml−1), with 1 ml MethoCult (STEMCELL Technologies H4230) supplemented with EPO
IL-3 (10 ng ml−1), IL-6 (10 ng ml−1), EPO (2 U ml−1), TPO (50 ng ml−1), IL-11 (0.05 U ml−1), in the presence or absence of IL-17A (R&D Systems 7955-IL-025).
(50 ng ml−1) and IL-5 (10 ng ml−1) for 7 days. Cells were collected on days two, CFU-e colonies were scored from triplicate plates on day 7.
five and seven, and labelled with the following cell-surface markers for flow cyto- Cell cycle studies. Flow cytometric cell cycle analysis of bone marrow cells in vivo.
metric analysis: TER119–BV421 (clone TER-119, Biolegend 116233), CD71–PE Flow cytometric analyses were carried out as described47. In brief, BrdU (100 μl
Cy7 (clone RI7217, Biolegend 113812), CD117–APC Cy7 (clone 2B8, Biolegend of 10 mg ml−1 stock in PBS) was injected intraperitoneally into adult mice 30 min
105826), FCER1A–AF700 (clone MAR-1, Biolegend 134323), CD41–BV605 (clone before euthanasia. After collection of bone marrow, cells were immediately placed
MWReg30, Biolegend 133921), CD11B–PE Cy5 (clone M1/70, Biolegend 101209), in cold staining buffer, labelled using a LIVE/DEAD kit (Invitrogen) to identify
LY 6G/C–FITC (clone RB6-8C5, BD Biosciences 553126). dead cells and were then fixed and permeabilized. Cell-surface staining for each of
Single-cell liquid cultures of mouse bone marrow progenitors. Freshly collected the five subsets P1–P5 was carried out as described earlier. Simultaneously, incor-
mouse bone marrow was labelled with the same antibody scheme as detailed ear- porated BrdU was detected using a biotin-conjugated anti-BrdU antibody (Abcam)
lier, to allow identification of the Kit+ gates for P1–P5 and CD55−. Single cells following mild digestion with DNaseI. DNA content was assayed by labelling with
were sorted from each of these gates into 96-well plates, retaining index-sorting the fluorescent indicator 7-AAD (BD Biosciences). Cells were then analysed for
parameters for each cell, using a BD FACSAria II with a 130-μm nozzle. Cells cell-surface labelling, BrdU incorporation and DNA content by flow cytometry.
were cultured for 3–10 days in IMDM with 20% FBS, with the following added Cell cycle arrest studies during erythroid differentiation in vitro. Bone marrow cells
growth factors: SCF (50 ng ml−1; recombinant murine SCF, Peprotech 250-03), were collected and immediately enriched for Kit+Lin−TER119−CD71− cells using
IL-3 (10 ng ml−1; recombinant murine IL-3, Peprotech 213-13), IL-6 (10 ng ml−1; magnetic beads, as described earlier. The enriched cell fraction was initially placed
recombinant murine IL-6, Peprotech 216-16), EPO (2 U ml−1; PROCRIT (epoetin in culture in IMDM with 20% FCS and EPO (2 U ml−1), in the presence or absence
alfa) 606-10-971-8), IL-11 (50 ng ml−1; recombinant murine IL-11, Peprotech of aphidicolin (6 μM, Sigma A0781). After 10 h, all the cells were washed three
220-11), IL-5 (10 ng ml−1; recombinant murine IL-5, Peprotech 215-15), TPO times in culture medium to remove aphidicolin, and returned to culture, which
(50 ng ml−1; recombinant murine TPO, Peprotech 315-14), G-CSF (15 ng ml−1; continued for up to a total of 36 h.
recombinant murine G-CSF, Peprotech 250-05), GM-CSF (15 ng ml−1; recombi- At the indicated time points, cell aliquots were taken for RNA extraction fol-
nant murine GM-CSF, Peprotech 315-03). lowed by qRT–PCR of Hbb-b1 and Actb and for a simultaneous flow cytometric
Fresh growth factors were added to the medium of each well on days 4 and 8. analysis of CD71, TER119 expression and cell cycle status. For the latter, cells were
The clones in each well were labelled on days 3, 7 or 10, with the same antibody pulsed with BrdU (33 μM) in vitro for 25 min before collection, then processed as
cocktail as described in the ‘Bulk liquid cultures of sorted cell populations’ sec- described earlier for BrdU incorporation, DNA content and cell-surface CD71
tion, but with concentrations for each antibody batch that were first optimized and TER119 expression.
with appropriate titrations, to minimize non-specific binding under conditions of Western blot analysis. Bone marrow cells were sorted as described earlier, except
low cell number. Clones were analysed using the high throughput sampler (HTS) that the P1 population was further subdivided into CD71medium and CD71high sub-
attachment of the BD LSR II (BD Biosciences). sets. For negative controls, we used 3T3-L1 cells. For positive controls, 3T3-L1 cells
Fate co-occurrence from single-cell liquid culture data. To measure the statistical were transduced with the MICD4-GATA1 retrovirus as described47. Cell pellets
significance of fate co-occurrence from the single-cell fate assay data, we used were snap-frozen in liquid nitrogen after sorting.
a method similar to that described for calculating fate couplings from the PBA Cell lysates were quantified using the BCA Protein Assay Kit (Pierce) and
predictions (see ‘Computing the haematopoietic lineage tree’ section). Because we sepa rated by SDS–PAGE. PVDF membranes were probed with antibodies against
assayed clonal fate from each FACS subset separately, clones were not represented at GATA1 (N6, Santa Cruz sc-265), β-actin (Abcam ab8227), MCM5 (Bethyl
the same frequency as in the Kit+ pool (number of clones assayed: CD55−, n = 58; Laboratories A300-195A-M), MCM6 (Bethyl Laboratories A300-194A), MCM2
P1, n = 287; P2, n = 324; P3, n = 125; P4, n = 96; P5, n = 268; average frequency in (Bethyl Laboratories A300-191A), PCNA (PC10) (Santa Cruz sc-56) and IL-17RA
Kit+ population: CD55− 59.1%, P1 21.4%, P2 6.6%, P3 4.0%, P4 0.8%, P5 4.9%). (R&D Systems AF448).
To adjust for this, we randomly resampled the clone data to ensure clones from Western blot membranes were quantified using the BIORAD Imaging system
each subset were represented in the same proportion as in the Kit+ population and Image Laboratory software.
(originally: n = 1,158 clones; after resampling: n = 8,000 clones). We then com- Intracellular signalling by STAT3 and STAT5. Freshly collected bone marrow
puted the observed fate co-occurrence for each fate pair as the number of clones cells were enriched for Lin−TER119− cells using magnetic beads, as described
with >2% of cells of the two fates (permitting the presence of other fates as well). above. The enriched cells were incubated in cytokine-free, low-serum medium
Next, we estimated the null distribution by shuffling the data of each fate separately (IMDM with 2% FCS) for 3 h. EPO (0.5 U ml−1), IL-17A (20 ng ml−1) or both
(2,000 replicates) and counting fate co-occurrence as described earlier. Lastly, we together was then added to the medium for either 30 or 60 min. Cells were
calculated the significance of the co-occurrence of each fate pair as the z-score of collected, washed with PhosphoWash Buffer69, stained with a LIVE/DEAD
the observed co-occurrence with respect to the null distribution. kit (Invitrogen), fixed and permeabilized with Cytofix/Cytoperm Buffer (BD
In Fig. 3d, the expectation value (E) and s.e.m. for the fraction of Biosciences 554722) supplemented with 1 mM sodium orthovanadate (Sigma
bipotent erythroid–basophil cells from each independent experiment were calcu- 450243-10G), 1 mM β-glycerophosphate (Sigma G9422-10G) and 1 μg ml−1
lated from a β posterior distribution, that is, E(p) = (n + 1)/(N + 2) and Microcystin (EMD Millipore 475815-500UG), and Perm/Wash Buffer I
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
(BD Biosciences 557885), and frozen in freezing medium (90% FCS, 10% DMSO, 57. Macosko, E. Z. et al. Highly parallel genome-wide expression
1 mM sodium orthovanadate, 1 mM β-glycerophosphate and 1 μg ml−1 micro- profiling of individual cells using nanoliter droplets. Cell 161, 1202–1214
(2015).
cystin). When thawed, cells were re-fixed and permeabilized, incubated with
5% milk and 200 μg ml−1 rabbit IgG (modified from ref. 69), and stained with 58. Weinreb, C., Wolock, S. & Klein, A. SPRING: a kinetic interface for visualizing
high dimensional single-cell expression data. Bioinformatics https://doi.
p-STAT3-AF488 (B-7) (Santa Cruz sc-8059 AF488), p-STAT5-AF647 (pY694) org/10.1093/bioinformatics/btx792 (2017).
(BD Bioscience 612599), CD71–PE/Cy7 (Biolegend 113812), CD55–PE (Biolegend 59. Vandin, F., Upfal, E. & Raphael, B. J. Algorithms for detecting
131804), CD105–Pacific Blue (Biolegend 120412), CD150–BV650 (Biolegend significantly mutated pathways in cancer. J. Comput. Biol. 18, 507–522
115931), CD49f–PE/Dazzle 594 (Biolegend 313626), CD41–BV605 (Biolegend (2011).
60. Heng, T. S. et al. The Immunological Genome Project: networks of
133921), CD117 (Kit)–APC/H7 (BD Bioscence 560185), strepavidin–AF700
gene expression in immune cells. Nat. Immunol. 9, 1091–1094
(Invitrogen S21383) and DAPI. Analysis was performed on an LSRII FACS (2008).
analyser. 61. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based
Code availability. Python scripts are described in the PBA section, and approach for interpreting genome-wide expression profiles. Proc. Natl Acad.
Supplementary Data 1 contains the input data files and code for running PBA on Sci. USA 102, 15545–15550 (2005).
62. Lachmann, A. et al. ChEA: transcription factor regulation inferred from
the bone marrow and fetal liver datasets. Code is available at https://github.com/
integrating genome-wide ChIP-X experiments. Bioinformatics 26, 2438–2444
indrops/indrops, https://github.com/AllonKleinLab/SPRING and https://github. (2010).
com/AllonKleinLab/PBA. 63. Scialdone, A. et al. Computational assignment of cell-cycle stage from
Data availability. Sequence data that supports the findings of this study have single-cell transcriptome data. Methods 85, 54–61 (2015).
been deposited in the Gene Expression Omnibus (GEO) with the accession code 64. Santos, A., Wernersson, R. & Jensen, L. J. Cyclebase 3.0: a multi-organism
GSE89754. An interactive tool for the interpretation of these data is available at database on cell-cycle regulation and phenotypes. Nucleic Acids Res. 43,
D1140–D1144 (2015).
https://kleintools.hms.harvard.edu/paper_websites/tusi_et_al/.
65. Shekhar, K. et al. Comprehensive classification of retinal bipolar neurons by
Source Data files are provided for Figs 2c–e, 3b, 5b–d, 6f, Extended Data Figs 3a, single-cell transcriptomics. Cell 166, 1308–1323.e1330 (2016).
4c, 5a, b, 7b, 9b, 10e, f–h and for all immunoblots (Supplementary Fig. 1). 66. Benjamini, Y. & Hochberg, Y. Controlling the false discovery rate: a practical
and powerful approach to multiple testing. J. R. Stat. Soc. Series B Stat.
53. Zilionis, R. et al. Single-cell barcoding and sequencing using droplet Methodol. 57, 289–300 (1995).
microfluidics. Nat. Protocols 12, 44–73 (2017). 67. Tusi, B. K. & Socolovsky, M. Novel FACS strategy for identification of early
54. Ester, M., Kriegel, H., Sander, J. & Xu, X. A density-based algorithm for hematopoietic progenitors including BFU-e, CFU-e and erythroid-biased MPPs
discovering clusters in large spatial databases with noise. In Proc. 2nd Protoc. Exch. http://doi.org/10.1038/protex.2018.031 (2018).
International Conference on Knowledge Discovery and Data Mining 68. El Malki, K. et al. An alternative pathway of imiquimod-induced psoriasis-like
(Eds Simoudis, E. et al.) 226–231 (AAAI, 1996). skin inflammation in the absence of interleukin-17 receptor a signaling.
55. Daszykowski, M., Walczak, B. & Massart, D. L. Looking for natural patterns in J. Invest. Dermatol. 133, 441–451 (2013).
data: Part 1. Density-based approach. Chemomtr. Intell. Lab. Syst. 56, 83–92 69. Porpiglia, E., Hidalgo, D., Koulnis, M., Tzafriri, A. R. & Socolovsky, M. Stat5
(2001). signaling specifies basal versus stress erythropoietic responses through
56. van der Maaten, L. Accelerating t-SNE using tree-based algorithms. J. Mach. distinct binary and graded dynamic modalities. PLoS Biol. 10, e1001383
Learn. Res. 15, 3221–3245 (2014). (2012).
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
Extended Data Figure 1 | See next page for caption.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
Extended Data Figure 1 | scRNA-seq of Kit+ haematopoietic c, Schematic of the population balance law, which relates the dynamic
progenitors for prediction of the early haematopoietic hierarchy. velocities of cells to the distribution of states they are in at a moment in
a, Top, SPRING plot of 7,959 human peripheral blood mononuclear cells time. The law states that in steady state, after accounting for cell division
(PBMCs) from 10X Genomics (https://support.10xgenomics.com/single- and loss, the flux of cells entering any region of gene expression space
cell-gene-expression/datasets/2.0.1/pbmc8k). Clusters were generated equals the flux out of that region. d, Flow diagram of the inputs and
by performing spectral clustering on the underlying kNN graph and outputs of the PBA algorithm. The population balance law is applied
annotated on the basis of marker genes. NK, natural killer. Random walks to inputs that include single-cell expression data and estimates of cell
over kNN graphs for the PBMC (middle) and Kit+ bone marrow (bottom) proliferation and loss rates at each point in gene expression space;
datasets. Each plot shows the fraction of nodes (cells) visited for 1,000 inferred outputs include cell dynamics such as fate probabilities and
simulated random walks. b, Top, SPRING plot of 2,855 Lin−Kit+SCA1− pseudo-temporal ordering. e, SPRING plot of bone marrow Kit+ cells
mouse HPCs from a previously published dataset12. Bottom, SPRING plot (Fig. 1) constructed using only the PBA-predicted fate probabilities and
of 1,656 cells from three mouse haematopoietic progenitor populations differentiation ordering as inputs (n = 4,763 cells from one inDrops
(Lin–Kit+Sca1–, Lin–Kit+SCA1+, and Lin–Kit+SCA1+FLK2–CD34+) experiment). Coloured cells indicate expression of lineage-specific genes
from a previously published dataset15. Coloured (non-grey) cells indicate as in Fig. 1b. f, SPRING plot of bone marrow Kit+ cells (Fig. 1), with cells
expression of lineage-specific genes (see Supplementary Table 7). coloured by library preparation batch.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
