---
source_path: /mnt/c/Users/Administrator/Zotero/storage/NHBQQFAU/s41592-022-01562-8.pdf
ingested: 2026-04-23
sha256: 57600c267c5e4f6c
---

Articles
https://doi.org/10.1038/s41592-022-01562-8
scBasset: sequence-based modeling of single-cell
ATAC-seq using convolutional neural networks
Han Yuan ✉ and David R. Kelley ✉
Single-cell assay for transposase-accessible chromatin using sequencing (scATAC) shows great promise for studying cellular
heterogeneity in epigenetic landscapes, but there remain important challenges in the analysis of scATAC data due to the inher-
ent high dimensionality and sparsity. Here we introduce scBasset, a sequence-based convolutional neural network method to
model scATAC data. We show that by leveraging the DNA sequence information underlying accessibility peaks and the expres-
siveness of a neural network model, scBasset achieves state-of-the-art performance across a variety of tasks on scATAC and
single-cell multiome datasets, including cell clustering, scATAC profile denoising, data integration across assays and transcrip-
tion factor activity inference.
E
pigenetic landscapes at a single-cell resolution are revealed by Here, we extend the Basset deep CNN architecture to pre-
scATAC1. The assay has been successfully applied to identify dict single-cell chromatin accessibility from a DNA sequence. In
cell types and their specific regulatory elements, reveal cellular this arrangement, the multiple tasks represent single cells and the
heterogeneity, map disease-associated distal elements and recon- model’s final layer learns cell embeddings. We show that these cell
struct differentiation trajectories2–4. embeddings outperform state-of-the-art methods for clustering
However, there are still substantial challenges in the analysis of and cell-state representation in multiome data. By making use of
scATAC data, due to the inherent high dimensionality of acces- sequence information in a deep learning framework, we also achieve
sible peaks and sparsity of sequencing reads per cell5,6. Multiple improved scATAC denoising, integration with single-cell RNA-seq
approaches have been proposed to address these challenges, which (scRNA) and TF activity inference over alternative methods.
can be broadly categorized into two main classes: sequence-free and
sequence-dependent methods. Starting from a sparse peak-by-cell Results
matrix generated through aggregation of reads and peak call- scBasset predicts single-cell chromatin accessibility on held-out
ing, most methods represent these annotated peaks as genomic peaks. scBasset is a deep CNN to predict chromatin accessibility
coordinates and ignore the underlying DNA sequences. Principal from sequence. CNNs have demonstrated state-of-the-art perfor-
component analysis (PCA) and latent semantic indexing perform mance for predicting epigenetic profiles in bulk data and have been
a linear transformation of the peak-by-cell matrix to project cells successfully used for genetic variant effect prediction and TF motif
to a low-dimensional space4,7. SCALE and cisTopic model the data grammar inference11–14. Here, we move the focus away from maxi-
generation using Latent Dirichlet Allocation or a variational auto- mizing accuracy on held-out sequences and view the model as a
encoder5,8. These sequence-free methods are able to detect biologi- representation learning machine. When trained on multiple tasks,
cally meaningful covariance to effectively represent and cluster or the final layer of these models involves a sequence embedded by the
classify cells; however, they ignore sequence information and rely convolutional layers and a linear transformation to predict the data
on post hoc motif-matching tools to relate accessibility to transcrip- in each separate task (Fig. 1a). The linear transformation matrix
tion factors (TFs). In contrast, sequence-dependent methods such comprises a vector representation of each task (each single cell),
as chromVAR and BROCKMAN represent peaks by their TF motif which specifies how to make use of each of the sequence-embedding
or k-mer content and aggregate these features across peaks or other latent variables to predict cell-specific accessibility. In a simple ideal
regions of interest to learn cell representations9,10. While chromVAR scenario, one can imagine each latent variable representing vari-
directly associates peaks to TFs, emphasizing interpretability, it ous regulatory factors such as TF binding or nucleotide composi-
tends to perform worse at learning cell representations, potentially tion and the final transformation specifying how much each cell
due to the loss of information from its simple implicit model relat- depends on that factor. We propose that these single-cell vectors
ing sequence to accessibility through position weight matrices6. serve as representations of the cells for downstream tasks such as
We propose a more expressive sequence-dependent model for visualization and clustering.
scATAC based on deep convolutional neural networks (CNNs) We recommend that users first apply standard processing tech-
applied to DNA sequences. In these models, the initial convolution niques, such as the 10x CellRanger scATAC pipeline, to bring the
layer learns TF motifs and other sequence factors. Subsequent lay- raw data to a peak-by-cell binary count matrix. scBasset takes
ers compute nonlinear combinations of these features, to produce as input a 1,344-bp DNA sequence from each peak’s center and
an explicit embedding of the sequence. When trained on multiple one-hot encodes it as a 4 × 1,344 matrix. The input DNA sequence
tasks, the final linear layer transforms the sequence embedding goes through eight convolution blocks, where each block is com-
to predict accessibility for each task (sequencing experiments). Its posed of one-dimensional (1D) convolution, batch normalization,
parameters implicitly embed the multiple tasks based on how they max pooling and Gaussian error linear unit (GELU) activation
make use of the latent variables in the sequence embedding. layers. Unlike most previous architectures, we follow these by a
Calico Life Sciences, South San Francisco, CA, USA. ✉e-mail: yuanh@calicolabs.com; drk@calicolabs.com
1088 NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods
NATurE METHoDS Articles
a
448
b
bottleneck layer (with size fixed to 32 in all analyses) intended to cell (referred to as ‘per cell’). To evaluate cell-type specificity, we also
learn a low-dimensional representation of the peak via the layer computed auROC and auPR across cells for each peak (referred to
output and the cells via the parameters of the following layer. as ‘per peak’) (Supplementary Fig. 1). scBasset achieved compelling
Finally, a dense linear transformation connects the bottleneck accuracy levels that indicate successful learning: auROC of 0.762
sequence embeddings to predict binary accessibility in each cell per cell and 0.730 per peak for the Buenrostro2018 dataset (Fig. 1b),
(Fig. 1a). We apply the standard binary cross-entropy loss func- 0.640 per cell and 0.662 per peak for the 10x multiome PBMCs and
tion and optimize model parameters with stochastic gradient 0.701 per cell and 0.734 per peak for the 10x multiome mouse brain
descent (Methods). dataset. Randomly shuffling the active peaks within each cell led to
To benchmark our approach, we applied scBasset to three pub- mean 0.5 auROC per cell and decreased auROC per peak (although
lic datasets: scATAC of FACS-sorted hematopoietic differentiation >0.5 due to the influence of different sequencing depths across cells;
(referred to as Buenrostro2018) with 2,000 cells15, 10x Multiome Supplementary Fig. 2).
RNA + ATAC peripheral blood mononuclear cells (PBMCs) with Although these statistics are slightly below the 0.75–0.95 range
3,000 cells and 10x Multiome RNA + ATAC mouse brain with achieved for bulk DNase samples in the original Basset publication,
5,000 cells. The first dataset provides ground-truth cell type labels this is inevitable due to the substantially increased measurement
from flow cytometry. We consider the multiome datasets to be a noise due to sparse sequencing for the single cell assay. In support of
valuable resource to validate scATAC methods as they provide this claim, we observed that in the 10x multiome PBMC and mouse
independent measurements of gene expression and chromatin brain datasets, peaks with very high read coverage are easier to pre-
accessibility in the same cells. Although these assays deliver dif- dict (Supplementary Fig. 1). Given that ubiquitous accessible peaks
ferent data, previous work demonstrates that they have substantial are known to exist, these peaks are likely truly accessible in all cells
mutual information16,17. and represent a rough upper bound on the achievable accuracy. To
First, we asked how well scBasset can predict accessibility across further assess the influence of sequencing depth, we downsampled
cells for held-out peak sequences to ensure that the model has learned the 10x multiome PBMCs at various levels and trained scBasset. As
a meaningful relationship between DNA sequence and accessibility expected, validation auROC and cell-embedding metrics decrease
despite the sparse noisy labels. For held-out peaks, we computed the with decreasing depth, but scBasset performance is still better than
area under the receiver operating characteristic curve (auROC) and random even when the dataset contains only 1% nonzero entries
area under the precision recall curve (auPR) across peaks for each (Supplementary Fig. 3).
882 323
224
363
112
704
56
654
28
215
14
652
7
23
scATAC peak atlas
Peak t Predicted Observed
Convolution tower accessibility accessibility
1,344
bp
1
Loss ...
Conv filters Number of cells
32
Peak embedding
Number
of cells
c
HSC
MPP
LMPP CMP
CLP pDC GMP MEP
tSNE1
2ENSt
Final layer weights
Input Cell embedding Output
Final layer weights used for
visualization/clustering
14
CLP
12 CMP
GMP 10 HSC
LMPP 8 MEP
MPP
UNK
6
Mono
0.5 0.6 0.7 0.8 0.9 pDC
auROC per cell
)tnuoc
kaep(
gol 2
Mean auROC = 0.762
10
9
8
7
6
5
0.5 0.6 0.7 0.8 0.9
auROC per peak
)tnuoc
llec(
gol 2
Mean auROC = 0.730
Fig. 1 | scBasset architecture. a, scbasset is a deep CNN to predict single-cell chromatin accessibility from the DNA sequence underlying peak calls. the
input to the model is a 1,344-bp DNA sequence from each peak’s center and the output is accessibility per cell (corresponding to one row of the peak × cell
matrix). Conv, convolution. b, scbasset prediction performance on held-out peaks evaluated by aurOC per cell (left) and aurOC per peak (right) for the
buenrostro2018 dataset. c, t-SNe visualization of cell embeddings learned by scbasset as the weights of the final dense layer, colored by cell type (left).
Hematopoietic stem cell differentiation lineage diagram in the buenrostro2018 study (right). the cell type labels refer to hematopoietic stem cell (HSC),
multipotent progenitor (mpp), lymphoid primed mpp (Lmpp), common lymphoid progenitor (CLp), plasmacytoid dendritic cell (pDC), common myeloid
progenitor (Cmp), granulocyte macrophage progenitor (Gmp), megakaryocyte-erythroid progenitor (mep) cell, monocyte (mono) and unkonwn (UNK).
Source data for this figure are provided.
NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods 1089
Articles NATurE METHoDS
1.0
0.8
0.6
0.4
0.2
0
chro m V A Rk- c m hr e o S r m C V A A L R E _ motif P C A sc D E C Arch R pe s a n k a V p I AT A ci C sTopic Cice s r c o Basset
scBasset final layer learns cell representations. We propose that multipotent progenitor (MPP) cells are most difficult to distin-
the weight matrix learned in the final dense layer, which connects guish (Supplementary Fig. 5). Visualizing the scATAC cell embed-
the bottleneck to the predictions, be used as a low-dimensional rep- dings generated by different approaches by t-SNE, we observed that
resentation of the single cells. One requirement for an effective cell chromVAR, PCA and scDEC struggle to distinguish common lym-
representation is removal of the influence of sequencing depth. Thus, phoid progenitor (CLP) cells from lymphoid primed MPP (LMPP)
we first verified that the intercept vector in the model’s final layer cells, whereas scDEC and SCALE struggle to distinguish mega-
almost perfectly correlates with cell sequencing depth for all datasets karyocyte–erythroid progenitor (MEP) cells from common myeloid
(Supplementary Fig. 4), suggesting that depth has been normalized progenitor (CMP) cells (Extended Data Fig. 1).
out from the representations. Next, we compared the cell representa- For the multiome PBMC and mouse brain datasets, we com-
tions learned by scBasset with other methods both qualitatively and puted an analog to the label scores for cell embeddings. As the
quantitatively. For the Buenrostro2018 dataset, we visualized the cell ground-truth cell types for the multiome datasets are unknown, we
embeddings in two-dimensions (2D) using t-distributed stochastic used cluster identifiers from scRNA-seq Leiden clustering as cell
neighbor embedding (t-SNE) (Fig. 1c) and observed that cells of the type labels. Again, scBasset outperforms the competitors by this
same type clustered together in the embedding space. metric across a range of neighborhoods using label score or con-
Following previous work, we quantified the correctness of cell ventional clustering metrics (Fig. 2c,e and Supplementary Fig. 6).
embeddings in Buenrostro2018 by comparing Louvain clustering For these multiome datasets, we also computed a ‘neighbor score’,
results with ground-truth cell-type labels using the adjusted rand in which we built independent nearest-neighbor graphs from the
index (ARI), adjusted mutual information (AMI) and homoge- scRNA and scATAC and asked what percentage of each cell’s neigh-
neity6 or by directly evaluating the distance between cells of the bors are shared between the two graphs. scBasset outperforms the
same label by cell type average silhouette width (ASW)18. scBas- competitors on both multiome PBMC and multiome mouse brain
set outperforms the other methods across these metrics (Fig. 2a). datasets when evaluated with neighbor scores across a range of
As Louvain clustering depends on hyperparameter choice and neighborhoods (Fig. 2d,f). We annotated multiome PBMC cells
initialization, we proposed an alternative cluster-free method for based on expression of marker genes (Methods) and visualized the
evaluating cell embeddings. We computed a ‘label score’ by build- cell embeddings from different methods using Uniform Manifold
ing a nearest-neighbor graph based on cell embeddings and asked Approximation and Projection (UMAP; Extended Data Fig. 2). We
what percentage of each cell’s neighbors share its same label. For observed that chromVAR, cisTopic, scDEC and peakVI struggle to
each embedding method, we computed label scores across a range distinguish FCGR3A+ monocytes from CD14+ monocytes, whereas
of neighborhoods and observed that scBasset consistently outper- scBasset clearly separates the two.
forms the competitors at learning cell representations that embed
cells of the same type near each other (Fig. 2b). We also evalu- Batch-conditioned scBasset corrects cell embeddings for batch.
ated label scores for each cell type individually and observed that In the Buenrostro2018 dataset, hematopoietic stem cells (HSCs)
plasmacytoid dendritic cells (pDCs) are learned best, whereas cluster into two populations, regardless of which cell-embedding
scirteM
1.0
ARI
Cell type ASW 0.8
AMI
Homogeneity 0.6
0.4
0.2
0
chro m c V h A ro R m k- V m A e R r _ moti s f c s D n E a C p AT A C S C AL E P C A peak V C I ice c ro isTopic Arc s h c R Basset
scirteM
1.0
0.8
0.6
0.4
0.2
0
chro m c V h A ro R m k- V m A e R r _ moti s f c D E C S C AL E s P n C ap A AT A C peak c V is I Topic Cicero Arc s h c R Basset
scirteM
a c e
ARI ARI
Cell type ASW Cell type ASW
AMI AMI
Homogeneity Homogeneity
b d f
1.0
0.8
0.6
0.4
0.2
0
chro m c V h A ro R m _ V m A o R tif k- me S r C AL E sc D E C P C A peak V A I rc c h i R sT s o n p a ic p AT A C Cice s r c o Basset
serocs
lebaL
10 neighbors
50 neighbors 100 neighbors 0.3
0.2
0.1
0
chro m c V h A ro R m k- V m A e R r _ s m n o a t p if AT A C sc D E C peak c V is I Topi S c C AL E P C A Arch R Cice s r c o Basset
serocs
robhgieN
10× multiome PBMC 0.4
0.3
0.2
0.1
0
chro m c V h A ro R m _ V m A o R tif k- me s r c s D n E a C p AT A S C C AL E P C A peak c V is I Topic Arch R Cice s r c o Basset
serocs
robhgieN
Buenrostro2018 10× multiome PBMC 10× multiome mouse brain
Buenrostro2018 10 neighbors 10 neighbors10× multiome mouse brain
50 neighbors 50 neighbors 100 neighbors 100 neighbors
Fig. 2 | scBasset cell representation performance. a, performance comparison of different cell-embedding methods evaluated by clustering metrics (ArI,
cell type ASW and AmI) on the buenrostro2018 dataset. b, performance comparison of different cell-embedding methods evaluated by label score—
the proportion of cells’ nearest neighbors that share its cell type label (methods)—on buenrostro2018 dataset. c, performance comparison of different
cell-embedding methods evaluated by clustering metrics on 10x multiome pbmC dataset. d, performance comparison of different cell-embedding methods
evaluated by neighbor score—the proportion of cells’ nearest neighbors that are also nearest neighbors in an independent scrNA analysis (methods)—on
10x multiome pbmC dataset. e, performance comparison of different cell-embedding methods evaluated by clustering metrics on 10x multiome mouse
brain dataset. f, performance comparison of different cell-embedding methods evaluated by neighbor score (methods) on 10x multiome mouse brain
dataset. Source data for this figure are provided.
1090 NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods
NATurE METHoDS Articles
scBasset
c
scBasset-BC 1.00
Cell type
CLP 0.75
CMP Batch scBasset-BC GMP BM0106
HSC BM0828 0.50 scDEC LMPP SCALE BM1077
MEP
BM1137
MPP 0.25
BM1214
UNK
Other
Mono
pDC 0
0 0.25 0.50 0.75 1.00
kBET
method we apply (Extended Data Fig. 1). As noted in previous stud- roughly the same number of cells in each batch, SCALE and scDEC
ies, this is caused by batch effects due to different donors (Fig. 3b)5,15. result in loss of biological structure, whereas peakVI and cisTopic
To correct for this, and batch effects more generally, we explored result in poor batch mixing. Harmony and scBasset-BC achieve the
modifications to the scBasset architecture. Specifically, after the best balance between batch mixing and preserving structure in the
bottleneck layer, we added a second fully connected layer to predict data (Fig. 3d and Extended Data Fig. 3). Harmony (PCA) achieved
the batch-specific contribution to accessibility (Methods; Extended slightly better mixing than scBasset-BC at the expense of worse cell
Data Fig. 3). We added the output of the batch layer and cell-specific type label maintenance. Harmony (scBasset) achieves the highest
layer before computing the final sigmoid. Intuitively, we expect the clustering and batch-mixing performance evaluated by label score
batch-specific variation will be captured in this path, whereas the and iLISI. Overall, Harmony and scBasset-BC performed similarly
original weight matrix will focus on the remainder of biologically for correcting batches from this balanced design.
relevant variation. By introducing an L2 normalization regulariza- Next, we trained scBasset-BC on the Buenrostro2018 dataset.
tion term on the cell-specific layer, we can control the information This dataset has an unbalanced batch design and represents a more
flow and degree of batch mixing. practical case for batch correction application. Again, we evaluated
We first implemented scBasset-BC to correct for batch effects in scBasset-BC performance as a function of L2 regularization and
a mixture of PBMC scATAC from 10x multiome and 10x next GEM observed that L2 = 1 × 10−8 achieved the best balance between mix-
chemistries (Fig. 3a). We quantified the mixing performance using inte- ing and conserving biological variation (Extended Data Fig. 4). On
gration local inverse Simpson’s index (iLISI) and k-nearest-neighbor these data, Harmony over-mixes and results in loss of biological vari-
batch-effect test (kBET) acceptance rate (Methods) and quantified the ation. cisTopic, peakVI, scDEC and SCALE all tend to under-correct
conservation of biological variation using label score19–21. We observed and maintain separation of batches. scBasset-BC achieves the
that training an scBasset-BC model with increasing L2 regularization best balance between mixing and preserving biological variability
results in better batch mixing at the expense of losing biological vari- (Extended Data Fig. 4 and Fig. 3e). The two HSC batches (BM0106
ation (Extended Data Fig. 3). The optimal balance was achieved at and BM0828) merge into one cluster. In addition, pDC cells from
L2 = 1 × 10−6 for the chemistry-mixed PBMC dataset. BM1137 and BM1214 batches previously fell into two distinct sub-
We comprehensively evaluated the batch correction perfor- clusters, but are mixed together after batch correction (Fig. 3b,c).
mance of scBasset compared to alternative methods such as cis-
Topic, Harmony, peakVI, SCALE and scDEC (Methods). Harmony scBasset denoises single cell accessibility profiles. Due to the spar-
is a general batch correction algorithm that can be implemented sity of scATAC, the binary accessibility indicator for any given cell
on top of any cell embeddings. We implemented two versions of and peak contains frequent false negatives, such that the data can-
Harmony, applying it to embeddings from (1) PCA or (2) scBas- not be studied with true single cell resolution and is usually aggre-
set. We observed that in the chemistry-mixed PBMC dataset, with gated across cells; however, numerous methods deliver denoised
a balanced batch design where every cell type is represented by (or imputed) numeric values to represent the accessibility status at
erocs
lebaL
a b
UMAP1
cisTopic peakVI
Harmony (scBasset) Harmony (PCA)
2PAMU
scBasset
UMAP1
2PAMU
1.00
peakVI Harmony (scBasset)
cisTopic scBasset-BC
0.75 scDEC Harmony (PCA)
SCALE
0.50
0.25
0
0 0.25 0.50 0.75 1.00
kBET
scBasset-BC
erocs
lebaL
d
Cell type
CLP
CMP Batch
GMP BM0106
HSC BM0828
LMPP BM1077
MEP BM1137
MPP BM1214
UNK Other
Mono
pDC
Multiome
Nextgem
e
Fig. 3 | scBasset batch correction. a, Cell embeddings learned by scbasset without batch correction on a mixture of pbmC scAtAC from 10x multiome and
10x next Gem chemistries (top). Cells are colored by chemistry. Cell embeddings learned by scbasset with batch correction (scbasset-bC) on the same data
(bottom). b, buenrostro2018 cell embeddings learned by scbasset, colored by cell type (left) or batch (right). c, buenrostro2018 cell embeddings learned by
scbasset-bC, colored by cell type (left) or batch (right). d, performance comparison of different batch correction methods on chemistry-mixed pbmC data.
Harmony is applied on either pCA, named Harmony (pCA), or scbasset embeddings, named Harmony (scbasset), and performance was evaluated by kbet
and label score (with a neighborhood of 100). e, Similar performance comparison of different batch correction methods on buenrostro2018 data. Source
data for this figure are provided.
NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods 1091
Articles NATurE METHoDS
0.5
0.4
0.3 0.2
0.1
0
0 0.1 0.2 0.3 0.4 0.5
Correlation (raw, scRNA)
every cell/peak combination. scBasset computes such values in its expression7,23. We propose that effective denoising would improve
sequence-based predictions. the correlation between these gene accessibility estimates and
From the Buenrostro2018 dataset, we sampled 500 peaks and the gene’s measured RNA expression in multiome experiments.
200 cells and directly visualized the raw cell-by-peak matrix versus Thus, we computed accessibility scores for each gene by averag-
the denoised matrix (Fig. 4a). In the raw binary matrix, we observed ing the predicted accessibility values at all promoter peaks before
that cells and peaks clustered by sequencing depth, showing no and after denoising (Methods). For both the 10x multiome PBMC
biologically relevant patterns. However, we observed that after and mouse brain datasets, we observed that scBasset denoising
scBasset denoising, cells of the same cell type share similar accessi- improves the consistency between gene accessibility and expression
bility profiles and hierarchical clustering of cells matched well with (P < 2.2 × 10−16, Wilcoxon signed-rank test). As one would expect,
ground-truth labels. the improvement is greater for cells with fewer scATAC unique
Following a previous study, we evaluated the denoising perfor- molecular identifiers (Fig. 4b and Extended Data Fig. 5).
mance of scBasset on Buenrostro2018 by its impact on cell–cell For 10x multiome PBMC and 10x multiome mouse brain data-
distance estimation and cell embeddings22. (1) We evaluated the sets, we quantified denoising performance by adopting metrics
cell–cell distance matrix calculated from the denoised cell-by-peak from22 and our additional multiome-specific metrics. We quantified
matrix and asked whether cells of the same label are closer together, the consistency between gene accessibility and expression either as
using the cell type ASW. (2) We performed PCA embedding (with correlation across genes for each cell (correlation per cell) or as cor-
50 components) on the denoised cell-by-peak matrix and asked relation across cells for each gene (correlation per gene).
whether cells of the same type embed closer together, as evaluated We observed that scBasset outperformed all alternative methods
by our label score on nearest neighbor sets. Comparing to cisTopic, on the cell type ASW and neighbor score metrics in the multiome
peakVI, MAGIC, SCALE and scOpen, we observed that scBasset datasets; however, there was not a clear winner for the RNA/ATAC
denoising outperformed these alternative approaches on the two consistency metrics (Fig. 4c and Extended Data Fig. 5). Methods
metrics (Extended Data Fig. 5). scBasset denoising also results in such as scBasset and MAGIC achieve better correlation per gene,
more robust differential accessibility results (Supplementary Fig. 7). whereas methods such as peakVI and scOpen achieve greater cor-
Several published strategies aggregate scATAC counts in the relation per cell. Overall, Spearman’s correlation between ‘correla-
region around a gene’s transcription start site to estimate its tion by cell’ and ‘correlation by gene’ metrics for different methods
)ANRcs
,tessaBcs(
noitalerroC
c
a b
P < 2.2 × 10–16
Depth 5.0
4.0
d e
0
–10
–20
–10 0 10 UMAP_1
2_PAMU
scRNA and raw scATAC integration
5
0
–5
–10
–15
–10 –5 0 5 10 UMAP_1
2_PAMU
Raw matrix
Cell labels MPP GMP MEP
HSC CLP CMP LMPP
pDC Mono
UNK
Peaks
scRNA and denoised scATAC integration
slleC
Denoised matrix
Peaks
slleC
1.0 0.34 scBasset
0
Accessibility 0.32 cisTopic MAGIC
0.30 peakVI
0.28 scOpen
SCALE 0.26 Raw
0.51 0.54 0.57
Cell type ASW
erocs
robhgieN
MAGICscBasset SCALE
0.25 cisTopic scOpen
peakVI
0.20
0.15
0.10 Raw
0.2 0.3 0.4
Correlation per cell (RNA, ATAC)
eneg
rep noitalerroC
)CATA
,ANR(
2,000
1,500
1,000
500
0
MA G sc I B C asse p t eak s V c I Ope S n CA c L i E sTopic ra w
ecnatsid
gniddebme
CATA/ANR
8,000
6,000
4,000
2,000
0
scBass M et A G c I i C sTop s i c c Ope p n eakV S I CALE ra w
ecnatsid
gniddebme
CATA/ANR
Multiome PBMC integration Multiome mouse brain integration
scATAC scATAC
scRNA scRNA
Fig. 4 | scBasset denoising performance evaluation. a, binary count matrix of 200 cells and 500 peaks sampled from buenrostro2018 dataset,
hierarchically clustered by both cells and peaks (left). Cell type labels annotate the rows. the same matrix and procedure after scbasset denoising (right).
b, Correlation between gene accessibility score and gene expression across genes for each cell before (x axis) and after scbasset denoising (y axis) for
the multiome pbmC dataset. A one-sided Wilcoxon signed-rank test was performed. Cells are colored by sequencing depth. c, Comparison of different
denoising methods in multiome pbmC dataset as evaluated by label score and cell type ASW (left). Comparison of different denoising methods in
multiome pbmC dataset as evaluated by correlation between scVI-denoised rNA and denoised AtAC profiles across genes per cell (correlation per cell),
and correlation between scVI-denoised rNA and denoised AtAC profiles across cells per gene (correlation per gene) (right). d, UmAps of rNA and AtAC
co-embeddings after integration for multiome pbmC dataset. Integration performed on scVI-denoised rNA (blue) and raw AtAC (red) (left). Integration
performed on scVI-denoised rNA (blue) and scbasset-denoised AtAC (red) (right). e, Comparison of integration performance on multiome pbmC dataset.
performance is measured by the relative distances between each cell’s rNA and AtAC embeddings (methods) when integrating the scVI-denoised rNA
profiles with AtAC profiles denoised with different methods; n = 2,714 cells for each box plot on the left, and n = 4,881 cells for each box plot on the right.
the box plot shows min and max as whiskers (excluding outliers), first and third quartiles as boxes and median in the center. Outliers (>1.5× interquartile
range away from the box) are not shown. Source data for this figure are provided.
1092 NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods
NATurE METHoDS Articles
(excluding the raw count matrix) is −0.71 for multiome PBMCs and Examining some of the key regulators of PBMC cell types, we
−0.89 for multiome mouse brain datasets. This suggests a tradeoff observed that scBasset TF activities have greater cell type specificity
between smoothing across cells and preserving cell–cell variability. and correlate better with TF expression than chromVAR (Fig. 5c and
Integration of cells independently profiled by scRNA and Extended Data Fig. 8). We observed this for B-cell-specific activity of
scATAC into a shared latent space is a key step for many scATAC PAX5, T-cell-specific activity of TCF7, natural killer (NK)-cell-specific
annotation and analysis methods24. We hypothesized that scATAC activity of RUNX3 and monocyte-specific activity of CEBPB.
denoising would improve scRNA and scATAC integration perfor- Notably, while scRNA-seq shows monocyte-specific expression of
mance. To evaluate integration performance, we treated the 10x RXRA, scBasset and chromVAR strongly disagree, making opposite
multiome scRNA and scATAC profiles as having originated from predictions for RXRA activity; scBasset predicts RXRA as a repressor
two independent experiments and quantitatively measured the rank (r = −0.70), whereas chromVAR suggests an activating role (r = 0.56).
distance between the RNA and ATAC embeddings for each match- A literature review revealed stronger evidence that RXRA plays a
ing cell (Methods). We observed that denoising either the scRNA or repressive role in the myeloid lineage through direct DNA binding,
the scATAC profiles improves integration performance and optimal which is more consistent with the scBasset prediction26.
performance is achieved when both profiles are denoised (Fig. 4d Beyond TF activity correlation with TF expression, one can vali-
and Extended Data Fig. 5). Comparing scBasset to alternative date TF activity inference by studying data in which the TF has been
scATAC denoising methods, we observed that scBasset and MAGIC perturbed. Pierce et al. introduced a technique called spear-ATAC,
outperformed alternative methods for data integration (Fig. 4e). in which they targeted specific TFs with CRISPRi in single cells and
read out the perturbed ATAC-seq profile27. To further validate scBas-
scBasset infers transcription factor activity at single-cell resolu- set TF activity inferences, we studied a dataset from this manuscript,
tion. TF binding is a major driver of chromatin accessibility25. As consisting of a pool of nine CRISPRi single guide RNAs (sgRNAs)
scBasset learns to predict accessibility from sequence, we expect the targeting GATA1 (sgGATA1) and GATA2 (sgGATA2) and nine inert
model to capture sequence information predictive of TF binding. sgRNA controls (sgNT) that were introduced into K562 cells express-
To query the single cell TF activity, we leveraged the flexibility of ing a dCas9-KRAB cassette. We trained a scBasset model on the pre-
the scBasset model to predict arbitrary sequences. More specifically, processed peak-by-cell matrix from the original paper. UMAP on
we fed synthetic DNA sequences (dinucleotide shuffled peaks) with the scBasset cell embeddings showed that cells with sgGATA1 can be
and without a particular TF motif of interest to a trained scBasset clearly distinguished from cells with sgGATA2 and sgNT (Extended
model and evaluated the activity of the motif in each cell based on Data Fig. 9), which is consistent with the original publication. We
changes in predicted accessibility (Methods)11. If a TF is playing an compared scBasset and chromVAR’s single cell TF activity inference
activating role in a particular cell, we expect to see increased acces- scores by their ability to distinguish sgGATA1 cells from sgNT and
sibility after the TF motif is inserted. sgGATA2 cells from sgNT using their inferred GATA1 and GATA2
TF regulation in the hematopoietic lineage profiled in the scores, respectively (Fig. 5d and Extended Data Fig. 9). While
Buenrostro2018 dataset has been studied in detail. We per- both scBasset and chromVAR inferred GATA1 activity very well,
formed motif insertion for all 733 human CIS-BP motifs using the scBasset achieved better auPR and auROC. chromVAR prediction
Buenrostro2018-trained model and recapitulated known trajecto- begins to lose precision at recall >0.8, whereas scBasset maintained
ries of motif activity. For example, CEBPB, a known regulator of near-perfect precision even at 0.95 recall (Fig. 5d). Both methods
monocyte development, shows the highest activity in monocytes; struggle to distinguish sgGATA2 from sgNT cells in this experiment.
GATA1, a key regulator of the erythroid lineage, is predicted to Unlike chromVAR, scBasset makes use of an accurate quantita-
be most active in MEPs; and HOXA9, a known master regulator tive model that predicts cell-specific accessibility from the DNA.
of HSC differentiation, has the highest predicted activity in HSCs Not only are we able to query scBasset for TF activity on a per-cell
(Extended Data Fig. 6)15. level, we can also infer TF activity at per-cell per-nucleotide resolu-
Previous sequence-based methods such as chromVAR are also tion. As a proof of principle, we examined a known enhancer for
able to quantify TF motif activity. To systematically compare scBas- the β-globin gene that regulates erythroid-specific β-globin expres-
set and chromVAR on this task, we analyzed the 10x PBMC multi- sion28,29. We performed in silico saturation mutagenesis (ISM) for
ome dataset, in which TF expression measured in the RNA-seq can this 100-bp sequence, in which we predicted the change in acces-
serve as a proxy for its motif’s activity. We inferred motif activity sibility in every cell after mutating each position to its three alterna-
for all 733 human CIS-BP motifs using both scBasset and chrom- tive nucleotides. We aggregated to a single score for each position
VAR. For the 203 TFs that are significantly differentially expressed by taking the normalized ISM score for each reference nucleotide
between cell type clusters, we asked how well the inferred TF activ- (Methods). Figure 5e,f shows the average ISM score for each cell
ity per cell correlates with its expression. We observed that overall type in the erythroid lineage. Using a procedure based on map-
scBasset TF activities correlate significantly better with expres- ping position weight matrices (PWMs) and computing a Pearson
sion than chromVAR TF activities (P < 3.38 × 10−2, Wilcoxon correlation between the PWM and ISM scores, we observed that
signed-rank test) (Fig. 5b). This one-sided test is an underesti- the most influential nucleotides correspond to GATA1 and KLF1
mate of scBasset’s performance advantage over chromVAR, as we motifs, which are known to bind to this enhancer region and regu-
would expect TF expression and inferred activity to be negatively late β-globin expression30.
correlated for repressors. Thus, we evaluated scBasset and chrom- Examining the per-cell ISM scores, we observed the GATA1
VAR on activating and repressive TFs separately. For 74 TFs that and KLF1 motifs contribute more to accessibility as the cells dif-
both methods agreed on a positive TF expression–activity corre- ferentiate in the erythroid lineage (Fig. 5f,g). In comparison, these
lation, scBasset-predicted TF activities have significantly greater two motifs’ nucleotides have low scores in cell types outside of the
correlation with expression than chromVAR-predicted activity erythroid lineage (Supplementary Fig. 8). This experiment sug-
(P < 7.38 × 10−12, Wilcoxon signed-rank test; Extended Data Fig. gests that scBasset learns the accessibility regulatory grammar at a
7). For 41 TFs that both methods agreed on a negative TF expres- single-cell resolution and could be used to identify the TFs regulat-
sion–activity correlation, scBasset-predicted TF activities have a ing specific enhancers in individual cells and lineages.
significantly lesser correlation (more negative) with expression
than chromVAR-predicted activity (P < 1.62 × 10−8, Wilcoxon scBasset scales to million cell datasets. As single-cell datas-
signed-rank test). This is also true for the 10x multiome mouse ets continue to grow in size, scalable and efficient computational
brain dataset (Extended Data Fig. 7). methods become critical. scBasset trains on batches of sequences,
NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods 1093
Articles NATurE METHoDS
a c
B cell
CD4+ T cell CD8+ T cell
CD14+ monocyte
Dendritic cell FCGR3A+ monocyte NK cell
Other
b
1.0
0.5
0
–0.5
–1.0
–1.0 –0.5 0 0.5 1.0
Expression–activity correlation (chromVAR)
e
but predicts all cells in every batch. Thus, the complexity of each users might choose to train for fewer epochs or begin examining
batch step depends on the number of cells but not peaks. intermediate results during training.
We assessed scBasset’s scaling properties by training on one of the To study the influence of cell number on runtime and memory
largest available scATAC datasets, in which the sci-ATAC method usage, we trained scBasset on downsampled human sci-ATAC data
was applied to many human tissues31, to map 1.3 million cells and with 10,000, 20,000, 50,000, 100,000, 200,000, 400,000, 600,000,
more than 200 cell types. After filtering, we trained scBasset with 800,000, 1 million and all cells, and measured the runtime, peak
1,114,621 cells and 118,043 peaks (Extended Data Fig. 10). scBasset CPU memory usage, and peak GPU memory usage (Extended Data
takes 273 s per epoch on this dataset using an Nvidia A100 GPU, Fig. 10). We observed that runtime, CPU memory and GPU mem-
with a peak CPU memory usage of 59.5 GB and peak GPU memory ory all scale linearly with cell number but with a small slope. When
usage of 19.2 GB. We trained for 1,000 epochs, which required 76 h. we increase the number of cells from 10,000 to 1 million (100×),
However, the results change minimally in the later epochs, so some runtime per epoch goes from 49 s to 293 s (6×), CPU memory goes
noitalerroc
ytivitca–noisserpxE )tessaBcs(
B cell: PAX5 PAX5_scBasset: 0.32 PAX5_chromVAR: 0.09
2
10 4
8 1 2
6 0 0
4 –1 –2 2
–4
–2
T cell: TCF7 TCF7_scBasset: 0.89 TCF7_chromVAR: 0.35
10 2
4 P = 3.38 × 10–2 TCF7 8 1 2 6
0 0 4
PAX5 2 –1 –2 –4 –2
Monocyte: RXRA RXRA_scBasset:-0.70 RXRA_chromVAR:0.56
8 2 4
RXRA 6 1 2
0 0
4
–2
–1 2
–4
–2
log(RPM) scBasset chromVAR
2
TF score TF score
2 HSC
0
2 MPP
0
2 CMP
0
2 MEP
0
0 20 40 60 80
chr11:5297168-5297248
erocs
MSI
d
GATA1
0 0.2 0.4 0.6 0.8 1.0
Recall
f
GATA1 KLF1
noisicerP
1.0
0.8
0.6
0.4
0.2
scBasset: auPR = 0.998
chromVAR: auPR = 0.971 0
GATA2
0 0.2 0.4 0.6 0.8 1.0
Recall
noisicerP
Spear-ATAC dataset
1.0
0.8
0.6
0.4
0.2
scBasset: auPR = 0.547
0 chromVAR: auPR = 0.543
HSC
MPP
LMPP CMP
CLP pDC GMP MEP
12.5
10.0
7.5
5.0
2.5
0
–2.5
–5.0
HSCMPPCMPMEP
erocs
MSI-1ATAG
5 4
3
2
1
0
–1
–2
–3
–4
HSCMPPCMPMEP
erocs
MSI-1FLK
g
GATA1 site at KLF1 site at
chr11:5297906 chr11:5297940
* * * NS NS *
Fig. 5 | scBasset infers single cell TF activity. a, UmAp showing annotated pbmC cell types. b, pearson correlation between tF expression and scbasset
or chromVAr-predicted tF activity for 203 differentially expressed tFs. A one-sided Wilcoxon signed-rank test was performed. the example tFs that we
examined in c are highlighted in red. c, UmAp visualization of tF expression (left), scbasset tF activity (middle) and chromVAr tF activity (right) for key
pbmC regulators. pearson correlation between inferred tF activity and expression are shown in the title. d, precision-recall (pr) curves of scbasset and
chromVAr for distinguishing sgGAtA1 cells from sgNt cells in the spear-AtAC dataset (top). pr curves of scbasset and chromVAr for distinguishing
sgGAtA2 cells from sgNt cells (bottom). e, HSC differentiation lineage diagram in the buenrostro2018 study. f, ISm scores for β-globin enhancer at
chr11:5297158-5297258 for HSC, mpp, Cmp and mep cell types. Sequences that match GAtA1 and KLF1 motifs are highlighted in red boxes. g, Distributions
of per-cell tF pWm-ISm scores for GAtA1 and KLF1 for cells in HSC, mpp, Cmp and mep cell types. n = 502, 344, 142, 138 cells for each of Cmp, HSC, mpp
and mep. the pWm-ISm score is the dot product of the pWm and ISm measurements at sites of motif matches (GAtA1 at chr11:5297906 and KLF1 at
chr11:5297940). A one-sided Wilcoxon rank-sum test was performed to test for significance. *P < 0.01; NS, not significant. exact P values are P = 2.06 × 10−9
for mpp versus HSC, P = 2.46 × 10−11 for Cmp versus mpp, and P = 3.83 × 10−39 for mep versus Cmp for GAtA1; P = 0.10 for mpp versus HSC, P = 0.38 for
Cmp versus mpp and P = 4.95 × 10−41 for mep versus Cmp for KLF1. Source data for this figure are provided.
1094 NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods
NATurE METHoDS Articles
from 8 G to 60 G (8×) and GPU memory goes from 1.5 G to 19 G neural network model would further improve scATAC peak-calling
(13×). This result suggests that scBasset is suitable for analysis of by taking into account sequence information (and accounting for
very large scATAC compendium. Tn5 transposition bias). Finally, we plan to explore transfer learning
approaches in which models are pre-trained on large data compen-
Discussion dia before fine-tune training on specific single cell datasets.
In this study we present scBasset, a sequence-based deep-learning
framework for modeling scATAC data. scBasset is trained to pre- online content
dict individual cell accessibility from the DNA sequence underlying Any methods, additional references, Nature Research report-
ATAC peaks, learning a vector embedding to represent the single ing summaries, source data, extended data, supplementary infor-
cells in the process. A trained scBasset model can strengthen mul- mation, acknowledgements, peer review information; details of
tiple lines of scATAC, and we demonstrate state-of-the-art perfor- author contributions and competing interests and statements of
mance on several tasks. Clustering the model’s cell embeddings data and code availability are available at https://doi.org/10.1038/
achieves greater alignment with ground-truth cell type labels. scBas- s41592-022-01562-8.
set can be adapted to achieve state-of-the-art performance in batch
correction tasks. The model outputs can be used as denoised acces- Received: 8 September 2021; Accepted: 27 June 2022;
sibility profiles, which improve concordance with RNA measure- Published online: 8 August 2022
ments. The model learns to recognize TF motifs and their influence
References
on accessibility, and we designed an in silico experiment to insert
motifs into background sequences to query for TF motif activity in 1. Buenrostro, J. D. et al. Single-cell chromatin accessibility reveals principles of
regulatory variation. Nature 523, 486–490 (2015).
single cells. The model can also be applied to predict the influence
2. Satpathy, A. T. et al. Massively parallel single-cell chromatin landscapes of
of mutations, enabling in silico saturation mutagenesis of regulatory human immune cell development and intratumoral T cell exhaustion. Nat.
sequences of interest at a single-cell resolution. Compared to pre- Biotechnol. 37, 925–936 (2019).
vious sequence-based approaches for scATAC such as chromVAR, 3. Miao, Z. et al. Single cell regulatory landscape of the mouse kidney highlights
scBasset achieves better performance at learning cell embeddings cellular differentiation programs and renal disease targets. Nat. Commun. 12,
2277 (2021).
and inferring TF activity because scBasset benefits from a more
4. Cusanovich, D. A. et al. A single-cell atlas of in vivo mammalian chromatin
expressive CNN model that learns more sophisticated sequence accessibility. Cell 174, 1309–1324 (2018).
features, including nonlinear relationships. Compared to previ- 5. Bravo González-Blas, C. et al. cisTopic: cis-regulatory topic modeling on
ous sequence-free approaches such as cisTopic, peakVI or SCALE, single-cell ATAC-seq data. Nat. Methods 16, 397–400 (2019).
6. Chen, H. et al. Assessment of computational methods for the analysis of
scBasset achieves better performance on benchmarking tasks and
single-cell ATAC-seq data. Genome Biol. 20, 241 (2019).
delivers a more interpretable model that can be directly queried for
7. Pliner, H. A. et al. Cicero predicts cis-regulatory DNA interactions from
TF activity or identifying regulatory sequences. single-cell chromatin accessibility data. Mol. Cell 71, 858–871 (2018).
Sequence-based approaches have several limitations. First, we 8. Xiong, L. et al. SCALE method for single-cell ATAC-seq analysis via latent
make use of the reference genome, but many samples will have vari- feature extraction. Nat. Commun. 10, 4576 (2019).
9. Schep, A. N., Wu, B., Buenrostro, J. D. & Greenleaf, W. J. chromVAR:
ant versions, including copy number variations that could lead our
inferring transcription-factor-associated accessibility from single-cell
models astray. Second, we assume that the regulatory motifs and
epigenomic data. Nat. Methods 14, 975–978 (2017).
their interactions generalize across the genome. This assumption 10. de Boer, C. G. & Regev, A. BROCKMAN: deciphering variance in epigenomic
may not be entirely true at some genomic loci for which evolution regulators by k-mer factorization. BMC Bioinf. 19, 253 (2018).
led to bespoke regulatory solutions, such as for X chromosome 11. Kelley, D. R., Snoek, J. & Rinn, J. L. Basset: learning the regulatory code of
the accessible genome with deep convolutional neural networks. Genome Res.
inactivation in females. However, scBasset takes a completely inde-
26, 990–999 (2016).
pendent approach to covariance-based methods, which handle this
12. Zhou, J. & Troyanskaya, O. G. Predicting effects of noncoding
better, and researchers may appreciate running both on their data variants with deep-learning-based sequence model. Nat. Methods 12,
for multiple perspectives. 931–934 (2015).
The foundational work with DNA CNNs has primarily focused 13. Kelley, D. R. et al. Sequential regulatory activity prediction across
chromosomes with convolutional neural networks. Genome Res. 28,
on modeling bulk datasets11,12. scATAC, analyzed with existing
739–750 (2018).
workflows to clusters or cell type labels, can be aggregated into 14. Avsec, Ž. et al. Base-resolution models of transcription-factor binding reveal
pseudo-bulk profiles representing those clusters or cell types. soft motif syntax. Nat. Genet. 53, 354–366 (2021).
Previous work has demonstrated the validity and utility of train- 15. Buenrostro, J. D. et al. Integrated single-cell analysis maps the continuous
ing DNA CNNs on these single-cell-derived profiles to infer regulatory landscape of human hematopoietic differentiation. Cell 173,
1535–1548.e16 (2018).
cell-type-specific TF regulators and predict cell-type-specific
16. Qin, Q. et al. Lisa: inferring transcriptional regulators through integrative
genetic variant effects4,32,33. scBasset also achieves these research modeling of public chromatin accessibility and ChIP-seq data. Genome Biol.
objectives, but we focus here on the contributions of the method to 21, 32 (2020).
single-cell embeddings for clustering and visualization, denoising 17. Wu, K. E., Yost, K. E., Chang, H. Y. & Zou, J. BABEL enables cross-modality
and TF activity inference. Working at a single-cell resolution may translation between multiomic profiles at single-cell resolution. Proc. Natl
Acad. Sci. USA 118, e2023070118 (2021).
be ideal for applications like continuous trajectory of cell states and
18. Lotfollahi, M. et al. Mapping single-cell data to reference atlases by transfer
other cases where discrete clusters may lose information, but work- learning. Nat. Biotechnol. 40, 121–130 (2022).
ing at cluster resolution may be a fine alternative for many other 19. Korsunsky, I. et al. Fast, sensitive and accurate integration of single-cell data
datasets and analyses. with Harmony. Nat. Methods 16, 1289–1296 (2019).
20. Büttner, M., Miao, Z., Wolf, F. A., Teichmann, S. A. & Theis, F. J. A test
In addition, we foresee several paths to further improve our
metric for assessing single-cell RNA-seq batch correction. Nat. Methods 16,
method. To enhance scBasset memory efficiency to scale to
43–49 (2019).
extremely large datasets far beyond one million cells, one could 21. Luecken, M. D. et al. Benchmarking atlas-level data integration in single-cell
sample mini-batches of both sequences and cells rather than genomics. Nat. Methods 19, 41–50 (2022).
only sequences in our current implementation. Methods such as 22. Li, Z. et al. Chromatin-accessibility estimation from single-cell ATAC-seq
data with scOpen. Nat. Commun. 12, 6386 (2021).
TF-MoDISco could be applied to scBasset ISM scores for de novo
23. Granja, J. M. et al. ArchR is a scalable software package for integrative
motif discovery14,34. All approaches to scATAC depend on accurate
single-cell chromatin accessibility analysis. Nat. Genet. 53, 403–411 (2021).
peak calls, and predictive modeling frameworks have been proposed 24. Stuart, T. et al. Comprehensive integration of single-cell data. Cell 177,
to help identify highly specific regulatory elements35. We expect a 1888–1902 (2019).
NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods 1095
Articles NATurE METHoDS
25. Thurman, R. E. et al. The accessible chromatin landscape of the human 32. Kelley, D. R. Cross-species regulatory sequence activity prediction. PLoS
genome. Nature 489, 75–82 (2012). Comput. Biol. 16, e1008050 (2020).
26. Kiss, M. et al. Retinoid X receptor suppresses a metastasis-promoting 33. Janssens, J. et al. Decoding gene regulation in the fly brain. Nature 601,
transcriptional program in myeloid cells via a ligand-insensitive mechanism. 630–636 (2022).
Proc. Natl Acad. Sci. USA 114, 10725–10730 (2017). 34. Shrikumar, A. et al. Technical note on transcription factor motif discovery
27. Pierce, S. E., Granja, J. M. & Greenleaf, W. J. High-throughput single-cell from importance scores (TF-MoDISco) version 0.5.6.5. arXiv. https://arxiv.
chromatin accessibility CRISPR screens enable unbiased identification of org/abs/1811.00416 (2018).
regulatory networks in cancer. Nat. Commun. 12, 2969 (2021). 35. Lal, A. et al. Deep learning-based enhancement of epigenomics data with
28. Tuan, D., Solomon, W., Li, Q. & London, I. M. The ‘β-like-globin’ AtacWorks. Nat. Commun. 12, 1507 (2021).
gene domain in human erythroid cells. Proc. Natl Acad. Sci. USA 82,
6384–6388 (1985). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
29. Li, Q., Peterson, K. R., Fang, X. & Stamatoyannopoulos, G. Locus control published maps and institutional affiliations.
regions. Blood 100, 3077–3086 (2002). Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to
30. Tallack, M. R. et al. A global role for KLF1 in erythropoiesis this article under a publishing agreement with the author(s) or other rightsholder(s);
revealed by ChIP-seq in primary erythroid cells. Genome Res. 20, author self-archiving of the accepted manuscript version of this article is solely governed
1052–1063 (2010). by the terms of such publishing agreement and applicable law.
31. Zhang, K. et al. A single-cell atlas of chromatin accessibility in the human © The Author(s), under exclusive licence to Springer Nature America, Inc. 2022,
genome. Cell 184, 5985–6001 (2021). corrected publication 2022
1096 NATuRe MeTHoDs | VOL 19 | September 2022 | 1088–1096 | www.nature.com/naturemethods
NATurE METHoDS Articles
Methods we only performed hyperparameter searches for the size of the bottleneck layer
scATAC-seq preprocessing. We downloaded the processed peak set for and optimization parameters, including batch size, learning rate, β1 and β2. For the
Buenrostro2018 generated by Chen et al. at https://github.com/pinellolab/ optimization parameters, we chose the values that minimized training loss. For the
scATAC-benchmarking/blob/master/Real_Data/Buenrostro_2018/input/ bottleneck layer, we also examined cell-embedding metrics.
combined.sorted.merged.bed, which involved calling peaks on the aggregated
profile of each cell type and merging them into a single atlas. We downloaded the Training approach. We used a binary cross-entropy loss and monitored the
aligned bam files from https://github.com/pinellolab/scATAC-benchmarking/tree/ training auROC after every epoch. We stopped training when the maximum
master/Real_Data/Buenrostro_2018/input/sc-bams_nodup, also provided by training auROC improved by less than 1 × 10−6 in 50 epochs. This stopping
Chen et al.6. Peaks accessible in fewer than 1% cells were filtered out. The final criterion led to training for around 600 epochs for the Buenrostro2018 dataset,
dataset contains 103,151 peaks and 2,034 cells. 1,100 epochs for the 10x multiome PBMC dataset and 1,200 epochs for the 10x
We downloaded the 10x multiome datasets from 10x Genomics: https:// multiome mouse brain dataset.
support.10xgenomics.com/single-cell-multiome-atac-gex/datasets/2.0.0/pbmc_ We focused on training auROC instead of validation auROC for model
granulocyte_sorted_3k for the PBMC dataset and https://support.10xgenomics. selection because we observed that the model continues to improve cell
com/single-cell-multiome-atac-gex/datasets/2.0.0/e18_mouse_brain_fresh_5k for embeddings even after the point where the validation auROC has plateaued
the mouse brain dataset. Genes expressed in fewer than 5% cells were filtered out. (Supplementary Fig. 9). Stopping criteria based on training set loss are typical
Peaks accessible in fewer than 5% cells were filtered out. for optimization of many statistical models but atypical for overparameterized
deep-learning models that are prone to overfitting. The primary overfitting risk
scRNA-seq preprocessing. For the 10x multiome datasets, we processed the is reduced performance on held-out data, which we do not observe; validation
expression data with scVI v.0.6.5 with n_layers, 1; n_hidden, 768; latent, 64 and a auROC during the later stages of training is stable. Our hyperparameter analyses
dropout rate of 0.2 (ref. 36). We trained scVI for 1,000 epochs with a learning rate indicate that the 32-unit bottleneck layer is a major impediment to true overfitting.
of 0.001, using the option to reduce the learning rate upon plateau using options Thus, although the convolution towers may learn sequence factors that do not
lr_patience of 20 and lr_factor of 0.1. We enabled early stopping when there was generalize well during the later training phase, the final layer weights (which
no improvement on the evidence lower bound loss for 40 epochs. To generate serve as cell embeddings) are constrained and continue to learn from the cell–cell
denoised expression profiles, we used the get_sample_scale() function to sample accessibility correlations in the training data.
from the generative model ten times and took the average. We updated model parameters using stochastic gradient descent using
Briefly, scVI performs denoising by modeling single-cell gene counts by the Adam update algorithm. We performed a random search for optimal
negative binomial distributions and infers the parameters of these distributions hyperparameters including batch size, learning rate and β1 and β2 for the Adam
with a variational autoencoder36. We used scVI-denoised expression profiles to optimizer. The best performance was achieved with a batch size of 128, learning
benchmark scATAC denoising and integration performance as previous work has rate of 0.01, β1 of 0.95 and β2 of 0.9995.
demonstrated that denoised expression values reflect the true values in the cell We focused on the Buenrostro2018 dataset to select the optimal bottleneck
more accurately than the observed counts37, and we observed better integration layer size. We trained models with bottleneck sizes of 8, 16, 32, 64 and 128 and
performance when both RNA and ATAC profiles were denoised (Extended Data observed that bottleneck size 32 gave the best performance (Supplementary Fig. 9).
Fig. 5). We used the learned latent cell representations to build nearest-neighbor
graphs and perform cell clustering. scBasset trained on shuffled labels. To establish baseline performance, for each
of the datasets, we trained scBasset on a training set with labels shuffled. For each
PBMC cell annotations. For multiome PBMC datasets, we performed a simple cell in the training set, we first binarized the accessibility vector and then randomly
cell-type annotation based on gene expression data following a scanpy tutorial shuffled the positives (accessibility regions), while the total number of positives
(https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html). Briefly, we (coverage) was not affected, and re-trained the scBasset model.
first clustered the cells based on scVI latent cell embeddings using the Leiden
algorithm. Then we normalized a cell-by-gene expression matrix by log(reads per Performance evaluation on data dropout. To benchmark model performance
10,000). We ran rank_genes_groups() on the normalized gene expression matrix as a function of data sparsity, we choose a scATAC dataset with relatively high
and plotted the top 25 enriched genes in each Leiden cluster. We compared the top sequencing depth, the 10x multiome PBMC dataset. The original scATAC
enriched genes in each cluster with PBMC marker genes provided in the tutorial peak-by-cell matrix contains 21.2% nonzero entries. We downsampled reads
to assign cell type annotation to each cluster. Clusters where no marker genes were from this matrix and generated datasets of the same size but increasing sparsity.
found in the top 25 enriched genes were assigned to ‘other’. The sampled datasets contain 16.9%, 12.7%, 8.45%, 4.22%, 2.11% and 1.06%
nonzero entries, which is 80%, 60%, 40%, 20%, 10% and 5% of the original data.
Model architecture. scBasset is a neural network architecture that predicts binary Then we trained scBasset models on each of these dropout datasets and evaluated
accessibility vectors for each peak based on its DNA sequence. scBasset takes as the training area under the curve and validation area under the curve, as well as
input a 1,344-bp DNA sequence from each peak’s center and one-hot encodes it as clustering performance (neighbor score), as a function of sparsity.
a 1,344 × 4 matrix. The neural network architecture includes the following blocks:
Benchmarking existing methods. For evaluation of cell embeddings, we
• 1D convolution layer with 288 filters of size 17 × 4, followed by batch normali-
compared scBasset to principal component analysis (PCA) implemented in
zation, GELU and width 3 max pooling layers, which generates a 488 × 288 scikit-learn38, latent sematic indexing (LSI) implemented in cicero7, cisTopic5,
output matrix.
SCALE8, chromVAR with motifs or k-mer features9, ArchR23, snapATAC39,
• Convolution tower of six convolution blocks each consisting of convolution,
peakVI40, and scDEC41.
batch normalization, max pooling and GELU layers. The convolution layers
For evaluation of batch correction performance, we compared scBasset to
have increasing numbers of filters (288, 323, 363, 407, 456 and 512) and kernel
Harmony19, peakVI40, scDEC41, cisTopic5 and SCALE8.
width 5. The output of the convolution tower is a 7 × 512 matrix.
For evaluation of scATAC denoising performance, we compare scBasset to
• 1D convolution layer with 256 filters of width 1, followed by batch normaliza-
cisTopic5, peakVI40, MAGIC42, SCALE8 and scOpen22.
tion and GELU. The output is a 7 × 256 matrix, which is then flattened into a
1 × 1,792 vector.
Cell-embedding evaluation. For implementation details of embedding methods,
• Dense bottleneck layer with 32 units, followed by batch normalization,
see Supplementary Notes.
dropout with rate 0.2, and GELU. The output is a compact peak representation
vector of size 1 × 32.
Clustering-based metrics. We evaluated learned cell embeddings by comparing
• Final dense layer predicting continuous accessibility logits for the peaks in
the clustering to the ground-truth labels (FACS-sorted cell-type labels for
every cell.
Buenrostro2018, RNA-based cell cluster labels for multiome data). We first built
• (Optional) to perform batch correction, we attach a second parallel dense
a nearest-neighbor graph using scanpy with default n neighbors of 15. Then we
layer to the bottleneck layer predicting batch-specific accessibility. This
followed a previous study to tune for a resolution that outputs 10 clusters for
batch-specific accessibility is multiplied by the batch-by-cell matrix to com-
Buenrostro2018, 18 clusters for multiome PBMC and 21 clusters for multiome
pute the batch contribution to accessibility in every cell. This vector is then
mouse brain so that they match the number of ground-truth labels6. Finally, we
added to the previous continuous accessibility logits per cell (Extended Data
compared the clustering outcome to the ground-truth cell type labels using ARI,
Fig. 3). L2 regularization can be optionally applied to the cell-embedding path
AMI and homogeneity as implemented in sklearn.metrics.
(with hyperparameter λ1 ) or the batch-specific path (with hyperparameter λ2 )
to tune the contribution of the batch covariate to the predictions.
Cell type average silhouette width. Silhouette width evaluates whether cells of
• Final sigmoid activation to [0,1] accessibility probability.
the same label are embedded close together by quantifying the distance of a
The total number of trainable parameters in the model is a function cell to other cells of the same label, as compared to distance to cells of different
of the number of cells (n) in the dataset. Specifically, the model will have labels. We evaluated cell embeddings by cell type ASW as proposed in previous
4,513,960 + 33 × n trainable parameters. Due to extensive previous work single-cell studies18, which is the silhouette score average across all cells and
establishing high-performing model architecture hyperparameter ranges11–13, re-normalized to 0 and 1.
NATuRe MeTHoDs | www.nature.com/naturemethods
Articles NATurE METHoDS
Label score. We evaluated the learned cell embeddings using label score for all three • Correlation per gene: computing the Pearson correlation between the gene
datasets. For a given nearest-neighbor graph, label score quantifies what percentage accessibility score and gene expression (after scVI denoising) across all cells
of each cell’s neighbors share its same label in a given neighborhood. For each for each gene.
cell-embedding method, we computed the label score across a neighborhood of 10,
50 and 100. As the ground-truth cell types for the multiome datasets are unknown, Integration evaluation. To evaluate integration performance, we treated the
we used cluster identifiers from scRNA-seq Leiden clustering as cell-type labels. 10x multiome scRNA and scATAC profiles as originated from two independent
experiments. We summarized the accessibility profile to the gene level by
Neighbor score. We evaluated the learned cell embeddings using neighbor score computing the gene accessibility score as described above and integrated the
for the 10x multiome datasets. For a 10x multiome dataset, we built independent scRNA and scATAC data by embedding them into a shared space using Seurat
nearest-neighbor graphs from the scRNA (using scVI) and scATAC (using the FindTransferAnchors() and TransferData() functions24.
cell-embedding method we wanted to evaluate) and quantified the percentage To quantify the integration performance, we measured a ‘RNA/ATAC
of each cell’s neighbors that were shared between the two graphs across embedding distance’ R between the RNA embedding and the ATAC embedding
neighborhoods of size 10, 50 and 100. of each cell c in the co- c embedding space. We use R to represent the ranking of
rna
the Euclidean distance between RNA embedding and ATAC embedding of cell c
Batch correction evaluation. For implementation details of batch correction among all neighbors of c’s RNA embedding and R to represent the ranking of the
methods, see Supplementary Notes. same distance among all neighbors of c’s ATAC em at b ac edding. R is computed as the
c
average of R and R . A smaller R indicates better integration, whereas a higher
Chemistry-mixed PBMC dataset. We first evaluated batch correction performance R indicates r w na orse in a t t e ac gration. c
on a dataset with perfect batch design. We mixed PBMC populations from 10x c
PBMC multiome chemistry (https://cf.10xgenomics.com/samples/cell-arc/1.0.0/ spear-ATAC analysis. spear-ATAC preprocessed count matrix
pbmc_granulocyte_sorted_10k/) and 10x PBMC next GEM chemistry (https:// ‘K562-Pilot-scATAC-Peak-Matrix-SE.rds’ was downloaded from the Gene
cf.10xgenomics.com/samples/cell-atac/2.0.0/atac_pbmc_10k_nextgem/). We Expression Omnibus (accession code GSE168851)27. This dataset contains a pool
generated a shared atlas of 21,017 peaks from the two datasets by resizing the of nine CRISPRi sgRNAs targeting GATA1 (sgGATA1) and GATA2 (sgGATA2)
10x peak calls from the two datasets to 1,000 bp and took the intersection. We and inert sgRNA controls (sgNT) that were introduced into K562 cells expressing
subsampled 2,000 cells from each dataset and merged them over the shared atlas. a dCas9-KRAB367 cassette. Cells with unknown sgRNAs were filtered out
(sgAssignFinal, ’UNK’). We kept cells with at least 5% peaks accessible and peaks
Buenrostro2018 dataset. We compared the batch correction performance of accessible in at least 5% cells for training the scBasset model.
different methods on the Buenrostro2018 dataset. This dataset has an unbalanced We used the cell embeddings generated by scBasset for visualization using
batch design and represents a more practical case for batch correction application. UMAP. We scored GATA1 and GATA2 motif activity using either an scBasset motif
Since popular metrics for batch correction such as kBET and iLISI assume all insertion approach or using chromVAR. We compared scBasset and chromVAR in
batches are present in a local neighborhood in a batch-corrected population21,43, we distinguishing sgGATA1 cells from sgNT using the predicted GATA1 scores and
sampled the Buenrostro2018 dataset to contain only cells from batch ‘BM0828’ and distinguishing sgGATA2 cells from sgNT cells using the predicted GATA2 scores.
‘BM1077’ to compute kBET and iLISI metrics. Prediction performance was evaluated by auPR and auROC.
k-nearest-neighbor batch-effect test acceptance rate. kBET acceptance rate measures sci-ATAC human atlas analysis. We downloaded the processed peak-by-cell
batch mixing by the concordance of local batch distribution with the global batch matrix from the sci-ATAC human atlas stored at http://renlab.sdsc.edu/kai/
distribution20. Higher acceptance rate indicates better mixing. We implemented the Key_Processed_Data/Cell_by_cCRE/31. We kept peaks accessible in more than
kBET R package (v.0.99.6) to compute kBET acceptance rate. 0.5% cells, and cells with at least 500 peaks accessible. The filtered matrix contains
1,114,621 cells and 118,043 peaks. Storing such a matrix in a dense format would
Integration local inverse Simpson’s index. iLISI measures batch mixing by the take more than 1 terabyte of disk space. The data are thus stored in h5ad and
effective number of batch labels in a local neighborhood19. Higher iLISI score sequences used for training are also stored in h5 format. scBasset can easily be
indicates better mixing. We implemented the lisi R package (v.1.0) to compute trained on a dataset of this size because it takes sparse data as input and interacts
iLISI scores. with batches of input at training time.
We trained scBasset on the whole sci-ATAC atlas as well as a sampled dataset
Label score. We quantified the conservation of biological variation after batch with 10,000, 20,000, 50,000, 100,000, 200,000, 400,000, 600,000, 800,000 and
correction by evaluating the cell embeddings with label score. Ground-truth 1,000,000 cells. We measured CPU memory, GPU memory and runtime when
cell-type labels for Buenrostro2018 are provided by FACS-sorting. Ground-truth training scBasset on each dataset. CPU memory is monitored by psutil.Process.
cell-type labels for multiome PBMCs are generated by annotating the matched memory info() command after reading or creating matrices and peak memory
RNA profiles as described previously. usage is reported. GPU memory is monitored using Tensorboard Profiler. Runtime
per epoch is reported by Tensorflow during training.
Denoising evaluation. For implementation details of denoising methods, see
Supplementary Notes. Motif insertion. We performed motif insertion on scBasset to compute a TF
To compute denoised and normalized accessibility across cells for a query peak activity score for each TF for each cell. Specifically, we first generated 1,000
with scBasset, we ran a forward pass on the input DNA sequence to compute the genomic background sequences by performing dinucleotide shuffling of 1,000
latent embedding for the peak. Then we generated the normalized accessibility randomly sampled peaks from the atlas using fasta ushuffle44. For each TF in
across all cells through dot product of the peak, embedding with the weight matrix the motif database, we sampled a motif sequence from the PWM and inserted it
of the final layer. As sequencing depth information is entirely captured by the into the center of each of the genomic background sequences. We ran forward
intercept vector of the final layer, we excluded the intercept term so that scBasset passes through the model for both the motif-inserted sequences and background
generates denoised profiles normalized for sequencing depth. sequences to predict normalized accessibility across all cells. We took the difference
Following a previous study, we evaluated the denoising performance of scBasset in predicted accessibility between the motif-inserted sequences and background
for cell–cell distance estimation and cell embedding22. sequences as the motif influence for each sequence. We averaged this influence
• Cell type ASW: we computed a cell–cell distance matrix from the score across all 1,000 sequences for each cell to generate a cell-level prediction of
denoised cell-by-peak matrix using 1 – PearsonR as the distance metric raw TF activity. Finally, we z score-normalized the raw TF activities to generate the
and asked whether cells of the same label are closer together, using the final TF activity predictions across all cells.
cell type ASW. We used CIS-BP 1.0 single species DNA database motifs downloaded from
• Label score or neighbor score: we performed PCA embedding (PC = 50) on https://meme-suite.org/meme/db/motifs for our motif analysis45.
the denoised cell-by-peak matrix and asked whether cells of the same type
embed closer together, as evaluated by our label score for Buenrostro2018 In silico saturation mutagenesis. We performed ISM to compute the importance
dataset and neighbor score for multiome datasets. scores of all single nucleotides on a sequence of interest. For each position, we
ran three scBasset forward passes, each time mutating the reference nucleotide
Then we evaluated additional multiome-specific metrics for 10x multiome
to an alternative. For each mutation, we compared the alternative accessibility
datasets. Our evaluation is based on the hypothesis that effective denoising would
prediction to that of the reference to compute the change in accessibility for each
improve the correlation between accessibility at genes’ promoters and the genes’
cell. We normalized the ISM scores for the four nucleotides at each position such
expression in multiome measurements7,23. For each gene, we computed a gene
that they summed to zero. We then took the normalized ISM score at the reference
accessibility score by averaging accessibility values for peaks at the gene’s promoter
nucleotide as the importance score for that position.
(2 kb from transcription start site). We evaluated denoising performance by:
In the β-globin enhancer ISM analysis, we labeled TF motifs using the
• Correlation per cell: computing the Pearson correlation between the gene following procedure. First, we scanned the DNA sequence for candidate motif
accessibility score and gene expression (after scVI denoising) across all genes matches using FIMO with a permissive P value threshold of 1 × 10−3 (ref. 46). For
for each individual cell. any motif match, we assigned a score using a Pearson correlation or dot product
NATuRe MeTHoDs | www.nature.com/naturemethods
NATurE METHoDS Articles
between the PWM and ISM. Finally, we performed a statistical test on the match 40. Ashuach, T., Reidenbach, D. A., Gayoso, A. & Yosef, N. PeakVI: A deep
score by comparing the observed correlation with a null distribution computed generative model for single-cell chromatin accessibility analysis. Cell Rep.
from shuffled input. Methods 2, 100182 (2022).
41. Liu, Q., Chen, S., Jiang, R. & Wong, W. H. Simultaneous deep generative
Reporting summary. Further information on research design is available in the modelling and clustering of single-cell genomic data. Nat. Mach. Intell.
Nature Research Reporting Summary linked to this article. https://doi.org/10.1038/s42256-021-00333-y (2021).
42. van Dijk, D. et al. Recovering gene interactions from single-cell data using
Data availability data diffusion. Cell https://doi.org/10.1016/j.cell.2018.05.061 (2018).
43. Tran, H. T. N. et al. A benchmark of batch-effect correction methods for
We used only public datasets in this study. We downloaded the processed
single-cell RNA sequencing data. Genome Biol. 21, 12 (2020).
peak set for Buenrostro2018 generated by Chen et al. at https://github.com/
44. Jiang, M., Anderson, J., Gillespie, J. & Mayne, M. uShuffle: a useful tool for
pinellolab/scATAC-benchmarking/blob/master/Real_Data/Buenrostro_2018/
shuffling biological sequences while preserving the k-let counts. BMC Bioinf.
input/combined.sorted.merged.bed. We downloaded the aligned bam files
9, 192 (2008).
from https://github.com/pinellolab/scATAC-benchmarking/tree/master/
45. Weirauch, M. T. et al. Determination and inference of eukaryotic
Real_Data/Buenrostro_2018/input/sc-bams_nodup. The original datasets are
transcription factor sequence specificity. Cell 158, 1431–1443 (2014).
from the Gene Expression Omnibus (GEO) under accession code GSE96769.
46. Grant, C. E., Bailey, T. L. & Noble, W. S. FIMO: scanning for occurrences of a
We downloaded the 10x multiome datasets from 10x Genomics at https://
given motif. Bioinformatics 27, 1017–1018 (2011).
support.10xgenomics.com/single-cell-multiome-atac-gex/datasets/2.0.0/pbmc_
granulocyte_sorted_3k for the PBMC dataset and https://support.10xgenomics.
com/single-cell-multiome-atac-gex/datasets/2.0.0/e18_mouse_brain_fresh_5k for Acknowledgements
the mouse brain dataset. We downloaded the processed peak-by-cell matrix from We thank V. Agarwal, J. Kimmel and M. Mohamed for feedback on the manuscript. We
sci-ATAC human atlas (GEO accession code GSE184461) stored at http://renlab. thank S. Spock for feedback on the code. We also thank N. Bernstein and A. Odak for
sdsc.edu/kai/Key_Processed_Data/Cell_by_cCRE/. spear-ATAC preprocessed helpful discussions.
count matrix ‘K562-Pilot-scATAC-Peak-Matrix-SE.rds’ was downloaded from
GEO (accession code GSE168851). Source data are provided with this paper. Author contributions
D.R.K. conceived the project. H.Y. and D.R.K. developed the model. H.Y. performed the
Code availability analysis. H.Y. and D.R.K prepared the manuscript.
Code for training and using the scBasset model can be found at https://github.com/
calico/scBasset. Instructions and tutorials are provided at the GitHub repository Competing interests
for how to train scBasset models from anndata and to compute cell embeddings,
H.Y. and D.R.K. are paid employees of Calico Life Sciences.
denoise accessibility profiles, perform TF activity inference and ISM from a
trained scBasset model. A trained scBasset model for the Buenrostro2018 dataset
is available in the kipoi model zoo (https://github.com/kipoi/models/tree/master/ Additional information
scbasset). Extended data is available for this paper at https://doi.org/10.1038/s41592-022-01562-8.
Supplementary information The online version contains supplementary material
References available at https://doi.org/10.1038/s41592-022-01562-8.
36. Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep generative Correspondence and requests for materials should be addressed to Han Yuan
modeling for single-cell transcriptomics. Nat. Methods 15, 1053–1058 (2018). or David R. Kelley.
37. Hou, W., Ji, Z., Ji, H. & Hicks, S. C. A systematic evaluation of single-cell
RNA-sequencing imputation methods. Genome Biol. 21, 218 (2020). Peer review information Nature Methods thanks Luca Pinello, Qiangfeng Cliff Zhang
38. Pedregosa, F. et al. Scikit-learn: machine learning in Python. J. Mach. Learn. and the other, anonymous, reviewer(s) for their contribution to the peer review of this
Res. 12, 2825–2830 (2011). work. Primary Handling editor: Lin Tang, in collaboration with the Nature Methods
39. Fang, R. et al. Comprehensive analysis of single cell ATAC-seq data with team.
SnapATAC. Nat. Commun. https://doi.org/10.1038/s41467-021-21583-9 (2021). Reprints and permissions information is available at www.nature.com/reprints.
NATuRe MeTHoDs | www.nature.com/naturemethods
Articles NATurE METHoDS
Extended Data Fig. 1 | Buenrostro2018 cell embeddings. t-SNe visualization of different cell embedding methods on buenrostro2018, including:
chromVAr motif, chromVAr kmer (k = 6), pCA, cicero (LSI), Archr, snapAtAC, cistopic, scDeC, SCALe, peakVI and scbasset.
NATuRe MeTHoDs | www.nature.com/naturemethods
NATurE METHoDS Articles
Extended Data Fig. 2 | 10x multiome PBMC cell embeddings. UmAp visualization of different cell embedding methods on the 10x multiome pbmC
dataset, including: chromVAr_motif, chromVAr_kmer (k = 6), pCA, cicero (LSI), Archr, snapAtAC, cistopic, scDeC, SCALe, peakVI and scbasset.
NATuRe MeTHoDs | www.nature.com/naturemethods
Articles NATurE METHoDS
Extended Data Fig. 3 | See next page for caption.
NATuRe MeTHoDs | www.nature.com/naturemethods
