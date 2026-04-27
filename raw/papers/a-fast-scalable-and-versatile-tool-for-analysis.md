---
source_path: /mnt/c/Users/Administrator/Zotero/storage/KR9H7ZW3/Zhang 等 - 2024 - A fast, scalable and versatile tool for analysis of single-cell omics data.pdf
ingested: 2026-04-23
sha256: caa9868c3455d3fa
---

nature methods
Article https://doi.org/10.1038/s41592-023-02139-9
A fast, scalable and versatile tool for analysis
of single-cell omics data
Received: 9 June 2023 Kai Zhang 1,6, Nathan R. Zemke1,2, Ethan J. Armand1,3 & Bing Ren 1,2,4,5
Accepted: 23 November 2023
Single-cell omics technologies have revolutionized the study of gene
Published online: 8 January 2024
regulation in complex tissues. A major computational challenge in
Check for updates
analyzing these datasets is to project the large-scale and high-dimensional
data into low-dimensional space while retaining the relative relationships
between cells. This low dimension embedding is necessary to decompose
cellular heterogeneity and reconstruct cell-type-specific gene regulatory
programs. Traditional dimensionality reduction techniques, however,
face challenges in computational efficiency and in comprehensively
addressing cellular diversity across varied molecular modalities. Here we
introduce a nonlinear dimensionality reduction algorithm, embodied in
the Python package SnapATAC2, which not only achieves a more precise
capture of single-cell omics data heterogeneities but also ensures efficient
runtime and memory usage, scaling linearly with the number of cells.
Our algorithm demonstrates exceptional performance, scalability and
versatility across diverse single-cell omics datasets, including single-cell
assay for transposase-accessible chromatin using sequencing, single-cell
RNA sequencing, single-cell Hi-C and single-cell multi-omics datasets,
underscoring its utility in advancing single-cell analysis.
Rapid advancements in single-cell omics technologies have enabled analyses such as clustering, batch correction, data integration and
the analysis of the gene regulatory programs encoded in the genome at visualization. Effective dimensionality reduction techniques are instru-
unprecedented resolution and scale1. Single-cell analysis of genomes, mental for visualization of distinct cell populations, identification of
transcriptomes, open chromatin landscapes, histone modifications, rare cell types and delineation of cell-type-specific transcriptional
transcription factor binding, DNA methylation, chromatin architec- regulatory programs2. Currently, single-cell omics dimensionality
ture, and so on, have provided valuable insights into the mechanisms reduction algorithms fall into two main categories: linear and non-
governing cellular identity and regulation1. However, the extreme scale linear techniques. Linear dimensionality reduction algorithms,
and complexity of single-cell omics data often present substantial such as principal component analysis (PCA), used by SCANPY3 and
computational challenges, necessitating the development of efficient, Seurat4, for single-cell RNA-sequencing (scRNA-seq) data analysis,
scalable and robust methods for data analysis2. and latent semantic indexing (LSI) used by ArchR5 and Signac6 for
A crucial step in analyzing single-cell omics data is to project the single-cell assay for transposase-accessible chromatin using sequenc-
high-dimensional data into low-dimensional space while retaining ing (scATAC-seq) data analysis, are popular due to their computa-
the relative relationships between cells, a process known as dimen- tional efficiency and scalability. However, these algorithms are not
sionality reduction. This step is key to the success of downstream optimal for handling single-cell datasets with complex and nonlinear
1Department of Cellular and Molecular Medicine, University of California, San Diego School of Medicine, La Jolla, CA, USA. 2Center for Epigenomics,
University of California, San Diego School of Medicine, La Jolla, CA, USA. 3Bioinformatics and Systems Biology Program, University of California, San Diego,
La Jolla, CA, USA. 4Ludwig Institute for Cancer Research, La Jolla, CA, USA. 5Institute for Genomic Medicine, University of California, San Diego, La Jolla,
CA, USA. 6Present address: Westlake Laboratory of Life Sciences and Biomedicine, School of Life Sciences, Westlake University, Hangzhou, China.
e-mail: biren@health.ucsd.edu
Nature Methods | Volume 21 | February 2024 | 217–227 217
Article https://doi.org/10.1038/s41592-023-02139-9
structures, such as single-cell Hi-C (scHi-C) and single-cell multimodal reduction subroutine is readily applicable to scATAC-seq, scRNA-seq,
omics datasets. single-cell DNA methylation and scHi-C data, showcasing its adapt-
Nonlinear dimensionality reduction methods address these issues ability. To enhance performance and scalability, SnapATAC2 uses the
by more effectively capturing complex and often nonlinear cell rela- Rust26 programming language for executing computationally intensive
tionships. Examples include latent Dirichlet allocation (LDA) used for subroutines and provides a Python27 interface for seamless installation
scATAC-seq and scHi-C data7,8, Laplacian-based algorithms used for and user-friendly operation. This combination allows for efficient pro-
scRNA-seq and scATAC-seq data9–13, and various neural network models cessing of large-scale single-cell omics data while maintaining acces-
developed for scRNA-seq, scATAC-seq and scHi-C data14–18. Nonlinear sibility for researchers across various levels of expertise. To further
dimensionality reduction methods have also become the standard improve scalability when handling large-scale single-cell data, on-disk
approach for single-cell data visualization. For example, t-distributed data structures and out-of-core algorithms are used whenever possible.
stochastic neighbor embedding19 and uniform manifold approxi- These modifications facilitate the analysis of large datasets without
mation and projection (UMAP)20 are two widely used algorithms for overburdening system resources. Additionally, SnapATAC2 is modu-
this purpose, despite recent concerns regarding their reliability and lar and adaptable, and allows users to tailor their analysis to specific
validity21. While nonlinear methods excel in handling complex struc- requirements and integrate with other software packages from the
tures and projecting data into low-dimensional manifolds, they are scverse28 ecosystem, such as SCANPY3 and scvi-tools14.
generally computationally inefficient, with limited scalability. For The SnapATAC2 package is made up of four main parts: preproc-
instance, LDA relies on the Markov chain Monte Carlo algorithm for essing, embedding/clustering, functional enrichment analysis and
model training, which is slow to converge, computationally expen- multimodal omics analysis (Fig. 1a). The preprocessing module handles
sive and difficult to parallelize, making it difficult to be applied to raw BAM files, assesses data quality, creates count matrices and spots
large datasets22. Laplacian-based techniques like our previous work, doublets, ensuring a strong base for downstream analysis. The core of
SnapATAC9, necessitate computing similarity matrices between all SnapATAC2 is its embedding/clustering module, which introduces a
pairs of cells, which leads to quadratic memory usage increase with the new algorithm for reducing data dimensions. This module also helps in
number of cells23,24. Deep neural network models, known for their high identifying unique cell clusters and revealing biological patterns. The
training costs, often require specialized computational hardware such functional enrichment module offers detailed data interpretation like
as graphics processing units (GPUs) to be computationally feasible. differential accessibility and motif analysis. Finally, the multimodal
In this study, we describe a nonlinear dimensionality reduction omics analysis part allows for the examination of complex and mul-
algorithm that achieves both computational efficiency and accuracy tifaceted biological datasets, combining different types of biological
in discerning cellular composition of complex tissues from a broad data, and building networks to understand gene regulation.
spectrum of single-cell omics data types. The key innovation of our
algorithm is the use of a matrix-free spectral embedding algorithm Efficient and accurate cell embedding for scATAC-seq data
to project single-cell omics data into a low-dimensional space that Spectral embedding, also known as Laplacian eigenmaps, is a widely
preserves the intrinsic geometric properties of the underlying data. used technique for nonlinear dimensionality reduction29. This method
Unlike the conventional spectral embedding approach that requires boasts several key advantages, such as locality preservation, noise
the construction of the graph Laplacian matrix, a process that demands reduction and a natural connection to clustering29. Spectral embedding
a storage space increasing quadratically with the number of cells, our techniques leverage the spectrum (eigenvalues and eigenvectors) of
algorithm achieves the same goal while avoiding this computationally the cell similarity matrix calculated from single-cell omics datasets
expensive step. Specifically, we utilize the Lanczos algorithm25 to derive to perform dimensionality reduction. However, the computation of
eigenvectors while implicitly using the Laplacian matrix. This strategy this matrix is a rate-limiting step and a memory bottleneck, creating
substantially shortens the time and space complexity, making it linearly challenges for handling datasets consisting of large numbers of cells.
proportional to the number of cells in the single-cell data. To evaluate For example, the memory usage of the similarity matrix for a dataset
the accuracy and utility of our algorithm, we conducted extensive with one million cells is approximately 7 TB, far beyond the capacity
benchmarking using a variety of datasets that encompass diverse of most computational servers. To address this barrier, we devised a
experimental protocols, species and tissue types. The results showed matrix-free spectral embedding algorithm that efficiently computes
that our matrix-free spectral embedding algorithm outperforms exist- eigenvectors using the Lanczos algorithm25, eliminating the need for
ing methods in terms of speed, scalability and precision in resolving constructing a full similarity matrix (Fig. 1b and Methods). This method
cell heterogeneity. Furthermore, we showed that our algorithm can be exhibits linear space and time usage relative to the input matrix size,
extended to diverse molecular modalities of single-cell omics datasets, resulting in a faster and memory-efficient approach for processing of
revealing cell heterogeneity by leveraging complementary information large datasets. Notably, our algorithm avoids heuristic approximations,
from different single-cell omics data types. delivering precise solutions, distinguishing it from previous methods
We have implemented these algorithmic advancements in a that generate approximate outcomes10,11,30 (Methods).
Python package called SnapATAC2. This package is a major revamp To benchmark the performance of SnapATAC2, we generated syn-
of the original SnapATAC, offering substantial improvements such as thetic scATAC-seq datasets with varying cell numbers and compared
increased speed, reduced memory usage, more reliable performance the scalability of the matrix-free spectral embedding algorithm to
and a comprehensive analysis framework for diverse single-cell omics other widely used dimensionality reduction algorithms, such as LSI
data. SnapATAC2 is freely available at https://github.com/kaizhang/ (used by ArchR5 and Signac6), LDA (used by cisTopic7), PCA (used by
SnapATAC2/. EpiScanpy31) and classic spectral embedding with the Jaccard index
(implemented in the original SnapATAC9 package). In addition to these,
Results we also considered deep neural network-based approaches, such as
An overview of the SnapATAC2 workflow PeakVI15, scBasset16 and SCALE17. The benchmarks were conducted on a
SnapATAC2 is a comprehensive, high-performance solution for Linux server utilizing four cores of a 2.6 GHz Intel Xeon Platinum 8358
single-cell omics data analysis. Like the original SnapATAC9, SnapA- CPU. For neural network methods, we additionally used an A100 GPU
TAC2 offers a wide range of functionalities to streamline the analysis to accelerate calculations and monitored the runtime over a total of
of scATAC-seq data across multiple stages of the process. Moreover, 50 epochs, a commonly accepted minimum number of epochs required
SnapATAC2 is designed with flexibility in mind, intended for a vari- for algorithmic convergence. Our findings, illustrated in Fig. 1c, show
ety of single-cell omics data types. For instance, its dimensionality that SnapATAC2, along with ArchR, Signac and EpiScanpy, had the least
Nature Methods | Volume 21 | February 2024 | 217–227 218
Article https://doi.org/10.1038/s41592-023-02139-9
30
20
10
0
1,000 10,000 100,000 1M
Number of unique fragments
Nature Methods | Volume 21 | February 2024 | 217–227 219
erocs
tnemhcirne
SST
Preprocessing Embedding and clustering Multimodal analysis
slleC
b diag
Features
1.2
1 2 1.09 0.400.80 0.45 0.90 0.3
0.9 Lanczos iteration by Arbitrary
1 3 0.40 1.09 1.20 0.67 0.74
0.40.8
1 0.40 0.40 1.00
1.2 1.3
Normalize to 1.1
IDF
unit norm Top k eigenvectors
c d
125
100
75
50
25
0
0
Number of cells
)BG(
yromeM
SnapATAC2 ArchR (LSI)
Signac (LSI) SnapATAC
cisTopic (LDA) epiScanpy (PCA)
800
600
400
200
0
0 50,000 100,000 150,000 200,000 50,000 100,000 150,000 200,000 50,000 100,000 150,000 200,000
Number of cells
e
SnapATAC2 5.22 h 63.4% cost reduction
14.27
ArchR h
Process and filter BAM file
Import data and compute QC metrics
Generate cell-by-bin matrix
Detect and remove doublets
Perform dimension reduction
Perform batch correction
Perform cell clustering
)nim(
desu
emiT
a
BAM file processing Matrix-free spectral embedding Peak calling Data integration
Import data and create h5ad file Batch correction Differential peak analysis Co-embedding of multiple modalities
Doublet identification & cell filtering Graph-based clustering Motif enrichment analysis Regulatory network analysis
SnapATAC2 ArchR (LSI) PeakVI (50 epoch)
SCALE (50 epoch) Signac (LSI) SnapATAC
cisTopic (LDA) epiScanpy (PCA) scBasset (50 epoch)
25
20
15
10
5
0
0
Number of cells
sepyt
lleC
Functional analysis
Target genes
92 sci-ATAC-seq data Run time
benchmark
~650,000 cells
>23 billion raw reads
1.6 TB
Fig. 1 | SnapATAC2 enables comprehensive and scalable analysis of scATAC- dimensionality reduction algorithms for scATAC-seq data. d, Line plots
seq data. a, Overview of the SnapATAC2 Python package, featuring four primary comparing memory usage of various dimensionality reduction algorithms
modules: preprocessing, embedding/clustering, functional enrichment analysis for scATAC-seq data. Neural network-based methods were excluded from this
and multimodal analysis. b, Schematic representation of the matrix-free comparison because their memory usage does not scale with the number of
spectral embedding algorithm in SnapATAC2, consisting of four main steps: cells (Methods). e, Runtime comparison between ArchR and SnapATAC2 for end-
feature scaling with inverse term frequency, row-wise L norm normalization, to-end analysis of 92 raw BAM files produced by scATAC-seq experiments. TSS,
2
normalization using the degree matrix and eigenvector calculation through transcription start site; QC, quality control.
the Lanczos algorithm25. c, Line plots comparing running times of various
Article https://doi.org/10.1038/s41592-023-02139-9
increase in runtime as the number of cells in the dataset expanded. We observed similar robustness in performance when assess-
Neural network-based methods, despite their linear scalability, were ing noise levels. SnapATAC2 achieved perfect ARI scores (1.0) at all
considerably slower. For example, SnapATAC2 took only 13.4 min to examined noise levels, followed closely by Signac and the original
analyze a dataset with 200,000 cells, whereas PeakVI needed approxi- SnapATAC (Fig. 2d). In comparison, SCALE and PeakVI showed the most
mately 4 h. sensitivity to noise, with their ARI scores dropping to 0.57 and 0.46,
Regarding memory efficiency, SnapATAC2 stood out by requiring respectively, at a noise level of 0.4 (Fig. 2d,e). Moreover, SnapATAC2
only 21 GB of memory to process 200,000 cells (Fig. 1d). In contrast, excelled in identifying rare cell populations in simulated datasets
the original SnapATAC package showed limitations, encountering with variable cell-type abundances (Extended Data Fig. 1). In sum-
out-of-memory errors when handling over 80,000 cells on a server mary, our results demonstrate that SnapATAC2 is highly robust to both
with 500 GB of available memory. cisTopic, although not constrained variable sequencing depths and noise levels, delivering consistently
by memory, demonstrated the highest growth in runtime among high-quality embeddings.
all tested methods (Fig. 1c,d). We excluded neural network-based
methods from memory usage comparisons, as their memory require- Benchmarking SnapATAC2 with real scATAC-seq data
ments do not scale with the cell count, thanks to the use of mini-batch To rigorously evaluate SnapATAC2’s performance in conditions that
training. Nevertheless, these methods do consume substantial closely resemble real experimental data, we analyzed multiple pub-
memory proportional to the number of features (for example, peaks licly available scATAC-seq datasets36–42. These datasets span different
or genes). For instance, PeakVI, scBasset and SCALE exhausted the technologies, species and tissue types (Table 1) and come with avail-
available memory on an A100 GPU with 40 GB when the feature count able cell-type labels. To ensure data reliability, we limited our analysis
exceeded 500,000. to datasets that have been broadly cited in the scientific literature.
One of the aims of SnapATAC2 is to offer a wide-ranging analysis We began our evaluation by comparing SnapATAC2 with
for scATAC-seq data, covering multiple stages of the process. ArchR has other dimensionality reduction algorithms using a well-regarded
been previously cited as one of the most scalable and comprehensive human hematopoietic system scATAC-seq dataset36. This dataset
software packages for similar tasks32. To evaluate how SnapATAC2 is widely recognized as a benchmark for scATAC-seq analysis meth-
measures up against ArchR, we conducted side-by-side analyses across ods, including 2,034 hematopoietic cells profiled and subjected to
eight critical stages in scATAC-seq data processing. These include fluorescence-activated cell sorting (FACS) from ten cell populations:
BAM file filtering and processing, data import, quality-control metric hematopoietic stem cells, multipotent progenitors, lymphoid-primed
calculation, cell-by-bin matrix creation, doublet identification and multipotent progenitors, common myeloid progenitors, granulocyte–
removal, dimensionality reduction, batch correction and clustering. macrophage progenitors, granulocyte–macrophage progenitor-like
We utilized a human single-cell atlas of chromatin accessibility for this cells, megakaryocyte–erythroid progenitors, common lymphoid pro-
comparison33. This atlas, which we previously published, comprises genitors, monocytes and plasmacytoid dendritic cells (Fig. 3a). To
92 scATAC-seq samples, around 650,000 cells, and more than 23 bil- assess the bio-conservation quality of the cell embeddings generated
lion raw reads, totaling a data size of 1.6 TB. According to our findings by each method, we used a suite of metrics: the ARI, adjusted mutual
(Fig. 1e), SnapATAC2 completed the analysis in 5.22 h on a Linux server information (AMI), cell-type average silhouette width (cell-type ASW)43
with eight CPU cores and 64 GB memory, while ArchR took 14.27 h for and graph integration local inverse Simpson’s index (graph iLISI)43.
the same tasks. To summarize, at this data scale, SnapATAC2 is nearly Detailed explanations of these metrics are available in the Methods.
three times faster than ArchR, leading to an approximate reduction in Our analysis revealed that SnapATAC2 outperformed the other eight
computational costs of 63.4%. methods examined, ranking highest based on the average scores across
all four metrics (Fig. 3b,c). Notably, nonlinear methods such as cisTopic,
SnapATAC2 is robust to noise and varying sequencing depths PeakVI and scBasset followed SnapATAC2. This pattern was further
We proceeded to assess the precision of our dimensionality reduction substantiated across nine additional benchmark datasets (Fig. 3d
algorithm in identifying the relationships between cells, in comparison and Extended Data Figs. 2–6), where nonlinear methods consistently
to other existing methods. For this purpose, we utilized a previously outperformed their linear counterparts.
published benchmark dataset of synthetic scATAC-seq data22, con- On average, SnapATAC2 achieved the top bio-conservation scores
sisting of eight simulated datasets with varying sequencing depths across all ten datasets and was followed by PeakVI, cisTopic and scBas-
(5,000, 2,500, 1,000, 500 and 250 reads per cell) and noise levels (0, 0.2 set (Fig. 3d). Beyond excelling in cell-type identification, SnapATAC2
and 0.4). Each dataset contains 1,200 cells and includes the following also presents several advantages over other high-performing methods
six cell types: hematopoietic stem cells, common myeloid progeni- like cisTopic and deep neural network-based algorithms. Specifically,
tors, erythroid cells, natural killer cells, CD4+ T cells and CD8+ T cells SnapATAC2 can operate without the need for specialized hardware
(Fig. 2a). After dimensionality reduction, we applied graph-based clus- like GPUs, requires substantially less computational time, maintains
tering using the Leiden algorithm34 and assessed the clustering qual- robust performance across diverse datasets and eliminates the need
ity with the adjusted Rand index (ARI), which measures the similarity for extensive hyperparameter tuning.
between two data clusterings and has been routinely used to assess
the performance of clustering algorithms22,35. We hypothesized that SnapATAC2 is applicable to a wide range of omics data types
high-quality embeddings should yield clusters consistent with the Spectral embedding is a versatile and effective technique across a broad
ground-truth cell-type labels, and hence resulted in high ARI scores. spectrum of applications. We next explored whether this algorithm
Our findings, illustrated in Fig. 2b, reveal that SnapATAC2 consist- could be applied to other single-cell data types, such as scRNA-seq
ently outperformed other methods across varying sequencing depths, and scHi-C.
achieving the highest ARI scores. For example, at a sequencing depth scHi-C data is notably sparse and exhibits an extraordinarily
of 5,000 reads per cell, all tested algorithms accurately identified the high dimensionality. Current computational methods struggle to
six cell types, garnering ARI scores between 0.94 and 1.00. However, fully utilize sparse scHi-C data for analyzing cell-to-cell variability in
when the sequencing depth was reduced to 1,000 reads per cell, only three-dimensional genome features. Therefore, we initially focused
SnapATAC2 and Signac maintained an ARI score above 0.9. Particularly, on scHi-C data and tested our method, SnapATAC2, on two datasets
PeakVI was highly sensitive to sequencing depth, its ARI score plum- with multiple cell types or known cell-state information, including a
meting to 0.006 at 250 reads per cell (Fig. 2b,c). In contrast, SnapATAC2 sci-Hi-C dataset8 made public by the 4D Nucleome Project (4DN) and
maintained a score of 0.47. a dataset from ref. 44. We converted scHi-C data into a cell-by-feature
Nature Methods | Volume 21 | February 2024 | 217–227 220
Article https://doi.org/10.1038/s41592-023-02139-9
CD4
CD8
CMP
Ery
HSC
NK
SnapATAC2 PeakVI
CD4 5
CD8
10 0 CMP
Ery
0 –5 HSC
NK
0 10 20 –5 0 5 10 15
count matrix by flattening the contact matrices of individual cells into Higashi (Fig. 4a,b), which is currently considered the state-of-the-art
vectors. This count matrix served as input for SnapATAC2’s matrix-free method in scHi-C analysis. What sets SnapATAC2 apart, especially when
spectral embedding algorithm. The resulting cell embeddings exhib- compared to Higashi, is its computational efficiency and accessibility.
ited clear patterns corresponding to the underlying cell types and cel- SnapATAC2 operates with a substantially reduced runtime and elimi-
lular states (Fig. 4a). We next compared the quality of cell embeddings nates the need for specialized hardware. This makes it a highly practical
generated by SnapATAC2 with three methods: Higashi18, scHiCluster45 choice for analyzing large-scale scHi-C datasets.
and PCA. Our analysis revealed that SnapATAC2 achieved substantially Extending our analysis, we applied SnapATAC2 to scRNA-seq data-
higher bio-conservation scores than both scHiCluster and PCA on both sets and compared its performance to two other methods commonly
datasets (Fig. 4a,b). Furthermore, it displayed performance on par with used for dimensionality reduction in this domain: scVI, a deep neural
Nature Methods | Volume 21 | February 2024 | 217–227 221
2-PAMU
a b
1
Bulk ATAC-seq data
0.75
In silico simulation
0.50
5 coverages 2 noise levels
0.25
scATAC-seq data
(Chen et al., 2019) 0
1,000 2,000 3,000 4,000 5,000
Number of reads per cell
c 250 reads per cell 1,000 reads per cell 2,500 reads per cell 5,000 reads per cell
15 15
5
4
10 10
0
2 5 5
SnapATAC2
0 5 0 0
–5
0 –5 –2
–10
–5 –10
5 7.5 10 12.5 –5 0 5 10 –5 0 5 –10 0 10
20
20
12 12 15
18
PeakVI 10
8
10
16 5
4
0
8 14
12 14 16 8 10 12 14 16 –10 –5 0 5 10 15 –5 0 5 10
UMAP-1
IRA Signac (LSI)
SnapATAC2 SnapATAC
ArchR (LSI) cisTopic (LDA)
PeakVI epiScanpy (PCA)
SCALE scBasset
1
0.8
0.6
0 0.1 0.2 0.3 0.4
Noise level
IRA
HSC
CMP
Ery CD4 CD8 NK
d e Noise level = 0.4
SnapATAC2
ArchR (LSI)
PeakVI
SCALE
Signac (LSI)
SnapATAC
cisTopic (LDA)
epiScanpy (PCA)
scBasset
Fig. 2 | SnapATAC2’s dimensionality reduction algorithm is robust to various coded based on the cell-type labels indicated in a. d, Line plot showing the ARI
noise levels and sequencing depths. a, Schema of the synthetic scATAC-seq (y axis) as a function of the noise level (x axis) for nine dimensionality reduction
datasets22 used in the present study. b, Line plot showing the ARI (y axis) as a methods. e, UMAP visualization of the embeddings generated by the best
function of the number of reads per cell (x axis) for nine dimensionality reduction performing method (SnapATAC2) and the worst performing method (PeakVI) for
methods. c, UMAP visualization of the embeddings generated by the best the simulated dataset at a noise level of 0.4. Individual cells are color coded based
performing method (SnapATAC2) and the worst performing method (PeakVI) for on the cell-type labels indicated in a. CMP, common myeloid progenitor; Ery,
the simulated dataset with varying sequencing depths. Individual cells are color erythroid; HSC, hematopoietic stem cell; NK, natural killer.
Article https://doi.org/10.1038/s41592-023-02139-9
Table 1 | Curated scATAC-seq benchmark datasets used in the present study
Dataset Protocol Tissue No. of cells No. of cell types No. of features Reads per cell
Buenrostro et al.36 IFC scATAC-seq Human bone marrow 2,034 10 237,440 15,409
10x brain 5k57 10x ATAC-seq Mouse cortex 2,317 10 155,093 38,282
10x PBMC 10k57 10x Multiome Human PBMCs 9,631 19 107,194 20,479
Chen et al.38 SNARE-seq Mouse cerebral cortex 9,190 22 241,757 2,641
GSE194122 (ref. 41)a 10x Multiome Human PBMCs 9,876 19 116,490 8,260
Ma et al.39 SHARE-seq Mouse skin 32,231 22 340,341 4,152
Trevino et al.37 10x ATAC-seq Human cerebral cortex 8,981 13 467,315 16,519
Yao et al.40 sci-ATAC-seq Mouse primary motor cortex 54,844 11 148,814 3,026
Zemke et al., human42a 10x Multiome Human primary motor cortex 15,284 20 380,517 16,854
Zemke et al., mouse42 10x Multiome Mouse primary motor cortex 45,089 19 330,448 28,880
aWe used a subset of the original dataset due to profound batch effects (Methods).
network-based approach14, and PCA, a standard linear method3,4,35,46. kernel matrix is calculated from each view; second, a joint kernel matrix
Across all five benchmark scRNA-seq datasets we tested35, SnapATAC2 is constructed by combining or co-regularizing the kernel matrices in
emerged as the top performer, generating cell embeddings that were a certain manner; and lastly, spectral embedding is performed using
most aligned with the underlying cell types (Fig. 4d,e and Extended the joint kernel matrix. In this study, we opted for kernel addition to
Data Fig. 7). It outperformed both PCA and scVI, which ranked second combine the kernel matrices, as it has shown to be an effective method
and third, respectively. One distinct advantage of SnapATAC2 is its for achieving excellent clustering results48,49. Moreover, kernel addition
independence from data centering or scaling, steps that are typically enables the extension of the matrix-free spectral embedding algorithm
essential for PCA-based analyses. We observed that PCA’s performance to multi-view spectral embedding while maintaining the linear time
suffered when applied to unscaled data, as evidenced by Fig. 4d. How- and space complexity of the algorithm (Methods).
ever, the process of scaling effectively converts a sparse matrix into a We applied this matrix-free multi-view spectral embedding algo-
dense one, which can be both computationally expensive and limiting, rithm to a 10x Genomics Multiome dataset, which jointly profiles chro-
especially for datasets with an extensive feature set. Overall, SnapA- matin accessibility and the transcriptome for 9,181 human peripheral
TAC2’s ability to function effectively without additional preprocessing blood mononuclear cells (PBMCs). To better evaluate the algorithm’s
steps like scaling not only maintains its computational efficiency but performance, we first annotated the cells according to a previously
also makes it a more versatile and practical tool for high-dimensional published single-cell atlas of human PBMCs4. To compare the perfor-
data analysis. mance of joint embedding with individual views, we also performed
SnapATAC2’s dimensionality reduction algorithm is also applicable spectral embedding on each modality separately. Our findings reveal
to single-cell DNA methylation data. When applied to 5-methylcytosine that, while independent unsupervised analyses of RNA and ATAC data
sequencing 2 (snmC-seq2) data generated in mouse pituitaries47, Sna- generated predominantly consistent cell classifications, there were
pATAC2 produced cell embeddings that are largely consistent with notable differences (Fig. 5a,b). For instance, CD8+ and CD4+ T cells
the cell types identified by the original study (Extended Data Fig. 8). were close to each other when analyzing the transcriptome but sepa-
Notably, the method provided finer resolution for some cell types, rated clearly in the ATAC data (Fig. 5a,b). Conversely, intermediate and
such as somatotropes and lactotropes. memory B cells partially overlapped when analyzing the ATAC data
In conclusion, SnapATAC2 is a versatile and effective method for but were more distinguishable in the transcriptomic data (Fig. 5a,b).
the analysis of various single-cell data types, including scATAC-seq, In comparison to the separate analysis of either modality, multi-view
scHi-C, scRNA-seq and single-cell DNA methylation data. It demon- spectral embedding using both modalities clearly separated CD4+
strates comparable or superior performance to existing methods, while and CD8+ T cells and uncovered subtle heterogeneity within B cells.
offering practical advantages such as reduced runtime and no need for Overall, the joint embedding of ATAC and RNA data enhanced the
specialized hardware. Finally, we incorporated batch correction bench- separation of cell types and revealed subtle heterogeneity within cell
marks into our evaluation, and SnapATAC2’s performance remained types, as evidenced by the increased silhouette scores across different
robust and reliable (Extended Data Fig. 9 and Supplementary Tables cell types (Fig. 5b).
1 and 2). This further attests to its practicality in real-world scenarios In our pursuit to further benchmark the performance of Sna-
where batch effects often pose a challenge. pATAC2, we compared it against other joint embedding techniques,
specifically MIRA50, Cobolt51 and MOFA+52. Using the same 10x Genom-
SnapATAC2 enables joint embedding of multi-omics data ics Multiome dataset, SnapATAC2 consistently ranked highest in
The rapid expansion of single-cell multimodal omics technologies, bio-conservation scores across all four evaluation metrics (Fig. 5c).
such as 10x Multiome (ATAC/RNA-seq), Paired-Tag48 and single-cell To broaden the scope of our comparative analysis, we also incorporated
methyl-Hi-C/single-nucleus methyl-3C sequencing44, has provided pow- a dataset profiling trimethylated histone H3 Lys 27 (H3K27me3) occu-
erful tools for investigating gene regulatory mechanisms. We therefore pancy and gene expression in 10,180 cells from the mouse frontal cor-
investigated the applicability of our algorithm to single-cell multimodal tex53. Once again, SnapATAC2 emerged as the top-performing method,
omics data. Multi-view spectral embedding is an extension of spectral achieving the highest average bio-conservation score (Fig. 5d). Beyond
embedding, which enables the joint embedding of multiple data rep- its exceptional accuracy, SnapATAC2 also showed unparalleled scal-
resentation views. This method has demonstrated its ability to har- ability. Across both datasets, it drastically outperformed MIRA, Cobolt
ness complementary information from individual views and enhance and MOFA+ in computational speed and memory efficiency, running
performance in downstream analyses, making it an ideal candidate more than 30 times faster than the next best method (Fig. 5c,d). In sum-
for analyzing single-cell multi-omics data. The multi-view spectral mary, these results validate SnapATAC2’s excellent performance not
embedding process typically consists of three steps: first, a similarity or only in bio-conservation quality but also in computational efficiency,
Nature Methods | Volume 21 | February 2024 | 217–227 222
Article https://doi.org/10.1038/s41592-023-02139-9
a HSC c
Human bone marrow
MPP FACS
LMPP CMP Freeze & bank
CLP pCD GMP MEP
scATAC-seq
(Buenrostro et al.)
B, T, Peripheral Monocyte, mDC, Ery,
NK cells pDC granulocytes mega
SnapATAC2 SnapATAC
15
10 10
5
5
0
0
–5 0 5 10 15 4 8 12 16
Buenrostro2018
Method Bio-conservation Average
1
0x_Brain5k
1
0x_PB
M C1 0k Buenrostro_2 018
Chen_
NBT_2 019 GSE194122
Ma_
Cell_2 02 0
Trevino_
Cell_2 021
Yao_
Nature_2 02
Z
1
e
mke_2
023_hu m
Z
a
e
n
mke_2
023_
mouse
scATAC-seq dataset
making it a highly robust and scalable solution for analyzing complex noise robustness and scalability, thus providing researchers with a pow-
single-cell multi-omics data. erful tool for investigating gene regulatory programs using single-cell
genomics, transcriptomics and epigenomics analysis.
Discussion SnapATAC2 offers a unique advantage in its seamless compat-
In the present study, we describe SnapATAC2 for the analysis of a diverse ibility with other software tools widely used in the single-cell analytics
array of single-cell omics data. The performance of SnapATAC2 exceeds ecosystem. By adopting the AnnData format, it facilitates effortless
that of existing dimensionality reduction methods in terms of accuracy, integration with established packages like SCANPY, scvi-tools and
Nature Methods | Volume 21 | February 2024 | 217–227 223
2-PAMU
Bio-conservation
Cell-type Graph
Method ARI AMI Average
ASW cLISI
SnapATAC2 1.00 1.00 0.75 0.82 0.89
cisTopic (LDA) 0.73 0.86 1.00 0.87 0.86
PeakVI 0.65 0.89 0.93 0.93 0.85
scBasset 0.55 0.71 0.92 1.00 0.80
SCALE 0.52 0.71 0.92 0.76 0.73
b
ArchR (LSI) 0.19 0.27 0.57 0.53 0.39
CLP MEP
Signac (LSI) 0.11 0.09 0.16 0.20 0.14
CMP MPP
GMP UNK epiScanpy (PCA) 0.07 0.00 0.00 0.15 0.05
HSC Mono
LMPP pDC SnapATAC 0.00 0.05 0.05 0.00 0.03
UMAP-1
d
SnapATAC2 1.00 1.00 0.89 0.91 0.91 1.00 0.90 1.00 0.91 0.79 0.93
PeakVI 0.74 0.76 0.85 0.51 0.93 0.89 0.64 0.79 0.99 1.00 0.81
cisTopic (LDA) 0.81 0.70 0.86 0.46 0.85 0.84 0.58 0.82 0.87 0.93 0.77
scBasset 0.83 0.17 0.80 1.00 0.91 0.00 0.99 0.96 0.26 0.75 0.67
ArchR (LSI) 0.84 0.83 0.39 0.41 0.47 0.76 0.46 0.59 0.63 0.52 0.59
SCALE 0.71 0.70 0.73 0.13 0.70 0.65 0.29 0.58 0.45 0.13 0.51
Signac (LSI) 0.44 0.46 0.14 0.25 0.17 0.54 0.06 0.63 0.01 0.47 0.32
SnapATAC 0.00 0.25 0.03 0.16 0.07 0.74 0.45 0.30 0.44 0.44 0.29
epiScanpy (PCA) 0.54 0.02 0.05 0.00 0.01 0.74 0.48 0.03 0.13 0.25 0.23
Fig. 3 | Benchmarking of SnapATAT2 and other dimensionality reduction A score of 1 indicates optimal performance. See Methods for metric details.
algorithms using real scATAC-seq data with cell labels. a, Overview of cell d, Table displaying the bio-conservation scores of nine dimensionality reduction
types analyzed in the Buenrostro et al. scATAC-seq dataset. b, UMAP visualization methods across ten benchmark datasets (Extended Data Figs. 2–6). CLP, common
of the embeddings generated by the best performing method (SnapATAC2) lymphoid progenitor; GMP, granulocyte–macrophage progenitor; LMPP,
and the worst performing method (original SnapATAC) for the Buenrostro et al. lymphoid-primed multipotent progenitor; MEP, megakaryocyte–erythroid
dataset. Individual cells are color coded based on the cell-type labels indicated progenitor; mono, monocyte; MPP, multipotent progenitor; pDC, plasmacytoid
in a. c, Table displaying normalized scores (0–1 range) of four metrics used to dendritic cell.
evaluate each method’s bio-conservation on the Buenrostro et al. dataset.
Article https://doi.org/10.1038/s41592-023-02139-9
a 4DN Kim (scHi-C)
GM12878
H1Esc
HAP1
HFF
IMR90
b c
4DN Kim (scHi-C) Lee et al. (scHi-C)
d e
SnapATAC2
Method Bio-conservation Average 15
10
5
0
–5
–5 0 5 10
scVI
10
8
6
4
Koh
Ku
mar
Zheng
mix4eq
Zheng
mix4uneq
Zheng
mix8eq 2
6
U
8
MAP-1
10 12
scRNA-seq dataset
SCENIC+54. This feature is especially advantageous for research- algorithms have been proposed to expedite spectral embedding10,11,23,30,
ers seeking to carry out specialized analyses, such as data imputa- our algorithm stands out as it does not rely on sub-sampling or approxi-
tion or trajectory inference, thereby enhancing the core functions mations, delivering the exact solution. This algorithm not only outper-
of SnapATAC2. forms current methods in identifying cell clusters and heterogeneity
The key innovation of SnapATAC2 lies in its matrix-free spectral but also maintains computational efficiency, making it highly suit-
embedding algorithm for dimensionality reduction. While numerous able for large-scale single-cell omics data analysis. Furthermore,
Nature Methods | Volume 21 | February 2024 | 217–227 224
2-PAMU
Higashi
12
8
4
0
3 6 9
Zhengmix4uneq (scRNA-seq)
2-PAMU
SnapATAC2 PCA scHiCluster
6 15
10 10 4
5
5 2
0
0 0
–5
–5 –2
0 5 10 –5 0 5 10 0 2.5 5
UMAP-1
Bio-conservation Bio-conservation
Cell-type Graph Cell-type Graph
Method ARI AMI Average Method ARI AMI Average
ASW cLISI ASW cLISI
SnapATAC2 1.00 1.00 1.00 1.00 1.00 Higashi 1.00 1.00 1.00 1.00 1.00
Higashi 0.82 0.74 0.66 0.96 0.79 SnapATAC2 0.84 0.92 0.88 1.00 0.91
PCA 0.43 0.69 0.32 1.00 0.61 PCA 0.52 0.63 0.49 0.96 0.65
scHiCluster 0 0 0 0 0 scHiCluster 0 0 0 0 0
SnapATAC2 0.95 0.95 0.97 1.00 0.87 0.95
PCA/scaled 0.87 0.92 0.96 0.63 0.57 0.79
PCA/unscaled 0.81 0.75 0.41 0.37 0.24 0.52
scVI 0 0.25 0.28 0 0.63 0.23
B cells Naive cytotoxic
CD14 monocytes Regulatory T
Fig. 4 | SnapATAC2 demonstrates superior performance over other each method’s bio-conservation on the Lee et al. dataset. d, Table displaying
methods on scHi-C and scRNA-seq datasets. a, UMAP visualization of the bio-conservation scores of four dimensionality reduction methods across
the embeddings generated by Higashi, SnapATAC2, scHiCluster and PCA for five benchmark datasets (Extended Data Fig. 7). e, UMAP visualization of the
the 4DN dataset by Kim et al. Cells are color coded based on cell-type labels. embeddings produced by the best performing method (SnapATAC2) and the
b, Table displaying normalized scores (0–1 range) of four metrics used to worst performing method (scVI) for the Zhengmix4uneq dataset35. Cells are color
evaluate each method’s bio-conservation on the 4DN dataset by Kim et al.8. coded according to cell-type labels.
c, Table displaying normalized scores (0–1 range) of four metrics used to evaluate
Article https://doi.org/10.1038/s41592-023-02139-9
20
10
0
–10 0 10 20
we demonstrated the versatility of the matrix-free spectral embed- One limitation of the matrix-free spectral embedding algorithm is
ding algorithm by applying it to various single-cell data types, includ- that it currently is implemented using only cosine function-based simi-
ing scATAC-seq, scRNA-seq, single-cell DNA methylation, scHi-C and larity. For some data types, researchers may prefer to use other metrics
single-cell multi-omics data. to quantify the cell-to-cell similarity. For instance, in our findings, the
Nature Methods | Volume 21 | February 2024 | 217–227 225
2PAMU
a
ATAC RNA ATAC + RNA
CD16 mono B naive B intermediate CD16 mono
15
B memory
CD8 CD14 mono
B intermediate CD14 mono 10 CD4 naive 10
B memory CD16 mono B naive
CD4 memory
B naive
CD4 naive 5 B intermediate
0 NK CD4 memory B memory
NK
CD4 memory
0
CD8 CD14 mono CD8
NK CD4 naive
–5 0 5 10 15 –10 0 10 20
UMAP1
B intermediate CD14 mono CD4 TCM CD8 TCM HSPC Platelet gdT
B memory CD16 mono CD4 TEM CD8 TEM MAIT T pDC
reg
B naive CD4 naive CD8 naive Eryth NK cDC2
b c
ATAC RNA ATAC + RNA Bio-conservation Scalability
Cell-type Graph Run Memory
Method ARI AMI Average
ASW cLISI time (min) (GB)
NK
SnapATAC2 1.00 1.00 1.00 1.00 1.00 1.88 5.80
MIRA 0.92 0.47 0.10 0.08 0.39 105.91 17.00
CD8 naive
MOFA+ 0 0.37 0.28 0.11 0.19 69.48 51.80
Cobolt 0.09 0 0 0 0.02 53.75 6.50
CD4 naive
PBMC (gene expression & ATAC - 9,181 cells)
d Bio-conservation Scalability
CD16 mono
Cell-type Graph Run Memory
Method ARI AMI Average
ASW cLISI time (min) (GB)
SnapATAC2 0.74 0.96 0.89 1.00 0.90 0.69 0.94
B memory
MIRA 1.00 0.97 0.79 0.75 0.88 35.35 9.80
Cobolt 0.65 1.00 1.00 0 0.66 21.86 3.10
B intermediate
MOFA+ 0 0 0 0.25 0.06 43.21 32.80
−0.6 −0.3 0 0.3 0.6
Mouse frontal cortex (gene expression & H3K27me3 - 10,180 cells)
Silhouette score
Fig. 5 | SnapATAC2 enables robust joint embedding of single-cell multi-omics the RNA modality or both modalities. The black line within each curve indicates
data. a, UMAP visualization of the embeddings generated by SnapATAC2 using the median value. c, Table comparing bio-conservation and scalability metrics of
ATAC modality (left), RNA modality (middle) or both modalities (right) on a 10x various joint embedding methods on 10x Genomics Multiome data from human
Genomics Multiome dataset consisting of 9,181 human PBMCs. Cells are color PBMCs. d, Table comparing bio-conservation and scalability metrics of various
coded based on cell-type labels. b, Violin plot comparing the silhouette scores joint embedding methods on Paired-Tag data from mouse frontal cortex.
of selected cell types derived from embeddings produced by the ATAC modality,
Article https://doi.org/10.1038/s41592-023-02139-9
Euclidean distance yielded more accurate results for the protein expres- 17. Xiong, L. et al. SCALE method for single-cell ATAC-seq analysis via
sion data used in cellular indexing of transcriptomes and epitopes by latent feature extraction. Nat. Commun. 10, 4576 (2019).
sequencing experiments55. Future developments could extend the 18. Zhang, R., Zhou, T. & Ma, J. Multiscale and integrative single-cell
matrix-free algorithm to accommodate other similarity metrics. For hi-c analysis with higashi. Nat. Biotechnol. 40, 254–261 (2021).
instance, a potential solution involves leveraging a small set of land- 19. Maaten, Lvander & Hinton, G. Visualizing data using t-SNE.
mark points to transform the given data into sparse feature vectors56, J. Mach. Learn. Res. 9, 2579–2605 (2008).
followed by the application of the scalable matrix-free spectral embed- 20. McInnes, L., Healy, J., Saul, N. & Großberger, L. UMAP: uniform
ding algorithm. In conclusion, SnapATAC2 represents a substantial manifold approximation and projection. J. Open Source Softw. 3,
advancement in single-cell data analysis, offering an accessible, scal- 861 (2018).
able and high-performance solution for researchers studying epig- 21. Chari, T. & Pachter, L. The specious art of single-cell genomics. 19,
enomics. With continued development and optimization, SnapATAC2 e1011288 (2021).
has the potential to become a general tool in single-cell multi-omics 22. Chen, H. et al. Assessment of computational methods for
data analysis, ultimately facilitating new biological discoveries. the analysis of single-cell ATAC-seq data. Genome Biol. 20,
241 (2019).
Online content 23. Tremblay, N. & Loukas, A. Approximating spectral clustering via
Any methods, additional references, Nature Portfolio reporting sum- sampling: a review. in Sampling Techniques for Supervised or
maries, source data, extended data, supplementary information, Unsupervised Tasks 129–183 (Springer International Publishing,
acknowledgements, peer review information; details of author contri- 2019).
butions and competing interests; and statements of data and code avail- 24. Fowlkes, C., Belongie, S., Chung, F. & Malik, J. Spectral grouping
ability are available at https://doi.org/10.1038/s41592-023-02139-9. using the Nystrom method. IEEE Trans. Pattern Anal. Mach. Intell.
26, 214–225 (2004).
References 25. Lanczos, C. An iteration method for the solution of the eigenvalue
1. Preissl, S., Gaulton, K. J. & Ren, B. Characterizing cis-regulatory problem of linear differential and integral operators. J. Res. Natl
elements using single-cell epigenomics. Nat. Rev. Genet. 24, Bur. Stand. 45, 255 (1950).
21–43 (2022). 26. Klabnik, S. & Nichols, C. The Rust Programming Language 2nd
2. Lähnemann, D. et al. Eleven grand challenges in single-cell data edition (No Starch Press, 2023).
science. Genome Biol. 21, 31 (2020). 27. Van Rossum, G. & Drake, F. L. The Python Language Reference
3. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell Manual (Network Theory Limited, 2011).
gene expression data analysis. Genome Biol. 19, 15 (2018). 28. Virshup, I. et al. The scverse project provides a computational
4. Hao, Y. et al. Integrated analysis of multimodal single-cell data. ecosystem for single-cell omics data analysis. Nat. Biotechnol. 41,
Cell 184, 3573–3587 (2021). 604–606 (2023).
5. Granja, J. M. et al. ArchR is a scalable software package for 29. Belkin, M. & Niyogi, P. Laplacian eigenmaps for dimensionality
integrative single-cell chromatin accessibility analysis. Nat. reduction and data representation. Neural Comput. 15, 1373–1396
Genet. 53, 403–411 (2021). (2003).
6. Stuart, T., Srivastava, A., Madad, S., Lareau, C. A. & Satija, R. 30. Chen, G. Scalable spectral clustering with cosine similarity. in
Single-cell chromatin state analysis with signac. Nat. Methods 18, 2018 24th International Conference On Pattern Recognition (ICPR)
1333–1341 (2021). (IEEE, 2018).
7. González-Blas, C. B. et al. cisTopic: cis-regulatory topic 31. Danese, A. et al. EpiScanpy: integrated single-cell epigenomic
modeling on single-cell ATAC-seq data. Nat. Methods 16, analysis. Nat. Commun. 12, 5228 (2021).
397–400 (2019). 32. Baek, S. & Lee, I. Single-cell ATAC sequencing analysis: from
8. Kim, H. -J. et al. Capturing cell type-specific chromatin data preprocessing to hypothesis generation. Computat. Struct.
compartment patterns by applying topic modeling to single-cell Biotechnol. J. 18, 1429–1439 (2020).
HI-C data. PLoS Comput. Biol. 16, e1008173 (2020). 33. Zhang, K. et al. A single-cell atlas of chromatin accessibility in the
9. Fang, R. et al. Comprehensive analysis of single cell ATAC-seq human genome. Cell 184, 5985–6001 (2021).
data with SnapATAC. Nat. Commun. 12, 1337 (2021). 34. Traag, V. A., Waltman, L. & van Eck, N. J. From Louvain to Leiden:
10. Schwartz, G. W. et al. TooManyCells identifies and visualizes guaranteeing well-connected communities. Sci. Rep. 9, 5233
relationships of single-cell clades. Nat. Methods 17, 405–413 (2019).
(2020). 35. Duò, A., Robinson, M. D. & Soneson, C. A systematic performance
11. Schwartz, G. W., Zhou, Y., Petrovic, J., Pear, W. S. & Faryabi, R. evaluation of clustering methods for single-cell RNA-seq data.
B. TooManyPeaks identifies drug-resistant-specific regulatory F1000Research 7, 1141 (2020).
elements from single-cell leukemic epigenomes. Cell Rep. 36, 36. Buenrostro, J. D. et al. Integrated single-cell analysis maps the
109575 (2021). continuous regulatory landscape of human hematopoietic
12. Haghverdi, L., Buettner, F. & Theis, F. J. Diffusion maps for differentiation. Cell 173, 1535–1548 (2018).
high-dimensional single-cell analysis of differentiation data. 37. Trevino, A. E. et al. Chromatin and gene-regulatory dynamics of
Bioinformatics 31, 2989–2998 (2015). the developing human cerebral cortex at single-cell resolution.
13. Angerer, P. et al. Destiny: diffusion maps for large-scale single-cell Cell 184, 5053–5069 (2021).
data in R. Bioinformatics 32, 1241–1243 (2015). 38. Chen, S., Lake, B. B. & Zhang, K. High-throughput sequencing of
14. Gayoso, A. et al. A Python library for probabilistic analysis of the transcriptome and chromatin accessibility in the same cell.
single-cell omics data. Nat. Biotechnol. 40, 163–166 (2022). Nat. Biotechnol. 37, 1452–1457 (2019).
15. Ashuach, T., Reidenbach, D. A., Gayoso, A. & Yosef, N. PeakVI: a 39. Ma, S. et al. Chromatin potential identified by shared
deep generative model for single-cell chromatin accessibility single-cell profiling of RNA and chromatin. Cell 183, 1103–1116
analysis. Cell Rep. Methods 2, 100182 (2022). (2020).
16. Yuan, H. & Kelley, D. R. scBasset: sequence-based modeling 40. Yao, Z. et al. A transcriptomic and epigenomic cell atlas
of single-cell ATAC-seq using convolutional neural networks. of the mouse primary motor cortex. Nature 598, 103–110
Nat. Methods 19, 1088–1096 (2022). (2021).
Nature Methods | Volume 21 | February 2024 | 217–227 226
Article https://doi.org/10.1038/s41592-023-02139-9
41. Luecken, M. et al. A sandbox for prediction and integration of 53. Xie, Y. et al. Droplet-based single-cell joint profiling of histone
DNA, RNA, and proteins in single cells. in Proceedings of the modifications and transcriptomes. Nat. Struct. Mol. Biol. 30,
Neural Information Processing Systems Track on Datasets and 1428–1433 (2023).
Benchmarks (eds. Vanschoren, J. & Yeung, S.) vol. 1 (Curran, 2021). 54. González-Blas, C. B. et al. SCENIC+: single-cell multiomic
42. Zemke, N. R. et al. Conserved and divergent gene regulatory inference of enhancers and gene regulatory networks. Nat.
programs of the mammalian neocortex. Nature https://doi. Methods 20, 1355–1367 (2023).
org/10.1038/s41586-023-06819-6 (2023). 55. Stoeckius, M. et al. Simultaneous epitope and transcriptome
43. Luecken, M. D. et al. Benchmarking atlas-level data integration in measurement in single cells. Nat. Methods 14, 865–868
single-cell genomics. Nat. Methods 19, 41–50 (2021). (2017).
44. Lee, D.-S. et al. Simultaneous profiling of 3D genome structure 56. Chen, G. A scalable spectral clustering algorithm based on
and DNA methylation in single human cells. Nat. Methods 16, landmark-embedding and cosine similarity. In Lecture Notes in
999–1006 (2019). Computer Science 52–62 (Springer International Publishing,
45. Zhou, J. et al. Robust single-cell HI-C clustering by convolution- 2018).
and random-walkbased imputation. Proc. Natl Acad. Sci. USA 116, 57. Cao, Z.-J. & Gao, G. Multi-omics single-cell data integration
14011–14018 (2019). and regulatory inference with graph-linked embedding. Nat.
46. Raimundo, F., Vallot, C. & Vert, J. -P. Tuning parameters of Biotechnol. 40, 1458–1466 (2022).
dimensionality reduction methods for single-cell RNA-seq
analysis. Genome Biol. 21, 212 (2020). Publisher’s note Springer Nature remains neutral with regard
47. Ruf-Zamojski, F. et al. Single nucleus multi-omics regulatory to jurisdictional claims in published maps and institutional
landscape of the murine pituitary. Nat. Commun. 12, 2677 (2021). affiliations.
48. Zhu, C. et al. Joint profiling of histone modifications and
transcriptome in single cells from mouse brain. Nat. Methods 18, Open Access This article is licensed under a Creative Commons
283–292 (2021). Attribution 4.0 International License, which permits use, sharing,
49. Kumar, A., Rai, P. & Daumé, H. Co-regularized multi-view spectral adaptation, distribution and reproduction in any medium or format,
clustering. in Proceedings of the 24th International Conference as long as you give appropriate credit to the original author(s) and the
on Neural Information Processing Systems 1413–1421 (Curran source, provide a link to the Creative Commons license, and indicate
Associates, 2011). if changes were made. The images or other third party material in this
50. Lynch, A. W. et al. MIRA: joint regulatory modeling of multimodal article are included in the article’s Creative Commons license, unless
expression and chromatin accessibility in single cells. Nat. indicated otherwise in a credit line to the material. If material is not
Methods 19, 1097–1108 (2022). included in the article’s Creative Commons license and your intended
51. Gong, B., Zhou, Y. & Purdom, E. Cobolt: Integrative analysis of use is not permitted by statutory regulation or exceeds the permitted
multimodal single-cell sequencing data. Genome Biol. 22, 351 use, you will need to obtain permission directly from the copyright
(2021). holder. To view a copy of this license, visit http://creativecommons.
52. Argelaguet, R. et al. MOFA+: a statistical framework for org/licenses/by/4.0/.
comprehensive integration of multi-modal single-cell data.
Genome Biol. 21, 111 (2020). © The Author(s) 2024
Nature Methods | Volume 21 | February 2024 | 217–227 227
Article https://doi.org/10.1038/s41592-023-02139-9
Methods iteratively refined by the Lanczos algorithm. By using the specific order
Dimensionality reduction using spectral embedding of operations shown in the formula, we can reduce the computational
In this section, we outline the core algorithms used to perform dimen- cost of the matrix–vector product to 2z + n, where n is the number of
sionality reduction in the SnapATAC2 package. We first describe the rows in X and z is the number of nonzero elements in X. In comparison,
preprocessing steps and then the classic spectral embedding method performing this operation on the full similarity matrix requires n2
that works for arbitrary similarity metrics. Finally, we describe the computations, which is prohibitively expensive for a large number of
matrix-free spectral embedding algorithm that works only for cosine cells. Thus, our matrix-free method is substantially faster and more
similarity, but substantially decreases the running time and memory memory efficient. The pseudocode for our algorithm is shown in
usage. Note the steps described below can be accomplished using the Extended Data Fig. 10a.
‘snapatac2.tl.spectral’ function from the SnapATAC2 package.
Nyström method for out-of-sample embedding
Preprocessing. Given a cell-by-feature count matrix C∈ℝn×p, we first The matrix-free method described above is very fast and memory efficient.
scale the columns of the matrix by the inverse document frequency However, for massive datasets with hundreds of millions of cells, storing
(IDF). The IDF of a column or a feature f is defined by idf(f)=log n . the cell-by-feature count matrix itself may already be a challenge. To cir-
1+||i∶Ci,f≠0||
cumvent this memory constraint, we choose to sample a subset of cells
Spectral embedding. Assuming the cell-by-feature count matrix C from the full dataset and use these as landmarks to perform out-of-sample
has been preprocessed according to the procedures described above, embedding using the Nyström method24,59. The pseudocode for this algo-
in classic spectral embedding, we first compute the n × n pairwise rithm and detailed benchmark comparisons can be found in Extended
similarity matrix W such that Wij=δ(Ci∗,Cj∗), where δ∶ℝp×ℝp→ℝ is Data Fig. 10b,c, Supplementary Fig. 1 and Supplementary Note 1.
the function defining the similarity between any two cells. Typical
choices of δ include the Jaccard index and the cosine similarity. Multi-view spectral embedding
We then compute the symmetric normalized graph Laplacian In this section, we extend our matrix-free spectral embedding method
Lsym=I−D−1/2WD−1/2, where I is the identity matrix and D = diag(W1). to perform dimensionality reduction on multimodal single-cell data.
The bottom eigenvectors of L are selected as the lower-dimensional Assume we have data in multiple views, for example, chromatin
sym
embedding. The corresponding eigenvectors can be computed alter- accessibility and gene expressions, represented by a sequence
natively as the top eigenvectors of the similarly normalized weight of count matrices {Xi,X2,…,Xk}∈ℝn×pk. Our objective is to obtain a
matrix: W˜ =D−1/2WD−1/2. low-dimensional representation of the data while preserving cell similar-
ity in each view using the spectral embedding method. One approach
Matrix-free spectral embedding with cosine similarity. In this sec- involves calculating the similarity matrix for each view, normalizing
tion, we introduce a matrix-free algorithm for spectral embedding that them and subsequently summing them. The resulting matrix is then
avoids calculating the similarity matrix. This approach is specifically used to compute the spectral embedding. This straightforward strategy
designed for cosine similarity. The cosine similarity between two vec- has been effective in revealing clusters in prior research48,49. However,
t u o s r in s g A m an a d tr B ix is o g p i e v r e a n t b io y n S s c , ( w A e , B fi ) r = st r∥Ae A ∥s ⋅ ∥ B cBa∥l . e T t o h e e x n p o re n s n s e t g h a e t c iv o e s c in o e u s n im t m il a a t r r it ix y i w t h n i e c c h e i s s s c it o a m te p s u th ta e t c io o n m a p ll u y t d a e ti m on a n o d f i t n h g e . s H im er i e la , r w it e y p m re a s tr e i n x t f a o n r e a a lg c o h r v it ie h w m ,
C to obtain a new matrix X, such that the rows of X have unit L norm. that is efficient in both time and space for computing this embedding.
2
Consequently, the cosine similarity matrix between rows of X can be We first normalize each X i such that the rows of X i have unit L 2
represented as XXT. norm. We then define X as the horizontally concatenated view of the
In traditional spectral clustering algorithms, it is necessary to set sequence of matrices,
the diagonals of the similarity matrix to zero58. This can be accom-
p
re
li
s
s
u
h
l
e
ti
d
n g
b y
in
s u
th
b
e
tr
f
a
in
ct
a
i
l
n
s
g
im
th
i
e
la
i
r
d
it
e
y
n
m
tit
a
y
t r
m
ix
a
W
tri
=
x f
X
r
X
o
T
m
−
t
I
h
.
e
T
s
h
i
e
m
d
il
e
a
g
r
r
it
e
y
e
m
m
a
a
t
t
r
r
i
i
x
x
, X=(
√‖W
λ
1
1
‖F
X1
√‖W
λ
2
2
‖F
X2 …
√‖W
λ
k
k
‖F
Xk)
can then be calculated as D=diag((XXT−I)1)=diag(X(XT1)−1). The
normalized similarity matrix, denoted as W˜, can then be computed as where λ
k
is the user-defined weights measuring the relative importance
follows: of each view; Wk=XkXT
k
−I is the similarity matrix of the k-th view; ‖Wk‖
F
is the Frobenius norm of W. We can see that,
k
W˜ =D−1/2XXTD−1/2−D−1=X˜X˜T−D−1
where X˜=D−1/2X. It is important to note that X˜ has the same dimensions
XXT−∑
k ‖W
λ
k
k
‖F
I=∑
k ‖W
λ
k
k
‖F
(XkXT
k
−I)
a
ti
s
o
X
n
,
a
a
l
n
s
d
p e
if
c
X
tr
i
a
s
l
s
e
p
m
ar
b
s
e
e
d
,
d
X˜
i n
p
g
re
a
s
l
e
g
r
o
v
r
e
it
s
h
t
m
he
s
s
c
p
o
a
m
rs
p
it
u
y
t e
p a
W˜
tt
a
e
n
rn
d
o
s
f
e l
X
e
.
c
C
t
o
it
n
s
v
t
e
o
n
p
- =∑
k
λk‖W W
k
k
‖F
eigenvectors as the lower-dimensional embedding. Previous work has
attempted to compute the top eigenvectors of an approximation of W˜ Without loss of generality, we can assume ∑ λk =1. In practice,
to avoid the need for computing the full similarity matrix30. In other
k‖Wk‖F
this can be achieved by normalizing λ. The above equation can now be
studies10,11, the authors chose not to set the diagonals of the similarity k
written as,
matrix to zero. Consequently, the eigendecomposition of W˜ is equiva-
l
c
e
o
n
m
t
p
to
u t
t
e
h
d
e
e
s
f
i
f
n
ic
g
i
u
en
la
t
r
ly
v
.
a
H
l
o
u
w
e
e
d
v
e
e
c
r
o
, o
m
u
p
r b
o
e
s
n
it
c
io
h
n
m
(
a
S
r
V
ki
D
n
)
g
o
re
f
v
X˜
e
,
a
w
ls
h
th
ic
a
h
t s
c
e
a
t
n
ti
b
ng
e XXT−I=∑
k
λk‖W W
k
k
‖ F
the diagonal of W to zero is necessary as it substantially improves the
embedding quality. Therefore, the matrix W = XXT − I is a linear combination of the
Unlike previous work, we offer an exact solution to the problem. normalized similarity matrices of the individual views. To compute the
We apply the Lanczos algorithm25, an iterative method for computing spectral embedding of W, it suffices to apply the matrix-free spectral
the top eigenvectors of a symmetric matrix, to our problem without embedding method described above to the concatenated view X. This
ever calculating W˜. This requires computing the matrix–vector product algorithm is implemented in the ‘snapatac2.tl.multi_spectral’ function
between W˜ and v in each iteration, as follows: W˜v=X˜(X˜Tv)−D−1v, from the SnapATAC2 package. The pseudocode for this algorithm is
where v is the current solution to the eigenvalue problem and is shown in Extended Data Fig. 10d.
Nature Methods
Article https://doi.org/10.1038/s41592-023-02139-9
Eigenvector selection in spectral embedding Typically, we fixed the dimensionality at 30, as it effectively captures
Not all eigenvectors produced by spectral embedding are informative most of the data variance. For methods that require fine-tuning of
and relevant for clustering tasks. Selecting appropriate eigenvectors is dimensionality or component count, like cisTopic, we followed the
essential, as using uninformative or irrelevant ones can lead to subop- recommendations provided in their respective publications to ascer-
timal clustering results. We found that the widely used elbow method tain the optimal dimensionality. A comprehensive elucidation on the
for determining the number of eigenvectors is not consistently reliable operational specifics of each method is provided below.
in practice. To identify relevant eigenvectors, we propose a simple
heuristic based on the eigenvalues of the graph Laplacian matrix. In ArchR. ArchR (version 1.0.1) is an R package for analyzing scATAC-seq
this approach, each eigenvector is weighted by the square root of its data. To generate the lower-dimensional embedding of the data, we
corresponding eigenvalue, and these weighted eigenvectors are then used the ‘ArchR:::.computeLSI’ function with the default parameters.
used for further analyses. The output dimension was set to 30. After performing the SVD, ArchR
scales the singular vectors by the singular values. As a result, com-
Overview of the benchmarking process ponent selection is not necessary, so we used all 30 dimensions for
In this study, we conducted a thorough evaluation of SnapATAC2, downstream analysis. Note that ArchR includes three variants of the
focusing on its dimensionality reduction capabilities across a range LSI algorithm: ‘TF-logIDF’, ‘log(TF-IDF)’ and ‘logTF-logIDF’. Although
of datasets, spanning scATAC-seq, scHi-C, scRNA-seq and multiome we have benchmarked all three variants, we only report the results
data. Moreover, we scrutinized the performance of SnapATAC2’s batch for the ‘log(TF-IDF)’ variant in the main text as it is the default setting.
effect correction features. The subsequent sections offer an in-depth
overview of the datasets utilized, the benchmarking procedures used Signac. Signac (version 1.6) is an R package for analyzing scATAC-seq
and the metrics applied for this comprehensive assessment. data. To generate the lower-dimensional embedding of the data, we
used the ‘Signac:::RunTFIDF.default’ and ‘Signac:::RunSVD.default’
Preparing scATAC-seq benchmarking datasets functions with the default parameters. The initial output dimension
Simulated scATAC-seq datasets. We obtained eight simulated was set to 30 and we used the elbow method to select the number of
scATAC-seq datasets from a prior study22, presented as cell-by-peak components retained for downstream analysis. Note Signac includes
matrices. These datasets were derived from well-annotated bulk four variants of the LSI algorithm: ‘IDF’, ‘TF-logIDF’, ‘log(TF-IDF)’ and
ATAC-seq datasets from bone marrow, with variations in noise levels ‘logTF-logIDF’. Although we have benchmarked all four variants, we
and read coverages. Specifically, a noise parameter, ranging from 0 to only report the results for the ‘log(TF-IDF)’ variant in the main text as
1, represented the fraction of reads appearing in a random peak from it is the default setting.
a sorted population, which was then used to produce the peak-by-cell
matrices. The remaining reads were allocated based on the bulk sam- EpiScanpy. EpiScanpy (version 0.4.0) is a Python package for analyzing
ple’s distribution. A matrix with a noise level of 0 perfectly retained scATAC-seq data. We first normalized the count matrix using ‘epis-
the cell-type specificity of the reads within peaks, while a matrix with canpy.pp.normalize_per_cell’ and ‘episcanpy.pp.log1p’ functions with
a noise level of 1 lacked any distinguishing information about cell types the default parameters. We then used the ‘episcanpy.pp.pca’ function
based on the reads within peaks. The simulated datasets featured three to generate the lower-dimensional embedding of the data. The initial
noise levels: none (0), moderate (0.2) and high (0.4). The clean dataset output dimension was set to 30 and we used the elbow method to
(zero noise level) also spanned five read coverages per cell: 5,000, select the number of components retained for downstream analysis.
2,500, 1,000, 500 and 250 fragments. The datasets utilized predefined
peak regions sourced from bulk ATAC-seq data. SCALE. SCALE (version 1.1.2) is a Python package for performing dimen-
sionality reduction on scATAC-seq data. We used the command ‘SCALE.
Curated scATAC-seq datasets. For further benchmarking analysis, we py’ with following parameters to generate the lower-dimensional
curated ten additional scATAC-seq datasets (Table 1). For each dataset, embedding: ‘--min_peaks 0 --min_cells 0 -i 30’. Additionally, as we knew
we assembled a cell-by-peak count matrix using the annotated cells the number of cell types in the benchmarking datasets, we set the ‘-k’
and peaks specified in the respective publications. We also sourced parameter (the number of clusters) to the true number of cell types.
cell labels from these publications. In preprocessing all the datasets,
we eliminated peaks that were absent in all cells. While we generally PeakVI. PeakVI (version 0.19.0) is a Python package for performing
retained all cells from the datasets, exceptions were made for the dimensionality reduction on scATAC-seq data. We used the ‘scvi.model.
GSE194122 and Zemke_human datasets. In these cases, the data were PEAKVI’ function to create a model with the default parameters. The
generated using multiple donors or protocols, leading to pronounced dimensionality of the latent variable was set to 30.
batch effects. To ensure that our evaluation was not skewed by these
batch effects, we opted to use only a subset of cells from these two scBasset. scBasset (GitHub: c15bec3a73fa1e04822db723338d-
datasets, specifically those originating from a consistent donor or 234ca9d384ce) is a Python package for performing dimensionality
protocol. It is worth noting that the full versions of these two datasets reduction on scATAC-seq data. We followed the instructions in the
were used in evaluating batch effect correction methodologies. scBasset GitHub repository to generate the lower-dimensional embed-
ding of the data. The dimensionality of the latent variable was set to 30.
Comparing dimensionality reduction methods on scATAC-seq
data pycisTopic. pycisTopic (GitHub: 242c2a47aad475250f8ab-
We utilized the cell-by-peak count matrices from the aforementioned b2469a0e36085d6e460) is a Python package for analyzing scATAC-seq
benchmarking datasets to assess various dimensionality reduction data. To generate the lower-dimensional embedding of the data, we
techniques. Unlike other tasks, we did not implement feature/peak first created a model using the ‘create_cistopic_object’ function with
selection or scaling for the ATAC tasks, as these steps are not customary the default parameters. We then used ‘run_cgs_models’ to train the
in an ATAC workflow43. We executed the nine selected dimensionality model with the following parameters: ‘n_iter = 300, alpha = 50, alpha_
reduction methods using their default settings, as specified in relevant by_topic = true, eta = 0.1, eta_by_topic = false’. We trained six models
tutorials or their associated research methodologies. The resulting with different dimensions of the latent variable: 5, 10, 15, 20, 25 and 30.
lower-dimensional cell embeddings were then assessed using four We then used the ‘evaluate_models’ function to select the best model
distinct metrics, further elaborated upon in ‘Benchmarking metrics’. for downstream analysis.
Nature Methods
Article https://doi.org/10.1038/s41592-023-02139-9
SnapATAC. SnapATAC (version 1.0) is an R package for analyzing dimensionality reduction methods can generate embeddings with
scATAC-seq data. For datasets with less than 20,000 cells, we used the varying numbers of dimensions, which can, in turn, impact the sil-
‘SnapATAC::runDiffusionMaps’ function with the default parameters houette width. Additionally, the ‘curse of dimensionality’ poses chal-
to generate the lower-dimensional embedding of the data. For datasets lenges, as distance metrics become less reliable in higher-dimensional
with more than 20,000 cells, running ‘SnapATAC::runDiffusionMaps’ spaces. Moreover, silhouette width is most effective for evaluating
on the full dataset requires a large amount of memory. In this case, we convex clusters, but the shape of the clusters can vary based on the
applied ‘SnapATAC::runDiffusionMaps’ on a subset of the data and then dimensionality reduction method used. To mitigate these issues,
used the ‘SnapATAC::runDiffusionMapsExtension’ function to gener- we standardized the dimensionality of all embeddings by applying
ate the lower-dimensional embedding of the full dataset. The output the UMAP algorithm to reduce them to three dimensions. This not
dimension was set to 30. We used the ‘SnapATAC:::weightDimReduct’ only facilitates a more equitable comparison but also enhances the
to scale eigenvectors by their corresponding eigenvalues. The scaled reliability of the silhouette width as a metric. Using the scib-metrics
eigenvectors were then used for downstream analysis. software (version 0.3.3), we calculated two variants of the ASW to
evaluate both cell-type separation (cell-type ASW) and batch mixing
SnapATAC2. SnapATAC2 (version 2.3.1) is a Python package developed (batch ASW).
in this study. We used the ‘snapatac2.tl.spectral’ function to generate
the lower-dimensional embedding of the data. The output dimension Graph LISI. The graph LISI metric extends the LISI by incorporating
was set to 30. integrated graph structures to measure both batch mixing (graph
iLISI) and cell-type separation (graph cLISI). LISI scores were computed
Benchmarking metrics using neighborhood lists from integrated k-NN graphs. The metric
To assess the quality of cell embeddings produced by various meth- leverages the inverse Simpson’s index to evaluate the diversity of
ods, we used a range of metrics: ARI, AMI, cell-type ASW and graph cells within a neighborhood. We used the scIB (v0.3.3) package for
cLISI43. For batch effect removal analysis specifically, additional these calculations.
metrics were included: batch ASW, k-nearest-neighbor (k-NN) graph
connectivity43, graph iLISI43, k-NN batch effect test (kBET)43 and kBET. The kBET algorithm tests if the label composition within a
isolated label ASW. k-nearest neighborhood reflects the overall label composition. We
To aggregate these individual metrics into a unified score, we used k-NN graphs with k set at 50 for this purpose. The test was applied
first normalized each metric using min–max scaling, which involved to a random subset of cells, and the rejection rate across all tested
subtracting the minimum value from each metric and then dividing it neighborhoods was summarized. kBET scores were computed using
by the range. We then calculated the mean of these scaled metrics to the scIB (v0.3.3) package.
derive an overall performance score for each method.
In the context of batch correction benchmarks, we categorized Isolated label ASW. This metric specifically assesses how well data
the metrics into two distinct groups: bio-conservation metrics and integration methods handle cell identity labels that are less com-
batch correction metrics. The bio-conservation group consists of ARI, monly shared across batches. It calculates the ASW between isolated
AMI, ASW, graph cLISI and isolated label ASW. In contrast, the batch and non-isolated labels within the cell embedding, scaling the score
correction group included batch ASW, k-NN graph connectivity, graph between 0 and 1. The final score is the mean isolated score for all such
iLISI and kBET. To calculate the overall performance score, denoted as labels, providing an evaluation of how well these less common labels
S , for each method, we took a weighted mean of the batch correc- are separated from other cell identities. Isolated label ASW calculations
overall
tion score, S , and the bio-conservation score, S , according to the were performed using the scIB (v0.3.3) package.
batch bio
equation: Soverall=0.4×Sbatch+0.6×Sbio .
Scalability of scATAC-seq dimension reduction methods
ARI. The ARI metric quantifies the degree of similarity between two To establish benchmarking datasets, we initially drew random cell
different clusterings, accounting for both correct overlaps and disa- samples from the Zemke_human dataset in varying numbers, ranging
greements. We generated a k-NN graph from cell embeddings with k from 5,000 to 200,000 cells. From these samples, we constructed
set at 50. Using this graph, we applied the Leiden algorithm34 to obtain cell-by-bin matrices with a bin size of 500 base pairs, omitting any bins
cell clusters. Given that the number of cell types in our benchmark- that were devoid of data across all cells. Subsequently, we applied vari-
ing datasets is known, we fine-tuned the Leiden algorithm’s resolu- ous dimensionality reduction methods to these matrices using their
tion parameter between 0.1 and 3.0 in increments of 0.1 to match the default parameters and recorded both the runtimes and peak memory
actual number of clusters. Subsequently, we used ARI to evaluate the usages, plotting these metrics against the cell count. The benchmarks
congruence between these Leiden clusters and the known cell-type were conducted on a Linux server utilizing four cores of a 2.6 GHz Intel
labels. An ARI score of 0 indicates random labeling, while 1 represents Xeon Platinum 8358 CPU.
a perfect match. We used the scikit-learn (v1.3.0) implementation for For neural network-based techniques like PeakVI, scBasset and
ARI calculations. SCALE, we conducted the experiments on an A100 GPU equipped
with 40 GB of memory. Notably, the memory usage of these methods
AMI. Like ARI, AMI also measures the similarity between two clusterings is influenced more by the number of features than by the number of
but is more effective when the reference clustering is imbalanced or cells, due to the use of mini-batch training. When the feature count
contains small clusters60. The procedure for generating clusters and exceeded 500,000, we encountered memory limitations on the GPU.
comparing them with cell-type labels mirrors that of ARI. The AMI To mitigate this, we capped the feature set at 500,000 and opted not to
scores range from 0 (random labeling) to 1 (perfect match) and were report memory usage metrics for these methods, as they aren’t directly
calculated using the scikit-learn (v1.3.0) package. comparable to other techniques. For benchmarking, we used a consist-
ent set of 10 epochs to gauge the average runtime per epoch. We then
ASW. The ASW metric quantifies the degree of separation between extrapolated this to calculate the total runtime for a typical 50 epochs,
clusters by averaging the silhouette widths across all cells. ASW val- which is generally the minimum required for model convergence. It’s
ues range from −1 to 1, with higher scores signaling better-defined important to clarify that the runtimes reported for these neural net-
clusters. However, the effectiveness of the ASW metric can be influ- work methods exclude data preprocessing time, thus representing a
enced by the dimensionality and topology of the data. Different lower limit on the actual time needed.
Nature Methods
Article https://doi.org/10.1038/s41592-023-02139-9
Preparing scHi-C benchmarking datasets the data, we first applied the ‘scanpy.pp.normalize_total’ and ‘scanpy.
We obtained preprocessed 4DN scHi-C datasets8 and a single-nucleus pp.log1p’ functions to preprocess the data. The data were then
methyl-3C sequencing dataset44 from a prior study18, including cell-level scaled using ‘scanpy.pp.scale’ with ‘max_value = 10’ and inputed to
contact matrices and cell labels. These datasets were already format- the ‘scanpy.tl.pca’ function to get lower-dimensional embedding.
ted for compatibility with Higashi. Additionally, we converted these The initial output dimension was set to 30 and we used the elbow
datasets to formats suitable for input into scHiCluster and SnapATAC2. method to select the number of components retained for downstream
analysis.
Comparing dimensionality reduction methods on scHi-C data
We used the prepared benchmarking datasets to evaluate various scvi-tools. scvi-tools (version 1.0.3) is a Python package for analyzing
dimensionality reduction techniques. This benchmarking approach is scRNA-seq data. We followed the instructions in the scvi-tools GitHub
analogous to the one used for scATAC-seq, as described earlier. Detailed repository to generate the lower-dimensional embedding of the data,
operational specifics for each method are provided below. setting the dimensionality of the latent variable to 30.
SnapATAC2. We began by converting each cell’s square region-by- Preparing single-cell multiome benchmarking datasets
region contact map into a vector. These vectors were then used to We obtained a paired ATAC and gene expression dataset of cryopre-
construct a sparse matrix representing all cells’ contact maps. We used served human PBMCs from the 10x Genomics website. Cell labels
the ‘snapatac2.pp.select_features’ function to identify the top 500,000 were annotated based on a previously published single-cell atlas
features based on total counts. The method showed little sensitivity of human PBMCs4. We used the ‘Seurat::FindTransferAnchors’ and
to the number of features selected. Finally, we used the ‘snapatac2. ‘Seurat::MapQuery’ functions to map cell labels from the reference
tl.spectral’ function to create a lower-dimensional embedding, setting dataset to the 10x dataset, using ‘spca’ as the reference reduction
the cell embedding dimension to 30. method and ‘wnn.umap’ as the reduction model. Cells were then filtered
based on a minimum threshold of 200 detected genes, 5,000 ATAC frag-
Higashi. Higashi (GitHub: 392da1d9cd7208aef0e8f6f7b1192a- ments and a TSS enrichment score of at least 10. Doublets were removed
5aa0265ed2) is a Python package for analyzing scHi-C data. We fol- using ‘snapatac2.pp.scrublet’. Cell-by-gene and cell-by-bin matrices
lowed the instructions in the Higashi GitHub repository to generate were constructed for scRNA-seq and scATAC-seq data, respectively.
the lower-dimensional embedding of the data. The dimensionality of The bin size was set to 500 bp, and the top 500,000 most accessible
the cell embeddings was set to 30. bins were selected using the ‘snapatac2.pp.select_features’ function.
The finalized dataset contained 9,181 cells.
scHiCluster. scHiCluster (version 1.3.2) is a Python package for analyz- As an additional benchmarking dataset, we downloaded a
ing scHi-C data. We followed the instructions in the scHiCluster GitHub Paired-Tag dataset from a study on the mouse frontal cortex53, which
repository to generate the lower-dimensional embedding of the data. simultaneously measures H3K27me3 histone modification and gene
The dimensionality of the cell embeddings was set to 30. expression at single-cell resolution. We obtained the cell-by-gene
matrix from the publication and created the cell-by-bin matrix using
SCANPY (PCA). For the SCANPY (PCA) method, we initially trans- the fragment files provided by the authors, with a bin size of 5 kb as
formed each cell’s square contact map into a vector and then con- recommended in the original paper. The top 100,000 most accessible
structed a sparse matrix, just like with SnapATAC2. The top 500,000 bins were selected using the ‘snapatac2.pp.select_features’ function,
features with the highest total counts were selected. We used the and cell labels were sourced from the original paper. The final dataset
‘scanpy.pp.normalize_total’ and ‘scanpy.pp.log1p’ functions for data in this case comprised 10,180 cells.
preprocessing. Lastly, we applied the ‘scanpy.tl.pca’ function to gener-
ate the lower-dimensional embedding. The initial output dimension Comparing cell embedding methods on single-cell multiome
was set to 30 and we used the elbow method to select the number of data
components retained for downstream analysis. We used the two curated single-cell multiome datasets to evaluate
four methods designed for joint cell embedding across multiple data
Preparing scRNA-seq benchmarking datasets modalities. For gene expression data, the top 3,000 highly variable
We sourced five scRNA-seq datasets from a prior benchmarking study35. genes were selected, while all features were included for ATAC or his-
These datasets contain cell-by-gene count matrices and cell labels, and tone modification data. Due to memory limitations, MOFA+ used a
had already undergone preprocessing to eliminate low-quality cells, maximum of 200,000 features for ATAC data. The accuracy of these
dimensionality reduction methods was assessed using four distinct
Comparing dimensionality reduction methods on scRNA-seq evaluation metrics, which are elaborated in ‘Benchmarking metrics’.
data A comprehensive elucidation on the operational specifics of each
We utilized the curated benchmarking datasets to assess a range of method is provided below.
dimensionality reduction techniques. The approach mirrors the one
taken for scATAC-seq benchmarking, with a notable exception: before SnapATAC2. For normalization of gene expression data, we used the
applying dimensionality reduction methods, we used the ‘scanpy. ‘scanpy.pp.normalize_total’ and ‘scanpy.pp.log1p’ functions. Subse-
pp.highly_variable_genes’ function to identify the top 5,000 highly quently, the ‘snapatac2.tl.multi_spectral’ function was applied to jointly
variable genes (‘n_top_genes = 5,000’). Below are detailed explanations reduce the dimensionality of both the gene expression and ATAC data,
of the methods used. setting the output dimensionality to 30.
SnapATAC2. To begin, we normalized the data using the ‘scanpy.pp. MIRA. MIRA (version 2.1.0) is a Python package focused on analyzing
normalize_total’ and ‘scanpy.pp.log1p’ functions. Following this, the dynamic gene regulation processes in single-cell multi-omics datasets.
‘snapatac2.tl.spectral’ function was utilized to create a lower-dimensional To generate a joint embedding, we initially conducted topic mod-
representation of the dataset. The cell embedding dimension was set to 30. eling on each modality using ‘mira.topics.make_model’ and selected
the number of topics via ‘mira.topics.gradient_tune’ and the elbow
SCANPY. SCANPY (version 1.9.5) is a Python package for analyzing method. The joint representation was then obtained using ‘mira.utils.
scRNA-seq data. To generate the lower-dimensional embedding of make_joint_representation’.
Nature Methods
