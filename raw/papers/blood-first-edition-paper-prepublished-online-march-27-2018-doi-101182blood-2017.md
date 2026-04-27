---
source_path: /mnt/c/Users/Administrator/Zotero/storage/CWNSZTIP/dahlin2018.pdf
ingested: 2026-04-23
sha256: cec76c278fe0126d
---

From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
Blood First Edition Paper, prepublished online March 27, 2018; DOI 10.1182/blood-2017-12-821413
1
A single cell hematopoietic landscape resolves eight lineage trajectories and
2
defects in Kit mutant mice
3
Short title: Revealing a single cell hematopoietic landscape
4
Joakim S. Dahlin,1,2* Fiona K. Hamey,1* Blanca Pijuan-Sala,1 Mairi Shepherd,3
5
Winnie W.Y. Lau,1 Sonia Nestorowa,1 Caleb Weinreb,4 Samuel Wolock,4 Rebecca
6
Hannah,1 Evangelia Diamanti,1 David G. Kent,3 Berthold Göttgens,1# and Nicola K.
7
Wilson1#.
8
1: University of Cambridge, Department of Haematology, Cambridge Institute for
9
Medical Research & Wellcome Trust and MRC Cambridge Stem Cell Institute, Hills
10
Road, Cambridge CB2 0XY, UK
11
2: Department of Medicine, Karolinska Institutet and Karolinska University Hospital,
12
Stockholm, Sweden
13
3: University of Cambridge, Department of Haematology, Clifford Allbutt Building &
14
Wellcome Trust and MRC Cambridge Stem Cell Institute, Hills Road, Cambridge,
15
CB2 0AH, UK
16
4: Department of Systems Biology, Harvard Medical School, Boston MA 02115,
17
USA
18
*: These authors contributed equally to this work.
19
#: corresponding authors:
20
N.K. Wilson; Address: University of Cambridge, Department of Haematology,
21
Cambridge Institute for Medical Research & Wellcome Trust and MRC Cambridge
22
Stem Cell Institute, Hills Road, Cambridge CB2 0XY, UK; E-mail:
23
nkw22@cam.ac.uk; Tel. +44-1223-336822; FAX +44-1223-762670
24
B. Göttgens; Address: University of Cambridge, Department of Haematology,
25
Cambridge Institute for Medical Research & Wellcome Trust and MRC Cambridge
26
Stem Cell Institute, Hills Road, Cambridge CB2 0XY, UK; E-mail:
27
bg200@cam.ac.uk; Tel. +44-1223-336829; FAX +44-1223-762670
28
1
Copyright © 2018 American Society of Hematology
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
Abstract word count: 174
2
Text word count: 4007
3
No of figures: 5
4
No of tables: 0
5
No of references: 59
2
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
Key points:
2
• A single cell transcriptional landscape of 44 802 hematopoietic stem and
3
progenitor cells defines entry points to 8 different blood lineages
4
• Comparison with 13 815 c-Kit mutant cells identifies pleiotropic changes in
5
cell type abundance as well as the underlying molecular profiles
6
7
Abstract:
8
Hematopoietic stem and progenitor cells (HSPCs) maintain the adult blood system
9
and their dysregulation causes a multitude of diseases. However, the differentiation
10
journeys towards specific hematopoietic lineages remain ill defined, and system-wide
11
disease interpretation remains challenging. Here, we have profiled 44 802 mouse bone
12
marrow HSPCs using single cell RNA-Sequencing to provide a comprehensive
13
transcriptional landscape with entry points to eight different blood lineages
14
(lymphoid, megakaryocyte, erythroid, neutrophil, monocyte, eosinophil, mast cell,
15
and basophil progenitors). We identified a common basophil/mast cell bone marrow
16
progenitor, and characterized its molecular profile at the single cell level.
17
Transcriptional profiling of 13 815 HSPCs from the c-Kit mutant (W41/W41) mouse
18
model revealed the absence of a distinct mast cell lineage entry point, together with
19
global shifts in cell type abundance. Proliferative defects were accompanied by
20
reduced Myc expression. Potential compensatory processes included upregulation of
21
the integrated stress response pathway and downregulation of pro-apoptotic gene
22
expression in erythroid progenitors, thus providing a template of how large-scale
23
single cell transcriptomic studies can bridge between molecular phenotypes and
24
quantitative population changes.
25
3
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
2
Introduction:
3
The generation of mature blood lineages from hematopoietic stem cells (HSCs) has
4
long served as a paradigm for the wider field of stem cell biology.1 Through a
5
combination of advanced purification protocols and functional validation assays,
6
high-purity HSC and progenitor populations have been defined. Classically, these
7
populations have been considered as discrete steps within an ordered and hierarchical
8
branching process. Introduction of additional surface marker combinations however
9
indicated that there are likely multiple routes that can lead to functionally equivalent
10
myeloid progenitors.2 Moreover, single cell profiling in the mouse,3 single cell
11
functional assays in the human system4, and transposon tracking during unperturbed
12
hematopoiesis5 all emphasized that many single cells within traditionally defined
13
multipotent populations may already be fated towards just one lineage.
14
15
Single cell expression profiling has provided new insights into hematopoietic
16
regulatory networks,6,7 cellular states associated with cell fate decision making,8,9 the
17
cellular heterogeneity of stem and progenitor populations,3,10 and the recognition that
18
transcriptional changes associated with early lineage diversification may be of a
19
continuous nature.11 When performed at a large enough scale, single cell expression
20
snapshots can be used to reconstruct entire transcriptional landscapes of a given
21
differentiation process, with multiple computational methods now in place to recover
22
complex branching within such differentiation landscapes.12,13 However, since HSCs
23
as well as some of the progenitor populations are exceedingly rare, systematic
24
application of such approaches to the hematopoietic system will be most powerful
25
once tens of thousands of single cell transcriptomes have been processed.
4
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
2
Here we report the generation and analysis of over 40 000 single cell transcriptomes
3
covering the hematopoietic stem/progenitor (HSPC) compartment from mouse bone
4
marrow. A transcriptional landscape representation distinguishes entry points for
5
eight distinct mature lineages, with all transcriptomic data readily accessible through
6
a user-friendly web interface. We resolve the early diversification between mast cell
7
and basophil progenitors, and go on to identify and validate a common progenitor cell
8
for these two lineages within mouse bone marrow. We demonstrate that bipotent
9
basophil-mast cell progenitor activity is present in the bone marrow of c-Kit mutant
10
W41/W41 mice, despite severe mast cell deficiencies in the periphery. Single cell
11
expression profiling of over 13 000 HSPCs from W41/W41 bone marrow reveals a
12
number of quantitative shifts and underlying gene expression changes in the stem cell,
13
myeloid and erythroid compartments, as well as the absence of cells with a
14
transcriptome characteristic for the entry point into mast cell differentiation, thus
15
highlighting the broad relevance of our new reference dataset for the unbiased
16
interpretation of mutant phenotypes.
17
18
Materials and methods:
19
For detailed Materials and Methods see Supplemental Methods.
20
Cell isolation
21
The femora, tibiae, and ilia of C57BL/6 or W41/W41 mice were crushed, the bone
22
marrow cells were released and the red blood cells were lysed with ammonium
23
chloride solution (STEMCELL Technologies, Vancouver, Canada). Antibodies used
24
for isolation are listed in Supplemental Methods. Cells were sorted using an Influx
25
cell sorter (BD Biosciences, San Jose, CA). For Smart-Seq2, cells were sorted into
5
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
lysis buffer and processed as described previously.10,14 For 10x Chromium™ (10x
2
Genomics, Pleasanton, CA) experiments, cells were sorted and processed according to
3
manufacturer’s protocol. The data were deposited in NCBI’s GEO (accession
4
numbers GSE106973 and GSE107727, respectively). For in vitro culture assays of
5
hematopoietic progenitors, cells were sorted twice and cultured. The single cell
6
precision mode was used for all clonogenic assays to minimize the probability of
7
plating doublets.
8
9
In vitro culture of primary hematopoietic progenitor cells
10
Cells were cultured in IMDM (Sigma-Aldrich, St Louis, MJ) with 20 % heat-
11
inactivated fetal calf serum (FCS) (Sigma-Aldrich), 100 units/ml penicillin (Sigma-
12
Aldrich), 0.1 mg/ml streptomycin (Sigma-Aldrich), 2 mM L-glutamine (Sigma-
13 μ
Aldrich), and 0.1 M 2-Mercaptoethanol (Thermo Fisher Scientific, Waltham, MA).
14
The medium was supplemented with 20 ng/ml IL-3, 50 ng/ml IL-5, 50 ng/ml IL-9, 10
15
ng/ml GM-CSF, and 20 ng/ml SCF to analyze myeloid potential (all were
16
recombinant mouse cytokines from Peprotech, Rocky Hill, NJ).15 Erythroid potential
17
was analyzed by culturing cells in the presence of 2 U/ml human erythropoietin
18
(Janssen-Cilag, High Wycombe, UK) with 20 ng/ml mouse IL-3 and 20 ng/ml mouse
19
SCF. Both the myeloid and the erythroid conditions support basophil and mast cell
20
differentiation.
21
22
Single cells were expanded in 72-well Terasaki plates (Greiner Bio-One,
23
Kremsmünster, Austria), stained with fluorophore-conjugated antibodies in the wells,
24
diluted in buffer containing DAPI (4',6-diamidino-2-phenylindole) (BD Biosciences),
25
and analyzed with flow cytometry without washing the cells. At least five events in a
6
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
gate were required to score single colonies positive for a cell population. Typically,
2
wells containing at least 20 cells were analyzed.
3
4
In vitro culture of HSCs
5
E-SLAM HSCs (CD45+ EPCR+ CD48- CD150+) were isolated as described
6
previously.16 Single E-SLAM HSCs were sorted into round bottom 96-well plates.
7
Cells were sorted and cultured in StemSpan (STEMCELL Technologies) containing
8
FCS (Sigma-Aldrich), 300 ng/ml SCF (Bio-techne, Minneapolis, MN) and 20 ng/ml
9
IL-11 (Bio-techne). Daily cell counts were performed to assess cell divisional
10
kinetics.17
11
12
Processing of droplet-based scRNA-Seq data
13
Data were processed using the Scanpy Python module.18 After quality control, 44 802
14
WT cells and 13 815 W41/ W41 cells were retained. Data were visualized using force-
15
directed graphs, similar to previously described.19
16
17
Clustering analysis on WT and W41/ W41 LK cells
18
WT LK cells were clustered using Louvain clustering (Scanpy igraph method) with
19
15 nearest neighbors. To assign W41/W41 LK cells to clusters, these data were
20
projected into the PCA space of the WT data, and nearest neighbors calculated
21
between the two data sets based on Euclidean distance in the top 50 components.
22
W41/W41 cells were assigned to the same cluster that the majority of their 15 nearest
23
WT neighbors belonged to.
24
25
7
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
Results:
2
Single cell profiling reveals entry points to eight blood lineages in the bone marrow
3
stem/progenitor compartment
4
Recent technologies have allowed the capture and RNA sequencing of ever increasing
5
numbers of single cells.20 To obtain a comprehensive view of hematopoiesis in mouse
6
bone marrow, we sorted cells in two broad gates: Lin- c-Kit+ (LK), capturing HSPCs,
7
and Lin- Sca-1+ c-Kit+ (LSK), a subset of the LK gate enriched for HSCs and more
8
immature progenitors (Figure 1A). Sorting LSK cells separately ensured that we
9
profiled sufficient numbers of the less abundant cell types. Droplet-based single cell
10
RNA-Sequencing (scRNA-Seq) was performed, resulting in 44 802 individual
11
transcriptional profiles, with a median of over 2500 genes detected per cell (Figure
12
1B).
13
14
Recent work has demonstrated the power of force-directed graph layouts for their
15
ability to separate cells from different lineages in two-dimensional embeddings.19,21
16
The force-directed graph embedding on the 44 802 HSPC profiles showed a central
17
region of earlier stem and progenitor cells mainly from the LSK gate, with the
18
majority of more differentiated LK cells residing on several branches (Figure 1C). To
19
locate the stem cells within our data, we calculated a score for each cell representing
20
the combined expression of a set of genes previously shown to be enriched in
21
functional HSCs,22 which highlighted a region populated by mainly LSK cells (Figure
22
S1A). Plotting the expression of marker genes on the graph allowed us to define entry
23
points for differentiation towards mature cell types (Figure 1D,S1B). Expression of
24
Procr, Fgd5 and Hoxb5 marked the location of HSCs,23–25 Dntt, Flt3 and Rag2
25
indicated lymphoid progenitors,26 and Pf4, Itga2b and Gp1bb27 highlighted
8
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
megakaryocyte progenitors. The largest branch showed high expression of erythroid
2
genes such as Klf1, Epor and Gata1,28 and neutrophil and monocyte progenitors were
3
marked by expression of genes such as Elane, Gfi1 and Cebpe, or Irf8, Csf1r and
4
Ly86, respectively.9 Expression of Prg2 and Prg3 indicated a small population of
5
eosinophil progenitors (Figure 1Ei).9,29
6
7
The graph layout also showed additional branches with strong expression of genes
8
such as Ms4a2 and Cpa3 (Figure 1Eii).30 Closer inspection revealed a separation of
9
cells appearing to enter mast cell (Gzmb and Cma1 expression)31,32 and basophil
10
lineages (Prss34 and Mcpt8 expression)31,33 (Figure 1Eiii-iv). The existence of these
11
progenitor populations was confirmed by visualizing the data using diffusion maps34
12
and t-Distributed Stochastic Neighbor Embedding35 (Figure S2). We also found that
13
force-directed graphs calculated on LSK and LK cells separately showed a more
14
homogeneous structure for the LSK cells, with less prominent entry points to the
15
different blood lineages, whereas the LK embedding recapitulated the structure
16
calculated on the LSK and LK cells together (Figure S3A-B). Pairwise distances
17
between the LSK cells were smaller than distances between LK cells, supporting the
18
difference in heterogeneity (Figure S3C). To allow exploration of gene expression by
19
the wider community, we created a freely accessible website (available at
20
http://gottgens-lab.stemcells.cam.ac.uk/adultHSPC10X/ and
21
http://app.stemcells.cam.ac.uk/adultHSPC10X/).
22
23
Single cell cultures reveal a population of bipotent basophil/mast cell progenitors in
24
the bone marrow
9
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
Visualizations of the scRNA-Seq data revealed entry points to both mast cell and
2
basophil lineages with these branches positioned next to each other in the graph
3
layout. Yet the early steps of basophil and mast cell lineage diversification remain
4
poorly defined. Bipotent basophil/mast cell progenitors (BMCPs) have been described
5 β
in the spleen as Lin- c-Kit+ integrin 7hi CD16/32hi cells,36 but this study failed to
6 β
detect integrin 7hi progenitors in the bone marrow. Here, we analyzed in excess of
7
2.5 million mouse bone marrow cells, which allowed us to identify a population of
8 β
Lin- Sca-1- c-Kit+ integrin 7hi CD16/32hi bone marrow cells that fell outside the
9
classic common myeloid progenitor (CMP), granulocyte/monocyte progenitor (GMP),
10
and megakaryocyte/erythroid progenitor (MEP) gates (Figure 2A,S4A). These cells
11
had a blast-like morphology, and sometimes contained a small number of scattered
12 β
granules (Figure 2B). We next sorted Lin- Sca-1- c-Kit+ integrin 7hi CD16/32hi cells
13
in bulk and cultured them in a myeloid cytokine medium that is capable of supporting
14
the growth of eosinophils, neutrophils, mast cells, and basophils (see “Materials and
15
Methods”). The sorted cells readily formed mast cells and basophils, but no or very
16
few eosinophils and neutrophils, as assessed by flow cytometry and confirmed with
17
cytochemical staining (Figure 2B-C,S4B-C). We therefore designated this population
18
as bone marrow BMCPs. GMPs and Lin- Sca-1- c-Kit+ progenitors falling outside the
19
newly defined BMCP gate, here referred to as mixed progenitors (MPs),
20
predominantly gave rise to neutrophils (Figure 2B-C,S4B-C).
21
Monocytes/macrophages could not be identified with our flow cytometry panel, but
22
were seen to be present using cytochemical staining (Figure S4D).
23
24
We next sorted individual cells from the newly defined bone marrow BMCP gate to
25
initiate clonal cultures for subsequent analysis by flow cytometry. Single bone
10
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
marrow BMCP cells differentiated into mast cells, basophils, and mixed mast
2
cell/basophil colonies in 4:4:1 ratio (day 5) (Figure 2D-E). By contrast, single MPs
3
and single GMPs predominantly formed neutrophil colonies (Figure 2D). When
4
cultured in conditions promoting erythroid differentiation, BMCPs formed mast cells
5
and basophils, with no detectable erythroid output (Figure 2E,F). In contrast, MEPs
6
cultured in the same conditions readily formed erythroid cells but not mast cells or
7
basophils (Figure 2E-F,S5A-B). Whilst we cannot exclude the possibility that a small
8
minority of bipotent colonies may be the result of a sorted doublet, all our
9
experimental protocols and procedures were designed to ensure that wells contained
10 β
single cells (Figure S5E). Taken together therefore, Lin- Sca-1- c-Kit+ integrin 7hi
11
CD16/32hi bone marrow cells constitute a mixture of unipotent and bipotent
12
progenitors with mast cell- and basophil-forming capacity.
13
14
BMCPs exhibit a distinct transcriptional profile that shows evidence of priming
15
towards the mast cell and basophil lineages
16
To interrogate the molecular profile of the newly defined bone marrow BMCP
17
population, we performed high-coverage scRNA-Seq analysis in parallel to our single
18
cell culture assays (Figure 2,3A). GMPs were processed in parallel as an outgroup for
19
both the culturing assays as well as the molecular profiling. We visualized the
20
transcriptomic data using diffusion maps,37 a dimensionality reduction technique
21
previously applied to single cell profiles,38 which clearly separated the BMCPs and
22
the GMPs (Figure 3B). Unsupervised clustering separated the BMCP population into
23
two clusters (Figure 3C). Genes highly expressed in BMCPs included genes found in
24 α β
mature mast cells and/or basophils, such as the and subunits of the IgE receptor,
25
Ms4a2 and Fcer1a (Figure S6).31 By contrast, genes specifically expressed in the
11
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
GMPs included characteristic neutrophil markers such as Elane, Prtn3, and Mpo
2
(Figure S6).
3
4
The BMCP cells within cluster 1 displayed higher expression of genes associated with
5
mature mast cells and basophils (Cma1, Mcpt8, and Ndst2) (Figure 3D), suggesting
6
that these cells were more differentiated than the cluster 2 BMCPs. Of interest,
7
retrospective analysis of the indexed sorting data revealed that cluster 1 BMCPs had
8 ε
higher expression of several surface markers including Fc RI and a higher side
9
scatter, consistent with a more differentiated status (Figure S7). Visualization of the
10
most differentially expressed genes between the clusters (Figure 3D) and in the
11
droplet scRNA-Seq landscape (Figure 3E) demonstrated that the cluster 1 gene set
12
was most similar to the tips of the mast cell and basophil branches, whereas the
13
cluster 2 gene set highlighted less differentiated cells. The cluster 3 gene set, which
14
represents genes highly expressed in GMPs, mapped to the neutrophil branch. Taken
15
together, this analysis provides the molecular profiles of the functionally defined bone
16
marrow BMCP progenitor cells and places them into the context of the broader bone
17
marrow HSPC transcriptional landscape.
18
19
W41/W41 mice with mutant c-Kit retain bipotent BMCPs but lack a distinct mast cell
20
trajectory in bone marrow
21
The importance of c-Kit for both the maintenance of LT-HSCs and the maturation of
22
mast cells in vivo, prompted us to investigate the W41/W41 mice, which have a
23
V831M mutation in the Kit gene, causing impaired c-Kit kinase activity.39 To
24
interrogate the mast cell phenotype and additional alterations of the HSPC
25
compartment in the presence of defective Kit signaling at a global level, we therefore
12
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
performed molecular profiling on LK cells from age- and sex-matched W41/W41 mice.
2
To compare cells from different lineages we firstly clustered the WT LK
3
compartment and then proceeded to map W41/W41 LK cells to their closest
4
corresponding cluster (Figure 4A-B,S8A-B). Comparison of WT and W41/W41 mice
5
showed dramatic alterations in the structure of the transcriptional landscape. Most
6
notably, the distinct mast cell branch is absent in W41/W41 mice, in agreement with
7
the severe mast cell deficiency observed in these mice (Figure 4C).40 The LK data
8
from the W41/W41 mice are also included on our interactive website to simultaneously
9
plot expression of any chosen gene in both the WT and W41/W41 landscapes.
10
11
Although the molecular cluster of mast cell progenitors was absent from the HSPC
12 β
landscape in W41/W41 mice, the Lin- Sca-1- c-Kit+ integrin 7hi CD16/32hi BMCP
13
cells were present in the bone marrow of these mice (Figure 4D), and when sorted in
14
bulk, gave rise to mast cells and basophils in vitro (Figure 4E). Subsequent single cell
15
analysis yielded pure mast cell and basophil colonies as well as mixed basophil/mast
16
cell colonies, similar to WT mice (Figure 4F,2D), consistent with the finding that IL-3
17
is sufficient for mast cell generation in vitro41 and a previous report which showed
18
that mast cell cultures can be obtained from W41/W41 bone marrow despite the mast
19
cell deficiency of these animals.39
20
21
Global effects of impaired c-Kit signaling across the hematopoietic landscape
22
W41/W41 mice are mast cell deficient and exhibit mild macrocytic anemia.40,42,43 To
23
further investigate the effects of impaired c-Kit signaling across the entire HSPC
24
transcriptional landscape, comparison of the proportions of LK cells within each
25
cluster was performed (Figure 5A). This analysis demonstrated that cluster 5,
13
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
corresponding to the most mature erythroid progenitors, and cluster 10, containing
2
neutrophil progenitors, showed large increases in relative size, whereas other clusters,
3
including cluster 9 containing mast cell and basophil progenitors, relatively decreased
4
in size. Flow cytometry analysis of LK cells using a recently described antibody
5
panel44 which enables the isolation of progenitors at different stages of erythroid
6
commitment, confirmed the relative increase in vivo in the most mature erythroid
7
progenitors in the W41/W41 mice (Figure S9A-B).
8
9
Impaired c-Kit signaling is known to affect the long-term repopulation capacity of
10
HSCs.43,45,46 Furthermore, the CFU-GEMMs but not CFU-GMs frequencies were
11
reduced in W41/W41 mice (Figure S9Ci),47 consistent with a reduced frequency of
12
early HSPCs (Figure 5A). To study the impact of the reduced kinase activity on the
13
long-term HSCs (LT-HSCs), E-SLAM HSCs were isolated and placed in in vitro
14
culture. W41/W41 HSCs were slower to divide when compared to WT HSCs (Figure
15
5B). This reduction in proliferation was even more apparent following 10 days in
16
culture (Figure 5C). Whilst the frequency of small colonies produced from the WT
17
and W41/W41 HSCs was comparable, the frequency of very small colonies was
18
significantly increased and large colonies of 5000 cells or more were dramatically
19
reduced or absent in the W41/ W41 cultures. E-SLAMs from W41/W41 mice gave rise to
20
monocytes, neutrophils and megakaryocytes, as for WT E-SLAMs (Figure S9Cii).
21
This first analysis of division time and colony output of ESLAM W41/W41 LT-HSCs
22
therefore clearly showed reduced proliferation at the upper tiers of the hematopoietic
23
tree, implicating SCF signaling in both exit from quiescence and in cell cycle transit
24
time in both LT-HSCs and immature progenitors. To investigate whether cell cycle
25
differences could be seen in the molecular profiles captured by scRNA-Seq, we
14
From www.bloodjournal.org by guest on March 27, 2018. For personal use only.
1
scored cells by combined expression of G2/M marker genes.48 This revealed an
2
uneven distribution of the expression of G2/M markers across the transcriptional
3
landscape (Figure S9D-E). The G2M signature was particularly low in the
4
intermediate erythroid population of cluster 3 (Figure S9D-G), which was seen to be
5
much depleted in the W41/W41 mice (Figure 5A), in contrast to the erythroid clusters
6
with higher G2M scores, which were found to be enriched.
7
8
To determine specific genes showing different behavior in W41/W41 when compared
9
to WT cells at corresponding stages of hematopoiesis we performed differential
10
expression between corresponding clusters. Myc was found to be within the most
11
significantly downregulated genes for each of the W41/W41 clusters 1-11 (Figure 5D;
12
Table S1), consistent with reduced c-Kit signalling. Computation of overlaps between
13
genes upregulated in W41/W41 clusters and gene sets from the Molecular Signatures
14
Database Hallmark Gene Set Collection48 revealed ‘unfolded protein response’ to be
15
amongst the significant gene sets, suggesting a possible induction of a stress response
16
program (HALLMARK_UNFOLDED_PROTEIN_RESPONSE, FDR=5.74 x 10-5).
17
Genes in this set showing significant upregulation across multiple clusters included
18
Atf4 (Figure 5E), Psat1, Mthfd2 and Imp3 (Figure S9H).
19
20
While previous reports have shown that the W41/W41 HSPCs are defective when
21
subjected to both in vivo and in vitro assays,45–47,49 the mutant mice have relatively
22
normal steady state hematopoiesis apart from mild anemia. No differences in the
23
distribution of expression of cytokine receptors such as Epor (Figure 5F) could be
24
seen, suggesting that in more lineage restricted cells, the dependency upon c-Kit
25
signaling is diminished and the lineage specific receptors are able to compensate and
15
