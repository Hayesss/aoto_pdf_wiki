---
source_path: /mnt/c/Users/Administrator/Zotero/storage/862THS69/Dalangood 等。 - 2020 - Identification of glycogene-type and validation of.pdf
ingested: 2026-04-23
sha256: ef1dbf0cc8376962
---

Theranostics 2020, Vol. 10, Issue 22 10078
Ivyspring
International Publisher Theranostics
2020; 10(22): 10078-10091. doi: 10.7150/thno.48711
Research Paper
Identification of glycogene-type and validation of
ST3GAL6 as a biomarker predicts clinical outcome and
cancer cell invasion in urinary bladder cancer
Sumiya Dalangood1,2*, Zhen Zhu1*, Zhihui Ma2,3, Jiaxuan Li1, Qinghe Zeng2,3, Yilin Yan4, Bing Shen4, Jun
Yan5,6 and Ruimin Huang2,3
1. MOE Key Laboratory of Model Animals for Disease Study, Model Animal Research Center of Nanjing University, Nanjing 210061, China.
2. State Key Laboratory of Drug Research, Shanghai Institute of Materia Medica, Chinese Academy of Sciences, Shanghai 201203, China.
3. University of Chinese Academy of Sciences, Beijing 100049, China.
4. Department of Urology, Shanghai General Hospital, Shanghai Jiaotong University School of Medicine, Shanghai 200080, China.
5. Department of Laboratory Animal Science, Fudan University, Shanghai 200032, China.
6. Model Animal Research Center of Nanjing University, Nanjing 210061, China.
*These authors contributed equally to this article.
 Corresponding authors: Jun Yan, Ph.D., Department of Laboratory Animal Science, Fudan University, Shanghai 200032, China; Phone: 86-21-54237454;
E-mail: yan_jun@fudan.edu.cn. Ruimin Huang, Ph.D., Shanghai Institute of Materia Medica, Chinese Academy of Sciences, Shanghai 201203, China; Phone:
86-21-50817066; E-mail: rmhuang@simm.ac.cn.
© The author(s). This is an open access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/).
See http://ivyspring.com/terms for full terms and conditions.
Received: 2020.05.26; Accepted: 2020.07.27; Published: 2020.08.08
Abstract
Background: Urinary bladder cancer (UBC) is one of the most common causes of morbidity and mortality
worldwide characterized by a high risk of invasion and metastasis; however, the molecular classification
biomarkers and underlying molecular mechanisms for UBC patient stratification on clinical outcome need to be
investigated.
Methods: A systematic transcriptomic analysis of 185 glycogenes in the public UBC datasets with survival
information and clinicopathological parameters were performed using unsupervised hierarchical clustering.
The gene signature for glycogene-type classification was identified using Limma package in R language, and
correlated to 8 known molecular features by Gene Set Variation Analysis (GSVA). The clinical relevance and
function of a glycogene was characterized by immunohistochemistry in UBC patient samples, and quantitative
RT-PCR, Western blotting, promoter activity, MAL II blotting, immunofluorescence staining, wound healing,
and transwell assays in UBC cells.
Results: A 14-glycogene signature for glycogene-type classification was identified. Among them, ST3GAL6, a
glycotransferase to transfer sialic acid to 3’-hydroxyl group of a galactose residue, showed a significant negative
association with the subtype with luminal feature in UBC patients (n=2,130 in total). Increased ST3GAL6 was
positively correlated to tumor stage, grade, and survival in UBCs from public datasets or our cohort (n=52).
Transcription factor GATA3, a luminal-specific marker for UBC, was further identified as a direct upstream
regulator of ST3GAL6 to negatively regulate its transactivation. ST3GAL6 depletion decreased MAL II level, cell
invasion and migration in 5637 and J82 UBC cells. ST3GAL6 could reverse the effects of GATA3 on global
sialylation and cell invasion in SW780 cells.
Conclusions: Herein, we successfully identified a novel 14-gene signature for glycogene-type classification of
UBC patients. ST3GAL6 gene, from this signature, was demonstrated as a potential biomarker for poor
outcomes and cell invasion in UBCs.
Key words: glycogene, ST3GAL6, urinary bladder cancer, clinical outcome, invasion
Introduction
Urinary bladder cancer (UBC) is one of the most worldwide characterized by a high risk of invasion,
common causes of morbidity and mortality metastasis and recurrence [1]. These tumors are
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10079
staged using the Tumor-Node-Metastasis (TNM) initiation, progression and metastasis [19]. The de novo
system, as non-muscle-invasive bladder cancer expression of certain antigens such as sialyl Lewis A
(NMIBC; Tis, Ta, and T1) and muscle-invasive (sLeA) and sialyl Lewis X (sLeX) are frequently
bladder cancer (MIBC; T2, T3, and T4) according to detected in many cancers, and associated with poor
the extent of invasions. Ta tumors are restricted to the prognosis [20]. For instance, CA19-9 is a sLeA-type
urothelium; T1 tumors have invaded the lamina glycan epitope, serves as a routine serum biomarker
propria; and T2, T3, and T4 tumors have invaded the for pancreatic and gastric cancers [21]. Dysregulated
superficial muscle, perivesical fat, and surrounding glycosyltransferases, such as sialyltransferase [22], at
organs, respectively [2]. UBCs could be graded the level of transcription and/or post-transcription
according to cellular characteristics as papillary were associated with cancer cell invasion [23],
urothelial neoplasm of low malignant potential migration and chemoresistance [24]. It is thus
(PUNLMP), low grade and high grade papillary intriguing and important to identify the glycogene-
urothelial carcinoma in the 2004 WHO/ISUP criteria type and/or glycosyltransferases as the biomarkers
[3]. Current prognostication and clinical management for molecular stratification in UBCs.
are highly based on above basic histopathologic Herein, we divided UBC patients into four
evaluation. glycogene-type based subtypes with different clinical
The intratumoral and intertumoral heterogeneity outcomes, using the transcriptomic data and clinical
at the genomic, transcriptional and cellular levels information from multiple public UBC datasets. A
contribute to the capricious outcomes of UBC patients 14-glycogene signature was then successfully
[4]. Even the pathologically similar, the intrinsic identified to predict the outcomes of UBC patients.
molecular and genetic events were quite different; After the comparison with the known subtype
thus, a number of groups used gene expression markers, ST3GAL6 (a sialyltransferase) was selected
patterns to reveal the molecular subtypes which because it was downregulated in the luminal subtype
traverse stage and grade classification [5-10]. For and upregulated in the non-luminal subtypes, as a
MIBCs, the luminal-like subtype was characterized by promising biomarker for poor prognosis of UBCs. We
the expression of transcription factors and markers for further demonstrated that ST3GAL6 was negatively
differentiation (GATA3, FoxA1 and KRT20) [11, 12]; regulated by a luminal-specific transcription factor
whereas, the basal-like subtype was enriched with GATA3, and knockdown its expression suppressed
cancer stem cell, mesenchymal-like markers (KRT14, the invasion capability of UBC cells.
KRT5, CD44, and Snails) and squamous
Methods
differentiation markers (TGM1 and PI3) [9]. Such
molecular classification helps to a precise prediction
Unsupervised hierarchical clustering and
of UBC outcomes and therapeutic interventions. For
assembly of the TCGA and GEO datasets
example, the luminal subtype with papillary feature
Gene expression and clinical data from the UBC
had the longest 5-year survival; the luminal subtype
cohort in TCGA database (TCGA-BLCA) were
with EMT feature and basal subtype with squamous
downloaded from Genomic Data Commons Data
differentiation feature had second survival
Portal (https://portal.gdc.cancer.gov/). The FPKM
performance; the subtype with neuroendocrine
expression of each gene was applied with
feature had the worst clinical outcomes [9]. However,
Log(1+FPKM) and normalized with Z-score
complexity of the bioinformatics, diversity of the
(mean-centered). Gene expression and clinical data
subtypes, even labor and cost for the microarray
from MSK (JCO 2013) dataset were collected from
analyses hurdle the clinical practice of molecular
Cbioportal (https://www.cbioportal.org/) [25-27].
taxonomy stratification in UBCs [7, 13, 14]. A novel
Medium expression of genes from this dataset was
clinical- and molecular-related biomarker for UBC
applied in the following analysis. Other public
outcomes is urgently needed.
microarray data as well as the corresponding clinical
Glycosylation represents a post-translational
data were obtained from the Gene Expression
modification that involves the enzymatic linkage of
Omnibus (GEO) database (http://www.ncbi.nlm.nih.
monosaccharides or whole oligosaccharides (glycans)
gov/geo). Gene expression in GEO were normalized
to specific amino acids within proteins [15, 16]. The
with Z-score (mean-centered). In the case one gene
glycosylation-related genes, including glycosyl-
with the multiple probes, the averaged expression
transferases, glycosidases, and nucleotide sugar
was used. 185 glycogenes were obtained from the
synthesis and transporter genes, are named as
glycogene database (GGDB, https://acgg.asia/
"glycogenes" and equivalent to 1% of human genome
ggdb2/) and the previous reports [18, 28, 29].
[17, 18]. As a potential cancer hallmark, aberrant
glycosylation plays an important role in tumor
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10080
Unsupervised hierarchical clustering of TCGA conjugated antibody. The slides were visualized by
and GEO datasets were indicated in Morpheus DAB visualization kit (DAB-0031; Maixin_Bio, China),
(https://software.broadinstitute.org/morpheus) by counterstained with hematoxylin. Images were
Average Linkage method with One minus Pearson acquired by a slide scanner (NanoZoomer 2.0-HT;
correlation. Different expressed genes in TCGA-BLCA HAMMATSU, Japan) and analyzed by NDP Serve
dataset were analyzed using Limma, an R package slide distribution and management software
using the linear models to assess the differential (HAMMATSU). IHC slides were evaluated by two
expression, based on the Log(1+FPKM). Glycogenes pathologists independently. The highest intensity was
exhibited remarkable differential expression between initially scored as 5 and the lowest was scored as 1;
B1 subcluster and other subclusters (A1, A2 and B2; and the final score of the ST3GAL6 staining was the
Log Fold Change > 1.5, p < 0.05, and FDR < 0.01) and multiplication of the intensity value and the positive
2
the confirmation study was performed in other three ratio value [33].
independent datasets (MSK (JCO 2013), GSE13507,
Cell culture and reagents
and GSE32894).
To investigate the relationship between UBC cell lines, including RT4, RT112, 5637, J82,
glycogene-types and molecular features, data from 12 T24, SW780, UMUC-3, UMUC-14 and HT1376 were
independent datasets (TCGA-BLCA, MSK (JCO 2013), obtained from Cell Bank of Type Culture Collection,
GSE13507, GSE32894, GSE48276, GSE128702, Chinese Academy of Sciences (Shanghai, China).
GSE48075, GSE87304, GSE32584, GSE31684, UMUC-3, UMUC-14 and HT1376 cells were
GSE128192 and GSE3167; n=2,130 in total) were maintained with EMEM medium and other cells were
analyzed using Gene Set Variation Analysis (GSVA) cultured with RPMI1640 medium at 37 °C in a
[30]. Gene sets for luminal markers (CYP2J2, ERBB2, humidified atmosphere of 5% CO 2 . Both medium
ERBB3, FGFR3, FOXA1, GATA3, GPX2, KRT18, contained 10% FBS and penicillin/streptomycin
KRT19, KRT20, KRT7, KRT8, PPARG, XBP1, UPK1A, (Invitrogen, USA). Knockdown experiments were
and UPK2), basal markers (CD44, CDH3, KRT1, conducted using siRNAs targeting ST3GAL6 or
KRT14, KRT16, KRT6B, and KRT6C), squamous- GATA3 or negative control (siNC) with
differentiation markers (DSC1, DSC2, DSC3, DSG1, Lipofectamine RNAiMAX reagent (Invitrogen),
DSG2, DSG3, S100A7, and S100A8), epithelial- according to manufacturer's instructions. Knockdown
mesenchymal markers (ZEB1, ZEB2, VIM, SNAIL, experiment using shRNAs were performed as
TWIST1, FOXC2, and CDH2), Claudin-low markers previously reported [32]. shRNA plasmids targeting
(CLDN3, CLDN7, CLDN4, CDH1, VIM, SNAI2, ST3GAL6 were generated using the lentiviral pLKO.1
TWIST1, ZEB1, and ZEB2), p53-like markers (ACTG2, backbone with puromycin resistance. The sequences
CNN1, MYH11, MFAP4, PGM5, FLNC, ACTC1, DES, for each siRNA and shRNA were listed in Table S1.
and PCP4), neuroendocrine markers (CHGA, CHGB,
RNA extraction and quantitative Reverse
SCG2, ENO2, SYP, and NCAM1), and cancer-stem cell
Transcription PCR (qRT-PCR) analyses
markers (CD44, KRT5, RPSA, and ALDH1A1) were
After total RNAs were extracted from UBC cells
adapted from the previous reports [9, 31].
by Trizol reagent (Invitrogen), 2 μg of total RNA was
Patient sample collection and reverse transcribed to cDNA by the QuantiTect
immunohistochemistry (IHC) Reverse Transcription Kit (QIAGEN, USA). RT-PCR
Fifty-two patients who initially diagnosed as analyses were performed by AceQ Universal SYBR
primary UBC were enrolled and samples were qPCR Master Mix (Q511-02; Vazyme, China) on
collected after surgery in Shanghai General Hospital LightCycler 96 detection system (BioRad, USA).
(Shanghai, China). This study was approved by the Primers for qRT-PCR were listed in Table S1. mRNA
Institutional Review Board of Shanghai General expression levels were determined by the 2-ΔΔct
Hospital, with the written informed consent from the method and relative mRNA levels of interested genes
corresponding patients. The formalin-fixed paraffin were normalized to β-actin mRNA level. Each
embedded tissues were cut and 5 μm-thick sections experiment was repeated three times.
were collected on super-frost, positively charged glass
Western blotting
slides. IHC was carried out as described previously
Total protein was extracted using RIPA lysis
[32]. Briefly, after antigen retrieval by autoclave in
buffer supplemented with EDTA-free Protease
citrate buffer at pH 6, sections were incubated with
Inhibitor Cocktail (#4693132001; Roche, Germany),
primary anti-ST3GAL6 antibody (1/100, ab106527;
and were boiled in SDS loading buffer. 10 μg protein
Abcam, USA) overnight at 4 °C, followed by the
was separated by 10% SDS-PAGE, followed by
incubation with the horseradish peroxidase (HRP)-
transferring onto 0.45 μm nitrocellulose membranes
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10081
(Millipore, USA). The membranes were blocked with Promoter activity assay
5% non-fat milk in PBST and incubated with primary
For promoter analysis assay, the fragment of
antibodies against ST3GAL6 (1/500, ab106527;
human ST3GAL6 gene promoter containing wild-type
Abcam), GATA3 (1/500, #558686; BD, USA), EGFR
(WT) GATA3 binding site was cloned into pGL3-Basic
(1/1000, #4267; Cell Signaling Technology (CST),
luciferase reporter vector (Promega, USA), and the
USA), phospho-EGFR (Tyr1068) (1/1000, #3777; CST),
reporter containing the mutant (MT) GATA3 binding
AKT (pan) (1/1000, #4691; CST), phospho-AKT
site was then generated using Mut Express II Fast
(Ser473) (1/1000, #4060; CST), p44/42 MAPK
Mutagenesis Kit V2 (C214-02; Vazyme). The human
(ERK1/2) (1/1000, #4695; CST), phospho-p44/42
GATA3 cDNA was cloned into pCDH-3×FLAG
MAPK (ERK1/2) (Thr202/Tyr204) (1/1000, #4370;
plasmid to obtain GATA3 expression construct. The
CST), STAT3 (1/1000, #9139; CST), phospho-STAT3
primers for cloning were listed in Table S1. The
(Tyr705) (1/1000, #9145; CST), or GAPDH (1/1,000,
pGL3-ST3GAL6-WT-Luc (0.2 μg) or
sc-47724; Santa Cruz Biotechnology, USA) at 4℃
pGL3-ST3GAL6-Mutant-Luc plasmid (0.2 μg) was
overnight. After rinse with PBST three times, the
transfected by Lipofectamine 3000 (Invitrogen) into
membranes were incubated with HRP-conjugated
5637 cells in 24-well plate, along with 1 ng pRL-CMV
anti-rabbit or anti-mouse antibodies (1/5,000; Jackson
plasmid (Promega) and 0.2 μg or 0.4 μg
ImmunoResearch, USA; Table S1), followed by the
pCDH-3×FLAG-GATA3. After 24 h, cell lysates were
detection with the Super Signal West Pico PLUS
collected. Luciferase activities were measured using
Chemiluminescent Substrate (Thermo Scientific,
the dual luciferase reporter assay system (RG027;
USA).
Beyotime Biotechnology) by an In Vivo Imaging
System (IVIS) Spectrum (PerkinElmer, USA). Firefly
Lectin blotting and silver staining
luciferase activity was normalized to renilla luciferase
Protein samples (10 μg) were separated by 10%
activity for the relative promoter activity.
SDS-PAGE and transferred to 0.45 μm nitrocellulose
Experiments were performed in triplicate.
membranes (Millipore). The membranes were
incubated with the biotinylated Maackia amurensis Cell proliferation assay
Lectin II (MAL II; 1/1,000, B-1265; Vector
Cell proliferation was assessed by the Cell
Laboratories, USA) overnight at 4 °C. After rinse with
Counting Kit-8 (CCK-8; Vazyme). Briefly, 2×103
TBST three times, the membranes were incubated
cells/well were plated in 96-well plates and 10 μL
with HRP-conjugated streptavidin (1×, SA-5704;
CCK8 solution was added into each well 2 h before
Vector Laboratories) for 1 h and detected with the
detection at the indicated time points. The absorbance
Super Signal West Pico PLUS Chemiluminescent
at 450 nm (A450) was examined by Synergy H1
Substrate. Silver staining was carried out using Fast
hybrid multi-mode reader (BioTek, USA).
Silver Stain Kit (P0017S; Beyotime Biotechnology,
China). Briefly, after electrophoresis and acid fixation, Wound healing assay
SDS-PAGE gels were impregnated with the 2×105 cells were seeded on a 12-well plate till
Sensitizing solution, followed by washing with confluency. A wound was made by scratching with a
ultrapure ddH 2 O. Gels were placed in the Staining pipette tip, followed by wash with PBS. The wound
solution till the desired band intensity was achieved. closure was captured by a microscope (ECLIPSE Ti;
The Stopper buffer was immediately added directly to Nikon, Japan) at different time points (0 h and 24 h).
the gel to terminate the reaction. The gels were
Transwell assay
photographed.
Invasion assay was performed using Corning
Immunofluorescence staining
BioCoat (Matrigel matrix) Tumor Invasion Systems
Cells were fixed with 4% paraformaldehyde for (FluoroBlok PET Membrane, 8.0 μm; 24-Multiwell)
30 min and permeabilized with 0.5% Triton X-100 for (#354165; Corning, USA). In brief, cells were serum-
20 min. After washed by PBS three times, cells were starved overnight, harvested and re-suspended in the
blocked with 5% BSA for 30 min and then incubated migration medium, a suspension of 2×105 cells in 100
with biotinylated-MAL II (Vector Laboratories) μL of serum-free medium was seeded on top of
overnight at 4 °C. Cells were incubated with FITC- transwell. Complete medium with serum was placed
Avidin (#405101; BioLegend, USA) for 1 h. The cells in the lower compartment of the chamber as a
were washed by PBST and counterstained with 2 chemoattractant. After 24 h, transwells were fixed by
μg/mL Hoechst (#33342; Thermo Scientific) for 5 min. 4% paraformaldehyde and stained by 0.2% crystal
Images were obtained using a fluorescence micro- violet. The cells on the upper side were removed by Q
scope (DM6 B; Leica, Germany). tips. The invasive capacity was evaluated by counting
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10082
the invading cells under a microscope (Nikon). Three 0.0441; Figure 1C). It is indicated that the novel
random fields of view were analyzed for each glycogene expression-
chamber. based profiling (glycogene-type) may also be suitable
for UBC classification with clinical outcomes.
Statistical analysis
To simplify the gene signature to differentiate
Fisher exact test, χ2 test and unpaired t test the subcluster B1 from other three subclusters, 14
(two-tailed) were used among clusters and variables. glycogenes (B4GALNT1, B4GALNT2, CHSY3, FUT7,
Pearson correlation was used to determine the GALNT17, GGTA1P, GLT1D1, GLT8D2, GXYLT2,
correlation between gene and gene or the correlation ST3GAL6, ST6GALNAC5, UGT2B4, UGT2B15, and
between gene and gene sets. Kaplan-Meier survival UGT2B28) were identified to be significantly dys-
curves with log-rank test were applied to analyze regulated in subcluster B1, comparing with the other
overall survival (OS), disease free survival (DFS), and three subclusters, in the TCGA provisional dataset (p
cancer-specific survival. Univariate and multivariate < 0.01; Table S3 and Figure S2A). The 14-glycogene
models were computed using Cox proportional signature enabled the division of the UBC patients by
hazards regression by “survival” and “survminer” in two clusters (14-G Cluster I and II; Figure 1D) with
R package, respectively. Statistical analysis was significant OS differences (p = 0.0002, Figure 1E; and
performed by GraphPad Prisms 8.0 software HR (95% CI) = 1.982(1.380-2.849), p = 0.0002, by
(GraphPad Software Inc., USA) or Bioconductor/R. univariate analysis, Table S4). Another 3 independent
Data were presented as means ± standard deviation datasets, including MSK (JCO 2013; n=50), GSE32894
(SD) from at least three independent experiments. In (n=224) and GSE13507 (n=165), were enrolled to
all analysis, p values less than 0.05 were considered validate this 14-glycogene signature (Figure 1F, 1H,
statistically significant. 1J, and Figure S2B-E). Remarkable differences of OS or
cancer-specific survival also existed between 14-G
Results
Cluster I and 14-G Cluster II in these three datasets (p
< 0.05, Figure 1G, 1I, and 1K; HR (95% CI) =
Molecular classification based on the
2.500(1.133-5.513), p = 0.023, by univariate analysis for
expression pattern of glycogenes correlated to
OS in GSE32894, Table S5; HR (95% CI) =
prognosis of UBC patients
3.447(1.699-6.993), p = 0.001, by univariate analysis for
To investigate whether the abnormal glycogene
cancer-specific survival in GSE13507, Table S6). These
expression defines a molecular subtype of UBC
data indicate the 14-glycogene signature may define
patients, we designed the study with the details
the new subtypes in UBC patients.
shown in Figure S1. An unsupervised hierarchical
clustering was carried out using 185 unique ST3 β-galactoside alpha-2,3-sialyltransferase 6
glycogenes in UBC patients from TCGA-BLCA (ST3GAL6) was negatively correlated to the
(TCGA provisional dataset; n=408). The result subtype with luminal feature in UBC patients
demonstrated that UBC patients can be categorized
The relevance between 14-glycogene signature
into two clusters (A and B) or four subclusters (A1,
and molecular features, such as luminal, basal,
A2, B1 and B2; Figure 1A). UBC patients in this
squamous-differentiation, epithelial-mesenchymal,
dataset have been well defined as five molecular
cancer-stem cell, Claudin-low, p53-like, and neuro-
subtypes, including Luminal papillary (~35%),
endocrine, was analyzed in 12 independent datasets
Luminal infiltrated (~19%), Luminal (~6%), Basal
(n=2,130 in total) using GSVA for the feature scores
squamous (~35%), and Neuronal (~5%), based on the
respectively. Because only 8 from the 14 glycogenes
mRNA expression pattern combining BayesNMF with
with complete probe information in all datasets,
a consensus hierarchical clustering approach [9]. The
correlations between mRNA expression levels of these
strong correlation between our four- subcluster and
8 genes and above 8 feature scores were then
above five-subtype classification was observed
determined by Pearson correlation test. Notably,
(Figure 1A). The association between subcluster B1
ST3GAL6 gene expression showed a negative
and Luminal papillary subtype, as well as the
association with luminal feature, along with positive
association between subcluster A2 and Basal
associations with other features (including basal
squamous subtypes were especially notable. In
feature) in the majority of 12 datasets (Figure 2 and
addition, the patients in subcluster B1 were negatively
Figure S3). An individual glycogene, ST3GAL6, as a
associated with tumor grade (p < 0.0001) and tumor
potential classification candidate for UBC patients is
stage (p < 0.0001; Table S2), and showed significantly
suggested.
better prognosis than other subclusters for all stages
(I-IV) (p = 0.0043; Figure 1B) or for stages II-III (p =
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10083
Figure 1. Identification of glycogene-based subtypes in UBCs. A, Unsupervised clustering analysis using 185 glycogenes divided the UBC patients from TCGA
provisional dataset (n=408) into two clusters (Cluster A and B) or four subclusters (A1, A2, B1, and B2). Five molecular subtypes were also indicated. B-C, Kaplan-Meier plot
of overall survival of UBC patients (Stage I-IV, B; Stage II-III, C) in TCGA provisional dataset, comparing that in subcluster B1 with other three subclusters (A1, A2 and B2). D,
F, H, and J, A 14-glycogene signature, which was identified to be significantly dysregulated in subcluster B1 comparing with subclusters A1, A2 and B2 in TCGA provisional dataset
(Figure S2A), allowed the glycogene-based classification (14-G Cluster I and II) in UBC patients from TCGA provisional (D), MSK (JCO 2013, F), GSE32894 (H) and GSE13507
(J) datasets. E, G, I, and K, Kaplan-Meier plot of overall survival or cancer-specific survival of UBC patients from TCGA provisional (E), MSK (JCO 2013, G), GSE32894 (I) and
GSE13507 (K) datasets, by glycogene-type classification as 14-G Cluster I and II.
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10084
Figure 2. The correlations between mRNA expressional levels of 14-glycogene signature and molecular features in UBC patients. Pearson correlation
analyses (r value, A) with the statistical significance of correlation (p value, B) were performed between the expression levels of 8 glycogenes from the 14-gene signature with
the complete probe information and 2 molecular features (Luminal and Basal) in 12 independent cohorts (n=2,130 in total). Colored-blocks in the heatmaps represented the
glycogenes with upregulation (in red) or downregulation (in blue), respectively.
cancer-specific survival in all 3 datasets (n=707 in
Increased expression of ST3GAL6 was
total, p < 0.05; Figure 3K-M), respectively.
associated with poor prognosis in UBC
Furthermore, we collected 52 UBC specimens
patients
(IHC cohort) to validate the results from public
To further validate whether ST3GAL6 was datasets. IHC staining showed that ST3GAL6 protein
involved in UBC development, 6 datasets with tumor was mainly located in the cytosol of UBC cells (Figure
stage information (n=1,268 in total) and 5 from these 6 3O). High ST3GAL6 protein level was also
datasets with tumor grade information (n=1,124 in significantly associated with tumor grade (p = 0.029;
total) were analyzed. ST3GAL6 mRNA expression Table S7) and poor OS (p = 0.0181, Figure 3N; HR
was significantly elevated in high stages (T2-4), (95% CI) = 2.951(1.149-7.579), p = 0.025, by univariate
compared with that in low stages (Ta+T1 or Tis+T1) (p analysis for OS, Table S8).
< 0.01; Figure 3A-E). Even in the MIBC subgroup In summary, increased expression of ST3GAL6
within the TCGA provisional dataset, we observed gene was demonstrated to be correlated to poor
that ST3GAL6 mRNA expression was much higher in prognosis in UBC patients from both public datasets
Stage III or Stage IV than that in Stage II (p < 0.001; and our own cohort.
Figure 3F). Overexpressed ST3GAL6 in high grade
Negative correlation of expression levels
UBCs was also shown (p < 0.05; Figure S4A-E). In the
between ST3GAL6 and GATA3 in UBC
TCGA provisional dataset, up-regulation of ST3GAL6
patients and cells
was observed in UBC patients with lymph node
metastasis (≥N1; n=128) or with recurrence (Recurred; It is important to explore which upstream factors
n=141), comparing to those without lymph node regulate the expression of ST3GAL6 gene. Since our
metastasis (N0; n=235, p < 0.05; Figure S4F) or without results suggested a negative association between
recurrence (DiseaseFree; n=178, p < 0.01; Figure S4G), ST3GAL6 mRNA expression and UBC patients with
respectively. luminal feature (Figure 2), we analyzed the expression
We also tested whether ST3GAL6 expression levels of ST3GAL6 mRNA in TCGA provisional and
level was associated with patients’ outcomes. The GSE87304 datasets which had molecular classification
patients were divided into two groups, with low or information. Significantly lower ST3GAL6 expression
high expression of ST3GAL6, using median values as was shown in all luminal-related subtypes (Luminal,
the cutoff points. The Kaplan-Meier survival analysis Luminal papillary, and Luminal infiltrated; n=246 in
showed that the ST3GAL6 expression level was total), compared with that in Basal squamous subtype
inversely associated with OS in all 4 datasets (n=739 (n=142) (TCGA provisional dataset, p < 0.001; Figure
in total, p < 0.05; Figure 3G-J) and disease-free/ 4A). Similar result was observed between the Luminal
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10085
subtype (n=118) and Basal subtype (n=84) (GSE87304 GSE13507, r = -0.52 for GSE31684, r = -0.60 for
dataset, p < 0.001; Figure 4D). Thus, the luminal GSE32584, r = -0.55 for GSE32894, and r = -0.66 for
subtype-specific transcriptional factors whose GSE48075; p < 0.001; Figure 4C, 4F and Figure S5).
expression level was negatively associated with Whether GATA3 directly regulates ST3GAL6
ST3GAL6 mRNA level were investigated in 7 gene expression at transcriptional level was further
independent datasets. GATA3, which was up- investigated. GATA3 and ST3GAL6 protein levels
regulated in Luminal-related subtypes and down- were examined in 9 UBC cell lines. We found that
regulated in Basal-related subtypes (p < 0.001; Figure GATA3 was relatively higher expressed in two
4B and 4E) [11], was identified because of the negative luminal-type UBC cell lines (RT4 and SW780), but
correlation with ST3GAL6 expression (r = -0.52 for lower in basal-type 5637 cells [11]; while ST3GAL6
TCGA provisional, r = -0.35 for GSE87304, r = -0.56 for was expressed relatively lower in RT4 and SW780
Figure 3. The association of ST3GAL6 expression and clinical features. A-F, The correlations between ST3GAL6 mRNA levels and tumor stage of UBC patients from
GES13507 (A), GES31684 (B), GES32584 (C), GES32894 (D), GES48075 (E), and TCGA provisional (F) datasets. G-J, Kaplan-Meier plot of overall survival of UBC patients in
TCGA provisional (G), GES13507 (H), GSE31684 (I) and GSE48075 (J) datasets, stratified by ST3GAL6 expression. K-M, Kaplan-Meier plot of disease-free survival or
cancer-specific survival of UBC patients in TCGA provisional (K), GES13507 (L), and GSE32894 (I) dataset, stratified by ST3GAL6 expression. N, Kaplan-Meier plot of
cumulative overall survival of UBC patients in our IHC cohort, using the mean value of ST3GAL6 IHC staining scores as the cutoff point. O, IHC staining of ST3GAL6 in UBC
patients. The representative images for different staining intensities were shown. ***, p < 0.001; **, p < 0.01.
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10086
cells, but higher in 5637 cells (Figure 4G). Knocking promoter fragment containing the wildtype (WT) or
down GATA3 by siRNAs, upregulated ST3GAL6 mutant GATA binding site (Figure 4J). Ectopically
mRNA and protein in RT4 and SW780 cells by expressed GATA3 decreased the luciferase activity of
quantitative RT-PCR (p < 0.001; Figure 4H) and ST3GAL6 WT reporter, but not mutant reporter, in
Western blotting (Figure 4I), respectively. Moreover, a 5637 cells (p < 0.05; Figure 4K) and 293T cells (p <
conserved putative GATA3 binding site was found in 0.001; Figure S6D). These results indicated that
the intron 1 of ST3GAL6 gene locus (Figure S6A-C), ST3GAL6 is a direct target of transcriptional factor
whose location was similar to the reported GATA3 GATA3, which may repress ST3GAL6 expression in
target genes, such as ITM2A [34]. ST3GAL6 luciferase luminal-related subtypes of UBCs.
reporters were generated, driven by the ST3GAL6
Figure 4. The correlation of GATA3 and ST3GAL6 expression in UBC samples and cells. A-C, The mRNA levels of ST3GAL6 (A) and GATA3 (B) in four subtypes,
along with their Pearson correlation (C) in UBC patients from TCGA provisional dataset. D-F, The mRNA levels of ST3GAL6 (D) and GATA3 (E) in four subtypes, along with
their Pearson correlation (F) in UBC patients from GSE87304 dataset. G, The protein levels of ST3GAL6 and GATA3 in 9 UBC cell lines by Western blotting. H-I, mRNA and
protein expression levels of ST3GAL6 and GATA3 in SW780 and RT4 cells transfected with siRNAs targeting GATA3 (siGATA3-1 or -2) or control siRNA (siNC), detected by
qRT-PCR (H) and Western blotting (I), respectively. J, Sequences for ST3GAL6 luciferase reporters, ranging between 13,614 and 14,255 bp from the transcriptional start site of
ST3GAL6 (NM_001323360). Wildtype (WT, in blue) and mutant (in orange) GATA binding sites were indicated. K, The activities of ST3GAL6 luciferase reporters (WT and
mutant) in the presence of GATA3 expression plasmids (0.2 and 0.4 µg/well) from 5637 cells in 24-well-plate, normalized by activities of co-transfected pRL-CMV. Data were
presented as mean ± SD of three independent experiments; ***, p < 0.001; *, p < 0.05.
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10087
Figure 5. Biological effects of ST3GAL6 depletion in UBC cells. A-B, mRNA and protein expression levels of ST3GAL6 gene in 5637 and J82 cells transfected with
siRNAs targeting ST3GAL6 (siST3GAL6-1 or -2) or control siRNA (siNC), detected by qRT-PCR (A) and Western blotting (B), respectively. C, The cell proliferation of 5637
and J82 cells with the depletion of ST3GAL6 by CCK-8 assay. D-E, Global sialylation levels in 5637 and J82 cells transfected with ST3GAL6 siRNAs, detected by MAL II blotting
(D) and immunofluorescence staining (E, upper panel), respectively. The silver staining blots (D) were used as loading controls. Hoechst 33253 was used for the nuclei staining
(E, middle panel). Scale bars, 10 µm. F and H, Cell invasion and migration capacities in 5637 and J82 cells transfected with ST3GAL6 siRNAs, detected by transwell invasion (F)
and wound healing (H) assays, respectively. Scale bars, 50 µm. G and I, Quantifications of images for transwell invasion (F) and wound healing (H) assays. Data were presented
as mean ± SD of three independent experiments; ***, p < 0.001; ns, p ≥ 0.05.
significant effect on cell proliferation (Figure 5C).
ST3GAL6 depletion resulted in the decrease of
Since ST3GAL6 is a member of the sialyl-transferase
global sialylation level and cell invasion
family that could transfer sialic acid to terminal
To understand the biological function of positions on sialylated glycolipids (gangliosides) or to
ST3GAL6 in tumor development, two UBC lines (5637 the N- or O-linked glycosylation, Lectin blotting and
and J82) with relatively high ST3GAL6 protein levels immunofluorescence staining for MAL II were
(Figure 4G) were selected for further analyses. performed to evaluate the transferase activity of
Knockdown of ST3GAL6 by two specific siRNAs ST3GAL6. It was demonstrated that inhibition of
(siST3GAL6-1 and siST3GAL6-2) was confirmed at ST3GAL6 expression led to the decreased signals of
both mRNA (Figure 5A) and protein levels (Figure MAL II on membranes (Figure 5D) and in cells (Figure
5B). However, downregulated ST3GAL6 did not have 5E), indicating that α-2,3 sialylation was suppressed
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10088
in 5637 and J82 cells. It was reported that the Consistently, ST3GAL6 knockdown by shRNAs could
α2,3-sialylation levels of EGFR were significantly also reduce the cell invasion capacity by transwell
decreased in the ST3GAL6 knockout HeLa cells; invasion assay (p < 0.001) (Figure S7B-C).
whereas overexpression of ST3GAL6 sufficiently
ST3GAL6 reversed GATA3’s effects on global
rescued the total α2,3-sialylation levels and α2,3-
sialylation level and cell invasion
sialylation of EGFR [35]. It is well known that down-
stream effects of EGFR signaling include regulations In order to examine whether ST3GAL6 plays a
on three major pathways, RAS-RAF-MEK-ERK, PI3K- key role in luminal specific marker GATA3-associated
AKT and JAK-STAT pathway, resulting in activation cell phenotype, we knocked down GATA3 alone, or
of cell survival, cell proliferation, cell migration and both GATA3 and ST3GAL6 in the luminal-type
invasion [36]; thus, we examined the phosphorylation SW780 UBC cells (Figure 6A and B). The increased
levels of ERK, AKT and STAT3 in ST3GAL6- α-2,3 sialylation by GATA3 depletion was reversed
knockdown 5637 UBC cells by two short hairpin with the knockdown of ST3GAL6 gene, which were
RNAs (shRNAs) targeting different regions of detected by MAL II blotting (Figure 6C) and
ST3GAL6 mRNA (shST3GAL6-1 and shST3GAL6-2). immunofluorescence staining (Figure 6D). In
As Figure S7A shown, the phosphorylation levels of addition, we observed that the loss of GATA3
AKT and STAT3 were decreased remarkably in increased SW780 cell invasiveness; however, co-
ST3GAL6-knockdown cells, compared with those in depletion of ST3GAL6 and GATA3 significantly
shCTL control cells. Interestingly, ST3GAL6 depletion reduced cell invasion compared to GATA3 deletion
by siRNAs could reduce both cell invasion and cell alone (Figure 6E). Different roles of the glycogene
migration using transwell invasion and wound ST3GAL6 in different subtypes of UBC patients for
healing assays, respectively (p < 0.001; Figure 5F-I). tumor progression were indicated (Figure 6F).
Figure 6. ST3GAL6 reversed the increase of UBC cell invasion driven by GATA3 depletion. A-B, mRNA and protein expression levels of GATA3 and ST3GAL6 in
GATA3 siRNA alone or combined with ST3GAL6 siRNA treated SW780 cells, detected by qRT-PCR (A) and Western blotting (B), respectively. C-D, Global sialylation levels
in SW780 cells transfected with GATA3 siRNA (siGATA3) alone or combined with ST3GAL6 siRNA (siST3GAL6), detected by MAL II blotting (C, right panel) and
immunofluorescence staining (D, upper panel), respectively. The silver staining blot (C, left panel) was used as a loading control. Hoechst 33253 was used for the nuclei staining
(D, middle panel). Scale bars, 50 µm. E, Transwell assay showed the cell invasion capacities of SW780 cells transfected with GATA3 siRNA alone or combined with ST3GAL6
siRNA. Scale bars, 50 µm. F, The working model of GATA3/ST3GAL6 axis in different subtypes of UBC, which is associated with glycogene expression and patients’ outcomes.
Data were presented as mean ± SD of three independent experiments; ***, p < 0.001.
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10089
type and amount of glycosylation of cancer cell
Discussion
mainly rely on the activity of glycosyltransferases and
Post-translational modifications including glyco- glycosidases [20, 41], we used an alternative strategy
sylation play key roles in UBC development. In this focusing on the expression levels of glycogenes from
study, to our knowledge, we are the first to provide a the numerous public transcriptomic data, and
global and unbiased approach to identify a novel identified the glycogene, ST3GAL6, as a potential
14-glycogene signature for glycogene-type based biomarker for molecular stratification in UBCs.
classification and prediction of clinical outcomes in ST3GAL6 is one member of the sialyltransferase
UBC patients by integrating the transcriptomic data subfamily, called as ST3Gal (α2,3-ST), which functions
and corresponding survival information. This to transfer sialic acid to 3’-hydroxyl group of a Gal
glycogene-type based classification was validated in a residue [42]. The overexpression of ST3GAL6 has
total number of 962 UBC patients derived from four been reported in multiple cancers, such as breast
independent datasets. From this 14-glycogene cancer, multiple myeloma and hepatocellular
signature, overexpressed ST3GAL6 was further carcinoma, whereas low expression level in their
identified to be positively associated with tumor normal counterparts [43-45]. Dysregulation of
aggressiveness and poor prognosis in UBC patients, ST3GAL6 promoted hepatocellular carcinoma and
from both public datasets and our own cohorts. colon cancer cell proliferation and invasion via
Multiple strategies for molecular classification of PI3K/AKT signaling, enhanced homing and survival
UBCs have been reported [5, 6, 8-10, 37]. Molecular of multiple myeloma in bone marrow niche [45, 46].
subtypes, including luminal, basal, squamous- Forced expression of ST3GAL6 also increased the
differentiation, epithelial-mesenchymal, cancer-stem resistance of gastric cancer cells to a Met tyrosine
cell, Claudin-low, p53-like, and neuroendocrine, kinase receptor inhibitor crizotinib, with the
started to be used for predictions of clinical outcomes compensatory activation of insulin receptor [47]. In
and therapeutic interventions. However, most of this study, we showed that ST3GAL6 expression was
these classifications were based on complicated gene required for UBC cell invasion, but not proliferation.
expression patterns; the underlying molecular Though only a few receptors or ligands on tumor cell
mechanisms are still to be investigated. Herein, we surface have been suggested as candidates for
simplified the expression pattern to a 14-gene ST3GAL6, until recently a study indicated that
signature, and furthermore a glycogene (ST3GAL6), ST3GAL6 was required for the α2,3-sialylation of
whose expression level was negatively correlated EGFR, but not that of integrin β1 in HeLa cells by
with luminal feature, as well as the positive knockout approach [35]. On the contrary, the down-
associations with other features (including basal regulation of ST3GAL6 was observed in hepato-
feature) in the majority of 12 datasets (n=2,130 in cellular carcinoma, and was not associated with the
total). The novel finding that luminal-specific levels of CD75s- and iso-CD75s-ganglioside content
transcriptional factor GATA3 suppressed ST3GAL6 [48]. The complicated role of ST3GAL6 in carcino-
gene transactivation provided a possible mechanistic genesis is suggested; to explain such discrepancy, the
evidence for the negative association between accurate quantitative analysis method, precise
ST3GAL6 mRNA level and the subtype with luminal application to clinical diagnosis and well
feature in UBCs. characterization of the function and putative
Aberrant global glycosylation has been substrates of ST3GAL6 in each cancer type should be
implicated in cancer development and associated with explored.
cell adhesion, invasion and metastasis. The elevated ST3GAL6 is reported to be regulated at multiple
levels of sLeA and sLex, which are essential for the levels. Under hypoxic or inflammatory conditions,
function of selectin ligands in the adhesion of cancer stabilized HIF1α and IL6 or IL8 induced ST3GAL6 at
cells onto the endothelium during metastasis, are transcriptional level in MDA-MB-231 and human
frequently utilized as serum biomarkers for bronchial mucosa cells, respectively [49]. LncRNA
pancreatic cancer [38]. A quantitative and qualitative ST3GAL6-AS1, overlapping with ST3GAL6 at
measure of glycosylation is currently dependent on genomic level, positively regulated its host gene
sequential tandem mass spectrometry analysis ST3GAL6 by recruiting MLL1 protein to enhance
coupled to liquid chromatography and ion mobility H3K4me3 level at ST3GAL6 promoter region [46]. In
spectrometry [39]. However, precise glycan structural addition, ST3GAL6 could also be regulated by
characterization of often isomeric glycans is non-coding RNAs. In liver cancer, miR-26a repressed
challenging to be implemented in biological samples ST3GAL6 at post-transcriptional level through
due to glycan separation, complex glycan mixtures, binding to its 3’UTR [45]. Herein, we added a new
reduced resolution, and even cost [40]. Because the piece of evidence, showing that ST3GAL6 was
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10090
down-regulated by the transcription factor GATA3, research funds from the National Natural Science
which is one of the key factor for the maintenance of Foundation of China (81872373 to JY, 91859106 &
luminal differentiation of urothelial cells [31]. In 81771890 to RH), the National Science & Technology
non-luminal UBC subtypes, the downregulation of Major Project “Key New Drug Creation and
GATA3 may release its repression on ST3GAL6 Manufacturing Program”, China (2018ZX09711002-
promoter activity, induce ST3GAL6 expression and 010-001 to RH), the State Key Laboratory of Drug
thus increase the global sialylation level in UBC cells Research (SIMM2004KF-02 to RH), One Hundred
for more malignant outcomes, such as increased Talent Program of Chinese Academy of Sciences (to
capability for cell migration and invasion (Figure 6F). RH), Wu Jieping Medical Foundation (320.6750.16051
It will be intriguing to identify the substrates of to BS), Shanghai Songjiang Municipal Science and
ST3GAL6 in UBC cells, which may unveil the Technology Commission Natural Science Foundation
molecular mechanism of poor prognosis in ST3GAL6- (17SJKJGG10 to BS) and Shanghai Specialized
active UBC subtype. Research Fund for Integrated Chinese and Western
Medicine in General Hospitals (ZHYY-ZXYJHZX-1-
Conclusions
201705 to BS).
In this study, we successfully identified a novel
Contributions
14-gene signature for glycogene-type classification of
RH, JY and ZZ designed the study. ZZ and JL
UBC patients. ST3GAL6 gene, from this signature,
performed bioinformatics analysis, SD, ZZ, ZM, JL,
was demonstrated to be regulated negatively by a
QZ performed experiments, SD, ZZ, YY analyzed
luminal-specific transcriptional factor GATA3 and
data. YY and BS provided clinical samples and
involved in UBC cell migration and invasion.
information. SD, ZZ, JY, and RH wrote the
ST3GAL6 as a potential biomarker for prediction of
manuscript. JY and RH supervised research.
poor outcomes was also suggested in UBC patients.
Competing Interests
Abbreviations
The authors have declared that no competing
UBC: Urinary bladder cancer; TNM: Tumor-
interest exists.
Node-Metastasis; NMIBC: non-muscle-invasive
bladder cancer; MIBC: muscle-invasive bladder
References
cancer; PUNLMP: papillary urothelial neoplasm of
1. Knowles MA, Hurst CD. Molecular biology of bladder cancer: new insights
low malignant potential; EMT: epithelial to mesen-
into pathogenesis and clinical diversity. Nat Rev Cancer. 2015; 15: 25-41.
chymal transition; sLeA: sialyl Lewis A; sLeX: sialyl 2. Sjödahl G, Eriksson P, Patschan O, Marzouka NA, Jakobsson L, Bernardo C, et
al. Molecular changes during progression from nonmuscle invasive to
Lewis X; ST3GAL6: ST3 beta-galactoside alpha-2,3-
advanced urothelial carcinoma. Int J Cancer. 2020; 146: 2636-47.
sialyltransferase 6; TCGA: The Cancer Genome Atlas; 3. Jones TD, Cheng L. Papillary urothelial neoplasm of low malignant potential:
evolving terminology and concepts. J Urol. 2006; 175: 1995-2003.
GEO: Gene Expression Omnibus; GGDB: glycogene
4. Meeks JJ, Al-Ahmadie H, Faltas BM, Taylor JA 3rd, Flaig TW, DeGraff DJ, et al.
database; NMF: non-negative matrix factorization; Genomic heterogeneity in bladder cancer: challenges and possible solutions to
improve outcomes. Nat Rev Urol. 2020; 17: 259-70.
GSVA: gene set variation analysis; IHC: immuno-
5. Sjödahl G, Lauss M, Lövgren K, Chebil G, Gudjonsson S, Veerla S, et al. A
histochemistry; HRP: horseradish peroxidase; NDP: molecular taxonomy for urothelial carcinoma. Clin Cancer Res. 2012; 18:
3377-86.
nanozoomer digital pathology; qRT-PCR: quantitative 6. Cancer Genome Atlas Research Network. Comprehensive molecular
reverse transcription polymerase chain reaction; MAL characterization of urothelial bladder carcinoma. Nature. 2014; 507: 315-22.
7. Choi W, Czerniak B, Ochoa A, Su X, Siefker-Radtke A, Dinney C, et al.
II: Maackia amurensis Lectin II; WT: wild-type; MT: Intrinsic basal and luminal subtypes of muscle-invasive bladder cancer. Nat
mutant; IVIS: in vivo imaging system; CCK-8: Cell Rev Urol. 2014; 11: 400-10.
8. Hedegaard J, Lamy P, Nordentoft I, Algaba F, Høyer S, Ulhøi BP, et al.
Counting Kit-8; PBS: Phosphate Buffered Saline; OS: Comprehensive transcriptional analysis of early-stage urothelial carcinoma.
Cancer Cell. 2016; 30: 27-42.
overall survival; DFS: disease free survival; SD:
9. Robertson AG, Kim J, Al-Ahmadie H, Bellmunt J, Guo G, Cherniack AD, et al.
standard deviation. Comprehensive molecular characterization of muscle-invasive bladder cancer.
Cell. 2017; 171: 540-556.e25.
10. Batista da Costa J, Gibb EA, Bivalacqua TJ, Liu Y, Oo HZ, Miyamoto DT, et al.
Supplementary Material
Molecular characterization of neuroendocrine-like bladder cancer. Clin Cancer
Res. 2019; 25: 3908-20.
Supplementary figures and tables. 11. Warrick JI, Walter V, Yamashita H, Chung E, Shuman L, Amponsa VO, et al.
http://www.thno.org/v10p10078s1.pdf FOXA1, GATA3 and PPAR cooperate to drive luminal subtype in bladder
cancer: A molecular analysis of established human cell lines. Sci Rep. 2016; 6:
38531.
Acknowledgements 12. Inamura K. Bladder cancer: New insights into its molecular pathology.
Cancers (Basel). 2018; 10: 100.
We would like to thank Junzun Li from Dr. Yan’s 13. Guo Y, Yuan X, Li K, Dai M, Zhang L, Wu Y, et al. GABPA is a master
regulator of luminal identity and restrains aggressive diseases in bladder
lab, Dr. Chengyuan Peng and Yu Dong from Dr.
cancer. Cell Death Differ. 2020; 27: 1862-77.
Huang’s lab and the Institutional Technology Service 14. Vakar Lopez F. Molecular subtyping bladder cancer: Is it ready for clinical
practice? Turk J Med Sci. 2020; Epub ahead of print.
Center of Shanghai Institute of Materia Medica for
15. Stowell SR, Ju T, Cummings RD. Protein glycosylation in cancer. Annu Rev
technical supports. This work was supported by Pathol. 2015; 10: 473-510.
http://www.thno.org
Theranostics 2020, Vol. 10, Issue 22 10091
16. Li J, Xu J, Li L, Ianni A, Kumari P, Liu S, et al. MGAT3-mediated glycosylation 45. Sun M, Zhao X, Liang L, Pan X, Lv H, Zhao Y. Sialyltransferase ST3GAL6
of tetraspanin CD82 at asparagine 157 suppresses ovarian cancer metastasis by mediates the effect of microRNA-26a on cell growth, migration, and invasion
inhibiting the integrin signaling pathway. Theranostics. 2020; 10: 6467-82. in hepatocellular carcinoma through the protein kinase B/mammalian target
17. Montpetit ML, Stocker PJ, Schwetz TA, Harper JM, Norring SA, Schaffer L, et of rapamycin pathway. Cancer Sci. 2017; 108: 267-76.
al. Regulated and aberrant glycosylation modulate cardiac electrical signaling. 46. Hu J, Shan Y, Ma J, Pan Y, Zhou H, Jiang L, et al. LncRNA
Proc Natl Acad Sci U S A. 2009; 106: 16517-22. ST3Gal6-AS1/ST3Gal6 axis mediates colorectal cancer progression by
18. Noda M, Okayama H, Tachibana K, Sakamoto W, Saito K, Thar Min AK, et al. regulating α-2,3 sialylation via PI3K/Akt signaling. Int J Cancer. 2019; 145:
Glycosyltransferase gene expression identifies a poor prognostic colorectal 450-60.
cancer subtype associated with mismatch repair deficiency and incomplete 47. Balmaña M, Diniz F, Feijão T, Barrias CC, Mereiter S, Reis CA. Analysis of the
glycan synthesis. Clin Cancer Res. 2018; 24: 4468-81. effect of increased α2,3-sialylation on RTK activation in MKN45 gastric cancer
19. Vajaria BN, Patel PS. Glycosylation: a hallmark of cancer? Glycoconj J. 2017; spheroids treated with crizotinib. Int J Mol Sci. 2020; 21: 722.
34: 147-56. 48. Souady J, Hülsewig M, Distler U, Haier J, Denz A, Pilarsky C, et al. Differences
20. Gomes C, Almeida A, Barreira A, Calheiros J, Pinto F, Abrantes R, et al. in CD75s- and iso-CD75s-ganglioside content and altered mRNA expression
Carcinoembryonic antigen carrying SLeX as a new biomarker of more of sialyltransferases ST6GAL1 and ST3GAL6 in human hepatocellular
aggressive gastric carcinomas. Theranostics. 2019; 9: 7431-46. carcinomas and nontumoral liver tissues. Glycobiology. 2011; 21: 584-94.
21. Pinho SS, Reis CA. Glycosylation in cancer: mechanisms and clinical 49. Albuquerque APB, Balmaña M, Mereiter S, Pinto F, Reis CA, Beltrão EIC.
implications. Nat Rev Cancer. 2015; 15: 540-55. Hypoxia and serum deprivation induces glycan alterations in triple negative
22. Vajaria BN, Patel KR, Begum R, Patel PS. Sialylation: an avenue to target breast cancer cells. Biol Chem. 2018; 399: 661-72.
cancer cells. Pathol Oncol Res. 2016; 22: 443-7.
23. Hao J, Zeltz C, Pintilie M, Li Q, Sakashita S, Wang T, et al. Characterization of
distinct populations of carcinoma-associated fibroblasts from non-small cell
lung carcinoma reveals a role for ST8SIA2 in cancer cell invasion. Neoplasia.
2019; 21: 482-93.
24. Ou L, He X, Liu N, Song Y, Li J, Gao L, et al. Sialylation of FGFR1 by ST6Gal‑I
overexpression contributes to ovarian cancer cell migration and
chemoresistance. Mol Med Rep. 2020; 21: 1449-60.
25. Cerami E, Gao J, Dogrusoz U, Gross BE, Sumer SO, Aksoy BA, et al. The cBio
cancer genomics portal: an open platform for exploring multidimensional
cancer genomics data. Cancer Discov. 2012; 2: 401-4.
26. Gao J, Aksoy BA, Dogrusoz U, Dresdner G, Gross B, Sumer SO, et al.
Integrative analysis of complex cancer genomics and clinical profiles using the
cBioPortal. Sci Sig. 2013; 6: pl1.
27. Iyer G, Al-Ahmadie H, Schultz N, Hanrahan AJ, Ostrovnaya I, Balar AV, et al.
Prevalence and co-occurrence of actionable genomic alterations in high-grade
bladder cancer. J Clin Oncol. 2013; 31: 3133-40.
28. Narimatsu H. Construction of a human glycogene library and comprehensive
functional analysis. Glycoconj J. 2004; 21: 17-24.
29. Ashkani J, Naidoo KJ. Glycosyltransferase gene expression profiles classify
cancer types and propose prognostic subtypes. Sci Rep. 2016; 6: 26451.
30. Hänzelmann S, Castelo R, Guinney J. GSVA: gene set variation analysis for
microarray and RNA-seq data. BMC Bioinformatics. 2013; 14: 7.
31. Chan KS, Volkmer JP, Weissman I. Cancer stem cells in bladder cancer: a
revisited and evolving concept. Curr Opin Urol. 2010; 20: 393-7.
32. Chang C, Liu J, He W, Qu M, Huang X, Deng Y, et al. A regulatory circuit
HP1γ/miR-451a/c-Myc promotes prostate cancer progression. Oncogene.
2018; 37: 415-26.
33. Thway K, Selfe J, Shipley J. Immunohistochemical detection of glypican-5 in
paraffin-embedded material: an optimized method for a novel research
antibody. Appl Immunohistochem Mol Morphol. 2012; 20: 189-95.
34. Tai TS, Pai SY, Ho IC. Itm2a, a target gene of GATA-3, plays a minimal role in
regulating the development and function of T cells. PLoS One. 2014; 9: e96535.
35. Qi F, Isaji T, Duan C, Yang J, Wang Y, Fukuda T, et al. ST3GAL3, ST3GAL4,
and ST3GAL6 differ in their regulation of biological functions via the
specificities for the α2,3-sialylation of target proteins. FASEB J. 2020; 34:
881-97.
36. An Z, Aksoy O, Zheng T, Fan QW, Weiss WA. Epidermal growth factor receptor
and EGFRvIII in glioblastoma: signaling pathways and targeted therapies.
Oncogene. 2018; 37: 1561-75.
37. Dadhania V, Zhang M, Zhang L, Bondaruk J, Majewski T, Siefker-Radtke A, et
al. Meta-analysis of the luminal and basal subtypes of bladder cancer and the
identification of signature immunohistochemical markers for clinical use.
EBioMedicine. 2016; 12: 105-17.
38. Fernandes E, Sores J, Cotton S, Peixoto A, Ferreira D, Freitas R, et al.
Esophageal, gastric and colorectal cancers: Looking beyond classical
serological biomarkers towards glycoproteomics-assisted precision oncology.
Theranostics. 2020; 10: 4903-28.
39. Gray CJ, Compagnon I, Flitsch SL. Mass spectrometry hybridized with
gas-phase InfraRed spectroscopy for glycan sequencing. Curr Opin Struct Biol.
2020; 62: 121-31.
40. Yang Y, Vankayalapati H, Tang M, Zheng Y, Li Y, Ma C, et al. Discovery of
novel inhibitors targeting multi-UDP-hexose pyrophosphorylases as
anticancer agents. Molecules. 2020; 25: 645.
41. Kawamura YI, Toyota M, Kawashima R, Hagiwara T, Suzuki H, Imai K, et al.
DNA hypermethylation contributes to incomplete synthesis of carbohydrate
determinants in gastrointestinal cancer. Gastroenterology. 2008; 135:
142-151.e3.
42. Harduin-Lepers A, Recchi MA, Delannoy P. 1994, the year of
sialyltransferases. Glycobiology. 1995; 5: 741-58.
43. Julien S, Ivetic A, Grigoriadis A, QiZe D, Burford B, Sproviero D, et al. Selectin
ligand sialyl-Lewis x antigen drives metastasis of hormone-dependent breast
cancers. Cancer Res. 2011; 71: 7683-93.
44. Glavey SV, Manier S, Natoni A, Sacco A, Moschetta M, Reagan MR, et al. The
sialyltransferase ST3GAL6 influences homing and survival in multiple
myeloma. Blood. 2014; 124: 1765-76.
http://www.thno.org
