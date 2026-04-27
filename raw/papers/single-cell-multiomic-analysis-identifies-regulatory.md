---
source_path: /mnt/c/Users/Administrator/Zotero/storage/JERJ7THN/Granja 等 - 2019 - Single-cell multiomic analysis identifies regulatory programs in mixed-phenotype acute leukemia.pdf
ingested: 2026-04-23
sha256: cda7bbb60008f870
---

Letters
https://doi.org/10.1038/s41587-019-0332-7
Single-cell multiomic analysis identifies regulatory
programs in mixed-phenotype acute leukemia
Jeffrey M. Granja1,2,3,13, Sandy Klemm 3,13*, Lisa M. McGinnis3,4,13*, Arwa S. Kathiria3, Anja Mezger3,5,
M. Ryan Corces1,4, Benjamin Parks 3,6, Eric Gars4, Michaela Liedtke7, Grace X. Y. Zheng 8,
Howard Y. Chang 1,3,9,10, Ravindra Majeti7 and William J. Greenleaf 1,3,11,12*
Identifying the causes of human diseases requires deconvolu- were highly correlated (Supplementary Fig. 1a–e). We then selected
tion of abnormal molecular phenotypes spanning DNA acces- a feature set of transcripts to mitigate batch effects and linearly pro-
sibility, gene expression and protein abundance1–3. We present jected retained transcript counts into a lower-dimensional space
a single-cell framework that integrates highly multiplexed using latent semantic indexing9[,10 (LSI; Methods). Cells were clus-
protein quantification, transcriptome profiling and analysis tered using Seurat’s shared nearest neighbor (SNN) approach11,
of chromatin accessibility. Using this approach, we establish annotated using a manually curated maker gene list and visualized
a normal epigenetic baseline for healthy blood development, using uniform manifold approximation and projection (UMAP)12
which we then use to deconvolve aberrant molecular features (Fig. 1b and Supplementary Fig. 1f).
within blood from patients with mixed-phenotype acute leu- We next established an epigenetic map of normal hematopoiesis
kemia4,5. Despite widespread epigenetic heterogeneity within by measuring chromatin accessibility across 35,038 single BMMCs
the patient cohort, we observe common malignant signatures (n = 16,510), CD34+ BMMCs (n = 10,160) and PBMCs (n = 8,368)
across patients as well as patient-specific regulatory features using droplet scATAC-seq (10x Genomics)7. These cells exhibited
that are shared across phenotypic compartments of individual a canonical fragment-size distribution with clearly resolved sub-,
patients. Integrative analysis of transcriptomic and chroma- mono- and multinucleosomal modes, a high signal-to-noise ratio
tin-accessibility maps identified 91,601 putative peak-to-gene at transcription start sites (TSSs), an average of 11,597 uniquely
linkages and transcription factors that regulate leukemia- accessible fragments per cell on average, a majority (61%) of Tn5
specific genes, such as RUNX1-linked regulatory elements insertions aligning within peaks and high reproducibility across
proximal to the marker gene CD69. These results demonstrate replicates (Supplementary Fig. 2a–h). Using LSI, Seurat’s SNN clus-
how integrative, multiomic analysis of single cells within tering and UMAP, we generated a chromatin-accessibility map of
the framework of normal development can reveal both hematopoiesis that complements the transcriptional map of hema-
distinct and shared molecular mechanisms of disease from topoiesis (Fig. 1c and Supplementary Fig. 2i).
patient samples. To validate the proposed transcriptomic and epigenetic single-
To identify pathologic features within neoplastic cells, we first cell maps of hematopoiesis, we directly visualized lineage-restricted
aimed to establish molecular features of normal development for cell-surface marker and transcription-factor (TF) enrichment
comparison. As mixed-phenotype acute leukemias (MPALs) pres- across each map. As anticipated, both scADT- and scRNA-seq mea-
ent with features of multiple hematopoietic lineages, we first con- surements of surface makers demonstrate CD3D enrichment across
structed independent immunophenotypic, transcriptomic and bone marrow and peripheral T cells; CD14 enrichment within the
epigenetic maps of normal blood development using droplet-based monocytic lineage; broad up regulation of CD19 across the B cell
cellular indexing of transcriptomes and epitopes by sequenc- lineage; and CD8A enrichment within cytotoxic T lymphocytes13
ing (CITE-seq)6 (combined single-cell antibody-derived tag and (Fig. 1d). Estimates of gene activity on the basis of correlated varia-
RNA sequencing) and single-cell assay for transposase-accessible tion in promoter and distal-peak accessibility (Cicero14) broadly
chromatin using sequencing (scATAC-seq; single-cell chromatin- recapitulates this pattern, confirming that lineage specification
accessibility profiling)7 on bone marrow and peripheral blood is consistently reflected across the phenotypic, transcriptional
mononuclear cells (BMMCs and PBMCs, respectively; Fig. 1a). For and epigenetic maps of hematopoietic development (Fig. 1d). We
CITE-seq analyses, we simultaneously generated 10x Genomics 3′ then visualized our scADT-seq data of BMMCs and PBMCs using
single-cell RNA sequencing8 (scRNA-seq) and antibody-derived UMAP and found that we could broadly recapitulate our transcrip-
tag sequencing6 (scADT-seq; Supplementary Table 3) libraries from tomic hematopoietic map (Supplementary Fig. 1g,h). To further
35,882 BMMCs (n = 12,602), CD34+-enriched BMMCs (n = 8,176) support these cell-type identifications and developmental map-
and PBMCs (n = 14,804). On average, 1,273 informative genes (2,370 pings, we show concordance between three separate single-cell
unique transcript molecules) were detected per cell and replicates measurements, including direct transcript measurements from the
1Center for Personal Dynamic Regulomes, Stanford University School of Medicine, Stanford, CA, USA. 2Biophysics Program, Stanford University School of
Medicine, Stanford, CA, USA. 3Department of Genetics, Stanford University School of Medicine, Stanford, CA, USA. 4Department of Pathology, Stanford
University School of Medicine, Stanford, CA, USA. 5Department of Medical Biochemistry and Biophysics, Karolinska Institute, Stockholm, Sweden.
6Department of Computer Science, Stanford University School of Engineering, Stanford, CA, USA. 7Department of Medicine, Division of Hematology,
Stanford Cancer Institute, Stanford University School of Medicine, Stanford, CA, USA. 810x Genomics, Pleasanton, CA, USA. 9Department of Dermatology,
Stanford University School of Medicine, Redwood City, CA, USA. 10Howard Hughes Medical Institute, Stanford University School of Medicine, Stanford,
CA, USA. 11Department of Applied Physics, Stanford University, Stanford, CA, USA. 12Chan–Zuckerberg Biohub, San Francisco, CA, USA. 13These authors
contributed equally: Jeffrey M. Granja, Sandy Klemm, Lisa M. McGinnis. *e-mail: klemm@stanford.edu; lisa.mcginnis@stanford.edu; wjg@stanford.edu
1458 NAtuRE BiotECHNoLoGY | VOL 37 | DECEMBER 2019 | 1458–1465 | www.nature.com/naturebiotechnology
NATUre BIoTechNology Letters
scRNA-seq dataset, inferred gene-activity scores from the scATAC- cell sorting (FACS) into our chromatin and transcription hemato-
seq dataset and TF activity using chromVAR15, for key develop- poietic maps and found high concordance with our healthy hema-
mental TFs, including CEBPB in monocytic development, GATA1 topoietic map and cluster definitions (Supplementary Fig. 6b). To
within the erythroid lineage and TBX21 in NK and CD8+ T mem- further validate our approach, we projected published scRNA-seq19
ory cells, as well as PAX5 in B cell and plasmacytoid dendritic and scATAC-seq20–22 data from different platforms and different
cell development (Fig. 1e). High-resolution single-cell multiomic genomes on our chromatin and transcription hematopoietic maps
tracks for key marker genes in each of the identified lineages fur- and found striking agreement (Supplementary Fig. 6c). Lastly, we
ther support these identifications (Fig. 1f,g and Supplementary used our iterative LSI approach on 299,337 cells from the Human
Fig. 3a–h). Collectively these results show that the proposed multiomic Cell Atlas (HCA) ‘Census of Immune Cells’ bone marrow data23
maps of healthy hematopoiesis are consistent and broadly capture (Supplementary Fig. 6d). By projecting our own hematopoietic
essential phenotypic, transcriptomic and epigenetic features of data into the subspace defined by these HCA data (Supplementary
blood development. Fig. 6d) we observe that our cohort reasonably repopulates the
Recent work has shown that immunophenotypically distinct hematopoietic manifold created from this completely distinct set of
subpopulations of MPAL blasts have similar genomic lesions within donors. These results show that our dataset and method can accu-
a patient, and that cells from one lineage can reconstitute the alter- rately identify the hematopoietic signature for chromatin and gene
nate lineage in xenograft models16, suggesting that MPAL lineage expression at a single-cell resolution.
plasticity may be epigenetically regulated. To explore the nature of Using this LSI-projection framework and landscapes of healthy
this regulatory and phenotypic dysfunction, we assayed six MPAL hematopoiesis, we next sought to deconvolve the normal and leuke-
samples including three T–myeloid MPALs (MPAL1–MPAL3), mic signatures of MPAL samples at a single-cell resolution. First, the
1 B myeloid MPAL (MPAL4) and one T–myeloid MPAL sampled leukemic single cells were projected into the hematopoietic linear
before CALGB chemotherapy (MPAL5) and after post-treatment LSI subspace. Next, we identified a non-redundant set of healthy
relapse (MPAL5R) (Supplementary Table 1). Across these samples, hematopoietic cells that were nearest-neighbor normal cells to each
we observed extensive immunophenotypic heterogeneity (via diag- leukemic cell, irrespective of their cell-type boundaries. Lastly, we
nostic flow cytometry analysis) including bilineal patterns (multiple computed the differences between the leukemic cells and near-
blast populations expressing both lymphoid and myeloid lineage est normal cells to identify the leukemic specific signature. We
antigens), biphenotypic patterns (a dominant blast population that first tested our approach by analyzing recently published scRNA-
simultaneously expresses both lymphoid and myeloid antigens) seq data from samples from patients with acute myeloid leukemia
and both patterns (Supplementary Fig. 4a–f). We then performed (AML)19. By projecting the AMLs into our healthy hematopoietic
whole-exome sequencing (WES) and found mutational profiles map, we see general agreement with previous classifications without
similar to previous studies16,17 (Supplementary Fig. 4g). To further the need for potentially arbitrary cell-type boundaries on normal
profile our MPAL samples, we performed CITE-seq (18,056 cells) hematopoiesis (Supplementary Fig. 7a–c). We next wanted to clas-
and scATAC-seq (35,423 cells) on either peripheral blood or bone sify our phenotypically diverse samples from patients with MPAL
marrow aspirates from these patients with MPAL, observing reason- using our hematopoietic maps. First, we clustered our MPALs with
able data quality per cell as compared to that obtained for healthy our hematopoietic data to classify cells as ‘disease-like’ MPAL cells
samples (Supplementary Fig. 5a–m). or ‘healthy-like’ cells (Supplementary Fig. 8a). These classifications
Using our transcriptomic and chromatin landscapes of healthy generally agreed with the fraction of cells classified as blasts by
hematopoiesis, we next sought to develop an analytical framework morphology or flow cytometry (Supplementary Fig. 8b). We then
to identify the hematopoietic developmental signature at single-cell projected our MPAL single cells onto our hematopoietic maps and
resolution. First, the chromatin and gene expression signatures of discovered broad epigenetic and gene-expression diversity. To fur-
single cells are projected into the LSI subspace of our ATAC- and ther resolve this diversity, we grouped MPAL cells within individual
RNA-based healthy hematopoietic map, and the results are then patients into broad hematopoietic developmental compartments:
visualized using UMAP (Fig. 2a and Supplementary Fig. 6a). Next, progenitor-like (comprising human stem cell and multipotent pro-
by determining the closest hematopoietic cells to the projected cells genitor-like cells), lymphoid-like (comprising lymphoid-primed
we can identify the hematopoietic developmental compartment. multipotent progenitors), erythroid-like (includes megakaryo-
This method does not require defining discrete cell -type boundaries cyte-erythroid progenitors), myeloid-like (includes granulocyte-
and uses a large feature set to robustly position cells within the con- monocyte progenitors) and T/natural killer (NK)-like (includes
tinuous landscape of hematopoiesis. To validate this approach, we differentiated T and NK cells24) (Fig. 2a,b and Supplementary
first projected downsampled published bulk RNA-seq and ATAC- Fig. 8a). The scADT-seq data resolve the dominant subpopulations in
seq data18 from subpopulations identified by fluorescence-activated the bilineal MPAL1 and MPAL5; however, it does not fully capture
Fig. 1 | Multiomic epigenetic and phenotypic analysis of human hematopoiesis. a, Schematic of multiomic profiling of chromatin accessibility,
transcription and cell-surface antibody abundance on healthy bone marrow and PBMCs using CITE-seq (combined single-cell RNA and antibody-derived
tag sequencing for each single cell, scRNA-seq and scADT-seq, respectively) and scATAC-seq. b, scRNA-seq LSI UMAP projection of 35,882 single
cells across healthy hematopoiesis. Below are the biological classifications for the scRNA-seq clusters (see Supplementary Table 1). c, Top, scATAC-
seq LSI UMAP projection of 35,038 single cells across healthy hematopoiesis. Bottom, the biological classifications for the scATAC-seq clusters (see
Supplementary Table 1). d, Surface-marker overlay on single-cell RNA UMAP (as in b) of ADT antibody signal (top; center-log ratio (CLR) normalized),
single-cell RNA (middle; log(gene expression) (Exp)) and single-cell ATAC log(gene-activity scores (GA)) for CD3D, CD14, CD19 and CD8A (bottom).
2 2
e, TF overlay on single-cell ATAC UMAP (as in c) of TF chromVAR deviations (top), gene-activity scores (middle) and single-cell RNA for CEBPB, GATA1,
TBX21 and PAX5 (bottom). f,g, Multiomic track of CD14 (specific in these clusters for monocytes) across monocyte development from HSC progenitor
cells (f; n = 1,425–4,222) and multiomic track of CD19 (specific in these clusters for pre-B cells) across B cell development (g; n = 62–2,260). Multiomic
tracks; average track of all clusters displayed (left top), binarized 100 random scATAC-seq tracks for each locus at a resolution of 100 bp (left bottom),
scRNA-seq log violin and box plots of normalized expression for each cluster and scADT-seq CLR violin and box plots of protein abundance for each
2
cluster (right). Violin plots represent the smoothed density of the distribution of the data. In box plots, the lower whisker is the lowest value greater than
the 25% quantile minus 1.5 times the interquartile range (IQR), the lower hinge is the 25% quantile, the middle is the median, the upper hinge is the 75%
quantile and the upper whisker is the largest value less than the 75% quantile plus 1.5 times the IQR.
NAtuRE BiotECHNoLoGY | VOL 37 | DECEMBER 2019 | 1458–1465 | www.nature.com/naturebiotechnology 1459
Letters NATUre BIoTechNology
the transcriptional diversity in the other MPALs 2–4 (Supplementary classifications (Fig. 2b). Comparing MPAL gene expression to
Fig. 8c). We visualized these projected MPALs colored by these this healthy nearest-neighbor set allowed the identification of
broad hematopoietic compartments, observing the expected pathogenic differential gene expression for MPALs from different
high concordance between the scRNA-seq and scATAC-seq compartments. In total, we identified 4,616 genes that were
a b c
scRNA-seq (35,882 cells) scATAC-seq (35,038 cells)
B
Erythroid HSC CLP
NK
CD8M
Plasma
Basophil pDC
Neutrophil
GMP CD4N
CD8N
Monocytes
2
noisnemid
PAMU
HSC Basophil Erythroid
CLP
NK
B
CD4M CD8M
pDC
GMP
Plasma
CD8N
CD4N
Monocytes
UMAP dimension 1
2
noisnemid
PAMU
CITE-seq
+
AAAAAA
AAAAAA
AAAAAA
Healthy
bone marrow
and blood scATAC-seq Neutrophil CD4M
UMAP dimension 1
d
f
e
g
srekram
ecafruS
noisserpxE
ytilibissecca
nitamorhC
)TDAcs(
)ANRcs(
)CATAcs(
chr5:139,963,285−140,063,286
0 2 4 6
HSC
CMP/LMPP
GMP
CD14 Mono 1
CD14 Mono 2
Strand
CD14 −
+
chr16:28,893,259−28,993,260
HSC
CMP/LMPP
CLP 1
CLP 2
Pre B
B cell
Plasma
Strand
−
CD19 +
rekram
ecafruS
noisserpxE
ytivitca
eneG
ytivitca
FT
ytivitca
eneG
noisserpxE
Surface markers
TFs
UMAP dimension 1
2
noisnemid
PAMU
CEBPB GATA1 TBX21 PAX5
2
noisnemid
PAMU
Biological classification
CD3D CD14 CD19 CD8A scRNA scATAC scRNA scATAC scRNA scATAC
HSC HSC cDC cDC CD8 N CD8 N
Early eryth. Early eryth. CD14 mono 1 CD14 mono 1 CD4 N1 CD4 N1
Late eryth. Late eryth. CD14 mono 2 CD14 mono 2 CD4 N2 CD4 N2
Early basophil Early basophil CD16 mono Unk. CD4 M CD4 M
CMP/LMPP CMP/LMPP Unk. Unk. CD8 EM CD8 EM
CLP 1 CLP 1 CLP 2 CLP 2 CD8 CM CD8 CM
GMP GMP Pre B Pre B NK NK
GMP/Neut. GMP/Neut. B B Unk. Unk.
pDC pDC Plasma Plasma
scRNA scADT
(logEx.) (CLR Ab.)
2
Average 0 2 4
UMAP dimension 1
scRNA scADT
(logEx.) (CLR Ab.)
Average 2
0123450 2 4 6
scADT scRNA Cicero chromVAR
(CLR Ab.) (logEx.) (logGA) Deviation scores
2 2 Promoter region Putative enhancer region
CITE-seq scATAC-seq
Min Max Min Max Min Max Min Max
1460 NAtuRE BiotECHNoLoGY | VOL 37 | DECEMBER 2019 | 1458–1465 | www.nature.com/naturebiotechnology
NATUre BIoTechNology Letters
significantly upregulated (log fold change (LFC) > 0.5 and false- programs. First, we identified which TFs were differentially enriched
2
discovery rate (FDR) < 0.01, see Supplementary Table 4) in at in each k-means cluster of differentially accessible peaks observed
least one MPAL subpopulation across the six patient samples, and in Fig. 2c (Fig. 3a and Supplementary Table 5). We found that
grouped these genes with k-means clustering (Fig. 2c). We further RUNX1 motifs were highly enriched in both cluster 4 and 10—the
categorized the most conserved differential genes, TFs and KEGG two clusters corresponding to the most commonly shared accessible
pathways across the MPALs25 (Supplementary Fig. 9a–c). Using elements across MPAL subset populations. In addition, RUNX1 is
the same approach for the scATAC-seq data, we performed test- significantly upregulated in about half (7 of 17) of the MPAL sub-
ing of differential peaks for each MPAL subpopulation and found populations. RUNX1 is one of the most frequently mutated genes
72,196 significantly upregulated peaks (LFC > 0.5 and FDR < 0.05; across hematologic malignancies acting as both a tumor suppres-
Supplementary Table 4) in at least one MPAL subpopulation (Fig. 2c). sor with loss-of-function mutations in AML29, myelodysplastic syn-
Multiomic differential tracks for the cyclin-dependent kinase drome30 and ETP T-ALL31,32, and as a putative oncogene in non-ETP
CDK11A and cyclin-dependent kinase inhibitor CDKN2A, genes T-ALL33,34. Furthermore, wild-type RUNX1 has been implicated as a
that are recurrently mutated in MPAL16,26, demonstrate these leuke- potential driver of leukemogenesis in core-binding factor leukemia35
mia-specific ATAC-seq and RNA-seq differences (Supplementary and mixed-lineage leukemia36.
Fig. 9d,e). Additionally, we calculated Pearson correlations of the To link RUNX1 and other putative regulatory TFs to their leu-
differential genes and peaks and found that transcription and acces- kemic programs we first developed an analytical framework that
sibility differs significantly across patients, but is relatively con- utilizes both our transcriptomic and chromatin single-cell data to
served across subpopulations within patients. (Fig. 2d). link putative regulator peaks to target genes. We used our matched
To compare the leukemic programs of the MPAL hematopoietic scATAC-seq and scRNA-seq data for all MPALs and concordant
compartments to previous studies, we downsampled bulk leuke- hematopoietic maps, and aligned each cell into a common sub-
mia RNA-seq and projected onto our transcriptomic hematopoi- space using canonical correlation analyses (CCA)10,11,37,38. For each
etic UMAP for childhood AMLs, B acute lymphoblastic leukemias scATAC-seq cell, we identified the nearest scRNA-seq neighbor
(B-ALLs), early T cell precursor T acute lymphoblastic leukemias (Fig. 3b and Supplementary Fig. 11a,b). We found that the map-
(ETP T-ALLs), non-ETP T-ALLs and MPALs16 (Supplementary ping of scATAC-seq cell clusters to scRNA-defined cell clusters
Fig. 10a,b). We calculated differential expression with respect was highly consistent (single-cell overlap of 52% across 26 clusters;
to the closest normal cell populations to identify their respective Supplementary Fig. 12a–d). We then aggregated our scATAC-seq
leukemic programs. Next, we performed LSI on variable malig- cells on the basis of nearest neighbors in the LSI subspace using
nant genes across all the leukemia subtypes, including MPAL1– Cicero14 and created a corresponding scRNA-seq aggregate for each
MPAL5, and then visualized these patients with UMAP (Fig. 2e cluster using the constructed CCA alignment. We next identified
and Supplementary Fig. 10c,d). Interestingly, we found large differ- 91,601 peak-to-gene links by correlating accessibility changes of
ences in the leukemic programs across various leukemias includ- ATAC peaks within 250 kb of the gene promoter with the expres-
ing T-ALLs and B-ALLs, as well as across different cytogenetic sion of the gene independently for both healthy and MPAL aggre-
subtypes. In addition, we found that the MPALs assayed in this gates (Fig. 3b and Supplementary Table 5). This analysis revealed
study were representative of previously characterized MPALs16 peak-to-gene links that were specific to healthy hematopoiesis, oth-
(Fig. 2e). Given that we were insufficiently powered to detect unique ers that were specific to MPALs and a conserved subset that was
leukemic differences between AML and our MPAL samples when shared across both hematopoiesis and MPALs. We hypothesize that
analyzing downsampled bulk data, we compared the malignant the MPAL-specific peak-to-gene links may be important for leu-
transcriptomic profiles identified from reanalyzed AML scRNA- kemic gene regulation. Overall, the identified set of peak-to-gene
seq data18 with our MPALs to dissect further these unique malig- links had similar distributions for peaks mapped per gene, genes
nant signatures (Fig. 2c and Supplementary Fig. 7c). To this end, we mapped per peak, number of skipped genes and the peak-to-gene as
identified genes that were more commonly universally upregulated previously observed in a similar linkage analyses2 (Supplementary
in AMLs or in MPALs, or jointly upregulated in both leukemias Fig. 12e). To further support these peak-to-gene links, we used pre-
(Fig. 2f, Supplementary Fig. 7c and Supplementary Table 4). These viously published H3K27ac HiChIP in primary T cells and a human
gene sets provide fine-grained phenotypic resolution for comparing coronary artery smooth muscle (HCASM) cell line and found that
the differences and similarities between AML and MPAL leukemic the T/NK-biased peak-to-gene links were more enriched in T cells
programs and suggest possible insight into why MPALs respond than the HCASM cell line39 (Supplementary Fig. 12f). We next
poorly to AML treatment27,28. examined GTEx expression quantitative trait locus (eQTL) map-
Having compared our leukemic transcriptomic programs to pings within our inferred peak-to-gene links, finding enrichment
other studies we wanted to identify the key TFs that regulate these of eQTLs in several functionally related categories such as whole
Fig. 2 | Multiomic projection of MPALs into hematopoiesis identifies normal and leukemic programs. a, Schematic for projection of MPAL single cells
onto hematopoiesis for both scRNA-seq and scATAC-seq classified into broad hematopoietic compartments. b, Left, MPAL single-cell projections
into hematopoiesis for both scRNA-seq and scATAC-seq. Right, the proportion of MPAL cells that were broadly classified as healthy or disease and
their respective hematopoietic compartment (range is from 0 to 1). c, Left, scRNA-seq heat map of upregulated genes (LFC > 0.5 and two-sided t test
FDR < 0.01) log 2 (fold changes) comparing MPAL disease subpopulations to closest non-redundant normal cells. Differential genes were clustered using
k-means clustering (k = 10) on the basis of their log 2 (fold changes). Right, scATAC-seq heat map (ordered by scRNA-seq hierarchal clustering on the left)
of differentially upregulated accessible peaks (LFC > 0.5 and two-sided t test FDR < 0.01) log 2 (fold changes) comparing MPAL disease subpopulations
to the closest non-redundant normal cells. Differential peaks were clustered using k-means clustering (k = 10) on the basis of their log 2 (fold changes).
d, Pearson correlation of the log(fold changes) (from c) for differentially upregulated genes and peaks across all MPAL subpopulations. e, LSI UMAP of
2
differentially upregulated gene-expression profiles across bulk leukemias16 (circle, n = 321) and MPAL samples assayed in this study (outlined triangle,
n = 17), colored by WHO 2016 classifications5. f, Left, MA plot (log-ratio (M) by mean average (A)) comparing the proportion of malignant (upregulated)
gene-expression profiles in AML and MPALs. The x axis represents, for each upregulated gene, the average proportion of subpopulations from patients
with AML and MPAL that are broadly upregulated (LFC > 0.5). The y axis represents, for each upregulated gene, the difference in the proportion of
upregulated subpopulations from patients with MPAL and AML (LFC > 0.5). Right, genes that are more malignantly biased to either AMLs or MPALs and
genes that are conserved across both AMLs and MPALs.
NAtuRE BiotECHNoLoGY | VOL 37 | DECEMBER 2019 | 1458–1465 | www.nature.com/naturebiotechnology 1461
Letters NATUre BIoTechNology
blood and lymphocytes (Supplementary Fig. 12g). To demonstrate FLT3 and apoptosis regulator MCL1 (Supplementary Fig. 13a–d).
the utility of these peak-to-gene links, we linked differentially acces- Overall, these analyses, show that the peak-to-gene links are highly
sible regions to known leukemic genes such as the surface protein enriched in immune regulation and across other previously pub-
CD96, the leukemic stem cell marker IL1RAP, the cytokine receptor lished linkage datasets2,39.
a MPAL single cells
CITE-seq scATAC-seq
b scRNA scATAC
1LAPM
2LAPM
3LAPM
4LAPM
5LAPM
R5LAPM
+ scRNA AAAAAA (logFC) AAAAAA 2
AAAAAA
–1 1 scATAC
(logFC) 2 –1.5 1.5
MPAL LSI projection ANRcs CATAcs Donor MPAL1
MPAL2
MPAL3
MPAL4
MPAL5
MPAL5R
Classification Erythroid-like Lymphoid-like
Myeloid-like
Progenitor-like
T/NK-like Healthy-like
UMAP dimension 1
2
noisnemid
PAMU
Differential scRNA versus closest normal
Differential scATAC versus closest normal
B HSC Basophil Erythroid Erythroid HSCCLP CLP NK CD8M B NK Basophil Plasma CD4M pDC CD8M
Neutrophil pDC GMP Plasma CD4M GMP CD4N CD8N
CD4N
CD8N
Monocytes Monocytes
n = 1,735 n = 7,326
n = 5,885 n = 8,255
n = 835 n = 4,195
n = 3,487 n = 6,569
UMAP dimension 1
n = 4,161 n = 4,127
n = 1,953 n = 4,951
2
noisnemid
PAMU
c
4,616 genes 72,196 peaks
d scRNA/scATAC e
Differential correlation
0 >0.8
B-ALL MPAL B/M AML
T-ALL MPAL T/M Bulk leukemia (16)
ETP MPAL others MPAL1-5R
Average proportion malignant (PMPAL+ PAML)/2
)LMAP
–LAPMP(
tnangilam
noitroporp
ni ecnereffiD
f
Conserved
CDKN2A CCND3 DUSP6
CD96 IL3RA IRF9 CCNA1 HLA-A CASP3
NFE2 IFTI2/3 TNF
FLT3 RASGRP3 TNFSF4
ANR
C C C PI C D D K N K 9 3 6 1 A C 1 1 A A/B 4 C C S I P L T T C D 1 A G R N 9 T 6 E A A 3 R P 1 4
3 C ST D A K T N 3 2A R C U D N 82 X1
IL1RAP CDK6 LSI projection LSI projection PTGER4 CASP3 CD82 10 STAT5A
10 2 S K A G K T N C S C C L C A C T R N L T F D A D D N A A F X A F A K S K 3 7 A T T 6 T 1 7 D S R P 6 1 5 6 C 5 3 D A 3 28 3 P K C F I A G K C T N C L C F A O C R R N L D D F D D N I6 F X A F K A S K 3 K 3 7 A 6 T 1 7 4 D C S B R 1 1 C 1 5 B D A 3 2 / 8 B PDLIM1 PDLIM1
MMP9 MMP9 9 G CK A B DD45A 6 C G M K A L B L D T D 1 4 1 5A KDM5B ITM2A MLLT11 LEF1
ITM2A 5 M SP A T R B C N K 1 SL1
LEF1 CCR9
1 M SP A T R B C N K 1 SL1 BCL2A1
CCR9 KMD6A
6 S B H T C L A A L T 2 -D 1 A R 1 B5 2 M PD E E F 7 2 A C IL1B CD40 KMD6A MACC1
RUNX1 HLA-DRB5
PRKCB STAT1
4 C FO D S 34 B 7 IL1B
LY6E ACY3
IFI6 CDC42
TMBIM6 GGT5
PIM1 PIK3CA
7 P C P LA 4 I D M H M 2 1 B 0 P 0 1 9 T M C P C M I D D C M B K 7 L 1 9 I 1 N M A 2 6 A
5 C G SN D N X 7 A 2 2 12 1 C G SN D N X 7 A 2 2 12
S FO PR X Y O 2 1 S FO PR X Y O 2 1
8 M FL C T L 3 1 8 F R C L C D T S 2 3 0 D 0 1 MYC PLD1
PLD1 PROM1
ATAC
gniretsulc
snaem-k
gniretsulc
snaem-k
Nearest genes
MPAL versus AML malignant comparison
1.0
MPAL biased
IL1RAP CD3D TCF7
CD69 PTGER4 TSPAN7
ATF3 RUNX1 CCL3
0.5
CLEC11A ICAM4 KLF6
0
−0.5 AML biased
STAT5A HLA-DRB5 MYC
IL2RA HOXA9 LGALS3
NR2F6 CEBPA IL1B
ZBTB7A HLX HOXA10
−1.0
0 0.25 0.50 0.75
Proportion
of
MPAL
single
cells
Donor Donor Classification Classification
T-ALL
MPAL
AML
T-like
B-ALL
B-like
1462 NAtuRE BiotECHNoLoGY | VOL 37 | DECEMBER 2019 | 1458–1465 | www.nature.com/naturebiotechnology
NATUre BIoTechNology Letters
a
scATAC-seq scRNA-seq
Heme ATAC-seq Heme RNA-seqMPAL ATAC-seqMPAL RNA-seq
(1) Convert
accessibility to
gene scores
with Cicero
(2) Align subspaces
with Seurat CCA
(3) Identify nearest
neighbors in CCA
scATAC to
scRNA-seq
91,601 significant peak-to-gene links
c
Having established a high-quality set of peak-to-gene links, we subpopulations. Next, we selected all linked differential accessibility
aimed to identify the set of malignant genes putatively regulated by sites that contain the RUNX1 motif. Finally, for each linked gene
RUNX1. First, we utilized our peak-to-gene links to identify differ- we combined all linked peaks to create a differential linkage score
ential peaks linked to a differential gene within at least two MPAL (Methods) and compared this score to the proportion of MPAL
yhtlaeH
LAPM
derahS
)598,15
=
n(
)540,03
=
n(
)093,9
= n(
ATAC z score RNA z score
–2 2 –2 2
Inferring TF malignant regulation
(1) Identify differential (2) Identify TF binding
linked motifs within linked
peaks and genes differential peaks
RUNX1 putative targets (n = 732)
Proportion of MPAL subpopulations differential
erocs
egaknil laitnereffiD
Strata (n = 179 donors)
RUNX1 targets high 33%
RUNX1 targets low 33%
Low High
snoitalupopbuS
(3) Identify which subpopulations
have at least 1 differentially
linked peak-to-gene
Differential peaks ∑
All peaks 1 1 0 1 0 1
0 0 1 0 1 1
0 0 1 0 0 0
1 1 0 1 1 1
1 0 1 1 1 1
0 0 1 0 0 0
)3102(
LMA
AGCT
ytilibaborp lavivruS
atartS
chr12:9,746,789−10,146,789
100
Motif hypergeometric Donor Classifications 75
–log 10 (FDR) MPAL1 MPAL4 Erythroid-like Progenitor-like 50
MPAL2 MPAL5 Lymphoid-like T/NK-like 25
6
0 100 MPAL3 MPAL5R Myeloid-like
llec
T
ca72K3H
SIE
.mron
PIhCiH
100 kb
scRNA (log2Exp.)
0 24
HL60 RUNX1 MPAL ChIP-seq Healthy closest normal
Peak-to-gene links
RUNX1 malignant peak-to-gene
links
Strand
CD69 −
+
**
**
**
**
**
**
**
**
**
**
**
**
**
**
** **
**
b
(4) Link distal
ATAC-seq peaks
to putative target
genes
(5) Identify
significant
peak-to-gene
links
–250 kb 250 kb
e
d f
1LAPM
2LAPM
3LAPM
4LAPM
5LAPM
R5LAPM
Motif enrichment in k-means differential ATAC-seq peaks
RUNX1
FLI1
KLF6
EGR1
MECP2
KLF2
WT1
ZFY
ETV6
ETV3
FEV
ERG
ETS2
ELF1
ATF6
EGR3
TFDP2
HES4
XBP1
KLF13
ZNF281
KLF7
SMARCC1
FOSL1
JUNB
FOS
JUN
BACH1
NFE2
FOSB
ATF3
4 10 3 6 5 2 7 9 1 8
0 0.25 0.5 0.75
8 SLC37A1 1.00
ZBTB16 ++ +
APBA2 +
0.75
6
SLC16A3
++
+ ST3GAL4 + +
4 KLF2 GRA B P C 2 L11B CD44 CD69 0.50 + + + +++ + ++++ ++ DFFB CD7 KLF6 + + 2 GLU P L XDN CD2 FO G S NA1 A 5 TF3 PDE3B 0.25 P = 0.023 +++ ++ ++ +
LAPTM5 MIR181A1HG 0
IFITM2 DUSP10
0 RAB8A 56 14 5 56 5 0
0 0.25 0.50 0.75 1.00
0 1,000 2,000
)301×(
skaep
fo
rebmuN
10 Proportion of upregulated
5 RNA across MPAL
hematopoietic compartments
0
k-means ATAC-seq differential to closest normal
sFT
Healthy-like
Correlation (r)
peak-to-gene
0.35 1.00
Jurkat CRISPRa E1 E2 E3 KLRF
NAtuRE BiotECHNoLoGY | VOL 37 | DECEMBER 2019 | 1458–1465 | www.nature.com/naturebiotechnology 1463
Letters NATUre BIoTechNology
Fig. 3 | integrative scAtAC-seq and scRNA-seq analyses nominate putative tFs that regulate leukemic programs. a, Top, number of accessible peaks in
each k-means cluster. Bottom left, hypergeometric TF motif enrichment FDR in differentially accessible peaks across each k-means cluster identified in
Fig. 2c. TFs are also identified as being differentially expressed and enriched in at least three MPAL hematopoietic compartments. Bottom right, proportion
of differentially upregulated TF gene-expression profiles across MPAL hematopoietic compartments. b, Left, schematic for alignment of scATAC-seq and
scRNA-seq data to link putative regulatory regions to target genes. First, scATAC-seq data are converted from accessible peaks to inferred gene-activity
scores using Cicero. Second, these gene activity scores and scRNA-seq expression are aligned into a common subspace using Seurat’s CCA. Third, each
scATAC-seq cell is assigned its nearest scRNA-seq neighbor. Fourth, ATAC-seq peaks within 2.5–250 kb of a gene promoter are correlated within the
healthy hematopoietic and MPAL k-neaest-neighbor groupings. Lastly, significant peak-to-gene links are identified by correlating peaks to genes on
different chromosomes. Right, heat maps of 91,601 peak-to-gene links across hematopoiesis and MPALs. Top, peak-to-gene links that are identified only
within hematopoiesis. Middle, peak-to-gene links that are unique to MPALs. Bottom, peak-to-gene links identified in both hematopoiesis and MPALs.
c, Schematic for identifying genes that are putatively regulated by the TF of interest. d, Putative RUNX1-target genes (n = 732) differentially upregulated
in at least one MPAL subpopulation. The x axis represents the proportion of MPAL subpopulations that are differential in both scRNA-seq and a linked
accessible peak. The y axis represents the cumulative linkage score between differentially upregulated peaks linked to differentially upregulated genes.
e, CD69 multiomic differential track. Top, T cell T helper 17 H3K27ac HiChIP virtual 4C of enhancer interaction signal (EIS) of the CD69 locus, the line
represents the average signal and shading represents the range of the signal times p2 between biological replicates (n = 2). Middle, aggregated scATAC-
I
seq tracks showing MPAL disease subpopulations (red) and aggregated nearest-neighbor healthy (gray). Right, violin plots of the distribution log2
ffiffiffi
normalized expression of CD69 for MPAL disease subpopulations (red) and closest normal cells (gray); the black line represents the mean and asterisks
denote significance (LFC > 0.5 and FDR < 0.01 from Fig. 2c). Violin plot of the log 2 -normalized expression and the black line represents the mean log 2 -
normalized expression. Bottom, HL60 AML line ChIP-seq data across the CD69 locus, CD69 peak-to-gene links, RUNX1-identified malignant peak-to-gene
links for CD69 and jurkat CRISPR activation of three CD69 enhancers39 (E1–E3 are shown in green and the KLRF locus negative control is shown in red).
Peak-to-gene links are colored by Pearson correlation of the peak accessibility and gene expression (Methods). f, Kaplan–Meier curve for patients with
AML from TCGA (n = 179) stratified by putative RUNX1-target genes (n = 732); top 33% versus bottom 33%, average z score log 2 (expression) (log-rank
test P = 0.023).
subpopulations that exhibited differential expression and accessibil- online content
ity in at least one linked peak and target gene (a measure of how Any methods, additional references, Nature Research reporting
common this RUNX1-driven dysfunction is across MPAL subsets) summaries, source data, extended data, supplementary informa-
(Fig. 3c). Using this approach, we found 732 genes putatively regu- tion, acknowledgements, peer review information; details of author
lated by a RUNX1-containing distal element in at least two MPAL contributions and competing interests; and statements of data and
subsets, and found that CD69, which is implicated in lymphocyte code availability are available at https://doi.org/10.1038/s41587-
activation through initiation of JAK–STAT signaling40 and lym- 019-0332-7.
phocyte retention in lymphoid organs41, was both highly enriched
in the calculated differential linkage score and was observed to be Received: 30 April 2019; Accepted: 29 October 2019;
differentially upregulated in almost every MPAL subpopulation Published online: 2 December 2019
(Fig. 3d and Supplementary Table 5). To further support the pre-
dicted RUNX1 regulation of CD69 (refs. 42,43), we incorporated
References
T cell H3K27ac HiChIP39, CRISPR-activation-validated CD69
1. Hoadley, K. A. et al. Cell-of-origin patterns dominate the molecular
enhancers39,44 and RUNX1 ChIP-seq45 into our multiomic differ-
classification of 10,000 tumors from 33 types of cancer. Cell 173,
ential track. These orthogonal datasets support RUNX1 binding 291–304 (2018).
to these linked distal regulatory regions (Fig. 3e). Finally, by using 2. Corces, M. R et al. The chromatin accessibility landscape of primary human
the 732 identified RUNX1-target genes to stratify patients with cancers. Science 362, eaav1898 (2018).
AML from The Cancer Genome Atlas (TCGA)46 by expression, we 3. Polak, P. et al. Cell-of-origin chromatin organization shapes the mutational
landscape of cancer. Nature 518, 360–364 (2015).
observed significantly decreased survival (P = 0.023) in donors with 4. Weinberg, O. K. & Arber, D. A. Mixed-phenotype acute leukemia: historical
a high RUNX1-target-gene signature46 (Fig. 3f). This analysis sug- overview and a new definition. Leukemia 24, 1844–1851 (2010).
gests that RUNX1 is an important TF that putatively upregulates a 5. Arber, D. A. et al. The 2016 revision to the World Health Organization
portion of the leukemic signature in MPAL and potentially AML. classification of myeloid neoplasms and acute leukemia. Blood 127,
2391–2405 (2016).
Collectively, this work establishes an experimental and analyti-
6. Stoeckius, M. et al. Simultaneous epitope and transcriptome measurement in
cal approach for deconstructing cancer-specific features using inte-
single cells. Nat. Methods 14, 865–868 (2017).
grative analysis of multiple single-cell technologies. We find that 7. Satpathy, A. T. et al. Massively parallel single-cell chromatin landscapes
MPAL malignant programs are largely conserved across pheno- of human immune cell development and intratumoral T cell exhaustion.
typically heterogenous cells within individual patients; this obser- Nat. Biotechnol. 37, 925–936 (2019).
8. Zheng, G. X. Y. et al. Massively parallel digital transcriptional profiling of
vation is consistent with a previous report16 that MPAL cells likely
single cells. Nat. Commun. 8, 14049 (2017).
originate from a multipotent progenitor cell, thereby sharing a com-
9. Cusanovich, D. A. et al. The cis-regulatory dynamics of embryonic
mon mutational landscape while populating different regions of development at single-cell resolution. Nature 555, 538–542 (2018).
the hematopoietic tree. We used integrative single-cell analyses to 10. Cusanovich, D. A. et al. A single-cell atlas of in vivo mammalian chromatin
further define putative TF regulation of these malignant programs. accessibility. Cell 174, 1309–1324 (2018).
11. Butler, A., Hoffman, P., Smibert, P., Papalexi, E. & Satija, R. Integrating
We inferred that RUNX1 acts as a potential oncogene in MPAL, reg-
single-cell transcriptomic data across different conditions, technologies, and
ulating malignant genes associated with poor survival. We antici- species. Nat. Biotechnol. 36, 411–420 (2018).
pate that similar approaches will be used in future studies to both 12. McInnes, L., Healy, J. & Melville, J. UMAP: Uniform manifold approximation
identify the differentiation status of different tumor types (that is, and projection for dimension reduction. Preprint at arXiv https://arxiv.org/
identify the closest normal cell type) and enable molecular dissec- abs/1802.03426 (2018).
13. Janeway, C. J., Travers, P., Walport, M. & Shlomchik, M. J. Immunobiology 5th
tion of molecular dysfunction in pathogenic cellular subtypes, with
edn (Garland Science, 2001).
the ultimate goal of identifying personalized therapeutic targets 14. Pliner, H. A. et al. Cicero predicts cis-regulatory DNA interactions from
through integrative single-cell molecular characterization. single-cell chromatin accessibility data. Mol. Cell 71, 858–871 (2018).
1464 NAtuRE BiotECHNoLoGY | VOL 37 | DECEMBER 2019 | 1458–1465 | www.nature.com/naturebiotechnology
NATUre BIoTechNology Letters
15. Schep, A. N., Wu, B., Buenrostro, J. D. & Greenleaf, W. J. chromVAR: 33. Wang, X et al. Breast tumors educate the proteome of stromal tissue
inferring transcription-factor-associated accessibility from single-cell in an individualized but coordinated manner. Sci. Signal. 10,
epigenomic data. Nat. Methods 14, 975–978 (2017). eaam8065 (2017).
16. Alexander, T. B. et al. The genetic basis and cell of origin of mixed phenotype 34. Sanda, T. et al. Core transcriptional regulatory circuit controlled by the TAL1
acute leukaemia. Nature 562, 373–379 (2018). complex in human T cell acute lymphoblastic leukemia. Cancer Cell 22,
17. Takahashi, K. et al. Integrative genomic analysis of adult mixed 209–221 (2012).
phenotype acute leukemia delineates lineage associated molecular subtypes. 35. Ben-Ami, O. et al. Addiction of t(8;21) and inv(16) acute myeloid leukemia
Nat. Commun. 9, 2670 (2018). to native RUNX1. Cell Rep. 4, 1131–1143 (2013).
18. Corces, M. R. et al. Lineage-specific and single-cell chromatin accessibility 36. Wilkinson, A. C. et al. RUNX1 is a key target in t(4;11) leukemias that
charts human hematopoiesis and leukemia evolution. Nat. Genet. 48, contributes to gene activation through an AF4–MLL complex interaction.
1193–1203 (2016). Cell Rep. 3, 116–127 (2013).
19. van Galen, P. et al. Single-cell RNA-seq reveals AML hierarchies relevant to 37. Stuart, T. et al. Comprehensive integration of single-cell data. Cell 177,
disease progression and immunity. Cell 176, 1265–1281 (2019). 1888–1902 (2019).
20. Satpathy, A. T. et al. Transcript-indexed ATAC-seq for precision immune 38. Welch, J. D. et al. Single-cell multi-omic integration compares and contrasts
profiling. Nat. Med. 24, 580–590 (2018). features of brain cell identity. Cell 177, 1873–1887 (2019).
21. Mezger, A. et al. High-throughput chromatin accessibility profiling at 39. Mumbach, M. R. et al. Enhancer connectome in primary human cells
single-cell resolution. Nat. Commun. 9, 3647 (2018). identifies target genes of disease-associated DNA elements. Nat. Genet. 49,
22. Buenrostro, J. D. et al. Integrated single-cell analysis maps the continuous 1602–1612 (2017).
regulatory landscape of human hematopoietic differentiation. Cell 173, 40. Martín, P. et al. CD69 association with Jak3/Stat5 proteins regulates Th17 cell
1535–1548 (2018). differentiation. Mol. Cell. Biol. 30, 4877–4889 (2010).
23. Li, B. et al. Census of immune cells. HCA https://data.humancellatlas.org/ 41. Shiow, L. R. et al. CD69 acts downstream of interferon-α/β to inhibit
explore/projects/cc95ff89-2e68-4a08-a234-480eca21ce79 (2018). S1P1 and lymphocyte egress from lymphoid organs. Nature 440,
24. Mitchell, K. et al. IL1RAP potentiates multiple oncogenic signaling pathways 540–544 (2006).
in AML. J. Exp. Med. 215, 1709–1727 (2018). 42. Egawa, T., Tillman, R. E., Naoe, Y., Taniuchi, I. & Littman, D. R. The role of
25. Yu, G., Wang, L.-G., Han, Y. & He, Q.-Y. clusterProfiler: an R package for the Runx transcription factors in thymocyte differentiation and in
comparing biological themes among gene clusters. OMICS 16, 284–287 (2012). homeostasis of naive T cells. J. Exp. Med. 204, 1945–1957 (2007).
26. Lim, S. & Kaldis, P. Cdks, cyclins and CKIs: roles beyond cell cycle 43. Laguna, T. et al. New insights on the transcriptional regulation of CD69 gene
regulation. Development 140, 3079–3093 (2013). through a potent enhancer located in the conserved non-coding sequence 2.
27. Wolach, O. & Stone, R. M. How I treat mixed-phenotype acute leukemia. Mol. Immunol. 66, 171–179 (2015).
Blood 125, 2477–2485 (2015). 44. Simeonov, D. R. et al. Discovery of stimulation-responsive immune enhancers
28. Zheng, C. et al. What is the optimal treatment for biphenotypic acute with CRISPR activation. Nature 549, 111–115 (2017).
leukemia? Haematologica 94, 1778–1780 (2009). 45. Feld, C. et al. Combined cistrome and transcriptome analysis of SKI in AML
29. Osato, M. et al. Biallelic and heterozygous point mutations in the runt cells identifies SKI as a co-repressor for RUNX1. Nucleic Acids Res. 46,
domain of the AML1/PEBP2αB gene associated with myeloblastic leukemias. 3412–3428 (2018).
Blood 93, 1817–1824 (1999). 46. Cancer Genome Atlas Research Network Genomic and epigenomic
30. Haferlach, T. et al. Landscape of genetic lesions in 944 patients with landscapes of adult de novo acute myeloid leukemia. N. Engl. J. Med. 368,
myelodysplastic syndromes. Leukemia 28, 241–247 (2014). 2059–2074 (2013).
31. Zhang, J. et al. The genetic basis of early T-cell precursor acute lymphoblastic
leukaemia. Nature 481, 157–163 (2012).
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
32. Della Gatta, G. et al. Reverse engineering of TLX oncogenic transcriptional
published maps and institutional affiliations.
networks identifies RUNX1 as tumor suppressor in T-ALL. Nat. Med. 18,
436–440 (2012). © The Author(s), under exclusive licence to Springer Nature America, Inc. 2019
NAtuRE BiotECHNoLoGY | VOL 37 | DECEMBER 2019 | 1458–1465 | www.nature.com/naturebiotechnology 1465
Letters NATUre BIoTechNology
Methods scATAC-seq. scATAC-seq processing. Raw sequencing data were converted to fastq
Experimental methods. Description of healthy donors. PBMCs, BMMCs and format using cellranger atac mkfastq (10x Genomics, v.1.0.0; Supplementary
CD34+ bone marrow cells were obtained from healthy donors with informed Fig. 14). scRNA-seq reads were aligned to the GRCh37 (hg19) reference genome
consent and compliance with relevant ethical regulations (AllCells). Individual and quantified using cellranger count (10x Genomics, v.1.0.0).
information for each donor is provided in Supplementary Table 1. All healthy
cells used in this study were cryopreserved (fresh frozen in either Bambanker scATAC-seq quality control. To ensure that each cell was both adequately sequenced
freezing medium or 10% DMSO with 90% serum). Thawed cells were not filtered and had a high signal-to-background ratio, we filtered cells with less than 1,000
for viability before loading into droplets. High-quality cells were identified unique fragments and enrichment at TSSs below 8. To calculate TSS enrichment2,
bioinformatically. genome-wide Tn5-corrected insertions were aggregated ±2,000 bp relative
(TSS-strand-corrected) to each unique TSS. This profile was normalized to the
Description of patients and donors with leukemia. Patient samples were collected mean accessibility ±1,900–2,000 bp from the TSS, smoothed every 51 bp and the
with informed consent in accordance with all relevant ethical regulations regarding maximum smoothed value was reported as TSS enrichment in R. We estimate that
human research participants under a protocol approved by the Institutional Review the multiplet percentage for this study was around 4% (ref. 7).
Board (IRB) at Stanford University Medical Center (Stanford IRB, 42949, 18329
and 6453). Peripheral blood and bone marrow aspirate samples were processed scATAC-seq counts matrix. To construct a counts matrix for each cell by each
by Lymphoprep (STEMCELL Technologies) gradient centrifugation and fresh feature (window or peaks), we read each fragment.tsv.gz fill into a GenomicRanges
frozen in Bambanker medium. Diagnostic flow cytometry performed on bone object. For each Tn5 insertion, which can be thought of as the ‘start’ and ‘end’ of
marrow aspirate samples were analyzed. In all cases, a retrospective review of the ATAC fragments, we used findOverlaps to find all overlaps with the feature by
clinical parameters, hemogram data, peripheral blood smears, bone marrow insertions. Then we added a column with the unique id (integer) cell barcode to
aspirates, trephine biopsies, results of karyotype and flow cytometry studies was the overlaps object and fed this into a sparseMatrix in R. To calculate the fraction
performed. Clinical follow-up information was obtained by retrospective review of of reads/insertions in peaks, we used the colSums of the sparseMatrix and divided
the medical record charts. Cases were classified using the 2016 WHO classification it by the number of insertions for each cell id barcode using table in R.
of hematopoietic and lymphoid neoplasms5. Thawed cells were not filtered for
viability before loading into droplet assays. High-quality cells were identified scATAC-seq union peak set from latent semantic index clustering. We adapted a
bioinformatically. previous workflow for generating a union peak set that will account for diverse
subpopulation structure2,9,10 (Supplementary Fig. 14). First, we created 2.5-kb
Combined single-cell antibody-derived tag and RNA sequencing. CITE-seq windows genome wide using ‘tile(hg19chromSizes, width = 2500)’ in R. Next, a
was performed as previously reported6 using the (version 2) Chromium cell-by-2.5-kb-window sparse matrix was constructed as described above. The top
Single Cell 3′ Library and Gel Bead kit (10x Genomics, 120237). Six thousand 20,000 accessible windows were kept and the binarized matrix was transformed
cells were targeted for each sample. Oligonucleotide-coupled antibodies were with the term frequency-inverse document frequency (TF-IDF) transformation8.
obtained from Biolegend, indexed by PCR (ten cycles) with custom barcodes In brief, we divided each index by the colSums of the matrix to compute the
(see Supplementary Table 3), quantified by PCR using a PhiX Control v3 cell ‘term frequency’. Next, we multiplied these values by log(1 + ncol(matrix)/
(Illumina, FC-110-3001) standard curve and sequenced on an Illumina rowSums(matrix)), which represents the ‘inverse document frequency’. This
NextSeq 550 together with scRNA-seq at no more than 60% of the total library normalization resulted in a TF-IDF matrix that was then used as input to the irlba
composition (1.5 pM loading concentration, 26 × 8 × 0 × 98 base pair (bp) singular value decomposition (SVD) implementation in R. The 2nd to 25th SVD
read configuration). dimensions (1st dimension is correlated with the depth of cell reads15) were used
for creating a Seurat object and initial clustering was performed using Seurat’s
Single-cell assay for transposase-accessible chromatin using sequencing. scATAC-seq SNN graph clustering (v.2.3.4) with ‘FindClusters’ at a default resolution of 0.8. If
targeting 4,000 cells per sample was performed using a beta version of Chromium the minimum cluster size was below 200 cells, the resolution was decreased until
Single Cell ATAC Library and Gel Bead kit (10x Genomics, 1000110). Each sample this criterion was reached leading to a final resolution of 0.8N (where N represents
library was uniquely barcoded and quantified by PCR using a PhiX Control v3 the iterations until the minimum cluster size is 200 cells). For each cluster, peak
(Illumina, FC-110-3001) standard curve. Libraries were then pooled and loaded on calling was performed on Tn5-corrected insertions (each end of the Tn5-corrected
a NextSeq 550 Illumina sequencer (1.4 pM loading concentration, 33 × 8 × 16 × 33 fragments) using the MACS2 callpeak command with parameters ‘--shift -75
bp read configuration) and sequenced to either 90% saturation or 30,000 unique --extsize 150 --nomodel --call-summits --nolambda --keep-dup all -q 0.05’. The
reads per cell on average. peak summits were then extended by 250 bp on either side to a final width of
501 bp, filtered by the ENCODE hg19 blacklist (https://www.encodeproject.org/
Whole-exome sequencing of patients and donors with leukemia. Genomic DNA annotations/ENCSR636HFF/) and filtered to remove peaks that extend beyond the
was extracted from diagnostic PBMCs or bone marrow samples using the Zymo ends of chromosomes.
Clean and Concentrator kit. Library construction (Agilent SureSelect Human All Overlapping peaks called were handled using an iterative removal procedure
Exon kit), quality assessment and 150-bp paired-end sequencing (HiSeq4000) were as previously described2. First, the most significant (MACS2 score) extended peak
performed by Novogene. Reads with adaptor contamination, uncertain nucleotides summit is kept and any peak that directly overlaps with that significant peak is
and paired reads with >50% low-quality nucleotides were discarded. Paired-end removed. This process reiterates to the next most significant peak until all peaks
reads were then aligned to the reference genome (GRCh37) using BWA software. have either been kept or removed owing to direct overlap with a more significant
Genome Analysis Toolkit (GATK) was used to ignore duplicates with Picard-tool. peak. The most significant 200,000 extended peak summits for each cluster were
Filtered variants (single-nucleotide polymorphisms and indels) were identified quantile normalized using ‘trunc(rank(v))/length(v)’ in R (where v represents the
using GATK HaplotypeCaller and variantFiltration. Variants obtained from initial vector of MACS2 peaks scores). These cluster peak sets were then merged and
analysis were further compared to dbSNP and the 1,000 Genomes database. Finally, the previous iterative removal procedure was used. Lastly, we removed any peaks
missense, stop–gain and frameshift mutations were compared against a custom whose nucleotide content had any ‘N’ nucleotides and any peaks mapping to chrY.
panel of 300 genes that are recurrently mutated in hematologic malignancies as
described previously16,17. scATAC-seq-centric latent semantic indexing clustering and visualization. scATAC-
seq clustering was performed by adapting the strategy of Cusanovich et. al9,10 to
Analytical methods. Fluorescence-activated cell sorting. Flow cytometry was compute the term TF-IDF transformation. In brief, we divided each index by the
performed on a FACSCalibur or FACSCanto II (Becton Dickinson) cytometer colSums of the matrix to compute the cell ‘term frequency’. Next, we multiplied
using commercially available antibodies (Supplementary Table 2). Lymphocytes these values by log(1 + ncol(matrix)/rowSums(matrix)), which represents the
were identified by low side scatter and bright CD45 expression. The gate was ‘inverse document frequency’. This resulted in a TF-IDF matrix that was used as
validated by backgating on CD3+ or CD19+ events. Blasts were identified by low input to the irlba SVD implementation in R. The first 50 SVD dimensions were
side scatter and dim CD45 expression. The gate was further assessed by backgating used as input into a Seurat object and initial clustering was performed using
on CD34+ events. Gates were drawn by additionally using isotype controls and Seurat’s (v.2.3.4) SNN graph clustering ‘FindClusters’ with a resolution of 1.5 (25
internal positive and negative controls. SVD dimensions for healthy hematopoiesis and 50 for healthy hematopoiesis and
MPALs). We found that in some cases, there was batch effect between experiments.
scADT-seq analysis. Raw sequencing data were converted to fastq format using To minimize this effect, we identified the top 50,000 variable peaks across the
bcl2fastq (Illumina, v.2.20.0.422). ADTs were then assigned to individual cells and initial clusters (summed cell matrix for each cluster followed by edgeR log(counts
antibodies (see reference antibody barcodes in Supplementary Table 3) allowing for per million) (CPM) transformation47). These 50,000 variable peaks were then
two and three barcode mismatches, respectively. Unique molecular counts for each used to subset the sparse binarized accessibility matrix and recompute the TF-IDF
cell and antibody were then generated by counting only barcodes with a unique transform. We used SVD on the TF-IDF matrix to generate a lower-dimensional
molecular identifier (UMI). PBMC and BMMC ADT count data were transformed representation of the data by retaining the first 50 dimensions. We then used these
using the centered log ratio (CLR) as previously described6. PBMCs and BMMCs reduced dimensions as input into a Seurat object and then final clusters were
were visualized in two dimensions using the uwot implementation of UMAP12 in R identified by using Seurat’s (v.2.3.4) SNN graph clustering ‘FindClusters’ with a
(n_neighbors = 50, min_dist = 0.4). resolution of 1.5 (50 SVD dimensions for healthy hematopoiesis and 50 for healthy
NAtuRE BiotECHNoLoGY | www.nature.com/naturebiotechnology
NATUre BIoTechNology Letters
hematopoiesis and MPALs). These same reduced dimensions were used as input clustering (v.2.3.4) with an increased resolution of 0.6. We then summed
to the uwot implementation of UMAP (n_neighbors = 55, n_components = 2, the individual clusters single cells, computed the logCPM transformation,
min_dist = 0.45) and plotted in ggplot2 using R. We merged scATAC-seq clusters ‘edgeR::cpm(mat,log = TRUE,prior.count = 3)’ and identified the top 2,500 variable
from a total of 36 clusters for hematopoiesis to 26 final clusters that best agreed genes across these clusters. We repeated this one more time (resolution 1.0)
with the scRNA-seq clusters. The objective of this analysis is to optimize feature and saved the final features and clusters. To align our clusters better with the
selection, which minimizes batch effects, and enable projection of future data into scATAC-seq data, we merged a total of 26 clusters from 31 initial clusters (included
the same manifold as described further below. in Supplemental Data). These LSI dimensions were used as input to the uwot
implementation of UMAP (n_neighbors = 35, n_components = 2, min_dist = 0.45)
scATAC-seq visualization in genomic regions. To visualize scATAC-seq data, we and plotted in ggplot2 using R. The objective of this analysis is to optimize feature
read the fragments into a GenomicRanges object in R. We then computed sliding selection, which minimizes batch effects, and enable projection of future data into
windows across each region we wanted to visualize every 100 bp ‘slidingWindow the same manifold as described further below.
s(region,100,100)’. We computed a counts matrix for Tn5-corrected insertions as
described above and then binarized this matrix. We then returned all non-zero scATAC-seq and scRNA-seq analytical methods. Latent semantic indexing
indices (binarization) from the matrix (cell × 100-bp intervals) and plotted them projection for scATAC-seq and scRNA-seq. We designed the above analytical
in ggplot2 in R with ‘geom_tile’. For visualizing aggregate scATAC-seq data, the approach to clustering of single-cell data because it optimized feature selection
binarized matrix above was summed and normalized. Scale factors were computed and enabled projection of new non-normalized data into a low-dimension
by taking the binarized sum in the global peak set and normalizing to 10,000,000. manifold. To enable these analyses, when computing the TF-IDF transformation
Tracks were then plotted in ggplot in R. on the hematopoietic hierarchy, we kept the colSums, rowSums and SVD from
the previous run and then when projecting new data into this subspace, we
chromVAR. We measured global TF activity using chromVAR15. We used the first identified which row indices to zero out on the basis of the initial TF-IDF
cell-by-peaks and the Catalog of Inferred Sequence Binding Preferences (CIS-BP) rowSums. We then computed the ‘term frequency’ by dividing by the colSums
motif (from chromVAR motifs ‘human_pwms_v1’) matches within these peaks in these features. Next, we computed the ‘inverse document frequency’ from
from motifmatchr. We then computed the GC-bias-corrected deviations using the previous TF-IDF transform (diagonal(1 + ncol(mat)/ rowSums(mat))) and
the chromVAR ‘deviations’ function. We then computed the GC-bias-corrected computed the new TF-IDF transform. We projected this TF-IDF matrix into the
deviation scores using the chromVAR ‘deviationScores’ function. SVD subspace that was previously generated. To do this calculation, we computed
the new coordinates by “t(TF_IDF) %*% SVD$u %*% diag(1/SVD$d)”, where
Gene-activity scores using Cicero and co-accessibility. We calculated gene activities TF_IDF is the transformed matrix and SVD is the previous SVD run, using irlba
using the R package Cicero14. In brief, we used the sparse binary cell-by-peaks in R (v.3.5.1). We computed the projected matrix by “SVD$u %*% diag(SVD$D) *
matrix and created a cellDataSet, detectedGenes and estimatedSizeFactors. We t(V)” where V is the projected coordinates above. For projecting bulk RNA-seq,
then created a ‘cicero_cds’ with k = 50 and the ‘reduced_coordinates’ being the we downsampled previously published data to 5,000 reads in genes 100 times and
LSI SVD coordinates (hematopoiesis = 25, hematopoiesis and MPALs = 50). This then made a sparse matrix for projection as single-cell data. For projecting
function returns aggregated accessibility across groupings of cells on the basis of bulk scATAC-seq, we downsampled previously published data to 10,000 reads
nearest-neighbor rules from the R package FNN. We then identified all peak–peak in peaks 100 times and then made a binary sparse matrix for projection as
linkages that were within 250 kb by resizing the peaks to 250 kb and 1 bp and using single-cell data.
‘findOverlaps’ in R. We calculated the Pearson correlation for each unique peak–
peak link and created a connections data.frame where the first column is peak_i, HCA immune census bone marrow projection. We downloaded the HCA bone
the second column is peak_j and the third column is co-accessibility (Pearson marrow immune census data (https://data.humancellatlas.org/explore/projects/
correlation). We created a gene data.frame from the TxDb ‘TxDb.Hsapiens.UCSC. cc95ff89-2e68-4a08-a234-480eca21ce79)23 comprising around 300,000 cells from
hg19.knownGene’ in R, resized each gene from its TSS and created a window eight different donors (filtered for at least 1000 UMI). We used our iterative
±2.5 kb centered at the TSS and annotated the ‘cicero_cds’ using ‘annotate_cds_ LSI approach (resolutions = 0.2, 0.6, 1.0 and 2,500 variable genes; UMAP
by_site’. We then calculated gene activities with ‘build_gene_activity_matrix’ (co- n_neighbors = 75, min_dist = 0.2, metric = “euclidean”) to create a UMAP manifold
access cutoff of 0.35). Lastly we normalized the gene activities by using ‘normalize_ that we could then project our scRNA-seq data onto. We LSI projected our scRNA-
gene_activities’ and the read depth of the cells, log normalized these gene activities seq data onto this subspace and found that our cohort reasonably repopulates the
scores for interpretability by computing log 2 (GA × 1,000,000 + 1), where GA is the hematopoietic manifold created on completely separate donors. This result shows
gene activity score. that our analysis approach is scalable and that our healthy hematopoietic data
reasonably recapitulates the biological diversity along hematopoiesis.
scRNA-seq. scRNA-seq processing. Raw sequencing data were converted to fastq
format using cellranger mkfastq (10x Genomics, v.3.0.0; Supplementary Fig. Classification of AML scRNA-seq. We wanted to evaluate our LSI projection of
14). scRNA-seq reads were aligned to the GRCh37 (hg19) reference genome and abnormal cells into a healthy subspace by using data from van Galen et al.19. We
quantified using cellranger count (10x Genomics, v.3.0.0). We kept genes that were first projected their healthy bone marrow scRNA-seq from a different platform
present in both 10x gene transfer formatfiles v.3.0.0 for hg19 and hg38 (https:// and genome and found remarkable agreement with their classifications and our
support.10xgenomics.com/single-cell-gene-expression/software/release-notes/ independent hematopoietic manifold. We then projected their ‘disease’ cell AML
build). Mitochondrial and ribosomal genes were also filtered before further scRNA-seq into our manifold and found reasonable agreement for more terminal
analysis. Genes remaining after these filtering steps we refer to as ‘informative’ states and less agreement in the ‘hematopoietic stem cell (HSC)’ and ‘progenitor-
genes and enable cross genome comparison. like’ classifications. We reasoned that this difference could be due to defining
discrete populations in a continuous subspace. We then reclassified their AML
scRNA-seq quality control. We wanted to filter out cells whose transcripts were ‘disease’ scRNA-seq by finding the nearest neighbors between their cells in our
lowly captured and first plotted the distribution of genes detected and UMIs for projected SVD subspace and our scRNA-seq data. We grouped our clusters into
all experiments. On the basis of these plots, we chose to filter out cells that had more broad groupings for interpretability (‘Progenitor-like’ is clusters 1–6,
less than 400 informative genes detected and 1,000 UMIs. In addition, to lower ‘GMP-like’ is clusters 7 and 8, ‘cDC-like’ is cluster 10, ‘Monocyte-like’ is clusters
multiplet representation, we filtered cells with above 10,000 UMIs. We estimate 11–13). For differential analyses we compared against their projected scRNA-seq
that the multiplet percentage for this study was around 6% (ref. 8). We then plotted healthy bone marrow to minimize batch differences in the comparison.
the correlation for each replicate experiment and found high reproducibility.
Classification of MPAL single cells with scATAC-seq and scRNA-seq. We wanted
scRNA-seq-centric latent semantic indexing clustering and visualization. We to classify MPAL single cells on the basis of their disease state and hematopoietic
initially tested a few methods for clustering scRNA-seq but settled on an progression. First, we aimed to determine which cells were healthy-like and
approach that enabled us to effectively capture the hematopoietic hierarchy disease-like. To do this analysis, we clustered all of the healthy hematopoietic cells
without substantial alteration of transcript expression (Supplementary Fig. with the MPAL of interest using our LSI workflow as described above (scRNA,
14). We first log normalized the transcript counts by first depth normalizing to 25 principal components (PCs), 1,000 variable genes, and Seurat’s SNN resolution
10,000 and adding a pseudocount before a log transform (log(counts per ten of 0.2, 0.8 and 0.8; scATAC, 25 PCs, 25,000 variable peaks and Seurat’s SNN
2 2
thousand transcripts + 1)). Next, we identified the top 3,000 variable genes and resolution of 0.8 and 0.8). We then defined clusters to be healthy-like if a high
performed the TF-IDF transform on these 3,000 genes. We performed SVD on percentage (>80% for scRNA-seq and >90% for scATAC) of the cells were from
this transformed matrix keeping the first 25 dimensions and used this as input the normal hematopoietic data. MPAL single cells belonging to these clusters were
to Seurat’s SNN clustering (v.2.3.4) with an initial resolution of 0.2. We summed classified as healthy-like and the remaining cells were classified as disease-like. We
the individual clusters single cells and computed the logCPM transformation, note that we did not detect significant copy-number amplifications with scATAC-
‘edgeR::cpm(mat,log = TRUE,prior.count = 3)’, and identified the top 2,500 variable seq using a previously described approach7, and the proportion of cells classified
genes across these initial clusters. These variable genes were used as input for a as disease-like was consistent with flow cytometry and morphological estimations
TF-IDF transform and an SVD was performed on this transformed matrix of the percentage of blast cells (Supplementary Fig. 8b). To accurately characterize
keeping the first 25 dimensions, which were used as input to Seurat’s SNN these MPAL as disease-like by their hematopoietic state, we established
NAtuRE BiotECHNoLoGY | www.nature.com/naturebiotechnology
Letters NATUre BIoTechNology
‘hematopoietic compartments’ across our scRNA-seq and scATAC-seq maps Peak-to-gene linkage. Cicero14 allows us to infer gene-activity scores by linking
that broadly characterized the hematopoietic continuum. The borders for these distally correlated ATAC peaks to the promoter peak. While this measure is
compartments were determined empirically using ‘fhs’ in R, guided by the initial extremely useful, it does not actually mean it is correlated to gene expression. To
clusters and agreement across the scRNA-seq and scATAC-seq classifications. circumvent this limitation, we used our grouped scATAC-seq and grouped linked
After classifying the normal hematopoietic continuum, we then broadly classified scRNA-seq to identify peak-to-gene links. First we log normalized the accessibility
the MPAL disease-like cells on the basis of their projected nearest neighbor in and gene expression with log 2 (counts per 10,000 + 1) and then we resized each of
the UMAP subspace. These classifications were used subsequently in differential the gene GenomicRanges to the start using resize(gr,1,“start”) and then resizing
analyses. We note that this approach identifies a cumulative set of leukemia- the start to a ±250-kb window using ‘resize(gr, 2 * 250000 + 1, “center”)’. We
specific changes relative to similar hematopoietic cells and does not discriminate then overlapped all ATAC-seq peaks using ‘findOverlaps’ to identify all putative
among intermediate changes along a leukemic developmental trajectory. We note peak-to-gene links. We then split the aggregated ATAC and RNA matrices by
that this method of classification is potentially limited as compared to classification whether the majority of the cells were from MPAL or hematopoietic single cells
on the basis common structural variants or mutations. Furthermore, identifying and correlated the peaks and genes for all putative peak-to-gene links. We used
disease cells that are partially transformed may likewise be challenging. a previously described approach for computing a null correlation on the basis of
trans correlations (correlating peaks and genes not on the same chromosome)2.
Identifying differential features with scATAC-seq and scRNA-seq. To identify In brief, for each chromosome, 1,000 peaks not on the same chromosome are
differential features for previously published AML data and MPALs, we identified and correlated to every gene on that chromosome. Each putative peak-
constructed a nearest-neighbor healthy aggregate using the following approach. to-gene correlation is converted into a z score by using the mean and s.d. of the null
First, we used FNN to identify the nearest 25 cells using ‘get.knnx(svdHealthy, trans correlations. These are then converted to P values and adjusted for multiple-
svdProjected, k = 25)’ on the basis of Euclidean distance between the projected hypothesis testing using the Benjamini–Hochberg correction ‘p.adjust’ in R. We
cells and hematopoietic cells in LSI SVD space. For each projected population, we retained links whose correlation (Pearson) was above 0.35 and FDR < 0.1 (the same
used a minimum of 50 and maximum of 500 cells (random sampling) as input. correlation cutoff as co-accessibility in Cicero14) in either MPAL or hematopoietic
Next, we took the unique of all hematopoietic single cells and if this number was aggregations. We then kept all peak-to-gene links that were greater than 2.5 kb in
greater than 1.25 times the number of the projected populations, we took the distance. We identified peak-to-gene links that are only present in hematopoiesis,
nearest 24 cells and repeated this procedure until this criterion was met. Then the MPALs or both. To visualize the peak-to-gene links we plotted all of them as a heat
projected population and non-redundant hematopoietic cells were downsampled map with ComplexHeatmap. To determine the column order we first computed
to an equal number of cells (maximum 500). For scATAC-seq, we binarized principal component analysis for the first 25 principal components using irlba.
the matrix for both the projected populations and hematopoietic matrices. We computed Seurat11 SNN clustering with a resolution of 1 and computed the
Next, we scaled the sparse matrices to 10,000 total counts for scRNA-seq and cluster means. We then computed the order of these clusters using hclust and
5,000 total promoter counts for scATAC-seq (promoter peaks defined as peaks the dissimilarity 1 − R as the distance. Next, we iterated through each cluster and
within 500 bp of TSS from hg19 10x v.3.0.0 gene transfer format file). Next, we performed hclust with the dissimilarity calculations to get a final column order.
computed row-wise two-sided t tests for each feature. We then calculated the FDR The peak-to-gene links were grouped by k-means clustering with 10 input centers,
using p.adjust(method = “fdr”). We then computed the log 2 mean and log 2 (fold 100 iterations and 10 random starts for healthy, disease and the overlapping links.
changes) for each feature. We chose these parameters on the basis of a previous We did this biclustering because it enabled us to plot smaller rasterized chunks of
study comparing analytical methods for differential expression48. For scRNA- the heat map without overwhelming the memory; individual rasterized k-means
seq, differential expression was determined by FDR < 0.01 and absolute log 2 (fold clusters were put together after analysis.
changes) greater than 0.5. For scRNA-seq, differential expression was determined
by FDR < 0.05 and absolute log 2 (fold changes) greater than 0.05. Enrichment of peak-to-gene links in GTEx eQTLs. We adopted a previous approach
To identify differential genes for bulk leukemia RNA-seq, we downsampled for identifying the enrichment of our peak-to-gene links in GTEx eQTL data. In
the gene counts to 10,000 counts randomly for 250 times. We then projected and brief, we downloaded GTEx eQTL data (version 7) from https://gtexportal.org/
used the above framework to resolve differential genes with log 2 (fold change) > 3 home/datasets and the *.signif_variant_gene_pairs.txt.gz files were used. We also
and FDR < 0.01. We then removed genes that were differential in 33% or higher of downloaded gencode v19 (matched to these eQTLs) and identified all gene starts
the normal samples to attempt to capture biased genes. In addition, we removed and the nearest gene starts to each peak and eQTL using ‘distanceToNearest’.
genes differential in 50% or higher of the leukemia samples. This filtering biases We filtered all eQTLs that were further than 250 kb from their predicted gene
our identified malignant genes to those that are variable across the leukemic types to be consistent with our linkage approach. To calculate a conservative overlap
as opposed to conserved across all leukemic types. We then took the average enrichment, we further pruned all eQTL links that were to its nearest gene. We
malignancy for each remaining gene for each leukemic type and used the top 300 then created a null set (n = 250) of peak-to-gene links by randomly selecting distal
variable malignant genes across the leukemic types for the heat map and LSI. For ATAC-seq peak-to-gene links (within 250 kb) that were distance matched to the
computing differential LSI, we binarized each gene as malignant or not for the 300 links tested at a resolution of 5 kb. We then calculated a z score and enrichment for
variable malignant genes and computed the TF-IDF transform followed by SVD each peak-to-gene link set as compared to the null set and calculated an FDR using
(LSI). We then visualized this in two dimensions using the uwot implementation of ‘p.adjust(method = “fdr”)’.
UMAP (50 SVD dimensions, n_neighbors = 50, min_dist = 0.005).
Enrichment of peak-to-gene links in K27ac HiChIP metaV4C. We wanted to
Matching scATAC-seq–scRNA-seq pairs using Seurat’s canonical correlation determine the specificity of our peak-to-gene links in published chromatin
analyses. To integrate our epigenetic and transcriptomic data we built on previous conformation data. We downloaded previously published naive T cell and HCASM
approaches for integration10,37. We found the approach that worked best for our cell line H3K27ac HiChIP data. We then identified within each peak-to-gene
integrative analyses was using Seurat’s CCA. We performed integration for each link subset the peaks that were most biased to T/NK cells. To do this analysis, we
biological group separately because (1) it improved alignment accuracy and calculated the z score for each peak in the peak-to-gene links, removed all links
(2) required much less memory. First, for both the gene-activity scores matrix below 100 kb and floored each peak coordinate (start or end) to its nearest 10-kb
and scRNA-seq matrix, a Seurat object was created using ‘CreateSeuratObject’, window. We then ranked these links by the z score for the peak, deduplicated the
normalized with ‘NormalizeData’ and the top 2,000 most variable genes or links at a resolution of 10 kb and kept the top 500 remaining peak-to-gene links.
activities ranked by dispersion with ‘FindVariableGenes’ were. We defined the Next, we used juicer dump (no normalization “NONE”) at a 10-kb resolution
union of the top 2,000 most variable genes from scRNA-seq and gene scores for each chromosome in the ‘.hic’ file. We read each chromosome into an
from scATAC-seq and found this increased the concordance downstream (as individual ‘sparseMatrix’ in R and scaled the sparse matrices such that the total
defined by cluster-to-cluster mapping in hematopoiesis and single-cell Spearman cis interactions summed up to 10 million paired-end tags (PETs). Then, for each
correlations). These genes were then used for running CCA using ‘RunCCA’ with peak-to-gene link, the upstream or downstream window (column or row) (whether
the number of canonical correlations to compute as 25. We then calculated the the peak was upstream or downstream of the gene promoter) was identified. To
explained variance using ‘CalcVarExpRatio’ grouping by each of the individual scale the distance of each interaction for interpretability, we linearly interpolated
experimental protocols scATAC-seq (gene-activity scores) and scRNA-seq. We the data to be on a scale from −50% to 150% to visualize the focal interaction. The
then filtered cells where the variance explained by CCA was less than twofold mean interaction signal was reported and repeated for both replicates. The mean
as compared to principal component analysis. We aligned the subspaces with and s.d. across both replicates were calculated and plotted with ggplot in R.
“AlignSubspace” and 25 dimensions to align with reduction.type = “cca” and
grouping.var = “protocol”. For each scATAC-seq cell the nearest scRNA-seq cell was Identifying TF malignant target genes and survival analysis. We wanted to create
identified on the basis of minimizing the Euclidean distance. We created a UMAP a framework for identifying TFs that potentially directly regulate malignant
using the aligned CCA coordinates as input into the uwot UMAP implementation genes. To do this analysis, we first identified a set of TFs whose hypergeometric
with n_neighbors = 50, min_dist = 0.5, metric = “euclidean” and plotted the output enrichment in differential peaks were high across the MPAL subpopulations
with ggplot2 in R. To enable more robust correlation-based downstream analyses, (comparing upregulated peaks against all peaks) and that were identified as being
we used our initial k-nearest-neighbor groupings (nGroups = 4998, KNN = 50) transcriptionally correlated with the accessibility of their motif (see above). Next,
from Cicero14 to group scATAC-seq accessibility, gene-activity scores, scRNA-seq for a given TF and all identified peak-to-gene links, we further subsetted these
closest neighbor and chromVAR15 deviation scores. links by those containing the TF motif. For each MPAL subpopulation,
NAtuRE BiotECHNoLoGY | www.nature.com/naturebiotechnology
NATUre BIoTechNology Letters
we determined whether, for each peak-to-gene link, both the peak and gene Acknowledgements
were upregulated. Then for each gene, we gave a binary score indicating We thank A. Satpathy and other members of the Chang and Greenleaf laboratories for
whether or not that MPAL subpopulation had at least one differential peak-to-gene helpful discussions. We thank the following people at 10x Genomics: D. Jhutty,
link (whose peak and gene are differentially upregulated), and reported J. Lau, J. Lee, L. Montesclaros, K. Pfeiffer, J. Terry, J. Wang, Y. Yin and S. Ziraldo for help
the proportion of subpopulations that were upregulated. In addition, for each gene with sample preparation and library generation of scATAC-seq and feature barcoding
that has at least one differential peak-to-gene link we summed their libraries. We acknowledge the Stanford Hematology Division Tissue Bank for providing
squared correlation R2 and reported that as the differential linkage score. samples for this study. This study was supported by the Swedish Research Council
We kept all genes that had least one MPAL subpopulation with corresponding (grant 2015–06403, to A.M.). M.R.C. is supported by grant K99AG059918 (NIA) and
differential peak-to-gene links. the American Society of Hematology Scholars award. Further support came from
For survival analysis, we downloaded the RPKM TCGA-LAML data46 National Institutes of Health grants P50-HG007735 and UM1-HG009442 (to H.Y.C.
(https://gdc.cancer.gov/about-data/publications/#/?groups=TCGA- and W.J.G.), UM1-HG009436 and U19-AI057266 (to W.J.G), and R35-CA209919 (to
LAML&years=&order=desc). We downloaded the survival data from Bioconductor H.Y.C.), as well as from Ludwig Cancer Research (to R.M. and H.Y.C.) and grants from
RTCGA.clinical (“patient.vital_status”) and matched the RPKM expression using the Chan-Zuckerberg Initiative and the Rita Allen Foundation. H.Y.C. is an Investigator
TCGA IDs. Next, we took all genes that were identified as target genes of the Howard Hughes Medical Institute. W.J.G is a Chan–Zuckerberg Investigator. S.K.
for RUNX1 (n = 732), and computed row-wise z scores for each gene. Next, was supported by The Stanford Genome Training Program (NIH/NHGRI). B.P. was
we took the column means of this matrix to get an average z score across all supported by the JIMB/NIST training program.
RUNX1-target genes. We then identified the top 33% and bottom 33% of donors
on the basis of this expression. We computed the P value using the R package Author contributions
survival ‘survfit(Surv(times,patient.vital_status)~Runx1_TG_Expression,
L.M.M. and S.K. conceived the project and designed the experiments. L.M.M., M.L., E.G.
LAML_Survival)’. We plotted the Kaplan–Meier curve using the R package
and R.M. curated patient samples. S.K. led data production and performed the experiments
survminer ‘ggsurvplot’ in R.
together with A.S.K., A.M. and L.M.M. G.X.Y.Z. provided healthy bone marrow and
peripheral blood CITE-seq data. S.K. analyzed the scADT-seq data with contribution
Reporting Summary. Further information on research design is available in the
from B.P. M.R.C. performed data analysis. J.M.G. conceived the analytical workflows and
Nature Research Reporting Summary linked to this article.
performed the data analysis for scATAC-seq and scRNA-seq supervised by H.Y.C. and
W.J.G. J.M.G., S.K., L.M.M. and W.J.G wrote the manuscript with input from all authors.
Data availability
Sequencing data are deposited in the Gene Expression Omnibus (GEO) with the Competing interests
accession code GSE139369. There are no restrictions on data availability or use.
R.M. is a founder of, is an equity holder in, and serves on the board of directors of Forty
Seven. H.Y.C. has affiliations with Accent Therapeutics (founder and scientific advisory
Code availability
board (SAB) member), 10x Genomics (SAB member), Boundless Bio (cofounder,
Code used in this study can be found on Github at https://github.com/ SAB), Arsenal Biosciences (SAB) and Spring Discovery (SAB member). W.J.G. has
GreenleafLab/MPAL-Single-Cell-2019. affiliations with 10x Genomics (consultant), Guardant Health (consultant) and Protillion
Biosciences (co-founder and consultant).
References
Additional information
47. Robinson, M. D., McCarthy, D. J. & Smyth, G. K. edgeR: a Bioconductor
Supplementary information is available for this paper at https://doi.org/10.1038/
package for differential expression analysis of digital gene expression data.
s41587-019-0332-7.
Bioinformatics 26, 139–140 (2010).
48. Soneson, C. & Robinson, M. D. Bias, robustness and scalability in single-cell Correspondence and requests for materials should be addressed to S.K., L.M.M. or W.J.G.
differential expression analysis. Nat. Methods 15, 255–261 (2018). Reprints and permissions information is available at www.nature.com/reprints.
NAtuRE BiotECHNoLoGY | www.nature.com/naturebiotechnology
