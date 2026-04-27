---
source_path: /mnt/c/Users/Administrator/Zotero/storage/FTLYECY5/Yuan 等 - 2025 - VDAC2 loss elicits tumour destruction and inflammation for cancer therapy.pdf
ingested: 2026-04-23
sha256: d5cdc795122ac6b1
---

Article
VDAC2 loss elicits tumour destruction and
inflammation for cancer therapy
https://doi.org/10.1038/s41586-025-08732-6 Sujing Yuan1,4, Renqiang Sun1,4, Hao Shi1, Nicole M. Chapman1, Haoran Hu1, Cliff Guy1,
Sherri Rankin1, Anil KC1, Gustavo Palacios1, Xiaoxi Meng1, Xiang Sun1, Peipei Zhou1,
Received: 7 April 2024
Xiaoyang Yang2, Stephen Gottschalk3 & Hongbo Chi1 ✉
Accepted: 3 February 2025
Published online: xx xx xxxx
Tumour cells often evade immune pressure exerted by CD8+ T cells or immunotherapies
Open access through mechanisms that are largely unclear1,2. Here, using complementary in vivo
Check for updates and in vitro CRISPR–Cas9 genetic screens to target metabolic factors, we established
voltage-dependent anion channel 2 (VDAC2) as an immune signal-dependent
checkpoint that curtails interferon-γ (IFNγ)-mediated tumour destruction and
inflammatory reprogramming of the tumour microenvironment. Targeting VDAC2
in tumour cells enabled IFNγ-induced cell death and cGAS–STING activation, and
markedly improved anti-tumour effects and immunotherapeutic responses. Using a
genome-scale genetic interaction screen, we identified BAK as the mediator of VDAC2-
deficiency-induced effects. Mechanistically, IFNγ stimulation increased BIM, BID
and BAK expression, with VDAC2 deficiency eliciting uncontrolled IFNγ-induced
BAK activation and mitochondrial damage. Consequently, mitochondrial DNA was
aberrantly released into the cytosol and triggered robust activation of cGAS–STING
signalling and type I IFN response. Importantly, co-deletion of STING signalling
components dampened the therapeutic effects of VDAC2 depletion in tumour cells,
suggesting that targeting VDAC2 integrates CD8+ T cell- and IFNγ-mediated adaptive
immunity with a tumour-intrinsic innate immune-like response. Together, our
findings reveal VDAC2 as a dual-action target to overcome tumour immune evasion
and establish the importance of coordinately destructing and inflaming tumours to
enable efficacious cancer immunotherapy.
Immunotherapies such as adoptive cell therapy (ACT) and immune mitochondrial complex I16 or autophagy17, in cancer cells reinvigorates
checkpoint blockade (ICB) show considerable clinical benefits for anti-tumour immunity and ICB. However, we lack a systemic under-
cancer treatment1,2. CD8+ T cells contribute to the cancer–immunity standing of the molecules or pathways in tumour cells that mediate
cycle and immunotherapeutic effects3 by releasing cytotoxic granules4 immune escape, including those related to metabolism and associated
and producing pro-inflammatory cytokines5. In particular, IFNγ con- signalling events.
tributes to tumour control by increasing tumour antigen presentation
and production of chemokines that mediate immune cell recruitment
VDAC2 mediates tumour immune evasion
and remodelling of the tumour microenvironment (TME). Accordingly,
IFNγ signalling is key to the immunotherapeutic success of ACT and To identify metabolism-associated factors underlying tumour immune
ICB6,7. Nonetheless, immunotherapies do not achieve sustained clinical evasion, we transduced Cas9- and ovalbumin (OVA)-expressing B16F10
responses in most patients with solid tumours1,2,8, with loss-of-function (B16-OVA) melanoma cells with a single guide RNA (sgRNA) library
mutations in IFNγ-pathway-related genes accounting for such therapeu- targeting 3,017 metabolism-associated genes18, and performed CRISPR
tic resistance in a small population of patients9,10. As it remains unclear drop-out screens19 under conditions of T cell-mediated immune pres-
how the majority of cancers evade immunosurveillance11, targeting sure (Fig. 1a and Methods). sgRNAs targeting Vdac2 were among the
the mechanisms that overcome tumour resistance to IFNγ and CD8+ top depleted sgRNAs in tumour cells responding to immune pressure
T cell-induced cytotoxic effects holds promise for inducing potent in vitro and in vivo (Fig. 1b,c, Extended Data Fig. 1a and Supplemen-
anti-tumour effects and maximizing immunotherapeutic responses. tary Table 1a–d), suggesting its role in tumour immune evasion. To
The TME is characterized by nutrient competition and metabolic validate these findings, we transduced Cas9-expressing B16-OVA
communication between cancer cells and immune cells that con- tumour cells with two independent sgRNAs targeting Vdac2 (or
tribute to the tumour immune escape12–15. Furthermore, targeting non-targeting control, NTC) to mediate Vdac2 deletion (Extended Data
metabolism-associated processes, including electron flow through Fig. 1b and Supplementary Table 2). VDAC2-deficient B16-OVA tumour
1Department of Immunology, St. Jude Children’s Research Hospital, Memphis, TN, USA. 2Experimental Cellular Therapeutics Laboratory, St. Jude Children’s Research Hospital, Memphis, TN,
USA. 3Department of Bone Marrow Transplantation and Cellular Therapy, St. Jude Children’s Research Hospital, Memphis, TN, USA. 4These authors contributed equally: Sujing Yuan, Renqiang
Sun. ✉e-mail: hongbo.chi@stjude.org
Nature | www.nature.com | 1
Article
sgVdac2 sgPigu sgPde4b sgExt1 sgFitm2
sgPigk
50
cells were more sensitive to OT-I-mediated cytotoxicity (Fig. 1d and to anti-PD-L1 and anti-PD-1 in B16-OVA and MC38 tumour models,
Extended Data Fig. 1c) but showed undisturbed in vitro proliferation respectively (Fig. 1f,g), and tumour-free mice after ICB therapy were
(Extended Data Fig. 1d). Also, Vdac2 deletion in MC38-OVA tumour protected against tumour rechallenge (Fig. 1f,g), indicating robust
cells increased their sensitivity to OT-I-cell-mediated killing (Extended induction of long-term immune memory. In a metastatic tumour
Data Fig. 1b,e). After transplantation into immunocompetent wild-type model, VDAC2 loss reduced the lung tumour burden and extended
mice, VDAC2-deficient tumour cells showed greatly reduced growth, mouse survival in an adaptive-immune-dependent manner (Extended
associated with extended mouse survival, while such phenotypes Data Fig. 1i–l). Given that unresponsiveness to tumour necrosis factor
were not observed in immunodeficient Rag1−/− mice (Extended Data (TNF) represents a major therapeutic barrier to ICB20, we generated
Fig. 1f,g), suggesting adaptive-immune-dependent effects. Moreover, B16-OVA tumour cells lacking both VDAC2 and TNF receptor (TNFR;
VDAC2-deficient tumours were markedly sensitized to OT-I-mediated encoded by Tnfrsf1a) to test whether VDAC2 targeting overcomes ICB
therapeutic effects in an ACT model (Fig. 1e and Extended Data Fig. 1h). resistance in TNF-unresponsive tumours. Although TNFR-deficient
Together, these results indicate that VDAC2 targeting sensitizes tumour tumours were resistant to OT-I-cell- or IFNγ- and TNF-induced killing21,
cells to CD8+ T cell-mediated killing in vitro and in vivo. Vdac2 co-deletion improved their responsiveness to these treatments
We next tested whether VDAC2 deficiency influences ICB efficacy. (Extended Data Fig. 1m,n). Furthermore, Vdac2 co-deletion also sen-
VDAC2 deficiency in tumours greatly improved responsiveness sitized TNFR-deficient tumours to anti-PD-L1 ICB therapy (Fig. 1h and
2 | Nature | www.nature.com
)%( lavivruS
b
e f g sgNTC + isotype (n = 7) sgVdac2 + isotype (n = 8)
sgNTC + anti-PD-L1 (n = 10) sgVdac2 + anti-PD-L1 (n = 10) 100
50
0
0 10203040
Days after inoculation
h
CTNgs
2cadVgs
sgNTC (n = 7) sgVdac2 (n = 7)
sgNTC + OT-I (n = 6) sgVdac2 + OT-I (n = 7)
7
Days after inoculation
*** ***
***
*** d
11 15 19
)%( ytilibaiv
llec ruomuT
sgNTC
sgVdac2 120 NS
90 60 *** *** 30 ***
0
0:1 0.25:1 0.5:1 1:1
E:T ratios
)%( lavivruS
Vdac2, Pigu, Pigk,
Fitm2, Pde4b, Ext1
100
50
0
0 1020304050
Days after inoculation
erocs ARR
KCeGAM
c
10–4 10–3 10–2
10–1
10–0
0 1,0002,0003,000
Rank
25
10 5
0
100
sgNTC sgNTC sgVdac2
sgVdac2
)3mm
201×( ezis ruomuT
)3mm
201×( ezis ruomuT
15
20 10 15 5
0
11 40 713192560 80
Days after inoculation Days after inoculation
)3mm
201×( ezis
ruomuT
)3mm
201×( ezis ruomuT
)3mm
201×( ezis
ruomuT
15
10 5
0
7 1519 6080100
6 *** 4
2
0
Day 25
j
)g( thgiew
reviL
ydob/reviL )%( oitar
thgiew
25 15
20 15 10 2 2 5 0 *** 10 5 15
5 10
0 0 5 7 11 15 19 7 13 19 25 0
Day 25
Days after inoculation Days after inoculation
sgVdac2
NS
a
MC38
i
k l
)%( ytilibaiv
llec
ruomuT
m
1 9 2 0 0 NS *** s s g g N VD TC AC2
60 **
3 0 0 ** * 0 0:1 0.125:1 0.25:1 0.5:1 1:1
E:T ratios
)%( +DAA-7+V-nixennA
Isotype sgNTC + sgNTC (n = 5) Anti-PD-L1 sgVdac2 + sgNTC (n = 5) sgNTC + sgTnfrsf1a (n = 5) sgVdac2 + sgTnfrsf1a (n = 5)
sgNTC 0 ng ml−1 sgVDAC2 sgNTC 0.05 ng ml−1 60 *** 0.1 ng ml−1 40
1 ng ml−1 20 NS
10 ng ml−1
*** ***
*** ******
***
sgNTC + isotype sgVdac2 + isotype
sgNTC + anti-PD-L1 sgVdac2 + anti-PD-L1
*** ******
***
sgNTC + isotype (n = 6) sgVdac2 + isotype (n = 7)
sgNTC + anti-PD-1 (n = 8) sgVdac2 + anti-PD-1 (n = 6)
*** ***
*** **
sgNTC + isotype sgVdac2 + isotype
sgNTC + anti-PD-1 sgVdac2 + anti-PD-1
***
*** *
*** *
sgNTC + sgNTC (n = 7) sgVdac2 + sgNTC (n = 8) sgNTC + sgTnfrsf1a (n = 7) sgVdac2 + sgTnfrsf1a (n = 8) *** ***
B16-OVA
IFNγ (h)
)301×( sllec
daeD
10 5
0
)301×( sllec
daeD
Lentiviral sgRNA metabolic Input C57BL/6 + OT-I versus Rag1−/−
sublibrary Non-treated (in vivo)
(9,55 3 1 ,0 s 1 g 7 R g N e A n s e s t ) a × rg 2 e ting (E O :T T = -I 0 tr . e 5 a :1 tm , 1 e 8 n t h) OT v -I e t r r s e u a s ted C v 5 e 7 rs B u L s / 6 R a + g O 1− T /− -I 14 days culture Rag1−/− mice DNA isolation and no (i n n - t v r i e tr a o te ) d (in vivo) Tumour 17 days deep sequencing 94 6 94
B16-OVA Injection (s.c.)
C57BL/6 mice
7 days 10 days
OT-I cell adoptive transfer
+ OT-I 36 h
+B7-H3-CAR T 36 h 10 5
0 8 16 24 0 0
I
8
FNγ (
1
h
6
)
24 Untreated
IFNγ
72 h
Fig. 1 | VDAC2 deficiency sensitizes tumours to IFNγ-induced cell death anti-PD-1 group (left). Right, the survival of mice after primary tumour challenge.
and immunotherapy. a, Schematic for CRISPR screening in B16-OVA tumour h, Indicated sgRNA-transduced B16-OVA tumour growth after the indicated
cells. Created in BioRender. Sun, R. (2025) https://BioRender.com/g06b183. treatments. i,j, Liver tumour burden (i) and histological analyses (j) at day 25.
b, The top depleted genes in tumour cells from C57BL/6 + OT-I cell versus n = 4 (sgNTC) and n = 8 (sgVdac2). Scale bars, 1 cm (i), 500 μm (j, left) and 100 μm
Rag1−/− condition. RRA, robust rank aggregation. c, The overlap between (j; high-magnification inset, right). k, Control or VDAC2-deficient LoVo
the top 100-ranked gene candidates from CRISPR screens. d, Control or tumour cell viability after co-culture with B7-H3-CAR T cells. n = 3 per group.
VDAC2-deficient tumour cell viability after co-culture with OT-I cells. n = 3 l,m, Control or VDAC2-deficient B16-OVA (l, n = 2 per group) or LoVo (m, n = 3
per group. E:T, effector:target ratio. e, Control or VDAC2-deficient B16-OVA per group) tumour cell death after IFNγ treatment. Data are mean ± s.e.m.,
tumour growth without or with (indicated by arrow) adoptive transfer of representative of three (f, i, j and m), two (d, e, g, k and l) or one (h) independent
activated OT-I cells. f, Control and VDAC2-deficient B16-OVA tumour growth experiments. Statistical analysis was performed using two-tailed unpaired
after the indicated treatments. Arrow indicates tumour rechallenge of sgVdac2 Student’s t-tests (d, i and k), two-way analysis of variance (ANOVA) (e; f and g
and anti-PD-L1 group (left). Right, the survival of mice after primary tumour (tumour size); h and m) and Mantel−Cox tests (f and g (survival)); NS, not
challenge. g, Control and VDAC2-deficient MC38 tumour growth after the significant; *P < 0.05; **P < 0.01; ***P < 0.001.
indicated treatments. Arrow indicates tumour rechallenge of sgVdac2 and
Extended Data Fig. 1o), indicating that VDAC2 loss enhances the thera- there was increased staining of activated caspase-3 and elevated cleav-
peutic potential of ICB-resistant tumours. Finally, we targeted VDAC2 age of caspase-3, caspase-7 and GSDME in VDAC2-deficient tumours,
in a well-established genetic model of constitutively active AKT and especially in response to anti-PD-L1 treatment, which promoted IFNγ
NRAS-driven liver cancer. The liver tumour burden was decreased production in the TME (Extended Data Fig. 2m–o). Collectively, VDAC2
and mouse survival was extended after VDAC2 targeting (Fig. 1i,j and loss drives IFNγ-mediated tumour cell death, mediated by apoptosis
Extended Data Fig. 1p). Such effects were not observed in Rag1−/− mice and secondary necrosis, in vitro and in vivo.
(Extended Data Fig. 1p–r), suggesting that Vdac2 deletion also conferred We next analysed the expression of VDAC family members in tumour
adaptive-immune-dependent protection in this genetic model. Thus, cells and immune cells from syngeneic mouse tumour (Gene Expression
VDAC2 deficiency impedes tumour growth and improves anti-tumour Omnibus (GEO): GSE121861), human melanoma (GEO: GSE215121) and
and immunotherapeutic effects in multiple tumour models in vivo. human lung cancer (GEO: GSE148071), and found higher expression
To expand the physiological and therapeutic relevance, we examined in mouse and human tumour cells compared with in various immune
the dependency of human cancer cells for VDAC2 using the Cancer Dep- cells (Extended Data Fig. 2p,q). However, only tumour cells deficient
Map. VDAC2 perturbation impaired the fitness of a small subgroup of in VDAC2 but not VDAC1 or VDAC3 showed elevated IFNγ-induced cell
human tumour cell lines (Extended Data Fig. 1s), suggesting that VDAC2 death (Extended Data Fig. 2r), indicating the selectivity for VDAC2 defi-
is not a common essential gene for tumour fitness. By contrast, VDAC2 ciency. In human LoVo tumour cells, VDAC2 deficiency also increased
deletion in a patient-derived melanoma cell line modestly sensitized IFNγ-induced cell death (Fig. 1m), suggesting conserved effects in
those cells to tumour-infiltrating lymphocyte (TIL) therapy in vitro22 mouse and human tumour cell lines.
(Extended Data Fig. 1t). Consistent with this notion, VDAC2-deficient PTPN2 targeting improves the immunotherapeutic response by
LoVo tumour cells (a human colon cancer cell line that expresses the enhancing IFNγ signalling7. B16-OVA tumour cells lacking VDAC2 or
B7-H3 antigen) were more sensitive to B7-H3 chimeric antigen recep- PTPN2 showed comparable sensitivity to CD8+ T cell-mediated kill-
tor (CAR)-T cell-mediated killing in vitro (Fig. 1k and Extended Data ing (Extended Data Fig. 3a), whereas VDAC2-deficient cells showed
Fig. 1u). Collectively, targeting VDAC2 in tumour cells represents a greater sensitivity to IFNγ-induced cell death (Extended Data Fig. 3b).
powerful means to overcome immune evasion and bolster cancer Moreover, targeting of VDAC2 or PTPN2 in tumour cells showed a simi-
immunotherapy. lar therapeutic benefit in vivo (Extended Data Fig. 3c). Importantly,
Vdac2 and Ptpn2 co-deletion further enhanced IFNγ-induced death
of VDAC2-deficient tumour cells and impaired their in vivo growth
VDAC2 loss enables tumour killing by IFNγ
compared with loss of either molecule alone (Extended Data Fig. 3d–f),
To determine the mechanisms underlying improved CD8+ suggesting that VDAC2 and PTPN2 represent molecular targets for
T cell-mediated killing of VDAC2-deficient tumour cells, we generated combination therapy.
perforin-, IFNγ- or TNF-deficient OT-I cells and cultured them with con-
trol or VDAC2-deficient B16-OVA tumour cells. Loss of IFNγ but not per-
Loss of VDAC2 inflames the TME
forin or TNF prevented OT-I-cell-mediated killing of VDAC2-deficient
tumours (Extended Data Fig. 2a). Similar impairment occurred after To unbiasedly profile the tumour immune microenvironment, we per-
IFNγ blockade (Extended Data Fig. 2b). Consistent with this notion, formed paired single-cell RNA-sequencing (scRNA-seq) with single-cell
co-deletion of Ifngr1, Ifngr2 or Jak1 in VDAC2-deficient B16-OVA T cell receptor sequencing (scTCR-seq) analysis of intratumoural immune
cells blocked their increased susceptibility to OT-I-cell-mediated cells (CD45+) and tumour cells (CD45–) from control and VDAC2-deficient
killing (Extended Data Fig. 2c). Thus, IFNγ enables increased CD8+ B16-OVA tumour-bearing mice. Unsupervised manifold approximation
T cell-mediated killing of VDAC2-deficient tumour cells in vitro. and projection (UMAP) clustering of intratumoural CD45+ cells identi-
We therefore tested whether VDAC2 deficiency renders tumour cells fied several major immune cell populations (Fig. 2a). Among them,
more sensitive to IFNγ. Whereas control cells were not susceptible the CD8+ T cell proportion was increased in VDAC2-deficient tumours
to IFNγ-induced cell death, VDAC2-deficient B16-OVA cells showed (Fig. 2b). Flow cytometry analysis validated the increased proportion
markedly increased cell death and lactate dehydrogenase (LDH) and number of CD8+ T cells, as well as the increased cellularity of intra-
release after IFNγ (but not TNF) stimulation (Fig. 1l and Extended Data tumoural CD45+ cells and CD4+ T cells (Fig. 2c,d and Extended Data
Fig. 2d,e). To validate the cell-intrinsic effects, we used a dual-colour Fig. 4a). Furthermore, the ratio of CD8+ T cells to regulatory T (T )
reg
co-culture system (Methods) and found that IFNγ but not TNF treat- cells was increased in VDAC2-deficient tumours (Fig. 2e), consistent
ment impaired the survival of VDAC2-deficient B16-OVA cells com- with improved anti-tumour effects. Moreover, CD8+ T cells had mark-
pared with the control cells (Extended Data Fig. 2f), indicating that edly increased clonal expansion in VDAC2-deficient tumours (Fig. 2f).
IFNγ mediates the increased death of VDAC2-deficient tumour cells. Furthermore, CD8+ T cells from VDAC2-deficient tumours showed
Mechanistically, VDAC2 deficiency did not affect canonical IFNγ–STAT1 increased activity scores of gene signatures related to early activation
signalling (Extended Data Fig. 2g). Instead, we found increased cleavage and effector/cytokine production (Fig. 2g) and augmented expression
of caspase-3, caspase-7 and gasdermin E (GSDME) in VDAC2-deficient of Ifng and Prf1 (Extended Data Fig. 4b), indicating enhanced effector
cells after IFNγ stimulation (Extended Data Fig. 2g). Such effects on function. Accordingly, there was an increased number of IFNγ+TNF+
GSDME cleavage were dependent on caspase-3 or caspase-9 (Extended or granzyme B+ (GZMB+) cells among intratumoural CD8+ T cells, and
Data Fig. 2h), suggesting activation of secondary necrosis mediated by expression of IFNγ, TNF and IL-2 was also elevated in intratumoural CD8+
caspase-3 and GSDME23–25 in the absence of VDAC2. T cells (Fig. 2h,i and Extended Data Fig. 4c), suggesting improved quality
To assess the requirement of specific caspases or GSDME in mediating of CD8+ T cell effector function in the TME.
cell death in response to IFNγ treatment, we generated VDAC2-deficient Additionally, stem-like and terminally differentiated CD8+ T cells
tumours cells lacking caspase-3, caspase-7 or GSDME (Extended Data showed reduced and increased frequencies in the VDAC2-deficient
Fig. 2i). Individual targeting of these molecules showed partial effects TME, respectively (Extended Data Fig. 4d–f). Notably, terminally
in mitigating the increased IFNγ-induced death of VDAC2-deficient cells differentiated CD8+ T cells retained high expression of Prf1, Ifng
(Extended Data Fig. 2j,k). Similarly, treatment with the pan-caspase and Gzmb (Extended Data Fig. 4e), suggesting that these cells were
inhibitor emricasan reduced IFNγ-induced cell death of VDAC2-deficient not fully exhausted. Moreover, the effector-like CD8+ T cell popula-
tumour cells, while inhibition of ferroptosis (using ferrostatin-1), tion26–29 was increased in VDAC2-deficient tumours (Extended Data
necroptosis (using necrostatin-1) and GSDMD-mediated pyroptosis Fig. 4f), consistent with their more activated state (Fig. 2g). For further
(with disulfiram) had no such effects (Extended Data Fig. 2l). Moreover, mechanistic insights, we performed assay for transposase-accessible
Nature | www.nature.com | 3
Article
c d
f g h
sgNTC sgVdac2
IFNγ−PE-Cy7 IFNγ−PE-Cy7
k l
chromatin using sequencing (ATAC–seq) analysis of PD-1– and (Extended Data Fig. 4r,s), suggesting that VDAC2 deficiency in tumour
PD-1+CD8+ T cells from control and VDAC2-deficient tumours. Both cells reprograms CD8+ T cell activity, potentially through pathways
PD-1– and PD-1+CD8+ T cells (largely representing non-clonally expanded that overlap with PD-1 blockade. Thus, VDAC2 deficiency reshapes
and clonally expanded cells, respectively; Extended Data Fig. 4d,e) the tumour immune compartment, with a particular effect on intra-
from VDAC2-deficient tumours had increased chromatin accessibil- tumoural CD8+ T cells.
ity of T cell-activation-associated genes including Batf, Ifng and Prkcb To establish translational relevance, we examined the correlation
(Extended Data Fig. 4g, Supplementary Table 3). Accordingly, the between VDAC2 expression and inflammatory signatures or T cell-
frequency of effector-like PD-1+Ki67+CD8+ T cells29 was increased in related genes in human tumour types (Methods), and found that 9 out
VDAC2-deficient tumours (Extended Data Fig. 4h), further establishing of 33 tumour types showed a negative correlation (P ≤ 0.05) between
increased effector function. VDAC2 expression and a tumour inflammation signature (Extended Data
Chronic IFNγ stimulation increases the expression of ligands for Fig. 4t). Moreover, VDAC2 expression was often negatively correlated
T cell inhibitory receptors (TCIRs) such as PD-L1 and TNFRSF1430. We (P ≤ 0.05) with CCL5 (13 out of 33 tumour types) or CD3D expression (18
therefore inoculated wild-type mice with control or VDAC2-deficient out of 33 tumour types) (Extended Data Fig. 4t). Accordingly, melanoma
B16-OVA tumour cells and analysed the expression of TCIR ligands30 and non-small cell lung cancer with high VDAC2 expression had reduced
(Extended Data Fig. 4i). VDAC2 deficiency did not exert major or con- CD8+ and CD4+ T cell fractions (Extended Data Fig. 4u,v), suggesting
sistent effects on TCIR ligands at days 15 and 21 after primary tumour that VDAC2 expression negatively correlates with inflammatory- and
inoculation, except for a modest increase in CD86 expression (Extended T cell-related signatures and T cell infiltration in human tumours.
Data Fig. 4j). We next isolated control or VDAC2-deficient tumour cells Finally, high expression of a curated VDAC2-suppressed gene signa-
on day 21 after primary tumour challenge, and reinoculated these cells ture was associated with improved overall survival in patients with
into naive recipient mice (Extended Data Fig. 4i). On day 15 after trans- melanoma, including those treated with anti-PD-1 antibody (Extended
plantation into new recipients, TCIR ligands were also not upregulated Data Fig. 4w,x and Supplementary Table 4). Thus, an increase in
(Extended Data Fig. 4k). Thus, TCIR ligand expression is not increased VDAC2-suppressed gene signature corresponds to improved disease
after long-term loss of VDAC2. outcomes and response to ICB in patients with melanoma.
Beyond B16-OVA tumours, MC38-OVA tumours lacking VDAC2
had reduced tumour growth and altered immune cell compositions
VDAC2 loss improves anti-tumour immunity
(Extended Data Fig. 4l–q). Notably, the effects of Vdac2 deletion in
tumour cells on intratumoural CD8+ T cells were similar to those To examine the contribution of IFNγ to VDAC2-deficiency-associated
induced by anti-PD-1 treatment in B16-OVA31 and MC3832 tumours effects, we treated VDAC2-deficient B16-OVA tumour-bearing mice
4 | Nature | www.nature.com
124VB−FNT 124VB−FNT
i
50 4.00 21.1 4.69 41.7 40 20
29.7 45.2 19.1 34.5 0
gnoma sllec +BMZG )%( sllec T +8DC NS 30 10
j
egatnecreP
b
sgNTC 30 sgVdac2 20 10 0
P < 0.001 erocs ytivitcA Early activation N/A Single (1) Small (2−5) 1 0.25 M La e r d ge iu m (21 (6 − − 1 2 0 0 0 ) ) 0 Hyper (101−500) −1 noitcarF
*** 2 0
1.00 0.75 0.50
0
)%( sllec +54DC 10 ** 8 6 4
Day 15
sllec +54DC )ruomut g rep 601×( 10 *** 5 0
Day 15
sllec T +8DC )ruomut g rep 601×( 3 2 1 0
Day 15
50 40 20
0
gnoma +FNT+γNFI )%( sllec T +8DC **
Day 15
sllec T +8DC+FNT+γNFI )ruomut g rep 501×(
a
−10 −5 0 5 10 UMAP 1
** 15 10 5
0
Day 15 Day 15
2 PAMU
B cell CD4+ T cell
10 CD8+ T cell cDC1 5 cDC2 40 ** Macrophage 0 mregDC −5 Neutrophil 30 NK cell −10 pDC −15 T T u reg m c o e u ll r cell 2 0 0
B C D ce 4+ ll C T D c 8 e + l l T cell cDC M 1 c a D cr C o 2 pha m ge re N g e D u C troph N il K cell pDC Tre g cell
gnoma sllec T +8DC )%( sllec +54DC
Day 15
8 sllec T +8DC+BMZG )ruomut g rep 501×( *** 6 4 2
0
Day 15
erocs ytivitcA
8
Effector/cytokine production 3 P < 0.001 2 1 0 −1
−2
oitar T/T +8DC ger
e
** 6 4 2 0
Day 15
25 sllec T +8DC+BMZG )ruomut g rep
501×(
20 15 10 5
0
sllec T +8DC+FNT+γNFI )ruomut g rep
501×(
15 10 5
0
Day 15 Day 15
sllec +54DC )ruomut g rep
601×(
8 6 4 2
0
sllec T +8DC )ruomut g rep
601×(
NS
*** ** 4 3 NS 2 1
0
Day 15 Day 15
*** NS * 15 sgNTC + isotype (n = 6) sgVdac2 + isotype (n = 5) 10 sgNTC + anti-IFNγ (n = 6) 5 sgVdac2 + anti-IFNγ (n = 6)
0
7
)3mm
201×( ezis ruomuT
B16-OVA tumour B16-OVA tumour
CD45+ and tumour cells CD45+ cells sgNTC sgVdac2 sgNTC sgVdac2 sgNTC
sgVdac2
CD8+ T cells CD8+ T cells sgNTC sgVdac2 sgNTC sgVdac2
Clonotype size 30 10
sgN
s
T
g
C Vdac2 sgNT
s
C gVdac2 sgNT
s
C gVdac2
NS NS NS
20 B16-OVA *** *** *** ** *** ** sgNTC + isotype sgNTC + isotype sgVdac2 + isotype sgVdac2 + isotype NS sgNTC + anti-IFNγ sgNTC + anti-IFNγ sgVdac2 + anti-IFNγ NS NS sgVdac2 + anti-IFNγ
11 15
Days after inoculation
Fig. 2 | VDAC2-deficiency-induced TME inflammatory reprogramming (n = 2,295 cells) B16-OVA tumours. The box plots show the median (centre line)
requires IFNγ. a, UMAP plot of the indicated cell clusters from scRNA-seq and the interquartile range (25% to 75%; box limits). h,i, IFNγ+TNF+ (h) and
profiling of control and VDAC2-deficient tumours. n = 2 biological replicates GZMB+ (i) CD8+ T cells from B16-OVA tumours. n = 7 (sgNTC) and n = 6 (sgVdac2).
per group. cDC, conventional dendritic cell; mregDC, mature dendritic cell j, Control and VDAC2-deficient tumour growth after the indicated treatments.
enriched in immunoregulatory molecules; pDC, plasmacytoid dendritic cell. k,l, CD45+ cells (k, left) and CD8+ T cells (k, right) or IFNγ+TNF+ (l, left) and GZMB+
b, The frequencies of the indicated intratumoural immune cell populations (l, right) CD8+ T cells from the indicated B16-OVA tumours. n = 5 (sgNTC + isotype
among CD45+ cells in each genotype. c–e, CD45+ cells (c), CD8+ T cells (d) and the and sgVdac2 + isotype) and n = 7 (sgNTC + anti-IFNγ and sgVdac2 + anti-IFNγ). Data
ratio of CD8+ T cells to T cells (e) in control (n = 8) and VDAC2-deficient (n = 7) are mean ± s.e.m., representative of three (c–e, h and i) or two (j–l) independent
reg
B16-OVA tumours. f, The frequencies of CD8+ T cells grouped by clonotype experiments. Statistical analysis was performed using two-tailed unpaired
sizes, as assessed by scTCR-seq. N/A, TCR type not detected. g, Activity scores Student’s t-tests (c–e, h and i), one-way ANOVA (k and l), two-way ANOVA (j)
of early activation and effector/cytokine production-related gene signatures in and two-tailed Wilcoxon rank-sum tests (g).
intratumoural CD8+ T cells from control (n = 710 cells) and VDAC2-deficient
with anti-IFNγ, which enhanced tumour growth to levels comparable to We next co-targeted cGAS or STING in VDAC2-deficient tumour cells
those observed in anti-IFNγ-treated control tumours (Fig. 2j). Blocking to establish functional effects and found that their targeting largely
IFNγ also reduced intratumoural CD45+ immune cells and the abun- blocked the capacity of VDAC2-deficient tumour cells to increase
dance and effector function of CD8+ T cells in VDAC2-deficient tumours TBK1 or IRF3 phosphorylation or IFNβ expression after IFNγ stimu-
(Fig. 2k,l). We next treated mice transiently with anti-IFNγ at early or lation (Fig. 3j–l). Co-deletion of Irf3 (albeit not Mavs, which induces
late time periods after tumour inoculation (Methods) and found that STING-independent type I IFN response34) also rectified such aberrant
both treatment regimens eliminated the beneficial effects of Vdac2 IFNβ expression (Extended Data Fig. 6g,h). In transcriptome profil-
deletion (Extended Data Fig. 5a,b). Thus, IFNγ reshapes the tumour ing, STING co-deletion largely reversed the increased expression of
immune microenvironment of VDAC2-deficient tumours. IFN-response genes induced by VDAC2 deficiency (Fig. 3m). By contrast,
To determine the cellular sources of IFNγ, we compared Ifng expres- co-deletion of Cgas, Sting1 or Irf3 did not mitigate the excessive cell
sion in different immune cell populations and found high expression of death of IFNγ-stimulated VDAC2-deficient tumour cells (Extended Data
Ifng in CD8+ T cells and, to a lesser extent, natural killer (NK) cells, in both Fig. 6i), suggesting that the effects of STING signalling were specific in
control and VDAC2-deficient B16-OVA tumours (Extended Data Fig. 5c). mediating the increased type I IFN response, albeit not the cell death
Given the pronounced accumulation of CD8+ T cells in VDAC2-deficient phenotypes, induced by Vdac2 deletion. Likewise, IFNγ-induced cell
tumours, we then depleted CD8+ T cells. We found that VDAC2-deficient death of VDAC2-deficient cells was unaltered after IFNαR1 blockade
tumour growth was increased (Extended Data Fig. 5d,e), suggesting the (Extended Data Fig. 6j). Upon in vivo tumour challenge, Sting1 or Irf3
importance of CD8+ T cells in mediating VDAC2 deficiency-associated co-deletion also partly blocked the therapeutic benefits of Vdac2 dele-
effects. To test whether CD8+ T cell-derived IFNγ contributes to these tion on tumour growth and mouse survival (Fig. 3n and Extended Data
effects, we generated Cd8creIfngfl/fl chimeras to deplete Ifng specifi- Fig. 6k). Together, these results reveal an interplay between IFNγ sig-
cally in CD8+ T cells (Methods) (Extended Data Fig. 5f). Compared nalling, VDAC2 and STING activation that dictates type I IFN response
with control tumours, VDAC2-deficient tumours had the expected and tumour growth.
reduction in tumour growth and enhanced mouse survival in wild-type Ccl5 expression was among the top-most upregulated genes in
chimeras, whereas VDAC2-deficient tumours and control tumours had VDAC2-deficient tumour cells treated with IFNγ or OT-I cells (Fig. 3b
comparable growth in Cd8creIfngfl/fl chimeras (Extended Data Fig. 5g). and Extended Data Fig. 6d). This increased Ccl5 expression was recti-
Collectively, these results indicate that intratumoural IFNγ derived fied after co-deletion of Cgas, Sting1 or Irf3 (albeit not Mavs) and was
from CD8+ T cells has a major role in mediating the impaired growth validated to occur after co-culture with OT-I cells in vitro (Extended
of VDAC2-deficient tumours. Data Fig. 6l–o). Furthermore, VDAC2-deficient tumour cells expressed
higher levels of Ccl5 in vivo, whereas intratumoural CD8+ T cells from
such tumours expressed higher levels of Ccr5 (Extended Data Fig. 6p,q).
VDAC2 impedes IFNγ-induced STING signalling
These results prompted us to test whether CCL5 contributes to the
To determine the mechanistic basis, we first analysed the transcrip- reshaping of the tumour immune landscape after Vdac2 deletion. Ccl5
tome profiles of control and VDAC2-deficient tumour cells in the co-deletion impeded the increased accumulation of CD8+ T cells, includ-
scRNA-seq dataset. Gene set enrichment analysis (GSEA) showed that ing those expressing IFNγ and TNF or GZMB, in the VDAC2-deficient
VDAC2-deficient tumour cells had increased IFNα- and IFNγ-related TME (Extended Data Fig. 6r). Thus, CCL5 contributes to the robust
gene signatures (Fig. 3a). Furthermore, GSEA of tumour cells treated accumulation of effector CD8+ T cells in VDAC2-deficient tumours.
with IFNγ or OT-I cells revealed increased IFNγ and IFNα response Cytosolic mitochondrial DNA (mtDNA) release triggers STING activa-
signatures in VDAC2-deficient versus control tumour cells, with tion35. As VDAC2 is a mitochondrial protein (Extended Data Fig. 6s), we
such signatures representing the only shared Hallmark pathways hypothesized that cytosolic mtDNA release may occur in IFNγ-treated
upregulated in the absence of VDAC2 under conditions of immune VDAC2-deficient tumour cells. Indeed, immunostaining revealed a
pressure (Extended Data Fig. 6a–c and Supplementary Table 5). decreased abundance of mitochondrially localized double-stranded
Accordingly, multiple genes in the IFN-responsive pathways were DNA in VDAC2-deficient tumour cells after IFNγ treatment (Fig. 3o
upregulated in VDAC2-deficient tumours treated with IFNγ or OT-I and Extended Data Fig. 6t). Furthermore, VDAC2-deficient tumour
cells (Fig. 3b,c and Extended Data Fig. 6d). Furthermore, Ifnb1 and Ccl5, cells showed increased abundance of cytosolic mtDNA (Fig. 3p and
which are induced by cGAS–STING33, were increased in IFNγ-treated Extended Data Fig. 6u). We next generated control and VDAC2-deficient
VDAC2-deficient tumour cells, with elevated IFNβ protein lev- tumour cells lacking mtDNA (ρ0 cells; Methods) and found that mtDNA
els also detected after IFNγ treatment in vitro or in tumour lysates depletion in IFNγ-stimulated VDAC2-deficient tumour cells rectified
in vivo (Fig. 3d–f and Extended Data Fig. 6e). Thus, IFNγ stimulation the increased levels of phosphorylated TBK1, IFNβ and Ccl5 (Fig. 3q and
aberrantly upregulates the type I IFN response in VDAC2-deficient Extended Data Fig. 6v–y). Likewise, VDAC2-deficient human LoVo cells
tumour cells. had increased inflammatory gene expression and STING activation
Furthermore, Ingenuity pathway analysis (IPA) revealed upregulated (Fig. 3r,s, Extended Data Fig. 6z and Supplementary Table 7), thereby
activities of STING, IRF3 and IRF7 in VDAC2-deficient tumour cells after establishing that VDAC2 restrains IFNγ-induced STING activation
IFNγ or OT-I cell treatment (Fig. 3g and Supplementary Table 6). ATAC– in human tumour cells. Together, aberrant cytosolic mtDNA drives
seq profiling of VDAC2-deficient versus control tumour cells, followed cGAS–STING signalling and type I IFN response in IFNγ-stimulated
by motif enrichment analysis of differentially accessible chromatin, VDAC2-deficient cells.
revealed that IRF5 and IRF7 (albeit not IRF1) activities were increased
in VDAC2-deficient tumour cells (Fig. 3h), indicating enhanced type I
VDAC2–BAK axis tunes tumour remodelling
IFN-related responses in VDAC2-deficient tumour cells in vitro and
in vivo. On the basis of these findings, we examined STING expression To unbiasedly identify functional genetic interactions for enhanced
and activation, and found that STING expression was upregulated in susceptibility to IFNγ-induced cell death, we performed a genetic
both control and VDAC2-deficient tumour cells after IFNγ treatment interaction screen by co-transducing VDAC2-deficient B16-OVA-Cas9
(Fig. 3i and Extended Data Fig. 6f). By contrast, compared with control tumour cells with a genome-scale sgRNA library and, after IFNγ treat-
tumours, the levels of phosphorylated STING (Ser365), TBK1 (Ser172) ment, assessed sgRNA enrichment or depletion among the viable
and IRF3 (Ser396) were increased in VDAC2-deficient tumour cells VDAC2-deficient tumour cells to nominate genetic interactions that
at ≥12 h of IFNγ stimulation (Fig. 3i and Extended Data Fig. 6f). Thus, either alleviate or synergize with VDAC2 deficiency-driven effects on
VDAC2 restrains IFNγ-induced STING activation. tumour cell death (Fig. 4a). Targeting Ptpn2 potentiated, and depleting
Nature | www.nature.com | 5
Article
e
***
***
IFNγ signalling-associated genes (Ifngr1, Ifngr2, Jak1, Jak2 and Stat1) related protein BAX orchestrate mitochondria-dependent cell death by
alleviated, VDAC2 deficiency-mediated cell death after IFNγ treatment promoting mitochondrial outer membrane permeabilization (MOMP),
(Extended Data Fig. 7a and Supplementary Table 8a,b). Next, we over- cytochrome c release and initiation of APAF-1- and caspase-9-dependent
laid these genetic interaction screen hits with the MitoCarta 3.0 data- cell death25. We found that co-deletion of Bak1, but not Bax, blocked
base, which contains all annotated mitochondria-associated genes36. IFNγ-induced cell death and LDH release of VDAC2-deficient tumour
We found that targeting Casp9 and Bak1 (encoding BAK) had the most cells (Extended Data Fig. 7b,c). Furthermore, in the absence of IFNγ
substantial effects on alleviating VDAC2-deficiency-mediated tumour treatment, overexpression of Bak1, but not Bax, promoted cell death
cell death (Fig. 4b and Supplementary Table 8c). BAK and/or the closely of VDAC2-deficient tumour cells (Extended Data Fig. 7d), further
6 | Nature | www.nature.com
)1–lm gp( βNFI 80 *** ** 60 40 20
0
βNFI )ruomut gm 001
rep
gp(
b d f
20 15 5
0
IFNγ (h): 3 6 9 12 18
sgNTC + − + − + − + − + − + −
sgVdac2 − + − + − + − + − + − + kDa
cGAS 50
1.05.5 37 37
1.02.8
75
75
1.06.3
50
37
VDAC2 25
Pla2g4a β-Actin Procr 37
n Row 20 z score 2 15 1 10 0 5 −1 −2 0 *** sgNTC + sgNTC (n = 8) sgVdac2 + sgNTC (n = 9) sgNTC + sgSting1 (n = 7) sgVdac2 + sgSting1 (n = 9) *** ***
c
200 *** 150 *** 100 *** 50 ***
0
ANRm evitaleR
)CTNgs
detaert-non
susrev(
g
OT-I Poly rI:rC-RNA IFNγ treatment Irf7 treatment 8 Lipopolysaccharide 4
Irf3
Sting1
Ifng
ANDtm
cilosotyC
)egnahc
dlof evitaler(
0
i
p q sgNTC sgVdac2 *** 40 50 sgNTC
30 40 sgVdac2 20 20 ** s s g g N Vd T a C c _ 2 ρ _ 0 ρ0 10
0 0 D-loop1 D-loop2 D-loop3 mtCytb mtNd4 mt16s Untreated
ANRm 1bnfI evitaleR 50 *** 40 *** 20 NS NS
12 18 24
o sgNTC sgVdac2
*** sgNTC + sgNTC (n = 8) sgVdac2 + sgNTC (n = 9) sgNTC + sgIrf3 (n = 8) sgVdac2 + sgIrf3 (n = 9) *** 5
Days after inoculation
)3mm 201×( ezis ruomuT 20 15 10 0
7 11 15 19
Days after inoculation
)3mm 201×( ezis ruomuT
7 11 15 19
*
j
IFNγ 24 h
sgNTC+ + + − + − + + + − + −
sgVdac2− + − + − + − + − + − +
sgCgas− − + + − − − − + + − −
sgSting1− − − − + + − − − − + + 1.02.2 0.50.60.50.5 kDa p-TBK1S172 75
TBK1 75
1.06.00.91.20.71.5
p-IRF3S396 50
IRF3 37
cGAS 50
37
STING
25
37
30 10
ANRm
1bnfI evitaleR
)CTNgs
detaert-non
susrev(
ANRm
1BNFI evitaleR
)CTNgs
detaert-non
susrev(
10
*** *** 20 NS 0 ANRm 1bnfI evitaleR )CTNgs detaert-non susrev(
k
*** 60 60 40 40 NS 20 0 )1–lm gp( βNFI
l m
sgNTC + sgNTC sgVdac2 + sgNTC
sgNTC + sgSting1 sgVdac2 + sgSting1
sgNTC sgVdac2
*** )201×( IFM
ANDtm
a
Hallmark IFNγ response
16 12
8 0
erocs
tnemhcirnE
Hallmark IFNα response
0.3 0.2 0.1 NES = 1.91 0 FDR < 0.0001
sgVdac2 sgNTC
erocs
tnemhcirnE 0.4 0.2 NES = 2.76 FDR < 0.0001 0
sgVdac2 sgNTC
logFC(sgVdac2 versus sgNTC)
2
)eulav P( gol− 01
B16-OVA + IFNγ 16 h
15 10 5 2
0
−1 0 1 2 Ccl5 lfit1 Isg15 Mx1 Oasl1 0
Il6
Irf7 Casp4 Lysmd2 Ccrl2 Upp1 Ccl5 Nfkbia Irf9 Mx2 Mx1 Trim26 Fas
)RDF( gol− 01
sgNTC sgNTC sgNTC sgNTC
sgVdac2 sgVdac2 sgVdac2 sgVdac2 30 10
h
200
100
Irf1 Irf5
0 Stat1 Irf7
−10 −5 0 5 10
Odds ratio (sgVdac2 versus sgNTC)
*** *** *** NSNS
r sgNTC sgVDAC2 600 ***
400 200 2
0
ANRm
5LCC evitaleR
)CTNgs
detaert-non
susrev(
B16-OVA from scRNA-seq
Vdac2 Mx2 Oasl1 Ifit2 Ccl5 Ifi207 Mx1 Ifit1 Ifi208 Ifi213 Isg20
Isg15
IFNγ 24 h Day 19
Time after IFNγ
treatment (h)
IPA ( s o g f V tw da o c m 2 i v c e ro rs a u r s ra s y g d N a T ta C s ) ets B16-OVA (in vivo) day 15 0 Untreated
p-STINGS365
STING
p-TBK1S172
TBK1
p-IRF3S396
IRF3
sgNTC + sgNTC sgNTC + sgNTC B16-OVA + IFNγ 24 h sgVdac2 + sgNTC sgVdac2 + sgNTC VDAC2
sgNTC + sgCgas sgNTC + sgCgas β-Actin sgVdac2 + sgCgas sgVdac2 + sgCgas
sgNTC + sgSting1 sgNTC + sgSting1 sgVdac2 + sgSting1 sgVdac2 + sgSting1 s Untreated IFNγ 48 h sgNTC + − + − sgVDAC2 − + − + kDa p-STAT1Y701 75 1.02.5 IFNγ 24 h IFNγ 24 h p-STINGS366 37
STING 37
1.02.4
p-TBK1S172 75
+IFNγ 24 h TBK1 75 IFNγ 24 h 1.02.2 600 *** p-IRF3S396 50
400 IRF3 50 200 NS 2 NS VDAC2 25
dsDNA TOMM20 IFNγ 24 h IFNγ 48 h Un 0 treated IFNγ 48 h β-Actin 37
Fig. 3 | VDAC2 loss enables IFNγ-induced mtDNA release and STING group) and IFNβ in culture supernatants of indicated cells (l; n = 3 per group).
activation. a, Hallmark IFNα and IFNγ response signatures. FDR, false- m, The relative expression of IFN-responsive genes repressed by VDAC2 in the
discovery rate; NES, normalized enrichment score. b, Gene expression profiles indicated IFNγ-treated B16-OVA tumour cells. n = 3 per group. n, The growth of
in IFNγ-treated B16-OVA tumour cells, with selective upregulated (red) and B16-OVA tumours. The same sgNTC and sgVdac2 groups are shown on the left
downregulated (blue) genes labelled. c,d, The relative levels of IFN-responsive and right. o, dsDNA and TOMM20 co-localization in IFNγ-treated B16-OVA
genes (c) or Ifnb1 (d) in IFNγ-treated B16-OVA tumour cells. n = 3 per group. tumour cells. n = 4,525 (sgNTC) and 5,948 (sgVdac2). Scale bar, 20 μm. MFI, mean
e,f, IFNβ levels in culture supernatants from IFNγ-treated B16-OVA tumour cells fluorescence intensity. p, Relative cytosolic mtDNA levels (versus non-treated
(e; n = 3 per group) or from tumour lysates after inoculation into wild-type mice control cells) in IFNγ-treated B16-OVA tumour cells. n = 2 per group. q, Relative
(f; n = 6 per group). g, Overlap of activated IPA-predicted upstream regulators Ifnb1 levels in IFNγ-treated B16-OVA tumour cells that lack (ρ0 cells) or contain
from transcriptome profiling of OT-I- or IFNγ-treated B16-OVA tumour cells. mtDNA (n = 3 per group). r, The relative IFNB1 and CCL5 levels in IFNγ-treated
The numbers indicate uniquely activated regulators. h, Motif enrichment LoVo tumour cells. n = 3 per group. s, Immunoblot analysis of LoVo tumour cells
analysis of differentially accessible chromatin profiled by ATAC–seq (n = 4 per before and after IFNγ treatment, with densiometric quantification of p-STING,
group), with selective upregulated (red) and downregulated (blue) motifs p-TBK1 or p-IRF3 shown. Data are mean ± s.e.m., representative of three (c, d, i,
labelled and black-labelled genes being unaltered. i,j, Immunoblot analysis of k and l), two (e, j and o–s) or one (f and n) independent experiments. Statistical
B16-OVA tumour cells after IFNγ treatment, with densiometric quantification analysis was performed using two-tailed unpaired Student’s t-tests (c–f and o),
of phosphorylated STING (p-STING), p-TBK1 or p-IRF3 shown (i), and p-TBK1 or one-way ANOVA (k, l and q), two-way ANOVA (n and r) and two-tailed Fisher’s
p-IRF3 shown (j). k,l, The relative levels of Ifnb1 in indicated cells (k; n = 3 per exact test (h).
d
sgNTC + sgNTC
sgVdac2 + sgNTC
sgNTC + sgBak1 sgVdac2 + sgBak1
D-loop3
f
Row z score
2
1
0 −1
−2
supporting an interplay between VDAC2 and BAK in orchestrating protein abundance (Fig. 4c). Accordingly, downstream events of BAK
tumour cell death. activation, including MOMP39 and cytosolic release of cytochrome c
Next, we examined STING activation in cells lacking VDAC2 and BAK and SMAC, were increased in VDAC2-deficient tumour cells after IFNγ
and found that Bak1 co-deletion blocked the increased phosphoryla- treatment (Extended Data Fig. 7j,k). Thus, VDAC2 interacts with and
tion of STING, TBK1 and IRF3 in IFNγ-stimulated VDAC2-deficient cells suppresses BAK in tumour cells, and IFNγ-stimulated BAK activity is
(Fig. 4c). Furthermore, co-deletion of Bak1 (but not Bax) rectified the unleashed after Vdac2 deletion.
increased mtDNA release and expression of IFNβ and IFN-responsive To establish the functional importance of the VDAC2–BAK interac-
genes (Fig. 4d,e and Extended Data Fig. 7e,f). Global transcriptome tion, we generated a wild-type VDAC2 construct or three types of VDAC2
alterations induced by VDAC2 deficiency were also substantially miti- mutants impairing the VDAC2–BAK interaction40,41. The interactions
gated by BAK co-deletion (Fig. 4f and Extended Data Fig. 7g). Collec- between these mutant proteins with BAK were substantially reduced
tively, Vdac2 deletion acts through BAK to mediate mtDNA release, compared with wild-type VDAC2 (Extended Data Fig. 7l). Moreover,
STING activation and inflammatory reprogramming. only wild-type, but not mutant, VDAC2 largely rectified the phenotypes
Mechanistically, VDAC2 interacted with BAK but not BAX in B16-OVA of VDAC2-deficient cells, including enhanced IFNγ-induced cell death
tumour cells, consistent with previous findings37 (Extended Data and type I IFN responses (Fig. 4g,h and Extended Data Fig. 7m), thereby
Fig. 7h). To determine whether VDAC2 affects BAK or BAX activity, establishing the functional importance of the VDAC2–BAK interaction
we measured BAK or BAX oligomer formation38 in mitochondrial to VDAC2-mediated effects in response to IFNγ.
fractions of IFNγ-treated control and VDAC2-deficient cells, which We next compared the functional effects of VDAC2 with MCL-1
revealed increased BAK but not BAX dimer and trimer formation in and BCL-2, which are known to inhibit BAK25,42. At 24 h of IFNγ treat-
VDAC2-deficient cells, especially after IFNγ treatment (Extended Data ment, in contrast to VDAC2-deficient cells, MCL-1- or BCL-2-deficient
Fig. 7i). Thus, there was aberrant activation of BAK in IFNγ-treated cells showed slightly increased or negligible cell death, respectively
VDAC2-deficient cells, which occurred despite a reduction in total BAK (Extended Data Fig. 7n,o), and no major changes in type I IFN responses
Nature | www.nature.com | 7
)erocs
ARR
KCeGAM( gol− 01
b c
sgCasp9 6
sgBak1 4 2 0 −2 0 1 logFC (IFNγ treatment ve2rsus non-treated)
NS )%( lavivruS
100
sgNTC + sgNTC sgVdac2 + sgNTC 50 sgNTC + sgBak1
sgVdac2 + sgBak1
0 0 10 20 30
Days after inoculation
*** ***
IFNγ (h): 0 12 24
sgNTC + + + − + + + − + + + −
sgVdac2 − + − + − + − + − + − + sgBak1− − + + − − + + − − + + kDa
p-STINGS365 37 STING 37 −1 p-TBK1S172 75 TBK1 75
p-IRF3S396 50
IRF3 37 1.00.3 1.80.6 3.11.1 25 BAK
VDAC2 25
β-Actin 37
h g
i
sgNTC + sgNTC
60 sgVdac2 + sgNTC sgNTC + sgNTC sgVdac2 + sgNTC sgNTC + sgBak1
sgNTC + sgBak1 20 sgVdac2 + sgBak1
sgVdac2 + sgBak1 0
sruomut
fo
rebmuN
e
sgNTC + sgNTC sgVdac2 + sgNTC sgNTC + sgBak1 sgVdac2 + sgBak1
j
NS
** 40 **
7 15 19 Day 21
Days after inoculation
)3mm
201×( ezis
ruomuT
20
15 sgNTC + sgNTC (n = 7) sgVdac2 + sgNTC (n = 8) 10 sgNTC + sgBak1 (n = 5) NS
5 sgVdac2 + sgBak1 (n = 6)
0 11
*** ***
ANRm 1bnfI
evitaleR
)VE
+ CTNgs detaert-non
susrev(
100 80 60 40
20
0
IFNγ 24 h
ANRm 5lcC
evitaleR
)VE
+ CTNgs detaert-non
susrev(
*** *** *** *** *** *** *** 80 *** *** *** s s g g N Vd T a C c 2 + + E V EV 60 sgVdac2 + HA-VDAC2 WT 40 sgVdac2 + HA-VDAC2(A172R)
20 sgVdac2 + HA-VDAC2(T168N/D170E)
0 0 sgVdac2 + HA-VDAC2(T168N/D170E/A172R)
IFNγ 24 h IFNγ 24 h
)%( +DAA-7+V-nixennA
sgNTC + sgNTC sgVdac2 + sgNTC sgNTC + sgBak1
sgVdac2 + sgBak1 sgNTC + sgBax
0 sgVdac2 + sgBax
*** *** 4 5 0 0 *** *** *** s s g g N Vd T a C c 2 + + E V E V 30 sgVdac2 + HA-VDAC2 WT 20 sgVdac2 + HA-VDAC2(A172R)
10 sgVdac2 + HA-VDAC2(T168N/D170E)
sgVdac2 + HA-VDAC2(T168N/D170E/A172R)
)1–lm gp(
βNFI
NS *** *** 10 *** 60 *** 8 6 40 4 NS
20 2 0
IFNγ 24 h
ANDtm cilosotyC )egnahc dlof
evitaler(
NS *** *** NS 0
NS
mtCytb
Untreated
ANDtm cilosotyC )egnahc dlof evitaler(
a
Lentiviral sgRNA Brie library B16-OVA-sgVdac2
(78,637 sgRNAs targeting MitoCarta3.0 (1,032 genes)
19,674 genes)
Input 1.03.4 1.11.0
14 days DNA isolation and deep Untreated sequencing 20 - B s 1 g 6 V - d O a V c A 2 IFNγ treatment 1.02.11.00.9 15 (10 ng ml−1, 24 h) 10 5 1.06.40.90.9 Untreated IFNγ 24 h
B16-OVA + IFNγ 24 h
IFNγ 24 h
Fig. 4 | BAK mediates VDAC2-deficiency-driven effects in response to tumour cells after IFNγ treatment. n = 3 per group. g, Cell death of the indicated
IFNγ. a, Schematic of the secondary genome-scale CRISPR screen. Created in B16-OVA tumour cells treated with IFNγ. n = 3 per group. EV, empty vector.
BioRender. Sun, R. (2025) https://BioRender.com/g06b183. b, Enriched (red) h, Relative Ifnb1 and Ccl5 levels (versus non-treated control cells) in the indicated
and depleted (blue) sgRNAs targeting mitochondria-associated genes in B16-OVA tumour cells treated with IFNγ. n = 3 per group. i, Control, VDAC2-
IFNγ-treated versus non-treated VDAC2-deficient B16-OVA tumour cells. deficient, BAK-deficient, or VDAC2 and BAK co-deficient B16-OVA tumour
c, Immunoblot analysis of the indicated sgRNA-transduced B16-OVA tumour growth (left) and survival of tumour-bearing mice (right). j, Lung tumour burden
cells after IFNγ treatment for indicated times; densiometric quantification of in mice that received intravenous injection of the indicated B16-OVA tumour
p-STING, p-TBK1, p-IRF3 or total BAK is shown. d, The relative cytosolic mtDNA cells. n = 5 per group. Scale bar, 1 cm. Data are mean ± s.e.m., representative of
levels (versus non-treated control cells) in the indicated B16-OVA tumour cells three (c and i), two (d, e, g and h) or one (j) independent experiments. Statistical
treated with or without IFNγ. n = 3 per group. e, IFNβ levels in the culture analysis was performed using one-way ANOVA (d, e, g, h and j), two-way ANOVA
supernatants from the indicated B16-OVA tumour cells after IFNγ treatment. (i (tumour size)) and Mantel−Cox test (i (survival)).
n = 4 per group. f, The relative gene expression in the indicated B16-OVA
Article
(Extended Data Fig. 7n,p). Nonetheless, after extended (48 h) IFNγ signature in IFNγ-stimulated VDAC2 and APAF-1 co-deficient tumour
treatment, MCL-1-deficient cells and, to a lesser extent, BCL-2-deficient cells compared with that in VDAC2-deficient tumour cells (Extended
cells, showed increased cell death (albeit less pronounced than Data Fig. 9n and Supplementary Table 9). Moreover, co-deletion of
VDAC2-deficient cells) (Extended Data Fig. 7o) and Ifnb1 and/or Ccl5 Apaf1 or Casp9, or treatment with emricasan, further reduced the
expression (Extended Data Fig. 7p). Furthermore, only VDAC2-deficient growth of VDAC2-deficient tumours in vivo, corresponding to increased
cells displayed increased BAK activation at 24 h after IFNγ treatment, mouse survival (Extended Data Fig. 9o,p), suggesting that inhibition of
while both VDAC2- and MCL-1-deficient cells showed enhanced BAK apoptosis modestly boosts the therapeutic effects of VDAC2 deficiency.
activation at 48 h (Extended Data Fig. 7q). Compared with the pro- Together, these data reveal that VDAC2 deficiency overrides the inhibi-
nounced effects of Vdac2 deletion, loss of MCL-1 or BCL-2 modestly tory effects of apoptotic caspases on cGAS–STING activation to enable
sensitized tumour cells to OT-I-cell-mediated killing (Extended Data BAK-dependent caspase and STING activation after IFNγ stimulation.
Fig. 7r). Thus, VDAC2-deficient B16-OVA cells are more sensitive than To establish the physiological relevance of VDAC2–BAK axis in vivo,
MCL-1- and BCL-2-deficient cells to these IFNγ-induced effects of cell we challenged wild-type mice with control B16-OVA tumours or those
death and inflammation. lacking VDAC2 and/or BAK. Bak1 co-deletion reversed the reduced
To mechanistically understand how VDAC2 deficiency unleashes growth of VDAC2-deficient tumours in both subcutaneous (s.c.) and
the sensitivity to IFNγ-induced mitochondrial apoptosis, we exam- lung metastasis models (Fig. 4i,j). Moreover, Bak1 co-deletion largely
ined the gene expression of BCL-2-family members in control and blocked the increased accumulation and effector-like features of CD8+
VDAC2-deficient B16-OVA tumour cells treated with IFNγ. IFNγ stimula- T cells (Extended Data Fig. 9q,r). Bak1 co-deletion also blocked the
tion increased expression of Bcl2l11 (encoding BIM) and Bid, along with enhanced therapeutic benefit of combining anti-PD-L1 treatment with
their downstream target Bak1, with such observations also evident at VDAC2 deficiency in tumour cells (Extended Data Fig. 9s,t). Thus, the
the protein levels (Extended Data Fig. 8a,b). By contrast, except for BIM, VDAC2–BAK axis tunes anti-tumour and ICB responses in vivo.
these proteins were not upregulated by anti-cancer apoptosis inducers To further explore the potential widespread effects of targeting
such as cisplatin and etoposide, which instead promoted expression of VDAC2, we examined whether VDAC2 limits IFNγ-induced cell death
PUMA and p53 (Extended Data Fig. 8c). Mechanistically, BID and BAK of non-tumorigenic cells. IFNγ stimulation did not cause marked cell
expression was decreased in STAT1- or IRF1-deficient cells, whereas BIM death of VDAC2-deficient mouse embryonic fibroblasts (MEFs), in
and STING expression was reduced in STAT1-deficient cells (Extended contrast to treatment with etoposide or TNF plus cycloheximide37
Data Fig. 8d,e). Furthermore, the protein levels of BIM and BAK (but not (Extended Data Fig. 10a). IFNγ also did not induce substantial cell
BID) (Extended Data Fig. 8f), as well as STING (Fig. 3s), were increased death of control or VDAC2-deficient OT-I cells in vitro (Extended
in IFNγ-stimulated human LoVo tumour cells, suggesting conserved Data Fig. 10b) and, accordingly, VDAC2-deficient OT-I cells retained
effects between human and mouse tumour cells. potent anti-tumour function in vivo (Extended Data Fig. 10c). Similarly,
To determine the functional contributions of STAT1 and IRF1 sig- VDAC2 deficiency did not alter cell death of T helper type 1 (T 1) and
H
nalling, we co-deleted Stat1 or Irf1 in VDAC2-deficient tumour cells. in vitro-derived T (iT ) cells (Extended Data Fig. 10d). We also found
reg reg
Co-deletion of Stat1 or Irf1 completely or partially rectified the that only BAK (but not BIM or BID) was upregulated by IFNγ in control
IFNγ-induced cell death and type I IFN phenotypes of VDAC2-deficient and VDAC2-deficient MEFs, whereas BID expression was modestly
cells, respectively (Extended Data Fig. 8g,h). Thus, STAT1 and, to a lesser downregulated in IFNγ-treated OT-I cells (Extended Data Fig. 10e,f).
extent, IRF1 contribute to the increased sensitivity of VDAC2-deficient These results suggest that IFNγ stimulation coordinately upregulates
cells to IFNγ-induced cell death and inflammatory remodelling. We BIM, BID and BAK selectively in tumour cells, associated with their
next co-deleted Bcl2l11 and Bid in VDAC2-deficient tumour cells, which increased sensitivity to VDAC2-deficiency-driven cell death.
largely rescued IFNγ-induced cell death or CD8+ T cell-mediated killing Finally, tumour cells are in a more primed state compared with
(Extended Data Fig. 8i,j). Accordingly, compared with VDAC2-deficient normal cells for apoptosis, with such effects associated with their
tumour cells, VDAC2-deficient tumour cells lacking BIM and BID had more abundant expression of certain apoptotic molecules42,47. Given
reduced BAK oligomerization (Extended Data Fig. 8k) and cytochrome that VDAC2-deficient B16-OVA cells but not MEFs are sensitive to
c or mtDNA release, as well as decreased STING activation and inflam- IFNγ-induced cell death, we compared the expression of BCL-2-family
matory gene expression after IFNγ treatment (Extended Data Fig. 8l–p). proteins in these cell types in the absence or presence of IFNγ. Without
Together, IFNγ sensitizes tumour cells by upregulating expression IFNγ stimulation, B16-OVA tumour cells and MEFs showed comparable
of BIM, BID and BAK, with VDAC2 loss triggering BAK activation and BIM, BID, BAK, MCL-1 and BCL-xL expression, while BAX, PUMA and
subsequent cell death and cGAS–STING activation. BCL-2 levels were highly expressed in B16-OVA tumour cells (Extended
Our genetic interaction CRISPR screen and validation experiments Data Fig. 10g). These results suggest that B16-OVA cells probably exist
also revealed that co-deletion of pro-apoptotic APAF-1 or caspase-925 in a partly primed state for apoptosis compared with MEFs. After IFNγ
rescued the increased cell death and LDH release of IFNγ-stimulated treatment, BIM, BID and BAK expression was upregulated to consider-
VDAC2-deficient tumour cells (Extended Data Figs. 7a and 9a–c). Simi- ably higher levels in B16-OVA cells compared with in MEFs (Extended
larly, pan-caspase inhibitor treatment led to a greater than 90% reduc- Data Fig. 10g). Thus, IFNγ differentially regulates the expression of BIM,
tion in IFNγ-induced cell death in VDAC2-deficient cells (Extended Data BID and BAK in tumour cells compared with in MEFs, which probably
Fig. 9d). Notably, inhibition of apoptosis through pharmacological or underlies the capacity of IFNγ to selectively sensitize tumour cells to
genetic approaches only delayed cell death of VDAC2-deficient tumour cell death after Vdac2 deletion (Extended Data Fig. 10h).
cells, as extensive cell death was still observed after 72 h of IFNγ stimu-
lation (Extended Data Fig. 9e–g). Furthermore, co-deletion of Apaf1
Discussion
or Casp9 in VDAC2-deficient tumour cells led to further enhanced
IFNγ-induced STING signalling and expression of downstream inflam- Tumour immune evasion and resistance to T cell-mediated killing rep-
matory genes (Extended Data Fig. 9h–k), in contrast to Bak1 co-deletion, resent barriers to effective immune-mediated cancer therapies. Besides
which blocked both the increased cell death and cGAS–STING activa- directly killing tumour cells, T cells produce cytokines such as IFNγ that
tion. Similar effects were observed in VDAC2-deficient cells with Casp3 remodel the inflammatory status of the TME48. Mechanisms mediating
or Casp7 co-deletion and those that were treated with the pan-caspase tumour cell responsiveness to IFNγ-mediated cytotoxicity are underex-
inhibitor Q-VD-OPh or emricasan (Extended Data Fig. 9l,m), consist- plored. Here we identified Vdac2 as a potent immune evasion gene, and
ent with the notion that apoptotic caspases inhibit the type I IFN the deletion of Vdac2 induced IFNγ-mediated destruction of tumour
response43–46. Accordingly, GSEA revealed upregulation of the IFNα cells in vivo. Notably, although IFNγ signalling in tumours cells may
8 | Nature | www.nature.com
favour tumour immune evasion by epigenome remodelling to induce
expression of TCIR ligands30, VDAC2-deficient tumour cells showed no Online content
such effects. Furthermore, VDAC2 deficiency promoted mitochondrial Any methods, additional references, Nature Portfolio reporting summa-
damage, suggesting that targeting VDAC2 may override the metabolic ries, source data, extended data, supplementary information, acknowl-
advantage enabled by IFNγ signalling for immune evasion49. Notably, edgements, peer review information; details of author contributions
co-deletion of Vdac2 and Ptpn2 further boosted anti-tumour immu- and competing interests; and statements of data and code availability
nity, probably through combined effects at potentiating IFNγ-induced are available at https://doi.org/10.1038/s41586-025-08732-6.
canonical JAK–STAT signalling7 (through Ptpn2 deletion) together with
activating Vdac2-deletion-associated downstream events, including
1. Waldman, A. D., Fritz, J. M. & Lenardo, M. J. A guide to cancer immunotherapy: from T cell
induction of pronounced cell death phenotypes that were stronger than basic science to clinical practice. Nat. Rev. Immunol. 20, 651–668 (2020).
Ptpn2 deletion. Mechanistically, IFNγ stimulation increased the expres- 2. Sharma, P. et al. Immune checkpoint therapy-current perspectives and future directions.
Cell 186, 1652–1669 (2023).
sion of BIM, BID and BAK in tumour cells, while VDAC2 counterbalances
3. Mellman, I., Chen, D. S., Powles, T. & Turley, S. J. The cancer-immunity cycle: indication,
BAK activation downstream of IFNγ priming and protects tumour cells genotype, and immunotype. Immunity 56, 2188–2205 (2023).
from IFNγ-induced MOMP and mitochondrial disruption to inhibit cell 4. Golstein, P. & Griffiths, G. M. An early history of T cell-mediated cytotoxicity. Nat. Rev.
Immunol. 18, 527–535 (2018).
death and inflammatory remodelling. Overall, our study broadens 5. Wang, W. et al. CD8+ T cells regulate tumour ferroptosis during cancer immunotherapy.
our understanding of IFNγ signalling in mediating T cell-dependent Nature 569, 270–274 (2019).
cytotoxicity against tumours and cancer immunotherapy. 6. Larson, R. C. et al. CAR T cell killing requires the IFNγR pathway in solid but not liquid
tumours. Nature 604, 563–570 (2022).
Although cGAS–STING signalling contributes to tumour immune
7. Manguso, R. T. et al. In vivo CRISPR screening identifies Ptpn2 as a cancer immunotherapy
surveillance, cancers often silence STING activity to mediate immune target. Nature 547, 413–418 (2017).
evasion50 by maintaining genome stability51 or clearing cytosolic DNA52. 8. Finck, A. V., Blanchard, T., Roselle, C. P., Golinelli, G. & June, C. H. Engineered cellular
immunotherapies in cancer and beyond. Nat. Med. 28, 678–689 (2022).
However, whether STING activity and mtDNA release in tumour cells
9. Gao, J. et al. Loss of IFN-γ pathway genes in tumor cells as a mechanism of resistance to
are shaped by adaptive immunity remains unclear. We establish target- Anti-CTLA-4 therapy. Cell 167, 397–404 (2016).
ing VDAC2 as an effective means to overcome immune evasion by sen- 10. Zaretsky, J. M. et al. Mutations associated with acquired resistance to PD-1 blockade in
melanoma. N. Engl. J. Med. 375, 819–829 (2016).
sitizing tumour cells to IFNγ-induced mtDNA release and cGAS–STING
11. Sharma, P., Hu-Lieskovan, S., Wargo, J. A. & Ribas, A. Primary, adaptive, and acquired
activation, highlighting the role of VDAC2 as a gatekeeper for such resistance to cancer immunotherapy. Cell 168, 707–723 (2017).
non-canonical IFNγ signalling events. Consequently, VDAC2-deficient 12. Chapman, N. M. & Chi, H. Metabolic adaptation of lymphocytes in immunity and disease.
Immunity 55, 14–30 (2022).
tumours showed increased CD8+ T cell accumulation and anti-tumour 13. Park, J., Hsueh, P. C., Li, Z. & Ho, P. C. Microenvironment-driven metabolic adaptations
responses. Therefore, VDAC2 targeting links CD8+ T cell-mediated guiding CD8+ T cell anti-tumor immunity. Immunity 56, 32–42 (2023).
IFNγ production and adaptive immune responses to tumour-intrinsic 14. Raynor, J. L. & Chi, H. Nutrients: signal 4 in T cell immunity. J. Exp. Med. 221, e20221839
(2024).
activation of innate immune machinery as well as eliciting excessive 15. Chapman, N. M. & Chi, H. Metabolic rewiring and communication in cancer immunity.
tumour cell death, which mechanistically distinguishes VDAC2 from Cell Chem. Biol. 31, 862–883 (2024).
other targets that mediate tumour immune evasion7,31,53–55. Although 16. Mangalhara, K. C. et al. Manipulating mitochondrial electron flow enhances tumor
immunogenicity. Science 381, 1316–1323 (2023).
BAK mediates both effects of VDAC2 targeting, our data reveal that cell 17. Lawson, K. A. et al. Functional genomic landscape of cancer-intrinsic evasion of killing by
death and STING-mediated inflammatory signals become divergent T cells. Nature 586, 120–126 (2020).
downstream of BAK, further highlighting the role of VDAC2 in coordi- 18. Wei, J. et al. Targeting REGNASE-1 programs long-lived effector T cells for cancer therapy.
Nature 576, 471–476 (2019).
nately orchestrating these two events. 19. Shi, H., Doench, J. G. & Chi, H. CRISPR screens for functional interrogation of immunity.
From a therapeutic perspective, our study highlights the importance Nat. Rev. Immunol. 23, 363–380 (2023).
20. Vredevoogd, D. W. et al. Augmenting immunotherapy impact by lowering tumor TNF
of the dual effects of destructing and inflaming tumours to induce
cytotoxicity threshold. Cell 178, 585–599 (2019).
effective tumour immunity and immunotherapy, thereby advancing 21. Kearney, C. J. et al. Tumor immune evasion arises through loss of TNF sensitivity. Sci.
our knowledge on cancer–immunity cycle3. Notably, many clinical Immunol. 3, eaar3451 (2018).
22. Frangieh, C. J. et al. Multimodal pooled Perturb-CITE-seq screens in patient models
trials combining ICB with other anti-tumour drugs are underway to
define mechanisms of cancer immune evasion. Nat. Genet. 53, 332–341 (2021).
explore possible combinatorial effects56. Targeting VDAC2 may provide 23. Wang, Y. et al. Chemotherapy drugs induce pyroptosis through caspase-3 cleavage of a
opportunities to improve ICB therapies, and may be further leveraged in gasdermin. Nature 547, 99–103 (2017).
24. Rogers, C. et al. Cleavage of DFNA5 by caspase-3 during apoptosis mediates progression
combination with ACT or with small-molecule inhibitors such as those
to secondary necrotic/pyroptotic cell death. Nat. Commun. 8, 14128 (2017).
targeting PTPN257. It will be important to determine the therapeutic 25. Newton, K., Strasser, A., Kayagaki, N. & Dixit, V. M. Cell death. Cell 187, 235–256 (2024).
window and/or specific targeting strategies to minimize potential del- 26. Beltra, J. C. et al. Developmental relationships of four exhausted CD8+ T cell subsets
reveals underlying transcriptional and epigenetic landscape control mechanisms.
eterious effects. Although Vdac2 deletion impairs the development and
Immunity 52, 825–841 (2020).
survival of thymocytes58, we showed that mature CD8+ T cells retained 27. Hudson, W. H. et al. Proliferating transitory T cells with an effector-like transcriptional
their anti-tumour effects in the absence of VDAC2, highlighting discrete signature emerge from PD-1+ stem-like CD8+ T cells during chronic infection. Immunity 51,
1043–1058 (2019).
functional effects of VDAC2 in different T cell populations. Thus, selec-
28. Zander, R. et al. CD4+ T cell help is required for the formation of a cytolytic CD8+ T cell
tive targeting of VDAC2 or the VDAC2–BAK axis may be permissive to subset that protects against chronic infection and cancer. Immunity 51, 1028–1042 (2019).
facilitate IFNγ- and CD8+ T cell-mediated killing and inflammatory 29. Zhou, P. et al. Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer.
Nature 624, 154–163 (2023).
rewiring of tumour cells. Collectively, our study establishes the target-
30. Benci, J. L. et al. Tumor interferon signaling regulates a multigenic resistance program to
ing of VDAC2 in tumour cells as a potent strategy for cancer therapy, by immune checkpoint blockade. Cell 167, 1540–1554 (2016).
enforcing IFNγ-dependent apoptotic cell death and an inflammation 31. Sun, Y. et al. Targeting TBK1 to overcome resistance to cancer immunotherapy. Nature
615, 158–167 (2023).
feedforward loop (Extended Data Fig. 10h), namely the induction of
32. Arlauckas, S. P. et al. Arg1 expression defines immunosuppressive subsets of
‘inflammatory apoptosis’ by partially overriding caspase-mediated tumor-associated macrophages. Theranostics 8, 5842–5854 (2018).
inhibition of STING activation. While innate control of adaptive immu- 33. Mowat, C., Mosley, S. R., Namdar, A., Schiller, D. & Baker, K. Anti-tumor immunity in
mismatch repair-deficient colorectal cancers requires type I IFN-driven CCL5 and
nity is a fundamental immunological principle59,60, our study provides
CXCL10. J. Exp. Med. 218, e20210108 (2021).
insights into how adaptive immunity instructs innate immune-like 34. Liu, S. et al. Phosphorylation of innate immune adaptor proteins MAVS, STING, and TRIF
reprogramming in tumour cells. Whether Vdac2 deletion effects and induces IRF3 activation. Science 347, aaa2630 (2015).
35. West, A. P. et al. Mitochondrial DNA stress primes the antiviral innate immune response.
coordination of adaptive and innate responses and cell death are func-
Nature 520, 553–557 (2015).
tionally conserved in additional contexts that require IFNγ signalling 36. Rath, S. et al. MitoCarta3.0: an updated mitochondrial proteome now with sub-organelle
and type 1 immunity, such as infectious, inflammatory and autoimmune localization and pathway annotations. Nucleic Acids Res. 49, D1541–D1547 (2021).
37. Cheng, E. H., Sheiko, T. V., Fisher, J. K., Craigen, W. J. & Korsmeyer, S. J. VDAC2 inhibits BAK
diseases, warrants further investigation.
activation and mitochondrial apoptosis. Science 301, 513–517 (2003).
Nature | www.nature.com | 9
Article
38. Dewson, G. et al. To trigger apoptosis, Bak exposes its BH3 domain and homodimerizes 54. Pan, D. et al. A major chromatin regulator determines resistance of tumor cells to T cell-
via BH3:groove interactions. Mol. Cell 30, 369–380 (2008). mediated killing. Science 359, 770–775 (2018).
39. Tait, S. W. et al. Resistance to caspase-independent cell death requires persistence of 55. Patel, S. J. et al. Identification of essential genes for cancer immunotherapy. Nature 548,
intact mitochondria. Dev. Cell 18, 802–813 (2010). 537–542 (2017).
40. Yuan, Z. et al. Key residues in the VDAC2-BAK complex can be targeted to modulate 56. Kim, T. K., Vandsemb, E. N., Herbst, R. S. & Chen, L. Adaptive immune resistance at
apoptosis. PLoS Biol. 22, e3002617 (2024). the tumour site: mechanisms and therapeutic opportunities. Nat. Rev. Drug Discov. 21,
41. Naghdi, S., Varnai, P. & Hajnoczky, G. Motifs of VDAC2 required for mitochondrial Bak 529–540 (2022).
import and tBid-induced apoptosis. Proc. Natl Acad. Sci. USA 112, E5590–E5599 57. Baumgartner, C. K. et al. The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent
(2015). anti-tumour immunity. Nature 622, 850–862 (2023).
42. Singh, R., Letai, A. & Sarosiek, K. Regulation of apoptosis in health and disease: the 58. Ren, D. et al. The VDAC2-BAK rheostat controls thymocyte survival. Sci. Signal. 2, ra48
balancing act of BCL-2 family proteins. Nat. Rev. Mol. Cell Biol. 20, 175–193 (2019). (2009).
43. Han, C. et al. Tumor cells suppress radiation-induced immunity by hijacking caspase 9 59. Iwasaki, A. & Medzhitov, R. Control of adaptive immunity by the innate immune system.
signaling. Nat. Immunol. 21, 546–554 (2020). Nat. Immunol. 16, 343–353 (2015).
44. Rongvaux, A. et al. Apoptotic caspases prevent the induction of type I interferons by 60. Chi, H., Pepper, M. & Thomas, P. G. Principles and therapeutic applications of adaptive
mitochondrial DNA. Cell 159, 1563–1577 (2014). immunity. Cell 187, 2052–2078 (2024).
45. White, M. J. et al. Apoptotic caspases suppress mtDNA-induced STING-mediated type I
IFN production. Cell 159, 1549–1562 (2014). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
46. Ning, X. et al. Apoptotic caspases suppress type I interferon production via the cleavage published maps and institutional affiliations.
of cGAS, MAVS, and IRF3. Mol. Cell 74, 19–31 (2019).
47. Ni Chonghaile, T. et al. Pretreatment mitochondrial priming correlates with clinical Open Access This article is licensed under a Creative Commons Attribution-
response to cytotoxic chemotherapy. Science 334, 1129–1133 (2011). NonCommercial-NoDerivatives 4.0 International License, which permits any
48. Hoekstra, M. E. et al. Distinct spatiotemporal dynamics of CD8+ T cell-derived cytokines in non-commercial use, sharing, distribution and reproduction in any medium or
the tumor microenvironment. Cancer Cell 42, 157–167 (2024). format, as long as you give appropriate credit to the original author(s) and the source, provide
49. Tsai, C. H. et al. Immunoediting instructs tumor metabolic reprogramming to support a link to the Creative Commons licence, and indicate if you modified the licensed material.
immune evasion. Cell Metab. 35, 118–133 (2023). You do not have permission under this licence to share adapted material derived from this
50. Ablasser, A. & Chen, Z. J. cGAS in action: expanding roles in immunity and inflammation. article or parts of it. The images or other third party material in this article are included in the
Science 363, eaat8657 (2019). article’s Creative Commons licence, unless indicated otherwise in a credit line to the material.
51. Lu, C. et al. DNA sensing in mismatch repair-deficient tumor cells is essential for If material is not included in the article’s Creative Commons licence and your intended use is
anti-tumor immunity. Cancer Cell 39, 96–108 (2021). not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
52. Tani, T. et al. TREX1 inactivation unleashes cancer cell STING-interferon signaling and permission directly from the copyright holder. To view a copy of this licence, visit http://
promotes antitumor immunity. Cancer Discov. 14, 752–765 (2024). creativecommons.org/licenses/by-nc-nd/4.0/.
53. Ishizuka, J. J. et al. Loss of ADAR1 in tumours overcomes resistance to immune checkpoint
blockade. Nature 565, 43–48 (2019). © The Author(s) 2 025
10 | Nature | www.nature.com
M et ho ds for the indicated genes using CRISPR–Cas9, retrovirus was produced
by co-transfecting the indicated LMA or pSIR-DsRed (BbsI) vector(s)
Mice with pCL-Eco (12371, Addgene) and VSV.G (14888, Addgene) packing
C57BL/6 (000664), OT-I (003831), SMARTA (030450), Rosa26-Cas9 plasmids into Plat-E cells. The supernatant containing viral particles
knock-in (026179), Cd8Cre (008766) and Rag1−/− (002216) mice (all on the was collected 48 h after transfection. B16-OVA-Cas9, MC38-OVA-Cas9
C57BL/6 background) were purchased from the Jackson Laboratory. or MC38-Cas9 cells were transduced with viral supernatant for 48 h in
OT-I mice were crossed with Rosa26-Cas9 knock-in mice to generate RPMI 1640 (for B16-OVA) or DMEM (for MC38-OVA and MC38) + 10%
OT-I-Cas9 mice. To generate Ifngfl/fl mice, loxP sites were inserted into (v/v) FBS supplemented with 10 μg ml−1 polybrene (Sigma-Aldrich),
intron 1 and the 3′ UTR of the Ifng gene, resulting in Cre-mediated dele- followed by sorting Ametrine+ or Ametrine+DsRed+ (for dual targeting)
tion of exons 2–4, which were then bred with Cd8cre mice to generate cells. Cells were cultured for another 14 days for genome editing and
Cd8CreIfngfl/fl mice. Sex- and age-matched (6–10-week-old) mice with expansion. Unless otherwise noted, Cas9-expressing tumour cells were
predetermined genotypes (not blinded to investigators) were ran- used for all of the experiments described in this study.
domly assigned to control and experimental groups throughout the To generate the pMIG-II-HA-VDAC2 plasmid used for VDAC2–BAK
study, and both male and female mice were used. To generate com- interaction analysis in B16-OVA cells that did not express Cas9 (see
plete bone marrow chimeras, bone marrow cells from Cd8CreIfngfl/fl or the ‘Immunoprecipitation and immunoblot analysis’ section below),
control Ifngfl/fl mice were flushed from mouse tibias and femurs, and the Vdac2 coding sequence was PCR-amplified from B16-OVA cDNA
red blood cells were lysed using ACK lysis buffer, followed by intra- and cloned into the pcDNA3.1-HA vector (128034, Addgene). The
venous injection into sublethally (5.5 Gy) irradiated Rag1−/− recipient HA-Vdac2 coding sequence was amplified and cloned into the pMIG-II
mice. Mice were inoculated with the indicated tumours at 8 weeks after (52107, Addgene) retroviral vector. To generate the pMIA-Flag-BAK
bone marrow reconstitution. All of the mice were maintained under and pMIA-Flag-BAX plasmids, Flag-Bak1 and Flag-Bax coding
specific-pathogen-free conditions in the Animal Resource Center at sequences were PCR-amplified from pcDNA-Flag-BAK or pMIG-BAX
St. Jude Children’s Research Hospital. The animals were housed under (8788, Addgene) and cloned into pMIA (52113, Addgene). To generate
12 h–12 h light–dark cycles coinciding with daylight in Memphis, TN, wide-type HA-VDAC2 plasmid, the HA-Vdac2 sequence with 6 amino acid
USA (light on at 06:00 and off at 18:00). Food and water were provided synonymous mutation at sgVdac2 targeting sequence (to circumvent
ad libitum. The St. Jude Children’s Research Hospital Animal Resource CRISPR–Cas9-mediated cleavage; ATCCATGGGTCAGCTGTCTTTGGT
Center was maintained at 20–25 °C and 30–70% humidity. The research changed (bold bases) to ATACACGGATCGGCAGTATTTGGT) was first
conducted in this study complied with all of the relevant ethical regula- synthesized by Integrated DNA Technologies (IDT). On the basis of this
tions. Experiments and procedures were approved by and performed CRISPR–Cas9-resistant VDAC2 construct, we designed three VDAC2
in accordance with the Institutional Animal Care and Use Committee mutants to alter specific sequences (A172R, T168N and D170E (T168N/
(IACUC) of St. Jude Children’s Research Hospital. The number of mice D170E) or T168N, D170E and A172R (T168N/D170E/A172R) reported to
per group were selected based on previous publications29,49,61. have reduced ability to bind BAK40,41, and these were synthesized by IDT.
The following sequences were used for introducing such mutations:
Cell lines (1) A172R (GCC > CGC); (2) T168N/D170E (ACCTTTGAC > AACTTTGAA);
B16-OVA, MC38-OVA and MC38 cell lines were provided by D. Vignali. (3) T168N/D170E/A172R (ACCTTTGACAGTGCC > AACTTTGAAAG
The HEK293T and LoVo cell lines were purchased from the American TCGC). All of the plasmids were cloned using the NEBuilder HiFi DNA
Type Culture Collection (ATCC). The Plat-E cell line was provided by Assembly Cloning Kit (E5520S, NEB). To generate stable B16-OVA
Y.-C. Liu. All cell lines were cultured in Dulbecco’s modified Eagle’s cells with Omi-mCherry (for imaging analysis), HA-VDAC2 and/or
medium (DMEM) (Gibco) or RPMI-1640 medium (Gibco) supplemented Flag-BAK/BAX overexpression (for immunoprecipitation), retro-
with 10% (v/v) FBS and 1% (v/v) penicillin–streptomycin at 37 °C with virus was produced by co-transfecting pBabe(puro)-Omi-mCherry
5% CO. No commonly misidentified cell lines (International Cell Line (48685, Addgene), pMIG-II-HA-VDAC2 or pMIA-Flag-BAK/BAX plasmid
2
Authentication Committee) were used in this study. Cell lines were with pCL-Eco (12371, Addgene) and VSV.G (14888, Addgene) packing
tested and determined to be free of mycoplasma contamination. The plasmids into plat-E cells. Omi-mCherry-, HA-VDAC2-, Flag-BAK- or
aforementioned cell lines were not independently authenticated. Flag-BAX-expressing cells were sorted based on the fluorescence
reporter mCherry (for Omi-mCherry), GFP (for HA-VDAC2) or Ametrine
Plasmid and stable cell line generation (for Flag-BAK or Flag-BAX).
The sgRNAs targeting Vdac2, Casp3, Casp7, Gsdme, Ifng, Tnf, Tnfrsf1a,
Prf1, Ifngr1, Ifngr2, Jak1, Ptpn2, Vdac1, Vdac3, Cgas, Sting1, Mavs, Irf3, T cell-mediated tumour cell killing assay in vitro
Ccl5, Bak1, Bax, Apaf1 and Casp9 or non-targeting control were syn- In total, 1 × 105 tumour cells were seeded into a 12-well plate for the
thesized, annealed and ligated into BbsI-HF-digested (R3539L, NEB) timepoints indicated in the figures and their legends. Naive OT-I CD8+
retroviral sgRNA vectors (LMA or pSIR-DsRed (BbsI), with Ametrine T cells were isolated from the spleen and peripheral lymph nodes of OT-I
or DsRed as a selection marker, respectively)18,62. A list of the sgRNA mice and activated using 10 μg ml−1 anti-CD3 (2C11, Bio X Cell, BE0001-1)
sequences is provided in Supplementary Table 10. For the mouse liver and 5 μg ml−1 anti-CD28 (37.51, Bio X Cell, BE0015-1) antibodies as previ-
tumour model, pX330-sgNTC and pX330-sgVdac2 plasmids were gener- ously described18. Activated OT-I cells were then expanded in Click’s
ated from pX330 (42230, Addgene) according to the established pro- medium (Irvine Scientific) containing 10% dialysed FBS supplemented
tocol63. To generate Cas9-expressing tumour cell lines (B16-OVA-Cas9, with glutamine in the presence of human recombinant IL-2 (20 IU ml−1;
MC38-OVA-Cas9 and MC38-Cas9), lentivirus was produced by PeproTech), mouse IL-7 (12.5 ng ml−1; PeproTech) and IL-15 (25 ng ml−1;
co-transfecting Lenti-Cas9-GFP (86145, Addgene) plasmid with psPAX2 PeproTech) for 2–3 days. Preactivated OT-I CD8+ T cells were then cocul-
(12260, Addgene) and pMD2.G (12259, Addgene) packing plasmids into tured with tumour cells at the indicated effector:tumour target ratios.
HEK293T cells. The supernatant containing viral particles was collected The live tumour cell number was calculated, and the mean value of
at 48 h after transfection. B16-OVA, MC38-OVA and MC38 cells were E:T = 0:1 group was set equal to 100%. Fresh human leukapheresis prod-
transduced with viral supernatant for 48 h in RPMI-1640 (for B16-OVA) ucts were purchased from Charles River. These leukapheresis products
or DMEM (for MC38-OVA and MC38) + 10% (v/v) FBS supplemented with were obtained from three de-identified healthy donors (donor numbers
10 μg ml−1 polybrene (Sigma-Aldrich), followed by sorting of transduced ECT026, ECT028 and ECT031) and were used to generate human CAR
(GFP+) into single clones, followed by expansion. Cas9 expression was T cells (ECT24-PD030) by St. Jude Experimental Cellular Therapeutics
verified by immunoblot analysis61. To generate tumour cells deficient Laboratory (ECTL), using an established protocol and a previously
Article
described lentiviral vector that encodes a B7-H3-CAR with a CD28ζ 5 min at room temperature, the embryo suspension was transferred to a
signalling domain64. Generated CAR T cells were cryopreserved at the new 50 ml conical tube and centrifuged at 1,500 rpm for 5 min. The cell
end of production. As de-identified leukapheresis products were used, pellet was resuspended in MEF medium and filtered through a 70 μm
CAR T cell generation and experiments with these cells are considered cell strainer to remove debris. The cells from each embryo were plated
non-human subject research. This determination was confirmed by the into one T-160 plates or three T-75 (or 10 cm plates), reaching around
Institutional Review Board (IRB) at St. Jude Children’s Research Hos- 70% confluency within approximately 2 days. MEFs were transduced
pital. Before conducting cytotoxicity assays, CAR T cells were thawed with sgNTC- or sgVdac2-expressing retrovirus for 48 h in MEF medium
and cultured in X-VIVO-15 medium (BEBP04-744Q, Lonza) containing containing 10 μg ml−1 polybrene (Sigma-Aldrich), followed by sorting
5% human serum (H4522, Sigma-Aldrich) in the presence of human Ametrine+ MEFs. Ametrine+ transduced MEFs were cultured for another
recombinant IL-7 (10 ng ml−1, 130-093-764, Miltenyi) and human recom- 14 days for genome editing and expansion. For assays involving IFNγ
binant IL-15 (10 ng ml−1, 130-095-362, Miltenyi) for 24 h. Recovered CAR (10 ng ml−1, 24 h), ΤNF (10 ng ml−1) plus cycloheximide (5 μg ml−1, 4 h),
T cells were then co-cultured with sgNTC- or sgVDAC2-transduced LoVo or etoposide (20 μM, 24 h) treatments, sgNTC- or sgVdac2-transduced
cells65 at the indicated B7-H3-CAR T effector:tumour target ratios. At MEFs were treated for the indicated times listed above, followed by
the indicated timepoints of co-culture, the number of live tumour cells flow cytometry, immunoblotting or RT–qPCR analysis, as indicated
were counted by flow cytometry using CountBright Absolute Counting in the figure legends.
Beads (C36950, Invitrogen).
Tumour models and immunotherapeutic treatments
T cell purification, differentiation and viral transduction for Mice (C57BL/6 mice, Cas9+ transgenic mice, Rag1−/− mice or complete
in vitro assays and adoptive transfer into tumour-bearing mice bone marrow chimeras) were injected s.c. with 1 × 106 B16-OVA-Cas9,
Naive Cas9-expressing OT-I CD8+ T cells were isolated as mentioned MC38-OVA-Cas9 or MC38-Cas9 cells expressing the indicated sgRNAs
above. Purified naive OT-I cells were activated in vitro for 18–20 h in the right flank. For the lung metastasis model, 1 × 106 B16-OVA-Cas9
with 10 μg ml−1 anti-CD3 (2C11, Bio-X-Cell), 5 μg ml−1 anti-CD28 cells transduced with the indicated sgRNAs were resuspended in 100 μl
(37.51; Bio-X-Cell) before viral transduction. Viral transduction was phosphate-buffered saline (PBS, Gibco) and injected into Cas9+ trans-
performed by spin-infection at 900g at 25 °C for 3 h with 10 mg ml−1 genic mice through the tail vein. After tumour inoculation, mice were
polybrene (Sigma-Aldrich). After transduction, cells were cultured randomly assigned to different groups for ICB and/or ACT treatments.
in T cell medium containing human recombinant IL-2 (20 IU ml−1; For tumour models with OT-I T cell transfer, preactivated OT-I cells
PeproTech), mouse recombinant IL-7 (12.5 ng ml−1; PeproTech) and (the details are provided above) were transferred intravenously into
mouse recombinant IL-15 (25 ng ml−1; PeproTech) for 4 days. Naive tumour-bearing mice at day 7 after tumour inoculation (1 × 107 OT-I cells
Cas9-expressing CD4+ T cells were isolated from the spleen and periph- per mouse). Anti-PD-L1 antibody (10 F.9G2, Bio X Cell) or IgG isotype
eral lymph nodes of Cas9-SMARTA mice as previously described66. control (LTF-2, Bio X Cell) was injected intraperitoneally three times at
Viral transduction was performed by spin-infection at 900g at 25 °C a dose of 100 μg in 100 μl PBS on days 7, 10 and 13 after inoculation of
for 3 h with 10 mg ml−1 polybrene (Sigma-Aldrich). After transduction, B16-OVA-Cas9 cells transduced with the indicated sgRNAs, as described
cells were cultured for iT or T 1 differentiation: naive CD4+ T cells previously61. Anti-PD-1 antibody (J43, Bio X Cell) or rat IgG isotype con-
reg H
were stimulated with 5 μg ml−1 anti-CD3 (2C11; Bio-X-Cell), 5 μg ml−1 trol (LTF-2, Bio X Cell) was injected intraperitoneally three times at a
anti-CD28 (37.51; Bio-X-Cell) in the presence of human IL-2 (100 U ml−1) dose of 100 μg in 100 μl PBS on days 7, 9 and 11 after inoculation of
plus human TGFβ (0.5 ng ml−1; PeproTech) for iT polarization; or MC38-Cas9 cells expressing the indicated sgRNAs, as described previ-
reg
human recombinant IL-2 (100 U ml−1) plus mouse recombinant IL-12 ously61. Mice that completely rejected tumours were rechallenged with
p40 (0.5 ng ml−1; BD Biosciences) for T 1 polarization for 5.5 days. 1 × 106 B16-OVA-Cas9-sgNTC or MC38-Cas9-sgNTC cells on day 40 or
H
Transduced cells were sort-purified based on the expression of day 50. Anti-CD8α antibody (2.43, Bio X Cell) or rat IgG isotype control
Ametrine. (LTF-2, Bio X Cell) was injected intraperitoneally at a dose of 200 μg in
For assays involving IFNγ or anti-IFNγ treatments of sgNTC- or sgV- 100 μl PBS on days −1, 2, 5, 8 and 11. Anti-IFNγ antibody (XMG1.2, Bio X
dac2-transduced OT-I, iT or T 1 cells, Ametrine+ sorted cells were Cell) or IgG isotype control (HRPN, Bio X Cell) was injected intraperi-
reg H
incubated with IFNγ (10 ng ml−1) or anti-IFNγ (10 μg ml−1) for 12–24 h toneally at a dose of 200 μg in 100 μl PBS on days −1, 3, 7, 11 and 15 or
as indicated in the figure legends. Cells were collected for flow cytom- the timepoints as indicated in the figures and their legends. Emricasan
etry, immunoblotting or quantitative PCR with reverse transcription was dissolved in PBS and tumour-bearing mice were treated with
(RT–qPCR) analysis as indicated in the figure legends. For adoptive emricasan (or PBS vehicle) intraperitoneally at 20 mg kg−1, twice a day
transfer of sgNTC- or sgVdac2-transduced OT-I cells into B16-OVA for 3 days43. To establish the constitutively active AKT and NRAS-driven
tumour-bearing mice, C57BL/6 mice were s.c. injected with 3 × 105 liver tumour mouse model, 6-week-old male mice were injected with
B16-OVA melanoma cells on day 0. At day 12 after tumour inocula- 5 μg pT3-EF1a-myrAKT1-HA (31789, Addgene), 5 μg pT-Caggs-NRASG12V
tion, a total of 4 × 106 sgNTC-transduced (labelled with Ametrine) and (20205, Addgene) and 2.5 μg pCMV(CAT)T7-SB100 (34879, Addgene) as
sgVdac2-transduced (labelled with Ametrine) OT-I cells were injected previously described67. To target Vdac2 in vivo, 50 μg pX330-sgNTC or
intravenously into separate B16-OVA tumour-bearing mice. Tumour pX330-sgVdac2 was mixed together with the above oncogenic vectors
growth and mouse survival were monitored. and injected into mice. A volume of plasmid solution equal to 10% of the
body weight in sterile Ringer’s solution was injected through the tail
Cas9+ MEF isolation, transduction and treatment vein within 5–7 s67. s.c. B16-OVA, MC38-OVA and MC38 tumours were
Cas9-expressing mouse embryos were isolated from Cas9-transgenic measured every 2 days with digital callipers and the tumour volumes
mice on E14.5. The embryos were euthanized by decapitation, and the were calculated using the formula: length × width × width × π/6. To
fetal liver and heart were removed with forceps, followed by rinsing of isolate intratumoural lymphocytes, s.c. tumours were collected on
the embryos with ice-cold PBS. The embryos were incubated with 3–5 ml the indicated days after inoculation, excised, minced and digested
ice-cold Trypsin-EDTA (25200-56, Gibco) overnight on ice in a 50 ml with 1 mg ml−1 collagenase IV (LS004188, Worthington Biochemicals)
conical tube (Falcon). The trypsin-EDTA was aspirated off the embryos, and 200 U ml−1 DNase I (DN25-1G, Sigma-Aldrich) for 1 h at 37 °C and
followed by resuspension in 2 ml of pre-warmed (37 °C) trypsin-EDTA passed through 70-μm filters to remove undigested tumour tissues.
and incubation for 5–7 min in a 37 °C water bath. The digestion reaction TILs from MC38-OVA tumours were further isolated by density-gradient
was stopped by addition of 10 ml of MEF medium (DMEM + 10% FBS) fol- centrifugation over Percoll (17089101, Cytiva). Tumour size limits were
lowed by pipetting without introduction of air bubbles. After resting for approved to reach a maximum of 3,000 mm3 or ≤20% of body weight
(whichever was lower) by the IACUC of St. Jude Children’s Research B16-OVA-Cas9 cells were treated with IFNγ (554587, BD) at 10 ng ml−1 for
Hospital. 24 h, resulting in more than 50% tumour cell death (2 replicates). Trans-
duced VDAC2-deficient B16-OVA-Cas9 cells without IFNγ treatment
CRISPR–Cas9 mutagenesis screening using the lentiviral were used as control. A total of 8 × 106 transduced VDAC2-deficient
metabolic library tumour cells (about 100× cell coverage per sgRNA) was collected and
Lentiviral sgRNA metabolic library construction. The mouse meta- used for deep sequencing. DNA exaction and sequencing library prepa-
bolic library containing 3,017 genes was synthesized based on the gene ration were as described in the ‘Sequencing library preparation’ section
list from reported human metabolic-associated genes, and library using Q5 enzyme (M0541L, NEB) for PCR reactions.
synthesis, purification and quality control were described previously18.
In brief, 6 sgRNAs were designed for each gene and were split into two Data processing. For data analysis, FASTQ read files obtained after
sub-libraries (AAAQ05 and AAAQ07), with each containing 3 sgRNAs sequencing were demultiplexed using the Hi-Seq analysis software
targeting one gene and 500 non-targeting controls. (Illumina) and processed using MAGeCK (v.0.5.9.4)69. Raw counts for
each sgRNA were generated with MAGeCK ‘count’ module by map-
In vitro and in vivo screens. Lentivirus was produced by co-transfecting ping reads to the mouse metabolic library or the Brie library with
HEK293T cells with the two lentiviral metabolic sublibrary plasmids, non-targeting sgRNAs as the control. The MAGeCK ‘test’ function was
psPAX2 (12260, Addgene) and pCAG4-Eco (35617, Addgene). Then, used to identify screen hits. For the initial in vitro and in vivo screens,
48 h after transfection, the supernatant containing viral particles was we were able to detect the majority (~99.9% and ~98.8%, respectively)
collected and frozen at −80 °C. A single clone of B16-OVA-Cas9 cells of genes contained in the library from tumour cells (Supplementary
with high Cas9-editing activity was expanded and transduced with Table 1). Total read counts were used for raw count normalization and
the two sub-pools at a multiplicity of infection (MOI) of 0.2–0.3 to the secondbest method was used for logFC quantification. The effects
2
achieve 20–30% transduction efficiency. The sublibrary-transduced of screen hits were ranked by MAGeCK RRA score.neg (in vitro OT-I
B16-OVA-Cas9 cells were purified by sorting of Ametrine+ cells and treated versus non-treated or C57BL/6 mice + OT-I versus Rag1−/− mice).
then mixed at 1:1 ratio. Cells were cultured in vitro for another 14 days For the genome-scale secondary genetic interaction screen using the
for genome editing and expansion. An aliquot of 5 × 106 transduced Brie library68, median read counts across all samples were used for
B16-OVA-Cas9 cells (about 250× cell coverage per sgRNA) was saved as normalization, and the ‘mean’ method was used for logFC quanti-
2
the input. For in vitro screening, transduced B16-OVA-Cas9 cells were fication and --gene-test-fdr-threshold was set to 1. The significantly
co-cultured with preactivated OT-I CD8+ T cells (see details above) for enriched or depleted screen hits in sgVdac2-transduced B16-OVA tu-
18 h. The remaining tumour cells (5 × 106, about 250× cell coverage mour cells were defined as |logFC| > 0.5 and MAGeCK RRA score < 0.05
2
per sgRNA) were sorted and used for deep sequencing analysis. For (Extended Data Fig. 7a). The targeted genes in the Brie library were
in vivo screening, 1 × 106 transduced B16-OVA cells were inoculated into further overlapped with genes included in the MitoCarta 3.0 database36
Rag1−/− mice or Cas9+ transgenic mice (10 mice each group, 2 replicates). (1,140 for total) to generate a list of 1,032 mitochondria-associated
Preactivated OT-I cells (the details are provided above) were transferred genes (Fig. 4b). The logFC values and MAGeCK RRA scores of the
2
intravenously into B16-OVA tumour-bearing mice at day 7 after tumour mitochondria-associated genes in this secondary genetic interaction
inoculation (1 × 107 OT-I cells per mouse). At day 17 after tumour chal- screen were visualized as a volcano plot by ggplot2 R package (v.3.3.5),
lenge, Ametrine+ tumour cells were collected from the pooled tumour with the top 1 and 2 significantly enriched (based on MAGeCK RRA
tissues using a cell sorter. At least 5 × 106 sorted B16-OVA cells (>250× score) mitochondria-associated gene candidates (Casp9 and Bak1)
cell coverage per sgRNA) were used for deep sequencing analysis. annotated.
Sequencing library preparation. Genomic DNA was extracted by Flow cytometry
using the DNeasy Blood & Tissue Kits (69506, Qiagen). Primary PCR For analysis of surface markers, cells were first incubated with Fc
was performed using the KOD Hot Start DNA Polymerase (71086, Milli- block (2.4G2, Bio X Cell) for 10 min in PBS containing 2% (w/v) FBS,
pore) and the following pair of Nextera next-generation sequencing and then stained with the appropriate antibodies on ice for 30 min.
(NGS) primers: (Nextera NGS forward (-F): TCGTCGGCAGCGTCAG For intracellular cytokine detection, cells were stimulated for 4 h
ATGTGTATAAGAGACAGTTGTGGAAAGGACGAAACACCG; Nextera with phorbol 12-myristate-13-acetate (Sigma-Aldrich) plus ionomycin
NGS reverse (-R): GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGCC (Sigma-Aldrich) in the presence of monensin (GolgiStop, 554724, BD
ACTTTTTCAAGTTGATAACGG). Primary PCR products were purified Biosciences) and stained for surface markers. The cells were fixed and
using the AMPure XP beads (A63881, Beckman). A second PCR reaction permeabilized using the CytoFix/CytoPerm fixation/permeabilization
was performed to attach Illumina adaptors and indexes to barcode each kit (554774, BD Biosciences) according to the manufacturer’s instruc-
sample. Hi-seq 50-bp single-end sequencing (Illumina) was performed tions followed by intracellular cytokine staining using the appropri-
for library sequencing. ate antibodies on ice for 30 min. For transcription factor staining,
cells were stained for surface markers, followed by fixation and per-
Secondary genome-scale CRISPR–Cas9 mutagenesis screening meabilization using FOXP3/transcription factor staining buffer set
in VDAC2-deficient tumour cells (00-5523-00, eBioscience) according to the manufacturer’s instructions
In vitro screening after IFNγ treatment. Lentivirus was produced by and intracellular staining with the appropriate antibodies on ice for
co-transfecting HEK293T cells with lentiviral genome-scale Brie library 30 min. 7-AAD (A9400, 1:200, Sigma-Aldrich) or fixable viability dye
plasmids with the puromycin-resistance gene68, psPAX2 (12260, Add- (65-0865-18, 1:1,000, eBioscience) was used for dead cell exclusion.
gene) and pCAG4-Eco (35617, Addgene). Then, 48 h after transfection, Active caspase-3 staining of control and VDAC2-deficient tumour cells
the supernatant containing viral particles was collected and frozen at was performed using instructions and reagents from an active caspase-3
−80 °C. VDAC2-deficient B16-OVA-Cas9 cells (transduction efficiency, apoptosis kit (BD Biosciences). The following antibodies were used: PE–
~5%) were subsequently transduced with the Brie library at an MOI anti-CD45 (1:400, 30-F11, 12-0451-83, eBioscience), FITC–anti-CD45.2
of 0.2–0.3. Brie-library-transduced VDAC2-deficient B16-OVA-Cas9 (1:400, 104, 109806, BioLegend), Brilliant Violet 785–anti-CD45.2
cells were then cultured with 4 μg ml−1 puromycin for another 14 (1:400, 104, 109839, BioLegend), Alexa Fluor 700–anti-CD8α (1:400,
days to select for transduced cells. An aliquot of 8 × 106 transduced 53-6.7, 100730, BioLegend), Brilliant Violet 605–anti-CD8α (1:400,
VDAC2-deficient B16-OVA-Cas9 cells (about 100× cell coverage per 53-6.7, 100743, BioLegend), Alexa Fluor 650–anti-CD4 (1:400, GK1.5,
sgRNA) were saved as input. In total, 5 × 107 transduced VDAC2-deficient 100469, BioLegend), Brilliant Violet 785–anti-TCRβ (1:400, H57-597,
Article
109249, BioLegend), PE/Dazzle 594–anti-PD-1 (1:400, 29F.1A12, Bio- the cytosolic supernatants were transferred to fresh tubes and centri-
legend,135228), Brilliant Violet 711–anti-B220 (1:400, RA3-6B2, fuged at 16,000g for 10 min to pellet any remaining cellular debris. The
103255, BioLegend), FITC–anti-CD19 (1:400, eBio1D3, 11-0193-85, cytosolic DNA and total cellular DNA (from whole-cell extracts) were
eBioscience), PE/Cyanine7–anti-IFNγ (1:200, XMG1.2, 505826, Bio- purified using the DNeasy Blood & Tissue Kit (69506, Qiagen). RT–qPCR
Legend), Brilliant Violet 421–anti-TNF (1:200, MP6-XT22, 506328, was performed on both whole-cell extracts and cytosolic fractions using
BioLegend), Alexa Fluor 647–anti-GZMB (1:100, GB11, 515406, Bio- mtDNA primers (mtCytb, mtNd4, mt16S, D-loop1, D-loop2 and D-loop3),
Legend), FITC–anti-FOXP3 (1:200, FJK-16s, 11-5773-82, eBioscience), and the C values of whole-cell extracts served as normalization con-
T
BV650–anti-Ki-67 (1:100, B56, 563757, BD Biosciences), Alexa Fluor trols for the values of cytosolic fractions (FC = log−ΔΔCT). A list of the
2
647–anti-active caspase-3 (1:100, C92-605, 560626, BD Biosciences), primers used for qPCR analysis is provided in Supplementary Table 11.
PE–anti-IL-2 (1:200, JES6-5H4, 554428, BD Biosciences). Intratumoural
CD8+ T cells were gated as CD45+CD8+TCRβ+; CD4+FOXP3− T cells were Generation of mtDNA-depleted cells
gated as CD45+CD4+TCRβ+FOXP3−; CD4+FOXP3+ T cells were gated B16-OVA cells were cultured in the presence or absence of 200 ng ml−1
reg
as CD45+CD4+TCRβ+FOXP3+; B cells were gated as CD45+B220+CD19+. ethidium bromide (EtBr, E7637, Sigma-Aldrich), as described previ-
Tumour cells were gated as Ametrine+CD45− cells. BD FACSDIva soft- ously44,45, for 6 days. Before IFNγ treatment, the culture medium was
ware (v.8) was used to collect flow cytometry data on LSRII, Fortessa replaced, and cells were cultured overnight in the absence of EtBr. To
or Symphony A3 cytometers (BD Biosciences). measure the efficiency of mtDNA depletion, total extracts were pre-
pared by resuspending the cells in NaOH 50 mM, incubating at 95 °C for
Cytokine-induced cell death assays in vitro 1 h and neutralizing by adding 10% volume 1 M Tris (pH 7.5). The ratio
To analyse cytokine-induced cell death, the indicated concentration of of mtDNA versus genomic DNA was measured using qPCR .
IFNγ and/or TNF (554589, BD) or human IFNγ (554616, BD) was added.
For cell death inhibition assays, pan-caspase inhibitor emricasan43 Immunoprecipitation, subcellular fractionation and
(20 μM), ferroptosis inhibitor ferrostatin-170 (Fer-1, 10 μM), necroptosis immunoblot analysis
inhibitor necrostatin-171 (Nec-1, 20 μM) and GSDMD-mediated pyropto- For immunoprecipitation, 2 × 106 cells expressing HA-VDAC2 and/or
sis inhibitor disulfiram72 (20 μM) were used. Tumour cell numbers were Flag-BAK or Flag-BAX were lysed in ice-cold Pierce IP lysis buffer (87787,
quantified at the indicated timepoints by flow cytometry using the cell Thermo Fisher Scientific) containing protease and phosphatase inhibi-
counting beads. Alternatively, cell death was detected and quantified tor cocktail (78442, Thermo Fisher Scientific) and 1% digitonin (D141,
in real-time using the IncuCyte S3 or IncuCyte SX5 imaging system (Sar- Sigma-Aldrich) with rotation at 4 °C for 30 min. The cell lysate was
torius). In brief, 2 × 104 B16-OVA cells per well were plated into a 48-well centrifuged at 13,000g for 10 min at 4 °C, and the supernatant was
plate in RPMI-1640 medium containing 10% FBS, 500 nM propidium incubated with anti-Flag (M8823, Sigma-Aldrich) or anti-HA (88836,
iodide (P3566, Invitrogen) or 100 nM SYTOX Deep Red (S11381, Invit- Thermo Fisher Scientific) magnetic beads at 4 °C for 2 h. The beads
rogen) and the indicated concentration of IFNγ (details are provided in were washed three times with ice-cold IP lysis buffer (87787, Thermo
the associated figures). Cells were imaged every 1 or 2 h and the PI+ or Fisher Scientific) and resuspended with 1× complete Laemmle sample
SYTOX Deep Red+ cells (counted as dead cells) were quantified using buffer (1610747, Bio-Rad).
the IncuCyte FLR or Zoom software (http://www.essenbioscience.com/ To detect cytochrome c and SMAC in the subcellular fractions, the
en/products/software/) as described previously73. For the LDH-release mitochondrial and cytosolic fractions were isolated using the Mito-
assay, the cell culture medium was collected at the indicated time- chondrial Fractionation Kit (Active Motif) according to the manufac-
points and centrifuged at 2,000g for 5 min to obtain the supernatant. turer’s instructions. In brief, cells were treated with 10 ng ml−1 IFNγ plus
LDH release was detected using the CytoTox 96 Non-Radioactive Cyto- 40 μM pan-caspase inhibitor Q-VD-OPh for 24 h and then washed using
toxicity Assay Kit (G1780, Promega) according to the manufacturer’s pre-chilled 1× PBS and centrifuged at 600g for 5 min at 4 °C. The cell
instructions. The absorbance was measured on the VERSAmax Tun- pellet was resuspended in 1 ml ice-cold cytosolic buffer and incubated
able Microplate Reader (Molecular Devices). For annexin-V and 7-AAD on ice for 15 min, then transferred to a pre-chilled pestle homogenizer.
staining, tumour cells (including both the adherent and suspension Cells were homogenized using 30–50 strokes with the homogenizer and
fractions) were washed and resuspended with annexin V binding buffer centrifuged at 800g for 20 min at 4 °C. After centrifugation, the super-
(00-0055-56, eBioscience) and then stained with APC–anti-annexin V natant was transferred to a fresh pre-chilled microcentrifuge tube and
(1:50, BMS306APC-100, Invitrogen) in annexin V binding buffer for centrifuged at 10,000g for 20 min at 4 °C to pellet the mitochondria;
15 min at room temperature. After washing with annexin V binding the supernatant contained the cytosolic fraction. The mitochondrial
buffer, the cells were resuspended with 7-AAD working solution (51- pellet was washed once with 100 μl 1× cytosolic buffer and lysed with
65875X, BD) and analysed using flow cytometry. 100 μl complete mitochondrial buffer on ice for 15 min to obtain the
mitochondrial fraction. The cytosolic fraction was transferred to a
Cytosolic mtDNA extraction and quantification fresh pre-chilled microcentrifuge tube and centrifuged at 16,000g for
B16-OVA cells were cultured in a 10 cm dish and treated with 10 ng ml−1 20 min at 4 °C to remove any residual mitochondria.
IFNγ plus pan-caspase inhibitor Q-VD-OPh (40 μM, HY-12305, Med- For chemical cross-linking of cysteines, cells were treated with
ChemExpress) for 24 h, followed by extraction and detection of total IFNγ (10 ng ml−1) plus Q-VD-OPh74 (40 μM) for 24 h or ABT-737
DNA and cytosolic DNA as described previously35. In brief, 1 × 107 (5 mM) + S63845 (5 mM) + Q-VD-OPh75 (40 μM) for 6 h. The mito-
B16-OVA cells were divided into two equal aliquots. One aliquot was chondrial fraction was obtained as mentioned before and resus-
resuspended in 300 μl of 50 mM NaOH and boiled for 60 min to solu- pended in cross-linking buffer (20 mM HEPES/KOH (pH 7.5), 100 mM
bilize DNA. Then, 10% volume of 1 M Tris-HCl (pH 7.5) was added to sucrose, 2.5 mM MgCl and 50 mM KCl) containing the fresh added
2
neutralize the pH and then centrifuged at 12,000g for 10 min to pellet 1,6-bis-maleimidohexane (BMH, 0.5 mM, 13.0 A° linker, Thermo Fisher
intact cells. Moreover, these extracts served as normalization con- Scientific) and incubated for 30 min at room temperature. Cross-linking
trols for total genomic DNA and mtDNA. The second equal aliquots was quenched by addition of reducing buffer (1× complete Laemmle
were resuspended in 300 μl of buffer containing 150 mM NaCl, 50 mM sample buffer with 10% 2-mercaptoethanol, M6250, Sigma-Aldrich),
HEPES (pH 7.4), and 20 mg ml−1 digitonin (D141, Sigma-Aldrich). The and the samples were analysed by SDS–PAGE.
homogenates were incubated for 15 min on ice to allow selective plasma For immunoblot analysis of tumours treated with isotype or
membrane permeabilization and then sequentially centrifuged at anti-PD-L1 in vivo (as described above), B16-OVA tumour tissues
980g for 3 min for a total of three times to pellet intact cells. Finally, (~100 mg) from tumour-bearing mice were homogenized in 1 ml
ice-cold RIPA buffer (89900, Thermo Fisher Scientific) containing at the indicated timepoints and centrifuged at 13,000g for 10 min at
protease and phosphatase inhibitor cocktail and homogenized using 4 °C to obtain the supernatant. IFNγ and IFNβ was measured by ELISA
the Bead Ruptor Elite (OMNI). The lysate was centrifuged at 13,000g using the Mouse IFNγ Quantikine ELISA Kit (MIF00-1, R&D systems) or
for 10 min at 4 °C, and the supernatant was mixed with 4× complete Mouse IFNβ Quantikine ELISA Kit (MIFNB0, R&D systems) according
Laemmli Sample Buffer (1610747, Bio-Rad). For immunoblot analysis to the manufacturer’s instructions. Absorbance was measured on a
of cells treated with IFNγ, cisplatin (HY-17394, MCE) or etoposide (HY- VERSAmax Tunable Microplate Reader (Molecular Devices).
13629, MCE) in vitro, cultured cells were directly lysed with 1× complete
Laemmli sample buffer. In Extended Data Figs. 8c and 10g, IFNγ-induced Immunostaining and histology analyses
expression of BCL-2 family members was analysed in B16-OVA cells Live-cell imaging was performed using B16-OVA-Cas9-sgNTC or
without Cas9 expression. All of the protein samples were boiled at B16-OVA-Cas9-sgVdac2 cells, which were cultured in chambered cov-
95 °C for 10 min, separated using 4–12% Criterion XT Bis-Tris Protein erslips (80426, Ibidi). Tumour cells expressing Omi-mCherry were
Gel (3450125, Bio-Rad) and transferred to a PVDF membrane (1620177, used for determination of MOMP (the pBabe(puro)-Omi-mCherry
Bio-Rad). The membranes were blocked using 5% BSA for 1 h and then plasmid expresses fusion protein in the mitochondria intermembrane
incubated overnight with primary antibodies (see below). The mem- space, and is released on MOMP39). Time-lapse imaging was performed
branes were then washed with TBST and then incubated with secondary using the A1RHD25 (Nikon Instruments) resonant scanning confocal
antibodies for 2 h. After antibody incubation, HRP was activated with equipped with heat and CO incubation, and NIS Elements software
2
Supersignal West Dura Extended Duration Substrate (34075, Thermo (64 bit, v.5.30.03). Images were collected with either a ×40/1.3 NA Plan
Fisher Scientific) and visualized with a chemiluminscent detection Fluor or 60× 1.3 NA Plan Apo oil objective and 561 nm laser excitation,
system using Amersham Imager 600 (GE Healthcare Life Sciences). and acquired with 1,024 × 1,024 with 0.1 μm px−1 resolution.
The blots were then processed and analysed using Image J. Primary mtDNA imaging was performed using control (sgNTC) and
antibodies and dilutions were as follows: anti-VDAC2 (1:1,000, PA5- VDAC2-deficient B16-OVA cells with or without 10 ng ml−1 IFNγ plus
28106, Invitrogen), anti-BCL-2 (1:1,000, sc-7382, Santa Cruz), anti-MCL-1 40 μM pan-caspase inhibitor Q-VD-OPh treatment for 0 to 24 h as indi-
(1:1,000, ab32087, Abcam), anti-GSDME (1:1,000, ab215191, Abcam), cated in figures. All of the cells were cultured in chambered coverslips
anti-Flag (1:5,000, F1804, Sigma-Aldrich), anti-BIM (1:1,000, B7929, (80426, Ibidi), fixed with 2% paraformaldehyde for 10 min at room
Sigma-Aldrich); anti-Cas9 (1:5,000, 14697), anti-β-actin (1:5,000, temperature, and then treated with 0.1% Triton-100 for permeabiliza-
4970), anti-p-STAT1Y701 (1:1,000, 9167), anti-STAT1 (1:1,000, 14994), tion. Cells were blocked with PBS containing 1% bovine serum albumin
anti-caspase-3 (1:1,000, 9662), anti-cleaved caspase-3 (1:1,000, 9661), and 5% normal goat serum before addition of anti-dsDNA (1 μg ml−1;
anti-caspase-7 (1:1,000, 9492), anti-cleaved caspase-7 (1:1,000, 9491), MAB030, Millipore-Sigma), anti-TOMM20 (1 μg ml−1; 186735, Abcam) or
anti-caspase-9 (1:1,000, 9504), anti-APAF-1 (1:1,000, 8969), anti-cGAS anti-HA (1 μg ml−1; 2367, Cell Signaling Technology) antibodies, followed
(1:1,000, 31659), anti-STING (1:1,000, 13647), anti-p-STINGS365 for by detection with donkey anti-mouse (1:500, A32773, Thermo Fisher
mouse cells (1:1,000, 72971), anti-p-STINGS366 for human cells (1:1,000, Scientific) and donkey anti-rabbit (1:500, A32795, Thermo Fisher Scien-
19781), anti-TBK1 (1:1,000, 38066), anti-p-TBK1S172 (1:1,000, 5483), tific) secondary antibodies. Images were acquired using the A1RHD25
anti-IRF3 (1:1,000, 4302), anti-p-IRF3S396 (1:1,000, 29047), anti-MAVS (Nikon Instruments) resonance scanning confocal microscope using a
(1:1,000, 4983), anti-BAK (1:1,000, 12105), anti-BAX (1:1,000, 2772), ×40/1.3 NA Plan Fluor oil objective, 1,024 × 1,024 and 0.1 μm px−1 resolu-
anti-BCL-xL (1:1,000, 2764), anti-BID for mouse cells (1:1,000, 2003), tion, 561 nm and 640 nm laser lines. Images were deconvolved using
anti-BID for human cells (1:1,000, 2002), anti-PUMA (1:1,000, 98672), NIS Elements (64 bit, v.5.30.03) and analysed using Imaris software
anti-HA (1:5,000, 3724), anti-SMAC (1:1,000; 15108), anti-cytochrome (Bitplane, v.9.5.1×64). For histology analyses, mouse tissues were fixed
c (1:1,000, 4280) and anti-TOMM20 (1:1,000, 42406) (all from Cell by 10% (v/v) neutral buffered formalin solution, embedded in paraffin,
Signaling Technology). Secondary antibodies and dilutions were as sectioned and stained with haematoxylin and eosin.
follows: HRP-conjugated anti-mouse IgG (1:3,000; W4021; Promega)
or HRP-conjugated anti-rabbit IgG (1:3,000, W4011, Promega). Densio- RNA isolation and gene expression profiling
metric quantification of phosphorylated protein levels was normal- Cells were lysed with Buffer RLT in the RNeasy Micro Kit (74004, Qia-
ized relative to the corresponding total protein, and densiometric gen), and total RNA was extracted according to the manufacturer’s
quantification of total protein expression was normalized relative instructions. Then, 1 μg total RNA was reverse transcribed using the
to the loading control β-actin or TOMM20 (specifically for Extended High-Capacity cDNA Reverse Transcription Kit (4368814, Applied Bio-
Data Fig. 7k). All densiometric quantifications depict the fold changes systems). Diluted cDNA was subjected to RT–qPCR reactions containing
compared with the relative control (set equal to 1.0) and are shown Power SYBR Green PCR Master Mix (4367659, Applied Biosystems) and
above the immunoblot image. gene-specific primers. The reactions were performed in a QuantStu-
dio7 Flex Real-Time PCR System (Applied Biosystems). Actb was used
MTT assay as the housekeeping control. A list of the primers is provided in Sup-
To assess tumour cell expansion in vitro, the MTT cell proliferation assay plementary Table 11.
was performed using a commercial kit (30-1010K, ATCC). In brief, 1,000
cells per well B16-OVA-Cas9-sgNTC or B16-OVA-Cas9-sgVdac2 cells were Microarray transcriptome analyses
plated onto the 96-well plate on day 0, and the cell number was detected For microarray analysis, to analyse the gene expression of tumour cells
every 24 h according to the manual. Absorbance was measured on the after treatment with OT-I cells, control or VDAC2-deficient B16-OVA
VERSAmax Tunable Microplate Reader (Molecular Devices). tumour cells were treated with OT-I cells for 24 h, and the remaining
tumour cells were sorted for RNA extraction (n = 4 replicates each
ELISA group). To compare the differently expressed genes in various groups
For in vivo IFNγ and IFNβ detection, B16-OVA tumour tissues (~200 mg) (control, VDAC2-deficient; BAK-deficient; VDAC2 and BAK co-deficient;
from tumour-bearing mice were homogenized in 500 μl ice-cold RIPA STING-deficient; VDAC2 and STING co-deficient; APAF-1-deficient;
buffer (89900, Thermo Fisher Scientific) containing protease and VDAC2 and APAF-1 co-deficient; BIM and BID co-deficient; or VDAC2,
phosphatase inhibitor cocktail using Bead Ruptor Elite device (OMNI). BIM and BID co-deficient) of B16-OVA tumour cells, tumour cells
The lysate was centrifuged at 13,000g for 10 min at 4 °C, and the super- were treated with or without IFNγ at 10 ng ml−1 for 24 h in vitro, and
natant was used for IFNγ and IFNβ enzyme-linked immunosorbent assay the adherent tumour cell fraction was collected for RNA extraction
(ELISA). For in vitro cultured cells, the culture medium was collected (3 or 4 replicates for each group). To analyse the gene expression of
