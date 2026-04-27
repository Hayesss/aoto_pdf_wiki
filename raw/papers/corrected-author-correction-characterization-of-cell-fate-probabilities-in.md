---
source_path: /mnt/c/Users/Administrator/Zotero/storage/PLWC4L3P/s41587-019-0068-4.pdf
ingested: 2026-04-23
sha256: 3ee7cf67dd11d8c9
---

Articles
https://doi.org/10.1038/s41587-019-0068-4
Corrected: Author Correction
Characterization of cell fate probabilities in
single-cell data with Palantir
Manu Setty, Vaidotas Kiseliovas, Jacob Levine, Adam Gayoso, Linas Mazutis and Dana Pe’er*
Single-cell RNA sequencing studies of differentiating systems have raised fundamental questions regarding the discrete ver-
sus continuous nature of both differentiation and cell fate. Here we present Palantir, an algorithm that models trajectories of
differentiating cells by treating cell fate as a probabilistic process and leverages entropy to measure cell plasticity along the
trajectory. Palantir generates a high-resolution pseudo-time ordering of cells and, for each cell state, assigns a probability of
differentiating into each terminal state. We apply our algorithm to human bone marrow single-cell RNA sequencing data and
detect important landmarks of hematopoietic differentiation. Palantir’s resolution enables the identification of key transcrip-
tion factors that drive lineage fate choice and closely track when cells lose plasticity. We show that Palantir outperforms exist-
ing algorithms in identifying cell lineages and recapitulating gene expression trends during differentiation, is generalizable to
diverse tissue types, and is well-suited to resolving less-studied differentiating systems.
Differentiation is among the most fundamental processes in points along the trajectory where the differentiation potential (DP)
biology. In the traditional view, cells transition from a less- drastically shifts. These shifts mark key events in hematopoiesis.
to a more-differentiated state via a series of discrete, well- Palantir thus provides a quantitative approach to characterizing a
defined stages. Single-cell studies1–6 have, however, demonstrated continuous model of cell fate choice.
that during differentiation cell states reside along largely continuous
spaces. Despite this evolution in thinking, cell fate decisions con- Results
tinue to be largely conceptualized as a series of discrete bifurcations Development as a Markov process. Differentiation proceeds
along development, leading to terminal cell states7,8. through cell divisions, where daughter cells are generally very
Epigenetic studies, however, support a probabilistic view of cell similar to their mother cells. Thus, the population is established
fate choice. Epigenomic measurements such as DNase I hypersensi- by incremental divergences, driven by regulatory mechanisms that
tivity site sequencing (DNase-seq) and assay for transposase-acces- create paths through the space of possible cell states (phenotypes).
sible chromatin using sequencing (ATAC-seq) suggest potential Regulation constrains cell states to a low-dimensional manifold of
mechanisms for a continuous process by indicating that progressive possible phenotypes12. Nearest-neighbor graphs, where each node
enhancer restriction, coupled with pre-establishment of lineage- represents a particular cell state and edges connect most similar
specifying enhancers in precursor cells, can serve as a vehicle for cells, have been widely used to model this manifold1–3,13.
driving differentiation5,9,10. Indeed, in human bone marrow, we A single bone marrow sample contains the full spectrum of cell
observe a lack of well-defined bifurcation points when single-cell states in hematopoiesis and importantly the frequencies of each
RNA sequencing (scRNA-seq) profiles are projected along the cell state. We leverage cell state frequencies to inform our model of
strongest axes of variation (Fig. 1a). Even at the level of individual possible differentiation paths in the neighbor graph and their likeli-
genes, we find a broad representation of gene ratios rather than hoods. Critically, paths along the graph represent probable trajec-
bimodal expression states (Fig. 1a). These observations raise funda- tories of cells in the population rather than the path of a particular
mental questions about whether cell fates, similar to cell state transi- cell, and each cell state (graph node) is associated with a probabil-
tions, are continuous and when and how cell fate choices are made. ity distribution for reaching the terminal states. We assert that cells
To investigate these questions, we developed Palantir, an algo- traverse the manifold in small steps which can be modeled using a
rithm that leverages scRNA-seq data to model the landscape of dif- Markov chain to represent cell fate choices in a probabilistic manner,
ferentiation and characterize continuity in both cell state and fate based on two key assumptions. Firstly, as in all pseudo-time infer-
choice. As differentiation is asynchronous, sequencing a population ence algorithms1,3,7,8, we assume unidirectional progression from a
of differentiating cells yields a snapshot representing a range of cell less- to a more-differentiated state. We posit that it is a reasonable
states. Based on scRNA-seq data from a single sample and the selec- first order approximation for healthy differentiation, but note that
tion of a representative early cell, Palantir generates a pseudo-time it fails in aberrant systems such as cancer, which require additional
ordering of cells and, for each cell state, assigns a probability for information (for example, mutations) to determine directionality.
differentiating into each terminal state. We applied Palantir to char- Second, we assume that for any node, the probability of traversing
acterize human hematopoietic differentiation using scRNA-seq pro- to any neighbor is independent of its history, that is, the path taken
files of ~25,000 cells enriched for CD34, a marker for hematopoietic to reach that state. Note that for a particular cell, the cell’s develop-
stem and progenitor cells11. Palantir identified established termi- mental history is likely to be encoded in its epigenetic profile and
nal states and ordered cells along a pseudo-time that recapitulated will probably impact cell fate choices. However, nodes are abstract
known marker trends in development. Notably, Palantir identified cell states representing multiple histories and potential trajectories
Program for Computational and Systems Biology, Sloan Kettering Institute, Memorial Sloan Kettering Cancer Center, New York, NY, USA.
*e-mail: peerd@mskcc.org
NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology 451
Articles NAtuRe BiotecHNology
rather than the path of an individual cell. Accounting for all past Generalized additive models are particularly suitable for deriving
paths into this cell state, we can compute population-level prob- a robust estimate of nonlinear trends and estimating the standard
abilities for future states, based on the structure and connectivity of error of prediction16.
nodes in the graph manifold.
Landscape of early human hematopoiesis. Hematopoiesis is a
The Palantir algorithm. Given scRNA-seq data from a sample of well-studied biological process with established markers to facilitate
differentiating cells and the expression profile of a user-defined the identification of lineages11, and many pseudo-time algorithms
‘early’ cell, Palantir orders cells along a pseudo-time, characterizes have been developed using it as a model system2,7,17. While scRNA-
terminal differentiated states, and assigns each cell a probability dis- seq has been extensively used to study hematopoiesis in mouse6,18,
tribution representing the cell’s branch probability for reaching each we chose to investigate early human hematopoiesis, since single-cell
terminal state (Supplementary Note 1). studies are particularly empowering in a system where perturbations
First, we represent the phenotypic manifold using a nearest- are not possible. Hematopoiesis has classically been characterized
neighbor graph (Supplementary Fig. 1a and Supplementary Note 1). as a series of bifurcations leading to mature, terminal cell states11,
We use diffusion maps14 to focus on developmental trends and avoid but single-cell profiling of sorted populations suggests a continuous
spurious edges resulting from the sparsity and noise in scRNA-seq. process of fate assignment4,5. Fundamental questions remain about
Projecting the data onto the top diffusion components effectively how cell fate choice is determined at the earliest stages of human
focuses edges in directions with high cell density and reweighs hematopoiesis and the degree of plasticity in early progenitors.
similarity along these directions (Supplementary Fig. 1a). Diffusion To investigate these cell fate choices, we generated approximately
maps have been previously used to study single-cell data2,3 and are 25,000 single-cell transcriptomes of bead-purified CD34+ cells from
particularly adept at capturing differentiation trajectories3,15. Unlike 3 human bone marrow donors using 10X Chromium (Methods).
other tools, Palantir uses multiple diffusion components when com- We first clustered the scRNA-seq profiles using PhenoGraph13
puting the pseudo-time ordering of cells, since we observe that a (Supplementary Fig. 4a). We identified the full complement of
single diffusion component can only approximate trajectories lead- hematopoietic cells, including hematopoietic stem and progeni-
ing to a subset of fates (Supplementary Fig. 2). Shortest paths from a tor cells, as well as cells committed to lymphoid, erythroid, mono-
user-defined early cell initiate pseudo-time, which is then iteratively cytic, and classical and plasmacytoid dendritic cell (cDCs and
refined by identifying the shortest distances from waypoints—sets of pDCs, respectively) lineages and megakaryocytes (Fig. 2a,b and
cells sampled to span the differentiation landscape (Supplementary Supplementary Fig. 4b,c)19,20. Hematopoietic stem and progenitor
Fig. 1b-c)1,2. The computed pseudo-time does not represent a single cells composed ~63% of the total sorted cells. Lineage-committed
trajectory, but rather assigns each cell a relative distance from an cells were also detected because of imperfect CD34 purification
initial cell, regardless of its lineage or terminal fates. (~90% pure) and the temporal lag in surface protein levels com-
We use the neighbor graph and pseudo-time to construct pared with messenger RNA.
a Markov chain that models differentiation as a stochastic process,
where a cell reaches one or more terminal states through a series Palantir recapitulates expected hematopoiesis trends. We applied
of steps in the manifold (Fig. 1b). Pseudo-time provides direc- Palantir to the hematopoiesis data, selecting a CD34-high cell as
tionality that is used to orient edges in the neighbor graph in a the start cell (Methods), and analyzed each of the three replicates
manner consistent with the ordering (Supplementary Fig. 1d-e). separately to evaluate robustness. The algorithm correctly identi-
For each directed edge, we assign a transition probability of reach- fied all expected cell types, including monocytes, erythroid cells,
ing a neighboring cell in one step. The probability of reaching megakaryocytes, lymphoid progenitors, and the two dendritic cell
a more distant cell is computed over multiple steps and will be populations, as terminal states (Fig. 2b,c). The pseudo-time order-
high if many paths connect them—that is, there is a high density ing identified by Palantir follows the expected progression from
of observed intermediary cell states (Supplementary Fig. 1f and hematopoietic stem cells (HSCs) to differentiated cell types (Fig. 2c)
Supplementary Note 1). Thus, while each single step is stochas- and cells at the beginning of pseudo-time have the potential to reach
tic, over longer distances, the manifold graph structure implicitly any terminal state, with a gradual loss of plasticity as they commit
encodes developmental trajectories. toward a particular lineage (Fig. 2d,e).
The Markov chain is also used to infer terminal states from the To evaluate the trajectories, we computed the expression trends
data. Palantir identifies terminal states as boundary cells (extrema of key markers (Fig. 2f). As expected, CD34 shows a decreasing
of diffusion components) that are outliers in the stationary distri- trend in all lineages as cells commit11, whereas lineage-specific fac-
bution—that is, the states into which the random walks converge tors such as CD79A, GATA1, and IRF8 are selectively upregulated
(Fig. 1c). Once the terminal states are identified, we convert them in the lymphoid, erythroid, and dendritic cell lineages, respectively.
to absorbing states with no outgoing edges. In an absorbing Markov MPO shows an initial upward trend across all lineages, which is
chain, a random walk from any state will continue until it reaches subsequently maintained only in the monocyte lineage (Fig. 2f).
a terminal absorbing state. For each cell, Palantir then integrates all Finally, CD41 expression is consistent with its role as a marker of
possible random walks from the cell to each possible terminal state early erythroid and megakaryocytic precursors, exhibiting contin-
to yield a vector of branch probabilities (Supplementary Fig. 1f,g). ued upregulation in the megakaryocytic lineages21.
We define a cell’s differentiation potential (DP) to be the entropy We next evaluated Palantir’s robustness and reproducibility. Our
over the branch probabilities, providing a quantitative metric for experiments demonstrate that both pseudo-time and DP are robust
cell plasticity (Fig. 1d and Supplementary Fig. 1h). to a wide range of parameters, including the number of neighbors for
Palantir assigns each cell both a pseudo-time (relative distance graph construction, number of diffusion components, and different
from the start) and branch probabilities to all terminal states. Thus, sampling of waypoints and subsampling of cells (see Supplementary
Palantir’s pseudo-time provides a unified ordering that enables pre- Figs. 5-8 and Methods). Pseudo-time and DP are highly correlated
cise alignment, characterization, and comparison of gene expres- between independent applications of Palantir to datasets from dif-
sion dynamics along all lineages, without having to select cells in ferent bone marrow donors (Supplementary Figs. 9-11), and gene
subsets of lineages (Supplementary Note 1). From this ordering, expression trends are also reproducible across the biological rep-
we compute gene expression trends using generalized additive licates (Supplementary Fig. 11). These findings collectively show
models, weighing each cell’s contribution based on branch proba- that Palantir results are reproducible and suggest that they correctly
bilities (Fig. 1e, Supplementary Fig. 3, and Supplementary Note 2). characterize gene expression dynamics in early hematopoiesis.
452 NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology
NAtuRe BiotecHNology Articles
Ery
HSC
Mega
PLEK
A hierarchical, continuous model of hematopoietic fate choice. model with step-wise losses in potential as stem cells differentiate
A number of single-cell studies4,6 have hypothesized that hema- into specific cell types.
topoietic decision-making is a continuous process, but that it By comparing the change in DP across lineages, we can use Palantir
lacks hierarchy. However, these studies were based on sorted to query human hematopoiesis, where genetic perturbation studies
populations and might have missed intermediate cell stages; are impossible. DP decreases along any given lineage, as cells lose
more importantly, the relative proportions of different cell types their ability to commit to other lineages (Supplementary Fig. 12a-d).
were not retained. On the other hand, lineage-tracing studies of Tracking branch probabilities and DP along pseudo-time enables us
murine hematopoiesis22 support a hierarchical developmental to determine when and in what manner these probabilities change for
BRVLB
Mono
HSC
DCs
FOSL2
ecaps
noisuffid
ni
slleC
noisserpxe
eneG
8FRI
Continuity in cell states and cell fate choices
Myl
HSC
Ery
SPI1
2ATAG
a
Erythroid lineages Myeloid lineages Erythroid-myeloid
HSC
Precursors
CLP
Mono
DCs
Ery
Mega
b c d
(1) (4)
Markov chain Stationary distribution Differentiation potential
(1) (4)
(5)
(2)
(2)
(5)
(6) (7)
Br C(7)
(3) Br B
(3)
Br A (6)
0.00.20.40.60.81.0
e
Gene trends
Br A
Br B
Branch A probabilities Br C
Palantir pseudo-time
eneg
gol
noisserpxe
2 2
1 1
0 0
–1 –1
–2 –2
–3 –3
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
Fig. 1 | Palantir characterizes cell fate choices in a continuous model of differentiation. a, Top: Projection of CD34+ human bone marrow cells along
diffusion components. Bottom: Expression of gene pairs involved in lineage decisions for cells in the corresponding top panel. Cells colored by Phenograph
cluster (Supplementary Fig. 4a); arrows highlight continuity in cell fate choices as a pervasive lack of well-defined branch points in decision-making
regions. Plots show comparison of 3,170, 4,224, and 3,510 cells, respectively. b–d, Palantir phenotypic manifold for a subsampled dataset of CD34+ human
hematopoiesis. Each dot represents a cell embedded into diffusion space based on the first three components and visualized using tSNE. b, Cartoon
of Markov chain construction over the manifold. Cells colored by pseudo-time. c, Cells colored by the stationary distribution of the Markov chain in b,
demonstrating outliers (yellow) in the mature states. Outliers that are also boundary states (circles) are selected as terminal states. d, Cells colored
by differentiation potential (DP). Highlighted examples (circles) show relationship between pseudo-time, DP, and branch probabilities (histogram with
bars colored by terminal state or branch, Br). High DP (1) decreases gradually as cells move toward commitment (2 and 3). Modeling cell fate choices as
probabilities provides a representation of their continuity (4–7). e, Expression of a branch A-specific gene along pseudo-time. Left: Each dot represents a
cell colored by its probability of reaching terminus A. Black line, gene expression trend for this data. Right. Expression trends for the three lineages. The
unified framework of pseudo-time and branch probabilities enables gene expression dynamics to be characterized across a common axis. DC, dendritic
cells; Ery, erythroid cells; Mega, megakaryocytes; Mono, monocytes; Myl, myeloid cells.
NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology 453
Articles NAtuRe BiotecHNology
a CD34+ cells from human bone marrow b Cell type composition c Pseudo-time d Differentiation potential
HSC Precursors Mono DCs Ery Mega HSC
1
Mono CLP 6
2
5
CD34 pDCs 3
7 cDCs Mega 4
Ery
MPO
1 2 3
IRF8
CD79A
1.0
4 5 6 7
GATA1
CD41
Differentiated/ terminal cell types
each terminal fate. Our results suggest continuity in early hematopoi- into different lineages and can detect when cell fate specification
etic lineage commitment: DP remains consistently high throughout changes. We observe points along pseudo-time where substan-
early hematopoiesis, with gradual losses as cells differentiate toward tial changes in DP occur and posit that these changes reflect key
specific lineages (Fig. 3a and Supplementary Fig. 12e). molecular and cellular events driving differentiation. Most of these
Importantly, we note that the rate of change in DP varies greatly changes coincide with commitment to different lineages (Fig. 3a
along pseudo-time and across lineages (Fig. 3a and Supplementary and Supplementary Fig. 12), except for a substantial decrease in DP
Fig. 12e; see also Methods). If lineage commitment was non-hier- in early differentiation (Fig. 3a, early cells) not associated with com-
archical, we would expect DP for different lineages to simultane- mitment toward any specific lineage.
ously drop downward at a particular point along pseudo-time. To gain insight into this drop in DP, we characterized gene expres-
Instead, we observe a sequential commitment to the lymphoid, ery- sion trends in the vicinity of this event. We clustered genes along
throid/megakaryocytic, and, finally, myeloid lineages (Fig. 3a and pseudo-time, assuming that genes involved in coherent biological
Supplementary Fig. 12e), supporting a hierarchical mode of lineage processes share similar expression dynamics, and used gene ontol-
commitment. These results suggest that differentiation in early ogy enrichment to annotate the resulting clusters (Supplementary
human hematopoiesis is hierarchical. Note 3). The strongest trends involved upregulation of aerobic
and mitochondrial respiration, and downregulation of hypoxic
DP identifies hematopoietic differentiation landmarks. DP rep- genes (Fig. 3b, Supplementary Fig. 13b). These data suggest that a
resents a quantitative measure of a cell’s potential to differentiate decrease in DP at the earliest stages of hematopoiesis corresponds
ytilibaborP
e
Branch probabilities
1.0
0.0
0.0
1.0
0.0
noisserpxe
dezilamroN
f
Gene expression trends
CD34 CD79B GATA1
1.0
0.0
Palantir pseudo-time
noisserpxe
dezilamroN
CLP
1.0 1.4
0.8 1.2
0.6 1 0 . . 0 8
0.4 0.6
0.2 0 0 . . 4 2
0.0
HSC
CLP
Ery
Mega
Mono
cDC
pDC
–4 –2 0 2 4 6
0 0.2 0.4 0.6 0.8 0 0.2 0.4 0.6 0.8 0 0.2 0.4 0.6 0.8
IRF8 MPO CD41
0 0.2 0.4 0.6 0.8 0 0.2 0.4 0.6 0.8 0 0.2 0.4 0.6 0.8
Fig. 2 | Differentiation landscape of early human hematopoiesis. Data shown for CD34+ human bone marrow cells, replicate 1. a, MAGIC51-imputed
expression of genes (rows) differentially expressed between PhenoGraph13 clusters (based on MAST52). Cells (columns) are ordered by cluster; top row
represents annotated cluster labels, with color-coding scheme used in all figures. tSNE maps show cells colored by imputed expression of characteristic
cell lineage markers. b–d, tSNE maps of full scRNA-seq dataset generated using one HSC as a start cell; 5,780 cells are shown on the tSNE maps. b, Cells
colored by cluster labels in a, annotated by correlation with bulk sorted populations. c, Cells colored by Palantir pseudo-time. d, Cells colored by Palantir
DP. e, Branch probabilities of example cells circled in d, highlighting early cells (1), lymphoid and erythroid lineages (2 and 3), and monocyte and dendritic
cell lineages (4–7). Bars are colored by cell type as in a. f, Gene expression trends for characteristic lineage genes, plotted as in Supplementary Fig. 3.
454 NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology
NAtuRe BiotecHNology Articles
b
Metabolic switch
2.0
Hypoxic genes
Mitochondrial genes
–2.0
0.0 0.25
with a change in metabolic state, occurring before cells begin to the metabolic switch reproducibly and independently in each of
commit toward lineages (Fig. 3b). the three replicate samples (Fig. 3b and Supplementary Fig. 14). DP
Studies have shown that HSC differentiation requires an exit change is also correlated with expression dynamics of THY1(CD90),
from the slow-cycling, quiescent long-term HSC state to a metaboli- a well-characterized marker of transition between long-term HSCs
cally active short-term HSC state, a process known as the metabolic and short-term HSCs (Supplementary Fig. 13c)24. Moreover, change
switch23. The range of cell types into which a cell can differentiate in DP is also accompanied by increased expression of early myeloid-
is thought to remain unaltered during this transition. Consistent erythroid-lymphoid genes compared with HSC genes (Fig. 3b and
with these studies, we show that the change in DP correlates with Supplementary Fig. 14). These results demonstrate that DP, as
seneg
fo
noisserpxe
naeM
c
Erythroid differentiation
2.0
Early myleoid genes
Early erythroid genes
–2.0
0.0 1.0
2.0 2.0
HSC genes Early myeloid genes
Myl-Ery-Lymph genes Heme metabolism/ Oxygen response
–2.0 –2.0
0.0 0.25 0.0 1.0
Cell bins
Expression trends along erythroid differentiation
TAL1 KLF1 GATA1
noisserpxe
dezilamroN
Change of differentiation potential along pseudo-time
All cells Early cells
d
1.0
Ery branch
probability
0.0
0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8
KLF3 HBB
Ery branch
probability
Palantir pseudo-time
PD
a
1.5 1.40
1.0 1.35
0.5 1.30
0.0 1.25
0.0 0.2 0.4 0.6 0.8 1.0 0.00 0.05 0.10 0.15 0.20 0.25
Palantir pseudo-time Palantir pseudo-time
HSC Precursors CLP Mono cDC pDC Ery Mega
Hematopoietic maturation Erythroid differentiation
DP DP
0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8
Fig. 3 | Palantir DP identifies landmarks of hematopoietic differentiation. Data shown for CD34+ human bone marrow cells, replicate 1. a, DP along
pseudo-time for all cells (left) or early cells (right) decreases as cells commit to lineages. Each dot represents a cell colored by cell type as in Fig. 2b and
at bottom. b, Mean expression of hypoxic and mitochondrial genes (top) and stem cell and mature lineage-specifying genes (bottom) in early cells in
equal-sized bins along Palantir pseudo-time. Box plots show the mean expression and 1.5 s.d. Dotted black line, DP; arrow, point of maximal DP change,
corresponding to cross-over points in gene expression. c, Mean expression of early myeloid and early erythroid genes (top), and early myeloid genes and
genes involved in functional specification of erythroid function (bottom) in early and erythroid-lineage cells. Dotted black line, DP; arrow, point of maximal
DP change, corresponding to point of higher erythroid gene expression. d, Gene expression trends (blue) of key erythroid transcription factors TAL1, KLF1,
and GATA1 are the most correlated with erythroid branch probability (dotted black line). Gene expression of downstream regulators KLF3 and HBB is also
shown. Shaded region represents 1 s.d.
NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology 455
Articles NAtuRe BiotecHNology
a b
TF expression along erythroid lineage
PU.1
0.0
GATA1 Erythroids
Monocytes
cDC
pDC
c
GATA2
Palantir pseudo-time
computed by Palantir strictly from the data, can identify key dif- with no previous knowledge, and expression trends of known key
ferentiation events such as metabolic switch even when these are regulators of erythropoiesis.
unrelated to specific cell fate choices. The high-resolution ordering of Palantir allows us to character-
ize the order and timing of events during erythropoiesis. We find
DP during erythroid commitment. We next characterized DP that upregulation of KLF1 is followed by upregulation of KLF3, a
changes during lineage commitment using erythropoiesis as a case known target of KLF1 that stabilizes the erythroid program (Fig.
study. Erythrocytes are derived from megakaryocyte-erythroid 3d and Supplementary Fig. 13e (Cluster 6))29, and that globin genes
precursor cells25. On erythroid commitment, we observe a sharp such as HBB are upregulated in the final wave, conferring functional
decrease in DP (Fig. 3a). To identify processes concordant with identity to red blood cells (Fig. 3d and Supplementary Fig. 13e
this decrease, we repeated the pseudo-temporal trend-based gene (Cluster 8)). These results strongly suggest that erythroid specifica-
set analysis as before (Supplementary Fig. 13d). Gene expression tion occurs in stages of coordinated gene upregulation.
trends in cells undergoing erythroid lineage commitment (increas-
ing branch probability toward erythroid fate) are associated with Transcriptional regulation of erythroid commitment. Given the
continued upregulation of early erythroid genes and a downregu- strong correspondence between key erythroid transcription factor
lation of early myeloid genes (Fig. 3c). As expected for maturing expression and erythroid branch probability, we next sought to use
red blood cells, decrease in DP also coincides with upregulation of Palantir to identify factors that influence lineage fate choices. We
heme metabolism and oxygen response genes (Fig. 3c). reasoned that such transcription factors should be expressed before
We reasoned that the transcription factors most closely cor- the lineage decision, should be upregulated during early specifica-
related with erythroid branch probabilities are likely to be key tion and correlate with increasing lineage probability, and should
regulators of erythroid commitment. Hence, we systematically also be downregulated in alternate lineages.
correlated all transcription factors with erythroid branch prob- Upon a systematic evaluation of all transcription factors
ability and found the most correlated transcription factors to be expressed in the erythroid lineage (Supplementary Note 4), we
TAL1, KLF1, and GATA1 (Pearson correlation > 0.99) (Fig. 3d and identified GATA2, LYL1, and MXD4 as best satisfying our criteria of
Supplementary Fig. 13e (Cluster 0)). Each has been shown to play a high expression in precursor cells and strong correlation with ery-
central role in erythropoiesis: TAL1 enhances erythroid potential26; throid commitment (Supplementary Fig. 15a,b). GATA2 shows the
KLF1 regulates early erythroid precursor genes and suppresses highest expression and correlation (Supplementary Fig. 15b). The
the megakaryocyte lineage27; and loss of GATA1 leads to complete interplay between GATA1, GATA2, and PU.1 (SPI1) has been pro-
loss of erythropoiesis28. Thus, we find remarkable correspondence posed to drive the myeloid-versus-erythroid lineage decision30, with
between erythroid branch probability, computed based on all genes mutual antagonization between PU.1 and GATA1 driving myeloid
noisserpxe
dezilamroN
Sorted bulk ATAC-seq sc RNA-seq
1.0
Genes
1.0
0.0
1.0
0.0
0.0 0.2 0.4 0.6 0.8 1.0
slleC
0.3 0.2
0.1 0.0
–0.1
–0.2 0.15 0 0 .170 5 .20 0 0 .220 5 .25 0 0 .270 5 .30 0 0 .325 0.350
TF binding signal
tegrat
llec-elgniS
noisserpxe
Target expression correlation
Single-cell TF activities
TF activities
slleC
Inference of TF activity
TF expression ratios and activity differences
PU.1/GATA2 TF expression ratios
TF activity differences
DP along erythroid
lineage
ytivitca/noisserpxE
ecnereffid
1.0
–1.0
0.0 0.2 0.4 0.6 0.8
Palantir pseudo-time
Fig. 4 | transcriptional regulation of erythroid differentiation. Data shown are for CD34+ human bone marrow cells, replicate 1 (5,708 cells). a, Gene
expression trends for PU.1, GATA1, and GATA2 in the myeloid and erythroid lineages. Trends are colored based on lineage, as in Fig. 2b. Shaded region
represents 1 s.d. b, Single-cell transcription factor activity inference using scRNA-seq data and ATAC-seq data from bulk sorted populations. ATAC-
seq data are used to identify cell type-specific transcription factor targets, and transcription factor activity in each cell is inferred by measuring the
correlation between predicted transcription factor sequence affinity of the targets and their expression. c, PU.1/GATA2 expression ratio and PU.1/GATA2
transcription factor activity difference (colored trends) strongly correlate with DP (black) change along erythroid lineage. Shaded regions represent 1 s.d.
TF, transcription factor.
456 NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology
NAtuRe BiotecHNology Articles
a Cell type composition b Pseudo-time ordering 1.0 c DP.
1.4
Mono
Neutro 0.8 1.2
Baso
1.0
Mega 0.6
Ery 0.8
Ery 0.4 0.6
MEP
Precusors 0.4
Precusors 0.2
0.2
0.0
d DP trends e Gene expression trends
Mpo Klf1
1
0
0.0 0.6 0.0 1.0 0.0 1.0
Palantir pseudo-time Palantir pseudo-time
and erythroid lineage commitments respectively30,31. More recently, of expression tilts toward GATA2 dominance. Indeed, the ratio of
GATA2 rather than GATA1 has been proposed to be the agonist PU.1 to GATA2 is correlated with DP change along the erythroid
of PU.132,33, consistent with Palantir identification of GATA2 as a lineage (Fig. 4c).
potential driver of erythroid commitment. To explore this further, we characterized the behavior of PU.1 and
Previous studies have shown that expression ratios between com- GATA2 target genes along the erythroid lineage. Measuring the con-
peting transcription factor pairs can be critical determinants of lin- cordant behavior of multiple target genes not only mitigates individ-
eage specification31,34. While average GATA2 levels remain relatively ual gene measurement noise, but also provides a functional readout
constant during early hematopoiesis (Supplementary Fig. 15c), we of transcription factor activity. We leveraged published bulk ATAC-
observe that a decrease in the ratio of PU.1 to GATA2 precedes the seq data10 from sorted erythroid and GMP cells for GATA2 and PU.1
drop in DP (Supplementary Fig. 15d), suggesting that gene expres- targets, respectively, to determine transcription factor activities at the
sion programs conferring erythroid fate are initiated as the balance single-cell level (Fig. 4b, Supplementary Fig. 15e, and Supplementary
noisserpxE 1
0
.PD
Mouse hematopoeisis
Mono Neutro Baso Mega Ery
f Cell type composition g Pseudo-time ordering h Differentiation potential
1.0
1.2
0.8
1.0
0.6 0.8
0.4 0.6
0.4
0.2
0.2
0.0
i DP. trends j Gene expression trends
30 Clca1 Car1
0
0.0 1.0 0.0 1.0 0.0 1.0
Palantir pseudo-time Palantir pseudo-time
noisserpxE
1.2
0.0
.PD
Mouse colon differentiation
Stem
Reg4+ Goblet
Goblet
Goblet pre
Colonocytes
Tuft
6
0
Reg4+ goblet Goblet Tuft Colonocytes
Fig. 5 | Palantir generalizes to mouse hematopoiesis and colon differentiation datasets. a, tSNE map of mouse hematopoiesis data generated by scRNA-
seq of sorted precursor populations6 lacking a well-defined stem cell population. Cells are colored by clusters generated in ref. 6; 2,700 cells are shown on
the tSNE maps. b,c, Palantir pseudo-time (b) and DP (c), generated after selecting an early cell for initiation. d, DP trends along pseudo-time, highlighting
the hierarchical nature of murine hematopoiesis (commitment toward erythroid lineage followed by commitment toward the myeloid lineages). Trends are
colored by clusters as in a. e, Expression trends of myeloid factor Mpo and erythroid factor Klf1 recapitulate expected behavior and are consistent with their
dynamics in human hematopoiesis. f, tSNE map of scRNA-seq dataset of epithelial enriched cells from the mouse colon35. Cells are colored by Phenograph
clusters; 1,811 cells are shown on the tSNE maps. g,h, Palantir pseudo-time (g) and DP (h) generated using an Lgr5+ stem cell as the start cell and manually
setting the tuft cells as one of the terminal states. i, DP trends recapitulate known hierarchy of lineage specification (colonocytes followed by goblet cell
populations). Trends colored by cluster as in f. j, Expression trends of Clca1 and Car1 across lineages. Goblet pre, goblet cell precursors.
NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology 457
Articles NAtuRe BiotecHNology
Note 5). In line with the expression ratios, the change in PU.1 and hematopoiesis, a well-studied system with scientific consensus
GATA activity difference precedes the change in DP (Supplementary on ground truth benchmarks (Supplementary Figs. 17–22 and
Fig. 15d) and is also strongly correlated with the decrease in DP Supplementary Note 6). In particular, we assessed their ability to iden-
along the erythroid lineage (Fig. 4c and Supplementary Fig. 15f-g). tify low-frequency lineages such as megakaryocytes, cDCs, and pDCs
Together, these results provide in vivo evidence that GATA2, rather and recover the expression trends of key genes such as CD34 (ref. 11),
than GATA1, functions as a mutual agonist of PU.1 to achieve ery- MPO (ref. 38), CD79B (ref. 39), GATA1 (ref. 28), CSF1R (ref. 40),
throid specification during human hematopoiesis. and CD41 (ref. 21). We also compared the nature of the outputs gen-
erated and the amount of previous biological knowledge needed
Analysis of mouse hematopoiesis and colon differentiation. as input to each algorithm. Palantir requires the least amount of a
Palantir is ideally suited for our CD34+ human hematopoiesis data- priori biological information (start cell) and provides both pseudo-
set, which is heavily enriched for multipotent precursors and pro- time and cell fate probabilities as output (Supplementary Fig. 17a).
vides sufficient early cells for fine resolution mapping of lineage fate However, PAGA is the only algorithm that allows a general topo-
decisions. To test Palantir on more challenging data with a paucity logical structure.
of early cells and potential bias induced by cell sorting, we selected Palantir outperforms the other algorithms (Supplementary
a mouse hematopoiesis dataset that profiled Lin−c-Kit+Sca-1+ Fig. 17b) by distinguishing the two dendritic cell populations,
cells using MARS-seq2 (ref. 6). This study sorted cells for differ- identifying megakaryocytic cells as separate from the erythroid
ent myeloid and erythroid precursor populations, but excluded the lineage (Fig. 2e and Supplementary Fig. 6), and accurately recov-
most multipotent stem cells, creating a challenge to correctly resolve ering the expression dynamics of key lineage genes (Fig. 2f;
branch probabilities. see also Supplementary Note 6 for details of the evaluations).
Even with a paucity of early cells (Fig. 5a), Palantir was able to Monocle 2 (ref. 17) and FateID37 (using RaceID clustering) fail to
correctly identify terminal states and estimate pseudo-time and DP generate a coherent map of hematopoiesis (Supplementary Figs.
characterizing mouse hematopoiesis (Fig. 5b,c and Supplementary 18 and 21). PAGA41 and DPT3 identify the major lineages, but
Fig. 16a; see also Methods). The small number of multipotent cells are unable to identify rarer lineages and lose resolution in gene
does appear to affect accuracy and resolution in early hematopoi- expression trends (Supplementary Fig. 19). Slingshot8 identifies
esis, as the peak DP is not located at the start of the pseudo-time the major lineages but not rare populations, resulting in incorrect
ordering (Fig. 5d). Despite these limitations, we observe a clear gene expression dynamics (Supplementary Fig. 20), and it does
hierarchical structure in lineage specification, consistent with not provide a unified framework for comparing expression trends
recent lineage-tracing experiments22. The hierarchical structure is across lineages8. FateID37 using Palantir’s preprocessing and clus-
similar to human hematopoiesis, with commitment to erythroid tering is still largely incorrect for most cell fate probabilities and,
lineage followed by specification of the different myeloid lineages critically, includes all early cells in the lymphoid lineage, lead-
(Fig. 5d). In further support of the Palantir model, the expression ing to mischaracterized expression dynamics (Supplementary
of key erythroid and myeloid genes Mpo and Klf1 is consistent with Fig. 21). Finally, while individual diffusion components have
their roles in their respective lineages (Fig. 5e)27 and their patterns been used to model differentiation trajectories15,42, in the CD34+
in human hematopoiesis (Figs. 2f and 3d). human bone marrow data they can only be used to infer order-
To test whether Palantir generalizes beyond hematopoietic data- ing in lymphoid and monocyte lineages (Supplementary Fig. 22).
sets, we applied it to a mouse colon differentiation dataset gener- Notably, none of the algorithms discussed above explicitly model
ated using the InDrop platform35. Lgr5+ stem cells were shown to and quantify the plasticity and branch probabilities along the dif-
differentiate to colonocytes, tuft cells, goblet cells, and Reg4+ gob- ferentiation landscape. Taken together, only Palantir could accu-
let cells (Fig. 5f). Palantir automatically identified the two goblet rately associate expression changes in key transcription factors
populations and colonocytes as terminal states but failed to identify with changes in commitment to the lineages these regulate.
tuft cells as a terminal state since this population is not completely
mature and is situated closer to Lgr5+ cells (Fig. 5f,g). By manu- Discussion
ally setting tuft cells as one of the terminal states, Palantir correctly Unlike existing algorithms, Palantir generates a probabilistic
identified the pseudo-time ordering, hierarchical relationships, and model of cell fate choice as a continuous process. Palantir is robust
order of lineage commitment in mouse colon differentiation (Fig. to parameters, reproducible across replicates, and generalizes to
5g-i and Supplementary Fig 16b)36. Palantir also recovers expected diverse datasets. Palantir’s high-resolution mapping of cells along
gene expression trends: Clca1 is specifically upregulated in goblet differentiation trajectories allowed us to characterize the order and
cells, Car1 first increases and then drops slightly in colonocytes, timing of regulatory factors that drive lineage choices in hematopoi-
Muc2 shows strongest induction in Reg4+ goblet cells, and Lgr5 is esis. Our findings clarified that DP drops gradually during the pro-
downregulated across all lineages (Fig. 5j and Supplementary Fig. gression from stem to differentiated cells and is hierarchical, such
16c)35. Branch probability changes and expression trends along lin- that cells are predisposed sequentially toward lymphoid, erythroid,
eages other than tuft were not substantially altered when tuft cells and finally myeloid lineages (potential drops gradually within
were not set as a terminal state (correlation: 0.98; Supplementary each lineage).
Fig. 16d), demonstrating that Palantir is robust to missing popula- The key to Palantir’s high resolution in pseudo-time is the use
tions and mislabeled cells. of multiple diffusion components and neighbor graphs to measure
distances between cells in this embedded space (Supplementary
Comparison with trajectory inference algorithms. While signifi- Fig. 23a-c). This enables Markov chain construction, which is cen-
cant advances have been made for resolving the ordering of cells, tral to both terminal state identification and modeling continuities
state-of-the-art pseudo-time algorithms continue to model dif- in lineage choices. Palantir outperforms other pseudo-time algo-
ferentiation as a series of discrete, deterministic bifurcations, pre- rithms, which largely treat lineage choices as discrete bifurcations,
dominantly approximated by clustering the data7,8. We compared in recovering biologically consistent gene expression trends and
Palantir with leading and widely used pseudo-time algorithms such lineage relationships. Enrichment of stem and precursor cells from
as Monocle2 (ref. 17), Partition-Based Graph Abstraction (PAGA)7, bone marrow was necessary to characterize lineage choices in early
Diffusion Pseudotime (DPT)3, Slingshot8, and FateID37. human hematopoiesis at high resolution. However, Palantir can
We evaluated the algorithms based on their ability to identify robustly recover expression trends in datasets for which precursors
lineages and recover known gene expression trends in human are not enriched.
458 NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology
NAtuRe BiotecHNology Articles
We anticipate that Palantir will be a valuable discovery tool for 14. Coifman, R. R. et al. Geometric diffusions as a tool for harmonic analysis and
many less-characterized systems, including those profiled by the structure definition of data: diffusion maps. Proc. Natl Acad. Sci. USA 102,
7426–7431 (2005).
Human Cell Atlas Project43. A key requisite is the presence of the
15. Haber, A. L. et al. A single-cell survey of the small intestinal epithelium.
full range of differentiating cells, made possible by the asynchro- Nature 551, 333–339 (2017).
nous nature of differentiation in tissues such as bone marrow, 16. Hastie, T. J. & Tibshirani, R. J. Generalized Additive Models (Chapman &
colon, and olfactory epithelium8,18,35. We note that this is not a fea- Hall/CRC, 1990).
ture of embryogenesis, which is typically studied using time course 17. Qiu, X. et al. Reversed graph embedding resolves complex single-cell
trajectories. Nat. Methods 14, 979–982 (2017).
experiments42,44. Time course data require explicit modeling of con-
18. Dahlin, J. S. et al. A single-cell hematopoietic landscape resolves 8 lineage
nectivity between time points and corrections for confounding by trajectories and defects in Kit mutant mice. Blood 131, e1–e11 (2018).
batch effects. 19. Azizi, E. et al. Single-cell map of diverse immune phenotypes in the breast
The most important assumption made by pseudo-time algo- tumor microenvironment. Cell 174, 1293–1308.e36 (2018).
20. Novershtern, N. et al. Densely interconnected transcriptional circuits control
rithms, including Palantir, is that differentiation is unidirectional
cell states in human hematopoiesis. Cell 144, 296–309 (2011).
and proceeds toward functionally mature cells. While this is reason-
21. Psaila, B. et al. Single-cell profiling of human megakaryocyte-erythroid
able for healthy differentiation, the assumption is violated in systems progenitors identifies distinct megakaryocyte and erythroid differentiation
such as tissue regeneration45 and cancer46. If cells dedifferentiate or pathways. Genome Biol. 17, 83 (2016).
trans-differentiate to earlier transcriptional states, scRNA-seq data 22. Pei, W. et al. Polylox barcoding reveals haematopoietic stem cell fates realized
in vivo. Nature 548, 456–460 (2017).
alone will be insufficient to distinguish these populations and their
23. Takubo, K. et al. Regulation of glycolysis by Pdk functions as a metabolic
differentiation paths. In vivo lineage-tracing technologies can pro-
checkpoint for cell cycle quiescence in hematopoietic stem cells. Cell Stem
vide ground truth for lineage relationships47,48 but require genetic Cell 12, 49–61 (2013).
modification, and hence are unsuitable to study cancer progression, 24. Majeti, R., Park, C. Y. & Weissman, I. L. Identification of a hierarchy of
metastasis, and healthy development in human tissues. As an alter- multipotent hematopoietic progenitors in human cord blood. Cell Stem Cell 1,
635–645 (2007).
native, mutations occur rapidly in most cancers and can provide a
25. Mori, Y. et al. Identification of the human eosinophil lineage-committed
source of directionality and lineage information in human systems.
progenitor: revision of phenotypic definition of the human common myeloid
Recent studies49 have demonstrated that somatic mutations occur progenitor. J. Exp. Med. 206, 183–193 (2009).
at a rate that enables lineage tracing even in healthy human tissues. 26. Ravet, E. et al. Characterization of DNA-binding-dependent and
The ability to simultaneously profile the transcriptome and DNA50 -independent functions of SCL/TAL1 during human erythropoiesis. Blood
103, 3326–3335 (2004).
has great potential to elucidate disease initiation and progression by
27. Siatecka, M. & Bieker, J. J. The multifunctional role of EKLF/KLF1 during
extending Palantir to incorporate lineage information to model cell erythropoiesis. Blood 118, 2044–2054 (2011).
fate decisions. 28. Ferreira, R., Ohneda, K., Yamamoto, M. & Philipsen, S. GATA1 function,
a paradigm for transcription factors in hematopoiesis. Mol. Cell. Biol. 25,
online content 1215–1227 (2005).
29. Funnell, A. P. et al. Erythroid Kruppel-like factor directly activates
Any methods, additional references, Nature Research reporting
the basic Kruppel-like factor gene in erythroid cells. Mol. Cell. Biol. 27,
summaries, source data, statements of data availability and asso- 2777–2790 (2007).
ciated accession codes are available at https://doi.org/10.1038/ 30. Nerlov, C., Querfurth, E., Kulessa, H. & Graf, T. GATA-1 interacts with the
s41587-019-0068-4. myeloid PU.1 transcription factor and represses PU.1-dependent
transcription. Blood 95, 2543–2551 (2000).
31. Zhang, P. et al. PU.1 inhibits GATA-1 function and erythroid differentiation
Received: 5 August 2018; Accepted: 11 February 2019;
by blocking GATA-1 DNA binding. Blood 96, 2641–2648 (2000).
Published online: 21 March 2019
32. May, G. et al. Dynamic analysis of gene expression and genome-wide
transcription factor binding during lineage specification of multipotent
References
progenitors. Cell Stem Cell 13, 754–768 (2013).
1. Bendall, S. C. et al. Single-cell trajectory detection uncovers progression 33. Tusi, B. K. et al. Population snapshots predict early haematopoietic and
and regulatory coordination in human B cell development. Cell 157, erythroid hierarchies. Nature 555, 54–60 (2018).
714–725 (2014). 34. Antebi, Y. E. et al. Mapping differentiation under mixed culture conditions
2. Setty, M. et al. Wishbone identifies bifurcating developmental trajectories reveals a tunable continuum of T cell fates. PLoS Biol. 11, e1001616 (2013).
from single-cell data. Nat. Biotechnol. 34, 637–645 (2016). 35. Herring, C. A. et al. Unsupervised trajectory analysis of single-cell RNA-seq
3. Haghverdi, L., Buttner, M., Wolf, F. A., Buettner, F. & Theis, F. J. Diffusion and imaging data reveals alternative tuft cell origins in the gut. Cell Syst. 6,
pseudotime robustly reconstructs lineage branching. Nat. Methods 13, 37–51 e39 (2018).
845–848 (2016). 36. Li, H. & Jasper, H. Gastrointestinal stem cells in health and disease: from flies
4. Velten, L. et al. Human haematopoietic stem cell lineage commitment is to humans. Dis. Model Mech. 9, 487–499 (2016).
a continuous process. Nat. Cell Biol. 19, 271–281 (2017). 37. Herman, J. S., Sagar & Grun, D. FateID infers cell fate bias in multipotent
5. Buenrostro, J. D. et al. Integrated single-cell analysis maps the continuous progenitors from single-cell RNA-seq data. Nat. Methods 15, 379–386 (2018).
regulatory landscape of human hematopoietic differentiation. Cell 173, 38. Yang, J., Zhang, L., Yu, C., Yang, X. F. & Wang, H. Monocyte and macrophage
1535–1548 e1516 (2018). differentiation: circulation inflammatory monocyte as biomarker for
6. Paul, F. et al. Transcriptional heterogeneity and lineage commitment in inflammatory diseases. Biomark. Res. 2, 1 (2014).
myeloid progenitors. Cell 163, 1663–1677 (2015). 39. Benschop, R. J. & Cambier, J. C. B cell development: signal transduction
7. Plass, M. et al. Cell type atlas and lineage tree of a whole complex animal by by antigen receptors and their surrogates. Curr. Opin. Immunol. 11,
single-cell transcriptomics. Science 360, eaaq1723 (2018). 143–151 (1999).
8. Street, K. et al. Slingshot: cell lineage and pseudotime inference for single-cell 40. Merad, M., Sathe, P., Helft, J., Miller, J. & Mortha, A. The dendritic cell lineage:
transcriptomics. BMC Genomics 19, 477 (2018). ontogeny and function of dendritic cells and their subsets in the steady state
9. Stergachis, A. B. et al. Developmental fate and cellular maturity encoded in and the inflamed setting. Annu. Rev. Immunol. 31, 563–604 (2013).
human regulatory DNA landscapes. Cell 154, 888–903 (2013). 41. Hoppe, P. S. et al. Early myeloid lineage choice is not initiated by random
10. Corces, M. R. et al. Lineage-specific and single-cell chromatin accessibility PU.1 to GATA1 protein ratios. Nature 535, 299–302 (2016).
charts human hematopoiesis and leukemia evolution. Nat. Genet. 48, 42. Ibarra-Soria, X. et al. Defining murine organogenesis at single-cell resolution
1193–1203 (2016). reveals a role for the leukotriene pathway in regulating blood progenitor
11. Orkin, S. H. & Zon, L. I. Hematopoiesis: an evolving paradigm for stem formation. Nat. Cell Biol. 20, 127–134 (2018).
cell biology. Cell 132, 631–644 (2008). 43. Regev, A. et al. The human cell atlas. Elife 6, e27041 (2017).
12. Amir el, A. D. et al. viSNE enables visualization of high dimensional 44. Farrell, J. A. et al. Single-cell reconstruction of developmental trajectories
single-cell data and reveals phenotypic heterogeneity of leukemia. during zebrafish embryogenesis. Science 360, 981–987 (2018).
Nat. Biotechnol. 31, 545–552 (2013). 45. Kotton, D. N. & Morrisey, E. E. Lung regeneration: mechanisms, applications
13. Levine, J. H. et al. Data-driven phenotypic dissection of AML reveals and emerging stem cell populations. Nat. Med. 20, 822–832 (2014).
progenitor-like cells that correlate with prognosis. Cell 162, 46. Beck, B. & Blanpain, C. Unravelling cancer stem cell potential. Nat. Rev.
184–197 (2015). Cancer 13, 727–738 (2013).
NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology 459
Articles NAtuRe BiotecHNology
47. Raj, B. et al. Simultaneous single-cell profiling of lineages and cell types in the Author contributions
vertebrate brain. Nat. Biotechnol. 36, 442–450 (2018). M.S. and D.P. conceived the study, designed and developed Palantir, developed additional
48. Spanjaard, B. et al. Simultaneous lineage tracing and cell-type analysis methods, analyzed the data, and wrote the manuscript. M.S. implemented Palantir
identification using CRISPR–Cas9-induced genetic scars. Nat. Biotechnol. 36, and all other analysis methods. V.K. and L.M. designed, optimized, and executed all single-
469–473 (2018). cell RNA-seq experiments. J.L. and D.P. developed an early theory on application of Markov
49. Biezuner, T. et al. A generic, cost-effective, and scalable cell lineage analysis chains to single-cell data. M.S. and A.G. developed trend-based clustering analysis.
platform. Genome Res. 26, 1588–1599 (2016).
50. Macaulay, I. C. et al. G&T-seq: parallel sequencing of single-cell genomes and Competing interests
transcriptomes. Nat. Methods 12, 519–522 (2015).
51. van Dijk, D. et al. Recovering gene interactions from single-cell data using The authors declare no competing interests.
data diffusion. Cell 174, 716–729.e27 (2018).
52. Finak, G. et al. MAST: a flexible statistical framework for assessing
transcriptional changes and characterizing heterogeneity in single-cell RNA Additional information
sequencing data. Genome Biol. 16, 278 (2015).
Supplementary information is available for this paper at https://doi.org/10.1038/
s41587-019-0068-4.
Acknowledgements
Reprints and permissions information is available at www.nature.com/reprints.
We thank R. Sharma for valuable conversations related to this manuscript, C. Trasande
Correspondence and requests for materials should be addressed to D.P.
and T. Nawy for helping to write the manuscript, and E. Azizi, C. Burdziak, and K.
Hadjantonakis for valuable comments. This study was supported by NIH grants nos. Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in
NIH DP1-HD084071 and NIH R01CA164729, Cancer Center Support Grant no. P30 published maps and institutional affiliations.
CA008748, and the Gerry Center for Metastasis and Tumor Ecosystems. © The Author(s), under exclusive licence to Springer Nature America, Inc. 2019
460 NAtuRe BioteChNoLoGy | VOL 37 | APRIL 2019 | 451–460 | www.nature.com/naturebiotechnology
NAtuRe BiotecHNology Articles
Methods This scaling is equivalent to estimating diffusion distances from 1, 2, … ∞
scRNA-seq of CD34+ human bone marrow cells. Cryopreserved bone marrow steps. See section ‘Measuring distances between cells using multi-scale distance’
stem/progenitor CD34+ cells from healthy donors were purchased from AllCells, under the Palantir algorithm description for details on scaling and its impact
LLC. (catalog no. ABM022F) and stored in vapor phase nitrogen until use. Typical on the representation. The number of components was chosen based on the
for scRNA-seq, a vial was removed from the storage and immediately thawed at eigengap of the eigenvalue decomposition of the diffusion operator. The set of
37 °C in a water bath for 2–3 min. Next, vial content (1 ml) was transferred to a 50- diffusion components is the same set used for running Palantir. Using diffusion
ml conical tube. To prevent osmotic lysis and ensure gradual loss of cryoprotectant, components as inputs led to maps more representative of differentiation when
1 ml of warm medium (IMDM with 10% FBS supplement) was added dropwise, compared with the maps generated on principal components or force-directed
while gently shaking the tube. Then, the cell suspension was serially diluted 5 graphs (Supplementary Fig. 25). We found that force-directed graphs represent
times with 1:1 volume additions of complete growth medium with 2-min wait the distinct mature populations better and provide less resolution in the regions of
between additions. The final ~32-ml volume of cell suspension was pelleted at manifold where lineage decisions are being made. An example of generating tSNE
300g for 5 min. After removing supernatant, cells were washed twice in ice-cold maps using diffusion components is available at http://nbviewer.jupyter.org/github/
1× PBS with 0.04% (wt/vol) BSA supplement to remove traces of medium. Cell dpeerlab/Palantir/blob/master/notebooks/Palantir_sample_notebook.ipynb
concentration and viability were determined with a Countess II automatic cell
counter employing the trypan blue staining method. Differential expression of genes. Differentially expressed genes between clusters
scRNA-seq was performed with 10X genomics system using Chromium were determined using MAST52. MAST was run using default parameters with
Single Cell 3’ Library and Gel Bead Kit V2 (catalog no. 120234). Briefly, 8,700 normalized counts (without log transform) as the input. Genes with FDR (false
cells (viability 90–97%) were loaded per reaction, targeting recovery of 5,000 cells discovery rate)-corrected P value <1 × 10−2 and absolute log(fold change) > 1.25
with 3.9% multiplet rate. After reverse transcription reaction emulsions were were considered significantly different.
broken, barcoded complementary DNA was purified with DynaBeads, followed
by 12 cycles of PCR amplification. The resulting amplified cDNA was sufficient Subsampled data used for figure generation. A dataset for Fig. 1 was generated
to construct next-generation sequencing libraries, which were sequenced on an using the human CD34+ hematopoiesis dataset by waypoint sampling of cells from
Illumina HiSeq 2500 system (HiSeq SBS V4 chemistry kit). erythroid and myeloid lineages (clusters 0, 1, 2, 3, 4, 6, 7, 8; Supplementary Fig. 4a).
A tSNE map was generated as described in ‘scRNA-seq data preprocessing’ and the
scRNA-seq data processing. Data preprocessing. Data derived from each replicate were projection of stem cells was manually adjusted for cleaner visualization.
processed independently. scRNA-seq data were preprocessed using the SEQC pipeline19
using hg38 human genome and the default SEQC parameters for 10X to obtain the Application of Palantir to CD34+ cells. Palantir was applied to each replicate
molecule count matrix. The SEQC pipeline aligns the reads to the genome, corrects separately using 1,200 waypoints and 1 of the CD34+ cells as the start cell. The
barcode and unique molecular identifier (UMI) errors, resolves multi-mapping reads, parameter k was set to 10% of the total number of cells in the data. The results,
and generates a molecule count matrix19. SEQC also performs a number of filtering however, are stable to the choice of k (Supplementary Fig. 6). The number of diffusion
steps: (1) Identification of true cells from cumulative distribution of molecule counts components was chosen based on the eigengap of the eigenvector decomposition
per barcode, (2) removal of apoptotic cells identified at cells with >20% of molecules of the diffusion operator. The results are stable to the choice of number of diffusion
derived from the mitochondria, and (3) removal of low-complexity cells identified as components and the choice of waypoints (Supplementary Fig. 7).
cells where the detected molecules are aligned to a small subset of genes19. In addition,
cells with less than 1,000 molecules detected were filtered out. Finally, genes that were Robustness of Palantir results to parameters. Palantir has the following
detected in at least ten cells were retained for downstream analysis. The retained cells parameters or variables: (1) k, number of neighbors for constructing the
have a median molecule count of ~3,200 and median gene count of ~1,800, indicating nearest-neighbor graph, (2) waypoint sampling (random waypoints selected),
the high quality of the data (Supplementary Fig. 24). and (3) number of diffusion components, which by default is determined based
The filtered count matrix was normalized by dividing the counts of each cell by on the eigengap. We systematically evaluated the robustness of Palantir using
the total molecule counts detected in that particular cell. The normalized matrix data from replicate 1 of the CD34+ bone marrow data (Supplementary
was multiplied by the median of total molecules across cells to avoid numerical Figs. 5-8). The same start cell was used across all runs. Palantir was run with
issues53. Normalized data were log transformed with a pseudo-count of 0.1. different parameters and the robustness of the results was measured using the
following criteria:
Cell cycle correction. Expression of cell cycle genes can confound the ordering of
cells in a differentiation trajectory, and hence we applied f-scLVM54,55 to factor (1) Pearson correlation of pseudo-time, DP, and branch probabilities for the dif-
out the cell cycle effect across all cells. Normalized and log-transformed data were ferent branches between a given pair of Palantir runs.
used as input to f-scLVM correction with default parameters. The following gene (2) Pearson correlation of pseudo-time, DP, and branch probabilities for a subset
ontology annotations were used to annotate the cell cycle effect: GO:0000279 M of cells sampled from the middle of the differentiation process (Supplemen-
phase, GO:0006260 DNA replication, GO:0007059 chromosome segregation, tary Fig. 4, Cluster 1). The lymphoid lineage was excluded from this analysis
GO:0000087 M phase of mitotic cell cycle, and GO:0048285 organelle fission. since cells of Cluster 1 have differentiated away from this lineage.
Following cell cycle correction, principal component analysis was performed
keeping the top 300 components, and diffusion maps were computed using Robustness to waypoint sampling. Robustness to waypoint sampling was tested by
the principal components as input14. See Supplementary Note 1 for details on fixing k and the number of diffusion components (Supplementary Fig. 5). The
constructing the diffusion maps. correlations of pseudo-time, DP, and branch probabilities for all branches, for all
cells, are shown in Supplementary Fig. 5a,b. All of the correlations comparing
Annotation of cell types and filtering of mature populations. Gene expression between runs are >0.98. A subset of cells sampled from the middle of the
profiles from sorted bulk hematopoietic populations were used to annotate the cell differentiation process is shown in Supplementary Fig. 5c with the corresponding
types19,20. Cell cycle corrected data were clustered with Phenograph13 using default pseudo-time, DP, and branch probability correlations shown in Supplementary
parameters and the top 300 principal components as inputs. Cluster centroids were Fig. 5c,d. Pseudo-time ordering correlations are all >0.97. DP correlations range
determined for each cluster and the expression of each gene was standardized. between 0.85 and 0.95, with 75% of correlations >0.9 (Supplementary Fig.
Bulk expression data were downloaded from the Dmap portal (http://portals. 5c). Branch probability correlations range between 0.85 and 0.95, with 90% of
broadinstitute.org/dmap/home) and expression of each cell type was standardized. correlations >0.9 (Supplementary Fig. 5d).
For each cluster, average correlation across bulk replicates was computed for each
cell type and the cell type with the highest correlation was used to annotate the
Robustness to k, the number of neighbors for k-nearest neighbor graph construction.
cluster (Supplementary Fig. 4c). Note, the inferred cell types are used only for
Robustness to k was tested by fixing the number of diffusion components,
interpretation and not used by Palantir.
waypoints, and terminal states (Supplementary Fig. 6). The correlations of
To limit the data to cell types undergoing differentiation in the bone marrow,
pseudo-time, DP, and branch probabilities for all branches for all cells are shown
clusters that were annotated as T cells and mature granulocytes were filtered out.
in Supplementary Fig. 6a, b. All of the correlations comparing between runs are
T cells were filtered out because these migrate from the periphery and do not
>0.97. A subset of cells sampled from the middle of the differentiation process is
differentiate in the bone marrow. Mature granulocytes were filtered out since no
shown in Supplementary Fig. 6c, with the corresponding pseudo-time, DP, and
coherent precursor population was identified in the data.
branch probability correlations shown in Supplementary Fig. 6c,d. Pseudo-time
ordering correlations are all >0.97. DP correlations are all >0.9 (Supplementary
tSNE (t-distributed stochastic neighbor embedding) visualization. tSNE maps56 were Fig. 6c). Branch probability correlations are >0.94, except for pDC branch with
generated using diffusion components scaled by the eigenvalues as inputs rather k = 25 where the correlations are lower because of insufficient connectivity of the
than principal components of the data and perplexity set to 150. The scaling of graph. (Supplementary Fig. 6d).
eigenvectors ensures less sensitivity to outliers in the data and is performed as follows:
Robustness to number of diffusion components. Robustness to number of
e i_scaled= 1−
λl
λl e i (1) d st i a f t f e u s s i ( o S n u p c p om lem po e n n e ta n r t y s w Fi a g s . t 7 e ) s . t T ed h e b y c o u r s r i e n l g at f i i o x n in s g o f k p , w se a u y d p o o - i t n im ts, e a , n D d P , t e a r n m d i b n r a a l n ch
NAtuRe BioteChNoLoGy | www.nature.com/naturebiotechnology
Articles NAtuRe BiotecHNology
probabilities for all branches for all cells are shown in Supplementary Fig. 7a,b. mitochondrial molecule fraction (>0.2) were excluded from the analysis. Immune
Pseudo-time ordering and DP correlations are all >0.96 (Supplementary Fig. 7a). cells were also excluded since they are not relevant for differentiation. Data were
Branch probability correlations are >0.94 (Supplementary Fig. 7b). A subset normalized as described in ‘scRNA-seq data preprocessing’. Phenograph clustering
of cells sampled from the middle of the differentiation process is shown in of data revealed a cluster of cells with low molecule count distribution, which was
Supplementary Fig. 7c, with the corresponding pseudo-time, DP, and branch excluded from the analysis. To maintain consistency with the analysis in
probability correlations shown in Supplementary Fig. 7c,d. Pseudo-time ordering the original publication, the data were not log transformed and were restricted
correlations are all >0.97. DP correlations range between 0.84 and 0.99, with 75% to genes used by the authors. The gene list was downloaded from Flowrepository
of correlations >0.9 (Supplementary Fig. 7c). Branch probability correlations are all (FR-FCM-ZYAG).
>0.94 (Supplementary Fig. 7d). As before, PCA was performed to reduce the data to 20 components
(explaining 85% of the variance) and diffusion maps were computed using
Robustness to subsampling of cells. To test the robustness of Palantir to subsampling principal components as the input. Palantir was run using one of the Lgr5+ stem
of the cells, cells from the different lineages were subsampled at different cells as the start. Palantir automatically identified colonocytes, goblet cells, and
rates (25%, 50%, and 75%) from each of the following clusters individually Reg4+ goblet cells as the terminal states but failed to identify tuft cells as one of the
(Supplementary Fig. 2): (1) 3, 6—monocytic, (2) 5—lymphoid, and (3) 2, terminal states. Tuft cells are very similar in their expression profiles to the early
8—erythroid lineage (Supplementary Fig. 8). The robustness was measured using cells and thus there was not sufficient variability for the small number of tuft cells
Pearson correlation between pseudo-time, DP, and branch probabilities with and to be projected onto a distinct diffusion component (note, we believe that greater
without subsampling (Supplementary Fig. 8). All correlations are >0.94. cell numbers would have resolved this). The results in Fig. 5b were generated by
manually setting tuft cells as one of the terminal states.
Comparison of Palantir results across replicates. Palantir results, specifically pseudo-
time and DP, from one replicate are projected onto cells from a second replicate Performance of competing methods on the CD34+ marrow data. We undertook
using mutually nearest neighbors (Supplementary Fig. 10). The projected results a systematic evaluation of the performance of Palantir in comparison with widely
are then correlated with Palantir results derived de novo from the second replicate used trajectory inference algorithms such as Monocle2, DPT, PAGA (based on
to measure reproducibility of Palantir results across the replicates. DPT), Slingshot, FateID, and Monocle 2.
Let N and N be the numbers of cells in replicates 1 and 2, respectively. As a We first compared the algorithms by evaluating their setup—the previous
1 2
first step, the count matrices of both replicates are combined to create a unified biology knowledge required as input and the diversity of outputs provided by each
molecule count matrix using genes detected in both replicates. This matrix is algorithm—using the following criteria:
normalized as described for scRNA-seq analysis in Data preprocessing and log
(1) Does the algorithm require the specification of start cell or start state?
transformed with a pseudo-count of 0.1, followed by PCA. Principal component
(2) Does the algorithm require the specification of number of branches or clus-
space of the combined count matrix is used to determine the k-nearest replicate
tering/segmentation of the data a priori?
1 neighbors of replicate 2. This neighborhood graph can be represented by an
(3) Are the terminal states automatically determined by the algorithm?
adjacency matrix D21∈RN2×N1, where D
i
2
j
1 is the distance between cell i of replicate
(4) Does the algorithm generate a unified pseudo-time ordering of cells that
2 and cell j of replicate 1 if i and j are neighbors. Similarly, let D12∈RN1×N2
enables the comparison of gene expression patterns across different lineages?
represent the adjacency matrix of replicate 2 neighbors of replicate 1.
(5) Does the algorithm identify continuities in cell fate specification by determin-
Mutually nearest neighbors between the two replicates are computed as below
ing branch probabilities, fate biases, or DP?
MNN2=D21⊙D12T (2) (6) D
to
o
p
e
o
s
l o
th
gy
e
?
algorithm generalize to topological structures beyond a tree
where MNN∈RN2×N1 and ⊙ is the Hadamard product or element-wise Supplementary Fig. 17a summarizes the characteristics of the different
algorithms according to the criteria outlined above:
multiplication operator. The distances of the MNN adjacency matrix are converted
to an affinity matrix using equation (12) (Supplementary Note 1). (1) All of the algorithms require the specification of a start cell or state to orient
the pseudo-time ordering.
W ij=exp(−MNN2 ij )∕ ∑ exp(−MNN i 2 k ) (3) (2) DPT, Slingshot, and FateID all require the specification of either the number
k=1:N2 of branches and/or predetermined clustering of the data, making them
Palantir results of replicate 1 are projected on to the cells of replicate 2 using the sensitive to the number of branches selected and the quality of the clustering,
weights computed in equation (27) (Supplementary Note 1). The projected results which is notoriously sensitive in the case of continuous differentiation data.
are thus a weighted average of the mutually nearest neighbors of each cell. (3) Palantir and Slingshot can automatically determine the terminal states. PAGA
resp L e e c t t i τ v R e e l p y 1 . a T n h d e τ p Re r p o 2 j b e e c t t e h d e p d s e e u n d o o v - o t i p m su e e i d s o c - o t m im p e u t o e r d d e a r s i n fo g l l o o f w r s eplicates 1 and 2, r F e a q te u I i D re s a n sp d e M cifi o c n a o t c io le n 2 o r f e t q h u e i r P e A e G x A pl i c c l i u t s s t p er e s c i t fi h c a a t t b io e n lo o n f g t t h o e a t e p r a m rt i i n c a u l l a st r a l t i e n s e . age.
DPT requires the specification of number of branches.
τRep2_projected=W×τRep1 (4) (4) Slingshot and FateID do not provide a unified pseudo-time ordering of
cells and thus do not facilitate comparison of gene expression trends across
Pearson correlation between τRep2_projected and τRep2 gives a measure of reproducibility lineages
of Palantir pseudo-time. Similarly, the projected DP is computed as follows (5) Palantir and FateID both output a probability vector of cell fate choice conti-
nuities for each cell. Furthermore, Palantir also quantifies the DP of a cell by
E Rep2_projected=W×E Rep1 (5) summarizing the cell fate choice branch probabilities.
(6) PAGA is the only algorithm that determines the topological structure of the
Similar to the pseudo-time, Pearson correlation between E and E gives differentiation hierarchy without previous assumptions about the topology.
Rep2_projected Rep2
a measure of reproducibility of the DP.
Thus, Palantir uses minimal a priori biological information to (1) automatically
determine the different terminal states, (2) generate a unified pseudo-time
Additional datasets. Mouse hematopoiesis dataset. The mouse hematopoiesis
ordering to compare gene expression trends across lineages, and (3) identify
dataset6 was downloaded and preprocessed using the procedure outlined in
continuous branch probabilities and DP for each cell.
Scanpy57 (https://github.com/theislab/paga/blob/master/blood/paul15/paul15. We next used the CD34+ human bone marrow data (replicate 1) as a
ipynb). A cluster of cells annotated as dendritic cells was projected as a clear outlier
benchmark to compare the results of the different algorithms. Due to the varied
along a diffusion component without a well-defined differentiation path (probably
nature of the different outputs, we evaluated the ability of the algorithm to
due to insufficient cell sampling) and therefore was excluded from the analysis.
determine known and well-established features of human hematopoiesis, such as
PCA was performed on the preprocessed data and components that explain
(1) identification of the different lineages represented in the data, with emphasis
85% of the variance were used for generating diffusion maps as described in The
on less frequent populations such as megakaryocytes, cDCs, and pDCs, which
Palantir algorithm. The eigengap suggested use of 7 diffusion components, but
are more subtle and challenging to infer, and (2) recovery of known expression
13 components were used instead to ensure inclusion of all cell types. Note that
trends of key genes across multiple lineages. We choose well-studied canonical
the frequencies of some of the populations such as basophils are extremely low,
genes across the different lineages, whose expression dynamics are known and can
necessitating the inclusion of additional components.
thus serve as ground truth. The following canonical genes, representing a broad
Palantir was run using one of the cells annotated as a megakaryocyte-erythroid
spectrum of gene expression dynamics, were chosen for this evaluation:
precursor cell since these are the most primitive cells present in the data. Palantir
automatically determined the different terminal states and determined pseudo- (1) CD34. Marker of stem and precursor cells and known to be downregulated
time ordering, DP, and branch probabilities. DP trends and gene expression trends with differentiation in all cells11.
were generated as described in Supplementary Note 2. (2) MPO. Early marker for myeloid lineages with higher expression during
monocyte lineage commitment38.
Mouse colon data. Raw counts for the mouse colon dataset35 were downloaded (3) CD79B. Marker for lymphoid lineage commitment39.
from GEO (GSE102698). Cells with low molecule count (<1,000) and high (4) GATA1. Marker for erythroid lineage commitment28.
NAtuRe BioteChNoLoGy | www.nature.com/naturebiotechnology
NAtuRe BiotecHNology Articles
(5) CSF1R. Known to be upregulated in cDCs and downregulated in pDCs fol- at http://nbviewer.jupyter.org/github/dpeerlab/Palantir/blob/master/notebooks/
lowing an initial upregulation40. Palantir_sample_notebook.ipynb. The code and data for this article, along with an
(6) CD41. Marker for megakaryocyte lineage commitment21. accompanying computational environment, are available and executable online as
a Code Ocean capsule: https://doi.org/10.24433/CO.6f3a9d2b-82d6-45bd-a583-
Supplementary Fig. 17b shows the results of this comparison for the different
5346a30e0c5d (ref. 58).
algorithms. Palantir and DPT were able to identify the megakaryocyte lineages,
whereas PAGA and Slingshot included these cells as part of the erythroid lineage.
Palantir was the only algorithm able to recover the distinction between the two Data availability
dendritic cell lineages. Comparing the expression trends, all algorithms except Raw and processed data are available through the Human Cell Atlas data portal
Monocle 2 recovered the downregulation of CD34 across all lineages. Palantir at https://data.humancellatlas.org/explore/projects/091cf39b-01bc-42e5-9437-
recovers the known gene expression trends across all lineages (Fig. 2). While f419a66c8a45.
PAGA, DPT, and Slingshot identify the trends in the larger lineages, PAGA (and
DPT) suffers from a loss in resolution in gene expression trends and Slingshot does
not provide a unified ordering of cells to compare gene expression trends across References
lineages. FateID with the default clustering using RaceID failed to identify any
53. Klein, A. M. et al. Droplet barcoding for single-cell transcriptomics applied to
correct lineages and gene expression trends, whereas FateID with a preprocessing
embryonic stem cells. Cell 161, 1187–1201 (2015).
procedure and clustering followed in Palantir identifies correct expression trends
54. Buettner, F. et al. Computational analysis of cell-to-cell heterogeneity in
in only the monocytic and lymphoid lineages. Monocle 2 could not recover the key
single-cell RNA-sequencing data reveals hidden subpopulations of cells. Nat.
hematopoietic lineages or expression trends from the CD34+ bone marrow data.
Biotechnol. 33, 155–160 (2015).
See Supplementary Note 6 for a detailed description of the different algorithms and
55. Buettner, F., Pratanwanich, N., McCarthy, D. J., Marioni, J. C. & Stegle, O.
their performances.
f-scLVM: scalable and versatile factor analysis for single-cell RNA-seq.
Genome Biol. 18, 212 (2017).
Reporting Summary. Further information on research design is available in the
56. van der Maaten, L. P. J. & Hinton, G. E. Visualizing high-dimensional data
Nature Research Reporting Summary linked to this article.
using t-SNE. J. Mach. Learn. Res. 9, 2579–2605 (2008).
57. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell gene
Code availability
expression data analysis. Genome Biol. 19, 15 (2018).
Palantir is available as a Python module at https://github.com/dpeerlab/Palantir/. 58. Setty, M. et al. Characterization of cell fate probabilities in single-cell data
A Jupyter notebook detailing the workflow including data preprocessing, running with Palantir. Code Ocean Capsule https://doi.org/10.24433/CO.6f3a9d2b-
Palantir along with a demonstration of various plots, and visualizations is available 82d6-45bd-a583-5346a30e0c5d (2018).
NAtuRe BioteChNoLoGy | www.nature.com/naturebiotechnology
1
nature
research
|
reporting
summary
October
2018
Corresponding author(s): Dana Pe'er
Last updated by author(s): Jan 29, 2019
Reporting Summary
Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency
in reporting. For further information on Nature Research policies, see Authors & Referees and the Editorial Policy Checklist.
Statistics
For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.
n/a Confirmed
The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement
A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly
The statistical test(s) used AND whether they are one- or two-sided
Only common tests should be described solely by name; describe more complex techniques in the Methods section.
A description of all covariates tested
A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons
A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient)
AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)
For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted
Give P values as exact values whenever suitable.
For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings
For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes
Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated
Our web collection on statistics for biologists contains articles on many of the points above.
Software and code
Policy information about availability of computer code
Data collection bcl2fastq2 v2.20
Data analysis Python 3.6. Python modules: numpy 1.14, pandas 0.22, networkx 2.1, sklearn 0.19.1, Phenograph 1.5.2, tables 3.4.2, python-bthsne,
matplotlib 2.2.2, seaborn 0.8.1, SEQC 0.2.1, MAST 1.2.1, bowtie2 2.3.4.1, samtools 1.6 SeqGL 1.1.4, scanpy 1.3.2
R 3.5.0, R module: gam 1.5
Custom software code: palantir 0.2 https://github.com/dpeerlab/Palantir
For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors/reviewers.
We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Research guidelines for submitting code & software for further information.
Data
Policy information about availability of data
All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:
- Accession codes, unique identifiers, or web links for publicly available datasets
- A list of figures that have associated raw data
- A description of any restrictions on data availability
Raw and processed data is available through the Human Cell Atlas data portal at https://prod.data.humancellatlas.org/explore/
projects/29f53b7e-071b-44b5-998a-0ae70d0229a4
2
nature
research
|
reporting
summary
October
2018
Field-specific reporting
Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.
Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences
For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf
Life sciences study design
All studies must disclose on these points even when the disclosure is negative.
Sample size Sample size scRNA-seq data was collected from three independent donors to asses for reproducibility of results.
Data exclusions No data was excluded
Replication Computational predictions were replicated across the three replicates. The results of the algorithm were projected onto second replicate and
compared to the results derived denovo from the replicate. The results are reproducible across the three replicates
Randomization Not applicable since there were no clinical trials.
Blinding Not applicable since there were no clinical trials.
Reporting for specific materials, systems and methods
We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material,
system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.
Materials & experimental systems Methods
n/a Involved in the study n/a Involved in the study
Antibodies ChIP-seq
Eukaryotic cell lines Flow cytometry
Palaeontology MRI-based neuroimaging
Animals and other organisms
Human research participants
Clinical data
