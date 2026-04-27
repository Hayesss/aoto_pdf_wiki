---
source_path: /mnt/c/Users/Administrator/Zotero/storage/HIXLNEUN/Monserrat 等 - 2021 - Disruption of the MSL complex inhibits tumour maintenance by exacerbating chromosomal instability.pdf
ingested: 2026-04-23
sha256: a3be6a37159f8cec
---

Europe PMC Funders Group
Author Manuscript
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Published in final edited form as:
Nat Cell Biol. 2021 April 01; 23(4): 401–412. doi:10.1038/s41556-021-00657-2.
Disruption of the MSL complex inhibits tumor maintenance by
exacerbating chromosomal instability
Josep Monserrat1, Cristina Morales Torres1, Louise Richardson1, Thomas S. Wilson1,
Harshil Patel2, Marie-Charlotte Domart3, Stuart Horswell2, Ok-Ryul Song4, Ming Jiang4,
Margaret Crawford5, Minh Bui6, Yamini Dalal6, Paola Scaffidi1,*
1Cancer Epigenetics Laboratory, Francis Crick Institute, London, NW1 1AT, UK
2Bioinformatics and Biostatistics, Francis Crick Institute, London, NW1 1AT, UK
3Electron Microscopy, Francis Crick Institute, London, NW1 1AT, UK
4High Throughput Screening, Francis Crick Institute, London, NW1 1AT, UK
5Advanced Sequencing, Francis Crick Institute, London, NW1 1AT, UK
6Center for Cancer Research, National Cancer Institute, National Institutes of Health, Bethesda,
MD, 20892, USA
Abstract
Rewiring of cellular programs in malignant cells generates cancer-specific vulnerabilities. Here,
using an unbiased screening strategy aimed at identifying non-essential genes required by tumor
cells to sustain unlimited proliferative capacity, we identify the Male-Specific Lethal (MSL)
acetyltransferase complex as a vulnerability of genetically unstable cancers. We find that
disruption of the MSL complex and consequent loss of the associated H4K16ac mark do not
substantially alter transcriptional programs, but compromise chromosome integrity and promote
chromosomal instability (CIN) that progressively exhausts the proliferative potential of cancer
cells through a p53-independent mechanism. This effect is dependent on pre-existing genomic
instability and normal cells are insensitive to MSL disruption. Using cell- and patient-derived
xenografts from multiple cancer types, we show that excessive CIN induced by MSL disruption
inhibits tumor maintenance. Our findings suggest that targeting of MSL may be a valuable means
to increase CIN beyond the level tolerated by cancer cells without inducing severe adverse effects
in normal tissues.
Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research,
subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms
*Correspondence to: Paola.Scaffidi@crick.ac.uk.
Author Contributions Statement
JM performed most of the experiments and analyses, with help from CMT and PS. LR, TSW and MJ generated Cas9-expressing cell
lines. HP performed NGS analysis of the CRISPR-KO screens and RNA-seq. MCD performed scanning electron microscopy. SH
performed karyotyping analysis. OS performed high-content microscopy analysis. MC performed low-pass genome sequencing. MB
analyzed chromatin fibers under the supervision of YD. PS conceived and supervised the study and wrote the manuscript with input
from other authors.
Competing Insterests Statement
The authors have no competing interests.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 2
During cancer development, cells acquire a range of biological properties that allow them to
initiate and maintain a growing tumor. Establishment and maintenance of malignant
phenotypes require rewiring of cellular programs, which creates cancer-specific
dependencies that can be exploited for therapeutic purposes1. Unbiased identification of
cancer dependencies has typically relied on drop-out viability screening employing pooled
lentiviral libraries1. This approach identifies genes essential for cell survival or cell cycle
progression and, in combination with suitable counter-screens, can reveal cancer-specific,
driver-specific2, 3, or cancer-type-specific4 dependencies. However, viability-based read-outs
cannot identify non-essential proteins that cancer cells depend on to maintain unlimited
proliferative capacity, a key cellular property underpinning disease maintenance, which is
mechanistically distinct from cell cycle progression 5–8.
Here, we devised a strategy to identify new cancer-specific dependencies combining in vitro
CRISPR-Cas9 screening to assess long-term proliferative capacity of malignant cells and in
vivo tumor maintenance assays. Given the therapeutic potential of epigenetic regulators,
their broad expression patterns across cancer types and their role in regulating cellular states
9, 10, we focused our search for dependencies on chromatin and DNA modifiers. We report
that malignant cells from various cancer types require a functional MSL complex to
maintain unlimited proliferative potential, and that MSL disruption inhibits tumor
maintenance. Surprisingly, this inhibitory effect is not mediated by changes in cellular
differentiation programs, but by the accumulation of chromosomal abnormalities that
progressively exhaust cells’ proliferative potential. Since MSL disruption has deleterious
effects only in cells with a basal level of genomic instability, normal cells are unaffected,
making MSL a specific vulnerability of chromosomally unstable cancers.
Results
A strategy to assess cancer cells’ proliferative potential
Within individual cancers, only subsets of cells can proliferate indefinitely and maintain
tumor growth11–15. Because of the challenges associated with isolating these cells from
clinically-derived samples and using them for large-scale screening, we opted to begin our
investigation using a well-characterized and tractable experimental system and subsequently
validate our findings using patient-derived xenograft models of multiple cancer types. We
have previously shown that xenografts generated by human de novo transformed dermal
fibroblasts (TDF) are maintained by a small subset of cells (1-5% of the tumor cell
population) characterized by a primitive phenotype and unlimited proliferative potential
(Extended Fig. 1a) 16, 17. The tumor-maintaining cells are marked by the surface antigen
Stage Specific Embryonic Antigen 1 (SSEA1), which allows their isolation and
characterization (Extended Fig. 1a) 16. TDF xenografts recapitulate features of
hierarchically-organized tumors from patients and have enabled the identification of
epigenetic mechanisms relevant for numerous cancer types 16–19.
To comprehensively identify dependencies of tumor-maintaining cells on epigenetic
regulators, we designed the CRISPR-Cas9 screen such that we could identify two distinct
sets of proteins: (i) factors whose loss results in death or immediate cycle arrest of tumor-
maintaining cells, excluding non-specific hits based on a counter-screen performed using an
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 3
isogenic, non-tumorigenic cell line (viability arm); (ii) proteins whose knock-out inhibit cell
long-term proliferative capacity (unlimited proliferation arm) (Fig. 1a). Whereas reduced
fitness within the population of transduced cells enables easy detection of the first class of
hits, the unlimited proliferation arm required the development of a more complex assay
based on combined phenotypic and functional readouts. In addition to monitoring SSEA1
expression, we also engineered TDF cells such that they express a fluorescent reporter when
they lose long-term proliferative capacity (Fig. 1a). To this end, we introduced the GFP
coding region in the 3’untranslated region (UTR) of DCN (Extended Fig. 1b,c), a gene
previously found to be lowly expressed in SSEA1+ cells, which undergoes a 15-fold
upregulation in SSEA1- tumor bulk cells characterized by limited proliferative capacity 16
(Extended Fig. 1d). Treatment of the engineered TDF cells with quisinostat, a histone
deacetylase inhibitor that drives cancer cell differentiation19, induced GFP expression,
showing that the fluorescent reporter responds to differentiation cues (Extended Fig. 1e). We
then analyzed TDF-induced tumors and observed that SSEA1- tumor bulk cells showed the
expected increase in fluorescent GFP signal, indicating correct regulation of the knocked-in
DCN-GFP allele in vivo (Extended Fig. 1f,g). Furthermore, transplantation assays for
secondary tumor formation showed a reduced tumorigenic potential for GFP+ tumor cells
compared with SSEA1+ cells, functionally validating the fluorescent reporter in vivo and
indicating that the two phenotypic markers distinguish tumor cell subpopulations with
distinct proliferative potential (Extended Fig. 1f,h). Although useful for enrichment of cells
that have lost unlimited proliferative capacity, we reasoned that selection based purely on
marker expression would yield many false positive hits since epigenetic modifiers targeted in
the screen are involved in transcriptional regulation. We thus combined a functional readout
based on clonogenic assays, a standard means to functionally assess cancer cell long-term
proliferative capacity in vitro and predict tumorigenicity in vivo 20, and searched for
sgRNAs that induced GFP expression and deprived cells of clonogenic ability (Fig. 1a).
As a positive control for the screen, knock-out of HRASV12, the oncogenic driver in TDF
cells, resulted in a 4-fold increase in the expression of the DCN-GFP reporter, a 16-fold
reduction in clonogenic ability and impaired tumorigenic potential (Extended Fig. 1i-k).
These effects were not a consequence of reduced cell viability, confirming that the different
screen readouts detect distinct consequences of gene knock-out on cell survival and
proliferative potential (Extended Fig. 1l). To efficiently knock-out chromatin and DNA
modifiers, we employed a previously characterized, focused sgRNA library21 that targets
3,759 nuclear genes, including 346 epigenetic regulators, with up to 10 guides per gene
(median number of sgRNAs per gene: 7) (Supplementary Table 1). The library also
contained negative controls (39 non-targeting guides), and two distinct sets of positive
controls (sgRNAs targeting 83 ribosomal genes, to assess screen saturation, and 3 HRAS-
targeting sgRNAs) (Supplementary Table 1). To be able to temporally control KO induction,
we introduced a doxycycline-inducible Cas9 in TDF cells.
We performed the screen in duplicate, favoring transduction of individual sgRNAs in each
cell. Upon selection of transduced cells (T population), gene knock-out was induced and
0
cells grown for 14 days (T population). In parallel, an isogenic control cell line not
14
expressing HRASV12, which is not clonogenic and does not induce tumor formation in vivo
16, was used for a viability counter-screen to exclude non-specific hits (Fig. 1a). At day 14,
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 4
half of the cell population was harvested for the viability arm, and the remaining cells were
used for the unlimited proliferation arm following the strategy indicated above. sgRNAs
were amplified from the cell population at various time points during the selection process
and sequenced by next-generation sequencing (NGS) (Fig. 1a). Assessment of controls
indicated highly consistent biological replicates at T (Extended Fig. 2a) (r = 0.93, p-value
14 s
< 0.0001), efficient depletion of ribosomal genes (89% ± 1.26% depleted genes) and other
essential genes such as POLR2A (Extended Fig. 2b,c and Fig. 1b), absence of non-targeting
sgRNAs in the depleted set (Fig. 1b, Extended Fig. 2b) and depletion of the positive HRAS
control in the unlimited proliferation arm (Fig. 1c). Overall, the viability arm identified 290
essential genes, 180 of which were also found in the counter-screen, leaving 110 hits
specific to the tumor-maintaining cells (Fig. 1d, Extended Fig. 2d,e, Supplementary Table
2). An additional 181 genes were identified through the unlimited proliferation arm (Fig.
1c,d and Extended Fig. 2e, Supplementary Table 2). Among the 291 specific hits, 19 have
been implicated in nuclear processes involving chromatin or DNA modifications (Fig. 1d,
Supplementary Table 2).
Broad and cancer-specific dependency on the MSL complex
Inspection of the epigenetic-related hits revealed the presence of 3 out of 4 subunits of the
acetyltransferase complex Male-Specific Lethal (MSL) 22 (p-value of the enrichment: 2.8 ×
10-5, hypergeometric test): KAT8 from the viability arm, MSL1 and MSL2 from the
unlimited proliferation arm (Fig. 1b,c). To validate the results of the screen, we performed
tumor maintenance assays in which we injected TDF cells containing inducible Cas9 and
sgRNAs targeting the three genes in NOD.Cg-Prkdcscid Il2rgtm1Wjl/SzJ (NSG) mice,
induced gene KO in vivo in established tumors in half of the animals, and compared the
growth rate of induced and uninduced tumors for each gene (Fig. 1e,f and Extended Fig. 3a).
Knock-out of KAT8, MSL1 and MSL2 using sgRNAs distinct from those used in the screen
significantly impaired tumor growth, while knock-out of the GFP reporter, as a control, had
no effect, confirming reliable identification of genes important for tumor maintenance (Fig.
1f, Extended Fig. 3a).
The MSL complex plays a key role in dosage compensation in Drosophila melanogaster,
where it mediates chromosome-wide gene upregulation on the X chromosome in male flies
through deposition of histone H4K16ac, a major driver of chromatin decondensation22, 23.
Although its molecular function and residue specificity are conserved in mammals, little is
known about the physiological role of the complex in mammalian cells, where dosage
compensation relies instead on gene silencing in females24. The mammalian MSL complex
is ubiquitously expressed and acts as a homotetramer composed of four subunits with
distinct molecular functions: the scaffold protein MSL1, the ubiquitin-ligase MSL2, the
H4K20me-binding protein MSL3, and the acetyltransferase KAT8 (Fig. 1g). KAT8 is also
part of the Non-Specific Lethal (NSL) complex that regulates expression of housekeeping
genes, and interference with this subunit affects both complexes, preventing dissection of the
specific role of MSL25, 26. In line with a role for MSL in sustaining cancer cell long-term
proliferative potential, we were unable to derive and maintain knock-out monoclonal cell
lines for any of the complex subunits. To overcome this issue, we introduced MSL-targeting
sgRNAs in TDF cells expressing inducible Cas9 to be able to acutely knock-out the genes
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 5
upon doxycycline treatment. All subsequent experiments thus employed polyclonal
populations in which the percentage of edited cells ranged from ~70% to ~90% (Extended
Fig. 3b). As expected, knock-out of each subunit resulted in loss-of-function of the MSL
complex (MSLLOF) and widespread loss of H4K16ac within the population (Fig. 2a). Low
H4K16ac levels were also observed upon generation of mutants of MSL subunits lacking
specific domains, confirming that a fully functional MSL complex is required to maintain
homeostatic levels of the histone marks 22 (Extended Fig. 3c,d, Supplementary Table 3).
Despite efficient gene editing, a minority of cells escaping knock-out and maintaining high
H4K16ac levels were present in all edited populations and their relative abundance increased
over time (Extended Fig. 3e,f). While supporting a role of the complex in preserving cell
long-term proliferative capacity, the negative selection of MSLLOF cells creates an
experimental challenge as it limits the time frame suitable for functional assays and leads to
an underestimation of the full effect of MSL disruption. The optimal temporal window
allowing MSLLOF cells to manifest proliferation defects prior to being substantially depleted
was between 14 and 21 days after knock-out.
In agreement with the screen results, KAT8 knock-out led to cell death, due to the
simultaneous disruption of both MSL and NSL complexes (Extended Fig. 4 a-c), whereas
inactivation of MSL-specific subunits did not affect cell survival but impaired the
proliferative capacity of cells, as assessed by limiting dilution clonogenic assays (Extended
Fig. 4d,e). To further characterize how disruption of the MSL complex affects tumor cells in
vivo, we repeated the tumor maintenance assays and harvested tumors 4 weeks after knock-
out induction (Fig. 2b). Sequencing of genomic DNA revealed that 11 out of 24 tumors did
not show substantial editing of the targeted MSL genes, indicating that they mainly
contained cells that escaped gene knock-out (Extended Fig. 3g). We therefore selected edited
tumors in which MSL loss-of-function (MSLLOF) had been achieved and assessed their
tumor organization, comparing them with unedited tumors used as controls. As expected,
flow cytometry analysis showed that MSL disruption resulted in a significant decrease in the
fraction of SSEA1+ cells and a concomitant increase in the percentage of cells expressing
the GFP reporter (Fig. 2c,d). In agreement, edited tumors contained 5-fold fewer cells
endowed with unlimited proliferative potential, as assessed by limiting dilution
transplantation assays for secondary tumor formation (Fig. 2e, Extended Fig. 4f). To validate
these findings in clinically-relevant samples, we disrupted the MSL complex in patient-
derived xenografts (PDX) from two different cancer types characterized by altered H4K16ac
patterns: gastric and pancreatic cancer27, 28, selecting models that shared the same genetic
drivers as TDF-induced xenografts (activating RAS mutations and inactivating TP53
mutations, see Supplementary Table 4). As observed in TDF-induced xenografts, disruption
of the MSL complex inhibited tumor growth in both PDXs (Fig. 2f). Limiting dilution
clonogenic assays showed impaired proliferative capacity of MSLLOF cells from various
other cancer types, including melanoma, breast cancer and osteosarcoma (Fig. 2g). HT-1080
fibrosarcoma cells, a p53-proficient, genetically stable line did not show a significant
inhibition of clonogenic ability, suggesting that high levels of genetic instability may
sensitize cells to MSL loss-of-function (Fig. 2g). As a more sensitive readout of proliferation
defects, negative selection of H4K16aclow cells over time indicated that despite a reduced
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 6
sensitivity compared with genetically unstable lines, HT-1080 cells were also affected by
MSL disruption (Extended Fig. 4g,h).
The observation that MSL components were not identified as hits in the counter-screen
performed using a non-transformed isogenic line suggests that cancer cells may be
specifically dependent on MSL to preserve long-term proliferative potential. To further
examine this, we disrupted the complex in an independent non-cancerous cell line:
telomerase-immortalized normal mammary epithelial cells (HME1). Consistent with the
counter-screen results, normal HME1 cells did not show impaired proliferative potential
upon MSL disruption and clones of MSLLOF cells could be readily isolated and maintained
(Fig. 2g,h). This observation is in line with the findings that Msl1-deficient ESCs have
unaffected self-renewal ability29 and that Msl3-null mice are viable and do not display overt
defects30, indicating that the MSL complex is largely dispensable for normal organismal
function (Extended Fig. 4i, Supplementary Table 5). Altogether, these results indicate that a
functional MSL complex is required to sustain tumor maintenance in various cancer types
and that disruption of the complex impairs the ability of cells to proliferate indefinitely.
Since many analyzed tumor models lack a functional p53, the effect of MSL disruption does
not rely on p53-dependent tumor suppressive pathways 31. The dependency on MSL is
specific to cancer cells and normal cells preserve long-term proliferative capacity in the
absence of a functional complex.
MSL loss induces genomic, not transcriptional, abnormalities
To understand how disruption of the MSL complex impairs cancer cell long-term
proliferative potential, we performed transcriptional profiling of TDF cells in which the
three MSL-specific subunits were knocked-out and compared them to two controls: wild-
type TDF cells (WT) and cntr-KO cells, in which the GFP reporter was targeted, controlling
for possible CRISPR-induced non-specific effects (Fig. 3a). We found 314 differentially
expressed genes (DEGs) in MSLLOF cells (False discovery rate (FDR) q-value ≤ 0.01,
maximum transcripts per million (TPM) > 1), showing only moderate fold changes (FC)
(median log FC: 0.31 and -0.42 for upregulated and downregulated genes, respectively)
2
(Fig. 3a, Supplementary Table 6). Surprisingly, considering the genome-wide accumulation
of H4K16ac at active promoters and enhancers32, gene set enrichment analysis (GSEA)33
did not show major alterations in specific biological processes or cancer-related pathways,
suggesting that MSL disruption, and consequent loss of the mark did not trigger substantial
changes in gene expression programs (Fig. 3b and Supplementary Table 7). In particular, we
did not detect transcriptional changes consistent with cell differentiation, a biological
process often associated with loss of unlimited proliferative potential within tumors 10
(Supplementary Table 7). However, GSEA revealed enrichment of 21 positional gene sets
(FDR q-value < 0.01), indicating that neighboring genes on chromosomes showed
concordant changes in mRNA levels upon MSL disruption (Fig. 3b,c and Supplementary
Table 7). We thus examined whether the detected changes in mRNA levels were due to
underlying differences in DNA content in MSLLOF cells, and performed low-pass whole
genome sequencing to identify possible copy number alterations. MSLLOF cells were highly
aneuploid (Extended Fig. 5a) and displayed several genomic alterations compared to both
WT and cntr-KO cells (Fig. 3d and Supplementary Table 8). Importantly, DNA changes in
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 7
MSLLOF cells correlated with the detected mRNA changes, with 13 out of 21 positional
gene sets identified by GSEA showing consistent DNA copy number changes, and
chromosomes displaying similar large-scale alterations in DNA and mRNA levels (Extended
Fig. 5b and Fig. 3e). Thus, the apparent gene upregulation and downregulation detected by
RNA-seq analysis in fact reflected increased aneuploidy in MSL-disrupted cells. Karyotype
abnormalities of MSLLOF cells were confirmed by analysis of chromosome spreads. As
expected, due to p53 inactivation in TDF cells, WT and cntr-KO cells displayed a basal level
of aneuploidy, with cells containing between 15 and 83 chromosomes (median: 64), but
MSLLOF cells showed additional numerical abnormalities and an overall increase in
chromosome number (median: 69) (Fig. 3f).
Aneuploidy is the product of chromosomal instability (CIN)34. We therefore examined
whether MSL-disrupted cells displayed an increased rate of mitotic defects and chromosome
mis-segregation. Both in TDF cells and in cells derived from the pancreatic, gastric and
melanoma PDXs, MSL disruption resulted in significantly increased frequency of cells
containing micronuclei and mitotic divisions displaying lagging chromosomes or anaphase
bridges, established hallmarks of CIN34 (Fig. 3g). As expected, the p53-deficient PDX
samples showed a basal level of CIN similarly to TDF cells. As a control, a low frequency of
micronuclei-containing cells was observed in non-cancerous HME1 cells, which did not
increase upon MSL disruption (Fig. 3g). To confirm these findings with a complimentary
approach, we induced MSL loss-of-function in a CIN reporter cell line that allows
quantification of CIN through detection of a GFP-encoding human artificial chromosome
(HAC)35 (Fig. 3h). MSLLOF cells showed increased rate of HAC loss, regardless of which
MSL-specific subunit was targeted, confirming enhanced CIN (Fig. 3i). We conclude that
MSL disruption impairs the fidelity of chromosome segregation during cell division, and
increases the rate of mitotic defects in cancer cells.
Accumulation of ssDNA promoting chromosome fragility
To dissect how disruption of the MSL complex leads to CIN we first analyzed the content of
micronuclei (MN), assessing for centromere presence, indicative of whole chromosome mis-
segregation, or γH2AX, indicative of damaged chromosomes. We found that 14% ± 4% of
MN in MSLLOF cells contained centromeric regions, indicating relatively infrequent
presence of whole chromosomes. In contrast, 70% ± 5% were marked by γH2AX,
suggesting compromised genome integrity as a major cause of MN formation (Fig. 4a,b,
Extended Fig. 6a). In agreement, chromosome fragments and broken chromatids were
enriched in metaphase spreads from MSLLOF cells (Fig. 4c,d). γH2AX-marked MN did not
contain active components of the double-strand break response pathway, such as 53BP1 and
phosphorylated ATM36 (Extended Fig. 6b,c), but were often marked by phosphorylated
Replication Protein A (pRPA), a major single-stranded DNA (ssDNA) sensor (68% of
γH2AX-marked MN, N: 213), and its downstream effector phosphorylated Checkpoint
Kinase 1 (pCHK1)36, suggesting the presence of ssDNA in MN (Fig. 4a, Extended Fig. 6d).
In agreement, DAPI intensity was significantly lower in MN than in nuclei (Extended Fig.
6e). pRPA and pCHK1 foci were also found at high frequency within nuclei, a pattern
consistent with widespread replication defects36, with foci as big as one tenth of the nuclear
area (Fig. 4e,f, Extended Fig. 6f,g). Increased frequency of pRPA-foci was also observed in
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 8
all other cancer models that had shown a dependency on MSL (Fig. 4f). To confirm that
MSL disruption increases the endogenous level of replication stress we treated TDF cells
with the DNA polymerase inhibitor aphidicolin, and indeed observed hypersensitivity of
MSLLOF cells to the drug (Fig. 4g). As a control, non-cancerous HME1 cells characterized
by low replication stress were more resistant to aphidicolin treatment (Extended Fig. 6h).
Importantly, while HME were insensitive to MSL disruption under normal growth
conditions (Fig. 2g, Fig. 4h), induction of replication stress impaired the growth of MSLLOF
cells over five days, suggesting that basal levels of genomic stress critically sensitize cells to
the loss of MSL function (Fig. 4h, Extended Fig. 6h). In line with the notion that under-
replicated DNA can escape the G2/M checkpoint and interfere with chromosome
segregation37, γH2AX- and pRPA-marked regions were also detected in mitotic cells (Fig.
4i-l), with large DNA regions characterized by low DAPI intensity being strongly stained
(Fig. 4i) and γH2AX foci marking anaphase bridges and chromatids with compromised
integrity (Fig. 4j,l). Given the key role of H4K16ac in chromatin decondensation, a pre-
requisite for efficient DNA replication23, 38, these findings suggest that MSL loss-of-
function and consequent loss of the histone mark promote CIN by leading to an
accumulation of under-replicated DNA that cannot be properly segregated during mitosis.
Mis-segregation of whole chromosomes in MSL-disrupted cells
Although clastogenic events appear to be the main source of CIN in MSLLOF cells, the
numerical abnormalities detected in MSLLOF cells suggests that cells may also suffer whole-
chromosome mis-segregation. In agreement, MSLLOF TDF cells displayed prolonged
mitosis compared to both wild-type and cntr-KO cells, with cell divisions lasting up to 2.5
hours (Fig. 5a,b and Supplementary videos 1 and 2). In particular, complete alignment of
chromosomes required up to 120 min and unattached chromosomes could often be detected
(Fig. 5a, Supplementary videos 3 and 4). Similar defects were also observed in PDX-derived
cells (Fig. 5b). This delay in mitotic progression was not due to alterations in the spindle
assembly checkpoint (SAC), as shown by unaffected expression of the SAC components39
and by the ability of cells to efficiently arrest in metaphase upon nocodazole treatment (Fig.
5c,d). Analysis of chromosome ultrastructure by scanning electron microscopy revealed that
H4K16ac-depleted chromosomes, as expected, were more compacted than control ones, but
these structural abnormalities did not result in altered centromeric chromatin (Fig. 5e,f). We
then asked whether accumulation of under-replicated DNA may interfere with chromosome
alignment. Indeed, mitotic MSLLOF cells displayed unaligned chromosomes marked by
strong γH2AX staining and containing a single centromere (Fig. 5g), and interphase cells
showed an increased frequency of micronuclei positive for both centromere and γH2AX
staining, likely containing under-replicated whole chromosomes (Fig. 5h,i). All together,
these observations support the notion that replication stress and whole-chromosome mis-
segregation may be mechanistically linked37, 40, 41 and suggest that accumulation of ssDNA
induced by MSL disruption promotes both structural and numerical CIN.
Enhanced CIN exhausts cells’ proliferative capacity
The observations that MSL disruption increases the rate of chromosome mis-segregation
suggests that a fitness cost associated with excessive CIN may underlie the loss of unlimited
proliferative potential in MSL-deficient cells. Although CIN is overall beneficial for tumors,
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 9
as it generates cellular diversity that promotes cancer evolution, abnormal chromosome
content is often deleterious at the individual-cell level42–44. Cancer cells, especially in the
absence of functional p53, can tolerate aneuploidy, but high CIN levels generate broad
cellular stress, including genotoxic, proteotoxic, metabolic and osmotic stress42–44. We
therefore examined whether the proliferative potential of individual MSL-disrupted cells
correlated with their CIN level. To do so, we grew clonal populations over 14 days and used
DNA fluorescence in situ hybridization (FISH) to visualize five chromosomes (Chr.3, Chr. 7,
Chr. 11, Chr. 12 and Chr. 17). For each clone, we quantified the number of cells and a CIN
score based on the heterogeneity in chromosome content across cells (see Methods). As
expected, MSLLOF clones were smaller than WT and cntr-KO clones (p-value < 0.0001)
(Fig. 6a, Extended Fig. 6i). Furthermore, confirming increased CIN, MSLLOF clones were
highly heterogeneous with respect to chromosome copy numbers, leading to significantly
higher CIN scores (p-value < 0.0001) (Fig. 6b,c). Importantly, CIN score and clone size
showed an inverse relationship, with clones characterized by high CIN containing
significantly less cells than more stable clones, linking MSL-disruption, increased CIN and
impaired long-term proliferative potential of cancer cells (Fig. 6d). To establish a causal link
between enhanced CIN and impaired proliferative capacity, we treated TDF cells with
reversine, an inhibitor of the mitotic kinase MSP1 that induces chromosome mis-
segregation45, and performed clonogenic assays. Reversine-treated cells grew over 12 days
but progressively exited the cell cycle, as indicated by loss of Ki67 staining, and formed
significantly smaller clones compared to DMSO-treated cells, phenocoping MSL genetic
disruption and confirming that excessive CIN is overall detrimental to cancer cells (Fig. 6e-
j). Reversine treatment also phenocopied MSL disruption in vivo, significantly delaying
tumor development compared with control tumors (Fig. 6k, p = 0.009). To finally examine
the relationship between enhanced CIN and cell differentiation state, we performed a similar
analysis using HCC1569 breast cancer cells, whose differentiation state can be assessed by
quantifying the phenotypic markers CD24 and CD4446. Although reversine impaired the
cells’ proliferative capacity, no change was observed in the markers, while the expected
increase in CD24+ cells was observed when cells were treated with quisinostat, which
induces cell differentiation19 (Fig. 6j,l). All together, these results show that excessive CIN
induced by disruption of the MSL complex exhausts the proliferative capacity of cancer cells
by compromising their fitness over multiple cell divisions, without affecting their
differentiation state (Fig. 6m).
Discussion
We show here that disruption of the MSL complex and consequent loss of H4K16ac, a major
driver of chromatin decondensation23, impair the proliferative capacity of malignant cells
from various cancer types. Surprisingly, this effect is not mediated by transcriptional
changes and activation of a differentiation program, but rather by the accumulation of
chromosomal abnormalities and aneuploidy that are progressively detrimental to cellular
fitness. Increasing evidence from the analysis of both clinical samples and experimental
systems suggests that the extent of CIN in cancer cells determines its tumor-promoting or
tumor-suppressive functional output44. While moderate CIN levels fuel cancer evolution,
high CIN levels are deleterious for tumor cells and correlate with good outcome in various
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 10
cancer types44. Based on these observations, strategies aimed at exacerbating CIN for
therapeutic purposes have been explored44. Although inhibition of mitotic checkpoints
effectively induces CIN39, 47, the clinical usefulness of this approach is limited by the severe
adverse effects on tissue homeostasis, as highly proliferative normal cells are also sensitive
to the treatment48–51. We find that the sensitivity to MSL loss-of-function depends on pre-
existing genetic instability and that non-cancerous cells preserve long-term proliferative
potential upon disruption of the complex. In agreement with our findings, Msl1-deficient
mouse embryonic stem cells display normal self-renewal ability29 and Msl3-null mice are
viable and do not display overt defects30. Owing to the selective effect of MSL disruption on
malignant cells, inhibition of MSL function may be a well-tolerated means to induce
extreme CIN in unstable cancer cells and deprive them of long-term proliferative capacity.
In agreement with observations made in Drosophila22, we find that a fully functional MSL
complex is required to maintain homeostatic levels of H4K16ac levels, offering multiple
opportunities for pharmacological targeting. Extensive characterization of the complex at the
biochemical and structural levels22, 52, 53 aids the development of targeting strategies, which
may include interference with protein-protein interactions among complex subunits, binding
to chromatin and DNA mediated by MSL3, or the ubiquitin-ligase activity of MSL2.
Targeting of KAT8’s acetyltransferase activity is complicated by the simultaneous effect that
such a strategy would have on the NSL complex, which contributes to the regulation of
housekeeping genes25, 26. Nevertheless, encouraging results obtained recently with
inhibitors targeting the related MYST acetyltransferases KAT6A/B and KAT754, 55 suggest
that despite the general role of these proteins in sustaining cellular homeostasis, there may
me a therapeutic window in cancer.
In addition to revealing MSL as a cancer-specific vulnerability relevant for various cancer
types, our findings also suggest that accumulation of genomic abnormalities during cancer
growth may be a differentiation-independent mechanism that generates non-self-renewing
cells within tumors. We show that absence of long-term proliferative potential detected by
standard self-renewal assays – clonogenic and limiting dilution transplantation assays - does
not necessarily imply a differentiated phenotype and could reflect compromised cell fitness.
These observations indicate that results from self-renewal assays may need to be cautiously
interpreted in the absence of molecular evidence of differentiation, especially when
analyzing solid tumors, which are often characterized by genetic instability.
Methods
Generation of the DCN-GFP reporter cell line
Transformed dermal fibroblasts (TDF) and the isogenic non-tumorigenic line lacking
HRASV12 (DF)16 were grown as indicated in Supplementary Table 9. To generate the
fluorescent reporter cell line expressing DCN-GFP, 4 different plasmids were obtained from
GenScript: pcDNA3.3-Cas9 for Cas9 expression, pCR Blunt II TOPO-sgRNA1 and 2
against DCN’s 3’UTR (Supplementary Table 10) and pUC57-DCN-GFP donor plasmid to
be used for homologous recombination. The donor plasmid contained an IRES (sequence as
in Addgene 64784), followed by the GFP coding sequence, and two 800 bp flanking regions
homologous to the DCN 3’UTR (chr12:91539008-91539807 and
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 11
chr12:91539808-91540607). The donor plasmid harbored point-mutations in the sequence of
the sgRNAs used for CRISPR-mediated editing to prevent re-editing of the integrated
cassette (Supplementary Table 10). Six million non-tumorigenic DF cells, which express 15
times higher DCN levels compared to TDF cells, were electroporated with the four plasmids
(5 μg each, with the donor plasmid linearized with NdeI [NEB R0111S] to increase editing
efficiency). Six days after transfection, GFP+ cells were sorted into individual wells of 96-
well plates to isolate clonal populations. Individual clones were screened for correct editing
by PCR and gel electrophoresis using primers specific to the knocked-in allele
(Supplementary Table 11). The selected clone (Cl. C3) was then transduced with pBabe-
HRASV12 as previously described16 to generate TDF cells containing the knocked-in
fluorescent reporter sequence. As expected, transformation induced downregulation of the
reporter, leading to undetectable GFP levels in TDF cells. Dox-inducible 3xFLAG-Cas9 was
finally introduced in the reporter TDF cell line by transducing cells with a modified pCW-
HygroCas9 vector (Addgene 50661) in which the sequence encoding resistance to
puromycin had been replaced with the sequence encoding resistance to hygromycin B
(Supplementary Table 11). Individual clones were isolated and a clone with minimal
leakiness and high expression levels upon induction with 1 μg/mL Doxycycline (Sigma
D9891) was selected for use in the screen (Cl.14). In a similar way, inducible Cas9 was
introduced in the DF reporter line and the resulting clone (Cl. L) was used for the counter-
screen.
sgRNA library quality control and generation of positive and negative control sgRNAs
The sgRNA library (33,829 guides) targeting 3,759 nuclear genes was obtained from
Addgene21 and propagated by transforming highly-competent Stbl3 cells (Thermo Fisher
C737303) ensuring at least 100 times coverage of the library complexity. Sequencing of the
library, as described below, revealed the presence of other sgRNAs in addition to those
belonging to the nuclear pool. These included sgRNAs targeting ribosomal genes and 5,692
sgRNAs from other pools of the genome-wide library21 (Supplementary Table 1).
Furthermore, non-targeting sgRNA controls (NTC) were underrepresented (only 9 out of
100 were detected). We therefore selected 30 NTC sequences from the non-targeting sgRNA
subpool from the original published library, cloned them into the pLX-sgRNA backbone
(Addgene 50662) as previously described21 (https://media.addgene.org/data/08/61/
acb3ad96-8db6-11e3-8f62-000c298a5150.pdf) and added them to the library obtained from
Addgene at an equimolar ratio. Similarly, three positive control sgRNAs were designed
using the CRISPR MIT Designer tool (crispr.mit.edu) against HRAS, cloned in the lentiviral
vector and added to the library.
Virus generation and titer estimation for the screen
Virus production was performed by transfecting 80% confluent HEK-293T cells, grown as
described in Supplementary Table 9, with pLenti- or pLX-sgRNAs21, 57 (Supplementary
Table 10), pCW-HygroCas9 (Addgene 50661) or H2B-mCherry (Addgene 20972) alongside
packaging plasmids (psPax2 and pMD2.G, Addgene 12260 and 12259, respectively). Viral
particles were used to infect cells with 5 μg/mL Polybrene (Santa Cruz sc-134220).
Transduced cells were selected with the appropriate antibiotic for 5 d to eliminate non-
infected cells (DF and TDF cells: 6 μg/mL Blasticidin S, Calbiochem 203350; 100 μg/mL
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 12
Hygromycin B, Thermo Fisher 10687010. HME1 and PDX-derived cells: 5 μg/mL
Blasticidin S [GXA 3067 and MEXF 2090] or 7.5 μg/mL [PAXF 1997], Calbiochem
203350; 100 μg/mL Hygromycin B, Thermo Fisher 10687010). To ensure that cells were
transduced with individual sgRNAs in the screens, the library viral titer was estimated by
infection of 100,000 cells with decreasing viral concentrations and selection with Blasticidin
S for 5 d. The percentage of surviving cells following selection relative to a non-selected
control was used as a measure of infection efficiency. A viral dilution yielding an infection
efficiency of 30% equivalent to a Multiplicity Of Infection (MOI) of 0.3 was used for the
screens.
CRISPR-Cas9 screen, counter-screen and assessment of sgRNA abundance
The screen was performed in duplicate, favoring transduction of individual sgRNAs in each
cell (multiplicity of infection: ~ 0.3) and ensuring that at least 1,000-fold coverage of the
library complexity was maintained at each step. One-hundred and twenty-six million TDF
cells (main screen) or DF cells (counter-screen) were transduced with the sgRNA library and
selected with 6 μg/mL Blasticidin S (Calbiochem 203350) for 5 d. A sample of 50 million
cells was isolated for use as T population. Subsequently, Cas9 expression and gene KO was
0
induced through continued administration of 1 μg/mL Dox for 14 d for TDF cells, or 24 d
for the slower cycling DF cells to equalize population doublings, at which stage 50 million
cells were isolated as end-point for the viability arm of the screen and counter-screen (T
14
and T , respectively). A further 50 million TDF cells were stained with an eFluor 660-
24
conjugated anti-SSEA1 antibody (eBioscience 50-8813-42) and analyzed by flow cytometry
(see protein immunodetection section) to isolate SSEA1-/GFP+ cells by cell sorting in the
unlimited proliferation arm. Sorted cells were grown for 48 h, after which half the
population was harvested for genomic DNA isolation and the other half was plated in semi
solid medium (Generon CBA-155, see clonogenic assay section). Cells were grown for 10 d,
the resulting colonies collected following the manufacturer’s instructions and their genomic
DNA extracted. For all samples, genomic DNA (gDNA) extraction was performed using the
DNeasy Blood & Tissue Kit (Qiagen 69506).
To prepare the sgRNA libraries for NGS, a 2-step nested PCR-based protocol originally
described by Wang et al. was followed21 using primers listed in Supplementary Table 11.
For initial quality control of the sgRNA plasmid library, 5 ng of plasmid DNA were used as
a template and amplified in 3 independent reactions that were pooled prior to sequencing.
For the screen samples, either 85 μg (viability arm, corresponding to ~13 million cells) or all
available gDNA (unlimited proliferation arm) was amplified. To ensure efficient
amplification of the sgRNAs, multiple PCR reactions were run for each sample, using a
maximum of 2 μg gDNA in 100 μl reactions with 20 cycles of amplification. Following the
first PCR, all reactions were pooled and 5 μL were used as template for the second PCR, run
in triplicates for 22-30 cycles. Final products were pooled, run on a 2% agarose gel, excised
and purified using QIAquick gel extraction kit (Qiagen 28706) prior to sequencing. The
libraries were analyzed on a DNA 1000 BioAnalyser 2,100 chip (Agilent) to ensure good
quality, and sequenced on an Illumina HiSeq 4000 platform using custom primers
(Supplementary Table 11) generating ~30-50 million reads per sample. PhiX DNA was
added to the sequencing lanes at 35% to increase read base diversity and enable efficient
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 13
sequencing. Raw sequencing reads were trimmed to 20 bp using cutadapt with the “--cut -
<trim_size>“ parameter to identify the sgRNA sequences. These were then mapped to the
sgRNA library using BWA (version 0.5.9-r16)58 with the parameters “-l 20 -k 2 -n 2”.
sgRNA counts were obtained after de-multiplexing samples based on i7 indexes and
excluding mapped reads with mismatches. To quantify the relative abundance of sgRNAs in
each sample, raw reads for each sgRNA were normalized to the overall read counts.
Hit identification
Viability arm—sgRNAs depleted upon gene knock-out were identified by comparing the
normalized sgRNA counts in the population 14 d after Cas9 induction (T ) and in the initial
14
population (T ). Only sgRNAs with at least 1 raw count in both biological replicates at T
0 0
were used for analysis. Raw reads for each sgRNA were normalized to total read counts for
each sample and the fold change (FC) between T and T calculated for each replicate.
14 0
Depleted sgRNAs showing a log FC ≤ -1 in both biological replicates at T compared to T
2 14 0
were selected. With a similar approach, depleted sgRNAs showing a log FC ≤ -0.6 between
2
T and T in the counter-screen were selected. The different threshold used in the counter-
24 0
screen is to account for the overall lower sgRNA depletion observed when using slower-
cycling DF cells. The log FC ≤ -0.6 threshold was chosen as it resulted in a fraction of
2
depleted ribosomal genes comparable to that observed in the main screen. To robustly
identify genes important for survival and cell cycle progression of tumor-maintaining cells,
multiple filters were applied to exclude: (i) genes with less than 3 depleted sgRNAs; (ii)
lowly expressed genes (TPM ≤ 5), as assessed by RNA-seq; (iii) genes with at least 3
depleted sgRNAs in the counter-screen after FC filtering. Positive and negative controls
were used for quality control purposes and are excluded from hit count and related tables.
Unlimited proliferation arm—Depleted sgRNAs were identified by comparing the
normalized sgRNA counts in cells retrieved from colonies grown in semi-solid medium and
sorted SSEA1-/GFP+ cells. Only sgRNAs with at least 1 raw count in both biological
replicates in the sorted population were used for analysis. Raw reads for each sgRNA were
normalized to total read counts for each sample and the FC between colonies and sorted
cells was calculated for each replicate. Depleted sgRNAs showing a log FC ≤ -4 in both
2
biological replicates in the colonies compared with the sorted population were selected. To
robustly identify genes important for sustaining unlimited proliferative capacity of tumor-
maintaining cells, multiple filters were applied to exclude: (i) genes with less than 2 depleted
sgRNAs; (ii) lowly expressed genes (TPM ≤ 5), as assessed by RNA-seq. Positive and
negative controls were used for quality control purposes and are excluded from hit count and
related tables.
Generation of Cas9-expressing cell lines
Cells were grown as indicated in Supplementary Table 9. For hTERT-immortalized human
mammary epithelial cells (hTERT-HME1, ME16C) (ATCC CRL-4010), the CIN reporter
HAC cells35, and HCC-1569 breast cancer cells (ATCC CRL-2330, obtained from the Crick
Institute common repository), doxycycline-inducible Cas9 was introduced as described for
TDF cells. The CIN reporter line was transduced with a plasmid encoding Puromycin
resistance and was selected with 1 μg/ml puromycin for 5 d. For U2OS osteosarcoma cells
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 14
(ATCC HTB-96, obtained from the Crick Institute common repository), and HT-1080
fibrosarcoma cells (ATCC CCL-121, obtained from the Crick Institute common repository)
doxycycline-inducible Cas9 was knocked-in into the AAVS1 locus using the Genome-
CRISPR Human AAVS1 Safe Harbor Gene Knock-in system (GeneCopoeia plasmids
SH100 (AAVS1 CRISPR-Cas9 clone) and SH304 (AAVS1 Cas9 knock-in donor clone-
TRE3G-Puro). TransIT-X2 (Mirus, MIR 6003) and Fugene HD (Promega E2311)
transfection reagents were used to introduce plasmids into U2OS and HT1080 cells,
respectively, and three days after transfection puromycin was added at concentration of 2
μg/ml for U2OS or 1 μg/ml for HT-1080 to select transfected cells. Individual clones were
isolated and clones with minimal leakiness and high editing activity upon induction with 1
μg/ml doxycycline were selected.
Generation of knock-out and MSL-mutant cell lines
Knock-out lines were generated either by transducing Cas9-expressing cells with lentiviral
constructs expressing sgRNA pools specific to the target genes57 or by transfecting synthetic
guide RNAs (Edit-R crRNA, Horizon) (Supplementary Table 10). pLenti-sgRNA constructs
were generated as previously described57 and transduction and selection performed as
described above. To induce gene KO in the selected population, Cas9 expression was
induced by treatment of cells with 1 μg/mL Doxycycline (Sigma D9891). For transfection of
synthetic guide RNAs, each CRISPR RNA (crRNA) and the trans-activating CRISPR RNA
(tracrRNA) were resuspended in 1x siRNA buffer (Horizon B-002000-UB-100) at a
concentration of 20 μM. Each crRNA was then mixed with an equal amount of tracrRNA
and the mix diluted 1:100 in Optimem. 10 μl of the cr/tracrRNA mix were added to a well of
a 96-well plate (to achieve a final concentration of 20 nM in a 100 μl of final volume) and
mixed with 10 μl of transfection reagent diluted in Optimem (Supplementary Table 9). After
15 min, 4,000 cells resuspended in 80 μl of complete medium containing 1 μg/ml
doxycycline were added to each well. To maximize editing efficiency, cells were pre-treated
with doxycycline for 24 h. The efficiency of knock-out in the populations ranged from 70%
to 95% of cells, as assessed by sequencing of the targeted locus and/or quantification of
H4K16ac by immunofluorescence microscopy. Because of progressive negative selection of
MSLLOF cells in the population, most experiments were performed between 7 and 21 days
after knock-out induction, the optimal temporal window that allowed MSLLOF cells to
manifest proliferation defects prior to being substantially depleted. MSL-mutant lines were
generated using the synthetic guide RNAs indicated in Supplementary Table 10.
Patient-derived xenograft (PDX) models
Information about the GXA 3067, PAXF 1997 and MEXF 2090 PDX models are listed in
Supplementary Table 4. Models were obtained from the Charles Rivers tumor model
compendium https://compendium.criver.com/compendium2/cancertype?
species.name=Human and propagated in NSG mice. Cells derived from each PDX were
grown as indicated in Supplementary Table 9. Doxycycline-inducible Cas9 was introduced
in PDX-derived cells as described above for TDF cells.
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
Monserrat et al. Page 15
Animal studies
Animal studies were subject to ethical review by the Francis Crick Animal Welfare and
Ethical Review Body and regulation by the UK Home Office project license PPL 70/8167
and PC2165EA4. NSG mice were maintained under pathogen-free conditions, and food and
water were provided ad libitum. For generation of primary tumors, 5 × 105 TDF or PDX-
derived cells and 1 × 105 carrier hTERT-immortalized fibroblasts were injected
intradermally in both flanks of 8-10 week-old male NSG mice in 50 μL of PBS. For
validation of the reporter cell line, 1,000 sorted cells and 1 × 105 carrier hTERT-
immortalized fibroblasts were injected. For tumor maintenance experiments, upon
appearance of ~2 × 2 mm tumors, mice were randomly segregated into a +/- Dox treatment
(2 mg/mL Doxycycline in drinking water supplemented with 1% sucrose, or 1% sucrose
alone, changed every 2-3 days) and tumor volume was measured biweekly using electronic
calipers until animals were humanely sacrificed. For experiments directly testing the effect
of CIN on tumor development, TDF cells were treated with DMSO (control) or 250 nM
reversine (Generon, HY-14711-1mL) for 4 days and then injected intradermally into both
flanks of 8-10 week-old female NSG mice (2.5 × 106 cells in 50 μl of sterile PBS). For
generation of secondary tumors in limiting dilution transplantation experiments, 10, 100 or
1,000 cells from dissociated TDF-induced primary tumors were re-injected into the flanks of
new recipient NSG mice together with 1 × 105 non-tumorigenic carrier hTERT-immortalized
fibroblasts in 50 μL of PBS. In experiments comparing unedited and edited tumors induced
by TDF cells containing MSL subunit-targeting sgRNAs, cells from all unedited (< 50%
edited sequence) or edited (> 50% edited sequence) MSL3-KO dissociated primary tumors
were pooled and injected into mice. Tumor appearance was scored over 8 weeks, when mice
were humanely sacrificed. Frequency of tumor-propagating cells in primary tumors was
estimated by limiting dilution analysis using ELDA software (http://bioinf.wehi.edu.au/
software/elda/).
Tumor characterization
For tumor dissociation, subcutaneous tumors were collected, cut into small pieces of ~2-3
mm in diameter with a scalpel, transferred into GentleMacs C tubes (Miltenyi Biotec
130-096-334) containing 3 volumes of RPMI (Gibco 21875034) supplemented with 0.5x
Liberase (Sigma 5401020001), dissociated with the GentleMacs dissociator (Human tumor
1.1 program) and incubated for 30 min in fast agitation at 37 °C. Cells were further
dissociated with the GentleMacs dissociator (Human tumor 2.1 program) and incubated for
30 min at 37 °C with 100 U/mL of DNase I (NEB M0303). Following one last dissociation
step (Human tumor 3.1 program), cells were filtered through a 70 μm cell strainer (Fisher
10788201), washed 3 times with RPMI and viable cells counted. Cells were then used for
flow cytometry analysis or limiting dilution transplantation assays.
For validation of the DCN-GFP reporter cell line, cells from dissociated primary tumors
were stained with an eFluor-660-conjugated anti-SSEA1 antibody (eBioscience 50-8813-42)
and SSEA1+ and GFP+ cells sorted by flow cytometry. One thousand SSEA1+ or GFP+
sorted cells were then injected into both flanks of new recipient NSG mice together with 1 ×
105 non-tumorigenic carrier hTERT-immortalized cells in 50 μL of PBS, and tumor growth
was scored over 4 weeks, when mice were humanely sacrificed.
Nat Cell Biol. Author manuscript; available in PMC 2021 October 09.
Europe
PMC
Funders
Author
Manuscripts
Europe
PMC
Funders
Author
Manuscripts
