---
source_path: /mnt/c/Users/Administrator/Zotero/storage/66VAKQML/Qu 等 - 2024 - Gene trajectory inference for single-cell data by optimal transport metrics.pdf
ingested: 2026-04-23
sha256: 1886178ccc535c98
---

nature biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
Gene trajectory inference for single-cell data
by optimal transport metrics
Received: 19 December 2022 Rihao Qu1,2,3,11, Xiuyuan Cheng4,11, Esen Sefik 3, Jay S. Stanley III5, Boris Landa5,
Francesco Strino 6, Sarah Platt2,7, James Garritano5, Ian D. Odell3,7,
Accepted: 26 February 2024
Ronald Coifman5,8,9, Richard A. Flavell 3,10,12, Peggy Myung 2,7,12 &
Published online: xx xx xxxx Yuval Kluger 1,2,5,12
Check for updates
Single-cell RNA sequencing has been widely used to investigate cell
state transitions and gene dynamics of biological processes. Current
strategies to infer the sequential dynamics of genes in a process typically
rely on constructing cell pseudotime through cell trajectory inference.
However, the presence of concurrent gene processes in the same group
of cells and technical noise can obscure the true progression of the
processes studied. To address this challenge, we present GeneTrajectory,
an approach that identifies trajectories of genes rather than trajectories
of cells. Specifically, optimal transport distances are calculated between
gene distributions across the cell–cell graph to extract gene programs
and define their gene pseudotemporal order. Here we demonstrate that
GeneTrajectory accurately extracts progressive gene dynamics in myeloid
lineage maturation. Moreover, we show that GeneTrajectory deconvolves
key gene programs underlying mouse skin hair follicle dermal condensate
differentiation that could not be resolved by cell trajectory approaches.
GeneTrajectory facilitates the discovery of gene programs that control the
changes and activities of biological processes.
Dynamic gene expression changes often specify mechanisms through construction, gene dynamics underlying a biological process can be
which cells determine state and function. Indeed, tightly regulated inferred by tracking the changing patterns of their expression levels
gene cascades underlie a myriad of fundamental processes, such as along the cell pseudotime12,15,21.
cell cycle (CC)/mitosis1–4 and tissue/organ differentiation5–8. With the However, when cells undergo multiple processes in parallel (for
emergence of single-cell RNA-sequencing (scRNA-seq) platforms, example, CC coupled with cell differentiation22 or circadian clock23) and
cell trajectory inference techniques9–19 are widely applied to study each process is governed by a different set of genes, cell pseudotime
the cellular dynamics of biological processes. These techniques use learned by organizing cells using the collective genes becomes less
single-cell whole-transcriptome data to organize cells into lineages informative, as it mixes the effects of multiple processes. Mathe-
and infer a unidimensional latent variable (that is, pseudotime20) that matically, when multiple processes that are not strongly correlated
describes a cell’s position along a lineage process. After pseudotime with each other co-occur in the same group of cells, cell geometry
1Computational Biology & Bioinformatics Program, Yale University, New Haven, CT, USA. 2Department of Pathology, Yale University School of Medicine,
New Haven, CT, USA. 3Department of Immunobiology, Yale University School of Medicine, New Haven, CT, USA. 4Department of Mathematics, Duke
University, Durham, NC, USA. 5Program in Applied Mathematics, Yale University, New Haven, CT, USA. 6PCMGF Limited, Watford, UK. 7Department of
Dermatology, Yale University School of Medicine, New Haven, CT, USA. 8Department of Mathematics, Yale University, New Haven, CT, USA. 9Department
of Electrical Engineering, Yale University, New Haven, CT, USA. 10Howard Hughes Medical Institute, Yale University School of Medicine, New Haven,
CT, USA. 11These authors contributed equally: Rihao Qu, Xiuyuan Cheng. 12These authors jointly supervised this work: Richard A. Flavell, Peggy Myung,
Yuval Kluger. e-mail: yuval.kluger@yale.edu
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
(determined by these processes) cannot be effectively parametrized populations. In our work, we distinctively define the graph-based
by a common single latent variable. Hence, organizing cells into Wasserstein distance between pairs of genes to study their underlying
unidimensional lineages is no longer appropriate. pseudotemporal dynamics. Specifically, we normalize the expression
To address this challenge, we propose GeneTrajectory, an approach of a gene into a probabilistic distribution over cells and then compute
to studying dynamic processes that does not rely on unidimensional the Wasserstein distances between gene distributions in the cell graph
parameterization of the cell manifold. GeneTrajectory allows us to (Fig. 1d). Here the cell graph is constructed in a way that provides a
deconvolve multiple, independent processes with sequential gene representation of cells, which preserves the cell manifold structure
dynamics. In contrast to cell trajectory approaches, GeneTrajectory in the high-dimensional space (Fig. 1c). In this construction, the
constructs trajectories of genes rather than trajectories of cells. Our graph-based Wasserstein distance between pairwise gene distributions
algorithm dissects out gene programs from the whole transcriptome, has the following characteristics: (1) it takes into account the geometry
eliminating the need for initial cell trajectory construction or the of cells; that is, it assigns a higher cost to transport a point mass from
specification of the initial and terminal cell states for each process. one cell to a distant cell as compared to its adjacent neighbors. (2) It
Using this method, genes that sequentially contribute to a given prevents the transport across the ambient cell space, which is often a
biological process can be extracted and organized into a respective problematic issue when using spatial distance measures (for example,
gene trajectory that reveals the successive order of gene activity. the Euclidean distance in the cell space).
In this work, we begin by showing GeneTrajectory’s efficacy In our approach, the computation of gene–gene Wasserstein
for unraveling gene dynamics through simulation experiments and distances is based on the following two steps (Table 1):
application to a human myeloid lineage dataset. Subsequently, we
use our approach on a mouse embryonic skin dataset to demonstrate • Construct a cell graph. As an initial step, we learn a reduced-
that GeneTrajectory can resolve critical cell state transitions during dimensional cell embedding that can capture and represent the
the early-stage development of hair follicles5,24. Our results indicate cell manifold structure in the original high-dimensional space.
that GeneTrajectory extracts gene geometry without the need for Next, we construct a k-nearest neighbor (kNN) graph of cells based
constructing cell pseudotime, revealing independent trajectories of on their relative distances in the cell embedding (Fig. 1c). This
concurrent processes that are otherwise obscured by cell pseudotime establishes a cell–cell connectivity map that serves as the
approaches. ‘roadmap’ for transporting gene distributions in the next step.
Here, for a given pair of cells u and v, we search for the shortest
Results path connecting them in the kNN cell graph and denote its length
Computing optimal transport between genes over the cell as the graph distance dG(u,v) between cells u and v. This graph
graph distance will be used to define the cost of transporting a point mass
A progressive dynamic biological process is usually governed by a between cells u and v in the next step.
finely regulated gene cascade25–27, in which genes are activated and • Compute gene–gene Wasserstein distances over the cell graph.
deactivated in a temporal order along the process, dictating the We model the expression level of genes as discrete distributions
transcriptomic changes of underlying cell states. Moreover, cells can on the cell graph. Specifically, we divide the original expression
partic ipate in multiple processes simultaneously, either in a dependent level of a given gene in each cell by the sum of its expression level
or independent manner. For instance, we illustrate two contrasting in all cells. We then define the distance between two gene distribu-
scenarios by considering the concurrence of a linear process (for tions by the graph-based Wasserstein-p distance (W distance,
p
example, differentiation) and a cyclic process (for example, CC; 1 ≤ p < ∞; Fig. 1c,d). Accordingly, the transport cost between cells
Fig. 1a). When these two processes are strictly dependent on each other, u and v is defined as Cu,v=dG(u,v) p. Here p is a user-defined para-
they can be parameterized by a common latent variable and result in meter, and p = 1 refers to the well-known Earth Mover’s distance.
a one-dimensional cell curve. In this scenario, it is straightforward Algorithmic details are described in ‘Step 2. Compute graph-based
to assign a meaningful pseudotime for the cells by ordering them Wasserstein distances between genes’.
along the curve. However, deconvolving genes into two processes
and retrieving their pseudotemporal order in each process is not In practice, computing the Wasserstein distance between all pair-
immediately apparent, which requires additional postprocessing wise gene distributions can be computationally expensive. When the
(for example, clustering gene dynamics along the cell pseudotime12). cell graph is large, the time cost for finding the OT solution increases
In contrast, when these two processes are independent, cells fall into exponentially. In our framework, we have designed two strategies to
a manifold (as a Cartesian product of these two processes) with an accelerate the computation based on (1) cell graph coarse-graining, and
intrinsic dimension >1. These processes do not share a common latent (2) gene graph sparsification (details in ‘Step 2. Compute graph-based
variable, thus gene dynamics inference based on unidimensional Wasserstein distances between genes’).
interpolation along the cell–cell manifold is no longer appropriate.
In practice, the weak and stochastic nature of the dependency between Gene trajectory construction
concurrent biological processes can complicate the extraction of the The gene–gene Wasserstein distance captures the pseudotemporal
cell path and the construction of cell pseudotime. relations of genes in the sense that if two genes are activated consec-
Here we present GeneTrajectory, an approach to inferring utively along a biological process, their distributions are expected
gene processes through learning the gene–gene geometry without to have a substantial overlap in the cell graph and thus have a small
one-dimensional parameterization of the cell manifold (Fig. 1b). Wasserstein distance between each other (Fig. 1e). To visualize the
Specifically, GeneTrajectory quantifies the distance of genes based geometry of all genes, we convert pairwise gene–gene Wasserstein
on their expression distributions over a cell graph using optimal distances into gene–gene affinities and use diffusion map to get a
transport (OT) metrics (Fig. 1d). Previously, OT metrics (for example, low-dimensional representation of genes. If dynamical cascades of
Wasserstein distance) have been applied in a wide range of scenarios in gene activation and deactivation exist in the data, viewing the gene
single-cell analysis, including (1) defining a distance measure between embedding by a combination of leading diffusion map eigenvectors
cells28,29 or cell populations30, (2) constructing cell trajectories31,32, delineates trajectories of genes (Fig. 1f). Each trajectory is linked with a
(3) spatial reconstruction of single-cell transcriptome profiles33,34 and specific gene program that dictates the underlying biological process.
(4) multi-omics data integration35. In these works, the dissimilarity In our approach, the extraction of gene trajectories is performed in
was quantified either between a pair of cells or between a pair of cell a sequential manner (Fig. 1g). To identify the first trajectory, we search
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
a Scenario A: Scenario B: Cell pseudotime Cell pseudotime
Cell geometry Cell pseudotime Cell geometry (linear process) (cyclic process)
Process diagram Process diagram
Cyclic Cyclic
Linear Linear
(Dependent) (Independent)
(Intrinsic dimension = 1) 0 T (Intrinsic dimension = 2) 0 T 0 T
L C
b Step 1: cell graph construction Step 2: gene–gene dist. computation Step 3: gene trajectory inference Step 4: gene ordering
Cell Cell graph Gene graph Gene trajectories Gene dynamics
Cell Gene 1 Geneg 2
Gene 2
g 1 OT g 1 g 2 g 3
Gene Count Cell Distance Gene
distance
g
4
c d Gene expression profiles Gene–gene OT distances
(over the cell graph)
Cell cloud Cell kNN graph 0000 ...69
3
G
(g
e
1 )
ne 1
g 1
1 1 0 0 . .0 . 5 5 G (g e 2 n ) e 2 g 2 g
3
3Gene 3
21
0
(g
3
)
Transcriptome space
g
(high-dimensional) 4
1.5Gene 4
00 1. . 0 5(g 4 )
e f g h
Gene–gene OT distance matrix
Gene affinity graph Trajectory identification and gene ordering Visualization
(submatrix example)
g 1 g 2 g 3 g 4 g 1 Terminus 2 Terminus 3
10
g 1 8 g Trajectory 1
g 2 6 3 Terminus 1 T T r r a a j j e e c c t t o o r r y y 3 2
g
g 3 4 g 2 4
2
g
4 0 0 1
Gene pseudo-order (normalized)
Fig. 1 | Overview of GeneTrajectory. a, Illustration of two scenarios when a on gene–gene affinities (transformed from gene–gene Wasserstein distances).
linear process and a cyclic process are dependent or independent of each other, g, Sequential identification of gene trajectories using a diffusion-based strategy.
resulting in cell manifolds with different intrinsic dimensions and requiring The initial node (terminus 1) is defined by the gene with the largest distance from
distinct pseudotime parametrizations. b, Schematic representation of the major the origin in the diffusion map embedding. A random-walk procedure is then
workflow of GeneTrajectory. c, Construction of cell kNN graph. d, Computation used on the gene graph to select the other genes that belong to the trajectory
of graph-based OT (Wasserstein) distances between paired gene distributions terminated at terminus 1. After retrieving genes for the first trajectory, we
(four representative genes are shown) over the cell graph. Gene distributions identify the terminus of the subsequent gene trajectory among the remaining
are defined by their normalized expression levels over cells. e, Heatmap of OT genes and repeat the steps above. This is done iteratively until all detectable
(Wasserstein) distances for genes g–g in d. f, Construction of gene graph based trajectories are extracted. h, Diffusion map visualization of gene trajectories.
1 4
for the gene that has the largest distance from the origin of diffusion eigenvector of the diffusion map embedding provides an intrinsic
map embedding, which serves as the terminus of the first gene trajec- ordering of the genes along that trajectory36,37.
tory. To retrieve the other genes along the first trajectory, we take that To examine how the gene order along a given gene trajectory
terminus gene as the starting point of a diffusion process. Specifically, is reflected over the cell graph, we can track how these genes are
we assign a unit point mass to that gene and then diffuse the mass to expressed across different regions in the cell embedding. Specifically,
the other genes. As the probability mass propagates along the gene we first group genes along each gene trajectory into successive bins and
trajectory from its terminus, the trajectory can be retrieved by a heu- generate a cell embedding ‘snapshot’ for each bin. In each snapshot, we
ristic thresholding procedure (‘Step 3. Construct gene trajectories’). color the cells according to the fraction of genes (from that bin) that
After retrieving genes for the first trajectory, we identify the terminus they express. By plotting the expression level of each gene bin on the
of the subsequent gene trajectory among the remaining genes and cell embedding, we can visualize how the underlying biological process
iterate the same procedure, until all detectable gene trajectories are progresses across cell populations.
extracted (Fig. 1g,h).
To order the genes along a given trajectory, we retain only these Assessing GeneTrajectory’s performance using simulation
genes to recompute a diffusion map embedding based on their pair- Assuming that a progressive biological process is temporally dictated
wise gene–gene Wasserstein distances. The obtained first nontrivial by a sequence of genes, we simulated several artificial scRNA-seq
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
Table 1 | List of core notations in Methods of two processes into two gene trajectories representing a (linear or
tree-like) differentiation process and a (circular) CC process. Along
u, v Index of cells each trajectory, genes are ordered in high concordance with the
i, j Index of genes ground truth (Supplementary Table 1), indicating that GeneTrajectory
allows deconvolving a mixture of biological processes that take place
m Original number of cells
simultaneously in the same group of cells.
n Original number of genes
m′ Reduced number of cells after coarse-graining GeneTrajectory resolves myeloid gene dynamics
We demonstrate GeneTrajectory’s application using myeloid
δ(p)(ρ,ρ′) Wasserstein-P distance between distributions ρ and ρ′
lineage differentiation, a classical biological system with a well-defined
d E (u, v) Euclidean distance between cell u and v bifurcation of two major lineages38,39. We extracted human myeloid
d (u, v) Graph distance between cells u and v cells from a public 10× Genomics peripheral blood mononuclear cell
G
(PBMC) dataset and identified four cell types based on canonical mark-
C Transport cost matrix on the cell graph. C represents the cost
of transport between cell u and v u,v ers (Fig. 3a and Extended Data Fig. 2b,c). These included CD14+ mono-
cytes, intermediate monocytes with high expression of HLA-DR (Human
C′ Transport cost matrix on the coarse-grained cell graph
Leukocyte Antigen – DR isotype), CD16+ monocytes and myeloid type-2
M kNN membership matrix for the cell graph. M(u, a) = 1/∣a∣ if and
dendritic cells. The UMAP visualization of the cell embedding shows a
only if the cell u belongs to the ath subset, where ∣a∣ represents
the number of cells in that subset; otherwise M(u, a) = 0 continuum of cell states underlying myeloid lineage genesis, compris-
ing monocyte maturation and dendritic cell differentiation. Human
A Gene–gene affinity matrix
monocyte maturation involves the upregulation of CD16 on a subset
P Row-normalized gene–gene affinity matrix (as the random-walk of CD14+ classical monocytes40. Specifically, CD14+ monocytes first
matrix)
transition into an intermediate subset of monocytes and then differ-
S Diffusion map (spectral) embedding of genes entiate into CD16+ nonconventional monocytes with distinct effector
functions.
We used GeneTrajectory to identify three gene trajectories, each
datasets with a variety of gene dynamics by modeling the change representing a specific aspect of the myeloid lineage differentiation
of gene expression over time (Extended Data Fig. 1a,b; ‘Workflow of process (Fig. 3b). Viewing the gene bin plots of Trajectory 1 illustrates
gene dynamics simulation’). Specifically, for a gene involved in a given that a subset of CD14+ monocytes start a differentiation cascade and
biological process, we simulate its expected expression level λ(t) as a gradually shift toward CD16+ monocytes, which suggests Trajectory 1
function of time t. For clarity, we note that t represents the pseudotime captures the gene dynamics underlying the early stage of monocyte
of a biological process, linked with the cell state (for example, differ- maturation (Fig. 3c). Notably, CLEC5A, RETN, CCR2 and SELL (CD62L) are
entiation status) rather than the actual time (for example, specific day known to be associated with the initial CD14+ monocyte cellular state40
of a developmental process). Here we use multiple parameters to and are highlighted as part of Trajectory 1 (Fig. 3b). Subsequently, the
account for the heterogeneity of gene expression profiles in single-cell ordering of genes that define Trajectory 2 provides a pseudotemporal
data, including the variation of duration time and expression intensi- view on the later stage of CD16+ monocyte differentiation (Fig. 3d). This
ties (details in ‘Workflow of gene dynamics simulation’). For each cell process is primarily driven in response to cytokine colony-stimulating
state at t along a biological process, we apply a Poisson sampling to factor 1 (CSF1) and requires CSF1R41. While ordered after CSF1R, ICAM2
generate the observed expression level of each gene by taking λ(t) as is known to be constitutively expressed in CD16+ monocytes and is
the mean of Poisson distribution. In these simulation experiments, necessary for their patrolling ability across the endothelium of blood
we know the ground truth of both the pseudotime of each cell in the vessels41,42. Coming toward the end, C1QA, C1QB43 and FCGR3A markers
corresponding biological process and the temporal order of genes broadly expressed by fully differentiated CD16+ monocytes are identi-
that dictate each process. Finally, we incorporate an optional step to fied. In addition, we retrieved a third gene trajectory (Trajectory 3) that
account for sequencing depth. This is achieved by sampling a speci- marks the differentiation of type-2 dendritic cells as a distinct myeloid
fied number of nonzero entries from the original count matrix. This lineage (Fig. 3e). Myeloid type-2 dendritic cells have the following two
procedure enables us to generate an artificial dataset with varying subsets: CD14+ and CD14−. Specifically, the CD14+ subset shares over-
levels of missing data. lapping features with CD14+ monocytes, whereas the CD14− subset is
We first simulated (1) a cycling process in which the change of gene delineated here as corresponding with a separate gene trajectory44. In
expression shows a periodical pattern over time (Fig. 2a and Extended contrast to CD16+ monocytes, these CD14− dendritic cells differentiate
Data Fig. 1c), and (2) a process with a branching point where it diverges in response to GMCSF and IL4, in line with expression of CCR5, CD2,
into two different lineages (Fig. 2b and Extended Data Fig. 1d). Inspec- CLEC10A, CD72, CD1C and PKIB45 (Fig. 3b and Extended Data Fig. 2a).
tion of the gene trajectories in these two simulation examples reveals Notably, GeneTrajectory does not necessitate specification of the ini-
similar layouts with their cell embeddings (Fig. 2a,b). The ordering of tial and terminal cell states for each process, while those states can be
genes along each gene trajectory shows a high concordance with the automatically revealed by inspecting the cell population that express
ground truth (Supplementary Table 1). the endpoint genes of each gene trajectory.
We next, created two scenarios that simulate a mixture of two
concurrent processes (Fig. 2c,d and Extended Data Fig. 1e,f). Speci- Deconvolving gene processes in dermal condensate genesis
fically, one process mimics cell differentiation (linear or branched Hair follicle dermal condensates (DCs) emerge in the skin dermis
in a multilayered fashion), and the other mimics the CC. In these two around embryonic day 14.5 (E14.5) and have an essential role in
scenarios, each cell state is determined by two independent hidden hair follicle formation. Morphogenetic signals, including Wnt/β-
variables—a pseudotime along the differentiation process and a catenin signaling, are critical for the differentiation of DC cells5,24,46.
pseudotime in the CC. For each process, we simulated an exclusive We collected skin from E14.5 wild-type (WT) and paired K14Cre;
set of genes with distinct dynamic characteristics (Extended Data Wntlessfl/fl (Wls) mutant embryos for scRNA-seq (Fig. 4a). The genetic
Fig. 1e,f; ‘Workflow of gene dynamics simulation’), generating a cell defect in the mutant results in attenuated dermal Wnt signaling
manifold with a cylinder-shaped or a coral-shaped structure (Fig. 2c,d). and a lack of DCs and hair follicles47,48 (Fig. 4b–c and Extended Data
In both scenarios, our approach deconvolves the original mixture Fig. 3a).
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
Cellembedding Biologicalprocess Geneexpressionprofilesoverthecellembedding Geneembedding
a
Low High 0 Max
Geneexpressionlevel Genepseudo-order
(ineachlineage/process)
Visualizing cells on UMAP reveals a continuum of cell states com- signals shown to be necessary and sufficient for DC differentiation5,
posed of lower dermal cells (Dkk2+) and Wnt-activated upper dermal are present in the DC gene trajectory. Notably, the upper dermal cell
cells (Dkk1+ or Lef1+), which include DC cells (Sox2+; Fig. 4c and Extended embedding integrates a mixture of biological processes (CC and DC
Data Fig. 3a). We applied GeneTrajectory to the combined dermal cell differentiation) that co-occur within the same cell population. By
populations and extracted three prominent gene trajectories that cor- using GeneTrajectory, each biological process can be deconvolved
respond to lower dermis (LD) differentiation, DC differentiation and CC from the other and independently examined. Viewing the gene bin
(Fig. 4d). Specifically, we examined the CC gene ordering by checking plots for the CC and DC gene trajectories together reveals that DC
the distribution of genes associated with different CC phases along progenitors actively proliferate throughout all stages and then exit
the gene trajectory (Extended Data Fig. 3b). Wnt signaling pathway the CC at the terminus of DC differentiation (Fig. 4e). These data imply
genes (for example, Lef1 and Dkk1) and SHH (Sonic Hedgehog) signal- that DC cells are the immediate progeny of proliferative progenitors
ing pathway genes (for example, Ptch1 and Gli1), two morphogenetic in the upper dermis.
Nature Biotechnology
1ssecorP 2ssecorP
1ssecorP
2ssecorP
g 5 g 1 g 2 g 3 g 4 g 5 g 4
g
3
g 4 g 1 4 3 4 5 3 4 5 3 4 5 3 4 5 3 g 5
2 2 2 2 2
1 0 1 0 1 0 1 0 1 0 g 2
g 3 g 2 g 1
b g g g g g
1 2 3 4 5 g
g 5
g 4 5 g 2 g 1 4 3 2 1 4 3 2 1 4 3 2 1 4 5 3 2 1 4 5 3 2 1 g 4 g 3 g 2
g 3 0 0 0 0 0 g 1
c g g g g g
1 2 3 4 5
g
g 1
g g 5 4 g g 3 g g 2 g 6 4 3 2 1 0 g 7 4 3 2 1 0 g 8 4 3 2 1 0 g 9 4 3 2 1 0 g 10 4 3 2 1 0 g g 8 9g g 10 7 g 3 g g 6 2 g 1
10 8 6 4 3 4 3 4 3 4 3 4 3 g 4 g 5
2 2 2 2 2
g 9 g 7 1 0 1 0 1 0 1 0 1 0
d g g g g g
1 2 3 4 5
g 5 g 4 g 3 g g 2 1 4 3 2 1 0 4 3 2 1 0 4 3 2 1 0 3 2 1 0 4 3 2 1 0 g
g g 6
g 6 g 7 g 8 g 9 g 10 g 1 3 g g 2 4 g 1 9 0 g g 8 7
g g 7 g 5
8 g 6 4 3 4 3 4 3 4 3 4 3
g g 10 2 1 2 1 2 1 2 1 2 1
9 0 0 0 0 0
Fig. 2 | GeneTrajectory performance assessment based on simulation and gene embedding showcase distinct topologies. Cells are organized along
experiments. a, Simulation of a cycling process (CC). The cell embedding and a coral-shaped manifold that has an intrinsic dimension of two. Genes that
gene embedding showcase the same topology that has a ring-shaped structure. contribute to the two processes are deconvolved and organized along a ring-
b, Simulation of a differentiation process with two lineages. The cell embedding shaped trajectory and a multilayered-tree-structured trajectory. (a and b are
and gene embedding showcase the same topology that has a bifurcating tree visualized by t-SNE (t-distributed stochastic neighbor embedding); c and d are
structure. c, Simulation of a linear differentiation process coupled with CC. The visualized by UMAP (uniform manifold approximation and projection). The first
cell embedding and gene embedding showcase distinct topologies. Cells are column shows the cell embedding; the second column delineates the progressive
organized along a cylinder-shaped manifold that has an intrinsic dimension of dynamics of the simulated process with five genes selected along each process;
two. Genes that contribute to the two processes are deconvolved and organized the third to seventh columns show the expression of selected genes in the cell
along a ring-shaped trajectory and a linear trajectory. d, Simulation of a embedding following their pseudotemporal order; the eighth column displays
multilevel lineage differentiation process coupled with CC. The cell embedding the embedding of genes, colored by the ground truth of gene pseudo-order).
Article https://doi.org/10.1038/s41587-024-02186-3
a b
Gene trajectories
SERPINB10
2.0
1.5
Trajectory 1 CLEC5A 1.0 Trajectory 2 0.5
Trajectory 3 0
EV4
SLC4A3
PKIB
0.8
0.6
SELL 0.4
RETN 0.2
0
CCR2 CD1C C1QB CD72 FIBCD1
C1QA CSF1R CD2
CLEC10A 1.2
FCGR3A ICAM2 0.9
EV3 0.6
0.3
EV2 0
Gene pseudo-order Gene bin-1 Gene bin-2 Gene bin-3 Gene bin-4 Gene bin-5
c
800
600
400
200
0
d
300
250
200
150
100
50
0
e
80
60
GeneTrajectory identifies biological defects in Wls mutant bin as markers indicative of a specific DC differentiation stage, we first
We next use GeneTrajectory to examine how attenuated Wnt sign- identified cells that express more than half of the genes in the last bin as
aling affects the DC differentiation gene program. By tracking the cells in the final stage of differentiation (stage 7). Among the remaining
expression status of genes along each gene trajectory in the WT and cells, we identified the cells that express more than half of the genes
mutant cells (Fig. 5a), we did not detect a difference between the mutant in the sixth bin as progenitors in stage 6. We repeated this procedure
and control with respect to the CC and LD gene trajectories (Extended iteratively until all seven gene bins were associated with their matched
Data Fig. 4a,b). However, along the DC gene trajectory, Wls mutant cells cell populations (Fig. 5e,f and Extended Data Fig. 4c).
fail to express later-stage DC markers, indicating the defect is specific By comparing the composition of progenitors in different stages
to DC differentiation. Visualizing gene bin plots for the DC gene trajec- between the WT and Wls mutant, we found that mutant cells fail to
tory shows that mutant cells fail to progress in the DC differentiation express most of the markers after stage 4, when key markers in Wnt (for
process (Fig. 5e,f). example, Lef1) and SHH (for example, Gli1 and Ptch1) signaling path-
Moreover, gene trajectory inference allows us to define a specific ways are upregulated in the WT condition (Fig. 5e,f and Supplementary
stage of cell state transition by specifying a gene window along the Table 2). The average expression level of Wnt target genes is uniformly
gene trajectory. To understand how genetic mutation affects DC dif- lower in the mutant than in the WT condition (Fig. 5c and Extended
ferentiation, we use GeneTrajectory to stratify the pool of progenitors Data Fig. 4d), while the proportion of cells in the G1 phase of the CC is
by different stages of DC differentiation. Considering genes in each higher in the mutant across all stages (Fig. 5b). Consistent with this,
Nature Biotechnology
z
x y
z
x y
z
UMAP 1
Trajectory 1
x y
Trajectory 2
Trajectory 3
40
20
0
0 1 Gene bins core
2 PAMU
Cell embedding
CD16+monocytes
Myeloid type-2 dendritic cells
Intermediatemonocytes
CD14+monocytes
Fig. 3 | Gene trajectory inference on a myeloid scRNA-seq dataset. a, UMAP of showing the gene expression activities along each gene trajectory (Trajectory 1
myeloid cell population colored by cell types. b, DM (Diffusion Map) embedding (c), Trajectory 2 (d) and Trajectory 3 (e)) over the cell embedding. Genes along
of the gene graph based on gene–gene Wasserstein distances, visualized using each trajectory are ordered and then split into five equal-sized bins. Gene bin
the three leading nontrivial eigenvectors. Three prominent gene trajectories are score is defined by the proportion of genes (from each bin) expressed in each cell.
identified. Expression profiles of the genes at the terminus of these trajectories Arrows indicate the path of gene distribution progression over the cells.
are shown, each indicating a distinct myeloid cell state. c–e, Gene bin plots
Article https://doi.org/10.1038/s41587-024-02186-3
a b
D
d
UMAP 1
e
the rate of EdU nucleotide incorporation (S phase) is lower in the Wls we assessed performance by calculating the Spearman correlation
mutant (Figs. 4b and 5d). These data suggest that higher levels of Wnt between the gene ordering inferred from each approach and the ground
signaling are necessary to maintain a normal rate of cell proliferation truth. To order genes based on these cell trajectory inference methods,
across the DC differentiation process until DC progenitors exit the CC we first constructed the cell pseudotime using their default pipelines
at stage 7. These results also raise the notion that dermal proliferation (‘Comparing GeneTrajectory with cell trajectory methods in terms of
itself may directly regulate dermal cell state progression during the gene ordering inference’). Subsequently, we fitted generalized addi-
DC differentiation process. tive models (GAM)49,50 to find the peak location of each gene expres-
sion along the cell pseudotime. The genes were then ordered based on
Comparison of GeneTrajectory to cell trajectory methods these peak locations. GeneTrajectory achieved the best performance in
We compared GeneTrajectory with five cell trajectory methods as recovering gene order for both cyclic and linear processes (Fig. 6a,b) in
follows: Monocle 2 (ref. 16), Monocle 3 (ref. 10), Slingshot9, PAGA11 simulation experiments, showing remarkable robustness to variations
and CellRank15. In the simulations of two co-occurring processes, in cell numbers and sparsity levels of the count matrix.
Nature Biotechnology
2
PAMU
WT
(CTL)
scRNA-seq
library
KO
(Wls)
c
WT
KO
Gene bin-1 Gene bin-2 Gene bin-3 Gene bin-4 Gene bin-5 Gene bin-6 Gene bin-7
Trajectory-DC
Trajectory-LD
Trajectory-CC
0 1 Genebinscore
5.41E
Lef1 Control Lef1 Lef1 Wls KO Lef1
Sox2 EdU Sox2 EdU
EdU EdU
DAPI DAPI
Sox2 Sox2
EdU EdU
Condition Celltype CCphase GeneTrajectories
EV4
EV6
Trajectory-DC
Trajectory-LD
Trajectory-CC
Sox2 Other
Sox2
DC G1 LD S
UD G2M EV3 EV2
EV2 EV3
Fig. 4 | GeneTrajectory deconvolves two mixed processes during DC genesis. of the gene graph to visualize three identified gene trajectories (two different
a, Experimental design of extracting skin tissue from a pair of WT and Wls KO combinations of leading nontrivial eigenvectors are displayed). e, Gene bin
embryos at day E14.5 for scRNA-seq. b, FISH images (scale bar = 50 μm) showing plots delineating the dynamics of each process (including DC differentiation, LD
the spatial distribution of Lef1, Sox2, EdU nucleotide and DAPI in the upper differentiation and CC), in which genes along each trajectory are split into seven
dermis of WT and Wls KO. EdU is a nucleotide that is incorporated by cells in equal-sized bins. Gene bin score is defined by the proportion of genes (from
the S phase of the CC. n = 8 (WT) and n = 9 (KO) embryos examined over four each bin) expressed in each cell. Arrows indicate the path of gene distribution
biologically independent experiments with similar results. c, UMAP of cells color progression over the cells. Upper dermis, UD; lower dermis, LD; dermal
coded by cell types, conditions and CC phases. d, DM (Diffusion Map) embedding condensate, DC; cell cycle, CC; wildtype, WT; control, CTL; knockout, KO.
Article https://doi.org/10.1038/s41587-024-02186-3
a b ProportionofcellsinG1
WT KO phase
0.8
WT
DCtrajectory KO
400
800
1,200
1,600
2 4 6
CCtrajectory Stage
c Lef1 level d Proliferation
LDtrajectory
Stage 1 Stage 2 Stage 3 Stage 4 Stage 5 Stage 6 Stage 7
Gene bin
e score
WT
Stage status
Yes
No
Gene bin
f score
KO
Stagestatus
Yes
No
In our real-world example of DC development, we examined Monocle 3 were unsuccessful in generating a reasonable sequence
the order of known markers during DC differentiation (Fig. 6c,d). for these genes. PAGA failed to generate a distinguishable ordering of
GeneTrajectory recovered the correct ordering—Wnt target genes later-stage markers. CellRank incorrectly placed the DC marker (Sox2)
Dkk1/Grem1/Lef1 and Bmp4 emerge first along this process. Dermal Wnt before Gli1 and failed to define the ordering for Bmp4/Lef1 and Cdkn1a.
signaling is known to be required for SHH activation47,48. Accordingly, Moreover, manually regressing out known coexisting biological
the emergence of Wnt target genes is succeeded by the expression of effects (for example, CC) does not guarantee an accurate recovery
SHH target genes (Gli1/Ptch1), which precedes the upregulation of the of gene dynamics when using cell trajectory inference methods. For
CC inhibitor, Cdkn1a, and terminates with the expression of mature DC instance, in our dermal example, regressing out CC effects resulted
markers (Sox2/Sox18/Foxd1). In contrast, SlingShot, Monocle 2 and in persistent incorrect gene orderings for SlingShot, Monocle 2,
Nature Biotechnology
noitroporP 0.6
0.4
sutats
noisserpxE
1
0
sutats
noisserpxE
1
0
0 25 50 75 100 0 25 50 75 100
Gene order Gene order
sutats
noisserpxE
1
0
sutats
noisserpxE
1
0
0 50 100 150 200 250 0 50 100 150 200 250
Gene order Gene order
1.00
0.75
0.50
0.25
0
1.00
0.75
0.50
0.25
0
sutats
noisserpxE
1
0
sutats
noisserpxE
300
200
1
100
0
0 100 200 0 100 200
Gene order Gene order WT
erocs
H 1feL
)%(
+UdE
Condition
Cellnumber
P < 0.0001 P = 0.0008 60
40
20
0
–100 0
KO WT KO
Fig. 5 | Gene dynamics comparative analysis. a, Gene expression status of the DC gene trajectory over the WT cell embedding. Cells involved in the DC
(smoothed) along each gene trajectory in two conditions (0, expressed in fewer differentiation process are stratified into seven different stages. f, Gene bin plots
than 1% of cells; 1, otherwise). b, Change in G1 proportion across seven stages of the DC gene trajectory over the Wls KO cell embedding. Cells involved in the
of DC differentiation. Error bar: mean ± s.e., n = the number of cells in each DC differentiation process are stratified into seven different stages. Violin plots:
stage of the corresponding condition. Dots in stages 5–7 of the KO are omitted n = 8 (WT) and n = 9 (KO) embryos examined over four biologically independent
when the number of cells is ≤10. c, Lef1 transcript levels (H score) quantified experiments. Statistical analysis was performed using two-sided Student’s t test.
by FISH in UD in two conditions. d, Percentage of Edu in UD in two conditions. Lines indicate 75th, 50th and 25th percentiles.
EdU is a nucleotide incorporated by cells in the S phase of CC. e, Gene bin plots
Article https://doi.org/10.1038/s41587-024-02186-3
a Linearprocess c Gene program of DC differentiation Cdkn1a
Sox2, Sox18, Foxd1 DC markers
Gli1 Ptch1 SHH gradient
Dkk1, Grem1 Bmp4,Lef1 Wnt gradient
Highly proliferative Quiescent
Cell arrest
d
GeneTraje P c A to G r S A y l | i D n P M g T S o h n o M o t c o l n e o G 2 c C e l e n e l e l 3 R Tr a a n je k P c A to G r S A y l | i D n P M g T S o h n o M o t c o l n e o G 2 c C e l e n e l e l 3 R Tr a a n j k e P c A to G r S A y l | i D n P M g T S o h n o M o t c o l n e o G 2 c C e l e n e l e l 3 R Tr a a n je k P c A to G r S A y l | i D n P M g T S o h n o M o t c o l n e o 2 c C l e e l l 3 Rank SlingShot
Method
Monocle 2
Monocle 3
PAGA
CellRank
Monocle 3, PAGA and CellRank (Extended Data Fig. 5), suggesting types of questions. Cell trajectory inference aims to define biological
that CC regression is not sufficient to deconvolve the intertwined gene processes by lineages of cells, while gene trajectory inference associ-
dynamics. This underscores the advantage of GeneTrajectory that it is ates each process with a sequence of genes. As demonstrated above,
capable of detecting and disentangling multiple gene programs when when cells participate in concurrent processes, cell trajectory inference
they are present. may fail to deconvolve them. Similarly, when one gene participates in
multiple biological processes, theoretically, it should be placed at the
Discussion joint of gene trajectories. However, if that gene is expressed across
We developed GeneTrajectory, an approach for constructing gene many cells, it may have a small Wasserstein distance to genes that are
trajectories where each trajectory comprises genes organized in homogeneously expressed (uninformative genes). As a result, it will be
a pseudotemporal order that characterizes the transcriptional colocalized with uninformative genes in the gene embedding, causing
dynamics of a specific biological process. GeneTrajectory uses difficulty for GeneTrajectory to distinguish them. Moreover, there
optimal-transport-based gene–gene dissimilarity metrics. These are multiple aspects of our proposed algorithm that could be further
metrics naturally leverage the underlying geometry of the cell–cell refined. For instance, the branch identification procedure requires
graph to reveal a coherent relation among genes that are involved interactive optimization and might exhibit instability if the branches
in progressive processes. Importantly, GeneTrajectory bypasses the differ substantially in length and size. In addition, GeneTrajectory can-
need for constructing cell pseudotime, which is a common requirement not automatically infer the directionality of progression along each
in existing methods. This renders it broadly applicable in scenarios trajectory. The directionality can be determined by checking whether
where cells do not form into clear lineages. the endpoint genes in each trajectory are initial stage markers or ter-
It is worthwhile to note that cell trajectory inference and gene minal stage markers of the corresponding process. Another important
trajectory inference can complement each other to address different aspect is that the idea of using the OT distance between genes over
Nature Biotechnology
yrotcejarTeneG
0.025 0.1 0.2
Method
GeneTrajectory
PAGA|DPT
SlingShot
Monocle 2
Monocle 3
CellRank
500
1,000
2,500
0.05
1.00
0.75
0.50
0.25
0
1.00
0.75
0.50
0.25
0
0 1. . 0 7 0 5 Dkk1 Grem1 Bmp4 Lef1 Gli1 Ptch1 Cdkn1a Sox2 Fox S d o 1 x18
0.50
0.25 0 25 50 75 100
Gene ordering
0
Grem1 Lef1 B C m d p k 4 n1a Sox2 Dkk1 Ptch1 Sox18 Gli1 Foxd1
0 25 50 75 100
Gene ordering
b Cyclicprocess Bmp4 S S o o x1 x 8 2 Foxd1 Ptch1 Lef1 Dkk1 Cdkn1a Gli1 Grem1
0 25 50 75 100
Gene ordering
Bmp4 Ptch1 Foxd1 Dkk1 Cdkn1a Sox2 Sox18 Gli1 Lef1 Grem1
0 25 50 75 100 Gene ordering
Dkk1 Grem1 Foxd1 Lef1 Sox2 Gli1 Cdkn1a Sox18 Ptch1 Bmp4
0 25 50 75 100
Gene ordering
GeneTraje P c A to G r S A y l | i D n P M g T S o h n o M o t c o l n e o G 2 c C e l e e n l e l 3 R T a ra n j k e P c A to G r S A y l | i D n P M g T S o h n o M o t c o l n e o 2 G c C e l e e n l e l 3 R T a ra n j k e P c A to G r S A y l | i D n P M g T S o h n o M o t c o l n e o G 2 c C e l e e n l e l 3 R Tr a a n j k e P c A to G r S A y l | i D n P M g T S o h n o M o t c o l n e o 2 c C l e e l l 3 Rank Gr 0 em1 Dkk1 25 Ptch1 50 Sox2 Gli1 75 Sox18 100
Method Gene ordering
yrotcejarTeneG
0.025 0.05 0.1 0.2
1.00
500
1,000
2,500
GeneTrajectory
0.75
0.50
0.25 0 1.00 Method
0.75 GeneTrajectory PAGA|DPT 0.50 SlingShot
Monocle 2
0.25 Monocle 3 0 CellRank 1.00
0.75
0.50
0.25
0
Fig. 6 | GeneTrajectory outperforms other methods in inferring gene gray boxes correspond to the percentage of nonzero entries in each count
ordering along concurrent processes. a,b, Comparison of GeneTrajectory matrix). c, Schematic representation of the key genes activated during the DC
with other approaches on simulated data (corresponding to the third simulation differentiation process. d, Gene ordering results obtained by different methods
example in Fig. 2) of simultaneous linear process (a) and cyclic process (b), on the DC genesis data. Box plots: the box represents the IQR, with the line inside
with varying sample size and sparsity level of the count matrix (the numbers in the box indicating the median. Whiskers extend to a maximum of 1.5× IQR beyond
the vertical gray boxes correspond to sample size, and those in the horizontal the box, with outliers represented as individual points. IQR, interquartile range.
Article https://doi.org/10.1038/s41587-024-02186-3
cell–cell graphs could have other potential applications beyond the 17. Haghverdi, L., Büttner, M., Wolf, F. A., Buettner, F. & Theis, F. J.
inference of gene programs and their dynamics. Intuitively, after we Diffusion pseudotime robustly reconstructs lineage branching.
compute the gene–gene affinity matrix, we can iteratively improve Nat. Methods 13, 845–848 (2016).
the organization of cells by an OT distance between the cells over the 18. Setty, M. et al. Characterization of cell fate probabilities in
gene–gene graph. This approach warrants further investigation from single-cell data with Palantir. Nat. Biotechnol. 37, 451–460 (2019).
theoretical and practical perspectives. 19. Lönnberg, T. et al. Single-cell RNA-seq and computational
In this work, we demonstrated the utility of GeneTrajectory to analysis using temporal mixture modeling resolves Th1/Tfh fate
unravel gene dynamics using scRNA-seq data. However, our method bifurcation in malaria. Sci. Immunol. 2, eaal2192 (2017).
can be generalized to other single-cell modalities, including but not 20. Tritschler, S. et al. Concepts and limitations for learning
limited to scATAC–seq51 and spatial transcriptomics52. Specifically, developmental trajectories from single cell genomics.
we anticipate that GeneTrajectory can be applied to resolve biologi- Development 146, dev170506 (2019).
cal processes using dual modalities53 at the same time. For instance, 21. Trapnell, C. et al. The dynamics and regulators of cell fate
we can quantify the pairwise distances between the distributions of decisions are revealed by pseudotemporal ordering of single
gene expression and chromatin accessibility, which facilitates under- cells. Nat. Biotechnol. 32, 381–386 (2014).
standing the interplay between epigenetic dynamics and transcrip- 22. Ruijtenberg, S. & van den Heuvel, S. Coordinating cell
tomic dynamics that underlie biological processes. proliferation and differentiation: antagonism between cell cycle
regulators and cell type-specific gene expression. Cell Cycle 15,
Online content 196–212 (2016).
Any methods, additional references, Nature Portfolio reporting sum- 23. Rougny, A., Paulevé, L., Teboul, M. & Delaunay, F. A detailed
maries, source data, extended data, supplementary information, map of coupled circadian clock and cell cycle with qualitative
acknowledgements, peer review information; details of author contri- dynamics validation. BMC Bioinformatics 22, 240 (2021).
butions and competing interests; and statements of data and code avail- 24. Gupta, K. et al. Single-cell analysis reveals a hair follicle dermal
ability are available at https://doi.org/10.1038/s41587-024-02186-3. niche molecular differentiation trajectory that begins prior to
morphogenesis. Dev. Cell 48, 17–31 (2019).
References 25. Sood, P. et al. Modular, cascade-like transcriptional program of
1. Mahdessian, D. et al. Spatiotemporal dissection of the cell cycle regeneration in stentor. eLife 11, e80778 (2022).
with single-cell proteogenomics. Nature 590, 649–654 (2021). 26. Zhu, H., Zhao, S. D., Ray, A., Zhang, Y. & Li, X. A comprehensive
2. Scialdone, A. et al. Computational assignment of cell-cycle stage temporal patterning gene network in Drosophila medulla
from single-cell transcriptome data. Methods 85, 54–61 (2015). neuroblasts revealed by single-cell RNA sequencing.
3. Skinner, S. O. et al. Single-cell analysis of transcription kinetics Nat. Commun. 13, 1247 (2022).
across the cell cycle. eLife 5, e12175 (2016). 27. Li, J. et al. Systematic reconstruction of molecular cascades
4. Cao, J., Zhou, W., Steemers, F., Trapnell, C. & Shendure, J. Sci-fate regulating GP development using single-cell RNA-seq. Cell Rep.
characterizes the dynamics of gene expression in single cells. 15, 1467–1480 (2016).
Nat. Biotechnol. 38, 980–988 (2020). 28. Huizing, G.-J., Peyré, G. & Cantini, L. Optimal transport
5. Qu, R. et al. Decomposing a deterministic path to mesenchymal improves cell–cell similarity inference in single-cell omics data.
niche formation by two intersecting morphogen gradients. Bioinformatics 38, 2169–2177 (2022).
Dev. Cell 57, 1053–1067 (2022). 29. Bellazzi, R., Codegoni, A., Gualandi, S., Nicora, G. & Vercesi, E. The
6. Macaulay, I. C. et al. Single-cell RNA-sequencing reveals a gene mover’s distance: single-cell similarity via optimal transport.
continuous spectrum of differentiation in hematopoietic cells. Preprint at arXiv 10.48550/arXiv.2102.01218 (2021).
Cell Rep. 14, 966–977 (2016). 30. Orlova, D. Y. et al. Earth mover’s distance (EMD): a true metric for
7. Chu, L.-F. et al. Single-cell RNA-seq reveals novel regulators comparing biomarker expression levels in cell populations. PLoS
of human embryonic stem cell differentiation to definitive ONE 11, e0151859 (2016).
endoderm. Genome Biol. 17, 173 (2016). 31. Schiebinger, G. et al. Optimal-transport analysis of single-cell
8. Chen, R., Wu, X., Jiang, L. & Zhang, Y. Single-cell RNA-seq reveals gene expression identifies developmental trajectories in
hypothalamic cell diversity. Cell Rep. 18, 3227–3241 (2017). reprogramming. Cell 176, 928–943 (2019).
9. Street, K. et al. Slingshot: cell lineage and pseudotime inference 32. Zhang, S., Afanassiev, A., Greenstreet, L., Matsumoto, T. &
for single-cell transcriptomics. BMC Genomics 19, 477 (2018). Schiebinger, G. Optimal transport analysis reveals trajectories in
10. Cao, J. et al. The single-cell transcriptional landscape of steady-state systems. PLoS Comput. Biol. 17, e1009466 (2021).
mammalian organogenesis. Nature 566, 496–502 (2019). 33. Cang, Z. & Nie, Q. Inferring spatial and signaling relationships
11. Wolf, F. A. et al. PAGA: graph abstraction reconciles clustering between cells from single cell transcriptomic data. Nat. Commun.
with trajectory inference through a topology preserving map of 11, 2084 (2020).
single cells. Genome Biol. 20, 59 (2019). 34. Moriel, N. et al. NovoSpaRc: flexible spatial reconstruction of
12. Van den Berge, K. et al. Trajectory-based differential expression single-cell gene expression with optimal transport. Nat. Protoc.
analysis for single-cell sequencing data. Nat. Commun. 11, 1201 16, 4177–4200 (2021).
(2020). 35. Demetci, P., Santorella, R., Sandstede, B., Noble, W. S. & Singh, R.
13. Deconinck, L., Cannoodt, R., Saelens, W., Deplancke, B. & Saeys, Y. SCOT: single-cell multi-omics alignment with optimal transport.
Recent advances in trajectory inference from single-cell omics J. Comput. Biol. 29, 3–18 (2022).
data. Curr. Opin. Syst. Biol. 27, 100344 (2021). 36. Coifman, R. R. & Lafon, S. Diffusion maps. Appl. Comput. Harmon.
14. Saelens, W., Cannoodt, R., Todorov, H. & Saeys, Y. A comparison Anal. 21, 5–30 (2006).
of single-cell trajectory inference methods. Nat. Biotechnol. 37, 37. Singer, A. From graph to manifold Laplacian: the convergence
547–554 (2019). rate. App. Comput. Harmon. Anal. 21, 128–134 (2006).
15. Lange, M. et al. CellRank for directed single-cell fate mapping. 38. Tacke, F. & Randolph, G. J. Migratory fate and differentiation of
Nat. Methods 19, 159–170 (2022). blood monocyte subsets. Immunobiology 211, 609–618 (2006).
16. Qiu, X. et al. Reversed graph embedding resolves complex 39. Van de Veerdonk, F. L. & Netea, M. G. Diversity: a hallmark of
single-cell trajectories. Nat. Methods 14, 979–982 (2017). monocyte society. Immunity 33, 289–291 (2010).
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
40. Patel, A. A. et al. The fate and lifespan of human monocyte 49. Hastie, T. J. Generalized Additive Models, pp. 249–307 (Routledge,
subsets in steady state and systemic inflammation. J. Exp. Med. 2017).
214, 1913–1923 (2017). 50. Wood, S. mgcv: Mixed GAM Computation Vehicle with GCV/AIC/
41. Chitu, V. & Stanley, E. R. Colony-stimulating factor-1 in immunity REML Smoothness Estimation (University of Bath, 2012).
and inflammation. Curr. Opin. Immunol. 18, 39–48 (2006). 51. Pott, S. & Lieb, J. D. Single-cell ATAC–seq: strength in numbers.
42. Imhof, B. A. & Dunon, D. Leukocyte migration and adhesion. Genome Biol. 16, 172 (2015).
Adv. Immunol. 58, 345–416 (1995). 52. Ståhl, P. L. et al. Visualization and analysis of gene expression in
43. Ghebrehiwet, B., Hosszu, K. K., Valentino, A., Ji, Y. & Peerschke, E. I. tissue sections by spatial transcriptomics. Science 353, 78–82
Monocyte expressed macromolecular C1 and C1q receptors as (2016).
molecular sensors of danger: implications in SLE. Front. Immunol. 53. Macaulay, I. C., Ponting, C. P. & Voet, T. Single-cell multiomics:
5, 278 (2014). multiple measurements from single cells. Trends Genet. 33,
44. Heger, L. et al. Subsets of CD1c+ DCs: dendritic cell versus 155–168 (2017).
monocyte lineage. Front. Immunol. 11, 559166 (2020).
45. Higashi, N. et al. The macrophage C-type lectin specific for Publisher’s note Springer Nature remains neutral with regard
galactose/N-acetylgalactosamine is an endocytic receptor to jurisdictional claims in published maps and institutional
expressed on monocyte-derived immature dendritic cells. J. Biol. affiliations.
Chem. 277, 20686–20693 (2002).
46. Myung, P., Andl, T. & Atit, R. The origins of skin diversity: lessons Springer Nature or its licensor (e.g. a society or other partner)
from dermal fibroblasts. Development 149, dev200298 (2022). holds exclusive rights to this article under a publishing agreement
47. Chen, D., Jarrell, A., Guo, C., Lang, R. & Atit, R. Dermal β-catenin with the author(s) or other rightsholder(s); author self-archiving
activity in response to epidermal Wnt ligands is required for of the accepted manuscript version of this article is solely
fibroblast proliferation and hair follicle initiation. Development governed by the terms of such publishing agreement and
139, 1522–1533 (2012). applicable law.
48. Fu, J. & Hsu, W. Epidermal Wnt controls hair follicle induction by
orchestrating dynamic signaling crosstalk between the epidermis © The Author(s), under exclusive licence to Springer Nature America,
and dermis. J. Invest. Dermatol. 133, 890–898 (2013). Inc. 2024
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
Methods Step 2. Compute graph-based Wasserstein distances between
Workflow genes. We model the expression level of a gene as a discrete distribu-
The major workflow of GeneTrajectory comprises the following four tion on the cell graph. Specifically, let g(u) represents the expression
i
main steps. Core notations are listed in Table 1. level of gene i in cell u, we then define the distribution of gene i by:
• Step 1—build a cell–cell kNN graph in which each cell is con-
m
nected to its kNNs. Find the shortest path connecting each pair ρi(u)=gi(u)
/
∑gi(v). (1)
of cells in the graph and denote its length as the graph distance v=1
between cells.
• Step 2—compute pairwise graph-based Wasserstein distance It has the following properties: (1) ρi∈ℝm + ; (2) ∑ v ρ i (v) = 1. We then define
between gene distributions, which quantifies the minimum the distance between two genes by the W p distance (1 ≤ p < ∞)
cost of transporting the distribution of a given gene into the between their distributions on the cell graph. Namely, the W p distance
distribution of another gene in the cell graph. δ(p)(ρ i , ρ j ) between gene i and gene j quantifies their dissimilarity.
• Step 3—generate a low-dimensional representation of genes Technically, the W p distance can be computed by solving a discrete
(using diffusion map by default) based on the gene–gene OT mapping over the cell graph. Details are described below.
Wasserstein distance matrix. Identify gene trajectories in a
sequential manner. W p distance formulation and computation. Here we set up some
• Step 4—determine the order of genes along each gene trajectory. mathematical notations as follows: for a graph consisting of m nodes
V = {1, ..., m}, a graph distribution is a non-negative vector ρ∈ℝm
+
Step 1. Construct a cell–cell graph and define graph distances. such that the sum of its elements is equal to one and the distribution
Data preprocessing. The data preprocessing contains the following assigns measure ρ(u) to node u. We assume the graph is equipped
steps: with a graph ground distance d G (u, v) for u, v ∈ V. Specifically, the
graph distance d is used to specify the cost of the OT, that is, the cost
(1) standard preprocessing of the count matrix (m cells and n G
genes). matrix C is defined as Cu,v=dG(u,v) p. As mentioned in Step 1. Construct
a cell–cell graph and define graph distances, we denote the shortest
(2) dimension reduction.
path distance on a kNN graph as d , while the computational method
G
Standard preprocessing—the original count matrix (cell-by-gene) also allows other options of d or even letting the cost matrix take a
G
is first preprocessed by using the standard pipeline in single-cell more general form. For two graph distributions ρ and ρ′, the W
p
distance
analysis, including library normalization, top variable gene selection is defined as:
and scaling.
Dimension reduction—due to the low-rank nature of single-cell δ(p)(ρ,ρ′)= min ⟨F,C⟩ 1/p , (2)
F∈Πρ,ρ′
data, we run dimensionality reduction on the original count matrix to
generate a low-dimensional representation of the cell geometry (cell where Πρ,ρ′ ={F,Fu,v≥0,∑
v
Fu,v=ρ(u)forallu,∑
u
Fu,v=ρ′(v)forallv}
embedding). Commonly used methods include PCA, t-SNE, UMAP and denotes the set of transport plan F that pushes from the source distri-
diffusion maps. By default, we apply PCA for the initial step of dimen- bution ρ to the target distribution ρ′.
sionality reduction and retain the leading n (typically around 30–100)
principal components (PCs). Then we use diffusion map to generate a Improve computational efficiency. In practice, the minimization in
manifold-preserving low-dimensional representation of cells. Specifi- equation (2) can be solved by linear programming, which is compu-
cally, for a given pair of cells u and v, we calculate the Euclidean distance tationally prohibitive on large cell graph and between all the pairs of
d(u, v) between their coordinates of the leading n PCs. We then convert genes. To reduce the cost of computing gene–gene W distances, we
E p
it into an affinity measure a(u, v) using the following Gaussian kernel have designed two strategies to accelerate the computation based
with a local-adaptive bandwidth: on (1) cell graph coarse-graining and (2) gene graph sparsification.
Briefly, cell graph coarse-graining aims to reduce the cell number by
a(u,v)= 1 (exp{− d2 E (u,v) }+exp{− d2 E (u,v) }), u,v=1,⋯,m, aggregating the nearest cells into ‘meta-cells’. Gene graph sparsifica-
2 σ(u) 2 σ(v) 2 tion aims to skip the computation for two gene distributions if they
are very far away from each other at a coarse-grained level, as they are
where σ(u) represents the Euclidean distance between cell u and its unlikely to participate in the same biological process. We note that
kNNs in the PC space. Using a local-adaptive bandwidth allows us to while coarse-graining the cell graph to a crude scale can make it fast
automatically adjust the kernel size based on the local cell density in for computation, it may lose accuracy and compromise the resolution.
the original cell space. After we get the affinities between all pairs of Hence, users should judiciously choose the level of coarse-graining
cells, we apply the diffusion map algorithm and retain its leading n′ based on the capacity of their computing resources.
eigenvectors as a low-dimensional representation of cells for the sub-
sequent cell graph construction, which preserves the geometric (1) Cell graph coarse-graining. We coarse-grain the cell graph by
information of the cell manifold. aggregating m cells into m′ ‘meta-cells’ using the k-means
clustering algorithm. Specifically, let M be the m-by-m′
Cell–cell graph distance computation. When cell geometry presents membership matrix where M(u, a) = 1/∣a∣ if and only if the cell
a low-dimensional manifold structure, the OT should be always done u belongs to the ath subset where ∣a∣ represents the number
across the cell manifold instead of taking a shortcut through empty of cells in that subset, otherwise M(u, a) = 0, then we define an
regions in the ambient space where there are no cells. Here we build updated transport cost matrix C′ on the coarse-grained cell
a cell kNN graph in which we connect each cell to its kNNs in the graph by MTCM. Accordingly, the expression level of a given
dimensionality-reduced cell space. For a given pair of cells u and v, we gene in each ‘meta-cell’ is defined by the sum of its expression
search for the shortest path connecting them in the kNN cell graph and level in all the cells in that subset. Intuitively, this procedure
denote its length as the graph distance d (u, v) between cells u and v. can be viewed as providing an approximation of a cell graph
G
Theoretically, in the limit of a large number of cells, the graph distances with fewer cell nodes.
constructed in this way reveal manifold geodesic distances, which are (2) Gene affinity graph sparsification. We sparsify the gene
the intrinsic cell–cell distances54,55. affinity graph by zeroing out the entries where their pairwise
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
Wasserstein distances are greater than a threshold. The Suppose gene j is selected as the initial node; then only the jth entry
threshold is selected such that affinities associated with of p is equal to 1, while all other entries are zeros. We then construct a
0
distances greater than it will be exponentially small and thus random-walk matrix P by row-wise normalizing the gene–gene affinity
contribute negligibly to the gene affinity graph. The threshold matrix A. Specifically, P is defined by:
is adaptively estimated for each cell using the approximate
Wasserstein distance on a coarse-grained cell graph (strategy 1) P=D−1A,
which allows fast computation.
Specifically, this is formulated in the following way: if we want where D is the degree matrix of A (that is, D is a diagonal matrix where
to construct the gene–gene Wasserstein distance matrix on a D = ∑A ). Calculating p = Pp gives the updated probability mass
ii j ij 1 0
cell graph of an original size m, we first coarse-grain m cells (over genes) after the first time of diffusion. We run the diffusion up
into m′ ‘meta-cells’ using the procedure in strategy 1, to t times (the integer t is a tunable parameter) on the gene graph to
where m′ is a size that can be quickly handled. Based on the get the t-step probability mass p
t
= Ptp
0
. We then select the genes
gene-by-gene Wasserstein distance matrix constructed {j,s.t.,pt(j)>τ0maxj′pt(j′)} as members of the first gene trajectory.
on m′ ‘meta-cells’, we identify the αk nearest neighbors for Here τ
0
is a thresholding parameter, which in practice can be set to be
each gene (where α is the predefined parameter and k is the in the range of 0.02–0.05. Throughout the experiments in this paper,
neighborhood size to construct the local-adaptive kernel for we choose τ = 0.02.
0
computing the diffusion map). Going back to the computation After the genes that belong to the first gene trajectory are extracted,
on the original cell graph, we then only compute the we repeat the abovementioned procedure on the remaining genes
Wasserstein distance between a pair of genes if one of them is to get the second gene trajectory, and then the third, etc. This algo-
included in the other’s αk nearest neighbors. Practically, this rithm allows retrieving a series of gene trajectories successively until
can reduce the running time to 2αk/m of the original, which all detectable trajectories are identified.
computes Wasserstein distances for all pairs of genes.
Step 4. Order genes along each trajectory. To determine the gene
Step 3. Construct gene trajectories. After we obtain the gene–gene ordering along a given gene trajectory, we first extract the correspond-
Wasserstein distance matrix, we convert it into an affinity matrix ing submatrix of gene-by-gene Wasserstein distances as computed in
A using a local-adaptive Gaussian kernel. Specifically, the kernel ‘Step 2. Compute graph-based Wasserstein distances between genes’.
bandwidth for each gene is defined by the distance to its kNN (similar That is, we only focus on the genes that are the members of that trajec-
to ‘Step 1. Construct a cell–cell graph and define graph distances’). tory. We then recompute the diffusion map on the Wasserstein distance
The affinity between gene i and gene j is defined by: submatrix to obtain a new spectral embedding of genes in that trajec-
tory. The first nontrivial eigenvector (EV2) of the new diffusion map
1 δ(p)(ρi,ρj) 2 δ(p)(ρi,ρj) 2 embedding provides an ordering of the genes along that trajectory,
Ai,j=
2
(exp{−
(σi) 2
}+exp{−
(σj) 2
}). (3)
according to the spectral convergence theory of diffusion map36,37. Spe-
cifically, genes are ordered based on ranking their coordinates along EV2.
Here ρ represents the distribution of gene i and σ represents the kth
i i
smallest Wasserstein distance between gene i and other genes. K is an Experiments and analyses
integer parameter to be specified by the user, which controls the size of Here we present the details for the following: (i) simulation experiments
the local neighborhood on the graph (in the sense that A is only large (‘Workflow of gene dynamics simulation’ and ‘Generalizing count
ij
on a subject of genes j that are sufficiently close to i). The affinity matrix model using negative binomial distribution to account for overdisper-
A in equation (3) is used to construct a random walk on the gene–gene sion’), (ii) the biological experiments of mouse embryo skin sample
graph (see below in the bullet point—diffusion of probability mass preparation (‘Experimental details of mouse embryo skin sample
on the gene graph). The random walk constructed from affinity A preparation’), (iii) the analyses on real-world biological datasets (‘Ana-
allows us to apply Diffusion Map to obtain a low-dimensional embed- lytical details of real-world examples’), (iv) comparing Wasserstein
ding of the genes. distance with other canonical metrics for learning gene geometry
Next, extracting gene trajectories is processed in a sequential (‘Comparing the Wasserstein metric to other canonical metrics for
manner when the gene graph exhibits a tree structure. Briefly, we first learning gene geometry’), (v) comparing GeneTrajectory with cell
identify an ‘extremum’ gene as the terminus for the first gene trajec- trajectory methods in terms of gene ordering inference (‘Comparing
tory and then use a diffusion strategy to retrieve genes belonging to GeneTrajectory with cell trajectory methods in terms of gene ordering
that trajectory where the terminus gene serves as the initial node of inference’) and (vi) the robustness evaluation experiments and guide-
the diffusion process. lines on parameter selection (‘Hyperparameter selection guidelines
The details are summarized below: and robustness evaluation’).
• Selection of the initial node. We retain the top d nontrivial
Workflow of gene dynamics simulation. We present the details of
diffusion map eigenvectors as the low-dimensional spectral
our simulation framework for the four examples in Fig. 2, including
embedding of genes, denoted by S. Let S represents the spectral
i
coordinates of gene i, we choose the gene with the largest L (1) a cyclic process,
2
embedding norm max||Si||2 as the starting point of diffusion on (2) a differential process with two lineages,
i (3) a linear differentiation process coupled with CC,
the gene graph. The assumption here is that the gene with the
(4) a multilevel lineage differentiation process coupled with CC.
largest distance from the origin of spectral embedding corres-
ponds to the terminus of a specific gene trajectory. For illustrative purposes, we first introduce the simulation procedure
• Diffusion of probability mass on the gene graph. The diffusion on a simple linear process. The corresponding plots are shown in
is performed by propagating a point mass from the initial node Extended Data Fig. 1a,b.
in the gene graph. Here the initial probability mass p can be
0
formulated as the following unit vector: Illustrative example: a linear process. To demonstrate the simplest
scenario (Extended Data Fig. 1a,b), we simulate a linearly progressive
p0=(0,…,0,1,0,…,0). biological process in [0, T], where t = 0 corresponds to the initial cell
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
state and t = T corresponds to the terminal cell state. We simulate a set each represents the pseudotime along the process of lineage 1 and
of genes {g
i
, i = 1, ⋯, n}, where each g
i
is a non-negative vector in ℝm and lineage 2 differentiation.
g
i
(u) represents the gene expression at cell u, u = 1, ⋯, m. Specifically, if a cell u is along the initial process, then
In this example, we let each cell u be uniquely associated with t(0)≥0,t(1)=t(2)=0. If a cell u is along lineage 1, then t(0)=
u u u u
a pseudotime t
u
, which is i.i.d. uniformly distributed on [0, T]. Our T(0),t(
u
1)≥0,t(
u
2)=0. If a cell u is along lineage 2, then t(
u
0)=
procedure is to first construct for each gene i a continuous function T(0),t(1)=0,t(2)≥0.
u u
λ i (t) on t ∈ [0, T] and then obtain the gene expression vectors g i from Similarly, we generate τ∗ i =(t( i 0)∗,t( i 1)∗,t( i 2)∗) based on the same
λ(t) based on Poisson sampling. Specifically, the simulation procedure procedure as described above to represent the ‘time point’ that
i
consists of the following two steps: gene i reaches the peak of its expected expression level. Here the expec-
• Simulate expected gene expression levels along the process. tation of the expression level of gene i at the time point τ is given by:
For each i, we define a function λ(t), where λ(t) represents the
i i u ||τ−τ∗||2
expected gene expression level of gene i at cell u. The function − i 1
λ i (t) is associated with a ‘peak time’ t∗ i , which represents the time λi(τ)=γ1αie
γ2d2
i . (8)
point when gene i reaches the peak of its expected expression
level. The time t∗ is uniformly sampled from [0, T]. The function Parameters γ 1 , γ 2 , α i and d i are defined based on the same procedure in
λ(t) then takes a i parametric expression as ‘Workflow of gene dynamics simulation’. We then simulate
i
|t−t∗|2 gi(u)∼Poi(λi(τu)), u=1,⋯,m, (9)
i
−
λi(t)=γ1αie
γ2d2
i , (4)
independently across u and i, similarly as in equation (5).
where parameters γ and γ are predefined positive scalars, and α and d Example C: a linear differentiation process coupled with CC. In this
1 2 i i
are positive random variables to account for the variation in duration example (Fig. 2c), we simulate genes for a linear process and a cyclic
length and expression intensity of different genes. Specifically, we draw process independently and then put them together. Specifically, we
d and α from log-normal prior distributions as below: associate each cell u with a generalized pseudotime vector τ comprising
i i
two pseudotime variables τu=(t(
u
1),t(
u
2)). Here t(
u
1)∈[0,T(1)] represents
di∼LN(μd,σ2 d ); αi∼LN(μα,σ2 α ). the pseudotime along the linear process, while t( u 2)∈[0,T(2)] represents
the pseudotime along the cyclic process. The sampling processes to
• Sample gene reads from a Poisson distribution.
generate {t(1)} and {t(2)} are independent.
In reality, the sequencing process is based on capturing molecules u u
Next, we simulate two sets of genes using the procedure same as in
(for example, DNA or RNA fragments) in a random manner. To
‘Workflow of gene dynamics simulation’ but with a different definition
mimic the randomness in the sequencing process, we simulate
of the Poisson rate function λ(τ). Specifically, the first list of genes {g},
i i
g(u) as from a Poisson distribution with a rate λ(t), namely,
i i u 1 ≤ i ≤ n, is simulated with
1
gi(u)∼Poi(λi(tu)), u=1,⋯,m, (5) |t(1)−t(1)∗|2
i
• (
i
O
nd
p
e
ti
p
o
e
n
n
a
d
l)
e
s
n
p
t
a
ly
rs
a
i
c
fy
ro
th
ss
e
a
c
l
o
l u
u n
a
t
n
m
d i
a
.
t
T
r
h
ix
i s
b
g
y
i
s
v
a
e
m
s
p
gi
li
∈
ng
ℝ
n
m +
o
a
n
s
z
d
e
e
r
s
o
i r
e
e
n
d
t
.
ries.
λi(τ)=γ1αie − γ2d2 i . (10)
Finally, we incorporate an optional step to account for sequenc-
ing depth. This is achieved by randomly selecting a specified The second list of genes {g}, n < j ≤ n, is defined with
j 1
number of entries from the original count matrix without
replacement and subsequently zeroing out the remaining min(|t(2)−t(2)∗|,|t(2)+T(2)−t(2)∗|,|t(2)−T(2)−t(2)∗|) 2
j j j
entries. The probability that an entry is selected is proportional −
to its original expression value. This procedure enables us to λj(τ)=γ1αje
γ2d2
j .
generate an artificial dataset with varying levels of missing data. (11)
Example A: a cyclic process. To simulate a biological process with cyclic Notably, the first list of genes contributes to the linear process,
dynamics (for example, CC) (Fig. 2a), based on the former setup of while the second list of genes contributes to the cyclic process.
the linear process simulation, we only need to modify equation (4) as This simu lation results in a cylinder-like cell manifold in the high-
dimensional space.
2
min(|t−t∗|,|t+T−t∗|,|t−T−t∗|)
i i i
λi(t)=γ1αie
− γ2d2
i . (6)
E
In
x a
th
m
i
p
s
l
e
e
x
D
a
:
m
a m
pl
u
e
l t
(
il
F
e
i
v
g
e
.
l
2
li
d
n
)
e
,
a
w
ge
e
d
s
i
i
f
m
fe
u
re
l
n
a
t
t
i
e
a t
g
i
e
o
n
n
e
p
s
r o
f
c
o
e
r
s s
a
c
t
o
w
u
o
p
-
l
l
e
e
d
v
w
e
i
l
t
t
h
r
C
e
C
e-
.
structured process and a cyclic process independently and then put
All other details are the same as in ‘Workflow of gene dynamics them together. In the general case, let us consider simulating a n-level
simulation’. bifurcating process, in which the initial process P first splits into two
0
lineages (P and P), then each lineage proceeds independently and fur-
1 2
Example B: a differentiation process with two lineages. To simulate a ther splits into another two sublineages (P and P , P and P ), and each
1.1 1.2 2.1 2.2
biological process with a bifurcating structure (for example, myeloid sublineage divides again in an iterative manner until a n-level tree struc-
lineage differentiation) (Fig. 2b), we represent the underlying cell state ture is generated. At the same time, all the cells are involved in a cyclic
by a generalized pseudotime vector τ comprising three pseudotime process. Here each cell u can be associated with a generalized pseudot ime
variables vector τ comprising 2n pseudotime variables τu=(t(
u
0),t(
u
1),…,t(
u
2n)),
each of the first 2n − 1 pseudotime variables corresponds to a pseudot ime
τu=(t( u 0),t( u 1),t( u 2)). (7) location along P0,P1,P2,P1.1,P1.2,P2.1,P2.2,…,P⏟1.⎵1⏟…⎵⏟.1,…,P2⏟.⎵2⏟…⎵⏟.2 , resp ect i-
n n
Here t(0)∈[0,T(0)] represents the pseudotime along the initial vely. For generating the instances of these 2n − 1 pseudotime variables,
u
process before lineage differentiation, t(1)∈[0,T(1)],t(2)∈[0,T(2)] we adopt the similar framework as applied in ‘Workflow of gene
u u
Nature Biotechnology
Article https://doi.org/10.1038/s41587-024-02186-3
dynamics simulation’ by requiring that when a cell u is along a daughter EdU administration. To assess proliferation, EdU was administered
lineage, its pseudotime variables corresponding to all the parent to pregnant mice intraperitoneally (25 μg gm−1) and embryos were
processes are set to the largest possible values, and its pseudotime collected after 1.5 h.
variables corresponding to other processes (excluding the daughter
lineage itself) are all set to 0. Besides, t(2n) represents the pseudotime In situ hybridization. In total, 10% of formalin-fixed paraffin-embedded
u
of cell u in the cyclic process, which is independent from the other 2n − 1 (FFPE) whole embryos were used for histological analysis. FFPE
pseudotime variables. specimens were subsectioned at 10 μm thickness. The RNAscope
Next, we simulate two sets of genes using the procedure same as in Multiplex Fluorescent Detection Kit v2 (ACDBio, 323110) was used for
‘Workflow of gene dynamics simulation’ but with a different definition single-molecule fluorescence in situ hybridization (FISH) according
of the Poisson rate function λ(τ). Specifically, the first list of genes {g}, to the manufacturer’s protocol. Briefly, subsections were deparaffi-
i i
1 ≤ i ≤ n, is simulated with nized and permeabilized with hydrogen peroxide followed by antigen
1
retrieval and protease treatment before probe hybridization. After
(||τ−τ∗
i
||1−|t(2n)−t(
i
2n)∗|) 2 hybridization, amplification and probe detection were done using
− the Amp 1–3 reagents. Probe channels were targeted using the pro-
λi(τ)=γ1αie
γ2d2
i . (12) vided HRP-C1-3 reagents and TSA (tyramide signal amplification)
fluorophores—Cy3 (Akoya Biosciences, NEL744001KT), Cy5 (Akoya
The second list of genes {g}, n < j ≤ n, is defined with Biosciences, NEL745001KT) and fluorescein (Akoya Biosciences,
j 1
NEL741001KT). EdU staining was done using the Click-it EdU Imaging Kit
min(|t(2n)−t(2n)∗|,|t(2n)+T(2n)−t(2n)∗|,|t(2n)−T(2n)−t(2n)∗|) 2 Alexa 488 (Life Technologies, c10338) according to the manufacturer’s
j j j
− instructions. Nuclear counter-stain was done using Hoechst 33342
λj(τ)=γ1αje
γ2d2
j . (Invitrogen, H3570) before mounting with SlowFade Mountant. RNA
(13) scope probes used (ACDBio)—Mm-Lef1 (441861) and Mm-Sox2 (401041).
Notably, the first list of genes contributes to the tree-structured Microscopy. FISH paraffin-embedded images were acquired using the
differentiation process, while the second list of genes contributes to Leica TCS SP8 Gated STED 3X super-resolution confocal microscope
the cyclic process. This simulation results in a coral-like cell manifold with a ×40 oil immersion (Numerical Aperture 1.3) objective lens,
in the high-dimensional space. scanned at 5 μm thickness, 1,024 × 1,024 pixel width, 400 Hz.
Details of the simulation examples. For the examples shown in Fig. 2, Single-cell dissociation. Embryonic dorsolateral/flank skin was micro-
the evaluation outputs can be found in Supplementary Table 1. Each dissected from E14.5 littermate control and mutant embryos and dis-
example was tested through ten replicates. Specifically, in the first sociated into a single-cell suspension using 0.25% trypsin (Gibco,
example, we simulated 1,000 cells, 500 genes underlying the cyclic Life Technologies) for 20 min at 37 °C. After genotyping, two to three
process. In the second example, we simulated 1,000 cells, 500 genes embryos were pooled by condition. Single-cell suspensions were then
for the initial process and 250 genes for each daughter lineage process. stained with DAPI (Thermo Fisher Scientific, NBP2-31156) just before
In the third example, we simulated 5,000 cells, 500 genes for the linear fluorescence-activated cell sorting.
process and 500 genes for the cyclic process. In the fourth example, we
simulated 10,500 cells, 400 genes for the cyclic process and 200 genes Fluorescence-activated cell sorting. DAPI-excluded live skin cells were
for each sublineage process. For all these samples, we adopted the fol- sorted on a BD FACS Aria II (BD Biosciences) sorter with a 100 μm noz-
lowing model parameters: γ = 25, μ = 0, μ = 0, σ = 0.25, σ = 0.25. We zle. Cells were sorted in bulk and submitted for 10X Genomics library
1 d α d α
chose T = 10 in the fourth example, while T = 15 in the other examples. preparation at 0.75–1.0 × 106 ml−1 concentration in 4% fetal calf serum/
We chose γ = 2 for simulating the cyclic process, while γ = 8 for simu- phosphate buffered saline (FCS/PBS) solution.
2 2
lating the other processes. In simulation experiments, genes along a
circular trajectory are ordered by their angular coordinates of the first H-score quantification. For quantification based on FISH, cells with
two nontrivial diffusion map eigenvectors. 4–5 dots were considered positive (according to the RNAScope manu-
facturer’s instructions) and subsections from a total of n = 4 different
Generalizing count model using negative binomial distribution to embryos were examined. To measure RNA expression levels, H scores
account for overdispersion. To investigate the impact of dispersion were calculated according to ACDBio manufacturer’s instructions—a
on the performance of GeneTrajectory, specifically in terms of gene cell with 0 dot is scored 0, 1–3 dots is scored 1, 4–9 dots is scored 2,
ordering, we performed a negative binomial variant of our second 10–15 dots and/or less than 10% clustered dots is scored 3 and more than
and third simulation experiments in Fig. 2. For each dataset, we 15 dots and/or more than 10% clustered dots is scored 4; then the
simulated three distinct sparsity levels (5%, 10% and 20%). For each final H score of a given cell type A is calculated by summing the (% cells
sparsity level, we tested four different dispersion levels (parameter- scored B within all cells in A) × B for score B in 0–4.
ized by θ), each comprising ten technical replicates. A lower θ value
indicates higher dispersion. We evaluated the consistency between scRNA-seq and library preparation. Chromium Single Cell 3′ GEM
the inferred gene ordering and the ground truth by calculating Library and Gel Bead Kit v3.1 (PN-1000121) were used according to the
their Spearman correlation (Supplementary Fig. 1). It shows that manufacturer’s instructions in the Chromium Single Cell 3′ Reagents
GeneTrajectory exhibits remarkable stability across all sparsity and Kits V3.1 User Guide. After cDNA libraries were created, they were
dispersion levels. subjected to Novaseq 6000 (Illumina) sequencing. For each scRNA-seq
experiment, control and littermate mutant samples were prepared
Experimental details of mouse embryo skin sample preparation. in parallel at the same time, pooled and sequenced on the same lane.
Mice. K14Cre (ref. 56) mice were bred to Wntlessfl/fl (ref. 57) mice. A
random population of both male and female embryos was used for all Analytical details of real-world examples. Human myeloid dataset
experiments. All procedures involving animal subjects were performed analysis. Myeloid cells were extracted from a publicly available 10×
under the approval of the Institutional Animal Care and Use Committee scRNA-seq dataset (https://support.10xgenomics.com/
of the Yale School of Medicine. single-cell-gene-expression/datasets/3.0.0/pbmc_10k_v3). QC (quality
Nature Biotechnology
