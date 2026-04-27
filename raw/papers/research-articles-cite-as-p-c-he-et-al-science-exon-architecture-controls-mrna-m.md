---
source_path: /mnt/c/Users/Administrator/Zotero/storage/479BDFUM/He 等 - 2023 - Exon architecture controls mRNA m 6 A s.pdf
ingested: 2026-04-23
sha256: e603f31f9093b48d
---

RESEARCH ARTICLES
Cite as: P. C. He et al., Science
10.1126/science.abj9090 (2023).
Exon architecture controls mRNA m6A suppression and
gene expression
P. Cody He1,2,3†, Jiangbo Wei1,3†, Xiaoyang Dou1,3†, Bryan T. Harada1,3†‡, Zijie Zhang1,3,4, Ruiqi Ge1,3, Chang
Liu1,3§, Li-Sheng Zhang1,3, Xianbin Yu1,3, Shuai Wang5, Ruitu Lyu1,3, Zhongyu Zou1,3, Mengjie Chen6,7, Chuan
He1,2,3*
1Department of Chemistry, Department of Biochemistry and Molecular Biology, Institute for Biophysical Dynamics, The University of Chicago, Chicago, IL 60637, USA.
2Committee on Immunology, The University of Chicago, Chicago, IL 60637, USA. 3Howard Hughes Medical Institute, The University of Chicago, Chicago, IL 60637, USA.
4State Key Laboratory for Conservation and Utilization of Bio-Resources, School of Life Sciences, Yunnan University, Kunming, Yunnan 650091, China. 5Department of
Neurobiology, The University of Chicago, Chicago, IL 60637, USA. 6Department of Human Genetics, The University of Chicago, Chicago, IL 60637, USA. 7Section of Genetic
Medicine, Department of Medicine, The University of Chicago, Chicago, IL 60637, USA.
†These authors contributed equally to this work. ‡Present address: Cell Press, Cambridge, MA 02139, USA. §Present address: Department of Cellular and Molecular
Medicine, University of California, San Diego, La Jolla, CA 92093, USA.
*Corresponding author. Email: chuanhe@uchicago.edu
N6–methyladenosine (m6A) is the most abundant mRNA modification and plays crucial roles in diverse
physiological processes. Utilizing a Massively Parallel Assay for m6A (MPm6A), we discover that m6A
specificity is globally regulated by “suppressors” that prevent m6A deposition in unmethylated
transcriptome regions. We identify Exon Junction Complexes (EJCs) as m6A suppressors that protect exon
junction-proximal RNA within coding sequences from methylation and regulate mRNA stability through m6A
suppression. EJC suppression of m6A underlies multiple global characteristics of mRNA m6A specificity,
with the local range of EJC protection sufficient to suppress m6A deposition in average-length internal
exons, but not in long internal and terminal exons. EJC-suppressed methylation sites co-localize with EJC-
suppressed splice sites, suggesting that exon architecture broadly determines local mRNA accessibility to
regulatory complexes.
N6–methyladenosine (m6A), the most prevalent mRNA methylation of mRNAs and m6A-mediated transcript destabi-
modification in mammals, influences wide-ranging aspects of lization. EJCs, together with interacting proteins, package
gene expression in diverse physiological and and protect long stretches of proximal RNA from cellular
pathophysiological processes (1–3). The METTL3-METTL14 methylation deposition, which may represent a general
methyltransferase complex installs m6A methylation on mechanism by which exon architecture and EJC positioning
mRNA in a common DRACH (D = A, G, or U; R= A or G; H= determine local mRNA accessibility to regulatory machiner-
A, C, or U) sequence motif, but only a fraction of DRACH ies.
sequences (~5%) in a subset of cellular transcripts are
selected for methylation (4). Additionally, m6A exhibits a Massively Parallel Assay for m6A
marked regional bias in its transcriptomic distribution, being The extent to which global m6A specificity is controlled has
strongly enriched in unusually long internal exons and near important implications for m6A regulation but is poorly un-
stop codons (5, 6). Despite the central importance of specific derstood (4). We approached this problem by asking: is the
m6A deposition in m6A-mediated gene regulation, the local sequence surrounding an m6A methylated site, when
mechanistic basis for m6A specificity has remained poorly uncoupled from its endogenous context, sufficient to specify
understood. methylation at that site? Conversely, is the local sequence
In this study, we discover the existence of prevalent regu- surrounding an unmethylated DRACH site, when uncoupled
latory mechanisms that restrict m6A methylation to specific from its endogenous context, sufficient to prevent methyla-
transcript regions through targeted suppression of m6A in tion at that site?
unmethylated regions. We find that pre-mRNA splicing selec- To assess this systematically on an epitranscriptome-wide
tively suppresses m6A deposition in average-length internal scale, we developed a Massively Parallel Reporter Assay
exons, but not in longer exons. We identify Exon Junction (MPRA) that enables high-throughput assessment of the m6A
Complexes (EJC) as major m6A suppressors that mediate this methylation status of thousands of designed sequences,
effect and control several key characteristics of global m6A which we termed Massively Parallel assay for m6A (MPm6A)
specificity. EJC depletion results in pervasive aberrant (Fig. 1A and fig. S1A). In the MPm6A workflow, thousands of
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 1
endogenously methylated m6A sites and endogenously un- than endogenous m6A sites (median = 915 nt) (Fig. 1D). These
methylated DRACH sites, with 102 nucleotides of sequence observations suggest that endogenous m6A enrichment in
surrounding each site, were synthesized and cloned into the long internal exons may be a consequence of suppression of
3 UTR of a plasmid-based intronless GFP transgene. For m6A deposition in shorter internal exons, which comprise
′
each sequence, we also designed a corresponding negative most exons (90% of internal exons are < 246 nt) (Fig. 1E). 942
control sequence in which all DRACH motifs were mutated genes containing suppressed m6A sites did not contain any
to prevent methylation. The sequences were expressed and endogenous m6A peaks on their transcripts (fig. S5B). Sup-
then m6A methylated through transfection into cells, or, pression of these sites appears to involve suppression of m6A
when specified, through in vitro transcription and in vitro deposition rather than active demethylation, as binding sites
m6A methylation. The methylation status of each individual for RBM15, a METTL3-METTL14 methyltransferase complex
sequence was assessed by its enrichment following m6A-im- accessory subunit, were highly enriched near endogenous
munoprecipitation (IP) of mRNA. We selected 6,897 HeLa m6A sites compared to suppressed m6A sites (fig. S6A), while
m6A sites and 3,058 unmethylated DRACH sites to assay in FTO and ALKBH5 binding sites were not significantly en-
HeLa cells and validated the assay’s precision and accuracy riched near suppressed sites and exhibited little binding near
(fig. S1, B to D). suppressed sites overall (fig. S6B). These results were unex-
pected as previous reports on m6A specificity had mainly fo-
Widespread mRNA m6A suppression controls m6A epi- cused on activating mechanisms (7–12). Our MPm6A assay
transcriptome specificity suggests the existence of unknown m6A “suppressors” that
When we compared the methylation levels of the endoge- govern global m6A specificity by suppressing m6A deposition.
nously methylated sequences to their negative control se-
quences, we found that 92.8% of the sequences exhibited Pre-mRNA splicing suppresses m6A methylation proxi-
significant methylation in this reporter assay (Fig. 1B and fig. mal to splice sites
S1E), indicating that most endogenously methylated sites do We next examined the relative enrichment of binding sites
not strictly require their larger surrounding native context for 120 RBPs near endogenously methylated versus sup-
for methylation. Unexpectedly, 90.2% of endogenously un- pressed m6A sites to identify candidate suppressors (13). Sev-
methylated sequences also exhibited significant methylation eral spliceosome components (BUD13, SF3B4, EFTUD2) were
(Fig. 1B and fig. S1E). The MPm6A enrichment scores of the significantly enriched near suppressed sites, suggesting that
endogenously unmethylated group were similar to the endog- splicing may suppress m6A (fig. S6A). Because suppressed
enously methylated group, despite their diverging endoge- m6A sites in CDS primarily reside within average-length in-
nous methylation states (Fig. 1B). We observed similar results ternal exons, we hypothesized that the splicing of average-
when the sequences were in vitro transcribed and methylated length internal exons may suppress m6A methylation. To test
with recombinant METTL3-METTL14 (fig. S2). Thus, thou- this, we cloned a suppressed m6A site from an average-length
sands of endogenously unmethylated DRACH sites became internal exon in the CRY1 gene (fig. S7A) into a rabbit beta-
methylated when they were uncoupled from their endoge- globin minigene reporter (BG), as well as a version with the
nous contexts and expressed in an artificial reporter context. introns removed (BG i1,i2). First, we cloned the suppressed
Δ
We term these identified sites “suppressed m6A sites”. We val- CRY1 site and 50/51 nt of flanking sequence into the internal
idated these results for three selected sequences (fig. S1F), exon, or in the last exon of these constructs. Notably, the
and confirmed that methylation was not notably influenced spliced construct strongly suppressed methylation of the se-
by the CMV promoter of the MPm6A plasmid (fig. S3). We quence placed within the internal exon, but not within the
observed similar results when sequences were expressed last exon (fig. S7B). Removal of either intron (BG i1 CRY1
Δ
within CDS or 5 UTR, though m6A enrichment was signifi- 102, BG i2 CRY1 102) resulted in partial loss of suppression,
′ Δ
cantly lower for many sequences when placed in the CDS or indicating that splicing of both introns contributed to meth-
5 UTR versus in the 3 UTR (fig. S4, A to D). This suggests ylation suppression (Fig. 2A). Consistent with this notion, de-
′ ′
that 5 regions are generally less conducive for m6A methyl- letion of all splice sites also resulted in a decrease in m6A
′
ation than 3 regions (fig. S4E). Collectively, these results re- suppression (fig. S7C). Cloning in 912 nt of the CRY1 exonic
′
veal the existence of thousands of suppressed m6A sites that sequence surrounding the suppressed site into the internal
are silenced by unknown mechanisms. exon (BG CRY1 912), forming a long internal exon, resulted in
We noted that suppressed m6A sites were enriched in the a loss of suppression (Fig. 2A). We hypothesized that the sup-
CDS and 3 UTR and were depleted near the stop codon, pression is dependent on the proximity of the m6A site, lo-
′
which is the reverse of endogenous m6A site enrichment (Fig. cated within the center of the exon, to splice sites. Expanding
1C and fig. S5A). Further, suppressed m6A sites in internal the length of the BG CRY1 102 internal exon by cloning in
exons reside within much shorter exons (median = 167 nt) larger amounts of CRY1 flanking exonic sequence resulted in
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 2
a progressive loss of suppression, with a > 476 nt internal by MPm6A to contain suppressed m6A sites, 46% become
exon unable to suppress m6A (Fig. 2B and fig. S7D). These methylated upon EIF4A3 and/or RBM8A KD, including the
results reveal a causal role for pre-mRNA splicing in m6A reg- CRY1 suppressed site (fig. S8E), with three selected sup-
ulation. pressed sites validated (fig. S8, F and G) (21). Furthermore,
EIF4A3 KD substantially alleviated the previously observed
Exon junction complexes control m6A epitranscriptome m6A suppression within the internal exon of BG CRY1 102
specificity (fig. S8H).
We next sought to understand the mechanism by which splic- Consistent with our model, newly methylated and hyper-
ing suppresses m6A deposition. Exon junction complexes methylated regions were highly enriched in average-length
(EJCs) are deposited by spliceosomes onto mRNA ~24 nt up- internal exons within CDSs (Fig. 3, C to E, and fig. S8, I and
stream of exon-exon junctions and plays multifaceted roles in J), with transcriptome-wide increases in m6A enrichment in
gene expression regulation (14, 15). Notably, two recent stud- exon junction-proximal regions observed (fig.S9, A and B)
ies reported that EJCs efficiently block splicing at proximal upon EIF4A3 or RBM8A KD. EIF4A3 KD disrupted m6A epi-
aberrant splice sites (16, 17). Additionally, EJCs, together with transcriptome specificity globally, resulting in substantial
interacting serine and arginine-rich (SR) proteins, package loss of enrichment of m6A peaks in long internal exons and
and compact mRNA and can protect long stretches of proxi- increased density of m6A in the CDS relative to the stop codon
mal RNA from nuclease accessibility in vitro, and also block (Fig. 3, D and E). It was previously reported that the peak of
5 to 3 exonuclease degradation in vivo (18, 19). We rea- m6A density near stop codons on metagene plots can be more
′ ′
soned that suppressed m6A sites within average-length inter- precisely visualized as an increased enrichment 150 nt past
nal exons are within relatively close proximity to both an the start of last exons (6). EIF4A3 KD resulted in a global in-
upstream and downstream EJC. Conversely, m6A sites within crease in m6A enrichment < 150 nt past the start of last exons
long internal exons and near stop codons (which generally (fig. S9, A to C), indicating that EJC suppression of methyla-
reside in long last exons) can be hundreds of nucleotides tion proximal to last exon-exon junctions is responsible for
away from the nearest EJC. We therefore hypothesized that the characteristic m6A peak density near stop codons. While
EJCs could mediate the splice site-proximal suppression of most transcripts exhibited hypermethylation and contained
m6A we observed. one or more endogenous m6A peaks upon EIF4A3 KD, over a
We knocked down (KD) the core EJC factor EIF4A3 in thousand transcripts that ordinarily lack endogenous m6A
HeLa cells and assessed the effect on m6A deposition tran- peaks also gained aberrant m6A methylation upon EIF4A3
scriptome-wide using m6A-MeRIP-seq. Notably, 24,350 re- KD, revealing a major role for EJCs in suppressing m6A dep-
gions were significantly hypermethylated upon EIF4A3 KD, osition on the subset of transcripts that ordinarily are not
while 3,140 regions were hypomethylated (Fig. 3A). 39% of subject to m6A regulation (fig. S9, D to F).
these hypermethylated regions exhibited a greater than 8- The widespread suppression of m6A by the EJCs also im-
fold increase in m6A enrichment compared to the non-target- plies that many m6A are deposited following splicing, which
ing siRNA control. We knocked down RBM8A, another core we confirmed using pulse-chase metabolic labeling experi-
EJC factor (20), and observed similar, though relatively ments and UHPLC-QQQ-MS/MS (supplementary text and fig.
milder, transcriptome-wide m6A changes, with 14,034 signif- S10). Two genes used in gene therapies for mucopolysaccha-
icantly hypermethylated regions observed, of which 57% ridosis type II and spinal muscular atrophy, IDS and SMN,
overlapped with hypermethylated regions observed in contain EJC-suppressed m6A sites in their mRNAs, respec-
EIF4A3 KD (Fig. 3A and fig. S8, A and B). The relatively tively. As expected, when these mRNAs were expressed from
milder m6A changes upon RBM8A KD may result from rela- cDNA constructs, and thus not bound by EJCs, they were sig-
tively lower KD efficiency (table S1) or may indicate a nificantly hypermethylated relative to the corresponding en-
stronger requirement of EIF4A3 for suppression. Concordant dogenous mRNAs (fig. S11). Further, lncRNAs that contain
with these transcriptome-wide m6A changes, using UHPLC- three or more exons globally exhibit EJC suppression of m6A
QQQ-MS/MS, we found that EIF4A3 KD increased global lev- in internal exons, while those with two or less do not (sup-
els of m6A in polyadenylated RNA by two-fold, while RBM8A plementary text and fig. S12). We depleted EIF4A3 with a dif-
KD resulted in a ~25% increase (fig. S8C). ferent siRNA in HeLa cells, and knocked down EIF4A3 in
94% of hypermethylated regions from EIF4A3 KD and HEK293T cells as well as in a glioblastoma cancer cell line
82% of hypermethylated regions from RBM8A KD did not (U87) that is sensitive to EIF4A3 perturbation (22), and ob-
overlap with m6A peaks identified under the non-targeting served similar transcriptome-wide m6A changes in each case
siRNA control conditions, suggesting that these regions con- (figs. S13 to S15). Altogether, our results indicate that spliceo-
tain newly methylated suppressed m6A sites (Fig. 3, A and B, somes widely suppress m6A methylation via deposition of
and fig. S8D). Indeed, out of 1,024 CDS sequences identified EJCs that protect proximal RNA from methylation.
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 3
EJCs regulate mRNA stability by suppressing m6A the strongest correlations and found that the majority (>
methylation 70%) exhibited a negative correlation between m6A and
m6A is known to mainly accelerate mRNA degradation via the EIF4A3 levels in different tissues. Further, m6A levels of these
reader protein YTHDF2 (23, 24). Accordingly, we observed genes also negatively correlated with their transcript abun-
globally reduced mRNA half-life of hypermethylated tran- dances (fig. S21B). Similar trends were also observed in
scripts (~90%) upon EIF4A3 KD (Fig. 4, A and B). Consist- mouse tissues (fig. S21C). These results further support m6A
ently, we observed generally increased YTHDF2 binding on suppression by EJCs and subsequently mRNA stability regu-
hypermethylated mRNAs, accompanied with the decreased lation in mammalian tissues.
mRNA half-life (Fig. 4C). YTHDF2 KD could rescue acceler- Notably, we observed the lowest EIF4A3 expressions in
ated degradation of YTHDF2 target transcripts upon EIF4A3 brain tissues, which exhibited the highest overall mRNA m6A
KD (fig. S16). Further, the density of EJC-loading on tran- levels (fig. S21A). We further compared the methylome of the
scripts (estimated by the number of exons within CDS regions human cerebellum (lowest EIF4A3 level and highest overall
per 1 kb) correlated with transcriptome-wide mRNA stability mRNA m6A) with that of the heart (higher EIF4A3 level and
(fig. S17). Higher EJC density on transcripts tended to corre- lower overall mRNA m6A). Regions that are hypermethylated
late with reduced m6A methylation and higher mRNA stabil- in the cerebellum (compared to heart) reside within short in-
ity, and the strength of this correlation was diminished by ternal exons (fig. S21D), suggesting reduced m6A suppression
Mettl3 KO (fig. S17, A and B). due to low EIF4A3 expression in cerebellum. This association
We also found that METTL3 depletion could generally re- between high m6A level and low EIF4A3 expression in cere-
duce the expression level changes of hypermethylated genes bellum was attenuated upon depletion of METTL3 (fig. S21C).
upon EJC depletion in HeLa cells (supplementary text and These observations further indicate the widespread suppres-
fig. S18), indicating that these EJC-dependent gene expres- sion by EJCs contributes to tissue-specific m6A deposition.
sion changes are at least in part mediated by m6A methyla- We also found that a subset of EJC-suppressed m6A sites
tion. physiologically escape suppression in certain tissues via
While the vast majority of hypermethylated transcripts methylation of alternative transcript isoforms. These
were destabilized by EIF4A3 KD, a small subset of hyper- isoforms contain longer exons and thus altered EJC position-
methylated transcripts were stabilized (Fig. 4A). One example ing; methylation of these isoforms generates tissue-specific
is p53, which mediates neurodevelopmental defects in mouse m6A patterns (supplementary text and fig. S22).
models of EJC haploinsufficiency (25). The TP53 transcript Lastly, the effect of exon-intron architecture on mRNA
was hypermethylated but also up-regulated upon EIF4A3 KD. stability may have co-evolved with YTHDF2 in vertebrates.
Mechanistically, we observed increased binding to TP53 The strong correlation between EJC loading, represented by
mRNA by IGF2BP proteins, which are known to stabilize the number of exons, and mRNA level across tissues is main-
methylated transcripts (supplementary text and fig. S19). In tained across humans, mice, and zebrafish, but not fly and
summary, while the predominant effect of EJC-mediated m6A worm, which lack YTHDF2 orthologs (supplementary text
suppression is to stabilize mRNAs by preventing the and fig. S23).
YTHDF2-mediated decay, in a minority of instances hyper-
methylated transcripts can be stabilized by other mecha- EJCs and peripheral EJC factor RNPS1 protect exon
nisms, such as binding by IGF2BPs (26). junction-proximal RNA regions from aberrant mRNA
Consistent with a general role for m6A in promoting trans- processing
lation (12, 27), EIF4A3 KD led to slightly increased translation We did not observe interactions between the methyltransfer-
efficiency of hypermethylated transcripts, with more highly ase complex and EJC complexes (fig. S24), suggesting that
hypermethylated transcripts exhibiting greater increases in steric hindrance from EJCs, rather than a specific inhibitory
translation efficiency (fig. S20), although the impact was interaction, accounts for methylation suppression. Nuclear
modest relative to the effects observed on mRNA stability. EJCs bound with the peripheral EJC factor RNPS1 multimer-
ize and associate with wide variety of SR and SR-like proteins
Differential m6A methylation across tissues and species to package and compact mRNA into higher-order, megadal-
through EJC suppression ton-scale mRNPs that ensheathe proximal RNA well beyond
Our model suggests that the cellular EJC levels may impact the canonical EJC deposition sites (18, 29, 30). Tens to hun-
global mRNA m6A deposition in different tissues. Indeed, we dreds of nucleotides of proximal RNA could be protected by
observed a negative correlation between EIF4A3 expression this mega-complex from nuclease digestion due to this pack-
level and global mRNA m6A modification level in 25 different aging (18, 31). To examine whether the mRNA packaging
human tissues with available transcriptome-wide m6A pro- function of the EJC-mediates suppression of proximal meth-
files (fig. S21A) (28). We examined the top 10% of genes with ylation, we isolated EJCs/EJC-bound RNA from cellular
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 4
extracts, digested away physically accessible RNA with in regulators: “suppressors”, which broadly suppress the depo-
vitro nuclease treatment, and then measured m6A levels on sition of m6A (fig. S28). EJCs appear to be a major regulator
the EJC-protected RNA footprints (fig. S25, A and B). EJC- of m6A deposition that mediate multiple key aspects of global
protected footprints were strongly depleted of m6A, indicat- m6A epitranscriptome specificity, including enrichment of
ing that these inaccessible RNA regions are largely protected m6A in long internal exons, depletion of m6A in CDSs and en-
from m6A deposition within cells (fig. S25C). EJCs also pro- richment of m6A in last exons near stop codons, and methyl-
tected these footprints from in vitro methylation by recombi- ation selectivity for transcripts possessing long internal
nant METTL3-METTL14 (fig. S25D). This was not due to exons. This mechanism may also explain the high abundance
general inhibition of methyltransferase activity or lack of of m6A on certain non-coding RNAs, such as LINE-1 elements
methylatable sites on the EJC footprints, as free, unmethyl- that are generally unspliced and thus not bound by the EJCs
ated RNA spiked into the methylation reaction as well as (32, 33). Further, our systematic analysis of m6A determi-
deproteinized footprints were both robustly methylated (fig. nants using MPm6A may suggest the existence of additional
S25, D and E). Therefore, EJCs suppress local m6A deposition m6A suppressing pathways, including m6A suppression
by packaging proximal RNA. within the CDS, as EIF4A3 KD does not appear to completely
We next asked whether the peripheral EJC factor RNPS1, restore methylation to unspliced levels (supplementary text,
which associates with high molecular weight EJCs in these fig. S8H, and fig. S29).
highly packaged mRNP structures (29), plays a role. RNPS1 Our results point to exon length within transcripts as a
knockdown led to substantial transcript m6A hypermethyla- functionally relevant element for post-transcriptional gene
tion within average-length internal exons and CDS regions expression regulation. Mammalian EJCs stably bind the vast
(Fig. 5, A to C, and fig. S26, A to C). We detected fewer hyper- majority of pre-translational mRNAs in the transcriptome at
methylated regions overall compared to depletion of the core closely spaced intervals. Long internal exons and terminal ex-
EJC factors; however, we did observe high overlap (45%) be- ons, which usually encode UTRs, are notably free of EJCs.
tween siRNPS1 hypermethylated regions and This widespread binding, in conjunction with their mRNA
siEIF4A3/siRBM8A hypermethylated regions (Fig. 5C and fig. packaging function, appears to uniquely position EJCs to
S26C). In contrast, depletion of UPF1, a central NMD factor broadly determine mRNA accessibility to regulatory machin-
that interacts with the EJC in the cytoplasm, did not result in eries, such as the m6A methylation and splicing machineries
m6A changes similar to those of the core EJC (fig. S27). (fig. S30). Our work has relevance for the use of cDNA expres-
The ability of EJCs to protect proximal RNA regions from sion constructs in research studies and gene therapies, as loss
methylation resembles the recently characterized EJC- and of endogenous mRNA exon architecture and EJC protection
RNPS1-mediated suppression of proximal aberrant splice results in m6A hypermethylation (fig. S11), which could mod-
sites and recursive splicing (16, 17). Transcriptome-wide, EJC- ulate gene expression outcome. Finally, our study also sug-
suppressed splice sites significantly colocalize with EJC- gests that exon length and architecture co-evolved with
suppressed m6A sites (supplementary text; Fig. 4, C to E; fig. mRNA processing steps as an additional regulatory layer of
S26, D to F; and table S2). Altogether, these results suggest gene expression.
that RNPS1-associated EJCs suppress both local cellular m6A
methylation and splicing through packaging of proximal REFERENCES AND NOTES
RNA and point to exon architecture as an important determi-
1. M. Frye, B. T. Harada, M. Behm, C. He, RNA modifications modulate gene expression
nant of local RNA accessibility to regulatory machineries. Ad- during development. Science 361, 1346–1349 (2018).
ditionally, beyond components of the m6A methyltransferase doi:10.1126/science.aau1646 Medline
2. W. V. Gilbert, T. A. Bell, C. Schaening, Messenger RNA modifications: Form,
complex, a number of other RBPs also exhibit preferential
distribution, and function. Science 352, 1408–1412 (2016).
binding at long internal exons, suggesting that EJCs may reg-
doi:10.1126/science.aad8711 Medline
ulate mRNA accessibility to a broader range of mRNA regu- 3. I. A. Roundtree, M. E. Evans, T. Pan, C. He, Dynamic RNA modifications in gene
lators in addition to the splicing and m6A methylation expression regulation. Cell 169, 1187–1200 (2017).
doi:10.1016/j.cell.2017.05.045 Medline
machineries through their mRNA packaging function (sup-
4. P. C. He, C. He, m6A RNA methylation: From mechanisms to therapeutic potential.
plementary text and fig. S28).
EMBO J. 40, e105977 (2021). doi:10.15252/embj.2020105977 Medline
5. D. Dominissini, S. Moshitch-Moshkovitz, S. Schwartz, M. Salmon-Divon, L. Ungar, S.
Discussion Osenberg, K. Cesarkas, J. Jacob-Hirsch, N. Amariglio, M. Kupiec, R. Sorek, G.
Rechavi, Topology of the human and mouse m6A RNA methylomes revealed by
Previously identified m6A effector proteins fall broadly into
m6A-seq. Nature 485, 201–206 (2012). doi:10.1038/nature11112 Medline
three categories according to their activities: “writers”, which
6. S. Ke, E. A. Alemu, C. Mertens, E. C. Gantman, J. J. Fak, A. Mele, B. Haripal, I. Zucker-
catalyze m6A methylation, “readers”, which preferentially Scharff, M. J. Moore, C. Y. Park, C. B. Vågbø, A. Kusśnierczyk, A. Klungland, J. E.
bind m6A, and “erasers”, which reverse m6A methylation. Darnell Jr., R. B. Darnell, A majority of m6A residues are in the last exons, allowing
the potential for 3′ UTR regulation. Genes Dev. 29, 2037–2053 (2015).
Here we establish the EJCs as a member of a new class of m6A
doi:10.1101/gad.269415.115 Medline
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 5
7. I. Barbieri, K. Tzelepis, L. Pandolfini, J. Shi, G. Millán-Zambrano, S. C. Robson, D. N6-methyladenosine modification. Angew. Chem. Int. Ed. 57, 15995–16000
Aspris, V. Migliori, A. J. Bannister, N. Han, E. De Braekeleer, H. Ponstingl, A. (2018). doi:10.1002/anie.201807942 Medline
Hendrick, C. R. Vakoc, G. S. Vassiliou, T. Kouzarides, Promoter-bound METTL3 22. W. Tang, D. Wang, L. Shao, X. Liu, J. Zheng, Y. Xue, X. Ruan, C. Yang, L. Liu, J. Ma,
maintains myeloid leukaemia by m6A-dependent translation control. Nature 552, Z. Li, Y. Liu, LINC00680 and TTN-AS1 stabilized by EIF4A3 promoted malignant
126–131 (2017). doi:10.1038/nature24678 Medline biological behaviors of glioblastoma cells. Mol. Ther. Nucleic Acids 19, 905–921
8. A. Bertero, S. Brown, P. Madrigal, A. Osnato, D. Ortmann, L. Yiangou, J. Kadiwala, (2020). doi:10.1016/j.omtn.2019.10.043 Medline
N. C. Hubner, I. R. de Los Mozos, C. Sadée, A.-S. Lenaerts, S. Nakanoh, R. Grandy, 23. X. Wang, Z. Lu, A. Gomez, G. C. Hon, Y. Yue, D. Han, Y. Fu, M. Parisien, Q. Dai, G.
E. Farnell, J. Ule, H. G. Stunnenberg, S. Mendjan, L. Vallier, The SMAD2/3 Jia, B. Ren, T. Pan, C. He, N6-methyladenosine-dependent regulation of
interactome reveals that TGF controls m6A mRNA methylation in pluripotency. messenger RNA stability. Nature 505, 117–120 (2014). doi:10.1038/nature12730
β
Nature 555, 256–259 (2018). doi:10.1038/nature25784 Medline Medline
9. L. Fish, A. Navickas, B. Culbertson, Y. Xu, H. C. B. Nguyen, S. Zhang, M. Hochman, 24. H. Du, Y. Zhao, J. He, Y. Zhang, H. Xi, M. Liu, J. Ma, L. Wu, YTHDF2 destabilizes
R. Okimoto, B. D. Dill, H. Molina, H. S. Najafabadi, C. Alarcón, D. Ruggero, H. m6A-containing RNA through direct recruitment of the CCR4-NOT deadenylase
Goodarzi, Nuclear TARBP2 drives oncogenic dysregulation of RNA splicing and complex. Nat. Commun. 7, 12626 (2016). doi:10.1038/ncomms12626 Medline
decay. Mol. Cell 75, 967–981.e9 (2019). doi:10.1016/j.molcel.2019.06.001 25. H. Mao, J. J. McMahon, Y.-H. Tsai, Z. Wang, D. L. Silver, Haploinsufficiency for Core
Medline Exon Junction Complex Components Disrupts Embryonic Neurogenesis and
10. B. Slobodin, R. Han, V. Calderone, J. A. F. O. Vrielink, F. Loayza-Puch, R. Elkon, R. Causes p53-Mediated Microcephaly. PLOS Genet. 12, e1006282 (2016).
Agami, Transcription impacts the efficiency of mRNA translation via co- doi:10.1371/journal.pgen.1006282 Medline
transcriptional N6-adenosine methylation. Cell 169, 326–337.e12 (2017). 26. H. Huang, H. Weng, W. Sun, X. Qin, H. Shi, H. Wu, B. S. Zhao, A. Mesquita, C. Liu, C.
doi:10.1016/j.cell.2017.03.031 Medline L. Yuan, Y.-C. Hu, S. Hüttelmaier, J. R. Skibbe, R. Su, X. Deng, L. Dong, M. Sun, C.
11. H. Huang, H. Weng, K. Zhou, T. Wu, B. S. Zhao, M. Sun, Z. Chen, X. Deng, G. Xiao, F. Li, S. Nachtergaele, Y. Wang, C. Hu, K. Ferchen, K. D. Greis, X. Jiang, M. Wei, L. Qu,
Auer, L. Klemm, H. Wu, Z. Zuo, X. Qin, Y. Dong, Y. Zhou, H. Qin, S. Tao, J. Du, J. Liu, J.-L. Guan, C. He, J. Yang, J. Chen, Recognition of RNA N6-methyladenosine by
Z. Lu, H. Yin, A. Mesquita, C. L. Yuan, Y.-C. Hu, W. Sun, R. Su, L. Dong, C. Shen, C. IGF2BP proteins enhances mRNA stability and translation. Nat. Cell Biol. 20, 285–
Li, Y. Qing, X. Jiang, X. Wu, M. Sun, J.-L. Guan, L. Qu, M. Wei, M. Müschen, G. 295 (2018). doi:10.1038/s41556-018-0045-z Medline
Huang, C. He, J. Yang, J. Chen, Histone H3 trimethylation at lysine 36 guides m6A 27. X. Wang, B. S. Zhao, I. A. Roundtree, Z. Lu, D. Han, H. Ma, X. Weng, K. Chen, H. Shi,
RNA modification co-transcriptionally. Nature 567, 414–419 (2019). C. He, N6-methyladenosine modulates messenger RNA translation efficiency. Cell
doi:10.1038/s41586-019-1016-7 Medline 161, 1388–1399 (2015). doi:10.1016/j.cell.2015.05.014 Medline
12. Z. Zhang, K. Luo, Z. Zou, M. Qiu, J. Tian, L. Sieh, H. Shi, Y. Zou, G. Wang, J. Morrison, 28. J. Liu, K. Li, J. Cai, M. Zhang, X. Zhang, X. Xiong, H. Meng, X. Xu, Z. Huang, J. Peng,
A. C. Zhu, M. Qiao, Z. Li, M. Stephens, X. He, C. He, Genetic analyses support the J. Fan, C. Yi, Landscape and regulation of m6A and m6Am methylome across
contribution of mRNA N6-methyladenosine (m6A) modification to human disease human and mouse tissues. Mol. Cell 77, 426–440.e6 (2020).
heritability. Nat. Genet. 52, 939–949 (2020). doi:10.1038/s41588-020-0644-z doi:10.1016/j.molcel.2019.09.032 Medline
Medline 29. J. W. Mabin, L. A. Woodward, R. D. Patton, Z. Yi, M. Jia, V. H. Wysocki, R.
13. E. L. Van Nostrand, P. Freese, G. A. Pratt, X. Wang, X. Wei, R. Xiao, S. M. Blue, J.-Y. Bundschuh, G. Singh, The exon junction complex undergoes a compositional
Chen, N. A. L. Cody, D. Dominguez, S. Olson, B. Sundararaman, L. Zhan, C. Bazile, switch that alters mRNP structure and nonsense-mediated mRNA decay activity.
L. P. B. Bouvrette, J. Bergalet, M. O. Duff, K. E. Garcia, C. Gelboin-Burkhart, M. Cell Rep. 25, 2431–2446.e7 (2018). doi:10.1016/j.celrep.2018.11.046 Medline
Hochman, N. J. Lambert, H. Li, M. P. McGurk, T. B. Nguyen, T. Palden, I. Rabano, 30. M. Metkar, H. Ozadam, B. R. Lajoie, M. Imakaev, L. A. Mirny, J. Dekker, M. J. Moore,
S. Sathe, R. Stanton, A. Su, R. Wang, B. A. Yee, B. Zhou, A. L. Louie, S. Aigner, X.- Higher-order organization principles of pre-translational mRNPs. Mol. Cell 72,
D. Fu, E. Lécuyer, C. B. Burge, B. R. Graveley, G. W. Yeo, A large-scale binding and 715–726.e3 (2018). doi:10.1016/j.molcel.2018.09.012 Medline
functional map of human RNA-binding proteins. Nature 583, 711–719 (2020). 31. H. Le Hir, E. Izaurralde, L. E. Maquat, M. J. Moore, The spliceosome deposits
doi:10.1038/s41586-020-2077-3 Medline multiple proteins 20-24 nucleotides upstream of mRNA exon-exon junctions.
14. H. Le Hir, J. Saulière, Z. Wang, The exon junction complex as a node of post- EMBO J. 19, 6860–6869 (2000). doi:10.1093/emboj/19.24.6860 Medline
transcriptional networks. Nat. Rev. Mol. Cell Biol. 17, 41–54 (2016). 32. J. Liu, X. Dou, C. Chen, C. Chen, C. Liu, M. M. Xu, S. Zhao, B. Shen, Y. Gao, D. Han,
doi:10.1038/nrm.2015.7 Medline C. He, N6-methyladenosine of chromosome-associated regulatory RNA regulates
15. V. Boehm, N. H. Gehring, Exon junction complexes: Supervising the gene chromatin state and transcription. Science 367, 580–586 (2020).
expression assembly line. Trends Genet. 32, 724–735 (2016). doi:10.1126/science.aay6018 Medline
doi:10.1016/j.tig.2016.09.003 Medline 33. J. Wei, X. Yu, L. Yang, X. Liu, B. Gao, B. Huang, X. Dou, J. Liu, Z. Zou, X.-L. Cui, L.-
16. V. Boehm, T. Britto-Borges, A.-L. Steckelberg, K. K. Singh, J. V. Gerbracht, E. S. Zhang, X. Zhao, Q. Liu, P. C. He, C. Sepich-Poore, N. Zhong, W. Liu, Y. Li, X. Kou,
Gueney, L. Blazquez, J. Altmüller, C. Dieterich, N. H. Gehring, Exon junction Y. Zhao, Y. Wu, X. Cheng, C. Chen, Y. An, X. Dong, H. Wang, Q. Shu, Z. Hao, T. Duan,
complexes suppress spurious splice sites to safeguard transcriptome integrity. Y.-Y. He, X. Li, S. Gao, Y. Gao, C. He, FTO mediates LINE1 m6A demethylation and
Mol. Cell 72, 482–495.e7 (2018). doi:10.1016/j.molcel.2018.08.030 Medline chromatin regulation in mESCs and mouse development. Science 376, 968–973
17. L. Blazquez, W. Emmett, R. Faraway, J. M. B. Pineda, S. Bajew, A. Gohr, N. (2022). doi:10.1126/science.abe9582 Medline
Haberman, C. R. Sibley, R. K. Bradley, M. Irimia, J. Ule, Exon junction complex 34. P. C. He, X. Dou, Custom scripts associated with “Exon architecture controls
shapes the transcriptome by repressing recursive splicing. Mol. Cell 72, 496– mRNA m6A suppression and gene expression”, Zenodo (2023);
509.e9 (2018). doi:10.1016/j.molcel.2018.09.033 Medline https://doi.org/10.5281/zenodo.7541415.
18. G. Singh, A. Kucukural, C. Cenik, J. D. Leszyk, S. A. Shaffer, Z. Weng, M. J. Moore, 35. C. C. Uphoff, H. G. Drexler, in Cancer Cell Culture: Methods and Protocols, S. P.
The cellular EJC interactome reveals higher-order mRNP structure and an EJC-SR Langdon, Ed., vol. 88 of Methods in Molecular Medicine (Humana Press, 2004),
protein nexus. Cell 151, 750–764 (2012). doi:10.1016/j.cell.2012.10.007 Medline pp. 319–326.
19. W.-C. Lee, B.-H. Hou, C.-Y. Hou, S.-M. Tsao, P. Kao, H.-M. Chen, Widespread exon 36. Y. Yue, J. Liu, X. Cui, J. Cao, G. Luo, Z. Zhang, T. Cheng, M. Gao, X. Shu, H. Ma, F.
junction complex footprints in the RNA degradome mark mRNA degradation Wang, X. Wang, B. Shen, Y. Wang, X. Feng, C. He, J. Liu, VIRMA mediates
before steady state translation. Plant Cell 32, 904–922 (2020). preferential m6A mRNA methylation in 3'UTR and near stop codon and associates
doi:10.1105/tpc.19.00666 Medline with alternative polyadenylation. Cell Discov. 4, 10 (2018). doi:10.1038/s41421-
20. T. Ø. Tange, T. Shibuya, M. S. Jurica, M. J. Moore, Biochemical analysis of the EJC 018-0019-0 Medline
reveals two new factors and a stable tetrameric protein core. RNA 11, 1869–1883 37. Y. Zhou, P. Zeng, Y.-H. Li, Z. Zhang, Q. Cui, SRAMP: Prediction of mammalian N6-
(2005). doi:10.1261/rna.2155905 Medline methyladenosine (m6A) sites based on sequence-derived features. Nucleic Acids
21. Y. Xiao, Y. Wang, Q. Tang, L. Wei, X. Zhang, G. Jia, An elongation- and ligation-based Res. 44, e91 (2016). doi:10.1093/nar/gkw104 Medline
qPCR amplification method for the radiolabeling-free detection of locus-specific 38. J. Ernst, P. Kheradpour, T. S. Mikkelsen, N. Shoresh, L. D. Ward, C. B. Epstein, X.
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 6
Zhang, L. Wang, R. Issner, M. Coyne, M. Ku, T. Durham, M. Kellis, B. E. Bernstein, doi:10.1016/j.molcel.2012.05.021 Medline
Mapping and analysis of chromatin state dynamics in nine human cell types. 58. M. Bartosovic, H. C. Molares, P. Gregorova, D. Hrossova, G. Kudla, S. Vanacova,
Nature 473, 43–49 (2011). doi:10.1038/nature09906 Medline N6-methyladenosine demethylase FTO targets pre-mRNAs and regulates
39. D. Kim, B. Langmead, S. L. Salzberg, HISAT: A fast spliced aligner with low memory alternative splicing and 3′-end processing. Nucleic Acids Res. 45, 11356–11370
requirements. Nat. Methods 12, 357–360 (2015). doi:10.1038/nmeth.3317 (2017). doi:10.1093/nar/gkx778 Medline
Medline 59. A. Busch, K. J. Hertel, HEXEvent: A database of Human EXon splicing Events.
40. Z. Zhang, Q. Zhan, M. Eckert, A. Zhu, A. Chryplewicz, D. F. De Jesus, D. Ren, R. N. Nucleic Acids Res. 41, D118–D124 (2013). doi:10.1093/nar/gks969 Medline
Kulkarni, E. Lengyel, C. He, M. Chen, RADAR: Differential analysis of MeRIP-seq 60. N. L. Bray, H. Pimentel, P. Melsted, L. Pachter, Near-optimal probabilistic RNA-seq
data with a random effect model. Genome Biol. 20, 294 (2019). quantification. Nat. Biotechnol. 34, 525–527 (2016). doi:10.1038/nbt.3519
doi:10.1186/s13059-019-1915-9 Medline Medline
41. G. Yu, L.-G. Wang, Y. Han, Q.-Y. He, clusterProfiler: An R package for comparing 61. A. Louloupi, E. Ntini, T. Conrad, U. A. V. Ørom, Transient N-6-methyladenosine
biological themes among gene clusters. OMICS 16, 284–287 (2012). transcriptome sequencing reveals a regulatory role of m6A in splicing efficiency.
doi:10.1089/omi.2011.0118 Medline Cell Rep. 23, 3429–3437 (2018). doi:10.1016/j.celrep.2018.05.077 Medline
42. W. J. Kent, C. W. Sugnet, T. S. Furey, K. M. Roskin, T. H. Pringle, A. M. Zahler, D. 62. K. I. Zhou, H. Shi, R. Lyu, A. C. Wylder, Ż. Matuszek, J. N. Pan, C. He, M. Parisien, T.
Haussler, The human genome browser at UCSC. Genome Res. 12, 996–1006 Pan, Regulation of co-transcriptional pre-mRNA splicing by m6A through the low-
(2002). doi:10.1101/gr.229102 Medline complexity protein hnRNPG. Mol. Cell 76, 70–81.e9 (2019).
43. A. M. Bolger, M. Lohse, B. Usadel, Trimmomatic: A flexible trimmer for Illumina doi:10.1016/j.molcel.2019.07.005 Medline
sequence data. Bioinformatics 30, 2114–2120 (2014). 63. W. Xiao, S. Adhikari, U. Dahal, Y.-S. Chen, Y.-J. Hao, B.-F. Sun, H.-Y. Sun, A. Li, X.-
doi:10.1093/bioinformatics/btu170 Medline L. Ping, W.-Y. Lai, X. Wang, H.-L. Ma, C.-M. Huang, Y. Yang, N. Huang, G.-B. Jiang,
44. S. Anders, P. T. Pyl, W. Huber, HTSeq—A Python framework to work with high- H.-L. Wang, Q. Zhou, X.-J. Wang, Y.-L. Zhao, Y.-G. Yang, Nuclear m6A reader
throughput sequencing data. Bioinformatics 31, 166–169 (2015). YTHDC1 regulates mRNA splicing. Mol. Cell 61, 507–519 (2016).
doi:10.1093/bioinformatics/btu638 Medline doi:10.1016/j.molcel.2016.01.012 Medline
45. B. Langmead, C. Trapnell, M. Pop, S. L. Salzberg, Ultrafast and memory-efficient 64. N. Viphakone, I. Sudbery, L. Griffith, C. G. Heath, D. Sims, S. A. Wilson, Co-
alignment of short DNA sequences to the human genome. Genome Biol. 10, R25 transcriptional loading of RNA export factors shapes the human transcriptome.
(2009). doi:10.1186/gb-2009-10-3-r25 Medline Mol. Cell 75, 310–323.e8 (2019). doi:10.1016/j.molcel.2019.04.034 Medline
46. M. I. Love, W. Huber, S. Anders, Moderated estimation of fold change and 65. K. M. Neugebauer, Nascent RNA and the Coordination of Splicing with
dispersion for RNA-seq data with DESeq2. Genome Biol. 15, 550 (2014). Transcription. Cold Spring Harb. Perspect. Biol. 11, a032227 (2019).
doi:10.1186/s13059-014-0550-8 Medline doi:10.1101/cshperspect.a032227 Medline
47. M. Martin, Cutadapt removes adapter sequences from high-throughput 66. J. Akhtar, N. Kreim, F. Marini, G. Mohana, D. Brüne, H. Binder, J.-Y. Roignant,
sequencing reads. EMBnet. J. 17, 10 (2011). doi:10.14806/ej.17.1.200 Promoter-proximal pausing mediated by the exon junction complex regulates
48. A. Dobin, C. A. Davis, F. Schlesinger, J. Drenkow, C. Zaleski, S. Jha, P. Batut, M. splicing. Nat. Commun. 10, 521 (2019). doi:10.1038/s41467-019-08381-0 Medline
Chaisson, T. R. Gingeras, STAR: Ultrafast universal RNA-seq aligner. 67. D. L. Silver, D. E. Watkins-Chow, K. C. Schreck, T. J. Pierfelice, D. M. Larson, A. J.
Bioinformatics 29, 15–21 (2013). doi:10.1093/bioinformatics/bts635 Medline Burnetti, H.-J. Liaw, K. Myung, C. A. Walsh, N. Gaiano, W. J. Pavan, The exon
49. Y. Liao, G. K. Smyth, W. Shi, featureCounts: An efficient general purpose program junction complex component Magoh controls brain size by regulating neural stem
for assigning sequence reads to genomic features. Bioinformatics 30, 923–930 cell division. Nat. Neurosci. 13, 551–558 (2010). doi:10.1038/nn.2527 Medline
(2014). doi:10.1093/bioinformatics/btt656 Medline 68. Z. Wang, V. Murigneux, H. Le Hir, Transcriptome-wide modulation of splicing by
50. N. T. Ingolia, S. Ghaemmaghami, J. R. S. Newman, J. S. Weissman, Genome-wide the exon junction complex. Genome Biol. 15, 551 (2014). doi:10.1186/s13059-014-
analysis in vivo of translation with nucleotide resolution using ribosome profiling. 0551-7 Medline
Science 324, 218–223 (2009). doi:10.1126/science.1168978 Medline 69. C.-C. Lu, C.-C. Lee, C.-T. Tseng, W.-Y. Tarn, Y14 governs p53 expression and
51. T. Buschmann, L. V. Bystrykh, Levenshtein error-correcting barcodes for modulates DNA damage sensitivity. Sci. Rep. 7, 45558 (2017).
multiplexed DNA sequencing. BMC Bioinformatics 14, 272 (2013). doi:10.1038/srep45558 Medline
doi:10.1186/1471-2105-14-272 Medline 70. E. Sendinc, D. Valle-Garcia, A. Jiao, Y. Shi, Analysis of m6A RNA methylation in
52. V. Agarwal, G. W. Bell, J.-W. Nam, D. P. Bartel, Predicting effective microRNA Caenorhabditis elegans. Cell Discov. 6, 47 (2020). doi:10.1038/s41421-020-
target sites in mammalian mRNAs. eLife 4, e05005 (2015). 00186-6 Medline
doi:10.7554/eLife.05005 Medline 71. L. Kan, S. Ott, B. Joseph, E. S. Park, W. Dai, R. E. Kleiner, A. Claridge-Chang, E. C.
53. S. Ke, A. Pandya-Jones, Y. Saito, J. J. Fak, C. B. Vågbø, S. Geula, J. H. Hanna, D. L. Lai, A neural m6A/Ythdf pathway is required for learning and memory in
Black, J. E. Darnell Jr., R. B. Darnell, m6A mRNA modifications are deposited in Drosophila. Nat. Commun. 12, 1458 (2021). doi:10.1038/s41467-021-21537-1
nascent pre-mRNA and are not required for splicing but do specify cytoplasmic Medline
turnover. Genes Dev. 31, 990–1006 (2017). doi:10.1101/gad.301036.117 Medline 72. G. Jia, Y. Fu, X. Zhao, Q. Dai, G. Zheng, Y. Yang, C. Yi, T. Lindahl, T. Pan, Y.-G. Yang,
54. F. Yan, A. Al-Kali, Z. Zhang, J. Liu, J. Pang, N. Zhao, C. He, M. R. Litzow, S. Liu, A C. He, N6-methyladenosine in nuclear RNA is a major substrate of the obesity-
dynamic N6-methyladenosine methylome regulates intrinsic and acquired associated FTO. Nat. Chem. Biol. 7, 885–887 (2011). doi:10.1038/nchembio.687
resistance to tyrosine kinase inhibitors. Cell Res. 28, 1062–1076 (2018). Medline
doi:10.1038/s41422-018-0097-4 Medline 73. J. Wei, F. Liu, Z. Lu, Q. Fei, Y. Ai, P. C. He, H. Shi, X. Cui, R. Su, A. Klungland, G. Jia,
55. R. Middleton, D. Gao, A. Thomas, B. Singh, A. Au, J. J.-L. Wong, A. Bomane, B. J. Chen, C. He, Differential m6A, m6Am, and m1A Demethylation Mediated by FTO
Cosson, E. Eyras, J. E. J. Rasko, W. Ritchie, IRFinder: Assessing the impact of in the Cell Nucleus and Cytoplasm. Mol. Cell 71, 973–985.e5 (2018).
intron retention on mammalian gene expression. Genome Biol. 18, 51 (2017). doi:10.1016/j.molcel.2018.08.011 Medline
doi:10.1186/s13059-017-1184-4 Medline 74. R. Su, L. Dong, C. Li, S. Nachtergaele, M. Wunderlich, Y. Qing, X. Deng, Y. Wang, X.
56. C. J. Herrmann, R. Schmidt, A. Kanitz, P. Artimo, A. J. Gruber, M. Zavolan, Weng, C. Hu, M. Yu, J. Skibbe, Q. Dai, D. Zou, T. Wu, K. Yu, H. Weng, H. Huang, K.
PolyASite 2.0: A consolidated atlas of polyadenylation sites from 3′ end Ferchen, X. Qin, B. Zhang, J. Qi, A. T. Sasaki, D. R. Plas, J. E. Bradner, M. Wei, G.
sequencing. Nucleic Acids Res. 48, D174–D179 (2020). doi:10.1093/nar/gkz918 Marcucci, X. Jiang, J. C. Mulloy, J. Jin, C. He, J. Chen, R-2HG Exhibits Anti-tumor
Medline Activity by Targeting FTO/m6A/MYC/CEBPA Signaling. Cell 172, 90–105.e23
57. A. G. Baltz, M. Munschauer, B. Schwanhäusser, A. Vasile, Y. Murakawa, M. (2018). doi:10.1016/j.cell.2017.11.031 Medline
Schueler, N. Youngs, D. Penfold-Brown, K. Drew, M. Milek, E. Wyler, R. Bonneau, 75. G. Zheng, J. A. Dahl, Y. Niu, P. Fedorcsak, C.-M. Huang, C. J. Li, C. B. Vågbø, Y. Shi,
M. Selbach, C. Dieterich, M. Landthaler, The mRNA-bound proteome and its global W.-L. Wang, S.-H. Song, Z. Lu, R. P. G. Bosmans, Q. Dai, Y.-J. Hao, X. Yang, W.-M.
occupancy profile on protein-coding transcripts. Mol. Cell 46, 674–690 (2012). Zhao, W.-M. Tong, X.-J. Wang, F. Bogdan, K. Furu, Y. Fu, G. Jia, X. Zhao, J. Liu, H.
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 7
E. Krokan, A. Klungland, Y.-G. Yang, C. He, ALKBH5 is a mammalian RNA
demethylase that impacts RNA metabolism and mouse fertility. Mol. Cell 49, 18–
29 (2013). doi:10.1016/j.molcel.2012.10.015 Medline
76. S. Zhang, B. S. Zhao, A. Zhou, K. Lin, S. Zheng, Z. Lu, Y. Chen, E. P. Sulman, K. Xie,
O. Bögler, S. Majumder, C. He, S. Huang, m6A Demethylase ALKBH5 Maintains
Tumorigenicity of Glioblastoma Stem-like Cells by Sustaining FOXM1 Expression
and Cell Proliferation Program. Cancer Cell 31, 591–606.e6 (2017).
doi:10.1016/j.ccell.2017.02.013 Medline
77. B. Molinie, J. Wang, K. S. Lim, R. Hillebrand, Z.-X. Lu, N. Van Wittenberghe, B. D.
Howard, K. Daneshvar, A. C. Mullen, P. Dedon, Y. Xing, C. C. Giallourakis, m6A-
LAIC-seq reveals the census and complexity of the m6A epitranscriptome. Nat.
Methods 13, 692–698 (2016). doi:10.1038/nmeth.3898 Medline
78. L. Hu, S. Liu, Y. Peng, R. Ge, R. Su, C. Senevirathne, B. T. Harada, Q. Dai, J. Wei, L.
Zhang, Z. Hao, L. Luo, H. Wang, Y. Wang, M. Luo, M. Chen, J. Chen, C. He, m6A RNA
modifications are measured at single-base resolution across the mammalian
transcriptome. Nat. Biotechnol. 40, 1210–1219 (2022). doi:10.1038/s41587-022-
01243-z Medline
79. K. C. H. Ha, B. J. Blencowe, Q. Morris, QAPA: A new method for the systematic
analysis of alternative polyadenylation from RNA-seq data. Genome Biol. 19, 45
(2018). doi:10.1186/s13059-018-1414-4 Medline
ACKNOWLEDGMENTS
We thank Tao Pan, Erin Adams, Marcus Clark, Marcelo Nobrega, Jonathan Staley,
and Amelia Joslin for comments and suggestions. We thank the Genomics
Facility of the University of Chicago and the University of Chicago
Comprehensive Cancer Center DNA Sequencing and Genotyping Facility for
assistance with sequencing. Funding: National Institutes of Health HG008935
(C.H.); National Institutes of Health grant T32 HD007009 (P.C.H); National
Institutes of Health grant F32 CA221007 (B.T.H); C.H. is an investigator of the
Howard Hughes Medical Institute. Author contributions: Conceptualization:
PCH; Methodology: PCH, JW, XD, BTH, ZZ, CH; Formal analysis: PCH, XD, XY, RL;
Investigation: PCH, JW, XD, BTH, SW, RG, CL, LZ, ZZ; Visualization: PCH, XD, JW;
Funding acquisition: PCH, BTH, CH; Project administration: CH; Supervision: MC,
CH; Writing – original draft: PCH, CH; Writing – review & editing: PCH, JW, XD,
BTH, ZZ, SW, RL, MC, CH. Competing interests: C.H. is a scientific founder and a
scientific advisory board member of Accent Therapeutics, Inc., Aferna Bio, Inc.,
and AccuraDX Inc. The other authors declare no competing interests. Data and
materials availability: Raw and processed data can be found at NCBI GEO
accession GSE162199. Custom scripts available on Zenodo (34). All other data
are available in the manuscript or the supplementary materials. License
information: Copyright © 2023 the authors, some rights reserved; exclusive
licensee American Association for the Advancement of Science. No claim to
original US government works. https://www.science.org/about/science-
licenses-journal-article-reuse. This article is subject to HHMI’s Open Access to
Publications policy. HHMI lab heads have previously granted a nonexclusive CC
BY 4.0 license to the public and a sublicensable license to HHMI in their research
articles. Pursuant to those licenses, the author-accepted manuscript of this
article can be made freely available under a CC BY 4.0 license immediately upon
publication.
SUPPLEMENTARY MATERIALS
science.org/doi/10.1126/science.abj9090
Materials and Methods
Supplementary Text
Figs. S1 to S30
Tables S1 to S6
References (35–79)
MDAR Reproducibility Checklist
Submitted 9 June 2021; resubmitted 3 October 2022
Accepted 16 January 2023
Published online 26 January 2023
10.1126/science.abj9090
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 8
Fig. 1. MPm6A reveals suppression of thousands of m6A sites in unmethylated
transcriptome regions. (A) Schematic of the MPm6A workflow. (B) MPm6A enrichment
scores (experimental IP/input – negative control IP/input) for endogenously methylated (n
= 6,095) and unmethylated (n = 2,716) sequences, mean ± SD, four biological replicates. (C)
Metagenes of endogenously methylated and unmethylated sequences that are significantly
methylated in MPm6A. (D) Exon lengths of endogenously methylated and unmethylated
sequences that are significantly methylated in MPm6A. Median, and IQR, Wilcoxon rank sum
test. Sample size for each violin plot from left to right is: n = 175, n = 22, n = 696, n = 519, n =
3,539, and n = 1,328. (E) Distribution of internal exon lengths in the human genome. Black
lines indicate 10th percentile (left, 60 nt) and 90th percentile (right, 246 nt). Blue and red lines
indicate median internal exon length for MPm6A endogenously methylated (915 nt) and
unmethylated (167 nt) sequences, respectively.
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 9
Fig. 2. Pre-mRNA splicing suppresses m6A
methylation in average-length exons. (A and B)
Left: schematic of specified BG CRY1 constructs.
Blue regions indicate sequences derived from the
CRY1 endogenous sequence, gray regions indicate
sequences derived from rabbit beta-globin (BG).
Number following CRY1 refers to the number of
nucleotides of exonic sequence surrounding the
CRY1 suppressed m6A site in the CRY1 endogenous
mRNA that was cloned into the BG construct. Grey
dot in the blue region denotes the suppressed m6A
site; the number at the left and right of the m6A site
shows the distance (nt) between the m6A site and
the 3′ and 5′ splice site, respectively; the number
next to the TSS shows the distance (nt) between the
m6A site and the promoter. Δ denotes deletion of the
specified intron(s). Details of each construct are
described in the supplementary method. Right: m6A
enrichment at a CRY1 suppressed m6A site. Primers
amplifying a 62 nt-fragment containing the CRY1
suppressed m6A site. m6A enrichment was
calculated as IP/input normalized to m6A-marked
Gaussia luciferase RNA spike-in IP/input. Mean ±
SEM, two-tailed t-test, *P < 0.05; **P < 0.01, ***P <
0.001. Three biological replicates.
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 10
Fig. 3. EJCs protect exon junction-proximal RNA in average-length exons within CDS
regions from m6A methylation. (A) Differentially methylated regions upon EIF4A3 KD (left)
and RBM8A KD (right) in HeLa cells (FDR<.1, |log FC|>1). Three biological replicates. Gray
2
and red dots indicate differentially methylated regions that overlap and do not overlap m6A
peaks in the control cells, respectively. (B) Input and m6A-IP read coverage at FUS and
SRSF6 in EIF4A3 KD, RBM8A KD, and control HeLa cells. (C) Numbers of EIF4A3 KD
hypermethylated regions (left) and m6A peaks in control cells (right) that reside within first,
internal or last exons (D) Exon lengths for m6A peaks residing within internal exons in control
KD, EIF4A3 KD and RBM8A KD cells, and exon lengths of hypermethylated regions residing
within internal exons in EIF4A3 and RBM8A KD cells. Dot and bar represent median and
interquartile range, Wilcoxon rank sum test of indicated group vs. siC all m6A peaks. Sample
size for each violin plot from left to right is: n = 3166, n = 6659, n = 8438, n = 3817, and n =
3827. (E) Metagenes of m6A peaks and significantly hypermethylated m6A regions (and top
quartile) in EIF4A3 KD HeLa cells, and m6A peaks in control cells.
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 11
Fig. 4. mRNA m6A hypermethylation
upon EJC depletion destabilizes
mRNAs. (A) Correlation between fold
changes in mRNA half-life and m6A level
upon EIF4A3 KD in HeLa cells (n = 3840).
(B) Boxplots showing half-life fold
changes of hypermethylated mRNAs
upon EIF4A3 KD in HeLa cells. mRNAs
were categorized into three groups
according to their methylation changes
upon EIF4A3 KD in HeLa cells. P values
from Wilcoxon rank sum test. Sample
size for each boxplot plot from left to
right is: n = 1887, n = 1201, and n = 752.
(C) Left: heatmap showing fold changes
in m6A level, mRNA half-life, and YTHDF2
binding upon EIF4A3 KD in HeLa cells.
Right: scatter plots showing the
correlation among fold changes in m6A
level, mRNA half-life, and YTHDF2
binding upon EIF4A3 KD in HeLa cells.
The hypermethylated mRNAs (m6A
log FC > 0; n = 3424) were categorized
2
into 100 bins based on ranked fold
change of m6A level upon EIF4A3 KD. For
(A) and (C), PCC and P values are shown.
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 12
Fig. 5. EJCs and RNPS1 protect proximal RNA regions from aberrant mRNA processing.
(A) Differentially methylated regions upon RNPS1 KD in HeLa cells (FDR < 0.1, |log FC| > 1),
2
three biological replicates. Gray and red dots indicate differentially methylated regions that
overlap and do not overlap with m6A peaks in the control KD cells, respectively. (B)
Metagenes of significantly m6A hypermethylated regions (and top quartile) upon RNPS1 KD
in HeLa cells in comparison with that of all m6A peaks in control cells. (C) Input and m6A-IP
read coverage at CDH24 and NRAS upon RNPS1 KD and EIF4A3 KD, respectively, as well as
corresponding controls in HeLa cells. (D) Enrichment of suppressed m6A sites (identified
from MPm6A) at EIF4A3-suppressed splice sites (left) and enrichment of EIF4A3 KD
hypermethylated regions at EIF4A3-suppressed splice sites (right). Fisher’s exact test, dot
and bar represent odds ratio and 95% confidence interval. (E) Input and m6A-IP read
coverage at SENP3 and HNRNPH1 in EIF4A3 KD and control HeLa cells. (F) Schematic model
depicting that EJCs and RNPS1 (and potentially other EJC-associated proteins) protect exon
junction-proximal RNA from m6A deposition through local mRNA packaging. For (C) and (E),
red bracket indicates EIF4A3-suppressed splice variant, with ends of bracket indicating the
suppressed splice junctions.
First release: 26 January 2023 science.org (Page numbers not final at time of first release) 13
