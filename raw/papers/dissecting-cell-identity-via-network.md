---
source_path: /mnt/c/Users/Administrator/Zotero/storage/4MFFDBC3/Kamimoto 等 - 2023 - Dissecting cell identity via network inference and.pdf
ingested: 2026-04-23
sha256: 4f0cae76d5cfcca9
---

Article
Dissecting cell identity via network
inference and in silico gene perturbation
https://doi.org/10.1038/s41586-022-05688-9 Kenji Kamimoto1,2,3, Blerta Stringa1,3, Christy M. Hoffmann1,2,3, Kunal Jindal1,2,3,
Lilianna Solnica-Krezel1,3 & Samantha A. Morris1,2,3 ✉
Received: 4 January 2022
Accepted: 28 December 2022
Cell identity is governed by the complex regulation of gene expression, represented
Published online: 8 February 2023
as gene-regulatory networks1. Here we use gene-regulatory networks inferred from
Open access
single-cell multi-omics data to perform in silico transcription factor perturbations,
Check for updates simulating the consequent changes in cell identity using only unperturbed wild-type
data. We apply this machine-learning-based approach, CellOracle, to well-established
paradigms—mouse and human haematopoiesis, and zebrafish embryogenesis—
and we correctly model reported changes in phenotype that occur as a result of
transcription factor perturbation. Through systematic in silico transcription factor
perturbation in the developing zebrafish, we simulate and experimentally validate a
previously unreported phenotype that results from the loss of noto, an established
notochord regulator. Furthermore, we identify an axial mesoderm regulator, lhx1a.
Together, these results show that CellOracle can be used to analyse the regulation of
cell identity by transcription factors, and can provide mechanistic insights into
development and differentiation.
The expansion of single-cell technologies into perturbational omics is cell fate regulation governed by TFs. Furthermore, we apply CellOracle
enabling the development of methods to characterize cell identity. For to systematically perturb TFs across zebrafish development, recover-
example, single-cell RNA sequencing (scRNA-seq) coupled with pooled ing known and putative regulators of cell identity. Focusing on axial
CRISPR screens offers much promise for analysing the genetic regula- mesoderm, we predict and validate a prechordal plate phenotype after
tion of cell identity2–4, but cannot be readily used in many biological con- loss of function (LOF) of the prototypical notochord regulator, noto.
texts. Computational methods to simulate single-cell phenotypes after Moreover, we also simulate and validate a role for the TF lhx1a in the
perturbation are emerging, although many approaches still require development of axial mesoderm. Together, these results show that
experimental perturbation data for model training, and thus their scale CellOracle can be used to infer and interpret cell-type-specific GRN
and application are limited5. Moreover, previous deep-learning-based configurations at high resolution, enabling mechanistic insights into
models represent a ‘black box’, which restricts the interpretation of the regulation of cell identity. CellOracle code and documentation are
gene-regulatory mechanisms that underlie the simulated biological available at https://github.com/morris-lab/CellOracle and data can be
events. In this respect, gene-regulatory network (GRN) modelling explored at https://celloracle.org.
approaches are promising as they reconstruct systematic gene–gene
associations from unperturbed single-cell omics data6–11. However,
In silico gene perturbation using CellOracle
previous methods for analysing GRNs largely focus on the static net-
work structure, and determining how a static GRN governs cell identity To gain mechanistic insight into the regulation of cell identity, we
during dynamic biological processes therefore remains a challenge. developed an in silico strategy to simulate changes in cell identity upon
Scalable and interpretable approaches are required to understand how TF perturbation. CellOracle uses custom GRN modelling (Extended
gene-regulatory mechanisms relate to observed complex single-cell Data Fig. 1a) to simulate global downstream shifts in gene expression
phenotypes. following knockout (KO) or overexpression of TFs. These simulated
Here we present a strategy that overcomes these limitations by values are converted into a vector map of transitions in cell identity,
combining computational perturbation with GRN modelling. Cel- which enables simulated changes in cell identity to be intuitively visu-
lOracle integrates multimodal data to build custom GRN models that alized within a low-dimension space (Fig. 1a and Methods). In silico
are specifically designed to simulate shifts in cell identity following perturbation involves four steps. (1) Cell-type- or cell-state-specific
transcription factor (TF) perturbation, providing a systematic and GRN configurations are constructed using cluster-wise regularized
intuitive interpretation of context-dependent TF function in regulat- linear regression models with multi-omics data. (2) Using these GRN
ing cell identity. We apply CellOracle to well-characterized biological models, shifts in target gene expression in response to TF perturba-
systems: haematopoiesis in mice and humans; and the differentiation tion are calculated. This step applies the GRN model as a function to
of axial mesoderm into notochord and prechordal plate in zebrafish. propagate the shift in gene expression rather than the absolute gene
In haematopoiesis, we show that CellOracle recapitulates well-known expression value, representing the signal flow from TF to target gene.
1Department of Developmental Biology, Washington University School of Medicine in St Louis, St Louis, MO, USA. 2Department of Genetics, Washington University School of Medicine in St Louis,
St Louis, MO, USA. 3Center of Regenerative Medicine, Washington University School of Medicine in St Louis, St Louis, MO, USA. ✉e-mail: s.morris@wustl.edu
742 | Nature | Vol 614 | 23 February 2023
b
c d e
GMPs Monocytes GM lineage differentiation
GMPs
inhibited
MEPs
MEPs
MEP
differentiation
Granulocytes promoted
PS
Erythrocytes 1 × 10–3
–5 0 5
f g MPP i
GMP differentiation promoted Gata1
0.8 Spi1
Gene annotation MEP GMP 0.6 ME lineage
differentiation
GM lineage h differentiation
ME lineage LLaattee GGMMPP Late GMP 0.4 Both GM and ME
differentiation,
differentiation maintenance
inhibited Other or unknown 0.2
PS 0 1 × 10–3 GGrr D aann if uu fe lloo re cc n yyyy t tt i ee ation in G hi r b a i n te u d lo f c ro y m te 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
–5 0 5 late GMP to early granulocyte Negative PS sum in GM lineage
This signal is propagated iteratively to calculate the broad, down- to a two-dimensional (2D) vector, allowing for more robust predic-
stream effects of TF perturbation, allowing the global transcriptional tions against noise (Extended Data Fig. 1e). We purposefully limit the
‘shift’ to be estimated (Extended Data Fig. 1b–d). (3) The cell-identity simulation output data to a 2D vector representing the predicted shift
transition probability is estimated by comparing this shift in gene in cell identity because our goal is to model changes in identity rather
expression to the gene expression of local neighbours. (4) The transi- than predicting absolute changes in gene expression levels. Further
tion probability is converted into a weighted local average vector to details of the CellOracle algorithm are provided in the Methods, includ-
represent the simulated directionality of cell-state transition for each ing validation of the range of simulated values; null or randomized
cell following perturbation of candidate TFs. In the final calculation model analysis; and hyperparameter evaluation (Supplementary
step, the multi-dimensional gene expression shift vector is reduced Figs. 2–10).
Nature | Vol 614 | 23 February 2023 | 743
egaenil
EM
ni mus
SP
evitageN
Monocytes
Mk
GMPs
MEPs
Granulocytes
Erythrocytes
FA1
2AF
scRNA-seq data
Late GMPs
Cluster 1 configuration
Gene C perturbation
Gene B perturbation
Cluster 1 Cluster 2 configuration
Cluster 2
Cluster 3
scATAC-seq data
Cluster 3
Co-accessible peaks
Zbtb7a E2f4
Klf1
Gata1 Smarcc1
Bdp1 Nfe2l2 Smarca5 Ybx1 Smarcc2Cbx5
Nfia Lmo2 Nfatc3 Elf1*
Zbtb1 Ezh2 Cxxc1
Nr3c1 Gfi1b Brf1 Bptf Rreb1 Myc
Arhgef12 Stat1Myb
Stat5a Bcl11a Runx1 Chd2 Cux1Etv6 Nfya Nfic
Irf9 Nfe2
Irf2 Foxp1 N R fk u b n 1 x2 Herpud1 Fli1 Spi1
Elk3
Ets1 CebpeIrf1Stat3Mef2c Cebpa Irf8
Rel Gfi1Tcfec Klf4
...
a Input data Calculation step 1 Calculation step 2 Output
Construct cell-state- In silico gene Cell-state transition vector
specific GRN models perturbation with after gene perturbation
GRN models
Gene A perturbation
Signal propagation
using GRN models
and scRNA-seq data
Fig. 1 | Overview of CellOracle and application to haematopoiesis. cell are shown in the inset. e, Spi1 KO simulation vector field with perturbation
a, Simulation of cell-state transitions in response to TF perturbation. First, scores (PSs). f, Gata1 KO simulation with perturbation scores. g, Schematic of
CellOracle constructs custom transcriptional GRNs using scRNA-seq and Spi1–Gata1 lineage switching. MPP, multipotent progenitor. h, Detail of Gata1
scATAC-seq data (left). Accessible promoter and enhancer peaks from simulation for the granulocyte branch. Left, cell-state transition vectors for
scATAC-seq data are then combined with scRNA-seq data to generate each cell. Right, summarized vectors. i, Systematic KO simulation result of 90
cluster-specific GRN models (middle). CellOracle simulates the change in cell TFs in the GM and ME lineage is summarized as a scatter plot of the sum of
state in response to a TF perturbation, projecting the results onto the cell negative perturbation scores (shown in log scale). Dashed lines represent
trajectory map (right). b, Force-directed graph of 2,730 myeloid progenitor cut-off values corresponding to false-positive rate (FPR) = 0.01. Genes are
cells from Paul et al.16. Twenty-four cell clusters (Louvain clustering) were classified into four categories on the basis of their previously reported functions
organized into six main cell types. Mk, megakaryocytes. c, Differentiation (Supplementary Table 2). The asterisk refers to Supplementary Fig. 11, where
vectors for each cell projected onto the force-directed graph. d, CellOracle we expand on the predicted phenotype. All scores can be explored through our
simulation of cell-state transition in Spi1 KO simulation. Summarized cell-state web application (https://celloracle.org).
transition vectors projected onto the force-directed graph. Vectors for each
Article
applying CellOracle to a 2,730-cell scRNA-seq atlas of myeloid pro-
GRN inference and benchmarking with CellOracle genitor differentiation16 (Fig. 1b and Extended Data Fig. 3a). We con-
The CellOracle GRN model must represent regulatory connections as structed GRN models for each of the 24 myeloid clusters identified,
a directed network edge to support signal propagation in response to representing megakaryocyte and erythroid progenitors (MEPs) and
TF perturbation. Thus, we developed a custom GRN modelling method granulocyte–monocyte progenitors (GMPs), differentiating toward
motivated by previous approaches that incorporate promoter and erythrocytes, megakaryocytes, monocytes and granulocytes (Fig. 1c).
TF-binding information with scRNA-seq data to infer a directional GRN7 To test whether the CellOracle simulation could recapitulate known TF
(Extended Data Fig. 1a and Methods). First, using single-cell chromatin regulation of cell identity, we performed in silico gene perturbation
accessibility data (single-cell assay for transposase-accessible chroma- using the inferred GRNs, and compared the CellOracle KO simulation
tin using sequencing; scATAC-seq), we incorporate flexible promoter results with previous biological knowledge and ground-truth KO data.
and enhancer regions, encompassing proximal and distal regulatory First, Spi1 (also known as PU.1) and Gata1 KO simulation is used to
elements. This initial step uses the transcriptional start site (TSS) data- illustrate the CellOracle in silico perturbation analysis. The TF perturba-
base (http://homer.ucsd.edu/) and Cicero, an algorithm that identifies tion simulation is visualized as a vector map on the 2D trajectory space
co-accessible scATAC-seq peaks, to distinguish accessible promoters (Fig. 1d and Supplementary Video 1), representing a potential shift in
and enhancers12. The DNA sequence of these elements is then scanned cell identity in response to TF perturbation. To enable the simulation
for TF-binding motifs, generating a ‘base GRN structure’ of all potential results to be assessed systematically and objectively, we also devised
regulatory interactions in the species of interest (Extended Data Fig. 1a, a ‘perturbation score’ metric, which compares the directionality of the
left). This process is beneficial as it narrows the scope of possible regula- perturbation vector to the natural differentiation vector (Extended
tory candidate genes before model fitting (below) and helps define the Data Fig. 4). A negative perturbation score suggests that TF KO delays
directionality of regulatory edges in the GRN. To support GRN infer- or blocks differentiation (Extended Data Fig. 4b–d, purple). Conversely,
ence without requiring sample-specific scATAC-seq datasets, we have a positive perturbation score suggests that the differentiation and KO
assembled a base GRN from a mouse scATAC-seq atlas13. We have also simulation vectors share the same direction, indicating that loss of TF
created general promoter base GRNs for ten commonly studied spe- function promotes differentiation (Extended Data Fig. 4b–d, green).
cies (Supplementary Table 1 and Methods). These base GRNs are built Spi1 KO simulation yielded positive perturbation scores for MEPs,
into the CellOracle library and provide an alternative solution when whereas GMPs had negative perturbation scores (Fig. 1e), suggesting
scATAC-seq data are unavailable. that Spi1 KO inhibits GMP differentiation and promotes MEP differentia-
In the second step of CellOracle GRN inference, we use scRNA-seq tion. Inverse perturbation score distributions were produced for the
data to identify active connections in the base GRN, generating Gata1 KO simulation (Fig. 1f). Comparing these predictions to previous
cell-type- or cell-state-specific GRN configurations for each cluster. reports17,18: PU.1 directs commitment to the neutrophil and monocyte
In this step, we build a machine-learning model to predict the expres- lineages19,20, whereas GATA1 promotes the differentiation of erythroid
sion of target genes on the basis of TF expression (Extended Data Fig. 1a, cells21 and eosinophil granulocytes22–24. Overall, CellOracle accurately
right). Because CellOracle uses genomic sequences and information simulated the myeloid lineage switching governed by Gata1 and Spi1
on TF-binding motifs to infer the base GRN structure and directional- (refs. 15,25–27; Fig. 1g), including a relatively mild Gata1 KO phenotype in
ity, it does not need to infer the causality or directionality of the GRN early granulocyte differentiation (Fig. 1h), which cannot be inferred
from expression data. This approach allows CellOracle to adopt a from the low levels of Gata1 expression in granulocytes (Extended
relatively simple modelling method for GRN inference—a regularized Data Fig. 3d). However, CellOracle did not detect a previously reported
linear machine-learning model. Crucially, this strategy enables the depletion of erythrocyte progenitors after Spi1 KO27,28, probably owing
above signal propagation to simulate TF perturbation. To support the to changes in cell proliferation that are not predicted by the method.
use of a linear model, the gene expression matrix of scRNA-seq data We next evaluated eight additional TFs that have established roles in
is divided into several clusters in advance so that a single data unit myeloid differentiation: Klf1 (also known as Eklf), Gfi1b, Fli1, Gfi1, Gata2,
for each fitting process represents a linear relationship rather than Lmo2, Runx1 and Irf8 (refs. 15,29). CellOracle also correctly reproduced
non-linear or mixed regulatory relationships. Furthermore, a Bayesian their reported KO phenotypes (Extended Data Figs. 5 and 6), which we
or bagging strategy enables the certainty of connection to be presented extended to two additional datasets of mouse and human haematopoie-
as a distribution; this allows weak or insignificant connections to be sis (Extended Data Figs. 7 and 8 and Supplementary Figs. 13 and 14). In
removed from the base GRN (Extended Data Fig. 1a, right), producing addition, we scaled up our simulation to all TFs that passed filtering
a cell-type- or cell-state-specific GRN configuration. (Methods) to systematically perturb 90 TFs in the dataset in the context
To benchmark our GRN inference method, we generated a com- of granulocyte–monocyte (GM) and megakaryocyte–erythroid (ME)
prehensive transcriptional ground-truth GRN using 1,298 chromatin differentiation. The reported cell-fate-regulatory functions of these
immunoprecipitation followed by sequencing (ChIP–seq) datasets for TFs fall into three major categories: (1) ME lineage differentiation; (2)
80 regulatory factors across 5 different tissues14. In addition to bench- GM lineage differentiation; and (3) ME and GM lineage differentiation
marking against diverse GRN inference algorithms, we also assessed the and maintenance of haematopoietic stem cell (HSC) identity (Sup-
performance of our approach using different base GRNs, data sources plementary Table 2). We ranked the TFs on the basis of the sum of the
and cell downsampling (Extended Data Fig. 2). Inference performance negative perturbation score in the KO simulation, representing the
as assessed by the area under the receiver operating characteristic potential of a TF potential to promote differentiation (Methods and
(AUROC) ranged from 0.66 to 0.85 for the promoter base GRN and Extended Data Fig. 3f).
0.73 to 0.91 for the scATAC-seq base GRN. Altogether, this benchmark- To summarize this systematic TF perturbation, the summed negative
ing demonstrates the accuracy of our transcriptional GRN modelling perturbation scores are shown on a scatter plot (Fig. 1i). The dashed
method with a diverse range of data sources. Combined with our signal lines represent cut-off values calculated with a randomized vector
propagation strategy, CellOracle can effectively interrogate network (Extended Data Fig. 3g). The distribution of negative perturbation
biology and cell-identity dynamics through in silico perturbation. score sums for all TF KOs was highly consistent with known TF functions
in differentiation. For example, TFs involved in ME lineage differentia-
tion are enriched on the top left side of the scatter plot. By contrast,
GRN analysis and TF KO in haematopoiesis
GM differentiation factors are found at the bottom right. TFs that
For validation, we aimed to reproduce known TF regulation of mouse regulate both lineages are located on the top right side, whereas the
haematopoiesis, a well-characterized differentiation paradigm15, by lower-ranked factors are enriched for TFs that have not been reported
744 | Nature | Vol 614 | 23 February 2023
b
to regulate blood differentiation (Fig. 1i). Overall, 85% of the top 30 TFs We further validated CellOracle simulation by focusing on several
ranked by this objective, systematic perturbation strategy are reported genes for which experimental KO scRNA-seq data are available: Cebpa,
regulators of myeloid differentiation (Supplementary Table 2). Of Cebpe and Tal1 (refs. 16,30). Cebpa is necessary for the initial differentia-
the remaining TFs, several have no reported phenotypes in haema- tion of GMPs, and its loss leads to a marked decrease in differentiated
topoiesis at present, and therefore represent putative regulators. myeloid cells, accompanied by an increase in erythroid progenitors. By
We note that the negative perturbation score metric does not always contrast, Cebpe is not required for initial GMP differentiation, but it is
convey all information of the vector field, which might oversimplify the essential for the subsequent maturation of GMPs into granulocytes16.
role of a TF. For example, Elf1 has a negative perturbation score in both Notably, when we compare the simulation results to the experimental
the ME and the GM lineage, and its function is unclear on the summa- KO cell distribution, we must again consider the effects of TF pertur-
rized perturbation score plot; however, closer inspection of the vector bation in the context of natural cell differentiation (Fig. 2a). Thus, we
reproduced its reported phenotype in the ME lineage, highlighting performed a Markov random walk simulation based on the differentia-
the importance of investigating the simulation output (Supplemen- tion and simulation vectors to estimate how TF perturbation leads to
tary Fig. 11). Finally, we directly compared the output of CellOracle to changes in cell distribution (Supplementary Fig. 17 and Methods). For
existing methods for identifying regulatory TFs using gene expres- Cebpa, CellOracle simulation predicted that differentiation is inhibited
sion and chromatin accessibility, demonstrating the unique insights at GMP–late GMP clusters, whereas early erythroid differentiation is
into context-dependent TF regulation that CellOracle can provide promoted (Fig. 2b). The simulation recapitulates the experimental cell
(Supplementary Figs. 15 and 16). distribution (Fig. 2b,d). For Cebpe, CellOracle again correctly modelled
Nature | Vol 614 | 23 February 2023 | 745
noitalumis
OK
apbeC
Differentiation Case 1: positive PS
vector
Simulation
vector
PS
Expected
outcome
Pseudotime
ytisned
lleC
ytisned
lleC
a Case 2: negative PS
Pseudotime
ytisned
lleC
Case 3: mixed PS
Pseudotime
ytisned
lleC
Case 4: mixed PS
Pseudotime
Vector field PS Markov simulation
GMPs Late GMPs MPP
MEPs
MEP GMP
Ery Mk Gra Mo
Granulocytes
Cebpa KO Cebpa KO
promotes inhibits
1 × 10–2 MEP and Ery differentiation
Erythrocytes –1 0 1 Low High differentiation at GMP stage
c
GMPs Late GMPs
MPP
MEPs
MEP GMP
Early
granulocytes
Ery Mk Gra Mo
Granulocytes Cebpe KO induces
differentiation inhibition
Erythrocytes –1 0 1 1 × 10–2 Low High e b a e r t l w y e g e r n a n la u t lo e c G y M te P s t a a n g d e
d
WT cell density Cebpa KO experiment Cebpe KO experiment
KKDDEE 1× 10–8 0.51.0
noitalumis
OK
epbeC
GMP differentiation inhibited
MEP
differentiation
promoted
Granulocyte
differentiation
inhibited
e
Cebpa KO
Cebpe KO
noitroporP
Differentiation Differentiation Inhibition Promotion Promotion Inhibition
promoted inhibited
High cell density CCeellll Cell Cell
at the later time point aaccccuummuullaattiioonn accumulation accumulation
No
increase
0.5 Genotype
0.4 WT
0.3
0.2
0.1
0
Ear G L ly a M g te P r a G s n G M u r lo P a c n s y u t M l e o s c o M y n t o e e c g s y a t k e M a s r E y E o P ry c s t y h t r e o s cytes
Fig. 2 | Validation of CellOracle using experimentally measured cell density cell-state transition vectors, perturbation scores and estimated cell density
in Cebpa and Cebpe KOs in haematopoiesis. a, Biological interpretation of (Markov simulation). Right, schematics of simulated phenotype. Ery,
perturbation scores (estimation of cell density based on perturbation score). erythrocyte. d, Ground-truth experimental cell density plot of wild-type (WT)
Case 1: the differentiation and perturbation simulation vectors share the same cells, Cebpa KO cells and Cebpe KO cells in the force-directed graph embedding
direction, indicating a population shift towards a more differentiated identity. space. Estimated kernel density data are shown as a contour line on a scatter
Case 2: the two vectors are opposed, suggesting that differentiation is inhibited. plot to depict cell density. e, Cell-type proportions in the WT and ground-truth
Case 3: predicted inhibition precedes promotion; thus, cells will be likely to KO samples. Gra, granulocyte; KDE, kernel density estimation; Mo, monocyte.
accumulate. b,c, CellOracle Cebpa KO (b) and Cebpe KO (c) simulations showing
Article
d e f
Notochord
Early notochord
differentiation inhibited
Prechordal plate
High
Early AM
Low
Prechordal plate
differentiation promoted
the inhibition of differentiation at the entry stage of granulocyte dif- obtaining information on TF-binding motifs from the Danio rerio
ferentiation (Fig. 2c), consistent with experimental KO data (Fig. 2d). CisBP motif database (Methods). Our benchmarking has shown that
We also analysed a single-cell atlas of mouse organogenesis30 to this approach produces reliable GRN inference (Extended Data Fig. 2).
simulate the loss of Tal1 function (Extended Data Fig. 9a–d). CellOra- After preprocessing and GRN inference, we performed KO simulations
cle reproduced the inhibited differentiation of haematoendothelial for all TFs with inferred connections to at least one other gene (n = 232
progenitors in the Tal1 KO30 (Extended Data Fig. 9e–h). In addition, ‘active’ TFs; Methods). The results of these simulations across all devel-
CellOracle showed that loss of Tal1 in later stages of erythroid differ- opmental trajectories can be explored at https://www.celloracle.org.
entiation does not block cell differentiation (Extended Data Fig. 9i,j), Our systematic TF KO simulation provides a valuable resource for
consistent with previous conditional Tal1 KO experiments at equivalent identifying regulators of early zebrafish development and enables
stages31. Together, these results show that CellOracle effectively simu- candidates to be prioritized for experimental validation. To further
lates cell-state-specific TF function, corroborating previous knowl- examine this comprehensive perturbation atlas, we focused on axial
edge of the mechanisms that regulate cell fate in haematopoiesis and mesoderm differentiation, spanning 4.3 to 12 h post-fertilization
ground-truth in vivo phenotypes. Furthermore, systematic KO simu- (hpf) (Fig. 3a,b and Extended Data Fig. 10a,b). This midline structure
lations demonstrate that CellOracle enables objective and scalable in bifurcates into notochord and prechordal plate lineages, represent-
silico gene perturbation analysis. ing a crucial patterning axis33, and has been extensively character-
ized, in part through large-scale genetic screens34. For these lineages,
we performed systematic TF KO simulation and network analysis for
Systematic TF KO simulations in zebrafish
232 candidate TFs (Extended Data Fig. 10c). CellOracle ranked noto, a
Next, we applied CellOracle to systematically perturb TFs across well-characterized TF regulator of notochord development, as the top
zebrafish development. We made use of a 38,731-cell atlas of zebrafish TF on the basis of degree centrality, along with other known regulators
embryogenesis published in a study by Farrell et al.32, comprising 25 of notochord development (Fig. 3c). Degree centrality is a straight-
developmental trajectories that span zygotic genome activation to forward measure that reports how many edges (genes) are directly
early somitogenesis. We first inferred GRN configurations for the 38 cell connected to a node (TF); highly connected nodes are likely to be essen-
types and states identified in the Farrell et al. study32, splitting the main tial for a biological process35,36. In zebrafish floating headn1/n1 (flhn1/n1)
branching trajectory into four sub-branches: ectoderm; axial meso- mutants, which lack a functional noto gene (noto is also known as flh)37,
derm; other mesendoderm; and germ layer branching point (Extended axial mesoderm does not differentiate into notochord, and assumes a
Data Fig. 10a,b). In the absence of scATAC-seq data, we constructed somitic mesoderm fate instead38. Noto LOF simulation correctly repro-
a base GRN using promoter information from the UCSC database, duced the loss of notochord (Fig. 3d–f and Extended Data Fig. 10d–f),
746 | Nature | Vol 614 | 23 February 2023
SP
2.0
1
1.5
0
1.0 –1
0.5
0
–0.5
–1.0
FA1
2AF
a b c Notochord GRN Prechordal plate GRN
Pseudotime Pseudotime
gradient vector
Notochord
Early AM
Prechordal plate
Notochord Late
differentiation
Early
Prechordal plate
differentiation
FA1
0.1 0.2 0.3
2AF
noto noto
mix1l mix1l
sox11b lhx1a foxa2 sox11b
foxd3 foxd3 vox vox
sox3 sox11a
sox11a foxa
lhx1a foxd5
foxa meox1
foxd5 foxa2
meox1 klf17 cdx4 sox3
sox19a sebox tbx16 foxe3
sebox bhlha15
gsc vent
hoxb1b tbx16
sp5l gsc
twist2 sox19a
gata5 ved nkx1.2la foxp1b
eve1 six7
foxa1 foxa1
shox2 zgc:110425
irx3a pitx2
zic2b gbx1
six3b zgc:174153
ved gata5
vent ctslb
0.1 0.2 0.3
Degree centrality Degree centrality
Fig. 3 | CellOracle KO simulation with zebrafish embryogenesis data. prechordal plate (right). Black text denotes TFs. Grey text denotes non-TFs.
a, Two-dimensional force-directed graph of the axial mesoderm (AM) d, Expression of noto projected onto the axial mesoderm sub-branch. e, Noto
sub-branch (n = 1,669 cells) in a published zebrafish embryogenesis atlas KO simulation vector and perturbation scores. f, Markov simulation to estimate
(Farrell et al.32). Arrows indicate notochord cell differentiation (top) and cell density in the noto KO sample. The simulation predicted inhibited early
prechordal plate differentiation (bottom). b, Conversion of URD-calculated notochord differentiation and promotion of prechordal plate differentiation,
pseudotime (left) into a 2D pseudotime gradient vector field (right). c, Degree indicating a potential lineage switch.
centrality scores were used to rank the top 30 TFs in notochord (left) and
b c
1.5 3
1.0 2
0.5 1
0 0
in addition to enhanced somite differentiation (Extended Data (WT) reference atlas from dissociated WT embryos at 6, 8 and 10 hpf
Fig. 10g–k). Moreover, CellOracle predicted a previously unknown (to (2 technical replicates per stage) and used Seurat’s label transfer
our knowledge) consequence of noto LOF: enhanced prechordal plate function39 to cluster and label the WT reference cells according to the
differentiation (Fig. 3e,f). We also noted that later stages of notochord annotations in Farrell et al.32 (Extended Data Fig. 11). Subsetting the
differentiation received a positive perturbation score, indicating that axial mesoderm clusters showed the expected bifurcation of cells into
continued expression of noto is not required for notochord differentia- notochord and prechordal plate, accompanied by upregulation of
tion. Alternatively, this finding could suggest that downregulation of marker genes (Fig. 4a,b). For visualization of axial mesoderm cells,
noto is required for notochord maturation. we used a uniform manifold approximation and projection (UMAP)
transfer function to enable comparable data visualization between
different samples (Methods).
Experimental validation of noto LOF
For experimental perturbation of noto, we generated and dissoci-
Next, we experimentally validated the predicted expansion of pre- ated pools of 25 flhn1/n1 mutant embryos, recognized at 10 hpf by the
chordal plate after noto LOF. First, we generated a 38,606-cell wild-type lack of notochord boundaries, and sibling controls (flhn1/+ and flh+/+)
Nature | Vol 614 | 23 February 2023 | 747
fo
noitroporP
)2–01×(
sllec
retsulc
fo
noitroporP
)2–01×(
sllec
retsulc
a
twist2 gsc
Control tyr crispant
Notochord Notochord flh mutant noto crispant
differentiation Early notochord
Early AM Prechordal plate
noto Stage
6 hpf 8 hpf 10 hpf
Prechordal plate differentiation
UMAP2
d flhn1/n1 mutant 10 hpf axial mesoderm e Control cell (flh+/+, flhn1/+) density flh mutant cell (flhn1/n1) density
f g
noto crispant 10 hpf axial mesoderm tyr crispant cell density noto crispant cell density
1PAMU
Notochord
Early notochord
Early AM
Prechordal plate
Reference
1PAMU
Control
flhn1/n1 mutant
Reference
UMAP2 UMAP2
1PAMU
1PAMU
1PAMU
UMAP2 UMAP2
Notochord tyr crispant
Early notochord noto crispant
Early AM Reference
Prechordal plate
Reference
UMAP2 UMAP2 UMAP2 UMAP2
1PAMU
1PAMU
1PAMU
1PAMU
*** ****
4 3
3 **** ****
**** 2 **** 2
1 1
0 0
3 2
4
Early axial
mes
E
o
a
d
rl
e
y
r
n
m otochor
N
d ot
P
o
r
c
e
h
c
o
h
r
o
d rdal plate
Early axial
mes
E
o
a
d
rl
e
y
r
n
m otochor
N
d ot
P
o
r
c
e
h
c
o
h
r
o
d rdal plate
1
0
KDE
1 × 10–2
2.0
1.5
1.0
0.5
KDE
1 × 10–2
1.5
1.0
0.5
Fig. 4 | Experimental validation of zebrafish noto LOF predictions. a, UMAP mutants and noto crispants, the notochord is significantly depleted (flhn1/n1:
plot of WT reference data for axial mesoderm (6, 8 and 10 hpf): notochord, early P = 5.55 × 10−52; noto: P = 1.39 × 10−33, chi-square test) and the prechordal plate is
notochord, early axial mesoderm and prechordal plate clusters (n = 2,012 cells). significantly expanded (flhn1/n1: P = 1.07 × 10−4; noto: P = 5.01 × 10−18, chi-square
Arrows indicate notochord differentiation (top) and prechordal plate differentiation test. ***P < 0.001; ****P < 0.0001). d–g, flhn1/n1 mutant or noto crispant data
(bottom). b, Gene expression (log-transformed unique molecular identifier projected onto the WT axial mesoderm UMAP plot. d, Cluster annotation and
(UMI) count) and developmental stage are projected onto the axial mesoderm sample label projected onto the UMAP plot. e, Kernel cell density contour plot
UMAP plot. Noto and twist2 are expressed in notochord, whereas gsc marks the shows control cell density (left) and flhn1/n1 mutant cell density (right). f, Cluster
prechordal plate. c, Bar plots comparing cell cluster compositions between annotation and sample label projected onto the UMAP plot. g, tyr crispant cell
treatments and controls (left, flhn1/n1 mutants (10 hpf) and controls; right, noto density (left) and noto crispant cell density (right) shown on the kernel cell
crispants (10 hpf) and tyr crispants). Cluster compositions are presented as the density contour plot.
proportion of each group normalized to the whole cell number. In both flhn1/n1
Article
for scRNA-seq. We integrated these datasets and projected them onto (Extended Data Fig. 12c,d and Supplementary Table 4). Notably, we
the WT axial mesoderm reference atlas. In agreement with previous found a more considerable reduction in the expression of late noto-
observations, we observed a significant depletion of cells labelled as chord genes relative to broad notochord markers, suggesting that
notochord in flhn1/n1 mutants (−98%, relative to control, P = 5.55 × 10−52, loss of lhx1a function inhibits the differentiation and maturation of
chi-square test; Fig. 4c, left), concomitant with an expansion of the notochord cells. We observed a slight yet significant reduction in the
somite cluster (+41.3%; P = 5.90 × 10−29; Extended Data Fig. 11e, left). expression of the notochord markers twist2, nog1 and tbxta in sebox
Furthermore, as predicted by noto LOF simulation, we observed a sig- crispants (Extended Data Fig. 12e,f and Supplementary Table 4), con-
nificant expansion of the prechordal plate cluster in flhn1/n1 mutants firming CellOracle’s predictions that lhx1a and sebox are regulators of
(+38.6%; P = 1.07 × 10−4; Fig. 4c, left). Plotting cell density revealed axial mesoderm development. Irx3a crispants showed no significant
stalled notochord differentiation and bifiurcation of the mid axial phenotype in cell-type composition but exhibited a slight reduction in
mesoderm, with excess prechordal plate cells (Fig. 4d,e), consistent twist2 expression in the notochord (Extended Data Fig. 12g,h).
with the noto LOF simulation (Fig. 3e,f). To orthogonally validate these We extended lhx1a LOF characterization by performing four inde-
results, we produced noto LOF with a modified CRISPR–Cas9 protocol pendent biological replicates for lhx1a crispants (n = 45,582 cells) and
that we have previously used to achieve near-complete gene disruption tyr crispants (n = 76,163 cells, 5 biological and 7 technical replicates).
in F embryos injected with two noto-targeting guide RNAs (gRNAs)40 CellOracle predicted inhibition of early axial mesoderm differentiation
0
(Methods). The resulting noto ‘crispants’ were dissociated at 10 hpf after lhx1a disruption, depleting both notochord and prechordal plate
(9,185 cells, n = 2 biological and n = 3 technical replicates) and compared lineages (Fig. 5b). Indeed, the lhx1a crispants exhibited inhibition of
by single-cell analysis to controls that targeted the tyrosinase gene axial mesoderm differentiation (Fig. 5c–e): a significant expansion
(tyr), which is not expressed until later in development (n = 46,440 of the early notochord cluster (+70.2%; P = 1.34 × 10−35), with a con-
single cells, n = 3 biological and n = 5 technical replicates; Extended comitant reduction of later notochord (−15.3%; P = 3.83 × 10−3) and
Data Fig. 11b). Analysis of cell-type composition confirmed a significant prechordal plate clusters (−24.7%; P = 1.28 × 10−7). These phenotypes
depletion of notochord, with an expansion of somitic mesoderm and were reproducible across independent biological replicates (Extended
prechordal plate (Fig. 4c, right, Fig. 4f,g and Extended Data Fig. 11e, Data Fig. 13e), validating the predicted inhibition of early axial meso-
right) in noto crispants, highly consistent with our flhn1/n1 mutant analy- derm differentiation (Fig. 5a,b).
sis. Together, in addition to further validating the performance of Cel- To further analyse the lhx1a LOF axial mesoderm phenotype, we
lOracle, these results highlight the ability of this approach to identify investigated global changes in gene expression across all cell types
experimentally quantifiable phenotypes in well-characterized mutants using non-negative matrix factorization (NMF), a method to quantify
that may have been previously overlooked owing to a reliance on gross gene module activation45 (Supplementary Table 5 and Methods). We
morphology. We next sought to identify new LOF phenotypes in axial observed that a module corresponding to the early notochord was
mesoderm development. significantly activated in lhx1a crispants (P = 2.62 × 10−32; Fig. 5f,g). The
top gene in this module is admp (Extended Data Fig. 13f, left), which is
significantly upregulated in lhx1a crispant cells (P = 6.69 × 10−46; Fig. 5h)
Discovery of axial mesoderm regulators
and encodes a known negative regulator of notochord and prechordal
To identify novel TFs required for axial mesoderm differentiation, plate development46. By contrast, the late notochord module received
we prioritized TFs according to predicted KO phenotypes, focusing a significantly lower score in the lhx1a crispant cells (P = 1.04 × 10−5;
on early-stage differentiation before evident lineage specification Fig. 5g, bottom). This module comprises late notochord marker genes,
(Extended Data Fig. 12a). The resulting ranked list contains several such as twist2 and nog1 (Extended Data Fig. 13f, right), which showed
known notochord regulators, including noto (Fig. 5a, red and Supple- significantly lower expression in lhx1a crispant cells (P = 4.52 × 10−105
mentary Table 2), confirming CellOracle’s capacity to model known and P = 4.95 × 10−105, respectively; Fig. 5h). Further, lhx1a crispant cells
developmental regulation. However, it is important to note that some exhibited a higher somite module score (P = 5.19 × 10−25 and Supple-
known notochord regulators, such as foxa3 (ref. 41), were not identified mentary Table 5), suggesting that notochord cells may be redirected
as they are filtered out in the first steps of data processing owing to low towards a somitic identity after lhx1a LOF. Overall, the NMF analysis
expression. Systematic perturbation simulations for all lineages can be supports the hypothesis that loss of lhx1a function induces global
found at https://celloracle.org. As well as the axial mesoderm, we also changes in gene expression that are related to inhibited notochord
performed an in-depth analysis of the adaxial mesoderm, which gives differentiation.
rise to somites. Overall, more than 80% of the top 30 TFs in this analysis Finally, we confirmed the lhx1a LOF phenotype using orthogonal
were associated with somite differentiation (Supplementary Table 3). approaches. Hybridization chain reaction (HCR) RNA fluorescence
In addition to known TFs, we identified several TFs with no previously in situ hybridization for nog1 (late notochord) and for gsc and twist2
reported role in axial mesoderm differentiation (Fig. 5a, black). We (prechordal plate and notochord, respectively) showed that these
further prioritized candidate genes for experimental validation by GRN genes were significantly downregulated in lhx1a crispants (Fig. 5i–k).
degree centrality, gene enrichment score in axial mesoderm and aver- These results were further confirmed by quantitative reverse transcrip-
age gene expression value, selecting lhx1a, sebox and irx3a (Extended tion PCR (qRT-PCR) and whole-mount in situ hybridization against
Data Fig. 12b). CellOracle predicts impaired notochord differentiation nog1 (Supplementary Fig. 22). Together, this experimental validation
for all three genes after their LOF (Fig. 5b and Supplementary Fig. 19). confirms the significant and consistent disruption of axial mesoderm
However, no LOF studies describing axial mesoderm phenotypes that development after loss of lhx1a function. In summary, these results
relate to these genes have, to our knowledge, been reported in zebrafish. demonstrate the ability of CellOracle to accurately predict known TF
Mouse Lhx1 (Lim1) KO embryos lack anterior head structures and kid- perturbation phenotypes, provide insight into previously characterized
neys42. In zebrafish, sebox (mezzo) has been implicated in mesoderm mutants and reveal regulators of established developmental processes
and endoderm specification43, whereas irx3a (ziro3) morphants exhibit in well-studied model organisms.
changes in the composition of pancreatic cell types44.
We generated lhx1a, sebox and irx3a crispants (Supplementary
Discussion
Fig. 20b–d). We performed initial single-cell analyses at 10 hpf, inte-
grating crispant scRNA-seq datasets with the control gRNA reference The emerging discipline of perturbational single-cell omics enables
atlas described above. We observed significant changes in cell-type regulators of cell identity and behaviour to be modelled and predicted5.
composition and notochord marker expression in lhx1a crispants For example, scGen combines variational autoencoders with latent
748 | Nature | Vol 614 | 23 February 2023
a b c
d e
space vector arithmetic to predict cell infection response. However, previous computational perturbation approaches because they rely
this approach requires experimentally perturbed training data, which on complex black-box models; thus, the simulations lack any means
limits its scalability47. More importantly, it remains challenging to inter- to interpret how gene regulation relates to cellular phenotype. On
pret the gene program behind the simulated outcome using these the other hand, previous GRN analyses relied largely on static graph
Nature | Vol 614 | 23 February 2023 | 749
fo noitroporP
)2–01×(
sllec
retsulc
tyr crispant lhx1a
crispant
tyr crispant lhx1a crispant
Notochord tyr crispant
Early notochord lhx1a crispant
Early AM WT reference
Prechordal plate
WT reference
UMAP2 UMAP2
h j
1PAMU 1PAMU
1PAMU 1PAMU
1.5
0
–0.5
19.9% 13.8%
14.8% 21.4%
UMAP2 UMAP2
SP
Negative PS sum
KDE
f g
atled
erocs
eludoM
)2–01×(
)erocs
tnapsirc
ryt
– erocs
tnapsirc
a1xhl(
Early notochord module
Early ectoderm and
mesendoderm module
tyr lhx1a
crispantcrispant Somite module
CM and
prechordal plate
module
Late notochord module
tyr lhx1a
crispant crispant
drohcoton
ylraE
erocs
eludom
Simulation vector field and PS Diffusion simulation
****
** Early axial mesoderm High **** Notochord differentiation
inhibited
Low Early AM
Prechordal plate
****
k
i
****
)elohw(1gon
WT tyr crispant lhx1a crispant
WT tyr crispant lhx1a crispant
csg
2tsiwt
Broad
modules
drohcoton
etaL
erocs
eludom
dezilamroN
noisserpxe
eneg
**** **** **** ****
admp noto twist2 nog1
Early NC gene Late NC gene
** *** **
** ** **
gsc twist2
WT tyr crispant lhx1a crispant
stops
RCH
0 20 40 60
foxa2 *
n s o p t 5 o l * * 2.5
zic2a creb3l2 2.0 jund eve1 * 1.5 her6 *
jun * 1.0 nkx1.2la
cdx4 * 0.5
irx3a
foxi1
lef1 * 0 cr t s s
l
e
m
w l t e r o
s
h f b f x
o
b o i e x
x
x s r 3 3
x
3
1
1 x o a t l 2
2
a 2 1 a
a
a a x * *
*
Early axial mes E o a d rl e y r n m otocho N rd o P to re c c h h o o r r d dal plate
her9
dlx3b
gbx1
sp5a *
nr3c1
tcf7l2
1 × 10–2
2.0
1.5
1.0
0.5
4
0.6 4
3 0.4
2
0.2
2
0 0
1
0
0.8
1.5
0.6
–1
1.0
0.4
–2 0.2 0.5
0 0 nog1
Fig. 5 | Experimental validation of lhx1a as a putative regulator of zebrafish difference in averaged NMF module scores between lhx1a and tyr crispants in
axial mesoderm development. a, Top 30 TFs according to predicted KO notochord lineage cells. Black, cell-type-specific modules. Light grey, broad
effects. Red and *: previously reported notochord regulators (Supplementary cluster modules. CM, cephalic mesoderm. g, Violin plot of NMF module score
Table 2). lhx1a, sebox and irx3a were selected for experimental validation. in notochord lineage cells (n = 1,918 lhx1a crispant and n = 2,616 tyr crispant
b, lhx1a LOF simulation in the axial mesoderm sub-branch, predicting an cells. h, Violin plots of gene expression in the notochord (NC) lineage cells.
inhibition of axial mesoderm differentiation from early stages. c, scRNA-seq ****P < 0.0001, two-tailed Wilcoxon rank-sum test with Bonferroni correction.
validation of experimental LOF: cell cluster composition of the axial mesoderm i, Quantification (number of spots in flattened HCR image) normalized to WT.
clusters normalized to the whole cell number in lhx1a and tyr (control) crispant Mean ± s.e.m. n = 2 independent biological replicates, 8 embryos per replicate.
samples. Early notochord is significantly expanded (P = 1.34 x 10−35, chi-square nog1: P = 0.0022 (WT versus lhx1a crispant), P = 0.0052 (tyr versus lhx1a
test) and differentiated axial mesoderm populations are significantly depleted crispant); gsc: P = 0.00042 (WT versus lhx1a crispant), P = 0.0018 (tyr versus
(notochord: P = 3.83 x 10−3; prechordal plate: P = 1.28 x 10−7, chi-square test) in lhx1a crispant); twist2: P = 0.0011 (WT versus lhx1a crispant), P = 0.0012 (tyr
lhx1a crispants. d, lhx1a and tyr crispant axial mesoderm cells at 10 hpf. Left, cell versus lhx1a crispant); two-sided t-test. j, Representative HCR images for nog1
type annotation of lhx1 and tyr crispant cells. Right, lhx1a and control crispant expression (yellow) in whole embryos at 10 hpf. k, Representative flattened
data projected onto the WT UMAP. e, Control cell density (left, n = 2,342 cells) HCR images of 10 hpf embryos stained with probes against gsc (yellow) and
and lhx1a crispant cell density (right, n = 2,502 cells). f, Rug plot showing the twist2 (red); nuclei are stained with DAPI (blue). Scale bars, 300 μm.
Article
theory and could not consider cell identity as a dynamic property. Here
Online content
we present a strategy that overcomes these limitations by integrating
computational perturbation with GRN modelling. CellOracle uses GRN Any methods, additional references, Nature Portfolio reporting summa-
models to yield mechanistic insights into the regulation of cell identity; ries, source data, extended data, supplementary information, acknowl-
simulation and vector visualization based on the custom network model edgements, peer review information; details of author contributions
enables the interpretable, scalable and broadly applicable analysis of and competing interests; and statements of data and code availability
dynamic TF function. are available at https://doi.org/10.1038/s41586-022-05688-9.
We validated CellOracle using various in vivo differentiation mod-
els, verifying its efficacy and its robustness to complex and noisy 1. Davidson, E. H. & Erwin, D. H. Gene regulatory networks and the evolution of animal body
biological data. CellOracle simulates shifts in cell identity by consid- plans. Science 311, 796–800 (2006).
2. Adamson, B. et al. A multiplexed single-cell CRISPR screening platform enables systematic
ering systematic gene-to-gene relationships for each cell state using
dissection of the unfolded protein response. Cell 167, 1867–1882 (2016).
multimodal data, generating a complex context-dependent vector 3. Dixit, A. et al. Perturb-Seq: dissecting molecular circuits with scalable single-cell RNA
representation that is not possible using differential gene expression profiling of pooled genetic screens. Cell 167, 1853–1866 (2016).
4. Datlinger, P. et al. Pooled CRISPR screening with single-cell transcriptome readout. Nat.
or chromatin accessibility alone. For example, the role of Gata1 in gran-
Methods 14, 297–301 (2017).
ulocyte differentiation would probably not be predicted given its low 5. Ji, Y., Lotfollahi, M., Wolf, F. A. & Theis, F. J. Machine learning for perturbational single-cell
expression in this cell type. However, CellOracle could corroborate this omics. Cell Syst. 12, 522–537 (2021).
6. Fiers, M. W. E. J. et al. Mapping gene regulatory networks from single-cell omics data.
relatively mild Gata1 phenotype. Furthermore, CellOracle correctly
Brief. Funct. Genomics 17, 246–254 (2018).
reproduced the reported early-stage-specific cell-fate-regulatory 7. Aibar, S. et al. SCENIC: single-cell regulatory network inference and clustering. Nat. Methods
role of Tal1 in erythropoiesis, which is impossible to uncover on the 14, 1083–1086 (2017).
8. Iacono, G., Massoni-Badosa, R. & Heyn, H. Single-cell transcriptomics unveils gene regulatory
basis of the constitutive expression of Tal1 throughout all erythroid
network plasticity. Genome Biol. 20, 110 (2019).
stages. This capacity of CellOracle means that it could identify previ- 9. Fleck, J. S. et al. Inferring and perturbing cell fate regulomes in human brain organoids.
ously unreported phenotypes. For example, the LOF simulation of a Nature https://doi.org/10.1038/s41586-022-05279-8 (2022).
10. Kartha, V. K. et al. Functional inference of gene regulation using single-cell multi-omics.
well-characterized regulator of zebrafish axial mesoderm develop-
Cell Genom. 2, 100166 (2022).
ment, noto, predicted a previously unreported expansion of the pre- 11. González-Blas, C. B. et al. SCENIC+: single-cell multiomic inference of enhancers and
chordal plate, which we experimentally validated. This case suggests gene regulatory networks. Preprint at bioRxiv https://doi.org/10.1101/2022.08.19.504505
(2022).
that noto has a role in suppressing alternate fates, which could only
12. Pliner, H. A. et al. Cicero predicts cis-regulatory DNA interactions from single-cell chromatin
be predicted by the integrative simulation using the GRN and cell accessibility data. Mol. Cell 71, 858–871 (2018).
differentiation trajectory together. Finally, although we focus on TF 13. Cusanovich, D. A. et al. A single-cell atlas of in vivo mammalian chromatin accessibility.
Cell 174, 1309–1324 (2018).
KO and LOF in this study, we have also recently demonstrated that
14. Oki, S. et al. ChIP-Atlas: a data-mining suite powered by full integration of public ChIP-seq
CellOracle can be used to simulate TF overexpression48. data. EMBO Rep. 19, e46255 (2018).
We note some limitations of the method. First, CellOracle visualizes 15. Orkin, S. H. & Zon, L. I. Hematopoiesis: an evolving paradigm for stem cell biology. Cell
132, 631–644 (2008).
the simulation vector within the existing trajectory space; thus, cell
16. Paul, F. et al. Transcriptional heterogeneity and lineage commitment in myeloid progenitors.
states that do not exist in the input scRNA-seq data cannot be analysed. Cell 163, 1663–1677 (2015).
Nevertheless, existing single-cell data collected after severe develop- 17. Rekhtman, N., Radparvar, F., Evans, T. & Skoultchi, A. I. Direct interaction of hematopoietic
transcription factors PU.1 and GATA-1: functional antagonism in erythroid cells. Genes
mental disruption do not report the emergence of new transcriptional
Dev. 13, 1398–1411 (1999).
states in the context of loss of gene function, which suggests extensive 18. Zhang, P. et al. Negative cross-talk between hematopoietic regulators: GATA proteins
canalization even during abnormal development32, supporting the use repress PU.1. Proc. Natl Acad. Sci. USA 96, 8705–8710 (1999).
19. Nutt, S. L., Metcalf, D., D’Amico, A., Polli, M. & Wu, L. Dynamic regulation of PU.1 expression
of CellOracle to accurately simulate TF perturbation effects. Second, in multipotent hematopoietic progenitors. J. Exp. Med. 201, 221–231 (2005).
we emphasize that TF simulation is limited by input data availability 20. Back, J., Allman, D., Chan, S. & Kastner, P. Visualizing PU.1 activity during hematopoiesis.
and data quality. For example, a perturbation cannot be simulated if a Exp. Hematol. 33, 395–402 (2005).
21. Fujiwara, Y., Browne, C. P., Cunniff, K., Goff, S. C. & Orkin, S. H. Arrested development of
TF-binding motif is unknown or TF expression is too sparse, as we note embryonic red cell precursors in mouse embryos lacking transcription factor GATA-1.
in the case of foxa3 in zebrafish41. Proc. Natl Acad. Sci. USA 93, 12355–12358 (1996).
Our application of CellOracle to systematically simulate TF pertur- 22. Yu, C. et al. Targeted deletion of a high-affinity GATA-binding site in the GATA-1 promoter
leads to selective loss of the eosinophil lineage in vivo. J. Exp. Med. 195, 1387–1395
bation has revealed regulators of a well-characterized developmental (2002).
paradigm: the formation of axial mesoderm in zebrafish. Although 23. Fulkerson, P. C. Transcription factors in eosinophil development and as therapeutic targets.
zebrafish axial mesoderm has been well-characterized through Front. Med. 4, 115 (2017).
24. Hirasawa, R. et al. Essential and instructive roles of GATA factors in eosinophil development.
mutagenesis screens, a role for Lhx1a in these developmental stages J. Exp. Med. 195, 1379–1386 (2002).
is likely to have gone unreported owing to the absence of gross mor- 25. Iwasaki, H. et al. Distinctive and indispensable roles of PU.1 in maintenance of hematopoietic
stem cells and their differentiation. Blood 106, 1590–1600 (2005).
phological phenotypical changes at 10 hpf after disruption of lhx1a
26. Mak, K. S., Funnell, A. P. W., Pearson, R. C. M. & Crossley, M. PU.1 and haematopoietic cell
(ref. 49). However, our ability to predict and validate such a phenotype fate: dosage matters. Int. J. Cell Biol. 2011, 808524 (2011).
showcases the power of single-cell computational and experimental 27. Wontakal, S. N. et al. A large gene network in immature erythroid cells is controlled by the
myeloid and B cell transcriptional regulator PU.1. PLoS Genet. 7, e1001392 (2011).
approaches, enabling finer-resolution dissection of gene regulation
28. Moreau-Gachelin, F., Tavitian, A. & Tambourin, P. Spi-1 is a putative oncogene in virally
even in well-characterized systems. Moreover, CellOracle provides induced murine erythroleukaemias. Nature 331, 277–280 (1988).
information at intermediate steps in a given developmental pathway, 29. Rosenbauer, F. & Tenen, D. G. Transcription factors in myeloid development: balancing
differentiation with transformation. Nat. Rev. Immunol. 7, 105–117 (2007).
obviating the need for gross morphological end-points. Indeed, each
30. Pijuan-Sala, B. et al. A single-cell molecular map of mouse gastrulation and early
simulation can be thought of as many successive predictions along a organogenesis. Nature 566, 490–495 (2019).
lineage, although we stress that experimental validation is essential 31. Mikkola, H. K. A. et al. Haematopoietic stem cells retain long-term repopulating activity
and multipotency in the absence of stem-cell leukaemia SCL/tal-1 gene. Nature 421,
to validate CellOracle’s predictions where possible. However, apply-
547–551 (2003).
ing these approaches to emerging systems or where experimental 32. Farrell, J. A. et al. Single-cell reconstruction of developmental trajectories during zebrafish
intervention is not feasible promises to accelerate our understanding embryogenesis. Science 360, eaar3131 (2018).
33. Halpern, M. E. Axial mesoderm and patterning of the zebrafish embryo. Am. Zool. 37,
of how cell identity is regulated. For example, in the context of human
311–322 (1997).
development, we have recently applied CellOracle to predict candi- 34. Fuentes, R. et al. The maternal coordinate system: molecular-genetics of embryonic
date regulators of medium spiny neuron maturation in human fetal axis formation and patterning in the zebrafish. Curr. Top. Dev. Biol. 140, 341–389
striatum50, demonstrating the power of in silico perturbation where (2020).
35. Joyce, A. R. & Palsson, B. Predicting gene essentiality using genome-scale in silico
experimental approaches cannot be deployed. models. Methods Mol. Biol. 416, 433–457 (2008).
750 | Nature | Vol 614 | 23 February 2023
36. Hahn, M. W. & Kern, A. D. Comparative genomics of centrality and essentiality in three 47. Lotfollahi, M., Wolf, F. A. & Theis, F. J. scGen predicts single-cell perturbation responses.
eukaryotic protein-interaction networks. Mol. Biol. Evol. 22, 803–806 (2005). Nat. Methods 16, 715–721 (2019).
37. Talbot, W. S. et al. A homeobox gene essential for zebrafish notochord development. Nature 48. Kamimoto, K. et al. Gene regulatory network reconfiguration in direct lineage
378, 145–149 (1995). reprogramming. Stem Cell Rep. https://doi.org/10.1016/j.stemcr.2022.11.010 (2022).
38. Halpern, M. E. et al. Cell-autonomous shift from axial to paraxial mesodermal development 49. Shestopalov, I. A., Pitt, C. L. W. & Chen, J. K. Spatiotemporal resolution of the Ntla
in zebrafish floating head mutants. Development 121, 4257–4264 (1995). transcriptome in axial mesoderm development. Nat. Chem. Biol. 8, 270–276 (2012).
39. Stuart, T. et al. Comprehensive integration of single-cell data. Cell 177, 1888–1902 50. Bocchi, V. D. et al. The coding and long noncoding single-cell atlas of the developing
(2019). human fetal striatum. Science 372, eabf5759 (2021).
40. Klatt Shaw, D. et al. Localized EMT reprograms glial progenitors to promote spinal cord
repair. Dev. Cell 56, 613–626 (2021). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
41. Dal-Pra, S., Thisse, C. & Thisse, B. FoxA transcription factors are essential for the development published maps and institutional affiliations.
of dorsal axial structures. Dev. Biol. 350, 484–495 (2011).
42. Shawlot, W. & Behringer, R. R. Requirement for LIml in head-organizer function. Nature
Open Access This article is licensed under a Creative Commons Attribution
374, 425–430 (1995).
4.0 International License, which permits use, sharing, adaptation, distribution
43. Poulain, M. & Lepage, T. Mezzo, a paired-like homeobox protein is an immediate target of
and reproduction in any medium or format, as long as you give appropriate
nodal signalling and regulates endoderm specification in zebrafish. Development 129,
credit to the original author(s) and the source, provide a link to the Creative Commons licence,
4901–4914 (2002).
and indicate if changes were made. The images or other third party material in this article are
44. Ragvin, A. et al. Long-range gene regulation links genomic type 2 diabetes and
included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
obesity risk regions to HHEX, SOX4, and IRX3. Proc. Natl Acad. Sci. USA 107, 775–780
to the material. If material is not included in the article’s Creative Commons licence and your
(2010).
intended use is not permitted by statutory regulation or exceeds the permitted use, you will
45. Brunet, J.-P., Tamayo, P., Golub, T. R. & Mesirov, J. P. Metagenes and molecular pattern
need to obtain permission directly from the copyright holder. To view a copy of this licence,
discovery using matrix factorization. Proc. Natl Acad. Sci. USA 101, 4164–4169 (2004).
visit http://creativecommons.org/licenses/by/4.0/.
46. Lele, Z., Nowak, M. & Hammerschmidt, M. Zebrafish admp is required to restrict the size
of the organizer and to promote posterior and ventral development. Dev. Dyn. 222, 681–687
(2001). © The Author(s) 2023
Nature | Vol 614 | 23 February 2023 | 751
Article
Methods the target gene name. This bed file is used in the next step. CellOracle
can also use other input data types to define cis-regulatory elements.
CellOracle algorithm overview For example, a database of promoter and enhancer DNA sequences or
The CellOracle workflow consists of several steps: (1) base GRN con- bulk ATAC-seq data can serve as an alternative if available as a .bed file.
struction using scATAC-seq data or promoter databases; (2) scRNA-seq For the analysis of mouse haematopoiesis that we present here, we
data preprocessing; (3) context-dependent GRN inference using assembled the base GRN using a published mouse scATAC-seq atlas con-
scRNA-seq data; (4) network analysis; (5) simulation of cell identity sisting of around 100,000 cells across 13 tissues, representing around
following TF perturbation; and (6) calculation of the pseudotime gradi- 400,000 differentially accessible elements and 85 different chromatin
ent vector field and the inner-product score to generate perturbation patterns13. This base GRN is built into the CellOracle library to support
scores. We implemented and tested CellOracle in Python (versions 3.6 GRN inference without sample-specific scATAC-seq datasets. In addi-
and 3.8) and designed it for use in the Jupyter notebook environment. tion, we have generated general promoter base GRNs for several key
CellOracle code is open source and available on GitHub (https://github. organisms commonly used to study development, including 10 species
com/morris-lab/CellOracle), along with detailed descriptions of func- and 23 reference genomes (Supplementary Table 1).
tions and tutorials.
Motif scan of promoter and enhancer DNA sequences. This step
Base GRN construction using scATAC-seq data scans the DNA sequences of promoter and enhancer elements to iden-
In the first step, CellOracle constructs a base GRN that contains tify TF-binding motifs. CellOracle internally uses gimmemotifs (https://
unweighted, directional edges between a TF and its target gene. gimmemotifs.readthedocs.io/en/master/), a Python package for TF
CellOracle uses the regulatory region’s genomic DNA sequence and motif analysis. For each DNA sequence in the bed file obtained in step
TF-binding motifs for this task. CellOracle identifies regulatory can- (i) above, motif scanning is performed to search for TF-binding motifs
didate genes by scanning for TF-binding motifs within the regulatory in the input motif database.
DNA sequences (promoter and enhancers) of open chromatin sites. For mouse and human data, we use gimmemotifs motif v.5 data. Cel-
This process is beneficial as it narrows the scope of possible regula- lOracle also provides a motif dataset for ten species generated from
tory candidate genes in advance of model fitting and helps to define the CisBP v.2 database (http://cisbp.ccbr.utoronto.ca).
the directionality of regulatory edges in the GRN. However, the base CellOracle exports a binary data table representing a potential con-
network generated in this step may still contain pseudo- or inactive nection between a TF and its target gene across all TFs and target genes.
connections; TF regulatory mechanisms are not only determined by CellOracle also reports the TF-binding DNA region. CellOracle provides
the accessibility of binding motifs but may also be influenced by many pre-built base GRNs for ten species (Supplementary Table 1), which can
context-dependent factors. Thus, scRNA-seq data are used to refine be used if scATAC-seq data are unavailable.
this base network during the model fitting process in the next step of
base GRN assembly. scRNA-seq data preprocessing
Base GRN assembly can be divided into two steps: (i) identification of CellOracle requires standard scRNA-seq preprocessing in advance
promoter and enhancer regions using scATAC-seq data; and (ii) motif of GRN construction and simulation. The scRNA-seq data need to be
scanning of promoter and enhancer DNA sequences. prepared in the AnnData format (https://anndata.readthedocs.io/en/
latest/). For data preprocessing, we recommend using Scanpy (https://
Identification of promoter and enhancer regions using scATAC-seq scanpy.readthedocs.io/en/stable/) or Seurat (https://satijalab.org/
data. CellOracle uses genomic DNA sequence information to define seurat/). Seurat data must be converted into the AnnData format using
candidate regulatory interactions. To achieve this, the genomic regions the CellOracle function, seuratToAnndata, preserving its contents.
of promoters and enhancers first need to be designated, which we infer In the default CellOracle scRNA-seq preprocessing step, zero-count
from ATAC-seq data. We designed CellOracle for use with scATAC-seq genes are first filtered out by UMI count using scanpy.pp.filter_
data to identify accessible promoters and enhancers (Extended Data genes(min_counts=1). After normalization by total UMI count per cell
Fig. 1a, left panel). Thus, scATAC-seq data for a specific tissue or cell type using sc.pp.normalize_per_cell(key_n_counts=‘n_counts_all’), highly
yield a base GRN representing a sample-specific TF-binding network. variable genes are detected by scanpy.pp.filter_genes_dispersion(n_
In the absence of a sample-specific scATAC-seq dataset, we recom- top_genes=2000~3000). The detected variable gene set is used for
mend using scATAC-seq data from closely related tissue or cell types downstream analysis. Gene expression values are log-transformed,
to support the identification of promoter and enhancer regions. Using scaled and subjected to dimensional reduction and clustering. The
broader scATAC-seq datasets produces a base GRN corresponding to non-log-transformed gene expression matrix (GEM) is also retained,
a general TF-binding network rather than a sample-specific base GRN. as it is required for downstream GRN calculation and simulation.
Nevertheless, this base GRN network will still be tailored to a specific
sample using scRNA-seq data during the model fitting process. The final Context-dependent GRN inference using scRNA-seq data
product will consist of context-dependent (cell-type or state-specific) In this step of CellOracle GRN inference, a machine-learning model is
GRN configurations. built to predict target gene expression from the expression levels of
To identify promoter and enhancer DNA regions within the the regulatory genes identified in the previous base GRN refinement
scATAC-seq data, CellOracle first identifies proximal regulatory DNA step. By fitting models to sample gene expression data, CellOracle
elements by locating TSSs within the accessible ATAC-seq peaks. extracts quantitative gene–gene connection information. For signal
This annotation is performed using HOMER (http://homer.ucsd. propagation, the CellOracle GRN model must meet two requirements:
edu/homer/). Next, the distal regulatory DNA elements are obtained (1) the GRN model needs to represent transcriptional connections as
using Cicero, a computational tool that identifies cis-regulatory a directed network edge; and (2) the GRN edges need to be a linear
DNA interactions on the basis of co-accessibility, as derived from regression model. Because of this second constraint, we cannot use
ATAC-seq peak information12. Using the default parameters of Cicero, pre-existing GRN inference algorithms, such as GENIE3 and GRNboost
we identify pairs of peaks within 500 kb of each other and calculate a (refs. 7,51). CellOracle leverages genomic sequences and information on
co-accessibility score. Using these scores as input, CellOracle then TF-binding motifs to infer the base GRN structure and directionality,
identifies distal cis-regulatory elements defined as pairs of peaks with and it does not need to infer the causality or directionality of the GRN
a high co-accessibility score (≥0.8), with the peaks overlapping a TSS. from gene expression data. This allows CellOracle to adopt a relatively
The output is a bed file in which all cis-regulatory peaks are paired with simple machine-learning model for GRN inference—a regularized linear
machine-learning model. CellOracle builds a model that predicts the
expression of a target gene on the basis of the expression of regulatory Simulation of cell identity following perturbation of regulatory
candidate genes: genes
The central purpose of CellOracle is to understand how a GRN governs
n
x = ∑ b x+ c, cell identity. Toward this goal, we designed CellOracle to make use of
j i,j i j
inferred GRN configurations to simulate how cell identity changes
i=0
following perturbation of regulatory genes. The simulated gene expres-
where x is single target gene expression and x is the gene expres- sion values are converted into 2D vectors representing the direction of
j i
sion value of the regulatory candidate gene that regulates gene x. b cell-state transition, adapting the visualization method previously used
j i,j
is the coefficient value of the linear model (but b = 0 if i = j), and c by RNA velocity52. This process consists of four steps: (i) data preprocess-
i,j
is the intercept for this model. Here, we use the list of potential regula- ing; (ii) signal propagation within the GRN; (iii) estimation of transition
tory genes for each target gene generated in the previous base GRN probabilities; and (iv) analysis of simulated transition in cell identity.
construction step (ii). (i) Data preprocessing
For simulation of cell identity, we developed our code by modify-
x∈{x , x, …x }=Regulatorycandidate TFs of genex
i 0 1 n j ing Velocyto.py, a Python package for RNA-velocity analysis (https://
velocyto.org). Consequently, CellOracle preprocesses the scRNA-seq
The regression calculation is performed for each cell cluster in par- data per Velocyto requirements by first filtering the genes and imputing
allel after the GEM of scRNA-seq data is divided into several clusters. dropout. Dropout can affect Velocyto’s transition probability calcula-
The cluster-wise regression model can capture non-linear or mixed tions; thus, k-nearest neighbour (KNN) imputation must be performed
regulatory relationships. In addition, L2 weight regularization is applied before the simulation step.
by the Ridge model. Regularization not only helps distinguish active (ii) Within-network signal propagation
regulatory connections from random, inactive, or false connections in This step aims to estimate the effect of TF perturbation on cell identity.
the base GRN but also reduces overfitting in smaller samples. CellOracle simulates how a ‘shift’ in input TF expression leads to a ‘shift’
The Bayesian Ridge or Bagging Ridge model provides the coefficient in its target gene expression and uses a partial derivative
∂xj.
As we use
value as a distribution, and we can analyse the reproducibility of the a linear model, the derivative
∂xj
is a constant value and
∂
a
xi
lready cal-
∂xi
inferred gene–gene connection (Extended Data Fig. 1a, right). In both culated as b in the previous step if the gene j is directly regulated by
i,j
models, the output is a posterior distribution of coefficient value b: gene i:
 n  ∂x
x
j
∼Normal∑b
i,j
x
i
+c
j
,ϵ
∂x
j =b
i,j
.
i=1  i
And we calculate the shift of target gene Δx in response to the shift
b∼Normal(μ ,σ) j
b b of regulatory gene Δx:
i
∂x
where μ is the centre of the distribution of b, and σ is the standard j
deviatio b n of b. The user can choose the model metho b d depending on Δx j = ∂x i Δx i =b i,j Δx i .
the availability of computational resources and the aim of the analysis;
CellOracle’s Bayesian Ridge requires fewer computational resources, As we want to consider the gene-regulatory ‘network’, we also con-
whereas the Bagging Ridge tends to produce better inference results sider indirect connections. The network edge represents a differenti-
than Bayesian Ridge. Using the posterior distribution, we can calculate able linear function shown above, and the network edge connections
P values of coefficient b; one-sample t-tests are applied to b to estimate between indirectly connected nodes is a composite function of the
the probability (the centre of b = 0). The P value helps to identify robust linear models, which is differentiable accordingly. Using this feature,
connections while minimizing connections derived from random noise. we can apply the chain rule to calculate the partial derivative of the
In addition, we apply regularization to coefficient b for two purposes: target genes, even between indirectly connected nodes.
(i) to prevent coefficient b from becoming extremely large owing to
overfitting; and (ii) to identify informative variables through regu- ∂x j = ∏ n ∂x k+1= ∏ n b ,
larization. In CellOracle, the Bayesian Ridge model uses regularizing ∂x ∂x k,k+1
i k=0 k k=0
prior distribution of b as follows:
where
b∼Normal(0,σ)
b
x ∈{x ,x,…x }=Gene expression of ordered network
k 0 1 n
σ−1∼Gamma(10−6,10−6) nodes on the shortest path from geneito genej.
b
σ is selected to represent non-informative prior distributions. This For example, when we consider the network edge from gene 0 to 1
b
model uses data in the fitting process to estimate the optimal regu- to 2, the small shift of gene 2 in response to gene 0 can be calculated
larization strength. In the Bagging Ridge model, custom regularization using the intermediate connection with gene 1 (Supplementary Fig. 1).
strength can be manually set.
∂x ∂x ∂x
For the computational implementation of the above machine-learning 2 = 1 × 2=b ×b
models, we use a Python library, scikit-learn (https://scikit-learn.org/ ∂x 0 ∂x 0 ∂x 1 0,1 1,2
stable/). For Bagging Ridge regression, we use the Ridge class in the
sklearn.linear_model and BaggingRegressor in the sklearn.ensemble ∂x
Δx = 2Δx =b b Δx
module. The number of iterative calculations in the bagging model can 2 ∂x 0 0,1 1,2 0
0
be adjusted depending on the computational resources and available
time. For Bayesian Ridge regression, we use the BayesianRidge class in In summary, the small shift of the target gene can be formulated by
sklearn.linear_module with the default parameters. the multiplication of only two components, GRN model coefficient b
i,j
Article
and input TF shift Δx. In this respect, we focus on the gradient of gene cell j after perturbation. To calculate p , CellOracle calculates the Pear-
i i,j
expression equations rather than the absolute expression values so son’s correlation coefficient between d and r :
i i,j
that we do not model the error or the intercept of the model, which
exp(corr(r,d)/T)
potentially includes unobservable factors within the scRNA-seq data. ij i
p = ,
The calculation above is implemented as vector and matrix ij ∑ j∈G exp(corr(r ij ,d i )/T)
multiplication. First, the linear regression model can be shown as
follows. where d
i
is the simulated gene expression shift vector ΔX
simulated
∈R 1×N
X′=X⋅B+C, f X o ∈ r c R e 1 l × l N i, b a e n t d w r e ij e ∈ n R c 1 e × l N l i i a s n a d s u ce b l t l r j a i c n t t i h o e n o o r f i t g h in e a g l e G n E e M ex . T p h re e s v s a io lu n e v is e c n t o o r r -
malized by the Softmax function (default temperature parameter T is
where the X∈R 1×N is a gene expression vector containing N genes, 0.05). The calculation of p
i.j
uses neighbouring cells of cell i. The KNN
C∈R 1×N is the intercept vector, B∈R N×N is the network adjacency method selects local neighbours in the dimensional reduction embed-
matrix, and each element b is the coefficient value of the linear model ding space (k = 200 as default).
i,j
from regulatory gene i to target gene j. (iv) Calculation of simulated cell-state transition vector
First, we set the perturbation input vector ΔX
input
∈R 1×N, a sparse The transition probability matrix P is converted into a transition vector
vector consisting of zero except for the perturbation target gene i. For V
i,simulated
∈R 1×2, representing the relative cell-identity shift of cell i in
the TF perturbation target gene, we set the shift of the TF to be simu- the 2D dimensional reduction space, as follows: CellOracle calculates
lated. The CellOracle function will produce an error if the user enters the local weighted average of vector V
i,j
∈R 1×2,V
i,j
denotes the 2D
a gene shift corresponding to an out-of-distribution value. vector obtained by subtracting the 2D coordinates in the dimensional
Next, we calculate the shift of the first target gene: reduction embedding between cell i and cell j (cellj∈G).
ΔX simulated,n=1 =ΔX input ⋅B. V i,simulated = ∑ p ij V i,j
j∈G
However, we fix the perturbation target gene i value, and the Δx
i
retains the same value as the input state. Thus, the following calculation (v) Calculation of vector field
will correspond to both the first and the second downstream gene shift The single-cell resolution vector V is too fine to interpret the
i,simulated
calculations. results in a large dataset consisting of many cells. We calculate the
summarized vector field using the same vector averaging strategy as
ΔX =ΔX ⋅B.
simulated,n=2 simulated,n=1 Velocyto. The simulated cell-state transition vector for each cell is
grouped by grid point to get the vector field, V vectorfield = R 2×L×L, (L is
Likewise, the recurrent calculation is performed to propagate the grid number, default L is 40). v
grid
∈R 2, an element in the V
vectorfield
, is
shift from gene to gene in the network. Repeating this calculation for calculated by the Gaussian kernel smoothing.
n iterations, we can estimate the effects on the first to the nth indirect
target gene (Extended Data Fig. 1b–d): v grid =∑ i∈H K σ (g, V i,simulated )V i,simulated ,
ΔX simulated,n =ΔX simulated,n−1 ⋅B. where the g∈R 2 denotes grid point coordinates, H is the neighbour
cells of g and K is the Gaussian kernel weight:
σ
CellOracle performs three iterative cycles in the default setting,
s
p
u
le
ff
m
ic
e
ie
n
n
ta
t
r
t
y
o
F
p
i
r
g
e
s
d
. 4
ic
a
t
n
th
d
e
5
d
).
i
W
re
e
c
a
ti
v
o
o
n
i
a
d
l
a
it
h
y
i
o
g
f
h
c
e
h
r
a
n
n
u
g
m
es
b
i
e
n
r
c
o
e
f
l
i
l
t
i
e
d
r
e
a
n
ti
t
v
it
e
y
c
(
a
S
l
u
cu
p-
-
K
σ
(v
0
,v
1
)=exp 

 − v
2
0
σ
−
2
v 1 2

 .
lations as it might lead to unexpected behaviour. Of note, CellOracle
performs the calculations cluster-wise after splitting the whole GEM
into gene expression submatrices on the basis of the assumption that Calculation of pseudotime gradient vector field and inner-
each cluster has a unique GRN configuration. Also, gene expression val- product score to generate a perturbation score
ues are checked between each iterative calculation to confirm whether To aid the interpretation of CellOracle simulation results, we quantify
the simulated shift corresponds to a biologically plausible range. If the the similarity between the differentiation vector fields and KO simula-
expression value for a gene is negative, this value is adjusted to zero. tion vector fields by calculating their inner-product value, which we
The code in this step is implemented from scratch, specifically for Cel- term the perturbation score (PS) (Extended Data Fig. 4). Calculation
lOracle perturbations using NumPy, a python package for numerical of the PS includes the following steps:
computing (https://numpy.org). (i) Differentiation pseudotime calculation
(iii) Estimation of transition probabilities Differentiation pseudotime is calculated using DPT, a diffusion-map-
From the previous steps, CellOracle produces a simulated gene expres- based pseudotime calculation algorithm, using the scanpy.tl.dpt func-
sion shift vector ΔX
simulated
∈R 1×N representing the simulated initial tion (Extended Data Fig. 4a, left). CellOracle also works with other
gene expression shift after TF perturbation. Next, CellOracle aims to pseudotime data, such as Monocle pseudotime and URD pseudo-
project the directionality of the future transition in cell identity onto time data. For the Farrell et al.32 zebrafish scRNA-seq data analysis, we
the dimensional reduction embedding (Fig. 1a, right and Extended used pseudotime data calculated by the URD algorithm, as described
Data Fig. 1e). For this task, CellOracle uses a similar approach to Velocyto previously32.
(https://github.com/velocyto-team/velocyto.py). Velocyto visualizes (ii) Differentiation vector calculation based on pseudotime data
future cell identity on the basis of the RNA-splicing information and The pseudotime data are transferred to the n by n 2D grid points (n = 40
calculated vectors from RNA synthesis and degradation differential as default) (Extended Data Fig. 4a, centre). For this calculation, we imple-
equations. CellOracle uses the simulated gene expression vector mented two functions in CellOracle: KNN regression and polynomial
ΔX instead of RNA-velocity vectors. regression for the data transfer. We choose polynomial regression when
simulated
First, CellOracle estimates the cell transition probability matrix the developmental branch is a relatively simple bifurcation, as is the
P∈R M×M (M is number of cells): p
i,j
, the element in the matrix P, is case for the Paul et al.16 haematopoiesis data. We used KNN regres-
defined as the probability that cell i will adopt a similar cell identity to sion for a more complex branching structure, such as the Farrell et al.32
zebrafish development data. Then, CellOracle calculates the gradient
of pseudotime data on the 2D grid points using the numpy.gradient GRN inference method
function, producing the 2D vector map representing the direction of After preprocessing, the exact same data were subjected to each GRN
differentiation (Extended Data Fig. 4a, right). inference algorithm to compare results fairly. We followed the pack-
(iii) Inner-product value calculation between differentiation and KO age tutorial and used the default hyperparameters unless specified
simulation vector field otherwise. Details are as follows. WGCNA: we used WGCNA v.1.68 with
Then, CellOracle calculates the inner-product score (perturbation score R 3.6.3. WGCNA requires the user to select a ‘power parameter’ for
(PS)) between the pseudotime gradient vector field and the perturba- GRN construction. We first calculate soft-thresholding power using
tion simulation vector field (Extended Data Fig. 4b). The inner product the ‘pickSoftThreshold’ function with networkType=“signed”. Other
between the two vectors represents their agreement (Extended Data hyperparameters were set to default values. Using the soft-thresholding
Fig. 4c), enabling a quantitative comparison of the directionality of power value, the ‘adjacency’ function was used to calculate the GRN
the perturbation vector and differentiation vector with this metric. adjacency matrix. The adjacency matrix was converted into a linklist
(iv) PS calculation with randomized GRN model to calculate PS cut-off object by the ‘getLinkLis’ function and used as the inferred value of
value the WGCNA algorithm. DCOL: we used nlnet v.1.4 with R 3.6.3. The
CellOracle also produces randomized GRN models. The randomized ‘nlnet’ function was used with default parameters to make the DCOL
GRNs can be used to generate dummy negative control data in Cel- network. The edge list was extracted using the ‘as_edgelist’ function.
lOracle simulations. We calculated cut-off values for the negative PS DCOL infers an undirected graph without edge weights. We assigned
analysis in the systematic KO simulation. First, the negative PS is cal- the value 1.0 for the inferred network edge and 0.0 for other edges.
culated for all TFs using either a normal or a randomized vector. The The assigned value was used as the output of the DCOL algorithm.
score distribution generated from the randomized vector was used as GENIE3: we used GENIE3 v.1.8.0 with R 3.6.3. The GRN weight matrix
a null distribution. We determined the cut-off value corresponding to a was calculated with the processed scRNA-seq data using the ‘GENIE3’
false-positive rate of 0.01 by selecting the 99th percentile value of PSs function and converted into a GRN edge and weight list by the ‘getLin-
generated with randomized results (Extended Data Fig. 3g). kList’ function. GENIE3 provides a directed network with network
weight. The weight value was directly used as the inferred value of the
Network analysis GENIE3 algorithm. SCENIC: we used SCENIC v.1.2.2 with R 3.6.3. The
In addition to CellOracle’s unique gene perturbation simulation, Cel- SCENIC GRN calculation involves multiple processes. The calculation
lOracle’s GRN model can be analysed with general network structure was performed according to SCENIC’s tutorial (https://rdrr.io/github/
analysis methods or graph theory approaches. Before this network aertslab/SCENIC/f/vignettes/SCENIC_Running.Rmd). First, we created
structure analysis, we filter out weak or insignificant connections. GRN the initialize settings configuration object with ‘initializeScenic’. Then
edges are initially filtered on the basis of P values and absolute values of we calculated the co-expression network using the ‘runGenie3’ func-
edge strength. The user can define a custom value for the thresholding tion, following the GRN calculation with several SCENIC functions;
according to the data type, data quality and aim of the analysis. After runSCENIC_1_coexNetwork2modules, runSCENIC_2_createRegulons
filtering, CellOracle calculates several network scores: degree central- and runSCENIC_2_createRegulons. We used the ‘10kb’ dataset for the
ity, betweenness centrality and eigenvector centrality. It also assesses promoter information range. The calculated GRN information was
network module information and analyses network cartography. For loaded with the ‘loadInt’ function, and the ‘CoexWeight’ value was used
these processes, CellOracle uses igraph (https://igraph.org). as the inferred value of the SCENIC algorithm.
Validation and benchmarking of CellOracle GRN inference Ground-truth data preparation for GRN benchmarking
To test whether CellOracle can correctly identify cell-type- or Cell-type-specific ground-truth GRNs were generated in the same man-
cell-state-specific GRN configurations, we benchmarked our new ner as in a previous benchmarking study55. Here, we selected tissues
method against diverse GRN inference algorithms: WGCNA, DCOL, commonly available in the Tabula Muris scRNA-seq dataset, mouse
GENIE3 and SCENIC. WGCNA is a correlation-based GRN inference algo- sci-ATAC-seq atlas data and ground-truth datasets: heart, kidney, liver,
rithm, which is typically used to generate a non-directional network53; lung and spleen. The ground-truth data were constructed as follows. (i)
DCOL is a ranking-based non-linear network modelling method54; and Download all mouse TF ChIP–seq data as bed files from the ChIP-Atlas
GENIE3 uses an ensemble of tree-based regression models, and aims database (https://chip-atlas.org). (ii) Remove datasets generated under
to detect directional network edges. GENIE3 emerged as one of the non-physiological conditions. For example, we removed ChIP–seq
best-performing algorithms in a previous benchmarking study55. The data from gene KOs or adeno-associated virus treatment. (iii) Remove
SCENIC algorithm integrates a tree-based GRN inference algorithm data that include fewer than 50 peaks. (iv) Select peaks detected in
with information on TF binding7. multiple studies. (v) Group data by TF and remove TFs if the number
of detected target genes is less than ten peaks. (vi) Convert data into a
Preparation of input data for GRN inference binary network: each network edge is labelled either 0 or 1, represent-
We used the Tabula Muris scRNA-seq dataset for GRN construction ing its ChIP–seq binding between genes. These steps yielded tissue- or
input data56. Cells were subsampled for each tissue on the basis of cell-type-specific ground-truth data for 80 TFs, corresponding to 1,298
the original tissue-type annotation: spleen, lung, muscle, liver and experimental datasets.
kidney. Data for each tissue were processed using the standard Seurat
workflow, including data normalization, log transformation, finding GRN benchmarking results
variable features, scaling, principal component analysis (PCA) and GRN inference performance was evaluated by the AUROC and the early
Louvain clustering. The data were downsampled to 2,000 cells and precision ratio (EPR), following the evaluation method used in a pre-
10,000 genes using highly variable genes detected by the correspond- vious benchmarking study55. CellOracle and SCENIC outperformed
ing Seurat function. Cell and gene downsampling were necessary to WGCNA, DCOL and GENIE3 based on AUROC (Extended Data Fig. 2a).
run the GRN inference algorithms within a practical time frame: we This is because CellOracle and SCENIC filter out non-transcriptional
found that some GRN inference algorithms, especially GENIE3, take a connections (that is, non-TF–target gene connections) and other
long time with a large scRNA-seq dataset, and GENIE3 could not com- methodologies detect many false-positive edges between non-TFs.
plete the GRN inference calculation even after several days if the whole CellOracle with a scATAC-seq atlas base GRN performed better than
dataset was used. CellOracle with a promoter base GRN and SCENIC. This difference was
Article
mainly derived from sensitivity (or true-positive rate). With scATAC-seq original gene expression, which correspond to the simulated expression
data, CellOracle captures a higher number of regulatory candidate level (termed ‘simulation gene expression level’ here for explanatory
genes. Considering EPR, representing inference accuracy for top k purposes: X = X + ΔX ). We evaluate all
simulation gene expression level original simulated,
network edges (k = number of network edges with the label ‘1’ in the genes, comparing the simulation gene expression level with the original
ground-truth data), CellOracle performed well compared to other gene expression distribution. To detect out-of-distribution data, we
approaches (Extended Data Fig. 2b): GENIE3 and WGCNA assigned a calculated the maximum exceedance percentage, representing the
high network edge weight to many non-transcriptional connections, percentage difference of the maximum value of the simulated gene
resulting in many false-positive edges for the highly ranked inferred expression level compared to the maximum value of the wild-type
genes. gene expression value. The higher maximum exceedance indicates a
The CellOracle GRN construction method was analysed further to bigger difference between simulated and wild-type values, identifying
assess the contribution of the base GRN. We performed the same GRN out-of-distribution values. For the Spi1 KO simulation with the Paul
benchmarking with a scrambled motif base GRN or no base GRN. For the et al. haematopoiesis dataset16, we present the top four genes showing
scrambled motif base GRN, we used scrambled TF-binding-motif data the maximum exceedance values (Supplementary Fig. 2). The simula-
for the base GRN construction. For the no base GRN analysis, selection tion expression levels of even these genes appear very similar to the
of regulatory candidate genes was skipped, and all genes were used as original wild-type distributions of gene expression. For example, in
regulatory candidate genes. As expected, the AUROC scores decreased the Ly86 simulated value distribution, 99.963% of all cells are within
when we used the scrambled motif base GRN (ranked 12/13 in AUROC, the wild-type gene expression range. Only 0.037% of cells exhibit a
11/13 in EPR; Extended Data Fig. 2a,b), decreasing even further in the Ly86 gene simulation value outside the wild-type distribution, but
no base GRN model (13/13; Extended Data Fig. 2a,b). The scrambled the maximum difference is only 3.2%. We designed CellOracle to simu-
motif base GRN did not detect many regulatory candidate TFs, pro- late a minimal relative shift vector rather than an out-of-distribution
ducing lower sensitivity. However, the scrambled motif base GRN can prediction, confirmed by this analysis. The functions we have used
still work positively by removing connections from non-TF genes to for these analyses are implemented in CellOracle. Users can check
TFs, functioning to filter out false-positive edges, and resulting in a simulation value distributions, and CellOracle will produce a warning
better score relative to the no base GRN model. In summary, the base if out-of-distribution simulations occur.
GRN is primarily important to achieve acceptable specificity, and the To further explore the minimum number of cells with minor
scATAC-seq base GRN increases sensitivity. out-of-distribution values, we generated a simulation vector in which
Next, we used CellOracle after downsampling cells to test how cell the out-of-distribution values are clipped into the wild-type distribu-
number affects GRN inference results. Cells were downsampled to tion range. The simulated cell-identity shift vector of clipped values
400, 200, 100, 50, 25 and 10 cells and used for GRN analysis with the is indistinguishable compared to the original results (Supplementary
scATAC-seq base GRN. GRNs generated with 400, 200, 100 and 50 cells Fig. 2b–e), confirming that the CellOracle simulation is not relying on
received comparable or slightly reduced AUROC scores. The AUROC these out-of-distribution values. The out-of-distribution value can be
score decreased drastically for GRNs generated with 25 and 10 cells clipped if we add ‘clip_delta_X=True’ in the CellOracle signal propaga-
(Extended Data Fig. 2c). EPR was relatively robust even with small cell tion function. Thus, users can ensure the simulation is not relying on
numbers (Extended Data Fig. 2d). out-of-distribution values.
We performed additional benchmarking to investigate data
compatibility between the base GRN and scRNA-seq data sources. CellOracle simulation results generated with randomized GRN
A tissue-specific base GRN was generated separately using bulk or no signal propagation
ATAC-seq data57. We focused on the same five tissue types as above. We performed KO simulation with randomized GRN models to clarify
Unprocessed bulk ATAC-seq data were downloaded from the NCBI the necessity of the GRN signal propagation simulation. In addition,
database using the SRA tool kit (spleen: SRR8119827; liver: SRR8119839; we calculated cell-identity vectors without the signal propagation
heart: SRR8119835; lung: SRR8119864; and kidney: SRR8119833). After step; the cell-identity shift vector was calculated solely on the basis of
FASTQC quality check (https://www.bioinformatics.babraham.ac.uk/ input TF expression loss, thus representing the information from the
projects/fastqc/), fastq files were mapped to the mm9 reference expression pattern of only a single TF. The vector map in Supplementary
genome and converted into bam files. Peak calling using HOMER Fig. 3 shows Gata1 KO simulation results and Spi1 KO simulation results
was used to generate bed files from the bam files. Peak bed files were with an intact GRN coefficient matrix, randomized GRN matrix or no
then annotated with HOMER. Peaks within 10 kb around the TSS were GRN signal propagation. The randomized GRN analysis results and
used. Peaks were sorted by the ‘findPeaks Score’ generated by the no GRN signal propagation results show only slight cell-identity shift
HOMER peak-calling step, and we used the top 15,000 peaks for base vectors (Supplementary Fig. 3b,c,e,f). Although very subtle vectors
GRN construction. These peaks were scanned with the gimmemotifs can be observed, most expected simulation results are not obtained.
v.5 vertebrate motif dataset, which is the same motif set we use for Thus, we confirmed that the GRN signal propagation strategy has an
scATAC-seq base GRN construction. essential role in the CellOracle KO simulation.
We compared benchmarking scores between GRN inference results
generated from different base GRNs. Overall, GRN construction per- Evaluation of signal propagation number
formed best when the same tissue type for ATAC-seq base GRN construc- We next tested the number of iterations at the signal propagation step.
tion and scRNA-seq was used (10/13 in AUROC, 11/13 in EPR; Extended We performed KO simulations using two independent mouse haema-
Data Fig. 2e,f). The score was lower with different tissue types combined topoiesis datasets: Paul et al.16 and Dahlin et al.58. For several TFs, we
between the base GRN and scRNA-seq data. In summary, benchmarking tested different numbers of signal propagation rounds in the KO simula-
confirmed that our GRN construction method performs well for the tions across independent clusters. First, focusing on the Paul dataset,
task of transcriptional GRN inference. simulation vector fields for Spi1 and Gata1, with 0, 1 and 3 rounds of
signal propagation, were investigated (Supplementary Fig. 4). The
CellOracle evaluation simulation under hyperparameter n = 0 shows the vector calculated
Evaluation of simulation value distribution range. We investigated without any signal propagation within the GRN; that is, the vector is
a range of simulated values to confirm that the signal propagation calculated from only the difference of the input TF gene expression
step does not generate an out-of-distribution prediction. Specifical- shift. This n = 0 simulation shows almost no phenotype, showing the
ly, we assessed the distribution of the sum of the simulated shift and necessity of the GRN signal propagation process. Next, a comparison
