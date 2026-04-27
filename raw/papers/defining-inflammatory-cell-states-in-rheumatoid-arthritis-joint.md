---
source_path: /mnt/c/Users/Administrator/Zotero/storage/84WY2FGH/Accelerating Medicines Partnership Rheumatoid Arthritis and Systemic Lupus Erythematosus (AMP RASLE) Consortium 等。 - 2019 - Defining inflammatory cell states in rheumatoid ar.pdf
ingested: 2026-04-23
sha256: a8179ab106e830c6
---

HHS Public Access
Author manuscript
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Published in final edited form as:
Nat Immunol. 2019 July ; 20(7): 928–942. doi:10.1038/s41590-019-0378-1.
Defining inflammatory cell states in rheumatoid arthritis joint
synovial tissues by integrating single-cell transcriptomics and
mass cytometry
A full list of authors and affiliations appears at the end of the article.
Abstract
To define the cell populations that drive joint inflammation in rheumatoid arthritis (RA), we
applied single-cell RNA sequencing (scRNA-seq), mass cytometry, bulk RNA-seq and flow
cytometry to T cells, B cells, monocytes and fibroblasts from 51 samples of synovial tissue from
patients with RA or osteoarthritis. Utilizing an integrated strategy based on canonical correlation
analysis of 5,265 scRNA-seq profiles, we identified 18 unique cell populations. Combining mass
cytometry and transcriptomics together revealed cell states expanded in RA synovia:
THY1(CD90)+HLA-DRAhi sublining fibroblasts, IL1B+ pro-inflammatory monocytes, ITGAX
+TBX21+ autoimmune-associated B cells and PDCD1+ T peripheral helper (Tph) and T follicular
helper (Tfh). We defined distinct subsets of CD8+ T cells characterized by a GZMK+, GZMB+ and
GNLY+ phenotype. We mapped inflammatory mediators to their source cell populations; for
example, we attributed IL6 expression to THY1+HLA-DRAhi fibroblasts, and IL1B production to
Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research,
subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms
Correspondence and requests for materials should be addressed to Soumya Raychaudhuri, 77 Avenue Louis Pasteur, Harvard New
Research Building, Suite 250D, Boston, MA 02446, USA. soumya@broadinstitute.org; 617-525-4484 (tel); 617-525-4488 (fax).
AUTHOR CONTRIBUTIONS
S.K., S.M.G., D.T., L.B.H., K.S.-E., A.M.M., D.L.B., J.H.A., V.P.B., V.M.H., A.F., C.P., H.P., G.S.F., L.M., P.K.G., W.A. and L.T.D.
recruited patients and obtained synovial tissues. B.F.B., E.D. and E.M.G. performed histological assessment of tissues. K.W., D.A.R.,
G.F.M.W., and M.B.B. designed and implemented tissue processing and cell sorting pipeline. J.A.L. obtained mass cytometry data
from samples. N.H., C.N., and T.M.E. obtained single cell RNA-seq data from samples. F.Z., K.S., C.Y.F., D.J.L. and S.R. conducted
computational and statistical analysis. A.H.J., J.R.-M., N.M.P., and C.R., designed and performed validation experiments. K.S., F.Z.,
and J.R.M. implemented the website. J.A., S.L.B., C.D.B., J.H.B., J.D., J.M.G., M.G., L.B.I., E.A.J., J.A.J., J.K., Y.C.L., M.J.M.,
M.M., F.M., J.N., A.N., D.E.O., M.P., C.R., W.H.R., A.S., D.S., J.S., J.D.T., and P.J.U. contributed to the procurement and processing
of samples, design of the AMP study. S.R., M.B.B., J.H.A., and L.T.D. supervised the research. F.Z., K.W., K.S, and S.R. generated
figures and wrote the initial draft. K.S, C.Y.F. D.A.R, L.T.D., J.H.A, M.B.B. edited the draft, and all the authors participated in writing
the final manuscript.
^Co-first authors
*Co-senior authors
Reporting Summary
Further information on research design is available in the Nature Research Reporting Summary linked to this article.
Data Availability
The single-cell RNA-seq data, bulk RNA-seq data, mass cytometry data, flow cytometry data, and the clinical and histological data
this study are available at ImmPort (https://www.immport.org/shared/study/SDY998 and https://www.immport.org/shared/study/
SDY999, study accession codes SDY998 and SDY999). The raw single-cell RNA-seq and mass cytometry data are deposited in
dbGAP (https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001457.v1.p1. The source code repository of the
computational and statistical analysis is located athttps://github.com/immunogenomics/amp_phase1_ra. Data can also be viewed on 3
different websites at https://immunogenomics.io/ampra, https://immunogenomics.io/cellbrowser/, and https://
portals.broadinstitute.org/single_cell/study/amp-phase-1.
COMPETING FINANCIAL INTERESTS
The authors declare no competing financial interests.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 2
pro-inflammatory monocytes. These populations are potentially key mediators of RA
pathogenesis.
Rheumatoid arthritis (RA) is an autoimmune disease with chronic inflammation in the
synovium of the joint tissue1–3. This inflammation leads to joint destruction, disability and
shortened life span4. Defining key cellular subsets and their activation states in the inflamed
tissue is a critical step to define new therapeutic targets for RA. CD4+ T cell5,6 B cells7,
monocytes8,9, and fibroblasts10,11 have established relevance to RA pathogenesis. Here, we
use single cell technologies to view all of these cell types simultaneously across a large
collection of samples from inflamed joints. We believe a global single-cell portrait of how
different cell types work together would advance our understanding of therapeutics.
Application of transcriptomic and cellular profiling technologies to whole synovial tissue
has already identified specific cell populations associated with RA3,12–14. However, most
studies have focused on a pre-selected cell type, surveyed whole tissues rather than
disaggregated cells, or used only a single technology platform. The latest advances in single-
cell technologies offer an opportunity to identify disease-associated cell subsets in human
tissues at high resolution in an unbiased fashion15–17. These technologies have already been
used to discover roles for T peripheral helper (Tph) cells18 and HLA-DR+CD27− cytotoxic
T cells19 in RA pathogenesis. Studies using scRNA-seq have defined myeloid cell
heterogeneity in human blood20 and identified overabundance of PDPN+CD34−THY1+
(THY1, also known as CD90) fibroblasts in RA synovial tissue15,21.
To generate high-dimensional multi-modal single-cell data from synovial tissue samples
collected across a collaborative network of research sites, we developed a robust pipeline22
in the Accelerating Medicines Partnership Rheumatoid Arthritis and Lupus (AMP RA/SLE)
consortium. We collected and disaggregated tissue samples from patients with RA and
osteoarthritis (OA), and then subjected constituent cells to scRNA-seq, sorted-population
bulk RNA-seq, mass cytometry, and flow cytometry. We developed a unique computational
strategy based on canonical correlation analysis (CCA) to integrate multi-modal
transcriptomic and proteomic profiles at a single cell level. A unified analysis of single cells
across data modalities can precisely define contributions of specific cell subsets to pathways
relevant to RA and chronic inflammation.
RESULTS
Generation of parallel mass cytometric and transcriptomic data from synovial tissue
In phase 1 of AMP RA/SLE, we recruited 36 patients with RA that met the 1987 American
College of Rheumatology (ACR) classification criteria and 15 patients with OA from 10
clinical sites over 16 months (Supplementary Table 1) and obtained synovial tissues from
ultrasound-guided biopsies or joint replacements (Methods, Fig. 1a). We required that all
tissue samples included had synovial lining documented by histology. Synovial tissue
disaggregation yielded an abundance of viable cells for downstream analyses (362,190 +/
− 7,687 (mean +/− SEM) cells per tissue). We used our validated strategy for cell sorting22
(Fig. 1a) to isolate B cells (CD45+CD3−CD19+), T cells (CD45+CD3+), monocytes
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 3
(CD45+CD14+), and stromal fibroblasts (CD45−CD31−PDPN+) (Supplementary Fig. 1a).
We applied bulk RNA-seq to all four sorted subsets for all 51 samples. For samples with
sufficient cell yield (Methods), we also measured single-cell protein expression using a 34-
marker mass cytometry panel (n=26, Supplementary Table 2), and single-cell RNA
expression in sorted cell populations (n=21, Fig. 1b).
Summary of computational data integration strategy to define cell populations
To confidently define RA-associated cell populations, we integrated multiple data modalities
(Fig. 1b, c). We use bulk RNA-seq data as the reference point because it was available for all
of the donors and most of the cell types, it had the highest dimensionality and least sensitive
to technical artifacts (Fig. 1b).
Integrating scRNA-seq with bulk RNA-seq data ensures robust discovery of cell populations.
Here, we used CCA to find linear combinations of bulk RNA-seq samples and scRNA-seq
cells (Fig. 1c, d) to create gene expression profiles that were maximally correlated. These
linear combinations captured sources of shared variation between the two datasets and
allowed us to identify individual cell populations that drive variation in the bulk RNA-seq
data. We analyzed the scRNA-seq data by using the canonical variate coefficients for each
cell to compute a nearest neighbor network, identifying clusters with a community detection
algorithm, and evaluating the separation between clusters with Silhouette analysis (Methods,
Supplementary Fig. 2b).
We identified cell clusters in mass cytometry data with density-based clustering23. Next, we
used CCA to identify linear combinations of bulk RNA-seq genes and mass cytometry
cluster abundances that maximize correlation across patients. These canonical variates offer
a way to visualize genes and mass cytometry clusters together. We then queried this CCA
result with the best marker genes from scRNA-seq to establish a relationship between each
scRNA-seq cluster and each mass cytometry cluster (Methods). We also used CCA to
associate bulk gene expression in each sample with proportions of cells in different flow
cytometry gates.
Flow cytometry features define a set of RA synovia that are leukocyte-rich
Histology of RA synovial tissues revealed heterogeneous tissue composition with variable
lymphocyte and monocyte infiltration (Fig. 2a,b, Supplementary Fig. 2c,d). This
heterogeneity was expected, because variation in tissue immune cell infiltration reflects local
disease activity in the source joint. Consequently, we employed a data-driven approach to
separate samples based on flow cytometry of lymphocyte and monocyte infiltration in each
tissue sample (Supplementary Fig. 1b,c). We calculated a multivariate normal distribution of
these parameters based on OA samples as a reference, and for each RA sample we
calculated the Mahalanobis distance from OA24. We defined the maximum OA distance
(4.5) as the threshold for defining leukocyte-rich RA (>4.5, n=19) or leukocyte-poor RA
(<4.5, n=17) samples (Methods, Supplementary Fig. 1d). Whereas leukocyte-rich RA tissues
had significant infiltration of synovial T cells and B cells, leukocyte-poor RA tissues had
cellular compositions more similar to OA (Fig. 2c). Synovial monocyte abundances were
similar between RA and OA (Fig. 2c).
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 4
To test if our classification indicates inflammation, we assessed tissue histology and
assigned each sample a Krenn inflammation score25. Samples we classified as leukocyte-
rich RA had a significantly higher Krenn inflammation score than leukocyte-poor RA or OA
(Fig. 2d). In contrast, synovial lining membrane hyperplasia was not significantly different
between leukocyte-rich RA, leukocyte-poor RA, and OA samples (Fig. 2d). We observed
significant correlation between synovial leukocyte infiltration measured by flow cytometry
and the histological Krenn inflammation score (Fig. 2e). Mass cytometry in 26 synovial
tissues was consistent with flow cytometry and histology. OA and leukocyte-poor RA
samples were characterized by high abundance of fibroblasts and endothelial cells; while
leukocyte-rich RA tissues were characterized by high abundance of CD4 T, CD8 T, and B
cells (Fig. 2f, Supplementary Fig. 3a).
Single-cell RNA-seq analysis reveals distinct cell subpopulations
Next, we analyzed 5,265 scRNA-seq profiles passing quality control (Methods), including
1,142 B cells, 1,844 fibroblasts, 750 monocytes, and 1,529 T cells. We used canonical
variates (from CCA with bulk RNA-seq) to define 18 cell clusters that were independent of
donor (n=21) and technical plate (n=24) effects (Fig. 3a–bb, Supplementary Fig. 2c,
Supplementary 4a). In contrast, conventional PCA-based clustering led to clusters that were
confounded by batch effects (Supplementary Fig. 4b). All of the clusters in the PCA-based
clustering, excluding clusters confounded by batch, were identified in CCA-based
clustering. Next, we compared expression values between cells in the cluster and all other
cells to select cluster marker genes (Methods, Supplementary Table 4). For selected genes,
we show expression values in each cell positioned in a t-distributed Stochastic Neighbor
Embedding (tSNE26) (Fig. 3c–f). Among fibroblasts, we identified four putative
subpopulations (Fig. 3c): CD34+ sublining fibroblasts (SC-F1), HLA-DRAhi sublining
fibroblasts (SC-F2), DKK3+ sublining fibroblasts (SC-F3), and CD55+ lining fibroblasts
(SC-F4). In monocytes (Fig. 3d), we identified IL1B+ pro-inflammatory monocytes (SC-
M1), NUPR1+ monocytes (SC-M2), C1QA+ monocytes (SC-M3), and interferon (IFN)
activated monocytes (SC-M4). In T cells (Fig. 3e), we identified three CD4+ clusters:
CCR7+ T cells (SC-T1), FOXP3+ regulatory T cells (T cells) (SC-T2), and PDCD1+ Tph
reg
and T follicular helper (Tfh) (SC-T3); and three CD8+ clusters: GZMK+ T cells (SC-T4),
GNLY+GZMB+ cytotoxic lymphocytes (CTLs) (SC-T5), and GZMK+GZMB+ T cells (SC-
T6). Within B cells (Fig. 3f), we identified four cell clusters, including naive IGHD+CD27−
(SC-B1) and IGHG3+CD27+ memory B cells (SC-B2). We identified an autoimmune-
associated B cells (ABCs) cluster (SC-B3) with high expression of ITGAX (also known as
CD11c) and a plasmablast cluster (SC-B4) with high expression of immunoglobulin genes
and XBP1, a transcription factor for plasma cell differentiation27.
We assessed protein fluorescence measurements of typical cell type markers, which were
consistent with our identified scRNA-seq clusters (Supplementary Fig. 2e). Cell density
quantified from 10 histology samples was correlated with the lymphocyte flow cytometric
cell yields, suggesting that samples with the most single cell measurements are those with
the best yields and the most inflammation (Supplementary Fig. 5).
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 5
Distinct synovial fibroblasts defined by cytokine activation and MHC II expression
To identify the fibroblast subpopulations overabundant in leukocyte-rich RA synovia, we
selected marker genes for each cluster and assessed their expression levels in bulk RNA-seq
from sorted fibroblasts (CD45−PDPN+) from RA and OA patients. For example, genes
associated with HLA-DRAhi (SC-F2) fibroblasts were more highly expressed in bulk RNA-
seq samples from leukocyte-rich RA than OA (t-test p<1×10−3 for HLA-DRA, IFI30, and
IL6) (Fig. 4a). Since the expression profile of a bulk tissue sample is an aggregate of the
expression profiles of its constituent cell populations, this result suggests expansion of HLA-
DRAhi (SC-F2) fibroblasts in RA tissues. Genes associated with CD55+ fibroblasts (SC-F4)
were significantly more highly expressed in bulk RNA-seq samples from OA than
leukocyte-rich RA (t-test p<1×10−3 for HBEGF, CLIC5, HTRA4, and DNASE1L3) (Fig.
4a). CD55+ fibroblasts (SC-F4) were the most transcriptionally distinct subset from the three
THY1+ clusters (SC-F1–3), including the highest expression of lubricin (PRG4), suggesting
that these cells represent synovial lining fibroblasts and THY1+ fibroblasts (SC-F1–3)
represent sublining (Fig. 4a). Next, we use the averaged expression level of the best marker
genes for each scRNA-seq cluster (AUC>0.7) and tested for differential expression in bulk
RNA-seq fibroblast samples from leukocyte-rich RA and OA synovia. The gene averages for
HLA-DRAhi sublining fibroblasts (SC-F2) and CD34+ sublining fibroblasts (SC-F1) were
higher in leukocyte-rich RA compared to OA (t-test p=2×10−6 and p=2×10−3, respectively),
while the gene averages for CD55+ lining fibroblasts (SC-F4) were higher in OA than
leukocyte-rich RA (t-test p=5×10−7) (Fig. 4b).
Consistent with the role of synovial fibroblasts in matrix remodeling, the sublining fibroblast
subsets (SC-F1–3) expressed genes encoding extracellular matrix constituents (Fig. 4c).
HLA-DRAhi sublining fibroblasts (SC-F2) expressed genes related to MHC class II
presentation and the interferon gamma-mediated signaling pathway (IFI30) (Fig. 4a,c),
suggesting upregulation of MHC class II in response to interferon-gamma signaling in these
cells. We identified a novel sublining fibroblast subtype (SC-F3) that is characterized by
high expression of DKK3, CADM1 and COL8A2 (Fig. 4a).
To independently confirm the presence of four fibroblast subpopulations discovered by
scRNA-seq, we analyzed CD45−PDPN+ cells in mass cytometry data, and found eight
putative cell clusters with differential protein levels of THY1, HLA-DR, CD34, and
Cadherin-11 without obvious batch effects (Fig. 4d–g, Supplementary Fig. 3b). CCA
revealed that greater abundance of THY1+CD34−HLA-DRhi fibroblasts measured by mass
cytometry is associated with higher expression of IL6, CXCL12, and HLA-DRA in bulk
RNA-seq of the same samples, suggesting these cells are in an active cytokine-producing
state (Fig. 4h). CCA allowed us to place mass cytometry clusters in the same space as bulk
RNA-seq genes, so we could query the positions of scRNA-seq genes within this space to
find the correspondence between scRNA-seq clusters and mass cytometry clusters (Fig. 4i,
Methods). We found HLA-DRAhi sublining fibroblasts (SC-F2) correspond to
THY1+CD34−HLA-DRhi fibroblasts (z-score=2.8), and CD34+ sublining fibroblasts (SC-
F1) correspond to THY1+CD34+HLA-DRlo fibroblasts (z-score=2.7) (Table 1). Consistent
with differential expression analysis of bulk RNA-seq, we found that THY1+CD34−HLA-
DRhi cells in the mass cytometry data were overabundant in leukocyte-rich RA relative to
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 6
leukocyte-poor RA and OA controls (36% versus 2% of fibroblasts, MASC OR = 33.8 (95%
CI: 11.7–113.1), one-sided MASC p=1.9×10−5) (Table 1).
To validate that the protein surface markers from mass cytometry were capturing the same
transcriptional populations from scRNA-seq, we isolated fibroblasts from 10 synovial tissue
samples based on surface protein levels of THY1 and HLA-DR and applied bulk RNA-seq
(Supplementary Fig. 6a). We trained a linear discriminant analysis (LDA) classifier on
fibroblast scRNA-seq data and used it to determine the most similar scRNA-seq cluster for
each bulk RNA-seq sample. The sorted THY1+HLA-DR+ fibroblast population was similar
to THY1+HLA-DRAhi (SC-F2) and the THY1− HLA-DR− population was similar to
THY1− (SC-F4) (Supplementary Fig. 7a–d). Genes upregulated in the sorted THY1+HLA-
DR+ fibroblasts included the interleukin IL6 and the chemokine CXCL12, consistent with
the scRNA-seq data.
Activation states define heterogeneity among synovial monocytes
We identified four transcriptionally distinct monocyte subsets in the scRNA-seq data: IL1B+
pro-inflammatory monocytes (SC-M1), NUPR1+ monocytes (SC-M2), C1QA+ monocytes
(SC-M3) and IFN-activated SPP1+ monocytes (SC-M4) (Fig. 5a). In bulk RNA-seq
monocyte samples from leukocyte-rich RA and OA donors, we found that genes associated
with IL1B+ monocytes (SC-M1), including NR4A2, HBEGF, PLAUR and the IFN-activated
gene IFITM3 were significantly upregulated in leukocyte-rich RA samples (t-test
p<1×10−4). In contrast, marker genes associated with NUPR1+ monocytes (SC-M2) were
downregulated in leukocyte-rich RA relative to OA (Fig. 5a). Next, we took the average of
the top marker genes (AUC>0.7) for each monocyte scRNA-seq subset and tested for
differential expression of these averages in the bulk RA versus OA RNA-seq data. This
analysis suggests that leukocyte-rich RA synovia have a greater abundance of IL1B+
monocytes (t-test p=6×10−5) and IFN-activated monocytes (t-test p=6×10−3), but lower
abundance of NUPR1+ monocytes (t-test p=2×10−5) (Fig. 5b). These data suggest that
cytokine activation drives expansion of unique monocyte populations in active RA synovia.
With GSEA, we tested MSigDB immunologic gene sets and found IL1B+ monocytes (SC-
M1) have relatively high expression levels of genes defining the LPS response in monocytes
and macrophages (Fig. 5b). This suggests IL1B+ monocytes (SC-M1) are similar to TLR-
activated IL-1-producing pro-inflammatory monocytes. Among Gene Ontology gene sets,
we found SPP1+ monocytes (SC-M4) express genes induced by type I and II IFN
(Supplementary Fig. 8a), including IFITM3 and IFI6 (Fig. 5a). The transcriptional profiles
of monocytes in SC-M2 and SC-M3 do not align with known activation states, possibly
indicating that these clusters represent cell phenotypes tailored to the unique homeostatic
needs of the synovium. Immunofluorescence staining confirmed the presence of CD14 and
IL-1β positive cells in 6 tissue samples, consistent with an enrichment of the IL1B+ pro-
inflammatory monocytes (SC-M1) phenotype in RA synovium (Fig. 5d, Supplementary Fig.
9a,b).
In the mass cytometry data, we identified five CD14+ monocyte clusters (Fig. 5e–h,
Supplementary Fig. 3c). Using CCA to integrate mass cytometry and bulk RNA-seq data, we
found that samples with a greater abundance of CD11c+CCR2+ and CD11c+CD38+ using
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 7
mass cytometry also had a higher expression of IFITM3, PLAUR, CD38, and HLA genes
(Fig. 5i). This was consistent with a correspondence between the CD11c+CD38+ mass
cytometry cluster and the activated monocyte scRNA-seq cluster IL1B+ (SC-M1) and SPP1+
(SC-M4) (z-score=2.3 and 2.3, respectively) (Fig. 5j, Table 1). Supporting this finding, we
confirmed that CD11c+CD38+ monocytes are significantly expanded in leukocyte-rich RA
(OR = 7.8 (95% CI: 3.6–17.2), one-sided MASC p=6.7×10−5) (Table 1). Conversely,
NUPR1+ monocytes (SC-M2) correspond to CD11c− monocytes in mass cytometry and are
inversely correlated with inflammatory monocyte populations (z-score=2.7) (Fig. 5j, Table
1).
To confirm that putative populations from mass cytometry correspond to those identified by
scRNA-seq clusters, we sorted CD14+ monocytes from 4 synovial tissue samples using
CD11c and CD38 protein markers and assayed them with RNA-seq (Supplementary Fig.
6c). Importantly, we found that CD14+ synovial cells had high expression of both CD11c
and CD38 particularly in the RA samples. The CD14+CD11c+++CD38+++ and
CD14+CD11c+CD38− sorted cells were consistent with IL1B+ pro-inflammatory (SC-M1)
and NUPR1+ (SC-M2) cells, respectively (Supplementary Fig. 7e–h). These data, alongside
the mass cytometry data, support the findings of greater abundance of IL1B+ pro-
inflammatory (SC-M1) monocytes and lower abundance of NUPR1+ (SC-M2) monocytes in
leukocyte-rich RA samples.
Heterogeneity in synovial CD4 and CD8 T cells defined by effector functions
We found three CD4+ and three CD8+ T cell subsets in the scRNA-seq data (Fig. 6a).
CCR7+ T cells (SC-T1) expressed genes in the MSigDB immunologic gene set for central
memory T cells (Fig. 6a, c). The two other CD4+ populations, FOXP3+ T cells and
reg
PDCD1+ Tph and Tfh cells, were marked by high expression of FOXP3 (SC-T2) and
CXCL13 (SC-T3) by examining differentially expressed genes between these two clusters18
(Supplementary Fig. 8c). CXCL13, a chemokine expressed by Tph cells, was upregulated in
bulk-sorted T cells (CD45+CD14−CD3+) from leukocyte-rich RA compared to OA (t-test
p=1.2×10−4) (Fig. 6a). We found that the average of marker genes for Tph and Tfh cells
(SC-T3) (AUC>0.7) was higher in leukocyte-rich RA than OA samples (t-test p=0.01) (Fig.
6b), suggesting greater abundance of Tph and activated T cells in RA than OA. We
identified three CD8 T cell subsets characterized by distinct expression patterns of effector
molecules GZMK, GZMB, GZMA and GNLY (Fig. 6a). We defined these populations as
GZMK+ (SC-T4), GNLY+GZMB+ cytotoxic T lymphocytes (CTLs) (SC-T5), and GZMK
+GZMB+ T cells (SC-T6). GZMK+GZMB+ T cells (SC-T6) also expressed HLA-DPA1 and
HLA-DRB1, and other genes suggestive of an effector phenotype (Fig. 6a,c).
To confirm these findings, we applied intracellular staining to tissues from RA samples and
RNA-seq to sorted CD8 T cells. Intracellular staining of GZMK and GZMB proteins in
disaggregated tissue samples from patients with RA revealed that the majority of CD8 T
cells in synovial tissue express GZMK (Supplementary Fig. 10a). Furthermore, we found
that most HLA-DR+ CD8 T cells express both GZMB and GZMK by intracellular protein
staining (Supplementary Fig. 10b). In a comparison of 7 synovial tissue samples, CD8 T
cells had higher proportion of IFNγ+ cells than CD4 T cells from the same sample
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 8
(Supplementary Fig. 10c,d). We also applied immunofluorescence to 6 synovial tissue
samples and found that IFNγ+CD3+CD8+ T cells were more frequent in RA than OA (Fig.
6d, Supplementary Fig. 9c,d). Overall, these results closely mirror the findings from the
scRNA-seq clusters.
Using mass cytometry, we identified nine putative T cell clusters among the synovial T cells
(CD45+CD14−CD3+) (Fig. 6e–h, Supplementary Fig. 3d). By integrating bulk RNA-seq
with mass cytometry cluster abundances, we found that higher gene expression of CXCL13
and inhibitory receptors TIGIT and CTLA4 was associated with greater abundance of the
CD4+PD-1+ICOS+ mass cytometry cluster. Greater abundance of CD8+ PD-1−HLA-DR+
cells was associated with greater expression of IFNG (Fig. 6i). We found correspondence
between Tph and Tfh cells (SC-T3) and CD4+PD-1+ICOS+ T cells (z-score = 3.4). CD8+
subsets including GZMK+GZMB+ (SC-T6), CTLs (SC-T5), and GZMK+ (SC-T4) tracked
with CD8+PD-1−HLA-DR+ T cells by mass cytometry (Fig. 6j, Table 1). In addition,
CD4+PD-1+ICOS+ cells were significantly overabundant in leukocyte-rich RA (MASC OR
= 3 (95% CI: 1.7–5.2), one-sided MASC p=2.7×10−4) (Table 1).
Autoimmune-associated B cells expanded in RA synovium by single-cell RNA-seq
We identified four synovial B cell clusters with scRNA-seq: naive B cells (SC-B1), memory
B cells (SC-B2), ITGAX+ ABC cells (SC-B3), and plasmablasts (SC-B4) (Fig. 7a). GSEA
with Gene Ontology pathways suggested that SC-B1, SC-B2, and SC-B3 clusters represent
activated B cells (Supplementary Fig. 8b). GSEA with MSigDB immunological gene sets
revealed that SC-B1 cells express naive B cell genes, while SC-B2 and SC-B3 cells express
IgM and IgG memory B cell genes (Fig. 7b). SC-B3 cells express high levels of ITGAX and
TBX21 (T-bet), which are markers of autoimmunity-associated B cells (Fig. 3f and Fig.
7a)28,29, as well as markers of recently activated B cells including ACTB30. High expression
of AICDA is consistent with the recently reported transcriptomic analysis of CD11c+ B cells
from SLE peripheral blood31. Interferon stimulated genes (GBP1 and ISG15) are also
expressed in ABCs (SC-B3) and upregulated in leukocyte-rich RA (Fig. 7a). While ABCs
(SC-B3) constitute a relatively small proportion of all B cells, they are almost exclusively
derived from two patients with leukocyte-rich RA (Fig. 3b). To confirm the presence of
ABCs in human tissues, we applied immunofluorescence staining to 6 synovial tissue
samples. RA synovium had increased numbers of CD20+T-bet+ CD11c+ B cells compared to
OA synovium. Specifically, we observed ABC cells in tissue sections from the same
inflamed tissue samples that had a high proportion of ABCs by scRNA-seq analysis (Fig. 7c,
Supplementary Fig. 9e, f).
We identified 10 putative B cell clusters in the mass cytometry data
(CD45+CD3−CD14−CD19+) (Fig. 7d–g, Supplementary Fig. 3e). CCA analysis showed that
samples with higher gene expression of CD38, MZB1, and plasma cell differentiation factor
XBP1 had greater abundance of CD38++CD20−IgM−IgD− plasmablasts (Fig. 7h).
Plasmablasts (SC-B4) corresponded with CD38++CD20−IgM−IgD− B cells (z-score=2.7)
(Fig. 7i, Table 1). ABCs (SC-B3) corresponded with the IgM− IgD− HLA-DR++ CD20+
CD11c+ mass cytometry cluster (z-score=1.6), which is significantly overabundant in
leukocyte-rich RA (OR = 5.7 (95% CI: 1.8–22.3), one-sided MASC p=2.7×10−3) (Fig. 7i,
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 9
Table 1). Mass cytometry analysis further identified three putative subsets within CD11c+
cells: IgM−IgD−HLA-DR++CD20+CD11c+, CD38+HLA-DR++CD20−CD11c+, and IgM
+IgD+CD11c+, which is suggestive of additional heterogeneity within ABCs.
To demonstrate that CD19+CD11c+ cells by surface protein markers correspond to SC-B3
(ABCs), we flow-sorted CD19+CD11c+ cells from an independent cohort of 6 RA synovial
samples and applied RNA-seq (Supplementary Fig. 6b). We show that these RNA-seq
profiles are most consistent with ABC cells (Supplementary Fig. 7i–k). In these sorted
samples, we found more putative marker genes (e.g. ZEB2 and CIITA) and interferon-
induced genes (IFITM3 and IFI27) for the ABC population (Supplementary Fig. 7l).
Inflammatory pathways and effector modules revealed by global single cell profiling
We used bulk and single cell transcriptomes of sorted synovial cells to examine pathologic
molecular signal pathways. First, principal component analysis (PCA) on post-QC OA and
RA bulk RNA-seq samples (Supplementary Fig. 11a,b) showed that cell type accounted for
most of the data variance. Each cell type expressed specific marker genes, PDGFRA for
fibroblasts, C1QA for monocytes, CD3D for T cells, and CD19 for B cells (Supplementary
Fig. 11c). Within each cell type, PCA showed that leukocyte-rich RA samples separated
from OA and leukocyte-poor RA samples (Supplementary Fig. 11d–g). Differential gene
expression analysis between leukocyte-rich RA and OA (FC>2 and FDR<0.01) revealed
genes upregulated in leukocyte-rich RA tissues: 173 in fibroblasts, 159 in monocytes, 10 in
T cells, and 5 in B cells. To define the pathways relevant to leukocyte-rich RA, we used
GSEA weighted by gene effect sizes on Gene Ontology pathways and identified type I
interferon response and inflammatory response (monocytes and fibroblasts) (Supplementary
Fig. 11h–i), Fc receptor signaling (monocytes), NF-kappa B signaling (fibroblasts), and
interferon gamma (T cells) (Fig. 8a). Leukocyte-rich RA samples had significantly higher
expression of some genes in fibroblasts and monocytes: inflammatory response genes
(PTGS2, PTGER3, and ICAM1), interferon response genes (IFIT2, RSAD2, STAT1, and
XAF1), and chemokine or cytokine genes (CCL2 and CXCL9) (Fig. 8b), consistent with a
coordinated chemotactic response to interferon activation. T cells had upregulation of
interferon regulatory factors (IRFs), including IRF7 and IRF9, and monocytes had
upregulation of IRF7, IRF8 and IRF9. Taken together, pathway analysis suggests crosstalk
between immune and stromal cells in leukocyte-rich RA synovia. Inflammatory response
genes upregulated in leukocyte-rich RA had comparable expression levels between
leukocyte-poor RA and OA synovial cells (Fig. 8b)
Next, we asked whether inflammatory cytokines upregulated in leukocyte-rich RA are
driven by global upregulation within a single synovial cell type, or specific upregulation
within a discrete cell subset defined by scRNA-seq. Whereas TNF was produced at a high
level by multiple monocyte, B cell and T cell populations; IL6 expression was restricted to
HLA-DRAhi sublining fibroblasts (SC-F2) and a subset of B cells (SC-B1) (Fig. 8c); CD8 T
cells, rather than CD4 T cells, were the dominant source of IFNG transcription in leukocyte-
rich synovia.
We also observed cell subset-specific responses to inflammatory pathways. Toll-like receptor
signaling pathway was enriched in B cells and monocytes in leukocyte-rich RA tissues (Fig.
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 10
8a). At the single cell level, we observed that TLR10 was only expressed by activated B
cells, indicating that TLR10 has a functional role within the B cell lineage. In contrast,
TLR8 was elevated in all RA monocyte subsets. The hematopoietic cell-specific
transcription factor IRF8 was expressed in a significant fraction of monocytes and B cells
that cooperatively regulate differentiation of monocytes and activated B cells in RA
synovium. SLAMF7 is highly expressed by pro-inflammatory monocytes (SC-M1), IFN-
activated monocytes (SC-M4), CD8 T cells, and plasmablasts (SC-B4).
Furthermore, mass cytometry analysis across all identified cell clusters revealed that
leukocyte-rich RA patients show high cell abundances of HLA-DRhi fibroblast populations,
Tph cells, CD11c+CD14+ monocytes, and CD11c+ B cell populations (Supplementary Fig.
3f).
DISCUSSION
Using multi-model, high-dimensional synovial tissue data we defined stromal and immune
cell populations overabundant in RA and described their transcriptional contributions to
essential inflammatory pathways. Recognizing the considerable variation in disease duration
and activity, treatment types, and joint histology scores32, we elected to use a molecular
parameter, based on percent leukocytes of the total cellularity, to classify our samples at the
local tissue level. We note that differences in leukocyte enrichment of joint replacement
samples and biopsy samples were best explained by leukocyte infiltration and not by the
histological scores (Supplementary Fig. 1, Supplementary Fig. 11d–g).
This study and a previous study33 have highlighted sublining fibroblasts as a potential
therapeutic target in RA. Sublining fibroblasts are a major source of pro-inflammatory
cytokines such as IL6 (Fig. 4), and a specific subset of sublining fibroblasts expressing
MHC II (SC-F2, THY1+CD34-HLA-DRhi) was >15 fold expanded in RA tissues. Further
studies are needed to define molecular mechanisms that regulate sublining fibroblast
expansion in RA. T cells, B cells, and monocyte proportions track with expression of
individual fibroblast genes (Supplementary Fig. 11j). We found DNASE1L3, a gene whose
loss of function is associated with RA34 and systemic lupus erythematosus35 to be highly
expressed in CD55+ lining fibroblasts (SC-F4) (Fig. 4a). We identified a novel fibroblast
subset (SC-F3) with high expression of DKK3+ (Fig. 4), encoding Dickkopf3, a protein
upregulated in OA that prevents cartilage degradation in vitro36.
Transcriptional heterogeneity in the synovial monocytes indicated that distinct RA-enriched
subsets are driven by inflammatory cytokines and interferons (Fig. 5). This suggests
monocytes may be differentially polarized by unique cytokine combinations in local
microenvironments. These newly identified inflammatory phenotypes align with RA
therapeutic targets, including anti-TNF therapies and interferon pathway JAK kinase
inhibitors37. The NUPR1+ (SC-M2) monocytes were inversely correlated with tissue
inflammation, and expressed high levels of monocyte tissue remodeling factors such as
MERTK (Fig. 5)38. Alternatively, NUPR1+ markers such as osteoactivin (GPNMB) and
cathepsin K (CTSK) may indicate a subset of osteoclast progenitors that control bone
remodeling (Fig. 5)37,39. Furthermore, spatial studies—particularly focused on lining versus
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 11
sublining, perivascular and lymphocyte aggregate-associated monocytes—will help
understand the functional roles of these subsets.
Single cell classification of T cell subsets in RA synovium demonstrated CD4+ T cell
heterogeneity that is consistent with distinction between the homing capacity and effector
functions of these subsets. Consistent with previous studies, we observed expansion of
PDCD1+CD4+ Tph cells (SC-T3) within leukocyte-rich RA. We also found CD8 T cell
subsets (SC-T4–6) characterized by a distinct granzyme expression pattern (Fig. 6a). A
larger study may be better powered to differentiate the relative expansion of individual
subpopulations.
A critical unmet need in RA is identifying therapeutic targets for patients failing to respond
to disease-modifying antirheumatic drugs (DMARDs)41. We observed upregulation of
chemokines (CXCL8, CXCL9, and CXCL13), cytokines (IFNG and IL1542,43), and surface
receptors (PDGFRB and SLAMF7) in distinct immune and stromal cell populations,
suggesting potential novel targets. This study was enabled by advances in the statistical
integration of single-cell data and our recent work optimizing robust methodologies for
disaggregation of synovial tissue22.
We developed advanced strategies to integrate multiple molecular datasets by modulating
technical artifact from single cell technologies44, while emphasizing biological signals. CCA
has been successfully employed in other contexts to integrate high-dimensional biological
data45,46. Our CCA-based strategy analyzed scRNA-seq data using canonical variates that
capture variance that are present in both single-cell and bulk RNA-seq data. The shared
variances likely represent biological trends, and not technical factors that would likely be
uncorrelated in these two independent datasets. We further confirmed that the identified
scRNA-seq clusters are well correlated with the bulk RNA-seq data and also the mass
cytometry data (Supplementary Fig. 12, 13).
The two single cell modalities used in this study, mass cytometry and scRNA-seq,
complement each other. Single-cell RNA-seq captures expression of thousands of genes, but
at the cost of sparse data47. Mass cytometry captures hundreds of thousands of individual
cells, but measures a limited number (~40)48 of pre-selected markers. However, since
markers are backed with decades of experimental experience they can be effective at
defining cellular heterogeneity49. To make the analysis consistent, we gated mass cytometry
cells on the same markers upon which the scRNA-seq was gated. Combining mass
cytometry with the extended dimensionality of scRNA-seq enables quantification of well-
established cell populations and discovery of novel cell states, such as the CD8 T cell states
noted here. As an ongoing AMP phase 2 study, we are examining larger numbers of ungated
cell populations from ~100 synovial tissue patients with RA by capturing mRNA and protein
expression simultaneously50 with detailed clinical data and ultrasound score evaluation of
synovitis. We anticipate that this larger study will enable us to not only discover additional
subpopulations, but to better define their link to clinical sub-phenotypes.
It is essential to interrogate the tissue infiltration of diseases other than RA, including SLE,
type I diabetes, psoriasis, multiple sclerosis and other organ targeting conditions.
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 12
Application of multiple single-cell technologies together can help define key novel
populations, thereby providing new insights about etiology and potential therapies.
Methods
Study design and patient recruitment
The study was performed in accordance with protocols approved by the institutional review
board. A multicenter, cross-sectional study of individuals undergoing elective surgical
procedures and a prospective observational study of synovial biopsy specimens from
patients with RA ≥ age 18, with at least one inflamed joint, recruited from 10 contributing
sites in the network. Synovial tissues were obtained from joint replacement procedures or
ultrasound-guided biopsies, followed by cryopreservation in cryopreservation media
Cryostor CS10 (Sigma-Aldrich) and transit to a central technology site.
Histological assessment of synovial tissue and quality control
Synovial tissue quality and grading of synovitis were evaluated in formalin-fixed, paraffin-
embedded sections by histologic analysis (H and E staining). Specimens were identified as
synovium by the presence of a lining layer or by characteristic histologic features of
synovium, including the presence of loose fibrovascular or fatty tissue lacking a lining layer.
Samples consisting of dense fibrous tissue, joint capsule or other tissues were determined
not to be synovium. For each histological and molecular analysis, we generated pooled data
from 6–8 separate fragments from different sites in the same joint. Thus, this should be
representative of the whole tissue and mitigate much of the biopsy site-to-site variability.
Krenn lining scores (0–3) and inflammation scores (0–3) for each tissue sample were
determined independently by three pathologists25.
Tissue disaggregation for mass cytometry and RNA-sequencing
For pipeline analysis, synovial tissue samples stored in cryovials were disaggregated into
single cell suspension as describe. Briefly, synovial tissue fragments were separated
mechanically and enzymatically in digestion buffer (Liberase TL (Sigma-Aldrich) 100
ug/mL and DNase I (New England Biolabs) 100 ug/ml in RPMI) in a 37°C water bath for 30
minutes. Single cell suspensions from disaggregated synovial tissues were assessed for cell
quantity and cell viability by trypan Blue. For samples with more than 200,000 viable
synovial cells, 50% of all synovial cells were allocated for analysis by mass cytometry and
the remaining cells were allocated for RNA-seq. For samples with less than 200,000 viable
synovial cells, all synovial cells were utilized for RNA-seq analysis.
Synovial cell sorting strategy for RNA sequencing
Synovial T cells, B cells, monocytes, and fibroblasts were isolated from disaggregated
synovial tissue, as described22. Briefly, disaggregated synovial cells were stained with
antibodies against CD45 (HI30), CD90 (5E10), podoplanin (NZ1.3), CD3 (UCHT1), CD19
(HIB19), CD14 (M5E2), CD34 (4H11), CD4 (RPA-T4), CD8 (SK1), CD31 (WM59), CD27
(M-T271), CD235a (KC16), using human TruStain FcX in 1% BSA in Hepes-Buffered
Saline (HBS,20 mM HEPES, 137 mM NaCl, 3mM Kcl, 1mM CaCl2) for 30 minutes. 1000
viable (PI-) T cells (CD45+, CD3+, CD14−), monocytes (CD45+, CD3−, CD14+), B cells
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 13
(CD45+, CD3−, CD14−, CD19+), and synovial fibroblasts (CD45−, CD31−, PDPN+) were
collected by fluorescence-activated cell sorting (BD FACSAria Fusion) directly in buffer
RLT (Qiagen) for bulk RNA-seq. For single cell RNA-seq, live cells of each population were
re-sorted into 384-well plates single cells with a maximum of 144 cells for each cell type,
per patient sample.
Flow sorting strategy for bulk RNA-seq experimental validation
For bulk RNA-seq validation experiments, RA and OA synovial tissue were disaggregated
and synovial cells were stained with cell-type specific antibody panels. For each cell subset,
up to 1000 cells were collected directly into buffer TCL (Qiagen). Antibody panels used to
define cell subsets are fibroblasts: CD90 (5E10), podoplanin (NZ1.3), HLA-DR (G46–6); B
cell subsets: HLA-DR (G46–6), CD11c (3.9), CD19 (SJ25C1), CD27 (M-T271), IgD (IA6–
2), CD3 (UCHT1), CD14 (M5E2), CD38 (HIT2); Monocyte subsets: CD14-BV421 (M5E2),
CD38-APC (HB-7), and CD11c-PECy7 (B-ly6). Immediately prior to sorting, DAPI or
LIVE/DEAD viability dye was added to cell suspensions and cells were passed through a
100μm filter. Synovial cell subsets were sorted based on flow cytometry gating schema
shown in Supplementary Fig. 6. In all, we sorted THY1− DR− populations from 4 OA
samples, THY1+DR− population from 4 OA and 6 RA samples, and THY1+ DR+ population
from 6 RA samples. For monocytes, we sorted CD14+CD11c+++CD38+++ population from 2
RA samples and CD14+CD11c+ CD38− population from 2 OA samples. For B cells, we
sorted CD11c−IgD−CD27+ population from 6 RA samples, CD11c−IgD+CD27− population
from 3 RA samples, CD19+CD11c+ population from 3 RA samples, and plasma cells from 3
RA samples.
To validate the identified single-cell populations using bulk RNA-seq, we fit an LDA (Linear
Discriminant Analysis) classifier on the scRNA-seq cell clusters and then classified each
flow sorted bulk RNA-seq sample. For each cell type, 1) we trained an LDA model on the
scRNA-seq clusters with the top 500 marker genes for each cluster; 2) Next, we applied this
LDA model to classify each sample of bulk sorted cells and estimated the maximum
posterior probability for each sample. In summary, we tested if we could sort new cells from
new, independent samples and see the same gene expression profiles in the new bulk
samples as the original scRNA-seq samples.
Multicolor immunofluorescent staining of paraffin synovial tissue
Briefly, 5 mm thick formalin fixed paraffin sections were incubated in a 60°C oven to melt
paraffin. Slides were quickly transferred to xylenes to completely dissolve the paraffin and
after 5 minutes transferred to absolute ethanol. Slides were left in absolute ethanol for 5
minutes and then transferred to 95% ethanol. At the end of the 5 minutes immersion in 95%
ethanol, slides were rinsed several times with distilled water and transfer to a plastic coplin
jar filled with 1× DAKO retrieval solution (S1699, Dakocytomation). Antigens were
unmasked by immersing of plastic coplin jar in boiling water for 30 minutes. Slides were let
cool down for 10 minutes at room temperature and washed several times with distilled water.
Non-specific binding was blocked with 5% normal donkey serum (017-000-121, Jackson
ImmunoResearch Laboratories,) dissolved in PBS containing 0.1% Tween 20 and 0.1%
Triton X-100. Without washing, blocking solution was removed from slides and
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 14
combinations of primary antibodies were added to PBS containing 0.1% Tween 20 and 0.1%
Triton X-100. Primary antibodies to detect IFNg+ T cells include goat anti-CD3 epsilon
(clone M-20, Santa Cruz Biotechnology), mouse anti-human CD8 (clone 144B, GeneTex),
and rabbit anti-human IFNg (Biorbyt, orb214082). To visualize ABC, we incubated slides
with goat anti-human CD20 (LifeSpan Biosciences, LS-B11144), rabbit anti-Tbet (H-210,
Santa Cruz Biotechnology) and biotinylated mouse anti-human CD11c (clone 118/A5,
Thermo Fisher Scientific). To identify IL1B+ monocytes, we used a mixture of goat anti
human CD14 (119–13402, RayBiotech) biotinylated rabbit anti-human IL1b (OABF00305-
Biotin, Aviva Systems Biology) and mouse anti-human CD16 (clone DJ130c, LifeSpan
Biosciences). Finally, slides were probed with rabbit monoclonal anti-human CD90 (2694–
1, Epitomics), rat anti-human HLADR (cloneYE2/36 HLK, LifeSpan Biosciences) and
mouse anti-human CD45 (clone F10-89-4, abcam) to detect fibroblasts, Class II expressing
cells and hematopoietic cells, respectively. Slides with primary antibodies were incubated in
a humid chamber at room temperature, overnight. Next morning, primary antibodies for
triple T cell stain and for detecting ABC’s were revealed with Alexa Fluor 568 donkey anti-
goat IgG (A-11057, Thermo Fisher Scientific), Alexa Fluor 488 donkey anti-rabbit
(771-546-152, Jackson ImmunoResearch Laboratories) and Alexa fluor 647 donkey anti-
mouse (715-606-151, Jackson ImmunoResearch Laboratories). Primary antibodies in the
stain for monocytes were revealed with Alexa Fluor 568 donkey anti-goat Ig G, Alexa fluor
488 streptavidin (S11223, Thermo Fisher Scientific) and Alexa Fluor 647 donkey anti-
mouse Ig G. Primary antibodies in the stain for fibroblasts and hematopoietic cells were
detected with Cy3 donkey anti-rabbit (711-166-152, Jackson ImmunoResearch
Laboratories), Alexa Fluor 488 donkey anti-rat Ig G (A-21208, Thermo Fisher Scientific)
and Alexa Fluor 647 donkey anti-mouse Ig G. After 2 hours of incubation, slides were
washed and mounted with Vectashield mounting media with DAPI (H-1200, Vector
Laboratories). Pictures were taken with an Axioplan Zeiss microscope and recorded with a
Hamamatsu camera. Double immunofluorescence pictures were obtained by merging
individual channels in NIH Image J software.
Estimation of number of cells by counting nuclei
To estimate number of cells, we counted number of nuclei in 5 random 200× fields that show
synovial lining with Image J NIH software. Briefly, original color TIFF files were first
transformed into 8-bit grayscale images. We use similar settings to adjust threshold in 8-bit
images (Lower threshold level: 0, Upper threshold level: 60). Next, we used process: binary:
watershed to separate nuclei. In the analyze icon, we select analyze particles and we use
equal settings to count particles in our images (Size (pixel2): 50-infinity, circularity 0.00–
1.00, Show: outlines) and we selected to display results. We visually confirmed that
individual nuclei were outlined in the final image and calculate the average number of cells/
200× field in individual samples.
Tissue samples classification based on leukocyte infiltration
We classified RA tissue samples into leukocyte-poor RA and leukocyte-rich RA based on
Mahalanobis distance from OA samples computed on leukocyte abundance measured by
flow cytometry. We first took OA samples as a reference, and calculated a multivariate
normal distribution of the percentages of live T cells, B cells, and monocytes. Here we used
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Zhang et al. Page 15
the mahalanobis function in R: data x = a matrix of all 51 samples by flow gates of T cells,
B cells, and monocytes; center = mean of T cells, B cells, and monocytes for all OA
samples; covariance = covariance of T cells, B cells, and monocytes for all OA samples. We
calculated the square root to get Mahalanobis distance for each sample,
mah= x−μ'Σ−1x−μ .
We then defined the maximum value of all OA samples (4.5) as a threshold to define 19
leukocyte-rich RA (>4.5) and 17 leukocyte-poor RA (<4.5) samples in our cohort
(Supplementary Fig. 1d).
Bulk RNA-seq gene expression quantification
We sorted cells into the major immune and stromal cell populations: T cells, B cells,
monocytes and synovial fibroblasts. We then performed RNA sequencing. Full-length cDNA
and sequencing libraries were performed using Illumina Smart-eq2 protocol51. Libraries
were sequenced on MiSeq from Illumina to generate 35 base paired-end reads. Reads were
mapped to Ensembl version 83 transcripts using kallisto 0.42.4 and summed expression of
all transcripts for each gene to get transcripts per million (TPM) for each gene.
Bulk RNA-seq quality control
For quality control of bulk RNA-seq data, we began by defining common genes as the set of
genes detected with at least 1 mapped fragment in 95% of the samples. Then, for each
sample, we computed the percent of common genes detected in that sample. Low quality
samples are those that have less than 99% of common genes detected, and these were
discarded. We found that the low-quality samples also had low cell counts (Supplementary
Fig. 11a). After discarding 25 low quality samples, we used 167 good quality samples,
including 45 fibroblast samples, 46 monocyte samples, 47 T cell samples, and 29 B cell
samples in all bulk RNA-seq analyses. Cell lineage markers, PDGFRA, C1QA, CD3D, and
CD19, are expressed selectively by fibroblasts, monocytes, T cells, and B cells, respectively
(Supplementary Fig. 11c).
Single-cell RNA-seq gene expression quantification
Single-cell RNA-seq was performed using the CEL-Seq2 method47 with the following
modifications. Single cells were sorted into 384-well plates containing 0.6 μL 1% NP-40
buffer in each well. Then, 0.6 μL dNTPs (10mM each; NEB) and 5 nl of barcoded reverse
transcription primer (1 μg/μL) were added to each well along with 20 nL of ERCC spike-in
(diluted 1:800,000). Reactions were incubated at 65°C for 5 min, and then moved
immediately to ice. Reverse transcription reactions were carried out, as previously described
(Hashimshony et al., 2016), and cDNA was purified using 0.8× volumes of Agencourt
RNAClean XP beads (Beckman Coulter). In vitro transcription reactions (IVT) were
performed, as described followed by EXO-SAP treatment. Amplified RNA (aRNA) was
fragmented at 80°C for 3 min and purified using Agencourt RNAClean XP beads (Beckman
Coulter). The purified aRNA was converted to cDNA using an anchored random primer and
Illumina adaptor sequences were added by PCR. The final cDNA library was purified using
Nat Immunol. Author manuscript; available in PMC 2019 November 06.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
