---
source_path: /mnt/c/Users/Administrator/Zotero/storage/5JD7WB6R/Cao和Gao - 2022 - Multi-omics single-cell data integration and regulatory inference with graph-linked embedding.pdf
ingested: 2026-04-23
sha256: 33da7f61821595b7
---

Articles
https://doi.org/10.1038/s41587-022-01284-4
Multi-omics single-cell data integration and
regulatory inference with graph-linked embedding
Zhi-Jie Cao 1,2 and Ge Gao 1,2 ✉
Despite the emergence of experimental methods for simultaneous measurement of multiple omics modalities in single cells,
most single-cell datasets include only one modality. A major obstacle in integrating omics data from multiple modalities is
that different omics layers typically have distinct feature spaces. Here, we propose a computational framework called GLUE
(graph-linked unified embedding), which bridges the gap by modeling regulatory interactions across omics layers explicitly.
Systematic benchmarking demonstrated that GLUE is more accurate, robust and scalable than state-of-the-art tools for hetero-
geneous single-cell multi-omics data. We applied GLUE to various challenging tasks, including triple-omics integration, integra-
tive regulatory inference and multi-omics human cell atlas construction over millions of cells, where GLUE was able to correct
previous annotations. GLUE features a modular design that can be flexibly extended and enhanced for new analysis tasks. The
full package is available online at https://github.com/gao-lab/GLUE.
R
ecent technological advances in single-cell sequencing have By modeling the regulatory interactions across omics layers explic-
enabled the probing of regulatory maps through multiple itly, GLUE bridges the gaps between various omics-specific feature
omics layers, such as chromatin accessibility (single-cell spaces in a biologically intuitive manner. Systematic benchmarks and
ATAC-sequencing (scATAC-seq)1,2), DNA methylation (snmC-seq3, case studies demonstrate that GLUE is accurate, robust and scalable
sci-MET4) and the transcriptome (scRNA-seq5,6), offering a unique for heterogeneous single-cell multi-omics data. Furthermore, GLUE
opportunity to unveil the underlying regulatory bases for the func- is designed as a generalizable framework that allows for easy exten-
tionalities of diverse cell types7. While simultaneous assays have sion and quick adoption to particular scenarios in a modular manner.
recently emerged8–11, different omics are usually measured inde- GLUE is publicly accessible at https://github.com/gao-lab/GLUE.
pendently and produce unpaired data, which calls for effective and
efficient in silico multi-omics integration12,13. Results
Computationally, one major obstacle faced when integrating Unpaired multi-omics integration via graph-guided embed-
unpaired multi-omics data (also known as diagonal integration) dings. Inspired by previous studies, we model cell states as
is the distinct feature spaces of different modalities (for exam- low-dimensional cell embeddings learned through variational auto-
ple, accessible chromatin regions in scATAC-seq versus genes in encoders30,31. Given their intrinsic differences in biological nature
scRNA-seq)14. A quick fix is to convert multimodality data into and assay technology, each omics layer is equipped with a separate
one common feature space based on prior knowledge and apply autoencoder that uses a probabilistic generative model tailored to
single-omics data integration methods15–18. Such explicit ‘feature the layer-specific feature space (Fig. 1 and Methods).
conversion’ is straightforward, but has been reported to result in Taking advantage of prior biological knowledge, we propose the
information loss19. Algorithms based on coupled matrix factoriza- use of a knowledge-based graph (‘guidance graph’) that explicitly
tion circumvent explicit conversion but hardly handle more than models cross-layer regulatory interactions for linking layer-specific
two omics layers20,21. An alternative option is to match cells from feature spaces; the vertices in the graph correspond to the features of
different omics layers via nonlinear manifold alignment, which different omics layers, and edges represent signed regulatory inter-
removes the requirement of prior knowledge completely and could actions. For example, when integrating scRNA-seq and scATAC-seq
reduce inter-modality information loss in theory22–25; however, this data, the vertices are genes and accessible chromatin regions (that
technique has mostly been applied to relatively small datasets with is, ATAC peaks), and a positive edge can be connected between an
limited number of cell types. accessible region and its putative downstream gene. Then, adver-
The ever-increasing volume of data is another serious chal- sarial multimodal alignment of the cells is performed as an iterative
lenge26. Recently developed technologies can routinely generate optimization procedure, guided by feature embeddings encoded
datasets at the scale of millions of cells27–29, whereas current integra- from the graph32 (Fig. 1 and Methods). Notably, when the iterative
tion methods have only been applied to datasets with much smaller process converges, the graph can be refined with inputs from the
volumes15,17,20–23. To catch up with the growth in data through- alignment procedure and used for data-oriented regulatory infer-
put, computational integration methods should be designed with ence (see below for more details).
scalability in mind.
Hereby, we introduce GLUE (graph-linked unified embedding), Systematic benchmarking demonstrates superior perfor-
a modular framework for integrating unpaired single-cell multi- mance. We first benchmarked GLUE against multiple popular
omics data and inferring regulatory interactions simultaneously. unpaired multi-omics integration methods15–18,23–25,33 using three
1State Key Laboratory of Protein and Plant Gene Research, School of Life Sciences, Biomedical Pioneering Innovative Center (BIOPIC) and Beijing
Advanced Innovation Center for Genomics (ICG), Center for Bioinformatics (CBI), Peking University, Beijing, China. 2Changping Laboratory, Beijing, China.
✉e-mail: gaog@mail.cbi.pku.edu.cn
1458 NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology
NATUrE BioTEcHNoLoGy Articles
Encoders Decoders
(Variational posteriors) (Generative models)
m
∣ν1∣
V
1
Knowledge-based
guidance graph ∣ν2∣
= (ν, ) V
2
q(V∣ ;ϕ )
∣ν3∣
˄ p
≈
(
V
˄ ∣
·
V
V
;
T
θ )
V
3
Feature
∣ν1∣ embeddings ∣ν1∣
N N
1 1
m
X 1 N 1 X˄ 1 p(X˄ 1∣U 1 ,V 1 ;θ1 )
≈U
1
·V
1
T
scRNA-seq U
q(U 1∣X
1
;ϕ1 ) 1
N 2
∣ν2∣
N 2 N 2
∣ν2∣
X 2 U 2 X˄ 2 p(X˄ 2∣U 2 ,V 2 ;θ2 )
scATAC-seq q(U 2∣X 2 ;ϕ2 ) N ≈U 2 ·V 2 T
3U
∣ν3∣ 3 Cell ∣ν3∣
N 3 X 3 q(U 3∣X 3 ;ϕ3 ) embeddings N 3 X˄ 3 p(X˄ 3∣U 3 ,V 3 ;θ3 )
snmC-seq Discriminator ≈U 3 ·V 3 T
? ? ? D(u;ψ)
Omics layers
Fig. 1 | architecture of the Glue framework. Denoting unpaired data from three omics layer as X1 ∈RN1 ×|V 1 | ,X2 ∈RN2 ×|V 2 | ,X3 ∈RN3 ×|V 3 |,
where N 1 , N 2 , N 3 are cell numbers, and V 1, V 2, V 3 are sets of omics features in each layer, GLUe uses omics-specific variational autoencoders to learn
low-dimensional cell embeddings u, u, u from each omics layer. the data dimensionality and generative distribution can differ across layers, but the
1 2 3
embedding dimension m is shared. to link the omics-specific data spaces, GLUe makes use of prior knowledge about regulatory interactions in the form of
a V g = uid ( a V n ⊤ ce , V gr ⊤ ap ,V h ⊤ G ) = ⊤ f ( r V om , E t ) h , w e h p e ri r o e r v k e n r o ti w ce le s d V ge = -ba V s 1 e ∪ d g V u 2 id ∪ an V c 3 e a g r r e a o p m h, i w cs h f i e c a h t a u r r e e s t . h A en g u ra s p e h d v in a r d ia a t t i a o d n e al c a o u d t e o r e s n to co r d e e c r o n is s u tr s u e c d t t o o m le ic a s r n d a fe ta a t v u i r a e i n e n m e b r e p d r d o i d n u g c s t
1 2 3
with cell embeddings, effectively linking the omics-specific data spaces to ensure a consistent embedding orientation. Last, an omics discriminator D
is used to align the cell embeddings of different omics layers via adversarial learning. ϕ
1
,ϕ
2
,ϕ
3
,ϕG represent learnable parameters in data and graph
encoders. θ1,θ2,θ3,θG represent learnable parameters in data and graph decoders. ψ represents learnable parameters in the omics discriminator.
gold-standard datasets generated by recent simultaneous scRNA-seq During the evaluation described above, we adopted a standard
and scATAC-seq technologies (SNARE-seq8, SHARE-seq9 and schema (ATAC peaks were linked to RNA genes if they overlapped
10X Multiome34), along with two unpaired datasets (Nephron35 in the gene body or proximal promoter regions) to construct the
and MOp36). guidance graph for GLUE and to perform feature conversion for
An effective integration method should match the correspond- other conversion-based methods. Given that our current knowl-
ing cell states from different omics layers, producing cell embed- edge about the regulatory interactions is still far from prefect, a
dings where the biological variation is faithfully conserved and the useful integration method must be robust to such inaccuracies.
omics layers are well mixed. Compared to other methods, GLUE Thus, we further assessed the methods’ robustness to corruption
achieved high level of biology conservation and omics mixing of regulatory interactions by randomly replacing varying fractions
simultaneously (Fig. 2a, each quantified by three separate metrics of existing interactions with nonexistent ones. For all three datas-
as shown in Extended Data Fig. 1), and was consistently the best ets, GLUE exhibited the smallest performance changes even at cor-
method across all benchmark datasets in terms of overall score ruption rates as high as 90% (Fig. 2d and Extended Data Fig. 2a),
(Fig. 2b, see Methods for details on metric aggregation); these suggesting its superior robustness. Consistently, we found that
results were also validated by uniform manifold approximation and using alternative guidance graphs defined in larger genomic
projection (UMAP) visualization of the aligned cell embeddings windows had minimal influence on integration performance
(Supplementary Figs. 1–5). (Extended Data Fig. 2b,c).
An optimal integration method should produce accurate align- Given its neural network-based nature, GLUE may suffer from
ments not only at the cell type level but also at finer scales. Exploiting undertraining when working with small datasets. Thus, we repeated
the ground truth cell-to-cell correspondence in the gold-standard the evaluations using subsampled datasets of various sizes. GLUE
datasets, we further quantified single-cell level alignment error via remained the top-ranking method with as few as 2,000 cells, but
the FOSCTTM (fraction of samples closer than the true match) met- the alignment error increased more steeply when the data volume
ric25. On all three datasets, GLUE achieved the lowest FOSCTTM, decreased to less than 1,000 cells (Fig. 2e and Extended Data Fig. 2d).
decreasing the alignment error by large margins compared to the Additionally, we also noted that the integration performance of
second-best method on each dataset (Fig. 2c, the decreases were GLUE was robust for a wide range of hyperparameter and feature
3.6-fold for SNARE-seq, 1.7-fold for SHARE-seq and 1.5-fold for selection settings (Extended Data Figs. 3 and 4). Apart from the
10X Multiome). cell embeddings, the feature embeddings of GLUE also exhibit
NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology 1459
Articles NATUrE BioTEcHNoLoGy
SNARE-seq SHARE-seq 10X Multiome
0.6
0.4
0.2
0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 5 0 0 0 0 0 5 0 0 0 0 0
2 5 0 0 0 0 2 5 0 0 0 0 2 5 0 0 0 0
1, 2, 4, 8, 1, 2, 4, 8, 1, 2, 4, 8,
Subsample size
considerable robustness to hyperparameter settings, prior knowl- called the integration consistency score, which measures the consis-
edge corruption and data subsampling (Extended Data Fig. 5). tency between the integrated multi-omics space and prior knowl-
In addition to the systematical difference among omics lay- edge in the guidance graph (Methods). We observed substantially
ers, single-cell data are often complicated by batch effect within lower scores (close to 0) when integrating data from inconsistent
the same layer. For example, the SHARE-seq data was processed tissues compared to integrating within the same tissue, making it a
in four libraries, one of which showed batch effect compared to reliable indicator of integration quality (Extended Data Fig. 6).
the other three in scRNA-seq (Supplementary Fig. 6a), while the
Nephron data profiled four donors, all of which showed substantial GLUE enables effective triple-omics integration. Benefitting from
batch effect against each other in both scRNA-seq and scATAC-seq a modular design and scalable adversarial alignment, GLUE read-
(Supplementary Fig. 7a,c). As a solution to such complex sce- ily extends to more than two omics layers. As a case study, we used
narios, GLUE provides batch correction capability by including GLUE to integrate three distinct omics layers of neuronal cells in the
batch as a decoder covariate (Methods). With batch correction adult mouse cortex, including gene expression37, chromatin acces-
enabled, GLUE was able to correct for these batch effects effec- sibility38 and DNA methylation3.
tively, producing substantially better batch mixing (Supplementary Unlike chromatin accessibility, gene body DNA methylation
Fig. 6b and Supplementary Fig. 7b,d). To guard against potential generally shows a negative correlation with gene expression in
over-correction, for example, when forcing an integration over neuronal cells39. GLUE natively supports the mixture of regula-
datasets lacking common cell states, we devised a diagnostic metric tory effects by modeling edge signs in the guidance graph. Such a
MTTCSOF
SNARE-seq SHARE-seq 10X Multiome
0.6
0.4
0.2
0
0 2 468 90 024 68 9 0 02 4 68 90 0.0.0.0.0.1. 0.0.0.0.0.1. 0.0.0.0.0.1.
Corruption rate
MTTCSOF
ni
esaercnI
SNARE-seq SHARE-seq 10X Multiome
1.00
0.75
0.50
0.25
0
Nephron MOp 0.25 0.50 0.75 1.00
1.00
0.75
0.50
0.25
0
0.25 0.50 0.75 1.00 0.25 0.50 0.75 1.00
Biology conservation
gnixim
scimO
AN AN AN AN AN
0.6
0.4
0.2
0
SNARE-seq SHARE-seq 10X Multiome
Dataset
AN AN AAA NNN AN AN AAA NNN AN
MTTCSOF
0.75
0.50
0.25
0
A
R
E-seq
A
R
E-seq
Multio
me Nephron
M
Op
S N S H 10 X
Dataset
erocs
noitargetni
llarevO
a c
d
b
e
UnionCom Online iNMF LIGER (FiG) Seurat v3
Method Pamona Online iNMF (FiG) Harmony GLUE
MMD-MA LIGER bindSC
Fig. 2 | Systematic benchmarks of integration performance. a, Biological conservation score versus omics integration score for different integration
methods. b, Overall integration score (defined as 0.6 × biology conservation + 0.4 × omics integration) of different integration methods (n = 8 repeats
with different model random seeds). c, Single-cell level alignment error (quantified by FOSCttM) of different integration methods (n = 8 repeats with
different model random seeds). d, Increases in FOSCttM at different prior knowledge corruption rates for integration methods that rely on prior feature
relations (n = 8 repeats with different corruption random seeds). e, FOSCttM values of different integration methods on subsampled datasets of varying
sizes (n = 8 repeats with different subsampling random seeds). FiG is an alternative feature conversion method recommended by online iNMF and LIGeR
(Methods). Online iNMF and LIGeR could not run with FiG conversion on the SNARe-seq data because the raw AtAC fragment file was not available,
thus marked as ‘NA’. Other NA marks were made because of memory overflow. the error bars indicate mean ± s.d.
1460 NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology
NATUrE BioTEcHNoLoGy Articles
0.8
0.6
0.4
0.2
0
Combined mCH mCG ATAC
Omics layer
strategy avoids data inversion, which is required by previous meth- gene expression in cortical neurons (average R2 = 0.187). When
ods16,17 and can break data sparsity and the underlying distribution. all epigenetic layers were considered, the expression predictability
For the triple-omics guidance graph, we linked gene body mCH increased further (average R2 = 0.236), suggesting the presence of
and mCG levels to genes via negative edges, while the positive edges nonredundant contributions (Fig. 3f). Among the neurons of dif-
between accessible regions and genes remained the same. ferent layers, DNA methylation (especially mCH) exhibited slightly
The GLUE alignment successfully revealed a shared manifold higher predictability for gene expression in deeper layers than in
of cell states across the three omics layers (Fig. 3a–d). Notably, the superficial layers (Supplementary Fig. 10a). Across all genes, the
original cell types were not annotated at the same resolution, and predictability of gene expression was generally correlated among
many could be further clustered into smaller subtypes even within the different epigenetic layers (Supplementary Fig. 10b). We also
single layers (Supplementary Fig. 8a–f). To unify the cell type observed varying associations with gene characteristics. For exam-
annotations, neighbor-based label transfer was conducted using ple, mCH had higher expression predictability for longer genes,
the integrated cell embeddings and we observed highly significant which was consistent with previous studies17,41, while chromatin
marker overlap (Fig. 3e, three-way Fisher’s exact test40, false discov- accessibility contributed more to genes with higher expression vari-
ery rate (FDR) < 5 × 10−17) for 12 out of the 14 mapped cell types ability (Supplementary Fig. 10c). We also repeated the same analy-
(Supplementary Figs. 8g–o and 9 and Methods), indicating reli- sis using online iNMF, which is currently the only other method
able alignment. The GLUE alignment helped improve the effects capable of integrating the three omics layers simultaneously, but it
of cell typing in all omics layers, including the further partition- produced much lower cell type resolution and epigenetic correla-
ing of the scRNA-seq ‘MGE’ cluster into Pvalb+ (‘mPv’) and Sst+ tion (Supplementary Fig. 11).
(‘mSst’) subtypes (highlighted with green circles/flows in Fig. 3 and
Supplementary Fig. 8), the partitioning of the scRNA-seq ‘CGE’ Integrative regulatory inference with GLUE. The incorporation of
cluster and scATAC-seq ‘Vip’ cluster into Vip+ (‘mVip’) and Ndnf+ a graph explicitly modeling regulatory interactions in GLUE further
(‘mNdnf’) subtypes (highlighted with dark blue circles/flows in enables a Bayesian-like approach that combines prior knowledge
Fig. 3 and Supplementary Fig. 8), and the identification of snmC-seq and observed data for posterior regulatory inference. Specifically,
‘mDL-3’ cells and a subset of scATAC-seq ‘L6 IT’ cells as claus- since the feature embeddings are designed to reconstruct the
trum cells (highlighted with light blue circles/flows in Fig. 3 and knowledge-based guidance graph and single-cell multi-omics data
Supplementary Fig. 8). simultaneously (Fig. 1), their cosine similarities should reflect infor-
Such triple-omics integration also sheds light on the quantita- mation from both aspects, which we adopt as ‘regulatory scores’.
tive contributions of different epigenetic regulation mechanisms As a demonstration, we used the official peripheral blood mono-
(Methods). Among mCH, mCG and chromatin accessibility, we nuclear cell Multiome dataset from 10X34 and fed it to GLUE as
found that the mCH level had the highest predictive power for unpaired scRNA-seq and scATAC-seq data. To capture remote
2R
noisserpxe
eneG
mPv
mL2/3
mL5-2
mL6-2
mDL-3
mL4
mL6-1
mSst mNdnf
mDL-2
mL5-1
mVip
mDL-1
mIn-1
0 50 100 150 200
–log FDR
10
epyt
lleC
UMAP1
2PAMU
UMAP1
Omics layer
scRNA-seq
scATAC-seq
snmC-seq
2PAMU
scRNA-seq cell type
Layer 2/3
Layer 5a
Layer 5
Layer 5b
Layer 6
Claustrum
CGE
MGE
UMAP1
2PAMU
snmC-seq cell type
mL2/3 mDL-3
mL4 mIn-1
mL5-1 mVip
mDL-1 mNdnf-1
mDL-2 mNdnf-2
mL5-2 mPv
mL6-1 mSst-1
mL6-2 mSst-2
UMAP1
2PAMU
a b c
scATAC-seq cell type
L2/3 IT
L4
L5 IT
L6 IT
L5 PT
NP
L6 CT
Vip
Pvalb
Sst
d e f
Fig. 3 | triple-omics integration of the mouse cortex. a–c, UMAP visualizations of the integrated cell embeddings for scRNA-seq (a), snmC-seq (b) and
scAtAC-seq (c), colored by the original cell types. Cells aligning with ‘mPv’ and ‘mSst’ are highlighted with green circles. Cells aligning with ‘mNdnf’ and
‘mVip’ are highlighted with dark blue circles. Cells aligning with ‘mDL-3’ are highlighted with light blue circles. d, UMAP visualizations of the integrated cell
embeddings for all cells, colored by omics layers. e, Significance of marker gene overlap for each cell type across all three omics layers (three-way Fisher’s
exact test40). the dashed vertical line indicates that FDR = 0.01. We observed highly significant marker overlap (FDR < 5 × 10−17) for 12 out of the 14 cell
types, indicating reliable alignment. For the remaining two cell types, ‘mDL-1’ had marginally significant marker overlap with FDR = 0.003, while the ‘mIn-1’
cells in snmC-seq did not properly align with the scRNA-seq or scAtAC-seq cells. f, Coefficient of determination (R2) for predicting gene expression based
on each epigenetic layer as well as the combination of all layers (n = 2,677 highly variable genes common to all three omics layers). the box plots indicate
the medians (centerlines), means (triangles), first and third quartiles (bounds of boxes) and 1.5× interquartile range (whiskers).
NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology 1461
Articles NATUrE BioTEcHNoLoGy
1.0
0.8
0.6
0.4
0.2
0
0 0.25 0.50 0.75 1.00
FPR
Target gene NCF2
0.5 GLUE
(FDR < 0.05)
0
pcHi-C
eQTL
0.5 ATAC
0
–0.5
SPI1 ChIP
NMNAT2 SMG7 APOBEC4 Genes
SMG7-AS1 NCF2 AL157899.1
AL137800.1
ARPC5
RGL1
AL590422.1
183,400 183,450 183,500 183,550 183,600 183,650 183,700 183,750 Kb
chr1
cis-regulatory interactions, we used a long-range guidance graph guidance graph containing distance-weighted interactions as well as
connecting ATAC peaks and RNA genes in 150-kb windows pcHi-C- and eQTL-supported interactions (Supplementary Fig. 13).
weighted by a power-law function that models chromatin con- The significance of regulatory score was evaluated by comparing
tact probability42,43 (Methods). Visualization of cell embeddings it to a NULL distribution obtained from randomly shuffled fea-
confirmed that the GLUE alignment was correct and accurate ture embeddings (Methods). As expected, while the multi-omics
(Supplementary Fig. 12a,b). As expected, we found that the regula- alignment was insensitive to the change in guidance graph, the
tory score was negatively correlated with genomic distance (Fig. 4a) inferred regulatory interactions showed stronger enrichment for
and positively correlated with the empirical peak–gene correlation pcHi-C and eQTL (Supplementary Fig. 13a–d). Large fractions of
(computed with paired cells, Fig. 4b), with robustness across differ- high-confidence interactions simultaneously supported by pcHi-C,
ent random seeds (Supplementary Fig. 12c). eQTL and correlation could be robustly recovered (FDR < 0.05),
To further assess whether the score reflected actual cis-regulatory even if they were corrupted in the guidance graph (Supplementary
interactions, we compared it with external evidence, including Fig. 13e). Furthermore, the GLUE-derived transcription factor (TF-)
pcHi-C44 and eQTL45. The GLUE regulatory score was higher for target gene network (Methods) showed more significant agreement
pcHi-C-supported peak–gene pairs in all distance ranges (Fig. 4a) with manually curated connections in the TRRUST v2 database46
and was a better predictor of pcHi-C interactions than empirical than individual evidence-based networks (Supplementary Figs. 13f
peak–gene correlations (Fig. 4b), as well as LASSO and Cicero43, and Supplementary Fig. 14 and Supplementary Data 2).
the coaccessibility-based regulatory prediction method (Fig. 4c and We noticed that the GLUE-inferred cis-regulatory interactions
Supplementary Fig. 12d). The same held for eQTL (Supplementary could provide hints about the regulatory mechanisms of known
Fig. 12e–h). TF-target pairs. For example, SPI1 is a known regulator of the NCF2
The GLUE framework also allows additional regulatory evi- gene, and both are highly expressed in monocytes (Supplementary
dence, such as pcHi-C, to be incorporated intuitively via the guid- Fig. 15a,b). GLUE identified three remote regulatory peaks for NCF2
ance graph. Thus, we further trained models with a composite with various pieces of evidence, that is, roughly 120 kb downstream,
RPT
pcHi-C prediction
1.0
0.5
0
Cicero (AUROC = 0.548)
–0.5 Spearman (AUROC = 0.555)
LASSO (AUROC = 0.547)
GLUE (AUROC = 0.631) –1.0
–0.5 0 0.5 1.0
Spearman correlation
erocs
yrotaluger
EULG
1.0
0.5
0
–0.5
pcHi-C
–1.0 False True
b b b b b b
5
k
0
k
5
k
0
k
5
k
0
k
2 5 7 0 2 5 – – – 1 1 1
0 5 0 – – – 2 5 5 0 5
7 0 2
1 1
Genomic distance
erocs
yrotaluger
EULG
a b c
pcHi-C
False
True
d e
Target gene CD83
0.5 GLUE
(FDR < 0.05)
0
pcHi-C
eQTL
0.5 ATAC
0 –0.5
BCL11A ChIP
PAX5 ChIP
RELB ChIP
RNF182 CD83 AL353152.2 Genes
MRPL35P1 AL133259.1
AL022396.1 RNU7-133P AL353152.1
LINC01108
13,950 14,000 14,050 14,100 14,150 14,200 14,250 14,300 Kb
chr6
Fig. 4 | integrative regulatory inference in peripheral blood mononuclear cells. a, GLUe regulatory scores for peak–gene pairs across different
genomic ranges, grouped by whether they had pcHi-C support. the box plots indicate the medians (centerlines), means (triangles), first and third
quartiles (bounds of boxes) and 1.5× interquartile range (whiskers). b, Comparison between the GLUe regulatory scores and the empirical peak–gene
correlations computed on paired cells. Peak–gene pairs are colored by whether they had pcHi-C support. c, Receiver operating characteristic curves for
predicting pcHi-C interactions based on different peak–gene association scores. AUROC is the area under the receiver operating characteristic curve.
d,e, GLUe-identified cis-regulatory interactions of NCF2 (d) and CD83 (e), along with individual regulatory evidence. SPI1 (highlighted with a green box)
is a known regulator of NCF2.
1462 NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology
NATUrE BioTEcHNoLoGy Articles
UMAP1
25 kb downstream and 20 kb upstream from the transcription start and unbalanced cell type compositions, and has yet to be accom-
site (TSS) (Fig. 4d), all of which were bound by SPI1. Meanwhile, plished at the single-cell level.
most putative regulatory interactions were previously unknown. Implemented as a neural network with minibatch optimization,
For example, CD83 was linked with three regulatory peaks (two GLUE delivers superior scalability with a sublinear time cost, prom-
roughly 25 kb upstream, one about 10 kb upstream from the TSS), ising its applicability at the atlas-scale (Supplementary Fig. 17a).
which were enriched for the binding of three TFs (BCL11A, PAX5 Using an efficient multistage training strategy for GLUE (Methods),
and RELB; Fig. 4e). While CD83 was highly expressed in both we successfully integrated the gene expression and chromatin acces-
monocytes and B cells, the inferred TFs showed more constrained sibility data into a unified multi-omics human cell atlas (Fig. 5).
expression patterns (Supplementary Fig. 15c–f), suggesting that its While the aligned atlas was largely consistent with the origi-
active regulators might differ per cell type. Supplementary Fig. 16 nal annotations29 (Supplementary Fig. 17c–e), we also noticed
shows more examples of GLUE-inferred regulatory interactions. several discrepancies. For example, cells originally annotated as
‘Astrocytes’ in scATAC-seq were aligned to an ‘Excitatory neu-
Atlas-scale integration over millions of cells with GLUE. As rons’ cluster in scRNA-seq (highlighted with pink circles/flows in
technologies continue to evolve, the throughput of single-cell Supplementary Fig. 17). Further inspection revealed that canonical
experiments is constantly increasing. Recent studies have generated radial glial markers such as PAX6, HES1 and HOPX47,48 were actively
human cell atlases for gene expression28 and chromatin accessibil- transcribed in this cluster, both in the RNA and ATAC domain
ity29 containing millions of cells. The integration of these atlases (Supplementary Fig. 18), with chromatin priming9 also detected at
poses a substantial challenge to computational methods due to the both neuronal and glial markers (Supplementary Figs. 19–21), sug-
sheer volume of data, extensive heterogeneity, low coverage per cell gesting that the cluster consists of multipotent neural progenitors
2PAMU
Cell type
UMAP1
2PAMU
a b
Omics layer
Omics layer Corneal and conjunctival epithelial cells Horizontal cells/amacrine cells? Mesangial cells? STC2_TLX1 positive cells
scATAC-seq Ductal cells IGFBP1_DKK1 positive cells Mesothelial cells Satellite cells
scRNA-seq ELF3_AGBL2 positive cells Inhibitory interneurons Metanephric cells Schwann cells
ELF3_AGBL2 positive cells? Inhibitory interneurons? Microglia Skeletal muscle cells
Cell type ENS glia Inhibitory neurons Muscle_Unknown.7 Skeletal muscle cells?
AFP_ALB positive cells ENS neurons Intestinal epithelial cells Myeloid cells Smooth muscle cells
Acinar cells ENS neurons? Intestine_Unknown.4 Neuroendocrine cells Squamous epithelial cells
Adrenocortical cells Endocardial cells Intestine_Unknown.8 Oligodendrocytes Stellate cells
Amacrine cells Epicardial fat cells Islet endocrine cells PAEP_MECOM positive cells Stromal cells
Antigen presenting cells Epithelial cells Kidney_Unknown.7 PDE1C_ACSM3 positive cells Stromal cells?
Astrocytes Erythroblasts Kidney_Unknown.14 PDE11A_FAM19A2 positive cells Sympathoblasts
Astrocytes/oligodendrocytes Excitatory neurons Lens fibre cells Pancreas_Unknown.1 Syncytiotrophoblast and villous cytotrophoblasts?
Bipolar cells Extravillous trophoblasts Limbic system neurons Parietal and chief cells Syncytiotrophoblasts and villous cytotrophoblasts
Bronchiolar and alveolar epithelial cells Eye_Unknown.6 Lymphatic endothelial cells Photoreceptor cells Thymic epithelial cells
CCL19_CCL21 positive cells Ganglion cells Lymphoid and myeloid cells Purkinje neurons Thymocytes
CLC_IL5RA positive cells Goblet cells Lymphoid cells Retinal pigment cells Trophoblast giant cells
CSH1_CSH2 positive cells Granule neurons Lymphoid/Myeloid cells Retinal progenitors and muller glia Unipolar brush cells
Cardiomyocytes Heart_Unknown.10 MUC13_DMBT1 positive cells SATB2_LRRC7 positive cells Ureteric bud cells
Cardiomyocytes/vascular endothelial cells Hematopoietic stem cells Megakaryocytes SKOR2_NPSR1 positive cells Vascular endothelial cells
Cerebrum_Unknown.3 Hepatoblasts Megakaryocytes? SLC24A4_PEX5L positive cells Vascular endothelial cells?
Chromaffin cells Horizontal cells Mesangial cells SLC26A4_PAEP positive cells Visceral neurons
Ciliated epithelial cells
Fig. 5 | integration of a multi-omics human cell atlas. a,b, UMAP visualizations of the integrated cell embeddings, colored by omics layers (a) and cell
types (b). the pink circles highlight cells labeled as ‘excitatory neurons’ in scRNA-seq but ‘Astrocytes’ in scAtAC-seq. the blue circles highlight cells
labeled as ‘Astrocytes’ in scRNA-seq but ‘Astrocytes/oligodendrocytes’ in scAtAC-seq. the brown circles highlight cells labeled as ‘Oligodendrocytes’ in
scRNA-seq but ‘Astrocytes/oligodendrocytes’ in scAtAC-seq.
NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology 1463
Articles NATUrE BioTEcHNoLoGy
(likely radial glial markers) rather than excitatory neurons or astro- for scRNA-seq and scATAC-seq, and zero-inflated log-normal
cytes as originally annotated. GLUE-based integration also resolved for snmC-seq (Methods). Nevertheless, generative distributions
several scATAC-seq clusters that were ambiguously annotated. For can be easily reconfigured to accommodate other omics layers,
example, the ‘Astrocytes/Oligodendrocytes’ cluster was split into such as protein abundance56 and histone modification57, and to
two halves and aligned to the ‘Astrocytes’ and ‘Oligodendrocytes’ adopt new advances in data modeling techniques58.
clusters of scRNA-seq (highlighted, respectively, with blue and • The guidance graphs used in GLUE have currently been limited
brown circles/flows in Supplementary Fig. 17), which was also to multipartite graphs, containing only edges between features
supported by marker expression and accessibility (Supplementary of different layers. Nonetheless, graphs, as intuitive and flex-
Figs. 20 and 21). These results demonstrate the unique value of ible representations of regulatory knowledge, can embody more
atlas-scale multi-omics integration where cell typing can be done in complex regulatory patterns, including within-modality inter-
an unbiased, data-oriented manner across modalities without losing actions, nonfeature vertices and multi-relations. Beyond canon-
single-cell resolution. In particular, the incorporation of batch cor- ical graph convolution, more advanced graph neural network
rection could further enable effective curation of new datasets with architectures59–61 may also be adopted to extract richer informa-
the integrated atlas as a global reference49. tion from the regulatory graph. Particularly, recent advances in
In comparison, we also attempted to perform integration using hypergraph modeling62,63 could facilitate the use of prior knowl-
online iNMF, which was the only other method capable of inte- edge on regulatory interactions involving multiple regulators
grating the data at full scale, but the result was far from optimal simultaneously, as well as enable regulatory inference for such
(Supplementary Figs. 22a,b and 23). Meanwhile, an attempt to inte- interactions.
grate the data as aggregated metacells (Methods) via the popular
Seurat v3 method also failed (Supplementary Fig. 22c,d). Recent advances in experimental multi-omics technologies have
increased the availability of paired data8–11,34. While most of the cur-
Discussion rent simultaneous multi-omics protocols still suffer from lower data
Combining omics-specific autoencoders with graph-based cou- quality or throughput than that of single-omics methods64, paired
pling and adversarial alignment, we designed the GLUE framework cells can be highly informative in anchoring different omics layers
for unpaired single-cell multi-omics data integration with supe- and should be used in conjunction with unpaired cells whenever
rior accuracy and robustness. By modeling regulatory interactions available. It is straightforward to extend the GLUE framework to
across omics layers explicitly, GLUE uniquely supports integrative incorporate such pairing information, for example, by adding loss
regulatory inference for unpaired multi-omics datasets. Notably, terms that penalize the embedding distances between paired cells65.
in a Bayesian interpretation, the GLUE regulatory inference can be Such an extension may ultimately lead to a solution for the general
seen as a posterior estimate, which can be continuously refined on case of mosaic integration14.
the arrival of new data. Apart from multi-omics integration, we also note that the GLUE
Unpaired multi-omics integration shares some conceptual simi- framework could be suitable for cross-species integration, espe-
larities with batch effect correction50, but the former is substantially cially when distal species are concerned and one-to-one orthologs
more challenging because of the distinct, omics-specific feature are limited. Specifically, we may compile all orthologs into a GLUE
spaces. While feature conversion may seem to be a straightforward guidance graph and perform integration without explicit ortholog
solution, the inevitable information loss19 can be detrimental. Seurat conversion. Under that setting, the GLUE approach could also be
v3 (ref. 15) and bindSC33 also devised heuristic strategies to use conceptually connected to a recent work called SAMap66.
information in the original feature spaces in addition to converted Finally, we note that the inferred regulatory interactions from
data, which may explain their improved performance than meth- the current GLUE model are based on the whole input dataset
ods that do not16,17. Meanwhile, known cell types have also been and may be an aggregation of multiple spatiotemporal-specific
used to guide integration via (semi-)supervised learning51,52, but circuits, especially for data derived from distinct tissues (for
this approach incurs substantial limitations in terms of applicability example, atlas). Meanwhile, we notice that in parallel to the
since such supervision is typically unavailable and in many cases coarse-scale global model (for example, the whole-atlas integra-
serves as the purpose of multi-omics integration per se29. Notably, tion model), finer-scale regulatory inference could be conducted
one of these methods was proposed with a similar autoencoder by training dedicated models on cells from a single tissue, poten-
architecture and adversarial alignment52, but it relied on matched tially with spatiotemporal-specific prior knowledge incorporated
cell types or clusters to orient the alignment. In fact, GLUE shares as well67. Such a ‘step-wise refinement’ extension would effectively
more conceptual similarity with coupled matrix factorization meth- help identify spatiotemporal-specific regulatory circuits and
ods20,21, but with superior performance, which mostly benefits from key regulators.
its deep generative model-based design. We believe that GLUE, as a modular and generalizable frame-
We note that the current framework also works for integrat- work, creates an unprecedented opportunity toward effectively
ing omics layers with shared features (for example, the integration delineating gene regulatory maps via large-scale multi-omics inte-
between scRNA-seq and spatial transcriptomics53,54), by using either gration at single-cell resolution. The whole package of GLUE, along
the same vertex or connected surrogate vertices for shared features with tutorials and demo cases, is available online at https://github.
in the guidance graph. In addition, cross imputation could also be com/gao-lab/GLUE for the community.
implemented by chaining encoders and decoders of different omics
layers. However, given a recent report that data imputation could online content
induce artifacts and deteriorate the accuracy of gene regulatory Any methods, additional references, Nature Research report-
inference55, such a function may need further investigation. ing summaries, source data, extended data, supplementary infor-
As a generalizable framework, GLUE features a modular mation, acknowledgements, peer review information; details of
design, where the data and graph autoencoders are independently author contributions and competing interests; and statements of
configurable. data and code availability are available at https://doi.org/10.1038/
s41587-022-01284-4.
• The data autoencoders in GLUE are customizable with appro-
priate generative models that conform to omics-specific data Received: 13 September 2021; Accepted: 15 March 2022;
distributions. In the current work, we used negative binomial Published online: 2 May 2022
1464 NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology
NATUrE BioTEcHNoLoGy Articles
References 34. PBMC from a healthy donor, single cell multiome ATAC gene expression
1. Cusanovich, D. A. et al. Multiplex single cell profiling of chromatin demonstration data by Cell Ranger ARC 1.0.0. 10X Genomics https://support.
accessibility by combinatorial cellular indexing. Science 348, 910–914 (2015). 10xgenomics.com/single-cell-multiome-atac-gex/datasets/1.0.0/pbmc_
2. Chen, X., Miragaia, R. J., Natarajan, K. N. & Teichmann, S. A. A rapid and granulocyte_sorted_10k (2020).
robust method for single cell chromatin accessibility profiling. Nat. Commun. 35. Muto, Y. et al. Single cell transcriptional and chromatin accessibility profiling
9, 5345 (2018). redefine cellular heterogeneity in the adult human kidney. Nat. Commun. 12,
3. Luo, C. et al. Single-cell methylomes identify neuronal subtypes and 2190 (2021).
regulatory elements in mammalian cortex. Science 357, 600–604 (2017). 36. Yao, Z. et al. A transcriptomic and epigenomic cell atlas of the mouse
4. Mulqueen, R. M. et al. Highly scalable generation of DNA methylation primary motor cortex. Nature 598, 103–110 (2021).
profiles in single cells. Nat. Biotechnol. 36, 428–431 (2018). 37. Saunders, A. et al. Molecular diversity and specializations among the cells of
5. Picelli, S. et al. Smart-seq2 for sensitive full-length transcriptome profiling in the adult mouse brain. Cell 174, 1015–1030 (2018).
single cells. Nat. Methods 10, 1096–1098 (2013). 38. Fresh cortex from adult mouse brain (v1), single cell ATAC demonstration
6. Zheng, G. X. et al. Massively parallel digital transcriptional profiling of single data by Cell Ranger 1.1.0. 10X Genomics https://support.10xgenomics.com/
cells. Nat. Commun. 8, 14049 (2017). single-cell-atac/datasets/1.1.0/atac_v1_adult_brain_fresh_5k (2019).
7. Packer, J. & Trapnell, C. Single-cell multi-omics: an engine for new 39. Mo, A. et al. Epigenomic signatures of neuronal diversity in the mammalian
quantitative models of gene regulation. Trends Genet. 34, 653–665 (2018). brain. Neuron 86, 1369–1384 (2015).
8. Chen, S., Lake, B. B. & Zhang, K. High-throughput sequencing of the 40. Wang, M., Zhao, Y. & Zhang, B. Efficient test and visualization of multi-set
transcriptome and chromatin accessibility in the same cell. Nat. Biotechnol. intersections. Sci Rep. 5, 16923 (2015).
37, 1452–1457 (2019). 41. Gabel, H. W. et al. Disruption of DNA-methylation-dependent long gene
9. Ma, S. et al. Chromatin potential identified by shared single-cell profiling of repression in Rett syndrome. Nature 522, 89–93 (2015).
RNA and chromatin. Cell 183, 1103–1116 (2020). 42. Dekker, J., Marti-Renom, M. A. & Mirny, L. A. Exploring the
10. Clark, S. J. et al. scNMT-seq enables joint profiling of chromatin accessibility three-dimensional organization of genomes: Interpreting chromatin
DNA methylation and transcription in single cells. Nat. Commun. 9, interaction data. Nat. Rev. Genet. 14, 390–403 (2013).
781 (2018). 43. Pliner, H. A. et al. Cicero predicts cis-regulatory DNA interactions from
11. Wang, Y. et al. Single-cell multiomics sequencing reveals the functional single-cell chromatin accessibility data. Mol. Cell 71, 858–871 (2018).
regulatory landscape of early embryos. Nat. Commun. 12, 1247 (2021). 44. Javierre, B. M. et al. Lineage-specific genome architecture links enhancers
12. Lake, B. B. et al. Integrative single-cell analysis of transcriptional and and non-coding disease variants to target gene promoters. Cell 167,
epigenetic states in the human adult brain. Nat. Biotechnol. 36, 70–80 (2018). 1369–1384 (2016).
13. Bravo Gonzalez-Blas, C. et al. Identification of genomic enhancers through 45. Aguet, F. et al. Genetic effects on gene expression across human tissues.
spatial integration of single-cell transcriptomics and epigenomics. Mol. Syst. Nature 550, 204–213 (2017).
Biol. 16, e9438 (2020). 46. Han, H. et al. TRRUST v2: an expanded reference database of human and
14. Argelaguet, R., Cuomo, A. S. E., Stegle, O. & Marioni, J. C. Computational mouse transcriptional regulatory interactions. Nucleic Acids Res. 46,
principles and challenges in single-cell data integration. Nat. Biotechnol. 39, D380–D386 (2018).
1202–1215 (2021). 47. Thomsen, E. R. et al. Fixed single-cell transcriptomic characterization of
15. Stuart, T. et al. Comprehensive integration of single-cell data. Cell 177, human radial glial diversity. Nat. Methods 13, 87–93 (2016).
1888–1902 (2019). 48. Pollen, A. A. et al. Molecular identity of human outer radial glia during
16. Gao, C. et al. Iterative single-cell multi-omic integration using online cortical development. Cell 163, 55–67 (2015).
learning. Nat. Biotechnol. 39, 1000–1007 (2021). 49. Fischer, D. S. et al. Sfaira accelerates data and model reuse in single cell
17. Welch, J. D. et al. Single-cell multi-omic integration compares and contrasts genomics. Genome Biol. 22, 248 (2021).
features of brain cell identity. Cell 177, 1873–1887 (2019). 50. Tran, H. T. N. et al. A benchmark of batch-effect correction methods for
18. Korsunsky, I. et al. Fast, sensitive and accurate integration of single-cell data single-cell RNA sequencing data. Genome Biol. 21, 12 (2020).
with Harmony. Nat. Methods 16, 1289–1296 (2019). 51. Stark, S. G. et al. SCIM: universal single-cell matching with unpaired feature
19. Chen, H. et al. Assessment of computational methods for the analysis of sets. Bioinformatics 36, i919–i927 (2020).
single-cell ATAC-seq data. Genome Biol. 20, 241 (2019). 52. Yang, K. D. et al. Multi-domain translation between single-cell imaging and
20. Duren, Z. et al. Integrative analysis of single-cell genomics data by sequencing data using autoencoders. Nat. Commun. 12, 31 (2021).
coupled nonnegative matrix factorizations. Proc. Natl. Acad. Sci. USA 115, 53. Eng, C.-H. L. et al. Transcriptome-scale super-resolved imaging in tissues by
7723–7728 (2018). RNA seqfish. Nature 568, 235–239 (2019).
21. Zeng, W. et al. DC3 is a method for deconvolution and coupled clustering 54. Rodriques, S. G. et al. Slide-seq: a scalable technology for measuring
from bulk and single-cell genomics data. Nat. Commun. 10, 4613 (2019). genome-wide expression at high spatial resolution. Science 363,
22. Demetci, P., Santorella, R., Sandstede, B., Noble, W. S. & Singh, R. SCOT: 1463–1467 (2019).
Single-Cell Multi-Omics Alignment with Optimal Transport. J. Comput. Biol. 55. Ly, L.-H. & Vingron, M. Effect of imputation on gene network reconstruction
29, 3–18 (2022). from single-cell RNA-seq data. Patterns 3, 100414 (2021).
23. Cao, K., Bai, X., Hong, Y. & Wan, L. Unsupervised topological alignment for 56. Bandura, D. R. et al. Mass cytometry: technique for real time single cell
single-cell multi-omics integration. Bioinformatics 36, i48–i56 (2020). multitarget immunoassay based on inductively coupled plasma time-of-flight
24. Cao, K., Hong, Y. & Wan, L. Manifold alignment for heterogeneous mass spectrometry. Anal. Chem. 81, 6813–6822 (2009).
single-cell multi-omics data integration using pamona. Bioinformatics 38, 57. Bartosovic, M., Kabbe, M. & Castelo-Branco, G. Single-cell CUT&Tag
211–219 (2021). profiles histone modifications and transcription factors in complex tissues.
25. Singh, R. et al. Unsupervised manifold alignment for single-cell multi-omics Nat. Biotechnol. 39, 825–835 (2021).
data. In Proc. 11th ACM International Conference on Bioinformatics, 58. Ashuach, T., Reidenbach, D. A., Gayoso, A. & Yosef, N. PeakVI: A deep
Computational Biology and Health Informatics (eds. Aluru, S., Kalyanaraman, generative model for single-cell chromatin accessibility analysis. Cell Reports
A. & Wang, M. D.) a40 (Association for Computing Machinery, 2020). Methods 2, 100182 (2022).
26. Svensson, V., Vento-Tormo, R. & Teichmann, S. A. Exponential scaling of 59. Hamilton, W., et al. in Advances in Neural Information Processing Systems
single-cell RNA-seq in the past decade. Nat. Protoc. 13, 599–604 (2018). (eds. Guyon, I. et al.) 1024–1034 (Curran Associates, Inc., 2017).
27. Kozareva, V. et al. A transcriptomic atlas of mouse cerebellar cortex 60. Veličković, P. et al. Graph attention networks. In Proc. 6th International
comprehensively defines cell types. Nature 598, 214–219 (2021). Conference on Learning Representations (eds. Bengio, Y. & LeCun, Y.)
28. Cao, J. et al. A human cell atlas of fetal gene expression. Science 370, (ICLR, 2018).
eaba7721 (2020). 61. Vashishth, S., Sanyal, S., Nitin, V. & Talukdar, P. Composition-based
29. Domcke, S. et al. A human cell atlas of fetal chromatin accessibility. Science multi-relational graph convolutional networks. In Proc. 8th International
370, eaba7612 (2020). Conference on Learning Representations (ed. Rush, A.) (ICLR, 2020).
30. Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep generative 62. Zhang, R., Zou, Y. & Ma, J. Hyper-SAGNN: a self-attention based graph
modeling for single-cell transcriptomics. Nat. Methods 15, 1053–1058 (2018). neural network for hypergraphs. In Proc. 8th International Conference on
31. Cao, Z. J., Wei, L., Lu, S., Yang, D. C. & Gao, G. Searching large-scale Learning Representations (ed. Rush, A.) (ICLR, 2020).
scRNA-seq databases via unbiased cell embedding with Cell BLAST. 63. Zhang, R., Zhou, T. & Ma, J. Multiscale and integrative single-cell Hi-C
Nat. Commun. 11, 3458 (2020). analysis with Higashi. Nat. Biotechnol. 40, 254–261 (2021).
32. Kipf, T. N. & Welling, M. Variational graph auto-encoders. In Neural 64. Stuart, T. & Satija, R. Integrative single-cell analysis. Nat. Rev. Genet. 20,
Information Processing Systems Workshop on Bayesian Deep Learning 257–272 (2019).
(eds. Gal, Y. et al.) (Curran Associates, Inc., 2016). 65. Amodio, M. & Krishnaswamy, S. MAGAN: aligning biological manifolds. In
33. Dou, J. et al. Unbiased integration of single cell multi-omics data. Preprint at Proc. 35th International Conference on Machine Learning (eds. Dy, J. G. Dy &
bioRxiv https://doi.org/10.1101/2020.12.11.422014 (2020). Krause, A.) 215–223 (PMLR, 2018).
NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology 1465
Articles NATUrE BioTEcHNoLoGy
66. Tarashansky, A. J. et al. Mapping single-cell atlases throughout metazoa adaptation, distribution and reproduction in any medium or format, as long as you give
unravels cell type evolution. eLife 10, e66747 (2021). appropriate credit to the original author(s) and the source, provide a link to the Creative
67. Jung, I. et al. A compendium of promoter-centered long-range chromatin Commons license, and indicate if changes were made. The images or other third party mate-
interactions in the human genome. Nat. Genet. 51, 1442–1449 (2019). rial in this article are included in the article’s Creative Commons license, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in Commons license and your intended use is not permitted by statutory regulation or exceeds
published maps and institutional affiliations. the permitted use, you will need to obtain permission directly from the copyright holder.
Open Access This article is licensed under a Creative Commons To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.
Attribution 4.0 International License, which permits use, sharing, © The Author(s) 2022
1466 NatuRe BioteChNoloGy | VOL 40 | OCtOBeR 2022 | 1458–1466 | www.nature.com/naturebiotechnology
NATUrE BioTEcHNoLoGy Articles
Methods we first sample the edges (i, j) with probabilities proportional to the edge weights
The GLUE framework. We assume that there are K different omics layers to be and then sample vertices j′ that are not connected to i and treat them as if sij′ = sij .
integrated, each with a distinct feature set V k,k = 1,2,…,K. For example, in When maximizing the graph likelihood, the inner products between features are
scRNA-seq, V is the set of genes, while in scATAC-seq, V is the set of chromatin maximized or minimized (per edge sign) based on the Bernoulli distribution. For
v t r t h h e a g e e r i y k k o i t t n n h h s g . o l d a Th m y im e i e r c e s d i n n k a l s a t i t y a o h e n s e r p a n a a li n t c t h d i e e s c s x e o . k l W f l i . ( d n N e i ) ff u , e i s i r s e ∈ e t n x h t V ( k e n o k ) s m t a ∈ o m i c d p X s e l l n e k a , o y s n e i t z e r = e s t h o a 1 r e f e , t o 2 h d b , e e s … n e k r o t , h v t N k e e l d d K a y a v t e o s a r l . d X u N e e k n o o ⊆ o t f a t e f b e R l c a y | e t , V u l t l k h r s | e e f w r i c o i o e t m h l f l s e h p x r a o a v m m e T s h p o i l e m t e e d , r i A l a w a t T r a o A e u l m i C l k d e b p l b e i e h e d a o d e k o n i s n d c l g o o s s c u p t a r o t a ( e g x t d h e k d | a n u t e t , o o a V f r h t ; t θ h a h v k e e ) e g p ( a e r t n h o d e m a is , t s o w i i s t m h , e r d i i l l a e o a t f r D a a e N d m g e A e c b n o e m e d d w e e d t r i o h s n u ) y g l l i d a n to t b i e o t e q h n u e a i a n t n t c o i o o t f h u n t e h r ( a e g 3 g e ) g e n e a d e n r t e e o .
K built on the inner product between the cell embedding u and feature embeddings
from different omics layers are unpaired and can have different sample sizes. To
V. Thus, analogous to the loading matrix in principal component analysis (PCA),
avoid cluttering, we drop the superscript (n) when referring to an arbitrary cell. k
the feature embeddings V confer semantic meanings for the cell embedding space.
We model the observed data from different omics layers as generated by a k
low-dimensional latent variable (that is, cell embedding) u∈Rm: As V k are modulated by interactions among omics features in the guidance graph,
the semantic meanings become linked. While this linearity limits decoder capacity,
p ( xk;θk )=∫p ( xk |u;θk ) p ( u ) du (1) our empirical evaluations show that it is well compensated by the nonlinear
encoders, producing high-quality multi-omics alignments (Fig. 2, Extended Data
where p(u) is the prior distribution of the latent variable, p ( xk |u;θk ) are Figs. 1–4 and Supplementary Figs. 1–7). The exact formulation of data likelihood
learnable generative distributions (that is, data decoders) and θk denotes learnable depends on the omics data distribution. For example, for count-based scRNA-seq
parameters in the decoders. The cell latent variable u is shared across different and scATAC-seq data, we used the negative binomial (NB) distribution:
o o
sp
m m
e
i i
c
c c
i
s s
fi
l o
c
a b
t
y
y
s e e
p
r r s
e
v .
o
a In
f
t i
m
o o n t
e
h s
a
, e
s
w r
u
w
r
h
e
i o
m
le rd
e
t
n
s h ,
t
e u
o
o
f
r b e
t
s
h
p e
e
r r e v
u
s e
n
e d n
d
t d
e
s
r
a t
l
t
y
h a
i
e
n
f r c
g
o o
c
m m
e l
m e
l
a
s
o c
ta
n h
t e
l c a
s
e y
.
ll e r s t a a r t e e s g u en n e d r e a r t l e y d in b g y a a ll p ( xk |u,V;θk )= i∈ ∏ V
k
NB(xki ;μ i ,θi ) (7)
e e n ff c ic o W i d en e it r t h s ly , t w h p e e h r i e f n r o e t r r m ϕ od k e u a d r c e b ti y l o e n m a r o a n f x a i v b m a l r e i i z a p i t n a i r o g a n t m a h l e e p t f e o o r s l s l t o e in w ri i t o n h r g e s e e q v n ( i c u d o | e d x n e k c ; r e ϕ s ) k l , o ) m w (t e o h r d a b e t l o i s f u , i n t d t d i a n s t g : a can be NB(xki ;μ i ,θi )= Γ( Γ θ ( i ) x Γ k(i + xk θ i + i ) 1 ) ( θi + μi μi )xki( θi + θi μi )θi (8)
LX k ( ϕk,θk )=E − x K k ∼ L pd ( a q ta ( ( x u k ) |x [ k E ;ϕ u∼ k ) q( ∥ u| p xk ( ;ϕ u k ) )) lo ] gp ( xk |u;θk ) (2) μ i = Softmaxi (α⊙V ⊤ k u + β)· j∈ ∑ V k xkj (9)
Since different autoencoders are independently parameterized and trained on where μ,θ∈R + |Vk| are the mean and dispersion of the negative binomial
separate data, the cell embeddings learned for different omics layers could have distribution, respectively, α∈R + |Vk| ,β∈R|Vk| are scaling and bias factors,
i i n n c c o o T n r o p s i o l s i r t n a e k t n e t t s h s p e e r m a io u a r t n o k t e i n c n o c m w o e d le a e d n r g s in e , w g a s b e u o p n u r t l o e t p s h s o e s t h e r e e a g y g u a u l r a i e t d o l a r i n n y c k i e e n d g te r p r a a r p o c h t p i e G o r n l = y s . am (V o , n E g ) f , e w at h u i r c e h s ⊙ so f i t s m th a e x H ou a t d p a u m t a a r n d d p ∑ ro j d ∈ u V c k t, x S k o j f g t i m ve a s x t i h r e e p to re t s a e l n c t o s u t n h t e i n it h th d e i m ce e ll n . s T i a o k n i n o g f t s h o e f tmax
a E t d = ist { i ( n i c , t j ) o | m i, i j cs ∈ la V ye } r i s s , w th h e e s r e e t V of = edg ∪ es K k . = E 1 a V ch k i e s d t g h e e i u s n a i l v so er a s s a s l o fe c a ia t t u e r d e w se i t t h a n s d ig ns a d A n a n t d a a l t m o h g e a o n t u c m h sl e u y s , l t m t i h p a e l n y o i y r n i o g g t i b h n y e a r l t 3 o d 0 t . i a s T l t h r c i e o b u u se n t t i t o o e n f n s l s e c u a a r r n e n s a a t l b s h l o e a t b p t e a h r s e a u m l p ib p e r o t a e r r r t y s e d s is i , z a θ e s k o l = o f n re g { c θ a o s , n α w st , e r β u c } c a . t n e d
and weights, which are denoted as s ij and w ij , respectively. We require that w ij ∈ parameterize the means of the distributions by feature-cell inner products.
(0,1], which can be interpreted as interaction credibility, and that sij ∈{−1,1}, For efficient inference and optimization, we introduce the following factorized
which specifies the sign of the regulatory interaction. For example, an ATAC peak variational posterior:
located near the promoter of a gene is usually assumed to positively regulate its
expression, so they can be connected with a positive edge (s ij = 1). Meanwhile, q ( u,V|xk,G;ϕk,ϕG )= q ( u|xk;ϕk )·q ( V|G;ϕG ) (10)
DNA methylation in the gene promoter is usually assumed to suppress expression,
so they can be connected with a negative edge (s ij = 1). In addition to the The graph variational posterior q ( V|G;ϕG ) (that is, graph encoder) is
connections between features, self-loops are also added for numerical stability, modeled as diagonal-covariance normal distributions parameterized by a graph
with sii = 1,wii = 1,∀i∈V. The guidance graph is allowed to be a multi-graph, convolutional network70:
w di h ff e e r r e e n m t o ty re p e th s a o n f p o r n i e o r e d re g g e u c l a a n to e r x y i s e t v b id e e t n w c e e e . n the same pair of vertices, representing q ( V|G;ϕG )= i∈ ∏ V q ( vi |G;ϕG ) (11)
We treat the guidance graph as observed variable and model it as generated
by low-dimensional feature latent variables (that is, feature embeddings)
a x V v n k i d a ∈ ∈ s t g h R R e e m m n c × e , e r i l | a l V ∈ t l e a |, d t V w e b n . h y F t i u c v th h r a t r e c h i a c o e b o m r m l m e b b o i u n i r n e e ∈ , a s t d a i R i o l f l m n f f e . e r o F a i f n t o u f g r e r a c e f t r o u e o n m r m v e e b l t n e a h d t i e e e d n n p i c t n r e e v g , v a s w i r i o i n e a u t b i s o n l e m t a s r o o s v i d d n i u e g ∈ l c l , e e w R t m e h m a e n , t o i n ri w ∈ o x t . m a V T ti o k h o d e n e l ( w G h C er N e ) ϕ e G n c r o ep d r e q e r s . ( e v n i t | s G t ; h ϕ e G l ) ea = rn N ab ( le v p i; a G ra C m N e μ t i e ( r G s i ; n ϕ G th ) e , g G r C ap N h σ c 2 i o ( n G v ; o ϕ l G ut ) i ) onal networ ( k 1 2)
model likelihood can thus be written as: The variational data posteriors q ( u|xk;ϕk ) (that is, data encoders) are
p ( xk,G;θk,θG )=∫p ( xk |u,V;θk ) p (G|V;θG ) p ( u ) p ( V ) dudV (3) m
pe
o
rc
d
e
e
p
le
t
d
ro
a
n
s
(
d
M
ia
L
g
P
on
)
a
n
l
e
-
u
co
ra
v
l
a
n
ri
e
a
t
n
w
c
o
e
r
n
k
o
s:
rmal distributions parameterized by multilayer
o
w
m
he
ic
re
s d
p
a
(
ta
x k
(
|
t
u
h
,
a
V
t i
;
s
θ
,
k
d
)
a
a
t
n
a
d
d e
p
co
(G
de
|V
rs
;
)
θ
a
G
n
)
d
a
k
re
n o
le
w
ar
le
n
d
a
g
b
e
le
g
g
r
e
a
n
ph
er
(
a
t
t
h
iv
a
e
t i
d
s
i
,
s
g
tr
r
i
a
b
p
u
h
t i
d
o
e
n
c
s
o
f
d
o
e
r
r
t
)
h
,
e q ( u|xk,Vk;ϕk )= N(u;MLPk,μ ( xk;ϕk ) ,MLPk,σ2 ( xk;ϕk )) (13)
r
a
e
r
s
e
p
t
e
h
c
e
t i
p
v
r
e
i
l
o
y
r
. θ
d
k
i s
a
t
n
ri
d
b u
θ
t
G
io
a
n
re
s o
le
f
a
t
r
h
n
e
a
c
b
e
le
ll
p
la
a
t
r
e
a
n
m
t
e
v
t
a
e
r
r
i
s
a b
in
le
t
a
h
n
e
d
d
f
e
e
c
a
o
t
d
u
e
re
rs
l
.
a
p
te
(
n
u
t
)
v
a
a
n
r
d
ia
p
b
(
l
V
es
)
,
where ϕk is the set of learnable parameters in the multilayer perceptron encoder of
the kth omics layer.
respectively, which are fixed as standard normal distributions for simplicity:
Model fitting can then be performed by maximizing the following evidence
p ( u )= N ( u;0,Im ) (4) lower bound:
p ( vi )= N ( vi;0,Im ) ,p ( V )= i∈ ∏ V p ( vi ) (5) k ∑ = K 1 E xk ∼pdata (xk )   E u∼q( − u| K xk L ;ϕ ( k ) q ,V ( ∼ u| q x ( k V ; | ϕ G k ;ϕ ) G q ) ( V lo | g G p ;ϕ ( x G k ) |u ∥ ,V p ; ( θ u k ) ) p p ( ( V G ) |V ) ;θG ) 
although alternatives may also be used68. For convenience, we also introduce the (14)
notation Vk ∈Rm×|V k |, which contains only feature embeddings in the kth omics
which can be further rearranged into the following form:
layer, and u, which emphasizes that the cell embedding is from a cell in the kth
k
omi T cs h l e a y g e r r a . ph likelihood p (G|V;θG ) (that is, graph decoder) is defined as: K·LG ( θG,ϕG )+
k
∑
=
K
1
LXk ( θk,ϕk,ϕG ) (15)
logp (G|V;θG )=E i,j∼p ( i,j;wij ) (6) where we have
[logσ(sijv ⊤ i vj )+E j′∼pns (j′|i)log(1−σ(sijv ⊤ i vj′))] LX k ( θk,ϕk,ϕG )=E xk ∼pdata (xk )
w H h er e e r e t h σ e i s g r t a h p e h s i l g ik m e o li i h d o f o u d n h ct a i s o n n o a n tr d a i p n n a s b is l e a p n a e r g a a m ti e v t e e s r a s, m so p li θ n G g d = is ∅ tr . i I b n u t o i t o h n e 6 r 9 . w ords, [E u∼q(u|xk;ϕk ),V∼q ( V|G;ϕG )logp ( xk |u,V;θk )−KL ( q ( u|xk;ϕk )∥p ( u ))] (16)
NatuRe BioteChNoloGy | www.nature.com/naturebiotechnology
Articles NATUrE BioTEcHNoLoGy
LG ( θG,ϕG )=E V∼q ( V|G;ϕG )logp (G|V;θG )−KL ( q ( V|G;ϕG )∥p ( V )) normalize by cluster size, which effectively balances the contribution of matching
(17) clusters regardless of their sizes. In the second stage, we fine-tune the GLUE
model with the estimated balancing weights, during which the additive noise
Below, for convenience, we denote the union of all encoder parameters ϵ∼N( ϵ;0,τ·Σ ) gradually anneals to 0 (with τ starting at 1 and decreasing
as ϕ =(∪K k=1 ϕk )∪ϕG and the union of all decoder parameters as linearly per epoch until 0). The number of annealing epochs was set automatically
θ =(∪K k=1 θk )∪θG . b
4,
a
0
s
0
e
0
d
i
o
te
n
r a
th
ti
e
o n
da
s
t
a
a
t
s
a
i z
le
e
a
a
r
n
n
d
in
l
g
ea
r
r
a
n
te
in
o
g
f
r
0
a
.
t
0
e
0
t
2
o
.
match a learning progress equivalent to
To ensure the proper alignment of different omics layers, we use the adversarial
alignment strategy31,71. A discriminator D with a K-dimensional softmax output is All benchmarks and case studies in the study were conducted with the
two-stage training procedure as described above, regardless of whether the dataset
introduced, which predicts the omics layers of cells based on their embeddings u.
being used is balanced or not.
The discriminator D is trained by minimizing the multiclass classification cross
entropy:
Batch effect correction. To handle batch effect within omics layers, we incorporate
L D ( ϕ,ψ )=− K 1
k
∑
=
K
1
E xk ∼pdata (xk ) E u∼q(u|xk;ϕk )logDk ( u;ψ ) (18) i b
p
n a d
(
tc
x
e h
k
x
|
, a
u
w s
,
h
V
a e c
,
r o
b
e
;
v
θ
B a
k
r i
)
i s
.
a
S
t t e h
p
e o
e c
f t o
i
t
f
h t
i
a
c
e l
a
d
l
n
l
a
y
u t
,
m a
t h
d b
i
e e
s
c r
i
o
s
o d
a
f e
c
b r
h
a s
i
t .
e
c A
v
h
e
s e
d
s s u ,
b
m t
y
h i e
c
n
o
d g
n
e b
v
c
e
o ∈
r
d
t
e
i
{
n
r 1
g
l , i
l
k 2
e
e ,
a
l …
r
ih
n
, o
a
B
b
o }
l
d
e
, i i
p
s s
a
e t
r
h x
a
t e
m
e b n
e
a d
t
t
e
e c
r
d h
s
to
where D k represents the kth dimension of the discriminator output and ψ is the in the data decoder to be batch-dependent. For example, in the case of a negative
set of learnable parameters in the discriminator. The data encoders can then be binomial decoder, the network now uses batch-specific α, β and θ parameters:
trained in the opposite direction to fool the discriminator, ultimately leading to the
align
T
m
he
e n
o
t
v e
o
r
f
a
c
l
e
l
l
t
l
r
e
a
m
in
b
in
e
g
d d
o
i
b
n
j
g
ec
s
t
f
i
r
v
o
e
m
o f
d
G
if
L
fe
U
re
E
n
t
t
h
o
u
m
s
i
c
c
o
s
n
l
s
a
i
y
s
e
ts
r s
o
72
f
.
:
p ( xk |u,V,b;θk )= i∈ ∏ V
k
NB(xki ;μ i ,θbi ) (25)
m ψ inλD ·L D ( ϕ,ψ ) (19) NB(xki ;μ i ,θbi )= Γ ( Γ θ ( bi x )k Γ i + ( x θ k b i + i ) 1 ) ( θbi μ +i μi )xki( θb θ i +bi μi )θbi (26)
m θ, a ϕ xλD ·L D ( ϕ,ψ )+ λGK·LG ( θG,ϕG )+ k ∑ = K 1 LXk ( θk,ϕk,ϕG ) (20) μ i = Softmaxi (αb ⊙V ⊤ k u + β b )· j∈ ∑ V
k
xkj (27)
align T m he e n tw t a o n h d y p gr e a r p p h ar - a b m as e e t d e r f s e a λ t D u a re n d em λ b G e c d o d n in tr g o , l r t e h s e p e co ct n iv tr e i l b y u . W tio e n u s s o e f s a t d o v c e h r a s s a t r ic ia l where α∈R + B×|V k | ,β∈RB×|V k | ,θ∈RB + ×|V k | , and αb , βb , θb are the bth row of α,
gradient descent to train the GLUE model. Each stochastic gradient descent β, θ. Other probabilistic decoders can also be extended in similar ways.
iteration is divided into two steps. In the first step, the discriminator is updated
according to objective equation (19). In the second step, the data and graph Implementation details. We applied linear dimensionality reduction using
autoencoders are updated according to equation (20). The RMSprop optimizer canonical methods such as PCA (for scRNA-seq) or LSI (latent semantic indexing,
with no momentum term is used to ensure the stability of adversarial training. for scATAC-seq) as the first transformation layers of the data encoders (note that
the decoders were still fitted in the original feature spaces). This effectively reduced
Weighted adversarial alignment. As shown in previous work31, canonical model size and enabled a modular input, so advanced dimensionality reduction or
adversarial alignment amounts to minimizing a generalized form of Jensen–Shannon batch effect correction methods can also be used instead as preprocessing steps for
divergence among the cell embedding distributions of different omics layers: GLUE integration.
During model training, 10% of the cells were used as the validation set. In
K
1 ∑ K
KL
(
qk
(
u
)||
K
1 ∑ K
qk
(
u
) )
(21)
t
t
h
h
e
e
f
v
i
a
n
l
a
id
l
a
s
t
t
i
a
o
g
n
e
l
o
o
f
s
t
s
r
d
ai
i
n
d
i n
n
g
o
,
t
t
i
h
m
e
p
l
r
e
o
a
v
rn
e
i
f
n
o
g
r
r
c
a
o
t
n
e
s
w
ec
o
u
u
t
l
i
d
v e
b
e
e
p
r
o
e
c
d
h
u
s
c
.
e
T
d
r a
b
i
y
n
f
i
a
n
c
g
t o
w
r
o
s
u
o
l
f
d
1
b
0
e
i f
k=1 k=1
terminated if the validation loss still did not improve for consecutive epochs. The
where qk ( u )=E xk ∼pdata (xk )q ( u|xk;ϕk ) represents the marginal cell embedding patience for learning rate reduction, training termination and the maximal number
distribution of the kth layer. Without other loss terms, equation (21) converges at of training epochs were automatically set based on the data size and learning rate
perfect alignment, that is, when qi ( u )= qj ( u ) ,∀i̸= j. This can be problematic to match a learning progress equivalent to 1,000, 2,000 and 16,000 iterations at a
when cell type compositions differ dramatically across different layers, for example, learning rate of 0.002, respectively.
in the cell atlas integration. To address this issue, we added cell-specific weights w(n) For all benchmarks and case studies with GLUE, we used the default
to the discriminator loss in equation (18): hyperparameters unless explicitly stated. The set of default hyperparameters is
presented in Extended Data Fig. 3.
L D ( ϕ,ψ )=− K 1 k ∑ = K 1 W 1 k n ∑ N = k 1 w (n)·E u∼q(u|x ( k n) ;ϕk) logDk ( u;ψ ) (22) Integration consistency score. The integration consistency score is a measure
of consistency between the integrated multi-omics data and the guidance graph.
w m h in e i r m e t i h zi e n n g o e r q m u a at li i z o e n r ( W 21 k ) = bu ∑ t w N n it =k h 1 w w e ( i n g ) h . T te h d e m ad ar v g e i r n sa a r l i c a e l l a l l e i m gn b m ed e d n i t n s g ti l d l i a s m tri o b u u n ti t o s n to s F sp ir a s c t e , w us e i n jo g i n k t - l m y c e l a u n s s t . e F r o c r e l e ls a c fr h o o m m a i l c l s o l m ay i e c r s , l t a h y e e c rs e l i l n s i t n h e e a a c li h g n cl e u d s t c e e r l l a e re m a b g e g d r d eg in a g te d
into a metacell. The metacells are established as paired samples, based on which
qk ( u )=
W
1
k n
∑ N
=
k
1
w (n) q ( u|x (
k
n) ;ϕk ). By assigning appropriate weights to balance f
t
e
h
a
e
t u
Sp
re
e a
c
r
o
m
rr
a
e
n
la
’s
t i
c
o
o
n
r r
c
e
a
l
n
at
b
io
e
n
c
f
o
o
m
r
p
ea
u
c
te
h
d
e
.
d
U
g
s
e
i n
in
g
t
t
h
h
e
e
g
p
u
a
i
i
d
re
a
d
n c
m
e
e
g
t
r
a
a
c
p
e
h
ll
.
s ,
T
w
h
e
e
t
i
h
n
e
te
n
g
c
ra
o
t
m
io
p
n
u te
the cell distributions across different layers, the optimum of qi ( u )= qj ( u ) ,∀i̸= j consistency score is defined as the average correlation across all graph edges,
could be much closer to the desired alignment. negated per edge sign and weighted by edge weight.
To obtain the balancing weights in an unsupervised manner, we devised the
following two-stage training procedure. First, we pretrain the GLUE model with Systematic benchmarks. UnionCom23, Pamona24 and GLUE were executed using
constant weight w (n)= 1, during which noise ϵ∼N( ϵ;0,Σ ) was added to the the Python packages ‘unioncom’ (v.0.3.0), ‘Pamona’ (v.0.1.0) and ‘scglue’ (v.0.2.0),
cell embeddings before passing to the discriminator. We set ∑ to be 1.5× the respectively. MMD-MA25 was executed using the Python script provided at
empirical variance of cell embeddings in each minibatch, which helps produce a https://bitbucket.org/noblelab/2020_mmdma_pytorch. Online iNMF16, LIGER17,
coarse alignment immune to composition imbalance. Then, we cluster the coarsely Harmony18, bindSC33, and Seurat v3 (ref. 15) were executed using the R packages
aligned cell embeddings per omics layer using Leiden clustering. The balancing ‘rliger’ (v.1.0.0), ‘rliger’ (v.1.0.0), ‘harmony’ (v.0.1.0), ‘bindSC’ (v.1.0.0) and ‘Seurat’
weight w for cells in cluster i is computed as: (v.4.0.2), respectively. For each method, we used the default hyperparameter
i
settings and data preprocessing steps as recommended. For the scRNA-seq data,
( )
wi = ∑ ki ̸=kj ni f ui,uj (23) 2 tw ,0 o 0 0 se h p i a g r h a l t y e v s a ch ri e a m bl e e s g t e o n c e o s n w s e tr r u e c s t e t le h c e t e g d u i u d s a i n n c g e t h gr e a S p e h u . r I a n t t ‘v h s e t ’ s m tan et d h a o r d d . s W ch e e u m s e e , d
we connected ATAC peaks with RNA genes via positive edges if they overlapped
f(ui,uj )=
{cos(ui,uj )4,cos ( ui,uj ) >0.5
(24)
i
f
n
ro
e
m
it h
th
er
e
t
T
h
S
e
S
g
)
e
.
n
In
e b
an
o d
a
y
lt e
o
r
r
n
p
a
r
t
o
iv
x
e
i m
sc
a
h
l
e
p
m
ro
e
m
in
o
v
t
o
er
lv
r
i
e
n
g
g
i o
la
n
r
s
g e
(d
r
e
g
f
e
in
n
e
o
d
m
a
ic
s 2
w
k
in
b
d
u
o
p
w
st
s
r
,
e
w
a
e
m
0, otherwise connected ATAC peaks with RNA genes via positive edges if the peaks are within
150 kb of the proximal gene promoters; the edges were weighted by a power-law
where u i is the average cell embedding of cluster i, k i denotes the omics layer of function w =( d + 1 )−0.75 (d is the genomic distance in kb), which has been
cluster i, and n is the number of cells in cluster i. In other words, we sum up the proposed to model the probability of chromatin contact42,43. For the methods
i
cosine similarities (raised to the power of 4 to increase contrast) between cluster that require feature conversion (online iNMF, LIGER, bindSC and Seurat v.3), we
i and all its matching clusters in other layers with cosine similarity >0.5, and then converted the scATAC-seq data to gene-level activity scores by summing up counts
NatuRe BioteChNoloGy | www.nature.com/naturebiotechnology
NATUrE BioTEcHNoLoGy Articles
in the ATAC peaks connected to specific genes in the guidance graph. Notably, where s
(i)
is the omics layer silhouette width for the ith cell, N is the number
omicslayer j
online iNMF and LIGER also recommend an alternative way of ATAC feature of cells in cell type j, and M is the total number of cell types. Omics layer ASW has a
conversion, that is, directly counting ATAC fragments falling in gene body and range of 0 to 1, and higher values indicate better mixing.
promoter regions without resorting to ATAC peaks (https://htmlpreview.github. Graph connectivity (GC) was also used to evaluate the extend of mixing among
io/?https://github.com/welch-lab/liger/blob/master/vignettes/Integrating_scRNA_ omics layers and was defined as in a recent benchmark study73:
and_scATAC_data.html), which we abbreviate to FiG (fragments in genes). We
a w l h so e n te e s v t e e r d a t p h p e l i F c i a G b l f e e . ature conversion method with online iNMF and LIGER GC = M 1 j ∑ = M 1 |LC N C j j | (36)
Mean average precision (MAP) was used to evaluate the cell type resolution.
Supposing that the cell type of the ith cell is y(i) and that the cell types of its K where LCC j is the number of cells in largest connected component of the cell
ordered nearest neighbors are y (i) ,y (i) ,…,y (i), the mean average precision is then k-nearest neighbors graph (K = 15) for cell type j, N j is the number of cells in cell
defined as follows: 1 2 K type j and M is the total number of cell types. Graph connectivity has a range of 0 to
1, and higher values indicate better mixing.
MAP = 1 ∑ N AP (i) (28)
N i=1 Omics mixing. Seurat alignment score, omics layer ASW and graph connectivity
all measure omics mixing of the data integration. Following the procedure from
the recent benchmark study73, we first conduct min-max scaling for each of the
AP (i)=   0 ∑
,
K k=11 y ∑ (i) K k= = 1 yk 1 · y ( ∑ i) k j= = 1 yk ( 1 i y ) ( k i)=y ( j i) ,
o
if
th
k ∑ =
e
K
r
1
w
1
i
y
s
(
e
i)=y ( k i) >0 (29) m sin e g tr le ic m s, e a t n r d ic t r h e o e p n m r e c i s c o e s m n m t p i i n u x g t i e n o t g m h = e i c a s v s m c e a r le i a ( x g S i e A n S g a ) : c + r s o c s al s e ( t o h m e i c t s
3
h la r y e e e r A t S o W s ) u + m sc m ale a ( r G i C z ) e them into ( a 3 7)
where 1 y (i)=y ( k i) is an indicator function that equals 1 if y (i)= y ( k i) and 0 otherwise. O we v i e g r h a t ll b in et t w eg e r e a n ti o b n io s l c o o g r y e . c T o o n s c e o r m va p t u io t n e a a n n d o v o e m ra i l c l s i n m te ix g i r n a g ti , o f n ol s lo c w or i e n , g w t e h e u s r e e c a e 6 n : t 4
For each cell, average precision (AP) computes the average cell type precision up to benchmark study73:
each cell type-matched neighbor, and mean average precision is the average average
precision across all cells. We set K to 1% of the total number of cells in each dataset. overallintegrationscore = 0.6×biologyconservation + 0.4×omicsmixing
Mean average precision has a range of 0 to 1, and higher values indicate better cell (38)
type resolution.
Cell type ASW (average silhouette width) was also used to evaluate the cell type FOSCTTM25 was used to evaluate the single-cell level alignment accuracy. It
resolution, which was defined as in a recent benchmark study73: was computed on two datasets with known cell-to-cell pairings. Suppose that each
dataset contains N cells, and that the cells are sorted in the same order, that is, the
celltypeASW = 1 2 ( ∑ N i=1 N sc ( e i l ) ltype + 1 ) (30) i x t h a n c d el y l i a n s t t h h e e f c ir e s ll t e d m at b a e se d t d i i s n p g a s i o re f d th w e i f t i h r s t t h a e n i d th s e c c e o ll n in d d th a e ta s s e e c t o , n re d s p d e a c ta ti s v e e t l . y D . T e h n e o te
FOSCTTM is then defined as:
where s ( ce i) lltype is the cell type silhouette width for the ith cell, and N is the total FOSCTTM = 1 ( ∑ N n ( 1 i) +∑ N n ( 2 i)) (39)
number of cells. Cell type ASW has a range of 0 to 1, and higher values indicate 2N i=1 N i=1 N
better cell type resolution.
Neighbor consistency (NC) was used to evaluate the preservation of
single-omics data variation after multi-omics integration and was defined n ( 1 i)=(cid:31) (cid:31) (cid:30)j|d(cid:29)xj,yi (cid:28)<d ( xi,yi )(cid:27)(cid:31) (cid:31) (40)
following a previous study74:
where NNS(i) is the set of k-n N ea C re = st n N 1 ei i ∑ = g N h 1 b (cid:31) (cid:31) (cid:31) (cid:31) (cid:31) (cid:31) o N N r N N s S S f ( ( o i i ) ) r ∩ ∪ c N N e N N ll I I ( ( i i i ) ) in (cid:31) (cid:31) (cid:31) (cid:31) (cid:31) (cid:31) the single-omics data, (31) w re h sp er e e c t n iv ( 1 e i) l y a , n t d h a n t ( 2 a i) r a e r c e l o th se e n r n ( 2 t i u ) o m = th b e e (cid:31) (cid:31) (cid:30) r it j o h | f d c c e (cid:29) e l x l l l i t s , h y i a n j (cid:28) n t h t < h e e d f i i r ( r x s t t r i , u a y n e i d ) m (cid:27) s a (cid:31) (cid:31) e t c c o h n e d s i d n a t t h as e e o t, p posite (41)
NNI(i) is the set of K-nearest neighbors for the ith cell in the integrated space, and dataset. d is the Euclidean distance. FOSCTTM has a range of 0 to 1, and lower
N is the total number of cells. We set K to 1% of the total number of cells in each values indicate higher accuracy.
dataset. Neighbor consistency has a range of 0 to 1, and higher values indicate Feature consistency was used to evaluate the consistency of feature embeddings
better preservation of data variation. from different models. Since the raw embedding spaces are not directly comparable
across models, we defined the consistency as the cross-modal conservation of
Biology conservation. Mean average precision, cell type ASW and neighbor cosine similarities among features in the same model. Specifically, we first randomly
consistency all measure biology conservation of the data integration. Following subsample 2,000 features and compute the pairwise cosine similarity among them
the procedure from the recent benchmark study73, we first conduct min-max using feature embeddings from the two compared models. The feature consistency
scaling for each of the metrics and then compute the average across the three to score is then defined as the Pearson’s correlation between the cosine similarities of
summarize them into a single metric representing biology conservation: two models, averaging across four random subsamples. Feature consistency has a
range of −1 to 1, and higher values indicate higher consistency.
biologyconservation = scale(MAP)+scale(cell 3 typeASW)+scale(NC) (32) For the baseline benchmark, each method was run eight times with different
random seeds, except for Harmony and bindSC that have deterministic
Seurat alignment score (SAS) was used to evaluate the extent of mixing among implementations and were run only once. For the guidance corruption benchmark,
omics layers and was computed as described in the original paper75: we removed the specified proportions of existing peak–gene interactions
SAS = 1− K ¯x− −N K K (33) a in n t d e r a a d c d ti e o d n s e q re u m al a n in u e m d b u e n rs c h o a f n n g o e n d e . x O is f t e n n o t t e in , t f e e r a a tu ct r i e o c n o s, n s v o e r t s h i e o n to w ta a l s n a u ls m o b r e e r p o ea f ted
N using the corrupted guidance graphs. The corruption procedure was repeated
where ¯ x is the average number of cells from the same omics layer among the eight times with different random seeds. For the subsampling benchmark, the
K-nearest neighbors (different layers were first subsampled to the same number scRNA-seq and scATAC-seq cells were subsampled in pairs (so FOSCTTM could
of cells as the smallest layer), and N is the number of omics layers. We set K to 1% still be computed). The subsampling process was also repeated eight times with
of the subsampled cell number. Seurat alignment score has a range of 0 to 1, and different random seeds.
higher values indicate better mixing. For the systematic scalability test (Supplementary Fig. 17a), all methods were
Omics layer ASW was also used to evaluate the extend of mixing among omics run on a Linux workstation with 40 CPU cores (two Intel Xeon Silver 4210 chips),
layers and was defined as in a recent benchmark study73: 250 GB of RAM and NVIDIA GeForce RTX 2080 Ti graphical processing units.
Only a single graphical processing unit card was used when training GLUE.
omicslayerASW = M 1 j ∑ = M 1 omicslayerASWj (34) Triple-omics integration. The scRNA-seq and scATAC-seq data were handled as
previously described (section Systematic benchmarks). Due to low coverage per
single-C site, the snmC-seq data were converted to average methylation levels in
omicslayerASWj =
N
1
j i
(cid:31)
=
Nj
1
1−(cid:30) (cid:30)
(cid:30)
s (
om
i)
icslayer
(cid:30) (cid:30)
(cid:30)
(35) g
tw
en
o
e
f e
b
a
o
t
d
u
i
r
e
e
s
s
.
p
T
e
h
r
e
g
m
en
C
e
H
. T
a
h
n
e
d
g e
m
n
C
e
G
m e
le
t
v
h
e
y
l
l
s
a t
w
io
e
n
re
l e
q
v
u
e
a
l
n
s
t
w
if
e
ie
re
d
n
se
o
p
rm
ar
a
at
li
e
z
l
e
y,
d
r
b
es
y
u
t
l
h
ti
e
n
g
g
l
i
o
n
b al
NatuRe BioteChNoloGy | www.nature.com/naturebiotechnology
Articles NATUrE BioTEcHNoLoGy
methylation level per cell. An initial dimensionality reduction was performed using network based on the scRNA-seq data, and then uses external cis-regulatory
PCA (section Implementation details). For the triple-omics guidance graph, the mCH evidence to filter out false positives. SCENIC accepts cis-regulatory evidence in
and mCG levels were connected to the corresponding genes with negative edges. the form of gene rankings per TF, that is, genes with higher TF enrichment levels
The normalized methylation levels were positive, with dropouts corresponding in their regulatory regions are ranked higher. To construct the rankings based
to the genes that were not covered in single cells. As such, we used the zero-inflated on our inferred peak–gene interactions, we first overlapped the ENCODE TF
log-normal (ZILN) distribution for the data decoder: chromatin immunoprecipitation (ChIP) peaks77 with the ATAC peaks and counted
the number of ChIP peaks for each TF in each ATAC peak. Since different genes
p ( xk |u,V;θk )= i∈ ∏ V
k
ZILN(xki ;μ i ,σi,δi ) (42) c
in
a n
le
h
n
a
g
v
t
e
h
d
(l
i
o
ff
n
e
g
re
e
n
r
t
p
n
e
u
ak
m
s
b
c
e
a
r
n
s
c
o
o
f
n
c
t
o
a
n
in
n e
m
ct
o
e
r
d
e
A
C
T
h
A
IP
C
p
p
e
e
a
a
k
k
s
s
b
,
y
an
c
d
h a
th
n
e
c e
A
),
T
w
A
e
C
d
p
e
e
v
a
is
k
e
s
d
v
a
a ry
sampling-based approach to evaluate TF enrichment. Specifically, for each gene,
ZILN(xki ;μ
i
,σi,δi )=  xki 1 σ − i √δi 2π exp ( − ( logx 2 k σ i − 2 i μi )2) ,xki >0 (43) w p
C
e
h
e a
I
r k
P
a s n
p
i d n
e
o
a
b m
k
o
s
l t y
i
h
n
s n a
t
u
h
m m
e
p
s
b
e
le e
r
d r
a n
1 an ,
d
0 d
o
0
m
0 le s n
A
e g t
T
t s
A
h o
C
d f i A
p
st T
e
r
a
A ib
k
C u
s
t
a
p io
s
e n a
n
k .
u
W s
l l
t e
d
h
i
a c
s
t o
t r
m u
i
n
b
a t
u
t e c
t
d
i
h
o
e t
n
h d
s
e
.
t h
F
n e
o
u
r
m c o
e
b n
a
e
c
n r
h
e s c
T
o te
F
f d T
i n
F A T
ea
A
c
C
h
δi,
xki
=
0 gene, an empirical P value could then be computed by comparing the observed
number of ChIP peaks to the null distribution. Finally, we ranked the genes by
the empirical P values for each TF, producing the cis-regulatory rankings used by
μ i = α⊙V ⊤ k u + β (44) SCENIC. Since peak–gene-based inference is mainly focused on remote regulatory
regions, proximal promoters could be missed. As such, we provided SCENIC with
where μ∈R|Vk| ,σ∈R + |Vk| ,δ∈( 0,1 )|Vk| are the log-scale mean, log-scale both the above peak-based and proximal promoter-based cis-regulatory rankings.
standard deviation and zero-inflation parameters of the zero-inflated log-normal
distribution, respectively, and α∈R + |Vk| ,β∈R|Vk| are scaling and bias factors. Integration for the human multi-omics atlas. The scRNA-seq and scATAC-seq
To unify the cell type labels, we performed a nearest neighbor-based label atlases have highly unbalanced cell type compositions, which are primarily caused
transfer with the snmC-seq dataset as a reference. The five nearest neighbors in by differences in organ sampling sizes (Supplementary Fig. 17b). Although cell
snmC-seq were identified for each scRNA-seq and scATAC-seq cell in the aligned types are unknown during real-world analyses, organ sources are typically available
embedding space, and majority voting was used to determine the transferred label. and can be used to help balance the integration process. To perform organ-balanced
To verify whether the alignment was correct, we tested for significant overlap in data preprocessing, we first subsampled each omics layer to match the organ
cell type marker genes. The features of all omics layers were first converted to compositions. For the scRNA-seq data, 4,000 highly variable genes were selected
genes. Then, for each omics layer, the cell type markers were identified using the using the organ-balanced subsample. Then, for the initial dimensionality reduction,
one-versus-rest Wilcoxon rank-sum test with the following criteria: FDR < 0.05 we fitted PCA (scRNA-seq) and LSI (scATAC-seq) on the organ-balanced
and log fold change >0 for scRNA-seq/scATAC-seq; FDR < 0.05 and log fold subsample and applied the projection to the full data. The PCA/LSI coordinates
change of <0 for snmC-seq. The significance of marker overlap was determined by were used as the first transformation layer in the GLUE data encoders (section
the three-way Fisher’s exact test40. Implementation details), as well as for metacell aggregation (below). The guidance
To perform correlation and regression analysis after the integration, we graph was constructed as described previously (section Systematic benchmarks).
clustered all cells from the three omics layers using fine-scale k-means (k = 200). The two atlases consist of large numbers of cells but with low coverage per
Then, for each omics layer, the cells in each cluster were aggregated into a cell. To alleviate dropout and increase the training speed simultaneously, we used
metacell by summing their expression/accessibility counts or averaging their DNA a metacell aggregation strategy during pretraining. Specifically, in the pretraining
methylation levels. The metacells were established as paired samples, based on stage, we clustered the cells in each omics layer using fine-scaled k-means
which feature correlation and regression analyses could be conducted. (k = 100,000 for scRNA-seq and k = 40,000 for scATAC-seq). To balance the organ
To integrate the same datasets using online iNMF, we inverted the snmC-seq compositions at the same time, k-means centroids were fitted on the previous
data via subtracting the data matrix by the largest entry, following the procedure organ-balanced subsample and then applied to the full data. The cells in each
described in the original paper16. k-means cluster were aggregated into a metacell by summing their expression/
accessibility counts and averaging their PCA/LSI coordinates. GLUE was then
GLUE-based cis-regulatory inference. To ensure consistency of cell types, we first pretrained on the aggregated metacells with additive noise, which roughly oriented
selected the overlapping cell types between the 10X Multiome and pcHi-C data. the cell embeddings but did not actually align them (section Weighted adversarial
The remaining cell types included T cells, B cells and monocytes. The eQTL data alignment). To better use the large data size, the hidden layer dimensionality was
were used as is, because they were not cell type-specific. For scRNA-seq, we selected doubled to 512 from the default 256. In the second stage, GLUE was fine-tuned
6,000 highly variable genes. To capture remote cis-regulatory interactions, the base on the full single-cell data with the balancing weight estimated as described in the
guidance graph was constructed for peak–gene pairs within a distance of 150 kb, section Weighted adversarial alignment. No metacell aggregation was used when
using the alternative scheme as described in the section Systematic benchmarks. comparing the scalability of different methods (Supplementary Fig. 17a).
To incorporate the regulatory evidence of pcHi-C and eQTL, we anchored all For a comparison with other integration methods, we also tried online iNMF
evidence to that between the ATAC peaks and RNA genes. A peak–gene pair was and Seurat v.3. Online iNMF was the only other method that could scale to
considered supported by pcHi-C if (1) the gene promoter was within 1 kb of a bait millions of cells, so we applied it to the full dataset. On the other hand, Seurat v.3
fragment, (2) the peak was within 1 kb of an other-end fragment and (3) significant showed the second-best accuracy in our previous benchmark. We also managed
contact was identified between the bait and the other-end fragment in pcHi-C. to apply it to the aggregated data used in the first stage of GLUE training, due to
The pcHi-C-supported peak–gene interactions were weighted by multiplying the the fact that Seurat v.3 could not scale to the full dataset (Supplementary Fig. 17a).
promoter-to-bait and the peak-to-other-end power-law weights (above). If a peak– Label transfer was performed using the same procedure as in the triple-omics case,
gene pair was supported by multiple pcHi-C contacts, the weights were summed except that we used majority voting in 50 nearest neighbors.
and clipped to a maximum of 1. A peak–gene pair was considered supported by
eQTL if (1) the peak overlapped an eQTL locus and (2) the locus was associated Reporting Summary. Further information on research design is available in the
with the expression of the gene. The eQTL-supported peak–gene interactions were Nature Research Reporting Summary linked to this article.
assigned weights of 1. The composite guidance graph was constructed by adding
the pcHi-C- and eQTL-supported interactions to the previous distance-based Data availability
interactions, allowing for multi-edges.
All datasets used in this study are already published and were obtained from public
For regulatory inference, only peak–gene pairs within 150 kb in distance were
data repositories. See Supplementary Table 1 for detailed information on single-cell
considered. The GLUE training process was repeated four times with different
omics datasets used in this study, including access codes and URLs. For regulatory
random seeds. For each repeat, the peak–gene regulatory score was computed
inference and evaluation, the pcHi-C data was obtained from supplementary file
as the cosine similarity between the feature embeddings. The final regulatory
of the original publication (https://www.sciencedirect.com/science/article/pii/
inference was obtained by averaging the regulatory scores across the four repeats.
S0092867416313228), eQTL data from GTEx v8 (https://www.gtexportal.org/
To evaluate the significance of the regulatory scores, we compared the scores to
home/datasets), TF ChIP–seq data from ENCODE data portal (https://www.
a NULL distribution obtained via randomly shuffled feature embeddings and
encodeproject.org/) and TRRUST v2 database from the official website (https://
computed empirical P values as the probability of getting more extreme scores in
www.grnpedia.org/trrust/downloadnetwork.php). All benchmarking source data
the NULL distribution. Finally, we compute FDR of regulatory inference based on
are available in Supplementary Data 1.
the P values using the Benjamini–Hochberg procedure. For cis-regulatory inference
using LASSO, we used hyperparameter α = 0.01, which was optimized for area
under the receiver operating characteristic curves of pcHi-C and eQTL prediction. Code availability
The GLUE framework was implemented in the ‘scglue’ Python package, which is
TF-target gene regulatory inference. We used the SCENIC workflow76 to available at https://github.com/gao-lab/GLUE. For reproducibility, the scripts for
construct a TF-gene regulatory network from the inferred peak–gene regulatory all benchmarks and case studies were assembled using Snakemake (v.6.12.3), which
interactions. Briefly, the SCENIC workflow first constructs a gene coexpression is also available in the above repository.
NatuRe BioteChNoloGy | www.nature.com/naturebiotechnology
NATUrE BioTEcHNoLoGy Articles
References comments during the study, as well as authors of the datasets used in this work for
68. Ding, J. & Regev, A. Deep generative model embedding of single-cell their kindly help. This work was supported by funds from the National Key Research
RNA-seq profiles on hyperspheres and hyperbolic spaces. Nat. Commun. 12, and Development Program (grant no. 2016YFC0901603), the State Key Laboratory
2554 (2021). of Protein and Plant Gene Research and the Beijing Advanced Innovation Center for
69. Mikolov, T., Sutskever, I., Chen, K., Corrado, G. & Dean, J. in Advances in Genomics at Peking University, as well as the Changping Laboratory. The research by
Neural Information Processing Systems (eds. Burges, C. J. C. et al.) 3111–3119 G.G. was supported in part by the National Program for Support of Top-notch Young
(Curran Associates, Inc., 2013). Professionals. Part of the analysis was carried out on the Computing Platform of the
70. Kipf, T. N. & Welling, M. Semi-supervised classification with graph Center for Life Sciences of Peking University and supported by the High-performance
convolutional networks. In Proc. 5th International Conference on Learning Computing Platform of Peking University. Parts of Fig. 1 were created using an image set
Representations (eds. Bengio, Y. & LeCun, Y.) (ICLR, 2017). downloaded from Servier Medical Art (https://smart.servier.com/, CC BY 3.0).
71. Dincer, A. B., Janizek, J. D. & Lee, S.-I. Adversarial deconfounding
autoencoder for learning robust gene expression embeddings. Bioinformatics author contributions
36, i573–i582 (2020). G.G. conceived the study and supervised the research. Z.J.C. designed and implemented
72. Goodfellow, I. et al. in Advances in Neural Information Processing Systems the computational framework and conducted benchmarks and case studies with
(eds Ghahramani, Z. et al.) 2672–2680 (Curran Associates, Inc., 2014). guidance from G.G. Z.J.C. and G.G. wrote the manuscript.
73. Luecken, M. D. et al. Benchmarking atlas-level data integration in single-cell
genomics. Nat. Methods 19, 41–50 (2022). Competing interests
74. Xu, C. et al. Probabilistic harmonization and annotation of single-cell
transcriptomics data with deep generative models. Mol. Syst. Biol. 17, The authors declare no competing interests.
e9620 (2021).
75. Butler, A., Hoffman, P., Smibert, P., Papalexi, E. & Satija, R. Integrating additional information
single-cell transcriptomic data across different conditions, technologies, and
Extended data are available for this paper at https://doi.org/10.1038/
species. Nat. Biotechnol. 36, 411–420 (2018).
s41587-022-01284-4.
76. Aibar, S. et al. SCENIC: single-cell regulatory network inference and
clustering. Nat. Methods 14, 1083–1086 (2017). Supplementary information The online version contains supplementary material
77. Davis, C. A. et al. The encyclopedia of DNA elements (ENCODE): data portal available at https://doi.org/10.1038/s41587-022-01284-4.
update. Nucleic Acids Res. 46, D794–D801 (2018). Correspondence and requests for materials should be addressed to Ge Gao.
Peer review information Nature Biotechnology thanks Ricard Argelaguet, Yun Li,
acknowledgements Romain Lopez and the other, anonymous, reviewer(s) for their contribution to the
peer review of this work.
We thank F. Tang, X.S. Xie, Z. Zhang, L. Tao, C. Li, J. Lu (at Peking University) and Y.
Ding (at the Beijing Institute of Radiation Medicine) for their helpful discussions and Reprints and permissions information is available at www.nature.com/reprints.
NatuRe BioteChNoloGy | www.nature.com/naturebiotechnology
Articles NATUrE BioTEcHNoLoGy
Extended Data Fig. 1 | individual metrics for evaluating integration performance. a, Mean average precision vs. Seurat alignment score for different
integration methods. Higher mean average precision indicates higher cell type resolution, and higher Seurat alignment score indicates better omics mixing.
b, Cell type vs. omics layer average silhouette width for different integration methods. Higher cell type average silhouette width indicates higher cell type
resolution, and higher omics layer average silhouette width indicates better omics mixing. c, Neighbor conservation vs. graph connectivity for different
integration methods. Higher neighbor conservation indicates better conservation of manifold structure in each original layer, and higher graph connectivity
indicates better omics mixing. n=8 repeats with different model random seeds. the error bars indicate mean ± s.d.
NatuRe BioteChNoloGy | www.nature.com/naturebiotechnology
