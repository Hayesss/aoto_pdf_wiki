---
source_path: /mnt/c/Users/Administrator/Zotero/storage/AXYM3HJC/Saelens 等 - 2019 - A comparison of single-cell trajectory inference methods.pdf
ingested: 2026-04-23
sha256: 99cbc8cc81625d8e
---

Articles
https://doi.org/10.1038/s41587-019-0071-9
A comparison of single-cell trajectory inference
methods
Wouter Saelens 1,2,6, Robrecht Cannoodt 1,3,4,6, Helena Todorov 1,2,5 and Yvan Saeys 1,2*
Trajectory inference approaches analyze genome-wide omics data from thousands of single cells and computationally infer
the order of these cells along developmental trajectories. Although more than 70 trajectory inference tools have already been
developed, it is challenging to compare their performance because the input they require and output models they produce vary
substantially. Here, we benchmark 45 of these methods on 110 real and 229 synthetic datasets for cellular ordering, topology,
scalability and usability. Our results highlight the complementarity of existing tools, and that the choice of method should depend
mostly on the dataset dimensions and trajectory topology. Based on these results, we develop a set of guidelines to help users
select the best method for their dataset. Our freely available data and evaluation pipeline (https://benchmark.dynverse.org)
will aid in the development of improved tools designed to analyze increasingly large and complex single-cell datasets.
Single-cell omics data, including transcriptomics, proteomics Given the diversity in TI methods, it is important to quantita-
and epigenomics data, provide new opportunities for study- tively assess their performance, scalability, robustness and usability.
ing cellular dynamic processes, such as the cell cycle, cell dif- Many attempts at tackling this issue have already been made7,22,25,28–33,
ferentiation and cell activation1,2. Such dynamic processes can be but a comprehensive comparison of TI methods across a large
modeled computationally using trajectory inference (TI) methods, number of different datasets is still lacking. This is problematic, as
also called pseudotime analysis, which order cells along a trajectory new users to the field are confronted with an overwhelming choice
based on similarities in their expression patterns3–5. The resulting of TI methods, without a clear idea of which would optimally solve
trajectories are most often linear, bifurcating or tree-shaped, but their problem. Moreover, the strengths and weaknesses of existing
more recent methods also identify more complex trajectory topolo- methods need to be assessed, so that new developments in the field
gies, such as cyclic6 or disconnected graphs7. TI methods offer an can focus on improving the current state-of-the-art.
unbiased and transcriptome-wide understanding of a dynamic pro- In this study, we evaluated the accuracy, scalability, stability and
cess1, thereby allowing the objective identification of new (primed) usability of 45 TI methods (Fig. 1a). We found substantial comple-
subsets of cells8, delineation of a differentiation tree9,10 and infer- mentarity between current methods, with different sets of methods
ence of regulatory interactions responsible for one or more bifurca- performing most optimally depending on the characteristics of the
tions11. Current applications of TI focus on specific subsets of cells, data. For method users, we created an interactive set of guidelines
but ongoing efforts to construct transcriptomic catalogs of whole (available at guidelines.dynverse.org), which gives context-specific
organisms12–14 underline the urgency for accurate, scalable11,15 and recommendations for method usage. Our evaluation also highlights
user-friendly TI methods. some challenges for current methods, and our evaluation strategy
A plethora of TI methods has been developed over the past few can be useful to spearhead the development of new tools that accu-
years and even more are being created every month (Supplementary rately infer trajectories on ever more complex use cases.
Table 1). Indeed, in several repositories listing single-cell tools, such
as omictools.org16, the ‘awesome-single-cell’ list17 and scRNA-tools. Results
org18, TI methods are one of the largest categories. While each Trajectory inference methods. To make the outputs from differ-
method has its own unique set of characteristics in terms of under- ent methods directly comparable to each other, we developed a
lying algorithm, required prior information and produced outputs, common probabilistic model for representing trajectories from all
two of the most distinctive differences between TI methods are possible sources (Fig. 1b). In this model, the overall topology is rep-
whether they fix the topology of the trajectory and what type(s) of resented by a network of ‘milestones’, and the cells are placed within
graph topologies they can detect. Early TI methods typically fixed the space formed by each set of connected milestones. Although
the topology algorithmically (for example, linear8,19–21 or bifurcat- almost every method returned a unique set of outputs, we were able
ing trajectories22,23) or through parameters provided by the user24,25. to classify these outputs into seven distinct groups (Supplementary
These methods therefore mainly focus on correctly ordering the Fig. 1) and we wrote a common output converter for each of these
cells along the fixed topology. More recent methods also infer the groups (Fig. 2a). When strictly required, we also provided prior
topology7,26,27, which increases the difficulty of the problem at hand, information to the method. These different priors can range from
but allows the unbiased identification of both the ordering inside a weak priors that are relatively easy to acquire, such as a start cell,
branch and the topology connecting these branches. to strong priors, such as a known grouping of cells, that are much
1Data mining and Modelling for Biomedicine, VIB Center for Inflammation Research, Ghent, Belgium. 2Department of Applied Mathematics, Computer
Science and Statistics, Ghent University, Ghent, Belgium. 3Center for Medical Genetics, Ghent University Hospital, Ghent, Belgium. 4Department of
Biomolecular Medicine, Ghent University, Ghent, Belgium. 5Centre International de Recherche en Infectiologie, Inserm, U1111, Université Claude Bernard
Lyon 1, CNRS, UMR5308, École Normale Supérieure de Lyon, Université de Lyon, Lyon, France. 6These authors contributed equally: Wouter Saelens,
Robrecht Cannoodt. *e-mail: yvan.saeys@ugent.be
NATuRe BioTeCHNologY | VOL 37 | MAY 2019 | 547–554 | www.nature.com/naturebiotechnology 547
Articles NATure BiOTecHNOlOgy
a b
110 real 45 trajectory Milestone 2
and 229 synthetic + inference + 4 metrics network Lengths
datasets methods 3 4 Topology
Region of
delayed commitment
Accuracy + Scalability + Stability + Usability
ab
Cells c Branch Multi-
assignment layered
d e
New possibilities
User guidelines +
for developers
a
b
Method wrappers methods.dynverse.org c Cell positions
Guidelines app guidelines.dynverse.org
Benchmarking pipeline benchmark.dynverse.org d e
cc
Cycle Linear Bifurcation Multifurcation Tree Connected Disconnected
graph graph
d Benchmarking metrics
Topology: HIM Branch assignment: F1 Cell positions: cor Features (genes): wcor
branches dist featureimp
Reference Prediction Geodesic distances between
1 1 all pairs of cells
22 G1
2 G2
3 3 G3
3
Match branches 2 Feature importance
Difference in relative 1
edge lengths 2 G1 G1
3 3 1 1 G2 G2
+ 22 G3 G3
Difference in degree
distributions
Magnitude of overlap Correlation of distances Correlation of importances
Fig. 1 | overview of several key aspects of the evaluation. a, A schematic overview of our evaluation pipeline. b, To make the trajectories comparable
to each other, a common trajectory model was used to represent reference trajectories from the real and synthetic datasets, as well as any predictions
of TI methods. c, Trajectories are automatically classified into one of seven trajectory types, with increasing complexity. d, We defined four metrics,
each assessing the quality of a different aspect of the trajectory. The HIM score assesses the similarity between the two topologies, taking into account
differences in edge lengths and degree distributions. The F1 assesses the similarity of the assignment of cells onto branches. The cor quantifies the
branches dist
similarity in cellular positions between two trajectories, by calculating the correlation between pairwise geodesic distances. Finally, wcor quantifies
features
the agreement between trajectory differentially expressed features from the known trajectory and the predicted trajectory.
harder to know a priori, and which can potentially introduce a large well across the board (Fig. 2b). We will discuss each evaluation cri-
bias into the analysis (Fig. 2a). terion in more detail (Fig. 3 and Supplementary Fig. 2), after which
The largest difference between TI methods is whether a method we conclude with guidelines for method users and future perspec-
fixes the topology and, if it does not, what kind of topology it can tives for method developers.
detect. We defined seven possible types of topology, ranging from
very basic topologies (linear, cyclical and bifurcating) to the more Accuracy. We defined several metrics to compare a prediction to a
complex ones (connected and disconnected graphs). Most methods reference trajectory (Supplementary Note 1). Based on an analysis
either focus on inferring linear trajectories or limit the search to tree of their robustness and conformity to a set of rules (Supplementary
or less complex topologies, with only a selected few attempting to Note 1), we chose four metrics each assessing a different aspect of
infer cyclic or disconnected topologies (Fig. 2a). a trajectory (Fig. 1d): the topology (Hamming–Ipsen–Mikhailov,
We evaluated each method on four core aspects: (1) accuracy of a HIM), the quality of the assignment of cells to branches (F1 ),
branches
prediction, given a gold or silver standard on 110 real and 229 syn- the cell positions (cor ) and the accuracy of the differentially
dist
thetic datasets; (2) scalability with respect to the number of cells and expressed features along the trajectory (wcor ). The data com-
features
features (for example, genes); (3) stability of the predictions after pendium consisted of both synthetic datasets, which offer the most
subsampling the datasets; and (4) the usability of the tool in terms exact reference trajectory, and real datasets, which provide the high-
of software, documentation and the manuscript. Overall, we found est biological relevance. These real datasets come from a variety of
a large diversity across the four evaluation criteria, with only a few single-cell technologies, organisms and dynamic processes, and con-
methods, such as PAGA, Slingshot and SCORPIUS, performing tain several types of trajectory topologies (Supplementary Table 2).
548 NATuRe BioTeCHNologY | VOL 37 | MAY 2019 | 547–554 | www.nature.com/naturebiotechnology
NATure BiOTecHNOlOgy Articles
a Method b Summary
Inferrable trajectory types Aggregated scores per experiment
Priors req W u r i a re p d per P ty la p t e form Topology i C nf y e c r l e e
nce
Linear Bifurcatio M n ultifurca T t r i e o e n Connecte D d isconnected Overall Accuracy Scalability Stability Usability
Graph methods
Direct Python Free
RaceID / StemID Proj R Free
SLICER Cell R Free
Tree methods
Slingshot Direct R Free
PAGA Tree Direct Python Free
MST Proj R Free Off-the-shelf
pCreode Proj Python Free
SCUBA ClusterPython Free
Monocle DDRTree Cell R Free
Monocle ICA Cell R Param
cellTree maptpx Cell R Free
SLICE Direct R Free
cellTree VEM Cell R Free
ElPiGraph Direct R Free
Sincell Cell R Free
URD Direct R Free
CellTrails Cell R Free
Mpath Cluster R Free
CellRouter Cell R Free
Multifurcation methods
STEMNET Prob R Param
FateID Prob R Param
MFA Prob R Param
GPfates Prob PythonParam
Bifurcation methods
DPT Direct R Fixed
Wishbone Direct PythonParam
Linear methods
SCORPIUS Linear R Fixed
Component 1 Linear R Fixed Off-the-shelf
Embeddr Linear R Fixed
MATCHER Linear Python Fixed
TSCAN Linear R Fixed
Wanderlust Linear Python Fixed
PhenoPath Linear R Fixed
topslam Linear Python Fixed
Waterfall Linear R Fixed
ElPiGraph linear Direct R Fixed
ouijaflow Linear Python Fixed
FORKS Linear Python Fixed
Cyclic methods
Angle Cycle R Fixed Off-the-shelf
ElPiGraph cycle Direct R Fixed
reCAT Cycle R Fixed
Prior information required Not shown, insufficient data points
None CALISTA ouija
Weak: Start or end cells cellTree Gibbs pseudogp
Strong: Cell grouping or time course GrandPrix SCIMITAR
MERLoT SCOUP
Fig. 2 | A characterization of the 45 methods evaluated in this study and their overall evaluation results. a, We characterized the methods according
to the wrapper type, their required priors, whether the inferred topology is constrained by the algorithm (fixed) or a parameter (param), and the types of
inferable topologies. The methods are grouped vertically based on the most complex trajectory type they can infer. b, The overall results of the evaluation
on four criteria: accuracy using a reference trajectory on real and synthetic data, scalability with increasing number of cells and features, stability across
dataset subsamples and quality of the implementation. Methods that errored on more than 50% of the datasets are not included in this figure and are
shown instead in Supplementary Fig. 2.
Real datasets were classified as ‘gold standard’ if the reference trajec- number of differentially expressed genes, drop-out rates and other
tory was not extracted from the expression data itself, such as via statistical properties36.
cellular sorting or cell mixing34. All other real datasets were classi- We found that method performance was very variable across
fied as ‘silver standard’. For synthetic datasets we used several data datasets, indicating that there is no ‘one-size-fits-all’ method that
simulators, including a simulator of gene regulatory networks using works well on every dataset (Supplementary Fig. 3a). Even meth-
a thermodynamic model of gene regulation35. For each simula- ods that can detect most of the trajectory types, such as PAGA,
tion, we used a real dataset as a reference, to match its dimensions, RaceID/StemID and SLICER were not the best methods across all
NATuRe BioTeCHNologY | VOL 37 | MAY 2019 | 547–554 | www.nature.com/naturebiotechnology 549
Articles NATure BiOTecHNOlOgy
a Method b Accuracy c Scalability d Stability e Usability
Predicted time (no. of Similarity Quality of
Per metric Per dataset source Per trajectory type
cells × no. of features) between runs software and paper
Topooo B lloo r gg a yy n C ch e l a l s p F s o i e s g i a n ti t m o u n G r e e s n o s t ld Silve D r yng D en ynto P y RO S S p S la T tt T e C r yccllleee Linea B r ifur C c o a n tio ve n M rg u e lt T n ifu c re e rc e a A t c io y n c C lic onn D e i c s t c e o d n 1 n m ec × t 1 e 0 1 d 0 0 0 k 1 0 × k 1 1 × k k 1 0 × 1 k 1 0 0 0 0 × C k o 1 r m . p T re o d ppp i ooo c B ll t oo e r gg a d yy n v c C e h e r s l a l u s p s s F o i r g e s e i n a t a i m t o u l A n e re v s n a s t ila B b e il h it a y C v o io d u e C r a o s dd s eee u D r qq o a uu c n aa u c P ll m ii e a ttyy e p n e t r ation
Graph methods
PAGA 1 h 7 m 55 s 19 s 25 s0.82
RaceID / StemID >7 d 1 d 1 h 1 h 14 h0.77
SLICER >7 d>7 d 2 h 31 s <1 s0.99
Tree methods
Slingshot >7 d11 h56 m 2 m 52 s0.98
PAGA Tree 2 h 8 m 1 m 20 s 15 s0.88
MST 56 m8 m12 m 2 m 52 s0.90 Off-the-shelf
pCreode >7 d 1 d 2 h 3 m 58 s0.89
SCUBA >7 d 3 d 4 h 10 m3 m0.86
Monocle DDRTree 1 h 26 m 2 h 14 h 2 d 0.86
Monocle ICA >7 d 2 d 1 h 1 h 1 d 0.95
cellTree maptpx >7 d>7 d 6 h 1 h 24 m0.51
SLICE >7 d>7 d 1 h 51 m 1 d 0.78
cellTree VEM >7 d23 h39 m10 m15 m0.78
ElPiGraph 12 h 1 d 6 h 20 m7 m0.93
Sincell >7 d>7 d 2 h 5 m 2 m0.97
URD >7 d 1 d 2 h 10 m1 m0.68
CellTrails >7 d>7 d 2 d 7 h 4 h 0.76
Mpath >7 d>7 d 8 h 4 h 1 d 0.90
CellRouter >7 d 1 d 1 h 9 m 9 m0.24
Multifurcation methods
STEMNET 1 h 36 m12 m 7 m 6 m0.64
FateID 1 d 6 h 1 h 26 m20 m0.71
MFA 5 h 9 h 9 h 9 h 7 h 0.86
GPfates >7 d>7 d 4 d 2 h 13 m0.75
Bifurcation methods
DPT 24 m36 m40 m 7 m 56 s0.76
Wishbone 1 d 2 h 17 m 6 m 7 m0.66
Linear methods
SCORPIUS 13 h 1 h 4 m 4 m 4 m0.96
Component 1 34 s 2 m11 m 3 m 51 s0.92 Off-the-shelf
Embeddr >7 d 2 d 33 m 2 m 34 s0.93
MATCHER 2 h 3 h 1 h 16 m3 m0.91
TSCAN 24 m7 m 9 m 7 m11 m0.96
Wanderlust 1 d 2 h 16 m 5 m 7 m0.73
PhenoPath 1 h 5 h 9 h 4 d >7 d0.83
topslam >7 d>7 d 1 d 4 h 8 h 0.99
Waterfall 47 m8 m13 m 2 m 51 s0.89
ElPiGraph linear 2 h 2 h 1 h 8 m 5 m0.92
ouijaflow >7 d>7 d20 h >7 d 3 d 0.80
FORKS 4 m 5 m25 m 5 m 2 m0.04
Cyclic methods
Angle 35 s 2 m10 m 3 m 54 s0.96 Off-the-shelf
ElPiGraph cycle 2 h 2 h 1 h 8 m 5 m0.92
reCAT 13 h 1 d 9 h 1 d >7 d0.92
Score Not shown, insufficient data points
CALISTA ouija
cellTree Gibbs pseudogp
0 0.2 0.4 0.6 0.8 1 GrandPrix SCIMITAR
MERLoT SCOUP
Fig. 3 | Detailed results of the four main evaluation criteria: accuracy, scalability, stability and usability. a, The names of the methods, ordered as in
Fig. 2. b, Accuracy of trajectory inference methods across metrics, dataset sources and dataset trajectory types. The performance of a method is generally
more stable across dataset sources, but very variable depending on the metric and trajectory type. c, Predicted execution times for varying numbers
of cells and features (no. of cells × no. of features). Predictions were made by training a regression model after running each method on bootstrapped
datasets with varying numbers of cells and features. k, thousands; m, millions; cor, correlation. d, Stability results by calculating the average pairwise
similarity between models inferred across multiple runs of the same method. e, Usability scores of the tool and corresponding manuscript, grouped per
category. Off-the-shelf methods were directly implemented in R and thus do not have a usability score.
trajectory types (Fig. 3b). The overall score between the different the accuracy of the gold standard trajectories and the relevance
dataset sources was moderately to highly correlated (Spearman rank of the synthetic data. On the other hand, the different metrics
correlation between 0.5–0.9) with the scores on real datasets con- frequently disagreed with each other, with Monocle and PAGA Tree
taining a gold standard (Supplementary Fig. 3b), confirming both scoring better on the topology scores, whereas other methods, such
550 NATuRe BioTeCHNologY | VOL 37 | MAY 2019 | 547–554 | www.nature.com/naturebiotechnology
NATure BiOTecHNOlOgy Articles
1 RunningPAGA Tree on all datasets All trajectory
will result in a top model 27% of the time types
PAGA Tree SCORPIUS Slingshot AngleMonocle PAGA
Whileother methods perform less well ICA
2 will resu R lt u in n n a i t n l g e a b s o t t h o n P e A t G op A m Tr o e d e e l a 4 n 5 d % S o C f O th R e P t I im US e Linear → tree Slingshot PAGA Tree SCORPIUSMonocle MFA cellTree
ICA maptpx
3 PAGA Tree, SCORPIUS and Slingshot Cycle
≥ 1 top model 57% of the time reCAT Angle
4 Add Angle 64% Linear
5 Add Monocle ICA SCORPIUS Embeddr Monocle
70% ICA
6 Add PAGA Bifurcation
74% Slingshot SLICE PAGA TreecellTree MFA
7 Add cellTree ma 7 p 8 tp % x Multifurcation maptpx
8 Add Embeddr PAGA Tree Slingshot MERLoT
81%
Tree
9 Add MER 8 L 4 o % T RaceID / PAGA Tree Monocle PAGA pCreode
10 Add Grand 8 P 7 r % ix Co g n r n a e p c h ted StemID ICA
PAGA RaceID /
11 Add re 9 C 0 A % T Disconnected StemID
12 Add pCreode graph PAGA RRaacceID /
92% StemID
25 50 75 100 0 25 50 75 100
Likelihood of obtaining a top model (%) Likelihood of obtaining a top model (%)
as Slingshot, were better at ordering the cells and placing them into the increasing demands on the number of features38. To assess
the correct branches (Fig. 3b). the scalability, we ran each method on up- and downscaled ver-
The performance of a method was strongly dependent on the sions of five distinct real datasets. We modeled the running time
type of trajectory present in the data (Fig. 3b). Slingshot typically and memory usage using a Shape Constrained Additive Model39
performed better on datasets containing more simple topologies, (Supplementary Fig. 4a). As a control, we compared the predicted
while PAGA, pCreode and RaceID/StemID had higher scores on time (and memory) with the actual time (respectively memory) on
datasets with trees or more complex trajectories (Supplementary all benchmarking datasets, and found that these were highly cor-
Fig. 3c). This was reflected in the types of topologies detected related overall (Spearman rank correlation >0.9, Supplementary
by every method, as those predicted by Slingshot tended to con- Fig. 5), and moderately to highly correlated (Spearman rank cor-
tain less branches, whereas those detected by PAGA, pCreode and relation of 0.5–0.9) for almost every method, depending to what
Monocle DDRTree gravitated towards more complex topologies extent the execution of a method succeeded during the scalability
(Supplementary Fig. 3d). This analysis therefore indicates that experiments (Fig. 3c and Supplementary Fig. 2a).
detecting the right topology is still a difficult task for most of these We found that the scalability of most methods was overall very
methods, because methods tend to be either too optimistic or too poor, with most graph and tree methods not finishing within an
pessimistic regarding the complexity of the topology in the data. hour on a dataset with ten thousand cells and ten thousand fea-
The high variability between datasets, together with the diver- tures (Fig. 3c), which is around the size of a typical droplet-based
sity in detected topologies between methods, could indicate some single-cell dataset37. Running times increased further with increas-
complementarity between the different methods. To test this, we ing number of cells, with only a handful of graph/tree methods
calculated the likelihood of obtaining a top model when using only completing within a day on a million cells (PAGA, PAGA Tree,
a subset of all methods. A top model in this case was defined as Monocle DDRTree, Stemnet and GrandPrix). Some methods, such
a model with an overall score of at least 95% as the best model. as Monocle DDRTree and GrandPrix, also suffered from unsatisfac-
On all datasets, using one method resulted in getting a top model tory running times when given a high number of features.
about 27% of the time. This increased up to 74% with the addition Methods with a low running time typically had two defining
of six other methods (Fig. 4a). The result was a relatively diverse aspects: they had a linear time complexity with respect to the fea-
set of methods, containing both strictly linear or cyclic methods, tures and/or cells, and adding new cells or features led to a relatively
and methods with a broad trajectory type range such as PAGA. low increase in time (Supplementary Fig. 4b). We found that more
We found similar indications of complementarity between the top than half of all methods had a quadratic or superquadratic complex-
methods on data containing only linear, bifurcation or multifur- ity with respect to the number of cells, which would make it difficult
cating trajectories (Fig. 4b), although in these cases less methods to apply any of these methods in a reasonable time frame on datas-
were necessary to obtain at least one top model for a given dataset. ets with more than a thousand cells (Supplementary Fig. 4b).
Altogether, this shows that there is considerable complementar- We also assessed the memory requirements of each method
ity between the different methods and that users should try out a (Supplementary Fig. 2c). Most methods had reasonable mem-
diverse set of methods on their data, especially when the topology is ory requirements for modern workstations or computer clusters
unclear a priori. Moreover, it also opens up the possibilities for new (≤12 GB) with PAGA and STEMNET in particular having a low
ensemble methods that utilize this complementarity. memory usage with both a high number of cells or a high number
of features. Notably, the memory requirements were very high for
Scalability. While early TI methods were developed at a time where several methods on datasets with high numbers of cells (RaceID/
profiling more than a thousand cells was exceptional, methods StemID, pCreode and MATCHER) or features (Monocle DDRTree,
now have to cope with hundreds of thousands of cells, and perhaps SLICE and MFA).
soon with more than ten million37. Moreover, the recent applica- Altogether, the scalability analysis indicated that the dimensions
tion of TI methods on multi-omics single-cell data also showcases of the data are an important factor in the choice of method, and
sdohtem
fo
rebmuN
a b
Number of methods 1 2 3 4 5 6
Fig. 4 | Complementarity between different trajectory inference methods. a, We assessed the likelihood for different combinations of methods to lead
to a ‘top model’ (defined as a model with an overall score of at least 95% of the best model) when applied to all datasets. b, The likelihood for different
combinations of methods to lead to a ‘top model’ was assessed separately on different trajectory types. For this figure, we did not include any methods
requiring a cell grouping or a time course as prior information.
NATuRe BioTeCHNologY | VOL 37 | MAY 2019 | 547–554 | www.nature.com/naturebiotechnology 551
Articles NATure BiOTecHNOlOgy
Estimated running time
(cells × features)
AccuracyUsability 100 k × 1 k 10 k × 10 k 1 k × 100 k Required priors
≤ Disconnected RaceID / S P te A m G ID A + – ± ± 7 1 m d 5 1 5 h s 1 1 9 h s Start cell(s)
≤ Graph PAGA + ± 7 m 55 s 19 s Start cell(s)
Yes / I don’t know RaceID / StemID – ± 1 d 1 h 1 h
Yes / I don’t know SLICER – ± >7 d 2 h 31 s Start cell(s)
Do you expect
Do m yo u u lt i e p x le pect cy to c p le o s lo in g y t ? he I don N ’t o k / now ≤ Tree Slin P g A s G ho A t ± + + ± 1 7 1 m h 5 5 6 5 m s 1 2 9 m s Start cell(s)
disconnected Monocle ICA ± + 2 d 1 h 1 h Number of end and start states
trajectories? No Do you expect a MST ± 8 m 12 m 2 m
No tree with two or Tree PAGA + ± 7 m 55 s 19 s Start cell(s)
No more bifurcations? Yes MST ± 8 m 12 m 2 m
Do a y p o a u rt i e cu xp la e r ct Free topology RaceID S / l S in t g e s m h I o D t ± ± ± + 1 1 1 d h 5 1 6 h m 2 1 m h
topology? Fixed topology Multifurcation STEMNET + ± 36 m 12 m 7 m End cell(s), Cell clustering
Slingshot + + 11 h 56 m 2 m
Yes PAGA + ± 7 m 55 s 19 s Start cell(s)
FateID + ± 6 h 1 h 26 m Cell clustering, Start and end cells
Bifurcation Slingshot + + 11 h 56 m 2 m
FateID + ± 6 h 1 h 26 m Cell clustering, Start and end cells
GrandPrix ± ± 7 m 28 m >7 d No. of end states
STEMNET ± ± 36 m 12 m 7 m End cell(s), Cell clustering
Linear SCORPIUS + ± 1 h 4 m 4 m
Embeddr + ± 2 d 33 m 2 m
Confirm Check out the TSCAN + + 7 m 9 m 7 m
expectations Confirm results interactive Slingshot + + 11 h 56 m 2 m
using a method u tw si o n g m a e t t h le o a d s s t dynverse guidelines at Cycle Angle + 2 m 10 m 3 m
with free topology guidelines.dynverse.org ElPiGraph cycle ± ± 2 h 1 h 8 m
reCAT ± – 1 d 9 h 1 d
RaceID / StemID – ± 1 d 1 h 1 h
Fig. 5 | Practical guidelines for method users. As the performance of a method mostly depends on the topology of the trajectory, the choice of TI method
will be primarily influenced by the user’s existing knowledge about the expected topology in the data. We therefore devised a set of practical guidelines,
which combines the method’s performance, user friendliness and the number of assumptions a user is willing to make about the topology of the trajectory.
Methods to the right are ranked according to their performance on a particular (set of) trajectory type. Further to the right are shown the accuracy
(+: scaled performance ≥ 0.9, ±: >0.6), usability scores (+:≥0.9, ± ≥0.6), estimated running times and required prior information. k, thousands; m, millions.
that method development should pay more attention to maintain- Installation issues seem to be quite general in bioinformatics41 and
ing reasonable running times and memory usage. the trajectory inference field is no exception.
We found that most methods fulfilled the basic criteria, such as the
Stability. It is not only important that a method is able to infer an availability of a tutorial and elemental code quality criteria (Fig. 3d
accurate model in a reasonable time frame, but also that it pro- and Supplementary Fig. 6). While recent methods had a slightly bet-
duces a similar model when given very similar input data. To test ter quality score than older methods, several quality aspects were
the stability of each method, we executed each method on ten consistently lacking for the majority of the methods (Supplementary
different subsamples of the datasets (95% of the cells, 95% of the Fig. 6 right) and we believe that these should receive extra attention
features), and calculated the average similarity between each pair from developers. Although these outstanding issues covered all five
of models using the same scores used to assess the accuracy of a categories, code assurance and documentation in particular were
trajectory (Fig. 3d). problematic areas, notwithstanding several studies pinpointing
Given that the trajectories of methods that fix the topology either these as good practices42,43. Only two methods had a nearly perfect
algorithmically or through a parameter are already very constrained, usability score (Slingshot and Celltrails), and these could be used
it is to be expected that such methods tend to generate very stable as an inspiration for future methods. We observed no clear relation
results. Nonetheless, some fixed topology methods still produced between usability and method accuracy or usability (Fig. 2b).
slightly more stable results, such as SCORPIUS and MATCHER for
linear methods and MFA for multifurcating methods. Stability was Discussion
much more diverse among methods with a free topology. Slingshot In this study, we presented a large-scale evaluation of the perfor-
produced more stable models than PAGA (Tree), which in turn pro- mance of 45 TI methods. By using a common trajectory representa-
duced more stable results than pCreode and Monocle DDRTree. tion and four metrics to compare the methods’ outputs, we were
able to assess the accuracy of the methods on more than 200 data-
Usability. While not directly related to the accuracy of the inferred sets. We also assessed several other important quality measures,
trajectory, it is also important to assess the quality of the implemen- such as the quality of the method’s implementation, the scalability
tation and how user-friendly it is for a biological user40. We scored to hundreds of thousands of cells and the stability of the output on
each method using a transparent checklist of important scientific small variations of the datasets.
and software development practices, including software packaging, Based on the results of our benchmark, we propose a set of prac-
documentation, automated code testing and publication into a peer- tical guidelines for method users (Fig. 5 and guidelines.dynverse.
reviewed journal (Supplementary Table 3). It is important to note org). We postulate that, as a method’s performance is heavily depen-
that there is a selection bias in the tools chosen for this analysis, dent on the trajectory type being studied, the choice of method
as we did not include a substantial set of tools due to issues with should currently be primarily driven by the anticipated trajectory
installation, code availability and executability on a freely avail- topology in the data. For most use cases, the user will know very
able platform (which excludes MATLAB). The reasons for not little about the expected trajectory, except perhaps whether the data
including certain tools are all discussed on our repository (https:// is expected to contain multiple disconnected trajectories, cycles or
github.com/dynverse/dynmethods/issues?q=label:unwrappable). a complex tree structure. In each of these use cases, our evaluation
552 NATuRe BioTeCHNologY | VOL 37 | MAY 2019 | 547–554 | www.nature.com/naturebiotechnology
NATure BiOTecHNOlOgy Articles
a
Reference Component 1 TSCAN SCORPIUS Waterfall Monocle ICA Slingshot PAGA
(consensus)
CDP MDP PreDC
b
Reference pCreode PAGA Slingshot MST DPT SCUBA Monocle RaceID / StemID
(consensus) DDRTree
d2_induced d2_intermediate d5_earlyiN d5_intermediate MEF Myocyte Neuron
c d
Reference RaceID / StemID PAGA MST Reference Angle RaceID / StemID PAGA
(consensus) (consensus)
Fig. 6 | Demonstration of how a common framework for Ti methods facilitates broad applicability using some example datasets. Trajectories inferred
by each method were projected to a common dimensionality reduction using multidimensional scaling. For each dataset, we also calculated a ‘consensus’
prediction, by calculating the cor between each pair of models and picking the model with the highest score on average. a, The top methods applied on a
dist
dataset containing a linear trajectory of differentiation dendritic cells, going from MDP, CDP to PreDC. b, The top methods applied on a dataset containing
a bifurcating trajectory of reprogrammed fibroblasts. c, A synthetic dataset generated by dyntoy, containing four disconnected trajectories. d, A synthetic
dataset generated by dyngen, containing a cyclic trajectory.
suggests a different set of optimal methods, as shown in Fig. 5. be extended to allow additional input data, such as spatial and
Several other factors will also impact the choice of methods, such RNA velocity information45, and easier downstream analyses. In
as the dimensions of the dataset and the prior information that is addition, further discussion within the field is required to arrive
available. These factors and several others can all be dynamically at a consensus concerning a common interface for trajectory
explored in our interactive app (guidelines.dynverse.org). This app models, which can include additional features such as uncertainty
can also be used to query the results of this evaluation, such as filter- and gene importance.
ing the datasets or changing the importance of the evaluation met- Our study indicates that the field of trajectory inference is matur-
rics for the final ranking. ing, primarily for linear and bifurcating trajectories (Fig. 6a,b).
When inferring a trajectory on a dataset of interest, it is impor- However, we also highlight several ongoing challenges, which
tant to take two further points into account. First, it is critical that a should be addressed before TI can be a reliable tool for analyzing
trajectory, and the downstream results and/or hypotheses originat- single-cell omics datasets with complex trajectories. Foremost, new
ing from it, are confirmed by multiple TI methods. This is to make methods should focus on improving the unbiased inference of tree,
sure that the prediction is not biased due to the given parameter set- cyclic graph and disconnected topologies, as we found that meth-
ting or the particular algorithm underlying a TI method. The value ods repeatedly overestimate or underestimate the complexity of the
of using different methods is further supported by our analysis indi- underlying topology, even if the trajectory could easily be identified
cating substantial complementarity between the different methods. using a dimensionality reduction method (Fig. 6c,d). Furthermore,
Second, even if the expected topology is known, it can be beneficial higher standards for code assurance and documentation could help
to also try out methods that make less assumptions about the trajec- in adopting these tools across the single-cell omics field. Finally,
tory topology. When the expected topology is confirmed using such new tools should be designed to scale well with the increasing num-
a method, it provides additional evidence to the user. When a more ber of cells and features. We found that only a handful of current
complex topology is produced, this could indicate that the underly- methods can handle datasets with more than 10,000 cells within a
ing biology is much more complex than anticipated by the user. reasonable time frame. To support the development of these new
Critical to the broad applicability of TI methods is the stan- tools, we provide a series of vignettes on how to wrap and evaluate
dardization of the input and output interfaces of TI methods, so a method on the different measures proposed in this study at
that users can effortlessly execute TI methods on their dataset of https://benchmark.dynverse.org.
interest, compare different predicted trajectories and apply down- We found that the performance of a method can be very vari-
stream analyses, such as finding genes important for the trajectory, able between datasets, and therefore included a large set of both real
network inference11 or finding modules of genes44. Our framework and synthetic data within our evaluation, leading to a robust over-
is an initial attempt at tackling this problem, and we illustrate its all ranking of the different methods. However, ‘good-yet-not-the-
usefulness here by comparing the predicted trajectories of several best’ methods46 can still provide a very valuable contribution to the
top-performing methods on datasets containing a linear, tree, cyclic field, especially if they make use of novel algorithms, return a more
and disconnected graph topology (Fig. 6). Using our framework, scalable solution or provide a unique insight in specific use cases.
this figure can be recreated using only a couple of lines of R code This is also supported by our analysis of method complementarity.
(https://methods.dynverse.org). In the future, this framework could Some examples for the latter include PhenoPath, which can include
NATuRe BioTeCHNologY | VOL 37 | MAY 2019 | 547–554 | www.nature.com/naturebiotechnology 553
Articles NATure BiOTecHNOlOgy
additional covariates in its model, ouija, which returns a measure of 26. Qiu, X. et al. Reversed graph embedding resolves complex single-cell
uncertainty of each cell’s position within the trajectory, and StemID, trajectories. Nat. Methods 14, 979–982 (2017).
27. Street, K. et al. Slingshot: cell lineage and pseudotime inference for single-cell
which can infer the directionality of edges within the trajectory.
transcriptomics. BMC Genomics 19, 477 (2018).
28. Ji, Z. & Ji, H. TSCAN: pseudo-time reconstruction and evaluation in
online content single-cell RNA-seq analysis. Nucleic Acids Res. 44, e117–e117 (2016).
Any methods, additional references, Nature Research reporting 29. Welch, J. D., Hartemink, A. J. & Prins, J. F. SLICER: inferring branched,
summaries, source data, statements of data availability, and asso- nonlinear cellular trajectories from single cell RNA-seq data. Genome. Biol.
17, 106 (2016).
ciated accession codes are available at https://doi.org/10.1038/
30. duVerle, D. A., Yotsukura, S., Nomura, S., Aburatani, H. & Tsuda, K.
s41587-019-0071-9. CellTree: an R/bioconductor package to infer the hierarchical structure of
cell populations from single-cell RNA-seq data. BMC Bioinformatics 17,
Received: 5 April 2018; Accepted: 13 February 2019; 363 (2016).
Published online: 1 April 2019 31. Cannoodt, R. et al. SCORPIUS improves trajectory inference and identifies
novel modules in dendritic cell development. Preprint at bioRxiv https://doi.
org/10.1101/079509 (2016).
References
32. Lönnberg, T. et al. Single-cell RNA-seq and computational analysis using
1. Tanay, A. & Regev, A. Scaling single-cell genomics from phenomenology to temporal mixture modeling resolves TH1/TFH fate bifurcation in malaria.
mechanism. Nature 541, 21350 (2017). Sci. Immunol. 2, eaal2192 (2017).
2. Etzrodt, M., Endele, M. & Schroeder, T. Quantitative single-cell approaches to 33. Campbell, K. R. & Yau, C. Probabilistic modeling of bifurcations in single-cell
stem cell research. Cell Stem Cell 15, 546–558 (2014). gene expression data using a Bayesian mixture of factor analyzers. Wellcome
3. Trapnell, C. Defining cell types and states with single-cell genomics. Genome Open Res. 2, 19 (2017).
Res. 25, 1491–1498 (2015). 3 4. Tian, L. et al. scRNA-seq mixology: Towards better benchmarking of
4. Cannoodt, R., Saelens, W. & Saeys, Y. Computational methods for single cell RNA-seq protocols and analysis methods. Preprint at bioRxiv
trajectory inference from single-cell transcriptomics. Eur. J. Immunol. 46, https://doi.org/10.1101/433102 (2018).
2496–2506 (2016). 35. Schaffter, T., Marbach, D. & Floreano, D. GeneNetWeaver: in silico
5. Moon, K. R. et al. Manifold learning-based methods for analyzing single-cell benchmark generation and performance profiling of network inference
RNA-sequencing data. Curr. Opin. Syst. Biol. 7, 36–46 (2018). methods. Bioinformatics 27, 2263–2270 (2011).
6. Liu, Z. et al. Reconstructing cell cycle pseudo time-series via single-cell 36. Zappia, L., Phipson, B. & Oshlack, A. Splatter: simulation of single-cell RNA
transcriptome data. Nat. Commun. 8, 22 (2017). sequencing data. Genome. Biol. 18, 174 (2017).
7. Wolf, F. A. et al. PAGA: graph abstraction reconciles clustering with 37. Svensson, V., Vento-Tormo, R. & Teichmann, S. A. Exponential scaling of
trajectory inference through a topology preserving map of single cells. single-cell RNA-seq in the past decade. Nat. Protoc. 13, 599–604 (2018).
Genome Biol. 20, 59 (2019). 38. Cao, J. et al. Joint profiling of chromatin accessibility and gene expression in
8. Schlitzer, A. et al. Identification of cDC1- and cDC2-committed DC thousands of single cells. Science 361, 1380–1385 (2018).
progenitors reveals early lineage priming at the common DC progenitor stage 39. Pya, N. & Wood, S. N. Shape constrained additive models. Stat. Comput. 25,
in the bone marrow. Nat. Immunol. 16, 718–728 (2015). 543–559 (2015).
9. Velten, L. et al. Human haematopoietic stem cell lineage commitment is a 40. Taschuk, M. & Wilson, G. Ten simple rules for making research software
continuous process. Nat. Cell Biol. 19, 271–281 (2017). more robust. PLoS Comput. Biol. 13, e1005412 (2017).
10. See, P. et al. Mapping the human DC lineage through the integration of 41. Mangul, S. et al. A comprehensive analysis of the usability and archival
high-dimensional techniques. Science 356, eaag3009 (2017). stability of omics computational tools and resources. Preprint at bioRxiv
11. Aibar, S. et al. SCENIC: Single-cell regulatory network inference and https://doi.org/10.1101/452532 (2018).
clustering. Nat. Methods 14, 1083–1086 (2017). 42. Wilson, G. et al. Best practices for scientific computing. PLoS Biol. 12,
12. Regev, A. et al. Science forum: the human cell atlas. eLife 6, e27041 (2017). e1001745 (2014).
13. Han, X. et al. Mapping the mouse cell atlas by microwell-seq. Cell 172, 43. Artaza, H. et al. Top 10 metrics for life science software good practices.
1091–1107.e17 (2018). F1000Res. 5, 2000 (2016).
14. Schaum, N. et al. Single-cell transcriptomics of 20 mouse organs creates a 44. Saelens, W., Cannoodt, R. & Saeys, Y. A comprehensive evaluation of module
Tabula Muris. Nature 562, 367–372 (2018). detection methods for gene expression data. Nat. Commun. 9, 1090 (2018).
15. Angerer, P. et al. Single cells make big data: new challenges and opportunities 45. Manno, G. L. et al. RNA velocity of single cells. Nature 560, 494–498 (2018).
in transcriptomics. Curr. Opin. Syst. Biol. 4, 85–91 (2017). 46. Norel, R., Rice, J. J. & Stolovitzky, G. The self-assessment trap: Can we all be
16. Henry, V. J., Bandrowski, A. E., Pepin, A.-S., Gonzalez, B. J. & Desfeux, A. better than average? Mol. Syst. Biol. 7, 537 (2011).
OMICtools: an informative directory for multi-omic data analysis. Database
(Oxford) 2014, bau069 (2014).
Acknowledgements
17. Davis, S. et al. List of software packages for single-cell data analysis. https://
github.com/seandavi/awesome-single-cell (2018); https://doi.org/10.5281/ We would like to thank the original authors of the methods for their feedback and
zenodo.1294021 improvements on the method wrappers. This study was supported by the Fonds
18. Zappia, L., Phipson, B. & Oshlack, A. Exploring the single-cell RNA-seq Wetenschappelijk Onderzoek (R.C., 11Y6218N and W.S., 11Z4518N) and BOF (Ghent
analysis landscape with the scRNA-tools database. PLoS Comput. Biol. 14, University, H.T.). Y.S. is an ISAC Marylou Ingram scholar.
e1006245 (2018)
19. Bendall, S. C. et al. Single-cell trajectory detection uncovers progression Author contributions
and regulatory coordination in human B cell development. Cell 157,
R.C., W.S., H.T. and Y.S. designed the study. R.C. and W.S. performed the experiments
714–725 (2014).
and analyzed the data. W.S., R.C. and H.T. implemented software packages. R.C., W.S.,
20. Shin, J. et al. Single-cell RNA-seq with waterfall reveals molecular cascades
Y.S. and H.T. prepared the manuscript. Y.S. supervised the project.
underlying adult neurogenesis. Cell Stem Cell 17, 360–372 (2015).
21. Campbell, K. & Yau, C. Bayesian Gaussian Process Latent Variable Models
Competing interests
for pseudotime inference in single-cell RNA-seq data. Preprint at bioRxiv
https://doi.org/10.1101/026872 (2015). The authors declare no competing interests.
22. Haghverdi, L., Büttner, M., Wolf, F. A., Buettner, F. & Theis, F. J. Diffusion
pseudotime robustly reconstructs lineage branching. Nat. Methods 13,
Additional information
845–848 (2016).
23. Setty, M. et al. Wishbone identifies bifurcating developmental trajectories Supplementary information is available for this paper at https://doi.org/10.1038/
from single-cell data. Nat. Biotechnol. 34, 637–645 (2016). s41587-019-0071-9.
24. Trapnell, C. et al. The dynamics and regulators of cell fate decisions are Reprints and permissions information is available at www.nature.com/reprints.
revealed by pseudotemporal ordering of single cells. Nat. Biotechnol. 32,
Correspondence and requests for materials should be addressed to Y.S.
2859 (2014).
25. Matsumoto, H. & Kiryu, H. SCOUP: a probabilistic model based on the Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in
Ornstein–Uhlenbeck process to analyze single-cell expression data during published maps and institutional affiliations.
differentiation. BMC Bioinformatics 17, 232 (2016). © The Author(s), under exclusive licence to Springer Nature America, Inc. 2019
554 NATuRe BioTeCHNologY | VOL 37 | MAY 2019 | 547–554 | www.nature.com/naturebiotechnology
NATure BiOTecHNOlOgy Articles
Methods milestones and sums for each cell to one. (3) The regions of delayed commitment
Trajectory inference methods. We gathered a list of 71 trajectory inference tools define connections between three or more milestones. These must be explicitly
(Supplementary Table 1) by searching the literature for ‘trajectory inference’ defined in the trajectory model and per region one milestone must be directly
and ‘pseudotemporal ordering’, and based on two existing lists found online: connected to all other milestones of the region.
https://github.com/seandavi/awesome-single-cell17 and https://github.com/agitter/ Depending on the output of a method, we used different strategies to convert
single-cell-pseudotime47. We welcome any contributions by creating an issue at the output to our model (Supplementary Fig. 1b). Special conversions are denoted
https://methods.dynverse.org. by an asterisk and will be explained in more detail in the second list below.
Methods were excluded from the evaluation based on several criteria: • Type 1, direct: CALISTA*, DPT*, ElPiGraph, ElPiGraph cycle, ElPiGraph
(1) not freely available; (2) no code available; (3) superseded by another method; linear, MERLoT, PAGA, SLICE*, Slingshot, URD* and Wishbone. The
(4) requires data types other than expression; (5) no programming interface; wrapped method directly returned a network of milestones, the regions of
(6) unresolved errors during wrapping; (7) too slow (requires more than 1 h on delayed commitment and for each cell it is given to what extent it belongs
a 100 × 100 dataset); (8) does not return an ordering; and (9) requires additional to a milestone. In some cases, this indicates that additional transformations
user input during the algorithm (other than prior information). The discussions were required for the method, not covered by any of the following output
on why these methods were excluded can be found at https://github.com/dynverse/ formats. Some methods returned a branch network instead of a milestone
dynmethods/issues?q=label:unwrappable. In the end, we included 45 methods in network and this network was converted by calculating the line graph of the
the evaluation. branch network.
• Type 2, linear pseudotime: Component 1, Embeddr, FORKS, MATCHER,
Method wrappers. To make it easy to run each method in a reproducible ouija, ouijaflow, PhenoPath, pseudogp, SCIMITAR, SCORPIUS, topslam,
manner, each method was wrapped within Docker and singularity containers TSCAN, Wanderlust and Waterfall. The method returned a pseudotime, which
(available at https://methods.dynverse.org). These containers are automatically is translated into a linear trajectory where the milestone network contains two
built and tested using Travis continuous integration (https://travis-ci.org/ milestones and cells are positioned between these two milestones.
dynverse) and can be ran using both Docker and Singularity. For each method, • Type 3, cyclical pseudotime: Angle and reCAT. The method returned a
we wrote a wrapper script based on example scripts or tutorials provided by the pseudotime, which is translated into a cyclical trajectory where the mile-
authors (as mentioned in the respective wrapper scripts). This script reads in stone network contains three milestones and cells are positioned between
the input data, runs the method and outputs the files required to construct a these three milestones. These milestones were positioned at pseudotime 0,
trajectory. We also created a script to generate an example dataset, which is used 1/3 and 2/3.
for automated testing. • Type 4, end state probability: FateID, GPfates, GrandPrix, MFA*, SCOUP
We used the Github issues system to contact the authors of each method, and and STEMNET. The method returned a pseudotime and for each cell and end
asked for feedback on the wrappers, the metadata and the usability scores. About state a probability (Pr) for how likely a cell will end up in a certain end state.
one-third of the authors responded and we improved the wrappers based on This was translated into a star-shaped milestone network, with one starting
their feedback. These discussions can be viewed on Github: https://github.com/ milestone (M) and several outer milestones (M), with regions of delayed
0 i
dynverse/dynmethods/issues?q=label:method_discussion. commitment between all milestones. The milestone percentage of a cell to
Method input. As input, we provided each method with either the raw count o p n er e c o en f t t a h g e e o t u o t e th r e m s i t l a e r s t t i o n n g e m s w ile a s s t e o q n u e a w l t a o s p eq se u u a d l t o o t i 1 m − e p × s P eu r M d i o . t Th im e e m . ilestone
data (after cell and gene filtering) or normalized expression values, based on • Type 5, cluster assignment: Mpath and SCUBA. The method returned a
the description in the method documentation or from the study describing the milestone network and an assignment of each cell to a specific milestone.
method. A large portion of the methods requires some form of prior information Cells were positioned onto the milestones they are assigned to, with milestone
(for example, a start cell) to be executable. Other methods optionally allow the percentage equal to 1.
exploitation of certain prior information. Prior information can be supplied as a • Type 6, orthogonal projection: MST, pCreode and RaceID/StemID. The
starting cell from which the trajectory will originate, a set of important marker method returned a milestone network, and a dimensionality reduction of the
genes or even a grouping of cells into cell states. Providing prior information to cells and milestones. The cells were projected to the closest nearest segment,
a TI method can be both a blessing and a curse. In one way, prior information thus determining the cells’ position along the milestone network. If a method
can help the method to find the correct trajectory among many, equally likely, also returned a cluster assignment (type 5), we limited the projection of
alternatives. On the other hand, incorrect or noisy prior information can bias the each cell to the closest edge connecting to the milestone of a cell. For these
trajectory towards current knowledge. Moreover, prior information is not always methods, we usually wrote two wrappers, one which included the projection
easily available, and its subjectivity can therefore lead to multiple equally plausible and one without.
solutions, restricting the applicability of such TI methods to well-studied systems. • Type 7, cell graph: CellRouter, CellTrails, cellTree Gibbs, cellTree maptpx,
The prior information was extracted from the reference trajectory as follows: cellTree VEM, Monocle DDRTree, Monocle ICA, Sincell* and SLICER. The
• Start cells: the identity of one or more start cells. For both real and synthetic method returned a network of cells and which cell–cell transitions were part
data, a cell was chosen that was the closest (in geodesic distance) to each of the ‘backbone’ structure. Backbone cells with degree ≠ 2 were regarded as
milestone with only outgoing edges. For ties, one random cell was chosen. For milestones and all other cells were placed on transitions between the mile-
cyclic datasets, a random cell was chosen. stones. If a method did not return a distance between pairs of cells, the cells
• End cells: the identity of one or more end cells. This is similar to the start cells, were uniformly positioned between the two milestones. Otherwise, we first
but now for every state with only incoming edges. calculated the distance between two milestones as the sum of the distances
• No. of end states: number of terminal states, i.e., the number of milestones between the cells and then divided the distance of each pair of cells with the
with only incoming edges. total distance to get the milestone percentages.
• Grouping: for each cell a label showing which state/cluster/branch it belongs Special conversions were necessary for certain methods:
to. For real data, the states were from the gold/silver standard. For synthetic
• CALISTA: We assigned the cells to the branch at which the sum of the cluster
data, each milestone was seen as one group and cells were assigned to their
probabilities of two connected milestones was the highest. The cluster prob-
closest milestone.
abilities of the two selected milestones were then used as milestone percent-
• No. of branches: number of branches/intermediate states. For real data, this
ages. This was then processed as a type 1, direct, method.
was the number of states in the gold/silver standard. For synthetic data, this
• DPT: We projected the cells onto the cluster network, consisting of a central
was the number of milestones.
milestone (this cluster contained the cells that were assigned to the ‘unknown’
• Discrete time course: for each cell a time point from which it was sampled. If
branch) and three terminal milestones, each corresponding to a tip point. This
available, this was directly extracted from the reference trajectory; otherwise
was then processed as a type 1, direct, method.
the geodesic distance from the root milestone was used. For synthetic data, the
• Sincell: To constrain the number of milestones this method creates, we
simulation time was uniformily discretized into four timepoints.
merged two cell clusters iteratively until the percentage of leaf nodes was
• Continuous time course: for each cell a time point from which it was sam-
below a certain cutoff, with the default cutoff set to 25%. This was then pro-
pled. For real data, this was equal to the discrete time course. For synthetic
cessed as a type 7, cell graph, method.
data, we used the internal simulation time of each simulator.
• SLICE: As discussed in the vignette of SLICE (https://research.cchmc.org/
pbge/slice.html), we ran principal curves one by one for every edge detected
Common trajectory model. Due to the absence of a common format for trajectory by SLICE. This was then processed as a type 1, direct, method.
models, most methods return a unique set of output formats with few overlaps. We • MFA: We used the branch assignment as state probabilities, which together
therefore post-processed the output of each method into a common probabilistic with the global pseudotime were processed as a type 4, end state probabili-
trajectory model (Supplementary Fig. 1a). This model consisted of three parts. ties, method.
(1) The milestone network represents the overall network topology, and contains • URD: We extracted the pseudotime of a cell within each branch using the
edges between different milestones and the length of the edge between them. y positions in the tree layout. This was then further processed as a type 1,
(2) The milestone percentages contain, for each cell, its position between direct, method.
NATuRe BioTeCHNologY | www.nature.com/naturebiotechnology
Articles NATure BiOTecHNOlOgy
More information on how each method was wrapped can be found within the spike-ins, and it includes a harsh cell filtering that looks at abnormalities in
comments of each wrapper script, listed at https://methods.dynverse.org. library sizes, mitochondrial gene expression and the number of genes expressed
using median absolute deviations (which we set to 3). We required that a gene was
Off-the-shelf methods. For baseline performance, we added several ‘off-the-shelf’ expressed in at least 5% of the cells and that it should have an average expression
TI methods that can be run using a few lines of code in R. higher than 0.02. Furthermore, we used the pipeline to select the most highly
• Component 1: This method returns the first component of a principal com- variable genes, using a false discovery rate of 5% and a biological component
ponent analysis (PCA) dimensionality reduction as a linear trajectory. This higher than 0.5. As a final filter, we removed both all-zero genes and cells
method is especially relevant as it has been used in a few studies already48,49. until convergence.
• Angle: Similar to the previous method, this method computes the angle with
respect to the origin in a two-dimensional PCA and uses this angle as a Benchmark metrics. The importance of using multiple metrics to compare
pseudotime for generating a cyclical trajectory. complex models has been stated repeatedly46. Furthermore, a trajectory is
• MST: This method performs PCA dimensionality reduction, followed by a model with multiple layers of complexity, which calls for several metrics
clustering using the R mclust package, after which the clusters are connected each assessing a different layer. We therefore defined several possible metrics
using a minimum spanning tree. The trees are orthogonally projected to the for comparing trajectories, each investigating different layers. These are all
nearest segment of the tree. This baseline is highly relevant as many methods discussed in Supplementary Note 1 along with examples and robustness analyses
follow the same methodology: dimensionality reduction, clustering, topology when appropriate.
inference and project cells to topology. Next, we created a set of rules to which we think a good trajectory metric
should conform, and tested this empirically for each metric by comparing scores
before and after perturbing a dataset (Supplementary Note 1). Based on this
Trajectory types. We classified all possible trajectory topologies into distinct
analysis, we chose four metrics for the evaluation, each assessing a different aspect
trajectory types, based on topological criteria (Fig. 1c). These trajectory types
of the trajectory: (1) the HIM measures the topological similarity; (2) the F1
start from the most general trajectory type, a disconnected graph, and move down branches
compares the branch assignment; (3) the cor assesses the similarity in pairwise
(within a directed acyclic graph structure), progressively becoming more simple dist
cell–cell distances and thus the cellular positions; and (4) the wcor looks at
until the two basic types are reached: linear and cyclical. A disconnected graph is a features
whether similar important features (genes) are found in both the reference dataset
graph in which only one edge can exist between two nodes. A (connected) graph is
and the prediction.
a disconnected graph in which all nodes are connected. An acyclic graph is a graph
containing no cycles. A tree is an acyclic graph containing no convergences (no
The Hamming–Ipsen–Mikhailov metric. The HIM metric52 uses the two
nodes with in-degree higher than 1). A convergence is an acyclic graph in which
weighted adjacency matrices of the milestone networks as input (weighted by
only one node has a degree larger than 1 and this same node has an in-degree
edge length). It is a linear combination of the normalized Hamming distance,
of 1. A multifurcation is a tree in which only one node has a degree larger than 1.
which gives an indication of the differences in edge lengths, and the normalized
A bifurcation is a multifurcation in which only one node has a degree equal to 3.
Ipsen–Mikhailov distance, which assesses the similarity in degree distributions.
A linear topology is a graph in which no node has a degree larger than 3. Finally,
a cycle is a connected graph in which every node has a degree equal to 2. In most
The latter has a parameter γ, which was fixed at 0.1 to make the scores
comparable between datasets. We illustrate the metric and discuss alternatives in
cases, a method that was able to detect a complex trajectory type was also able to
Supplementary Note 1.
detect less complex trajectory types, with some exceptions shown in Fig. 2a.
For simplicity, we merged the bifurcation and convergence trajectory type,
The F1 between branch assignments. To compare branch assignment, we used
and the acyclic graph and connected graph trajectory type in the main figures
an F1 score, also used used for comparing biclustering methods44. To calculate
of the paper.
this metric, we first calculated the similarity of all pairs of branches between
the two trajectories using the Jaccard similarity. Next, we defined the ‘Recovery'
Real datasets. We gathered real datasets by searching for ‘single-cell’ at the
(respectively ‘Relevance') as the average maximal similarity of all branches in the
Gene Expression Omnibus and selecting those datasets in which the cells are
reference dataset (respectively prediction). The F1 was then defined as the
sampled from different stages in a dynamic process (Supplementary Table 2). branches
harmonic mean between Recovery and Relevance. We illustrate this metric further
The scripts to download and process these datasets are available on our
in Supplementary Note 1.
repository (https://benchmark.dynverse.org/tree/master/scripts/01-datasets).
Whenever possible, we preferred to start from the raw counts data. These raw
Correlation between geodesic distances. When the position of a cell is the same
counts were all normalized and filtered using a common pipeline, as discussed
in both the reference and the prediction, its relative distances to all other cells
later. Some original datasets contained more than one trajectory, in which case
in the trajectory should also be the same. This observation is the basis for the
we split the dataset into its separate connected trajectory, but also generated
cor metric. To calculate the cor , we first sampled 100 waypoint cells in both
several combinations of connected trajectories to include some datasets with dist dist
the prediction and the reference dataset, using stratified sampling between the
disconnected trajectories in the evaluation. In the end, we included 110 datasets
different milestones, edges and regions of delayed commitment, weighted by the
for this evaluation.
number of cells in each collection. We then calculated the geodesic distances
For each dataset, we extracted a reference trajectory, consisting of two parts:
between the union of waypoint cells from both datasets and all other cells.
the cellular grouping (milestones) and the connections between these groups
The calculation of the geodesic distance depended on the location of the two
(milestone network). The cellular grouping was provided by the authors of
cells within the trajectory, further discussed in Supplementary Note 1, and was
the original study, and we classified it as a gold standard when it was created
weighted by the length of the edge in the milestone network. Finally, the cor was
independently from the expression matrix (such as from cell sorting, the origin dist
defined as the Spearman rank correlation between the distances of both datasets.
of the sample, the time it was sampled or cellular mixing) or as a silver standard
We illustrate the metric and assess the effect of the number of waypoint cells in
otherwise (usually by clustering the expression values). To connect these cell
Supplementary Note 1.
groups, we used the original study to determine the network that the authors
validated or otherwise found to be the most likely. In the end, each group of cells
The correlation between important features. The wcor assesses whether the
was placed on a milestone, having a percentage of 1 for that particular milestone. features
same differentially expressed features are found using the predicted trajectory as in
The known connections between these groups were used to construct the
the known trajectory. To calculate this metric, we used Random Forest regression
milestone network. If there was biological or experimental time data available, we
(implemented in the R ranger package53), to predict expression values of each gene,
used this as the length of the edge; otherwise we set all the lengths equal to one.
based on the geodesic distances of a cell to each milestone. We then extracted
feature importance values for each feature and calculated the similarity of the
Synthetic datasets. To generate synthetic datasets, we used four different synthetic
feature importances using a weighted Pearson correlation, weighted by the feature
data simulators:
importance in the reference dataset to give more weight to large differences. As
• dyngen: simulations of gene regulatory networks, available at https://github. hyperparameters we set the number of trees to 10,000 and the number of features
com/dynverse/dyngen on which to split to 1% of all available features. We illustrate this metric and assess
• dyntoy: random gradients of expression in the reduced space, available at the effect of its hyperparameters in Supplementary Note 1.
https://github.com/dynverse/dyntoy
• PROSSTT: expression is sampled from a linear model that depends on Score aggregation. To rank methods, we needed to aggregate the different scores on
pseudotime50
two levels: across datasets and across different metrics. This aggregation strategy is
• Splatter: simulations of non-linear paths between different expression states36 explained in more detail in Supplementary Note 1.
These simulators are discussed in Supplementary Note 2. To ensure that easy and difficult datasets have equal influence on the final
score, we first normalized the scores on each dataset across the different methods.
Dataset filtering and normalization. We used a standard single-cell RNA-seq We shifted and scaled the scores to σ = 1 and μ = 0, and then applied the unit
preprocessing pipeline that applies parts of the scran and scater Bioconductor probability density function of a normal distribution on these values to get the
packages51. The advantages of this pipeline are that it works both with and without scores back into the [0,1] range.
NATuRe BioTeCHNologY | www.nature.com/naturebiotechnology
NATure BiOTecHNOlOgy Articles
Since there is a bias in dataset source and trajectory type (for example, there original features. We ran every method on each of the bootstraps, and assessed the
are many more linear datasets), we aggregated the scores per method and dataset stability by calculating the benchmarking scores between each pair of subsequent
in multiple steps. We first aggregated the datasets with the same dataset source models (run i is compared to run i + 1). For the cor dist and F1 branches , we only used
and trajectory type using an arithmetic mean of their scores. Next, the scores the intersection between the cells of two datasets, while the intersection of the
were averaged over different dataset sources, using an arithmetic mean that was features was used for the wcor .
features
weighted based on how much the synthetic and silver scores correlated with the
real gold scores. Finally, the scores were aggregated over the different trajectory Usability. We created a transparent scoring scheme to quantify the usability of each
types again using an arithmetic mean. method based on several existing tool quality and programming guidelines in the
Finally, to get an overall benchmarking score, we aggregated the different literature and online (Supplementary Table 3). The main goal of this quality control
metrics using a geometric mean. is to stimulate the improvement of current methods, and the development of user-
and developer-friendly new methods. The quality control assessed six categories,
Method execution. Each execution of a method on a dataset was performed in a each looking at several aspects, which are further divided into individual items.
separate task as part of a gridengine job. Each task was allocated one CPU core of The availability category checks whether the method is easily available, whether
an Intel(R) Xeon(R) CPU E5-2665 at 2.40 GHz, and one R session was started for the code and dependencies can be easily installed, and how the method can be
each task. During the execution of a method on a dataset, if the time limit (>1 h) used. The code quality assesses the quality of the code both from a user perspective
or memory limit (16 GB) was exceeded, or an error was produced, a zero score was (function naming, dummy proofing and availability of plotting functions) and a
returned for that execution. developer perspective (consistent style and code duplication). The code assurance
category is frequently overlooked, and checks for code testing, continuous
Complementarity. To assess the complementarity between different methods, we integration54 and an active support system. The documentation category checks
first calculated for every method and dataset whether the overall score was equal the quality of the documentation, both externally (tutorials and function
to or higher than 95% of the best overall score for that particular dataset. We then documentation) and internally (inline documentation). The behavior category
calculated for every method the weighted percentage of datasets that fulfilled assesses the ease by which the method can be run, by looking for unexpected
this rule, weighted similarly as in the benchmark aggregation, and chose the output files and messages, prior information and how easy the trajectory model can
best method. We iteratively added new methods until all methods were selected. be extracted from the output. Finally, we also assessed certain aspects of the study
For this analysis, we did not include any methods that require any strong prior in which the method was proposed, such as publication in a peer-reviewed journal,
information and only included methods that could detect the trajectory types the number of datasets in which the usefulness of the method was shown and the
present in at least one of the datasets. scope of method evaluation in the paper.
Each quality aspect received a weight depending on how frequently it
Scalability. To assess the scalability of each method, we started from five was found in several papers and online sources that discuss tool quality
real datasets, selected using the centers from a k-medoids as discussed in (Supplementary Table 3). This was to make sure that more important aspects,
Supplementary Note 2. We up- and downscaled these datasets between 10 and such as the open source availability of the method, outweighed other less
100,000 cells and 10 and 100,000 features, while never going higher than 1,000,000 important aspects, such as the availability of a graphical user interface. For each
values in total. To generate new cells or features, we first generated a 10-nearest- aspect, we also assigned a weight to the individual questions being investigated
neighbor graph of both the cells and features from the expression space. For every (Supplementary Table 3). For calculating the final score, we weighed each of the
new cell or feature, we used a linear combination of one to three existing cells or six categories equally.
features, where each cell or feature was given a weight sampled from a uniform
distribution between 0 and 1. Guidelines. For each set of outcomes in the guidelines figure, we selected one to
We ran each method on each dataset for maximally 1 h and gave each process four methods, by first filtering the methods on those that can detect all required
10 GB of memory. To determine the running time of each method, we started the trajectory types, and ordering the methods according to their average accuracy
timer right after data loading and the loading of any packages, and stopped the score on datasets containing these trajectory types (aggregated according to the
clock before postprocessing and saving of the output. Pre- and postprocessing scheme presented in the section Accuracy).
steps specific to a method, such as dimensionality reduction and gene filtering, We used the same approach for selecting the best set of methods in the
were included in the time. To estimate the maximal memory usage, we used the guidelines app (guidelines.dynverse.org), developed using the R shiny package.
max_vmem value from the qacct command provided by a gridengine cluster. This app will also filter the methods, among other things, depending on the
We acknowledge, however, that these memory estimates are very noisy and the predicted running time and memory requirements, the prior information available
averages provided in this study are therefore only rough estimates. and the preferred execution environment (using the dynmethods package or
The relationship between the dimensions of a dataset and the running time or standalone).
maximal memory usage was modeled using shape constrained additive models39,
with log |cells| and log |features| as predictor variables, and fitted this model Reporting Summary. Further information on research design is available in the
10 10
using the scam function as implemented in the R scam package, with log (time) Nature Research Reporting Summary linked to this article.
10
(or log (memory)) as outcome.
10
To classify the time complexity of each method with respect to the number of Data availability
cells, we predicted the running time at 10,000 features with increasing number of
The processed real and synthetic datasets used in this study are deposited on
cells from 100 to 100,000, with steps of 100. We trained a generalized linear model
Zenodo (https://doi.org/10.5281/zenodo.1443566)55.
with the following function: y ≈ log(x) + sqrt(x) + x + x2 + x3 with y as running time The main analysis repository is available at https://benchmark.dynverse.org and
and x as the number of cells or features. The time complexity of a method was then
is divided into several experiments. Every experiment has its own set of scripts
classified using the weights w from this model:
and results, each accompanied by an illustrated readme that can be browsed and
 

superquadratic ifw x3>0.25, explored on the Github website.
   quadratic ifw x2>0.25 Code availability
  linear ifw x>0.25 The analysis scripts call several other R packages, of which an overview is available
 

sublinear ifw log(x)>0.25orw sqrt(x)>0.25 at dynverse.org. These packages include dynwrap, used to wrap the output
  casewithhighestweight else of methods into the common trajectory model, dyneval, which contains the
evaluation metrics, dynguidelines, the guidelines app, and dynplot for plotting
trajectories.
This process was repeated for the classification of the time complexity with
respect to the number of features, and the memory complexity both with respect to
References
the number of cells and features.
47. Gitter, A. Single-cell RNA-seq pseudotime estimation algorithms. https://
Stability. In the ideal case, a method should produce a similar trajectory, even github.com/agitter/single-cell-pseudotime (2018); https://doi.org/10.5281/
when the input data is slightly different. However, running the method multiple zenodo.1297423
times on the same input data would not be the ideal approach to assess its stability, 48. Kouno, T. et al. Temporal dynamics and transcriptional control using
given that a lot of tools are artificially deterministic by internally resetting the single-cell gene expression analysis. Genome. Biol. 14, R118 (2013).
pseudorandom number generator (for example, using the set.seed function in R 49. Zeng, C. et al. Pseudotemporal ordering of single cells reveals
or the random.seed function in numpy). To assess the stability of each method, metabolic control of postnatal β cell proliferation. Cell. Metab. 25,
we therefore selected a number of datasets, which consisted of 25% of the datasets 1160–1175.e11 (2017).
accounting for 15% of the total runtime, chosen such that after aggregation the 50. Papadopoulos, N., Parra, R. G. & Soeding, J. PROSSTT: probabilistic
overall scores still has >0.99 correlation with the original overall ranking. We simulation of single-cell RNA-seq data for complex differentiation processes.
subsampled each dataset 10 times with 95% of the original cells and 95% of the Bioinformatics, btz078 (2019).
NATuRe BioTeCHNologY | www.nature.com/naturebiotechnology
Articles NATure BiOTecHNOlOgy
51. Lun, A. T., McCarthy, D. J. & Marioni, J. C. A step-by-step workflow for 53. Wright, M. N. & Ziegler, A. Ranger: a fast implementation of random forests
low-level analysis of single-cell RNA-seq data with Bioconductor. F1000Res. 5, for high dimensional data in C++ and R. J. Stat. Softw. 77, 1-17 (2017).
2122 (2016). 54. Beaulieu-Jones, B. K. & Greene, C. S. Reproducibility of computational workflows
52. Jurman, G., Visintainer, R., Filosi, M., Riccadonna, S. & Furlanello, C. in is automated using continuous analysis. Nat. Biotechnol. 35, 3780 (2017).
Proc. 2015 IEEE International Conference on Data Science and Advanced 55. Cannoodt, R., Saelens, W., Todorov, H. & Saeys, Y. Single-cell -omics datasets
Analytics (DSAA) 1–10 (IEEE, 2015); https://doi.org/10.1109/ containing a trajectory (Version 2.0.0). Zenodo https://doi.org/10.5281/
DSAA.2015.7344816 zenodo.1443566 (2018).
NATuRe BioTeCHNologY | www.nature.com/naturebiotechnology
1
nature
research
|
reporting
summary
April
2018
Corresponding author(s): Yvan Saeys
Reporting Summary
Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency
in reporting. For further information on Nature Research policies, see Authors & Referees and the Editorial Policy Checklist.
Statistical parameters
When statistical analyses are reported, confirm that the following items are present in the relevant location (e.g. figure legend, table legend, main
text, or Methods section).
n/a Confirmed
The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement
An indication of whether measurements were taken from distinct samples or whether the same sample was measured repeatedly
The statistical test(s) used AND whether they are one- or two-sided
Only common tests should be described solely by name; describe more complex techniques in the Methods section.
A description of all covariates tested
A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons
A full description of the statistics including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND
variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)
For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted
Give P values as exact values whenever suitable.
For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings
For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes
Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated
Clearly defined error bars
State explicitly what error bars represent (e.g. SD, SE, CI)
Our web collection on statistics for biologists may be useful.
Software and code
Policy information about availability of computer code
Data collection The scripts to download and process the datasets are available at the dynbenchmark repository: https://www.github.com/dynverse/
dynbenchmark
Data analysis The data analysis was conducted using several custom software package, all available at https://www.github.com/dynverse/dynverse
For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors/reviewers
upon request. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Research guidelines for submitting code & software for further information.
Data
Policy information about availability of data
All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:
- Accession codes, unique identifiers, or web links for publicly available datasets
- A list of figures that have associated raw data
- A description of any restrictions on data availability
Data is deposited in Zenodo (https://zenodo.org/record/1443566) with doi 10.5281/zenodo.1443566
2
nature
research
|
reporting
summary
April
2018
Field-specific reporting
Please select the best fit for your research. If you are not sure, read the appropriate sections before making your selection.
Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences
For a reference copy of the document with all sections, see nature.com/authors/policies/ReportingSummary-flat.pdf
Life sciences study design
All studies must disclose on these points even when the disclosure is negative.
Sample size In our case the number of datasets used to compare methods corresponds to the sample size. We included as many real datasets as we could
find.
Data exclusions No data was excluded from the study
Replication To make sure that the experimental findings are reproducible, we (1) verified that the performance of the methods is similar between
different dataset sources, (2) verified that the metrics we use produce the expected results under a varied set of perturbational settings and
(3) assessed the stability of each method.
Randomization This is not relevant to our study because we do not include separate experimental groups
Blinding This is not relevant to our study because we do not include separate experimental groups
Reporting for specific materials, systems and methods
Materials & experimental systems Methods
n/a Involved in the study n/a Involved in the study
Unique biological materials ChIP-seq
Antibodies Flow cytometry
Eukaryotic cell lines MRI-based neuroimaging
Palaeontology
Animals and other organisms
Human research participants
nature
research
|
software
submission
checklist
June
2017
Corresponding author(s): Yvan Saeys
Code and Software Submission Checklist
Prior to submitting your work to Nature Research, we strongly recommend that you ask at least one colleague who is unfamiliar with your software to
install the tool(s), follow the instructions, and provide feedback. This process will help ensure that reviewers will also be able to run your software.
You must submit all required content as a single zip file prior to peer review or provide a link where editors and reviewers can access all required content.
(cid:96) Required content
✔ Compiled standalone software and/or source code
✔ A small (simulated or real) dataset to demo the software/code
A README file that includes:
1. System requirements
✔ All software dependencies and operating systems (including version numbers)
✔ Versions the software has been tested on
✔ Any required non-standard hardware
2. Installation guide
✔ Instructions
✔ Typical install time on a "normal" desktop computer
3. Demo
✔ Instructions to run on data
✔ Expected output
✔ Expected run time for demo on a "normal" desktop computer
4. Instructions for use
✔ How to run the software on your data
✔ (OPTIONAL) Reproduction instructions
We encourage you to include instructions for reproducing all the quantitative results in the manuscript.
(cid:96) Additional information
Describe your software's license for use. We strongly recommend using a license approved by the Open Source Initiative.
GPL-3
Provide a link to the code in an open source repository (when available).
https://github.com/dynverse/dynbenchmark and https://github.com/dynverse/dynguidelines
Your manuscript should include a complete, detailed description of the code's functionality (i.e. pseudocode).
Please indicate where this is found:
Main text
Methods section
Elsewhere (specify):
The descriptions of the code can be found in the READMEs in the github repository
(cid:96) Examples of well-structured software packages
1. https://github.com/neurodata-papers/MGC
2. https://github.com/neurodata-papers/LOL
3. https://www.nature.com/nbt/journal/v34/n6/abs/nbt.3569.html#supplementary-information
4. https://www.nature.com/nature/journal/v548/n7669/full/nature23463.html#extended-data
https://github.com/yasharhezaveh/Ensai
5. https://www.nature.com/nbt/journal/v34/n11/full/nbt.3685.html#supplementary-information
https://github.com/IFIproteomics/LFQbench
1
