---
source_path: /mnt/c/Users/Administrator/Zotero/storage/VSDJSIHT/Li 等 - 2025 - scPANDA PAN-Blood Data Annotator with a 10-Million Single-Cell Atlas.pdf
ingested: 2026-04-23
sha256: fd8638c999d229e5
---

Chin Med Sci J
Research Article
2025; 40(1): 68-87
doi: 10.24920/004472
scPANDA: PAN-Blood Data Annotator with a 10-Million
Single-Cell Atlas
Chang-Xiao Li, Can Huang, Dong-Sheng Chen*
State Key Laboratory of Common Mechanism Research for Major Diseases, Suzhou Institute of Systems
Medicine, Chinese Academy of Medical Sciences & Peking Union Medical College, Suzhou 215123,
Jiangsu Province, China
ABSTRACT
Objective Recent advancements in single-cell RNA sequencing (scRNA-seq) have revolutionized the study of
cellular heterogeneity, particularly within the hematological system. However, accurately annotating cell types
remains challenging due to the complexity of immune cells. To address this challenge, we develop a PAN-blood
single-cell Data Annotator (scPANDA), which leverages a comprehensive 10-million-cell atlas to provide precise
cell type annotation.
Methods The atlas, constructed from data collected in 16 studies, incorporated rigorous quality control,
preprocessing, and integration steps to ensure a high-quality reference for annotation. scPANDA utilizes a three-
layer inference approach, progressively refining cell types from broad compartments to specific clusters. Iterative
clustering and harmonization processes were employed to maintain cell type purity throughout the analysis.
Furthermore, the performance of scPANDA was evaluated in three external datasets.
Results The atlas was structured hierarchically, consisting of 16 compartments, 54 classes, 4,460 low-level
clusters (pd_cc_cl_tfs), and 611 high-level clusters (pmid_cts). Robust performance of the tool was demonstrated
in annotating diverse immune scRNA-seq datasets, analyzing immune-tumor coexisting clusters in renal cell
carcinoma, and identifying conserved cell clusters across species.
Conclusion scPANDA exemplifies effective reference mapping with a large-scale atlas, enhancing the accuracy
and reliability of blood cell type identification.
Key words: single-cell RNA sequencing; immunology; cell type annotation; single-cell atlas;
blood cells
INTRODUCTION erogeneity that bulk sequencing methods could not re-
solve. This has significantly advanced research in hema-
Immune cells play vital roles in both physiologi-
tology and immunology. In 2022, Xie et al.[1] created de-
cal and pathological conditions in humans. Recent ad-
tailed transcriptomic maps and transcription factor pro-
vancements in single-cell technologies have enabled
files for various human blood cells, establishing a plat-
researchers to observe cellular dynamics with unparal-
form for gene expression analysis and the prediction of
leled precision, tackling the challenge of cellular het-
blood cell types and functions. These resources provide
essential references for further blood cell research. How-
Received January 18, 2025; accepted March 4, 2025; published
ever, accurately annotating single-cell sequencing re-
online March 31, 2025.
sults and identifying cell identities are crucial for analyz-
*Corresponding author Email: cds@ism.pumc.edu.cn
ing single-cell RNA sequencing (scRNA-seq) data, espe-
© The authors 2025. Published by Chinese Academy of Medical
cially when studying the complex cellular compositions
Sciences. This is an open access article distributed under the terms
of the CC BY-NC license (http://creativecommons.org/licenses/ inherent in hematology and immune systems.
by-nc/4.0). In recent years, various cell annotation methods
Vol. 40, No.1 Chinese Medical Sciences Journal 69
have emerged, which can be broadly categorized into MATERIALS AND METHODS
three types. The first uses marker-based approaches,
Data collection, quality control, and preprocessing
such as CellAssign[2], where specific genes label and
The large number of cells that constructed the sc-
classify cells, determining their cell type. The second
PANDA atlas were obtained from 16 studies (Table 1).
method involves annotating cells based on their simi-
In total, the raw data contained 11,215,872 single-cell
larity to predefined reference cells, as seen in tools
like SingleR[3]. The third category employs machine transcriptomics. The atlas types of these datasets can
be summarized into six categories: aging, COVID-19,
learning techniques for probability-based predictions,
incorporating unbiased feature selection from reduced- bacterial infection, tuberculosis infection, immune,
dimensional spaces, exemplified by supervised classifi- and tumor. Such diversity and scale of single-cell at-
cation methods like CellTypist[4]. lases across various biological contexts and diseases
While these annotation methods have proven ef- went through a series of operations (quality control,
fective, there is a lack of specialized tools for annotat- preprocessing, harmonization, and integration) to
ing cells in the hematological system. Accurately and form the scPANDA atlas.
consistently annotating immune cells remain challeng- Scanpy was deployed to perform quality control
ing due to the complexity of the blood system. For im- (QC) of the raw scRNA-seq data. Cells with only a few
mune cells, different tools may assign varying layer la- genes (<200; possibly low-quality or empty droplets)
bels, complicating the annotation process. Addition- or excessive genes (>6,000; potentially doublets)
ally, the presence of similar gene expression profiles were excluded by scanpy. pp. filter_cells to remove
among different types of immune cells further compli- stressed or dying cells, only those with <15% mito-
cates precise annotation. Therefore, there is an ur- chondrial (MT) gene content were retained via apply-
gent need for precise and specialized tools for annotat- ing scanpy.pp.calculate_qc_metrics for MT percentage
ing immune cells within the hematological system us- calculation and subsetting accordingly. Expression pro-
ing single-cell data. files of the filtered data were log-normalized by
To address this need, we developed the PAN-blood scanpy.pp.normalize_total and scanpy.pp.log1p with a
single-cell Data Annotator (scPANDA), an annotation target sum of 1e4 (all the datasets were normalized in
tool designed to infer cell types within the hematological
system using a comprehensive 10-million-cell atlas. This Table 1. Summary of the 16 datasets that con-
large-scale scRNA-seq data was curated from 16 studies structed the scPANDA atlas.
and processed using a Scanpy[5] and CellHint[6]-based PMID Atlas type
bioinformatics pipeline. The atlas summarizes fine- 37963457[20] Aging
grained layers of cell compartments and classes, as well
34782790[21] Infection (COVID-19)
as high- and low-level clusters, forming the foundation
33657410[22] Infection (COVID-19)
of the three-layer cell type annotation tool.
35216673[23] Infection (COVID-19)
scPANDA, along with the blood atlas, facilitates
33879890[24] Infection (COVID-19)
biological discoveries in various areas. Exploring the
34429372[25] Infection (COVID-19)
meta-information of cells within different clusters in
35672358[26] Infection (bacterial)
the atlas helps to gain important insights into cellular
34031617[27] Infection (tuberculosis)
differences across various physiological and pathologi-
34290408[28] Immune (tumor)
cal states. Moreover, scPANDA's effectiveness was
35618845[29] Immune (eQTL)
demonstrated through multiple use cases, including
35549406[4] Immune (cross-tissue)
validation on three external blood single-cell datasets,
35549310[30] Immune (developmental)
analysis of immune-tumor coexisting clusters in
scRNA-seq data, and identification of probably con- 34914499[31] Tumor (pan-T)
served cell clusters in mice and monkeys in relation to 37607536[32] Tumor (pan-NK)
humans. Lastly, the atlas clusters can serve as valu- 36352227[33] Tumor (neutrophil)
able references for deconvolving bulk RNA-seq data, 31675496[34] Pan-tumor PBMC
such as TCGA cancer datasets[7], to examine their cell eQTL: expression quantitative trait locus; NK: natural
type compositions. killer cell; PBMC: peripheral blood mononuclear cell.
70 Chinese Medical Sciences Journal
the same way, whether it be conducted by their au- Supplementary Table S1.
thors or us). To achieve finer partitioning of the 10 million at-
We systematically categorized the 1,030 cell las, within each cell class, Leiden clustering[8] was per-
types from the raw datasets using a bottom-up ap- formed twice by scanpy.tl.leiden, both at a resolution
proach. Initially, we grouped these into 54 cell of 1.0. The first round identified coarse-grained clus-
classes, from CD4+ T cells to unidentified types, and ters that captured large cell subpopulations, while the
subsequently consolidated these into 16 broader com- second round refined these clusters via detection of
partments, which include diverse cell types such as T subtle, more homogeneous subsets of cells in the ini-
cells, myelomonocytic cells, and progenitor cells. De- tial clusters. Those second-round clusters with less
tails of these categorizations can be found in the than 100 cells were removed to improve the reliability
supplementary Table S1. Cells marked with "un- of results, since clusters containing few cells might
known" or lacked cell type information in the original represent spurious groups due to technical artifacts
datasets were removed. The above QC and prepro- rather than biologically meaningful (sub) populations.
cessing operations resulted in 10,838,520 cells with After this refinement, the final size of the blood atlas
13,220 common genes for the subsequent bioinfor-
remains 9,841,765 cells.
matics analysis.
To further enhance cell type purity, within each
second-round Leiden cluster, we carried out cell type
Integration, partitioning, clustering, and harmo-
harmonization by deploying cellhint.harmonize on the
nization
original annotations, according to the cells' dataset ori-
To remove batch effects and integrate the filtered and
gins and top 50 PCs. Specifically, a cell-to-cell type
preprocessed multi-atlas data, the restricted neighbor-
dissimilarity matrix was created by CellHint based on
hood search-based data integration functionality of
the PCs; from the matrix, a predictive clustering tree
CellHint[6] was deployed with the 16 dataset origins as
(PCT) for each dataset (as reference) was formed to
the batch confounder and the 54 cell classes as the
predict transcriptomic dissimilarities between cell
cell type groups. Specifically, cellhint.integrate con-
types in the reference dataset and other datasets.
structed the neighborhood graph of the 10.8 million
Next, these dissimilarities were combined into a har-
cells through a restricted approach of searching neigh-
monization graph that included equivalent or divisible
bors (computed by scanpy.pp.neighbors) across
cell types, thereby formulating a CellHint harmoniza-
matched cell classes in different datasets (batches),
tion table, which summarized diverse cell types into
based on the top 50 principal components (PCs) ob-
semantically connected ones in a format like "Type1
tained by scanpy.tl.pca. These PCs were the lower rep- ∈
Type2=Type3". Cells with the same or similar seman-
resentations of the top 3,000 highly variable genes
tics were grouped together. By adopting the harmoni-
(HVGs) among the 13,220 genes, ranked by scanpy.pp.
zation process and splitting by such groups, each
highly_variable_genes.
second-round Leiden cluster could be broken down
The integrated data was directly partitioned by
the 16 predefined cell compartments to build the top- into even finer clusters with better cell type purity. In
level of the blood atlas, spanning T cells, B cells, natu- total, 4,460 clusters were attained and assigned with
ral killer cells, dendritic cells, myelomonocytic cells, names in the pd_cc_cl_tf structure.
megakaryo-erythroid cells, innate lymphoid cells, The 611 high-level clusters named in the
other immune cells, progenitor cells, fibroblasts, endo- pmid_ct structure were finally created to maintain the
thelial cells, neurons/glial cells, epithelial cells, muscle link between the atlas and the original annotations
cells, bone cells, etc. Then, each compartment was and to provide flexibility in the granularity of cluster-
further split by the corresponding cell classes to pro- ing results. We conducted majority voting on the origi-
duce the second level of the blood atlas. For example, nal annotations within each pd_cc_cl_tf cluster, and
T cells were divided into CD4+ T cells, CD8+ T cells, grouped those pd_cc_cl_tfs with the same voting as a
regulatory T cells, MAIT cells, gamma delta T cells, pmid_ct. These low and high-level clusters' naming
double negative T cells, double positive T cells, and conventions are illustrated in Fig. 1, and their com-
innate T cells. These two atlas levels have been plot- plete statistics are provided in Supplementary
ted in Fig 1, with complete statistics available in Table S2.
Vol. 40, No.1 Chinese Medical Sciences Journal 71
Figure 1. The workflow chart of building the 10-million single-cell atlas for hematological cells.
HVG: highly variable genes; PCA: principal component analysis; UMAP: uniform manifold approximation and projection.
The three-layer PAN-blood single-cell transcrip- compartment level (T cells or not) to the high-level
tomic data annotator clusters (pmid_ct) and finally to the low-level clusters
The process of cell type annotation using scPANDA (pd_cc_cl_tf), utilizing t-statistic matrices at each
and the three-layered reference-based method have layer.
been illustrated in supplementary Fig. S1. This The three-layer reference matrices (respectively
method sequentially identifies cell types from the denoted M , M , and M ) that scPANDA relies on to
1 2 3
72 Chinese Medical Sciences Journal
make inferences were generated as follows. In Layer analysis and ranking are conducted with regard to the
1 for T cell classification, the atlas comprising ~10 mil- rows of the Layer 3 (pd_cc_cl_tf) reference matrix
lion cells were divided into a T cell group (58.79%) M corresponding to the previously determined
3
and a non-T cell group (41.21%). DE analysis was per- pmid_ct. This step identifies the specific low-level clus-
formed on the top 3,000 HVGs between these two ter for each query cluster.
groups using scanpy.tl.rank_genes_groups, with the To improve the robustness of this sequential in-
default t-test method. This analysis resulted in the ference process, a reannotation mechanism is addi-
matrix of t-statistics for each HVG, M 2×3000, which tionally conducted for those inferred pd_cc_cl_tfs with
1∈ℝ
serve as the reference for cell type inference at this low correlation values. If the ith query cluster is in-
layer. In Layer 2 for pmid_ct classification, the second ferred as T cells in Layer 1 but has a Layer 3 cor-
t-statistic matrix, S 611×3000, was generated by con- ri lower than the predefined threshold γ (de-
∈ℝ pd_cc_cl_tf
ducting DE analysis of the top 3,000 HVGs between fault at 0.2, indicating a weak correlation), it will be
each of the 611 high-level clusters (pmid_ct) and the considered more likely to be non-T cells and go
remaining clusters. This reference matrix was used to through recalculation of correlation using the corre-
further classify the query clusters identified as T cells sponding non-T cell rows of M and M . This proce-
2 3
or non-T cells from Layer 1. Layer 3 for pd_cc_cl_tf dure helps combat the false positives of T cell infer-
classification involved the creation of the third t- ence.
statistic matrix, M 4460×3000, by performing DE analy- Default parameters (α=0.1, β=0, and γ=0.2)
3∈ℝ
sis on the top 3,000 HVGs between each of the 4,460 were used to perform the application of scPANDA to
low-level clusters (pd_cc_cl_tf) and the other clusters. infer cell types of the three external datasets. For the
This matrix refined the cell type classification to the cross-tissue datasets analysis, apart from the default
most specific clusters. settings, a stricter criterion (corr
T cells
≥0.1) of the
Using the three reference matrices, scPANDA de- Layer 1 inference was added to tackle the possible in-
termines the cell types of the query dataset with C terference of non-blood tissues in the query dataset.
clusters and G genes progressively. The inference pro- The cross-species datasets analysis was performed
cess begins with calculating the t-statistic matrix, M q∈ with larger thresholds (α=0.2, β=0, and γ=0.4) to
C×G, for the query dataset using scanpy. tl. rank_ deal with a possible higher rate of false positives in
ℝ
genes_groups. Pearson correlation coefficients (corr) non-human blood query datasets.
between row pairs of the query matrix M and the
q
Layer 1 (T cells or not) reference matrix M are com- Non-negative least squares-based deconvolution
1
puted. By comparing the correlation values of T cells using the atlas clusters
and non-T cells, each query cluster is classified as ei- Non-negative least squares (NNLS)[9] has been proven
ther belonging to the T cells compartment or not. By to be a fast-to-solve, top performing algorithm for cell
default, the ith query cluster is inferred as T cells only type deconvolution of bulk RNA-seq data. In this study,
if it simultaneously meets two requirements, i.e., we implemented NNLS using scipy. optimize. nnls in
corri -corri α Python, with the 4,460 pd_cc_cl_tf clusters utilized as
T cells non-T cells≥
the single-cell reference. Expression profiles of the top
corri <β
non-T cells 3,000 HVGs were averaged across all cells within each
pd_cc_cl_tf to generate a reference expression profile
Here, both comparison criteria can be changed
matrix M 4460×3000. The optimization problem for de-
(addition or deletion) by users; the numeric thresh- d∈ℝ
convolution was formulated as minimizing the squared
olds α and β with default values of 0.1 and 0, respec-
differences between the gene expression vector V
tively, can also be tuned. For clusters identified as T b∈
3000 of the bulk data and the estimated cell type com-
cells, correlation analysis and ranking are performed
ℝ
positions
between the corresponding rows in M and the T cells-
q
only rows in the Layer 2 (pmit_ct) reference matrix min V -M P
M to infer the most probable high-level cluster type P b d 2
2
in the scPANDA atlas. For non-T cell clusters, only the where P 4460 denotes the cell type proportion vector
∈ℝ
non-T cells rows of M are used. Finally, correlation to be predicted.
2
Vol. 40, No.1 Chinese Medical Sciences Journal 73
RESULTS high-level clusters, named using the structure
"pmid_ct" (e.g., PMID34914499.c06.Tm.ANXA1), rep-
The comprehensive 10 million blood single-cell
resenting the reference dataset's PMID and the origi-
atlas
nal cell type annotation. Complete statistics for
The bioinformatics workflow (Fig. 1) ensures the in-
pd_cc_cl_tf and pmid_ct clusters are provided in
clusion of high-quality and abundant cells in the blood
supplementary Table S2.
atlas, achieving computationally distinct and biologi-
cally meaningful cell compartments, classes, and clus-
Differentially expressed genes and enrichment
ters. The following criteria were considered for data in-
related to age and gender
clusion: (1) ensuring comprehensiveness and hetero-
Age
geneity by incorporating datasets covering physiologi-
By preprocessing and standardizing the age informa-
cal, aging, and disease conditions; (2) improving an-
tion, six age intervals in relation to 50.09% of cells of
notation accuracy and resolution by increasing the
the atlas were obtained. Fig. 2A illustrates the distri-
number of cells per type and state; and (3) minimiz-
bution of cell counts across various age intervals, the
ing batch effects by prioritizing large-scale datasets.
largest proportion of cells falls within the group of 40–
After quality control and preprocessing to re-
59 years, constituting 28.14%; 20–39 years follows
move low-quality and unidentified cells, the datasets
closely with 27.52%; 60 – 79 years accounts for
were concatenated to create an expression profile ma-
23.66%; the "gestational" group makes up 17.16%;
trix of 9,841,765 cells and 13,220 genes.
the smallest proportions are seen in the 80–99 years
The top 3,000 HVGs were selected for principal
and 0–19 years groups, with 2.88% and 0.66%, re-
component analysis (PCA) and cell neighbor calcula-
spectively.
tion, which were then input to CellHint, a machine
Among the 1,754 pd_cc_cl_tf clusters (39.33%
learning approach that can (1) harmonize diverse cell
of clusters in the atlas) containing the age informa-
type annotation styles in multiple datasets and (2) in-
tion, as shown in Fig. 2B, "gestational" has the high-
tegrate the datasets. Here, the latter functionality
est cluster count, comprising 36.6%; the 40–59 years
(CellHint Integration) was firstly used to remove batch
and the 20–39 years groups have comparable cluster
effects in the concatenated matrix.
counts, making up 23.09% and 21.72%, respectively;
To achieve finer partitioning, each class was clus-
the 60–79 years follows with 17.45%; the 80–99 years
tered twice using the Leiden algorithm. In each of the
has the least number of clusters at 1.14%. Notably,
resulting Leiden clusters, CellHint Harmonization was
carried out to standardize the diverse annotation there are no clusters identified in 0–19 years group.
styles across the original datasets (e.g., "CD4-Th (1)" An upset plot (Fig. 2C) further visualizes the in-
in PMID: 33657410 versus "T_CD4_c01_LEF1" in tersections between age intervals in terms of cell
PMID:34290408). This operation could possibly divide counts. The most significant intersection is seen
the Leiden cluster into multiple cell groups; further among 20–39 years, 40–59 years and 60–79 years,
segregation by such groups gave the final clustering and 80–99 years, with a size of 555. Other intersec-
outcomes, i.e., the 4,460 low-level clusters, each with tions have much smaller sizes, indicating less overlap
ensured purity of cell types. The clusters were named between these age groups. "Gestational" intersects
using the structure "pd_cc_cl_tf" (e.g., PD_T4_c0001_ with several other age groups but shows a higher
TSC22D1), representing the scPANDA project code, number of unique clusters (587) than intersections.
the cell class abbreviation, the cluster number, and Distinct sets of differentially expressed genes
the top-ranked transcription factor gene. (DEGs) and enrichment analysis results can be found
To maintain the link between the atlas and the in the two extreme age groups, "gestational" and 80–
original annotations and to provide flexibility in the 99 years, with regard to the young adulthood and
granularity of clustering results, clusters at a meaning- early middle age group (20–39 years) as the refer-
fully higher level were created in addition to these low- ence. Fig. 2D depicts the gene expression UMAPs of
level clusters. Majority voting was conducted for each the three most common DEGs (STMN1, CD38, and
"pd_cc_cl_tf" cluster, assigning the most common an- SH2D1A) in "gestational" T cell clusters, whereas Fig.
notation to the cluster. This resulted in 611 distinctive 2E conveys the visualizations of the three most com-
74 Chinese Medical Sciences Journal
Figure 2. Summary statistics, DEGs, and enrichment analysis results regarding age and gender.
(A) Distribution of cell counts across various age intervals. (B) Distribution of cell cluster counts by age intervals. (C) Intersections be-
tween age intervals in terms of cell counts. (D) Gene expression UMAPs of the three most common DEGs in "gestational" T cell clusters,
(E) DEGs in T cell clusters of age interval of [80-99]. (F) Comparison of the respective top three GO and KEGG pathway enrichments for
the 1st "gestational" T cell cluster, and the 1st [80-99] T cell cluster. (G) Cell counts and cluster counts by gender with the intersection of
clusters. (H) The UMAP visualization of cells belonging to male (blue), female (pink), and gender-neutral (purple) groups. (I) The gene ex-
pression UMAPs of the three most common DEGs in male clusters, and (J) in female clusters. (K) Comparison of DEGs and enrichments be-
tween male and female cell groups within the 1st gender-neutral T cell cluster, PD_T4_c0004_BATF3. (L) Comparison of the respective top
three GO and KEGG pathway enrichments for the 1st male and female T cell cluster. DEG: differentially-expressed Genes. UMAP: uniform
manifold approximation and projection.
Vol. 40, No.1 Chinese Medical Sciences Journal 75
mon DEGs (RPS29, RPL27A, and RPL13A) in 80–99 highlight the functional heterogeneity between gen-
years T cell clusters. Notably, those "gestational" ders (Fig. 2L). Despite that both clusters exhibit sig-
genes tend to be more differentially expressed than nificant enrichment in "response to stimulus" and
80–99 ones. "regulation of response to stimulus", more diversity
To underscore the functional heterogeneity be- exists than similarity: the former cluster has a pro-
tween age groups, Fig. 2F compares the respective nounced GO enrichment in "cellular response to stimu-
top three Gene Ontology (GO) and Kyoto Encyclopedia lus" and "cellular response to chemical stimulus", as
of Genes and Genomes (KEGG) pathway enrichments for well as KEGG pathways "apoptosis", "JAK-STAT signal-
the "gestational" T cell cluster, PD_T4_c0005_TSC22D1, ing pathway", and "pathways in cancer"; the latter
and the 80–99 years T cell cluster, PD_T4_c1081_ cluster, in contrast, shows significant enrichment in
CEBPB. While the former cluster exhibits significant "cytokine-cytokine receptor interaction", "MAPK signal-
enrichment in processes related to "cellular response ing pathway", and "FoxO signaling pathway".
to stimulus", "regulation of response to stimulus", and Gender differences can further be observed
"response to stress", as indicated by the relatively within the gender-neutral clusters. For instance, as in-
larger and darker red dots, the latter cluster is promi- dicated in Fig. 2K, via comparative analysis of male
nently enriched in the "FoxO signaling pathway", "Ri- and female cells in the 1st gender-neutral T cell clus-
bosome", and "Coronavirus disease - COVID-19" path- ter, PD_T4_c0004_BATF3, significant GO terms ("regu-
ways, as evidenced by larger dots with darker colors. lation of multicellular organismal process", "regulation
Both clusters exhibit notable enrichment in "response of immune system process", and "response to stimu-
to stimulus", whereas "MAPK signaling pathway" is lus") and KEGG pathways ("Hematopoietic cell lin-
more significantly enriched in PD_T4_c0005_TSC22D1 eage", "Rheumatoid arthritis", and "Asthma") with
compared to PD_T4_c1081_CEBPB. their corresponding DEGs sets can be identified; DEGs
and enrichment analysis results are also attained in the
Gender
1st gender-neutral non-T cell cluster, PD_Mono_c0034_
Preprocessing and standardization resulted in 5,679,895
IRF9.
cells (57.71% of the atlas) with the gender informa-
tion; they were grouped into 2,186 pd_cc_cl_tf clus- Differentially expressed genes and enrichment
ters (49.01% of clusters in the atlas). The composite related to disease statuses
plot (Fig. 2G) provides an analysis of cell counts and The atlas focuses particularly on respiratory diseases
cluster counts by gender, together with a Venn dia- and cancers. The majority of cells are associated with
gram showing the intersection of clusters between respiratory diseases (49.85%), followed by cancers
genders. In terms of cell count, males constitute for (43.81%), while normal cells constitute a much
59.71% of the cells, while females account 40.29% of smaller proportion (6.34%). Cancer clusters are the
the cells. Regarding the cluster count, males and fe- most prevalent (51.07%), outnumbering respiratory
males represent 56.95% and 43.05% of the clusters, disease clusters (46.73%) and normal clusters
respectively. (2.20%).
Fig. 2H visualizes cells belonging to male (blue), COVID-19 overwhelmingly dominates both cell
female (pink), and gender-neutral (purple) groups. and cluster percentages within respiratory diseases,
Collectively, Fig. 2I and Fig. 2J provide an inter- indicating its significant impact. Minor contributions
gender analysis of the three most common DEGs in are observed from other respiratory diseases such as
male clusters (HLA-B, B2M, and IL32) versus those in flu and respiratory system disorder (RSD).Hepatocellu-
female clusters (HSP90AA1, PTP4A1, and RPS29). The lar carcinoma (HCC) stands out prominently with the
distinct sets of DEGs imply disparities in cell and clus- highest percentage in both cell and cluster counts,
ter distributions between genders, offering a founda- highlighting its prevalence (Fig. 3A).
tion for further exploration into gender-specific cellu- Fig. 3B presents analyses of first-numbered clus-
lar characteristics. The respective top three GO and ters for the three respiratory diseases, focusing on the
KEGG pathway enrichments for the 1st male T cell top GO enrichments and the top KEGG pathway
cluster, PD_T4_c0003_NR1D1, and the 1st female T enrichments, along with the associated DEGs. Since
cell cluster, PD_T4_c0005_TSC22D1, are compared to FLU contains only non-T cell clusters, the first such
76 Chinese Medical Sciences Journal
Figure 3. Summary of statistics, DEGs, and enrichment analysis results regarding disease statuses.
(A) Comprehensive overview of cell and cluster counts across various disease statuses. (B) Analyses of first-numbered clusters for the
three respiratory diseases, focusing on the top GO enrichments and the top KEGG pathway enrichments, along with the associated DEGs.
(C) The GO and KEGG pathway enrichments with corresponding DEGs for different first-numbered clusters of acute leukemia (AL), adeno-
squamous carcinoma (ASC), and breast cancer (BC), respectively. FLU: influenza RSD: resperitory systen disorder.
cluster labeled PD_Mono_c0682_CEBPD is solely plot- larly in recognizing and responding to external biotic
ted: the primary GO enrichments are heavily oriented stimuli; the KEGG terms resonate with this through
towards immune-related processes, suggesting a sig- pathways such as "Leishmaniasis", "Phagosome", and
nificant role in the body's immune response, particu- "Influenza A", with associated genes (e.g., IFITM3,
Vol. 40, No.1 Chinese Medical Sciences Journal 77
S100A8, S100A9, TYROBP, and LGALS1) that are con- the enrichment of "Hematopoietic cell lineage" path-
sistent with an immune response role. way indicates a broader involvement in blood cell de-
In relation to the RSD T cell cluster, PD_T4_c0434_ velopment and immune cell differentiation. The
ID1, the top GO terms are related to T cell functions, unique genes in this cluster further highlight its par-
indicating a role in adaptive immunity, specifically in ticular role in responding to specific viral pathogens.
the activation and differentiation of T cells; the KEGG Fig. 3C describes the GO and KEGG pathway en-
pathways confirm T cell involvement with enrichments richments with corresponding DEGs for different first-
in "Th17 cell differentiation", "Th1 and Th2 cell differ- numbered clusters of acute leukemia (AL), adenosqua-
entiation", and "T cell receptor signaling pathway". mous carcinoma (ASC), and breast cancer (BC), respec-
The non-T cell cluster, PD_Mono_c0452_CEBPB, re- tively. Since ASC contains no T cell or monocyte clus-
sembles FLU's PD_Mono_c0682_CEBPD cluster in ters, the 1st tumor cluster (PD_Tumor_c0051_HEY1) is
terms of the top GO terms and KEGG pathways, em- plotted; and only the 1st T cell cluster (PD_T8_0078_
phasizing immune responses. Key terms include "im- NR4A3) is drawn for BC due to the lack of non-T cell
mune system process", "defense response", "osteo- clusters.
clast differentiation", and "phagosome"; the consis- The subplot for AL demonstrates its clusters' sig-
tent presence of genes like S100A8, S100A9, and nificant involvement in immune system processes,
TYROBP indicates similar functional roles between apoptosis, and pathogen response pathways. In
these two monocyte clusters in pathogen response PD_T8_c0135_TSC22D1, "immune system process"
and phagocytosis. shows the highest significance, with DEGs such as
For the COVID-19 T cell cluster, PD_T4_c0028_CEBPB CCL5, HSP90AA1, and PIK3R1. "Lymphocyte activa-
shows GO enrichments related to immune activation tion" and "leukocyte activation" are also significantly
("immune system process", "T cell activation", and enriched, involving genes such as CCL5, PIK3R1,
"lymphocyte activation"). The cluster is also enriched ZFP36L2, and JUNB. "Natural killer cell mediated cyto-
for the "coronavirus disease—COVID-19" pathway, toxicity" and "antigen processing and presentation" in-
emphasizing its relevance in the context of the COVID- dicate a strong immune-related functional involve-
19 pandemic. The presence of genes like S100A8, ment, with genes like PIK3R1, IFNG, and HSPA1A.
S100A9, and TYROBP suggests involvement in both "Apoptosis" is another significant process, with genes
general immune responses and specific responses to including PIK3R1, JUN, and MCL1. In PD_Mono-
viral infections. The non-T cell cluster, PD_Mono_c0003_ like_c0014_TRPS1, notable enrichments include "im-
CEBPD, shares similar GO terms and KEGG pathways mune system process" (CCL5, RPS29, and MT-ATP6)
with the other monocyte clusters, such as "immune and "response to external stimulus and immune re-
system process", "defense response", "Osteoclast dif- sponse" (CCL5, HSP90AA1, and DNAJA1). In addition,
ferentiation", and "Phagosome", implying a consistent leishmaniasis, tuberculosis, and hematopoietic cell lin-
role across different monocyte clusters in immune re- eage pathways suggest specific pathogen responses
sponses and pathogen interaction, with genes (e.g., and cell lineage differentiation, with genes such as MT-
LYZ, TYROBP, and S100A9) common to these pro- ND1, IRF1, and TGFB1.
cesses. The ASC cluster, PD_Tumor_c0051_HEY1, is sig-
Despite similarities in immune system involve- nificantly involved in developmental processes, struc-
ment, pathogen response and several common genes tural development, response to stimuli, and critical
among the monocyte clusters of the three respiratory signaling pathways. Specifically, the GO term "ana-
diseases, stark differences lie in the T cell clusters of tomical structure development" exhibits the highest
RSD and COVID-19. PD_T4_c0434_ID1 focuses more enrichment significance, with DEGs such as KRT5,
on general T cell functions, including activation, differ- SFN, ANXA2, HSPB1, and PERP, suggesting a critical
entiation, and signaling pathways related to T cell re- role in the formation and maintenance of anatomical
ceptor and Th1/Th2 differentiation. On the other features in the tumor context. "Developmental pro-
hand, PD_T4_c0028_CEBPB shows a distinct enrich- cess" and "tissue development" (with common DEGs
ment for pathways related to specific immune such as KRT5, ANXA2, and SPINT2) underscore the
responses ("coronavirus disease - COVID-19"), sug- importance of cellular growth and differentiation pro-
gesting a specialized role in viral infections. Moreover, cesses in ASC. "Multicellular organism development"
78 Chinese Medical Sciences Journal
and "anatomical structure morphogenesis" (KRT5, To sum up, while the clusters of all three cancers
ANXA2, and TACSTD2) indicate the complex develop- show a moderate degree of overlap in immune re-
mental mechanisms at play in tumor progression and sponse pathways, the AL and BC clusters tend to be
morphology. "Response to stimulus" (KRT5, S100A11, more heavily centered on immune system processes
and HSPB1) stresses on the tumor cells' ability to re- and specific immune cell activations. In contrast, the
spond to various environmental and physiological ASC cluster emphasizes developmental and structural
stimuli. In terms of KEGG pathway enrichment, "pro- pathways, reflecting the distinct cellular mechanisms
teoglycans in cancer" and "focal adhesion" (SDC1, underlying each type of cancer.
SDC4, and COL1A1) are vital for cancer metastasis
and growth. "ECM-receptor interaction" and "HIF-1 Automatic cell type annotation using scPANDA
signaling pathway" (SDC1, COL1A1, and GAPDH) influ- on three external datasets
ence tumor survival and proliferation. "PI3K-Akt sig- The application of scPANDA to infer low-level cell clus-
naling pathway" and "fluid shear stress and athero- ters was demonstrated in a query dataset (PMID:
sclerosis" (COL1A1, ITGB4, and TXN) indicate signal- 32561858)[10] that originally contains general, mixed
ing mechanisms that affect cell survival, growth, and types for 12,738 cells with 25,660 genes (Fig. 4A).
response to mechanical forces, which are relevant in Distinct clusters visualized in the UMAP plot indicate
the tumor microenvironment. separation of different cell types based on their gene
The breast cancer T cell cluster, PD_T8_ expression profiles, and the table links the original
0078_NR4A3, closely correlates with immune sys-
general cell types with the inferred low-level clusters
tem processes, T cell activation, and various differ-
(pd_cc_cl_tf) as determined by scPANDA. Apparently,
entiation pathways. The GO term "Response to
each original cell type can be appropriately matched
stimulus" (CD8A, ZFP36L2, CCL5, SRGN, and CD7)
with a corresponding low-level cluster. For example:
exhibits the highest enrichment significance, reflect-
B cell inferred as PD_B_c0093_IRF9, Cancer as
ing a critical role in the cellular response to various
PD_Tumor_ c0007_EGR4, epithelial as PD_Epi_c0025_
environmental and physiological stimuli in the con-
RFX3, fibroblast as PD_Fib_c0025_NRID1, and T cell
text of BC. "Immune system process" and "T cell ac-
as PD_T8_ c0301_ID1.
tivation" (CD8A, PIK3R1, CCL5, CD8B, and IL2RG)
Fig. 4B illustrates the use of scPANDA to infer
highlight the importance of immune system activity
low-level cell clusters in a detailed, mixed cell-typed
and T cell-mediated responses in BC. "Cellular re-
query dataset (PMID: 35389779) [11] consisting of
sponse to stimulus" and "lymphocyte activation"
1,248,980 cells and 36,469 genes. Although the UMAP
(CD8A, ZFP36L2, and TNFAIP3) imply the complex
plot conveys a more complex landscape of cellular di-
interactions and activation mechanisms of immune
versity, the inferred low-level clusters can still match
cells in the tumor microenvironment. "Immune re-
the original ones.
sponse" (CD8A, CD8B, HLA-B, and HSPA8) reveals
Unlike the previous two applications that ad-
the broad immune reactions to BC's behavior and
dressed general and detailed mixed cell types respec-
progression. In terms of KEGG terms, "Th17 cell dif-
tively, Fig. 4C focuses exclusively on T cells, where
ferentiation" and "Th1 and Th2 cell differentiation"
98,068 cells with 33,105 genes in the query dataset
(IL2RG, TGFB1, JUN, RORA, and GATA3) are crucial
(PMID: 38213787)[12] are grouped into diverse T cell
for the differentiation and function of helper T cells,
subtypes. Clear mappings can be observed between
which play key roles in immune responses against
cancer. "T cell receptor signaling pathway" (CD8A, the original and the inferred types.
PIK3R1, and CD247) is essential for T cell activation Overall, the above three applications showcase
and signaling, influencing the immune response to the accuracy, flexibility, and robustness of scPANDA in
cancer cells. "Apoptosis", "osteoclast differentia- handling query datasets with diverse focal points,
tion", and "cytokine-cytokine receptor interaction" whether it be varying granularities of cellular differen-
(MCL1, JUN, and CCL5) concern with programmed tiation or concentrated analysis of a single compart-
cell death, bone resorption, and immune signaling, ment. The tool can advance scRNA-seq data analysis
respectively, corresponding to diverse mechanisms by revealing detailed cellular identities within complex
in the tumor microenvironment. datasets.
Vol. 40, No.1 Chinese Medical Sciences Journal 79
Figure 4. The comparative evaluation of scPANDA and CellTypist on three external blood single-cell datasets.
(A) Application of scPANDA and CellTypist to infer low-level cell clusters in a general, mixed cell-typed query dataset (PMID: 32561858).
(B) Application of scPANDA and CellTypist to infer low-level cell clusters in a detailed, mixed cell-typed query dataset (PMID: 35389779).
(C) Application of scPANDA and CellTypist to infer low-level cell clusters in a T cell type-only query dataset (PMID: 38213787).
80 Chinese Medical Sciences Journal
Analysis of immune-tumor coexisting clusters in 38177281)[15]. The cell clusters' original types identi-
renal cell carcinoma fied in this mouse dataset are listed in Fig. 6C, along
scPANDA can be further extended to annotation of with their corresponding pd_cc_cl_tfs inferred by sc-
multi-tissue datasets (not only blood). Take the renal PANDA as well as the correlation scores that reflect
cell carcinoma (RCC) dataset (PMID: 36423636)[13] as the confidence of inference.
an example, the mixed cell types of 270,855 cells from Identification is achieved by mapping these origi-
12 patients with kidney tumors, based on 19,477 nal mouse cell types to their human equivalents. B
genes' expression profiles( Fig. 5A). Nine clusters cells is inferred as PD_B_c0102_BCL11B at a high
contain cells from both blood and kidney tissues, as score of 0.592128, indicating a highly likely conserva-
listed in Fig. 5B. scPANDA maps these original blood- tion; Dendritic cells is annotated as PD_DC_c0043_
tumor co-existing clusters to their inferred low-level SPIB at a lower score of 0.243233, implying a moder-
clusters (pd_cc_cl_tf): effector memory CD4-positive, ate conservation likelihood. Other likely conserved
alpha-beta T cell annotated as PD_T4_c1035_LYL1, clusters include: T cells as PD_T8_c0949_BACH2
naive thymus-derived CD8-positive, alpha-beta T cell (0.467695), Neutrophils as PD_Neu_c0030_TRPS1
as PD_T8_c0034_BACH2, gamma-delta T cell as (0.459682), Monocytes as PD_Mono_c0085_SPIB
PD_Tgd_c0001_JUN, mucosal invariant T cell as (0.312561). In contrast, Urothelial cells may not be con-
PD_MAIT_c0016_TSC22D1, natural killer cell as served due to the unmatched inference PD_Platelet_
PD_NK_c0024_ID1, innate lymphoid cell as PD_NK_c0037_ c0011_BACH2.
BATF3, plasmacytoid dendritic cell as PD_DC_c0058_ Fig. 6E further explores the top GO and KEGG
SPIB, plasma cell as PD_B_c0121_E2F3, and non- terms with associated DEGs for the five likely con-
classical monocyte as PD_Mono_c0473_BATF3. Such served clusters between mice and humans. Each clus-
a precise correspondence proves scPANDA's versatility ter is associated with specific processes and path-
in handling scRNA-seq data with varying tissue origins. ways, from adaptive immune responses to innate de-
Fig. 5C presents the enrichment analysis results fense mechanisms. PD_B_c0102_BCL11B is primarily
and the associated DEGs for the nine blood-tumor co- involved in immune activation, particularly B cell acti-
existing pd_cc_cl_tfs inferred above. The left subplot vation and leukocyte functions, suggesting its role in
focuses on the four T cell clusters, .and the right sub- adaptive immunity and response to infections and dis-
plot displays the five non-T cell clusters. Overall, the eases like asthma. PD_T8_c0049_BACH2 is related to
capability of scPANDA to identify and annotate de- T cell functions, including activation, differentiation,
tailed functional characteristics of both T cell and non- and signaling pathways crucial for immune responses
T cell clusters, each with valuable roles in immune re- and cancer-related processes. PD_Neu_c0030_TRPS1
sponse and cellular processes within a mixed tissue concerns with immune defense mechanisms, including
context was demonstrated. responses to stimuli and pathogens like tuberculosis
and leishmaniasis. PD_Mono_c0085_SPIB also focuses
Identification of probably conserved clusters in on innate immune responses and defense against
mice and monkeys in relation to humans pathogens, emphasizing its role in monocyte-
scPANDA, developed based on human blood scRNA- mediated immune functions. PD_DC_c0043_SPIB per-
seq data, can also be deployed to annotate cross- forms dendritic cell functions and immune system
species cell types for identification of likely preserved regulation is associated with antigen processing and
cell clusters between humans and other species such presentation, critical for adaptive immunity, and re-
as mice (Mus musculus) and monkeys (Macaca fas- sponses to external stimuli.
cicularis). The following inferences were made based
Monkeys
on the analysis of homologous genes in mice and mon-
Fig. 6B shows the clustering of 18,353 peripheral
keys, as compared to humans, using Ensembl[14].
blood cells with 13,416 genes, obtained from 13 young
Mice crab-eating monkey samples in the literature (PMID:
Fig. 6A visualizes the clustering of 17,652 peripheral 35418686)[16]. The cell clusters' original types identi-
blood cells with 16,623 genes, obtained from four fied in this monkey dataset are listed in Fig. 6D, to-
young male mouse samples in the literature (PMID: gether with their corresponding inferred pd_cc_cl_tfs
Vol. 40, No.1 Chinese Medical Sciences Journal 81
Figure 5. scPANDA's low-level cluster inference, DEGs, and enrichment analysis results of blood-tumor coexisting clusters.
(A) The UMAP visualization of the mixed cell-typed kidney cancer dataset (PMID: 36423636) of 270,855 cells from 12 patients with kidney
tumors, based on 19,477 genes' expression profiles. (B) The nine blood-tumor co-existing clusters and their corresponding inferred low-
level clusters. (C) The enrichment analysis results and the associated DEGs for the nine blood-tumor co-existing pd_cc_cl_tfs inferred.
and the correlation scores. A3 (0.338358). Besides, the three unmatched clusters
Five cell clusters can be matched at moderate-to- (NKT cell, CD4 T cell, and CD8 T cell) have relatively
high correlation scores: NK cell and PD_NK_c0025_ high scores, implicating a certain degree of similarity
PLEK (0.571083), B cell and PD_B_c0026_SPIB between monkeys and humans' T cells despite un-
(0.531479), Monocyte and PD_Mono_c0821_NR1D1 likely conservation.
(0.454454), Plasma B cell and PD_B_c0121_E2F3 Fig. 6F depicts the top GO and KEGG terms with
(0.422939), and Erythrocyte and PD_ERY_c0029_NR4 associated DEGs for the five likely conserved clusters
82 Chinese Medical Sciences Journal
Figure 6. Probably conserved clusters in mice and monkeys in relation to humans, identified by scPANDA.
(A) The clustering of 17,652 peripheral blood cells with 16,623 genes, obtained from four young male mouse samples in the literature (PMID:
38177281). (B) The clustering of 18,353 peripheral blood cells with 13,416 genes, obtained from 13 young crab-eating monkey samples
(PMID: 35418686). (C) The cell clusters' original types identified in the mouse dataset and (D) in the monkey dataset, along with their corre-
sponding pd_cc_cl_tfs inferred by scPANDA as well as the correlation scores that reflect the confidence of inference. (E) The top GO and
KEGG terms with associated DEGs for the five likely conserved clusters between mice and humans, and (F) between monkey and humans.
between monkeys and humans. Processes and path- PD_NK_c0025_PLEK is enriched in innate immune re-
ways regarding diverse aspects of the immune system sponses such as natural killer cell functions and immune
and cellular functions can be observed in each cluster. activation, with an additional role in antigen processing
