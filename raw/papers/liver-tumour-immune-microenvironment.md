---
source_path: /mnt/c/Users/Administrator/Zotero/storage/PGWLX6D2/Xue 等 - 2022 - Liver tumour immune microenvironment subtypes and neutrophil heterogeneity.pdf
ingested: 2026-04-23
sha256: 4428fb816ea17949
---

Article
Liver tumour immune microenvironment
subtypes and neutrophil heterogeneity
https://doi.org/10.1038/s41586-022-05400-x Ruidong Xue1,7, Qiming Zhang2,7, Qi Cao1,7, Ruirui Kong1,7, Xiao Xiang3,7, Hengkang Liu1,
Mei Feng1, Fangyanni Wang1, Jinghui Cheng1, Zhao Li3, Qimin Zhan4, Mi Deng4, Jiye Zhu3,8 ✉,
Received: 7 September 2021
Zemin Zhang2,5,8 ✉ & Ning Zhang1,4,6,8 ✉
Accepted: 30 September 2022
Published online: 9 November 2022
The heterogeneity of the tumour immune microenvironment (TIME), organized by
Check for updates various immune and stromal cells, is a major contributing factor of tumour metastasis,
relapse and drug resistance1–3, but how different TIME subtypes are connected to the
clinical relevance in liver cancer remains unclear. Here we performed single-cell
RNA-sequencing (scRNA-seq) analysis of 189 samples collected from 124 patients and
8 mice with liver cancer. With more than 1 million cells analysed, we stratified patients
into five TIME subtypes, including immune activation, immune suppression mediated
by myeloid or stromal cells, immune exclusion and immune residence phenotypes.
Different TIME subtypes were spatially organized and associated with chemokine
networks and genomic features. Notably, tumour-associated neutrophil (TAN)
populations enriched in the myeloid-cell-enriched subtype were associated with an
unfavourable prognosis. Through in vitro induction of TANs and ex vivo analyses of
patient TANs, we showed that CCL4+ TANs can recruit macrophages and that PD-L1+
TANs can suppress T cell cytotoxicity. Furthermore, scRNA-seq analysis of mouse
neutrophil subsets revealed that they are largely conserved with those of humans.
In vivo neutrophil depletion in mouse models attenuated tumour progression,
confirming the pro-tumour phenotypes of TANs. With this detailed cellular
heterogeneity landscape of liver cancer, our study illustrates diverse TIME subtypes,
highlights immunosuppressive functions of TANs and sheds light on potential
immunotherapies targeting TANs.
Primary liver cancer (PLC) has three major histological subtypes—
A large-scale single-cell atlas of liver cancer
hepatocellular carcinoma (HCC), intrahepatic cholangiocarcinoma
(ICC) and combined hepatocellular and intrahepatic cholangiocar- To survey the TIME landscape across PLC covering all cell populations,
cinoma (CHC)4. Despite recent progress in immunotherapies5, our we performed scRNA-seq analysis of 160 samples of 124 treatment-naive
understanding of the baseline TIME landscape in PLC is limited, patients, including 79 with HCC, 25 with ICC and 7 with CHC (Fig. 1a,
precluding biomarker identification for better patient stratifica- Extended Data Fig. 1a and Supplementary Tables 1 and 2). A total of
tion. A comprehensive single-cell study covering most cell popu- 89 TIME cell clusters were identified among 1,092,172 cells obtained
lations and three major subtypes of PLC with established clinical (Fig. 1b,c, Extended Data Figs. 1 and 2, Supplementary Fig. 1, Supplemen-
parameters is needed. Functional contributions of neutrophils in tary Note 1 and Supplementary Table 3). Owing to our large cohort and
cancer are increasingly recognized6–10 with both anti-tumour11,12 and enrichment-free strategy, we captured more diverse populations and
pro-tumour13,14 roles reported. scRNA-seq has been used to dissect identified a substantial proportion of neutrophils lacking characteri-
TIME components of PLC15–22 and neutrophil heterogeneity23–25, but zation in PLC15–22 (Extended Data Fig. 1i,j). TIME cell clusters exhibited
these studies usually involve antibody-based cell enrichment and obvious tissue and cancer type preference, and some were associated
are limited in cohort size. Owing to the short lifespan of neutrophils with aetiologies (Extended Data Fig. 2b–d). Copy-number analysis
and technical difficulties in handling them, the functional hetero- showed that most epithelial cells were tumour cells, showing either
geneity of neutrophils in cancer remains unclear. Here we analysed high hepatic or biliary scores (Extended Data Fig. 1e–h). In contrast
the cellular landscape of 189 samples collected from patients and to TIME clusters constituting cells across different patients, tumour
mouse models with liver cancer, dissected the TIME subtypes, and cell clusters tended to be patient specific. On the basis of PLC subtype
investigated the phenotypic and functional heterogeneity of neu- composition representing real-world epidemiology, our multifaceted
trophils in liver cancer. data encompass well-annotated clinical information, a single-cell atlas
1Translational Cancer Research Center, Peking University First Hospital, Beijing, China. 2BIOPIC, Beijing Advanced Innovation Center for Genomics, School of Life Sciences, Peking University,
Beijing, China. 3Beijing Key Surgical Basic Research Laboratory of Liver Cirrhosis and Liver Cancer, Department of Hepatobiliary Surgery, Peking University People’s Hospital, Beijing, China.
4International Cancer Institute, Peking University Health Science Center, Beijing, China. 5Changping Laboratory, Beijing, China. 6Yunnan Baiyao Group, Kunming, China. 7These authors
contributed equally: Ruidong Xue, Qiming Zhang, Qi Cao, Ruirui Kong, Xiao Xiang. 8These authors jointly supervised this work: Jiye Zhu, Zemin Zhang, Ning Zhang. ✉e-mail: gandanwk@vip.
sina.com; zemin@pku.edu.cn; zhangning@bjmu.edu.cn
Nature | Vol 612 | 1 December 2022 | 141
Article
a b
124 patients, 160 samples
Single-cell scRNA-seq 10
Primary tumour suspension
HCC ICC CHC Others Intrahepatic 0 (79/100) (25/37) (7/9) (13/14)
metastasis
Alb-cre/Trp53fl/fl, 8 mice, 29 samples
Adjacent liver –10
Peripheral blood
WES: 84 patients
Myc-Δ90Ctnnb1 Myc-KrasG12D
(pTMC:5/18) (pTMK:3/11) –10 0 10
UMAP 1
with diverse populations and matched genomic profiles, enabling us to immunosuppression—enriched signatures of ‘immune suppres-
to examine the cellular heterogeneity landscape of PLC in detail. sion by myeloid cells’ and ‘pro-tumour cytokines’, and the association
with a worse prognosis collectively suggest immunosuppressive and
pro-tumour phenotypes of CM2, and the corresponding patients were
Cellular module analyses reveal five TIME subtypes
therefore designated as TIME-ISM (immune suppressive myeloid).
To investigate TIME subtypes of PLC, we examined co-enrichment pat- Stromal cells were enriched in both CM3 and CM4. The enrichment
terns of cells from tumour tissues. Hierarchy clustering identified five of two stromal clusters (EC_03_TFF3 and Fb_01_FAP), high expres-
stable cellular modules (CM1–CM5) (Fig. 2a and Extended Data Fig. 3a). sion of tumour-activated stromal genes such as COL1A1, MMP11 and
On the basis of the differential enrichment of CM1–CM5, we stratified ITGA1, enriched signatures of ‘matrix’ and ‘cancer-associated fibro-
the patients into five corresponding TIME subtypes (Fig. 2b–e), of blasts’ and the association with a worse prognosis led us to designate
which the properties were designated considering four aspects: (1) cell CM3-dominant patients as TIME-ISS (immune suppressive stromal).
clusters, (2) functional marker gene expression, (3) TIME-related gene By contrast, CM4 contained most endothelial cell and mesenchymal
signatures26 and (4) prognostic relevance (Extended Data Fig. 3b–f). clusters but lacked immune cells. Particularly, the enriched CXCL12+
CM1 contained activated myeloid and T cell clusters, including fibroblasts (Fb_02_CXCL12) could exclude T cells from tumour cells29.
mature dendritic cells enriched in immunoregulatory molecules On the basis of these results together, we propose an immune exclu-
(DC_03_LAMP3), CXCL9+ macrophages (Mph_06_CXCL9), T helper sion phenotype (TIME-IE). Unexpectedly, cytotoxic T cells (CD8T_08_
type-1-like cells (CD4T_07_CXCL13) and exhausted T cells (Fig. 1c). High GZMK) were also enriched in this cellular module. Using multicolour
expression of IFNG, GZMB and PDCD1, along with enriched signatures immunohistochemistry (mIHC), we observed that GZMK+ CD8+ T cells
of ‘co-activation molecules’ and ‘checkpoint molecules’ suggested mainly localized in the stroma yet were excluded from tumour regions
that CM1-dominant patients exhibited an immune-activated state, (Fig. 2f), suggesting that these immune-excluded T cells are actu-
and were therefore designated as TIME-IA (immune activation). The ally cytotoxic rather than exhausted. CM5 contained liver-resident
enrichment of Mph_03_SPP127 and high IL1B expression28—both related clusters including residential natural killer cells (NK_05_CD160),
142 | Nature | Vol 612 | 1 December 2022
2 PAMU
NK CD4+ T
CD8+ T γδT Treg
B Neutrophil Monocyte DC
Epithelial Macrophage
EC
Mesenchymal Mast
c
10
5 0
–5
–10 –5 0 5
UMAP 1
CD4+ T cells 15CD8T_04_GNLY 2 B_02_MS4A1_CD83 6 DC_06_STMN1 21Mph_09_STMN1 2 EC_02_CLEC4A_APOA2
1 CD4T_01_CCR7 16CD8T_05_KLRD1 3 B_03_MZB1 7 MonoDC Neutrophils 3 EC_03_TFF3
2 CD4T_02_SELL 17CD8T_06_CD69 4 B_04_STMN1 Monocytes 22Neu_01_MMP8 4 EC_04_ACKR1
3 CD4T_03_GPR183 18CD8T_07_PLCG2 NK cells 8 Mo_01_CD14 23Neu_02_S100A12 5 EC_05_KDR
4 CD4T_04_BAG3 19CD8T_08_GZMK 5 NK_01_FCGR3A_CX3CR1 9 Mo_02_CD16 24Neu_03_ISG15 6 EC_06_KDR_ESM1
5 CD4T_05_CD69 20CD8T_09_PDCD1_IFNG 6 NK_02_FCGR3A_CXCR4 Macrophages 25Neu_04_TXNIP 7 EC_07_KDR_APOA2
6 CD4T_06_PLCG2 21CD8T_10_PDCD1 7 NK_03_FCGR3A_IFNG 10Mono-like_01_CD14 26Neu_05_ELL2 8 EC_08_IGFBP3
7 CD4T_07_CXCL13 22CD8T_11_SLC4A10 8 NK_04_PLCG2 11Mono-like_02_CD16 27Neu_06_PTGS2 9 EC_09_PLCG2
8 CD4T_08_STMN1 23CD8T_12_IFIT3 9 NK_05_CD160 12Mono-like_03_CD14_CD16 28Neu_07_APOA2 10EC_10_STMN1
T reg cells 24CD8T_13_STMN1 10NK_06_ITGA1 13Mph_01_MARCO 29Neu_08_CD74 Mesenchymal cells
9 CD4T_09_FOXP3 γδT cells 11NK_07_STMN1 14Mph_02_CCL20 30Neu_09_IFIT1 11Mu_01_MYH11
10CD4T_10_FOXP3_CTLA4 25γδT_01_GNLY_S1PR5 Dendritic cells 15Mph_03_SPP1 31Neu_10_SPP1 12Mu_02_ABCC9
11CD4T_11_FOXP3_STMN1 26γδT_02_GNLY 1 DC_01_CLEC9A 16Mph_04_TREM2 32Neu_11_CCL4 13Mu_03_STMN1
CD8+ T cells 27γδT_03_KLRD1 2 DC_02_CD1C 17Mph_05_IL1B Mast cells 14Fb_01_FAP
12CD8T_01_CCR7 28γδT_04_STMN1 3 DC_03_LAMP3 18Mph_06_CXCL9 33Mast 15Fb_02_CXCL12
13CD8T_02_CX3CR1 B cells 4 DC_04_CD207 19Mph_07_SLC40A1 Endothelial cells 16Fb_03_KLF4
14CD8T_03_GZMK_S1PR1 1 B_01_MS4A1 5 DC_05_LILRA4 20Mph_08_APOE 1 EC_01_CLEC4A 17Fb_04_FABP4
2 PAMU
T cells
15
13 25 14 12
15 1 10 9 27 16 26 18 17 5 28 8 20 6 22 24 23 4 11 21 5 0
7 19 3 2
–5 10
–10
–10 –5 0 5 10
UMAP 1
2 PAMU
NK and B cells
10 3
4 5 NK 11 10 0 9
7 6 2 –5
8 5 1 –10
–10 –5 0 5 10
UMAP 1
2 PAMU
Myeloid cells
33 Neutrophils 10
13 21 6 30 29 32 27 19 31 5 20 18 16 28 24 25 2 2 3 6 17 15 22 0 14
3 24 121 1 1 0
9
–5
1 5 7 8 –10
–5 0 5 10
UMAP 1
2 PAMU
ECs and mesenchymal cells
1
8 6 2 5 4 7 9 10 17 3 Mesenchymal
11 15 13
16 12 14
Fig. 1 | The single-cell landscape of 124 patients with liver cancer. a, The killer cells; T , regulatory T cells; DC, dendritic cells; EC, endothelial cells.
reg
experimental workflow. The numbers of cases and samples collected for each c, UMAP plots showing TIME clusters. To facilitate illustration, cells are
cancer type and mouse model are denoted. b, Uniform manifold approximation grouped into four panels: T cells; natural killer (NK) and B cells; myeloid cells;
and projection (UMAP) plot showing the major cell types. Dots represent and endothelial cells (ECs) and mesenchymal cells. Colour code and cluster ID
individual cells, and colours represent different cell populations. NK, natural are shown.
f e
100 100 100 100 100
75 75 75 75 75
50 50 50 50 50
25 25 25 25 25
0 0 0 0 0
h
Kupffer cells (Mph_01_MARCO) and liver sinusoidal endothelial cells co-detection by indexing (CODEX) analysis of representative samples
(EC_01_CLEC4A), and was associated with a better prognosis. Thus, and reanalysing spatial transcriptomes of PLC33 successfully recapitu-
CM5-dominant patients were designated as TIME-IR (immune resi- lated the cellular composition of each subtype, further validating our
dence). TIMELASER framework at spatial resolution (Supplementary Note 2
Taken together, we name this classification scheme TIMELASER, and Extended Data Fig. 4f,g).
for ‘tumour immune microenvironment subtypes at the single-cell
resolution including immune activation, suppression, exclusion and
TIMELASER subtypes exhibit distinct features
residence phenotypes’ (Fig. 2d and Extended Data Fig. 5e,f). Survival
analysis by assigning each patient into a single-cellular module or by Diverse expression patterns of chemokines and cytokines and their
stratifying patients on the basis of each cellular module signature receptors observed in both tumour and TIME cells hint at underlying
showed consistent results (Fig. 2e and Extended Data Fig. 3e,f), sug- factors shaping diverse TIMELASER subtypes (Fig. 2g,h, Extended Data
gesting that our classification is robust and clinically relevant. Reanalys- Fig. 5a–d and Supplementary Note 3). Concordant chemokine expres-
ing published scRNA-seq15–17 and bulk RNA-seq datasets30–32 revealed sion patterns of tumour and TIME cells were observed in the TIME-IA
similar enrichment of five TIMELASER subtypes across PLC (Extended and TIME-ISM subtypes, suggesting positive-feedback loops. For exam-
Data Fig. 4a–e). These results validated our TIMELASER framework ple, CXCL9/10/11–CXCR3 ligand–receptor (L–R) pairs were enriched
and showed that our TIMELASER-derived signatures (Supplemen- in TIME-IA, whereas CXCL1/3/8–CXCR2 L–R pairs were enhanced in
tary Table 3) could also be used for bulk data. Moreover, performing TIME-ISM (Fig. 2g,h). These results, along with unique L–R pairs in other
Nature | Vol 612 | 1 December 2022 | 143
)%(
SFP
P = 0.19 P = 0.00077 P = 0.0046 P = 0.26 P = 0.0016
High (n = 56) High (n = 56) High (n = 56) High (n = 56) High (n = 72)
Low (n = 55) Low (n = 55) Low (n = 55) Low (n = 55) Low (n = 39)
0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30 0 10 20 30
Time (months) Time (months) Time (months) Time (months) Time (months)
9LCXC 01LCXC 11LCXC 31LCXC 5LCC 3RCXC 1LCXC 2LCXC 3LCXC 5LCXC 8LCXC 2LCC 3LCC 4LCC 7LCC 1RCC 2RCXC A1LI B1LI 41LCXC 12LCC 21LCXC 7RCC 4RCXC R7LI
g
TIME-IR TIME-IR Percentage ● 80
TIME-IE TIME-IE ● 85
● 90
TIME-ISS TIME-ISS ●95
TIME-ISM TIME-ISM
●100
TIME-IA TIME-IA Average
expression
–1 0 1
9LCXC 01LCXC 11LCXC 2LCC 3LCC 4LCC 1LCXC 2LCXC 3LCXC 5LCXC 8LCXC B1LI 81LI 51LCC 61LCC
a DC_03_LAMP3 ** b
CD4T_08_STMN1 * TIME-IATIME-ISMTIME-ISS TIME-IE TIME-IR Percentage
CD4T_07_CXCL13
Mph_06_CXCL9 0 100
CM1 CM2 CM3 CM4 CM5
CD8T_13_STMN1 CM1
CD8T_10_PDCD1
Neu_09_IFIT1 CM2 HCC
Neu_11_CCL4 CM3 ICC
Mph_02_CCL20 * CHC
Mph_03_SPP1 * CM4
Neu_10_SPP1 *
NK_06_ITGA1 CM5
C M D p 4 h T _ _ 0 0 4 6 _ _ T P R L E C M G 2 2 * c IFNG GZMB LAG3 d
CD4T_04_BAG3 ** CCL5 Tcellactivation PDCD1 TIMELASER
EC_03_TFF3 ** KLRB1 SPP1
TIME subtype 1 (TIME-IA)
EC
C
F
E
M
_
D
b
C
0
F
u
8
_
_
7
b
_
0
T
0
_
0
_
2
_
8
K
2
0
_
0
_
D
_
1
C
8
I
A
G
_
R
_
X
F
B
G
F
_
C
A
C
A
B
Z
L
P
P
C
P
M
1
O
3
9
2
K
A2
*
*
**
C
T
C
X
G
C
C
A
F
R
R
N
B
4
7
X
1
A1
Cell
migration Neutrophilim
yt
m inu
CX
S
C
F
IL
1
C
L
1
0
8
E
B
0
R
A
1
8
G
I
T
I
T
I
m
m
m
I
I
M
M
m
m
m
E
E
u
u
u
n
n
n
s
s
e
e
e
u
u
b
b
a
s
s
t
t
u
u
c
y
y
p
p
t
p
p
iv
p
p
e
e
a
r
r
2
3
e
e
ti
s
s
o
(
(
s
s
T
T
n
i
i
I
I
v
v
M
M
e
e
E
E
m
s
-
-
t
I
I
r
y
S
S
o
e
M
S
m
lo
)
)
a
id
l
DC_01_CLEC9A **
C
M
N D N
p
e 4 K
h
u T _
_
_ _ 0
0
0 0 5
1
7 3 _
_
_ _ C
M
A G D P
A
P O 1
R
R 6 A
C
1 0 2 8
O
3 * * CXCL1 F 2 GB
FG
m si
A
lobatem citapeH noitazinagro M
C
CE
OL1
M
A
M
1
IT P G 1 A 1 1 T I T
I
m
m
I I M M m
m
E E u
u
n
n
s s e
e
u u b b e
re
t t x y y
s
c p p
i
l
d
e e u
e
s 4 5
n
io
c
( ( T n T
e
I I M M E E - - I I E R ) )
EC_01_CLEC4A APOH COL1A2
Pearson’s correlation –1 1 –1 log10(haz 0 ard ratio 1 ) APOA1 LUM TIME-IE
TIME-IA TIME-ISM TIME-ISS TIME-IE TIME-IR
Tumour
Stroma
Expression in tumour cells Expression in TIME cells
Percentage ● 40
● 60
● 80
●100
Average
expression
–1 0 1
CD8GZMKα-SMAVONDAPI
Fig. 2 | Five TIME subtypes of PLC. a, The five cellular modules on the basis of pathway scaled to 0–1. d, Definitions of the five subtypes for TIMELASER
correlations of cell clusters from tumours. Key cell clusters from each cellular phenotypes. e, Progression-free survival (PFS) of cases stratified by each
module are shown on the right with the forest plot showing the hazard ratio cellular module. Statistical analysis was performed using log-rank tests.
based on progression-free survival. Statistical analysis was performed using f, Staining of GZMK+ CD8+ T cells (CD8 and GZMK), fibroblasts (α-SMA) and
log-rank tests; *P < 0.05; **P < 0.01, ***P < 0.001. b, The percentage of CM1–CM5 endothelial cells (VON) in TIME-IE. Scale bars, 100 μm (top) and 20 μm
across PLC cases. c, Radar plot showing marker genes and signalling pathways (bottom). g,h, The expression of specific cytokines, chemokines and receptors
enriched for CM1–CM5. CMs are denoted by colour. The distance from the dots in tumour cells (g) and TIME cells (h) across five TIMELASER subtypes.
to the centre of the circle represents the normalized expression of each
Article
TIME subtypes, suggest that distinct chemokine networks contribute
Chemokine secretion and immunosuppression
to the organization of TIMELASER subtypes.
phenotypes of TANs
Analyses of exome data identified recurrently mutated genes cor-
related with TIMELASER subtypes, including driver genes such as We next focused on phenotypes and functions of two TAN subsets—
TP53, CTNNB1, KRAS and IDH134 (Extended Data Fig. 6a–e and Supple- Neu_11_CCL4 and Neu_09_IFIT1. CCL4+ TANs (Neu_11_CCL4) expressed
mentary Fig. 2). Furthermore, despite the extensive heterogeneity of high levels of chemokine genes CCL3 and CCL4, confirmed by mIHC
tumour cells, we characterized eight common gene modules35 linked (Fig. 3d and Extended Data Fig. 8g). In vitro induced TANs also showed
with TIMELASER subtypes (Supplementary Note 4 and Extended Data elevated CCL4 expression (Fig. 3e, Extended Data Fig. 8h and Supple-
Fig. 6f,g). For example, the cell cycle gene module was enriched in mentary Fig. 3). We next directly investigated chemokine secretion
TIME-IA, indicating that these proliferating tumour cells would engage by ex vivo analysis of patient-derived TANs and non-tumoural neu-
with immune cells. In summary, our TIMELASER subtypes exhibit dif- trophils (that is, PBNs or ALNs, referred to as non-TANs). Compared
ferent chemokine networks, and are associated with distinct somatic with non-TANs, TANs showed higher accessibility signals of CCL4 and
alterations and transcriptomic profiles of tumour cells. CCL4 protein secretion (Fig. 3f,g). CCL4+ TANs were predicted to recruit
macrophages through CCL4–CCR5 (Extended Data Fig. 8i). Consistently,
more autologous monocytes were recruited in the chemotactic assay
Neutrophil heterogeneity in liver cancer
when co-cultured with TANs (Fig. 3h and Extended Data Fig. 8j). These
The enrichment of multiple neutrophil subsets in TIME-ISM, their results validate the chemokine-secreting function of TANs and support
association with poor prognosis and their scarcity36 led us to further that CCL4+ TANs could recruit macrophages.
examine neutrophils. Using mIHC, we validated the existence of neu- We also found that TANs showed a marked increase in CD274 (encod-
trophils in PLC, showing that ICC has significantly more neutrophils ing PD-L1) expression compared with non-TANs, with Neu_09_IFIT1
than HCC (Extended Data Fig. 7a), consistent with our observation that showing the highest expression (Fig. 3i). CD274 expression of in vitro
TIME-ISM is enriched in ICC. A total of 34,307 neutrophils were divided induced TANs continuously increased in a time-dependent manner
into 11 subsets that exhibited clear tissue separation and cancer-type (Fig. 3j). Fluorescence-activated cell sorting (FACS) analysis further
preference (Fig. 3a,b and Extended Data Fig. 7b–e). Neu_02_S100A12, showed significantly higher PD-L1 expression in in vitro induced TANs
Neu_03_ISG15 and Neu_04_TXNIP were mainly peripheral blood neu- compared with in the controls (Fig. 3k and Extended Data Fig. 8k).
trophils (PBNs) (Extended Data Fig. 7f), whereas Neu_05_ELL2 and ATAC-seq and FACS analyses also revealed higher accessibility signals
Neu_06_PTGS2 were mainly adjacent liver neutrophils (ALNs). All of of CD274 and PD-L1 expression in patient-derived TANs (Fig. 3l,m). To
the other six subsets (Neu_01_MMP8, Neu_07_APOA2, Neu_08_CD74, investigate whether the high PD-L1 expression of TANs would directly
Neu_09_IFIT1, Neu_10_SPP1 and Neu_11_CCL4) were enriched in tumours inhibit T cell activity, we co-cultured CD8+ T cells with in vitro induced
and designated as TANs. Developmental trajectory analysis revealed TANs (Extended Data Fig. 9a,b) or patient-derived TANs. CD8+ T cells
a clear sequential differentiation path from PBNs to ALNs and then co-cultured with in vitro induced TANs showed lower protein levels of
to TANs (Fig. 3a and Extended Data Fig. 7e). Notably, a combinatorial the T cell cytotoxic marker IFNγ and activation markers CD25 and CD69
high proportion of three TAN subsets from TIME-ISM (Neu_09/10/11, (Fig. 3n and Extended Data Fig. 9c). After adding anti-PD-L1 antibodies,
accounting for an average of 86.8% of total TANs) was associated with a the decline in IFNγ in CD8+ T cells was reversed in the PBN-MHCC97H
worse prognosis (Extended Data Fig. 7g), indicating pro-tumour func- group compared with in the controls (Fig. 3o and Extended Data
tions of these TANs. Fig. 9d), confirming that PD-L1 mediates the suppressive function of
Distinct gene signatures were observed across these neutrophil sub- TANs. Furthermore, autologous CD8+ T cells co-cultured with human
sets (Extended Data Fig. 7h,i). PBNs expressed high levels of secretory TANs exhibited lower proliferation property (CFSE), and lower levels of
vesicle signatures associated with anti-pathogen activities, whereas IFNγ, GZMB, PRF1 and CD25 (Fig. 3p and Extended Data Fig. 9e). Moreo-
ALNs and TANs expressed enhanced levels of matrix and chemokine sig- ver, mIHC revealed the physical proximity of PD-L1+ neutrophils and
natures. Analysing regulons of transcription factors (Fig. 3c) revealed PD1+ CD8+ T cells (Fig. 3q), supporting their direct interaction. These
higher SPI1 activity in PBNs, whereas NFE2L2 and CREM were more results together demonstrate that PD-L1+ TANs suppress cytotoxic
active in both ALNs and TANs. MAFG, BHLHE40 and HES4 were more CD8+ T cells in PLC.
active in TANs and possibly related to neutrophil reprogramming in Notably, two IFIT1+ neutrophil subsets enriched in PBNs (Neu_03_
tumours (Extended Data Fig. 8a). The activities of these transcrip- ISG15) and TANs (Neu_09_IFIT1) showed distinct PD-L1 expression
tion factors were confirmed by accessibility signals detected by assay (Fig. 3i). L–R analyses revealed that Neu_09_IFIT1 cells were more likely
for transposase accessible chromatin using sequencing (ATAC-seq) to interact with IFNG+ lymphocytes (CD8T_13_PDCD1_IFNG and NK_03_
analysis of matched patient-derived PBNs, ALNs and TANs (Extended FCGR3A_IFNG) through IFNγ–type II IFNR (Supplementary Note 7 and
Data Fig. 8b). Collectively, our results present a layered landscape of Extended Data Fig. 9f–j). These results indicate that interactions with
11 neutrophil subsets and support that neutrophil differentiation may IFNγ+ cells may contribute to the high PD-L1 expression of Neu_09_IFIT1.
be orchestrated by transcription factors in a spatiotemporal manner
(Supplementary Note 5 and Supplementary Table 3).
Conserved neutrophil subsets in human and mouse
To systematically examine the function of TANs, we first induced
liver cancer
TANs in vitro by co-culturing human PBNs with three human liver can-
cer cell lines—HepG2, HCCLM3 and MHCC97H—and a control cell line, To further examine heterogeneous functions of TANs in vivo, we built
HEK293T (Extended Data Fig. 8c–f). Compared with the controls, PBNs two new spontaneous liver cancer mouse models, with the pTMC mice
co-cultured with various cancer cell lines showed concordant higher developing mainly HCC and pTMK mice developing mainly ICC (Methods
expression of pro-angiogenesis and chemokine production signatures, and Extended Data Fig. 10a–c). We performed scRNA-seq analysis of
indicating TAN-like phenotypes, and we therefore termed these cells 21 samples that included peripheral blood, tumour-adjacent liver and
‘in vitro induced TANs’. Signatures of PBN and ALN subsets were down- tumours collected from 6 mice (Extended Data Fig. 10d,e and Sup-
regulated, whereas most TAN subsets were upregulated, with that of plementary Table 4). A total of 17,780 neutrophils were divided into
Neu_11_CCL4 as the highest (Supplementary Note 6 and Extended Data 12 clusters showing clear tissue specificity and ordered develop-
Fig. 8f), suggesting that this subset is more favoured than others in our mental trajectory (Fig. 4a,b and Extended Data Fig. 10f–h). Unbiased
co-culture system. These results support the spectrum of neutrophil cross-species data integration of neutrophil subsets and concordant
subsets identified from our scRNA-seq data. expression of key signature genes suggested that neutrophils in mouse
144 | Nature | Vol 612 | 1 December 2022
CXCR1 ● ● ● ● ● ● ● ● ● ● ●
CXCR2 ● ● ● ● ● ● ● ● ● ● ●
CCR1 ● ● ● ● ● ● ● ● ● ● ● CCR2 ● ● ● ● ● ● ● ● ● ● ● CXCL8 ● ● ● ● ●●●●●●●
CCL2 ● ● ● ● ● ● ● ● ● ● ● CCL3 ● ● ● ● ● ● ● ● ● ● ● CCL4 ● ● ● ● ● ● ● ● ● ● ●
CCL5 ● ● ● ● ● ● ● ● ● ● ● 1 2 3 4 5 6 7 8 9 1011
Average exp. Percentage
e
3 CXCL8 2 1 P = 2.7 × 10–3 0 –1 –2
and human were largely conserved (Fig. 4c, Extended Data Fig. 10i–k depletion resulted in significant reductions in liver cancer nodules and
and Supplementary Note 8). Specifically, three TAN subsets from tumour weight (Fig. 4e,f). Both the number of TANs and PD-L1 expres-
TIME-ISM (Neu_09/10/11) corresponded to mNeu_10/11/12, respec- sion of TANs decreased after anti-Ly6G treatment compared with the
tively. Notably, higher Cd274 expression was observed in mouse TANs, isotype control (Fig. 4g and Extended Data Fig. 10l–m). IHC analysis
consistent with that in human TANs (Fig. 4d). These results laid the confirmed that there were lower numbers of neutrophils and prolifera-
basis for investigating neutrophil-based therapy in our mouse models. tive malignant cells in the Ly6G-blockade group (Fig. 4h and Extended
Data Fig. 10n). We further assessed the neutrophil-depletion efficacy
by parallel detection of surface and intracellular Ly6G38 (Extended
Neutrophil depletion attenuates tumour progression
Data Fig. 10o,p). Analysis of intracellular Ly6G confirmed that about
A collectively pro-tumour phenotype of the TIME-ISM TANs 70% of neutrophils were depleted after Ly6G blockade, consistent with
(Neu_09/10/11) led us to examine the therapeutic effect of eliminating IHC (Fig. 4h and Extended Data Fig. 10n). Furthermore, we observed a
those pro-tumour TAN subsets in vivo. As a combinatory in vivo elimi- 46.6% reduction in infiltrating macrophages (Extended Data Fig. 10n).
nation strategy specifically targeting Neu_09/10/11 was not available, Although Ly6G blockade did not alter the number of CD8+ T cells,
we reasoned that neutrophil depletion using anti-Ly6G antibodies37 their exhaustion states were relieved as shown by decreased levels
might be the most proximate way to mimic such therapy. Neutrophil of the checkpoint markers PD-1 and TIM3 (Fig. 4g and Extended Data
Nature | Vol 612 | 1 December 2022 | 145
●● ● ● 0 75 –1 2
])h 0 susrev
emit( CF[gol 2
])h 0 susrev
emit( CF[gol 2
f
CCL4 CCL4 3,787 bp 4 2 P = 1.4 × 10–3 0 –2
g h Time (h) Time (h) 0 18 24 30 Non TAN
Time (h)
fo rebmuN setyconom P = 0.0316 P = 0.0175 6,000 600 0 0 Non TAN )1–lmgp( 4LCC
i j k l
PBN 1 CD274 2 5.0 P = 1.7 × 10–3 ALN 3 2.5 4 TAN 5 0 6 7 –2.5
8 m 9 CEACAM8 1 1 0 1 1.5 P = 3.5 × 10–2 0 0.1 1.0 PBN ALN 0.5 TAN 0 0 CD274 0.04 0 18 24 30 Time (h)
n o 80
0 PBN P - B H N E P K B 29 N 3 P - T H B e N p - P G H B 2 C N C - L M M H 3 CC97H
)%( sllec
T
+8DC
fo sllec
+γNFI
)%( sllec
T
+8DC
fo sllec
+γNFI
P = 0.0349 P = 0.0300 P = 0.0331 P = 0.0398 80 P = 0.4134 P = 0.4605 P = 0.0364 P = 0.9334 P = 0.0310 P = 0.3312
P = 0.0418 P = 0.0241
0 PB P N B – N Ig P – G B H P N c E o B K – n a N 2 t n 9 – r P t o 3 H i B - l T E P N – K D I – g 2 - M G L 9 P 1 H 3 c B T C o – N C n a – t 9 n r M o 7 ti l H - H P – C D I C g - G L 9 1 7 c H o – n a t n ro ti l -PD-L1
1L-DP
fo IFM
P = 0.0065
P = 0.0027 400 P = 0.0002 P = 0.1568P = 0.0284 P = 0.0107 P = 0.0067
0 PB P N B –H N EK P 2 B 93 N T –H PB ep N G –H 2 P C B C N L – M M 3 HCC97H Non TAN
p q
1L-DPfoIFM P = 0.0110 2,000 0
P = 0.0079
NonTAN
)%(
ESFC
80
0
)%(
+γNFI
P = 0.0135 80
0 NonTAN
BMZG foIFM
P = 0.0281
1× 104 0 NonTAN 1FRPfoIFM
P = 0.0249
8× 103 0 NonTAN )%( +52DC
NonTAN
P = 0.0228
60 0 NonTAN
)1–lmgp(
γNFI
P = 0.0229 400 CD66b PD-L1 CD8 PD1 DAPI R1
0
R2 fo sllec +8DC +1DP )%( sllec T +8DC P = 0.0003 30 20 10 Tu 0 mou S r tro ma
fo sllec+b66DC+1L-DP )%( sllec
T
+b66DC
100 TAN980 Non68 0 101 105 PD-L1–BV421
P = 0.0004 100 60
20
0
Tu mou S r tro ma
egatnecrep .xaM
b ± ± ± ± +++ SPI1 (98g) d
± ± ± ± +++ FOXO3_ext (17g)
IRF1 (343g) ± ± ± + +++ STAT2 (25g)
± ± +++++ ± STAT1 (47g) ± ± +++ ± ± NFE2L2_ext (212g) ± ± +++ ± ± CREM (297g)
± ++ ± ± ± ETS2_ext (53g) ± ++ ± ± ± MAFG (12g) BHLHE40_ext (12g) +++ ± ± ± ±
HES4_ext (13g) +++ ± ± ± ± XBP1 (14g) +++ ± ± ± ± YBX1_ext (39g)
PBAL Regulon activity 0 0.2
Tumour
Stroma
CCH CHC CCI
a 11 c
10
4 9
8 7 0 1
6 5 –4 4
Predicted order 3 of differentiation –8 2
–5 0 5 0 1 UMAP 1
2 PAMU
34,307 cells 1 Neu_01_MMP8
2 Neu_02_S100A12 AL
1 5 7 3 Neu_03_ISG15 PB
Tumour 2 6 11 10 5 4 N N e e u u _ _ 0 0 4 5 _ _ T E X LL N 2 IP R ± o/e 1 0 6 Neu_06_PTGS2 +
4 9 7 Neu_07_APOA2 ++ 1.5 3 8 8 Neu_08_CD74 +++ 3 >3
9 Neu_09_IFIT1 10 Neu_10_SPP1
11 Neu_11_CCL4 1234567891011
Chemokine PBN CD2745,000 bp 3 2 P = 1.8 × 10–3 ALN 1 TAN 0
0 18 24 30 0 18 24 30 PBN–HepG2 PBN–MHCC97H PBN–HCCLM3 PBN–HEK293T PBN
Fig. 3 | Neutrophil heterogeneity and functional validation in humans. non-TAN populations. n = 4. MFI, mean flucorescence intensity. n, Proportions
a, Neutrophil clusters coloured by cluster, tissue source and developmental of IFNγ+CD8+ T cells. n = 4. o, IFNγ expression in CD8+ T cells co-cultured with
order. b, Tissue preference of neutrophil clusters in humans, revealed by different neutrophil–cell line–antibody combinations. n = 3. p, Comparison of
R (ratio of observed cell number to expected cell number). c, Transcription autologous CD8+ T cells co-cultured with matched TANs or non-TANs. n = 4,
o/e
factors inferred by SCENIC. The number of target genes for each transcription including proliferation (CFSE) and functional marker (CD25, IFNγ, GZMB and
factor is indicated in parentheses. d, Expression (exp.) of chemokines and PRF1) expression. IFNγ production was further quantified by ELISA (n = 3).
receptors. e, Expression of signatures and genes in in vitro induced TANs. q, Staining of neutrophils (CD66b) and CD8+ T cells. Representative cells are
f, Normalized ATAC-seq tracks of CCL4. The ATAC peak is denoted with the indicated by arrows, including PD-L1+ CD66b+ cells (white), PD1+ CD8+ T cells
grey line and red shading. g, Quantification of CCL4 production using (cyan), PD-L1−CD66b+ cells (yellow) and PD1− CD8+ T cells (red). Scale bars,
enzyme-linked immunosorbent assay (ELISA). n = 4. h, Chemotaxis abilities of 100 μm (left) and 20 μm (right). The bar plots show the quantification results.
matched TAN or non-TAN populations on autologous monocytes. n = 3. i, CD274 n = 5. In g–q, n denotes biologically independent samples. For k, n, o and q, data
expression. j, CD274 and CEACAM8 expression as described in e. k, PD-L1 are mean ± s.e.m. Statistical analysis was performed using two-sided Student’s
expression in co-cultured PBNs from e examined using FACS. n = 4. l, ATAC-seq t-tests (k and q), one-sided Student’s t-tests (n), two-sided paired t-tests
tracks of CD274 as described in f. m, PD-L1 expression in matched TAN or (g, h, m, o and p) and two-way ANOVA (e and j).
Article
17,780 cells
8
9 1 11 7 6 2
12 10 5 3 4
UMAP 1
Fig. 10l–m). Furthermore, we performed the Ly6G blockade thera- human and mouse APOA2+ TANs exhibited unique lipid metabolism sig-
peutically in pTMC mice with the luciferase reporter (pTMC-Luc) natures similar to hepatic lipid-associated macrophages39,40 and might
(Fig. 4i). Ly6G blockade at 36 days after tumour formation (at 7 days) therefore be lipid-associated neutrophils (Supplementary Note 9).
showed substantial reductions in bioluminescence signal and tumour Taken together, neutrophil depletion can alter the TAN composition
burdens (Fig. 4j). Collectively, neutrophil depletion could attenuate and attenuate tumour progression in mouse models.
macrophage recruitment and T cell suppression, resulting in tumour
inhibition.
Discussion
To further investigate the neutrophil dynamics during the anti-Ly6G
treatment, we performed scRNA-seq of eight samples covering bone On the basis of about 1.3 million cells from human and mouse, our
marrow, peripheral blood, tumour-adjacent liver tissues and tumours large-scale, sorting-free single-cell analyses delineate a comprehen-
from two mice (Supplementary Fig. 4). Although most TANs diminished sive cellular landscape of PLC, enabling us to identify five TIMELASER
after the treatment, mNeu_09_Apoa2 retained and expanded relatively subtypes and decode the neutrophil heterogeneity. The TIMELASER
in the tumour. Correspondingly, its human counterpart, Neu_07_ framework covers most cell populations and provides a non-biased
APOA2, was associated with favourable prognosis. Furthermore, both stratification of baseline TIME subtypes manifesting spatial resolution.
146 | Nature | Vol 612 | 1 December 2022
2 PAMU
a b c mNeu_12_Ccl4 d
1 ++ ± ± hNeu_11_CCL4
hNeu_10_SPP1 2 ++ ± ± mNeu_11_Spp1 hNeu_08_CD74
3 ++ ± ± hNeu_07_APOA2 mNeu_09_Apoa2 4 ++ ± ± mNeu_10_Ifit1 hNeu_09_IFIT1 mNeu_06_Marco 5 ++ ± ± hNeu_05_ELL2 mNeu_07_Actg1
6 ± +++ ± hNeu_06_PTGS2
hNeu_01_MMP8 7 ± ++ ++ mNeu_08_Mmp8 hNeu_03_ISG15
8 ± ± ++ mNeu_04_Ifit3
mNeu_03_Pabpc1
9 ± ± ++ m hN N e e u u _ _ 0 0 4 5 _ _ T G X m N 2 IP a
10 ± ± ++ m m N N eu e _ u 0 _ 1 0 _ 2 N _L g t p f hNeu_02_S100A12 11 ± ± ++ 12 ± ± ++ Z-score PB AL Tumour 0 1 Ro/e ± + +++++ –4 –2 0 2 4 0 11.5 3>3
e i
f g h j
Isotype Anti-Ly6G
1 1 1 A 4 9 9 2 2 2 2 2 2 2 2 5 O R 6 M P N P B R L P B A T F S A N K S L A H M T P R L A C X P R L A M K 0 3 O A M 0 T C D S 1 A A T G B G S C 0 I C 5 C R P L L T L M S C C S 1 C F 3 L I I A P I S H S P S 1 1 1 1 1 1 A A 4 4 4 B 3 3 3 8 9 2 2 2 F X L P P T A M T 7 R S D L P 6 R T L R 1 T B M A L D C D L S B B I O L L L M P C 2 7 A Y F B N T E A I O C A D 2 C C 1 1 P X I C C M S Y C F G S L N A C I D I S L C T C
1 mNeu_01_Ngp 1
2 mNeu_02_Ltf 2 3 mNeu_03_Pabpc1
4 mNeu_04_Ifit3 3 5 mNeu_05_Gm2a 4 6 mNeu_06_Marco 5 7 mNeu_07_Actg1 8 mNeu_08_Mmp8 6
9 mNeu_09_Apoa2 7
10 mNeu_10_Ifit1 8 11 mNeu_11_Spp1 9
12 mNeu_12_Ccl4
10
11
12 AL 0 2.5 5.0 7.5 PBN PB ALN TAN Tumour 0 1 2 3 Cd274
HDTV Analysis Luminescence Alb-Cre/Trp53fl/fl pTMC
–7 d 0 d2 d 33 d
Anti-Ly6G or Isotype (12.5 μg per day) HDTV Anti-Ly6G or Isotype (25 μg per day)
Intraperitoneal injection pTMC-Luc Intraperitoneal injection
oitar
thgiew
ydob
ot
reviL
P = 0.0464 P = 0.0234 P = 0.0251 0.3 2×105 8×104
0.2
0.1 5×104
0 0 0 Isoty A p n e ti-Ly6G
revil
rep
rebmun
eludoN
P = 0.0120 P = 0.0135 200 20
150 15
100 10
50 5 0 0
hgihb11DCwol08/4F
)%(
sllec
P = 0.7402 20
15
10
5 0
1-DP
fo IFM
)%(
sllec
T +3DC+8DC
3MIT
fo
IFM
P = 6.0 × 10–5
6
4
2 0
Isoty A pe nti-Ly6G Isoty A pe nti-Ly6G
)%(
sllec
evitisoP
Ly6G
100 P = 2.0 × 10–7
50 Isotyp A e nti-Ly6G
)%(
sllec
evitisoP
Ki-67
]stinu
ecnaidar[
gol 01
8.0 P = 0.0094 P = 0.2280
7 d 36 d 36 d 7.0
6.0
5.0 Isotyp A e n , t i 7 -L d y a 6 y G s Is , o 7 t y d p a A e y n , s t 3 i- 6 L y d 6 a G y , s 36 days
epytosI
G6yL-itnA
0.3
Radiance 0.2 (p s–1 cm–2 sr–1)
0.1
M M i a n x = = 8 1 .0 × × 10 1 5 03 Isot A y n p t e i- , L 3 y 6 0 6 G da , y 3 s 6 days
ydob
ot
reviL
oitar
thgiew
Predicted order of differentiation
Analysis
0 d 7 d 36 d
P = 0.0292
Fig. 4 | Neutrophil heterogeneity and depletion in mouse models. a, UMAP macrophages (n = 10) and CD8+ T cells (n = 10), and the expression of functional
plots showing the neutrophil clusters (top), tissue sources (bottom left) and markers (PD1 and TIM3; n = 6) in tumours of the anti-Ly6G and isotype groups.
developmental orders (bottom right) in mice. b, The tissue preference of h, The proportions of neutrophils (Ly6G) and proliferating malignant cells
neutrophil clusters in mice revealed by R (ratio of observed cell number to (Ki-67) assessed by IHC (n = 6). i, Schematic of the anti-Ly6G treatment in a
o/e
expected cell number). c, Heat map comparing representative gene expression therapeutic manner. j, Representative images and quantitative results of the
across neutrophil clusters in humans and mice. d, The expression of Cd274 in tumour load examined by luminescence at 7 days and 36 days in i. n = 5.
neutrophil clusters (top) and different tissues (bottom) in mice. e, Schematic of Representative photos of tumours at 36 days are also shown. For f–j, n values
the anti-Ly6G treatment procedure. f, Representative photos of tumours denote biologically independent samples; data are mean ± s.e.m. Statistical
generated in anti-Ly6G and control groups. The ruler tick marks show mm. analysis was performed using two-sided Student’s t-tests (f–i and j (top)) and a
The bar plots (right) show the nodule numbers per liver and the ratio of liver one-sided Student’s t-test (j, bottom).
weight to body weight. n = 15. g, FACS analyses showing the proportions of
We speculate that in-depth analysis of these data, along with functional 17. Ma, L. et al. Single-cell atlas of tumor cell evolution in response to therapy in
studies, will provide new insights for tumour-TIME and TIME-TIME hepatocellular carcinoma and intrahepatic cholangiocarcinoma. J. Hepatol. 75,
1397–1408 (2021).
crosstalk, assist to identify immune cell functions, and guide the 18. Ma, L. et al. Tumor cell biodiversity drives microenvironmental reprogramming in liver
identification of biomarkers or targets for immunotherapies41. The cancer. Cancer Cell 36, 418–430 (2019).
19. Sun, Y. et al. Single-cell landscape of the ecosystem in early-relapse hepatocellular
heterogeneity of neutrophils and their functions in tumorigenesis
carcinoma. Cell 184, 404–421 (2021).
have been under intense investigation6–9. We identified a neutrophil 20. Zheng, C. et al. Landscape of infiltrating t cells in liver cancer revealed by single-cell
spectrum that is broadly conserved between humans and mice, and sequencing. Cell 169, 1342–1356 (2017).
21. Zhang, M. et al. Single-cell transcriptomic architecture and intercellular crosstalk of
clearly show their gene expression, gene signatures and developmen-
human intrahepatic cholangiocarcinoma. J. Hepatol. 73, 1118–1130 (2020).
tal trajectories governed by different sets of transcription factors. 22. Aizarani, N. et al. A human liver cell atlas reveals heterogeneity and epithelial progenitors.
Our investigation shows that TANs exhibit a collective pro-tumour Nature 572, 199–204 (2019).
phenotype, among which we speculate that the pro-tumour CCL4+, 23. Xie, X. et al. Single-cell transcriptome profiling reveals neutrophil heterogeneity in
homeostasis and infection. Nat. Immunol. 21, 1119–1133 (2020).
SPP1+ and PD-L1+ TANs are promising immunotherapy targets, either 24. Zilionis, R. et al. Single-cell transcriptomics of human and mouse lung cancers reveals
alone or in combination with immune checkpoint inhibitors. Further conserved myeloid populations across individuals and species. Immunity 50, 1317–1334
(2019).
exploring the impact of neutrophils on immunotherapies and related
25. Ballesteros, I. et al. Co-option of neutrophil fates by tissue environments. Cell 183,
confounding clinical factors would offer new opportunities to better 1282–1297 (2020).
understand TAN biology and propose translational research paths for 26. Bagaev, A. et al. Conserved pan-cancer microenvironment subtypes predict response to
immunotherapy. Cancer Cell 39, 845–865 (2021).
treating liver cancer.
27. Zhang, L. et al. Single-cell analyses inform mechanisms of myeloid-targeted therapies in
colon cancer. Cell 181, 442–459 (2020).
28. Kiss, M. et al. IL1β promotes immune suppression in the tumor microenvironment
Online content independent of the inflammasome and gasdermin D. Cancer Immunol. Res. 9, 309–323
(2021).
Any methods, additional references, Nature Portfolio reporting summa- 29. Feig, C. et al. Targeting CXCL12 from FAP-expressing carcinoma-associated fibroblasts
ries, source data, extended data, supplementary information, acknowl- synergizes with anti-PD-L1 immunotherapy in pancreatic cancer. Proc. Natl Acad. Sci. USA
110, 20212–20217 (2013).
edgements, peer review information; details of author contributions
30. Cancer Genome Atlas Research Network. Comprehensive and integrative genomic
and competing interests; and statements of data and code availability characterization of hepatocellular carcinoma. Cell 169, 1327–1341 (2017).
are available at https://doi.org/10.1038/s41586-022-05400-x. 31. Farshidfar, F. et al. Integrative genomic analysis of cholangiocarcinoma identifies distinct
IDH-mutant molecular profiles. Cell Rep. 18, 2780–2794 (2017).
32. Xue, R. et al. Genomic and transcriptomic profiling of combined hepatocellular and
intrahepatic cholangiocarcinoma reveals distinct molecular subtypes. Cancer Cell 35,
1. Binnewies, M. et al. Understanding the tumor immune microenvironment (TIME) for 932–947 (2019).
effective therapy. Nat. Med. 24, 541–550 (2018). 33. Wu, R. et al. Comprehensive analysis of spatial architecture in primary liver cancer. Sci.
2. Thorsson, V. et al. The immune landscape of cancer. Immunity 48, 812–830 (2018). Adv. 7, eabg3750 (2021).
3. Li, X. et al. The immunological and metabolic landscape in primary and metastatic liver 34. Xiang, X. et al. IDH mutation subgroup status associates with intratumor heterogeneity
cancer. Nat. Rev. Cancer 21, 541–557 (2021). and the tumor microenvironment in intrahepatic cholangiocarcinoma. Adv. Sci. 8,
4. Marquardt, J. U., Andersen, J. B. & Thorgeirsson, S. S. Functional and genetic e2101230 (2021).
deconstruction of the cellular origin in liver cancer. Nat. Rev. Cancer 15, 653–667 (2015). 35. Wu, S. Z. et al. A single-cell and spatially resolved atlas of human breast cancers. Nat.
5. Finn, R. S. et al. Atezolizumab plus bevacizumab in unresectable hepatocellular Genet. 53, 1334–1347 (2021).
carcinoma. N. Engl. J. Med. 382, 1894–1905 (2020). 36. Ramachandran, P., Matchett, K. P., Dobie, R., Wilson-Kanamori, J. R. & Henderson, N. C.
6. Coffelt, S. B., Wellenstein, M. D. & de Visser, K. E. Neutrophils in cancer: neutral no more. Single-cell technologies in hepatology: new insights into liver biology and disease
Nat. Rev. Cancer 16, 431–446 (2016). pathogenesis. Nat. Rev. Gastroenterol. Hepatol. 17, 457–472 (2020).
7. Jaillon, S. et al. Neutrophil diversity and plasticity in tumour progression and therapy. Nat. 37. Wculek, S. K. & Malanchi, I. Neutrophils support lung colonization of metastasis-initiating
Rev. Cancer 20, 485–503 (2020). breast cancer cells. Nature 528, 413–417 (2015).
8. Shaul, M. E. & Fridlender, Z. G. Tumour-associated neutrophils in patients with cancer. 38. Boivin, G. et al. Durable and controlled depletion of neutrophils in mice. Nat. Commun. 11,
Nat. Rev. Clin. Oncol. 16, 601–620 (2019). 2762 (2020).
9. Ng, L. G., Ostuni, R. & Hidalgo, A. Heterogeneity of neutrophils. Nat. Rev. Immunol. 19, 39. Remmerie, A. et al. Osteopontin expression identifies a subset of recruited macrophages
255–265 (2019). distinct from kupffer cells in the fatty liver. Immunity 53, 641–657 (2020).
10. Quail, D. F. et al. Neutrophil phenotypes and functions in cancer: a consensus statement. 40. Guilliams, M. et al. Spatial proteogenomics reveals distinct and evolutionarily conserved
J. Exp. Med. 219, e20220011 (2022). hepatic macrophage niches. Cell 185, 379–396 (2022).
11. Cui, C. et al. Neutrophil elastase selectively kills cancer cells and attenuates 41. Zhu, A. X. et al. Molecular correlates of clinical response and resistance to atezolizumab
tumorigenesis. Cell 184, 3163–3177 (2021). in combination with bevacizumab in advanced hepatocellular carcinoma. Nat. Med. 28,
12. Ponzetta, A. et al. Neutrophils driving unconventional T cells mediate resistance against 1599–1611 (2022).
murine sarcomas and selected human tumors. Cell 178, 346–360 (2019).
13. Yang, L. et al. DNA of neutrophil extracellular traps promotes cancer metastasis via Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
CCDC25. Nature 583, 133–138 (2020). published maps and institutional affiliations.
14. Szczerba, B. M. et al. Neutrophils escort circulating tumour cells to enable cell cycle
progression. Nature 566, 553–557 (2019). Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this
15. Zhang, Q. et al. Landscape and dynamics of single immune cells in hepatocellular article under a publishing agreement with the author(s) or other rightsholder(s); author self-
carcinoma. Cell 179, 829–845(2019). archiving of the accepted manuscript version of this article is solely governed by the terms of
16. Sharma, A. et al. Onco-fetal reprogramming of endothelial cells drives such publishing agreement and applicable law.
immunosuppressive macrophages in hepatocellular carcinoma. Cell 183, 377–394
(2020). © The Author(s), under exclusive licence to Springer Nature Limited 2022
Nature | Vol 612 | 1 December 2022 | 147
Article
Methods bovine serum (FBS, Gibco) and enzymatically digested using the MACS
tumour dissociation kit (Miltenyi Biotec) for 30 min on a rotor at 37 °C,
Patient sample collection according to the manufacturer’s instructions. After filtering using the
This study was approved by the Research Ethics Committee of both 70 μm CellStrainer (BD) in RPMI-1640 medium, the suspended cells
Peking University First Hospital and Peking University People’s were centrifuged at 400g for 5 min. After removing the supernatant,
Hospital. Written informed consent was obtained from each patient. cell pellets were resuspended in sorting buffer (PBS supplemented
We performed a prospective screen of treatment-naive patients with with 2% FBS) after washing twice with PBS. Moreover, 10 ml of fresh PB
liver cancer who underwent primary curative resection from March samples were collected before surgery in EDTA anticoagulant tubes.
2019 to January 2020 at Peking University People’s Hospital. Fresh For PB samples, RBC removal was performed using the ErythroClear
tumour and tumour-adjacent liver tissue (AL) samples (at least 2 cm kit (STEMCELL) according to the manufacturer’s instructions. After
from tumour tissues) were collected within 30 min after the opera- collecting single-cell suspensions for different samples, 10 μl of each
tion. Peripheral blood (PB) samples were collected before the surgery. cell suspension was counted using an automated cell counter (Luna-II,
A total of 124 patients were enrolled and 160 samples were obtained for Logos Biosystems) to assess the number of live cells. Throughout the
scRNA-seq, including 79 HCC, 25 ICC, 7 CHC, 2 hepatic haemangioma dissociation procedure, cells were maintained on ice whenever pos-
(HH), 1 adenosquamous carcinoma (ASC), 1 sarcomatoid carcinoma sible. The entire procedure was completed in less than 1 h (typically
(SAR) and 9 secondary liver cancer (SLC, liver metastases from various ~45 min) to avoid dissociation-associated artifacts. Cell viability and
primary sites) cases. Focusing on PLC, proportions of HCC, ICC and concentration were then assessed using the Rigel S3 fluorescence cell
CHC patients were 69.9%, 22.1% and 6.2%, respectively, consistent with analyser (Countstar).
the PLC incidence worldwide. For 14 of 124 patients, AL and PB were To avoid biases introduced by any enrichment steps on the cellular
collected in addition to tumours. We also performed whole-exome composition of queried samples, the original unsorted single-cell sus-
sequencing (WES) for 84 of these patients. No blinding or randomiza- pensions were directly used for subsequent library construction. Cells
tion was performed for the human tumor samples, because this was an were loaded onto the Chromium single cell controller (10x Genomics)
observational study. Detailed clinical characteristics and mutational to generate single-cell gel beads in the emulsion according to the manu-
profiles are summarized in Supplementary Tables 1 and 2, respectively. facturer’s protocol. scRNA-seq libraries were constructed using Single
Cell 3′ Library and Gel Bead Kit v3.1 and sequenced using the NovaSeq
Mouse models 6000 sequencer (Illumina).
Trp53fl/fl and Alb-cre mice (both C57BL/6) were purchased from the
Jackson Laboratory and bred in a pathogen-free environment accord- scRNA-seq data processing
ing to the guidelines of the animal facility in Peking University First scRNA-seq data were aligned and quantified using the CellRanger
Hospital. Trp53fl/fl mice were crossed with Alb-cre mice to generate toolkit v.3.1 against the reference genome GRCh38 and GRCm39 for
the liver conditional Trp53-knockout (Trp53 cKO) mice. 7-week-old human and mouse samples, respectively. Empty droplets were filtered
male Trp53 cKO mice were used for subsequent experiments. Sleep- using the emptyDrops function of the R package dropletUtils v.1.10.3
ing beauty transposase (SB100) and transposon pT3-Neo-EF1a-GFP by assessing whether the RNA content associated with a cell barcode is
plasmids were purchased from Addgene. cDNA of mouse Myc gene was significantly distinct from the ambient background RNA present within
cloned into the transposon vector through the MluI and SpeI restriction each sample. Cells with FDR < 0.01 (Benjamini–Hochberg-corrected)
enzyme sites, obtaining the pT3-Neo-EF1a-Myc plasmid. Next, mutated were selected for further analysis. The quality of cells was assessed
forms of mouse Ctnnb1 (∆90Ctnnb1) or mouse Kras (KrasG12D) were based on three metrics: (1) the number of total UMI count per cell
generated by PCR cloning of mouse Ctnnb1 or Kras cDNA. Then, the (library size) was below 30,000; (2) the number of detected genes
Myc and ∆90Ctnnb1 transposon plasmid (pT3-EF1a-Myc-∆90Ctnnb1, was above 500 and below 6,000; (3) the percentage of mitochondrial
pTMC) was generated through the AscI and NotI restriction sites. Simi- genes was below 50. As neutrophils showed very low transcript counts
larly, the Myc and KrasG12D transposon plasmid (pT3-EF1a-Myc-KrasG12D, as reported24, the range of detected gene number of neutrophils was
pTMK) was generated. For construction of the pTMC-luciferase plasmid set as 100–6,000. Next, we used a cluster-level approach to remove
(pTMC-Luc), the luciferase fragment was linked to Myc by P2A using potential doublet cells. In brief, the doublet score was calculated for
In-Fusion cloning. Plasmids for hydrodynamic tail-vein (HDTV) injection each cell using doubletCells function of the scran R package v.1.18.7.
were prepared using the EndoFree-Maxi Kit (Qiagen). For HDTV, a total Cell clusters in each sample were identified by examining the top 50
of 30 μg DNA mixture (5:1 ratio of transposon to transposase-encoding principal components (PCs) across highly variable genes (HVGs),
plasmid) was suspended in 0.9% saline solution at a final volume equal building neighbour graph by buildSNNGraph function, and then clus-
to 10% of body weight of the mice, and was then injected into 7-week-old tering using the cluster_louvain function from the igraph R package
male Trp53-cKO mice through the tail vein within 5–7 s (ref. 42). All of the v.1.2.9. The median doublet score of each cell cluster was calculated
mice were housed in pathogen-free conditions at an ambient tempera- using median-centred MAD-variance normal distribution. Clusters
ture 20–26 °C and humidity of 30–70% with a 12 h–12 h light–dark cycle with a median score above the extreme top end of this distribution
before use. The body weight of mice was monitored twice every week (Benjamini–Hochberg-corrected P < 0.1) were considered as doublets.
for signs of dynamic tumour growth. The diameter of single tumour After quality control, a total of 1,297,609 cells comprising 1,092,172
was <2 cm. For cKO mouse models, body-weight-matched mice were cells from 160 human samples (124 patients) and 205,437 cells from
randomized over the treatment groups, anti-Ly6G and isotype control. 29 mouse samples (8 mice) were retained for downstream analysis.
For pTMC-Luc mouse model, tumor size was monitored by lumines- Raw counts and log (normalized counts) were computed for each cell.
2
cence signals at day 7 after HDTVi, and tumor-size-matched mice were As immune and stromal cells from different patients mixed well, we
randomized over the treatment groups, anti-Ly6G and isotype con- did not observe obvious batch effect. Gene–cell count matrices from
trol. No blinding was performed for mouse samples, because this was an different samples were merged using Seurat (v.3.2.3)43.
observational study. All of the mouse experiments were approved by
the Animal Care and Use Committee at Peking University First Hospital. Cell clustering and annotation
To identify major cell types, we used scanpy (v.1.6) Python package44.
scRNA-seq analysis of human and mouse samples A total of 2,000 HVGs were selected using the highly_variable_genes
Fresh tumour and AL samples were cut into approximately 1 mm3 function, and then the top 50 PCs were calculated using the pca func-
pieces in RPMI-1640 medium (Thermo Fisher Scientific) with 10% fetal tion. We regressed out the effect of percentage of mitochondrial genes
and scaled each gene to unit variance. Nearest neighbourhood graphs processing time may cause the failure of neutrophil capture. For data
were built using the neighbours function, and the community algorithm analysis, we set the range of detected UMI as 100–6,000 for neutro-
was applied for clustering using the louvain function (resolution = 1). phils, while keeping that of other cell populations as 500–6,000 for
The dimensionality of each dataset was reduced using UMAP. downstream analysis. A total of 34,307 neutrophils were identified on
We first annotated the 14 major cells types identified in our dataset the basis of the expression of CSF3R, S100A8 and S100A923,24. Eleven
on the basis of well-known marker genes, including CD3D, CD8A, CD4, subsets of human neutrophils were characterized (Fig. 3a and Extended
FOXP3, TRDC, NKG7, CD79A and MS4A1 for lymphoid lineage (CD8+ T, Data Fig. 7b–d) and exhibited clear separation according to the tissue
conventional CD4+ T, T regulatory, γδT, natural killer and B cells); sources of PB, AL and tumour (Fig. 3a,b and Extended Data Fig. 7e),
CD14, CD16, CD68, CD163, CD1C, LAMP3, TPSAB1, CSF3R and S100A8 for consistent with the previous notion that neutrophils exhibited tissue
myeloid lineage (monocytes, macrophages, dendritic cells, mast cells specificity6–9. SingleR (v.1.10.0)47 was also used to assess the similarity
and neutrophils); VWF and COL1A1 for stromal cells (endothelial cells of neutrophil clusters in this study compared to previously reported
and fibroblasts); and ALB and EPCAM for epithelial cells. Epithelial neutrophil subsets. Neu_02_S100A12, Neu_03_ISG15 and Neu_04_TXNIP
cells, composed of hepatocytes, cholangiocytes and progenitor cells, were mainly composed of PBNs, matching the reported circulating
were analysed as a whole in cluster analysis. Among these epithelial G5a, G5b and G5c states23,24 (Extended Data Fig. 7f). Neu_05_ELL2 and
cells, malignant cells were further distinguished from non-malignant Neu_06_PTGS2 were mainly ALNs. All of the other six subsets (Neu_01_
cells by inferring large-scale copy-number variations (CNVs) of each cell MMP8, Neu_07_APOA2, Neu_08_CD74, Neu_09_IFIT1, Neu_10_SPP1 and
using inferCNV (v.1.3.3) R package as described45. As non-malignant Neu_11_CCL4) were enriched in tumours and therefore designated as
cells derived from ALs were annotated, we used the average patterns TANs. These TANs were differentially enriched across PLC subtypes,
of these cells as a reference for the CNV estimation. with Neu_01_MMP8 and Neu_07_APOA2 in HCC, and Neu_09_IFIT1,
Next, we performed a second round of clustering to further charac- Neu_10_SPP1 and Neu_11_CCL4 in ICC (Fig. 3b).
terize subpopulations of major cell types in the TIME. We converted
the scanpy object to Seurat object using the anadata Python package Calculation of gene signature scores based on scRNA-seq data
(v.0.7.5) and then clustering using Seurat (v.3.2.3)43. To avoid unex- Multiple gene signature scores were calculated on the basis of the
pected noise and expression artefacts by dissociation, a total of 1,514 scRNA-seq data. For each gene signature, individual cells were scored
genes associated with mitochondria (50 genes), heat-shock protein using the AddModuleScore function, which calculated the average
(178 genes), ribosome (1,253 genes) and dissociation (33 genes) were expression levels of selected genes at the single-cell level and sub-
excluded (Supplementary Table 1). Owing to variable amount and tracted by the aggregated expression of control feature sets. Control
property of cells in each major cell type, different parameters for features were composed of 100 randomly selected genes from each
clustering were used. For the clustering of T cells, top 20 PCs were bin where all features were binned into 24 groups based on averaged
selected on the basis of 2,000 HVGs (resolution = 1). For the clustering expression. For malignant cells, hepatic score was calculated based
of natural killer or B cells, the top 10 PCs were selected on the basis of on the expression of 21 hepatocyte-related genes18 (ADH1A, ADH4,
1,000 HVGs (resolution = 0.6). For monocytes or dendritic cells, the top AFM, AHSG, AMBP, C4BPB, C6, CYP2E1, CYP4F2, F9, FGA, FGB, FGG,
10 PCs were selected on the basis of 1,000 HVGs (resolution = 0.8). For GC, HPX, PROC, SAA4, SERPINA6, SERPINC1, SERPIND1 and SLC2A2).
macrophages, the top 10 PCs were selected on the basis of 1,500 HVGs Biliary epithelial score was calculated based on the expression of 13
(resolution = 1). For endothelial cells or fibroblasts, the top 15 PCs were cholangiocyte-related genes (KRT14, KRT17, KRT6A, KRT5, KRT19,
selected on the basis of 1,000 HVGs (resolution = 1). For neutrophils, KRT8, KRT16, KRT6B, KRT15, KRT6C, KRTCAP3, SFN and EPCAM). For
the top 8 PCs were selected on the basis of 500 HVGs (resolution = 0.8). neutrophils, scores for azurophil granule, specific granule, gelatinase
Specifically, the resolution of neutrophil clusters was determined on granule, secretory vesicle, neutrophil maturation and neutrophil age-
the basis of its biological features. Here we took a scRNA-seq dataset ing were calculated23 (Supplementary Table 3). Other functional signa-
of neutrophils from PB as a reference23. The reported three neutrophil tures for neutrophil activation (GO:0042119), neutrophil chemotaxis
subsets (G5a–c) in PB were recapitulated with resolutions of 0.7 and (GO:0030593), apoptosis (GO:0043065), angiogenesis (GO:0001525),
0.8, with the latter having a better separation of neutrophil clusters. extracellular matrix (GO:0031012), phagocytosis (GO:0006911), type
As a result, we identified 13 CD8+ T, 8 conventional CD4+ T, 3 T regula- I interferon signalling pathway (GO:0060337) and chemokine activity
tory, 4 γδ T, 7 natural killer and 4 B cell clusters for the lymphoid lineage, (GO:008009) were derived from the Gene Ontology database.
5 monocyte, 9 macrophage, 7 DC, 1 mast cell and 11 neutrophil clusters
for the myeloid lineage, and 10 endothelial cell and 7 mesenchymal Tissue and cancer type enrichment of clusters
clusters35,46 for the stromal components. To facilitate data visualization To quantify the enrichment of cell clusters across tissues (PB, AL and
in Fig. 1c, cells were reclustered into four embeddings using Seurat, tumour) and PLC subtypes (HCC, ICC and CHC), we compared the
including (1) T cells, (2) natural killer and B cells, (3) myeloid cells and observed and expected cell numbers in each cluster by computing
(4) endothelial cells and mesenchymal cells. Next, we used the Find- the R value using the epitools (v.0.5-10.1) R package according to
o/e
Markers or FindAllMarkers function to identify differentially expressed the following formula15:
genes (DEGs) with adjusted P < 0.05 using Bonferroni correction. Gene
Observed
Ontology analysis was performed using the clusterProfiler R package R = ,
(v.3.18.1). o/e Expected
Experimental and analytical strategies for neutrophils where the expected cell numbers for each combination of cell clusters
As neutrophils are very fragile and have a relatively low level of RNA con- and tissues were obtained from the χ2 test. We assumed that one cluster
tent, both experimental and analytical procedures were improved to was enriched in a specific tissue or cancer type if R > 1.
o/e
capture neutrophils during this study. For scRNA-seq experiments, we
kept a minimal hands-on time for the tissue samples. When single-cell Identification of cellular modules and TIMELASER subtypes
suspensions were collected, only the MACS Dead Cell Removal Kit To examine the potential cellular compositions of different TIME eco-
(Miltenyi Biotec) was used to collect viable cells and no FACS enrich- systems in liver cancer, we investigated the co-existence patterns of
ment steps were applied, therefore limiting the experimental process different TIME cell subpopulations. Pairwise correlation values between
from tissue collection (for both tumour and adjacent liver tissues) after the normalized frequency of any two clusters across different tumour
surgery to PCR with reverse transcription within 2 h. Prolonging the samples were calculated using the corr.test function. These values were
Article
then clustered using the pheatmap (v.1.0.12) R package with the ward. Catalog of Somatic Mutations in Cancer (COSMIC) database. Finally,
D2 cluster method and correlation distance. To avoid potential distor- point mutations identified by Mutect2 and indels identified by both
tion of clustering due to the low frequency of certain clusters (present Mutect2 and VarScan were retained after filtering. All of the variants
in less than 10 tumours), tumour cells fall into 13 PB-enriched clusters were annotated using the VEP (v.96; Ensembl Variant Effect Predictor).
(CD4T_01_CCR7, CD4T_09_FOXP3, CD8T_01_CCR7, CD8T_02_CX3CR1, Tumour ploidy and cellularity were inferred using ABSOLUTE (v.1.0.6).
CD8T_03_GZMK_S1PR1, γδT_01_GNLY_S1PR5, NK_01_FCGR3A_CX3CR1, CNVkit (v.0.9.7) was then performed using the default parameters
MonoDC, Mo_01_CD14, Mo_02_CD16, Neu_02_S100A12, Neu_03_ISG15 on paired tumour–normal WES data. After segmentation, GISTIC2
and Neu_04_TXNIP) and 2 additional clusters (Neu_01_MMP8 and Fb_06_ (v.2.0.23; Genomic Identification of Significant Targets in Cancer) was
FABP3) were excluded from this analysis. As a result, we identified five applied to identify focal CNVs.
highly correlated cellular modules. For each patient, cluster-normalized
frequencies of clusters from the same cellular module were summed Gene modules of malignant cells
and the most abundant cellular module was designated as the dominant Gene modules of malignant cells were extracted as described previ-
cellular module for this patient. Each cellular module corresponds to ously35. For each individual tumour with more than 50 malignant cells,
a TIMELASER subtype, of which the phenotype was designated based clusters were calculated using Seurat (v.3.2.3) at five resolutions (0.5,
on four aspects: (1) cell populations, (2) marker genes, (3) TIME-related 0.8, 1, 1.2, 1.5). For each cluster, the top 200 DEGs were identified and
gene signatures as previously defined26 and (4) prognostic relevance, only clusters with more than five tumour cells and more than five DEGs
which combinatorically support the phenotype of our TIME subtypes were retained. The DEGs of these clusters were then defined as a gene
(Extended Data Fig. 5e,f and Supplementary Table 3). signature. The redundancy of gene signatures identified from the five
resolutions was reduced by a pairwise comparison of gene signatures
Classification of TIMELASER subtypes for bulk RNA-seq data within each sample. For each pair with a Jaccard index > 0.75, the gene
To apply our single-cell based TIMELASER subtypes to published bulk signature with fewer genes was removed. Across all tumours, 1,187 gene
RNA-seq data, we defined gene signatures for each subtype by com- signatures were identified. Consensus clustering of the Jaccard simi-
bining top 8 DEGs of all clusters in the corresponding cellular module larities between these gene signatures identified eight gene modules.
(Supplementary Table 3). For each patient, z-scores of 5 TIMELASER Highly recurrent genes were identified for each gene module and the
signatures were computed. First, TIMELASER signature scores were enriched pathways were calculated using ClusterProfiler (v.3.18.1).
calculated on the basis of the average expression of signature genes,
and then subtracted by the aggregated expression of control features. Cell–cell interactions
Control features were composed of 100 randomly selected genes from To investigate cell–cell interactions among clusters from each cel-
each bin where all features were binned to 24 groups based on averaged lular module, we analysed the L–R pairs using CellphoneDB (v.2.1.7)
expression. Next, z-scores of five TIMELASER signatures were calculated as described previously48. In brief, a log-normalized count matrix
2
by scaling five scores in the same sample. The TIMELASER subtype of was subsampled into 500 cells per cluster. Significant L–R pairs were
each patient was then determined on the basis of the highest signature identified after filtering for frequencies below 0.1% or above 2% of all
score across five z-scores. For example, we assembled a bulk RNA-seq cluster–cluster combinations. For each L–R pair, the total number of
dataset of 453 patients with PLC collected from three published studies, this L–R pair across clusters from the same cellular module was counted.
including TCGA-LIHC (HCC study of TCGA)30, TCGA-CHOL (ICC study of Cellular-module-specific L–R pairs were then determined based on the
TCGA)31 and our previous study of CHC32. Classification of TIMELASER enrichment score by R values (R > 3). To identify potential ligands
o/e o/e
subtypes was performed for this large cohort dataset. that drive the unique phenotype of Neu_09_IFIT1, we compared the
To compare our single-cell-based TIMELASER subtypes with the bulk transcriptomic differences between Neu_03_ISG15 and Neu_09_IFIT1,
RNA-seq data based molecular functional portrait subtypes26, we calcu- and then used the highly expressed genes in Neu_09_IFIT1 for NicheNet
lated the expression levels of molecular functional portrait signatures (v.1.1.0) analysis. Genes with log[fold change] > 0.2 and adjusted
2
for each individual in our dataset (Supplementary Table 3). We first P < 0.05 were then used as gene sets of interest. Genes were consid-
calculated the average expression of a certain gene across TIME cells ered to be expressed when they had non-zero values in at least 10% of
in each patient using the AverageExpression function. The signature the cells in a cell type.
scores were then calculated by the mean expression of involved genes.
Developmental trajectory
WES CytoTRACE (v.0.3.3)49, Monocle (v.2.12)50, and CellRank (v.1.5.1)51 were
DNA was extracted using the DNeasy Blood & Tissue Kit (Qiagen) from adopted to infer the developmental trajectory of human and mouse
fresh-frozen tumour and AL samples. A total of 200 ng to 1 μg DNA was neutrophils. CytoTRACE is based on the notion that transcriptional
taken from each sample and sheared into fragments of ~300 bp using a diversity, that is, the number of genes expressed in a cell decreases
Covaris S2 ultrasonicator. The library was constructed using the NEB- during differentiation. The log-normalized expression matrix was
2
Next Ultra DNA Library Prep Kit for Illumina and exome regions were accessed. The predicted orders were projected onto the neutrophil
captured using Agilent SureSelect All Exon V6. The post-hybridization UMAP space. For Monocle 2, we built a new CellDataSet object from
amplification product was quality-checked and sequenced. Paired-end cluster-annotated Seurat object using the newCellDataSet function.
Illumina reads were aligned to the human genome hg38 (UCSC) using We used the differentialGeneTest function to derive DEGs from each
BWA-mem2 (v.2.0pre1) with the default parameters. SAM files were then cluster, and genes with q < 1 × 10−5 were used to order the cells in pseu-
converted to BAM files and sorted by chromosomal coordinates using dotime. Dimension reduction was performed using the DDRTree algo-
Samtools (v.1.10). The Genome Analysis Toolkit (GATK, v.4.1.7.0) was rithm and then cells were ordered along the trajectory. Moreover, the
used to remove PCR duplicates and recalibrate the base quality score. CytoTRACE scores were also projected on the Monocle trajectory.
Point mutations and indels were identified using Mutect2 (v.4.1.0.0) and CellRank was performed to map the cell fate of neutrophil subsets
VarScan (v.2.4.2). All variants were annotated using ANNOVAR. A series after anti-Ly6G treatment as described.
of filtering criteria were applied to the variant candidates: (1) at least 10×
coverage was required in the normal sample of each patient bearing at Regulon network
most 1× mutation coverage; (2) at least 10× total coverage was required The regulon network was explored using the R package SCENIC
in tumour samples with at least 3× mutation coverage; (3) variations (v.1.1.3)52, which analysed the co-expression of transcriptional factors
listed in dbSNP 150 were removed unless they were documented in the and their putative target genes. We built and scored gene regulatory
network using the default parameters. Raw count matrix was used coverslips were washed for 4 min by staining buffer and fixed in wells
to build co-expression network using the runCorrelation and runG- containing 1.6% paraformaldehyde for 10 min, followed by three washes
ENIE3 functions. Potential regulons based on DNA-motif analysis were in PBS. The coverslips were then incubated in 100% methanol on ice
selected by RcisTarget and active gene networks were identified by for 5 min, followed by three washes in PBS. Fresh fixative solution was
AUCell. Regulon activity for each cell was calculated as the average prepared immediately before final fixation, and final fixation was per-
normalized expression of putative target genes. formed at room temperature for 20 min, followed by three washes in
PBS. Next, the CODEX reporter plate containing the reporter master
Cross-species data integration mix for every cycle was prepared accordingly. The CODEX multicycle
Cross-species single-cell data integration was performed using the reaction and image acquisition were performed using the Akoya CODEX
LIGER v.1.0 workflow53. In brief, single-cell datasets of mouse and human instrument. During imaging, the tissue was kept in H2 buffer. Hybridiza-
neutrophils were preprocessed to produce a raw digital gene expression tion of the fluorescent oligonucleotides was performed in rendering
matrix using createLiger and then normalized. Variable genes were buffer. After imaging, fluorescent oligonucleotides were removed using
selected and the gene expression was scaled using scaleNotCenter. stripping buffer. Data processing and analysis were performed using
Shared and species-specific factors were identified through integrative CODEX analysis manager and CODEX Multiplex Analysis Manager.
non-negative matrix factorization using optimizeALS. Joint clustering
of cells was performed by louvainCluster and then visualized using Isolation of immune cells from PB
UMAP. PB samples (20 ml) were collected from healthy human donors or
patients with liver cancer. Density gradient separation was performed
Survival analysis with Lymphoprep (STEMCELL, 07861). The layer of peripheral blood
Prognostic values of cell clusters and cellular modules were evalu- mononuclear cells was sent for isolation of CD8+ T cells with anti-CD8
ated in our cohort. Kaplan–Meier survival curves were plotted using magnetic beads (STEMCELL, 17853), followed by isolation of monocytes
ggsurvplot function in the R package Survminer v.0.4.9. with anti-CD14 magnetic beads (STEMCELL, 19359). The bottom layer
of erythrocyte/granulocyte pellet was resuspended with Red Cell Lysis
IHC and mIHC Buffer (TIANGEN). Lysis was stopped using RPMI-1640 medium sup-
Formalin-fixed and paraffin-embedded (FFPE) tissues sectioned to plemented with 2% FBS, followed by centrifugation at 400g for 10 min.
4 μm were used for histology evaluation of liver tumours in both Cells were washed twice with PBS and filtered through a 70 μm nylon
human and mouse models. Haematoxylin and eosin (H&E) staining mesh (FALCON).
was performed for each sample. For IHC and mIHC, tissue slides were
deparaffinized with xylene and rehydrated through a graded series of Isolation of neutrophils
ethanol solutions (100%, 95% and 70%). Then, slides were treated by Neutrophils were isolated from PB, AL and tumours from selected
microwave to induce antigen retrieval using citric acid solution for patients. For PB, neutrophils were extracted from the lower layer of
15 min. For mouse tumours, primary antibodies for anti-hepatocyte the erythrocyte/granulocyte pellet after red blood cells were removed
(1:500, ab75677, Abcam), anti-EPCAM (1:200, ab213500, Abcam), using the ErythroClear kit (STEMCELL). Cells were washed twice with
anti-Ly6G (1:500, GB11229, Servicebio), anti-Ki-67 (1:500, ab15580, PBS and filtered through a 70 μm nylon mesh (Falcon). Anti-CD66b
Abcam) and anti-CD68 (1:200, GB113109, Servicebio) were used. Each antibodies (BD, 561650) coupled with magnetic anti-PE microbeads
section was evaluated by 2–3 experienced pathologists. For mIHC analy- (STEMCELL, 17694) were used to purify neutrophils. For AL and
sis of human samples, three panels of primary antibodies were used, tumours, single-cell suspensions of tissues were collected as descried
including, (1) CD66b (1:1,000, GTX19779, GeneTex) and CCL4 (1:800, for scRNA-seq, centrifuged at 300g for 5 min and resuspended in 36%
ab235961, Abcam); (2) Von (1:100, ab9378, Abcam), α-SMA (1:5,000, Percoll (Sigma, P4937, diluted with PBS), followed by centrifugation at
ab7817, Abcam), CD8 (1:100, ZA0508, ZSGB), GZMK (1:1,000, ab282703, 500g for 15 min. Cell pellets were collected and washed twice with PBS.
Abcam); (3) CD8 (1:100, ZA0508, ZSGB), PD1 (1:50, ZM0381, ZSGB), Anti-CD66b antibodies (BD, 561650) coupled with magnetic anti-PE
CD66b (as in panel 1) and PD-L1 (1:1,000, ab237726, Abcam). The slides microbeads (STEMCELL, 17694) were further used to purify neutro-
were then incubated with secondary antibodies (1:1,100 μl for each phils. For survival analysis, PBNs were cultured for 4 days and tested for
slide; HRP-anti-rabbit IgG, ZSGB, PV-6001; or HRP-anti-mouse IgG, viability at multiple time points using the Cell Counting Kit-8 (Bestbio).
ZSGB, PV-6002) for 10 min at room temperature. After each cycle of A total of 24.97% and 4.99% of PBNs remained alive after 1 and 3 days,
staining, heat-induced epitope retrieval was performed to remove all consistent with the lifespan of cultured human neutrophils55.
the antibodies including primary antibodies and secondary antibod-
ies. Multiplex immunofluorescence staining was performed using the Co-culture of PBNs with cell lines
AlphaTSA Multiplex IHC Kit (AXT36100031, AlphaX). The samples The human embryonic kidney cell line (HEK293T, ATCC number, CRL-
were counterstained for nuclei with DAPI for 10 min and mounted in 3216) and the liver cancer cell line (HepG2, ATCC number, HB-8065) were
mounting medium. Multispectral images were scanned with ZEISS obtained from American Type Culture Collection (ATCC). Human liver
AXIOSCAN 7. Cells of interest were quantified using Halo (v.3.4; Indica cancer cell lines (HCCLM3 and MHCC97H) were obtained from the Liver
Labs) or QuPath (v.0.2.0). Cancer Institute, Zhongshan Hospital, Fudan University (Shanghai,
China). All cell lines used in this study were authenticated by apply-
CODEX ing short tandem-repeat (STR) DNA profiling and tested negative for
CODEX was performed on FFPE tissues according to the manufacturer’s mycoplasma. All cells were cultured in RPMI1640 medium (Corning)
instructions (Akoya Biosciences)54. In brief, 4 μm tissue sections were supplemented with 10% fetal bovine serum (FBS) (VISTECH), 100 U ml−1
mounted on poly-l-Lysine-coated coverslips and then deparaffinized of penicillin and 100 μg ml−1 of streptomycin (Hyclone) in a humidified
and rehydrated. The tissue-retrieval process is the same as for IHC. incubator at 37 °C with 5% CO. PBNs (1 × 106) were placed in the top
2
Tissues were then fixed using prestaining fixing solution and then insert of a Transwell (0.4 μm, Corning) and tumour cells were placed
washed using tissue hydration buffer. For each coverslip, the antibody in the bottom chamber of a 12-well plate and co-cultured for 0 h, 6 h,
cocktail (containing β-catenin, CD3e, CD4, CD8, CD11c, CD20, CD31, 12 h, 18 h, 24 h and 30 h. After co-culture, PBNs were sent for qPCR,
CD45RO, CD68, E-cadherin, HLA-DR, keratin14, Ki-67, MAC2/galectin-3 bulk RNA-seq and FACS analysis, including staining with anti-CD45
and pan-cytokeratin) was then added to the coverslip and staining (BD, 557833), anti-CD66b (BD, 561650) and anti-PD-L1 (BD, 557924)
was performed in a sealed humidity chamber for 3 h. After staining, antibodies.
Article
using RSEM (v.1.3.1) and DEGs were analysed using the DESeq2 (v.1.24)
Co-culture of neutrophils with CD8+ T cells R package.
For the co-culture experiment involving PBNs, cell lines and CD8+ T
cells, CD8+ T cells and PBNs were isolated from the same donor at dif- ATAC-seq
ferent time points. At day 1, CD8+ T cells were purified and then stimu- Fresh neutrophils (1 × 104–5 × 104 cells) isolated from different tis-
lated with 25 μg ml−1 CD3/CD28 T Cell Activator (STEMCELL, 10971) and sues of patients with liver cancer were immediately sent for bulk
50 U ml−1 rhIL-2 (STEMCELL, 78036.1) for 3 days. At day 3, PBNs from the ATAC-seq using the TruePrep DNA Library Prep Kit V2 for Illumina
same donor were isolated and placed in the lower chamber of a 12-well (Vazyme, TD501). Raw sequencing reads were trimmed using trimmo-
plate. Tumour cells were placed in the top insert of Transwell (0.4 μm, matic (v.0.39) and then mapped to the GRCh38 human genome using
Corning). After co-culture of PBNs with cell lines for 12 h, CD8+ T cells Bowtie2 (v.2.4.4). PCR duplicates were removed using MarkDupli-
were added to the bottom chamber at a 1:5 ratio of CD8+ T cells to PBNs cates from PicardTools (v.2.23.3). Peaks were called with MACS3
and co-cultured for 24 h and 48 h. (v.3.0.0a7) and peaks that were found in at least two biological rep-
For the co-culture experiment involving PBNs, ALNs and TANs with licates were retained and merged for further analysis. Significantly
CD8+ T cells, PBNs were extracted as described above, whereas ALNs and differentially accessible peaks were identified with adjusted P < 0.05,
TANs were purified from single-cell suspensions of tumour and adjacent and fold change > 1.5 by DESeq2 (v.1.24). Normalized BigWig files
liver tissues with anti-CD66b antibodies coupled with magnetic anti-PE were generated by DeepTools (v.3.5.1) and merged for visualization
microbeads from the EasySep PE Selection Kit (STEMCELL). Purified by pyGenomeTracks (v.3.6).
PBNs, ALNs and TANs were directly co-cultured with CD8+ T cells in a
12-well plate at a 1:2.5 ratio of CD8+ T cells to PBNs for 24 h. In vivo neutrophil depletion
After the co-culture, these mixed cells were separated by a BD FAC- The anti-Ly6G antibody (1A8, Bio X Cell) or IgG2a Isotype control (2A3,
SAria SORP flow cytometer using FACSDiva (v.8.0.1), and the data were Bio X Cell) at a dose of 12.5 μg per 100 μl PBS was administered daily
analysed using FlowJo (v.10.4). Antibodies against CD45 (BD, 557833), through intraperitoneal injection, starting 7 days before HDTV injection
CD3 (BD, 562426), CD8 (BD, 560179) and CD11b (BioLegend, 101256) of the pTMC plasmid. After 33 days, mice were euthanized by carbon
were used to gate CD8+ T cells and neutrophils. PD-L1 antibodies (BD, dioxide asphyxiation and the liver tumours were carefully separated
557924) were used to assess the immunosuppression of neutrophils. from mice. The number of liver tumour nodules was quantified and
IFNγ (BD, 557643), GZMB (BD, 561142) and PRF1 (BD, 563762) antibodies the ratio of liver weight to body weight was calculated.
were used to assess the cytotoxicity of CD8+ T cells. CD69 (BD, 562884) To deplete the neutrophils in a therapeutic manner, the pTMC-Luc
and CD25 (BD, 563701) antibodies were used to assess the activation mouse model was used. Mice were given fresh prepared d-luciferin
status of CD8+ T cells. CFSE (BD, 565082) was used to assess the prolif- (150 μg per g) intraperitoneally and incubated for 5 min and imaged
eration of CD8+ T cells. For PD-L1 neutralization, anti-PD-L1 (BE0285, using in vivo imaging system. In vivo luciferase bioluminescence sig-
Bio X cell) and the control IgG (BE0086, Bio X cell) were used in the nal was detected for an exposure time of 60 s using the Living Image
co-culture experiments. software. At day 7 after the pTMC-Luc HDTV injection, the tumour can
be visually detected by the bioluminescence signal, then the anti-Ly6G
Chemotaxis antibody (1A8, Bio X Cell, BE0075-1) or IgG2a (2A3, Bio X Cell, BE0089)
PBNs, ALNs or TANs (5 × 105) were suspended in RPMI1640 medium isotype control was injected into mice at a dose of 25 μg per 100 μl PBS
and placed in the bottom chamber of a 12-well plate. Purified CD14+ on a daily basis. At day 36, the bioluminescence signal was detected,
monocytes (2 × 105) were placed in the top insert of a Transwell (5 μm, and mice were euthanized. The ratio of liver weight to body weight
Corning) and incubated in macrophage differentiation medium with was calculated. FACS analysis was performed using the following anti-
100 ng ml−1 M-CSF (STEMCELL, 78059). After co-culture of PBNs with bodies, CD45 (BioLegend, 103116), CD3ε (BioLegend, 100353), CD8a
monocytes for 48 h, monocytes that migrated and attached to the (BD, 552877), CD11b (BioLegend, 101242), Ly6G (surface, BioLegend,
low surface of the Transwell membrane were fixed with 4% paraform- 127618; intracellular, BD, 551461), F4/80 (BioLegend, 123133) to gate
aldyhyde, and stained with 1% crystal violet. The number of migrated CD8+ T cells, neutrophils and macrophages, respectively. Data were
monocytes was calculated using Image J (v.1.52k). analysed using FlowJo (v.10.4) and the gating strategies are shown in
Supplementary Fig. 5. PD-L1 antibody (BD, 558091) was used to assess
RNA isolation and qPCR the immunosuppression of neutrophils. PD-1 (CD279, BD, 562523) and
Total RNA was isolated using the Trizol RNA Isolation kit (Invitrogen). TIM3 (BD, 566346) were used to assess the exhaustion of CD8+ T cells.
The Reverse Transcription Reagents kit (TIANGEN) was used for cDNA The depletion efficiency of neutrophils was detected by both surface
synthesis from total RNA. qPCR was performed in triplicates using the and intracellular Ly6G staining. In brief, the cell suspension was first
AriaMx Real-Time PCR System (G8830A). Gene expression of stained with Ly6G-PE-Cy7 antibodies to cover the surface Ly6G protein.
chemokines (CCL2, CCL3, CCL4 and CCL5) and CD274 were quantified Cells were then fixed and permeabilized and intracellular proteins were
by the comparative C method (2−ΔΔCt) with GAPDH as an internal con- stained with Ly6G-PE antibodies.
t
trol. The fold change of each gene was calculated at different time points
versus 0 h. A list of the primers used for the queried genes is provided Statistical analysis
in Supplementary Table 5. Statistical analyses were performed using GraphPad Prism (v.9.0)
(for experimental data), and R (v.3.6.1), RStudio (v.3.5.3) and Python
Bulk RNA-seq (v.3.7.4) (for sequencing data and matched clinical variables). Compar-
RNA-seq libraries were constructed using the NEBNext Ultra RNA isons between groups were conducted using χ2 tests or Fisher’s exact
Library Prep Kit (New England Biolabs) according to the manufacturer’s test for categorical variables. Student’s t-tests, Wilcoxon rank-sum
protocol. The library was quality-checked and sequenced using the tests and ANOVA were used for continuous variables. Paired t-tests
NovaSeq 6000 sequencer (Illumina). The quality of sequencing reads were used for paired comparisons. Survival analyses were conducted
was evaluated using FastQC. Adaptor sequences and low-quality score using log-rank tests. P < 0.05 was considered to be statistically signifi-
bases were trimmed using trimmomatic (v.0.36). These reads were then cant. No statistical methods were used to predetermine the sample
mapped to human genome reference GRCh38 from Ensembl release 98 size of scRNA-seq libraries. Unless otherwise noted, each experiment
using STAR (v.2.5.2b). The fragments per kilobase of exon per million was repeated three or more times with biologically independent
mapped reads (FPKM) values and gene count values were computed samples.
49. Gulati, G. S. et al. Single-cell transcriptional diversity is a hallmark of developmental
Reporting summary potential. Science 367, 405–411 (2020).
50. Qiu, X. et al. Single-cell mRNA quantification and differential analysis with Census. Nat.
Further information on research design is available in the Nature Port- Methods 14, 309–315 (2017).
folio Reporting Summary linked to this article. 51. Lange, M. et al. CellRank for directed single-cell fate mapping. Nat. Methods 19, 159–170
(2022).
52. Aibar, S. et al. SCENIC: single-cell regulatory network inference and clustering. Nat.
Methods 14, 1083–1086 (2017).
Data availability 53. Welch, J. D. et al. Single-cell multi-omic integration compares and contrasts features of
brain cell identity. Cell 177, 1873–1887 (2019).
Raw sequencing data reported in this paper have been deposited at the
54. Schürch, C. M. et al. Coordinated cellular neighborhoods orchestrate antitumoral
Genome Sequence Archive at the National Genomics Data Center (Beijing, immunity at the colorectal cancer invasive front. Cell 182, 1341–1359 (2020).
China) under the BioProject ID PRJCA007744. The data deposited and 55. Fan, Y. et al. Targeting multiple cell death pathways extends the shelf life and preserves
the function of human and mouse neutrophils for transfusion. Sci. Transl. Med. 13,
made public are compliant with the regulations of the Ministry of Sci-
eabb1069 (2021).
ence and Technology of China. To facilitate the use of our data by the
wider research community, we developed an interactive web-based
tool (http://meta-cancer.cn:3838/scPLC) for analysing and visualizing Acknowledgements We thank Y. Guo, C. Shan and J. Ren from National Center for Protein
Sciences at Peking University for FACS and CODEX assistance. This work is jointly supported
our single-cell data. Other public data used in this study include refer- by National Natural Science Foundation of China (81988101, 82173035, 82030079, 81972656,
ence genomes for human (https://asia.ensembl.org/, GRCh38.p13) 81802813, 81902401, 81972735 and 81872508), the National Science and Technology Major
and mouse (https://asia.ensembl.org/, GRCm39) and TCGA datasets Project of China (2018ZX10723204), Beijing Natural Science Foundation (7212108), Changping
Laboratory, the Michigan Medicine and PKU-HSC JI for Translational and Clinical Research
(https://portal.gdc.cancer.gov/). Source data are provided with this (BMU2020JI005) and Sino-Russian Math Center in PKU.
paper.
Author contributions R.X., Z.Z. and N.Z. conceived and designed the project. R.X., X.X., Z.L.
and J.Z. collected the human samples and clinical information. X.X., Z.L. and J.Z. performed
pathological examination. R.X. and X.X. performed the scRNA-seq experiments. Q.C., Q. Zhang
Code availability
and R.X. performed bioinformatic analyses. Q. Zhang, R.X. and Q.C. performed IHC, mIHC and
Codes used in this study are available at GitHub (https://github.com/ CODEX experiments. R.K., R.X., M.F. and F.W. performed functional experiments of neutrophils.
R.K. and R.X. constructed the mouse models and analysed the in vivo data. R.X., Q. Zhang,
meta-cancer/scPLC). Q.C., R.K., X.X., H.L., Q. Zhan, M.D., J.Z., Z.Z. and N.Z. discussed and interpreted the data. Q.C.,
R.X. and J.C. built the online website. R.X., Q. Zhang, Q.C. and R.K. wrote the manuscript with
42. Seehawer, M. et al. Necroptosis microenvironment directs lineage commitment in liver help from Z.Z. and N.Z.; Z.Z., J.Z. and N.Z. supervised the project.
cancer. Nature 562, 69–75 (2018).
43. Satija, R., Farrell, J. A., Gennert, D., Schier, A. F. & Regev, A. Spatial reconstruction of Competing interests Z.Z. is a founder of Analytical BioSciences and is a consultant for
single-cell gene expression data. Nat. Biotechnol. 33, 495–502 (2015). InnoCare Pharma and ArsenalBio. N.Z. is the CSO of Yunnan Baiyao Group. The other authors
44. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell gene expression data declare no competing interests.
analysis. Genome Biol. 19, 15 (2018).
45. Puram, S. V. et al. Single-cell transcriptomic analysis of primary and metastatic tumor Additional information
ecosystems in head and neck cancer. Cell 171, 1611–1624 (2017). Supplementary information The online version contains supplementary material available at
46. Muhl, L. et al. Single-cell analysis uncovers fibroblast heterogeneity and criteria for https://doi.org/10.1038/s41586-022-05400-x.
fibroblast and mural cell identification and discrimination. Nat. Commun. 11, 3953 (2020). Correspondence and requests for materials should be addressed to Jiye Zhu, Zemin Zhang or
47. Aran, D. et al. Reference-based analysis of lung single-cell sequencing reveals a Ning Zhang.
transitional profibrotic macrophage. Nat. Immunol. 20, 163–172 (2019). Peer review information Nature thanks Andres Hidalgo, Alexander Swarbrick and the other,
48. Vento-Tormo, R. et al. Single-cell reconstruction of the early maternal-fetal interface in anonymous, reviewer(s) for their contribution to the peer review of this work.
humans. Nature 563, 347–353 (2018). Reprints and permissions information is available at http://www.nature.com/reprints.
Article
Extended Data Fig. 1 | See next page for caption.
Extended Data Fig. 1 | Patient cohort and cluster information. a, Pie charts tumour cells and TIME cells. Tumour cells were further coloured by patient,
showing the composition of cancer types in our cohort. HCC, hepatocellular cancer type, virus, and cirrhosis. f, CNV profiles inferred from scRNA-seq data
carcinoma; ICC, intrahepatic cholangiocarcinoma; CHC, combined for each cell and from matched bulk exome data in the sample A014_HCC.
hepatocellular and cholangiocarcinoma; HH, hepatic hemangioma; g, Boxplots showing hepatic scores and biliary epithelial scores in tumour
ASC, adenosquamous carcinoma; SAR, sarcomatoid carcinoma; SLC, (n = 193,877 cells) and TIME cells (n = 898,295 cells). Cells are from 124 patients.
secondary liver cancer. CRC_M, liver metastasis from colorectal cancer, h, Boxplots showing hepatic scores and biliary epithelial scores in tumour cells
PAN_M, liver metastasis from pancreatic cancer, LYM_M, liver metastasis from of different PLC subtypes (HCC, n = 96,211 cells from 79 cases, ICC, n = 52,345
lymphoma, GAS_M, liver metastasis from gastric cancer, BRC_M, liver cells from 25 cases, CHC, n = 15,493 cells from 7 cases). Cells are from 111
metastasis from breast cancer. b, UMAP plots showing the distribution of patients. i, Pie charts showing the patient number (top) and cell number
patients, cancer types, viruses and liver cirrhosis states. Dots represent (bottom) of our study and published single cell studies for PLC. Colours
individual cells. PB, peripheral blood; AL, adjacent liver; HBV, hepatitis B virus, represent different studies. j, Stacked barplot showing proportions of major
HCV, hepatitis C virus, NBNC, double negative of HBV and HCV. c, UMAP plots cell populations among different studies. Colours represent major cell
showing expression of canonical marker genes of major cell populations populations. In g-h, n denotes individual cells. Two-sided Wilcoxon rank-sum
including T cells (CD3D, CD8A, FOXP3), NK cells (NKG7), B cells (CD79A), test is used. For boxplots, centre line shows median, box limits indicate upper
macrophages (CD68), neutrophils (CSF3R), dendritic cells (CLEC10A), mast cells and lower quartiles, and whiskers extend 1.5 times the interquartile range,
(TPSAB1), fibroblasts (COL1A1), endothelial cells (VWF), and epithelial cells while data beyond the end of the whiskers are outlying points that are plotted
(EPCAM). d, Stacked barplot showing the distribution of major cell types in individually. ***, P < 0.001.
each sample. e, UMAP plots showing the distribution of cell identities for
