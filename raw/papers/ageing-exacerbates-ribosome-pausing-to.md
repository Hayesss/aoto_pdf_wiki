---
source_path: /mnt/c/Users/Administrator/Zotero/storage/Q83DD3UW/Stein 等。 - 2022 - Ageing exacerbates ribosome pausing to disrupt cot.pdf
ingested: 2026-04-23
sha256: 33b311abf1ee9b56
---

Article
Ageing exacerbates ribosome pausing to
disrupt cotranslational proteostasis
https://doi.org/10.1038/s41586-021-04295-4 Kevin C. Stein1, Fabián Morales-Polanco1, Joris van der Lienden1, T. Kelly Rainbolt1 &
Judith Frydman1,2 ✉
Received: 1 August 2020
Accepted: 1 December 2021
Ageing is accompanied by a decline in cellular proteostasis, which underlies many
Published online: 19 January 2022
age-related protein misfolding diseases1,2. Yet, how ageing impairs proteostasis
Check for updates
remains unclear. As nascent polypeptides represent a substantial burden on the
proteostasis network3, we hypothesized that altered translational efficiency during
ageing could help to drive the collapse of proteostasis. Here we show that ageing
alters the kinetics of translation elongation in both Caenorhabditis elegans and
Saccharomyces cerevisiae. Ribosome pausing was exacerbated at specific positions in
aged yeast and worms, including polybasic stretches, leading to increased ribosome
collisions known to trigger ribosome-associated quality control (RQC)4–6. Notably,
aged yeast cells exhibited impaired clearance and increased aggregation of RQC
substrates, indicating that ageing overwhelms this pathway. Indeed, long-lived yeast
mutants reduced age-dependent ribosome pausing, and extended lifespan correlated
with greater flux through the RQC pathway. Further linking altered translation to
proteostasis collapse, we found that nascent polypeptides exhibiting age-dependent
ribosome pausing in C. elegans were strongly enriched among age-dependent protein
aggregates. Notably, ageing increased the pausing and aggregation of many
components of proteostasis, which could initiate a cycle of proteostasis collapse.
We propose that increased ribosome pausing, leading to RQC overload and nascent
polypeptide aggregation, critically contributes to proteostasis impairment and
systemic decline during ageing.
Accurately generating the nascent proteome represents a substantial that ageing increased the translation of genes that are involved in stress
burden on proteostasis networks3,7. Compared with mature proteins, responses, such as GCN4 in yeast (Extended Data Fig. 1i).
partially folded nascent polypeptides are metastable and more sus- To analyse ribosome pausing, we calculated a pause score for each
ceptible to misfolding8,9. During translation elongation, the speed of position of a coding sequence relative to the whole transcript. The
the ribosome is positionally variable10 and these local changes impact cumulative distribution of pause scores across the transcriptome
co-translational proteostasis11. The transient slowing of elongation showed no global age-related changes (Fig. 1c), similar to previous
facilitates co-translational protein folding12–15, assembly16, organelle observations42. Average amino acid pause scores also showed negli-
targeting17,18 and chaperone recruitment19. However, the prolonged gible differences with age (Extended Data Figs. 1j, k, 2h, i). This indi-
slowing of elongation can lead to ribosome collisions and degradation cates that the metabolic changes of ageing do not cause a systemic
of the nascent polypeptide and transcript4–6,20–22. Disrupting transla- change in overall elongation pausing. However, hypothesizing that
tion kinetics or co-translational processing leads to aggregation of ageing might cause specific alterations in translation elongation, we
nascent proteins, impaired cellular fitness and neurodegeneration23–33. adapted a statistical metric19 to investigate elongation pausing during
Although proteostasis collapse is also a hallmark of ageing1,34,35, it ageing at the single-codon resolution. To validate this approach, we
remains unclear whether disrupting the tight balance between trans- used Ribo-seq analysis of yeast treated with 3-amino-1,2,4-triazole43,44,
lation elongation and co-translational flux is involved (Fig. 1a). which inhibits histidine biosynthesis and causes ribosome pausing at
We used ribosome profiling (Ribo-seq) to examine whether age- histidine positions43,44 (Extended Data Fig. 3a). Our approach identified
ing alters translation elongation in two well-established models of statistically significant ribosome pausing and found that only histidine
post-mitotic ageing: the nematode C. elegans and budding yeast S. was enriched among these sites (Extended Data Fig. 3b).
cerevisiae (Fig. 1b, Extended Data Fig. 1a). Validating our datasets, we Having validated our metric for detecting specific changes in ribo-
observed an age-related reduction of translation initiation in both some pausing, we used our Ribo-seq data to identify positions with
organisms, which was associated with a lower production of translation significant ageing-related changes in translation kinetics (Fig. 1d).
components, such as ribosomal proteins, and is consistent with previ- Notably, in both worms and yeast, these changes included thousands
ous studies36–41 (Extended Data Figs. 1b–h, 2a–g). We also confirmed of positions with significantly increased ribosome occupancy during
1Department of Biology, Stanford University, Stanford, CA, USA. 2Department of Genetics, Stanford University, Stanford, CA, USA. ✉e-mail: jfrydman@stanford.edu
Nature | Vol 601 | 27 January 2022 | 637
Article
a positions (Fig. 2a, b). Examining codon frequency in age-dependent
pause sites showed that most codons for a given amino acid were
enriched (Extended Data Fig. 3f). This indicates that amino acid prop-
erties and not codon optimality primarily determine age-dependent
pausing. We also used an alternative approach to examine amino acid
enrichment by calculating the average pause score for all possible
8,000 tripeptide motifs46. This strategy again identified a particular
Day 1 Day 0 association of Arg, Lys and Pro residues with increased ribosome paus-
Ribo-seq
ing during ageing (Extended Data Fig. 3g–i).
Day 6 Day 2
Prolonged pausing leads to ribosome collisions, which are detrimental
Elongation pausing and must be cleared by the RQC pathway4,20. We noted that similar amino
Day 12 analysis Day 4
acid residues associated with age-dependent pausing lead to the forma-
c tion of collided disomes and trisomes47 (Extended Data Fig. 4a). As ageing
further compromises the decoding of these residues, such as at a Trp
codon in HAT2 (Extended Data Fig. 4b, c), we examined whether ageing
impacts the likelihood of ribosome collisions. We identified the position
in each transcript at which disomes were most enriched over monosomes
in young cells47 and found that ageing exacerbated ribosome collisions
at these sites (Extended Data Fig. 4d). Similarly, we found that ageing
Pause score exacerbated ribosome collisions at codon pairs that were previously
shown to slow translation elongation48 and at tripeptide motifs associated
with ribosome collisions47 (Extended Data Fig. 4e–h). Polybasic motifs
such as RKK showed both increased ribosome collisions and pausing.
Collectively, these observations indicate that ageing alters translation
kinetics and exacerbates ribosome pausing and collisions at many posi-
tions in the yeast translatome, but particularly at motifs that are known
to cause slowdowns in young organisms, such as polybasic stretches20.
8 –4 0 4 We next wanted to dissect how ageing impacts the translation of
Relative pausing (log[odds ratio D4/D0])
2 polybasic regions. We identified repeats of Lys and Arg residues (K/R)
e of increasing length within the yeast transcriptome (Supplemen-
tary Table 3) and used previous Ribo-seq data from monosome- or
disome-protected mRNA47 to establish expected patterns of ribosome pausing and collisions. Longer polybasic stretches caused increased
ribosome pausing, a shift in peak ribosome occupancy after the poly-
basic stretch enters the ribosome and increased lagging ribosome
peaks indicative of disome/trisome pileup (Extended Data Fig. 5a, b).
We next determined how ageing affected ribosome occupancy at poly-
basic regions in yeast. Compared with young cells, aged cells showed
more severe pausing, and an additional ribosome peak was observed
~10 codons upstream of the main pause site—a signature of ribosome
collision4,20,43,44,47 (Fig. 2c, d, Extended Data Fig. 5c–e). Moreover,
the age-dependent increase in pausing and ribosome collisions was
enhanced for longer polybasic tracts. We also observed age-dependent
pausing and collisions at polybasic sites without consecutive Arg/
Lys residues, such as in the Hsp40 chaperone SIS1 (Extended Data
Fig. 5f). The polybasic tract in YTM1 further highlights the impact of
ageing—although disome profiling47 showed that ribosomes collide
at this region even in young cells, monosome footprinting detected
an upstream ribosome peak only in aged cells (Fig. 2e, f). Thus, ageing
sufficiently increases the frequency of ribosome collisions to make
ageing, incrementally increasing as the organism aged (Fig. 1e). We them directly detectable without isolating disomes.
termed these positions age-dependent ribosome pause sites (Supple- Several factors in the RQC pathway help to resolve collided ribosomes
mentary Table 1), representing sites with increased ribosome slowdown and degrade the nascent protein4–6,20,47,49–51, including recognition by
during ageing. These sites were enriched in genes that are involved in Hel2, C-terminal alanine and threonine (CAT) tail formation by Rqc2,
proteostasis and translation (Extended Data Fig. 3c, d, Supplemen- and ubiquitination by Ltn1/Rkr16,21,52–60. Disrupting this pathway leads
tary Table 2), suggesting that there are multiple mechanisms through to toxic aggregation of stalled nascent chains29,30. To test whether the
which altered elongation may impair proteostasis (Supplementary age-dependent increase in ribosome pausing and collisions affects the
Discussion). Moreover, transcripts with age-dependent pausing were handling of stalled nascent chains, we used RQC reporters contain-
enriched among polypeptides that are co-translationally ubiquitinated ing polybasic stretches of either 12 Arg or Lys residues (R12 or K12)
(Extended Data Fig. 3e), indicating that ageing may disrupt the biogen- inserted between GFP and RFP6,22. These inserts cause ribosome pausing
esis of proteins that are metastable even in young cells. and efficient degradation of stalled polypeptides in young cells22. By
To investigate the basis of age-dependent ribosome pausing in yeast, contrast, aged cells exhibited substantial accumulation of truncated,
we analysed the sequence specificity of pauses45. We found significant stalled nascent chains (Fig. 3a, Extended Data Fig. 6a) that did not result
positional enrichment of certain amino acids, with Pro and the basic from changes in medium composition or metabolism during yeast
residues Arg and Lys being enriched in multiple ribosomal active site chronological ageing (Extended Data Fig. 6b, c).
638 | Nature | Vol 601 | 27 January 2022
]P
detsujda[
gol–
01
0.1 1.0 10.0
noitcarf
evitalumuC
1.00
0.75
0.50
0.25
0
0.1 1.0 10.0
Pause score
300 200
150
200
100
100
50
0 0
–4 0 4
Relative pausing (log[odds ratio D12/D1])
2
]P
detsujda[
gol–
01
Ageing
? Translation elongation kinetics Co-translational proteostasis
5′ 3′ Functional protein
Fast Slow Aggregation
b C. elegans S. cerevisiae
Ageing Ageing
Overall pausing: all CDS codon positions
Day 1 Day 0
Day 6 Day 2
Day 12 Day 4
d Age-dependent changes in pausing
Age-dependent pause sites
Day 1 Day 0 Day 6 Day 2 Day 12 Day 4
noitcarf
evitalumuC
1.00
0.75
0.50
0.25
0
2.1
1.8
1.5
1.2
0.9
–20 –10 0 10 20
Distance from pause site (codons)
dezilamroN
ycnapucco
emosobir
dezilamroN
ycnapucco
emosobir
Age-dep. pausing Age-dep. pausing
1.7
1.5
1.3
1.1
–20 –10 0 10 20
Distance from pause site (codons)
Fig. 1 | Age-dependent ribosome pausing is conserved. a, Investigating the
impact of ageing on translation kinetics and co-translational proteostasis.
b, Overview of the procedure. c, Cumulative frequency histogram of pause
scores in the coding sequences (CDS) of worms (left) and yeast (right).
d, Relative ribosome pausing during ageing. The coloured points indicate
codon positions in day 12 adult worms and day 4 yeast with significantly
increased age-dependent (dep.) pausing (odds ratio > 1, adjusted P < 0.05), all
other translatome positions in grey. Statistical analysis was performed using a
two-sided Fisher’s exact test with Benjamini–Hochberg correction. e, The
average ribosome occupancy at age-dependent pause sites. n = 5,503 sites in
1,282 genes in worms (left) and n = 5,600 sites in 890 genes in yeast (right).
3
2
1
0
0 100 200 300 400
Codon position
To further validate that ageing decreases the ability to clear stalled We further used hel2∆ cells to examine how ageing impacts RQC
RQC substrates, we used RQC mutants. Ageing exacerbated the levels initiation20,51. Although aged hel2∆ cells showed increased GFP+RFP−
of stalled truncated products observed in ltn1∆ and rqc2∆ cells (Fig. 3a), puncta formation similar to the other RQC mutants, there was also
suggesting that age-dependent accumulation of stalled polypeptides a significant increase in GFP+RFP+ puncta using the stalling report-
does not simply result from impaired RQC activity. Notably, aged ltn1∆ ers (Fig. 3b, Extended Data Figs. 6d–f, 7d). As we also observed an
cells showed an increase in the formation of high molecular weight increased production of full-length reporter protein in aged cells
aggregates of the stalling reporters but not the GFP–RFP control, and of all genotypes (Fig. 3a), we hypothesized that ageing may cause
a decrease in CAT-tailed products, presumably by incorporation into greater bypass of stalling sequences. We used Ribo-seq analysis of
aggregates (Fig. 3a, Extended Data Fig. 6a). Similarly, using fluorescence young and aged cells containing the K12 stalling reporter and found
microscopy, we found that ageing strongly increased the formation that ageing increased ribosome occupancy at the 3′ end of the coding
of GFP+RFP− puncta for both polybasic reporters, which we validated sequence (Extended Data Fig. 7e), similar to findings in mice61. These
by immunoblot using a Flag–His3 reporter (Fig. 3b, Extended Data data suggest that ageing has pleiotropic effects on RQC, disrupting
Fig. 6d–g). Although formation of GFP+RFP− puncta increased in aged both the resolution of stalled ribosomes and processing of stalled
rqc2∆ cells, it was less than wild-type (WT) and ltn1∆ cells, suggest- polypeptides.
ing that CAT tails promote, but are not necessary for, age-dependent After linking ageing with increased ribosome pausing/collisions and
aggregation of stalled truncated polypeptides. dysfunctional RQC, we next examined whether the clearance of RQC
We next extended these findings to endogenous proteins that substrates affects lifespan (Fig. 3c). We compared two genome-wide
showed increased pausing in aged cells. First, we used fusion con- screens: one measured the chronological lifespan of each strain in the
structs of YTM1 that had either an N-terminal or C-terminal GFP tag to yeast deletion collection62, and the other quantified the clearance of
differentiate between co-translational or post-translational products, the GFP–R12 RQC substrate6. We grouped yeast strains on the basis of
respectively. In contrast to young cells, ageing increased the produc- GFP–R12 abundance, which acts as a proxy for RQC flux—strains with
tion of co-translational truncated products, which were distinct from high GFP levels, such as the RQC mutants, have a reduced ability to
post-translational products (Extended Data Fig. 7a). Moreover, ageing clear stalled nascent chains. We found that strains with the highest
increased GFP+ puncta formation when YTM1 was N-terminally tagged, GFP–R12 abundance had shortened lifespans, whereas strains with the
but not C-terminally tagged, in both WT and ltn1∆ cells (Extended Data lowest GFP–R12 levels had the longest lifespans (Fig. 3c), suggesting
Fig. 7b). We also observed the accumulation of co-translational trun- that RQC flux impacts longevity. Moreover, compared with strains with
cated products with age for N-terminally GFP-tagged HAT2 (Extended impaired RQC flux, we found an increased RQC flux in yeast strains that
Data Fig. 7c). This confirms that ageing impairs RQC processing of are chronologically long-lived, including strains that are not involved
stalled polypeptides. in the TOR pathway, as well as strains that have an extended replicative
Nature | Vol 601 | 27 January 2022 | 639
erocs
esuaP
a
c 3
2
2.0 1
0
1.5 250 260 270 280
1.0
0.5
–20 –10 0 10 20
Distance from polybasic start (codons)
d
dezilamroN
ycnapucco
emosobir
e 4 K/R
Tunnel EPA
4 K/R starts
2.0
1.5
1.0
0.5
–20 –10 0 10 20
Distance from polybasic start (codons)
dezilamroN
ycnapucco
emosobir
****
2 **** **** *** * * * **** **** ** *
0
–2
–4
ACDEFGHIKLMNPQRSTVWY ACDEFGHIKLMNPQRSTVWY ACDEFGHIKLMNPQRSTVWY
Residue Residue Residue
YTM1
(ribosomal assembly)
5 K/R
starts
6 K/R
Tunnel EPA
6 K/R Day 0 (Y) starts Day 4 (A)
)ycneuqerf
eudiser(gol
2
b
EPA
3′ 5′ * ** *
10.4
5.2
0
–3.3
–6.7
E P A
f
2
1
0
0 100 200 300 400
Codon position
)mpr(
ycnapucco
emosobiR
1.5 Monosome Disome
1.0
0.5
0
250 260 270 280
emosobiR
)mpr(
ycnapucco
Codon position
5 K/R starts
erocs
tnemhcirnE
E site P site A site
erocs
esuaP
Day 0 (Y) Day 4 (A)
Day 0 (Y) Day 4 (A)
Codon position
Fig. 2 | Ageing exacerbates ribosome pausing at polybasic regions in yeast. in 606 genes. The shaded region represents the 95% bootstrapped confidence
a, b, Peptide motif (a) and amino acid frequencies (b) associated with interval. The arrow indicates putative ribosome collisions. d, The average
age-dependent pause sites (n = 271 sites with day 4 pause score > 6 in 232 ribosome occupancy at polybasic regions with six consecutive K/R residues.
genes). Statistical analysis was performed using two-sided Fisher’s exact tests; n = 60 sites in 58 genes. e, Ribosome occupancy on YTM1. Inset: pausing and
*P < 0.05, **P < 0.01, ****P < 1 × 10−4. Basic residues are highlighted. c, The collision (arrow) at five consecutive K/R residues are highlighted. f, The
average ribosome occupancy at polybasic regions with four consecutive Lys/ occupancy of monosomes and disomes on YTM1 from disome profiling of
Arg (K/R) residues for young (Y) day 0 and aged (A) day 4 yeast. n = 738 K/R sites young cells47 (rpm, reads per million).
Article
RQC-mediated stalled polypeptide clearance
CAT tail Ubn N Polybasic Rqc2 Ltn1
GFP RFP
R12 K12
WT ltn1(cid:39) rqc2(cid:39) hel2(cid:39) WT ltn1(cid:39) rqc2(cid:39) hel2(cid:39)
Day: 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4
HMW
(aggregates)
GFP–RFP
(full length) 0.8
CAT tails
0.6
GFP
(paused
truncation) 0.4
WB: GFP WB: GFP
0.2
WB: histone H3 WB: histone H3
0
R12 Puncta formation? WT sch9(cid:39)
Ageing Truncated nascent polypeptide? GFP RFP CAT tail dependence?
WT ltn1(cid:39) rqc2(cid:39) hel2(cid:39)
Day 0 (Y) Day 4 (A) Day 0 (Y) Day 4 (A) Day 0 (Y) Day 4 (A) Day 0 (Y) Day 4 (A)
GFP
RFP
Merge
DNA
lifespan (Extended Data Fig. 8a). These analyses link defective clearance Extended Data Fig. 8g, h). We also found that ageing reduced the transla-
of stalled nascent polypeptides with accelerated ageing. tion of several RQC components, which was attenuated in sch9∆ cells
To further examine the relationship between translation elongation (Extended Data Fig. 8i). Notably, LTN1 translation was reduced in WT
and lifespan, we used cells deleted for SCH9, the orthologue of mam- cells but not changed in sch9∆ cells. Collectively, our data suggest that
malian S6K and a substrate of the TOR pathway34. The mutation of this the age-dependent increase in ribosome pausing overwhelms the RQC
component is a highly conserved means of extending lifespan63,64. We pathway, contributing to dysfunctional co-translational proteostasis
first found that sch9∆ cells significantly mitigated the age-dependent and the regulation of lifespan (Fig. 3f).
pausing observed in WT cells (Extended Data Fig. 8b, c). Moreover, sites Extending our analysis to C. elegans, we also found enrichment of
with greater pausing in aged WT cells versus aged sch9∆ cells showed certain residues at age-dependent pause sites (Fig. 4a, b, Extended Data
enrichment of Arg, Pro, Gly and Lys residues (Extended Data Fig. 8d), Fig. 9a–f). In particular, Arg was enriched at these sites, independent of
indicating that the loss of Sch9 reduces pausing at these residues. There codon usage, as well as in tripeptide motifs that have increased pausing
was also a marked reduction in both pausing and collisions at polybasic during ageing. Moreover, we found a length-dependent increase in ribo-
tracts in aged sch9∆ cells (Fig. 3d, Extended Data Fig. 8e, f). Using stall- some pausing in aged worms at polybasic motifs—pausing increased
ing reporters, aged sch9∆ cells exhibited less accumulation of truncated at regions of four consecutive K/R residues and was even higher at
polypeptides and abrogated their aggregation during ageing (Fig. 3e, five and six consecutive K/R residues (Fig. 4c, Extended Data Fig. 9g).
640 | Nature | Vol 601 | 27 January 2022
atcnup
–PFR+PFG
htiw
sllec
fo
noitcarF
GFP–R12 abundance
Long-lived
Low
Short-lived
High
***
**
WT sch9(cid:39) WTsch9(cid:39)
GFP–RFP R12 K12
nedrub
sisatsoetorP
Lifespan
Lifespan versus RQC flux ****
2 *
1
0
–1
?
–2
<1 s.d.1 s.d. 3 s.d.
regnoL
retrohS
RQC2
HEL2
RQC1 LTN1
ASC1
Low High
2.0
1.5
1.0
0.5
–20 –10 0 10 20 Distance from polybasic start (codons)
ycnapucco
emosobir
dezilamroN
(kDa)
- 150
- 75
- 50
- 37 WT Day 0
WT Day 4
sch9∆ Day 0
- 25 sch9∆ Day 4
- 15
N Polybasic
0.8
***
5′
Day 0
0.6 *** Day 4 Collided
ribosome RQC
0.4 Young Aged
**
0.2
P = 0.06 Clearance Truncated nascent
polypeptide aggregation
0
WT ltn1(cid:39) rqc2(cid:39)hel2(cid:39)
atcnup
–PFR+PFG
htiw
sllec
fo
noitcarF
)UA(
napsefiL
a c
5′ 3′
GFP–R12
abundance
d e
4 K/R
Tunnel EPA Day 0
4 K/R Day 4
starts
b N
5′ 3′
f
3′
Fig. 3 | Polybasic-driven age-dependent aggregation of truncated nascent GFP abundance of <1 s.d. of the total collection (n = 4,195); 1 s.d., strains with a
polypeptides in yeast is mitigated in lifespan extension models. GFP abundance of > 1 s.d. and <3 s.d. (n = 172); >3 s.d., strains with a GFP
a, Immunoblot analysis of young and aged WT and RQC mutant strains abundance greater than 3 s.d. (n = 39). The grey line indicates the average
harbouring reporters with 12 R or K between GFP-RFP. Truncated, full-length lifespan of the population. RQC mutants are noted. Statistical analysis was
and high molecular weight (HMW) products are noted. n ≥ 3 biological performed using two-sided Wilcoxon rank-sum tests; ****P = 6.6 × 10−13,
replicates. Representative examples are shown. Gel source data are provided in *P = 0.05. d, Average ribosome occupancy in WT and sch9∆ yeast at regions with
Supplementary Fig. 1. WB, western blot. b, Fluorescence microscopy and four consecutive K/R residues. n = 728 K/R sites in 598 genes. The shaded
quantification of GFP+RFP− puncta formation in cells harbouring the R12 region represents the 95% bootstrapped confidence interval. The arrow
reporter. n ≥ 3 biological replicates. Representative examples are shown. indicates putative ribosome collisions. e, Quantification of GFP+RFP− puncta
n ≥ 200 cells. Data are mean ± s.e.m. Statistical analysis was performed using formation in WT and sch9∆ cells. n ≥ 200 cells, 3 biological replicates. Data are
two-sided Welch’s t-tests; P = 6.6 × 10−4 (WT), P = 7.6 × 10−4 (ltn1Δ), P = 8.9 × 10−3 mean ± s.e.m. Statistical analysis was performed using two-sided Welch’s
(rqc2Δ). Scale bars, 3 µm. c, Investigating the association between lifespan and t-tests; **P = 0.004, ***P = 0.0004. f, The proposed model highlighting the
RQC by analysing the lifespan distribution62 of the yeast deletion collection on age-dependent aggregation of truncated nascent polypeptides after a
the basis of the abundance of the GFP-R12-HIS3 reporter6. <1 s.d., strains with a ribosome pausing event.
A site **
0.5
1.3 0
1.2
−0.5 1.1
1.0
ACDEFGHIKLMNPQRSTVWY 0.9
Residue
0.8 −20 −10 0 10 20
Distance from polybasic start (codons)
Increased pausing at motifs of six K/R residues was accompanied by the proteostasis dysfunction. The age-dependent increase in ribosome
signature upstream peak of ribosome collisions, as shown at a five-K/R pausing is conserved between worms and yeast, and is associated with
stretch in tag-342 (Fig. 4c, d). Thus, exacerbated ribosome pausing increased ribosome collisions, decreased flux through the RQC pathway
at polybasic regions that leads to increased ribosome collisions is a and ensuing aggregation of truncated nascent proteins. We propose
conserved feature of ageing in both yeast and worms. that this connection between age-related pausing and aggregation
We next examined the relationship between age-dependent ribo- of nascent chains precipitates a cycle of dysfunction during ageing
some pausing and protein aggregation during worm ageing37,65. Nota- (Supplementary Discussion).
bly, we found a strong association; proteins that aggregate with age Alterations in elongation rate probably disrupt several co-translational
were over-represented by about threefold among genes that had pathways, including folding and organelle targeting11,17–19,23. Here
age-dependent ribosome pauses (Fig. 4e, Extended Data Fig. 10a). we focused on the interplay between ribosome pausing and RQC.
Furthermore, proteins that aggregate in aged worms were enriched for The fact that increased stalling32 or dysfunctional RQC33 can cause
polybasic motifs, particularly in proteins with age-dependent pausing neurodegeneration highlights the importance of this interplay. There
(Extended Data Fig. 10b). We also found that age-dependent pausing is probably a delicate balance between ribosome slowdowns that facili-
and aggregation affected many proteins that are involved in transla- tate protein folding/targeting and slowdowns that lead to ribosome
tion and proteostasis (Fig. 4f, Extended Data Fig. 10c, Supplementary collisions and trigger RQC. Our data suggest that ageing disrupts this
Table 2). For example, all nine aminoacyl tRNA synthetases show- balance by causing greater ribosome pausing (Fig. 4h), particularly at
ing age-dependent pausing also aggregated during ageing (Fig. 4g, polybasic stretches. We propose that, in younger organisms, pausing
Extended Data Fig. 10d). Furthermore, several RQC components have at these regions rarely causes ribosome collisions that trigger RQC,
reduced translation and increased aggregation during worm ageing in agreement with RQC not regulating basal expression of positively
(Extended Data Fig. 10e, f). This probably exacerbates the enhanced charged proteins66. As a result, young organisms presumably have
load on this pathway from increased ribosome collisions and fur- adequate capacity to handle infrequent strong ribosome pauses.
ther disrupts co-translational proteostasis. By contrast, impaired resolution of ribosome pausing in aged organisms
Our data establish that altered ribosome pausing is a crucial conduc- increases the frequency of ribosome collisions, thereby overwhelming
tor of the ageing process, providing a link to protein aggregation and RQC. Altered translation kinetics during ageing might also disrupt
Nature | Vol 601 | 27 January 2022 | 641
dezilamroN
ycnapucco
emosobir
3
2
1
0 100 200 300 400
Codon position
erocs
esuaP
4
3
2
1
0
0 100 200 300
Codon position
erocs
esuaP
a c
6 K/R starts Day 1 (Y) Day 12 (A)
d e
4 Day 1 (Y) 0.25 Day 12 (A) 5 K/R 3 0.20
starts 2
0.15
1
0 0.10
250 260 270 280
0.05
0
g Day 1 (Y) h
f Age-dependent wars-1 3 Day 12 (A)
aggregates (Trp tRNA synthetase) 2 tRNA
aminoacylation
Arg in 1 dev G el e o r p m m c e e n l t l active site
P granule 150 160 170 180
Proteasome
Adult lifespan
Translation
0 3 6 9
Fold enrichment
tnedneped-ega
fo
noitcarF
snietorp
detagergga
Young Aged ****
No
pause Pause
)ycneuqerf
eudiser(gol
2
2.2
1.1
0
−1.0
−2.0
E P A
erocs
tnemhcirnE
b
tag-342
(calmodulin binding) Day 1 (Y) Day 12 (A)
Age-dependent
ribosome pausing
? Age-dependent
protein aggregation
Codon position
N
Young 5′ 3′
Functional Aged protein
Functional Pausing
protein Pausing
Pause + agg. Degradation Aggregate Polypeptide Proteostasis
aggregation burden
erocs
esuaP
Codon position
erocs
esuaP
6 K/R
Tunnel EPA
Fig. 4 | Conserved mechanisms of age-dependent ribosome pausing and with a pause site, 6,219 proteins without a pause site. Statistical analysis was
aggregation in worms. a, b, Peptide motif (a) and ribosomal A-site amino acid performed using a two-sided Fisher’s exact test; P = 5.6 × 10−22. f, Comparing the
frequencies (b) associated with age-dependent pause sites. n = 587 sites functional enrichment within aggregated (agg.) proteins37 with those that also
with day 12 pause score >10 in 437 genes). Statistical analysis was performed have age-dependent ribosome pausing, displaying representative Gene
using a two-sided Fisher’s exact test; **P = 0.005. c, The average ribosome Ontology terms (adjusted P < 0.05). Categories related to proteostasis are
occupancy at polybasic regions with six consecutive K/R residues. n = 109 K/R highlighted. The unfiltered results are provided in Supplementary Table 2.
sites in 100 genes. The shaded region represents the 95% bootstrapped g, Ribosome occupancy on wars-1 (Trp tRNA synthetase). Inset: pausing at a
confidence interval. The arrow indicates putative ribosome collisions. position with Arg in the ribosomal active site is highlighted. h, The proposed
d, Ribosome occupancy on tag-342. Inset: the pausing and collision (arrow) at model of increased ribosome pausing and aggregation of truncated nascent
five consecutive K/R residues are highlighted. e, Investigating the association polypeptides during ageing.
between age-dependent ribosome pausing and aggregation37. n = 742 proteins
Article
co-translational folding of nascent polypeptides and cause additional 30. Yonashiro, R. et al. The Rqc2/Tae2 subunit of the ribosome-associated quality control
aggregation or stoichiometry imbalances that further disrupt proteo- (RQC) complex marks ribosome-stalled nascent polypeptide chains for aggregation.
eLife 5, e11794 (2016).
stasis (Supplementary Discussion). Such implications demonstrate 31. Wu, C. C.-C., Peterson, A., Zinshteyn, B., Regot, S. & Green, R. Ribosome collisions trigger
that ribosome pausing is probably a critical driver of age-related pro- general stress responses to regulate cell fate. Cell 182, 404–416 (2020).
32. Ishimura, R. et al. Ribosome stalling induced by mutation of a CNS-specific tRNA causes
teostasis decline associated with many late-onset misfolding diseases.
neurodegeneration. Science 345, 455–459 (2014).
33. Bengtson, M. H. & Joazeiro, C. A. P. Role of a ribosome-associated E3 ubiquitin ligase in
protein quality control. Nature 467, 470–473 (2010).
Online content 34. Taylor, R. C. & Dillin, A. Aging as an event of proteostasis collapse. Cold Spring Harb.
Perspect. Biol. 3, a004440 (2011).
Any methods, additional references, Nature Research reporting sum- 35. Ben-Zvi, A., Miller, E. A. & Morimoto, R. I. Collapse of proteostasis represents an early
maries, source data, extended data, supplementary information, molecular event in Caenorhabditis elegans aging. Proc. Natl Acad. Sci. USA 106, 14914–
14919 (2009).
acknowledgements, peer review information; details of author contri-
36. Steffen, K. K. & Dillin, A. A ribosomal perspective on proteostasis and aging. Cell Metab.
butions and competing interests; and statements of data and code avail- 23, 1004–1012 (2016).
ability are available at https://doi.org/10.1038/s41586-021-04295-4. 37. Walther, D. M. et al. Widespread proteome remodeling and aggregation in aging C.
elegans. Cell 161, 919–932 (2015).
38. Pan, K. Z. et al. Inhibition of mRNA translation extends lifespan in Caenorhabditis elegans.
1. López-Otín, C., Blasco, M. A., Partridge, L., Serrano, M. & Kroemer, G. The hallmarks of Aging Cell 6, 111–119 (2007).
aging. Cell 153, 1194–1217 (2013). 39. Hansen, M. et al. Lifespan extension by conditions that inhibit translation in
2. Chiti, F. & Dobson, C. M. Protein misfolding, functional amyloid, and human disease. Caenorhabditis elegans. Aging Cell 6, 95–110 (2007).
Annu. Rev. Biochem. 75, 333–366 (2006). 40. Reis-Rodrigues, P. et al. Proteomic analysis of age-dependent changes in protein
3. Pechmann, S., Willmund, F. & Frydman, J. The ribosome as a hub for protein quality solubility identifies genes that modulate lifespan. Aging Cell 11, 120–127 (2012).
control. Mol. Cell 49, 411–421 (2013). 41. Narayan, V. et al. Deep proteome analysis identifies age-related processes in C. elegans.
4. Simms, C. L., Yan, L. L. & Zaher, H. S. Ribosome collision is critical for quality control Cell Syst. 3, 144–159 (2016).
during no-go decay. Mol. Cell 68, 361–373 (2017). 42. Hu, Z. et al. Ssd1 and Gcn2 suppress global translation efficiency in replicatively aged
5. Juszkiewicz, S. et al. ZNF598 is a quality control sensor of collided ribosomes. Mol. Cell yeast while their activation extends lifespan. eLife 7, 4443 (2018).
72, 469–481 (2018). 43. Young, D. J., Guydosh, N. R., Zhang, F., Hinnebusch, A. G. & Green, R. Rli1/ABCE1 recycles
6. Brandman, O. et al. A ribosome-bound quality control complex triggers degradation of terminating ribosomes and controls translation reinitiation in 3'UTRs in vivo. Cell 162,
nascent peptides and signals translation stress. Cell 151, 1042–1054 (2012). 872–884 (2015).
7. Balchin, D., Hayer-Hartl, M. & Hartl, F. U. In vivo aspects of protein folding and quality 44. Guydosh, N. R. & Green, R. Dom34 rescues ribosomes in 3' untranslated regions. Cell 156,
control. Science 353, aac4354 (2016). 950–962 (2014).
8. Jahn, T. R. & Radford, S. E. Folding versus aggregation: polypeptide conformations on 45. Choi, J. et al. How messenger RNA and nascent chain sequences regulate translation
competing pathways. Arch. Biochem. Biophys. 469, 100–117 (2008). elongation. Annu. Rev. Biochem. 87, 421–449 (2018).
9. Ciryam, P., Tartaglia, G. G., Morimoto, R. I., Dobson, C. M. & Vendruscolo, M. Widespread 46. Schuller, A. P., Wu, C. C.-C., Dever, T. E., Buskirk, A. R. & Green, R. eIF5A functions globally
aggregation and neurodegenerative diseases are associated with supersaturated in translation elongation and termination. Mol. Cell 66, 194–205 (2017).
proteins. Cell Rep. 5, 781–790 (2013). 47. Meydan, S. & Guydosh, N. R. Disome and trisome profiling reveal genome-wide targets of
10. Gingold, H. & Pilpel, Y. Determinants of translation efficiency and accuracy. Mol. Syst. ribosome quality control. Mol. Cell 79, 588–602 (2020).
Biol. 7, 481 (2011). 48. Gamble, C. E., Brule, C. E., Dean, K. M., Fields, S. & Grayhack, E. J. Adjacent codons act in
11. Stein, K. C. & Frydman, J. The stop-and-go traffic regulating protein biogenesis: concert to modulate translation efficiency in yeast. Cell 166, 679–690 (2016).
how translation kinetics controls proteostasis. J. Biol. Chem. 294, 2076–2084 (2019). 49. Han, P. et al. Genome-wide survey of ribosome collision. Cell Rep. 31, 107610 (2020).
12. Yu, C.-H. et al. Codon usage influences the local rate of translation elongation to regulate 50. Juszkiewicz, S., Speldewinde, S. H., Wan, L., Svejstrup, J. Q. & Hegde, R. S. The ASC-1
co-translational protein folding. Mol. Cell 59, 744–754 (2015). complex disassembles collided ribosomes. Mol. Cell 79, 603–614 (2020).
13. Pechmann, S. & Frydman, J. Evolutionary conservation of codon optimality reveals 51. Ikeuchi, K. et al. Collided ribosomes form a unique structural interface to induce
hidden signatures of cotranslational folding. Nat. Struct. Mol. Biol. 20, 237–243 Hel2-driven quality control pathways. EMBO J. 38, e100276 (2019).
(2013). 52. Shen, P. S. et al. Protein synthesis. Rqc2p and 60S ribosomal subunits mediate
14. Kudla, G., Murray, A. W., Tollervey, D. & Plotkin, J. B. Coding-sequence determinants of mRNA-independent elongation of nascent chains. Science 347, 75–78 (2015).
gene expression in Escherichia coli. Science 324, 255–258 (2009). 53. Shao, S., Malsburg, von der, K. & Hegde, R. S. Listerin-dependent nascent protein
15. Zhang, G., Hubalewska, M. & Ignatova, Z. Transient ribosomal attenuation coordinates ubiquitination relies on ribosome subunit dissociation. Mol. Cell 50, 637–648 (2013).
protein synthesis and co-translational folding. Nat. Struct. Mol. Biol. 16, 274–280 54. Shao, S. & Hegde, R. S. Reconstitution of a minimal ribosome-associated ubiquitination
(2009). pathway with purified factors. Mol. Cell 55, 880–890 (2014).
16. Collart, M. A. & Weiss, B. Ribosome pausing, a dangerous necessity for co-translational 55. Shao, S., Brown, A., Santhanam, B. & Hegde, R. S. Structure and assembly pathway of the
events. Nucleic Acids Res. 48, 1043–1055 (2020). ribosome quality control complex. Mol. Cell 57, 433–444 (2015).
17. Chartron, J. W., Hunt, K. C. L. & Frydman, J. Cotranslational signal-independent SRP 56. Juszkiewicz, S. & Hegde, R. S. Initiation of quality control during poly(A) translation
preloading during membrane targeting. Nature 536, 224–228 (2016). requires site-specific ribosome ubiquitination. Mol. Cell 65, 743–750 (2017).
18. Pechmann, S., Chartron, J. W. & Frydman, J. Local slowdown of translation by nonoptimal 57. Sundaramoorthy, E. et al. ZNF598 and RACK1 regulate mammalian ribosome-associated
codons promotes nascent-chain recognition by SRP in vivo. Nat. Struct. Mol. Biol. 21, quality control function by mediating regulatory 40S ribosomal ubiquitylation. Mol. Cell
1100–1105 (2014). 65, 751–760 (2017).
19. Stein, K. C., Kriel, A. & Frydman, J. Nascent polypeptide domain topology and elongation 58. Matsuo, Y. et al. Ubiquitination of stalled ribosome triggers ribosome-associated quality
rate direct the cotranslational hierarchy of Hsp70 and TRiC/CCT. Mol. Cell 75, 1117–1130 control. Nat. Commun. 8, 159 (2017).
(2019). 59. Tsuboi, T. et al. Dom34:hbs1 plays a general role in quality-control systems by dissociation
20. Sitron, C. S. & Brandman, O. Detection and degradation of stalled nascent chains via of a stalled ribosome at the 3′ end of aberrant mRNA. Mol. Cell 46, 518–529 (2012).
ribosome-associated quality control. Annu. Rev. Biochem. 89, 417–442 (2020). 60. Sitron, C. S. & Brandman, O. CAT tails drive on- and off-ribosome degradation of stalled
21. Brandman, O. & Hegde, R. S. Ribosome-associated protein quality control. Nat. Struct. polypeptides. Nat. Struct. Mol. Biol. 26, 450–459 (2018).
Mol. Biol. 23, 7–15 (2016). 61. Anisimova, A. S. et al. Multifaceted deregulation of gene expression and protein synthesis
22. Dimitrova, L. N., Kuroha, K., Tatematsu, T. & Inada, T. Nascent peptide-dependent with age. Proc. Natl Acad. Sci. USA 117, 15581–15590 (2020).
translation arrest leads to Not4p-mediated protein degradation by the proteasome. 62. Powers, R. W., Kaeberlein, M., Caldwell, S. D., Kennedy, B. K. & Fields, S. Extension of
J. Biol. Chem. 284, 10343–10352 (2009). chronological life span in yeast by decreased TOR pathway signaling. Genes Dev. 20, 174–
23. Buhr, F. et al. Synonymous codons direct cotranslational folding toward different protein 184 (2006).
conformations. Mol. Cell 61, 341–351 (2016). 63. Fabrizio, P., Pozza, F., Pletcher, S. D., Gendron, C. M. & Longo, V. D. Regulation of longevity
24. Nedialkova, D. D. & Leidel, S. A. Optimization of codon translation rates via trna and stress resistance by Sch9 in yeast. Science 292, 288–290 (2001).
modifications maintains proteome integrity. Cell 161, 1606–1618 (2015). 64. Kaeberlein, M. et al. Regulation of yeast replicative life span by TOR and Sch9 in response
25. Kim, S. J. et al. Protein folding. Translational tuning optimizes nascent protein folding in to nutrients. Science 310, 1193–1196 (2005).
cells. Science 348, 444–448 (2015). 65. David, D. C. et al. Widespread protein aggregation as an inherent part of aging in C.
26. Willmund, F. et al. The cotranslational function of ribosome-associated Hsp70 in elegans. PLoS Biol. 8, e1000450 (2010).
eukaryotic protein homeostasis. Cell 152, 196–209 (2013). 66. Barros, G. C. et al. Rqc1 and other yeast proteins containing highly positively charged
27. Duttler, S., Pechmann, S. & Frydman, J. Principles of cotranslational ubiquitination and sequences are not targets of the RQC complex. J. Biol. Chem. 296, 100586 (2021).
quality control at the ribosome. Mol. Cell 50, 379–393 (2013).
28. Koplin, A. et al. A dual function for chaperones SSB-RAC and the NAC nascent Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
polypeptide-associated complex on ribosomes. J. Cell Biol. 189, 57–68 (2010). published maps and institutional affiliations.
29. Choe, Y.-J. et al. Failure of RQC machinery causes protein aggregation and proteotoxic
stress. Nature 531, 191–195 (2016). © The Author(s), under exclusive licence to Springer Nature Limited 2022
642 | Nature | Vol 601 | 27 January 2022
Methods ~1,000 worms per plate. Animals were carefully monitored to ensure
that adequate bacteria was in constant supply, adding concentrated
Strains and growth conditions stocks of bacteria as necessary. At each of the indicated ages, ~40,000
The Bristol N2 strain of C. elegans was grown at 20 °C on nematode adult worms were collected by quickly washing subsets of plates into
growth medium agar plates seeded with Escherichia coli strain OP50 microcentrifuge tubes using modified lysis buffer (20 mM Tris-HCl
according to standard methods67. All yeast experiments were per- pH 7.5, 140 mM KCl, 1.5 mM MgCl), followed by a short centrifugation
2
formed using derivatives of BY4741 (MATa his3Δ1 leu2Δ0 met15Δ0 (0.3g at room temperature for 10 s) that minimized the number of eggs
ura3Δ0). Ribo-seq experiments used diploid BY4743 (WT) and homozy- and bacteria that pelleted with the animals. The supernatant from each
gous sch9Δ/sch9Δ (YSC6275-201917395), which were obtained from GE tube was then aspirated and pelleted animals were dripped into liquid
Healthcare Dharmacon. For immunoblotting and microscopy experi- nitrogen. Lysis was performed by combining 1 ml of lysis buffer con-
ments, haploid strains of WT, ltn1Δ, rqc2Δ, hel2Δ and sch9Δ were from taining twice the concentration of dithiothreitol (DTT), cycloheximide
the Yeast Knockout Collection68. Strains from the N-terminally GFP (CHX) and Triton X-100 (20 mM Tris-HCl pH 7.5, 140 mM KCl, 1.5 mM
tagged seamless collection69 as well as from the C-terminally GFP tagged MgCl, 1 mM DTT, 200 µg ml−1 CHX, 2% Triton X-100) to compensate for
2
clone collection70 were used for the YTM1 and HAT2 experiments. the approximate volume of lysis buffer that remained when collecting
Yeast cells were grown at 30 °C in variations of synthetic complete the animals. Worms were then pulverized using a MM-301 mixer mill at
(SC) medium62 with a fivefold excess of nutrients to compensate for 20 Hz for 1 min; the lysate was thawed in a water bath at room tempera-
strain auxotrophies. ture and centrifuged at 15,000g at 4 °C for 10 min. After quantifying
RNA concentration, 200 µg RNA was incubated for 45 min with 0.75 µl
Plasmid and yeast strain construction 100 U µl−1 RNase I (Ambion), with another 200 µg RNA being kept on ice
Ribosome pausing reporter plasmids were derived from gifts from O. undigested to use for polysome profiles. Sucrose gradient centrifuga-
Brandman52 and T. Inada22. The PGK1 promoter was amplified using tion and fractionation were then performed as described previously17.
oligonucleotides 5′-GCGGAGCTCTGTTTGCAAAAAGAACAAAAC Total RNA was extracted from the digested 80S fraction using the hot
and 5′-GCGTCTAGATGTTTTATATTTGTTGTAAAAAG, digested SDS–phenol–chloroform method, 20–35 nucleotide RNA footprints
with SacI/XbaI and ligated to create p416PGK-GFP-R12-FLAG-HIS3 were isolated, ribosomal RNA was removed using the Ribo-Zero kit
and p416PGK-GFP-K12(AAA)-FLAG-HIS3. The correct clones (Illumina) and the remaining library preparation steps were described
were confirmed by colony PCR and sequencing. Experiments previously72. Barcoded samples were pooled and sequenced using the
using GFP-R12-RFP and GFP-K12-RFP pausing reporters were HiSeq 4000 (Illumina) system. For yeast samples, overnight cultures
performed after integrating these reporters into yeast. First, were diluted to an optical density at 600 nm (OD ) of 0.05 in 500 ml
600
RFP was amplified from pTDH3-GFP-R12-RFP52 using oligonu- SC medium and grown at 30 °C. Part of each culture was collected as
cleotides 5′-GCGACTAGTATGGTGAGCGAGCTGATTAAG and day 0 cells at an OD of ~0.7, with the remaining culture placed back at
600
5′-GCGGAATTCTTATCTGTGCCCCAGTTTG, digested with SpeI/ 30 °C for 48 h and 96 h for collection at day 2 and day 4, respectively. All
EcoRI-HF and ligated to replace the FLAG-HIS3 in the plasmids above to cells were collected by vacuum filtration and freezing in liquid nitrogen.
create p416PGK-GFP-R12-RFP and p416PGK-GFP-K12(AAA)-RFP. A XbaI/ Lysis was performed by combining 2 ml of lysis buffer (20 mM Tris-HCl
ClaI digest was used to clone the reporter into pAG306GPD-ccdB-chrI, pH 7.5, 140 mM KCl, 1.5 mM MgCl, 0.5 mM DTT, 100 µg ml−1 CHX, 1%
2
a gift from D. Gottschling (Addgene plasmid, 41894)71. These con- Triton X-100) frozen in liquid nitrogen with cell pellets; the remaining
structs were then digested with NotI and transformed into yeast cells steps of lysis and library preparation were performed according to that
using standard methods and selected on SC-ura. The correct clones described for worms above.
were confirmed by colony PCR, sequencing and microscopy.
To construct ltn1Δ strains with integrated YTM1-GFP fusions, Data processing and pause score calculation
LTN1 was deleted from the knock-in strains by standard PCR-based Demultiplexed sequencing reads were trimmed of adaptor sequences
homologous recombination. The YTM1-GFP ltn1Δ strain was con- using Cutadapt v.1.4.2, followed by removal of the 5′ nucleotide using
structed by replacing LTN1 with LEU2 using a cassette amplified FASTX-Trimmer. Reads that mapped to ribosomal RNAs using Bow-
from plasmid GTL-g (Addgene plasmid, 81099) with the oligonu- tie v.1.0.0 (http://bowtie-bio.sourceforge.net/index.shtml)73 were
cleotides 5′-GATTATGCCCCAACATGGAA AACTGAAAAATATTGAT removed. The remaining reads were aligned to reference libraries
GAAGCGAGTCTGTAGGCGAACCTAACCGG and 5′-TTTCCAGAA that consisted of coding sequences containing 21 nucleotides flank-
TATCCGGGTGATGGGCTGGATTGGCAAGGTATTATATGAAGATTGTTC ing upstream of the start codon and downstream of the stop codon,
TACCATTCACAACTATAT. Similarly, the GFP-YTM1 ltn1Δ strain was or the entire transcript sequence including untranslated regions. The
constructed by replacing LTN1 with URA3 using a cassette amplified C. elegans library consisted of the longest transcript of 20,222 genes
from plasmid pSH100 (Addgene plasmid, 45930) with the oligonucleo- (ce11/WBcel235), and the yeast library consisted of 5,793 ORFs (sac-
tides 5′-GATTATGCCCCAACATGGAAAACTGAAAAATATTGATGAAGCG Cer3/R64-1-1) that excluded ORFs that were characterized as dubi-
AGCCACAGCTTTTCAATTCAATTCATCA and 5′-TTTCCAGAATATCCG ous or that overlapped with other genes. Bowtie v.1.0.0 alignment of
GGTGATGGGCTGGATTGGCAAGGTATCCTGATGCGGTATTTTCTCCTTA. sequencing reads to these libraries used the following parameters to
Both cassettes were amplified, separated by electrophoresis, gel puri- allow for two mismatches and retain only uniquely mapped reads for
fied and transformed into yeast cells using the lithium acetate method. further analysis: -y -a -m 1 -v 2 -norc -best -strata. For each footprint
Correct transformants were verified by standard PCR using the oli- length, custom Python scripts were used to sum reads at each nucleo-
gonucleotides LTN1-VF: 5′-TCCGTTTTGGATT CGTTGGAGT; LTN1-VR: tide. Metagene analysis was performed separately on each fragment
5′-ACCGCCAAGCAGAA AATCC; LEU2-VF: 5′-AGCACGAGCCTCCTT length, and lengths that did not exhibit the characteristic 3-nucleotide
TACCT; and URA3-VF: 5′-CGAATGCACA CGGTGTGGT. periodicity were removed. The remaining reads had a nucleotide offset
empirically determined from the 5′ end of each fragment length, using
Ribo-seq analysis the characteristic large ribosome density at the start codon, such that
For C. elegans samples, after passaging for at least three generations, each read was assigned to the first A-site nucleotide. Nucleotide reads
age-synchronized populations of L1 larvae were obtained and grown at each codon were then summed and used for all additional analyses.
to the L4 larval stage (day 0). The plates of L4 animals were then To analyse gene expression, reads were summed for each gene after
washed and the collected animals were transferred to plates contain- excluding the first 20 and last 20 sense codons, followed by calculating
ing 50 µg ml−1 5-fluoro-2′-deoxyuridine (FUdR; Millipore Sigma) at tpm (transcripts per million). Statistical significance was calculated
Article
using DESeq2 (ref. 74) for genes with greater than 64 reads in each bio- To control for differences in gene expression and coverage, ribosome
logical replicate. Pause scores at each codon position in a transcript reads were normalized by dividing the reads at each codon by the
were calculated by dividing the number of reads at that position by the mean number of reads per codon across the analysis window. We
expected number of reads, which was defined as the average number excluded low-coverage genes that had an average reads per codon
of reads across the internal part of the transcript, that is, excluding the across the analysis window of less than 0.5.
first 20 and last 20 sense codons. Mathematically:
Pause-site sequence analysis
RRij
Pausescore= To examine the enrichment of amino acids and codons associated
∑i k = − 2 2 1 0RRij with greater ribosome pausing during ageing, we first calculated the
k−40
average frequency of each residue/codon across coding sequences.
where RR is the number of ribosomal reads at position i of gene j that Using this as background, we generated logo plots to analyse amino
has length k codons. acid enrichment in two ways using the R package Logolas75. First, we
used the tripeptide motifs of age-dependent pause sites in the upper
Age-dependent pause site identification rank of ribosome pausing (pause score > 10 for day 12 worms or pause
To identify positions at which ribosome pausing was increased during score > 6 for day 4 yeast). Second, we calculated the average pause
ageing, we included genes that had an average sequencing coverage score for each of the 8,000 possible tripeptide motifs across coding
of ≥0.5 reads per codon (calculated as described above), and ≥64 total sequences and used the motifs that had a higher average pause score,
reads in each replicate, which included 7,200 C. elegans genes and 4,082 as indicated, and filtered by count (≥100) and pause score (average
yeast genes. Next, we adapted a strategy that we used previously19 using pause score in older sample of >2 in worms and >1.5 in yeast). We also
two-tailed Fisher’s exact tests to identify positions at which there were calculated the residue and codon frequency in the ribosomal active site
statistically significant changes in ribosome pausing between the young and compared it to the background frequency within coding sequences.
(day 1 worms and day 0 yeast) and old (day 12 worms and day 4 yeast)
samples. In brief, reads at each position and for each transcript were Other computational analysis
averaged between replicates and rounded to the nearest integer. At To examine the association of yeast chronological lifespan with the
each position of a transcript, 2 × 2 contingency tables were created to ability to clear paused, truncated nascent polypeptides, we used pre-
perform a two-tailed Fisher’s exact test to compare the ratio of reads viously published datasets6,62. We binned yeast strains based on the
in the young and aged fractions at a given position to the ratio at all distribution of the GFP–R12 reporter abundance, as indicated (Fig. 3c).
other positions in that transcript (that is, the summed reads in each To examine the association of age-dependent ribosome pausing and
fraction for the entire transcript minus the position of interest). In protein aggregation (Fig. 4e, Extended Data Fig. 10a), we compared
other words, this compares the observed ratio of ribosome reads from our dataset of ribosome pausing to two previous datasets that identi-
our young and aged samples at a given position to the expected ratio fied age-dependent protein aggregates in C. elegans37,65. For the higher
based on the total number of reads that map to the transcript. At each coverage dataset37, we used proteins that were identified in at least three
position, this enables us to calculate the odds ratio as a measure of of the four replicates of day 1 and day 12 worms, and had an average
enrichment, along with an adjusted P value to test significance, using aggregate abundance at day 12 higher than that at day 1. To examine
the Benjamini–Hochberg correction for multiple hypothesis testing the association of age-dependent ribosome pausing and ubiquitina-
for each gene. The odds ratio is: tion (Extended Data Fig. 3e), we compared our dataset of ribosome
pausing to a previous dataset examining co-translational ubiquitina-
Aij tion in yeast27.
Yij
Oddsratio=
(∑i k =1Aij)−Aij
Immunoblotting
(∑i k =1Yij)−Yij
Yeast strains were grown at 30 °C in SC medium containing 2% glucose
(standard conditions), 3% glycerol or buffered to pH 6.0 with citrate
where A and Y are the ribosomal reads of the aged and young trans- phosphate buffer (64.2 mM NaHPO, 17.9 mM citric acid, pH 6.0)76,
2 4
latome fractions, respectively, at position i of gene j that has length k as indicated. Day 0 cells were collected at an OD of ~0.7, and day
600
codons. Age-dependent pause sites were identified as those that had: 4 cells were collected 96 h later from the same culture. For medium
(1) Benjamini–Hochberg adjusted P < 0.05; (2) 1 < odds ratio < ∞; (3) swap experiments, overnight cultures were diluted into either fresh SC
pause score in the oldest sample greater than the pause score in the medium or the nutrient-depleted medium of the supernatant collected
intermediate aged sample (day 6 worms and day 2 yeast); (4) reads in after pelleting day 4 cells, and day 0 cells were collected as described
the oldest sample greater than the average number of reads across the above. Frozen cell pellets were resuspended in 200 µl of lysis buffer
transcript, to control for background; and (5) a position in the internal (50 mM Tris pH 7.5, 150 mM NaCl, 1 mM EDTA, 5% glycerol, 0.1% Triton
part of the transcript (that is, not in the first 20 or last 20 sense codons). X-100, 0.1% SDS, 1 mM PMSF, 0.5 mM DTT, Roche cOmplete EDTA-free
Protease Inhibitor Cocktail), and lysed by vortexing with glass beads at
Ribosome occupancy analysis 3,000 rpm at 4 °C for 3 min, incubating on ice for 3 min and vortexing
Ribosome occupancy for individual genes was plotted using a again at 3,000 rpm at 4 °C for 3 min. After clearing by centrifugation
five-residue moving average of the pause scores. To analyse ribo- of cell lysates at 4,000 rpm at 4 °C for 30 s, the protein concentration
some occupancy around polybasic regions, we identified polybasic was normalized using the Bradford Assay (Bio-Rad) and 4× NuPage
regions in the genomes of worms and yeast as defined by a stretch of LDS sample buffer (Thermo Fisher Scientific) was added. The sam-
3, 4, 5 or 6+ consecutive residues that were either lysine or arginine ples were then boiled for 5 min, run on a 12% SDS–PAGE gel and trans-
(Supplementary Table 3). These regions were categorized into only ferred to a nitrocellulose membrane. The membranes were blocked
one group, such that regions of 6+ consecutive basic residues were in 5% milk reconstituted in TBS (20 mM Tris pH 7.5, 150 ml NaCl, 0.1%
not included in the analysis of the shorter regions. For metagene NaN). Primary antibodies were diluted in Antibody Buffer (20 mM Tris
3
analysis of ribosome pausing, reads were aligned at the ribosome pH 7.5, 150 ml NaCl, 0.1% NaN, 5% BSA) and secondary antibodies were
3
A-site around the region of interest (for example, age-dependent prepared in 5% milk in TBS. As indicated, the blots were subjected to
pause sites or the start of the polybasic region). We next calculated immunoblotting using mouse anti-GFP antibodies (Millipore Sigma,
the mean and bootstrapped 95% confidence intervals at each position. 11814460001, 1:1,000 dilution), rabbit anti-Flag antibodies (Millipore
Sigma, F7425, 1:1,000 dilution) and rabbit anti-histone H3 antibodies
Data availability
(EpiCypher 13-0001, 1:2,500 dilution), and visualized using the LI-COR
system IRDye 800CW donkey anti-mouse IgG (LI-COR 926-32212, The datasets generated for this study have been deposited in NCBI’s
1:10,000 dilution) and IRDye 680RD donkey anti-rabbit IgG (LI-COR Gene Expression Omnibus (GEO) under GEO Series accession number
926-68073, 1:10,000 dilution). The uncropped blots are provided in GSE152850. Additional datasets used in this study are also publicly
the Supplementary Data. available: GSE139036 (disome profiling), GSE69414 and GSE52968
(Ribo-seq of yeast treated with 3-amino-1,2,4-triazole), ref. 62 (yeast
Microscopy analysis chronological lifespan), ref. 6 (RQC flux), and refs. 37 and 65 (protein
Yeast cells were grown as described above for immunoblotting. After aggregation during C. elegans ageing).
collecting, cells were fixed in 4% paraformaldehyde by incubating at
room temperature for 15 min, and washed again in 1× PBS. Cells were
Code availability
then immobilized onto polylysine-coated coverslips (Neuvrito) and
mounted with ProLong Diamond antifade mountant with DAPI (Thermo All customized Python or R scripts used for data processing and analysis
Fisher Scientific). Fluorescence microscopy for quantification was are available from the corresponding author on request.
acquired using a Zeiss Axio observer.Z1 inverted microscope equipped
with a Plan-Apochromat ×100/1.4 NA oil-immersion DIC M27 objective 67. Brenner, S. The genetics of Caenorhabditis elegans. Genetics 77, 71–94 (1974).
68. Winzeler, E. A. et al. Functional characterization of the S. cerevisiae genome by gene
(Zeiss), X-cite 120 LED system (Lumen Dynamics), filter set (HE) RFP/
deletion and parallel analysis. Science 285, 901–906 (1999).
GFP/DAPI (Zeiss) and a digital Axiocam MRm camera (Zeiss) controlled 69. Yofe, I. et al. One library to make them all: streamlining the creation of yeast libraries via a
with the Zen blue software. Raw data were collected as z-stacks and pro- SWAp-Tag strategy. Nat. Chem. Biol. 13, 371–378 (2016).
70. Huh, W.-K. et al. Global analysis of protein localization in budding yeast. Nature 425,
jected using ImageJ (NIH) and quantification was performed manually.
686–691 (2003).
Confocal microscopy analysis of representative cells was performed 71. Hughes, A. L. & Gottschling, D. E. An early age increase in vacuolar pH limits
using the Leica TCS SP8 inverted sSTED microscope equipped with a mitochondrial function and lifespan in yeast. Nature 492, 261–265 (2012).
72. Ingolia, N. T., Brar, G. A., Rouskin, S., McGeachy, A. M. & Weissman, J. S. The ribosome
×100/1.40 NA APO objective and using the following detection mir-
profiling strategy for monitoring translation in vivo by deep sequencing of
ror settings: RFP, 560–630 nm; GFP, 470–536 nm. DAPI staining was ribosome-protected mRNA fragments. Nat. Protoc. 7, 1534–1550 (2012).
detected using a blue diode 405 nm laser (10%) and a photon multiply- 73. Langmead, B., Trapnell, C., Pop, M. & Salzberg, S. L. Ultrafast and memory-efficient
alignment of short DNA sequences to the human genome. Genome Biol. 10, R25
ing tube. One representative middle slide was collected, and images
(2009).
were subsequently deconvolved and background subtracted using 74. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold change and dispersion
Huygens Professional (Scientific Volume Imaging). for RNA-seq data with DESeq2. Genome Biol. 15, 550 (2014).
75. Dey, K. K., Xie, D. & Stephens, M. A new sequence logo plot to highlight enrichment and
depletion. BMC Bioinform. 19, 473 (2018).
Statistical analysis 76. Burtner, C. R., Murakami, C. J., Kennedy, B. K. & Kaeberlein, M. A molecular mechanism of
All analysis was performed in R (https://www.r-project.org). Gene chronological aging in yeast. Cell Cycle 8, 1256–1270 (2009).
77. Huang, D. W., Sherman, B. T. & Lempicki, R. A. Systematic and integrative analysis of large
Ontology annotations and significance were obtained using the Data-
gene lists using DAVID bioinformatics resources. Nat. Protoc. 4, 44–57 (2009).
base for Annotation, Visualization, and Integrated Discovery (DAVID 78. McCormick, M. A. et al. A comprehensive analysis of replicative lifespan in 4,698
v.6.8)77 using as background, as indicated, the transcripts included in single-gene deletion strains uncovers conserved mechanisms of aging. Cell Metab. 22,
895–906 (2015).
the Ribo-seq reference library or present in both this library and the
mass spectrometry datasets37,65. Statistical significance of categorical
Acknowledgements We thank R. Aviner and M. Aguilar-Rangel for comments on the
variable distributions shown in box plots used two-sided Wilcoxon
manuscript; members of the Frydman Laboratory for discussions and advice; J. Chartron, P.
rank-sum tests (Fig. 3c, Extended Data Fig. 8). For box plots, the centre Dolan and K. Dalton for technical input; and J. Lim and J. Arribere for C. elegans expertise. YTM1
line represents the median, the box limits indicate the upper and lower and HAT2performed at the UCSF Center for Advanced Technology. K.C.S. was supported as a
Glenn Foundation for Medical Research Postdoctoral Fellow and by NIH/NIA grant
quartiles, the whiskers indicate 1.5× the interquartile range, and the
(T32AG047126). F.M.-P. was supported by The Pew Trusts in the Biomedical Sciences
points are outliers. Significance of age-dependent puncta formation postdoctoral Award (00034104), and T.K.R was supported by the NIH/NIGMS National
(Fig. 3b) was assessed using two-sided Welch’s t-tests. Two-sided Fisher’s Research Service Award (F32GM120947). This work was supported by NIH grants GM056433
and AG054407 (to J.F.). J.F. is a CZ Biohub Investigator.
exact tests were used to calculate the significance of residue and codon
frequency in age-dependent pause sites (Figs. 2, 4, Extended Data Fig. 9),
Author contributions K.C.S. and J.F. designed the study. K.C.S. performed all of the
association of ribosome pausing and ubiquitination (Extended Data experiments and computational analyses, with assistance from F.M.-P., J.L. and T.K.R. in
Fig. 3e), association of ribosome pausing and aggregation (Fig. 4e) and carrying out the yeast reporter immunoblot and microscopy experiments. K.C.S. and J.F. wrote
the manuscript with input from all authors.
sequence enrichment of protein aggregates (Extended Data Fig. 10b).
Additional statistical details are mentioned in the figures or figure leg- Competing interests The authors declare no competing interests.
ends, including the values of n and P. None of the experiments involved
Additional information
blinding or randomization, and the sample size was not predetermined.
Supplementary information The online version contains supplementary material available at
https://doi.org/10.1038/s41586-021-04295-4.
Reporting summary Correspondence and requests for materials should be addressed to Judith Frydman.
Peer review information Nature thanks Andrew Dillin, Toshifumi Inada and the other,
Further information on research design is available in the Nature
anonymous, reviewer(s) for their contribution to the peer review of this work.
Research Reporting Summary linked to this paper. Reprints and permissions information is available at http://www.nature.com/reprints.
Article
Extended Data Fig. 1 | See next page for caption.
Extended Data Fig. 1 | Decreased protein synthesis and translatome fold down, adjusted P < 0.05, Benjamini-Hochberg method) in Day 4 yeast cells
changes during chronological ageing of yeast. a, Survival curve of yeast relative to Day 0 yeast cells. g, Functional enrichment of differentially
during chronological ageing. n = 3 biological replicates with mean ± s.e.m. translated genes during ageing displaying representative gene ontology terms
b – c, Average ribosome occupancy at the b, start and c, stop codons during (adjusted P < 0.1, Benjamini-Hochberg method). See Supplementary Table 2 for
yeast chronological ageing. The shaded region represents the 95% complete, unfiltered results. h, Ribosome occupancy on ribosomal protein
bootstrapped confidence interval. d, Polysome profiles of chronologically RPL3 showing decreased translation during yeast ageing. i, Ribosome
aged yeast at the indicated ages showing decreased population of polysomes occupancy on the 5’UTR and coding sequence of GCN4, showing decreased
during ageing. n ≥ 3 biological replicates with representative profiles shown. occupancy at upstream ORFs and increased occupancy across the coding
e, Heat map of gene expression analysis of Ribo-seq data showing Pearson’s sequence during ageing. j, Scatter plot of average pause scores for each
correlation coefficient between all yeast samples. f, Volcano plot of differential amino acid residue in coding sequences of young Day 0 and aged Day 4 yeast.
gene expression shows widespread translatome changes for chronologically k, Scatter plots of average pause scores for each amino acid residue in coding
aged yeast. n = 2,981 total genes with 901 genes having increased ribosome sequences of two biological replicates of Day 0 (left) and Day 4 (right)
occupancy (purple, > 2 fold up, adjusted P < 0.05, Benjamini-Hochberg chronologically aged yeast.
method) and 1,033 genes having decreased ribosome occupancy (green, > 2
Article
Extended Data Fig. 2 | Decreased protein synthesis and translatome occupancy (green, > 2 fold down, adjusted P < 0.05, Benjamini-Hochberg
changes during chronological ageing of worms. a, Polysome profiles of method) in Day 12 adult worms relative to Day 1 adult worms. f, Functional
adult worms at the indicated ages showing decreased population of polysomes enrichment of differentially translated genes displaying representative gene
during ageing. n ≥ 3 biological replicates with representative profiles shown. ontology terms (adjusted P < 0.1, except for categories with number of genes <
b – c, Average ribosome occupancy at the b, start and c, stop codons of young 20 where adjusted P < 0.25, Benjamini-Hochberg method). See Supplementary
Day 1 and aged Day 12 worms. The shaded region represents the 95% Table 2 for complete, unfiltered results. g, Ribosome occupancy on ribosomal
bootstrapped confidence interval. d, Heat map of gene expression analysis of protein rps-3 showing decreased translation during ageing of worms. h, Scatter
Ribo-seq data showing Pearson’s correlation coefficient between worm plot of average pause scores for each amino acid residue in coding sequences of
samples. e, Volcano plot of differential gene expression shows widespread Day 1 and Day 12 adult worms. i, Scatter plots of average pause scores for each
translatome changes during worm ageing. n = 8,341 total genes with 621 genes amino acid residue in coding sequences of two biological replicates of Day 1
having increased ribosome occupancy (purple, > 2 fold up, adjusted P < 0.05, (left) and Day 12 (right) adult worms.
Benjamini-Hochberg method) and 655 genes having decreased ribosome
Extended Data Fig. 3 | Age-dependent ribosome pausing. a, Scatter plot of an age-dependent pause site in worms displaying representative gene
the average pause score for each amino acid residue in coding sequences of ontology terms (adjusted P < 0.1, Benjamini–Hochberg method). See
young WT yeast cells either untreated or treated with 3-amino-1,2,4-triazole Supplementary Table 2 for complete, unfiltered results. e, Investigating the
(3-AT) from previously published Ribo-seq data43. b, Amino acid residue association between age-dependent ribosome pausing and co-translational
frequency in the ribosomal A-site of statistically significant ribosome pause ubiquitination27. Population n = 937 transcripts with a pause site, 3,145
sites enriched in yeast cells treated with 3-AT43, relative to the residue transcripts without a pause site. P = 0.002, two-sided Fisher’s exact test.
frequency in the transcriptome. c, Functional enrichment of genes with an f, Codon frequency in the ribosomal A-site of age-dependent ribosome pause
age-dependent pause site in yeast displaying representative gene ontology sites relative to the codon frequency in the transcriptome. n = 271 pause sites
terms (adjusted P < 0.1, Benjamini–Hochberg method). See Supplementary with Day 4 pause score > 6 in 232 genes. g – i, Peptide motif associated with
Table 2 for complete, unfiltered results. d, Functional enrichment of genes with greater ribosome pausing in the indicated age comparisons.
Article
Extended Data Fig. 4 | Association of age-dependent ribosome pausing in aged yeast, with a lagging ribosome peak present in aged cells, at d, the
yeast with disome formation. a, Peptide motif associated with disome position where disomes were most enriched in each transcript in young cells47;
formation in young cells47. b, Ribosome occupancy on HAT2 with e, inhibitory codon pairs previously associated with ribosome pausing48 and
age-dependent ribosome pausing at position 188 with Trp in the A-site. disome formation47; and f – h, tripeptide motifs previously associated with
c, Occupancy of monosomes and disomes on HAT2 from disome footprint disome formation47. The shaded region represents the 95% bootstrapped
profiling of young cells47. d – h, Average ribosome occupancy in young and confidence interval.
Extended Data Fig. 5 | Age-dependent ribosome pausing at polybasic in 152 genes. The shaded region represents the 95% bootstrapped confidence
regions. a – b, Average ribosome occupancy at polybasic regions of interval. Arrow indicates a putative increase in ribosome collision events with
a, monosomes and b, disomes in young WT yeast47 showing length-dependent age at regions with 5 K/R. d – e, Average ribosome occupancy at polybasic
pausing and collisions. c, Average ribosome occupancy at polybasic regions regions of d, young Day 0 and e, aged Day 4 yeast. Also see panel c and Fig. 2c
consisting of 3 (left) or 5 (right) consecutive Lys or Arg (K/R) for young Day 0 and 2d. f, Ribosome occupancy on SIS1 with inset highlighting ribosome
and aged Day 4 yeast. n = 3,729 sites of 3 K/R in 2,198 genes, and 159 sites of 5 K/R pausing and collision (arrow) at stretch of 6 K/R within a 10 residue window.
