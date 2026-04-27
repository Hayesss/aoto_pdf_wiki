---
source_path: /mnt/c/Users/Administrator/Zotero/storage/EZBCMGWW/Jorge 等 - 2025 - A comprehensive review and benchmark of differential analysis tools for Hi-C data.pdf
ingested: 2026-04-23
sha256: ddbb2b8f61dce1ab
---

BriefingsinBioinformatics,2025,26(2),bbaf074
https://doi.org/10.1093/bib/bbaf074
Review
A comprehensive review and benchmark of differential
analysis tools for Hi-C data
Elise Jorge1, Sylvain Foissac1, Pierre Neuvial2, Matthias Zytnicki3, Nathalie Vialaneix 3, *
1GenPhySE, Université de Toulouse, INRAE, ENVT, 31326 Castanet-Tolosan, France
2Institut de Mathématiques de Toulouse, UMR 5219, Université de Toulouse, CNRS UPS, 31062 Toulouse, France
3Université Fédérale de Toulouse, INRAE, MIAT, 31326 Castanet-Tolosan, France
*Corresponding author. Université Fédérale de Toulouse, INRAE, MIAT, 31326 Castanet-Tolosan, France. E-mail: nathalie.vialaneix@inrae.fr
Abstract
Motivation: The 3D organization of the genome plays a crucial role in various biological processes. Hi-C technology is widely used to
investigate chromosome structures by quantifying 3D proximity between genomic regions. While numerous computational tools exist
for detecting differences in Hi-C data between conditions, a comprehensive review and benchmark comparing their effectiveness is
lacking. Results: This study offers a comprehensive review and benchmark of 10 generic tools for differential analysis of Hi-C matrices
at the interaction count level. The benchmark assesses the statistical methods, usability, and performance (in terms of precision
and power) of these tools, using both real and simulated Hi-C data. Results reveal a striking variability in performance among the
tools, highlighting the substantial impact of preprocessing filters and the difficulty all tools encounter in effectively controlling the
false discovery rate across varying resolutions and chromosome sizes. Availability: The complete benchmark is available at https://
forgemia.inra.fr/scales/replication-chrocodiff using processed data deposited at https://doi.org/10.57745/LR0W9R. Contact: nathalie.
vialaneix@inrae.fr
Keywords: Hi-C; differential analysis; statistical tests; benchmark
Introduction
basic methods,which directly compute a similarity score (e.g.a cor-
Chromosomes are highly compacted within the cell nucleus, relation) between two matrices [11], map-informed methods, which
resulting in the spatial proximity of linearly distant genomic first calculate a Hi-C-related metric along a 1D track for each
positions [1]. Hi-C [2] is a widely used technology to profile the matrix separately (e.g.directionality index) and then compare the
3D organization of the genome. It does so by estimating the resulting tracks [12], and feature-informed methods, which predict
spatial proximity between pairs of genomic positions through specific chromatin structures for each matrix (e.g. TAD bound-
their frequency of interaction. The typical output of a Hi-C aries or chromatin loops) before comparing the predictions [13].
experiment, after preliminary data preprocessing, is usually While these methods offer various similarity or dissimilarity met-
summarized as a symmetric matrix of counts, where the entry rics, none provide statistical guarantees such as p-values. More-
(i,j) (or (j,i)) corresponds to the number of interactions registered over, they focus solely on pairwise matrix comparisons without
during the Hi-C experiment between genomic regions (“bins”) i incorporating biological replicates.
and j. Hi-C has been widely used to uncover structural genomic Another approach to comparing Hi-C data is differential anal-
elements at different hierarchical levels, such as A/B chromatin ysis. Instead of quantifying the overall similarity between two
compartments, TADs, and loops [1–3]. Many computational tools Hi-C matrices (one for each condition), differential analysis aims
exist to call these structures from Hi-C data, with variable at identifying local differences with statistical guarantees, often
reliability however [4–6]. leveraging biological replicates for each condition. Following the
Changes in 3D structures have been implicated in gene expres- previous classification,some of the methods can be considered as
sion, cell division, cell differentiation, developmental disorders, map-informed, as they use 1D metrics to detect differential struc-
and cancers [7–9].This underscores the need for reliable methods turessuchasTADboundaries[14,15]orchromatincompartments
and tools to compare Hi-C data across different conditions. One [16] at the bin level. Other methods fall under the feature-informed
approach to comparing Hi-C data is to compute a similarity score category, aiming to identify differential TADs, for instance [17].
for a pair of matrices, either at the level of the entire matrix However, most tools for differential analysis of Hi-C data do not
(matrix-level) or for specific genomic regions (bin-level).Gunsalus fit into these categories, as they test for differences at the level
et al., 2023 [10] reviewed several methods for the pairwise com- of the bin pair, focusing on interaction counts between genomic
parison of Hi-C matrices, classifying them into three categories: regions [18–25]. To our knowledge, these methods have not been
Received:September26,2024.Revised:January24,2025.Accepted:February10,2025
©TheAuthor(s)2025.PublishedbyOxfordUniversityPress.
ThisisanOpenAccessarticledistributedunderthetermsoftheCreativeCommonsAttributionLicense(https://creativecommons.org/licenses/by/4.0/),which
permitsunrestrictedreuse,distribution,andreproductioninanymedium,providedtheoriginalworkisproperlycited.
2 | Jorgeetal.
extensively reviewed or benchmarked. A recent book chapter [26] • model and p-value computation, which is the core of the statis-
describes a few (four) such methods. While it provides technical tical analysis and performs a test on all remaining bin pairs,
instructions on their use and visualization of results, it does not using normalized interaction values;
evaluate the quality of the results. • multipletestingcorrection,whichaimsataccountingforthefact
To address this gap, we propose a comprehensive review of the that a large number of tests have been performed.
following tools for the differential analysis of Hi-C data: ACCOST
Most tools operate at the chromosome level, detecting intra-
[18], CHESS [27], diffHic [19], FIND [20], HiCcompare [21], HiCDC-
chromosomal (cis) differential interactions only. However, diffHic,
Plus [22], multiHiCcompare [23], Selfish [24], and sslHiC [25]. We
HOMER , ands slHiC can also detect inter-chromosomal (trans)
also considered a former version of HOMER (The version available
interactions.
and documented at http://homer.ucsd.edu/homer/interactions/.),
The steps of the Hi-C differential analysis workflow and the
whichincludedatesttoperformcomparisonsbetweentwomatri-
various options used by different tools are described in detail in
ces, although 3D structure changes are not the primary focus of
the sections below. Table 1 summarizes the main methodological
that tool. Our review provides a detailed technical description
characteristics of the tested tools in relation to the steps of this
of each tool, focusing on implementation aspects, usability, and
workflow.
scalability. We explain the differences between the statistical
methods employed by these tools and analyze their expected
impacts on the results. Filtering
We also conducted two extensive benchmarks of the tools Several tools propose to remove some bin pairs before the analy-
using real Hi-C data from the literature. The first benchmark sis. The rationale behind this step is that low quality bin pairs or
used Hi-C data generated from a human tissue sample, with bin pairs with low interaction counts have little (if any) chance to
an artificially introduced ground truth to allow a quantitative beidentifiedas differentialbutincreasethenumberof hypothesis
evaluation of each tool’s precision and power. The second bench- tests that are performed. Including such bin pairs can affect
mark involved Hi-C data from a CTCF depletion study during the test power, due to stronger multiple testing correction (see
mouse cell cycle progression, evaluating the biological relevance corresponding section below for further details). Discarding bin
of each tool’s results by comparing them to findings from ChIP- pairs before the test (and independently from its result) is a
seq experiments. standard way to reduce this impact [28, 29].
The article is organized as follows: The second section “Meth- ThemostcommonfiltersusedinHi-Cdifferentialanalysesare:
ods” reviews the statistical grounds of the different tools in a
rigorous way. The third section “Implementation and usability” • low count filtering (implemented in diffHic, HiCcompare,
describes the technical aspects of the tools. The fourth section HiCDCPlus, multiHiCcompare, andS elfish). These filters
“Numerical experiments”introduces our benchmark protocol and simply remove, from the analysis, bin pairs that have
the fifth section “Results” analyses the tools’ performances. interaction counts below a certain threshold. This threshold
is either user-defined (i.e. all bin pairs for which the average
or total interaction counts across analyzed matrices is below
Methods the threshold as in diffHic, HiCcompare, multiHiCcompare,
Methodological overview of the tools and Selfish) or data-driven (the threshold is obtained as
an estimation of a “background signal” from the data as in
This article covers tools that all aim at answering the same
diffHic and HiCDCPlus);
question: given a set of n Hi-C matrices, M 1, ..., M n, belonging
• bin quality filtering (implemented in CHESS, ACCOST, and
to K different groups of biological interest (that we will call “con-
HiCDCPlus). These filters remove bin pairs including at least
ditions”), are we able to find bin pairs with significantly different
one bin with low mappability or, alternatively, bin pairs for
interaction counts between conditions? While several descriptive
which the interaction counts are below the expected (data-
metrics (such as correlation or other similarity measures) can
driven) value considering the bin mappability and GC con-
be used for this purpose, we focus on approaches that provide
tent. These filters require that mappability or GC content is
statistical guarantees for identified bin pairs. Such approaches
provided for each bin.
perform one statistical test for each bin pair. The result of each
of these tests can be summarized by a p-value (or an adjusted p- Additionally, Selfish allows to discard all bin pairs for which
value), which quantifies the statistical evidence of a significant thegenomicdistancebetweenthetwobinsislargerthanacertain
difference. (user-defined) value, typically targeting bins with low interaction
The tools discussed in this article all have a common workflow counts.Also,HiCcomparehasanoptiontoletusersspecifyasetof
(Fig. 1). In short, this workflow takes Hi-C matrices from different bins that should not be considered in the analysis.Supplementary
conditions and performs a statistical test, which results in a p- Table S1 summarizes the type of filters available in each
value (or an adjusted p-value) for each bin pair. CHESS is the only tool.
tool that slightly differs from this description because it provides
p-values for fixed-sized windows of the Hi-C matrix (and not for
Normalization
every bin pair; see Section “Methodological background of the
Hi-C matrix normalization is an important step of the workflow.
tools”).
It aims at removing technical or biological biases that can impede
As shown in Fig. 1, the Hi-C differential analysis workflow can
a fair comparison between bins or between matrices [30]. The
be decomposed into four main steps:
mainknownbiasesthatcanaffectHi-Cdataanalysisarescaledif-
• filtering, which consists in removing bin pairs considered not ferences between matrices (e.g. due to differences in sequencing
relevant from the analysis in all Hi-C matrices; depths), scale differences between bins in a given matrix (e.g. due
• normalization, which consists in making bin pairs in a matrix to differences in mappability), or effects of the genomic distance
or bin pairs between different matrices more comparable; in interaction counts within a given matrix.In the current section,
DifferentialanalysisofHi-Cdata | 3
Figure 1. A schematic representation of the typical workflow for differential analysis of Hi-C matrices at the bin-pair (pixel) level. Input matricesfrom
two conditions,with or without replicates,are first filtered and normalized (first two steps).Statistical tests are then conducted to generate raw p-values,
which are subsequently adjusted for multiple testing correction (last two steps). Additionally, a (log) fold change matrix can be generated, representing
the ratio of average interaction values between conditions for each bin pair (not shown).
we discuss these biases,their impact on the analysis,and how the compare bin pairs between matrices and not bin pairs within the
different tools address them. same matrices, correcting for these biases is not strictly neces-
sary from a statistical perspective. However, several tools never-
Differences in total interaction counts between matrices. Total
theless recommend or implement methods for correcting these
interaction counts across all bin pairs can differbetween matrices
biases.
due to experimental factors, such as variations in sequencing
Among the most popular methods for within-matrix normal-
depth or library complexity. To prevent false positive predictions
ization, non-parametric methods do not explicitly use GC con-
that would incorrectly label bin pairs as “differential”, these tech-
tent or mappability values to remove biases between bin counts.
nical artifacts must be accounted for, as commonly done in RNA-
On the contrary, similarly to TSS normalization, they align the
seq [31] or ChIP-seq data [32, 33] differential analyses.
observed total count across all bins of a given matrix. These
The most straightforward method to correct this bias is the
include iterative correction and eigenvector decomposition (ICE)
total sum scaling (TSS) that simply aligns the total counts of all
[35], implemented in HOMER, or Knight–Ruiz (KR) matrix balanc-
matrices in the dataset (implemented in sslHiC and advised, but
ing [36], implemented in diffHic. Other tools (FIND and Selfish)
not implemented, in HiCcompare). However, this approach has
benefit from the juicer data format [37] and embed values that
been shown to be generally inefficient for sequencing data, as it
allow for KR correction. Finally, CHESS and HiCDCPlus recom-
is strongly influenced by large outlier counts [31].
mend the ICE correction but do not implement it.
Hence, the article of Lun & Smyth, 2016 [33] emphasizes the
An alternative to choosing a specific method to correct
need for an adequate between-matrix normalization and pro-
between-bin biases is to let users provide bin-specific correction
poses the MA correction (correction of the trend in an MA plot,
values. This is the course of action taken by ACCOST (that
where the difference “M” between two or more matrices is dis-
recommends using ICE but allows for any other type of bin
played as a function of their average count “A”). This correc-
correction values to be used).
tion, performed by cyclic locally estimated scatterplot smoothing
Finally, note that if all bin sums in a given matrix are aligned
(LOESS), has been shown to be efficient for ChIP-seq data and
to the same total count B (e.g. B = 1 for KR correction), then it is
robust to a large proportion of low counts. It is implemented in
sufficient to use the same B for all matrices to align, at the same
diffHic (and advised in FIND but not implemented).
time, overall total interaction counts between matrices.
A more sophisticated alternative is used in HiCcompare and
multiHiCcompare. The MA correction is replaced by an MD cor- Genomic distance related differences between interaction
rection (where D stands for the genomic distance between bin counts within a given matrix. Hi-C matrices are strongly
pairs, instead of its average count). However, since A and D are structured with respect to the genomic distance between bin
strongly related in Hi-C matrices (the larger the distance between pairs. Likewise biases between bin total counts within a given
the two bins of a pair, the lower the count for this bin pair), both matrix, this bias does not necessarily require correction but is
methods are expected to result in similar corrections. nevertheless accounted for in several tools.
Finally, although this does not strictly aim at correcting differ- One of the most popular approach to correct for this bias is
ences in sequencing depths, sslHiC also implements a min/max to compute an “observed over expected” matrix. The interaction
normalization applied to log 10 -transformed matrices so as to count of a bin pair is divided by the average interaction counts
make all counts in a given matrix lie between 0 and 1 (and thus of all bin pairs with the same genomic distance. This approach
be more comparable across matrices). is implemented in CHESS.Similarly,the interaction count of a bin
Differences in total counts between bins within a given matrix. pair at the same genomic distance can be centered and reduced to
The total number of interactions assigned to a specific bin or unitvariance(asimplementedinSelfish)orscalingfactorsforbin
over a given genomic region depends on local properties of the pairsatthesamegenomicdistance(e.g.median)canbecomputed
genomic sequence,such as GC content,mappability,or restriction and used for normalization (as implemented in ACCOST and
site density [34]. Since the purpose of differential analysis is to HiCDCPlus).
4 | Jorgeetal.
)txet
eht
ees
sliated
rehtruf
rof
;dezirammus(
sloot
eht
fo
noitpircsed
lacigolodohteM
.1 elbaT
seulav-p
ledoM
gnissecorperP
noitcerroc
eulav-p
war
sedivorP
fo
epyT
ro
setairavoc
swollA
erawa-D2
segareveL
noitubirtsid
ataD
noitazilamroN
gniretliF
looT
seulav-p
tset/ledom
snoitidnoc
2
>
K
hcaorppa
setacilper
noitpmussa
)HB(
(cid:2)
tset
tcaxe
×
×
(cid:2)
BN
)ECI(
ytilauq
niB
TSOCCA
×
(cid:2)
MISS
×
(cid:2)
×
enoN
)ECI(
ytilauq
niB
SSEHC
HB
(cid:2)
MLG
(cid:2)
×
(cid:2)
BN
RK
,AM
stnuoc
woL
ciHffid
ecnatsid
yb
HB
×
tset
tcaxe
×
(cid:2)
(cid:2)
PPS
RK
,)AM(
×
DNIF
ecnatsid
yb
HB
(cid:2)
erocs-Z
×
×
×
enoN
DM
,SST
denifed-resU
erapmocCiH
HB
(cid:2)
tset
tcaxe
×
×
(cid:2)
BN
)ECI(
ytilauq
nib
,stnuoc
woL
sulPCDCiH
HB
(cid:2)
MLG
×
×
(cid:2)
BN
ECI
×
REMOH
ecnatsid
yb
HB
(cid:2)
MLG
(cid:2)
×
(cid:2)
BN
DM
stnuoc
woL
erapmocCiHitlum
HB
×
erocs-Z
×
(cid:2)
×
enoN
RK
ecnatsid
,stnuoc
woL
hsifleS
HB
×
NNG
×
(cid:2)
×
enoN
xam/nim
,SST
×
CiHlss
laruen
hparg
:NNG
;ledom
raenil
dezilareneg
:MLG
;xedni
ytiralimis
derutcurts
:MISS
;ssecorp
nossioP
laitaps
:PPS
;laimonib
evitagen
:BN
;ziuR–thginK
:RK ;noitisopmoced
rotcevnegie
dna
noitcerroc
evitareti
:ECI
loot
rieht
ni
detnemelpmi
ton
tub
srohtua
dohtem
eht
yb
desivda
spets
ot
dnopserroc
sesehtnerap
neewteb
smetI
.grebhcoH–inimajneB
:HB
;krowten
Other normalizations.
Other methods designed to correct various other biases are also
implemented: diffHic proposes a method based on DNA copy
number variation (CNV) estimation to correct for this bias. How-
ever, as discussed by Servant et al., 2018 [38], CNV could be of
interest in cancer studies and it is therefore not necessarily sound
to always use this correction.
Finally, note that all tools that use the genomic distance
between bins for the normalization are restricted to detect
intra-chromosomal (cis) differential interactions only and cannot
consider inter-chromosomal (trans) interactions.
Supplementary Table S2 summarizes the different normaliza-
tion options offered by the tools.
Methodological background of the tools
This section describes the methodological premises and solutions
of the different tools. The tools can be classified according to the
following two questions:
• Can the tool use biological replicates to perform the test (i.e.
handle more than one matrix in each condition)? When
biological replicates are available, it is still possible to use a
tool designed to only compare one matrix in each condition
by merging (computing the sum of) the replicates of each
condition. However, it is strongly advised, from a statistical
perspective, that these replicates are used in order to relate
the inter-condition variability to the intra-condition variabil-
ity.
• Does the tool consider interaction counts as independent
from each other, or does it try to take advantage of the fact
that two bin pairs, (i,j) and (i(cid:2),j(cid:2)) in the matrix, tend to have
more similar interaction counts when they are close to each
other (e.g. |i−i(cid:2)|+|j−j(cid:2)| is “small”)? We will use the term “2D-
agnostic” for the tools that consider bin pairs independent
and the term “2D-aware” for the tools that account for this
property.
These two typology levels for the tools are provided in the two
columns of Table 1 named “use of replicates” and “2D-aware”. We
nowgiveabriefoverviewofeachtoolbasedontheanswertothese
two questions.
Comparison of two matrices
The tools designed to perform differential analysis between two
matrices are: HiCcompare (2D-agnostic), CHESS, Selfish,ands sl-
HiC (2D-aware).
2D-agnostic method. A 2D-agnostic method means that a mea-
sure of the difference between the two matrices is obtained at
bin pair level and transformed into a Z score, from which a p-
value is derived using the Gaussian distribution. More precisely,
HiCcompare uses the M-value (log-fold change between the two
matrices) of the interaction count to obtain a Z score.
2D-aware methods. Existing 2D-aware methods that perform
tests between two matrices are based on different premises:
CHESS first partitions the Hi-C matrix into fixed-size square
submatrices and computes a structural similarity index (SSIM).
This index is commonly used in imaging analysis to quantify the
similarity between two matrices. It depends on the average signal
in each submatrix,the variance of the signal in a given submatrix,
andthe signalcorrelation between thetwo submatrices.A p-value
is then derived for each square from this index, quantifying the exceptionality of the observed index with respect to a background
model.
DifferentialanalysisofHi-Cdata | 5
Selfish performs a sort of “local smoothing” of the matrices: p-value for the test of the null hypothesis λ 1 =λ 2 is then obtained
For each bin pair, it applies Gaussian filters centered at the bin for each bin pair. The final p-value at each bin pair is obtained
pair, with increasing radius. The idea is to take advantage of by aggregating the first-level p-values in the local neighborhood
the spatial self-similarity in contact maps to improve statistical around the bin pair, using the r-ordered p-value (rOP) method
evidence. Differences of the Gaussian filter evolutions between [43]. However, the resulting p-value may not be valid since the
the two matrices are then assumed to be Gaussian, from which a rOP method assumes independence between the hypotheses to
p-value is derived for each radius. The final p-value is defined as be aggregated.
the minimum radius-specific p-value across radii. However, since
Multiple testing correction
nomultipletestingcorrection is appliedat thisstage,theresulting
p-values are invalid. All the evaluated tools perform one statistical test for each bin
Finally, sslHiC is based on a graph neural network (GNN) [39, pair (i,j),withF IND and Self ish deriving this p-value by aggre-
40]. The idea is to represent a Hi-C matrix as a graph in which gating results from other previous tests. Therefore, a multiple
binsarenodesandpositiveinteractioncountsareedges(weighted testing correction is necessary to control false positives–bin pairs
by the interaction count). Bin pairs of the form (i,i + 1) (linking identified as differential by chance rather than due to a true dif-
two bins that are neighbors on the chromatin) are also linked ference in interaction levels between the two conditions. Multiple
with an edge to encode the genome structure in the Hi-C graph. tests in genomic studies are generally handled by controlling the
The authors propose a new architecture of GNN, which they call false discovery rate (FDR). The FDR corresponds to the expected
“edge-enhanced GNN” (EEGNN) that aims at better exploiting the proportion of false positives among the bin pairs called significant
information carried by edges in the message passing process of by a given method. The state-of-the art method for FDR control is
the GNN. Using this architecture, all the bin pairs (i,j) in the the Benjamini–Hochberg (BH) method [44].
matrix are represented by their embeddings hk , d-dimensional However, multiple testing correction is handled in different
(i,j)
vectors organized in different layers, k. The method is fully aware ways across tools. diffHic, HiCDCPlus, HOMER, and sslHiC imple-
of the whole matrix since the embedding hk at layer k is passed ment FDR control using the BH method. While ACCOST does
(i,j)
to the other bin pairs that share a common node to compute not directly provide multiple testing correction, its authors also
their embeddings at layer k+ 1. The method finally derives a p- used the BH method in [18]. A different strategy is implemented
value for (i,j) by assuming Gaussian distribution of the Euclidean in HiCcompare, multiHiCcompare, andF IND. These methods
distance between embeddings hK of the two matrices in the last perform multiple testing correction on a per-distance basis, also
(i,j)
layer K. using the BH method. This implies that the FDR of their results
is (theoretically) not globally controlled at the chromosome level,
Comparison of multiple matrices for each condition. which means that more false positives can be expected for these
Tools that leverage replicates to perform differential analysis
tools. Notably, as the typical use case of the tools considers indi-
are ACCOST, diffHic, HiCDCPlus, HOMER, multiHiCcompare (2D-
vidual chromosomes, looking for differences in cis-interactions,
agnostic),and FIND (2D-aware).As explained above,an important
multiple testing correction is not performed by these methods at
advantage of these tools from a statistical perspective is that
the genome-level.
they can account for the variability across replicates within each
Handling more complex experimental designs
condition (e.g. by computing variances, which cannot be done
when a single replicate is available). Finally, diffHic and multiHiCcompare are designed to perform a
test between more than K = 2 conditions or are able to include
2D-agnostic methods. 2D-agnostic tools that account for repli-
external covariates in the model. The latter is useful when an
cates (ACCOST, diffHic, HiCDCPlus, HOMER,andm ultiHiCcom-
experimental factor is not of primary interest for the differential
pare) all assume that the interaction counts follow a negative
analysis but might influence the results (e.g. a noise effect, like
binomial (NB) distribution. This is a standard hypothesis already
the sex or the tissue, could mask the differences due to the factor
used in other differential analysis methods for sequencing data,
of interest, like the treatment). In this case, it is common practice
notably for RNA-seq. More precisely, diffHic and multiHiCcom-
to account for this covariate as a “blocking factor,” correcting the
pareintegrateedgeR[41]functionsthatfitaNBgeneralizedlinear
effect without testing for it. However, due to the high cost of Hi-C
model (GLM) (and thus directly benefit from the flexibility of this
data generation, such complex designs (involving more than two
framework, able to account for complex experimental designs).
conditions and/or covariates) remain rare.As a result,while these
The main difference with the standard RNA-seq pipelines is the
features may be valuable for future experimental designs, they
addition of an offset derived from the MA (diffHic)orMD(multi-
are not the primary focus at present.
HiCcompare) normalization in the NB GLM. Similarly, HiCDCPlus
and HOMER use DESeq2 [42] and differ from DESeq2 by the
preprocessing performed on Hi-C matrices,especially the filtering Implementation and usability of the tools
step described in the “Filtering”section.Alternatively,HOMER can
Table 2summarizestechnicalinformationforeachtool,including
also use an edgeR model. Even if it does not directly depend
theprogramminglanguage,whetherthetoolispackagedandeasy
on DESeq2, ACCOST also derives its method from DESeq2’s NB
to install, which input formats are handled, whether a documen-
model, plugging the bin-specific correction values described in
tation is provided, and when it has been last updated.
“Normalization” into the NB GLM method of DESeq2.
Inputs and input formats
2D-aware method. The only 2D-aware tool able to account for
replicates is FIND. InF IND, a bin pair is described by its posi- Almost all the tested tools assume that the raw sequencing
tion (i,j) in the matrix 2D structure and its interaction counts reads have preliminary been processed with a Hi-C data analysis
across matrices. The resulting triplet is distributed as a spatial pipeline and consequently converted into interaction matrices.
Poisson process (a count process that has a spatial structure) Notable exceptions are diffHic, which can also handle BAM or
with condition-specific intensity parameter λ 1 and λ 2.A first-level FASTQ files, and HOMER, which requires BAM or FASTQ files.
6 | Jorgeetal.
sloot
detset
eht
fo
noitpircsed
lacinhceT
.2 elbaT
yrotisoper
edoC
noitacifidom
tsaL
noitatnemucoD
tamrof
tupnI
noitallatsnI
egaugnaL
looT
1TSOCCA
70-2202
launam
LMTH
lacol
cisaB
vst
nwo
stpircs
nohtyP
R
& 2nohtyP
]81[
TSOCCA
buhtiG
70-3202
noitatnemucod
”scodehtdaer“
etelpmoC
cnaf./looc./cih.
pip
3nohtyP
]72[
SSEHC
buhtiG
30-4202
ettengiv
rotcudnocoiB
+launaM
tcejbo
R snoitcaretnIG
rotcudnocoiB
R
)0.62.1v(
]91[
ciHffid
tekcubtiB
11-2202
ettengiv
lacol
+launam
enilno
cisaB
ORP-CiH
egakcap
R
ecruos
R
)0.0.1v(
]02[ DNIF
buhtiG
60-3202
ettengiv
rotcudnocoiB
+launaM
vst
nwo/ORP-CiH
rotcudnocoiB
R
]12[
erapmocCiH
)0.61.1v(
buhtiG
60-2202
ettengiv
rotcudnocoiB
+launaM
tcejbo
R snoitcaretnIG
rotcudnocoiB
R
]22[
sulPCDCiH
)1.2.1v(
enon
)denoitnem
ton(
etisbew
etelpmoC
sdaer
QTSAF
tpircs
++C
&
lreP
++C
&
lreP
]15[
REMOH
buhtiG
40-2202
ettengiv
rotcudnocoiB
+launaM
vst
nwo/ORP-CiH
rotcudnocoiB
R
]32[
erapmocCiHitlum
)0.21.1v(
buhtiG
50-1202
launam
cisaB
nwo/ORP-CiH/looc./cih.
reniatnoc/pip
3nohtyP
]42[
hsifleS
vst
buhtiG
40-3202
launam
enilno
cisaB
zpn./ypn./xtm./looc.
vne
adnoc
+stpircs
nohtyP
3nohtyP
]52[
CiHlss
eno
,edoc
TSOCCA
rof
seirotisoper
eerht
dnuof
eW
)1(
.nmuloc
tsrif
eht
ni
detacidni
si )loot
eht
yb
dedivorp
nehw(
kramhcneb
eht
ni
desu
loot
eht
fo
noisreV
.3202
rebmevoN
ni
detcelloc
erew
noitacifidom
tsal
fo setaD
redisnoc
ot
yrotisoper
eht
su
detacidni
ohw
srohtua
eht
detcatnoc
eW
.)sraey
8
rof
detadpu
neeb
ton
sah
meht
fo
eno(
buhtiG
no
owt
dna
tekcubtiB
no
During the construction of the interaction matrix, paired-end
reads are usually mapped to a genomic reference sequence.Chro-
mosomes are then discretized into fixed-size bins,and interaction
matrices are obtained by counting for each bin pair the number of
read pairs that link the corresponding bins. In short, interaction
matrices are essentially symmetric square matrices with non-
negative entries and many zeros.
Severalfileformatshavebeenproposedtostorethesematrices,
with different degrees of adoption. Although none of them has
becometheuniversalstandardyet,afewareusedbyseveraltools.
Such common formats include binary (and possibly compressed)
formats, like the .hic [37], .cool, .mcool [45] and. fanc [ 46]
formats, and text-based formats like the HiC-PRO [47] or BEDPE
[48] formats. A majority of the tested tools (namely CHESS, FIND,
HiCcompare, multiHiCcompare, Selfish, ands slHiC) use these
standard formats (Table 2). Note that sslHiC can take as input a
.cool file or a contact matrix file similar to the one generated
by HiC-PRO. In the latter case, unlike the other tools, it does not
require an index file but only the matrix resolution (only certain
resolutionsareallowed;seeMethods).Thematrixfileisthengiven
as an .mtx file in the Matrix Market format, or can directly be
passed as a binary Python/numpy file (.npy or .npz).
The other tools use more specific formats. For instance,
ACCOST requires a tab-delimited format file, with columns
<chr1> <mid1> <chr2> <mid2> <#reads>, wherem id i is the position of the middle of bin i (i =1,2), and #reads is the raw
interactioncount.HiCDCPlusanddiffHic usetheGInteractions
Bioconductor class [49] as input format. HOMER is the only tool
in the list that exclusively accepts raw reads as input, rather than
interaction matrices. As a result, users must map the data with
HOMER, making it incompatible with pre-existing matrices for
differential analysis.
Furthermore, some tools require additional data with the
interaction counts.ACCOST requires a bin-specific normalization
score for each bin, which can be obtained with the ICE method
[35], as implemented, e.g. in Bioconductor/HiC-PRO package [47]
or in Cooler [45]. Note that ACCOST can accommodate any
possible bin-specific bias as input, allowing to use parametric
methods based on GC content, mappability, or restriction site
density, as long as they provide a score for each bin. Additionally,
ACCOST requires a mappability score for each bin, but this
information is only used to discard some bins from the analysis.
Likewise, HiCDCPlus requires GC content information, but
the tool can compute it internally as long as the corresponding
genome is available from Bioconductor [50]. Optionally, map-
pability information can also be provided. In contrast to other
tools, CHESS performs a test and derives a p-value only if a set
of background regions, where no difference is expected between
the two matrices, is provided. Otherwise, CHESS only computes
similarity scores between the matrices and does not return a
p-value.
Finally, some of the tools contain format converters, like HiC-
compare and multiHiCcompare that provide functions to convert
.hic and .cool files to their own internal format.
Of note, sslHiC is the only tool that restricts the bin size.
Namely, it can only analyze Hi-C matrices at resolutions 10, 50, or
500 kb, because the authors trained their deep-learning models
for these resolutions only.
Programming languages and packaging
Most of the tools reviewed are implemented in Python and/or R (Table 2), with the exception of HOMER. From a user perspec-
tive, availability through a package management system (like
DifferentialanalysisofHi-Cdata | 7
pip, conda, or the CRAN repository) is highly valuable because tools.Inparticular,wedescribethedatasets,thetools,andhowwe
dependencies are usually handled during the installation process, designed the tests to evaluate the Type-I error control, the power,
making it much easier to install compared to non-packaged tools. and the biological relevance of the results.
Bioconductor packaging [50] offers additional stability for several
reasons: the code is extensively reviewed before acceptance,every Tested tools
release is tested on the three main operating systems, and exten-
Among the tools described in “Methods,” we excluded three tools
sive documentation is required (including a use case vignette).
from the simulation study:
Python packages often rely on an external documentation web-
site,which can be extensive and detailed (such as the ones hosted 1) CHESS because it is made to provide p-values for fixed-
on the “Read the Docs” documentation service https://about. sized windows of the Hi-C matrix that “cannot be smaller
readthedocs.com/). than 20×the bin size of the data”(User documentation even
From this point of view, the R/Bioconductor packages diffHic, recommends to use regions spanning at least 100× the bin
HiCcompare, HiCDCPlus, andm ultiHiCcompare are easy to size of the data.), which is hardly comparable with the other
install, thanks to the Bioconductor common installation process. tools (that obtain results at a bin pair resolution);
FIND is also easy to install, even if not included in an official 2) ACCOST because it is not actively maintained anymore (it
package repository. resulted in errors with Python. We contacted the authors
Similarly, for Python tools, CHESS and Selfish are easy to about this problem which they intend to solve);
install, thanks to pip. In addition, Selfish also proposes an 3) HOMER, which led to an error with our data. We contacted
installation process via a Docker or a Singularity/Apptainer the authors about this problem without success.
container, providing further reproducibility and robustness. In
Supplementary Table S3 provides the link to the source code
contrast, ACCOST does not offer a pip installation and is just
and the version or date at which it was accessed for installation.
provided as Python scripts. For ACCOST, the authors simply
All tools were launched successfully for all experiments except
mention its dependency with Python 2.7 and R ,a s well as with
for:
numpy, scipy,and somes cikit-learn libraries. In contrast, sslHiC
is easier to use thanks to a provided conda environment setting • multiHiCcompare that filtered out all bin pairs in chr 21
file. HOMER includes a script, which installs and configures experiments with the semi-simulated dataset. All bin pairs
the tool. A description of the documentation of the tools, were also filtered for chr 13, 14, and 15 of the CTCF depletion
together with their comprehensivenesses and readabilites, and a dataset. The tool was successful but no results were pro-
description of issues encountered during installation of the tools duced;
are provided as Supplementary Sections 3.1 and 3.2, respectively. • sslHiC that we could run only on 500 kb resolution matrices.
The tool was successful for this setting but not designed for
Illustrative datasets
the other settings.
In addition, having some data included in the tool for illustration
is usually appreciated by users. From this perspective, HOMER
Tool parameters
and Selfish do not include any dataset. diffHic includes a small
BAM file used in its manual, while its vignette features three These tools were tested with their default parameters whenever
external datasets also mentioned in their article. FIND, HiCcom- possible.TheexceptionstothischoicearelistedinSupplementary
pare, HiCDCPlus,ands slHiC include (part of) the processed data Table S4 and correspond to parameters with no default but
from [3](GEO: GSE12878),whichthey used intheir documentation required by the tool to work, as for FIND.
and also (except for FIND) in the results of the article. ACCOST In addition, by default FIND filters out results for which the
also includes part of the same dataset but does not use it in adjusted p-value was above a certain threshold. We turned this
the HTML manual for illustration (this dataset is discussed in filter using qvalue = 1 to retrieve all results (Using this setting
their article, however). sslHiC also includes datasets simulated results in FIND returning adjusted p-values equal to one as zeros,
from chromosome 21 of a GM12878 cell line dataset (the original which is not desirable. We manually corrected this setting in our
dataset is only used to illustrate another feature of the tool on code.). We also used the option to split the computation into
a replication measure). The simulated dataset consists in three several chunks (otherwise, using the tool resulted in memory
couples of matrices including a certain percentage of simulated overload).
differential interactions with varying fold changes (2, 4,and 6). Similarly, diffHic provides several functions that can perform
CHESS includes the processed data from [52] (ArrayExpress: E- different types of filtering before the differential analysis. In our
MTAB-5875) and multiHiCcompare part of the data from [53] experiments,we did not filter out bin pairs with a low logCPM but
(GEO:GSE104888).Both usethesedatasets intheirdocumentation we used their filterTrended filter.
and article. For a given experiment and tool, p-values were adjusted inde-
Note that all datasets are not provided under the same format. pendently for each chromosome. The BH procedure [44] was used
ACCOST provides compressed .tsv files that correspond to their toadjustp-valueswhenthetooldidnotprovideadjustedp-values.
input format,CHESS and HiCDCPlus provide .hic files,FIND and For tools that perform a per-distance-basis FDR correction (HiC-
HiCcompare embed data in their tool (they can then be loaded compare and multiHiCcompare), we kept their adjusted p-values
using the function data, directly properly formatted for usage in and also computed adjusted p-values at the chromosome level
their functions or as GInteractions objects [49]). (“standard” BH procedure). In the Results section, these two types
of results are identified by HiCcompare (original adjusted p-value
of the tool) and HiCcompare-realFDR (re-computed adjusted p-
Numerical experiments
value). We were unable to perform this correction for Selfish,
In this section, we present the extensive numerical experiments FIND, ands slHiC, which, unfortunately, do not provide raw p-
that we performed to assess the statistical performance of the values.
8 | Jorgeetal.
Figure 2. Design of the simulations. (a) The available matrices used for the numerical experiments consist in five technical replicates from three
chromosomes (1, 7, and 21) generated at three different resolutions (200 kb, 500 kb, 1 Mb). Numbers at the bottom row correspond to genomic positions
(inMb),indicatingthesizeofthesematrices.(b)IllustrationofthesimulationprocessforType-Ierrorassessment(H1 setting,topright)andassessmentof
false positive rate (FPR) and true positive rate (TPR) (H0 setting,bottom left).Type-I error control was assessed by splitting technical replicates randomly
into two groups, while FPR and TPR were assessed by generating artificial true positive examples where read counts are increased in a target zone by
adding resampled Hi-C data from the remaining technical replicate.
Semi-simulated data study Foreachchromosome,weassignedthefivetechnicalreplicates
Wefirstusedausecasewherethegroundtruthofdifferenceloca- to two conditions (three replicates in a condition and the other
tions is precisely controlled. One possibility to do this would have two in the other condition) and processed them with the six tools
been to rely on a simulation study,generating data from a specific to extract p-values for differential interactions between the two
probability distribution. A natural choice for this distribution conditions. The C3 5 = 10 possible assignments of the replicates
would be the NB model, since a number of differential analysis into two groups were obtained and considered as independent
tools rely on this distribution (diffHic, HiCDCPlus, multiHiCcom- experiments (i.e. p-values were adjusted independently in each
pare,andA CCOST). However, the evaluation process would have assignment and chromosome).
then been biased infavor of thesetools.More generally,any choice For tools designed to compare only two matrices (one for each
of a particular distribution induces biases since the true data condition), i.e. HiCcompare and Selfish, we merged the replicates
generating distribution is unknown. of the same condition into a single matrix before processing the
We therefore used semi-simulated data coming from real Hi- two resulting matrices with the tool (Fig. 2b). Also, Selfish results
C data. This type of approach has previously been applied mul- were not symmetric (the p-value assigned to the bin pair (i,j) was
tiple times to benchmark tools for, e.g. RNA-seq data [54–56]. not always equal to the p-value assigned to the pair (j,i) whereas
More specifically, we used an ENCODE dataset [57] from a Hi- the Hi-C matrix is symmetric by design and logFC were found
C experiment performed on a human colon sample (experiment identical between the two pairs). For instance, for simulation 6,
accession: ENCSR295BDK), that includes five technical replicates chromosome 21, and resolution 1 Mb, Selfish returned a p-value
(sequencing runs). To obtain Hi-C matrices, raw sequencing reads of 0.9 for the pair (2810,2805) and a p-value of 7.4e−4 for the pair
ofeachtechnicalreplicatewereprocessedusingthenf-core/hic (2805,2810), as documented in our code repository). To address
pipeline [58] v1.2.2 on the assembly version GRCh38 of the human this, we arbitrarily kept one of the two p-values returned by the
genome (see Supplementary Section 4.1 for further details). Hi- tool (the one corresponding to i < j).
C matrices at three different resolutions and for three different The total number of performed tests, the percentage of signifi-
chromosomes were finally used, as shown in Fig. 2a. Processed cant results (based on p-values and adjusted p-values) at different
data are available at https://doi.org/10.57745/LR0W9R. risk levels as well as the empirical cumulative density function
To assess the Type-I error control,we ran each tool on technical (ECDF) were obtained for each tool, chromosome, and resolution.
replicates randomly split into two groups, where no signal is Note that not all tools provided raw p-values. FIND, Selfish,
expected. We also assessed the statistical power of the tests by and sslHiC only returned p-values adjusted for FDR control. For
creating a controlled difference in a given part of some matrices. these tools, one can only verify that the average number of tests
Figure 2 illustrates (a) the data matrices used and (b) the test declared significant (at any target FDR level) is zero for a H0
protocol. setting.
Simulations with ground truth signal (H
1
setting)
Type-I error control (H
0
setting)
The same dataset was used to generate pseudo-simulated exper-
The quality of statistical tests is usually assessed via their math-
iments corresponding to the existence of a region with a positive
ematical validity (proper control of the Type-I error, or false dis-
signal, as described in Fig. 2b. More specifically, the five technical
coveries) and by their performance (statistical power or ability to
replicates of each chromosome were used in the following way:
detecttruepositives).Inthisfirstsimulationsetting,wegenerated
data under the null hypothesis (H0) in which no signal is expected, • two replicates were used as the Hi-C matrices of the first
as described in Fig. 2b. condition;
DifferentialanalysisofHi-Cdata | 9
Table 3. Total number of bin pairs (third column) and number of
bin pairs in the target zone for the evaluation of true positive
detection rates (fourth column; H 1 setting only), for each
chromosome and resolution
Chr. Resolution Total In target
1 1Mb 26 741 1275
7 1Mb 12 765 861
21 1Mb 861 45
1 500 kb 105 231 5151
7 500 kb 49 967 1888
21 500 kb 3218 136
1 200 kb 637 599 31 375
7 200 kb 306 209 10 936
21 200 kb 17 558 730
Note that, due to filters in the tools, not all these bin pairs were actually
tested for each method.
Figure 3. Average percentage of performed tests (across the 10 repeats)
• two other replicates were modified to be used as the Hi-C
compared to the number of bin pairs passed as input to the tool (given in
matrices of the second condition. We first selected a region, Table 3) across chromosomes and resolutions (200kb, 500kb, and 1Mb) in
called “target zone”,and increased the counts of the matrices the H0 setting. sslHiC could only be used on 500 kb resolution data.
of the second condition in this region by adding the cor-
responding values from the fifth replicate. The target zone
particular genomic regions with a high density of active CTCF
consisted of bin pairs where both bins were located within
binding sites [ 59]. In order to assess the biological consistency
the 20th to 40th percentile range of chromosome length,
of the predicted differential interactions, we compared the corre-
with 0% representing the start of the chromosome and 100%
sponding genomic positions with those of the active CTCF binding
representing the end.
sites that were profiled by ChIP-seq experiments on the same cell
This simulation setting was designed to obtain a controlled dif- line (GEO ACCESSION GSE129997, [60]). More precisely, for each
ferential area in the matrix approximately mimicking a structure 100 kb bin of the genome, we both computed:
similar to a TAD. In particular, this setting should favor 2D-aware
• the number of times this bin was included in a bin pair found
tools, e.g. tools that exploit the spatial autocorrelation of the 2D
significantly different by the tool;
Hi-C matrix (FIND, Selfish,ands slHiC).
• the number of CTCF active sites (called peaks) present in this
Finally,the four matrices (from two conditions) were processed
bin pair.
as described in “Type-I error control (H0 setting)”, distinguishing
results for the target zone from the others. The precision-recall The joint distribution of these two quantities was thus
(PR) curves based on adjusted p-value filtering were then obtained obtained, and the Spearman correlation was computed to assess
to simultaneously assess the precision (i.e.the ratio of bin pairs in the general biological consistency of each tool’s results.
the target zone among bin pairs declared positive) and the recall
(i.e. the ratio of bin pairs declared positive among bin pairs in Computational time
the target zone). Note that the recall is also named power in the All tools were tested on the same infrastructure(Genotoul-Bioinfo
framework of statistical tests and that “1− Precision” indicates if cluster) on a single CPU node, except for sslHiC that was tested
the test properly controls the FDR. on a different node because it required GPU. For comparison
Table 3 gives the total number of bin pairs for each chromo- purposes, we ran the tools on one processor only and recorded
some and resolution, as well as the number of bin pairs in the computational times in the H1 setting and for the CTCF depletion
target zone. study.
Processed data as used in the numerical experiments along
CTCF depletion study
with scripts implementing the different tools and performing
To test the tools on a real life use case, we retrieved publicly the result analysis are made available at https://forgemia.inra.fr/
available data from a CTCF depletion study in post-mitotic mouse scales/replication-chrocodiff.
cells [59]. This study features a Hi-C chromatin structure pro-
filing of a murine erythroblast cell line under two conditions:
Results
eitherunderaccutedepletionofCTCFthroughanauxin-inducible
Number of tested bin pairs
degron system (CTCF-condition) or in the control condition with-
out auxin-induced depletion (CTCF+ condition). Hi-C libraries We used the H0 setting to assess the differences in the number of
were generated, sequenced, and processed for three biological bin pairs filtered before the test procedure by the different tools.
replicates per condition. We downloaded the six corresponding Figure 3 provides the proportion of tests performed for each tool
interaction matrices (GEO Accession GSE168251) and ran all the in the H0 setting (relative to the maximum number of possible
tools on each autosome independently at the resolution of 100 kb. tests, as given in Table 3 for each chromosome and resolution).
Although no precise and exhaustive ground truth exists for The difference in the numbers of tested bins is thus only due to
such a real case dataset, it is well known that the CTCF protein differences in the filtering step.
plays a major role in chromatin loop and TAD boundary forma- The different tools apply pre-filtering steps that resulted in a
tion.As reported in the original study,many structural differences very different number of tested bin pairs.HiCcompare performed
are therefore expected between the two conditions, involving in a number of tests that is constantly close to the maximum and
10 | Jorgeetal.
HiCDCPlus constantly performed a very low number of tests its proper control of Type-I error. Finally, no large difference was
because it only tests (the union of) regions with an interaction observed between the standard BH correction (“XXX-realFDR”)
considered significantly above the interaction background (FDR and the multiple test correction implemented in multiHiC-
adjusted p-value < 10%). For the relatively short chromosome 21, compare and HiCcompare. This is confirmed by the strong
multiHiCcompare did not perform any test (all interactions were linear relationship between these two quantities (Supplementary
filtered out at preprocessing). However, it performed a number Fig. S2).
of tests close the maximum for the other two chromosomes For the tools that returned unadjusted p-values, Fig. 5 provides
at resolutions 500 kb and 1 Mb. At a 500 kb resolution (the the ECDF of p-values. Note that the data displayed in Fig. 4 cor-
only resolution available for this tool), sslHiC performed a num- respond to the values of the ECDF at risk x = 5% (a) and 1% (b),
ber of tests close to the maximum for the three chromosomes. respectively.
Finally, diffHic and Selfish filtered out approximately half of the For all resolutions and chromosomes, diffHic was the tool
bin pairs. closest to the expected uniform distribution, followed closely by
Note that the differences in the number of tested bin pairs are the slightly conservative multiHiCcompare (Fig. 5). HiCcompare
partially due to default values set differently by different tools exhibited a slight excess of very small p-values; in the area where
for the same parameter: For instance, HiCcompare filters out bin thep-valueisbelow0.1%,theECDFofHiCcomparewasfrequently
pairs with an average A value smaller than the 10th percentile abovethediagonal(seealsoFig. 4).Thisbehaviorcanbeexplained
of A values while multiHiCcompare filters out bin pairs with an by its incapacity to account for variability across replicates of one
average A value smaller than 5. condition, resulting in an excess of false positives. In contrast,
HiCDCPlus generally displayed the opposite behavior, suggesting
Type-I error control (H 0 setting) a lack of power (especially for chromosomes 1 and 7). However,
Figure 4 provides the percentage of tests declared significant for it occasionally presented a strong excess of false positives, as
all chromosomes, resolutions, and tools, based on a 5% and a observed on chromosome 21.
1% thresholding of p-values and adjusted p-values. Figure S1 in
Precision and Recall (H setting)
Supplementary material additionally provides the same plots for 1
a 10% threshold. Figure 6a provides the proportion of tested interactions that are
In H0 settings, the percentage of p-values below 5% is expected located within the target zone, where positive calls are expected
to be at most 5% if the test is properly calibrated (type-I error con- (true signal). This proportion may vary even for tools that rely
trol).Apercentagemuchsmallerthan5%indicatesthattheType-I on similar models or methods, because different data filtering
error control is valid but that the tool is conservative, suggesting methods are applied before testing for differential interaction.
that the test may be underpowered in non-H0 situations. Also, Results confirmed that this filtering step can have per se astrong
since some tools only returned the adjusted p-value, we also gave impact on the test. In particular, HiCDCPlus predominantly dis-
the percentage of adjusted p-values below 5%. Since p-values are carded interactions outside the target zone rather than inside,
adjusted to control the FDR, this percentage is expected to be 0 if which may be a desirable behavior. However, the overall number
the test is properly calibrated.However, it is not possible to assess of retained interactions was generally very low for this tool (see
how conservative the test is only based on adjusted p-values. Fig. 3 and the corresponding discussion). The other tools tended
The results shown in Fig. 4 are remarkably consistent across to generally have a proportion of tested interactions in the target
resolutions. This illustrates the fact that since FDR corre- zone close to the corresponding proportion in the original matrix
sponds to a proportion of false positives, FDR control is a (before filtering).
priori designed to be comparable across studies with different Figure 6b displays PR curves based on predictions computed
numbers of tests. Overall, the results show that only diffHic from adjusted p-values, for all chromosomes, resolutions, and
and multiHiCcompare properly controlled the Type-I error on tools. An ideal classifier would have a precision of one and a
this dataset, with a percentage of tests declared positive very recall of one. The resulting PR curve, based on various adjusted
close to the expected value. Nonetheless, for chromosome 21, p-value thresholds, would then be the horizontal line joining
multiHiCcompare did not perform any test as discussed above the point at (0,1) coordinates to point at (1,1) coordinates (i.e.
(see Fig. 3). varying power depending on the number of interactions selected
HiCcompare, which does not account for replicates and hence by the threshold, but all true positives), followed by a vertical line
for variability within conditions, suffered from a small excess of joining (1,1) and (1,0) (i.e. negative interactions are all selected
false positives (e.g. chromosome 21, 1 Mb resolution, 1% risk). On after the positive one, for larger thresholds). The symbols on
the contrary, HiCDCPlus detected very few false positive results, the PR curves in Fig. 6 b indicate for each tool the obtained
except for chromosome 21 which displays a massive excess of precision and recall when thresholding the adjusted p-values
false positives. This discrepancy between chromosomes could provided at risk 5%, a threshold that corresponds to standard
be related to the very low proportion of bin pairs passing the practice. A well calibrated tool should have a precision above
HiCDCPlus filters (see Fig. 3). Both Selfish and, in particular, the dashed horizontal line at 95% (for a clearer visualization of
FIND produced a large number of false positives, as visible these results, Fig. S3 in Supplementary material also provides
in the plots based on adjusted p-values (bottom). For both the obtained precision and recall for additional adjusted p-values
methods, this could be explained by a statistical issue in the thresholds).
definition of the bin pair-level p-value (lack of multiple testing In Fig. 6b, diffHic appears to be one of the best tools in the
correction across radii for Selfish, and incorrect assumption H1 setting, as it yields curves closest to the ideal classifier in
of independence between aggregated p-values for FIND), as a majority of cases. In particular, it performed best on smaller
explained in Section “Methodological background of the tools.” chromosomes and at higher resolutions. This variability seems
sslHiC did not return any positive result based on adjusted p- to be directly related to the number of performed tests: The
value thresholding (which is the expected behavior). However, smaller the number of tests (chromosome 21 or lower resolutions
since it does not provide raw p-values, we were not able to assess correspond to smaller numbers of interactions), the better the
DifferentialanalysisofHi-Cdata | 11
Figure 4. Percentage of tests declared significant (H0 setting) for three chromosomes and three resolutions (200kb, 500kb, and 1Mb). Decisions are
taken based on p-values (top) and adjusted p-values (bottom) with 5% (left) and 1% (right) risks. The black horizontal line (top figures) indicates the risk
controlled by raw p-values. When the method did not perform a global FDR correction (see Table 1), we re-computed the adjusted p-values with the BH
method applied to raw p-values (when available). This corresponds to columns named “XXX-realFDR” (bottom figures). sslHiC could only be used on
500 kb resolution data and multiHiCcompare performed no test on chromosome 21 because of its filtering step.
performance. However, in a number of cases, it did not properly a curve consistently close or above the ideal classifier. However,
control the FDR (the symbol corresponding to the 5% threshold its performances were bad for chromosomes 7 and 21, as all
of p-values is below the vertical dotted line at 95%). For instance, interactions had an adjusted p-value equal to 1. Note that, even
for chromosome 1, resolution 200 kb, the precision of diffHic was forchromosome1,FINDwasfarfromproperlycontrollingtheFDR
between 50 and 75% for the three thresholds. when thresholding the adjusted p-value. In all cases, its precision
multiHiCcompare and HiCcompare often displayed similar was close to 0.
performances (and sometimes better than diffHic),with a marked HiCDCPlus had a rather heterogeneous and mild performance
disadvantage of HiCcompare for the highest resolution (200 kb). across chromosomes and resolutions. However, it was systemati-
Aside from this resolution, and despite not utilizing informa- cally the second or third best performing method.
tion on biological replicates, HiCcompare achieved slightly better Finally, although being somewhat heterogeneous between
results than multiHiCcompare overall. Note that, similarly to the chromosomes and resolutions, Selfish and sslHiC had poor
H0 setting, the difference between the standard BH correction performances on this benchmark, altogether with PR curves
(“XXX-realFDR”) and the multiple testing correction implemented usually close or below those of a random classifier.
in multiHiCcompare and HiCcompare is small, with a slight
improvement of performances when the standard BH correction
CTCF depletion study
is used. However, none of the two tools and the two versions In order to test the tools in a realistic setting on a full size dataset,
of the correction properly controls the FDR at 5%. The only we retrieved and analyzed genome-wide Hi-C matrices from a
exceptions are HiCcompare at resolutions 1 Mb and 500 kb, but CTCF depletion study in mouse [59] (see Methods).
only for chromosomes 1 and 7 and with a recall of zero for Figure 7 provides for each tool the joint distribution over the
chromosome 1. 100 kb bins of the genome between the number of CTCF sites
From a PR curve point of view, FIND performed rather well for present in the bin (x-axis) and the number of differential inter-
chromosome 1, especially at resolutions 500 kb and 1 Mb with actions in which the bin was involved after comparing matrices
12 | Jorgeetal.
Figure 5.ECDF of p-values (H0 setting).Well-calibrated tools are expected to have an ECDF that closely follows the diagonal,corresponding to a uniform
distribution of p-values under H0. An ECDF below the diagonal indicates a valid but conservative test, while an ECDF above the diagonal indicates
that the test is not properly calibrated, yielding an excess of false positives. multiHiCcompare performed no test on chromosome 21 because of its
filtering step.
from the CTCF+ and the CTCF- conditions (y -axis). Since CTCF tests. This can primarily be attributed to the fact that its filtering
depletion is expected to predominantly impact genomic regions steps removed most bin pairs, and its computational time scaled
with CTCF binding sites,a positive correlation should be observed with the total number of bin pairs rather than the number of
between these quantities. bin pairs remaining after filtering. The tools showing the best
This was the case for some of the tools. In particular, scalabilitywereHiCcompare,multiHiCcompare,andSelfish.This
Spearman’s correlation values of r = 0.44, r = 0.42,and r = 0.41 result may be partly attributed to the faster implementation of
were, respectively, obtained for multiHiCcompare, HiCDCPlus, the cyclic LOESS (used for MA and MD normalization) available in
and diffHic. Globally, these tools detected more differential HiCcompare and multiHiCcompare, but not in diffHic.
interactions between CTCF-rich regions than between CTCF- Finally,as sslHiC is designed to run on GPU processors,its com-
poor regions, as expected. However, in line with previous results putational time could not be directly compared with that of the
from the H0 setting (Fig. 3), HiCDCPlus realized a low number other tools.Despite its relatively short runtime,its computational
of tests compared to the total number of bin pairs in the whole resource requirements were substantial.
dataset.Less than 5% of bin pairs were kept after the filtering step
(Supplementary Fig. S4).
Discussion and conclusion
Onthecontrary,nosubstantialcorrelationwasobtainedforthe
other tools,with r =0.04 for HiCcompare,r =0.05 for Selfish,and Our benchmark allowed to evaluate and compare the statistical
r=0.08 for FIND. performances of Hi-C data differential analysis tools on practical
examples. Importantly, the results revealed that the FDR was not
Computational time
properly controlled across all tools.This could be due to the small
Figure 8 shows the computational time required for performing number of samples in our experiments (only two per condition
the tests in the H1 setting and for the CTCF depletion dataset. In for the H1 setting), highlighting the importance of that factor.
addition, Supplementary Fig. S5 provides another representation Nonetheless, some tools—particularly diffHic—still managed to
of these results for the H1 setting with respect to the number correctly control the Type-I error rate in the H0 setting. Addi-
of tests performed, and Supplementary Fig. S6 gives the total tionally, the per-distance-basis FDR correction appeared to have
computational time required for the CTCF depletion dataset. a limited effect, especially when applied to a single chromosome.
FIND exhibited large computational times for certain chro- Globally, in our benchmark, diffHic delivered the best results.
mosomes and resolutions. However, the scalability of this tool It properly controlled the Type-I error rate in the H0 setting and
was not the worst: HiCDCPlus showed the greatest increase in was the only tool to properly control the FDR in some cases.
computational time with respect to the number of performed Its power, for a 5% risk, was also among the best, always larger
DifferentialanalysisofHi-Cdata | 13
Figure 6.Results for H1 setting.(a) Proportion of tested interactions that are in the target zone for each tool.The horizontal line indicates the proportion
of interactions within the target zone of the original data before filtering. The reported proportions (y-axis) lie above or below the horizontal line
depending on whether the tools (x-axis) predominantly filter interactions outside or inside the target zone, respectively. (b) PR curves computed from
adjusted p-values, displaying recall (or power, x-axis) and precision (y-axis). For each method, the point corresponding to a threshold= 0.05 (target FDR,
as claimed by the method) is marked with a specific symbol. For methods that filtered out all interactions in the target zone before the test, the Recall
cannot be computed (because the denominator would be 0).In this case,we arbitrarily represented them with a circle at (0,0).Finally,the top horizontal
dashed line (in black) corresponds to a Precision of 95% and the bottom horizontal dashed line (in blue) corresponds to the precision expectation of a
uniform random draw of interactions. sslHiC could only be used on 500 kb resolution data and multiHiCcompare performed no test on chromosome
21 because of its filtering step.
Figure 7. Joint distribution of the number of CTCF sites and the number of differential interactions per genomic bin of 100 kb in the CTCF depletion
dataset. Each boxplot represents the distribution of differential interactions (y-axis) obtained by a given tool (one per panel) between matrices from the
CTCF+ and the CTCF-conditions for genomic bins with 0,1,2,or at least 3 CTCF sites (x-axis).The Spearman correlation between these values across all
bins is provided for each tool (r). Bins with many CTCF sites are expected to be predominantly involved in differential interactions upon CTCF depletion
compared to bins with few CTCF sites, as observed in results from diffHic and HiCDCPlus for instance (left side).
14 | Jorgeetal.
Figure 8. Computational time. Left: Computational time in seconds (y-axis) needed for each tool (y-axis) to run in the H1 setting. sslHiC could only be
used on 500 kb resolution data and multiHiCcompare performed no test on chromosome 21 because of its filtering step. Right: Computational time in
seconds (y-axis) versus the number of tests performed in a given chromosome (y-axis) for the CTCF depletion dataset. sslHiC could not be used.
than 50% and generally close to 100%.Interestingly,for the lowest showsuperiorperformances,eveninsituationsliketheH1 setting,
resolution, HiCcompare also showed interesting performances in where there is a strong spatial dependency in differential interac-
the H1 setting but always exhibited an inflated number of false tion locations within the 2D Hi-C matrix. This suggests that the
positives in the H0 setting and gave disappointing results in the current methods for incorporating spatial 2D structure may not
CTCF depletion use case. be effectively capturing its relevance.
diffHic and multiHiCcompare produced comparable results in Finally, it is worth noting that the currently available tools are
the H0 setting and, in terms of PR curves, in the H1 setting. Both still unable to accommodate a wide variety of study designs. Few
tools also showed good biological consistency between Hi-C and methods allow to use covariates (see Table 1) and, to the best of
ChIP-seq data in the CTCF depletion analysis. This alignment was our knowledge,no tool is capable of properly handling paired data
expected, as they rely on the same model. However, the perfor- (e.g. differences between two tissues, with multiple individuals
mance differences observed between the two tools underscore each providing a pair of tissue samples as replicates) or repeated
the importance of filtering and the choice of default param- measurement designs (similarly to what is done in mixed
eters. Notably, the default filters in multiHiCcompare seemed models).
sometimes too stringent (e.g. no results were obtained for some In this study, we focused on two datasets, encompassing two
chromosomes in both the simulated and real-world experiments). simulation settings and a real-world application. Expanding the
Additionally, the FPR of multiHiCcompare consistently exceeded investigation to include broader datasets and experimental set-
30% (and often surpassed 50%) for a 5% risk threshold. The tings would be valuable to assess the robustness of our conclu-
strong impact of preprocessing steps is unsurprising and has been sions across more varied designs, resolutions, and size effects.
previously acknowledged in other omics studies [61]. Additionally, our analysis underscored the need for a deeper
HiCDCPlus was also found to be overly stringent in its fil- understanding of the complex interplay between preprocessing
tering step, consistently performing a very low number of tests. steps—particularly normalization types and filtering—and the
However, in the CTCF depletion application, it produced good models used.
results.
FIND presents an interesting case. In both simulation settings,
the tool tended to predict too many false positives for a given
Key Points
threshold.However,on chromosome 1 in the H1 setting,it demon-
• We reviewed and benchmarked available tools for differ-
strated excellent ordering of interactions based on adjusted p-
ential analysis of Hi-C matrices.
values, with the PR curve closely approaching that of a perfect
• Preprocessing steps differed between tools, strongly
classifier. This suggests that the adjusted p-values returned by
impacting the results, even for tools with the same type
FIND can serve as a reliable score for ranking interactions by sig-
of model.
nificance level, although they cannot be statistically interpreted.
• None of the tools properly controlled the FDR at the
In this case, using higher thresholds than typically expected is
expected rate in our simulation setting. However, some
recommended. However, for chromosomes 7 and 21, all adjusted
tools effectively controlled the Type-I error in situations
p-values returned by FIND were equal to 1. Overall, contrary to
where no signal was expected in the data.
diffHic, the performance differences observed with FIND do not
• In our simulations, diffHic yielded the best overall
seem to be directly related to the number of tested interactions.
results. Currently, tools based on a 2D-aware model did
For instance, in the H1 setting, FIND performed better on the
not outperform the others.
largest chromosome but worse for the highest resolution of 200
• Our review highlighted the need for models and tools
kb, which has more interactions to test.
able to handle paired designs and repeated measure-
Interestingly, 2D-aware tools such as FIND, Selfish,ands slHiC
ment designs.
leverage the spatial auto-correlation inherent to the 2D Hi-C
matrices in their modeling. However, these tools did not generally
DifferentialanalysisofHi-Cdata | 15
Acknowledgments gene-enhancer interactions. Cell 2015;161:1012–25. https://doi.
org/10.1016/j.cell.2015.04.004
We are grateful to the genotoul bioinformatics platform Toulouse
8. Spielmann M, Lupiáñez DG, Mundlos S. Structural variation
Occitanie (Bioinfo Genotoul,https://doi.org/10.15454/1.557236932
in the 3D genome. Nat Rev Genet 2018;19:453–67. https://doi.
8961167E12) for providing assistance, as well as computing and
org/10.1038/s41576-018-0007-0
storage resources.
9. Marieke Oudelaar A, Higgs DR. The relationship between
genome structure and function. Nat Rev Genet 2020;22:154–68.
Author contributions https://doi.org/10.1038/s41576-020-00303-x
10. Gunsalus LM, McArthur E, Gjoni K. et al. Comparing chromatin
SF, PN, MZ, and NV conceived the project and designed the study.
contact maps at scale: methods and insights bioRxiv preprint
All authors contributed to the review and to the benchmark. All
2023.04.04.535480. 2023.
authors wrote, read, revised, and approved the manuscript.
11. Yang T,Zhang F,Yardimci GG.et al.HiCRep: assessing the repro-
ducibility of Hi-C data using a stratum-adjusted correlation
Supplementary data coefficient.GenomeRes2017;27:1939–49.https://doi.org/10.1101/
gr.220640.117
Supplementary data are available at Briefings in Bioinformatics
12. Wang Z,Zhang Y,Zang C.BART3D: inferring transcriptional reg-
online.
ulators associated with differential chromatin interactions from
Conflicts of interest: The authors declare no conflict of interest. Hi-C data.Bioinformatics 2021;37:3075–8.https://doi.org/10.1093/
bioinformatics/btab173
13. Soler-Vila P, Cuscó P, Farabella I. et al. Hierarchical chromatin
Funding
organization detected by TADpole. Nucleic Acids Res 2020;48:e39.
This work is funded by the INRAE/DIGIT-BIO network ChrocoNET https://doi.org/10.1093/nar/gkaa087
and by the CNRS project SCALES (Mission “Osez l’interdiscip 14. Mourad R. TADreg: a versatile regression framework for
linarité”). E.J.’s PhD is funded by INRAE. TAD identification, differential analysis and rearranged 3D
genome prediction. BMC Bioinformatics 2022;23:82. https://doi.
org/10.1186/s12859-022-04614-0
Data availability
15. Chen F, Li G, Zhang MQ. et al. HiCDB: a sensitive and
For the H0 and H1 settings, raw sequencing data were obtained robust method for detecting contact domain boundaries.
from the ENCODE project https://www.encodeproject.org/ using Nucleic Acids Res 2018;46:11239–50. https://doi.org/10.1093/nar/
accession ENCSR295BDK. Processed Hi-C data (by chromosome, gky789
resolution, and technical replicates) and corresponding quality 16. Chakraborty A, Wang JG, Ay F. dcHiC detects differential
controls are available at https://doi.org/10.57745/LR0W9R. compartments across multiple Hi-C datasets. Nat Commun
For the CTCF dataset, Hi-C matrices and ChIP-seq peaks were 2022;13:6827. https://doi.org/10.1038/s41467-022-34626-6
retrieved from GEO using accession GSE168251 and GSE129997, 17. Hua D, Ming G, Zhang X. et al. DiffDomain enables iden-
respectively. Processed Hi-C data (by chromosome at 100 kb tification of structurally reorganized topologically associat-
resolution) and converter script are available at https://doi. ing domains. Nat Commun 2024;15:502. https://doi.org/10.1038/
org/10.57745/LR0W9R. s41467-024-44782-6
18. Cook KB, Hristov BH, Le Roch KG. et al. Measuring sig-
nificant changes in chromatin conformation with ACCOST.
References
Nucleic Acids Res 2020;48:2303–11. https://doi.org/10.1093/nar/
1. Bonev B, Cavalli G. Organization and function of the 3D gkaa069
genome. Nat Rev Genet 2016;17:661–78. https://doi.org/10.1038/ 19. Lun ATL, Smyth GK. diffHic: a Bioconductor package to detect
nrg.2016.112 differentialgenomicinteractionsinHi-Cdata.BMCBioinformatics
2. Lieberman-Aiden E, Van Berkum NL, Williams L. et al.Compre- 2015;16:258. https://doi.org/10.1186/s12859-015-0683-0
hensive mapping of long-range interactions reveals folding prin- 20. Djekidel MN, Chen Y, Zhang MQ. FIND: difFerential chromatin
ciples of the human genome. Science 2009;326:289–93. https:// INteractions Detection using a spatial Poisson process. Genome
doi.org/10.1126/science.1181369 Res 2018;28:412–22. https://doi.org/10.1101/gr.212241.116
3. Rao SSP, Huntley MH, Durand NC. et al. A 3D map of the 21. Stansfield JC, Cresswell KG, Vladimirov VI. et al. HiCcom-
human genome at kilobase resolution reveals principle of chro- pare: an R-package for joint normalization and comparison
matin looping. Cell 2014;159:1665–80. https://doi.org/10.1016/j. of HI-C datasets. BMC Bioinformatics 2018;19:279. https://doi.
cell.2014.11.021 org/10.1186/s12859-018-2288-x
4. Dali R, Blanchette M. A critical assessment of topologically 22. Sahin M, Wong W, Zhan Y. et al. HiC-DC+ enables system-
associating domain prediction tools. Nucleic Acid Res 2017;45: atic 3D interaction calls and differential analysis for Hi-C
2994–3005. https://doi.org/10.1093/nar/gkx145 and HiChIP. Nat Commun 2021;12:3366. https://doi.org/10.1038/
5. Zufferey M,Tavernari D,Oricchio E.et al.Comparison of compu- s41467-021-23749-x
tational methods for the identification of topologically associ- 23. Stansfield JC, Cresswell KG, Dozmorov MG. multiHiCcom-
ating domains. Genome Biol 2018;19:217. https://doi.org/10.1186/ pare: joint normalization and comparative analysis of complex
s13059-018-1596-9 Hi-C experiments. Bioinformatics 2019;35:2916–23. https://doi.
6. Liu L, Han K, Huimin Sun L. et al. A comprehensive review of org/10.1093/bioinformatics/btz048
bioinformatics tools for chromatin loop calling. Brief Bioinform 24. Ardakany AR, Ay F, Lonardi S. Selfish: discovery of differential
2023;24:bbad072. https://doi.org/10.1093/bib/bbad072 chromatin interactions via a self-similarity measure. Bioinfor-
7. Lupiáñez DG, Kraft K, Heinrich V. et al. Disruptions of matics 2019;35:i145–53. https://doi.org/10.1093/bioinformatics/
topological chromatin domains cause pathogenic rewiring of btz362
