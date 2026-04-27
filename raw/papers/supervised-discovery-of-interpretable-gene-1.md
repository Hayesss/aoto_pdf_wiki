---
source_path: /mnt/c/Users/Administrator/Zotero/storage/GDM9CDEZ/s41587-023-01940-3.pdf
ingested: 2026-04-23
sha256: 3aa0d054aacfeeed
---

nature biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
Supervised discovery of interpretable gene
programs from single-cell data
Received: 21 December 2022 Russell Z. Kunes1,2,7, Thomas Walle 1,3,4,5,7, Max Land 1, Tal Nawy 1 &
Dana Pe’er 1,6
Accepted: 9 August 2023
Published online: xx xx xxxx
Factor analysis decomposes single-cell gene expression data into a minimal
Check for updates
set of gene programs that correspond to processes executed by cells in
a sample. However, matrix factorization methods are prone to technical
artifacts and poor factor interpretability. We address these concerns with
Spectra, an algorithm that combines user-provided gene programs with
the detection of novel programs that together best explain expression
covariation. Spectra incorporates existing gene sets and cell-type labels as
prior biological information, explicitly models cell type and represents input
gene sets as a gene–gene knowledge graph using a penalty function to guide
factorization toward the input graph. We show that Spectra outperforms
existing approaches in challenging tumor immune contexts, as it finds
factors that change under immune checkpoint therapy, disentangles the
highly correlated features of CD8+ T cell tumor reactivity and exhaustion,
finds a program that explains continuous macrophage state changes under
therapy and identifies cell-type-specific immune metabolic programs.
A key challenge in the interpretation of single-cell RNA-sequencing representing the degree to which a cell activates each gene program)
(scRNA-seq) data is to retrieve coherent interpretable gene programs rather than a noisy vector of all observed genes or a single label denot-
representing cellular processes and to quantify them in response to per- ing cell type. Yet, there are many ways to decompose a matrix, and
turbation. Gene programs are sets of genes defined by common tasks, unsupervised approaches, such as principal component analysis and
such as metabolic pathways or responses to inflammatory cues. Gene non-negative matrix factorization (NMF), produce factors that are
set scoring (for example, scanpy score_genes1,2) is a simple and widely often difficult to interpret or are driven by technical artifacts, such
used approach to query which known gene programs are active in which as batch effects, ambient RNA or gene expression scale differences4,5.
cells, but it is often confounded by gene set overlap and technical fac- Supervised approaches use known gene sets to make detected factors
tors. The regulation of gene programs tends to be shared across cell more interpretable6,7, but preexisting gene sets are typically defined
subpopulations, creating collinearity in gene expression and imbuing in different biological contexts than those under study. In addition,
high-dimensional cell-by-gene count matrices with low-dimensional cell-type factors tend to prevail in factor analysis because expression
structure. Matrix factorization can mine this structure to identify can- differences between cells are dominated by cell type5. The popular
didate gene programs3,4 and is a core tool in single-cell analysis; for practice of partitioning data by cell type and factoring each subset
example, factorization by principal component analysis appears in separately mitigates this issue but makes it impossible to find shared
most analysis pipelines. programs.
In principle, the power of factorization lies in summarizing bio- We developed Spectra (supervised pathway deconvolution of
logical activity as a set of cellular building blocks (a minimal vector interpretable gene programs) to provide meaningful annotations of
1Computational and Systems Biology Program, Sloan Kettering Institute, Memorial Sloan Kettering Cancer Center, New York, NY, USA. 2Department
of Statistics, Columbia University, New York, NY, USA. 3Clinical Cooperation Unit Virotherapy, German Cancer Research Center (DKFZ), Heidelberg,
Germany. 4Department of Medical Oncology, National Center for Tumor Diseases, Heidelberg University Hospital, Heidelberg, Germany. 5German Cancer
Consortium (DKTK), Heidelberg, Germany. 6Howard Hughes Medical Institute, Chevy Chase, MD, USA. 7These authors contributed equally:
Russell Z. Kunes, Thomas Walle. e-mail: peerd@mskcc.org
Nature Biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
cell function by balancing prior knowledge with data-driven discovery removing edges in the input graph. The algorithm incorporates back-
(https://github.com/dpeerlab/spectra). Spectra incorporates existing ground edge and non-edge rates (provided as input parameters or
gene sets and cell-type labels as prior information, explicitly models learned from the data) to determine edge addition and removal rates.
cell type and represents input gene sets as a gene–gene knowledge Critically, Spectra can detach factors from graph penalization to learn
graph using a penalty function to guide factorization toward the input entirely new factors. In effect, Spectra attempts to explain as many of
graph. The graph representation enables data-driven modification of the input gene counts as possible by adapting the input gene graph
the input to reflect biological context and the identification of novel (providing highly interpretable factors) and uses the residual unex-
gene programs from residual unexplained variation. The degree of plained counts to identify non-penalized factors that can capture
reliance on prior knowledge can be tuned with a global parameter. entirely novel biology.
The minimization of cell-type influence allows Spectra to identify
factors that are shared across cell types. We show that Spectra outper- Spectra factors predict ground truth signaling perturbations
forms existing approaches and solves longstanding challenges in tumor We first curated a general resource of 231 immunological cell-type and
immune contexts, including the identification of an interpretable cellular process gene sets that can be input into Spectra for analyzing
tumor reactivity factor in CD8+ T cells and a new invasion program in any immune-related dataset (Fig. 1b, Supplementary Table 1 and Meth-
macrophages, which associate with response and resistance to can- ods). To maximize how many processes can be dissected and to avoid
cer immunotherapy, respectively. Our open-source software scales size-driven effects, our cellular process gene sets have comparable
to large atlases and overcomes batch effects to find factors that are size (median of 20 genes per set) and relatively little overlap (median
stable across cohorts and even tumor types and are robust enough to of 40% pairwise overlap).
be associated with clinical variables. We used our immunology knowledge base to infer gene programs
in a ground truth scRNA-seq dataset8 from human peripheral blood
Results mononuclear cells (PBMCs) stimulated in vitro with interferon-γ (IFNγ),
Spectra identifies interpretable gene programs lipopolysaccharide (LPS) or phorbol myristate acetate (PMA), a protein
We assume that each cell executes a small number of gene programs kinase C activator used to mimic TCR activation (Fig. 1c). We ran Spectra in
and that its observed expression is determined by the sum of its active addition to expiMap9 and Slalom6 (factorization methods that also incor-
programs. Spectra decomposes the cell-by-gene expression matrix porate prior gene sets) and tested the association of factor cell scores
into a cell-by-factor matrix that identifies and quantifies the programs with their corresponding perturbations. Only Spectra identified gene
executed by each cell and a factor-by-gene matrix representing the programs associated with all three perturbations in the correct condition
genes in each program (Fig. 1a and Methods). As input, the algorithm and cell type (Fig. 1d), substantially outperforming Slalom and expiMap.
receives a normalized cell-by-gene count matrix, a cell-type annotation
for each cell and either a list of gene sets or gene–gene relationships Spectra identifies robust factors in immuno-oncology data
in the form of knowledge graphs. As output, Spectra provides a set of We next applied Spectra to scRNA-seq data from the challenging
normalized global and cell-type-specific factor matrices that represent context of individuals with non-metastatic breast cancer before and
the gene loadings for each identified factor (gene scores), a sparse after pembrolizumab (anti-PD-1) treatment (‘Bassez dataset’; Fig. 2a)10.
matrix of normalized factor loadings for each cell (cell scores) and The original study used clustering and gene set analysis to identify
a modified gene knowledge graph that represents factors inferred therapy-induced changes and used TCR sequencing to define the clonal
from the data (see Methods for a technical description of Spectra and T cell expansion status of each participant treated with anti-PD-1 as a
parameter settings). surrogate for immune checkpoint therapy (ICT) response10.
Two key features distinguish Spectra from other factorization We annotated 14 broad cell types (including CD8+ T cells and
methods, enabling it to identify more interpretable factors and dis- macrophages), leaving Spectra to infer factors associated with finer
cover new biology. First, Spectra uses known cell-type information and cell-type distinctions, such as T cell activation or macrophage polariza-
allows for cell-type-specific factors. Second, Spectra represents exist- tion (Fig. 2b, Extended Data Fig. 1, Supplementary Table 2 and Meth-
ing gene sets as an input gene–gene knowledge graph, enabling their ods). Fitting the Spectra model with default parameters (Methods) and
data-driven modification and the derivation of entirely new factors. our cell-type labels and immunology knowledge base as input resulted
Cell-type labels are provided as input to Spectra, which models the in 152 global and 45 cell-type-specific factors, the latter including CD4+
influence of a factor on gene expression relative to baseline expression T cells (n = 12), CD8+ T cells (n = 7) and myeloid cells (n = 6).
per cell type, thereby mitigating its influence on the factors. The ability We determined overlap with known gene sets to assess whether
to incorporate cell-type-specific factors guides inference. For example, Spectra can identify biologically interpretable programs. For every
the T cell antigen receptor (TCR) activation program should be limited factor, Spectra estimates a dependence parameter (η) that quantifies
to T cells, but many of its genes are activated by additional programs in reliance on the gene–gene graph. Most factors (171) are strongly con-
other cell types, which confuses traditional factor analysis. strained by the graph (η ≥ 0.25), whereas 26 are novel (Extended Data
Spectra attempts to balance prior knowledge and interpretability Fig. 2). We found that factors with η ≥ 0.25 generally share over 50% of
with faithfulness to the data. Its likelihood function ensures that the their genes with an input gene set, whereas the unbiased factorization
reconstituted matrix closely matches the input matrix, and its penalty approaches NMF and scHPF4,5 produce factors that do not agree with
function guides gene factorization toward the gene–gene knowledge annotated gene sets (Fig. 2c), underscoring the difficulty of interpret-
graph (Methods). To capture prior knowledge, we use binary gene– ing programs derived by these approaches.
gene relationships and encourage these gene pairs to share similar Spectra uses cell-type labels and cell-type-specific input gene sets
factors. Spectra takes input gene sets and turns each into a fully con- to restrict factors to their appropriate cell type, ensuring more biologi-
nected clique in the input graph, indicating their relationships. Factors cally sensible factor loadings; for example, Spectra limits CD8-specific
are thus scored by how well they match the data and how many edges TCR signaling, tumor reactivity and exhaustion factors to CD8+ T cells
in the gene–gene graph support them. (Extended Data Fig. 3). By contrast, the gene set-based factorization
Most gene sets are derived from multiple biological contexts, method Slalom6 and autoencoder-based method expiMap9 misassign
which differ from the context under study. Spectra can take a com- some TCR activity, CD8+ T cell exhaustion and tumor reactivity to the
pilation of gene sets and determine the subset supported by the myeloid, natural killer (NK) cell and plasma cell lineages (Extended
data. Encoding prior knowledge as a graph facilitates computational Data Fig. 3a), likely because many genes in these factors participate
efficiency and allows Spectra to adapt gene programs by adding or in multiple programs.
Nature Biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
Input Model fitting Output
Reconstructed count matrix Cell scores Gene scores
Reliance on
input gene sets λ
Input gene sets Modified gene–gene graphs
Global Cell-type-specific
Pleiotropy similarly confounds score_genes1,2. For example, Spec- almost exclusively in the myeloid population (Fig. 2d). This myeloid bias
tra’s IFNγ response factor is well correlated with the gene encoding the is due to differences in baseline expression across cell types, especially
IFNγ receptor upstream of this gene program and correctly captures it higher expression of genes encoding major histocompatibility complex
across all cell types, whereas the score_genes IFNγ response is detected class II (MHC class II) molecules by myeloid antigen-presenting cells
Nature Biotechnology
slleC
Factors
srotcaF
Matrix factorization
Global
= Cell type A
Cell type B
Cell type C
Genes Genes
slleC
Gene expression data
Genes
slleC
Gene program expression
Cell types Input count matrix (cell score)
Cell score
Factor loading per cell Factor distribution
Modified marker gene lists
New gene
Omitted gene
Global Cell-type-specific
sllec
.oN
a
Input gene–gene graphs
b d
Immunology
knowledge base
Hemostasis/coagulation 0.0016
Cellular stress Proliferation/cell cycle 0.0014
Cellular identity Homeostasis 0.0012
Signaling 0.0010 0.0008
Immune cellular 0.0006 response
0.0004
Cell death/ 0.0002
autophagy 0
Immune function
Metabolism
n = 231 gene sets
c
PBMCs
B T/ILC M
Unperturbed Perturbed
Unperturbed Perturbed
erocs
llec
naeM
IFNγ response factor 101
IFNγ response factor
erocs
llec
naeM
B T/ILC M
B T/ILC M
erocs
llec
naeM
IFNγ perturbation
TCR activation factor 180
0.0005
0.0004
0.0003
0.0002
0.0001
0
TCR activation factor
0.25
0
–0.25
–0.50
–0.75
–1.00
–1.25
IFNγ response factor 5
2.5 2.0
1.5 1.0
0.5
0
–0.5
–1.0
erocs
llec
naeM
B T/ILC M
B T/ILC M
erocs
llec
naeM
1.25
1.00 0.75
0.50 0.25
0
–0.25
–0.50
–0.75
B T/ILC M
erocs
llec
naeM
TCR perturbation
0.012
0.010
0.008
Spectra 0.006
0.004
0.002
0
2.5
2.0
1.5
expiMap 1.0
0.5
0
–0.5
–1.0
TCR activation factor 12
Slalom
erocs
llec
naeM
LPS response factor 170
LPS response factor
0.2
0.1
0
–0.1
erocs
llec
naeM
B T/ILC M
B T/ILC M
0
–0.2
–0.4
–0.6
–0.8
–1.0
erocs
llec
naeM
LPS perturbation
LPS response factor 10
B T/ILC M
slleC
Fig. 1 | Spectra uses gene sets and cell types to guide gene program discovery base. c, Design of the perturbation experiments from Kartha et al.8. PBMCs
from scRNA-seq data. a, As input, Spectra receives a gene expression count (n = 23,754) from healthy human donors (n = 3) were incubated for 6 h with LPS,
matrix with cell-type labels for each cell as well as predefined gene sets, which it PMA or recombinant human IFNγ. d, Ability of different algorithms to identify
converts to a gene–gene graph. The algorithm fits a factor analysis model using gene programs associated with biological perturbations in the PBMC dataset.
a loss function that optimizes reconstruction of the count matrix and guides For select factors, mean per-donor cell scores are provided for T cells or innate
factors to support the input gene–gene graph. As output, Spectra provides lymphoid cells (T/ILCs), B cells (B) and myeloid cells (M; n = 3 donors). Boxes
factor loadings (cell scores) and gene programs corresponding to cell types and and lines represent interquartile range (IQR) and median, respectively; whiskers
cellular processes (factors). b, Gene set categories in the immunology knowledge represent 1.5× IQR.
Article https://doi.org/10.1038/s41587-023-01940-3
(Extended Data Fig. 4). Spectra overcomes pleiotropy by implicitly down- coexpressed in the same cells. We applied factor analysis with held-out
weighting the influence of genes whose expression could be explained cells and evaluated the coherence of inferred factors in the test set
by multiple factors. Specifically, Spectra decomposes gene expression (Methods). Spectra and other methods that take the sparsity of
using the factors best supported by total expression in a given cell. Spec- scRNA-seq data into account (Slalom and scHPF) perform well, whereas
tra is able to identify IFNγ activity and its previously reported activation generic models (NMF) do not (Fig. 2f). The key advantage of supervised
by ICT11,12 across expected immune cell types13 (Extended Data Fig. 4b) approaches is that by seeding inference with a known gene set, coher-
because it learns these factors in a cell-type-specific manner. ent genes are more likely to be biologically meaningful (Extended
Thus, in addition to yielding more interpretable gene programs Data Fig. 5b,c).
than other supervised methods, Spectra is better at inferring which Unlike other methods, Spectra’s use of prior knowledge enabled
cells these programs are active in. it to separate highly correlated factors in simulated data generated
by a generic factor analysis model with both correlated and uncorre-
Spectra outperforms other methods on gene program lated factors (Methods and Extended Data Fig. 5d). Estimating factor
benchmarks loadings in these data is particularly challenging because pleiotropy
We systematically benchmarked Spectra against other methods by creates correlation between gene programs (Methods). As gene set
measuring how well they identify coherent gene programs and assign overlap increases, score_genes1,2 surges in false-positive score esti-
activity to cells. A key feature of Spectra is that it can modify input mates, whereas Spectra correctly assigns expressed factors to cells
gene sets in a data-driven manner. We held out 30% of genes from 20 (Extended Data Fig. 5e). Due to their multivariate nature and encour-
input gene sets and tracked their identification in the resulting factors agement of sparsity, factorization methods select the factors that best
(Methods). Spectra factors recover many more genes than Slalom6 explain the data globally, such that each factor accounts for expression
(Fig. 2e) and expiMap9 (Extended Data Fig. 5a–c). For example, among not already explained by other factors. Factor analysis is thus superior
the 50 genes with the highest gene scores for the MYC factor, Spectra to score_genes even for the simple task of scoring gene sets.
identified 7 of 33 held-out genes; moreover, it recovered additional MYC In contrast to Spectra, Slalom’s accuracy drops substantially as the
target genes DKC1 (ref. 14) and TOMM40 (ref. 15), which are absent from number of active gene sets increases (Extended Data Fig. 5f). Moreover,
the training and hold-out sets, whereas MYC signaling was not captured Slalom can only assess a few dozen gene sets before run time becomes
by Slalom (Fig. 2e, Extended Data Fig. 5a and Methods). prohibitive, whereas Spectra scales to hundreds of thousands of cells
To evaluate new gene detection, we reasoned that genes belong- and hundreds of gene programs. When run on a graphics processing
ing to a program should exhibit coherence; that is, they should be unit (GPU), Spectra outperforms all methods, including NMF and the
Nature Biotechnology
noitcarf
derevoceR
e f
Reconstruction Coherence
0.8 1.0
0.7
0.8 0.6
0.5 0.6 0.4
0.4 0.3
0.2 0.2
0.1 S 0 pectra Slalom S 0 pectra sc HPF Slalo m N MF
ecnerehoC
Map expi
)nim(
emit
nuR
g
Run time
103
102 Spectra (GPU) 101 Spectra (CPU)
expiMap (GPU)
100 Slalom
net-NMF 10–1 scHPF 103 104 105 101 102 No. cells No. gene sets
)nim(
emit
nuR
a b c
Bassez dataset Breast tumor-infiltrating leukocytes Factor interpretability
Breast cancer cohort
Plasma Myeloid
GC B CD8 T
Memory B DC
Chemo- Mast Naive B ILC3 CD4 T Mac therapy NK Plasma T pDC Biopsy 1 reg
γδT
Pembrolizumab D B D i a a o y y p s 0 s 7 y – 2 15 B T/ILC Mast Spectra expi Map scHPF
Cell number Gene set number
tneiciffeoc
palrevo
mumixaM
tes
eneg
tupni htiw
d
IFN response and receptor
1.0
0.8
0.6
0.4 0.2
Slalo m N MF
Gene sets No gene
sets
esnopser
γNFI
erocs
)01 rotcaf(
Spectra
0.012
0.010
0.008
0.006 0.004
0.002 Pearson r = 0.69 0
0 0.5 1.0 1.5
IFNGR1 expression
erocs
esnopser
γNFI
0
Score genes
250 Macrophage
103 200 Other
102 150
100 101
50
100 0
10–1 –50 Pearson r = 0.59 –100 NMF 0 0.5 1.0 1.50 IFNGR1 expression
Fig. 2 | Evaluation of Spectra performance on simulated data and an immuno- (t = 3) IFNGR1 expression for each cell colored by cell type (n = 97,863 cells); IFN,
oncology dataset. a, Treatment and scRNA-seq sampling regimen of individuals interferon. e, Proportion of held-out genes recovered by Spectra or Slalom from
with breast cancer in the Bassez dataset10. b, t-Distributed stochastic neighbor the Bassez dataset for each input gene set tested. Lines connect identical input
embedding (t-SNE) of tumor-infiltrating leukocytes (n = 97,863 cells) from the gene sets. f, Coherence (mean pairwise log-normalized co-occurrence rate among
Bassez dataset colored by cell type; B, B cell; DC, dendritic cell; γδT, γδ T cell; GC, the top 50 markers) of factors generated by various factor analysis methods using
germinal center; ILC3, type 3 innate lymphoid cell; Mac, macrophage; Mast, mast a random sample of 10,000 cells from the Bassez dataset with 14 cell types and 20
cell; NK, natural killer cell; pDC, plasmacytoid dendritic cell; Plasma, plasma input genes sets (Slalom) or 181 input gene sets (other methods). The experiment
cell; T, T cell; T , regulatory T cell. c, Maximum overlap coefficient of every was repeated n = 5 times. Boxes and lines represent IQR and median, respectively;
reg
global factor generated by Spectra (n = 152 global factors), expiMap9 (n = 155 whiskers represent 1.5× IQR. g, Run time dependence on cell number with 35 gene
factors, soft_mask = True), Slalom6 (n = 20 factors), NMF (n = 100 factors) and sets (left) and gene set number with 25,000 cells (right). The experiment was
scHPF4 (n = 100 factors) with every input gene set. Boxes and lines represent performed using one cell type with the methods in b and netNMFsc (net-NMF)7
IQR and median, respectively; whiskers represent 1.5× IQR range. d, Cell scores and was repeated n = 3 times; shading indicates 95% confidence interval; CPU,
for Spectra and scanpy.score_genes1,2 factors plotted against MAGIC-imputed central processing unit.
Article https://doi.org/10.1038/s41587-023-01940-3
GPU-based expiMap (Fig. 2g). Similarly, Spectra’s peak memory usage T cells kill cancer cells after binding to mutation-associated neoan-
remains low with increasing gene set numbers (Extended Data Fig. 5g). tigens (MANAs). To test whether our tumor reactivity program identi-
Spectra run time and memory increase proportionally with the number fies T cells with MANA-specific TCRs, we leveraged a lung cancer atlas
of cell types and remain low for typical cell-type numbers (Extended of tumor-infiltrating T cells with functionally validated TCR antigen
Data Fig. 5g,h). Our benchmarking demonstrates that Spectra is faster specificity30 (‘Caushi dataset’; Fig. 3g). Spectra detected tumor reactiv-
and infers programs with superior interpretability and coherence while ity and 172 additional factors in these data. Despite the different context
retrieving more ground truth factors. and tumor type, 13 genes overlap among the top 50 marker genes in the
Caushi and Bassez reactivity factors (Extended Data Fig. 6d). Moreover,
Spectra separates tumor reactivity and exhaustion features the Caushi reactivity factor is almost exclusively expressed in T cells
To understand and ultimately improve therapeutic efficacy, we quan- with a MANA-specific TCR rather than in T cells with TCRs for unrelated
tified therapy-induced gene program changes in non-dysfunctional antigens (Fig. 3h). This independent, functionally validated dataset
tumor-reactive CD8+ T cells, a subset of T cells that recognize provides strong support for the Spectra tumor reactivity factors and
tumor-associated antigens16 and are also cytotoxic17,18. These cells suggests that transcriptional features of tumor-reactive T cells are
express clonal TCRs and specific markers and accumulate after PD-1/ shared across tumor types.
PD-L1 checkpoint blockade (clonal expansion19,20). Conversely, T cells In contrast to Spectra, Slalom6, scHPF4 and expiMap9 failed to
that expand clonally under ICT are likely to be tumor-reactive18,19. These deconvolve the two factors (Extended Data Fig. 6e). Only Spectra was
cells may also gradually become exhausted (lose effector capacity) able to distinguish a clonally expanding tumor-reactive T cell popula-
after prolonged antigen exposure in the tumor microenvironment21,22. tion that is specific to responders (Extended Data Fig. 6f) and associates
Although exhaustion and tumor reactivity lead to different cellular with patient-level response (Extended Data Fig. 6g).
behaviors with highly consequential phenotypes, their gene programs Spectra is thus unique in its ability to disentangle tumor reactivity
are correlated and challenging to discriminate computationally; clus- and exhaustion programs in CD8+ T cells, making it possible to iden-
tering approaches typically group exhaustion, tumor reactivity and tify tumor-reactive populations across cancer types and find novel
cytotoxicity features together10,23. mediators of tumor reactivity that can be associated with patient-level
We evaluated Spectra’s ability to deconvolve these programs, therapeutic responses and nominated as candidate targets for enhanc-
focusing on CD8+ T cells (Fig. 3a). The exhaustion and tumor reactivity ing ICT efficacy.
factors scored high in Spectra’s information and importance scores
(see Methods), suggesting that they explain relevant gene programs Spectra uncovers metabolic pathway use in leukocytes
(Extended Data Fig. 6a). Genes from these two programs are correlated Metabolic processes are fundamental to cancer therapeutic response,
in these data (Extended Data Fig. 6b), explaining why they were not but metabolic genes participate in multiple pathways, making their
distinguished previously10,23. score_genes1,2 generates visually similar analysis very challenging38. We tested Spectra’s metabolic inference on
distributions of input gene sets in responders and non-responders immune cells in the Bassez dataset10 and identified programs related
(Fig. 3b), yet the absence of tumor-reactive, non-terminally exhausted to all 89 metabolic input gene sets (overlap coefficient of >0.25), reca-
states in responders is inconsistent with the treatment-induced clonal pitulating known macrophage characteristics, such as iron uptake,
expansion of these states19,20,24,25, and it conflicts with the proven effi- iron storage39,40 and cholesterol synthesis41,42 as well as DNA synthesis
cacy of ICT in this clinical setting26. in cycling germinal center B cells (Fig. 4a).
Whereas gene set scores fail to distinguish expanding from Spectra also uncovered cell-type-specific expression of amino acid
non-expanding clones (Fig. 3b), Spectra clearly disentangles them factors, such as lysine metabolism in plasma cells (Fig. 4a). Lysine is a
(Extended Data Fig. 6c), identifying a substantial tumor-reactive popu- scarce nutrient in malignant breast cancer tissue43. Lysine metabolism
lation that is almost exclusive to responders (Fig. 3c). Spectra extracts scored high in Spectra’s information and importance scores (Extended
gene programs directly from the unlabeled data and does not need Data Fig. 7a). Its top 50 marker genes contain 72% of the input gene
response status to successfully dissect these features. Spectra’s likeli- set, including all key metabolic enzymes (Fig. 4b), and Spectra added
hood function discourages overlap between gene programs when unfolded protein response genes, including the pivotal initiators
a single program is sufficient to explain the observed count matrix, XBP1 and ATF6 and their downstream targets (ERLEC1 (ref. 44), SDF2L1
harnessing unique features of each gene set to associate cells with (ref. 45), HERPUD1 (ref. 46) and PDIA6 (ref. 47)). These genes are
the best fit program. We identified CXCL13 as the gene exhibiting the expressed more coherently and at higher levels in plasma cells than in
highest covariance with tumor reactivity as well as exhaustion factors other cells, as expected for a gene program (Extended Data Fig. 7b).
(Extended Data Fig. 6b). Spectra assigns this tumor reactivity marker27 a Endoplasmic reticulum stress regulates the capacity of plasma cells
high weight in tumor reactivity but not exhaustion and strongly weights to produce immunoglobulins48, likely because large quantities of mis-
genes related to TCR signaling, T cell activation and cytotoxicity in the folded antibodies48 must be degraded, generating lysine49. Other meth-
tumor reactivity factor, whereas the exhaustion factor mostly includes ods identified factors that are either not enriched for lysine metabolism
genes encoding exhaustion-inducing transcription factors (TOX21,22 genes or are uniformly expressed across cells (Extended Data Fig. 7c–e).
and NR4A1 (ref. 28)) and PDCD1 (PD-1) (refs. 21,22). To gauge stability and reproducibility, we fit an independent Spectra
In CD8+ T cells, tumor reactivity correlates with proliferative pro- model onto data from individuals with metastatic breast cancer biopsied
grams, as expected for clonally expanding cells, oxidative phosphoryla- before and during paclitaxel chemotherapy with or without anti-PD-L1
tion and glycolysis, processes associated with enhanced CD8+ T cell treatment (Zhang dataset)23 using identical parameters (Extended Data
effector function29 and IFNγ signaling, a key mediator of ICT efficacy11 Fig. 1b). Of the top 50 markers in the Bassez dataset10, 28 were also iden-
(Fig. 3d). Of the top 50 marker genes in tumor-reactive CD8+ T cells, 42 tified in the Zhang dataset (Fig. 4c), including 17 of the 37 new genes
are outside the input gene set, but recent studies support their roles in learned directly from both datasets and encompassing ER stress. Spectra
tumor reactivity (Fig. 3e and Supplementary Table 3)30–35. lysine metabolism factors from both datasets are specifically expressed
Expression of this factor is higher in responders at baseline in plasma cells (Fig. 4d). Our results link lysine metabolism and ER stress
than in non-responders, and it increases further under therapy in as features of tumor-infiltrating plasma cells in breast cancer.
responders (Fig. 3f), consistent with the reported association between
tumor-reactive cell clusters and therapeutic response36,37. Spectra thus Macrophage states change continuously under therapy
disentangles a CD8+ T cell tumor reactivity program that is associated Macrophages mediate resistance to ICT by becoming immunosuppres-
with response to ICT at the cell and patient levels. sive under therapy (adaptive resistance); however, the effect of ICT on
Nature Biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
a d
TILs Clonal expansion Factor–factor correlation
CD8+ T cells
CD8+ T cells NA
b
Cell scores for input gene sets
Tumor reactivity Exhaustion
gene set gene set
10
c
macrophage gene programs and the association with response remains for Spectra factors form gradients along DC2, with successive peaks
unclear50,51. Bassez et al.10 linked a macrophage cluster expressing the of tumor necrosis factor-α (TNF-α) signaling and CYP enzyme activity,
complement gene C3 to therapy resistance (Extended Data Fig. 8a,b); followed by glycolytic activity54, a novel factor containing invasive and
yet, complement genes such as CFB (which activates C3 (ref. 52)) exhibit angiogenic mediators (‘invasion program’) and finally complement
opposite trends to C3 and are more highly expressed in responders production, a key feature of mature macrophages55. Along DC4, Spectra
(Extended Data Fig. 8b,c). identified programs for type 2 IFN signaling and MHC class II antigen
To determine whether Spectra can identify more interpretable gene presentation at one extreme, followed by the interleukin-4 (IL-4)/IL-13
programs underlying adaptive resistance, we used diffusion compo- response, hypoxia signaling and the invasion program at the other
nents (DCs) to visualize continuous states53. DC2 captures maturation (Fig. 5a; see Supplementary Table 4 for all DC-associated factors).
from monocyte-like to macrophage states, and DC4 separates respond- To find states that change in non-responders under ICT and could
ers from non-responders (Fig. 5a and Extended Data Fig. 8d). Cell scores therefore confer adaptive resistance, we used Milo56, which revealed
Nature Biotechnology
tes
eneg
noitsuahxE
10 3.0 3.0
2.5 2.5 8
2.0 2.0 6
1.5 1.5 4
1.0 1.0 2
0.5 0.5
0 0 0
0 2 4 6 8
Tumor reactivity gene set
0.025
0.020
0.015
0.010
0.005 0
noitsuahxE
:271
rotcaF
Factors
Non-responder Responder 0.7 0 –0.7
Non-responder Responder
Cell scores for spectra factors
Factor 171: Tumor Factor 172:
reactivity Exhaustion
1.6
1.4 0.020 1.2
1.0 0.015
0.8
0.6 0.010
0.4 0.005 0.2
0 0
0 0.5 1.0 1.5
Factor 171: Tumor
reactivity
srotcaF
Pearson correlation
e f
0.8
0.6
0.4
0.2
0
Pre-anti-PD-1 On anti-PD-1
erocs
llec
naeM
Factor 171: Tumor reactivity
Factor 171: Tumor reactivity
marker genes response
Cytotoxicity IC receptor P < 0.0001 PRF1 HAVCR2 P < 0.0001
GZMB TNFRSF4
LTA
T cell survival
BATF
CCL3 TCR signaling
CCR1 DOK2
GADD45G NFATC1 LAYN SH2D2A Non-responder Responder
g
0.010
0.008
0.006
0.004
0.002
0
serocs
lleC
Factor 55: Type I IFN response
Factor 171: Tumor reactivity
Factor 10: Type II IFN response
Factor 127: MHC class II presentation
Factor 27: G2/M transition
Factor 101: DNA synthesis
Factor 102: G1/S transition
Factor 94: Glycolysis
Factor 140: Pentose phosphate
Factor 3: Glyocylate dicarboylate
Factor 31: OXPHOS
Cell score Cell score
h
NSCLC TILs Factor 171: Tumor reactivity antigen specificity
P < 0.0001
Cell score Cell score P < 0.0001
scRNA-seq/ PBMCs scTCR-seq
Match
TCRβ–CDR3 sequence
TCR-seq
Non-responder Responder Tumor neoantigen MANA EBV Influenza A
pulse
Fig. 3 | Spectra deconvolves the highly correlated features of tumor reactivity and lines represent IQR and median, respectively; whiskers represent 1.5× IQR.
and exhaustion in CD8+ T cells. a–h, Analysis of tumor-infiltrating leukocytes Two-sided P values were calculated using Mann–Whitney U-tests; pre-anti-PD-1
(TILs) from the Bassez data10 (n = 42 participants). a, Left, t-SNE embeddings (n = 40 participants): P = 3.84 × 10–5, statistic = 308, Cohen’s d = 1.51; on anti-PD-1
highlighting CD8+ T cells. Right, force-directed layout of CD8+ T cells (n = 31,925 (n = 40 participants): P = 2 × 10–5, statistic = 313, Cohen’s d = 1.49. g, Design of
cells) labeled by clonal T cell expansion (responder) under therapy; NA, not the Caushi study30 (n = 251,777 CD8+ T cells), which profiled PBMCs and TILs
available. b,c, Force-directed layout of CD8+ T cells colored by tumor reactivity from participants with non-small cell lung cancer (NSCLC). PBMCs were pulsed
(left) or exhaustion (right) cell scores and contour plots depicting cell score by peptide pools, and expanding TCR clones were identified by comparing
density distribution. Cell scores were obtained using scanpy.score_genes1,2 PBMC and tumor-infiltrating leukocyte TCR sequences indicating their antigen
(b) or Spectra (c). d, Pearson coefficients of factor cell scores (n = 31,925 cells). specificity; scTCR-seq, single-cell TCR sequencing. h, Cell scores in tumor-
The inset displays factors that are highly correlated to tumor reactivity in CD8+ infiltrating CD8+ T cells with different specificities (n = 1,151); EBV, Epstein–Barr
T cells; OXPHOS, oxidative phosphorylation. e, New genes identified by Spectra virus. P values (two-sided) were calculated by using Mann–Whitney U-tests
(n = 38) among the 50 highest scoring genes in the tumor reactivity factor, (MANA versus influenza A: P = 5.20 × 10–101, statistic = 148,361, Cohen’s d = 1.45;
highlighting processes involved in tumor reactivity in different colors (also see MANA versus Epstein–Barr virus: P = 6.04 × 10–104, statistic = 164,536, Cohen’s
Supplementary Table 3); IC, immune checkpoint. f, Per-sample mean cell scores d = 1.44). Boxes and lines represent IQR and median, respectively; whiskers
for the Spectra tumor reactivity factor in positive cells (score > 0.001). Boxes represent 1.5× IQR.
Article https://doi.org/10.1038/s41587-023-01940-3
a b
Factor 103: Lysine metabolism
Plasma
marker genes
pDC
Mast SLC3A1 SLC7A1 SLC7A2
γδT
T reg SPCS1 ER stress response
NK SPCS2 SSR3
Mac SPCS3 XBP1
LYS
ILC3 Trimethyl-LYS SEC61A1
SEC11C
DC
PDIA6
CD8 T AASS PIPOX TMLHE CANX
CD4 T Glu FKBP2
B naive ALDH7A1 SEC61G
PYCR2/3 BBOX1 SERP1
B mem NH 3 AADAT HERPUD1
B GC PIP SEC1 SLC25A15 DNAJB9 HSPA5
Acetyl-CoA
SELENOS SSR4
HSP90B1
FKBP11 Input gene
ERLEC1 New gene (Spectra) FKBP2
R ex e p la r t e iv ss e i on 0.15 0.30 0.45 0.60 0.75 0.90 P fr o a s c i t t i i o v n e 0.8 0.6 0.4 0.2
c
Factor 103: Lysine metabolism Factor 103: Lysine metabolism
Bassez et al. Cell score Zhang et al. Cell score
Input Bassez et al. 0.14 0.35
2 20 0.12 0.30
4 AADAT 0.10 0.25
XBP1
11 HERPUD1 AASS 0.08 0.20
ALDH7A1
1 17 E FK R B LE P C 2 1 BBOX1 0.06 0.15
IGKC PIPOX 0.04 0.10
SLC3A1
ITM2C SLC7A1 0.02 0.05
MYDGF
21 PDIA6 SLC7A2 0 0
SPCS1 SDF2L1
SPCS3
Zhang et al. SEC11C TMLHE SEC61B
SERP1
SSR3
SSR4
TMED2
TMEM59
TPT1
overlapping cellular neighborhoods (states) that only expand under (ref. 69)), some of which suppress inflammatory cytokine (IL-6 and
anti-PD-1 therapy in non-responders (Fig. 5b) and are high in the novel TNF-α) release65. Our results suggest that in individuals who do not
invasion program (Fig. 5c). This invasion program does not correspond respond to ICT, macrophages may upregulate these genes coordinately
to input gene sets (η = 0.24) but has high importance and information (Fig. 5d). By focusing on residual expression that is not well explained
scores; moreover, Slalom6 and scHPF4 do not identify a similar pro- by the gene knowledge graph, Spectra can thus find a gene program
gram (Extended Data Fig. 8e–g). Its constituent genes are coherently that is both interpretable and related to ICT response.
expressed in macrophages, only increase in non-responders and include To test for replication, we ran Milo, identified macrophage popu-
genes encoding known invasion and metastasis mediators (CTSL57, lations in the Zhang dataset23 and scored expression of the top 50
CTSD58, CTSB59, CHI3L1 (ref. 60), SPP1 (ref. 61) and PLIN2 (ref. 62)). invasion factor genes. Despite the different setting of metastatic
Furthermore, the invasion program includes genes of inflamma- tumors, the invasion and cholesterol metabolism genes identified in
tion modulators (TREM1 (ref. 63), TREM2 (ref. 64) and GPNMB65) and the Bassez data have high expression in the Zhang data, validating our
cholesterol metabolism genes (APOE66,67, APOC1 (ref. 68) and CYP27A1 invasion program (Fig. 5c,d). Spectra thus identifies a prometastatic
Nature Biotechnology
amsalP CG
B
B
yromeM
B
eviaN
T
4DC
T
8DC
CD 3CLI caM KN gerT Tδγ tsaM CDp amsalP B
CG
B
yromeM
B
eviaN
B
gnilcyC
T
4DC
T
8DC
CD 3CLI caM KN T gerT Tδγ tsaM onoM CDp
Factor cell scores
d
Marker genes
Percent positive Percent positive
20406080100 20406080100
Relative expression Relative expression
0 1 0 1
13 rotcaf
:SOHPXO
23 rotcaf
:msilobatem
eninitaerC
17 rotcaf
:srotcaf
noitalugaoC
74 rotcaf
:enarbmemsnarT
3 rotcaf
:msilobatem
etalyxoylG
47 :msilobatem
SIH
901 rotcaf
:sisehtnys
enidimiryP
83 rotcaf
:msilobatem
SYC
42 rotcaf
:htaed
llec
cigahpotuA
51 rotcaf
:enorepahc
ygahpotuA
521 rotcaf
:noitadarged
nacylG-N
131 rotcaf
:noiatadarged
nacylG-N
921 rotcaf
:esnopser
aixopyH
65 rotcaf
:sisenegocylG
66 rotcaf
:gnitavitca
teletalP
33 rotcaf
:noitaluger
ygahpotuA
92 rotcaf
:msilobatem
eninalA-β
68 rotcaf
:msilobatem
loniteR
28 rotcaf
:msilobatem
loretselohC
61 rotcaf
:enarbmemsnarT
601 rotcaf
:msilobatem
etaonaporP
38 rotcaf
:msilobatem
PI
81 rotcaf
:sisehtnys
nacylG-O
37 rotcaf
:sisylonegocylG
95 :msilobatem
enimaihT
821 :tropsnart
RE
311 rotcaf
:msilobatem
nitoiB
59 rotcaf
:msilobatem
PRT
97 rotcaf
:msilobatem
nivalfobiR
011 rotcaf
:msilobatem
dica
yttaF
03 rotcaf
:sisehtnys
niretP
301 rotcaf
:msilobatem
SYL
101 rotcaf
:sisehtnys
AND
841 :noitcudorp
tnemelpmoC
86 rotcaf
:msilobatem
PYC
121 rotcaf
:srotcaf
sisylobmorhT
05 rotcaf
:msilobatem
etavuryP
96 rotcaf
:egarots
dna
ekatpu
norI
Fig. 4 | Spectra reveals cell-type-specific metabolic profiles in breast cancer Spectra in the lysine metabolism pathway; CoA, coenzyme A; Glu, glutamine; PIP,
data. a, Mean cell scores among positive (score > 0.01) cells normalized to pipecolic acid. c, Overlap between the input lysine metabolism gene set and the
maximum cell scores of each factor and positive fractions per cell type for each top 50 marker genes from lysine metabolism factors identified in the Bassez10
Spectra metabolic factor identified in the Bassez data10 (n = 97,863 leukocytes). and Zhang23 datasets. d, t-SNE embeddings of TILs colored by Spectra factor cell
The box highlights the plasma cell-enriched lysine (LYS) metabolism factor; CYP, scores in the Bassez (n = 97,863 leukocytes) and Zhang (n = 150,985 leukocytes)
cytochrome P450; CYS, cysteine; ER, endoplasmic reticulum; HIS, histidine; datasets.
mem, memory; TRP, tryptophan. b, Input genes and genes newly inferred by
Article https://doi.org/10.1038/s41587-023-01940-3
b
Anti-PD-1 fold change (non-responder)
Size
50
100
150
200
250
Overlap
50
100
–4 0 4
Enriched pre-anti-PD-1 Enriched on-anti-PD-1 log (fold change) on/pre
2
c d
gene program that is upregulated following anti-PD-1/PD-L1 treatment Spectra factors generalize to hundreds of individuals
in individuals with therapy-resistant breast cancer, with implications Batch correction of technical differences between samples and cohorts
for understanding adaptive resistance mechanisms and macrophage tends to remove subtle, yet important, biological signals70, so we asked
polarization. whether Spectra can find shared features without explicit batch correction.
Nature Biotechnology
)noitaziralop
egahporcam(
4CD
y ~ response + timepoint * response + timepoint
FDR<0.05
DC2
Macrophage like Monocyte like
01
rotcaf
:esnopser
γNFI
721
rotcaf
noitatneserp
II
ssalc
CHM
Macrophages/monocytes
)noitaziralop
egahporcam(
4CD
Responder
Non-responder
Factor 148: Complement
Factor 94: Glycolysis
Factor 68: CYP metabolism Factor 2: TNF-α signaling
Factor 182: Invasion
481
rotcaf
:esnopser
31-LI/4-LI
921
rrotcaf
:esnopser
aixopyH
DC2 Macrophage like Monocyte like 281
rotcaf
:noisavnI
a
z-scored
cell score
–2 –1 0 1 –2 –1 0 1 2 3
Bassez et al.
serocs
lleC
Factor 182: Invasion
cell scores
Bassez et al.
Zhang et al.
serocs
lleC
z-scored
cell score
Factor 182: Invasion
marker genes
0.7 P < 0.0001 Non-responder
0.6 Mac
0.5 Other Mac
0.4
0.3
0.2
0.1
0
Other Non-responder Zhang et al.
Mac Mac
Non-responder
Mac
Other Mac
14 P = 0.0002
12
10
8
6
4
2 Ce
2
l
0
ls
4 0
in
6 0
g
8
r
0
o 1 u
00
p (%)
–1.5
Average
0
z score
1.5
0
Other Non-responder
Mac Mac
1PPS
1PPS
9PMM
9PMM
LSTC
LSTC
2LCC
2LCC
1COPA
1COPA
1SANR
1SANR
1RPUN
1RPUN
84fro51C
84fro51C
BMNPG
BMNPG
8LCXC
8LCXC
MDA
MDA
52MIMS
52MIMS
1PBF
1PBF
91PMM
91PMM
1A11CLS
1A11CLS
1A72PYC
1A72PYC
4PBAF
4PBAF
OCRAM
OCRAM
NR1LI
NR1LI
1XOMH
1XOMH
7G2ALP
7G2ALP
2NILP
2NILP
H1TM
H1TM
5PBAF
5PBAF
63DC
63DC
RUALP
RUALP
2CDS
2CDS
G1TM
G1TM
86DC
86DC
1NF
1NF
BRVLB
BRVLB
EOPA
EOPA
1PPU
1PPU
1L3IHC
1L3IHC
2AXNA
2AXNA
3LCXC
3LCXC
2DOS
2DOS
1MERT
1MERT
7LCC
7LCC
2MERT
2MERT
DCS
DCS
LULG
LULG
81LCC
81LCC
PBORYT
PBORYT
3H1RN
3H1RN
LPN
LPN
BTSC
BTSC
PEPNA
PEPNA
DSTC
DSTC
4SLAGL
4SLAGL
Fig. 5 | Spectra reveals therapy-induced macrophage gene expression and cell scores for all other macrophage neighborhoods in the independent
programs. a, Macrophage cells plotted along DCs 2 and 4 colored by patient- Bassez and Zhang breast cancer datasets. Cell scores were calculated using
level T cell expansion status (responder and non-responder) in the Bassez the Spectra invasion factor (factor 182 from Bassez et al.10) or by using scanpy.
data10 (n = 12,132 cells). Heat maps indicate z-scored gene program cell scores score_genes1,2 on the top 50 marker genes of factor 182 in Zhang et al.23. P values
along DCs smoothened by fitting a generalized additive model (Methods); (two-sided) were calculated using Mann–Whitney U-tests (Bassez: P = 4.96 × 10–5,
IL, interleukin; TNF, tumor necrosis factor. b, Graph with nodes representing statistic = 1,060, Cohen’s d = 1.49; Zhang: P = 3.74 × 10–12, statistic = 600,886,
cellular neighborhoods (n = 858) plotted along DC2 and DC4 and edges Cohen’s d = 1.03). Boxes and lines represent IQR and median, respectively;
representing overlap colored by log (fold change) under anti-PD-1 treatment, as whiskers represent 1.5× IQR. d, Mean expression z scored across cells (n = 12,132
2
estimated with Milo (Methods). The log (fold change) of non-significant (false cells) and percentage of cells with at least one detected copy of the indicated
2
discovery rate (FDR) ≥ 0.05) neighborhoods is set to 0. c, Average cell scores of factor genes in non-responder macrophage populations and other macrophage
macrophage neighborhoods (n = 858) enriched in non-responders under therapy populations in the Bassez (n = 12,132 cells) and Zhang (n = 3,206 cells) datasets.
Article https://doi.org/10.1038/s41587-023-01940-3
a b
Lysine metabolism
cell-type specificity (per study)
Nature Biotechnology
53–01
× 94.5
= P
33–01
× 50.3
= P
13–01
× 17.7
= P
52–01
× 90.6
= P
32–01
× 88.1
= P
51–01
× 92.1
= P
72–01
× 76.2
= P
71–01
× 75.1
= P
03–01
× 22.2
= P
31–01
× 13.4
= P
Vieira
Chen
Lambrechts
Wu
Laughney
Habermann
Adamns
He
Madissoon
Zilionis
UKIM-V
Reyfman
Leader
Goveia
Mayr
Kim
Guo
Maynarrd
Travaglini
rohtua
ydutS
Mean z-scored expression
Mann–Whitney U-test
(versus plasma)
Cell type caM T 4DC CD KN T 8DC T ger B tsaM T narG amsalP
Salcher et al. NSCLC atlas Batch specificity of global factors
Study (318 individuals, 1.28 million cells) Cell type
Adams Laugh. B Fibro
Chen Leader CD4 T Gran
Goveia Madis. CD8 T Mast
Guo Mayn. DC Plasma
Vieira Zilionis Mac
Haber. Mayr NK
He Reyfm. T
Kim Travag. T
reg
Lambr. UKIM-V Endo
Wu Epi
c
Mac invasion marker genes
Bassez et al. Zhang et al.
Retained new genes 20 10 21 TREM1 CTSD 12 APOC1 CTSL APOE FN1 8 7 FABP5 CD68
GPNMB NUPR1 23 SCD SLC11A1
Salcher et al.
d e f
Factor 174: CD8 tumor reactivity Factor 193: Macrophage invasion
0.014
0.012
0.010
0.008
0.006
0.004
0.002
0
Never smoker Ever smoker Never smoker Ever smoker
–1
0 40
0 Participant 1 number
–2 0 2
z-scored mean cell score
EGFR mutated EGFR wild type
erocs
llec
naeM
erocs
llec
naeM
0.020
0.015
0.010
0.005
0
0.012
0.010
0.008
0.006
0.004
0.002
0
erocs
llec
naeM
0.014
0.012
0.010
0.008
0.006
0.004
0.002
0
erocs
llec
naeM
Factor 37
Ascorbate met.: factor 124 Frozen cells
Factor 103
β-Catenin: factor 62
Cyclic nucleotide met.: factor 47
Glycerophospholipid met.: factor 122
DNA demethylation: factor 17
Factor 52
Factor 128
TRP met.: factor 138
Thiamin met.: factor 32
Smoking status Smoking status
EGFR status EGFR status
smadA nehC aievoG ouG nnamrebaH eH miK sthcerbmaL redaeL yenhguaL nossidaM dranyaM ryaM namfyeR inilgavarT V-MIKU arieiV uW sinoiliZ Positive fraction (%) Mean expression
10 30405060 0 0.5 1.0
Study
Lysine metabolism marker genes CD8 tumor-reactivity marker genes
Bassez et al. Zhang et al. Bassez et al. Zhang et al.
16 19 21 24
Retained new genes
10 10 Retained new genes 0 5 7 2 P S D D I F A 2 6 L1 T T M M E E D M 2 59 0 2 6 3 B LA A G TF 3 3 G G Z Z M M B H 4 29 S S E E C C 1 6 1 1 C B IGKC 0 30 PRF1 FASLG 6 4
1 4 R A e A ta S i S ned in S p P u C t S g 1 enes 0 5 R IT e G ta A in E ed in IF p N ut G genes
0 2 ALDH7A1 SPCS3 0 2 TNFRSF9GZMA
PIPOX TMLHE
Input 0 Salcher et al. Input 0 Salcher et al.
P = 0.002 P = 0.051
P = 0.010
P = 0.180
EGFR mutated EGFR wild type
Fig. 6 | Spectra gene programs are reproducible across multiple studies. tests. (B cells: statistic = 2,903, Cohen’s d = 0.77; CD4+ T cells: statistic = 2,385,
a, Uniform manifold approximation and projection (UMAP) embeddings of Cohen’s d = 0.88; CD8+ T cells: statistic = 4,555, Cohen’s d = 0.70; dendritic cells:
whole tumor single cell suspensions (n = 1.28 million cells) colored by study statistic = 3,152, Cohen’s d = 0.76; granulocytes: statistic = 516, Cohen’s d = 0.91;
(left) or cell type (right) in the Salcher atlas71; Endo, endothelial; Epi, epithelial; macrophages: statistic = 2,350, Cohen’s d = 0.86; mast cells: statistic = 5,348,
Fibro, fibroblast; Gran, granulocyte; Haber., Habermann; Lambr., Lambrechts; Cohen’s d = 0.52; NK cells: statistic = 3,883, Cohen’s d = 0.70; regulatory T cells:
Laugh., Laughney; Madis., Madissoon; Mayn., Maynard; Reyfm., Reyfman; statistic = 4,441, Cohen’s d = 0.61; T cells: statistic = 3,345, Cohen’s d = 0.56). The
Travag., Travaglini. b, Expression and positive cell fraction of global Spectra studies listed in a, b and d are from Salcher et al.71. e,f, Mean cell scores per patient
factors with the lowest entropy across studies. The Adams study with batch in positive (>0.001) CD8+ T cells (e) or macrophages (f) for the tumor reactivity
effect is highlighted in red; met., metabolism. c, Overlap between the input gene factor (e) and the macrophage invasion factor (f) based on smoking (top) or EGFR
set and the top 50 marker genes for lysine metabolism (left), tumor reactivity mutation (bottom) status. P values were calculated using Mann–Whitney U-tests
(middle) and macrophage invasion (right; new factor, no input set) factors. (two-sided); tumor reactivity smoking: n = 153, P = 0.0022, statistic = 3,500,
d, Mean cell scores, z-scored across cell type, of the lysine metabolism factor Cohen’s d = 0.45; tumor reactivity EGFR: n = 30, P = 0.18, statistic = 78, Cohen’s
per study and cell type. Bars indicate mean z score per column (bottom) and d = 0.52; invasion smoking: n = 147, P = 0.051, statistic = 2,928, Cohen’s d = 0.30;
participant numbers per study (right). Two-sided P values between plasma cells invasion EGFR: n = 32, P = 0.010, statistic = 59, Cohen’s d = 1.17). Boxes and lines
and other cell types were calculated using Wilcoxon matched-pairs signed-rank represent IQR and median, respectively; whiskers represent 1.5× IQR.
Article https://doi.org/10.1038/s41587-023-01940-3
The scRNA-seq lung cancer atlas from Salcher et al.71 is composed us to discover a cancer invasion program describing an axis of variation
of 1.28 million cells from 19 studies and 318 individuals, including a in tumor-associated macrophages that is strongly related to anti-PD-1
study that uses cryopreserved cells and exhibits a strong batch effect therapy resistance and is replicated in two independent datasets.
(Fig. 6a). We applied Spectra with default parameters and our immunol- The common simplifying assumption made by factor analysis
ogy knowledge base and found 11 global factors with low cross-study methods is that factors combine linearly to drive expression, which is
entropy (Methods), 10 of which are specific to the cryopreserved cell not always the case. Uncovering interpretable nonlinear relationships
study and account for its batch-driven variation (Fig. 6b). is a future goal of factorization methods development.
Spectra identified lysine metabolism, CD8+ T cell-specific tumor We designed Spectra to unravel heterogeneity in large-scale
reactivity and macrophage-specific invasion factors in the Salcher atlas scRNA-seq studies. Spectra factors are stable across two breast cancer
without batch correction. Despite differences in tumor type and clinical datasets and a lung cancer atlas totaling over 1.5 million cells from 375
cohort, multiple factor genes are shared across the Bassez, Zhang and individuals and 21 studies, demonstrating the ability to find robust bio-
Salcher datasets (Fig. 6c). Newly discovered shared genes include ER logical signal and overcome batch effects at this scale. Spectra factors
stress transcription factors XBP1 and ATF6 and targets (SDF2L1 (ref. 45) make it possible to associate clinical covariates with cell-type-specific
and PDIA6 (ref. 47; lysine metabolism factor)), the TCR signaling target gene programs. In addition, the ability to transfer factors learned from
BATF31,35 and the immune checkpoint gene LAG3 (refs. 32,72; tumor reac- one dataset to another can advance our ability to iteratively transfer
tivity factor), invasion mediators CTSL and CTSD57,58 and inflammatory and refine knowledge across scRNA-seq studies without requiring
mediators TREM1 (ref. 63) and GPNMB65 (macrophage invasion factor). data integration.
The identified factors are very stable across the Salcher atlas, and lysine
metabolism is significantly enriched in plasma cells (13 of 19 studies, Online content
P < 10−12), as observed in breast cancer (Fig. 6d). Any methods, additional references, Nature Portfolio reporting sum-
Next, we tested for associations between Spectra factors and maries, source data, extended data, supplementary information,
two clinically important variables, EGFR mutation and smoking sta- acknowledgements, peer review information; details of author contri-
tus. Although EGFR-mutated tumors are resistant to ICT73, smokers butions and competing interests; and statements of data and code avail-
respond more frequently74. Tumor reactivity cell scores are higher in ability are available at https://doi.org/10.1038/s41587-023-01940-3.
CD8+ T cells from tumors of smokers than from tumors of non-smokers
(P = 0.002) and are higher in wild-type EGFR tumors than in mutated References
tumors (P = 0.180; Fig. 6e). The invasion factor similarly shows higher 1. Satija, R., Farrell, J. A., Gennert, D., Schier, A. F. & Regev, A.
cell scores in macrophages from smokers (P = 0.051) and wild-type EGFR Spatial reconstruction of single-cell gene expression data.
tumors (P = 0.010; Fig. 6f). In the breast cancer datasets, this factor is Nat. Biotechnol. 33, 495–502 (2015).
associated with ICT resistance (Fig. 5c), and studies of its marker genes 2. Wolf, F. A., Angerer, P. & Theis, F. J. Scanpy: large-scale single-cell
suggest that they are involved in suppressing antitumor immunity gene expression data analysis. Genome Biol. 19, 15 (2018).
(FABP5 (ref. 75) and TREM1 (ref. 63)). 3. Bielecki, P. et al. Skin-resident innate lymphoid cells converge on
Spectra thus finds subtle programs across batches and patients a pathogenic effector state. Nature 592, 128–132 (2021).
without requiring explicit batch correction. Although patient- or 4. Levitin, H. M. et al. De novo gene signature identification from
sample-level phenotypic association has been attempted with cell-type single-cell RNA-seq with hierarchical poisson factorization.
fractions, Spectra factors make it possible to associate clinical pheno- Mol. Syst. Biol. 15, e8557 (2019).
types with cell-type-specific gene programs, a promising strategy for 5. Pelka, K. et al. Spatially organized multicellular immune hubs in
cancer research and biomarker discovery. human colorectal cancer. Cell 184, 4734–4752 (2021).
6. Buettner, F., Pratanwanich, N., McCarthy, D. J., Marioni, J. C. &
Discussion Stegle, O. f-scLVM: scalable and versatile factor analysis for
Spectra anchors data-driven factorization with prior knowledge to single-cell RNA-seq. Genome Biol. 18, 212 (2017).
infer factors that are coherently expressed, interpretable and not pol- 7. Elyanow, R., Dumitrascu, B., Engelhardt, B. E. & Raphael, B. J.
luted by cell-type markers. The algorithm modifies each factor to the netNMF-sc: leveraging gene–gene interactions for imputation
dataset’s biological context by upweighting novel genes that are tightly and dimensionality reduction in single-cell expression analysis.
expressed with factor genes, and it can dissect highly correlated factors, Genome Res. 30, 195–204 (2020).
such as T cell exhaustion and tumor reactivity. We demonstrate that 8. Kartha, V. K. et al. Functional inference of gene regulation using
tumor reactivity program expression separates individuals with breast single-cell multi-omics. Cell Genom. 2, 100166 (2022).
cancer by their clonal expansion status after anti-PD-1 treatment (other 9. Lotfollahi, M. et al. Biologically informed deep learning to query
methods fail) and is replicated in a lung cancer setting with functionally gene programs in single-cell atlases. Nat. Cell Biol. 25, 337–350
validated T cell specificity. (2023).
We found that differences related to cell type dominate the mar- 10. Bassez, A. et al. A single-cell map of intratumoral changes during
ginal gene–gene covariance matrix, obscuring higher-resolution anti-PD-1 treatment of patients with breast cancer. Nat. Med. 27,
cell-type-conditional covariance structure. Spectra uniquely addresses 820–832 (2021).
this multiscale expression variance by accepting cell-type labels as input 11. Grasso, C. S. et al. Conserved interferon-γ signaling drives clinical
and explicitly modeling cell-type-specific factors that can account for response to immune checkpoint blockade therapy in melanoma.
local correlation patterns. As a result, Spectra reliably identifies programs Cancer Cell 38, 500–515 (2020).
that are conserved across multiple cell types related to metabolism, 12. Goswami, S. et al. Immune profiling of human tumors identifies
response to cytokine signaling, differentiation and growth and separately CD73 as a combinatorial target in glioblastoma. Nat. Med. 26,
estimates the cell-type-specific components of these programs. 39–46 (2020).
Our knowledge base of high-confidence gene sets can improve 13. Jorgovanovic, D., Song, M., Wang, L. & Zhang, Y. Roles of IFN-γ in
immune scRNA-seq data analysis using any supervised method, but tumor progression and regression: a review. Biomark. Res. 8, 49
Spectra does not strictly need good relevant gene sets; it adaptively (2020).
tunes its reliance on prior information based on concordance of the 14. Alawi, F. & Lee, M. N. DKC1 is a direct and conserved
input graph with observed data, and it allocates novel factors when prior transcriptional target of c-MYC. Biochem. Biophys. Res. Commun.
information does not fully explain expression. This property allowed 362, 893–898 (2007).
Nature Biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
15. Marinkovic, D. et al. Identification of novel MYC target genes 37. Chow, A. et al. The ectonucleotidase CD39 identifies
with a potential role in lymphomagenesis. Nucleic Acids Res. 32, tumor-reactive CD8+ T cells predictive of immune checkpoint
5368–5378 (2004). blockade efficacy in human lung cancer. Immunity 56, 93–106
16. Van der Leun, A. M., Thommen, D. S. & Schumacher, T. N. CD8+ (2023).
T cell states in human cancer: insights from single-cell analysis. 38. Artyomov, M. N. & Van den Bossche, J. Immunometabolism in the
Nat. Rev. Cancer 20, 218–232 (2020). single-cell era. Cell Metab. 32, 710–725 (2020).
17. Duhen, T. et al. Co-expression of CD39 and CD103 identifies 39. Costa da Silva, M. et al. Iron induces anti-tumor activity in
tumor-reactive CD8 T cells in human solid tumors. Nat. Commun. tumor-associated macrophages. Front. Immunol. 8, 1479 (2017).
9, 2724 (2018). 40. Sun, J.-L. et al. Tumor cell-imposed iron restriction drives
18. Li, H. et al. Dysfunctional CD8 T cells form a proliferative, immunosuppressive polarization of tumor-associated
dynamically regulated compartment within human melanoma. macrophages. J. Transl. Med. 19, 347 (2021).
Cell 176, 775–789 (2019). 41. Lee, M.-S. & Bensinger, S. J. Reprogramming cholesterol
19. Lee, Y. J. et al. CD39+ tissue-resident memory CD8+ T cells with a metabolism in macrophages and its role in host defense against
clonal overlap across compartments mediate antitumor immunity cholesterol-dependent cytolysins. Cell. Mol. Immunol. 19,
in breast cancer. Sci. Immunol. 7, eabn8390 (2022). 327–336 (2022).
20. Yost, K. E. et al. Clonal replacement of tumor-specific T cells 42. Behmoaras, J. et al. Macrophage epoxygenase determines a
following PD-1 blockade. Nat. Med. 25, 1251–1259 (2019). profibrotic transcriptome signature. J. Immunol. 194, 4705–4716
21. Scott, A. C. et al. TOX is a critical regulator of tumour-specific (2015).
T cell differentiation. Nature 571, 270–274 (2019). 43. Vazquez Rodriguez, G., Abrahamsson, A., Turkina, M. V. &
22. Khan, O. et al. TOX transcriptionally and epigenetically programs Dabrosin, C. Lysine in combination with estradiol promote
CD8+ T cell exhaustion. Nature 571, 211–218 (2019). dissemination of estrogen receptor positive breast cancer via
23. Zhang, Y. et al. Single-cell analyses reveal key immune cell upregulation of U2AF1 and RPN2 proteins. Front. Oncol. 10,
subsets associated with response to PD-L1 blockade in 598684 (2020).
triple-negative breast cancer. Cancer Cell 39, 1578–1593 44. Misiewicz, M. et al. Identification of a novel endoplasmic
(2021). reticulum stress response element regulated by XBP1. J. Biol.
24. Miller, B. C. et al. Subsets of exhausted CD8+ T cells differentially Chem. 288, 20378–20391 (2013).
mediate tumor control and respond to checkpoint blockade. 45. Sasako, T. et al. Hepatic SDF2L1 controls feeding-induced ER
Nat. Immunol. 20, 326–336 (2019). stress and regulates metabolism. Nat. Commun. 10, 947 (2019).
25. Siddiqui, I. et al. Intratumoral TCF1+PD-1+CD8+ T cells with 46. Sharma, R. B., Darko, C. & Alonso, L. C. Intersection of the ATF6
stem-like properties promote tumor control in response to and XBP1 ER stress pathways in mouse islet cells. J. Biol. Chem.
vaccination and checkpoint blockade immunotherapy. Immunity 295, 14164–14177 (2020).
50, 195–211 (2019). 47. Vekich, J. A., Belmont, P. J., Thuerauf, D. J. & Glembotski, C. C.
26. Schmid, P. et al. Pembrolizumab for early triple-negative breast Protein disulfide isomerase-associated 6 is an ATF6-inducible
cancer. N. Engl. J. Med. 382, 810–821 (2020). ER stress response protein that protects cardiac myocytes from
27. Liu, B., Zhang, Y., Wang, D., Hu, X. & Zhang, Z. Single-cell ischemia/reperfusion-mediated cell death. J. Mol. Cell. Cardiol.
meta-analyses reveal responses of tumor-reactive CXCL13+ T cells 53, 259–267 (2012).
to immune-checkpoint blockade. Nat. Cancer 3, 1123–1136 48. Ricci, D., Gidalevitz, T. & Argon, Y. The special unfolded
(2022). protein response in plasma cells. Immunol. Rev. 303, 35–51
28. Liu, X. et al. Genome-wide analysis identifies NR4A1 as a key (2021).
mediator of T cell dysfunction. Nature 567, 525–529 (2019). 49. Dennler, P., Fischer, E. & Schibli, R. Antibody conjugates: from
29. Chowdhury, P. S., Chamoto, K., Kumar, A. & Honjo, T. heterogeneous populations to defined reagents. Antibodies 4,
PPAR-induced fatty acid oxidation in T cells increases the number 197–224 (2015).
of tumor-reactive CD8+ T cells and facilitates anti-PD-1 therapy. 50. Wang, L. et al. Myeloid cell-associated resistance to PD-1/
Cancer Immunol. Res. 6, 1375–1387 (2018). PD-L1 blockade in urothelial cancer revealed through bulk and
30. Caushi, J. X. et al. Transcriptional programs of neoantigen- single-cell RNA sequencing. Clin. Cancer Res. 27, 4287–4300
specific TIL in anti-PD-1-treated lung cancers. Nature 596, 126–132 (2021).
(2021). 51. DeNardo, D. G. & Ruffell, B. Macrophages as regulators of tumour
31. Seo, H. et al. BATF and IRF4 cooperate to counter exhaustion in immunity and immunotherapy. Nat. Rev. Immunol. 19, 369–382
tumor-infiltrating CAR T cells. Nat. Immunol. 22, 983–995 (2021). (2019).
32. Gros, A. et al. PD-1 identifies the patient-specific CD8+ 52. Riihilä, P. et al. Complement component C3 and complement
tumor-reactive repertoire infiltrating human tumors. J. Clin. Invest. factor B promote growth of cutaneous squamous cell carcinoma.
124, 2246–2259 (2014). Am. J. Pathol. 187, 1186–1197 (2017).
33. Boutet, M. et al. Memory CD8+ T cells mediate early 53. Haghverdi, L., Buettner, F. & Theis, F. J. Diffusion maps for
pathogen-specific protection via localized delivery of high-dimensional single-cell analysis of differentiation data.
chemokines and ifnγ to clusters of monocytes. Sci. Adv. 7, Bioinformatics 31, 2989–2998 (2015).
eabf9975 (2021). 54. Lee, M. K. et al. Glycolysis is required for LPS-induced activation
34. Shanker, A. et al. CD8 T cell help for innate antitumor immunity. and adhesion of human CD14+CD16– monocytes. Front. Immunol.
J. Immunol. 179, 6651–6662 (2007). 10, 2054 (2019).
35. Chen, Y. et al. BATF regulates progenitor to cytolytic effector CD8+ 55. Lubbers, R., Van Essen, M., Van Kooten, C. & Trouw, L. Production
T cell transition during chronic viral infection. Nat. Immunol. 22, of complement components by cells of the immune system.
996–1007 (2021). Clin. Exp. Immunol. 188, 183–194 (2017).
36. Yeong, J. et al. Intratumoral CD39+CD8+ T cells predict response 56. Dann, E., Henderson, N. C., Teichmann, S. A., Morgan, M. D. &
to programmed cell death protein-1 or programmed death Marioni, J. C. Differential abundance testing on single-cell data
ligand-1 blockade in patients with NSCLC. J. Thorac. Oncol. 16, using k-nearest neighbor graphs. Nat. Biotechnol. 40, 245–253
1349–1358 (2021). (2022).
Nature Biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
57. Dykes, S. S., Fasanya, H. O. & Siemann, D. W. Cathepsin L secretion 70. Persad, S. et al. Seacells infers transcriptional and epigenomic
by host and neoplastic cells potentiates invasion. Oncotarget 10, cellular states from single-cell genomics data. Nat. Biotechnol.
5560–5568 (2019). https://doi.org/10.1038/s41587-023-01716-9 (2023).
58. Rochefort, H. & Liaudet-Coopman, E. Cathepsin D in cancer 71. Salcher, S. et al. High-resolution single-cell atlas reveals diversity
metastasis: a protease and a ligand. APMIS 107, 86–95 (1999). and plasticity of tissue-resident neutrophils in non-small cell lung
59. Vasiljeva, O. et al. Tumor cell-derived and macrophage-derived cancer. Cancer Cell 40, 1503–1520 (2022).
cathepsin B promotes progression and lung metastasis of 72. Tawbi, H. A. et al. Relatlimab and nivolumab versus nivolumab
mammary cancer. Cancer Res. 66, 5242–5250 (2006). in untreated advanced melanoma. N. Engl. J. Med. 386, 24–34
60. Lee, Y. S. et al. A small molecule targeting CHI3L1 inhibits lung (2022).
metastasis by blocking IL-13Rα2-mediated JNK–AP-1 signals. 73. Hastings, K. et al. EGFR mutation subtypes and response to
Mol. Oncol. 16, 508–526 (2022). immune checkpoint blockade treatment in non-small-cell lung
61. Huang, R.-h et al. Osteopontin promotes cell migration and cancer. Ann. Oncol. 30, 1311–1320 (2019).
invasion, and inhibits apoptosis and autophagy in colorectal 74. Dai, L. et al. The effect of smoking status on efficacy of immune
cancer by activating the p38 MAPK signaling pathway. checkpoint inhibitors in metastatic non-small cell lung cancer:
Cell. Physiol. Biochem. 41, 1851–1864 (2017). a systematic review and meta-analysis. EClinicalMedicine 38,
62. He, Y. et al. Lipid droplet-related PLIN2 in CD68+ 100990 (2021).
tumor-associated macrophage of oral squamous cell 75. Liu, J. et al. Lipid-related FABP5 activation of tumor-associated
carcinoma: implications for cancer prognosis and monocytes fosters immune privilege via PD-L1 expression on
immunotherapy. Front. Oncol. 12, 824235 (2022). T cells in hepatocellular carcinoma. Cancer Gene Ther. 29,
reg
63. Yuan, Z. et al. TREM-1 is induced in tumor associated 1951–1960 (2022).
macrophages by cyclo-oxygenase pathway in human non-small
cell lung cancer. PloS ONE 9, e94241 (2014). Publisher’s note Springer Nature remains neutral with regard to
64. Park, M. D. et al. TREM2 macrophages drive NK cell paucity and jurisdictional claims in published maps and institutional affiliations.
dysfunction in lung cancer. Nat. Immunol. 24, 792–801 (2023).
65. Liguori, M. et al. The soluble glycoprotein NMB (GPNMB) produced Open Access This article is licensed under a Creative Commons
by macrophages induces cancer stemness and metastasis via Attribution 4.0 International License, which permits use, sharing,
CD44 and IL-33. Cell. Mol. Immunol. 18, 711–722 (2021). adaptation, distribution and reproduction in any medium or format,
66. Baitsch, D. et al. Apolipoprotein E induces antiinflammatory as long as you give appropriate credit to the original author(s) and the
phenotype in macrophages. Arterioscler. Thromb. Vasc. Biol. 31, source, provide a link to the Creative Commons license, and indicate
1160–1168 (2011). if changes were made. The images or other third party material in this
67. Kemp, S. B. et al. Apolipoprotein E promotes immune suppression article are included in the article’s Creative Commons license, unless
in pancreatic cancer through NF-κB-mediated production of indicated otherwise in a credit line to the material. If material is not
CXCL1. Cancer Res. 81, 4305–4318 (2021). included in the article’s Creative Commons license and your intended
68. Fuior, E. V. & Gafencu, A. V. Apolipoprotein C1: its pleiotropic use is not permitted by statutory regulation or exceeds the permitted
effects in lipid metabolism and beyond. Int. J. Mol. Sci. 20, 5939 use, you will need to obtain permission directly from the copyright
(2019). holder. To view a copy of this license, visit http://creativecommons.
69. Li, T., Chen, W. & Chiang, J. Y. PXR induces CYP27A1 and regulates org/licenses/by/4.0/.
cholesterol metabolism in the intestine. J. Lipid Res. 48, 373–384
(2007). © The Author(s) 2023
Nature Biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
Methods Components of the Spectra objective function
Overview of Spectra Broadly speaking, Spectra fits a set of factors and cell scores by mini-
Spectra (https://github.com/dpeerlab/spectra) grounds data-driven mizing an objective function with two components. The first compo-
factors with prior biological knowledge (Supplementary Fig. 1). First, nent of the objective function, ℒReconstruction , measures how well the
Spectra takes in prior biological information in the form of cell-type estimated model parameters can reconstruct (or predict) the observed
labels and explicitly models separate cell-type-specific factors that expression data using the set of all model parameters Θ. We write
can account for local correlation patterns. This explicit separation of ℒReconstruction(Θ) to emphasize that ℒReconstruction is a function that maps
cell-type-specific and global factors enables the estimation of factors a set of model parameters to a corresponding objective value. The
at multiple scales of resolution. Second, Spectra resolves indetermi- second component of the objective function measures how well the
nacy of the reconstruction loss function via a penalty derived from a set of model parameters Θ corresponds to our biological prior informa-
gene–gene knowledge graph that encourages solutions that assign tion. This second component is denoted ℒGraph(Θ). We weight this term
similar latent representations to genes with edges between them. by a user-defined hyperparameter λ, which allows a user to control the
To account for prior information of variable relevance and quality, level of confidence placed in the given biological prior information.
Spectra adaptively tunes its reliance on prior information based on The general form of the Spectra objective function is
concordance of the prior and observed expression data. Third, novel
factors are adaptively allocated when prior information is insufficient ℒ(Θ)=λℒReconstruction(Θ)+ℒGraph(Θ)
to explain the observed expression data.
In the first step of Spectra, a set of gene–gene similarity graphs is Below, we describe the precise functional forms of each of the objective
built by aggregating information across gene sets and/or other sources. function components.
This graph representation is flexible and can accommodate various
types of prior knowledge; gene sets can be incorporated into graphs ℒℒℒReconstruction (Θ): modeling gene expression as a low-rank product
by including edges between genes that are annotated to the same We assume that the expression variation observed in the count matrix
pathway, whereas existing datasets can be used to generate annota- is driven by variation in the activity of different biologically meaning-
tions by thresholding partial correlations or factor similarity scores. ful gene programs as well as technical variation that often involves
This representation lends computational convenience, as the graph highly expressed genes. Therefore, our model of gene expression
dimensions are fixed regardless of the size of the input annotations. needs to account for both components. In more detail, interpretation
The annotations are either labeled as cell-type-specific or have global of factors estimated from scRNA-seq data is often hindered by highly
scope. A separate graph is thus built for each cell type alongside a expressed genes, which factor analysis methods based on reconstruc-
global graph. tion loss functions must account for. Housekeeping genes required for
In the second step, Spectra learns a multidimensional parameter basal cellular function, such as GAPDH, ACTB and ribosomal genes, are
for each cell and each gene, representing each cell and each gene’s dis- expressed at high levels and hence unduly influence the reconstruc-
tribution over gene expression programs. Similarity of the parameters tion loss function despite the fact that their expression variance is
between genes indicates that these genes are likely to have an edge explained in large part by overall levels of transcription. As a result,
joining them, whereas similarity of the parameters between a cell and existing matrix decomposition methods tend to put high weight on
a gene indicates that the cell is likely to express that gene. Hence, the such nonspecifically expressed genes, although post hoc corrections
graph encodes the prior that genes with edges between them are likely can be applied for the interpretation of individual factors. However,
to be expressed by the same set of cells. In practice, we take several certain important cytokine genes (for example, IL4, IL6, IL2 and IL10),
additional steps to fulfill the desiderata: (1) factors not represented in chemokine receptor genes (CXCR1 and CXCR2) and transcription factor
the annotations can be discovered, (2) low-quality annotations can be genes (RORC and BATF3) are expressed in low mRNA copy numbers.
removed, and (3) discrete cell types are assumed to be fixed and known Normalization strategies that rescale features empirically tend to
and therefore not captured as factors by the model. amplify measurement uncertainty associated with lowly expressed
To avoid penalizing novel factors that have no relation to the anno- genes, leading matrix factorization methods to overfit and return
tations, we introduce a weighting matrix that scales the computation of low-quality gene expression programs. To address this, we introduce
gene–gene similarity scores by factor-specific weights that are learned gene scale factors g that are estimated from the data and allow the
j
from the data. Factors that have low weight are not used in computing model to explain high expression and variability of certain genes with-
edge probabilities, whereas factors with high weights influence the out increasing the magnitude of the gene factor weights. Because lowly
edge probabilities directly. Hence, Spectra can estimate similar param- expressed genes are correspondingly noisier, we bound the minimum
eters for two genes without forcing a high edge probability between gene scale factors below by a tuning parameter δ.
them as long as the factors corresponding to these genes also have By way of notation, X refers to the processed gene expression
low weight. These weights allow the addition of new, unbiased factors matrix, with entry X containing the gene expression value for cell i and
ij
that are not influenced by the input annotations. Importantly, weights gene j. The matrix X has n rows (the number of cells) and p columns
are estimated from the data, allowing for an adaptive determination (the number of genes). K refers to the number of gene expression
of the relative number of unbiased and biased factors. An estimated programs unless otherwise specified. Additionally, for a given cell
background rate of edges in the graph allows for the removal of anno- indexed by i, the cell loading (a set of weights across the set of factors)
tations with little supporting evidence from gene expression data. is denoted by α. The distribution across factors for gene j is denoted
i
Finally, Spectra explicitly separates global and cell-type-specific factors as θ j , which sums to 1 over K gene expression programs, ∑ K k=1 θjk=1.
by enforcing a cell-type-determined block sparsity pattern in the cell Unsubscripted variables refer to the collection containing all possible
loading matrix. Cell-type-specific factors capture within-cell-type vari- subscripts; for example, θ refers to the collection of all θ. The base
j
ation, whereas global factors capture any variation that is shared across expression model describing the gene expression measurement for
multiple cell types. To reduce the burden of modeling constitutively cell i and gene j is
expressed cell-type marker genes, each factor’s contribution to gene
expression is multiplied by a cell-type-specific gene weight. These 𝔼𝔼𝔼Xij]=(gj+δ)α⊤
i
θj
cell-type-specific gene weights explain away the influence of cell-type
marker genes and hence mitigate the tendency of these marker genes with g j ∈ [0, 1] a gene scaling parameter, αi∈ℝK + and θ j ∈ ΔK−1 (where ΔK−1
to influence the factors themselves. is the set of positive K − vectors that sum to 1). The low-rank
Nature Biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
decomposition of this expression model can be visualized in Supple- ℒℒℒGraph (Θ): modeling gene–gene relationships in relation to
mentary Fig. 2. expression data
In addition to faithful approximation of the input count matrix, we
Incorporating cell types into modeling expression variation. Because would also like interpretable factors that correspond known gene
expression variation is dominated by cell types, existing methods gener- programs and biological processes (prior). Therefore, the second
ally fit factors that are polluted with cell-type markers or alternatively component of our likelihood function is a penalty term that guides
must be run on a subset of the data. For example, TCR activation pro- the solution toward this prior. One aspect that makes Spectra unique is
grams (consisting of marker genes such as NFATC1 and NFATC2) are that it models this prior knowledge as a gene–gene community graph,
confounded with T cell identity, and existing factor analysis methods which provides both computational efficiency and flexibility to adapt
tend to return identity marker genes, such as CD3, CD4 and CD8. Simi- the graph structure to the data.
larly, programs representing metabolic pathways are often confounded In this graph, nodes represent individual genes, and edges
with plasmacytoid dendritic cell (IL3R and BDCA2) or B cell (CD19 and between genes occur when each gene has a similar distribution over
CD79A) identity marker genes. Although it is challenging to fit a biologi- factors. Communities within the graph, or densely connected subsets,
cally meaningful factor model, successful cell typing of scRNA-seq data then represent gene programs, whereas edges between communities
using clustering approaches is a solved problem for discrete cell types contain information about genes that participate in multiple gene
but not for intermediate states. Therefore, to mitigate this issue, Spectra programs. Providing an imperfect, partially known graph structure as
assumes that discrete cell types are known and therefore not captured input, we can constrain our matrix factorization solution to respect
as factors by the model; instead, Spectra explicitly fits cell-type-specific the structure to yield interpretable gene programs. A main advantage
and global factors, allowing Spectra to effectively deal with expression of this approach is its flexibility. Gene sets are naturally incorporated
variance at multiple scales. To perform this cell-type-integrative factor into a graph by forming fully connected cliques among members
analysis, for cell type c and cell i, the model is extended to of each set.
Further, more complex prior knowledge graph structures can
𝔼𝔼𝔼Xcij]=(gj+δ)α⊤
c,i,∶K
θj+(gcj+δ)α⊤
c,i,K+1∶
θcj be used as input, for example, arising from gene programs esti-
mated from a separate dataset or cell atlas. Most importantly, the
where c is the cell-type label for cell i, g is cell-type-specific gene scal- structure of this input gene–gene graph can be improved by fitting
cj
ing, and θcj∈ΔKc−1 is a cell-type-specific gene representation with it to the data and learning gene programs that are more faithful to
αc,i∈ℝK+Kc. Single-subscript variables, such as g
j
and θ
j
, denote global the data.
parameters, whereas the notation α indicates the first K elements of A second advantage of the graph prior is its scalability. Although
:K
a vector (typically denoting global elements), and α indicates the gene sets may be highly overlapping, especially when curated from
K+1:
tail of the vector from the K + 1st element (typically denoting several separate databases, this redundancy is eliminated when stor-
cell-type-specific elements). The threshold δ restricts the maximum ing information at the level of gene–gene relationships. Redundant
ratio of gene scaling factors to 1+δ. gene sets will be merged into highly overlapping communities, and
Spectra models the presencδe of gene programs with highly limited so two redundant gene sets can be approximately described by a
scope in that they can only be activated by a specific cell type, which single factor. A further computational advantage over gene set pri-
can be represented by a hard-coded sparsity pattern in the cell load- ors is that the dimensions of the graph are fixed as the size of gene
ing matrix (Supplementary Fig. 3). The cell-type-specific gene scal- set database increases, with only the number of edges increasing,
ings (g ) associated with these programs are encouraged to capture and eliminates the need for iterating over the gene set dimension.
cj
cell-type identity markers and constitutively active genes, enabling Finally, operations involving the graph are implemented via efficient
factors themselves to capture variation across cell types and within and parallelizable matrix multiplications with the graph adjacency
cell types (Supplementary Fig. 4). Spectra tends to assign constitu- matrix, thus allowing Spectra to efficiently scale to a large number
tive genes, such as EEF1A1 and ACTB, and identity marker genes, such of gene sets and cells (Fig. 2g).
as CD4 and CD3, high values of g. Lowly expressed genes important To encourage factors to capture our prior knowledge of gene pro-
j
for CD4+ T cell-specific gene programs, such as IL21, IL13 and IL6, are grams, we assume that binary gene–gene relationships are evidence of
often assigned small values of g, which allows Spectra to attend to gene a pair of genes having similar latent profiles. This assumption could be
j
expression differences that occur on a smaller scale (Supplementary incorporated by assuming a model for edge probabilities depending
Fig. 4). By default, Spectra runs with at least one cell-type-specific factor on the similarity scores 〈θ i , θ j〉 for genes i and j. However, the naive inner
per cell type so that global factors do not capture cell-type identities. product does not explicitly account for the fact that prior information
is invariably imperfect in systematic ways. First, at the level of entire
Determining cell-type granularity. Spectra can accommodate gene programs, not all gene programs are active in all datasets, and,
cell-type labels at any level of granularity, subject to a linear increase therefore, entire graph communities may be unnecessary for describ-
in computational burden with the number of cell types in the dataset. ing the observed expression data, while there are likely novel gene
Additionally, as the granularity increases, the effective sample size for programs observed in the expression data that are not represented
estimating cell-type-specific factors decreases, leading to potentially by communities in the graph. Also gene programs are imperfect due
lower-quality cell-type-specific factors. The correct cell-type granu- to inaccuracy of annotation, and, more frequently, gene programs
larity depends on the dataset and the specific scientific questions at differ across biological contexts, and our prior information is typically
hand. First, the analyst should incorporate cell types that are known to derived from a different biological context. Therefore, genes may be
be discrete and easily identifiable in the dataset via standard cluster- misclassified into gene sets to which they do not belong (correspond-
ing analysis (for example, T cells, B cells, myeloid cells and epithelial ing to noisy edge observations), or gene sets may be incomplete (cor-
cells). If cell subtypes exist that are not included as input to the model, responding to missing edges). Spectra addresses these issues in the
Spectra devotes factors to describing variation across these subtypes. following two ways: (1) adaptively modeling background noise in the
Moreover, if intermediate differentiation states between subtypes exist graph, allowing for the addition and removal of edges (Background
in the data, these subtypes should generally not be included as input to edge rates), and (2) tuning the weight of the prior gene–gene matrix
the model because (1) coarser cell-type-specific factors can describe through the incorporation of a weight matrix, termed the factor inter-
these intermediate states, and (2) delineating between subtypes via action matrix, into the inner product between gene representations
clustering may be inaccurate. θ and θ (see below).
i j
Nature Biotechnology
Article https://doi.org/10.1038/s41587-023-01940-3
The factor interaction matrix tunes the weight of the gene– the effect of low-quality edges in the prior graph by allowing edges
gene prior between genes that are in separate gene expression programs to arise
To understand the purpose of the factor interaction matrix, let us first with non-zero probability.
consider the ordinary inner product measuring gene–gene similarity
in terms of gene program representations: Full Spectra model
As a notation, we refer to the adjacency matrix of an input graph as
⟨θi,θj⟩=θi1θj1+⋯+θiKθjK A∈ℝp×p with element A
ij
= 1 if an edge exists between i and j and A
ij
= 0
otherwise. Following the discussion above, the Spectra generative
The maximum value of this product is 1 and is achieved only when model states (Supplementary Fig. 5)
gene i and gene j put all their weight into a single gene program. Con-
sider what happens if genes i and j are important components of a ℙ[Aij=1]=⟨θi,Bθj⟩
gene program that exists only in the expression data and not in our
prior information. Then, i and j are not connected in the graph, and In the full Spectra model, each gene has a separate representation per
so the inner product model encourages 〈θ i , θ j〉 ≈ 0. When 〈θ i , θ j〉 ≈ 0, cell type (in addition to its global representation), θ ci , where c indexes
genes i and j must be components of entirely separate programs. In into the possible cell types. To supervise these representations in a
this way, we see that the naive inner product discourages new factors cell-type-specific manner, the user (optionally) provides one graph
from being estimated from the expression data. Such an inner product for each cell type and a graph representing global gene–gene rela-
model estimates novel factors that are heavily biased by the graph. tionships (Supplementary Figs. 6 and 7). These graphs are modeled
Now, instead of the naive inner product, consider a weighted separately, where each graph’s edges can only be predicted using factor
product weighted by scalar values (b, b,…, b) that are between 0 and 1: representations specific to that cell type. The cell-type-specific graphs
1 2 K
are denoted A for cell type c, with A = 1 if there is a cell-type-specific
c c,ij
⟨θi,θj⟩ b =b1θi1θj1+⋯+bKθiKθjK annotation between genes i and j for cell type c. The cell-type-specific
graphs can only influence cell-type-specific factors and vice versa:
To model the data, we can adjust the values of (b,…, b ) to achieve
1 K
the best fit. Consider the same situation as above, where i and j are not ℙ[Ac,ij=1]=⟨θci,Bcθcj⟩
connected in the graph, but they are components of a gene program
supported by expression data alone. The product model again encour- diagrammed in Supplementary Fig. 7. Importantly, a separate factor
ages ⟨θi,θj⟩ b ≈0; however, now this constraint does not necessarily interaction matrix, B c , is learned for each cell type with a prior graph
encourage θ and θ to be dissimilar. To see this, suppose that θ = [1, 0, 0] provided.
i j i
and θ = [1, 0, 0]. If b = 0, then The computational cost of including granular cell-type-specific
j 1
prior information can be large, as each cell type requires its own graph.
⟨θi,θj⟩
b
=b11∗1+b20∗0+b30∗0
Background edge rates
=0
Realistic annotation graphs have several edges that are not supported
Hence, novel gene programs can be estimated as long as the value of b by expression data, and the model should be allowed the flexibility to
k
corresponding to that program is pushed toward 0. We can interpret attribute edges (or the lack thereof) in annotations to a background
gene programs corresponding to low values of b as novel and gene rate of noise. To allow flexibility in modifying the original graph, we
k
programs corresponding to high values of b as supported by prior incorporate background edge and non-edge rates κ and ρ that reflect
k
information. We could equivalently write each weight b as one of the noise rates in the observed graph. These parameters serve two separate
k
non-zero elements of a diagonal matrix purposes. First, these parameters deal with numerical stability issues by
moving probabilities away from 0 and 1. Second, the parameters control
⎡
b1
⎤ the rate that edges are added and removed from the original graph.
⎢ ⎥
B=⎢ ⋱ ⎥ Intuitively, our inference procedure examines whether a relationship
⎢ ⎥ (or lack of a relationship) in the prior knowledge graph is consistent with
⎣ bK⎦
expression data and if not can ascribe this relationship to random noise.
so that The generative process of our model is that with some probability
ρ, edges between gene i and j are blocked out and cannot occur irrespec-
⟨θi,Bθj⟩=⟨θi,θj⟩ b tive of the corresponding factor values θ i and θ j . If this does not occur,
an edge will be generated by random chance with probability κ. Finally,
=b1θi1θj1+⋯+bKθiKθjK
if neither of these events occur, an edge is generated according to the
In practice, we allow the off diagonals of this matrix B to be estimated factor similarity score 〈θ
i
, Bθ j〉. This yields the following distribution
as non-zero (Supplementary Fig. 5). The resulting matrix is termed the for the adjacency matrix:
factor interaction matrix.
Allowing off diagonals of the factor interaction matrix to be ℙ[Aij=1]=(1−κ)(1−ρ)θ⊤
i
Bθj+κ(1−ρ)
n
ov
o
e
n
r
-
l
z
a
e
p
r
p
o
i
s
n
e
g
r
g
ve
en
s
e
tw
se
o
t
p
s
u
w
r
i
p
th
o
o
se
u
s
t
.
f
F
o
i
r
r
c
s
i
t
n
,
g
it
s
a
h
ll
a
o
r
w
ed
s t
g
h
e
e
n
m
es
o
t
d
o
e
h
l
a
t
v
o
e
e
p
x
a
p
r
l
t
a
i
i
a
n
l
ℙ[Aij=0]=(1−κ)(1−ρ)(1−θ⊤
i
Bθj)+ρ
membership. For example, if two gene sets overlap but in reality repre-
sent two distinct biological processes that can be separated in the gene where κ and ρ are (cell-type-specific) background rates of 1 and 0 in
expression data, the model is not forced to assign partial membership the adjacency matrix, respectively. κ and ρ can be estimated from the
to overlapping genes but can fully assign genes to one of two programs. data or fixed to constants and treated as tunable hyperparameters.
To account for this, the off-diagonal element corresponding to this
pair of gene programs (B for programs k and l) can be estimated as Constructing the gene–gene prior graph
k,l
greater than 0. On real data, we see this occur for β-alanine metabolism In most applications, Spectra receives a set of gene sets rather than a
and fatty acid metabolism (Supplementary Fig. 6). Second, non-zero gene–gene graph as input, and the gene–gene graph is constructed
off-diagonal elements of the factor interaction matrix serve to mitigate from these gene sets. Large gene sets generally provide lower evidence
Nature Biotechnology
