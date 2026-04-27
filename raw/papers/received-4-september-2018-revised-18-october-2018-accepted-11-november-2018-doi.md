---
source_path: /mnt/c/Users/Administrator/Zotero/storage/UHRTBDJC/Liu 等。 - 2019 - Amino acid metabolism-related gene expression-base.pdf
ingested: 2026-04-23
sha256: 0c1ba23b8c7e5ab4
---

Received: 4 September 2018 | Revised: 18 October 2018 | Accepted: 11 November 2018
DOI: 10.1111/cas.13878
ORIGINAL ARTICLE
Amino acid metabolism- related gene expression- based risk
signature can better predict overall survival for glioma
Yu-Qing Liu1,2 | Rui-Chao Chai1,2 | Yong-Zhi Wang1,2,3 | Zheng Wang2,3 |
Xing Liu1,2 | Fan Wu1,2 | Tao Jiang1,2,3
1Department of Molecular
Metabolic reprogramming has been proposed to be a hallmark of cancer. Aside from
Neuropathology, Beijing Neurosurgical
Institute, Beijing, China the glycolytic pathway, the metabolic changes of cancer cells primarily involve amino
2Chinese Glioma Genome Atlas Network acid metabolism. However, in glioma, the characteristics of the amino acid
(CGGA), Beijing, China
metabolism-r elated gene set have not been systematically profiled. In the present
3Department of Neurosurgery, Beijing
Tiantan Hospital, Capital Medical University, study, RNA sequencing expression data from 309 patients in the Chinese Glioma
Beijing, China
Genome Atlas database were included as a training set, while another 550 patients
Correspondence within The Cancer Genome Atlas database were used to validate. Consensus cluster-
Fan Wu, Department of Molecular
ing of the 309 samples yielded two robust groups. Compared with Cluster1, Cluster2
Neuropathology, Beijing Neurosurgical
Institute, Beijing, China. correlated with a better clinical outcome. We then developed an amino acid
Email: wufan0510284@163.com
metabolism-r elated risk signature for glioma. Our results showed that patients in the
and
Tao Jiang, Department of Neurosurgery, high- risk group had dramatically shorter overall survival than low-r isk counterparts in
Beijing Tiantan Hospital, Capital Medical
any subgroup, stratified by isocitrate dehydrogenase and 1p/19q status based on the
University, Beijing, China.
Email: Taojiang1964@163.com 2016 World Health Organization classification guidelines. The 30- gene signature
showed better prognostic value than the traditional factors “age” and “grade” by ana-
Funding information
Beijing Natural Science Foundation, Grant/ lyzing the receiver operating characteristic curve with areas under curve of 0.966,
Award Number: 7182076; National Natural
0.692, 0.898 and 0.975, 0.677, 0.885 for 3- and 5- year survival, respectively.
Science Foundation of China, Grant/
Award Number: 81502495, 81672479 and Moreover, univariate and multivariate analysis showed that the 30- gene signature
81773208; Capital Medical Development
was an independent prognostic factor for glioma. Furthermore, Gene Ontology anal-
Research Fund, Grant/Award Number:
2016-1-1072 ysis and Gene Set Enrichment Analysis showed that tumors with a high risk score
correlated with various aspects of the malignancy of glioma. In summary, we demon-
strated a novel amino acid metabolism-r elated risk signature for predicting prognosis
for glioma.
KEYWORDS
amino acid metabolism, CGGA, glioma, prognosis, risk signature
Abbreviations: AUC, area under curve; CGGA, Chinese Glioma Genome Atlas; CI, confidence interval; GBM, glioblastoma; GO, gene ontology; GSEA, gene set enrichment analysis; HR,
hazard ratio; IDH, isocitrate dehydrogenase; KEGG, Kyoto Encyclopedia of Genes and Genomes; LGG, lower-grade glioma; OS, overall survival; ROC, receiver operating characteristic;
TCGA, The Cancer Genome Atlas; WHO, World Health Organization.
Liu and Chai contributed equally to this work.
This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in
any medium, provided the original work is properly cited, the use is non- commercial and no modifications or adaptations are made.
© 2018 The Authors. Cancer Science published by John Wiley & Sons Australia, Ltd on behalf of Japanese Cancer Association.
|
Cancer Science. 2018;1–13. wileyonlinelibrary.com/journal/cas 1
2 | LIU et aL.
1 | INTRODUCTION association between amino acid metabolism- related signature and
prognosis. Finally, GO analysis and GSEA identified that a tumor
Metabolic reprogramming, as both direct and indirect conse- with a higher risk score of amino acid metabolism- related signature
quences of oncogenic mutations, has been proposed to be a was involved in many aspects of tumor progression, including cell
hallmark of cancer.1,2 Amino acid metabolism might represent an division, angiogenesis, cell adhesion and immune response. These
“Achilles heel” in cancer as a number of tumors acquire an altered results might provide a new insight into the research of glioma ma-
dependency on some of these metabolic pathways.3-5 Amino acid lignancy and individual therapy.
metabolism involving serine, glycine and threonine and the carbon
units they provide satisfies cell growth and proliferation, as well
2 | MATERIALS AND METHODS
as the maintenance of cellular redox, genetic and epigenetic sta-
tus.6-8 Also, glutamine, as a super nutrient, plays surprising roles in
2.1 | Samples and data collection
supporting the biological hallmarks of malignancy.9,10 Additionally,
several lines of evidences have shown that an individual amino We retrospectively collected whole- genome RNA- seq expression
acid metabolism- related gene plays a pivotal role in tumor pro- data and corresponding clinical and molecular information from 309
gression. For instance, inhibition of glutaminase (GLS) with siRNA patients (gender, age, IDH mutational status, status of loss of 1p/19q
or small molecule inhibitor preferentially slows growth of glioma and methylguanine methyltransferase [MGMT] promoter methyla-
cells with mutant IDH 1.11 Yue et al12 found that oncogenic MYC tion and survival information) from the CGGA database (http://www.
selectively activates SLC7A5/SLC43A1 transcription and the MYC- cgga.org.cn) as the training set.20,21 Tumor tissue samples were ob-
SLC7A5/SLC43A1 signaling circuit promotes essential amino acid tained from patients with newly diagnosed glioma who were treated
transport and tumorigenesis. ASCT2 (encoded by SLC1A5) is a by the CGGA group. All tissues were independently diagnosed histo-
sodium- dependent neutral amino acid transporter, and pharma- logically by two or more neuropathologists. Only samples containing
cological blockade of ASCT2 with V- 9302 led to attenuated can- above 80% tumor cells were selected for whole- genome expression
cer cell growth, increased cell death and raised oxidative stress, profiling. OS was calculated from the date of diagnosis until death or
which collectively contributed to antitumor responses in vitro and the end of follow up. The study protocol was approved by the ethics
in mouse models in vivo.13 Nevertheless, currently, the character- committee of the Beijing Tiantan Hospital. We selected the TCGA-
istic of the amino acid metabolism- related gene set has not been RNAseq cohort as the validation set, which contains 683 samples
systematically profiled. (http://cancergenome.nih.gov/),22,23 and after eliminating cases in
In our study, we focused on gliomas, the most common form which clinical information was incomplete and lacked prognostic in-
of primary malignant brain tumor, which can be subdivided into formation, 550 samples were retained.
grades II- IV in light of WHO classification. Compared with WHO
Grades II- III, which comprise LGG, GBM WHO IV bears a dismal
2.2 | Bioinformatics analysis
prognosis with median survival rates of 14.6 months.14-16 The
2016 WHO classification of central nervous system (CNS) tumors We carried out consensus clustering with the R programming lan-
combines molecular parameters and histology to define diffuse guage (http://cran.r- project.org) to access expression patterns of
gliomas.17 Based on traditional histopathology but enriched with amino acid metabolism- related genes from the CGGA and TCGA
IDH and 1p/19q codeletion status, gliomas could be classified datasets. GO analysis and KEGG pathway analysis were carried out
into five subtypes (three LGG and two GBM), as follows: (i) LGG in DAVID (http://david.abcc.ncifcrf.gov/home.jsp) for functional an-
with wild- type IDH (LGG- IDHwt); (ii) LGG with IDH mutation and notation of the genes positively and negatively correlated with risk
1p/19q non- codeletion (LGG- IDHmut- noncodel); (iii) LGG with score in the two cohorts.24,25 GSEA (http://www.broadinstitute.
IDH mutation and 1p/19q codeletion (LGG- IDHmut- codel); (iv) org/gsea/index.jsp) was carried out to determine whether con-
GBM with wild- type IDH (GBM- IDHwt); and (v) GBM with IDH firmed gene sets were significantly distinct between the two groups
mutation (GBM- IDHmut).18,19 These five subtypes of glioma show (high risk score vs low risk score).24,26 We evaluated tumor purity
distinct tumor characteristics and OS outcomes. of each sample using the ESTIMATE algorithm, which reflects the
In the present study, we conducted systematic and comprehen- enrichment of stromal and immune cell gene signatures in a tran-
sive research on the characteristics of the amino acid metabolism- scriptional profile.27 Protein- protein interactions among 30 amino
related gene set in glioma. First, we demonstrated that amino acid acid metabolism- related proteins were analyzed using the STRING
metabolism- related gene sets could stratify the clinical and mo- database (http://www.string-db.org/).
lecular characteristics of gliomas, highlighting their significance
in the malignancy of glioma. Then, we developed an amino acid
2.3 | Statistical analysis
metabolism- related signature for glioma patients in the CGGA
RNA sequencing (RNAseq) dataset, and validated in TCGA RNAseq Amino acid metabolism- related gene sets (REACTOME_
dataset. Furthermore, the 30- gene- based risk signature was veri- METABOLISM_OF_AMINO_ACIDS_AND_DERIVATIVES) were first
fied as an independent prognostic factor for gliomas, indicating an extracted from the Molecular Signatures Database v5.1 (MSigDB)
LIU et aL. | 3
(http://www.broad.mit.edu/gsea/msigdb/),20 which contained a had a better prognosis compared with the Cluster2 subgroup
total of 200 genes. After overlapping with genes in CGGA and TCGA (P < .001, log- rank; Figure 1F). These results indicated that amino
RNA- seq datasets, 194 and 196 genes related to amino acid metabo- acid metabolism- related gene sets were involved in the malignancy
lism, respectively, remained. of gliomas and closely related to prognosis of patients. According
Univariate Cox regression analysis was carried out to assess the to the CGGA cohort, TCGA samples were also clearly stratified into
prognostic value of genes associated with amino acid metabolism two different prognostic subgroups (Figure S2F).
and 121 genes correlating with survival (P < 0.05) were selected to
achieve further gene signature selection and risk- based classification
3.2 | Identification of a 30- gene risk signature
in the training datasets. A risk signature was formulated according to
associated with amino acid metabolism
the Least Absolute Shrinkage and Selection Operator (LASSO) re-
gression algorithm.28-30 The penalty parameter λ was chosen based To identify an amino acid metabolism- related gene signature, first,
on 10- fold cross- validation within the training set, which produced we selected 121 genes associated with OS (P < .05) by univariate Cox
the minimum mean cross- validated error for the Cox model. Based regression analysis in the training cohort. Then, by LASSO regres-
on this, 30 genes and their regression coefficients were obtained. sion algorithm, 30 genes were selected as active covariates to evalu-
We then computed the risk score according to the formula followed ate the prognostic value, and the risk scores for the patients in the
in the training and validation datasets. training cohort were obtained (Figure 2A,B). To assess performance
of the signature genes as classifier, we distinguished the training
Riskscore=expr ×coefficient +expr ×coefficient
gene(1) gene(1) gene(2) gene(2)
dataset into high- risk and low- risk groups by using the median risk
+⋯+expr
gene(n)
×coefficient
gene(n) score as the cutoff value, and found a significant difference in the
clinical and molecular features between the two groups (Figure 2C
On the basis of the median risk value, patients were separated and Table 1). In comparison with the low- risk group, patients in the
into high- and low- risk groups in both CGGA and TCGA databases. high- risk group tended to be older (P < .001). As shown in Table 1,
Kaplan- Meier survival curves and the log rank test were exploited classical and mesenchymal subtypes were found in 12.9% and 73.5%
to evaluate the prognostic significance.31 Differences in clinico- of low- risk and high- risk groups, respectively (P < .001). Moreover,
pathological features between groups were tested by Student’s t or we found that GBM accounted for a large proportion, 72.9% of the
chi- squared tests. Multivariate Cox regression analyses were carried total, in the high- risk group, whereas GBM was 12.9% in the low-
out to determine independent prognostic factors, and the statistical risk group (P < .001). We found that 78.6% and 24.5% of samples in
analyses were conducted using SPSS version 16.0 software (SPSS the low- risk and high- risk groups, respectively, were found to carry
Inc., Chicago, IL, USA). P value <.05 was regarded as statistically IDH mutations (P < .001). Loss of chromosome 1p/19q was found
significant. in 24.6% and 3.1% of low- risk and high- risk groups, respectively
(P < .001). Our results also showed that MGMT promoter methyla-
tion was found in 70.6% and 42.8% of low- risk and high- risk groups,
3 | RESULTS
respectively (P < .001).
To validate the 30 amino acid metabolism- related risk signature
3.1 | Stratification of gliomas based on amino acid
in other populations, we formulated the risk scores for each patient
metabolism- related gene sets
in TCGA database based on the 30- gene coefficients derived from
Amino acid metabolism- related gene expression profiling of 309 the training dataset. Consistent with the above results, we also
samples was obtained from the CGGA RNAseq datasets, and we found that there was significant difference between the two groups
analyzed the genes identified as having highly variable expres- in an independent validation cohort (Figure S3 and Table 1). In brief,
sion among the samples. Consensus clustering of the 309 samples compared to the low- risk group, the high- risk group tended to com-
determined two robust clusters with clustering stability increas- prise the patients with poor prognostic features.
ing between k = 2 and k = 10 (Figure 1A- D and Figure S1). We ob-
served that consensus clustering determined striking differences
3.3 | Identification of 30- gene signature for
in the clinical and molecular features of the two glioma subclasses
prognostication in glioma
(Figure 1E, Table S1). In the training cohort, Cluster1 was strongly
linked with older age at diagnosis (median age = 46, P < .001), clas- In view of the close correlation between risk groups and clin-
sical or mesenchymal subtypes (72.3%, P < .001), GBM phenotype icopathological features, we sought to assess the prognos-
(71.8%, P < .001), IDH wild type (72.9%, P < .001) and 1p/19q non- tic value of the risk score. In all gliomas, patients were assigned
codeletion (96.3%, P < .001). Cluster2 cluster mainly represented the to two groups according to the median risk score. Our results
proneural or neural subtypes (92.0%, P < .001), lower grade (88.5%, showed that patients in the high- risk group (n = 155) had dra-
P < .001), and IDH mutational status (81.3%, P < .001). These find- matically shorter OS than their low- risk counterparts (n = 154) in
ings were validated in the TCGA datasets (Figure S2). Furthermore, the training cohort (median OS = 9.0 vs 37.9 months; P < .0001;
OS analysis showed that glioma patients with the Cluster1 subgroup Figure 3A). Moreover, we explored the prognostic value of risk
4 | LIU et aL.
score in gliomas of different grades and found that OS differed significantly between high- risk and low- risk groups in WHO grade
LIU et aL. | 5
FIGURE 1 Amino acid- related gene sets could classify the clinical and molecular features of gliomas. A,B, Consensus clustering matrix
of 309 CGGA samples for k = 2 and k = 3. C, Consensus clustering CDF for k = 2 to k = 10. D, Relative change in area under CDF curve
according to various k values. E, Heat map and clinicopathological features of the two clusters defined by the amino acid- related gene sets.
F, Survival analysis of Cluster 1 and Cluster 2 subgroups in CGGA samples. CDF, cumulative distribution function; CGGA, Chinese Glioma
Genome Atlas; Codel, codeletion; IDH, isocitrate dehydrogenase; MGMT, methylguanine methyltransferase; Noncodel, noncodeletion; OS,
overall survival
FIGURE 2 Identification of 30- gene risk signature for OS by LASSO regression analysis in CGGA datasets. A, Partial likelihood deviance
as function of regularization parameter λ in the training dataset. Each red point marks a λ value along regularization paths, and gray error
bars represent confidence intervals for the cross- validated error rate. Left vertical dotted line marks the minimum error, whereas the right
vertical dotted line marks the largest λ value, the error of which is within 1 SD of the minimum. Horizontal row of numbers above the plot
marks the gene number in each condition upon shrinkage and selection based on linear regression. Results of 30 genes selected and their
regression coefficients by LASSO are shown in (B). C, Heat map shows the association of risk scores and clinicopathological features based
on the 30- gene risk signature. CGGA, Chinese Glioma Genome Atlas; Codel, codeletion; IDH, isocitrate dehydrogenase; LASSO, Least
Absolute Shrinkage and Selection Operator; MGMT, methylguanine methyltransferase; Noncodel, noncodeletion; OS, overall survival;
TCGA, The Cancer Genome Atlas
6 | LIU et aL.
TABLE 1 Correlation between 30- gene- based risk scores and clinicopathological factors of glioma patients in the two cohorts
Training set CGGA RNA- seq cohort (n = 309) Validation set TCGA RNA- seq cohort (n = 550)
Low-r isk score High- risk score
Features (n = 154) (n = 155) P-v alue Low- risk score (n = 275) High- risk score (n = 275) P-v alue
Age
Mean (range) 40 (10- 75) 47 (8- 81) <.001 40 (14- 87) 56 (21- 89) <.001
Gender
Female 62 53 .113 119 112 .390
Male 92 102 156 163
TCGA subtype
Pro 65 34 <.001 237 108 <.001
Neural 69 7 28 5
Classical 17 52 9 132
Mes 3 62 1 30
WHO grade
II 95 9 <.001 160 31 <.001
III 34 33 115 96
IV 25 113 0 148
IDH status
WT 33 117 <.001 17 195 <.001
Mut 121 38 258 80
1p/19q status
Codel 32 4 <.001 134 3 <.001
Noncodel 98 124 141 266
NA 24 27 0 6
MGMT promoter status
Unmethy 32 79 <.001 30 105 <.001
Methy 77 59 245 138
NA 45 17 0 32
Bold type indicates a statistically significant difference ( P value < .05).
CGGA, Chinese Glioma Genome Atlas; Codel, codeletion; IDH, isocitrate dehydrogenase; Mes, mesenchymal; Methy, methylated; MGMT, methylgua-
nine methyltransferase; Mut, mutation; NA, not applicable; Noncodel, noncodeletion; Pro, proneural; TCGA, The Cancer Genome Atlas; Unmethy,
unmethylated; WHO, World Health Organization; WT, wildtype.
II (median OS = 26.5 vs 56.8 months; P = .0024), grade III (median Meanwhile, the signature value showed significant differ-
OS = 11.4 vs 33.6 months; P < .0001) and GBM (median OS = 7.2 vs ences between samples stratified by WHO grade in the CGGA
12.7 months; P < .0001; Figure 3B- D). and TCGA cohorts (Figure 5A and Figure S5A). Such being the
The 2016 update to the WHO proposed a classification strategy case, gliomas were classified into five principal groups on the
and, thus, gliomas were classified into five subtypes based on tradi- basis of IDH status and 1p/19q codeletion status. Based on
tional histopathology and the status of IDH and 1p/19q codeletion. the critical molecular markers IDH and 1p/19q, we investigated the
Given that these five glioma subtypes showed distinct tumor char- distribution of the 30- gene signature in patients stratified by IDH
acteristics and OS outcomes, we determined whether the risk score status among distinct WHO grades (Figure 5B- D and Figure S5B-
had prognostic value in the five various populations. For LGG, survival D) and 1p/19q codeletion status in LGG- IDH mutation patients
time of the high- risk group was remarkably shorter than that of the (Figure 5E and Figure S5E). Verhaak et al32 have identified four clini-
low- risk group in LGG- IDHmut- noncodel (P < .0001; Figure 4A) and cally relevant subtypes (neural, proneural, classical, mesenchymal) of
LGG- IDHwt (P < .0001; Figure 4B), whereas there was no significant GBM characterized by abnormalities in platelet derived growth fac-
difference in LGG- IDHmut- codel (P = .1175; Figure 4C). For both tor receptor alpha (PDGFRA), IDH1, epidermal growth factor recep-
GBM- IDHwt and GBM- IDHmut, there were significant differences in tor (EGFR) and neurofibromin 1 by an integrated genomic analysis.
OS between the two risk groups (P < .0001; P = .0015, respectively; Therefore, we explored the distribution of TCGA subtypes for GBM
Figure 4D,E). in the CGGA and TCGA cohorts (Figure 5F and Figure S5F).
LIU et aL. | 7
FIGURE 3 Prognostic significance of the 30- gene signature- derived risk scores in different WHO grades. Prognosis efficiency of the
30- gene risk signature in all grades (A), grade II (B), grade III (C) and GBM (D) from the CGGA datasets. P- value shown in each panel is
determined by a log- rank test between the two groups. E,F, ROC curves indicating the sensitivity and specificity of predicting 3- and 5- y
survival with the amino acid metabolism- related signature in the CGGA datasets. CGGA, Chinese Glioma Genome Atlas; GBM, glioblastoma;
OS, overall survival; ROC, receiver operating characteristic; WHO, World Health Organization
curve, and compared the 30- gene signature with traditional “age” and
3.4 | Prognostic validity of the 30- gene signature
“grade”. The 30- gene signature showed striking prognostic validity,
for glioma
with AUC of 0.966 and 0.975 for 3- and 5- year survival, respectively,
Subsequently, we investigated the specificity and sensitivity of risk which were higher than for the traditional factors (Figure 3E,F), un-
score in the prediction of 3- and 5- year survival by analyzing the ROC derscoring the superior predictive value of the 30- gene signature.
8 | LIU et aL.
FIGURE 4 Prediction of outcome in diverse cohorts stratified by IDH mutation and 1p/19q codeletion status. Kaplan- Meier survival
curves for LGG patients with IDH- wild type (A), IDH- mutation but not the 1p/19q codeletion (B) and IDH- mutation with 1p/19q codeletion
(C), classified into two groups based on 30- gene signature- derived risk scores. Kaplan- Meier survival curves also show the prognostic value
of GBM patients with IDH- wild type (D) and IDH- mutation (E) in the CGGA cohort. P- value is the result of a log- rank test between the two
groups shown in each panel. CGGA, Chinese Glioma Genome Atlas; Codel, codeletion; GBM, glioblastoma; IDH, isocitrate dehydrogenase;
LGG, lower- grade glioma; OS, overall survival
and 1p/19q status; Table 2). Consistently, the local immune- related
3.5 | Univariate and multivariate analysis shows
risk signature was validated as an independent factor after Cox re-
prognostic value of 30- gene signature
gression analyses in TCGA cohort (Table S2).
To further explore whether the risk score was an independent prog-
nostic factor of prognosis in glioma, we carried out univariate and
3.6 | Functional annotation of 30- gene signature
multivariate Cox regression analyses in the CGGA cohort. Results
showed that the 30- gene signature was independently correlated To explore the potentially altered functional characteristics associ-
with OS by adjusting for clinicopathological factors (age, gender, ated with the 30- gene signature, GO analysis was carried out to study
WHO grade, TCGA subtype, IDH status, MGMT promoter status differences in biological processes between the two risk groups.
LIU et aL. | 9
FIGURE 5 Associations between the amino acid- related signature and other features in CGGA datasets. Distribution of the amino acid-
related gene signature in patients stratified by WHO grade (A), IDH1 status in each grade (B- D), 1p/19q status in IDH mutation- LGG (E) and
TCGA subtypes in GBM (F). *P < .05; **P < .01; ****P < .0001; ns, not significant. CGGA, Chinese Glioma Genome Atlas; Codel, codeletion;
GBM, glioblastoma; IDH, isocitrate dehydrogenase; LGG, lower- grade glioma; TCGA, The Cancer Genome Atlas; WHO, World Health
Organization
10 | LIU et aL.
TABLE 2 Uni- and multivariate Cox
Univariate analysis Multivariate analysis
regression analysis of the clinical features
Variables HR 95% CI P-v alue HR 95% CI P-v alue and 30- gene- based risk score for OS in
CGGA datasets
Age 1.038 1.022- 1.053 <.001 0.995 0.979- 1.012 .593
Gender 1.187 0.841- 1.675 .330 NA NA NA
WHO grade 3.469 2.709- 4.443 <.001 1.090 0.738- 1.610 .666
TCGA subtype 1.936 1.642- 2.282 <.001 0.880 0.687- 1.127 .310
IDH status 0.229 0.159- 0.331 <.001 0.770 0.391- 1.514 .448
MGMT 0.529 0.374- 0.750 <.001 0.989 0.644- 1.517 .959
promoter
status
1p/19q status 0.165 0.067- 0.404 <.001 0.970 0.362- 2.596 .951
Risk score 4.077 3.326- 4.999 <.001 3.825 2.830- 5.171 <.001
Bold type indicates a statistically significant difference ( P value < .05).
Variables with prognostic significance in univariate Cox regression analysis were included in further
multivariate Cox analysis.
Gender (female and male); WHO grade (II, III and IV); TCGA subtype (neural, proneural, mesenchy-
mal and classical); IDH status (mutant and wildtype); MGMT promoter status (methylated and un-
methylated); 1p/19q status (codeletion and non- codeletion); Risk score (low and high). CI, confidence
interval; CGGA, Chinese Glioma Genome Atlas; HR, hazard ratio; IDH, isocitrate dehydrogenase;
MGMT, methylguanine methyltransferase; NA, not applicable; OS, overall survival.
First, we demonstrated 1346 high- risk score positively related genes A previous study has identified a glucose- related risk signature
(P < .05) and 922 negatively related genes (P < .05) using Pearson for the malignancy of glioma and the survival of patients through
correlation analysis. Genes upregulated in the high- risk group were bioinformatic profiling.20 Also, metabolomic investigations have
primarily involved in tumor progression, including “extracellular ma- provided novel biomolecular insights into the aggressive pheno-
trix organization”, “cell division”, “angiogenesis”, “cell adhesion”, “ap- type of the malignancy of brain tumors.24,33,34 However, there
optotic process” and “immune response”. In contrast, downregulated continues to be a gap in systematically understanding the charac-
genes in the high- risk group were closely related to neurogenesis, teristics of the amino acid metabolism- related gene set in glioma.
such as “chemical synaptic transmission”, “learning”, “neurotransmit- In the present study, for the first time, we built an amino acid
ter secretion” and “nervous system development” (Figure 6A). metabolism- related risk signature to predict the prognosis of glioma.
Moreover, GO analysis was implemented to explore the differ- RNAseq expression data from 309 patients in the CGGA database were
ences in KEGG pathway between the high- and low- risk score groups. included as the training set, whereas another 550 patients with TCGA
We found that positively related genes were mainly enriched in KEGG database were used to validate. First, the 309 samples were apparently
terms including “ECM- receptor interaction”, “cell cycle”, “focal adhe- clustered into two distinct subclasses (k = 2), and the two subclasses
sion” and “TNF signaling pathway”, whereas the negatively correlated showed significant differences in clinical and molecular features in both
genes were enriched in terms including “retrograde endocannabinoid the CGGA and TCGA cohort. However, for k = 3, the area under the cu-
signaling”, “insulin secretion” and “dopaminergic synapse” (Figure 6B). mulative distribution function (CDF) curve was increased by more than
These results were validated in TCGA cohort (Figure S6). 0.1- fold that of k = 2 (Figure 1C,D), and we found the ratio of samples in
Next, GSEA analyses were carried out for validation, show- the third subclass was very small (Figure 1B). It also meant that for k > 2,
ing that the high- risk groups were positively associated with clustering stability did not improve significantly.
regulation of innate immune response (P < .001) and response to Next, we developed a 30- gene- based risk signature to determine
tumor necrosis factor (P < .001), negatively with synaptic signal- the status of amino acid metabolism in glioma patients. We observed
ing (P < .001) and regulation of neurotransmitter levels (P < .001; that the high- risk group was closely associated with IDH wildtype,
Figure 6C). 1p/19q noncodeletion, higher WHO grades and worse TCGA sub-
types (classical and mesenchymal) (Figures 2C and 5, Figure S2C and
S5), which implies that the amino acid metabolism- related risk sig-
4 | DISCUSSION nature may, to some extent, result in the poor prognosis of patients
with IDH wildtype, 1p/19q noncodeletion, higher WHO grades and
Fast- growing tumor cells largely draw energy out of typically in- worse TCGA subtypes.
creasing aerobic glycolysis, a phenomenon known as the Warburg We further showed that the 30- gene signature could predict the
effect.1,12 Aside from the glycolytic pathway, the metabolic prognosis of glioma regardless of WHO grade and the five subgroups
changes of cancer cells primarily involve amino acid metabolism.3 of WHO 2016 classification based on the stratification of IDH and
LIU et aL. | 11
FIGURE 6 Altered functional characteristics related to the 30- gene signature. A,B, Functional annotation of genes positively (red bar
chart) or negatively (green bar chart) correlated with the risk score using GO terms of biological processes (A) and KEGG pathway (B). C,
Gene set enrichment analysis (GSEA) shows that higher risk score was positively associated with immune response and negatively correlated
with synaptic signaling and neurotransmitter levels. Codel, codeletion; NES, normalized enrichment score; Noncodel, noncodeletion. Orange
and green bars represent P- value, and the blue dots represent the 1/3 gene count
1p/19q status in the CGGA cohort (Figures 3A- D and 4). Then, ROC AUC of 0.966, 0.692, 0.898 and 0.975, 0.677, 0.885 for 3- and 5- year
curves were carried out to compare the prognostic values between survival, respectively (Figure 3E,F). These results suggested that the
the 30- gene signature and traditional factors “age” and “grade”, with 30- gene signature could better predict the prognosis of glioma.
12 | LIU et aL.
In the validation cohort, in contrast with WHO grade II and III, of gliomas. We then developed a 30- amino acid metabolism- related
the 30- gene signature predicted poor overall prognosis for GBM gene expression- based risk signature, which was strongly related to
(Figure S4A- D). One possible reason is that there were distinct dif- the OS of glioma patients in the five subgroups of WHO 2016 clas-
ferences in the distribution of grades and subtypes between CGGA sification for patients based on the stratification of IDH and 1p/19q
and TCGA cohorts. As shown in Table S3, GBM patients in the CGGA status, and confirmed that the 30- risk signature could better pre-
cohort accounted for 44.7% of the total, whereas GBM accounted dict OS for glioma than traditional factors. Moreover, we carried
for a proportion of 26.9% in TCGA cohort. LGG were divided into out functional annotation of the positive and negative amino acid
three subgroups based on the status of IDH and 1p/19q codeletion. metabolism- related gene in glioma. Furthermore, the risk signature
As for LGG- IDHwt, glioma patients in the high- risk group had a poorer could contribute to understanding the carcinogenesis and develop-
prognosis than those with low- risk score, with a significant differ- ment of glioma, as well as providing new insight into the therapeu-
ence (P = .001). However, for LGG- IDHmut- codel and LGG- IDHmut- tic targets for glioma patients. In short, we identified a novel amino
noncodel, the OS of high-risk patients tended to be worse, although acid metabolism- related risk signature for predicting the prognosis
the difference showed no significance (P > .05) (Figure S4E- G). We of glioma.
considered that if the sample sizes were increased, there might be a
statistical difference in GBM and these subtypes.
ACKNOWLEDGMENTS
Of note, we identified that the amino acid metabolism- related
risk signature remained an independent prognostic factor after ad- The authors conducting this work represent the Chinese Glioma
justment of clinical and molecular features. There is great potential Cooperative Group (CGCG). This work was supported by grants from
for the status of amino acid metabolism to refine the clinicopatho- the Capital Medical Development Research Fund (2016- 1- 1072),
logical features of accurate prognostication, so combining the risk the National Natural Science Foundation of China (Grant Numbers:
signature and other features could better predict the prognosis of 81672479, 81773208, and 81502495) and the Beijing Natural
glioma. Science Foundation (7182076). The study protocol was approved
Functional annotation of the 30- gene signature showed that bio- by the ethics committees of participating hospitals, and all patients
logical functions of angiogenesis, cell adhesion and immune response signed written, informed consent.
may contribute to patients’ high risk and poor clinical outcome. Low-
purity gliomas were characterized by intensive local immune pheno-
types and correlated with a poor prognosis.23 Therefore, we applied CONFLICTS OF INTEREST
the ESTIMATE algorithm to predict tumor purity using gene expres-
Authors declare no conflicts of interest for this article.
sion profiles26 and found a significant increase in ESTIMATE scores
in the high- risk group (Figure S7), indicating that a greater presence
of inflammatory microenvironment components is associated with ORCID
progressive tumorigenesis.27
Yu-Qing Liu https://orcid.org/0000-0002-5119-2984
In addition, we analyzed the 30- amino acid metabolism- related
Rui-Chao Chai https://orcid.org/0000-0003-3451-8871
genes and proteins in detail. DAVID functional annotation was car-
Fan Wu https://orcid.org/0000-0001-9256-0176
ried out to determine the biological process in which each gene
selected as 30- risk signature is involved (Figure S8A). Our results Tao Jiang https://orcid.org/0000-0002-7008-6351
showed that a group of genes (including PSMC6, PSMD12, PSMB4,
PSMC2, PSME4 and PSMB2) engaged in similar biological processes,
REFERENCES
such as “regulation of cellular amino acid metabolic process”, “NIK/
NF- kappaB signaling”, “TNF/T- cell receptor mediated signaling path- 1. Pavlova NN, Thompson CB. The emerging hallmarks of cancer me-
way” and “protein polyubiquitination” etc. Five genes (CBS, PAH, tabolism. Cell Metab. 2016;23:27-47.
2. Jain M, Nilsson R, Sharma S, et al. Metabolite profiling identifies
OAT, GPT and BCAT2) among them participated in “cellular amino
a key role for glycine in rapid cancer cell proliferation. Science.
acid biosynthetic process”. We still found some genes that played
2012;336:1040-1044.
roles in certain amino acid metabolic processes. For instance, ODC1 3. Karpel-Massler G, Ramani D, Shu C, et al. Metabolic reprogramming
took part in the “polyamine metabolic process”, and AADAT and of glioblastoma cells by L- asparaginase sensitizes for apoptosis in
vitro and in vivo. Oncotarget. 2016;7:33512-33528.
GCLC were involved in the “glutamate metabolic process”. Moreover,
4. Alberghina L, Gaglio D. Redox control of glutamine utilization in
we analyzed the protein- protein interaction network for 30- amino
cancer. Cell Death Dis. 2014;5:e1561.
acid metabolism- related genes/proteins using the STRING data- 5. Seyfried TN, Flores R, Poff AM, D’Agostino DP, Mukherjee P.
base (Figure S8B). Further molecular mechanisms as to how these Metabolic therapy: a new paradigm for managing malignant brain
cancer. Cancer Lett. 2015;356:289-300.
genes affect the progression of glioma remain to be studied in our
6. Locasale JW. Serine, glycine and one- carbon units: cancer metabo-
follow- up work.
lism in full circle. Nat Rev Cancer. 2013;13:572-583.
In conclusion, we identified that the amino acid metabolism- 7. Kalhan SC, Hanson RW. Resurgence of serine: an often neglected
related gene set could distinguish the clinical and molecular features but indispensable amino acid. J Biol Chem. 2012;287:19786-19791.
LIU et aL. | 13
8. DeBerardinis RJ, Cheng T. Q’s next: the diverse functions of 25. Cheng W, Ren X, Zhang C, Cai J, Han S, Wu A. Gene expression
glutamine in metabolism, cell biology and cancer. Oncogene. profiling stratifies IDH1- mutant glioma with distinct prognoses. Mol
2010;29:313-324. Neurobiol. 2017;54:5996-6005.
9. Hensley CT, Wasti AT, DeBerardinis RJ. Glutamine and cancer: 26. Cheng W, Ren X, Zhang C, et al. Bioinformatic profiling identi-
cell biology, physiology, and clinical opportunities. J Clin Invest. fies an immune- related risk signature for glioblastoma. Neurology.
2013;123:3678-3684. 2016;86:2226-2234.
10. Zhang J, Pavlova NN, Thompson CB. Cancer cell metabolism: the 27. Hu X, Martinez-Ledesma E, Zheng S, et al. Multigene signature for
essential role of the nonessential amino acid, glutamine. EMBO J. predicting prognosis of patients with 1p19q co- deletion diffuse gli-
2017;36:1302-1315. oma. Neuro Oncol. 2017;19:786-795.
11. Seltzer MJ, Bennett BD, Joshi AD, et al. Inhibition of glutaminase 28. Gu J, Zhang X, Miao R, et al. A three- long non- coding RNA-
preferentially slows growth of glioma cells with mutant IDH1. Can expression- based risk score system can better predict both overall
Res. 2010;70:8981-8987. and recurrence- free survival in patients with small hepatocellular
12. Yue M, Jiang J, Gao P, Liu H, Qing G. Oncogenic MYC activates a carcinoma. Aging. 2018;10:1627-1639.
feedforward regulatory loop promoting essential amino acid me- 29. Gao J, Kwan PW, Shi D. Sparse kernel learning with LASSO and
tabolism and tumorigenesis. Cell Rep. 2017;21:3819-3832. Bayesian inference algorithm. Neural Netw. 2010;23:257-264.
13. Schulte ML, Fu A, Zhao P, et al. Pharmacological blockade of 30. Qian Z, Li Y, Fan X, et al. Molecular and clinical characterization
ASCT2- dependent glutamine transport leads to antitumor efficacy of IDH associated immune signature in lower- grade gliomas.
in preclinical models. Nat Med. 2018;24:194-202. Oncoimmunology. 2018;7:e1434466.
14. Strickland M, Stoll EA. Metabolic reprogramming in glioma. Front 31. Yan W, Zhang W, You G, et al. Molecular classification of gliomas
Cell Dev Biol. 2017;5:43. based on whole genome gene expression: a systematic report of
15. Jiang T, Mao Y, Ma W, et al. CGCG clinical practice guide- 225 samples from the Chinese Glioma Cooperative Group. Neuro
lines for the management of adult diffuse gliomas. Cancer Lett. Oncol. 2012;14:1432-1440.
2016;375:263-273. 32. Verhaak RG, Hoadley KA, Purdom E, et al. Integrated genomic anal-
16. Pandey R, Caflisch L, Lodi A, Brenner AJ, Tiziani S. Metabolomic ysis identifies clinically relevant subtypes of glioblastoma charac-
signature of brain cancer. Mol Carcinog. 2017;56:2355-2371. terized by abnormalities in PDGFRA, IDH1, EGFR, and NF1. Cancer
17. Louis DN, Perry A, Reifenberger G, et al. The 2016 World Health Cell. 2010;17:98-110.
Organization classification of tumors of the central nervous system: 33. Griffin JL, Kauppinen RA. A metabolomics perspective of human
a summary. Acta Neuropathol. 2016;131:803-820. brain tumours. FEBS J. 2007;274:1132-1139.
18. Lu CF, Hsu FT, Hsieh KL, et al. Machine learning- based ra- 34. Ahmed KA, Chinnaiyan P. Applying metabolomics to understand
diomics for molecular subtyping of gliomas. Clin Cancer Res. the aggressive phenotype and identify novel therapeutic targets in
2018;24:4429-4436. glioblastoma. Metabolites. 2014;4:740-750.
19. Brat DJ, Verhaak RG, Aldape KD, et al. Comprehensive, integra-
tive genomic analysis of diffuse lower- grade gliomas. N Engl J Med.
SUPPORTING INFORMATION
2015;372:2481-2498.
20. Zhao S, Cai J, Li J, et al. Bioinformatic profiling identifies a glucose-
Additional supporting information may be found online in the
related risk signature for the malignancy of glioma and the survival
Supporting Information section at the end of the article.
of patients. Mol Neurobiol. 2017;54:8203-8210.
21. Wu F, Zhao Z, Chai R, et al. Expression profile analysis of antisense
long non- coding RNA identifies WDFY3- AS2 as a prognostic bio-
marker in diffuse glioma. Cancer Cell Int. 2018;18:107. How to cite this article: Liu Y-Q, Chai R-C, Wang Y-Z, et al.
22. Brennan CW, Verhaak RG, McKenna A, et al. The somatic genomic
Amino acid metabolism- related gene expression- based risk
landscape of glioblastoma. Cell. 2013;155:462-477.
signature can better predict overall survival for glioma.
23. Zhang C, Cheng W, Ren X, et al. Tumor purity as an underlying key
factor in glioma. Clin Cancer Res. 2017;23:6279-6291. Cancer Sci. 2018;00:1–13. https://doi.org/10.1111/cas.13878
24. Subramanian A, Tamayo P, Mootha VK, et al. Gene set enrichment
analysis: a knowledge- based approach for interpreting genome- wide
expression profiles. Proc Natl Acad Sci USA. 2005;102:15545-15550.
