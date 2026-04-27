---
source_path: /mnt/c/Users/Administrator/Zotero/storage/MRAP8AKU/Parreno 等 - 2024 - Transient loss of Polycomb components induces an epigenetic cancer fate.pdf
ingested: 2026-04-23
sha256: b6b9a6ad68c45b1a
---

Article
Transient loss of Polycomb components
induces an epigenetic cancer fate
https://doi.org/10.1038/s41586-024-07328-w V. Parreno1,9, V. Loubiere1,2,9, B. Schuettengruber1, L. Fritsch1, C. C. Rawal3, M. Erokhin4,
B. Győrffy5,6, D. Normanno1, M. Di Stefano1, J. Moreaux1,7,8, N. L. Butova3, I. Chiolo3,
Received: 20 January 2023
D. Chetverina4, A.-M. Martinez1 ✉ & G. Cavalli1 ✉
Accepted: 15 March 2024
Published online: xx xx xxxx
Although cancer initiation and progression are generally associated with the
Open access accumulation of somatic mutations1,2, substantial epigenomic alterations underlie
Check for updates many aspects of tumorigenesis and cancer susceptibility3–6, suggesting that genetic
mechanisms might not be the only drivers of malignant transformation7. However,
whether purely non-genetic mechanisms are sufficient to initiate tumorigenesis
irrespective of mutations has been unknown. Here, we show that a transient
perturbation of transcriptional silencing mediated by Polycomb group proteins is
sufficient to induce an irreversible switch to a cancer cell fate in Drosophila. This is
linked to the irreversible derepression of genes that can drive tumorigenesis,
including members of the JAK–STAT signalling pathway and zfh1, the fly homologue of
the ZEB1 oncogene, whose aberrant activation is required for Polycomb perturbation-
induced tumorigenesis. These data show that a reversible depletion of Polycomb
proteins can induce cancer in the absence of driver mutations, suggesting that
tumours can emerge through epigenetic dysregulation leading to inheritance of
altered cell fates.
Genetic, epigenetic and environmental inputs are deeply intertwined, associated with cancer38. PRC2 deposits the H3K27me3 repressive mark,
making it difficult to disentangle their respective contributions to cell whereas PRC1, which contains the PH, PC, PSC and the SCE subunits in
fate decisions8,9, and epigenetic reprogramming is a major contributor flies, is responsible for H2AK118Ub deposition36. Contrasting with the
to tumour plasticity and adaptation10,11. Over recent decades, large-scale redundancy found in mammals36, most PcG components are encoded
projects expanded the known repertoire of cancer-associated genetic by a single gene in Drosophila, making this system more tractable for
mutations affecting epigenetic factors12,13, including chromatin functional studies39.
remodellers and modifiers, which regulate histone marks14,15, DNA
methylation16, micro-RNAs17 and 3D-genome folding18, corroborating
Epigenetic perturbations initiate tumours
the role of epigenetic aberrations in the aetiology of haematologi-
cal and solid malignancies19,20. Indeed, epigenetic modifications are Null mutations or constant RNAi (RNA interference) knock-down (KD)
used as biomarkers and are targeted by epi-drugs in cancer therapy21. targeting both ph homologues (ph-p and ph-d, which we refer to as ph
Tumorigenesis is therefore associated with genetic as well as epigenetic for simplicity) can induce growth defects, loss of differentiation and
determinants22–25. The fact that several hallmarks of human cancer24,26 cell overproliferation40–43. To test whether a transient epigenetic per-
may be acquired through epigenome dysregulation suggests that epi- turbation might initiate an irreversible change in cell fate, we set up a
genetic alterations play causal roles in cancer4,27,28 and in metastatic thermosensitive ph-RNAi system enabling the reversible KD of ph in the
progression29–33. In some paediatric cancers, such as posterior fossa developing larval eye imaginal disc (ED) (Fig. 1a,b and Extended Data
ependymoma, low numbers of mutations were detected, consistent Fig. 1a–d). The PH protein is depleted in 24 h at 29 °C and is restored
with the possibility that epigenetic changes may drive tumorigenesis30. within 48 h of recovery at 18 °C (Extended Data Fig. 1e).
These observations suggest that cancer is not solely a consequence of As expected, on constant PH depletion throughout development,
DNA mutations34,35, but whether purely non-genetic reprogramming 100% of EDs collected at the third larval stage (L3) are transformed
mechanisms are sufficient to initiate tumorigenesis remains an open into tumours (Fig. 1c,d and Methods), resulting in reduced viabil-
question. Polycomb group (PcG) proteins are epigenetic factors form- ity (Extended Data Fig. 1f). A transient 24 h depletion of PH at the L1
ing two main classes of complexes called Polycomb Repressive Complex stage, during which the ED starts developing, is also sufficient to trig-
1 and 2 (PRC1 and PRC2, respectively), which are highly conserved from ger tumour formation in L3 EDs, characterized by overgrowth, loss of
fly to human and play a critical role in cellular memory by repressing apico-basal cell polarity and of the ELAV differentiation marker (Fig. 1c–e
developmental genes throughout development36. PcG dysregulation and Extended Data Fig. 1g–i). These tumours show normal concentra-
leads to cell fate changes37, developmental transformations and is tions of PH protein in L3 EDs, both at day 9 (transient ph-KD d9) and day
1Institute of Human Genetics, CNRS, University of Montpellier, Montpellier, France. 2Research Institute of Molecular Pathology, Vienna BioCenter, Vienna, Austria. 3University of Southern
California, Los Angeles, CA, USA. 4Institute of Gene Biology, Russian Academy of Sciences, Moscow, Russia. 5Semmelweis University Department of Bioinformatics, Budapest, Hungary.
6Department of Biophysics, Medical School, University of Pécs, Pécs, Hungary. 7Department of Biological Hematology, CHU Montpellier, Montpellier, France. 8UFR Medicine, University of
Montpellier, Montpellier, France. 9These authors contributed equally: V. Parreno, V. Loubiere. ✉e-mail: anne-marie.martinez@igh.cnrs.fr; giacomo.cavalli@igh.cnrs.fr
Nature | www.nature.com | 1
Article
a b
FRT FRT act STOP Gal4
FLP Gal4 Gal80ts
eyflippase act Gal4 tubGal80ts
18 ºC
No ph-KD UAS GFP UAS ph RNAi d 29 ºC ph-KD UAS GFP UAS ph RNAi GFP ph RNAi
e
11 (transient ph-KD d11) after egg laying (AEL) (Fig. 1b and Extended Data whole cancer genomes by collecting eggs from several independent
Fig. 1c,d). EDs continue to grow after PH recovery (Fig. 1e) and cannot crosses of mated females and subjecting them to transient KD, constant
differentiate (Extended Data Fig. 1i), suggesting that the tumour state KD or no ph-KD (control condition), before sequencing their genomic
is stable and maintained independently of its epigenetic trigger. Like- DNA (gDNA). In total, we sequenced four independent control samples
wise, PH depletion at L2 or early L3 stage induces tumours (Extended as well as 12 independent tumour samples (Methods). When using
Data Fig. 1g–i), suggesting that PRC1 is required throughout develop- batch-matched control tissues (no ph-KD) to identify single nucleotide
ment to prevent tumorigenesis. Transient depletion of PSC-SU(Z)2, variants (SNV) or small insertions and deletions (InDels)46, we found that
another core PRC1 subunit for which null mutations drive neoplastic 68.1% of the identified variants are present in only one of the samples
transformation44, is also sufficient to induce tumorigenesis (Extended and that 7 out of 12 tumour samples contained fewer SNVs or InDels
Data Fig. 1j–m). than at least one of the control samples (Extended Data Fig. 2a), ruling
Transient PH depletion induces tumours with 100% penetrance out that PH depletion induces a massive increase in mutation rates and
within 2 days, as illustrated by the early L3 PH depletion experiment consistent with previous data47. Moreover, 92.8% of the identified SNVs
(Extended Data Fig. 1g–i). To assess whether such tumours may arise or InDels had an allele frequency below 0.2, precluding them from
from a clonal subpopulation of cells, we performed EdU (5-ethynyl- driving whole-tissue tumours (Fig. 1g). Regarding SNVs or InDels with
2′-deoxyuridine) staining after 24 h ph-KD in early L3 EDs (Fig. 1f and an allele frequency higher than 0.2, none of them was shared among
Supplementary Videos 1 and 2). Aberrant replication was observed the 12 tumour samples (Fig. 1h). Instead, 89% were found in only one
throughout the tissue within 24 h, indicating that most or all cells sample and the 217 variants shared between at least two tumours had
undergo malignant transformation. For DNA mutations to drive these similar feature distributions compared to the variants found in control
tumours, they should simultaneously occur in many cells to trigger samples, without bias towards exons (Fig. 1i). No genes contained del-
overproliferation in the whole tissue. Given the low frequency of dele- eterious SNVs or InDels in all tumour samples, and similar results were
terious mutations per cell generation (about 1.2 per genome45) and found when considering structural variants or copy number variations
the limited number of genes that can act as cancer drivers in Dros- (CNVs) (Fig. 1h and Methods). Together, these results argue strongly
ophila46, this scenario seemed unlikely. Nevertheless, we sequenced against the presence of recurrent driver mutations in these tumours.
2 | Nature | www.nature.com
ytiraloP
htworG
Development Constant Transient ph-KD stage ph RNAi No ph-KD ph-KD Day 9 Day 11
Embryo – + – – FF--aaccttiinn L1 – + + +
L2 – + – –
L3 – + – – kDa
PH 170
Tubulin 52 Apical Apical Apical Apical
f
4
3
2
1
)501×,2mμ(
aera
DE
P = 4 × 10–7 **** DK-etihw
DK-hp
0 h after 24 h after
24 h KD 24 h KD
EdU
12
SNV or InDel allele frequency
ytisneD
h SNVs or InDels
g 92.8% 7.2%
36,627 2,835 6
0
0 0.2 0.4 0.6 0.8 1.0
selpmas
ruomut
fo noitcarF
Genes SVs CNVs
89.4% 85.1% 93.4% 78.7% n = 1,833 n = 57 n = 23,063 n = 6,296 1/12 2/12 161 7 1,331 1,129
3/12 37 3 227 357
4/12 13 0 49 137
5/12 5 0 10 48
6/12 1 0 1 24
7/12 0 0 0 9 8/12 0 0 0 2
9/12 0 0 0 0 10/12 0 0 0 1 11/12 0 0 0 0
12/12 0 0 0 0
0 1,000 0 2040 0 15,000 0 5,000 Number of alterations
100 Downstream Exonic 80 Intergenic 60 139 115 I n n c t R ro N n A ic _exonic
40 ncRNA_intronic Upstream 20 81 42 Upstream;downstream
UTR3 0 26 23 UTR5
)%( sleDnI
ro sVNS
c
i j llec
rep icof
vA2H(cid:74)
N C o o T n p r s h a t - a n K n s T D i t e r p a n h n t - s p K ie h D n -K t D ph d - 9 KD d11
P = 2 × 10–15 ****
P = 3 × 10–11 ****
P = 3 × 10–4
***
N C o o
p
n
h
T s
-
r t a
K
a n n
D
s t i
p
T en r
h
a t
-
n
K
p s
D
h ie
-K
nt
D
p
d
h
9 -KD d11
P = P 7 = × × 4 0 1 × × . 0 5 3 1 – 7 . 3 1 0 1 7 –6 ** * * * * ** × P ** 0 = * .6 * 6 4 × 10–31 12
9 6
3 0
Any ≥2 tumour 0′ 30′480′ 0′ 30′480′
control samples
n =
20
n
2
=
6
n
9
=
107
n =
113
n =
77
n =
94
No ph-KD Transient ph-KD
Fig. 1 | Transient PRC1 depletion is sufficient to initiate tumours. a, Scheme imaged at 0 h (left) and 24 h (right) after 24 h of w-KD (control, top) or ph-KD
depicting the conditional ph-KD system (Methods). b, Western blot analysis of (bottom). g, Distribution of somatic SNVs or InDel allele frequencies detected
PH protein concentrations in the EDs of L3 larvae subjected to no ph-KD in all samples. h, Number of tumour samples in which each SNVs or InDels, gene
(control), constant or transient ph-KD at L1 stage. c, Representative confocal with deleterious SNVs or InDels, structural variants (SVs) and CNVs were found.
images of F-actin staining (red) showing a polarized epithelium with apical i, Feature distribution of SNVs or InDels found in any of the control samples
F-actin (xz cross-sections at the bottom) in no ph-KD (control, left), whereas (no ph-KD, left bar) or shared between at least two tumour samples (right bar).
polarity is disrupted on constant or transient ph-KD EDs (dissected at L3 stage). j, Number of γH2Av foci per cell before (0 min; indicated as 0′) and after (30 and
DNA is stained with DAPI (blue). d,e, DAPI staining (d) is used to measure ED 480 min, indicated as 30′ and 480′) exposure to 5 Gy irradiation in control (no
areas (e) under no ph-KD (control), constant or transient ph-KD conditions ph-KD, left) or transient ph-KD EDs (right). Individual data points are shown in
(n = 30 EDs per condition; two-sided Wilcoxon test: ***P < 1 × 10−3, ****P < 1 × 10−5; grey and bars correspond to the mean ± standard error (whiskers). Two-sided
box plots show the median (line), upper and lower quartiles (box) ±1.5× t-test ****P < 1 × 10−5. Scale bars, 10 μm (c), 100 μm (d,f).
interquartile range (whiskers); outliers are not shown). f, EdU staining (green)
a b
4
2 0
–2
–4
d e
To test whether transient PH depletion could induce genome insta-
JAK–STAT signalling activation in EICs
bility, we counted the number of phospho-H2AvD foci (γH2Av) per
cell in control (no ph-KD) and transient ph-KD tumours before and We compared the transcriptomes of the control condition (no ph-KD),
during a time course after irradiation. Despite a slightly higher num- transient and constant ph-KD tumours to temperature-matched con-
ber of foci before irradiation, probably due to the higher fraction of trols, generated with a similar RNAi system targeting the white (w)
cells engaged in DNA replication, tumour and control samples showed gene, which is dispensable for normal eye development (differen-
a similar decrease in the number of γH2Av foci between 30 and 480 min- tial transcriptome analyses are available in Supplementary Table 1).
utes after irradiation (Fig. 1j and Extended Data Fig. 2b,c), suggesting As expected, the ph-RNAi and the w-RNAi lines are hardly distinguish-
that these tumours can efficiently repair DNA breaks to prevent the able at 18 °C, as well as in the transient w-KD condition (Fig. 2a and
accumulation of mutations. Finally, karyotype analysis of the tumours Extended Data Fig. 3a). Consistent with our previous work41,42, constant
collected on transient ph-KD did not show significant differences in ph-KD is associated with the upregulation of 340 genes—including
chromosomal rearrangements compared to control samples (Extended canonical PcG targets such as Hox and developmental transcription
Data Fig. 2d). factor genes—and the down-regulation of 2,110 genes, including
In summary, transient depletion of PRC1 components is sufficient to most key regulators of ED development (Fig. 2a and Extended Data
switch cells into a neoplastic state that is maintained even after normal Fig. 3b). Only a subset of these genes was also differentially expressed
PcG protein concentrations are re-established. As the same genotype in transient ph-KD at d9 AEL (256 and 812, respectively), and even less
can generate both a normal phenotype or a tumour depending on a at later d11 AEL (154 and 446, respectively), suggesting a progressive
transient gene regulatory modification in the absence of DNA driver yet incomplete rescue of the transcriptome (Fig. 2a and Extended Data
mutations, we defined these tumours as epigenetically initiated can- Fig. 3a–c). Therefore, most (75%) of the transcriptional defects observed
cers (EICs). on constant ph-KD can be restored on reinstating normal levels of PH.
Nature | www.nature.com | 3
egnahc
dloF
)gol( 2
Upregulated Reversible (n = 184) Unaffected Irreversible (n = 174)
Downregulated Transient-specific (n = 171)
Down 1 (n = 420)
Down 2 (n = 547)
Down 3 (n = 1,092)
seneg
fo rebmuN
)DK-w
dehctam-erutarepmet
susrev(
c
35 340 256 154 Unaffected NS 3 . ( 5 P % = 1)
251 **** Reversible 22.8% (P = 1 × 10–16)
**** 1,633 Irreversible 17.2% (P = 5 × 10–9) 2,101
2,641 Transient-specific 12 * . * 3 * % (P = 1 × 10–4)
2,110 *** Down 1 9.3% (P = 1 × 10–4)
*** Down 2 8.8% (P = 1 × 10–4)
25 812 446 Down 3 7 * .7 ** % (P = 4 × 10–5)
No ph- C K o D nstant T p r h a - n K s D ient p T h r - a K n D s ie d n 9 t ph-KD d11 Constant T p r h a - n K s D ient p T h r - a K n D s ie d n 9 t ph-KD d11 enr P ic c h G m 1 t e a n rg t e ( 3 o t d g d e s n 6 e ra s tio)
Fold change (log) PcG targets Unbound 2 PcG
target
Posterior head segmentation FDR (−log ) –4 –2 0 2 4
Head segmentation 12 10
Anterior/posterior pattern specification, imaginal disc upd1 0 0.6 2.9 2.4 +
Cell fate specification 8
DN An A t - e b r i i n o d r/ i p n o g s t t r e a r n io s r c p rip at t t io e n rn f a s c p t e o c r i fi a c c a ti t v io it n y 4 Ligands upd2 –0.3 4.3 5.5 5.1 +
Segmentation
N C e e u ll r f o a n te d c if o fe m re m n i t t i m at e io n n t OR 6 (log 2 ) upd3 0 4.7 5.6 5.4 +
Paracrine signalling 4
Cytokine activity 2 Receptor dome 0 0.2 0.4 0.3 –
Receptor signalling pathway by JAK−STAT
Regulation of cell population proliferation
Compound eye cone cell differentiation NR TyrK hop 0 0 –0.1 –0.1 –
Eye photoreceptor cell fate commitment
Eye photoreceptor c E e y l e l d d if e fe ve re lo n p ti m at e io n n t TF Stat92E 0 0.6 0.1 –0.1 –
Eye−antennal disc morphogenesis
DNA replication zfh1 0 0.6 2.2 1.8 +
DNA recombination
DNA repair
Cellular response to calcium ion Target genes chinmo 0 2 1.5 –0.3 +
Dopamine secretion
Synaptic signalling
Structural constituent of cuticle Socs36E 0 0.9 0.7 0.6 –
Transmembrane transporter activity
R T e r v a I e r n r r s e s i v e ib e n l r e t s - i s b p le ec D ifi o c w G D n o e 1 w n D n e o 2 R w T c e r n a v l I u e n 3 rr r s s e s i v e i t b e n e l r t e r s -s ib p le ec D ifi o c w D n o 1 w D n o 2 wn 3 No p C h o -K ns D tan T t r a p n h s - i K e D nt p T h r - a K n D s i d en 9 t ph-KD d11
Fig. 2 | EICs show irreversible transcriptional changes. a, Alluvial plot showing domain in control condition). One-sided Fisher’s exact test P values were
differentially expressed genes after no ph-KD (control), constant and transient corrected for multiple testing using FDR: ***FDR < 1 × 10−3, ****FDR < 1 × 10−5; NS,
ph-KD. Transitions between upregulated (orange), unaffected (grey) and P > 0.05. d, Representative Gene Ontology terms enriched for each gene cluster,
downregulated (blue) states are indicated by thin lines of the same respective further stratified as being direct PcG targets (left) or not (right). The full chart is
colours. b, Clustering of differentially expressed genes after constant or available in Extended Data Fig. 3d. e, Transcriptional fold changes of genes
transient ph-KD. c, Over-representation of direct PcG target genes (defined as involved in the JAK–STAT signalling pathway on ph-KD. Direct PcG targets (+)
more than or equal to 50% of the gene body overlapping a H3K27me3 repressive are indicated in the right column.
Article
Hierarchical clustering of differentially expressed genes identi- PH and CUT&RUN for several histone marks after no ph-KD (control),
fied three clusters that are upregulated in at least one condition, and constant and transient ph-KD. Whereas most reversible and irrevers-
three downregulated clusters (Fig. 2b; clustering results available in ible genes lost the H3K27me3 repressive mark on constant ph-KD,
Supplementary Table 2 and Methods). The upregulated clusters show H3K27me3 domains were notably recovered after transient ph-KD
stronger and significant over-representation of PcG target genes cov- (Fig. 3b,d). Most H3K27me3 domains and overlapping PH peaks are
ered with H3K27me3 in control EDs (Fig. 2c). This suggests that their erased on constant PH depletion, but are recovered after transient
upregulation is a direct consequence of compromised PcG repres- depletion (Extended Data Fig. 4b). The same applies to the H2AK118Ub
sion, although they retain distinct patterns. The ‘reversible’ cluster repressive mark deposited by PRC1 (Fig. 3d and Extended Data Fig. 4b).
includes canonical PcG target genes such as en, eve, Ubx and Scr, that H3K27me3 loss on constant ph-KD is accompanied by a reciprocal gain
are upregulated on constant ph-KD but recover control levels of expres- of H3K27Ac peaks, its activating counterpart, at both reversible and
sion after transient ph-KD, precluding them from being required for irreversible genes (Fig. 3c,d). Nevertheless, both groups show similar
the maintenance of EICs (Fig. 2b and Extended Data Fig. 3b). The same H3K27me3 and H3K27Ac levels after transient ph-KD, suggesting that
is true for ‘transient-specific’ genes, whose upregulation is dispensable comparable chromatin landscapes may promote distinct transcrip-
for tumour growth after constant ph-KD. tional outcomes (Extended Data Fig. 4a). Inspection of individual loci
The ‘irreversible’ cluster is of particular interest, as it contains a showed that recovery of chromatin composition is similar at the level of
high fraction of PcG target genes that remain upregulated despite PH reversible and irreversible genes, as evidenced by the upd locus, which
restoration and therefore represents candidate genes involved in the does not contain H3K27Ac peaks after transient ph-KD although it is
development of EICs (Fig. 2b,c). Whereas PcG target genes from the irreversibly upregulated (Figs. 2e and 3d).
reversible and irreversible clusters share ontologies associated with Nevertheless, we noted some exceptions, such as the zhf1 gene that
developmental transcription factors, irreversible genes show specific retains low but significantly higher levels of H3K27Ac compared to
enrichments for paracrine signalling and cytokine activity (Fig. 2d control tissues on transient depletion of PH (Fig. 3d), suggesting that a
and Extended Data Fig. 3d), including the JAK–STAT ligands (upd1, fraction of irreversible loci might retain small quantitative differences.
upd2, upd3), which were shown to be associated with various tumours, Differential analyses indicated that most H3K27me3 domains showed
including those depending on PcG mutations43,44,48 (Fig. 2e). In addi- a steep decrease on constant ph-KD but overall recovered to normal
tion, chinmo and zfh1 are direct PcG targets that have been described levels under transient conditions (Fig. 3e). Similar trends were found
to act downstream of the JAK–STAT pathway49 and are accordingly at H3K27Ac peaks and H2AK118Ub domains, whereby transient ph-KD
upregulated on PH depletion (Fig. 2e). The transcriptional repressor showed weaker and fewer significant differences compared to constant
ZFH1 is of particular interest, because it remains upregulated at d11 ph-KD (Fig. 3f and Extended Data Fig. 4c, respectively). This approach
AEL, is known to be involved in self-renewal and tumour growth50–52 again identified the zfh1 locus as an outlier showing significantly
and is conserved in mammals, in which its homologue ZEB1 can induce increased H3K27Ac peaks after transient ph-KD (Fig. 3f). To precisely
epithelial-to-mesenchymal transition53. Consistent with its transcrip- assess whether small differences in terms of H3K27me3 or H3K27Ac fold
tional upregulation, ZFH1 protein is increased on constant PH depletion changes would be predictive of irreversible transcriptional changes, we
and even more on transient PH depletion (Extended Data Fig. 3e,f), classified H3K27me3 domains based on whether they contain irrevers-
suggesting that it might support the development of EICs. ible or reversible genes and interestingly found that genes from the two
Finally, we noted that irreversible genes that are not PcG targets are groups are usually found in different domains (Extended Data Fig. 4d).
enriched for Gene Ontology (GO) terms related to DNA replication Domains overlapping irreversible versus reversible genes showed small
and repair (Fig. 2d and Extended Data Fig. 3d), suggesting that their differences in H3K27me3 or H3K27Ac fold changes (Fig. 3g,h), which
upregulation may be a consequence of the proliferation of tumour are unlikely to explain the clear-cut difference between reversible and
cells. Together, these results indicate that EICs are driven by a restricted irreversible genes. Therefore, irreversible transcriptional changes drive
set of irreversibly upregulated genes, including major members of the tumorigenesis despite the re-establishment of an essentially normal
JAK–STAT signalling pathway, rather than by the vast pleiotropic dys- chromatin landscape at PcG target genes.
regulation of cancer genes that is observed on constant PH depletion.
Therefore, we sought to investigate why this subset of genes remains
Heritable chromatin accessibility changes
irreversibly upregulated after restoration of normal PH levels and to
test whether they are required for the development of EICs. For simplic- The analysis of PH binding levels at PH peaks located ±25 kb from the
ity, unless explicitly stated, further investigations of transient ph-KD transcription start sites (TSS) of reversible (n = 113) or irreversible
EDs were conducted on tissues collected at d11 AEL after a 24 h KD at (n = 91) genes revealed no significant differences either in control
the L1 stage, representing the condition with the smallest number of EDs (no ph-KD) or after transient ph-KD (Extended Data Fig. 4e). This
differentially expressed genes. is consistent with the levels of H3K27me3 and H2AK118Ub repressive
marks, which are also similar (Extended Data Fig. 4a). We therefore won-
dered whether the irreversible transcriptional changes found in EICs
Chromatin analysis at irreversible genes
might be due to the binding of specific transcription factors to specific
To identify their unique chromatin features, we focused on irreversible chromatin targets on ph-KD, preventing re-repression on restoration
(n = 30) and reversible (n = 42) genes that are direct PcG targets and are of PH. In this scenario, one would expect the opening of specific sites at
covered with the H3K27me3 repressive mark in control EDs (for a full irreversible gene loci. To test this hypothesis, we performed ATAC-Seq in
list of PcG target genes, see Supplementary Table 2). Both groups show control EDs (no ph-KD) or after constant or transient ph-KD, and found
similar H3K27me3 levels in control tissues (Extended Data Fig. 4a), 1,220 reversible peaks showing a stark increase in accessibility after
where they are transcribed at similarly low levels (Fig. 3a). They are constant PH depletion but returning to normal levels after transient KD
also induced at comparable levels on constant ph-KD, ruling out the (Fig. 4a). By contrast, 446 ATAC-Seq peaks increased accessibility both
possibility that weaker PcG repression and/or higher transcriptional on constant as well as on transient PH depletion (Fig. 4a). We named
levels are the reason for irreversible genes being unable to recover these ATAC-Seq regions irreversible peaks (clusters are fully available
normal transcription after transient ph-KD (Fig. 3a). in Supplementary Table 3).
We then explored the possibility that chromatin might not be cor- To assess whether reversible and irreversible peaks correlate
rectly re-established at irreversible genes in EICs, by performing chro- with transcriptional changes, we assigned them to the closest TSS
matin immunoprecipitation combined with sequencing (ChIP–seq) for (±25 kb, Methods). Reversible and irreversible ATAC-Seq peaks were
4 | Nature | www.nature.com
a b c
Overlaps H3K27me3 domain
PcG-bound unaffected genes (n = 337)
PcG-bound irreversible
genes (n = 30)
PcG-bound
reversible
genes (n = 42)
d Irreversible Reversible
No ph-KD100 25 kb 10 kb 25 kb 10 kb
PH Constant ph-KD100
Transient ph-KD350
No ph-KD18
H3K27me3 Constant ph-KD24
Transient ph-KD15
No ph-KD15
H2AK118Ub Constant ph-KD15
Transient ph-KD15
No ph-KD10
H3K27Ac Constant ph-KD10
Transient ph-KD10
upd2 upd3 upd1 zfh1 inv wg
e g
f h
significantly associated with the reversible and irreversible genes iden- after transient ph-KD and is surrounded by several promoter-distal
tified by RNA sequencing (RNA-seq) analysis in Fig. 2b, respectively irreversible ATAC-Seq peaks, whereas the reversible gene Ubx shows
(Fig. 4b). This suggests that a substantial fraction of these peaks might reversible ATAC-Seq peaks that can be observed only on constant ph-KD
correspond to enhancer elements that activate the transcription of (Fig. 4d). In parallel, 604 peaks show reduced accessibility and are
cognate TSSs from a distance. Consistently, roughly 70% of reversible associated with downregulated genes (Figs. 2b and 4a,b).
and irreversible peaks are found more than 1 kb away from the closest To understand which transcription factors might cause these differ-
TSS (Fig. 4c,d). For example, the upd3 gene is irreversibly upregulated ences in accessibility, we searched for DNA binding motifs in ATAC-Seq
Nature | www.nature.com | 5
seneg
fo
rebmuN
Overlaps H3K27Ac peak
Reversible
40
Irreversible 30
20
10
0
seneg
fo
rebmuN
Reversible
40
Irreversible 30
20
10
0
Constant ph-KD
4
2
0
−2
−4
baseMean (log )
10
)gol(
egnahc
dlof
cA72K3H
2 Up (305) Transient ph-KD Unaffected (5,179) 4
Down (281)
2
0
−2
−4
1.5 2.0 2.5 3.0 3.5 4.0
baseMean (log )
10
)gol(
egnahc
dlof
cA72K3H
2
Constant ph-KD 4
2
0
−2
−4
baseMean (log )
10
Up (4) Unaffected (5,761)
Down (0)
1.5 2.0 2.5 3.0 3.5 4.0
)gol(
egnahc
dlof
3em72K3H
2 Transient ph-KD Up (13) 4 Unaffected (97)
Down (190) 2
0
−2
−4
1.5 2.5 3.5 4.5
baseMean (log )
10
)gol(
egnahc
dlof
3em72K3H
2 Up (1) Unaffected (284)
Down (15)
upd1–3
upd1–3
zfh1
zfh1
1.5 2.5 3.5 4.5
3
zfh1 zfh1 2
1
0 −1
)gol(
egnahc
dlof
cA72K3H
2
0
−1
−2
−3
NS NS
H3K27Ac peaks
within H3K27me3
domains
Constant Transient
ph-KD ph-KD
)gol(
egnahc
dlof
3em72K3H
2
80
60
40
20
0
NS
H3K27me3 domains
All (n = 264)
Overlapping
irreversible
gene(s) (n = 27)
Overlapping
reversible
gene(s) (n = 36)
Constant Transient
ph-KD ph-KD
MKPF
qes-ANR
NS
P = 1 × 10–11****
P = 1 × 10–7****
P = 5 × 10–2* NS
P = 3 × 10–2* P = 2× 10–2* NS P = 6× 10–4***
No
ph-
C
K
o
D
nstant
ph-
T
K
ra
D
nsient
ph-KD
C N o o n s
p
t
h
a T
-
n
K
r t a
D
n
p
s
h
i
-
e
K
n
D
t
ph-K
C N
D
o o n s
p
t
h
a T
-
n
K
r t a
D
n
p
s
h
i
-
e
K
n
D
t
ph-KD
C N o o n s
p
t
h
a T
-
n
K
r t a
D
n
p
s
h
i
-
e
K
n
D
t
ph-K
C N
D
o o n s
p
t
h
a T
-
n
K
r t a
D
n
p
s
h
i
-
e
K
n
D
t
ph-KD
P = 2× 10–8**** P = 1× 10–3** P = 3× 10–5*** P = 1× 10–6**** P = 1× 10–2*
P = 2× 10–8**** P = 3× 10–9****
P = 7× 10–7****P = 9× 10–9****
All (n = 424)
Overlapping
irreversible
gene(s) (n = 72) Overlapping
reversible gene(s) (n = 126)
Fig. 3 | PcG repressive landscape is restored after transient ph-KD. average-normalized counts across all samples (baseMean) for constant (left) or
a, Fragments per kilobase of transcript per million mapped reads (FPKM) of transient (right) ph-KD conditions. Significant changes are highlighted using a
irreversible (pink), reversible (green) and unaffected (grey) genes that are colour code (colour legend). g, The H3K27me3 fold changes (between constant
direct PcG targets. Two-sided Wilcoxon test: *P < 5 × 10−2, ***P< 1 × 10−3, or transient ph-KD and no ph-KD conditions) at H3K27me3 domains that are
****P < 1 × 10−5, NS, P > 0.05. Box plots show the median (line), upper and lower found in the control sample (no ph-KD) and overlap irreversible (pink) or
quartiles (box) ±1.5× interquartile range (whiskers), outliers are not shown. reversible (green) genes. All H3K27me3 domains are shown for reference (grey).
b, Number of irreversible (pink) and reversible (green) genes overlapping an Two-sided Wilcoxon test: *P < 5 × 10−2, **P < 1 × 10−2, ***P < 1 × 10−3, ****P < 1 × 10−5,
H3K27me3 domain (more than or equal to 50% of the gene body) after no ph-KD NS, P > 0.05. Box plots show the median (line), upper and lower quartiles (box)
(control), constant or transient ph-KD. c, Number of irreversible (pink) and ±1.5× interquartile range (whiskers), outliers are not shown. h, The H3K27Ac
reversible (green) genes overlapping at least one H3K27Ac peak (in the gene fold changes at H3K27Ac peaks overlapping the H3K27me3 domains found in
body or up to 2.5 kb upstream of the TSS) after no ph-KD (control), constant or control sample (no ph-KD) and overlapping the irreversible (pink) or reversible
transient ph-KD. d, Screenshot of PH ChIP–seq, H3K27me3, H2AK118Ub and (green) genes. All H3K27Ac peaks overlapping control H3K27me3 domains
H3K27Ac CUT&RUNs tracks at representative irreversible (left) or reversible are shown for reference (grey). Two-sided Wilcoxon test: ****P <1 × 10−5, NS.
(right) loci under the indicated conditions (left). e,f, For H3K27me3 domains P > 0.05. Box plots show the median (line), upper and lower quartiles (box)
(e) and H3K27Ac peaks (f), fold changes are shown as a function of their ±1.5× interquartile range (whiskers), outliers are not shown.
Article
a
c
Irreversible (n = 446) Fold
change
(log)
2
Reversible (n = 1,220)
Decreased (n = 613)
peaks. Reversible and irreversible peaks show distinct motif signatures constant PH depletion but not in a transient condition (Fig. 4f and
(Fig. 4e). Reversible peaks are enriched for Abd-B, cad and eve motifs, Extended Data Fig. 5a), suggesting that their effect on chromatin
three different PcG canonical targets involved in antero-posterior pat- and transcription is dispensable for the growth of EICs. Conversely,
terning that are strongly upregulated after constant ph-KD compared STAT92E and ZFH1 motifs were among the best predictors of increased
to transient ph-KD (Extended Data Fig. 3b). By contrast, irreversible and decreased accessibility after transient ph-KD, respectively
peaks are enriched for Jra and kay motifs, the Drosophila homologues (Fig. 4f,g).
of AP-1, which are the main transcription factors of the oncogenic JNK
signalling pathway54. Furthermore, they were strongly and specifically
enriched for Stat92E motifs, the key effector of the JAK–STAT pathway55. Tumorigenesis requires STAT92E and ZFH1
Finally, decreased peaks are enriched in glass (gl) and sine oculis (so) To assess whether the STAT92E activator and the ZFH1 repressor are
motifs, two key regulators of eye development that are irreversibly necessary for the development of EICs, we set up dual RNAi systems
downregulated (the down 1 cluster in Fig. 2b and Extended Data Fig. 3b). allowing the depletion of each of the two factors in combination with
This latter point indicates that the activation of the retinal determina- white or ph. As a control, we combined gfp (green fluorescent protein)
tion gene network is compromised in the absence of PcG, consistent and white-RNAi (gfp + w-KD), which had no impact on ED growth or dif-
with our previous work42. ferentiation, whereas gfp+ph-KD induced tumours as expected (Fig. 5a
These results indicate that the Abd-B, cad and eve genes are respon- and Extended Data Fig. 5b). Both on constant and on transient deple-
sible for the pleiotropic transcriptional defects observed on constant tion, Stat92E and zfh1-KD alone had no visible effect. However, when
PH depletion, but are unlikely to be required for the progression of combined with ph-KD, they both significantly reduced ph-dependent
EICs. On the other hand, recruitment of AP-1 and STAT92E at irre- tumour growth and partially restored cell polarity and photoreceptor
versible peaks could maintain irreversible genes in an active state, differentiation (Fig. 5a and Extended Data Fig. 5b–f), indicating that
potentially by maintaining open chromatin at their cis-regulatory they are both bona fide drivers of the tumour phenotype. These res-
regions. To tackle this latter point, we sought to predict ATAC-Seq cues are also associated with an overall rescue of constant gfp + ph-KD
changes using transcription factor motif counts (Methods). cad transcriptomes, with 50% of differentially expressed genes returning
and Abd-B motifs are associated with increased accessibility after to control levels on gfp+zfh1-KD (Fig. 5b). Consistent with previous
6 | Nature | www.nature.com
)%(
skaep
latsid-SST bk 1>
d et c eff a n U
el bisr ev errI
RD ee el bisr ev
d es a er c
60
40
20
0
so 14.1 Normalized gl 5.9 e sc n o ri r c e hment
peb 5.7 6 Abd-B 6 4 eve 5.6
2 Nf-YA 5.5 0 Nf-YB 5.6 cad 6.3 cnc 6.2 Stat92E 7.7 kay 5.5 Jra 5.8
mor 5.9
elbisreverrI elbisreveR desaerceD
**** 6
Irreversible 4 2 0
**** 4 Reversible 2 *** 0
RNA-seq cluster
oitar sddO **** **** 4 Decreased 2 *
0 -tneisnarT cfiiceps elbisreverrI elbisreveR 1
nwoD
2
nwoD
3
nwoD
d
ATAC-Seq 10 kb
25
No ph-KD
25
Constant ph-KD
25
Transient ph-KD
upd3 Ubx
e f g
b
NS NS
NS NS NS
t value transient ph-KD ATAC-Seq fold change
egnahc
dlof qeS-CATA
DK-hp tnatsnoc eulav
t
ytilibissecca
desaercnI
ytilibissecca desaerceD
Stat92E
cad 10 Abd-B 1.0
0.5 CG11085 Mes2 0 5 cnc gsbtrh mor –0.5
dan 0 1 2 ≥3 zfh1 ab grn 0 usp tgo ftz-f1 chinm g o rh Stat92E zfh1 sna ovofru –5 RunxAken nu b b r lola v C v f l 2Ubx 1.0 ttk 0.5 hth peb 0
–10 –0.5
–10 –5 0 5 10 0 1 2 ≥3
Decreased accessibility Increased accessibility
Motif counts
)gol(
DK-hp
tneisnart egnahc dlof qeS-CATA
2
n = 8, n 4 9 = 9 2,0 n 7 1 = 7 n 8 1 = 263
n
=
7,
n
5 5
=
2 2,9
n
2 8 = 8
n
3 5 = 299
errI ev bisr el R e ev bisr el D e c er a es d
2
1 0
−1
−2
Const
p
a
h
n
-
t KD Trans
p
ie
h
n
-
t KD
P = 7× 10–3 **
P = 1× 10–32 ****
Fig. 4 | Chromatin accessibility changes underlie reversible and irreversible upd3 gene (left) and the reversibly upregulated Ubx gene (right). e, Normalized
transcriptional changes. a, Clustering of ATAC-Seq peaks showing significant enrichment scores of DNA binding motifs found at each cluster of ATAC-Seq
changes after constant or transient ph-KD. b, Over-representation of genes peaks (±250 bp, x axis). f, Linear model t values of DNA binding motifs associated
associated with irreversible (top), reversible (middle) or decreased (bottom) with increased (positive t values) or decreased (negative t values) accessibility
ATAC-Seq peaks, for each of the six RNA-seq clusters defined in Fig. 2b. One- after transient (x axis) or constant ph-KD (y axis). Only motifs with a significant
sided Fisher’s exact test P values were corrected for multiple testing using FDR: P < 1 × 10−5 in at least one of the two linear models are shown. g, Fold changes at
*FDR < 5 × 10−2, ***FDR < 1 × 10−3, ****FDR < 1 × 10−5, NS, P > 0.05. Exact FDR values: ATAC-Seq peaks (y axis) on transient ph-KD, as a function of the number of
2 × 10−1, 4 × 10−23, 1 × 10−1, 1 × 100, 1 × 100, 1 × 100 (irreversible); 4 × 10−1, 2 × 10−5, Stat92E (left, in orange) or zfh1 (right, in blue) motifs that they contain (x axis).
2 × 10−34, 1 × 100, 1 × 100, 3 × 10−1 (reversible), 8 × 10−2, 1 × 100, 1 × 100, 2 × 10−21, Two-sided Wilcoxon test: **P < 1 × 10−2, ****P < 1 × 10−5. Box plots show the median
5 × 10−32, 1 × 10−2 (decreased). c, Fraction of TSS-distal peaks per cluster (greater (line), upper and lower quartiles (box) ±1.5× interquartile range (whiskers),
than 1 kb). d, Screenshot of ATAC-Seq tracks after no ph-KD (control, top), outliers are not shown.
constant (middle) or transient (bottom) ph-KD, at the irreversibly upregulated
a b
studies showing that zfh1 is a target of STAT92E (ref. 50), the zfh1 gene
EICs are autonomous immortal tumours
returned to control levels in Stat92E+ph-KD (differential analyses are
available in Supplementary Table 4). Thus, ZFH1 seems to play a master Most EIC-bearing larvae die after day 11 AEL, preventing the study of
role in shaping the tumour transcriptome. tumour development over time. To circumvent this limitation, allo-
Therefore, we sought to investigate its impact on chromatin by per- grafts of imaginal disc tissue into the abdomen of adult Drosophila
forming comparative ATAC-Seq experiments in gfp+ph-KD, gfp+zfh1-KD hosts are commonly used to assess the tumorigenic potential of a
and zfh1+ph-KD. Consistent with our previous result showing that tissue, and we previously showed that ph mutant EDs continuously
zfh1 motifs are associated with decreased accessibility in tumours grow until they eventually kill the host43. To be able to track trans-
compared to control tissues (Fig. 4g), zfh1-KD in combination with planted EICs, we developed a variant of our thermosensitive system
ph-KD was found to be associated with the reopening of roughly that constitutively expresses GFP in the eye, whereas an upstream
1,700 peaks showing decreased accessibility in gfp+ph-KD tumours activation sequence-red fluorescent protein (UAS-RFP) cassette can
(Fig. 5c). Moreover, zfh1 motif counts are predictive of an increase in be used as a reporter of continuing ph-KD (Extended Data Fig. 6a,f–i).
ATAC-Seq signal between gfp+ph-KD and zfh1+ph-KD tissues (Fig. 5d). This system induces EICs with similar penetrance, morphological
These results indicate that zfh1 represses transcription by reducing and transcriptional defects, showing that EICs can be obtained in
the accessibility of a subset of regulatory elements. Thus, we classi- different genetic backgrounds (Extended Data Fig. 6b–e). The dif-
fied ATAC-Seq peaks based on their fold change between gfp+ph-KD ferential analyses of the corresponding transcriptomes are available
and zfh1+ph-KD and assigned them to the closest TSS (±25 kb). Peaks in Supplementary Table 5. We then performed allografts using this
with increased accessibility on zfh1+ph-KD were associated with line (Extended Data Fig. 7), keeping host flies at a restrictive tem-
genes that were aberrantly downregulated on gfp+ph-KD (Fig. 5e) perature after transplant (18 °C) to preclude activation of ph-RNAi in
and are involved in eye development and differentiation (Fig. 5f), transplanted tissues.
reminiscent of the genes identified in the Down 1 RNA-seq cluster Constant ph-KD primary tumours grew in a high fraction of the
(Fig. 2b). injected host flies within 20 days of transplantation (Extended Data
Altogether, these results indicate a multistep model (Fig. 5g) in which Fig. 7a–c). Transient ph-KD primary EICs behaved similarly, indicating
transient disruption of PcG-mediated silencing irreversibly activates that their overgrowth results from an autonomous, stably acquired
the JAK–STAT pathway, which induces cell proliferation as well as the state (Extended Data Fig. 7a–c). To measure tumour growth over time,
zfh1 gene. In turn, ZFH1 represses genes required for ED development, we set up a scheme allowing us to trace the tumour of origin (Extended
thereby preventing cell differentiation in EICs. Data Fig. 7d). Tumours derived from both constant or transient PH
Nature | www.nature.com | 7
seneg
fo
rebmuN
dehctam-erutarepmet
susrev(
)DK-w+pfg
415 304 Up
692 Unaffected
Down 451
1,477 1,814
2,046 1,297
1,071
htworG
noitaitnereffiD
gfp+w-KD Stat92E+w-KD zfh1+w-KD gfp+ph-KD Stat92E+ph-KD zfh1+ph-KD
ELAV
d e
skaep
qeS-CATA
fo rebmuN
dehctam-erutarepmet
susrev(
)DK-w+pfg
311 Increased
Unaffected
1,549 Decreased
66
3,082
2,089
311
ZFH1 motif counts
)gol(
egnahc
dlof
qeS-CATA
2 DK-hp+pfg
susrev
DK-hp+1hfz
c
P = 1× 10–29**** ATAC-Seq changes f GO terms of genes associated
gfp+ph
S
-
t
K
at
D 92E+ph-K
z
D fh1+ph-KD gfp+ph-KD zfh1+ph-KD
zfh1+ph-KD versus gfp+ph-KD to rescued ATAC-Seq peaks
1
2
Decreased
P
×
**
1
=
*
0
9
–1
.2
0
P
E
h
y
C
e
o t
o
p
o
m
h
re
o
p
c
t
o
o
e
u
r
p
e
n
t
c
d
o
e
r
e
p
c
y
t
e
e
o
l l
r
p
d
d
(
d
≥
h
i
i
i
f
f
1
o
f
f
f
f
e
e
t
e
Z
o
r
r
r
e
e
F
r
e
e
n
n
H
n
c
t
t
t
1
i
i
e
i
a
a
a
p
m
t
t
t
i
i
t
i
o
o
o
o
o
n
n
n
r
tif)
FDR
g
Develop
ment
d
P
e
P
p
c
l
c
G
e
G
tion
Tum
origenesis
Unaffected Sensory organ morphogenesis (−log 10 ) restoration
0 P = 7.7 Eye morphogenesis 1.7 × 10–47 Cell fate commitment
–1 Increased **** Compound ey E e y m e o d r e p v h e o lo g p en m e e s n is t 1.5 Nucleosome N f o at r e m A al N f o at r e m B al T f u a m te o B ra ′ l T f u at m e o B ra ″ l
H3K27me3
0 1 2 ≥3 –8 –4 0 2 0 1 H3K27Ac Reversible
n = 9 n ,6 = 0 2 3,5 n 4 5 = 94 n 9 = 307 gf C p+ lo p s h e - s K t D g e v ( n l e o e r g s f u o ) s ld g c fp h + a w ng -K e D Od ( d lo s g r 2 a ) tio T S Z r F T a H A n T 1 s 9 c 2 ri E ption Irreversible
2 Other TFs Differentiation
Fig. 5 | Tumour development requires STAT92E and ZFH1. a, DAPI (top, in ****P < 1 × 10−5. Box plots show the median (line), upper and lower quartiles
grey) and neuronal differentiation marker ELAV (bottom, in magenta) stainings (box) ±1.5× interquartile range (whiskers), outliers are not shown. e, RNA-seq
of EDs after constant KD of the following components: gfp+w, Stat92E+w, fold changes on gfp+ph-KD (x axis) of genes associated with ATAC-Seq peaks
zfh1+w, gfp+ph, Stat92E+ph and zfh1+ph (top labels). Two independent that are decreased (in blue), unaffected (in grey) or increased (in orange) after
biological replicates were performed with similar results. Scale bars: 100 μm zfh1+ph-KD compared to gfp+ph-KD (y axis). Two-sided Wilcoxon test:
(DAPI), 10 μm (ELAV). b, Number of differentially expressed genes after gfp+ph- ****P < 1 × 10−5. Box plots show the median (line), upper and lower quartiles
KD (tumours), Stat92E+ph-KD and zfh1+ph-KD. Transitions between upregulated (box) ±1.5× interquartile range (whiskers), outliers are not shown. f, Top
(orange), unaffected (grey) and downregulated (blue) states are indicated by enriched Gene Ontology (GO) terms for genes associated with ATAC-Seq peaks
thin lines of the same respective colours. c, Number of ATAC-Seq peaks showing containing at least one ZFH1 motif and showing significantly increased
significant accessibility changes after gfp+ph-KD or zfh1+ph-KD. Transitions accessibility after zfh1+ph-KD compared to gfp+ph-KD. g, Schematic
between increased (orange), unaffected (grey) and decreased (blue) states are illustration showing that PcG depletion triggers an epigenetic switch to a
indicated by thin lines of the same respective colours. d, Fold changes at cancer fate. Resulting cancers persist after the PcG protein is restored, and
ATAC-Seq peaks between zfh1+ph-KD and gfp+ph-KD, depending on the their maintenance is associated with stable transcriptional changes supported
number of ZFH1 motifs they contain (x axis). Two-sided Wilcoxon test, by the STAT92E activator and the ZFH1 repressor.
Article
depletion maintained their ability to expand in host flies more than ten and competing interests; and statements of data and code availability
rounds of transplantation. Tumour growth penetrance, defined as the are available at https://doi.org/10.1038/s41586-024-07328-w.
percentage of host flies bearing GFP-positive cells 20 days after trans-
plantation, increased over generations of transplantation (Extended
1. McGranahan, N. & Swanton, C. Biological and therapeutic impact of intratumor
Data Fig. 7b), whereas the survival of host flies decreased (Extended
heterogeneity in cancer evolution. Cancer Cell 27, 15–26 (2015).
Data Fig. 7c,e,f). Furthermore, tumours metastasized to regions and 2. Vogelstein, B. et al. Cancer genome landscapes. Science 339, 1546–1558 (2013).
organs far from the injection site, with increasing penetrance with the 3. Brock, A., Chang, H. & Huang, S. Non-genetic heterogeneity—a mutation-independent
driving force for the somatic evolution of tumours. Nat. Rev. Genet. 10, 336–342 (2009).
number of transplants (Extended Data Fig. 7g,h). Finally, allografts
4. Flavahan, W. A., Gaskell, E. & Bernstein, B. E. Epigenetic plasticity and the hallmarks of
originating from tissues injected after a transient ph-KD at the late cancer. Science 357, eaal2380 (2017).
L3 stage also gave rise to tumours of increasing penetrance over the 5. Marine, J. C., Dawson, S. J. & Dawson, M. A. Non-genetic mechanisms of therapeutic
resistance in cancer. Nat. Rev. Cancer 20, 743–756 (2020).
number of transplantations (Extended Data Fig. 7i,j).
6. Timp, W. & Feinberg, A. P. Cancer as a dysregulated epigenome allowing cellular growth
Together, these results indicate that the tumorigenic potential of EICs advantage at the expense of the host. Nat. Rev. Cancer 13, 497–510 (2013).
is maintained autonomously, increases over time and can propagate 7. Teixeira, V. H. et al. Deciphering the genomic, epigenomic, and transcriptomic
landscapes of pre-invasive lung cancer lesions. Nat. Med. 25, 517–525 (2019).
months after ph-RNAi has been removed. This progression might sug-
8. Cavalli, G. & Heard, E. Advances in epigenetics link genetics to the environment and
gest that EICs acquire secondary modifications, either epigenetic or disease. Nature 571, 489–499 (2019).
genetic, that increase their aggressiveness over time. 9. Waddington, C. H. The epigenotype. Int. J. Epidemiol. 41, 10–13 (1942).
10. Nam, A. S., Chaligne, R. & Landau, D. A. Integrating genetic and non-genetic
determinants of cancer evolution by single-cell multi-omics. Nat. Rev. Genet. 22, 3–18
(2021).
Discussion 11. Shaffer, S. M. et al. Rare cell variability and drug-induced reprogramming as a mode of
cancer drug resistance. Nature 546, 431–435 (2017).
It is difficult to discriminate among genetic, environmental and
12. Hutter, C. & Zenklusen, J. C. The Cancer Genome Atlas: creating lasting value beyond its
cell-intrinsic epigenetic contributions to tumorigenesis33. The system data. Cell 173, 283–285 (2018).
described here shows that on transient depletion of PRC1 subunits cells 13. Stunnenberg, H. G., International Human Epigenome, C. & Hirst, M. The International
Human Epigenome Consortium: a blueprint for scientific collaboration and discovery.
undergo neoplastic transformation (Fig. 5g and Extended Data Fig. 8),
Cell 167, 1145–1149 (2016).
associated with the irreversible activation of genes including key JAK– 14. Butera, A., Melino, G. & Amelio, I. Epigenetic ‘drivers’ of dancer. J. Mol. Biol. 433, 167094
STAT pathway members that sustain cell growth, proliferation, loss of (2021).
15. Piunti, A. & Shilatifard, A. Epigenetic balance of gene expression by Polycomb and
cell polarity, cell migration and cytokine activity. One main difference
COMPASS families. Science 352, aad9780 (2016).
between these irreversibly activated genes and reversible PcG target 16. Muller, D. & Gyorffy, B. DNA methylation-based diagnostic, prognostic, and predictive
genes is the presence of different sets of transcription factor binding biomarkers in colorectal cancer. Biochim. Biophys. Acta Rev. Cancer 1877, 188722 (2022).
17. Pon, J. R. & Marra, M. A. Driver and passenger mutations in cancer. Annu. Rev. Pathol. 10,
motifs in their vicinity. We posit that, even if PRC1 is wiped out from
25–50 (2015).
both classes of genes on depletion, the preferential binding of JAK–STAT 18. Kloetgen, A., Thandapani, P., Tsirigos, A. & Aifantis, I. 3D chromosomal landscapes in
related transcription factors in the vicinity of irreversible genes might hematopoiesis and immunity. Trends Immunol. 40, 809–824 (2019).
19. Cancer Genome Atlas Research, N. et al. Genomic and epigenomic landscapes of adult
specifically foster their transcription after transient perturbation of
de novo acute myeloid leukemia. N. Engl. J. Med. 368, 2059–2074 (2013).
PcG, dampening their re-repression and inducing a self-sustaining aber- 20. Feinberg, A. P., Koldobskiy, M. A. & Gondor, A. Epigenetic modulators, modifiers and
rant cell state (Extended Data Fig. 8). One of these JAK–STAT targets, mediators in cancer aetiology and progression. Nat. Rev. Genet. 17, 284–299 (2016).
21. Bates, S. E. Epigenetic therapies for cancer. N. Engl. J. Med. 383, 650–663 (2020).
zfh1 plays an important role by blocking cell differentiation. Altogether, 22. Baylin, S. B. & Jones, P. A. Epigenetic determinants of cancer. Cold Spring. Harb. Perspect.
this cascade of events results in a self-sustaining mechanism that drives Biol. https://doi.org/10.1101/cshperspect.a019505 (2016).
tumorigenesis even after recovery of normal PcG protein concentra- 23. Feinberg, A. P. & Tycko, B. The history of cancer epigenetics. Nat. Rev. Cancer 4, 143–153
(2004).
tions and in the wake of the rescue of their chromatin function at most 24. Hanahan, D. Hallmarks of cancer: new dimensions. Cancer Discov. 12, 31–46 (2022).
of the PcG binding sites. 25. You, J. S. & Jones, P. A. Cancer genetics and epigenetics: two sides of the same coin?
Previous work showed that self-sustaining alternative cell states can Cancer Cell 22, 9–20 (2012).
26. Alonso-Curbelo, D. et al. A gene-environment-induced epigenetic program initiates
be triggered by transient perturbations in a sensitized Drosophila sys- tumorigenesis. Nature 590, 642–648 (2021).
tem56, as well as in immortalized breast cells57 or other cultured cells58, 27. Vicente-Duenas, C., Hauer, J., Cobaleda, C., Borkhardt, A. & Sanchez-Garcia, I. Epigenetic
including neural progenitor cells subjected to transient inhibition priming in cancer initiation. Trends Cancer 4, 408–417 (2018).
28. Terekhanova, N. V. et al. Epigenetic regulation during cancer transitions across 11 tumour
of the PRC2 complex59. PRC2 impairment in mouse striatal neurons types. Nature 623, 432–441 (2023).
induces progressive neurodegeneration by triggering a self-sustaining 29. Makohon-Moore, A. P. et al. Limited heterogeneity of known driver gene mutations
transcription derailment programme over time60. Furthermore, among the metastases of individual patients with pancreatic cancer. Nat. Genet. 49,
358–366 (2017).
knock-out or transient chemical inhibition of PRC2 also led cells to 30. McDonald, O. G. et al. Epigenomic reprogramming during pancreatic cancer progression
enter a quasi-mesenchymal state that depends on ZEB1, the mouse links anabolic glucose metabolism to distant metastasis. Nat. Genet. 49, 367–376
(2017).
homologue of fly zfh1, which is highly metastatic and associated with
31. Fennell, K. A. et al. Non-genetic determinants of malignant clonal fitness at single-cell
poor patient survival53. Therefore, epigenetic events might play a major resolution. Nature 601, 125–131 (2022).
role at early stages of oncogenesis or during tumour progression in 32. Mack, S. C. et al. Epigenomic alterations define lethal CIMP-positive ependymomas of
some mammalian cancers61. Our survey of a large database of different infancy. Nature 506, 445–450 (2014).
33. Pascual, G. et al. Dietary palmitic acid promotes a prometastatic memory via Schwann
types of solid cancer (Extended Data Fig. 9) as well as of data from sev- cells. Nature 599, 485–490 (2021).
eral cohorts of patients with multiple myeloma (Extended Data Fig. 10) 34. Chatterjee, A., Rodger, E. J. & Eccles, M. R. Epigenetic drivers of tumourigenesis and
cancer metastasis. Semin. Cancer Biol. 51, 149–159 (2018).
indicates that low expression levels of genes encoding canonical PRC1
35. Feinberg, A. P. The key role of epigenetics in human disease prevention and mitigation.
subunits is associated with poor patient prognosis, consistent with a N. Engl. J. Med. 378, 1323–1334 (2018).
putative suppressive role for PRC1 in these tumour types. Future work 36. Chan, H. L. & Morey, L. Emerging roles for Polycomb-group proteins in stem cells and
cancer. Trends Biochem. Sci. https://doi.org/10.1016/j.tibs.2019.04.005 (2019).
might address the role of epigenetic perturbations in these tumours
37. Parreno, V., Martinez, A. M. & Cavalli, G. Mechanisms of Polycomb group protein function
and in other physiological processes. in cancer. Cell Res. 32, 231–253 (2022).
38. Schuettengruber, B., Bourbon, H. M., Di Croce, L. & Cavalli, G. Genome regulation by
Polycomb and Trithorax: 70 years and counting. Cell 171, 34–57 (2017).
39. Bilder, D., Ong, K., Hsi, T. C., Adiga, K. & Kim, J. Tumour-host interactions through the lens
Online content
of Drosophila. Nat. Rev. Cancer 21, 687–700 (2021).
Any methods, additional references, Nature Portfolio reporting summa- 40. Beuchle, D., Struhl, G. & Muller, J. Polycomb group proteins and heritable silencing of
Drosophila Hox genes. Development 128, 993–1004 (2001).
ries, source data, extended data, supplementary information, acknowl-
41. Loubiere, V. et al. Coordinate redeployment of PRC1 proteins suppresses tumor formation
edgements, peer review information; details of author contributions during Drosophila development. Nat. Genet. 48, 1436–1442 (2016).
8 | Nature | www.nature.com
42. Loubiere, V., Papadopoulos, G. L., Szabo, Q., Martinez, A. M. & Cavalli, G. Widespread 55. Hou, X. S. & Perrimon, N. The JAK-STAT pathway in Drosophila. Trends Genet. 13, 105–110
activation of developmental gene expression characterized by PRC1-dependent (1997).
chromatin looping. Sci. Adv. 6, eaax4001 (2020). 56. Pinal, N., Martin, M., Medina, I. & Morata, G. Short-term activation of the Jun N-terminal
43. Martinez, A. M. et al. Polyhomeotic has a tumor suppressor activity mediated by kinase pathway in apoptosis-deficient cells of Drosophila induces tumorigenesis. Nat.
repression of Notch signaling. Nat. Genet. 41, 1076–1082 (2009). Commun. 9, 1541 (2018).
44. Classen, A. K., Bunker, B. D., Harvey, K. F., Vaccari, T. & Bilder, D. A tumor suppressor 57. Iliopoulos, D., Hirsch, H. A. & Struhl, K. An epigenetic switch involving NF-kappaB, Lin28,
activity of Drosophila Polycomb genes mediated by JAK-STAT signaling. Nat. Genet. 41, Let-7 MicroRNA, and IL6 links inflammation to cell transformation. Cell 139, 693–706
1150–1155 (2009). (2009).
45. Haag-Liautard, C. et al. Direct estimation of per nucleotide and genomic deleterious 58. Reizel, Y. et al. FoxA-dependent demethylation of DNA initiates epigenetic memory of
mutation rates in Drosophila. Nature 445, 82–85 (2007). cellular identity. Dev. Cell 56, 602–612 e604 (2021).
46. Rossi, F., Attolini, C. S., Mosquera, J. L. & Gonzalez, C. Drosophila larval brain neoplasms 59. Holoch, D. et al. A cis-acting mechanism mediates transcriptional memory at Polycomb
present tumour-type dependent genome instability. G3 Genes Genom. Genet. 8, target genes in mammals. Nat. Genet. 53, 1686–1697 (2021).
1205–1214 (2018). 60. von Schimmelmann, M. et al. Polycomb repressive complex 2 (PRC2) silences genes
47. Sievers, C., Comoglio, F., Seimiya, M., Merdes, G. & Paro, R. A deterministic analysis of responsible for neurodegeneration. Nat. Neurosci. 19, 1321–1330 (2016).
genome integrity during neoplastic growth in Drosophila. PLoS ONE 9, e87090 (2014). 61. Jaffe, L. F. Epigenetic theories of cancer initiation. Adv Cancer Res. 90, 209–230
48. Beira, J. V., Torres, J. & Paro, R. Signalling crosstalk during early tumorigenesis in the (2003).
absence of Polycomb silencing. PLoS Genet. 14, e1007187 (2018).
49. Flaherty, M. S. et al. chinmo is a functional effector of the JAK/STAT pathway that
regulates eye development, tumor formation, and stem cell self-renewal in Drosophila. Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
Dev. Cell 18, 556–568 (2010). published maps and institutional affiliations.
50. Leatherman, J. L. & Dinardo, S. Zfh-1 controls somatic stem cell self-renewal in the
Drosophila testis and nonautonomously influences germline stem cell self-renewal. Cell Open Access This article is licensed under a Creative Commons Attribution
Stem Cell 3, 44–54 (2008). 4.0 International License, which permits use, sharing, adaptation, distribution
51. Boukhatmi, H., Martins, T., Pillidge, Z., Kamenova, T. & Bray, S. Notch mediates inter-tissue and reproduction in any medium or format, as long as you give appropriate
communication to promote tumorigenesis. Curr. Biol. 30, 1809–1820 e1804 (2020). credit to the original author(s) and the source, provide a link to the Creative Commons licence,
52. Enomoto, M., Takemoto, D. & Igaki, T. Interaction between Ras and Src clones causes and indicate if changes were made. The images or other third party material in this article are
interdependent tumor malignancy via Notch signaling in Drosophila. Dev. Cell 56, included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
2223–2236 e2225 (2021). to the material. If material is not included in the article’s Creative Commons licence and your
53. Zhang, Y. et al. Genome-wide CRISPR screen identifies PRC2 and KMT2D-COMPASS as intended use is not permitted by statutory regulation or exceeds the permitted use, you will
regulators of distinct EMT trajectories that contribute differentially to metastasis. Nat. need to obtain permission directly from the copyright holder. To view a copy of this licence,
Cell Biol. 24, 554–564 (2022). visit http://creativecommons.org/licenses/by/4.0/.
54. Uhlirova, M. & Bohmann, D. JNK- and Fos-regulated Mmp1 expression cooperates with Ras
to induce invasive tumors in Drosophila. EMBO J. 25, 5294–5304 (2006). © The Author(s) 2024
Nature | www.nature.com | 9
Article
Methods and the number of pupae was counted for each condition. The adult
hatching rate was calculated by dividing the number of male and female
Drosophila strains and genetics adults hatched from pupae by the number of pupae.
Flies were raised on a standard cornmeal yeast extract medium at 25 °C For the zfh1-RNAi and Stat92E-RNAi rescue experiments under con-
unless otherwise indicated. Fly lines and crosses performed to deplete stant ph-KD, ey-FLP, Act5C-gal4 (FRT.CD2 STOP); + ; UAS-GFP (BL#64095)
PRC1 subunits or to perform control experiments were generated from females were crossed with males of various genotypes. For negative con-
stocks provided by the Bloomington Drosophila Stock Center (BL) and trol experiments, females were crossed with UAS-gfp-RNAi (BL#9331);
the Vienna Drosophila Resource Center (VDRC), as indicated below for UAS-w-RNAi (BL#33623) males. To confirm that the zfh1-RNAi and
each experiment. The work with transgenic strains of Drosophila was Stat92E-RNAi do not induce any significant change in the eye develop-
performed under the ethical approval no. n6906C2 of the Ministère de ment we crossed female to UAS-zfh1-RNAi (VDRC#103205); UAS-w-RNAi
l’Enseignement Supérieur, de la Recherche et de l’Innovation, issued (BL#33623) and UAS-Stat92E-RNAi (VDRC#43866); UAS-w-RNAi
on 8 April 2020. (BL#33623) males. Positive control experiments were conducted
For KD experiments of PRC1 subunits and generation of EICs, Gal80ts by crossing females with UAS-gfp-RNAi (BL#9331); UAS-ph-RNAi
was used to control the temporal ph or Psc/Su(z)2 down-regulation by (VDRC#50028) males. For the rescue condition we crossed females
switching the temperature from 18 to 29 °C. KDs are generated in the to UAS-zfh1-RNAi (VDRC#103205); UAS-ph-RNAi (VDRC#50028) and
larval EDs using the ey-FLP system. The rationale of the reversible KD UAS-Stat92E-RNAi (VDRC#43866); UAS-ph-RNAi (VDRC#50028) males.
system is the following: ph-RNAi, as well as the GFP marker, are under This systematic breeding strategy facilitated the investigation of the
control of UAS sequences. Cells expressing ey-FLP (in pink in Fig. 1a) specific roles of zfh1 and Stat92E genes under constant ph-KD condi-
induce FLP-out of a transcriptional stop (located between two FRT tions.
sites and indicated in orange in Fig. 1a) in EDs, leading to expression of Flies were reared and crossed at 18 °C and tumours were scored in
act-Gal4 (in light blue in Fig. 1a). tub-Gal80ts (in purple in Fig. 1a) encodes the progeny reared at 18 °C. Note that in this genetic background there
a ubiquitously expressed, temperature-sensitive Gal4 repressor. is no Gal80ts and therefore the KDs are obtained independently of the
At restrictive temperature (29 °C), Gal80ts is inactivated. Gal4 activates temperature. In the case of the ph-KD positive control, a tumour phe-
UAS sequences, expressing ph-RNAi and GFP (as readout of ph-KD). notype with 100% penetrance was observed in the progeny.
To perform KDs, flies were reared and crossed at 18 °C to inhibit Gal4 For the zfh1-RNAi and Stat92E-RNAi rescue experiments under tran-
activity. A total of 80 virgin females were crossed with 20 males for sient ph-KD, ey-FLP, Act5C-gal4 (FRT.CD2 STOP) (BL#64095); + ; Tub-
each genotype and experiment. In all conditions (no, constant or tran- Gal80ts (BL#7018)/TM6BTb females were crossed with males of various
sient KDs), flies were allowed to lay eggs at 18 °C for 4 h to synchronize genotypes. For negative control experiments, females were crossed
embryonic and larval stages. As the timing of Drosophila development with UAS-gfp-RNAi (BL#9331); UAS-w-RNAi (BL#33623) males. To con-
is temperature dependent, we adapted the timing for each KD condi- firm that the zfh1-RNAi and Stat92E-RNAi do not induce any significant
tion to carry out phenotypic and molecular analyses at comparable change in the eye development, we crossed female to UAS-zfh1-RNAi
developmental times. The genotypes of the flies on which we carried (VDRC#103205); UAS-w-RNAi (BL#33623) and UAS-Stat92E-RNAi
out the different KDs are listed below. (VDRC#43866); UAS-w-RNAi (BL#33623) males. Positive control
For ph-KD: ey-FLP, Act-gal4 (FRT.CD2 STOP) (BL#64095); TubGal80ts experiments were conducted by crossing females with UAS-gfp-RNAi
(BL#7019); UAS-ph-RNAi (VDRC#50028)/UAS-GFP (BL#64095). (BL#9331); UAS-ph-RNAi (VDRC#50028) males. For the rescue condition
For Psc-Su(z)2-KD: ey-FLP, Act-gal4 (FRT.CD2 STOP) (BL#64095); we crossed females to UAS-zfh1-RNAi (VDRC#103205); UAS-ph-RNAi
UAS-Psc-Su(z)2 RNAi (BL#38261, VDRC#100096); TubGal80ts (VDRC#50028) and UAS-Stat92E-RNAi (VDRC#43866); UAS-ph-RNAi
(BL#7018)/UAS-GFP (BL#64095). (VDRC#50028) males. This systematic breeding strategy facilitated
For control white-KD: ey-FLP, Act-gal4 (FRT.CD2 STOP) (BL#64095); the investigation of the specific roles of the zfh1 and Stat92E genes
TubGal80ts (BL#7019); UAS-w-RNAi (BL#33623)/UAS-GFP (BL#64095). under transient ph-KD conditions.
All dissections were performed on female larvae at the L3 stage. Flies were reared and crossed at 18 °C and flies were allowed to lay
For the no ph-KD (no depletion), flies were kept at 18 °C throughout eggs overnight at 18 °C. For transient depletion, flies were kept at 18 °C
development and dissected 10 days AEL. For the constant ph-KD (con- for 48 h, then shifted at 29 °C for 24 h and returned to 18 °C until dis-
stant depletion), flies were kept at 29 °C throughout development and section 10 days AEL.
dissected 5 days AEL. For the larval depletion (from L1 to L3) flies were Allografts were performed according to the protocol described previ-
kept at 18 °C for 48 h and shifted at 29 °C until dissection 5 days AEL. ously62. The following fly line was used: ey-FLP (BL#5580), Ubi-p63E(FRT.
For the transient ph-KD at the L1 stage, flies were kept at 18 °C for 48 h, STOP)Stinger (BL#32249); Tub-Gal80ts (BL#7019); Act5C-Gal4(FRT.CD2),
then shifted at 29 °C for 24 h and returned to 18 °C until dissection 9 UAS-RFP (BL#30558)/UAS-ph-RNAi (VDRC#50028). Briefly, GFP-positive
or 11 days AEL. For the transient ph-KD at the L2 stage, flies were kept EDs from no-ph-KD, constant ph-KD or transient ph-KD L3 female lar-
at 18 °C for 96 h, shifted at 29 °C for 24 h and returned to 18 °C until vae were dissected in PBS, cut into small pieces and injected into the
dissection 8 days AEL. For the transient ph-KD at the L3 early stage, abdomen of adult female hosts (BL#23650). The whole experiment
flies were kept at 18 °C for 120 h, shifted at 29 °C for 24 h and returned was performed at 18 °C to avoid reactivation of ph-RNAi expression.
to 18 °C until dissection 8 days AEL. For the transient ph-KD at the L3 To score tumour progression in allografts, flies were imaged every
late stage, flies were kept at 18 °C for 168 h, shifted at 29 °C for 24 h 2 days using Leica MZ FLIII to verify GFP as a readout of tumour growth.
and returned to 18 °C until dissection 8 days AEL. For the transient Tumours were dissected and re-injected when the host abdomen was
Psc-Su(z)2-KD at the L1 stage, flies were kept at 18 °C for 48 h, shifted at fully GFP. Injected Drosophila pictures were taken using Ximea USB 3.1
29 °C for 48 h and returned to 18 °C until dissection 8 days AEL. For all Gen1 camera with a Sony CMOS-xiCAll sensor.
conditions, a minimum of three biological replicates was performed.
For each replicate, 150 discs were scored in PH depletions and more Immunostaining procedures
than 30 discs were scored for PSC depletions. Constant and transient EDs from L3 female larvae were dissected at room temperature in 1× PBS
depletions of PH (PH-d and PH-p) or PSC-SU(Z)2 generated tumours and fixed in 4% formaldehyde for 20 min. Tissues were permeabilized
in 100% of dissected tissues. for 1 h in 1× PBS + 0.5% Triton X-100 on a rotating wheel. Permeabilized
To assess viability, we measured adult hatching rate. For this purpose, tissues were blocked for 1 h in 3% BSA PBTr (1× PBS + 0.1% Triton X-100),
after 4 h of egg laying, we applied the treatments described above to and incubated O/N on a rotating wheel at 4 °C with primary antibod-
produce ph-KD at the desired times. The vials were maintained at 18 °C ies diluted in PBTr + 1% BSA. For double-strand break staining, larvae
were dissected at room temperature in 1× PBS, fixed in 4% paraform- for 5 min, air dried and stained with fluorescence in situ hybridiza-
aldehyde for 30 min and primary antibodies were incubated for 2 h tion (FISH) probes for AACAC, AATAT and 359 base pair (bp) repeats
at room temperature. The following primary antibodies were used: as previously described65. Probe sequences are: 5′-6-FAM-(AACAC),
7
goat anti-PH63 (1:500), mouse anti-ELAV (1:1,000, DSHB, catalogue 5′-Cy3-TTTTCCAAATTTCGGTCATCAAATAATCAT and 5′-Cy5-(AATAT).
6
no. 9F8A9), mouse anti-ABD-B (1:1,000, DSHS, catalogue no. 1A2E9), FISH staining was used to help identify chromosomes in rearranged
chicken anti-GFP (1:500, Invitrogen, catalogue no. A10262), rabbit conditions. Microscopy acquisition was performed on a DeltaVision
anti-ZFH1 (ref. 49) (1:2,000) and rabbit anti-histone H2AvD pS137 (1:500, deconvolution microscope using a ×60 oil immersion objective and
Rockland, catalogue no. 600-401-914). Then, samples were washed in a CoolSNAP HQ2 camera. Images were processed for Deconvolution
PBTr three times before adding secondary antibodies in PBTr for 2 h at using SoftWoRx v.6.0.
room temperature on a rotating wheel. The following secondary anti-
bodies were used: donkey anti-goat Alexa Fluor 555 (1:1,000, Invitrogen, Damage induction by X-ray exposure
catalogue no. A-21432), donkey anti-mouse Alexa Fluor 647 (1:1,000, L3 early-stage female larvae were transferred into a petri dish contain-
Invitrogen, catalogue no. A-31571), donkey anti-chicken (1:1,000, Cli- ing standard food medium, and were exposed to 5 Gy of X-rays using a
nisciences, catalogue no. 703-546-155), donkey anti-rabbit Alexa Fluor Precision X-RAD iR160 irradiator. After irradiation, larval heads were
555 (1:1,000, Invitrogen, catalogue no. A-31572), donkey anti-rabbit dissected at indicated timepoints at room temperature in 1× PBS and
Alexa Fluor 488 (1:1,000, Invitrogen, catalogue no. A-21206). F-actin fixed in 4% paraformaldehyde for 30 min before immunostaining.
was stained by adding rhodamine phalloidin Alexa Fluor 555 (1:1,000, Microscopy and image analysis were performed as described above.
Invitrogen, catalogue no. R415) or Alexa Fluor 488 (1:1,000, Invitro-
gen, catalogue no. A12379). Tissues were washed three times in PBTr. RT–qPCR experiments
DAPI (4,6-diamidino-2-phenylindole) staining was performed at a final L3 female larvae were dissected in Schneider medium on ice. Total RNA
concentration of 1 μg ml−1 for 15 min. Then discs were washed in PBTr was extracted from EDs using TRIzol reagent. RNA purification was per-
and mounted in Vectashield medium (Eurobio Scientific, catalogue formed using the RNA Clean & Concentrator kit (Zymo Research, cata-
no. H-1000-10) or ProLong Gold antifade agent (Life Technologies, logue no. R1015). Reverse transcription was performed using Maxima
P36930). Image acquisition was performed using a Leica SP8-UV confo- First Strand complementary DNA synthesis kit (Invitrogen, catalogue
cal microscope. ED areas were measured using Fiji64 by drawing contour no. K1642). Quantitative PCR (qPCR) was performed using LightCycler
lines around the DAPI-labelled tissue and measuring their surface. A 480 SYBR Green I Master Mix (Roche, catalogue no. 04707516001).
minimum of 30 EDs was considered to measure average ED areas in qPCR with reverse transcription (RT–qPCR) experiments were analysed
each condition. Images for quantification of double-strand break foci using LightCycler and GraphPad Prism software. All experiments were
were taken with a DeltaVision deconvolution microscope using a ×60 performed in biological triplicates.
oil immersion objective and a CoolSNAP HQ2 camera. Images were
processed using Deconvolution through SoftWoRx v.6.0. All experi- RNA-seq experiments
ments were performed in biological duplicates. L3 female larvae were dissected in Schneider medium on ice. Total RNA
was extracted from EDs using TRIzol reagent. RNA purification was
EdU staining performed using the RNA Clean & Concentrator kit (Zymo Research,
EdU experiments were performed using Click-iT Plus EdU Alexa fluor catalogue no. R1015). Finally, poly-A RNA selection, library prepara-
555 Imaging kit (Invitrogen, catalogue no. C10638). The EDs of L3 female tion and Illumina sequencing (20 M paired-end reads, 150 nt) were
larvae were dissected at room temperature in Schneider medium. Then, performed by Novogene (https://en.novogene.com/). All experiments
EdU incorporation was performed for 15 min with 25 μM EdU solution were performed in triplicates.
on a rotating wheel at room temperature. After washing with PBS, tis-
sues were fixed in 4% formaldehyde 30 min and washed three times gDNA sequencing
with PBS. The imaginal discs were permeabilized for 1 h in 1× PBS + 0.5% gDNA was isolated using QIAamp DNA Micro Kit (Qiagen) following
Triton X-100 on a rotating wheel then blocked for 1 h in 1× PBS + 0.1% the manufacturer’s instructions. For each biological replicate, roughly
Triton X-100 + 3% BSA. EdU detection was performed according to the 70 EDs from wandering female larvae were dissected. In total, we
manufacturer’s instructions for 30 min on a rotating wheel at room sequenced four biological replicates for control samples (no ph-KD
temperature away from light. Next, 500 μl of Click-iT reaction cocktail condition, that is, larvae of the crosses used for transient depletion that
were prepared per tube containing 20 EDs. After 1× PBS + 0.1% Triton were reared at constant permissive temperature of 18 °C). Furthermore,
wash DAPI staining was performed at a final concentration of 1 μg ml−1 12 tumour samples were sequenced, that is, two biological replicates
for 15 min. Tissues were washed in 1× PBS + 0.1% Triton and discs were for six different depletion conditions as follows: (1) constant ph-KD;
mounted in Vectashield medium. Image acquisition was performed (2) transient ph-KD d9; (3) transient ph-KD d11; (4) early L3 ph-KD, 24 h
using a Leica SP8-UV confocal microscope. Images of EdU stained EDs recovery; (5) early L3 ph-KD, 96 h recovery and (6) early L3 ph-KD, 144 h
shown in Supplementary Videos were acquired using a Zeiss LSM980 recovery. All these conditions result in tumour formation. The gDNAs
Airyscan microscope in 4Y modality. Airyscan images of EdU stained of all samples were processed for library preparation by Novogene
EDs were processed with ZEN (v.3.6 Blue Edition, Zeiss) using default (https://en.novogene.com/). Briefly, gDNA was fragmented to an aver-
settings. Videos were created using Imaris (v.10.1, Oxford Instruments). age size of roughly 350 bp and then processed for DNA library prepara-
All experiments were performed in biological duplicates. tion according to the manufacturer’s (Illumina) paired-end protocols.
Sequencing was performed using the Illumina Novaseq 6000 platform
Analysis of chromosomal abnormalities to generate 150 bp paired-end reads with a coverage of at least ten times
Chromosome preparation and FISH were performed as previously for 99% of the genome.
described65,66. EDs from L3 stage larvae were dissected in 0.7% NaCl solu-
tion and incubated in Colchicine solution (3 ml of 0.7% NaCl + 100 μl Western blot
of 10−3 M Colchicine) for 1 h at room temperature away from light. EDs Roughly 150 EDs were dissected in Schneider medium on ice per rep-
were incubated in 0.5% sodium acetate for 7 min, followed by fixation licate. To collect sufficient material, EDs were dissected in batches,
(freshly prepared 2.5% PFA in 45% acetic acid) for 4 min on coverslip. snap frozen in liquid nitrogen and stored at −80 °C. Discs were
EDs were pressed onto poly-lysine coated slides using manual force homogenized with a Tenbroeck directly in radioimmunoprecipita-
and snap frozen in liquid nitrogen. Slides were washed in 100% ethanol tion assay lysis buffer (50 mM Tris pH 7.5, 150 mM NaCl, 1% NP40, 0.5%
Article
Na-deoxycholate, 0.1% SDS, 2× protease inhibitor) and incubated on atac-seq/#standards). RNA-seq were performed in triplicates, follow-
ice for 10 min. If necessary, a second round of mechanical dissocia- ing Encode’s recommendations (https://www.encodeproject.org/
tion was performed. Samples were centrifuged for 10 min at 10,000g data-standards/rna-seq/long-rnas/).
at 4 °C and the supernatant was transferred to a fresh tube. Proteins In general, immunostaining experiments were performed in biologi-
were quantified using BCA protein assay and 10 μg were used per gel cal duplicates. Each biological replicate was obtained from independent
lane, before 40 min of migration at 200 V in MES 20× migration buffer genetic crosses. The only exception was the phospho-H2AV staining
and 1 h of transfer (1 A). Membranes were blocked for 1 h in PBS + 0.2% shown in Fig. 1j and Extended Data Fig. 2c, which was performed once,
Tween + 10% milk powder at room temperature, incubated O/N with but scoring tissues that came from six independent genetic crosses. For
primary antibodies in PBS + 0.2% Tween at 4 °C on a shaker and washed sample sizes of immunostaining experiments, see the sheet named ‘All
in PBS + 0.2% Tween. The following primary antibodies were used: rab- IF sample numbers’ in Supplementary Table 6. For transcriptomic, RT–
bit anti-PH (1:200), rabbit anti-zfh1 (ref. 49) (1:2,000), mouse anti-beta qPCR and western blot analysis, experiments were performed in bio-
tubulin (1:5,000, DSHB, catalogue no. AA12.1). HRP-conjugated sec- logical triplicates. ATAC-Seq, CUT&RUN, ChIP–seq and immunostaining
ondary antibodies were incubated with the membrane for 2 h at room experiments were performed in biological duplicates. Each biological
temperature. The following secondary antibodies were used: goat replicate was obtained from independent genetic crosses.
antirabbit (1:15,000, Sigma, catalogue no. A0545), rabbit antimouse For experiments presented in Figs. 1 and 5, as well as Extended Data
(1:15,000, Sigma, catalogue no. A9044). Membranes were washed in Figs. 1, 2, 3, 5 and 6, involving genetic crosses with different lines and
PBS + 0.2% Tween and revealed using Super Signal West Dura kit (Pierce) in different conditions, followed by tissue area measurements and
and Chemidoc Bio-Rad. Western blots were analysed using ImageLab immunofluorescence, two independent biological replicates were
software v.6.1 from Bio-Rad. The full-size raw blot images are provided performed with similar results. Measured areas and the number of
in the Supplementary Fig. 1. tissues analysed in imaging are reported in Supplementary Table 6.
Allograft experiments were performed in two independent biologi-
ChIP–seq experiments cal replicates. In the first replicate, one starting tumour obtained on
ChIP–seq on L3 EDs were performed as described previously41, with constant PH depletion and one tumour obtained from transient PH
minor modifications, and 400 EDs were used per replicate. If necessary, depletion were used. In the second replicate, two constant PH depletion
several dissection and/or collection batches were frozen in liquid nitro- and two transient PH depletion tumours were injected. Results were
gen and stored at −80 °C to collect sufficient material. Chromatin was similar for both replicates. The total number of injected host flies is
sonicated using a Bioruptor Pico (Diagenode) for 10 min (30 s on, 30 s reported in the graphs of the Extended Data Fig. 7b,c.
off). PH antibodies67 were diluted 1:100 for immunoprecipitation. After
decrosslinking, DNA was purified using MicroChIP DiaPure columns Bioinformatic analyses on Drosophila datasets
from Diagenode. DNA libraries for sequencing were prepared using All in-house bioinformatic analyses were performed in R v.3.6.3 (https://
the NEBNext Ultra II DNA Library Prep Kit for Illumina. Sequencing www.R-project.org/). Computations on genomic coordinate files
(paired-end sequencing 150 bp, roughly 4 Gb per sample) was per- and downstream computations were conducted using the data.table
formed by Novogene (https://en.novogene.com/). All experiments R package (data.table: Extension of ‘data.frame’. https://r-datatable.
were performed in biological duplicates. com, https://Rdatatable.gitlab.io/data.table, https://github.com/
Rdatatable/data.table, v.1.14.2). In all relevant panels of figures and
CUT&RUN experiments Extended Data figures, box plots depict the median (line), upper and
CUT&RUN experiments were performed as described by Kami Ahmad lower quartiles (box) ±1.5× interquartile range (whiskers) and outliers
in protocols.io (https://doi.org/10.17504/protocols.io.umfeu3n) with are not shown. For each relevant panel, the statistical test that was
minor modifications. We dissected 50 EDs in Schneider medium, cen- used is specified in the caption: NS denotes not significant (P > 0.05),
trifuged them for 3 min at 700g and washed them twice with wash+ *P < 5 × 10−2, **P < 1 × 10−2, ***P < 1 × 10−3, ****P < 1 × 10−5.
buffer before adding concanavalin A-coated beads. MNase digestion
(pAG-MNase Enzyme from Cell Signaling) was performed for 30 min on gDNA processing and mapping of somatic variants
ice. After ProteinaseK digestion, DNA was recovered using SPRIselect gDNA variant calling was performed by Novogene (https://en.novogene.
beads and eluted in 50 μl of Tris-EDTA. DNA libraries for sequencing com/). Briefly, base calling was performed using Illumina pipeline
were prepared using the NEBNext Ultra II DNA Library Prep Kit for Illu- CASAVA v.1.8.2, and subjected to quality control using fastp with the
mina. Sequencing (paired-end sequencing 150 bp, roughly 2 Gb per following parameters: -g -q 5 -u 50 -n 15 -l 150 --min_trim_length 10
sample) was performed by Novogene (https://en.novogene.com/). The --overlap_diff_limit 1--overlap_diff_percent_limit 10. Then, sequenc-
following antibodies were used: H3K27me3 (1:100, Active Motif, cata- ing reads were aligned to the dm6 version of the Drosophila genome
logue no. 39155), H3K27Ac (1:100, Active Motif, catalogue no. 39133), using Burrows–Wheeler aligner with default parameters and dupli-
H2AK118Ub (1:100, Cell Signaling, catalogue no. 8240). All experiments cate reads were removed using samtools and PICARD (http://picard.
were performed in biological duplicates. sourceforge.net). Raw SNP and InDel sets were called using GATK with
the following parameters: --gcpHMM 10 -stand_emit_conf 10 -stand_
ATAC-Seq experiments call_conf 30. Then, SNPs were filtered using the following criteria:
ATAC-Seq experiments were performed using the ATAC-Seq kit from SNP QD < 2, FS > 60, MQ < 30, HaplotypeScore > 13, MappingQuality-
Diagenode (catalogue no. C01080002). Ten EDs were used as start- RankSum < −12.5, ReadPosRankSum < −8. For INDEL variants, the fol-
ing material for each replicate and condition. Tagmentated DNA was lowing criteria were used: QD < 2, FS > 200, ReadPosRankSum < −20.
amplified by PCR using 13 cycles and the purified DNA libraries were UCSC known genes were used for gene and region annotations.
sequenced (paired-end sequencing 150 bp, roughly 2 Gb per sample) Finally, the variants were compared to a batch-matched control sam-
by Novogene (https://en.novogene.com/). All experiments were per- ple (no ph-KD), in the search for bona fide SNVs and InDels using the
formed in biological duplicates. MuTect2 module of the GATK package. Only SNVs and InDels variants
that passed Mutect2 filtering (FILTER = “PASS”) were considered for
Statistics and reproducibility downstream analyses. Structural variants and CNVs were detected
ChIP–seq, CUT&RUN and ATAC-Seq were performed in duplicates, fol- using breakdancer (https://github.com/genome/breakdancer) and
lowing Encode’s standards (https://www.encodeproject.org/chip-seq/ CNVnator (https://github.com/abyzovlab/CNVnator) software pack-
transcription_factor/#standards; https://www.encodeproject.org/ ages, respectively.
Then, called variants were imported in R for downstream analyses. across all conditions (maximum gap of 250 bp for H3K27Ac and
When looking at the fraction of tumour samples that contained a given ATAC-Seq peaks; 2.5 kb for H3K27me3 and H2AK118Ub domains) and
alteration (Fig. 1h), we only retained SNVs or InDels with an allelic frac- overlapping reads were counted using the featureCounts function
tion greater than 0.2, structural variants that were supported by at least from the Rsubread R package (v.2.0.1, isPairedEnd = TRUE). Differential
five reads and CNVs with an allelic fraction bigger than 1.5 (duplication) analysis was then performed using the DESeq2 R package (v.1.26.0, size
or smaller than 0.66 (deletion). factors, total number of aligned reads; design, ~replicate + condition).
The same procedure was used for the differential analysis of ATAC-Seq
RNA-seq processing and differential analysis peaks between zfh1+ph-KD and gfp+ph-KD.
After initial quality checks of the newly generated data using fastqc
(http://www.bioinformatics.babraham.ac.uk/projects/fastqc/), the Clustering of differentially accessible ATAC-Seq peaks
paired-end reads were aligned to a custom index consisting of the For the clustering of ATAC-Seq peaks, we only considered the peaks
dm6 version of the Drosophila genome together with GFP, EGFP and showing a significant difference (P < 1 × 10−3 and |log fold change| >1)
adj 2
mRFP1 sequences, using the align function from the Rsubread R pack- after constant or transient ph-KD (day 11 AEL) and with a minimum
age68 (v.2.0.1) with the following parameters: maxMismatches = 6, log base mean of 1.25 to avoid noisy peaks. The log fold change val-
10 2
unique = TRUE. Next, aligned reads were counted for each D. mela- ues were clipped at the 5th and 95th percentiles and clustered using
nogaster transcript (dmel_r6.36 annotation) using the featureCounts the supersom function from the kohonen R package70 (v.3.0.10) using
function from the Rsubread R package (v.2.0.1, isPairedEnd = TRUE) a four-layer self-organizing map (layer 1, logfold change constant
2
and differential expression analysis was performed using the DESeq2 ph-KD; layer 2, logfold change transient ph-KD; layer 3, P constant
2 adj
R package69 (v.1.26.0, design = ~replicate + condition). The tables corre- ph-KD; layer 4, P transient ph-KD) with similar weights for the four
adj
sponding to the different comparisons are available in Supplementary layers, using a 1 × 3 grid (topology = hexagonal, toroidal = TRUE). Full
Tables 1, 4 and 5. clustering output is available in Supplementary Table 3.
For the differential analysis of the transcriptomes after no ph-KD
(control), constant and transient ph-KD, each ph-RNAi sample was Classification of PcG target genes and peaks-to-gene
compared to temperature-matched w-RNAi controls (Fig. 2a and assignment
Extended Data Fig. 8b). DESeq2 outputs are available in Supplementary To define PcG target genes, we defined a clean set of H3K27me3 domains
Tables 1 and 5. For the differential analysis of the transcriptomes after in the control (no ph-KD) condition by removing artefactual splits due
zfh1+w-KD, Stat92E+w-KD, gfp+ph-KD, zfh1+ph-KD and Stat92E+ph-KD, to sequencing gaps (github), resulting in 241 domains. Then, only the
all were compared to temperature-matched gfp+w-KD (Supplementary genes for which at least 50% of the gene body was overlapping with a
Table 4). H3K27me3 domain were considered as direct PcG target. When rel-
evant, only irreversible, reversible and unaffected genes that were
Clustering of differentially expressed genes direct PcG targets when considered (Fig. 3). PcG target gene assignment
For the clustering, we selected the genes that were differentially is available in Supplementary Table 2 (PcG_bound and class columns).
expressed (P < 0.05 and |logfold fold change | >1) after constant or To assess whether a gene was overlapping a H3K27me3 domain or
adj 2 2
transient ph-KD (d9 or d11 AEL). In addition, we only considered the a H3K27Ac peak in a given condition, we used different criteria. For
genes that did not show significant changes after no ph-KD (control). H3K27me3 (Fig. 3b), only the genes for which at least 50% of the gene
Then, log fold change values were clipped at the 5th and 95th percentiles body was overlapping a confident H3K27me3 domain (‘CUT&RUN,
2
and clustered using the supersom function from the kohonen R pack- ChIP–seq and ATAC-Seq processing, peak calling and differential anal-
age70 (v.3.0.10). As day 9 and day 11 transient ph-KD yielded substantially ysis’ section above) were considered as hits. For H3K27Ac (Fig. 3c),
similar transcriptomes, a two-layer self-organizing map was trained only the genes containing a confident peak (‘CUT&RUN, ChIP–seq
(layer 1, constant ph-KD; layer 2, D9 and D11 transient ph-KD) with similar and ATAC-Seq processing, peak calling and differential analysis’ sec-
weights for the two layers, using a 3 × 2 grid (topology = hexagonal, toroi- tion above) in the gene body or up to 2.5 kb upstream of the TSS were
dal = TRUE). Clustering output is available in Supplementary Table 2. considered as hits.
To assign PH peaks (Extended Data Fig. 6e) or ATAC-Seq peaks
CUT&RUN, ChIP–seq and ATAC-Seq processing, peak calling and (Fig. 4b), peaks were assigned to the closest TSS with a maximum
differential analysis genomic separation of 25 kb (peaks that were located further away
After initial quality checks of the newly generated data using fastqc, were not considered).
the reads were aligned to the dm6 version of the Drosophila genome
using bowtie 2 (ref. 71, v.2.3.5.1) with the following parameters: --local Gene Ontology terms enrichment
--very-sensitive-local --no-unal --no-mixed --no-discordant --phred33 Gene Ontology terms associated with the genes of interest and a back-
-I 10 -X 700, and low mapping quality reads were discarded using sam- ground set of genes, consisting of all the genes that passed DESeq2
tools72 (-q 30, v.1.10, using htslib v.1.10.2-3). initial filters, were retrieved using the AnnnotationDbi R package
PH, H3K27me3, H3K27Ac, H2AK118Ub and ATAC-Seq peaks and/ (https://bioconductor.org/packages/AnnotationDbi.html, v.1.48.0).
or domains were called for each replicate separately and on merged For each Gene Ontology term, over-representation was assessed using a
reads using macs2 (ref. 73, v.2.2.7.1) with the following parameters: one-sided Fisher’s exact test (alternative = ‘greater’). Obtained P values
--keep-dup 1 -g dm -f BAMPE -B --SPMR. For PH ChIP–seq, the input were corrected for multiple testing using false discovery rate (FDR).
sample was used as control. For H3K27me3, H3K27Ac and H2AK118Ub
CUT&RUN, the IgG sample was used as control. Only peaks detected in Motif enrichment
both replicates (enrichment greater than 0 AND q value less than 0.05) To search for DNA binding motifs enriched at each ATAC-Seq cluster, we
and using merged replicates (enrichment greater than 2 AND q < 0.01) used the centre of corresponding peaks ±250 bp (500 bp total). Result-
were retained for further analyses, after being merged with a minimum ing regions were analysed with the i-cisTarget online tool74, using v.6.0
gap size of 250 bp for narrow peaks (PH, H3K27Ac and ATAC-Seq) and of the position weight matrix database (consisting of 24,453 position
2.5 kb for broad marks (H3K27me3 and H2AK118Ub). The macs2 bed- weight matrics). Only top scoring motifs with a normalized enrichment
graph files were used for visualization purposes. score greater than 5.5 and a rank less than 50 were considered (Fig. 4e).
For the differential analysis of H3K27me3, H3K27Ac, H2AK118Ub To search for motifs associated with increased or decreased acces-
CUT&RUN and ATAC-Seq, peaks and/or domains were first merged sibility after constant or transient ph-KD, we used a collection of
Article
non-redundant transcription factor motifs75 and counted their occur- previously described89. The differential gene expression analysis
rences across all ATAC-Seq peaks ±250 bp, using the matchMotifs func- between normal bone marrow plasma cells from healthy donors and
tion from the motifmatch R package (v.1.18.0; https://doi.org/10.18129/ multiple myeloma cells from patients was carried out by using the
B9.bioc.motifmatchr) with the following parameters: P = 5 × 10−4, Mann–Whitney test. The prognostic value of PHC1, PHC2, PHC3, CBX2,
cutoff
bg = ‘genome’, genome = ‘dm6’. Of note, only motifs associated with a CBX7 and BMI1 genes was combined using our previously published
Drosophila transcription factor gene that passed initial DESeq2 initial methodology89 (sum of the Cox b coefficients of each of the six genes,
filters were considered. Then, we fitted two LASSO regressions using weighted by ±1 if the patient’s multiple myeloma cell signal for a given
the cv.glmnet and the glmnet functions from the glmnet package in R gene is above or below the probe set Maxstat value of the gene). Clus-
(v.4.1.4), with the following parameter: lambdas = 10seq(2, −3, by = −0.1), tering was performed using the Morpheus software (https://software.
standardize, TRUE; nfolds, 5), aiming at predicting log fold changes broadinstitute.org/morpheus) and violin plots using GraphPad Prism
2
after constant or transient ph-KD. The top 25 motifs with the strongest software (http://www.graphpad.com/scientific-software/prism/).
|s0| coefficients in any of the two models were used to train two linear
models to predict log fold changes after transient or constant ph-KD. Reporting summary
2
Only the motifs with a significant coefficient in at least one of the two Further information on research design is available in the Nature Port-
linear models (P < 1 × 10−5) were considered (Fig. 4f). folio Reporting Summary linked to this article.
Analysis of human solid tumours
Data availability
The differential gene expression analysis was carried out by using
a Mann–Whitney test and the TNMplot database, which contains The NGS datasets generated in this study were made publicly available
transcriptome-level RNA-seq data for different tumour samples from in the Gene Expression Omnibus (accession number GSE222193). A
The Cancer Genome Atlas (TCGA) and The Genotype-Tissue Expression UCSC browser to visualize the data is available at http://genome-euro.
(GTEx) repositories76. ucsc.edu/s/cavalli/EpiCancer.
The survival analysis was carried out using the Pan-Cancer (Bladder,
Lung adenocarcinoma and Rectum adenocarcinoma) or gene array
(Breast, Ovarian and Prostate) datasets77,78 of the online tool www. Code availability
kmplot.com (accessed on 22 December 2022). The Pan-Cancer dataset All custom scripts that were generated for this study were made publicly
is based on TCGA data generated using the Illumina HiSeq 2000 plat- available at https://github.com/vloubiere/Parreno_Loubiere_2023.
form with survival information derived from the published sources79.
The gene-array samples were obtained using Affymetrix HGU133A and
62. Rossi, F. & Gonzalez, C. Studying tumor growth in Drosophila using the tissue allograft
HGU133plus2 gene chips. The samples were MAS5 normalized and the method. Nat. Protoc. 10, 1525–1534 (2015).
mean expression in each sample was scaled to 1,000. The most reliable 63. Grimaud, C. et al. RNAi components are required for nuclear clustering of polycomb
group response elements. Cell 124, 957–971 (2006).
probe sets to represent single genes were identified usNAiing JetSet80.
64. Schindelin, J. et al. Fiji: an open-source platform for biological-image analysis. Nat.
In the survival analysis, each cut-off value between the lower and Methods 9, 676–682 (2012).
upper quartiles of expression was analysed by Cox proportional hazards 65. Larracuente, A. M. & Ferree, P. M. Simple method for fluorescence DNA in situ
hybridization to squashed chromosomes. J. Vis. Exp. https://doi.org/10.3791/52288
regression and FDR was computed to correct for multiple hypothesis
(2015).
testing. Then, the best performing cut-off was used when drawing 66. Ryu, T. et al. Heterochromatic breaks move to the nuclear periphery to continue
the Kaplan–Meier survival plots that were generated to visualize the recombinational repair. Nat. Cell Biol. 17, 1401–1411 (2015).
67. Schuettengruber, B. et al. Functional anatomy of polycomb and trithorax chromatin
survival differences. Hazard rates with 95% confidence intervals were
landscapes in Drosophila embryos. PLoS Biol. 7, e13 (2009).
computed to numerically assess the survival time difference between 68. Liao, Y., Smyth, G. K. & Shi, W. The R package Rsubread is easier, faster, cheaper and
the two cohorts. The statistical analysis was performed in the R statisti- better for alignment and quantification of RNA sequencing reads. Nucleic Acids Res. 47,
e47 (2019).
cal environment (www.r-project.org). The analysis results for single 69. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold change and dispersion
genes can be validated using the platforms at www.kmplot.com and for RNA-seq data with DESeq2. Genome Biol. 15, 550 (2014).
www.tnmplot.com. 70. Wehrens, R. & Kruisselbrink, J. Flexible self-organizing maps in kohonen 3.0. J. Stat. Softw.
87, 1–18 (2018).
71. Langmead, B. & Salzberg, S. L. Fast gapped-read alignment with Bowtie 2. Nat. Methods
Analysis of cohorts of patients with multiple myeloma 9, 357–359 (2012).
For gene expression profiling data from patients with multiple mye- 72. Danecek, P. et al. Twelve years of SAMtools and BCFtools. Gigascience 10, giab008
(2021).
loma, we used six cohorts that included Affymetrix gene expression 73. Zhang, Y. et al. Model-based analysis of ChIP-Seq (MACS). Genome Biol. 9, R137 (2008).
data (HGU133plus2) of purified multiple myeloma cells from the TT2 74. Herrmann, H. et al. Delineation of target expression profiles in CD34+/CD38− and CD34+/
(ref. 81) (Gene Expression Omnibus, accession number GSE2658), TT3 CD38+ stem and progenitor cells in AML and CML. Blood Adv. 4, 5118–5132 (2020).
75. de Almeida, B. P., Reiter, F., Pagani, M. & Stark, A. DeepSTARR predicts enhancer activity
(ref. 82) (accession number E-TABM-1138 accession number GSE4583) from DNA sequence and enables the de novo design of synthetic enhancers. Nat. Genet.
and Hovon83 (accession number GSE19784) cohorts (345, 158 and 282 54, 613–624 (2022).
76. Bartha, A. & Gyorffy, B. TNMplot.com: a web tool for the comparison of gene expression
newly diagnosed patients with multiple myeloma who were treated with
in normal, tumor and metastatic tissues. Int. J. Mol. Sci. 22, 2622 (2021).
high-dose melphalan and autologous haematopoietic stem cell trans- 77. Gyorffy, B. Survival analysis across the entire transcriptome identifies biomarkers with the
plantation); the Mulligan cohort84 (188 patients at relapse treated by highest prognostic power in breast cancer. Comput. Struct. Biotechnol. J. 19, 4101–4109
(2021).
proteasome inhibitor in monotherapy); the Mtp cohort non-eligible for
78. Lanczky, A. & Gyorffy, B. Web-based survival analysis tool tailored for medical research
HDT85 (63 newly diagnosed patients with multiple myeloma who were (KMplot): development and implementation. J. Med. Internet Res. 23, e27633 (2021).
not eligible for high-dose melphalan and autologous haematopoietic 79. Nagy, A., Munkacsy, G. & Gyorffy, B. Pancancer survival analysis of cancer hallmark
stem cell transplantation) and the Mtp Dara cohort85,86 (51 patients at genes. Sci. Rep. 11, 6047 (2021).
80. Li, Q., Birkbak, N. J., Gyorffy, B., Szallasi, Z. & Eklund, A. C. Jetset: selecting the optimal
relapse treated by anti-CD38 monoclonal antibody (Daratumumab)). microarray probe set to represent a gene. BMC Bioinf. 12, 474 (2011).
Gene expression data were normalized with the MAS5 algorithm and 81. Barlogie, B. et al. Total therapy 2 without thalidomide in comparison with total therapy 1:
role of intensified induction and posttransplantation consolidation therapies. Blood 107,
processing of the data was performed using the webtool genomicscape
2633–2638 (2006).
(http://www.genomicscape.com), as done previously87,88, using the 82. Pineda-Roman, M. et al. VTD combination therapy with
R environment (www.r-project.org). The prognostic values of PHC1, bortezomib-thalidomide-dexamethasone is highly effective in advanced and refractory
multiple myeloma. Leukemia 22, 1419–1427 (2008).
PHC2, PHC3, CBX2, CBX7 and BMI1 gene expression was investigated
83. Kuiper, R. et al. A gene expression signature for high-risk multiple myeloma. Leukemia 26,
using the Maxstat R function and Kaplan–Meier survival curves as 2406–2413 (2012).
84. Mulligan, G. et al. Gene expression profiling and correlation with outcome in clinical trials Research in the G.C. laboratory was supported by grants from the European Research Council
of the proteasome inhibitor bortezomib. Blood 109, 3177–3188 (2007). (Advanced Grant 3DEpi), the European CHROMDESIGN ITN project (Marie Skłodowska-Curie
85. Ovejero, S. et al. The BLM helicase is a new therapeutic target in multiple myeloma grant agreement no. 813327), the European E-RARE NEURO DISEASES grant ‘IMPACT’, by the
involved in replication stress survival and drug resistance. Front. Immunol. 13, 983181 Agence Nationale de la Recherche (PLASMADIFF3D, grant no. ANR-18-CE15-0010), by the
(2022). Fondation pour la Recherche Médicale (grant no. EQU202303016), by the MSD Avenir
86. Chemlal, D. et al. EZH2 targeting induces CD38 upregulation and response to anti-CD38 Foundation ((Project GENE-IGH) and by the French National Cancer Institute (INCa, PIT-MM
immunotherapies in multiple myeloma. Leukemia 37, 1925–1928 (2023). grant no. INCA-PLBIO18-362). M.E. was supported by RSF grant no. 20-74-10099.
87. Kassambara, A. & Moreaux, J. Analysis of global gene expression profiles. Methods Mol.
Biol. 1792, 157–166 (2018). Author contributions V.L., V.P., A.-M.M. and G.C. initiated and led the project. V.P., L.F. and V.L.
88. Kassambara, A. et al. GenomicScape: an easy-to-use web tool for gene expression data performed genetic experiments. V.P. performed immunostaining, molecular biology and
analysis. Application to investigate the molecular events in the differentiation of B cells genomic experiments. V.L. and M.D.S. performed computational analysis of genomic datasets.
into plasma cells. PLoS Comput. Biol. 11, e1004077 (2015). V.P. and A.-M.M. performed allograft experiments. B.S. performed ChIP–seq, ATAC-Seq and
89. Alaterre, E. et al. Comprehensive characterization of the epigenetic landscape in multiple CUT&RUN experiments. D.N. helped with EdU imaging. M.E., B.G. and D.C. performed
myeloma. Theranostics 12, 1715–1729 (2022). computational analysis of different tumour types. J.M. performed computational analysis of
multiple myeloma samples. C.C.R. performed irradiation experiments and N.L.B. performed
karyotyping under the guidance of I.C. V.L., V.P., A.-M.M. and G.C. wrote the manuscript. All the
Acknowledgements We thank Montpellier Resources Imagerie facility as well as the authors discussed the data and reviewed the manuscript.
Drosophila facilty (both affiliated to BioCampus University of Montpellier, CNRS, INSERM,
Montpellier, France). We thank A.-M. Popmihaylova for help with immunostaining of Drosophila Competing interests The authors declare no competing interests.
tissues. We thank J. Drouin for discussions and advice on the manuscript. We thank E. Soler
for discussions on the function of the ZEB1 protein in cancer. V.P. was supported by the Additional information
EpiGenMed cluster of Excellence funding (Programme d’Investissements d’Avenir of the Supplementary information The online version contains supplementary material available at
French Ministry of Higher Education and Research) and by la Ligue Nationale Contre le Cancer. https://doi.org/10.1038/s41586-024-07328-w.
V.L. was supported by the EpiGenMed cluster of Excellence funding (PIA of the French Ministry Correspondence and requests for materials should be addressed to A.-M. Martinez or
of Higher Education and Research). A.-M.M. was supported by the University of Montpellier G. Cavalli.
and a grant from the Fondation ARC (contract no. 216574, acronym ‘Epicancer’). B.S. was Peer review information Nature thanks the anonymous reviewers for their contribution to the
supported by INSERM. G.C. was supported by CNRS. I.C. was supported by National Institutes peer review of this work. Peer reviewer reports are available.
of Health grant no. R01GM117376 and National Science Foundation Career no. 1751197. Reprints and permissions information is available at http://www.nature.com/reprints.
