---
source_path: /mnt/c/Users/Administrator/Zotero/storage/7SZPTR78/Li 等 - 2023 - Non-cell-autonomous cancer progression from chromosomal instability.pdf
ingested: 2026-04-23
sha256: 33ce73c56c50bfde
---

Article
Non-cell-autonomous cancer progression
from chromosomal instability
https://doi.org/10.1038/s41586-023-06464-z Jun Li1,2,14, Melissa J. Hubisz3,4,5,6,14, Ethan M. Earlie3,4,5,14, Mercedes A. Duran1,2,14,
Christy Hong1,2, Austin A. Varela3,4,5, Emanuele Lettera1,2, Matthew Deyell3,4,5,
Received: 9 December 2021
Bernardo Tavora7, Jonathan J. Havel7, Su M. Phyu8, Amit Dipak Amin9,10, Karolina Budre3,4,5,
Accepted: 20 July 2023 Erina Kamiya3,4,5, Julie-Ann Cavallo1,2, Christopher Garris11,12, Simon Powell2,
Jorge S. Reis-Filho13, Hannah Wen13, Sarah Bettigole7, Atif J. Khan2, Benjamin Izar9,10,
Published online: 23 August 2023
Eileen E. Parkes8, Ashley M. Laughney3,4,5,15 ✉ & Samuel F. Bakhoum1,2,15 ✉
Open access
Check for updates
Chromosomal instability (CIN) is a driver of cancer metastasis1–4, yet the extent to
which this effect depends on the immune system remains unknown. Using Contact
Tracing—a newly developed, validated and benchmarked tool to infer the nature
and conditional dependence of cell–cell interactions from single-cell transcriptomic
data—we show that CIN-induced chronic activation of the cGAS–STING pathway
promotes downstream signal re-wiring in cancer cells, leading to a pro-metastatic
tumour microenvironment. This re-wiring is manifested by type I interferon
tachyphylaxis selectively downstream of STING and a corresponding increase in
cancer cell-derived endoplasmic reticulum (ER) stress response. Reversal of CIN,
depletion of cancer cell STING or inhibition of ER stress response signalling abrogates
CIN-dependent effects on the tumour microenvironment and suppresses metastasis
in immune competent, but not severely immune compromised, settings. Treatment
with STING inhibitors reduces CIN-driven metastasis in melanoma, breast and colorectal
cancers in a manner dependent on tumour cell-intrinsic STING. Finally, we show that CIN
and pervasive cGAS activation in micronuclei are associated with ER stress signalling,
immune suppression and metastasis in human triple-negative breast cancer,
highlighting a viable strategy to identify and therapeutically intervene in tumours
spurred by CIN-induced inflammation.
Chromosomal instability (CIN) is a cancer hallmark5 that is associ- the effect of CIN on tumour progression is cancer cell autonomous or
ated with therapeutic resistance6, immune evasion7,8 and metastasis2. rather dependent on the immune system. Moreover, it is unclear how
CIN arises from ongoing errors in chromosome segregation during chromosomally unstable tumours adapt to CIN and evade immune
mitosis9,10. In normal cells, chromosome missegregation is poorly surveillance that would arise from cGAS–STING activation and a down-
tolerated11 and can suppress oncogenic transformation12,13. Yet, stream type I interferon (IFN) response20.
advanced human cancers are often characterized by elevated rates
of chromosome missegregation and aneuploidy2,14,15, invoking adap-
tive processes that allow tumours to withstand and co-opt CIN3. Using Immune dependence of CIN-driven metastasis
isogenic models that enable genetic manipulation of chromosome To interrogate the influence of the immune system on CIN-driven metas-
missegregation rates in cancer cells16, we have previously shown that tasis, we used four syngeneic metastatic cancer models, including
CIN promotes metastasis by inducing a cytosolic double-stranded DNA triple-negative breast cancer (TNBC) (4T1 and EO771.LMB), colorectal
(dsDNA) response in tumour cells, mediated by the cGAS–STING innate adenocarcinoma (CT26) and melanoma (B16F10). All models exhibited
immune pathway2. Errors in chromosome segregation lead to the for- elevated rates of chromosome segregation errors during anaphase
mation of rupture-prone micronuclei17 and exposure of genomic dsDNA and a preponderance of micronuclei (Extended Data Fig. 1a–c). Highly
to the cytoplasm2,18,19. These findings were based on partially immune metastatic melanoma cells (B16F10) had significantly higher rates
compromised tumour models2; thus, it remained unknown whether of CIN compared with their less metastatic parental counterparts
1Human Oncology and Pathogenesis Program, Memorial Sloan Kettering Cancer Center, New York, NY, USA. 2Department of Radiation Oncology, Memorial Sloan Kettering Cancer Center,
New York, NY, USA. 3Department of Physiology, Biophysics, and Systems Biology, Weill Cornell Medicine, New York, NY, USA. 4Meyer Cancer Center, Weill Cornell Medicine, New York, NY, USA.
5Institute for Computational Biomedicine, Weill Cornell Medicine, New York, NY, USA. 6Bioinformatics Facility, Institute of Biotechnology, Cornell University, Ithaca, NY, USA. 7Volastra
Therapeutics Inc., New York, NY, USA. 8Department of Oncology, Medical Sciences Division, University of Oxford, Oxford, UK. 9Columbia Center for Translational Immunology, New York, NY, USA.
10Division of Hematology and Oncology, Columbia University Medical Center, New York, NY, USA. 11Department of Pathology, Harvard Medical School, Boston, MA, USA. 12Center for Systems
Biology, Massachusetts General Hospital, Boston, MA, USA. 13Department of Pathology and Laboratory Medicine, Memorial Sloan Kettering Cancer Center, New York, NY, USA. 14These authors
contributed equally: Jun Li, Melissa J. Hubisz, Ethan M. Earlie, Mercedes A. Duran. 15These authors jointly supervised this work: Ashley M. Laughney, Samuel F. Bakhoum. ✉e-mail: ashley.
laughney@gmail.com; samuel.bakhoum@gmail.com
1080 | Nature | Vol 620 | 31 August 2023
a b c
*** * Control **** Cgas KO
d e f
C57BL/6 NSG
**** **** ***
g h i j
Control Sting1 KD *** *
Sting1 sg – + + + +
Sting1 OE – – + ++
4 mm STING
COX IV
(B16F0 and B16F1, Extended Data Fig. 1b,c). In all models, we observed difference in NSG hosts (Fig. 1a). We then depleted Cgas or Sting1 from
CIN-dependent activation of cGAS–STING, as evidenced by cGAS locali- CINhigh 4T1, B16F10, EO771.LMB and CT26 cells using CRISPR–Cas9
zation in micronuclei, measurable cGAMP levels from cell lysates in a knockout (KO) (Extended Data Fig. 1e). Tail-vein inoculation or ortho-
manner dependent on cGAS expression and detectable STING protein topic transplantation of WT, Cgas-KO or Sting1-KO cells in BALB/c (4T1
levels (Extended Data Fig. 1d–f). We also manipulated CIN levels in 4T1 and CT26) or C57BL/6 (B16F10 and EO771.LMB) led to a significant
cells through expression of the non-motile kinesin-13 proteins, Kif2b reduction in lung colonization and metastasis as assessed directly
or MCAK16, either of which led to significant reductions in anaphase through enumeration of surface lung metastases or using biolumi-
chromosome missegregation compared with wild-type (WT) cells, nescence imaging (Fig. 1b–f and Extended Data Fig. 1h,i). Strikingly,
or cells expressing a dominant-negative MCAK mutant (dnMCAK)21 this phenotype was entirely dependent on the immune system, as
(Extended Data Fig. 1g). Expression of Kif2a, a kinesin-13 family mem- transplantation of these cells in NSG hosts completely abolished the
ber that possesses microtubule depolymerizing activity but lacks a effect of Cgas or Sting1 KO on metastasis (Fig. 1b–f and Extended Data
centromere or kinetochore targeting domain, had no impact on CIN Fig. 1h,i). Loss of cancer cell Sting1 did not impact primary tumour
(Extended Data Fig. 1g). size, whereas Cgas-KO tumours were slightly smaller compared with
We next transplanted CINhigh (WT, Kif2a or dnMCAK expressing) and control tumours, as previously reported22 (Extended Data Fig. 1j). To
CINlow (Kif2b or MCAK expressing) 4T1 tumours in immune competent rule out potential off-target effects from CRISPR–Cas9-mediated KO,
(BALB/c) and severely immune compromised (NOD-scid IL2Rγnull, there- we depleted Sting1 using short hairpin RNA (shRNA) and observed a
after referred to as NSG) mice. There was an 11-fold difference in the similar reduction in lung metastasis with no impact on primary tumour
median number of surface lung metastases in the BALB/c mice when formation (Fig. 1g–i and Extended Data Fig. 1k). Furthermore, comple-
comparing CINhigh and CINlow tumours as opposed to only a 1.1-fold mentation of Sting1-KO cells with constructs expressing WT Sting1 using
Nature | Vol 620 | 31 August 2023 | 1081
lortnoC
BALB/c NSG
lortnoC
OK sagC
OK
1gnitS
200
150
100 50
0 0
hgihNIC wolNIC hgihNIC wolNIC lortnoC OK
sagC
OK
1gnitS
lortnoC OK
sagC
OK
1gnitS
100
25
20 10
sesatsatem
gnul ecafruS
2.5 15 2.0
10
1.5
1.0 5 0.5
0 0
0 10 20 30 0 5 10 15
Days Days
)000,1×(
ILB evitaleR
20 300
15 200
10 100 5
0 0
sesatsatem
gnul ecafruS
150 300
100 200
50 100
0 0
sesatsatem
gnul
ecafruS
40 200
30 150
20 100
10 50
0 0
sesatsatem
gnul
ecafruS
20
15
10
5
0
sesatsatem
gnul
ecafruS
150
100
50
0
sesatsatem
gnul
ecafruS
250
200
150
100
50
0
)3mm(
emulov
ruomut
yramirP
4T1 4T1 CT26
BALB/c NSG BALB/c NSG BALB/c NSG
Control Cgas KO
0 0.80 1.4
×107 ×108
(p s–1 cm–2 sr–1)
EO771.LMB B16F10 B16F10
C57BL/6 NSG C57BL/6 NSG
37 kDa
15 kDa
lortnoC
lortnoC
OK
sagC
DK
1gnitS
OK
1gnitS
lortnoC OK
sagC
lortnoC
OK
1gnitS
DK
1gnitS
lortnoC OK
sagC
OK
1gnitS
lortnoC OK
sagC
OK
1gnitS
25
Fig. 1 | CIN drives cancer progression through tumour cell non-autonomous per group. f, Representative lung images from C57BL/6 or NSG animals tail-
mechanisms. a, Number of surface lung metastases arising from orthotopically vein-injected with control or Sting1-KO B16F10 cells. g, Volume of resected
transplanted and resected CINhigh or CINlow 4T1 tumours in BALB/c hosts (n = 19 orthotopically transplanted control and Sting1-depleted primary 4T1 tumours;
and 23 animals for CINlow and CINhigh, respectively) or from tail-vein-injected CINhigh n = 8–16 mice per condition. h, Number of surface lung metastases in animals
or CINlow 4T1 cells in NSG hosts (n = 10); bars represent the median; ***P < 0.001, arising after tumour resection; lines in the plot represent the median; *P < 0.05,
*P < 0.05, two-sided Mann–Whitney test. b, Normalized bioluminescence (BLI) two-sided t-test after testing for normality. i, Representative haematoxylin and
signal from BALB/c or NSG mice tail-vein injected with 4T1 control and Cgas-KO eosin (H&E)-stained lungs 3 weeks after resection of control or Sting1-depleted
cells (n = 10 animals per condition) and representative bioluminescence orthotopically transplanted 4T1 tumours. j, Number of surface lung metastases
images on days 5 and 8 for BALB/c and NSG mice, respectively; mean ± s.e.m. arising from tail-vein injection of 4T1 control, Sting1-KO and Sting1-KO cells with
c–e, Number of surface lung metastases upon tail-vein injection of control, exogenous overexpression (OE) of STING and immunoblot for STING and CoxIV
Cgas-KO or Sting1-KO CT26 (c), EO771.LMB (d) or B16F10 cells (e) into immune of the cells; lines in the plot represent the median; ***P < 0.001, two-sided Mann–
competent hosts (BALB/c for CT26, C57BL/6 for EO771.LMB and B16F10) or NSG Whitney test. KD, knockdown; p s−1 cm−2 sr−1, photon second–1 centimeter–2
hosts; ****P < 0.0001, ***P < 0.001, two-sided-Mann–Whitney test; n = 8–29 mice steradian–1; sg, single guide.
Article
a b CIN
Tumour cells Low High
M1-like macrophages 2
Macrophages CD4+ T helper cell
M1-like macrophages 1
M2-like M1-like 1 IFN-responsive B cells
CINlow CINhigh Mast cells
Plasma cells
Fibroblasts NK cells
Dendritic
B cells cells M1-like 2 ISG-neutrophil
CD8+ early activation T cells
resp IF o N n - sive B3 cDC2 Activated cDC
Activated cDC1 CD8+ effector-memory T cells
cDC
B1 B2 Plasma Endothelial c T D reg C c 1 ells
cells Granulocytic
pDC
Gr-
Plasmacytoid MDSC(c) Fibroblasts
dendritic cells cDC2
n C a D iv 8 e + T cells CD4 M + ast MD G S r C - (d) E C n D d 8 o + t h n e a l i i v a e l c T e c ll e s lls
CD4+ helper CD4+ naive T cells
naive
Treg cells ISG- CD8+ dysfunctional T cells
CD8+ early activation neutrophil GR-MDSC
Gr- M2-like macrophages
effector me C m D o 8 ry + NK cells MDSC(a) Mature B cells
CD8+ –6–4–2 0 2 4 6
dysfunctional Differential abundance
log (fold change)
2
Fig. 2 | CIN-induced STING signalling engenders an immune-suppressive dialled-down. b, Strip plot showing CIN-dependent effects on differential
tumour microenvironment. a, Uniform manifold approximation and abundance, log(fold change (FC)), at the neighbourhood level grouped by cell
2
projection (UMAP) of all single cells coloured by cell subtype assignment; subtype and ranked by mean log(FC) within each cell subtype. Node opacity is
2
includes carcinoma, as well as immune and other stromal cell types within the scaled by P value, such that more significant neighbourhoods are more opaque
TME (n = 39,234 cells). Macro cell-type assignments are capitalized. Inset, and P ≤ 0.1 neighbourhoods are completely opaque. cDC, classical dendritic
schematic showing that tumour cell rates of CIN were genetically dialled-up or cells; pDC, plasmacytoid dendritic cells; T , regulatory T cells.
reg
different promoters revealed a dose-dependent relationship between in the TME, called ContactTracing. Our strategy exploited intrinsic
Sting1 re-expression and metastasis (Fig. 1j). variability in scRNA-seq data to infer cellular responses to ligand–
receptor-mediated interactions. Importantly, this was done without
relying on prior knowledge of downstream target genes, allowing unbi-
CIN and STING promote immune suppression
ased discovery of heretofore unknown cellular responses to receptor
We orthotopically transplanted CINhigh, CINlow and Sting1-depleted engagement. This method was based on the simple premise that, within
CINhigh 4T1 cells in the mammary fat pad of BALB/c mice and performed a given tumour, it is unlikely that all donor (ligand-producing) cells
single-cell RNA sequencing (scRNA-seq) of freshly resected 14-day-old and target (receptor-expressing) cells are fully engaged in a particu-
tumours (Fig. 2a). As expected, CINhigh tumour cells exhibited signifi- lar cell–cell interaction. Exploiting inherent biological variability in
cantly higher karyotype diversity as inferred from scRNA-seq data (1) receptor expression on target cells and (2) sample-level ligand avail-
compared with their CINlow counterparts (Extended Data Fig. 1l). At a ability in the TME, we predicted the effect of a ligand on its target cell
high level, CIN engendered a pro-metastatic tumour microenviron- in its native, in vivo context (Fig. 3a–c and Methods). For all putative
ment (TME) that was markedly enriched in immune-suppressive mac- ligand–receptor-mediated interactions, we performed a likelihood
rophages, granulocytic myeloid-derived suppressor cells (Gr-MDSCs) ratio test between receptor-expressing and receptor-null target cells
and dysfunctional T cells (Fig. 2b and Extended Data Figs. 2a–g and (Extended Data Fig. 4a,b), which could capture unwanted confound-
3a–d). Conversely, CINlow tumours were enriched in pro-inflammatory ing (correlation) between receptor expression and the expression of
macrophages, IFN-responsive B cells, activated dendritic cells and CD4+ other genes. However, by exploiting secondary variability in ligand
T helper cells (Fig. 2b and Extended Data Figs. 2c,h,I and 3). Impor- availability across experimental conditions—such as levels of CIN or
tantly, depleting cancer cell Sting1 in CINhigh tumours abolished many cancer cell STING expression (Extended Data Fig. 4c)—we distinguished
of the effects of CIN on the TME, ultimately restoring it to a CINlow-like ligand effects from genes merely co-expressed with the relevant recep-
state (Extended Data Figs. 2c,e–g and 3). Some of the scRNA-seq find- tor (Fig. 3b,c and Extended Data Fig. 4c). True ligand effects were not
ings were validated through flow cytometry, revealing enrichment of correlated across conditions, unlike their unobserved confounders
CD11b+ and CD206+ as well as CD11b+Ly6G+ cells in CINhigh compared with (Extended Data Fig. 4d,e). Ligand effects (that is, distinct transcrip-
CINlow tumours (Extended Data Fig. 2a,b). Coculture of CINhigh tumour tional responses in receptor-expressing target cells when the ligand is
cells with macrophages led to significant reduction in relative argin- present) largely clustered by cell type (Extended Data Fig. 4f), and were
ase expression upon loss of cancer cell Cgas or Sting1 (Extended Data mapped back to subpopulations within the target cell type (Extended
Fig. 2f). And suppression of CIN or knockout of either Cgas or Sting1 Data Fig. 4g).
in CINhigh cells enhanced CD8+ T cell migration and led to increased We performed multiple orthogonal validations of ligand effects
tumour cell killing by pan-T cells, CD8+ T cells or natural killer (NK) predicted by ContactTracing. First, we compared target genes inferred
cells (Extended Data Fig. 3e). by ContactTracing with those previously reported in experimental
assays23 (Methods). ContactTracing predicted many transcriptional
responses, including those that were context-dependent and could not
ContactTracing to map cell–cell interactions
be inferred from in vitro cytokine assays, such as target genes induced
To determine how CIN-induced STING signalling reprograms the in CCR2-expressing macrophages upon activation in vivo23,24 (Extended
TME, we developed a fundamentally new, systems-level approach to Data Fig. 5a–c). Second, we observed significant correlation between
predict the effect of conditionally dependent cell–cell interactions empirically derived transcriptional responses inferred from bulk
1082 | Nature | Vol 620 | 31 August 2023
1.0 ContactTracing (downstream signalling, sc-variability) NicheNet 0.8 (downstream signalling, prior knowledge) CellPhoneDB
0.6 (database, no prior knowledge)
Random ranking
0.4
0.2
0 101 102 103
Number of top-ranked interactions
RNA sequencing (RNA-seq) of ligand (in this case APOE)-treated and of ligand–receptor pairs (Extended Data Fig. 6a,b). An analysis of
untreated cells (RAW264.7 macrophages) (Extended Data Fig. 5d) and human TNBC scRNA-seq data25 likewise revealed many unique CIN-
those predicted by ContactTracing using scRNA-seq of APOE-treated dependent interactions predicted by ContactTracing (Fig. 3e). We then
RAW264.7 cells only (Fig. 3d and Extended Data Fig. 5e). used matched spatial transcriptomics data to determine the veracity
To benchmark our approach, we compared the top 1,000 CIN- of these interactions. Strikingly, many unique predictions made by
dependent interactions predicted by ContactTracing with those iden- ContactTracing were found to colocalize on spatial transcriptomics
tified by existing cell–cell interaction methods (Methods). Similar data from the same human tumour samples (Fig. 3e and Extended
to other methods that considered downstream signalling, interac- Data Fig. 6c). Furthermore, ContactTracing prioritized interactions in
tions predicted by ContactTracing were largely orthogonal to those a way that better captured their probability of colocalization on spatial
predicted by methods that merely relied on the mutual expression transcriptomics data (Fig. 3f).
Nature | Vol 620 | 31 August 2023 | 1083
dezilacoloc
noitcarF
b c
– – + +
– + – +
APOE-effect on
1.50 Sdc4-expressing macrophages
1.25
1.00
0.75
0.50
0.25
0
(R2 = 0.69,
–0.25 P = 1.45 × 10–91)
Bulk RNA-seq log(FC)
2
)CF(gol
gnicarTtcatnoC
2
d e
ContactTracing
CellPhoneDB
NATMI
SingleCellSignalR
iTalk
Connectome
CytoTalk
CellCom
–5.0 –2.5 02.55.07.5 10.0 12.5 N
C
ic
e
h
ll
e
C
N
h
e
a
t
t
Set size
f g
Macrophages/mMDSC CINhigh
Number of
interaction
effects in
target cell
Tumour cells
noisserpxE dnagil
)CF(gol
2
ContactTracing Ligand
Target cell type
Receptor Cellular detection rate
Ligand available? Discrete Donor cell type Target cell type Receptor expressed?
Gene expression Ligand
effect Continuous
CIN-dependent?
Ligand expressed?
Microenvironment
Receptor expressed?
Colocalized in matched
600 spatial transcriptomics
400 True
200 False
0
CINlow
rotpeceR
dnagiL
detalerroc
tceffe
noitcesretnI
erocs
noisserpxe
eneG
epyt
llec
tegrat
ni
a CINlow CINhigh
?
+
L+R
SIRB I 1 tg _ b c 7 o It m ga p 4 l I e tg x b1 Cd4 H 4 sp9 T 0 lr a 4 a T 1 nc Pf4Apoe Tgm I 2 tgb2 Cd81 aMb2 F _ n c 1 o A m n p xa l V e 2 x im Hbe L g r f p1 Cd6 A 3 bca S 1 dc1 Trem2 Ccr2 Ccr1 Gas6 Il11ra C 1 adm T 1 gfb1
Cd47 Cdh V 1 cam1 Fn L 1 amc2 Hbegf Lrp S 1 100a S 8 100a9 Itgav Ldlr Sdc4 M
a
m
Vb
p
1
9 _c C om 3 plex Cd S 4 e 4 rpin H e2 spa1b Ctsd Timp1 Apoe Ccl2Axl Il N 1 e 1 ctin3 Tgfbr2
Fig. 3 | ContactTracing infers conditionally dependent ligand effects samples, for which there exist matched single-cell and spatial transcriptomics
in vivo from single-cell variability. a, ContactTracing infers the effect of data. Histogram shows fraction of significantly colocalized interactions in a
ligand–receptor-mediated interactions on target (receptor-expressing) 200-μm radius on matched spatial transcriptomics data (Methods) for each
cells. (b) Inferences are based on intrinsic biological variability in receptor set. f, Colocalization of non-secreted interactions within a 50-μm visium spot,
expression on target cells and ligand abundance in the TME; we focus on CIN- reported as a function of number of top-ranked interactions. Each interaction is
and STING-dependent ligand effects. c, Plate diagram of the ContactTracing defined by [ligand, receptor, target cell type], and is designated as colocalized
Hurdle model. Plates represent the conditional dependence of variables within by a nominal one-sided permutation-based P < 0.05; fraction colocalized was
the TME and within a target cell population. Hurdle models are fitted using assessed for ContactTracing (considers downstream signalling, no prior
MAST, which splits models into discrete and continuous components. White knowledge), CellPhoneDB (no downstream signalling), NicheNet (prioritizes
boxes depict variables predicted by MAST, and grey boxes indicate variables interactions exhibiting downstream signalling based on prior knowledge) and
that ContactTracing calculates to identify CIN-dependent ligand effects for randomly ranked interactions as a function of number of top interactions.
(yellow box). d, Correlation between APOE effect on macrophages inferred Lines represent the average fraction of colocalized interactions across four
from single-cell variability (ContactTracing) and defined through bulk patient tumours with matched spatial transcriptomics data. Dotted lines
RNA-seq comparison of ligand-treated versus untreated macrophages. represent interactions that did not pass prefiltering steps of NicheNet or
Each node represents a gene; log(FC) expression in bulk RNA-seq (x axis) as CellPhoneDB; these interactions were sorted randomly and assigned the
compared with that inferred from scRNA-seq (y axis) for APOE receptor, Sdc4. lowest score. g, CIN- and STING-dependent interactions between tumour cells
Node size is proportional to −log (FDR) of scRNA-seq target test, and node and macrophages, predicted by ContactTracing. Significant interactions are
10
colour is proportional to −log (FDR) of bulk RNA-seq test for differential defined by receptor-expressing target cells that exhibit at least 10 significant
10
expression. R2 is Pearson’s correlation coefficient; P value is two-sided and interaction effects (FDR < 0.25) when the cognate ligand is conditionally
testing for correlation. e, UpSet plot showing intersection between top 1,000 available in the TME, ligand abs(log(FC)) > 0.12 at FDR < 0.05, with log(FC)
2 2
interactions (each defined by a unique receptor and target cell type) predicted having the same sign for both the CIN and STING comparisons. abs, absolute;
by ContactTracing and other cell–cell interaction methods in human TNBC mMDSC, myeloid-derived suppressor cell; sc-variability, single cell-variability.
Article
Immune suppression from endoplasmic reticulum stress STING inhibitors suppress metastasis
All CIN- and STING-dependent cell–cell interactions were then visual- Given that signalling downstream of STING in chromosomally unstable
ized for cell pairs (Fig. 3g) or across all major cell types in the TME using cancer cells is skewed towards an ER stress response as opposed to
a Circos plot (Fig. 4a). Cell–cell interactions in CINhigh tumours largely its canonical IFN function, we reasoned that STING inhibition might
involved cancer cells, immune-suppressive macrophages, Gr-MDSCs represent a viable therapeutic strategy in tumours with CIN. Treat-
and dysfunctional T cells (Extended Data Fig. 4h). Tumour cell-derived ment with C-176, a covalent inhibitor that blocks activation-induced
factors contributing to these interactions had well-established palmitoylation of STING33, dampened ER stress response signalling,
roles in immune suppression and metastasis, including Ccl2, Cxcl1, as evidenced by lower CHOP and BiP protein levels in TM-treated
Il11, Apoe and Serpine2 (refs. 26–30) (Fig. 4a,c). Conversely, CINlow CINhigh 4T1 cells, and reduced baseline CCL2 levels in conditioned media
tumours were characterized by interaction between tumour cells, (Extended Data Fig. 9e,f). Transcriptomic analysis of C-176-treated
pro-inflammatory macrophages, and helper and cytotoxic T cells B16F10 CINhigh cells revealed downregulation of pathways related to
(Extended Data Fig. 4h). inflammation, epithelial-to-mesenchymal transition, as well as the
Interestingly, CIN- and STING-dependent ligands that measurably UPR/ER stress response (Extended Data Fig. 9g). We next delivered
impacted recipient cells in the TME were associated with an unfolded C-176 or H-151, a second covalent STING inhibitor, through daily intra-
protein response (UPR) to endoplasmic reticulum (ER) stress, in peritoneal injections to tumour-bearing immune competent animals
addition to canonical pathways associated with CIN such as NF-κB after tail-vein inoculation of CINhigh 4T1, B16F10 or CT26 tumour cells.
and IL6-Jak-Stat3 signalling2,31, whereas effectual ligands emanating In all instances, treatment with C-176 or H-151 prolonged survival
from CINlow or Sting1-depleted CINhigh tumour cells were associated (Fig. 5c and Extended Data Fig. 9h). We necropsied another subset
with IFN responses (Fig. 4b–d). Accordingly, pairwise comparison of animals 13 d after inoculation of CT26 cells and observed a signifi-
of CINhigh and CINlow tumour cells revealed significant enrichment cant reduction in surface lung metastases (Extended Data Fig. 9i).
of ER stress-related and NF-κB target genes and reduced IFN sig- Reduced metastasis by the STING inhibitor did not match complete
nalling (Extended Data Fig. 7a). On the other hand, pairwise analy- Sting1 KO, and this might be due to incomplete target exposure by
sis between CINlow and Sting1-depleted CINhigh tumour cells did not the drug or dichotomous contributions of cancer cell and host cell
reveal significant enrichment in the ER stress (normalized enrichment STING, both of which would be inhibited with drug treatments. We
score (NES) = −0.85, false discovery rate (FDR) = 0.83) or type I IFN thus administered C-176 to C57BL/6 mice inoculated with Sting1-KO
(NES = 0.56, FDR = 0.95) pathways, suggesting that Sting1 depletion B16F10 cells. In these mice, C-176 treatment did not provide an addi-
abolishes CIN-dependent effects in tumour cells. Transcriptional tional survival advantage beyond Sting1 KO (Fig. 5c). Prolonged daily
targets of all three arms of the ER stress response32 were upregu- treatment with the STING inhibitor was well tolerated and did not lead
lated in basal stem-like tumour cells that were enriched in CINhigh to any clinically evident toxicity when compared with vehicle-treated
tumours relative to the luminal-like subpopulations that primarily control animals.
belonged to CINlow and Sting1-depleted CINhigh tumours (Extended Data
Fig. 7b–f).
IFN tachyphylaxis downstream of STING
To better define the context-dependent nature of cellular responses
STING is required for ER stress response
to STING activation, we developed a tractable model system using
Despite constitutive cGAS–STING activation, CINhigh cells exhibited non-immortalized IMR90 human lung fibroblasts, which have an intact
low baseline expression of IFN-stimulated genes (ISGs), with mini- cGAS–STING pathway that is unstimulated at baseline, yet primed to
mal induction upon treatment with exogenous cGAMP but not with respond upon cGAMP treatment34. We treated IMR90 fibroblasts with
Poly(I:C), an activator of the dsRNA sensing pathway, which led to cGAMP for five consecutive daily doses and assessed time-dependent
a robust induction of ISGs (Extended Data Fig. 8a). We then treated expression of key ISGs and ER stress response target genes after the
CINhigh cells (4T1, B16F10, EO771.LMB and CT26) with tunicamycin (TM), first and fifth daily doses of cGAMP. We observed expected induction
an ER stress inducer, which promoted robust and time-dependent of IFNB1 and ISGs after the first cGAMP treatment (Fig. 5d). However, by
ER stress response signalling (Fig. 5a and Extended Data Fig. 8b,c). the fifth daily treatment, the expression of ISGs was nearly completely
Notably, ER stress response signalling was blunted in Sting1-KO cells abolished (Fig. 5d). This reduction in IFN responsiveness to repetitive
(Fig. 5a and Extended Data Fig. 8b,c). We next knocked out each of stimulation—a process known as tachyphylaxis—was limited to STING,
the three main ER stress sensors, IRE1α (Ern1), PERK (Eif2ak3) or ATF6 as transfection with Poly:IC after the fifth cGAMP stimulation led to an
(Atf6), using CRISPR–Cas9 ribonucleoprotein transfection in 4T1 acute and robust ISG induction (Extended Data Fig. 10a), mirroring
cells and observed a significant reduction in the number of surface observations derived from cancer cells (Extended Data Fig. 8a). Con-
lung metastases after tail-vein inoculation, without impacting cel- versely, repetitive treatment with cGAMP led to increased expression
lular proliferation rates (Fig. 5b and Extended Data Fig. 8d,e). Strik- of ER stress and NF-κB target genes (Fig. 5d), which was abolished when
ingly, this effect was again entirely dependent on the immune system cells were cotreated with the chemical chaperone and ER stress inhibi-
(Fig. 5b). tor 4-phenylbutyric acid (4-BPA) (Extended Data Fig. 10b). Treatment
Next, we examined the expression of three ER stress-related of IMR90 fibroblasts with the STING antagonist H-151 reduced both
cytokines identified from ContactTracing, Ccl2, Cxcl1 and Il11, acute (early) and chronic (late) STING-dependent effects (Extended
in 4T1 cells and validated their dependence on tumour-intrinsic Data Fig. 10c).
STING activation (Extended Data Fig. 8f). While KO of individual Repeated stimulation of IMR90 cells with cGAMP led to reduc-
cytokines in CINhigh 4T1 cells was not sufficient to significantly sup- tions in STING protein levels (Extended Data Fig. 11a), in line with
press metastasis, overexpression of either Ccl2 or Cxcl1 led to a sig- autophagy-lysosomal-dependent degradation of STING mediated
nificant increase in metastasis of Sting1-KO cells (Extended Data by its own activation35. Thus, we asked whether CIN-induced chronic
Fig. 8g). Treatment of CINhigh tumours with AMG44, a selective PERK STING activation might also explain reduced STING protein levels
inhibitor, led to a significant decrease in Gr-MDSCs and a corre- often observed in cancer cells. Indeed, alleviating chronic activa-
sponding increase in NK cells and CD8+ T cell infiltration, yet did not tion of STING through Cgas KO led to a significant rebound in STING
measurably impact macrophage polarization (Extended Data protein levels in three of the four CINhigh cancer cell lines examined
Fig. 9a–d). (Extended Data Figs. 1e and 11b). Furthermore, treatment with the
1084 | Nature | Vol 620 | 31 August 2023
a
NK
Pro-inflammatory
M
p
D
C
cDC acrophage
mplex
G R- M D S C B c ells S C d A a c x v 1 l 1 C P C T a t x g g d c C P f T e m A b r d r 2 h t C C c r p 2 L 1 9 b 1 v d d d r 3 d r j 4 I 1 l G t l r 4 1 g 7 n a 7 S a 4 C d i C 2 c d d T 1 2 8 h 8 3 L b y d 9 It 6 g T b gf 1 br1 S10 S 0 1 a 0 8 0 S a 1 9 00 S a 1 8 00a9 S100a9 Tln1 S carb1 S dc2 S 100a8App Itga4 Itgal Ccr1 Hsp90aa1 Tg m2 T F l p r4 r2 Tgfb1 L S rp I R 1 B Il 1 1 _ C r2 c d o O 47 s C m cr I 2 tg C b C c 2 l2 d 4 4 I L t 4 g g b a A A 7 l c n s v I 3 x l r 1 a S l1 r 1 S e n m C d C c a d x 4 P 1 8 I d c t 6 t g g l P 3 s b V e S 2 A 1 i C c m n d I a x n 5 C c a m h a c 2 4 b r 1 r I 1 a l t 2 E g C n b T A d g A 3 g b 9 f p b c 3 o r a e 1 I 1 l11 T C C r T g a x d r f 1 c e b 3 l m 1 r 8 2 6 2 A C I x 1 t l g q a a P 9 f4 A n ti-in fl a m m a to ry Cd93 Tre I m l1a 2 C C a d d 6 m 3 1 Gas6
Ccrl2 Sdc4 Vcam1
Hsp90 Il a 1 a rn 1 C F C g x a c f v r l 2 1 1 Cdh1 mi n al
s lle c T C C tla S d 4 S 1 4 0 1 4 0 0 K 0 a I l a 9 t C r g c 8 x b 1 K c 1 r lr 6 C c2 K cl l 5 rk S T C 1 i d C m c d t 4 p s C 6 1 I d g 3 d f1 4 T r G 7 L H F r 2 p b - S e 1 T t e a T 2 r g p 3 f r b in e r3 c e S e 2 p dc to 2 A r1 xl App Tgfbr1 Cd74 Vca m1 Tg Il f 1 b 1 r r 2 a1 Efna1 Itgb1 Lifr Eng Col7a1 Ccr5Itgb2 C d44 S dc1 S 100a S 8 100a9 C 5ar1 C cr2 Trem 2 C d93 Itgal Klrk E 1 ph A a p 1 o Il e 1r N 2 ectin3 Ccr1 E I p t I g h t A g a a a b 2 3 b L 2 c d 4 b a l 1 r C 1 H cl s 2 I M l p 1 a m 1 1 p b 9 L u
EN
Basal
Tumour
cell
Low
Nature | Vol 620 | 31 August 2023 | 1085
)oitar
sddo(ngis
×
)P(
gol– 01 eessnnooppsseerr
ggNNFFII
logFC(ligand)
2
CINhigh
CINlow and
CINhigh + Sting1KD
DC1
Differential abundance CINhighversus CINlow Magnitude CIN- and STING-dependent ligand effect
d CIN Chronic STING
activation
c CIN Sting1 UPR and WT
high Apoe Ccl2 Il11 S100a8 Timp1 S100a9 Serpine2 Cxcl1 Col7a1 IRE1a IFN
Cd74 Cdh1 Mmp9 Ctsd KD Efna1 H2-T23 Vcam1 Hspa1b PERK ATF6
TTMMEE ttnneemmeellppmmooCC nnooiittcceejjeerr ttffaarrggoollllAA bbKKFFNN
aaiivv
aaFFNNTT
eessnnooppsseerr yyrroottaammmmaaflflnnII ssiisseenneeggooiiggnnAA 33ttaattSS--kkaaJJ--66LLII
eessnnooppsseerr
aaNNFFIIII
ggnniillllaannggiiss
bbFFGGTT
nnooiittcceejjeerr
ttffaarrggoollllAA nnooiittccnnuujj
llaacciippAA
a9b1_complex Cd72
_complex CD94_NKG2C IL1_receptor_inhibitor IL1 b 6 _ _receptor
4
2
0
–2
–4
ER stress
sssseerrttss
RREE
oott
RRPPUU
Fig. 4 | ContactTracing identifies ER stress as a central mediator of CIN- the middle link interacting [ligand, donor cell type] and [receptor, target cell
induced immune suppression. a, ContactTracing Circos plot highlighting all type] pairs; ribbon thickness is proportional to the number of genes exhibiting
CIN- and STING-dependent interactions. Each segment represents a cell type, a CIN- and STING-dependent interaction effect (whichever is greater) and
and cell types are further divided into ligands and receptors, which are ordered colour represents CIN- and STING-dependent log(FC) of its complementary
2
according to the first diffusion component (DC1) computed on differentially ligand measured in the donor cell type (whichever is greater). Links are only
expressed genes (DEGs) in each cell type conditioned on ligand/receptor shown if they exhibit (1) CIN- and STING-dependent expression of ligand in
expression. Outer rings encode CIN-dependent interactions, which include donor cells (in the same direction with FDR Q value < 0.05 and abs(log
2
target (receptor-expressing) cells distinguished by ≥10 CIN-dependent (expression FC) > 0.12)) and (2) at least 10 CIN-dependent and 10 STING-
interaction effects (two-sided P value, FDR Q value < 0.25), as well as CIN- dependent interaction effects in the target cell type. Ligands/receptors are
dependent ligands complementing those receptors (FDR Q value < 0.05 and labelled at ribbon ends; ligands are in black and receptors in grey. The data
abs(log(ligand expression FC) > 0.12)). The outer circle represents cell type. encoded in the ContactTracing Circos plot are provided in Supplementary
2
The next circle shows the DC1 score for ligand/receptor represented at that Table 9 and may be explored interactively at http://contacttracing.laughneylab.
coordinate; for example, macrophage response states were organized from com/circos. b, Differentially expressed pathways associated with CIN- and
pro-inflammatory to anti-inflammatory polarization states. The next circle STING-dependent, tumour-derived ligands that effect the TME with nominal
shows the correlation between the log-normalized expression of that ligand/ P < 0.05. The y axis is scaled by −log (P values) times the sign of the odds ratio
10
receptor and its CIN-dependent differential abundance (log(FC) as computed and colour indicates the pathway odds ratio. c, Bar plot highlighting CIN- and
2
by Milo in local neighbourhoods and mapped to single cells as the described in STING-dependent tumour-derived ligands that affect the TME, as described in
the Methods). The histogram in the next inner circle shows the number of a. d, Schematic illustrating the impact of chronic STING activation on functions
significant CIN-dependent interaction effects (FDR Q value < 0.25). Ribbons in associated with ligand effects.
Article
autophagy inhibitor bafilomycin A1 led to an increase in STING with a preponderance of cGAS+ micronuclei had low, but detectable,
protein levels in CINhigh WT but not Cgas-KO cells (Extended Data STING protein levels within cancer cells (cGAShighSTINGlow), whereas
Fig. 11c). those with a paucity of cGAS+ micronuclei had higher STING protein
expression (cGASlowSTINGhigh). This inverse correlation between the
expression of cGAS and STING in cancer cells was also observed within
Prognostic relevance of CIN in human TNBC spatially heterogeneous tumours (Fig. 5e). cGAShighSTINGlow tumours
We then asked whether the inverse relationship between cGAS activity exhibited fewer tumour infiltrating lymphocytes and were associ-
and STING protein levels can be recapitulated in human tumour sam- ated with reduced distant metastasis-free survival (DMFS), whereas
ples. Using antibodies that were validated on WT and CGAS-depleted cGASlowSTINGhigh tumours had a more favourable prognosis (Extended
cell pellets, we observed an inverse correlation between the frequency Data Fig. 11f–h and Fig. 5f). Unlike cancer cells, stromal cells consist-
of cGAS+ micronuclei and tumour cell-intrinsic STING expression ently displayed strong STING protein expression without evidence
in human TNBC (Extended Data Fig. 11d,e and Methods). Tumours of cGAS+ micronuclei.
1086 | Nature | Vol 620 | 31 August 2023
lortnoC OK
1nrE
OK
6ftA
OK
3ka2fiE
lortnoC OK
1nrE
OK
6ftA
OK
3ka2fiE
150
100
50
0
sesatsatem
gnul
ecafruS
200 100
150 75
100 50
50 25
0 0 0 50 100
Time (days)
)%(
lavivruS
a b c
WT—vehicle
WT—C-176
Sting1 KO—vehicle Sting1 KO—C-176
d ISGs ER stress/NF-κB
300 CCL5 CXCL10 sXBP1 HSPA5 8 DDIT3
6 200
4
First treatment 100
Fifth treatment 2
0 0
IFNB1 ISG15 OAS3 ATF3 20 CCL2 TNF
15
10
5
0
Time (h) Time (h) Time (h)
cGASlowSTINGhigh
cGASlowSTINGlow
cGAShighSTINGhigh
cGAShighSTINGlow
noitcudni-dloF
5.0 1 2 4 6 21 42
noitcudni-dloF
5.0 1 2 4 6 21 42 5.0 1 2 4 6 21 42
noitcudni-dloF
5.0 1 2 4 6 21 42 5.0 1 2 4 6 21 42 5.0 1 2 4 6 21 42
TM 0 h 1 h 3 h 6 h BALB/c NSG B16F10
Sting1 KO – + – + – + – +
BiP ****
CHOP
p-PERK
PERK
p-eIF2α
eIF2α
ATF4
α-tubulin
2′,3′-cGAMP
1 2 3 4 5 Days
***
300 5 5
4 4 200 3 3
100 2 2
1 1
0 0 0
400 400 250 25
300 300 200 20
150 15
200 200
100 10
100 100 50 5
0 0 0 0
100
50
0
0 100 200 300
Time (months)
)%(
SFMD
30
20
10
0
e f
g
710.0
= P
50 μm
hgihGNITSwolSAGc
wolGNITShgihSAGc
75 kDa
25 kDa
150 kDa
150 kDa
37 kDa
37 kDa
50 kDa
50 kDa
cGAS cGAS STING DNA
Acute Chronic
IFN ER stress
Anti-tumour Immune evasion
immunity and metastasis
Fig. 5 | Chronic STING activation promotes IFN tachyphylaxis and ER stress- vehicle control, log-rank test; ***P < 0.001; n = 15 animals per arm. d, Relative
dependent transcription. a, Immunoblots for BiP, CHOP, phosphorylated expression levels of ISGs and ER stress/NF-κB target genes at indicated time
PERK, total PERK, phosphorylated eIF2α, total eIF2α and ATF4 of 4T1 WT and points after the first (blue) and the fifth (red) cGAMP stimulations of IMR90
Sting1-KO cells at indicated time points post TM treatment with α-tubulin as human lung fibroblasts. e, Representative images from the same TNBC tumour
loading control. b, Number of surface lung metastases in BALB/c or NSG mice stained using DAPI (DNA), anti-cGAS and anti-STING antibodies, illustrating the
that were tail-vein-injected with control 4T1 cells or cells lacking key mediators inverse correlation between the frequency of cGAS+ micronuclei and STING
of the ER stress response; bars represent the median; ****P < 0.0001, two-sided expression in cancer cells. f, DMFS of patients with TNBC stratified based on
Mann–Whitney test; n = 12–24 and 10 animals per group for the BALB/c and tumour cGAS and STING expression intensity, log-rank test; n = 159 patients.
NSG injected hosts, respectively. c, Survival of C57BL/6 mice upon tail-vein g, Schematic illustrating the functional consequences of acute and chronic
inoculation of WT or Sting1-KO B16F10 cells with C-176 or a corresponding STING signalling.
We then analysed CIN-dependent interaction effects in available 1. Li, J. et al. Metastasis and immune evasion from extracellular cGAMP hydrolysis. Cancer
scRNA-seq data from eight human TNBCs25 using sample-level kar- Discov. 11, 1212–1227 (2021).
2. Bakhoum, S. F. et al. Chromosomal instability drives metastasis through a cytosolic DNA
yotypic diversity and CIN-associated transcriptional signatures to response. Nature 553, 467–472 (2018).
stratify patient tumours into CINhigh and CINlow cohorts (Extended 3. Bakhoum, S. F. & Cantley, L. C. The multifaceted role of chromosomal instability in cancer
and its microenvironment. Cell 174, 1347–1360 (2018).
Data Fig. 12a and Methods). There was a consistent cell-level correla-
4. Wormann, S. M. et al. APOBEC3A drives deaminase domain-independent chromosomal
tion between CIN transcriptional signatures2 and cancer cell-intrinsic instability to promote pancreatic cancer metastasis. Nat. Cancer 2, 1338–1356 (2021).
expression of ER stress-related genes, but not ISGs (Extended Data 5. Lengauer, C., Kinzler, K. W. & Vogelstein, B. Genetic instability in colorectal cancers.
Fig. 12b), across patients. CINhigh tumours were likewise associated Nature 386, 623–627 (1997).
6. Lee, A. J. et al. Chromosomal instability confers intrinsic multidrug resistance. Cancer
with an immune-suppressive TME characterized by enrichment Res. 71, 1858–1870 (2011).
of M2-like macrophages and dysfunctional T cells, whereas CINlow 7. Taylor, A. M. et al. Genomic and functional approaches to understanding cancer
aneuploidy. Cancer Cell 33, 676–689 e673 (2018).
tumours were enriched for M1-like macrophages and monocytes
8. Davoli, T., Uno, H., Wooten, E. C. & Elledge, S. J. Tumor aneuploidy correlates with markers
(Extended Data Fig. 12c,d). Finally, we applied ContactTracing to iden- of immune evasion and with reduced response to immunotherapy. Science https://doi.org/
tify CIN- and STING-dependent cell–cell interactions in human TNBCs, 10.1126/science.aaf8399 (2017).
9. Bakhoum, S. F. et al. The mitotic origin of chromosomal instability. Curr. Biol. 24, R148–149
and compared these with CIN-dependent interactions predicted in
(2014).
the mouse (Extended Data Fig. 12e,f). Many conserved interactions 10. Thompson, S. L. & Compton, D. A. Examining the link between chromosomal instability
involved tumour ligands associated with ER stress, such as APOE, and aneuploidy in human cells. J. Cell Biol. 180, 665–672 (2008).
11. Santaguida, S. et al. Chromosome mis-segregation generates cell-cycle-arrested cells
IL11 and CCL2.
with complex karyotypes that are eliminated by the immune system. Dev. Cell 41, 638–651
e635 (2017).
12. Laucius, C. D., Orr, B. & Compton, D. A. Chromosomal instability suppresses the growth
Discussion of K-Ras-induced lung adenomas. Cell Cycle 18, 1702–1713 (2019).
13. Hoevenaar, W. H. M. et al. Degree and site of chromosomal instability define its
CIN and STING activation are poorly tolerated in normal cells, where oncogenic potential. Nat. Commun. 11, 1501 (2020).
they often promote cellular senescence and immune-mediated 14. Nguyen, B. et al. Genomic characterization of metastatic patterns from prospective
clinical sequencing of 25,000 patients. Cell 185, 563–575 e511 (2022).
clearance36–38. This led to the idea that CIN may act as a tumour
15. Watkins, T. B. K. et al. Pervasive chromosomal instability and karyotype order in tumour
suppressor12,13. Furthermore, STING activation has been proposed as a evolution. Nature https://doi.org/10.1038/s41586-020-2698-6 (2020).
checkpoint against cellular transformation39,40 or the re-awakening of 16. Bakhoum, S. F., Thompson, S. L., Manning, A. L. & Compton, D. A. Genome stability is
ensured by temporal control of kinetochore-microtubule dynamics. Nat. Cell Biol. 11,
dormant metastasis41. Paradoxically, advanced and metastatic human
27–35 (2009).
tumours often exhibit evidence for CIN, and, in this context, it is asso- 17. Hatch, E. M., Fischer, A. H., Deerinck, T. J. & Hetzer, M. W. Catastrophic nuclear envelope
ciated with immune evasion2,7,8,14,42. Similarly, in tumour models, CIN collapse in cancer cell micronuclei. Cell 154, 47–60 (2013).
18. Mackenzie, K. J. et al. cGAS surveillance of micronuclei links genome instability to innate
and persistent STING activation were shown to promote tumour cell
immunity. Nature 548, 461–465 (2017).
survival as well as drive cancer progression, metastasis and immune 19. Harding, S. M. et al. Mitotic progression following DNA damage enables pattern
suppression2,4,31,34,43–49. This dichotomy invokes key adaptive steps that recognition within micronuclei. Nature 548, 466–470 (2017).
20. Ablasser, A. & Chen, Z. J. cGAS in action: expanding roles in immunity and inflammation.
must take place for cancer cells to tolerate—and co-opt—ongoing chro-
Science https://doi.org/10.1126/science.aat8657 (2019).
mosome missegregation and downstream inflammatory signalling. 21. Moore, A. T. et al. MCAK associates with the tips of polymerizing microtubules. J. Cell Biol.
Rather than the wholesale loss of STING protein from cancer cells, our 169, 391–397 (2005).
22. Liu, H. et al. Nuclear cGAS suppresses DNA repair and promotes tumorigenesis. Nature
data argue that the most parsimonious path toward tumour progres-
563, 131–136 (2018).
sion and metastasis is adaptive re-wiring of signalling downstream 23. Jiang, P. et al. Systematic investigation of cytokine signaling activity at the tissue and
of STING—a process that can occur within days, thereby allowing single-cell levels. Nat. Methods 18, 1181–1191 (2021).
24. Bartneck, M. et al. The CCR2+ macrophage subset promotes pathogenic angiogenesis
tumours to simultaneously eschew the deleterious pro-inflammatory for tumor vascularization in fibrotic livers. Cell. Mol. Gastroenterol. Hepatol. 7, 371–390
role of type I IFN while benefiting from immune-suppressive ER stress (2019).
signalling (Fig. 5g). 25. Wu, S. Z. et al. A single-cell and spatially resolved atlas of human breast cancers. Nat.
Genet. 53, 1334–1347 (2021).
Activators of the STING pathway are currently in clinical devel- 26. Dhanda, J. et al. SERPINE1 and SMA expression at the invasive front predict extracapsular
opment50,51. The IFN-specific tachyphylaxis observed upon chronic spread and survival in oral squamous cell carcinoma. Br. J. Cancer 111, 2114–2121 (2014).
STING activation, along with an immunosuppressive TME, might 27. Jiang, S. et al. Activation of WNT7b autocrine eases metastasis of colorectal cancer via
epithelial to mesenchymal transition and predicts poor prognosis. BMC Cancer 21, 180
explain pre-existing resistance of chromosomally unstable tumours (2021).
to STING agonists, which have thus far demonstrated limited efficacy in 28. Acharyya, S. et al. A CXCL1 paracrine network links cancer chemoresistance and
early-stage clinical trials despite evidence for adequate target engage- metastasis. Cell 150, 165–178 (2012).
29. Lim, S. Y., Yuzhalin, A. E., Gordon-Weeks, A. N. & Muschel, R. J. Targeting the CCL2-CCR2
ment50,51. Critically, our results pave the way for a biomarker-based signaling axis in cancer metastasis. Oncotarget 7, 28697–28710 (2016).
approach to stratify patients whose tumours still maintain the abi- 30. Johnstone, C. N., Chand, A., Putoczki, T. L. & Ernst, M. Emerging roles for IL-11 signaling in
cancer development and progression: focus on breast cancer. Cytokine Growth Factor
lity to mount an acute IFN-dominant response to STING activation
Rev. 26, 489–498 (2015).
(cGASlowSTINGhigh, Fig. 5e,f). Our paradigm also recognizes a subset 31. Hong, C. et al. cGAS-STING drives the IL-6-dependent survival of chromosomally instable
of patients who might instead benefit from inhibition of cGAS–STING cancers. Nature 607, 366–373 (2022).
32. Adamson, B. et al. A multiplexed single-cell CRISPR screening platform enables
signalling to curb tumour-intrinsic chronic inflammation and its
systematic dissection of the unfolded protein response. Cell 167, 1867–1882 e1821 (2016).
immune-suppressive sequalae (cGAShighSTINGlow, Fig. 5e,f). Given ongo- 33. Haag, S. M. et al. Targeting STING with covalent small-molecule inhibitors. Nature 559,
ing efforts to develop selective inhibitors of cGAS, STING33,52 and ER 269–273 (2018).
stress sensors, such as PERK53, our work offers an exciting opportunity 34. Dou, Z. et al. Cytoplasmic chromatin triggers inflammation in senescence and cancer.
Nature 550, 402–406 (2017).
for therapeutic intervention in chromosomally unstable tumours for 35. Gui, X. et al. Autophagy induction via STING trafficking is a primordial function of the
which there are currently few effective therapeutic options. cGAS pathway. Nature 567, 262–266 (2019).
36. Ishikawa, H., Ma, Z. & Barber, G. N. STING regulates intracellular DNA-mediated, type I
interferon-dependent innate immunity. Nature 461, 788–792 (2009).
37. Wang, R. W., Vigano, S., Ben-David, U., Amon, A. & Santaguida, S. Aneuploid senescent
Online content cells activate NF-κB to promote their immune clearance by NK cells. EMBO Rep. 22,
e52032 (2021).
Any methods, additional references, Nature Portfolio reporting summa-
38. Wang, H. et al. cGAS is essential for the antitumor effect of immune checkpoint blockade.
ries, source data, extended data, supplementary information, acknowl- Proc. Natl Acad. Sci. USA 114, 1637–1642 (2017).
edgements, peer review information; details of author contributions 39. Ranoa, D. R. E. et al. STING promotes homeostasis via regulation of cell proliferation and
chromosomal stability. Cancer Res. 79, 1465–1479 (2019).
and competing interests; and statements of data and code availability
40. Nassour, J. et al. Autophagic cell death restricts chromosomal instability during
are available at https://doi.org/10.1038/s41586-023-06464-z. replicative crisis. Nature 565, 659–663 (2019).
Nature | Vol 620 | 31 August 2023 | 1087
Article
41. Hu, J. et al. STING inhibits the reactivation of dormant metastasis in lung 51. Meric-Bernstam, F. et al. Combination of the STING agonist MIW815 (ADU-S100) and PD-1
adenocarcinoma. Nature https://doi.org/10.1038/s41586-023-05880-5 (2023). inhibitor spartalizumab in advanced/metastatic solid tumors or lymphomas: an open-label,
42. Rosenthal, R. et al. Neoantigen-directed immune escape in lung cancer evolution. Nature multicenter, phase Ib study. Clin. Cancer Res. 29, 110–121 (2023).
567, 479–485 (2019). 52. Lama, L. et al. Development of human cGAS-specific small-molecule inhibitors for
43. Fujiwara, T. et al. Cytokinesis failure generating tetraploids promotes tumorigenesis in repression of dsDNA-triggered interferon expression. Nat. Commun. 10, 2261 (2019).
p53-null cells. Nature 437, 1043–1047 (2005). 53. Calvo, V. et al. Discovery of 2-amino-3-amido-5-aryl-pyridines as highly potent, orally
44. Ahn, J. et al. Inflammation-driven carcinogenesis is mediated through STING. Nat. bioavailable, and efficacious PERK kinase inhibitors. Bioorg. Med. Chem. Lett. 43, 128058
Commun. 5, 5166 (2014). (2021).
45. Lemos, H. et al. STING promotes the growth of tumors characterized by low antigenicity
via IDO activation. Cancer Res. 76, 2076–2081 (2016). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
46. Foijer, F. et al. Chromosome instability induced by Mps1 and p53 mutation generates published maps and institutional affiliations.
aggressive lymphomas exhibiting aneuploidy-induced stress. Proc. Natl Acad. Sci. USA
111, 13427–13432 (2014). Open Access This article is licensed under a Creative Commons Attribution
47. Foijer, F. et al. Deletion of the MAD2L1 spindle assembly checkpoint gene is tolerated in 4.0 International License, which permits use, sharing, adaptation, distribution
mouse models of acute T-cell lymphoma and hepatocellular carcinoma. eLife https://doi. and reproduction in any medium or format, as long as you give appropriate
org/10.7554/eLife.20873 (2017). credit to the original author(s) and the source, provide a link to the Creative Commons licence,
48. Shoshani, O. et al. Transient genomic instability drives tumorigenesis through and indicate if changes were made. The images or other third party material in this article are
accelerated clonal evolution. Genes Dev. 35, 1093–1108 (2021). included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
49. Frittoli, E. et al. Tissue fluidification promotes a cGAS-STING cytosolic DNA response to the material. If material is not included in the article’s Creative Commons licence and your
in invasive breast cancer. Nat. Mater. https://doi.org/10.1038/s41563-022-01431-x intended use is not permitted by statutory regulation or exceeds the permitted use, you will
(2022). need to obtain permission directly from the copyright holder. To view a copy of this licence,
50. Meric-Bernstam, F. et al. Phase I dose-escalation trial of MIW815 (ADU-S100), an visit http://creativecommons.org/licenses/by/4.0/.
intratumoral STING agonist, in patients with advanced/metastatic solid tumors or
lymphomas. Clin. Cancer Res. 28, 677–688 (2022). © The Author(s) 2023
1088 | Nature | Vol 620 | 31 August 2023
Methods
Immunofluorescence microscopy
Cell culture Cells were fixed with ice-cold (−20 °C) methanol for 15 min. Subse-
IMR90, 4T1, CT26, RAW264.7 and B16F10 cell lines were purchased from quently, cells were permeabilized using 1% Triton for 4 min. The primary
the American Type Culture Collection and cultured in MEM (IMR90), antibody information is listed in Supplementary Table 3. TBS-BSA was
DMEM (B16F10, RAW264.7) or RPMI (4T1, IMR90, CT26) supplemented used as a blocking agent during antibody staining. DAPI was added
with 10% FBS in the presence of penicillin (50 U ml−1) and streptomycin together with secondary antibodies. Cells were mounted with Prolong
(50 μg ml−1). All cells were found to be negative for mycoplasma upon Diamond Antifade Mountant (Life Technologies, P36961).
repeated routine testing.
H&E staining of lung metastases
The generation of KO and gene-overexpressing cell lines Lungs were excised from euthanized mice and submerged in 4% PFA
Murine cancer cells with Cgas, Sting1, Atf6, Ern1, Eif2ak3, Ccl2, Cxcl1 overnight at 4 °C, and then were transferred to 70% ethanol. Tissue
and Il11 KO were generated by Cas9 ribonucleoprotein nucleofection embedding, slide sectioning and H&E staining were performed by the
using a Lonza 4D-Nucleofector and SF Pulse Code CM-150 Cell Line Molecular Cytology Core Facility at MSKCC.
Kit. For Cgas and Sting1 KO, four guides were screened per target and
KO cell lines were confirmed using immunoblotting. For Atf6, Ern1 Quantitative PCR
and Eif2ak3 KO, three guides were used simultaneously. For Ccl2, RNA was extracted from cells with Trizol (Invitrogen no. 15596026).
Cxcl1 and Il11 KO, two guides were used sequentially. Stable knock- cDNA was synthesized using the RNA to cDNA EcoDry Premix (Double
down of Cgas or Sting1 in 4T1 cells was achieved using shRNAs in pRRL Primed) kit (Takara no. 639549). Real-time PCR was performed to
(SGEP) plasmids obtained from the Memorial Sloan Kettering Cancer measure the relative messenger RNA expression levels of ISGs and the
Center (MSKCC) RNA Interference Core. Four distinct shRNA hair- control GAPDH using Luna Universal qPCR Master Mix (NEB M3003L).
pins were screened per target. Targeted shRNA and CRISPR guide The quantitative PCR reaction and analysis were performed on a Quant-
RNA sequences are listed in Supplementary Table 1. To overexpress Studio 6 platform (Life Technology). The primer sequences are listed
Kif2c or dnMCAK, Kif2c and dnMCAK complementary DNA sequences in Supplementary Table 4. Relative expression of analysed genes was
were cloned into the pEGFP vectors, which, then, were transfected determined, normalizing to human Gusb or mouse Actb housekeeping
to 4T1 cells. Cells were selected using 2 μg ml−1 puromycin. To exog- gene expression.
enously express Sting1, Cxcl1, Ccl2 or Il11, cDNAs were cloned into viral
pLenti-EF1a-Bsd-P2A vector and were transduced with the lentiviral Cell stimulation with APOE for bulk and single-cell RNA-seq
system. For APOE treatment assays, 1 × 105 RAW264.7 cells were seeded in
24-well plates or 5 × 105 RAW264.7 cells were seeded in 6-well plates.
cGAMP quantification After 36 h, when culture plates were 80–90% confluent, medium with
For cGAMP quantification in cell lysates, cancer cells were seeded in APOE (3 μg ml−1) was added to the wells for 2 h. For scRNA-seq experi-
15-cm culture dishes. When culture plates were 80–90% confluent, ments, treated and non-treated cells from 24-well plates were mixed at
cells were washed with PBS twice then trypsinized for 5 min at 37 °C, equal cellular concentrations to generate 5,000 Gel Bead-In-Emulsions
and cells counts were measured. Cells were then centrifuged at ≥600g (GEMs), with an average initial cell viability of 93%. RNA purification
at 4 °C for 15 min. Whole cell lysates were generated by lysing the cell from the cells seeded in six-well plates was performed using the
pellet in LP2 lysis buffer (Tris HCl pH 7.7 20 mM, NaCl 100 mM, NaF Monarch Total RNA Miniprep Kit (New England BioLabs), and samples
10 mM, β-glycerophosphate 20 mM, MgCl 5 mM, Triton X-100 0.1% with high-quality RNA (RNA integrity number > 8.5) as measured using
2
(v/v), glycerol 5% (v/v)). The homogenate was then subjected to centrifu- 2200 TapeStation (Agilent Technologies) were used for bulk RNA-seq
gation at 10,000g for 15 min. For tumour samples, the tumour tissues library preparation. cDNA was processed with TruSeq Stranded mRNA
were homogenized in LP2 lysis buffer (1:10 w/v) with homogenizer. Library Preparation Kit (Illumina, 20020594) and sequenced with a
The homogenate was then subjected to centrifugation at 10,000g for NextSeq2000 instrument.
15 min. cGAMP ELISA was performed according to the manufacturer’s
protocol using DetectX Direct 2′,3′-Cyclic GAMP Enzyme Immunoassay In vitro TM treatment
Kit (Arbor Assay). For TM treatment, 0.5 × 104 cells were seeded in 6-well plates. When
cell confluence reached 70 per cent, media containing indicated con-
Immunoblotting centrations of TM (63 ng ml–1 for 4T1, 126 ng ml–1 for CT26, 210 ng ml–1
Cells were pelleted and lysed using RIPA buffer. Protein concentra- for B16F10 and 84 ng ml–1 for EO771.LMB) or dimethylsulfoxide were
tion was determined using BCA protein assay and 20–30 μg of total added. Cell lysates were collected at indicated time points and were
protein was loaded in each lane. Proteins were separated by gradient analysed (12 h for CT26, 11 h for B16F10 and 10 h for EO771.LMB). For
SDS–PAGE and transferred to PVDF or nitrocellulose membranes. the C-176 pretreatment experiment, cells were pretreated with 1 μM
Membranes were blocked with TBST buffer containing 5% BSA for C-176 or vehicle for 3 weeks, during which the medium was replaced
1 h and incubated with the primary antibody in 5% BSA TBST over- with freshly prepared medium with C-176 or vehicle and cells were split
night at 4 °C. The primary antibody information is listed in Supple- every 3 d. When cells were treated with TM and vehicle, C-176 and its
mentary Table 2. After three washes with TBST, membranes were vehicle were also present in the medium during treatment.
incubated with proper horseradish peroxidase (HRP)- or fluorescent
dye-conjugated secondary antibodies in TBST containing 3% BSA for 1 h In vitro cGAMP stimulation
at room temperature. After three washes with TBST, membranes using IMR90 cells were seeded at a density of 1 × 104 cells per well in 6-well
fluorescent dye-conjugated secondary antibodies were imaged using plates on day 0. For single-dose cGAMP stimulation, medium was
the LI-COR Odyssey system. For membranes using HRP-conjugated replaced with medium containing 10 μM cGAMP. For repetitive stimula-
secondary antibodies, signal was visualized using SuperSignal West tion, medium was replaced with fresh medium containing cGAMP every
Femto Maximum Sensitivity Substrate by Amersham Imager. Relative day. Gene expression analysis and immunoblots were performed as
STING protein levels were quantified by measuring band intensities described before. For 4-BPA (Enzo Life Technologies) treatment, cells
on immunoblots using ImageJ software, background subtracted and were stimulated with cGAMP in the presence of 5 mM 4-BPA. For STING
normalized to a loading control. inhibitor treatment, cells were pretreated with 0.5 μM H-151 (Invivogen)
Article
followed by stimulation with cGAMP in the presence of H-151. For the
poly(I:C) stimulation, cells were stimulated by transfecting 2 μg ml−1 Animal metastasis studies
poly(I:C) for 6 h at 24 h after the fifth cGAMP stimulation. Animal experiments were performed in accordance with protocols
approved by the MSKCC Institutional Animal Care and Use Committee.
Autophagy inhibition by BafA1 For survival experiments, power analysis indicated that 15 mice per
In 6-well plates, 0.5 × 106 4T1 WT and Cgas-KO cells were seeded per group would be sufficient to detect a difference at relative hazard ratios
well on day 0. On day 1, cells were treated with 0.5 μM BafA1 or vehicle of less than 0.25 or more than 4.0 with 80% power and 95% confidence,
together with 25 μg ml−1 cycloheximide. Cell lysates were collected and given a median survival of 58 d in the control group and a total follow-up
were analysed as described before. period of 180 d, accounting for accidental animal death during proce-
dures. For metastasis experiments relying on the tumour burden or lung
NK killing assay surface metastasis number, the animal numbers were estimated based
Primary NK cells were isolated from splenocytes of nude athymic mice on previous experience with these models. For in vivo experiments,
using EasySep mouse NK cell isolation kit (Stemcell Technologies, animals were randomly assigned to different groups. Investigators
19855) in accordance with the manufacturer’s protocol. The isolated were not blinded to group allocation. For tail-vein injections, 5 × 104 4T1,
NK cells were then seeded with tumour cells at a ratio of 1:10 (tumour: 1 × 105 4T1-Luc, 2.5 × 104 B16F10 or 105 CT26 cells were injected into the
NK cells) in media supplemented with 20 ng ml−1 IL-12 (BioLegend, tail-vein of 6–7-week-old BALB/c (4T1 and CT26) or C57BL/6 (B16F10)
577002) and 10 ng ml−1 IL-15 (BioLegend, 566302). After 16 h of cocul- female mice. For experiments using immune-deficient mice, 2.5 × 104
ture, wells were washed with PBS twice to remove dying tumour cells 4T1, 1 × 105 4T1-Luc, 1.25 × 104 B16F10, 5 × 104 CT26 or 2.5 × 105 EO771.
and floating NK cells and the remaining adherent tumour cells were LMB cells were injected into 6–8-week-old NSG mice (JAX:005557).
collected and counted. Metastasis was primarily assessed through overall survival. Overall
survival end point was when the mice died or met the criteria for
T cell killing assay euthanasia under the Institutional Animal Care and Use Committee
Primary T cells or CD8+ T cells were isolated from splenocytes of BALB/cJ protocol. Pain and distress were monitored by observing the pres-
mice using EasySep mouse T cell isolation kit (Stemcell Technolo- ence of rapid weight loss, weight loss exceeding 20% of body weight,
gies, 19851) or CD8+ cell isolation kit (Stemcell Technologies, 19853) hunched posture, lethargy, lack of movement, rapid growth of tumour
in accordance with the manufacturer’s protocol. Isolated T cells or CD8+ masses, mass larger than 2 cm3, gait abnormalities, lesion interfering
T cells were activated with 20 ng ml−1 IL-2 (BioLegend, 575402) for 24 h with eating and drinking, anuria, ulcerated tumour, change in stool
before being seeded with tumour cells at a ratio of 1:5 (tumour:T cells/ shape and/or size, and vaginal bleeding. Mice exhibiting any of these
CD8+ T cells). After 24 h of coculture, wells were washed with 1 × PBS signs were euthanized. Transplanted tumours were not to exceed 20%
twice and remaining adherent cells were collected and counted. in any dimension or 10% of body weight. Surface lung metastases were
assessed at end point by direct visual examination after euthanasia, at
Macrophage polarization assay which point lungs were perfused and fixed in 4% paraformaldehyde
Primary macrophages were collected from bone marrow of BALB/cJ (4T1, EO771.LMB and B16F10 experiments) or stained using India ink
mice and differentiated into M1 macrophages as previously described54. (CT26 experiments). Furthermore, lung metastasis after injection of
After 7 d of the differentiation process, differentiated M1 macrophages 4T1 cells was qualitatively assessed using routine H&E staining. For
were cultured with conditioned medium from tumour cells for 24 h. 4T1 orthotopic tumour implantation, 2.5 × 105 4T1 cells in 50 μl of PBS
Then, macrophages were collected, and RNA isolation was performed were mixed 1:1 with Matrigel (BD Biosciences) and injected into the
using the RNAeasy mini plus kit (Qiagen, 74134). mRNA expression of fourth mammary fat pad. For EO771.LMB orthotopic tumour implanta-
Arginase1 from RT–PCR was employed as a proxy measurement of M1 tion, 2.5 × 105 EO771.LMB cells in 50 μl of Hanks’ Balanced Salt Solution
polarization to M2 macrophages. were implanted. Only one tumour was implanted per animal. Primary
tumours were surgically excised on day 7 (4T1) or day 14 (EO771.LMB)
Transwell migration assay after implantation and metastatic dissemination was assessed by
Splenocytes collected from spleens of BALB/cJ mice were seeded in the monitoring overall survival or through quantification of surface lung
top compartment of a Transwell chamber with 3-μm pore size (Corning, metastases upon euthanasia on day 30. The length (L) and width (W) of
3462). Tumour cells were seeded in the bottom compartment 24 h the primary tumours were measured using callipers. Tumour size was
before the addition of splenocytes. After 48 h of incubation, media calculated according to the following formula: L × W2/2.
from the bottom compartment were collected and numbers of immune
cells were calculated. Bioluminescence imaging to monitor metastatic progression
4T1 cells were transduced with lentiviral particles encoding firefly lucif-
Flow cytometry analysis erase under control of the CAG promoter with an RFP–blasticidin fusion
Primary tumours arising by implanting 2.5 × 105 GFP-expressing 4T1 dual selection marker (Amsbio, LVP571). Transduced cells were grown
cells in 100 μl of PBS:Matrigel (1:1) into the mammary fat pads were in selection media containing 20 μg ml−1 blasticidin for 2 weeks, then
resected on day 10. Tumour pieces were digested to single-cell sus- sorted for a narrow range of medium RFP expression. Plasmids encoding
pensions with Collagenase/Hyaluronidase (Stemcell Technologies, enhanced specificity SpCas9 (eSpCas9), a customized guide RNA, and
catalogue no. 07912) and DNAase I (Stemcell Technologies, catalogue GFP were purchased from Genscript (eSpCas9-2A-GFP (PX458)). Guide
no. 100-0762) according to the manufacturer’s manual, followed by sequences for murine Cgas were: 5′-GGCCAUGCAGAGAGCUUCCG-3′
filtration with 70-μM cell strainers. Cells were stained with Zombie and 5′-CGAGUCUCCGGCUGCCCCCG-3′. The guide sequence for murine
NIR Fixable Viability Kit (BioLegend, catalogue no. 423105) for 10 min Trac was: 5′-UUCUGGGUUCUGGAUGUCUG-3′. For Cgas-KO cells,
on ice, followed by blocking with TruStain FcX (anti-mouse CD16/32) RFP-luc-4T1 cells were transiently transfected with both Cgas-targeting
antibody (BioLegend, catalogue no. 101319). Cells were then stained plasmids simultaneously. For Trac KO (cutting, but non-expressing
with fluorophore-conjugated antibody solution in PBS containing 2% control) cells, RFP-luc-4T1 cells were transiently transfected with the
FBS on ice for 30 min. The primary antibody information is listed in Trac-targeting plasmid. After 2 d, cells were sorted for GFP expression.
Supplementary Table 5. After washing with PBS, cells were analysed These cells were allowed to expand for 2 weeks. A second round of
using the Cytek Aurora Flow Cytometry System. Data were analysed transient transfection and GFP-based sorting was performed to obtain
with FlowJo software. polyclonal cell lines with greater than 95% KO efficiency by western blot.
Experimental metastasis assays were performed by injecting 100,000 (Illumina, 20020594) and sequenced on the Illumina NovaSeq platform.
4T1 (Luc-RFP) cells in the tail-vein of female BALB/cJ (Jackson Labora- Reads were mapped to the mouse reference GRCm38 with the Broad
tory, stock no. 000651) mice. For the metastasis assay with NSG mice, Picard Pipeline (http://broadinstitute.github.io/picard/). Gene
50,000 4T1 (RFP-Luc) cells were injected in the tail-vein of female expression levels were estimated with GenomicAlignments (v.1.18.1)57.
NSG mice (stock no. 005557). In all experiments, 5–7-week-old mice Differential analysis was performed by DESeq2 (v.1.24.0)58. Gene set
were used. The cells were re-suspended in PBS and passed through enrichment analysis was performed on the normalized reads estimated
a 70-μm cell strainer and injected in a final volume of 100 μl of PBS. by DESeq2. Genes downregulated in C-176-treated cells were filtered by
To detect lung metastasis, animals were injected retro-orbitally with two cutoffs: adjusted P value less than 0.05 and log-transformed FC
2
100 μl of luciferin (PerkinElmer, XenoLight d-Luciferin Potassium (C-176 versus vehicle) less than −1. Genes downregulated in Sting1
Salt, catalogue no. 122799) diluted in PBS (final concentration of KO were filtered by two cutoffs: adjusted P value less than 0.1 and
16.67 mg ml−1). Luminescence was measured twice a week with an IVIS log-transformed FC less than −1.
2
spectrum device (PerkinElmer, CLS136331 IVIS Lumina LT Inst, Series III,
120 V), starting straight after the tail-vein injection on day 0. Mice were Dissociation of murine tumours for scRNA-seq
checked twice a day and euthanized when showing any signs of illness Animal experiments were performed in accordance with protocols
or distress. approved by the MSKCC Institutional Animal Care and Use Com-
mittee. First, 1.25 × 105 4T1 cells in 50 μl of PBS were mixed 1:1 with
Analysis of cGAS and STING protein expression in breast tumour Matrigel (Corning) and injected into the fourth mammary fat pad of
samples 7-week-old BALB/c immune competent mice. Primary tumours were
Primary analysis of cGAS and STING protein expression was performed resected under sterile conditions 14 d after orthotopic implanta-
on a tissue microarray of 217 formalin-fixed, paraffin-embedded TNBC tion. The entire tumour was immediately placed in RPMI medium
samples. Samples and follow-up data were collected under MSKCC (Corning) on ice and dissociated using both mechanical and enzy-
Institutional Review Board approval. Patients gave consent accord- matic digestion (Mouse Tumor Dissociation Kit no. 130-096-730,
ing to the institutional review board-approved standard operating Miltenyi Biotec), generally within 1 h of surgical resection. Tissues
procedures for informed consent. Written, informed consent was were minced with a razor blade in the Miltenyi enzyme mix according
obtained from all patients. The study was conducted in accordance to the manufacturer’s specifications and transferred to a Gentle MACS
with the Declaration of Helsinki and good clinical practice guidelines. Octo Dissociator with heaters (no. 30-096-427, 37 °C) for further
There were three cores per tumour sample. Of the 217 samples, 183 mechanical dissociation. Upon dissociation, cell suspensions were
and 180 samples had sufficient material for adequate assessment of passed through a 70-μm filter and washed twice with FACS buffer (2%
cGAS and STING expression levels, respectively. This included 179 heat-inactivated FBS, 1 mM EDTA and Pen/Strep in PBS without Ca or
samples with adequate expression and quality to simultaneously Mg). The remaining cell suspensions were subsequently flow sorted
quantify both proteins. Detailed clinical characteristics and clinical with a BD FACSAria II cell sorter fitted with a 100-μm nozzle to enrich
follow-up data were previously reported55. Immunohistochemistry for viable, single cells according to forward and side scattering, and
for cGAS and STING was performed on the automated Discovery XT DAPI exclusion. Cells were sorted directly into RPMI medium with 10%
processor (Ventana Medical Systems) by the Molecular Cytology Core FBS, washed three times and re-suspended in PBS with 0.04% BSA for
Facility at MSKCC56. Briefly, after deparaffinization and tumour tissue single-cell encapsulation. Final cell concentrations were determined
conditioning, the antigen was retrieved using standard CC1 (Ventana with a haemocytometer.
Medical Systems). Following blockage with Background Buster
(Innovex), the slides were incubated with 1:100 diluted anti-STING scRNA-seq library preparation
antibody for 4 h, and then incubated with the biotinylated secondary The 10X Genomics Chromium platform was used to generate a tar-
antibody for 30 min. The Streptavidin-HRP D kit (DABMap kit, Ventana geted 5,000 single-cell GEMs per sample, loaded with an average initial
Medical Systems) and the Alexa Fluor 488 Tyramide SuperBoost Kit, cell viability of 87%. scRNA-seq libraries were prepared following the
Streptavidin (Life Technologies, catalogue no. B40932) were used 10X Genomics user guide (Single Cell 3′ V2 Reagent Kits User Guide
to detect the signal according to the manufacturer instructions. A PN-120233, 10X Genomics). After encapsulation, emulsions were
similar procedure was then applied to detect cGAS with 1:100 diluted transferred to a thermal cycler for reverse transcription at 53 °C for
anti-cGAS antibody and Alexa Fluor 594 Tyramide SuperBoost Kit, 45 min, followed by heat inactivation for 5 min at 85 °C. cDNA from
Streptavidin (Life Technologies, catalogue no. B40935). Slides were the reverse transcription reaction was purified using DynaBeads
counterstained with haematoxylin and were mounted with Permount MyOne Silane Beads (Thermo Fisher Scientific) and amplified for 12
mounting medium. Slides of immunofluorescence and immunohisto- cycles using Amplification mix and primers provided in the Single
chemistry were scanned with a Pannoramic Flash 250 (3DHistech) with Cell 3′ reagents module 1 (10X Genomics). After purification with 0.6X
×20/0.8 numerical aperture air objective by the Molecular Cytology SPRIselect beads (Beckman Coulter), cDNA quality and yield were evalu-
Core Facility at MSKCC. cGAS and STING protein expression levels ated using Agilent Bioanalyzer 2100. Using a fragmentation enzyme
were assessed manually using scores of 0 (absent), 1 (weak), 2 (mod- blend (10X Genomics), the libraries were fragmented, end-repaired
erate) and 3 (strong). STING expression was assessed separately in and A-tailed. Products were double-side cleaned using 0.6X and 0.8X
the tumour and stromal compartments. cGAS was rarely localized SPRIselect beads, and adaptors provided in the kit were ligated for
to micronuclei in the stroma and therefore was primarily assessed in 15 min at 30 °C. After cleaning ligation products, libraries were ampli-
the tumour compartment. DMFS data were collected by reviewing fied and indexed with unique sample index i7 through PCR amplifi-
medical records available at MSKCC. Tumours were categorized as cation. The number of PCR cycles was chosen based on cDNA yield
having low (negative or weak) or high (moderate or strong) cGAS or for each sample individually. Final libraries were double-side cleaned
STING expression. using 0.6X and 0.8X SPRIselect beads and their quality and size were
evaluated using an Agilent Bioanalyzer 2100. Libraries were pooled
RNA-seq analysis and sequenced on a HiSeq2500 (Illumina) paired-end read flow cell
B16F10 cells were pretreated with 1 μM C-176 or dimethylsulfoxide for following recommendations in the 10X Genomics guide, sequenced
48 h, and media with fresh drug was added at 24 h. RNA was extracted for 26 cycles on the forward read (10X barcode + unique molecular
using the RNeasy Mini Kit (Qiagen, 74104). Non-strand-specific paired- identifier), followed by 8-base pair I7 index (sample index) and 98 base
end sequencing libraries were generated with TruSeq Stranded mRNA pairs on the reverse read.
Article
a categorical variable indicating sample source (CINhigh, CINlow or
ContactTracing to identify and map the effects of conditionally Sting1KD) and target is a binary parameter indicating cell membership
dependent cell–cell interactions in the receptor-expressing subset (target+). The zlm function results
ContactTracing exploits inter- and intrasample variability in single- in parameter estimates for each gene, including log(FC) estimates for
2
cell data to ask whether putative interactions, identified based on the how expression relates to condition and target status. We then use
co-occurrence of complementary ligand–receptor pairs in the TME59, MAST’s lrTest function to compute the change in likelihood when tar-
indeed yield a transcriptional response in target (receptor-expressing) get is dropped from the model. This produces a P value for each gene
cells that depends on condition-specific presence of ligand (Fig. 3a–c indicating whether the model including target as a covariate fits sig-
and Extended Data Fig. 4a–c). The model makes no assumptions nificantly better than a model without. Thus, significant P values
about what this ligand effect looks like, but rather infers genes and indicate genes whose expression is different between receptor-
processes associated with each cellular response based on intrinsic expressing (target+) and receptor-null (target−) subpopulations. We
variability in receptor expression (within the target cell type) and apply the Benjamini–Hochberg procedure to account for multiple
ligand abundance in the TME (Extended Data Fig. 4f); here, we focus hypothesis testing, yielding an FDR value per gene.
on ligands that are CIN- or STING-dependent. Finally, we map these
cellular response states, that is, ligand effects, back to individual Testing for condition-specific responses to receptor engagement
cells to ask whether multiple, distinct tumour subpopulations coop- in target cells. Fitted parameter values from the target test can reflect
eratively shape the TME and whether their abundance is dependent associations and are not causal if there is unobserved confounding
on perturbation of tumour-intrinsic CIN or Sting1 (Extended Data (correlation) between receptor expression and the expression of other
Fig. 4g,h). genes. However, we may exploit secondary variability in ligand avail-
ability across conditions to distinguish genes that are ligand effects
Database of complementary ligand–receptor pairs. To obtain an from those that happen to be co-expressed with the relevant receptor
interaction database as input to ContactTracing, we took the intersec- protein. Thus, for all interactions that involve a ligand that is differen-
tion of two databases: CellTalkDb60 (http://tcm.zju.edu.cn/celltalkdb/ tially expressed across conditions (CIN- or STING-dependent in any
download.php, accessed 26 March 2021) and the database used by cell type), we performed a second likelihood ratio test to determine
the CellPhoneDb59 (v.2.1.4) method. CellTalkDb has both human- and whether model fit improves with the addition of a condition-specific
mouse- specific databases, and we used the appropriate one for each interaction effect (Extended Data Fig. 4c). Thus, zlm fits the function:
species. CellPhoneDb is a human database; for the mouse analysis Y≈CDR+condition+target+condition_specific_interaction_effect,
we mapped the genes to the mouse genome as described in the next where condition_specific_interaction_effect is a categorical variable
section, ‘Mouse to human gene mapping’. CellPhoneDb includes ‘com- indicating a cell that is both expressing the receptor (target+) and from
plex’ ligands and receptors, where each complex consists of multiple a particular condition (that is, CINhigh). The lrTest function evaluates
genes. For any putative complex-mediated interactions, we added a the significance of including the condition_specific_interaction_effect
corresponding ‘complex gene’ to our scRNA-seq expression matrix covariate when modelling expression across all genes. The P values
whose expression is the minimum expression of all genes comprising produced by this test are significant when the transcriptional response
the complex. We removed any interactions where the ligand or recep- in receptor-expressing target cells differs across conditions (in this
tor were filtered from our scRNA-seq database for low expression. The case, through perturbation of tumour CIN or Sting1), with condition-
total mouse interaction database contains 1,885 interactions (1,261 specific ligand availability. Again, we apply the Benjamini–Hochberg
from CellTalkDb, 917 from CellPhoneDB, 293 of which overlap). The procedure to account for multiple hypothesis testing. Notably, the
total human interaction database contains 2,934 interactions (2,348 number of genes differentially expressed in receptor-expressing
from CellTalkDb, 846 from CellPhoneDb; 260 overlapping). versus -null target cells is highly correlated across conditions, while
those exhibiting an interaction effect (gene responses that differ in the
Mouse to human gene mapping. Human–mouse orthologs annotated presence of the ligand) are not (Extended Data Fig. 4d,e).
by the Jackson Laboratory (http://www.informatics.jax.org/downloads/
reports/HOM_MouseHumanSequence.rpt, accessed 1 March 2021) were Defining ligand effects in target cells. Altogether, target and interac-
used to map 79.3% of our mouse genes to human genes one-to-one. An tion tests were performed for all receptors and ligands in our database,
additional 23 mouse ligands and receptors were mapped to human crossed with all possible cell types in the TME. Target tests were per-
genes through capitalization, that is, Lgasl9 → LGASL9. Finally, we manu- formed within cells derived from the target cell type, conditioned on
ally dealt with six human genes that mapped to multiple mouse genes receptor expression; and interaction tests were performed in target
(HLA-A, SIRPB1, KLRB1, LILRB4, SAA1, CSF2RB). After inspecting expres- cell types when their complementary ligand was differentially
sion patterns of these multi-mapped genes, we mostly used the average expressed across conditions in the TME. Thus, the output consists of
expression across multiple orthologs for each gene to represent that P values and log(FC) estimates across all genes for each component
2
mapped ligand/receptor. The only exception was HLA-A, whose mouse of a putative cell–cell interaction. To functionally define transcrip-
orthologs exhibited several distinct patterns of expression and so was tional responses to a ligand–receptor-mediated interaction, we com-
dropped from further analysis. pute −log (P )×log (foldchange) from the target likelihood ratio
10 adj 2
test for each gene, where P is the Bonferroni-corrected P value. Ligand
adj
Testing for a transcriptional response in receptor-expressing tar- effects are then transcriptional response genes that exhibit a significant
get cells. We used the BioConductor package MAST61 (v.1.14.0) to interaction effect in the presence of the condition-specific ligand.
perform a likelihood ratio test between receptor-expressing (any For each cell type, we create a matrix of condition-specific transcrip-
molecules detected, target+) and receptor-null (no molecules detected, tional response vectors with rows corresponding to [receptor, target
target−) cells, within the target cell type, across all genes (Fig. 3b,c cell type] pairs and columns corresponding to all genes. Since each
and Extended Data Fig. 4a,b). We refer to this as the target test. The row of the matrix encodes both a cell type and a receptor, dependent
MAST function, zlm, fits a Hurdle model to the log-normalized expres- transcriptional responses can be evaluated across multiple cell types.
sion of each gene using generalized linear regression. We used the We then use scanpy to compute principal components on this matrix,
regression formula: Y≈CDR+condition+target, where CDR models choosing an optimal number of principal components for data dimen-
the cellular detection rate (fraction of genes detected in a cell, an impor- sionality based on kneepoint analysis of the cumulative variance
tant covariate for modelling single-cell expression data), condition is described by each component, and visualize in two dimensions with
UMAP (Extended Data Fig. 4f). Phenotypic states associated with recep- cells (Gr-MDSC)) or lymphoid (T cells, B cells, NK cells). Extended Data
tor expression in each cell type are computed according to Fig. 5c compares the distribution of all-versus-all connectivity scores,
−log (P )×log (foldchange) from the target likelihood ratio test compared with the subset of those with matching target cell types and
10 adj 2
for each gene, where P is the Bonferroni-corrected P value. We com- receptors. We used a Mann–Whitney test to determine that the connec-
adj
pute principle components and the DC1 on this matrix using Palantir tivity scores are significantly higher in the matched subset (P = 0.0031).
to identify genes that significantly correlate with this principle source
of variance. After removing scores of zero and rescaling correlation Benchmarking ContactTracing against existing methods that
values to the range [−1,1], we use these scores as input to gene set enrich- infer cell–cell interactions from single-cell data
ment analysis (GSEA), along with cell-type-specific GMT files (provided To compare the top set of interactions predicted by ContactTracing
in Supplementary Table 7), to assign pathways to these major axes of with those predicted by other cell–cell interaction models, we evaluate
biological variation. For example, macrophage transcriptional their intersection (Fig. 3e and Extended Data Fig. 6a,b) and colocali-
responses largely reflected underlying single-cell heterogeneity in zation in matched spatial transcriptomics data (Fig. 3f and Extended
IFN-γ responsiveness and polarization (Fig. 4a). Data Fig. 6c).
Mapping ligand–receptor-mediated effects to cellular subpopula- Implementation of alternative cell–cell interaction models. The
tions. To assign ligand effects to subclusters within the target cell type, expression counts and ligand–receptor databases used by Contact-
we took the dot-product between the transcriptional response score Tracing were loaded using the typical workflows required by each
(defined above) and the log(FC) of every gene in each cell subcluster respective tool. Counts matrices were split according to experimental
2
versus all other cells using the MAST statistical framework61 (Extended condition. For all instances that required conversion between human
Data Fig. 4g). The log(FC) per gene per cluster is set to zero before and mouse gene names, we followed the same procedure described
2
computing this dot-product when it is not significant (FDR > 0.15). above (‘Mouse to human gene mapping’). Since some methods are
The dot-product score is standardized by normalizing to its max, and unable to account for protein complex definitions, when necessary,
transcriptional response states (conditioned on receptor expression) complex interactions are split into all pairwise combinations of complex
are assigned to subclusters for standardized scores greater than 0.5; in components to a given ligand/receptor. Common approaches to under-
this way, transcriptional response states can be assigned to more than standing ligand–receptor-mediated interactions are based on tests that
one subcluster. Ligands are simply assigned to subclusters if they are compare co-expression of ligands and receptors across cell types. The
positively enriched (FDR < 0.15, log(FC) > 0) in that subcluster relative most common example of such tests is CellPhoneDB59. As many methods
2
to all other cells in the donor cell type as determined by MAST61. are difficult to supply with custom ligand–receptor databases, we use
the LIANA package (v.0.1.6)63, which reimplements many of these com-
Validating ligand effects predicted by ContactTracing mon methods. LIANA was configured to use the following methods:
We downloaded the CytoSig database of human cytokine responses ‘cellphonedb’, ‘connectome’, ‘logfc’ (iTALK), ‘natmi’, ‘sca’ (SingleCell-
(https://cytosig.ccr.cancer.gov/download /, accessed 11 February 2022). SignalR), ‘call_cellchat’ (CellChat) and ‘cytotalk’. Permutation-based
This database provides measurements for 2,002 experiments in which tests were set to use 10,000 permutations, and CellChat was set to
cells were treated with a cytokine, and the log-fold expression change use 1,000 bootstraps. NicheNet64 v.1.1.0 was also implemented using a
was measured across 19,918 genes. We mapped all genes in this data- custom ‘ligand–receptor network’ with author-recommended settings,
base to mouse genes in our dataset, yielding a mapped database of 740 which allowed us to integrate the same database of complementary
experiments with measurements in 13,013 genes. We then associated ligand–receptor pairs, while retaining the default ‘signalling’ and ‘gene
the ligands in the CytoSig database to their corresponding receptors regulatory’ networks. This new database was compiled using default
in our set of mouse interactions, and focused on ligand–receptor pairs optimized NicheNet hyperparameters. Since NicheNet is based on the
that are CIN-dependent (ligand log(FC) FDR < 0.05 and at least 1 signifi- Seurat toolkit, expression was preprocessed using a typical preprocess-
cant interaction effect). We found 115 CIN-dependent ligand–receptor ing workflow including its SCTransform ‘v2’ workflow (Seurat v.4.1.1,
pairs, from 75 distinct receptors, that were in the mapped CytoSig SCTransform v.0.3.3), with a consistent number of variable features as
database (in a total of 571 experiments across different cell types and used for ContactTracing. NicheNet was run on all pairwise combina-
conditions). We then compared every CIN-dependent transcriptional tions of cell types with recommended parameters and ligand/receptor
response measured by ContactTracing with each of the 571 cytokine activity was scored using NicheNet’s Pearson correlation coefficients.
responses measured by CytoSig. To compare the response vectors, A newer method for understanding cell–cell signalling is CellComm
we computed the connectivity score62, illustrated in Extended Data (part of the FUSCA package, v.1.3.1)65. Expression data were prepared
Fig. 5b, which is to test whether upregulated genes in one list are also for CellComm by following the typical FUSCA workflow demonstrat-
upregulated in another, without making many assumptions about the ed by the authors: counts were filtered to require a minimum of 100
distributions of values in the lists. ContactTracing upregulated genes genes expressed per cell and a minimum of 10 cells expressing each
have a log(FC) > 0 from the target test, and are CIN-specific (interac- gene, then processed using the ‘Normalize’ and ‘scaleData’ functions.
tion test FDR < 0.05). We then apply the connectivity score to this set The CellComm algorithm was run by computing co-expression pat-
of cytokine response genes in CytoSig; the larger the score, the more terns with minimum mean expression set to 0.2, using 10,000 cluster
these genes are also upregulated in CytoSig. We get a distribution of permutations across cell types. CellComm P values were calculated
connectivity scores from our all-versus-all comparison. We then take a using 1,000 permutations.
subset of these comparisons in which the target genes (receptor) are the
same in each database, and the cell types are generally matched. There Application of cell–cell interaction models to human and mouse
was a large variety of cell type names used in the CytoSig database; we data. When running tools on spatially matched human TNBC and ER
manually created a mapping to ContactTracing cell types according to data25, we ran the typical workflow for each tool as described above
Supplementary Table 10 (many remain unmapped); we consider cell on each condition independently so that each condition’s colocali-
types ‘roughly matched’ if they both belong in one of the following zation could be evaluated independently. To compare the results of
sets: epithelial/stromal (tumour cells, fibroblast cells); myeloid (mac- ContactTracing with other tools in the mouse model of CIN, we ran
rophages/myeloid-derived suppressor cells (mMDSC), plasmacytoid LIANA-based methods on condition-specific counts matrices sepa-
dendritic cells (pDC), classical dendritic cells (cDC), polymorphonu- rately. As a substitute for the lack of condition-dependent analyses
clear neutrophils (PMN)/granulocytic myeloid-derived suppressor on those methods, we calculated a post hoc score for each method
Article
measuring the differential magnitude across conditions by comput- detection of significant sample-specific effects, Harmony68 was applied
ing the absolute value of the difference of CINhigh and CINlow scores, for batch correction to the full log-transformed count matrix to gener-
and if P values were reported we selected the most significant value ate the default n = 100 corrected Harmony principal components. Using
to be representative. These scores were then used to rank reported the optimal number of principal components selected before and after
interactions from LIANA. To incorporate experimental conditions batch correction (n = 17 and n = 19, respectively), sample mixing was
from the mouse model in NicheNet results, we used the full counts noticeably improved in immune cell subsets; thus, corrected Harmony
matrices (which includes both conditions) with the recently published principal components were used for downstream differential abun-
‘Differential NicheNet’ workflow, using ‘min_lfc’ specificity scores with dance testing (Extended Data Fig. 12c,d). To validate CIN-dependent
an author-recommended cutoff of 0.15. While the typical Connectome findings from the 4T1 mouse model, we focused on the eight TNBC
scores are implemented in LIANA, the original implementation contains samples that had tumour cells present in the data. To separate these
a ‘Differential Connectome’ workflow66 which would allow for explicit eight samples into expected ‘CINlow’ and ‘CINhigh’ groups, we used the
consideration of experimental conditions. Since it is also Seurat-based, standard inferCNV i6 HMM model69 to detect copy number variants
we used the same data as prepared for Differential NicheNet and ran (CNVs) within the tumour cell compartment for each sample (applied
the method according to the author-recommended usage to analyse to raw data). As a measure of CIN, we computed the Shannon diversity
and calculate P values. While CellComm does not explicitly have a ‘Dif- index of the variant states, weighted by the number of copy number
ferential’ workflow, it has a ‘subcluster’ workflow which we used by alterations in each variant, for all tumour cells in each sample:
setting experimental condition as the ‘cluster’ and cell-type annotation
n
as the ‘subcluster’. CNV =∑−s×ln(s)
SDI i i
i=1
Comparing predicted interactions across models. As ContactTrac-
ing and alternative methods are run with a consistent ligand/receptor where n is the number of unique predicted variants in current sample
database, results differ only in terms of detection sensitivity and pri-
freq ×δ
oritization. Thus, interactions are compared in terms of set overlap s= i i
(Fig. 3e and Extended Data Fig. 6a) and ranked differences (Extended i ∑n freq ×δ
i=1 i i
Data Fig. 6b). For comparison, we required interactions to be present
in both conditions and collapsed interactions to unique (target cell where freq is the proportion of variant i in current sample and δ is
i i
type, receptor) pairs. First, all methods that report a P value had results the sum of the absolute values of the predicted difference from normal
filtered using a 0.05 threshold. Next, for each target cell type/receptor across all chromosome positions for variant i. This CNV metric not
SDI
pair, the maximum significant reported score (regardless of source only captures the diversity in the unique CNV states detected in the
cell type and ligand) was selected to be the representative score for sample, but it also accounts for how altered these states are predicted to
each target cell type/receptor pair. Rankings were then determined be from diploid. As expected, the CNV was markedly higher in CINhigh
SDI
by sorting target cell type/receptor pairs according to previously mouse samples (Extended Data Fig. 1l) and was used in conjunction
described maximum scores. Similarly, ContactTracing target cell type/ with the mean tumour cell expression of key pathways (Type 1 IFN,
receptor pairs were first filtered by requiring at least one significant CIN signature, Non-Canonical Nf-Kb and Hallmark UPR) to cluster the
interaction term (FDR < 0.05) in the target cell type for ligands that eight human TNBC samples into CINlow (n = 4) and CINhigh (n = 4) subsets
were differentially expressed across conditions in any donor cell type (Extended Data Fig. 12a). We then used the Milo70 python framework
(absolute log(FC) > 0 and FDR < 0.05). The ContactTracing target cell to compute differentially abundant neighbourhoods within the TNBC
2
type/receptor pairs were then sorted by the number of significant inter- subset between the inferred CINlow and CINhigh samples (k = 15, P = 0.5
action terms, with ties broken by secondarily sorting according to the and d = 22). The mapped cell subtype annotations were used to label
number of DEGs for a given target cell type/receptor pair. Since the each neighbourhood based on the mode cell subtype and log(FC)
2
methods had variable numbers of results reported, overlap coefficients values were mapped to the single-cell resolution in the same manner
were calculated to represent set similarity. The overlap coefficient is a as described in Supplementary Note 5. ContactTracing was likewise
set size-invariant metric for similarity that is related to the Jaccard applied to these human data to detect CIN-specific ligand effects, as
index. While the Jaccard index for sets X and Y is calculated as described in the section above (‘ContactTracing to identify and map
Jaccard=∣X∩Y∣, the overlap coefficient corrects for set size difference the effects of conditionally dependent cell–cell interactions’).
∣X∪Y∣
by normalizing set intersection cardinality by minimum set cardinal- The breast cancer dataset also includes matched Visium spatial tran-
ity rather than the cardinality of the union between sets, that is, scriptomics data from four of the samples: two patients with TNBC
Overlap= ∣X∩Y∣ . Similarly to the Jaccard index, overlap coefficients and two ER+ patients. We ran ContactTracing on the scRNA-seq data for
min(∣X∣,∣Y∣)
range from 0 to 1, where 1 represents the highest degree of overlap. All these samples separately, comparing TNBC versus ER+ conditions. We
pairwise combinations of ranked result lists were then used to calculate used the output from ContactTracing to rank interactions relevant to
corresponding overlap coefficients for various rank thresholds. each condition; interactions identified by [ligand, receptor, receptor
cell type] are ranked by the number of significant interaction effects,
Validation within an independent human breast cancer cohort multiplied by the identity function that indicates whether the ligand is
To validate the relevance of key biological findings in human breast upregulated in at least one cell type for the relevant condition. There-
cancers, we obtained scRNA-seq data from a publicly available cohort fore, there is a different ranking of interactions relevant to TNBC, and
of 26 primary breast cancer tumours (11 ER+, 5 HER2+ and 10 TNBCs)25. of those relevant to ER+. For each of the four patients, we then used the
To compare cell subtypes between the human and mouse cell atlases, relevant ranking, and assessed whether top TNBC or ER+ interactions
we mapped the subtype annotations provided by Wu et. al.25 to the tended to colocalize in the spatial data for patients in corresponding
most similar cell subtype in the mouse for all immune cells where a breast cancer subtypes (Fig. 3f). Colocalization was determined by sum-
corresponding cell subtype was present (Supplementary Table 10). ming the product of [log(ligand expression), probability or Pr(target
This was done using subtype-specific DEGs and pathways provided by cell type), Identity(receptor expressed)] across all cells in the spatial
the original authors and recomputed using our pipeline. Most original data for an individual. Ligand expression was then permuted 100 times
DEGs and annotations published were validated by our analyses, except and the colocalization statistic recomputed to obtain a colocalization
for the Myeloid:c8 S100A9+ cluster, which we classify as mMDSCs based P value (Extended Data Fig. 6c). The probability of a target cell type in
on their upregulation of S100A8 and S100A9 (ref. 67). Following the each Visium spot was determined using the deconvolution software
