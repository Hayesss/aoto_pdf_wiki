---
source_path: /mnt/c/Users/Administrator/Zotero/storage/KW7R4J2I/Zappia 等 - 2025 - Feature selection methods affect the performance of scRNA-seq data integration and querying.pdf
ingested: 2026-04-23
sha256: 6135616c82e3e705
---

nature methods
Registered Report https://doi.org/10.1038/s41592-025-02624-3
Feature selection methods affect the
performance of scRNA-seq data integration
and querying
Received: 7 June 2023 Luke Zappia 1,2, Sabrina Richter1, Ciro Ramírez-Suástegui1,3,
Raphael Kfuri-Rubens 1,4,5, Larsen Vornholz 1, Weixu Wang1,
Accepted: 8 February 2025
Oliver Dietrich 1,6, Amit Frishberg1, Malte D. Luecken 1,7 &
Published online: 13 March 2025 Fabian J. Theis 1,2,8
Check for updates
The availability of single-cell transcriptomics has allowed the construction
of reference cell atlases, but their usefulness depends on the quality
of dataset integration and the ability to map new samples. Previous
benchmarks have compared integration methods and suggest that feature
selection improves performance but have not explored how best to select
features. Here, we benchmark feature selection methods for single-cell
RNA sequencing integration using metrics beyond batch correction and
preservation of biological variation to assess query mapping, label transfer
and the detection of unseen populations. We reinforce common practice
by showing that highly variable feature selection is effective for producing
high-quality integrations and provide further guidance on the effect of the
number of features selected, batch-aware feature selection, lineage-specific
feature selection and integration and the interaction between feature
selection and integration models. These results are informative for analysts
working on large-scale tissue atlases, using atlases or integrating their own
data to tackle specific biological questions.
Single-cell transcriptomics technologies are now accessible to many remove technical differences while conserving interesting biological
biological researchers. As the number of single-cell RNA sequenc- variation. Good quality integration is especially critical for large-scale
ing (scRNA-seq) datasets has increased and analysis methods have human atlas-building enterprises, where fully capturing tissue hetero-
improved, we are seeing a shift from exploratory experiments toward geneity requires samples from a variety of individuals across locations,
multi-sample datasets. This trend includes more designed experiments collected in different ways from different organ areas and profiled using
investigating specific phenomena or testing differences between con- a range of protocols or technologies1.
ditions and larger efforts to catalog the cellular heterogeneity within Many computational scientists have tackled the integration prob-
tissues. More samples allow a deeper study of biology but present lem and at least 250 tools for single-cell integration are now available2.
additional challenges including successful integration of samples to Studies have evaluated the performance of some methods3–6, leading
1Institute of Computational Biology, Computational Health Center, Helmholtz Munich, Neuherberg, Germany. 2School of Computing, Information and
Technology, Technical University of Munich, Munich, Germany. 3Wellcome Sanger Institute, Wellcome Genome Campus, Hinxton, Cambridge, UK.
4School of Medicine, Technical University of Munich, Munich, Germany. 5Klinikum rechts der Isar, IIIrd Medical Department, Munich, Germany. 6Helmholtz
Institute for RNA-based Infection Research, Helmholtz Centre for Infection Research, Würzburg, Germany. 7Institute of Lung Health & Immunity,
Helmholtz Munich; Member of the German Center for Lung Research (DZL), Munich, Germany. 8School of Life Sciences Weihenstephan, Technical
University of Munich, Friesing, Germany. e-mail: fabian.theis@helmholtz-munich.de
Nature Methods | Volume 22 | April 2025 | 834–844 834
Registered Report https://doi.org/10.1038/s41592-025-02624-3
to a set of established metrics for assessing integration performance. a natural range of zero to the number of labels in the dataset, which are
While the methods have been compared, preprocessing steps that rescaled to be between zero and one, compressing the observed range
may affect integration have largely been overlooked. One step that so that even small differences can be informative. When considering the
has received some attention is feature selection, where benchmarks correlation of metrics with the number of selected features, we found
have shown that using highly variable genes generally leads to better that most metrics are positively correlated with the number of selected
integrations3; however, this study only considered one commonly features, with a mean correlation of around 0.5. A few metrics (local
used feature selection method. Unlike other analysis steps, such as structure14 and kNN correlation) showed stronger and more consist-
clustering7,8, the best feature selection approach for integration has ent associations with the number of features. In contrast, the mapping
not been assessed. Additional questions arise when considering how metrics are generally negatively correlated. This relationship could
the integrated space is used as a reference to analyze further query be because smaller feature sets produce noisier integrations where
samples. It is possible that selecting features could result in better cell populations are mixed. This scenario requires less-precise query
integration of reference samples while at the same time leading to an mapping where mapping somewhere within the mixed population is
integration model that is ignorant of alternative sources of biological sufficient to receive a high mapping score.
variation relevant to understanding other samples. The effect of technical factors of datasets on metric scores is more
This study assesses the impact of feature selection on integrating difficult to interpret as we consider relatively few datasets here, and
scRNA-seq samples and using the integrated reference to analyze query the factors are associated across datasets (a dataset with more cells
samples. We evaluate the performance of variants of over 20 feature typically has more batches and labels). We see that more complex
selection methods using a range of metrics divided into five categories: datasets generally result in lower scores for all metrics (Extended Data
batch effect removal, conservation of biological variation, quality of Fig. 3). The exceptions to this are the Milo15 and Uncertainty metrics.
query to reference mapping, label transfer quality and ability to detect For Milo, it is difficult to say if the positive association between scores
unseen populations (Extended Data Fig. 1). The results from our robust and technical factors is a general effect of having more data or an effect
benchmarking pipeline (Extended Data Fig. 2) are informative for of individual features. In the case of the Uncertainty metric, it is likely
researchers integrating their own datasets or creating reference atlases, that the classifier model used is not well calibrated and is less certain
leading to better community resources and further biological insights. (giving higher scores) for more complex datasets regardless of any
The study was conducted in accordance with the registered, peer- specific technical factor. Proper assessment of the effect of technical
reviewed protocol at https://doi.org/10.6084/m9.figshare.24995690.v1 dataset features would require more datasets where each factor is
(ref. 9). Except for pre-registered and approved pilot data, all anal ysis varied independently, potentially through a simulation study.
results reported in the paper were collected after the date of the regis- Perhaps the most important consideration for metric selection
tered protocol publication. is the correlation between metrics (Fig. 1b and Extended Data Fig. 3).
We want metrics that measure different aspects of integration and
Results query mapping and selecting several highly correlated metrics would
Metric selection is critical for reliable benchmarking bias our results in that direction. This effect is evident in the Integra-
For this study, we collected a wide variety of metrics covering different tion (Bio) category where several metrics (adjusted Rand index (ARI),
aspects of integration and query mapping. While measuring a broad batch-balanced ARI (bARI)16, normalized mutual information (NMI),
range of factors is important, the behavior of many of these metrics has batch-balanced NMI (bNMI)16, cLISI, label average silhouette width
not been thoroughly characterized. This characterization is particularly (Label ASW)3 and Local structure) are highly correlated with each
important in our context as we use metrics developed to compare dif- other, prompting us to select only a subset of these. The classification
ferent integration approaches to instead assess the effect of feature metrics show even stronger correlations, with all metrics having similar
selection methods. For this reason, we include a metric selection step scores. Here, we also selected a representative sample of metrics, but
to profile metrics and decide which to use for benchmarking. This using only one or all metrics would have little effect on the results. The
step aims to select metrics that effectively measure performance, are other consideration for metric correlations is the correlation between
not overly associated with technical factors and are nonredundant. metric types. To aid interpretation, we want to be able to summarize
We performed the metric selection using random and highly vari- these aspects individually, and correlations between opposing metric
able (scanpy10 implementation of a Seurat algorithm11) feature sets of types make this difficult. This categorization is difficult for the case of
different sizes for each dataset, performing integration and mapping, the kBET metric17, which is placed in the Integration (Batch) category
calculating metric scores and comparing the results (Fig. 1a). The but is also correlated with metrics that measure the conservation of
observed range of scores was calculated using the random gene sets biological variation. While this may be desirable for a single metric,
for each dataset–integration combination. We also used random sets including kBET in our study would confuse the signal between those
to calculate the correlation between metrics and technical aspects of categories. Another metric that stands out is graph connectivity3, which
datasets (number of features, number of reference cells, number of ref- was considered a batch correction metric by the original authors but is
erence labels and batches, number of query cells and number of query negatively correlated with other metrics in this category and positively
batches and unseen labels). We calculated the correlation between correlated with Integration (Bio) metrics. We have kept this metric
metric scores and the number of selected features using the highly for the evaluation but include it in the Integration (Bio) category in all
variable feature sets as random feature sets do not have any inherent further analyses.
ordering (the first 100 features are no more informative than the next Based on this analysis we selected three Integration (Batch) met-
100). An ideal metric would accurately measure what it is designed for, rics (batch principal-component regression (Batch PCR)3, cell-specific
returning scores across its whole output range that are independent of mixing score (CMS) and integration local inverse Simpson’s index
technical features of the data and are orthogonal to other metrics in the (iLISI)13), six Integration (Bio) metrics (isolated label ASW3, isolated
study. Figure 1b shows a summary of the metric evaluation. label F1 (ref. 3), bNMI, cLISI, local density factor difference (ldfDiff)18
Using these results, we selected metrics to evaluate feature and graph connectivity), four mapping metrics (Cell distance12, Label
selection methods. We found that some metrics, such as batch aver- distance12, mapping local inverse Simpson’s index (mLISI)12 and query
age silhouette width (Batch ASW)3 and k-nearest neighbors (kNN) local inverse Simpson’s index (qLISI)12), three classification metrics (F1
correlation12, showed little variation, even across a wide range of (Macro), F1 (Micro) and F1 (Rarity)19) and three unseen population met-
selected feature sets; however, this is not always easy to interpret. For rics (Milo, Unseen cell distance and Unseen label distance). Extended
example, the cell-type local inverse Simpson’s index (cLISI)13 metric has Data Table 1 gives our reasoning for excluding metrics.
Nature Methods | Volume 22 | April 2025 | 834–844 835
Registered Report https://doi.org/10.1038/s41592-025-02624-3
a
Evaluate
Observed range
Select features
Correlation with
Random Calculate metrics
dataset features
Select metrics
Correlation
Datasets between metrics
Highly variable Correlation with
Calculate metrics
genes number of features
b
Batch PCR
CMS
Graph connectivity
iLISI
Batch ASW
Mixing
kBET
Isolated label ASW
Isolated label F1
bNMI
cLISI
ldfDiff
ARI
Cell cycle
Label ASW
Local structure
NMI
bARI
Cell distance
Label distance
mLISI
qLISI
Reconstruction
kNN correlation
F1 (macro)
F1 (micro)
F1 (rarity)
AUPRC
Accuracy
Jaccard index (macro)
Jaccard index (micro)
Jaccard index (rarity)
MCC
Milo
Unseen cell distance
Unseen label distance
Uncertainty
Included?
Mean correlation Mean feature Mean metric Correlation
Included Mean range with num. features correlation correlation s.d.
Included as
other type
Excluded 0 0.250.500.751.00 −1.0−0.5 0 0.5 1.0 −1.0−0.5 0 0.5 1.0 −1.0−0.5 0 0.5 1.0 0.1 0.2 0.3 0.4 0.5
Using baselines to effectively scale and summarize metrics sets) and 200 stably expressed features selected using the scSEGIndex
Individual metrics have different effective ranges and interact differ- method23 (as negative controls that should not capture signal) and
ently with datasets. To summarize and compare metric scores, they use single-cell variational inference (scVI)24 to integrate each dataset
need to be adjusted to have the same range for each dataset. We use a using the selected features. These methods are sufficiently diverse to
scaling approach based on baseline methods, similar to that used by the demonstrate the effective range of each metric and allow us to establish
Open Problems in Single-cell Analysis project20. We use four baseline baseline ranges for each dataset (Fig. 2a).
methods: all features, 2,000 highly variable features selected using We scaled the metric scores using the baseline ranges and aggre-
the batch-aware variant of the scanpy-Cell Ranger21 method (as a rep- gated them as shown in Fig. 2, using the scIB pancreas dataset3 as an
resentative commonly used approach suggested as good practice3,22), example. This dataset was also used in stage 1 of the registered report.
500 randomly selected features (scores averaged over five feature Along with the real baseline methods, we include theoretical ‘Good’ and
Nature Methods | Volume 22 | April 2025 | 834–844 836
0 52.0 05.0 57.0 00.1
Observed range
00.1− 05.0− 00.0 05.0 00.1
Correlation
with number
of features
serutaeF sllec
ecnerefeR
sehctab
ecnerefeR
slebal
ecnerefeR
sllec
yreuQ
sehctab
yreuQ
slebal
neesnU
Correlations
with dataset Integration Integration
Mapping Classification Unseen
features (batch) (bio)
RCP
hctaB
SMC ytivitcennoc
hparG
ISILi WSA
hctaB
gnixiM TEBk WSA
lebal detalosI
1F
lebal
detalosI
IMNb ISILc ffiDfdl IRA elcyc
lleC
WSA
lebaL
erutcurts
lacoL
IMN IRAb ecnatsid
lleC
ecnatsid
lebaL
ISILm ISILq noitcurtsnoceR noitalerroc
NNk
)orcam(
1F
)orcim(
1F
)ytirar(
1F
CRPUA ycaruccA )orcam(
xedni
draccaJ
)orcim(
xedni
draccaJ
)ytirar(
xedni
draccaJ
CCM oliM ecnatsid
llec
neesnU
ecnatsid
lebal
neesnU
ytniatrecnU
(batch)
(bio)
Mapping
Classification
Unseen
Integration
Integration
Correlations between metrics
Fig. 1 | Overview and results of the metric selection step. a, Diagram of the indicates the mean correlation, and the size of squares is the s.d. (larger points
metric selection workflow. b, Results of the metric selection step. Densities are less variable). The heatmap on the right shows the mean correlation between
for the observed range and correlation with the number of features across metrics grouped by metric type (Extended Data Fig. 3b). The color bar on the left
datasets and integrations are shown for each metric. Colors indicate the mean indicates which metrics were selected for the final benchmark. This indication is
value and vertical lines represent the median. The middle heatmap shows the continued as shaded areas in the other plots.
mean correlation with technical dataset features (Extended Data Fig. 3a). Color
Registered Report https://doi.org/10.1038/s41592-025-02624-3
1 Int. batch Int. bio 1 Mapping Class. Unseen
Overall = ×( + )+ ×( + + )
2 2 2 2 3 3 3
Reference Query
‘Bad’ methods that illustrate the behavior of methods that generally equal consideration to the different metric types. While the overall
perform well or poorly across metric types (in contrast to the baselines, scores are useful, we also present scores for each metric type in the
which each score highly on some metric types and lowly on others). The following sections.
raw metric scores are scaled relative to the minimum and maximum
baseline scores. After scaling, scores greater than one are possible if a The number of selected features affects performance
method outperforms all the baselines (the ‘Good’ theoretical example) In addition to the method used to select features, the number of
or negative scores are possible if a method performs worse than all selected features affects the success of integration and query map-
baselines (the ‘Bad’ theoretical example). The interpretability of scores ping. Evaluating different feature set sizes for every selection method
outside the reference range is an advantage of this scaling approach, would be ideal but computationally prohibitive. Instead, we tested
providing additional context to the scaled values. We calculated sum- different numbers of features for a set of commonly used methods
mary scores for each metric type by taking the mean of the scaled values from the Seurat and scanpy packages, as well as simple methods that
for that category. A final overall score is calculated as a weighted mean select the most expressed or variable features.
of category scores (Fig. 2b). Figure 3a shows standardized summary scores (z-scores for each
We chose this weighting scheme to give equal importance to inte- dataset and method combination), highlighting the trend with the
grating the reference and mapping of the query and, within those, number of features. We see different trends for categories that focus
Nature Methods | Volume 22 | April 2025 | 834–844 837
senilesab
laeR
)saercnap
BIcs(
a
F1 (macro) F1 (micro) F1 (rarity) Batch PCR CMS iLISI Graph connectivity
Fetal liver
HLCA
HLCA (epithelial)
HLCA (immune)
Human endoderm
NeurIPS
Reed breast
scEiaD
scIB pancreas
Splat
Isolated label ASW Isolated label F1 bNMI cLISI ldfDiff Cell distance Label distance
Fetal liver
HLCA
HLCA (Epithelial)
HLCA (immune)
Human endoderm
NeurIPS
Reed breast
scEiaD
scIB pancreas
Splat
mLISI qLISI Milo Unseen cell distance Unseen label distance 0 0.25 0.5 0.75 1 0 0.25 0.5 0.75 1
Fetal liver Baseline method Metric type
HLCA
HLCA (Epithelial)
HLCA (immune) Scanpy−Cell Ranger Integration (Batch)
Human endoderm (n = 2,000, batch = true)
NeurIPS Integration (Bio)
Reed s b c r E e i a a s D t All Mapping
scIB pancreas Random (n = 500) Classification
Splat
scSEGIndex Unseen populations
0 0.250.500.751.000 0.250.500.751.000 0.250.500.751.000 0.250.500.751.000 0.250.500.75 1.00
Metric value (higher is better)
b
1 Measure metrics 2 Scale using baselines 3 Average by metric type 4 Calculate overall score
‘Good’ method
Scanpy−Cell Ranger
(n = 2,000, batch = true)
All
Random
(n = 500)
scSEGIndex
‘Bad’ method
0 0.25 0.50 0.75 1.00 0 0.25 0.50 0.75 1.00 0 0.25 0.50 0.75 1.00 0 0.25 0.50 0.75 1.00
Value Scaled value Type mean value Overall score
Fig. 2 | Establishing baseline ranges and scaling and aggregating metrics. ‘Bad’ methods are shown. First, the metrics are measured, and then the values are
a, Baseline ranges for selected metrics. Each panel shows baseline scores for scaled using the baseline ranges. Scaled values greater than one or less than zero
all datasets for a single metric. Shaded areas colored by metric type show the are possible if a method performs better or worse than the baselines. Average
baseline ranges, and points show the values for individual baseline methods. scores for each metric type are computed, and the overall score is calculated as a
b, The process for scaling and aggregating metrics using the scIB pancreas weighted average of the category scores using the equation below.
dataset as an example. The real baseline methods and theoretical ‘Good’ and
Registered Report https://doi.org/10.1038/s41592-025-02624-3
Integration (Batch) Integration (Bio) Mapping Classification Unseen populations Overall
2
1
0
−1
−2
on batch correction than those that measure biological variation. The unseen populations (Extended Data Fig. 4). This pattern suggests that
Integration (Batch) score shows the highest values for small feature selecting features in these simple ways can return sets that capture
sets and decreases as the number of features increases. The mapping information well in the reference but not as well in the query compared
category shows a similar but less extreme trend, converging to the to more sophisticated methods.
mean value after around 500 features. The other categories show dif- We see more variation in the highest-scoring number of features
ferent patterns, increasing with the number of features before leveling when methods are averaged for each dataset (Fig. 3b and Extended
off (classification and unseen populations) or declining (Integration Data Fig. 4). The two datasets with the fewest cells (splat and scIB pan-
(Bio)). These patterns reflect that achieving high scores for batch creas) show different patterns. For the simulated splat dataset26, few
correction is possible by creating a noisy integrated embedding (a features are required to capture the variation present. In contrast, the
single noisy mass of cells). In this case, batches will be well mixed in the highest scores are associated with higher numbers of features for the
reference and the query, but there is no separation between cell types, scIB pancreas dataset. These differences reflect the properties of the
resulting in low scores for the other categories. Due to this effect, we two datasets, with the splat simulation producing data with less com-
gave a lower consideration to the Integration (Batch) category when plexity than a real dataset, whereas the scIB pancreas dataset contains
choosing the number of features. The overall score shows a similar data from several technologies that present a difficult integration
trend to the biological categories, with peak values between 500 and challenge. The larger fetal liver dataset also requires more features to
5,000 selected features. achieve high scores in the query categories, with the highest averages
While there are clear trends for each metric category, there is for the mapping and unseen population categories when all features
also significant variation. The following panels in Fig. 3 show mean are used. This trend suggests that feature sets selected from the refer-
standardized values for datasets band methods. We see that meth- ence do not capture information in the query for this dataset. While
ods are largely consistent across datasets Fig. 3c. The Seurat-VST25, less pronounced, this trend holds across all datasets, with more fea-
scanpy-SeuratV3 and scanpy-Seurat methods peak at slightly higher tures required to achieve high scores on the classification and unseen
numbers of features, whereas the statistic-Variance and statistic-Mean population categories compared to the Integration (Bio) category;
methods peak at lower numbers of features for Integration (Batch) and however, the performance of selecting all features shows a limit to
Integration (Bio) but higher numbers of features for classification and how much additional signal can be obtained. The number of features
Nature Methods | Volume 22 | April 2025 | 834–844 838
eulav
dezidradnatS
Datasets
Splat
scIB pancreas
scEiaD
Reed breast
NeurIPS
Human endoderm
HLCA (immune)
HLCA (epithelial)
HLCA
Fetal liver
001 002 005 000,1 000,2 000,5 000,01 000,51 llA 001 002 005 000,1 000,2 000,5 000,01 000,51 llA 001 002 005 000,1 000,2 000,5 000,01 000,51 llA 001 002 005 000,1 000,2 000,5 000,01 000,51 llA 001 002 005 000,1 000,2 000,5 000,01 000,51 llA 001 002 005 000,1 000,2 000,5 000,01 000,51 llA
a
b
c Methods
Statistic−Variance
Statistic−Mean
Seurat−VST
Seurat−scTransform
Seurat−Dispersion
Scanpy−SeuratV3
Scanpy−Seurat
Scanpy−Pearson
Scanpy−Cell Ranger
Number of selected features
Mean standardized s.d. of
value standardized values
−2 −1 0 1 0 0.5 1.0 1.5 2.0
Fig. 3 | Effect of the number of selected features on metric performance. each dataset (Extended Data Fig. 4a). Colors indicate mean standardized values
a, Metric values standardized by dataset and method across different numbers and sizes of squares show the s.d. (smaller squares are more variable). Methods
of features for each metric category and overall scores. Points show individual are ordered using hierarchical clustering. c, Similar heatmap to b but rows are
standardized values and large diamonds connected by lines show the mean for methods rather than datasets (Extended Data Fig. 4b).
each number of features. b, Heatmap of standardized values by metric type for
Registered Report https://doi.org/10.1038/s41592-025-02624-3
Overall Int. (Batch) Int. (Bio) Mapping Classification Unseen
Dataset Overall Integration Classification
(bio)
Baseline method Type
Mean Integration Mapping Unseen
(batch) populations
Nature Methods | Volume 22 | April 2025 | 834–844 839
0 52.0 05.0 57.0 00.1 0 4.0 8.0 0 5.0 0.1 5.1 0.1− 5.0− 0 5.0 0.1 0 4.0 8.0 2.1 0 5.0 0.1 5.1
Wilcoxon
Seurat−VST (n = 2,000)
Scanpy−SeuratV3 (n = 2,000, batch = false)
Scanpy−Seurat (n = 2,000, batch = true)
Scanpy−Seurat (n = 2,000, batch = false)
triku
Scanpy−SeuratV3 (n = 2,000, batch = true)
Scanpy−Cell Ranger (n = 2,000, batch = true)
Scanpy−Cell Ranger (n = 2,000, batch = false)
Seurat−MVP
Brennecke
Seurat−scTransform (n = 2,000)
Random (n = 2,000)
Scanpy−Pearson (n = 2,000, batch = false)
Seurat−dispersion (n = 2,000)
SingleCellHaystack
OSCA
Scanpy−Pearson (n = 2,000, batch = true)
Transcription factors
Hotspot
scPNMF
Random (n = 500)
NBumi
All Anticor
Statistic−variance (n = 2,000)
scry
DUBSstepR
Statistic−mean (n = 2,000)
scSEGIndex
llarevO )hctab(
noitargetnI
)oib(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
Mean ranks
Rank s.d.
0
3
6
9
12
Mean rank
10
20
30
scSEGIndex
Transcription factors Splat scPNMF
DUBSstepR
Anticor scIB pancreas
All
Sta S ti t s a t t ic is − t v ic a − r m ian ea c n e scEiaD
scry
Seurat−scTransform Reed breast Scanpy−Cell Ranger (Batch = false)
Scanpy−Seurat (batch = true)
Scanpy−Cell Ranger (batch = true) NeurIPS
Scanpy−Pearson (batch = true)
Scanpy−Pearson (batch = false)
OSCA Human endoderm
Hotspot
SingleCellHaystack
Seurat−MVP HLCA (immune)
Seurat−dispersion Scanpy−Seurat (bat B c r h e n = n f e a c ls k e e ) HLCA (epithelial)
Wilcoxon triku HLCA
NBumi
Seurat−VST Scanpy−SeuratV3 (batch = false) Fetal liver
Scanpy−SeuratV3 (batch = true)
Mean
Jaccard JI > 0.5 s.d.
index0 0.25 0.50 0.75 1.00 0 0.1 0.2
Number of selected features (log scale)
01 001 005 000,1 000,5 000,01
| All
|
Anticor
NBumi
Wilcoxon
triku
Transcription
factors
Seurat−MVP
DUBSstepR
001 002 005 000,1 000,2 000,5 000,01 000,02
a
b c d
Number of methods
5
10
15
20
25
Dataset
Fetal liver
HLCA
HLCA (epithelial)
HLCA (immune)
Human endoderm NeurIPS
Reed breast
scEiaD
scIB pancreas
Splat
e
Overall Integration (Batch) Integration (Bio) Mapping Classification Unseen populations
revil
lateF
talps SPIrueN tsaerb
deeR
)enummi(
ACLH
DaiEcs ACLH mredodne
namuH
)lailehtipe(
ACLH
saercnap
BIcs
revil
lateF
talps SPIrueN tsaerb
deeR
)enummi(
ACLH
DaiEcs ACLH mredodne
namuH
)lailehtipe(
ACLH
saercnap
BIcs
revil
lateF
talps SPIrueN tsaerb
deeR
)enummi(
ACLH
DaiEcs ACLH mredodne
namuH
)lailehtipe(
ACLH
saercnap
BIcs
revil
lateF
talps SPIrueN tsaerb
deeR
)enummi(
ACLH
DaiEcs ACLH mredodne
namuH
)lailehtipe(
ACLH
saercnap
BIcs
revil
lateF
talps SPIrueN tsaerb
deeR
)enummi(
ACLH
DaiEcs ACLH mredodne
namuH
)lailehtipe(
ACLH
saercnap
BIcs
revil
lateF
talps SPIrueN tsaerb
deeR
)enummi(
ACLH
DaiEcs ACLH mredodne
namuH
)lailehtipe(
ACLH
saercnap
BIcs
Batch aware −
standard
Scanpy−Seurat
Scanpy−Pearson 0.2
Scanpy−Cell Ranger
Scanpy−SeuratV3 0
−0.2
−0.4
Fig. 4 | Results of the benchmark of feature selection methods. a, Summary of with white borders. c, The number of features (on a log scale) selected by at least
10
method performance by metric type. Points show scores for individual datasets n methods (n = 25, 20, 15, 10 and 5) for each dataset. Colors indicate the number
and diamonds show the mean values (Extended Data Fig. 5a). Methods are sorted of methods. d, The number of features selected by different methods. Points are
by mean overall score, and baseline methods are indicated by gray shading. colored by dataset, and blue bars show the mean for each method. Only methods
Shaded areas show scores less than (red) or greater than (blue) the baseline range which automatically determine the number of features are shown. Most other
(0–1). Average rankings for each metric type are shown on the right, with color methods were set to select 2,000 features, as indicated by the red line, except
indicating mean rank and size s.d. (smaller is more variable) (Extended Data scPNMF, which uses 200 features. e, Heatmap of the relative performance of
Fig. 5b). b, Overlap of features selected by different methods. The heatmap shows batch-aware variants of scanpy methods. Colors show the difference in score
the mean Jaccard index (JI) between feature sets selected by different methods for each metric type on each dataset, with negative values (purple) indicating
(excluding random gene sets) (Extended Data Fig. 6). Sizes of squares indicate that the batch-aware variant performed worse than the standard approach and
the s.d. (smaller is more variable). Mean JI values greater than 0.5 are highlighted positive values (green) that it performed better.
Registered Report https://doi.org/10.1038/s41592-025-02624-3
at which the additional signal saturates is unclear and is likely to be these methods results from randomness in integration or metrics. The
different for each dataset as a function of the biological and technical scanpy-Seurat and Seurat-MVP methods also implement the same
diversity that is present. approach but the scanpy implementation allows specifying the num-
Based on this analysis, we used 2,000 features for most methods ber of features, while the Seurat implementation selects the number
in the following evaluation, as this number consistently produced of features dynamically using a threshold. There are also some differ-
high scores across datasets, methods and metric categories. Excep- ences in preprocessing steps, contributing to their lack of consistency.
tions to this are methods that dynamically select the number of fea- Despite the lack of high overlap between selected feature sets,
tures (Anticor27, DUBStepR28, NBumi29, Seurat-MVP11 and triku30) and we still see a core set of features selected by most methods, with
single-cell projective non-negative matrix factorization (scPNMF)31, between 500 and 1,000 features being selected by at least 20 methods
where the documentation recommends using fewer features than for most datasets (Fig. 4c). This consistency suggests that a subset
other methods for which we use 200 features. of features clearly contains information for a dataset and should be
crucial for effective integration and query mapping. That the remain-
Highly variable features and supervised methods perform well ing selected features are less likely to be shared between methods
After determining the number of features to use, we compared feature that have similar performance may result from redundancy in gene
selection methods. We were able to successfully run the majority of expression, with several genes carrying information about the same
methods on all datasets; however, NBumi failed to complete on the biological processes.
Reed breast dataset32 within 24 h, scPNMF, exceeded 400 GB of memory The number of features selected by dynamic methods (Fig. 4d)
or failed to complete in 24 h on the Human Lung Cell Atlas (HLCA)33, can also be related to performance. The Anticor method selects the
HLCA immune, HLCA epithelial, Human endoderm34 and Reed breast majority of features in each dataset and, therefore, performs similarly
datasets, and Anticor produced an unexpected error for the Human to using all features. DUBStepR uses the most complex procedure of
endoderm dataset. the methods compared here, resulting in very few selected features
Figure 4a shows the overall results for each metric category, sorted and low overall performance. However, DUBStepR scores relatively
by the mean overall score across datasets for scVI integration (Extended highly on biological metrics, suggesting that the features it selects
Data Fig. 5a). Several methods obtain similar average overall scores. are informative but insufficient to correct batch effects. The dynamic
The Wilcoxon method, the only method to select features using cell methods that perform well (Wilcoxon, triku and Seurat-MVP) select
labels, has the highest average overall score but is more variable across a number of features closer to the 2,000 features we chose to use for
datasets than other top-performing methods. This higher variability most methods. Seurat-MVP selects fewer than 2,000 features for all
suggests that supervised selection of features may not be effective for datasets and in comparison to scanpy-Seurat, which uses the same algo-
all datasets, even when the same labels are used for evaluation, and that rithm but is set to 2,000 features, Seurat-MVP has higher Integration
tuning the number of features selected using this approach could be (Batch) scores but similar Integration (Bio) performance. While fewer
required. The Seurat-VST method obtains the highest overall ranking features are adequate for integrating the reference, the additional
and several other highly variable feature selection methods also per- features included by scanpy-Seurat improve query classification and
form well with similar mean scores and more consistent performance unseen population detection.
than Wilcoxon. The other top-performing alternative method is triku, Feature selection can also be employed in a batch-aware fashion
which has similar overall scores to the highly variable selection meth- by selecting features for individual batches and combining the results,
ods but shows some bias toward batch correction over conserving typically by choosing the features selected for the most batches. The
biological variation. intuition behind this approach is that it avoids selecting features that
The lower-ranked methods show more variation in scores for vary between batches but not between biological states within a batch.
individual categories (Extended Data Fig. 5). In particular, the baseline To assess the effectiveness of this approach, we included batch-aware
random and scSEGIndex methods score very highly on the Integration variants of the scanpy methods. Figure 4e shows the difference in
(Batch) and mapping categories but poorly on the categories measur- performance for each dataset and metric type compared to standard
ing biological information. This effect demonstrates that it is easy to selection. We see significant differences in the summary scores for
obtain good mixing between batches by selecting features that only some scenarios, but this effect is inconsistent across either datasets or
contain noise and the importance of including metrics that measure metric types, and the differences in the overall score are relatively small.
the conservation of biological variation. Using a predefined list of For example, batch-aware selection improves the unseen population
transcription factors also produces a bias toward batch correction, score for the HLCA (Immune) dataset but is significantly worse for the
demonstrating that it is not sufficient for features to be biologically HLCA (Epithelial), Human endoderm and scIB pancreas datasets. The
important but that they must also be relevant to particular datasets. OSCA method also selects features in a batch-aware way but does not
Transcription factors are typically lowly expressed and therefore noisy. rank among the top-performing methods. While we do not rule out
Although the effect is less pronounced, some methods, such as OSCA35 batch-aware feature selection as a useful approach, we cannot identify a
and singleCellHaystack36, rank highly on Integration (Bio) but not on scenario where it is consistently more effective than selecting features
batch correction, with singleCellHaystack also scoring similarly to across batches.
the top methods on unseen population detection. The singleCell-
Haystack method uses Seurat-VST as a preprocessing step to create a Lineage-specific feature selection and integration
principal-component analysis (PCA) space where the final features are An open question in large-scale integration projects is whether to inte-
selected but these additional steps do not lead to better performance grate across the full diversity of cell states or to limit the complexity
than Seurat-VST alone. by subsetting to specific lineages or conditions. While we cannot fully
We see some overlap in selected features for most methods, but address this question here, we can investigate some aspects by consid-
there are very few combinations where the mean Jaccard index is ering the three versions of the HLCA dataset.
above 0.5 (Fig. 4b and Extended Data Fig. 6). One pair that stands out Figure 5a shows the rankings for all methods for each HLCA subset,
is Seurat-VST and scanpy-SeuratV3, which produce identical sets. This including the overall ranking and the ranking for each metric type. In
overlap is unsurprising, given that they are different implementations general, these follow the trends we observed when considering all
of the same method, but it is reassuring to see consistency between datasets, and we do not see any methods that consistently rank higher
packages using different programming languages. As the selected on the lineage subsets compared to the full dataset. To see whether
features are identical, any differences in performance we see between the similar rankings across subsets resulted from selecting similar
Nature Methods | Volume 22 | April 2025 | 834–844 840
Registered Report https://doi.org/10.1038/s41592-025-02624-3
Rank Jaccard index Mean proportion
5 10 15 20 25
feature sets, we computed the Jaccard index between selected features One motivation for lineage-specific feature selection is that it
(Fig. 5b). While there is some similarity in feature sets, the overlap is results in selecting more specific features for the cell types in that
not higher than we saw between all datasets. The Jaccard index tends to subset. To test this, we considered the published marker gene sets for
be lower for higher-ranking methods, suggesting that these methods the HLCA and calculated the proportion of these markers selected
can successfully adapt to each dataset. We also see that the overlap in by each method on each dataset subset. Figure 5c and Extended Data
selected features between the immune and epithelial subsets is less Fig. 7 show the mean proportion of selected markers across cell types
than with the full dataset. for each lineage in the full HLCA (endothelial, epithelial, immune and
Nature Methods | Volume 22 | April 2025 | 834–844 841
0 52.0 05.0 57.0 00.1 0 52.0 05.0 57.0 00.1
s.d. proportion
0 1.0 2.0
Milo score Difference
0 52.0 05.0 57.0 00.1 0.1− 5.0− 0.0 5.0 0.1
a b c
Overall Int. (Batch) Int. (Bio) Mapping Classification Unseen
d
lluF enummI lailehtipE lluF enummI lailehtipE lluF enummI lailehtipE lluF enummI lailehtipE lluF enummI lailehtipE lluF enummI lailehtipE
Wilcoxon
Seurat−VST (n = 2,000)
Scanpy−SeuratV3 (n = 2,000, batch = false)
Scanpy−Seurat (n = 2,000, batch = true)
Scanpy−Seurat (n = 2,000, batch = false)
triku
Scanpy−SeuratV3 (n = 2,000, batch = true)
Scanpy−Cell Ranger (n = 2,000, batch = true)
Scanpy−Cell Ranger (n = 2,000, batch = false)
Seurat−MVP
Brennecke
Seurat−scTransform (n = 2,000)
Random (n = 2,000)
Scanpy−Pearson (n = 2,000, batch = false)
Seurat−dispersion (n = 2,000)
SingleCellHaystack
OSCA
Scanpy−Pearson (n = 2,000, batch = true)
Transcription factors
Hotspot
scPNMF
Random (n = 500)
NBumi
All
Anticor
Statistic−variance (n = 2,000)
scry
DUBSstepR
Statistic−mean (n = 2,000)
scSEGIndex
.mmI
sv
lluF
.ipE
sv
lluF
.mmI
sv
.ipE
Endothelial Epithelial Immune Stroma
lluF enummI lailehtipE lluF enummI lailehtipE lluF enummI lailehtipE lluF enummI lailehtipE
Full Immune Epithelial
sllec
B
sllec
tsaM
hpM
raloevlA
+3LCC 2CD )lasan(
bulC
suocum
GMS
suores
GMS
)laihcnorb( suores
GMS
)lasan( telboG )latnemgesbus( detailicitluM )lasan( elcsum
htoomS
etycorea
CE
yrallipac elcsum
htoomS
+D38MAF laihcnorbireP stsalborbif sllec
B
sllec
tsaM
hpM
raloevlA
+3LCC 2CD )lasan(
bulC
suocum
GMS
suores
GMS
)laihcnorb( suores
GMS
)lasan( telboG )latnemgesbus( detailicitluM )lasan(
Immune Epithelial
Wilcoxon
Seurat−VST (n = 2,000)
Scanpy−SeuratV3 (n = 2,000, batch = false)
Scanpy−Seurat (n = 2,000, batch = true)
Scanpy−Seurat (n = 2,000, batch = false)
triku
Scanpy−SeuratV3 (n = 2,000, batch = true)
Scanpy−Cell Ranger (n = 2,000, batch = true)
Scanpy−Cell Ranger (n = 2,000, batch = false)
Seurat−MVP
Brennecke
Seurat−scTransform (n = 2,000)
Random (n = 2,000)
Scanpy−Pearson (n = 2,000, batch = false)
Seurat−dispersion (n = 2,000)
SingleCellHaystack
OSCA
Scanpy−Pearson (n = 2,000, batch = true)
Transcription factors
Hotspot
scPNMF
Random (n = 500)
NBumi
All
Anticor
Statistic−variance (n = 2,000)
Scry
DUBSstepR
Statistic−mean (n = 2,000)
scSEGIndex
sllec
B
sllec
tsaM
hpM
raloevlA
+3LCC 2CD )lasan(
bulC
suocum
GMS
suores
GMS
)laihcnorb( suores
GMS
)lasan( telboG )latnemgesbus( detailicitluM )lasan(
Fig. 5 | Analysis of lineage subsets of the HLCA dataset. a, Method rankings The mean is calculated for each lineage in the full dataset (endothelial, epithelial,
for the full HLCA dataset, the immune subset and the epithelial subset. Overall immune and stroma). The size of squares shows the s.d. of proportion across
rankings are shown, along with rankings for each metric category. Methods are cell types in each lineage (smaller is more variable) (Extended Data Fig. 7).
ordered by their overall performance across all datasets. b, Overlap of selected Overlaps are not shown for random gene sets. d, Analysis of cell label Milo scores.
feature sets. The Jaccard index values between feature sets from each subset A heatmap shows the Milo score for each unseen cell type on the full, immune and
are shown as a heatmap. c, Overlap with marker genes. A heatmap of the mean epithelial subsets. On the right is shown the difference in scores for each lineage
proportion of marker genes selected by each method on each dataset subset. subset compared to the full dataset.
Registered Report https://doi.org/10.1038/s41592-025-02624-3
scVI scANVI Symphony
stroma). In most cases, relatively few calculated markers are selected Interaction between selected features and integration method
(proportion of markers mean, 0.38; median, 0.39; and first quartile, The focus of this study is the effect of feature selection rather than
0.04) (Extended Data Fig. 7). The lack of markers chosen may be due integration method, but we also measured the performance of the
to redundancy in the information contained by related genes and dif- semi-supervised single-cell annotation using variational inference
ferences in which features are prioritized for selection compared to (scANVI) model37 and Harmony13 followed by query mapping using
marker detection. Selectivity of the markers chosen was not related Symphony12 (referred to as ‘Symphony’) in addition to scVI. This analysis
to performance, with some of the worst-performing methods most allows us to assess the interaction between feature selection and inte-
effectively selecting markers only for the cell types in a specific lineage gration models and the effect of biological supervision. Figure 6 shows
(Extended Data Fig. 7). the average scores and ranks for each integration method and the dif-
So far, we only considered the ranks of methods because indi- ferences in performance for scANVI and Symphony compared to scVI.
vidual scores are not directly comparable between subsets as they Overall, there are no clear differences in metric rankings (Fig. 6d).
contain different cells and labels. To consider one area in more detail, We see a slight trend toward decreases in rankings for methods that
we calculated Milo scores for individual unseen labels, allowing us to rank highly for scVI and increases in rankings for methods that rank
see if an unseen cell type is easier to distinguish in a whole-tissue or lowly for scVI (Extended Data Fig. 8). This effect could be explained
lineage-specific atlas (Fig. 5d). We see a clear trend of lower scores by interactions between feature selection and integration methods or
on the lineage subsets. This pattern supports the argument that by alternatively by scANVI and Symphony being less sensitive to feature
providing more diverse input data to the integration model it learns selection or regression to the mean due to randomness in integra-
more of the possible cell space and can, therefore, better distinguish tion and some metrics. Looking more closely at the differences in
new cell populations. scores (Fig. 6b), we see some methods that stand out. For scANVI,
Nature Methods | Volume 22 | April 2025 | 834–844 842
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
scANVI Symphony
Wilcoxon
Seurat−VST (n = 2,000)
Scanpy−SeuratV3 (n = 2,000, batch = false)
Scanpy−Seurat (n = 2,000, batch = true)
Scanpy−Seurat (n = 2,000, batch = false)
triku
Scanpy−SeuratV3 (n = 2,000, batch = true)
Scanpy−Cell Ranger (n = 2,000, batch = true)
Scanpy−Cell Ranger (n = 2,000, batch = false)
Seurat−MVP
Brennecke
Seurat−scTransform (n = 2,000)
Random (n = 2,000)
Scanpy−Pearson (n = 2,000, batch = false)
Seurat−dispersion (n = 2,000)
SingleCellHaystack
OSCA
Scanpy−Pearson (n = 2,000, batch = true)
Transcription factors
Hotspot
scPNMF
Random (n = 500)
NBumi
All
Anticor
Statistic−variance (n = 2,000)
Scry
DUBSstepR
Statistic−mean (n = 2,000)
scSEGIndex
Mean score
0 0.4 0.8 1.2 1.6
s.d.
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
scVI scANVI Symphony
Difference to scVI
−0.5 0 0.5
s.d.
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
scANVI Symphony
Mean rank
5 10 15 20 25 30
s.d.
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
llarevO )hctaB(
noitargetnI
)oiB(
noitargetnI
gnippaM noitacifissalC snoitalupop
neesnU
a b c d
Difference to scVI
−10−5 0 5 10
s.d.
0.51.01.52.02.5 0.51.01.52.02.5 0 3 6 9 12 5 10 15
Fig. 6 | Comparison of feature selection method performance for different c, A heatmap of mean ranks for methods for each metric category. d, A heatmap
integration and query mapping methods. a, A heatmap of mean scores for each of differences in mean ranks compared to scVI. In all heatmaps, colors represent
metric category for the evaluated methods for integration and query mapping values, and sizes of squares show s.d. across datasets (smaller is more variable).
with scVI, scANVI and Symphony (negative scores in gray). b, A heatmap of Methods are ordered by overall ranking for scVI.
difference in mean scores for scANVI and Symphony compared to scVI.
Registered Report https://doi.org/10.1038/s41592-025-02624-3
there are significant improvements in the Integration (Bio) score for We only compared different numbers of features for some com-
scanpy-Seurat (batch = false), Seurat-MVP, Brennecke38, DUBStepR and mon methods to select a number of features for the final evaluation as
all features. This improvement in performance showed that including the computation required was infeasible for all methods. For the meth-
biological information in the integration process can overcome the ods where we examined different numbers of features, we observed a
limitations of selected features in some cases. relationship between datasets and the optimal number of features for
In fact, scANVI leads to minor but consistent improvements for different metric types; however, the limited number of datasets did not
most metric types compared to scVI, except for Integration (Batch). allow us to connect this relationship to specific technical features, such
This trade-off would be acceptable for many applications, particularly as the number of batches or cell labels, and methods may perform dif-
as the mapping score also increases, showing that preserving more ferently with a different number of features. We encourage analysts to
biological information does not limit the ability to map query datasets tune the number of selected features for their dataset and use case and
to the reference. Symphony shows decreased performance compared we believe this will affect performance more than switching between
to scVI across metric categories, except for the mapping score. While top-performing methods; however, adjusting the number of features
this decreased performance is relatively consistent across methods, is computationally intensive and difficult to assess with new datasets as
the most significant decreases in the unseen population scores are for labels are typically not available for evaluation. Developing methods for
the highest-ranking methods. These results show that Symphony is automatically tuning the number of selected features based on techni-
unable to detect new cell populations that could be separated by scVI cal aspects of datasets is a potential avenue for future research. We also
and scANVI using the same features. emphasize that better performance on query tasks, especially unseen
population detection, needs more features than producing a good
Discussion integrated reference and should be considered if this is an intended use.
In this comprehensive benchmark, we evaluated variants of 24 feature During the planning and implementation of this study, several
selection methods on ten datasets using 1,700 selected feature sets, feature selection methods39–44, alternative metrics45,46 and other
over 6,000 integration runs producing over 140,000 metric scores. comparisons47–49 were published. While we consider it is unlikely that
We performed a rigorous metric selection process and determined a other methods would significantly improve performance, establishing
number of features (2,000) that performed well across datasets. Our this requires further benchmarking. More likely to affect the results
evaluation found highly variable feature selection methods to perform is the inclusion of additional metrics, such as the recently proposed
well, with the approach based on a variance-stabilizing transforma- scGraph metric46 which aims to address limitations of some metrics
tion (Seurat-VST/scanpy-SeuratV3) being the top-ranked method. by considering distances between cell labels and has shown significant
This result reinforces common practice and recommendations from differences in performance between integration methods.
previous benchmarks. Label-guided marker genes (Wilcoxon) also Our benchmark reinforces established practices as highly effective
performed well but were more variable across datasets. We focused on and provides guidance on generally effective parameters that can be
unsupervised methods and other supervised techniques may produce optimized for individual datasets.
more stable results; however, supervised feature selection only applies
when cell labels are available, typically not the case before integration. Online content
The triku method was also highly ranked but showed some bias toward Any methods, additional references, Nature Portfolio reporting sum-
batch correction. maries, source data, extended data, supplementary information,
We did not find a consistent advantage for batch-aware variants of acknowledgements, peer review information; details of author contri-
methods implemented in scanpy. Batch-aware selection could improve butions and competing interests; and statements of data and code avail-
performance in some scenarios, but a more specific evaluation includ- ability are available at https://doi.org/10.1038/s41592-025-02624-3.
ing additional methods is required to determine its applicability. For
large datasets, batch-aware feature selection has a computational References
advantage, as loading the whole dataset into memory can be avoided. 1. Regev, A. et al. Human cell atlas meeting participants. The human
However, we could run many top-performing methods on the full cell atlas. eLife https://doi.org/10.7554/elife.27041 (2017).
datasets with relatively modest memory requirements. 2. Zappia, L., Phipson, B. & Oshlack, A. Exploring the single-cell
We used scVI for our primary benchmark but compared the per- RNA-seq analysis landscape with the scRNA-tools database. PLoS
formance to scANVI, to inspect the effect of adding prior knowledge, Comput. Biol. 14, e1006245 (2018).
and Symphony to see the interaction with an alternative integration 3. Luecken, M. D. et al. Benchmarking atlas-level data integration
approach. We saw that methods performed differently across integra- in single-cell genomics. Nat. Methods https://doi.org/10.1038/
tion approaches but did not identify clear relationships, suggesting s41592-021-01336-8 (2021).
that differences are the result of randomness in integration runs and 4. Tran, H. T. N. et al. A benchmark of batch-effect correction methods
shuffling between equally performing methods; however, there were for single-cell RNA sequencing data. Genome Biol. 21, 12 (2020).
clear differences between integration methods, with scANVI improving 5. Mereu, E. et al. Benchmarking single-cell RNA-sequencing protocols
in all metric categories for the same feature sets. In contrast, Symphony for cell atlas projects. Nat. Biotechnol. 38, 747–755 (2020).
showed decreased performance compared to scVI, particularly at 6. Chazarra-Gil, R., van Dongen, S., Kiselev, V. Y. & Hemberg, M.
unseen population detection. Flexible comparison of batch correction methods for single-cell
Using subsets of the HLCA dataset, we considered lineage-specific RNA-seq using BatchBench. Nucleic Acids Res. 49, e42 (2021).
feature selection. We did not see any clear preference for methods 7. Sheng, J. & Li, W. V. Selecting gene features for unsupervised
and particular lineages, and the top-performing methods effectively analysis of single-cell gene expression data. Brief. Bioinform.
adapted to different subsets. Milo scores for individual unseen labels https://doi.org/10.1093/bib/bbab295 (2021).
showed that it is easier to distinguish new cell populations using a 8. Yip, S. H., Sham, P. C. & Wang, J. Evaluation of tools for highly
more diverse reference atlas; however, this comparison was not our variable gene discovery from single-cell RNA-seq data. Brief.
primary focus, and further work is required to determine if or when Bioinform. https://doi.org/10.1093/bib/bby011 (2018).
lineage-specific features selection and integration can be effective. 9. Zappia, L. et al. Feature selection methods affect the performance
For example, we did not consider whether lineage-specific features of scRNA-seq data integration and querying (Registered
could improve integration of the full dataset or attempt to disentangle Reports Stage 1 manuscript). figshare https://doi.org/10.6084/
effects of feature selection from integration. m9.figshare.24995690.v1 (2024).
Nature Methods | Volume 22 | April 2025 | 834–844 843
Registered Report https://doi.org/10.1038/s41592-025-02624-3
10. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell 34. Yu, Q. et al. Charting human development using a multi-
gene expression data analysis. Genome Biol. 19, 15 (2018). endodermal organ atlas and organoid models. Cell 184,
11. Satija, R., Farrell, J. A., Gennert, D., Schier, A. F. & Regev, A. 3281–3298.e22 (2021).
Spatial reconstruction of single-cell gene expression data. Nat. 35. Amezquita, R. A. et al. Orchestrating single-cell analysis with
Biotechnol. 33, 495–502 (2015). Bioconductor. Nat. Methods https://doi.org/10.1038/s41592-019-
12. Kang, J. B. et al. Efficient and precise single-cell reference atlas 0654-x (2019).
mapping with Symphony. Nat. Commun. 12, 5890 (2021). 36. Vandenbon, A. & Diez, D. A clustering-independent method for
13. Korsunsky, I. et al. Fast, sensitive and accurate integration of finding differentially expressed genes in single-cell transcriptome
single-cell data with Harmony. Nat. Methods https://doi.org/ data. Nat. Commun. 11, 4318 (2020).
10.1038/s41592-019-0619-0 (2019). 37. Xu, C. et al. Probabilistic harmonization and annotation of
14. Butler, A., Hoffman, P., Smibert, P., Papalexi, E. & Satija, R. single-cell transcriptomics data with deep generative models.
Integrating single-cell transcriptomic data across different Mol. Syst. Biol. 17, e9620 (2021).
conditions, technologies, and species. Nat. Biotechnol. 38. Brennecke, P. et al. Accounting for technical noise in single-cell
https://doi.org/10.1038/nbt.4096 (2018). RNA-seq experiments. Nat. Methods 10, 1093–1095 (2013).
15. Dann, E., Henderson, N. C., Teichmann, S. A., Morgan, M. D. & 39. Lazaros, K., Dimitrakopoulos, G. N., Vlamos, P. & Vrahatis, A. G.
Marioni, J. C. Differential abundance testing on single-cell data using A gene selection strategy for enhancing single-cell RNA-seq data
k-nearest neighbor graphs. Nat. Biotechnol. 40, 245–253 (2022). integration. Eng. Proc. 50, 12 (2023).
16. Maan, H. et al. Characterizing the impacts of dataset imbalance 40. Zhang, H. Feature selection for single cell RNA sequencing data
on single-cell data integration. Nat. Biotechnol. https://doi. based on a noise-robust fuzzy relation and fuzzy evidence theory.
org/10.1038/s41587-023-02097-9 (2024). Appl. Soft Comput. 148, 110940 (2023).
17. Büttner, M., Miao, Z., Wolf, F. A., Teichmann, S. A. & Theis, F. J. 41. Taguchi, Y.-H. & Turki, T. Application note: TDbasedUFE and
A test metric for assessing single-cell RNA-seq batch correction. TDbasedUFEadv: bioconductor packages to perform tensor
Nat. Methods 16, 43–49 (2019). decomposition based unsupervised feature extraction. Front.
18. Lütge, A. et al. CellMixS: quantifying and visualizing batch effects Artif. Intell. 6, 1237542 (2023).
in single-cell RNA-seq data. Life Sci Alliance 4, e202001004 (2021). 42. Ng, G. Y. L., Tan, S. C. & Ong, C. S. On the use of QDE-SVM
19. Gupta, A. et al. Class-weighted evaluation metrics for imbalanced for gene feature selection and cell type classification from
data classification. Preprint at http://arxiv.org/abs/2010.05995 scRNA-seq data. PLoS ONE 18, e0292961 (2023).
(2020). 43. Peng, M., Lin, B., Zhang, J., Zhou, Y. & Lin, B. scFSNN: a feature
20. Luecken, M. D. et al. Defining and benchmarking open problems selection method based on neural network for single-cell
in single-cell analysis. Preprint at Res. Sq. https://doi.org/ RNA-seq data. BMC Genomics 25, 264 (2024).
10.21203/rs.3.rs-4181617/v1 (2024). 44. Ranek, J. S. et al. DELVE: feature selection for preserving
21. Zheng, G. X. Y. et al. Massively parallel digital transcriptional biological trajectories in single-cell data. Nat. Commun. 15,
profiling of single cells. Nat. Commun. 8, 14049 (2017). 2765 (2024).
22. Heumos, L. et al. Best practices for single-cell analysis across 45. Loh, J. W. & Ouyang, J. F. cellstruct: metrics scores to quantify the
modalities. Nat. Rev. Genet. https://doi.org/10.1038/s41576-023- biological preservation between two embeddings. Preprint at
00586-w 1–23 (2023). bioRxiv https://doi.org/10.1101/2023.11.13.566337 (2023).
23. Lin, Y. et al. Evaluating stably expressed genes in single cells. 46. Wang, H., Leskovec, J. & Regev, A. Metric mirages in cell
Gigascience 8, giz106 (2019). embeddings. Preprint at bioRxiv https://doi.org/10.1101/
24. Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep 2024.04.02.587824 (2024).
generative modeling for single-cell transcriptomics. Nat. Methods 47. Huang, H., Liu, C., Wagle, M. M. & Yang, P. Evaluation of deep
15, 1053–1058 (2018). learning-based feature selection for single-cell RNA sequencing
25. Stuart, T. et al. Comprehensive integration of single-cell data. Cell data analysis. Genome Biol. 24, 259 (2023).
177, 1888–1902.e21 (2019). 48. Zhu, X., Wang, J., Li, R. & Peng, X. Comparison of gene selection
26. Zappia, L., Phipson, B. & Oshlack, A. Splatter: simulation of methods for clustering single-cell RNA-seq data. Curr. Bioinform.
single-cell RNA sequencing data. Genome Biol. 18, 174 (2017). 18, 1–11 (2023).
27. Tyler, S. R., Lozano-Ojalvo, D., Guccione, E. & Schadt, E. E. 49. Alani, M. et al. A roadmap for selecting and utilizing optimal
Anti-correlated feature selection prevents false discovery of features in scRNA sequencing data analysis for stem cell
subpopulations in scRNAseq. Nat. Commun. 15, 699 (2024). research: a comprehensive review. Int. J. Stem Cells https://doi.org/
28. Ranjan, B. et al. DUBStepR is a scalable correlation-based feature 10.15283/ijsc23170 (2024).
selection method for accurately clustering single-cell data.
Nat. Commun. 12, 5849 (2021). Open Access This article is licensed under a Creative Commons
29. Andrews, T. S. & Hemberg, M. M3Drop: dropout-based feature Attribution 4.0 International License, which permits use, sharing,
selection for scRNASeq. Bioinformatics https://doi.org/10.1093/ adaptation, distribution and reproduction in any medium or format,
bioinformatics/bty1044 (2018). as long as you give appropriate credit to the original author(s) and the
30. M Ascensión, A., Ibáñez-Solé, O., Inza, I., Izeta, A. & Araúzo-Bravo, source, provide a link to the Creative Commons licence, and indicate
M. J. Triku: a feature selection method based on nearest if changes were made. The images or other third party material in this
neighbors for single-cell data. Gigascience 11, giac017 (2022). article are included in the article’s Creative Commons licence, unless
31. Song, D., Li, K., Hemminger, Z., Wollman, R. & Li, J. J. scPNMF: indicated otherwise in a credit line to the material. If material is not
sparse gene encoding of single cells to facilitate gene selection included in the article’s Creative Commons licence and your intended
for targeted gene profiling. Bioinformatics 37, i358–i366 (2021). use is not permitted by statutory regulation or exceeds the permitted
32. Reed, A. D. et al. A single-cell atlas enables mapping of use, you will need to obtain permission directly from the copyright
homeostatic cellular shifts in the adult human breast. Nat. Genet. holder. To view a copy of this licence, visit http://creativecommons.
56, 652–662 (2024). org/licenses/by/4.0/.
33. Sikkema, L. et al. An integrated cell atlas of the lung in health and
disease. Nat. Med. 29, 1563–1577 (2023). © The Author(s), 2025
Nature Methods | Volume 22 | April 2025 | 834–844 844
Registered Report https://doi.org/10.1038/s41592-025-02624-3
Methods Model-based methods
Our study follows a standard benchmark design, consisting of test data- Model-based methods fit an appropriate distributional model to the
sets, feature selection methods to be evaluated and metrics for measur- dataset. Features are then selected by looking for those significantly
ing performance (Extended Data Fig. 1). The complete benchmarking different from the fitted model. These include scTransform55 (v.0.3.5,
pipeline is implemented as a Nextflow50 workflow (Extended Data Fig. 2) accessed via Seurat), analytic Pearson residuals56 (implemented in
available from GitHub51 and archived on Zenodo52. Summaries of the scanpy) and scry (v.1.10.0)57.
specific methods, metrics, datasets and processing steps are provided
in the following sections. Please refer to the supplementary methods, Embedding-based methods
pipeline code, original publications and package documentation for Dimensionality reduction is a commonly used preprocessing step in
further information. scRNA-seq analysis. Some feature selection methods either use sophis-
ticated embedding methods or look for features that vary across an
Evaluated methods embedding. scPNMF (commit 47d5b10c) performs a modified PNMF,
We selected a range of feature selection methods covering approaches where an alternative initialization is used and selects features associ-
from standard analysis workflows and alternative methods proposed ated with informative bases31, and singleCellHaystack (v.0.3.4) uses
for scRNA-seq data. To be considered, a method must be implemented Kullback-Leibler divergence to find features that are expressed in subsets
in a publicly available package that we could reliably install and run. of nonrandomly positioned cells36. For singleCellHaystack, we first select
Some methods can automatically determine the number of features features using Seurat-VST and perform a 50-dimensional PCA as input.
to select, but for most others this must be specified. A few methods
can consider batch labels during selection, but for most, this requires Graph-based methods
manually splitting the data, computing feature sets on each batch and Another common step in scRNA-seq analysis is to build a
combining the results. We have used the default settings or what is rec- nearest-neighbor graph of cells, typically using positions in an embed-
ommended in any accompanying documentation for most methods, ded space. Some methods operate on these graphs. Hotspot (v.1.0.0)
but for a subset of highly used methods, we evaluated variants. Any looks for features with a high local auto-correlation within a graph58 and
preprocessing steps required before feature selection are considered triku (v.2.1.4) uses a neighborhood graph to distinguish features that
part of the method. We used the steps suggested in the documentation are expressed in a few cells randomly across a dataset from those that
for each method as they are recommended by the authors and repre- are expressed in a few related cells30. For both, we use a graph based on
sent the most likely real-world usage. a PCA of all features as input.
Simple control methods. We include all features and random feature Supervised methods
sets in the evaluation as control methods. We expect that using feature We focus on evaluating unsupervised feature selection methods, as
sets selected by real methods improves performance over using all cell labels are typically not available before the integration process;
features and any randomly selected sets. To control for variability however, at least some level of cell labels may be available, particularly
in selecting random features, we always include five random feature for atlas-building projects that combine previously annotated public
sets selected with different seeds and average metric scores over the datasets. As an example supervised method, we include marker genes
five sets. selected using the Wilcoxon rank-sum test (as implemented in scanpy)
followed by a filtering procedure to remove features expressed in less
Excess variability methods. The most common approach to feature than 10% of cells within a label, expressed in more than 80% of cells out-
selection in RNA-seq analysis tool boxes such as scanpy10 and Seurat11 side the label or with a P value >0.1. The remaining features are sorted
is to select highly variable features, those that show excess variability by estimated log fold change and the top 200 features are selected per
beyond what is expected. This approach assumes that extra variability label. The final feature set is the intersection of the features selected
results from differences in gene expression between cell populations for each label.
or states and that selecting these features will identify those important We also included known transcription factors downloaded from
to the cells in the sample. The Human Transcription Factors59 website (https://humantfs.ccbr.
We benchmark the following excess variability methods: utoronto.ca/index.php) selecting 1,639 genes where the ‘Is TF?’ field
features with the highest variance, the fitting method from was equal to ‘Yes’. The intersection of this list with the genes in each
Brennecke et al.38 (implemented in scran53 v.1.26.0), variants from dataset was used. This method cannot be applied to the splat dataset
Seurat11 (v.4.3.0) (Seurat-dispersion, Seurat-MVP11 and Seurat-VST25), as it does not contain real gene names.
variants from scanpy10 (v.1.9.1) (scanpy-Seurat, scanpy-SeuratV3
and scanpy-Cell Ranger) and the approach from ‘Orchestrating Stable expression methods
Single-Cell Analysis with Bioconductor’35 using batchelor54 (v.1.14.0) The opposite of highly variable features are those stably expressed or
and scran. For scanpy methods we used both standard and batch- varying less than expected. The scSEGIndex method in the scMerge
aware variants. package (v.1.1.4.0) fits a gamma-Gaussian mixture model to each fea-
ture23. The parameters of this model and other features, such as the
Methods based on other statistical features proportion of zero counts, are used to rank features and calculate a
Other feature statistics can also be used for feature selection including stability index. We used these stable features as a negative control and
selecting features with the highest mean expression, Anticor27 (v.0.1.8), they should perform poorly for integration as they should not capture
which selects features with excess negative correlations, NBumi which either technical noise or biological signal.
selects features with excess zeros (M3Drop v.1.24.0)29 and DUBStepR
(commit 76aa3948), which uses stepwise regression of a binned cor- Evaluation metrics
relation matrix28. We implemented a wide array of metrics designed to evaluate different
For Anticor, we disabled the filtering of predefined gene pathways aspects of creating and using an integrated scRNA-seq reference. Some
as it requires gene identifiers, which are not available for all datasets. metrics require a ground truth cell label, while others are unsupervised
For NBumi, we select features with an adjusted P value <0.01 unless this and measure whether the structure in a single sample is maintained. All
results in fewer than 500 features, in which case the 500 features with metrics are designed so that a raw score of 0 represents the worst pos-
the lowest P values were used. sible performance and a raw score of 1 the best possible performance.
Nature Methods
Registered Report https://doi.org/10.1038/s41592-025-02624-3
Integration (Batch). Integration (Batch) metrics measure the mixing The reconstruction metric assesses a generative model’s ability to
between batches in the reference. Cells of the same cell type should represent query cells by sampling from the posterior distribution and
be thoroughly mixed and neighborhoods should be equally likely to measuring the cosine distance between the mean posterior expression
contain cells from any batch. The batch ASW3, Batch PCR3, graph con- profile and the true cell expression profile64. We adjusted the distances
nectivity3 and graph-based iLISI3,13 are implemented in scIB3 (v.1.1.4) to be in the range 0 to 1 and took 1 minus the mean distance as the final
using scikit-learn60 (v.1.1.2). The kBET metric17 is accessed from the kBET score. This metric cannot be calculated for Symphony integrations as
R package (commit a10ffeaa) via scIB. To calculate an overall score for it is not a generative method.
the Seurat mixing metric14 we divided the cell scores by the maximum
neighborhood size, took the mean across cells and subtracted from 1 Classification. The classification (or label transfer) metrics measure
so higher scores are better. For the CMS metric18 in the CellMixS pack- how well a classifier trained on the reference can correctly predict
age (v.1.14.0) we use 1 minus the proportion of cells with a P value <0.1. labels for query cells. We use standard classification metrics: accuracy,
F1 score, Jaccard index, Matthews correlation coefficient (adjusted to
Integration (Bio). Integration (Bio) metrics measure whether biological [0, 1]) and macro-averaged area under the precision-recall curve as
signals (primarily cell labels) are conserved after integration. Unlike implemented by scikit-learn. For F1 and the Jaccard index we use micro,
batch correction metrics, where perfect scores can be obtained by map- macro and rarity-weighted19 averages over labels.
ping cells to a single point, biological conservation metrics require that
cell labels are separated after integration. The label ASW3, graph-based Unseen population prediction. Unseen population metrics focus on
cLISI3,13, cell cycle conservation3, ARI3, NMI3, Isolated labels ASW3 and novel biology in the query by measuring how mapping has affected cell
Isolated labels FI3 metrics are implemented in scIB using scikit-learn. labels present in the query but deliberately left out of the reference.
bARI16 and bNMI metrics are available from balanced_clustering (com- These should be maintained as separate populations but an integra-
mit a2ae3a4d). For the Seurat local structure metric14 we used the aver- tion that does not properly capture variation may merge them with
age over all cells as the final score and for ldfDiff18 we took the absolute other labels.
distance and set an upper bound to get a cell score and used 1 minus The unseen uncertainty metric uses the output of the label transfer
the mean cell score as the overall score. The cell cycle metric3 scores classifier and measures poor classification of unseen cell by calculat-
cells11 using genes from Tirosh et al.61 with ENSEMBL IDs obtained from ing 1 minus the mean probability of the assigned class for query cells
Biomart62 using the biomaRt package63. It cannot be calculated for from unseen populations. Unseen cell distance is based on the cell
the splat dataset as it does not contain cell cycle effects. For metrics distance metric but calculated only for unseen query populations. As
that require clusters (ARI, NMI, bARI and bNMI), we performed Leiden the label does not exist in the reference, we calculate distances to each
clustering with the resolution parameter set to values between 0.1 and cell’s nearest reference population and subtract the final score from 1
2 in steps of 0.1 using scanpy via scIB and selected the resolution with so that higher distances (greater separation from the reference) give
the best metric score. higher scores. Unseen label distance applies similar changes to the
label distance metric by calculating distances to the nearest reference
Mapping quality. Mapping quality metrics assesses how well the refer- label centroid.
ence represents the query and is able to merge it into the same space. We use the milopy65 (commit be1a6cc8) implementation of the
For perfect mapping, cell types present in both the reference and query Milo differential abundance method15 as a metric to detect unseen
should be mixed, as should batches within the query. At the same time, populations by taking query or reference as the covariate of interest64.
biology within the query should be preserved. The cell distance metric A neighborhood graph is calculated in the integrated embedding using
calculates the Mahalonobis distance between each mapped query cell a number of neighbors equal to five times the number of batches (up
and the distribution of the corresponding label in the reference12. To to a maximum of 200). Milo is then applied to a subset of cells (up to
create a bound for the distance we calculate the distance for every cell 20,000 cells or 10% of the datasets, whichever is higher). The score for
in the reference for a label and take the 90th quantile. The final score each label is the proportion of cell neighborhoods significantly associ-
is 1 minus the proportion of mapped cells outside the boundary. The ated with the query (false discovery rate-adjusted P value <0.1). The
label distance considers labels as a whole rather than individual cells12. overall score is the average of the proportions across all unseen labels.
The Mahalonobis distance is calculated between the centroid of the In rare cases for poor integrations where Milo cannot select cells from
label in the query and the matching label in the reference. Labels are an unseen label, that label is assigned a score of 0.
skipped if they have fewer than 20 cells in the query or are not in the
reference. We used the maximum distance of query cells to their label Benchmarking datasets
centroid as a boundary. Distances to the matching reference label are We selected datasets representing different scenarios (tissues, tech-
then scaled using this value and set to 1 if they exceed the maximum nologies and developmental stages) where integration is a critical
distance. The final score is the mean across cell types. analysis step, including smaller-scale datasets and larger atlases. We
mLISI is the same as iLISI but measures mixing between the query chose query batches by selecting batches with shared characteristics
and reference (also known as ref_query LISI12) and qLISI measures different from the remaining samples, such as technology, time point
mixing between query batches after mapping (also known as query_ or location. The unseen populations removed from the reference were
donors LISI12). chosen by looking for labels enriched in the query batches and select-
kNN correlation measures how well cell neighborhoods are main- ing labels presenting different challenges, such as rare or perturbed
tained12. For each query batch, a PCA is performed and the Euclidean cells. For each dataset, we use the cell labels assigned by the original
distances to the 100 nearest neighbors of each cell are calculated. authors.
The distances to the same neighbors in the joint integrated embed-
ding are also calculated and the Spearman correlation is computed. scIB Pancreas. We downloaded the scIB pancreas dataset3 from fig-
After adjusting the correlations to the range 0 to 1, the mean of cells share66. Cell labels were taken from the ‘celltype’ cell annotation column
in each batch is calculated and the final score is the mean across (12 reference labels) and batches from the ‘tech’ column. For the query,
batches. For particularly bad integrations (that is small random we used batches representing the CEL-seq and CEL-seq2 technologies
feature sets), a cell may be equally distant from all neighbors, in with the ‘activated_stellate’ label treated as an unseen population.
which case the correlation cannot be calculated and it is assigned a The prepared dataset contained 18,319 features, 12,731 reference cells
score of 0. (seven batches) and 3,243 query cells (two batches).
Nature Methods
Registered Report https://doi.org/10.1038/s41592-025-02624-3
NeurIPS 2021. We downloaded the NeurIPS 2021 CITE-seq dataset67,68 ‘Multiciliated (nasal)’, ‘Club (nasal)’, ‘Goblet (subsegmental)’, ‘SMG
from the Gene Expression Omnibus (GEO)69 (GSE194122) and used only serous (nasal)’, ‘SMG serous (bronchial)’, ‘SMG mucous’, ‘EC aerocyte
the gene expression features. Cell labels were taken from the ‘cell_type’ capillary’, ‘Peribronchial fibroblasts’, ‘Smooth muscle’, ‘Smooth muscle
annotation and batch labels from the ‘batch’ annotation. We considered FAM83D+’, ‘B cells’, ‘DC2’, ‘Alveolar Mph CCL3+’ and ‘Mast cells’ labels are
samples from Site 4 as the query with the ‘CD8+ T naive’ and ‘Proeryth- unseen populations. After preparation, the dataset included 27,987
roblast’ labels treated as unseen query populations. After preparation, features, 314,573 reference cells (nine batches and 47 reference labels)
the dataset contained 13,953 features, 70,061 reference cells (nine and 251,400 query cells (five batches).
batches) with 42 reference labels and 16,715 query cells (three batches).
HLCA (immune). The HLCA (immune) dataset takes the full HLCA
Fetal liver hematopoiesis. We downloaded the fetal liver hematopoie- dataset and uses the coarsest level of annotation to select cells in the
sis70 dataset from CellAtlas.io71 using batch labels from the ‘fetal.ids’ immune compartment. The batches and labels are the same as the
annotation and cell labels from the ‘cell.ids’ annotation. Three samples full HLCA dataset, but after subsetting, only ‘B cells’, ‘DC2’, ‘Alveolar
from different developmental stages were treated as the query with Mph CCL3+’ and ‘Mast cells’ remain as unseen labels. We also removed
‘Kupffer Cell’, ‘NK’, ‘ILC precursor’ and ‘Early lymphoid_T lymphocyte’ some batches with insufficient cells. The prepared dataset has 26,618
as unseen populations. The prepared dataset contains 26,686 features, features, 155,385 reference cells (seven batches and 16 reference labels)
62,384 reference cells (11 batches and 23 reference labels) and 26,449 and 52,795 query cells (two batches).
query cells (three batches).
HLCA (epithelial). The HLCA (epithelial) dataset is a second subset of
Reed breast. We downloaded the version of the Reed breast dataset32 the HLCA dataset focusing on the epithelial compartment. This sub-
released with the preprint72 from the Chan Zuckerberg CELLxGENE: set consists of 27,673 features, 118,374 reference cells (eight batches
Discover Census (https://cellxgene.cziscience.com/)73 (dataset ID and 17 reference labels) and 162,875 query cells (five batches) with
0ba636a1-4754-4786-a8be-7ab3cf760fd6, Census version 2023-07-05) ‘Multiciliated (nasal)’, ‘Club (nasal)’, ‘Goblet (subsegmental)’, ‘SMG
using the cellxgene-census package (v.1.0.1) and subsetted to cells with serous (nasal)’, ‘SMG serous (bronchial)’ and ‘SMG mucous’ remaining
a BRCA status of either wild-type (‘WT’ or ‘assumed_WT’) or ‘BRCA1’. as unseen labels.
Donor ID was used as the batch label, with cell labels taken from the
‘level2’ annotation. We excluded a subset of cells labeled as doublets, splat. Simulations address some limitations of real data by providing a
as it is not clear how they should be treated by metrics. Wild-type definite ground truth. We generated a dataset using a modified version
cells were used to create the reference and BRCA1 cells were used of the splat simulation in the Splatter package26 designed to represent a
as the query. The ‘BSL2’, ‘CD8T 1’, ‘CD8T 2’, ‘CD8T 3’, ‘FB5’, ‘LEC1’ and scenario where a tissue is measured using three different technologies
‘LEC2’ labels were used as unseen labels. After preparation, the dataset (two batches each) in two conditions. These ‘technologies’ measure a
contained 33,691 features, 337,339 reference cells (24 batches and 32 medium number of cells at medium depth (Batch1 and Batch2), a low
reference labels) and 197,649 query cells (17 batches). number of cells at high depth (Batch3 and Batch4) and a high number
of cells at low depth (Batch5 and Batch6), with the low-depth sam-
Single-cell Eye in a Disk. We downloaded the single-cell Eye in a Disk ples used as the query. The simulation contains ten cell labels, includ-
(scEiaD) dataset74 from the plae: PLatform for Analysis of scEiad website ing a progenitor differentiating along two trajectories (one with an
(https://plae.nei.nih.gov/) and selected the human cells derived from ‘Intermediate’ cell type only present in the query) and six discrete cell
tissue samples where the organ was specified as ‘Eye’. We removed cells types that differ in number of cells, number of differentially expressed
that did not have a cell label or were labeled as doublets and batches genes and number of detected features. The discrete groups include a
with fewer than 500 cells remaining, as these caused some metrics ‘Rare’ population and a ‘Perturbed’ state, which are only present in the
to produce unreliable results. Cell labels were taken from the ‘Cell- query. To increase the variability in the simulation, we added additional
Type_predict’ annotation (harmonized labels from a classifier) and label-specific noise factors to the model, which were applied before
the ‘batch’ annotation was used for batches. We split batches using generating counts. The splat dataset contains 9,984 features, 30,041
cell capture technology, with 10x v.2 taken as the reference and 10x reference cells (four batches and seven reference labels) and 69,936
v.3 and Drop-seq batches as the query. The ‘B-Cell’, ‘Blood Vessel’, query cells (two batches).
‘Macrophage’, ‘Pericyte’, ‘Smooth Muscle Cell’ and ‘T/NK-Cell’ labels are
unseen populations. After preparation, the dataset contained 19,560 Benchmarking pipeline
features, 360,270 reference cells (69 batches and 41 reference labels) To improve reproducibility, make sure that results are up-to-date as code
and 48,496 query cells (18 batches). is updated and easily take advantage of computing resources, we built
a pipeline using Nextflow50 (Extended Data Fig. 2). The pipeline takes
Human endoderm. We downloaded the Human endoderm dataset34 a dataset, applies standard preprocessing and splits it into reference
from Mendeley Data75. Individuals were treated as batches with labels and query samples. The feature selection methods are applied to the
obtained from the ‘Cell_type’ annotation. A small number of cells labeled reference, and selected features used for integration. After integra-
as ‘Undefined’ were removed. Samples from weeks 12–15 were selected tion, the query is mapped to the reference, and a cell label classifier is
as the query with ‘Basal like’, ‘Ciliated’, ‘Hepatocyte’, ‘Mesenchyme sub- trained. The reference and query, ground truth cell labels and trans-
type 4’ and ‘T cell/NK cell 1’ labels treated as query-specific. The prepared ferred labels are provided to metrics. The metric scores are then scaled,
dataset consisted of 27,855 features, 100,580 reference cells (ten batches aggregated and ranked. Pipeline stages use both Python (v.3.9.13) and R76
and 21 reference labels) and 44,784 query cells (four batches). (v.4.2.2), including packages from Bioconductor77. The Python anndata
package78 (v.0.8.0) was used to store data and save it as H5AD files
Human Lung Cell Atlas. We downloaded the core Human Lung Cell between pipeline stages. The zellkonverter package (v.1.8.0) was used
Atlas dataset33 from the Chan Zuckerberg CELLxGENE: Discover Cen- to load data into R via the reticulate (v.1.26) interface where it was stored
sus (dataset ID 066943a2-fdac-4b29-b348-40cede398e4e, Census as SingleCellExperiment35 (v.1.20.0) or SeuratObject (v.4.1.3) objects.
version 2023-07-25) and used the ‘dataset’ annotation as defined by
the authors as batch labels with the ‘ann_finest_level’ annotation as Dataset preprocessing
labels. Datasets from organ donors were treated as the reference and The preprocessing step includes basic quality control filtering of cells
healthy and diseased samples from living donors made up the query. using scanpy and storing information (such as batch and label) in
Nature Methods
Registered Report https://doi.org/10.1038/s41592-025-02624-3
standard locations. We removed cells with fewer than 100 total counts we used a set of reference methods to establish the effective range of
or expressing fewer than 100 features. The dataset is split into a refer- each metric. These are all features, randomly selected features, stably
ence and query based on the batch labels. Labels with fewer than 20 expressed features from scSEGIndex and batch-aware features from
cells are removed from both the reference and query, as some metrics scanpy-Cell Ranger as an example of current standard practice3,22.
can behave unpredictably with small cell numbers. Labels defined as Depending on the metric, using all features performs either well or
unseen populations are also removed from the reference. The final pre- poorly, while random and stably expressed features result in high
processing step removes any features not expressed in the reference. batch-correction scores but poor biological conservation. The baseline
methods were used to establish a range for each metric (for a dataset),
Integration and query mapping and then all scores were scaled relative to that range. Scaling using
The base model we use for integration is scVI24 available in scvi-tools79 baseline methods provides ranges that are more interpretable and are
(v.0.17.1). This model uses a conditional variational autoencoder and not affected by adding or removing methods.
allows the mapping of query samples using architecture surgery80. We The scaled metric scores were aggregated by taking the mean for
also train a scANVI model37 a semi-supervised extension of scVI where each category. This level of aggregation gives a summarized perfor-
cell labels are used to finetune the network. These models take raw mance for each of the methods for each task. An overall score for each
count data as input, so we did not consider the interaction between dataset is obtained using a weighted mean of the task scores.
feature selection and normalization methods.
As an alternative approach based on correcting a PCA space, we Overall= 1 ×( Int.Batch + Int.Bio )+ 1
2 2 2 2
included integration with Harmony13 followed by query mapping using
Mapping Class. Unseen
Symphony12. We provide Harmony with normalized expression values ×( + + )
3 3 3
rather than raw counts as suggested by the documentation. Counts are
first normalized to counts per 10,000, then log-transformed. The dataset Methods were ranked at the level of metric categories, datasets
is subset to the selected features and scaled with a maximum value of 10 and over the whole benchmark. These rankings let us evaluate which
(per feature) and 30 principal components are provided to Harmony. methods perform better at different tasks or scenarios. We also checked
For Symphony, log-transformed normalized query data are provided for consistency between integration approaches and variants of feature
(scaling is performed during mapping). Data preprocessing steps are selection methods.
performed using functions in scanpy and integration and query mapping Further analysis examined the similarity between methods by
are performed using harmonypy81 (v.0.0.9) and symphonypy82 (v.0.2.1). considering the overlap in selected sets calculated using the Jaccard
index. We also compared between the full HLCA dataset and subsets
Label transfer representing the immune and epithelial compartments.
We trained a multinomial logistic regression classifier on the integrated Final figures were produced using the ggplot2 package83 (v.3.5.0)
reference using scikit-learn, taking the position of each cell in the and assembled using patchwork (v.1.2.0). Data processing was per-
integrated embedding space as input and the ground truth cell labels formed using tidyverse84 (v.2.0.0) packages.
as the output. Labels are transferred to the query by providing the
mapped embedding coordinates to the trained classifier, predicting Reporting summary
the probability for each reference label and recording the label with Further information on research design is available in the Nature
the highest probability. Portfolio Reporting Summary linked to this article.
Metric selection Data availability
For metric selection we used different numbers of randomly selected All real scRNA-seq datasets were downloaded from public repositories
features across all test datasets. We also included feature sets of differ- provided by the original authors as described in the methods (scIB Pan-
ent sizes from the scanpy-Seurat method to evaluate the relationship creas, figshare66; NeurIPS, GEO (GSE194122); Fetal liver, CellAtlas.io71;
with the number of features as random gene sets have no inherent Reed Breast, Chan Zuckerberg CELLxGENE: Discover Census (dataset
ordering (the first features selected are no more informative than the ID 0ba636a1-4754-4786-a8be-7ab3cf760fd6, Census version 2023-07-
last features selected). We evaluated the behavior of individual metric 25); scEiaD, plae: PLatform for Analysis of scEiad website (https://plae.
scores and the relationships between them. Metrics were removed if nei.nih.gov/); Human endoderm, Mendelay Data75; and HLCA, Chan
they could not distinguish between feature sets (have an insufficient Zuckerberg CELLxGENE: Discover Census (dataset ID 066943a2-fdac-
dynamic range), were overly correlated (Pearson correlation) with the 4b29-b348-40cede398e4e, Census version 2023-07-25)). Raw and pre-
number of features, were associated with technical dataset features or pared dataset files, selected feature sets, metric scores and rendered
showed undesirable correlation patterns. analysis reports from this benchmark are available from figshare85.
Selecting a number of features Code availability
We evaluated different numbers of features for methods in Seurat and All code associated with this study is available on GitHub51 and archived
scanpy as well as high variance or high mean expression. We calculated on Zenodo52, including scripts for downloading datasets from public
z-scores across methods and datasets to see how performance changed repositories provided by the original authors, running methods and cal-
with the number of features. To reduce the computational cost, we culating metrics, the Nextflow pipeline and associated environment and
limited this part of the analysis by methods rather than datasets as it configuration files. The code for analyzing the benchmark results, includ-
allowed us to see the effect of the number of features across datasets. ing the production of final figures, is also available in this repository.
The number of features used for the benchmark (2,000) was chosen by
considering trends over methods, datasets and metric types. References
50. Di Tommaso, P. et al. Nextflow enables reproducible
Analysis of results computational workflows. Nat. Biotechnol. 35, 316–319 (2017).
The relative rather than absolute performance of methods and the 51. Zappia, L. et al. Atlas-feature-selection-benchmark: Code for
aggregation across metrics are most informative. All metrics produced ‘Feature selection methods affect the performance of scRNA-seq
scores in the range of 0 to 1 (with higher being better), but they have data integration and querying’. GitHub https://github.com/
different real dynamic ranges. To scale each metric for each dataset theislab/atlas-feature-selection-benchmark (2024).
Nature Methods
