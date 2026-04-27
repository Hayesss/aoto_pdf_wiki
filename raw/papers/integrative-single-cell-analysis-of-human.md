---
source_path: /mnt/c/Users/Administrator/Zotero/storage/R3VJXXGH/Chu 等 - 2024 - Integrative single-cell analysis of human colorectal cancer reveals patient stratification with dist.pdf
ingested: 2026-04-23
sha256: 3810248697bee139
---

nature cancer
Analysis https://doi.org/10.1038/s43018-024-00807-z
Integrative single-cell analysis of human
colorectal cancer reveals patient
stratification with distinct immune evasion
mechanisms
Received: 17 June 2023 Xiaojing Chu 1,5, Xiangjie Li 1,5, Yu Zhang1,5, Guohui Dang 1,2, Yuhui Miao 1,
Wenbin Xu1, Jinyu Wang1, Zemin Zhang 3,4,6 & Sijin Cheng 1,6
Accepted: 16 July 2024
Published online: xx xx xxxx
The tumor microenvironment (TME) considerably influences colorectal
Check for updates
cancer (CRC) progression, therapeutic response and clinical outcome, but
studies of interindividual heterogeneities of the TME in CRC are lacking.
Here, by integrating human colorectal single-cell transcriptomic data
from approximately 200 donors, we comprehensively characterized
transcriptional remodeling in the TME compared to noncancer tissues
and identified a rare tumor-specific subset of endothelial cells with T cell
recruitment potential. The large sample size enabled us to stratify patients
based on their TME heterogeneity, revealing divergent TME subtypes
in which cancer cells exploit different immune evasion mechanisms.
Additionally, by associating single-cell transcriptional profiling with risk
genes identified by genome-wide association studies, we determined that
stromal cells are major effector cell types in CRC genetic susceptibility. In
summary, our results provide valuable insights into CRC pathogenesis and
might help with the development of personalized immune therapies.
Colorectal cancer (CRC) is among the most common malignancies. However, these single-cell studies had limited sample sizes and cell
Extensive bulk-level studies have characterized the molecular land- numbers, hindering a full and in-depth characterization of the cellular
scapes of CRC1–3 and established four consensus molecular subtypes heterogeneity in the CRC TME. Furthermore, each study annotated
(CMSs) with distinct prognoses4,5. With the aid of single-cell tech- cell subsets according to its own procedures, making cross-study
nologies, recent studies have revealed the heterogeneities in the comparisons difficult, and it remains to be determined whether sub-
tumor microenvironment (TME)6–8 of CRC and highlighted several sets defined in a specific study can be generalized to other studies.
tumor-specific subpopulations, such as the SPP1+ tumor-associated Therefore, a harmonized single-cell reference atlas of human CRC is
macrophages, which have a proangiogenic role in CRC9. Addition- needed to guide subsequent single-cell studies on CRC. Additionally,
ally, studies have begun to characterize the cellular heterogeneities interpatient heterogeneity has received increasing attention in rela-
in the TME for different CRC subtypes and found that interferon tion to different clinical outcomes, but a patient stratification model
(IFN)-stimulated gene (ISG) signaling and regulatory T (T ) cells based on the cellular composition of the CRC TME at the single-cell
reg
show preferences in mismatch repair-deficient tumors10,11. level is still lacking.
1Changping Laboratory, Beijing, China. 2Academy for Advanced Interdisciplinary Studies, Peking University, Beijing, China. 3BIOPIC, Beijing Advanced
Innovation Center for Genomics, School of Life Sciences, Peking University, Beijing, China. 4Peking-Tsinghua Center for Life Sciences, Academy for
Advanced Interdisciplinary Studies, Peking University, Beijing, China. 5These authors contributed equally: Xiaojing Chu, Xiangjie Li, Yu Zhang. 6These
authors jointly supervised this work: Zemin Zhang, Sijin Cheng. e-mail: zemin@pku.edu.cn; chengsj@mail.cbi.pku.edu.cn
Nature Cancer
Analysis https://doi.org/10.1038/s43018-024-00807-z
By integrating multiple single-cell datasets, we have created the in the tumor and paracancerous regions also supported this finding
largest cohort study of CRC, allowing us to paint a complete land- (Extended Data Fig. 4a). Additionally, a marked enrichment of mono-
scape of the cellular heterogeneity in human colon tissues, covering cytes and macrophages was observed in nonphysiological proliferating
samples from healthy volunteers, patients with chronic inflammation regions (polyps and tumors), not in inflamed tissues, indicating that
and patients with cancer. Furthermore, we have identified transcrip- the accumulation of monocytes and macrophages was not likely driven
tional alterations and cell subsets specific to tumors and evaluated by local inflammation (Fig. 1f). Importantly, we observed different
the interindividual variation across patients with CRC. Six patient distribution patterns of CD4+ T cells and CD8+ T cells (Fig. 1f). CD4+
groups with diverse TME cellular compositions have been identified, T cells exhibited a comparable high proportion in inflamed, polyp
providing insights into the cellular and molecular mechanisms of and tumor tissues. In contrast, CD8+ T cells showed a higher propor-
immune evasion exploited by tumor cells in different patient groups. tion in tumor tissues than in inflamed tissues, in line with the pivotal
These findings provide valuable insights into CRC pathology and roles of CD8+ T cells in antitumor immunity. This distribution pattern
can guide the development of immunotherapy for different CRC was also observed in the validation cohort (Extended Data Fig. 4b).
patient groups. To reinforce the robustness of our findings, we performed sensitivity
analyses for the cell abundance analysis by randomly excluding one or
Results two datasets. Remarkably, we were able to reproduce all the observed
A single-cell atlas of the human colorectum patterns (Extended Data Fig. 5a).
To establish a comprehensive single-cell atlas of the human colorectum We then assessed the transcriptional shifts of major cell types
under both physiological and pathological conditions, we collected under different conditions by measuring their transcriptional similar-
published single-cell RNA-sequencing data of healthy colorectal tis- ity using the Bhattacharyya distance24,25. We found large differences
sues12,13, uninflamed and inflamed tissues from patients with ulcera- for fibroblasts and ECs when comparing tumors to paracancerous and
tive colitis (UC)14–17, colorectal polyp tissues18, paracancerous tissues inflamed tissues (Fig. 2a), indicating the acquisition of specific cellular
and tumor tissues of CRC7,9–11,19,20. The atlas comprised 1,144,726 cells functions for stromal cells during tumor development. Monocytes
across 427 samples from 192 donors (Supplementary Table 1). After and macrophages showed the largest differences when comparing
quality control, we classified 873,302 cells into 58 subsets, including tumors to polyps (Extended Data Fig. 5b), characterized by enhanced
15 T cell/natural killer (NK) cell/innate lymphoid cell (ILC) subsets, migration, phagocytosis, response to IFNγ and production of tumor
12 myeloid cell subsets, 12 endothelial cell (EC) subsets and others necrosis factor (TNF) in tumors (Extended Data Fig. 5c). We further
based on their distinct gene expression patterns (Extended Data Figs. 1 investigated the tumor-specific transcriptional alterations in ECs
and 2a–e). We then filtered out cells expressing <800 genes and con- and fibroblasts by comparing them to those in inflamed tissues from
structed a high-quality colorectal atlas containing 671,192 single cells patients with UC (Supplementary Tables 5 and 6). We found that the
(http://118.190.148.166:8918/). This atlas includes data on tumor tissues downregulated genes in tumors showed significant enrichments in
from 124 donors, paracancerous tissues from 78 donors, polyps from cytokine-mediated signaling and complement activation-related
9 donors, inflamed tissues from 23 donors, uninflamed tissues from pathways, indicating an immune dysfunction of stromal cells in tumors
11 donors and healthy tissues from 36 donors (Fig. 1a–c). Addressing (Fig. 2b,c). The expression levels of genes associated with EC migration,
the concerns about batch effects, we observed that cells were clus- extracellular matrix organization, response to transforming growth
tered based on cell types and pathological status rather than datasets factor-β (TGFβ) and the Wnt signaling pathway were significantly
(Extended Data Fig. 3a). We also conducted a principal component elevated in tumors (Fig. 2d,e). Previous studies have elucidated the
(PC) analysis (PCA) and a distance analysis on the samples based on cell immunosuppressive role of TGFβ (ref. 26), and the activation of TGFβ
subtype proportions. The results showed that the differences between and Wnt signaling has been reported to be associated with tumor
the samples were mainly caused by pathological status (Fig. 1d,e and progression27,28. Therefore, compared to those in chronic inflamma-
Extended Data Fig. 3b). We further collected single-cell data from 31 new tion, stromal cells in tumors were shaped into an immunosuppressive
patients with CRC21 and annotated the subclusters (Methods). These and tumor-promoting phenotype to facilitate tumorigenesis and the
new patients were used as a validation cohort (Supplementary Table 2). development of CRC.
We next aimed to characterize major cell-type preferences among
different tissues (Extended Data Fig. 3c,d and Supplementary Tables 3 Immune and stromal cell compartment remodeling in tumors
and 4). We observed substantial differences in cell-type proportions We next examined the tissue distribution preference of each cell sub-
across different pathological conditions. For instance, plasma cells set. Using a Ro/e (observed and expected cell ratio) analysis29,30, we
showed the lowest abundance in tumor tissues and the highest propor- found that cell subsets in both the immune and stromal cell compart-
tion in healthy tissues (Fig. 1f), primarily driven by the loss of immuno- ments exhibited obvious tissue preferences among tumors and para-
globulin A (IgA)+ plasma cells in tumors. By contrast, IgG+ plasma cells cancerous tissues (Fig. 2f). As expected, tumor-reactive CD8+ T cells
exhibited a higher proportion in tumors and inflamed tissues (Fig. 1g), (CD8-CXCL13), CD4-IL17A, T -FOXP3 and macro-SPP1 were enriched
reg
consistent with a previous report22, suggesting their important roles in tumors compared to controls. The distribution patterns of gamma
in tumor immunity and inflammation. Based on spatial transcriptomic delta (γδ) T cells remain controversial6,11. Our results showed that
data from two patients23, the expression patterns of IgG and IgA genes γδ T cells exhibited a slight preference for paracancerous samples
Fig. 1 | Human colorectal atlas and tissue preference of major cell types. 83 (paracancerous), 16 (polyp) and 180 (tumor). Data were analyzed using a
a, Overview of the data included in the atlas. b, UMAP plot showing the tissue Student’s t test (two-sided). P values are shown in Supplementary Table 3. g, Box
origins of cells (n = 671,192 cells). c, UMAP plot showing the identified subsets plots (top and bottom quartiles with horizontal lines at the median and whiskers
of all immune and nonimmune cells (n = 671,192 cells). d, PCA plots showing denote the range of the data that falls within 1.5 times the interquartile range
sample clustering based on cell subset abundance, colored by tissue type above the third quartile and below the first quartile) showing the cell proportion
(n = 245 samples). e, Heatmap showing the distances between each two tissue of each plasma subset in all nonepithelial cells. Each dot indicates a sample; n = 28
types. f, Box plots (top and bottom quartiles with horizontal lines at the (healthy), 10 (uninflamed), 15 (inflamed), 83 (paracancerous), 16 (polyp) and
median and whiskers denote the range of the data that falls within 1.5 times 180 (tumor). Data were analyzed using a Student’s t test (two-sided). P values are
the interquartile range above the third quartile and below the first quartile) shown in Supplementary Table 3. cDC, conventional DC; pDC, plasmacytoid DC;
showing the cell proportion relative to all nonepithelial cells in different tissues. Fib, fibroblast; Mono, monocyte; Macro, macrophage.
Each dot indicates a sample; n = 28 (healthy), 10 (uninflamed), 15 (inflamed),
Nature Cancer
Analysis https://doi.org/10.1038/s43018-024-00807-z
than tumors. Furthermore, mast cells have been reported to have in the abundance of mast cells between tumors and paracancerous
higher proportions in tumor tissues than in paracancerous tissues controls, except for a slight increase in polyps (Extended Data Fig. 3c)
in most cancer types31. Our study did not find an obvious difference than in paracancerous and healthy tissues.
a Polyp b
23 donors 9 donors
26,509 cells 46,947 cells
192 donors
671,192 cells
Paracancerous tissue
11 donors 78 donors
17,656 cells 167,470 cells
Healthy tissue Tumor tissue
36 donors 124 donors
110,136 cells 302,474 cells
c B cells T/NK/ILCs Stromal cells
B-IgD NK-GZMH Fib-CCL19
B-LRMP NK-XCL1 Fib-FABP5
B-LRMP-proliferating T-CD4-ANXA1 Fib-IGF1
B-MS4A1 T-CD4-CCR7 Fib-MFAP5
B-plasma-IgA T-CD4-CXCL13 Fib-pericyte-RGS5
Malignant cells/
B-plasma-IgG T-CD4-IL17A Fib-POSTN
epithelial cells Myeloid cells T-CD4-Treg-FOXP3 Fib-proliferating
T-CD8-CXCL13 Fib-smooth muscle-DES
DC-cDC-CD1C
T-CD8-γδT-TRDC Fib-transiting
DC-cDC-CLEC9A
T-CD8-GZMK Fib-WNT5A
DC-cDC-LAMP3
T-CD8-IL7R Glial cell-CLU
DC-pDC-LILRA4
T-CD8-ISG15 EC-artery-FBLN2
Mono-CD16 T-CD8-MAIT-KLRB1 EC-artery-GJA5
T/NK/ILCs Myelo S id tr o c m el a ls l cells M M a o c n r o o - - F C C 1 N Q 1 C T IL - C pr -I o L l 4 if I e 1 rating E E C C - - c c a a p p i i l l l l a a r r y y - - B C T A N 4 L9
B cells M M M a a a c c c r r r o o o - - - I L S S Y P G V P 1 E 1 5 1 Ma M li a g li n g a n n a t n /e t p c i e th ll elial cells E E E C C C - - - H H ly E E m V V p - - C S h E a X L t C i E c L 1 E 0 C-LYVE1
Mast cell-TPSAB1 Epithelial cell EC-lymphatic EC-PROX1
Myeloid-proliferating EC-proliferating
EC-transiting 1
EC-transiting 2
EC-vein-ACKR1
d
f g
Plasma Mono/macro CD4 CD8 Plasma−IgA Plasma−IgG
0.75
0.50
0.25
0
Nature Cancer
noitroporP
0.8
0.6
0.4
0.2
0
yhtlaeH demalfninU demalfnI suorecnacaraP pyloP romuT yhtlaeH demalfninU demalfnI suorecnacaraP pyloP romuT yhtlaeH demalfninU demalfnI suorecnacaraP pyloP romuT yhtlaeH demalfninU demalfnI suorecnacaraP pyloP romuT
noitroporP
yhtlaeH demalfninU demalfnI suorecnacaraP pyloP romuT yhtlaeH demalfninU demalfnI suorecnacaraP pyloP romuT
e
Tissue type
Healthy
Uninflamed
Inflamed
Paracancerous
Polyp
Tumor
PCA_1
2_ACP
UMAP_1
2_PAMU
Healthy
Uninflamed
Inflamed
Paracancerous
Polyp
Tumor
UMAP_1
2_PAMU
Inflamed tissue
Uninflamed tissue
Healthy
med
Healthy 0
Uninfla
Un
I
in
n
f
f
l
l
a
a
m
m
e
e
d
d 0
0
.
.
1
1
8
2
0.
0
07
In
0
fla
med
Paracancerous
Paracancerous 0.13 0.04 0.09 0
Polyp
Polyp 0.18 0.1 0.07 0.13 0 Tu
mor
Tumor 0.35 0.25 0.18 0.26 0.18 0
0 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50
Distance
Analysis https://doi.org/10.1038/s43018-024-00807-z
f
1.54 0.70 B-IgD 2.15 0.36 Fib-CCL19
1.66 0.63 B-LRMP 2.32 0.27 Fib-FABP5
1.16 0.91 B-MS4A1 0.41 1.33 Fib-IGF1
1.98 0.46 Plasma-IgA 2.50 0.17 Fib-MFAP5
0.46 1.30 Plasma-IgG 2.21 0.33 Fib-POSTN
Ro/e
1.25 0.86 CD4-ANXA1 0.08 1.51 Fib-WNT5A
2.0
1.17 0.90 CD4-CCR7 0.39 1.34 Pericyte
1.5
0.75 1.14 CD4-CXCL13 1.76 0.58 Smooth muscle
0.27 1.41 CD4-IL17A 2.23 0.32 Artery-FBLN2 1.0
0.30 1.39 T reg -FOXP3 0.04 1.53 Artery-GJA5 0.5
0.11 1.49 CD8-CXCL13 2.20 0.34 Capillary-BTNL9 0
1.38 0.79 CD8-γδT 2.48 0.18 Capillary-CA4
0.67 1.18 CD8-GZMK 0.20 1.44 HEV-CXCL10
1.54 0.70 CD8-IL7R 0.01 1.55 HEV-SELE
0.29 1.39 CD8-ISG15 1.86 0.52 Lymphatic EC-LYVE1
0.51 1.27 CD8-MAIT 2.26 0.30 Lymphatic EC-PROX1
0.61 1.22 NK-GZMH 1.74 0.59 Vein-ACKR1
0.81 1.11 NK-XCL1 2.17 0.35 Glial cell
1
0
1
.
.
5
.
0
9
2
1
0
0
1
0
.
.
0
.
7
9
6
1
9
I
c
c
L
D
D
C
C
C
-
-
C
C
D
LE
1C
C9A
Paracancerous
Tu
mor
0.25 1.42 cDC-LAMP3
0.20 1.44 pDC
0.92 1.04 Mono-CD16
0.36 1.36 Mono-FCN1
0.20 1.44 Macro-C1QC
0.21 1.44 Macro-ISG15
0.94 1.03 Macro-LYVE1
0.05 1.52 Macro-SPP1
1.13 0.93 Mast cell
Paracancerous
Tu
mor
Nature Cancer
B
amsalP
4DC
8DC
KN
CLI
CD
orcam/onoM
tsaM
tsalborbiF
CE
lailG
a b c
Bhatt distance difference Downregulated in ECs in tumors Downregulated in fibroblasts in tumors
Tumor vs. paracancerous Type I IFN signaling pathway 5 Leukocyte chemotaxis 14
− 0 3 2 1 1 Regulation C o y f t o s k u i p n r C e a - e m m ll o e u B l d l l e a o i C c a r o u t o r d e e l m a d s v r p p e s f o s l R i i e g s b n e m e n e s s l a e r p e E l o n o i t C n o r t n g g a s m t a e y c p n i p t a g t i i o e v z t r h a a a I I w t t t F I i i i F N o o o a N n n n y γ 5 8 6 10 6 5 Pos N it e iv g e a r t e iv g e u r l e at g io u n la t o io f N n s e u o g p f a r t r a i e M m v s e y p o e r o l C e e l n o C g c e s i C u o u l d e l l l m u e a a l t l l e o r t l a p u u i f r o l e l k i e b n a r x o m e r e t c o s e r d e y p f r o e n t n c o e t r t a o n o g a m l a s x a c s e g i n i f t t g u i i i i t c v m z r o l a a a a a u T t t t t t i i i i i l N o o o o o u n n n n n F s 1 1 9 1 1 1 3 7 0 3 19
Fib m E C acro Glial IL C D C C D M 4 as C tD8BNK Cellular R r e e s s p p o o n n s s e e t t o o I F T N N β F 6 3 Resp R o e n s s p e o n to s e h y to p o T x N i F a 1 1 4 3
Mono/
0
−
1
log
2 3 0
−
1
log
2 3
10 10
(adjusted (adjusted
P value) P value)
Tumor vs. inflamed d e
− 0 2 1 1 E C Mo F n ib o/ N m K acro C D8B C D4 P P o o s s i i t t i i v v e e r r e e g g u u l l a a t t i i o o n n o o f f c P s e u o l b s l i s m t t iv r o a e r t p e r I e h n a g P o t d e u o g h g l s e a e r i n t t i s i n i e v i o U o - s e m n p n i s r E - r o e e d e i n f d n g g e d c v i E u p a u o o e p l t e l a t l l e a i h l v n t t − d t h i e e d e o s e d l s d e u n i l E i u n i b g i a i C o n m n t s n l f t c d d a c E r c d e E l a i i e C i ff ff e e l C n t l l s l e l e e v g l s e m m r r i a a p n e e p l d d o i i r n n a g g t e h h p u t t t r r a i i e e h m m a a a a d s s w t t t t e i o i i i i i i n o o o o o o a n r g n n n n n n y s t 2 1 2 9 1 0 4 7 18 12 1 1 3 4 I C n U E t e p e x l r t g l e E − r r a g x s in c t u u r e - b l a m C a l s c C l t o u t e e e C o r l l d l d a l a e l l C a l u i t r l a a i e g W l e l n s − t g a e l e j t c n l r e u f n r − d i e u t n b n m s m l c s s R c r u l f a o i i t t i e s b g g e b u t i b i s o r t s n n g r r i a l p t n e i x a a a n l r b o l l s a a o o o o i i o n t n n t l r r r r s e l i s g g g g g g i n c e i a a a a a g n p p d p t n n n n a a o t b h i i i i r u z z z z t t o y e T h h m a a a a c s G W w w t t t t e o i i i i i o o o o o F a a s n r n n n n n β y y s s t 4 2 4 2 0 2 2 3 0 4 2 4 4 6 22 4 4 9 9
0 1 2 3 4 0 5 10 15
Less More
similar similar −log 10 −log 10
(adjusted (adjusted
P value) P value)
g Upregulated pathways in artery-GJA5
Cell−substrate adhesion 56
Epithelium migration 54
EC migration 45
Regulation of actin cytoskeleton organization 46
0 5 10 15
−log (adjusted P value)
10
Fig. 2 | Characterization of immune and stromal cell subsets in CRC. a, Box pathways. Data were from an overrepresentation analysis (BH adjustment).
and violin plots (top and bottom quartiles with horizontal lines at the median and d,e, Lollipop plots showing upregulated pathways in ECs (d) and fibroblasts
whiskers denote the range of the data that falls within 1.5 times the interquartile (e) in tumors compared to inflamed tissues. Numbers in the dots indicate gene
range above the third quartile and below the first quartile) showing the counts matched to corresponding biological pathways. Data were from an
Bhattacharyya (Bhatt) distance difference between tumors and paracancerous overrepresentation analysis (BH adjustment). f, Heatmap showing the tissue
tissues (top) and between tumors and inflamed tissues (bottom) in different cell preference of each cell subset as indicated by the Ro/e score. g, Lollipop plot
types (n = 100 for each cell type). b,c, Lollipop plots showing downregulated showing upregulated pathways in artery-GJA5 compared to artery-FBLN2.
pathways in ECs (b) and fibroblasts (c) in tumors compared to inflamed tissues. Numbers in the dots indicate gene counts matched to corresponding biological
Numbers in the dots indicate gene counts matched to corresponding biological pathways. Data were from an overrepresentation analysis (BH adjustment).
Analysis https://doi.org/10.1038/s43018-024-00807-z
Artery-GJA5
Artery-FBLN2
Capillary-BTNL9
Capillary-CA4
EC-transiting 1
EC-transiting 2
Vein-ACKR1
HEV-SELE
HEV-CXCL10
Lymphatic EC-LYVE1
Lymphatic EC-PROX1
Proliferating ECs UMAP_1
Nature Cancer
2_PAMU
a b c
23 12.5
10.0
25
7.5
5.0
8 2.5
0
T cell R m e i s g p r o at n R i s o e e n s p to o n T s N e F to IFNγ d e
f
g
j
h
i
01LCXC 11LCXC 9LCXC 1PBG 1ODI ELES 1PAT PMYT 1MACV 1ENIPRES 61SGR 1SBHT 12LCC
01LCXC-VEH
ni
syawhtap
detalugerpU
2PIAFNT 312FNR
−log10(adjusted
P)
Top marker genes of HEV-CXCL10 cells
IFNG
TNF
CD40LG
TNFSF14
SPP1
POMC
HMGB1
IL15
ITGAM
EBI3
TGFB1
TGFA
ADAM17
PGF
AGT
sdnagil
dezitiroirP
Max
Min
CUA
delacS
laitnetop
yrotalugeR
2
1
0
−1 −2
noisserpxe
delacs
naeM
Tumor
B-LRMP B-MKI67-LRMP
CD8-MAIT ILCs
B-IgD
B-MS4A1
CD4-ANXA1 CD4-CCR7
CD8-IL7R CD4-CXCL13 CD8-GZMK CD8-ISG15 CD4-IL17A
T NreKg- - F G O Z X M P H 3 NK-XCL1 T-proliferating CD8-CXCL13 CD8-γδT Macro-LYVE1 Macro-ISG15 Macro-C1QC Macro-SPP1
Mono-FCN1 cDC-CLEC9A
Mast cells
cDC-CD1C ESRRA Proliferating myeloids
STAT1 c M D o C n - o L - A C M D P 16 3
RELB Plasma p -I D g C A STAT2 Plasma-IgG IRF2 Ca C p a il p la il r l y a - r B y T -C N A L9 4
IRF7 F F ib ib - - P F O A S B T P N 5
SOX4 Pericyte
NFKB1 Fib-proli F fe ib ra -I t G in F g 1 IRF9 V F e ib in -W -A N C T K 5 R A 1 NFKB2 HEV-SELE
Artery-GJA5
Proliferating ECs Glial cells Lymphatic EC-LYVE1 Smooth muscle Artery-FBLN2 Fib-CCL19 Fib-MFAP5 HEV-CXCL10 Lymphatic EC-PROX1
Paracancerous
Correlation coefficient
−1 −0.5 0 0.5 1
PMRL-B PMRL-76IKM-B TIAM-8DC sCLI DgI-B 1A4SM-B 1AXNA-4DC 7RCC-4DC R7LI-8DC 31LCXC-4DC KMZG-8DC 51GSI-8DC A71LI-4DC H 3P
M X Z O G F - - KgeNrT
1LCX-KN gnitarefilorp-T 31LCXC-8DC Tδγ-8DC 1EVYL-orcaM 51GSI-orcaM CQ1C-orcaM 1PPS-orcaM 1NCF-onoM A9CELC-CDc sllec
tsaM
C1DC-CDc sdioleym
gnitarefilorP
61DC-onoM 3PMAL-CDc CDp AgI-amsalP GgI-amsalP 4AC-yrallipaC 9LNTB-yrallipaC 5PBAF-biF NTSOP-biF etycireP gnitarefilorp-biF 1FGI-biF A5TNW-biF 1RKCA-nieV ELES-VEH 5AJG-yretrA sCE
gnitarefilorP
sllec
lailG
1EVYL-CE
citahpmyL
elcsum
htoomS
2NLBF-yretrA 91LCC-biF 5PAFM-biF 01LCXC-VEH 1XORP-CE
citahpmyL
60
40
20
0
Stromal cells
T/NK
Macrophage CAFs
Macrophage
Plasma cells
T/NK Macrophage
Stromal cells CAFs
Stromal cells
)%(
+54DC
ni noitroporp
T
01LCXC-VEH
tnesba
01LCXC-VEH
tneserp
4
3 2
1
0
CXCL9/10/11 VWF, PECAM1 SELP P = 0.05 CD8A, CD4
T cell
EC
10 µm Patient 1
10 µm
Patient 2
level
noisserpxE
9LCXC
5
4
3
2
1
0
01LCXC
4 3
2
1 0
ESRRA (21g)
3
STAT1 (92g)
RELB (187g)
STAT2 (37g)
IRF2 (219g) 0
IRF7 (56g)
SOX4 (318g)
NFKB1 (208g) IRF9 (43g) −3 NFKB2 (82g)
RELB
STAT1 NFKB2
CXCL9
ESRRA CXCL11 CXCL10 NFKB1
Weights >0.005
Weights ≤0.005
STAT2 IRF7
IRF2
11LCXC
Arte A r C r y t a - e G p ry i J l - A l F a C 5 B ry a L - p N B E i 2 T l C l N a - r t L E y r 9 C a -C n -t A s r i a 4 ti n n V s g i e t i 1 i n n L g - y A H 2 m C H L E p K y V E h R m V - a 1 S - p t C E i h c L X a E E C t P i C c L r - o 1 E L 0 l C Y if V e -P r E a R 1 t O in X g 1 ECs
Arte A r C r y t a e -G p ry i J l - A l F a C 5 B r a y L p - N B E il 2 C T la N -t r E L r y a 9 C - n C -t s A r i a t 4 i n n V s g e i t 1 i i n n L - g A y H m 2 C H L E K p y E V R m h V -S a 1 - p t C E i h c L X a E E C t P i C c L r - 1 o E L 0 Y l C if V - e P E r R a 1 O tin X g 1 ECs
Arte A C r r y t a e -G p ry i J l - A l F a C 5 B ry a L - p N E B i C 2 T ll N - a t E r L r y C a 9 - n - C t s r A i a t 4 i n n V s g e it i i 1 n L n y - g A H m L C H 2 E y p V K E m h - V R S a p - 1 t E C h ic L X a E t E C P ic C L r o - 1 E L 0 l C i Y f - e V P r E R a 1 t O in X g 1 ECs
Analysis https://doi.org/10.1038/s43018-024-00807-z
Fig. 3 | Characterization of EC subsets and cell subset co-occurrence in MERSCOPE FFPE Human Immuno-oncology (https://vizgen.com/data-release-
CRC. a, UMAP plot showing a HEV-like endothelial subset (red dashed circle) program/). The results were replicated in two patients. f, Heatmap showing the
(n = 11,233 cells). b, Violin plots showing the expression level of CXCL9, CXCL10 regulatory potentials of the top 15 prioritized ligands in regulating target genes.
and CXCL11 in each endothelial subset (n = 11,233 cells). c, Lollipop plot showing g, Heatmap showing the regulon activities of the top ten prioritized transcription
enriched pathways in marker genes of HEV-CXCL10. Numbers in the dots indicate factor genes in each endothelial subset. AUC, area under the curve. g is short
gene counts matched to corresponding biological pathways. Data were from for target genes. h, Heatmap showing the scaled expression levels of the top ten
an overrepresentation analysis (BH adjustment). d, Box plot (top and bottom prioritized transcription factor genes in endothelial subsets. i, Network plot
quartiles with horizontal lines at the median and whiskers denote the range showing regulation weights between transcription factor genes (yellow) and
of the data that falls within 1.5 times the interquartile range above the third downstream targeted genes (red). j, Heatmap showing correlation coefficients
quartile and below the first quartile) showing the proportion of T cells relative between cell subsets in tumor (top right) and paracancerous (bottom left)
to all CD45+ cells in patients with and without HEV-CXCL10 (n = 14 (left) and 30 samples (n = 180 (tumor) and 83 (paracancerous)). Data were analyzed using a
(right)). Data were analyzed using a Wilcoxon’s test (two-sided). e, Vizgen spatial Spearman’s correlation test.
transcriptomic data showing HEV-CXCL10-like cells. Data were acquired from
Consistent with the Bhattacharyya distance analysis, the largest Co-occurrence patterns between tumor-associated cell
Ro/e values were found for EC and fibroblast subsets. Comparing subsets
the tumor-enriched arterial subset (artery-GJA5) and the normal To infer the co-occurrence patterns between cell subsets, we performed
arterial subset (artery-FBLN2) highlighted an enhanced migration a correlation analysis on the abundance of cell subsets in both tumors
capacity of tumor arteries (Fig. 2g). Among the fibroblast subsets, and paracancerous tissues. As shown in Fig. 3j, cell subsets were clus-
two tumor-enriched subsets were denoted as cancer-associated fibro- tered majorly on their broad cell types, and the plasma subsets were
blasts (CAFs) (Extended Data Fig. 5d). These two subsets (fib-IGF1 clustered closely to stromal cells, consistent with the results of a
and fib-WNT5A) represented the inflammatory and myofibroblastic study on gastric adenocarcinoma36. We observed a positive correla-
CAFs, respectively, based on the expression patterns of the chemokine tion between macrophage subsets and fibroblasts in both tumor and
CXCL12 and the myofibroblastic marker POSTN (ref. 32) (Extended Data paracancerous samples, supporting the reported function of macro-
Fig. 5e,f), in line with previous findings reported in pancreatic ductal phages in promoting the proliferation and activation of fibroblasts37.
adenocarcinoma33 and gastric cancer34. In contrast to paracancerous tissues, as we expected, stronger
Notably, we identified a rare and tumor-enriched subset of ECs co-occurrences were observed for tumor-associated cell subsets; for
characterized by the specific expression of the venous EC marker ACKR1, example, positive correlations were found between macro-LYVE1,
selectin E (SELE) and chemokines (CXCL9, CXCL10 and CXCL11) (Fig. 3a,b macro-ISG15, macro-C1QC, macro-SPP1 and mono-FCN1 in tumors.
and Extended Data Fig. 6a), resembling high endothelial venule Furthermore, T/NK cell subsets showed negative correlations with
(HEV) cells35. A gene enrichment analysis suggested that this subset stromal subsets, and these correlations were missing in paracancerous
has a high capacity for T cell recruitment (Fig. 3c), and we associated samples, in line with the function of fibroblasts in impeding immune
the presence of this HEV-CXCL10 subset in tumors with higher T cell cell recruitment in tumors38. Altogether, our results revealed distinct
infiltration (Fig. 3d). We further validated the positive correlation co-occurrence patterns between cell subsets in tumors, suggesting
between the HEV-CXCL10 signature score and the T cell signature their important functional relevance in CRC development.
score in The Cancer Genome Atlas (TCGA) (Extended Data Fig. 6b),
supporting the HEV-like phenotype of this endothelial subset. Besides, Patient stratification with distinct immune phenotypes
in the spatial transcriptomic data with subcellular resolution from To investigate the interindividual heterogeneity of the TME, we applied
two patients with CRC, we found the colocalization of EC markers (VWF hierarchical clustering on patients based on their cell subset abun-
and PECAM1), a HEV marker (SELP) and CXCL9/10/11, demonstrating dances in the TME and classified patients with CRC into six groups
the existence of this rare endothelial subset (HEV-CXCL10). In addi- (groups 1–6 (G1–G6)) (Fig. 4a and Supplementary Table 2). Address-
tion, T cells, characterized by CD8A or CD4 expression, were around ing concerns about batch effects raised from our observation that
the ECs, which might imply the function of HEV-CXCL10 in recruiting patients from different datasets have imbalanced distributions in
T cells (Fig. 3e). the six groups, we first performed PCA on patients based on their
Next, we explored extracellular signals that drive the phenotype cell subtype preference. We observed that patients were clustered
of this HEV-like subset (Methods). IFNG and TNF were prioritized according to the six grouping labels and were partially associated with
as the top-ranked ligands regulating the signature genes of the a microsatellite-instable (MSI) status, a well-known factor influencing
CXCL10+ HEV-like subset (Fig. 3f), consistent with the gene enrich- the TME (Extended Data Fig. 6c–e). Notably, the variation within large
ment analysis. Additionally, we examined the regulatory network datasets (for example, the Pelka dataset) was greater than the varia-
that underlies this HEV-like subset (Methods) and observed that the tion across datasets (for example, between the Pelka and GSE188711
STAT1/2 and IRF2/7 regulons were activated in this subset (Fig. 3g,h). datasets), indicating that the interindividual variation far exceeded
These regulons could regulate the expression of the chemokines the variation introduced by datasets (Extended Data Fig. 6e). Next,
CXCL9, CXCL10 and CXCL11 (Fig. 3i), shaping the CXCL10+ HEV- we applied a multivariable analysis of variance (ANOVA) test to assess
like subset into an immune-recruiting phenotype. the contributions of the TME groups, datasets and MSI status to both
Fig. 4 | Characterization of interindividual heterogeneity across the TMEs showing overall survival in patients stratified based on the expression level of
of patients with CRC. a, Heatmap showing unsupervised clustering of patients G1 signature genes (n = 96 (high) and 551 (low)). Data were analyzed using Cox
based on relative cell subset abundance in each individual (n = 116). b, Violin regression. e, Lollipop plot showing downregulated pathways in malignant
plots showing the module scores of CMS marker genes in different groups (n = 10 cells of G1 in contrast to the remaining groups. Numbers in the dots indicate
(G1), 23 (G2), 10 (G3), 14 (G4), 25 (G5) and 33 (G6)). c, Box plots (top and bottom gene counts matched to corresponding biological pathways. Data were from an
quartiles with horizontal lines at the median and whiskers denote the range of overrepresentation analysis (BH adjustment). f, Circle plot showing G1-specific
the data that falls within 1.5 times the interquartile range above the third quartile cell–cell interactions among the major cell types. g, Dot plot showing the
and below the first quartile) showing EMT (left) and TGFβ (right) signatures estimated probability of ligand–receptor pairs from malignant cells to other
in different groups (n = 10 (G1), 23 (G2), 10 (G3), 14 (G4), 25 (G5) and 33 (G6)). cell types with nominal P values. P values were computed by comparing inferred
Data were analyzed using a Student’s t test (two-sided). d, Kaplan–Meier plot communication probabilities with probabilities in permutated sets.
Nature Cancer
Analysis https://doi.org/10.1038/s43018-024-00807-z
Abundance Patient group Major cell type
CD45neg
CD45pos –5 0 5
Nature Cancer
1G 2G 3G 4G 5G 6G
Cell type
B amsalP T
4DC
T
8DC
KN CLI CD /onoM orcam tsaM biF CE lailG
Site
MSI status
CD8-γδT
CD8-IL7R
CD4-CXCL13
CD8-CXCL13
CD8-GZMK
NK-GZMH
NK-XCL1
CD8-ISG15
Macro-ISG15
CD4-IL17A
C
TrDeg8 -F
-
O
M
X
A
P
IT
3
CD4-ANXA1
CD4-CCR7
B-IgD
B-MS4A1
ILCs
B-LRMP
Macro-SPP1
Mono-FCN1
Macro-C1QC
Macro-LYVE1
pDC
cDC-CLEC9A
cDC-CD1C
cDC-LAMP3
Mono-CD16
Mast cells
Plasma-IgA
Plasma-IgG
Lymphatic EC-PROX1
Glial cells
Fib-FABP5
Fib-POSTN
HEV-CXCL10
Capillary-BTNL9
Capillary-CA4
Artery-GJA5
HEV-SELE
Artery-FBLN2
Lymphatic EC-LYVE1
Vein-ACKR1
Pericyte
Fib-CCL19
Smooth muscle
Fib-MFAP5
Fib-IGF1
Fib-WNT5A
b
1.5 CMS1 CMS2 CMS3 2 CMS4
0 1. . 0 5 0.5 1 1
0 0 0 0
−0.5
− − 1 1 . . 0 5 −0.5 −1 −1
G1 G2 G3 G4 G5 G6 G1 G2 G3 G4 G5 G6 G1 G2 G3 G4 G5 G6 G1 G2 G3 G4 G5 G6
e
Downregulated pathways
d f
epyt
llec
rojaM
epyt
lleC
Site MSI status
Left MSI
Right MSS
1.00
0.75
0.50
0.25 P = 0.016
0
0 50 100 150 Time (months)
ytilibaborp
lavivruS
Gene module score Gene module score Gene module score Gene module score
g
VEGFB−FLT1
CD4 Plasma SEMA3C−PLXND1 Max
SEMA3C−NRP1_NRP2
B
CD8 PDGFA−PDGFRB
PDGFA−PDGFRA
Malignant cells
COL1A2−ITGA11_ITGB1
NK
COL1A2−ITGA1_ITGB1
COL1A1−ITGA11_ITGB1 Min
G1 signature genes = high DC EC COL1A1−ITGA1_ITGB1
G1 signature genes = low Mono/macro Fib ADGRE5−CD55
Numb in e t r e o ra f c G t 1 io -s n p s ecific 0 P . < 0 0 1 . < 0 P 1 < 0.05 Fib E C C D M 8 o m no a / cro
1 10 17
Probability
a
0.0017 4.2 × 10−5 0.3 3.4 2 . × 2 × 1 0 1 − 0 5 −5 Cellular respiration 21
0.0002 Electron transport chain 16
0.2 Cytokine-mediated signaling pathway 27
Leukocyte chemotaxis 18
0.1 Response to decreased oxygen levels 19
Cellular response to chemokine 10
0 0 2 4 6
−log (adjusted P)
10
Receiver cell type
erocs
gnilangis
TME
0.0036 1.00 0.00019 3.7 × 10−5 0.75 6.9 × 10−5
0.00052
0.50
0.25
0
erocs
noitavitca
βFGT
c
G1G2G3G4G5G6 G1G2G3G4G5G6
Analysis https://doi.org/10.1038/s43018-024-00807-z
PC1 and PC2 (Extended Data Fig. 6f,g). The results revealed that our that platelet-derived growth factor subunit A (PDGFA)–PDGFRA/B
TME groups exhibited the strongest contribution to both PC1 and PC2. was significantly enriched in malignant cells and fibroblasts (Fig. 4g),
Thus, we believe that batch effects were not a major contributor to which may serve as an important mechanism of malignant cells in
patient-level variation. To assess the robustness of our patient group- recruiting fibroblasts42. Next, we validated the inferred malignant cell
ing, we extracted and rescaled the relative proportions within patients interactions in the validation cohort (Methods, Extended Data Fig. 7d
from the Pelka dataset, the largest dataset in our study. The same and Supplementary Table 2) and successfully rediscovered the interac-
patient stratification persisted in this single large dataset (Extended tions of PDGFA and PDGFRA/B, ADGRE5 and CD55 (P < 0.05). Besides, we
Data Fig. 6h), indicating that our observed grouping was driven by observed a colocalization between ADGRE5 (also called CD97) and CD55
interindividual variation. in the tumor region from spatial transcriptomic data (Extended Data
Patients in G1 were characterized by a higher proportion of stro- Fig. 7e,f). This is in line with the reported immune-repressed regula-
mal cells but fewer infiltrating CD45+ cells. Monocytes/macrophages, tory effects of the interaction on T cells43. Our results suggest that the
dendritic cells (DCs) and plasma cells were enriched in G2, G3 and transcriptomic characteristics of malignant cells might determine the
G4, respectively. Group 5 had the largest proportion of CD8+ T and stromal cell-enriched phenotype in G1.
NK cells, whereas most CD4+ T and follicular B cell subsets fell into
G6. As expected, the MSI samples were enriched in G5, whereas the Divergent tumor immune evasion mechanisms in TME
microsatellite-stable (MSS) samples were enriched in G1, consistent subtypes
with their clinical prognosis. Additionally, we observed that more MSI We hypothesized that tumors with different TME immune subtypes
samples were located on the right side, in line with a previous report39. would evolve diversely and exploit distinct immune escape mecha-
Surprisingly, we noticed that MSS samples were enriched in G6. To nisms. Group 5, characterized by CD8+ T cell dominance and associated
confirm this finding, we evaluated a G6 score based on the expres- with favorable clinical outcomes in CRC (Fig. 5a), would be subject to
sion signatures of G6 subcluster marker genes (Methods) in TCGA highly selective pressure from T cell cytotoxicity. We compared the
datasets of CRC. We observed that a subset of MSS samples exhibited expression patterns of co-inhibitory molecules44 in CD8+ T cells across
high expression levels of G6 signature genes (Extended Data Fig. 7a). different patient groups (Methods). We found that CD8+ T cells from
Interestingly, EMP1, a marker of metastatic buds40, was less expressed G5 exhibited the highest expression levels of most of the co-inhibitory
in malignant cells of G3 and G4, whereas LGR5, a marker of CRC cancer molecules in our atlas and validation cohort (Fig. 5b and Extended Data
stem cells41, was highly expressed in patients in G4 (Extended Data Fig. 8a), indicating a higher level of T cell exhaustion. In particular, the
Fig. 7b), suggesting a potential correlation of TME immune phenotypes tumor-reactive CD8+ T cell subset (CD8-CXCL13) exhibited the high-
and malignant cell status. est aggregated expression levels of these co-inhibitory molecules in
We next assessed the relationship between our classification and G5 (Extended Data Fig. 8b). Meanwhile, CD274 and PDCD1LG2 (also
the CMS classification system4 (Methods). We found that patients in G1 called PDL1/2), the ligands of programmed cell death 1 (PD-1), were
largely matched CMS4, which is marked by stromal cell enrichment4,5 also highly expressed in the malignant cells of this group (Fig. 5b and
(Fig. 4b) and high activation of the epithelial-to-mesenchymal tran- Extended Data Fig. 8a). Thus, these inhibitory signals in T cells and
sition (EMT) and TGFβ signaling pathways (Fig. 4c). CMS4 was also malignant cells might be an effective immune evasion mechanism for
associated with the shortest overall survival4, and we observed that tumors in this group.
the top marker genes of fibroblasts and ECs were associated with poor We also observed that a CD4+ T cell subset (CD4-CXCL13) was
survival of patients with CRC (Fig. 4d). Meanwhile, G5 and G6 and a enriched in this CD8+ T and NK cell-dominated group, and the propor-
small part of G2 exhibited higher CMS1 scores, in line with the reported tion of CD4-CXCL13 was highly correlated with that of tumor-reactive
immune-activating phenotypes of CMS1 (refs. 4,5) (Fig. 4b). However, CD8+ T cells (CD8-CXCL13; Fig. 5c). By comparing CD8-CXCL13 and
these groups dominated by distinct cell subset abundances denoted CD4-CXCL13 to naive-like CD8+ and CD4+ T cells (CD8-IL7R and
diverged immune phenotypes (Fig. 4a), suggesting that our TME-based CD4-CCR7 in this study), we found that the gene expression alterations
classification revealed further subsets upon the CMS system. We also were also highly correlated for CD8-CXCL13 and CD4-CXCL13 (Fig. 5d
attempted to match our six groups with an intrinsic CMS (iCMS) classifi- and Supplementary Table 8), indicating that they might share common
cation system based on epithelial tumor cell states21 (Methods). Groups regulations. Thus, we captured their potential extracellular regulators
2 and 5 were roughly matched to iCMS3, consistent with the high inflam- (Methods), and IL15 was predicted to have a crucial impact on both
mation response of iCMS3, and patients of G3, G4 and G6 had higher the CD8-CXCL13 and CD4-CXCL13 subsets (Fig. 5e and Extended Data
iCMS2 scores but with large heterogeneity (Extended Data Fig. 7c). Fig. 8c), consistent with its role in maintaining T cell survival and cyto-
To investigate the potential mechanism underlying the stromal toxicity45. Furthermore, we observed that IL15 was highly expressed
cell-enriched phenotype in G1, we next characterized the malignant in LAMP3+ DCs (also called mregDCs (mature regulatory DCs)) (Fig. 5f
cells and specific cell–cell interactions in this group. Malignant cells and Extended Data Fig. 8d), and the expression of LAMP3 was signifi-
in G1 exhibited lower expression of genes related to aerobic respira- cantly positively correlated with that of IL15 in TCGA datasets of CRC
tion and cytokine-mediated signaling (Fig. 4e), which might result in a (Extended Data Fig. 8e), consistent with what was reported in hepa-
hypoxic microenvironment and contribute to poor immune infiltration. tocellular carcinoma46. This reminded us of the cellular triads (CD8+
Furthermore, we observed enhanced cell–cell interactions between T cells, CXCL13+ T helper cells and mregDCs) reported in hepatocellular
malignant cells, fibroblasts and ECs in G1 (Fig. 4f and Supplementary carcinoma47, implying that LAMP3+ DCs might have important roles in
Table 7). Among the ligand–receptor pairs specific to G1, we noticed the regulation of T cell functions through IL15.
Fig. 5 | Characterization of potential immune evasion mechanisms and correlation). d, Scatter plot showing the correlation between log(fold change
2
regulations. a, Kaplan–Meier plot showing overall survival in patients stratified (FC)) values in CD8-CXCL13 and CD4-CXCL13 compared to naive-like CD8+ and
based on the expression level of G5 signature genes (n = 433 (high) and 214 CD4+ T cells, respectively (n = 1,167, P = 4.48 × 10−302, Pearson’s correlation).
(low)). Data were analyzed using Cox regression. b, Heatmaps showing the e, Heatmap showing the regulatory potentials of the top 15 prioritized ligands
scaled mean expression of co-inhibitory molecules in CD8+ T cells, PDL1/2 and in regulating target genes in the CD8-CXCL13 subset. aShared ligands between
CD47 in malignant cells, and SIRPA and Fcγ receptors in macrophages. c, Bar plot CD8-CXCL13 and CD4-CXCL13. f, Dot plots showing the expression levels of the
showing correlation coefficients between the proportion of CD8-CXCL13 and top ten prioritized ligands identified for CD8-CXCL13 in each cell subset. The dot
other immune subsets in CD45+ cells. Significant correlations are colored red size indicates the fraction of expressing cells. The dot color indicates normalized
for positive correlation and blue for negative correlation (n = 198, Spearman’s expression levels.
Nature Cancer
Analysis https://doi.org/10.1038/s43018-024-00807-z
1.00
0.75
0.50
0.25
P = 0.032
0
0 50 100 150
Time (months)
Nature Cancer
ytilibaborp
lavivruS
a
G5 signature genes = high
G5 signature genes = low
05.0− 52.0−
0
52.0 05.0
CXCL13
2.5
TNFRSF18
TIGIT
PDCD1
CTLA4
0
−2.5
−2.5 0 2.5
log(FC) between CD8-CXCL13 and naive-CD8
2
c Correlation coefficient
CD8-GZMK
CD8-ISG15
CD4-CXCL13
CD8-γδT-TRDC
CD8-IL7R
CD4-IL17A
NK-XCL1
NK-GZMH
Treg-FOXP3
pDC-LILRA4
Macro-ISG15
cDC-CLEC9A
CD4-CCR7
cDC-LAMP3
CD8-MAIT-KLRB1
CD4-ANXA1
Mono-CD16
Macro-SPP1 Positive
ILCs-IL4I1 significant
Mono-FCN1
Not
Macro-C1QC
significant
Mast cell-TPSAB1
cDC-CD1C Negative
Macro-LYVE1 significant
4DC-evian
dna
31LCXC-4DC
neewteb
)CF(gol
2
R = 0.83
BTCA
HDPAG
A2TM JPBR BOLE 1NFP 2PCU
B5DIRA 4PSUD
MKP 1IPT 28DC FTAB
31LCXC
47DC ALS
PA5XOLA
A72BAR 4ALTC A1PBKF
e
aCXCL12
aSEMA4D
NAMPT
AGRN
HSPG2
aIL15
aJAG2
aIL6
aLAMB2
aCXCL14
ADAM12
COL18A1
aPTPRF
GRN
aPROS1
Regulatory potential
Min Max
sdnagil
dezitiroirP
CD8-CXCL13
f
B CD4 CD8 NK ILC Myeloid Fib Glial EC
CXCL12
SEMA4D
NAMPT
AGRN
HSPG2
IL15
JAG2
IL6
LAMB2
CXCL14
DgI-B PMRL-B 1A4SM-B AgI-amsalP GgI-amsalP 1AXNA-4DC 7RCC-4DC 31LCXC-4DC A71LI-4DC 3PXOF-
T
ger
31LCXC-8DC Tδγ-8DC KMZG-8DC R7LI-8DC 51GSI-8DC TIAM-8DC HMZG-KN 1LCX-KN sCLI C1DC-CDc A9CELC-CDc 3PMAL-CDc CDp 61DC-onoM 1NCF-onoM CQ1C-orcaM 51GSI-orcaM 1EVYL-orcaM 1PPS-orcaM sllec
tsaM
91LCC-biF 5PBAF-biF 1FGI-biF 5PAFM-biF NTSOP-biF A5TNW-biF etycireP elcsum
htoomS
sllec
lailG
2NLBF-yretrA 5AJG-yretrA 9LNTB-yrallipaC 4AC-yrallipaC 01LCXC-VEH ELES-VEH 1EVYL-CE
citahpmyL
1XORP-CE
citahpmyL
1RKCA-nieV
BTLA
TNFRSF18
CTLA4
TIGIT
PDCD1
HAVCR2
LAG3
Percentage expressed Average expression
0 50 100 −1 0 1 2
llec
T
+8DC
noisserpxe
delacs
naeM
1.8
0.9
0
−0.9
−1.8
CD274
PDCD1LG2
CD47
llec
tnangilaM
SIRPA
FCGR1A
FCGR2A
FCGR2B
FCGR3A
FCGR3B
egahporcaM
molecules
PDL1/2
Fcγ
receptors
Co-inhibitory
signaling
‘Do
not
eat
me’
d
b
G1 G2 G3 G4 G5 G6
Analysis https://doi.org/10.1038/s43018-024-00807-z
In patients with macrophage-dominated tumors (G2), cancer cells of the IgG Fc receptors in macrophages and NK cells across different
might face strong pressure from macrophage-mediated phagocytosis. patient groups. As expected, macrophages in G4 exhibited the lowest
The ‘do not eat me’ signaling pathway has crucial roles in inhibiting expression levels of the activating Fc receptors FCGR3A (also called
macrophage phagocytosis48. As expected, one of the major ‘do not eat CD16A) and FCGR2A (also called CD32A) (Fig. 5b). However, the inhibi-
me’ signaling axis, CD47–SIRPA, was colocalized in the tumor region and tory receptor FCGR2B was also downregulated in G4 (Fig. 5b), which
showed high expression correlation according to the spatial transcrip- might be a passenger effect resulting from the coregulatory pattern of
tomic data of CRC (Extended Data Fig. 8f,g). We observed that the CD47– these Fc receptors. In an ADCC process, FCGR3A+ NK cells are the main
SIRPA axis was highly activated in malignant cells and macrophages in G2 effectors that eliminate the antibody-bound tumor cells by the inter-
compared to other groups (Fig. 5b), suggesting that tumors in G2 were action between FCGR3A and the antibody Fc fragment50. In our study,
likely to inhibit macrophage phagocytosis. Surprisingly, another ‘do not FCGR3A was specifically expressed in the NK-GZMH subset but not in
eat me’ ligand, CD24 (ref. 49), was specifically expressed by malignant NK-XCL1 (Fig. 6a and Extended Data Fig. 8i,j). Moreover, the NK-XCL1
cells in G6 (Extended Data Fig. 8h). This phenomenon indicated that CD24 subset represented a larger proportion in G4 than in other groups
might not be induced by the pressure of high macrophage infiltration, (P = 0.0134, Fisher’s exact test) (Fig. 6b). To support the decreased Fc
and further investigation is required to understand the mechanism fully. receptor level in each macrophage and NK cell along with increased
Given that the largest proportion of plasma cells was found for plasma abundance, we correlated plasma signatures with Fc receptor
patients in G4 and plasma-IgG, but not plasma-IgA, was enriched in signatures (Methods) in TCGA datasets of CRC. We found a significant
tumors as shown previously (Fig. 1g), we hypothesized that down- negative correlation, supporting our hypothesis of repressed ADCP/
regulation of Fc gamma (Fcγ) receptors might occur in this group, ADCC capacity of macrophages and NK cells to cope with the high
attenuating the antibody-dependent cell phagocytosis (ADCP) capac- presence of antibodies in patients enriching plasma cells (Extended
ity of macrophages and the antibody-dependent cellular cytotoxicity Data Fig. 8k). Considering the enrichment of regulatory T cells and MSS
(ADCC) capacity of NK cells50. We examined the expression patterns cancer types in G6, we hypothesized that the CD8+ T cells in the patients
Nature Cancer
Expression
noitroporP
%19.15
%90.84
%63.24
%46.75
b NK-GZMH c
NK-XCL1
FCGR3A
4
3
2
NK-GZMH
1
NK-XCL1
0
UMAP_1 G4 Other
groups
d
CD8+ T cell-enriched TME Plasma cell-enriched TME
Inhibit T cell cytotoxicity (G5) Impair ADCP and ADCC (G4)
FFccγγRR
PD-L1
PD-1
PD-L2
TAM-enriched TME T -enriched TME
reg
Inhibit macrophage phagocytosis (G2) Impede cytotoxicity (G6)
MSS
enriched
T
reg
enriched
CD47 SIRPα
Impeded
cytotoxicity
2_PAMU
a
P = 2.23 × 10−308
2
1
0
G6 Other groups
erocs
yticixototyC
Fig. 6 | Characterization of potential immune evasion mechanisms. a, UMAP first quartile) showing the cytotoxicity scores of patients in G6 and other groups
plot showing reclustering of NK cells (NK-GZMH and NK-XCL1, left) and the (n = 10,459 (G6) and 15,830 (other groups)). Data were analyzed using a Student’s
expression of FCGR3A in NK subsets (right) (n = 8,805 cells). b, Bar plot showing t test (two-sided). The P value is less than the smallest nonzero normalized
the composition of NK cell subsets in G4 and other groups (n = 183 cells (G4) and floating-point number of R. d, Schematics of the dominant immune evasion
2,713 cells (other groups)). c, Box and violin plots (top and bottom quartiles with mechanisms in G5, G2, G4 and G6. FcγR, Fcγ receptor; SIRPα, signal regulatory
horizontal lines at the median and whiskers denote the range of the data that falls protein-α; TAM, tumor-associated macrophage.
within 1.5 times the interquartile range above the third quartile and below the
Analysis https://doi.org/10.1038/s43018-024-00807-z
a
b c d
e
f g
60
40
20
0
G1 G2 G3 G4 G5 G6
of G6 were not adequately activated. This hypothesis was supported We found that tumors with distinct TME immune subtypes would
by the overall lower expression of cytotoxicity genes29 in CD8+ T cells exploit different immune escape approaches, such as the upregulation
in G6 compared to other groups (Fig. 6c). of the PDL1/2–PDCD1 and CD47–SIRPA axes and downregulation of
Nature Cancer
)%(
noitroporp
egahporcam
+FNT
7.1 × 10−6
2.2 × 10−5
6 × 10−5
3 0.00071
0.00047
0.00028
2
1
0
P = 0.013
P = 3.89 × 10–5
P = 5.20 × 10–5
erocs
evitaleR
TLS classical G6 subcluster
markers score markers score
Subcluster markers
G1 G4
G2 G5
G3 G6
TLS classical markers
G1 G2 G3 G4 G5 G6
6
4
2
0
level
noisserpxe
BTL
citahpmyL 1XORP-CE sllec
lailG
5PBAF-biF NTSOP-biF 01LCXC-VEH 9LNTB-yrallipaC 4AC-yrallipaC 5AJG-yretrA ELES-VEH 2NLBF-yretrA citahpmyL EVYL-CE 1RKCA-nieV etycireP 91LCC-biF elcsum
htoomS
5PAFM-biF 1FGI-biF A5TNW-biF 1PPS-orcaM 1NCF-onoM CQ1C-orcaM 1EVYL-orcaM CDp A9CELC-CDc C1DC-CDc 3PMAL-CDc AgI-amsalP GgI-amsalP Tδγ-8DC R7LI-8DC 31LCXC-4DC 31LCXC-8DC KMZG-8DC HMZG-KN 1LCX-KN 51GSI-8DC 51GSI-orcaM A71LI-4DC 3PXOF-
T
ger
TIAM-8DC 1AXNA-4DC 7RCC-4DC DgI-B 1A4SM-B sCLI PMRL-B
0 0.4 0.8 0 0.20.40.6
TLS
650 µm
1.00
0.75
LTB 0.50
expression
3
0.25 2
P = 0.0028
1
0
0
0 50 100 150
Time (months)
Myeloid leukocyte migration 13
Neutrophil chemotaxis 9
Cytokine-mediated signaling pathway 18
Epithelial cell migration 15
EC migration 13
Response to TNF 12
Cellular response to corticosteroid stimulus 6
Cellular response to TNF 11
0 1 2 3
−log (adjusted P) 10
ytilibaborp
lavivruS
G6 signature genes = high
G6 signature genes = low
Upregulated pathways in malignant cells of G6
Analysis https://doi.org/10.1038/s43018-024-00807-z
Fig. 7 | TLS characterization by spatial transcriptome and single-cell Extended Data Fig. 9b. e, Violin plot showing LTB expression in each cell subset
transcriptome analyses. a, Colocalization of TLS markers and G6 markers (n = 12, 383, 772, 580, 78, 294, 97, 919, 454, 164, 268, 747, 3,022, 112, 769, 753, 1,888,
revealed by spatial transcriptomics. Left, hematoxylin–eosin staining of tumor 6,314, 6,959, 9,117, 14,510, 2,262, 1,346, 317, 2,947, 1,362, 12,366, 5,818, 5,309, 3,559,
tissue sections. The TLS region is indicated by a dashed circle. Middle, scores of 4,631, 7,208, 9,324, 1,905, 1,282, 835, 959, 5,390, 14,496, 1,818, 7,973, 6,865, 2,923,
the 12 TLS classical markers in spatial transcriptomic spots. Right, scores of 65 G6 8,990, 581 and 1,512 cells from left to right). f, Box plot (top and bottom quartiles
subcluster markers in spatial transcriptomic spots. This pattern was replicated with horizontal lines at the median and whiskers denote the range of the data that
in six patients, and two of them are shown in Extended Data Fig. 9a. b, Kaplan– falls within 1.5 times the interquartile range above the third quartile and below
Meier plot showing overall survival in patients stratified based on the expression the first quartile) showing the TNF+ macrophage proportion in all macrophages
level of G6 signature genes (n = 423 (high), 224 (low)). Data were analyzed using of patients from different groups (n = 10 (G1), 23 (G2), 10 (G3), 15 (G4), 25 (G5)
Cox regression. c, Box plots (top and bottom quartiles with horizontal lines at and 33 (G6)). Data were analyzed using a Wilcoxon’s test (two-sided). g, Lollipop
the median) showing the scores of marker genes of the TLS regions relative to plot showing upregulated pathways in malignant cells of G6 in contrast to
non-TLS regions in spatial transcriptomic slides (n = 6). Data were analyzed using the remaining groups. Numbers in the dots indicate gene counts matched to
a Student’s t test (paired, two-sided). d, LTB expression in spatial transcriptomic corresponding biological pathways. Data were from an overrepresentation
spots. This pattern was replicated in six patients, and two of them are shown in analysis (BH adjustment).
Fcγ receptors and cytotoxicity genes (Fig. 6d). Patient stratification first detected the P-value distribution of these genes in the comparisons
with different immune evasion mechanisms would provide valuable of tumor and paracancerous tissues for each cell type and compared
insights to guide immunotherapy development tailored for different these distributions to an expected uniform distribution. Then, we used
patient groups. a lambda statistic to evaluate inflated deviations (Methods). The larg-
est inflated deviations from the expected distribution were observed
Group 6 is associated with tertiary lymphoid structures for fibroblasts and ECs (Fig. 8a,b), suggesting that stromal cells were
Multiple B cell subsets, including B-IgD, B-MS4A1 and B-LRMP, were the major effector cell types of CRC risk genes. Notably, this pattern
enriched in patients in G6. Considering that the abundance of B cells was consistent among the six TME groups of patients (Extended Data
within the TME is highly dependent on the presence of tertiary lym- Fig. 10b). Upon close inspection of risk genes with high levels of expres-
phoid structures (TLSs)51, using spatial transcriptomic data from CRC sion alteration, we inferred that most risk genes might be related to CRC
samples19,52, we found that the signature genes of G6 were colocalized susceptibility by affecting one or a few specific cell types (Fig. 8c). For
with the signature of the reported 12 TLS classical markers53 (Fig. 7a and instance, upregulation of COL4A2 in cancer tissues compared to para-
Extended Data Fig. 9a). The presence of TLSs is known to be associated cancerous tissues was mainly observed in the cancer stroma (Fig. 8d),
with a better prognosis, and our survival analysis confirmed a positive consistent with a previous study58. COL4A2 has been reported to have
association between G6 signature genes and longer overall survival a role in a wide range of biological processes, including cancer patho-
(Fig. 7b). These analyses indicated that the TME of G6 was likely associ- genesis and progression59. Our analysis revealed that the impact of
ated with TLSs. We next evaluated whether the signature genes of G6 COL4A2 on CRC susceptibility is mediated through the cancer stroma.
performed better as a TLS indicator than the reported 12 markers and Furthermore, risk genes showing differential expression in fibroblasts
signature genes of the other TME groups. We calculated the signature were related to EMT, and risk genes associated with ECs were enriched
score within and without TLS regions based on the expression of the in extracellular matrix organization and PDGFB signaling (Fig. 8e).
marker genes (Methods). The results demonstrated that the signature These analyses suggest that these pathways might be involved in the
genes of G6 achieved the best performance in distinguishing TLS from genetic regulation of stromal cells and may further influence the indi-
the non-TLS regions (P < 0.05, paired Student’s t test, two-sided; Fig. 7c). vidual risk of CRC.
It has been previously shown that LTB released by CD8+ T and NK Next, by comparing risk genes significantly altered in the six TME
cells contributes to the transition from postcapillary venules into HEVs, groups (Methods), we identified 94 group-specific cell type–gene pairs
facilitating the generation of T lymphocyte niches35 and TLSs53. Here, (Extended Data Fig. 10c and Supplementary Table 9). For example,
we confirmed the expression of LTB specifically in TLS regions (Fig. 7d upregulation of the IFN-induced nuclear protein SP110 was observed
and Extended Data Fig. 9b) and observed that its high expression was only in CD8+ T cells of G5 (Extended Data Fig. 10d), which might be
prevalent within the cell subsets enriched in G6, including B cells, CD4+ relevant to its reported function in lymphocyte immunity60. Overall,
T cells and a mucosal-associated invariant T (MAIT) subset, rather our analysis provides important insights into the cellular mecha-
than in other CD8+ T and NK subsets in both our atlas and validation nisms of genes associated with CRC susceptibility. Additional experi-
cohort (Fig. 7e and Extended Data Fig. 10a). This suggests that these mental validations are needed to elucidate their function in cancer
cell subsets might aid TLS formation through the expression of LTB. development.
Furthermore, macrophages were also reported to trigger lymphoid
tissue formation through a TNF-dependent pathway54. We observed Discussion
a higher proportion of TNF+ macrophages in patients of G6 (Fig. 7f), In this study, we established a high-quality cell atlas for colorectal tissues
and genes associated with ‘response to TNF’ were upregulated in the and characterized transcriptional remodeling in tumors compared to
malignant cells of G6 (Fig. 7g), indicating that the TNF signaling path- local inflammation. Notably, we identified a rare HEV-like endothelial
way was highly activated in G6. In summary, our findings suggest that subset (HEV-CXCL10) that correlated with T cell recruitment. However,
TLS regions are likely enriched in the TME of patients in G6, and immune limited by the sampling bias of the 10x Genomics technology, we were not
cell subsets enriched in this group might contribute to TLS formation able to collect and annotate neutrophils. This requires particular attention
by releasing LTB. These require in-depth functional validation. in future studies. The atlas is accessible at http://118.190.148.166:8918/,
allowing for more in-depth functional studies.
Stromal cells show enriched expression changes of CRC risk Most importantly, based on the individual-level abundance of
genes the TME cell subsets, we constructed a classification system dividing
CRC has a strong heritable basis55, with 12–13% susceptibility accounted patients into six groups using an unsupervised approach. We observed
for by genetic effects56. Large genome-wide association studies (GWASs) that malignant cells could downregulate cytokine-related genes and
have underscored the contribution of genetic polymorphisms to CRC express ligands such as COL1A1 to recruit fibroblasts to block the
susceptibility57. To explore the effector cell types of these genetic regu- infiltration of immune cells. Meanwhile, upregulation of the PDL1/2–
lations, we acquired all mapped genes of CRC risk loci (Methods). We PDCD1 and CD47–SIRPA axes and downregulation of Fcγ receptors
Nature Cancer
Analysis https://doi.org/10.1038/s43018-024-00807-z
were activated to different extents to help tumor cells escape from Thus far, GWASs have revealed hundreds of genetic loci associ-
immune surveillance in different patient groups. This suggests that ated with CRC susceptibility. However, the cellular mechanisms of
different immune escape mechanisms correspond to different TMEs. those genetic risk genes are less studied. Our study highlights that
Thus, evaluating the dynamic adaptive evolution of malignant cells in transcriptional alterations in fibroblasts and ECs are associated with
response to the TME is encouraged in future CRC studies. these CRC risk genes, inferring a genetic-driven pathogenic phenotype
The presence of TLSs is associated with a better prognosis of stromal cells before atypical epithelial cells appear.
because of their function in recruiting and activating immune cells. We must acknowledge possible confounders and limitations in
In this study, we show that CD4+ T cells, follicular B cells and MAIT cells this study. The influence of batch effects on the results is the most
are the source of LTB, which might have an important role in trigger- notable concern for all data integration studies. As we collected data
ing TLS formation. We did not observe NK cells expressing LTB, as from multiple data sources, differences in paracancerous tissue sam-
reported in a mouse model study35. Additionally, our results support pling (that is, distance from the edge of the tumor) and sequencing
those of a mouse experiment showing that TNF+ macrophages might (only one dataset is from single-nucleus sequencing) might introduce
contribute to this process54 and provide evidence from real-world batch effects, despite only data from 10x being included in the atlas.
human data. Through extensive computational analysis, we have ruled out the
Nature Cancer
)egnahc
dlof(gol
2
d
c
1LNBM 02BTBZ 5PBKF 1PA3KIP 1SAIP 2MCC 12SPR 3LPR 2DNCC B4PPNI MKP 1MDRP 2KCOPS 38DC LNRTEM 9CADH LVPC 4FCT 4BRLIL 1PAGRS D2KMAC 1PASA 1PBF FATIL C1ABUT 2A3CLS A1ZAB 1PBNTD 2BRDA 2A4LOC 2PMM 1A51LOC RSNI A701MAF 3−2XKN 71HDCP 1HNIPRES 1CMAL 9STMADA BFGDP 8HOTA 13BAR 1TSGM 1HPSH 1PEPCS 3DOS 4PMB 28010CNIL 41MIMS NACV 1MERG 8TRK 5KCOD 2MDAC
Fib
100
EC
Mono/macro
75 B
Mast
Glial
50 DC
CD4
ILC
25
Plasma
CD8
0 NK
0 0.5 1.0 1.5 2.0 0 10 20 30 40
−log 10 (expected P value) Lambda
B
Plasma
CD4 1.5
CD8
ILC
DC 0
Mono/macro
Mast
−1.5
EC
Fib
Glial
)eulav
P
devresbo(
gol−
01
a b
4
3
2
1
0
P
B las ma C D4 C D8N
M
K
on
IL
o
C
/
macro D C Mast E C Fib Glial
e
Risk genes in fibroblasts Risk genes in ECs
Artery morphogenesis 6 Extracellular matrix organization 9
Regulation of EMT 6 Glycolytic process 5
Glucose catabolic process to pyruvate 3 PDGFB signaling pathway 3
Canonical glycolysis 3 Cell−substrate adhesion 9
EMT 6 EC differentiation 5
0 0.5 1.0 1.5 0 0.5 1.0 1.5 2.0
−log (adjusted P value) −log (adjusted P value)
10 10
level
noisserpxE
COL4A2
4
3
2
1
0
Fib
E
C
level
noisserpxE Paracancerous
Tumor
Fig. 8 | Transcriptional alterations of CRC genetic risk genes. a, Quantile– n = 28,158, 49,042, 54,671, 41,247, 4,236, 1,263, 38,132, 7,769, 5,186, 8,337, 29,998
quantile plot showing the nominal P-value distribution derived from an expected and 1,693 cells from left to right) and in fibroblasts and ECs from tumors and
distribution (dashed line) (n = 288, 266, 193, 149, 120, 187, 198, 119, 143, 112, 99 and paracancerous tissues (bottom; n = 14,981, 15,017, 4,349 and 3,988 cells from left
93 genes from top to bottom). b, Bar plot showing lambda statistics for each cell to right). e, Lollipop plots showing enriched pathways of risk genes differentially
type (n = 288, 266, 193, 149, 120, 187, 198, 119, 143, 112, 99 and 93 genes from top expressed in fibroblasts (left) and ECs (right). Numbers in the dots indicate
to bottom). c, Heatmap showing the log(fold change) of each risk gene in each gene counts matched to corresponding biological pathways. Data were from an
2
cell type. d, Violin plot showing the expression of COL4A2 in each cell type (top; overrepresentation analysis (BH adjustment).
Analysis https://doi.org/10.1038/s43018-024-00807-z
impact of batch effects on our findings, in line with previous reports Clustering and cell-type identification
that the variation between pathological status and different individuals Seurat (v4.3)62 and Harmony (v0.1.1)63 were applied to analyze the
far exceeds the variation introduced by batch effects11. Additionally, expression matrix following the workflow below:
by taking the CRC-SG1 dataset as an example, we calculated the cell
1. The count matrix was normalized with default settings, and
subset proportions for each biological replicate and assigned them to
2,000 shared top variable genes identified in each of the
our classification groups. We found that most of the replicates (79.3%)
datasets were scaled and used for PCA.
were annotated to the same group as those using all cells from the cor-
2. The first 50 PCs were calculated and corrected by different
responding patient (Supplementary Table 10). The analysis of those
datasets and donors, using Harmony to regress out the
biological replicates indicated that there were cellular composition
variations introduced by different studies and donors.
heterogeneities in different sectors of the same tumor. Therefore,
3. Harmony-corrected PC1–PC50 were used to construct a
sampling from multiple sites of the tumor is recommended for a more
K-nearest neighbor graph with K = 30 and to identify unsuper-
accurate patient classification. Lastly, we acknowledge that functional
vised cell clusters. Resolutions ranging from 0.1 to 0.5 were
experimental validation is still needed to support our results obtained
chosen for different cell cluster identifications. Cluster-specific
from bioinformatic profiling, which is the major limitation of this study
gene markers were identified by the FindMarker function in
and may see progress in the future.
Seurat with adjusted P < 0.05 and log(fold change) > 0.25.
In conclusion, this study comprehensively interrogates complex 2
4. For dimension reduction, a Uniform Manifold Approximation
approaches in single-cell characterization, which could serve as a
and Projection (UMAP) was implemented on 1–50 Harmony
valuable resource. Our stratification of patients based on TME hetero-
embeddings to visualize cell clustering.
geneities and different dominant immune evasion mechanisms
5. Cell types were identified mainly based on the expression
provides insights into different treatment strategies and might help
pattern of canonical markers for major cell types and well-
with the development of personalized medicine for CRC.
known or newly identified markers for cell subsets. We took
cell annotations inherited from each of the collected datasets
Methods
as a reference for major cell-type confirmation.
Single-cell RNA-sequencing data collection and quality
control We first carried out this workflow on all single cells to identify
We collected single-cell transcriptomic data from 15 public datasets major cell types. Then, we reapplied the workflow to identify vari-
comprising 427 human colon and rectum samples from 192 donors able genes across cells within the same major cluster and built cell
divided into six groups, including healthy, uninflamed, inflamed, embeddings for subset identification. For instance, to annotate stromal
polyp, paracancerous and tumor samples7,9–17,19,20 (Supplementary cells, we first classified the cells into fibroblasts, glial cells and ECs.
Table 1). Samples from the inflamed region and those from the unaf- By applying the workflow to the fibroblast and EC clusters, we further
fected colorectal regions of patients with UC served as the inflamed identified 22 subsets. In total, we identified 58 subsets in 873,392 cells,
and uninflamed samples, respectively. Biopsy specimens taken from among which 671,192 cells expressing >800 genes were included in
the tumor center and adjacent normal region in patients diagnosed downstream analysis.
with CRC were grouped as the tumor and paracancerous samples,
respectively. In total, we collected data from 1,144,726 cells with or Validation data collection and cell subset annotation
without quality control. A total of 31 new patients were used as a validation cohort, and their
To annotate cell subsets accurately, we excluded cells with single-cell transcriptomic data were acquired from three public data-
<800 detected genes and with >20% mitochondrial counts for fibro- sets21 (Supplementary Table 2). After filtering out cells from lymph
blasts, ECs, monocytes/macrophages and DCs for cluster identification nodes and cells expressing <800 genes, 201,892 nonepithelial/
and annotation. For the remaining cell types, cells with <500 detected nonmalignant cells and 26,967 epithelial/malignant cells were left.
genes were excluded. We filtered out potential doublets, which were We next annotated the nonepithelial/nonmalignant cells by training
identified by the coexpression of different well-known cell-type markers, a machine-learning model using the TOSICA tool (v.1.0.0)64, taking the
leaving 873,392 cells with identified subsets. previously annotated 507,268 nonepithelial/nonmalignant cells as a
reference. The training parameters were set as follows: batch size = 64
TCGA data collection and training epochs = 15. Subsequently, we used this trained model to
We collected gene expression data in TPM format, patients’ age and predict the cell subset labels for each cell within the validation cohort.
sex, and clinical outcome information of CRC from TCGA database
(https://portal.gdc.cancer.gov/) using the R package TCGAbiolinks Cell-type abundance evaluation and comparison
(v2.22.4)61 in December 2022, under the projects TCGA-COAD (colon Samples covering all cell types and with >200 cells were considered
adenocarcinoma) and TCGA-READ (rectum adenocarcinoma). in this analysis. Cells belonging to each major cell type were divided
by the total nonepithelial/malignant cells or total immune cells for
Spatial transcriptomic data collection and TLS annotation the analysis of immune cell subsets. A Student’s t test (two-sided) was
We downloaded spatial resolved transcriptomic slides from public applied to compare the cell-type abundance between samples from
studies19,52. After excluding two slides from which we could not observe different tissues.
obvious TLS regions, six slides were left for downstream analysis.
TLS regions were identified according to two criteria: (1) presence Tissue similarity evaluation of cell types
of aggregated lymphocytes in the hematoxylin–eosin image and To evaluate the similarity between different tissues for each cell subset,
(2) copresentation of spots expressing T cell markers (CD3D, CD3E, we introduced a Bhattacharyya distance metric24,25 by taking the top 30
CD3G), B cell markers (CD19, MS4A1) and follicular DC markers (CR2, PCs from the Harmony embeddings as input. Only clusters with >200
FCER2). The online spatial transcriptomic dataset with subcellular cells in each group were included in the analysis. We randomly selected
resolution can be accessed at https://info.vizgen.com/ffpe-showcas 100 permuted sets of 50 cells from each group of tissues and all cells
e?submissionGuid=b22e6bed-bbe3-4719-84ea-920fac6c66cf. Two regardless of grouping information as controls. We then calculated the
spatial transcriptomic slides with a distinct boundary between distances for each permuted set and compared them to the correspond-
the tumor and the adjacent normal region were acquired from a ing controls. We applied a downsampling strategy to limit the influence
public study23. of different sample sizes in the comparison between tumors, inflamed
Nature Cancer
Analysis https://doi.org/10.1038/s43018-024-00807-z
tissues and polyps. We randomly dropped cells from tumor samples to Assigning patients of the validation cohort to TME groups
make the cell numbers equal to those from inflamed tissues or polyps We calculated the proportions of different cell subsets for each
ten times to obtain ten subsets for each cell type. Then, we randomly patient. Then, we scaled the query data of the validation cohort to
selected ten permuted sets of 50 cells from each of the ten subsets the original data and computed the Spearman’s correlation coeffi-
and calculated the distances for the 100 permuted sets as previously cient between the scaled proportions of each patient in the validation
mentioned. A larger increase indicates less similarity between tissues. cohort and those in the original atlas. Each patient in the validation
cohort was assigned to the group with the highest average Spear-
Differential expression and enrichment analyses man’s correlation coefficient with the corresponding group in the
To perform differential expression analysis, we applied Wilcoxon original atlas.
rank-sum tests on the genes expressed in >25% of the cells in either
group being compared. Genes with adjusted P < 0.05 and absolute Signature gene identification and scoring
log(fold change) > 0.25 were considered differentially expressed We first filtered out the marker genes of each cell subset with adjusted
2
genes. For enrichment analysis, we used the R package clusterProfiler P > 1 × 10−4. Then, we defined the top ten genes upregulated in each
(v4.2.2)65 to identify overrepresented Gene Ontology terms, and subset based on average log(fold change) values and grouped these
2
Benjamini–Hochberg (BH)-adjusted P values of <0.05 were considered genes based on their preference in each TME group as group signature
statistically significant. genes. To show the overall expression pattern of signature genes in the
spots of spatial transcriptomic slides and for patient grouping in sur-
Tissue preference evaluation of cell subsets vival analysis, we applied the AddModuleScore function in the Seurat
To detect the tissue preference of each cell subset, we calculated package on the normalized expression values of signature genes to
the Ro/e, where the expected cell numbers were obtained using the obtain a score for each spot/patient.
chi-square test, as previously described29,30. To show the signature of the 12 classical TLS markers (CCL2, CCL3,
CCL4, CCL5, CCL8, CCL18, CCL19, CCL21, CXCL9, CXCL10, CXCL11 and
Extracellular regulatory signal analysis CXCL13)53 in spatial transcriptomic data and to compare the expression
NicheNet (v1.1.1)66, which can powerfully predict ligand–target genes patterns of co-inhibitory molecules44 and the cytotoxic capacity29 of
from transcriptomic cell data, was applied to investigate the regula- CD8+ T cells from the six TME groups, we applied the AddModuleScore
tory ligands of potential target genes in certain cell subsets to obtain function to the expression values of each dot/cell.
the top 15 regulatory ligand genes and inferred ligand–target pairs. A To evaluate the signature of plasma cells, macrophages and
heatmap was used to show the regulatory potential of all prioritized NK cells, we first obtained the marker genes of plasma cells, macro-
interaction pairs. phages and NK cells in contrast to other major cell types by using
the FindMarkers function of the Seurat package. We next applied the
Transcription factor regulon analysis AddModuleScore function to the normalized gene expression values
We used the R package SCENIC (v1.3.1)67 to identify the regulatory of each of the top ten marker genes in the COAD and READ datasets
transcription factor genes (also called regulons) of cell subsets. The to indicate the relative abundance of plasma cells, macrophages and
regulatory activity (measured in area under the curve) and expression NK cells in each tumor sample.
of the prioritized transcription factor genes in HEV-CXCL10 were com- The AddModuleScore function was also applied to obtain the
pared to those in other endothelial subsets, using Wilcoxon rank-sum overall signature of activating Fc receptors (FCGR1A, FCRG2A, FCGR3A
tests to obtain HEV-CXCL10-specific regulons. and FCGR3B) in TCGA datasets.
Hierarchical clustering analysis Survival analysis
We used the R package ‘pheatmap’ (v1.0.12) to cluster the patients. We used the R packages ‘survival’ (v3.5.5) and ‘survminer’ (v0.4.9) for
Euclidean distances between patients were calculated based on the cell survival analysis. We grouped patients collected from TCGA based on
subset abundance scaled across patients, and clustering was performed the module score of signature genes using the ‘surv_cutpoint’ func-
on the distance with the ‘ward.D’ approach. tion. The ‘ggsurvplot’ function was then applied for survival curve
visualization and comparison. Significant differences were indicated
Matching with the CMS/iCMS classification by P < 0.05 in a Cox proportional hazards regression model correcting
To match our classification with the CMS classification of CRC, we col- for age and sex effects.
lected CMS marker genes from a published paper68, in which patients
were classified into five groups based on their ‘bulk’ transcriptomic Cell–cell interaction identification
data. Two groups were clustered together as CMS2 according to the We used CellChat (v1.6.1)69 to infer cell–cell interactions between
CMS classification4. The signature genes for each CMS group were ‘sender’ and ‘receiver’ cell clusters. We considered only ligands
defined as genes for which the largest fold changes were reported. expressed in >30% of cells of the sender cell type, and ligand–recep-
Next, we constructed pseudo-bulk data by randomly selecting 1,000 tor pairs with P < 0.05 were considered in the downstream analysis
cells from each patient with >1,000 cells or all cells from each patient and visualization.
with <1,000 cells and merging the count data for each patient. After
normalization, we used the AddModuleScore function of the Seurat Correlation between plasma and Fc receptor signatures
package on the pseudo-bulk data with the CMS signature genes to To evaluate the association between plasma abundance and Fc recep-
obtain CMS scores for all patients. tor levels in macrophages and NK cells in TCGA datasets, we first
A total of 715 iCMS marker genes were acquired from a published regressed out the contribution of the macrophage/NK cell abundance
paper21. We built pseudo-bulk data for epithelial/malignant cells in the difference on the variation of Fc receptor expression by fitting a
tumor and paracancerous tissues of each patient by randomly selecting linear regression model in which the Fc receptor signature was
500 cells from each patient with >500 cells or all cells from each patient the independent variable and the macrophage signature and NK
with <500 but >200 cells and merging the count data for each patient. cell signature were the dependent variables to obtain the residuals.
Next, by applying the AddModuleScore function in Seurat to the Next, a Pearson’s correlation analysis was performed between plasma
normalized expression data, we determined the relative scores of the signatures and the residuals. A P value of <0.05 was considered
marker genes in each group. significant.
Nature Cancer
