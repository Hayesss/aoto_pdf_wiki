---
source_path: /mnt/c/Users/Administrator/Zotero/storage/SPKDT4VK/Knol 等 - 2025 - The pan-cancer proteome atlas, a mass spectrometry-based landscape for discovering tumor biology, bi.pdf
ingested: 2026-04-23
sha256: 24bf082e17ae4da6
---

Article
The pan-cancer proteome atlas, a mass
spectrometry-based landscape for discovering
tumor biology, biomarkers, and therapeutic targets
Graphical abstract Authors
JacoC.Knol,MenggeLyu,
FranziskaBo¨ttger,...,XiaoluZhan,
TiannanGuo,ConnieR.Jimenez
Correspondence
guotiannan@westlake.edu.cn(T.G.),
c.jimenez@amsterdamumc.nl(C.R.J.)
In brief
Knoletal.reportalargepan-cancer
proteomelandscapebasedonhigh-
throughput,single-shotmass
spectrometryacross22cancertypes
includingbothliquid(n=4)andsolid
cancers(n=18),revealingco-expression-
basedphenotypesandimmune
phenotypesanddefiningtop25ranked
proteinsaspotentialbiomarkersanddrug
targetsforeachcancertypeaswellasa
multi-cancerclassifier.
Highlights
•
Pan-cancerproteomeacross18solidand4liquidcancers
from999humansamples
•
Co-expressedpan-cancerproteinsandbiologywith
potentialclinicalutility
•
CMSproteinsandimmunesubtypeswithprognosticvaluein
colorectalcancer
•
Multi-cancerclassifierforidentificationofmetastasisof
unknownprimaryorigin
Knoletal.,2025,CancerCell43,1328–1346
July14,2025©2025ElsevierInc.Allrightsarereserved,includingthosefor
textanddatamining,AItraining,andsimilartechnologies.
ll
https://doi.org/10.1016/j.ccell.2025.05.003
ll
Article
The pan-cancer proteome atlas, a mass
spectrometry-based landscape for discovering
tumor biology, biomarkers, and therapeutic targets
Jaco C. Knol, 1,2,32 Mengge Lyu, 3,4,32 Franziska Bo¨ ttger, 1,2,32 Madalena Nunes Monteiro, 1,2,32 Thang V. Pham, 1,2
Frank Rolfs, 1,2 Andrea Valle´ s-Mart´ı,1 ,2 Tim Schelfhorst, 1,2 Richard R. de Goeij-de Haas, 1,2 Irene V. Bijnsdorp, 1,2,5
Shuaiyao Wang, 3,4 Fangfei Zhang, 3 Jun A, 3,4 Bart A. Westerman, 2,6 Barbara Sitek, 7,8 Janne Lehtio¨ ,9 Jan Koster,1 0,11
Jan N.M. IJzermans, 12 Hanneke W.M. van Laarhoven, 2,13 Maarten F. Bijlsma, 10,11,14 Jan Paul Medema, 10,11,14
Alex A. Henneman, 1,2 Sander R. Piersma, 1,2 Ruud H. Brakenhoff, 11,15
(Author list continued on next page)
1 Amsterdam UMC, location Vrije Universiteit Amsterdam, Department of Medical Oncology, OncoProteomics Laboratory, De Boelelaan 1117,
Amsterdam, the Netherlands
2 Cancer Center Amsterdam, Imaging and Biomarkers, Amsterdam, the Netherlands
3 School of Medicine, Westlake University, Hangzhou, Zhejiang, China
4 Westlake Center for Intelligent Proteomics, Westlake Laboratory of Life Sciences and Biomedicine, Hangzhou, Zhejiang, China
5 Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Urology, De Boelelaan 1117, Amsterdam, the Netherlands
6 Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Neurosurgery, De Boelelaan 1117, Amsterdam, the Netherlands
7 Medizinisches Proteom-Center, Ruhr-Universita¨ t Bochum, Bochum, Germany
8 Department of Anesthesia, Intensive Care Medicine and Pain Therapy, University Hospital Knappschaftskrankenhaus Bochum, Bochum,
Germany
9 Department of Oncology-Pathology, Science for Life Laboratory, Karolinska Institutet, Stockholm, Sweden
10 Amsterdam UMC location University of Amsterdam, Center for Experimental and Molecular Medicine, Laboratory for Experimental
Oncology and Radiobiology, Meibergdreef 9, Amsterdam, the Netherlands
11 Cancer Center Amsterdam, Cancer Biology and Immunology, Amsterdam, the Netherlands
12 Department of Surgery, Division of HPB & Transplant Surgery, Erasmus MC Transplant Institute, University Medical Center Rotterdam,
Rotterdam, the Netherlands
13 Amsterdam UMC location University of Amsterdam, Department of Medical Oncology, Meibergdreef 9, Amsterdam, the Netherlands
14 Oncode Institute, Amsterdam, the Netherlands
15 Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Otolaryngology and Head and Neck Surgery, De Boelelaan 1117,
Amsterdam, the Netherlands
(Affiliations continued on next page)
SUMMARY
Most cancer proteomics studies to date have focused on a single cancer type. We report The Pan-Cancer Pro-
teome Atlas (TPCPA) based on data-independent acquisition mass spectrometry, to better understand cancer
biology and identify therapeutic targets and biomarkers. TPCPA includes 9,670 proteins derived from 999 pri-
mary tumors representing 22 cancer types. We describe pan-cancer and cancer type-enriched proteins with
extensive external annotation, prioritizing candidate drug targets and biomarkers. Relevant for proteolysis-tar-
geting chimeras, we identify E3-ubiquitin ligases highly expressed in specific tumor types, including HERC5
(esophageal cancer) and RNF5 (liver cancer). Co-expression analysis reveals 13 modules, including unexpected
hub proteins as potential drug targets (e.g., GFPT1, LRPPRC, PINK1, DOCK2, and PTPN6). Analysis of 195
colorectal cancers identifies protein markers for RNA-based consensus molecular subtypes (CMSs) and two
immune subtypes with prognostic value. We report a cancer type classifier for identification of cancers of
unknown primary origin. All TPCPA data can be queried in a dedicated web resource.
INTRODUCTION normal checks and balances. Molecular profiles of tumors may
be leveraged for clinical intervention with personalized treat-
Cancer is a heterogeneous collection of diseases characterized ments. Large-scale genomics efforts of The Cancer Genome
by uncontrolled growth and spread of malignant cells escaping Atlas (TCGA) and the International Cancer Genome Consortium
1328 Cancer Cell 43, 1328–1346, July 14, 2025 © 2025 Elsevier Inc.
All rights are reserved, including those for text and data mining, AI training, and similar technologies.
ll
Article
Jacqueline Cloos, 2,16 Valentina Cordo’,1 7 Daphne de Jong, 2,18,19,20 Geert Kazemier, 11,21 Danijela Koppers-Lalic, 6,11
Mariette Labots, 2,22 Tessa Y.S. Le Large, 11,21 John W.M. Martens, 23 Jules P.P. Meijerink, 17 Madiha Mumtaz, 24
Chantal Scheepbouwer, 6,11,18 Robby E. Kibbelaar, 25 David P. Noske, 6,11 Renske D.M. Steenbergen, 2,18
Nicole C.T. van Grieken, 11,18 Winan van Houdt, 26 Elisa Giovannetti, 2,22 Geert J.L.H. van Leenders, 27 Jos Jonkers, 14,28
Tong Liu, 29 Meisi Yan,3 0 Xiaolu Zhan, 31 Tiannan Guo, 3,4, * and Connie R. Jimenez 1,2,33, *
16 Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Hematology, De Boelelaan 1117, Amsterdam, the Netherlands
17 Princess Maxima Center for Pediatric Oncology, Utrecht, the Netherlands
18 Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Pathology, De Boelelaan 1117, Amsterdam, the Netherlands
19 Department of Pathology, Netherlands Cancer Institute, Amsterdam, the Netherlands
20 HOVON Pathology Facility and Biobank, Amsterdam, the Netherlands
21 Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Surgery, De Boelelaan 1117, Amsterdam, the Netherlands
22 Amsterdam UMC location Vrije Universiteit Amsterdam, Department of Medical Oncology, De Boelelaan 1117, Amsterdam, the Netherlands
23 Department of Medical Oncology, Erasmus MC Cancer Institute, University Medical Center Rotterdam, Rotterdam, the Netherlands
24 School of Biological Sciences, University of the Punjab, Lahore, Pakistan
25 on behalf of the HemoBase Consortium (www.hemobase.eu); Department of Pathology, Pathology Friesland, Leeuwarden, the Netherlands
26 Department of Surgical Oncology, Netherlands Cancer Institute, Amsterdam, the Netherlands
27 Department of Pathology, Erasmus University Medical Center, Rotterdam, the Netherlands
28 Division of Molecular Pathology, Netherlands Cancer Institute, Amsterdam, the Netherlands
29 Department of Breast Surgery, Harbin Medical University, Harbin, China
30 Department of Pathology, Harbin Medical University, Harbin, China
31 Harbin Medical University Cancer Hospital, Harbin, China
32 These authors contributed equally
33 Lead contact
*Correspondence: guotiannan@westlake.edu.cn (T.G.), c.jimenez@amsterdamumc.nl (C.R.J.)
https://doi.org/10.1016/j.ccell.2025.05.003
(ICGC) aim to catalog major cancer-causing genomic alterations data processing methods1 2–14 make it possible to generate
and provide a comprehensive ‘‘atlas’’ of cancer genomic pro- reproducible proteomes at large scale by single-shot liquid chro-
files. 1 Extensive genome sequencing of large cohorts of over matography (LC)-MS without pre-separation of samples. 15,16
30 human cancer types coupled with integrated analyses of indi- Pan-cancer efforts to date focus on a limited set of proteins
vidual cancer types and comprehensive pan-cancer analyses measured using antibody-based methods such as reverse
uncover a very heterogeneous landscape of cellular abnormal- phase protein arrays1 7,18 or involve a meta-analysis of individual
ities, extend current knowledge of tumorigenesis, and innovate cancer type datasets. 19–21 The latter studies use tandem mass
molecular diagnostics. 2,3 Despite these advances, it remains tags (TMT) for sample multiplexing, which poses a challenge
challenging to predict how (epi)genomic and transcriptomic al- for integrating pan-cancer analyses, as, e.g., the number of
terations in tumors affect downstream expression and activity currently available tags is insufficient to accommodate a large
of proteins, the functional units in cells and targets for most ther- panel of different sample groups in a balanced way.
apies. Therefore, selection of targeted therapy solely based on This study reports The Pan-Cancer Proteome Atlas (TPCPA), a
(epi)genomic and transcriptomic profiles leaves room for DIA-MS-based pan-cancer proteomic landscape quantifying
improvement. 9,670 proteins across 999 primary cancer samples, representing
As proteins are key to virtually everything happening in cells, 22 cancer types. This comprehensive analysis reveals sample
comprehensive and quantitative protein measurements are of clustering that is primarily based on cancer type, and supports
high interest for phenotypic characterization. Mass spectrom- the discovery of core cancer biology and cancer type-enriched
etry (MS)-based proteomics provides a powerful approach to features as well as potential biomarkers and therapeutic targets.
directly measure protein abundance and modifications, 4 for Weighted gene co-expression analysis2 2 identifies 13 modules
example in different tissues. 5 Proteome measurements may with known and potential oncogenic drivers as hub proteins. Im-
not only expand our insight into the dynamic molecular behavior mune subset analysis demonstrates the value of single-shot
of cells and help unveil how cancer phenotypes arise but also DIA-MS for cancer immune subtyping in bulk tissues and their
have the potential to improve diagnosis and treatment prognostic value in colorectal cancer. Altogether, our approach
choices. 6–8 Most cancer proteomics studies to date focus on identifies well-established and novel protein biomarkers of cancer
single cancer types, providing in-depth inventories of pro- (sub)types and, more importantly, highlights key proteins that
teomes, often in a multi-omics context. 9–11 These studies aid together enable cancer type classification. TPCPA data are avail-
in understanding the functional states of oncogenic drivers, able via a data portal (http://r2platform.com/TPCPA).
revealing potentially novel therapeutic avenues.
Large-scale proteome analyses across multiple cancer types RESULTS
will provide a more direct view of how the striking diversity of
genomic aberrations impacts signaling pathways and oncogenic Rediscovery of cancer types by unsupervised proteome
processes in different ways, and may reveal new molecular tax- analyses
onomy beyond any phenotypic contributions from the tissue of Comprehensive profiling of protein expression patterns across
origin. This requires a high-throughput MS approach. Recent de- cancer types may elucidate the shared and context-dependent
velopments in data-independent acquisition (DIA)-MS and novel nature of cancer phenotypes. To date, such an approach has
Cancer Cell 43, 1328–1346, July 14, 2025 1329
ll
Article
not been applied in a large pan-cancer context. To explore com- MYC targets, E2F targets, G2M checkpoint, and DNA repair
mon and cancer (sub)type biology, we applied an unbiased pro- (see Figure S2 for ranked violin plots of all hallmark ssGSEA
teomics approach based on DIA-MS to generate a pan-cancer scores across cancer types).
analysis including 22 cancer types. Altogether our unsupervised analyses identified distinct can-
The TPCPA dataset originated from 1,236 DIA raw files cer-type proteomes and discriminatory cancer type biology,
comprising cancer samples, normal tissues and non-tumor adja- underscoring the validity of our large pan-cancer proteome land-
cent tissues, adenoma tissues, benign tissues, as well as HeLa scape. As a first use case, we explored TPCPA data for E3 ubiq-
cell line control samples. A total of 1,172 samples met basic uitin ligases. Targeted therapy via ubiquitin-mediated protein
quality control criteria (Tables S1 and S2A). After further filtering degradation is an emerging approach in cancer therapy. Proteol-
for primary cancer samples only, a minimum number of five sam- ysis-targeting chimeras (PROTACs) are dual-ligand small mole-
ples per cancer type and a minimum data presence of 30% per cules that enable targeting of oncogenic proteins by linking
cancer type, 999 samples remained with a total of 11,250 iden- them to an E3 ligase. 25,26 However, the small subset of currently
tified protein groups for 22 cancer types (Table S2B). The final used E3 ligases may not be sufficient to target the diverse range
TPCPA dataset has been included as a data portal in the R2 of cell lineages and cellular compartments. To address this lim-
platform (http://r2platform.com/TPCPA, Figures S1A–S1E). itation, we investigated whether E3 ligase protein expression is
Grouped by cancer type, the smallest sample set contained enriched in certain tumor types. Such enrichment could enable
eight samples (skin/melanoma), whereas the largest contained selective degradation of oncogenic proteins in tumor cells while
195 colorectal cancer (CRC) samples covering four consensus sparing non-transformed cells in personalized treatments.
molecular subtypes. Figure 2C shows a TPCPA expression heatmap for all E3 ligases
Figure 1 shows an overview of the TPCPA pan-cancer tissue tested. We identified several ligases that are relatively highly ex-
landscape as measured by DIA-MS. Figure 1A gives an overview pressed in specific solid or liquid tumor types (statistics and, for a
of the cancer types in TPCPA. Most samples yielded 5,000– selection, annotation are detailed in the TPCPA data portal,
6,000 identified proteins (Figure 1B), with abundance spanning ‘‘Dedicated Analyses’’ module). These include HERC5 (esopha-
∼4 orders of magnitude. Seven proteins are ‘‘missing proteins’’ geal cancer), RNF5 (liver cancer), LONRF2 (sarcoma), and
according to the HUPO HPP Portal (https://hppportal.net), one RNF216 (cervical cancer). 27–31 The association of enriched li-
of which (USP17L10) was detected with four peptides. Uniform gases with oncogenic pathways (p53, BRCA1, and AKT/
manifold approximation and projection (UMAP)-based dimen- mTORC) as well as metabolic (fat metabolism and amino acid
sion reduction shows approximate co-clustering of cancer types sensing) and immunogenic (TLR) processes points to their
(Figure 1C). HeLa cell line quality controls from different acquisi- essential roles, which might benefit future PROTAC applications.
tion batches cluster together and away from the cancer samples
(Figure S1F). In addition, unsupervised hierarchical clustering Weighted gene co-expression network analysis
occurred largely according to cancer type and separated solid identifies 13 modules with distinct cancer biology and
and non-solid (blood) cancers (Figure 1D). Importantly, blood, enrichment across cancer types
liver, and prostate cancer samples clustered together by cancer We applied the weighted gene co-expression network analysis
type, despite being generated by two laboratories. Moreover, in (WGCNA) algorithm 22 to discern modules of functionally con-
the case of prostate cancer and diffuse large B-cell lymphoma nected proteins with correlated gene expression, and thus iden-
(DLBCL), co-clustering was also seen despite sample type het- tify common and cancer-specific protein modules in TPCPA.
erogeneity (fresh-frozen and formalin-fixed paraffin-embedded This resulted in the assignment of protein subsets to one of 13
tissue). Altogether, these unsupervised analyses indicate that modules (Figure 3A; Table S3). For each module, we listed
cancer type clustering reflects molecular differences between the top five proteins with strongest correlation to the eigenpro-
the 22 cancer types in TPCPA, rather than data acquisition batch tein pattern (‘‘hub proteins’’), looked for correlated tissue
effects. signatures from external sources, 32–34 and created protein net-
To explore cancer biology in an unbiased manner, we per- works as well as protein expression heatmaps showing banding
formed single-sample gene set enrichment analysis (ssGSEA2 3 ) in specific cancer types (Figures 3 and S3).
and unsupervised clustering of ssGSEA scores for cancer Figure 3A shows that modules 1–5 are associated with lower
hallmarks gene sets 24 (Figure 2A). This analysis recapitulated expression in liquid tumors (DLBCL is somewhat of an excep-
approximate clustering of cancer types and separation of solid tion, growing in lumps invading tissues). Modules 1–4 are either
and blood cancers, independent of lab and sample preparation. associated with cell adhesion (modules 1/2), or with an immune/
Importantly, it rediscovered known biology such as the androgen inflammation response (modules 3/4), possibly in a tissue/tumor
response being highly enriched in prostate cancers and the es- microenvironment context. There is ample evidence for an
trogen response relatively high in breast cancers (Figures 2A important role of the tumor microenvironment in cancers
and 2B), while liver cancers were characterized by high enrich- including PDAC and breast cancer. 35–37 The eigengenes/pro-
ment of bile acid metabolism, xenobiotic metabolism, peroxi- teins of modules 1–4 do not strongly correlate with any specific
some and fatty acid metabolism as well as adipogenesis. Apart tissue-specific gene signature (Figure 3A), suggesting that they
from sarcomas, pancreatic cancers showed relatively high represent more common modules in solid tumors. Other mod-
enrichment for the epithelial-mesenchymal transition hallmark. ules appear to be more linked to specific tissues/cancer types,
DLBCL was highly enriched in immune signaling and response and we describe examples in the following texts.
terms. Furthermore, liquid cancers were characterized by rela- Module 5 shows restricted expression, which is very high in
tively high scores for proliferation-related hallmarks, such as colon cancers and also associated with colon tissue signatures
1330 Cancer Cell 43, 1328–1346, July 14, 2025
ll
Article
A B Figure 1. Overview of the TPCPA pan-can-
cer landscape
(A) Origin and sample number per cancer type.
(B) Protein identification rate per sample.
(C) UMAP-based visualization of samples.
(D) Hierarchical clustering of samples after filtering
for the 20% most variable protein groups. Corre-
sponding color legends are at the bottom of the
figure. Color codes for (A–C) are the same as for
the cancer types in (D). B-ALL/T-ALL, B-cell/T-cell
acute lymphoblastic leukemia; AML, acute
myeloid leukemia; DLBCL, diffuse large B-cell
lymphoma; FF, fresh frozen; FFPE, formalin-fixed
paraffin-embedded; mirVana/QIAGEN/RNA-Bee,
C D leftover after nucleic acid extraction with the
respective kits; PB, peripheral blood.
extracellular vesicles (included in mod-
ule 6 biology), and stress-induced
secretion of the latter has been impli-
cated in tumor progression. 51–53 Module
6 hub proteins also have links with
mitochondria and mitophagy. Both
Hsp90alpha and PMPCB are involved
in mitochondrial protein import 54–56
and influence levels of the mitophagy-
inducing kinase PINK1, 57,58 and
LRPPRC is a multi-functional protein 59
that also impacts, among others, mito-
chondrial biology and mitophagy.
(Figure 3A). Key associated processes include cell adhesion and Use of module 7 is also more widespread although module
cell junction biology, which are important in epithelial tis- expression is strongly correlated with normal-liver tissue sig-
sues.3 8–41 CTNNB1/β-catenin, a hub protein in module 5, has natures. It is predominantly linked to small molecule meta-
been classically known for its role in (aberrant) Wnt signaling in bolism and respiration in mitochondria. These organelles,
colorectal cancer carcinogenesis. 42,43 Interestingly, nucleotide which also affect apoptotic and redox states, play an impor-
sugar biosynthesis represents the top biological process, and tant role in cancer. 60,61 Various mitochondrial metabolites
this is in line with GFPT1/GFAT1 and GFPT2/GFAT2 (gluta- can have broader cell physiological roles such as signaling
mine-fructose-6-phosphate transaminases) being among the and transcriptional and epigenetic activation. 62,63 This ‘‘mito-
five hub proteins. These proteins have key roles in N- and chondrial’’ module is apparently utilized by multiple can-
O-linked glycosylation, thereby impacting protein activity, cer types.
expression, and possibly interactions important for cell Module 10 exhibits a strong correlation with esophagus tis-
adhesion. Notably, functionally linking two hub proteins, the sue signatures, and is mainly active in cervical, head-and-
GFAT1/hexosamine biosynthetic pathway/O-GlcNAcylation neck, and esophageal cancers. Especially the former two are
axis regulates β-catenin activity to promote pancreatic cancer dominated by squamous cell histology, and module 10 is asso-
aggressiveness. 44 Underscoring their importance, both GFPT1 ciated with keratin-based intermediate filaments and epithelial
and GFPT2 have been shown to be a targetable liability in mouse cell biology.
models for pancreatic or lung cancer. 45,46 Module 12 is mostly restricted to blood cancers, correlated
Module 6 expression, albeit more widespread, is also prom- with spleen and lymphoid signatures, and linked with immune
inent in colon cancers, correlates with both colon tissue and biology (Figures 3A and S3). Concordantly, module 12 hub pro-
housekeeping signatures, and is linked to diverse biology teins subserve associated roles in immune cells. DOCK2 and
including stress-related terms. Hub proteins of module 6 are ARHGAP25 are Rho GTPase regulators involved in actin
all potential drug targets. Heat shock proteins HSP90AA1 cytoskeleton remodeling, cell polarity, and lymphocyte migra-
and HSP90AB1 are stress-responsive molecular proteins that tion.6 4,65 Furthermore, PTPN6 is a protein tyrosine phosphatase
promote proper protein folding as chaperones, and modulate involved in hematopoietic cell signaling and immune checkpoint
transcription regulation and signal transduction. HSP90 modulation, 66 and IL16 is a cytokine with chemotactic and T cell-
expression is upregulated in numerous solid tumors and impli- modulatory functions. 67 Apart from module 12, blood cancers
cated in proliferation, angiogenesis, and metastasis. 47,48 Inhi- exhibit high(er) expression in a limited number of modules. ALL
bition of HSP90 has emerged as an attractive anticancer and DLBCL display activity in modules 9 and 13, which are corre-
approach. 49,50 Interestingly, HSPs are major components of lated with housekeeping signatures and are involved in gene
Cancer Cell 43, 1328–1346, July 14, 2025 1331
ll
Article
A Figure 2. Recapitulation of tumor biology
and use case
(A) Hierarchical clustering of ssGSEA scores for
enrichment of cancer hallmark gene sets. Anno-
tation tracks as in Figure 1, and color legends are
at the bottom of the panel.
(B) ssGSEA score distributions for selected cancer
hallmarks showing established biology. See also
Figure S2.
(C) Use case: heatmap showing differential
expression of E3 ubiquitin ligases detected in
TPCPA. Color codes for cancer types are the
same for all panels and as in Figure 1.
Overall, this co-expression analysis
underscores global differences between
solid and liquid cancers. It extends the
hallmark enrichment analysis by connect-
ing different sets of proteins to a more
limited number of phenotypes that are
not restricted to individual cancer types,
and by pinpointing unexpected hub pro-
teins that may provide drug targets.
Immune infiltration analysis
B reveals cancer type heterogeneity
To characterize the level of general
immune infiltration, we applied the
ESTIMATE algorithm. 68 As expected,
non-solid (blood) cancer types that arise
from the expansion of abnormal immune
progenitors had the highest immune
scores. Of the solid cancers, skin cancer
(melanoma) had one of the highest
scores, while prostate cancer, brain can-
cer (high-grade glioma), and ovarian can-
cer were found at the other extreme
(Figure 4A, left). These findings are in
line with the general concept of immune
‘‘hot’’ and ‘‘cold’’ solid tumor types
defined by their clinical response to
C immunotherapy. Most prostate, ovary,
and brain cancers are considered cold
tumors and are generally found to
respond poorly to immune checkpoint in-
hibitors. 69 Likewise, the known stromal
character of the tumor microenvironment
of pancreatic cancer was reflected in
the highest stromal score (Figure 4A,
right). 70 Thus, despite being based on
transcriptional cancer tissue profiles, the
ESTIMATE algorithm can also give mean-
ingful stromal and immune score esti-
mates for tumor samples based on bulk
protein expression data.
expression and cell cycling. DLBCL also shows high expression To better understand the immune phenotypes, we performed
in module 11, which correlates moderately with spleen/lymphoid ssGSEA using immune signatures that were generated either
signatures, is rather widespread, and includes antigen presenta- from the transcriptional profiles of purified immune cell
tion hub proteins. subsets by Bindea et al. 71 (Figure S4C) or Tamborero et al.7 2
1332 Cancer Cell 43, 1328–1346, July 14, 2025
ll
Article
A
B C
Figure 3. Weighted gene co-expression network analysis
(A) Overview of WGCNA modules. Five proteins with highest correlation to a module’s eigenprotein were considered hub proteins. Gene ontology analysis reveals
distinct module biology. High correlation with published tissue signatures is indicated. The heatmap shows standardized module eigenprotein expression
patterns (low-high, blue-red).
(B) Protein association networks for modules 5 and 6 highly expressed in colon cancer, showing top 100 nodes (by module eigenprotein correlation; white: hub
proteins) and top 500 edges (by topological overlap measure).
(C) Module 5/6 expression heatmaps. Annotation tracks in (A) and (C) indicate cancer types and color codes are the same as in Figure 1. See also Figure S3, and
Table S3 for gene ontology statistics.
(Figures 4B–4D, S4A, and S4B), or from the MS-based protein tures were best able to separate non-solid from solid tumors
expression profiles of primary human hematopoietic cell popula- (Figure 4D), showing the expected strong enrichment of B cell
tions 73 (Figure S4D). In hierarchical clustering of individual subtypes in B-ALL (and DLBCL) and T cell subtypes in T-ALL
cancer samples based on ssGSEA scores, the Tamborero signa- (Figures 4B–4D). Of note, deconvolution approaches using
Cancer Cell 43, 1328–1346, July 14, 2025 1333
ll
Article
A
B C
D
Figure 4. Immune infiltration analysis reveals cancer type heterogeneity
(A) Cancer type-specific distribution of ESTIMATE immune (left) and stroma (right) scores.
(B) Hierarchical clustering of ssGSEA scores for enrichment of Tamborero immune subtype signatures, averaged per cancer type.
(C) Cancer type-specific distribution of ssGSEA scores for selected Tamborero immune subtypes (upper: B cells; lower: CD8 + T cells; remaining subtypes in
Figure S4A).
(D) As (B), using individual sample scores. Color codes for cancer types are the same as in Figure 1. Tcm, T central memory cells; Tem, T effector memory cells;
Tfh, T follicular helper cells; NKbrigh, natural killer (NK) CD56bright cells; NKdim, NK CD56dim cells; iDC, immature dendritic cells; Tgd, T gamma delta cells; Treg,
regulatory T cells; Th, T helper cells. See also Figure S4.
EPIC 74 and CIBERSORT 75 did not result in meaningful results neous nature of most cancer types. Gene set coverage varied,
(data not shown), suggesting that they may be less suitable to ranging from 33% for NK CD56dim (strongly enriched in prostate
quantify infiltration of immune cell populations in solid tumors us- cancer, Figure S4A) to 81% for the CD8+ T cell signature
ing bulk protein expression data. This was also observed for RNA (Table S4).
sequencing (RNA-seq) expression data. 72 Evaluating the marker-based inference approaches described
Beyond the clear distinction between solid and non-solid can- previously, we selected the Tamborero gene sets for a dedicated
cer types and the expected non-solid tumor enrichment profiles, analysis of immune infiltration in CRC (see in the following text).
hierarchical clustering of solid cancers (Figure S4B) showed that This was based on superior ability to separate non-solid from
cancer type does not fully determine the immune infiltration solid tumors in clustering of individual tumors (Figure S4D). Alto-
pattern of a tumor. While tumors of certain cancer types (e.g., gether, our immune subset analysis shows both heterogeneity
prostate, brain, and colon) clustered largely together, samples within cancer types and shared immune subset compositions
of other types were more interspersed, illustrating the heteroge- across multiple cancer types.
1334 Cancer Cell 43, 1328–1346, July 14, 2025
ll
Article
Figure 5. Annotation of top 10 cancer type-enriched proteins as potential biomarkers
Proteins enriched in a cancer type compared to all/most other solid or non-solid cancers are annotated by: log2 fold change, Comp_higher, the number of
comparisons to other individual solid/non-solid cancers where abundance is at least Comp_higher_FC-fold higher, (when available) log2 fold change in published
(legend continued on next page)
Cancer Cell 43, 1328–1346, July 14, 2025 1335
ll
Article
Supervised analyses pinpoint pan-cancer and cancer ‘‘Cancers’’ module). Among the top 10 genes for 32 T-ALL sam-
type-associated proteins as potential biomarkers and ples (FAM76A, MYO7B, GATA3, CYP4V2, CBFA2T2, TFDP2,
drug targets CD1E, HIRA, KLF12, and ZBTB14; all uniquely identified), only
Pan-cancer biology and markers GATA3 and CBFA2T2 have thus far been connected to T-ALL,
To gain further insight into (pan-)cancer biology and proteins a cancer type that has not been extensively explored by prote-
associated with solid and non-solid/blood tumors as well as in- omics. As an example for the solid cancers, all top 10 proteins
dividual cancer types, we performed supervised analyses. In or- for 30 brain cancer/high-grade glioma samples (CAMK2D,
der to pinpoint markers for pan-cancer intrinsic processes, all ADGRL3, CPNE5, GPR37L1, PCDH9, RGMA, GFAP, NCAN,
blood cancers were compared to all solid cancers. Hierarchical SLC1A3, and INA) have been connected to cancer, and most
clustering based on significantly differential proteins and volcano of them are tissue-enriched and implicated in nervous system
plotting underscore the large proteome differences between development and synaptic signaling. To our knowledge, multiple
non-solid and solid cancers (Figures S5A and S5B). brain cancer-enriched proteins (ADGRL3, CPNE5, GPR37L1,
Unsurprisingly, pan-cancer features of blood cancers and RGMA) have thus far remained unreported in the context
included immune-associated functions (lymphocyte/leukocyte of brain cancer. The top-ranked protein (uniquely identified in
activation/differentiation, antigen processing/presentation, and brain cancers) is CAMK2D, a protein kinase involved in cell adhe-
phagocytosis), as well as supporting biological processes, sion, neuron projection development, and multicellular organism
such as cell cycle, chromatin organization, and cell adhesion signaling, and previously linked to mitotic checkpoint control in
(Figure S5C). Interestingly, several of the top 25 blood cancer- glioma. 77 Underscoring their potential utility as non-invasive
enriched proteins, i.e., BCL7A, IKZF1, SEPTIN6, DOCK2, biomarker, many top-ranked proteins are detectable in plasma
PTPRC, and PAX5, are known cancer genes, while PASK is a (see annotations in Figure 5).
protein kinase implicated in a link between cellular energy Altogether, our approach of selecting the most enriched pro-
metabolism and differentiation competence 76 (Figure S5E). teins for a given cancer type can not only identify known diag-
Conversely, solid cancers were characterized by terms such as nostic biomarkers but also putative diagnostic and prognostic
cell adhesion, cytoskeletal/cell junction organization and cell biomarkers as well as potential therapeutic targets.
migration, as well as response to stress, detoxification, and Cancer type classifier
regulation of vesicle-mediated transport and endocytosis We investigated the possibility of identifying the solid cancer
(Figure S5D). Interestingly, subcluster 1 of the protein interaction type in our pan-cancer landscape using the top 25 differential
network, linked to cell differentiation and adhesion, includes the solid tumor proteins as input. When validated on metastatic tis-
oncogenic kinases EGFR (a highly connected node) and ERBB3 sues, such a classifier could be of interest for identification of
(Figure S5D). Top ranked proteins (unique in solid cancers) metastases with an unidentified primary origin. Three-quarters
included the cancer gene PTPRK and the indatuximab ravtan- (649) of the solid tumor samples were employed to train a
sine target SDC1, which is detectable on the cell surface and multiclass model using the extreme gradient boosting
in plasma (Figure S5F). (XGBoost) algorithm (Figure S6). The top 25 proteins of each
Cancer type-enriched biology and markers of 17 solid cancer types were prioritized in the training of the
To pinpoint cancer type-enriched proteins, each solid cancer model. We selected 75 proteins with importance scores
type of interest was compared to the 17 other solid cancers while ≥0.005 as features of the model (Figures 6A and 6B). The model
each non-solid/blood cancer of interest was compared to the 3 was evaluated using leave-one-out cross-validation on the
other blood cancers (Table S5). For each cancer type, we training set (Table S7). It demonstrated good generalization abil-
created protein-protein interaction networks annotated with ity on the remaining 217 samples (Figures 6C and S6B), with an
gene ontologies for the top 200 enriched proteins (Table S6) as area under the curve (AUC) of 0.97–1 and only 20 samples being
well as annotation plots for the top 25 most differentially abun- misclassified (Figures 6C and S6). The latter all had a missing
dant proteins. Visualization of complete results can be viewed rate exceeding 20% for the 75-protein signature. Among
in the TPCPA data portal (for an example, see Figure S1D). them, three misclassified esophagus samples out of 8 were pre-
Next to proteins that were not previously implicated, most top dicted as pancreas. This suggests that distinguishing between
25 cancer type-enriched proteins included well-established the two cancer types within the model is challenging. Two out
markers for the pertinent tumor type, including NAPSA in lung of 11 pancreas samples from the Guo lab were incorrectly iden-
adenocarcinomas, CEACAM5 in CRC, CEACAM6 in gastric can- tified as gallbladder, which may be related to the anatomical
cer, FOLH1 in prostate cancer, KRT75 and KRT14 in head-neck connection between the gallbladder and pancreas via the com-
cancer, MPO in AML, and TSHR in thyroid cancer. Figure 5 mon bile duct. Three out of 13 stomach samples were misclas-
shows the top 10 enriched proteins per cancer type that where sified as either colon, esophagus, or pancreas, which may
possible were filtered for increased abundance in cancer versus correlate with the site of origin of the gastric cancer samples.
normal tissue based on external data. Many top enriched These misclassifications may also reflect a high resemblance
proteins in Figure 5 are supported by literature as detailed between gastrointestinal cancers, especially foregut-derived
in the TPCPA data portal (http://r2platform.com/TPCPA, tumors.
normal-versus-tumor tissue comparisons at the protein (NvT_Log2FC) or RNA level (RNA_ NvT_Log2FC), tissue-/cancer-enrichment (Tissue_enr./Cancer_enr.)
according to the Human Protein Atlas (HPA), presence in plasma/secretome/surfaceome/kinase/cancer gene data collections, and the subcluster index in a top
200 protein network. Color bar indicates color scale for log2 fold change columns.
1336 Cancer Cell 43, 1328–1346, July 14, 2025
ll
Article
A B Figure 6. Cancer type classifier
(A) Feature score of 75 proteins derived from the
top 25 proteins of 17 solid cancer types (darkred:
score ≥0.005).
(B) Feature network. Border colors: cancer type(s)
where the protein is a top-25 differential protein.
Node colors: average log2 protein intensity in the
border-indicated cancer type. Cancer type colors
are as in Figure 1.
(C) Prediction accuracy for each sample in the test
dataset. Filled circles: predictions, closed circles:
truth. Dotted lines: incorrect predictions. Dot and
bar colors indicate cancer types and are the same
as in Figure 1.
(D) Receiver operating characteristic (ROC) curves
showing performance of the classifier in external
validation datasets for primary kidney or breast
tumors.
(E) Same for external validation datasets for met-
astatic colon or ovary cancers See also Figure S6.
C
Protein markers associated with
colorectal cancer consensus
molecular subtypes
Colorectal cancer presents a complex
and heterogeneous disease land-
scape. 81 The consensus molecular
subtype (CMS) classification system fa-
cilitates a more comprehensive under-
D E standing of CRC in relation to cancer
biology and clinical characteristics.
The four CMS subtypes include MSI-
immune, ‘‘canonical’’, metabolic, and
mesenchymal subtypes. These sub-
types have specific molecular and clin-
ical characteristics, such as DNA repair
insufficiency and genomic alterations,
Since we used all samples, including test samples, for feature mutations in specific genes, activation of signaling pathways,
selection, there may have been some overfitting in test set clas- and disparities in survival. 82
sification. To further validate the potential of our cancer-type The CMS system is based on data from multiple transcriptom-
classifier, we explored four external datasets. First, data from ics studies. Using proteogenomics, the CPTAC consortium an-
the Clinical Proteomic Tumor Analysis Consortium (CPTAC) renal notated CRC samples by CMS subtype. 83 However, an in-depth
cancer study 78 and an independent DIA breast cancer dataset 79 proteomic analysis of the biological features of each CMS and a
were processed in the same way as for TPCPA. Predictions using proteomic classifier that can be used in the absence of transcrip-
our model achieved an AUC of 0.998 for the CPTAC kidney can- tomic data are lacking. To fill this gap, we analyzed the proteome
cer dataset, and an AUC of 0.992 for the breast cancer dataset of 191 primary CRC tumor samples from TPCPA with matched
(Figure 6D). Second, to demonstrate the utility of our model for transcriptome profiling and CMS classification (54 CMS1, 102
metastatic cancers, we analyzed 28 metastatic ovarian cancer CMS2, 15 CMS3, and 20 CMS4 from AMC, EMC, and NKI co-
samples 80 and 32 metastatic colorectal cancer samples (unpub- horts). We investigated ssGSEA enrichment scores of cancer
lished Jimenez lab data). Using the top 75 features identified in hallmark gene sets 24 in each CMS group across cohorts
training, classification of metastatic ovarian and colorectal can- (Figure 7A) and per cohort (Figure S7A). Although samples
cers yielded an AUC of 1 and 0.98, respectively (Figure 6E). derived from different sample preparation workflows and three
This indicates that the model has the potential to classify meta- different cohorts, CMS-associated cancer biology was largely
static cancers from different primary origins, warranting studies preserved across cohorts. Overall, we confirmed previously re-
in more independent cancer types. ported CMS biology. 82 CMS1 had an immune phenotype, spe-
Hence, it is possible to distinguish solid cancer types using DIA- cifically IL6-JAK/STAT3 signaling. Other immune pathways,
MS-based proteomics, with an important possible application be- such as IL2-STAT5, inflammatory response, complement, and
ing the determination of the origin of metastatic lesions when interferon responses were enriched in both CMS1 and CMS4.
unknown. CMS2 had a proliferative phenotype including MYC signaling
Cancer Cell 43, 1328–1346, July 14, 2025 1337
ll
Article
A B Figure 7. Colorectal cancer CMS subtype
analysis
(A) Heatmap of ssGSEA scores for enrichment of
cancer hallmark genesets significantly different (t
test, p < 0.05) between the highest group and the
rest.
(B) Heatmap of proteomic CMS signatures across
191 CRC samples. Signatures: top-25 proteins
from comparisons of each CMS against the
others. Annotation by cohort, CMS subtype, mi-
crosatellite instability (MSI, unstable; MSS, sta-
ble), and immune consensus cluster.
(C) CMS class centroids from classification of a
38-sample subset. Expression weights around the
mean per protein and subtype. See also Figure S7.
C
lation. The top 25 proteins for each CMS
exhibited consistent and enriched abun-
dance across samples of the pertinent
subtype (Figure 7B). Separate cohorts
showed a similar pattern of enrichment
(Figure S7B).
CMS subtype proteome classifier
To assess the potential of DIA-MS prote-
ome profiling for CMS subtype classifica-
tion, we constructed a CMS subtype
and G2M checkpoint terms, confirming the previously reported classifier. The top 25 enriched proteins for each CMS were
cell cycle enrichment. CMS3 had a metabolic phenotype, evi- used to train a classifier using the AMC cohort (n = 38) with a
denced by fatty acid metabolism, and CMS4 had a mesen- balanced composition of transcriptomics-based CMS subtypes,
chymal phenotype, with activation of angiogenesis, EMT, and while performance was examined on an independent label-free
apical surface and junction terms. As new insights, we found colon cancer proteomics dataset from CPTAC (n = 100).8 3 Out
enrichment of the MTORC1 pathway for CMS1, peroxisome of 100 CMS-enriched proteins, 84 were detected in the valida-
and protein secretion terms for CMS3, and ROS pathway, p53 tion set. These were used as input for classification training as
pathway, UV response, and hypoxia terms for CMS4. Similar an- performed in the CPTAC study8 3 with the nearest shrunken cen-
alyses per cohort (Figure S7A) were consistent with the global troids method 84 implemented in the pamr package for R.
analysis and, importantly, proteome insights were largely consis- Using default cross-validation, a minimal error was achieved
tent between cohorts. using 52 proteins (Figure S7C), which were used to construct
To identify significant proteome differences between CMS the final CMS classifier (Figure 7C). The classifier generalized
subtypes, we compared each CMS versus all others (see the well on the validation dataset with an accuracy of 72%
TPCPA data portal for complete results per CMS subtype). (Figure S7D) and a significant association between predicted
Importantly, most top 200 CMS subtype-enriched proteins vali- values and true values (p < 0.0001, Fisher’s exact test). In addi-
date well at the RNA level in external datasets as can be seen tion, we repeated the training procedure with 10,000 random
from violin plots that have been added to the TPCPA data portal permutations of CMS labels. The accuracy distribution is shown
(‘‘CRC CMS prot/mRNA’’ module). At the RNA level, only a small in Figure S7E, illustrating a significant association of proteomics
subset of 44 blood proteins were absent or not enriched, while data and CMS labels (p = 0.00001).
79 CMS-enriched proteins were differentially abundant (see Colon cancer immune subtype analysis reveals an
data portal). The top 200 proteins enriched in CMS1 were largely association with CMS subtypes and survival
related to immune system processes, exosomes and secretory Based on 209 protein members of the Tamborero immune signa-
granules. Top 200 CMS2 proteins largely revealed biology tures that were detected in the 195 TPCPA colon cancer sam-
related to mitochondrial gene expression and translation, and ples, we used consensus clustering to identify samples with
small molecule metabolism. Interestingly, transcriptomic studies similar immune infiltration patterns (Figures 8A and S8A). We
did not find metabolism-related pathways as differential in identified 3 robust immune consensus clusters (CC), where a
CMS2 82 ; mitochondrial respiration could be supportive of cell fourth CC consisted of only 2 samples (Figure S8A). Unsuper-
growth. Top 200 CMS3 proteins were related to vesicle-medi- vised hierarchical clustering based on the ssGSEA scores for
ated transport, extracellular exosomes, and carbohydrate and Tamborero signatures revealed 2 major clusters, one being en-
lipid metabolism. Top 200 CMS4 proteins included cell adhe- riched for CMS subtypes 1/4, and the other for CMS subtypes
sion, extracellular matrix, and angiogenesis-related proteins, 2/3 (Figure 8A). Strikingly, this aligned with the clustering of im-
and important processes included response to transforming mune CC2 and CC1, respectively. Indeed, for both AMC and
growth factor β (TGF-β), blood vessel development, and coagu- EMC cohorts immune CC2 was enriched for CMS subtypes
1338 Cancer Cell 43, 1328–1346, July 14, 2025
ll
Article
A
B C
D E
Figure 8. Immune subsets in colorectal CMS subtypes and relation to survival
(A) Hierarchical clustering of ssGSEA scores for enrichment of Tamborero immune subtype signatures in 195 CRC samples. Annotation of CMS subtype, immune
consensus cluster (CC), microsatellite instability, and cohort.
(B) Immune consensus cluster-specific distribution of ssGSEA scores for selected Tamborero immune subtype signatures with a significant difference between
CC1 and CC2 and a gene set overlap of >50%.
(C) Association of CMS subtypes with immune CC1/2 for the AMC cohort.
(D) Survival plots for the AMC cohort.
(E) Same, but independent RNA-level analysis. N.A., not available. See also Figure S8.
1/4 and immune CC1 for CMS subtypes 2/3 (Figures 8C and rence-free survival (RFS) data (Table S8C). In this cohort,
S8D). Immune CC1 was characterized by significantly increased CMS2/3 showed considerably better RFS than CMS1/4
infiltration with activated CD8 + T cells and T helper (Th) cells, (Figure 8D, top survival plot). Remarkably, immune CC could
lower infiltration with regulatory T cells, and lower levels of innate predict survival more significantly than CMS subtype, with im-
immunity subsets, such as macrophages, neutrophils, and mast mune CC1 (CMS2/3-enriched) showing longer RFS than immune
cells (Figures 8B and S8B; Table S8A). As all immune CC3 sam- CC2 (CMS1/4-enriched) (Figure 8D, bottom plot). In line with this,
ples (mainly CMS2) were part of the NKI cohort (Table S8B), in early-stage colorectal cancer the presence of activated CD8 +
these were not considered for immune subtype comparisons T cells both within the tumor and in the surrounding stroma may
to avoid cohort bias. be a better predictor of patient survival than traditional staging. 85
Finally, to assess which colon cancer subtyping could best CMS4, which had the worst RFS (Figure 8D, top survival plot),
explain clinical behavior, survival analysis was conducted for was significantly depleted in Th cells and also had the lowest
the AMC cohort, stage-2 cancer patients with available recur- level of CD8 + T cells (Figure S8C; Table S8D). On the other
Cancer Cell 43, 1328–1346, July 14, 2025 1339
ll
Article
hand, CMS4 was significantly enriched in eosinophils, macro- scape of almost 10,000 proteins based on 999 tumor samples.
phages, mast cells, and regulatory T cells, in agreement with Our analysis pinpointed top candidate protein biomarkers and
its previously described ‘‘inflamed phenotype’’ associated with targets for individual cancer types and (pan-cancer) for solid
expansion of innate immunity cells, expression of immunosup- and blood cancers. The value of the cancer type-enriched pro-
pressive factors, and decreased presence of components of teins was highlighted by constructing a cancer-type classifier
Th and CD8 T cell pathways.8 6–88 While the immune ‘‘cold’’ of 75 proteins that was validated on four independent cohorts
CMS2 and CMS3 subtypes show similar enrichment trends for of renal, breast, ovarian, and colorectal tumors. Moreover, our
most immune subsets (Figure S8C), the relatively higher enrich- immune subset analysis further uncovered tumor heterogeneity
ment of T follicular helper cells and NK CD56bright cells in CMS3 with potential implications for immunotherapy. Finally, analysis
distinguishes CMS3 from all other CMS subtypes. Of note, in the of 195 colon cancers in TPCPA identified protein markers and
EMC cohort (stage-1/2 CRC), CMS1/4 showed better disease- a 52-protein-based classifier for the four CRC CMS subtypes
free survival than CMS2/3 (Figure S8E). However also here, im- previously defined using transcriptomics data. 82
mune CC1 was CMS2/3-enriched whereas immune CC2 was Our functional proteome analyses provide insights into (co-ex-
CMS1/4-enriched (Figure 8D). Again, immune CC could predict pressed) proteins linked to cancer hallmarks and immune land-
survival more significantly than CMS subtype (Figure S8E). scapes that, together with cancer-type enrichment analyses
Importantly, an RNA-level analysis for the AMC cohort (public and ranking, reveal potentially novel diagnostic and therapeutic
data from independent pieces of the same tumors) largely avenues. Because not all cancer-enriched proteins are drivers
corroborated the protein-level results (Figure 8E). themselves, identifying causally implicated markers remains a
In summary, single-shot bulk proteomics in combination with key challenge. We therefore also mapped extensive external an-
infiltrating immune cell inference are powerful tools to categorize notations (tissue-enriched, cancer-enriched, detectability in
CRC samples according to their distinct immune landscapes. In plasma/on cell surface, kinase, cancer gene) to the top cancer-
doing so, we can not only capture known immune-related enriched proteins. These annotations were used to pinpoint the
biology but also highlight immune-activated/suppressed sub- most relevant markers and targets for blood and solid tumors
populations that translate to differences in patient survival. To (pan-cancer) and per cancer type. Moreover, many top enriched
our knowledge, this is the first analysis of colon cancer immune proteins were validated using literature mining (see http://
subtyping performed at the proteome level with a clinically rele- r2platform.com/TPCPA). The rediscovery of established cancer
vant, prognostic link, adding insights to the burgeoing field of im- type-associated biology and multiple markers used in the clinic
muno-oncology. for the different cancer types underscores the validity of our
approach. For example, top 25 enriched proteins included
Interactive TPCPA data portal MPO for AML, KRT7 and KRT14 for bladder cancer, GFAP in
The TPCPA portal included in the R2 Genomics Analysis & Visu- brain cancer (high-grade glioma), CEACAM5 in colon cancer,
alization Platform (http://r2platform.com/TPCPA) has five mod- CEACAM6 in stomach cancer, KRT75 in head and neck cancer,
ules: Cohort—overview of meta data with filtering options and CD70 in kidney cancer, NAPSA in lung cancer, FOLH1 and KLK2
interactive pie charts (Figure S1B); Proteins—for searching/se- in prostate cancer, and TSHR and TG in thyroid cancer. Novel
lecting and interactive expression plotting for specific proteins potential protein markers and targets of interest based on
(single/couples/groups) (Figure S1C); Cancers—summary fig- ranking and annotation were identified for almost every cancer
ures with biological data mining and supporting tables per can- type and remain to be validated in future studies.
cer type (Figure S1D); CRC CMS Protein/mRNA—violin plots Another important result is the cancer type classifier utilizing
for expression of top 200 CMS features at the protein or mRNA 75 proteins derived from the top 25 enriched proteins of the can-
level in external datasets; and Dedicated Analyses—E3 ligase cer type analysis. This classifier performed well on four external
use case and subtype analyses for lung and breast cancer datasets, including two metastatic cohorts. More extensive
(Figure S1E). exploration of its potential to identify the unknown primary origin
of metastases (∼10% of all cancers) is warranted. In future
DISCUSSION studies, we will benchmark this classifier by determining the can-
cer of origin of metastatic lesions with known origin and explore
Large-scale cancer genomics and in-depth cancer proteoge- the value for classifying metastases with unidentified origin.
nomics efforts of individual cancer types have increased our Moreover, in view of the importance of the four RNA-based
understanding of cancer biology and driving oncogenic mecha- CMS subtypes of colorectal cancer and international efforts to
nisms. 1–3,9–11 To further obtain insights into cancer type biology develop this system as a basis for future clinical stratification
in a pan-cancer context and unravel pan-cancer and cancer type and subtype-based targeted interventions, we developed a pro-
markers and targets, a global molecular readout close to func- tein-based CMS classifier. The advantage is that it can be easily
tion is needed with sufficient throughput. High-throughput clin- coupled to the analysis of FFPE material. The 52-protein classi-
ical proteomics based on single-shot DIA-MS has enabled fier was based on the top 25 subtype-enriched proteins for each
large-scale proteome profiling in recent years, also in a multi-lab- CMS subtype. It generalized well on an external validation data-
oratory setting. 16,89–92 set, and permutation analysis demonstrated a highly significant
In a collaborative effort of four cancer proteomics laboratories association of predicted labels with true labels. These promising
and their clinical partners, we generated a proteome atlas results warrant further development of DIA-MS-based colon
comprising 22 cancer types and performed pan-cancer and can- cancer subtyping, and possibly an assessment of the CMS clas-
cer (sub)type analyses of the resultant large pan-cancer land- sifier’s utility for other gastro-intestinal (GI) and non-GI cancers.
1340 Cancer Cell 43, 1328–1346, July 14, 2025
ll
Article
Furthermore, we were able to demonstrate that single-shot pro- Materials availability
teomics coupled to infiltrating immune cell inference is a power- This study did not generate new reagents.
ful approach to characterize CRC samples by their immune
landscape, the latter being linked to (differences in) patient Data and code availability
survival. Though pinpointing proteins associated with these im-
The mass-spectrometric data have been deposited to the ProteomeXchange
Consortium via the PRIDE partner repository with dataset identifier
mune subtypes is of interest for an immunohistochemistry
PXD054790. The TPCPA data portal can be freely accessed at http://
approach, we believe that immune subset analysis using protein
r2platform.com/TPCPA/by selecting ‘‘use R2 without an account’’ when land-
signatures will be a more robust approach for confident subtype ing in the login screen.
determination. Finally, to make TPCPA available to the cancer
research community, an interactive data portal was constructed ACKNOWLEDGMENTS
for exploration of protein expression patterns across different
cancer types and functional data mining summaries per can- Cancer Center Amsterdam and the Netherlands Organisation for Scientific
cer type. Research (NWO Middelgroot, #91116017) are acknowledged for support of
In summary, the TPCPA dataset generated by high-throughput
proteomics infrastructure. This work was further supported by project grants
of the Dutch Cancer Society to C.R.J. (KWF VU-6816, KWF-VU10212, and
DIA-MS yielded relevant global insights into proteins associated
KWF-VU12516), KWF- UvA2013-6331 to J.P.M. and C.R.J., KWF-EMCR
with the functional underpinning of cancers. Future studies using 2015–8022 to C.R.J. (coPI), KWF2016_10355 to J.P.M. and C.R.J.,
more molecular information layers including post-translational Netherlands eScience (ASDI.2020.014) to C.R.J. and T.V.P., and National
modifications, metabolites, and spatial refinement using laser Key R&D Program of China (grant no. 2021YFA1301600) to T.G.
capture microdissection could enhance our mechanistic under-
standing. Robust, reproducible, and high-throughput proteome AUTHOR CONTRIBUTIONS
measurements of tumor resection material and needle biopsies
in clinical real-time will enable proteomics to move into clinical
Conceptualization, C.R.J. and T.G.; samples, B.A.W., B.S., C.S., D.d.J., D.
K.-L., D.N., E.G., G.J.L.H.v.L., G.K., H.W.M.vL., I.V.B., J.C., J.L., J.N.M.I., J.
applications. The observation that immune consensus cluster
P.M., J.P.P.M., J.W.M.M., M.F.B., M.L., M.M., M.Y., N.C.T.v.G., R.D.M.S.,
classification could predict survival more significantly than R.E.K., R.H.B., T.L., T.Y.S.L.L., V.C., W.v.H., J.J., and X.Z.; methodology, B.
CMS subtyping awaits further validation, and immunohistochem- S., J.L., M.L., R.R.d.G.-d.H., S.R.P., and T.S.; software, J.C.K., M.L., and T.
istry of key markers or MS of an independent cohort would be of V.P.; validation, M.L. and T.V.P.; formal analysis, A.V.-M., A.H., F.B., F.R., I.
high interest. Our findings show the value of high-throughput pro- V.B., J.A., J.C.K., M.L., M.N.M., and T.V.P.; resources, J.K. and T.G.; data cu-
teome profiling for tumor characterization, uncovering cancer
ration, F.R., J.C.K., and M.L.; writing–original draft, C.R.J., F.B., J.C.K., M.L.,
M.N.M., T.G., and T.V.P.; writing–review and editing, C.R.J., J.C.K., T.G.,
heterogeneity with potential clinical implications.
and all co-authors; visualization, A.V.-M., F.B., F.R., F.Z., I.V.B., J.C.K., J.K.,
M.L., M.N.M., S.R.P., and T.V.P.; supervision, C.R.J. and T.G.; funding acqui-
Limitations of the study sition, C.R.J. and T.G.
The TPCA dataset encompasses diverse tissues, processed
with different methods, and analyzed in different laboratories in DECLARATION OF INTERESTS
separate batches, thus batch effects may arise. However,
T.G. is a shareholder of Westlake Omics Inc.; M.F.B. has received research
HeLa reference samples measured in different batches showed
funding from Celgene, Frame Therapeutics, and Lead Pharma and has acted
clustering that was independent of the laboratory that generated as consultant to Servier, Olympus, and Wholomics; R.D.M.S. is a minority
the data. Importantly, blood, liver, and prostate cancers for shareholder of Self-screen BV and received consultancy fee from
which data were generated in multiple laboratories largely clus- AstraZeneca.
tered together in UMAP and hierarchical clustering.
While developing a cancer classifier, we did not remove test STAR★METHODS
samples from the data used for feature selection of the model.
Although we have shown the potential of the classifier using
Detailed methods are provided in the online version of this paper and include
the following:
four external datasets, two harboring metastatic tumors, this
could cause overfitting and should be taken into account. Future • KEY RESOURCES TABLE
validation in larger, independent cohorts is also needed to • EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS
address potential tumor heterogeneity. ○ Human sample collection
Furthermore, although the majority of the TPCPA cancer type
• METHOD DETAILS
cohorts encompass ≥30 samples, some sample counts are
○
○
S
D
a
IA
m
L
p
C
le
- M
pr
S
o
/
c
M
es
S
sing
considerably lower, which could raise concerns about statistical ○ General bioinformatics
power. Nevertheless, we are still able to identify promising can- ○ Overview analyses of the pan-cancer proteome atlas including
cer type-enriched proteins and signatures for all cancer types UMAP, hierarchical clustering and ssGSEA
with >10 samples, as well as an immune consensus cluster clas- ○ E3 ubiquitin ligase analysis in the TPCPA data portal
sifier for CRC, which await further validation in the future. ○ Weighted gene Co-expression network analysis
○ Analyses on infiltrating immune cell types
○ Analyses for individual cancer types
RESOURCE AVAILABILITY ○ Colon cancer CMS subtype analysis
○ Survival analysis
Lead contact ○ Cancer type classifier
Requests for information/resources should be directed to the lead contact, ○ TPCPA data portal
Connie Jimenez (c.jimenez@amsterdamumc.nl). • QUANTIFICATION AND STATISTICAL ANALYSIS
Cancer Cell 43, 1328–1346, July 14, 2025 1341
