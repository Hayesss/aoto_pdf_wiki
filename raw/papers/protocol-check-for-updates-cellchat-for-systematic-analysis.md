---
source_path: /mnt/c/Users/Administrator/Zotero/storage/F5JQC3X4/Jin 等 - 2025 - CellChat for systematic analysis of cell–cell communication from single-cell transcriptomics.pdf
ingested: 2026-04-23
sha256: 6c1094060c349149
---

nature protocols https://doi.org/10.1038/s41596-024-01045-4
Protocol Check for updates
CellChat for systematic analysis
of cell–cell communication from
single-cell transcriptomics
Suoqin Jin 1,2 , Maksim V. Plikus 3,4 & Qing Nie 3,4,5
Abstract Key points
Recent advances in single-cell sequencing technologies offer an opportunity • CellChat is a software package
for systematic inference,
to explore cell–cell communication in tissues systematically and with
quantitative analysis and
reduced bias. A key challenge is integrating known molecular interactions and intuitive visualization of cell–cell
communication in an easily
measurements into a framework to identify and analyze complex cell–cell
interpretable way from single-
communication networks. Previously, we developed a computational tool,
cell transcriptomic data; it also
named CellChat, that infers and analyzes cell–cell communication networks enables comparative analysis
of intercellular communication
from single-cell transcriptomic data within an easily interpretable framework.
across different conditions.
CellChat quantifies the signaling communication probability between two cell
• CellChat v2 is an updated
groups using a simplified mass-action-based model, which incorporates the
version that includes additional
core interaction between ligands and receptors with multisubunit structure functionalities for comparative
along with modulation by cofactors. Importantly, CellChat performs a analysis and an expanded
database of ligand–receptor
systematic and comparative analysis of cell–cell communication using a
pairs along with rich functional
variety of quantitative metrics and machine-learning approaches. CellChat annotations.
v2 is an updated version that includes additional comparison functionalities,
an expanded database of ligand–receptor pairs along with rich functional Key references
annotations, and an Interactive CellChat Explorer. Here we provide a step-
by-step protocol for using CellChat v2 on single-cell transcriptomic data,
Jin, S. et al. Nat. Commun. 12,
including inference and analysis of cell–cell communication from one 1088 (2021): https://doi.org/
10.1038/s41467-021-21246-9
dataset and identification of altered intercellular communication, signals
and cell populations from different datasets across biological conditions. Vu, R. et al. Cell Rep. 40, 111155
(2022): https://doi.org/10.1016/
The R implementation of CellChat v2 toolkit and its tutorials together with
j.celrep.2022.111155
the graphic outputs are available at https://github.com/jinworks/CellChat.
This protocol typically takes ~5 min depending on dataset size and requires
a basic understanding of R and single-cell data analysis but no specialized
bioinformatics training for its implementation.
1School of Mathematics and Statistics, Wuhan University, Wuhan, China. 2Hubei Key Laboratory of Computational
Science, Wuhan University, Wuhan, China. 3NSF-Simons Center for Multiscale Cell Fate Research, University of
California, Irvine, Irvine, CA, USA. 4Department of Developmental and Cell Biology, University of California, Irvine,
Irvine, CA, USA. 5Department of Mathematics, University of California, Irvine, Irvine, CA, USA. e-mail: sqjin@
whu.edu.cn; qnie@uci.edu
Nature Protocols | Volume 20 | January 2025 | 180–219 180
Protocol
Introduction
Cell–cell communication orchestrates tissue organization. Recent advances in single-cell
genomics offer unprecedented opportunities to systematically explore signaling mechanisms
for cell fate decisions and their consequent tissue phenotypes. Using single-cell transcriptomic
data and ligand–receptor (L–R) interaction information from prior knowledge, computational
methods such as CellPhoneDB have been developed for inferring cell–cell communication
between groups of cells1–4. However, a versatile and easy-to-use toolkit capable of systematic
analysis and intuitive visualization of cell–cell communication as well as comparison analysis
across biological conditions was still needed, so we developed CellChat to systematically and
comprehensively infer and analyze cell–cell communication from single-cell transcriptomic
data within an easily interpretable framework5.
Development of the protocol
Comprehensive and accurate recapitulation of known molecular interactions is crucial for
predicting biologically meaningful intercellular communications. We manually curated a
literature-supported signaling molecule interaction database called CellChatDB5, which
considers several critical interaction mechanisms that are often neglected. Specifically,
CellChatDB not only incorporates the multisubunit structure of L–R complexes but also
accounts for soluble and membrane-bound stimulatory and inhibitory cofactors such as
agonists, antagonists and coreceptors (Fig. 1). In addition, CellChatDB classifies each L–R pair
into one of the functionally related signaling pathways (for example, WNT, BMP, CXCL and CCL)
to construct cell–cell communication networks at a signaling pathway level, where each link
of the network is computed by summing the interaction strengths of all associated L–R pairs.
Such information allows the interpretation of inferred intercellular communications at a
pathway scale. Moreover, the L–R pairs are categorized into different types, including ‘Secreted
Signaling’, ‘ECM-Receptor’ and ‘Cell–Cell Contact’ (where ECM is extracellular matrix). The
updated CellChat v2 expands upon the original CellChatDB database to include more than
1,000 protein and nonprotein interactions (for example, metabolic and synaptic signaling)
based on the peer-reviewed literature and other existing databases such as CellPhoneDB6
and NeuronChatDB7. In addition, CellChat v2 includes additional functional annotations of
L–R pairs, such as UniProtKB keywords (including biological process, molecular function,
functional class, disease and so on), subcellular location and relevance to neurotransmitter.
To quantify communication between two cell groups mediated by a given ligand and its
cognate receptor, CellChat leverages the law of mass action to associate each interaction with
an interaction score5, which is calculated based on the average expression values of a ligand
by one cell group and that of a receptor by another cell group, as well as their cofactors (Fig. 1).
CellChat uses Hill functions in the simplified mass action model to reflect the saturation
effect of the L–R binding. Significant interactions are identified based on a statistical test
that randomly permutes the group labels of cells. When inferring cell–cell communication,
CellChat computationally scales well with the number of cells and cell groups in the data,
as reflected by the observed running time of ~15 min on a single cell atlas of adult human skin
with ~300,000 cells (Fig. 2). It should be noted that the inferred signaling depends on the
method for calculating average gene expression per cell group. To demonstrate this point, we
used a human skin dataset from atopic dermatitis patients to compare the number of inferred
interactions and the enriched signaling pathways when using ‘triMean’, ‘truncatedMean’ with
‘trim = 0.1’ and ‘truncatedMean’ with ‘trim = 0.05’, respectively (Procedure 1; Fig. 3a,b). The
most stringent method, called ‘triMean’, produces fewer but stronger interactions, whereas
the ‘truncated Mean’ method, with smaller values of ‘trim’ parameter (for example, ‘trim = 0.1’),
outputs more interactions, leading to the detection of weak signaling.
To obtain biological insights from many complicated cell–cell communication networks,
CellChat employs quantitative analysis and machine learning approaches for various critical
analysis tasks5 (Fig. 1). First, to identify critical microenvironment components, CellChat
determines major signaling sources and targets, as well as mediators and influencers within
Nature Protocols | Volume 20 | January 2025 | 180–219 181
Protocol
Input
Ligands
Receptors
a given signaling network using network centrality analysis. Second, to reveal how cells and
signals coordinate together and to explore their communication patterns, CellChat predicts key
incoming and outgoing signals for specific cell types, as well as coordinated responses among
different cell types by leveraging pattern recognition approaches. Outgoing patterns reveal how
sender cells (that is, cells acting as signal sources) coordinate with each other, as well as how
they coordinate with certain signaling pathways to drive communication. Incoming patterns
show how target cells (that is, cells acting as signal receivers) coordinate with each other to
respond to incoming signals. Third, to predict signaling groups sharing similar communication
Nature Protocols | Volume 20 | January 2025 | 180–219 182
1 tinubuS 2 tinubuS
Agonist Antagonist
yrotibihnioC
rotpecer
yrotalumitsoC
rotpecer
Output
Single-cell data Cellular communication modeling Visualization
(Procedure 1, Steps 1–3) (Procedure 1, Steps 7–14) (Procedure 1, Steps 16–21)
L–R database
(Procedure 1, Steps 4–6)
Communication network modeling
(Procedure 1, Steps 22–25)
Systematic analysis of cell–cell communication from one dataset (Procedure 1, Steps 22–25)
CellChatDB
Pattern recognition
Manifold learning and classification
CXCL Normal
BMP Diseased CCL CXCL BMP
CCL
FGF FGF WNT WNT
High-dimensional cell–cell Reduced-dimensional
communication networks manifold
sepyt
lleC
Patterns
snrettaP
CellChat
Expression profile Law of mass action Statistical analysis
AG AN
K2 K3
+
L R K1 LR
K1[L][R];
K2
[
+
A G
[A
]
G] K3 +
K
[
3
AN]
Cells (with assigned labels)
Signaling
seneG
Circle plot Hierarchy plot Chord diagram
Signaling to C1/C2/C3 Signaling to C4/C5/C6 C5
S
A
o
u
u
t
r
o
c
c
e
rin
Ta
e
rg
P
e
a
t
r
S
ac
o
r
u
in
rc
e
e So
P
u
ar
r
a
c
c
e
ri
T
n
a
e
rg
A
e
u
t
to
S
c
o
ri
u
n
r
e
ce C4
C6
C1 C4 C1 C4
C2 C5 C2 C5
3C
1C
C3 C6 C3 C6 C2
Heatmap Bubble plot
L1–R1
L1–R2
L2–R1
L2–R3
L3–R4
L5–R6
C1 →
C
C
2
1 →
C
C
3
1 →
C
C
4
1 →
C
C
5
1 →
C6
Sender Mediator
Identification of signaling roles for cells Discovery of cell group and
using network centraility analysis signaling’s coordinated behavior
Receiver Influencer
Comparative analysis across biological conditions
(Procedure 2, Steps 1–13; Procedure 3, Steps 1–4)
)sredneS(
secruoS
Targets (Receivers)
C4
C5
C6
C3
C1 C2
Outgoing centrality score
erocs
ytilartnec
gnimocnI
C1 FGF
C2 P1 P1 V C E C G L F
CXCL
C3 CSF
C4 P2 P2 C T D N 4 F 0
C5 WNT
GAS C6 P3 P3 TGFb
Cell groups Patterns Signaling
Specific signaling
Shared Specific Shared
Dim 1
2
miD
gnilangiS
CXCL
WNT
Information flow
snoitcaretni
fo rebmuN
Up
0 Down
gnilangiS
Cell groups
)redneS(
secruoS
C3 C2
C4 C1
C5 C6
Social network theory and metrics
Targets (Receivers)
secruoS
3D communication probability array
Targets
L–R
pairs or
pathways
(~3,300 L–R pairs)
Influencer
Mediator Receiver
Sender
;
Word cloud
......
12% Secreted Signaling 38%20% ECM−Receptor
Cell−Cell Contact 30%
Non-protein Signaling
45% Heterodimers
55% Others
Rich annotations of L–R pairs ••Classification (e.g., secreted)
••Signaling pathways (e.g., WNT)
••UniProtKB keywords (e.g., GO, functional class, disease) ••Subcellular location
••Neurotransmitter
Fig. 1 | Overview of CellChat along with the procedure step numbers. Left: identifies significant communications using permutation tests. The inferred
required input data and the L–R interaction database CellChatDB. CellChat’s communication probabilities among all pairs of cell groups across all L–R pairs or
input data consist of gene expression data and cell group information. signaling pathways are represented by a three-dimensional (3D) array. CellChat
CellChatDB considers known composition of the L–R complexes, including analyzes the inferred networks by leveraging social network metrics, pattern
complexes with multimeric ligands and receptors, as well as several cofactor recognition methods, and manifold learning approaches. Right: CellChat offers
types: soluble agonists, antagonists, costimulatory and coinhibitory membrane- several intuitive visualization outputs to facilitate data interpretation of different
bound receptors. Rich annotations of all L–R pairs are provided. Middle: CellChat analytical tasks. In addition to analyzing individual datasets, CellChat also
models the communication probability based on the law of mass action and delineates signaling changes across different conditions.
Protocol
4
2.7
2.1 2.2
2
1.6 1.6 1.7
0
6 8 12 18 22 32
Number of cell groups
architecture and interpret the biological functions of poorly studied pathways, CellChat groups
signaling pathways by defining similarity measures and performing manifold learning from
both functional and topological perspectives5.
To identify signaling changes across conditions, CellChat identifies altered signaling
pathways and L–R pairs in terms of network architecture and interaction strength by performing
joint manifold learning and information flow comparison analysis5. Compared to the original
CellChat tool, CellChat v2 provides additional functionalities to allow systematic comparisons
between multiple conditions. CellChat v2 first focuses on the overall signaling changes at the
cell population level and then narrows down to altered signaling pathways and L–R pairs5,8,9
(Fig. 1). Specifically, CellChat v2 identifies which interactions between two specific cell groups
changed notably, as well as the cell group identities showing notable changes in sending or
receiving signaling patterns across conditions. To identify substantially upregulated and
downregulated L–R pairs across conditions, CellChat v2 combines cell–cell communication
analysis with differential gene expression analysis and quantifies the enrichment of L–R pairs
for each condition by defining an enrichment score8.
Nature Protocols | Volume 20 | January 2025 | 180–219 183
)nim(
emit
gninnuR
Calculating average gene expression
using trimean (20,000 cells)
5.5
4.3
4 3.9
3.3
2.6 2.7
2
0
6 8 12 18 22 32
Number of cell groups
)nim(
emit
gninnuR
15 14.3
10 9.6
4.9
5
2.4
1.1 1.4 1.6 1.9
0
5,000 10,000 20,000 30,000 50,000 100,000 200,000 300,000 5,000 10,000 20,000 30,000 50,000 100,000 200,000 300,000
Number of cells Number of cells
Calculating average gene expression
using truncated mean (trim = 10%; 20,000 cells)
)nim(
emit
gninnuR
Calculating average gene expression
using trimean
16.4
15
10.9
10
5
5
3.8
2.6 2.7 2.9 3.3
0
)nim(
emit
gninnuR
a b
Calculating average gene expression
using truncated mean (trim = 10%)
c d
Fig. 2 | CellChat running time in relation to the increase of cell numbers and cell groups. a,b, Running time over
different cell numbers in the data when calculating average gene expression per cell group using trimean (a) or 10%
truncated mean (b). c,d, Running time over different numbers of cell groups in the data (no. 20,000 cells) when calculating
average gene expression per cell group using trimean (c) or 10% truncated mean (d). Here, the running time is the total time
when running Steps 1–8 and 11–14 in Procedure 1.
Protocol
MIF MIF
GALECTIN
MIF GALECTIN CXCL
CXCL COMPLEMENT
PTN
COMPLEMENT TNF
GALECTIN
PTN FGF
ANGPTL
TNF CCL
140 CXCL FGF IL4
GAS
CCL SPP1
GAS VISFATIN
COMPLEMENT IL4 PERIOSTIN
LIGHT
100 SPP1 CD40
82 FGF PERIOSTIN PD M G K F
ANGPTL PARs
CD40 IL1
ANNEXIN
50 TNF LIGHT CSF
PARs SEMA3 TGFb
VISFATIN PROS
19 CCL IL1 LT
IL16
PDGF VEGF
0 GAS CSF IFN−II
EGF
PROS GRN
TGFb CD70
IL4 VEGF O F X L 4 T 0 3
IFN−II CALCR
Methods for calculating average ncWNT
gene expression per cell group CD40 CD70 OSM
IL16 BAG
SEMA3 CD30
FASLG
LIGHT LT RANKL
EGF TWEAK
CHEMERIN
CALCR IL2
CSF
FLT3 CD137
BTLA
OSM IGF
VEGF ncWNT IL10
PTH
CD30 WNT
Information flow Information flow Information flow
Moreover, CellChat v2 offers an interactive web browser function to allow intuitive
exploration and visualization of CellChat outputs (Fig. 4). To facilitate intuitive user-guided
data interpretation, CellChat v2 provides a variety of visualization outputs, including circle plot,
chord diagram, heatmap, hierarchy plot, bubble plot and word cloud (Fig. 1).
Comparison with other methods
Numerous computational tools have been developed to facilitate cell–cell communication
exploration and analysis2,10–18. The cell–cell communication inference depends on the reference
databases of known L–R interactions. The Python tool CellPhoneDB12,19 is a pioneering method
that considers multiple subunits of ligands and receptors to accurately represent known
heteromeric molecular complexes. Two other R-based tools, CellChat5 and ICELLNET15, adopted
the subunit architecture of heteromeric complexes and other tools have since followed their
lead. Compared with CellPhoneDB and CellChat, which have over 2,000 L–R interactions,
ICELLNET only has 380 interactions, resulting in partial characterization of signaling pathways.
Recently, CellPhoneDB v420 added interactions of nonprotein molecules not directly encoded
by genes, and NeuronChat7 was designed specifically for neuron-to-neuron communication
mediated by neurotransmitters. In CellChat v2, we add new literature-supported interactions,
Nature Protocols | Volume 20 | January 2025 | 180–219 184
sriap
noitcaretni
derrefni
fo
rebmuN
b
a
Trimean
Truncated mean (trim = 10%)
Truncated mean (trim = 5%)
Fig. 3 | Comparison of the number of inferred L–R pairs and the identified 5% truncated mean. The most stringent method ‘triMean’ produces fewer but
signaling pathways when using different methods for calculating average stronger interactions, while the ‘truncated Mean’ method with smaller values
gene expression per cell group. a, The number of inferred L–R pairs when of ‘trim’ parameter enables the identification of weak signaling. This analysis
using three different methods for calculating average gene expression per cell is performed on a human skin dataset from atopic dermatitis patients with
group, including trimean, 10% truncated mean and 5% truncated mean. b, The 5,011 cells and 12 cell groups.
identified signaling pathways when using trimean, 10% truncated mean and
Protocol
Plotly powered exploration to
Rich user-guided highlight one cell group
sliders in each panel and many others
Click one cell to show
its attributes
Specialized feature plot
for signaling analysis
Fig. 4 | Overview of the Interactive CellChat Explorer created by cell groups and signaling expression, (2) examines the inferred signaling between
runCellChatApp function in the R package. To facilitate the exploration of different cell groups and (3) further visualizes the individual signaling pathway.
cell–cell communication, CellChat allows the end-user to visualize and explore Rich user-guided sliders are provided for flexible exploration, highlight and
the data and the inferred signaling interactively. CellChat Explorer (1) visualizes zoom-out of the related information of interest.
Nature Protocols | Volume 20 | January 2025 | 180–219 185
Protocol
including both proteins and nonproteins acting as ligands, leading to a total of ~3,300
interactions for both mouse and human. Four unique features of CellChatDB v2 are:
1. Incorporation of soluble and membrane-bound stimulatory and inhibitory cofactors.
This feature is considered because many pathways, such as BMP and WNT, are prominently
modulated, positively or negatively, by their cofactors.
2. Categorization of L–R pairs into different types, including ‘Secreted Signaling’,
‘ECM-Receptor’, ‘Cell–Cell Contact’ and ‘Non-protein Signaling’. This feature greatly
facilitates cell–cell communication analysis within a particular type.
3. Classification of L–R pairs into functionally related signaling pathways. This feature
provides useful insights into signaling mechanisms by examining cell–cell communication
at a signaling pathway scale.
4. Rich annotations of each L–R pair. This feature is useful for selecting L–R pairs with similar
biological functions and interpreting the downstream analysis.
Despite the adoption of different built-in L–R databases, current tools for cell–cell
communication inference are all somewhat distinct in their performance, visualization
outputs and downstream analysis. Two recent systematic evaluations of more than 15 cell–cell
communication inference methods suggest CellChat is among the top-performing methods11,18.
In addition to the high accuracy of cell–cell communication inference, CellChat offers a variety
of visualization outputs that allow multiple intuitive user-guided interpretations of the complex
cell–cell communication. Another key unique feature of CellChat is its ability to analyze the
inferred cell–cell communications using a systems approach. Methods and concepts from
social network analysis, pattern recognition and manifold learning are adapted to derive higher-
order network information in an easily interpretable way. Moreover, CellChat is the pioneering
method for the systematic comparison of communications inferred for different conditions,
which is critically important for identifying altered signaling mechanisms responsible
for cell fate decisions in single-cell studies. Afterwards, methods such as Connectome16,
Tensor-cell2cell17 and multinichenetr21 introduced functionalities for comparison across
multiple conditions.
Applications of the method
So far, CellChat has been widely used in a broad range of biological systems to dissect signaling
mechanisms during tissue homeostasis, development and disease22. In our original report5,
we applied CellChat to a small conditional RNA sequencing (scRNA-seq) dataset on mouse
skin development and predicted a novel role of Edn3 signaling in stimulating the directed
migration of melanocytes into placodes during hair follicle formation. Comparative analysis
of nonlesional and lesional human skin from patients with atopic dermatitis using CellChat
uncovered major signaling changes in response to disease. CCL19-CCR7 was identified as the
most important signaling event activated in lesional skin, contributing to the communication
from inflammatory fibroblasts to dendritic cells. Recently, we used CellChat to study
aging-dependent dysregulations during skin wound healing in mice8, showing system-level
differences in the number, strength, route and signaling mediators of putative cell–cell
communications in young versus aged skin wounds.
Using CellChat, a previous study found a strong increase of key inflammatory pathways in
the choroid-to-cortex network in patients with coronavirus disease 2019 (COVID-19) compared
with control individuals23. Another study revealed increased interactions of CD163/LGMN-
macrophages with myofibroblasts, fibroblasts and pericytes at later time points of COVID-19-
induced ‘acute respiratory distress syndrome’24. In a single-cell atlas of the adult human cerebral
vasculature25, CellChat analysis identified Nd2 as the strongest contributor to abnormal cell
communications in arteriovenous malformations. Recently, state- and niche-dependent
signaling pathways for reparative states in proximal and distal tubules have been identified
by mining healthy and injured human kidney single-cell atlases26. Comparative analysis of
Gabbr1 mutant and control cortices from adult mice uncovered alterations in astrocyte–neuron
communication27. CellChat has been used to predict a new role for a unique subset of cancer-
associated fibroblasts in recruiting monocytes and neutrophils using in situ tumor arrays28.
Nature Protocols | Volume 20 | January 2025 | 180–219 186
Protocol
A study of PD1 blockade in mismatch repair-deficient colorectal cancer identified an interaction
between CD4+ T helper cells and germinal center B cells in antitumor immunity during immune
checkpoint inhibitor treatment29.
Limitations
It is possible that there are missing L–R interactions not covered in CellChatDB. Guidelines
to update CellChatDB by adding user-defined L–R pairs or integrating other resources are
provided in Box 1. There are several other limitations to the original CellChat and its updated
version (v2), including the following:
• CellChat infers potential interactions between cell groups without considering heterogeneity
within the defined cell groups. Users can refine cell grouping via subclustering analysis before
applying CellChat.
• Like other methods, CellChat is limited to hypothesis generation and employs heuristics to
guide the interpretation of cell–cell communication outputs. With limited benchmarking
studies10,11,18, the question of how to better validate the inferred signaling networks and their
downstream gene outputs remains to be answered.
• Cross-condition analysis in CellChat is largely restricted to pairwise comparisons.
Identification of signaling changes across multiple conditions and time series is valuable.
• For nonprotein-mediated cellular communication such as metabolic or synaptic signaling
(where molecules are not directly encoded by genes measured in scRNA-seq), CellChat v2
approximately estimates the expression of ligands and receptors using the molecules’ key
mediators or enzymes. More sophisticated computational methods for estimating the
expression of those signaling molecules could likely improve the inference accuracy.
• Given that cell–cell communication occurs within a short spatial distance and at the protein
level, newly emerging data modalities (for example, spatially resolved transcriptomics22,30,31
and single-cell multiomics such as single-cell proteomics32 and epigenomics33–35) can be
used to improve the inference of cell–cell communication. Recently, several methods
have been developed for spatially resolved transcriptomics4, such as SpaOTsc36, SpaTalk37,
COMMOT38, CellPhoneDB v313 and HoloNet39, which are better at detecting spatially
proximal cell–cell communication.
• CellChat employs a simplified mass-action-based model to quantify communication
probability between a given ligand and its cognate receptor, and models with more
biochemical details can potentially improve inference predictions. Finally, incorporation
of the downstream signaling events of activated receptors on receiving cells could further
improve the overall inference accuracy40–44.
Overview of the procedure
Procedure 1 demonstrates the steps to run the CellChat package for inferring (Steps 1–15),
visualizing (Steps 16–21) and analyzing (Steps 22–27) cell–cell communication from a single
scRNA-seq dataset. Specifically, Procedure 1 includes the preprocessing of the input data
(Steps 1–9) and the inference of cell–cell communication at both a L–R pair level and a signaling
pathway level (Steps 10–15), the visualization of cell–cell communication networks of individual
(Steps 16–19) and multiple (Step 20) signaling pathways or L–R pairs, the identification of the
signaling roles and major contributing genes and pathways between cell groups (Steps 22–23),
the analysis of global communication patterns (Step 24) and the manifold learning and
classification analysis of signaling networks (Step 25), as well as the interactive exploration
of the inferred cell–cell communication through a CellChat Shiny App (Step 26).
Procedure 2 demonstrates CellChat’s ability to perform comparative analysis across
different biological conditions by quantitative contrasts and joint manifold learning, including
merging different CellChat objects together (Steps 1–4), detecting altered interactions and
cell populations (Steps 5–9), altered signaling with distinct network architecture (Step 10)
and interaction strength (Steps 11–13), as well as visually comparing the inferred cell–cell
communication networks (Steps 14–15).
Procedure 3 briefly demonstrates how to apply CellChat to the comparative analysis of
multiple conditions with differing cell type compositions (Steps 1–5).
Nature Protocols | Volume 20 | January 2025 | 180–219 187
Protocol
BOX 1
Updating the L–R interaction database CellChatDB
In this box, we demonstrate the use of the function ‘updateCellChatDB’ to update the L–R interaction database CellChatDB by integrating
new L–R pairs from other cell–cell communication analysis tools or utilizing a custom L–R interaction database.
Additional material:
Input data:
• Customized L–R pairs: a data frame with at least two columns named ‘ligand’ and ‘receptor’. To infer cell–cell communication at a signaling
pathway level, another column named ‘pathway_name’ must be provided, which classifies each L–R pair into one of known signaling pathways
• (Optional) Additional input files: (1) gene information: a data frame with one column named as ‘Symbol’; (2) complex information: a data
frame in which each row is the subunit information of either ligand or receptor; and (3) cofactor information: a data frame in which each row
is the cofactor information of each pair
▲ CRITICAL Users can check the details of the required input data in the online tutorial (https://htmlpreview.github.io/?https://github.
com/jinworks/CellChat/blob/master/tutorial/Update-CellChatDB.html), particularly the example codes on how to utilize other resources
such as CellTalkDB and CellPhoneDB.
Procedure
▲ CRITICAL To demonstrate how to update the L–R interaction database, we use CellTalkDB50 in human as an example. CellTalkDB can be
downloaded from https://github.com/ZJUFanLab/CellTalkDB.
1. Load the customized L–R pairs by typing the following command in RStudio:
db.user <- readRDS("./CellTalkDB-master/database/human_lr_pair.rds")
2. (Optional) Load the gene information:
gene_info <- readRDS("./CellTalkDB-master/data/human_gene_info.rds")
3. (Optional) Modify the colnames if needed
colnames(db.user) <- plyr::mapvalues(colnames(db.user), from = c("ligand_gene_symbol","receptor_gene_
symbol","lr_pair"), to = c("ligand","receptor","interaction_name"), warn_missing = TRUE)
4. Create a new database by using the user-provided gene information (option A), create a new database by using the built-in gene
information (option B) or integrate the customized L–R pairs into the built-in CellChatDB (option C).
A. Create a new database by using the user-provided gene information:
db.new <- CellChat::updateCellChatDB(db = db.user, gene_info = gene_info)
B. Create a new database by using the built-in gene information:
db.new <- CellChat::updateCellChatDB(db = db.user, gene_info = NULL, species_target = "human")
C. Integrate the customized L–R pairs into the built-in CellChatDB:
db.new <- updateCellChatDB(db = db.user, merged = TRUE, species_target = "human")
5. Use this new database in the Procedure 1, Step 6 for CellChat analysis
cellchat@DB <- db.new
6. Save the new database for future use
save(db.new, file = "CellChatDB.human_user.rda")
Nature Protocols | Volume 20 | January 2025 | 180–219 188
Protocol
Experimental design
RNA isolation and sequencing data
Although CellChat can, in principle, be used for any single-cell transcriptomics datasets, the
quality of datasets directly affects the quality of CellChat outputs. First, having sufficient
sequencing depth is critical to capturing gene expression of ligands and receptors. Expression
levels are usually low for ligands during development, so sensitivity and depth of sequencing
become particularly important for such cases. Second, batch effect may introduce output
variability for any inference method, including CellChat. Whenever possible, it is important to
use the same RNA isolation protocol for replicates and different conditions. To perform control
analysis, we include several datasets that have been well explored using CellChat with known
signaling events or pathways. New CellChat users are encouraged to first test their CellChat code
on these datasets by comparing the outputs with the deposited cell–cell communication results.
Required input data
CellChat requires two user inputs: one is the gene expression data of cells and the other is the
user-assigned cell labels. For the gene expression data matrix, genes should be in rows with
rownames and cells in columns with colnames. Normalized data are required as input for
CellChat analysis (for example, library-size normalization and then log-transformed with a
pseudocount of 1). If users input raw count data, CellChat provides a ‘normalizeData’ function
for normalization. For the cell group information, a dataframe with rownames is required.
Alternatively, users can use a Seurat, SingleCellExperiment or AnnData object as input.
Inference of cell–cell communication networks
To identify strong or weak cell–cell communications, users can modify the parameters ‘type’
and ‘trim’ in the function ‘computeCommunProb’ when inferring cell–cell communication
networks. The parameter ‘type’ is the method for computing the average gene expression
per cell group. By default, CellChat uses a statistically robust mean method by setting
‘type = "triMean"’, producing fewer but stronger interactions. When setting ‘type =
"truncatedMean"’, a value should be assigned to another parameter ‘trim’, producing more
interactions. However, we find that CellChat performs well at predicting stronger interactions,
which is helpful for identifying interactions for further experimental validations. The ‘trimean’
approximates 25% truncated mean, implying that the average gene expression is zero if the
percentage of expressing cells in one group is less than 25%. To identify weak signaling, users
should use ‘truncatedMean’. In general, users can use 10% truncated mean by setting ‘type =
"truncatedMean"’ and ‘trim = 0.1’. To determine a proper value of ‘trim’, CellChat provides
a function ‘computeAveExpr’, which can help to check the average expression of signaling
genes of interest. Therefore, if well-known signaling events in the studied biological process are
not predicted, users can try ‘truncatedMean’ with lower values of ‘trim’ to change the method
for calculating the average gene expression per cell group.
Visualization of cell–cell communication networks
Upon inferring the cell–cell communication networks, CellChat provides various ways to
visualize such networks, including hierarchical plots, circle plots, chord diagrams, heatmap and
bubble plots. In hierarchical plots, circle plots and chord diagrams, edge colors are consistent
with the sources as sender, and edge weights are proportional to the interaction strength.
Thicker edge lines indicate a stronger signal. One can visualize the inferred communication
network of signaling pathways using ‘netVisual_aggregate’ and visualize the inferred
communication networks of individual L–R pairs associated with that signaling pathway
using ‘netVisual_individual’.
Hierarchical plots consist of two components: the left portion shows autocrine and
paracrine signaling to certain cell groups of interest, and the right portion shows autocrine
and paracrine signaling to the remaining cell groups in the dataset. Thus, a hierarchical plot
provides an informative and intuitive way to visualize autocrine and paracrine signaling
communications between cell groups of interest. In the hierarchical plot, solid and open
circles represent the sources and targets, respectively.
Nature Protocols | Volume 20 | January 2025 | 180–219 189
Protocol
In addition to creating a chord diagram using ‘netVisual_aggregate’ or ‘netVisual_
individual’, CellChat provides another two functions with more adjustable parameters for better
visualization. ‘netVisual_chord_cell’ is used for visualizing the cell–cell communication
between different cell groups (where each sector in the chord diagram is a cell group) and
‘netVisual_chord_gene’ is used for visualizing the cell–cell communication mediated by multiple
L–Rs or signaling pathways (where each sector in the chord diagram is a ligand, receptor or signaling
pathway). In the chord diagram, the inner thinner bar colors represent the targets that receive signals
from the corresponding outer bar. The inner bar size is proportional to the signal strength received by
the targets. Such an inner bar is helpful for interpreting the complex chord diagram.
Systematic analysis of cell–cell communication
To facilitate the interpretation of complex intercellular communication networks, CellChat
quantitively measures networks through methods abstracted from graph theory, pattern
recognition and manifold learning. It can determine major signaling sources and targets, as well
as mediators and influencers within a given signaling network, using centrality measures from
network analysis. It can also predict key incoming and outgoing signals for specific cell types
as well as coordinated responses among different cell types by leveraging pattern recognition
approaches. Finally, it can group signaling pathways by defining similarity measures and
performing manifold learning from both functional and topological perspectives.
CellChat identifies dominant senders, receivers, mediators and influencers in the
intercellular communication network using measures in weighted-directed networks, including
out-degree, in-degree, flow betweenness and information centrality5,45, respectively. In a
weighted directed network with the weights as the computed communication probabilities,
the outdegree (computed as the sum of communication probabilities of the outgoing signaling
from a cell group) and the in-degree (computed as the sum of the communication probabilities
of the incoming signaling to a cell group) can be used to identify the dominant cell senders
and receivers of signaling networks, respectively. CellChat also provides another intuitive way
to visualize the dominant senders (sources) and receivers (targets) in a two-dimensional (2D)
space using the function ‘netAnalysis_signalingRole_scatter’. In this plot, the x axis and
y axis are, respectively, the total outgoing or incoming communication probability associated
with each cell group. Dot size is proportional to the number of inferred links (both outgoing and
incoming) associated with each cell group. The dot colors indicate different cell groups. The dot
shapes indicate different categories of cell groups if the parameter ‘group’ is defined.
CellChat predict key incoming and outgoing signals for specific cell types using the
function ‘netAnalysis_signalingRole_heatmap’. In this heatmap, colorbar represents
the relative signaling strength of a signaling pathway across cell groups. The top-colored bar
plot shows the total signaling strength of a cell group by summarizing all signaling pathways
displayed in the heatmap. The right bar plot shows the total signaling strength of a signaling
pathway by summarizing all cell groups displayed in the heatmap.
CellChat employs a pattern recognition method to identify global communication
patterns. For outgoing (or incoming) patterns, the cell group pattern indicates how these cell
groups coordinate to send (or receive) signals and the signaling pathway pattern indicates how
these signaling pathways work together to send (or receive) signals. To intuitively show the
associations of latent patterns with cell groups and signaling pathways or L–R pairs, we used a
river (alluvial) plot. As the number of patterns increases, there might be redundant patterns,
making it difficult to interpret the communication patterns. In addition, CellChat also provides
the function ‘selectK’ to infer the number of patterns, which is based on two metrics including
Cophenetic and Silhouette. Both metrics measure the stability for a particular number of
patterns based on a hierarchical clustering of the consensus matrix. A suitable number of
patterns is the one at which Cophenetic and Silhouette values begin to drop suddenly.
CellChat can quantify the similarity between all significant signaling pathways and then group
them based on their cellular communication network similarity. This analysis is helpful to predict
putative functions of the poorly studied pathways based on their similarity to pathways with
well-known functions. Signaling pathways can be grouped based on their functional similarity or
structural similarity. A high degree of functional similarity indicates the major senders and receivers
Nature Protocols | Volume 20 | January 2025 | 180–219 190
Protocol
are similar and can be interpreted as the two signaling pathways or two L–R pairs exhibiting similar
and/or redundant roles. A structural similarity relates to signaling network structure, without
considering the similarity of senders and receivers. To obtain a manifold embedding of all inferred
communication networks and further intuitively visualize these networks in a 2D space, we first
compute the pairwise functional or topological similarity between any pair of inferred networks,
then smooth the similarity matrix using a shared nearest-neighbor graph, and finally perform a
uniform manifold approximation and projection (UMAP) on the smoothed similarity matrix.
Comparative analysis of cell–cell communication
CellChat provides versatile functionalities to allow systematic comparisons of cell–cell
communication between different conditions. Here we present two examples of how we design
the comparative analysis. CellChat shows the differential number of interactions or interaction
strengths between pairs of scRNA-seq datasets in greater detail using the function ‘netVisual_
heatmap’. In this heatmap, the top-colored bar plot represents the sum of each column of the
absolute values displayed in the heatmap (incoming signaling). The right-colored bar plot
represents the sum of each row of the absolute values (outgoing signaling). Therefore, the bar
height indicates the degree of change in terms of the number of interactions or interaction
strength between the two conditions. The colorbar indicates increased (or decreased) signaling
in the second dataset compared to the first one.
CellChat performs joint manifold learning and classification of all inferred communication
networks across different conditions. The manifold embeddings are obtained by first computing
the pairwise functional or topological similarity between any pair of inferred networks and then
performing UMAP on a shared nearest neighbor-smoothed similarity matrix. UMAP is used for
visualizing signaling relationships and interpreting our signaling outputs in an intuitive way
without requiring classification of conditions. By quantifying the similarity between the cellular
communication networks of signaling pathways across conditions, this analysis highlights
the potentially altered signaling pathways. CellChat adopts the concept of network rewiring
from network biology and is based on the hypothesis that the difference between different
communication networks may affect biological processes across conditions. Furthermore,
CellChat identifies the signaling networks with larger differences across conditions based on
their Euclidean distance in the 2D UMAP space. CellChat computes and visualizes this Euclidean
distance using the function ‘rankSimilarity’. Larger distance implies larger difference of
the communication networks between two datasets in terms of either functional or structure
similarity. CellChat only computes the distance of overlapping signaling pathways between two
datasets. Those signaling pathways that are only identified in one dataset are not included in this
analysis. If there are more than three datasets, you can do pairwise comparisons by modifying
the parameter ‘comparison’ in ‘rankSimilarity’.
Materials
Equipment
Hardware
• Any desktop workstation or laptop with an Internet connection is sufficient. This protocol
was run on a MacBook Pro (MacOS Ventura Monterey, Version 13.5) with a 12-Core central
processing unit (CPU) and 64 GB of random-access memory (RAM). For minimal performance,
we recommend using a dual-core CPU with at least 16 GB of RAM for analyses
Software
• Operating system: Linux, Windows (10) or MacOS
• RStudio: an integrated development environment for R, which can be accessed at
https://posit.co/download/rstudio-desktop/
• CellChat: the actively maintained open-source program is freely available at https://github.
com/jinworks/CellChat
Nature Protocols | Volume 20 | January 2025 | 180–219 191
Protocol
Data files
Required input data:
• Gene expression data matrix
• User-assigned cell labels
Example datasets: example datasets for running this protocol can be downloaded from
the open-access repository figshare at https://figshare.com/projects/Example_data_for_cell-
cell_communication_analysis_using_CellChat/157272.
Equipment setup
Installation of CellChat package
We recommend that users install CellChat and perform analysis in RStudio. In an RStudio
environment, the following commands can be run from an R script or directly in the built-in R
console. The R commands are the same on MacOS, Linux and Windows.
(Optional) Install RStudio. RStudio can be manually installed by downloading RStudio from
its official website at https://posit.co/download/rstudio-desktop/.
1. (Optional) Install the devtools package from the Comprensive R Archive Network.
install.packages('devtools')
2. Install CellChat R packages from our GitHub repository by typing the following commands:
devtools::install_github("jinworks/CellChat")
Procedure 1: inferring cell–cell communication from a single scRNA-seq dataset
● TIMING 4 min
▲ CRITICAL Procedure 1 demonstrates the R commands needed to run the CellChat package
for inferring and analyzing cell–cell communication from a single scRNA-seq dataset. The
equivalent online version, along with the graphical plots, are available in the tutorial directory
of the CellChat github repository (https://htmlpreview.github.io/?https://github.com/
jinworks/CellChat/blob/master/tutorial/CellChat-vignette.html).
Data input and preprocessing
● TIMING ~12 s
▲ CRITICAL The example dataset containing single-cell data and cell metadata can be
accessed directly from figshare via the following link: https://figshare.com/articles/dataset/
scRNA-seq_data_of_human_skin_from_patients_with_atopic_dermatitis/24470719. Users can
refer to the online tutorial of the CellChat github repository (https://htmlpreview.github.io/
?https://github.com/jinworks/CellChat/blob/master/tutorial/Interface_with_other_single-cell_
analysis_toolkits.html) for further details on preparing the input data for CellChat analysis.
1. Prepare the input data by following option A when the normalized count data and
metadata are available, option B when the Seurat object is available, option C when
the SingleCellExperiment object is available and option D when the Anndata object is
available.
(A) Generate data input starting from a count data matrix:
(i) Upload the count data matrix in a .rda or other format:
load("./tutorial/data_humanSkin_CellChat.rda")
(ii) Obtain the normalized data matrix:
data.input = data_humanSkin$data
Nature Protocols | Volume 20 | January 2025 | 180–219 192
Protocol
(iii) Generate a data frame with rown ames containing cell meta data:
meta = data_humanSkin$meta
(iv) Subset the data from one condition for further analysis:
cell.use = rownames(meta)[meta$condition == "LS"]
data.input = data.input[, cell.use]
meta = meta[cell.use,]
(B) Generate data input starting from a Seurat object:
(i) Obtain the normalized data matrix:
data.input <- seurat_object[["RNA"]]@data
(ii) Generate a data frame with row names containing cell meta data:
labels <- Seurat::Idents(seurat.obj)
meta <- data.frame(labels = labels, row.names = names(labels))
(C) Generate data input starting from a SingleCellExperiment object:
(i) Obtain the normalized data matrix:
data.input <- SingleCellExperiment::logcounts(sce_object)
(ii) Generate a data frame with row names containing cell meta data:
meta <- as.data.frame(SingleCellExperiment::colData(sce_object))
meta$labels <- meta[["sce.clusters"]]
(D) Generate data input starting from an Anndata object:
(i) Upload the Anndata object using the anndata R package:
install.packages("anndata")
library(anndata)
ad <- read_h5ad("scanpy_object.h5ad")
(ii) Obtain the count data matrix:
counts <- t(as.matrix(ad$X))
(iii) Normalize the count data matrix:
data.input <- normalizeData(counts)
(iv) Generate a data frame with row names containing cell meta data:
meta <- ad$obs
meta$labels <- meta[["ad_clusters"]]
2. Using the ‘createCellChat’ function and the input data files generated in Step 1, create a
CellChat object by following option A if taking the digital gene expression matrix and cell
label information as input, option B if taking a Seurat object as input, option C if taking
a SingleCellExperiment object as input and option D if taking a AnnData object as input.
Nature Protocols | Volume 20 | January 2025 | 180–219 193
Protocol
Users should refer to the ‘Required input data’ section in the ‘Experimental design’ section
for further details.
(A) Create a CellChat object from the digital gene expression matrix and cell label
information
library(CellChat)
cellchat <- createCellChat(object = data.input, meta = meta,
group.by = "labels")
(B) Create a CellChat object from a Seurat object
library(CellChat)
cellchat <- createCellChat(object = seurat.obj, group.by =
"ident", assay = "RNA")
(C) Create a CellChat object from a SingleCellExperiment object
library(CellChat)
cellchat <- createCellChat(object = sce.obj, group.by = "sce.clusters")
(D) Create a CellChat object from an AnnData object
(i) Convert the Anndata object to the SingleCellExperiment object using the zellkon-
verter R package:
sce <- zellkonverter::readH5AD(file = "adata.h5ad")
assayNames(sce)
(ii) Obtain the count data matrix:
counts <- assay(sce, "X")
(iii) Normalize the count data matrix and add a new assay entry ‘logcounts’ if not available:
logcounts(sce) <- normalizeData(counts)
(iv) Generate a CellChat object from a SingleCellExperiment object:
cellchat <- createCellChat(object = sce, group.by = "sce.clusters")
◆ TROUBLESHOOTING
3. (Optional) If cell meta information is not added when creating the CellChat object (Step 2A),
use the ‘addMeta’ function to add it and the ‘setIdent’ function to assign the cell identities
to each cell.
cellchat <- addMeta(cellchat, meta = meta)
cellchat <- setIdent(cellchat, ident.use = "labels")
4. Before running CellChat to infer cell–cell communication, select the L–R interaction database
relevant to the study (for example, use the database CellChatDB.human when analyzing
human samples or the database CellChatDB.mouse when analyzing mouse samples):
CellChatDB <- CellChatDB.human
showDatabaseCategory(CellChatDB)
dplyr::glimpse(CellChatDB$interaction)
Nature Protocols | Volume 20 | January 2025 | 180–219 194
