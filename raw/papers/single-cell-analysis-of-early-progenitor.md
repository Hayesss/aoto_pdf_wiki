---
source_path: /mnt/c/Users/Administrator/Zotero/storage/F2PYB5EM/Su 等 - 2018 - Single-cell analysis of early progenitor cells that build coronary arteries.pdf
ingested: 2026-04-23
sha256: 571bb423ad393751
---

Article
https://doi.org/10.1038/s41586-018-0288-7
Single-cell analysis of early progenitor
cells that build coronary arteries
tianying Su1,12, Geoff Stanley2,12, rahul Sinha3,12, Gaetano D’Amato1, Soumya Das1, Siyeon rhee1, Andrew H. chang1,
Aruna Poduri1, Brian raftrey1, thanh theresa Dinh4,5, Walter A. roper4,5, Guang li6, Kelsey e. Quinn7, Kathleen M. caron7,
Sean Wu3,6,8, lucile Miquerol9, eugene c. Butcher4,5, irving Weissman3, Stephen Quake10,11 & Kristy red-Horse1*
Arteries and veins are specified by antagonistic transcriptional programs. However, during development and regeneration,
new arteries can arise from pre-existing veins through a poorly understood process of cell fate conversion. Here, using
single-cell RNA sequencing and mouse genetics, we show that vein cells of the developing heart undergo an early cell
fate switch to create a pre-artery population that subsequently builds coronary arteries. Vein cells underwent a gradual
and simultaneous switch from venous to arterial fate before a subset of cells crossed a transcriptional threshold into
the pre-artery state. Before the onset of coronary blood flow, pre-artery cells appeared in the immature vessel plexus,
expressed mature artery markers, and decreased cell cycling. The vein-specifying transcription factor COUP-TF2 (also
known as NR2F2) prevented plexus cells from overcoming the pre-artery threshold by inducing cell cycle genes. Thus,
vein-derived coronary arteries are built by pre-artery cells that can differentiate independently of blood flow upon the
release of inhibition mediated by COUP-TF2 and cell cycle factors.
The ability of cells to switch fates and acquire new identities is critical activation of cell cycle genes, which ultimately inhibited artery devel-
for organogenesis and regeneration, but the mechanisms that underlie opment. Understanding this and other cell fate switches and inhibitory
cell fate conversions are poorly understood. The vasculature is a model signals will advance our knowledge of tissue development and could
for this process because it initially differentiates into arteries and veins improve regenerative medicine.
whose transcriptional networks antagonize each other (Notch signal-
ling maintains arteries while COUP-TF2 maintains veins1,2). However, Finding developmental transitions in scRNA-seq data
during development and regeneration, veins can become the source of We performed a two-step analysis that identified and clustered cell
new arteries3–6. The timing and requirements of vein-to-artery conver- subtypes by iterative robust principal component analysis (rPCA), and
sions are not known, but could inform artery regeneration. then subjected clusters to a pairwise discreteness test (Fig. 1b). First,
In mice, a portion of the coronary arteries of the heart develop from cell subtype clusters were manually defined on the basis of unique
a vein called the sinus venosus (SV; Fig. 1a). During embryogenesis, gene expression patterns and cell separation in multiple iterations of
endothelial cell-lined angiogenic sprouts migrate from the SV to fill the rPCA12 (Fig. 1b). rPCA was better than classical PCA at separating
heart with an immature coronary vessel plexus4. This plexus unites with small subpopulations of cells13 (Extended Data Fig. 1a). We also
plexus vessels from the endocardium4,7,8, and, together, they remodel replaced default principal component scores with a sum of the top 60
into arteries, capillaries and veins. The plexus lacks blood flow until it genes score because it was less correlated with technical artefact and
attaches to the aorta, and arterial morphogenesis requires this event, better correlated with cluster-specific genes (Extended Data Fig. 1b, c).
suggesting that blood flow initiates artery development8–11. However, it Cell cycle heterogeneity was also removed (Extended Data Fig. 1d), and
has been difficult to delineate cell fate changes during coronary angio- plots were inspected to confirm the absence of doublets (Extended Data
genesis owing to the limited number of molecular markers and bulk Fig. 1e). This process resulted in cell clusters that correlate well with
transcriptional analyses of heterogeneous populations. genes that define cell identity, and not with cell cycle heterogeneity or
Single-cell RNA sequencing (scRNA-seq) can overcome this lim- technical artefact (Extended Data Fig. 1c, d).
itation by producing single-cell-resolution maps of developmental Second, we developed the pairwise discreteness test to determine
transitions. Here, we developed a statistical test that categorizes sub- whether clusters were discrete or continuous (that is, connected by
populations within scRNA-seq data sets as continuous or discrete to intermediate or transitioning cells). This statistical test projects pairs
identify candidate developmental transitions. Computational or in of subpopulations onto a linear axis of cell identity, measures the size
vivo analysis of the SV-to-coronary transition revealed that SV cells of the gap between the populations, and estimates the number of inter-
of the mouse heart undergo a gradual conversion from vein to artery mediate cells (Fig. 1b and Extended Data Fig. 1f). It also determines the
before a subset crosses a threshold to differentiate into pre-artery strength of continuity (Extended Data Fig. 1h), and could be confirmed
cells. Pre-artery cells differentiated before blood flow from the SV using simulated data (Extended Data Fig. 1h). Combining the results
and endocardium and produced a large portion of coronary arteries. created a relationship graph (Fig. 1b), which could identify candidate
COUP-TF2 blocked progression to the pre-artery state through developmental transitions. Then, cell fate changes could be analysed
1Department of Biology, Stanford University, Stanford, CA, USA. 2Program in Biophysics, Stanford University, Stanford, CA, USA. 3Institute for Stem Cell Biology and Regenerative Medicine,
Stanford University School of Medicine, Stanford, CA, USA. 4Veterans Affairs Palo Alto Health Care System and The Palo Alto Veterans Institute for Research, Palo Alto, CA, USA. 5Department of
Pathology, Stanford University, Stanford, CA, USA. 6Cardiovascular Institute, Stanford University School of Medicine, Stanford, CA, USA. 7Department of Cell Biology and Physiology, University
of North Carolina at Chapel Hill, Chapel Hill, NC, USA. 8Division of Cardiovascular Medicine, Department of Medicine, Stanford University School of Medicine, Stanford, CA, USA. 9Aix-Marseille
Université, CNRS UMR 7288, IBDM, Marseille, France. 10Department of Bioengineering, Stanford University, Stanford, CA, USA. 11Chan Zuckerberg Biohub, San Francisco, CA, USA. 12These authors
contributed equally: Tianying Su, Geoff Stanley, Rahul Sinha. *e-mail: kredhors@stanford.edu
356 | NAtUre | VOl 559 | 19 JUlY 2018
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
a b
c 2. Number of 1. Gap size intermediates
fint = 0.04
x Discrete
or Cell identity score Cell identity score
fint = 0.74 x
continuous
Cell identity score Cell identity score
d e Venous markers Arterial markers
SVc Arterial SVc Arterial
V S w V f Coup-t V f2 enous Apj Apln Coronary Dll4 Cx40 Arterial Cxcr4 Coup Ti - A e t - f p 2 2 j 2 3 U S C H n o c x e x 5 3 y 1 b 7 1 7 2.0
Dab2 Efnb2 1.5
Ep N h r B p 4 2 1 No V M t e D c s g h x l f l 1 4 4 c 1.0
Cxcr4
Alk1 Jag2 0.5
Tox2
Hes1 Cx40 0 PC3
in high resolution by observing gene expression changes across con- expressed in angiogenic vessels, and are not artery-specific18,19. The
tinuous populations (Fig. 1b). scRNA-seq analysis revealed that, within the Dll4+ domain, some
We used this pipeline to analyse 843 ApjCreER lineage-labelled (Cre cells had initiated a distinctive transcriptional program, shifting
expressed in SV) cardiac endothelial cells from hearts removed from away in the rPCA plot (Fig. 1d). Cells within this subset specifically
mouse embryos at embryonic day 12.5 (E12.5) (Extended Data Fig. 1g). expressed mature artery-specific genes, including Cx40 (also known
Our data set contained endothelial cells from the SV, SV-derived coro- as Gja5) (Fig. 1d). Analysis of multiple arterial and venous genes in
nary vessels, venous valves, valve mesenchyme, and some ventricular single cells or as averages within clusters (defined in Extended Data
endocardial cells (Extended Data Fig. 1i, j). Clustering and the pair- Fig. 2g) revealed that many arterial genes were either specific to or
wise discreteness test revealed a continuum between coronary vessel significantly increased in the Cx40+ cluster (Fig. 1d and Extended Data
subtypes, the SV, venous valves, ventricular endocardium, and mesen- Fig. 3a, b). Multiple venous genes were either completely depleted or
chyme (Pdgfra+, Pecam1low/−) (Fig. 1c and Extended Data Fig. 1i–k). significantly downregulated (Fig. 1d and Extended Data Fig. 3c, d).
These associations are consistent with anatomical relationships (SV is Comparison of expression between the SVc and arterial populations
adjacent to venous valves and endocardium) and previous lineage trac- revealed that SV-derived cells showed an extensive switch towards arte-
ing experiments (SV transitions into coronary vessels and endocardium rial fate (Fig. 1e).
transitions into mesenchyme)8,11,14–17. Thus, our pipeline can identify We next compared E12.5 arterial cells with adult coronary vessel
subpopulations and recapitulate known developmental transitions and cells. Each embryonic cell was matched to the adult cell to which it
anatomical relationships. was most similar within the artery–capillary–vein continuum formed
by adult coronary vessels20 (Extended Data Fig. 3e–g). E12.5 artery
Pre-artery cells differentiate before blood flow cells were most similar to adult arterial cells, whereas coronary vessel
We analysed the developmental transition linking SV coronary pro- plexus cells were most similar to adult capillaries and veins (Extended
genitors (SVc) and coronary vessels (Fig. 1c, dotted line). Only the SVc Data Fig. 3h). We also found that E12.5 and adult artery populations
was included because clustering indicated that the SV had two domains were enriched for nearly the same artery markers (Supplementary
(Fig. 1c), and this was confirmed using immunofluorescence and in situ Table 1). The exception was Notch1 (enriched only in adults), possibly
hybridization (Extended Data Fig. 2a–f). The SVc was anatomically because blood flow upregulates Notch121, and E12.5 is before the onset
and transcriptionally continuous with coronary vessels, whereas the of coronary perfusion. Thus, a subpopulation of plexus cells undergo
SVv (SV valve proximal) was continuous with venous valves (Fig. 1c, a transcriptional shift to resemble mature arteries before the presence
Extended Data Fig. 2d, f). Therefore, rPCA of the SVc and coronary of arterial vessels or blood flow, prompting us to term them pre-artery
vessels was performed to study the SVc–coronary vessel continuum cells.
(Fig. 1d). The scRNA-seq also identified new arterial genes (Extended Data
Unexpectedly, the SVc–coronary vessel continuum identified cells Fig. 4a). Slc45a4 marked pre-artery cells at early stages and was later
that were transcriptionally distinct and expressed genetic markers of specific to mature embryonic arteries (Extended Data Fig. 4b, c). It was
mature arterial cells (Fig. 1d). We previously reported4 that plexus also enriched in adult coronary artery cells (Extended Data Fig. 4a).
cells express arterial genes such as Dll4 and Efnb2, but these are also We found other genes to be enriched in pre-artery cells (Extended
2CP
Dorsal view
At
SV (vein)
Ven Endo
Immature vessel plexus
Blood Re-specificationflow?
Veins Capillary Artery
SVc
CV
Artery
5.21E
?
5.41E
Clustering Cluster visualization
Define
All cells Iteration 1 ... Iteration n clusters
Gene expression Subpopulations
Gene ... ? expression = High ?
?
mod. PC scores
?
Low ... = ?
Pairwise discreteness test
Venous Mesenchyme 1 Developmental Relationship valve 1 Mesenchyme 2 cont t in ra u n o s u it s i o r n el s a t f i r o o n m ships graph Result:
SVv SV V v e a n lv o e u 2 s Clusters Gene expression
Endocardium dynamics
SVc
CV2 Coronary
CV1 vessel
subtypes
Artery
A-V genes not changed:
Nrp2 Bmx Epas1
Flt4 Jag1 Hes1
Emcn Hey2 Vegfa 1 2 3 4 Nr3c2 Nkx2-3Prdm16 Lefty1 Aff3 Notch1
log10CPM
Fig. 1 | Identifying pre-artery cells using scRNA-seq. a, b, Schematics of ApjCreER-traced endothelial subtypes. d, Pre-artery cells extend from the
coronary artery development (a) and computational pipeline plexus in the SVc–coronary vessel continuum. Gene expression in brown.
(fint, estimated fraction of cells that are intermediate; x, width of the n = 415 cells. e, Heat map of venous and arterial genes. At, atria; endo,
largest gap in scores between populations) (b). c, Relationship graph for endocardium; ven, ventricle.
19 JUlY 2018 | VOl 559 | NAtUre | 357
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
a
E11.5 E12.5 E13.5
d
E11.5 tamoxifen
g e E15.5 f P8
Data Fig. 4d). Of these, Mecom and Igfbp3 marked arteries in adults at E11.5; only the most distal tips were unlabelled (Fig. 2f and Extended
(Extended Data Fig. 4d). Data Fig. 6i). Thus, pre-artery cells build a large portion of mature
coronary arteries.
Location, origins, and fate of pre-artery cells Pre-artery cells first appeared before blood flow, but they were
In late embryonic stages (E17.5), CX40 is specific to mature arteries abundant in the plexus through E14.5 (Extended Data Fig. 7c), sug-
(Extended Data Fig. 5a). By contrast, whole-mount immunostaining gesting that specification could continue after coronary perfusion.
at early stages revealed that a small population of CX40+ cells first To investigate this possibility, we used Cre lines that specifically label
appeared at E12.5. These cells were interspersed within the intramy- either coronary vessel plexus (ApjCreER) or pre-artery (Cx40CreER)
ocardial plexus and expanded by E13.5 (Fig. 2a, b). Localization of cells (Extended Data Fig. 7a) and induced labelling at various times
additional pre-artery genes confirmed this result (Extended Data (Extended Data Fig. 7b). Labelling of the coronary vessel plexus at E12.5
Fig. 5b). The absence of CX40+ cells in the SV and their presence in or E13.5 lineage-traced a small number of pre-artery cells (Extended
the coronary vessel plexus agreed with clustering and pairwise analysis Data Fig. 7d, e). However, when the coronary vessel plexus was labelled
showing that pre-artery cells were continuous only with the coronary at E14.5, there was no tracing into artery main branches and very little
vessel plexus (Fig. 1c). Defining clusters using Seurat showed similar in the tips (Extended Data Fig. 7f, h). Conversely, labelling at E14.5 with
results (Extended Data Fig. 6a), although clusters were not as precise Cx40CreER lineage-traced most left and right coronary artery branches
and were associated with cell cycle genes (Extended Data Fig. 6b, c). (Extended Data Fig. 7g, h). Finally, inducing labelling with Cx40CreER
Thus, coronary angiogenesis involves the specification of single arterial at E16.5 resulted in few capillary cells being labelled at embryonic and
endothelial cells within the intramyocardial plexus (Fig. 1b). postnatal stages (Extended Data Figs. 6j, 7i). These data indicate that
Although our scRNA-seq investigated only SV-derived vessels, lin- pre-artery specification occurs in the coronary plexus between E12.5
eage tracing revealed that coronary arteries are derived from both the and E14.5, creating a progenitor pool that forms virtually all of the
SV and the endocardium22 (Extended Data Fig. 6d). Single CX40+ embryonic left and right coronary artery branches.
cells were detected in the plexus from both sources (Fig. 2c), indicating We next investigated whether the artery tips that did not form from
that pre-artery specification occurs during both SV and endocardium pre-artery cells (Fig. 2f) arose from pre-existing arteries or through
angiogenesis. capillary differentiation. Induction of ApjCreER and Cx40CreER
Cx40CreER RosatdTomato embryos were used for lineage tracing of labelling at P2 revealed that artery tips at P6 were composed of
pre-artery cells (tamoxifen, E11.5; Extended Data Fig. 6e, f). CX40+ ApjCreER-lineage cells but depleted of Cx40CreER-labelled cells
pre-artery cells were later found in arteries, but not veins (Fig. 2d, e). (Extended Data Fig. 6k). Thus, postnatal artery tips grow by capil-
A few capillaries were lineage-traced, indicating that pre-artery cells lary arterialization.
could revert to a capillary fate (Fig. 2d). Dosing at E10.5 ensured that The morphogenic changes that accompany coronary artery remodel-
our result was not due to persistent tamoxifen (Extended Data Fig. 6g), ling are seen after blood flow has been established, and are thought to be
and clonal level labelling confirmed the lineage data (Extended Data triggered by shear stress9,10. In E13.5 Isl1 mutant mice that have delayed
Fig. 6h). Notably, at postnatal day (P)8, the right and left coronary blood flow23, pre-artery cells had congregated in the region where the
artery branches were heavily lineage-labelled in hearts from mice dosed coronary artery would eventually form (Fig. 2g) and began to increase
04XC
VEGFR2 CX40
VE-cadherin CX40
noiger
dexoB
b CX40+ Venous
Myo SV E12.5 E13.5 E17.5
Myo
SV
CX40+ arterial ECs appear
within myocardial plexus
c
noiger
dexob
E11.5 SV
SV
Myo
SV
CV
SV-derived Endocardium-derived
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
wofl
doolb
on
–/+1lsI
ApjCreER lineage CX40Nfatc1Cre lineage CX40
Artery/capillary Vein Whole heart Proximal RCA branch
1 1 2
* myo
2
1 1 2
myo *
2
GRE
nirehdac-EV
egaenil
+04XC
egaenil
+04XC
egaenil
+04XC
AMSa
egaenil
+04XC
Myo Myo
Ventricle
Ventricle
120 100
80
60
40
20
0
Veins Capillary Arteries
Most distal LCA branch
h
egaenil
REerC04xC
)%(
sllec
dellebal
Contribution of pre-artery cells to mature coronary vessels
**** ***
80
60 40
20
0
retemaid
lesseV
)mμ(
CX40+ vessels thicken
prior to blood flow
** ****
CX40: – + – +
WT Isl1+/–
Fig. 2 | Pre-artery cells build coronary arteries. a, CX40 and P8 (f). Asterisks in f indicate non-lineage labelled tips. g, CX40+ cells
immunofluorescence in hearts to mark pre-artery cells (arrowheads). (arrowhead) in hearts that lack coronary blood flow. h, CX40+ vessels
b, Schematic of pre-artery cells during coronary development. c, CX40+ begin remodelling without blood flow. Wild-type, n = 7 hearts; Isl1+/−,
cells in SV- and endocardium-derived plexus. d, Cx40CreER lineage n = 6 hearts. d, h, Data shown as mean ± s.d. myo, myocardium. Scale
labelling (E11.5 induction). n = 7 hearts. e, f, Pre-artery lineage labelling bars: c, 50 μm; a, e, f, 100 μm. Unpaired two-tailed t test. **P ≤ 0.01;
in arteries (arrowheads) and a subset of capillaries (arrows) at E15.5 (e) ***P ≤ 0.001; ****P ≤ 0.0001.
358 | NAtUre | VOl 559 | 19 JUlY 2018
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
lumen size (Fig. 2h). Therefore, pre-artery cells within the plexus can and Apj (also known as Aplnr); Fig. 3b). Arterial gene expression
differentiate and initiate remodelling before cues from blood flow. showed two patterns: ‘early’ genes, expression of which progressively
increased in coronary vessel plexus and pre-artery cells (Fig. 3c and
Gradual cell fate conversion Extended Data Fig. 8a), and ‘late’ genes, expression of which was low in
To investigate the vein-to-artery conversion, single cells along the coronary vessel plexus, but increased sharply in pre-artery cells (Fig. 3d
SVc–coronary vessel plexus–pre-artery developmental transition were and Extended Data Fig. 8a). Notch ligands and receptors were early
projected onto a linear continuum (Fig. 3a, b). Gene expression was then genes, with the exception of Hey1, which increased sharply in pre-
visualized by LOESS regression (Fig. 3b–e, g and Extended Data Fig. 8a). artery cells (Fig. 3e and Extended Data Fig. 8a). These findings suggest
There was a progressive decrease in venous identity as cells exited the that the loss of venous identity is initially gradual with a progressive
SV and moved towards pre-artery (see Coup-tf2, EphB4 and Tie-2 (also increase in arterial identity, and that pre-artery specification occurs
known as Tek); Fig. 3b). A sharp decrease in venous genes was seen after a threshold of venous loss and arterial gain has been achieved
in cells that had undergone full pre-artery specification (see Coup-tf2 (Fig. 3f).
a b e
VE-cadherin
COUP-TF2OE
COUP-TF2OE (ApjCreER)
A
f
A A
GFP/ERG overlap GFP (ApjCreER)
A A
h
c g
yretra-erp
erofeb
noitcudni
ciasoM
yretra-erp
retfa
noitcudni
ciasoM
yretra-erp
erofeb
lailehtodne-naP
Veins Capillary Artery
REerCjpA
lortnoC
REerC04xC
EO2FTpuoC
PFG
,REerCjpA
EO2FTpuoC
VE-cadherin
COUP-TF2OE
Cap
**** ****
Cap VE-cadherin
GFP ERG
* NS
VE-cadherin CXCR4 COUP-TF2OE COUP-TF2OE
Cap Cap ** **
A A
lortnoC
REerC5hdC
REerC5hdC
EO2FTpuoC
Blood
flow?
lessev
ni
EO2FT-PUOC
lessev
ni
PFG
EO2FT-PUOC
fo
.oN
)oitar(
sepytbus
)oitar(
sepytbus
aera
rep
sllec
50
40
30
20
10
0
SV
Endo COUP-TF2OE (Cx40CreER)
Vessel plexus COUP-TF2
ReversionPre-artery
yranoroc
fo
htdiW
)mμ(
yretra
1.5
1.0 Pan-EC expression of Coup-tf2OE
before pre-artery specification
0.5 can prevent artery development
****
0.0
Vein CapillaryArtery
1.5
ControlCdh5CreER,
1.0
Coup-TF2OE
0.5
0.0
Vein CapillaryArtery
20
15
10
5
0
50
40 30
20
10
0
Vein Capillary Artery
yranoroc
fo
htdiW
)mμ(
yretra
a b c d e g
SVc–CV plexus–pre-artery axis Venous genes Arterial genes: Arterial genes: Notch pathway Cell cycle
early late genes
SVc Coup-tf2 EfnB2 Cxcr4 Notch4 Myc
3 3 3 3
2 2 2 2
CV plexus 1 1 1 1
0 0 0 0
Pre-artery EphB4 Unc5b Cxcr7 Dll4 Mki67
3 3 3 3
2 2 2 2
1 1 1 1
0 0 0 0
Tie-2 Igfbp3 Cx37 Jag2 Cdk1
f 3 3 3 3
Model for vein-to-artery fate change 1 2 1 2 1 2 1 2
Gene expression 0 0 0 0
Apj Msx1 Cx40 Hey1 Odc1
3 3 3 3
Venous 2 2 2 2
1 1 1 1
Arterial 0 0 0 0
Threshold for full
SVc CV Art SVc CV Art SVc CV Art SVc CV Art SVc CV Art
vein-to-artery conversion
d
Pan-EC expression of Coup-tf2OE after pre-artery specification
does not prevent artery development *
Control Cdh5CreER,
Coup-TF2OE
Fig. 4 | COUP-TF2 specifically blocks pre-artery specification. g, Coup-tf2OE induction in all endothelial cells after pre-artery
a, b, E15.5 hearts induced to express Coup-tf2OE or Gfp before pre-artery specification. Control, n = 16 hearts; Coup-tf2OE, n = 9 hearts.
specification. c, d, E15.5 hearts induced to express Coup-tf2OE after h, Schematic displaying differentiation step blocked by COUP-TF2. A,
pre-artery specification. b, Coup-tf2OE, n = 11 hearts; Gfp, n = 11 hearts. artery; Cap, capillary; Endo, endocardium. Scale bars, 100 μm. Data shown
d, n = 6 hearts. e, f, Coup-tf2OE induction in all endothelial cells before as mean ± s.d. P value: unpaired two-tailed t-test. NS, P > 0.05; *P ≤ 0.05;
pre-artery specification. Control, n = 12 hearts; Coup-tf2OE, n = 20 hearts. **P ≤ 0.01; ****P ≤ 0.0001.
slevel
ANRm
evitaleR
)MPC01gol(
3
2
1
0
3
2
1
0
3
2 1
0
3
2
1
0
Fig. 3 | The venous-to-arterial fate change is gradual and culminates lines, SVc expression levels; red shading, pre-artery cells. f, Model based
in an expression threshold. a, Coronary differentiation pathway (dashed on known marker gene patterns. g, Cell cycle genes decreased in pre-artery
arrow). b–e, Gene expression along the differentiation pathway. Dotted cells. Art, pre-artery; CV, coronary vessel.
19 JUlY 2018 | VOl 559 | NAtUre | 359
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
Venous/plexus Venous/plexus Plexus/artery Artery: early Artery: late Artery: late Notch pathway
Coup-tf2 Apj Dll4 Igfbp3 Cxcr4 Cx40 Hey1
To understand the pre-artery threshold, we performed pathway analysis (Extended Data Fig. 9f–h), although they caused a mild increase in ves-
using gene set enrichment analysis (GSEA)24. Most pathways that were sel density at E13.5 (Extended Data Fig. 9g). Thus, forced COUP-TF2
enriched in plexus over arterial cells were associated with cell cycling expression before pre-artery specification blocks cells from contribut-
(Extended Data Fig. 8b). Arterial cells are thought to leave the cell cycle ing to coronary arteries, suggesting a failure to acquire pre-artery fate.
in response to blood flow25–27; however, pre-artery cells collected before Induction of Coup-tf2OE after pre-artery specification with Cx40CreER
blood flow displayed a decrease in cell cycle genes (Fig. 3g, Extended (tamoxifen at E11.5 or E12.5) resulted in numerous Coup-tf2OE
Data Fig. 8c, and Supplementary Table 2). In vivo, pre-artery cells were cells within the artery (Fig. 4c, d, and Extended Data Fig. 9i) that
less proliferative than the surrounding plexus (Extended Data Fig. 8d). expressed the arterial markers CXCR4 and JAG1 (Fig. 4c and Extended
Thus, decreased proliferation in arteries is acquired during pre-artery Data Fig. 9i). Therefore, Coup-tf2OE inhibits arterial fate only before
specification, and not specifically in response to blood flow. pre-artery specification. Pre-artery specification was then blocked
throughout the entire coronary plexus by inducing widespread Coup-
COUP-TF2 blocks artery formation tf2OE recombination using Cdh5CreER (tamoxifen at E11.5 and E13.5).
To investigate whether pre-artery specification was necessary for This resulted in small or completely absent coronary arteries (Fig. 4e, f).
artery formation, we required a tool to block this process. We tested By contrast, induction of Cdh5CreER-Coup-tf2OE after pre-artery
COUP-TF2 because it induces venous fate and antagonizes arterial specification, but before arterial morphogenesis (tamoxifen at E13.5
fate1,28 and was sharply decreased in pre-artery cells (Figs. 1d, 3b). and E15.5), resulted in relatively normal artery development, confirm-
ApjCreER mice were crossed to mice that constitutively express ing that the later steps in artery formation are not greatly inhibited
Coup-tf2 after Cre recombination29 (Extended Data Fig. 9a) and preg- by COUP-TF2 (Fig. 4g). Thus, pre-artery specification is required for
nant dams were treated with tamoxifen to induce overexpression of artery development, and this is the specific differentiation step that is
Coup-tf2 (Coup-tf2OE) before pre-artery specification. Cre recombina- antagonized by COUP-TF2 (Fig. 4h).
tion of the Coup-tf2OE allele was low, making this experiment a mosaic
analysis in which Coup-tf OE cells were followed within wild-type tissue COUP-TF2 inhibits pre-artery via cell cycle genes
(Extended Data Fig. 9b, c). We next used scRNA-seq to compare control and Coup-tf2OE cells.
Coup-tf2OE cells were present in capillaries and veins, but not arteries E14.5 coronary endothelial cells (Extended Data Fig. 10a) were
(Fig. 4a, b, top and Extended Data Fig. 9d). By contrast, control GFP+ analysed as described for E12.5. Coup-tf2OE cells were identified by the
cells were found in arteries, capillaries, and veins (Fig. 4a, b, bottom). expression of the transgene’s FLAG-myc tag (Extended Data Fig. 10b, c).
Coup-tf2OE cells could survive in arteries when VE-cadherin-CreER rPCA revealed a transcriptional continuum linking venous, coronary
induced recombination after arteries had formed (Extended Data vessel plexus, and arterial cells (Fig. 5a, b). Vein cells in this data set
Fig. 9e). Coup-tf2OE cells could also migrate normally onto the heart expressed Coup-tf2 and Apj and lacked Dll4 and Notch4, as has been
lortnoC
EO2ft-puoC
a b Early vein
CV plexus
Art
PC2.pos
c Control Coup-tf2OE
Missing cells
in Coup-tf2OE
e Control log10CPM
f g
d Venous genes Arterial genes
EphB4 Dll4 h
Coup-tf2OE
AApplnjr Cxcr4
Vein CV Art Vein CV Art
gen.2CP
0.8
0
0 0.8
PC2.pos
(superimposed)
gen.2CP
)desopmirepus(
0.8
0
0 0.8
Density:
3 3 2 2 1 1 0 0
3 3
2 2
1 1 0 0
)MPC gol(
slevel
ANRm
evitaleR
01
High
Low
erocs S/1G 6 4
2
0
G0 G2/M score
gnillebal fo
esaercni
dloF
5.11E revo
segatnecrep
COUP-TF2-OE cells
expand more over time
*** 40 30
20
10
Contro C l oup-tf2OE 0
sCE evitsop
UdE
%
Coup-tf2 heterozygous
deletion decreases S-phase occupancy
* ** 50 40
30 20
10
0 Con C tr o o u l p-tf2fl/+ Con C tr o o u l p-tf2fl/+ E12.5 E14.5
yranoroc
fo
htdiW
)mμ(
yretra
0.6
0.4
0.2
0.0 0.2 0.4 0.6 0.8
PC2.pos
Cell cycle inhibition rescues
Coup-tf2OE arterial phenotype NS
Control Cdh5CreER, Dinac + iclib Coup- + TF2OE Dinaciclib
gen.2CP
0.6
0.4
0.2
0.0 0.2 0.4 0.6 0.8
PC2.pos
gen.2CP
1 23 4
Fig. 5 | COUP-TF2 inhibits artery specification through cell cycle genes. plexus cells in the indicated cell cycle phases. f, Fold increase in control
a, rPCA plots from E14.5 hearts (wild-type, n = 347 cells; Coup-tf2OE, GFP or COUP-TF2OE cells between E11.5 and E14.5. Control, n = 8 hearts;
n = 321 cells). Red brackets, artery cells devoid of Coup-tf2 and Apj. Coup-tf2OE, n = 5 hearts. g, EdU incorporation in coronary endothelial
b, Coronary continuum based on gene expression patterns in a. n = 347 cells from Cdh5CreER Coup-tf2fl/+ hearts. E12.5: control, n = 4 hearts;
cells. c, Coup-tf2OE cells do not populate the Coup-tf2−Apj− artery Coup-tf2fl/+, n = 2 hearts. E14.5: control, n = 3 hearts; Coup-tf2fl/+, n = 3
population. Wild-type, n = 347 cells; Coup-tf2OE, n = 321 cells. hearts. h, Cell cycle inhibition reverses the ability of Coup-tf2OE to block
d, Progression towards artery is not generally affected by Coup-tf2OE. artery formation (compare to Fig. 4f). Control, n = 6 hearts; Coup-tf2OE,
Wild-type, grey lines; Coup-tf2OE, yellow lines. Red-shaded region, n = 6 hearts. P = 0.4167. Data shown as mean ± s.d. Unpaired two-tailed
pre-artery cells. e, Heat map showing the distribution of coronary vessel t test. *P ≤ 0.05; **P ≤ 0.01; ***P ≤ 0.001.
360 | NAtUre | VOl 559 | 19 JUlY 2018
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
described for coronary veins4,30. Superimposing transgenic cells onto Online content
the control continuum showed that Coup-tf2OE cells were excluded only Any Methods, including any statements of data availability and Nature Research
from the arterial population (Fig. 5c). Venous and arterial genes along reporting summaries, along with any additional references and Source Data files,
the continuum were not generally inhibited by Coup-tf2OE (Fig. 5a, d are available in the online version of the paper at https://doi.org/10.1038/s41586-
018-0288-7.
and Extended Data Fig. 10d). The defect instead was in the number
of fully pre-artery or arterial cells, as shown with genes such as Cxcr4
Received: 31 July 2017; Accepted: 29 May 2018;
and Cx40 (Fig. 5a).
Published online 4 July 2018.
Analysis of differential gene expression did not reveal marked
changes in the expression of Notch genes, despite the prevailing theory
1. Chen, X., Qin, J., Cheng, C.-M., Tsai, M.-J. & Tsai, S. Y. COUP-TFII is a major
that COUP-TF2 functions by antagonizing this pathway (Fig. 5a, d,
regulator of cell cycle and Notch signaling pathways. Mol. Endocrinol. 26,
Extended Data Fig. 10d and Supplementary Table 3). Furthermore, 1268–1277 (2012).
overexpression of Notch signalling did not rescue the Coup-tf2OE 2. Fish, J. E. & Wythe, J. D. The molecular regulation of arteriovenous specification
and maintenance. Dev. Dyn. 244, 391–409 (2015).
phenotype (Extended Data Fig. 9j, k). It is possible that expression levels
3. Isogai, S., Lawson, N. D., Torrealday, S., Horiguchi, M. & Weinstein, B. M.
were not high enough to overcome COUP-TF2. Instead, a prominent Angiogenic network formation in the developing vertebrate trunk. Development
feature of Coup-tf2OE cells was an increase in cell cycle gene expression 130, 5281–5290 (2003).
4. Red-Horse, K., Ueno, H., Weissman, I. L. & Krasnow, M. A. Coronary arteries form
(Supplementary Table 3). Plotting coronary vessel plexus and vein cells
by developmental reprogramming of venous cells. Nature 464, 549–553
according to G1/S/G2/M cell cycle staging revealed that the Coup-tf2OE (2010).
population contained more cells with a cycling profile when compared 5. Xu, C. et al. Arteries are formed by vein-derived endothelial tip cells. Nat.
to controls (Fig. 5e). Commun. 5, 5758 (2014).
6. Kametani, Y., Chi, N. C., Stainier, D. Y. R. & Takada, S. Notch signaling regulates
COUP-TF2 also influenced coronary vessel proliferation. The relative venous arterialization during zebrafish fin regeneration. Genes Cells 20,
increase in Coup-tf2OE cells over developmental time was greater than for 427–438 (2015).
controls (Fig. 5f). Endothelial deletion of one copy of Coup-tf2 resulted 7. Wu, B. et al. Endocardial cells form the coronary arteries by angiogenesis
through myocardial-endocardial VEGF signaling. Cell 151, 1083–1096 (2012).
in decreased proliferation and expansion of coronary vessels (Fig. 5g and
8. Chen, H. I. et al. The sinus venosus contributes to coronary vasculature through
Extended Data Fig. 10e). As pre-artery specification was associated with VEGFC-stimulated angiogenesis. Development 141, 4500–4512 (2014).
decreased proliferation, these data suggest that COUP-TF2 may block 9. Volz, K. S. et al. Pericytes are progenitors for coronary artery smooth muscle.
eLife 4, e10036 (2015).
arterial specification by activating cell cycle genes.
10. Ivins, S. et al. The CXCL12/CXCR4 axis plays a critical role in coronary artery
Next, we sought evidence that cell cycle exit enhances arterial spec- development. Dev. Cell 33, 455–468 (2015).
ification, and that COUP-TF2 antagonizes this activity. First, cultured 11. Sharma, B., Chang, A. & Red-Horse, K. Coronary artery development: progenitor
cells and differentiation pathways. Annu. Rev. Physiol. 79, 1–19 (2017).
SV sprouts were treated with a cyclin-dependent kinase (CDK) inhibi-
12. Todorov, V. & Filzmoser, P. An object-oriented framework for robust multivariate
tor, which significantly increased artery differentiation (Extended Data analysis. J. Stat. Softw. 32, 1–47 (2009).
Fig. 9l and m). Second, a CDK inhibitor was administered to Cdh5CreER 13. Gokce, O. et al. Cellular taxonomy of the mouse striatum as revealed by
Coup-tf2OE mice dosed with tamoxifen early to assess whether the single-cell RNA-seq. Cell Reports 16, 1126–1137 (2016).
14. Rivera-Feliciano, J. et al. Development of heart valves requires Gata4 expression
phenotype of small and absent coronary arteries could be alleviated in endothelial-derived cells. Development 133, 3607–3618 (2006).
(see phenotype in Fig. 4f). Inhibition of CDKs resulted in no significant 15. Zhang, H. et al. Endocardium minimally contributes to coronary endothelium in
difference between control and transgenic animals (Fig. 5h), demon- the embryonic ventricular free walls. Circ. Res. 118, 1880–1893 (2016).
16. Chen, Q. et al. Endothelial cells are progenitors of cardiac pericytes and vascular
strating that the ability of COUP-TF2 to inhibit artery formation had smooth muscle cells. Nat. Commun. 7, 12422 (2016).
been reversed. 17. Lin, C.-J., Lin, C.-Y., Chen, C.-H., Zhou, B. & Chang, C.-P. Partitioning the heart:
mechanisms of cardiac septation and valve development. Development 139,
3277–3299 (2012).
Discussion
18. Adams, R. H. et al. Roles of ephrinB ligands and EphB receptors in
scRNA-seq can reveal developmental transitions at a much higher cardiovascular development: demarcation of arterial/venous domains, vascular
resolution than was previously possible31–33. By combining scRNA-seq morphogenesis, and sprouting angiogenesis. Genes Dev. 13, 295–306 (1999).
19. Sacilotto, N. et al. MEF2 transcription factors are key regulators of sprouting
with in vivo localization and genetic manipulations, we show that a
angiogenesis. Genes Dev. 30, 2297–2309 (2016).
subset of endothelial cells within the immature coronary plexus crosses 20. The Tabula Muris Consortium, Quake, S. R., Wyss-Coray, T. & Darmanis, S.
a transcriptional threshold to become pre-artery cells. Pre-artery spec- Single-cell transcriptomic characterization of 20 organs and tissues from
individual mice creates a Tabula Muris. Preprint at https://www.biorxiv.org/
ification is a critical step because blocking this process inhibited artery
content/early/2018/03/29/237446 (2018).
formation. Prior to pre-artery specification, SV-derived endothelial 21. Mack, J. J. et al. NOTCH1 is a mechanosensor in adult arteries. Nat. Commun. 8,
cells gradually decreased expression of venous genes while gradually 1620 (2017).
22. Tian, X. et al. Vessel formation. De novo formation of a distinct coronary
increasing expression of arterial genes. These data suggest that fate
vascular population in neonatal heart. Science 345, 90–94 (2014).
switching during angiogenesis occurs in a progressive manner, and 23. Chen, H. I. et al. VEGF-C and aortic cardiomyocytes guide coronary artery stem
that individual plexus cells that reach a threshold towards full arterial development. J. Clin. Invest. 124, 4899–4914 (2014).
differentiation form the mature coronary arteries. 24. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based
approach for interpreting genome-wide expression profiles. Proc. Natl Acad. Sci.
Although COUP-TF2 is considered a master regulator of veins, USA 102, 15545–15550 (2005).
precisely how it brings about venous fate and suppresses artery fate is 25. Akimoto, S., Mitsumata, M., Sasaguri, T. & Yoshida, Y. Laminar shear stress
still under investigation2. Single-cell analysis revealed that COUP-TF2 inhibits vascular endothelial cell proliferation by inducing cyclin-dependent
kinase inhibitor p21(Sdi1/Cip1/Waf1). Circ. Res. 86, 185–190 (2000).
did not push cells towards a venous fate or markedly suppress arterial
26. Lin, K. et al. Molecular mechanism of endothelial growth arrest by laminar
genes. Instead, COUP-TF2 specifically blocked pre-artery specification, shear stress. Proc. Natl Acad. Sci. USA 97, 9385–9389 (2000).
because Coup-tf2OE induction before the pre-artery stage prevented 27. Fang, J. S. et al. Shear-induced Notch–Cx37–p27 axis arrests endothelial cell
cycle to enable arterial specification. Nat. Commun. 8, 2149 (2017).
mature artery development, whereas induction afterwards had little
28. You, L.-R. et al. Suppression of Notch signalling by the COUP-TFII transcription
effect. Our data indicate that COUP-TF2 suppresses pre-artery speci- factor regulates vein identity. Nature 435, 98–104 (2005).
fication by activating cell cycle genes. Recently, retinal artery differen- 29. Qin, J. et al. COUP-TFII inhibits TGF-β-induced growth barrier to promote
prostate tumorigenesis. Nature 493, 236–240 (2013).
tiation has been shown to depend on cell cycle arrest triggered by blood
30. Grieskamp, T., Rudat, C., Lüdtke, T. H.-W., Norden, J. & Kispert, A. Notch signaling
flow, Notch activation, and CX37 (also known as GJA4)27. Pre-artery regulates smooth muscle differentiation of epicardium-derived cells. Circ. Res.
specification was independent of flow, but may engage similar mech- 108, 813–823 (2011).
anisms. Future experiments should investigate whether this higher- 31. Gawad, C., Koh, W. & Quake, S. R. Single-cell genome sequencing: current state
of the science. Nat. Rev. Genet. 17, 175–188 (2016).
resolution understanding of coronary artery differentiation during cardiac 32. Treutlein, B. et al. Reconstructing lineage hierarchies of the distal lung
angiogenesis could aid the development of regenerative therapies. epithelium using single-cell RNA-seq. Nature 509, 371–375 (2014).
19 JUlY 2018 | VOl 559 | NAtUre | 361
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
33. Velten, L. et al. Human haematopoietic stem cell lineage commitment is a performed CXCR7–GFP and FBLN2/ADM in situ hybridization. S.D. performed
continuous process. Nat. Cell Biol. 19, 271–281 (2017). P2/P6 postnatal analysis. S.R. peformed EdU experiments. A.H.C. performed
E14.5/E17.5 lineage quantification. A.P. performed the Isl1 experiment.
Acknowledgements We thank S. Tsai, M.-J. Tsai, S. Evans, B. Zhou, B.R. performed GSEA. T.T.D. and W.A.R. provided Coup-tf2 flox mice. K.E.Q. and
T. Quertermous and L. Iruela-Arispe for mice; M. Miyanishi for assistance with K.M.C. provided CXCR7–GFP mice. L.M. provided Cx40CreER mice. S.W. and G.L.
fluorescence-activated cell sorting; R. Morganti and G. Gulati for assistance provided adult scRNA-seq. T.S., G.S., and K.R.-H. prepared the manuscript. T.S.
with scRNA-seq; L. O’Brien, D. Bergmann, and V. Greco for manuscript performed most wet lab experiments. R.S., E.C.B., I.W., S.Q., and K.R.-H. provided
comments; and J. Ban for technical assistance. T.S. is supported by the NIGMS resources.
of the National Institutes of Health (T32GM007276). K.R.-H. is supported by
Competing interests The authors declare no competing interests.
the NIH/NHLBL (R01-HL128503) and the New York Stem Cell Foundation
(NYSCF-Robertson Investigator). T.T.D. is supported by the NIH/NHLBL T32 Additional information
(HL098049) and an AHA Postdoctoral Fellowship. E.C.B. is supported by the Extended data is available for this paper at https://doi.org/10.1038/s41586-
NIH (R01-GM037734, R01-AI130471) and the Department of Veterans Affairs. 018-0288-7.
Supplementary information is available for this paper at https://doi.
Reviewer information Nature thanks R. Adams, C. Marr and A. Siekmann for org/10.1038/s41586-018-0288-7.
their contribution to the peer review of this work. Reprints and permissions information is available at http://www.nature.com/
reprints.
Author contributions T.S., R.S., G.S. and K.R.-H. conceived the study. T.S. Correspondence and requests for materials should be addressed to K.R.
and R.S. captured cells and performed scRNA-seq. G.S. performed scRNA- Publisher’s note: Springer Nature remains neutral with regard to jurisdictional
seq computation. T.S., G.S. and K.R.-H. performed scRNA-seq analysis. G.D. claims in published maps and institutional affiliations.
362 | NAtUre | VOl 559 | 19 JUlY 2018
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
MEthodS tube were washed with a total of 1,200 μl sterile PBS. Cells were then centrifuged
Mice. All mice were used in compliance with Stanford University IACUC regulations. at 400g at 4 °C for 5 min. Each cell pellet was then gently resuspended in 600 μl 3%
The following mouse strains were used: wild type (CD1, Charles River Laboratories, FBS (in sterile PBS). Cells were centrifuged again at 400g at 4 °C for 5 min. Each
Strain Code #022), ApjCreER8, RosaCoup-tf2OE29, RosamTmG Cre reporter (The Jackson pellet was then gently resuspended in 2,000 μl 3% FBS and 32 U/ml DNase I in
Laboratory, Gt(ROSA)26Sortm4(ACTB-tdTomato,-EGFP)Luo/J, Stock #007576), RosaNICD sterile PBS. Cells were kept on ice until they were used for FACS.
(The Jackson Laboratory, Gt(ROSA)26Sortm1(Notch1)Dam/J, Stock #008159), RosatdTomato DAPI (1.1 μM) was added to the cells immediately before FACS. Single cells
Cre reporter (The Jackson Laboratory, B6.Cg-Gt(ROSA)26Sortm9(CAG-tdTomato)Hze/J, with a low DAPI signal, moderate PE-Texas Red signal and the highest Alexa-
Stock #007909), Isl1MerCreMer34, Cdh5CreER35, Cx40Creer36, Nfatc1Cre7, RosaConfetti Fluor 488 signal were sorted using Aria II SORP (BD Biosciences). Each cell was
(The Jackson Laboratory, Gt(ROSA)26Sortm1(CAG-Brainbow2.1)Cle/J, Stock #013731), sorted into a separate well of a 96-well plate containing 4 μl lysis buffer. Cells
Coup-tf2 flox (Mutant Mouse Regional Resource Center, B6;129S7Coup-tf2tm2Tsa/ were spun down after sorting and stored at −80 °C until cDNA synthesis. A total
Mmmh, Stock #032805MU). Apln-lacZ37, CXCR7-GFP (The Jackson Laboratory, of 480 SV cells and 480 ventricular cells were sorted and processed for cDNA
C57BL/6-Ackr3tm1Litt/J, Stock #008591), CXCL12-DsRed (The Jackson Laboratory, synthesis. Cells were analysed on the AATI 96-capillary fragment analyser, and
Cxcl12tm2.1Sjm/J, Stock #022458), VE-Cadherin-CreER38. All mice were maintained a total of 915 cells that had sufficient cDNA concentration were barcoded and
on a mixed background. pooled for sequencing.
Timed pregnancies were determined by defining the day on which a plug E14.5 scRNA-seq. The experiment was performed once following the same pro-
was found as E0.5. For Cre inductions, tamoxifen (Sigma-Aldrich, T5648) was cedure as for E12.5 above unless otherwise noted here.
dissolved in corn oil at a concentration of 20 mg/ml and was injected into the One thousand, one hundred and fifty-two FACS-captured coronary cells
peritoneal cavities of pregnant dams. For cell cycle inhibition, 0.4 mg dinaciclib was lineage-labelled with ApjCreER were collected from E14.5 hearts (SV cells were
dissolved in 2.6% DMSO (in PBS) and was injected into the peritoneal cavities of excluded and the later time point used to ensure sufficient numbers of Coup-tf2OE
pregnant dams. Dosing and dissection schedules for individual experiments were: cells). To isolate Coup-tf2OE cells, male ApjCreER Coup-tf2OE mice were crossed
(1) E12.5 single-cell RNA sequencing: tamoxifen on E9.5 and E10.5, dissection to RosamTmG females who were dosed with tamoxifen at E11.5 and E12.5 and the
on E12.5. (2) E14.5 single-cell RNA sequencing: tamoxifen at E11.5 and E12.5, embryos removed at E14.5. A total of 16 GFP-positive embryos from four lit-
dissection at E14.5. (3) ApjCreER Coup-tf2OE experiments: tamoxifen at E9.5 and ters were dissected for cell isolation and FACS. To isolate wild-type cells, male
E10.5, dissected at E14.5 or E15.5 for coronary contribution quantification. Same ApjCreER RosamTmG mice were crossed to CD1 females. Pregnant dams were dosed
dosing schedule, but dissected at E11.5 and E14.5 for recombination rate experi- with tamoxifen at E11.5 and E12.5 and embryos removed at E14.5. A total of 12
ment (E11.5 only) and expansion experiment. Same dosing schedule, but dissected GFP-positive embryos from three litters were sorted out and further dissected. For
at E11.5, E12.5, or E13.5, was used for ventricular coverage visualization; tamoxifen both the wild-type and the Coup-tf2OE samples, a few GFP-negative embryos were
at E11.5 and E12.5, dissected at E15.5 for capillary visualization in Extended Data processed for dissection and cell isolation in the exact same manner to serve as a
Fig. 9. (4) Cx40Creer Coup-tf2OE experiments: tamoxifen at E11.5 and E12.5 or negative control for the GFP signal during FACS.
E13.5, dissected at E15.5; for Extended Data Fig. 9i: tamoxifen at E11.5, dissected Cells with the highest Alexa-Fluor 488 signal, low DAPI signal, and low
at E15.5. (5) Cdh5CreER Coup-tf2OE before pre-artery: tamoxifen at E11.5 and PE-Texas Red signal were sorted into lysis buffer. For Coup-tf2OE, a total of 861
E13.5, dissected at E15.5. (6) Cdh5CreER Coup-tf2OE after pre-artery: tamox- cells were sorted and processed for cDNA synthesis. For wild-type, a total of 608
ifen at E13.5 and E15.5, dissected at E16.5. (7) Cdh5CreER Coup-tf2OE dinaciclib cells were sorted and processed for cDNA synthesis. Of these, 1,152 passed cDNA
experiment: tamoxifen at E11.5 and E13.5, dinaciclib at E12.5, dissected at E15.5. fragment quality control (concentration >0.05 ng/μl) and were sequenced. Of
(8) Cx40Creer Rosaconfetti: tamoxifen at E12.5, dissected at E15.5. (9) ApjCreER those, 1,126 passed QC threshold (>1,000 genes, 105 mm10-aligned reads). In
Coup-tf2OE NICD experiment: tamoxifen at E11.5 and E12.5, dissected at E15.5. Coup-tf2OE embryos, 326 cells expressed the FLAG-Myc transgene and were com-
(10) Cx40Creer RosatdTomato lineage tracing: tamoxifen at E11.5, dissected at E12.5, pared to the 423 control cells that passed QC.
P7 or P8; tamoxifen at E10.5, dissected at E15.5; tamoxifen at E16.5, dissected at cDNA synthesis and library preparation for scRNA-seq. We used Smart-seq2
P8. (11) Cdh5CreER Coup-tf2 flox dosage: tamoxifen at E10.5, dissected at E12.5; to perform scRNA-seq39. Poly-A mRNA in the cell lysate was converted to cDNA
tamoxifen at E11.5, dissected at E13.5 or E14.5. (12) ApjCreER lineage tracing and amplified as described39. Amplified cDNA in each well was quantified using
in right or left coronary artery: tamoxifen at E9.5 and E10.5, dissected at E14.5 a high-throughput fragment analyser (Advanced Analytical). After quantification,
and E15.5. (13) Pre-artery cells/Slc45a4 in ApjCreER lineage vessels: tamoxifen cDNA from each well was normalized to the desired concentration range (0.05–
at E9.5 and E10.5, dissected at E13.5. (14) Additional Cx40Creer and ApjCreER 0.16 ng/μl) by dilution, consolidated into a 384-well plate, and subsequently used
lineage-tracing experiments: see Extended Data Fig. 7. (15) VE-Cadherin-CreER for library preparation (Nextera XT kit; Illumina) using a semiautomated pipe-
Coup-tf2OE: tamoxifen at E15.5 and E16.5, dissected at E17.5. line as described40,41. The distinct libraries resulting from each well were pooled,
For additional Cx40Creer RosatdTomato embryonic lineage-tracing experiment, cleaned-up and size-selected using precisely 0.6× to 0.7× volumes of Agencourt
pregnant dams were dosed via oral gavage with 1 mg 4-OH tamoxifen (Sigma- AMPure XP beads (Beckman Coulter), as recommended by the Nextera XT pro-
Aldrich H6278) at E11.5 and dissected at E12.5 (Extended Data Fig. 6f) or E15.5 tocol (Illumina). A high-sensitivity Bioanalyzer (Agilent) run was used to assess
(Fig. 2). fragment distribution and concentrations of different fragments within the library
For postnatal lineage tracing at P2 and P6, tamoxifen was injected into the pool. It is important to note that after pooling the libraries and before sequencing
peritoneal cavity of the mother when the neonates were at P2 so that tamoxifen there is no PCR step in our protocol. Pooled libraries were sequenced on NextSeq
could be passed from the mother to the neonates through milk. 500 (Illumina).
No statistical methods were used to predetermine sample size. For in vitro Demultiplexing and alignment of scRNA-seq reads. The resulting reads were 1)
experiments, cultures were randomly chosen for different treatments and exper- demultiplexed using Illumina’s demultiplexing tool bcl2fastq (default settings),
iments were performed multiple times. Randomization was not relevant to our and 2) processed using skewer11 for 3′ quality-trimming, 3′ adaptor-trimming,
mouse experiments because genotypes/groups were determined by mouse genetics. and removal of degenerate reads, as described9. The processed reads were mapped
Blinding was used in scRNA-seq and mouse experiments, except for lineage tracing, to the mouse genome (mm10) using STAR (https://github.com/alexdobin/STAR)
EdU experiments, Coup-TF2OE cell quantification and NICD quantification, where and gene expression was quantified with HTSeq (http://htseq.readthedocs.io/en/
blinding was not possible because cells positive for certain markers (MYC tag, GFP, release_0.9.1/). The expression of the Coup-TFII-OE transgene was quantified by
tdTomato, EdU) revealed the identities of the samples. aligning reads to the following sequence, encoding the FLAG-Myc t ag: T AA GCT
Cell isolation for scRNA-seq. E12.5 scRNA-seq. SV-derived cells were captured by TCGTATATACCTTTCTATACGAAGTTGTGGATCTGCGATCTAAGTAAGC
fluorescence-activated cell sorting (FACS) of ApjCreER lineage-labelled cells (Cre CGCGGCCATGGACTACAAGGATGACGATGACAAGGCCGCGGCAACTA
expressed in SV). An experiment was performed once in which male ApjCreER GTAAGCTTGCCGCCATGGAGCAGAAACTCATCTCTGAAGAGGATCTGT.
RosamTmG mice were crossed to CD1 females, who were dosed with tamoxifen at Cell subtype discovery with iRPCA. First, low-quality cells were filtered out
E9.5 and E10.5. Embryos were removed and placed into cold, sterile PBS at E12.5. by the following thresholds: >1,000 genes, <40% rRNA, >105 mm10-aligned
The SVs of each of 27 GFP-positive hearts were microdissected away from the reads, from 915 sequenced cells. Eight hundred and fourty-three cells passed
ventricles and pooled into a 300-μl mix consisting of 500 U/ml collagenase IV quality control.
(Worthington #LS004186), 1.2 U/ml dispase (Worthington #LS02100), 32 U/ml To identify the broad cell subtypes present, in situ hybridization data on 52
DNase I (Worthington #LS002007), and sterile DPBS with Mg2+ and Ca2+. The genes from the Euroexpress42 database were compared to expression levels in
ventricles of the 27 hearts were minced with forceps and pooled together in another an rPCA plot of all cell in the data set, excluding erythrocytes (Extended Data
300 μl of the aforementioned mix. The pooled SVs and ventricles were then incu- Fig. 1j).
bated at 37 °C, and gently resuspended every 7 min. After the incubation, 60 μl cold Cell subtypes in the ApjCreER-labelled populations were manually defined
FBS followed by 1,200 μl cold sterile PBS were added and mixed into each tube. The using gene expression patterns in manually selected PC plots derived from multi-
samples were then filtered through a 70-μm cell strainer; the filter and the source ple iterative rounds of rPCA (iRPCA). There were two overall goals of iRPCA. The
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
first was to fully describe the cellular subtypes within an scRNA-seq data set while of 202 cell cycle genes described below). Cells are then given a score x by their
minimizing over-clustering of homogenous populations or continua, clustering expression of these genes:
based on cell cycle phase or technical artefacts/cell quality, and under-clustering of
g
small subpopulations. The second goal was to preserve continuity or discreteness x = ∑
between subpopulations. A g∈gA maxg
Our pipeline differed from standard pipelines in several ways. First, we used
rPCA (rrcov::PcaHubert) in lieu of standard PCA. Second, we replaced default PC g
scores by those calculated by the sum of top 60 genes: PC.score = PC.pos−PC.neg x B = ∑ maxg
(Extended Data Fig. 1b, c). These two parameters were used because they provided g∈gB
more clearly defined separations among cells with unique gene expression patterns
(see Extended Data Fig. 1a, b and additional description in main text). Finally, we x= x A − x B
made frequent use of PC pos/neg biplots, which we defined by: maxx maxx
A B
PC.pos=∑ 30 g i,p W
all
h
c
e
e
r
ll
e
s
g
i n
is
t
i
h
n
e
l o
p
g
a
1
ir
0
o
co
f
u
su
n
b
ts
t y
p
p
e
e
r
s
m
. T
il
h
li
i
o
s
n
s c
(
o
C
r
P
e
M
s c
)
e
u
ll
n
s
i
a
t
l
s
o
a
n
n
g
d
t
m
he
a
a
x
x
i
i
s
s
t
o
h
f
e
c
m
ell
a
i
x
d
im
en
u
ti
m
ty
a
a
c
l
r
o
o
n
s
g
s
maxg
i=1 i,p A and B. The resulting distribution of cells along this axis is tested for discreteness,
or a lack of intermediate cells, by the width of the largest gap between the two
30 g distributions. The statistic is calculated by the following procedure (Extended Data
PC.neg=∑ i,n
Fig. 1f):
maxg
i=1 i,n 1. The distribution is fitted to a Gaussian mixture model with two components,
Where gi,p are the top 30 genes by positive loading to the PC and gi,n by giving means µ A and µ B.
negative loading. These were used to identify and exclude cell cycle-associated 2. Cells within the range (µ A, µ B) are identified as candidate intermediates.
PCs (described below in Identifying cell cycle-regulated genes) (Extended 3. The largest gap distance between candidate intermediate cells, dmax, is
Data Fig. 1d) and to inspect for cell doublets (expected to have nearly equal identified.
levels, on a log scale, of the top markers for two distinct subpopulations; we did 4. The list of candidate intermediate cells is further restricted to the 10 cells on
not see any in our data set, possibly owing to strict FACS gating on FSC-W and either side of dmax, and their gap distances, excluding dmax, are fit to an exponential
SSC-W and the large spacing of wells on standard 96-well plates) (Extended with rate k, F(d;k). If there is a uniform distribution of intermediate cells along the
Data Fig. 1e). continuum from A to B, the gap distances di follow an exponential distribution
Cell subtype clusters were assigned through the following process. After P(d) ≈ e−kd, where the mean gap distance E[d] = 1/k (equivalent to the mean time
removing a small number of erythrocytes, all cells in the data set were used between events for a Poisson process occurring at rate k).
to calculate 15 PCs where the input was all genes minus those in our cell cycle 5. The discreteness statistic is calculated as D = log10F(dmax;k).
category (see Identifying cell cycle-regulated genes) and the output was PC plots 6. Two populations are considered discrete if D < −6. In the PlotConnectogram
based on the sum of top 60 genes. Among the resulting 15 PC plots, one was man- function, distributions with −3 > D > −6 are connected by a semitransparent lines
ually chosen for further analysis based on the following criteria: 1. cells were well to indicate lower confidence in their continuity. In simulated data, this corre-
separated among the PC axes; 2. expression patterns of the top 60 genes revealed sponded to 3–5 intermediate cells. Distributions with med(D) > −3 are connected
distinct populations or clusters; and 3. the PC was not highly correlated with by 100%-opacity lines to indicate high confidence in their continuity.
cell cycle genes (see Identifying cell cycle-regulated genes) or number of genes Estimating the number of intermediate cells. Second, the number of intermediate
detected (that is, technical artefact). Distinct cell populations within the selected cells connecting the two pairs is estimated by maximum-likelihood fitting of a
PC were manually identified by their separation from other cells within the plots five-parameter distribution. This distribution was derived by considering two cell
and strong correlation with distinct gene expression patterns. One (or more) types with mean expression values µ A, µ B and a transitional population sampled
distinct cell population was then removed, and another iteration was performed evenly from the range of values µ A < µ < µ B. The exact PDF that describes sam-
to calculate another set of PCs containing the decreased number of cells. Each of pling from this distribution with Gaussian noise is:
these subsequent iterations similarly involved, first, a PC calculation (10–15 PCs µB
depending on step), then, a manual selection of one PC plot based on the P(x;µ ,µ ,σ)=f N(x;µ ,σ)+f N(x;µ ,σ)+f ∫ N(x;µ,σ)dµ (1)
above-described criteria, and, finally, within that selected PC the manual identi- A B A A B B AB
fication or removal of cell subpopulations based on the above-described criteria.
µA
These iterations ended when the calculated PCs revealed a single continuum that where fA is the fraction of cells in cell type A, fB is the fraction of cells in cell type
was arranged in a linear progression on the PC plots, which indicated the pres- B, and fAB is the fraction of cells along the A–B continuum. The integral in (1) is
ence of only two groups of cells: one with high expression of one set of markers approximated by
and the other with high expression of a second set of markers (Extended Data
Fig. 1k). These last continua were separated into two groups, which comprised 0, x<µ −2.7σ
t
m
th
h
o
e
e
I r n
r
f
e
e
i
c
n
p
t l h u
a
o
a d
l
r
n
t
c
e
e
d
l
d
t
u
w i
s
c
n
t
o
l
e
u
t g
r
s
h
s
r
t
e
.
e
o
r
I
c u
s
n
u p
i
s s
n
t
t
h
. o
t
i
m
h
s
e
w
R
E
a
1
s
y
2
c
,
.
r
a
5
i p
s
d
t
i
a
s
n
t
a
g
a
r
l
.
e
e
I n
t
c
h
o
t
e
h
n
e
e
t i
x
f
n
i
a
r
u
c
s
t
u
t
s
m
tw
te
o
p
w
s
r
a
o
b
s
u
y
n
n
w
o
d
t
h
s ,
o
i c
r
v
h
P
e
C
r
w
c
A
e
lu
o
(
s
r
b
t
r
e
t
c
a
r
o
i
e
n
v
d
:
e
: P
d
in
c
a
t
a
l
o
-
l
∫
µB
N(X;µ,σ)dµ≈
   
    
1
C
,
exp

   
(x−
3σ
µ
3 A
)3
    +D, µ
µ
A −
+
2
A
2
.7
.7
σ
σ
≤
≤
x
x
<
<
µ
µ
A +
−
2
2
.
.
7
7
σ
σ (2)
Hubert, k = 15) was run using all genes expressed in >1 cell, filtered by removing  A B

r L b i a e b l r o o s2 s w o , a m w n a a d s l M p a r l a s o o l t a e t r i 1 e n . m s I n b o y v a l e g l d r r e o f p u ro ( n R m d p s [ t a l h s f e ] te * g r ) e , t n h as a e t w l , i t s e h t l . e l I a l n i s s t R t o o n t f 4 a 2 5 l 0 , s 2 2 ( 0 a c e l r s l o o l u c k y n n c d l o e s w g o n e f n i a R e s s P R d C n e A s a c 4 r w 5 ib s e 5 e r ) d e , µA        Fexp      (x− 3σ µ 3 B )3     +G, µ B −2.7σ≤x<µ B +2.7σ
performed to cluster cells into the 10 subpopulations in this work.

  0, x≥µ
B
+2.7σ
Pairwise discreteness test. To analyse the relationship between pairs of sub-
populations of cells, the cells of the two subtypes are first projected onto a single Where C, D, F, G are calculated to make (2) a continuous function. This PDF is
axis of identity. For the purpose of the following description, these populations then fit to the distribution using Nelder-Mead optimization (stats::optim) with five
are referred to as A and B. To do this, cells are scored by their expression of the top iterations for different initial values of fAB. The initial values for µ A, µ B, and σ are
differentially expressed genes between the two populations. Differential expression derived by fitting with a two-component Gaussian mixture model. fAB determines
is calculated as log fold change, fractional difference (difference in fraction of A the width of the lines connecting populations in our PlotConnectogram function.
cells expressing minus the fraction of B cells expressing), and Wilcoxon P value; Simulation of population distributions for model validation. We optimized the
genes are filtered by fold change >0.2 (natural logarithm), fractional difference cutoffs for the discreteness test using simulated data. The data was simulated by
>0.05, and P < 10−3. The top n genes, sorted by fold change and fractional differ- drawing from the five-parameter distribution described above under Estimating
ence, are referred to as ga (top n genes enriched in A) and gb (top n genes enriched the number of intermediate cells, where fAB ranged from 0 to 1 (Extended Data
in B). The results do not vary much for n between 20 and 100 (Extended Data Fig. 1h). Using the simulations, we found −6 to be a good cutoff for calling cell
Fig. 1l, only low-confidence connections change). In this work, the gene list is types discrete—this cutoff is low so as to be sufficiently sensitive to a small number
pre-filtered by removing ribosomal genes (Rp[ls]*) and cell cycle genes (the list of intermediates (~3 intermediate cells out of 150).
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
Identifying cell cycle-regulated genes. When mentioned in the main text, we stored at −20 °C for the long term. Imaging was done with Zeiss LSM-700 (10×
filtered out a list of 202 cell cycle genes from the input to rPCA to reduce the con- or 20× objective lens) with Zen 2010 software (Zeiss).
tribution of cell cycle to heterogeneity. We defined this list by rPCA: cell cycle PCs For whole-mount postnatal hearts. Hearts were fixed in 4% PFA for 1 h at 4 °C with
were identified by high loadings of known cell cycle markers (for example, cyclins, shaking and washed twice (15 min each wash) with PBS at 4 °C with shaking before
Mki67, Top2a). Also, cell cycle has a unique pattern on PCi.pos versus PCi.neg dissection for whole-mount immunostaining. In the primary antibodies (diluted
biplots (described above): there is typically a large coordinated increase in genes in PBT), hearts were shaken at room temperature for 6 h and overnight at 4 °C. To
upon entering cell cycle with little corresponding decrease in genes, and PCi.pos wash the primary antibodies, hearts were shaken in PBT at room temperature for
has low correlation to PCi.neg. The positive and negative loadings were therefore 10 h and overnight at 4 °C. Hearts were washed in 50 ml PBT and the wash was
inspected separately for cell cycle genes. In this work, rPCA was performed on a changed every 2 h while shaking at room temperature. Hearts were then placed
highly cycling, relatively homogeneous subgroup of cells (later identified as SVc and in secondary antibodies (diluted in PBT) at room temperature with shaking for
CV) using all genes; we used the union of the top 60 genes by each of the following 6 h and overnight with shaking at 4 °C. Hearts were then washed in 50 ml PBT
loadings: PC1-positive, PC2-negative, PC2-negative, PC4-positive, PC5-negative, for 8 h (wash changed every 2 h) and overnight at 4 °C. The washing was repeated
and PC6-negative, which produced a list of 230 candidate cell cycle genes. We for six more days. Prior to imaging, Vectashield (Vector Labs, H1000) was added
filtered this list for genes that had high loadings to other PCs, marked subpopu- to hearts in clean tubes, and hearts were equilibrated at room temperature for
lations of cells, and had no cell cycle annotation; these included arterial markers 40 min. Imaging was done with Zeiss LSM-700 (10× or 20× objective lens) with
such as Unc5b. This produced the final list of 202 cell cycle genes. This list was not Zen 2010 software (Zeiss).
complete, but was sufficient to remove cell cycle heterogeneity from the top PCs. Primary and secondary antibodies. The following primary antibodies were used
Defining the fetal SVc–CV plexus–arterial axis. We defined the SVc–CV plexus– at the indicated concentrations: MYC-Tag for COUP-TF2OE (Cell Signaling
arterial axis (x) using the scores generated by PC2 and PC3 from RPCA on SVc, Technology, Inc., 2278S, 1:300), VE-Cadherin (BD Pharmingen, 550548, 1:125),
CV, and arterial cells (Fig. 3a, Extended Data Fig. 4) as below: VEGFR2 (R&D Systems, AF644, 1:125), CX40 (Alpha Diagnostic International,
CX40A, 1:300), ERG (Abcam, ab92513, 1:500), CXCR4 (BD Pharmingen, 551852,
  PC2.score, PC3.score3−PC2.score−0.4 1:125), GFP (Abcam, ab13970, 1:500), VWF (Abcam, ab6994, 1:500), CLDN11
x=
   PC2.score2+PC3.score2, PC3.score<−PC2.score−0.4 ( α A -s b m ca o m ot , h a b m 5 u 3 s 0 c 4 le 1 – , F 1 I : T 1, C 00 ( 0 S ) ig , m SO a, X F 1 3 7 7 ( 7 R 7, & 1 D :2 0 S 0 y ) s , t V em EG s, F A R F 3 1 ( 9 R 2 & 4, D 1 : S 5 y 0 s 0 te ) m , a s n , t A i- F a 7 c 4 ti 3 n ,
1:125), DACH1 (Proteintech, 10914-1-AP, 1:500), JAG1 (R&D Systems, AF599,
Figure 3a was coloured by the value of this axis.
1:125).
Cell cycle scoring. G1/S and G2/M signatures were discovered in an unbiased
All secondary antibodies were Alexa Fluor conjugates (488, 555, 633, 635, 594,
manner as follows: coronary vessel plexus cells from wild-type E14.5 animals were
647, Life Technologies, 1:125 or 1:250). DAPI (1 mg/ml) was used at 1:500.
analysed with rPCA using all detected genes. Many of the top 60 genes by loading
In situ hybridization. To identify the broad cell subtypes in the E12.5 single cell
to PC3.neg and PC2.neg were known G1/S markers, and, thus, the G1/S score of
data set, expression levels in rPCA plots of 52 genes were compared to in situ
a cell was defined by the sum of the scaled expression of these genes. Many of the
hybridization data from the Euroexpress42 and Allen Brain Atlas databases (stages
genes with high loadings to PC4.neg and PC5.neg were known G2/M markers,
ranged from E11.5 to E15.5). Expression patterns from E14.5 Euroexpress data are
and the G2/M score was calculated by the sum of the scaled expression of these
shown in Extended Data Fig. 1i.
genes. Cells were scored as cycling if they were not in the bottom-left modes (high
For Adm and Fbln2, in situ hybridization on paraffin sections were performed
expression of at least one cell cycle signature).
twice as described previously43. Antisense Adm and Fbln2 probes were labelled with
Seurat clustering for comparison. To compare our clustering to Seurat, we ran
digoxigenin (DIG)-UTP using the Roche DIG RNA labelling System according
Seurat with primarily default options. We filtered our list of 202 cell cycle genes
as well as ribosomal proteins from the list of highly variable genes (y.cutoff = 0.5) to the manufacturer’s guidelines.
For Slc45a4, whole hearts were fixed and in situ hybridization performed according
and ran PCA with 20 scores calculated. Based on the PC elbow plot, we selected
to protocol from Additional File 2 of ref. 44. Probes were Cdh5 (Advanced Cell
the first 10 PCs to be used for clustering. We excluded PC6 for high loading of cell
Diagnostics 312531-C2), Cx40 (Advanced Cell Diagnostics 518041), and Slc45a4
cycle genes (since our list of 202 genes was not exhaustive), and clustered using
(Advanced Cell Diagnostics 522131-C3). Reagents are RNAscope Protease III
FindClusters with resolution 2. We also calculated t-SNE, and we used the t-SNE
& IV Reagents (Advanced Cell Diagnostics 322340) and RNAscope Fluorescent
mediods of cell clusters to place the vertices for our results from pairwise PCA
Multiplex Detection Reagents (Advanced Cell Diagnostics 320851). About 12
(Extended Data Fig. 1l).
embryonic hearts were dissected in a sterile and RNase-free environment into a
Comparison to adult artery–vein continuum. We determined the similarity
1.5-ml tube and fixed in 1 ml 4% PFA for 1 h at room temperature. Three fixed
between our E12.5 endothelial cells and the mature artery–vein continuum as
hearts were processed in the same tube with 100 μl of the probes master mix. The
follows. We selected cells from the Tabula Muris data set with the Tissue label
experiment was performed three times, once each for E13.5 (n = 3), E14.5 (n = 2),
‘Heart’ and annotation label ‘1’. We ran PCA on the most variable genes
(y.cutoff = 0.35) with the Seurat package. PC2 and PC3 separated cells into three and E15.5 (n = 3).
SV–atria explant experiment. The experiment was performed three times. In total,
populations along a single continuum, and we projected cells onto a single axis
 PC2,PC2<0 71 embryos were dissected at E12.5. The SV and atria of each embryo were dis-
x=  . Known arterial genes such as Cx40, Cx37, and sected on sterile PBS and gently dropped onto a cell culture insert (EMD Millipore
   PC22+PC32, PC2≥0 PI8P01250) coated with Matrigel (BD Biosciences) inside a well of a 24-well plate.
Unc5b were negatively correlated, and known capillary/venous markers such as Two to five explants were cultured onto each insert. Immediately after the explants
Apj and Nrp2 were positively correlated to the axis, so we considered it to be the were dropped onto the insert, 200 μl EGM2-MV medium was added into the
artery–vein continuum (AVc). We then calculated the similarity of each fetal cell space between the insert and the well. The SVs were allowed to attach onto the
to each adult cell. To do this, we used as input the union of the top 300 genes Matrigel at 37 °C for 2–6 h before another 200 μl EGM2-MV medium was added
correlated to the adult and fetal AVc, smoothed by LOESS regression over the AVc to the space between the insert and the well. The explants were cultured at 37 °C
defined above. We calculated the Pearson correlation similarity using these for approximately 72 h before either flavopiridol or DMSO was added: 900 μl of
features, and mapped each fetal cell to the adult cell to which it was most similar 40 nM flavopiridol (dissolved in 0.1% DMSO in EGM2-MV) or 0.1% DMSO in
by this metric. EGM2-MV (drug vehicle control) was added to each insert. After addition of
Immunohistochemistry and Imaging. For whole-mount embryonic hearts. All either flavopiridol or DMSO, explants were incubated at 37 °C for approximately
embryos were fixed in 4% PFA at 4 °C with shaking and washed twice (10 min each 48 h before they were fixed and stained.
wash) with PBS at room temperature with shaking before dissection for whole- Each cell culture insert was fixed in 1,000 μl 4% PFA for 2 h at 4 °C without
mount immunostaining. shaking. Then, each insert was washed with 1,000 μl PBS three times at room
Intact embryonic hearts were washed in PBT (PBS with 0.5% Triton-X 100) temperature. Five hundred microlitres of primary antibodies (diluted in 0.5% PBT)
at room temperature for one hour before incubation with primary antibodies. were added onto each insert and inserts were incubated at room temperature with
Primary antibodies were dissolved in either 5% goat serum or 5% donkey serum in shaking for 4–6 h. The inserts were subsequently washed with PBS at room tem-
PBT. Hearts were incubated in the solution with primary antibodies with shaking perature with shaking for 2 h. Five hundred microlitres of secondary antibodies
overnight at 4 °C. Hearts were then washed with PBT for six to nine hours with (diluted in 0.5% PBT) were added onto each insert and inserts were incubated at
shaking at room temperature, and the wash was changed every hour. Hearts were 4 °C for about 16 h. The inserts were then washed with PBS three times at room
then stained with secondary antibodies with the same conditions and procedure temperature with shaking for 2 h. The membrane containing the SVs was then
as for primary antibodies. After washing off the secondary antibodies, hearts were excised from the insert and mounted onto a drop of Vectashield on a slide and
then left in enough PBT to cover them. Two drops of Vectashield (Vector Labs, stored at −20 °C. Imaging was done using a Zeiss LSM-700 (10× or 20× objective
H1000) were added and mixed with the PBT for each heart, and the hearts were lens) with Zen 2010 software (Zeiss).
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
Acquisition and processing of images. All images were acquired with Zen 2010 35. Wang, Y. et al. Ephrin-B2 controls VEGF-induced angiogenesis and
software (Zeiss). Images were prepared using Photoshop CS6 (Adobe). Any lymphangiogenesis. Nature 465, 483–486 (2010).
36. Miquerol, L. et al. Endothelial plasticity drives arterial remodeling within the
changes to brightness and contrast were applied equally across the entire image.
endocardium after myocardial infarction. Circ. Res. 116, 1765–1771 (2015).
In vivo EdU Assay. To measure in vivo proliferation rate, 50 μg/g body weight
37. Sheikh, A. Y. et al. In vivo genetic profiling and cellular localization of apelin
of EdU was injected into pregnant mice intraperitoneally 2–3 h before embryo reveals a hypoxia-sensitive, endothelial-centered pathway activated in ischemic
collection. EdU-positive cells were detected using a Click-iT EdU kit (Invitrogen, heart failure. Am. J. Physiol. Heart Circ. Physiol. 294, H88–H98 (2008).
C10338) according to the manufacturer’s instructions. In brief, Click-iT reaction 38. Alva, J. A. et al. VE-Cadherin-Cre-recombinase transgenic mouse: a tool for
cocktails were incubated for 30 min after the secondary antibody incubation of lineage analysis and gene deletion in endothelial cells. Dev. Dyn. 235, 759–767
(2006).
the immunostaining protocol.
39. Picelli, S. et al. Full-length RNA-seq from single cells using Smart-seq2.
Quantification and statistical analysis of confocal images. See Supplementary Nat. Protocols 9, 171–181 (2014).
Methods for details. 40. Koh, P. W. et al. An atlas of transcriptional, chromatin accessibility, and surface
Code availability. The custom R scripts used to analyse the scRNA-seq data are marker changes in human mesoderm development. Sci. Data 3, 160109
publicly available on GitHub (https://github.com/gmstanle/coronary-progeni- (2016).
41. Loh, K. M. et al. Mapping the pairwise choices leading from pluripotency to
tor-scRNAseq).
human bone, heart, and other mesoderm cell types. Cell 166, 451–467
Data availability. Raw scRNA-seq data are available at https://github.com/gmstanle/ (2016).
coronary-progenitor-scRNAseq. Figures associated with the raw data are Figs. 1, 3, 4, 42. Diez-Roux, G. et al. A high-resolution anatomical atlas of the transcriptome in
and Extended Data Figs. 1–8. There is no restriction on data availability. Source Data the mouse embryo. PLoS Biol. 9, e1000582 (2011).
for Figs. 2, 4, 5, and Extended Data Figs. 6–9 are provided with the paper. 43. D’Amato, G. et al. Sequential Notch activation regulates ventricular chamber
development. Nat. Cell Biol. 18, 7–20 (2016).
44. Gross-Thebing, T., Paksa, A. & Raz, E. Simultaneous high-resolution detection of
34. Sun, Y. et al. Islet 1 is expressed in distinct cardiovascular lineages, including multiple transcripts combined with localization of proteins in whole-mount
pacemaker and coronary vascular cells. Dev. Biol. 304, 286–296 (2007). embryos. BMC Biol. 12, 55 (2014).
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
Extended Data Fig. 1 | See next page for caption.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
Extended Data Fig. 1 | Single cell analysis of ApjCreER lineage discrete (left) and continuous (right) pair of subpopulations.
labelled cells. a, Comparison of rPCA and classical PCA at separation g, FACS plots used to isolate GFP-positive cells (red box) from ApjCreER
of subpopulations. PC scores were selected to best separate the Enpp+ RosamTmG hearts at E12.5. h, Top, discreteness statistic generated by
Esam− population. Cells are coloured by expression (log10 CPM, scaled pairwise discreteness test as a function of number of intermediate cells
to maximum per gene). n = 352 cells. b, Comparison of default and (nint) for simulated distributions. Bottom, pairwise distributions of cell
sum-of-60 modified PC scores. PC2 is the default PC score from rPCA; clusters in the data set and the fraction of intermediate cells estimated by
PC2.score is the modified sum-of-top-60 scores (expression is log10 CPM, pairwise discreteness analysis. i, rPCA plots and their accompanying gene
scaled to maximum). Y-axis is the number of genes detected per cell (>1 expression patterns in the embryonic heart as reported by Euroexpress. In
count). n = 426 cells. c, Comparison of default and sum-of-top-60 scores. situ hybridization images show whole hearts (top); insets of specific areas
Scores were chosen that best separated the Vwf+ and Cxcr4 populations. are in lower panels with relative expression levels indicated. Expression
n = 426 cells. d, Unique cell cycle signature on PC.pos/PC.neg biplots. levels in rPCA plots range from 0 (yellow) to 4 (brown) in log10CPM. Top,
PC1.pos (PC1.neg) is the sum of the top 30 genes by positive (negative) n = 843 cells. j, Summary of broadly defined cell populations as indicated
loading to PC1. Cells are coloured by expression. Lower panel is the same by gene expression patterns. n = 843 cells. k, Example of manual clustering
rPCA after removing the list of 202 cell cycle genes. Numbers in bold are process. For i, n = 732 cells; ii, n = 531 cells; iii, n = 415 cells; iv, n = 284
the correlations between PC1.pos and PC1.neg. n = 674 cells. e, PC.pos/ cells; v, n = 261 cells. l, Comparison of pairwise discreteness test results for
PC.neg biplot showing theoretical location of doublets expressing high different numbers of genes per cell type signature (n).
levels of both gene sets. f, Schematic of the pairwise discreteness test on a
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
Article reSeArcH
Extended Data Fig. 2 | Identification of a coronary progenitor niche SV has two distinct domains, the SVc (sinus venosus, coronary
within the SV. a, Gene expression patterns identify cell types in rPCA adjacent) and the SVv (sinus venosus, valve adjacent). e, rPCA on the
plots of the venous valve–SV–CV continuum. Expression levels are log10 valve–SVv–SVc continuum identified specific markers of the SVv and SVc.
CPM and range from 0 (yellow) to 4 (brown) as indicated. Left, n = 843 Solid box, n = 732 cells. Dotted box, n = 415 cells. f, In situ hybridization
cells; right, n = 732 cells. b, c, Expression patterns in rPCA plots (b) and of SVv and SVc markers revealed complementary localization in vivo.
whole-mount confocal immunofluorescence (c) of selected genes. For g, Colour coding showing subpopulations that were used to calculate
b, n = 732 cells. d, Overlaying gene expression patterns suggests that the average expression levels. Scale bars, b, 200 μm, e, 30 μm.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
reSeArcH Article
Extended Data Fig. 3 | Characterization of pre-artery cells. a–d, rPCA coronary artery cells. Data are from the Tubula Muris consortium. n = 445
plots of the E12.5 SVc–CV continuum. Each dot is an individual cell, and cells. f, Assignment of artery, capillary, and vein in adult coronary cells
gene expression levels are indicated by the colour spectrum as shown in based on gene expression enrichment in e. n = 445 cells. g, Schematic for
Fig. 1d, which reflects log10 CPM. a, Arterial genes highly enriched in comparing E12.5 coronary cells to those along the adult artery–capillary–
the arterial areas of the plot. b, Arterial genes significantly upregulated vein continuum. h, Results of experiment schematized in g. The centre
in, but not specific to, the arterial area of the plot. c, Venous genes highly line correspond to the median; the upper and lower hinges correspond to
depleted in the arterial areas of the plot. d, Venous genes downregulated, the first and third quartile, respectively; the whiskers extend to the largest
but not depleted, in the arterial area of the plot. For a–d, Bonferroni- value or to 1.5 × IQR (inter-quartile range, or distance between quartiles),
adjusted P < 0.01; PCA plots, n = 415 cells. Centre and error bars are whichever is smaller. Pre-artery cells: n = 20 cells. CV: n = 277 cells.
mean ± s.e.m. of log CPM expression values. e, Genes expressed in adult P = 6.2 × 10−13. Statistical test is two-tailed.
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
