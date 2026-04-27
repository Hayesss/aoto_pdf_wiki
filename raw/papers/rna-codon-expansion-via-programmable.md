---
source_path: /mnt/c/Users/Administrator/Zotero/storage/G2MY7VRC/Liu 等 - 2025 - RNA codon expansion via programmable pseudouridine editing and decoding.pdf
ingested: 2026-04-23
sha256: 6a46cc2cb0b89b8f
---

Article
RNA codon expansion via programmable
pseudouridine editing and decoding
https://doi.org/10.1038/s41586-025-09165-x Jiangle Liu1,2,3,11, Xueqing Yan1,11, Hao Wu1,3,11, Ziqin Ji2, Ye Shan2,3, Xinyan Wang4, Yunfan Ran5,
Yichen Ma1,3, Caitao Li6, Yuchao Zhu2,7, Ruichu Gu1,8, Han Wen8,9,10, Chengqi Yi1,2,3,9 ✉ &
Received: 29 April 2024
Peng R. Chen2,3,7 ✉
Accepted: 15 May 2025
Published online: xx xx xxxx
The incorporation of non-canonical amino acids (ncAAs) enables customized chemistry
Check for updates to tailor protein functions1–3. Genetic code expansion offers a general approach for
ncAA encoding by reassigning stop codons as the ‘blank’ codon; however, it is not
completely orthogonal to translation termination for cellular transcripts. Here, to
generate more bona fide blank codons, we developed an RNA codon-expansion (RCE)
strategy that introduces and decodes bioorthogonally assignable pseudouridine (Ψ)
codons (ΨGA, ΨAA or ΨAG) on specified mRNA transcripts to incorporate ncAAs
in mammalian cells. The RCE strategy comprises a programmable guide RNA4, an
engineered decoder tRNA, and aminoacyl-tRNA synthetase. We first developed the
RCE(ΨGA) system, which incorporates functional ncAAs into proteins via the ΨGA
codon, demonstrating a higher translatome-wide and proteomic specificity compared
with the genetic code expansion system. We further expanded our strategy to produce
the RCE(ΨAA) and RCE(ΨAG) systems, with all three Ψ codon:(Ψ codon)-tRNAPyl pairs
exhibiting mutual orthogonality. Moreover, we demonstrated that the RCE system
cooperates compatibly with the genetic code expansion strategy for dual ncAA
encoding. In sum, the RCE method utilized Ψ as a post-transcriptional ‘letter’ to encode
and decode RNA codons in specific mRNA transcripts, opening a new route for genetic
alphabet expansion and site-specific ncAA incorporation in eukaryotic cells.
The rapidly growing repertoire of ncAAs represents a broad range of sense codons into stop codons20. Nevertheless, GCE utilizes genetic
chemical structures and functions, whose incorporation enables the blank codons transcribed from DNA to RNA, which have been limited
probing, dissection and modulation on various proteins of interest to stop codons in mammalian cells, and these interfere with translation
in living systems1–3. The genetic code expansion (GCE) strategy has termination of cellular transcripts.
been developed to reassign stop codons as a genetic blank codon1–3 in Alongside the central dogma, the genetic information contained
order to specifically incorporate ncAAs into proteins. However, reas- in RNA codons in the GCE strategy remains the same as in upstream
signing stop codons is not completely orthogonal to the translation DNA codons. However, given that diverse and abundant RNA modi-
termination of cellular transcripts, because this may result in off-target fications are independent of DNA codons and can directly influence
readthrough for endogenous stop codons in the translatome. Alter- the decoding process21–23, we postulate that it is possible to create
native strategies have been devised to create genetic blank codons RNA-based blank codons outside of the canonical 64 genetic codons.
in Escherichia coli, including: (1) orthogonal ribosome evolution for Therefore, we proposed that generating the post-transcriptional letter
quadruplet codon recognition5–7; (2) genome engineering8–11 to cre- as RNA-based blank codons might help to overcome the issues associ-
ate genomically recoded organisms such as syn61 (ref. 12), rE.coli-57 ated with leveraging existing genetic blank codons in the translatome.
(refs. 10,13) and Ochre14; and (3) the development of unnatural base This could be realized by programming specific encoding and decoding
pairs with hydrophobic interactions15,16. However, transplanting these processes of a targeted codon of interest in specified mRNA transcripts.
genetic blank codons into mammalian cells encounters challenges For instance, as a representative RNA modification, programmable
such as potential cytotoxicity, global translation byproducts and the installation of pseudouridine (Ψ) on specified mRNAs via guide small
complex eukaryotic genome17. Instead, two strategies have emerged nucleolar RNAs (gsnoRNAs)4,24,25 could generate Ψ-modified nonsense
to exploit translation processes. An artificial, membraneless organelle codons (Ψ codons) with enhanced, near-cognate decoding, probably
was created in mammalian cells to achieve orthogonal translation for owing to Ψ-promoted base pairing, base stacking and strengthen-
the UAG stop codon18,19. In addition, RNA base editors have converted ing sugar-phosphate backbone26. However, there is a current lack of
1The National Key Laboratory of Gene Function Studies and Manipulation, School of Life Sciences, Peking University, Beijing, China. 2Synthetic and Functional Biomolecules Center, Beijing National
Laboratory for Molecular Sciences, College of Chemistry and Molecular Engineering, Peking University, Beijing, China. 3Peking-Tsinghua Center for Life Sciences, Academy for Advanced
Interdisciplinary Studies, Peking University, Beijing, China. 4DP Technology, Beijing, China. 5School of Medicine, Shanghai Jiao Tong University, Shanghai, China. 6School of Life Science and
Technology, ShanghaiTech University, Shanghai, China. 7Key Laboratory of Bioorganic Chemistry and Molecular Engineering of Ministry of Education, Peking University, Beijing, China.
8Institute for Advanced Algorithms Research, Shanghai, China. 9Beijing Advanced Center of RNA Biology (BEACON), Peking University, Beijing, China. 10AI for Science Institute, Beijing, China.
11These authors contributed equally: Jiangle Liu, Xueqing Yan, Hao Wu. ✉e-mail: chengqi.yi@pku.edu.cn; pengchen@pku.edu.cn
Nature | www.nature.com | 1
Article
specific decoder tRNAs that are capable of recognizing modified RNA the corresponding reporters (such as 1:4, 1:2 and 1:1), and observed
codons from the 64 genetic codons, posing challenges for harnessing consistently high Ψ installation efficiency (Fig. 1b,c and Extended Data
the modified RNA codons as orthogonal blank codons to expand the Fig. 1a–c). After we tested a series of tRNA dosages, we found that the
genetic alphabet. tRNA dosage did not influence Ψ ratio (Fig. 1d,e and Extended Data
Here we developed an RCE approach to assign modified RNA codons Fig. 1d). Together, these results demonstrated that our designed
as new blank codons for ncAA incorporation in mammalian cells, gsnoRNAs operated robustly and efficiently for Ψ codon encoding
which are independent of the endogenous codon assignment in the during the RCE process.
translatome. To decode the three generated Ψ codons (ΨGA, ΨAA To further verify the encoding specificity, we determined the
and ΨAG) on specified mRNA transcripts, we generated three specific transcriptome-wide off-target Ψ sites27 (Supplementary Table 2 and
decoder tRNAs to three Ψ codons: (ΨGA)-tRNAPyl, (ΨAA)-tRNAPyl and Supplementary Fig. 3). Because the guide RNAs were carefully designed
(ΨAG)-tRNAPyl. These Ψ codon-tRNAs exhibited a robust preference to minimize off-targets, we identified only 9 off-target sites with a rela-
for the corresponding Ψ codons compared with endogenous codons, tively low Ψ ratio (ranging from 10.7% to 25.2%) as well as a consensus
which were retained in the translatome. RCE(ΨGA) achieved high speci- sequence motif resembling the on-target sequence (Extended Data
ficity for ncAA incorporation in ribosome profiling and proteome analy- Fig. 2a–f). Of note, none of these off-target sites resides at endogenous
sis, preserving the UGA codon which represents around 52% of stop stop codons (Extended Data Fig. 2g). In addition, we showed that these
codons in the human genome. We demonstrated that the three pairs— off-target Ψ sites had negligible impact on RNA expression and ribo-
ΨGA:(ΨGA)-tRNAPyl, ΨAA:(ΨAA)-tRNAPyl and ΨAG:(ΨAG)-tRNAPyl—are some footprints (Extended Data Fig. 2h,i). In sum, we conclude that
orthogonal to each other, enabling the specific incorporation of ncAAs our programmable and targeted RNA pseudouridylation is efficient
carrying different side chains into mammalian proteins. Moreover, and specific for creating Ψ codons.
our RCE approach cooperated with the current GCE system, confirm-
ing the compatibility of different codon-expansion strategies for
Generating a decoder tRNA for ΨGA
encoding dual ncAAs within cells. Overall, the RCE method enabled
programmable encoding and decoding of modified RNA codons via To make ΨGA a bioorthogonally assignable codon for reprogramming,
independent Ψ codon:(Ψ codon)-tRNAPyl pairs, significantly improving a decoder tRNA is necessary to efficiently suppress ΨGA but not the
the translatome-wide specificity of ncAA incorporation, allowing for UGA codon with customized ncAAs. This is difficult, not only because
the precise investigation and modulation of proteins of interest under UGA represents the most prevalent stop codon (approximately 52%
various in vivo settings. of stop codons) in the human genome, but also because UGA is natu-
rally prone to readthrough among the 3 stop codons28. Initially, we
evaluated whether wild-type tRNAPyl(UCA) could distinguish ΨGA from
Rationale of RCE
the cognate UGA codon. We selected three representative wild-type
RNA modifications are well-studied for their dynamic influences on tRNAPyl molecules from distinct species: Methanosarcina mazei
the decoding process of the targeted codon during translation21, (Mm) tRNAPyl(UCA), Methanomethylophilus alvus (Ma) tRNAPyl(UCA)
independent of the central dogma. To harness RNA modifications from class A ΔNPyltRNAs, and Methanomassiliicoccus intestinalis (Mi)
as post-transcriptional letters and expand the genetic alphabet, we tRNAPyl(UCA) from class B ΔNPyltRNAs29. Notably, minimal readthrough
programmed the RCE using a two-step process: encoding and decod- differences between ΨGA and UGA were observed for the three
ing (Fig. 1a). For encoding using RNA modifications, we utilized the wild-type tRNAPyl decoder tRNAs.
programmable pseudouridylation tool RESTART4 (RNA editing to spe- To produce a decoder tRNA with a high ΨGA preference, we focused
cific transcripts for pseudouridine-mediated premature termination on the anticodon stem-loop (ASL) of tRNA and attempted to identify
codon readthrough) to produce site-specific Ψ codons, converting the possible variant tRNAs with desired properties, relying on ASL muta-
targeted uridine (U) to Ψ on specific mRNA transcripts. For decoding, tions to influence stability, flexibility and proximal interactions of the
we identified specific decoder tRNAs for the modified RNA codons by tRNAPyl decoder tRNAs during decoding in the small subunit of the ribo-
screening the wild-type and engineered tRNAPyl constructs. Therefore, some30, thereby potentially swaying the decoding preference toward
using programmable encoding and decoding processes, we were able ΨGA. It is equally important that the ASL mutations do not affect the
to assign the modified RNA Ψ codons as new blank codons for ncAA interaction of PylRS with tRNAPyl (refs. 31,32), so that we can generate
incorporation that operate orthogonally to canonical codon assign- tRNAPyl variants without affecting its aminoacylation activity.
ment for protein biogenesis throughout the translatome. To assess the possibilities, we screened 150 tRNAPyl variants for all
combinations of single-nucleotide mutations within the ASL region
of the three representative wild-type tRNAPyl(UCA) decoder tRNAs
Programmable encoding of the ΨGA codon
(Fig. 2a). We used the dual-fluorescent reporter Screen-TGA to measure
To implement the RCE approach, we first ensured that the Ψ codon the readthrough efficiency of tRNA variants (Supplementary Fig. 4a),
installation method was robust. As the proposed RCE approach includes and the fold change between the readthrough ratios of ΨGA and UGA
ternary components containing the RESTART tool for Ψ installation, a as a measure for the ΨGA preference. We determined that more than
non-canonical aminoacyl-tRNA synthetase (RS) and a decoder tRNA half of the mutations at the ASL produced at least 1.5-fold ΨGA prefer-
for Ψ codon decoding, we evaluated the efficiency and robustness of ence, with mutations at position 37 generally producing a high ΨGA
programmable and targeted RNA pseudouridylation as the initial step preference (greater than twofold) (Fig. 2b and Supplementary Table 3).
to create the Ψ codon4,24 for the RCE system. Screening these tRNA variants, we determined that although the exact
We constructed several dual-fluorescent mCherry–linker–GFP identity of the 37th nucleotide had to be experimentally tested, posi-
reporters, with a target UGA codon in the linker sequence (Supple- tion 37 improved the ΨGA preference in general (Fig. 2b). This finding
mentary Table 1). We then designed guide RNAs targeting the UGA mirrors previous structural insights, which revealed that nucleotide
codon, following the principle of RESTART4 for Ψ installation. To quan- 37 consistently stacks between anticodon nucleotides, contributing
titatively determine Ψ ratios, we used PRAISE, a Ψ detection method to overall ASL stability and flexibility30. Therefore, from a series of
that utilizes sequencing27 (Supplementary Fig. 2). We found high Ψ tRNA variants responding to ΨGA, we selected MmtRNAPyl(UCA)-37G
ratios for the targeted UGA with different flanking sequences in the owing to its higher specificity for the ΨGA codon as well as its efficiency
reporters, ranging from 55% to 96% (average ratio approximately 71%). for incorporating various ncAAs, and we named this decoder tRNA
We also tested different stoichiometry between the gsnoRNAs and (ΨGA)-tRNAPyl.
2 | Nature | www.nature.com
a
1. Encoding: produce Ψ codon on intended mRNA 2. Decoding: Ψ codon-tRNAPyl generated to expand Ψ codon
U Ψ Target Translatome-wide specificity
O O
NHP2 NHP2
NOP10 NOP10
NH GAR1 GAR1 HN NH
DKC1 DKC1
N O O
UGA/UAA/UAG Restart ΨGA/ΨAA/ΨAG Pro b n i c n A g A , d in is c s o e r c p t o in r g a t o io r n m o o n d P u O la I ting
Ψ codon: ΨGA/ΨAA/ΨAG
Non-target
Programmable Ψ
Stop codon via gsnoRNA Ψ codon
Undisturbed
Non-target
Non-target stop codon
Unmodified
RCE components
gsnoRNA
Endogenous targeted sequence
UGA/UAA/UAG
DKC1 DKC1
ncAA
PylRS to aminoacylate Ψ codon: Specified mRNA Non-target mRNA Ribosome
gsnoRNA Ψ codon-tRNAPyl Ψ codon-tRNAPyl with ncAA ΨGA/ΨAA/ΨAG
b d
gsnoRNA dosage per reporter = 0.25 gsnoRNA dosage per reporter = 1 PyIRS–tRNAPyl per reporter = 1 PyIRS–tRNAPyl per reporter = 4
30 bp 30 bp 30 bp 30 bp
[0–2206244] [0–1795897] [0–1482475] [0–3600313]
T
CCTATATCACCGGAtgaGGATCAGCCCCA CCTATATCACCGGAtgaGGATCAGCCCCA CCTATATCACCGGAtgaGGATCAGCCCCA CTATATCACCGGAtgaGGATCAGCCCCAG
Deletion at Ψ site Deletion at Ψ site Deletion at Ψ site Deletion at Ψ site
c e
100
75
50
25
0
gsnoRNA dosage gctrl 0.25 1 2 1
(per reporter) GCE PylRS–tRNAPyl + gsnoRNA gsnoRNA
Nature | www.nature.com | 3
AGT-sunev
no
oitar
AGΨ
)ANRr
S81
ta Ψ
%(
100
75
50
25
0
PylRS–tRNAPyl 0 1 4 8
dosage (per reporter) gsnoRNA
AGT-sunev
no
oitar
AGΨ
)ANRr
S81
ta Ψ
%(
RNA : A C G U Protein: Genetic codon
Post-transcriptional letter Expanded codon
RNA modification: Ψ... RCE Modified RNA codon for ncAA
Match
Translation termination
Undisturbed
Ribosome disassembly
Legend
Programmable
PylRS–tRNAPyl + gsnoRNA
Fig. 1 | See next page for caption.
Article
Fig. 1 | Schematic overview of the RCE strategy and yields of encoded ΨGA decoder tRNA, the lock represents the Ψ codon and the yellow star represents
codon in the specified mRNA transcript. a, The RCE strategy contains the the mutation in decoder tRNA. POI, protein of interest. b,c, Representative
encoding and decoding processes for a modified RNA codon. For encoding, IGV views of the installed Ψ at targeted U sites (b) and corresponding bar plots
the RESTART system was used, including a programmable gsnoRNA and DKC1. of ΨGA codon yields (c) in target mRNA under a 1:4 or 1:1 stoichiometric ratio
A gsnoRNA was constructed to target the specified mRNA transcript via of gsnoRNA-TGA to the targeted Venus-TGA reporter. Following selective
base pairing, interacting with the DKC1 and the endogenous proteins to chemical labelling of Ψ with the PRAISE method, Ψ sites were identified as
pseudouridylate the U of the intended codon, thus sequence-specifically deletion signals during sequencing, and normalized to the deletion ratio of
producing Ψ codon (ΨAA/ΨAG/ΨGA) from stop codons (UAA/UAG/UGA). For Ψ sites (Ψ1347 and Ψ1367) in 18S ribosomal RNA (rRNA) for ΨGA codon yields.
decoding, (Ψ codon)-tRNAPyl decoder tRNAs were generated from tRNAPyl Data are shown as mean values (n = 2 independent experiments). gctrl,
mutants with a single-nucleotide mutation in the red region for the installed control non-targeting guide RNA. d,e, Representative IGV views (d) and
Ψ codons, whereas the endogenous stop codons remained undisturbed. Thus, corresponding ΨGA codon yields (e) in intended mRNA with different dosages
the RCE system could discriminate the Ψ-modified RNA codons (Ψ codons) of RS–tRNA relative to the targeted reporter. Data are shown as mean values
from usual stop codons. The hexagon represents a ncAA, the key represents the (n = 2 biologically independent replicates).
Next, we validated that (ΨGA)-tRNAPyl exhibited a robust preference while leaving the endogenous stop codons less disturbed compared
for the ΨGA codon on the dual-fluorescence LDLR, AGXT and CFTR-TGA to the GCE(UGA) system. Therefore, we performed ribosome profiling
reporters (Supplementary Table 1), whose ΨGA codons reside in differ- experiments for the RCE(ΨGA) system to measure its off-target activi-
ent sequence contexts adapted from approximately 200-nt segments ties, which directly reflect interferences on translation termination
of the CFTR, AGXT and LDLR transcripts surrounding the annotated within cells.
premature termination codons (PTC) in Clinvar33 (Supplementary To provide a holistic perspective on stop codon readthrough ratios
Fig. 5). With a 45.1–99.1% yield for the ΨGA codons (Supplementary in the translatome, we calculated the ribosome readthrough score
Fig. 6a), we found that (ΨGA)-tRNAPyl demonstrated a 2.7- to 11.7-fold (RRTS)34,40 values for all transcripts with identified ribosome foot-
ΨGA preference and adequate readthrough efficiencies (approximately prints on the 3′ untranslated region (UTR). As expected, the RCE(ΨGA)
19–21%) in the presence of ncAA-CbzK (carbobenzyloxy-l-lysine) and GCE(UGA) systems did not induce off-target readthrough on UAA
(Fig. 2c–f and Supplementary Fig. 6b,c). Besides HEK293T cells, we and UAG codons (Supplementary Fig. 9). For the UGA codon of the
also confirmed evident ΨGA preference of the RCE(ΨGA) system intended transcript, RCE(ΨGA) and GCE(UGA) systems exhibited simi-
to four additional cell lines (Supplementary Fig. 7). Finally, we con- lar on-target RRTS values of 0.366 and 0.375 using the intended UGA
firmed that (ΨGA)-tRNAPyl decoded the ΨGA codon specifically with as the stop codon (Supplementary Fig. 10). For the UGA codons of
ncAA but not natural amino acids by identifying readthrough product globally non-targeting transcripts, the median RRTS value in GCE(UGA)
using liquid chromatography–mass spectrometry (LC–MS) and liquid cells, RCE(ΨGA) cells and control cells was found to be 0.057, 0.014
chromatography–tandem mass spectrometry (LC–MS/MS), and the and 0, respectively (Fig. 3a). These findings suggest that RCE exhibited
tRNA charging with acid-denaturing gel northern blots (Extended Data a median fourfold reduction in global off-target readthrough ratios
Fig. 3 and Supplementary Fig. 8). and a similar on-target readthrough efficiency to GCE(UGA) cells, dem-
We also inspected the structural basis for the observed ΨGA codon onstrating a median fourfold ncAA incorporation specificity for the
preference. We performed all-atom molecular dynamics simulation intended transcript in the translatome.
based on cryo-electron microscopy (cryo-EM) structures of ribo- To further investigate the off-target transcripts, we used the RRTS
some, mRNA and tRNA (Extended Data Fig. 4a–c). By extracting the value of a transcript in control cells as background, and designated
tRNA ASL and mRNA for restrained simulations, we investigated the transcript as off-target if the transcript possessed obvious RRTS
the codon–anticodon pairing probability for nine selected tRNAs fold changes in RCE(ΨGA) or GCE(UGA) cells. Regardless of the
with and without Ψ codon preference. We found enhanced pair- RRTS fold-change cut-off that we used, we consistently identified
ing probabilities for ΨGA compared with UGA for tRNAs with ΨGA lower off-target transcripts for RCE(ΨGA) cells than for GCE(UGA)
preference (Extended Data Fig. 4d). For instance, MmtRNAPyl(UCA)- cells (Fig. 3b). For instance, using a strict cut-off of a tenfold change,
37G formed more stable hydrogen bonds with the ΨGA codon than we observed that the number of off-target transcripts significantly
with the UGA codon (Extended Data Fig. 4e–h), indicating that the decreased from 63 in GCE(UGA) to 34 in RCE(ΨGA) (Fig. 3b). We also
strengthened pairing with the ΨGA codon may account for the codon evaluated the gene ontology (GO) terms of off-target transcripts, and
preference. Overall, we successfully established a decoder tRNA, determined that GCE(UGA) led to 16 enriched pathways. Notably,
(ΨGA)-tRNAPyl, that preferentially decoded the ΨGA codon, and thus the top enriched term appears to be related to ribosome biogenesis.
distinguished the ΨGA codon from endogenous allocations of the Off-target transcripts in RCE(ΨGA) were enriched across only four
64 genetic codons. pathways (Fig. 3c), demonstrating substantially reduced enrichment
in ribosome biogenesis and no enrichment in DNA damage and repair.
Given that natural stop codon readthrough events are associated with
Translatome-wide decoding specificity
diverse pathologies, we next examined the RRTS of reported transcripts
We next evaluated the decoding specificity of the RCE(ΨGA) system, with naturally occurring readthrough events at the UGA codon. After
which consists of the ΨGA codon and (ΨGA)-tRNAPyl, by evaluating excluding transcripts with low footprint coverage, we identified two
the potential off-target readthrough events on the UGA codon (which representative transcripts, MDH1 (ref. 28) and THG1L (ref. 41), which
accounts for around 52% of stop codons) across the translatome. Ribo- exhibited distinct readthrough in control cells. In RCE(ΨGA) cells,
some profiling has been widely utilized to assess global off-target we identified numbers of readthrough events that resembled those
activities of suppressor tRNAs34, as well as to examine the relevant in control cells, suggesting a minimal impact of the RCE system on
pathologies resulting from upregulated stop codon readthrough, these transcripts. In GCE(UGA) cells, the readthrough activities were
involving protein mislocalization35, aggregation36, instability37 and significantly enhanced. For MDH1, the RRTS in control cells, RCE(ΨGA)
the cascades of nontrivial magnitude38,39. It should also be suitable for cells and GCE(UGA) cells was 0.021, 0.033 and 0.169, respectively. Thus
the evaluation of the translatome-wide specificity of the RCE system the off-target readthrough ratio on MDH1 of RCE(ΨGA) exhibited a
alongside the GCE system. By design, the RCE(ΨGA) system should 12-fold reduction compared with the GCE(UGA) system, with a dis-
incorporate a ncAA at the produced ΨGA codon on specified mRNAs, tinct increase in RRTS of 0.148 induced by the GCE system (Fig. 3d).
4 | Nature | www.nature.com
tRNA variant library
UGA ΨGA
Readthrough on UGA
1. ΨGA preference 2. Readthrough on ΨGA
Readthrough on ΨGA
Nature | www.nature.com | 5
G
AAcn–
KzbC+
(ΨGA)-tRNAPyl
(ΨGA)-tRNAPyl = MmtRNAPyl (UCA) – 37G
AGT-RLDL
a
b
c
0.20
0.15
0.10
0.05
0 –ncAA
d
oitar
hguorhtdaeR
)ytisnetni
yrrehCm/PFG(
0.25
3.08 × 10–4
+Cbzk
0.20 RCE(ΨGA)
0.15
0.10
0.05
0
–ncAA +Cbzk
oitar
hguorhtdaeR
)ytisnetni
yrrehCm/PFG(
200 μm
UGA ΨGA 0.25 4.35 × 10–3
200 μm
yrrehCm
PFG
yrrehCm
PFG
UGA ΨGA
AGT-TXGA
AAcn–
KzbC+
yrrehCm
PFG
yrrehCm
PFG
15
10
5
0
ecnereferp
AGΨ
3
2
1
0
ecnereferp
AGΨ
Low decoding High decoding
UGA ΨGA
MatRNAPyl MitRNAPyl MmtRNAPyl
e
f
WT
G
WT NN A
27 GC T
A
28 CG
T
A 29a GC T A
29b GC T
A
30 GC
T
A
31 TC
G
A
32 CG
T A 33 TC
G C 37 AG
T C 38 AG
T
C 39 AG
T
A
40 CG
T
A
41a CG
T
A 41b TC
G
C
41c AG T
A
42 GC
T A
43 CG
T
PosRefMut
–ncAA UGA –ncAA UGA –ncAA UGA +ncAA ΨGA +ncAA ΨGA +ncAA ΨGA
000.0 500.0 010.0
Readthrough
510.0 020.0
1.0 2.0 3.0
WT NN A
27 CG T
A
28 CG
T
C 29a AG T A
29b GC T
A
30 GC
T
A
31 CG
T
A
32 CG
T A 33 TC
G A 37 CG
T C 38 AG
T
A 39 GC
T
A
40 CG
T
A
41a CG
T
C 41b AG
T
A
41c CG T
A
42 GC
T A
43 GC
T
PosRefMut
0000.0 5200.0 0500.0 5700.0 0010.0
1.0
Readthrough
2.0 3.0
(ΨGA)-tRNAPyl on UGA
RCE(ΨGA)
WT NN C
27 AG T
C
28 AG
T
A 29a TC G
A 29b GC
T
A
30 GC
T
C
31 AG
T
A
32 CG T WT (ΨGA)-tRNAPyl A
33 TC G
C 37 AG (ΨGA)-tRNAPyl on UGA T
C
38 AG T
A
39 TC
G
A
40 CG
T
A
41a CG T
A
41b GC T
A
42 TC
G A
43 TC
G
PosRefMut
(ΨGA)-tRNAPyl
1.0 2.0
Readthrough
4.0
000.0 500.0 010.0 510.0
3.0
30 40 30 40 30 40
37 37 37
Fig. 2 | Screening and evaluation of the specific and efficient decoder ratios are truncated to improve visualization. c,d, Representative fluorescence
tRNA for the ΨGA codon over the UGA codon. a, Scheme demonstrating the images showing readthrough of (ΨGA)-tRNAPyl on UGA and ΨGA codons in
screening strategy of decoder tRNA for the ΨGA codon. Each tRNA variant the LDLR-TGA (c) and AGXT-TGA (d) reporters in the absence and presence of
was assessed with readthrough efficiencies in both UGA and ΨGA conditions. CbzK. Experiments were repeated independently three times. e,f, Readthrough
b, Top, secondary structures of MmtRNAPyl(UCA), MatRNAPyl(UCA) and ratios of (ΨGA)-tRNAPyl on UGA and ΨGA codons in the LDLR-TGA (e) and AGXT-
MitRNAPyl(UCA), with mutated regions highlighted in red. Bottom, dot plot TGA (f) reporters in the absence and presence of CbzK. Data are mean ± s.d.
showing readthrough ratios on the UGA and ΨGA codons of tRNA variants (n = 3 biologically independent replicates). Readthrough ratios were normalized
bearing single-nucleotide mutations. Wild-type (WT) nucleotides, mutated using read reporters, which do not contain stop codons in the coding sequences.
nucleotides and position are shown in the Ref, Mut and Pos columns, respectively. P values were calculated by a two-sided Student’s t-test.
Experiments were performed with or without ncAA. y axes showing readthrough
Article
3.74 × 10–37
3.72 × 10–10 5.54 × 10–12
0.8
0.6
0.4
0.2
0
GCE(UGA) RCE(ΨGA) Control
G
CE( U
GA
R
)
CE( Ψ
GA)
G
CE( U
GA)
R
CE( Ψ
GA) Control
G
CE( U
GA)
R
CE( Ψ
GA) Control
For THG1L, the RCE(ΨGA) cells possessed no clear off-target read- gene expression. We found no interference in the transcriptome of
through on THG1L, whereas the GCE(UGA) system induced an RRTS RCE(ΨGA) or GCE(UGA) cells, supported by robust correlations among
increase of 0.153 (Fig. 3e). These lower off-target stop codon read- RCE(ΨGA), GCE(UGA) and control cells (Fig. 3h,i). This indicated that
through ratios in RCE(ΨGA) cells were directly supported by the counts the interferences of codon-expansion methods probably occur in
per million mapped reads (CPM) viewed using the Integrated Genome the translatome but not the transcriptome, consistent with previous
Viewer (IGV) (Fig. 3f,g). reports42. Collectively, these results demonstrated that the RCE(ΨGA)
In addition to ribosome profiling, we also conducted RNA-seq system exhibits higher specificity during codon expansion than the
experiments to assess any potential effects of the RCE approach on GCE(UGA) approach.
6 | Nature | www.nature.com
STRR
200
150
100
50
0
2 4 6 8 10
seneg
tegrat-ffo
fo
rebmuN
GCE Ribosome biogenesis Adjusted P value rRNA metabolic process 0.03
RCE Ribonucleoprotein complex biogenesis
0.02
rRNA processing
ncRNA processing 0.01
Spindle elongation
DNA recombination
Maturation of SSU-rRNA
Positive regulation of mitotic sister chromatid separation
Regulation of DNA recombination
Establishment of protein localization to organelle
Regulation of response to DNA damage stimulus
Ribosomal small subunit biogenesis Gene count
Regulation of DNA repair
10
Mitotic spindle midzone assembly
20 Ribosome assembly
30
0.4
0.3
0.2
0.1
0
L1GHT
fo
STRR
0.20
0.15
0.10
0.05
0
1HDM
fo
STRR
a b c
d f [0–95] MDH1 [0–4] h
GCE-rep1 12
[0–95] [0–4]
GCE-rep2 9 [0–95] [0–4]
RCE-rep1
[0–95] [0–4] 6
RCE-rep2
[0–95] [0–4] 3
Control-rep1
[0–95] [0–4]
Control-rep2 0
0 3 6 9 12
CDS 3′ UTR log (control FPKM) 2
e g i
THG1L
[0–50] [0–4]
12.5
GCE-rep1
[0–50] [0–4]
10.0 GCE-rep2
[0–50] [0–4]
7.5 RCE-rep1
[0–50] [0–4]
5.0
RCE-rep2
[0–50] [0–4] 2.5
Control-rep1
[0–50] [0–4] 0
Control-rep2 0 2.5 5.0 7.5 10.0 12.5
log (GCE FPKM) CDS 3′ UTR 2
)MKPF
ECR(
gol
)MKPF
ECR(
gol
2
2
0
Fold-change cut-off
r = 0.991
r = 0.996
MDH1
THG1L
r = 0.996
r = 0.998
MDH1
THG1L
Fig. 3 | The RCE(ΨGA) system exhibited high translatome-wide decoding the Benjamini–Hochberg method. SSU-rRNA, small subunit rRNA. d,e, RRTS
specificity without transcriptome-wide disturbance. a, Jitter plot of RRTS values of MDH1 (d) and THG1L (e) in GCE(UGA), RCE(ΨGA) and control cells.
values for transcripts containing canonical UGA stop codons with 3′ UTR Data are shown as mean values (n = 2 biologically independent replicates).
footprints in GCE(UGA), RCE(ΨGA) and control cells via ribosome profiling f,g, Zoomed-in IGV views of ribosome footprints on representative MDH1 (f)
experiments for (n = 909 transcripts) from n = 2 biologically independent and THG1L (g) transcripts in which natural readthrough efficiencies on the
replicates. The centre horizontal line indicates the median RRTS and error bars canonical stop codon, UGA, were upregulated (n = 2 biologically independent
represent 50% confidence intervals. P values for RRTS values between groups replicates). h,i, RNA sequencing, illustrating consistent RNA transcription
were computed using a two-sided Mann–Whitney U test. b, Bar plot depicting levels between RCE(ΨGA) and control cells (h), and between RCE(ΨGA) and
the number of potential off-target transcripts detected in GCE(UGA) and GCE(UGA) cells (i), including off-target transcripts (red dots), MDH1 and THG1L
RCE(ΨGA) cells at indicated RRTS fold-change thresholds. c, Comparison of (blue dots), and other transcripts (grey dots). Data are shown as mean values
enriched GO terms of off-target transcripts in GCE(UGA) and RCE(ΨGA) cells. (n = 2 biologically independent replicates).
P value was calculated by hypergeometric test and subsequently corrected by
a b d
UGA or ΨGA CbzK TCOK-a AzK 1.13 × 10–7
N domain Catalytic domain GFP Flag )P FG 8 R (Ψ C G E A (Ψ )- G tR A N ) APyl on UGA
c
ncAA
oitar
hguorhtdaeR
–)TW
(C
R S fo % ( P
FG
–C
4
6
5.95 × 10–4 5.11 × 10–4
–ncAA CbzK TCOK-a AzK R S 2
no
= UGA ΨGA UGA ΨGA UGA ΨGA UGA ΨGA
0
–ncAA +CbzK +AzK +TCOK-a
P
FB
Caged Decaged
UGA ΨGA UGA ΨGA
P
FG
–C
R
S
Actin
Phosphorylating
substrates
ATP
ATP
Substrate
tyrosine kinase that participates in signalling pathways that control a
Site-specific ncAA encoding via RCE
wide range of biological activities. As lysine 295 in its catalytical pocket
After examining the incorporation specificity in the translatome, we is crucial for ATP docking and phosphoryl transfer, we produced a
demonstrated the applicability of the RCE strategy for incorporating SRC(K295*/Y527F)–GFP construct43,44 (Fig. 4a), in which a ncAA was
ncAAs with diverse functionalities, which would facilitate the probing incorporated at residue 295 in the catalytic pocket, and the Y527F
and modulation of protein activity, location and interactions within mutation abolishes autoinhibition by Y527 phosphorylation, thereby
living cells. We selected SRC kinase, a well-known non-receptor protein mimicking the constitutive phosphorylation activity of SRC.
Nature | www.nature.com | 7
0001Yp
SRC
SRC(K295TCOK-a)
enisoryt
detalyrohpsohP
:BI
Decaging Phosphorylation Western
blotting
SRC-K295 SRC-K295
6
4
2
0
−8 −6 −4 −2 0 2 4 6 8
log [fold change
(dec2aged/caged)]
)eulav
P( gol– 01
f
pSRC-Y416
e
g h i
SRC direct substrates
PTK2 pY861
MPZL1 pY263
DVL2 pY27 HNRNPK pY72 RAB7A pY183 SRC pY187
SRC pY419
ANXA2 pY24
LDHA pY10 HNRNPK pY380
DVL2 pY18 ARHGDIA pY156 MPZL1 pY241 VHL pY185 SRC pY216
ARHGAP35 pY1087 PRKCD pY313 GAB1 pY259 EMD pY74
ARHGAP35 pY1105
Caged-
C
1 aged-
C
2 age
D
d
e
-
c
3 age
D
d
e
-1 caged
D
-
e
2 caged-3
5.1– 0.1– 5.0– 0 5.0
R
NH N3
O
R = R = O R =
O O O H2N COOH O
kDa
95
95
43
N N
190
N N
O
N
H
O NH2
33
j
mRNA processing Regulation of mRNA processing
Regulation of mRNA splicing, via spliceosome
Gene count
Inner mitochondrial membrane organization 5
RNA splicing, via transesterification reactions 10 GCE RCE mRNA splicing, via spliceosome 82 31 13 RNA splicing, via transesterification reactions Adjusted
Regulation of mRNA metabolic process P value RNA splicing 0 0 . . 0 0 0 1 1
Viral entry into host cell 0.2
Regulation of protein complex stability 0.6
Entry into host
Protein insertion into mitochondrial inner
z-score membrane
0.1 GCE RCE
Fig. 4 | RCE(ΨGA) enables site-specific ncAA incorporation and precise with similar results. g, Volcano plot showing the abundance changes of the
modulation of protein activity in living cells. a, Scheme of the SRC(K295*/ identified phosphotyrosine (pTyr) sites following SRC(K295TCOK-a) decaging.
Y527F)–GFP (SRC–GFP) construct for ncAA incorporation. b, Chemical Red dots represent significantly upregulated (more than twofold) pTyr sites.
structures of CbzK, TCOK-a, and AzK. c,d, Representative fluorescence P values were calculated by two-sided Student’s t-tests (n = 3 biologically
images (c) of cells and readthrough ratios (d) of (ΨGA)-tRNAPyl on the UGA and independent replicates). h, Heat maps showing the SRC decaging-triggered
ΨGA codons of SRC(K295*/Y527F)–GFP reporter in the absence and presence increase of phosphorylations on proteins that have been previously reported
of different ncAAs. Scale bar, 200 µm. d, Readthrough ratios of (ΨGA)-tRNAPyl as direct SRC substrates, across the three biologically independent replicates
on the UGA and ΨGA codons of SRC(K295*/Y527F) in the absence of ncAA and of caged and decaged samples. The colour bar represents the phosphorylation
the presence of CbzK, TCOK-a or AzK. Data are mean ± s.d. (n = 3 biologically level (z-score). i, Venn diagram showing a high overlap of ncAA-incorporated
independent replicates). P values were calculated by a two-sided Student’s endogenous proteins induced by the GCE and RCE systems. j, GO enrichment
t-test. e, Illustration of MeTz-mediated cleavage of the trans-cyclooctene analysis of the off-target misincorporated endogenous proteins, showing that
2
(TCO) moiety and the resulting SRC kinase activation. f, Western blotting of the standard GCE system is much more enriched in misincorporated biological
(ΨGA)-tRNAPyl-mediated readthrough products from suppression of the processes than the RCE system. P values were calculated by hypergeometric
UGA or ΨGA codons, as well as the phosphorylated substrates using pY1000 or tests and subsequently corrected by the Benjamini–Hochberg method (n = 3
anti-pSRC Y416 antibodies. Each experiment was repeated twice independently biologically independent replicates).
Article
To validate the incorporation capability of different ncAAs, we nearly a subset of that induced by GCE, further demonstrating the supe-
selected three representative ncAAs, including an aromatic lysine deriv- rior specificity of the RCE system (Fig. 4i,j and Supplementary Table 5).
ative, CbzK, a chemically caged lysine analogue, TCOK-a (axial isomer Collectively, our results demonstrated that the RCE(ΨGA) method
of trans-cyclooctene-caged lysine amino acid), and the bioorthogonally could introduce functional ncAAs as efficiently as the GCE(UGA) strat-
clickable AzK (Fig. 4b). With a 60.9% yield for the ΨGA codon (Supple- egy while maintaining high specificity on the ΨGA, allowing applica-
mentary Fig. 11a), we determined that (ΨGA)-tRNAPyl had a high ΨGA tions ranging from specific protein labelling to functional modulations
preference (from 5.1- to 8.3-fold) in the presence of CbzK, AzK and in living cells.
TCOK-a (Fig. 4c,d). For the ncAA incorporation efficiency, we identi-
fied similar readthrough efficiencies of RCE(ΨGA) and GCE(UGA) on
Expanding mRNA codons beyond ΨGA
the SRC(K295*/Y527F)–GFP construct in the presence of CbzK, AzK or
TCOK-a (Supplementary Fig. 12a,b). Therefore, the RCE(ΨGA) system Following the establishment of the RCE(ΨGA) system, we next extended
incorporated ncAAs into proteins as efficiently as the standard GCE the RCE rationale to create additional Ψ codons for ncAA incorporation
system. by adapting the similar encoding and decoding processes. To develop
These site-specifically incorporated ncAAs allowed specific protein the RCE(ΨAA) system, we developed two representative reporters,
labelling via the bioorthogonal ligation reaction45, as well as in situ pro- LDLR-TAA and AGXT-TAA, adapted from the LDLR-TGA and AGXT-TGA
tein activation via the bioorthogonal cleavage reaction inside cells46. reporters (Supplementary Table 1). When producing the ΨAA codon,
In particular, chemically caged ncAAs that can undergo bioorthogonal we observed high ΨAA yields of ~100% on AGXT-TAA reporters with the
cleavable reactions have been extensively applied for gain-of-function corresponding gsnoRNA-AGXT (Supplementary Fig. 13a). Via a screen-
study of proteins under native cellular context46. Among them, TCOK-a ing process (Supplementary Fig. 14) which is similar to that for ΨGA,
has been increasingly used as it can undergo rapid and biocompatible we identified tRNA variants showing preference for ΨAA, and selected
inverse electron-demand Diels–Alder (invDA) reaction in the presence MitRNAPyl(UUA)-37G with 2.1-fold ΨAA preference and GCE-comparable
of 3,6-dimethyl-1,2,4,5-tetrazine (MeTz)47 (Fig. 4e). To this end, we efficiency as (ΨAA)-tRNAPyl (Fig. 5a–e and Supplementary Fig. 13b,c).
2
utilized this reaction pair and the RCE(ΨGA) method for bioorthogo- For the RCE(ΨAG) system, we screened the ΨAG-preferring tRNA vari-
nal SRC kinase activation in living cells. We first demonstrated that ants without obtaining satisfying variants with high ΨAG preference
RCE(ΨGA) achieved efficient expression of the caged oncogenic SRC and readthrough. Given that mutations at position 37 improved ΨAG
mutant (SRC(K295TCOK-a/Y527F)–GFP), similarly to the previous preference and mutations at position 31 exhibited a higher readthrough
GCE(UGA) strategy44 (Fig. 4f and Supplementary Fig. 11b–d). Of note, efficiency (Supplementary Fig. 15), we performed a second round of
incorporation of TCOK-a at SRC Lys295 temporally blocked SRC acti- screening for tRNAs with double mutations at positions 31 and 37. To
vity, which could be rescued by adding MeTz to trigger the regenera- our delight, the MmtRNAPyl(CUA)-31G37G exhibited a 2.1-fold ΨAG
2
tion of the native SRC protein (Fig. 4f and Supplementary Fig. 12c–e). preference and ~15% ΨAG readthrough efficiency, and thus was chosen
We then performed functional investigations in a mass spectrometry- as (ΨAG)-tRNAPyl (Supplementary Table 6 and Supplementary Fig. 16).
based proteomics study. Although investigating SRC substrates remains We then examined the preference of (ΨAG)-tRNAPyl on the produced
difficult owing to the dynamic and low-abundance tyrosine phospho- ΨAG codon in p53 transcripts. We produced a p53K305*–EGFP construct,
rylation, we successfully profiled the phosphoproteome changes upon encoding a p53 variant in which the AAG codon for lysine 305 that is
SRC decaging. Using an affinity purification–mass spectrometry strat- crucial for nuclear localization52–54 was replaced by a UAG codon (Fig. 5f),
egy48, we identified significantly upregulated phosphotyrosyl (pTyr) and then used our RCE(ΨAG) system for TCOK-a incorporation to con-
sites (Fig. 4g and Supplementary Table 4), several of which have been trol p53 protein localization. With a high ΨAG yield of 74.2% (Supple-
previously shown as direct substrates of SRC (Fig. 4h). Furthermore, mentary Fig. 17), (ΨAG)-tRNAPyl exhibited a 12.3-fold ΨAG preference
many of the identified pTyr sites contain the characteristic SRC sub- on the p53K305*–EGFP construct (Fig. 5f). The RCE(ΨAG) system demon-
strate motif (Fig. 4i and Supplementary Fig. 12f,g). We also detected strated a yield of 10.7% (Fig. 5f), and the produced p53(K305TCOK-a)–
phosphorylation at Y416, the auto-phosphorylation site44, upon SRC EGFP protein was specifically located in the cytoplasm (Fig. 5g). After
activation (Fig. 4f and Supplementary Fig. 12e). These results collec- MeTz-mediated TCOK-a decaging, the decaged protein p53-K305–
2
tively demonstrated that our gain-of-function SRC decaging strategy EGFP regained its nuclear localization (Fig. 5g and Supplementary
effectively elicits cellular responses that are directly attributable to Fig. 18). Notably, the three specific Ψ codon:(Ψ codon)-tRNAPyl pairs
the enzymatic function of SRC. Together, we demonstrated that the are mutually orthogonal, as the anticodon of (Ψ codon)-tRNAPyl specifi-
RCE(ΨGA) method enabled orthogonal control and functional study cally pairs with its corresponding Ψ codon (Fig. 5h and Supplementary
of enzyme activity in a gain-of-function manner in living cells. Fig. 19).
Next, we investigated the specificity of bioorthogonal protein label-
ling of the RCE system. We used a GCE(UGA) system with a widely used
MmPylRS–tRNA pair49–51, which we referred to here as TetRS–tRNATet, to RCE is compatible with GCE
incorporate TetBu (3-(6-butyl-1,2,4,5-tetrazin-3-yl)-l-phenylalanine), a Finally, we demonstrated that the RCE strategy could cooperate com-
commercially available ncAA (Extended Data Fig. 5a). For the RCE(ΨGA) patibly with other codon-expansion methods, and in particular the GCE
system, we adopted tRNATet-37G with ΨGA preference (Extended Data strategy. We integrated the RCE(ΨGA) and the GCE(UAG) strategy to
Fig. 5b). Although the on-target constructs were expressed at an endog- incorporate two different ncAAs (Fig. 5i). As the catalytic activity of SRC
enous concentration in the GCE and RCE system, the off-target signal kinase relies on its lysine 295 and can be inhibited by phosphorylation
from the RCE system was significantly lower than the GCE system, at Y527 (ref. 43), its activity could be caged through the incorporation
demonstrating the ncAA incorporation specificity (Extended Data of TCOK-a at residue 295 and the ncAA BocK at residue 527.
Fig. 5b–d). To illustrate dual ncAA incorporation in SRC, we used the MaRS–
We further illustrated the negligible disturbance of the RCE system on MaΔNtRNAPyl(CUA)(19) pair29 as the GCE(UAG) system to introduce
endogenous transcripts by measuring potential off-target TetBu incor- BocK. For the RCE(ΨGA) system to install TCOK-a, we utilized the
porations without transfecting any exogenous reporters (Extended MmPylRS-306A384F–MmtRNAPyl(UCA)-6T37G pair, in which a C at posi-
Data Fig. 5e,f). Finally, we detected the off-target TetBu-incorporated tion 6 of MmtRNAPyl(UCA)-37G was mutated to a T to ensure orthogonal-
proteins via mass spectrometry, and identified 43 and 113 off-target ity with MaPylRS29 according to the acceptor arm on Methanosarcina
TetBu-incorporated proteins for RCE and GCE, respectively (Extended spelaei (Spe)tRNAPyl. The MmtRNAPyl(UCA)-6T37G, still exhibited strong
Data Fig. 6). Of note, the off-target incorporations induced by RCE are ΨGA preference regardless of the presence of the GCE(UAG) system
8 | Nature | www.nature.com
UAA ΨAA
–ncAA +BocK
UAA ΨAA
Nature | www.nature.com | 9
yrrehCm
PFG
N domain Core domain NLS C domain GFP Flag
)A
503K
(35p
)TW
( 503K
-35p
RCE(ΨAG)-mediated p53(K305TCOK-a)–GFP
3.19 × 10–4
TCOK-a
9
6
3
0
RCE(ΨAG)
no
oitar
hguorhtdaeR
)TW
35p
fo
%(PFG–*503K-35p
–ncAA +BocK 5
UAA ΨAA
4
3
2
tRNA variant library
1
0
LDLR-TAA
UAA ΨAA
1. Ψ codon preference
2. Readthrough on Ψ codon
Ψ codon-tRNAPyl
AGXT-TAA
Hoechst p53 Merged Hoechst p53 Merged
ecnereferp
AAΨ
2.4
2.2
2.0
1.8
1.6
1.4
1.2
yrrehCm
PFG
ecnereferp
AAΨ
0.125
0.100
0.075
0.050
0.025
0
Decaging
oitar
hguorhtdaeR
)ytisnetni
yrrehCm/PFG(
(ΨAA)-tRNAPyl
on UAA
RCE(ΨAA)
(ΨAA)-tRNAPyl 0.09 on UAA
RCE(ΨAA)
0.06
0.03
0
–ncAA +BocK
oitar
hguorhtdaeR
)ytisnetni
yrrehCm/PFG(
Readthrough ratio
52.0 02.0 51.0 01.0 50.0
0
(ΨGA)-tRNAPyl
lyPANRt-nodoc
Ψ
a b c 7.88 × 10–3
G
G
–ncAA +BocK WT (ΨAA)-tRNAPyl
d e
2.77 × 10–3
Stop codon ΨCodon
WT (ΨAA)-tRNAPyl
f UAG or ΨAG g
UAG ΨAG
ncAA
degaC degaceD
(ΨAG)-tRNAPyl on UAG
h i j
GCE(UAG)
+TCOK-a
+TCOK-a, –BocK +TCOK-a, +BocK
At residue 295 At residue 527
Caged Decaged Caged Decaged
+TCOK-a BocK
kDa UGA ΨGA UGA ΨGA UGA ΨGA UGA ΨGA
(ΨAA)-tRNAPyl Full 95
length
SRC 70
truncation
(ΨAG)-tRNAPyl at 527 55
ΨGA UAG SRC 43
ΨGA ΨAA ΨAG truncation
Ψ codon RCE(ΨGA) GCE(UAG) at 295 33
Fig. 5 | The RCE strategy is expandable to other modified RNA codons and fluorescence images of cells containing RCE(ΨAG)-produced p53(K305TCOK-a)–
is compatible with the GCE strategy. a, Schematic of the screening strategy GFP protein before and after decaging. Cells expressing p53-K305A–GFP and
for (ΨAA)-tRNAPyl. b,c, Representative fluorescence images of cells (b) and bar p53-K305–GFP were used as cytoplasm- and nucleus-localized protein controls,
plots and dot plots (c) showing the readthrough performances of (ΨAA)-tRNAPyl respectively. The experiment was repeated twice independently with similar
on UAA and ΨAA codons of the LDLR-TAA and AGXT-TAA reporters. Scale bar, results. Scale bar, 10 µm. h, Readthrough ratio heatmap of three Ψ codons
200 µm. Data are mean ± s.d. (n = 3 biologically independent replicates). independently decoded by the corresponding (Ψ codon)-tRNAPyl decoder
d,e, Representative fluorescence images of cells (d) and bar plots and dot plots (e) tRNAs without cross-activity. Data are shown as mean values (n = 3 biologically
showing the readthrough performances of (ΨAA)-tRNAPyl on LDLR-TAA and independent replicates). i, Schematic illustrating dual ncAA incorporation
AGXT-TAA reporters. Scale bar, 200 µm. Data are mean ± s.d. (n = 3 biologically by coordination of the mutually orthogonal RCE(ΨGA) and GCE(UAG)
independent replicates). P values were calculated by a two-sided Student’s systems. j, Orthogonal TCOK-a and BocK dual incorporation (producing
t-test. f, Readthrough ratios of (ΨAG)-tRNAPyl on the UAG and ΨAG codons of SRC(K295TCOK-a/Y527BocK) protein) by coordination of RCE(ΨGA) and
the p53K305*–GFP construct in the absence and presence of TCOK-a. Data are GCE(UAG) systems. The dual-ncAA-incorporated full-length SRC protein was
mean ± s.d. (n = 3 biologically independent replicates). P values were calculated verified by western blotting, which was repeated twice independently with
by a two-sided Student’s t-test. NLS, nuclear localization signal. g, Representative similar results.
Article
(Fig. 5j), and obtained orthogonality to MaPylRS. This orthogonality was of the native 64 heritable codons, dynamically enriching the genetic
also demonstrated via mass spectrometry44,55 (Supplementary Fig. 20). alphabet in mammalian cells.
This adaption implied that based on properly arranged orthogo-
nal RS–tRNA pairs29, we could integrate and program various codon-
Online content
expansion methods as orthogonal modules for encoding different
ncAAs. Thus, we have demonstrated the adaptability of the (Ψ codon)- Any methods, additional references, Nature Portfolio reporting summa-
tRNAPyl in the RCE approach, enabling RCE to serve as an independent ries, source data, extended data, supplementary information, acknowl-
codon-expansion module that work compatibly with the GCE strategy. edgements, peer review information; details of author contributions
and competing interests; and statements of data and code availability
are available at https://doi.org/10.1038/s41586-025-09165-x.
Discussion
In summary, we established a general applicable RCE strategy 1. Liu, C. C. & Schultz, P. G. Adding new chemistries to the genetic code. Annu. Rev.
and obtained three triply orthogonal pairs, ΨGA:(ΨGA)-tRNAPyl, Biochem. 79, 413–444 (2010).
ΨAA:(ΨAA)-tRNAPyl and ΨAG:(ΨAG)-tRNAPyl, for site-specific ncAA 2. Lemke, E. A. The exploding genetic code. ChemBioChem 15, 1691–1694 (2014).
3. Chin, J. W. Expanding and reprogramming the genetic code. Nature 550, 53–60 (2017).
incorporation into proteins in mammalian cells. Using ribosome profil- 4. Song, J. et al. CRISPR-free, programmable RNA pseudouridylation to suppress premature
ing and proteomics analysis, we demonstrated the translatome-wide termination codons. Mol. Cell 83, 139–155.e139 (2023).
5. Neumann, H., Wang, K., Davis, L., Garcia-Alai, M. & Chin, J. W. Encoding multiple
decoding specificity of the RCE strategy, which significantly reduced
unnatural amino acids via evolution of a quadruplet-decoding ribosome. Nature 464,
off-target stop codon readthroughs compared with the standard GCE 441–444 (2010).
method. The high specificity of the RCE strategy was verified through 6. Orelle, C. et al. Protein synthesis by ribosomes with tethered subunits. Nature 524,
119–124 (2015).
multiple approaches, indicating that RCE-based protein decaging offers
7. Fried, S. D., Schmied, W. H., Uttamapinant, C. & Chin, J. W. Ribosome subunit stapling for
a general strategy for activation of enzymes of interest. In the encod- orthogonal translation in E. coli. Angew. Chem. Int. Ed. 54, 12791–12794 (2015).
ing component, we identified high Ψ codon yields on these specified 8. Isaacs, F. J. et al. Precise manipulation of chromosomes in vivo enables genome-wide
mRNA transcripts with specified gsnoRNAs4. In the decoding compo- codon replacement. Science 333, 348–353 (2011).
9. Lajoie, M. J. et al. Genomically recoded organisms expand biological functions. Science
nent, the (Ψ codon)-tRNAPyl decode Ψ codons with robust Ψ codon 342, 357–360 (2013).
preferences across various transcripts, consistent with the globally 10. Ostrov, N. et al. Design, synthesis, and testing toward a 57-codon genome. Science 353,
819–822 (2016).
reduced off-target readthrough events. The specificities in encoding
11. Wang, K. et al. Defining synonymous codon compression schemes by genome recoding.
and decoding processes contributed to the overall ncAA-incorporating Nature 539, 59–64 (2016).
specificity of our RCE strategy, which could be further advanced by 12. Fredens, J. et al. Total synthesis of Escherichia coli with a recoded genome. Nature 569,
514–518 (2019).
engineering the relevant mRNAs, small nucleolar RNAs (snoRNAs) and
13. Nyerges, A. et al. Synthetic genomes unveil the effects of synonymous recoding. Preprint
decoder tRNAs. In addition, although we focused on the stop codons at bioRxiv https://doi.org/10.1101/2024.06.16.599206 (2024).
in this study, our RCE strategy could in principle be extended to sense 14. Grome, M. W. et al. Engineering a genomically recoded organism with one stop codon.
Nature 639, 512–521 (2025).
codons, owing to its programmability and specificity during the encod-
15. Malyshev, D. A. et al. A semi-synthetic organism with an expanded genetic alphabet.
ing and decoding processes. Indeed, a new GCE strategy leveraging Nature 509, 385–388 (2014).
rare codons has been reported recently51. 16. Fischer, E. C. et al. New codons for efficient production of unnatural proteins in a
semisynthetic organism. Nat. Chem. Biol. 16, 570–576 (2020).
In addition to pseudouridine, the RCE approach may allow for the
17. Thompson, D. B. et al. The future of multiplexed eukaryotic genome engineering. ACS
utilization of various post-transcriptionally modified RNA-expanded Chem. Biol. 13, 313–325 (2018).
codons for translation. More than 150 types of chemical modifica- 18. Reinkemeier, C. D., Girona, G. E. & Lemke, E. A. Designer membraneless organelles
enable codon reassignment of selected mRNAs in eukaryotes. Science 363, eaaw2644
tion have been identified in cellular RNAs so far, most of which can
(2019).
influence the stability, structure and interactions of RNA to a certain 19. Reinkemeier, C. D. & Lemke, E. A. Dual film-like organelles enable spatial separation of
extent, including N6-methyladenosine, N1-methylpseudouridine, orthogonal eukaryotic translation. Cell 184, 4886–4903.e4821 (2021).
20. Hao, M. et al. Tracking endogenous proteins based on RNA editing-mediated genetic
5-methylcytosine and 2′-O-methylation22,23. We anticipate that we could code expansion. Nat. Chem. Biol. 20, 721–731 (2024).
generate additional blank RNA codons by adapting the corresponding 21. Ranjan, N. & Leidel, S. A. The epitranscriptome in translation regulation: mRNA and tRNA
encoding and decoding processes. The encoding of these varied RNA modifications as the two sides of the same coin? FEBS Lett. 593, 1483–1493 (2019).
22. Boccaletto, P. et al. MODOMICS: a database of RNA modification pathways. 2021 update.
modifications can be attained with molecular precision—for instance, Nucleic Acids Res. 50, D231–D235 (2022).
by using Cas13-directed methyltransferase56 or CRISPR–Cas9 based 23. Shi, H., Chai, P., Jia, R. & Fan, X. Novel insight into the regulatory roles of diverse RNA
enzymes57. For decoding, the engineering and characterization of modifications: Re-defining the bridge between transcription and translation. Mol. Cancer
19, 78 (2020).
(Ψ codon)-tRNAPyl decoder tRNAs could enable the development of 24. Karijolich, J. & Yu, Y.-T. Converting nonsense codons into sense codons by targeted
specific decoder tRNAs for other modified RNA codons. Collectively, pseudouridylation. Nature 474, 395–398 (2011).
the RCE approach enables a subtantial expansion of the four-letter 25. Luo, N. et al. Near-cognate tRNAs increase the efficiency and precision of pseudouridine-
mediated readthrough of premature termination codons. Nat. Biotechnol. 48, 114–123
(A, U, C and G) transcription ‘alphabet’. (2025).
Furthermore, the RCE approach can act as an adaptable strategy 26. Charette, M. & Gray, M. W. Pseudouridine in RNA: what, where, how, and why. IUBMB Life
49, 341–351 (2000).
that is compatible with the current approaches that exploit translation
27. Zhang, M. et al. Quantitative profiling of pseudouridylation landscape in the human
processes, such as RNA base editors20 and orthogonally translating transcriptome. Nat. Chem. Biol. 19, 1185–1195 (2023).
organelles18,19. RNA base editors can deaminate the C to U, converting 28. Hofhuis, J. et al. The functional readthrough extension of malate dehydrogenase reveals a
sense codons into stop codons on endogenous mRNA transcripts20. modification of the genetic code. Open Biol. 6, 160246 (2016).
29. Dunkelmann, D. L., Willis, J. C. W., Beattie, A. T. & Chin, J. W. Engineered triply orthogonal
In the same transcripts, the gsnoRNA for encoding in the RCE system pyrrolysyl–tRNA synthetase/tRNA pairs enable the genetic encoding of three distinct
could pseudouridylate the produced U of the targeted stop codon, non-canonical amino acids. Nat. Chem. 12, 535–544 (2020).
30. Seelam Prabhakar, P., Takyi, N. A. & Wetmore, S. D. Posttranscriptional modifications at
followed by decoding in the RCE system. Similarly, the RCE approach
the 37th position in the anticodon stem-loop of tRNA: structural insights from MD
could operate compatibly with the orthogonally translating organelles simulations. RNA 27, 202–220 (2021).
to spatially confine UAG codons18,19. This is due to the molecular basis 31. Nozawa, K. et al. Pyrrolysyl-tRNA synthetase–tRNAPyl structure reveals the molecular
of the RCE strategy, in which the Ψ codon and the (Ψ codon)-tRNAPyl, basis of orthogonality. Nature 457, 1163–1167 (2009).
32. Suzuki, T. et al. Crystal structures reveal an elusive functional domain of pyrrolysyl-tRNA
which are compatible with the RNA motifs and the fused PylRS18,19, synthetase. Nat. Chem. Biol. 13, 1261–1266 (2017).
promote phase separation. Collectively, our RCE approach offers a 33. Landrum, M. J. et al. ClinVar: public archive of relationships among sequence variation
and human phenotype. Nucleic Acids Res. 42, D980–D985 (2014).
post-transcriptional codon-expansion strategy for ncAA incorpora-
34. Wang, J. et al. AAV-delivered suppressor tRNA overcomes a nonsense mutation in mice.
tion, in which the modified RNA codons can be assigned independently Nature 604, 343–348 (2022).
10 | Nature | www.nature.com
35. Hollingsworth, T. J. & Gross, A. K. The severe autosomal dominant retinitis pigmentosa 49. Jang, H. S., Jana, S., Blizzard, R. J., Meeuwsen, J. C. & Mehl, R. A. Access to faster
rhodopsin mutant Ter349Glu mislocalizes and induces rapid rod cell death. J. Biol. Chem. eukaryotic cell labeling with encoded tetrazine amino acids. J. Am. Chem. Soc. 142,
288, 29047–29055 (2013). 7245–7249 (2020).
36. Vidal, R. et al. A stop-codon mutation in the BRI gene associated with familial British 50. Bryson, D. I. et al. Continuous directed evolution of aminoacyl-tRNA synthetases. Nat.
dementia. Nature 399, 776–781 (1999). Chem. Biol. 13, 1253–1260 (2017).
37. Shibata, N. et al. Degradation of stop codon read-through mutant proteins via the ubiquitin– 51. Ding, W. et al. Rare codon recoding for efficient noncanonical amino acid incorporation in
proteasome system causes hereditary disorders. J. Biol. Chem. 290, 28428–28437 mammalian cells. Science 384, 1134–1142 (2024).
(2015). 52. Liang, S.-H. & Clarke, M. F. Regulation of p53 localization. Eur. J. Biochem. 268, 2779–2783
38. Namy, O., Duchateau-Nguyen, G. & Rousset, J.-P. Translational readthrough of the PDE2 (2001).
stop codon modulates cAMP levels in Saccharomyces cerevisiae. Mol. Microbiol. 43, 53. O’Keefe, K., Li, H. & Zhang, Y. Nucleocytoplasmic shuttling of p53 is essential for
641–652 (2002). MDM2-mediated cytoplasmic degradation but not ubiquitination. Mol. Cell. Biol. 23,
39. Capone, J. P., Sharp, P. A. & RajBhandary, U. L. Amber, ochre and opal suppressor tRNA 6396–6405 (2003).
genes derived from a human serine tRNA gene. EMBO J. 4, 213–221 (1985). 54. Gautier, A. et al. Genetically encoded photocontrol of protein localization in mammalian
40. Wangen, J. R. & Green, R. Stop codon context influences genome-wide stimulation of cells. J. Am. Chem. Soc. 132, 4086–4088 (2010).
termination codon readthrough by aminoglycosides. eLife 9, e52611 (2020). 55. Guangcan, S. et al. How to use open-pFind in deep proteomics data analysis?—A protocol
41. Schueren, F. et al. Peroxisomal lactate dehydrogenase is generated by translational for rigorous identification and quantitation of peptides and proteins from mass
readthrough in mammals. eLife 3, e03640 (2014). spectrometry data. Biophys. Rep. 7, 207–226 (2021).
42. Shi, N. et al. Restoration of dystrophin expression in mice by suppressing a nonsense 56. Wilson, C., Chen, P. J., Miao, Z. & Liu, D. R. Programmable m6A modification of cellular
mutation through the incorporation of unnatural amino acids. Nat. Biomed. Eng. 6, RNAs with a Cas13-directed methyltransferase. Nat. Biotechnol. 38, 1431–1440 (2020).
195–206 (2022). 57. Liu, X.-M., Zhou, J., Mao, Y., Ji, Q. & Qian, S.-B. Programmable RNA N6-methyladenosine
43. Yeatman, T. J. A renaissance for SRC. Nat. Rev. Cancer 4, 470–480 (2004). editing by CRISPR–Cas9 conjugates. Nat. Chem. Biol. 15, 865–871 (2019).
44. Zhang, G. et al. Bioorthogonal chemical activation of kinases in living systems. ACS Cent.
Sci. 2, 325–331 (2016). Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
45. Sletten, E. M. & Bertozzi, C. R. Bioorthogonal chemistry: fishing for selectivity in a sea of published maps and institutional affiliations.
functionality. Angew. Chem. Int. Ed. 48, 6974–6998 (2009).
46. Li, J. & Chen, P. R. Development and application of bond cleavage reactions in Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this
bioorthogonal chemistry. Nat. Chem. Biol. 12, 129–137 (2016). article under a publishing agreement with the author(s) or other rightsholder(s); author
47. Li, J., Jia, S. & Chen, P. R. Diels–Alder reaction-triggered bioorthogonal protein decaging self-archiving of the accepted manuscript version of this article is solely governed by the
in living cells. Nat. Chem. Biol. 10, 1003–1005 (2014). terms of such publishing agreement and applicable law.
48. Bian, Y. et al. Ultra-deep tyrosine phosphoproteomics enabled by a phosphotyrosine
superbinder. Nat. Chem. Biol. 12, 959–966 (2016). © The Author(s), under exclusive licence to Springer Nature Limited 2025
Nature | www.nature.com | 11
Article
Methods were captured using a 10× microscope objective, and these images were
subsequently analysed automatically using MetaXpress software (MX
Cell culture version 6.2.3.733; CME version 6.2.3.991). The intensities of mCherry or
HEK293T, U-2 OS, COS-7 and HeLa cells were cultured in DMEM medium EGFP were determined as the intensity per cell multiplied by the number
(Corning, 10-013-CVR) and CHO-K1 cells were cultured in DMEM/F12 of positive cells in the fluorescence images. The readthrough ratio was
medium (Gibco). All cells were cultured with medium containing 10% calculated as the GFP intensity divided by the mCherry intensity, and
FBS and 1% penicillin/streptomycin (both from Gibco, v/v) at 37 °C then normalized to the DF-Read reporter without any truncations.
with 5% CO. To passage cells, they were initially rinsed with PBS (Corn-
2
ing), and then treated with 0.25% Trypsin (Gibco) before incubation Readthrough product enrichments
(37 °C, 1 min). Following this, the trypsin was neutralized by adding HEK293T cells were seeded into 6-well plates (Corning, 3516) and incu-
FBS-containing medium. The cells were subsequently collected by bated for 16–24 h. For general readthrough reporters with adequate
centrifugation (500g, 5 min), counted, and divided for various exper- gsnoRNAs, 1 µg of expression reporter, 250 ng of gsnoRNA, 125 ng
imental uses. All cells were confirmed to be free from mycoplasma of DKC1-iso3, and 1 µg of RS-2×Decoder plasmids were transfected
contamination using a mycoplasma detection kit (TransGene Biotech, using PEI (Yeasen, 40816ES02) following to the manufacturer’s direc-
FM311-01) prior to use. tions in the presence of ncAAs. The culture medium was changed after
24 h of transfection. At 96 h post-transfection, the cells were rinsed
Plasmid construction with PBS and collected with PBS. Following centrifugation, the cells
Dual-fluorescent reporters were generated based on previously were resuspended with a TBS-containing protease inhibitor (Roche)
described dual-colour reporters using site-directed mutagenesis and 1 mM DTT. After ultrasonic lysis, the cell lysate was centrifuged at
with FastPfu polymerase (Transgene) following the manufacturer’s 21,000 rpm at 4 °C. The supernatant was obtained and incubated for 2 h
guidelines. For the construction of hU6-driven gsnoRNA expression alongside anti-Flag M2 magnetic beads (Sigma Aldrich) for flag-tagged
constructs, gsnoRNA fragments were amplified using an overlapping readthrough product purification following the manufacturer’s direc-
PCR strategy involving one sense strand and three antisense strands, tions. The beads were rinsed with TBST three times, TBS three times,
and subsequently integrated into the pLenti-sgRNA-lib 2.0 backbone and finally with HO. Samples with a concentration of 2 mg ml−1 of 3×Flag
2
(Addgene, #89638) using Golden Gate cloning. The secondary struc- peptide in TBS were used to elute the enriched readthrough products
tures of gsnoRNAs were predicted using RNAfold58,59 (http://rna.tbi. at 37 °C for 2 h.
univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi) with default settings.
The sequences of gsnoRNAs and synthetases are provided in Supple- Amino acid characterization at specified locations by mass
mentary Table 1. Synthetases and tRNAs were custom synthesized by spectrometry
Beijing Qsingke Biotechnology Company. p53 and SRC genes were also Following the enrichment of readthrough products as described
synthesized by Beijing Qsingke Biotechnology Company and inserted above, the elution was supplemented with 5× SDS loading buffer
into the pcDNA3.1-GFP vector using Gibson assembly with NEBuilder (Beyotime), and subjected to boiling at 95 °C for 30 min. Subsequently,
HiFi DNA Assembly Master Mix (NEB). RS3#-2×(ΨAG)-tRNAPyl and centrifugation at 21,000 rpm for 10 min facilitated the separation of
RS3#-2×(ΨGA)-tRNAPyl constructs were generated by recombining the supernatant, which was then loaded onto a 4%–15% SDS–PAGE
PCR-amplified RS3# and Decoder sequences using NEBuilder HiFi gel (Beyotime) along with Blue Plus V Protein Marker (DM141-01,
DNA Assembly Master Mix (NEB). All clones were verified by Sanger Transgene) markers. After staining with Coomassie blue, the correct
sequencing. Plasmids for transfection were purified using the EndoFree protein bands were excised and destained using a solution containing
Mini Plasmid Kit II (Tiangen Biotech). 25 mM ammonium bicarbonate in 50% acetonitrile. Following reduction
with dithiothreitol and alkylation with iodoacetamide, the proteins
Screening assay for decoder tRNA based on high-content imaging were subjected to overnight digestion with porcine trypsin (Sequenc-
HEK293T cells were rinsed with PBS and treated with 0.25% Trypsin at ing grade modified; Pierce) at 37 °C. The resulting tryptic peptides
37 °C for 1 min. Trypsin activity was halted by adding FBS-containing were extracted from the gel pieces using acetonitrile supplemented
medium. After centrifugation at 500g for 5 min, the cells were enumer- with 0.1% formic acid. Subsequently, the samples were dried using a
ated and diluted to a concentration of 4 × 105 cells per ml. Subsequently, vacuum centrifuge concentrator at 30 °C and reconstituted in 10 µl
the cells were seeded into individual wells of 96-well flat-bottom plates of 0.1% formic acid/HO. LC–MS/MS analysis was conducted using
2
(LABSELECT, 11514) that had been pre-coated overnight with a 20 ng µl−1 an Orbitrap Fusion Lumos mass spectrometer (Thermo Scientific).
poly-d-lysine (Beyotime, ST508) solution and rinsed with water. Follow- Data analysis was performed using Proteome Discoverer (Thermo)
ing 16–24 h of incubation, each tRNA mutant was separately assessed against the UniProt database (https://www.uniprot.org) using human
under both the UGA and ΨGA conditions. proteome (UP000005640), along with a custom database (Supple-
For each tRNA mutant, a ΨGA mixture was prepared by combin- mentary Table 1) containing reporter sequences featuring 20 differ-
ing 62.5 ng of the Screen-TGA reporter, 15.6 ng of gsno-TGA, 7.8 ng of ent natural amino acids at positions corresponding to the premature
DKC1-iso3, 62.5 ng of synthetases, and 122.5 ng of the tRNA mutant with termination codon location. Variable modifications of CbzK, TCOK-a
0.5 µl of Lipofectamine LTX reagent (Invitrogen) and 0.2 µl of PLUS and BocK were considered during the search process according to their
reagent (Invitrogen), following the manufacturer’s instructions. Simi- molecular weight. Abundances of peptides containing different amino
larly, for the UGA mixture, 62.5 ng of the Screen-TGA reporter, 15.6 ng acids were used to calculate the incorporation percentage of different
of gctrl, 7.8 ng of DKC1-vector, 62.5 ng of synthetases, and 122.5 ng of amino acids.
the tRNA mutant were mixed with 0.5 µl of Lipofectamine LTX reagent
(Invitrogen) and 0.2 µl PLUS reagent (Invitrogen) in the same manner. Western blotting
The UGA and ΨGA mixtures were added to separate wells contain- HEK293T cells were seeded into 24-well plates (Corning, 3526) and
ing HEK293T cells cultured in a medium supplemented with 200 µM incubated for 16–24 h. For the ΨGA condition of HA–SRC(K295*/
ncAA (CbzK or BocK, corresponding to the synthetases). After 24 h, Y527F)–GFP, 500 ng of HA-SRCK295*/Y527F–GFP, 125 ng of gsnoRNA-SRC,
the transfected cells were provided with fresh culture medium. At 62.5 ng of DKC1-iso3, and 500 ng of RS3#-2×(ΨGA)-tRNAPyl plasmids
48–72 h post-transfection, cell imaging was conducted using the Imag- were transfected using Lipofectamine LTX reagent (Invitrogen) sup-
eXpress Micro 4 high-content imaging system (Molecular Devices). plemented with PLUS reagent (Invitrogen) following the manufacturer’s
Four images from different regions of a single well on the 96-well plates directions. For the UGA condition of HA–SRC–(K295*/Y527F)–GFP,
500 ng of HA-SRCK295*/Y527F–GFP, 125 ng of gctrl, 62.5 ng of DKC1-iso3, and recycled with the standard medium. After 2 h, cells were incubated
500 ng of RS3#-2×(ΨGA)-tRNAPyl plasmids were transfected using Lipo- with 10 µg ml−1 Hoechst (Beyotime) in DMEM for 10 min and rinsed
fectamine LTX reagent (Invitrogen) supplemented with PLUS reagent with DMEM three times. A Spin SR (Evident, Olympus) was used to
(Invitrogen). The UGA and ΨGA conditions encompassed two copies, capture images, measure colocalization and fluorescence intensity
one was supplied to cells incubated with 100 µM ncAA, while the other using 63× magnification.
was provided to cells under standard cell culture conditions as a control.
For evaluating ncAA incorporation, the TetRS-2×(ΨGA)-tRNATet plasmid mRNA sequencing
was used for RCE, the TetRS-2×tRNATet (wild-type tRNATet) plasmid was Total RNAs were extracted from the same cell lysates utilized in the
used for GCE, others remain unchanged in transfection. ribosome profiling step, and used for RNA-seq by Guangzhou Epibiotek.
For the ΨGA condition of HA–SRC(K295*/Y527*)–GFP, 500 ng of Library concentrations were determined using a Qubit 2.0 fluorometer
HA-SRCK295*/Y527*–GFP, 125 ng of gsno-SRC, 62.5 ng of DKC1-iso3, 500 ng with the Qubit dsDNA HS Assay kit (Invitrogen), while size distribution
of RS3#-2×(ΨGA)-tRNAPyl (based on SpetRNAPyl), 500 ng of MaPylRS, was assessed using the Agilent 4150 TapeStation System with High
and 980 ng of MaΔNtRNAPyl(CUA)(19) plasmids were transfected using Sensitivity D1000 ScreenTape. Finally, sequencing of the libraries was
Lipofectamine LTX PLUS reagent (Invitrogen). For the UGA condition performed on the Illumina Hiseq X-ten platform, generating 2 ×150 bp
of HA–SRC(K295*/Y527*)–GFP, 500 ng of HA-SRCK295*/Y527*–GFP, 125 ng of paired-end raw reads.
gctrl, 62.5 ng of DKC1-vector, 500 ng of RS3#-2×(ΨGA)-tRNAPyl (based
on SpetRNAPyl), 500 ng of MaPylRS, and 980 ng of MaΔNtRNAPyl(CUA)(19) Analysis of RNA-seq data
plasmids were transfected using Lipofectamine LTX PLUS reagent. The The raw reads were quality-controlled using Trim galore60 (version
UGA and ΨGA conditions both encompassed four copies, the first was 0.6.6) to exclude adaptor sequences and low-quality reads. Clean
supplied to cells under common cell culture conditions, the second was reads (length > 30 bp) were mapped to the human reference genome
supplied to cells incubated with 100 µM TCOK-a, the third was supplied (GRCh38) with HISAT2 (ref. 61) (version 4.8.5). Expression abundance
to cells incubated with 100 µM BocK, while the fourth was supplied to values were computed using featureCount62 (version 2.0.4), and genes
cells incubated with 100 µM TCOK-a and 100 µM BocK. with a reads per kilobase per million mapped reads (RPKM) value below
At 24–48 h post-transfection, cells were rinsed with cold PBS and 1 were removed for subsequent analysis.
centrifuged at 500g at 4 °C for 5 min. The cell pellets were mixed with
1× SDS loading buffer, boiled at 95 °C for 30 min, and centrifuged at Quantification of Ψ via PRAISE
21,000 rpm for 10 min. Proteins in supernatants were separated via HEK293T cells were plated in 24-well plates and allowed to incubate
electrophoresis on 4%–15% SDS–PAGE gel and transferred to PVDF for 16–24 h. Each well received transfection with 500 ng of reporter,
membranes (Millipore). These membranes were blocked using 5% BSA along with either 125 ng or 500 ng of Gsno (RCE samples) or Gctrl (GCE
and incubated with primary antibodies for 2 h at room temperature, samples), 62.5 ng of DKC1-iso3, and 500 µg of RS3#-2×Decoder plasmids
rinsed three times with TBST, and then incubated with horseradish using Lipofectamine LTX reagent (Invitrogen) supplemented with PLUS
peroxidase (HRP)-conjugated antibodies for 1 h at room temperature. reagent (Invitrogen), following the manufacturer’s directions. Total
The protein bands were visualized using a ChemiDoc MP Imaging RNA extraction was performed using TRIzol (Life Technologies), fol-
System (Bio-Rad). The intensity data were collected by Fiji (64-bit lowed by isopropanol precipitation, per the manufacturer’s protocol
for Windows; https://imagej.net/software/fiji/downloads, released (Invitrogen). A portion of 200 ng of total RNA from each sample was
30 May 2017). subjected to DNase I treatment at 37 °C for 30 min. Subsequently, RNA
For immunoblots shown in figures, the corresponding antibody and was fragmented to approximately 150 nt using magnesium RNA frag-
their dilution are as follows: mouse anti-Flag (Sigma Aldrich, F1804, mentation buffer (New England Biolabs) for 4 min at 94 °C, followed by
1:2,000 or 1:750 dilution); β-actin mouse monoclonal antibody (CWBIO, cooling on ice. The reaction was quenched using RNA fragmentation
CW0096M, 1:5,000 dilution); phosphotyrosine (P-Tyr-1000) MultiMab stop solution and then purified by ethanol precipitation. Following
rabbit monoclonal antibody mix (herein referred as pY1000) (CST, ethanol precipitation, RNA was resuspended in 5 µl of nuclease-free
8954, 1:2,000 or 1:750 dilution); phospho-SRC family (Tyr416) (E6G4R) water. A fresh bisulfite solution was freshly prepared by dissolving
rabbit monoclonal antibody 59548 (herein referred as pSRC Y416) 4.05 g of sodium bisulfite (Sigma Aldrich) in 5.5 ml of RNase-free water,
(CST, 1:1,000 dilution); eIF2α antibody 9722 (CST, 1:1,000 dilution); adjusting the pH to 5.1 with 10 M sodium hydroxide, and adjusting the
phospho-eIF2α (Ser51) (D9G8) XP rabbit monoclonal antibody 3398 volume to 10 ml with water. Additionally, a 100 mM hydroquinone
(CST, 1:1,000 dilution); ATF-4 (D4B8) rabbit monoclonal antibody solution was freshly prepared by adding 11.01 mg of hydroquinone
11815 (CST, 1:1,000 dilution); biotin antibody (33):sc-101339 (Santa (Sigma Aldrich) to 1 ml of RNase-free water. A sample of 5 µl of RNA
Cruz, 1:2,000 dilution); p53 antibody 9282 (CST, 1:1,000 dilution); fragments was dissolved in 50 µl of bisulfite/sulfite solution, consist-
phospho-p53 (Ser15) antibody 9284 (CST, 1:1,000 dilution); goat ing of a 100:1 mixture of bisulfite/sulfite solution and 100 mM hydro-
anti-mouse IgG, HRP conjugated (CWBIO, CW0102, 1:5,000 dilu- quinone, and heated to 70 °C for 5 h. The reaction mixture was then
tion); goat anti-rabbit IgG, HRP conjugated (CWBIO, CW0103, 1:5,000 desalted by moving it twice through Micro Bio-Spin 6 chromatography
dilution). columns (Bio-Rad). The desalted RNA was transferred to a new 1.5-ml
nuclease-free tube and adjusted to 100 µl with RNase-free water, fol-
Confocal imaging of subcellular localization lowed by incubation with an equal volume of 1 M Tris-HCl (pH 9.0) at
HEK293T cells cultured in wells were diluted to 4 × 105 cells per ml as 75 °C for 30 min. The reaction was promptly halted by chilling on ice
outlined above and seeded on 20-mm glass-bottom dishes following and ethanol precipitation.
coating with 20 ng µl−1 poly-d-lysine (Beyotime) solution overnight and For targeted amplicon sequencing, the bisulfite/sulfite-treated RNA
pre-rinsed with water. After 16–24 h of incubation, in the presence of was subsequently reverse transcribed into cDNA using random hex-
TCOK-a, 500 ng of p53K305*–EGFP reporter, 125 ng of gsno-P53, 62.5 ng amers (Thermo Fisher) with Maxima H minus Reverse Transcriptase
of DKC1-iso3, and 500 ng of RS3#-2×(ΨAG)-tRNAPyl were transfected (Thermo Fisher). For transcriptomic sequencing, mRNA or total RNA
into one specific dish according to numbering, using Lipofectamine for each sample was subjected to library construction using SMARTer
LTX reagent (Invitrogen) supplemented with PLUS reagent (Invitro- Stranded Total RNA-Seq Kit v3 Pico Input Mammalian (Takara Bio,
gen) following the manufacturer’s directions. Each transfection con- 634485) according to the manufacturer’s protocol, with a substitu-
dition consisted of two dishes providing TCOK-a; one was incubated tion of reverse transcriptase Maxima H minus Reverse Transcriptase
with 200 µM MeTz in medium to decage TCOK-a, while the other was (Thermo Fisher).
2
Article
significant differences in RRTS values across diverse samples. The genes
Analysis of PRAISE data that experience a twofold increase in RRTS after the treatment of GCE
The identification of Ψ sites and the assessment of modification levels or RCE tools are defined as potential off-targets to conduct GO enrich-
were conducted according to the established PRAISE pipeline (https:// ment analysis. To alleviate background noise, we additionally require
github.com/Zhe-jiang/PRAISE). Initially, only read 1 and 2 underwent that the RRTS of off-target genes must exceed 0.02. GO enrichment
further processing. Raw reads underwent adaptor removal and qual- analysis was performed using R package clusterProfiler68 (v4.8.3). We
ity control utilizing cutadapt (version 2.10)60. PCR redundancy was listed the transcripts with off-target UGA codon readthrough events
then eliminated using Seqkit (version 0.14.0)63 according to the unique by ribosome profiling in Supplementary Table 6.
molecular identifiers (UMIs) of 4 bp and 6 bp located at the 5′ and 3′
ends of reads R1, respectively. UMIs were sequentially removed by Quantitative tyrosine phosphoproteomic profiling
umi_tools (version 1.0.0)64. The obtained cleaned reads were aligned Cells were collected in lysis buffer, which contained 50 mM Tris-HCl,
to the reference sequences using the PRAISE tool (version 4.8.5) with pH 8.5, 7 M urea, 1% Triton X-100, 7 M urea, 1 mM PMSF, protease
default parameters27. Based on the realigned bam file, we first calcu- inhibitors mixture (RHAWN) and phosphatase inhibitor mixtures
lated the deletion rate for Ψ sites, and then normalized them to the (HY-K0022). The protein concentration was measured by the BCA
averaged deletion ratio of 18S Ψ1347 and Ψ1367 so as to obtain the protein assay kit (Pierce). Cellular proteins were precipitated by the
actual Ψ level. To identify the transcriptome-wide off-target Ψ editing chloroform-methanol method, and were solubilized in 50 mM Tris-HCl
of the RCE system, we used following criteria: (1) the deletion ratio in buffer (with 8 M urea, pH 8.5) with sonication. The soluble proteins
control samples should be less than 5%; (2) the difference in deletion were reduced with DTT, alkylated with iodoacetamide and digested
ratio between RCE samples and the control samples should be greater with trypsin (Sigma Aldrich). The digested proteins were acidified
than 10%; (3) the deletion ratio in RCE samples should be statistically by 10%TFA to pH 2-3, purified by the CAE-Ti-IMAC (J&K), and further
significantly great than that in control samples with a false discovery enriched by the pTyr superbinder48,69. The obtained peptides were
rate (FDR) value < 0.05. Primers for targeted deep sequencing were desalted and identified with LC–MS/MS (Orbitrap Fusion Lumos Tribid
listed in Supplementary Table 7. LC–MS).
The phosphoproteomic data were processed following reported pro-
Ribosome profiling tocol70, using Maxquant (version 2.6.5) with the Homo sapiens (organ-
HEK293T cells were seeded into 10-cm dishes and incubated for ism_id:9606) proteome databases (as UP000005640) downloaded
16–24 h as described above. For RCE samples, 40 µg of SRCK295*/Y527F– from Uniprot (https://www.uniprot.org). The phosphotyrosine (pTyr)
GFP reporter, 10 µg of gsno-SRC, 5 µg of DKC1-iso3, and 40 µg of RS3#- proteomic data were processed as previous study. We first removed
2×(ΨGA)-tRNAPyl plasmids were transfected into four dishes using the pTyr sites from reverse sequences and potential contaminants or
Lipofectamine LTX reagent (Invitrogen) supplemented with PLUS rea- showing localization probability less than 0.75. The intensities were
gent (Invitrogen) alongside 200 µM CbzK. For GCE samples, 40 µg of log-transformed, and the Pearson correlation values were calculated.
2
SRCK295*/Y527F–GFP reporter, 10 µg of gctrl, 5 µg of DKC1-vector, and 40 µg Data imputation was performed using Perseus software (version 4.8.5)
of RS3#-2×MmtRNAPyl (wild-type MmtRNAPyl) plasmids were transfected with parameters: downshift = 1.8 and width = 0.3. pTyr sites with log
2
into four dishes using Lipofectamine LTX reagent (Invitrogen) sup- fold change greater than one and analysis of variance adjusted P value
plemented with PLUS reagent (Invitrogen) alongside 200 µM CbzK. were kept as significantly changed pTyr sites.
The culture medium was changed after 12 h of transfection. At 48 h
post-transfection, the cells were cycled into fresh DMEM medium con- Proteomic profiling the mis-incorporations
taining 10% FBS and 0.1 mg ml−1 cycloheximide (CHX), and incubated at HEK293T cells were seeded into 10-cm dishes and incubated for
37 °C with 5% CO for 10 min. The cells were rinsed with pre-chilled PBS 16–24 h as described above. For RCE samples, 40 µg of SRCK295*/Y527F–
2
containing 0.1 mg ml−1 CHX 3 times and collected with the pre-chilled GFP reporter, 10 µg of gsno-SRC, 5 µg of DKC1-iso3, and 40 µg of
PBS containing 0.1 mg ml−1 CHX. TetRS-2×(ΨGA)-tRNATet plasmids were transfected into four dishes
The primary procedures followed the ribosome profiling protocol65 using Lipofectamine LTX reagent (Invitrogen) supplemented with
and were conducted by Guangzhou Epibiotek, incorporating the use of PLUS reagent (Invitrogen) alongside 200 µM CbzK. For GCE samples,
RNase I to enhance base resolution during treatment of the cell lysates. 40 µg of SRCK295*/Y527F–GFP reporter, 10 µg of gctrl, 5 µg of DKC1-vector,
RNA fragments between 26 and 32 nucleotides in length were isolated and 40 µg of TetRS-2×tRNATet (wild-type tRNATet) plasmids were trans-
via urea–PAGE and utilized for library construction. fected into 4 dishes using Lipofectamine LTX reagent (Invitrogen) sup-
plemented with PLUS reagent (Invitrogen) alongside 200 µM CbzK. At
Analysis of Ribo-seq data 48 h post-transfection, the cell were collected with modified RIPA buffer
Raw sequencing reads had their adaptors trimmed and low-quality following previous protocol51. The proteins in cell lysate were denatured
bases were trimmed using Trim_galore60 along with standard settings. with PBS buffer (containing 8 M urea), reacted with TCO-biotin probe
Reads mapping to rRNA and tRNA were removed, and the remaining (Confluore) for 2 h, precipitated with chloroform-methanol method.
reads were mapped to the human genome (hg38, GENCODE v44). The The proteins were redissolved in 2% SDS with sonication, diluted with
mapping was performed using bowtie66 (version 1.3.0) with the follow- PBS to final SDS concentration at 0.2%, and incubated with Streptavi-
ing parameters to allow one mismatch and acquire uniquely mapped din agarose resin beads (Thermo, 20353). The peptides on beads were
reads: ‘-m 1 -v 1 --best –strata’. In the reference annotation file, only the reduced with DTT, alkylated with iodoacetamide, digested with trypsin,
annotated transcript containing the longest coding sequence (CDS) desalted and identified under data-independent acquisition mode via
for each gene was utilized for further evaluation. RiboWaltz67 (version LC–MS/MS (Bruker, TIMS-TOF Pro2).
1.2.0) was used to characterize the P-sites for each ribosome-protected Data were analysed with DIA-NN software (version 1.9.2) under
fragment. default parameters71, with the H. sapiens (organism_id:9606) pro-
To identify transcripts that have undergone stop codon readthrough, teome database (as UP000005640) downloaded from Uniprot
we used RRTS40. RRTS represents a ratio of the ribosome density (https://www.uniprot.org)70. Proteins were filtered to include only
between the natural stop codon and the next in-frame stop codon to those identified in both replicates of at least one condition. The fil-
the ribosome density in the CDS. To increase the read depth of the initial tered proteins were then used as input for DEP Bioconductor package
samples, biological replicates were pooled during the comparison of (version 1.14.0)72 to conduct differential enrichment analysis. Miss-
RRTS between samples. A Mann–Whitney U test was utilized to assess ing values were imputed using the MinProb method with q = 0.01.
Proteins were considered differentially enriched if they exhibited log (December 2013) was downloaded from the following link: https://
2
fold changes greater than 1 relative to the control samples, with an hgdownload.soe.ucsc.edu. The H. sapiens proteome database
adjusted P value < 0.05. (UP000005640) was downloaded from https://www.uniprot.org. The
custom database containing reporter sequences featuring 20 differ-
Detecting tRNA aminoacylation ent natural amino acids at positions corresponding to the premature
Total RNA was extracted using TRIzol reagent (Invitrogen), chloroform termination codon location is provided in Supplementary Table 1.
(TGREAG), 3 M sodium acetate (pH 4.5) and ethanol (TGREAG). The The tRNA reference sequences were derived from GtRNAdb81 (http://
RNA samples were dissolved in 0.1 M sodium acetate (pH 4.5), mixed gtrnadb.ucsc.edu/; accessed September 2024). ISR-related genes were
with 2× RNA loading buffer (0.1 M sodium acetate pH 4.5, 90% glycerol, collected from the GeneCards database (https://www.genecards.org/;
0.03% xylene cyanide, and 0.03% bromophenol blue), and fractionated accessed September 2024). Source data are provided with this paper.
by electrophoresis at a constant 18 W on a 10% urea–PAGE gel (0.1 M
sodium acetate, pH 4.5) at 4 °C. Each blots contain the control tRNA
samples from cells which were transfected with wild-type tRNAPyl or Code availability
decoder tRNA but lack ncAA. We use the dye indicator, Xylenecyanol FF, Custom codes are available on GitHub (https://github.com/yanxue-
which is reported to indicate 55-nt RNA in the 10% urea–PAGE gel73. The qing621/RCE_project). These scripts include the pipelines for off-target
RNA was then transferred to nylon membrane (MILLIPORE) which was Ψ sites identification based on PRAISE sequencing data, evaluation of
then crosslinked using UVLink 1000 Crosslinker (Jena). The tRNA was potential off-target readthrough events based on Ribo-seq data, and
detected by Digoxigenin (DIG)-labelled DNA probes (Sangon), and visu- RNA-seq data analysis.
alized with Anti-Digoxigenin-AP (Roche). DIG-labelled probes were as
follows: MmtRNA, CGGAAACCCCGGGAATCTAACCCGGCTGAACGGA; 58. Lorenz, R. et al. ViennaRNA Package 2.0. Algorithms Mol. Biol. 6, 26 (2011).
59. Gruber, A. R., Lorenz, R., Bernhart, S. H., Neuböck, R. & Hofacker, I. L. The Vienna RNA
MatRNA, CGAGAGACCGGGGCGTCGAACCCCGCTGGCTAGG; MitRNA,
Websuite. Nucleic Acids Res. 36, W70–W74 (2008).
CGAAGTGCCCGGGAGTTGAACCCGGCTGCCGTGG. Each probe was 60. Martin, M. Cutadapt removes adapter sequences from high-throughput sequencing
modified with DIG at both 5′ and 3′ ends. reads. EMBnet J. 17, 10–12 (2011).
61. Kim, D., Paggi, J. M., Park, C., Bennett, C. & Salzberg, S. L. Graph-based genome alignment
and genotyping with HISAT2 and HISAT-genotype. Nat. Biotechnol. 37, 907–915 (2019).
Molecular dynamics simulation 62. Liao, Y., Smyth, G. K. & Shi, W. featureCounts: an efficient general purpose program for
The mRNA-tRNA–ribosome complex was built from crystal structures, assigning sequence reads to genomic features. Bioinformatics 30, 923–930 (2013).
63. Shen, W., Le, S., Li, Y. & Hu, F. SeqKit: a cross-platform and ultrafast toolkit for FASTA/Q file
with the mRNA and ribosome (Protein Data Bank (PDB) ID: 4JYA) and
manipulation. PLoS ONE 11, e0163962 (2016).
tRNA (PDB ID: 5UD5) from crystal structures. Molecular dynamics 64. Smith, T., Heger, A. & Sudbery, I. UMI-tools: modeling sequencing errors in unique
workflows were implemented using AmberTools (version 23) for force molecular identifiers to improve quantification accuracy. Genome Res. 27, 491–499
(2017).
field parameter assignment and system setup74, OpenMM (version
65. Ingolia, N. T., Brar, G. A., Rouskin, S., McGeachy, A. M. & Weissman, J. S. The ribosome
8.1.2) for simulation execution75, and MDTraj (version 1.9.8) for trajec- profiling strategy for monitoring translation in vivo by deep sequencing of ribosome-
tory analysis76. The simulation system utilized Amber99sb*-ildn77 for protected mRNA fragments. Nat. Protoc. 7, 1534–1550 (2012).
66. Langmead, B., Trapnell, C., Pop, M. & Salzberg, S. L. Ultrafast and memory-efficient
proteins, OL3 (ref. 78) for nucleic acids, GAFF2 (ref. 79) with AM1-BCC
alignment of short DNA sequences to the human genome. Genome Biol. 10, R25
charges for the cofactor, and Amber parameters with RESP charges80 (2009).
for Ψ (derived from HF/6-31 G* calculations). The structure was then 67. Lauria, F. et al. riboWaltz: optimization of ribosome P-site positioning in ribosome profiling
data. PLoS Comp. Biol. 14, e1006169 (2018).
solvated using TIP3P waters80 in a 12 Å buffer supplemented with 0.2 M
68. Wu, T. et al. clusterProfiler 4.0: a universal enrichment tool for interpreting omics data.
MgCl, followed by system preparation through energy minimization Innovation 2, 100141 (2021).
2
and sequential equilibration stages. 69. Dong, M. et al. Sensitive, robust, and cost-effective approach for tyrosine phosphoproteome
analysis. Anal. Chem. 89, 9307–9314 (2017).
Initial equilibration comprised 40 ns constant-temperature, 70. Cox, J. & Mann, M. MaxQuant enables high peptide identification rates, individualized
constant-pressure (NPT; number of particles N, pressure P, tempera- p.p.b.-range mass accuracies and proteome-wide protein quantification. Nat. Biotechnol.
ture T) ensemble simulation under 100 kJ mol−1 Å−1 restraints applied 26, 1367–1372 (2008).
71. Demichev, V., Messner, C. B., Vernardis, S. I., Lilley, K. S. & Ralser, M. DIA-NN: neural
to the ribosome–mRNA-tRNA complex. Subsequent relaxation was networks and interference correction enable deep proteome coverage in high
achieved through three consecutive 20 ns NPT simulations with pro- throughput. Nat. Methods 17, 41–44 (2020).
gressively reduced restraints of 50, 20, 5 kJ/mol/Å. In the production 72. Shaw, J. J. & Green, R. Two distinct components of release factor function uncovered by
nucleophile partitioning analysis. Mol. Cell 28, 458–467 (2007).
phase, 50 ns NPT simulation was performed for tRNA while maintain- 73. Gagnon, K. T. & Maxwell, E. S. Electrophoretic mobility shift assay for characterizing
ing 5 kJ/mol/Å restraints on the ribosome–mRNA backbone. The 5 kJ/ RNA–protein interaction. Methods Mol. Biol. 703, 275–291 (2011).
mol/Å restraints on the ribosome–mRNA backbone were not lifted 74. Case, D. A. et al. AmberTools. J. Chem. Inf. Model. 63, 6183–6191 (2023).
75. Eastman, P. et al. OpenMM 8: molecular dynamics simulation with machine learning
because the mRNA provided in the crystal structure contains only 5 potentials. J. Phys. Chem. B 128, 109–116 (2024).
bases. Additional restraints were necessary to maintain consistency 76. McGibbon, RobertT. et al. MDTraj: a modern open library for the analysis of molecular
dynamics trajectories. Biophys. J. 109, 1528–1532 (2015).
with the crystal structure.
77. Lindorff-Larsen, K. et al. Improved side-chain torsion potentials for the Amber ff99SB
The tRNA-mRNA binding structure were extracted form mRNA-tRNA– protein force field. Proteins Struct. Funct. Bioinformatics 78, 1950–1958 (2010).
ribosome complex, and performed restrained simulation based on the 78. Zgarbová, M. et al. Refinement of the Cornell et al. nucleic acids force field based on
reference quantum chemical calculations of glycosidic torsion profiles. J. Chem. Theory
codon–anticodon binding geometries were aligned to the correspond-
Comput. 7, 2886–2902 (2011).
ing region in 4JYA. Solvation and equilibration followed established 79. Wang, J., Wolf, R. M., Caldwell, J. W., Kollman, P. A. & Case, D. A. Development and testing
protocols, with production simulations extended to 200 ns. of a general amber force field. J. Comput. Chem. 25, 1157–1174 (2004).
80. Jorgensen, W. L., Chandrasekhar, J., Madura, J. D., Impey, R. W. & Klein, M. L. Comparison
of simple potential functions for simulating liquid water. J. Chem. Phys. 79, 926–935
Reporting summary
(1983).
Further information on research design is available in the Nature Port- 81. Chan, P. P. & Lowe, T. M. GtRNAdb 2.0: an expanded database of transfer RNA genes
identified in complete and draft genomes. Nucleic Acids Res. 44, D184–D189 (2016).
folio Reporting Summary linked to this article.
Acknowledgements The authors thank the National Center for Protein Sciences at Peking
University in Beijing, China, for assistance with the 4150 TapeStation System (G. Li), mass
Data availability
spectrometry (D. Liu and Q. Zhang), Zeiss LSM 980 confocal microscope and Spin SR confocal
All next-generation sequencing data generated for this study have microscope (L. Fu); G. Jia, R. Liu, F. Lin, X. Rao, C. Shao, M. Zhang and Y. Ma for discussions and
materials; the Center for Quantitative Biology at Peking University for assistance with the
been deposited in the NCBI Sequence Read Archive (SRA) under acces-
ImageXpress Micro 4 high-content imaging system; and X. Li for help. Part of the analysis was
sion code PRJNA1090628. The human reference genome GRCh38 performed on the High-Performance Computing Platform of the Center for Life Science
