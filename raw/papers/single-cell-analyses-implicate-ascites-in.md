---
source_path: /mnt/c/Users/Administrator/Zotero/storage/J8CMWAE4/s43018-023-00599-8.pdf
ingested: 2026-04-23
sha256: dc0873430f80b5a4
---

nature cancer
Article https://doi.org/10.1038/s43018-023-00599-8
Single-cell analyses implicate ascites in
remodeling the ecosystems of primary and
metastatic tumors in ovarian cancer
Received: 18 March 2022 Xiaocui Zheng1,9, Xinjing Wang1,9, Xi Cheng2,9, Zhaoyuan Liu3, Yujia Yin1,
Xiaoduan Li1, Zhihao Huang4, Ziliang Wang1, Wei Guo3, Florent Ginhoux3,5,6,7,
Accepted: 19 June 2023
Ziyi Li 3 , Zemin Zhang 8 & Xipeng Wang 1
Published online: 24 July 2023
Check for updates Ovarian cancer (OC) is an aggressive gynecological tumor usually diagnosed
with widespread metastases and ascites. Here, we depicted a single-cell
landscape of the OC ecosystem with five tumor-relevant sites, including
omentum metastasis and malignant ascites. Our data reveal the potential
roles of ascites-enriched memory T cells as a pool for tumor-infiltrating
exhausted CD8+ T cells and T helper 1-like cells. Moreover, tumor-enriched
macrophages exhibited a preference for monocyte-derived ontogeny,
whereas macrophages in ascites were more of embryonic origin.
Furthermore, w e characterized MAIT and dendritic cells in malignant
a sci t es, as w ell a s two endothelial subsets in primary tumors as predictive
biomarkers for platinum-based chemotherapy response. Taken together,
our study provides a global view of the female malignant ascites ecosystem
and offers valuable insights for its connection with tumor tissues and
paves the way for potential markers of efficacy evaluation and therapy
resistance in OC.
As a heterogeneous disease, ovarian cancer (OC) is the most lethal circulation6. Although treatments with chemotherapy plus bevaci-
gynecological malignancy, which accounts for 5% of cancer deaths in zumab prolong the 5-year survival, the overall benefits are still limited.
females1. OC is a heterogeneous disease consisting of malignancies Additionally, immunotherapies such as immune-checkpoint inhibitors
with different histological subtypes, molecular biology and microen- only showed an objective response rate of 10% in clinical trials7 and OC
vironment features, which affect its treatment response and clinical subtypes often exhibited diverse responses to immunotherapy owing to
outcomes2. Among all OC types, high-grade serous OC (HGSOC) is the the different proportion and quality of tumor-infiltrating lymphocytes
most common histological subtype accounting for more than 70% of (TILs)8,9. Therefore, it is essential to characterize the tumor microen-
patients with OC3. Once diagnosed, over 75% of patients with HGSOC vironment (TME) of OC, which harbors diverse cellular components
present an advanced disease with widespread metastasis and ascites4,5. playing important roles in disease progression and therapy response.
As reported, a predilection of metastasis to omentum in OC is consist- Single-cell mRNA sequencing (scRNA-seq) is a powerful tool
ently identified owing to the fatty structure of omentum and peritoneal to characterize the cellular features and dynamic relationships of
1Department of Obstetrics and Gynecology, Xinhua Hospital, Shanghai Jiaotong University School of Medicine, Shanghai, China. 2Department of
Gynecological Oncology, Fudan University Shanghai Cancer Center, Shanghai, China. 3Department of Immunology and Microbiology, Shanghai
Institute of Immunology, Shanghai Jiao Tong University School of Medicine, Shanghai, China. 4Analytical Biosciences Limited, Beijing, China.
5Singapore Immunology Network (SIgN), Agency for Science, Technology and Research (A∗STAR), Singapore, Singapore. 6Translational Immunology
Institute, SingHealth Duke-NUS Academic Medical Centre, Singapore, Singapore. 7Gustave Roussy Cancer Campus, Villejuif, France. 8BIOPIC,
and School of Life Sciences, Peking University, Beijing, China. 9These authors contributed equally: Xiaocui Zheng, Xinjing Wang, Xi Cheng.
e-mail: liziyie@shsmu.edu.cn; zemin@pku.edu.cn; wangxipeng@xinhuamed.com.cn
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1138
Article https://doi.org/10.1038/s43018-023-00599-8
different cell populations in multiple malignancies10–12. For instance, Unlike nonmalignant cells, tumor cells as defined by inferred
a previous single-cell atlas of primary ovarian tumor has revealed a copy number variations (inferCNV), exhibited a strong interpatient
GZMK+ CD8+ effector memory (T ) T cell subset as pre-dysfunctional heterogeneity (Extended Data Fig. 2a–c). Notably, tumor cells were
EM
effector memory cells13. Moreover, another OC study defined a popu- identified in all ascites samples, with an averaged proportion of 2.7%
lation of stem cell-like tissue-resident memory T cells with a maxi- (1,444 of 53,499) (Extended Data Fig. 2d). Our observation was consist-
mal expression level of GZMK, which would develop into exhausted ent with the notion that OC tumor cells prefer to ‘seed’ to the peritoneal
T (T ) cells14; however, where these memory T cells originate from is cavity rather than spreading via vasculature, which highlights the
EX
still unknown due to the limited sampling tissues in previous studies. tight association between ascites and intraperitoneal spread of OC17.
Besides primary tumors, omentum metastases and malignant ascites Further, inferCNV analyses showed that the subclones of tumor cells
are equally important in OC studies. For example, interleukin (IL)-6 found within Met.Ome were also detectable in that of Pri.OT (Extended
secreted from cancer-associated fibroblasts in the ascites ecosystem Data Fig. 2e), indicating these subclones as tumorigenic populations
could stimulate JAK–STAT signaling in malignant cells, leading to a poor of peritoneal metastasis.
prognosis and resistance to chemotherapies15. But previous single-cell
analysis of OC ascites focused largely on malignant cells and other Dynamic relationships of T cells in OC
CD45− cells15 and little is known about the immune milieu in the OC Given that HGSOC is the most common OC subtype, we focused on
ascites and how malignant ascites influence the immune status of OC. HGSOC in the subsequent analyses of specific cellular compartments
Thus, a high-resolution cellular landscape involving multiple-site tis- in the TME. We first focused on the intrinsic properties and potential
sues is needed to characterize the comprehensive TME of different OC functions of T cell populations in OC. By unsupervised clustering, we
sites, especially omentum metastasis and ascites. identified five CD4+ clusters, five CD8+ clusters and two unconventional
Here, we delineated a comprehensive landscape of OC TME via clusters (Fig. 2a, Extended Data Fig. 3a,b and Supplementary Table 4).
scRNA-seq by comparing the unique cellular compositions of five The conventional T cell clusters were further split into naive (T ), central
N
tumor-related sites, including primary ovarian tumor (Pri.OT), omen- memory (T ), effector memory (T ), effector (T ), regulatory (T ), T
CM EM eff reg
tum metastasis (Met.Ome), ascites, pelvic lymph node (PLN) and helper 1 (T 1)-like18 and exhausted19 (T ) T cell clusters, which showed
H EX
peripheral blood (PB). Through T cell receptor (TCR)-based lineage different tissue preference patterns (Fig. 2a,b, Extended Data Fig. 3c
tracing and trajectory inference, we unveiled potential dynamic char- and Supplementary Table 5). T cells (T01 and T06) were enriched in PB
N
acteristics of T cells from ascites to tumor tissues. We characterized and PLN, maintaining a quiescent state. Consistent with previous stud-
the functional states and ontogeny of macrophages in ascites and ies20, the majority of immunosuppressive FOXP3+ T (T03) cells and the
reg
tumor tissues and also highlighted DES+ mesothelial cells as impor- HAVCR2+ exhausted CD8+ cells (T10), were predominantly enriched in
tant immunoregulators reprogramming OC ascites. Additionally, both two tumor sites. The analyses by flow cytometry also suggested a
we revealed the associations between distinct cellular compositions higher proportion of T and PD-1+ T cells in tumor sites than in ascites
reg
and the clinical responses to platinum-based chemotherapy, which (Extended Data Fig. 3d), further proving a more immunosuppressive
might serve as indicators of treatment effectiveness. Taken together, status in tumor tissues compared to malignant ascites. Additionally,
our findings provide insights into the functions of malignant ascites CXCL13+ T 1-like cells (T05) were also enriched in tumor sites, whereas
H
and would provide an important resource to guide the development CD4+ANXA1+ T (T02) and CX3CR1+ T cells (T04 and T09) were mainly
CM eff
of additional therapeutic strategies. detected in blood and ascites. Specifically, we identified two CD8+ T
EM
clusters occupying a large proportion of CD8+ T cells, with T07 ANXA2+
Results T enriched in tumor sites and T08 GZMK+ T enriched in ascites
EM EM
High-resolution landscape of OC by multisite scRNA-seq (Fig. 2b). Based on limited differential expressed genes, we observed
To elucidate the complexity of cellular compositions in ovarian can- that tumor-enriched ANXA2+ T cells expressed increased levels of
EM
cer, we utilized scRNA-seq to analyze unsorted cells from PB, PLN, genes encoding effector molecules (such as GNLY, GZMB and TNFSF10)12
Pri.OT, matched Met.Ome and malignant ascites of 14 patients with (Extended Data Fig. 3e), indicating the intrinsic antitumor effector
advanced OC (Fig. 1a and Supplementary Table 1). These patients potential of T cells inside tumors. By contrast, ascites-enriched
EM
exhibited five distinct histological subtypes and varying responses GZMK+ T cells exhibited higher expressions of EOMES and TCF7
EM
to platinum-based chemotherapy. In total, we cataloged 223,363 (ref. 21) (Extended Data Fig. 3e), which are the key transcription factor
high-quality single cells into five major cell lineages annotated by genes in progenitor T cells, suggesting that GZMK+ T cells were more
EX EM
canonical marker expression (Fig. 1b,c, Extended Data Fig. 1a–c and likely to transit into T cells.
EX
Supplementary Table 2). Combined with TCR-seq and single-cell transcriptomics, we cap-
We first quantified relative tissue enrichment of major cell clus- tured at least one pair of full-length productive α- and β-chains in
ters by calculating the ratio of observed to expected cell numbers 54,061 T cells, of which 21.12% (11,415 cells) harbored repeated TCRs
(R ) using data of patients with HGSOC (Fig. 1d,e, Extended Data of 2,386 clonotypes (Fig. 2a and Extended Data Fig. 3f,g). We then
o/e
Fig. 1d and Supplementary Table 3). As expected, B cells and CD4+ T cells quantitatively evaluated the T cell dynamics using the previously
dominated the PLNs, whereas lymphocytes and monocytes constituted developed STARTRAC indices upon TCR tracking18 (Methods). T cells
the main cellular components of PB samples. Of note, we identified carrying repetitive TCRs are defined as clonal cells. The presence of
all five major cell lineages in both Pri.OT and Met.Ome and the enrich- clonal cells across several different tissue sites within the same clus-
ment pattern of most cell types showed no significant differences ter implies the tissue migration (STARTRAC-migr) of indicated T cell
between these two sites, suggesting a similar complex TME necessary subtypes. And clonal cells found within a T cell cluster were quantified
to the development of both primary and metastatic tumor cells (Fig. 1e with STARTRAC-expa index, whereas clonal cells between two differ-
and Extended Data Fig. 1e). Ascites, frequently found in patients with ent T cell subtypes referred to cell state transition (STARTRAC-tran).
advanced OC and associated with chemotherapy response5, harbored Among all CD8+ T cells, T cells showed the highest clonal expansion,
eff
a large number of immune cells and stromal cells. Among them, CD8+ migration and transition index (Fig. 2c), as expected. Additionally, expa
T cells, macrophages and dendritic cells (DCs) were major constitu- index pointed out that clonal expansion might be a possible explana-
ents of ascites with high cell proportions, indicating an inflammatory tion for the T enrichment in tumor sites (Fig. 2c), consistent with
EX
microenvironment. Mesothelial cells, recently reported to be tightly previous findings22. Notably, we observed strong TCR sharing of T
EX
associated with metastasis of OC16, were also preferentially found in cells among two tumor sites and ascites (Met.Ome-AS, Pri.OT-AS and
malignant ascites (Fig. 1d,e). Pri.OT-Met.Ome) (Extended Data Fig. 4a). Considering that exhausted
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1139
Article https://doi.org/10.1038/s43018-023-00599-8
b c d
+++ ++ + +/– + B cells R o/e
++ ++ + +/– + CD4+ T Max + + ++ + ++ CD8+ T + ++ ++ + + NK 0 +/– ++++/– +/– +/– Monocyte ++ + ++ Macrophage + + ++ + + DC ++ ++ Fibroblast — — ++ ++ ++ Mesothelial cells + — — ++ ++ Other stromal cells ++ — — ++ ++ Endothelial cells ++ ++ Cancer cells ++ ++ ++ HSC + + + ++ ++ Proliferative cells
e
Monocyte Monocyte Monocyte
Endothelial cells Endothelial cells
T cells had poor migration capability18, this was seemingly logical as exhibited a high ability of transition to T , ANXA2+ T and T cells
eff EM EX
these T cells would recognize the same tumor-derived neoantigens (Fig. 2e and Extended Data Fig. 4c), further supporting our inferred
EX
in different tissues. trajectory analyses. As reported, CD8+ GZMK+ T cells were defined as
To decipher the potential developmental trajectories of T cells, ‘pre-exhausted’ cells within tumors, which were accumulated by local
we performed PAGA23 and Palantir24 analysis, excluding two uncon- expansion and replenishment and could further transit to terminal
ventional clusters due to their distinct TCR characteristics. We noticed exhausted T cells11,25. Likewise, compared to other T cells, T08 GZMK+
that ascites-enriched GZMK+ T (T08) was located centrally bridging T T in our study also harbored a higher ability to transit into T cells
EM N EM EX
(T06), T (T09) and T (T10) cells (Fig. 2d and Extended Data Fig. 4b), (Fig. 2e and Extended Data Fig. 4c), suggesting transition from GZMK+
EX eff
indicating their intermediate states. In addition, STARTRAC pairwise T as an important source of T cells. Given that GZMK+ T cells were
EM EX EM
transition analysis based on TCR sharing also showed that GZMK+ T mostly enriched in ascites, their transitions to tumor-enriched clusters
EM
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1140
NLP BP seticsA TO.irP emO.teM
a
PLN PB Ascites Pri.OT Met.Ome
Monocyte Monocyte
10 Macrophage Macrophage Macrophage Macrophage Macrophage
NK Fibroblast Fibroblast NK Fibroblast NK Fibroblast NK Fibroblast
0 B cel H ls S C C D8 Pr + o T life D r C ative c M e e ll s s othelial cells H N SC K C P D ro 8 l + i f T e D r C ative c M e O e ll s t s h o e th r e s l t i r a o l m ce a l l l s cells B cel H ls S C C D8 P c + e r o l T l l s ife D r C ative O M t e h s e o r t s h t e ro lia m l a c l e c ll e s lls HS C C D8 P + r o T lif D er C ative O M c t e h e l e s ls o r t s h tr e o li m al a c l e c l e ls lls HS C C D8 P + r o T lif D er C ative M c O e e t l s l h s o e t r h s e t l r ia o l m c a e l l l c s ells
CD4+ T B cells CD4+ T CD4+ T B cells CD4+ T B cells CD4+ T
Epithelial cells Epithelial cells
−10 Epithelial cells Epithelial cells Epithelial cells
Endothelial cells Endothelial cells Endothelial cells
−10 0 10 −10 0 10 −10 0 10 −10 0 10 −10 0 10
UMAP_1
2_PAMU
B cells CD4+ T CD8+ T NK Monocyte Macrophage DC Fibroblast Mesothelial cells Other stromal cells Endothelial cells Epithelial cells HSC Proliferative cells
UMAP_1
2_PAMU
Ascites
PB
4 platinum-resistant patients unknown Met.Ome Lymphoid cells
Pri.OT 10x barcoded 22 c 5 e , l 3 ls 73 Cancer cells
beads 5 cellular
PLN C re e a ll g s e a n n t d s Oil lineages Stromal cells Endothelial cells
9 platinum-sensitive patients Single cell
Patients with OC Sample collection isolation 10x Genomics sequencing Data analysis
Monocyte 10 Macrophage NK DC Fibroblast Mesothelial cells CD8+ T Proliferative cells 0 Other stromal cells B cellsHSC CD4+ T Scaled Epithelial cells expression −10 >4 2 Endothelial cells 0 <−2
−10 0 10 sllec
B
T
+4DC
T
+8DC
KN etyconoM egahporcaM CD tsalborbiF sllec
lailehtoseM
sllec
lamorts
rehtO
sllec
lailehtodnE
sllec
recnaC
CSH sllec
evitarefilorP
Myeloid cells
CMC D DS7 149 9AA1
CD4 HH H A P P P C M F E P M T M U DT K M M M C M C C C N C C C A C C C M D S W D F K A S KK L L C P R D H E D O N Y Y L P I N RR O P LL L P U C O C E KDD D D D D 1 S D D A U M K M M S Y T T C Q C R P Z 6 AA A P G G E O KS B TT 1 G T G S S K 38 3 8 3 1 1 K N C I L X1 R L C P P P 6 C C E 1 RC 4 81 A A 3 −− − S 3 A T P N F F D 4 4 A 6 R 1 1 E 7 C P 4 8 1 1 2 7 7 DD D 1A B 6 1 M 1 M R R N 1 1 6 1 T A O QR P 2 A B 2 1 B BB 1 11 + + + / / / – – – + + — / / – – + + / / – – +/– +/–
Other stromal cells
Fig. 1 | Landscape of advanced ovarian cancer via scRNA-seq of five sites. showing 14 clusters of n = 10 patients with HGSOC identified by integrated
a, Overall study design with flowchart of sample collection and single-cell analysis. Each dot corresponds to a single cell, colored by clusters. NK, natural
analysis of OC by 10x Genomics sequencing. n = 14 patients with OC who killer; HSC, hematopoietic stem cell. c, Heat map depicting expression levels of
were responsive or nonresponsive to platinum-based chemotherapy were selected highly expressed genes (including marker genes) across major clusters
recruited to our study. In total, n = 39 samples, including n = 6 PB, n = 5 PLN, of HGSOC. Rows represent genes and columns represent clusters. d, Tissue
n = 13 Pri.OT, n = 5 matched Met.Ome and n = 10 ascites samples were analyzed. preference of each major cluster in HGSOC estimated by R . e, UMAP plots
o/e
Each dot corresponds to one sample, colored by sample types. Red triangle, showing the distinct cell composition of five different sample sites in patients
orange triangle, dark red circle, dark red triangle, green triangle represent with HGSOC. For b–e, a total of n = 31 HGSOC samples, including n = 5 PB, n = 4
blood, ascites, primary tumor, omentum metastases and pelvic lymph node, PLN, n = 10 Pri.OT, n = 4 Met.Ome and n = 8 ascites samples were analyzed.
respectively. b, Uniform Manifold Approximation and Projection (UMAP) plot
Article https://doi.org/10.1038/s43018-023-00599-8
a Clonal T cell b
c
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1141
xedni-CARTRATS
apxE
rgiM
narT
++ ++ + T01 (T N ) R o/e
++ + ++ T02 (T ) Max
CM + + + +++ ++ T03 (T ) reg
+/– ++ ++ T04 (T eff ) 0 + – ++ +++ T05 (T 1-like) H ++ ++ + T06 (T ) N +++ +++ T07 (T -ANXA2)
EM + + ++ ++ + T08 (T -GZMK) EM
++ ++ + T09 (T ) eff – + ++ +++ T10 (T ) EX ++ ++ – T11 (MAIT)
++ ++ + + T12 (γδT)
e
0.4
0.3
0.2
0.1
0
1.5
1.0
0.5
0
1.0
0.5
0
h
NLP BP seticsA TO.irP emO.teM
5.0 T03
T05 2.5 T10 T07 T01 T02 0
T08 T09
−2.5 T11 T04 T06 T12 −5.0
−5 0 5 −5 0 5
UMAP_1
2_PAMU
T-cell clusters T01_CD4−CCR7
T02_CD4−ANXA1
T03_CD4−FOXP3 T04_CD4−CX3CR1
T05_CD4−CXCL13 T06_CD8−CCR7 T07_CD8−ANXA2 T08_CD8−GZMK T09_CD8−CX3CR1
T10_CD8−HAVCR2 T11_CD8−SLC4A10
T12_CD8−TRDV2 Single TCR or not detected
d
Shared TCR
T06 (T )
N 0 0.1 0.2 0.3
PIndex.tran
T07 (T -ANXA2)
EM
T08 (T -GZMK)
EM
T10 (T EX ) T09 (T eff )
f
)
T(
60T
N )2AXNA-
T(
70T
ME
)KMZG-
T(
80T
ME
)
T(
90T
ffe )
T(
01T
XE
g T08 in ascites-T07
0.06
0.04
0.02
T08–T07 T08–T10
0.4 T07-MT 0
T07-PT MT PT
0.3
T08 in ascites-T10
0.15 0.2 0.10
0.1
0.05
0 0
ASMTPT ASMTPT
sRCT
derahs
fo snoitroporP
rebmun
llec
)01T
ro( 70T
yb
detcerroc
T10-MT
T10-PT
T07 (T -ANXA2) CM
MT PT
T08 (T -GZMK) T08 (T -GZMK) T10 (T )
EM EM EX
80T_SA 70T_TM 80T_TM 01T_TM T
+8DC_BP
T
+8DC_NL
Cells >8 8 7
6 5
4 3
2
1
0
80T_SA 70T_TP 80T_TP 01T_TP T
+8DC_BP
T
+8DC_NL
***
***
***
Cells >8 8 7
6 5
4 3
2
1
0
yb
detcerroc
sRCT
derahs
fo snoitroporP
rebmun
llec
80T
+/– +/–
+/– +/–
+/– +/– +/– +/– +/– +/– +/– +/–
+/– +/– +/– +/– +/–
+/–
T08 (T -GZMK)
EM
T09 (T )
eff
T07 (T -ANXA2) EM
T10 (T )
EX
T06 (T )
ns N
Ascites—metastatic tumor Ascites—primary tumor
0.4
0.3
0.2
0.1
0
ASMTPT ASMTPT
)KMZG-
T(
80T
ME
)
T( 90T
ffe )2AXNA-
T(
70T
ME
)
T( 01T
XE ) T(
60T
N
Fig. 2 | Characterization of T cell clusters and dynamics of CD8+ T cells in between GZMK+ T and other CD8+ T cells and the vertical red box refers to
EM
HGSOC. a, UMAP plots showing 12 clusters of T cells and clonal T cells within each the transition between other CD8+ T cells and T cells. f, Bar plots showing
EX
cluster, colored by clusters. b, Tissue preference of each T cell cluster estimated proportions of shared TCRs between GZMK+ T (T08) and ANXA2+ T (T07)
EM EM
by R . c, Clonal expansion, migration and transition potential of CD8+ T cells (left) or T (T10) (right) corrected by cell numbers of ANXA2+ T (T07) or T
o/e EX EM EX
quantified by STARTRAC indices. Indices were quantified for n = 9 patients (T10) in sampled tissues, respectively. g, Bar plots showing proportions of shared
with more than two matched samples. Center line indicates the median value, TCRs between GZMK+ T (T08) and ANXA2+ T (T07) (top) or T (T10) (bottom)
EM EM EX
lower and upper hinges represent the 25th and 75th percentiles, respectively corrected by cell numbers of GZMK+ T (T08) in ascites. h, The distribution of
EM
and whiskers denote 1.5 × interquartile range. *P < 0.05, **P < 0.01, ***P < 0.001; clonal clonotypes in indicated CD8+ subsets derived from ascites and two
permutation test (exact P values are provided in source data). d, PAGA analysis tumor sites. For a,b,d, data were summarized from all n = 31 HGSOC samples.
of CD8+ T cells. Each dot represents a T cell cluster. e, Heat map showing the For c,e–h, all n = 30 HGSOC samples except for the primary tumor sample of
developmental transition potential between CD8+ T cells quantified by pairwise HGSOC7 were analyzed. AS, ascites; PT, primary ovarian tumor; MT, omentum
STARTRAC-tran indices. The horizontal red box represents the transition metastatic tumor.
Article https://doi.org/10.1038/s43018-023-00599-8
a
(T and ANXA2+ T ) might happen together with cross-tissue migra- GZMK+ T cells than tumor-derived GZMK+ T cells (Fig. 2f). The results
EX EM EM EM
tion. Thus, we further checked TCR sharing between GZMK+ T and indicated that ascites-derived GZMK+ T cells might serve as an impor-
EM EM
T /ANXA2+ T across different tissues and found that T and ANXA2+ tant source of T cells infiltrating into tumor sites and further transit into
EX EM EX
T cells in tumor sites shared more TCR clones with ascites-derived T or ANXA2+ T . Furthermore, GZMK+ T in ascites shared more TCR
EM EX EM EM
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1142
xedni-CARTRATS
b 0.3
0.2
0.1
0
0.8
0.6
0.4
0.2
0
0.4
0.2
0
)
T ( 10 T
N )
T ( 2 0 T
M
C
)
T ( 3 0 T
ger )
T ( 4 0 T
ffe )e
k il-1 T (
5
H
0
T
d
0.4
0.2
0
Met.Ome Pri.OT
sllec
T +4DC
ni
oitar
)ekil-1
T(
50T
H
c Shared TCR
0 0.005 0.010 0.015
T01 (T ) PIndex.tran
N
T02 (T ) CM
T04 (T ) eff
T02 (T ) CM
T05 (T 1-like) H
T03 (T )
T04 (T ) reg eff
T01 (T )
N
T03 (T reg ) T05 (T H 1-like)
g
e f
*P = 0.037
)
T(
20T
MC )
T(
40T
ffe )ekil-1
T(
50T
H
)
T(
30T
ger )
T(
10T
N
CD8+ T cells
Other CD8+ T
Expansion
Teff GZMK+ TEM TEX
Other CD8+ T
TEX
TEX Expansion
Expansion ANXA+ TEM
GZMK+ TEM ANXA+ TEM GZMK+ TEM
Pri.OT Met.Ome
CD4+ T cells
Ascites
Other CD4+ T Other CD4+ T
Expansion
0.010
0.008
T
T
0
0
5
5
-
-
M
PT
T
Migration
TCM
Teff
Migration
0.006
TH1-like
0.004 TH1-like
0.002 TCM
Treg TCM Treg
0 Pri.OT Met.Ome
yb
xedni
gnirahs
RCT
detsujdA
seticsa
ni 20T
T02 in ascites-T05
MT PT
T05 (T 1-like)
H
20T_SA 20T_TM 30T_TM 50T_TM T
+4DC_BP
T
+4DC_NL
20T_SA 20T_TP 30T_TP 50T_TP T
+4DC_BP
T
+4DC_NL
***
***
***
***
**
ns
Ascites—metastatic tumor Ascites—primary tumor
Cells Cells
3 3
2 2
1 1
0 0
apxE
rgiM
narT
Ascites
Migration
Fig. 3 | Characterization and dynamics of CD4+ T cells in HGSOC. a, Clonal clonotypes in indicated CD4+ subsets derived from ascites and two tumor sites.
expansion, migration and transition potential of CD4+ T cells quantified by e, Bar plots showing proportions of shared TCRs between T (T02) and T 1-like
CM H
STARTRAC indices. Indices were quantified for each n = 9 patient with more than cells (T05) corrected by cell numbers of T (T02) in ascites, related to Extended
CM
two matched samples. Center line indicates the median value, lower and upper Data Fig. 5e. f, Frequency of T 1-like cells as a proportion of all CD4+ T cells in n = 4
H
hinges represent the 25th and 75th percentiles, respectively and whiskers denote Met.Ome and n = 10 Pri.OT samples from ten patients with HGSOC. Center line
1.5 × interquartile range. *P < 0.05, **P < 0.01, ***P < 0.001; permutation test (exact indicates the median value, lower and upper hinges represent the 25th and 75th
P values are provided in source data). b, PAGA analysis of CD4+ T cells. Each dot percentiles, respectively and whiskers indicates min to max. *P < 0.05, **P < 0.01,
represents a T cell cluster. In total n = 31 HGSOC samples were used for analysis. ***P < 0.001; unpaired two-sided t-test. g, Sketch map showing the dynamics of
c, Heat map showing the developmental transition potential between CD4+ T CD8+ T cells (top) and CD4+ T cells (bottom) between ascites and two tumor sites.
cells quantified by pairwise STARTRAC-tran indices. The red box represents For a,c–e, data were summarized from all n = 30 HGSOC samples except for the
the transition between T and other CD4+ T cells. d, The distribution of clonal primary tumor sample of HGSOC7.
CM
Article https://doi.org/10.1038/s43018-023-00599-8
clones with T or ANXA2+ T cells in Met.Ome than in Pri.OT (Fig. 2g), a potential explanation for the relative enrichment of T 1-like cells in
EX EM H
reflecting a preference of ascites-derived GZMK+ T infiltrating into Met.Ome than Pri.OT (Fig. 3f).
EM
Met.Ome. Then, we checked the TCRs shared among ascites-derived Collectively, through integrated analysis of single-cell transcrip-
T (T08) and tumor-derived T07, T08 and T (T10) to confirm the tome and TCR data, we identified multiple T cell populations with dis-
EM EX
connections between ascites T and tumor T cells. Of note, tumor tinct distribution patterns and revealed unique dynamics of T cells from
EM EX
T (T10) clones linked to ascites-derived GZMK+ T showed mutu- ascites to tumor sites in OC. We found that ascites-enriched memory
EX EM
ally exclusive patterns with tumor T10 clones linked to T07 and T08 T cells (CD8+ GZMK+ T and CD4+ T ) could be a potential important
EM CM
clusters in tumors (Fig. 2h). Considering the hard-to-reverse nature pool for TILs, including CD8+ T and CD4+ T 1-like cells, especially for
EX H
of exhaustion and the lack of mobility of T cells, these results further Met.Ome (Fig. 3g). These results implicate a potential role of ascites in
EX
support the notion that T cells in tumor may be derived from GZMK+ shaping the TME of OC during T cell infiltration.
EX
T in ascites, in a process including cross-tissue migration and state
EM
transition. Moreover, we checked whether the TCR clones shared by DC subsets show tissue-specific patterns
ascites T (T08) and tumor T (T10) also existed in blood or lymph For myeloid cells, unsupervised clustering gave rise to 15 clusters with
EM EX
nodes. We found that the majority of TCR clones shared by ascites T distinct gene signatures (Fig. 4a). HLAhiCD14− DC subsets (M01–M04)
EM
(T08) and T cells (T10) from primary tumor (61.73%) or metastatic were further distinguished as CD1C+ DCs (cDC2), CLEC9A+ DCs (cDC1),
EX
tumor (77.8%) could not be detected in blood or lymph node-derived LAMP3+ DCs and LGALS2+ DCs. Notably, the LAMP3+ DC cluster was
T cells (Fig. 2h and Extended Data Fig. 4d), further supporting the idea also annotated as ‘mregDC’ for its high expression of maturation
that ascites T cells could be an important direct source for TILs. To and immunoregulatory marker genes (such as CCR7, IL12B, CD274,
EM
find the clues about where these TCR clones that are undetected in PDCD1LG2 and LAMP3), a cellular state induced upon uptake of tumor
blood/lymph nodes might come from, we examined the origins of antigens26 (Extended Data Fig. 6a). In line with the tissue distribu-
all ascites-enriched T cells (T08). We found that the TCRs in 15.36% tion patterns reported in other cancer types27, LAMP3+ DCs showed
EM
ascites T (T08) cells could be detected in both blood and lymph relatively comparable enrichment in tumor and lymph nodes.
EM
nodes, whereas 9.57% and 3.34% ascites clonal T shared TCRs only As LAMP3+ DCs exhibited increased expression of genes encoding a
EM
with blood T cells or lymph node T cells, respectively (Extended Data co-stimulatory molecule such as CD40, which is associated with inter-
Fig. 4e). Taken together, these findings provide insights into the cycle action between myeloid cells and T cells28, and IL12B, which promotes
of CD8+ T cells in OC and suggest that ascites-derived GZMK+ T cells T 1 development29(Extended Data Fig. 6a), we speculate that LAMP3+
EM H
might serve as a direct source of tumor-infiltrating T cells. DCs might also help potentiate the infiltration and differentiation of
EX
Similar analyses were also performed on CD4+ T cells to quantify T 1-like cells in ovarian tumors. This could explain the higher enrich-
H
their tissue distributions and TCR sharing. In contrast to CD8+ T cells, ment indexes of both LAMP3+ DCs and T 1-like T cells in Met.Ome than
H
CD4+ T cells showed an overall lower clonal expansion. Among these in Pri.OT (Fig. 4b). Notably, we did not detect many conventional DCs
clusters, CD4+ T cells exhibited the highest clonal expansion, migra- (cDCs) in tumor tissues as reported in recent studies27, but instead
eff
tion and transition indexes (Fig. 3a), similar to the observations in observed their specific relative enrichment in malignant ascites
CD8+ T cells. The inferred developmental trajectories also exhibited (Fig. 4b and Extended Data Fig. 6b,c). To further elucidate the func-
a similar branched structure. T (T01), T 1-like (T05) and T (T03) tions and relationships between different myeloid clusters, we per-
N H reg
cells were positioned at three different branches whereas T (T02) formed similarity analysis of myeloid cells in our dataset with those
CM
cells were located in the middle (Fig. 3b and Extended Data Fig. 5a). In reported in colorectal cancer (CRC)28 and hepatocellular carcinoma
addition, pairwise transition analysis based on TCR sharing (Fig. 3c and (HCC)27 (Fig. 4c). As expected, both cDC1 and cDC2 from different can-
Extended Data Fig. 5b) and the shared TCR pattern among T02, T03 and cer types or tissue sources were clustered together, indicating their
T05 (Extended Data Fig. 5c,d) also revealed that T cells were associ- conserved phenotypes (Fig. 4c and Extended Data Fig. 6d). We also
CM
ated with T and T 1-like cells, suggesting T as potential precursors checked the potential origins of LAMP3+ DC in tumor and observed
eff H CM
of CXCL13+ T 1-like cells. Given that T cells were enriched in ascites, more cDC2-derived LAMP3+ DC (Extended Data Fig. 6e), which could
H CM
whereas T 1-like cells were enriched in tumors (Fig. 2b), their transi- be associated with higher proportions of cDC2 in ascites.
H
tion was accompanied by the ascites to tumors cross-tissue migration In addition, we noticed that the distribution of DC clusters was
of CD4+ memory T cells. Then, we noticed that the TCR clones shared correlated with chemotherapy responses. Notably, among all DCs, the
by tumor T 1-like cells and T in ascites were almost undetected in proportion of M01_DC-CD1C (cDC2) significantly increased in ascites of
H CM
any other T cells from tumor, blood and lymph nodes (Fig. 3d and nonresponsive patients, whereas the M02_DC-CLEC9A (cDC1) propor-
Extended Data Fig. 5e), implying that ascites-derived T cells might tion decreased (Fig. 4d). Although the previous studies reported that
CM
be a direct source of T 1-like cells in tumors. Additionally, we observed the protumor or antitumor responses of cDCs are uncertain among
H
more shared TCR clones between T in ascites and T 1-like cells in Met. various types of tumors30, our observations indicated that cDC1 and
CM H
Ome compared to that in Pri.OT (Fig. 3e and Extended Data Fig. 5e), cDC2 cells in the OC ascites might function in an opposite fashion in
suggesting that ascites-derived T cells were more likely to infiltrate responses to platinum-based chemotherapy, which remains to be
CM
into Met.Ome. Such a tissue preference of T cell infiltration could be confirmed by further studies.
CM
Fig. 4 | Two distinct functional states of tumor-enriched and ascites-enriched between TeMs (M07, M10 and M12) and AeMs (M08, M09, M11 and M14) (left).
macrophages in HGSOC. a, UMAP projection of 15 myeloid clusters colored by P value < 0.05; two-sided Wilcoxon test adjusted by the Benjamini–Hochberg
clusters (left) and heat map showing expression patterns of selected genes (BH) procedure; log(FC) > 0.5. n = 10 primary tumor, n = 4 matched omentum
2
across indicated clusters (right). b, Tissue preference of each myeloid cluster metastatic tumor and n = 8 ascites samples from ten patients with HGSOC were
estimated by the R . c, Hierarchical clustering comparing the similarity of used for analysis. IFN, interferon; FDR, false discovery rate; FC, fold change. f, Dot
o/e
myeloid cell clusters in our dataset (OC) with those reported in CRC and HCC. plot showing the mean interaction strength for selected ligand–receptor pairs
Clusters were colored by dataset. n = 3 tumor types were used for analysis. among macrophages and T cell clusters in tumors. Dot size indicates percentage
d, Frequency of DC subclusters as a proportion of all DCs in ascites from n = 6 of ligand–receptor expression in cells of one cluster, colored by average ligand–
platinum-sensitive patients and n = 2 platinum-resistant patients. Center line receptor expression level. n = 10 primary tumor and n = 4 matched omentum
indicates the median value, bottom and top hinges represent the 25th and 75th metastatic tumor from ten patients with HGSOC were used for analysis. For a,b,
percentiles, respectively and whiskers denote 1.5 × interquartile range. *P < 0.05, data were summarized from all n = 31 HGSOC samples.
**P < 0.01, ***P < 0.001; two-sided t-test. e, Differentially expressed genes
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1143
Article https://doi.org/10.1038/s43018-023-00599-8
Tumor-enriched and ascites-enriched macrophages FCGR3A+ nonclassical monocytes, respectively. The remaining clus-
As for the monocyte/macrophage compartment, two blood-enriched ters were all identified as macrophages (M07–M15) based on the high
clusters (M05 and M06) were characterized as CD14+ monocyte and expression of CD68 (Fig. 4a). Notably, macrophages detected in tumor
a
10
M14
M09
5
M08
M11
M15
0 M06 M01 M10 M13
M05
M04 M03 M12
−5 M07
M02
−10 −5 0 5 10
UMAP_1
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1144
2_PAMU
b
R o/e
Max
0
NLP BP seticsA TO.irP emO.teM
M01_DC−CD1C
M02_DC−CLEC9A
M03_DC−LAMP3
M04_DC−LGALS2
M05_Mono−CD14
M06_Mono−FCGR3A
M07_Macro−EREG
M08_Macro−FN1 M09_Macro−FABP5
M10_Macro−C1QA
M11_Macro−VCAN
M12_Macro−C3
M13_Prolif−Macro−C3
M14_Macro−FOLR2
M15_Prolif−Macro
−FOLR2
c
+ ++ +/– +/– M01
++ ++ +/– +/– M02
+++ + M03
+ +/– M04
+/– +/– +/– +/– M05
+/– +/– +/– M06
++ – M07(TeM)
+/– ++ +/– +/– M08(AeM)
+/– ++ +/– +/– M09(AeM)
+ +/– M10(TeM)
+/– ++ +/– +/– M11(AeM)
+/– +/– M12(TeM)
+/– +/– M13
– ++ +/– M14(AeM)
++ ++ M15
e d
4
2
0
0 2 4
Mean expression of M08−M09−M11−M14
21M−01M−70M
fo noisserpxe
naeM
M07−M10−M12 M08−M09−M11−M14
Neutrophil chemotaxis
Cell chemotaxis MHC class II protein complex
Cellular response to tumor necrosis factor Cellular response to IFN-γ
Positive regulation of cytokine production
Response to IFN-γ
Cellular response to IL-1 IFN-γ-mediated signaling pathway
Lymphocyte migration Positive regulation of inflammatory response Regulation of lymphocyte chemotaxis Regulation of chemotaxis
Antigen receptor-mediated signal
Regulation of immune effector process
Neutrophil activation
Regulation of innate immune response Prr signaling pathway Innate immune response Receptor-mediated endocytosis Positive regulation of immune process Leukocyte migration Positive regulation of secretion
–9 –6 –3 0 3 6 9
−log (adjusted P value)
10
Significant FDR < 0.05 and logFC > 0.5 Not significant
3PMAL-CD_30M 3PMAL-4C-CD 3FTAB-1CDc_40Mh EOPA-3C-φM A1RECF-2C-CD C1DC-CD_10M 2SLAGL-CD_40M A9CELC-3C-CD A9CELC-CD_20M C1DC-1C-CD C1DC-2CDc_30Mh 4ARLIL-CDp_20Mh 3APC-2C-tsaM
3XPG-4C-φM
NACV-orcaM_11M NACV-5C-φM 1NCF-ekilonoM_11Mh 1SBHT-1C-φM 41DC-1C-onoM 41DC-onoM_50Mh 41DC-onoM_50M 61DC41DC-onoM_70Mh A3RGCF-2C-onoM 61DC-onoM_60Mh A3RGCF-onoM_60M 1BASPT-tsaM_10Mh R7LI-1C-tsaM 1NF-orcaM_80M OCRAM-6C-φM 5PBAF-orcaM_90M 2RLOF-orcaM_41M AQ1C-orcaM_01M CQ1C-MAT_21Mh AQ1C-2C-φM B1LI-orcaM_01Mh 3C-orcaM_21M PTLP-orcaM_90Mh 1PPS-MAT_31Mh 3PRLN-orcaM_80Mh GERE-orcaM_70M
Cluster dendrogram
2.0
1.0
0
thgieH
C1DC A1RECF A01CELC 1AQD−ALH 1BQD−ALH 1MTIFI 8FRI A9CELC 1RCX
2
KNLC 1BPD−ALH
1
1APD−ALH 3PMAL
0
1ODI
1−
2 4 S FR LA I GL 21A001S ZYL NACV 9A001S 2BGTI MAGTI 1ANIPRES 1RC3XC 5ARLIL 1BRLIL GERE 86DC 02LCC GERA 8LCXC NR1LI AFGEV 1SBHT A3CEBOPA 01LCXC RACF 1NF 2NILP 1PMIT A3RGCF 361DC 5PBAF AQ1C 2SGR 1I4LI BFAM 3MTIFI 6IFI 2ESANR B3RGCF 4LCC B1LI FNT 2PSUD EOPA 3C 9PMM 1PPS IBFGT PTLP OCRAM PMAH 1RPUN 2RLOF BMNPG 41DC 76IKM
Average expression Percent expressed 0 25 50 75 100
Dataset
OC
HCC
CRC
1.00
0.75
0.50
0.25 0
M04_DC−LGALS2 M01_DC−CD
M
1C 02_DC−CLEC9
M
A
03_DC−LA
MP3
seticsa
ni
sretsulc
CD
fo
noitroporP
*P = 0.046 Resistant
Sensitive
*P = 0.044
Cell–cell interaction between TeMs and T cells
Ligand Percent of 25 50 75 Ligand Percent of 25 50 75
expression0 1 2 3 expression expression0 1 2 3 4 expression
XCL1 CXCR4 Percent of XCL1 CXCR4 Percent of
P C P X B C P L3 A A D C G K R R V 3 1 expression P C P X B C P L3 A A D C G K R R V 3 1 expression
C C C P C C C C C C C C C C C C F C C C X X C C C X C C X X X X 4 C C C C C C C L L L L L L L L 2 2 1 8 2 2 1 2 L L L L L L L 1 9 4 1 5 2 1 8 1 1 1 2 1 3 1 0 2 G C C C A C C A C C C C C C C D P C X X X C C X I R C C C C N C P C D C C C K C R K C P R R R R R R E R R R R R R 1 R 4 5 9 4 3 2 2 7 1 0 4 3 5 2 1 1 D R ex e p c 2 5 7 1 2 2 r e . 5 5 . . 0 0 e 0 5 p s t s o io r n C C C P C C C C C C C C C C C C F C C C X X C C C X C C X X X X 4 C C C C C C C L L L L L L L L 2 2 1 8 2 2 1 2 L L L L L L L 1 9 4 1 5 2 1 8 1 1 1 2 1 3 1 0 2 G C C C A C C A C C C C C C C D P C X X X C C X I R C C C C N C P C D C C C K C R K C P R R R R R R E R R R R R R 1 R 4 5 9 4 3 2 2 7 1 0 4 3 5 2 1 1 D R ex e p c 2 5 7 1 2 3 r e 0 5 5 0 e p 0 s t s o io r n
C C C C L L 3 5 S C L C C R 7A 5 1 C C C C L L 3 5 S C L C C R 7A 5 1 1
CCL1 GPR152 0 CCL1 GPR152
CCL4 CCR8 CCL4 CCR8 0
M07_ M M a 1 c 0 r _ o M −E ac R M r E o 1 G 2 −C _ M 1 Q ac A ro−C3 T01 T _C 02 D _ 4 C T − 0 D C 3 4 C T _ − 0 C R A 4 7 D N _ 4 C X − T A D F 0 1 4 O 5 − X _ C C P T X D 3 0 3 4 6 C T − _ P 0 R C D 1 7 D _ C 8 C D T − D 0 C 1 8 8 T C − 0 _ R A C 9 7 N D _ T C X 8 1 A D − 0 G 2 8 _C − Z T C D M 11 8 X _ K C − 3 H C D A R 8 V − 1 S C L R C 2 4A10 M07_ M M a 1 c 0 r _ o M −E a R c M r E o G 1 − 2 C _ M 1 Q ac A ro−C3 T01_ T C 0 D 2 4 _C − T C 0 D C 3 4 T _ R − C 0 A 7 D 4 N 4 _ X C − A T D F 1 0 O 4 5 − X _ C P C X T 3 D 0 3 4 C 6 − _ R T P C 0 1 D D 7 C 8 _C D − T C 1 D 0 C 8 8 T − R _ 0 A 7 C 9 N D _ X 8 C T A − 1 D 2 G 0 8 _ Z − C M C D X K 8 3 − C H R A 1 VCR2
romut yramirP sisatsatem mutnemO
+
+/–
– ++ +++
+++ + +
+++
+++ –
+/– ++ +++
–
+/–
– + +++
+/–
– +++ ++
– +++ ++
– +
+/– + +
FTL
CD74
CCL4CCL3APOE HLA−DRA
HLA−DRB1 IL1B C1QC H C L 1 A Q − A D C P 1 B Q 1 B IFITM3 CXCL2HLA−DRB5
CXCL8 HLA−DQA1 S100A6
CCL20HLA−DQB1
HLA−DMA
C V C EG L C 5 3 F R A G C S X 2 CL10 C C A D LM 1 IF 6 3 I 3 TM S F 2 1 A 0 B 0 P A 5 9 C C C I X L X X C 6 C C L L L 1 9 1 1 I 2 L1 H 0 K3L V Y C V A M E1 N F C A C C R N R C 1 1 O S100A8
f
Article https://doi.org/10.1038/s43018-023-00599-8
and ascites were clustered primarily by their tissue distribution. Exclud- and relatively lower levels of HLA-II genes (Fig. 4e), indicative of a dys-
ing the proliferating macrophages (M13 and M15), clusters showing functional state of macrophages which further contributed to a pro-
relatively comparable enrichment in tumor sites (M07, M10 and M12) tumor environment in ascites. Moreover, AeMs also showed strong
were denoted as tumor-enriched macrophages (TeMs), whereas the enrichment of leukocyte migration pathway, with specifically upregu-
remaining clusters that showed relatively preferential enrichment lated expression level of CCR1 (Fig. 4e). Notably, we also noticed that
in ascites (M08, M09, M11 and M14) were named as ascites-enriched AeMs highly expressed LYVE1 and CD163 (Fig. 4e), signature genes of
macrophages (AeMs) (Fig. 4b). Among TeMs, C3+ M12 was the dominant tissue-resident macrophages (RTMs) found in multiple human tissues38,
subset distributed in both Pri.OT and Met.Ome, whereas EREG+ M07 implying that RTMs might be an important source of macrophages
and C1QA+ M10 tended to be enriched in Met.Ome. Likewise, four AeM in ascites.
subsets were further marked by their featured genes, leading to the
classification of FN1+ M08, FABP5+ M09, VCAN+ M11 and FOLR2+ M14. Dichotomous ontogeny of TeMs and AeMs in OC
To further understand the heterogeneity of macrophage subsets Recent studies in mice have suggested that tumor-associated mac-
across different tissues and tumor types, we also evaluated the similari- rophages could have both RTM and monocyte origins39. Here, to fur-
ties between macrophage clusters in our study and those reported in ther infer the ontogeny of TeMs and AeMs, we defined an RTM score
HCC and CRC, as mentioned above. C3+ TeMs (M12) and C1QA+ TeMs using a set of tissue-resident relevant genes, including CD163, LYVE1,
(M10) were clustered into the same branch, resembling the IL1B+ macro FOLR2, MRC1 and TIMD4 (Fig. 5a,b)39–41. Two of three TeM subsets (M07
and C1QC+ TAMs identified in colon cancer, respectively (Fig. 4c). These and M12) showed much lower RTM scores compared to M10, whereas
clusters highly expressed C1QA and major histocompatibility complex about half of cells from AeM clusters (M09 and M14) had relatively
(MHC) class II molecules associated with antigen presentation (Fig. 4a higher RTM scores (Fig. 5a). Additionally, a set of monocyte-derived
and Extended Data Fig. 6d). Notably, C3+ TeMs not only expressed genes macrophage-associated genes were used to complement the analysis of
related to phagocytosis and inflammation (C3, CCL4 and TNF)31, but also macrophage origins. The results displayed a similar trend, with M07 and
upregulated transcriptomic programs associated with the response to M12 exhibiting the highest potential of monocyte-derived ontogeny
tumors (APOE, SPP1 and TGFBI)32,33 (Fig. 4a and Extended Data Fig. 6d), (Extended Data Fig. 7b)28,42. These findings implied that macrophages
which was distinct from the IL1B+ macro in CRC28. Conversely, EREG+ identified in OC had two possible origins, with monocyte-derived mac-
TeMs (M07) exhibited high expression of chemokines like CCL20, CCL4, rophages as the dominant components in tumors and RTMs accounting
CXCL10, CXCL8 and angiogenesis-related gene VEGFA, as well as low for a large part in ascites-enriched subsets. As reported, although RTMs
expressions of HLA-related genes, resembling the SPP1+ TAM identified in adult tissues are gradually replaced by circulating monocytes, there
in CRC (Fig. 4a,c and Extended Data Fig. 6d). Among AeM cells, FABP5+ constantly exists a self-maintenance population of RTMs arising from
AeM (M09), FOLR2+ AeM (M14) and FN1+ AeM (M08) were all clustered embryonic precursors43. To explore the extent to which embryonic peri-
into the same branch with HCC ascites-enriched C6-MARCO, likely toneal macrophages contribute to ascites-enriched RTMs, we employed
reflecting the environmental plasticity of macrophages. Of note, VCAN+ Ms4a3Cre-RosaTdT monocyte fate-mapping mouse models42 to precisely
AeM (M11), characterized by high expression of transcripts associated quantify the different ontogeny of macrophages in malignant ascites
with monocytes (VCAN, S100A9 and S100A12)34, was clustered into the of ovarian tumor-bearing mouse. Based on the flow cytometry data,
same branches with tumor-enriched C5-VCAN and ascites-enriched nearly half of the AeMs were embryonic-derived macrophages with
C1-THBS1 in HCC dataset and FCN1+ mono-like cells in CRC (Fig. 4c and ~45% proportion of tdTomato− cells (Extended Data Fig. 7c). Further,
Extended Data Fig. 6d). These two macrophages in HCC were defined as ~70% CD163+TIM4+ RTMs in malignant ascites were contributed by
myeloid-derived suppressor cells (MDSCs) in the same differentiation embryonic precursors (Fig. 5c and Extended Data Fig. 7d,e). These
lineage27. Therefore, VCAN+ AeMs (M11) in our study were more likely results implied that embryonic macrophages as an important resource
to be MDSCs distributed in ascites. of AeMs, contributing to the maintenance of RTMs in the peritoneal
We next investigated the different functional states of TeMs (M07, microenvironment in OC.
M10 and M12) and AeMs (M08, M09, M11 and M14). We observed that Subsequently, we characterized the distinct signatures of TeMs
TeMs predominantly expressed MHC class II molecules and CD74, which or AeMs with divergent ontogeny. RTM-derived M10 expressed sig-
are essential for antigen processing and presentation to CD4+ T cells. nificantly higher levels of complement C1Q genes and HLA-II related
TeMs also upregulated the expressions of VEGFA, implying a role for genes (HLA-DRA, HLA-DPB1 and HLA-DQA1) (Fig. 5d). By contrast,
tissue macrophages in promoting tumor angiogenesis. Moreover, we monocyte-derived M07 showed specific expression of VEGFA, IL1B
observed upregulated chemokines (such as CCL3/4/5 and CXCL10/11/12) and TNF. The pathway analysis also revealed a strong enrichment
expression in TeMs (Fig. 4e), suggesting the importance of tumor mac- of complement activation and antigen processing and presenta-
rophages in recruiting T cells35,36. Cell–cell interaction analysis within tion pathways in RTM-derived M10, whereas tumor angiogenesis,
tumor tissues also confirmed that TeMs participated actively in the response to IL-1 and NF-κB pathways were significantly increased in
recruitment of T cells through CXCL10/11–CXCR3, CCL3/4/5–CCR5 and monocyte-derived M07 (Fig. 5d). Multicolor imaging data further
CXCL12–CXCR4 signaling (Fig. 4f). In primary tumors, EREG+ macro confirmed the coexistence of monocyte-derived M07 EREG+ macro
(M07) expressed increased levels of CXCL10/11, whereas C3+ macro and RTM-derived M10 C1QA+ macro in ovarian tumors (Extended
(M12) highly expressed CXCL12; however, in metastatic tumors, it was Data Fig. 7f). Next, we compared the distinct biological features of
surprising to find that the dominant source of CXCL10/11 was switched ascites-enriched RTMs (M09 and M14) and monocyte-derived AeMs
from EREG+ M07 to C3+ M12 and C1QA+ M10 upregulated the expres- (M08 and M11). RTMs in ascites exhibited higher expression levels of
sion level of CXCL12, indicating a reprogramming of macrophages in complement C1Q genes (Extended Data Fig. 7g), consistent with the
metastatic tumors. In addition, EREG+ TeM (M07) and C3+ TeM (M12) tumor-enriched RTMs. Besides, ascites-enriched RTMs expressed spe-
also showed preferential expression of molecule CCL4 and CCL5, which cifically increased levels of FABP5, associated with tumor regulation44
binds to CCR4 and CCR8, receptors highly expressed by CD4+ T cells. and CCL2 molecule responsible for monocyte recruitment (Extended
reg
We also found very similar interaction patterns between TeMs and Data Fig. 7g). Bulk RNA sequencing of tumor-bearing fate-mapping
ascites T cells (Extended Data Fig. 7a). Collectively, our data suggested mice models also confirmed the upregulation of C1q genes, Fabp5 and
the function of TeMs in recruiting T cells and shaping an immuno- RTM signature genes, including Timd4 and Cd163 in ascites-enriched
suppressive niche in tumors. embryonic macrophages (Fig. 5e and Extended Data Fig. 7h), further
By contrast, AeMs exhibited high expression levels of S100A confirming that embryonic macrophages might be a major source
family (S100A8 and S100A9) associated with tumor progression37 of RTMs in the ascites of patients with OC. Of note, we observed that
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1145
Article https://doi.org/10.1038/s43018-023-00599-8
a c
d
ascites-enriched RTMs expressed lower levels of CD74 and HLA-II Stromal cells contribute to shaping the ascites TME
related genes than monocyte-derived AeMs, contrary to the observa- For nonimmune cells, we first dissected the gene signatures and
tions of TeMs (Extended Data Fig. 7g), likely reflecting the different tissue distributions of all 19 stromal clusters revealed in this study
ontogeny of RTMs in ascites and tumor tissues. Furthermore, we (Fig. 6a,b and Extended Data Fig. 8a–c), including 9 fibroblast clusters
compared the differences between RTMs distributed in tumor and (COL1A2+ PDGFRA+), 4 mesothelial cell (MC) clusters (MSLN+UPK3B+),
ascites. Ascites-enriched RTMs (M09 and M14) exhibited specific 4 clusters of pericytes (CSPG4+TRPC6+) and 2 vascular smooth muscle
enrichment of oxidative phosphorylation and metabolic-related path- cell clusters (MYH11+CNN1+)46,47. Among MCs, DES+ MC (S11) was the
ways, whereas tumor-enriched RTMs (M10) significantly upregulated dominant stromal cluster in ascites (Fig. 6b,c), which was confirmed
immune response and immune cell migration pathways (Extended by multicolor immunohistochemistry (Fig. 6d). In contrast, VCAN+
Data Fig. 7i). Notably, RTMs in ascites also showed specific high expres- MCs (S13) were highly enriched in Met.Ome (Fig. 6b and Extended
sion of CCL2, which mediates the recruitment of CCR2+ monocytes45. Data Fig. 8b,c). It has been shown previously that MCs undergo
Taken together, our analyses establish the connections between mac- morphological changes and detach from the peritoneal surface during
rophage ontogeny-specific features and their various functions in OC peritoneal metastases16. We therefore compared the expression lev-
tumor growth. Further studies will be needed to fully discriminate els of cell-adhesion-associated genes (CD44, ICAM1, ITGAV, ITGB1, ITGB8,
macrophage ontogeny and to attribute the specific functional profile VCAM1, VCAN, CADM3 and CLDN1) in tumor-derived MCs and found the
of these macrophages to their ontogenies. lowest expression in DES+ MCs (Fig. 6e and Extended Data Fig. 8d),
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1146
erocs
MTR
****
P = 9.6 × 10–212
4
****
P = 4.56 × 10–184
3
2
1
0
M07 M12 M10 M11 M08 M09 M14
TeMs AeMs
M07 M10 e
6 Response to tumor necrosis factor
Cell chemotaxis
Response to IL-1
Regulation of apoptotic signaling pathway
Regulation of inflammatory response I−κB kinase/NF−κB signaling Cytokine secretion Regulation of cell−cell adhesion
Regulation of angiogenesis 4 Neutrophil activation
Epithelial cell proliferation Regulation of innate immune response Negative regulation of immune process Regulation of lymphocyte activation
Complement activation Antigen processing and presentation Regulation of immune effector process 2 Regulation of inflammatory response
Response to IFN-γ
Receptor-mediated endocytosis Neutrophil activation Regulation of innate immune response Regulation of lymphocyte activation Activation of innate immune response Negative regulation of defense response 0 Regulation of endocytosis Response to tumor necrosis factor
0 2 4 6 –12 –9 –6 –3 0 3 6 9 12
Mean expression of M07 −log (adjusted P value)
10
01M
fo
noisserpxe
naeM
80
60
40
20
0
Significant FDR < 0.05 and logFC > 0.5 Not significant
sllec
+4MIT
+361DC
ni
noitroporP
***P = 0.0002
mato– mato+
Tdto Tdto
CD74 C1QBC1QCAPOE
HLA−DRB1HLA−DRA
C1QA APOC1 HLA−DRB5 HLA−DQA1 HLA−DPB1 NFKBIA
M C AR D C 16 O 3 H H L L A A − − D D M QB A 1 CXCL8CCL3IL1B
CXCL16 CCL4
HLA−DMB SPP1 S100A6 CXC F L O 9 LR2 S100A4 TGFBI TNF EREG LYVE1 VCANVE T G NF F A A IP8 CCL5 CXCL11
4dmiT 361dC 2rloF
1.6
AeEM−1
AeEM−2 0.8
AeEM−3
AeEM−4 0
AeMM−1
AeMM−2
−0.8 AeMM−3 AeMM−4 −1.6
361DC 1EVYL 4DMIT 2RLOF 1CRM
b
1.8
M07_Macro−EREG
M08_Macro−FN1
0.9
M09_Macro−FABP5
M10_Macro−C1QA 0
M11_Macro−VCAN
–0.9
M12_Macro−C3
M14_Macro−FOLR2
–1.8
Fig. 5 | Two different origins of tumor-enriched and ascites-enriched unpaired two-sided t-test. d, Differentially expressed genes (left) and
macrophages in HGSOC. a, Bar plot showing the mean expression levels differentially activated pathways (right) between tissue-resident macrophages
of tissue-resident marker genes in all macrophage clusters. Center line (M10) versus monocyte-derived macrophages (M07) in tumor sites (left).
indicates the median value, lower and upper hinges represent the 25th Genes, P value < 0.05, two-sided Wilcoxon test adjusted by the BH procedure;
and 75th percentiles, respectively and whiskers denote 1.5 × interquartile log(fold change) > 0.5. Pathways, Gene Ontology (GO), adjusted P value by
2
range. *P < 0.05, **P < 0.01, ***P < 0.001, two-sided t-test, adjusted by the BH the BH procedure <0.05. n = 10 primary tumor and n = 4 matched omentum
procedure. b, Expression levels of tissue-resident relevant genes in seven metastatic tumor from ten patients with HGSOC were used for analysis. e, Heat
macrophage clusters. Rows represent clusters and columns represent genes. map showing expression levels of tissue-resident marker genes in macrophages
c, Quantification of tdTomato− or tdTomato+ macrophages as a percentage of of mouse ascites using ascites samples from n = 4 mice. AeEM, ascites-
total CD163+ TIM4+ RTMs in n = 4 independent experiments using n = 4 mice enriched embryonic macrophage; AeMM, ascites-enriched monocyte-derived
ascites samples, related to Extended Data Fig. 7d. Center line indicates the macrophage. Rows represent repetitive samples and columns represent genes.
median value, bottom and top hinges represent the 25th and 75th percentiles, For a,b, data were summarized from all n = 31 HGSOC samples.
respectively and whiskers indicates min to max. *P < 0.05, **P < 0.01, ***P < 0.001,
Article https://doi.org/10.1038/s43018-023-00599-8
suggesting that DES+ MCs were more likely to fall off into the ascites samples of platinum-resistant patients (Fig. 7e). Moreover, IL13RA1+
from tumor tissues. Meanwhile, we observed a significantly decreased E02 expressed higher levels of SPARC, COL4A1, COL4A2, ANGPT2 and
cell adhesion potential of MCs in Met.Ome compared to that in Pri.OT ITGB1 (Fig. 7f), genes involved in vasculature development, epithelial
(Fig. 6f). These analyses indicated that the loss of cell–cell adhesions cell proliferation and migration pathways (Fig. 7g), suggesting that
could be a reason for MCs to shed from the omentum into ascites, IL13RA1+ E02 could contribute to chemotherapy resistance by pro-
which provides a favorable condition for tumor cell metastasis and moting tumor angiogenesis and migration. In contrast, VCAM1+ E06
colonization. showed preferential expression of HLA-II related molecules and ACKR1,
Notably, DES+ MCs showed high expression of CXCL12, CXCL13 a marker of venular endothelium and with a known role in adhesive
and CXCL16 (Extended Data Fig. 8e), reminiscent of the recently leukocyte-endothelial interactions52 (Fig. 7f,g), indicating that VCAM1+
reported immunomodulatory cancer-associated fibroblasts (CAFs) E06 might assist lymphocytes infiltration and participate in antigen
identified in ascites15. By integrating our dataset with that of CAFs in OC processing and presentation to enhance the chemotherapy sensitivity.
ascites, we further confirmed the similarities between DES+ MCs in our Therefore, we hypothesized that the relative proportions of IL13RA1+
study and the immunomodulatory CAFs15 (Fig. 6g and Extended Data versus VCAM1+ endothelial cells might serve as a biomarker to pre-
Fig. 8f). We also observed that DES+ MCs had high potential to exten- dict the benefit from chemotherapy. Furthermore, we also examined
sively interact with memory T cells and macrophages (Fig. 6h,i). One of whether IL13RA1+ and VCAM1+ endothelial clusters were associated with
the significantly enriched ligand–receptor pairs was CXCL12–CXCR4, the long-term prognosis of HGSOC patients using data from The Cancer
which is associated with recruitment of immune cells48. This could help Genome Atlas (TCGA). We found that patients highly expressing the top
explain the underlying reasons for the abundance of immune cells in 20 signature genes of IL13RA1+ E02 had shorter overall survival (Fig. 7h),
ascites and the inflammatory milieu of ascites. DES+ MCs were also further confirming their functions in tumor angiogenesis; however,
predicted to interact with macrophages and MAIT cells via C3-C3AR1 signature genes of VCAM1+ E06 were not significantly correlated with
(ref. 49), which would lead to the further recruitment of these cells to clinical outcomes of patients with HGSOC (Extended Data Fig. 9d). We
enhance the inflammatory response in ascites (Fig. 6h). Taken together, also used another independent microarray dataset to validate these
the results indicate that DES+ MCs might constitute a key cellular com- results (Extended Data Fig. 9e,f).
ponent that plays an important role in the regulation of inflammatory
and immune responses in OC ascites. MAIT in ascites as potential predictors of platinum response
It has been reported that ascites accumulated in patients with OC is
Endothelial cell phenotypes associated with chemotherapy associated with chemotherapy response and prognosis5. Here, we
response further investigated the distinct compositions of the ascites micro-
Among all endothelial cells, E07 and E08 were annotated as lymphatic environment between responsive and nonresponsive patients. Based
endothelial cells based on the expression of canonical marker PROX1 on the linear model analysis of all ascites-derived T cells using Milo,
(ref. 50), whereas other clusters were identified as vascular endothelium we noticed that MAIT cells were highly enriched in ascites of respon-
(Fig. 7a and Extended Data Fig. 9a). It has been reported that tumor sive patients before therapy, which was supported by the R data
o/e
angiogenesis mainly undergoes two alternate processes, including (Fig. 8a,b). It has been reported that MAIT cells could accumulate and
vessel sprouting by migrating tip endothelial cells and sprout elon- function in the peritoneal cavity during a pathological process or in
gating51, suggesting that the tip cells could accelerate angiogenesis the tumor tissues53,54. In our study, MAIT cells were mainly detected
whereas other endothelial cells were relatively more static. Here, clus- in PB and ascites (Fig. 2b). We were able to detect 50 unique shared
ter E03 showed high expression of genes associated with endothelial TCR clones between ascites- and blood-derived MAIT cells (Fig. 8c),
cell migration and matrix remodeling50 (Fig. 7b and Extended Data suggesting PB as a potential source of ascites MAIT cells. Moreover,
Fig. 9b), resembling the tip cells detected in lung tumor, which indicated ascites-enriched MAIT cells upregulated homing receptors CXCR3 and
poor prognosis of patients50. CXCR4, which bind to CXCL12 and CXCL10, molecules upregulated by
Further deciphering the transcriptional trajectories of endothelial other ascites-enriched cells (such as cDC1 and DES+ MC) (Fig. 8d–f),
cells using PAGA, we found that IL13RA1+ E02 and VCAM1+ E06, two further supporting the chemotaxis of MAIT cells. Ascites-enriched
major endothelial cell clusters in tumor tissues, exhibited unique MAIT cells also showed preferential expression of genes related to cell
features (Fig. 7c,d). We observed that IL13RA1+ E02 showed closer activation (TMIGD2, CCL4 and CCL5) (Fig. 8d,e), suggesting an acti-
connectivity with the tip-like cells (E03) and upregulated tip cells vated status. We next compared the characteristics of ascites-enriched
signatures, whereas VCAM1+ E06 were positioned at another branch MAIT cells from responsive and nonresponsive patients. MAIT cells
(Fig. 7b,d and Extended Data Fig. 9b). Notably, the proportion of captured from responsive patients overexpressed genes associated with
IL13RA1+ E02 was significantly increased in Pri.OT samples of non- T cell activation, such as ZFP36, JUN, DUSP1, NCR3 and KLRB55–57, whereas
responsive patients, whereas VCAM1+ E06 was depleted in Pri.OT MAIT cells of nonresponsive patients highly expressed genes related to
Fig. 6 | Characterization of stromal cell clusters of HGSOC, especially DES+ tumor samples (e) or in all mesothelial cells in n = 10 primary tumor, n = 4
mesothelial cells in ascites. a, UMAP projection of 19 stromal cell clusters omentum metastasis and n = 8 ascites from ten patients with HGSOC, respectively
colored by clusters (left) and heat map showing expressions of selected genes (f). Center line indicates the median value, bottom and top hinges represent the
across indicated clusters (right). b, Tissue preference of each stromal cell cluster 25th and 75th percentiles, respectively and whiskers denote 1.5 × interquartile
estimated by the ratio of observed to expected cell numbers (R ). c, Frequency range. *P < 0.05, **P < 0.01, ***P < 0.001, two-sided Wilcoxon test. Each dot
o/e
of each ascites-enriched stromal cell cluster as a proportion of all stromal corresponds to a single cell. g, Hierarchical clustering comparing the similarity of
cells in ascites, n = 8 ascites samples were analyzed. Center line indicates the stromal cell clusters in our dataset with those reported in OC ascites by Aviv. The
median value, bottom and top hinges represent the 25th and 75th percentiles, clusters in black font were detected in our dataset. h, Bubble heat map showing
respectively and whiskers indicates min to max. *P < 0.05, **P < 0.01, ***P < 0.001, the mean interaction strength for selected ligand–receptor pairs between DES+
unpaired two-sided t-test. d, Representative example of ascites cell precipitation mesothelial cells and various immune cell clusters. Dot size indicates P value
from one patient with HGSOC stained by multicolored immunohistochemistry generated by permutation test, colored by interaction strength levels. DES+
and the corresponding quantification plot. Original magnification, ×20; scale MCs were cells providing ligands. i, Chord diagram showing predicted cell–cell
bar, 50 μm. n = 3 individual patient samples were examined independently. interactions of CXCL12–CXCR4 ligand pair between DES+ mesothelial cells and
e,f, Bar plots showing the geometric mean expression levels of adhesion- various immune cell clusters in ascites. The arrow width indicates the interaction
associated genes in three mesothelial cell clusters from a total of n = 14 HGSOC strength levels. For a,b,h,i, all n = 31 HGSOC samples were analyzed.
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1147
Article https://doi.org/10.1038/s43018-023-00599-8
a
b c
R
+/– – – ++ ++ o/e ++ + ++ Max
– ++ +
– ++ + 0
– + ++
+++ ++ –
– ++ +
– + ++ +
+++ +/– –
– ++ +/–
– ++++/– +
– ++++/– +
– + + +++
+++ + +
+ ++ ++
+ ++ + + ++ + +++ + +/– +++ + ++
e f g
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1148
NLP BP seticsA TO.irP emO.teM
S01 S02
S03
S04
S05
S06
S07
S08
S09
S10
S11(MC-DES)
S12
S13
S14
S15
S16 S17 S18 S19
1.5
1.0
0.5
Pri. OT Met. O me Ascites
ni
sCM
fo
erocs
noisehdA
setis
tnereffid
S07
4 S03
S05
S16
0 S01 S09 S15
S17
S08 S14
−4 S10 S19
S13 S1 S 2 04 S18
S11
−8
−10 0 10
UMAP_1
h i CXCL12_CXCR4 M09_Macro−FABP5 M11_Macro−VCAN M08_Macro−FN1 M14_Macro−FOLR2 M02_DC−CLEC9A S11_MC−DES M01_DC−CD1C T02_CD4−ANXA1 T11_CD8−SLC4A10 T09_CD8−CX3CR1 T04_CD4−CX3CR1
T08_CD8−GZMK
2_PAMU
S01_CAF−C3
S02_CAF−COL15A1
S03_CAF−CXCL10
S05_CAF−MME
S06_CAF−TNXB
S07_CAF−TWIST1
S08_CAF−VEGFA
S09_Fibrocyte−CD34
S10_MC−CXCL10
S11_MC−DES
S13_MC−VCAN
S14_Pericyte−CCL21
S15_Pericyte−IL6
S17_Pericyte−TRPC6
S18_SMC−IL6
S19_SMC−ELN
S04_CAF−MKI67 S12_MC−MKI67
S16_Pericyte−MKI67
M M T T T M M 0 0 1 T 1 0 T M 4 0 1 1 9 4 0 9 0 _ 1 _ 2 _ 0 _ M C _ 2 _ M 8 M C M _ C _ 8 D 0 D _ C a D a _ D a C 8 1 c C M c D 4 c _ 8 D − r − r D r − 4 o a − S o 8 o C C C − c C − L − − − L A F r X C − F X G V o E O N C 3 A 4 3 C − Z C C X L D B C A F M A 9 R A P N R 1 1 R N A K C 2 0 5 1 1 1 1 4RCXC_21LCXC 3RCXC_01LCXC 3RCXC_21LCXC 4PPD_2LCXC 4PPD_01LCXC 3RBFGT_1FGF 3RBFGT_1BFGT 3RBFGT_3BFGT GLSAF_A1FSRFNT GLSAF_B01FSRFNT GLSAF_SAF 2L4LCC_2CMRGP 74DC_APRIS FIM_RFGE 1RA3C_3C 1RPF_1AXNA 1PRL_KDM FLKC_6PRL ARLIP_99DC APRIS_1FSC 01LI_rotpecer
01LI
B31FSFNT_04DC NRG_RFGE NRG_A1FSRFNT
08_ C AF− VE G S F 11 A _ M C S − 1 D 2 E _ S M C− M S K 13 I6 _ M 7 C− V C A N
S
Interaction score 1.5 1.0 0.5 0 Pval_group Not significant ** 0.01
S11_MC−DES
seticsa
ni
sllec
lamorts
fo
snoitcarF
d
MSLN UPK3B WT1
DES
NLE 1A51LOC 01LCXC 1BEZ
2
76IKM
1
NACV 1A1LOC
0
PAF BXNT
1−
ARFGDP 2RA5C 1TSIWT 2IANS 8LCXC AFGEV EMM NPDP 5LCC 43DC 3C 21LCXC B3KPU NLSM ULC SED 1TW 12LCC 4SBHT 4AJG 5SGR 4GPSC BRFGDP 6CPRT 3HCTON 11HYM 1NNC NLGAT 6RGL 6LI 2ATCA 4A001S
Scaled expression Percent expressed 0 25 50 75 100
1A51LOC−FAC_20S
BXNT−FAC_60S 43DC−etycorbiF_90S
6LI−CMS_91S NLE−CMS_02S 12LCC−etycireP_41S 4SBHT−etycireP_71S 76IKM−etycireP_61S 6LI−etycireP_51S 6CPRT−etycireP_81S
7_stsalborbiF_vivA
6_stsalborbiF_vivA 01LCXC−CM_01S 76IKM−CM_21S
9_stsalborbiF_vivA
8_stsalborbiF_vivA SED−CM_11S
AFGEV−FAC_80S NACV−CM_31S
76IKM−FAC_40S
01LCXC−FAC_30S 1TSIWT−FAC_70S 3C−FAC_10S EMM−FAC_50S
Cluster dendrogram
0.8
0.4
0
thgieH
1.5
1.0
0.5
S1
0_
M
C-
C X CL1 0
S11_
M C- DES
S13_
M
C- V C A N
-romut
fo
erocs
noisehdA
sCM
devired
*** P = 4.6 × 10–4 – – *** P = 2.1 × 10–4
– – *** P = 2.5 × 10–4
– – 1.0
– –
– –
0.8 – –
–
– – 0.6
– –
– Merge 100
– 0.4
80
–
– – 60
– – 0.2 40
– – – – 0 20 – – 0 – – Sample 1 Sample S 2 ample 3
** P = 0.0014 *** P = 3.56 × 10–9
** P = 0.0026
* P = 0.029 *** P = 5.2 × 10–22
+B3KPU+NLSM
ni )%(
sllec +SED
sllec
lailehtosem
+1TW
Article https://doi.org/10.1038/s43018-023-00599-8
a b
2.0
1.5
1.0
0.5
c d
f
immunosuppression such as LAG3 and IFITM3 (Fig. 8g), suggesting that might help patients benefit from chemotherapy, whereas MAIT cells in
MAIT cells in ascites from patients with HGSOC with different responses ascites of nonresponsive patients were more likely to be dysfunctional.
to chemotherapy also exhibited different functions and phenotypes. Furthermore, the levels of activated MAIT cells in ascites could be a use-
Altogether, these results indicated that immune-activated MAIT cells ful and noninvasive predictor of effective responses to chemotherapy.
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1149
sCE
fo
erocs
ekil-piT
E07 E01
E05
5 E08
E06
0
E02
−5 −10 UM E0 A 4 P_1 0 E03 E 01_E N E D 0 O 2 − _E C N C D L O 14 −I E L 0 13 3 R _E E A N 0 1 D 4_ O E E 0 − N K 5 D I _ T O E N − M D O KI E − 6 S 0 7 E 6 R _E P E N I 0 N D 7 E O _ 2 L − y V m E C p 0 A h 8 M a _ t L 1 i y c m −P p D h P a N tic−PL AT
h
2_PAMU
E01_ENDO−CCL14
E02_ENDO−IL13RA1
E03_ENDO−KIT
E04_ENDO−MKI67
E05_ENDO−SERPINE2
E06_ENDO−VCAM1
E07_Lymphatic−PDPN
E08_Lymphatic−PLAT
1.0
0.8
0.6
0.4
0.2
0
sCE
lla
ni
oitaR
)TO.irp(
e
E02_ENDO−IL13RA1
E03_ENDO−KIT
E06_ENDO−VCAM1
E05_ENDO−SERPINE2
E 01_E N D E 0 O 2 − _ C E C N L D 1 O 4 −IL E 1 0 3 3 R _ A E E 1 N 0 D 4 O _E − E N K 0 D I 5 T O _E − N M D K O I6 − E 7 S 0 E 6 R _ P E I E N N 0 D E 7 2 O _L − y V m C p E A h 0 M a 8 1 t _ i L c y − m P D p P h N atic−PL AT E01_ENDO−CCL14
5
4
3
2 1
0
0 1 2 3 4 5
Mean expression of E02
60E
fo
noisserpxe
naeM
E02 E06
Extracellular matrix organization
Extracellular structure organization Regulation of angiogenesis
Regulation of vasculature development
Positive regulation of angiogenesis
Cell−substrate adhesion CD74 Positive regu B la a t s io e n m o e f n v t a m sc e u m la b t r u a r n e e d o e r v g e a l n o i p z m at e io n n t
Ameboidal-type cell migration EC migration Epithelium migration
Epithelial cell migration SPARC Regulation of epitheli T a i l s c su el e l m m i i g g r r a a t t i i o o n n
ACKR1 Collagen metabolic process
Immunoglobulin mediated immune response
HLA−DRA B cell-mediated immunity
V A SE C D L I A H R E CM L F L A 1U N −D N C R M C B T L 5 2 ITGB1C S O A L T 4 1C A O 2 L4A1 I A C A L H A m e n c d o u u m u t a m m i k t p g u e o o p t e n c i r l i n v e a n e y e m l f t p r l e i i e a r m e m o m s m n m p c m t m i e o g u a u s n a r c n n s a s t t e i e o t e i n v i r r o - g r a y a e e n t c s a s r io p t e n p i n o v s d o p a , n n p t c o s s i r e l n n e e a g s s s e s e c i n c e t a l a l l t s p i u o a r n t f h ac w e a y receptor CXCL2 AN F G L P T T 1 2 R R R e e e g g sp u u o l l a a n t t s i i o o e n n t o o o f f I F i p n N r f o - l γ a te m in m a a c to ti r v y a t r i e o s n p c o a n s s c e ade
THYM1IR4435−2IHGGFBP3 P R r e o g t u e l i a n t a io c n t iv o a f t c io o n m c p a le sc m a e d n e t activation
CXCL12GJ C A A 4 2 ESM1 H Ly u m m p o h r o al c i y m te m -m un e e d i r a e t s e p d o i n m s m e unity
–20 –15 –10 –5 0 5 10 15 20
−log (adjusted P value)
10
Significant FDR < 0.05 and logFC > 0.5 Not Significant
TO.irp
ni
sCE
fo
noitroporP
* P = 0.012
** P = 0.0098
Sensitive Resistant E02_ENDO−IL13RA1 E06_ENDO−VCAM1
41LCC 1AR31LI TIK 76IKM 2ENIPRES 1MACV NPDP TALP 1EVYL 1XORP 1MACEP
Percent expressed 0 25 50 75 100
Scaled expression−1 0 1 2
Sensitive Resistant
g
1.00
0.75
0.50
0.25 P = 0.035 HR = 1.323
0
0 1,000 2,000 3,000 4,000 5,000
Time (days)
ytilibaborp
lavivruS
1.00 1.00
0.75 0.75
0.50 0.50
0.25 0.25
0 0
TCGA HGSOC data
Low E02 signatures group (n = 188)
High E02 signatures group (n = 186)
Fig. 7 | Characterization of endothelial cell phenotypes within two tumor e, Frequency of E02 (left) and E06 (right) cluster as a proportion of all endothelial
sites in HGSOC. a, UMAP projection of eight endothelial cell clusters colored by cells in ten primary tumor samples from n = 7 platinum-sensitive and n = 3
clusters (left) and heat map showing expression patterns of selected genes across platinum-resistant patients. Center line indicates the median value, bottom and
indicated clusters (right). b, Bar plot showing the geometric mean expression top hinges represent the 25th and 75th percentiles, respectively and whiskers
levels of tip-like genes (referred to in Extended Data Fig. 9b) in eight endothelial denote 1.5 × interquartile range. *P < 0.05, **P < 0.01, ***P < 0.001; two-sided t-test.
cell (EC) clusters. Each dot corresponds to a single cell. Center line indicates the f, Differentially expressed genes between E02 and E06 cluster. P value < 0.05; two-
median value, bottom and top hinges represent the 25th and 75th percentiles, sided Wilcoxon test adjusted by the BH procedure; log(FC) > 0.5. g, Differentially
2
respectively and whiskers denote 1.5 × interquartile range. c, Frequency of activated pathways between E02 and E06 cluster. GO, adjusted P value by the BH
each endothelial cluster as a proportion of all endothelial cells in n = 10 primary procedure <0.05. h, The Kaplan–Meier overall survival curves of patients with
tumor samples from ten patients with HGSOC. The center line indicates the HGSOC grouped by the gene signature expression of IL13RA1+ ENDO cells.
median value, bottom and top hinges represent the 25th and 75th percentiles, HR, hazard ratio. Multivariate Cox regression. P value was determined by
respectively and whiskers indicates min to max. Each dot corresponds to one Kaplan–Meier survival curves and log-rank test. For a,b,d,f,g, all n = 31 samples
sample. d, PAGA analysis of endothelial cells. Each dot represents a cell cluster. from ten patients with HGSOC were used for analysis.
Article https://doi.org/10.1038/s43018-023-00599-8
a c Ascites PB
Cells
8 6
4
2
T11_CD8-SLC4A10(MAIT)
f M 01_ D C M − 0 C 2 D _ D 1 C C M − 0 C 3 L _ E D C C M 9 − 0 A L 4 A _ M D C P S 3 − 1 L 1_ G M A C L T − S 1 D 2 1 E _ C S D8−SL C4 A1 0 M 01_ D M C− 0 C 2 D _ D 1 M C C 0 − C 3 L _ D E M C C 9 − 0 L A 4 A _ M D C P S 3 − 11 L _ G M A C L T − S D 1 2 1 E _ C S D8−SL C4 A1 0
Receptor
CXCL17 GPR35
CCL18 PITPNM3 expression XCL1 CXCR4
CXCL3 ADGRV1 2
CXCL12 ACKR3
C C C X X X C C C L L L 1 1 2 1 0 C C C C X X C C C C R R R R 9 5 2 7 1
C C C C L L 1 2 9 2 C C X X C C R R 3 1 0
CXCL13 DPP4
C C C C L L 2 2 1 5 A C C C K R R 4 4 Percent of
CCL7 CCR10 expression
C C X C C L8 L5 A H C R K H R 4 1 25
CXCL8 CCR1 50
C C C C C C C XC L L L 2 2 1 L 1 4 1 G G P C C R P C R C C I 1 5 D R R 5 D 3 E 2 1 75
CCL5 CNR2
CCL3 SLC7A1 CCL4L2 CCR5 CCL16 GPR152
CCL4 CCR8
Ligand Percent of
expression 0 1 2 3 expression 2550 75
e g
Mean expression of resistant
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1150
evitisnes
fo noisserpxe
naeM
4
2
0
0 1 2 3 4 5
Average expression of MAIT in ascites
Significant FDR < 0.05 and logFC > 0.2 Not Significant
doolb
ni TIAM
fo
noisserpxe
egarevA
AC090498.1
CCL5
HBBICAM2 GNLY JUN
IGHA1 CXCR4
IFI6 M TM X I 1 G I D TM 2 2C IFI44LCXCR3
CXCR4 CCL4
Sensitive Resistant
3 6
SRP−dependent cotranslational protein targeting to membrane 2 4 Nuclear-transcribed mR Pr N o A te c in a t t a a b rg ol e ic ti n p g ro t c o e E s R s
Establishment of protein localization to endoplasmic reticulum
1 2 Cotranslational protein targeting to membrane Protein localization to endoplasmic reticulum
0 0 Vira V l i g ra e l n t e r a e n x s p c r r e ip ss ti i o o n n
Translational initiation CXCR3 CCL5 Protein targeting to membrane
Nuclear-transcribed mRNA catabolic process
3 4 Establishment of protein localization to membrane mRNA catabolic process 2 3 RNA c P a r t o a t b e o in li c t a p r r g o e c t e in s g s
2 Regulation of leukocyte-mediated cytotoxicity
1 1 P R o e s g i u ti l v a e ti o re n g o u f l a c t e io ll n k o il f li n ly g mphocyte-mediated immunity Positive regulation of leukocyte-mediated cytotoxicity 0 0 Positive regulation of cell killing
Leukocyte-mediated cytotoxicity
IFI44L TMIGD2 Positive regulation of leukocyte-mediated immunity
Regulation of lymphocyte-mediated immunity 3 R C e e g ll u k l i a ll t i i n o g n of leukocyte-mediated immunity 2 Positive regulation of immune effector process 2 L P y o m sit p iv h e o c re y g te u - l m at e io d n ia o te f d re im ce m pt u o n r i t b y inding 1 1 R C e e g ll u u l l a a t r i o re n s o p f o i n m se m t u o n i e ro e n ff i e o c n tor process Negative regulation of receptor binding 0 0 A A m nt y ig lo e i n d p fi r b o r c il e f s o s r i m ng a t a i n o d n presentation via MHC class Ib
–6 –4 –2 0 2 4 6
−log (adjusted P value)
10
noisserpxe
eneG
Sensitive Resistant b
T01_CD4-CCR7(T N ) T01_CD4-CCR7(T N ) 1.03 0.95 R o/e
1.5 T02_CD4-ANXA1(T CM ) T02_CD4-ANXA1(T CM ) 0.80 1.30 1.0
T03_CD4-FOXP3(T reg ) T03_CD4-FOXP3(T reg ) 1.19 0.72 0.5
T04_CD4-CX3CR1(T )
eff T04_CD4-CX3CR1(T ) 0.62 1.58
eff
T06_CD8-CCR7(T)
N T06_CD8-CCR7(T) 1.18 0.73
T08_CD8-GZMK( T ) N
EM
T08_CD8-GZMK(T ) 1.04 0.94
T09_CD8-CX3CR1(T ) EM
eff
T09_CD8-CX3CR1(T ) 1.02 0.97
T10_CD8-HAVCR2(T ) eff
EX
T11_CD8-SLC4A10(MAIT) T10_CD8-HAVCR2(T EX ) 1.29 0.56
T12_CD8-TRDV2(γδT) T11_CD8-SLC4A10(MAIT) 1.56 0.16
Mixed T cells T12_CD8-TRDV2(γδT) 1.41 0.38
log FC −5 0 5 Sensitive Resistant
d
5
4 HLA−B
CCL5 3
2
NCR3JUN
CCL4 ZFP36 1 DUSP1 TGFB1KLF2 FOSTNF LAG3T B R A A X C TGFBR2 0 MAPK14 KLRC1
0 1 2 3 4 5
MAIT enriched in ascites MAIT enriched in blood
Significant P value < 0.05 and logFC > 0.2 Not significant
Fig. 8 | MAIT cells in ascites predict the chemotherapy efficacy of patients in MAIT cells derived from ascites and PB. f, Dot plot showing the mean
with HGSOC. a, UMAP plot showing the distribution preference of MAIT cells in interaction strength for selected ligand–receptor pairs among major immune
eight ascites samples from n = 6 platinum-responsive and n = 2 nonresponsive and stromal cell clusters in ascites. n = 8 HGSOC ascites samples were analyzed.
patients as calculated by Milo. Each dot represents a single cell. b, The treatment- Dot size indicates percentage of ligand–receptor expression in cells of one
sensitivity preference (responsive or nonresponsive to platinum-based cluster, colored by average ligand–receptor expression levels. g, Differentially
chemotherapy) of each T cell cluster estimated by R score. n = 8 ascites samples expressed genes (left) and differentially activated pathways (right) between
o/e
from n = 6 platinum-responsive and n = 2 nonresponsive patients with HGSOC ascites-derived MAIT cells of n = 6 responsive versus n = 2 nonresponsive patients
were used for analysis. c, The distribution of clonal clonotypes within the MAIT with HGSOC. SRP, signal recognition particle; ER, endoplasmic reticulum.
cluster in ascites and PB. Each row represents an individual clonotype. d, Volcano Genes, P value < 0.05, two-sided Wilcoxon test adjusted by the BH procedure;
plot showing differentially expressed genes between MAIT cells in ascites versus log(FC) > 0.2. Pathways, GO, adjusted P value by the BH procedure < 0.05. For
2
PB. Genes, P value < 0.05, two-sided Wilcoxon test adjusted by the BH procedure; c–e, all n = 8 ascites sample and n = 5 blood samples from patients with HGSOC
log(FC) > 0.2. e, Violin plots showing the expression levels of selected genes were used for analysis.
2
Article https://doi.org/10.1038/s43018-023-00599-8
Discussion Human specimens
Despite the usage of platinum-based chemotherapy and improved sur- Fourteen patients pathologically diagnosed with OC were enrolled
vival, most patients with advanced OC undergo relapse due to chemo- in this study for single-cell sequencing. None of the patients had an
therapy resistance58. Here, we applied scRNA-seq to five tissue types of autoimmune disorder or a history of previous cancer. Only one patient
14 patients with OC with different sensitivities to chemotherapy and sys- diagnosed with undifferentiated OC was treated with adjuvant chemo-
tematically dissected the complexity of TME as well as the connections therapy. The disease stages of these patients were classified according
among five tissues. Our analyses revealed that ascites-derived GZMK+ to the 2018 International Federation of Gynecology and Obstetrics stag-
T , resembling the previously reported ‘pre-exhausted’ CD8+ T cells ing system. Fresh samples including primary ovarian tumor, omentum
EM
within tumors11,13,25, might be a major source of tumor-infiltrating T metastatic tumor, PLNs, malignant ascites and PB were obtained from
EX
cells. These findings suggest that ascites-derived memory T cells could the patients during surgery. The patients received upfront debulking
migrate into tumor sites, acting as an additional important cell pool for surgery followed by at least six courses of platinum-based chemother-
TILs. As reported, pre-exhausted GZMK+ T subpopulation were regarded apy. Platinum resistance was defined as progression within 6 months
as pre-activated T cells which would accumulate in responsive lung can- after the last treatment course. Patients HGSOC3, HGSOC6, HGSOC7
cer and melanoma tumors following immune-checkpoint-based treat- and ECO1 were platinum-resistant (nonresponsive), whereas the other
ment11. We suspected that accelerating the migration of ascites-derived patients, except UOC1 were platinum sensitive (responsive). Patients
GZMK+ T cells into tumor sites could be a potential therapeutic strat- ranged in age from 43 to 82 years old, with a median age of 62 years.
EM
egy for OC. Moreover, we identified the proportions of MAIT cells in Five more patients pathologically diagnosed with HGSOC (patients
ascites as a potential predictive index in response to chemotherapy. HGSOC11–HGSOC15) were enrolled in this study for flow cytometry
Thus, our work on ascites-enriched T cells inspires us to rethink the analysis of T cells. The available clinical metadata of these patients are
functions of malignant ascites in shaping the tumor microenvironment. summarized in Supplementary Table 1.
Future studies will be needed to fully understand the functional roles
of these ascites T cells. In vivo mouse models
Here, we found that cDCs exhibited specific ascites-enriched All animal experiments were approved by the Institutional Animal
distribution patterns in OC. We hypothesized that the presence of Care and Use Committee of the Model Animal Research Center, Xinhua
cDCs in ascites might serve as a potential source of LAMP3+ DCs in Hospital, Shanghai Jiaotong University School of Medicine and were
tumor tissues as we found in T cells, which require additional in vivo performed in compliance with the guidelines for the care and use of
lineage-tracing validation. Moreover, it has been shown that mac- laboratory animals. The maximal tumor burden was not exceeded for
rophages were highly heterogeneous in the tumor TME59. We identi- mouse tumor experiments on the requirement of our ethics commit-
fied that macrophages of different origins and phenotypes coexisted tee. All Ms4a3TdT fate-mapping C57BL/6 mice were female and sourced
within the ovarian tumor and ascites, with TeMs functioning in immune from Florent Ginhoux Laboratories in Shanghai Institute of Immuno-
regulation and AeMs being more pro-inflammatory. RTMs in tumor logy. All mice were provided with water and food and maintained in
tissues have been reported to provide a pro-tumorigenic niche in lung a pathogen-free facility (12-h light–dark cycle, room temperature at
cancer and the omentum of ovarian tumors60. Our data also indicated 20–4 °C and relative humidity kept at 45–65%) at the Model Animal
the potential function of tumor regulation and monocyte recruitment Research Center, Xinhua Hospital, Shanghai Jiaotong University School
of ascites-enriched RTMs. of Medicine. Mice were given an intraperitoneal injection with 106 ID8
Ultimately, we identified specific populations of stromal cells cells in 500 μl sterile PBS (pH 7.4) to mimic the peritoneal spread of
playing important roles in tumor progression, such as DES+ meso- epithelial ovarian cancer when 4–5 weeks old. Details of cell lines are
thelial cells in ascites and IL13RA1+ endothelial cells in tumor site. Our shown in Supplementary Table 6. For flow cytometry studies and bulk
findings reveal that ascites-enriched DES+ MCs could help remold RNA-seq, bloody malignant ascites was collected 65 d after injection
the microenvironment of ascites through recruiting T cells and mac- of tumor cells.
rophages via CXCL12–CXCR4. The chemokine CXCL12 is known to be
expressed by CAFs and binds to the receptor CXCR4, mediating the ScRNA-seq data generation
recruitment of immune cells in tumors13. Further, IL13RA1+ endothe- Fresh tumor and lymph node samples were cut into approximately
lial cells exhibited tip-like signatures involved in angiogenesis and 1-mm3 pieces in RPMI-1640 medium (Invitrogen) with 10% fetal bovine
were significantly enriched in platinum-resistant patients. Navi- serum (FBS; Gibco) and enzymatically digested with a MACS Tumor
gating tip cells usually lead the way during vessel sprouting, which Dissociation kit (Miltenyi) for 30 min using a gentleMACS Octo Dis-
could facilitate tumor progression and implies a worse prognosis50. sociator (Miltenyi) at 37 °C. Dissociated cells were subsequently
These observations suggest that the abundance of IL13RA1+ tip-like passed through a 70-μm cell strainer (BD) and centrifuged at 400g
endothelial cells might activate angiogenesis and further influence for 10 min. The pelleted cells were then resuspended in red blood
chemotherapy resistance. cell lysis buffer (Miltenyi) and incubated on ice for 5 min to lyse red
In conclusion, we depicted a comprehensive atlas of the OC micro- blood cells. After washing twice with PBS (Invitrogen), cell pellets were
environment and revealed the connections between ascites and two resuspended in RPMI-1640 medium supplemented with 10% FBS. PB
tumor sites. Our work provided additional insights into the biologi- mononuclear cells were isolated using a leukocyte separation solu-
cal factors that help remodel the OC TME and identified specific cell tion (Sigma-Aldrich) according to the manufacturer’s instructions.
subpopulations that might serve as potential predictive markers for Malignant ascites samples were collected in 50-ml conical tubes (BD),
chemotherapy and prognostic markers of long-term survival, as well followed by centrifugation for 10 min at 400g. The remaining pel-
as new therapeutic targets or strategies for overcoming platinum let was washed twice with PBS and any residual red blood cells were
resistance and immune suppression. lysed using the above-mentioned procedure. The concentration of
single-cell suspensions was adjusted to about 500–1,200 cells per μl.
Methods Then, single-cell gene expression and immune repertoire measure-
This study complies with all relevant ethical regulations and was ments were conducted using the Chromium Single Cell V(D)J Reagent
approved by the Ethics Committee of Xinhua Hospital Affiliated to kit (10x Genomics) following the manufacturer’s instructions. All
Shanghai Jiaotong University School of Medicine and Fudan University subsequent steps were performed following the standard manufac-
Shanghai Cancer Center. Written informed consent was provided by turer protocols. Completed libraries were sequenced on an Illumina
all participants. NovaSeq6000 system.
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1151
Article https://doi.org/10.1038/s43018-023-00599-8
ScRNA-seq data processing human VDJ reference genome ‘GRCh38-alts-ensembl’. If two or more
Low-quality cells were filtered out if cells had fewer than 200 genes cells had the same identical α/β chain pair, the α/β chain pair were
expressed or >10% unique molecular identifiers (UMIs) linked to mito- identified as clonal TCRs and these T cells were considered to originate
chondrial genes. The gene expression matrices of the remaining cells from the same clonotypes, identified as clonal cells. After integrating
were generated with log normalization and linear regression using TCR results with the gene expression data of 10x Genomics data, we
the NormalizeData and ScaleData functions of the Seurat package identified TCR α/β-chain pairs for 59,334 cells. We then presented
(v.3.1.4). Cells with expression of more than one major cell marker were three STARTRAC indices to analyze different aspects of T cells based on
considered as doublets and removed from each cluster individually. paired single-cell transcriptomes and TCR sequences using STARTRAC
The remaining cells that passed the filtering criteria were considered (v.0.1.0) as previously described18. STARTRAC-expa, STARTRAC-migr
single cells. We also identified 2,010 platelets with high expression and STARTRAC-tran are designed to measure the degree of clonal
of pro-platelet basic protein. Almost all platelets were found in PB expansion, tissue migration and state transition of T cell clusters
mononuclear cell samples and they are not discussed in this study. For upon TCR tracking, respectively. The MAIT cells (T11) and γδT cells
visualization, the dimensionality of each dataset was further reduced (T12) were not included in these types of analyses because they have
using UMAP with the Seurat function Run-UMAP. The principal com- distinct TCRs.
ponents (PCs) used to calculate the embedding were the same as those
used for clustering. Developmental trajectory inference
PAGA. To characterize the developmental origins of CD4+ and CD8+
Unsupervised clustering and identification of cell T cells, respectively, we performed the partition-based graph abstrac-
subpopulations tion method PAGA23, a part of the single-cell analysis package Scanpy
After the main cell populations were identified by first-run clustering, (v.1.7.2) in Python (v.3.6.13)63, to infer the potential differential trajec-
we ran the Seurat pipeline for a second time. Unwanted effects caused tory. Moreover, we used PAGA to assess the most likely trajectories of
by percentage of mitochondrial UMI counts were removed by regres- cell progression among endothelial cells in OC. The computations were
sion in this run. The selection of the resolution on the characteristics carried out using default parameters. The edge connectivity between
of each dataset and the top n PCs from principal-component analysis each subpopulation node for all edges are further compared by using
were used for identification of clusters. For T lymphocytes, we per- an unpaired two-sided Student’s t-test.
formed extra batch correction across different samples with Harmony
(v.1.0) at the default settings. Small clustering groups with expres- Palantir. We also applied Palantir24 to complement the trajectory
sion of dual-lineage signatures, including EPCAM–PECAM1–CD3D, analysis using default parameters.
EPCAM–CD79A, PECAM1–CD79A and CD79A–CD3D, were removed
from downstream analysis. For other cell types, we did not conduct any Comparison dendrograms for similarity analysis of clusters
batch correction as no obvious clustering bias using raw transcripts per For an unsupervised comparison of the myeloid clusters identified
million-like expression data would affect our downstream analyses. from multiple datasets, we identified the top 2,000 highly variable
Supplementary Table 5, showing the distribution of cell subclusters genes across different clusters, calculated the mean expression of these
in five tissues and patients with HGSOC, was provided as diagnostic genes in each cluster and performed hierarchical clustering using the
data to ensure that none of the clusters would arise from individual distance defined as (1 − Pearson correlation coefficient)/2. Here, we
tissues or patients. used the batch-corrected expression value from the CCA function of
the Seurat package. For comparison of stromal cell clusters reported
Identification and analysis of malignant cells with CNV in OC ascites15 and that detected in ascites in our study, we used the top
estimation 1,000 highly variable genes.
Copy number variation (CNV) for individual cells was estimated using
inferCNV (v.1.2.1) with a 100-gene sliding window. The method to use Differential expression and Gene Ontology enrichment
for smoothing was pyramidal. Genes with an average read count <0.1 analysis
among reference cells were filtered when running inferCNV. Endothelial The significantly overexpressed marker genes for clusters were
cells, stromal cells, lymphoid cells and myeloid cells were used to define identified using the FindAllMarkers() function of Seurat. Genes with
the reference. Epithelial cells were used for the observations. Down- adjusted P value < 0.05 by Wilcoxon rank-sum test were defined as
sampling was conducted for both the reference and observations to cluster-specific signature genes. For two different clusters, we used the
increase the speed of analysis. Epithelial cells were classified to malig- Wilcoxon test to evaluate the significance of each gene, with multiple
nant cells using a similar method previously described by Wu et al.61 hypothesis correction using the BH procedure. Genes with adjusted
P value <0.05 were considered as differentially expressed genes that
Tissue distribution of clusters were further used for GO enrichment analysis with the clusterProfiler
We calculated the R for each cluster in different tissues to quantify package (v.3.14.3). GO terms with adjusted P values <0.05, using the BH
o/e
the tissue preference of each cluster18,25. The expected cell numbers procedure, were considered significant.
for each combination of cell clusters and tissues were obtained from
the chi-squared test. One cluster was identified as being enriched in a RTM phenotype analysis
specific tissue if R > 1. For most clusters, we used the R index (+++, To identify the origins of macrophages enriched in tumors and ascites,
o/e o/e
R > 3; ++, 1 < R ≤ 3; +, 0.2 ≤ R ≤ 1; +/−, 0 < R < 0.2; and −, R = 0) we used a panel of genes associated with tissue-resident macrophages/
o/e o/e o/e o/e o/e
to define the cluster preference in a specific tissue. Furthermore, when monocytes to define the signature of macrophages in our study. The
analyzing the association between each T cell subset and treatment RTM/monocyte-like phenotype of each macrophage cluster was
responses to platinum-based chemotherapy, we applied miloR (v.1.5.0), defined as the mean expression of gene signatures. P values were meas-
a differential abundance testing framework based on K-NN graphs and ured by two-sided t-test using Rstatix (v.0.7.0).
generalized linear models62.
Cell–cell interaction analysis
TCR analysis We used cellphoneDB (v.3.0.0)64 based on cellphoneDB database v.2.0.0
The TCR sequences for each single T cell from 10x Genomics were to infer cell–cell interactions of selected ligand–receptor pairs between
processed using CellRanger (v.3.0.2) with the manufacturer-supplied tumor-enriched macrophages and T cell subsets, DES+ mesothelial
Nature Cancer | Volume 4 | August 2023 | 1138–1156 1152
