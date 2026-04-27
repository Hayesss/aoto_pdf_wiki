---
source_path: /mnt/c/Users/Administrator/Zotero/storage/X2SDMBJY/Heumos 等 - 2024 - Pertpy an end-to-end framework for perturbation analysis.pdf
ingested: 2026-04-23
sha256: ac9cccd1695314f0
---

nature methods
Article https://doi.org/10.1038/s41592-025-02909-7
Pertpy: an end-to-end framework for
perturbation analysis
Received: 4 August 2024 Lukas Heumos 1,2,3, Yuge Ji1,2, Lilly May 1,4, Tessa D. Green 5, Stefan Peidli6,7,8,
Xinyue Zhang1,4, Xichen Wu1,4, Johannes Ostner1,9, Antonia Schumacher 1,
Accepted: 16 October 2025
Karin Hrovatin 1,2, Michaela Müller 1, Faye Chong1,10, Gregor Sturm 11,
Published online: 31 December 2025 Alejandro Tejada1, Emma Dann12, Mingze Dong 13, Gonçalo Pinto1,
Mojtaba Bahrami 1,2, Ilan Gold1, Sergei Rybakov1,4, Altana Namsaraeva1,14,
Check for updates Amir Ali Moinfar 1,4, Zihe Zheng1, Eljas Roellin 1, Isra Mekki15, Chris Sander5,
Mohammad Lotfollahi 1,13,16, Herbert B. Schiller3,17 & Fabian J. Theis 1,2,4
Advances in single-cell technology have enabled the measurement of
cell-resolved molecular states across a variety of cell lines and tissues
under a plethora of genetic, chemical, environmental or disease
perturbations. Current methods focus on differential comparison or
are specific to a particular task in a multi-condition setting with purely
statistical perspectives. The quickly growing number, size and complexity
of such studies require a scalable analysis framework that takes existing
biological context into account. Here we present pertpy, a Python-based
modular framework for the analysis of large-scale single-cell perturbation
experiments. Pertpy provides access to harmonized perturbation
datasets and metadata databases along with numerous fast and
us er -f ri en dly im pl em en ta tions of both established and novel methods,
such as automatic metadata annotation or perturbation distances, to
efficiently analyze perturbation data. As part of the scverse ecosystem,
pertpy interoperates with existing single-cell analysis libraries and is
designed to be easily extended.
Understanding cellular response to stimuli is crucial for describing bio- responses in primary human T cells5. However, the size and complex-
logical phenomena and mechanisms. Single-cell data have increasingly ity of high-throughput perturbation screens can pose considerable
shifted from observational experiments to perturbation experiments, interpretation challenges, lacking meaningful lower-dimensional
encompassing genetic modifications, chemical treatments, physical representations and additional context regarding cell lines or pertur-
interventions, environmental changes, diseases and combinations bations. Current perturbation analysis frameworks such as MUSIC6,
thereof. Technologies such as Perturb-seq1, CROP-seq2 and Sci-plex3 ScMAGeCK7, SCEPTRE8, GSFA9 and FR-Perturb10 primarily focus on
leverage single-cell readouts to capture perturbations at scale. By moni- CRISPR perturbation analysis, neglecting other perturbation data
toring resulting shifts in intrinsic cell states, single-cell perturbation types and perturbation analysis steps. Furthermore, no current analysis
analyses offer insights into changes in gene programs, shared and diver- framework exists that scales to genome-scale datasets11, contextual-
gent responses across tissues, drug targets and interactions, changes izes data with public annotations and uses common data structures
in cell type frequency and cell−cell interactions after perturbation. across tools (Extended Data Table 1). In addition, many tools suffer
Statistical and machine-learning-based analysis methods have from maintenance issues or are confined to the R ecosystem, compli-
been developed for these complex data, resulting in the discovery of, for cating analysis. Other widely used frameworks in the single-cell field,
example, cell states associated with autism risk genes4 or stimulation such as scirpy12 for adaptive immune receptor data and scvi-tools13 for
A full list of affiliations appears at the end of the paper. e-mail: fabian.theis@helmholtz-muenchen.de
Nature Methods | Volume 23 | February 2026 | 350–359 350
Article https://doi.org/10.1038/s41592-025-02909-7
probabilistic modeling, have demonstrated the importance of enabling Table 1 | Summary of implemented methods
efficient multimodal data analysis while providing flexible building
blocks for developers. Inspired by their impact and the lack of effi- Analysis step Tool or algorithm Original authors
cient frameworks for perturbation data, we present a new framework Datasets Data loaders Peidli et al.43
focused on perturbation data within scverse14.
Metadata annotation API requests to public Novel
Pertpy, a framework for perturbation analysis in Python, is pur- databases
pose built to organize, analyze and visualize complex perturbation
gRNA assignment Threshold-based Adamson et al. 66
datasets. Pertpy is flexible and can be applied to datasets of different Poisson−Gaussian Repogle et al. 11
assays, data types, sizes and perturbations, thereby unifying previ- mixture model
ous data-type-specific or assay-specific single-problem approaches.
Differential gene ‘Formulaic’ interface Novel
Designed to integrate external metadata with measured data, it ena- expression
bles unprecedented contextualization of results through swiftly built,
Pooled CRISPR screens Mixscape Papalexi et al. 19
experiment-specific pipelines, leading to more robust outcomes. To
evaluate methods and obtained representations for perturbations, we Differential abundance Milo Dann et al.39
scCODA 2.0 Büttner et al.37
implemented a series of shared metrics. The wide array of use cases and tascCODA 2.0 Ostner et al.38
different types of growing datasets are addressed by pertpy through
MCPs DIALOGUE Jerby-Arnon and
its sparse and memory-efficient implementations, which leverage the
Regev40
parallelization and graphics processing unit (GPU) acceleration library
JAX15, thereby making them substantially faster than original imple- Enrichment Drug2Cell Kanemaru et al.67
mentations (Extended Data Fig. 1). We demonstrate this versatility by Perturbation response Distances and metrics Novel
applying pertpy to three different, popular, single-cell RNA sequencing evaluation Augur Skinnider et al.68
CINEMA-OT Squair et al.69
(scRNA-seq) perturbation use cases. To show how pertpy can discover Dong et al.41
new gene programs, we study a CRISPR activation (CRISPRa) screen
Embedding Perturbation spaces Novel
(Perturb-seq)16, projecting it onto a meaningful perturbation space and
evaluating the effect of different preprocessing strategies. Moreover,
we demonstrate how pertpy can be used to deconvolve perturbation The first data transformation step assigns guide RNAs (gRNAs) to
responses into viability-dependent and viability-independent compo- cells. These gRNAs are short RNA sequences that direct Cas9 nuclease
nents in a large-scale gene expression and drug response screen17 by to specific genomic targets. In single-cell CRISPR screens, each cell typi-
integrating metadata from existing databases. Finally, we decipher com- cally receives one gRNA (low multiplicity of infection (MOI)), although
positional changes and rank perturbation effects in a triple-negative some experimental designs allow for multiple guides per cell (high
breast cancer (TNBC) study18. Whereas previously, a user would sepa- MOI). This makes accurate guide-to-cell assignment crucial for linking
rately download cell line or perturbation information from scattered phenotypic changes to specific genetic modifications. Pertpy provides
databases while piecing together analysis tools from different, incom- a thresholding and a Poisson−Gaussian mixture model11 approach that
patible ecosystems, it is now possible to efficiently analyze complex has been shown to perform well in recent benchmarks24, accommodat-
perturbation datasets end to end with integrated biological context. ing both low and high MOI scenarios. This assignment step is required
We provide online links to tutorials with more than 15 additional for downstream analyses, including quality control metrics, perturba-
use cases that demonstrate pertpy’s usage with datasets spanning a tion efficiency assessment and statistical aggregation of phenotypic
variety of cell lines and perturbation conditions, ranging from CRISPR effects across cells containing identical guides.
screens19 to inflammation20 and COVID-19 severity states21. Pertpy is In a second step, confounding factors such as unwanted techni-
accessible as an extendable, user-friendly, open-source software pack- cal variation and other single-cell-specific quality control issues are
age hosted at https://github.com/scverse/pertpy and installable from addressed. Technical variation between experimental batches, arising
PyPI. It comes with comprehensive documentation, tutorials and use from differences in sample processing, reagent lots or sequencing
cases available at https://pertpy.readthedocs.io. runs, can introduce systematic biases that confound biological signals.
These so-called batch effects are particularly challenging in perturba-
Results tion experiments where treatments may be applied across multiple
Pertpy enables fast and scalable perturbation analyses experimental rounds or where controls are processed separately from
Pertpy includes methods for analysis of single and combinatorial perturbed samples. Complexity is further compounded when studying
perturbations covering diverse types of perturbation data, including combinatorial perturbations, where systematic batch variations could
genetic knockouts, drug screens and disease states. The framework be mistaken for interaction effects between different treatments. As
is designed for flexibility, offering more than 100 composable and pertpy is integrated with the scverse ecosystem, users of pertpy can
interoperable analysis functions organized in modules that further ease seamlessly integrate established batch correction methods25,26 to
downstream interpretation and visualization (Table 1). These modules disentangle technical artifacts from true perturbation responses.
host fundamental building blocks for implementation and methods After diligent quality control, a typical analysis with pertpy starts
that share functionality and can be chained into custom pipelines. To by curating the perturbation annotations against ontologies such as
facilitate setting up these pipelines, pertpy guides analysts through a Cell Line Ontology27 or Drug Ontology28 and enriching the perturba-
general analysis pipeline (Fig. 1) with the goal of elucidating underlying tions with additional metadata obtained from Cancer Dependency
biological mechanisms by examining how specific interventions alter Map (DepMap) and Genomics of Drug Sensitivity in Cancer (GDSC)29
cellular states and interactions. for cell lines, Connectivity Map (CMap)30 for mechanisms of action and
The inputs to a typical analysis with pertpy are unimodal scRNA-seq the PubChem31 and ChEMBL32 databases for drugs (Methods).
or multimodal perturbation readouts stored in AnnData22 or MuData23 The application of CRISPR can exhibit variable efficacy in affecting
objects. Although pertpy is primarily designed to explore perturba- gene expression. Pertpy’s fast Mixscape19 implementation accounts for
tions such as genetic modifications, drug treatments, exposure to this by classifying targeted cells based on their response to a perturba-
pathogens and other environmental conditions, its utility extends to tion, analyzing each cell’s perturbation signature to determine if the
various other perturbation settings, including diverse disease states cell was successfully perturbed (Methods and Extended Data Fig. 1).
where experimental perturbations have not been applied. As the number of applied perturbations increases, comparing and
Nature Methods | Volume 23 | February 2026 | 350–359 351
Article https://doi.org/10.1038/s41592-025-02909-7
Data transformation
1 Perturbation type 2 Perturbation data
Control
Perturbation 1
Perturbation 2
Perturbation 1 + 2
...
Variables
Data
interpreting them becomes increasingly challenging. Pertpy provides whether the experiment involved multiple cell types or a number of
several distinct ways to learn biologically interpretable perturbation experimental perturbations.
spaces that depart from the individualistic perspective of cells, instead Gene expression changes between experimental conditions are
generating a single embedding per perturbation that summarizes crucial for understanding cellular responses to perturbations. Differential
cellular responses (Methods). This specialized space, termed a per- gene expression analysis helps researchers identify which genes signifi-
turbation space, represents the collective impact of perturbations cantly change their expression levels when cells are exposed to different
on cells and serves as potential input for downstream analysis16,33. stimuli or treatments. Although scanpy34 is widely used for single-cell
Generally, pertpy’s analysis pipeline can be adapted depending on analysis, it lacks support for complex experimental designs that account
Nature Methods | Volume 23 | February 2026 | 350–359 352
observations
Multidimensional
Observations
3 Metadata annotation
Preprocessing
Not targeted
Not perturbed 1.5
Knockout
1.0
0.5
0
−1 0 1
Perturbation score
ytisned
lleC
Differential gene
expression
10.0 Gene 1
7.5 Gene 2
5.0
2.5
0
–6 –3 0 3 6
log fold change
4 5 Perturbation space
Perturbation 1
Control
Perturbation 2 Perturbation 1 + 2
Program 1
Program 2
Unknown program
P
gol–
01
Distances
Response prediction
δ δ δ δ
MCPs
Cell type 1
Cell type 2
Cell type m
Mechanisms of action
enrichment
Unknown
Beta-blockers
1
eneG
2
eneG
n
eneG
MCP 1 MCP 2
1
eneG
2
eneG
n
eneG
a b
Knowledge inference
Differential abundance
Enriched in A
A Enriched in B
B
* C
*
* D
* E
* * –1.0 0 1.0
log fold change
project score 2
PRISM
mondo
Connectivity Map
Disease
Ontology
CancerRxGene
DepMap
Human
Phenotype
Ontology
Fig. 1 | Modules of the pertpy framework. a, Unimodal or multimodal single-cell successfully or not successfully perturbed. Together, these modules enable the
perturbation data originating from genetic modifications, chemical treatments, calculation of a meaningful perturbation space. b, Pertpy enables downstream
physical interventions, environmental changes or diseases are enriched with analyses, depending on the question of interest. These include differential
metadata from several databases. During preprocessing, confounding factors expression analysis, response prediction, determination of MCPs, calculation of
such as cell cycle and batch effects may be removed. Targeted cells are labeled as distance between perturbations and mechanism of action enrichment.
Article https://doi.org/10.1038/s41592-025-02909-7
for multiple conditions, batch effects and nested comparisons simulta- Built on the scverse14 ecosystem, pertpy ensures seamless interop-
neously. Pertpy fills this gap by providing an intuitive interface for dif- erability with existing single-cell omics workflows and can be combined
ferential gene expression that supports complex designs and contrasts, with tools such as decoupler-py44 and NetworkCommons45 for tasks
which is needed for multi-condition data (Methods). Currently, pertpy such as context-specific inference of protein interaction networks
supports PyDESeq235, edgeR36, Wilcoxon tests and t-tests. This interface while being purposefully extensible to address new challenges. Base
is accompanied by a suite of plotting functions including visualizations classes for additional perturbation spaces, distances, differential gene
such as volcano plots, paired sample expression plots and multi-condition expression tests and other components are provided to facilitate swift
heatmaps. Going beyond differential gene expression at scale, both development. We additionally provide a dataset module with more than
annotated metadata and differentially expressed genes can be used as 30 public loadable perturbational single-cell datasets in AnnData and
input for further pertpy modules such as gene set enrichment tests to MuData format, building upon and extending scPerturb43 to kickstart
uncover the biological effects induced by the perturbations (Methods). analysis, development and benchmarking with pertpy. The meta-
Tracking cell type compositional shifts is crucial for understand- data of the datasets were curated against public ontologies to enable
ing the underlying mechanisms of disease progression, tissue regen- swift dataset integration and large-scale machine learning, including
eration and developmental biology, offering insights into cellular foundational models.
responses and adaptations. Pertpy offers two distinct methods for
detecting compositional shifts, both utilizing a common MuData-based Learning and exploring perturbation representations with
data structure. If labeled groups are available, pertpy provides pertpy
accelerated and scalable implementations of scCODA37 2.0 and its To demonstrate pertpy’s ability to learn meaningful perturbation
cell type hierarchy-aware extension tascCODA38 2.0 (Methods and spaces, we examined a publicly available CRISPRa screen dataset ini-
Extended Data Fig. 1). Both approaches employ Bayesian methods to tially presented by Norman et al.16, consisting of 111,255 single-cell
elucidate cell type compositional changes. If no labeled groups are transcriptomes of K562 cells subjected to 287 single gene and gene
available or continuous proportions are expected, such as during pair perturbations (Fig. 2a). We use this dataset to show how genetic
developmental processes, pertpy implements a scalable version of interactions through combinatorial expression of genes lead to cellular
Milo, previously unique to the R ecosystem39, which conducts differen- and organismal gene programs and phenotypes. We further use pertpy
tial abundance tests by assigning cells to overlapping neighborhoods to investigate how different perturbation-specific preprocessing strate-
within a k-nearest neighbor graph (Methods). gies affect the outcome. In particular, we examine whether different
Understanding how cells function together within tissues is a strategies may inadvertently remove true biological signals, such as
major challenge. Multicellular programs (MCPs) refer to the orches- the cell cycle effects induced by CDKN2A perturbations.
trated activities of various cell types that collaborate to create complex After initial preprocessing (Methods), we test three
functional structures at the tissue scale. Pertpy’s fast implementation of perturbation-specific processing strategies: (1) computing cell-specific
DIALOGUE40 uncovers MCPs through a combination of factor analysis perturbation signatures based on the 20 nearest neighbor control cells
and hierarchical modeling, owing to a fast input-order-invariant linear of a perturbed cell and filtering out targeted cells that escaped pertur-
programming solver and a new, fast test to determine significantly bation based on this signature (Methods); (2) computing cell-specific
associated MCP genes (Methods). perturbation signatures using all control cells within the same Gel
Not all cell types are equally affected by perturbations. Pertpy’s Bead-in-Emulsion (GEM) group (that is, cells processed in the same
fast implementation of Augur (Extended Data Fig. 1) ranks cell types sequencing lane) to detect and filter out unperturbed cells (Methods);
based on their response to perturbations by training machine learn- and (3) no perturbation-signature-based filtering of cells.
ing models to predict experimental labels within each cell type and Pertpy’s Mixscape19 implementation supports strategies (1)
then ranking these cell types by the models’ accuracy metrics across and (2), facilitating comparison of preprocessing strategies. After
multiple cross-validation runs (Methods). Furthermore, understand- applying each of the three strategies, we project the normalized gene
ing the dynamics of cellular response to various stimuli is crucial when expression of the remaining cells into a perturbation space using
experimental exploration of all possible conditions is unfeasible. the penultimate layer of our multilayer perceptron (MLP)-based
CINEMA-OT41, via scalable pertpy implementation, extends this con- discriminator classifier for each processing strategy (Methods and
cept by distinguishing between confounding variations and the effect Extended Data Fig. 2). We found that all strategies yielded similar per-
of perturbations, achieving an optimal transport match that mirrors turbation spaces (Extended Data Fig. 2i), suggesting that, for this data-
counterfactual cell pairings (Methods). These pairings enable analysis set, the approach without perturbation-signature-based cell filtering
of potentially causal perturbation responses, allowing for individual is preferable. This is expected because the CRISPRa approach used for
treatment effect analysis, clustering of responses, attribution analysis this dataset does not suffer from cells escaping a perturbation through
and examination of synergistic effects. in-frame mutations, as would be expected in CRISPR−Cas9 screens.
For accurate statistical comparison and measurement of pertur- Examining this perturbation space, we observe that explicitly
bation effects, it is essential to employ distance metrics between cell training the classifier to distinguish between individual perturba-
groups. A suitable metric quantifies divergence or similarity in expres- tions results in clustering of perturbations with similar effects on the
sion patterns of cells under different perturbations, enabling inference cell, as indicated by the affected gene program as originally labeled
of unique or common mechanisms. Different types of distance metrics by Norman et al.16. We assessed the importance of individual input
make varying assumptions on the shape of the data and emphasize genes in the classifier’s assignment of a cell to a specific perturbation
specific aspects of difference. For instance, optimal transport-based using integrated gradients46 (Methods). By averaging these feature
distances, such as the Wasserstein distance42, assume correspondence importances for each annotated gene program, we demonstrate
between cell populations, whereas the Mahalanobis distance focuses that the classifier prioritizes the respective targeted genes from the
on covariance structures and scale differences within the data. To cap- set of 4,000 highly variable input genes (for example, KLF1 for the
ture a wide range of distance metric types, pertpy implements more pro-growth program), highlighting their relevance to the prediction
than 18 different metrics, including, but not limited to, the Euclidean (Extended Data Fig. 3a). In addition to validating known annotations,
distance (E-distance)11,43 and the Wasserstein distance (Methods). All evaluating data in perturbation space also allows for refinement of
included metrics can also be used for perturbation testing through previous annotations. For instance, the perturbation TP73, character-
Monte Carlo permutation testing, allowing for the statistical evaluation ized as a pioneer factor gene program in the original publication16,
of perturbation distinguishability and efficacy (Methods). clusters with the G1 cell cycle perturbations when embedded using the
Nature Methods | Volume 23 | February 2026 | 350–359 353
Article https://doi.org/10.1038/s41592-025-02909-7
Perturbation status Cell cycle GEM group
1
2
3
4
5
6
7
G1 8
Control
Perturbed G2M
S
Cluster disentanglement (1)
COL2A1+KLF1
Gene program labeling KLF1
BAK1+KLF1
FOXA1+KLF1
TP73 KLF1 KLF1+TGFBR2
+MAP2K6
KLF1+SET
CLDN6+KLF1
CDKN1B CEBPE+KLF1
CDKN1A +CDKN1C IER5L AHR+KLF1
+CDKN1B +LYL1
CDKN1A
+CDKN1C
CDKN1A CDKN1B Cluster identification MAPK1+PRTG
CDKN1C IGDCC3+MAPK1
MIDN PRTG
S +Z N B A T I1 B10 PRTG IGDCC3 ETS2 ETS2+IGDCC3
+TGFBR2 +PRTG
+ IG ZB D T C B C 2 3 5 IGDCC3+PRTG
IGDCC3+TGFBR2
Gene program Cluster disentanglement (2) Control
Erythroid
MAP2K3+SLC38A2 G1 cell cycle
ELMSAN1
ELMSAN1+MAP2K3 Granulocyte apoptosis
ELMSAN1+MAP2K6 MAP2K6 Megakaryocyte
MAP2K3+MAP2K6 Pioneer factors
Pro-growth
MAP2K3
Unknown
discriminator classifier. This can be explained by the profound influ- effect on the neutrophil degranulation pathway (Fig. 2b). This use
ence of TP73 on the cell cycle47. Moreover, what the original authors case demonstrates the simplicity and effectiveness of combining
identified and labeled as a single pro-growth gene program cluster can several of pertpy’s modules into a new analysis pipeline, spanning
now be differentiated into two distinct clusters (mean squared error from quality control over perturbation space to the annotation of
(MSE) distance between the two subclusters: 0.46; mean pairwise MSE previously unlabeled gene programs.
distance between all gene programs: 0.29; Extended Data Fig. 3b).
Indeed, we found that although both clusters comprise perturba- Pertpy streamlines discovery for complex perturbation
tions targeting genes important for cell growth, one cluster mainly experiments
targets genes encoding Krüppel-like factors (KLFs), whereas the Advancements in multiplexing technologies have markedly increased
other comprises perturbations of mitogen-activated protein kinase the number of cell states that can be profiled in one experiment, result-
(MAPK) encoding genes. Projection of data into the perturbation ing in large perturbation screens. McFarland et al.17 introduced MIX-Seq,
space also allows for an in-depth exploration of clusters without gene an experimental assay that enables multiplexing of different cell lines
program annotation, enabling identification of a previously unan- within a single sequencing run. We use pertpy to efficiently analyze a
notated cluster comprising perturbations with a downregulating dataset comprising 172 cell lines and 13 drug treatments17.
Nature Methods | Volume 23 | February 2026 | 350–359 354
yawhtap
CAER
dehcirnE
Upregulated 1 × 10–7
L13a-mediated
silencing of cerulo-
plasmid expression
GTP hydrolysis
and joining of the 60S ribosomal subunit Cap-dependent
translation initiation
Neutrophil
degranulation
Innate
immune system
Immune system
P value
Gene count
Downregulated1 × 10–13
P
value
a
b
5
4
3
2
0 10
4
2
0
0 100
Gene count
Fig. 2 | Learning a unified perturbation space in combinatorial CRISPRa same lane on a 10x Genomics chip). b, Perturbation space highlighting gene
perturbation scRNA-seq data via pertpy’s perturbation space pipeline. programs that were originally labeled by Norman et al.16 and details of specific
a, UMAP representation of the preprocessed dataset, colored by perturbation subclusters of interest.
status, cell cycle phase and GEM group (that is, batch of cells processed in the
Article https://doi.org/10.1038/s41592-025-02909-7
12 UBALD2
NPAS2 RP11-879F14.2
10 MYEOV
8
IER3
6
4
2
0
−3 −2 −1 0 1 2
Intercept
Nature Methods | Volume 23 | February 2026 | 350–359 355
)eulav
P
.jda(01gol–
10
CEBPD ZEB2 UFD1L CDKN2D
ETV4
8
6
4
2
0
−3 −2 −1 0 1 2 3 4
Slope
)eulav
P
.jda(01gol–
a OncoTree lineage
McFarland et al. dataset:
•154,710 cells Perturbation Biliary tract Lung
• • 1 1 7 3 2 d c ru e g ll l p in e e rt s urbations A A Z fa D ti 5 n 5 ib 91 I J d Q a 1 sanutlin B ur la in d a d r e y r t / ract O Pa v n a c ry re /f a a s llopian tube
BRD3379 Navitoclax Bowel Peripheral nervous system
Bortezomib Prexasertib Breast
Pleura
Dabrafenib Taselisib CNS/brain
Prostate
Everolimus Trametinib Esophagus/
Gemcitabine Control stomach Skin
Cell line Head and neck Soft tissue
based Kidney Thyroid
Liver Uterus
Mechanism of action
Metadata
annotation BCL inhibitor
Control
EGFR inhibitor
Perturbation MDM inhibitor
based
MEK inhibitor
NFκB pathway inhibitor/proteasome inhibitor
PI3K inhibitor
RAF inhibitor
mTOR inhibitor
b
Ribonucleotide reductase inhibitor
NA
Drug sensitivity
Cell line
and
perturbation
based
Gene expression log FC = Intercept + Slope × Dabrafenib sensitivity
c Viability-independent response d Viability-dependent response
LN
IC50
GDSC2
scores
6
4
2
0
–2
–4
–6
0 5 10 15
CCLE bulk expression
noisserpxe
kluboduesP
10
Linear regression 12
Mean PCC: 0.876
8 10
6 8
6
4
4
2 2
0 0
log
density
1.0
0.5
0
−0.5
−1.0
0.6 0.8 1.0 Dabrafenib sensitivity (1 − AUC)
CF
gol
2DLABU
3
2
1
0
−1
0.6 0.8 1.0 Dabrafenib sensitivity (1 − AUC)
CF
gol
4VTE
Sensory perception 0.04
0.03
0 3 6 9
Signal transduction
Regulation of RUNX2 expression and activity
Downstream signaling events of B cell receptor
0 60 120 180
Gene count
P value
0.006
0.004
0.002 0
P value
Diseases of mitotic cell cycle 0.0025
S in e t m er a a p c h ti o o r n in s o A d f b m u e e r i r t t a o o n t i t R c r B c e 1 e g d l u l e l c a fe y ti c c o l t n e s 0.0020
Glycerophospholipid biosynthesis 0.0015
0 3 6 9
Interferon gamma signaling
Interferon signaling
Signaling by receptor tyrosine kinases
0 5 10 15
Gene count
P value
0.025
0.020
0.015
P value
Glycosaminoglycan metabolism
detalugerpU
detalugernwoD
detalugerpU
detalugernwoD
Fig. 3 | Deconvolution of viability-related response signatures in scRNA-seq UBALD2 (bottom left) shows that a change in UBALD2 expression in a cell line
drug screen data. a, Overview of the chemical perturbation dataset. Cell is observable, irrespective of the respective cell line’s sensitivity to dabrafenib
lines and perturbations were annotated with pertpy with additional metadata treatment. The top genes were used to perform GSEA (bottom right), with
facilitating detailed analysis. b, Linear regression model between single-cell enrichment P values computed using blitzGSEA65, which applies Kolmogorov–
expression data and GDSC profiles shows high correlation, reinforcing the Smirnov tests and gamma distribution fitting. The figure design is inspired by
high quality of the dataset. c, Volcano plot showing the value and significance Fig. 2c in the original publication that introduces the dataset17. d, The same
(two-sided t-test, Benjamini−Hochberg corrected) of the intercept of the fit linear as in c but for the slope of the linear regression models, indicating the
regression models for each gene (top), indicating the viability-independent viability-dependent response. adj., adjusted; CNS, central nervous system;
response. An example linear regression (±95% confidence interval) for the gene FC, fold change; PCC, Pearson correlation coefficient; NA, not available.
Article https://doi.org/10.1038/s41592-025-02909-7
Pertpy reduces annotation and quality control to just a few To rank perturbation effects, we used pertpy to calculate the MSE
steps. Its metadata module annotates cell lines with tissue-of-origin, distance between pre-treatment and post-treatment patients of the
cancer type and bulk expression profiles from the disease ontology four groups, selected for its strong performance on independent
OncoTree48 and the Cancer Cell Line Encyclopedia49 (CCLE). Com- benchmarks59. We found that patients responding to NACT alone had
pounds are annotated with their targets and mechanism of action from a greater distance between pre-treatment and post-treatment expres-
DepMap50, GDSC29 and CMap30 (Methods). After annotation, pertpy sion profiles compared to responders to anti-PD-L1 and NACT combina-
enables immediate visualization for exploratory analysis (Fig. 3a). tion therapy, implying that the latter led to potentially a less intense
Additionally, annotated bulk expression allows users to compare RNA response or was used in cases with a worse prognosis.
profiles of their cell lines with established public datasets, provid- To identify cell types involved in treatment response, we investi-
ing rapid quality control functionality. Comparative analysis of the gated shifts in cell type composition induced by the treatment. Track-
dataset revealed an average Pearsonʼs correlation coefficient of 0.88 ing cell type shifts is essential for understanding disease progression,
across all cell lines (Fig. 3b), demonstrating substantial consistency tissue regeneration and treatment responses, revealing key insights
with the cell line passages cataloged in the DepMap CCLE database into cellular adaptations. We applied pertpy’s implementation of the
and enabling the integration of additional screening data from the Bayesian model scCODA37 2.0 to the dataset per treatment (Methods).
DepMap PRISM project51. We found compositional shifts for NACT treatment in CD4 central
Pertpy significantly streamlines the replication and exten- memory, CD8 effector memory, CD8 tissue-resident memory and
sion of the original analyses by McFarland et al.17. We used pertpy naive T cells between disease stages but not for combination therapy
to fetch and annotate area under the dose−response curve (AUC) (Fig. 4d). To better understand whether cell types that are subject to
values for each cell line and perturbation pair from GDSC and PRISM compositional shifts are a part of a common cell circuit, we set out to
(Methods). This allows us to easily replicate the original statistical find shared gene expression signatures in several cell types that jointly
method to uncover viability-dependent and viability-independent act as tissue-level units, so-called MCPs40.
gene expression associations. We selected a different drug from We applied pertpy’s implementation of DIALOGUE40, which finds
the original analysis17, the BRAF inhibitor dabrafenib52, and used MCPs using matrix decomposition in conjunction with a novel, fast
pertpy to compute post-treatment log fold changes across 95 input-order-invariant linear programming solver, to the TNBC treat-
cell lines (Methods). We interpret the intercept and slope of the ment dataset, calculating 10 MCPs that can be assessed for associa-
linear regression on dabrafenib sensitivity (1 − AUC) to be the tion with treatment response (Methods). Exploratory analysis of
viability-independent and viability-dependent responses of the average MCP2 scores across seven distinct cell types in each patient
respective gene to dabrafenib (Methods and Fig. 3c,d). Notably, (Extended Data Table 2) indicated a potential association with treat-
we found that cancer-progression-linked genes ETV4, CDKN2D and ment response for both treatment groups, based on cell-type-specific
MYEOV53 displayed significant variation in their fitted response t-tests (adjusted P ≤ 1.1 × 10−1) (Extended Data Figs. 3a,b and 4a,b).
parameters (Fig. 3c,d). Additionally, our analysis identified enrich- Initial investigations of the MCP2-associated genes suggest involve-
ment of genes involved in interferon signaling in viability-dependent ment in heat shock protein activity and cytokine signaling (Methods,
genes, consistent with initiation of an immune-mediated cell death Extended Data Fig. 4 and extended data materials), including an interac-
response to dabrafenib (Fig. 3d). Interestingly, protein translation tion between interleukin 7 (IL-7) and its receptor IL-7R in T cells, which
pathway genes were upregulated in the viability-independent effects are known to have an antitumor role across diverse cancers60. Increased
of dabrafenib, a response previously noted with dabrafenib54 but with IL-7 activity may contribute to suboptimal treatment outcomes by
no mechanistic information until now. This mechanism is distinct affecting T cell behavior and elevating levels of MCP2-associated genes
from dabrafenib’s putative mechanism of action, BRAF inhibition, JUN, FOS and FOSB (Extended Data Table 3 and Extended Data Fig. 5),
which targets an orthogonal cell survival pathway. Pertpy’s ability to which are key components of the AP-1 complex that can either inhibit
efficiently manage, analyze and supplement complex experimental or promote tumor growth, depending on the context61.
design with additional datasets underscores its utility in conducting
sophisticated biology-informed analyses. This streamlined approach Discussion
greatly enhances the depth of biological insights discoverable. Pertpy facilitates the end-to-end analysis of complex perturbation
datasets with a versatile toolbox of interoperable components, encom-
Pertpy enables deciphering effects of perturbations on passing metadata annotation, data analysis and visualization tools.
cellular systems Through shared infrastructure and modules and with collaboration
Understanding the complex interplay between the immune system and with original authors, we developed improved versions of widely used
the tumor microenvironment (TME) is crucial for unraveling cancer methods that were originally unmaintained or easily available only to
progression. This is particularly important in solid tumor entities, such the R community, making them widely available to the Python com-
as TNBC, a rare, aggressive breast cancer subtype that lacks estrogen, munity as well. Our community effort will ensure that all of these meth-
progesterone and human epidermal receptors, rendering it unrespon- ods are jointly maintained and further developed. We demonstrated
sive to standard receptor-targeted therapies55. Single-cell transcrip- pertpy’s flexibility through several use cases, including the identifica-
tomics of breast cancer tumors has uncovered distinct T cell subtypes tion of perturbation-specific gene programs using a CRISPRa screen
and the involvement of plasmacytoid dendritic cells in promoting (Perturb-seq) dataset, deconvolution of viability-related response
immunosuppression within the TME in TNBC through tumor−immune signatures in a chemical perturbation dataset and deciphering treat-
crosstalk56, which is a significant driver of treatment resistance57. Stud- ment response to drugs in TNBC. Many further use cases can be found
ies have further elucidated TNBC-specific features and differential in pertpy’s extensive online tutorials.
responses to neoadjuvant chemotherapy (NACT) and immunotherapy, As perturbation datasets grow larger and incorporate additional
highlighting the role of programmed cell death protein 1 (PD-1) and modalities such as spatial transcriptomics, we anticipate the develop-
programmed cell death ligand 1 (PD-L1) pathways in modulating treat- ment of specialized methods for analyzing multimodal perturbation
ment outcomes58. Therefore, we set out to demonstrate how pertpy can data. By combining efforts such as Squidpy62 and pertpy, additional
be used to investigate treatment responses using a publicly available functionality designed for spatial perturbations to uncover, for exam-
dataset of 22 patients with TNBC treated with NACT with and without ple, differentially regulated neighborhoods, could be made widely
additional PD-L1 inhibitor paclitaxel18, initially presented by Zhang available. To scale to datasets with hundreds of millions of cells, such as
et al.18 (Methods and Fig. 4a,b). the recently published Tahoe-100M63 dataset, further optimizations in
Nature Methods | Volume 23 | February 2026 | 350–359 356
Article https://doi.org/10.1038/s41592-025-02909-7
a b
Cell type Group Treatment
Activated T cell
Anti-PD-L1+chemo
B cell
Chemo
CD4 T cell
CD8 T cell
Dendritic cell
ILC
Pre-treat.,
Macrophage partial response
Mast cell Pre-treat.,
stable disease
Monocyte Post-treat.,
Naive T cell partial response
Post-treat.,
Proliferating T cell stable disease
Both groups together Chemo Anti-PD-L1+chemo
part P ia r l e r - e tr s e p a o t. n , s s e ta P b re le -t r d e is a p e t. a a , r s P t e i o a s l t r - e tr s e p a o t. n , s s e P ta o b s l t e -t r d e is a e t. a , se part P ia r l e r - e tr s e p a o t. n , s s e ta P b re le -t r d e is a p e t. a a , r s P t e i o a s l t r - e tr s e p a o t. n , s s P e ta o b s l t e -t r d e is a e t. a , se
d
pertpy through out-of-memory implementations using Dask are neces- and generative foundation models where perturbation analysis is a key
sary, following the approach pioneered by recent Scanpy improvements. task that can be confidently evaluated with pertpy’s metrics.
Finally, we expect pertpy to support the creation of perturba- We expect pertpy to lead to more robust biological discoveries
tion atlases through harmonized data collection, the generation of through its capability of enriching measurements with biological meta-
meaningful perturbation spaces and the evaluation of these spaces data. As an extendable and interoperable framework, we anticipate that
using pertpy’s distance metrics. Such atlases can comprehensively pertpy will enable future robust perturbation analysis methods, tack-
characterize cell types under various conditions to capture the wide ling the growing complexity and multimodality of perturbation data.
array of inducible cell states beyond their basal states. Enabled by per-
turbation dataset collections such as scperturb43 (available in pertpy) Online content
and PerturBase64 (extends scperturb with more recent datasets), we Any methods, additional references, Nature Portfolio reporting sum-
expect such atlases to become essential for the development of robust maries, source data, extended data, supplementary information,
Nature Methods | Volume 23 | February 2026 | 350–359 357
MSE
distance
Pre-treat., partial response
Pre-treat., stable disease
Post-treat., partial response
Post-treat., stable disease
part P ia r l e r - e tr s e p a o t. n , s s e ta P b re le -t r d e is a p e t. a a , r s P t e i o a s l t r - e tr s e p a o t. n , s s e P ta o b s l t e -t r d e is a e t. a , se
omehC
omehc+1L-DP-itnA noitroporp
epyt
lleC
0.20 0.3 0.20 0.6
0.15 0.15
0.2
0.4
0.10 0.10
0.1 0.2
0.05 0.05
0 0 0 0
noitroporp
epyt
lleC
Pre-
treatment
Treatment
Partial Stable
response disease
CD4 T cells CD8 T cells CD8 T cells Naive T cells
cm em rm
0.25 * * 0.3 * * 0.15 * * * 0.20 * * *
0.20 *
* 0.2 00..1100 0.15
0.15
0.10
0.10
0.1 0.05
0.05 0.05
Group
0 0 0 0 Pre-treat., stable disease
Post-treat., stable disease
Pre-treat., partial response Post-treat., partial response
*Credible effect identified
by scCODA
yparehtomehC
yparehtomehc+1L-DP-itnA
Post-
treatment c
1.5
0 0.86 0.36 0.59 0 0.90 0.83 0.73 0 1.31 0.42 1.35
0.86 0 0.52 0.48 0.90 0 1.22 0.39 1.31 0 1.53 0.46 1.0
0.36 0.52 0 0.44 0.83 1.22 0 1.09 0.42 1.53 0 1.38 0.5
0.59 0.48 0.44 0 0.73 0.38 1.09 0 1.35 0.46 1.38 0 scRNA-seq samples
Pre-treat., partial response 0
Pre-treat., stable disease Post-treat., partial response Post-treat., stable disease
Fig. 4 | Pertpy identifies complex perturbation effects in multicellular tissue pre-treatment (partial response), n = 3 pre-treatment (stable disease), n = 3
as demonstrated on a TNBC treatment dataset. a, Schematic overview of post-treatment (partial response) and n = 3 post-treatment (stable disease).
the experimental design. b, scRNA-seq of tissue from 15 patients with TNBC, For the anti-PD-L1 cohort, the corresponding numbers were n = 4 pre-treatment
comparing pre-treatment and post-treatment responses to anti-PD-L1 therapy (partial response), n = 5 pre-treatment (stable disease), n = 2 post-treatment (partial
and NACT. c, MSE distance between treatment responses shows higher distances response) and n = 4 post-treatment (stable disease). Box plots indicate the median
between partial responses and stable disease. d, scCODA analysis shows and quartiles. ILC, innate lymphoid cell; T , central memory T; T , effector
cm em
significant compositional changes for patients treated with chemotherapy. memory T; T , tissue-resident memory T; treat., treatment.
rm
For the chemotherapy cohort, the number of biological replicates was n = 3
Article https://doi.org/10.1038/s41592-025-02909-7
acknowledgements, peer review information; details of author contri- 21. Stephenson, E. et al. Single-cell multi-omics analysis of the
butions and competing interests; and statements of data and code avail- immune response in COVID-19. Nat. Med. 27, 904–916 (2021).
ability are available at https://doi.org/10.1038/s41592-025-02909-7. 22. Virshup, I., Rybakov, S., Theis, F. J., Angerer, P. & Wolf, F. A.
anndata: access and store annotated data matrices. J. Open
References Source Softw. 9, 4371 (2024).
1. Dixit, A. et al. Perturb-Seq: dissecting molecular circuits with 23. Bredikhin, D., Kats, I. & Stegle, O. MUON: multimodal omics
scalable single-cell RNA profiling of pooled genetic screens. Cell analysis framework. Genome Biol. 23, 42 (2022).
167, 1853–1866 (2016). 24. Braunger, J. M. & Velten, B. Guide assignment in single-cell
2. Datlinger, P. et al. Pooled CRISPR screening with single-cell CRISPR screens using crispat. Bioinformatics 40, btae535 (2024).
transcriptome readout. Nat. Methods 14, 297–301 (2017). 25. Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep
3. Srivatsan, S. R. et al. Massively multiplex chemical generative modeling for single-cell transcriptomics. Nat. Methods
transcriptomics at single-cell resolution. Science 367, 45–51 15, 1053–1058 (2018).
(2020). 26. Lotfollahi, M., Wolf, F. A. & Theis, F. J. scGen predicts single-cell
4. Jin, X. et al. In vivo Perturb-Seq reveals neuronal and glial perturbation responses. Nat. Methods 16, 715–721 (2019).
abnormalities associated with autism risk genes. Science 370, 27. Sarntivijai, S. et al. CLO: the Cell Line Ontology. J. Biomed.
eaaz6063 (2020). Semantics 5, 37 (2014).
5. Schmidt, R. et al. CRISPR activation and interference screens 28. Hogan, W. R., Hanna, J., Joseph, E. & Brochhausen, M. Towards
decode stimulation responses in primary human T cells. Science a consistent and scientifically accurate Drug Ontology. CEUR
375, eabj4008 (2022). Workshop Proc. 1060, 68–73 (2013).
6. Wang, X., Park, J., Susztak, K., Zhang, N. R. & Li, M. Bulk tissue 29. Yang, W. et al. Genomics of Drug Sensitivity in Cancer (GDSC):
cell type deconvolution with multi-subject single-cell expression a resource for therapeutic biomarker discovery in cancer cells.
reference. Nat. Commun. 10, 380 (2019). Nucleic Acids Res. 41, D955–D961 (2013).
7. Yang, L. et al. scMAGeCK links genotypes with multiple 30. Subramanian, A. et al. A next generation Connectivity Map: L1000
phenotypes in single-cell CRISPR screens. Genome Biol. 21, 19 platform and the first 1,000,000 profiles. Cell 171, 1437–1452
(2020). (2017).
8. Barry, T., Wang, X., Morris, J. A., Roeder, K. & Katsevich, E. 31. Kim, S. et al. PubChem 2023 update. Nucleic Acids Res. 51,
SCEPTRE improves calibration and sensitivity in single-cell D1373–D1380 (2023).
CRISPR screen analysis. Genome Biol. 22, 344 (2021). 32. Gaulton, A. et al. ChEMBL: a large-scale bioactivity database for
9. Zhou, Y., Luo, K., Liang, L., Chen, M. & He, X. A new Bayesian factor drug discovery. Nucleic Acids Res. 40, D1100–D1107 (2012).
analysis method improves detection of genes and biological 33. Duan, Q. et al. L1000CDS: LINCS L1000 characteristic direction
processes affected by perturbations in single-cell CRISPR signatures search engine. npj Syst. Biol. Appl. 2, 16015 (2016).
screening. Nat. Methods 20, 1693–1703 (2023). 34. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell
10. Yao, D. et al. Scalable genetic screening for regulatory circuits gene expression data analysis. Genome Biol. 19, 15 (2018).
using compressed Perturb-seq. Nat. Biotechnol. 42, 1282–1295 35. Muzellec, B., Teleńczuk, M., Cabeli, V. & Andreux, M. PyDESeq2:
(2024). a python package for bulk RNA-seq differential expression
11. Replogle, J. M. et al. Mapping information-rich analysis. Bioinformatics 39, btad547 (2023).
genotype-phenotype landscapes with genome-scale Perturb-seq. 36. Robinson, M. D., McCarthy, D. J. & Smyth, G. K. edgeR: a
Cell 185, 2559–2575 (2022). Bioconductor package for differential expression analysis of
12. Sturm, G. et al. Scirpy: a Scanpy extension for analyzing digital gene expression data. Bioinformatics 26, 139–140 (2010).
single-cell T-cell receptor-sequencing data. Bioinformatics 36, 37. Büttner, M., Ostner, J., Müller, C. L., Theis, F. J. & Schubert, B.
4817–4818 (2020). scCODA is a Bayesian model for compositional single-cell data
13. Gayoso, A. et al. A Python library for probabilistic analysis of analysis. Nat. Commun. 12, 6876 (2021).
single-cell omics data. Nat. Biotechnol. 40, 163–166 (2022). 38. Ostner, J., Carcy, S. & Müller, C. L. tascCODA: Bayesian
14. Virshup, I. et al. The scverse project provides a computational tree-aggregated analysis of compositional amplicon and
ecosystem for single-cell omics data analysis. Nat. Biotechnol. 41, single-cell data. Front. Genet. 12, 766405 (2021).
604–606 (2023). 39. Dann, E., Henderson, N. C., Teichmann, S. A., Morgan, M. D. &
15. Frostig, R., Johnson, M. & Leary, C. Compiling machine learning Marioni, J. C. Differential abundance testing on single-cell data
programs via high-level tracing. In SysML https://research. using k-nearest neighbor graphs. Nat. Biotechnol. 40, 245–253
google/pubs/compiling-machine-learning-programs-via-high- (2022).
level-tracing/(2018). 40. Jerby-Arnon, L. & Regev, A. DIALOGUE maps multicellular
16. Norman, T. M. et al. Exploring genetic interaction manifolds programs in tissue from single-cell or spatial transcriptomics
constructed from rich single-cell phenotypes. Science 365, data. Nat. Biotechnol. 40, 1467–1477 (2022).
786–793 (2019). 41. Dong, M. et al. Causal identification of single-cell experimental
17. McFarland, J. M. et al. Multiplexed single-cell transcriptional perturbation effects with CINEMA-OT. Nat. Methods 20, 1769–1779
response profiling to define cancer vulnerabilities and (2023).
therapeutic mechanism of action. Nat. Commun. 11, 4296 42. Villani, C. in Optimal Transport: Old and New (ed. Villani, C.) 93–111
(2020). (Springer, 2009).
18. Zhang, Y. et al. Single-cell analyses reveal key immune cell 43. Peidli, S. et al. scPerturb: harmonized single-cell perturbation
subsets associated with response to PD-L1 blockade in data. Nat. Methods 21, 531–540 (2024).
triple-negative breast cancer. Cancer Cell 39, 1578–1593 (2021). 44. Badia-I-Mompel, P. et al. decoupleR: ensemble of computational
19. Papalexi, E. et al. Characterizing the molecular regulation of methods to infer biological activities from omics data. Bioinform.
inhibitory immune checkpoints with multimodal single-cell Adv. 2, vbac016 (2022).
screens. Nat. Genet. 53, 322–331 (2021). 45. Paton, V. et al. NetworkCommons: bridging data, knowledge,
20. Smillie, C. S. et al. Intra- and inter-cellular rewiring of the human and methods to build and evaluate context-specific biological
colon during ulcerative colitis. Cell 178, 714–730 (2019). networks. Bioinformatics 41, btaf048 (2025).
Nature Methods | Volume 23 | February 2026 | 350–359 358
Article https://doi.org/10.1038/s41592-025-02909-7
46. Sundararajan, M., Taly, A. & Yan, Q. Axiomatic attribution for 61. Bhosale, P. B. et al. Structural and functional properties of
deep networks. In Proc. 34th International Conference on activator protein-1 in cancer and inflammation. Evid. Based
Machine Learning (eds Precup, D. & Teh, Y. W.) 3319–3328 (PMLR, Complement. Altern. Med. 2022, 9797929 (2022).
2017). 62. Palla, G. et al. Squidpy: a scalable framework for spatial omics
47. Murray-Zmijewski, F., Lane, D. P. & Bourdon, J.-C. p53/p63/ analysis. Nat. Methods 19, 171–178 (2022).
p73 isoforms: an orchestra of isoforms to harmonise cell 63. Zhang, J. et al. Tahoe-100M: a giga-scale single-cell perturbation
differentiation and response to stress. Cell Death Differ. 13, atlas for context-dependent gene function and cellular modeling.
962–972 (2006). Preprint at bioRxiv https://doi.org/10.1101/2025.02.20.639398
48. Kundra, R. et al. OncoTree: a cancer classification system for (2025).
precision oncology. JCO Clin. Cancer Inform. 5, 221–230 (2021). 64. Wei, Z. et al. PerturBase: a comprehensive database for single-cell
49. Ghandi, M. et al. Next-generation characterization of the Cancer perturbation data analysis and visualization. Nucleic Acids Res.
Cell Line Encyclopedia. Nature 569, 503–508 (2019). 53, D1099–D1111 (2025).
50. Tsherniak, A. et al. Defining a Cancer Dependency Map. Cell 170, 65. Lachmann, A., Xie, Z. & Ma’ayan, A. blitzGSEA: efficient
564–576 (2017). computation of gene set enrichment analysis through gamma
51. Corsello, S. M. et al. Discovering the anti-cancer potential of distribution approximation. Bioinformatics 38, 2356–2357 (2022).
non-oncology drugs by systematic viability profiling. Nat. Cancer 66. Adamson, B. et al. A multiplexed single-cell crispr screening
1, 235–248 (2020). platform enables systematic dissection of the unfolded protein
52. Spain, L., Julve, M. & Larkin, J. Combination dabrafenib and response. Cell 167, 1867–1882 (2016).
trametinib in the management of advanced melanoma with 67. Kanemaru, K. et al. Spatially resolved multiomics of human
BRAFV600 mutations. Expert Opin. Pharmacother. 17, 1031–1038 cardiac niches. Nature 619, 801–810 (2023).
(2016). 68. Skinnider, M. A. et al. Cell type prioritization in single-cell data.
53. Zhu, H.-Y. et al. LncRNA CRNDE promotes the progression and Nat. Biotechnol. 39, 30–34 (2021).
angiogenesis of pancreatic cancer via miR-451a/CDKN2D axis. 69. Squair, J. W., Skinnider, M. A., Gautier, M., Foster, L. J. &
Transl. Oncol. 14, 101088 (2021). Courtine, G. Prioritization of cell types responsive to biological
54. Li, B. B. et al. Targeted profiling of RNA translation reveals mTOR- perturbations in single-cell data with Augur. Nat. Protoc. 16,
4EBP1/2-independent translation regulation of mRNAs encoding 3836–3873 (2021).
ribosomal proteins. Proc. Natl Acad. Sci. USA 115, E9325–E9332
(2018). Publisher’s note Springer Nature remains neutral with regard to
55. Toney, N. J. et al. Tumor-B-cell interactions promote isotype jurisdictional claims in published maps and institutional affiliations.
switching to an immunosuppressive IgG4 antibody response
through upregulation of IL-10 in triple negative breast cancers. Open Access This article is licensed under a Creative Commons
J. Transl. Med. 20, 112 (2022). Attribution 4.0 International License, which permits use, sharing,
56. Bayik, D. & Lathia, J. D. Cancer stem cell−immune cell crosstalk in adaptation, distribution and reproduction in any medium or format,
tumour progression. Nat. Rev. Cancer 21, 526–536 (2021). as long as you give appropriate credit to the original author(s) and the
57. Qian, J. et al. A pan-cancer blueprint of the heterogeneous tumor source, provide a link to the Creative Commons licence, and indicate
microenvironment revealed by single-cell profiling. Cell Res. 30, if changes were made. The images or other third party material in this
745–762 (2020). article are included in the article’s Creative Commons licence, unless
58. Deng, J. et al. Serial single-cell profiling analysis of metastatic indicated otherwise in a credit line to the material. If material is not
TNBC during Nab-paclitaxel and pembrolizumab treatment. included in the article’s Creative Commons licence and your intended
Breast Cancer Res. Treat. 185, 85–94 (2021). use is not permitted by statutory regulation or exceeds the permitted
59. Ji, Y. et al. Optimal distance metrics for single-cell RNA-seq use, you will need to obtain permission directly from the copyright
populations. Preprint at bioRxiv https://doi.org/10.1101/2023. holder. To view a copy of this licence, visit http://creativecommons.
12.26.572833 (2023). org/licenses/by/4.0/.
60. Lin, J. et al. The role of IL-7 in immunity and cancer. Anticancer
Res. 37, 963–967 (2017). © The Author(s) 2025
1Institute of Computational Biology, Helmholtz Center Munich, Munich, Germany. 2TUM School of Life Sciences Weihenstephan, Technical University of
Munich, Munich, Germany. 3Research Unit Precision Regenerative Medicine (PRM), Comprehensive Pneumology Center (CPC); Member of the German
Center for Lung Research (DZL), Munich, Germany. 4School of Computation, Information and Technology, Technical University of Munich, Munich,
Germany. 5Harvard Medical School, Ludwig Center at Harvard, DF/HCC Cancer Center, Broad Institute, Boston, MA, USA. 6European Molecular Biology
Laboratory, Heidelberg, Germany. 7Charité − Universitätsmedizin Berlin, Corporate Member of Freie Universität Berlin and Humboldt-Universität zu Berlin,
Institute of Pathology, Berlin, Germany. 8Institute for Biology, Humboldt-Universität zu Berlin, Berlin, Germany. 9Department of Statistics, LMU Munich,
Munich, Germany. 10Helmholtz Pioneer Campus, Munich, Germany. 11Boehringer Ingelheim International Pharma GmbH & Co. KG, Biberach, Germany.
12Wellcome Sanger Institute, Wellcome Genome Campus, Cambridge, UK. 13Interdepartmental Program in Computational Biology and Bioinformatics,
Yale University, New Haven, CT, USA. 14Konrad Zuse School of Excellence in Learning and Intelligent Systems (ELIZA), Darmstadt, Germany. 15Helmholtz AI,
Helmholtz Zentrum München, Munich, Germany. 16Wellcome MRC Cambridge Stem Cell Institute, University of Cambridge, Cambridge, UK. 17Institute of
Experimental Pneumology, LMU University Hospital, Ludwig-Maximilians University, Munich, Germany. e-mail: fabian.theis@helmholtz-muenchen.de
Nature Methods | Volume 23 | February 2026 | 350–359 359
Article https://doi.org/10.1038/s41592-025-02909-7
Methods (2) Identify and remove cells that have ‘escaped’ CRISPR perturba-
Implementation of pertpy tion by estimating the distributions of KO cells. Afterwards,
Pertpy is implemented in Python and builds upon several scientific the posterior probability that a cell belongs to the KO cells is
open-source libraries, including NumPy70, Scipy71, JAX15, scikit-learn72, calculated, and the cells are binary assigned based on a fixed
Pandas72,73, AnnData22, scanpy34, muon23, NumPyro74, OTT-JAX75, blitzG- probability threshold (defaults to 0.5).
SEA69, PyTorch76 and scvi-tools13 for omics data handling and matplot- (3) Visualize similarities and differences across different perturba-
lib77 and seaborn78 for data visualization. tions using linear discriminant analysis.
Summary table of implemented methods. Pertpy provides implemen- When calculating the perturbation-specific signatures, Mixscape
tations of many novel, but also established, methods that can be easily makes strong assumptions, such as cells with a perturbation not exhib-
accessed and combined to easily build custom analysis pipelines (Table 1). iting compositional differences with respect to variation seen within
the control cells. Additional limitations include the assumption that
gRNA assignment. Assigning relevant guides to each cell is essential in perturbation effects are additive and separable from underlying cell
genetic perturbation assays, ensuring that the observed cellular responses state, the equal weighting of all genes regardless of their relevance to
are accurately linked to the intended genetic modifications. This step is the perturbation target and the failure to account for temporal dynam-
critical for validating experimental design and interpreting results reliably. ics in cellular responses where early and late responding genes create
Pertpy provides two approaches to assigning cells to guides. composite signatures.
First, a simple thresholding model where the most expressed gRNA Generally, the Mixscape pipeline assumes KO data. Applying Mix-
is assigned to a cell if it additionally exceeds an optional user-specified scape to CRISPR interference (CRISPRi) and CRISPRa data is more
count threshold. nuanced but still valid under certain conditions. Unlike KO, these
Second, a previously published Poisson−Gaussian model11. For modalities do not introduce permanent genomic alterations, but vari-
each guide, cells with non-zero expression are log transformed and ability in perturbation efficiency can create functionally not effectively
2
modeled as a mixture of two populations, with cells automatically perturbed cells. Factors such as incomplete transcriptional repression/
classified as negative if they show zero expression. A cell is labeled activation, gRNA efficiency, chromatin state, CRISPR expression or
as positive for a guide if it belongs to the higher-expressing popula- variable effector recruitment (for example, KRAB for CRISPRi and
tion, with a maximum of five guide assignments per cell to prevent VP64 for CRISPRa) can lead to heterogeneous perturbation effects.
over-assignment; cells exceeding this threshold are marked as ‘mul- If these effects result in a clear separation between perturbed and
tiple’, whereas those failing to meet the mixture model threshold for unperturbed-like transcriptomic states, Mixscape can still be meaning-
any guide are designated as ‘negative’. fully applied. However, careful validation is needed to ensure that the
identified unperturbed population reflects true biological variability
Differential gene expression. Differential gene expression analysis rather than technical artifacts.
compares the mean gene expression levels between different condi- We implemented Mixscape following the implementation of the
tions or groups to identify genes with statistically significant changes, original authors19. We further optimized the implementation by using
utilizing statistical models to account for between-sample variability PyNNDescent (https://github.com/lmcinnes/pynndescent) for near-
and control for false discovery rates. Pertpy provides a unified appli- est neighbor search for the calculation of the perturbation signature.
cation programming interface (API) to support a variety of such mod- The implementation was verified by comparing the classifica-
els. The first group of models comprises the t-test and Wilcoxon test tion results between the original Seurat Mixscape implementation
as simple statistical tests for comparing expression values between and the pertpy implementation through a confusion matrix, showing
two groups without covariates. The second group includes models high agreement, with 4,674 KO, 13,098 NP and 2,386 non-targeted
of the linear model family that allow modeling complex designs and cells correctly classified by both implementations, with only minor
contrasts. Currently included are PyDESeq235, edgeR36 as well as a disagreements (438 cells classified as NP by pertpy but KO by original
wrapper around statsmodels (https://www.statsmodels.org), which and 133 cells classified as KO by pertpy but NP by original). Addition-
provides access to a wide range of regression models, including ordi- ally, the perturbation signature scores between implementations
nary least squares regression, robust linear models and generalized show a strong correlation of 0.97 (P < 0.0001), confirming that
linear models. Linear model designs can be specified via Wilkinson pertpy’s implementation closely reproduces the original method’s
formulas as known from R (through ‘Formulaic’, https://github.com/ quantitative measurements.
matthewwardrop/formulaic). Pseudobulk workflows that account for
pseudoreplication bias79 are enabled by integration with scanpy’s get. Compositional analysis of labeled groups with scCODA and tas-
aggregate() function. Results tables ranked by adjusted P value are pro- cCODA. Tracking cell type shifts is crucial for understanding the
vided as a Pandas data frame and can be visualized using volcano plots. underlying mechanisms of disease progression, tissue regeneration
and developmental biology, offering insights into cellular responses
Analysis of pooled CRISPR screens with mixscape. CRISPR−Cas9 can and adaptations. Despite their critical role in biological processes
sometimes lead to cells escaping gene perturbation, such as knockout, such as disease, development, aging and immunity, detecting shifts in
by receiving an ineffective in-frame mutation, underscoring the neces- cell type compositions through scRNA-seq is challenging. Statistical
sity for computational quality control to predict and enhance their analyses must navigate various technical and methodological con-
specificity and performance. Mixscape classifies targeted cells—that straints, including limited experimental replicates and compositional
is, those identified as perturbed by presence of a gRNA—into success- sum-to-one constraints37. scCODA and its extension tascCODA both
fully perturbed (KO) and targeted but not successfully perturbed (NP) employ Bayesian methods to elucidate cell type compositional changes,
based on their response. Other perturbations, such as activations or with tascCODA being able to also take cell type hierarchies into account.
inhibitions, are here collectively referred to as ‘KO’ for consistency with The implementations of scCODA 2.0 and tascCODA 2.0 are math-
the original publication. ematically equivalent to the original implementations37,38 but allow
In particular, the Mixscape pipeline includes the following steps: for accelerated inference by replacing the Hamiltonian Monte Carlo
algorithm with the no-U-turn sampler from NumPyro74. The joint imple-
(1) Calculate the perturbation-specific signature of every cell,
mentation also allows users to conveniently apply both methods from
which is the difference of the targeted and the closest k (de-
within the same framework.
faults to 20) nearest control neighbors.
Nature Methods
Article https://doi.org/10.1038/s41592-025-02909-7
Pertpy further uses MuData23 objects to simultaneously handle analyses83. Unlike traditional clustering approaches where cells are
cell-by-gene and sample-by-cell-type representations of the same forcibly separated based on expression patterns and then the same
data, simplifying the data aggregation and model specification steps data are used to identify what drives that separation (creating artifi-
for scCODA 2.0 and tascCODA 2.0 while ensuring compatibility with cially small P values), the MCP scores represent continuous axes of
other methods featured in the scverse14 ecosystem. A wide range of biological variation extracted through independent matrix factoriza-
visualization options through scanpy34, ETE 3 (ref. 80) and ArviZ81 for tion methods, whereas the extrema selection merely applies thresholds
representation of differentially abundant cell types, their hierarchical to these pre-computed scores. The subsequent differential expression
structure and inference diagnostics, respectively, are also provided testing therefore examines distinct biological phenomena rather
within pertpy. than confirming the same signal, maintaining statistical validity and
The implementation was verified by comparing parameter esti- interpretability of the identified gene signatures.
mates and log fold changes with the original implementation across Owing to these differences, the reported MCPs and MCP genes
2
multiple test scenarios, including different reference cell types and will not exactly match those identified in the DIALOGUE R package.
treatment conditions, with results showing nearly identical values Notably, users should be aware that the Seurat and scanpy imple-
between implementations (within approximately 0.01 for parameters mentations calculate principal component analysis (PCA) differently,
and approximately 0.005 for log fold changes). resulting in downstream differences in MCP scores. When the same
2
PCA representation is used, the MCP values between the R and Python
Compositional analysis of unlabeled groups with Milo. Most meth- implementation have an average Pearsonʼs correlation of 0.96 when
ods for comparing single-cell datasets often rely on identifying discrete tested on the sample dataset provided in the R tutorial.
clusters to test for differences in cell abundance across experimental
conditions. However, this approach may lack the necessary resolution Enrichment with blitzGSEA. Gene set enrichment analysis (GSEA)
and fail to represent continuous biological processes accurately. To determines whether predefined sets of genes, often associated with
address these limitations, Milo was designed to conduct differential specific biological functions or pathways, show statistically signif-
abundance tests by assigning cells to overlapping neighborhoods icant, concordant differences in expression across two biological
within a k-nearest neighbor graph. states or phenotypes. It is used to identify biological processes that
The implementation of Milo is based on Milopy (https://github. are overrepresented in a ranked list of genes, typically arising from
com/emdann/milopy). It uses the same MuData-based data struc- high-throughput experiments. This approach shifts the analysis focus
ture that the scCODA 2.0 and tascCODA 2.0 implementations also from individual genes to the collective behavior of genes within prede-
use. Here, neighborhood counts are stored in a slot in MuData for fined, functionally related groups, facilitating a deeper understanding
downstream usage. of the biological mechanisms underlying observed changes. Pertpy
The implementation was verified by comparing the results from provides access to a variety of metadata databases that provide gene
the pertpy implementation and the original miloR package, showing a sets whose enrichment can be tested for.
strong correlation (r = 0.987) between log fold change values calculated We generally followed the enrichment pipeline described in Drug-
at the cell level. Additionally, precision and recall analysis across differ- 2Cell66 to test for the enrichment of gene sets. This pipeline entails:
ent significance thresholds demonstrated high concordance between
(1) Fetching gene sets from databases
the two implementations, with both metrics approaching 1.0 as the
(2) Scoring gene sets by computing the mean expression of each
threshold increases. This confirms that pertpy’s Milo implementation
gene group per cell
accurately reproduces the statistical findings of the original method.
(3) Performing a differential expression test to get ranked gene
groups that are upregulated in particular clusters
MCPs with DIALOGUE. MCPs, or gene programs, refer to the complex
(4) Determining enriched genes using a hypergeometric test on the
regulatory networks and signal transduction pathways that govern the gene set scores or using blitzGSEA69
behavior, differentiation and communication of cells. DIALOGUE40 is a
matrix factorization method for identifying these specific gene expres- The implementation was verified by comparing the results from
sion patterns. The implementation of DIALOGUE in pertpy resembles pertpy’s enrichment module and the original Drug2Cell package,
the original implementation40. The main differences are as follows: demonstrating exact equivalence in both overrepresentation and
• The R implementation of MultiCCA has been replaced with enrichment analyses. Tests confirmed that the pertpy implementation
a Python implementation of the original mathematical produces identical results for hypergeometric overrepresentation test-
formulation82, which can be found at https://github.com/theis- ing in cell-type-specific pathways and GSEA, with all results being equal.
lab/sparsecca. In addition, the Python implementation also has
the option to solve for the canonical covariate weights w using Distances, metrics and permutation tests. Distance metrics serve as
linear programming, allowing for concurrent instead of iterative an important baseline in two primary tasks in single-cell perturbation
optimization over the pairwise factor matrices. This results in analysis: (1) identifying relative heterogeneity and response and (2)
weights that are consistent regardless of the order in which cell evaluating and training single-cell perturbation models. To this end,
types are passed, which was not previously true. various commonly used distance metrics have been implemented to
• An additional gene identification method, referred to as be easily applied to single-cell AnnData objects with accompanying
extrema MCP genes, which selects cells at the extreme val- perturbation or disease labels. In the following, we present the 16
ues of the MCP (cells with the top 10% and bottom 10% MCP distances, in order of performance according to Ji et al.59, that are
scores in each cell type) and then runs the rank_genes_groups implemented in pertpy. We use xk to denote the gene expression in cell
function from scanpy with default parameters to perform a k and xi and yi for the expression of gene i in the perturbed and control
t-test between the two groups of cells to identify differentially conditions, respectively.
expressed genes to provide adjusted P values based on the • MSE
number of tested genes. Determines the mean squared distance between the mean vec-
tors of two groups.
Although the extrema MCP genes approach utilizes gene expres-
sion data twice—once for defining MCPs and again for differential
1 2
testing—it avoids statistical circularity common in post-clustering MSE= n ∑(xi−yi)
Nature Methods
Article https://doi.org/10.1038/s41592-025-02909-7
• Maximum mean discrepancy (MMD) • Pearson’s distance
Evaluates the discrepancy between the empirical distributions Uses Pearson’s correlation to assess the linear correlation
of two groups using kernel-based methods. Let n denote the between the mean vectors of two groups, returning 1 minus the
number of samples and k(⋅,⋅) the linear kernel function. correlation coefficient. Let x and y denote the mean expression
N N N M over all genes.
MMD 2 = 1 ∑∑k(xi,xj)− 2 ∑∑k(xi,yj)
N(N−1)i=1j≠i NMi=1j=1
∑(xi−x)(yi−y)
r=1−
+ 1 ∑ M ∑ M k(yi,yj) √∑(xi−x) 2 ∑(yi−y) 2
M(M−1)i=1j≠i
• Coefficient of determination distance
• Euclidean distance Calculates the coefficient of determination (R2) between the
Calculates the Euclidean distance between the means of the two mean vectors of two groups. Note that, unlike most other
groups. distances listed here, R2 is not symmetric/has not been
Σ 2 symmetrized.
Euclideandistance=√ (xi−yi)
2
• Energy distance11,43 R2= ∑(xi−yi)
2
Computes a statistical energy distance between two groups ∑(xi−x)
based on mean pairwise distances within and between groups.
We define w here x is the mean expression over all genes in the perturbed
condition.
1 M N • Classifier control probability
δXY=
NM
∑∑||||xi−yj||||,
To compute the classifier class projection distance between per-
i=1j=1
turbations P and control condition C, we train a linear regression
N N
δX=
N(1
1
−N)
∑∑||||xi−xj|||| classifier to distinguish between C and P, with 20% of P held out
i=1j=1 for testing. To calculate the distance for perturbation class P, we
i
obtain the average post-softmax classification probabilities of
and δY accordingly, where δ denotes the mean pairwise distance all cells in P
i
and return the probability of class C.
between samples. The energy distance is then calculated as
• Kendallʼs tau distance
E(X,Y)=2δXY−δX−δY Applies Kendall’s tau, a measure of ordinal association, between
the mean vectors of two groups. We define C as the number of
• Kolmogorov−Smirnov test distance concordant pairs, D as the number of discordant pairs, X as the
Applies the Kolmogorov−Smirnov statistic to measure the maxi- number of ties in x’s ranking and Y as the number of ties in y’s
mum distance between the empirical cumulative distributions ranking.
of two groups. We define the empirical distribution function for
gene i as (C−D) n(n−1)
τ′ =(1− )
fi(z)=||{yk
i
∶yk
i
≤z,k∈{1,…,N}|| xy √(C+D+X)(C+D+Y) 4
over all cells of the control condition and, analogously, f̂(z) for • Spearman’s rank distance
i
perturbed cells. For each gene, the maximum distance between Similar to Pearson’s distance but uses Spearman’s rank correla-
both distribution functions m
z≥
a
0
x||fi(z)−f
i
̂(z)|| is computed, and the tion to measure nonlinear relationships.
results are averaged over all genes to yield a single distance value. 6 Σ d2
• Mean absolute error (MAE) ρ= i
n(n2−1)
Measures the mean absolute difference between the mean vec-
tors of two groups. w here di represents the difference in rank of gene i across both
samples.
1
MAE=
n
∑|xi−yi| • Wasserstein distance
Also known as Earth Mover’s Distance, computes the cost of
• Two-sided t-test statistic optimally transporting mass from one distribution to another.
Uses the t-test statistic to compare the means of two groups Let W(p,q) be the first-order Wasserstein distance between
under the assumption of unequal variances. Let s2 xi and s2 yi denote probability distributions p and q, Γ (p,q) the set of all joint
the variances of gene i for perturbed and control, nx and ny the distributions with marginals p and q and c(x,y) the cost of
sample sizes for perturbed and control and ϵ a small factor to transporting a unit of mass from x to y, and X and Y are the
avoid dividing by zero. support sets of p and q, respectively.
t=
1
∑
xi−yi
n s2 xi + s2 yi W(p,q)=infγ∈Γ(p,q)∫ c(x,y)dγ(x,y)
√nx+ϵ ny+ϵ X×Y
• Cosine distance • Symmetric Kullback−Leibler divergence
Computes the cosine of the angle between the mean vectors of Measures how one probability distribution diverges from a
the two groups. second. In the case of discrete inputs, the Kullback−Leibler
divergence is calculated as follows:
x⋅y
Cosinedistance=1−
|x|⋅|y|
P(x)
where - denotes the dot product.
DKL(P||Q)=
x
∑
∈Ω
P(x)log(
Q(x)
)
Nature Methods
Article https://doi.org/10.1038/s41592-025-02909-7
w here P and Q are discrete probability distributions.For non- data, Augur uses the AUC, and, for numerical data, it uses the concord-
discrete inputs, the Kullback−Leibler divergence is computed as ance correlation coefficient.
Our implementation of Augur follows the original implementa-
KL=∑ln
syi
+
s2 xi +(xi−yi) 2
−
1 tion67,68. We further optimized it by parallelizing the training of the
sxi 2∗s2
yi
2 predictive models. Moreover, the pertpy implementation allows for
gene selection using either the originally used variance based imple-
where s denotes the standard deviation. mentation or scanpy’s highly variable genes.
• Classifier class projection The implementation was verified by comparing the results from
The classifier class projection distance between perturbation Pi pertpy’s Augur implementation and the original R-based Augur pack-
and control condition Ci is calculated by training a linear age, showing excellent agreement in both default and velocity mode.
regression classifier on all x∉Pi and all C, subsequently The AUC scores from both implementations were highly consistent
retrieving the average post-softmax classification probabilities across all tested cell types, with all data points falling within 4% of the
of all cells x
i
and returning the probability of class Ci . expected y = x line. This close correspondence was observed in both
The following distance was also implemented in pertpy but was analysis modes, confirming that pertpy’s implementation faithfully
not part of the aforementioned benchmark: reproduces the computational methodology of the original R package.
• Negative binomial log likelihood Causal identification of single-cell experimental perturbation
Fits a negative binomial distribution to one group and uses it to effects with CINEMA-OT. Cellular responses to environmental sig-
compute the log likelihood of the other group’s data. For each gene i nals are crucial for understanding biological processes. Effectively
that is not overdispersed in x, we fit a negative binomial distribution extracting biological insights from such data, especially through
with parameters μi and θi . The distance between two categories x and single-cell perturbation analysis, remains challenging due to a lack of
y is then computed as the average negative log likelihood of y given methods that can directly account for underlying confounding varia-
the parameters of the distribution fit on x for each gene i—that is, tions. CINEMA-OT distinguishes between confounding variations and
N the effects of perturbations, achieving an optimal transport match
1/n∑θxi (log(θxi )−log(θxi +μxi ))+yi(log(μxi )−log(θxi +μxi )) that mirrors counterfactual cell pairings. These pairings allow for the
i=1
analysis of causal perturbation responses, enabling novel approaches,
Γ Γ Γ
+ln( (yi+θxi ))−ln( (θxi ))−ln( (yi+1)) including individual treatment effect analysis, clustering of responses,
The ‘distances’ module allows users to quickly fetch the pairwise dis- attribution analysis and the examination of synergistic effects.
tances between any set of categorically labeled cells. The ‘distance_ The implementation of CINEMA-OT is based on the original
tests’ module allows users to compute a P value through Monte Carlo implementation41. We used OTT-JAX79 to make the implementation
permutation testing, thereby providing a confidence value for any portable across hardware. It can, therefore, also be run on GPUs. Nota-
given distance. This can be particularly comforting in cases in which bly, the JAX-based implementation may initially run slower than the
distances have been used as proxies for real biological response in NumPy-based version due to the overhead of just-in-time compilation.
gene expression space. The implementation was verified by comparing the results from
Note that, although we refer to all of the above as ‘distances’, they pertpy’s CINEMA-OT implementation and the original CINEMA-OT pack-
do not all meet the mathematical definition of a distance; deviations age. Tests showed strong agreement between both implementations,
from the standard distance axioms are detailed in Ji et al.59. Although with a relative Frobenius norm difference of less than 0.1 (0.0973) for the
these distances can be used with any single-cell measurement, it optimal transport transformed confounders. Additionally, single-cell
should be noted that the ranking above was performed in the context treatment effects showed exceptionally high correlation between
of single-cell transcriptomics. implementations, with mean Pearsonʼs correlation of 0.989 and mean
We also implemented two metrics for evaluating expression pre- Spearmanʼs correlation of 0.983 across all genes. Both implementations
diction models. To evaluate if perturbation prediction leads to mean- consistently revealed the same biological insight regarding distinct treat-
ingful biological conclusions, we implemented a differential expression ment effects in monocytes, confirming that pertpy’s implementation
correlation metric. This metric uses Spearmanʼs correlation to com- faithfully reproduces the computational methods of the original tool.
pare differential gene ranking from the scanpy rank_genes_groups func-
tion performed on control versus real perturbed data and on control Perturbation spaces. Pertpy discriminates between two fundamental
versus predicted perturbed data. To evaluate if the distribution of gene domains to embed and analyze data: the ‘cell space’ and the ‘perturba-
expression means versus variances corresponds to real data, we used tion space’. In this paradigm, the cell space represents configurations
a similar method as proposed previously84. The distribution of expres- where discrete data points represent individual cells. Conversely, the
sion mean−variance two-dimensional relationship was estimated with perturbation space departs from the individualistic perspective of cells
kernel density for both real and predicted perturbed data. The distance and, instead, categorizes cells based on similar response to perturba-
between the two densities was estimated based on the difference of tion or expressed phenotype where discrete data points represent
values sampled across the whole data range. individual perturbations. This specialized space enables comprehend-
ing the collective impact of perturbations on cells. We differentiate
Perturbation ranking with Augur. Augur aims to rank or prioritize between perturbation spaces (where we create one data point for all
cell types according to their response to experimental perturba- cells of one perturbation) and cluster spaces (where we cluster all cells
tions. The fundamental idea is that, in the space of molecular meas- and then test how well the clustering overlaps with the perturbations).
urements, cells reacting heavily to induced perturbations are more
easily separated into perturbed and unperturbed than cell types with Pseudobulk space. This space takes the pseudobulk of a covariate such
little or no response. This separability is quantified by measuring how as the condition to represent the respective perturbations using the
well experimental labels (for example, treatment and control) can Python implementation of DecoupleR44 (https://github.com/saezlab/
be predicted within each cell type. Augur trains a machine learning decoupler-py), which can subsequently be embedded.
model predicting experimental labels for each cell type in multiple
cross-validation runs and then prioritizes cell type response according Centroid space. The centroid space calculates the centroids as the
to metric scores measuring the accuracy of the model. For categorical mean of the points of a condition for a pre-calculated embedding. Next,
Nature Methods
Article https://doi.org/10.1038/s41592-025-02909-7
it finds the closest actual point to that centroid, which determines the annotations, leading to incorrect annotations if the reference is not
perturbation space point for that specific condition. representative of the target data. Differences in batch effects, technical
noise or biological variability can distort nearest neighbor relation-
MLP classifier space. The MLP classifier space trains a feed-forward ships, reducing the reliability of transferred labels. Additionally, major-
neural network to predict which perturbation has been applied to a ity voting can fail in cases where distinct perturbations and cell states
given cell. By default, a neural network with one hidden layer of 512 are underrepresented, leading to misclassification of rare populations.
neurons and batch normalization is created and trained using a batch
size of 256. However, all these hyperparameters can be customized by Metadata support. Pertpy provides access to several databases that
the user to suit the specific requirements of the dataset. We account for contain additional metadata for cell lines, mechanisms of actions
class imbalances by oversampling perturbations with fewer instances. and drugs. On request, the database content gets cached locally, and
The MLP is trained using cross-entropy loss until detection of overfitting the respective information gets stored in the appropriate slots of the
(early stopping) or until it reaches the maximum number of epochs to passed AnnData object.
train, set to 40 by default. To obtain perturbation-informed embeddings
of the cells, the cell representations in the last hidden layer are extracted. Cell line. Pertpy provides access to DepMap (https://depmap.org/
Another perturbation space, such as pseudobulk, can be applied down- portal/, version 23Q4) and GDSC29. The following information can
stream to obtain a per-perturbation embedding if required. For creation be obtained:
and training of the MLP, we leverage the PyTorch library. • Cell line identification: Comprehensive details such as cell line
names, aliases, DepMap IDs and CCLE86 names
Logistic regression classifier space. The logistic regression classifier • Genetic information: Data on genetic aberrations prevalent in
space generates perturbation embeddings, as opposed to per-cell embed- cancer cell lines, including mutations, copy number alterations,
dings computed by the MLP classifier space. A logistic regression classifier fusion genes and comprehensive gene expression profiles
is trained for each perturbation individually to determine if the respective • Dependency scores: Quantitative assessments of gene essenti-
perturbation was applied to a cell or not. Depending on user preference, ality that showcases the impact of specific genes on the viability
the classifier can be trained on the high-dimensional feature space or of cancer cell lines
on a pre-computed embedding, such as one obtained through PCA. For • Drug sensitivity: Detailed measurements of how cancer
each perturbation, we extract the coefficients of the logistic regression cell lines respond to various drugs, with metrics such as
classifier, trained until convergence or reaching the maximum number half-maximal inhibitory concentration (IC ) values providing
50
of iterations (1,000 by default), to derive a per-perturbation embedding. insights into the effectiveness and potential toxicity of thera-
We use scikit-learn’s implementation for the logistic regression classifier. peutic compounds
• Lineage and type: Information categorizing cell lines based on
DBSCAN space. DBSCAN85 (density-based spatial clustering of applica- their tissue of origin and the type of cancer they represent
tions with noise) is a clustering algorithm that identifies clusters in a • Molecular subtypes: Classifications based on detailed genetic,
dataset based on the density of data points, grouping together points epigenetic and proteomic analyses, which help in understanding
that are closely packed while marking points in low-density regions the heterogeneity within and across cancer types
as outliers. Pertpy’s implementation of a DBSCAN space is based on • Phenotypic data: Observations on cell growth rates and
scikit-learn’s DBSCAN implementation. morphological characteristics, which can correlate with genetic
traits and drug responses
k-means space. k-means is a clustering algorithm that partitions a • Genomic profiling: Includes high-resolution data from
dataset into k distinct, non-overlapping clusters by minimizing the whole-exome and whole-genome sequencing efforts, offering a
distance between data points and the centroid of their assigned cluster. comprehensive view of the genetic landscape of cell lines
It iteratively adjusts the positions of centroids to reduce the total vari- • Proteomics profiling: Protein intensity values acquired using
ance within clusters, making it suitable for identifying spherical-shaped data-independent acquisition mass spectrometry (DIA-MS)
clusters in feature space. Pertpy’s implementation of a k-means space from DepMap Sanger.
uses k-means clustering as implemented in scikit-learn.
Mechanism of action. Pertpy provides access to CMAP30, also com-
Label transfer. Label transfer in single-cell analysis involves using monly referred to as CMap and LINCS Unified Environment (CLUE),
annotations of a dataset to predict the states of unannotated data which hosts the infrastructure. CMAP is a resource designed to
points, leveraging similarities in gene expression patterns or nearest help researchers discover functional connections among diseases,
neighbors. Pertpy’s label transfer function uses PyNNDescent to find genetic perturbation and drug action. The following information can
the closest neighbors for all data points and then uses majority voting be obtained:
to label unlabeled data points. • Compound names: The name of the compound of genetic
The label transfer function further quantifies uncertainty, where perturbagen
each neighbor’s contribution is weighted by its connectivity strength • Mechanism of action: The specific biochemical interactions
(derived from the distance in gene expression space). These weighted through which compounds exert their effects on cellular func-
contributions are first converted into a one-hot encoded matrix where tions. This includes detailed descriptions of whether a com-
each column represents a label category. The uncertainty score for pound acts as an inhibitor, activator or modulator of particular
each transferred label is then calculated as the Shannon entropy of the molecular targets.
weighted label distribution in the cell’s neighborhood—if all neighbors • Target: The sets of genes or proteins that directly interacted
have the same label, the entropy (and, thus, uncertainty) is 0, whereas with or were affected by the perturbagen
diverse labels among neighbors result in higher entropy values. This
uncertainty score provides a quantitative measure of prediction con- Drug. Pertpy provides access to PubChem31 using PubChemPy
fidence, where higher values indicate more heterogeneous neighbor- (https://github.com/mcs07/PubChemPy). PubChem is a compre-
hoods and, thus, less reliable label transfers. hensive resource for chemical information, primarily known for its
Any obtained labels through label transfer must be diligently vast database of chemical molecules. The following information can
verified. Label transfer can propagate biases from the reference be obtained:
Nature Methods
