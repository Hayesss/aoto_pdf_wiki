---
source_path: /mnt/c/Users/Administrator/Zotero/storage/SUD4ERQJ/Song 等 - 2024 - Mapping snoRNA-target RNA interactions in an RNA binding protein-dependent manner with chimeric eCLI.pdf
ingested: 2026-04-23
sha256: cad3d00d1e4a0ea8
---

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
Mapping snoRNA-target RNA interactions in an RNA binding protein-dependent manner
with chimeric eCLIP
Zhuoyi Song1*, Bongmin Bae2*, Simon Schnabl2, Fei Yuan1, Thareendra De Zoysa2, Maureen
Akinyi1, Charlotte Le Roux1, Karine Choquet3, Amanda Whipple2†, Eric Van Nostrand1†
1Therapeutic Innovation Center & the Verna Marrs McLean Department of Biochemistry &
Molecular Pharmacology, Baylor College of Medicine, Houston, TX USA
2Department of Molecular & Cellular Biology, Harvard University, Cambridge MA USA
3Department of Biochemistry and Functional Genomics, Université de Sherbrooke, Québec CA
*Authors contributed equally
†Corresponding authors: eric.vannostrand@bcm.edu, amanda_whipple@fas.harvard.edu
Abstract
Small nucleolar RNAs (snoRNAs) are non-coding RNAs that function in ribosome and
spliceosome biogenesis, primarily by guiding modifying enzymes to specific sites on ribosomal
RNA (rRNA) and spliceosomal RNA (snRNA). However, many orphan snoRNAs remain
uncharacterized, with unidentified or unvalidated targets, and studies on additional snoRNA-
associated proteins are limited. We adapted an enhanced chimeric eCLIP approach to
comprehensively profile snoRNA-target RNA interactions using both core and accessory snoRNA
binding proteins as baits. Using core snoRNA binding proteins, we confirmed most annotated
snoRNA-rRNA and snoRNA-snRNA interactions in mouse and human cell lines and called novel,
high-confidence interactions for orphan snoRNAs. While some of these interactions result in
chemical modification, others may have modification-independent functions. We then showed that
snoRNA ribonucleoprotein complexes containing certain accessory proteins, like WDR43 and
NOLC1, enriched for specific subsets of snoRNA-target RNA interactions with distinct roles in
ribosome and spliceosome biogenesis. Notably, we discovered that SNORD89 guides 2'-O-
methylation at two neighboring sites in U2 snRNA that are important for activating splicing, but
also appear to ensure imperfect splicing for a subset of near-constitutive exons. Thus, chimeric
eCLIP of snoRNA-associating proteins enables a comprehensive framework for studying
snoRNA-target interactions in an RNA binding protein-dependent manner, revealing novel
interactions and regulatory roles in RNA biogenesis.
1
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
Introduction
Small nucleolar RNAs (snoRNAs) constitute a class of non-coding RNAs primarily known for their
fundamental roles in ensuring the proper biogenesis of ribosomal RNA (rRNA). SnoRNAs can be
categorized into box C/D and box H/ACA snoRNAs, distinguished by the presence of conserved
box motif sequences and structural features. In addition, a class of snoRNAs known as small
Cajal body-specific snoRNAs (scaRNAs), which contain either C/D, H/ACA, or hybrid (both) motifs,
are involved in the biogenesis of spliceosomal RNAs (snRNAs). During their maturation, snoRNAs
associate with core RNA-binding proteins (snoRBPs) to form functional snoRNPs. Specifically,
C/D snoRNAs associate with FBL, NOP56, NOP58, and SNU13 (NHP2L1/15.5K), while H/ACA
snoRNAs associate with DKC1, NOP10, NHP2 and GAR1 (Fig. 1A). SnoRNPs translocate to the
nucleolus or Cajal body, where they interact with nascent pre-rRNA or snRNA [1]. The antisense
elements of snoRNAs engage in base pairing with their RNA targets, orchestrating the precise
positioning of 2’-O-methylation (Nm) by C/D snoRNPs or isomerization of uridine to pseudouridine
(Ψ) by H/ACA snoRNPs. Human rRNA contains more than 200 nucleotides that undergo
snoRNA-guided chemical modification [2]. Some of these chemical modifications cluster at
functionally important regions of the ribosome, such as the peptidyl transferase center, tRNA
binding sites, and the interface between the small and large subunits, and they contribute to the
stabilization of rRNA folding, facilitation of efficient ribosome assembly, export of ribosomal
subunits, and binding interactions with translation factors [3–5].
Over the years, research efforts have successfully identified snoRNA-target pairs for most known
2’-O-methylation and pseudouridine sites in rRNA. Advances in mass spectrometry approaches
and high-throughput assays have facilitated the discernment of nucleotides subject to chemical
modifications [2]. Additionally, bioinformatics tools have been employed to associate numerous
snoRNAs with specific rRNA modification sites [6–9] . The development of RNA-RNA interaction
mapping tools have validated additional snoRNA-rRNA interactions [10–15]. However, despite
these collective efforts, the targets for a considerable subset of snoRNAs, known as orphan
snoRNAs, have yet to be identified or experimentally validated.
Beyond their role in rRNA modifications, C/D snoRNAs can guide Nm in other RNA targets. This
extends to snRNAs, tRNAs, and even a few mRNAs [13,16–20]. Furthermore, C/D snoRNAs can
act in a chaperone-like fashion independent of chemical modification. For instance, base pairing
2
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
interactions between snoRNAs and pre-rRNA contribute to rRNA processing and assembly by
influencing pre-rRNA conformation [21,22]. Additionally, interactions between snoRNAs and pre-
mRNA can contribute to splicing and 3’ end processing [20,23,24], further highlighting the
multifaceted roles of these snoRNAs beyond guiding chemical modifications. In many instances,
these non-traditional functions require the assembly of additional proteins to snoRNA complexes
[24–26]; however, the landscape of RNA-binding proteins (RBPs) and their snoRNA-interacting
networks beyond the core snoRBP complexes remain undercharacterized.
Here we performed a deep, large-scale profiling of RNA interactions for all eight core RNA-binding
protein components of the C/D and H/ACA snoRNA complexes. We then adopted chimeric eCLIP
to directly capture snoRNA-target RNA interactions, utilizing both established core proteins and
lesser-known snoRNA-associated RBPs as bait. Our results demonstrate that chimeric eCLIP
successfully corroborated canonical snoRNA interactions with rRNAs and snRNAs. Moreover, we
discovered novel interactions of orphan snoRNAs with rRNA and snRNA, a subset of which
mediate chemical modification at the target site. Using non-core snoRNA-associated RBPs as
baits in chimeric eCLIP revealed specific subnetworks of snoRNAs, suggesting specific roles of
snoRNAs in distinct stages of snRNA or rRNA biogenesis. We further show that one such snoRNA,
SNORD89, plays a key role in 2’-O-methylation of the G11 and G12 sites in U2 snRNA, which
appears to be essential for maintaining imperfect splicing. Together, this study presents a
systematic approach to investigate snoRNA-target interactions, revealing novel roles in RNA
biogenesis and splicing regulation, and highlighting the potential for further discoveries in snoRNA
biology.
Results
Core snoRNP proteins show consistent RNA interactomes
Previous profiling of the RNA interactomes of core C/D snoRNP proteins FBL, NOP56, and
NOP58 by CLIP-seq led to the characterization of novel snoRNAs as well as the identification of
candidate interactions for orphan snoRNAs [27,28]. However, of the four core H/ACA snoRNP
proteins, the RNA interactome has only been profiled for DKC1 [27,29]. To expand upon this prior
work, we set out to use the updated eCLIP framework that allows deeper recovery of unique RNA
molecules as well as quantitative normalization against input controls to comprehensively profile
the direct interactions for the C/D and H/ACA snoRNP complex members [30]. We obtained and
3
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
performed IP-western blot validation of antibodies against the four core proteins for both C/D (FBL,
NOP56, NOP58, and SNU13) and H/ACA (DKC1, NOP10, NHP2, and GAR1) snoRNP
complexes respectively (Fig. S1A), followed by eCLIP in K562 cells to facilitate contrast analysis
with other ENCODE RBP datasets (Fig. 1B).
Basic analysis of snoRBP eCLIP indicated successful enrichment of snoRNAs (Fig. 1C,D). Similar
to previous observations with PAR-CLIP [27], eCLIP for FBL, NOP56, NOP58, and SNU13 each
showed significant enrichment for C/D snoRNAs versus paired input (³ 6.5-fold) (Fig. 1C). Over
5% of reads mapped to C/D snoRNAs for FBL and NOP56, with an additional 80% of reads
mapping to either precursor or mature rRNA; NOP58 and SNU13 had significantly enriched but
lower frequency of reads mapping to C/D snoRNAs (>1.5%) (Fig. 1C). The C/D snoRBPs showed
an average 1.5-fold depletion for H/ACA snoRNAs compared to size-matched inputs, suggesting
that the C/D complex shows specificity for binding to C/D snoRNAs (Fig. 1C,D). Similarly, all four
H/ACA snoRBPs showed significant enrichment for H/ACA snoRNAs (³ 6.2-fold) (Fig. 1C,D).
Over 5% of reads mapped to H/ACA snoRNAs for each RBP and another 71% to rRNA (Fig. 1C).
Surprisingly, all four H/ACA snoRBPs also showed enrichment for C/D snoRNAs (³ 2.5-fold) (Fig.
1C,D), which may indicate a broader role for H/ACA snoRBPs or reflect low-level co-
immunoprecipitation of FBL in these experiments (Fig. S1B).
Previous research has observed examples of sub-complex specificity, as SNU13 is involved in
other RNA-protein complexes such as the U4/U6.U5 tri-snRNP [31] in addition to its role in
snoRNP assembly. Consistent with this, eCLIP of SNU13 but not the other C/D snoRBPs showed
enrichment at the 5’ stem loop of the U4 snRNA similar to other U4-interacting tri-snRNP factors
(Fig. S1C). However, when we performed transcriptome-wide analysis comparing the enrichment
of individual snoRNAs, we observed striking pair-wise correlation in per-snoRNA enrichment
among all core C/D snoRBPs (all Pearson R > 0.90) and significant correlation in enrichment
among all core H/ACA snoRBPs (R > 0.50) (Fig. 1E,F), which was independent of FBL or DKC1
co-immunoprecipitation (Fig. S1B). In contrast, there is little correlation in per-snoRNA enrichment
between C/D and H/ACA snoRBPs, such as FBL and DKC1 (R = 0.02) (Fig. 1E,F). To consider
these results in the context of outgroup (non-snoRNA-related) RBPs, we utilized available
ENCODE eCLIP data to compare the correlation of enrichment for individual snoRNAs across
149 other RBPs. Although the majority of RBP and negative control (using FLAG or V5 pulldown
in wildtype cells) datasets were depleted for snoRNAs (Fig. 1D), we surprisingly observed a
significant per-snoRNA correlation with FBL across RBP datasets (median R = 0.62) and negative
4
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
controls (median R = 0.76) that may reflect low-level co-precipitation of the C/D snoRNP complex
across eCLIP experiments (Fig. S1B,D). However, the correlation between pairs of core C/D or
H/ACA snoRBPs was higher than with nearly any other RBPs (Fig. S1D), providing further
evidence that the four core C/D and four core H/ACA snoRBPs coordinately associate with C/D
and H/ACA snoRNAs, respectively, in a consistent manner.
In order to examine how snoRBP interaction profiles compare across cell types, we performed
FBL and DKC1 eCLIP in 293T and HepG2 cells in addition to K562 cells. The enrichment of
snoRNAs across the profiled cell lines is highly correlated (Fig. S1E). When considering well
expressed snoRNAs present at more than 10 reads per million in at least one cell type, only 6
snoRNAs (SNORD50, SNORD64, SNORD109, SNORD115, SNORD116, and SNORA35) show
cell type-specific binding to FBL or DKC1 (Fig. S1F). These data suggest that the snoRNA
landscape is highly consistent across cancer cell types. In summary, we comprehensively profiled
the RNA interactions of all core proteins in both the C/D and H/ACA snoRNP complexes. We
demonstrated that the core proteins within each complex coordinately associate with the
respective C/D or H/ACA snoRNAs and that the binding specificity of snoRNP complexes is
strongly cell type independent.
Chimeric eCLIP of core C/D snoRNP proteins comprehensively recovers known C/D
snoRNA interactions
Chimeric CLIP approaches enable unambiguous identification of RNA-RNA interactions by taking
advantage of an intramolecular ligation of interacting RNAs during immunoprecipitation, which
can then be read out as a ‘chimeric’ sequencing read that contains both fragments [15]. Prior
analysis of CLIP for C/D snoRBPs successfully recovered C/D snoRNA-target interactions
through mapping chimeric reads [14,15,28]. Here, we set out to determine whether we could
deeply interrogate snoRNA-target interactions across cell lines and organisms with chimeric
eCLIP, using core C/D snoRNP proteins as bait (Fig. 2A). Chimeric eCLIP combines the library
preparation optimizations in eCLIP with an additional ligation step to encourage intermolecular
ligations between co-precipitated RNA-target fragments [32]. SnoRNA targets have been
extensively queried in human cancer cell lines but less characterized in rare cell types or other
mammalian systems, so we profiled mouse embryonic stems cells (mESC) in addition to a
standard human cell line (293T) and implemented a computational pipeline to identify
snoRNA:target chimeric reads (Fig. S2A).
5
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
Chimeric eCLIP generated 0.2 – 0.6% chimeric reads out of total reads in FBL and NOP56
libraries from mESC and FBL, NOP56, and NOP58 libraries from 293T cells (Fig. S2B). The
efficiency of chimeric read formation was on par with or slightly better than a previously reported
ligation-based approach [11]. The per-snoRNA abundance was highly correlated between non-
chimeric and chimeric reads (Fig. 2B), indicating that chimeric ligation does not cause biased
recovery of snoRNAs. The number of chimeric reads per snoRNA was highly correlated between
different core C/D snoRBP baits in both mESC (Fig. 2C) and 293T cells (Fig. S2C). This result,
similar to our observations by eCLIP, suggests a consistent recovery of snoRNA-target
interactions using any of the core C/D snoRBPs. It is noteworthy that the number of chimeric
reads between core C/D snoRBPs was highly correlated for SNORD13, an acetylation-guiding
C/D snoRNA, as well as orphan C/D snoRNAs that lack known targets (Fig. 2C, S2C). These
results implicate FBL as a constitutive component of the C/D snoRNP complex irrespective of
Nm-guiding activities, and they further justify the suitability of FBL chimeric eCLIP approaches for
identifying targets of orphan snoRNAs.
We captured chimeric reads for nearly all expressed C/D snoRNAs in each cell line, namely 143
out of 145 (99%) expressed snoRNAs in mESC [RPM >= 3] (Fig. 2D) and 116 out of 125 (92%)
expressed snoRNAs in 293T cells [RPM >= 3] (Fig. S2D). The capture of chimeric reads to a
larger proportion of snoRNAs in mESC compared to 293T cells was likely due to the greater
sequence depth of the mESC libraries (Fig. S2B; 80M raw reads in mESC versus 30M raw reads
in 293T). The highest numbers of chimeric reads were captured for highly abundant snoRNAs
that mediate pre-rRNA processing, such as Snord3, Snord14, and Snord118, but we observed
substantial coverage for both ‘canonical’ snoRNAs, which guide modification on rRNA and snRNA,
and orphan snoRNAs whose targets are unknown (Fig. 2D,E, S2D).
As an initial evaluation of the success of chimeric eCLIP in identifying known C/D snoRNA-target
interactions, we mapped chimeric reads to pre-rRNA and snRNA. Chimeric reads were observed
primarily to the mature regions of rRNA and had a distinct distribution profile compared to non-
chimeric reads from input or IP samples (Fig. 2F). Visual examination of individual snoRNA:rRNA
and snoRNA:snRNA chimeric read tracks showed a marked enrichment of chimeric reads at their
known Nm-guiding target sites in mESC (Fig. 2G) and 293T cells (Fig. S2E). Furthermore,
metagene analysis highlighted a significant enrichment of chimeric reads at Nm sites in both rRNA
and snRNA that is not observed at pseudouridylation sites (Fig. 2H, S2F). All together, these
6
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
analyses lend strong support to the power and accuracy of chimeric eCLIP in experimentally
detecting snoRNA-target interactions by C/D snoRBPs.
Transcriptomic mapping of C/D snoRNA chimeras calls novel, high-confidence
interactions
Next, we performed transcriptome-wide mapping of the chimeric reads obtained from core C/D
snoRBP chimeric eCLIP in mESC and 293T cells. We examined the chimeric read distribution
amongst different RNA classes. The majority of snoRNA chimeras mapped to rRNA (~75%,
mESC; ~55%, 293T), and to a lesser extent, pre-mRNA (~10%, mESC; ~20%, 293T), snRNA
(~0.3%, mESC and 293T), and tRNA (~0.1%, mESC; ~0.4%, 293T) (Fig. 3A, S3A). When the
chimeric read distribution was analyzed for individual canonical snoRNAs, we observed that
rRNA-targeting snoRNAs had the highest proportion of rRNA-mapping chimeras, whereas some
snRNA-targeting snoRNAs had an appreciably higher proportion of snRNA-mapping chimeras
(Fig. S3B). Interestingly, the chimeric read distribution for individual orphan snoRNAs hinted at
possible target classes; Snord23 and Snord89 chimeras were enriched for snRNAs while Snord90
and Snord101 were enriched for rRNA (Fig. S3B).
To call high-confidence interaction sites across the transcriptome, we performed peak calling
using Clipper [33]. Peaks at known interaction sites were readily distinguished from poorly
supported ‘background’ peaks when two parameters were considered: peak fold enrichment
(chimeric reads from snoRBP IP relative to non-chimeric reads from input) and fraction of per-
snoRNA reads in peak (chimeric reads in peak relative to total number of per-snoRNA chimeric
reads) (Fig. S3C). The fraction of per-snoRNA reads in peak (i.e. the most predominant peak(s)
for each snoRNA) was deemed a good classifier of positive interactions as the receiver operating
characteristic curve (ROC) for known snoRNA-rRNA interactions presented an area under the
curve of 99.2% in mESC and 97.4% in 293T cells (Fig. S3D).
Based on the optimal threshold determined by ROC (0.026, mESC; 0.075, 293T), we selected a
peak fraction ³ 0.1 and peak fold enrichment ³ 3 as thresholds to minimize the false positive rate
and stringently call high-confidence interactions. We called a maximum of two significant peaks
per snoRNA (Fig. S3E), consistent with the presence of two antisense elements per snoRNA.
When considering significant peaks called in both FBL and NOP56 chimeric eCLIP datasets from
mESCs (i.e. reproducible peaks), we identified high-confidence interactions for 70% (102 out of
7
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
145) of expressed snoRNAs. This included significant peaks at 84% (90 out of 107) of known
snoRNA-rRNA interactions and two known snoRNA-snRNA interactions (Fig. 3B). Peaks were
present at an additional 17 known rRNA and snRNA interaction sites but fell below the stringent
threshold (Fig. S3F). In 293T cells, we called a smaller percentage of snoRNA-rRNA interactions
that are annotated in snoDB (Fig. S3F,G), likely reflecting the increased annotation of rare
snoRNAs in human cancer cells.
Importantly, our analyses detected significant, reproducible peaks at a number of novel snoRNA
interaction sites (Table S1). This included 21 novel snoRNA-rRNA and 1 novel snoRNA-snRNA
interactions in mESC (Fig. 3B). While an additional 4 novel interactions were observed with pre-
mRNA, the peaks were located around or adjacent to intron-embedded snoRNAs (Fig. S3H),
potentially indicating spurious chimeric RNA formation during snoRNA biogenesis or incomplete
snoRNA annotation. In total, we assigned high-confidence interactions for 10 orphan snoRNAs
(Table S1); for example, Snord89 with U2 snRNA and Snord90, Snord101, Snord117, DQ267101,
and Gm26922 with rRNA (Fig. 3C). We also observed an interaction between orphan Snord23
and U6 snRNA, but it fell below the significance cutoff (Fig. 3C). Beyond orphan snoRNAs, we
called novel interactions for canonical snoRNAs that already have one antisense element
assigned as an Nm guide. For example, Snord31, Snord51, Snord54, Snord62, and Snord82
each had two significant peaks in rRNA (Fig. 3C) — one peak at the known Nm target site and a
second peak at the novel site. Lastly, we detected significant, reproducible peaks for two
snoRNAs that mediate pre-rRNA processing, Snord14 and Snord118 (Fig. 3C). A high degree of
concordance was observed across reproducible peaks in mESC and 293T cells (Table S1).
Box C/D snoRNAs base pair with their targets through an antisense element located immediately
upstream of the D or D’ box element. To further characterize the interactions identified by chimeric
eCLIP, we predicted the snoRNA antisense element associated with each interaction, then
quantified the base pair complementarity of the snoRNA-target interaction. The base pair
complementarity for novel snoRNA-rRNA interaction sites was slightly lower than known sites
(78.1% mean identity at novel sites versus 86.8% at known sites) and was more commonly
associated with D’ box elements (Fig. 3D). The strength of the conserved ‘CTGA’ box motif was
higher for known snoRNA-rRNA interactions compared to novel interactions (Fig. 3E), which is
consistent with the lower conservation of D’ box motifs compared to D box motifs. This observation
suggests that the novel interactions identified by chimeric eCLIP more frequently involve less
8
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
conserved D’ box motifs, which could explain why these interactions have not been identified by
previous bioinformatic approaches utilizing sequence complementarity modeling.
Canonical snoRNAs guide Nm to the site on target RNA that is base paired exactly 5 nucleotides
upstream of the snoRNA D/D’ box. To determine potential snoRNA-guided methylation at novel
interactions in mESC, we quantified Nm levels in rRNA and snRNA by RiboMeth-seq (RMS) [34].
High levels of methylation were observed at the fifth nucleotide position for nearly all known
snoRNA interactions detected in our study (mean RMS = 0.78, Fig. 3F). Novel interactions
displayed overall lower RMS scores at the predicted methylation sites (mean RMS = 0.34, Fig.
3F), indicating possible methylation-independent functions of these interactions. Several novel
sites, though, did display high levels of methylation at the expected nucleotide, including 18S-C87
(Snord14), 18S-U355 (Snord90), 28S-G3283 (Snord101), 28S-G4022 (Snord62), U2-G12
(Snord89), and U6-A70 (Snord23) (Fig. 3C). Snord60 is already assigned as the guide for
modification at 28S-G4022, so the co-detection of Snord60 and Snord62 at this site in our study
could indicate compensatory or competitive interactions that merit further investigation.
Based on our data we hypothesized that Snord89 guides methylation at U2-G12, as similarly
observed in a yeast cell system [35]. To examine the targeting specificity of Snord89 in mouse
cells, we performed loss-of-function experiments followed by RiboMeth-seq. Surprisingly, we
found that ASO-mediated knockdown of Snord89 resulted in loss of methylation at two
neighboring nucleotides in U2, as methylation at U2-G11 and U2-G12 were decreased by 72%
and 37%, respectively (Fig. 3G). We then validated the targeting specificity of Snord101 using the
same approach. ASO-mediated knockdown of Snord101 resulted in complete loss of methylation
at 28S-G3283 with no effect on the flanking Nm sites (Fig. 3H).
We also tested whether the chimeric eCLIP approach could capture H/ACA snoRNA-target
interactions by performing chimeric eCLIP with DKC1 and GAR1 as the bait proteins from 293T
cells. Analysis of non-chimeric reads from chimeric eCLIP yielded similar results to standard
eCLIP, as over 24% of reads mapped to snoRNAs with greater recovery for H/ACA snoRNAs
( 16% and 20% of total reads by DKC1 and GAR1) versus C/D snoRNAs (7% in both RBPs) (Fig.
S4A). Chimeric analysis recovered ~1% chimeric reads out of total reads, but despite the higher
recovery of H/ACA snoRNAs among non-chimeric reads, we observed that less than half of the
chimeric reads contained an H/ACA snoRNA (Fig. S4B). Manual inspection of well-studied H/ACA
snoRNAs suggested that while some known sites may be captured, most showed poor recovery
9
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
and resolution at known target regions (Fig. S4C). Performing peak calling confirmed that DKC1
chimeric eCLIP had at best marginal recovery of true interactions (Fig. S4D). We hypothesize that
the distinct structural complexity of H/ACA snoRNAs may make them refractory to standard
chimeric CLIP approaches and that alternative approaches will be required to profile H/ACA
interactomes.
Thus, these results confirm that chimeric eCLIP can be used to find new C/D snoRNA interactions
for but requires further optimization for H/ACA snoRNAs. We identified high-confidence
interactions with reproducibility between different core C/D snoRBP baits in rRNA and snRNA, a
subset of which may involve alternative functions or regulatory mechanisms beyond 2’-O-
methylation. Compared to bioinformatic approaches, this experimental approach is agnostic to
the identification of D/D’ box motifs, target RNA class, or presence of chemical modification at the
target site.
Identification of specific subsets of snoRNA-target interactions using orthogonal protein
baits
In addition to the core C/D and H/ACA snoRNA binding proteins, several additional RBPs have
been reported to associate with snoRNAs and regulate their functions beyond guiding rRNA
modifications [24,36]. As these interactions are under-explored, we set out to test whether
performing chimeric eCLIP with less-studied snoRNA-associated proteins would enrich for
functionally related subsets of snoRNAs and help uncover new aspects of snoRNA biology. We
first identified candidate bait proteins to use in our study by integrating our core C/D and H/ACA
snoRBP eCLIP datasets with the 150 RBPs profiled by ENCODE to analyze snoRNA enrichment
with a customized analysis pipeline [29,37]. While the majority of evaluated RBPs displayed a
depletion for both C/D and H/ACA snoRNAs, 11 RBPs (in addition to the core snoRBPs above)
showed at least 4-fold enrichment for snoRNAs and may represent potential snoRNA partners
(Fig. 4A). These non-core snoRBPs clustered into two functional annotations: a cluster of RBPs
that included splicing- and spliceosomal RNA-associated factors (LARP7, NOLC1, PTBP1,
SMNDC1, TRA2A, and ZC3H8), discussed further below, and a cluster of rRNA processing
factors (AATF, UTP3, UTP18, WDR3, WDR43) which showed even stronger specificity for C/D
snoRNAs than the core C/D snoRBPs (Fig. 4A). Considering individual snoRNA enrichment, we
observed that these rRNA processing RBPs, members of the small-subunit (SSU) processome
[38,39], were particularly enriched for the processing snoRNA SNORD3 (U3) relative to FBL (Fig.
10
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
4B, S5A). Comparing SNORD3 fold-enrichment across all RBPs in ENCODE confirmed that rRNA
processing RBPs, and particularly the small-subunit processome, showed strong enrichment for
SNORD3 (Fig. 4C, S5B), consistent with the critical role of SNORD3 in coordinating the function
of the SSU in rRNA processing [40].
To test whether we could recover distinct interaction profiles of SNORD3 associated with these
SSU factors versus the core C/D snoRNP complex, we performed chimeric eCLIP for WDR43
and UTP18 in K562 cells (Fig. S5C). Although SNORD3 was typically the most frequently
observed snoRNA in chimeric reads for all RBPs profiled (Fig. S5D), WDR43 and UTP18 showed
an even higher frequency of SNORD3:rRNA chimeras compared to FBL, NOP56, or NOP58 (Fig.
S5E). Visual examination of SNORD3:rRNA chimeric read tracks showed a strong enrichment of
SNORD3 chimeric reads in the 5’ETS region of pre-rRNA, with a distinct interaction profile for
UTP18 and WDR43 compared to FBL or other core C/D snoRBPs (Fig. 4D, purple, red, and
orange peaks). SNORD3 chimeric reads were enriched and preferentially positioned at the 01-
A0 early processing sites with WDR43 and UTP18 pulldown compared to FBL (Fig. 4E, S5F),
consistent with SSU-associated SNORD3 playing a key role in interacting with these sites during
early ribosomal processing. We also see capture of SNORD3 chimeras with UTP18 and WDR43
at other downstream sites in pre-rRNA in a manner distinct from FBL, suggesting that SSU-
mediated SNORD3 interactions may also drive later rRNA processing steps (Fig. 4D, yellow and
green peaks). Notably, sequence alignment indicates that sequences within the 01/A’ (400-700
nucleotide) and intermediate 700-1000 nucleotide regions of pre-rRNA are complementary to
overlapping regions of SNORD3 (Fig. 4F), suggesting that the chimeras may reflect sequential
interactions during the complex series of processing steps involved in pre-rRNA transcription,
folding, and maturation [41]. Overall, these results indicate that chimeric eCLIP for SSU
processome components can recover SNORD3 interactions distinct from those observed with
FBL, validating the principle that using unique protein baits can reveal new snoRNA interaction
landscapes.
Chimeric eCLIP of LARP7 and NOLC1 detects unique snoRNA-snRNA interactions
Post-transcriptional modifications of snRNAs are essential for spliceosomal fidelity and are largely
guided by snoRNAs, with the scaRNA class playing a particularly important role [42,43]. More
snoRNA-snRNA interactions continue to be discovered, including our identification of Snord23-
U6 and Snord89-U2 interactions above and other recent work [18]. This, together with a recent
11
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
study that identified LARP7 as a novel bridging factor for snoRNA-guided modifications on U6
[25,44], suggests that more principles of snRNA regulation by snoRNAs are yet to be uncovered.
As such, we next asked whether chimeric profiling of the splicing- and spliceosomal RNA-
associated proteins we identified above could enrich for unique snoRNA-snRNA regulatory
networks.
As validation of this approach, we first examined LARP7. Previous studies proposed a mechanism
in which LARP7 binds the subset of C/D snoRNAs that have been shown to guide U6 2’-O-
methylation, including SNORD7, SNORD8, SNORD9, SNORD10, SNORD67, and SNORD94
[25]. Consequently, we performed chimeric eCLIP on LARP7 and FBL in HepG2 cells (Fig. S6A)
to determine if LARP7 could capture and enrich for these snoRNA-U6 interactions. We observed
that the previously characterized LARP7-associated snoRNAs had the highest enrichment among
non-chimeric (i.e. snoRNA only) and chimeric reads in LARP7 compared to FBL chimeric eCLIP
(Fig. 5A,B, S6B). SnoRNA:U6 chimeras were recovered for five of the six LARP7-associated
snoRNAs, and these chimeras mapped to the known U6 Nm target sites in both FBL and LARP7
datasets (Fig. 5C,D), validating the role of LARP7 in bridging functional snoRNA-snRNA
interactions. Many of the other U6-interacting snoRNAs annotated in snoDB were not captured
by FBL, and manual inspection of their annotation source found these were often supported by
sparse interaction data and lacked validation of snoRNA-responsive methylation. Overall,
recovery of chimeras for known snoRNA-U6 interactions was 2.2 times higher in LARP7 versus
FBL chimeric eCLIP, whereas recovery of chimeras for known snoRNA-rRNA interactions was
dramatically lower (11.9 times) (Fig. 5E,F). These data confirm that chimeric eCLIP can capture
and enrich for specific subsets of snoRNA interactions involving LARP7.
We then looked for novel RBP baits that could highlight additional snoRNA-snRNA interaction
principles. We further analyzed the ENCODE RBP eCLIP data and identified four spliceosomal
RNA-associated proteins (NOLC1, SMNDC1, ZC3H8, and PTBP1) with co-enrichment for both
snoRNAs and scaRNAs (Fig. S6C). These RBPs were also often enriched for either U2 or U6
snRNAs, echoing their known roles in snRNA processing (Fig. S6D,E) [45–48]. Next, we
performed chimeric eCLIP for NOLC1, SMNDC1, and ZC3H8 in the same cell lines as the
ENCODE eCLIP experiments: NOLC1 in HepG2 cells and SMNDC1 and ZC3H8 in K562 cells
(Fig. S6A). Due to technical issues, PTBP1 was not profiled. We noted that the size-resolved
band of NOLC1 was present in standard eCLIP but lost after chimeric ligation (Fig. S6A,F),
suggesting that this ligation may create a mixture of higher-order complexes.
12
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
NOLC1 chimeric eCLIP enriched for snoRNA:snRNA chimeras compared to either FBL or LARP7
(Fig. S6G), with a pronounced enrichment for both U2 and U6 chimeras (Fig. 5G). In contrast,
SMNDC1 and ZC3H8 had low recovery of snoRNA:snRNA chimeras for U2 and U6 despite their
enrichment among non-chimeric reads (Fig. 5G, S6H), and we did not pursue further analysis on
these RBPs. Unlike LARP7, NOLC1 chimeric eCLIP did not enrich for a specific subset of C/D
snoRNAs; rather, the entire class of scaRNAs was enriched in NOLC1 versus FBL chimeric eCLIP
among both non-chimeric reads (Fig. 5H) as well as chimeric reads (Fig. 5I). This included not
only scaRNAs containing box C/D motifs, but also H/ACA and hybrid motifs, consistent with the
role of NOLC1 in maturation and function of both snoRNA classes [49].
For C/D-containing snoRNAs known to target U2 or U6, in many cases NOLC1 recovered
chimeras at their known target sites, as illustrated for SCARNA2 and SCARNA9 in U2 (Fig. 5J)
and SNORD8, SNORD9, and SNORD10 in U6 (Fig. 5D). The enrichment profiles for these known
snoRNA guides were very similar to chimeric eCLIP of FBL (Fig. 5D,J), suggesting NOLC1 may
act in concert with the core snoRNP at these target sites. In addition, we also observed chimeras
with snoRNAs that have not previously been linked to U2 (n = 22) and U6 (n = 9) (Fig. S6I).
Interestingly, we noted that many of candidate interactions lack chimeric support in FBL pulldown,
had a stereotypical positioning of NOLC1 chimeras in the central region of U2 which overlaps the
Sm binding region, and contained snoRNAs that have been shown to target modifications on
other snRNAs (Fig. 5J, S6J), suggesting that these unique chimeras in NOLC1 pulldown may
reflect the more general role of NOLC1 in snRNA biogenesis [49,50]. In summary, these results
suggest that chimeric eCLIP can successfully enrich for previously characterized snoRNA
interactions, as well as provide further depth to identify and understand novel interactions driven
by non-canonical snoRNP complexes.
SNORD89 mediates U2 processing to fine-tune splice site recognition
To test whether integration of NOLC1 and FBL chimeric experiments could reveal biological
insights into U2 function, we performed further studies of one poorly characterized snoRNA with
strong chimeric signal in NOLC1 and FBL experiments, SNORD89. While NOLC1 captured
SNORD89:U2 chimeras throughout U2 (with an enrichment in the central Sm binding region),
FBL and NOP56 captured SNORD89:U2 chimeras primarily at the 5’ end of U2 (Fig. 3C, 5J),
overlapping the G11 and G12 Nm target sites that are responsive to SNORD89 knockdown (Fig.
13
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
3G). The functional impact of U2 modification at these specific nucleotides remains unclear:
methylation at G12 was shown to be essential for splicing progression on a single pre-mRNA in
vitro [43] but has not been explored on transcriptome-wide in vivo, and the role of G11 methylation
is unknown. Thus, we next wanted to examine the functional impact of SNORD89 loss on
spliceosomal activity.
To quantify the effect of SNORD89 on splicing in human cells, we performed SNORD89 ASO
knockdown in 293T cells (Fig. 6A), followed by RNA-seq. Analysis of alternative splicing identified
300 cassette exons more excluded upon SNORD89 knockdown (‘knockdown-excluded exons’)
and 334 cassette exons more included upon SNORD89 knockdown (‘knockdown-included exons’)
(Fig. 6B), confirming that SNORD89 significantly alters splicing. In further analysis, we noted that
SNORD89 preferentially regulates exons with nearly constitutive splicing — 60% of knockdown-
excluded exons had percent spliced in (PSI) values of 0.95 or higher in control samples, and 66%
of knockdown-included exons had PSI values of 0.95 or higher upon SNORD89 ASO (Fig. 6C).
To consider whether the effect of SNORD89 on knockdown-excluded exons with high PSI values
was unique, we performed re-analysis of 473 RBP knockdown datasets generated by the
ENCODE consortium [29]. We observed that canonical alternative splicing regulators showed a
more varied distribution of PSI values for knockdown-excluded exons whereas spliceosomal
components showed a pattern similar to SNORD89. For example, only 20% (28 out of 143) of
PTBP1-dependent exons had PSI ³ 0.95 in controls (Fig. 6D), but 57% (571 out of 1003) of
U2AF1-dependent exons had PSI ³ 0.95 in controls (Fig. 6E). Indeed, considering all 64 ENCODE
datasets with at least 100 knockdown-excluded exons, the observation that more than half of
knockdown-excluded exons had PSI ³ 0.95 in controls was only seen for RBPs that were core
components of the spliceosome or exon junction complex (Fig. 6F). Thus, SNORD89 enables
inclusion of a set of near-constitutive exons similar to core splicing machinery RBPs.
In contrast, similar analysis of knockdown-included exons across ENCODE datasets indicated
that the preferential regulation of near-constitutive exons was a unique property of SNORD89, as
no RBP knockdown from ENCODE showed more than 20% of knockdown-included exons with
PSI ³ 0.95 (Fig. 6G). Thus, rather than simply being essential for enabling recognition of
constitutive splice sites, SNORD89-mediated modifications on U2 appear to play a more precise
role in limiting complete processing of near-constitutive sites. Analysis of intron retention
suggested a similar role: SNORD89 knockdown caused a 24.7% decrease in the overall fraction
14
bioRxiv preprint doi: https://doi.org/10.1101/2024.09.19.613955; this version posted September 21, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC-ND 4.0 International license.
of intronic reads observed (from 7.4% in control to 5.6% in knockdown) (Fig. S7A), and intron-
specific analysis of SNORD89 knockdown showed only 250 retained introns with increased
retention but 800 retained introns with increased splicing (Fig. S7B).
The observation that SNORD89 knockdown more often led to more efficient splicing of retained
introns, coupled with SNORD89 knockdown causing both increased and decreased mis-splicing
of near-constitutive cassette exons, suggested that SNORD89 might be playing a unique role in
maintaining both accurate and inaccurate splicing of specific introns. To test this hypothesis, we
queried whether SNORD89 knockdown altered the accuracy of utilizing known splice junctions.
We observed that SNORD89 knockdown caused a 12% decrease in the frequency of
unannotated splice junctions (Fig. S7C), indicating that SNORD89 is acting to maintain rather
than suppress utilization of unannotated junctions. In sum, these results suggest that
modifications directed by SNORD89 are not only essential for proper splicing but may also be
playing a critical role in maintaining splicing errors at a subset of splice sites.
Discussion
SnoRNAs play crucial roles in the modification and processing of rRNA and snRNA, impacting
fundamental cellular processes such as translation and splicing. Despite clear biological
relevance, research efforts have failed to identify targets for many orphan snoRNAs, and the roles
of snoRNA-associated proteins are not well characterized. To address these gaps in
understanding, we implemented an improved chimeric eCLIP approach that enables deep and
accurate profiling of snoRNA interactions in an RBP-dependent manner. This new approach
resulted in increased depth of snoRNA:target chimeras relative to previous efforts to directly map
snoRNA interactions [14,15,18,28]. The high accuracy achieved (AUC > 97% in both human and
mouse cell lines) allows for benchmarking against known targets and the characterization of novel
interactions. Notably, this accuracy was achieved empirically without needing to model interaction
complementarity as in previous work [28], enabling recovery of candidate interactions that may
have non-canonical interaction dynamics.
Using stringent peak calling criteria, we identified novel snoRNA interactions, including those of
orphan snoRNAs. For example, we called a high-confidence interaction between Snord101 and
28S rRNA as well as Snord89 and U2 snRNA. While similar interactions were detected in previous
chimeric ligation sequencing approaches, the predicted Nm sites were either inaccurate or lacked
15
