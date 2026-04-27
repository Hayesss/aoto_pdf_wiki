---
source_path: /mnt/c/Users/Administrator/Zotero/storage/ESNIDQB8/Amezquita 等 - 2020 - Orchestrating single-cell analysis with Bioconductor.pdf
ingested: 2026-04-23
sha256: 6c8205263c0c5851
---

PersPective
https://doi.org/10.1038/s41592-019-0654-x
Corrected: Publisher Correction
Orchestrating single-cell analysis with Bioconductor
Robert A. Amezquita 1, Aaron T. L. Lun2,16, Etienne Becht1, Vince J. Carey3, Lindsay N. Carpp 1,
Ludwig Geistlinger4,5, Federico Marini 6,7, Kevin Rue-Albrecht 8, Davide Risso9,10,
Charlotte Soneson 11,12, Levi Waldron 4,5, Hervé Pagès1, Mike L. Smith 13, Wolfgang Huber13,
Martin Morgan14, Raphael Gottardo1* and Stephanie C. Hicks 15*
Recent technological advancements have enabled the profiling of a large number of genome-wide features in individual cells.
However, single-cell data present unique challenges that require the development of specialized methods and software infra-
structure to successfully derive biological insights. The Bioconductor project has rapidly grown to meet these demands, host-
ing community-developed open-source software distributed as R packages. Featuring state-of-the-art computational methods,
standardized data infrastructure and interactive data visualization tools, we present an overview and online book (https://osca.
bioconductor.org) of single-cell methods for prospective users.
S
ince 2001, the Bioconductor project1 has attracted a rich com- single-cell RNA-seq (scRNA-seq) data, much of the concepts men-
munity of developers and users from diverse scientific fields, tioned are also generalizable to other types of single-cell assays. We
driving the development of open-source software packages cover data import, common data containers for storing single-cell
using the R language for the analysis of high-throughput biological assay data, fast and robust methods for transforming raw single-cell
data2–6. While bulk profiling technologies have yielded important data into processed data suitable for downstream analyses, inter-
scientific insights and methods7–9, recent advancements in sequenc- active data visualization, and downstream analyses. To help users
ing technologies to profile samples at single-cell resolution have leverage this robust and scalable framework, we describe selected
emerged that can answer previously inaccessible scientific ques- packages and present an online book (https://osca.bioconductor.
tions10–20. Bioconductor has been home to a wide range of software org) covering installation, sources of help, specialized topics per-
packages used in analyzing bulk profiling data, and more recently it taining to specific aspects of scRNA-seq analysis and complete
has expanded significantly into the realm of single-cell data analy- workflows analyzing various scRNA-seq datasets. The references
sis with a rapidly growing list of community-contributed software for all packages are available at http://bioconductor.org/packages/.
packages (Fig. 1).
Current single-cell assays can be both high-throughput, measur- Data infrastructure
ing thousands to millions of cells, and high dimensional, measur- One of Bioconductor’s strongest advantages is the availability of
ing thousands of features within each individual cell. Compared to common representations and infrastructure for complex, highly
bulk assays, there are two defining characteristics of single-cell data interdependent data sets1. Bioconductor uses standardized data con-
that must be specially handled to achieve biological insight: (1) the tainers to enable modularity and interoperability of diverse pack-
increased scale of the number of observations (that is, cells) that are ages while maintaining robust end-user accessibility. To this end,
assayed in large compendiums such as those from the Human Cell Bioconductor employs a flexible object-oriented paradigm called S4
Atlas21,22 and the Mouse Cell Atlas23; and (2) the increased sparsity (ref. 31) that enables encapsulation of multiple object components
of the data due to biological fluctuations in the measured traits or into a single instance with a rich and user-friendly interface. Such
limited sensitivity for quantifying small numbers of molecules13,24–26. an approach is especially important for biological analysis, as there
These unique characteristics have motivated the development are often many links between primary data and metadata that need
of statistical methods tailored for single-cell data analysis27–30. to be preserved throughout an analysis.
Furthermore, as single-cell technologies mature, the increasing
complexity and volume of data require fundamental changes in data The SingleCellExperiment container. Bioconductor uses the
access, management and infrastructure alongside specialized meth- SingleCellExperiment class for storing single-cell assay data and
ods to facilitate scalable analyses. metadata (Fig. 2). Primary data, such as count matrices, are stored
To address these challenges, software packages developed for in the assays component as one or more matrices, where rows rep-
the analysis of single-cell data have become an integral part of the resent features (for example, genes and transcripts) and columns
Bioconductor project. Herein, we primarily focus on the analysis of represent cells. In addition, low-dimensional representations of
1Fred Hutchinson Cancer Research Center, Seattle, WA, USA. 2Cancer Research UK Cambridge Institute, University of Cambridge, Cambridge, UK.
3Channing Division of Network Medicine, Brigham And Women’s Hospital, Boston, MA, USA. 4Graduate School of Public Health and Health Policy, City
University of New York, New York, NY, USA. 5Institute for Implementation Science in Population Health, City University of New York, New York, NY,
USA. 6Center for Thrombosis and Hemostasis, Mainz, Germany. 7Institute of Medical Biostatistics, Epidemiology and Informatics, Mainz, Germany.
8Kennedy Institute of Rheumatology, University of Oxford, Oxford, UK. 9Department of Statistical Sciences, University of Padua, Padua, Italy. 10Division of
Biostatistics and Epidemiology, Department of Healthcare Policy and Research, Weill Cornell Medicine, New York, NY, USA. 11Friedrich Miescher Institute
for Biomedical Research, Basel, Switzerland. 12SIB Swiss Institute of Bioinformatics, Basel, Switzerland. 13European Molecular Biology Laboratory, Genome
Biology Unit, Heidelberg, Germany. 14Biostatistics and Bioinformatics, Roswell Park Comprehensive Cancer Center, Buffalo, NY, USA. 15Department of
Biostatistics, Johns Hopkins Bloomberg School of Public Health, Baltimore, MD, USA. 16Present address: Bioinformatics and Computational Biology,
Genentech Inc., San Francisco, CA, USA. *e-mail: rgottard@fredhutch.org; shicks19@jhu.edu
NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods 137
PersPective NaTuRe MeTHods
Number of R/Bioconductor packages for the analysis of sequencing data Feature Primary and Cell Dimension
metadata transformed data metadata reductions
Gene Entrez…
Cell
1
Cell
2
Cell
3
Cell
4… Cell_id batch…
P
C A
P
1
C A
P
2
C A
3…
300
Cell 1
Gene 1 Cell 2
200 Gene 2 Cell 3
Gene 3 Cell 4
… …
rowData colData
Assays reducedDims
100 Rows = features Rows = cells
SingleCellExperiment
Fig. 2 | Overview of the SingleCellExperiment class. The
0
2010 2012 2014 2016 2018 SingleCellExperiment class instantiates an object (SingleCellExperiment,
abbreviated as sce) capable of storing various datatypes generated
Transcriptomic-seq Microbiome from single-cell assays. An sce object is organized into components
(RNA-seq, miRNA-seq) (16S rRNA-seq, Metagenome-seq) (for example, rowData, assays, colData, reducedDims). In the assays
Single cell Genomic-seq component, the rows represent features such as genes (horizontal
(scRNA-seq, scATAC-seq) (Exome-seq, WGS)
pink bands), and the columns represent cells (vertical yellow band).
Epigenomic-seq
The rowData and colData components can hold information (such
(ChIP-seq, HiC, DNase-seq,
Methyl-seq, ATAC-seq) as metadata) about those features and cells, respectively. Note that
in the colData and reducedDims components, cells are represented
Fig. 1 | Number of Bioconductor packages for the analysis of high- as rows (horizontal yellow bands) and the number of columns in the
throughput sequencing data over ten years. Bioconductor software assays component must match the number of rows in the colData and
packages associated with the analysis of sequencing data were tracked by reducedDims components.
date of submission over the course of ten years. Software packages were
uniquely defined by their primary sequencing technology association, with
examples of specific terms used for annotation in parentheses. In all the above workflows, the end result is the import of a
count matrix into R and creation of a SingleCellExperiment object.
For specific file formats, we can use dedicated methods from the
the primary data, and metadata describing cell or feature charac- DropletUtils (for 10X data) or tximeta (for pseudo-alignment
teristics, can also be stored in the SingleCellExperiment object. methods) packages.
Through the SingleCellExperiment class, all pertinent data and
results relevant to a scRNA-seq experiment can be stored in a single Quality control. Low-quality libraries in scRNA-seq data can
instance. By standardizing the storage of single cell data and results, arise from a variety of sources such as cell damage during disso-
Bioconductor fosters interoperability between single-cell analy- ciation or failure in library preparation (for example, inefficient
sis packages and facilitates the development and usage of complex reverse transcription or PCR amplification). These usually mani-
analysis workflows. fest as ‘cells’ with low total counts, few expressed genes and high
mitochondrial read proportions. These low-quality libraries are
Data processing problematic as they can contribute to misleading results in down-
The aim of this section is to describe the precursor steps that are stream analyses.
common to most scRNA-seq analyses. These preliminary steps For droplet-based protocols, it is common to exclude data from
follow a general workflow (Fig. 3): (1) preprocessing raw sequenc- droplets that did not contain exactly one cell. The DropletUtils34
ing data to produce a per-gene (or transcript) per-cell expression package distinguishes between empty—ambient RNA-containing—
count matrix, followed by creating a SingleCellExperiment object; and cell-containing droplets, based on the frequency of each droplet
(2) applying quality control metrics and subsequent removal of barcode observed and a comparison of their respective expression
low quality cells that would otherwise interfere with downstream profile with that of the ambient solution. It can also remove artifi-
analyses; (3) converting counts into normalized expression values cial cells generated by barcode swapping in droplet-based experi-
to eliminate cell- and gene-specific biases; (4) performing feature ments38. Similarly, droplets that likely contain more than one cell
selection to pick a subset of biologically relevant genes for down- (doublets) can be identified using the scran28 or scds39 packages,
stream analyses; (5) applying dimensionality reduction methods to which compare the droplets in question against the expression
compact the data and reduce noise; and (6), if applicable, integrat- profile of simulated doublets.
ing multiples batches of scRNA-seq data. After excluding empty droplets and identifying potential dou-
blets, droplets containing potentially damaged cells or exhibiting
Preprocessing. For scRNA-seq data, preprocessing involves the align- poor read coverage are filtered out. The library size—defined as
ment of sequencing reads to a reference transcriptome and quantifica- the total sum of counts across all relevant features for each cell—
tion into a per-cell and per-gene count matrix of expression values. is an oft-used metric for filtering. Cells with small library sizes
While various preprocessing methods are available as command line are more likely to be of low quality, as the RNA has been lost at
software, Bioconductor packages such as scPipe32 and scruff33 provide some point during library preparation, either due to cell lysis or
a preprocessing workflow that is entirely written in R. For preprocess- inefficient cDNA capture and amplification. Another metric is the
ing workflows utilizing command line software, the DropletUtils34 and number of expressed features in each cell, defined as the number of
tximeta Bioconductor packages can import the results from various endogenous genes with non-zero counts for that cell. Cells with very
tools, including Cell Ranger35 (10X Genomics), Kallisto-Bustools36 few expressed genes are likely to be of poor quality as the diverse
and Alevin37. Notably, pseudo-alignment methods such as Alevin and transcript population has not been successfully captured. The pro-
Kallisto significantly reduce compute time and memory usage. portion of reads mapped to genes in the mitochondrial genome
138 NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods
NaTuRe MeTHods PersPective
Quantification into raw counts matrix
Quality control metrics
Feature selection
Integrating datasets
Dimensionality reduction
Clustering
Differential expression
Trajectory analysis
Annotation
Interactive data visualization
can also be used, as high proportions indicate the possible loss of Here, we consider methods that moderate systematic differ-
cytoplasmic RNA due to cell damage, wherein the mitochondria— ences within a single scRNA-seq experiment that bias all genes in
being larger than individual transcript molecules—are less likely to a similar manner. This includes, for example, a change in sequenc-
escape through holes in the cell membrane40. The scater41 package ing depth that scales the expected coverage of all genes by a certain
simplifies the calculation of these various metrics. factor. Library size normalization is the simplest strategy for per-
forming scaling normalization, as implemented in scater41. While
Normalization. Systematic differences in coverage between librar- this approach makes the assumption that there is no imbalance
ies are often observed in scRNA-seq data, such as differences due in the differentially expressed genes (DEGs) between any pair of
to sequencing depth25,28,42. This typically arises from differences in cells, normalization accuracy is usually not a major consideration
cDNA capture or PCR amplification efficiency across cells, attribut- for exploratory scRNA-seq analysis, as there are minimal effects on
able to the difficulty of achieving consistent library preparation with cluster separation.
minimal starting material. Normalization aims to remove these sys- Accurate normalization, however, is important for procedures
tematic differences such that they do not interfere with comparisons that involve estimation and interpretation of per-gene statistics,
of the expression profiles between cells, for example during cluster- as in DEGs. Composition biases that systematically shift log-fold
ing or differential expression analyses. changes are most often observed when multiple cell types are
maertsnwoD
gnissecorp-erP
gnissecorp
ataD
sisylana
lacitsitats
Sample processing and sequencing
Read alignment
Report generation
dna
elbisseccA
sisylana
elbicudorper
Workflow
Preprocessing of raw
sequencing data into
primary data (counts matrix)
Sample metadata
specified as colData (sce)
Reference genome
as specified as rowData (sce)
Primary data specified
as assay (sce, 'counts’)
Quality control metrics
added to colData (sce)
and rowData (sce)
Normalizing data
Normalized data
added into assays as
assay (sce, ‘logcounts’)
Dimension reductions added
into reducedDims as
reducedDims (sce, ‘PCA’) and
reducedDims (sce, ‘UMPA’)
Cell-level results such as clusters,
cell labels and trajectory-based
cell order added to colData (sce)
Gene-level results such as
differential expression and pathway
annotations added to rowData (sce)
Interactive data
visualization and
report generation
R
ot
tropmI
Description
Construction of SingleCellExperiment
gninnalP Experimental metadata
Experimental design is recorded for downstream
annotation
Fig. 3 | Bioconductor workflow for analyzing single-cell data. A typical analytical workflow using Bioconductor leads to the creation and evolution of
a SingleCellExperiment (sce) object during data processing and downstream statistical analysis (left column). An example of an sce object evolving
throughout the course of a workflow is shown, including visualization, analysis and annotation (right column).
NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods 139
PersPective NaTuRe MeTHods
present in a given scRNA-seq dataset. Normalization by deconvolu- the additional benefit of reducing noise by averaging across multiple
tion overcomes this by pooling counts from many cells to increase genes to obtain a more precise representation of patterns in the data
the size of the counts for accurate size factor estimation, followed by (for example, related to a specific pathway). Computational work in
deconvolution into cell-based factors for normalization per-cell, as downstream analyses is also reduced, as calculations only need to
implemented in scran28. be performed for a few dimensions rather than thousands of genes.
Alternatively, BASiCS43, zinbwave30 and MAST27 provide model- More aggressive dimensionality reduction schemes yield two- or
based approaches to normalization that can not only handle such three-dimensional representations that can be directly visualized to
library size or composition biases, but also can adjust for known assist in the interpretation of the results.
covariates or other intrinsic technical factors that could conceal A common first step to dimensionality reduction of scRNA-seq
biologically meaningful variation25. These methods enable more data is principal components analysis (PCA). PCA discovers axes
complex scaling strategies such as non-linear transformations of the (principal components, PCs) in high-dimensional space that capture
data. For reviews on this topic, see ref. 42. the largest amount of variation. The top PCs capture the dominant
factors of heterogeneity in the data set, and thus can be used to effi-
Imputation. Imputation methods have been proposed to address ciently perform dimensionality reduction. This takes advantage of
the challenge of data sparsity in single-cell assays44,45. As scRNA-seq the well-studied theoretical properties of the PCA—namely, that a
experiments frequently fail to measure expression for some genes, low-rank approximation formed from the top PCs is the optimal
leading to an overabundance of zero-values46, zero-inflated models approximation of the original data for a given matrix rank. Given this
have been developed. However, there are differences in the degree of property, calculations performed using the top PCs (or any similar
zero-inflation depending on the type of assay or protocol46–48, sug- low-rank approximation) takes advantage of data compression and
gesting that the optimal method is assay-dependent. Furthermore, denoising, which includes downstream analyses such as clustering.
imputation methods for scRNA-seq data have been shown to gen- No matter the approach, dimensionality reduction for visualiza-
erate false-positive results and decrease the reproducibility of cell- tion necessarily involves discarding information and distorting the
type specific markers49. distances between cells. Thus, it is ill-advised to directly analyze
the low-dimensional coordinates used for plotting. Rather, these
Feature selection. Exploratory analyses of scRNA-seq data is often plots should only be used to interpret or communicate the results
directed to characterize heterogeneity across cells. Procedures such of quantitative analyses based on a more accurate, higher-rank rep-
as clustering and dimensionality reduction, compare cells based on resentation of the data. This ensures that analyses make use of the
their gene expression profiles. However, the choice of genes to use information that was lost during compression into two dimensions.
in these calculations has a major impact on the behavior and per- For example, given a discrepancy between the visible clusters on a
formance of such downstream methods. Feature selection methods 2-dimensional plot and those identified by clustering using the top
aim to identify genes that contain useful information about the biol- PCs, one would be inclined to favor the latter.
ogy of the system while removing genes that contain random noise. The SingleCellExperiment class has a dedicated component,
By limiting analyses to such genes, interesting biological structure reducedDims, for storing lower dimensional representations of
is preserved without the variance that obscures that structure. the assay data (Fig. 2). The scater41 package provides convenience
Furthermore, focusing on such a subset of the transcriptome can wrapper functions for dimensionality reduction algorithms,
significantly reduce the size of the dataset, improving the computa- including Principal Components Analysis (PCA), t-Distributed
tional efficiency of downstream analyses. See refs. 50,51 for reviews in Stochastic Neighbor Embedding (t-SNE)53, and Uniform Manifold
feature selection methods. Approximation and Projection (UMAP)54. Diffusion map methods
The simplest approach to feature selection is to select the most are available via the destiny55 package. The zinbwave30 and glmpca48
variable genes based on their expression across the population. packages use a zero-inflated negative binomial model and a multi-
This assumes that genuine biological differences will manifest as nomial model, respectively, for model-based dimensionality reduc-
increased variation in the affected genes, compared to other genes tion approaches that can account for confounding factors.
that are only affected by technical noise or a baseline level of unin-
teresting biological variation (for example, from transcriptional Integrating datasets. Large scRNA-seq projects usually need to
bursting). However, the log-transformation does not achieve perfect generate data across multiple batches due to logistical constraints.
variance stabilization. This means that the variance of a gene is more However, the processing of different batches is often subject to
affected by its abundance than the underlying biological heterogene- uncontrollable differences, for example, changes in operator or
ity. Thus, calculation of the per-gene variance for feature selection differences in reagent quality. This results in systematic differ-
requires modelling of the mean-variance relationship. Packages such ences in the observed expression in cells from different batches.
as scran52, BASiCS43 and scFeatureFilter adopt this approach. Furthermore, as the prevalence of scRNA-seq data expands and
Alternate metrics to variance have also been proposed, such as reference datasets become available, encountering such confound-
selecting genes based on their deviance, a metric that quantifies how ing variables will become inevitable in meta-analysis contexts. Such
well each gene fits a null model of constant expression across cells48. batch effects are problematic as they can be major drivers of het-
Unlike variance-based feature selection approaches, calculating the erogeneity in the data, masking relevant biological differences and
deviance is done on raw unique molecular identifier (UMI) counts, complicating the interpretation of results.
thus making the approach less sensitive to errors brought on by nor- While generalized linear modeling frameworks can be used to
malization. The deviance can be calculated using the glmpca package. integrate disparate data sets6, these frameworks may be sub-opti-
mal in the scRNA-seq context. This is often due to the underlying
Dimensionality reduction. Dimensionality reduction aims to assumption that the composition of cell populations is either known
reduce the number of separate dimensions in the data. This is pos- or identical across batches of cells. To overcome these limitations,
sible because different genes are correlated if they are affected by bespoke methods have been developed for batch correction of sin-
the same biological process. Thus, we do not need to store separate gle-cell data56,57 that do not require a priori knowledge about the
information for individual genes, but can instead compress mul- composition of the population. This enables exploratory analyses of
tiple features into a single dimension. Dimensionality reduction scRNA-seq data where such knowledge is usually unavailable.
approaches thus create low-dimensional representations that aim Before batch correction, it is important to examine the pres-
to preserve the most meaningful structures in the dataset. This has ence of a batch effect. This can be examined by performing PCA
140 NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods
NaTuRe MeTHods PersPective
on the log-expression values of select genes, followed by graph- each node is a cell that is connected to its nearest neighbours (NN)
based clustering to obtain a summary of the population structure. in the high-dimensional space. Edges are weighted based on the
Ideally, clusters should consist of cells from replicate scRNA-seq similarity between the cells involved, with higher weight given to
datasets. However, if instead clusters are comprised of cells from a cells that are more closely related. Algorithms such as louvain and
single batch, this indicates that cells of the same type are artificially leiden59 can then be used to identify clusters of cells.
separated due to technical differences. Approaches such as t-SNE BiocNeighbors provides an engine for both exact and approxi-
and UMAP will also typically show a strong separation between mate nearest-neighbor detection, with scran building the actual
cells from different batches that are consistent with such cluster- graph. Notably, for large scRNA-seq datasets, approximate NN
ing results. Notably, such a diagnostic that relies on the degree of methods trade an acceptable loss in accuracy for vastly improved
intermingling may not be effective when the batches involved may run times, with the added advantage of smoothing over noise and
indeed contain unique subpopulations, but is nonetheless a useful sparsity. Alternative approaches include the SIMLR package60, which
first approximation. uses multiple kernels to learn a distance metric between cells that
Supervised integration via the labeling of cells a priori (see the best fits the data, and can then be used for clustering and dimen-
section ‘Annotation’) can be used via packages, such as scMerge57 sion reduction. For large data, the mbkmeans package implements
and scmap58, to guide the application of any batch correction on the a scalable version of the k-means algorithm. Finally, the SC361 and
gene-expression values or to adjust lower dimensional representa- clusterExperiment62 packages calculate consensus clusters derived
tions. On the other hand, unsupervised approaches, such as mutual from multiple parameterizations.
nearest neighbours (MNN), identify pairs of cells from different Many of these packages allow quantitative and visual evalua-
batches that belong in each other’s set of nearest neighbours. Thus, tion of the clustering results, alongside external packages designed
the difference between cells in MNN pairs can be used as an estimate solely for data visualization and evaluation (for example, clustree).
of the batch effect, the subtraction of which yields batch-corrected Clusters can also be evaluated independently by assessing metrics
values56. Vitally, by altering the number of k-nearest neighbors that such as cluster modularity or the silhouette coefficient.
are considered, the aggressiveness of the batch correction can be
tuned, wherein a higher k-value results in more generous match- Differential expression. Differential gene expression (DGE) analy-
ing of subpopulations across batches. This MNN-based approach is sis can be used to identify marker genes that drive the separation
implemented in the batchelor package. between clusters. These marker genes allow us to assign biologi-
The success of the batch correction is contingent on the preser- cal meaning to each cluster based on their functional annotation.
vation of biological heterogeneity, as one could envision a correc- In the most obvious case, the marker genes for each cluster are
tion method of simply aggregating all cells together, which would a priori associated with particular cell types, allowing for cluster-
achieve perfect mixing but also discard the biology of interest. To ing to serve as a proxy for cell-type identity. The same principle
this end, the CellMixS package can be used to evaluate the degree can be applied to detect more subtle differences, such as activation
of cell mixing across batches. Another useful heuristic is to com- status or differentiation state. An alternative to DGE analysis for
pare clusters identified in the merged data against those identified cell-type annotation is gene-set enrichment analysis, which groups
per batch. Ideally, we should see a many-to-one mapping, where the genes into pre-specified gene modules or biological pathways
across-batch clustering is nested inside the within-batch clustering, to facilitate biological interpretation. We discuss this topic in the
indicating that any within-batch structure was preserved post-cor- section ‘Annotation’.
rection. A summary statistic such as the Rand index can then be DGE can also be used to compare individual cells within a given
calculated, where larger Rand indices are more desirable. population across conditions, such as time or treatment, while
adjusting for covariates (for example, patient identification or
Downstream statistical analysis batch effects).
The choice of methods and workflows can differ greatly depend- Across differential expression methods, two general approaches
ing on the specific goals of the investigation and the experimental stand out. The first approach retrofits well-supported and long-
protocol used. Following data processing, Bioconductor can be used standing DE analysis frameworks initially designed for bulk RNA-
to generate new biological insights from single-cell data, using tools sequencing (edgeR (ref. 2), DESeq2 (ref. 5) and limma-voom (ref. 6))
that are interoperable with the SingleCellExperiment class and that that have made the transition to scRNA-seq through various
scale with cell number. Our online book (https://osca.bioconductor. approaches, such as by creating pseudo-bulk RNA-seq profiles.
org) provides prospective users with workflows and case studies for Alternatively, approaches such as zinbwave30 can be used to down-
downstream analyses and visualizations (Fig. 4). weight excess zeros observed in scRNA-seq data during the disper-
sion estimation and model fitting steps prior to assessing differential
Clustering. Clustering is used in scRNA-seq data analysis to empir- expression (DE), and consequently further enabling the adaptation
ically define groups of cells with similar expression profiles. This of bulk RNA-seq-based DE methods for use with scRNA-seq data63.
allows us to describe population heterogeneity in terms of discrete The second class of approaches is uniquely tailored for single-
labels that can be more easily understood, rather than attempting cell data because the statistical methods proposed directly model
to comprehend the high-dimensional manifold on which the cells the zero-inflation component, frequently observed in scRNA-seq
truly reside. After annotation based on differentially expressed data. These methods explicitly separate gene expression into two
marker genes, the clusters can be treated as proxies for more abstract components: the discrete component, which describes the fre-
biological concepts, such as cell types or states. quency of a discrete component (zero versus non-zero expression);
It is worth highlighting the distinction between clusters and cell and the continuous component, where the level of gene expres-
types. The former is an empirical construct while the latter is a bio- sion is quantified. While all the methods mentioned herein can
logical truth (albeit a vaguely defined one). Thus, it is helpful to test for differences in the continuous component, only this second
realize that clustering, like a microscope, is simply a tool to explore class of approaches can explicitly model the discrete component,
the data. One can zoom in and out by changing the resolution of and thus test for differences in the frequency of expression. To
the clustering parameters, and experiment with different clustering do this, the MAST27 package utilizes a hurdle model framework,
algorithms to obtain alternative perspectives of the data. whereas the scDD64, BASiCS43 and SCDE14 use Bayesian mixture
Graph-based clustering is a flexible and scalable technique for and hierarchical models, respectively. Together, these methods
clustering large scRNA-seq datasets. A graph is constructed where are able to provide a broader suite of testing functionality and
NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods 141
PersPective NaTuRe MeTHods
Dimensionality reduction Clustering Trajectory analysis
Integrating datasets Differential expression Annotation
4 4
3 3 2 2
1 1 0 0
4 4
3 3
2 2
1 1 0 0
300
200
100
−2
can be directly utilized on scRNA-seq data contained within the Bioconductor facilitates such testing by providing standardized data
SingleCellExperiment class. representation, such as the SingleCellExperiment class objects. See
For more details regarding DE analysis and the benchmarking of ref. 74 for further discussion.
the various packages mentioned above, see refs. 65–67.
Annotation
Trajectory analysis. Heterogeneity may also be modeled as a con- The most challenging task in scRNA-seq data analysis is arguably
tinuous spectrum arising from biological processes, such as cell the interpretation of the results. Obtaining clusters of cells is fairly
differentiation. A specialized application of dimension-reduction straightforward, but it is more difficult to determine what biologi-
specific to single-cell analysis—trajectory analysis or pseudotime cal state is represented by each of those clusters. Doing so requires
inference—uses phylogenetic methods to order cells along an bridging the gap between the current dataset and prior biological
(often time-continuous) trajectory, such as development over time. knowledge, and the latter is not always available in a consistent and
Inferred trajectories can identify transition between cell states, a quantitative manner. As such, interpretation of scRNA-seq data is
differentiation process, or events responsible for bifurcations in a often manual and is a common bottleneck in the analysis workflow.
dynamic cellular process68. To expedite this step, various computational approaches can
Modern approaches for trajectory inference have minimized be applied that exploit prior information to assign meaning to an
the need for extensive parameterization and can test for differential uncharacterized scRNA-seq dataset. The most obvious sources of
gene expression across various topologies (for example, Monocle69, prior information are curated gene sets associated with particular
LineagePulse and switchde70). Moreover, several Bioconductor biological processes (for example, from the Gene Ontology (GO) or
packages for trajectory inference (for example, slingshot71, the Kyoto Encyclopedia of Genes and Genomes (KEGG) collections).
TSCAN29, Monocle69, cellTree72 and MFA73) were recently demon- An alternative approach involves directly comparing expres-
strated to have excellent performance74. As different methods can sion profiles to published reference datasets where each sample or
produce drastically different results for the same dataset, a suite of cell has already been annotated with its putative biological state by
methods and parameterizations must be tested to assess robustness. domain experts.
]RDF[01gol–
Gene ranks
Clusters
10
8
6 4 2
0
−1 0 1 2
log[FC.2] 0 1,000 2,000
erocs
tnemhcirnE
9
3
7
5 6
2 8
1
4
Pre-integration
0.0
−0.2
−0.4
−0.6
−0.8
0 1,000 2,000
Rank
UMAP 1
1 2
3
4 5 6 7 8
9
PAMU 2
Donor
BM1
BM2
BM3 BM4
BM5 BM6 BM7
BM8
Post-integration
PAMU 2
Donor
BM1
BM2 BM3
BM4
BM5 BM6 BM7 BM8
UMAP
1
PAMU 2
LYZ
UMAP
1
PAMU 2
CD3E
UMAP
1
PAMU 2
CD79A
UMAP
1
PAMU 2
NKG7
UMAP
1
PAMU 2
UMAP UMAP
1 1
PAMU 2 PAMU 2
UMAP
1
Fig. 4 | Select visualizations derived from various Bioconductor workflows. Various visualizations associated with pre-processing (blue boxes) and
downstream statistical analyses (pink boxes). The example data set used throughout was generated as part of the Human Cell Atlas21. Details on the
generation of these figures are described in our online companion book (https://osca.bioconductor.org).
142 NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods
NaTuRe MeTHods PersPective
Gene-set enrichment. Classical gene-set enrichment (GSE) of high-quality scRNA-seq data from various contexts. In addition,
approaches have the advantage of not requiring reference expres- simulated data are useful for benchmarking methods.
sion values. This is particularly useful when dealing with gene sets Alternately, the splatter package84 can simulate scRNA-seq data
derived from the literature or other qualitative forms of biological that contains multiple cell types, batch effects, varying levels of drop-
knowledge. In the context of cell annotation, GSE is typically per- out events, differential gene expression and trajectories. The splatter
formed on a group of cells (or cluster) to identify the gene set (or package uses both its own simulation framework and wraps around
pathway) that is enriched in these cells. The enriched pathway can other simulation frameworks with differing generative models to
then be used to deduce a cell type (or state). provide a comprehensive resource for single-cell data simulation.
Bioconductor provides dedicated packages to programmati- To promote the reproducibility of benchmark comparisons
cally access predefined gene signatures from databases such as assessing the performance of single-cell methods, software pack-
MSigDB75, KEGG76, Reactome77 and Gene Ontology (GO)78. ages have been developed that provide infrastructure to compute
EnrichmentBrowser79 simplifies the compilation of gene-set col- and store the results of applying different methods to a data set. The
lections from such repositories. This prior knowledge is used to SummarizedBenchmark85 and CellBench86 packages provide inter-
test for the enrichment of specific gene modules in scRNA-seq faces for which to store metadata (method parameters and package
data, often adapting existing gene-set analysis methods originally versions) and evaluation metrics.
developed for bulk data. The EnrichmentBrowser79, EGSEA80 and
fgsea packages each provide some version of classical GSE analy- Interactive data visualization. The maturation of web technolo-
sis. Alternative approaches to testing for GSE are implemented in gies has opened new avenues for interactive data exploration, aided
MAST27, AUCell81 and slalom82. by shiny, an R package facilitating development of rich graphical
user interfaces. The iSEE87 and singleCellTK packages provide
Automated classification of cells. A conceptually straightforward full-featured applications for interactive visualization of scRNA-
annotation approach is to compare the single-cell expression pro- seq datasets through an internet browser, eliminating the need for
files with previously annotated reference datasets. Labels can then programming experience if the instance is hosted on the web. Both
be assigned to each cell in an uncharacterized dataset based on the packages directly interface with the SingleCellExperiment data con-
most similar reference sample(s) or on some other similarity met- tainer to enable scRNA-seq analysis results.
ric. This is a common classification challenge that can be tackled
by standard machine-learning techniques, such as random forests Outlook
and support vector machines. Any published and labelled RNA-seq Since the early days of genomics, the Bioconductor project has
dataset (bulk or single-cell) can be used as a reference, though its embraced the development of open-source and open-develop-
reliability depends greatly on the domain expertise of the original ment software through the R statistical programming language.
authors who assigned the labels in the first place. Bioconductor has established best practices for coordinated pack-
The SingleR method83 provides one such automated system for age versioning and code review. Alongside community-contributed
cell type annotation assignment. SingleR labels cells based on the packages, a core developer team (https://www.bioconductor.org/
reference samples with the highest Spearman rank correlations, about/core-team) implements and maintains the essential infra-
and thus can be considered a rank-based variant of k-nearest- structure, and reviews contributed packages to ensure they satisfy
neighbor classification. To reduce noise, SingleR identifies marker a set of guidelines to guarantee interoperability across packages.
genes between pairs of labels and computes the correlation using These packages are organized into BiocViews, an ontology of top-
only those markers. A number of built-in reference datasets are ics that classify packages by task or technology. For example, top-
included with the package that are derived from a variety of sources ics in single-cell analysis are labeled under the view SingleCell.
and tissues, including Immunological Genome project (ImmGen), Most importantly, the broader Bioconductor community—acces-
ENCODE and the Database for Immune Cell Expression (DICE). sible through various means, including forums, Slack or mailing
lists—is a model of altruism in code sharing and technical help.
Accessible analysis Together, these practices produce high-quality, well maintained
With the increased interest in data from single-cell assays, packages, contributing to a unified and stable environment for
Bioconductor has developed not only the methods and software biological research.
to analyze the data, but also has prioritized making the data itself Most recently, the Bioconductor community has developed
and the data analysis tools more easily accessible to both users state-of-the-art computational methods, infrastructure and interac-
and developers. Specifically, the community has contributed data tive data visualization tools available as software packages for the
packages, containing both publicly available published data and analysis of data derived from single-cell experiments. Emerging
simulated data, and interactive data visualization tools. Making sin- single-cell technologies in epigenomics, T cell and B cell rep-
gle-cell data and data analysis tools more accessible allows research- ertoires, spatial profiling, and sequencing-based protein profil-
ers to leverage these resources in their own work and democratizes ing88–95, promise to continue driving advances in computational
data analysis. biology. In particular, technologies enabling multimodal profiling
are rapidly developing, and Bioconductor has laid the groundwork
Benchmarking. As new single-cell assays, statistical methods and necessary to support statistical methodologies that fully leverage
corresponding software are developed, it is increasingly impor- such approaches.
tant to facilitate the publication of data sets, to reproduce existing In addition, Bioconductor’s standardized data containers enable
analyses as well as to enable comparisons across new and existing interoperability within and between Bioconductor packages as well
tools. Bioconductor houses a collection of data packages focused on as other software. Analysis stored in a SingleCellExperiment can be
providing accessible and well-annotated versions of data ready for converted to formats usable with Seurat96, Monocle69 and Python’s
analysis, alongside vignettes that can be used to reproduce manu- scanpy97, enabling the use of tools that best serve the objective at
script figures and showcase data characteristics. hand. Indeed, R has a long history of interoperability with other
To facilitate querying of published data packages on programming languages. Four examples are the Rcpp98 package for
Bioconductor, the ExperimentHub package enables programmatic integrating C++ compiled code into R, the rJava package to call Java
access of published data sets using a standardized interface. Of note, code from within R, the.Fortran() function in base R to call Fortran
the scRNAseq package provides direct access to a curated selection code, and the reticulate CRAN package for interfacing with Python.
NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods 143
PersPective NaTuRe MeTHods
This interoperability enables common machine learning frame- 25. Hicks, S. C., Townes, F. W., Teng, M. & Irizarry, R. A. Missing data and
works, such as TensorFlow/Keras, to be used directly in R. technical variability in single-cell RNA-sequencing experiments. Biostatistics
19, 562–578 (2018).
To the newcomer, the wealth of single-cell analyses possible
26. Kharchenko, P. V., Silberstein, L. & Scadden, D. T. Bayesian approach to
in Bioconductor can be daunting. To address the rapid growth of single-cell differential expression analysis. Nat. Methods 11, 740–742 (2014).
contributed packages within the single-cell analysis space, we have 27. Finak, G. et al. MAST: a flexible statistical framework for assessing
summarized and highlighted state-of-the-art data infrastructure transcriptional changes and characterizing heterogeneity in single-cell RNA
(Fig. 2), methods and software, and organized the packages along a sequencing data. Genome Biol. 16, 278 (2015).
28. Lun, A. T. L., Bach, K. & Marioni, J. C. Pooling across cells to normalize
typical workflow (Fig. 3) for the most common single-cell analyses
single-cell RNA sequencing data with many zero counts. Genome Biol. 17,
(Fig. 4). Finally, we have developed an online companion book that
75 (2016).
provides more details on focused topics as well as complete cod- 29. Ji, Z. & Ji, H. TSCAN: Pseudo-time reconstruction and evaluation in
ing workflows (https://osca.bioconductor.org). This effort will be single-cell RNA-seq analysis. Nucleic Acids Res. 44, e117 (2016).
continuously updated and maintained with new packages as they 30. Risso, D., Perraudeau, F., Gribkova, S., Dudoit, S. & Vert, J.-P. A general
and flexible method for signal extraction from single-cell RNA-seq data.
emerge, which increases discoverability of Bioconductor resources.
Nat. Commun. 9, 284 (2018).
31. Chambers, J. M. Object-oriented programming, functional programming and
Received: 26 March 2019; Accepted: 14 October 2019; R. Stat. Sci. 29, 167–180 (2014).
Published online: 2 December 2019 32. Tian, L. et al. scPipe: a flexible R/Bioconductor preprocessing pipeline for
single-cell RNA-sequencing data. PLoS Comput. Biol. 14, e1006361 (2018).
References 33. Wang, Z., Hu, J., Johnson, W. E. & Campbell, J. D. scruff: an R/Bioconductor
package for preprocessing single-cell RNA-sequencing data. BMC Bioinform.
1. Huber, W. et al. Orchestrating high-throughput genomic analysis with
20, 222 (2019).
Bioconductor. Nat. Methods 12, 115–121 (2015).
34. Lun, AaronT. L. et al. Emptydrops: distinguishing cells from empty droplets
2. Robinson, M. D. et al. edgeR: A Bioconductor package for differential
expression analysis of digital gene expression data. Bioinformatics 26, in droplet-based single-cell RNA sequencing data. Genome Biol. 20,
139–140 (2010). 63 (2019).
3. Lawrence, M. et al. Software for computing and annotating genomic ranges. 35. Zheng, G. X. Y. et al. Massively parallel digital transcriptional profiling of
PLoS Comput. Biol. 9, e1003118 (2013). single cells. Nat. Commun. 8, 14049 (2017).
4. Aryee, M. J. et al. Minfi: a flexible and comprehensive Bioconductor package 36. Melsted, P. et al. Modular and efficient pre-processing of single-cell rna-seq.
for the analysis of Infinium DNA methylation microarrays. Bioinformatics 30, Preprint at bioRxiv https://doi.org/10.1101/673285 (2019).
1363–1369 (2014). 37. Srivastava, A., Malik, L., Smith, T., Sudbery, I. & Patro, R. Alevin efficiently
5. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold estimates accurate gene abundances from dscRNA-seq data. Genome Biol. 20,
change and dispersion for RNA-seq data with DESeq2. Genome Biol. 15, 65 (2019).
550 (2014). 38. Griffiths, J. A., Richard, A. C., Bach, K., Lun, A. T. L. & Marioni, J. C.
6. Ritchie, M. E. et al. limma powers differential expression analyses for Detection and removal of barcode swapping in single-cell RNA-seq data.
RNA-sequencing and microarray studies. Nucleic Acids Res. 43, e47 (2015). Nat. Commun. 9, 2667 (2018).
7. Serratì, S. et al. Next-generation sequencing: advances and applications in 39. Bais, A. S. & Kostka, D. scds: computational annotation of doublets in single
cancer diagnosis. Onco. Targets Ther. 9, 7355–7365 (2016). cell RNA sequencing data. Bioinformatics https://doi.org/10.1093/
8. Nakato, R. & Shirahige, K. Recent advances in ChIP-seq analysis: from bioinformatics/btz698 (2019).
quality management to whole-genome annotation. Brief. Bioinform. 18, 40. Ilicic, T. et al. Classification of low quality cells from single-cell RNA-seq
279–290 (2017). data. Genome Biol. 17, 29 (2016).
9. Kukurba, K. R. & Montgomery, S. B. RNA sequencing and analysis. 41. McCarthy, D. J., Campbell, K. R., Lun, A. T. L. & Wills, Q. F. Scater:
Cold Spring Harb. Protoc. 2015, 951–969 (2015). pre-processing, quality control, normalization and visualization of single-cell
10. Kolodziejczyk, A. A., Kim, J. K., Svensson, V., Marioni, J. C. & Teichmann, S. RNA-seq data in R. Bioinformatics 33, 1179–1186 (2017).
A. The technology and biology of single-cell RNA sequencing. Mol. Cell 58, 42. Vallejos, C. A., Risso, D. R., Scialdone, A., Dudoit, S. & Marioni, J. C.
610–620 (2015). Normalizing single-cell RNA sequencing data: challenges and opportunities.
11. Patel, A. P. et al. Single-cell RNA-seq highlights intratumoral heterogeneity in Nat. Methods 14, 565–571 (2017).
primary glioblastoma. Science 344, 1396–401 (2014). 43. Vallejos, C. A., Richardson, S. & Marioni, J. C. Beyond comparisons of
12. Tirosh., I. et al. Dissecting the multicellular ecosystem of metastatic means: understanding changes in gene expression at the single-cell level.
melanoma by single-cell RNA-seq. Science 352, 189–196 (2016). Genome Biol. 17, 70 (2016).
13. Karaayvaz, M. et al. Unravelling subclonal heterogeneity and aggressive 44. Huang, M. et al. SAVER: gene expression recovery for single-cell RNA
disease states in TNBC through single-cell RNA-seq. Nat. Commun. 9, sequencing. Nat. Methods 15, 539–542 (2018).
3588 (2018). 45. Li, W. V. & Li, J. L. An accurate and robust imputation method scImpute for
14. Jean Fan. et al. Linking transcriptional and genetic tumor heterogeneity singlecell RNA-seq data. Nat. Commun. 9, 997 (2018).
through allele analysis of single-cell RNA-seq data. Genome Res. 28, 46. Svensson, V. Droplet scRNA-seq is not zero-inflated. Preprint bioRxiv https://
1217–1227 (2018). doi.org/10.1101/582064 (2019).
15. Levitin, H. M., Yuan, J. & Sims, P. A. Single-cell transcriptomic analysis of 47. Vieth, B., Ziegenhain, C., Parekh, S., Enard, W. & Hellmann, I. powsimR:
tumor heterogeneity. Trends Cancer 4, 264–268 (2018). power analysis for bulk and single cell RNA-seq experiments. Bioinformatics
16. Paulson, K. G. et al. Acquired cancer resistance to combination 33, 3486–3488 (2017).
immunotherapy from transcriptional loss of class I HLA. Nat. Commun. 9, 48. Townes, F. W., Hicks, S. C., Aryee, M. J. & Irizarry, R. A. Feature selection
3868 (2018). and dimension reduction for single cell RNA-seq based on a multinomial
17. Zeisel, A. et al. Brain structure: cell types in the mouse cortex and model. Preprint at bioRxiv https://doi.org/10.1101/574574 (2019).
hippocampus revealed by single-cell RNA-seq. Science 347, 1138–1142 (2015). 49. Andrews, T. & Hemberg, M. False signals induced by single-cell imputation.
18. Deng, Q., Ramsköld, D., Reinius, B. & Sandberg, R. Single-cell RNA-seq F1000Res. https://doi.org/10.12688/f1000research.16613.2 (2019).
reveals dynamic, random monoallelic gene expression in mammalian cells. 50. Andrews, T. & Hemberg, M. M3Drop: Dropout-based feature selection for
Science 343, 193–196 (2014). scRNASeq. Bioinformatics 35, 2865–2867 (2019).
19. Kiselev, V. Y., Andrews, T. S. & Hemberg, M. Challenges in unsupervised 51. Yip, S. H., Sham, P. C. & Wang, J. Evaluation of tools for highly variable
clustering of single-cell RNA-seq data. Nat. Rev. Genet. 20, 273–282 (2019). gene discovery from single-cell RNA-seq data. Brief. Bioinform. 20,
20. Cannoodt, R., Saelens, W. & Saeys, Y. Computational methods for trajectory 1583–1589 (2018).
inference from single-cell transcriptomics. Eur. J. Immunol. 46, 2496–2506 52. Lun, A. T. L., McCarthy, D. J. & Marioni, J. C. A step-by-step workflow for
(2016). low-level analysis of single-cell RNA-seq data with Bioconductor. F1000Res. 5,
21. Regev, A. et al. The Human cell atlas. eLife 6, e27041 (2017). 2122 (2016).
22. Rozenblatt-Rosen, O., Stubbington, M. J. T., Regev, A. & Teichmann, S. A. 53. van der Maaten, L. & Hinton, G. Visualizing data using t-SNE. J. Mach.
The human cell atlas: from vision to reality. Nature 550, 451–453 (2017). Learn. Res. 9, 2579–2605 (2008).
23. Han, X. et al. Mapping the mouse cell atlas by microwell-seq. Cell 173, 54. Melville, J., McInnes, L. & Healy, J. UMAP: uniform manifold approximation
1307 (2018). and projection for dimension reduction. Preprint at arXiv https://arxiv.org/
24. McDavid, A. et al. Data exploration, quality control and testing in abs/1802.03426 (2018).
single-cell qPCR-based gene expression experiments. Bioinformatics 29, 55. Angerer., P. et al. Destiny: diffusion maps for large-scale single-cell data in R.
461–467 (2013). Bioinformatics 32, 1241–1243 (2016).
144 NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods
NaTuRe MeTHods PersPective
56. Haghverdi, L., Lun, A. T. L., Morgan, M. D. & Marioni, J. C. Batch effects in 87. Rue-Albrecht, K., Marini, F., Soneson, C. & Lun, A. T. L. iSEE: interactive
single-cell RNA-sequencing data are corrected by matching mutual nearest SummarizedExperiment Explorer. F1000Res. 7, 741 (2018).
neighbors. Nat. Biotechnol. 36, 421–427 (2018). 88. Peterson, V. M. et al. Multiplexed quantification of proteins and transcripts in
57. Lin, Y. et al. scMerge leverages factor analysis, stable expression, and single cells. Nat. Biotechnol. 35, 936–939 (2017).
pseudoreplication to merge multiple single-cell RNA-seq datasets. Proc. Natl. 89. Dey, S. S., Kester, L., Spanjaard, B., Bienko, M. & van Oudenaarden, A.
Acad. Sci. USA 116, 9775–9784 (2019). Integrated genome and transcriptome sequencing of the same cell.
58. Kiselev, V. Y., Yiu, A. & Hemberg, M. scmap: projection of single-cell Nat. Biotechnol. 33, 285–289 (2015).
RNA-seq data across data sets. Nat. Methods 15, 359–362 (2018). 90. Macaulay, IainC. et al. Separation and parallel sequencing of the
59. Traag, V. A., Waltman, L. & van Eck, N. J. From Louvain to Leiden: genomes and transcriptomes of single cells using GT-seq. Nat. Protoc. 11,
guaranteeing well-connected communities. Sci. Rep. 9, 5233 (2019). 2081–2103 (2016).
60. Wang, B., Zhu, J., Pierson, E., Ramazzotti, D. & Batzoglou, S. Visualization 91. Stoeckius, M. et al. Simultaneous epitope and transcriptome measurement in
and analysis of single-cell RNA-seq data by kernel-based similarity learning. single cells. Nat. Methods 14, 865–868 (2017).
Nat. Methods 14, 414–416 (2017). 92. Shahi, P., Kim, S. C., Haliburton, J. R., Gartner, Z. J. & Abate, A. R. Abseq:
61. Kiselev, V. Y. et al. SC3: consensus clustering of single-cell RNA-seq data. ultrahighthroughput single cell protein profiling with droplet microfluidic
Nat. Methods 14, 483–486 (2017). barcoding. Sci. Rep. 7, 44447 (2017).
62. Risso, D. et al. clusterExperiment and RSEC: a bioconductor package and 93. Angermueller, C. et al. Parallel single-cell sequencing links transcriptional
framework for clustering of singlecell and other large gene expression and epigenetic heterogeneity. Nat. Methods 13, 229–232 (2016).
datasets. PLoS Comp. Biol. 14, e1006378–16 (2018). 94. Cao, J. et al. Joint profiling of chromatin accessibility and gene expression in
63. Van den Berge, K. et al. Observation weights unlock bulk RNA-seq tools for thousands of single cells. Science 361, 1380–1385 (2018).
zero inflation and single-cell applications. Genome Biol. 19, 24 (2018). 95. Clark, S. J. et al. scNMT-seq enables joint profiling of chromatin accessibility
64. Korthauer, K. D. et al. A statistical approach for identifying differential DNA methylation and transcription in single cells. Nat. Commun. 9,
distributions in single-cell RNA-seq experiments. Genome Biol. 17, 781 (2018).
222 (2016). 96. Butler, A., Hoffman, P., Smibert, P., Papalexi, E. & Satija, R. Integrating
65. Soneson, C. & Robinson, M. D. Bias, robustness and scalability in single-cell single-cell transcriptomic data across different conditions, technologies, and
differential expression analysis. Nat. Methods 15, 255–261 (2018). species. Nat. Biotechnol. 36, 411–420 (2018).
66. Wang, T., Li, B., Nelson, C. E. & Nabavi, S. Comparative analysis of 97. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell gene
differential gene expression analysis tools for single-cell RNA sequencing expression data analysis. Genome Biol. 19, 15 (2018).
data. BMC Bioinform. 20, 40 (2019). 98. Eddelbuettel, D. & François, R. Rcpp: seamless R and C++ integration.
67. Crowell, H. L. et al. On the discovery of population-specific state transitions J. Stat. Softw. 40, 1–18 (2011).
from multi-sample multi-condition single-cell RNA sequencing data. Preprint
at bioRxiv https://doi.org/10.1101/713412 (2019). Acknowledgements
68. Andrews, T. S. & Hemberg, M. Identifying cell populations with scRNASeq.
Bioconductor is supported by the National Human Genome Research Institute (NHGRI)
Mol. Asp. Med. 59, 114–122 (2018).
and National Cancer Institute (NCI) of the National Institutes of Health (NIH) (grant
69. Qiu, X. et al. Reversed graph embedding resolves complex single-cell
no. U41HG004059, U24CA180996), the European Union (EU) H2020 Personalizing
trajectories. Nat. Methods 14, 979–982 (2017).
Health and Care Program Action (contract number 633974) and the SOUND
70. Campbell, K. R. & Yau, C. switchde: inference of switch-like differential
Consortium. In addition, M.M., S.C.H., R.G., W.H., A.T.L.L. and D.R. are supported
expression along single-cell trajectories. Bioinformatics 33, 1241–1242 (2017).
by the Chan Zuckerberg Initiative (CZI) DAF (grant no. 2018-183201, 2018-183560),
71. Street, K. et al. Slingshot: cell lineage and pseudotime inference for single-cell
an advised fund of Silicon Valley Community Foundation. D.R., W.H., M.M. and
transcriptomics. BMC Genomics 19, 477 (2018).
S.C.H. are supported by 2019-002443 from the CZI. S.C.H. is supported by the NIH/
72. duVerle, D. A., Yotsukura, S., Nomura, S., Aburatani, H. & Tsuda, K. CellTree:
NHGRI (grant no. R00HG009007). R.A.A. and R.G. are supported by the Integrated
an R/bioconductor package to infer the hierarchical structure of cell
Immunotherapy Research Center at Fred Hutch. M.M. is supported by the NCI/NHGRI
populations from single-cell RNA-seq data. BMC Bioinform. 17,
(grant no. U24CA232979). L.G. is supported by a research fellowship from the German
363 (2016).
Research Foundation (grant no. GE3023/1-1). L.W. and V.J.C. are supported by the
73. Campbell, K. R. & Yau, C. Probabilistic modeling of bifurcations in single-cell
NCI (grant no. U24CA18099). V.J.C. is additionally supported by NCI U01 CA214846
gene expression data using a bayesian mixture of factor analyzers. Wellcome
and Chan Zuckerberg Initiative DAF (grant no. 2018-183436). ATLL received support
Open Res. 2, 19 (2017).
from CRUK (grant no. A17179) and the Wellcome Trust (grant no. WT/108437/Z/15).
74. Saelens, W., Cannoodt, R., Todorov, H. & Saeys, Y. A comparison of
F.M. is supported by the German Federal Ministry of Education and Research (grant
single-cell trajectory inference methods. Nat. Biotechnol. 37, 547 (2019).
no. BMBF 01EO1003). M.L.S. is supported by the German Network for Bioinformatics
75. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based
Infrastructure (grant no. 031A537B). D.R. is supported by the Programma per Giovani
approach for interpreting genome-wide expression profiles. Proc. Natl. Acad.
Ricercatori Rita Levi Montalcini from the Italian Ministry of Education, University and
Sci. USA 102, 15545–15550 (2005).
Research. H.P. is supported by the NIH Bioconductor grant (no. U41HG004059).
76. Kanehisa, M., Furumichi, M., Tanabe, M., Sato, Y. & Morishima, K. KEGG:
new perspectives on genomes, pathways, diseases and drugs. Nucleic Acids
Author contributions
Res. 45, 353–361 (2017).
77. Fabregat, A. et al. The reactome pathway knowledgebase. Nucleic Acids Res. E.B., V.J.C., L.N.C., L.G., F.M., K.R., D.R., C.S. and L.W. contributed equally to this work.
44, 481–487 (2015). S.C.H. and R.G. contributed equally to the supervision of this work. S.C.H. and R.G.
78. Ashburner, M. et al. Gene ontology: tool for the unification of biology. conceptualized the manuscript. R.A.A., A.T.L.L., S.C.H. and R.G. wrote the manuscript
Nat. Genet. 25, 25–29 (2000). with contributions and input from all authors. All authors read and approved the
79. Geistlinger, L., Csaba, G. & Zimmer, R. Bioconductor’s EnrichmentBrowser: final manuscript.
seamless navigation through combined results of set and network-based
enrichment analysis. BMC Bioinform. 17, 45 (2016). Competing interests
80. Alhamdoosh, M. et al. Combining multiple tools outperforms individual
R.G. declares ownership in CellSpace Biosciences.
methods in gene set enrichment analyses. Bioinformatics 33, 414–424 (2017).
81. Aibar, S. et al. SCENIC: single-cell regulatory network inference and
clustering. Nat. Methods 14, 1083–1086 (2017). Additional information
82. Buettner, F., Pratanwanich, N., McCarthy, D. J., Marioni, J. C. & Stegle, O.
Supplementary information is available for this paper at https://doi.org/10.1038/
fscLVM: scalable and versatile factor analysis for single-cell RNA-seq.
s41592-019-0654-x.
Genome Biol. 18, 212 (2017).
83. Aran, D. et al. Reference-based analysis of lung single-cell sequencing reveals Correspondence should be addressed to R.G. or S.C.H.
a transitional profibrotic macrophage. Nat. Immunol. 20, 163–172 (2019). Peer review information Lei Tang was the primary editor on this article and managed its
84. Zappia, L., Phipson, B. & Oshlack, A. Splatter: simulation of single-cell RNA editorial process and peer review in collaboration with the rest of the editorial team.
sequencing data. Genome Biol. 18, 174 (2017).
Reprints and permissions information is available at www.nature.com/reprints.
85. Kimes, P. K. & Reyes, A. Reproducible and replicable comparisons using
SummarizedBenchmark. Bioinformatics 35, 137–139 (2019). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
86. Tian, L. et al. Benchmarking single cell RNA-sequencing analysis pipelines published maps and institutional affiliations.
using mixture control experiments. Nat. Methods 16, 479–487 (2019). © Springer Nature America, Inc. 2019
NATuRE METHODS | VOL 17 | FEBRUARY 2020 | 137–145 | www.nature.com/naturemethods 145
