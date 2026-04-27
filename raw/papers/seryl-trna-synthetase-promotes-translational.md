---
source_path: /mnt/c/Users/Administrator/Zotero/storage/EBTHLU5W/Liu 等 - 2023 - Seryl-tRNA synthetase promotes translational readthrough by mRNA binding and involvement of the sele.pdf
ingested: 2026-04-23
sha256: f2abcfa2e9c37578
---

10768–10781 Nucleic Acids Research, 2023, Vol. 51, No. 19 Published online 22 September 2023
https://doi.org/10.1093/nar/gkad773
Seryl-tRNA synthetase promotes translational
readthrough by mRNA binding and involvement of the
selenocysteine incorporation machinery
Ze Liu1 , † , Justin Wang1 , † , Yi Shi 1 , 2 , Brian A. Yee3 , Markus Terrey4 , Qian Zhang1 ,
Jenq-Chang Lee5 , Kuo-I Lin 6 , Andrew H.-J. Wang7 , Susan L. Ackerman4 , 8 , Gene W. Yeo 3 ,
Haissi Cui1 , * and Xiang-Lei Yang 1 , *
1 Department of Molecular Medicine, Scripps Research Institute, La Jolla, CA 92037, USA, 2 Department of
Biochemistry, School of Medicine, Nankai University, Tianjin, China, 3 Department of Cellular and Molecular Medicine,
University of California San Diego, La Jolla, CA 92093, USA, 4 How a rd Hughes Medical Institute, Department of
Cellular and Molecular Medicine, School of Medicine, University of California San Diego, La Jolla, CA 92093, USA,
5 Department of Surgery, National Cheng Kung University Medical College and Hospital, Taiwan, 6 Genomics
Research Center, Academia Sinica, Taiwan, 7 The Ph.D. Progr a m for Translational Medicine, College of Medical
Science and Technology, Taipei Medical University and Academia Sinica, Taipei 110, Taiwan and 8 Department of
Neurobiology, University of California San Diego, La Jolla, CA 92093, USA
Received July 27, 2022; Revised August 17, 2023; Editorial Decision August 20, 2023; Accepted September 19, 2023
ABSTRACT GRAPHICAL ABSTRACT
Translational readthrough of UGA stop codons by
selenocy steine-specific tRNA (tRNA Sec ) enabl es the
synthesis of selenoproteins. Seryl-tRNA synthetase
(SerRS) charges tRNA Sec with serine, which is mod-
ified into selenocysteine and delivered to the ribo-
some by a designated elongation factor (eEFSec
in eukaryotes). Here we found that components of
the human selenocysteine incorporation machinery
(SerRS, tRNA Sec , and eEFSec) also increased transla-
tional readthrough of non-selenocysteine genes, in-
cluding VEGFA , to create C-terminally extended iso-
forms. SerRS recogniz es targ et mRNAs through a
stem-loop structure that resembles the variable loop
of its cognate tRNAs. This function of SerRS de-
pends on both its enzymatic activity and a vertebrate-
specific domain. Through eCLIP-seq, we identified
additional SerRS-interacting mRNAs as potential
readthro ugh genes. Moreov er, SerRS ov erexpres-
INTRODUCTION
sion was sufficient to rev ers e premature termina- mRNA translation is a finely tuned process by which pro-
tion caused by a pathogenic nonsense mutation. teins are generated. tRNAs are charged by their cognate
Our findings expand the repertoire of selenoprotein aminoacyl-tRNA synthetase (aaRS) with the specific amino
biosynthesis machinery and suggest an avenue for acid their anticodon deciphers ( 1 ). These charged tRNAs
therapeutic targeting of nonsense mutations using are then used by the ribosome to produce a polypeptide
endogenous factors.
chain following instructions encoded by mRNA. Howev e r,
in order for the ribosome to know where to begin and end,
* To whom correspondence should be addressed. Tel: +1 858 784 8972; Email: xlyang@scripps.edu
Correspondence may also be addressed to Haissi Cui. Email: haissi.cui@utoronto.ca
† The authors wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors.
Pre sent addre ss: Haissi Cui, Department of Chemistry, Univ e rsity of To ronto, To ronto, ON M5S 3H6, Canada.
(cid:2) C The Author(s) 2023. Published by Oxford University Press on behalf of Nucleic Acids Research.
This is an Open Access article distributed under the terms of the Creativ e Commons Attribution-NonCommercial License
(http: // creativ e commons.org / licenses / by-nc / 4.0 / ), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work
is properly cited. For commercial re-use, please contact journals. permissions@oup. com
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
Nucleic Acids Research, 2023, Vol. 51, No. 19 10769
specific translation initiation, elongation, and termination esis, although its exact function is debated ( 25–27 ). VEGFA
factors are needed to facilitate the recognition of signals TR is dependent on heterogeneous nuclear ribonucleopro-
embedded in the mRNA ( 2 , 3 ). In fact, the same mRNA tein HNRNPA2 / B1 binding to a regulatory element follow-
can produce different protein isoforms with vastly differ- ing the stop codon. Howev e r, this mechanism does not di-
ent functions ( 4 ). Regulation by the flanking untranslated rectly explain how the stop codon is suppressed nor why
regions (UTRs), especially the 3 (cid:3) UTR, dictates the propor- serine is ex clusiv e ly incorporat ed at the stop codon position
tions of different protein variants that are synthesized ( 5 ). ( 25 ). We further investigated the mechanism of VEGFA TR
This allows for an additional lev e l of gene product regula- and found that it involved SerRS and select components
tion unrestricted by genetically encoded information. of the selenocysteine incorporation machinery. This func-
Translational readthrough (TR) is one mode of trans- tion was dependent on the conserved catalytic function of
lat ional regulat ion involving the 3 (cid:3) UTR. Suppression of a SerRS and a unique appended domain that appeared in ver-
stop codon leads to TR, upon which additional amino acids teb rates. Moreover, we performed enhanced cross-linking
are attached to the C-terminus of a nascent peptide chain immunoprecipitation (eCLIP) in human cells and identi-
( 6 ). Stop codon suppression is div e rsely utilized in cells – fied other candidate genes beyond VEGFA whose TR may
apart from the generation of protein isoforms by functional be regulated by SerRS. We further showed that ove rex pres-
TR, it is also key to introducing the 21st amino acid of the sion of human SerRS alone was sufficient to alleviate pro-
genetic code, selenocysteine ( 7 ). tein truncation in a cell-based model of a familial nonsense
The incorporation of selenocysteine via TR occurs in all mutation in the tumor suppressor MSH2 that causes high
three domains of life. The first step, strictly conserved across risk for colorectal cancer.
kingdoms, is the aminoacylation of tRNA Sec by seryl-tRNA
synthetase (SerRS, gene name SARS1 ) with a serine ( 8 , 9 ).
The serine residue is further converted to selenocysteine MATERIALS AND METHODS
in the second step, where eukaryotes use a div e rgent sys- Cell culture and constructs
tem from that of bacteria ( 10 , 11 ). In eukaryotes, this step
is catalyzed by two consecutiv e enzymes: O-phosphoseryl- All cells were cultured in a humidified incubator at 37 ◦C
tRNASec kinase (PSTK) and O-phosphoseryl-tRNASec with 5% CO 2 . Human HEK293 and MDA-MB-231 cell
selenium tra nsfera se (SepSecS). The resulting Sec-tRNA Sec lines were purc hased from the American Type Culture
is deliv e red to the ribosome by a designat ed alternat iv e Collection (ATCC, Manassas, VA, USA) and the human
translat ional elongat ion factor, eEFSec, to decode the 293AD cell line was purchased from Agilent (Agilent, Santa
UGA stop codon ( 12 ). In all cases, whether to synthesize Clara, CA, USA). These were cultured in Dulbecco’s Mod-
selenoproteins or to extend specific protein forms, TR must ified Eagle Medium (ThermoFisher Scientific, Grand Is-
be strictly regulated as random disregard of stop codons land, NY, USA) supplemented with heat -inactivat ed fetal
would be highly detrimental. Thus, complex RNA struc- bovine serum (Omega Scientific, Tarzana, CA, USA) to a
tures, which dictat e translat ional speed to allow for the re- final concentration of 10% and 1% Penicillin-Streptomycin
cruitment of nearby factors, regulate the readthrough of the (ThermoFisher Scientific). Tra nsient tra nsfections were
stop codon for selenocysteine incorporation ( 13 ). performed using Lipofectamine 2000 (ThermoFisher Sci-
Numerous diseases are caused by nonsense mutations entific). Human SerRS variants, GlyRS, and TyrRS were
leading to in-frame pre mature termination codons (PTCs); cloned into pCDNA6c-V5 / His6 vector (ThermoFisher Sci-
in fact, about 11% of all genetic lesions that cause human entific), and human full-length SerRS was cloned into
disease can be traced to PTCs ( 14 ). Nonsense mutations pBabe-puro vector (Addgene, pBABE-puro was a gift
can lead to a breadth of symptoms, ranging from dev e lop- from Hartmut Land & Jay Morgenstern & Bob Wein-
mental disorders early in life to increased susceptibility to- berg) (Addgene plasmid # 1764; http://n2t.net/addgene:
wards cancer during adulthood ( 15 , 16 ). Methods to utilize 1764 ; RRID:Addgene 1764) ( 28 ). For mutations in SerRS,
TR as a therapeutic paradigm in these diseases are curre ntly we performed site-directed mutagenesis PCR to obtain the
being evaluated ( 17 ), such as using aminog ly coside drugs SerRS T429A construct. We established MDA-MB-231 cell
( 18 ), nonsense suppressor tRNAs ( 19 , 20 ), and nonsense- lines stably expressing human SerRS mutants by using
mediated mRNA decay (NMD) inhibitors. pBabe-puro ( 28 ) vector-based retroviral infections. Stable
A major concern with these techniques is side effects polyclonal cell lines with either SerRS ove rex pression or
resulting from possible readthrough of non-PTC genes the corresponding control were generated through selection
( 21 , 22 ), necessitating the dev e lopment of targeted therapeu- with puromycin.
tics. Deeper knowledge into the mechanisms of naturally
occurring readthrough would provide clues on how to res-
Protein purification
cue nonsense mutations without the need to introduce for-
eign components. For protein purification, human SerRS was subcloned into
TR has been described for the master angiogenesis reg- pET-20b(+) plasmid (Novagen, Dar mstadt, Ger many) and
ulator VEGFA, a pivotal protein in cancer and dev e lop- expressed in E. coli . The recombinant C-terminal His6-
ment ( 23 , 24 ). Attachment of 22 additional amino acids tagged proteins were purified using Ni-NTA beads (Qiagen,
(Figure 1 A) leads to novel VEGFA functions: instead Valencia, CA, USA) followed by a heparin column and size
of eliciting a pro-angiogenic response as found for the exclusion chromatog rap hy. The purities of the recombinant
prototypical VEGFA variant, the so-termed VEGF-Ax proteins were assessed by Coomassie blue staining and elec-
readthro ugh pro duct no longer stro ngly induces angiog en- trophoresis with 4–12% Bis-Tris Mini gels (ThermoFisher
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
10770 Nucleic Acids Research, 2023, Vol. 51, No. 19
A
VEGFA 165 UGA GCC GGG CAG GAG GAA GGA GCC UCC CUC AGG G UU UCG GGA ACC AGA UCU CUC ACC AGG AAA GAC UGA 3UTR
X A G Q E E G A S L R V S G T R Y L S R K D X
B
UGA VEGFA 3UTR Firefly Luc.
n.s. GAC GGA
n.s. 10 *** 8 6 4 2 0
ytivitca
esareficul evitaleR
Serine (S)
C
5 G C C C G G G
CCA- 3
5 G U G C A
CCA- 3
C G A U
G C G C
G U U A
G G U U G CU AC GG U G C G CU G G G U C A A U G A G C C U U AG C U U C A C G U G A U G A C G U C C G C A U U U G A U U C G A C A G G U UU GA A G AG C G CG CG G G G U A A U G C U U C C A U G C C G G C G G G C C G C U A G C G C U C G C C U U U U A C A G C A A A G G G G G G G A GG U C CC C U C C C G A
Vector SerRS GlyRS TyrRS
U
C
UC A
A
A U
C
UGA
A
A
5 - UGAGCC
G
G U
C
AG - 3
D
Human tRNA-Sec Human tRNA-Ser VEGFA 3UTR
tRNASec
C47j
G47a
3.93 Å
3.96 Å
Asp51 SerRS
E
10
8 6
4 2 0 SerRS - + + + WT WT
GC
AU
Struct.
Mut.
ytivitcaesareficulevitaleR
VEGFA 3UTR Firefly Luc.
**** ****
***
WT G G GC AU G G Struct. Mut. 3 A A A A G
A G A G A
C A G G G G G G G A C C U C C C U C C A G G G G G A A A U C U C U C U C G C G A G G C CG G G A A G A G C A U U C A A A 5 - UGAGCC AG - 3 5 - UGAGCC AG - 3 5 - UGAG AG
-
CMV
UGA
CMV
WT +12nt +24nt
ytivitcaesareficulevitaleR
F G
G G 1.0
A A G G A G C G A A G G ****
G C A G C G A A 1.5 **
A U G C A G WT5’-UGAGC C A C G G G G G C C C U C A 3 G ’ GGUU C A G G G G G A U C C C U C3’ C A G G G G G A C C U C C C 0 1 . . 5 0 0.5
+12 nt5’-UGAAGUAAUAGUAAUGCC AGGGUU G U 0.0 0.0
+24 nt5’-UGAAGUAAUAGUAAUAGUAAUAGUAAUGCC G C A 3 G ’ GGUU WT +12nt +24nt
GC
A
S
U
truct.
Mut.
AFGEV
TWnoitcarF
noititepmoc
retfa dnuob
*
** *
n.s.
Figure 1. SerRS binds to the 3 (cid:3) UTR of VEGFA to facilitat e translat ional re adthrough. ( A ) Scheme of VEGFA downstre am of the first stop codon. VEGFA
mRNA can be read through its first stop codon, resulting in VEGF-Ax with 22 appended amino acids. ( B ) Luciferase assay to quantify VEGFA translational
re adthrough. SerRS overe xpre ssion incre ased VEGFA TR while expression of two other aminoacyl-tRNA synthetases, Gly RS and TyrRS, did not impact
VEGFA TR. ( C ) Upper panel: Secondary structure analysis of VEGFA predicts a stem-loop in the 3 (cid:3) UTR. Comparison between the VEGFA stem-loop
motif and variable loops of tRNA Ser and tRNA Sec . Both variable loops and the VEGFA stem-loop contain G–C base pairs, which are recognized by SerRS
(PDB-ID: 4RQF, lower panel). ( D ) Alignment of human tRNA Sec and tRNA Ser isoacceptor variable loops. The conserved G–C base pairs in each variable
loop are highlighted. ( E ) Disruption of the VEGFA stem-loop motif abrogated SerRS-mediated TR, quantified by luciferase reporter assay. Exchanging G–
C base pairs to A–U reduced TR, as did disrupting the stem-loop structure entirely. ( F ) Addition of 12 or 24 nucleotide spacers between the VEGFA UGA
stop codon and stem-loop reduced TR as quantified by luciferase reporter assay. ( G ) Quantification of competitiv e EMSA results show ing how different
VEGFA constructs compete WT VEGFA mRNA off SerRS. (A–G) (n.s., not significant; * P < 0.05, ** P < 0.01, *** P < 0.001; **** P < 0.0001).
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by guest
on
07 August
2025
Nucleic Acids Research, 2023, Vol. 51, No. 19 10771
Scientific). Protein concentrations were determined by mea- Cross-linking immunoprecipitation (CLIP)
suring absorbance at 280 nm.
CLIP was performed as previously described ( 30 ). Briefly,
2 × 10 8 SerRS-ove rex pressing MDA-MB-231 cells were
Cell fractionation analysis
crosslinked by exposure to short-wave UV light at 300 mJ
Cell fractionation was performed according to a previ- per cm 2 . Cells were harvested by scraping and solubilized
ously described protocol ( 29 ). Briefly, the cells were har- in RIPA buffer (50 mM Tris [pH 7.6], 150 mM NaCl,
vested with 0.25% Trypsin-EDTA, and cells were lysed with 1.0% NP-40, 0.5% sodium deoxycholate, 0.1% SDS) and
swelling buffer (10 mM Tris–HCl pH 7.4, 2 mM EDTA, frozen at −80 ◦C. Immediat ely preceding immu noprecipi-
proteinase inhibitor cocktail (Roche, Basel, Switzerland)). tat ion, lysat es were thawed on ice, vortexed until homoge-
The cytoplasmic fraction was separated by centrifugation neous, and clarified by centrifugation at 16 000 × g for 5
at 800 ×g for 5 min (supernatant) and the pellet containing min in a 4 ◦C refrigerated microcentrifuge. Clarified lysate
nuclear proteins was washed. The nuclear fractions were ex- was transferred to a fresh microcentrifuge tube and pre-
tracted using nuclear extraction buffer (20 mM HEPES pH depleted with protein G Sepharose beads for 30 min at 4 ◦C.
7.6, 300 mM NaCl, 2 mM EDTA, 1 mM 1,4-dithiothreitol, The resin was removed from the clarified lysate by centrifu-
10% glycerol, 1% Triton X-100, protease inhibitor cocktail). gat ion at 5000 × g for 5 min, and the depleted lysate was
SerRS was detected with an anti-SerRS antibody (made transferred to a fresh microcentrifuge tube, followed by the
in-house by immunizing rabbits with recombinant human addition of rabbit polyclonal SerRS antibody or rabbit IgG
SerRS protein). Lamin A / C and (cid:2)-tubulin, nuclear and cy- control. The extracts were incubated for 2 h at 4 ◦C under
toplasmic mark ers, respectiv e ly, were detected by western constant agitat ion. After antibody binding, the immuno-
blot to test the purity of cellular fractions. complexe s were capture d from the lysate by the addition of
pro tein G Sepharo se resin and incubated for 2 h at 4 ◦C un-
Western blot
d
re
e
l
r
e a
a
s
g
e
i
d
ta
b
ti
y
o n
p
.
r o
A
t
f
e
t
i
e
n
r
a
b
se
in
K
di n
d
g
ig
,
e
R
st
N
io
A
n
- p
at
r o
3
t
7
e
◦
in
C
c
i
o
n
m
th
p
e
le
p
x
r
e
e
s
s
w
en
e
c
re
e
Cells were washed with phosphat e-buff ered saline (PBS) of 1% SDS. RNA fragments were TRIzol extracted.
and lysed with cell lysis buffer (20 mM Tris–HCl pH 7.5,
150 mM NaCl, 1 mM of EDTA, 1 mM EGTA, 1% Tri-
eCLIP-seq
ton X-100, 2.5 mM sodium pyrophosphate, 1 mM beta-
glycero phosphate, 1 mM Na
3
VO
4
and pro tease inhibitor eCLIP-seq was performed using the RBP-eCLIP Kit
cocktail). Protein concentration of each sample was quan- (#ECK001, Eclipse Bioinnovations, San Diego, CA).
tified with a BCA Protein Assay Kit (ThermoFisher Sci- 2 ×10 7 MDA-MB-231 cells were used for each of the three
entific). Equal amounts of protein extract were mixed with replicat es at diff erent cell passages. Cell culture medium
SDS loading buffer and boiled at 95 ◦C for 5 minutes. Sam- was replaced with ice-cold PBS and cross-linking was per-
ples were loaded on 4–12% Tris-acrylamide gels, then trans- formed at 254 nM UV with a setting of 400 mJ / cm 2 . Af-
ferred onto polyvinylidene difluoride membranes. Mem- ter cross-linking, cells were scraped, washed, counted, cen-
branes were first blocked with 5% milk, then incubated with trifuged and snap-frozen. eCLIP was performed by follow-
the indicated antibodies, followed by secondary antibody ing the manufacturer’s instructions. Briefly, cells were lysed,
conjugated to horseradish peroxidase. Blots were visualized sonicated using a Bioruptor Pico (Diagenode, Denville,
with an ECL chemiluminescence kit (ThermoFisher Scien- NJ), and digested with DNase and Ambion RNase I, cloned
tific, USA) in a FluorChem M (Proteinsimple). Custom- (#AM2294, ThermoFisher Scientific). Immunoprecipita-
made rabbit anti-human SerRS antibody was made by the tion was performed with mouse monoclonal anti-SerRS an-
Scripps Research antibody core. Monoclonal anti-His6- tibody (#sc-271032, Santa Cruz Biotechnology) bound to
Tag antibody (#HRP-66005) was purchased from Protein- goat anti-mouse IgG magnetic beads (#S1430, New Eng-
tech. Monoclonal anti-V5 antibody (#R960CUS) and poly- land Biolabs). Size-matched input (SMInput) samples were
clonal anti-eEFSec antibody (#PA5-31764) were purchased taken before antibody enrichment. Samples were washed,
from ThermoFisher Scientific. The anti-MSH2 (#2017), adap ters were added, protein-RNA complexes were sepa-
anti-Lamin A / C (#2032), anti- (cid:3)-actin (#3700), and anti- (cid:2)- rated by SDS-PAGE electrophoresis and transferred to ni-
tubulin (#3873) antibodies were purc hased from Cell Sig- trocellulose membranes by wet transfer. The membrane sec-
naling Technology. Monoclonal anti-SBP2 antibody (#sc- tion containing the complexes was cut out and digested
130639) was purchased from Santa Cruz (Santa Cruz, CA, with Proteinase mix supplied by the manufacturer. Result-
USA). ing RNAs were purified and rev e rse transcribed. Result-
ing cDNA was purified and adapters were ligated on the
Lucifera se re porter system ends. cDNA was quantified by qRT-PCR, and libraries were
amplified by PCR. Libraries were gel-purified from a 3%
Firefly luciferase (FLuc) reporters downstream of se- low-melting temperature agarose gel, pooled, analyzed by
quences of interest ( VEGFA , MSH2 , BAK1 , TIMP1 , CFL1 ) Agilent TapeStation, and sequenced on a NextSeq 2000
were transfected (500 ng / well) into HEK293 cells in 24-well (Illumina).
plates using Lipofectamine 2000. Renilla luciferase (RLuc)
(50 ng / well) was co-transfected as a control. After 48 h, cells
eCLIP-seq analysis
were lysed and FLuc and RLuc activity were measure d us-
ing Dual-Luciferase Reporter Assay System (Promega) in a Reads were processed using the Skipper processing pipeline,
Victor3 1420 Multilabel Plate Counter (PerkinElmer). availab le at https://github.com/YeoLab /skipper ( 31 ). In
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
10772 Nucleic Acids Research, 2023, Vol. 51, No. 19
short, re ads were trimmed of adapters with skewer ( 32 ), transcribed to cDNA with M-MLV rev e rse transcriptase
mapped with STAR (2.7.10a alpha 220314) ( 33 ) and PCR- (Promega, Madison, WI, USA) or SuperScript III (Invit-
deduped with UMIcollapse ( 34 ). Binding candidates were rogen). All re al-time PCR re actions were performed using
identified using a tiled window ap proach, wh ere the 5 (cid:3) re ad the StepOnePlus Real-Time PCR system (ThermoFisher
ends (re pre senting the crosslinking site) were counted across Scientific) with SYBR Select Master Mix (Applied Biosys-
ev e nly sized windows for each genic region. Windows were tems) or Power Sybr Green Master Mix (Thermo Fisher).
then binned according to GC content to estimate and ad- Primers used for the PCR reactions are listed in Supple-
just for GC biases, and the comparison of IP reads to corre- mentary Table S1. The PCR reaction started at 95 ◦C for
sponding size-matched input (SMinput) reads were used to 10 min, followed by 45 cycles of 95 ◦C for 20 s and 60 ◦C for
determine enrichment of signal above backgro und. Bro wser 1 min.
tracks were cre ated using IGV ( 35 ). Pa thwa y analysis wa s
performed using Metascape ( 36 ).
RNAi
DNA oligos encoding short-hairpin RNAs (shRNA) de-
Ribosome profiling library construction signed against human eEFSec (5 (cid:3) -GAT CCG CTA GAT
Ribosome profiling libraries were generated as previously GCG GAC ATT CAC ACC TCG AGG TGT GAA TGT
described ( 37 , 38 ) with some minor modifications. Briefly, CCG CAT CTA GCT TTT TTC -3 (cid:3) ), SECISBP2 (5 (cid:3) - GAT
two 10 cm dishes of cells were used for each biological CCG CCA GTC CTT TCC AAA GAA TGC TCG AGC
re plicate, and thre e biological re plicates were pre pare d for ATT CTT TGG AAA GGA CTG GCT TTT TTC -3 (cid:3) ),
each cell line (MDA-MB-231-empty vector, MDA-MB- and tRNASec (5 (cid:3) -GAT CCG TGC AGG CTT CAA ACC
231-SARS). Cell homogenization was performed in 1 ml ly- TGT AGC TCG AGC TAC AGG TTT GAA GCC TGC
sis buffer (20 mM Tris–Cl, pH 8.0, 150 mM NaCl, 5 mM ACT TTT TTC -3 (cid:3) ) were inserted into pLentiLox-hH1 plas-
MgCl
2
, 1 mM DTT, 100 (cid:4)g / ml CHX, 1% (v / v) TritonX- mid, modified from the pLentiLox 3.7 plasmid to contain
100, 50 units / ml Turbo DNaseI). RNase I-treated lysates a H1 promoter (between Xba I and Xho I sites) to driv e
were overlaid on top of a sucrose cushion in 5 ml Beck- the shRNA expression. For non-targeting control shRNA,
man Ultraclear tubes and centrifuged in an SW55Ti ro- we used the sequence 5 (cid:3) -TA A GGC TA T GAA GAG AT A
tor for 4 hours at 4 ◦C at 46 700 rpm to isolate mono- C-3 (cid:3) . Cells were transfected with shRNA plasmids by using
somes. Pellets were resuspended and RNA was extracted Lipofectamine 2000 reagent (ThermoFisher Scientific). 48
using the miRNeasy kit (Qiagen) according to manufac- h post-transfection, cells were subjected to analysis.
turer’s instructions. 26–34 nucleotide RNA fragments were
purified by electrophoresis on a 15% denaturing gel. Linker
Electrophoretic mobility shift assay (EMSA)
addition, cDNA genera tion (first-stra nd synthesis was per-
formed at 50 ◦C for 1 h), circularization, rRNA deple- EMSA was performed as previously described ( 41 ). Briefly,
tion, and amplification of cDNAs with indexing primers the 69 bp RNA oligonucleotides corresponding to the
were performed. Library quality and concentration were as- SerRS binding site on the VEGFA 3 (cid:3) UTR (5 (cid:3) -UGA GCC
sessed using high sensitivity D1000 screen tape on the Ag- GGG CAG GAG GAA GGA GCC UCC CUC AGG
ilent tape station, Qubit 2.0 Fluorometer, and qPCR. All GUU UCG GGA ACC AGA UCU CUC ACC AGG
libraries were pooled and run on HiSeq4000 (SR75). AAA GAC UGA-3 (cid:3) ) and its variants were synthesized.
For MSH2 , a 30 bp RNA oligonucleotide (5 (cid:3) -UCA AAU
GGA GCA CCU GUU CCA UAU GUA CGA-3 (cid:3) ) was
Ribosome profiling analysis
synthesized. The RNA products were annealed and [32P]-
Ribosomal footprints were analyzed as described by Ingolia labeled at the 5 (cid:3) end by T4 polynucleotide kinase (New
et al. ( 37 ) with these modifications: Trimgalore was used to England Biolabs, Ipswich, MA, USA) before desalting us-
trim off adapters and clip the first nucleotide off the 5 (cid:3) end. ing a Sephadex G-25 spin column (GE Healthcare, Pitts-
Reads were then mapped to ribosomal RNA using bowtie2 burgh, PA, USA). The labeled oligonucleotides (5 nM fi-
( 39 ) and unmapped reads were further mapped to the hu- nal concentration) were incubated with recombinant SerRS
man transcriptome (v19) with STAR aligner ( 33 ). Expected at the indicated concentrations (and cold RNA competi-
read length distribution was tested with the R package Ri- tors in competitiv e EMSAs) in binding buffer [20 mM Tris–
boProfiling. To center ribosomes and obtain a list of genes HCl pH 8.0, 60 mM KCl, 5 mM MgCl
2
, 0.1 mg / mL BSA,
with P-sites in their 3 (cid:3) UTR, we used functionalities within 10 ng / (cid:4)l poly(I:C), 1 mM DTT, 5% glycerol] for 1 h at
Ribowaltz ( 40 ) and a custom python script by Scott Adam- room temperature. The samples were loaded on a 5% na-
son, UConn, and Jax Laboratories. tiv e polyacrylamide gel and underwent electrophoresis at
250 V in running buffer (25 mM Tris, pH 8.3, 190 mM
glyc ine). Afterward s, the gel was dried and examined by
Quantitative real-time PCR assay (qRT-PCR)
autora diogra phy.
Total RNA was isolated from cells with TRIzol Reagent
(ThermoFisher Scientific) as a control. For assaying mRNA
stability, cells were tre ated with 5 (cid:4)g / ml actinomycin D
Northern blot
for up to 4 h before isolating total RNA. One microgram Total RNAs of HEK293 cells transfected with shRNA-
( (cid:4)g) of total RNA from each CLIP experiment was rev e rse encoding plasmids were extracted by using TRIzol
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
Nucleic Acids Research, 2023, Vol. 51, No. 19 10773
A 1 152 T 4 2 9 A 481 N L S 514
SerRS TBD CD UNE-S V5
B
n.s.
n.s.
n.s.
***
kDa
70
- SerRS
53 - UNE-S - TBD
41 - CD
30
- -actin
ytivitca
esareficul
evitaleR
10.0
7.5
5.0
2.5
0.0 Vect
F
o
u
r
ll
length UNE-SCD TBD
E F
8 **** Vector
SerRS 6
4 n.s.
2
0
ytivitca
esareficul
evitaleR
UGA UAA
UAG VEGFA 3UTR Firefly Luc.
n.s.
10 ***
8
6
4 n.s.
2
0 Vector SerRSW
S
T erRST429A UGA UAA UAG
ytivitca
esareficul
evitaleR
G
n.s.
**
8 ** ***
6
4
2
0
ytivitca
esareficul
evitaleR
(Invitrogen) according to manufacturer’s instructions with
minor modifications. RNAs were precipitated by adding 2.5
volumes of ethanol and incubating at –20 ◦C overnight. The
RNA samples were subjected to electrophoresis on 10%
TBE-Urea gels (Inv itrogen), fo llowed by electroblotting
to Hybond-N + nylon membranes (GE Healthcare). The
membranes were blocked and incubated with [32P]-labeled
DNA probes at 50 ◦C. The probes used for detecting human
tRNA Sec and U6 snRNA are as follows: 5 (cid:3) - GAA AGG
TG G AAT TG A AC C AC T CTG TCG CTA GAC AGC
TAC AGG TTT GAA GCC TGC ACC CCA GAC CAC
TGA GGA TCA TCC G -3 (cid:3) and 5 (cid:3) -GCA GGG GCC ATG
CTA ATC TTC TCT GTA TCG-3 (cid:3) .
C D
[SerRS] [SerRS]
0.25/0.5/1/2/4 ( M) 0.25/0.5/1/2/4 ( M)
Patient-derived B cell isolation and immortalization
SerRS/RNA SerRS/RNA
Blood samples were collected from the mother (P) and
her three children (F1, M1, M2) (Figure 3 A) at the Na-
N
bi
o
n
n
d
-
in
sp
g
ecific N
bi
o
n
n
d
-
in
sp
g
ecific tional Cheng Kung Univ e rsity Hospital following institu-
Free RNA Free RNA
tional guidelines for re searc h with human subjects (IRB
Protocol Number: B-ER-106–186). B cells were isolated by
Free probe SerRSWT SerRSUNE-S Fr S e e e r R pr S o W b T e (1 M) SerRST429A p b iz e o e a s d i d t b s iv y ( e I i n n s v e c i l u t e r b c o t a g i t o e io n n n ) u . w P si u i n t r h g i fi s C e u d D p e p 1 r r 9 n i m a D t a a y r n n y t a B b fr e o c a e m d ll s s s o P w d a e i n r u e B m i m m b m a u g t o y n r r e t a a t t i l e c -
(3 mM) and TPA (tetradecanoyl phorbol acetate, 40 ng / ml)
CMV treated B95.8 cell for 1.5 h at 37 ◦C to infect them with EBV.
Aliquots of infected cells were collected at diff erent time
points for analysis: day 16, week 3 and week 6 (to ensure that EBV immortalization had occurred).
tRNA alignment
tRNA sequences were retriev e d from GtRNAdb ( 42 , 43 ).
Statistical analyses
shCtrl + - - - -
SerRS OE - + + + + Statistical significance was tested with Student’s t -test us-
shtRNAsec - - + - - sheEFsec - - - + - ing GraphPad Prism (Graphpad Software, Inc.). n.s., not
shSBP2 - - - - + significant; * P < 0.05; ** P < 0.01; *** P < 0.001; ****
kDa 53 - - SerRS P < 0.0001.
70 - - eEFSec
shCtrl + - - - - RESULTS
SerRS OE - + + + + 93 - - SBP2
shtRNAsec - - + - -
sh s e h E S F B s P e 2 c - - - - - - + - + - 41 - - -actin S V e E r G RS FA o v i e n r a e x r p e r p e o s r s t i e o r n s p y r s o t m em o tes tra nslational re adthrough of
Figure 2. SerRS-mediated translational readthrough is dependent on Eswarappa et al. reported that the amino acid serine was
SerRS catalytic activity and selenocysteine incorporation elements. ( A ) incorporated in the position of the UGA stop codon to
Scheme of SerRS domain structure. ( B ) Domain mapping for SerRS- generate VEGF-Ax ( 25 ) (Figure 1 A). As SerRS charges
mediat ed translat ional readthrough. SerRS contains a tRNA-binding do- serine onto tRNA Sec , wh ich can suppress the UGA stop
main (TBD), a catalytic domain (CD) and a domain unique to SerRS
(UNE-S) involved in nucleic acid binding. Expression of V5-tagged SerRS
codon, during the initial step of selenocysteine incorpo-
domains was confirmed by western blot. ( C ) EMSA showing binding of ration, we we re intere sted in investigating whether these
SerRS WT but not SerRS (cid:2) UNE-S to the VEGFA mRNA. ( D ) EMSA show- processes are re lat ed. The effi ciency of stop codon sup-
ing binding of the catalytic mutant SerRST429A to the VEGFA mRNA. pre ssion is incre ased if local concentrations of the charged
( E ) A point mutation in the SerRS catalytic site (T429A), which renders
tRNA are high ( 44 ), so we tested whether increasing the
SerRS cataly tically inactiv e , abolished SerRS translational readthrough
activity. ( F ) Mutation of the UGA stop codon to UA A or UA G abro- lev e ls of SerRS would affect VEGFA TR. Howev e r, de-
gated increased translational readthrough upon SerRS ove rex pression in tection of VEGF-Ax on the protein lev e l is challenging
a VEGFA -based luciferase reporter assay. ( G ) SerRS-mediated TR mea- as the TR ev e nt likely makes up only a small percentage
sured by a VEGFA reporter assay with SerRS ove rex pression. TR is depen-
dent on tRNA Sec and eEFSec, as their knockdown abrogates the increase
of the total VEGFA protein produced and no commer-
in translational readthrough by SerRS ove rex pression. SBP2 knockdown
cial antibodies are available against the appended amino
does not affect TR. Knockdown was verified by western blot. (A–G) (n.s., acid sequence to specifically detect the VEGF-Ax isoform.
not significant; ** P < 0.01; *** P < 0.001; **** P < 0.0001) To facilitate VEGF-Ax detection, we used a luciferase
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
10774 Nucleic Acids Research, 2023, Vol. 51, No. 19
Vecto S r er R G S l - y V R 5 T S y - r V R 5 S- V5 3
Anti-V5 2
1
-actin 0
Vector
Ser
R S
Gly
R S
Tyr
R S
ytivitcaesareficulevitaleR
I
II
III
1.5
1.0
0.5
0.0
P F1 M1 M2
F S612X CMV MSH2 Firefly Luc.
Stem-loop n.s. n.s. **
levelANRm2HSMevitaleR
A B
S612X
DNA-binding MSH3/MSH6 MutL homologs
domain interaction domain interaction domain
MSH2 Protein (934aa ; 104.7kDa)
P
E
C C SerRS Conc. ( M)
A U
F1 M1 M2 C G 0 1 2 4
G U
A U
GG CC
C D GG CC
U A
Stop A U SerRS-MSH2
5 - UGAA AUGUACGA - 3
n.s. P F1 M1 M2
MSH2-S612X
n.s. n.s. - MSH2 C C
A U
C G
G U
A U
GG CC
- SerRS GG CC
U A Stop A U Free RNA
- -actin 5 - UCAA AUGUACGA - 3
MSH2-WT
G X X+ Vec X to + r Ser X R + S G - V ly 5 R X S + - T V r 5 p R S- V5 WT S612 S612 S612 S612 S612
H2- H2- H2- H2- H2- H2-
S S S S S S M MM M M M 93 70 Anti-V5 53
130
93 MSH2
70
53 -actin
Figure 3. SerRS-mediated translational readthrough rescues protein lev e ls reduced by a cancer-causing nonsense mutation found in a Taiwanese family.
( A ) Pedigree of the Taiwanese family with a hereditary MSH2 nonsense mutation (p.S612X, annotated as S611X in a previous study ( 16 )). Female carriers
are indicated by filled black circles, male carriers by filled black squares, and affected individuals (diagnosed with gastrointestinal cancers) by arrows. Open
circ les and square s indicate family members carrying the WT MSH2 gene. ( B ) Domain structure of MSH2. The monoallelic p.S612X nonsense mutation is
located in the domain that interacts with MSH3 and MSH6. ( C ) qRT-PCR of MSH2 mRNA lev e ls in patient-deriv e d B cells ( n = 3) showed no difference
between mutant carriers and wild type individuals. ( D ) Western blot result of MSH2 protein levels in patient-derived B cells showed reduced full-length
MSH2 protein in mutant carriers. ( E ) RNA structure prediction of the stem-loop motif following the p.S612X mutation on MSH2 that is recognized by
SerRS. An EMSA showed SerRS binding to the stem-loop structure of MSH2 . ( F ) Luciferase assay to quantify MSH2-S612X translational readthrough.
Signal amplification was obtained from a reporter containing the N-terminal MSH2-S612X sequence including the 30 nucleotides downstream of the
pre mature stop codon, followed by the coding sequence for luciferase. SerRS ove rex pression increased MSH2-S612X translational readthrough while
expression of two other aminoacyl-tRNA synthetases, Gly RS and TyrRS, did not impact MSH2-S612X translational readthrough ( n = 3). ( G ) Western
blot results showing SerRS-mediated rescue of full-length MSH2-S612X protein lev e ls after ove rex pression of SerRS, GlyRS and TrpRS with MSH2-S612X
in HEK293 cells. (A–G) (n.s., not significant; ** P < 0.01).
reporter assay to allow sensitiv e detection and quantifi- SerRS re cognizes stem–loop structure s re sembling its cog-
cation of TR ev e nts while controlling for other regula- nate tRNAs
tory eff ects that might aff ect general protein synthesis
As unre gulated re adthrough of genes caused by the expres-
(Figure 1 B). Expression of VEGFA from a plasmid un-
sion of a constitutiv e ly ex pressed protein would be highly
der a CMV promoter additionally enabled us to easily ex-
undesirabl e, we inve stigated whether SerRS-dependent
change regulatory elements in the mRNA and avoided in-
readthrough would be specific to VEGFA transcripts due
terference with potential SerRS-dependent transcriptional
to the recognition of internal RNA sequences or struc-
regulation of VEGFA ( 45 ). Ove rex pression of SerRS in
293AD cells increased TR by ∼7-fold, while ove rex pres-
tures. SerRS does not use the tRNA anticodon as an iden-
tity element for recognition ( 46 ). Instead, a long variable
sion of other aaRSs (gly cyl-tRNA synthetase, Gly RS,
loop unique to both tRNA Ser and tRNA Sec is recognized
GARS1 , and tyrosyl-tRNA synthetase, TyrRS, YARS1 ) did
by SerRS ( 9 , 46 , 47 ) (Figure 1 C). Recognition of tRNA Sec
not alter TR significantly (Figure 1 B, Supplementary Fig-
by SerRS is mediated by contacts with a G-C base pair in
ure S1A), demonstrating that SerRS specifically induced
the middle of the variable loop ( 9 ) (Figure 1 C). Conserved
VEGFA TR.
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
Nucleic Acids Research, 2023, Vol. 51, No. 19 10775
G-C base pairs are also found in the tRNA Ser variable loop to bind the VEGFA mRNA, which in turn mediates TR
( 43 ) (Figure 1 C and D). We found a stem-loop structure (Figure 2 C). Consistently, expre ssion of the catalytic do-
following the regular UGA stop codon in the 3 (cid:3) UTR of main alone had no effect on TR (Figure 2 B). To investi-
VEGFA mRNA that shared similarities with the variable gate whether the catalytic activity of SerRS is re quire d for
loop in tRNA Ser and tRNA Sec (Figure 1 C and Supplemen- SerRS-mediated TR, we mutated threonine 429 to alanine
tary Figure S1B). Specifically, two G–C base pairs are simi- in full-length SerRS (SerRS T429A ). The mutation is located
larly located in the stem-loop compared with the conserved near the activ e site in the catalytic domain (Supplementary
G-C pairs in the variable loops of tRNA Ser and tRNA Sec Figure S2), which disrupts tRNA charging ( 45 , 48 ). Despite
(Figure 1 C). To test the importance of the stem-loop struc- the intact binding of SerRS T429A to the VEGFA stem-loop
ture and the G–C base pairs for TR, we introduced muta- (Figure 2 D), ove rex pression of SerRS T429A did not lead to
tions in the VEGFA mRNA stem-loop wh ich substituted incre ased TR (Figure 2 E), demonstrating that enzymatic
these two G–C base pairs for A–U pairs or with mutations activity is essential for SerRS-mediated TR. These experi-
that were predicted to disrupt stem-loop formation entirely ments suggested that to stimulate TR, not only the catalytic
(Figure 1 E and Supplementary Figure S1B). Substitution activity and tRNA-binding capacity of SerRS are required,
of the two G–C base pairs with A-U or disruption of the but also the vertebrate-specific UNE-S domain, possibly
stem-loop structure both significantly reduced the SerRS- through its capacity to bind nucleic acids other than tRNA.
mediated increase of VEGFA TR using our luciferase TR
assay (Figure 1 E). Through competitiv e EMSA analysis, we SerRS-mediated translational readthrough utilizes tRNA Sec
confirmed that SerRS binds to the VEGFA mRNA and that
and eEFSec for stop codon suppression
the A–U and structural mutants displayed weaker ability to
compete off WT VEGFA mRNA from SerRS (Figure 1 G As we could establish that SerRS binding directly to mRNA
and Supplementary Figure S1C), demonstrating that bind- and its catalytic activity were re quire d for TR, we next in-
ing by SerRS was dependent on stem-loop G–C base pairs vestigated the mechanism. VEGFA contains a UGA stop
in its target mRNA . Additionally , we introduced either a 12 codon, so we tested whether SerRS-dependent TR would
or 24 nucleotide spacer between the UGA stop codon and tolerate any of the three stop codons. Mutating UGA to
the stem-loop, both of which also decreased the efficiency of either of the other two stop codons, UA A or UA G, ab ro-
TR (Figure 1 F). In contrast to the A-U and structural mu- gated SerRS-induced TR in our system (Figure 2 F). This
tants, extending the distance between stop codon and the suggests that SerRS-mediat ed TR is highly specific to UGA
stem-loop either did not affect or improved WT VEGFA and likely dependent on stop codon suppression by specific
mRNA binding to SerRS (Figure 1 G and Supplementary tRNA s recog nizing the UGA stop codon.
Figure S1C), despite the observed reduction of TR in cells SerRS initiates the first step in the incorporation of se-
(Figure 1 F). This strongly suggests that the close proximity lenocysteine by charging tRNA Sec , wh ich decodes UGA
between the SerRS binding site and the stop codon is also stop codons. If the mechanism behind SerRS-dependent
important for TR. To further rule out the possibility that TR is shared with selenocysteine incorporation, reduction
the observed TR increase was due to a mRNA stabilization of tRNA Sec should sev e rely impair SerRS-dependent TR.
effect of SerRS binding, we performed qPCR of the VEGFA We used a shRNA directed against tRNA Sec to reduce the
reporter mRNA with and without SerRS ove rex pression tRNA lev e l ( 49 ) (Supplementary Figure S3A), which in-
(Supplementary Figure S1D). No significant difference in deed strongly reduced SerRS-dependent TR (Figure 2 G).
the lev e ls and the stability of VEGFA reporter mRNA be- Selenocysteine incorporation is driv e n by a complex ma-
tween the two conditions was observed, suggesting SerRS chinery of factors that enables stop codon suppression by
does not increase TR by mRNA stabilization. tRNA Sec . A specific elongation factor, eEFSec, competes
with termination factors and employs a mechanism distinct
from other elongation factors ( 50 ). Knockdown of eEF-
Tr a nslational re adthrough re lies on SerRS aminoacylation
Sec also significantly impaired TR, suggesting that SerRS-
function and a vertebrate-specific domain
dependent TR does rely on the same components as seleno-
Using the luciferase assay, we further mapped the involve- cysteine incorporation (Figure 2 G). Knockdown of either
ment of different domains of SerRS in TR. SerRS consists tRNA Sec or eEFSec also significantly reduced the lev e l of
of a N-terminal tRNA-binding domain (TBD) that binds TR in the absence of SerRS ove rex pression (Supplementary
to the long variable loop of its cognate tRNAs, a catalytic Figure S3B), further confirming that the mechanism also
domain (CD) containing the activ e site, and a C-terminal occurs in cells with an endogenous lev e l of SerRS.
UNE-S domain (Figure 2 A), which is an evolutionarily new During selenocysteine incorporation, the specific site of
addition found in vertebrate SerRS from fish to humans stop codon suppression is determined by SBP2, which rec-
( 45 ). We found both the tRNA-binding and UNE-S do- ognizes the SECIS, an in-cis RNA stem-loop motif in the
mains are necessary for mediating TR, as expression of 3 (cid:3) UTR of selenoprotein mRNAs. SBP2 also interacts with
truncated SerRS lacking either domain did not stimulate the ribosome stalled at the upstream UGA stop codon,
TR (Figure 2 B). Unlike the conserved tRNA-binding do- which brings the eEFSec / Sec-tRNA Sec complex via its
main and catalytic domain, the UNE-S domain does not binding to the SECIS to the proximity of the UGA codon
contribute to tRNA binding and is dispensable for aminoa- ( 51 ). Howev e r, knockdown of SECISBP2 (SBP2 gene) did
cylation but mediates binding to other nucleic acids, for not reduce TR significantly as opposed to knockdown
example genomic DNA ( 45 ). Through EMSA, we deter- of tRNA Sec or EEFSEC (eEFSec gene) (Figure 2 G and
mined that the UNE-S domain is also necessary for SerRS Supplementary Figure S3B). Therefore, SerRS-mediated
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
10776 Nucleic Acids Research, 2023, Vol. 51, No. 19
TR shares some but not all key factors for selenocysteine bound by SerRS through PCR and Sanger sequencing
incorporation. (Supplementary Table S2). Enrichment of the so identified 9
genes and VEGFA could be verified by qRT-PCR (Supple-
SerRS rescues full-length protein expression by suppressing a mentary Figure S5A). Of these genes (including VEGFA ),
pathogenic nonsense mutation in MSH2 four contained a UGA stop codon. To verify that SerRS
ove rex pression could lead to increased readthrough, we de-
To further explore the applicability of our observations to
veloped the luciferase reporter assay fo r one of the identi-
disease-causing nonsense mutations, we focused on a family
fied target genes with a UGA stop codon, BAK1 . BAK1,
with an autosomal dominant nonsense mutation in MSH2
a mitochondrial outer membrane protein, also possesses a
( 16 ) (Figure 3 A). The MSH2 gene encodes for a DNA mis- stem-loop motif in its 3 (cid:3) UTR (Supplementary Figure S5B).
match repair protein, and the loss of one copy of this gene
In line with our findings for VEGFA , SerRS ove rex pres-
is sufficient to cause microsatellite instability and increase
sion increased TR of BAK1 over 14-fold while ove rex press-
cancer risk, especially of hereditary nonpolyposis colorec-
ing other aaRSs did not affect TR (Supplementary Fig-
tal cancer (HNPCC) or Lynch syndrome ( 52 ). The proband
ure S5B). These findings re inforc ed that SerRS binding to
(III-M1) and the proband’s mother (II-P) both carry a
heterozygous (c.1835C > G) mutation, introducing a stop
mRNA stem-loop motifs is a common mechanism to pro-
mote TR in different genes.
codon where a serine should be (p.Ser612X, annotated as
While the CLIP method was able to identify SerRS-
S611X in the original case report ( 16 )). We confirmed the
bound mRNAs, it could not pinpoint where SerRS bound
mu tation independently by Sanger sequencing, wh ile se-
and was limited in the number of genes that could feasi-
quencing of the proband’s siblings (III-F1, III-M2) revealed
bly be identified. To unbiasedly search for mRNAs that are
no mutation (Supplementary Figure S4A). The nonsense
mutation falls within the MSH3 / MSH6 interaction domain
potentially regulated by SerRS and their binding sites, we
perfo rmed enhanced CLIP fo llowed by next-generation se-
and truncation of the protein would likely result in loss-
quencing of SerRS-bound RNA targets (eCLIP-seq).
of-function (Figure 3 B). qRT-PCR analysis of the affected
Reads from triplicate eCLIP-seq experiments in MDA-
proband and parent compared to the proband’s unaffected
MB-231 cells were passed through a CLIP-seq analysis
sibl ings rev e aled no significant differences in MSH2 mRNA
pipeline, Skipper ( 31 ), to obtain a set of 50613 sites with
lev e ls (Figure 3 C), suggesting that nonsense-mediated decay
significant SerRS binding over size-matched input ( q < 0.2),
is not engaged. Howev e r, western bl otting of MSH2 from
corresponding to 7102 unique RNAs (Figure 4 A and Sup-
immortalized patient-deriv e d B cells showed reduced full-
plementary Table S3). Most of the genes identified in the
length protein in the individuals with the mutation (Fig-
original CLIP experiment (Supplementary Table S2) were
ure 3 D). Truncated MSH2 could not be detected in patient
also found in this new eCLIP set (6 / 9 genes). All tRNAs for
B cells, possibly due to degradation caused by instability.
serine and selenocysteine were found as top hits when call-
RNA structure pre diction of the nucleotides directly follow-
ing repeat elements, confirming the suitability of the eCLIP
ing the aberrantly introduced stop codon rev e aled the for-
technique and Skipper analysis pipeline (Supplementary
mation of a G–C-containing stem-loop structure (Supple-
Figure S6A and Supplementary Table S4). Although most
mentary Figure S4B), and an EMSA performed with puri-
binding sites were found within the coding sequence of mR-
fied SerRS and the 30 nucleotides of MSH2 mRNA con-
NAs, including three binding sites in MSH2, many sites
taining the stem-loop structure confirmed binding (Figure were also found within 5 (cid:3) UTRs and 3 (cid:3) UTRs (Supplemen-
3 E). We dev e loped a luciferase reporter system for MSH2
tary Figure S6B). Further refinement to include only sites
readthrough, similar to the one described for VEGFA : the
within 50 nucleotides of a protein-coding UGA stop codon
N-terminal sequence of MSH2 including the p.Ser612X
and with q < 0.05 led to the identification of 408 sites, cor-
mutation and the 30 nucleotides downstream of mutation
responding to 365 unique mRNAs (Figure 4 A and Supple-
were placed under a CMV promoter, followed by a lu-
mentary Table S5). Of note, VEGFA appeared in this list.
ciferase re porter (Figure 3 F). This was transfected into
As further validation that SerRS mediates physiological TR
293AD cells along with SerRS or other aaRSs as controls.
ev e nts we compared our gene set with previously reported
Ove rex pression of SerRS, but not of the other aaRSs, led
readthrough ev e nts. We saw a sizeabl e ove rlap with a prev i-
to increased translational readthrough of the MSH2 re-
ous set of genes with TR confirmed through ribosome pro-
porter (Figure 3 F). This was confirmed through western
filing by Dunn et al. ( 6 ), with 27 / 42 genes appearing in our
bl ot, where ove rex pression of SerRS increased full-length
eCLIP set and 5 / 27 of those genes having SerRS occupancy
MSH2 expression and simu ltaneously reduced the trun-
within 50 nucleotides of the UGA stop codon ( RHOA , TM-
cated form (Figure 3 G). These experiments suggest that
BIM6 , PHPT1 , TIMP1 , SQSTM1 ) (Figure 4 B and Supple-
SerRS ove rex pression could rescue full-length MSH2 trans-
mentary Table S6).
lation in this single model of a clinically relevant nonsense
To test whether other mRNAs that appear in our eCLIP
mutation.
list beside VEGFA are subject to TR, we selected CFL1
and TIMP1 to perform the same luciferase readthrough
SerRS translational readthrough affects a specific gene set
reporter assay that we did for VEGFA . Both CFL1 and
As SerRS recognized stem-loop structures, we asked TIMP1 contain a stem-loop structure containing G-C base
whether TR of other genes could be similarly regulated pairs immediately after the UGA stop codon (Figure 4 C).
by SerRS. We enriched SerRS-bound mRNAs using cross- We saw a similar increase in CFL1 readthrough as we did
linking immunoprecipitation (CLIP) in human breast can- for VEGFA , and a smaller but significant increase in TR for
cer MDA-MB-231 cells and manually identified genes TIMP1 (Figure 4 C). Using Metascape ( 36 ), we performed a
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
Nucleic Acids Research, 2023, Vol. 51, No. 19 10777
A
C
CCU
5
A C
A A
3 4 A A C C C A C C C C U C A U C A C U U A
2 A A U C CC U C C C C C U U C C C C A
C C U A C
U U A C
C C C
5 5 5
VS
r erRS TyrRS
VS
r erRS TyrRS
VS
r erRS TyrRS VEGFA 3UTR CFL1 3UTR TIMP1 3UTR
D
RHO TP seeffet rs(RHSA 9525 )
Met b is fRNA(RHSA 953 54)
Mit ti e y e( O: 2 )
VE FAVE FR2sign ingp thw y(WP3 )
Neutr phidegr nu ti n(RHSA6 9 695)
Nerv ussyste deve p ent(RHSA96 5 )
Ceu rresp nsest stress(RHSA2262 52)
Rib nu e sidetriph sph te et b i pr ess( O: 9 99)
Peptide et b i pr ess( O: 65 )
Ad ptivei unesyste (RHSA 2 2 )
Mit h ndri n rg niz ti n( O: 5)
2 4 6
g (qv ue)
eR
B
F RHOA 4
365 unique TMBIM6
PHPT1
TIMP1
SQSTM1
***
***
***
Figure 4. eCLIP-seq identifies a set of SerRS-bound RNAs that includes other translational readthrough genes. ( A ) A schematic showing the eCLIP-seq
analysis workflow and filtering steps to reach the final list of 408 SerRS-bound windows within 50 nucleotides of a UGA stop codon ( q < 0.05). Created
with BioRender.com. ( B ) Venn diagram showing the overlap between the final 365 unique genes found in our eCLIP set (from 408 windows) with the
confirmed translational readthrough genes identified in human foreskin fibroblasts by Dunn et al. ( 6 ). ( C ) Luciferase reporter assays were performed for
the hits CFL1 and TIMP1 , using VEGFA as a positiv e control. All three RNAs possess a G–C base pair-containing stem-loop after the canonical UGA
stop codon. ( D ) Gene Ontology (GO) analysis was performed on RNAs from the final list of 408 windows. The number of genes enriched in each pathway
are shown along with the overlapping translational readthrough genes from Figure 4 B and our experimentally confirmed translational readthrough genes
in Figure 4 C. (A–D) (n.s., not significant; *** P < 0.001).
gene ontolog y (GO) analy sis to determine cellular pathways Collectiv e ly, our dat a indicat e a ro le for SerRS in contro l-
that may be enriched by bound RNAs ( q < 0.05, window ling translational readthrough for a subset of genes defined
within 50 nucleotides of UGA). We found that Rho GTPase by their mRNA structure and stop codon usage.
effectors, metabolism of RNA, cell cycle, and VEGFA–
VEGFR2 signaling pathways were enriched (Figure 4 D and
DISCUSSION
Supplementary Table S7). We highlighted VEGFA , CFL1 ,
and the 5 readthrough genes from Dunn et al. ( 6 ) that over- We showed that SerRS can bind and mediate TR of specific
lapped with our set (Figure 4 B) in each related GO pathway mRNAs by recruiting certain components of the seleno-
(Figure 4 D). cysteine incorporation machinery, including tRNA Sec and
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
10778 Nucleic Acids Research, 2023, Vol. 51, No. 19
the corresponding elongation factor, eEFSec, for ribosomal 1 F). Howev e r, binding strength is still important as shown
deliv e ry. Our data suggests that SerRS binds to specific by the GC > AU and structural mutat ions that reduce
stem-loop motifs in the 3 (cid:3) UTR that mimic the long variable SerRS binding and consequently TR efficiency (Figures 1 E
loop (a major identity element) of tRNA Ser and tRNA Sec and G). SerRS binds to many distinct RNA species, and
(Figure 1 ) and that the catalytic activity and UNE-S do- having TR efficiency be modified by binding strength, bind-
main of SerRS are necessary for mediating TR (Figures 2 B ing location, and catalytic activity allows greater regulation
and C). of SerRS-mediated TR.
Not all components of the selenocysteine incorporation Other RNA binding factors have been identified as
machinery are needed for SerRS-mediated TR. SerRS per- regulators of VEGFA TR, such as HNRNPA2 / B1 ( 25 ).
forms the same function in both mechanisms to initiate Eswarappa et al. discovered that HNRNPA2 / B1 is criti-
the charging of tRNA Sec with serine ( 53 ). For selenocys- cal for VEGFA TR through interactions with translating
teine incorporation, this is followed by the conversion of ribosomes that prev e nt recruitment of eukaryotic trans-
Ser-tRNA Sec to Sec-tRNA Sec through PSTK and SepSecS lat ion terminat ion factor 1 (eRF1) to the stop codon.
( 11 ). SepSecS forms a complex with the enzymes that pro- The consensus binding sequence for hnRNPA2 / B1 (5 (cid:3) -
vide activated selenium ( 54 ), suggesting a supramolecular GCCAAG GAG CC-3 (cid:3) ) falls within the stem-loop structure
hub for the conversion of Ser-tRNA Sec to Sec-tRNA Sec . of VEGFA that we also identified as critical for binding by
To avoid nonspecific extension of off-target proteins for SerRS. Mutations in the hnRNPA2 / B1 region which abro-
selenocysteine incorporation, mRNAs containing a SE- gated TR could also affect stem-loop formation for SerRS
CIS are re cog nized by SBP2, wh ich allows recruitment of binding. It is possible that hnRNPA2 / B1 and SerRS bind
Sec-tRNA Sec -bound eEFSec ( 55 ). While we showed that to VEGFA mRNA at different stages of TR (blocking
eEFSec and tRNA Sec are important for SerRS to medi- recruitment of the termination factor versus increasing
ate TR, SBP2 is not, suggesting that SerRS and SBP2, local tRNA concentrations) or that hnRNPA2 / B1 and
with their corresponding mRNA binding motifs, dictate SerRS promote TR through cooperativ e binding. In con-
mRNA selectivity and allow the separation of the two TR trast to other RNA -binding proteins, only SerRS directly
mechanisms. generates the necessary aminoacylated suppressor tRNA,
The SECIS is quite complex in humans, consisting of a thereby enabling translation to continue through the stop
lower stem, central core, upper stem, and apical loop ( 55 ). codon.
In contrast, SerRS recognizes a comparativ e ly simple G–C- The 3 (cid:3) UTR stem-loops in target mRNA s mu st compete
containing stem-loop motif mimicking the variable loop of with high endogenous lev e ls of tRNA Ser for SerRS bind-
tRNA Ser and tRNA Sec , suggesting the need for further safe- ing. In addition, tRNA Sec mu st be both locally available and
guard mechanisms. The RNA sequence surrounding the aminoacylated over tRNA Ser despite a slight pre fere nce of
stop codon impacts the efficiency of TR, partly due to inter- SerRS for tRNA Ser over tRNA Sec ( 47 ). We speculat e that
actions between the translational machinery and structural reducing the availability of tRNA Ser could contribute to the
features of the mRNAs ( 56 ). mRNAs with a stem-loop must success of SerRS-mediated TR. As tRNA lev e ls are re gu-
be accessible to SerRS, so we speculate that SerRS competes lated during stress conditions by selectiv e cleavage ( 58 ) and
with other RNA binding proteins for these structures or retroactiv e nuclear import ( 59 ), SerRS-mediated TR might
that exposure of these stem-loops during translation only offer an additional pathway for cells to adapt to stress by
occurs under specific conditions. SerRS is activ e as a ho- altering protein variant production. Strict regulation is nec-
modimer (Supplementary Figure S2), so tethering one sub- essary to allow SerRS-regulated TR to be both gene-specific
unit to the mRNA close to the UGA stop codon would still and potentially responsiv e to the present state of the cell de-
allow the other subunit to recognize and charge tRNA Sec . spite the ubiquitous expression of SerRS as an integral part
The resulting high local concentration of Ser-tRNA Sec may of the translation machinery.
enable suppression of the UGA stop codon and TR of spe- Recently, studies into aaRSs and their noncanonical roles
cific mRNAs. Having high local concentrations of an aaRS have ex panded the involve ment of aaRSs in regulatory pro-
for the charging of suppressor tRNAs has been shown to be cesses, with sev e ral of these new functions being mecha-
favorable for efficient stop codon suppression ( 44 ). In addi- nistically involved in the regulation of translation ( 60–63 ).
tion, while binding ( k
on
) is comparable between eEFSec and SerRS is especially suitable to enable stop codon suppres-
Sec-tRNA Sec versus Ser-tRNA Sec , the eEFSec-Ser-tRNA Sec sion as it does not use the anticodon of its cognate tRNA
complex dissociates faster ( k
off
) than Sec-tRNA Sec , further as an identity element ( 64 , 65 ), thus it can be repurposed to
suggesting that high local concentrations of Ser-tRNA Sec recog nize tRNA s with different anticodons with more ease
might be crucial ( 57 ). Recently, it was shown by another than other aaRSs. In addition, aaRSs acquired additional
group that eEFSec can enable UGA readthrough using Ser- domains during evolution which allow for new interactions
tRNA Sec , supporting our mechanism ( 51 ). and functionalities ( 66 ). SerRS contains a unique domain at
Based on our data, readthrough efficiency is determined its C-terminus (UNE-S), which arose in vertebrates ( 45 ) and
by more factors than just the strength of SerRS binding to is necessary for TR, presumably by enabling SerRS to inter-
target mRNA. SerRS also needs to be cataly tically compe- act with target mRNAs (Figure 2 B and Supplementary Fig-
tent (Figure 2 E) and the binding of SerRS needs to occur ure S2). This suggests that the regulation of TR by SerRS
close to the stop codon, as demonstrated by reduced TR ef- is ev olutionarily new , ev e n though prototypes of the seleno-
ficiency when spacers are introduced between the UGA stop cysteine machinery trace back to archaea. It is possible that
codon and the SerRS-binding stem-loop structure (Figure the pre-ex isting involve ment of SerRS in the selenocysteine
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
Nucleic Acids Research, 2023, Vol. 51, No. 19 10779
biosynthesis machinery and the emergence of the UNE-S SUPPLEMENTA RY DAT A
domain enabl ed ve rtebrate SerRS to dev e lop the function
Supplementary Data are available at NAR Online.
in mediating TR as described herein. It is worth noting
that the appearance of the UNE-S domain has already been
linked to the emergence of a closed circulatory system ( 45 ) ACKNOWLEDGEMENTS
and indeed SerRS is necessary for functional vascular de-
We thank the Scripps Research next generation sequencing
ve lopment ( 45 , 67 ). Prev ious findings linked SerRS to the
and bioinformatics core for eCLIP sequencing and prelim-
transcriptional regulation of VEGFA , the master regulator
inary data analysis and the antibody core for the genera-
of angiogenesis ( 45 , 67 ). We suggest that vertebrate SerRS
tion of SerRS antibody used for CLIP. We thank Dr. Paul
may further regulate angiogenesis via its ability to influence
Schimmel for valuable input and support and Dr. Paul Fox
VEGFA translational readthrough.
for providing material for preliminary experiments and dis-
To obtain additional evidence for SerRS-mediated
cussion. We thank Dr. Kristopher W. Brannan for guidance
readthrough in MDA-MB-231 cells, we performed ribo-
on performing and analyzing the eCLIP-seq experiments.
some profiling on control MDA-MB-231 cells and SerRS- Scripts for the calculation of ex pected / observe d were pro-
ove rex pressing MDA-MB-231 cells. Howev e r, no signifi-
vided by Dr. Scott Adamson and we thank him for his ad-
cant difference in ribosome occupancy with SerRS over-
vice on ribosome profiling analysis.
expression was detected for most genes, including VEGFA
(Supplementary Tabl e S8), possibl y due to insufficient read
depth. FUNDING
To determine whether our eCLIP-seq hits overlapped National Institutes of Health [R35 GM139627 to X.-L.Y.,
with prev iously publ ished mechanisms of TR, we looked HG004659, HG009889 to G.W.Y.]; Deutsche Forschungs-
at the overlap between our set and the set described in gemeinschaft [327097878 to H.C.]; Human Frontier Science
Loughran et al. ( 68 ). This study identified UGA CUAG as Program [LT000207 to H.C.]; Z.L. and J.W. were supported
a ve rtebrate-conserve d motif that enabl ed TR of a set of by a fellowship from the Nat ional Foundat ion for Cancer
23 human genes. Some of the hits identified in Loughran Research; G.W.Y. was partially supported by an Allen Dis-
et al. appeared in our broader set of eCLIP hits (q < 0.2, tinguished Inve stigator Award , a Paul G. Allen Frontiers
CDKN3, CGGBP1, DCTN3, PHF19), but none of these Group advised grant of the Paul G. Allen Family Founda-
appeared in our more stringent list ( q < 0.05, binding within tion. S.L.A. is an investigator of the Howard Hughes Med-
50 nucleotides of UGA). We also do not see an enrich- ical Institute. Funding for open access charge: National In-
ment of the UGA CUAG motif in our dataset. There fore , stitutes of Health [R35 GM139627].
it appears that the TR mediated by SerRS and components Conflict of interest statement. G.W.Y. is a co-founder, mem-
of the selenocysteine incorporation machinery acts distinc- ber of the Board of Directors, on the scientific advisory
tiv e ly from the phenomenon described in Loughran et al. board, equity holder, and paid consultant for Locanabio
Taken together we here describe a novel mechanism for and Eclipse BioInnovations. G.W.Y. is a visiting professor
the regulation of physiological translational readthrough at the National Univ e rsity of Singapore. G.W.Y.’s interests
of specific mRNAs through direct provision of suppressor have been reviewed and approved by the University of Cali-
tRNA by a tRNA synthetase. TR has powerful implica- fornia, San Diego in accordance with its conflict-of-interest
tions for therapeutics designed to counteract PTCs. Most policies. The authors declare no other competing financial
current approaches to promote TR of genes with nonsense interests.
mu tations rely on engineered RNA s or chemical modifiers,
potentially promoting TR of undesired mRNAs. While our
findings here might be more limited in their direct appli- REFERENCES
cability as a therapeutic option due to the need for natu- 1. Schimmel,P.R. and S o¨ll,D. (1979) Aminoacyl-tRNA synthetases:
rally occurring RNA motifs, the mechanism makes use of general features and recognition of transfer RNAs. Annu. Rev.
endogenous components. The findings discussed here un- Biochem. , 48 , 601–648.
2. Jackson,R.J., Hellen,C.U.T. and Pestova,T.V. (2010) The mechanism
cover another aspect of how cells dev e loped complex trans-
of eukaryotic translation initiation and principles of its regulation.
lational control by coordinating mRNA and protein fea- Nat. Rev. Mol. Cell Biol. , 11 , 113–127.
tures together to achiev e functional readthrough. Insights 3. Schuller,A.P. and Green,R. (2018) Roadblocks and resolutions in
such as these may improve therapeutics by leveraging the eukaryotic translation. Nat. Rev. Mol. Cell Biol. , 19 , 526–541.
4. Zerbino,D.R., Achuthan,P., Akanni,W., Amode,M.R., Barrell,D.,
natural systems already in place to manage TR in cells,
Bhai,J., Billis,K., Cummins,C., Gall,A., Gir o´n,C.G. et al. (2018)
making them more efficient and less prone to off-target
Ensembl 2018. Nucleic Acids Res. , 46 , D754–D761.
effects. 5. Mayr,C. (2017) Regulation by 3’-untranslated regions. Annu. Rev.
Genet. , 51 , 171–194.
6. Dunn,J.G., Foo,C.K., Belletier,N.G., Gavis,E.R. and Weissman,J.S.
(2013) Ribosome profiling rev e als pervasiv e and regulated stop codon
DAT A AV A ILABILITY readthrough in Drosophila melanogaster. Elife , 2 , e01179.
7. Driscoll,D.M. and Copeland,P.R. (2003) Mechanism and regulation
eCLIP-seq data was deposited at the GEO (GSE206674). of selenoprotein synthesis. Annu. Rev. Nutr. , 23 , 17–40.
UCSC Browser tracks for the analyzed data can be 8. Leinfelder,W., Zehelein,E., Mandrand-Berthelot,M.A. and B o¨ck,A.
(1988) Gene for a novel tRNA species that accepts L-serine and
accessed at: https://genome.ucsc.edu/s/jwang95070/
cotranslationally inserts selenocysteine. Nature , 331 , 723–725.
hg38 eCLIP skipper 2.24.23 . Ribosome profiling data
9. Wang,C., Guo,Y., Tian,Q., Jia,Q., Gao,Y., Zhang,Q., Zhou,C. and
can be accessed at the GEO (GSE230349). Xie,W. (2015) SerRS-tRNASec complex structures rev e al mechanism
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
10780 Nucleic Acids Research, 2023, Vol. 51, No. 19
of the first step in selenocysteine biosynthesis. Nucleic Acids Res. , 43 , 33. Dobin,A., Davis,C.A., Schlesinger,F., Drenkow,J., Zaleski,C., Jha,S.,
10534–10545. Batut,P., Chaisson,M. and Gingeras,T.R. (2013) STAR: ultrafast
10. Carlson,B.A., Xu,X.-M., Kryukov,G.V., Rao,M., Berry,M.J., univ e rsal RNA-seq aligner. Bioinformatics , 29 , 15–21.
Gladyshev,V.N. and Hatfield,D.L. (2004) Identification and 34. Liu,D. (2019) Algorithms for efficiently collapsing reads with Unique
characterization of phosphoseryl-tRNA[Ser]Sec kinase. Proc. Natl. Molecular Identifiers. Peer J. , 7 , e8275.
Acad. Sci. U.S.A. , 101 , 12848–12853. 35. Robinson,J.T., Thorvaldsd o´ttir,H., Winckler,W., Guttman,M.,
11. Pa lioura,S., Sherre r,R.L., Steitz,T.A., S o¨ll,D. and Simonovic,M. Lander,E.S., Getz,G. and Mesirov,J.P. (2011) Integrativ e genomics
(2009) The human SepSecS-tRNASec complex reveals the viewer. Nat. Biotechnol. , 29 , 24–26.
mechanism of selenocysteine formation. Science , 325 , 321–325. 36. Zhou,Y., Zhou,B., Pache,L., Chang,M., Khodabakhshi,A.H.,
12. Lescure,A., Fagegaltier,D., Carbon,P. and Krol,A. (2002) Protein Tanaseichuk,O., Benner,C. and Chanda,S.K. (2019) Metascape
factors mediating selenoprotein synthesis. Curr. Protein Pept. Sci. , 3 , provides a biologist-oriented re sourc e for the analysis of systems-lev e l
143–151. datasets. Nat. Commun. , 10 , 1523.
13. Copeland,P.R., Fletcher,J.E., Carlson,B.A., Hatfield,D.L. and 37. Ingolia,N.T., Brar,G.A., Rouskin,S., McGeachy,A.M. and
Driscoll,D.M. (2000) A novel RNA binding protein, SBP2, is Weissman,J.S. (2012) The ribosome profiling strategy for monitoring
re quire d for the translation of mammalian selenoprotein mRNAs. translation in vivo by deep sequencing of ribosome-protected mRNA
EMBO J. , 19 , 306–314. fragments. Nat. Protoc. , 7 , 1534–1550.
14. Mort,M., Ivanov,D., Cooper,D.N. and Chuzhanova,N.A. (2008) A 38. Ishimura,R., Nagy,G., Dotu,I., Zhou,H., Yang,X.-L., Schimmel,P.,
meta-analysis of nonsense mutations causing human genetic disease. Senju,S., Nishimura,Y., Chuang,J.H. and Ackerman,S.L. (2014) RNA
Hum. Mutat. , 29 , 1037–1047. function. Ribosome stalling induced by mutation of a CNS-specific
15. Atkinson,J. and Martin,R. (1994) Mutations to nonsense codons in tRNA causes neurodegeneration. Science , 345 , 455–459.
human genetic disease: implications for gene therapy by nonsense 39. Langmead,B. and Salzberg,S.L. (2012) Fast gapped-read alignment
suppressor tRNAs. Nucleic Acids Res. , 22 , 1327–1334. with Bowtie 2. Nat. Methods , 9 , 357–359.
16. Chen,W.-C. , Lin,S.-C. and Lee,J.-C. (2011) A novel nonsense 40. Lauria,F., Tebaldi,T., Bernab o`,P., Groen,E.J.N., Gillingwater,T.H.
mutation of MSH2 gene in a Taiwanese family with hereditary and Viero,G. (2018) riboWaltz: optimization of ribosome P-site
nonpolyposis colorectal cancer. Kaohsiung J. Med. Sci. , 27 , 68–71. positioning in ribosome profiling data. PLoS Comput. Biol. , 14 ,
17. Keeling,K.M., Xue,X., Gunn,G. and Bedwell,D.M. (2014) e1006169.
Therapeutics based on stop codon readthrough. Annu. Rev. Genomics 41. Hellman,L.M. and Fried,M.G. (2007) Electrophoretic mobility shift
Hum. Genet. , 15 , 371–394. assay (EMSA) for detecting protein-nucleic acid interactions. Nat.
18. Manuva khova ,M., Keeling,K. and Bedwell,D.M. (2000) Protoc. , 2 , 1849–1861.
Aminog ly coside antibiotics mediate context-dependent suppression 42. Chan,P. P. and Lowe,T.M. (2009) GtRNAdb: a database of transfer
of termination codons in a mammalian translation system. RNA , 6 , RNA genes detected in genomic sequence. Nucleic Acids Res. , 37 ,
1044–1055. D93–D97.
19. Porter,J. J. , Heil,C.S. and Lueck,J.D. (2021) Therapeutic promise of 43. Chan,P. P. and Lowe,T.M. (2016) GtRNAdb 2.0: an expanded
engineered nonsense suppressor tRNAs. Wiley Interdiscip. Rev. RNA , database of transfer RNA genes identified in complete and draft
12 , e1641. genomes. Nucleic Acids Res. , 44 , D184–189.
20. Wang,J., Zhang,Y., Mendonca,C.A., Yukselen,O., Muneeruddin,K., 44. Reinkemeier,C.D., Girona,G.E. and Lemke,E.A. (2019) Designer
Ren,L., Liang,J., Zhou,C., Xie,J., Li,J. et al. (2022) AAV-deliv e red membraneless organelles enable codon reassignment of selected
suppressor tRNA overcomes a nonsense mutation in mice. Nature , mRNAs in eukaryotes. Science , 363 , eaaw2644.
604 , 343–348. 45. Xu,X., Shi,Y., Zhang,H.-M., Swindell,E.C., Marshall,A.G., Guo,M.,
21. Lueck,J. D., Yoon,J. S., Perales-Puchalt,A., Mackey,A.L., Infield,D.T., Kishi,S. and Yang,X.-L. (2012) Unique domain appended to
Behlke,M.A., Pope,M.R., Weiner,D.B., Skach,W.R., McCray,P.B. vertebrate tRNA synthetase is essential for vascular development.
et al. (2019) Engineered transfer RNAs for suppression of premature Nat. Commun. , 3 , 681.
termination codons. Nat. Commun. , 10 , 822. 46. Lenhard,B., Orellana,O., Ibba,M. and Weygand-Durasevi c´,I. (1999)
22. Wangen,J.R. and Green,R. (2020) Stop codon context influences tRNA recog nition and evolution of determinants in seryl-tRNA
genome-wide stimulation of termination codon readthrough by synthesis. Nucleic Acids Res. , 27 , 721–729.
aminog ly cosides. Elife , 9 , e52611. 47. Holman,K.M., Puppala,A.K., Lee,J.W., Lee,H. and Simonovi c´,M.
23. Ferra ra ,N. (2002) VEGF and the quest for tumour angiogenesis (2017) Insights into substrate promiscuity of human seryl-tRNA
factors. Nat. Rev. Cancer , 2 , 795–803. synthetase. RNA , 23 , 1685–1699.
24. Ferra ra ,N., Gerber,H.-P. and LeCouter,J. (2003) The biology of 48. Fukui,H., Hanaoka,R. and Kawahara,A. (2009) Noncanonical
VEGF and its receptors. Nat. Med. , 9 , 669–676. activity of seryl-tRNA synthetase is involved in vascular
25. Eswarappa,S.M., Potdar,A.A., Koch,W.J., Fan,Y., Vasu,K., dev e lopment. Circ . Res. , 104 , 1253–1259.
Lindner,D., Willard,B., Graham,L.M., DiCorleto,P.E. and Fox,P.L. 49. Kirchner,S., Cai,Z., Rauscher,R., Kastelic,N., Anding,M., Czech,A.,
(2014) Programmed translational readthrough generates Kleizen,B., Ostedgaard,L.S., Braakman,I., Sheppard,D.N. et al.
antiangiogenic VEGF-Ax. Cell , 157 , 1605–1618. (2017) Alteration of protein function by a silent polymorphism linked
26. Eswarappa,S.M. and Fox,P.L. (2015) Antiangiogenic VEGF-Ax: a to tRNA abundance. PLoS Biol. , 15 , e2000779.
new participant in tumor angiogenesis. Cancer Res. , 75 , 2765–2769. 50. Dobosz-Bartoszek,M., Pinkerton,M.H., Otwinowski,Z.,
27. Xin,H., Zhong,C., Nudleman,E. and Ferra ra ,N. (2016) Evidence for Chakravarthy,S., S o¨ll,D., Copeland,P.R. and Simonovi c´,M. (2016)
pro-angiogenic functions of VEGF-Ax. Cell , 167 , 275–284. Crystal structures of the human elongation factor eEFSec suggest a
28. Morgenstern,J.P. and Land,H. (1990) Advanced mammalian gene non-canonical mechanism for selenocysteine incorporation. Nat.
tra nsfer: high titre retroviral vectors with multiple drug selection Commun. , 7 , 12941.
markers and a complementary helper-free packaging cell line. Nucleic 51. Hilal,T., Killam,B.Y., Grozdanovi c´,M., Dobosz-Bartoszek,M.,
Acids Res. , 18 , 3587–3596. Loerke,J. , Bu¨rger,J. , Mielke ,T., Copeland,P.R., Simonov i c´,M. and
29. Shi,Y., Wei,N. and Yang,X.-L. (2017) Studying nuclear functions of Spahn,C.M.T. (2022) Structure of the mammalian ribosome as it
aminoacyl tRNA synthetases. Methods , 113 , 105–110. decodes the selenocysteine UGA codon. Science , 376 , 1338–1343.
30. Darnell,R. (2012) CLIP (cross-linking and immunoprecipitation) 52. Ligtenberg,M.J.L., Kuiper,R.P., Chan,T.L., Goossens,M.,
identification of RNAs bound by a specific protein. Cold Spring Harb Hebeda,K.M., Voorendt,M., Lee,T.Y.H., Bodmer,D., Hoenselaar,E.,
Protoc , 2012 , 1146–1160. Hendriks-Cornelissen,S.J.B. et al. (2009) Heritable somatic
31. Boyle,E.A., Her,H.-L., Mueller,J.R., Nguyen,G. G. and Yeo,G.W. methylation and inactivation of MSH2 in families with Lynch
(2022) Skipper analysis of RNA-protein interactions highlights syndrome due to deletion of the 3’ exons of TACSTD1. Nat. Genet. ,
depletion of genetic variation in translation factor binding sites. Cell 41 , 112–117.
Genomics , 3 , 100317. 53. Gonzalez-Flores,J.N., Shetty,S.P., Dubey,A. and Copeland,P.R.
32. Jiang,H., Lei,R., Ding,S.-W. and Zhu,S. (2014) Skewer: a fast and (2013) The molecular biology of selenocysteine. Biomol Concepts , 4 ,
accurate adapter trimmer for next-generation sequencing paired-end 349–365.
reads. BMC Bioinformatics , 15 , 182.
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
Nucleic Acids Research, 2023, Vol. 51, No. 19 10781
54. Oudouhou,F., Casu,B., Dopgwa Puemi,A.S., Sygusch,J. and 62. Putney,S.D. and Schimmel,P. (1981) An aminoacyl tRNA synthetase
Baron,C. (2017) Analysis of novel interactions between components binds to a specific DNA sequence and regulates its gene transcription.
of the selenocysteine biosynthesis pathway, SEPHS1, SEPHS2, Nature , 291 , 632–635.
SEPSECS, and SECp43. Bioch emistry , 56 , 2261–2270. 63. Jones,J.A., Wei,N., Cui,H., Shi,Y., Fu,G., Rauniyar,N., Shapiro,R.,
55. Howard,M.T. and Copeland,P.R. (2019) New directions for Morodomi,Y., Berenst,N., Dumitru,C.D. et al. (2023) Nuclear
understanding the codon redefinition required for selenocysteine translocation of an aminoacyl-tRNA synthetase may mediate a
incorporation. Biol Trace Elem Res , 192 , 18–25. chronic “integrated stress response”. Cell Rep. , 42 , 112632.
56. Dabrow ski,M., Bukow y-Bieryllo,Z. and Zietkiewicz,E. (2015) 64. Normanly,J., Ogden,R.C., Horvath,S.J. and Abelson,J. (1986)
Translational readthrough potential of natural termination codons in Changing the identity of a transfer RNA. Nature , 321 , 213–219.
eucaryotes–the impact of RNA sequence. RNA Biol. , 12 , 950–958. 65. Biou,V., Yaremchuk,A., Tukalo,M. and Cusack,S. (1994) The 2.9 A
57. Paleskava,A., Konev e ga,A.L. and Rodnina,M.V. (2010) crystal structure of T. thermophilus seryl-tRNA synthetase
Thermodynamic and kinetic framew ork of selenocysteyl-tRNASec complexed with tRNA(Ser). Science , 263 , 1404–1410.
recognition by elongation factor SelB. J. Biol. Chem. , 285 , 3014–3020. 66. Guo,M., Schimmel,P. and Yang,X.L. (2010) Functional expansion of
58. Ivanov,P., Emara,M.M., Villen,J., Gygi,S.P. and Anderson,P. (2011) human tRNA synthetases achiev e d by structural inventions. FEBS
Angiog enin-induced tRNA fra gments inhibit tra nslat ion initiat ion. Lett. , 584 , 434–42.
Mol. Cell , 43 , 613–623. 67. Shi,Y., Xu,X., Zhang,Q., Fu,G., Mo,Z., Wang,G.S., Kishi,S. and
59. Schwenzer,H., Ju¨hling,F., Chu,A., Pallett,L.J., Baumert,T.F., Yang,X.-L. (2014) tRNA synthetase counteracts c-Myc to develop
Maini,M. and Fassati,A. (2019) Oxidativ e stress triggers selectiv e functional vasculature. Elife , 3 , e02349.
tRNA retrog ra de tra nsport in human cells during the integra ted 68. Loughran,G., Jungreis,I., Tzani,I., Power,M., Dmitriev,R.I.,
stre ss re sponse. Cell Rep. , 26 , 3416–3428. Ivanov,I.P., Kellis,M. and Atkins,J.F. (2018) Stop codon readthrough
60. Jeong,S. J., Park,S. , Nguyen,L.T., Hwang,J., Lee,E.-Y., Giong,H.-K., generates a C-terminally extended variant of the human vitamin D
Lee,J.-S., Yoon,I., Lee,J.-H., Kim,J.H. et al. (2019) A threonyl-tRNA receptor with reduced calcitriol response. J. Biol. Chem. , 293 ,
synthetase-mediat ed translat ion initiat ion machinery. Nat. Commun. , 4434–4444.
10 , 1357.
61. Mukhopadhyay,R., Jia,J., Arif,A., Ray,P.S. and Fox,P.L. (2009) The
GAIT system: a gatekeeper of inflammatory gene expression. Trends
Biochem. Sci. , 34 , 324–331.
(cid:2) C The Author(s) 2023. Published by Oxford University Press on behalf of Nucleic Acids Research.
This is an Open Access article distributed under the terms of the Creativ e Commons Attribution-NonCommercial License
(http: // creativ e commons.org / licenses / by-nc / 4.0 / ), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work
is properly cited. For commercial re-use, please contact journals. permissions@oup. com
Downloaded
from
https://academic.oup.com/nar/article/51/19/10768/7280545
by
guest
on
07
August
2025
