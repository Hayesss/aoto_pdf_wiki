---
source_path: /mnt/c/Users/Administrator/Zotero/storage/TUR9NFYX/Zhang 等 - 2023 - Single-cell transcriptomics reveals multiple chemoresistant properties in leukemic stem and progenit.pdf
ingested: 2026-04-23
sha256: 4f491ed2f6e210d8
---

Zhang et al. Genome Biology (2023) 24:199 Genome Biology
https://doi.org/10.1186/s13059-023-03031-7
RESEARCH Open Access
Single-cell transcriptomics reveals multiple
chemoresistant properties in leukemic stem
and progenitor cells in pediatric AML
Yongping Zhang1†, Shuting Jiang2,3†, Fuhong He2,3†, Yuanyuan Tian1†, Haiyang Hu2,3, Li Gao1, Lin Zhang2,3,
Aili Chen2,3, Yixin Hu1, Liyan Fan1, Chun Yang4, Bi Zhou5, Dan Liu2, Zihan Zhou2,3, Yanxun Su2,3, Lei Qin2,3,
Yi Wang1, Hailong He1, Jun Lu1, Peifang Xiao1, Shaoyan Hu1* and Qian‑Fei Wang2,3*
†Yongping Zhang, Shuting Jiang,
Abstract
Fuhong He, and Yuanyuan Tian
contributed equally to this work. Background: Cancer patients can achieve dramatic responses to chemotherapy
*Correspondence: yet retain resistant tumor cells, which ultimately results in relapse. Although xenograft
hsy139@126.com; wangqf@big. model studies have identified several cellular and molecular features that are associ‑
ac.cn
ated with chemoresistance in acute myeloid leukemia (AML), to what extent AML
1 Department of Hematology
patients exhibit these properties remains largely unknown.
and Oncology, Children’s
Hospital of Soochow University, Results: We apply single‑cell RNA sequencing to paired pre‑ and post‑chemotherapy
Suzhou 215025, China
whole bone marrow samples obtained from 13 pediatric AML patients who had
2 CAS Key Laboratory
of Genomic and Precision achieved disease remission, and distinguish AML clusters from normal cells based
Medicine, Beijing Institute on their unique transcriptomic profiles. Approximately 50% of leukemic stem and pro‑
of Genomics, Chinese Academy
genitor populations actively express leukemia stem cell (LSC) and oxidative phospho‑
of Sciences and China National
Center for Bioinformation, rylation (OXPHOS) signatures, respectively. These clusters have a higher chance of tol‑
Beijing 100101, China erating therapy and exhibit an enhanced metabolic program in response to treatment.
3 University of Chinese Academy
Interestingly, the transmembrane receptor CD69 is highly expressed in chemoresistant
of Sciences, Beijing 100049,
China hematopoietic stem cell (HSC)‑like populations (named the CD69+ HSC‑like sub‑
4 Institute of Pediatric Research, population). Furthermore, overexpression of CD69 results in suppression of the mTOR
Children’s Hospital of Soochow
signaling pathway and promotion of cell quiescence and adhesion in vitro. Finally,
University, Suzhou 215025, China
5 SuZhou Hospital of Anhui the presence of CD69+ HSC‑like cells is associated with unfavorable genetic mutations,
Medical University, Suzhou, the persistence of residual tumor cells in chemotherapy, and poor outcomes in inde‑
China
pendent pediatric and adult public AML cohorts.
Conclusions: Our analysis reveals leukemia stem cell and OXPHOS as two major
chemoresistant features in human AML patients. CD69 may serve as a potential bio‑
marker in defining a subpopulation of chemoresistant leukemia stem cells. These find‑
ings have important implications for targeting residual chemo‑surviving AML cells.
Keywords: Residual tumor cell, Single‑cell RNA sequencing, AML, Chemotherapy
resistance, Leukemia stem cell, Oxidative phosphorylation, HSC‑like, CD69
© The Author(s) 2023. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits
use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third
party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the mate‑
rial. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://
creat iveco mmons. org/ licen ses/ by/4. 0/. The Creative Commons Public Domain Dedication waiver (http:// creat iveco mmons. org/ pub li
cdoma in/ zero/1. 0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.
Zhang et al. Genome Biology (2023) 24:199 Page 2 of 41
Background
Cancer patients often achieve dramatic responses to chemotherapeutic drugs yet
retain therapy-resistant tumor cells, which ultimately results in relapse and decreased
patient survival [1]. Chemotherapy serves as a main treatment strategy for acute
myeloid leukemia (AML), a neoplastic cancer characterized by the accumulation of
aberrant immature cells in the bone marrow (BM). To prevent AML relapse, increas-
ing attention is being paid to leukemia cells that can survive chemotherapy. Although
emerging sequencing technology has allowed more sensitive detection of those cells
through genetic mutations, the biological characteristics of chemoresistant cells in
AML patients remain largely unknown [2, 3].
Mouse model studies employing patient pre-chemotherapy samples have proposed
that leukemia stem cells (LSCs) with self-renewal properties can preferentially sur-
vive chemotherapy [4]. Nevertheless, this prediction is mainly based on their inher-
ent dormancy and has not been demonstrated in post-treatment patients [5]. In
contrast, accumulating evidence using xenograft models with cytarabine treatment
has found that chemoresistant properties were not associated with LSCs but resided
in cells with active oxidative phosphorylation (OXPHOS), chemo-induced leukemia
regenerating cells (LRC) or senescence-like cells [6–8]. However, to what extent AML
patients exhibit these cellular and molecular features remains largely unknown.
Single-cell RNA sequencing (scRNA-seq) has emerged as a powerful tool for reveal-
ing tumor heterogeneity and identifying subpopulations with distinct molecular sig-
natures [9]. Here, we applied scRNA-seq to paired pre- and post-chemotherapy whole
BM samples from AML patients to maximize the ability to detect leukemic cells and
evaluate their chemoresistant potential. We developed an efficient strategy to distin-
guish leukemic and normal cells based on their transcriptomes. Our analysis iden-
tified leukemic cell populations with distinct chemoresistant transcription features.
Remarkably, we identified a quiescent CD69+ HSC-like subpopulation with stem and
adhesion characteristics that could survive after chemotherapy. The clinical relevance
of this subpopulation was further determined by deconvolution analysis of two pub-
licly available cohorts. Collectively, our study provided the first in vivo characteriza-
tion of post-therapy tumor heterogeneity in AML patients and identified a key cell
population that may convey chemoresistance and drive disease recurrence.
Results
Single‑cell baseline transcriptome landscape of human normal hematopoiesis
To gain insight into the cellular diversity of leukemic cells, we first profiled the base-
line cellular diversity in normal hematopoiesis for comparison. We applied high-
throughput 10X Genomics scRNA-seq to profile 72,624 cells from nine healthy BM
and peripheral blood (PB) samples, including 40,326 CD34+-enriched cells, to inves-
tigate stem and progenitor populations. We also integrated three publicly available
scRNA-seq datasets with 82,950 cells to capture a broad representation of hemat-
opoietic cell types (Additional file 1: Fig. S1a; Additional file 2: Table S1) [10–12]. In
total, 155,574 high-quality cells from thirty-one samples from healthy donors were
combined for downstream analysis.
Z hang et al. Genome Biology (2023) 24:199 Page 3 of 41
After removing the batch effect, unsupervised clustering was performed, and the
results were visualized by uniform manifold approximation and projection (UMAP)
(see “Material and methods”; Additional file 1: Fig. S1b) [13]. Twenty cell types were
inferred according to well-known cell type-specific genes, including six hematopoi-
etic stem and progenitor cell (HSPC) populations as well as multiple myeloid, lym-
phoid, megakaryocyte, and erythroid populations (Fig. 1a-b and Additional file 1:
Fig. S1c; see “Material and methods”). Our cell type annotations were consistent with
recent scRNA-seq studies and published gene signatures (Additional file 1: Fig. S1d).
We further focused on the transcriptional characteristics of three cell types along the
hematopoietic stem cell (HSC) to myeloid progenitor axis, including HSC, lymphoid-
primed multi-potential progenitor (LMPP), and granulocyte–macrophage progenitor
(GMP) (n 26,423 cells). Gene set enrichment analysis (GSEA) revealed that HSCs pos-
=
sessed expression signatures enriched for stemness and quiescence, while LMPPs and
GMPs exhibited increased proliferation and OXPHOS expression (Fig. 1c). In agreement
with the enrichment analysis, HSCs overexpressed genes related to stem cell function,
including self-renewal regulators (CD34, MLLT3, MSI2, LYL1, HOPX) and cell cycle
regulators (SOCS2) (Fig. 1d and Additional file 3: Table S2). In contrast, both LMPPs
and GMPs highly expressed genes that were involved in cell cycle progression (TUBA1B,
TUBB, HMGB2, HMGN2, TUBA1B, ENO1), DNA replication, and metabolism path-
ways including ATP synthase and NADH dehydrogenase. GMPs also highly expressed
granule genes such as AZU1 and ELENE (Fig. 1d and Additional file 3: Table S2). In addi-
tion, cell cycle state prediction analysis further confirmed that HSCs contained a higher
proportion of cells in a resting cell cycle state (G0/G1 phase) than LMPPs and GMPs
(Additional file 1: Fig. S1e). Interestingly, quiescence, stemness, and OXPHOS features
have been associated with chemoresistance properties in leukemia cells [18].
Overall, we revealed that HSPC populations at different developmental stages had dis-
tinct molecular characteristics that are relevant to chemoresistance properties in AML.
In addition, the normal hematopoietic landscape serves as an important reference for
distinguishing leukemic cells and understanding their heterogeneity.
Identification and validation of AML cells from pre‑ and post‑chemotherapy whole bone
marrow populations
There is currently a lack of universal markers for the prospective isolation of leukemic
cells. To maximize the power to detect leukemic cells from a mixed population of leu-
kemic and normal cells, we used unsorted whole BM samples for high-throughput 10X
Genomics scRNA-seq. Twenty-six BM samples collected at two time points (pre- and
post-chemotherapy) from thirteen remission pediatric AML patients were sequenced
(Fig. 2a and Additional file 4: Table S3). Overall, we retained 227,842 high-quality cells
for downstream analyses, with an average of 8,763 cells per sample (range: 2,647–17,512;
Additional file 4: Table S3). Approximately 9,986 cells per post-chemotherapy sample
were analyzed for the identification of residual leukemic cells.
Previous studies have shown that leukemic cells within high tumor burden sam-
ples could be distinguished from normal cells based on their distinct transcriptomic
programs [19, 20]. We reasoned that a high tumor burden diagnostic sample could
serve as an anchor, and the AML cells with low abundance presented in the remission
Zhang et al. Genome Biology (2023) 24:199 Page 4 of 41
Fig. 1 Single‑cell transcriptome landscape of human normal hematopoiesis. a UMAP visualization of healthy
human hematopoietic cells (n 155,574 cells), with each dot representing a cell and colors indicating distinct
=
cell types. The inset plot provides an enlarged view of the six HSPC clusters, including HSC (hematopoietic
stem cell), LMPP (lymphoid‑primed multi‑potential progenitor), GMP (granulocyte–macrophage progenitor),
CLP (common lymphoid progenitor), MEP (megakaryocyte (MK) and erythroid progenitor), and E/B/M
(eosinophil/basophil/mast cell progenitor) that express three lineages‑specific canonical markers and MEP
commitment‑essential transcription factors, consistent with previous reports [14–17]. b Heatmap illustrating
cell type‑specific gene expression (rows) across various HSPC populations (columns). c GSEA plots showing
the representative gene signatures enriched in HSC, LMPP, and GMP populations with accompanying
normalized enrichment score (NES), p value, and false discovery rate (FDR) value. d Dot plot representing
the expression of representative genes involved in indicated biological processes in HSC, LMPP, and GMP
populations. Dot size signifies the proportion of cells expressing a gene in a cell population, while shading
represents the relative expression level
samples could be reliably identified by coclustering with the isolated leukemic cell
populations from diagnostic samples. We first tested the feasibility of this approach in
a published dataset in which both high quality scRNA-seq and mutational genotyping
data were available [21]. By compiling scRNA-seq data from healthy donors and seven
Z hang et al. Genome Biology (2023) 24:199 Page 5 of 41
Fig. 2 Identification and validation of AML cells in pre‑ and post‑chemotherapy whole bone marrow
samples. a Workflow illustrating the collection and processing of BM aspirates from 13 pediatric AML
patients for scRNA‑seq analysis. b UMAP shows the clustering of healthy donors (n 155,574 cells) with
=
paired pre‑ and post‑therapy samples from patient P115 (n 18,257 cells). Cells are color‑coded by sample
=
origin. The inset plot provides an enlarged view of leukemia clusters, with the predicted leukemic cell count
indicated. c UMAP visualization as in panel b, with cells colored based on detected mutant (purple) or
wild‑type (orange) transcripts. The number of mutant cells is indicated, and the percentage of mutant cells
assigned to predicted leukemia cells is noted in parentheses. d (Left) Scatterplot comparing the proportions
of predicted malignant cells determined by morphology and scRNA‑seq, with correlation coefficient (R)
and p values calculated using Pearson’s correlation test. (Right) Boxplot comparing the proportions of
post‑therapy malignant cells determined by scRNA‑seq, morphology, and flow cytometry, with each point
representing a sample and p values calculated using the Wilcoxon signed‑rank test. e Heatmap displays
KEGG pathways enriched by highly expressed genes in leukemic cells within each AML patient. f Ridge plots
showing the expression of RUNX1‑RUNX1T1 fusion gene signature in leukemic and normal cells from four
patients (P115, P116, P119, and P120) harboring this chromosomal translocation. g Violin plots depicting the
expression of Y chromosome‑located gene RPS4Y1 in cells from healthy female and male donors, as well as in
predicted leukemic and normal cells pre‑ and post‑chemotherapy from two patients (P105 and P115) with a
chromosome Y deletion. P values were calculated using the Wilcoxon signed‑rank test
Zhang et al. Genome Biology (2023) 24:199 Page 6 of 41
patients with matched pre- and post-therapy samples, we found that pre-therapy cells
in all seven patients formed separate clusters away from healthy donors. Noticeably,
in three patients with identifiable post-therapy malignant cells (AML7070B, AML328,
and AML329), a small proportion of post-therapy cells coclustered with pre-therapy
AML cells (Additional file 1: Fig. S2a). The predicted malignant cells derived from our
transcriptomic clustering were in high agreement with previous classifications using a
machine learning classifier based on integrated genomic and transcriptional informa-
tion in a published study (R 0.9; Additional file 1: Fig. S2b) [22]. Specifically, 78.04%
=
(range: 47.50%-98.63%) of post-therapy malignant cells assigned by the previous study
were also classified as malignant cells in our analysis, while few cells were identified
as malignant cells in post-therapy samples where the previous study detected no AML
cells. Overall, these data showed that our approach was able to identify malignant
cells, especially from patient specimens with rare malignant cells.
We further applied this method to classify leukemic cells in pre- and post-chemo-
therapy samples from our patient cohort. Based on the morphology and flow cytom-
etry examination, our untreated pre-therapy samples had a high tumor burden, with
an estimated average of 64.76% leukemia cells (range: 22%-92%), while post-chem-
otherapy BM samples predominantly showed enrichment of normal cells (> 95%)
and exhibited an average of 3.58% leukemia cells (range: 1%-9%; Additional file 4:
Table S3). We integrated scRNA-seq data from thirty-one healthy donors and paired
pre- and post- therapy samples from each patient, and performed UMAP projection
(Fig. 2b and Additional file 1: Fig. S2c). Our analysis identified two types of major
clusters: one almost entirely consisted of normal healthy donor cells, while the other
mainly comprised cells derived from pre-therapy samples. Interestingly, a small pro-
portion (~ 1.85%) of post-therapy cells colocalized with the pre-therapy clusters,
indicating that these post-therapy cells were residual leukemia cells that survived
chemotherapy. We defined a cluster as leukemic if more than 80% of the cells in this
cluster were derived from pre-therapy samples and exhibited a close relationship with
myeloid cells, while cells in the remaining clusters were classified as normal cells (see
“Material and methods”, Additional file 1: Fig. S2d). Overall, we identified an average
of 5,481 (range: 2,381–12,433) leukemic cells per diagnostic sample and an average
of 152 (range: 5–1,262) leukemic cells per post-treatment sample based on transcrip-
tional profiling (Additional file 4: Table S3). These transcriptionally predicted leu-
kemic cells averagely accounted for 71.43% and 1.85% of total pre- and post-therapy
cells, respectively. These data were highly consistent with clinical blast counts esti-
mated by morphology and flow cytometry analysis (Fig. 2d; Additional file 1: Fig. S2e).
Interestingly, the genes overexpressed in transcriptionally predicted leukemic cells
were found to be associated with activation of MYC, SATB1, and TAL1, as well as
repression of CEBPA, SPI1 (PU.1), FOXC1, NLRC5, and NONO. Most of these genes
were hematopoietic lineage-specific transcription factors, indicating that the healthy
hematopoietic process was repressed in those leukemic cells (Additional file 1: Fig.
S2f). Kyoto Encyclopedia of Genes and Genomes (KEGG) enrichment analysis
showed that those leukemic cells had high activities of pathways such as ribosome,
transcriptional misregulation in cancer, pathways in cancer, and hematopoietic cell
Z hang et al. Genome Biology (2023) 24:199 Page 7 of 41
lineage (Fig. 2e). These results were consistent with the distinct transcriptomic pro-
grams observed in malignant AML cells from a previous scRNA-seq study [14].
To independently validate these results, we examined the presence of somatic mutations,
expression signatures associated with chromosomal structural changes (translocation or
chromosome deletion), and the coexpression of leukemia-associated immunophenotype
(LAIP) markers in these transcriptionally predicted leukemic cells. First, targeted DNA
sequencing was used to identify high-confidence somatic mutations (see “Material and
methods”). Cells expressing the somatic mutations were identified using the scRNA-seq
data (see “Material and methods”; Fig. 2c and Additional file 4: Table S3). This analysis
enabled identification of the fraction of leukemic cells that harbored somatic mutations
in proximity to the 3’ end of the gene. An average of 148 (range: 9–455) pre- and post-
therapy mutant cells were identified per patient (Additional file 4: Table S3). More than
93% of those mutant cells in each sample were transcriptionally predicted to be leukemic
cells (Fig. 2c and Additional file 1: Fig. S2c). Second, patients with chromosomal altera-
tions (four patients with RUNX1-RUNX1T1 fusions and two patients with a Y chromo-
some deletion, with patient P115 concurrently carrying these two genomic lesions) were
validated by specific gene expression signatures for leukemic cells derived from pre- and
post-chemotherapy. In four patients with RUNX1-RUNX1T1 fusion gene, we exam-
ined the fusion target gene score of each cell based on the expression of known signature
genes (see “Material and methods”) [23]. It was apparent that these genes were prefer-
entially expressed at higher levels in leukemic cells from three patients (P115, P116, and
P119; Fig. 2f). Additionally, in two patients (P105 and P115) who harbored a Y chromo-
some deletion, Y chromosome transcripts were minimally detected in leukemic cells
(Fig. 2g). Notably, three patients (P105, P115, and P116) were transcriptionally predicted
to have more than 100 post-treatment leukemic cells. Those cells expressed significantly
higher levels of RUNX1-RUNX1T1 fusion transcripts, as well as the fusion gene-associated
expression signatures (P115 and P116; Fig. 2c, f and Additional file 1: Fig. S2g). In patients
(P105 and P115) who had a Y chromosome deletion, the predicted residual leukemic cells
minimally expressed Y chromosome transcripts (Fig. 2g). Third, flow cytometry was used
to identify leukemia cells with LAIP expression as previously described [24]. Eleven out of
thirteen patients had suitable expression of LAIP markers for defining and monitoring leu-
kemia cells at pre- and post-therapy (Additional file 4: Table S3). Cells coexpressing LAIP
markers were identified using the scRNA-seq data of these eleven patients (see “Material
and methods”, Additional file 4: Table S3). We observed that 94.73% of those cells were
classified as transcriptionally defined leukemia cells, while only 5.27% were classified as
transcriptionally defined normal cells (Additional file 1: Fig. S2c).
Together, these data indicate that we were able to confirm the identification of the
transcriptionally predicted leukemic cells from all thirteen patients using at least one
independent method (Additional file 1: Fig. S2i).
LSC and OXPHOS signatures were prevalent in leukemic stem and progenitor populations
and persistent in drug‑resistant subsets after chemotherapy
Leukemic cells from AML patients were found to reside in different cellular hierar-
chies [22, 25]. To identify leukemic cells with chemoresistant potential at the time of
diagnosis, we first annotated the cellular types of each of the AML cells. Specifically,
Zhang et al. Genome Biology (2023) 24:199 Page 8 of 41
each single cell was projected to the nearest healthy counterpart based on the cosine
similarity calculated from the expression of cell type-specific genes using the scmap
tool (see “Material and methods”) [26], which showed general agreement with previ-
ous classifications in annotating cell types across multiple public single-cell datasets
(Additional file 1: Fig. S3a, b). The tumor cells resembled one of the ten normal cell
types along the HSC to myeloid axis with a high median cosine similarity of 0.85
(range: 0.35–0.91; Additional file 1: Fig. S3c-d), and were named their healthy coun-
terpart with a “-like” suffix (Fig. 3a). Consistent with recent single cell studies [22],
the composition of different cell types varied between patients and generally agreed
with the clinical French–American–British (FAB) classification, except for in three
patients (P114, P118, and P120; Fig. 3b). To clarify this, we assessed the proportion
of HSPC-like cells using flow cytometry by examining the expression of canonical
stem cell markers (CD34 and CD117). Flow cytometry supported the scRNA-seq
prediction and showed a high proportion (77.40% and 95.14%) of HSPC-like popula-
tions in two patients (P114 and P118, Additional file 1: Fig. S3e).
We then investigated the chemoresistant potential of each tumor population based
on the presence of known chemoresistance-related gene expression signatures. Four
transcription signatures were identified to be associated with chemoresistance in PDX
models, including LSC activity, active OXPHOS, LRC, and senescence (Additional file 5:
Table S4) [6–8, 27, 28]. These molecular signatures represented distinct biological func-
tions with little overlap in the associated genes (Fig. 3c). Only leukemic cell populations
with sufficient cell numbers were used for the following analysis. Among the 73 cell
populations derived from thirteen patients, these features were significantly enriched
in the populations that resembled HSPCs, including HSC, LMPP, and GMP (20/37 vs,
0/36, p < 0.0001; Fig. 3d and Additional file 1: Fig. S4a). Interestingly, the presence of LSC
and OXPHOS signatures was mutually exclusive in different populations. Cell popula-
tions with the LSC signature were either HSC-like (7/12, 58.33%) or LMPP-like (6/13,
46.16%), while the OXPHOS signature was mainly restricted to a different subset of
LMPP-like and GMP-like cell populations. LRC and senescence signatures were largely
undetectable. In addition, LMPP-like cells showing different chemoresistant signa-
tures were from different AML patients. Specifically, LMPP-like cells within AML-M4/
M5 patients tended to highly express the OXPHOS signature, while those from AML-
M2 patients were likely to show LSC signatures (Additional file 4: Table S3). We also
examined the expression of the core enriched genes that contributed to each signature.
An analogous pattern of mutually exclusive expression of the core enriched genes was
observed in HSPC-like populations (Fig. 3e and Additional file 1: Fig. S4b). HSC- and/or
LMPP-like populations with LSC signatures highly expressed several well-known genes
related to stemness (e.g., CD34 and ERG). In contrast, LMPP-like and GMP-like sub-
populations with the OXPHOS signature exhibited higher expression of metabolic genes
(e.g., SLC25A1 and MRPS34).
To explore whether the two major chemoresistance features were exclusively pre-
sent in HSPC-like populations in independent cohorts, we reanalyzed recently pub-
lished scRNA-seq data from eleven adult AML samples [21]. Consistent with our
findings, 62.5% (five out of eight) of populations with LSC signatures were HSC-
like, while higher OXPHOS expression signatures were present in LMPP-like or
Z hang et al. Genome Biology (2023) 24:199 Page 9 of 41
Fig. 3 LSC and OXPHOS signatures were prevalent in leukemic stem and progenitor populations. a UMAP
plot illustrating the projection of transcriptionally predicted leukemic cells from thirteen AML patients onto
the normal hematopoietic hierarchy, based on transcriptomic similarity to normal cells. Projected cells are
highlighted, with shading indicating the frequency of being projected. b Bar plot showing the cell counts
of pre‑therapy leukemia cell populations in each AML patient. c Dot plot displaying pathways enriched by
four known chemoresistance‑related expression signatures derived from mouse model studies, with colors
representing enrichment p values. d Heatmap depicting the GSEA results of the four expression signatures in
panel c for each HSPC‑like population compared to all other leukemic populations within each patient before
therapy. Colors represent NES values obtained from GSEA analysis, and an asterisk denotes both NES > 1.9
and FDR < 0.001. Patient code colors indicate resistant (red) and sensitive (blue) cases. e Heatmaps showing
expression fold changes (FC) of core enriched genes (columns) contributing to LSC and OXPHOS signatures
in each HSPC‑like population (rows) compared to all other leukemic populations in three representative
patients (P116, P105, and P122). Core enriched genes are identified from GSEA results and those related to
cell stemness and metabolism are indicated
GMP-like populations (Additional file 1: Fig. S4c). The loss of self-renewal capac-
ity and increase in OXPHOS also occurred during normal myeloid development
(Fig. 1d), suggesting that these are conserved biological features in both normal and
Zhang et al. Genome Biology (2023) 24:199 Page 10 of 41
malignant conditions. Together, these findings suggest that LSC and OXPHOS, two
known chemoresistance-related signatures derived from mouse models, are present
in different HSPC-like populations.
To explore whether the populations containing LSC or OXPHOS signatures were
enriched for chemoresistant cells, we first examined the changes in AML cell com-
position over the course of chemotherapy. Interestingly, ten patients who achieved
complete remission (CR) displayed a decrease in cellular diversity in response to
treatment, with a significant reduction in the variety of early stem and progenitor
populations (Additional file 4: Table S3; Additional file 1: Fig. S4e). In contrast, two
(P116 and P105) out of three patients who achieved partial remission (PR) main-
tained diverse cell types (Additional file 4: Table S3; Additional file 1: Fig. S4e). Fur-
thermore, the presence of chemoresistance-related signatures was correlated with
treatment response. All seven diagnostic HSPC-like populations without LSC or
OXPHOS signatures were cleared after chemotherapy (Fig. 3d and Additional file 1:
Fig. S4e). In contrast, two (P116 and P105) out of seven patients whose pre-ther-
apy HSC-like cell populations carried LSC signatures had an average of 147 cells
(1.76% of total cells) that survived after chemotherapy, and half (three out of six;
P116, P105, and P124) of patients whose diagnostic LMPP-like populations carried
an active OXPHOS signature had 0.17%-2.57% of total cells persisting at remission
(Fig. 3d and Additional file 1: Fig. S2e). Importantly, the persistence of AML cells
after chemotherapy in these patients was also supported by morphology examina-
tion and flow cytometry data (Additional file 4: Table S3).
Next, we investigated the transcriptional features of AML cells that survived chem-
otherapy. Three patients (P105, P115, and P116) who had hundreds of cells (aver-
age: 492; range: 194–1,262) remaining after treatment were used for this analysis
(Fig. 4a-d). We performed high-dimensional clustering analysis and UMAP projec-
tion of pre- and post-therapy leukemic cells from each patient (Fig. 4a, b). This anal-
ysis revealed that most post-therapy cells overlapped with pre-therapy leukemic cells
in their distribution, while some cells showed transcriptional changes that shifted
their location within the projection (Fig. 4a). Single-cell gene signature score analy-
sis showed that post-therapy HSC- and LMPP-like cells maintained high expression
of LSC and OXPHOS signatures, respectively (Fig. 4e). Gene enrichment analysis of
the upregulated genes confirmed these results (Fig. 4f). Specifically, self-renewal-
associated signaling pathways (e.g., hypoxia and NF-κB) were highly expressed in
post-therapy HSC-like populations, while biological processes related to oxidative
phosphorylation were activated in progenitor-like cells (Fig. 4f). E/B/M-like cells in
P115 exhibited an increased transcriptional activity in the apoptosis pathway after
therapy (Fig. 4f), which was consistent with prior in vitro and in vivo studies show-
ing that cytarabine induces DNA double strand breaks and apoptotic morphology
[29]. Notably, post-therapy AML cells from patients who achieved partial remission
(P116 and P105) displayed activation of response to reactive oxygen species (PRDX2,
BTK, NRIP1) and heme metabolism signaling pathways (HBB, HBA1, HBA2) com-
pared to the pre-therapy populations (Fig. 4f, g). Together, these results indicate that
chemo-surviving HSPC-like cells acquire enhanced metabolic features while main-
taining the original LSC and OXPHOS signatures.
Z hang et al. Genome Biology (2023) 24:199 Page 11 of 41
Fig. 4 Dynamic cellular and transcriptomic changes in leukemic cells after chemotherapy in P116, P105,
and P115. a,c UMAP plots of leukemic cells from pre‑ and post‑therapy samples for each patient, with cells
color‑coded by sample origin (a) and cell type (c). b Bar plot showing the number of leukemic cells in
samples described in a. d Bar plot depicting the distribution of cell types in samples described in c. e Violin
plots of normalized single‑cell expression scores for LSC and OXPHOS signatures in HSC‑like and LMPP‑like
cells from patients P116 and P105, with black dots representing average signature expression. P values were
calculated using the Wilcoxon signed‑rank test. f Heatmap visualization of Metascape pathways enriched by
upregulated genes in each cell population from post‑therapy samples compared to pre‑therapy samples. g
Violin plots showing the expression of genes related to heme metabolism signaling pathways and response
to reactive oxygen species in pre‑ and post‑therapy cell populations
Identification of a chemoresistant HSC‑like subpopulation characterized by the surface
marker CD69
We further focused on the seven patients (out of thirteen; P116, P105, P122, P106,
P119, P118, and P115) whose HSC-like populations possessed LSC signatures. The
HSC-like populations persisted after therapy in two (P116 and P105) of the seven
patients (Figs. 3d and 4d). Therefore, we referred to the two patients with persis-
tent HSC-like populations as “resistant cases”. In contrast, HSC-like populations in
the remaining five patients became undetectable after therapy, and we referred to
Zhang et al. Genome Biology (2023) 24:199 Page 12 of 41
Fig. 5 Characterization of the CD69+ HSC‑like cell subpopulation potentially conferring chemoresistance.
a Heatmap displaying differentially expressed genes (DEGs) in pre‑therapy HSC‑like populations between
resistant cases (P105 and P116) and sensitive cases (P115, P106, P118, P119, and P120). b Bar plot presenting
representative suppressed biological functions enriched by DEGs in panel a using Ingenuity Pathway
Analysis (IPA). c GSEA plots showing the enrichment of quiescence, proliferation, adhesion (KEGG term: cell
adhesion molecules), and migration (KEGG term: leukocyte transendothelial migration) signatures in HSC‑like
cells from resistant cases compared to sensitive cases. d Dot plots of normalized expression of differentially
expressed surface marker genes between resistant and sensitive cases. Dot size represents the proportion of
cells expressing a gene in a patient’s HSC‑like cell population, and shading indicates the relative expression
level. e Violin plots depicting CD69 expression in HSC‑like populations from patients and HSC populations
from healthy donors. f Regulatory network showing upstream regulators and their targets predicted to be
activated or suppressed in HSC‑like cells from resistant cases. Colors indicate increased (red) or decreased
(green) gene expression relative to sensitive cases. Red and blue lines represent known activating or
inhibitory effects, respectively, between each regulator and its targets
these patients as “sensitive cases” (Additional file 1: Fig. S4e). To explore the molecu-
lar features underlying the differential therapy response of HSC-like populations, we
compared pre-therapy HSC-like populations from resistant and sensitive cases. We
found 117 differentially expressed genes (DEGs) that were unique to patients with
Z hang et al. Genome Biology (2023) 24:199 Page 13 of 41
a resistance phenotype (Fig. 5a and Additional file 6: Table S5). Ingenuity Pathway
Analysis (IPA) biological function and upstream regulator analysis revealed that
those genes were related to the repression of proliferation of stem cells (e.g., CDK6,
CCND1, JUNB, SPARC ), cellular movement (e.g., CD69, DUSP1, LGALS1, ANXA1),
hematopoietic differentiation regulators (e.g., GATA1, CEBPA, RUNX1, ZFP36) and
activation of glucose metabolism (e.g., SOD2, MT-CO2; Fig. 5b, Additional file 1: Fig.
S5a, and Additional file 7: Table S6). Consistently, GSEA showed that the HSC-like
populations from resistant cases were enriched for specific gene expression signatures
derived from hematopoietic cells, including HSC self-renewal capacity, leukemia qui-
escent state, and leukocyte adhesion (Fig. 5c). Although these biological processes
were similarly present in the LSC expression signature, this analysis suggests that the
HSC-like populations from resistant cases may have enhanced functions.
Among several differentially expressed cell surface marker genes (CD69, CD79A,
CD317/BST2, RGS10, and B2M), CD69, a type II transmembrane C-type lectin recep-
tor, exhibited the most prominent difference between resistant and sensitive HSC-like
cells (fold change 1.75; Fig. 5d and Additional file 6: Table S5). Furthermore, in the two
=
resistant patients, nearly 90% of HSC-like cells expressed CD69 (90.00% in P105 and
89.20% in P116), while less than 40% of HSC-like cells (median: 39.52%, range: 24.40%-
88.97%) from the sensitive patients did (Fig. 5d-e). These data suggested that HSC-like
populations that were able to survive chemotherapy were dominated by CD69+ cells
(named the CD69+ HSC-like subpopulation), while those that became undetectable
after chemotherapy were enriched for CD69− HSC-like cells (named the CD69− HSC-
like subpopulation, Fig. 5d-e). In addition, the UMAP projection of HSC-like popula-
tions from these seven patients showed two major clusters (Additional file 1: Fig. S4f).
Resistant HSC-like subpopulations were clustered together and showed significantly
higher expression of CD69, while the majority (four out of five) of sensitive HSC-like
subpopulations formed another cluster with lower expression of CD69. The expression
of CD69 was still maintained in post-therapy HSC-like subpopulations of the two resist-
ant patients (Additional file 1: Fig. S5b). In addition, the mRNA and surface protein lev-
els of CD69 showed a strong correlation in primary AML samples (R 0.89, p 0.045;
= =
Additional file 1: Fig. S5c), and the expression of CD69 was minimally detected in HSCs
from healthy donors (Fig. 5e, Additional file 1: Fig. S5d). These findings suggest that
CD69 can serve as a potential biomarker for chemoresistant HSC-like subpopulations.
Considering that CD34+CD38− leukemic cells immunophenotypically resemble HSCs
and functionally enrich LSCs, we investigated whether the CD69+CD34+CD38− popu-
lation could recapitulate the expression signature in a single-cell analysis-defined CD69+
HSC-like subpopulation. We utilized publicly available bulk microarray expression pro-
files of flow cytometry-sorted C D34+CD38− cells. We divided 54 samples from 78 AML
patients into the CD69+CD34+CD38− group and the CD69−CD34+CD38− group based
on the expression level of CD69 (See “Material and methods”; Additional file 1: Fig.
S5e) [30]. The differential gene expression analysis between these two groups (named
“bulkRNA DEGs”) revealed a similar set of biological function terms with our scRNA
DEGs (Additional file 1: Fig. S5f-g). Specifically, bulkRNA DEGs of CD69+CD34+CD38−
cells were associated with the activation of adhesion (CXCR4, DUSP1, CXCL2, CCL3/5,
CCL3L1/3), viability (MCL1, LYZ), cell cycle repression (SPARC, CDKN1A, BTG1/2),
Zhang et al. Genome Biology (2023) 24:199 Page 14 of 41
and suppression of differentiation (RUNX1, ZFP36), as revealed by IPA biological
function analysis (Additional file 1: Fig. S5f,h and Additional file 8: Table S7). In agree-
ment with these findings, the known signatures relevant to leukemia quiescence and
adhesion to vascular endothelial cells were enriched in CD69+CD34+CD38− popula-
tions (Additional file 1: Fig. S5i). Therefore, this dataset supported the notion that the
CD69+CD34+CD38− combination serves as a surrogate for enriching the CD69+ HSC-
like subpopulation.
In addition, we were particularly interested in investigating the regulatory network to
provide mechanistic information related to drug resistance. Upstream regulator analysis
identified MTOR and STAT3 as two major suppressed hubs, which were associated with
decreased expression of cell cycle regulators (e.g., CDK6 and CCND1) as well as upreg-
ulation of CXCR4-mediated microenvironmental interaction molecules (e.g., PIM1) in
CD69+ HSC-like subpopulations (Fig. 5f). As the expression level of CD69 in AML cell
lines was either very low or undetectable, CD69-overexpressing AML cell lines were
established (Additional file 1: Fig. S6a), to address the functional role of CD69 in regulat-
ing its downstream pathways. We found that CD69 overexpression resulted in reduced
phosphorylated protein levels of mTOR and its key downstream effectors (P70S6K and
4EBP1), as well as decreased total protein levels of mTOR and P70S6K in both HL60
and Kasumi-1 cells (Fig. 6a). The relative levels of phosphorylation of mTOR, P70S6K
and 4EBP1, shown as the fold change in the levels of phosphorylated protein over total
protein levels, were significantly lower in CD69-overexpressing cell lines than those in
controls. The total and phosphorylated protein levels of STAT3 were comparable in con-
trol and CD69-overexpressing HL60 or Kasumi-1 cells, respectively (Additional file 1:
Fig. S6b). Moreover, CD69 overexpression decreased the expression of the classic prolif-
eration marker Ki67 and the regulators CCND1 and CDK6, and increased the adhesion
molecule CXCR4 expression (Fig. 6b-d). Subsequently, we analyzed the adhesive inter-
action of these cell lines with human mesenchymal stem cells (hMSCs). Cell adhesion
assays showed that CD69 overexpression significantly increased the ratio of adherent
cells to hMSCs (Fig. 6e). Since homing to bone marrow is a crucial step for AML cells
to interact with stromal cells, we used a Transwell assay to determine if CD69 affects
AML cell migration to CXCL12, which is expressed in BM niches. CD69 overexpres-
sion increased cell migration toward a high gradient of CXCL12 (Fig. 6f). These data
suggested that CD69 enhanced cell adhesion and homing to the BM niche through the
(See figure on next page.)
Fig. 6 CD69 overexpression inhibits the mTOR pathway and enhances AML cell adhesion and migration.
a (Left) Western blot showing total and phosphorylated protein levels of mTOR, 4EBP1, and P70S6K in
negative control (NC) and CD69‑overexpressing HL60 and Kasumi‑1 cells. (Right) Bar plots displaying relative
quantification by densitometry. b (Top) Western blot showing total protein levels of CDK6 and CCND1 in NC
and CD69‑overexpressing HL60 and Kasumi‑1 cells. (Bottom) Bar plots displaying relative quantification by
densitometry. c Representative histograms (left) and corresponding statistical results (right) of flow cytometry
analyses showing protein levels of the classic proliferation marker Ki67 in NC and CD69‑overexpressing
HL60 and Kasumi‑1 cells. d Representative histograms (left) and corresponding statistical results (right)
of flow cytometry analyses showing protein levels of surface chemokine receptor CXCR4 on NC and
CD69‑overexpressing HL60 and Kasumi‑1 cells. e Representative images (left) and corresponding statistical
results (right) showing adhesion capacity of NC and CD69‑overexpressing HL60 and Kasumi‑1 cells to hMSCs.
f Representative images (left) and corresponding statistical results (right) showing migration of NC and
CD69‑overexpressing HL60 and Kasumi‑1 cells toward CXCL12 and S1P respectively. * p < 0.05; **p < 0.01;
***p < 0.001; ns, not significant; t test. Mean SEM values are shown for panels a, c‑f
±
Z hang et al. Genome Biology (2023) 24:199 Page 15 of 41
Fig. 6 (See legend on previous page.)
CXCR4-CXCL12 interaction. In concordance with our findings in AML cell lines, the
protein levels of Ki67 were significantly reduced and the protein levels of CXCR4 were
increased in CD69highCD34+CD38− populations from primary AML patients (Addi-
tional file 1: Fig. S7a-c).
Collectively, these findings suggest that CD69+ HSC-like cells possess enhanced abili-
ties to adhere to the microenvironment and maintain cellular quiescence via dysregu-
lated mTOR signaling, potentially contributing to their resistance to chemotherapy.
