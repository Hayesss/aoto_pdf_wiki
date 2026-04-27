---
source_path: /mnt/c/Users/Administrator/Zotero/storage/C4SKMEXZ/Kang 等 - 2025 - Improved reconstruction of single-cell developmental potential with CytoTRACE 2.pdf
ingested: 2026-04-23
sha256: 41b61bbf0947fe86
---

nature methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
Improved reconstruction of single-cell
developmental potential with CytoTRACE 2
Received: 20 March 2025 Minji Kang 1,2,3,14, Gunsagar S. Gulati 4,14, Erin L. Brown 1,2,14, Zhen Qi 1,14,
Susanna Avagyan2, Jose Juan Almagro Armenteros1,5, Rachel Gleyzer1,2,
Accepted: 2 September 2025
Wubing Zhang1,2, Chloé B. Steen6,7,8, Jeremy Philip D’Silva 1,2,
Published online: xx xx xxxx Janella Schwab 1,2,9, Michael F. Clarke 1,10, Aadel A. Chaudhuri 11,12 &
Aaron M. Newman 1,2,10,13
Check for updates
While single-cell RNA sequencing has advanced our understanding of
cell fate, identifying molecular hallmarks of potency—a cell’s ability to
differentiate into other cell types—remains a challenge. Here we introduce
CytoTRACE 2, an interpretable deep learning framework for predicting
absolute developmental potential from single-cell RNA sequencing data.
Across diverse platforms and tissues, CytoTRACE 2 outperformed previous
methods in predicting developmental hierarchies, enabling detailed
mapping of single-cell differentiation landscapes and expanding insights
into cell potency.
All cells, from the fertilized egg to its mature progeny, are hierarchically To overcome these challenges, we developed CytoTRACE 2, an
organized in multicellular life. Each cell has distinct potency, or ability interpretable deep learning framework for determining single-cell
to differentiate into specialized cell types, ranging from totipotent potency categories and absolute developmental potential from
(capable of generating an entire organism) and pluripotent (capable of scRNA-seq data. Unlike most deep learning methods9, CytoTRACE 2
generating all adult cells) to multipotent, oligopotent, unipotent and learns multivariate gene expression programs that are readily inter-
differentiated cells, each with increasingly restricted developmental pretable and enable accurate predictions of developmental potential.
potential1 (Fig. 1a). While lineage tracing, functional transplantation Moreover, it suppresses batch and platform-specific variation through
assays and single-cell genomics have expanded our understanding of multiple mechanisms, including competing representations of gene
cell potency2, there remains a need for interpretable methods that can expression and training set diversity (Methods). Our approach uncov-
learn developmental programs, predict potency states and generate ers cross-tissue correlates of cell potency and highlights the value of
insights applicable to regenerative and cancer biology. interpretable deep learning for characterizing single-cell develop-
We previously introduced CytoTRACE 1 (ref. 3), a computational mental states in health and disease (https://cytotrace2.stanford.edu).
method for predicting cellular maturity from single-cell RNA sequenc- To develop CytoTRACE 2, we curated an extensive atlas of human
ing (scRNA-seq) data, based on the number of genes expressed per and mouse scRNA-seq datasets with experimentally validated potency
cell. However, like other trajectory inference methods4–8, CytoTRACE levels, spanning 33 datasets, nine platforms, 406,058 cells and
1 provides predictions that are dataset-specific, making it difficult to 125 standardized cell phenotypes (Fig. 1b and Supplementary
unify results across datasets and contextualize them within the broader Table 1). Phenotypes were grouped into six broad potency categories—
framework of cellular potency. totipotent, pluripotent, multipotent, oligopotent, unipotent and
1Institute for Stem Cell Biology and Regenerative Medicine, Stanford University, Stanford, CA, USA. 2Department of Biomedical Data Science, Stanford
University, Stanford, CA, USA. 3Department of Computer Science, Stanford University, Stanford, CA, USA. 4Department of Medical Oncology, Dana-Farber
Cancer Institute, Boston, MA, USA. 5Department of Genetics, Stanford University, Stanford, CA, USA. 6Department of Medical Genetics, Oslo University
Hospital and University of Oslo, Oslo, Norway. 7Institute for Cancer Research, Oslo University Hospital and University of Oslo, Oslo, Norway. 8Precision
Immunotherapy Alliance, University of Oslo, Oslo, Norway. 9Department of Bioengineering, Stanford University, Stanford, CA, USA. 10Stanford Cancer
Institute, Stanford University, Stanford, CA, USA. 11Department of Radiation Oncology, Mayo Clinic, Rochester, MN, USA. 12Mayo Clinic Comprehensive
Cancer Center, Rochester, MN, USA. 13Chan Zuckerberg Biohub – San Francisco, San Francisco, CA, USA. 14These authors contributed equally: Minji Kang,
Gunsagar S. Gulati, Erin L. Brown, Zhen Qi. e-mail: amnewman@stanford.edu
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
differentiated—and further subdivided into 24 granular levels based developmental systems, termed ‘clades’, were held out from training.
on expected developmental order from lineage tracing and functional In all cases, results were well correlated with ground truth (Fig. 1f,
assays (Fig. 1b and Supplementary Tables 2 and 3). A training set of Extended Data Fig. 2d,e and Supplementary Tables 8 and 9), implying
93 cell phenotypes from 16 tissues and 13 studies was used to develop that potency-related biology is conserved across datasets. We also
the model, with the remaining data reserved for performance found that CytoTRACE 2 is resistant to moderate annotation errors and
evaluation (Fig. 1b and Supplementary Table 1). performs reliably under practical data limitations (Extended Data Fig. 3
CytoTRACE 2 decodes developmental potential using a novel, and Supplementary Note).
explainable deep learning architecture called a gene set binary A key advantage of CytoTRACE 2 is its ability to predict absolute
network (GSBN). Inspired by binarized neural networks10, GSBNs developmental potential on a continuous scale from 1 (totipotent) to 0
assign binary weights (0 or 1) to genes, identifying highly discrimi- (differentiated), which enables cross-dataset comparisons and avoids
native gene sets that define each potency category (Fig. 1c and imposing a developmental order where none exists. For example,
Extended Data Fig. 1a). Multiple gene sets can be learned for each unlike its predecessor, CytoTRACE 2 corroborated a pluripotency
potency group, and the informative genes driving model predictions program in cranial neural crest cell precursors11 and correctly dis-
can be easily extracted—an advantage over conventional deep learn- tinguished datasets with and without immature cells12,13 (Fig. 1g and
ing architectures. As such, CytoTRACE 2 provides two key outputs Extended Data Fig. 4). It also outperformed other methods3,14–20 in
for each single-cell transcriptome: (1) the potency category with ordering mouse single-cell transcriptomes from six datasets2,21–25 across
maximum likelihood and (2) a continuous ‘potency score’ gener- 62 developmental time points (Extended Data Fig. 5a–c) and accurately
ated by integrating GSBN predictions across potency categories captured the progressive decline in potency across 258 evaluable
and calibrating the range from 1 (totipotent) to 0 (differentiated) phenotypes during mouse development (Extended Data Fig. 5d,e)—
(Fig. 1c, Extended Data Fig. 1a and Supplementary Tables 2–4). Based on without requiring data integration or batch correction. CytoTRACE 2
the assumption that transcriptionally similar cells occupy related potency predictions also aligned with known leukemic stem cell
differentiation states, CytoTRACE 2 also leverages Markov diffusion signatures in acute myeloid leukemia (Extended Data Fig. 6a)26 and
combined with a nearest neighbor approach to smooth individual identified known multilineage potential in oligodendroglioma27,
potency scores (Extended Data Fig. 1b,c). highlighting its applicability to cancer (Extended Data Fig. 6b and
Having compiled a compendium of ground truth datasets, we Supplementary Table 10).
evaluated the performance of CytoTRACE 2 by assessing both the Next, we benchmarked CytoTRACE 2 against multiple strategies
accuracy of potency predictions and the ordering of known develop- for cell potency classification and developmental hierarchy infer-
mental trajectories. We used two definitions of development order- ence (Supplementary Table 11). CytoTRACE 2 outperformed eight
ing: ‘absolute order’, which compares predictions to known potency state-of-the-art machine learning methods28–32 for cell potency clas-
levels across datasets, and ‘relative order’, which ranks cells within sification in 33 datasets, achieving a higher median multiclass F1 score
each dataset from least to most differentiated (Extended Data Fig. 1d and lower mean absolute error (Extended Data Fig. 7). Moreover, it
and Supplementary Tables 2–4). The agreement between known and surpassed eight developmental hierarchy inference methods for
predicted developmental orderings was quantified using weighted cross-dataset (absolute) and intra-dataset (relative) performance3,14–20,
Kendall correlation to ensure balanced evaluation and minimize bias demonstrating over 60% higher correlation, on average, for recon-
(Supplementary Table 5). structing relative orderings in 57 developmental systems, including
We started by evaluating model hyperparameters through data from Tabula Sapiens33 (Fig. 1h,i and Supplementary Tables 12
cross-validation and observed minimal performance variation across and 13). Similar results were observed when comparing CytoTRACE 2
a wide range of values (Extended Data Fig. 1e,f and Supplementary against nearly 19k annotated gene sets34–36 (Fig. 1i and Supplementary
Table 6). Based on this, we selected stable hyperparameters and Table 13) and scVelo5, a generalized RNA velocity model for predicting
retrained the model. On the training data, we demonstrated that future cell states (Extended Data Fig. 8 and Supplementary Table 14).
CytoTRACE 2 achieves high accuracy in distinguishing absolute Previous genomic studies of stemness largely focused on pluri-
potency for broad potency labels (Fig. 1d). potency, with limited insight into other potency states. Given the
To validate our approach, we next extended our analysis to inherent interpretability of our GSBN design, we next explored the
unseen data, comprising 14 held-out datasets spanning nine tissue molecular programs driving potency predictions (Fig. 2a). Across our
systems, seven platforms and 93,535 evaluable cells. Performance on potency atlas, GSBN modules produced a cohesive gradient of differen-
broad and granular potency labels was consistently high in testing tiation states (Fig. 2b and Extended Data Fig. 9a,b). The top-ranking
(Fig. 1d,e) and robust to differences in species, tissues, platforms or genes showed conserved signatures across species, platforms and
phenotypes that were absent during training (Extended Data Fig. 2a–c developmental clades, identifying both positive and negative cor-
and Supplementary Table 7). To rigorously assess generalizability, relates of cell potency (Fig. 2c and Supplementary Tables 15 and 16).
we retrained CytoTRACE 2 on different subsets of the potency atlas, Given these results, we hypothesized that CytoTRACE 2 might
including random train–test splits and scenarios where distinct enrich for key potency-specific factors. Indeed, the core transcription
Fig. 1 | Development and benchmarking of CytoTRACE 2. a, Overview of cell training. For d–f, concordance with ground truth was assessed using weighted
potency across six developmental categories. b, Summary of the 33-dataset Kendall correlation (τ) applied to single cells, with significance assessed by
single-cell potency atlas. c, Schematic of the CytoTRACE 2 model. Toti., two-sided z-test. Box plots show medians, quartiles and 1.5 × interquartile range
totipotent; Pluri., pluripotent; Multi., multipotent; Oligo., oligopotent; Uni., (IQR). g, Uniform Manifold Approximation and Projection (UMAP) of three
unipotent; Diff., differentiated. d, CytoTRACE 2 performance across six broad held-out datasets showing ground truth (top), CytoTRACE 2 (middle)
potency categories in training and held-out test sets, with mean potency scores and CytoTRACE 1 (bottom). h, Violin plots comparing nine methods for
shown for each standardized phenotype–dataset pair (circles). e, CytoTRACE 2 reconstructing 57 developmental systems. P values were calculated by two-sided
performance across 17 evaluable granular potency levels in held-out test data. Wilcoxon tests against CytoTRACE 2; **P < 0.01; ****P < 0.0001. i, Performance
Points denote mean potency score per phenotype; large circles indicate the comparison with eight previous methods and 18,706 gene sets in the test
median across these points for each granular potency level. Thick black lines set (left) and Tabula Sapiens (right) using weighted τ to assess absolute
(x axis) separate broad potency categories. A linear regression line with 95% (six broad potency levels) and relative order (median correlation across
confidence band is shown. f, Same as e, but using a leave-clade-out strategy, individual trajectories). a and c were created using BioRender.com.
where each of 19 developmentally distinct clades (b) was held out during
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
1.0
0.8
0.6
0.4
0.2
0
Nature Methods
erocs
ycnetoP
1.0
0.8
0.6
0.4
0.2
0
erocs
ycnetoP
a b
Developmental
potential
Totipotent
Zygote (organism)
Two-cell
Four-cell
Eight-cell Embryonic Pluripotent
stem cell (germ layers)
... Multipotent
(>3 lineages)
Neural Hematopoietic Intestinal
stem cell stem cell stem cell
Oligopotent
... (2 or 3 lineages)
... Myeloid
progenitor Unipotent Motor neuron (1 lineage)
progenitor
... ... Differentiated (mature)
Motor Erythrocyte NeutrophilPaneth Goblet neuron cell cell
c
Ground truth potency
Mouse cranial Human Mouse mature
neural crest bone marrow neural cell types (Smart-seq2) (CITE-seq) (10x)
oyrbme
ylraE
metsys
suovreN
enummI enitsetnI evitcennoC gnuL tsaerB eugnot/nikS elcsuM saercnaP reddalB lailehtodnE yendiK reviL enircodneorueN aehcarT enoB alludem
lanerdA
Human embryo (Tang et al.) Mouse embryo 1 (Tang et al.)
Direct in vitro neuron (inDrop)
Mesoderm (C1) Standard in vitro neuron (inDrop)
HSPCs (C1)
Immune cell atlas (10x) Intestine (drop−seq)
Intestine (smart−seq2) Tabula Muris (10x)
Tabula Muris (smart−seq)
Bone marrow (10x)
Bone marrow (smart−seq2)
Peripheral blood (10x)
AT2/AT1 lineage (C1) Dendritic cells (C1)
Human breast 1 (10x)
Human breast 1 (C1)
Human breast 2 (10x)
Mouse embryo 3 (smart−seq)
Mouse embryo 2 (smart−seq2) Neural crest (smart−seq2)
BM−MNC (CITE−seq)
HSC development (smart−seq2)
HSCs and MPPs (indrop) Lgr5−CreER intestine (CEL−seq)
Mouse neurogenesis (10x) Pancreas (10x) Peripheral glia (smart−seq2)
Retinal neurons (10x)
Skeletal stem cell (C1)
Cord blood (CITE−seq)
Mouse mature neural cell types (10x)
1 2 3 4 5 6 7 8 9 01 11 21 31 41 51 61 71 81 91 02 12 22 32 42
Single-cell potency atlas (n = 33 scRNA-seq datasets)
Ground truth potency Developmental cladesCohort
Number cells analyzed
>1,000
100 10
Training
Test
Broad potency level Granular potency level
Totipotent Oligopotent
Broad potency level Pluripotent Unipotent Multipotent Differentiated
d
Absolute order prediction (n = 6 broad potency levels)
Training set
(n = 19 datasets)
1.0
0.8
0.6
0.4
0.2 0
erocs
ycnetoP
Test set Predicted
(n = 14 held-out datasets) potency
Toti.
Pluri.
Multi.
Oligo.
Uni. Diff.
Ground truth potency
Number of cells 100 500 1,000 5,000
Predicted potency
Toti.
Pluri.
Multi.
Oligo.
Uni.
Diff.
Ground truth potency
(n = 17 granular potency levels)
1 2 3 4 5 6 21 31 41 51 61 71 81 12 22 32 42 1 2 3 4 5 6 7 8 9 01 11 21 31 41 51 61 71 81 91 02 12 22 32 42
e f
Absolute order prediction
(n = 14 held-out test datasets)
Test set and Tabula Sapiens Performance across ~19k measures and 62 developmental systems
(n = 57 developmental systems)
Median τ 0.53 0.33 0.31 0.17 0.17 0.16 0.16 0.15 0.10
1.0 ** ** ************************
0.5
0
–0.5
–1.0
CytoTR C A y C t E o T 2 RACE S 1 C sc E T N o T u ( r C S C C A E T N ) T (SR F ) itDevo SLICE Ste mI m D RNAsi
noitciderp
redro
evitaleR
)τ(
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 Absolute order prediction Absolute order prediction (τ) (τ)
noitciderp
redro
evitaleR
)τ
naidem(
g
h i
Test set Tabula Sapiens
(n = 14 held-out datasets) (n = 48 tissue, platform pairs)
0.4
0.2
0
0 0.2 0.4
1 ECARTotyC Less diff.
More
diff.
hturt
dnuorG2
ECARTotyC
Dataset
Potency category
Gene set binary network modules
Toti.
Totipotent
Pluripotent Potency Pluri.
Multipotent probability Multi.
Oligopotent Oligo.
Unipotent Uni.
GS1 Potency score
Calculates enrichments Predicts potency score
Toti.
Pluri.
Multi. Oligo.
Uni.
Diff.
Toti.
Pluri.
Multi.
Oligo.
Uni.
Diff.
... ... ... ...
Binary weight matrix
...
... ...
... ...
Gene sets
seneG
X1 Enrichment layers
X2
X4 XN ...
τ = 0.82 τ = 0.81
Differentiated Diff. P < 2.2 × 10–16 P < 2.2 × 10–16
GS2 GST
X3 G G S S 1 1G G S S 2 2 G G S S T T 1 Toti.
GS1GS2 GST Pluri. Multi. 0.5 GS1GS2 GST Oligo. Uni.
Diff.
0
1 Learns gene sets 2 3
Leave-clade-out model
(n = 33 datasets) Predicted potency
τ = 0.86 τ = 0.70 Toti.
P < 2.2 × 10−16 P < 2.2 × 10−16 Pluri.
Multi.
Oligo.
Uni.
Diff.
Ground truth potency
(n = 24 granular potency levels)
CytoTRACE 2
CytoTRACE 1
SCENT (CCAT)
SCENT (SR)
FitDevo SLICE
StemID scTour
mRNAsi
Gene sets (n = 18,706)
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
Training set Test set
0.6
0.4
0.2
0
–0.2
–0.4
Toti P p l o u t r e i M p n o u t t lt O e ip n li t o g t o e p n U D o t n t i i ff e p n e o r t t e e n n t t ia T t o ed ti P p l o u t r e i M p n o u t t lt O e ip n li t o g t o e p n U D o t n t i i ff e p n e o r t t e e n n t t iated
Potency
Nature Methods
erocs
tnemhcirnE
a
UMAP 1
UMAP 1
CytoTRACE 2
0.3 0.2
0.1
0
−0.1
−0.2
0.1 0
−0.1 −0.2 −0.3 −0.4
2 PAMU
2 PAMU
Potency score Average expression of top 500 positive and negative
(CytoTRACE 2) potency-associated genes in training and test sets
Toti. Pluri. Multi. Oligo. Uni. Diff.
1.0Toti.
0.5 0 Diff.
Ground truth
(Potency category)
Toti.
Pluri.
Multi.
Oligo. Uni.
Diff.
Schema for CRISPR screen (Haney et al.)
~7,000 CRISPR KO pool
c-Kit+ mouse HSCs in culture
Transplantation into Hematopoietic
irradiated mice reconstitution and
measure gRNA distribution
Pro-hematopoiesis Anti-hematopoiesis
gRNA (n = ~7,000)
fo tnemhcirnE srekram
evitisop
Enrichment of multipotency-associated
markers by effect score in CRISPR screen
fo tnemhcirnE
srekram
evitagen
... ... ... ...
KO promotes diff. KO inhibits diff.
gRNA ranked by effect score
(n = 5,757)
... ... ... ... ...
GSBN Feature importance matrix
Learned
gene sets
Visualization and
interpretation of learned
gene sets
seneG )172,41
=
n(
.itoT .irulP .itluM .ogilO .inU .ffiD
Potency
...
Frequency of genes
per GSBN module
with directionality (%)
... ... ... ... ...
... ... ... ...
–100 0 100
... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ...
b c
d e
n = 237 phenotype, species, platform combinations
Cohort Tissue
P = 0.040, Q = 0.043 Train Adrenal medulla Endothelial Muscle
Test Bladder Immune Nervous system
NES = 1.36 Breast Intestine Neuroendocrine
Bone Kidney Pancreas
Connective Liver Skin/tongue
P = 0.043, Q = 0.043 Early embryo Lung Trachea
Species Platform Average expression NES = –1.36 Human Plate-seq
Mouse Droplet-seq –1.5 1.5
1.6
1.2
0.8
Pathways (n = 537)
SEN
Lipid uptake
Enrichment in Phospholipid
multipotent genes formation
Cholesterol metabolism
0.6 α-Linolenic acid Saturated fatty acids 0.4 ELOVLs Fatty acid SCDs
0.2 FADSs synthesis FADSs 0
Polyunsaturated Monounsaturated
fatty acids fatty acids
Rank in cholesterol met. 18 3 (GSEA, n = 48) Rank in multipotency 1,449 (CytoTRACE 2, n = 14,271)
erocs
tnemhcirnE
Pathways enriched in multipotency UFA genes Conservation of UFA genes across
tissues in training and test sets
**** ****
Q = 0.001
Pos. markers Neg. markers
of multipotency of multipotency
Genes ranked by multipotency scores from CytoTRACE 2 154
UFA expression in mouse UFA expression in mouse intestinal crypts and villi (RNA ISH)
hematopoietic subsets (qPCR)
1.00
0.75
0.50
0.25 Multi. HSC
MPP
Oligo.
0 CMPCLP
Diff.
HSC/
MPP
C
MP CLP
T
cells
B
cells T B
Phenotype
noisserpxe
dezilamroN
DAPI Lgr5 Fgfbp1 Mki67 Fgfbp1 Fads1 Fads2 Scd2
Gene
Fads1 Diff.
Fads2
Scd2
Uni.
Potency Multi.
E-cad Lgr5 Mki67 Fgfbp1 Fads1 Fads2 Scd2
Potency Multi. Fgfbp1+
* * * * *
Lgr5+ * * * * *
* * * * *
sulliV
tpyrC
CBC
Framework for model interpretability
f g h
i j
srekram
evitisoP
Potency
Cohort Tissue Species Platform Totipotent
Pluripotent
Multipotent
Oligopotent
Unipotent
Differentiated
srekram
evitageN
Totipotent
Pluripotent
Multipotent
Oligopotent
Unipotent
Differentiated
enoz
AT
KO promotes HSC diff.
KO inhibits HSC diff.
Fads1 Fads2 Scd2
1 14
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
Fig. 2 | Model interpretability and cross-tissue signatures of cell potency. 237 pseudo-bulk samples, colored by tissue type as in c. ****P < 0.0001 (one-sided
a, Schematic for characterizing CytoTRACE 2 gene sets and feature importance. permutation testing). Box plots show medians, quartiles and 1.5 × IQR. i, qPCR of
b, UMAP of gene set expression levels in training–test sets, aggregated in a UFA genes in FACS-purified mouse hematopoietic subsets (n = 3), normalized to
0.5 × 0.5 grid, colored by CytoTRACE 2 (top) or ground truth potency (bottom). HSC/MPP; Actb as internal control. MPP, multipotent progenitor; CMP, common
c, Expression of top 500 positive (pos.) and negative (neg.) markers per potency myeloid progenitor; CLP, common lymphoid progenitor. Violin plots show
category, shown across 237 pseudo-bulks aggregated by phenotype, species median and range. j, In situ mRNA imaging of mouse jejunum (top) shows spatial
and platform from training–test sets. d, Overview of a CRISPR knockout (KO) expression of multipotent (Lgr5 and Fgfbp1), proliferation (Mki67), and UFA
screen assessing in vivo differentiation effects in hematopoietic stem cells (Fads1, Fads2 and Scd2) marker genes in crypts and villi. Higher magnification
(HSCs)38. e, Enrichment of top CytoTRACE 2 multipotency markers among genes views (bottom) highlight boxed regions. Cell boundaries were visualized with
whose knockout promotes or inhibits HSC differentiation (from d), using GSEA. E-cadherin immunostaining; asterisks mark representative Lgr5+ crypt base
f, GSEA of 537 pathways in genes ranked by multipotency scores, highlighting columnar (CBC) cells. TA, transit-amplifying. Scale bars, 50 μm (top), 10 μm
‘cholesterol metabolism’. g, Top: overview of UFA pathways, inspired by ref. 42. (bottom). Images are representative of three mice. Images in a, d, g, i, j were
Bottom: top UFA biosynthesis genes (Fads1, Fads2 and Scd2) ranked by GSEA and created using BioRender.com. NES, normalized enrichment score.
CytoTRACE 2 multipotency scores). h, Single-sample GSEA of UFA genes across
factors Pou5f1 and Nanog37 ranked within the top 0.2% of pluripotency trained on human and mouse data, ortholog mapping may expand its
genes (Supplementary Table 15). To further explore this hypothesis, applicability to other species. Given its demonstrated advantages, we
we analyzed data from a large-scale CRISPR screen, in which ~7,000 anticipate that CytoTRACE 2 will have immediate utility for improving
genes in multipotent mouse hematopoietic stem cells were individually our understanding of cell potency, with implications for the identifi-
knocked out and assessed for developmental consequences in vivo38 cation of novel biomarkers and therapeutic targets in diseases where
(Fig. 2d). Among the 5,757 genes overlapping CytoTRACE 2 features, altered developmental hierarchies play a role.
the top 100 positive multipotency markers were enriched for genes
whose knockout promotes differentiation, whereas the top 100 nega- Online content
tive markers were enriched for genes whose knockout inhibits dif- Any methods, additional references, Nature Portfolio reporting sum-
ferentiation (Q = 0.04; Fig. 2e and Extended Data Fig. 9c). This trend maries, source data, extended data, supplementary information,
was consistent across different numbers of top markers and highly acknowledgements, peer review information; details of author contri-
specific for multipotency, underscoring the fidelity of learned potency butions and competing interests; and statements of data and code avail-
representations (Extended Data Fig. 9d). ability are available at https://doi.org/10.1038/s41592-025-02857-2.
To more deeply analyze multipotency in mouse and human tissues
and explore the potential of CytoTRACE 2 for biomarker discovery, we References
next applied pathway enrichment analysis to genes ranked by feature 1. Zakrzewski, W., Dobrzyński, M., Szymonowicz, M. & Rybak, Z.
importance. Remarkably, cholesterol metabolism emerged as a leading Stem cells: past, present, and future. Stem Cell Res. Ther. 10, 68
multipotency-associated pathway (Fig. 2f, Extended Data Fig. 9e and (2019).
Supplementary Table 17). Within this pathway, three genes related to 2. Qiu, C. et al. A single-cell time-lapse of mouse prenatal
unsaturated fatty acid (UFA) synthesis (Fads1, Fads2 and Scd2) were development from gastrula to birth. Nature 626, 1084–1093
among the top-ranking markers (Fig. 2g). These genes were consistently (2024).
enriched in multipotent cells across 125 phenotypes in our potency 3. Gulati, G. S. et al. Single-cell transcriptional diversity is a hallmark
atlas (Fig. 2h; train–test area under the curve (AUC) values of 0.87 and of developmental potential. Science 367, 405–411 (2020).
0.92, respectively). 4. La Manno, G. et al. RNA velocity of single cells. Nature 560,
To experimentally confirm these findings, we performed quantita- 494–498 (2018).
tive PCR on mouse hematopoietic cells sorted into multipotent, oligo- 5. Bergen, V., Lange, M., Peidli, S., Wolf, F. A. & Theis, F. J.
potent, and differentiated subsets (Fig. 2i and Extended Data Fig. 10a,b) Generalizing RNA velocity to transient cell states through
and multiplexed in situ mRNA imaging on mouse intestinal epithelium dynamical modeling. Nat. Biotechnol. 38, 1408–1414 (2020).
co-stained with multipotency markers, Lgr539 and Fgfbp140 (Fig. 2j and 6. Qiu, X. et al. Reversed graph embedding resolves complex
Extended Data Fig. 10c–e). In both approaches, Fads1, Fads2 and Scd2 single-cell trajectories. Nat. Methods 14, 979–982 (2017).
showed reproducible and preferential expression in multipotent cells 7. Lange, M. et al. CellRank for directed single-cell fate mapping.
(Fig. 2i,j and Extended Data Fig. 10). While fatty acid metabolism has Nat. Methods 19, 159–170 (2022).
been linked to stem cell biology41, no study has specifically attrib- 8. Weiler, P., Lange, M., Klein, M., Pe’er, D. & Theis, F. CellRank 2:
uted lipid metabolism genes to distinct potency levels. Therefore, unified fate mapping in multiview single-cell data. Nat. Methods
CytoTRACE 2 provides a framework to uncover molecular relationships 21, 1196–1205 (2024).
and facilitate new hypotheses and discoveries. 9. Rudin, C. Stop explaining black box machine learning models
In summary, CytoTRACE 2 is an interpretable deep learning for high stakes decisions and use interpretable models instead.
framework that predicts cell potency and continuous differentia- Nat. Mach. Intell. 1, 206–215 (2019).
tion states from scRNA-seq data. Unlike previous methods, it links 10. Hubara, I., Courbariaux, M., Soudry, D., El-Yaniv, R. & Bengio, Y.
stemness and pseudotime to absolute developmental potential, offer- Binarized neural networks. In Advances in Neural Information
ing cross-dataset compatibility and transparency into the molecular Processing Systems 29 (eds Lee, D. et al) (Curran Associates,
profiles driving its predictions. Nonetheless, this study has several limi- 2016).
tations. Like all supervised machine learning approaches, CytoTRACE 11. Zalc, A. et al. Reactivation of the pluripotency program precedes
2 depends on the quality and breadth of its training data, although formation of the cranial neural crest. Science 371, eabb4776
robust results were observed across diverse training–test splits, and (2021).
moderate labeling variation was well tolerated. Performance may 12. Stuart, T. et al. Comprehensive integration of single-cell data. Cell
decline when analyzing cells with very low RNA content or number 177, 1888–1902.e1821 (2019).
of expressed genes (Extended Data Fig. 3). While some phenotypes 13. Zheng, X. et al. Massively parallel in vivo Perturb-seq reveals
were misclassified in held-out data, absolute errors remained low and cell-type-specific transcriptional networks in cortical
outcompeted existing methods. Finally, although the current model is development. Cell 187, 3236–3248 e3221 (2024).
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
14. Teschendorff, A. E., Maity, A. K., Hu, X., Weiyan, C. & Lechner, M. 31. Tan, Y. & Cahan, P. SingleCellNet: a computational tool to classify
Ultra-fast scalable estimation of single-cell differentiation single cell RNA-seq data across platforms and across species.
potency from scRNA-seq data. Bioinformatics 37, 1528–1534 Cell Syst. 9, 207–213 e202 (2019).
(2020). 32. Kiselev, V. Y., Yiu, A. & Hemberg, M. scmap: projection of
15. Teschendorff, A. E. & Enver, T. Single-cell entropy for accurate single-cell RNA-seq data across data sets. Nat. Methods 15,
estimation of differentiation potency from a cell’s transcriptome. 359–362 (2018).
Nat. Commun. 8, 15599 (2017). 33. Consortium, T. T. S. et al. The Tabula Sapiens: a multiple-organ,
16. Herman, J. S., Sagar & Grün, D. FateID infers cell fate bias in single-cell transcriptomic atlas of humans. Science 376,
multipotent progenitors from single-cell RNA-seq data. Nat. eabl4896 (2022).
Methods 15, 379–386 (2018). 34. Gerstein, M. B. et al. Architecture of the human regulatory
17. Guo, M., Bao, E. L., Wagner, M., Whitsett, J. A. & Xu, Y. SLICE: network derived from ENCODE data. Nature 489, 91–100 (2012).
determining cell differentiation and lineage based on single cell 35. Lachmann, A. et al. ChEA: transcription factor regulation
entropy. Nucleic Acids Res. 45, e54 (2017). inferred from integrating genome-wide ChIP-X experiments.
18. Malta, T. M. et al. Machine learning identifies stemness features Bioinformatics 26, 2438–2444 (2010).
associated with oncogenic dedifferentiation. Cell 173, 338–354. 36. Liberzon, A. et al. The Molecular Signatures Database hallmark
e315 (2018). gene set collection. Cell Syst. 1, 417–425 (2015).
19. Li, Q. scTour: a deep learning architecture for robust inference 37. Loh, Y. H. et al. The Oct4 and Nanog transcription network
and accurate prediction of cellular dynamics. Genome Biol. 24, regulates pluripotency in mouse embryonic stem cells. Nat.
149 (2023). Genet. 38, 431–440 (2006).
20. Zhang, F. et al. FitDevo: accurate inference of single-cell 38. Haney, M. S. et al. Large-scale in vivo CRISPR screens identify
developmental potential using sample-specific gene weight. SAGA complex members as a key regulators of HSC lineage
Brief. Bioinform. 23, bbac293 (2022). commitment and aging. Preprint at bioRxiv https://doi.
21. Cheng, S. et al. Single-cell RNA-seq reveals cellular heterogeneity org/10.1101/2022.07.22.501030 (2022).
of pluripotency transition and x chromosome dynamics during 39. Barker, N. et al. Identification of stem cells in small intestine and
early mouse development. Cell Rep. 26, 2593–2607.e2593 (2019). colon by marker gene Lgr5. Nature 449, 1003–1007 (2007).
22. Deng, Q., Ramsköld, D., Reinius, B. & Sandberg, R. Single-cell 40. Capdevila, C. et al. Time-resolved fate mapping identifies the
RNA-seq reveals dynamic, random monoallelic gene expression intestinal upper crypt zone as an origin of Lgr5+ crypt base
in mammalian cells. Science 343, 193–196 (2014). columnar cells. Cell 187, 3039–3055 e3014 (2024).
23. Mohammed, H. et al. Single-cell landscape of transcriptional 41. Kang, J. X., Wan, J. B. & He, C. Concise review: regulation of stem
heterogeneity and cell fate decisions during mouse early cell proliferation and differentiation by essential fatty acids and
gastrulation. Cell Rep. 20, 1215–1228 (2017). their metabolites. Stem Cells 32, 1092–1098 (2014).
24. Pijuan-Sala, B. et al. A single-cell molecular map of mouse 42. Jin, H.-R. et al. Lipid metabolic reprogramming in tumor
gastrulation and early organogenesis. Nature 566, 490–495 microenvironment: from mechanisms to therapeutics. J. Hematol.
(2019). Oncol. 16, 103 (2023).
25. Qiu, C. et al. Systematic reconstruction of cellular trajectories
across mouse embryogenesis. Nat. Genet. 54, 328–341 (2022). Publisher’s note Springer Nature remains neutral with regard to
26. Zeng, A. G. X. et al. A cellular hierarchy framework for jurisdictional claims in published maps and institutional affiliations.
understanding heterogeneity and predicting drug response in
acute myeloid leukemia. Nat. Med. 28, 1212–1223 (2022). Open Access This article is licensed under a Creative Commons
27. Tirosh, I. et al. Single-cell RNA-seq supports a developmental Attribution 4.0 International License, which permits use, sharing,
hierarchy in human oligodendroglioma. Nature 539, 309–313 adaptation, distribution and reproduction in any medium or format,
(2016). as long as you give appropriate credit to the original author(s) and the
28. Abdelaal, T. et al. A comparison of automatic cell identification source, provide a link to the Creative Commons licence, and indicate
methods for single-cell RNA sequencing data. Genome Biol. 20, if changes were made. The images or other third party material in this
194 (2019). article are included in the article’s Creative Commons licence, unless
29. Cao, X. et al. A systematic evaluation of supervised machine indicated otherwise in a credit line to the material. If material is not
learning algorithms for cell phenotype classification using included in the article’s Creative Commons licence and your intended
single-cell RNA sequencing data. Front. Genet. 13, 836798 use is not permitted by statutory regulation or exceeds the permitted
(2022). use, you will need to obtain permission directly from the copyright
30. Alquicira-Hernandez, J., Sathe, A., Ji, H. P., Nguyen, Q. & holder. To view a copy of this licence, visit http://creativecommons.
Powell, J. E. scPred: accurate supervised method for cell-type org/licenses/by/4.0/.
classification from single-cell RNA-seq data. Genome Biol. 20,
264 (2019). © The Author(s) 2025
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
Methods and test), developmental maturity, lineage contributions and sup-
Ethical compliance porting evidence. This format allows for consistent annotation and
All animal procedures were performed in compliance with ethical comparison across datasets. For full details of potency annotations and
regulations and conducted according to a protocol approved by the associated rationale, see ‘Potency annotation scheme’ (Supplementary
Stanford University Administrative Panel for Laboratory Animal Care Note) and Supplementary Tables 2–4.
committee (protocol no. 10868).
Training and test datasets. Using the abovementioned criteria, we
Single-cell potency atlas assembled a 33-dataset potency atlas (Fig. 1b), from which we selected
Developmental potency reflects a cell’s capacity to differentiate into a training cohort consisting of seven human and 12 mouse scRNA-seq
various cell types, with six widely recognized categories in stem cell datasets from 13 studies (Supplementary Table 1). We ensured that all
biology: totipotency, pluripotency, multipotency, oligopotency, six broad potency categories were represented in both species along
unipotency, and differentiated (Fig. 1a,b and Supplementary Note). with a diverse array of biological (for example, tissue types) and tech-
These broad classifications are based on decades of research, including nical characteristics (for example, sequencing platforms). As part of
lineage tracing, transplantation and colony-formation experiments this effort, and to align with precedent in the field, we incorporated
across multiple tissues and species. Each category represents a pro- all human and mouse scRNA-seq datasets (n = 13) with annotatable
gressively restricted ability to generate downstream cell types, from potency categories analyzed by Gulati et al.3. To broadly cover tissue
totipotent cells capable of forming all embryonic and extra-embryonic types, we also included cell phenotypes from the Tabula Muris
lineages to unipotent cells restricted to producing a single mature cell scRNA-seq atlas43 for which potency categories could be determined
type; however, as developmental potential exists on a continuum, we (15 tissue types and 43 phenotypes). The resulting training cohort
also devised a more granular classification system, as described in encompasses 312,523 cells, 16 tissue types, 93 phenotypes and six
Supplementary Note and Supplementary Tables 2 and 3. scRNA-seq platforms (Fig. 1b).
Of note, classically defined potency levels are not directly anno- The remaining datasets served as a held-out test cohort, which
tated in publicly available scRNA-seq datasets. Therefore, to train, mirrors the training cohort with respect to species representation in
validate and benchmark CytoTRACE 2, we downloaded and curated each broad potency category (Supplementary Table 1). Consisting of
33 human and mouse scRNA-seq datasets from peer-reviewed three human and 11 mouse scRNA-seq datasets from 14 studies, the
studies with experimentally confirmed developmental states and test cohort spans 93,535 cells, 73 phenotypes, nine tissue types and
assignable potency levels (Supplementary Table 1). As part of this seven scRNA-seq platforms, including two tissue types and 21 pheno-
selection process, we applied the following inclusion and exclusion types that were absent from training (Fig. 1b and Supplementary
criteria to enhance experimental rigor: Tables 1 and 7).
To augment these data, we annotated potency categories in
• Only functionally validated developmental states supported 459,320 evaluable cells from Tabula Sapiens, a multi-tissue scRNA-seq
by lineage tracing or transplantation assays were considered atlas from postmortem human donor biopsies33 (Supplementary
for analysis. Datasets with transient cell changes, such as from Table 1); however, given the confounding influence of postmortem
metabolic activation or suppression, cell cycle transitions or intervals on human tissue messenger RNA levels44, we hypothesized
environmental perturbations were excluded, as these do not that Tabula Sapiens might exhibit reduced data quality. To test this,
represent durable developmental processes. we calculated the ratio of mitochondrial reads to total reads (MTR)
• Datasets with irreconcilable technical batches resulting in major within each single-cell transcriptome as a proxy for overall data quality.
imbalances in the number of cells per phenotype were excluded. Indeed, we calculated a mean MTR across all Tabula Sapiens tissue
• Single-nucleus RNA sequencing datasets were excluded, as types, stratified by platform, of 7.4% (median of medians), which is
they do not capture cytoplasmic RNA and include immature nearly 90% higher than expected for human cell types profiled by
transcripts. scRNA-seq data (median of medians of 3.9%; Table S1 of Osorio and
Cai45) and 78% higher than other human datasets in the training and test
Among datasets satisfying these conditions, author-supplied cohorts, both of which include embryonic tissues with high metabolic
cell type annotations were mapped to one of six broad potency activity (median of medians of 4.2%). Accordingly, we omitted Tabula
categories (totipotent, pluripotent, multipotent, oligopotent, uni- Sapiens from the primary test cohort and evaluated it as a secondary
potent and differentiated) or not evaluable using established defini- benchmark in Fig. 1h,i. Author-supplied phenotypes in Tabula Sapiens
tions (‘Potency annotation scheme’, Supplementary Note). These with fewer than five cells in a tissue–platform pair were excluded from
potency categories were further subdivided into 24 granular catego- further analysis.
ries, ranging from 1 (least differentiated) to 24 (most differentiated) Collectively, these ground truth datasets with newly annotated
(Supplementary Tables 2 and 3). Cellular phenotypes were hierarchi- potency levels represent a unique community resource for systematic
cally grouped into these categories based on potency, developmental characterization of absolute developmental states and their molecular
timing and sequence, and self-renewal capacity. programs in humans and mice. Depending on platform, all scRNA-seq
Where possible, we also examined single-cell developmental expression matrices were normalized to transcripts per million (TPM)
states in a dataset-specific manner and without regard to potency or counts per million (CPM) as appropriate. Full details of each dataset,
categories, as previously described3. Such ‘relative’ orderings, most including dataset name, accession number, PMID, species, platform,
of which were obtained from Gulati et al.3, ranged from 1 (least differ- tissue type, number of cells, number of phenotype, and number of
entiated) to N (most differentiated) in a given dataset, and exceeded potency levels, are available in Supplementary Table 1. These data
the number of resolvable potency categories in some datasets can also be interactively explored at https://cytotrace2.stanford.edu.
(Supplementary Table 4), permitting a more granular assessment
Our comprehensive potency atlas catalogs experimentally Additional annotation considerations. For cells with identical pheno-
confirmed cell states and their corresponding potency levels, pro- types but different author-supplied labels, we unified the annotations
viding a structured reference for model training and validation. (Supplementary Table 3). For example, ‘HSC-MPPs’ from ‘HSC develop-
Supplementary Table 3 includes key details such as the broad and ment (Smart-seq2)’ and ‘Hematopoietic stem cell progenitor (HSCP)’
granular potency levels, standardized and original cell phenotypes, from ‘HSPCs (C1)’ were annotated as ‘Hematopoietic stem and early pro-
species, dataset source, cohort type (for example, training, validation genitor’. To balance the representation of cells from distinct lineages
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
within a given broad potency category, we also re-annotated related of a shared input layer; a set of G GSBN modules, where G denotes the
cell subsets sharing a common parental phenotype. For example, ‘CD4+ number of potency categories; and a shared output layer (Extended
helper T cells’ from ‘peripheral blood (10x)’ and ‘CD8+ memory T cells’ Data Fig. 1a). Within the core model, each GSBN module is trained to
from ‘BM-MNC (CITE-seq)’ were labeled as ‘T cell’. This was crucial when discriminate a single potency category and contains (1) a binary neu-
training CytoTRACE 2 as the probability of sampling individual cells ral network (BNN) component, which encodes potency-associated
was weighted based on phenotype. In this way, each major phenotype gene sets and (2) downstream functions to calculate and integrate
contributed equally during model training regardless of the number of gene set enrichment scores (Fig. 1c and Extended Data Fig. 1a). Notably,
evaluable cells, mitigating the chance of overweighting and overfitting because weights in BNNs are constrained to binary rather than continu-
(see ‘Training and hyperparameter tuning’ below). The standardized ous values, BNNs also allow for more efficient computation and provide
phenotype assignments along with the original annotations are sum- an implicit form of model regularization48.
marized in Supplementary Table 3.
Preprocessing. Let input scRNA-seq dataset X be an I×C gene expres-
The CytoTRACE 2 framework sion matrix over I genes and C cells. The following preprocessing
Existing RNA-based surrogates of cellular differentiation status have steps prepare the input dataset for training or prediction.
notable limitations for imputing absolute differentiation states and First, gene symbols in X are mapped and filtered using dictionary
potency categories from scRNA-seq data. For example, the original 𝔻𝔻, a collection of gene symbols that harmonizes all HGNC (human) and
CytoTRACE, termed CytoTRACE 1 in this work, employs gene counts MGI (mouse) identifiers supported by CytoTRACE 2 (‘Dictionary of
as an unbiased strategy for identifying immature cells3. Despite the input genes’ below). Following this step, the resulting expression
utility of this approach, gene counts are subject to dataset-specific matrix, denoted X′, consists of n=14,271 genes and C cells. As part
biases, making them suboptimal for potency assessment. Measures of this process, any genes in X′ not present in X through mapping
based on transcriptional entropy and RNA velocity also suffer from are set to zero. In the second step, X′ is converted into dual representa-
dataset-specific biases, a nonspecific relationship to absolute differ- tions: for the first, it is normalized to CPM/TPM and log-adjusted,
2
entiation status, or the requirement for continuous developmental yielding an N×C matrix L; for the second, it is mapped to rank space,
processes within a narrowly defined time window4,5,14–16. yielding an N×C matrix R, with the genes of each single-cell transcrip-
Supervised machine learning models offer a potentially robust tome X′ assigned relative integer rank such that rank 1 corresponds to
c
alternative to the abovementioned strategies when adequate training the gene with highest expression. While the log CPM/TPM representa-
2
data are available; however, machine learning methods also face key tion maintains detailed transcriptomic information, the alternative
challenges when applied to scRNA-seq data, including sparsity, high encoding provided by rank space helps circumvent batch effects,
dimensionality and data heterogeneity encompassing both biological mitigate the influence of extreme values and outliers, and reduce the
and technical variation. While deep learning is a promising subtype of risk of model overfitting. In tandem, these two representations provide
machine learning, often achieving remarkable performance gains over an inherent regularization to model inputs. R and L are subsequently
other machine learning methods (especially in the presence of high passed to the CytoTRACE 2 core model where they jointly constitute
complexity, noise and uncertainty) most existing architectures lack the model input layer.
inherent interpretability, limiting their broad applicability.
To address these challenges, we designed a novel deep learning Gene set binary networks. Inputs R and L are passed to each of G GSBN
framework that can handle the complexities of single-cell potency modules within the CytoTRACE 2 core model. These modules begin
assessment while achieving direct biological interpretability. Unlike by thresholding R (Extended Data Fig. 1a) to learnable maximum rank
recent methods46,47 that decompose single-cell expression data into τ∈ℕ, yielding N×C matrix T:
a combination of previously known and simultaneously learned new
gene programs, our approach, termed a GSBN, is anchored to known Ti,k=min(Ri,k,τ)
phenotypic states but not known gene sets. As such, GSBNs have the
flexibility to discover new gene programs for known phenotypic states, This rank trimming (see also ‘Model initialization and updates’)
such as potency categories, from scRNA-seq data. As part of their enables calculation of the rank-based enrichment score, described in
design, GSBNs are highly robust and fully interpretable, meaning they ‘Enrichment assessment’ below. Input L remains the same.
can be directly interrogated to extract meaningful markers for each Next, within each GSBN module, M gene sets are learned in binary
phenotypic class of interest across datasets, platforms and tissues. N×M matrix WB, where M∈ℕ is prespecified and all entries WB ∈{0,1}.
i,j
WB constitutes the gene set selection layer of the CytoTRACE 2 core
Technical description. CytoTRACE 2 consists of five high-level com- model; it has a continuous equivalent W used for model initialization
ponents, schematically depicted in Fig. 1c and Extended Data Fig. 1a and backpropagation (see also ‘Training and hyperparameter tuning’).
and described in detail below. At each forward iteration for model training, W undergoes binarization:
• Preprocessing: ortholog mapping and expression normalization. WB=binarize(W,0)
• GSBNs: identification of interpretable potency-associated gene
sets for each potency category. where binarize denotes the following utility function:
• Enrichment assessment: evaluation of gene set activation levels
in single cells. 1, Mi,j>a
binarize(M,a) ={
• Integration of scores: integration of gene set activation levels, i,j 0, Mi,j≤a
both within and across gene set binary networks.
• Postprocessing: leveraging transcriptional covariance and Enrichment assessment. To quantify the enrichment of each gene
uncertainty in model predictions to smooth single-cell potency set in the module (each column of WB), CytoTRACE 2 leverages two
scores and produce the final output. complementary measures: rank-based enrichment score (ScoreU )
and expression-based enrichment score (ScoreA ). ScoreU aggregates
Core model architecture. Among these five components, GSBNs, overall expression activity of a given gene set j in rank space whereas
enrichment assessment and integration of scores constitute the ScoreA compares the average expression of genes in j versus background
CytoTRACE 2 core model, a neural network architecture consisting levels. By integrating both scores, each providing a different axis of
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
information, CytoTRACE 2 can learn more complex expression patterns To transfer these enrichment scores into comparable spaces,
while also achieving additional regularization through enrichment CytoTRACE 2 standardizes each score across cells, yielding C×2M
score competition. The two scores are defined as follows. matrix Knorm. This standardization, implemented via torch.
ScoreU calculates the commonly used nonparametric UCell nn.BatchNorm1d from PyTorch v.2.0.0 with affine = False, tracks
score49 for each gene set, or column of WB. For each cell 1≤k≤C and the mean and variance of each score during training. Once trained,
module gene set 1≤j≤M, the model applies these learned values, rather than dataset-specific
values, for standardization at inference.
ScoreU(T,WB) k,j =1+[
S ⇀ j(S ⇀ j+1)−2∑
⇀
N
i=1
Ti,kWB
i,j ], Integration of scores. To convert the gene set enrichment scores to a
2τSj
single score per cell per GSBN module, the normalized scores Knorm are
passed through a feedforward layer, termed the ‘enrichment layer’ in
where S ⇀ denotes the vector of length M containing the number of the CytoTRACE 2 core model, containing the associated length 2M
genes per gene set assigned nonzero weight in the binary weighti ng gene set enrichment score weight vector V ⇀ and yielding length C
matrix: potency category score vector q⇀. As part of this process, dropout is
applied to reduce overfitting during model training, with a predeter-
S ⇀ =∑ N WB 1≤j≤M mined fraction of the normalized scores set at random to zero.
j i=1 i,j From the weights in each V ⇀, concatenated across potency categories
into matrix V, the directionality and importance of each gene set can
ScoreA implements a scoring system based on Seurat’s AddModuleScore be interpreted (see ‘Interpretability’ below).
(AMS), computing the average expression of genes within a gene set The model then integrates across the potency category scores
subtracted by the aggregated expression of control, or background, produced by each GSBN module, concatenating the potency category
feature sets50. To select background features, AMS groups genes into score vectors into C×G potency score matrix Q. This procedure repre-
nbins bins according to their average expression within a dataset. Then, sents the shared output layer of the CytoTRACE 2 core model.
for each gene, a ‘background’ set of nsample genes from the same average To convert the logit entries of Q to likelihoods, the model applies
expression bin is sampled, ensuring that each gene is compared to a softmax activation function, yielding C×G matrix P representing the
other genes with similar average expression. Here, for computational likelihood of each cell belonging to each of the six potency categories.
efficiency and to avoid introducing a dependency on dataset composi- The model then predicts cellular potency by assigning the potency
tion, we use our entire curated training cohort (see ‘Single-cell potency category with highest likelihood for each cell, yielding length C
atlas’) as the ‘dataset’ in which to rank genes by average expression. We vector ŷ:
then compute a constant set of background genes to use for each gene.
We encode the mapping of genes to their background genes in the ŷ k =argmax {p}G p=1 (Pk,∗)
binary N×N matrix G, where each row represents a gene as used in a
gene set, and the jth entry of row i is 1 if gene j is used as background for The ŷ vector represents one of the key outputs of the CytoTRACE
gene i, and 0 otherwise. 2 core model; however, the model also computes an absolute develop-
In detail, we construct G as follows. First, we compute the average mental potential from this set of likelihoods, termed the raw potency
log 2 CPM/TPM expression per gene across all cells from the training score R ⇀ PS. For this aspect, we introduce length G ordered vector ⇀ t
cohort. We then rank the results and uniformly partition genes to be multiplied by the potency category likelihood matrix:
i d n e t f o a u nb lt in 5 s 0. = N 2 e 4 x b t, i n fo s r o e f a si c z h e g sb e in n a e c ( c e o a r c d h in r g o w to o r f a n G k ) , , f w o e ll o ra w n in d g o m th l e y S s e e u le r c a t t RP ⇀ S=P ⇀ t
without replacement a set of background genes, where the number of
background genes follows a Gaussian distribution with mean μ=nsample ⇀ t=[0.0,0.2,0.4,0.6,0.8,1.0],
and variance
where R ⇀ PS is the length C raw potency score vector. As the potency
σ2=nsample( sbin−
sb
n
in
sample ) c
ti
a
a
t
l
e
,
g
th
o
e
ri
r
e
e
s
s
a
u
r
l
e
t i
o
n
r
g
d e
ra
re
w
d
p
b
o
a
t
s
e
e
n
d
c
o
y
n
s
t
c
h
o
e
r
i
e
r a
w
b
il
s
l
o
b
lu
e
t
c
e
l o
d
s
e
e
v
r
e l
t
o
o
p
o
m
n
e
e
n
f
t
o
a
r
l
h
p
i
o
g
t
h
e
e
n
r
-
potency categories, such as totipotent, and closer to zero for lower
where nsample=100. This approach provides an additional regularizing potency categories, such as differentiated. As R ⇀ PS directly incorporates
effect compared to constant selection of a uniform number of back- model uncertainty, it is passed to ‘Postprocessing’ below to define a
ground genes per gene. Note that left-multiplying a gene set matrix more granular developmental ordering.
WB by G maps the genes in the gene sets (columns) of WB to their
corresponding background genes. Postprocessing. As the fully trained CytoTRACE 2 model predicts
Then, given G, for each cell 1≤k≤C and module gene set 1≤j≤M, potency for each cell individually, CytoTRACE 2 further processes the
output (raw potency score R ⇀ PS and predicted potency categories ŷ) to
(LW B ) (LGW B ) incorporate the neighborhood structure of transcriptionally similar
B k,j k,j
ScoreA(L,W )
k,j
=
∑ N i=1 WB i,j
−
∑ N i=1 (GW B ) i,j
, c
g
e
iv
ll
e
s
n
. W
ou
e
r
r
p
e
r
a
e
s
v
o
i
n
o
e
u
d
s e
th
x
a
p
t
e
d
ri
o
e
i
n
n
c
g
e
s
c
o
o
c
m
o
b
u
i
l
n
d
i
f
n
u
g
r
g
th
e
e
n
r
e
i
c
m
o
p
u
r
n
o
t
v
s
e
w
p
it
e
h
r
t
fo
ra
r
n
m
s
a
c
n
ri
c
p
e
-
tional covariance in CytoTRACE 1 (ref. 3). To this end, we devised and
where the first term simply computes the average expression of validated a three-step procedure using the training cohort, as described
selected gene set genes in each cell of input gene expression matrix L, below. Notably, this procedure improves correlations with relative
and the second term calculates the aggregated average expression of developmental orderings (see ‘Metrics’ below) over R ⇀ PS or ŷ alone
background genes within the same cells. without sacrificing the potency classification performance achieved
The two resulting enrichment score matrices are subsequently by ŷ (Extended Data Fig. 1b).
concatenated into a single C×2M matrix K: In the first step, CytoTRACE 2 applies Markov diffusion to smooth
R ⇀ PS using the same implementation as CytoTRACE 1 (ref. 3). In brief,
B B
K=[ScoreU(T,W ) ScoreA(L,W )] the log 2 -adjusted CPM/TPM gene expression input L is used to create
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
a Markov matrix from the transcriptional similarity between cells over where N(w) denotes the set of all cells within the selected neighborhood
the top 1,000 genes with highest dispersion3. This similarity matrix is of center cell w, including w itself, and dc denotes the Euclidean
then used to smooth R ⇀ PS with diffusion parameter α = 0.9 as previously distance of cell c to cell w. Categorical potency predictions are updated
described3, yielding smoothed potency score SP ⇀ S. Using the same based on the defined intervals above, yielding ŷ∗.
sampling procedure described in our previous work3, the running We found empirically that combining these three approaches
time of this step can be significantly reduced without loss of perfor- yielded superior performance on the training cohort (Extended
mance (Extended Data Fig. 1c). In this study, sampling was restricted Data Fig. 1b).
to datasets with >10,000 cells (Supplementary Table 1).
To reconcile SP ⇀ S with predicted potency categories ŷ, in the sec- Training and hyperparameter tuning
ond step CytoTRACE 2 performs a binning procedure to maintain ŷ Loss function. For model training, we defined a loss function combin-
while preserving relative potency ordering within each category. ing cross-entropy loss with an additional term penalizing gene set size
To do so, CytoTRACE 2 first separates cells by their predicted potency based on the binary weighting matrix WB originating from each GSBN
p
category and assigns each cell 1≤w≤C a rank ℛ(k,ŷ ) relative to module, 1≤p≤G. More precisely, we define the loss function as the
w
all cells sharing predicted potency category ŷ
w
. For this transformation, sum of gene set size penalty loss JS and a prediction loss per cell JP :
within each potency category 1≤p≤G, the cell with lowest potency
score receives rank 1 while the cell with highest potency score receives J=JS(WB 1 ,⋯,WB G )+∑ J P (ŷ w ,y w )
maximum rank rmax(p). Cells are then arranged uniformly by rank per w
potency category within equal length partitions of the unit interval, In detail, given potency category predictions ŷ and ground truth
w
yielding binned smooth potency score SP ⇀ SB. Thus, the binned smooth potency categories y for cell w (see ‘Single-cell potency atlas’ above),
w
potency score for differentiated cells extends from 0 to 1/6, unipotent we defined prediction loss JP as:
from 1/6 to 2/6, and so on, with relative ordering within each bin match-
ing that of the original smoothed potency score. JP(ŷ w ,y w )=v⇀ w×CE(ŷ w ,y w )
In the third step, to further smooth SP ⇀ SB while minimizing the
impact on ŷ and allowing for the preservation of rare cell states where v⇀ w denotes the loss weight assigned to cell w, and CE(ŷ w ,y w )
(Extended Data Fig. 3f), CytoTRACE 2 applies a variation of k-nearest denotes the cross-entropy loss for cell w. Loss weights for all cells
neighbor (k-NN) smoothing to datasets with >100 cells. Here, we intro- are contained in the length C weighting vector v⇀, which has unit
duce an efficient heuristic approach for adaptive neighborhood sum and is constructed hierarchically to assign equal weight (1) to all
smoothing guided by two key assumptions: (1) cells with more similar broad potency categories, (2) to all phenotypes within each broad
gene expression profiles are more likely to share a potency phenotype; potency category, and (3) to all datasets contributing to each
and (2) prediction errors for cells with the same ground truth potency phenotype.
exhibit a random distribution around a central mean. To balance these We defined gene set size penalty loss JS as:
two considerations and identify an appropriate neighborhood size,
w
Fi
e
rs
s
t
e
,
l
g
e
i
c
v
t
e
k
n
a
l
d
o
a
g
p
2 -
t
a
iv
d
e
j
l
u
y
s
f
t
o
e
r
d
e
C
a
P
ch
M
c
/
e
T
l
P
l a
M
c c
g
o
e
r
n
d
e
in
e
g
x p
to
r e
th
ss
e
i o
fo
n
l l
p
o
r
w
o
i
f
n
il
g
e
p
s
r
f
o
o
c
r
e
t
s
h
s
e
. JS(WB
1
,⋯,WB
G
)=aλ
p
∑ G
=1
| |
|N
1 (WB
p
) T (WB
p
)⊙I | |
| F
,a= √
√
1
M
2
selected cell, we standardize expression per cell to zero mean and unit
variance, then perform dimension reduction of standardized gene where |•| denotes the Frobenius norm, ⊙ denotes the Hadamard
F
expression profiles over all cells to the top 30 principal components (or element-wise) product, I denotes the M×M identity matrix,
(PCs). Using the top 30 PCs, we then compute pairwise Euclidean dis- λ denotes the gene set size penalty weight, and a serves as a scaling
tances for all cells, rescaling the resulting distances to unit maximum factor to make JS invariant to the number of gene sets included in WB
p
,
per cell of interest. Next, we define the neighborhood around each with factor √12 selected to anchor the gene set size penalty weight to
center cell w through an iterative procedure, allowing a maximum the center of the range of hidden sizes tested (see ‘Hyperparameter
neighborhood size of 30 cells. We start with the nearest cell to w, optimization’). This loss component serves to minimize the number
denoted c1 , and calculate the average potency score prediction for w of genes in each gene set while regularizing the training of the model.
and c1 , mapping the result to one of six broad potency categories,
yielding P1 . We repeat this calculation for the next two nearest cells to Model regularization. To promote model generalizability, we intro-
w (c2 and c3 ), yielding P2 , and compare P1 and P2 . If identical, we assume duced two explicit regularization aspects. We included a dropout layer
that we have sufficiently captured the neighborhood, setting k = 3 (for to avoid model overfitting to specific enrichment scores (“Integration
the three non-self-neighbors) and exiting the process. If not identical, of scores”). A dropout layer51 randomly drops (sets to zero) units in a
we repeat the procedure increasing the group size by one, in other hidden layer of a neural network. This layer was applied to the normal-
words, comparing the nearest two cells to w (yielding three total ized scores Knorm during training only. Additionally, a penalty term
cells) with the next nearest three cells (c3 , c4 and c5 ). We repeat this was added to the loss function to constrain the number of genes in
process until the resulting potency categories are the same between each gene set of WB (“Loss function”).
two groups, in which case we select k to encompass all cells considered
between the two groups, or until we exhaust our candidate nearest Model initialization and updates. Model weights were initialized
neighbor cells (reach a group size of 15). If concordance between according to PyTorch v.2.0.0 default except for the binary weight-
nearest and next nearest groups is not found, we keep our initial ing matrices, which were initialized at random with values sampled
selection of k = 3. from the Gaussian distribution with mean of –0.1 and s.d. of 0.055 to
Once k is determined, we update our prediction for w according produce a sparse initial binarization with approximately 500 genes
to the distance-weighted mean of neighborhood potencies to obtain selected per gene set.
the final potency score prediction: Model training was performed with mini-batch learning using a
batch size of 1,024. To balance batches and ensure equal representation
for the model learning process, each batch was constructed via uniform
sampling across datasets and phenotypes (Supplementary Tables
1 and 3) as implemented by torch.utils.data.WeightedRandomSampler
in PyTorch.
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
Following initialization, forward propagation proceeded for each accuracy over model validation sets (Supplementary Table 3; see
iteration as described in ‘Core model architecture’, with parameters ‘Model evaluation and stopping’).
updated according to their definition. For numeric stability, the cutoff We observed that variation in hyperparameter values had minimal
rank τ (‘Gene set binary networks’) for trimming input rank space impact on performance, underscoring overall model robustness
expression matrix R was not learned directly but rather computed (Extended Data Fig. 1e, left and Supplementary Table 6). Final hyper-
as a function of learnable parameter τm∈ℝ, which was initialized parameter selection was carried out by a manual curation process
uniformly at random from 0≤τm≤1 per module and suitably scaled. identifying values yielding consistently (albeit modestly) higher
As gene set enrichment score calculation (‘Enrichment assessment’) weighted accuracy. In selecting the number of gene sets M per potency
requires a gene set pool larger than the gene set itself for comparison, category, we found that model performance increased with M
τ was computed from τm in such a way as to ensure that the ranks of at before plateauing (Extended Data Fig. 1e, right); as such, we selected
least ten more genes beyond the maximum gene set size of the module M slightly larger than the number corresponding to the elbow of
were preserved following trimming to T. Thus, at each iteration, the this curve. The final hyperparameters used were M=24 gene sets per
updated τm was scaled and constrained as follows: potency; ρ=0.5 dropout probability; λ=0.01 gene set size penalty
weight; and lr=0.001 learning rate.
⇀
τ=10+max1≤j≤MSj+1,000×max(0,τm) Next, we evaluated the enrichment metrics. Among all models, we
limited to 84 models with hyperparameter values in ranges of plateau
Model predictions were assessed at each iteration against ground (M≥2 gene sets per potency; ρ=0.5 dropout probability, λ≤0.01,
truth, with the loss function and its gradient computed and used to lr≤0.001). AMS enrichment and both AMS and UCell enrichment
backpropagate updates to network weights using PyTorch’s NAdam achieved superior performance compared to UCell enrichment
optimizer with custom learning rate lr=0.001 (see ‘Hyperparameter alone (Extended Data Fig. 1f and Supplementary Table 6). Given the
optimization’ below) and otherwise default parameters. Given the role potential to enhance generalizability, we therefore selected the com-
of inertia in successfully training binary neural networks52,53, we bination of AMS and UCell enrichment metrics for the final model.
employed cross-epoch gradient accumulation to dampen binary
weight flipping and achieve a stabilizing effect. This approach addition- Model ensembling. Models were trained via leave-one-dataset-out
ally facilitates broader hyperparameter space exploration while cross-validation for each of the training datasets, with final CytoTRACE
validation-based early stopping (see ‘Model evaluation and stopping’) 2 predictions in non-training data obtained as the result of integrating
ensures that the most performant model encountered during predictions across the 19 resulting models followed by an additional
training is retained. Backpropagation for the binary neural network postprocessing step. As described in ‘Integration of scores’ above, each
component of each GSBN module was implemented with Straight- model m yields a C×G potency category likelihood matrix Pm. Models
Through Estimator and hardtanh activation function as previously were integrated by entry-wise averaging of potency category likelihood
described48. matrices to yield a single potency category likelihood matrix Pensemble
from which potency category predictions and raw potency scores were
Model evaluation and stopping. We evaluated model validation per- computed as described above, before passing them to ‘Postprocessing’.
formance via weighted accuracy, defined as the mean F1 score across
evaluable potency categories. To do this, we first calculated the F1 Dictionary of input genes
score for each phenotype (standardized as in Supplementary Table 3) To create dictionary 𝔻𝔻 (‘Preprocessing’ above), all human gene symbols
and dataset pair using metrics.precision_recall_fscore_support from were mapped to their closest mouse orthologs, as determined by gene
sklearn v.1.0.2. We then averaged the resulting scores across datasets sequence similarity, using the GRCh38.p13 and GRCm39 annotation
per phenotype, across phenotypes within each broad potency cate- files available from Ensembl v.109, respectively. In cases where a single
gory, and across broad potency categories, yielding the final weighted mouse gene g was identified as the best hit for multiple human genes,
accuracy. For the standard CytoTRACE 2 model, each validation set con- the human gene with maximum sequence similarity to g was selected
sisted of a single dataset; however, for the leave-clade-out model (see and the remaining human gene(s) excluded from further consideration.
‘Generalizability to unseen cell-type clades’), validation sets included Unique human gene symbols without orthologs by the above process
all cells covering a clade, regardless of dataset. All models were trained were also included for completeness. To define a common subset, only
for 100 epochs with the best model weights by the highest score on the genes present in at least 80% of datasets from an initial development
validation set after a minimum of 15 initial training epochs preserved cohort, a subset of the final training cohort, were retained. Combining
and returned for the final model. these steps, 𝔻𝔻 was assembled with 14,271 unique gene symbols, includ-
ing 13,750 orthologous pairs and 521 genes without orthologs in
Hyperparameter optimization. To evaluate the hyperparameter space Ensembl via the mapping step above. When mapping human datasets
of CytoTRACE 2, we performed a hyperparameter sweep over the to 𝔻𝔻, gene symbol aliases are resolved using linked aliases available
training cohort using wandb (v.0.16.4) (https://wandb.ai). We explored from https://biomart.genenames.org. When mapping to mouse
the learning rate lr over {0.01,0.005,0.001,0.0005,0.0001}, number M datasets, alias gene symbols are resolved using data available from
of gene sets per broad potency category over {1,2,4,8,12,16,24,32,48}, https://www.informatics.jax.org/mgihome/nomen/.
gene set size penalty weight λ over {0.5,0.1,0.05,0.01,0.005,0.001},
dropout rate ρ over {0,0.25,0.5}, and enrichment considering whether Interpretability
to use AMS enrichment, UCell enrichment, or the combination of both The GSBN architecture of CytoTRACE 2 enables direct interrogation
as described in ‘Enrichment assessment’ above. For every iteration of of the binary weight matrices, consisting of gene sets associated with
leave-one-dataset-out nested cross-validation, we trained models each potency category (Fig. 1c and Extended Data Fig. 1a). By exam-
across 500 different combinations of these hyperparameters sampled ining the orientation of the output layer weights for each gene set,
based on the random hyperparameter search. To minimize overfitting we found that gene sets with positive weights (polarity) were highly
to training data, we used a nested cross-validation framework. While enriched in a given potency category, whereas those with negative
one dataset was held out from training and evaluated as a validation weights (polarity) were preferentially depleted (Fig. 2c). Addition-
set, another dataset was also held out from training but used to deter- ally, we reasoned that genes repeatedly selected for a given potency
mine the early stopping point as described in ‘Model evaluation and category were more likely to be important for effective classification.
stopping’. We scored each hyperparameter combination by weighted As such, we designed a metric to quantify feature importance, assigning
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
importance scores to genes according to the frequency at which they analysis (Supplementary Table 2). The final clades cleanly separate,
were selected in positively versus negatively weighted gene sets. Here, for example, immune cells, neural cells, endothelial cells, connective
we incorporate gene selection frequency across all 19 training models tissue cells and bone cells, among others. Stem and progenitor cells
computed by leave-one-out cross-validation (LOOCV) over the training that produce a given clade were included in the same partition as that
cohort datasets. clade (for example, pancreatic multipotent progenitors were included
More formally, we define N×G feature importance score matrix with pancreatic epithelial cells). Epithelial cells were separated by
F (Supplementary Table 15) containing the feature importance score tissue to avoid conflating tissue-specific developmental hierarchies.
of each gene 1≤i≤N for each potency category 1≤p≤G based on For each clade, we trained an ensemble of two models over the remain-
the gene set compositions and enrichment weights across models. ing 18 clades, selecting at random 17 clades for training and one clade
Two enrichment weights correspond with each gene set, one per as a held-out validation set to be used for early stopping (see ‘Model
enrichment score type (see ‘Enrichment assessment’). Given gene set evaluation and stopping’) for each model. We then applied the result-
enrichment weight matrix Vl of model l, we calculate the polarity ing ensemble to the unseen test clade, assessing performance across
Polarity(Vl,j,p) of gene set j defined within model l for potency cate- all held-out clades in Fig. 1f.
gory module p as the sign of the average of these two weights. Then,
relying on model binary weighting matrices to encode gene set com- Randomization of training and test sets. To assess the robust-
position, we construct feature importance score matrix F entry-wise as ness of the model to variation in the composition of the training
cohort, we repeated the CytoTRACE 2 training process as described
19 M in ‘The CytoTRACE 2 framework’ across a series of three rando-
Fi,p=∑∑WB
p,l
[i,j]×Polarity(Vl,j,p),
mized splits covering all 33 datasets in the single-cell potency atlas
l=1j=1
(Supplementary Table 8). We partitioned the datasets at random into
where WB [i,j] denotes the [i,j]th entry of the binary weighting three folds, each containing 11 datasets. To ensure minimum adequate
p,l
matrix from module p of model l. representation within each category, we confirmed that each fold
contained at least one phenotype per broad potency category. Tabula
Performance assessment Muris, which was divided into two sub-datasets according to platform
Metrics. Two key metrics, illustrated in Extended Data Fig. 1d, were for the original CytoTRACE 2 training cohort due to its size and diver-
used to quantify reconstruction of known developmental orderings: sity, was again divided, with one of its sub-datasets assigned to another
absolute order and relative order. Absolute order quantifies cross- fold at random. For each split, two folds were combined to form
dataset performance, whereby predicted orderings from all cells with the training cohort and the remaining one left as a test set for evalu-
annotated potency levels are analyzed together, regardless of dataset, ation (2:1 training–test split; Supplementary Table 8). Performance
tissue type or platform (Supplementary Tables 2 and 3). Relative order per test set of these three randomized splits, along with the original
quantifies performance within a given dataset and tissue type, akin to CytoTRACE 2 test set, was assessed by absolute order, relative order,
conventional pseudotime and ranges from 1 (least differentiated) to N mean multiclass F1 score and MAE (see ‘Metrics’), showing strong
(most differentiated) in each dataset (Supplementary Table 4). For both consistency across folds (Extended Data Fig. 2d). Performance for the
metrics, we applied weighted Kendall correlation (τ) (wdm package three randomized splits was additionally assessed across all held-out
v.0.2.4 in R) to assess concordance between known and predicted devel- datasets jointly in Extended Data Fig. 2e.
opmental orderings, with weighting schemes provided in Supplementary
Table 5. Similar to our previous work3, ground truth phenotypes corres- Robustness of CytoTRACE 2
ponding to less mature cells were coded with lower ranks (starting at 1); Robustness to annotation error. To evaluate the robustness of
therefore, higher predictions of developmental order were ranked such CytoTRACE 2 to potential noise within potency annotations, we trained
that higher values received lower ranks and vice versa. models across two scenarios of training cohort annotation error, then
For categorical predictions (CytoTRACE 2 and potency classifica- evaluated model performance over the test cohort (see ‘Training and
tion benchmarking outputs only), we evaluated potency classification test datasets’). To simulate annotation error, we formulated label noise
performance as well. Binary correctness of predicted versus ground as a transition matrix54, encoding the probability of perturbation from
truth broad potency categories was assessed via mean multiclass F1 one potency to another (Extended Data Fig. 3a). Transition matrix
score, implemented with function f1_score from sklearn.metrics with perturbation probabilities were designed to follow a Gaussian distribu-
average = none (Extended Data Figs. 1c top, 2d second from right, tion based on the rank distance between the original potency and
3b–e left bottom, 7a left and 7b x axis). To account for the magnitude perturbed potency. In detail, the probability that the potency label of
of deviations from ground truth potency, we also considered mean cell s transitions from true potency j to perturbed potency i
absolute error (MAE), assigning each broad potency class an integer
label corresponding to the class ordering, with labels ranging from 1 (j−i) 2
1 (differentiated) to 6 (totipotent), and computing the absolute value
P(si|sj)=
√2πσ2
exp(−
2σ2
),i,j∈{1,2,3,4,5,6}
of the difference between predicted and ground truth categories
(Extended Data Figs. 2d far right, 3b–e right bottom, 7a right and 7b where potencies i,j are represented by their rank within the six broad
y axis). For both metrics, scores were computed per ground truth potency categories. The s.d. values (σ) were selected to yield a titration
potency category then aggregated by mean across potencies. of 5%, 10%, 20%, 50% and 80% perturbation levels. Rows were normal-
ized to unit sum for a net probability of one. For the first annotation
Generalizability to unseen cell-type clades. To test the generaliz- error scenario, we considered cell-level annotation error and perturbed
ability of CytoTRACE 2 to unseen developmental systems, we trained the potency annotations of individual cells independently (Extended
a version with a leave-clade-out framework (Fig. 1f), grouping pheno- Data Fig. 3b). For the second, we considered phenotype-level annota-
types into 18 mutually exclusive developmental clades as detailed in tion errors and simultaneously perturbed the potency annotations of
Fig. 1b and Supplementary Table 9. Of note, to ensure representation the entire standardized phenotypes (Extended Data Fig. 3c).
of some totipotent and pluripotent phenotypes for all training sets,
we partitioned embryonic phenotypes into two clades by alternating Robustness to variation in gene counts and UMI counts. To deter-
granular potency level annotation, corresponding to distinct time mine the influence of variable gene counts and unique molecular
points during development and resulting in 19 total clades for this identifier (UMI) counts on CytoTRACE 2, we performed two experiments
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
in which scRNA-seq expression data from all 14 datasets in the test For the analyses in Extended Data Fig. 5d,e, we leveraged a data-
cohort were perturbed by downsampling gene counts (Extended driven lineage tree of mouse embryogenesis encoded as a directed
Data Fig. 3d) and all seven droplet-based datasets in the test cohort acyclic graph2. Although the tree was constructed using a heuristic
(Supplementary Table 1) were perturbed by downsampling UMIs approach based on transcriptional covariance across embryonic
(Extended Data Fig. 3e). We assessed the robustness of the model to time, it reflects many known parent-daughter relationships2. It thus
different gene counts by downsampling the expression data of each serves as a proxy for developmental potential. We defined ground
cell to the same number of genes: 2,000, 1,000, 750, 500, 250 and 100. truth as the distance from the root (zygote) to each daughter node
We selected the top genes by highest expression and set the expres- (Extended Data Fig. 5d, top). Using matching phenotype labels between
sion of the remaining genes to zero. For any expression level ties at the the tree and the data presented in Extended Data Fig. 5a, CytoTRACE 2
threshold, we selected the genes to include to reach the target gene potency scores were averaged by phenotype, balanced first by time
count at random. The downsampling process for UMIs consisted of points within a given embryonic day (if any) and then by embryonic
randomly sampling the expression data of each cell based on the tran- day. If the same phenotype was present in more than one dataset,
scriptome probability distribution, defined as the fractional expression we weighted equally by dataset. For each direct path in the tree
of each gene after scaling the sum of UMIs in each cell to one. Then, (from root to leaf), the resulting scores were then converted to rank
using the raw count matrices, we downsampled the expression data space (Extended Data Fig. 5d, center). To reconcile cases where a
of each cell to the same number of UMIs: 5,000, 3,000, 2,000, 1,000, given node i participates in multiple paths, we used the average
500 or 100 UMIs. Cells with UMIs lower than a given threshold were rank for i. CytoTRACE 1 predictions were processed in the same
unaltered. We repeated each process for five replicates, then assessed manner (Extended Data Fig. 5d, bottom). The resulting ranks were
performance for standard metrics as described above (see ‘Metrics’) correlated with ground truth distances (distance from the root) in
relative to the CytoTRACE 2 predictions without perturbation. Extended Data Fig. 5e.
Robustness to titration of cell type rarity. Given the inclusion of Application to cancer types with known developmental states
neighborhood-based smoothing in model postprocessing, we per- Acute myeloid leukemia analysis. For the analysis presented in
formed a titration experiment applying CytoTRACE 2 to test datasets Extended Data Fig. 6a, we downloaded the Galen et al.56 acute myeloid
with selected phenotypes downsampled to increasingly rare abun- leukemia (AML) dataset (Gene Expression Omnibus (GEO) accession
dance. For 11 phenotypes spanning a range of potencies, we down- number GSE116256; PMID 30827681) from the Curated Cancer Cell Atlas
sampled cells of the selected phenotype to predefined abundances of website on 28 June 2023 (https://www.weizmann.ac.il/sites/3CA/)57.
50, 20, 10, 8, 5, 2 and 1 cell(s), leaving the remaining cells in the dataset We leveraged author-supplied cell type annotations, including clas-
unchanged. We repeated this titration process five times for each sifications of malignant and non-malignant cells from 3CA57. From
phenotype, observing robust predictions down to five cells per pheno- this dataset, comprising 28 samples with malignant cells, we excluded
type (Extended Data Fig. 3f). As such, we recommend that the final two cell line samples (‘MUTZ3’ and ‘OCI-AML3’). We ran CytoTRACE 2
postprocessing step (adaptive k-NN smoothing) be omitted when with default parameters (‘Benchmarking developmental potential
exceedingly rare cell states (consisting of <5 cells each) are of interest. inference methods and annotated gene sets’) on all annotated malig-
nant cells from each tumor sample. For quality control, we further
Analysis of mouse embryogenesis excluded samples for which each predicted potency label contained
For the analyses presented in Extended Data Fig. 5, we downloaded <10 malignant cells. For each of the resulting tumor samples (n = 19),
and curated six publicly available scRNA-seq datasets spanning each we created a single matrix of malignant cells and non-malignant cells,
embryonic day during mouse prenatal development2,21–25 (Supplementary with the latter uniformly downsampled from all patients to 100 cells
Table 1). One dataset, which covers pre-implantation through per author-supplied phenotype (‘B_cell’, ‘erythrocyte’, ‘myeloid’,
early implantation (E0.5–E4.5) (Deng et al.22), was obtained from the ‘NK_cell’, ‘plasma’ and ‘T_cell’; non-malignant cells labeled as ‘undif-
19-dataset training cohort (Supplementary Table 1) and evaluated ferentiated’ were excluded from additional analysis). We then calcu-
using a CytoTRACE 2 model trained on the remaining 18 datasets to lated the log fold changes (LFCs) of each potency category versus
2
avoid overfitting (see ‘Benchmarking developmental potential infer- all other phenotypes by tumor sample and averaged by potency
ence methods and annotated gene sets’). Four datasets21,23–25 covering category across tumor samples. Finally, we normalized the logFC
embryogenesis periods from implantation to organogenesis were values of each gene to mean zero and unit variance across potency
previously assembled by Qiu et al.25 and are accessible through http:// categories and plotted the enrichment of AML cell-type-specific gene
tome.gs.washington.edu. Finally, a single-nucleus RNA-seq dataset2 signatures26 (‘LSPC-Primed-Top100’, ‘LSPC-Quiescent’, ‘GMP-like-
covering organogenesis through birth (E8.75-P0) and generated by Top100’ and ‘Mono-like-Top100’; https://github.com/andygxzeng/
sci-RNA-seq3 was downloaded from http://mouse.gs.washington.edu. AMLHierarchies), each expected to be enriched in multipotent, multi-
As we compared CytoTRACE 2 against multiple methods with highly potent, oligopotent and unipotent/differentiated cells, respectively
variable time complexity (‘Benchmarking developmental potential (Extended Data Fig. 6a and Supplementary Table 10).
inference methods and annotated gene sets’), all cells were randomly
downsampled to 30 cells per author-supplied phenotype per time Oligodendroglioma analysis. For Extended Data Fig. 6b, we applied
point, resulting in a combined dataset of 183,771 cells. This allowed us CytoTRACE 2 to scRNA-seq profiles of six oligodendrogliomas27, with
to balance considerations of performance versus computational effi- coordinates for the associated oligodendroglioma 2D lineage hierarchy
ciency. We ran each method on each dataset individually as described embedding obtained from https://singlecell.broadinstitute.org/single_
in ‘Benchmarking developmental potential inference methods and cell/study/SCP12/oligodendroglioma-intra-tumor-heterogeneity.
annotated gene sets’. No dataset integration or batch normalization We then assigned malignant oligodendroglioma cells to four trans-
procedures were applied. For Organogenesis (E8.5)25 and Organo- criptional states following the protocol described by the authors27
genesis (E8.5–P0)2, which were sequenced using sci-RNA-seq3, we and visualized the association of CytoTRACE 2 potency predictions
used count data after running SCTransform of Seurat (v.4.3.0) with with the author-supplied stemness score. For the latter, we sepa-
default parameters. Due to the large size of the dataset, Organogenesis rated cells according to the stemness score by partitioning them into
(E8.75–P0)2 was run with ten randomly divided batches for SCENT (SR) successive intervals of 0.25 units. We then displayed CytoTRACE 2
and SLICE. Primordial germ cells were excluded owing to the wide range potency scores as a function of each interval (Extended Data
of potency levels reported in previous literature55. Fig. 6b, right).
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
Benchmarking cell type prediction methods adapted for informative genes and indexCell() to create a scmapCell index for the
potency classification training dataset. For classification, we used scmapCell() to project the
To evaluate CytoTRACE 2 against supervised machine learn- index onto the test dataset and scmapCell2Cluster() to obtain label
ing approaches commonly employed in cell type prediction tasks assignments. A relaxed probability threshold of 0 was set to assign
(Extended Data Fig. 7a,b), we selected three dedicated single-cell anno- labels to as many cells as possible regardless of assignment confidence.
tation methods with superior performance in a benchmarking study28
(scPred30, SingleCellNet31 and scmap32) and five general-purpose Logistic regression. We trained a logistic regression model to perform
classifiers (below), each trained to predict six broad potency labels cell potency classification using the SGDClassifier from scikit-learn
based on single-cell expression profiles. (v.1.4.2) with loss = ‘log_loss’, default L2 regularization, and sample
All tools were trained and tested over a series of four folds, includ- weights provided for class balancing. This function internally employs
ing the original CytoTRACE 2 training–test split (Fig. 1b) along with a one-versus-rest (OVR) strategy, training a separate binary classifier
three randomized splits (see ‘Randomization of training and test for each potency category and selecting the potency category with
sets’), collectively encompassing all 33 ground truth datasets in the highest confidence at evaluation.
single-cell potency atlas described above, with classification perfor-
mance per test cohort assessed by mean multiclass F1 score and MAE XGBoost. We trained and applied the XGBClassifier function from the
(Extended Data Fig. 7a and b; see ‘Metrics’). For all methods, expres- XGBoost library (v.2.1.1) with default parameters and without sample
sion data were first mapped into the uniform feature space used by weights. Like logistic regression, this method uses the OVR approach.
CytoTRACE 2 (see ‘Preprocessing’ and ‘Dictionary of input genes’).
Unless otherwise specified, and for all general-purpose classifiers, Linear SVM. We implemented a linear SVM model using Scikit-learn’s
expression data were then CPM/TPM normalized and log-transformed SGDClassifier with loss = ‘hinge’ for linear support vector classification
2
and subsequently standardized per cell to zero mean and unit variance. with OVR. Sample weights were provided during training.
Other normalization schemes generally yielded worse performance
and were thus omitted from further consideration (log-adjusted Radial SVM. We implemented an additional SVM version using
2
CPM/TPM data, either used alone or with gene-level standardization). SVC from scikit-learn (v.1.4.2) with the default radial basis function
No explicit dataset integration or batch correction was performed. For kernel and γ = ‘auto’. The default decision function, which employs an
general-purpose classifiers, versions were trained with and without inference of OVR from one-versus-one fits internally, was used. Sample
sample weighting (computed as for CytoTRACE 2; see ‘Loss function’) weights were not provided during training.
for class imbalance mitigation, with the best performing version across
all folds selected for each. All parameters were set to default values Multinomial logistic regression. Using LogisticRegression from
unless otherwise specified. scikit-learn (v.1.4.2) with multi_class = ‘multinomial’, we fit a single
logistic regression model for all potency categories simultaneously
CytoTRACE 2. We applied CytoTRACE 2 with model ensembling and using cross-entropy loss and the ‘sag’ solver. A maximum number of
postprocessing as described in ‘The CytoTRACE 2 framework’ to pre- iterations (max_iter = 500) and tolerance (tol = 1 × 10−3) were set to
dict cell potency categories. Datasets containing more than 100,000 ensure convergence. Sample weights were not provided during training.
cells were processed in batches of 100,000 cells, and diffusion was
applied in batches of 10,000 cells for datasets exceeding 10,000 cells. Benchmarking developmental potential inference methods
and annotated gene sets
scPred. A dedicated cell type classification method, scPred first per- To rigorously assess performance on our compendium of 33 curated
forms a dimension reduction, identifying PCs exhibiting significant scRNA-seq datasets, we compared CytoTRACE 2 with eight published
variation across classes, then, as the default option, applies a support methods for predicting developmental potential from scRNA-seq data
vector machine approach for classification30. Following the recom- as well as nearly 19,000 previously annotated gene sets (Fig. 1h,i and
mended pipeline for scPred (v.1.9.2) as described at https://powell- Supplementary Tables 11–13). Unless otherwise stated, all evaluated
genomicslab.github.io/scPred/articles/introduction.html, we first methods and gene sets were applied to scRNA-seq datasets individually,
normalized and scaled expression data using the NormalizeData() and without batch correction or integration across datasets, with expres-
ScaleData() functions in Seurat (v.5.1.0), respectively. We then used sion data normalized per author recommendations and with default
scPred’s getFeatureSpace() function to identify class-informative PCs, parameters. All expression data were subset to the cells with known
trainModel() to train the default support vector machine (SVM) with potency. Each tissue and platform pair of Tabula Sapiens33 and Tabula
radial kernel model for each potency category (one-versus-rest), and Muris43 datasets were run separately.
scPredict() for classification. A relaxed probability threshold of 0 was Several methods rely on human gene symbols, as noted below. For
used to avoid ‘unassigned’ labels. all such instances, we mapped mouse dataset gene symbols to their
closest human orthologs, as determined by gene sequence similarity,
SingleCellNet. SingleCellNet performs cell type classification using using the GRCm39 and GRCh38.p13 annotation files available from
a random forest multiclass classification approach31. Here, we trained Ensembl, respectively. In cases where a single human gene g was identi-
the method over unnormalized expression data via the scn_train fied as the best hit for multiple mouse genes, the mouse gene with
function of pySingleCellNet (v.0.1.1) with nTopGenes = 200, nTop- maximum sequence similarity to g was selected.
GenePairs = 200, nRand = 100, nTrees = 1,000, stratify = False, and As several methods have slower running times, to promote an
propOther= 0.4, following the tutorial provided at https://pysingle- equitable comparison while achieving computational feasibility, larger
cellnet.readthedocs.io/en/latest/notebooks/train_classifier.html. datasets were first downsampled. The Tabula Muris43 dataset was down-
The scn_classify() function with nrand = 0 was used for classification. sampled to 30 cells per phenotype, separated by tissue and platform
pair, and the ‘Immune cell atlas (10x)’, ‘Human breast 1 (10x)’, ‘Human
scmap. scmap uses a clustering approach to project cells onto a refer- breast 2 (10x)’, and Tabula Sapiens33 datasets were downsampled to
ence dataset for cell type classification32. Following the recommended 100 cells per phenotype (Supplementary Table 1). Cell types in Tabula
pipeline for scmap (v.1.26.0) provided at https://bioconductor.org/ Sapiens33 with fewer than five cells were removed after the prediction of
packages/devel/bioc/vignettes/scmap/inst/doc/scmap.html, we each method to overcome the reduced data quality of Tabula Sapiens33
log-transformed expression data, then used selectFeatures() to select (‘Training and test datasets’).
2
Nature Methods
Brief Communication https://doi.org/10.1038/s41592-025-02857-2
CytoTRACE 2. We applied CytoTRACE 2 with model ensembling and When the raw count matrix was available for the dataset, the nega-
postprocessing as described in ‘The CytoTRACE 2 framework’ to pre- tive binomial conditioned likelihood loss function was used. Other-
dict cell potency categories and scores. Datasets containing more wise, the CPM/TPM expression matrix was log-transformed, and the
2
than 100,000 cells were processed in batches of 100,000 cells, and mean squared error loss function was used instead. Cell potency
diffusion was applied in batches of 10,000 cells for datasets exceed- scores were obtained from the developmental pseudotime predictions
ing 10,000 cells. To evaluate the 19 scRNA-seq datasets included in the extracted from the model training output with get_time().
CytoTRACE 2 training cohort, we trained a separate model for each
over the remaining 18 datasets. All other datasets were evaluated with mRNAsi. mRNAsi utilizes a one-class logistic regression framework to
the primary version of CytoTRACE 2 trained over all training datasets. construct a cellular stemness index applicable to cell potency estima-
tion from bulk and scRNA-seq data18. mRNAsi was trained as described
CytoTRACE 1. CytoTRACE 1, the predecessor of CytoTRACE 2, intro- previously3. All input gene expression matrices were CPM/TPM normal-
duced transcriptional diversity quantified through gene counts as ized and log-transformed.
2
a correlate of developmental potential and exploited this concept
to predict relative cellular potency from scRNA-seq3. CytoTRACE 1 Gene sets. The predictive capacity of 18,706 annotated gene sets
(v.0.3.3) was applied with default parameters. (17,810 gene sets from MSigDB36 and 896 gene sets of transcription
factor binding sites from ENCODE/ChEA34,35) was assessed via GSEA. For
SCENT (SR). SCENT estimates relative cellular potency from scRNA-seq each gene set, the AddModuleScore() function with default parameters
and a reference protein–protein interaction (PPI) network using from Seurat (v.4.3.0) was applied to each expression matrix normalized
single-cell signaling entropy (SR), a measure of the diversity of mole- via Seurat’s NormalizeData() function.
cular pathway activity in a cell15. SCENT (v.1.0.3) was executed with the
‘net13Jun12’ human PPI network provided with the package and other- Comparison to scVelo
wise default parameters. For mouse datasets, genes were first mapped to As scVelo5 relies on splicing kinetics, necessitating the processing of
human orthologs as described above. All gene symbols were converted raw sequencing data, we limited our analyses to nine ground truth
to Entrez ID using org.Hs.eg.db (v.3.15.0) in R. Gene expression matrices datasets from the test cohort that were generated by platforms with
were normalized per documentation recommendation (https://github. built-in support by velocyto and for which raw sequencing data are
com/aet21/SCENT/blob/master/vignettes/SCENT.Rmd). publicly available (Supplementary Tables 1 and 14). Raw FASTQ files for
seven of these datasets, namely ‘BM-MNC (CITE-seq)’, ‘Retinal neurons
SCENT (CCAT). CCAT, implemented within the SCENT package, (10x)’, ‘Pancreas (10x)’, ‘Peripheral glia (Smart-seq2)’, ‘Skeletal stem cell
was developed as a highly efficient alternative to the original SCENT (C1)’ and ‘HSCs and MPPs (inDrop)’, were obtained from the Sequence
method, SCENT (SR)14. CCAT was applied with the same package, Read Archive (SRA) from NCBI, with study IDs SRP188993, SRP168426,
PPI network, and preprocessing steps described above (‘SCENT SRP200419, SRP109011, SRP239468 and SRP094420, respectively. For
(SR)’) with expression datasets prepared as per documentation ‘Peripheral glia (Smart-seq2)’, we analyzed sample IDs prefixed with
recommendations. ‘E12.5’. Notably, raw FASTQ files were only available for 227 of 473 cells
in the ‘Skeletal stem cell (C1)’ dataset. For the remaining two datasets,
FitDevo. Similar to SCENT (CCAT), FitDevo infers cellular potency ‘Mouse neurogenesis (10x)’ and ‘Mouse mature neural cell types (10x)’,
from the correlation between gene expression and a measure of data were obtained as BAM files from SRA study ID SRP476153.
gene weights20. FitDevo (v.1.2.0) was applied following tutorial instruc- FASTQ files were downloaded using sra-tools v.3.1.1 and processed
tions with binary gene weight matrix downloaded from the same with cutadapt v.4.9 for adaptor trimming of Smart-seq2/C1 reads. For
source (https://github.com/jumphone/FitDevo/#demo-1–infer- preprocessing of inDrop samples, dropest v.0.8.6 was used (according to
developmental-potential-dp-using-expression-matrix-of-scrna- recommended workflow at https://velocyto.org/velocyto.py/tutorial/
seq-data). cli.html#run-dropest-run-on-dropseq-indrops-and-other-techniques).
Reads were mapped and sorted BAM files were generated with STAR
SLICE. SLICE relies on transcriptomic entropy for cellular potency pre- (v.2.7.11b) and Cell Ranger (v.8.0.1) using GRCm39 and GRCh38.p13
diction and lineage reconstruction, estimating entropy over functional reference genomes for mouse and human datasets, respectively. Loom
groups of genes computed from Gene Ontology annotations17. SLICE files containing spliced, unspliced and spanning reads were then gen-
(v.0.99.0) was applied according to demo details from the method’s erated from the BAM files along with corresponding Gene Transfer
GitHub page (https://github.com/xu-lab/SLICE/blob/master/demo/ Format files using the velocyto.py v.0.17.17 Python command line tool.
FB.R). Following quantification of spliced/unspliced counts, the scVelo
v.0.3.1 Python velocity estimation workflow was run as described in the
StemID. StemID infers cellular differentiation trajectories from scRNA- tutorial at https://scvelo.readthedocs.io/en/stable/. For all datasets,
seq data with a clustering-based algorithm analyzing links between both a generalized dynamical model (as detailed at https://scvelo.
clusters16. StemID, implemented in RaceID (v.0.1.4), was run according readthedocs.io/en/stable/DynamicalModeling.html) and a differential
to documentation vignette instructions (https://cran.r-project.org/ kinetics adjusted model with grouping by the CytoTRACE 2 standard-
web/packages/RaceID/vignettes/RaceID.html). For each dataset, an ized phenotypes (as detailed at https://scvelo.readthedocs.io/en/
SCseq object was initialized from each input gene expression matrix stable/DifferentialKinetics.html) were employed. With the excep-
using filterData() with mintotal = 10. Ltree() and compentropy() were tion of random_state in scvelo.pp.neighbors(), which was set to 0 to
then applied consecutively to obtain the StemID score for cell potency. ensure reproducible results, all other parameters were set to those
in the respective vignettes, including min_shared_counts in scvelo.
scTour. scTour implements a deep learning architecture combining a pp.filter_and_normalize(), which was set to 20 for dynamical models
variational autoencoder with a neural ordinary differential equation to and 30 for differential kinetics models. Following velocity estimation,
reconstruct the developmental trajectory of an input scRNA-seq data- cell-internal latent time was inferred using scvelo.tl.latent_time(). The
set, oriented according to gene counts19. scTour (v.1.0.0) was trained resulting outputs were then evaluated via absolute and relative order
and applied to each dataset individually per ‘Model training’ docu- (see ‘Performance assessment’ above) and CytoTRACE 2 outputs were
mentation vignette instructions at https://sctour.readthedocs.io/ assessed over the same cells for comparison (Extended Data Fig. 8 and
en/latest/notebook/scTour_inference_PostInference_adjustment.html. Supplementary Table 14).
Nature Methods
