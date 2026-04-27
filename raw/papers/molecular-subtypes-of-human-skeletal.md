---
source_path: /mnt/c/Users/Administrator/Zotero/storage/NRI3LHXH/Bhatt 等 - 2025 - Molecular subtypes of human skeletal muscle in cancer cachexia.pdf
ingested: 2026-04-23
sha256: b8d62114ce0d5310
---

Article
Molecular subtypes of human skeletal
muscle in cancer cachexia
https://doi.org/10.1038/s41586-025-09502-0 Bhumi J. Bhatt1,2, Sunita Ghosh1, Vera Mazurak3, Aurélien Q. Brun4, Oliver Bathe5,
Vickie E. Baracos1,6 ✉ & Sambasivarao Damaraju2,3,6 ✉
Received: 17 September 2024
Accepted: 7 August 2025
Cancer-associated muscle wasting is associated with poor clinical outcomes1, but its
Published online: xx xx xxxx
underlying biology is largely uncharted in humans2. Unbiased analysis of the RNAome
Check for updates
(coding and non-coding RNAs) with unsupervised clustering using integrative non-
negative matrix factorization3 provides a means of identifying distinct molecular
subtypes and was applied here to muscle of patients with colorectal or pancreatic
cancer. Rectus abdominis biopsies from 84 patients were profiled using high-
throughput next-generation sequencing. Integrative non-negative matrix
factorization with stringent quality metrics for clustering identified two highly
coherent molecular subtypes within muscle of patients with cancer. Patients with
subtype 1 (versus subtype 2) showed clinical manifestations of cachexia: high-grade
weight loss, low muscle mass, atrophy of type IIA and type IIX muscle fibres, and
reduced survival. On the basis of differential expression between the subtypes, we
identified biological processes that may contribute to cancer-associated loss of
muscle mass and function, including altered posttranscriptional regulation and
perturbation of neuronal systems; cytokine storm and cellular immune response;
pathways related to extracellular matrix; and metabolic abnormalities spanning
xenobiotic metabolism, haemostasis, signal transduction, embryonic and/or
pluripotent stem cells, and amino acid metabolism. Differential expression between
subtypes indicated the involvement of multiple intertwined higher-order gene
regulatory networks, suggesting that network interactions of (hub) long non-coding
RNAs, microRNAs and mRNAs could represent targets for future research.
Cancer cachexia is defined by progressive loss of weight and skeletal RNA-seq and multiomics, whereas only two studies have analy-
muscle mass in the presence of underlying malignant disease. This sed mRNAs from muscle of patients with cancer using an RNA-seq
muscle loss has been extensively characterized using computed tomog- platform7,8. The accessibility of a repertoire of cachexia-inducing
raphy (CT) and shows associations with mortality, complications of murine tumours (for instance, pancreatic KPC or KPP, lung LLC and
cancer therapies, and reduced physical functioning and quality of life1. colon C26) has enabled the development of a large body of experi-
Despite the clinical importance of loss of muscle mass and function, mental evidence on cancer-associated muscle wasting; rodent studies
its underlying molecular mechanisms remain largely uncharted. The outnumber clinical studies of human muscle biology by approximately
invasive nature of muscle biopsy is a key limitation to research; studies 100:1. Experimental research has identified several molecular entities
based on this approach have been few in number and undermined by that potentially contribute to muscle wasting9,10. However, these mecha-
low quality and high risk of bias, as well as being restricted to consid- nisms remain untested in humans, and the translational relevance
eration of a few putative candidate molecules2. Most such studies have of animal models has been debated9. We thus planned a comprehen-
reported body mass index (BMI) and weight loss but lacked CT-defined sive analysis of muscle transcriptome in a representative cohort of
specific measures of muscle mass or muscle loss4,5. Transcriptomic patients with cancer to gain deeper insights into the pathogenesis of
studies have also been limited in sample size relative to the numbers this complex condition. To this end, we generated high-throughput
required to achieve stability in rank order and statistical significance next-generation sequencing datasets for small non-coding RNAs and
of gene signatures6. long RNAs (mRNAs and long non-coding RNAs (lncRNAs)). By including
Primary muscle pathologies (for instance, dystrophies) have been non-coding RNA species, we hoped to observe higher-order control
extensively researched using RNA sequencing (RNA-seq), assay for of gene expression exerted by microRNAs (miRNAs) and lncRNAs. We
transposase-accessible chromatin using sequencing, small nuclear implemented an unsupervised clustering algorithm to infer molecular
1Department of Oncology, Faculty of Medicine and Dentistry, University of Alberta, Edmonton, Alberta, Canada. 2Department of Laboratory Medicine and Pathology, Faculty of Medicine
and Dentistry, University of Alberta, Edmonton, Alberta, Canada. 3Department of Agricultural, Food and Nutritional Science, Faculty of Agricultural, Life and Environmental Science, University
of Alberta, Edmonton, Alberta, Canada. 4Unité de Nutrition Humaine (UNH), INRAE, Université Clermont Auvergne, Clermont-Ferrand, France. 5Departments of Surgery and Oncology, Arnie-
Charbonneau Cancer Institute, University of Calgary, Calgary, Alberta, Canada. 6These authors contributed equally: Vickie E. Baracos, Sambasivarao Damaraju. ✉e-mail: vbaracos@ualberta.ca;
sdamaraj@ualberta.ca
Nature | www.nature.com | 1
Article
a
Time 1 Time 2
Biopsy
Weight change (%)
Muscle change (%)
BMI (kg m−2)
28 25 22 20
2.5
6
11
15
e
Data Feature selection Unsupervised learning approach: intNMF
preprocessing
Quantification of mRNA, IncRNA, miRNA, piRNA, tRNA, snoRNA
RNAs using
annotation RNA-seq
databases (filter out non- Sample × gene matrix variable features)
Rank (k number of clusters): five-fold cross-
validation
Read count filtering
(1 read count in 100 iterations
100% of samples) Small RNA-seq k = 2:5
(filter out non- Seeding and multiple
variable runs
features) 300 iterations
Normalization and k = 2 transformation of read counts of all Silhouette width RNAs (n = 6 RNAs)
Quality metrics
Cluster prediction
index and cophenetic
coefficient
correlations (that is, coregulated RNA species) and identify patient expressed (DE) genes in the clusters identified; (5) perform multilay-
subtypes from these coregulated patterns of expression. Integrative ered RNA cross-talk analysis to gain insight into posttranscriptional
non-negative matrix factorization (intNMF) was chosen owing to its regulatory mechanisms; (6) make biological and clinical inferences of
robust sample clustering, data dimensionality reduction and decom- subtypes; and (7) compare the findings with those obtained in animal
position of non-negative expression datasets11,12. We also aimed to models of cachexia.
perform multilayered RNA cross-talk (lncRNA–miRNA–mRNA) analysis
to obtain insights into posttranscriptional regulatory mechanisms.
Patient characteristics
We expected that classification of skeletal muscle into molecular
subtypes on the basis of the transcribed genome (RNAome) and its Participants underwent surgery for resection of pancreatic cancer (at
regulation would offer mechanistic insights into the pathophysiology any stage) or hepatic metastases of colon cancer in a single clinical
of cachexia. Our aims were to: (1) create a skeletal muscle biobank repre- service serving southern Alberta, Canada. Patients provided consent
sentative of the population of patients with cancer undergoing surgery consecutively (n = 84); 3% of patients declined participation. Rectus
in our region; (2) generate a transcriptional atlas of rectus abdominis abdominis specimens were collected from the incision margin, at open-
using next-generation sequencing; (3) apply intNMF to ascertain inher- ing, and data on weight and muscle changes were collected before
ent molecular subtypes within the sample; (4) investigate differentially surgery (Fig. 1a). Overall, the patient population was 57% male, with
2 | Nature | www.nature.com
)%(
ssol
thgieW
b
Population SMI distribution
Biopsy population
SMI distribution
10 20 30 40 50 60 70 80 90 10 20 30 40 50 60 70
SMI (cm2 m−2) SMI (cm2 m−2)
c d Sex-specific SMI distribution
0 0 1 1 3 High SMI High SMI
male female
1 2 2 2 3 Low SMI ≥60.9 cm2 m−2 Low SMI ≥47.5 cm2 m−2
2 3 3 3 4 male female
–1.00 s.d. –1.00 s.d.
3 3 3 4 4 <42.0 cm2 m−2 <34.6 cm2 m−2
3 4 4 4 4
10 20 30 40 50 60 70 80 90 10 20 30 40 50 60 70
SMI (cm2 m−2) SMI (cm2 m−2)
f
tRNA
13% mRNA
28%
snoRNA Male
22% patients
lncRNA
piRNA 16%
10%miRNA
12%
tRNA
14% mRNA
26%
snoRNA Female 23% patients lncRNA
14% piRNA
11% miRNA
12%
Fig. 1 | Research design and cachexia classification. a, Study schema depicting (male, SMI ≥ 60.9 cm2 m−2; female, SMI ≥ 47.5 cm2 m−2; on the basis of values
muscle biopsy collection and presurgery muscle and weight changes computed reported for healthy 30-year-olds), low (SMI ≤ −1.0 standard deviations below
as percentage change for n = 84 patients. The samples obtained for expression the sex-specific and age-specific mean for patients in our population cohort)
profiling consisted of biological replicates for all 84 samples. b, Unbiased or medium (all other SMI values). e, Flow diagram of the research design for
sampling. The SMI distributions of patients participating in muscle biopsy identification of subtypes from the RNAome of skeletal muscle using intNMF.
(red curve) are indicated for male patients (left) and female patients (right); f, Relative abundance of RNA species depicted using donut plots (top, men;
the mean values were 48.2 ± 7.8 cm2 m−2 in male and 39.1 ± 8.1 cm2 m−2 in female bottom, women). The human silhouettes depicting the rectus abdominis
individuals. The population SMI distribution is shown in black for each sex; in part b were used under licence from Shutterstock (www.shutterstock.com);
population data are from Martin et al.5. c, Weight loss grades were classified original artwork by V. Baracos.
according to Martin et al.13. d, Sex-specific SMI was categorized as high
45% having pancreatic cancer, and the presurgical skeletal muscle index was identified. We also provide benchmarks for categorization of
(SMI; the muscle cross-sectional area normalized for height in m2) high muscularity. Thus classified (Fig. 2g), 82% patients of subtype 2
was representative of the regional population distribution (Fig. 1b). had minimal weight loss, and 10 of 10 (100%) of patients who met cri-
Weight loss grades13 spanning 0–4 were captured (Fig. 1c). SMI was teria for high SMI (that is, as muscular as healthy 30-year-olds) were
categorized as low, medium or high (Fig. 1d). Overall, the population sub type 2. By contrast, patients of subtype 1 had lower BMI and total
was losing muscle before biopsy during a median scan interval of 101 adipose tissue index, and higher percentage weight loss and grade, and
(interquartile range: 63–165) days. The rate of muscle loss was highly all had low–medium SMI. Poorer overall survival was concordant with
intercorrelated among different regions of the body despite variation the suggestion that subtype 1 is a cachexia subtype (Fig. 2h). Overall, 91%
in the specific muscles present at these levels (Extended Data Fig. 1): of participants had died by the time of analysis. As pancreatic and colon
thoracic (T4) versus thigh Pearson’s r = 0.982; T4 versus L3 r = 0.984; cancer have different prognoses, survival by subtype was adjusted for
L3 versus thigh r = 0.975. The high degree of intercorrelation of muscle primary cancer. Patients of subtype 1 had an increased risk of mortality
change over time in these regions suggests that cancer-associated (hazard ratio 2.086; 98% CI: 1.255–3.466; log-rank P = 0.005) and were
muscle atrophy is systemic. more likely to have a primary cancer diagnosis of colon versus pancreas
(hazard ratio 0.0468; 98% CI: 0.286–0.768; P = 0.003).
RNAome of patient muscle biopsies
Immunohistological features
The research design (Fig. 1e) included next-generation sequencing
followed by data preprocessing, feature selection and intNMF analysis. A further cohort of n = 70 patients from the same pipeline of muscle
Transcriptome data generation was performed in a single batch. The biopsy in pancreatic and colon cancer surgery was used to make mor-
RNA species studied were mRNAs (protein-coding), lncRNAs (more than phological observations across the SMI distribution in both sexes.
200 nt in length) and small non-coding RNAs (less than 200 nt, miRNAs, Type I, type IIA and type IIX fibres were detected in all biopsies. The
piwi-interacting RNA (piRNAs), small nucleolar RNA (snoRNAs) and percentages of fibres in rectus abdominis were as follows: 35.4% ± 9.1%
transfer RNAs (tRNAs)). As muscle gene expression is sexually dimor- (s.d.) Type IIA, 17.3% ± 14.6 type IIX; and 47.3% ± 13.4% type I. These
phic14, all ensuing analyses were sex-specific unless otherwise stated. proportions were unaffected by sex and SMI category, as shown pre-
Data have been deposited at the NCBI Gene Expression Omnibus (GEO) viously2. Cross-sectional areas of all fibre types varied across the low,
and are accessible through GEO series accession numbers GSE254877 medium and high SMI categories (Extended Data Table 2; a representa-
(RNA-seq), GSE254878 (small RNA-seq) and GSE292052) (rat RNA-seq) tive micrograph is shown in Fig. 2i). Fast glycolytic type IIX fibres were
embedded in GEO super series GSE292053. −64% smaller, and type IIA fibres were −55% smaller in low versus high
SMI in both sexes (P < 0.001). Muscle fibre cross-sectional areas were
correlated with CT-defined SMI (P < 0.001): male, Pearson r2 = 0.667;
RNAome-based molecular subtypes in muscle female, r2 = 0.717. Nuclear positioning in muscle fibres is normally sub-
There were no sex differences in relative abundances of RNA species, sarcolemmal, with central nuclei appearing both in muscle diseases
ruling out preferential enrichment of any specific RNA classes (P > 0.8; and during tissue regeneration16. The percentage of fibres with central
Fig. 1f). The entire transcribed genome (approximately 36,000 indi- nuclei (Extended Data Table 2; representative micrograph in Fig. 2j)
vidual RNAs per sample) was entered into the unsupervised learning were highest in the high SMI category (12.8% versus 5.1% in the low SMI
approach, intNMF3 (Fig. 2a). This algorithm defines the optimal number category; P < 0.005).
of clusters and their coherence on the basis of defined quality metrics,
silhouette width and cluster prediction index. The intNMF algorithm
Differential expression between subtypes
was run with 100 and 300 iterations using a random initializing seed
parameter of an optimal number of clusters range of K = 2:5, with We next studied biological characteristics on the basis of the differential
five-fold cross-validation and Euclidean as the distance metric. In both expression of RNAs between subtypes. It was unknown to what extent
sexes, a K = 2 cluster solution was consistent with all iterations; that is, differential expression might be sexually dimorphic, so initially we
the optimal separation was a K = 2 cluster solution (Fig. 2b–d). The K = 2 evaluated it separately in both sexes. Data on DE RNAs are presented
cluster solution showed a high degree of coherency according to the in Fig. 2e and Supplementary Table 1A,B). There were no DE tRNAs for
silhouette width, which has a maximum value of 1.00 (Fig. 2c) (male, female participants and only one DE tRNA for male participants. The
cluster 1: 0.95, cluster 2: 0.99; female, cluster 1: 0.88, cluster 2: 0.96). total absolute number of DE RNAs (Fig. 2e) was greater by 50–60% in
Hereafter, we refer to these clusters as subtypes. Subtypes did not differ male individuals. For all RNA classes, DE RNAs between subtypes over-
in distribution of patient age, pancreas versus colon primary, disease lapped between male and female participants (Fig. 2f): 83% and 90% of
stage, Charleston comorbidity index or C-reactive protein (Extended DE mRNAs and lncRNAs, respectively, from female participants over-
Data Table 1), ruling out any biases or stratification on the basis of lapped with those from male participants. DE small non-coding RNAs
these clinical variables. Previous chemotherapy was present among from female participants showed lesser overlap with those from male
the patients with colorectal cancer only, using 5-fluoruracil-based regi- participants (69% for miRNAs, 39% for piRNAs and 12% for snoRNAs).
mens (Extended Data Table 1), and did not differ between subtypes. We concluded that there was dimorphic differential expression accord-
ing to subtype in individual RNA species, and that this was especially
prominent in the non-coding regulatory genome.
Subtype 1 is a cachexic subtype
Weight loss grades13 and SMI (Fig. 2g and Extended Data Table 1) were
Regulatory networks of the RNAome
assessed, as neither of these alone described cachexia and both are
considered to be diagnostic criteria15. Our CT-based approach improved RNA-mediated gene silencing was identified as the top gene set
classification, enabling us to avoid many limitations of the clinical (P ≤ 0.003) in gene set enrichment analysis (GSEA) (Fig. 3a). Other
weight loss record (different time frames, lack of precision, recall bias significant gene sets were pre-miRNA and miRNA processing, regula-
and missing data). This approach also addressed the lack of tissue- tion of non-coding RNA processing, non-coding RNA catabolic process,
level specificity when considering overall weight; that is, muscle loss piRNA processing, and negative regulation of mRNA metabolic process,
greater than 10% was confirmed in five patients who did not recall any suggesting that subtype 1 shows extensive posttranscriptional gene
weight loss, and one patient with fat loss without any loss of muscle regulation.
Nature | www.nature.com | 3
Article
a
f g i
Subtype 1 Subtype 2 Low SMI Medium SMI High SMI
SMI categories
mRNAs Medium Medium
w
1,143 2,376 471 Lo H igh
piRNAs
4
127 9 17 4 0 3
lncRNAs 1 2 0
3 2 1
1,847 2,385 252 Weight loss grades
snoRNAs
h Overall survival j
52 7 50 1.0 Hoechst Laminin
miRNAs 0.8 1 2
45 27 12 0.6
0.4
0.2
0 P = 0.003
0 1,0002,0003,0004,0005,000
Survival since biopsy (days)
Understanding the interplay of RNAs could help to elucidate novel We implemented several target prediction databases (in silico and exper-
posttranscriptional regulatory networks17. lncRNAs and miRNAs com- imentally validated) to investigate miRNA binding sites for lncRNAs
prise two layers of upstream regulation of mRNAs. Hub lncRNAs are and mRNAs. To identify skeletal-muscle-specific gene targets, we over-
considered to be master regulators, because they regulate multiple lapped our muscle expression dataset with those of the target prediction
miRNAs, each of which can interact with multiple mRNAs (competing databases. The stringency cutoffs applied for ceRNA analysis were as
endogenous RNAs; ceRNAs). We were interested to learn how ceRNAs follows: hypergeometric P < 0.01, Pearson’s correlation P < 0.01, corre-
collectively influenced posttranscriptional gene regulation. We there- lation r > 0.7 and regulation similarity score > 0). Total non-redundant
fore performed ceRNA analysis using sex-specific and subtype-specific lncRNA–miRNA–mRNA triplets and their overlap between men and
DE profiles of lncRNAs, miRNAs and mRNAs (competing RNA triplets). women are depicted in Fig. 3b. The top 20 hub lncRNAs with the highest
4 | Nature | www.nature.com
lavivrus
evitalumuC
b c Cluster 1 Cluster 2 d Subtype 1 Subtype 2 e
(n = 27) (n = 21)
S = 0.95 S = 0.99
1.0 i i
Cluster 1Cluster 2
RNA Total 0.8 RNA Subtype
type profiled species 1 versus 2
0.6
Men Men
0.4
mRNA 18,586 mRNA 3,519
lncRNA 16,204 000 ... 6420 0.2 lncRNA 4,231
miRNA 479 10..08 0 miRNA 72
piRNA 868 Patients samples piRNA 436
–2 –1 0 1 2
snoRNA 608 Row-scaled normalized counts snoRNA 59
Cluster 1 Cluster 2 Subtype 1 Subtype 2
Women (n = 18) (n = 18) Women
mRNA 18,548 Cluster 1Cluster 2 1.0 S i = 0.88 S i = 0.96 mRNA 2,847
lncRNA 16,183 lncRNA 2,638
miRNA 565 0.8 miRNA 39
piRNA 838 0.6 piRNA 26
snoRNA 604 snoRNA 57
0.4
0
0.2
0 0 . . 6 4 0.2
0.8
1.0 0
Patient samples
–2 –1 0 1 2
Row-scaled normalized counts
w Lo
Subtype
Fig. 2 | Subtype identification, genome-wide RNAome profiles, association weight loss grades 0–4 by subtype. Data underlying the chord plots are
with clinical, radiological and histological parameters. a, Expression available in Extended Data Table 1. SMI categories (top semiarc: grey, low SMI;
profiling; total profiled RNAs. b, Consensus plot for the K = 2 solution showing light pink, medium SMI; blue, high SMI) and weight loss grades (bottom arc:
two distinct non-overlapping clusters. c, Silhouette plot for the K = 2 solution. 0, orange; 1, navy blue; 2, slate grey; 3, dark pink; 4, yellow). No patients in
A y-axis value for the silhouette coefficient (S) close to 1.00 indicates a data subtype 1 had high SMI. h, Cumulative survival plot, adjusted for primary
i
point distant from other clusters, whereas an S value close to 0 reflects a data tumour with log-rank P value. i, Photomicrographs from patients with low,
i
point that lies close to the decision boundary between clusters. The x axis medium and high SMI. Blue, type I; green, type IIA; red, type IIX; yellow,
indicates individual patients within the cluster. The mean S is given for each laminin. All patients whose images are shown were of male sex and of the same
i
cluster. d, Heatmap representation of expression of top DE mRNAs by subtype. age decade. The median fibre areas for patients with low SMI (2,460 µm2),
e, Numbers of DE RNAs between subtype 1 and subtype 2. For a–e, data are medium SMI (4,241 µm2) and high SMI (5,420 µm2) reflect the mean values for
presented for male (top row) and female (bottom row) patients. Additional male individuals (Extended Data Table 2). j, Representative photomicrograph
are available in Supplementary Table 1a,b. f, Venn diagram of sex-related of central nuclei from a 63-year-old female patient (SMI 46 cm2 m−2, fibre area
transcriptional differences for individual RNA species in subtype 1 versus 2. 1,926 µm2 and 23.6% fibres with central nuclei); arrows indicate central nuclei.
g, Cachexia characteristics of subtypes. Chord plot shows SMI categories and Scale bars, 250 µm (i and left panel of j), 50 µm (right panel of j).
a b
Enrichment plot: Enrichment plot:
GO BP RNA-mediated silencing GO BP RNA-mediated silencing
0.5
0.4
0.3
0.2 P = 0.001
0.1
0
0.4 0.2 0 –0.2
0 2,000 4,000 6,000 8,000 10,000 12,000 14,000 16,000 18,000 20,000 0 2,000 4,000 6,000 8,000 10,000 12,000 14,000 16,000 18,000
c d
lncRNA miRNAs mRNAs lncRNA miRNAs mRNAs
hsa-miR-98-5p
hsa-miR-96-5p TTLL9
hsa-miR-92a-5p TG
hsa-miR-92a-3p TFAP2B
hsa-miR-885-3p TAT hsa-miR-98-5p
hsa-miR-493-3p SPTSSB
hsa-miR-433-3p SH3GL2 hsa-miR-543
h h s s a a - - m m i i R R - - 3 4 7 2 9 3 - - 5 5 p p S S A A L L L L 4 3 hsa-miR-511-5p
h h s s a a - - m m i i R R - - 3 3 7 7 4 0 b -3 - p 5p RSPO2 hsa-miR-493-3p
hsa-miR-363-3p PTPRO hsa-miR-379-5p
hsa-miR-361-3p OLR1 hsa-miR-379-5p
hsa-miR-339-5p NIPAL4
hsa-miR-320b NECAB1 hsa-miR-370-3p
h h s s a a - - m m i i R R - - 3 3 2 0 0 e- a 5 -3 p p N M A A T C 1 C1 hsa-miR-30e-5p
hsa-miR-30a-5p LYPD6B hsa-miR-27b-3p
hsa-miR-27a-3p LYPD6 TRIM71
hsa-miR-26b-5p LMNB1 hsa-miR-27a-3p
hsa-miR-22-5p LHX1 hsa-miR-214-5p
hsa-miR-214-5p KYNU SLC6A15
hsa-miR-2110 KRT5 hsa-miR-21-5p
HELLPAR h h s s a a - - m m i i R R - - 2 1 1 9 - 9 5 b p -5p K K I C F N 5C G3 HELLPAR hsa-miR-199b-5p FASLG
hsa-miR-197-3p IQCH hsa-miR-18a-5p CRB1
hsa-miR-196b-5p IL10
hsa-miR-195-5p HOXC11 hsa-miR-155-5p
h h s s a a - - m m i i R R - - 1 1 9 9 4 3 - b 5 - p 5p H H O M O G K A 1 2 hsa-miR-155-5p CDC25A
hsa-miR-192-5p HELB hsa-miR-151a-5p
hsa-miR-182-5p GABRG2 hsa-miR-146b-5p
hsa-miR-16-5p FASLG
hsa-miR-15b-5p EPHA7 hsa-miR-143-3p
hsa-miR-155-5p CPS1
hsa-miR-151a-5p COL9A1 hsa-miR-140-5p
hsa-miR-146b-5p CHRNB2 hsa-let-7i-5p
hsa-miR-146a-5p CDH1
hsa-miR-145-5p CACNB4 hsa-let-7g-5p
hsa-miR-143-5p BTLA
hsa-miR-140-5p BRCA2 hsa-let-7f-5p
hsa-miR-125b-5p BLM
hsa-miR-101-3p ARHGEF38
hsa-let-7i-5p ADAMTS6
hsa-let-7g-5p ADAM28
hsa-let-7f-5p
numbers of interacting miRNA and mRNA partners (Fig. 3b) and the top affecting a trait) and redundancy of gene functions prevail, for biological
hub lncRNA (HELLPAR; Fig. 3c,d) are shown with their interacting RNAs. insights, we focused on the pathways to which these genes contributed.
The full list of ceRNAs is provided in Supplementary Table 2. As the differential expression at the mRNA level in female participants
showed an 83% overlap with that of male participants, subsequent dis-
cussion focuses on pathways common to both sexes (Fig. 4a). A total
Distinctive pathophysiologies of subtype 1
of n = 174 (male) and n = 166 (female) DE canonical pathways (P ≤ 0.05)
Functional annotation of the DE mRNAs between subtypes was con- were identified. Subtype 1 (versus subtype 2) showed eight main themes
ducted using Ingenuity pathway analysis (IPA) and GSEA. Gene-level dif- of differential expression, which were ranked by P value (these are sum-
ferential expression is recognized, and as pleiotropy (two or more genes marized in Fig. 4a, with full details provided in Supplementary Table 3).
Nature | www.nature.com | 5
tnemhcirnE
tsil deknaR
erocs
cirtem
0.5
0.4
0.2
0.1
0
0.4 0.2 0
tnemhcirnE
tsil deknaR
erocs
cirtem
lncRNAs (men) No ( . n o o f n t - a re rg d e u t n m da R n N t) AsNo m . i o R f N ta A r s get lncRNAs (women) No ( . n o o f n t - a re rg d e u t n m da R n N t) As No m . i o R f N ta A r s get
HELLPAR 43 46 HELLPAR 5 24
XACT 16 39 AC016717.2 5 14
LINC00511 46 26 CASC19 33 14
0.3 DLEU1 17 23 AL365440.1 7 12
P = 0.003 CASC19 78 22 CCDC26 5 12
LINC00943 91 22 DLX6-AS1 75 12
CDKN2B-AS1 63 21 DRAIC 35 12
DLX6-AS1 91 21 LINC00511 44 12
‘Subtype1’ (positively correlated) ‘Subtype1’ (positively correlated) S A O L1 X 1 2 7 - 3 O 2 T 9.1 6 6 5 1 2 2 0 1 L F I I N RR C E 00943 3 1 3 5 1 1 2 1 ‘Subtyp Z e e 2 ro ’ ( c n r e o g s a s t i a v t e 1 ly 1 c ,8 o 0 r 4 related) – – 0 0 . . 2 4 ‘Subtype2 Z ’ e ( r n o e c g r a o t s iv s e a ly t c 1 o 1 r , r 1 e 5 la 0 ted) C FI C R D R C E 26 3 7 2 1 1 9 9 L R I F N P C L 0 1 2 S 389 3 3 8 4 1 1 1 1
CCDC144NL-AS1 60 18 CASC2 51 10
TRG-AS1 105 18 CDKN2B-AS1 67 10
C5orf64 34 17 LINC01748 59 10
Rank in ordered dataset Rank in ordered dataset AC084082.1 23 16 LINC02607 31 10
Enrichment profile Hits Ranking metric Enrichment profile Hits Ranking metric KCNIP4-IT1 72 16 MIR4500HG 55 10
scores scores LINC00461 61 16 PTPRG-AS1 16 10
SILC1 66 10
LINC00707 22 16
SOX2-OT 34 10
LMCD1-AS1 51 16
Fig. 3 | Multilayered RNA cross-talk and hub lncRNAs. a, GSEA plots for individuals. Higher HELLPAR expression in subtype 1 was evident in both sexes
men (left) and women (right) showing significant differential expression (3.52-fold for male and 2.93-fold for female individuals). Nodes represent
of posttranscriptional regulatory processes in both sexes. P values were lncRNAs (dark blue, left), miRNAs (centre) and mRNAs (right), and edges
calculated using permutation tests from GSEA to assess the significance (flow lines) represent interactions, that is, RNA cross-talk in skeletal muscle.
enrichment score. GO BP, gene ontology biological process. b, Top 20 hub Complex higher-order interactions occurred at the lncRNA–miRNA–mRNA
lncRNAs for men (left) and women (right), presented with the corresponding level; hence, multiple flow lines for each target mRNA are described on the
non-redundant numbers of target mRNAs and miRNAs. The hub lncRNAs right. Source data for all the lncRNA–miRNA–mRNA interactions are available
common to both sexes are highlighted in grey. c,d, Cognate binding partner in Supplementary Table 2.
networks of the top hub lncRNA (HELLPAR) for male (c) and female (d)
Article
a
−log[P]
Neuronal and synapses
12.5 Neurovascular coupling signalling
10.0
7.5 CREB signalling in neurons
5.0 GABAergic receptor signalling
2.5
Glutaminergic receptor signalling b d
Potassium channels
Cytokines and cytokine receptors
Glutamate receptor signalling
Acetylcholine signalling Chemoattraction
Neurexins and neuroligins
Synaptic signal transmission
NCAM signalling for neurite outgrowth Inflammasome Tethering and rolling
Synaptogenesis signalling Leucocyte
Acetylcholine receptor signalling
Receptor-type tyrosine-protein phosphatases Cytokine
Neurotransmitter release cycle storm
Immune and inflammatory Pyroptosis Migration
Pathogen-induced cytokine storm Chemokine
Wound healing signalling
Granulocyte adhesion and diapedesis
MSP-RON signalling
Agranulocyte adhesion and diapedesis
Interleukin-4 and interleukin-13 signalling
Differential regulation of cytokine production
Pyroptosis signalling c e
TREM1 signalling Interleukins and Inflammasome and Chemokines and Interstitial
Complement system TNF family pyroptosis cell adhesion migration
Immunoregulatory cell interactions Fold difference Fold difference Fold difference Fold difference
LPS/IL-1- P m h e a d se ia I t I e : d c o in n h ju ib g i a t P i t o X io n R n o / R o f f X R c R X o X R a m e c f n p u t o i o n v b u c a i t t n o i i o o d ti n n c s 7 6 5 4 3 2 IL1 I 2 L R 12 B B 1 1 7 5 2 0 . . . 5 0 5 .0 C G A B S P P 7 5 6 5 4 3 2 CD C 24 5 4 L 6 5 4 3 CLDN14
Phase I: functionalization of compounds IL18RAP GSDMA CLDN16
CD8B
Xenobiotic metabolism CAR signalling IL9 AIM2 CLDN18
Extracellular matrix CD8B2
Collagen degradation IL1B NLRP10 CD96 MMP10
Extracellular matrix organization IL12R2 NLRP11
Degradation of extracellular matrix IL1RAPL2 CXCL3 MMP12
NLRP12
Collagen chain trimerization IL1RL2 CXCL5 MMP13
NLRP13
Activati I o n n te o g f r i m n a c t e r l i l x s m ur e fa ta c l e lo p in r t o e t r e a i c n t a io s n es s IL22RA1 NLRP14 CXCR5 MMP20
Signalling IL23R NLRP2 CXCR6 MMP21
Gα signalling events IL5
Posttranslational protein phosphorylation IL5RA NLRP4 FASLG MMP8
Calcium signalling IL6 NLRP5 ICAM4
nNOS signalling in skeletal muscle cells NLRP6 ICAM5
IL7
GP6 signalling SOCS3 NLRP7 KLRC1
Cell development
NLRP8
Gene activation related to proliferation TNF LECT2
Transcriptional regulation of pluripotent stem NLRP9
cells TNFRSF11B SELE
Activin inhibin signalling pathway TNFSF11 TLR10
Amino acid metabolism
Phenylalanine and tyrosine metabolism TNFSF18
Asparagine degradation I
Haemostasis
Intrinsic prothrombin activation pathway
Coagulation system
Extrinsic prothrombin activation pathway
Fig. 4 | Top Differentially Expressed canonical pathways in subtype 1 leucocyte extravasation (d) and gene expression (e) associated with cellular
versus subtype 2. a, Bubble plot of pathway enrichment in male and female immune response. DE chemokines, cell adhesion molecules and those involved
participants. The colour gradient from high (yellow) to low (blue) indicates in interstitial migration are depicted. The colour gradient from high (yellow) to
the −log[P] calculated using Fisher’s exact test in IPA. b, Schematic of cytokine low (blue) represents the fold difference (subtype 1 versus 2). The schematics in
storm, inflammasome and pyroptosis. c, Gene expression associated parts b and d were created in BioRender. Lab, B. (2025) https://BioRender.com/
with cytokine storm, inflammasome and pyroptosis. DE cytokines, 1fw6v1b.
inflammasome and pyroptosis elements are depicted. d,e, Schematic of
acetylcholine signalling (Fig. 4a). Top DE mRNAs included voltage-
Neurons and synapses gated calcium channels (P < 0.0001), CHRNA6 cholinergic recep-
Top pathways included neurovascular coupling, CREB signalling, tor, GABRA6 and GABRA1 receptors, neurodifferentiation factors
GABAergic and glutaminergic signalling, potassium channels, and NEUROD6 and NEUROD4, MOG (myelin oligodendrocyte glycoprotein)
6 | Nature | www.nature.com
and synaptogamin SYT4. Concordant with GABAergic signalling18,
lncRNA DLX6-AS1, which has been implicated in human GABAergic Haemostasis and coagulation
neuronal function, was among the top DE lncRNAs. Top pathways included intrinsic and extrinsic prothrombin activa-
tion pathways and the coagulation system. Factors of the clotting
Inflammation cascade (F2, F5, F9 and F2R), the α, β and γ subunits of fibrinogen, and
Expression related to cytokines, inflammasome and pyroptosis six kallikreins were prominent. Highly expressed molecules (5–8-fold,
(Fig. 4b,c) was prominent. Pathogen-induced cytokine storm (Fig. 4b,c P < 0.001) included F13B (coagulation factor XIII B subunit).
and Extended Data Fig. 2) included mRNAs encoding multiple cytokines
and cytokine receptors and inflammasome and pyroptosis elements
Comparison with rodent models
(Fig. 4c), as well as mRNAs involved in cellular immune response
(Fig. 4d,e). The DE ceRNAs included lncRNAs CASC19, FIRRE, EGOT Developing an alignment of animal models with clinical cachexia enti-
and SOX2, as well as miRNAs hsa-let-7g-5p, hsa-miR-146b-5p and ties will be an important and challenging phase of cachexia research,
hsa-miR-21-5p (associated with inflammatory myopathy and other and our human data provide an opportunity to attempt such alignment.
inflammatory disorders19 and cytokine storm signalling). The differential expression of mRNAs between human female subtypes
1 and 2 was compared with that observed in gastrocnemius of female
Xenobiotic metabolism rats injected with a colon adenocarcinoma with or without treatment
Top pathways mapped to PXR/RXR activation, phase I (functionaliza- with FOLFIRI chemotherapy23, as colon cancer with and without chemo-
tion of compounds) and phase II (conjugation of compounds). This therapy were clinical features of around half of the patients in our biopsy
signal included high expression of several cytochrome P450 enzymes, cohort (Fig. 5 and Supplementary Tables 4 and 5). In these rat studies,
UDP-glucuronosyl-transferases and sulfotransferases. Xenobiotic path- we observed tumour-induced loss of median fibre cross-sectional area
ways mapped to degradation of exogenous compounds (for instance, (from 2,607 µm2 to 2,030 µm2, −22%; P < 0.05); further 22% muscle loss
nicotine and bupropion) and endogenous compounds (including ara- was seen in tumour-bearing rats after treatment with two cycles of
chidonic acid, melatonin and steroid hormones). Highly expressed chemotherapy (to 1,579 µm2, P < 0.05). At the transcript level, there was
mRNAs (P < 0.001) included UGT3A2, SULT2B1 and SULT2A1, which 98% discordance between human subtype DE and rat DE datasets and
encode phase II enzymes that mediate the sulfation of steroids and 95.6% discordance at the pathway level (Fig. 5); concordance was limited
sterols, and CYP2C19, which encodes a cytochrome P450 involved in to the extracellular matrix domain. Pathways exclusive to humans were
the metabolism of polyunsaturated fatty acids and drugs. Regulators neuronal system and synapses, cytokine storm and cellular immune
of xenobiotic metabolism20 hsa-miR-495-3p and hsa-miR-370-3p were response, and xenobiotic metabolism (as well as signalling, amino
among the top DE miRNAs. acid metabolism and haemostasis) (Fig. 5), whereas those exclusive
to rats (for the tumour and tumour plus chemotherapy groups) were
Extracellular matrix stress-related transcriptional regulation and canonical atrophy gene
Top pathways mapped to collagen degradation, extracellular matrix program.
organization, degradation of the extracellular matrix, collagen chain Neyroud et al.24 conducted a time series study of diaphragm RNA
trimerization, matrix metalloprotease activation and integrin–surface expression in murine pancreatic cancer, encompassing days 8, 10, 12
interactions (Extended Data Fig. 3). This expression pattern included and 14 and the humane end point mandated by the Institutional Animal
several DE collagens and matrix metalloproteinases. Highly expressed Care and Use Committee (15–18 days), in male mice injected orthotopi-
mRNAs (P < 0.001) included COL9A1, MMP10 and MMP8. cally with pancreatic adenocarcinoma. The animal welfare criterion for
this end point was body condition score 2 (segmentation of vertebral
Signal transduction column evident and dorsal pelvic bones readily palpable, reflecting
Various pathways mapped to signal transduction, including intracellu- advanced cachexia). As in our patients, predominant atrophy of type
lar and second messenger signalling and posttranslational modification IIA and type IIX fibres was noted. Canonical pathways identified in the
of proteins. Top canonical pathways included receptor Gα signalling, late disease stage in male mice (days 14–18, GSE271521) overlapped
posttranslational protein phosphorylation, calcium signalling, nNOS considerably with those discovered by RNAome-based classification in
signalling in skeletal muscle cells and GP6 signalling. men (Extended Data Fig. 5). This overlap encompassed neural, inflam-
matory, extracellular matrix, haemostasis and signal transduction
Cell development pathways. At day 8 in the (male) mouse diaphragm, 23 single transcripts
Top pathways mapped to gene activation related to proliferation and matched the top 800 DE mRNA in male subtype 1 (2.9% overlap); this
transcriptional regulation of pluripotent stem cells, including embry- increased to 334 matching transcripts (41.7% overlap) in the late mouse
onic myosin (MYH13), transcription factor GATA4, which is involved in cachexia stage (days 15–18). In a related study25, several modifications
embryogenesis, pluripotency-related factors ISL1, NANOG, DPPA4 and were made to the KPC model to extend the time course and increase the
POU5F1, and factors involved in determination of cell fate (EOMES and rate of metastasis to approximately 70%. At metastatic (as opposed to
SOX2), as well as the C and D subunits of inhibin β and seven of the nine locally advanced) disease, the transcriptome of tibialis anterior showed
members of the paired box (PAX) family of transcription factors (PAX1, several signals in common with subtype 1, that is, ECM organization,
PAX2, PAX4, PAX5, PAX6, PAX8 and PAX9), which are associated with the regulation of neurogenesis and dendrite formation, muscle cell dif-
activin inhibin signalling pathway. ferentiation and developmental morphogenesis.
Protein and amino acid metabolism
Discussion
Canonical pathways for phenylalanine and tyrosine metabolism and
asparagine degradation were identified by IPA. GSEA included gene We analysed the transcriptional landscape of rectus abdominis in
sets encompassing amino acid metabolism more broadly (Extended patients with cancer using high-throughput next-generation sequenc-
Data Fig. 4), for instance, aspartate family amino acid catabolic process. ing. The use of intNMF to integrate multiomics signatures from tumour
Although proteolysis is transcriptionally upregulated in muscle atrophy gene expression with mutational patterns and pathway discovery has
in rodent models21,22, no elements of ub/proteasome and none of the previously been established; we built on this here to group patients
135 ‘atrogin program’ genes22 were DE, including the ubiquitin ligases according to their coregulated transcriptional patterns and gain
taken as ‘sentinel’ of muscle atrophy (FBXO32 and TRIM63). insights into muscle biology. Using intNMF with stringent quality
Nature | www.nature.com | 7
Article
D ex if p fe re re s n s t io ia n l T h v u e e m a rs lt o u h u s y r ver T s c u u h m s e o m h u e o r a . + lthy C ca a c c v h h e e e n r x x o s i i u a a s ( ( S S 2 1 ) ) t d r r e a a s t n e a s a s c e r r c t i . h p T t i h n o e m r e c e e la a R t n N e a d A l y d n s o e is m t w to a o i g n rk e s s n i n i e d r w e a n t h e t i i c a f h i n e t o d h p i e n e r n o o - u l s e r o s s u t o r u c f d e n y o m a n u l - l s c o c o w l d e l i i R n n N g ka A R g o N e m A to e s
have been determined and targeting networks of lncRNAs has already
Neuronal system and synapses
Glutaminergic receptor signalling pathway −log[P] been raised as a therapeutic possibility. Experimental studies sug-
GABAergic receptor signalling pathway 10 gest high expression of regulatory lncRNAs and miRNAs in skeletal
Glutamate P o re ta c s e s p iu to m r s c i h g a n n a n lli e n l g s 4 muscle compared with other tissues26,27. Likewise, the involvement of
2
Acetylcholine receptor signalling pathway lncR NAs and miRNAs in cytokine storm in respiratory infection is under
Cy P t a o t k h in o e g e s n to -i r n m d u a c n e d d c c e y ll t u o l k a i r n i e m s m to u r n m e s re ig s n p a o l n lin s g e intense study28,29, and similar cytokine storm signals were observed
Wound healing signalling pathway in the muscle of patients of subtype 1, including mRNA, miRNA and
Exclusive
Granulocyte adhesion and diapedesis to lncRNA species.
Agranulocyte adhesion and diapedesis humans
IL-23 signalling pathway This study contributes to our understanding of perturbed muscle
Xenobiotic metabolism biology in malignant disease on the basis of the differential gene signa-
Phase I: Functionalization of compounds
LXR/RXR activation tures identified between the two subtypes. More research is required to
PXR/RXR activation understand the implications of these diverse signals in human cancer
Phase II: conjugation of compounds
LPS/IL-1-mediated inhibition of RXR function cachexia. Neuromuscular systems adapt to the demands of contractile
Extracellular matrix work and disease by means of two-way interactions between nerves
Extracellular matrix organization
Degradation of the extracellular matrix and muscle cells; however, these have barely been studied in cancer
Integrin cell surface interactions Common cachexia. In a morphological study of neuromuscular junctions in
Collagen biosynthesis and modifying enzymes
Collagen chain trimerization rectus abdominis of patients with cachexia, neuromuscular junction
Stress-related transcriptional regulation structure was unchanged compared with those of healthy controls and
Processing capped intron-containing pre-mRNA weight-stable patients with cancer30. Observations in mice bearing C26
EIF2 signalling
Non-homologous end-joining tumours included lower muscle force, motor unit connectivity, action
Nucleosome assembly potential and number of motor units31, as well as loss of neuromuscular
Eukaryotic translation initiation
DNA methylation Exclusive to junction integrity and myofibre denervation32.
rR C N a A no p n r i o c c a e l s a s tr i o n p g h in y t g h e e n e n s u c a l n e d ol u re s l a a t n e d d c s y ig to n s a o ls l mu ra s t c s l e w f i r t o h m The IL-1, IL-6 and TNF-family cytokines have catabolic effects on mus-
Deubiquitination tum ch o e u m rs o a . nd cle cells33,34, and muscle actively participates in immune response35,36
STAT3 pathway through cell receptors, including Toll-like, cytokine and NOD-like
Unfolded protein response
Cachexia signalling pathway receptors, and the NLRP inflammasome. Signals suggesting leuco-
FOXO-mediated transcription of cell death genes cyte extravasation are concordant with findings from murine KPC
E3 ubiquitin ligases ubiquitinate target proteins
models that immune cells orchestrate cachexia by infiltrating the liver,
Adipogenesis
Transcriptional regulation of white adipocyte Exclusive to central nervous system37,38 and skeletal muscles39. The complex hyper-
differentiation muscle from
Stearate biosynthesis I rats with inflammation of muscle in patients with cancer seems likely to require
Fatty acyl-CoA biosynthesis tumours immune-modulating therapeutic strategies rather than non-steroidal
anti-inflammatory drugs or antibodies inactivating single cytokines.
Fig. 5 | Comparison of canonical pathways in rat model compared with
Signals for embryogenesis and stem cells include key transcription
human molecular subtype. Results of an experimental study in female rats
were compared with the expression profile of human female subtype 1. Next- factors (POU5F1, SOX2, NANOG), which bind to promoters and activate
generation RNA-seq of gastrocnemius muscle was conducted in healthy rats, at least 353 genes that comprise the core transcriptional network of
rats implanted with colon tumours, and rats implanted with tumours and pluripotent stem cells. This could be related to alterations in stem
subsequently given two cycles of chemotherapy. DE canonical pathways are cell proliferation and differentiation that have been characterized in
indicated for: (1) muscle mRNAs from female rats implanted with tumours animal models of cancer cachexia40–42. Signals related to extracellular
versus the healthy control group; (2) muscle mRNAs from female rats with matrix are consistently strong across animal models of cachexia, and
tumour implantation plus chemotherapy (chemo.) versus the healthy control the rectus abdominis of patients with pancreatic cancer shows evidence
group; and (3) human (female) cachexia subtype 1 (S1) versus subtype 2 (S2). of expansion of connective tissue43. It has also been suggested that
Canonical pathways exclusive to humans, those overlapping between human muscle fibrosis occurs in a murine LLC model with cachexia44. Neyroud
and rat datasets, and those that were found to be unique in rats with tumours
et al.24 demonstrated in murine KPC models that leucocyte infiltration
and/or chemotherapy are depicted. Each bubble represents the enrichment of
and expansion of PDGFRα mesenchymal progenitors precedes ECM
representative pathways in humans and/or rat datasets, with the colour
remodelling in diaphragm.
corresponding to the pathway category and the size of the bubble corresponding
Cancer cachexia is a complex ‘metabolic disorder’45 in which dis-
to the −log[P] calculated using Fisher’s exact test from IPA; pathways were
considered statistically significant if they met the criterion of −log[P] ≤ 1.3. turbed catabolism of amino acids in muscle has been well character-
The human, female rat, tumour and syringe images were created in BioRender. ized. We observed upregulation of phase I and phase II metabolism of
Lab, B. (2025) https://BioRender.com/5tbaubn. compounds, with potentially far-reaching effects. Cytochrome P450
enzymes metabolize endogenous compounds such as lipids, proteins
and hormones, and sulfotransferases are involved in the metabolism
metrics for clustering, we identified two highly coherent molecular of catecholamines and thyroid and steroid hormones. Dysregulation
subtypes of skeletal muscle. RNAome-based subtypes transcended of these pathways could contribute to endocrine disorders and altered
age, comorbidity, primary tumour site, cancer stage, systemic cancer fatty acid metabolism, cholesterol synthesis and bile acid biosynthesis.
therapy and patient sex (none of these features drove the clustering). This study had several limitations. Owing to ethical, scientific and
Subtype 1 was cachexia-related and based on patients’ high-grade practical considerations, no muscles from matched healthy controls
weight loss, low muscle mass, type II fibre atrophy and shortened were available. Muscle biopsy is invasive and is considered to have no
median survival. direct benefit to study participants46. The lack of healthy participants
Our approach to clinical classification of cachexia was based on notwithstanding, the long survival and youthful SMI of patients of
precise radiologically defined criteria for muscle mass and muscle subtype 2 suggested that they could serve as internal controls for the
loss. Other strengths of our approach included unbiased sampling, study cohort. There remain some limitations of clinical cachexia clas-
characterization of sexual dimorphism and leverage of unbiased sification. The lifelong SMI of patients is unknown, so whether their SMI
8 | Nature | www.nature.com
was inherently high or low long before the cancer diagnosis cannot be 5. Martin, L. et al. Cancer cachexia in the age of obesity: skeletal muscle depletion is a
discerned. The new classification will be nonetheless useful in future powerful prognostic factor, independent of body mass index. J. Clin. Oncol. 31, 1539–1547
(2013).
studies for stratification and analysis of key criteria of muscle mass 6. Stretch, C. et al. Effects of sample size on differential gene expression, rank order and
and muscle loss that are strongly related to tissue-level morphology prediction accuracy of a gene signature. PLoS ONE 8, e65380 (2013).
7. Talbert, E. E. et al. Modeling human cancer-induced cachexia. Cell Rep. 28, 1612–1622.
and biology. Skeletal muscle is a heterogeneous tissue consisting of
e1614 (2019).
multinucleated muscle fibres, immune cells, endothelial cells, muscle 8. Narasimhan, A. et al. Profiling of adipose and skeletal muscle in human pancreatic cancer
stem cells and non-myogenic mesenchymal progenitors. RNA-seq at cachexia reveals distinct gene profiles with convergent pathways. Cancers 13, 1975
(2021).
single-cell resolution will be necessary to clarify cell-specific gene
9. Baracos, V. E., Martin, L., Korc, M., Guttridge, D. C. & Fearon, K. C. H. Cancer-associated
expression. Future studies should focus on the non-coding part of the cachexia. Nat. Rev. Dis. Primers 4, 17105 (2018).
genome that we have identified to be clearly sexually dimorphic. Cancer 10. Zhao, K. et al. Transcriptomic signature of cancer cachexia by integration of machine
learning, literature mining and meta-analysis. Comput. Biol. Med. 172, 108233 (2024).
cachexia research has been limited in part by a lack of experimental
11. Brunet, J. P., Tamayo, P., Golub, T. R. & Mesirov, J. P. Metagenes and molecular pattern
models that have been proven to recapitulate the clinical entity. We con- discovery using matrix factorization. Proc. Natl Acad. Sci. USA 101, 4164–4169 (2004).
ducted a few comparisons between animal models and the DE mRNAs 12. Carmona-Saez, P., Pascual-Marqui, R. D., Tirado, F., Carazo, J. M. & Pascual-Montano, A.
Biclustering of gene expression data by non-smooth non-negative matrix factorization.
between our RNAome-based subtypes, revealing both differences and
BMC Bioinformatics 7, 78 (2006).
similarities. One difference was the lack of signals for the canonical 13. Martin, L. et al. Diagnostic criteria for the classification of cancer-associated weight loss.
atrophy gene program between subtypes, a result concordant with J. Clin. Oncol. 33, 90–99 (2015).
previous human muscle biopsy studies47 but discordant with findings 14. Zhong, X. & Zimmers, T. A. Sex differences in cancer cachexia. Curr. Osteoporos. Rep. 18,
646–654 (2020).
in rodent models. We noted similarities between our subtype-specific 15. Fearon, K. et al. Definition and classification of cancer cachexia: an international
expression in transcripts and canonical pathways in diaphragm of mice consensus. Lancet Oncol. 12, 489–495 (2011).
with advanced pancreatic cancer (syngeneic KPC model)24. In another 16. Folker, E. S. & Baylies, M. K. Nuclear positioning in muscle development and disease.
Front. Physiol. 4, 363 (2013).
study, diaphragm of immunosuppressed (PDX) mice with implantation 17. Tay, Y., Rinn, J. & Pandolfi, P. P. The multilayered complexity of ceRNA crosstalk and
of a human pancreatic cancer showed expression signatures (immune competition. Nature 505, 344–352 (2014).
18. Aouci, R. et al. The antidepressant action of fluoxetine involves the inhibition of Dlx5/6 in
system regulation and extracellular matrix) overlapping with those
cortical GABAergic neurons through a TrkB-dependent pathway. Cells 13, 1262 (2024).
observed in rectus abdominis of the patient48. However, humans with 19. Lu, Y. et al. The NF-κB-responsive long noncoding RNA FIRRE regulates posttranscriptional
cachexia and current rodent models differ fundamentally. Rodents are regulation of inflammatory gene expression through interacting with hnRNPU. J. Immunol.
199, 3571–3582 (2017).
typically young and healthy, whereas patients are older and polymor-
20. Li, D. et al. MicroRNAs hsa-miR-495-3p and hsa-miR-486-5p suppress basal and
bid2. Intrinsic differences among muscles exist (for instance, fibre type rifampicin-induced expression of human sulfotransferase 2A1 (SULT2A1) by facilitating
and transcriptional responses49) and have been noted in rodents, but mRNA degradation. Biochem. Pharmacol. 169, 113617 (2019).
21. Lecker, S. H. et al. Multiple types of skeletal muscle atrophy involve a common program
human studies have been limited to one or a few muscles accessible at
of changes in gene expression. FASEB J. 18, 39–51 (2004).
surgery. Experiments in animal models have demonstrated that cancer 22. Peris-Moreno, D., Cussonneau, L., Combaret, L., Polge, C. & Taillandier, D. Ubiquitin ligases
cachexia evolves across early, intermediate and late stages in an ordered at the heart of skeletal muscle atrophy control. Molecules 26, 407 (2021).
23. Almasud, A. A. et al. Fish oil mitigates myosteatosis and improves chemotherapy efficacy
sequence24; however, any temporal alignment between humans and
in a preclinical model of colon cancer. PLoS ONE 12, e0183576 (2017).
animals remains elusive. The point of genesis of muscle wasting in 24. Neyroud, D. et al. Local inflammation precedes diaphragm wasting and fibrotic remodelling
patients with cancer is unknown, although recent findings indicate that in a mouse model of pancreatic cancer. J. Cachexia Sarcopenia Muscle 16, e13668
(2025).
skeletal muscle depletion may be occurring up to 18 months before the
25. Spadafora, V. et al. Optimization of a mouse model of pancreatic cancer to simulate the
clinical diagnosis of pancreatic cancer50. human phenotypes of metastasis and cachexia. BMC Cancer 24, 414 (2024).
Collectively, our results indicate a muscle disorder of daunting 26. Chen, R., Lei, S., Jiang, T., She, Y. & Shi, H. Regulation of skeletal muscle atrophy in
cachexia by microRNAs and long non-coding RNAs. Front. Cell Dev. Biol. 8, 577010
complexity. Participation of regulatory lncRNAs and miRNAs seems (2020).
to be extensive; thus, future exploration of top regulatory lncRNAs 27. Cesana, M. et al. A long noncoding RNA controls muscle differentiation by functioning as
(hub lncRNAs) could be a promising avenue. A multiplex approach a competing endogenous RNA. Cell 147, 358–369 (2011).
28. Mukherjee, S., Banerjee, B., Karasik, D. & Frenkel-Morgenstern, M. mRNA-lncRNA
involving simultaneous knockdown, knockout or overexpression co-expression network analysis reveals the role of lncRNAs in immune dysfunction during
of multiple lncRNA targets could provide valuable insights into the severe SARS-CoV-2 infection. Viruses 13, 402 (2021).
functional significance of lncRNAs. Techniques such as CRISPR–Cas9 29. Arman, K., Dalloul, Z. & Bozgeyik, E. Emerging role of microRNAs and long non-coding
RNAs in COVID-19 with implications to therapeutics. Gene 861, 147232 (2023).
for gene knockout and use of short interfering RNAs or antisense oli- 30. Boehm, I. et al. Neuromuscular junctions are stable in patients with cancer cachexia.
gonucleotides for knockdown and lentiviral or adenoviral vectors J. Clin. Invest. 130, 1461–1465 (2020).
for overexpression would enable effective and specific manipula- 31. Huot, J. R., Pin, F. & Bonetto, A. Muscle weakness caused by cancer and chemotherapy is
associated with loss of motor unit connectivity. Am. J. Cancer Res. 11, 2990–3001 (2021).
tion of multiple lncRNA targets in relevant in vitro and in vivo mod- 32. Sartori, R. et al. Perturbed BMP signaling and denervation promote muscle wasting in
els of cancer cachexia. Disruption of RNA cross-talk could offer a cancer cachexia. Sci. Transl. Med. 13, eaay9592 (2021).
33. Webster, J. M., Kempen, L., Hardy, R. S. & Langen, R. C. J. Inflammation and skeletal
means of understanding muscle wasting beyond iterative study of
muscle wasting during cachexia. Front. Physiol. 11, 597675 (2020).
single mRNAs. 34. Baazim, H., Antonio-Herrera, L. & Bergthaler, A. The interplay of immunology and
cachexia in infection and cancer. Nat. Rev. Immunol. 22, 309–321 (2022).
35. Lang, C. H. Importance of the innate immune response in skeletal muscle to depsis-
Online content induced alterations in protein balance. Shock 59, 214–223 (2023).
36. Frost, R. A., Nystrom, G. J. & Lang, C. H. Multiple Toll-like receptor ligands induce an IL-6
Any methods, additional references, Nature Portfolio reporting summa- transcriptional response in skeletal myocytes. Am. J. Physiol. Regul. Integr. Comp. Physiol.
290, R773–R784 (2006).
ries, source data, extended data, supplementary information, acknowl-
37. Olson, B., Diba, P., Korzun, T. & Marks, D. L. Neural mechanisms of cancer cachexia.
edgements, peer review information; details of author contributions Cancers 13, 3990 (2021).
and competing interests; and statements of data and code availability 38. Burfeind, K. G. et al. Circulating myeloid cells invade the central nervous system to mediate
cachexia during pancreatic cancer. eLife 9, e54095 (2020).
are available at https://doi.org/10.1038/s41586-025-09502-0.
39. Dzierlega, K. et al. Activin A-expressing polymorphonuclear myeloid-derived suppressor
cells infiltrate skeletal and cardiac muscle and promote cancer cachexia. J. Immunol. 211,
1. Xia, L. et al. Sarcopenia and adverse health-related outcomes: an umbrella review of 497–507 (2023).
meta-analyses of observational studies. Cancer Med 9, 7964–7978 (2020). 40. Wang, R. et al. A human skeletal muscle stem/myotube model reveals multiple signaling
2. Anoveros-Barrera, A. et al. Clinical and biological characterization of skeletal muscle tissue targets of cancer secretome in skeletal muscle. iScience 26, 106541 (2023).
biopsies of surgical cancer patients. J. Cachexia Sarcopenia Muscle 10, 1356–1377 (2019). 41. Arneson, P. C. & Doles, J. D. Impaired muscle regeneration in cancer-associated cachexia.
3. Chalise, P. & Fridley, B. L. Integrative clustering of multi-level ‘omic data based on Trends Cancer 5, 579–582 (2019).
non-negative matrix factorization algorithm. PLoS ONE 12, e0176278 (2017). 42. Brzeszczynska, J. et al. Loss of oxidative defense and potential blockade of satellite cell
4. Roeland, E. J. et al. Weight loss versus muscle loss: re-evaluating inclusion criteria for maturation in the skeletal muscle of patients with cancer but not in the healthy elderly.
future cancer cachexia interventional trials. Support. Care Cancer 25, 365–369 (2017). Aging 8, 1690–1702 (2016).
Nature | www.nature.com | 9
Article
43. Judge, S. M. et al. Skeletal muscle fibrosis in pancreatic cancer patients with respect to 49. Terry, E. E. et al. Transcriptional profiling reveals extraordinary diversity among skeletal
survival. JNCI Cancer Spectr. 2, pky043 (2018). muscle tissues. eLife 7, e34613 (2018).
44. Washington, T. A. et al. Development of skeletal muscle fibrosis in a rodent model of 50. Babic, A. et al. Adipose tissue and skeletal muscle wasting precede clinical diagnosis of
cancer cachexia. Cell Biochem. Funct. 41, 478–489 (2023). pancreatic cancer. Nat. Commun. 14, 4317 (2023).
45. Berriel Diaz, M., Rohm, M. & Herzig, S. Cancer cachexia: multilevel metabolic dysfunction.
Nat. Metab. 6, 2222–2245 (2024). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
46. Levit, L. A. et al. Ethical framework for including research biopsies in oncology clinical published maps and institutional affiliations.
trials: American Society of Clinical Oncology Research Statement. J. Clin. Oncol. 37,
2368–2377 (2019). Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this
47. Gallagher, I. J. et al. Suppression of skeletal muscle turnover in cancer cachexia: article under a publishing agreement with the author(s) or other rightsholder(s); author
evidence from the transcriptome in sequential human muscle biopsies. Clin. Cancer Res. self-archiving of the accepted manuscript version of this article is solely governed by the
18, 2817–2827 (2012). terms of such publishing agreement and applicable law.
48. Nosacka, R. L. et al. Distinct cachexia profiles in response to human pancreatic tumours
in mouse limb and respiratory muscle. J. Cachexia Sarcopenia Muscle 11, 820–837 (2020). © The Author(s), under exclusive licence to Springer Nature Limited 2025
10 | Nature | www.nature.com
Methods
Clinical classification of cachexia by grading of weight loss
Accrual of human skeletal muscle biopsies Grading was conducted as described by Martin et al.13 with the addition
Rectus abdominis biopsy tissues were accessed from the Hepatopan- of a radiological confirmation step. Radiological review consisted of
creaticobiliary/Gastrointestinal Tumor Bank (University of Calgary, precise quantification of muscle loss percentage and fat loss percentage
Alberta, Canada). Tumour bank participants provided written informed in the time frame immediately before the biopsy during a median scan
consent, and the tissue banking was approved by the Conjoint Health interval of 101 (interquartile range: 63–165) days, which was available
Research Ethics Board at the University of Calgary (ethics ID: E17213). in clinical records for 85% of our patients. Arguably, the clinical feature
Patients undergoing elective abdominal surgery were consecutively of direct relevance to muscle biopsy is muscle loss rather than overall
approached about participation in tumour and tissue banking. The weight loss. There is clear evidence that fat loss may occur without mus-
study cohort and conditions for the acquisition of muscle samples cle loss52, and that often apparently weight-stable individuals are losing
were as described previously6,51. Briefly, rectus abdominis samples muscle with concurrent fat gain4. For patients whose clinical record
(0.5–3.0 g) were collected during open abdominal surgery scheduled of weight loss was discrepant with their CT-confirmed muscle loss,
as part of routine clinical care. An upper abdominal transverse incision the percentage muscle loss confirmed by CT was taken in preference.
was performed, and muscle biopsy was obtained at opening by sharp
dissection, without use of electrocautery. Muscle biopsies were taken Clinical classification of cachexia by classification of muscularity
within 30 min of the start of the surgery and immediately flash-frozen The emergence of L3-SMI values from healthy young adults enabled
in liquid nitrogen to minimize ischaemic shock after devitalization. For SMI values of patients to be expressed in relation to a reference popula-
histology, a subsample of the muscle was frozen in isopentane cooled tion53,54. We used L3-SMI sex-specific reference values to classify high
in liquid nitrogen. All samples were stored at −80 °C until further use. SMI (male, SMI ≥ 60.9 cm2 m−2; female, SMI ≥ 47.5 cm2 m−2). This refer-
Rectus abdominis was chosen because it is accessible in many abdom- ence sample (n = 735) included L3-CT imaging of healthy 30-year-old
inal cancer surgeries and is the muscle most frequently chosen for kidney donors from a similar population demographic (central USA)
study of cancer-associated changes2. Whether rectus abdominis can to our central Canadian cohort. Categorical low SMI was defined as
be taken as representative of cachexia-related changes has not been SMI ≤ −1.0 standard deviations below the sex-specific and age-specific
proven; however, most of the putative influences on muscle in malig- mean for patients in our population cohort (Fig. 1d). All others falling
nant disease (circulating tumour and inflammatory mediators, altered between these benchmarks were classified as having medium SMI.
hormonal levels, deficiency of energy fuels and essential nutrients) The SMI distribution for older, polymorbid people with a diagnosis
have been suggested to be systemic9. The release of n = 84 samples of cancer crossed over the distribution of SMI values of healthy young
from the bank for whole-transcriptome profiling and n = 70 samples individuals. This was previously reported for patients in our biopsy
for histology, as well as patient information (demographic, clinical pipeline2, as well as in published work for other primary tumour sites53.
and operative data) from medical records, was performed under pro-
tocol ID CC-17-0432, authorized by the Health Research Ethics Board of Immunofluorescence of fibre types, laminin and dystrophin,
Alberta Cancer Committee. Only samples from patients with pancreatic and nuclei
cancer or colorectal cancer with liver metastasis were included; this Muscle serial sections (10 µm) were cryosectioned transversely with
was because of the relatively high prevalence of weight loss in these a Leica CM300 cryostat at −22 °C and stored at −80 °C until staining.
cancers, and also to limit heterogeneity. Primary antibodies for differential myosin heavy chain (MYH) gene
expression (MyHC I, IIX and IIA) and secondary antibodies were as
Patient recruitment and demographic and clinical data described in Supplementary Table 6. After application of the secondary
acquisition antibody, a nuclear stain (4′,6‐diamidino‐2‐phenylindole) was added for
Medical records were accessed to obtain patient clinical history (demo- 2 min, followed by washing. Sections were mounted on Apex Superior
graphic, clinical and survival data) and included the following charac- adhesive slides (Leica Biosystems), covered and dried for 12 h. Images of
teristics: age (more than 18 years), weight history over time, height, tissue sections were acquired using a ×20/0.85 oil lens with a spinning
BMI (weight (kg)/height (m2)), sex, cancer type, date of surgery, and disk confocal microscope (Quorum Wave FX Spinning Disc Confocal
time from surgery to death or censoring. Percentage weight loss was System, Quorum Technologies). Individual Z‐stacked images were
calculated as: assembled to create a composite image of a whole-tissue cross-section.
Tissue images were captured and analysed with Volocity 6.3 software
(currentweight−previousweight~(6~months))/previousweight×100.
(PerkinElmer). A software script was developed to identify and auto-
matically quantify muscle fibre types (I, IIA, IIX) on the basis of MyHC
Patients were assigned composite grades based on the weight loss staining intensity. Mean muscle fibre area (µm2) was calculated on
BMI grading system ranging from 0–4. the basis of detection of membrane (laminin or dystrophin antibody)
fluorescence of muscle fibres in a cross-section. The percentage of
Body composition analyses fibres with central nuclei was manually assessed by selecting muscle
Cross-sectional CT imaging was used to assess body composition fibres with mispositioned nuclei (clearly separated from sarcolemma,
using a single axial image at lumbar vertebra 3 (L3). Preoperative CT equidistant or not).
images were quantified for muscle and fat tissue cross-sectional area
(cm2) using Slice-O-Matic software (v.6 Rev-10, TomoVision). Single Next-generation sequencing profiling of human transcriptome
and consecutive CTs obtained preoperatively at L3 were analysed. from skeletal muscle
Muscle radiation attenuation was measured and reported in Hounsfield Transcriptome data generation was performed in a single batch.
units (HU) (range: −29 to +150 HU). The specific HU ranges for fat com- RNA extraction was performed using the TRIzol method and a Qia-
ponents were as follows: −190 to −30 for subcutaneous adipose tissue gen RNeasy midi kit. The optical density 260/280 ratio was measured
and intramuscular adipose tissue and −150 to −50 for visceral adipose using a NanoDrop instrument, and the RNA integrity number (RIN)
tissue. Total adipose tissue was computed as the sum of subcutaneous, was assessed using an Agilent 2100 Bioanalyzer for all samples. The
visceral and intramuscular adipose tissue. Muscle and total adipose Genome Quebec facility (Montreal, Canada) provided services for
tissue cross-sectional areas were normalized for stature and reported library preparation and whole-transcriptome sequencing of RNA
as SMI (cm2 m−2) and total adipose tissue index (cm2 m−2), respectively. from human skeletal muscle. Preprocessing of isolated total RNA and
Article
downstream processing of samples were performed per the manufac- classes was performed using the DESeq2 (ref. 59) R package. RNAs were
turer’s instructions, as summarized. considered to be DE at a fold-change cutoff of 1.5 and P < 0.05 (unad-
justed), and an adjusted (by false discovery rate) P < 0.05.
rRNA-depleted sequencing
Total RNA was quantified, and its RIN was assessed using a 5K/RNA/ intNMF clustering to identify molecular subtypes of human
Charge Variant Assay LabChip and RNA Assay Reagent Kit (Perkin skeletal muscle
Elmer). All samples had RIN values greater than 5 (90% of samples had Using one RNA class to identify the molecular subtype of muscle does
RIN > 6), and one sample had a RIN of 4.3. The RNA quality was based not provide an intuitive understanding and holistic picture of the
on the RIN for paired-end sequencing using rRNA-depleted libraries underlying pathophysiology. Integrative unsupervised approaches
for RNA-seq, and small RNA-seq was shown to have no dependence are therefore necessary. We performed sex-specific integrative analyses
on RIN (except for poly-A-enriched RNA library preparation). Quality for all RNA classes. The filtered, normalized and transformed (sam-
indices were consistently obtained and surpassed the recommended ple × gene) matrix was subjected to intNMF analysis using R package
thresholds for assessment of library and sequence quality scores. rRNA intNMF. An integrative analysis was implemented, combining all the
was depleted from 250 ng of total RNA using QIAseq FastSelect (Human RNA classes to determine the molecular subtypes of human skeletal
96rxns). New England Biolabs provided the following reagents and kits, muscle. The intNMF algorithm was run at 100 and 300 iterations using
including adapters and primers for the complementary DNA (cDNA) a random initializing seed parameter of an optimal number of clusters,
synthesis: NEBNext RNA First-Strand Synthesis and NEBNext Ultra 2–5 (K = 2:5), with five-fold cross-validation and Euclidean distance as
Directional RNA Second Strand Synthesis Modules. The remaining the distance metric. The optimal number of clusters was selected on
steps of the library preparation were performed using a NEBNext Ultra the basis of the study sample size within the clusters, with the cluster
II DNA Library Prep Kit for Illumina. Libraries were quantified using a prediction index and silhouette width as quality indices.
Quant-iT PicoGreen dsDNA Assay Kit (Life Technologies) and Kapa
Illumina GA with Revised Primers-SYBR Fast Universal kit (Kapa Bio- Statistical analysis
systems). The average size fragment was determined using a LabChip Statistical analyses were performed using RStudio build 748 (R v.4.1.0)
GX (PerkinElmer) instrument. and SPSS v.27. Differences between groups were analysed using an
The libraries were normalized, pooled and then denatured in 0.05 N independent t-test for continuous variables and Pearson’s χ2 test or
NaOH and neutralized using HT1 buffer. The pooled libraries were Fischer’s exact test for categorical variables. Non-normally distrib-
loaded at 225 pM on an Illumina NovaSeq S4 lane using the Xp protocol uted variables were compared using the Mann–Whitney U-test. Cor-
per the manufacturer’s recommendations. The run was performed for relations between continuous variables were assessed using Pearson
2 × 100 cycles (paired-end mode). A phiX library was used as a control correlation coefficients with the Hmisc and corrplot R packages. The
and mixed with libraries at a 1% level. All samples had a Phred qual- Kaplan–Meier method was used to identify associations of subtypes
ity score greater than 30, per the manufacturer’s recommendations. with overall survival, and log-rank tests were used to compare the sur-
Base-calling was performed with RTA v.3.4.4, and bcl2fastq2 v.2.20 was vival curves. Univariable and multivariable analyses for overall survival
then used to demultiplex samples and generate fastq reads. were performed using the Cox proportional hazards model. Results
were considered to be significant at P < 0.05.
Small RNA-seq
Total RNA was quantified, and its integrity (RIN) was assessed as Next-generation sequencing of gastrocnemius rat model system
described above for the RNA-seq protocol. Libraries were generated of muscle atrophy
from 300–800 ng of total RNA using a NEBNext Multiplex Small RNA All methods pertinent to rodent models were approved by the Univer-
Library Prep Kit for Illumina, per the manufacturer’s recommenda- sity of Alberta IACUC and conducted in accordance with the Guide-
tions. cDNA constructs were purified using SparQ beads (Qiagen). Final lines of the Canadian Council on Animal Care under protocol number
libraries were quantified using a Quant-iT PicoGreen dsDNA Assay Kit AUP00003572. The development of the preclinical animal model for
(Life Technologies) and Kapa Illumina GA with Revised Primers-SYBR cancer-associated muscle wasting has been described previously23,60.
Fast Universal kit (Kapa Biosystems). The average size fragment was The effects of colon cancer and 5-flurouracil-based chemotherapy
determined using a LabChip GX (PerkinElmer) instrument. were intended to mimic the clinical features of the colorectal cancer
The libraries were normalized and pooled and then denatured in subset of our population, who typically had received systemic therapy
0.05 N NaOH and neutralized using HT1 buffer. The pool was loaded at regimens of this class before surgical resection of oligometastases in
225 pM on an Illumina NovaSeq SP lane using the Xp protocol per the the liver. Tumour size was restricted to 1% of body weight (at the time
manufacturer’s recommendations. Downstream steps in the sequenc- of chemotherapy, or euthanasia in the tumour-bearing animals). Two
ing protocol were the same as those used for RNA-seq, including cycles of chemotherapy reduced tumour volume by 80% (to 0.2% of
base-calling, demultiplexing and generation of fastq reads. body weight); transient anorexia and weight loss occurred at each
cycle, but body weight and food intake were restored within 72 h of each
Analysis of raw sequence files and identification of DE RNAs treatment cycle. The IACUC stipulates use of a daily scoring scheme
Data analyses of raw fastq sequence files were performed using Partek to define animal condition, encompassing body weight, responsive-
Flow software v.10.0.21.0929 unless otherwise specified. The raw fastq ness, respiration, tumour and mobility scores. None of the animals in
files were subjected to Cutadapt for 3′ adapter trimming. The trimmed our study required veterinary appraisal or early euthanasia before the
reads were then aligned to the human genome (reference index hg38) planned end point.
using STAR aligner (v.2.7.3a) and Bowtie (v.2.2.5) for RNA-seq and small Briefly, Ward colorectal carcinomas (0.05 g) were subcutaneously
RNA-seq data, respectively. The generated .bam files were quantified implanted into the flanks of female Fischer 344 rats aged 11–12 weeks.
with respect to the transcriptome using RNAs obtained from different The tumours were subcutaneously introduced to enable assessment
annotation databases: lncRNAs and mRNAs were quantified using of the rate of tumour growth. Tumour growth was followed until the
Ensembl transcripts v.102, miRNAs using miRbase v.22 (ref. 55), sno- tumour weight reached 0.5% of animal body weight, at which time
RNAs using snoDB v.1.2.0 (ref. 56), piRNAs using piRNAdb v.1.8.0 (ref. 57) rats were randomized to be either euthanized immediately or treated
and tRNAs using GtRNAdb58. The features (that is, RNAs) were filtered with two weekly cycles of chemotherapy and then euthanized. Cycles
for ten read counts in 90% of samples following quantification of the of treatment consisted of CPT-11 (50 mg kg−1 body weight, intraperi-
reads. Differential expression analysis of the RNAs referring to all RNA toneal), followed 24 h later by 5-flurouracil (50 mg kg−1 body weight,
intraperitoneal); this treatment is hereafter referred to as FOLFIRI. 3. To ascertain the regulatory effect of miRNAs on lncRNAs and
Healthy animals, tumour-bearing animals and tumour-bearing ani- mRNAs, a regulation similarity score and sensitivity correlation were
mals treated with FOLFIRI (n ≥ 5 per group) were compared. RNA was calculated. The regulation similarity score was used to check the
isolated from gastrocnemius muscle using a MagMax-95 total RNA similarity of expression correlation between lncRNA–miRNA and
isolation kit (Ambion) following the manufacturer’s instructions. mRNA–miRNA pairs. Sensitivity correlation was used to measure
RNA-seq libraries were prepared using a TruSeq Stranded Total RNA whether the correlation between mRNA and lncRNA competing
with Ribo-Zero Human/Mouse/Rat kit according to the manufac turer’s pairs was mediated by miRNA.
instructions. Total RNA (1 µg per sample with a RIN value greater
than 8.0) was used as an input material, depleted of ribosomal RNA The filtering criteria hypergeometric P < 0.01, correlation P < 0.01
(rRNA), and the remaining RNA was purified, fragmented and used and regulation similarity score > 0 (where 0 signifies no interaction)
for cDNA synthesis. The samples were sequenced on an Illumina Next- were applied to define ceRNAs (lncRNA–miRNA–mRNA).
Seq 500 using high-throughput 2 × 150 nt runs (paired-end reads)
with a density of 35 samples per flow cell to generate 10–13 million Network analysis
reads per sample. Sequencing services were provided by PlantBiosis. Network visualization of the lncRNA–miRNA–mRNA triplets as ceRNAs
Base-calling and demultiplexing were performed using 87 Illumina was performed to identify hub lncRNAs for individual male and female
CASAVA1.9 with default settings. Adapter trimming was done using datasets using Cytoscape v.3.9.0 (ref. 66) and RStudio build 748R 4.1.0.
Trim Galore v.0.4.1. Quality control of the sequenced reads was per- Network analysis was performed, and the top hub lncRNAs with the
formed using FastQC v.0.11.4. Trimmed sequences were aligned to the highest node degrees and betweenness centrality were selected as
rat reference genome using TopHat 2.0.10 with Bowtie2. Rat genome hub lncRNAs.
Rnor_6 (Ensembl) was downloaded from the iGENOME website and
served as a rat reference genome. Aligned sequences were saved as Functional annotation and pathway analysis
.sam files; these were then converted to .bam files and used for fur- DE genes were subjected to pathway analysis and functional annotation
ther data processing. Data analysis of .bam files was performed using using IPA67 (QIAGEN, https://digitalinsights.qiagen.com/IPA). P values in
Partek Flow software. mRNAs were annotated using Ensembl Rattus IPA were calculated using right-tailed Fisher’s exact test and indicated
norvegius Rnor_6.0.104. Differential expression analyses were per- the likelihood that the association or overlap between a set of molecules
formed using DESeq2 with a fold-change cutoff of 1.5 and P < 0.05. from the experimental dataset and the associated pathway or process
Pathway analysis data from rodent diaphragm RNA-seq (Neyroud predicted from the IPA knowledge base was due to random chance
et al., GSE271521) was used to compare findings from our human alone. The smaller the P value, the less likely that the association was
male dataset. random. A −log[P] threshold of 1.3 (equivalent to a nominal P value of
0.05) was used to define statistically significant pathways. GSEA68 was
Target prediction of miRNA binding sites in lncRNA and mRNAs performed to infer the biological processes enriched by specific gene
The expression profiles of miRNAs, lncRNAs and mRNAs were gener- sets expressed in the skeletal muscle of patients with cancer. Pathway
ated from rectus abdominis biopsy specimens. In silico target predic- maps were generated using the KEGG database69–71.
tion of miRNA binding sites was performed individually for lncRNAs
(full-length non-coding RNAs) and mRNAs (3′ untranslated regions). Reporting summary
DE miRNAs, mRNAs and lncRNAs within the sex-specific subtypes Further information on research design is available in the Nature Port-
were subjected to in silico target prediction. Target prediction tools folio Reporting Summary linked to this article.
including miRanda61 were used to determine miRNA binding sites in
DE lncRNAs and mRNAs in the datasets. Functionally validated target
Data availability
predictions for mRNAs and lncRNAs were also accessed from pub-
licly available databases including TarBase v.8.0 (ref. 62), lncBase v.3.0 The data generated during this study are available in the Supplementary
(ref. 63) and miRTarBase64, which use different prediction algorithms Information and have been deposited at GEO (https://www.ncbi.nlm.
from expression datasets from tissues and cell lines. To identify skel- nih.gov/geo/), being accessible through GEO series accession codes
etal-muscle-specific genes (mRNAs) as targets, mRNAs from male and GSE254877 (RNA-seq), GSE254878 (small RNA-seq) and GSE292052
female datasets in this study cohort were overlapped with the gene (rat RNA-seq) embedded in GEO super series GSE292053.
targets from the publicly available databases.
51. Narasimhan, A. et al. Small RNAome profiling from human skeletal muscle: novel miRNAs
ceRNA analysis and their targets associated with cancer cachexia. J. Cachexia Sarcopenia Muscle 8,
R package GDCRNA tools was used for ceRNA analysis65. Competing 405–416 (2017).
52. Kays, J. K. et al. Three cachexia phenotypes and the impact of fat-only loss on survival in
lncRNA–mRNA pairs were determined using three criteria as follows. FOLFIRINOX therapy for pancreatic cancer. J. Cachexia Sarcopenia Muscle 9, 673–684
1. Hypergeometric tests were performed to determine whether DE (2018).
lncRNA–mRNA pairs shared a significant number of miRNA binding 53. Kubrak, C. et al. Quantifying the severity of sarcopenia in patients with cancer of the head
and neck. Clin. Nutr. 43, 989–1000 (2024).
sites: 54. Derstine, B. A. et al. Skeletal muscle cutoff values for sarcopenia diagnosis using T10 to L5
measurements in a healthy US population. Sci. Rep. 8, 11369 (2018).
KN −K 55. Kozomara, A., Birgaoanu, M. & Griffiths-Jones, S. miRBase: from microRNA sequences to
m    function. Nucleic Acids Res. 47, D155–D162 (2019).
kn −k
P=1− ∑ 56. Bouchard-Bourelle, P. et al. snoDB: an interactive database of human snoRNA sequences,
N abundance and interactions. Nucleic Acids Res. 48, D220–D225 (2020).
k=0  
n 57. Piuco, R. & Galante, P. A. F. piRNAdb: a piwi-interacting RNA database. Preprint at bioRxiv
https://doi.org/10.1101/2021.09.21.461238 (2021).
58. Chan, P. P. & Lowe, T. M. GtRNAdb 2.0: an expanded database of transfer RNA genes
where m is the number of shared miRNAs between lncRNA– identified in complete and draft genomes. Nucleic Acids Res. 44, D184–D189 (2016).
59. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold change and dispersion
mRNA competing pairs, N is the total number of miRNAs, n is the
for RNA-seq data with DESeq2. Genome Biol 15, 550 (2014).
number of miRNAs targeting the lncRNA and K is the number of 60. Xue, H. et al. Single and combined supplementation of glutamine and n-3 polyunsaturated
miRNAs targeting the mRNA. fatty acids on host tolerance and tumour response to 7-ethyl-10-[4-(1-piperidino)-
1-piperidino]carbonyloxy-camptothecin (CPT-11)/5-fluorouracil chemotherapy in rats
2. For lncRNA–mRNAs to be competing pairs, they must be
bearing Ward colon tumour. Br. J. Nutr. 102, 434–442 (2009).
co-expressed. We determined this using the Pearson correlation test. 61. Enright, A. J. et al. MicroRNA targets in Drosophila. Genome Biol. 5, R1 (2003).
Article
62. Karagkouni, D. et al. DIANA-TarBase v8: a decade-long collection of experimentally Acknowledgements We thank the Canadian Institute of Health Research (CIHR) for providing
supported miRNA-gene interactions. Nucleic Acids Res. 46, D239–D245 (2018). operating research grants.
63. Karagkouni, D. et al. DIANA-LncBase v3: indexing experimentally supported miRNA
targets on non-coding transcripts. Nucleic Acids Res. 48, D101–D110 (2020). Author contributions B.J.B., V.E.B. and S.D. performed conceptualization and overall data
64. Huang, H. Y. et al. miRTarBase 2020: updates to the experimentally validated microRNA– analysis. Next-generation sequencing, molecular and bioinformatical analysis, and unsupervised
target interaction database. Nucleic Acids Res. 48, D148–D154 (2020). clustering techniques and interpretations were performed by B.J.B. and S.D. The collection,
65. Li, R. et al. GDCRNATools: an R/Bioconductor package for integrative analysis of lncRNA, assembly and statistical analysis of clinical, demographic, histological and radiological data
miRNA and mRNA data in GDC. Bioinformatics 34, 2515–2517 (2018). were performed by B.J.B. and V.E.B. The human muscle biopsy histology was carried out by
66. Shannon, P. et al. Cytoscape: a software environment for integrated models of biomolecular A.Q.B. The accrual of human skeletal muscle biopsies was carried out by O.B. The preclinical
interaction networks. Genome Res. 13, 2498–2504 (2003). model was developed by V.M. S.G. provided statistical advice. B.J.B., V.E.B. and S.D. wrote the
67. Kramer, A., Green, J., Pollard, J. Jr & Tugendreich, S. Causal analysis approaches in manuscript. All authors approved the final version.
Ingenuity Pathway Analysis. Bioinformatics 30, 523–530 (2014).
68. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based approach for Competing interests The authors declare no competing interests.
interpreting genome-wide expression profiles. Proc. Natl Acad. Sci. USA 102, 15545–15550
(2005). Additional information
69. Kanehisa, M., Furumichi, M., Sato, Y., Kawashima, M. & Ishiguro-Watanabe, M. KEGG for Supplementary information The online version contains supplementary material available at
taxonomy-based analysis of pathways and genomes. Nucleic Acids Res. 51, D587–D592 https://doi.org/10.1038/s41586-025-09502-0.
(2023). Correspondence and requests for materials should be addressed to Vickie E. Baracos or
70. Kanehisa, M. Toward understanding the origin and evolution of cellular organisms. Sambasivarao Damaraju.
Protein Sci. 28, 1947–1951 (2019). Peer review information Nature thanks Russell Hepple, Serkan Kir and the other, anonymous,
71. Kanehisa, M., Sato, Y., Kawashima, M., Furumichi, M. & Tanabe, M. KEGG as a reference reviewer(s) for their contribution to the peer review of this work.
resource for gene and protein annotation. Nucleic Acids Res. 44, D457–D462 (2016). Reprints and permissions information is available at http://www.nature.com/reprints.
Extended Data Fig. 1 | Correlation between muscle change over time in
lumbar, thoracic and thigh musculature. Total muscle cross-sectional area
was determined in the 3rd lumbar vertebra, at the 4th thoracic vertebra and thigh
11.25 mm below the lesser trochanter of the femur. Muscle change over time is
expressed as % for N = 39 patients. Statistic Pearson r. Inset: cross correlations
between L3, T4 and leg muscle change over time. These regions include different
muscles: abdomen at L3 (rectus abdominis, lateral and oblique abdominis
muscles, quadratus lumborum, psoas, paraspinal (multifidus, erector spinae),
thigh (rectus femoris, sartorius, vastus intermedius, vastus lateralis, adductor,
gracilis, gluteus maximus, biceps femoris and semitendinosus) and chest at the
4th thoracic vertebra (pectoralis, external intercostal, serratus anterior, teres
major, subscapularis, infraspinatus, rhomboid major, erector spinae, trapezius).
The high degree of intercorrelation of muscle change over time these regions
suggests that cancer-associated muscle atrophy is systemic.
